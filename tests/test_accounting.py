"""Essay-size and saved-response cost accounting, with no network access."""
import json
import tempfile
import unittest
from pathlib import Path

from almost_twin.accounting import (essay_json_bytes, max_essay_json_bytes,
                                    prisoner_input_ceiling, require_essay_within_limit,
                                    sample_usage)
from almost_twin.common import EvalError, encoded
from almost_twin.prompts import assignment, cases, prisoners


ROOT = Path(__file__).resolve().parents[1]


class AccountingTests(unittest.TestCase):
    def test_essay_json_byte_bound_matches_serialized_prisoner_messages(self):
        case = next(c for c in cases(ROOT) if c['case_id'] == 't4_distinct_leads_001')
        item = assignment(ROOT, 'cdt_wikipedia')
        unusual = 'Quotes " backslash \\ newline\n Unicode 🙂 control \u0001'
        empty = prisoners(ROOT, item, '', case)
        filled = prisoners(ROOT, item, unusual, case)
        for base, updated in zip(empty, filled):
            self.assertEqual(len(encoded(updated)) - len(encoded(base)),
                             essay_json_bytes(unusual))
        endpoint = {'context_length': 200000, 'max_prompt_tokens': 200000}
        ceiling = prisoner_input_ceiling(ROOT, item, case, {'max_json_bytes': 800}, endpoint, 3000)
        self.assertEqual(ceiling, max(len(encoded(m)) for m in empty) + 512 + 800)
        self.assertEqual(max_essay_json_bytes({'max_json_bytes': 800}), 800)
        require_essay_within_limit('x' * 800, {'max_json_bytes': 800})
        with self.assertRaisesRegex(EvalError, 'essay exceeds hard JSON-encoded size limit'):
            require_essay_within_limit('x' * 801, {'max_json_bytes': 800})

    def test_usage_tracks_judges_and_never_infers_missing_cost(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            researcher = root / 'researcher' / 'call_0'
            prisoner_a = root / 'prisoners' / 'call_0'
            prisoner_b = root / 'prisoners' / 'call_1'
            judge = root / 'judge' / 'call_a'
            for folder in (researcher, prisoner_a, prisoner_b, judge):
                folder.mkdir(parents=True)
                (folder / 'request.json').write_text('{}')
            (researcher / 'response.raw').write_text(json.dumps({
                'usage': {'prompt_tokens': 100, 'completion_tokens': 30, 'cost': 0.01}}))
            (prisoner_a / 'response.raw').write_text(json.dumps({
                'usage': {'prompt_tokens': 200, 'completion_tokens': 20, 'cost': 0}}))
            (prisoner_b / 'response.raw').write_text(json.dumps({
                'usage': {'prompt_tokens': 200, 'completion_tokens': 40}}))
            (judge / 'response.raw').write_text(json.dumps({
                'usage': {'prompt_tokens': 50, 'completion_tokens': 10, 'cost': '0.002'}}))
            stats = sample_usage({'researcher_run': str(root / 'researcher'),
                                  'prisoner_run': str(root / 'prisoners'),
                                  'judge_run': str(root / 'judge')})
            self.assertEqual(stats['reported_provider_usd'], '0.012')
            self.assertEqual(stats['reported_by_stage_usd']['judge'], '0.002')
            self.assertEqual(stats['prompt_tokens'], 550)
            self.assertEqual(stats['completion_tokens'], 100)
            self.assertEqual(stats['attempted_calls'], 4)
            self.assertEqual(stats['priced_calls'], 3)
            self.assertEqual(stats['unpriced_calls'], 1)
            self.assertFalse(stats['all_calls_priced'])


if __name__ == '__main__':
    unittest.main()
