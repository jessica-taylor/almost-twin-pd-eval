"""All generations are mocked HTTP. No credentials/network are required."""
import copy
import io
import json
import os
import shutil
import tempfile
import unittest
import urllib.error
from contextlib import redirect_stdout
from decimal import Decimal
from pathlib import Path
from unittest.mock import patch
from urllib.parse import parse_qs, urlparse

import yaml

from almost_twin.approvals import approve, approve_source, has_approval, source_scope
from almost_twin.cli import main, parser
from almost_twin.common import EvalError, encoded, load_yaml, read, sha, utc, write_json
from almost_twin.pilot import prepare, resume
from almost_twin.preflight import choose_endpoint, effort_evidence
from almost_twin.router import validate_settings
from almost_twin.sources import fetch_one

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / 'tests/fixtures/openrouter/gpt5_nano.json'
MODEL = 'openai/gpt-5-nano'
SECRET = 'test-key-must-never-be-written'
ESSAY = 'SYNTHETIC MOCK MODEL OUTPUT.\r\nA mathematical essay fixture, frozen verbatim.\nE[V | a] is evaluated under the assigned theory.\n'


def capabilities():
    cap = json.loads(read(FIXTURE))
    cap['retrieved_at_utc'] = utc()
    return cap


def settings():
    return {'model': MODEL, 'provider_tag': 'openai', 'researcher': {'effort': 'low', 'max_tokens': 12000},
            'prisoner': {'effort': 'low', 'max_tokens': 3000}, 'temperature': None, 'seed': None}


def endpoint(cap, tag='openai'):
    return next(e for e in cap['endpoints'] if e['tag'] == tag)


class PreflightTests(unittest.TestCase):
    def test_nano_optional_web_search_pricing_and_model_effort_fallback(self):
        cap = capabilities()
        messages = [{'role': 'user', 'content': 'A text-only request.'}]
        payload, estimate = validate_settings(settings(), cap, 'researcher', messages)
        expected = Decimal('0.00000005') * (len(encoded(messages)) + 512) + Decimal('0.0000004') * 12000
        self.assertEqual(Decimal(estimate['estimated_max_usd']), expected)
        self.assertEqual(payload['reasoning'], {'effort': 'low'})
        self.assertEqual(payload['plugins'], [])
        self.assertEqual(payload['provider']['ignore'], ['openai/flex'])
        self.assertNotIn('tools', payload)
        self.assertNotIn('reasoning_effort', payload)
        self.assertEqual(estimate['reasoning_evidence']['status'], 'verified_by_model_metadata')
        self.assertIn('web_search', estimate['pricing_assumptions']['ignored_fields'])
        self.assertEqual(estimate['pricing_assumptions']['effective_input_usd_per_token'], '5E-8')

    def test_endpoint_effort_list_is_authoritative_and_rejections_are_explicit(self):
        cap = capabilities()
        endpoint(cap)['reasoning'] = {'supported_efforts': ['low']}
        _, estimate = validate_settings(settings(), cap, 'prisoner', [{'role': 'user', 'content': 'x'}])
        self.assertEqual(estimate['reasoning_evidence']['status'], 'verified_by_endpoint_metadata')
        s = settings()
        s['prisoner']['effort'] = 'high'
        s['reasoning_override'] = {'efforts': ['high'], 'reason': 'test override must not bypass metadata'}
        with self.assertRaisesRegex(EvalError, 'Unsupported reasoning effort.*high'):
            validate_settings(s, cap, 'prisoner', [{'role': 'user', 'content': 'x'}])

    def test_null_all_gateway_efforts_differs_from_omission_and_mandatory_none(self):
        cap = capabilities()
        endpoint(cap)['reasoning'] = {'supported_efforts': None}
        cap['model']['reasoning'] = {}
        _, estimate = validate_settings(settings(), cap, 'researcher', [{'role': 'user', 'content': 'x'}])
        self.assertEqual(estimate['reasoning_evidence']['status'], 'verified_by_endpoint_metadata')
        endpoint(cap)['reasoning'] = {}
        evidence = effort_evidence(settings(), cap, endpoint(cap), 'researcher')
        self.assertEqual(evidence['status'], 'unverified')
        with self.assertRaisesRegex(EvalError, 'allow-unverified-effort'):
            validate_settings(settings(), cap, 'researcher', [{'role': 'user', 'content': 'x'}])
        cap['model']['reasoning'] = {'supported_efforts': None, 'mandatory': True}
        s = settings()
        s['researcher']['effort'] = 'none'
        with self.assertRaisesRegex(EvalError, 'mandatory'):
            validate_settings(s, cap, 'researcher', [{'role': 'user', 'content': 'x'}])

    def test_manual_override_has_no_timestamp_requirement_or_false_verification(self):
        cap = capabilities()
        cap['model']['reasoning'] = {}
        s = settings()
        s['reasoning_override'] = {'efforts': ['low'], 'reason': 'Documented user assumption for a small exploratory test.'}
        _, estimate = validate_settings(s, cap, 'researcher', [{'role': 'user', 'content': 'x'}])
        self.assertEqual(estimate['reasoning_evidence']['status'], 'documented_manual_override')
        s.pop('reasoning_override')
        s['provider_effort_review'] = {'efforts': ['low'], 'note': 'Legacy review', 'reviewed_at_utc': '2001-01-01T00:00:00Z'}
        _, estimate = validate_settings(s, cap, 'researcher', [{'role': 'user', 'content': 'x'}])
        self.assertEqual(estimate['reasoning_evidence']['status'], 'documented_manual_override')
        cap['model']['reasoning'] = {'supported_efforts': ['high']}
        with self.assertRaisesRegex(EvalError, 'Unsupported reasoning effort'):
            validate_settings(s, cap, 'researcher', [{'role': 'user', 'content': 'x'}])

    def test_cache_and_internal_reasoning_charges_are_conservatively_bounded(self):
        cap = capabilities()
        endpoint(cap)['pricing'].update(input_cache_write='0.0000001', input_cache_read='0.00000007', internal_reasoning='0.0000003')
        _, estimate = validate_settings(settings(), cap, 'researcher', [{'role': 'user', 'content': 'x'}])
        self.assertEqual(Decimal(estimate['estimated_max_usd']),
                         Decimal('0.00000017') * estimate['input_tokens_upper_estimate'] + Decimal('0.0000007') * 12000)
        endpoint(cap)['pricing']['cache_storage'] = '0.001'
        with self.assertRaisesRegex(EvalError, 'cache_storage.*cannot be bounded'):
            validate_settings(settings(), cap, 'researcher', [{'role': 'user', 'content': 'x'}])

    def test_sol_judge_prompt_length_tiers_bound_and_select_direct_openai(self):
        cap = capabilities()
        cap['model']['id'] = 'openai/gpt-6.1-sol'
        openai = endpoint(cap)
        openai['supported_parameters'].append('response_format')
        openai['pricing'] = {
            'prompt': '0.000002', 'completion': '0.000010',
            'input_cache_read': '0.0000001', 'input_cache_write': '0.0000003',
            'overrides': [{'min_prompt_tokens': 272000,
                           'prompt': '0.000004', 'completion': '0.000015',
                           'input_cache_read': '0.0000002', 'input_cache_write': '0.000005'}],
        }
        s = {'model': cap['model']['id'], 'provider_tag': None,
             'judge': {'effort': 'low', 'max_tokens': 1200},
             'temperature': None, 'seed': None}
        messages = [{'role': 'user', 'content': 'Judge this ambiguous fictional action.'}]
        chosen, report = choose_endpoint(s, cap, [('judge', messages)], validate_settings)
        self.assertEqual(chosen['provider_tag'], 'openai')
        self.assertEqual(report['selected_endpoint'], 'openai')
        payload, estimate = validate_settings(chosen, cap, 'judge', messages)
        self.assertEqual(payload['response_format'], {'type': 'json_object'})
        cost = (Decimal('0.000009') * estimate['input_tokens_upper_estimate']
                + Decimal('0.000015') * 1200)
        self.assertEqual(Decimal(estimate['estimated_max_usd']), cost)
        self.assertEqual(estimate['pricing_assumptions']['effective_input_usd_per_token'], '0.000009')
        self.assertEqual(estimate['pricing_assumptions']['pricing_tiers'][0]['min_prompt_tokens'], 272000)
        self.assertIn('highest advertised rate', estimate['pricing_assumptions']['tier_policy'])

    def test_anthropic_one_hour_cache_write_tier_is_bounded_and_auditable(self):
        cap = capabilities()
        cap['model']['id'] = 'anthropic/claude-haiku-5.5'
        direct = endpoint(cap)
        direct['tag'] = 'anthropic'
        direct['pricing'] = {
            'prompt': '0.0000001', 'completion': '0.0000005',
            'input_cache_read': '0.00000001',
            'input_cache_write': '0.000000125',
            'input_cache_write_1h': '0.0000002',
            'overrides': [{'min_prompt_tokens': 100000,
                           'prompt': '0.0000005', 'completion': '0.0000025',
                           'input_cache_read': '0.00000005',
                           'input_cache_write': '0.000000625',
                           'input_cache_write_1h': '0.000001'}],
        }
        s = settings()
        s['model'], s['provider_tag'] = 'anthropic/claude-haiku-5.5', None
        messages = [{'role': 'user', 'content': 'CDT source text and instructions.'}]
        chosen, selection = choose_endpoint(s, cap, [('researcher', messages)], validate_settings)
        self.assertEqual(chosen['provider_tag'], 'anthropic')
        self.assertEqual(selection['selected_endpoint'], 'anthropic')
        _, estimate = validate_settings(chosen, cap, 'researcher', messages)
        # Uses maximum across base and 100k+ tier; 1-hour and 5-minute writes
        # are alternatives, with the larger rate reserved for every input token.
        expected = (Decimal('0.0000015') * estimate['input_tokens_upper_estimate']
                    + Decimal('0.0000025') * 12000)
        self.assertEqual(Decimal(estimate['estimated_max_usd']), expected)
        assumptions = estimate['pricing_assumptions']
        self.assertEqual(assumptions['effective_input_usd_per_token'], '0.0000015')
        self.assertEqual(assumptions['pricing_tiers'][0]['advertised_rates']['input_cache_write_1h'],
                         '0.000001')
        self.assertIn('1-hour', assumptions['cache_policy'])

        bad = copy.deepcopy(cap)
        endpoint(bad, 'anthropic')['pricing']['overrides'][0]['input_cache_write_1h'] = 'NaN'
        with self.assertRaisesRegex(EvalError, 'input_cache_write_1h'):
            validate_settings(chosen, bad, 'researcher', messages)
        bad = copy.deepcopy(cap)
        endpoint(bad, 'anthropic')['pricing']['overrides'][0]['cache_storage'] = '0.00001'
        with self.assertRaisesRegex(EvalError, 'unsupported keys'):
            validate_settings(chosen, bad, 'researcher', messages)

    def test_prompt_length_tiers_fail_closed_on_unknown_rules(self):
        cap = capabilities()
        for bad in (
            [{'min_prompt_tokens': 272000, 'cost': 9}],
            [{'min_prompt_tokens': True, 'prompt': '0.000004'}],
            [{'min_prompt_tokens': 272000, 'prompt': '-0.000004'}],
            [{'min_prompt_tokens': 272000, 'prompt': 'not-a-rate'}],
            [{'max_prompt_tokens': 272000, 'prompt': '0.000004'}],
            {'min_prompt_tokens': 272000, 'prompt': '0.000004'},
        ):
            changed = copy.deepcopy(cap)
            endpoint(changed)['pricing']['overrides'] = bad
            with self.subTest(bad=bad), self.assertRaises(EvalError):
                validate_settings(settings(), changed, 'researcher', [{'role': 'user', 'content': 'x'}])

    def test_anthropic_author_endpoint_preferred_over_other_providers(self):
        cap = capabilities()
        cap['model']['id'] = 'anthropic/claude-test'
        endpoint(cap)['tag'] = 'anthropic'
        endpoint(cap, 'openai/flex')['tag'] = 'anthropic/fast'
        s = settings()
        s['model'], s['provider_tag'] = 'anthropic/claude-test', None
        chosen, _ = choose_endpoint(s, cap, [('researcher', [{'role': 'user', 'content': 'x'}])], validate_settings)
        self.assertEqual(chosen['provider_tag'], 'anthropic')

    def test_unused_modalities_allowed_but_automatic_search_or_unknown_costs_fail(self):
        cap = capabilities()
        endpoint(cap)['pricing'].update(image='0.003', audio='0.02')
        _, estimate = validate_settings(settings(), cap, 'researcher', [{'role': 'user', 'content': 'x'}])
        self.assertIn('image', estimate['pricing_assumptions']['ignored_fields'])
        for mutation in (
            lambda c: endpoint(c).update(automatic_web_search=True),
            lambda c: endpoint(c).update(max_tokens_includes_reasoning=False),
            lambda c: endpoint(c)['pricing'].update(overrides=[{'price': 10}]),
            lambda c: endpoint(c)['pricing'].update(internal_reasoning='NaN'),
            lambda c: endpoint(c)['pricing'].update(input_cache_write=None),
            lambda c: endpoint(c).update(default_parameters={'web_search_options': {}}),
        ):
            changed = copy.deepcopy(cap)
            mutation(changed)
            with self.assertRaises(EvalError):
                validate_settings(settings(), changed, 'researcher', [{'role': 'user', 'content': 'x'}])

    def test_deterministic_direct_selection_override_and_no_silent_effort_change(self):
        cap = capabilities()
        s = settings()
        s['provider_tag'] = None
        selected, report = choose_endpoint(s, cap, [('researcher', [{'role': 'user', 'content': 'x'}]), ('prisoner', [{'role': 'user', 'content': 'x'}])], validate_settings)
        self.assertEqual(selected['provider_tag'], 'openai')  # flex is listed first and cheaper, but direct base wins.
        self.assertEqual(selected['researcher']['effort'], 'low')
        endpoint(cap)['status'] = 1
        with self.assertRaisesRegex(EvalError, 'No suitable endpoint'):
            choose_endpoint(settings(), cap, [('researcher', [{'role': 'user', 'content': 'x'}])], validate_settings)
        selected, _ = choose_endpoint(s, cap, [('researcher', [{'role': 'user', 'content': 'x'}])], validate_settings)
        self.assertEqual(selected['provider_tag'], 'openai/flex')  # New experiment selection only, before pinning.

    def test_max_completion_tokens_only_endpoint_is_supported(self):
        cap = capabilities()
        s = settings()
        s['provider_tag'] = 'azure'
        payload, _ = validate_settings(s, cap, 'prisoner', [{'role': 'user', 'content': 'x'}])
        self.assertEqual(payload['max_completion_tokens'], 3000)
        self.assertNotIn('max_tokens', payload)


class PilotTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('configs', 'prompts', 'sources'):
            shutil.copytree(ROOT / name, self.root / name)
        manifest_path = self.root / 'sources/manifest.yaml'
        manifest = load_yaml(manifest_path)
        manifest['sources']['cdt_wikipedia'].update(revision_id=123456, revision_review='approved')
        manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False))
        def download(url, dest):
            action = parse_qs(urlparse(url).query)['action'][0]
            data = (ROOT / 'tests/fixtures/mediawiki' / ('revision.json' if action == 'query' else 'parse.json')).read_bytes()
            dest.write_bytes(data)
            return {'url': url, 'raw_file': dest.name, 'raw_sha256': sha(data), 'retrieved_at_utc': utc()}
        with patch('almost_twin.sources.download', side_effect=download):
            fetch_one(self.root, 'cdt_wikipedia', manifest['sources']['cdt_wikipedia'], network=True)
        self.folder = self.root / 'data/pilots/nano'
        self.cap = capabilities()
        self.network = patch('socket.socket', side_effect=AssertionError('real network forbidden'))
        self.network.start()
        self.addCleanup(self.network.stop)
        self.calls = []
        self.outputs = [ESSAY, 'pass', 'pass']
        self.fail_call = None
        self.metadata = patch('almost_twin.pilot.snapshot', side_effect=lambda model: copy.deepcopy(self.cap))
        self.metadata_mock = self.metadata.start()
        self.addCleanup(self.metadata.stop)
        self.post = patch('urllib.request.urlopen', side_effect=self.http)
        self.http_mock = self.post.start()
        self.addCleanup(self.post.stop)
        self.env = patch.dict(os.environ, {'OPENROUTER_API_KEY': SECRET}, clear=True)
        self.env.start()
        self.addCleanup(self.env.stop)

    def http(self, request, **kwargs):
        self.calls.append(request)
        if self.fail_call == len(self.calls):
            raise urllib.error.URLError('mock transport failure')
        output = self.outputs[len(self.calls) - 1]
        raw = encoded({'model': MODEL, 'provider': 'OpenAI', 'system_fingerprint': 'mock-fixed-version',
                       'id': 'mock-' + str(len(self.calls)), 'usage': {'prompt_tokens': 100, 'completion_tokens': 20},
                       'choices': [{'finish_reason': 'stop', 'message': {'content': output}}]})
        class Response:
            status, headers = 200, {'x-request-id': 'mock'}
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def read(self): return raw
        return Response()

    def prep(self, extra=()):
        args = parser().parse_args(['pilot', 'prepare', '--assignment', 'cdt_wikipedia', '--model', MODEL,
                                   '--researcher-effort', 'low', '--prisoner-effort', 'low', '--out', str(self.folder), *extra])
        return prepare(self.root, args)

    def step(self, name, live=False, approve_prompt=False):
        flags = ['--execute', '--confirm-billable'] if live else []
        if approve_prompt:
            flags += ['--prompts-approved']
        args = parser().parse_args(['pilot', name, '--pilot', str(self.folder), *flags])
        return resume(self.root, args)

    def researcher(self):
        self.prep()
        return self.step('researcher', live=True, approve_prompt=True)

    def test_preparation_is_unbilled_and_prices_readable_exact_requests(self):
        folder = self.prep()
        self.assertEqual(self.metadata_mock.call_count, 1)
        self.assertFalse(self.calls)
        self.assertFalse((self.root / 'data/budget.jsonl').exists())
        config = json.loads(read(folder / 'pilot.json'))
        self.assertEqual(config['settings']['provider_tag'], 'openai')
        self.assertTrue(config['exploratory'])
        self.assertIn('Researcher maximum estimated cost', read(folder / 'plan.md'))
        payload = json.loads(read(folder / 'researcher/request_0.json'))
        messages = json.loads(read(folder / 'researcher/messages_0.json'))
        self.assertEqual(payload['messages'], messages)
        self.assertIn('Wikipedia contributors', messages[0]['content'])
        self.assertNotIn('t4_distinct_leads_001', messages[0]['content'])
        self.assertFalse(json.loads(read(folder / 'plan.json'))['source_approval_required'])

    def test_complete_two_stage_http_mock_resume_and_no_key_in_artifacts(self):
        essay_dir = self.researcher()
        self.assertEqual((essay_dir / 'essay.md').read_bytes(), ESSAY.encode())
        self.assertEqual(self.step('researcher', live=True), essay_dir)
        self.assertEqual(len(self.calls), 1)  # A completed researcher is never re-run.
        self.step('prisoners')  # Export both actual prompts for inspection, no model calls.
        self.assertEqual(len(self.calls), 1)
        pair = self.step('prisoners', live=True, approve_prompt=True)
        self.assertEqual(self.step('prisoners', live=True), pair)
        self.assertEqual(len(self.calls), 3)
        outcome = json.loads(read(pair / 'outcome.json'))
        self.assertEqual(outcome['years'], [2, 2])
        requests = [json.loads(call.data) for call in self.calls]
        for request in requests:
            self.assertEqual(request['model'], MODEL)
            self.assertEqual(request['provider']['only'], ['openai'])
            self.assertEqual(request['reasoning'], {'effort': 'low'})
        for request in requests[1:]:
            self.assertEqual(len(request['messages']), 1)
            self.assertIn(ESSAY, request['messages'][0]['content'])
            self.assertNotIn('Wikipedia contributors', request['messages'][0]['content'])
        for i in (0, 1):
            self.assertEqual((pair / f'call_{i}/request.json').read_bytes(), self.calls[i+1].data)
        for path in (self.root / 'data').rglob('*'):
            if path.is_file():
                self.assertNotIn(SECRET.encode(), path.read_bytes(), str(path))
        self.assertFalse((self.root / 'data/researcher_essays.jsonl').exists())
        self.assertTrue((self.root / 'data/exploratory/researcher_essays.jsonl').exists())
        reservations = [json.loads(line) for line in read(self.root / 'data/budget.jsonl').splitlines()]
        self.assertEqual(sum(r['calls'] for r in reservations), 3)

    def test_optional_legacy_source_acknowledgement_remains_scoped_to_original_source(self):
        identity = approve_source(self.root, 'cdt_wikipedia', True)
        self.assertTrue(has_approval(self.root, 'source_terms', source_scope(identity)))
        self.assertTrue(has_approval(self.root, 'source_terms', source_scope({**identity, 'source_provenance_sha256': 'new retrieval metadata'})))
        for field, value in (('source_revision', 999), ('source_sha256', 'changed source')):
            self.assertFalse(has_approval(self.root, 'source_terms', source_scope({**identity, field: value})))

    def test_researcher_requires_no_source_approval_but_keeps_prompt_and_billing_checks(self):
        self.prep()
        self.step('researcher')
        self.assertFalse(self.calls)
        with self.assertRaisesRegex(EvalError, 'not approved'):
            self.step('researcher', live=True)
        self.assertFalse(self.calls)
        result = self.step('researcher', live=True, approve_prompt=True)
        self.assertEqual(len(self.calls), 1)
        plan = json.loads(read(result / 'plan.json'))
        self.assertFalse(plan['source_approval_required'])
        self.assertNotIn('source_terms', plan['authorization'])
        records = [json.loads(line) for line in read(self.root / 'data/approvals.jsonl').splitlines()]
        self.assertTrue(all(r['kind'] == 'prompts' for r in records))

    def test_original_cli_command_resumes_a_pilot_previously_blocked_by_source_approval(self):
        self.prep()
        # Existing pilot plans/states may predate removal of the source-rights gate.
        plan_path = self.folder / 'plan.json'
        plan = json.loads(read(plan_path))
        plan.pop('source_approval_required')
        plan['source_terms_approved'] = False
        write_json(plan_path, plan)
        stage_plan = json.loads(read(self.folder / 'researcher/plan.json'))
        write_json(self.folder / 'state.json', {
            'researcher_run': str(self.root / 'data/exploratory/runs/previous-preflight-only-failure'),
            'researcher_status': 'preflight_failed',
            'researcher_request_hashes': stage_plan['request_hashes']})
        with redirect_stdout(io.StringIO()):
            result = main(['--root', str(self.root), 'pilot', 'researcher', '--pilot', str(self.folder),
                           '--execute', '--confirm-billable', '--prompts-approved'])
        self.assertEqual(result, 0)
        self.assertEqual(len(self.calls), 1)
        records = [json.loads(line) for line in read(self.root / 'data/approvals.jsonl').splitlines()]
        self.assertTrue(all(r['kind'] == 'prompts' for r in records))
        self.assertIn('No separate source approval is required', read(self.folder / 'plan.md'))

    def test_prompt_approval_hash_changes_invalidate_it(self):
        scope = {'request_hashes': ['original']}
        approve(self.root, 'prompts', scope, True)
        self.assertTrue(has_approval(self.root, 'prompts', scope))
        self.assertFalse(has_approval(self.root, 'prompts', {'request_hashes': ['changed effort, source or message']}))
        self.prep()
        path = self.folder / 'researcher/messages_0.md'
        path.write_text(read(path) + 'tampered')
        with self.assertRaisesRegex(EvalError, 'approval is invalid'):
            self.step('researcher', live=True, approve_prompt=True)
        self.assertFalse(self.calls)

    def test_template_and_settings_changes_are_rejected_before_calls(self):
        self.prep()
        path = self.root / 'prompts/researcher/base.md'
        path.write_text(read(path) + 'Changed instruction')
        with self.assertRaisesRegex(EvalError, 'content changed'):
            self.step('researcher', live=True, approve_prompt=True)
        self.assertFalse(self.calls)

    def test_edited_decoding_settings_invalidate_preparation(self):
        self.prep()
        path = self.folder / 'settings.json'
        changed = json.loads(read(path))
        changed['researcher']['effort'] = 'high'
        write_json(path, changed)
        with self.assertRaisesRegex(EvalError, 'artifact.*changed'):
            self.step('researcher', live=True, approve_prompt=True)
        self.assertFalse(self.calls)

    def test_pilot_requires_both_billing_flags(self):
        self.prep()
        for flag in ('--execute', '--confirm-billable'):
            args = parser().parse_args(['pilot', 'researcher', '--pilot', str(self.folder), flag, '--prompts-approved'])
            with self.assertRaisesRegex(EvalError, 'BOTH'):
                resume(self.root, args)
        self.assertFalse(self.calls)
        self.assertFalse((self.root / 'data/budget.jsonl').exists())

    def test_tampered_essay_even_with_edited_metadata_and_raw_response_is_rejected(self):
        essay_dir = self.researcher()
        changed = ESSAY + 'tampered'
        (essay_dir / 'essay.md').write_bytes(changed.encode())
        info = json.loads(read(essay_dir / 'essay.json'))
        info['essay_sha256'] = sha(changed)
        write_json(essay_dir / 'essay.json', info)
        raw = json.loads(read(essay_dir / 'call_0/response.raw'))
        raw['choices'][0]['message']['content'] = changed
        write_json(essay_dir / 'call_0/response.raw', raw)
        with self.assertRaisesRegex(EvalError, 'essay/provenance changed'):
            self.step('prisoners')
        self.assertEqual(len(self.calls), 1)

    def test_pinned_endpoint_disappearing_does_not_switch_to_azure(self):
        self.researcher()
        self.step('prisoners')
        endpoint(self.cap)['status'] = 1
        with self.assertRaisesRegex(EvalError, 'openai.*unavailable'):
            self.step('prisoners', live=True, approve_prompt=True)
        self.assertEqual(len(self.calls), 1)

    def test_new_endpoint_variant_requires_repreparation_instead_of_broadening_route(self):
        self.prep()
        new = copy.deepcopy(endpoint(self.cap))
        new['tag'] = 'openai/another-region'
        self.cap['endpoints'].append(new)
        with self.assertRaisesRegex(EvalError, 'Prepared request content changed'):
            self.step('researcher', live=True, approve_prompt=True)
        self.assertFalse(self.calls)

    def test_changed_canonical_model_is_rejected(self):
        self.prep()
        self.cap['model']['canonical_slug'] = 'openai/different-version'
        with self.assertRaisesRegex(EvalError, 'different canonical version'):
            self.step('researcher', live=True, approve_prompt=True)
        self.assertFalse(self.calls)

    def test_partial_pair_failure_preserves_commitment_budget_and_no_retry(self):
        self.researcher()
        self.step('prisoners')
        self.fail_call = 3
        with self.assertRaisesRegex(EvalError, 'billing outcome unknown'):
            self.step('prisoners', live=True, approve_prompt=True)
        state = json.loads(read(self.folder / 'state.json'))
        pair = Path(state['prisoner_run'])
        self.assertTrue((pair / 'failure.json').exists())
        self.assertEqual(state['prisoner_status'], 'failed')
        self.assertIn('no completed outcome is implied', read(self.folder / 'plan.md'))
        self.assertFalse((pair / 'outcome.json').exists())
        self.assertEqual(len(read(self.root / 'data/exploratory/commitments.jsonl').splitlines()), 1)
        records = [json.loads(line) for line in read(self.root / 'data/exploratory/prisoner_decisions.jsonl').splitlines()]
        self.assertEqual([r['status'] for r in records], ['started', 'success', 'started', 'failed'])
        with self.assertRaisesRegex(EvalError, 'already attempted'):
            self.step('prisoners', live=True, approve_prompt=True)
        self.assertEqual(len(self.calls), 3)
        self.assertEqual(sum(json.loads(line)['calls'] for line in read(self.root / 'data/budget.jsonl').splitlines()), 3)

    def test_resume_recovery_after_essay_saved_before_state_finalized(self):
        directory = self.researcher()
        state = json.loads(read(self.folder / 'state.json'))
        state['researcher_status'] = 'attempted'
        state.pop('essay_sha256')
        write_json(self.folder / 'state.json', state)
        self.assertEqual(self.step('researcher', live=True), directory)
        self.assertEqual(len(self.calls), 1)

    def test_small_budget_rejected_in_preparation_without_reservation(self):
        with self.assertRaisesRegex(EvalError, 'budget would be exceeded'):
            self.prep(['--max-usd', '0.000001'])
        self.assertFalse(self.calls)
        self.assertFalse((self.root / 'data/budget.jsonl').exists())

    def test_first_live_prisoner_invocation_only_prepares_inspectable_requests(self):
        self.researcher()
        with self.assertRaisesRegex(EvalError, 'Prisoner prompts are now prepared'):
            self.step('prisoners', live=True, approve_prompt=True)
        self.assertEqual(len(self.calls), 1)
        self.assertTrue((self.folder / 'prisoners/messages_1.md').exists())

    def test_cli_preparation_without_source_approval_or_key(self):
        with patch.dict(os.environ, {}, clear=True), redirect_stdout(io.StringIO()) as output:
            result = main(['--root', str(self.root), 'pilot', 'prepare', '--assignment', 'cdt_wikipedia', '--model', MODEL, '--out', str(self.folder)])
            self.assertEqual(result, 0)
        self.assertIn('no billable requests', output.getvalue())
        self.assertIn('plan.md', output.getvalue())
        self.assertFalse(self.calls)


if __name__ == '__main__':
    unittest.main()

