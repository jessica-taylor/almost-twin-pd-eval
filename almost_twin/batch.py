"""Auditable, resumable exploratory batches of complete essay/decision/judge trials.

Every sample owns a separate pilot, a fresh essay, and a separate prisoner pair.
No API generation is performed at preparation time. Live batch authorization
approves the *template family*, not the unknown essay-specific request bytes.
"""
import csv
import fcntl
import io
import json
import uuid
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from decimal import Decimal
from pathlib import Path
from time import monotonic
from types import SimpleNamespace

from .approvals import approve, source_scope
from .common import EvalError, append_json, encoded, read, sha, utc, write_json
from .failures import sample_failure
from .judge import judge_messages
from .judge_runner import run_judge
from .limits import DEFAULT_API_TIMEOUT_SECONDS, essay_from_args
from .pilot import prepare as prepare_pilot, resume as resume_pilot
from .preflight import choose_endpoint
from .progress_log import progress
from .review_disposition import classify_adjudication
from .router import Budget, snapshot, validate_settings


CSV_FIELDS = (
    'batch_id', 'sample_id', 'sample_index', 'status', 'assignment', 'scenario',
    'model', 'provider_tag', 'researcher_effort', 'prisoner_effort', 'judge_model',
    'researcher_run_id', 'prisoner_run_id', 'judge_run_id', 'essay_sha256',
    'intent_a', 'intent_b', 'disclosure_a', 'disclosure_b',
    'enacted_a', 'enacted_b', 'adjudicated_a', 'adjudicated_b',
    'final_a', 'final_b', 'enacted_score_a', 'enacted_score_b',
    'final_score_a', 'final_score_b', 'needs_review', 'needs_human_review',
    'researcher_run', 'prisoner_run', 'judge_run', 'error',
    'failure_category', 'failure_stage', 'completion_tokens', 'output_token_limit',
    'reasoning_tokens', 'essay_words',
    'essay_json_bytes', 'essay_target_exceeded',
)

CODE_FILES = (
    'almost_twin/batch.py', 'almost_twin/cli.py', 'almost_twin/common.py',
    'almost_twin/pilot.py', 'almost_twin/router.py',
    'almost_twin/judge_runner.py', 'almost_twin/judge.py',
    'almost_twin/game.py', 'almost_twin/preflight.py',
    'almost_twin/prompts.py', 'almost_twin/sources.py',
    'almost_twin/approvals.py', 'almost_twin/review_disposition.py',
    'almost_twin/accounting.py',
    'almost_twin/failures.py',
    'almost_twin/limits.py',
)


def _code_hashes(root):
    # The package being executed may be installed outside the experimental
    # data root (as it is in test fixtures). Hash the actual running code.
    package_root = Path(__file__).resolve().parents[1]
    return {name: sha((package_root / name).read_bytes()) for name in CODE_FILES}


def _seal(path, data):
    write_json(path, data)
    path.with_suffix('.sha256').write_text(sha(path.read_bytes()) + '\n', encoding='utf-8')


def _sealed(path):
    if sha(path.read_bytes()) != read(path.with_suffix('.sha256')).strip():
        raise EvalError(f'Batch configuration changed: {path}. Refuse generation.')
    return json.loads(read(path))


def _event(folder, event, **fields):
    append_json(folder / 'events.jsonl', {'utc': utc(), 'event': event, **fields})


def _load(root, folder, require_original_code=False):
    root, folder = Path(root).resolve(), Path(folder).resolve()
    config = _sealed(folder / 'batch.json')
    if config.get('schema_version') != 1 or not config.get('exploratory'):
        raise EvalError('Unknown/non-exploratory batch format')
    if Path(config['repo_root']) != root:
        raise EvalError('Batch belongs to a different repository root; move/copying raw artifacts is unsupported')
    if require_original_code and config.get('code_hashes') != _code_hashes(root):
        raise EvalError('Batch execution code changed since preparation. Preserve the original code for this batch; '
                        'start a new batch when upgrading the runner.')
    for entry in config['samples']:
        sample = folder / entry['path']
        pilot = _sealed(sample / 'pilot.json')
        shared_settings = dict(pilot['settings'])
        if config.get('seed_base') is not None:
            if shared_settings.get('seed') != config['seed_base'] + entry['index']:
                raise EvalError(f'Sample seed changed: {sample}')
            shared_settings['seed'] = 'per_sample_seed_base_plus_index'
        if (pilot['assignment'] != config['assignment'] or
            pilot['scenario'] != config['scenario'] or
            shared_settings != config['settings'] or
            source_scope(pilot['source_identity']) != source_scope(config['source_identity']) or
            pilot['template_hashes'] != config['template_hashes']):
            raise EvalError(f'Sample preparation changed: {sample}. Refuse generation.')
    if config.get('judge_settings'):
        if _sealed(folder / 'judge_settings.json') != config['judge_settings']:
            raise EvalError('Pinned batch judge settings changed')
        _sealed(folder / 'judge_capabilities.json')
    return config


def _approval_scope(config):
    return {
        'batch_id': config['batch_id'], 'assignment': config['assignment'],
        'scenario': config['scenario'], 'source_identity': source_scope(config['source_identity']),
        'template_hashes': config['template_hashes'],
        'judge_template_sha256': config['judge_template_sha256'],
        'settings': config['settings'], 'judge_settings': config.get('judge_settings'),
        'variable_fields': ['independently_generated_researcher_essay',
                            'two_prisoner_private_observations',
                            'raw_prisoner_response_in_blinded_judge_packet'],
    }


def prepare(root, args):
    root = Path(root).resolve()
    args.essay = essay_from_args(args)
    if args.count < 1 or args.count > 10000:
        raise EvalError('--count must be between 1 and 10000')
    if args.seed_base is not None and args.seed_base < 0:
        raise EvalError('--seed-base must be nonnegative')
    folder = Path(args.out).resolve() if args.out else root / 'data/batches' / str(uuid.uuid4())
    if folder.exists():
        raise EvalError(f'Batch directory already exists: {folder}; choose a new --out or resume it')
    # Discovery is unbilled. One frozen snapshot is reused for sample preparation;
    # pilot.resume revalidates current live metadata immediately before spending.
    model_cap = json.loads(read(args.capabilities)) if args.capabilities else snapshot(args.model)
    judge_settings = None
    judge_cap = None
    if not args.no_judge:
        judge_cap = (json.loads(read(args.judge_capabilities)) if args.judge_capabilities
                     else snapshot(args.judge_model))
        judge_settings = {
            'model': args.judge_model, 'provider_tag': args.judge_provider_tag,
            'judge': {'effort': args.judge_effort, 'max_tokens': args.judge_max_tokens},
            'temperature': None, 'seed': None,
            'api_timeout_seconds': getattr(args, 'api_timeout_seconds', DEFAULT_API_TIMEOUT_SECONDS),
        }
        if args.judge_allow_unverified_effort:
            judge_settings['reasoning_override'] = {'efforts': [args.judge_effort],
                                                     'reason': args.judge_allow_unverified_effort}
        trial_judge = judge_messages(root, 'Synthetic review evidence', 'pass')
        judge_settings, judge_selection = choose_endpoint(
            judge_settings, judge_cap, [('judge', trial_judge)], validate_settings)
        # This validates the route and JSON-format capability, not any future
        # ambiguous response length (actual judge requests are revalidated).
        validate_settings(judge_settings, judge_cap, 'judge', trial_judge)
    else:
        judge_selection = None

    folder.mkdir(parents=True)
    write_json(folder / 'model_capabilities.json', model_cap)
    if judge_settings is not None:
        _seal(folder / 'judge_settings.json', judge_settings)
        _seal(folder / 'judge_capabilities.json', judge_cap)

    entries = []
    first = None
    for i in range(args.count):
        sample = folder / 'samples' / f'{i:05d}'
        p = SimpleNamespace(
            assignment=args.assignment, model=args.model,
            researcher_effort=args.researcher_effort, prisoner_effort=args.prisoner_effort,
            researcher_max_tokens=args.researcher_max_tokens, prisoner_max_tokens=args.prisoner_max_tokens,
            essay=getattr(args, 'essay', None),
            api_timeout_seconds=getattr(args, 'api_timeout_seconds', DEFAULT_API_TIMEOUT_SECONDS),
            scenario=args.scenario, provider_tag=args.provider_tag, capabilities=folder / 'model_capabilities.json',
            allow_unverified_effort=args.allow_unverified_effort, temperature=args.temperature,
            seed=args.seed_base + i if args.seed_base is not None else None,
            out=sample, max_calls=args.max_calls, max_usd=args.max_usd)
        prepare_pilot(root, p)
        pilot_config = _sealed(sample / 'pilot.json')
        if first is None:
            first = pilot_config
        if (pilot_config['settings']['provider_tag'] != first['settings']['provider_tag'] or
            pilot_config['template_hashes'] != first['template_hashes'] or
            source_scope(pilot_config['source_identity']) != source_scope(first['source_identity'])):
            raise EvalError('Batch sample selection or source changed during preparation')
        entries.append({'sample_id': str(uuid.uuid4()), 'index': i,
                        'path': f'samples/{i:05d}', 'pilot_id': pilot_config['pilot_id']})
        write_json(sample / 'batch_sample.json', entries[-1])

    # Across samples only a seed can vary. Freeze everything else in the batch.
    settings = dict(first['settings'])
    if args.seed_base is not None:
        settings['seed'] = 'per_sample_seed_base_plus_index'
    projected = json.loads(read(folder / entries[0]['path'] / 'plan.json'))
    estimates = projected['estimates'] * args.count
    budget_check = Budget(root / 'data/budget.jsonl', args.max_calls, args.max_usd).check(estimates)
    if judge_settings:
        # Judge input depends on generated outputs. Its *actual* cost is bounded
        # and reserved immediately before each call; require enough call slots.
        Budget(root / 'data/judge_budget.jsonl', args.judge_max_calls, args.judge_max_usd).check(
            [{'estimated_max_usd': '0'}] * (2 * args.count))
    batch = {
        'schema_version': 1, 'exploratory': True, 'batch_id': str(uuid.uuid4()),
        'repo_root': str(root), 'created_at_utc': utc(), 'assignment': args.assignment,
        'scenario': args.scenario, 'model': args.model,
        'settings': settings, 'source_identity': first['source_identity'],
        'template_hashes': first['template_hashes'], 'judge_template_sha256': sha((root / 'prompts/judge/intent.md').read_bytes()),
        'judge_settings': judge_settings, 'judge_selection': judge_selection,
        'count': args.count, 'samples': entries, 'max_calls': args.max_calls, 'max_usd': str(args.max_usd),
        'judge_max_calls': args.judge_max_calls, 'judge_max_usd': str(args.judge_max_usd),
        'seed_policy': 'unset; independent API requests, not guaranteed independent model samples'
                       if args.seed_base is None else f'deterministic varied seed: {args.seed_base} + index',
        'seed_base': args.seed_base,
        'code_hashes': _code_hashes(root),
    }
    # Individual samples contain their actual seed; the global batch settings
    # represent only the shared fields and explicit seed policy.
    _seal(folder / 'batch.json', batch)
    plan = {'batch_id': batch['batch_id'], 'exploratory': True, 'count': args.count,
            'expected_researcher_plus_prisoner_usd': str(
                Decimal(projected['expected_three_call_usd']) * args.count),
            'projected_researcher_plus_prisoner_usd': str(sum(
                Decimal(e['estimated_max_usd']) for e in estimates)),
            'projected_request_count': 3 * args.count,
            'possible_judge_calls': 2 * args.count if judge_settings else 0,
            'judge_pricing': 'Actual uncertain judge prompts priced and reserved only when generated',
            'budget_check': budget_check, 'judge_selection': judge_selection,
            'approval_scope': _approval_scope(batch),
            'note': 'Projected prisoner costs use the enforced researcher-essay JSON-size ceiling; '
                    'actual assembled prompts are independently checked before billing.'}
    write_json(folder / 'plan.json', plan)
    (folder / 'plan.md').write_text(
        '# Exploratory Almost-Twin PD batch\n\n'
        f'Batch: {batch["batch_id"]}; {args.count} fresh researcher essays + {2 * args.count} prisoner calls.\n\n'
        f'Assignment: {args.assignment}; scenario: {args.scenario}; model: {args.model}; endpoint: {first["settings"]["provider_tag"]}.\n\n'
        f'Expected researcher + prisoner cost (heuristic): ${plan["expected_researcher_plus_prisoner_usd"]}. '
        f'Estimated upper bound: ${plan["projected_researcher_plus_prisoner_usd"]}. '
        'Judge costs are separately capped and validated at request time.\n\n'
        'Review the source and prompt templates, the first sample in samples/00000/researcher/messages_0.md, '
        'and plan.json before authorizing dynamic sample generation.\n\n'
        'Batch authorization covers reviewed templates with *variable generated essays*; '
        'it does not claim manual inspection of each resulting prompt. '
        'Every request/response is saved separately.\n\n'
        'Preparation makes zero billable model calls. To execute, explicitly use '
        '--execute --confirm-billable --approve-variable-prompts.\n',
        encoding='utf-8')
    _event(folder, 'batch_prepared', count=args.count, model=args.model)
    export(root, folder)
    return folder


def _read_sample(folder, config, entry):
    sample = folder / entry['path']
    ps = json.loads(read(sample / 'state.json'))
    result = {
        'batch_id': config['batch_id'], 'sample_id': entry['sample_id'],
        'sample_index': entry['index'], 'assignment': config['assignment'], 'scenario': config['scenario'],
        'model': config['model'],
        'provider_tag': json.loads(read(sample / 'pilot.json'))['settings']['provider_tag'],
        'researcher_effort': config['settings']['researcher']['effort'],
        'prisoner_effort': config['settings']['prisoner']['effort'],
        'judge_model': (config.get('judge_settings') or {}).get('model'),
        'status': 'prepared', 'error': None, 'needs_review': None, 'needs_human_review': None,
        'researcher_run': ps.get('researcher_run'), 'prisoner_run': ps.get('prisoner_run'),
        'researcher_run_id': None, 'prisoner_run_id': None,
        'judge_run': None, 'judge_run_id': None,
        'essay_sha256': ps.get('essay_sha256'),
    }
    for stage in ('researcher', 'prisoner'):
        path = ps.get(stage + '_run')
        if path:
            result[stage + '_run_id'] = Path(path).name
    if ps.get('researcher_status') == 'success':
        result['status'] = 'researcher_complete'
    if ps.get('researcher_run'):
        run_dir = Path(ps['researcher_run'])
        info_file = run_dir / ('essay.json' if (run_dir / 'essay.json').exists() else 'failure.json')
        if info_file.exists():
            info = json.loads(read(info_file))
            result.update({k: info[k] for k in ('essay_words', 'essay_json_bytes', 'essay_target_exceeded') if k in info})
    if ps.get('prisoner_status') == 'success' and ps.get('prisoner_run'):
        original = json.loads(read(Path(ps['prisoner_run']) / 'outcome.json'))
        result.update(status='complete' if not original['needs_review'] else 'pending_judge',
                      original_outcome=original, needs_review=original['needs_review'],
                      intents=original['intents'], disclosures=original['disclosures'],
                      enacted_actions=original['enacted_actions'],
                      enacted_score=original.get('enacted_score'),
                      final_actions=original['enacted_actions'],
                      final_score=original.get('enacted_score'))
    for stage in ('researcher', 'prisoner'):
        if ps.get(stage + '_status') in ('failed', 'preflight_failed', 'attempted'):
            result.update(status='failed', error=f'{stage}: {ps[stage + "_status"]}; inspect {ps.get(stage + "_run")}')
    sample_state = json.loads(read(sample / 'sample_state.json')) if (sample / 'sample_state.json').exists() else {}
    if sample_state.get('judge_run'):
        jdir = Path(sample_state['judge_run'])
        result['judge_run'], result['judge_run_id'] = str(jdir), jdir.name
        if (jdir / 'adjudicated_outcome.json').exists():
            judged = json.loads(read(jdir / 'adjudicated_outcome.json'))
            terminal = classify_adjudication(judged)
            result.update(judge_outcome=judged, adjudicated_actions=judged['adjudicated_actions'],
                          needs_human_review=judged['needs_human_review'],
                          final_actions=judged['adjudicated_actions'],
                          final_score=judged.get('adjudicated_score'),
                          status=terminal['status'])
        elif sample_state.get('judge_status') == 'attempted':
            result.update(status='failed', error=f'Judge attempted; inspect {jdir}; no automatic retry')
    if sample_state.get('error'):
        result.update(status='failed', error=sample_state['error'])
    result.update({k: v for k, v in sample_failure(result).items()
                   if k != 'essay_words' or v is not None})
    return result


def _cell(value, i):
    if not isinstance(value, (list, tuple)) or len(value) <= i:
        return None
    return value[i]


def _csv_row(r):
    enacted_score = (r.get('enacted_score') or {}).get('utilities') or []
    final_score = (r.get('final_score') or {}).get('utilities') or []
    result = {k: r.get(k) for k in CSV_FIELDS}
    for letter, i in (('a', 0), ('b', 1)):
        for key, vals in (('intent', r.get('intents')), ('disclosure', r.get('disclosures')),
                          ('enacted', r.get('enacted_actions')),
                          ('adjudicated', r.get('adjudicated_actions')),
                          ('final', r.get('final_actions'))):
            result[f'{key}_{letter}'] = _cell(vals, i)
        result[f'enacted_score_{letter}'] = _cell(enacted_score, i)
        result[f'final_score_{letter}'] = _cell(final_score, i)
    for field in ('needs_review', 'needs_human_review'):
        if result.get(field) is not None:
            result[field] = json.dumps(result[field], ensure_ascii=False)
    return result


def export(root, folder):
    folder = Path(folder).resolve()
    config = _load(root, folder)
    rows = [_read_sample(folder, config, entry) for entry in config['samples']]
    # Derived views may be regenerated. Raw generations, reservations, event
    # journals and per-sample pilot/judge records are never overwritten.
    (folder / 'results.jsonl').write_bytes(b''.join(encoded(row) + b'\n' for row in rows))
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=CSV_FIELDS)
    writer.writeheader()
    for row in rows:
        writer.writerow(_csv_row(row))
    (folder / 'results.csv').write_text(buffer.getvalue(), encoding='utf-8')
    counts = dict(sorted(Counter(row['status'] for row in rows).items()))
    write_json(folder / 'summary.json', {'batch_id': config['batch_id'], 'total': len(rows),
               'counts': counts, 'results_jsonl': str(folder / 'results.jsonl'),
               'results_csv': str(folder / 'results.csv')})
    return folder


def _sample_live(root, folder, entry, scope, config):
    sample = folder / entry['path']
    state_file = sample / 'sample_state.json'
    # Exactly one process/thread may control a sample at a time. Repeated
    # batch launches therefore cannot duplicate an already completed stage.
    with (sample / '.batch.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        sample_state = json.loads(read(state_file)) if state_file.exists() else {}
        try:
            for stage in ('researcher', 'prisoners'):
                opts = SimpleNamespace(pilot_command=stage, pilot=sample, execute=True,
                       confirm_billable=True, prompts_approved=False, batch_approval_scope=scope)
                resume_pilot(root, opts)
            pilot_state = json.loads(read(sample / 'state.json'))
            pair_dir = Path(pilot_state['prisoner_run'])
            original = json.loads(read(pair_dir / 'outcome.json'))
            if original['needs_review'] and config['judge_settings']:
                if sample_state.get('judge_run'):
                    judge_dir = Path(sample_state['judge_run'])
                    if not (judge_dir / 'adjudicated_outcome.json').exists():
                        raise EvalError(f'Judge previously attempted at {judge_dir}; no automatic retry')
                else:
                    judge_dir = root / 'data/judge_runs' / str(uuid.uuid4())
                    sample_state.update(judge_run=str(judge_dir), judge_status='attempted')
                    write_json(state_file, sample_state)
                    judge_args = SimpleNamespace(run=pair_dir, settings=folder / 'judge_settings.json',
                          capabilities=folder / 'judge_capabilities.json', run_id=judge_dir.name,
                          execute=True, confirm_billable=True, prompts_approved=True,
                          batch_approval_scope=scope, max_calls=config['judge_max_calls'],
                          max_usd=config['judge_max_usd'])
                    run_judge(root, judge_args)
                    sample_state['judge_status'] = 'complete'
            sample_state.pop('error', None)
            write_json(state_file, sample_state)
            return {'sample_id': entry['sample_id'], 'status': 'processed'}
        except Exception as error:
            sample_state['error'] = f'{type(error).__name__}: {error}'
            write_json(state_file, sample_state)
            return {'sample_id': entry['sample_id'], 'status': 'failed', 'error': str(error)}


def _timed_sample_live(root, folder, entry, scope, config):
    progress.info('Sample %d/%d for %s: started', entry['index'] + 1,
                  config['count'], config['model'])
    started = monotonic()
    result = _sample_live(root, folder, entry, scope, config)
    elapsed = round(monotonic() - started, 3)
    progress.info('Sample %d/%d for %s: %s after %.1fs%s',
                  entry['index'] + 1, config['count'], config['model'],
                  'pipeline finished' if result['status'] == 'processed' else result['status'], elapsed,
                  f'; error: {result["error"]}' if result.get('error') else '')
    return {**result, 'elapsed_seconds': elapsed}


def run(root, args):
    root, folder = Path(root).resolve(), Path(args.batch).resolve()
    config = _load(root, folder, require_original_code=bool(args.execute or args.confirm_billable))
    live = args.execute or args.confirm_billable
    if not live:
        return export(root, folder)
    if not (args.execute and args.confirm_billable and args.approve_variable_prompts):
        raise EvalError('Batch execution requires --execute, --confirm-billable, and --approve-variable-prompts. '
                        'Review plan.md and the source/templates first; the approval covers new dynamic essays, '
                        'not each exact request. No model calls sent.')
    if args.jobs < 1 or args.jobs > 16:
        raise EvalError('--jobs must be 1..16')
    if args.limit is not None and args.limit < 1:
        raise EvalError('--limit must be positive')
    # Batch-wide activation lock prevents two simultaneous invocations from
    # racing to start the same pending sample; individual samples also lock.
    with (folder / '.batch.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX if args.wait_for_lock else fcntl.LOCK_EX | fcntl.LOCK_NB)
        scope = _approval_scope(config)
        approve(root, 'batch_dynamic_templates', scope, acknowledged=True)
        _event(folder, 'batch_execution_authorized', jobs=args.jobs)
        todo = []
        for entry in config['samples']:
            status = _read_sample(folder, config, entry)['status']
            if status in ('complete', 'failed', 'needs_human_review',
                          'resolved_nonaction', 'resolved_unscored'):
                continue
            if status == 'pending_judge' and config['judge_settings'] is None:
                continue
            todo.append(entry)
        if args.limit is not None:
            todo = todo[:args.limit]
        progress.info('Batch %s: running %d pending samples (jobs=%d)',
                      config['model'], len(todo), args.jobs)
        results = []
        started = monotonic()
        with ThreadPoolExecutor(max_workers=args.jobs) as pool:
            futures = [pool.submit(_timed_sample_live, root, folder, entry, scope, config) for entry in todo]
            for future in as_completed(futures):
                result = future.result()
                results.append(result)
                _event(folder, 'sample_processed', **result)
                # Keep a resumable materialized index even if interrupted.
                export(root, folder)
        _event(folder, 'batch_run_finished', attempted=len(todo),
               failed=sum(r['status'] == 'failed' for r in results),
               elapsed_seconds=round(monotonic() - started, 3))
        progress.info('Batch %s: finished %d samples in %.1fs; %d failed',
                      config['model'], len(results), monotonic() - started,
                      sum(r['status'] == 'failed' for r in results))
        if getattr(args, 'auto_reports', True):
            from .sample_report import write_reports
            write_reports(root, folder)  # Offline; no additional model requests.
        return folder
