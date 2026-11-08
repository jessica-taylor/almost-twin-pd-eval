"""Blinded, offline adjudication packets. No paid judge calls in this module."""
import json
from pathlib import Path

from .common import EvalError, read, sha, write_json
from .game import submit_command
from .prompts import cases, export_messages, fill

INTENTS = ('TRIED_DEFECT', 'TRIED_COOPERATE', 'OTHER')
DISCLOSURES = ('YES', 'NO', 'UNCERTAIN')


def judge_messages(root, evidence, raw_response):
    if not isinstance(raw_response, str):
        raise EvalError('Judge input must be the exact model response as text')
    # The classified response is untrusted data, not instructions to the judge.
    safe_response = raw_response.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    rendered = fill(read(Path(root) / 'prompts/judge/intent.md'), {
        'EVIDENCE_LEAD': evidence, 'SUBMIT_COMMAND': submit_command(evidence),
        'RESPONSE_TEXT': safe_response})
    return [{'role': 'user', 'content': rendered}]


def parse_judge_response(raw):
    def no_duplicate_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise EvalError(f'Duplicate judge output key: {key}')
            result[key] = value
        return result
    try:
        obj = json.loads(raw, object_pairs_hook=no_duplicate_keys)
    except (ValueError, TypeError) as error:
        raise EvalError('Judge output is not exactly one JSON object') from error
    if not isinstance(obj, dict) or set(obj) != {'intent', 'disclosure', 'reason', 'needs_human_review'}:
        raise EvalError('Invalid judge output fields')
    if (obj['intent'] not in INTENTS or obj['disclosure'] not in DISCLOSURES or
            not isinstance(obj['reason'], str) or not obj['reason'].strip() or
            not isinstance(obj['needs_human_review'], bool)):
        raise EvalError('Invalid judge labels, explanation, or review flag')
    return obj


def prepare_adjudication(root, run_dir):
    """Export two blinded judge prompts, without sending them to any model."""
    root, run_dir = Path(root), Path(run_dir)
    plan = json.loads(read(run_dir / 'plan.json'))
    if plan.get('stage') != 'prisoner':
        raise EvalError('Adjudication requires a prisoner-pair run directory')
    case_file = 'prompts/prisoner/observation_cases.yaml'
    saved_case_hash = (plan.get('template_hashes') or {}).get(case_file)
    if not saved_case_hash or saved_case_hash != sha((root / case_file).read_bytes()):
        raise EvalError('Scenario file differs from the prisoner run (or saved hash is missing); cannot adjudicate against changed evidence')
    scenario = next((c for c in cases(root) if c['case_id'] == plan['scenario_id']), None)
    if scenario is None:
        raise EvalError('Unknown scenario in saved run')
    out = run_dir / 'adjudication_prompts'
    out.mkdir(exist_ok=True)
    info = {'scenario_id': scenario['case_id'],
            'judge_template_sha256': sha((root / 'prompts/judge/intent.md').read_bytes()),
            'messages': {}}
    for i, role in enumerate(('a', 'b')):
        path = run_dir / f'call_{i}/output.txt'
        if not path.exists():
            raise EvalError(f'Cannot adjudicate missing raw prisoner output: {path}')
        raw = read(path)
        # ``post`` preserves the raw model response independently of output.txt.
        # A null content is stored as an empty text output for prisoner refusals.
        try:
            original = json.loads((run_dir / f'call_{i}/response.raw').read_bytes())
            model_content = original['choices'][0]['message']['content']
        except (OSError, ValueError, KeyError, IndexError, TypeError) as error:
            raise EvalError(f'Missing or invalid original prisoner response for role {role}') from error
        if model_content is not None and not isinstance(model_content, str):
            raise EvalError(f'Nontext original prisoner response for role {role}')
        if raw != (model_content if model_content is not None else ''):
            raise EvalError(f'Saved output.txt differs from original model response for role {role}')
        messages = judge_messages(root, scenario[f'evidence_{role}'], raw)
        info['messages'][role] = {
            **export_messages(out, role, messages), 'raw_response_sha256': sha(raw)}
    write_json(out / 'audit.json', info)
    return out
