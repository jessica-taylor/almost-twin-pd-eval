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
from .common import EvalError, read, write_json


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
    lines.extend(['## Inspect the original model outputs', ''])
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
