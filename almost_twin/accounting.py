"""Conservative essay-size planning and offline provider-reported usage accounting.

Nothing here estimates *actual* charges from advertised token rates: a missing
provider cost remains unknown.  The essay bound is enforced before a researcher
output can be passed to prisoners, making the planning ceiling meaningful.
"""

import json
from decimal import Decimal, InvalidOperation
from pathlib import Path

from .common import EvalError, GenerationError, encoded, read
from .limits import essay_limits
from .prompts import prisoners


# Essay ceilings are independent of output tokens (which include reasoning).
EXPECTED_RESEARCHER_OUTPUT_TOKENS = 3000
EXPECTED_PRISONER_OUTPUT_TOKENS = 800
EXPECTED_ESSAY_JSON_BYTES_PER_OUTPUT_TOKEN = 4


def essay_json_bytes(essay):
    """Serialized bytes when inserted into one JSON string (without quotes)."""
    return len(encoded(essay)) - 2


def max_essay_json_bytes(limits=None):
    return essay_limits(limits)['max_json_bytes']


def essay_metrics(essay, limits=None):
    limits = essay_limits(limits)
    words = len(essay.split())
    return {'essay_words': words, 'essay_json_bytes': essay_json_bytes(essay),
            'essay_target_exceeded': words > limits['target_words'][1],
            'essay_below_target': words < limits['target_words'][0], 'essay_limits': limits}


def require_essay_within_limit(essay, limits=None):
    limits = essay_limits(limits)
    count, maximum = essay_json_bytes(essay), limits['max_json_bytes']
    if count > maximum:
        raise GenerationError('essay_size_limit', f'Researcher essay exceeds hard JSON-encoded size limit: '
                        f'{count} bytes > {maximum} bytes (independent essay.max_json_bytes). '
                        'Raw generation preserved; no prisoner request is authorized.')
    words = len(essay.split())
    if words > limits['max_words']:
        raise GenerationError('essay_size_limit',
                              f'Researcher essay exceeds hard word limit: {words} > {limits["max_words"]} '
                              '(whitespace-delimited words, including references and math). '
                              'Raw generation preserved; no prisoner request is authorized.')


def prisoner_input_ceiling(root, item, scenario, limits, endpoint, prisoner_max_tokens):
    """Upper-bound the byte-based input estimator for a valid bounded essay.

    `encoded` uses standard JSON string escaping.  Inserting an essay adds
    exactly `essay_json_bytes(essay)` bytes to the serialized empty-essay
    message, so the separate hard output-size check closes this bound.
    An endpoint can accept a shorter actual essay even if this bound would
    exceed its full context; each live payload is validated independently.
    """
    empty = prisoners(root, item, '', scenario)
    baseline = max(len(encoded(messages)) for messages in empty) + 512
    capacity = min(endpoint['context_length'] - prisoner_max_tokens,
                   endpoint.get('max_prompt_tokens') or endpoint['context_length'])
    if capacity < baseline:
        raise EvalError('Prisoner scenario prompt does not fit the selected endpoint context')
    return min(capacity, baseline + max_essay_json_bytes(limits))


def expected_prisoner_input_tokens(root, item, scenario, limits,
                                   endpoint, prisoner_max_tokens):
    """A labeled planning heuristic; never used for safety caps or reservations."""
    base = max(len(encoded(m)) for m in prisoners(root, item, '', scenario)) + 512
    capacity = prisoner_input_ceiling(root, item, scenario, limits,
                                     endpoint, prisoner_max_tokens)
    typical_bytes = min(max_essay_json_bytes(limits),
                        EXPECTED_ESSAY_JSON_BYTES_PER_OUTPUT_TOKEN * EXPECTED_RESEARCHER_OUTPUT_TOKENS)
    return min(capacity, base + typical_bytes)


def _decimal_cost(value):
    if isinstance(value, bool) or value is None:
        return None
    try:
        amount = Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError):
        return None
    return amount if amount.is_finite() and amount >= 0 else None


def sample_usage(row):
    """Read saved calls only; never contact OpenRouter or infer unreported costs."""
    stages = [('researcher', ('call_0',)), ('prisoners', ('call_0', 'call_1')),
              ('judge', ('call_a', 'call_b'))]
    counts = {'attempted_calls': 0, 'priced_calls': 0, 'unpriced_calls': 0,
              'prompt_tokens': 0, 'completion_tokens': 0}
    total = Decimal(0)
    by_stage = {}
    for stage, calls in stages:
        folder = row.get({'researcher': 'researcher_run', 'prisoners': 'prisoner_run',
                          'judge': 'judge_run'}[stage])
        stage_total = Decimal(0)
        if folder:
            for call in calls:
                path = Path(folder) / call
                raw = path / 'response.raw'
                if not (path / 'request.json').exists() and not raw.exists():
                    continue
                counts['attempted_calls'] += 1
                response = {}
                if raw.is_file():
                    try:
                        response = json.loads(read(raw))
                    except (ValueError, UnicodeDecodeError):
                        pass
                if not isinstance(response, dict):
                    response = {}
                usage = response.get('usage') or {}
                if not isinstance(usage, dict):
                    usage = {}
                amount = _decimal_cost(usage.get('cost'))
                if amount is None:
                    counts['unpriced_calls'] += 1
                else:
                    counts['priced_calls'] += 1
                    total += amount
                    stage_total += amount
                for key in ('prompt_tokens', 'completion_tokens'):
                    value = usage.get(key)
                    if isinstance(value, int) and not isinstance(value, bool) and value >= 0:
                        counts[key] += value
        by_stage[stage] = str(stage_total)
    return {**counts, 'reported_provider_usd': str(total),
            'all_calls_priced': counts['unpriced_calls'] == 0,
            'reported_by_stage_usd': by_stage}
