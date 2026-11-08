"""Failure diagnostics derived from saved requests/responses; no retries or network."""
import json
from pathlib import Path

from .common import read


def response_failure(data):
    """Classify provider stop signals without guessing from natural-language text."""
    if not isinstance(data, dict):
        return 'parse_error'
    if data.get('error'):
        return 'provider_error'
    choices = data.get('choices')
    if not isinstance(choices, list) or len(choices) != 1 or not isinstance(choices[0], dict):
        return 'parse_error'
    choice = choices[0]
    if choice.get('finish_reason') == 'length':
        return 'output_token_limit'
    if choice.get('finish_reason') == 'error':
        return 'provider_error'
    if choice.get('finish_reason') == 'content_filter':
        return 'refusal'
    if choice.get('finish_reason') != 'stop':
        return 'incomplete_generation'
    return None


def _json(path):
    try:
        value = json.loads(read(path))
        return value if isinstance(value, dict) else {}
    except (OSError, ValueError):
        return {}


def failure_details(folder, stage, category=None):
    """Read new or historical failed attempts without changing original artifacts.

    Unknown/interrupted and validation failures stay distinct from API errors.
    Token counts include reasoning, exactly as reported by the provider.
    """
    folder = Path(folder)
    record = _json(folder / 'failure.json')
    calls = sorted(p for p in folder.glob('call_*') if p.is_dir())
    call = calls[-1] if calls else folder / 'call_0'
    request = _json(call / 'request.json')
    data = _json(call / 'response.raw')
    usage = data.get('usage') or {}
    usage = usage if isinstance(usage, dict) else {}
    choices = data.get('choices')
    choice = choices[0] if isinstance(choices, list) and choices and isinstance(choices[0], dict) else {}
    message = choice.get('message') or {}
    message = message if isinstance(message, dict) else {}
    content = message.get('content')
    tokens = usage.get('completion_tokens_details') or {}
    tokens = tokens if isinstance(tokens, dict) else {}
    detected = response_failure(data) if (call / 'response.raw').exists() else None
    transport = _json(call / 'transport.json')
    if isinstance(transport.get('status'), int) and transport['status'] >= 400:
        detected = 'provider_error'
    if not detected and stage == 'researcher' and message.get('refusal'):
        detected = 'refusal'
    category = category or record.get('failure_category') or detected
    if not category:
        category = ('validation_error' if record or choice.get('finish_reason') == 'stop' else
                    'unknown_failure' if calls else 'preflight_error')
    return {'failure_category': category, 'failure_stage': stage,
            'completion_tokens': usage.get('completion_tokens'),
            'output_token_limit': request.get('max_tokens', request.get('max_completion_tokens')),
            'reasoning_tokens': tokens.get('reasoning_tokens', usage.get('reasoning_tokens')),
            'essay_words': len(content.split()) if stage == 'researcher' and isinstance(content, str) else None,
            'finish_reason': choice.get('finish_reason'), 'failed_call': call.name}


def sample_failure(row):
    if row.get('status') != 'failed':
        return {}
    candidates = [(stage, Path(row[key])) for stage, key in
                  (('researcher', 'researcher_run'), ('prisoner', 'prisoner_run'), ('judge', 'judge_run'))
                  if row.get(key)]
    for stage, folder in reversed(candidates):
        if (folder / 'failure.json').exists():
            return failure_details(folder, stage)
    if candidates:
        stage, folder = candidates[-1]
        return failure_details(folder, stage)
    return {'failure_category': 'preflight_error', 'failure_stage': None}
