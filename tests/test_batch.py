"""Batch tests use synthetic sources/outputs and mocked OpenRouter transport only."""
import copy
import csv
import json
import os
import shutil
import tempfile
import threading
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
from urllib.parse import parse_qs, urlparse

import yaml

from almost_twin.batch import _approval_scope, _load, export, prepare, run
from almost_twin.common import EvalError, encoded, load_yaml, read, sha, utc, write_json
from almost_twin.sample_report import write_reports
from almost_twin.sources import fetch_one

ROOT = Path(__file__).resolve().parents[1]
NANO = 'openai/gpt-5-nano'
JUDGE = 'openai/gpt-6.1-sol'


def cap_for(model):
    cap = json.loads(read(ROOT / 'tests/fixtures/openrouter/gpt5_nano.json'))
    cap['retrieved_at_utc'] = utc()
    cap['model']['id'] = model
    if model == JUDGE:
        for ep in cap['endpoints']:
            ep['supported_parameters'] = list(set(ep['supported_parameters']) | {'response_format'})
    return cap


class BatchTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        for name in ('configs', 'prompts', 'sources'):
            shutil.copytree(ROOT / name, self.root / name)
        manifest_file = self.root / 'sources/manifest.yaml'
        manifest = load_yaml(manifest_file)
        manifest['sources']['cdt_wikipedia'].update(revision_id=123456, revision_review='approved')
        manifest_file.write_text(yaml.safe_dump(manifest, sort_keys=False))

        def download(url, dest):
            action = parse_qs(urlparse(url).query)['action'][0]
            payload = (ROOT / 'tests/fixtures/mediawiki' /
                       ('revision.json' if action == 'query' else 'parse.json')).read_bytes()
            dest.write_bytes(payload)
            return {'url': url, 'raw_file': dest.name, 'raw_sha256': sha(payload), 'retrieved_at_utc': utc()}
        with patch('almost_twin.sources.download', side_effect=download):
            fetch_one(self.root, 'cdt_wikipedia', manifest['sources']['cdt_wikipedia'], network=True)
        self.folder = self.root / 'data/batches/test'
        self.lock = threading.Lock()
        self.calls = []
        self.essay_number = 0
        self.prisoner_number = 0
        self.judge_number = 0
        for path in ('almost_twin.batch.snapshot', 'almost_twin.pilot.snapshot',
                     'almost_twin.router.snapshot', 'almost_twin.judge_runner.snapshot'):
            patcher = patch(path, side_effect=lambda model: copy.deepcopy(cap_for(model)))
            patcher.start()
            self.addCleanup(patcher.stop)
        for path in ('almost_twin.router.post', 'almost_twin.judge_runner.post'):
            patcher = patch(path, side_effect=self.fake_post)
            patcher.start()
            self.addCleanup(patcher.stop)
        environment = patch.dict(os.environ, {'OPENROUTER_API_KEY': 'test-secret'}, clear=True)
        environment.start()
        self.addCleanup(environment.stop)

    def fake_post(self, payload, key, call_dir, allow_nonaction=False):
        with self.lock:
            self.calls.append(payload)
            if payload['model'] == JUDGE:
                self.judge_number += 1
                output = json.dumps({'intent': 'TRIED_DEFECT', 'disclosure': 'YES',
                                     'reason': 'Explicit evidence and disclosure intent.',
                                     'needs_human_review': False})
            elif not allow_nonaction:
                self.essay_number += 1
                output = f'Synthetic essay #{self.essay_number}: reason according to CDT.'
            else:
                self.prisoner_number += 1
                # Sample 0's first prisoner is ambiguous (and thus judged).
                # Sample 1 follows the exact pass command for both positions.
                output = ('I submit the locker 17 information to the prosecutor.'
                          if self.essay_number == 1 and self.prisoner_number == 1 else 'pass')
        response = {'model': payload['model'], 'provider': 'OpenAI',
                    'system_fingerprint': 'fixed-test-model', 'id': 'mock-' + str(len(self.calls)),
                    'usage': {'prompt_tokens': 20, 'completion_tokens': 8},
                    'choices': [{'finish_reason': 'stop', 'message': {'content': output}}]}
        call_dir.mkdir(parents=True, exist_ok=True)
        (call_dir / 'request.json').write_bytes(encoded(payload))
        (call_dir / 'response.raw').write_bytes(encoded(response))
        (call_dir / 'output.txt').write_text(output, encoding='utf-8')
        return response, output

    def prep_args(self, count=2, extra=None):
        options = dict(count=count, assignment='cdt_wikipedia', model=NANO, scenario='t4_distinct_leads_001',
                       researcher_effort='low', prisoner_effort='low', researcher_max_tokens=12000,
                       prisoner_max_tokens=3000, provider_tag=None, capabilities=None,
                       allow_unverified_effort=None, temperature=None, seed_base=None,
                       judge_model=JUDGE, judge_provider_tag=None, judge_effort='low', judge_max_tokens=1200,
                       judge_capabilities=None, judge_allow_unverified_effort=None, no_judge=False,
                       max_calls=30, max_usd='5.00', judge_max_calls=20, judge_max_usd='5.00',
                       out=self.folder)
        options.update(extra or {})
        return SimpleNamespace(**options)

    def run_args(self, extra=None):
        options = dict(batch=self.folder, execute=True, confirm_billable=True,
                       approve_variable_prompts=True, jobs=1, limit=None, wait_for_lock=False)
        options.update(extra or {})
        return SimpleNamespace(**options)

    def test_preparation_creates_independent_samples_and_no_paid_calls(self):
        folder = prepare(self.root, self.prep_args(count=3))
        self.assertEqual(folder, self.folder)
        self.assertEqual(len(self.calls), 0)
        self.assertEqual(len(json.loads(read(folder / 'batch.json'))['samples']), 3)
        self.assertFalse((self.root / 'data/budget.jsonl').exists())
        rows = [json.loads(x) for x in read(folder / 'results.jsonl').splitlines()]
        self.assertEqual([r['status'] for r in rows], ['prepared'] * 3)
        self.assertNotIn('t4_distinct_leads_001',
                         read(folder / 'samples/00000/researcher/messages_0.md'))
        self.assertNotEqual(
            json.loads(read(folder / 'samples/00000/pilot.json'))['pilot_id'],
            json.loads(read(folder / 'samples/00001/pilot.json'))['pilot_id'])
        write_reports(self.root, folder)
        self.assertIn('Not a complete scored trial', read(folder / 'samples/00000/result.md'))
        self.assertEqual(len(self.calls), 0)

    def test_prepare_autoselects_sol_judge_with_known_long_context_prices(self):
        def metadata(model):
            cap = cap_for(model)
            if model == JUDGE:
                base = next(ep for ep in cap['endpoints'] if ep['tag'] == 'openai')
                base['pricing']['overrides'] = [{
                    'min_prompt_tokens': 272000, 'prompt': '0.000004',
                    'completion': '0.000015', 'input_cache_read': '0.0000002',
                    'input_cache_write': '0.000005',
                }]
            return cap
        with patch('almost_twin.batch.snapshot', side_effect=metadata):
            folder = prepare(self.root, self.prep_args(count=1))
        batch = json.loads(read(folder / 'batch.json'))
        self.assertEqual(batch['judge_settings']['provider_tag'], 'openai')
        self.assertFalse(self.calls)

    def test_full_batch_judges_only_ambiguous_and_exports_one_row_each(self):
        prepare(self.root, self.prep_args())
        run(self.root, self.run_args())
        self.assertEqual(self.essay_number, 2)
        self.assertEqual(self.prisoner_number, 4)
        self.assertEqual(self.judge_number, 1)
        self.assertEqual(len(self.calls), 7)
        rows = [json.loads(x) for x in read(self.folder / 'results.jsonl').splitlines()]
        self.assertEqual(len(rows), 2)
        self.assertEqual([r['status'] for r in rows], ['complete', 'complete'])
        self.assertNotEqual(rows[0]['essay_sha256'], rows[1]['essay_sha256'])
        self.assertEqual(rows[0]['final_actions'], ['SUBMIT', 'WITHHOLD'])
        self.assertEqual(rows[1]['final_actions'], ['WITHHOLD', 'WITHHOLD'])
        self.assertEqual(rows[0]['judge_run_id'] is not None, True)
        self.assertIsNone(rows[1]['judge_run_id'])
        with (self.folder / 'results.csv').open() as stream:
            csv_rows = list(csv.DictReader(stream))
        self.assertEqual(len(csv_rows), 2)
        self.assertEqual(csv_rows[0]['final_a'], 'SUBMIT')
        self.assertTrue(csv_rows[0]['final_score_a'])
        self.assertNotIn('test-secret', read(self.folder / 'results.jsonl'))
        records = [json.loads(x) for x in read(self.root / 'data/approvals.jsonl').splitlines()]
        self.assertEqual(sum(r['kind'] == 'batch_dynamic_templates' for r in records), 1)
        for row in rows:
            self.assertEqual(json.loads(read(Path(row['researcher_run']) / 'plan.json'))['authorization']['approval_kind'],
                             'reviewed_template_with_variable_essay')
            self.assertTrue((Path(row['prisoner_run']) / 'call_1/response.raw').exists())
        write_reports(self.root, self.folder)
        self.assertEqual(len(self.calls), 7)  # Reporting makes no model requests.
        first = read(self.folder / 'samples/00000/result.md')
        self.assertIn('Prisoner A — Defect (SUBMIT); Prisoner B — Cooperate (WITHHOLD)', first)
        self.assertIn('Prisoner A raw response', first)
        self.assertIn('Judge annotations', first)
        self.assertIn('All responses and returned reasoning', first)
        self.assertIn('[results.csv](../../results.csv)', first)
        per_sample = json.loads(read(self.folder / 'samples/00000/result.json'))
        self.assertEqual(per_sample['final_actions'], rows[0]['final_actions'])
        self.assertEqual(per_sample['enacted_actions'], rows[0]['enacted_actions'])
        transcript = read(self.folder / 'samples/00000/transcript.md')
        self.assertIn('Prisoner A', transcript)
        self.assertIn('Judge for A', transcript)
        self.assertIn('Readable reasoning: **not provided**', transcript)
        self.assertIn('### Complete visible response', transcript)
        self.assertIn('I submit the locker 17 information to the prosecutor.', transcript)
        self.assertIn('Synthetic essay #1: reason according to CDT.', transcript)
        self.assertTrue((self.folder / 'samples/00000/transcript/prisoner_a_response.txt').exists())
        self.assertIn('I submit the locker 17 information to the prosecutor.',
                      read(self.folder / 'samples/00000/transcript.txt'))
        self.assertIn('Terminal-friendly full transcript', first)

    def test_clear_refusal_is_terminal_unscored_without_human_review(self):
        """A fictional refusal is not cooperation, an error, or a review case."""
        prepare(self.root, self.prep_args(count=1))
        generated = []

        def scripted_post(payload, key, call_dir, allow_nonaction=False):
            if payload['model'] == JUDGE:
                content = json.dumps({'intent': 'OTHER', 'disclosure': 'NO',
                    'reason': 'Explicitly declines both game commands.',
                    'needs_human_review': False})
            elif allow_nonaction:
                # A plays `pass`; B declines to take any in-game action.
                prompt = payload['messages'][0]['content']
                content = ('I refuse to participate in this game or choose either command.'
                           if 'Rowan\'s signed inventory sheet' in prompt else 'pass')
            else:
                content = 'Synthetic CDT essay.'
            generated.append(content)
            response = {'id': f'mock-{len(generated)}', 'model': payload['model'],
                'provider': 'OpenAI', 'usage': {'prompt_tokens': 20, 'completion_tokens': 8},
                'choices': [{'finish_reason': 'stop', 'message': {'content': content}}]}
            call_dir.mkdir(parents=True, exist_ok=True)
            (call_dir / 'request.json').write_bytes(encoded(payload))
            (call_dir / 'response.raw').write_bytes(encoded(response))
            (call_dir / 'output.txt').write_text(content, encoding='utf-8')
            return response, content

        with patch('almost_twin.router.post', side_effect=scripted_post), \
                patch('almost_twin.judge_runner.post', side_effect=scripted_post):
            run(self.root, self.run_args())
            # A confidently unscored pair must not trigger a second paid call.
            run(self.root, self.run_args())
        self.assertEqual(len(generated), 4)  # Essay, A, B, judge B.
        row = json.loads(read(self.folder / 'results.jsonl').splitlines()[0])
        self.assertEqual(row['status'], 'resolved_nonaction')
        self.assertEqual(row['final_actions'], ['WITHHOLD', None])
        self.assertEqual(row['needs_human_review'], [])
        self.assertIsNone(row['final_score'])
        self.assertEqual(row['judge_outcome']['judgements']['b']['intent'], 'OTHER')
        write_reports(self.root, self.folder)
        result = read(self.folder / 'samples/00000/result.md')
        self.assertIn('No human review needed', result)
        self.assertIn('Resolved nonaction (unscored)', result)
        self.assertNotIn('**Outcome: Prisoner A', result)

    def test_transcript_exposes_returned_reasoning_and_unavailable_traces(self):
        prepare(self.root, self.prep_args(count=1))
        run(self.root, self.run_args())
        row = json.loads(read(self.folder / 'results.jsonl').splitlines()[0])
        researcher = Path(row['researcher_run']) / 'call_0/response.raw'
        prisoner_a = Path(row['prisoner_run']) / 'call_0/response.raw'
        prisoner_b = Path(row['prisoner_run']) / 'call_1/response.raw'
        judge = Path(row['judge_run']) / 'call_a/response.raw'

        # Synthetic variants of OpenRouter's documented non-streaming shapes.
        raw = json.loads(read(researcher))
        raw['choices'][0]['message']['reasoning'] = 'Private-model-reasoning returned as plaintext.'
        raw['usage']['completion_tokens_details'] = {'reasoning_tokens': 18}
        write_json(researcher, raw)
        raw = json.loads(read(prisoner_a))
        raw['choices'][0]['message']['reasoning_details'] = [
            {'type': 'reasoning.text', 'text': 'Considering option A.'},
            {'type': 'reasoning.summary', 'summary': 'Compared possible actions.'},
        ]
        write_json(prisoner_a, raw)
        raw = json.loads(read(prisoner_b))
        raw['choices'][0]['message']['reasoning_details'] = [
            {'type': 'reasoning.encrypted', 'data': 'synthetic-encrypted-payload'},
        ]
        raw['usage']['completion_tokens_details'] = {'reasoning_tokens': 15}
        write_json(prisoner_b, raw)
        raw = json.loads(read(judge))
        raw['choices'][0]['message']['reasoning_content'] = 'Judge rationale via legacy alias.'
        write_json(judge, raw)

        call_count = len(self.calls)
        write_reports(self.root, self.folder)
        self.assertEqual(len(self.calls), call_count)
        sample = self.folder / 'samples/00000'
        self.assertEqual(read(sample / 'transcript/researcher_reasoning.txt'),
                         'Private-model-reasoning returned as plaintext.')
        self.assertEqual(read(sample / 'transcript/prisoner_a_reasoning.txt'),
                         '[reasoning.text]\nConsidering option A.\n\n[reasoning.summary]\nCompared possible actions.')
        self.assertEqual(read(sample / 'transcript/judge_a_reasoning.txt'), 'Judge rationale via legacy alias.')
        self.assertFalse((sample / 'transcript/prisoner_b_reasoning.txt').exists())
        self.assertEqual(json.loads(read(sample / 'transcript/prisoner_b_reasoning_details.json'))[0]['data'],
                         'synthetic-encrypted-payload')
        index = json.loads(read(sample / 'transcript_index.json'))
        self.assertEqual(index[0]['reasoning_tokens'], 18)
        self.assertEqual(index[1]['reasoning_status'], 'readable_structured_details')
        self.assertEqual(index[2]['reasoning_status'], 'structured_but_no_readable_text')
        transcript = read(sample / 'transcript.md')
        self.assertIn('Reasoning tokens reported in usage: `15`', transcript)
        self.assertIn('Original API response (complete JSON)', transcript)
        self.assertIn('Private-model-reasoning returned as plaintext.', transcript)
        self.assertIn('Considering option A.', transcript)
        self.assertIn('Judge rationale via legacy alias.', read(sample / 'transcript.txt'))
        self.assertNotIn('synthetic-encrypted-payload', transcript)

    def test_transcript_escapes_model_markdown_fences_without_truncation(self):
        prepare(self.root, self.prep_args(count=1))
        run(self.root, self.run_args())
        row = json.loads(read(self.folder / 'results.jsonl').splitlines()[0])
        raw_file = Path(row['prisoner_run']) / 'call_1/response.raw'
        raw = json.loads(read(raw_file))
        reasoning = 'A note before.\n```\n## A heading that should stay literal\n```\nA note after.'
        raw['choices'][0]['message']['reasoning'] = reasoning
        write_json(raw_file, raw)
        calls = len(self.calls)
        write_reports(self.root, self.folder)
        self.assertEqual(len(self.calls), calls)
        sample = self.folder / 'samples/00000'
        markdown = read(sample / 'transcript.md')
        text = read(sample / 'transcript.txt')
        self.assertIn('````text\n' + reasoning + '\n````', markdown)
        self.assertIn(reasoning, text)
        self.assertEqual(read(sample / 'transcript/prisoner_b_reasoning.txt'), reasoning)

    def test_resume_only_pending_samples_and_no_double_calls(self):
        prepare(self.root, self.prep_args())
        run(self.root, self.run_args({'limit': 1}))
        self.assertEqual(self.essay_number, 1)
        run(self.root, self.run_args())
        self.assertEqual(self.essay_number, 2)
        self.assertEqual(len(self.calls), 7)
        run(self.root, self.run_args())
        self.assertEqual(len(self.calls), 7)

    def test_concurrent_samples_export_consistent_rows_and_reservations(self):
        prepare(self.root, self.prep_args(count=3))
        run(self.root, self.run_args({'jobs': 2}))
        rows = [json.loads(x) for x in read(self.folder / 'results.jsonl').splitlines()]
        self.assertEqual(len(rows), 3)
        self.assertEqual([r['sample_index'] for r in rows], [0, 1, 2])
        self.assertTrue(all(r['status'] == 'complete' for r in rows))
        self.assertEqual(len({r['essay_sha256'] for r in rows}), 3)
        self.assertEqual(self.essay_number, 3)
        self.assertEqual(self.prisoner_number, 6)
        spent = [json.loads(x) for x in read(self.root / 'data/budget.jsonl').splitlines()]
        self.assertEqual(sum(e['calls'] for e in spent), 9)
        self.assertEqual(len({e['run_id'] for e in spent}), 6)

    def test_partial_prisoner_failure_preserves_raw_artifacts_without_retry(self):
        prepare(self.root, self.prep_args(count=1))
        def fail_second_prisoner(payload, key, call_dir, allow_nonaction=False):
            if allow_nonaction and self.prisoner_number == 1:
                call_dir.mkdir(parents=True, exist_ok=True)
                (call_dir / 'request.json').write_bytes(encoded(payload))
                raise EvalError('Synthetic transport failure during second prisoner')
            return self.fake_post(payload, key, call_dir, allow_nonaction)
        with patch('almost_twin.router.post', side_effect=fail_second_prisoner):
            run(self.root, self.run_args())
        row = json.loads(read(self.folder / 'results.jsonl').splitlines()[0])
        self.assertEqual(row['status'], 'failed')
        self.assertIn('second prisoner', row['error'])
        pair = Path(row['prisoner_run'])
        self.assertTrue((pair / 'call_0/response.raw').exists())
        self.assertTrue((pair / 'failure.json').exists())
        attempted_count = len(self.calls)
        run(self.root, self.run_args())
        self.assertEqual(len(self.calls), attempted_count)

    def test_batch_requires_explicit_variable_prompt_approval(self):
        prepare(self.root, self.prep_args(count=1))
        with self.assertRaisesRegex(EvalError, 'approve-variable-prompts'):
            run(self.root, self.run_args({'approve_variable_prompts': False}))
        self.assertFalse(self.calls)
        self.assertFalse((self.root / 'data/budget.jsonl').exists())

    def test_seed_policy_is_frozen_per_sample_and_export_detects_tampering(self):
        prepare(self.root, self.prep_args(extra={'seed_base': 700}))
        self.assertEqual(_load(self.root, self.folder)['seed_base'], 700)
        first = json.loads(read(self.folder / 'samples/00000/pilot.json'))
        second = json.loads(read(self.folder / 'samples/00001/pilot.json'))
        self.assertEqual([first['settings']['seed'], second['settings']['seed']], [700, 701])
        second['settings']['seed'] = 700
        (self.folder / 'samples/00001/pilot.json').write_bytes(encoded(second))
        with self.assertRaisesRegex(EvalError, 'changed'):
            export(self.root, self.folder)

    def test_no_judge_leaves_ambiguous_response_visible(self):
        prepare(self.root, self.prep_args(count=1, extra={'no_judge': True}))
        run(self.root, self.run_args())
        row = json.loads(read(self.folder / 'results.jsonl').splitlines()[0])
        self.assertEqual(row['status'], 'pending_judge')
        self.assertTrue(row['needs_review'])
        self.assertEqual(self.judge_number, 0)
        run(self.root, self.run_args())  # No duplicate prisoner calls or auto-judging.
        self.assertEqual(len(self.calls), 3)
        write_reports(self.root, self.folder)
        report = read(self.folder / 'samples/00000/result.md')
        self.assertIn('Classification pending', report)
        self.assertIn('Unresolved', report)
        self.assertEqual(len(self.calls), 3)


if __name__ == '__main__':
    unittest.main()
