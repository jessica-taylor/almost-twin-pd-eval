"""Offline, derived per-sample decision reports for existing exploratory batches.

Kept separate from the pinned generation runner so previously prepared batches
remain executable with their original code hashes. No API calls are made.
"""
import argparse
import json
import os
import sys
from pathlib import Path

from .batch import export
from .common import EvalError, read, sha, write_json


def action_label(action):
    if action == 'WITHHOLD':
        return 'Cooperate (WITHHOLD)'
    if action == 'SUBMIT':
        return 'Defect (SUBMIT)'
    return 'Unresolved'


def _at(values, i):
    return values[i] if isinstance(values, list) and len(values) > i else None


def _link(sample, path, suffix, title):
    if not path:
        return None
    target = Path(path) / suffix
    if not target.is_file():
        return None
    relative = os.path.relpath(target, sample)
    return f'- [{title}]({relative})'


def _reasoning_tokens(response):
    usage = response.get('usage') or {}
    if not isinstance(usage, dict):
        return None
    for key in ('completion_tokens_details', 'output_tokens_details'):
        details = usage.get(key) or {}
        if isinstance(details, dict) and details.get('reasoning_tokens') is not None:
            return details['reasoning_tokens']
    return usage.get('reasoning_tokens')


def _transcript_entry(sample, title, stem, run_dir, call):
    """Export exactly what was returned, without attempting to recover hidden reasoning."""
    entry = {'speaker': title, 'call': call, 'status': 'not_run', 'reasoning_status': 'not_provided'}
    if not run_dir:
        return entry
    call_dir = Path(run_dir) / call
    raw_path = call_dir / 'response.raw'
    if not raw_path.is_file():
        entry['status'] = 'no_raw_response'
        return entry
    entry['raw_path'] = str(raw_path)
    entry['raw_sha256'] = sha(raw_path.read_bytes())
    try:
        response = json.loads(raw_path.read_bytes())
    except (ValueError, UnicodeDecodeError):
        entry['status'] = 'unparseable_raw_response'
        return entry
    if not isinstance(response, dict):
        entry['status'] = 'unparseable_raw_response'
        return entry
    entry.update(model=response.get('model'), provider=response.get('provider'),
                 response_id=response.get('id'), reasoning_tokens=_reasoning_tokens(response))
    choices = response.get('choices') or []
    choice = choices[0] if isinstance(choices, list) and choices else {}
    if not isinstance(choice, dict):
        choice = {}
    message = choice.get('message') or {}
    if not isinstance(message, dict):
        message = {}
    entry['finish_reason'] = choice.get('finish_reason') if isinstance(choice, dict) else None
    content = message.get('content')
    folder = sample / 'transcript'
    folder.mkdir(parents=True, exist_ok=True)
    if isinstance(content, str):
        output_path = call_dir / 'output.txt'
        if output_path.is_file() and output_path.read_bytes() != content.encode('utf-8'):
            raise EvalError(f'{title} raw response disagrees with saved output.txt: {call_dir}')
        target = folder / f'{stem}_response.txt'
        target.write_bytes(content.encode('utf-8'))
        entry.update(status='response_available', response_file=str(target.relative_to(sample)),
                     response_sha256=sha(content))
    else:
        entry['status'] = 'no_text_content'

    reasoning = message.get('reasoning')
    if not isinstance(reasoning, str):
        reasoning = message.get('reasoning_content')  # Legacy alias.
    details = message.get('reasoning_details')
    if isinstance(details, list):
        target = folder / f'{stem}_reasoning_details.json'
        write_json(target, details)
        entry['reasoning_details_file'] = str(target.relative_to(sample))
        entry['reasoning_details_types'] = [d.get('type') for d in details if isinstance(d, dict)]
    if isinstance(reasoning, str):
        target = folder / f'{stem}_reasoning.txt'
        target.write_bytes(reasoning.encode('utf-8'))
        entry['reasoning_file'] = str(target.relative_to(sample))
        entry['reasoning_status'] = 'plaintext' if reasoning else 'empty_plaintext'
    elif isinstance(details, list):
        # The full detail blocks are separately saved, including encrypted
        # ones. This convenience text includes only explicitly readable parts.
        readable = []
        for d in details:
            if not isinstance(d, dict):
                continue
            value = d.get('text') if isinstance(d.get('text'), str) else d.get('summary')
            if isinstance(value, str):
                readable.append(f'[{d.get("type", "reasoning detail")}]\n{value}')
        if readable:
            target = folder / f'{stem}_reasoning.txt'
            target.write_text('\n\n'.join(readable), encoding='utf-8')
            entry['reasoning_file'] = str(target.relative_to(sample))
            entry['reasoning_status'] = 'readable_structured_details'
        else:
            entry['reasoning_status'] = 'structured_but_no_readable_text'
    elif message.get('reasoning') is not None:
        target = folder / f'{stem}_reasoning_field.json'
        write_json(target, message['reasoning'])
        entry['reasoning_field_file'] = str(target.relative_to(sample))
        entry['reasoning_status'] = 'nontext_field'
    return entry


def write_transcript(sample, row):
    speakers = [('Researcher', 'researcher', row.get('researcher_run'), 'call_0'),
                ('Prisoner A', 'prisoner_a', row.get('prisoner_run'), 'call_0'),
                ('Prisoner B', 'prisoner_b', row.get('prisoner_run'), 'call_1')]
    if row.get('judge_run'):
        speakers.extend([('Judge for A', 'judge_a', row['judge_run'], 'call_a'),
                         ('Judge for B', 'judge_b', row['judge_run'], 'call_b')])
    entries = []
    lines = [f'# Sample {row["sample_index"]:05d} — model responses and reasoning', '',
             'The files below reproduce the **visible response text** and any **reasoning material actually returned** '
             'by OpenRouter. The linked `response.raw` JSON remains authoritative. '
             'A missing reasoning field does not mean that the model performed no internal reasoning.', '']
    for title, stem, run_dir, call in speakers:
        entry = _transcript_entry(sample, title, stem, run_dir, call)
        entries.append(entry)
        lines.extend([f'## {title}', '', f'Status: `{entry["status"]}`.'])
        if entry.get('reasoning_tokens') is not None:
            lines.append(f'Reasoning tokens reported in usage: `{entry["reasoning_tokens"]}` '
                         '(not necessarily a readable trace).')
        if entry.get('response_file'):
            lines.append(f'- [Complete visible response]({entry["response_file"]})')
        if entry.get('reasoning_file'):
            lines.append(f'- [Readable reasoning returned]({entry["reasoning_file"]}) '
                         f'(`{entry["reasoning_status"]}`)')
        else:
            lines.append(f'- Readable reasoning: **not provided** (`{entry["reasoning_status"]}`).')
        if entry.get('reasoning_details_file'):
            lines.append(f'- [Complete structured reasoning details]({entry["reasoning_details_file"]}) '
                         '(may contain summaries or encrypted blocks).')
        if entry.get('reasoning_field_file'):
            lines.append(f'- [Non-text reasoning field]({entry["reasoning_field_file"]})')
        if entry.get('raw_path'):
            lines.append(_link(sample, run_dir, f'{call}/response.raw', 'Original API response (complete JSON)'))
        lines.append('')
    write_json(sample / 'transcript_index.json', entries)
    (sample / 'transcript.md').write_text('\n'.join(lines), encoding='utf-8')


def render(sample, row):
    status = row['status']
    final = row.get('final_actions') or []
    enacted = row.get('enacted_actions') or []
    intents = row.get('intents') or []
    disclosures = row.get('disclosures') or []
    judge = row.get('judge_outcome') or {}
    judged_intents = judge.get('intents') or []
    judged_disclosures = judge.get('disclosures') or []
    needs_review = row.get('needs_review') or []
    final_score = row.get('final_score') if status == 'complete' else None
    years = (final_score or {}).get('years') or []
    utilities = (final_score or {}).get('utilities') or []

    lines = [f'# Sample {row["sample_index"]:05d} — {status}', '',
             f'Assignment: `{row["assignment"]}` · model: `{row["model"]}` · scenario: `{row["scenario"]}`', '']
    if status == 'complete':
        lines.append(f'**Outcome: Prisoner A — {action_label(_at(final, 0))}; '
                     f'Prisoner B — {action_label(_at(final, 1))}.**')
    elif status == 'pending_judge':
        lines.append('**Classification pending:** at least one response needs judging. '
                     'Any displayed action may be only a parser result.')
    elif status == 'needs_human_review':
        lines.append('**Needs human review:** the judge did not produce a fully scored outcome.')
    else:
        lines.append('**Not a complete scored trial.** See the stage status and saved logs below.')
    lines.extend(['', '## Prisoner decisions', '',
                  '| Prisoner | Current classification | Recognized command | Initial intent | Judge intent | Evidence disclosed (initial / judge) | Years | Utility |',
                  '|---|---|---|---|---|---|---:|---:|'])
    for name, i in (('A', 0), ('B', 1)):
        initial_disclosure = _at(disclosures, i) or '—'
        judge_disclosure = _at(judged_disclosures, i) or '—'
        lines.append('| ' + ' | '.join([
            name, action_label(_at(final, i)), action_label(_at(enacted, i)),
            _at(intents, i) or '—', _at(judged_intents, i) or '—',
            f'{initial_disclosure} / {judge_disclosure}',
            str(_at(years, i)) if _at(years, i) is not None else '—',
            str(_at(utilities, i)) if _at(utilities, i) is not None else '—',
        ]) + ' |')
    lines.extend(['', '**Interpretation:** `WITHHOLD` = cooperate; `SUBMIT` = defect. '
                  'The recognized command is the original parser result. '
                  'A judge can infer intent/disclosure for analysis, but cannot retroactively send evidence '
                  'or alter the fictional commitment journal. Years and utility are shown only for a complete scored outcome.', ''])
    if needs_review:
        labels = ', '.join(('A', 'B')[i] for i in needs_review)
        lines.extend([f'Initial classifier flagged prisoner(s): {labels}.', ''])
    if row.get('needs_human_review'):
        lines.extend([f'Judge requested human review: {row["needs_human_review"]}.', ''])
    if row.get('error'):
        lines.extend(['## Error', '', f'`{row["error"]}`', ''])
    lines.extend(['## Inspect the original model outputs', '',
                  '- [All responses and returned reasoning (transcript)](transcript.md)',
                  '- [Machine-readable transcript index](transcript_index.json)'])
    references = [
        _link(sample, row.get('researcher_run'), 'essay.md', 'Researcher essay'),
        _link(sample, row.get('prisoner_run'), 'call_0/output.txt', 'Prisoner A raw response'),
        _link(sample, row.get('prisoner_run'), 'call_1/output.txt', 'Prisoner B raw response'),
        _link(sample, row.get('prisoner_run'), 'outcome.json', 'Original pair outcome'),
        _link(sample, row.get('judge_run'), 'adjudicated_outcome.json', 'Judge annotations'),
    ]
    lines.extend(x for x in references if x is not None)
    if not any(references):
        lines.append('No model outputs yet.')
    lines.extend(['', 'Full structured record: [result.json](result.json). '
                  'Batch-wide comparisons: [results.csv](../../results.csv) and '
                  '[results.jsonl](../../results.jsonl).',
                  '', 'This report is derived from existing artifacts; running the reporter makes no generation calls.', ''])
    return '\n'.join(lines)


def write_reports(root, batch):
    root, batch = Path(root).resolve(), Path(batch).resolve()
    export(root, batch)  # Validate and rebuild derived indexes; never generate.
    config = json.loads(read(batch / 'batch.json'))
    rows = [json.loads(line) for line in read(batch / 'results.jsonl').splitlines()]
    if len(rows) != len(config['samples']):
        raise EvalError('Mismatched sample count; refusing to create reports')
    for entry, row in zip(config['samples'], rows):
        if row['sample_id'] != entry['sample_id'] or row['sample_index'] != entry['index']:
            raise EvalError('Mismatched sample index or ID; refusing to create reports')
        sample = batch / entry['path']
        write_json(sample / 'result.json', row)
        write_transcript(sample, row)
        (sample / 'result.md').write_text(render(sample, row), encoding='utf-8')
    return rows


def main(argv=None):
    parser = argparse.ArgumentParser(description='Write readable per-sample action reports (offline; no model calls)')
    parser.add_argument('--root', type=Path, default=Path.cwd(), help='Original repository root')
    parser.add_argument('--batch', type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        rows = write_reports(args.root, args.batch)
    except (EvalError, OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        return 1
    print(f'Wrote {len(rows)} per-sample result.md and result.json files in {args.batch}/samples/')
    for row in rows[:20]:
        actions = row.get('final_actions') or []
        print(f'{row["sample_index"]:05d}: A {action_label(_at(actions, 0))}, '
              f'B {action_label(_at(actions, 1))} [{row["status"]}]')
    if len(rows) > 20:
        print(f'... {len(rows) - 20} more samples; see files for the full list.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
