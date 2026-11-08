"""Optional, separately authorized OpenRouter judging of ambiguous responses."""
import json
import uuid
from decimal import Decimal
from pathlib import Path

from .common import EvalError, append_json, encoded, read, sha, utc, write_json
from .game import score
from .judge import parse_judge_response, prepare_adjudication
from .router import Budget, api_key, post, snapshot, validate_settings


def _action(intent, disclosure):
    if intent == 'TRIED_COOPERATE' and disclosure == 'NO':
        return 'WITHHOLD'
    if intent == 'TRIED_DEFECT' and disclosure == 'YES':
        return 'SUBMIT'
    return None


def run_judge(root, args):
    """Dry-run by default; judges only the original run's flagged responses."""
    root, prisoner_dir = Path(root), Path(args.run)
    pair = json.loads(read(prisoner_dir / 'plan.json'))
    if pair.get('stage') != 'prisoner':
        raise EvalError('Judge input must be a completed prisoner pair')
    original = json.loads(read(prisoner_dir / 'outcome.json'))
    uncertain_indices = original['needs_review']
    if not isinstance(uncertain_indices, list) or any(i not in (0, 1) for i in uncertain_indices):
        raise EvalError('Invalid original review indices')

    judge_dir = prepare_adjudication(root, prisoner_dir)
    settings = json.loads(read(args.settings))
    allowed = {'model', 'provider_tag', 'judge', 'temperature', 'seed', 'provider_effort_review'}
    if (not isinstance(settings, dict) or set(settings) - allowed or
            not isinstance(settings.get('judge'), dict) or
            set(settings['judge']) != {'effort', 'max_tokens'}):
        raise EvalError('Judge settings must specify model/provider and judge effort/max_tokens')
    live = args.execute or args.confirm_billable
    if live and not (args.execute and args.confirm_billable and args.prompts_approved):
        raise EvalError('Live judging requires --execute, --confirm-billable, and --prompts-approved')
    key = api_key(root) if live and uncertain_indices else None
    cap = snapshot(settings.get('model')) if live and uncertain_indices else (
        json.loads(read(args.capabilities)) if args.capabilities else None)

    roles = [('a', 0), ('b', 1)]
    chosen = [(role, i, json.loads(read(judge_dir / f'{role}.json')))
              for role, i in roles if i in uncertain_indices]
    payloads, estimates = [], []
    if cap:
        for role, i, messages in chosen:
            payload, estimate = validate_settings(settings, cap, 'judge', messages)
            payloads.append(payload)
            estimates.append(estimate)

    run_id = str(uuid.uuid4())
    output = root / 'data/judge_runs' / run_id
    output.mkdir(parents=True, exist_ok=False)
    write_json(output / 'plan.json', {
        'judge_run_id': run_id, 'prisoner_run_id': pair['run_id'],
        'judge_model': settings['model'], 'provider_tag': settings['provider_tag'],
        'settings': settings, 'live': bool(live),
        'roles_to_judge': [role for role, _, _ in chosen],
        'judge_template_sha256': sha((root / 'prompts/judge/intent.md').read_bytes()),
        'prompt_hashes': [sha(encoded(messages)) for _, _, messages in chosen],
        'estimates': estimates,
        'estimated_total_usd': str(sum((Decimal(x['estimated_max_usd']) for x in estimates), Decimal(0))) if cap else None,
        'validation': 'validated' if cap else 'NOT VALIDATED: choose endpoint and inspect capabilities'})
    for role, _, messages in chosen:
        write_json(output / f'messages_{role}.json', messages)
    if not live:
        return output
    if not cap and chosen:
        raise EvalError('Live judging requires validated model/provider capabilities')
    if chosen:
        Budget(root / 'data/judge_budget.jsonl', args.max_calls, args.max_usd).reserve(estimates, run_id)

    judgements = {}
    for j, (role, i, _) in enumerate(chosen):
        call_dir = output / f'call_{role}'
        call_dir.mkdir()
        record = {'judge_run_id': run_id, 'prisoner_run_id': pair['run_id'],
                  'role': role, 'model': settings['model'], 'utc': utc(), 'status': 'started'}
        append_json(root / 'data/judge_decisions.jsonl', record)
        try:
            response, raw_label = post(payloads[j], key, call_dir)
            expected_provider = estimates[j]['endpoint'].get('provider_name')
            if response.get('provider') and expected_provider and response['provider'] != expected_provider:
                raise EvalError('Returned judge provider differs from the pinned endpoint provider')
            label = parse_judge_response(raw_label)
            record.update(status='success', label=label, response_id=response.get('id'),
                          usage=response.get('usage'), provider=response.get('provider'),
                          model_version=response.get('model'))
            judgements[role] = label
            write_json(call_dir / 'label.json', label)
            append_json(root / 'data/judge_decisions.jsonl', record)
        except Exception as error:
            record.update(status='failed', error=str(error))
            append_json(root / 'data/judge_decisions.jsonl', record)
            write_json(output / 'failure.json', record)
            raise EvalError(f'Judge run failed; raw artifacts: {output}; {error}') from error

    intents, disclosures = list(original['intents']), list(original['disclosures'])
    for role, i in roles:
        if role in judgements:
            intents[i] = judgements[role]['intent']
            disclosures[i] = judgements[role]['disclosure']
    adjudicated = [_action(intent, disclosure) for intent, disclosure in zip(intents, disclosures)]
    human_review = [role for role, label in judgements.items() if label['needs_human_review']]
    write_json(output / 'adjudicated_outcome.json', {
        'prisoner_run_id': pair['run_id'], 'judge_run_id': run_id,
        'judgements': judgements, 'intents': intents, 'disclosures': disclosures,
        'adjudicated_actions': adjudicated, 'needs_human_review': human_review,
        'adjudicated_score': score(*adjudicated) if all(adjudicated) and not human_review else None,
        'note': 'Post hoc labels for analysis only; the original irreversible game journal is unchanged.'})
    return output
