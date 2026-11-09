#!/usr/bin/env python3
"""Independent stdlib-only verifier: no imports from the experiment/exporter."""
import argparse
import collections
import csv
import hashlib
import io
import json
import random
import re
from decimal import Decimal
from pathlib import Path, PurePosixPath


def sha(data):
    return hashlib.sha256(data).hexdigest()


def check(value, message):
    if not value:
        raise ValueError(message)


def load(root, name):
    p = PurePosixPath(name)
    check(not p.is_absolute() and '..' not in p.parts, 'Unsafe public path')
    return json.loads((root / name).read_bytes())


def csv_rows(path):
    return list(csv.DictReader(io.StringIO(path.read_text())))


def set_pointer(obj, path, replacement, expected):
    keys = path.lstrip('/').split('/')
    keys = [k.replace('~1', '/').replace('~0', '~') for k in keys]
    parent = obj
    for k in keys[:-1]:
        parent = parent[int(k)] if isinstance(parent, list) else parent[k]
    k = int(keys[-1]) if isinstance(parent, list) else keys[-1]
    check(sha(parent[k].encode()) == expected, 'Redaction original-value hash mismatch')
    parent[k] = replacement


def verify_derivation(source, output, desc, original_roots):
    ops = desc['operations']
    kind = next((o for o in ops if o.get('operation') == 'omit_full_source_body'), None)
    if kind:
        before = json.loads(source); after = json.loads(output)
        text = before['messages'][0]['content']; start, end = kind['span_utf8_bytes']; raw = text.encode()
        check(sha(raw[start:end]) == kind['omitted_sha256'], 'Omitted body hash/span mismatch')
        before['messages'][0]['content'] = (raw[:start] + kind['replacement'].encode() + raw[end:]).decode()
        check(before == after, 'Researcher derivative changes more than the declared source span')
        return
    changes = [o for o in ops if o.get('operation') == 'replace_local_repository_paths']
    if not changes:
        return  # Other derived files are independently checked below.
    suffix = Path(desc['path']).suffix
    if suffix == '.json':
        before = json.loads(source); after = json.loads(output)
    elif suffix == '.csv':
        before = list(csv.DictReader(io.StringIO(source.decode()))); after = list(csv.DictReader(io.StringIO(output.decode())))
    elif suffix == '.jsonl':
        before = [json.loads(x) for x in source.splitlines()]; after = [json.loads(x) for x in output.splitlines()]
    else:
        text = source.decode()
        for old in sorted(original_roots, key=len, reverse=True):
            text = text.replace(old+'/data/exploratory/runs/', 'runs/').replace(old+'/data/studies/', 'studies/')
            text = text.replace(old+'/', '<LOCAL_REPOSITORY>/')
            if text == old:
                text = '<LOCAL_REPOSITORY>'
        check(text.encode() == output, 'Undeclared metadata text change')
        return
    for o in changes:
        set_pointer(before, o['pointer'], o['replacement'], o['original_value_sha256'])
    check(before == after, 'Undeclared structured metadata change')


def status_and_actions(root, rec):
    base = rec['publication_path']; state = load(root, base+'/state.json')
    sidefile = root/base/'sample_state.json'; side = json.loads(sidefile.read_bytes()) if sidefile.exists() else {}
    state_status = 'prepared'
    if state.get('researcher_status') == 'success':
        state_status = 'researcher_complete'
    original = load(root, rec['classification']) if rec['classification'] else None
    if state.get('prisoner_status') == 'success':
        check(original is not None, 'Successful prisoner state lacks outcome')
        state_status = 'pending_judge' if original.get('needs_review') else 'complete'
    if any(state.get(k+'_status') in ('failed', 'preflight_failed', 'attempted') for k in ('researcher', 'prisoner')):
        state_status = 'failed'
    actions = original.get('enacted_actions') if original else None
    if rec['adjudication']:
        judged = load(root, rec['adjudication']); actions = judged['adjudicated_actions']
        if judged.get('needs_human_review'):
            state_status = 'needs_human_review'
        elif all(x in ('SUBMIT', 'WITHHOLD') for x in actions):
            state_status = 'complete'
        else:
            state_status = 'resolved_unscored'
        for role, j in judged['judgements'].items():
            idx = 0 if role == 'a' else 1
            expected = 'WITHHOLD' if (j['intent'], j['disclosure']) == ('TRIED_COOPERATE', 'NO') else ('SUBMIT' if (j['intent'], j['disclosure']) == ('TRIED_DEFECT', 'YES') else None)
            check(actions[idx] == expected, 'Judge label/action inconsistency')
        score = judged.get('adjudicated_score')
    else:
        score = original.get('enacted_score') if original else None
    if side.get('judge_status') == 'attempted' and not rec['adjudication']:
        state_status = 'failed'
    if side.get('error'):
        state_status = 'failed'
    check(state_status == rec['status'], 'Status differs from saved state/outcomes: '+rec['sample_id'])
    if state_status != 'complete':
        check(not rec['pair_outcome'], 'Unscored scenario has a scored outcome')
        return state_status, None
    check(actions and len(actions) == 2 and all(x in ('SUBMIT', 'WITHHOLD') for x in actions), 'Invalid complete actions')
    outcome = ''.join('C' if x == 'WITHHOLD' else 'D' for x in actions)
    check(outcome == rec['pair_outcome'], 'Outcome/action mismatch')
    check(actions == [rec['row']['final_a'], rec['row']['final_b']], 'Index/classification mismatch')
    years = {'CC': [2, 2], 'CD': [5, 0], 'DC': [0, 5], 'DD': [4, 4]}[outcome]
    check(score and score['years'] == years and score['utilities'] == [5-y for y in years], 'Payoff calculation mismatch')
    return state_status, outcome


def verify(root, source_root=None):
    root = Path(root).resolve(); source_root = Path(source_root).resolve() if source_root else None
    manifest = load(root, 'MANIFEST.json'); files = {x['path']: x for x in manifest['files']}
    check(len(files) == len(manifest['files']), 'Duplicate manifest paths')
    actual = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
    check(actual == set(files) | {'MANIFEST.json', 'SCAN.json'}, 'Unexpected or missing exported files')
    original_roots = set()
    if source_root:
        for identity in manifest['studies']:
            path = source_root/'data/studies'/identity['name']/'study.json'
            original_roots.add(json.loads(path.read_bytes())['repo_root'])
        for origin in manifest['input_files']:
            p = source_root/origin['path']
            check(p.is_file() and sha(p.read_bytes()) == origin['sha256'], 'Original input changed: '+origin['path'])
    for name, desc in files.items():
        p = root/name; check(p.is_file() and not p.is_symlink(), 'Missing/symlink payload')
        data = p.read_bytes()
        check(len(data) == desc['bytes'] and sha(data) == desc['sha256'], 'Export hash mismatch: '+name)
        if desc['evidence'] == 'verbatim':
            check(len(desc['inputs']) == 1 and desc['inputs'][0]['sha256'] == desc['sha256'] and not desc['operations'], 'False verbatim designation')
        if source_root and len(desc['inputs']) == 1:
            origin = (source_root/desc['inputs'][0]['path']).read_bytes()
            if desc['evidence'] == 'verbatim':
                check(origin == data, 'Verbatim bytes changed')
            else:
                verify_derivation(origin, data, desc, original_roots)
    scan = load(root, 'SCAN.json')
    check(scan['blocking_findings'] == 0, 'Export scan reports a blocking issue')
    reports = []
    for identity in manifest['studies']:
        name = identity['name']; base = 'studies/'+name; refs = root/base/'reference'
        expected = load(root, base+'/reference/summary.json')
        roster = load(root, base+'/index.json')
        check(len(roster) == expected['total_samples'], 'Scenario roster count mismatch')
        check(len({r['sample_id'] for r in roster}) == len(roster), 'Duplicate scenario identity')
        decisions = {(d['sample_id'], d['role']): d for d in csv_rows(refs/'decisions.csv')}
        all_records = {}
        cells = {}; statuses = collections.Counter(); costs = Decimal(0); attempted = priced = 0; prompt = completion = 0
        stage_counts = collections.Counter(); seen_calls = set(); failed = []
        for entry in roster:
            rec = load(root, entry['record']); pilot = load(root, rec['publication_path']+'/pilot.json')
            all_records[rec['sample_id']] = rec
            check(rec['settings'] == pilot['settings'] and rec['source_identity'] == pilot['source_identity'], 'Frozen model/source metadata differs')
            check(rec['template_hashes'] == pilot['template_hashes'], 'Template hashes differ')
            check(rec['researcher_effort'] == rec['settings']['researcher']['effort'] and rec['prisoner_effort'] == rec['settings']['prisoner']['effort'], 'Requested effort differs')
            status, outcome = status_and_actions(root, rec); statuses[status] += 1
            c = cells.setdefault(rec['cell_id'], {'planned': 0, 'outcomes': collections.Counter(), 'status': collections.Counter(), 'cost': Decimal(0), 'fractions': [], 'calls': 0, 'priced': 0, 'essays_measured': 0, 'essays_above_target': 0})
            c['planned'] += 1; c['status'][status] += 1
            if outcome:
                c['outcomes'][outcome] += 1; c['fractions'].append(outcome.count('C')/2)
                for role in ('a', 'b'):
                    check(decisions[(rec['sample_id'], role)]['final_action'] == rec['row']['final_'+role], 'Decisions CSV mismatch')
            if status == 'failed':
                failed.append(rec['sample_id'])
            if rec['essay']:
                essay = (root/rec['essay']).read_bytes(); check(sha(essay) == rec['essay_sha256'], 'Frozen essay hash mismatch')
            else:
                essay = None
            prisoner_messages = []
            paircost = Decimal(0)
            for call in rec['calls']:
                check(call['request'] not in seen_calls, 'Call assigned twice')
                seen_calls.add(call['request']); attempted += 1; c['calls'] += 1; stage_counts[call['stage']] += 1
                req = load(root, call['request'])
                if call['stage'] != 'researcher':
                    check(call['request_is_exact'] and files[call['request']]['evidence'] == 'verbatim', 'Nonexact prisoner/judge request')
                else:
                    check(not call['request_is_exact'] and 'SOURCE BODY OMITTED FROM PUBLICATION' in req['messages'][0]['content'], 'Unmarked/full researcher request')
                    check(call['original_request_sha256'] == files[call['request']]['inputs'][0]['sha256'], 'Original request hash differs')
                if call['stage'] in ('researcher', 'prisoner'):
                    setting = rec['settings'][call['stage']]
                    check(req['model'] == rec['model'] and req['reasoning']['effort'] == setting['effort'] and req['max_tokens'] == setting['max_tokens'], 'Model/effort/limit substitution')
                if call['stage'] == 'prisoner':
                    check(essay is not None and len(req['messages']) == 1 and req['messages'][0]['role'] == 'user', 'No essay or unexpected conversation history')
                    text = req['messages'][0]['content']; check(essay.decode() in text, 'Essay changed in prisoner input')
                    role = 'a' if call['call'] == 'call_0' else 'b'; case = pilot['scenario_record']; private = case['private_'+role]; evidence = case['evidence_'+role]
                    check(text.count(private) == 1 and text.count(evidence) == 2, 'Private observation/evidence count differs')
                    prisoner_messages.append(text.replace(private, '[PRIVATE]', 1).replace(evidence, '[EVIDENCE]'))
                if call['response']:
                    check(files[call['response']]['evidence'] == 'verbatim', 'Raw response modified')
                    response = load(root, call['response']); check(response['model'] == req['model'], 'Returned model differs')
                    if call['stage'] == 'researcher':
                        choice = response['choices'][0]; text = choice['message'].get('content')
                        if choice['finish_reason'] == 'stop' and isinstance(text, str) and text.strip():
                            c['essays_measured'] += 1
                            bound = rec['settings'].get('essay', {}).get('target_words', [2400, 3000])[1]
                            c['essays_above_target'] += len(text.split()) > bound
                    usage = response.get('usage') or {}; prompt += usage.get('prompt_tokens', 0); completion += usage.get('completion_tokens', 0)
                    if usage.get('cost') is not None:
                        cost = Decimal(str(usage['cost'])); costs += cost; c['cost'] += cost; paircost += cost; priced += 1; c['priced'] += 1
                    if call['output']:
                        check(files[call['output']]['evidence'] == 'verbatim', 'Output modified')
                        content = response['choices'][0]['message']['content']; check(content.encode() == (root/call['output']).read_bytes(), 'Output/raw-response disagreement')
            if len(prisoner_messages) == 2:
                check(prisoner_messages[0] == prisoner_messages[1], 'Pair differs outside intended private fields')
            if status == 'prepared':
                check(not rec['calls'], 'Prepared scenario has attempted calls')
            check(paircost == Decimal(rec['row']['reported_provider_usd']), 'Per-scenario cost mismatch')
        check(dict(statuses) == expected['status_counts'], 'Study status counts mismatch')
        check(sum(statuses.values()) == len(roster), 'Scenario accounting mismatch')
        failure_rows = csv_rows(refs/'failures.csv')
        check(len(failed) == len(failure_rows) and set(failed) == {f['sample_id'] for f in failure_rows}, 'Failure CSV identities mismatch')
        for f in failure_rows:
            rec = all_records[f['sample_id']]
            for key in ('failure_category', 'failure_stage', 'failed_call'):
                if key in f:
                    check(f[key] == rec['row'][key], 'Failure classification/index mismatch')
            category = f.get('failure_category')
            calls = [c for c in rec['calls'] if c['stage'] == f.get('failure_stage') and c['call'] == f.get('failed_call')]
            if calls and calls[0]['response']:
                response = load(root, calls[0]['response']); choice = response['choices'][0]; msg = choice['message']
                if category == 'output_token_limit':
                    check(choice['finish_reason'] in ('length', 'max_tokens'), 'Token-limit failure lacks exhausted-output stop')
                elif category == 'refusal':
                    check(choice['finish_reason'] == 'content_filter' or msg.get('refusal') or choice.get('native_finish_reason') == 'refusal', 'Refusal lacks saved provider evidence')
                elif category == 'essay_size_limit':
                    text = msg['content']; limits = rec['settings']['essay']
                    encoded = json.dumps(text, ensure_ascii=False, separators=(',', ':')).encode()
                    check(len(text.split()) > limits['max_words'] or len(encoded) > limits['max_json_bytes'], 'Essay-size failure is within both hard bounds')
        usage = expected['provider_usage']
        times = collections.defaultdict(float)
        if (refs/'events.jsonl').exists():
            events = [json.loads(x) for x in (refs/'events.jsonl').read_bytes().splitlines()]
            for e in events:
                if e['event'] == 'study_cell_finished':
                    times[e['cell']] += e['elapsed_seconds']
            check(round(sum(times.values()), 3) == usage['recorded_execution_seconds'], 'Aggregate cell time differs from event log')
            finished = [e['elapsed_seconds'] for e in events if e['event'] == 'study_run_finished']
            check((finished[-1] if finished else None) == usage.get('last_run_wall_seconds'), 'Last completed invocation time differs')
        check((attempted, priced, attempted-priced) == (usage['attempted_calls'], usage['priced_calls'], usage['unpriced_calls']), 'Call/unknown-cost counts mismatch')
        check(costs == Decimal(usage['reported_provider_usd']), 'Study cost mismatch')
        check(prompt == usage['prompt_tokens'] and completion == usage['completion_tokens'], 'Token totals mismatch')
        cs = csv_rows(refs/'summary.csv')
        check(len(cs) == len(cells), 'Cell roster mismatch')
        for ref in cs:
            c = cells[ref['cell_id']]; counts = c['outcomes']; n = sum(counts.values())
            check(c['planned'] == int(ref['samples_planned']) and n == int(ref['complete_pairs']), 'Cell denominator mismatch')
            for x in ('CC', 'CD', 'DC', 'DD'):
                check(counts[x] == int(ref['outcome_'+x]), 'Cell outcome mismatch')
            rate = sum(c['fractions'])/n if n else None
            check((rate is None and ref['cooperation_rate']=='') or (rate is not None and abs(rate-float(ref['cooperation_rate']))<1e-12), 'Cell cooperation mismatch')
            for status in ('prepared', 'failed', 'needs_human_review', 'resolved_nonaction', 'resolved_unscored'):
                check(c['status'][status] == int(ref['status_'+status]), 'Cell status mismatch')
            check(c['cost'] == Decimal(ref['reported_provider_usd']) and c['priced'] == int(ref['priced_calls']), 'Cell cost mismatch')
            if times:
                check(abs(times[ref['cell_id']] - float(ref['recorded_execution_seconds'])) < 1e-8, 'Cell execution time differs')
            for key in ('essays_measured', 'essays_above_target'):
                if key in ref:
                    check(c[key] == int(ref[key]), 'Essay target metric differs: '+ref['cell_id'])
            if n >= 10:
                rng = random.Random(int(sha(ref['cell_id'].encode())[:16],16)); v=c['fractions']
                bs = sorted(sum(v[rng.randrange(n)] for _ in range(n))/n for _ in range(2000))
                check([bs[50], bs[1949]] == [float(ref['pair_bootstrap_ci_low']), float(ref['pair_bootstrap_ci_high'])], 'Saved pair-bootstrap interval differs')
            saved = next(x for x in expected['cell_summaries'] if x['cell_id']==ref['cell_id'])
            for key in ('complete_pairs', 'cooperation_rate', 'pair_bootstrap_ci_low', 'pair_bootstrap_ci_high', 'reported_provider_usd'):
                check(str(saved[key]) == ref[key] or saved[key] is None and ref[key]=='', 'JSON/CSV summary disagreement')
        reports.append({'study': name, 'scenario_records': len(roster), 'status_counts': dict(statuses), 'cells': len(cells),
                        'attempted_calls': attempted, 'raw_responses_priced': priced, 'unknown_prices': attempted-priced,
                        'stage_calls': dict(stage_counts), 'reported_provider_usd': str(costs)})
    return {'verified': True, 'payload_files': len(files), 'private_input_hashes_checked': len(manifest['input_files']) if source_root else 0, 'studies': reports}


def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('publication', type=Path); p.add_argument('--source-root', type=Path)
    p.add_argument('--out', type=Path); args=p.parse_args()
    try:
        result=verify(args.publication,args.source_root)
    except (ValueError, KeyError, OSError, TypeError) as e:
        p.exit(1,'VERIFICATION FAILED: '+str(e)+'\n')
    text=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.out:args.out.write_text(text)
    print(text,end='')


if __name__=='__main__':main()
