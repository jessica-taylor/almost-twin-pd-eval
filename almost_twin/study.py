"""One frozen matrix of auditable full-scenario batches.

Study preparation uses only unbilled capability discovery. Generation remains
in batch.run, with its existing approval, budget, hash, and no-retry rules.
The prisoner roles and observation assignments are intentionally fixed.
"""

import csv
import fcntl
import io
import json
import random
import re
import uuid
from collections import Counter
from decimal import Decimal
from pathlib import Path
from types import SimpleNamespace

from . import batch
from .common import EvalError, append_json, encoded, load_yaml, read, sha, utc, write_json
from .judge import judge_messages
from .preflight import choose_endpoint, estimate_price
from .prompts import assignment, cases, prisoners, researcher
from .router import Budget, snapshot, validate_settings
from .sources import load_source


THEORIES = {'cdt_wikipedia', 'edt_wikipedia', 'fdt_eq4', 'fdt_policy'}
SPEC_FIELDS = {'schema_version', 'name', 'exploratory', 'assignments', 'models',
               'researcher_efforts', 'prisoner_efforts', 'count_per_cell', 'scenario',
               'researcher_max_tokens', 'prisoner_max_tokens', 'judge', 'budgets',
               'temperature', 'seed_base'}
MODEL_FIELDS = {'id', 'provider_tag', 'researcher_efforts', 'prisoner_efforts',
                'allow_unverified_effort'}
JUDGE_FIELDS = {'enabled', 'model', 'provider_tag', 'effort', 'max_tokens',
                'allow_unverified_effort'}
BUDGET_FIELDS = {'max_calls', 'max_usd', 'judge_max_calls', 'judge_max_usd'}


def _keys(value, allowed, label):
    if not isinstance(value, dict):
        raise EvalError(f'{label} must be a mapping')
    unknown = set(value) - allowed
    if unknown:
        raise EvalError(f'Unknown {label} keys: {sorted(unknown)}')


def _positive_integer(value, field):
    if not isinstance(value, int) or isinstance(value, bool) or value < 1:
        raise EvalError(f'{field} must be a positive integer')
    return value


def _positive_usd(value, field):
    try:
        amount = Decimal(str(value))
    except Exception as exc:
        raise EvalError(f'{field} must be a positive finite USD amount') from exc
    if not amount.is_finite() or amount <= 0:
        raise EvalError(f'{field} must be a positive finite USD amount')
    return str(amount)


def _efforts(value, label):
    allowed = {'none', 'minimal', 'low', 'medium', 'high', 'xhigh', 'max'}
    if not isinstance(value, list) or not value or len(set(map(str, value))) != len(value):
        raise EvalError(f'{label} must be a nonempty list without duplicates')
    if any(not isinstance(e, str) or e not in allowed for e in value):
        raise EvalError(f'{label} contains an unknown reasoning effort')
    return value


def load_spec(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    spec = load_yaml(path)
    _keys(spec, SPEC_FIELDS, 'study specification')
    if spec.get('schema_version') != 1 or spec.get('exploratory') is not True:
        raise EvalError('Only schema_version=1 exploratory=true study specifications are supported')
    if not isinstance(spec.get('name'), str) or not spec['name'].strip():
        raise EvalError('Study name must be nonempty')
    assignments = spec.get('assignments')
    if (not isinstance(assignments, list) or not assignments or
        any(not isinstance(value, str) for value in assignments) or
        len(set(assignments)) != len(assignments)):
        raise EvalError('Study assignments must be a nonempty list without duplicates')
    if any(theory not in THEORIES for theory in assignments):
        raise EvalError(f'Unknown study assignment; choose from {sorted(THEORIES)}')
    if not isinstance(spec.get('models'), list) or not spec['models']:
        raise EvalError('Study models must be a nonempty list')
    researcher_efforts = _efforts(spec.get('researcher_efforts', ['low']), 'researcher_efforts')
    prisoner_efforts = _efforts(spec.get('prisoner_efforts', ['low']), 'prisoner_efforts')
    models = []
    for entry in spec['models']:
        _keys(entry, MODEL_FIELDS, 'model')
        ident = entry.get('id')
        if not isinstance(ident, str) or not re.fullmatch(r'[a-zA-Z0-9_.-]+/[a-zA-Z0-9_.:-]+', ident):
            raise EvalError(f'Use a specific author/model identifier: {ident!r}')
        for key in ('provider_tag', 'allow_unverified_effort'):
            if entry.get(key) is not None and (not isinstance(entry[key], str) or not entry[key].strip()):
                raise EvalError(f'Invalid model {ident} {key}')
        models.append({**entry,
            'researcher_efforts': _efforts(entry.get('researcher_efforts', researcher_efforts), f'{ident}.researcher_efforts'),
            'prisoner_efforts': _efforts(entry.get('prisoner_efforts', prisoner_efforts), f'{ident}.prisoner_efforts')})
    if len({m['id'] for m in models}) != len(models):
        raise EvalError('Each study model must appear once; use effort lists instead of duplicate models')
    judge = spec.get('judge', {'enabled': True})
    _keys(judge, JUDGE_FIELDS, 'judge')
    judge = {'enabled': True, 'model': 'openai/gpt-6.1-sol', 'effort': 'low',
             'max_tokens': 1200, **judge}
    if not isinstance(judge['enabled'], bool):
        raise EvalError('judge.enabled must be Boolean')
    if judge['enabled']:
        if not isinstance(judge['model'], str) or judge['model'].count('/') != 1:
            raise EvalError('judge.model must be a specific author/model identifier')
        _efforts([judge['effort']], 'judge.effort')
        _positive_integer(judge['max_tokens'], 'judge.max_tokens')
        for key in ('provider_tag', 'allow_unverified_effort'):
            if judge.get(key) is not None and (not isinstance(judge[key], str) or not judge[key].strip()):
                raise EvalError(f'Invalid judge {key}')
    budgets = spec.get('budgets')
    _keys(budgets, BUDGET_FIELDS, 'budgets')
    for name in ('max_calls', 'judge_max_calls'):
        _positive_integer(budgets.get(name), f'budgets.{name}')
    for name in ('max_usd', 'judge_max_usd'):
        budgets[name] = _positive_usd(budgets.get(name), f'budgets.{name}')
    count = _positive_integer(spec.get('count_per_cell'), 'count_per_cell')
    if count > 10000:
        raise EvalError('count_per_cell exceeds the batch limit of 10000')
    for name, default in (('researcher_max_tokens', 12000), ('prisoner_max_tokens', 3000)):
        spec[name] = _positive_integer(spec.get(name, default), name)
    if not isinstance(spec.get('scenario', 't4_distinct_leads_001'), str):
        raise EvalError('scenario must be a case_id')
    if spec.get('seed_base') is not None and (not isinstance(spec['seed_base'], int) or spec['seed_base'] < 0):
        raise EvalError('seed_base must be a nonnegative integer when specified')
    spec.update(models=models, judge=judge, budgets=budgets,
                researcher_efforts=researcher_efforts, prisoner_efforts=prisoner_efforts,
                scenario=spec.get('scenario', 't4_distinct_leads_001'))
    return spec, raw


def _cells(spec):
    result = []
    for theory in spec['assignments']:
        for model in spec['models']:
            for researcher_effort in model['researcher_efforts']:
                for prisoner_effort in model['prisoner_efforts']:
                    number = len(result)
                    tag = re.sub(r'[^a-zA-Z0-9._-]+', '_', model['id'])
                    result.append({'id': f'{number:03d}_{theory}_{tag}_r{researcher_effort}_p{prisoner_effort}',
                                   'assignment': theory, 'model': model['id'],
                                   'provider_tag': model.get('provider_tag'),
                                   'researcher_effort': researcher_effort,
                                   'prisoner_effort': prisoner_effort,
                                   'allow_unverified_effort': model.get('allow_unverified_effort')})
    return result


def check(root, spec):
    """Validate the whole matrix and projected project budget; never POST."""
    root = Path(root).resolve()
    scenario = next((c for c in cases(root) if c['case_id'] == spec['scenario']), None)
    if scenario is None:
        raise EvalError(f'Unknown active scenario {spec["scenario"]!r}')
    sources = {}
    for theory in spec['assignments']:
        item = assignment(root, theory)
        source, info = load_source(root, item['source_id'])
        sources[theory] = researcher(root, item, source, info)
        prisoners(root, item, 'Synthetic preflight essay; no generation occurred.', scenario)
    caps = {}
    failures = []
    for model in spec['models']:
        try:
            caps[model['id']] = snapshot(model['id'])
        except EvalError as exc:
            failures.append({'cell': f'metadata:{model["id"]}', 'reason': str(exc)})
    judge = spec['judge']
    judge_cap = None
    if judge['enabled']:
        try:
            judge_cap = caps.get(judge['model']) or snapshot(judge['model'])
        except EvalError as exc:
            failures.append({'cell': 'judge metadata', 'reason': str(exc)})
    judge_settings = None
    judge_selection = None
    if judge['enabled'] and judge_cap is not None:
        judge_settings = {'model': judge['model'], 'provider_tag': judge.get('provider_tag'),
                          'judge': {'effort': judge['effort'], 'max_tokens': judge['max_tokens']},
                          'temperature': None, 'seed': None}
        if judge.get('allow_unverified_effort'):
            judge_settings['reasoning_override'] = {'efforts': [judge['effort']],
                                                    'reason': judge['allow_unverified_effort']}
        try:
            judge_settings, judge_selection = choose_endpoint(
                judge_settings, judge_cap, [('judge', judge_messages(root, 'Synthetic review evidence', 'pass'))],
                validate_settings)
        except EvalError as exc:
            failures.append({'cell': 'judge', 'reason': str(exc)})
    projected = Decimal(0)
    estimates = []
    validated_cells = []
    for cell in _cells(spec):
        if cell['model'] not in caps:
            failures.append({'cell': cell['id'], 'reason': 'Model metadata unavailable; cannot select a provider'})
            continue
        settings = {'model': cell['model'], 'provider_tag': cell['provider_tag'],
                    'researcher': {'effort': cell['researcher_effort'], 'max_tokens': spec['researcher_max_tokens']},
                    'prisoner': {'effort': cell['prisoner_effort'], 'max_tokens': spec['prisoner_max_tokens']},
                    'temperature': spec.get('temperature'), 'seed': None}
        if cell.get('allow_unverified_effort'):
            settings['reasoning_override'] = {'efforts': sorted({cell['researcher_effort'], cell['prisoner_effort']}),
                                              'reason': cell['allow_unverified_effort']}
        try:
            settings, selection = choose_endpoint(settings, caps[cell['model']],
                [('researcher', sources[cell['assignment']]),
                 ('prisoner', [{'role': 'user', 'content': ''}])], validate_settings)
            _, researcher_price = validate_settings(settings, caps[cell['model']], 'researcher',
                                                    sources[cell['assignment']])
            prisoner_payload, prisoner_price = validate_settings(settings, caps[cell['model']], 'prisoner',
                                                                 [{'role': 'user', 'content': ''}])
            endpoint = prisoner_price['endpoint']
            ceiling = min(endpoint['context_length'] - spec['prisoner_max_tokens'],
                          endpoint.get('max_prompt_tokens') or endpoint['context_length'])
            per_prisoner, _ = estimate_price(prisoner_payload, endpoint, caps[cell['model']]['model'],
                                            ceiling, spec['prisoner_max_tokens'])
            per_sample = Decimal(researcher_price['estimated_max_usd']) + 2 * Decimal(per_prisoner)
            projected += spec['count_per_cell'] * per_sample
            # These are the same three conservative reservations prepared by batch.
            estimates.extend([{'estimated_max_usd': researcher_price['estimated_max_usd']},
                              {'estimated_max_usd': per_prisoner},
                              {'estimated_max_usd': per_prisoner}] * spec['count_per_cell'])
            validated_cells.append({**cell, 'selected_provider_tag': settings['provider_tag'],
                                    'selection': selection, 'projected_usd': str(per_sample * spec['count_per_cell'])})
        except EvalError as exc:
            failures.append({'cell': cell['id'], 'reason': str(exc)})
    if not failures:
        budget = spec['budgets']
        try:
            Budget(root / 'data/budget.jsonl', budget['max_calls'], budget['max_usd']).check(estimates)
            if judge['enabled']:
                # Judge prompts depend on generated decisions, so only the
                # worst-case call count is reserved conceptually at preparation.
                possible = 2 * spec['count_per_cell'] * len(validated_cells)
                Budget(root / 'data/judge_budget.jsonl', budget['judge_max_calls'],
                       budget['judge_max_usd']).check([{'estimated_max_usd': '0'}] * possible)
        except EvalError as exc:
            failures.append({'cell': 'project-wide budget', 'reason': str(exc)})
    return {'schema_version': 1, 'checked_at_utc': utc(),
            'no_billable_requests': True, 'count_per_cell': spec['count_per_cell'],
            'expected_cells': len(_cells(spec)), 'validated_cells': validated_cells,
            'projected_researcher_prisoner_usd': str(projected),
            'projected_researcher_prisoner_calls': len(estimates),
            'possible_judge_calls': (2 * spec['count_per_cell'] * len(_cells(spec)) if judge['enabled'] else 0),
            'judge_selection': judge_selection, 'failures': failures}, caps, judge_cap


def _seal(path, data):
    write_json(path, data)
    path.with_suffix('.sha256').write_text(sha(path.read_bytes()) + '\n', encoding='utf-8')


def _study_code_sha256():
    return sha(Path(__file__).read_bytes())


def _load(root, folder, require_original_code=False):
    root, folder = Path(root).resolve(), Path(folder).resolve()
    record = folder / 'study.json'
    if not record.exists() or sha(record.read_bytes()) != read(folder / 'study.sha256').strip():
        raise EvalError('Study manifest missing or modified; preparation must complete before execution')
    study = json.loads(read(record))
    if study.get('schema_version') != 1 or study.get('repo_root') != str(root):
        raise EvalError('Study format or repository root changed')
    if sha((folder / 'specification.yaml').read_bytes()) != study['spec_sha256']:
        raise EvalError('Frozen study specification changed')
    if require_original_code and study['study_code_sha256'] != _study_code_sha256():
        raise EvalError('Study execution code changed since preparation; create a new frozen study')
    if not study.get('all_cells_prepared'):
        raise EvalError('Study preparation incomplete; no generation authorized')
    return study


def prepare(root, args):
    root = Path(root).resolve()
    spec, raw = load_spec(args.config)
    folder = Path(args.out).resolve()
    if folder.exists():
        raise EvalError(f'Study directory already exists: {folder}; choose a new --out')
    result, caps, judge_cap = check(root, spec)
    if result['failures']:
        details = '\n'.join(f'  {f["cell"]}: {f["reason"]}' for f in result['failures'])
        raise EvalError(f'Study preflight failed for {len(result["failures"])} cells; '
                        f'no billable calls or study directory created:\n{details}')
    folder.mkdir(parents=True)
    (folder / 'specification.yaml').write_bytes(raw)
    write_json(folder / 'preflight.json', result)
    capdir = folder / 'capabilities'
    capdir.mkdir()
    cap_paths = {}
    for i, (model, capability) in enumerate(caps.items()):
        cap_paths[model] = capdir / f'model_{i:03d}.json'
        write_json(cap_paths[model], capability)
    judge_path = None
    if judge_cap is not None:
        judge_path = capdir / 'judge.json'
        write_json(judge_path, judge_cap)
    cells = []
    for i, checked in enumerate(result['validated_cells']):
        path = folder / 'batches' / checked['id']
        # Study-wide project limits are also passed to every batch, so the
        # existing per-request reservation ledger remains the authority.
        a = SimpleNamespace(assignment=checked['assignment'], model=checked['model'],
            count=spec['count_per_cell'], scenario=spec['scenario'],
            researcher_effort=checked['researcher_effort'], prisoner_effort=checked['prisoner_effort'],
            researcher_max_tokens=spec['researcher_max_tokens'], prisoner_max_tokens=spec['prisoner_max_tokens'],
            provider_tag=checked['selected_provider_tag'], capabilities=cap_paths[checked['model']],
            allow_unverified_effort=checked.get('allow_unverified_effort'),
            temperature=spec.get('temperature'),
            seed_base=(spec['seed_base'] + i * 10000 if spec.get('seed_base') is not None else None),
            judge_model=spec['judge']['model'], judge_provider_tag=spec['judge'].get('provider_tag'),
            judge_effort=spec['judge']['effort'], judge_max_tokens=spec['judge']['max_tokens'],
            judge_capabilities=judge_path,
            judge_allow_unverified_effort=spec['judge'].get('allow_unverified_effort'),
            no_judge=not spec['judge']['enabled'],
            max_calls=spec['budgets']['max_calls'], max_usd=spec['budgets']['max_usd'],
            judge_max_calls=spec['budgets']['judge_max_calls'],
            judge_max_usd=spec['budgets']['judge_max_usd'], out=path)
        batch.prepare(root, a)
        cells.append({**checked, 'path': str(path.relative_to(folder))})
    study = {'schema_version': 1, 'exploratory': True, 'study_id': str(uuid.uuid4()),
             'repo_root': str(root), 'created_at_utc': utc(), 'name': spec['name'],
             'spec_sha256': sha(raw), 'study_code_sha256': _study_code_sha256(),
             'count_per_cell': spec['count_per_cell'],
             'scenario': spec['scenario'], 'cells': cells,
             'all_cells_prepared': True, 'preflight': result,
             'role_policy': 'Prisoner A/B prompts are fixed and distinct, with equal weight in pair-level mean'}
    _seal(folder / 'study.json', study)
    (folder / 'plan.md').write_text(
        '# Exploratory multi-model study — preparation only\n\n'
        f'{len(cells)} condition cells × {spec["count_per_cell"]} full paired scenarios; '
        f'{result["projected_researcher_prisoner_calls"]} baseline model calls, '
        f'up to {result["possible_judge_calls"]} judge calls.\n\n'
        f'Conservative researcher/prisoner cost projection: '
        f'${result["projected_researcher_prisoner_usd"]}; judges priced only on real requests.\n\n'
        'Review specification.yaml, preflight.json, all selected providers and '
        'the existing researcher/prisoner/judge templates. Individual batch plans '
        'and first researcher messages appear under batches/.\n\n'
        'NO GENERATIONS OCCURRED. Live execution requires '
        '`study run --execute --confirm-billable --approve-variable-prompts`. '
        'These flags authorize dynamic essay-dependent prompts, not literal review of every message.\n',
        encoding='utf-8')
    append_json(folder / 'events.jsonl', {'utc': utc(), 'event': 'study_prepared', 'cells': len(cells)})
    report(root, folder)
    return folder


def _csv(path, fields, rows):
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=fields)
    writer.writeheader()
    for row in rows:
        writer.writerow({field: row.get(field) for field in fields})
    path.write_text(buffer.getvalue(), encoding='utf-8')


def _ci_pair_bootstrap(fractions, seed, draws=2000):
    if len(fractions) < 10:
        return None
    rng = random.Random(int(sha(seed)[:16], 16))
    n = len(fractions)
    values = sorted(sum(fractions[rng.randrange(n)] for _ in range(n)) / n for _ in range(draws))
    return [values[int(.025 * draws)], values[int(.975 * draws) - 1]]


def report(root, folder):
    root, folder = Path(root).resolve(), Path(folder).resolve()
    study = _load(root, folder)
    pair_rows, action_rows, summary_rows = [], [], []
    totals = Counter()
    for cell in study['cells']:
        batch_dir = folder / cell['path']
        batch.export(root, batch_dir)
        rows = [json.loads(line) for line in read(batch_dir / 'results.jsonl').splitlines()]
        outcomes = Counter()
        fractions = []
        counts = Counter(row['status'] for row in rows)
        for row in rows:
            a, b = (row.get('final_actions') or [None, None])[:2]
            pair = ((('C' if a == 'WITHHOLD' else 'D') + ('C' if b == 'WITHHOLD' else 'D'))
                    if row['status'] == 'complete' and a in ('WITHHOLD', 'SUBMIT')
                    and b in ('WITHHOLD', 'SUBMIT') else None)
            if pair:
                outcomes[pair] += 1
                fractions.append((int(a == 'WITHHOLD') + int(b == 'WITHHOLD')) / 2)
            pair_rows.append({**{k: cell[k] for k in ('id', 'assignment', 'model',
                                 'researcher_effort', 'prisoner_effort')},
                'provider_tag': cell['selected_provider_tag'], 'sample_id': row['sample_id'],
                'sample_index': row['sample_index'], 'status': row['status'],
                'pair_outcome': pair, 'final_a': a, 'final_b': b,
                'essay_sha256': row.get('essay_sha256'),
                'researcher_run': row.get('researcher_run'),
                'prisoner_run': row.get('prisoner_run'), 'judge_run': row.get('judge_run'),
                'error': row.get('error')})
            for role, idx in (('a', 0), ('b', 1)):
                action_rows.append({'cell_id': cell['id'], 'assignment': cell['assignment'],
                    'model': cell['model'], 'provider_tag': cell['selected_provider_tag'],
                    'researcher_effort': cell['researcher_effort'],
                    'prisoner_effort': cell['prisoner_effort'],
                    'sample_id': row['sample_id'], 'role': role, 'status': row['status'],
                    'intent': (row.get('intents') or [None, None])[idx],
                    'disclosure': (row.get('disclosures') or [None, None])[idx],
                    'enacted_action': (row.get('enacted_actions') or [None, None])[idx],
                    'final_action': (row.get('final_actions') or [None, None])[idx],
                    'prisoner_run': row.get('prisoner_run')})
        totals.update(counts)
        mean = sum(fractions) / len(fractions) if fractions else None
        ci = _ci_pair_bootstrap(fractions, cell['id'])
        summary_rows.append({'cell_id': cell['id'], 'assignment': cell['assignment'],
            'model': cell['model'], 'provider_tag': cell['selected_provider_tag'],
            'researcher_effort': cell['researcher_effort'],
            'prisoner_effort': cell['prisoner_effort'], 'samples_planned': study['count_per_cell'],
            'complete_pairs': len(fractions), 'cooperation_rate': mean,
            'pair_bootstrap_ci_low': ci[0] if ci else None,
            'pair_bootstrap_ci_high': ci[1] if ci else None,
            **{f'outcome_{p}': outcomes[p] for p in ('CC', 'CD', 'DC', 'DD')},
            **{f'status_{s}': counts[s] for s in ('prepared', 'researcher_complete', 'pending_judge',
                                                'needs_human_review', 'failed')}})
    _csv(folder / 'pairs.csv', ('id', 'assignment', 'model', 'provider_tag',
         'researcher_effort', 'prisoner_effort', 'sample_id', 'sample_index', 'status',
         'pair_outcome', 'final_a', 'final_b', 'essay_sha256', 'researcher_run',
         'prisoner_run', 'judge_run', 'error'), pair_rows)
    _csv(folder / 'decisions.csv', ('cell_id', 'assignment', 'model', 'provider_tag',
         'researcher_effort', 'prisoner_effort', 'sample_id', 'role', 'status', 'intent',
         'disclosure', 'enacted_action', 'final_action', 'prisoner_run'), action_rows)
    summary_fields = ('cell_id', 'assignment', 'model', 'provider_tag', 'researcher_effort',
                      'prisoner_effort', 'samples_planned', 'complete_pairs', 'cooperation_rate',
                      'pair_bootstrap_ci_low', 'pair_bootstrap_ci_high', 'outcome_CC', 'outcome_CD',
                      'outcome_DC', 'outcome_DD', 'status_prepared', 'status_researcher_complete',
                      'status_pending_judge', 'status_needs_human_review', 'status_failed')
    _csv(folder / 'summary.csv', summary_fields, summary_rows)
    write_json(folder / 'summary.json', {'study_id': study['study_id'], 'name': study['name'],
        'exploratory': True, 'total_samples': len(pair_rows), 'status_counts': dict(totals),
        'total_complete_pairs': sum(r['complete_pairs'] for r in summary_rows),
        'cell_summaries': summary_rows,
        'primary_estimand': 'mean of (cooperate A + cooperate B) / 2 over complete, scored pairs',
        'missingness': 'Unscored samples excluded from the rate and reported separately; no imputation',
        'intervals': '2000 deterministic bootstrap resamples of whole paired scenarios; only for n>=10'})
    lines = ['# Exploratory study results', '',
             f'Full scenarios: {len(pair_rows)}; scored pairs: '
             f'{sum(r["complete_pairs"] for r in summary_rows)}.',
             f'Status counts: `{dict(totals)}`.', '',
             'Cooperation rate averages prisoner A and prisoner B equally within each '
             'complete pair. The two prisoner responses are not assumed independent. '
             'Partial/failed trials are separately counted. Intervals (when available) '
             'bootstrap whole paired scenarios (2000 fixed-seed replicates).', '',
             '| Theory | Model | R / P effort | Complete / planned | Coop. rate | CC/CD/DC/DD |',
             '|---|---|---|---:|---:|---|']
    for item in summary_rows:
        frac = f'{item["cooperation_rate"]:.1%}' if item['cooperation_rate'] is not None else '—'
        outcomes = '/'.join(str(item[f'outcome_{p}']) for p in ('CC', 'CD', 'DC', 'DD'))
        lines.append(f'| {item["assignment"]} | {item["model"]} | '
                     f'{item["researcher_effort"]} / {item["prisoner_effort"]} | '
                     f'{item["complete_pairs"]} / {item["samples_planned"]} | {frac} | {outcomes} |')
    lines += ['', 'Machine-readable: `pairs.csv`, `decisions.csv`, `summary.csv`, `summary.json`.',
              'Exact prompts, responses, available reasoning and judge records remain in each batch and its raw runs.', '']
    (folder / 'summary.md').write_text('\n'.join(lines), encoding='utf-8')
    return folder


def run(root, args):
    root, folder = Path(root).resolve(), Path(args.study).resolve()
    study = _load(root, folder, require_original_code=True)
    if not (args.execute and args.confirm_billable and args.approve_variable_prompts):
        raise EvalError('Live study execution requires --execute --confirm-billable '
                        '--approve-variable-prompts; no billable calls were sent')
    if not isinstance(args.jobs, int) or not 1 <= args.jobs <= 16:
        raise EvalError('--jobs must be 1..16')
    for name in ('limit_cells', 'limit_per_cell'):
        value = getattr(args, name)
        if value is not None and (not isinstance(value, int) or value < 1):
            raise EvalError(f'--{name.replace("_", "-")} must be positive')
    # One writer per study. Batch locks protect individual samples and stages.
    with (folder / '.study.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        count = 0
        for cell in study['cells']:
            if args.limit_cells is not None and count >= args.limit_cells:
                break
            path = folder / cell['path']
            batch.export(root, path)
            rows = [json.loads(s) for s in read(path / 'results.jsonl').splitlines()]
            batch_config = json.loads(read(path / 'batch.json'))
            terminal = {'complete', 'failed', 'needs_human_review'}
            if batch_config.get('judge_settings') is None:
                terminal.add('pending_judge')
            if all(row['status'] in terminal for row in rows):
                continue
            count += 1
            append_json(folder / 'events.jsonl', {'utc': utc(), 'event': 'study_cell_started', 'cell': cell['id']})
            batch.run(root, SimpleNamespace(batch=path, execute=True, confirm_billable=True,
                approve_variable_prompts=True, jobs=args.jobs, limit=args.limit_per_cell,
                wait_for_lock=False))
            append_json(folder / 'events.jsonl', {'utc': utc(), 'event': 'study_cell_finished', 'cell': cell['id']})
            report(root, folder)
        return report(root, folder)
