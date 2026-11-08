"""Thin, fail-closed OpenRouter path. Dry runs make zero network requests."""
import fcntl
import json
import math
import os
import urllib.error
import urllib.parse
import urllib.request
import uuid
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path

from .common import EvalError, append_json, encoded, load_yaml, read, sha, utc, write_json
from .accounting import require_essay_within_limit
from .game import Game, classify_response, score
from .prompts import assignment, cases, export_messages, prisoners, researcher, template_hashes
from .sources import load_source, source_identity
from .preflight import choose_endpoint, effort_evidence, estimate_price
from .approvals import approve, source_scope

BASE = 'https://openrouter.ai/api/v1'
MAX_AGE_HOURS = 24


def http_get(path):
    # Discovery endpoints are unbilled and send no article, essay or API key.
    with urllib.request.urlopen(BASE + path, timeout=30) as response:
        return json.loads(response.read())


def snapshot(model):
    if not isinstance(model, str) or model.count('/') != 1 or any(x in model for x in ('~', '@', '?', '#')):
        raise EvalError('Choose an explicit author/model ID, not an auto/router/preset alias')
    try:
        models = http_get('/models')
        selected = next((m for m in models['data'] if m['id'] == model), None)
        if selected is None:
            raise EvalError(f'Model ID absent from OpenRouter catalog: {model}. Check its availability; the runner will not substitute another model.')
        endpoints = http_get('/models/' + urllib.parse.quote(model, safe='/') + '/endpoints')
    except (OSError, urllib.error.URLError, ValueError, KeyError) as error:
        if isinstance(error, EvalError):
            raise
        raise EvalError(f'Could not refresh unbilled OpenRouter metadata for {model} ({type(error).__name__}). Check connectivity or use pilot prepare --capabilities SAVED_SNAPSHOT for offline preparation. No generation was sent.') from error
    return {'retrieved_at_utc': utc(), 'model': selected, 'endpoints': endpoints['data']['endpoints'],
            'discovery_urls': [BASE + '/models', BASE + '/models/' + model + '/endpoints']}


def age_hours(value):
    try:
        stamp = datetime.fromisoformat(value.replace('Z', '+00:00'))
        age = (datetime.now(timezone.utc) - stamp).total_seconds() / 3600
        if age < -0.1:
            raise ValueError('future timestamp')
        return age
    except (ValueError, TypeError, AttributeError) as error:
        raise EvalError('Missing or invalid UTC capability/review timestamp') from error


def validate_settings(settings, cap, stage, messages):
    try:
        return _validate_settings(settings, cap, stage, messages)
    except EvalError as error:
        raise EvalError(f"{settings.get('model')} / endpoint {settings.get('provider_tag')} / {stage} effort={settings.get(stage, {}).get('effort')}: {error}") from error


def _validate_settings(settings, cap, stage, messages):
    model = settings.get('model')
    provider = settings.get('provider_tag')
    if not model or not provider:
        raise EvalError('Researcher must select explicit model and endpoint provider_tag; no defaults')
    if cap['model']['id'] != model:
        raise EvalError('Capability snapshot belongs to another model')
    if age_hours(cap['retrieved_at_utc']) > MAX_AGE_HOURS:
        raise EvalError('Capability snapshot is stale (>24h); refresh with inspect-model --network')
    matched = [e for e in cap['endpoints'] if e.get('tag') == provider]
    if len(matched) != 1:
        raise EvalError('Select one exact endpoint tag from the snapshot; ambiguous/unknown provider')
    endpoint = matched[0]
    if endpoint.get('status') not in (None, 0):
        raise EvalError('Selected endpoint is unavailable')
    params = set(endpoint.get('supported_parameters') or [])
    options = settings[stage]
    effort, limit = options.get('effort'), options.get('max_tokens')
    if not isinstance(limit, int) or isinstance(limit, bool) or limit < 1:
        raise EvalError('max_tokens must be a positive integer')
    if 'reasoning' not in params or not params & {'max_tokens', 'max_completion_tokens'}:
        raise EvalError('Endpoint must advertise reasoning and a generation token limit')
    evidence = effort_evidence(settings, cap, endpoint, stage)
    if evidence['status'] == 'unverified':
        raise EvalError('Reasoning effort is unverified: ' + evidence['reason'])
    payload = {'model': model, 'messages': messages, 'reasoning': {'effort': effort},
               ('max_tokens' if 'max_tokens' in params else 'max_completion_tokens'): limit, 'stream': False,
               'plugins': [], 'usage': {'include': True},
               'provider': {'only': [provider], 'order': [provider], 'allow_fallbacks': False, 'require_parameters': True}}
    # OpenRouter base slugs also match regional/variant descendants. Exclude
    # every advertised descendant so the selected base tag is not a route pool.
    excluded_variants = sorted(e['tag'] for e in cap['endpoints']
                               if isinstance(e.get('tag'), str) and e['tag'].startswith(provider + '/'))
    if excluded_variants:
        payload['provider']['ignore'] = excluded_variants
    # Researchers and prisoners use free text. Only the separate blinded
    # classifier asks for a machine-readable judgment.
    if stage == 'judge':
        if 'response_format' not in params:
            raise EvalError('Judge endpoint must advertise JSON response_format')
        payload['response_format'] = {'type': 'json_object'}
    for field in ('temperature', 'seed'):
        value = settings.get(field)
        if value is not None:
            if field not in params:
                raise EvalError(f'Endpoint does not support requested {field}')
            if field == 'temperature' and (not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(value) or not 0 <= value <= 2):
                raise EvalError('temperature must be finite and between 0 and 2')
            if field == 'seed' and (not isinstance(value, int) or isinstance(value, bool)):
                raise EvalError('seed must be an integer')
            payload[field] = value
    # Intentionally conservative UTF-8 byte bound plus generous chat framing.
    # It is an estimate, not a provider tokenizer or a hard billing guarantee.
    input_bound = len(encoded(messages)) + 512
    context = endpoint.get('context_length')
    output_max = endpoint.get('max_completion_tokens')
    if not isinstance(context, int) or not isinstance(output_max, int):
        raise EvalError('Endpoint context/output limits unknown; cannot preflight safely')
    if input_bound + limit > context or limit > output_max or input_bound > (endpoint.get('max_prompt_tokens') or context):
        raise EvalError('Full untruncated input plus requested output exceeds endpoint limits')
    estimate, assumptions = estimate_price(payload, endpoint, cap['model'], input_bound, limit)
    return payload, {'input_tokens_upper_estimate': input_bound, 'max_output_tokens_including_reasoning': limit,
                     'estimated_max_usd': estimate, 'endpoint_tag': provider, 'endpoint': endpoint,
                     'reasoning_evidence': evidence, 'pricing_assumptions': assumptions,
                     'routing_assumptions': {'excluded_descendant_tags': excluded_variants, 'reference': 'https://openrouter.ai/docs/guides/routing/provider-selection'},
                     'token_estimate_method': 'UTF-8 message JSON byte length + 512 framing; not exact tokenization'}


def api_key(root):
    key = os.environ.get('OPENROUTER_API_KEY', '').strip()
    env = root / '.env'
    if not key and env.exists():
        for line in read(env).splitlines():
            line = line.strip()
            if line.startswith('OPENROUTER_API_KEY='):
                key = line.split('=', 1)[1].strip().strip('\"\'')
    if not key:
        raise EvalError('Live mode requires OPENROUTER_API_KEY in environment or gitignored .env')
    return key


class Budget:
    def __init__(self, path, max_calls, max_usd):
        self.path, self.max_calls = Path(path), max_calls
        try:
            self.max_usd = Decimal(str(max_usd))
            if not self.max_usd.is_finite() or self.max_usd <= 0 or not isinstance(max_calls, int) or max_calls < 1:
                raise ValueError()
        except (ValueError, InvalidOperation):
            raise EvalError('Budget call count and spending cap must be positive and finite')

    def check(self, estimates):
        previous = [json.loads(line) for line in read(self.path).splitlines()] if self.path.exists() else []
        count = sum(r['calls'] for r in previous)
        spent = sum((Decimal(r['reserved_usd']) for r in previous), Decimal(0))
        total = sum((Decimal(e['estimated_max_usd']) for e in estimates), Decimal(0))
        if count + len(estimates) > self.max_calls or spent + total > self.max_usd:
            raise EvalError(f'Project budget would be exceeded: {count} reserved calls + {len(estimates)} proposed (cap {self.max_calls}); ${spent} reserved + ${total} estimated (cap ${self.max_usd}). Inspect data/budget.jsonl; explicitly raise --max-calls/--max-usd if intended. No generation sent.')
        return {'previous_reserved_calls': count, 'previous_reserved_usd': str(spent),
                'proposed_calls': len(estimates), 'proposed_estimated_usd': str(total),
                'max_calls': self.max_calls, 'max_usd': str(self.max_usd), 'reservation_made': False}

    def reserve(self, estimates, run_id):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.with_suffix('.lock').open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            checked = self.check(estimates)
            total = Decimal(checked['proposed_estimated_usd'])
            append_json(self.path, {'utc': utc(), 'run_id': run_id, 'calls': len(estimates), 'reserved_usd': str(total)})
            # Reservations include failures/unknown transport outcomes; never automatically refund/retry.


def post(payload, key, folder, allow_nonaction=False):
    body = encoded(payload)
    (folder / 'request.json').write_bytes(body)
    req = urllib.request.Request(BASE + '/chat/completions', data=body,
          headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json'}, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=180) as response:
            raw = response.read()
            metadata = {'status': response.status, 'headers': dict(response.headers)}
    except urllib.error.HTTPError as error:
        raw = error.read()
        (folder / 'response.raw').write_bytes(raw)
        write_json(folder / 'transport.json', {'status': error.code})
        raise EvalError(f'OpenRouter HTTP {error.code}; raw error saved; no retry') from error
    except (OSError, urllib.error.URLError) as error:
        raise EvalError(f'OpenRouter transport failed ({type(error).__name__}); billing outcome unknown, no retry') from error
    (folder / 'response.raw').write_bytes(raw)
    write_json(folder / 'transport.json', metadata)
    try:
        data = json.loads(raw)
        choice = data['choices'][0]
        # Always preserve content even on truncation/refusal/route mismatch.
        text = choice['message'].get('content')
        if isinstance(text, str):
            (folder / 'output.txt').write_bytes(text.encode('utf-8'))
        if data.get('error') or len(data['choices']) != 1 or choice.get('finish_reason') != 'stop':
            raise EvalError('Error or incomplete generation (finish reason is not stop)')
        if data.get('model') != payload['model']:
            raise EvalError('Returned model differs from explicit selected model; review raw response')
        if allow_nonaction and (isinstance(text, str) or text is None):
            # A prisoner's empty or refused *action* is an observed OTHER,
            # not a lost trial. A model transport/finish failure still fails.
            if text is None:
                text = ''
                (folder / 'output.txt').write_bytes(b'')
            return data, text
        if not isinstance(text, str) or not text.strip() or choice['message'].get('refusal'):
            raise EvalError('Empty/nontext/refused output')
        return data, text
    except (KeyError, IndexError, TypeError, json.JSONDecodeError) as error:
        raise EvalError('Malformed OpenRouter response; raw bytes saved') from error


def run(root, args):
    stage = args.stage
    live = args.execute or args.confirm_billable
    if live and not (args.execute and args.confirm_billable):
        raise EvalError('Live generation requires BOTH --execute and --confirm-billable')
    if live:
        key = api_key(root)
    settings = json.loads(read(args.settings))
    allowed = {'model', 'provider_tag', 'researcher', 'prisoner', 'temperature', 'seed', 'provider_effort_review', 'reasoning_override'}
    if not isinstance(settings, dict) or set(settings) - allowed:
        raise EvalError('Unknown settings fields; credentials belong only in environment or .env')
    for name in ('researcher', 'prisoner'):
        if not isinstance(settings.get(name), dict) or set(settings[name]) != {'effort', 'max_tokens'}:
            raise EvalError(f'{name} settings must contain exactly effort and max_tokens')
    item = assignment(root, args.assignment)
    hashes = template_hashes(root, item)
    essay_info, essay_text = None, None
    if stage == 'researcher':
        source, source_info = load_source(root, item['source_id'])
        message_sets = [researcher(root, item, source, source_info)]
        source_record = source_identity(item['source_id'], source, source_info)
        source_record['theory'] = item['theory_label']
        source_hash = sha(source)
        essay_id = str(uuid.uuid4())
        scenario = None
    else:
        if not args.essay:
            raise EvalError('Prisoner stage requires --essay pointing to a completed researcher run directory')
        essay_dir = Path(args.essay)
        essay_info = json.loads(read(essay_dir / 'essay.json'))
        if not settings.get('provider_tag'):
            settings['provider_tag'] = essay_info.get('provider_tag')
        essay_text = read(essay_dir / 'essay.md')
        if (essay_info.get('status') != 'success' or essay_info.get('assignment') != args.assignment or
            essay_info.get('essay_sha256') != sha(essay_text) or essay_info.get('model') != settings['model'] or
            essay_info.get('provider_tag') != settings['provider_tag']):
            raise EvalError('Essay status, assignment, hash, model or pinned-provider provenance mismatch')
        # Recheck raw response to prevent accidentally using an edited essay export.
        original = json.loads((essay_dir / 'call_0/response.raw').read_bytes())
        if original['choices'][0]['message']['content'] != essay_text:
            raise EvalError('Frozen essay differs from exact model output')
        scenario = next((c for c in cases(root) if c['case_id'] == args.scenario), None)
        if scenario is None:
            raise EvalError(f'Unknown active observation scenario: {args.scenario}')
        message_sets = prisoners(root, item, essay_text, scenario)
        if original.get('model') != settings['model'] or original['choices'][0].get('finish_reason') != 'stop':
            raise EvalError('Essay raw response model/finish provenance mismatch')
        fields = ('source_id', 'source_revision', 'source_revision_timestamp', 'source_permanent_url', 'source_sha256', 'source_provenance_sha256', 'theory')
        source_record = {field: essay_info.get(field) for field in fields}
        if source_record['theory'] is not None and source_record['theory'] != item['theory_label']:
            raise EvalError('Assignment theory label differs from the frozen researcher artifact')
        source_hash, essay_id = essay_info['source_sha256'], essay_info['essay_id']
    cap = ((getattr(args, 'fresh_capabilities', None) or snapshot(settings.get('model'))) if live else
           (json.loads(read(args.capabilities)) if args.capabilities else None))
    selection = {'policy': 'frozen essay endpoint' if stage == 'prisoner' else 'explicit provider tag', 'selected_endpoint': settings.get('provider_tag')}
    if cap and not settings.get('provider_tag'):
        checks = [(stage, m) for m in message_sets]
        if stage == 'researcher':
            checks.append(('prisoner', [{'role': 'user', 'content': ''}]))
        settings, selection = choose_endpoint(settings, cap, checks, validate_settings)
    payloads, estimates = [], []
    for messages in message_sets:
        if cap:
            payload, estimate = validate_settings(settings, cap, stage, messages)
            payloads.append(payload)
            estimates.append(estimate)
    request_hashes = [sha(encoded(p)) for p in payloads]
    expected = getattr(args, 'expected_request_hashes', None)
    if expected is not None and request_hashes != expected:
        raise EvalError('Prepared request content changed. Re-prepare and inspect the new prompts/settings; previous approval is invalid. No generation was sent.')
    expected_source = getattr(args, 'expected_source_identity', None)
    if expected_source is not None and source_scope(source_record) != expected_source:
        raise EvalError('Source revision/text changed since pilot preparation. Prepare a new pilot for the changed source; no generation was sent.')
    authorization = {}
    if live:
        batch_scope = getattr(args, 'batch_approval_scope', None)
        if batch_scope is not None:
            # A batch approval authorizes reviewed *templates* to be instantiated
            # with different model-generated essays/observations. It must not be
            # misrepresented as manual approval of each final request's bytes.
            authorization['batch_dynamic_templates'] = approve(root, 'batch_dynamic_templates', batch_scope)
            authorization['approval_kind'] = 'reviewed_template_with_variable_essay'
            authorization['generated_request_hashes'] = request_hashes
        else:
            authorization['prompts'] = approve(root, 'prompts', {'request_hashes': request_hashes}, args.prompts_approved)
            authorization['approval_kind'] = 'exact_requests'
    cfg = load_yaml(root / 'configs/early_test.yaml')
    max_calls = args.max_calls if args.max_calls is not None else cfg['mode']['max_paid_calls']
    max_usd = args.max_usd if args.max_usd is not None else cfg['mode']['max_estimated_spend_usd']
    # Unique directories prevent clobbering any earlier result/commitment.
    run_id = getattr(args, 'run_id', None) or str(uuid.uuid4())
    exploratory = bool(getattr(args, 'exploratory', False))
    artifact_root = root / ('data/exploratory' if exploratory else 'data')
    folder = artifact_root / 'runs' / run_id
    folder.mkdir(parents=True, exist_ok=False)
    for i, messages in enumerate(message_sets):
        export_messages(folder, f'messages_{i}', messages)
    plan = {**source_record, 'run_id': run_id, 'exploratory': exploratory, 'pilot_id': getattr(args, 'pilot_id', None), 'stage': stage, 'assignment': args.assignment, 'live': bool(live),
            'essay_id': essay_id, 'scenario_id': scenario['case_id'] if scenario else None,
            'template_hashes': hashes, 'source_sha256': source_hash,
            'essay_sha256': sha(essay_text) if essay_text is not None else None,
            'settings': settings, 'endpoint_selection': selection, 'authorization': authorization,
            'request_hashes': request_hashes, 'capabilities_sha256': sha(encoded(cap)) if cap else None,
            'message_hashes': [sha(encoded(m)) for m in message_sets],
            'max_calls': max_calls, 'max_estimated_usd': str(max_usd), 'estimates': estimates,
            'estimated_total_usd': str(sum((Decimal(e['estimated_max_usd']) for e in estimates), Decimal(0))) if estimates else None,
            'validation': 'validated' if cap else 'NOT VALIDATED: supply selected model/settings and --capabilities; no price estimate available',
            'source_approval_required': False, 'prompt_approval_acknowledged': bool(args.prompts_approved)}
    for i, payload in enumerate(payloads):
        (folder / f'request_{i}.json').write_bytes(encoded(payload))
    write_json(folder / 'plan.json', plan)
    if cap:
        write_json(folder / 'capabilities.json', cap)
    if not live:
        return folder
    if not payloads:
        raise EvalError('Live mode requires capability validation')
    Budget(root / 'data/budget.jsonl', max_calls, max_usd).reserve(estimates, run_id)
    game = Game(artifact_root / 'commitments.jsonl', run_id)
    fingerprints = []
    decisions = []
    log = artifact_root / ('researcher_essays.jsonl' if stage == 'researcher' else 'prisoner_decisions.jsonl')
    for i, payload in enumerate(payloads):
        call_dir = folder / f'call_{i}'
        call_dir.mkdir()
        record = {**source_record, 'assignment': args.assignment, 'exploratory': exploratory,
                  'pilot_id': getattr(args, 'pilot_id', None), 'reasoning_evidence': estimates[i]['reasoning_evidence'],
                  'reasoning_settings': {name: settings[name] for name in ('researcher', 'prisoner')},
                  'utc': utc(), 'run_id': run_id, 'essay_id': essay_id, 'scenario_id': plan['scenario_id'],
                  'role': 'researcher' if stage == 'researcher' else ('a', 'b')[i],
                  'template_hashes': hashes, 'source_sha256': source_hash, 'essay_sha256': plan['essay_sha256'],
                  'model': settings['model'], 'effort': settings[stage]['effort'], 'provider_tag': settings['provider_tag'],
                  'request_sha256': sha(encoded(payload)), 'status': 'started', 'attempt': 1}
        append_json(log, record)
        try:
            response, output = post(payload, key, call_dir, allow_nonaction=(stage == 'prisoner'))
            returned_tag = response.get('provider_tag') or response.get('provider_endpoint_tag')
            if returned_tag and returned_tag != settings['provider_tag']:
                raise EvalError('Returned endpoint tag differs from the pinned endpoint; no substitution accepted')
            expected_provider = estimates[i]['endpoint'].get('provider_name')
            if response.get('provider') and expected_provider and response['provider'] != expected_provider:
                raise EvalError('Returned provider differs from the pinned endpoint provider')
            record.update(usage=response.get('usage'), finish_reason=response['choices'][0]['finish_reason'],
                          model_version=response.get('model'), fingerprint=response.get('system_fingerprint'),
                          provider=response.get('provider'), returned_endpoint_tag=returned_tag, response_id=response.get('id'),
                          refusal=response['choices'][0]['message'].get('refusal'))
            if stage == 'researcher':
                require_essay_within_limit(output, settings['researcher']['max_tokens'])
                (folder / 'essay.md').write_bytes(output.encode('utf-8'))
                info = {**record, 'status': 'success', 'assignment': args.assignment, 'essay_sha256': sha(output),
                        'researcher_effort': settings['researcher']['effort']}
                write_json(folder / 'essay.json', info)
            else:
                evidence = scenario[f'evidence_{record["role"]}']
                decision = classify_response(output, evidence, scenario[f'evidence_markers_{record["role"]}'],
                                             refused=bool(record['refusal']))
                if decision['enacted_action'] is not None:
                    game.commit(record['role'], decision['enacted_action'])
                # Every generation, including an ambiguous/refused *action*,
                # is preserved as a trial rather than treated as a parse crash.
                record.update(decision=decision, committed_action=decision['enacted_action'],
                              researcher_effort=essay_info['researcher_effort'])
                decisions.append(decision)
                fingerprints.append(response.get('system_fingerprint'))
            record['status'] = 'success'
            append_json(log, record)
        except Exception as error:
            # The exact raw response remains available even when validation fails.
            raw_path = call_dir / 'response.raw'
            if raw_path.exists():
                try:
                    raw_data = json.loads(raw_path.read_bytes())
                    record.update(usage=raw_data.get('usage'), provider=raw_data.get('provider'),
                                  model_version=raw_data.get('model'), response_id=raw_data.get('id'),
                                  finish_reason=(raw_data.get('choices') or [{}])[0].get('finish_reason'))
                except (ValueError, TypeError, AttributeError):
                    pass
            record.update(status='failed', error=str(error))
            append_json(log, record)
            write_json(folder / 'failure.json', record)
            raise EvalError(f'Run failed; artifacts: {folder}; {error}') from error
    if stage == 'prisoner':
        if all(fingerprints) and len(set(fingerprints)) != 1:
            write_json(folder / 'failure.json', {'error': 'Model fingerprints differ; commitments stand but pair excluded'})
            raise EvalError('Model fingerprints differ; no valid matched pair outcome (commitments retained)')
        intent_actions = {'TRIED_COOPERATE': 'WITHHOLD', 'TRIED_DEFECT': 'SUBMIT'}
        intended = [intent_actions.get(d['intent']) for d in decisions]
        enacted = [d['enacted_action'] for d in decisions]
        write_json(folder / 'outcome.json', {
            **(game.outcome() if all(enacted) else {}),
            'status': 'complete' if all(enacted) else 'incomplete_pending_adjudication',
            'pair_id': run_id, 'essay_id': essay_id,
            'intents': [d['intent'] for d in decisions],
            'disclosures': [d['disclosure'] for d in decisions],
            'enacted_actions': enacted,
            'intent_score_if_enacted': score(*intended) if all(intended) else None,
            'enacted_score': game.outcome() if all(enacted) else None,
            'needs_review': [i for i, d in enumerate(decisions) if d['needs_review']],
            'fingerprint_check': 'matched' if all(fingerprints) else 'unavailable; weights/version equality not independently verifiable'})
    return folder

