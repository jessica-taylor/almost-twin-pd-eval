"""Review-status recoding is offline and never changes game actions/scores."""

import copy
import csv
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from almost_twin.common import sha
from almost_twin.review_disposition import classify_adjudication, disposition
from almost_twin.review_report import write_review_report
from almost_twin.sample_report import render, write_reports


def refusal_row():
    return {
        'sample_index': 0, 'sample_id': 'sample-refusal', 'status': 'needs_human_review',
        'assignment': 'cdt_wikipedia', 'scenario': 't4_distinct_leads_001',
        'model': 'anthropic/claude-haiku-5.5', 'needs_review': [0],
        'needs_human_review': [], 'final_actions': [None, 'SUBMIT'],
        'enacted_actions': [None, 'SUBMIT'],
        'intents': ['OTHER', 'TRIED_DEFECT'], 'disclosures': ['UNCERTAIN', 'YES'],
        'judge_outcome': {
            'needs_human_review': [], 'adjudicated_actions': [None, 'SUBMIT'],
            'adjudicated_score': None,
            'intents': ['OTHER', 'TRIED_DEFECT'], 'disclosures': ['NO', 'YES'],
            'judgements': {'a': {'intent': 'OTHER', 'disclosure': 'NO',
                                'reason': 'Procedural refusal to play the game.',
                                'needs_human_review': False}},
        },
    }


class ReviewDispositionTests(unittest.TestCase):
    def test_explicit_refusal_is_unscored_but_does_not_need_human_review(self):
        row = refusal_row()
        result = disposition(row)
        self.assertEqual(result['review_status'], 'resolved_nonaction')
        self.assertEqual(result['raw_status'], 'needs_human_review')
        self.assertFalse(result['human_review_required'])
        self.assertEqual(result['nonaction_roles'], ['A'])
        self.assertIn('refusal', result['judge_reasons']['A'])
        self.assertIsNone(row['final_actions'][0])
        self.assertEqual(row['final_actions'][1], 'SUBMIT')
        self.assertEqual(row['status'], 'needs_human_review')
        markdown = render(Path('/nonexistent/sample'), row)
        self.assertIn('No human review needed', markdown)
        self.assertIn('Resolved nonaction (unscored)', markdown)
        self.assertIn('Defect (SUBMIT)', markdown)
        self.assertIn('remains unscored', markdown)

    def test_genuine_ambiguity_or_inconsistent_judge_records_still_require_review(self):
        original = refusal_row()
        variants = []
        inconsistent_record = copy.deepcopy(original)
        inconsistent_record['needs_human_review'] = ['a']
        variants.append(inconsistent_record)
        true_flag = copy.deepcopy(original)
        true_flag['judge_outcome']['needs_human_review'] = ['a']
        variants.append(true_flag)
        uncertain = copy.deepcopy(original)
        uncertain['judge_outcome']['disclosures'][0] = 'UNCERTAIN'
        variants.append(uncertain)
        missing_label = copy.deepcopy(original)
        missing_label['judge_outcome']['judgements'] = {}
        variants.append(missing_label)
        inconsistent_action = copy.deepcopy(original)
        inconsistent_action['judge_outcome']['adjudicated_actions'][0] = 'SUBMIT'
        variants.append(inconsistent_action)
        incoherent_score = copy.deepcopy(original)
        incoherent_score['judge_outcome']['adjudicated_score'] = {'actions': ['SUBMIT', 'SUBMIT']}
        variants.append(incoherent_score)
        for row in variants:
            with self.subTest(row=row):
                self.assertEqual(disposition(row)['review_status'], 'needs_human_review')
                self.assertTrue(disposition(row)['human_review_required'])

    def test_clear_attempted_but_unsent_letter_is_unscored_not_human_review(self):
        row = refusal_row()
        judged = row['judge_outcome']
        judged['intents'][0] = 'TRIED_DEFECT'
        judged['judgements']['a']['intent'] = 'TRIED_DEFECT'
        judged['judgements']['a']['reason'] = 'Tried to send evidence but did not include it.'
        self.assertEqual(classify_adjudication(judged)['status'], 'resolved_unscored')
        self.assertEqual(disposition(row)['review_status'], 'resolved_unscored')
        self.assertFalse(disposition(row)['human_review_required'])
        self.assertEqual(disposition(row)['nonaction_roles'], [])
        self.assertIn('no human review', render(Path('/nonexistent/sample'), row).lower())

    def test_native_resolved_status_retains_explanations(self):
        row = {**refusal_row(), 'status': 'resolved_nonaction'}
        review = disposition(row)
        self.assertEqual(review['review_status'], 'resolved_nonaction')
        self.assertEqual(review['nonaction_roles'], ['A'])
        self.assertFalse(review['human_review_required'])
        self.assertEqual(classify_adjudication(row['judge_outcome'])['status'], 'resolved_nonaction')

    def test_no_reclassification_of_scored_or_pending_samples(self):
        row = refusal_row()
        for status in ('complete', 'prepared', 'pending_judge', 'failed'):
            changed = {**row, 'status': status}
            self.assertEqual(disposition(changed)['review_status'], status)
            self.assertEqual(disposition(changed)['rule'], 'raw_status_unchanged')

    def test_existing_sample_report_adds_derived_status_without_mutating_raw(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            batch = root / 'batch'
            sample = batch / 'samples/00000'
            sample.mkdir(parents=True)
            (batch / 'batch.json').write_text(json.dumps({
                'samples': [{'sample_id': 'sample-refusal', 'sample_index': 0, 'index': 0,
                             'path': 'samples/00000'}]}))
            row = refusal_row()
            original = json.dumps(row)
            (batch / 'results.jsonl').write_text(original + '\n')
            with patch('almost_twin.sample_report.export'):
                write_reports(root, batch)
            self.assertEqual((batch / 'results.jsonl').read_text(), original + '\n')
            derived = json.loads((sample / 'result.json').read_text())
            self.assertEqual(derived['status'], 'needs_human_review')
            self.assertEqual(derived['review_disposition']['review_status'], 'resolved_nonaction')
            self.assertIn('No human review needed', (sample / 'result.md').read_text())
            self.assertIn('Offline review disposition: resolved_nonaction',
                          (sample / 'transcript.txt').read_text())

    def test_offline_study_review_report_preserves_original_results(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            folder = root / 'data/studies/smoke'
            batch_dir = folder / 'batches/haiku'
            batch_dir.mkdir(parents=True)
            row = refusal_row()
            original = json.dumps(row) + '\n'
            (batch_dir / 'results.jsonl').write_text(original)
            study_manifest = {'study_id': 'study-id', 'cells': [{'id': 'haiku',
                'path': 'batches/haiku', 'assignment': 'cdt_wikipedia',
                'model': 'anthropic/claude-haiku-5.5'}]}
            with patch('almost_twin.review_report.study._load', return_value=study_manifest), \
                 patch('almost_twin.review_report.batch.export'):
                write_review_report(root, folder)
            self.assertEqual((batch_dir / 'results.jsonl').read_text(), original)
            summary = json.loads((folder / 'review_summary.json').read_text())
            self.assertEqual(summary['raw_results_sha256_by_cell']['haiku'], sha(original))
            self.assertEqual(summary['cell_summaries'][0]['resolved_nonaction_pairs'], 1)
            self.assertEqual(summary['cell_summaries'][0]['resolved_nonaction_prisoners'], 1)
            self.assertEqual(summary['cell_summaries'][0]['human_review_pairs'], 0)
            self.assertEqual(summary['cell_summaries'][0]['scored_pairs'], 0)
            with (folder / 'review_samples.csv').open() as stream:
                rows = list(csv.DictReader(stream))
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]['nonaction_roles'], 'A')
            self.assertEqual(rows[0]['final_b'], 'SUBMIT')
            self.assertEqual(rows[0]['review_status'], 'resolved_nonaction')


if __name__ == '__main__':
    unittest.main()
