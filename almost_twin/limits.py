"""Independent visible-essay constraints and effort-specific generation ceilings."""
import math

from .common import EvalError

DEFAULT_ESSAY = {'target_words': [1200, 1500], 'max_words': 2500, 'max_json_bytes': 32000}
DEFAULT_OUTPUT_TOKENS = {'researcher': {'low': 16000, 'high': 32000},
                         'prisoner': {'low': 6000, 'high': 12000}}
DEFAULT_API_TIMEOUT_SECONDS = 600
EFFORTS = {'none', 'minimal', 'low', 'medium', 'high', 'xhigh', 'max'}


def positive_integer(value, field):
    if not isinstance(value, int) or isinstance(value, bool) or value < 1:
        raise EvalError(f'{field} must be a positive integer')
    return value


def essay_limits(value=None):
    if value is not None and (not isinstance(value, dict) or set(value) - set(DEFAULT_ESSAY)):
        raise EvalError('essay must contain only target_words, max_words, max_json_bytes')
    result = {**DEFAULT_ESSAY, **(value or {})}
    target = result['target_words']
    if not isinstance(target, list) or len(target) != 2:
        raise EvalError('essay.target_words must be [minimum, maximum]')
    for bound in target:
        positive_integer(bound, 'essay.target_words')
    for field in ('max_words', 'max_json_bytes'):
        positive_integer(result[field], f'essay.{field}')
    if not target[0] <= target[1] <= result['max_words']:
        raise EvalError('essay.target_words must be ordered and not exceed essay.max_words')
    return {**result, 'target_words': list(target)}


def api_timeout(value=DEFAULT_API_TIMEOUT_SECONDS):
    if (not isinstance(value, (int, float)) or isinstance(value, bool)
            or not math.isfinite(value) or value <= 0):
        raise EvalError('api_timeout_seconds must be a positive finite number')
    return value


def essay_from_args(args):
    value = getattr(args, 'essay', None)
    if value is None:
        value = {key: getattr(args, 'essay_' + key) for key in DEFAULT_ESSAY
                 if getattr(args, 'essay_' + key, None) is not None}
    return essay_limits(value)


def output_budgets(value=None):
    if value is not None and (not isinstance(value, dict) or set(value) - set(DEFAULT_OUTPUT_TOKENS)):
        raise EvalError('output_tokens must contain only researcher and prisoner effort maps')
    result = {}
    for stage, defaults in DEFAULT_OUTPUT_TOKENS.items():
        mapping = (value or {}).get(stage, {})
        if not isinstance(mapping, dict) or set(mapping) - EFFORTS:
            raise EvalError(f'output_tokens.{stage} must map known efforts to positive token limits')
        for effort, limit in mapping.items():
            positive_integer(limit, f'output_tokens.{stage}.{effort}')
        result[stage] = {**defaults, **mapping}
    return result


def output_limit(stage, effort, override=None, budgets=None):
    if override is not None:
        return positive_integer(override, f'{stage}_max_tokens')
    mapping = (budgets or DEFAULT_OUTPUT_TOKENS)[stage]
    if effort not in mapping:
        raise EvalError(f'No output token allowance for {stage} effort={effort}; '
                        f'set output_tokens.{stage}.{effort} or an explicit {stage}_max_tokens. '
                        'No effort or token allowance was substituted.')
    return mapping[effort]
