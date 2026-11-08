"""Auditable request-aware capability and price checks. No network or model calls."""
from decimal import Decimal, InvalidOperation

from .common import EvalError

EFFORTS = {'none', 'minimal', 'low', 'medium', 'high', 'xhigh', 'max'}
REASONING_DOC = 'https://openrouter.ai/docs/guides/best-practices/reasoning-tokens'
WEB_DOC = 'https://openrouter.ai/docs/guides/features/plugins/web-search'
CACHE_DOC = 'https://openrouter.ai/docs/guides/best-practices/prompt-caching'
SELECTION_POLICY = 'direct author base tag, then direct author variants, then other tags; within each group sort by tag; require every requested stage to pass preflight; no fallback after pinning'


def effort_evidence(settings, cap, endpoint, stage):
    effort = settings[stage].get('effort')
    if not isinstance(effort, str) or effort not in EFFORTS:
        raise EvalError(f'Unknown reasoning effort {effort!r}; choose one of {sorted(EFFORTS)}')
    for layer in (endpoint, cap['model']):
        if (layer.get('reasoning') or {}).get('mandatory') and effort == 'none':
            raise EvalError('Reasoning is mandatory; effort=none is explicitly unsupported')
    for label, layer in (('endpoint', endpoint), ('model', cap['model'])):
        reasoning = layer.get('reasoning') or {}
        if 'supported_efforts' not in reasoning:
            continue
        supported = reasoning['supported_efforts']
        if supported is not None and (not isinstance(supported, list) or effort not in supported):
            raise EvalError(f'Unsupported reasoning effort {effort!r} in {label} metadata; supported={supported!r}. Choose an advertised effort; overrides cannot bypass an explicit rejection.')
        return {'status': f'verified_by_{label}_metadata', 'selected_effort': effort,
                'supported_efforts': supported, 'evidence_url': REASONING_DOC,
                'meaning': 'null explicitly accepts gateway effort values' if supported is None else 'explicit effort list',
                'scope': 'gateway parameter acceptance, not measured or equivalent reasoning compute'}
    review = settings.get('reasoning_override') or settings.get('provider_effort_review') or {}
    reason = review.get('reason') or review.get('note')
    if effort in review.get('efforts', []) and isinstance(reason, str) and reason.strip():
        return {'status': 'documented_manual_override', 'selected_effort': effort,
                'reason': reason, 'evidence_url': review.get('evidence_url'),
                'scope': 'User assumption; effort support is not verified by metadata. No expiry or silent translation.'}
    return {'status': 'unverified', 'selected_effort': effort,
            'reason': 'Neither endpoint nor model exposes supported_efforts. Use --allow-unverified-effort REASON in pilot prepare, or settings.reasoning_override with efforts and reason. No effort is substituted.'}


def decimal_rate(value, field):
    try:
        rate = Decimal(str(value))
        if not rate.is_finite() or rate < 0:
            raise ValueError()
        return rate
    except (ValueError, InvalidOperation, TypeError) as error:
        raise EvalError(f'Invalid applicable pricing field {field}={value!r}; need a finite nonnegative USD rate or a different endpoint') from error


def estimate_price(payload, endpoint, model_info, input_tokens, output_tokens):
    """Bound supported plain-text requests; never price a requested tool as free."""
    if any(not isinstance(m.get('content'), str) for m in payload['messages']):
        raise EvalError('This price estimator supports plain text messages only; multimodal/tool pricing needs a separate bound')
    if ('web_search_options' in payload and payload['web_search_options'] is not None) or any(payload.get(k) for k in ('tools', 'plugins', 'audio', 'modalities', 'prediction', 'response_format_schema')):
        raise EvalError('Requested tools/plugins/modalities require pricing bounds; the pilot supports ordinary text-only chat')
    model = payload['model'].lower()
    defaults = [endpoint.get('default_parameters') or {}, model_info.get('default_parameters') or {}]
    if (':online' in model or 'search' in model or model.startswith('perplexity/') or
        any(layer.get('automatic_web_search') for layer in (endpoint, model_info)) or
        any(('web_search_options' in d and d['web_search_options'] is not None) or any(d.get(k) for k in ('tools', 'plugins')) for d in defaults)):
        raise EvalError('This model/endpoint may automatically search or enable tools; search charges cannot be bounded here. Select a non-search chat model/endpoint.')
    if endpoint.get('max_tokens_includes_reasoning') is False:
        raise EvalError('Endpoint output limit excludes reasoning; total reasoning charges cannot be bounded. Select an endpoint with a combined output limit.')
    price = endpoint.get('pricing') or {}
    if 'prompt' not in price or 'completion' not in price:
        raise EvalError('Missing prompt/completion prices; refresh metadata or select another endpoint')
    prompt = decimal_rate(price['prompt'], 'prompt')
    completion = decimal_rate(price['completion'], 'completion')
    fixed = decimal_rate(price.get('request', 0), 'request')
    ignored, included = {}, {}
    optional = {'web_search', 'image', 'image_output', 'image_input', 'audio', 'input_audio', 'output_audio',
                'audio_input', 'audio_output', 'input_audio_cache', 'audio_cache_read', 'video', 'video_per_second',
                'file', 'file_search', 'tool_use', 'tool_calls'}
    for field, value in price.items():
        if field in ('prompt', 'completion', 'request'):
            continue
        if field in optional:
            ignored[field] = {'advertised_rate': value, 'reason': 'No tools/plugins, multimodal input/output or search are enabled; automatic-search variants/defaults are rejected.'}
        elif field == 'discount':
            discount = decimal_rate(value, field)
            if discount > 1:
                raise EvalError('Unknown discount convention; cannot bound applicable price. Select another endpoint.')
            ignored[field] = {'advertised_rate': value, 'reason': 'Estimate uses undiscounted prices; no discount savings assumed.'}
        elif field in ('input_cache_read', 'input_cache_write', 'internal_reasoning'):
            included[field] = decimal_rate(value, field)
        elif value in (None, [], {}, '0', 0):
            ignored[field] = {'advertised_rate': value, 'reason': 'No nonzero charge advertised.'}
        else:
            raise EvalError(f'Potentially applicable pricing field {field}={value!r} cannot be bounded (tier overrides/storage/unknown units). Refresh metadata or select a different endpoint with --provider-tag; no generation was sent.')
    # Cache reads replace ordinary input billing. Writes may add a surcharge;
    # count that full rate on every input token, without assuming any cache hit.
    input_rate = max(prompt, included.get('input_cache_read', Decimal(0))) + included.get('input_cache_write', Decimal(0))
    # Reasoning normally shares the output limit and completion price. If a separate
    # rate is advertised, also charge it on the entire output budget (conservative).
    output_rate = completion + included.get('internal_reasoning', Decimal(0))
    total = input_rate * input_tokens + output_rate * output_tokens + fixed
    assumptions = {'request_kind': 'plain-text chat without search/tools/media', 'ignored_fields': ignored,
                   'included_additional_rates': {k: str(v) for k, v in included.items()},
                   'effective_input_usd_per_token': str(input_rate), 'effective_output_usd_per_token': str(output_rate),
                   'fixed_usd_per_request': str(fixed),
                   'cache_policy': 'max(prompt, cache_read) + cache_write on every input token; no cache savings assumed',
                   'reasoning_policy': 'combined visible/reasoning output limit; separate reasoning rate added on entire output budget if advertised',
                   'scope': 'estimated bound from published token/request rates; excludes account-level credit purchase fees/tax; not a provider-enforced dollar cap',
                   'references': [REASONING_DOC, WEB_DOC, CACHE_DOC]}
    return str(total), assumptions


def choose_endpoint(settings, cap, checks, validate):
    """Select once. An explicit override is validated alone, never replaced."""
    requested = settings.get('provider_tag')
    author = settings['model'].split('/')[0].lower()
    def rank(endpoint):
        tag = str(endpoint.get('tag', ''))
        return (0 if tag == author else 1 if tag.startswith(author + '/') else 2, tag)
    candidates = sorted(cap['endpoints'], key=rank)
    if requested:
        candidates = [e for e in candidates if e.get('tag') == requested]
    failures = []
    for endpoint in candidates:
        selected = {**settings, 'provider_tag': endpoint.get('tag')}
        try:
            for stage, messages in checks:
                validate(selected, cap, stage, messages)
            return selected, {'policy': 'explicit override' if requested else SELECTION_POLICY,
                              'selected_endpoint': endpoint['tag'], 'rejected_candidates': failures}
        except EvalError as error:
            failures.append({'endpoint': endpoint.get('tag'), 'reason': str(error)})
    raise EvalError(f'No suitable endpoint for {settings["model"]} (override={requested!r}). '
                    f'Candidates: {failures or "requested tag absent"}. Change the requested limits/efforts or select a documented endpoint; no model was substituted.')
