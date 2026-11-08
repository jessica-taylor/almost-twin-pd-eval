"""Exploratory, two-stage pilot convenience layer over the existing audited runner."""
import fcntl
import json
import uuid
from decimal import Decimal
from pathlib import Path
from types import SimpleNamespace

from .approvals import source_scope
from .accounting import (EXPECTED_PRISONER_OUTPUT_TOKENS, EXPECTED_RESEARCHER_OUTPUT_TOKENS,
                         expected_prisoner_input_tokens, prisoner_input_ceiling)
from .common import EvalError, append_json, encoded, read, sha, utc, write_json
from .preflight import choose_endpoint, estimate_price
from .prompts import assignment, cases, export_messages, prisoners, researcher, template_hashes
from .router import Budget, run, snapshot, validate_settings
from .sources import load_source, source_identity


def _seal(path, value):
    write_json(path, value)
    path.with_suffix('.sha256').write_text(sha(path.read_bytes()) + '\n', encoding='utf-8')


def _sealed(path):
    if sha(path.read_bytes()) != read(path.with_suffix('.sha256')).strip():
        raise EvalError(f'Pilot artifact {path} changed. Prepare a new pilot and re-review its prompts; no generation sent.')
    return json.loads(read(path))


def _event(folder, event, **details):
    append_json(folder / 'events.jsonl', {'utc': utc(), 'event': event, **details})


def _total(estimates):
    return str(sum((Decimal(e['estimated_max_usd']) for e in estimates), Decimal(0)))


def _stage_export(folder, payloads, estimates, metadata):
    folder.mkdir(parents=True, exist_ok=False)
    hashes = []
    for i, payload in enumerate(payloads):
        export_messages(folder, f'messages_{i}', payload['messages'])
        (folder / f'request_{i}.json').write_bytes(encoded(payload))
        hashes.append(sha(encoded(payload)))
    plan = {**metadata, 'request_hashes': hashes, 'estimates': estimates, 'estimated_total_usd': _total(estimates)}
    _seal(folder / 'plan.json', plan)
    return plan


def _check_export(folder, plan):
    for i, digest in enumerate(plan['request_hashes']):
        if sha((folder / f'request_{i}.json').read_bytes()) != digest:
            raise EvalError('Prepared serialized request changed; prepare and review a new pilot.')
        payload = json.loads(read(folder / f'request_{i}.json'))
        messages = payload['messages']
        if json.loads(read(folder / f'messages_{i}.json')) != messages:
            raise EvalError('Prepared message JSON changed; approval is invalid.')
        markdown = '\n\n'.join(f'<!-- message role: {m["role"]} -->\n{m["content"]}' for m in messages)
        if read(folder / f'messages_{i}.md') != markdown:
            raise EvalError('Readable prompt changed; approval is invalid. Re-prepare and inspect exact requests.')


def _readable(folder, config, state):
    root_plan = json.loads(read(folder / 'plan.json'))
    lines = ['# Exploratory pilot — not preregistered data', '',
             f'Assignment: {config["assignment"]}; model: {config["settings"]["model"]}; pinned endpoint: {config["settings"]["provider_tag"]}.', '',
             f'Efforts: researcher={config["settings"]["researcher"]["effort"]}, prisoner={config["settings"]["prisoner"]["effort"]}. Scenario: {config["scenario"]}.', '',
             f'Researcher maximum estimated cost: ${root_plan["researcher_estimated_usd"]}.',
             f'Expected three-call cost (heuristic, not a cap): ${root_plan["expected_three_call_usd"]}.',
             f'Projected three-call upper estimate: ${root_plan["projected_three_call_usd"]} (prisoner input bounded by the enforced researcher-essay size limit and endpoint context; actual prompts/cost checked after essay).', '',
             '[Researcher prompt](researcher/messages_0.md) · [Exact message JSON](researcher/messages_0.json) · [Exact serialized request](researcher/request_0.json)', '',
             '[Machine plan, effort evidence and price assumptions](plan.json) · [Pinned settings](settings.json) · [Append-only pilot events](events.jsonl)', '',
             'No separate source approval is required. Source hashes and attribution are retained. Model calls require both --execute and --confirm-billable; prompt approval is tied to serialized request hashes.', '']
    if state.get('researcher_run'):
        path = Path(state['researcher_run'])
        if (path / 'essay.json').exists():
            lines += [f'[Frozen essay]({path / "essay.md"}) · [Researcher run]({path / "plan.json"})', '']
        else:
            lines += [f'Researcher attempt: `{path}`; status: {state.get("researcher_status")}. See events.jsonl and any failure.json.', '']
    if (folder / 'prisoners/plan.json').exists():
        lines += ['[Prisoner A](prisoners/messages_0.md) · [Prisoner B](prisoners/messages_1.md) · [Exact pair requests/cost](prisoners/plan.json)', '']
    if state.get('prisoner_run'):
        path = Path(state['prisoner_run'])
        if (path / 'outcome.json').exists():
            lines += [f'[Pair outcome]({path / "outcome.json"}) · [Pair run and responses]({path / "plan.json"})', '']
        else:
            lines += [f'Pair attempt: `{path}`; status: {state.get("prisoner_status")}. See events.jsonl and any failure.json; no completed outcome is implied.', '']
    (folder / 'plan.md').write_text('\n'.join(lines), encoding='utf-8')


def prepare(root, args):
    root = Path(root).resolve()
    item = assignment(root, args.assignment)
    source, info = load_source(root, item['source_id'])
    identity = source_identity(item['source_id'], source, info)
    messages = researcher(root, item, source, info)
    scenario = next((c for c in cases(root) if c['case_id'] == args.scenario), None)
    if scenario is None:
        raise EvalError(f'Unknown active observation scenario: {args.scenario}')
    cap = json.loads(read(args.capabilities)) if args.capabilities else snapshot(args.model)
    settings = {'model': args.model, 'provider_tag': args.provider_tag,
                'researcher': {'effort': args.researcher_effort, 'max_tokens': args.researcher_max_tokens},
                'prisoner': {'effort': args.prisoner_effort, 'max_tokens': args.prisoner_max_tokens},
                'temperature': args.temperature, 'seed': args.seed}
    if args.allow_unverified_effort:
        settings['reasoning_override'] = {'efforts': sorted({args.researcher_effort, args.prisoner_effort}),
                                          'reason': args.allow_unverified_effort}
    settings, selection = choose_endpoint(settings, cap, [('researcher', messages), ('prisoner', [{'role': 'user', 'content': ''}])], validate_settings)
    payload, estimate = validate_settings(settings, cap, 'researcher', messages)
    prisoner_payload, prisoner_estimate = validate_settings(settings, cap, 'prisoner', [{'role': 'user', 'content': ''}])
    endpoint = prisoner_estimate['endpoint']
    prompt_ceiling = prisoner_input_ceiling(root, item, scenario, args.researcher_max_tokens,
                                             endpoint, args.prisoner_max_tokens)
    price, assumptions = estimate_price(prisoner_payload, endpoint, cap['model'], prompt_ceiling, args.prisoner_max_tokens)
    typical_input = expected_prisoner_input_tokens(root, item, scenario, args.researcher_max_tokens,
                                                   endpoint, args.prisoner_max_tokens)
    typical_prisoner, _ = estimate_price(prisoner_payload, endpoint, cap['model'], typical_input,
                                         min(args.prisoner_max_tokens, EXPECTED_PRISONER_OUTPUT_TOKENS))
    typical_researcher, _ = estimate_price(payload, estimate['endpoint'], cap['model'],
                                           estimate['input_tokens_upper_estimate'],
                                           min(args.researcher_max_tokens, EXPECTED_RESEARCHER_OUTPUT_TOKENS))
    typical_three_calls = str(Decimal(typical_researcher) + 2 * Decimal(typical_prisoner))
    projection = {'estimated_max_usd': price, 'pricing_assumptions': assumptions,
                  'input_tokens_upper_estimate': prompt_ceiling, 'reasoning_evidence': prisoner_estimate['reasoning_evidence'],
                  'kind': 'enforced essay-size ceiling; final assembled prisoner request still independently checked'}
    estimates = [estimate, projection, projection]
    budget = Budget(root / 'data/budget.jsonl', args.max_calls, args.max_usd).check(estimates)
    folder = Path(args.out).resolve() if args.out else root / 'data/pilots' / str(uuid.uuid4())
    if folder.exists():
        raise EvalError(f'{folder} already exists. Resume it with pilot researcher/prisoners --pilot, or choose a new --out; existing pilots are never overwritten.')
    folder.mkdir(parents=True)
    config = {'schema_version': 1, 'pilot_id': str(uuid.uuid4()), 'exploratory': True, 'assignment': args.assignment,
              'assignment_record': item, 'scenario': args.scenario, 'scenario_record': scenario, 'source_identity': identity,
              'template_hashes': template_hashes(root, item), 'settings': settings,
              'max_calls': args.max_calls, 'max_usd': args.max_usd, 'created_at_utc': utc(),
              'metadata_mode': 'offline_snapshot' if args.capabilities else 'online_refresh',
              'canonical_model': cap['model'].get('canonical_slug')}
    _seal(folder / 'pilot.json', config)
    _seal(folder / 'settings.json', settings)
    _seal(folder / 'capabilities.json', cap)
    _stage_export(folder / 'researcher', [payload], [estimate], {'stage': 'researcher', 'exploratory': True, **identity})
    write_json(folder / 'plan.json', {'exploratory': True, 'pilot_id': config['pilot_id'], 'source_identity': identity,
                'endpoint_selection': selection, 'researcher_estimated_usd': estimate['estimated_max_usd'],
                'projected_three_call_usd': _total(estimates),
                'expected_three_call_usd': typical_three_calls,
                'estimates': estimates, 'budget': budget,
                'source_approval_required': False,
                'metadata_sha256': sha(encoded(cap))})
    write_json(folder / 'state.json', {})
    _event(folder, 'prepared', endpoint=settings['provider_tag'])
    _readable(folder, config, {})
    return folder


def _load(root, folder):
    config = _sealed(folder / 'pilot.json')
    if _sealed(folder / 'settings.json') != config['settings']:
        raise EvalError('Pinned settings differ from pilot configuration; prepare a new pilot')
    item = assignment(root, config['assignment'])
    if item != config['assignment_record'] or template_hashes(root, item) != config['template_hashes']:
        raise EvalError('Assignment/template/scenario content changed since preparation. Prepare a new pilot; old approvals cannot cover changed prompts.')
    return config, json.loads(read(folder / 'state.json'))


def _essay(config, state):
    if not state.get('researcher_run'):
        raise EvalError('No successful researcher essay. Run pilot researcher --pilot PATH first, then inspect the essay.')
    folder = Path(state['researcher_run'])
    info = json.loads(read(folder / 'essay.json'))
    text = read(folder / 'essay.md')
    raw = json.loads(read(folder / 'call_0/response.raw'))
    plan = json.loads(read(folder / 'plan.json'))
    if (info.get('status') != 'success' or info.get('essay_sha256') != sha(text) or
        (state.get('essay_sha256') is not None and state['essay_sha256'] != sha(text)) or
        raw['choices'][0]['message'].get('content') != text or raw['choices'][0].get('finish_reason') != 'stop' or
        info.get('model') != config['settings']['model'] or raw.get('model') != config['settings']['model'] or
        info.get('provider_tag') != config['settings']['provider_tag'] or info.get('assignment') != config['assignment'] or
        source_scope(info) != source_scope(config['source_identity']) or
        plan.get('request_hashes') != state.get('researcher_request_hashes')):
        raise EvalError('Frozen researcher essay/provenance changed or is incomplete; inspect its raw response and logs. No prisoner calls sent.')
    return folder, text, info


def resume(root, args):
    root, folder = Path(root).resolve(), Path(args.pilot).resolve()
    # Lock the whole resume operation to prevent concurrent duplicate model calls.
    if not folder.is_dir():
        raise EvalError(f'Pilot {folder} does not exist; run pilot prepare first')
    with (folder / '.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        return _resume(root, folder, args)


def _resume(root, folder, args):
    config, state = _load(root, folder)
    stage = 'researcher' if args.pilot_command == 'researcher' else 'prisoner'
    live = args.execute or args.confirm_billable
    batch_scope = getattr(args, 'batch_approval_scope', None)
    if live and not (args.execute and args.confirm_billable):
        raise EvalError('Making a model request requires BOTH --execute and --confirm-billable')
    # Recover a completed essay even if the process stopped before writing state.
    if state.get('researcher_run') and (Path(state['researcher_run']) / 'essay.json').exists():
        _, text, _ = _essay(config, state)
        state.update(researcher_status='success', essay_sha256=sha(text))
        write_json(folder / 'state.json', state)
    if stage == 'researcher' and state.get('researcher_status') == 'success':
        _readable(folder, config, state)
        return Path(state['researcher_run'])  # Resume never repeats a completed call.
    previous = state.get(stage + '_run')
    if previous and (Path(previous) / 'outcome.json').exists():
        return Path(previous)
    if previous and list(Path(previous).glob('call_*')):
        raise EvalError(f'{stage} was already attempted at {previous}. Inspect failure/raw responses; no automatic retries or duplicate commitments. Prepare a new exploratory pilot if a new attempt is intended; reservations remain counted.')
    cap = _sealed(folder / 'capabilities.json')
    cap_path = folder / 'capabilities.json'
    settings = config['settings']
    if live or config['metadata_mode'] == 'online_refresh':
        cap = snapshot(settings['model'])
        cap_path = folder / 'metadata_checks' / (str(uuid.uuid4()) + '.json')
        write_json(cap_path, cap)
    if config.get('canonical_model') and cap['model'].get('canonical_slug') != config['canonical_model']:
        raise EvalError('The model ID now resolves to a different canonical version. Prepare and review a new pilot; the pinned experiment will not change models.')
    if stage == 'researcher':
        prepared_dir = folder / 'researcher'
        prepared = _sealed(prepared_dir / 'plan.json')
        essay_dir = None
    else:
        essay_dir, essay, _ = _essay(config, state)
        pair = prisoners(root, config['assignment_record'], essay, config['scenario_record'])
        payloads, estimates = [], []
        for messages in pair:
            payload, estimate = validate_settings(settings, cap, 'prisoner', messages)
            payloads.append(payload)
            estimates.append(estimate)
        prepared_dir = folder / 'prisoners'
        if not prepared_dir.exists():
            _stage_export(prepared_dir, payloads, estimates, {'stage': 'prisoner', 'exploratory': True, 'essay_sha256': sha(essay)})
            _event(folder, 'prisoner_prompts_prepared', essay_sha256=sha(essay))
            _readable(folder, config, state)
            if live and batch_scope is None:
                raise EvalError(f'Prisoner prompts are now prepared at {prepared_dir}. Inspect both Markdown/JSON requests and cost, then rerun with the billing flags and --prompts-approved.')
        prepared = _sealed(prepared_dir / 'plan.json')
        if prepared['essay_sha256'] != sha(essay):
            raise EvalError('Essay changed since prisoner prompt preparation; previous approval invalid')
    _check_export(prepared_dir, prepared)
    run_id = str(uuid.uuid4())
    opts = SimpleNamespace(stage=stage, execute=args.execute, confirm_billable=args.confirm_billable,
           prompts_approved=args.prompts_approved,
           assignment=config['assignment'], settings=folder / 'settings.json', capabilities=cap_path, fresh_capabilities=cap if live else None,
           essay=essay_dir, scenario=config['scenario'], max_calls=config['max_calls'], max_usd=config['max_usd'],
           expected_request_hashes=prepared['request_hashes'], expected_source_identity=source_scope(config['source_identity']),
           exploratory=True, pilot_id=config['pilot_id'], run_id=run_id,
           batch_approval_scope=batch_scope)
    anticipated = root / 'data/exploratory/runs' / run_id
    if live:
        state.update({stage + '_run': str(anticipated), stage + '_status': 'attempted'})
        if stage == 'researcher':
            state['researcher_request_hashes'] = prepared['request_hashes']
        write_json(folder / 'state.json', state)
        _event(folder, 'execution_requested', stage=stage, run_id=run_id)
    try:
        actual = run(root, opts)
    except Exception as error:
        if live:
            state[stage + '_status'] = 'failed' if list(anticipated.glob('call_*')) else 'preflight_failed'
            write_json(folder / 'state.json', state)
        _event(folder, 'execution_failed' if live else 'preflight_failed', stage=stage, error=str(error))
        _readable(folder, config, state)
        raise
    if live:
        state.update({stage + '_run': str(actual), stage + '_status': 'success'})
        if stage == 'researcher':
            state['essay_sha256'] = sha((actual / 'essay.md').read_bytes())
        write_json(folder / 'state.json', state)
        _event(folder, 'execution_completed', stage=stage, run_id=run_id)
    _readable(folder, config, state)
    return actual

