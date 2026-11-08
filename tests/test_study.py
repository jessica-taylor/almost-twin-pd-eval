"""Study matrix tests. All source downloads and model generations are mocked."""

import copy
import csv
import json
import os
import shutil
import tempfile
import threading
import time
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
from urllib.parse import parse_qs, urlparse

import yaml

from almost_twin.cli import parser
from almost_twin import batch
from almost_twin.common import EvalError, GenerationError, encoded, load_yaml, read, sha, utc
from almost_twin.game import submit_command
from almost_twin.prompts import cases
from almost_twin.sources import fetch_one
from almost_twin.study import check, load_spec, prepare, report, run


ROOT = Path(__file__).resolve().parents[1]
NANO = 'openai/gpt-5-nano'
JUDGE = 'openai/gpt-6.1-sol'


class StudyTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        for name in ('configs', 'prompts', 'sources'):
            shutil.copytree(ROOT / name, self.root / name)
        manifest_path = self.root / 'sources/manifest.yaml'
        manifest = load_yaml(manifest_path)
        manifest['sources']['cdt_wikipedia'].update(revision_id=123456,
                                                    revision_review='approved')
        manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False))

        def download(url, dest):
            action = parse_qs(urlparse(url).query)['action'][0]
            fixture = ROOT / 'tests/fixtures/mediawiki' / (
                'revision.json' if action == 'query' else 'parse.json')
            payload = fixture.read_bytes()
            dest.write_bytes(payload)
            return {'url': url, 'raw_file': dest.name, 'raw_sha256': sha(payload),
                    'retrieved_at_utc': utc()}

        with patch('almost_twin.sources.download', side_effect=download):
            fetch_one(self.root, 'cdt_wikipedia', manifest['sources']['cdt_wikipedia'], network=True)
        self.calls = []

        def metadata(model):
            cap = json.loads(read(ROOT / 'tests/fixtures/openrouter/gpt5_nano.json'))
            cap['retrieved_at_utc'] = utc()
            cap['model']['id'] = model
            if model == JUDGE:
                for endpoint in cap['endpoints']:
                    endpoint['supported_parameters'] = list(
                        set(endpoint['supported_parameters']) | {'response_format'})
            return copy.deepcopy(cap)

        for name in ('almost_twin.study.snapshot', 'almost_twin.batch.snapshot',
                     'almost_twin.pilot.snapshot', 'almost_twin.router.snapshot',
                     'almost_twin.judge_runner.snapshot'):
            p = patch(name, side_effect=metadata)
            p.start()
            self.addCleanup(p.stop)

        def fake_post(payload, key, folder, allow_nonaction=False, timeout_seconds=600):
            self.calls.append(payload)
            content = ('pass' if allow_nonaction else 'Synthetic CDT explanation, independently generated.')
            response = {'id': f'mock-{len(self.calls)}', 'model': payload['model'],
                        'provider': 'OpenAI', 'system_fingerprint': 'same-mock-weights',
                        'usage': {'prompt_tokens': 10, 'completion_tokens': 5,
                                  'cost': '0.002'},
                        'choices': [{'finish_reason': 'stop', 'message': {'content': content}}]}
            folder.mkdir(parents=True, exist_ok=True)
            (folder / 'request.json').write_bytes(encoded(payload))
            (folder / 'response.raw').write_bytes(encoded(response))
            (folder / 'output.txt').write_text(content)
            return response, content

        p = patch('almost_twin.router.post', side_effect=fake_post)
        self.fake_post = fake_post
        p.start()
        self.addCleanup(p.stop)
        p = patch.dict(os.environ, {'OPENROUTER_API_KEY': 'synthetic-test-key'}, clear=True)
        p.start()
        self.addCleanup(p.stop)
        self.config = self.root / 'study_config.yaml'
        self.study = self.root / 'data/studies/v1'
        self.spec = {
            'schema_version': 1, 'name': 'fixture study', 'exploratory': True,
            'assignments': ['cdt_wikipedia'], 'scenario': 't4_distinct_leads_001',
            'count_per_cell': 2, 'models': [{'id': NANO}],
            'researcher_efforts': ['low'], 'prisoner_efforts': ['low', 'high'],
            'judge': {'enabled': True, 'model': JUDGE, 'effort': 'low', 'max_tokens': 1200},
            'budgets': {'max_calls': 30, 'max_usd': '10.00',
                        'judge_max_calls': 30, 'judge_max_usd': '5.00'},
        }
        self.config.write_text(yaml.safe_dump(self.spec, sort_keys=False))

    def prep_args(self):
        return SimpleNamespace(config=self.config, out=self.study)

    def run_args(self, **overrides):
        values = dict(study=self.study, execute=True, confirm_billable=True,
            approve_variable_prompts=True, jobs=2, limit_cells=None, limit_per_cell=None,
            )
        values.update(overrides)
        return SimpleNamespace(**values)

    def test_study_run_concurrency_defaults(self):
        args = parser().parse_args(['study', 'run', '--study', str(self.study)])
        self.assertEqual(args.jobs, 5)
        self.assertEqual(args.provider_jobs, 2)

    def test_preflight_and_preparation_are_unbilled(self):
        spec, data = load_spec(self.config)
        self.assertEqual(spec['output_tokens']['researcher']['low'], 16000)
        self.assertEqual(spec['models'][0]['prisoner_efforts'], ['low', 'high'])
        result, _, _ = check(self.root, spec)
        self.assertEqual(result['expected_cells'], 2)
        self.assertEqual(result['projected_researcher_prisoner_calls'], 12)
        self.assertLess(float(result['projected_researcher_prisoner_usd']),
                        float(result['projected_full_context_ceiling_usd']))
        self.assertLess(float(result['expected_researcher_prisoner_usd']),
                        float(result['projected_researcher_prisoner_usd']))
        self.assertIn('Independent enforced essay.max_json_bytes', result['cost_projection_method'])
        self.assertFalse(result['failures'])
        self.assertEqual(self.calls, [])
        prepare(self.root, self.prep_args())
        self.assertEqual(self.calls, [])
        study = json.loads(read(self.study / 'study.json'))
        self.assertEqual(study['spec_sha256'], sha(data))
        self.assertEqual(len(study['cells']), 2)
        self.assertTrue(all(c['selected_provider_tag'] == 'openai' for c in study['cells']))
        self.assertEqual(json.loads(read(self.study / 'summary.json'))['total_samples'], 4)
        self.assertFalse((self.root / 'data/budget.jsonl').exists())
        with self.assertRaisesRegex(EvalError, 'already exists'):
            prepare(self.root, self.prep_args())

    def test_study_run_resume_report_and_paired_average(self):
        prepare(self.root, self.prep_args())
        with self.assertRaisesRegex(EvalError, 'Live study execution requires'):
            run(self.root, self.run_args(execute=False))
        self.assertEqual(len(self.calls), 0)
        run(self.root, self.run_args(limit_cells=1, limit_per_cell=1))
        self.assertEqual(len(self.calls), 3)
        sample = next((self.study / 'batches').glob('*/samples/00000'))
        self.assertTrue((sample / 'result.md').exists())
        self.assertTrue((sample / 'transcript.txt').exists())
        self.assertTrue((self.study / 'review_summary.md').exists())
        summary = json.loads(read(self.study / 'summary.json'))
        self.assertEqual(summary['total_complete_pairs'], 1)
        run(self.root, self.run_args())
        self.assertEqual(len(self.calls), 12)
        run(self.root, self.run_args())
        self.assertEqual(len(self.calls), 12)
        report(self.root, self.study)
        self.assertEqual(len(self.calls), 12)
        with (self.study / 'pairs.csv').open() as stream:
            pairs = list(csv.DictReader(stream))
        with (self.study / 'decisions.csv').open() as stream:
            decisions = list(csv.DictReader(stream))
        with (self.study / 'summary.csv').open() as stream:
            cells = list(csv.DictReader(stream))
        self.assertEqual(len(pairs), 4)
        self.assertEqual(len(decisions), 8)
        self.assertEqual([c['complete_pairs'] for c in cells], ['2', '2'])
        self.assertEqual([c['cooperation_rate'] for c in cells], ['1.0', '1.0'])
        self.assertTrue(all(p['pair_outcome'] == 'CC' for p in pairs))
        self.assertTrue(all(d['final_action'] == 'WITHHOLD' for d in decisions))
        self.assertEqual(json.loads(read(self.study / 'summary.json'))['status_counts'],
                         {'complete': 4})
        usage = json.loads(read(self.study / 'summary.json'))['provider_usage']
        self.assertEqual(usage['reported_provider_usd'], '0.024')
        self.assertEqual(usage['priced_calls'], 12)
        self.assertEqual(usage['unpriced_calls'], 0)
        self.assertGreaterEqual(usage['recorded_execution_seconds'], 0)
        self.assertIn('$0.024', read(self.study / 'summary.md'))

    def test_effort_matrix_accepts_target_overshoots_and_preserves_exact_essays(self):
        self.spec.update(count_per_cell=1, researcher_efforts=['low', 'high'],
                         prisoner_efforts=['low', 'high'], api_timeout_seconds=420,
                         essay={'target_words': [1000, 1400], 'max_words': 2500, 'max_json_bytes': 32000})
        self.config.write_text(yaml.safe_dump(self.spec, sort_keys=False))
        prepare(self.root, self.prep_args())
        self.assertEqual(self.calls, [])
        checked = json.loads(read(self.study / 'preflight.json'))['validated_cells']
        # Larger researcher reasoning budgets cannot increase permitted prisoner input.
        self.assertEqual(checked[0]['prisoner_input_tokens_upper_estimate'],
                         checked[2]['prisoner_input_tokens_upper_estimate'])
        word_counts = iter((1852, 2091, 1853, 1000))
        original_essays, timeouts = [], []

        def scripted(payload, key, folder, allow_nonaction=False, timeout_seconds=600):
            timeouts.append(timeout_seconds)
            response, content = self.fake_post(payload, key, folder, allow_nonaction)
            if not allow_nonaction:
                self.assertIn('1,000–1,400 words', payload['messages'][0]['content'])
                self.assertNotIn('almost-twin', payload['messages'][0]['content'])
                content = 'w ' * next(word_counts)
                original_essays.append(content)
                response['choices'][0]['message']['content'] = content
                (folder / 'response.raw').write_bytes(encoded(response))
                (folder / 'output.txt').write_text(content)
            return response, content

        with patch('almost_twin.router.post', side_effect=scripted):
            run(self.root, self.run_args(jobs=1, provider_jobs=1))
        self.assertEqual(timeouts, [420] * 12)
        for index, (researcher_tokens, prisoner_tokens) in enumerate(
                ((16000, 6000), (16000, 12000), (32000, 6000), (32000, 12000))):
            researcher_call, a, b = self.calls[index * 3:index * 3 + 3]
            self.assertEqual(researcher_call['max_tokens'], researcher_tokens)
            self.assertEqual([a['max_tokens'], b['max_tokens']], [prisoner_tokens] * 2)
            self.assertEqual(set(researcher_call['reasoning']), {'effort'})
            for prisoner in (a, b):
                self.assertIn(original_essays[index], prisoner['messages'][0]['content'])
        summary = json.loads(read(self.study / 'summary.json'))
        self.assertEqual(summary['status_counts'], {'complete': 4})
        self.assertEqual(sum(c['essays_above_target'] for c in summary['cell_summaries']), 3)
        self.assertIn('Essay target overshoots: 3 / 4', read(self.study / 'summary.md'))

    def test_endpoint_output_maximum_blocks_high_budget_without_substitution(self):
        self.spec['researcher_efforts'] = ['high']
        self.config.write_text(yaml.safe_dump(self.spec, sort_keys=False))
        spec, _ = load_spec(self.config)
        from almost_twin.router import snapshot
        cap = snapshot(NANO)
        for endpoint in cap['endpoints']:
            endpoint['max_completion_tokens'] = 20000
        with patch('almost_twin.study.snapshot', return_value=cap):
            spec['judge']['enabled'] = False
            result, _, _ = check(self.root, spec)
        self.assertTrue(result['failures'])
        self.assertTrue(all('32000' in f['reason'] and '20000' in f['reason'] for f in result['failures']))
        self.assertEqual(self.calls, [])

    def test_study_jobs_overlap_distinct_model_providers(self):
        self.spec.update(count_per_cell=1, prisoner_efforts=['low'], models=[
            {'id': NANO, 'provider_tag': 'openai'},
            {'id': 'openai/gpt-5-other', 'provider_tag': 'azure'},
        ])
        self.config.write_text(yaml.safe_dump(self.spec, sort_keys=False))
        prepare(self.root, self.prep_args())
        active = peak = 0
        mutex = threading.Lock()
        original = batch._timed_sample_live

        def slow_sample(*args):
            nonlocal active, peak
            with mutex:
                active += 1
                peak = max(peak, active)
            try:
                time.sleep(.05)
                return original(*args)
            finally:
                with mutex:
                    active -= 1

        def routed_post(payload, key, folder, allow_nonaction=False, timeout_seconds=600):
            response, content = self.fake_post(payload, key, folder,
                                               allow_nonaction=allow_nonaction)
            if payload['provider']['only'] == ['azure']:
                response['provider'] = 'Azure'
                (folder / 'response.raw').write_bytes(encoded(response))
            return response, content

        with patch('almost_twin.batch._timed_sample_live', side_effect=slow_sample), \
                patch('almost_twin.router.post', side_effect=routed_post):
            run(self.root, self.run_args(jobs=2, provider_jobs=1, limit_per_cell=1))
        self.assertEqual(peak, 2)
        summary = json.loads(read(self.study / 'summary.json'))
        self.assertEqual(summary['total_complete_pairs'], 2)
        self.assertIsNotNone(summary['provider_usage']['last_run_wall_seconds'])
        # Scenarios were truly concurrent, not only their reporting.
        self.assertGreater(summary['provider_usage']['recorded_execution_seconds'],
                           summary['provider_usage']['last_run_wall_seconds'] * .8)

    def test_study_provider_cap_serializes_shared_provider(self):
        # Separate study cells sharing the same selected provider must not
        # bypass the per-provider cap, even when endpoint tags have variants.
        self.spec.update(count_per_cell=1, prisoner_efforts=['low'], models=[
            {'id': NANO, 'provider_tag': 'openai'},
            {'id': 'openai/gpt-5-other', 'provider_tag': 'openai/flex'},
        ])
        self.config.write_text(yaml.safe_dump(self.spec, sort_keys=False))
        prepare(self.root, self.prep_args())
        active = peak = 0
        mutex = threading.Lock()
        original = batch._timed_sample_live

        def slow_sample(*args):
            nonlocal active, peak
            with mutex:
                active += 1
                peak = max(peak, active)
            try:
                time.sleep(.03)
                return original(*args)
            finally:
                with mutex:
                    active -= 1

        with patch('almost_twin.batch._timed_sample_live', side_effect=slow_sample):
            run(self.root, self.run_args(jobs=2, provider_jobs=1))
        self.assertEqual(peak, 1)
        self.assertEqual(json.loads(read(self.study / 'summary.json'))['total_complete_pairs'], 2)

    def test_study_rejects_invalid_provider_concurrency_without_api_calls(self):
        prepare(self.root, self.prep_args())
        with self.assertRaisesRegex(EvalError, 'provider-jobs must be 1..16'):
            run(self.root, self.run_args(provider_jobs=0))
        self.assertEqual(self.calls, [])

    def test_study_reports_judge_resolved_refusals_separately_from_review(self):
        prepare(self.root, self.prep_args())
        calls = []

        def scripted_post(payload, key, folder, allow_nonaction=False, timeout_seconds=600):
            if payload['model'] == JUDGE:
                content = json.dumps({'intent': 'OTHER', 'disclosure': 'NO',
                                      'reason': 'The prisoner explicitly refused to play.',
                                      'needs_human_review': False})
            elif allow_nonaction:
                content = ('I will neither pass nor submit evidence.'
                           if "Rowan's signed inventory sheet" in payload['messages'][0]['content']
                           else 'pass')
            else:
                content = 'Synthetic CDT essay.'
            calls.append(content)
            response = {'id': f'mock-{len(calls)}', 'model': payload['model'],
                'provider': 'OpenAI', 'usage': {'prompt_tokens': 10, 'completion_tokens': 5},
                'choices': [{'finish_reason': 'stop', 'message': {'content': content}}]}
            folder.mkdir(parents=True, exist_ok=True)
            (folder / 'request.json').write_bytes(encoded(payload))
            (folder / 'response.raw').write_bytes(encoded(response))
            (folder / 'output.txt').write_text(content, encoding='utf-8')
            return response, content

        with patch('almost_twin.router.post', side_effect=scripted_post), \
                patch('almost_twin.judge_runner.post', side_effect=scripted_post):
            run(self.root, self.run_args(jobs=1))
            run(self.root, self.run_args(jobs=1))
        self.assertEqual(len(calls), 16)  # 4 scenarios x (researcher, A, B, judge).
        summary = json.loads(read(self.study / 'summary.json'))
        self.assertEqual(summary['status_counts'], {'resolved_nonaction': 4})
        self.assertEqual(summary['total_complete_pairs'], 0)
        self.assertEqual(summary['provider_usage']['unpriced_calls'], 16)
        self.assertTrue(all(item['status_resolved_nonaction'] == 2 for item in summary['cell_summaries']))
        self.assertTrue(all(item['status_needs_human_review'] == 0 for item in summary['cell_summaries']))
        self.assertTrue(all(item['cooperation_rate'] is None for item in summary['cell_summaries']))
        with (self.study / 'pairs.csv').open() as stream:
            pairs = list(csv.DictReader(stream))
        self.assertTrue(all(p['status'] == 'resolved_nonaction' and not p['pair_outcome']
                            for p in pairs))
        self.assertIn('refusals', read(self.study / 'summary.md'))

    def test_modified_study_spec_is_rejected_after_preparation(self):
        prepare(self.root, self.prep_args())
        (self.study / 'specification.yaml').write_text('modified after preparation')
        with self.assertRaisesRegex(EvalError, 'specification changed'):
            report(self.root, self.study)

    def test_oversized_essay_is_preserved_but_prisoners_are_not_called(self):
        self.spec['researcher_max_tokens'] = 20
        self.spec['essay'] = {'max_json_bytes': 160}
        self.config.write_text(yaml.safe_dump(self.spec, sort_keys=False))
        prepare(self.root, self.prep_args())
        sent = []

        def oversized_post(payload, key, folder, allow_nonaction=False, timeout_seconds=600):
            sent.append(payload)
            output = 'x' * 161  # Exceeds the independent 160-byte essay ceiling.
            response = {'id': 'mock-oversize', 'model': payload['model'],
                        'usage': {'prompt_tokens': 10, 'completion_tokens': 5},
                        'choices': [{'finish_reason': 'stop', 'message': {'content': output}}]}
            folder.mkdir(parents=True, exist_ok=True)
            (folder / 'request.json').write_bytes(encoded(payload))
            (folder / 'response.raw').write_bytes(encoded(response))
            (folder / 'output.txt').write_text(output)
            return response, output

        with patch('almost_twin.router.post', side_effect=oversized_post):
            run(self.root, self.run_args(limit_cells=1, limit_per_cell=1))
        self.assertEqual(len(sent), 1)
        self.assertEqual(sent[0]['usage'], {'include': True})
        summary = json.loads(read(self.study / 'summary.json'))
        self.assertEqual(summary['status_counts']['failed'], 1)
        first_cell = json.loads(read(self.study / 'study.json'))['cells'][0]
        sample = self.study / first_cell['path'] / 'samples/00000'
        self.assertIn('essay exceeds hard JSON-encoded size limit', read(sample / 'result.json'))
        self.assertIn('x' * 161, read(sample / 'transcript.txt'))
        self.assertEqual(summary['failed_attempts'][0]['failure_category'], 'essay_size_limit')
        self.assertIn('essay_size_limit', read(self.study / 'failures.csv'))
        self.assertIn('essay_size_limit', read(self.study / 'summary.md'))

    def test_long_essay_fails_without_prisoners_or_retry(self):
        self.spec['prisoner_efforts'] = ['low']
        self.config.write_text(yaml.safe_dump(self.spec, sort_keys=False))
        prepare(self.root, self.prep_args())
        calls = []

        def long_post(payload, key, folder, allow_nonaction=False, timeout_seconds=600):
            calls.append(payload)
            content = 'word ' * 2501
            response = {'model': payload['model'], 'usage': {'completion_tokens': 4000, 'cost': '.01'},
                        'choices': [{'finish_reason': 'stop', 'message': {'content': content}}]}
            folder.mkdir(exist_ok=True)
            (folder / 'request.json').write_bytes(encoded(payload))
            (folder / 'response.raw').write_bytes(encoded(response))
            (folder / 'output.txt').write_text(content)
            return response, content

        with patch('almost_twin.router.post', side_effect=long_post):
            run(self.root, self.run_args(limit_cells=1, limit_per_cell=1))
            # Only the remaining sample in the same cell can run on resume.
            run(self.root, self.run_args(limit_cells=1, limit_per_cell=1))
            run(self.root, self.run_args(limit_cells=1, limit_per_cell=1))
        self.assertEqual(len(calls), 2)
        summary = json.loads(read(self.study / 'summary.json'))
        self.assertEqual(summary['status_counts']['failed'], 2)
        for failure in summary['failed_attempts']:
            self.assertEqual(failure['failure_category'], 'essay_size_limit')
            self.assertEqual(failure['essay_words'], 2501)
            self.assertEqual(failure['failure_stage'], 'researcher')
        for payload in calls:
            self.assertEqual(payload['max_tokens'], 16000)

    def test_http_429_failure_is_reported_without_retry(self):
        prepare(self.root, self.prep_args())
        sent = []

        def rate_limited(payload, key, folder, allow_nonaction=False, timeout_seconds=600):
            sent.append(payload)
            raise EvalError('OpenRouter HTTP 429; raw error saved; no retry')

        with patch('almost_twin.router.post', side_effect=rate_limited):
            run(self.root, self.run_args(limit_cells=1, limit_per_cell=1))
        self.assertEqual(len(sent), 1)
        summary = json.loads(read(self.study / 'summary.json'))
        self.assertEqual(summary['provider_usage']['rate_limit_failures'], 1)
        self.assertIn('HTTP 429 failed scenarios: 1', read(self.study / 'summary.md'))

    def test_truncation_records_token_and_word_diagnostics_before_size_checks(self):
        self.spec['prisoner_efforts'] = ['low']
        self.spec['count_per_cell'] = 1
        self.config.write_text(yaml.safe_dump(self.spec, sort_keys=False))
        prepare(self.root, self.prep_args())
        sent = []

        def truncated(payload, key, folder, allow_nonaction=False, timeout_seconds=600):
            sent.append(payload)
            text = 'word ' * 5341
            response = {'model': payload['model'],
                        'usage': {'completion_tokens': 16000, 'cost': '.02',
                                  'completion_tokens_details': {'reasoning_tokens': 9580}},
                        'choices': [{'finish_reason': 'length', 'message': {'content': text}}]}
            (folder / 'request.json').write_bytes(encoded(payload))
            (folder / 'response.raw').write_bytes(encoded(response))
            (folder / 'output.txt').write_text(text)
            raise GenerationError('output_token_limit', 'Provider exhausted output budget; no retry')

        with patch('almost_twin.router.post', side_effect=truncated):
            run(self.root, self.run_args())
            run(self.root, self.run_args())
        self.assertEqual(len(sent), 1)
        failure = json.loads(read(self.study / 'summary.json'))['failed_attempts'][0]
        self.assertEqual(failure['failure_category'], 'output_token_limit')
        self.assertEqual(failure['completion_tokens'], 16000)
        self.assertEqual(failure['output_token_limit'], 16000)
        self.assertEqual(failure['reasoning_tokens'], 9580)
        self.assertEqual(failure['essay_words'], 5341)
        summary_text = read(self.study / 'summary.md')
        self.assertIn('16000 / 16000', summary_text)
        self.assertIn('9580 | 5341', summary_text)
        logs = list((self.root / 'data/exploratory').glob('researcher_essays.jsonl'))
        records = [json.loads(line) for line in read(logs[0]).splitlines()]
        self.assertEqual(records[-1]['failure_category'], 'output_token_limit')
        self.assertEqual(records[-1]['essay_words'], 5341)

    def test_study_code_changes_block_generation_but_not_offline_reporting(self):
        prepare(self.root, self.prep_args())
        with patch('almost_twin.study._study_code_sha256', return_value='different'):
            report(self.root, self.study)
            with self.assertRaisesRegex(EvalError, 'execution code changed'):
                run(self.root, self.run_args())
        self.assertEqual(self.calls, [])

    def test_one_cooperation_one_defection_is_half_without_role_randomization(self):
        # Both prisoner prompts stay in their fixed A/B positions; a mixed
        # response counts as 0.5 cooperation at the paired-scenario level.
        evidence = cases(self.root)[0]['evidence_b']
        real_post = self.fake_post

        def mixed_post(payload, key, folder, allow_nonaction=False, timeout_seconds=600):
            if allow_nonaction and evidence in payload['messages'][0]['content']:
                # Replace the default mock's A/B-independent pass response.
                content = submit_command(evidence)
                self.calls.append(payload)
                response = {'id': f'mock-{len(self.calls)}', 'model': payload['model'],
                    'provider': 'OpenAI', 'system_fingerprint': 'same-mock-weights',
                    'choices': [{'finish_reason': 'stop', 'message': {'content': content}}]}
                folder.mkdir(parents=True, exist_ok=True)
                (folder / 'request.json').write_bytes(encoded(payload))
                (folder / 'response.raw').write_bytes(encoded(response))
                (folder / 'output.txt').write_text(content)
                return response, content
            return real_post(payload, key, folder, allow_nonaction)

        prepare(self.root, self.prep_args())
        with patch('almost_twin.router.post', side_effect=mixed_post):
            run(self.root, self.run_args())
        with (self.study / 'summary.csv').open() as stream:
            cells = list(csv.DictReader(stream))
        self.assertEqual([c['cooperation_rate'] for c in cells], ['0.5', '0.5'])
        self.assertEqual([c['outcome_CD'] for c in cells], ['2', '2'])
        self.assertEqual([c['outcome_DC'] for c in cells], ['0', '0'])

    def test_incompatible_effort_is_reported_before_any_output(self):
        spec, _ = load_spec(self.config)
        spec['models'][0]['prisoner_efforts'] = ['none']
        spec['output_tokens']['prisoner']['none'] = 6000
        result, _, _ = check(self.root, spec)
        self.assertEqual(len(result['failures']), 1)
        self.assertEqual(result['projected_researcher_prisoner_calls'], 0)
        self.assertEqual(len(self.calls), 0)
        self.spec['prisoner_efforts'] = ['none']
        self.spec['output_tokens'] = {'prisoner': {'none': 6000}}
        self.config.write_text(yaml.safe_dump(self.spec, sort_keys=False))
        with self.assertRaisesRegex(EvalError, 'preflight failed'):
            prepare(self.root, self.prep_args())
        self.assertFalse(self.study.exists())

    def test_cli_has_study_commands(self):
        self.assertEqual(parser().parse_args(['study', 'check', '--config', 'x']).study_command, 'check')
        self.assertEqual(parser().parse_args(['study', 'prepare', '--config', 'x', '--out', 'y']).study_command, 'prepare')
        self.assertEqual(parser().parse_args(['study', 'run', '--study', 'y']).study_command, 'run')
        self.assertEqual(parser().parse_args(['study', 'report', '--study', 'y']).study_command, 'report')

    def test_cross_provider_cdt_smoke_config_has_exactly_two_low_effort_cells(self):
        spec, _ = load_spec(ROOT / 'configs/study.cdt-haiku-gemini-smoke.yaml')
        self.assertTrue(spec['exploratory'])
        self.assertEqual(spec['assignments'], ['cdt_wikipedia'])
        self.assertEqual(spec['scenario'], 't4_distinct_leads_001')
        self.assertEqual(spec['count_per_cell'], 2)
        self.assertEqual(spec['researcher_efforts'], ['low'])
        self.assertEqual(spec['prisoner_efforts'], ['low'])
        self.assertEqual([model['id'] for model in spec['models']], [
            'anthropic/claude-haiku-5.5', 'google/gemini-3.8-flash'])
        self.assertTrue(all(model.get('provider_tag') is None for model in spec['models']))
        self.assertTrue(spec['judge']['enabled'])
        self.assertEqual(spec['judge']['model'], JUDGE)
        self.assertEqual(spec['judge']['effort'], 'low')


if __name__ == '__main__':
    unittest.main()
