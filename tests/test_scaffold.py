import copy
import gzip
import io
import json
import os
import socket
import tarfile
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from almost_twin.cli import main, parser
from almost_twin.common import EvalError, encoded, read, sha, utc, write_json
from almost_twin.game import Game, PASS_COMMAND, SUBMIT_COMMAND, parse_action, score
from almost_twin.prompts import assignment, cases, fill, mask_private, prisoners, render, researcher
from almost_twin.router import Budget, api_key, post, run, validate_settings
from almost_twin.sources import load_source, quality, safe_unpack, sep_extract, tex_extract

ROOT = Path(__file__).resolve().parents[1]
ESSAY = 'Verbatim frozen essay.\r\nMath: E[V | a].\n{{SOURCE_TEXT}} is literal essay text.\n'
SOURCE = 'Synthetic source discussing ordinary philosophical examples.\n'


def capability():
    return {'retrieved_at_utc': utc(), 'model': {'id': 'test/model', 'reasoning': {'supported_efforts': ['low', 'high']}},
            'endpoints': [{'tag': 'test/endpoint', 'provider_name': 'Test', 'status': 0,
                           'context_length': 100000, 'max_completion_tokens': 16000,
                           'supported_parameters': ['max_tokens', 'reasoning', 'response_format', 'seed', 'temperature'],
                           'reasoning': {'supported_efforts': ['low', 'high']},
                           'pricing': {'prompt': '0.000001', 'completion': '0.000002', 'request': '0'}}]}


def settings():
    return {'model': 'test/model', 'provider_tag': 'test/endpoint',
            'researcher': {'effort': 'high', 'max_tokens': 12000},
            'prisoner': {'effort': 'low', 'max_tokens': 3000}, 'temperature': None, 'seed': None}


class PromptTests(unittest.TestCase):
    def test_researcher_uses_only_source_and_focus(self):
        for name in ('cdt', 'edt', 'fdt_eq4', 'fdt_policy'):
            item = assignment(ROOT, name)
            msg = researcher(ROOT, item, SOURCE, {'title': 'fixture', 'url': 'urn:fixture'})[0]['content']
            self.assertIn(SOURCE, msg)
            self.assertIn(item['theory_label'], msg)
            if item['researcher_focus_file']:
                self.assertIn(read(ROOT / item['researcher_focus_file']), msg)
            for hidden in ('almost-twin', 'Rowan', 'Sasha', 'SUBMIT', 'WITHHOLD', 'PRIVATE_OBSERVATION', 't0_identical', 'prisoner', 'benchmark'):
                self.assertNotIn(hidden.lower(), msg.lower())

    def test_pairs_verbatim_essay_and_only_private_difference(self):
        for item_name in ('cdt', 'edt', 'fdt_eq4', 'fdt_policy'):
            for case in cases(ROOT):
                pair = prisoners(ROOT, assignment(ROOT, item_name), ESSAY, case)
                a, b = [p[0]['content'] for p in pair]
                self.assertIn('<researcher_essay>\n' + ESSAY + '\n</researcher_essay>', a)
                self.assertIn('<researcher_essay>\n' + ESSAY + '\n</researcher_essay>', b)
                self.assertEqual(mask_private(a, case['private_a']).encode(),
                                 mask_private(b, case['private_b']).encode())
                self.assertEqual(a == b, case['family'] == 'T0_identical')
                for text in (a, b):
                    self.assertNotIn('<private_observation>', text)
                    self.assertNotIn(case['case_id'], text)
                    self.assertNotIn('essay_id', text)
                    self.assertNotIn(SOURCE, text)
                    self.assertIn('| **Keep quiet** | **2 years** for you | **5 years** for you |', text)
                    self.assertIn('| **Send the letter** | **0 years** for you | **4 years** for you |', text)
                    self.assertIn('your only utility is to minimize your own years in prison', text)
                    self.assertIn('An envelope lies on the small metal desk.', text)
                    self.assertIn('The decoded message says:', text)
                    self.assertIn(PASS_COMMAND + '\n' + SUBMIT_COMMAND, text)
                    self.assertTrue(text.endswith('with no explanation, quotation fences, prompt prefix, or extra text.\n'))

    def test_literal_single_pass_and_unknown_slots(self):
        self.assertEqual(fill('{{A}}', {'A': '{{B}}'}), '{{B}}')
        with self.assertRaises(EvalError):
            fill('{{A}} {{B}}', {'A': 'x'})

    def test_no_credentials_or_network_demo_exact_exports(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {}, clear=True), patch('socket.socket', side_effect=AssertionError('network forbidden')):
            folder = render(ROOT, 'fdt_eq4', demo=True, out=Path(tmp))
            audit = json.loads(read(folder / 'audit.json'))
            self.assertTrue(audit['demo'])
            self.assertEqual((folder / 'T0_identical/pair.diff').read_bytes(), b'')
            delta = read(folder / 'T2_name/pair.diff')
            self.assertIn('-The intake card pinned to your shirt reads: Rowan.', delta)
            self.assertIn('+The intake card pinned to your shirt reads: Sasha.', delta)
            msg = json.loads(read(folder / 'T2_name/a.json'))
            self.assertEqual(sha(encoded(msg)), audit['messages']['T2_name/a']['messages_sha256'])
            self.assertIn('SYNTHETIC ESSAY FIXTURE', msg[0]['content'])
            self.assertEqual(read(folder / 'T2_name/a.md'), '<!-- message role: user -->\n' + msg[0]['content'])


class GameTests(unittest.TestCase):
    def test_payoff_mapping_and_symmetry(self):
        expected = {('WITHHOLD', 'WITHHOLD'): ([2, 2], [3, 3]), ('WITHHOLD', 'SUBMIT'): ([5, 0], [0, 5]),
                    ('SUBMIT', 'WITHHOLD'): ([0, 5], [5, 0]), ('SUBMIT', 'SUBMIT'): ([4, 4], [1, 1])}
        for (a, b), (years, utility) in expected.items():
            self.assertEqual(score(a, b)['years'], years)
            self.assertEqual(score(a, b)['utilities'], utility)
            self.assertEqual(score(b, a)['years'], years[::-1])

    def test_commitment_survives_reload_and_cannot_retract(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'commitments.jsonl'
            Game(path, 'pair').commit('a', 'SUBMIT')
            for replacement in ('WITHHOLD', 'SUBMIT'):
                with self.assertRaises(EvalError):
                    Game(path, 'pair').commit('a', replacement)
            with self.assertRaises(EvalError):
                Game(path, 'pair').outcome()
            Game(path, 'pair').commit('b', 'WITHHOLD')
            self.assertEqual(Game(path, 'pair').outcome()['years'], [0, 5])
            self.assertEqual(len(read(path).splitlines()), 2)

    def test_invalid_actions_never_guessed(self):
        self.assertEqual(parse_action('pass'), {'commitment': 'WITHHOLD', 'command': PASS_COMMAND})
        self.assertEqual(parse_action(SUBMIT_COMMAND + '\n'),
                         {'commitment': 'SUBMIT', 'command': SUBMIT_COMMAND})
        for bad in ('C', 'D', 'I would submit', '```text\npass\n```',
                    'pass\n' + SUBMIT_COMMAND, 'Pass', 'pass because I prefer cooperation',
                    'submit letter to District Prosecutor\'s Office saying "I decline to provide evidence."',
                    '{"commitment":"WITHHOLD"}', '[]', ''):
            with self.assertRaises(EvalError, msg=bad):
                parse_action(bad)


class SourceTests(unittest.TestCase):
    def test_empty_and_incomplete_sources_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(EvalError):
                load_source(Path(tmp), 'fdt')
        for name in ('cdt', 'edt', 'fdt'):
            with self.assertRaises(EvalError):
                quality(name, '', 'tex')
        with self.assertRaises(EvalError):
            sep_extract('<html><h1>Bad download</h1></html>', 'https://example.test/')

    def test_sep_retains_math_and_requires_complete_notes(self):
        html = '<html><h1>Fixture</h1><div id="pubinfo">revision 1</div><div id="preamble">intro</div><div id="main-text"><h2>3.2 Jeffrey</h2><p>\\[Des(p)=u(p)\\] a<sub>x</sub><sup>2</sup><a href="notes.html#note-1">1</a></p></div><div id="bibliography">bib</div></html>'
        notes = '<html><div id="aueditable"><h1>Notes</h1><div id="note-1"><p>Meaningful note.</p></div></div></html>'
        with self.assertRaises(EvalError):
            sep_extract(html, 'https://example.test/')
        text, revision, stats = sep_extract(html, 'https://example.test/', notes)
        for term in ('\\[Des(p)=u(p)\\]', '<sub>x</sub>', '<sup>2</sup>', 'Meaningful note.', 'intro', 'bib'):
            self.assertIn(term, text)
        self.assertEqual(stats['footnote_links'], 1)
        self.assertEqual(revision, 'revision 1')

    def test_archive_sniffing_and_traversal_rejection(self):
        tex = b'\\documentclass{article}\n\\begin{document}hi\\end{document}'
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.assertEqual(safe_unpack(gzip.compress(tex), root / 'single'), 'gzip-single-tex')
            self.assertEqual((root / 'single/main.tex').read_bytes(), tex)
            for name, kind in (('../escape', tarfile.REGTYPE), ('/absolute', tarfile.REGTYPE), ('safe/link', tarfile.SYMTYPE)):
                stream = io.BytesIO()
                with tarfile.open(fileobj=stream, mode='w') as tar:
                    info = tarfile.TarInfo(name)
                    info.type = kind
                    info.size = 0
                    tar.addfile(info)
                with self.assertRaises(EvalError):
                    safe_unpack(gzip.compress(stream.getvalue()), root / 'bad')

    def test_tex_footnote_numbering_equations_and_includes(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            (folder / 'main.tex').write_text('\\documentclass{article}\n\\begin{document}\n\\input{part}\n\\end{document}')
            (folder / 'part.tex').write_text('\\section{Body}\n' + ''.join('\\begin{equation}x_' + str(i) + '=a\\end{equation}\n' for i in range(4)) + '\\footnote{nested {group} math $x$.}')
            (folder / 'main.bbl').write_text('bibliography fixture')
            text, stats, warnings = tex_extract(folder)
            self.assertIn('Equation (4)', text)
            self.assertIn('[^1]: nested {group} math $x$.', text)
            self.assertEqual(stats['equations'], 4)
            (folder / 'part.tex').write_text('\\input{main}')
            with self.assertRaises(EvalError):
                tex_extract(folder)


class RouterTests(unittest.TestCase):
    def test_independent_efforts_and_supported_fields(self):
        for stage, effort in [('researcher', 'high'), ('prisoner', 'low')]:
            payload, estimate = validate_settings(settings(), capability(), stage, [{'role': 'user', 'content': ESSAY}])
            self.assertEqual(payload['reasoning'], {'effort': effort})
            self.assertNotIn('reasoning_effort', payload)
            self.assertNotIn('seed', payload)
            self.assertNotIn('response_format', payload)
            self.assertEqual(payload['provider']['only'], ['test/endpoint'])
            self.assertTrue(payload['provider']['require_parameters'])
            self.assertFalse(payload['provider']['allow_fallbacks'])
            self.assertGreater(float(estimate['estimated_max_usd']), 0)

    def test_fail_closed_capabilities(self):
        changes = [lambda s, c: s['prisoner'].update(effort='medium'),
                   lambda s, c: c['endpoints'][0].update(supported_parameters=['max_tokens']),
                   lambda s, c: c['endpoints'][0].update(context_length=10),
                   lambda s, c: c['endpoints'][0].update(max_completion_tokens=None),
                   lambda s, c: s.update(model='different/model'),
                   lambda s, c: s.update(seed=4) or c['endpoints'][0].update(supported_parameters=['reasoning', 'max_tokens', 'response_format']),
                   lambda s, c: c['endpoints'][0].update(reasoning={}),
                   lambda s, c: c.update(retrieved_at_utc='2001-01-01T00:00:00+00:00'),
                   lambda s, c: c['endpoints'][0]['pricing'].update(overrides=[{'cost': 10}])]
        for mutate in changes:
            s, c = settings(), capability()
            mutate(s, c)
            with self.assertRaises(EvalError):
                validate_settings(s, c, 'prisoner', [{'role': 'user', 'content': ESSAY}])

    def test_missing_key_and_live_gates_fail_before_network(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {}, clear=True), patch('socket.socket', side_effect=AssertionError('network forbidden')):
            with self.assertRaises(EvalError):
                api_key(Path(tmp))
            for flags in (['--execute'], ['--confirm-billable'], ['--execute', '--confirm-billable'],
                          ['--execute', '--confirm-billable', '--prompts-approved'],
                          ['--execute', '--confirm-billable', '--prompts-approved', '--source-terms-reviewed']):
                args = parser().parse_args(['run', 'researcher', '--assignment', 'cdt'] + flags)
                with self.assertRaises(EvalError):
                    run(Path(tmp), args)

    def test_budget_persistent_reserves_failed_calls(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'budget.jsonl'
            Budget(path, 2, '0.50').reserve([{'estimated_max_usd': '0.20'}], '1')
            with self.assertRaises(EvalError):
                Budget(path, 2, '0.50').reserve([{'estimated_max_usd': '0.40'}], '2')
            Budget(path, 2, '0.50').reserve([{'estimated_max_usd': '0.20'}], '3')
            with self.assertRaises(EvalError):
                Budget(path, 2, '0.50').reserve([{'estimated_max_usd': '0'}], '4')
            self.assertEqual(len(read(path).splitlines()), 2)

    def test_raw_truncated_response_preserved(self):
        class Response:
            status, headers = 200, {}
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def read(self): return b'{"model":"test/model","choices":[{"finish_reason":"length","message":{"content":"partial essay"}}]}'
        with tempfile.TemporaryDirectory() as tmp, patch('urllib.request.urlopen', return_value=Response()):
            with self.assertRaises(EvalError):
                post({'model': 'test/model'}, 'test-secret', Path(tmp))
            self.assertEqual(read(Path(tmp) / 'output.txt'), 'partial essay')
            self.assertIn('length', read(Path(tmp) / 'response.raw'))
            self.assertNotIn('test-secret', read(Path(tmp) / 'request.json'))

    def test_researcher_dry_run_without_key_or_network(self):
        args = parser().parse_args(['run', 'researcher', '--assignment', 'fdt_eq4'])
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {}, clear=True), patch('socket.socket', side_effect=AssertionError('network forbidden')):
            # Keep templates/configs in repo, but redirect only local artifacts.
            root = Path(tmp)
            import shutil
            for name in ('configs', 'prompts'):
                shutil.copytree(ROOT / name, root / name)
            with patch('almost_twin.router.load_source', return_value=(SOURCE, {'title': 'fixture', 'url': 'urn:fixture'})):
                folder = run(root, args)
            plan = json.loads(read(folder / 'plan.json'))
            self.assertFalse(plan['live'])
            self.assertIn('NOT VALIDATED', plan['validation'])
            self.assertFalse((root / 'data/budget.jsonl').exists())
            self.assertFalse((root / 'data/researcher_essays.jsonl').exists())


class RunnerIntegrationTests(unittest.TestCase):
    def make_root(self, tmp):
        import shutil
        root = Path(tmp)
        for name in ('configs', 'prompts'):
            shutil.copytree(ROOT / name, root / name)
        write_json(root / 'settings.json', settings())
        return root

    def response(self, output, fingerprint='fixed'):
        return {'model': 'test/model', 'provider': 'Test', 'system_fingerprint': fingerprint,
                'id': 'mock-response', 'usage': {'prompt_tokens': 30, 'completion_tokens': 20},
                'choices': [{'finish_reason': 'stop', 'message': {'content': output}}]}

    def test_two_independent_calls_frozen_essay_and_failure_journal(self):
        for invalid in (False, True):
            with self.subTest(invalid=invalid), tempfile.TemporaryDirectory() as tmp:
                root = self.make_root(tmp)
                seen = []
                outputs = [ESSAY, PASS_COMMAND, 'I prefer C' if invalid else SUBMIT_COMMAND]
                def fake_post(payload, key, folder):
                    seen.append(copy.deepcopy(payload))
                    output = outputs[len(seen) - 1]
                    data = self.response(output)
                    (folder / 'request.json').write_bytes(encoded(payload))
                    (folder / 'response.raw').write_bytes(encoded(data))
                    return data, output
                with patch('almost_twin.router.api_key', return_value='mock-only'), patch('almost_twin.router.snapshot', return_value=capability()), patch('almost_twin.router.post', side_effect=fake_post), patch('almost_twin.router.load_source', return_value=(SOURCE, {'title': 'synthetic', 'url': 'urn:fixture'})), patch('socket.socket', side_effect=AssertionError('real network forbidden')):
                    common_args = ['--settings', str(root / 'settings.json'), '--execute', '--confirm-billable', '--prompts-approved']
                    ra = parser().parse_args(['run', 'researcher', '--assignment', 'fdt_eq4', '--source-terms-reviewed'] + common_args)
                    essay_dir = run(root, ra)
                    self.assertEqual((essay_dir / 'essay.md').read_bytes(), ESSAY.encode())
                    pa = parser().parse_args(['run', 'prisoner', '--assignment', 'fdt_eq4', '--essay', str(essay_dir), '--scenario', 't2_name_001'] + common_args)
                    if invalid:
                        with self.assertRaises(EvalError):
                            run(root, pa)
                        self.assertFalse(list((root / 'data/runs').glob('*/outcome.json')))
                    else:
                        pair_dir = run(root, pa)
                        self.assertEqual(json.loads(read(pair_dir / 'outcome.json'))['years'], [5, 0])
                self.assertEqual(len(seen), 3)
                self.assertEqual(seen[1]['reasoning'], {'effort': 'low'})
                self.assertEqual(seen[0]['reasoning'], {'effort': 'high'})
                self.assertEqual(len(seen[1]['messages']), 1)
                self.assertEqual(len(seen[2]['messages']), 1)
                name_case = next(c for c in cases(ROOT) if c['case_id'] == 't2_name_001')
                self.assertEqual(
                    mask_private(seen[1]['messages'][0]['content'], name_case['private_a']),
                    mask_private(seen[2]['messages'][0]['content'], name_case['private_b']))
                for payload in seen[1:]:
                    self.assertIn(ESSAY, payload['messages'][0]['content'])
                    self.assertIn('**Your command?**', payload['messages'][0]['content'])
                    self.assertNotIn('response_format', payload)
                events = [json.loads(l) for l in read(root / 'data/prisoner_decisions.jsonl').splitlines()]
                if invalid:
                    self.assertEqual(events[-1]['status'], 'failed')
                    self.assertNotIn('committed_action', events[-1])
                    self.assertEqual(len(read(root / 'data/commitments.jsonl').splitlines()), 1)
                else:
                    self.assertEqual([e['status'] for e in events], ['started', 'success', 'started', 'success'])


if __name__ == '__main__':
    unittest.main()
