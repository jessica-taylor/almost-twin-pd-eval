"""Independent essay, generation and transport budgets; no network or model calls."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import yaml

from almost_twin.accounting import essay_metrics, max_essay_json_bytes, require_essay_within_limit
from almost_twin.common import EvalError, load_yaml
from almost_twin.limits import api_timeout, essay_limits, output_limit
from almost_twin.router import post
from almost_twin.study import _cells, load_spec

ROOT = Path(__file__).resolve().parents[1]


class LimitTests(unittest.TestCase):
    def load(self, changes):
        spec = load_yaml(ROOT / 'configs/study.smoke.example.yaml')
        spec.update(changes)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'study.yaml'
            path.write_text(yaml.safe_dump(spec))
            return load_spec(path)[0]

    def test_effort_specific_budgets_resolve_all_four_cells(self):
        spec = self.load({'researcher_efforts': ['low', 'high'], 'prisoner_efforts': ['low', 'high']})
        self.assertEqual([(c['researcher_max_tokens'], c['prisoner_max_tokens']) for c in _cells(spec)],
                         [(16000, 6000), (16000, 12000), (32000, 6000), (32000, 12000)])
        self.assertEqual(spec['essay'], {'target_words': [1200, 1500], 'max_words': 2500, 'max_json_bytes': 32000})
        self.assertEqual(spec['api_timeout_seconds'], 600)

    def test_legacy_explicit_limits_are_preserved_and_conflicts_rejected(self):
        spec = self.load({'researcher_efforts': ['low', 'high'], 'researcher_max_tokens': 12000,
                          'prisoner_max_tokens': 3000})
        self.assertTrue(all(c['researcher_max_tokens'] == 12000 and c['prisoner_max_tokens'] == 3000
                            for c in _cells(spec)))
        with self.assertRaisesRegex(EvalError, 'not both'):
            self.load({'researcher_max_tokens': 12000, 'output_tokens': {'researcher': {'low': 16000}}})

    def test_limits_are_strictly_validated(self):
        for change in ({'essay': {'target_words': [1500, 1200]}},
                       {'essay': {'max_words': 1000}}, {'essay': {'max_json_bytes': True}},
                       {'essay': {'max_words': 0}}, {'essay': {'unknown': 3}},
                       {'output_tokens': {'prisoner': {'high': 0}}},
                       {'output_tokens': {'researcher': {'typo': 2000}}},
                       {'output_tokens': {'prisoner': 6000}}, {'api_timeout_seconds': -1},
                       {'api_timeout_seconds': float('inf')}, {'api_timeout_seconds': True}):
            with self.subTest(change=change), self.assertRaises(EvalError):
                self.load(change)
        with self.assertRaisesRegex(EvalError, 'No output token allowance'):
            self.load({'researcher_efforts': ['medium']})
        spec = self.load({'researcher_efforts': ['medium'],
                          'output_tokens': {'researcher': {'medium': 24000}}})
        self.assertEqual(_cells(spec)[0]['researcher_max_tokens'], 24000)

    def test_target_overshoots_are_metrics_and_hard_bounds_are_independent(self):
        for words in (1852, 1853, 2091, 2500):
            text = 'w ' * words
            require_essay_within_limit(text)
            self.assertTrue(essay_metrics(text)['essay_target_exceeded'])
        require_essay_within_limit('x' * 32000)
        with self.assertRaisesRegex(EvalError, 'JSON-encoded size limit'):
            require_essay_within_limit('x' * 32001)
        with self.assertRaisesRegex(EvalError, 'word limit'):
            require_essay_within_limit('w ' * 2501)
        self.assertFalse(essay_metrics('w ' * 1500)['essay_target_exceeded'])
        for effort in ('low', 'high'):
            self.assertIn(output_limit('researcher', effort), (16000, 32000))
            self.assertEqual(max_essay_json_bytes(), 32000)

    def test_custom_timeout_is_used_without_changing_api_payload(self):
        class Response:
            status, headers = 200, {}
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def read(self):
                return json.dumps({'model': 'test/model', 'choices': [
                    {'finish_reason': 'stop', 'message': {'content': 'Essay'}}]}).encode()
        payload = {'model': 'test/model', 'max_tokens': 32000, 'reasoning': {'effort': 'high'}}
        original = copy.deepcopy(payload)
        with tempfile.TemporaryDirectory() as directory, patch('urllib.request.urlopen', return_value=Response()) as http:
            post(payload, 'synthetic-key', Path(directory), timeout_seconds=900)
            self.assertEqual(http.call_args.kwargs['timeout'], 900)
            self.assertEqual(json.loads((Path(directory) / 'request.json').read_text()), original)
        self.assertEqual(payload, original)
        for value in (None, 0, float('nan'), '600'):
            with self.assertRaises(EvalError):
                api_timeout(value)


if __name__ == '__main__':
    unittest.main()
