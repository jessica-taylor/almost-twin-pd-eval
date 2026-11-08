"""Saved-output diagnostics and actual HTTP parsing, with synthetic responses only."""
import json
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError, URLError

from almost_twin.accounting import require_essay_within_limit
from almost_twin.cli import parser
from almost_twin.common import GenerationError, encoded
from almost_twin.failures import failure_details
from almost_twin.prompts import assignment, researcher
from almost_twin.router import post

ROOT = Path(__file__).resolve().parents[1]


class FailureTests(unittest.TestCase):
    def test_word_limit_counts_entire_essay_without_truncating_or_rewriting(self):
        require_essay_within_limit('word ' * 2500)
        with self.assertRaises(GenerationError) as raised:
            require_essay_within_limit('word ' * 2501)
        self.assertEqual(raised.exception.category, 'essay_size_limit')

    def test_uniform_length_prompt_and_16k_cli_defaults(self):
        for name in ('cdt_wikipedia', 'edt_wikipedia', 'fdt_eq4', 'fdt_policy'):
            text = researcher(ROOT, assignment(ROOT, name), 'SYNTHETIC SOURCE',
                              {'title': 'Fixture', 'url': 'https://example.test'})[0]['content']
            self.assertIn('1,200–1,500 words', text)
            self.assertNotIn('Do not exceed 1,800 words', text)
            self.assertIn('brief conclusion', text)
            for forbidden in ('almost-twin', 'prisoner', 'SUBMIT', 'PRIVATE_OBSERVATION'):
                self.assertNotIn(forbidden, text)
        args = parser().parse_args(['pilot', 'prepare', '--assignment', 'cdt_wikipedia',
                                    '--model', 'test/model'])
        self.assertIsNone(args.researcher_max_tokens)

    def test_provider_stops_classified_and_raw_partial_outputs_preserved(self):
        normal = {'model': 'test/model', 'choices': [{'finish_reason': 'stop',
                  'message': {'content': 'visible words'}}],
                  'usage': {'completion_tokens': 12000,
                            'completion_tokens_details': {'reasoning_tokens': 9580}}}
        for case in ('length', 'refusal', 'content_filter', 'empty', 'malformed', 'error', 'bad_message'):
            with self.subTest(case=case), tempfile.TemporaryDirectory() as directory:
                response = json.loads(json.dumps(normal))
                expected = 'parse_error'
                if case in ('length', 'content_filter'):
                    response['choices'][0]['finish_reason'] = case
                    expected = 'output_token_limit' if case == 'length' else 'refusal'
                elif case == 'refusal':
                    response['choices'][0]['message']['refusal'] = 'declined'
                    expected = 'refusal'
                elif case == 'empty':
                    response['choices'][0]['message']['content'] = ''
                elif case == 'error':
                    response = {'error': {'message': 'provider unavailable'}}
                    expected = 'provider_error'
                elif case == 'bad_message':
                    response['choices'][0]['message'] = []
                raw = b'invalid json' if case == 'malformed' else encoded(response)

                class Response:
                    status, headers = 200, {}
                    def __enter__(self): return self
                    def __exit__(self, *args): pass
                    def read(self): return raw

                folder = Path(directory) / 'call_0'
                folder.mkdir()
                with patch('urllib.request.urlopen', return_value=Response()) as http:
                    with self.assertRaises(GenerationError) as raised:
                        post({'model': 'test/model', 'max_tokens': 12000}, 'secret', folder)
                self.assertEqual(raised.exception.category, expected)
                self.assertEqual(http.call_count, 1)
                self.assertEqual((folder / 'response.raw').read_bytes(), raw)
                self.assertNotIn('secret', (folder / 'request.json').read_text())
                if case == 'length':
                    self.assertEqual((folder / 'output.txt').read_text(), 'visible words')
                    details = failure_details(Path(directory), 'researcher')
                    self.assertEqual(details['failure_category'], 'output_token_limit')
                    self.assertEqual(details['completion_tokens'], 12000)
                    self.assertEqual(details['output_token_limit'], 12000)
                    self.assertEqual(details['reasoning_tokens'], 9580)
                    self.assertEqual(details['essay_words'], 2)

    def test_http_and_transport_failures_are_provider_errors_without_retries(self):
        for error in (HTTPError('https://example.test', 429, 'limited', {}, io.BytesIO(b'limited')),
                      URLError('disconnected')):
            with self.subTest(error=type(error).__name__), tempfile.TemporaryDirectory() as directory:
                folder = Path(directory)
                with patch('urllib.request.urlopen', side_effect=error) as http:
                    with self.assertRaises(GenerationError) as raised:
                        post({'model': 'test/model'}, 'secret', folder)
                self.assertEqual(raised.exception.category, 'provider_error')
                self.assertEqual(http.call_count, 1)
                self.assertTrue((folder / 'request.json').exists())
                if isinstance(error, HTTPError):
                    error.close()


if __name__ == '__main__':
    unittest.main()
