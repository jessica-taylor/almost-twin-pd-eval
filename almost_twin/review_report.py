"""Offline study-wide review dispositions; never changes scored outcomes.

Source responses and judge outcomes are authoritative; derived result indexes
can be regenerated under the current code without making model calls.
"""

import argparse
import csv
import io
import json
import sys
from collections import Counter
from pathlib import Path

from . import batch, study
from .common import EvalError, read, sha, utc, write_json
from .review_disposition import RULE_ID, disposition


def _csv(path, fields, rows):
    out = io.StringIO()
    writer = csv.DictWriter(out, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
    path.write_text(out.getvalue(), encoding='utf-8')


def write_review_report(root, folder):
    """Reinterpret only *whether review is required*, not A/B game actions."""
    root, folder = Path(root).resolve(), Path(folder).resolve()
    manifest = study._load(root, folder)  # Hash checks, but no generation-code check.
    sample_rows, cell_summaries, input_hashes = [], [], {}
    for cell in manifest['cells']:
        batch_dir = folder / cell['path']
        batch.export(root, batch_dir)  # Validates and rebuilds derived raw records.
        source = batch_dir / 'results.jsonl'
        input_hashes[cell['id']] = sha(source.read_bytes())
        original_rows = [json.loads(line) for line in read(source).splitlines()]
        counters = Counter()
        nonaction_prisoners = 0
        for row in original_rows:
            review = disposition(row)
            counters[review['review_status']] += 1
            nonaction_prisoners += len(review['nonaction_roles'])
            original_actions = row.get('final_actions') or []
            sample_rows.append({
                'cell_id': cell['id'], 'model': cell['model'], 'sample_index': row['sample_index'],
                'sample_id': row['sample_id'], 'raw_status': row['status'],
                'review_status': review['review_status'],
                'human_review_required': review['human_review_required'],
                'nonaction_roles': ','.join(review['nonaction_roles']),
                'review_rule': review['rule'],
                'judge_reason_a': review['judge_reasons'].get('A'),
                'judge_reason_b': review['judge_reasons'].get('B'),
                'final_a': original_actions[0] if len(original_actions) > 0 else None,
                'final_b': original_actions[1] if len(original_actions) > 1 else None,
                'judge_run': row.get('judge_run'), 'prisoner_run': row.get('prisoner_run'),
            })
        cell_summaries.append({
            'cell_id': cell['id'], 'model': cell['model'], 'assignment': cell['assignment'],
            'planned_pairs': len(original_rows),
            'scored_pairs': counters['complete'],
            'resolved_nonaction_pairs': counters['resolved_nonaction'],
            'resolved_unscored_pairs': counters['resolved_unscored'],
            'resolved_nonaction_prisoners': nonaction_prisoners,
            'human_review_pairs': counters['needs_human_review'],
            'other_unscored_pairs': sum(count for status, count in counters.items()
                                        if status not in ('complete', 'resolved_nonaction',
                                                          'resolved_unscored', 'needs_human_review')),
            'status_counts': dict(counters),
        })

    _csv(folder / 'review_samples.csv', (
        'cell_id', 'model', 'sample_index', 'sample_id', 'raw_status', 'review_status',
        'human_review_required', 'nonaction_roles', 'review_rule',
        'judge_reason_a', 'judge_reason_b', 'final_a', 'final_b',
        'judge_run', 'prisoner_run'), sample_rows)
    write_json(folder / 'review_summary.json', {
        'schema_version': 1, 'generated_at_utc': utc(), 'study_id': manifest['study_id'],
        'rule': RULE_ID, 'raw_results_sha256_by_cell': input_hashes,
        'note': 'Offline review annotations. Does not change source responses, judge outcomes, final actions, scores, or primary cooperation estimand.',
        'cell_summaries': cell_summaries})
    lines = ['# Offline study review dispositions', '',
             '**No paid model calls.** Source model responses and judge outcomes '
             'remain unchanged. This report separates unscored, clearly judged '
             'nonactions (including refusals) from genuinely unresolved human-review cases.', '',
             '| Theory | Model | Scored pairs | Resolved nonaction pairs | Other resolved unscored | Human-review pairs | Other unscored |',
             '|---|---|---:|---:|---:|---:|---:|']
    for item in cell_summaries:
        lines.append(f'| {item["assignment"]} | {item["model"]} | {item["scored_pairs"]} | '
                     f'{item["resolved_nonaction_pairs"]} | {item["resolved_unscored_pairs"]} | '
                     f'{item["human_review_pairs"]} | '
                     f'{item["other_unscored_pairs"]} |')
    lines += ['', 'A resolved nonaction requires a judge label of `OTHER`, disclosure `NO`, '
              'and an explicit `needs_human_review=false` for each unscored prisoner. '
              'The current judge schema does not distinguish refusal from other clear '
              'nonparticipation. Other resolved unscored responses have clear intent and '
              'disclosure labels but no valid scored game action. Exact judge explanations '
              'are in `review_samples.csv`. '
              '**Do not score these as cooperation.**', '',
              'Input result hashes and the rule ID are in `review_summary.json`; '
              'source response and judge files are untouched.', '']
    (folder / 'review_summary.md').write_text('\n'.join(lines), encoding='utf-8')
    return folder


def main(argv=None):
    parser = argparse.ArgumentParser(description='Offline post-hoc study review status (no API calls)')
    parser.add_argument('--root', type=Path, default=Path.cwd())
    parser.add_argument('--study', type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        path = write_review_report(args.root, args.study)
    except (EvalError, OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        return 1
    print(f'Wrote {path / "review_summary.md"} and {path / "review_samples.csv"} (offline).')
    return 0


if __name__ == '__main__':
    sys.exit(main())
