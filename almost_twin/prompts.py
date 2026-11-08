"""Literal, single-pass substitutions; model-visible messages contain no run metadata."""
import difflib
import json
import re
from pathlib import Path

from .common import EvalError, encoded, load_yaml, read, sha, write_json

SLOT = re.compile(r'\{\{([A-Z_]+)\}\}')


def mask_private(rendered, observation):
    """For pair audits, mask the known private insertion without visible XML tags."""
    if not isinstance(observation, str) or not observation.strip() or rendered.count(observation) != 1:
        raise EvalError('Private scene text must appear exactly once in the rendered prompt')
    return rendered.replace(observation, '[PRIVATE_OBSERVATION]', 1)


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
        text = fill(read(root / 'prompts/prisoner/base.md'), {
            'THEORY_LABEL': item['theory_label'], 'ESSAY_TEXT': essay,
            'OBSERVATION_RELATION': case['relation'], 'PRIVATE_OBSERVATION': case[f'private_{role}']})
        result.append([{'role': 'user', 'content': text}])
    a, b = (x[0]['content'] for x in result)
    if mask_private(a, case['private_a']) != mask_private(b, case['private_b']):
        raise EvalError('Pair differs outside private observations')
    if case['family'] == 'T0_identical' and a != b:
        raise EvalError('T0 pair is not identical')
    return result


def cases(root):
    return load_yaml(root / 'prompts/prisoner/observation_cases.yaml')['cases']


def export_messages(folder, name, messages):
    write_json(folder / f'{name}.json', messages)
    # The role label is export framing; content below it is exactly model-visible.
    (folder / f'{name}.md').write_bytes(('\n\n'.join(
        f'<!-- message role: {m["role"]} -->\n{m["content"]}' for m in messages)).encode('utf-8'))
    return {'messages_sha256': sha(encoded(messages)),
            'content_sha256': [sha(m['content']) for m in messages]}


def render(root, name, demo=False, essay_path=None, out=None):
    from .sources import load_source
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
    audit = {'assignment': name, 'demo': demo, 'source_sha256': sha(source),
             'essay_sha256': sha(essay) if essay is not None else None,
             'template_hashes': template_hashes(root, item), 'messages': {}}
    audit['messages']['researcher'] = export_messages(folder, 'researcher', researcher(root, item, source, info))
    if essay is not None:
        if not essay.strip():
            raise EvalError('Empty essay')
        for case in cases(root):
            if case['family'] not in ('T0_identical', 'T2_name'):
                continue
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
        for family in ('T0_identical', 'T2_name'):
            index += f'| {family} | [A]({family}/a.md) | [B]({family}/b.md) | [Diff]({family}/pair.diff) |\n'
    (folder / 'index.md').write_text(index, encoding='utf-8')
    return folder
