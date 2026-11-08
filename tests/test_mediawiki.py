"""Synthetic API responses only. No article excerpts or credentials are fixtures."""
import copy
import json
import os
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.parse import parse_qs, urlparse

from almost_twin.cli import parser
from almost_twin.common import EvalError, load_yaml, read, sha, write_json
from almost_twin.mediawiki import api_json, extract, parsed_data, revision_data, revision_url
from almost_twin.prompts import assignment, cases, prisoners, render, researcher
from almost_twin.router import run
from almost_twin.sources import fetch_one, load_source, quality

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / 'tests/fixtures/mediawiki'


class MediaWikiTests(unittest.TestCase):
    def setUp(self):
        self.spec = load_yaml(ROOT / 'sources/manifest.yaml')['sources']['cdt_wikipedia']
        self.query = json.loads(read(FIXTURES / 'revision.json'))
        self.parsed = json.loads(read(FIXTURES / 'parse.json'))

    def root(self, tmp):
        root = Path(tmp)
        for folder in ('sources', 'configs', 'prompts', 'fixtures'):
            shutil.copytree(ROOT / folder, root / folder)
        return root

    def downloader(self, requests):
        def fake(url, dest):
            requests.append(url)
            params = parse_qs(urlparse(url).query)
            data = self.query if params['action'] == ['query'] else self.parsed
            if params['action'] == ['parse']:
                self.assertEqual(params['oldid'], ['123456'])
                self.assertNotIn('page', params)
            payload = (json.dumps(data, ensure_ascii=False) + '\n').encode()
            dest.write_bytes(payload)
            return {'url': url, 'resolved_url': url, 'retrieved_at_utc': '2026-11-01T00:00:00+00:00',
                    'raw_file': dest.name, 'raw_sha256': sha(payload), 'bytes': len(payload), 'content_type': 'application/json'}
        return fake

    def fetch(self, root, spec=None):
        requests = []
        with patch('almost_twin.sources.download', side_effect=self.downloader(requests)), patch('socket.socket', side_effect=AssertionError('network forbidden')), patch('almost_twin.sources.sep_extract', side_effect=AssertionError('wrong extractor')):
            info, folder = fetch_one(root, 'cdt_wikipedia', spec or self.spec, network=True)
        self.assertEqual(len(requests), 2)
        return info, folder, requests

    def test_revision_selection_pinning_and_consistency(self):
        url = revision_url(self.spec)
        self.assertEqual(parse_qs(urlparse(url).query)['titles'], ['Causal decision theory'])
        pinned = {**self.spec, 'revision_id': 123456, 'revision_review': 'approved'}
        params = parse_qs(urlparse(revision_url(pinned)).query)
        self.assertEqual(params['revids'], ['123456'])
        self.assertNotIn('titles', params)
        rev, stamp, wiki = revision_data(self.query, pinned)
        html, sections, _ = parsed_data(self.parsed, pinned, rev, wiki)
        self.assertEqual(stamp, '2026-10-01T12:00:00Z')
        self.assertIn('Decision rule', html)
        for mutate in (
            lambda d: d['parse'].update(revid=123457),
            lambda d: d['parse'].update(wikitext=wiki + ' altered'),
            lambda d: d['parse'].update(title='Different article'),
        ):
            data = copy.deepcopy(self.parsed)
            mutate(data)
            with self.assertRaises(EvalError):
                parsed_data(data, pinned, rev, wiki)
        with self.assertRaises(EvalError):
            revision_data(self.query, {**pinned, 'revision_id': 9})

    def test_pinned_acquisition_and_incomplete_api_errors(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.root(tmp)
            pinned = {**self.spec, 'revision_id': 123456, 'revision_review': 'approved'}
            info, _, requests = self.fetch(root, pinned)
            self.assertEqual(parse_qs(urlparse(requests[0]).query)['revids'], ['123456'])
            self.assertTrue(info['revision_pinned'])
            with self.assertRaises(EvalError):
                revision_url({**self.spec, 'revision_review': 'approved'})
            damaged = copy.deepcopy(self.parsed)
            del damaged['parse']['sections']
            with self.assertRaises(EvalError):
                parsed_data(damaged, self.spec, 123456, self.parsed['parse']['wikitext'])
            for content in ('{', '{"error":{"code":"badrevid"}}', '{"continue":{}}'):
                path = root / 'bad.json'
                path.write_text(content)
                with self.assertRaises(EvalError):
                    api_json(path)

    def test_math_sections_examples_citations_tables_and_no_image_urls(self):
        rev, _, wiki = revision_data(self.query, self.spec)
        html, sections, _ = parsed_data(self.parsed, self.spec, rev, wiki)
        text, stats, warnings, exclusions = extract(html, wiki, sections, 'https://en.wikipedia.org/w/index.php?oldid=123456')
        for expected in ('## Decision rule', '## Examples', 'First example', 'Second example', 'twin agents',
                         'V(a)=\\sum_s P(s)U(a,s)', 'Example Author. Invented reference.',
                         '<a id="cite_note-fiction-1"></a>', '| Action | Value |', '| Sample | 3 |',
                         'A meaningful diagram description', 'Example diagram caption.'):
            self.assertIn(expected, text)
        for excluded in ('https://example.test/diagram.png', 'https://example.test/formula.svg', 'Unrelated navigation', 'mw-editsection', 'display:block'):
            self.assertNotIn(excluded, text)
        self.assertEqual(stats['math_expressions'], 1)  # MathML + fallback image are one expression.
        self.assertEqual(stats['wikitext_math_expressions'], 1)
        self.assertEqual(len(exclusions), 1)

    def test_annotation_free_mathml_uses_original_wikitext_with_explicit_review_warning(self):
        import re
        rev, _, wiki = revision_data(self.query, self.spec)
        html, sections, _ = parsed_data(self.parsed, self.spec, rev, wiki)
        html = re.sub(r'<annotation.*?</annotation>', '', html)
        html = re.sub(r'<img class="mwe-math-fallback-image-inline"[^>]*>', '', html)
        text, stats, warnings, _ = extract(html, wiki, sections, 'https://en.wikipedia.org/')
        self.assertIn('V(a)=\\sum_s P(s)U(a,s)', text)
        self.assertEqual(stats['wikitext_math_recoveries'], 1)
        self.assertTrue(any('manual mathematical review' in w for w in warnings))
        with self.assertRaises(EvalError):
            extract(html.replace('</p>', '<math><mi>x</mi></math></p>', 1), wiki, sections, 'https://en.wikipedia.org/')

    def test_missing_math_or_truncated_article_fails(self):
        rev, _, wiki = revision_data(self.query, self.spec)
        html, sections, _ = parsed_data(self.parsed, self.spec, rev, wiki)
        bad_html = [html[:-6], html.replace('id="References"', 'id="Missing"'),
                    html.replace('id="cite_note-fiction-1"', 'id="missing-note"'),
                    html.replace('V(a)=\\sum_s P(s)U(a,s)', 'V(a)=1'),

                    '<div class="mw-parser-output">empty</div>']
        for damaged in bad_html:
            with self.subTest(damaged=damaged[:60]), self.assertRaises(EvalError):
                extract(damaged, wiki, sections, 'https://en.wikipedia.org/')
        data = copy.deepcopy(self.query)
        data['query']['pages'][0]['revisions'][0]['slots']['main']['content'] += 'changed'
        with self.assertRaises(EvalError):
            revision_data(data, self.spec)

    def test_acquisition_reextraction_and_attribution_in_source_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.root(tmp)
            info, folder, requests = self.fetch(root)
            self.assertEqual(info['revision'], 123456)
            self.assertEqual(info['method'], 'mediawiki')
            self.assertFalse(info['revision_pinned'])
            self.assertEqual(info['revision_timestamp'], '2026-10-01T12:00:00Z')
            self.assertIn('CC BY-SA 4.0', info['attribution']['license_name'])
            self.assertIn('Twin or identical-agent examples', info['experimental_exposure'])
            text, loaded = load_source(root, 'cdt_wikipedia')
            self.assertEqual(loaded['provenance_sha256'], sha((folder / 'provenance.json').read_bytes()))
            self.assertIn('Wikipedia contributors', text)
            self.assertIn('action=history', text)
            self.assertIn('oldid=123456', text)
            self.assertIn('creativecommons.org/licenses/by-sa/4.0/', text)
            self.assertIn('third-party quoted material', text)
            self.assertNotIn('experimental exposure', text.lower())
            for filename in ('revision.json', 'parse.json', 'revision.wikitext', 'rendered.html', 'article.md'):
                self.assertTrue((folder / filename).is_file())
            with patch('socket.socket', side_effect=AssertionError('network forbidden')):
                again, other = fetch_one(root, 'cdt_wikipedia', self.spec, network=False, reextract=True)
            self.assertNotEqual(folder, other)
            self.assertEqual(again['downloads'], info['downloads'])
            self.assertEqual((folder / 'article.md').read_bytes(), (other / 'article.md').read_bytes())
            self.assertEqual(again['artifacts'], info['artifacts'])
            # A manual manifest pin can be applied after review without replacing the cached bytes.
            pinned = {**self.spec, 'revision_id': 123456, 'revision_review': 'approved'}
            with patch('socket.socket', side_effect=AssertionError('network forbidden')):
                approved, _ = fetch_one(root, 'cdt_wikipedia', pinned, network=False, reextract=True)
            self.assertTrue(approved['revision_pinned'])
            with patch('socket.socket', side_effect=AssertionError('network forbidden')):
                with self.assertRaises(EvalError):
                    fetch_one(root, 'cdt_wikipedia', {**pinned, 'revision_id': 123457}, network=False, reextract=True)

    def test_hash_verification_rejects_altered_raw_derived_normalized_and_metadata(self):
        for filename in ('revision.json', 'parse.json', 'revision.wikitext', 'rendered.html', 'article.md', 'provenance.json'):
            with self.subTest(filename=filename), tempfile.TemporaryDirectory() as tmp:
                root = self.root(tmp)
                _, folder, _ = self.fetch(root)
                with (folder / filename).open('ab') as stream:
                    stream.write(b' tampered')
                with self.assertRaises(EvalError):
                    load_source(root, 'cdt_wikipedia')
                if filename in ('revision.json', 'parse.json', 'revision.wikitext', 'rendered.html', 'article.md', 'provenance.json'):
                    with self.assertRaises(EvalError), patch('socket.socket', side_effect=AssertionError('network forbidden')):
                        fetch_one(root, 'cdt_wikipedia', self.spec, network=False, reextract=True)

    def test_assignments_cli_metadata_and_no_new_instructions(self):
        for source_id, theory in (('cdt_wikipedia', 'CDT'), ('edt_wikipedia', 'EDT')):
            with self.subTest(source_id=source_id), tempfile.TemporaryDirectory() as tmp:
                root = self.root(tmp)
                spec = load_yaml(root / 'sources/manifest.yaml')['sources'][source_id]
                self.query['query']['pages'][0]['title'] = spec['page_title']
                self.parsed['parse']['title'] = spec['page_title']
                with patch('almost_twin.sources.download', side_effect=self.downloader([])):
                    info, source_dir = fetch_one(root, source_id, spec, network=True)
                item = assignment(root, source_id)
                self.assertEqual(item['source_id'], source_id)
                self.assertEqual(item['theory_label'], theory)
                source, loaded = load_source(root, source_id)
                request = researcher(root, item, source, loaded)[0]['content']
                self.assertIn(source, request)
                # The ordinary article examples survive; only harness-added target instructions are forbidden.
                instruction_only = request.replace(source, '')
                for forbidden in ('almost-twin', 't0_identical', 't2_name', 't4_distinct', 'Rowan', 'Sasha', 'benchmark', 'hypotheses'):
                    self.assertNotIn(forbidden.lower(), instruction_only.lower())
                self.assertNotIn('wikipedia', instruction_only.split('## Human-written reference')[0].lower())
                for pair in (prisoners(root, item, 'Synthetic frozen essay.\n', case) for case in cases(root)):
                    for messages in pair:
                        self.assertNotIn(source, messages[0]['content'])
                        self.assertNotIn('Wikipedia contributors', messages[0]['content'])
                with patch.dict(os.environ, {}, clear=True), patch('socket.socket', side_effect=AssertionError('network forbidden')):
                    rendered = render(root, source_id, essay_path=root / 'fixtures/demo_essay.md')
                    args = parser().parse_args(['run', 'researcher', '--assignment', source_id, '--settings', str(root / 'configs/openrouter.example.json')])
                    run_dir = run(root, args)
                plan = json.loads(read(run_dir / 'plan.json'))
                self.assertEqual(plan['assignment'], source_id)
                self.assertEqual(plan['theory'], theory)
                self.assertEqual(plan['source_id'], source_id)
                self.assertEqual(plan['source_revision'], 123456)
                self.assertIn('oldid=123456', plan['source_permanent_url'])
                self.assertEqual(plan['source_sha256'], sha(source))
                self.assertEqual(plan['source_provenance_sha256'], sha((source_dir / 'provenance.json').read_bytes()))
                self.assertFalse(plan['live'])
                self.assertEqual(parser().parse_args(['fetch-sources', '--source', source_id]).source, [source_id])
                self.assertEqual(parser().parse_args(['render-prompts', '--assignment', source_id]).assignment, source_id)

    def test_prisoner_dry_run_preserves_historical_source_identity_without_reloading_article(self):
        for source_id, theory in (('cdt_wikipedia', 'CDT'), ('edt_wikipedia', 'EDT')):
            with self.subTest(source_id=source_id), tempfile.TemporaryDirectory() as tmp:
                root = self.root(tmp)
                frozen = root / 'data/runs/synthetic-researcher-fixture'
                essay = 'SYNTHETIC TEST ARTIFACT. Frozen essay for network-free dry-run validation.'
                frozen.mkdir(parents=True)
                (frozen / 'essay.md').write_text(essay)
                info = {'status': 'success', 'assignment': source_id, 'theory': theory,
                        'model': None, 'provider_tag': None, 'essay_id': 'synthetic-test-id',
                        'essay_sha256': sha(essay), 'researcher_effort': None, 'source_id': source_id,
                        'source_revision': 123456, 'source_permanent_url': 'https://en.wikipedia.org/w/index.php?oldid=123456',
                        'source_revision_timestamp': '2026-10-01T12:00:00Z',
                        'source_sha256': 'frozen-source-hash', 'source_provenance_sha256': 'frozen-provenance-hash'}
                write_json(frozen / 'essay.json', info)
                write_json(frozen / 'call_0/response.raw', {'model': None, 'choices': [{'finish_reason': 'stop', 'message': {'content': essay}}]})
                args = parser().parse_args(['run', 'prisoner', '--assignment', source_id, '--essay', str(frozen),
                                           '--settings', str(root / 'configs/openrouter.example.json')])
                # Change the current assignment source to prove the frozen metadata is used.
                path = root / 'configs/early_test.yaml'
                path.write_text(read(path).replace('source_id: ' + source_id, 'source_id: cdt'))
                with patch('socket.socket', side_effect=AssertionError('network forbidden')), patch('almost_twin.router.load_source', side_effect=AssertionError('article must not be loaded for prisoners')):
                    result = run(root, args)
                plan = json.loads(read(result / 'plan.json'))
                for field in ('source_id', 'source_revision', 'source_permanent_url', 'source_sha256', 'source_provenance_sha256', 'theory'):
                    self.assertEqual(plan[field], info[field])
                self.assertFalse(plan['live'])
                self.assertIn(essay, read(result / 'messages_0.md'))
                self.assertNotIn('Wikipedia contributors', read(result / 'messages_0.md'))

    def test_existing_source_routes_unchanged_and_short_wikipedia_allowed(self):
        manifest = load_yaml(ROOT / 'sources/manifest.yaml')['sources']
        self.assertEqual(manifest['cdt']['url'], 'https://plato.stanford.edu/entries/decision-causal/')
        self.assertEqual(manifest['edt']['url'], 'https://plato.stanford.edu/entries/decision-theory/')
        self.assertEqual(manifest['fdt']['preferred_source_url'], 'https://arxiv.org/src/1710.05060v2')
        short = 'A synthetic short Wikipedia article about choices. ' * 15
        quality('cdt_wikipedia', short, 'mediawiki')
        for name in ('cdt', 'edt', 'fdt'):
            with self.assertRaises(EvalError):
                quality(name, short, 'html')


if __name__ == '__main__':
    unittest.main()
