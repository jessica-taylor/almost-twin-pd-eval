"""Literal, single-pass substitutions; model-visible messages contain no run metadata."""
import difflib
import json
import re
from pathlib import Path

from .common import EvalError, encoded, load_yaml, read, sha, write_json
from .game import submit_command

SLOT = re.compile(r'\{\{([A-Z_]+)\}\}')


def mask_private(rendered, observation, evidence):
    """Mask all role-specific scene/letter slots without visible instrumentation."""
    if not isinstance(observation, str) or not observation.strip() or rendered.count(observation) != 1:
        raise EvalError('Private scene text must appear exactly once in the rendered prompt')
    command = submit_command(evidence)
    # One appearance in the notebook and one inside the suggested letter.
    if rendered.count(command) != 1 or rendered.count(evidence) != 2:
        raise EvalError('Role-specific evidence must occur exactly in notebook and command')
    return (rendered.replace(observation, '[PRIVATE_OBSERVATION]', 1)
            .replace(command, '[PRIVATE_SUBMIT_COMMAND]', 1)
            .replace(evidence, '[PRIVATE_EVIDENCE]', 1))


def fill(template, values):
    slots = set(SLOT.findall(template))
    if slots != set(values):
        raise EvalError(f'Placeholder mismatch: required {sorted(slots)}, supplied {sorted(values)}')
    # Source and essay contents are data: never recursively render placeholders in them.
    return SLOT.sub(lambda m: values[m[1]], template)


def assignment(root, name):
    cfg = load_yaml(root / 'configs/early_test.yaml')
    for item in cfg['assignments']:
        if item['id'] == name:
            return item
    raise EvalError(f'Unknown assignment: {name}')


def template_hashes(root, item):
    paths = ['prompts/researcher/base.md', 'prompts/prisoner/base.md',
             'prompts/prisoner/observation_cases.yaml']
    if item['researcher_focus_file']:
        paths.append(item['researcher_focus_file'])
    return {p: sha((root / p).read_bytes()) for p in paths}


def researcher(root, item, source, source_info):
    focus = read(root / item['researcher_focus_file']) if item['researcher_focus_file'] else ''
    text = fill(read(root / 'prompts/researcher/base.md'), {
        'THEORY_NAME': item['theory_label'], 'FOCUS_INSTRUCTION': focus,
        'SOURCE_TITLE': source_info['title'], 'SOURCE_URL': source_info['url'],
        'SOURCE_TEXT': source})
    return [{'role': 'user', 'content': text}]


def prisoners(root, item, essay, case):
    result = []
    for role in ('a', 'b'):
        evidence = case[f'evidence_{role}']
        text = fill(read(root / 'prompts/prisoner/base.md'), {
            'THEORY_LABEL': item['theory_label'], 'ESSAY_TEXT': essay,
            'OBSERVATION_RELATION': case['relation'], 'PRIVATE_OBSERVATION': case[f'private_{role}'],
            'EVIDENCE_LEAD': evidence, 'SUBMIT_COMMAND': submit_command(evidence)})
        result.append([{'role': 'user', 'content': text}])
    a, b = (x[0]['content'] for x in result)
    if mask_private(a, case['private_a'], case['evidence_a']) != mask_private(b, case['private_b'], case['evidence_b']):
        raise EvalError('Pair differs outside the declared role-specific scene/evidence/command slots')
    if a == b:
        raise EvalError('Every active observation pair must have distinct model-visible prompts')
    return result


def cases(root):
    data = load_yaml(root / 'prompts/prisoner/observation_cases.yaml')
    result = []
    seen_ids, seen_families = set(), set()
    for case in data['cases']:
        c = dict(case)
        for field in ('case_id', 'family', 'relation', 'private_a', 'private_b',
                      'evidence_a', 'evidence_b', 'evidence_markers_a', 'evidence_markers_b'):
            if field not in c or not c[field]:
                raise EvalError(f'Active observation case missing required field: {field}')
        if c['case_id'] in seen_ids or c['family'] in seen_families:
            raise EvalError('Duplicate observation case ID/family would overwrite a rendered preview')
        seen_ids.add(c['case_id'])
        seen_families.add(c['family'])
        if c['private_a'] == c['private_b'] or c['evidence_a'] == c['evidence_b']:
            raise EvalError('Active cases must have different private observations and evidence leads')
        for role in ('a', 'b'):
            submit_command(c[f'evidence_{role}'])
            markers = c[f'evidence_markers_{role}']
            if not isinstance(markers, list) or not markers or any(
                    not isinstance(x, str) or not x.strip() or x.casefold() not in c[f'evidence_{role}'].casefold()
                    for x in markers):
                raise EvalError('Every evidence marker must occur in its own evidence lead')
        result.append(c)
    if not result:
        raise EvalError('No active observation cases')
    return result


def export_messages(folder, name, messages):
    write_json(folder / f'{name}.json', messages)
    # The role label is export framing; content below it is exactly model-visible.
    (folder / f'{name}.md').write_bytes(('\n\n'.join(
        f'<!-- message role: {m["role"]} -->\n{m["content"]}' for m in messages)).encode('utf-8'))
    return {'messages_sha256': sha(encoded(messages)),
            'content_sha256': [sha(m['content']) for m in messages]}


def render(root, name, demo=False, essay_path=None, out=None):
    from .sources import load_source, source_identity
    item = assignment(root, name)
    if demo:
        source = 'SYNTHETIC SOURCE FIXTURE: This is invented placeholder material for offline software inspection. It is not a human-written reference article.'
        info = {'title': 'SYNTHETIC SOURCE FIXTURE', 'url': 'urn:synthetic:source'}
        essay = read(root / 'fixtures/demo_essay.md')
    else:
        source, info = load_source(root, item['source_id'])
        essay = read(essay_path) if essay_path else None
    folder = Path(out) if out else root / 'data/rendered_prompts' / ('demo' if demo else 'source_review') / name
    folder.mkdir(parents=True, exist_ok=True)
    audit = {**source_identity(item['source_id'], source, info), 'assignment': name,
             'theory': item['theory_label'], 'demo': demo, 'source_sha256': sha(source),
             'essay_sha256': sha(essay) if essay is not None else None,
             'template_hashes': template_hashes(root, item), 'messages': {}}
    audit['messages']['researcher'] = export_messages(folder, 'researcher', researcher(root, item, source, info))
    if essay is not None:
        if not essay.strip():
            raise EvalError('Empty essay')
        for case in cases(root):
            pair = prisoners(root, item, essay, case)
            case_dir = folder / case['family']
            case_dir.mkdir(exist_ok=True)
            for role, messages in zip(('a', 'b'), pair):
                audit['messages'][f'{case["family"]}/{role}'] = export_messages(case_dir, role, messages)
            diff = ''.join(difflib.unified_diff(pair[0][0]['content'].splitlines(True),
                       pair[1][0]['content'].splitlines(True), fromfile='a', tofile='b'))
            (case_dir / 'pair.diff').write_bytes(diff.encode('utf-8'))
    write_json(folder / 'audit.json', audit)
    index = '# Rendered prompt review\n\n'
    index += 'Demo uses explicitly synthetic source and essay fixtures.\n\n' if demo else 'Actual source text is included. Any supplied essay is preserved verbatim; inspect its provenance before execution.\n\n'
    index += '[Complete researcher prompt](researcher.md) · [Exact messages JSON](researcher.json) · [Hashes](audit.json)\n\n'
    if essay is not None:
        index += '| Case | Prisoner A | Prisoner B | Precise diff |\n|---|---|---|---|\n'
        for family in (c['family'] for c in cases(root)):
            index += f'| {family} | [A]({family}/a.md) | [B]({family}/b.md) | [Diff]({family}/pair.diff) |\n'
    (folder / 'index.md').write_text(index, encoding='utf-8')
    return folder

