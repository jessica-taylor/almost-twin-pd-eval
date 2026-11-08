"""Version-matched MediaWiki API acquisition and mechanical Markdown extraction.

Only API JSON is downloaded. Media, scripts, styles and linked pages are never fetched.
"""
from collections import Counter
import hashlib
import json
import re
from html import unescape
from pathlib import Path
from urllib.parse import urlencode, urljoin

from .common import EvalError, read, sha
from .sources import DOM, Node, clean

VERSION = 'mediawiki-markdown/1.0'
API = 'https://en.wikipedia.org/w/api.php'
MODIFICATIONS = [
    'Mechanically converted revision-pinned rendered HTML to Markdown; retained article prose, headings, lists, tables, citations and references.',
    'Recovered formula LaTeX from MathML annotations/image alt text, or the same revision wikitext in order when counts match; did not rewrite, summarize or repair formulas.',
    'Removed navigation, edit controls, styles and website UI; excluded media bytes/URLs while retaining meaningful text descriptions.',
    'Prepended title, contributor attribution, revision/history URLs, license and conversion notice.'
]
RIGHTS = 'Individual media and third-party quoted material may have separate rights. Source reuse or adaptations in future publications may carry attribution/share-alike or other obligations.'


def api_url(**params):
    return API + '?' + urlencode({'format': 'json', 'formatversion': 2, **params})


def revision_url(spec, revision_id=None):
    pin = spec.get('revision_id') if revision_id is None else revision_id
    params = {'action': 'query', 'prop': 'revisions', 'rvprop': 'ids|timestamp|content|size|sha1', 'rvslots': 'main'}
    if pin is None and spec.get('revision_review') == 'approved':
        raise EvalError('An approved Wikipedia source must have an explicit revision_id pin')
    if pin is None:
        params['titles'] = spec['page_title']
    elif isinstance(pin, int) and not isinstance(pin, bool) and pin > 0:
        params['revids'] = pin
    else:
        raise EvalError('MediaWiki revision_id must be a positive integer or null pending manual review')
    return api_url(**params)


def parse_url(revision_id):
    return api_url(action='parse', oldid=revision_id, prop='text|revid|wikitext|sections|parsewarnings',
                   disableeditsection=1, disabletoc=1)


def api_json(path):
    try:
        data = json.loads(read(path))
    except (ValueError, UnicodeError) as error:
        raise EvalError('Truncated or non-JSON MediaWiki response') from error
    if not isinstance(data, dict) or data.get('error') or 'continue' in data:
        raise EvalError('MediaWiki API error or incomplete/paginated response')
    return data


def revision_data(data, spec):
    try:
        pages = data['query']['pages']
        if len(pages) != 1 or pages[0].get('missing') or pages[0].get('invalid') or pages[0]['ns'] != 0:
            raise EvalError('Expected one existing main-namespace Wikipedia article')
        page = pages[0]
        if page['title'] != spec['page_title']:
            raise EvalError('MediaWiki returned a different article title')
        revisions = page['revisions']
        if len(revisions) != 1:
            raise EvalError('Expected exactly one article revision')
        revision = revisions[0]
        rev_id = revision['revid']
        if not isinstance(rev_id, int) or rev_id <= 0 or (spec.get('revision_id') is not None and rev_id != spec['revision_id']):
            raise EvalError('Wikipedia revision does not match the manifest pin')
        main = revision['slots']['main']
        text = main['content']
        if main['contentmodel'] != 'wikitext' or not isinstance(text, str) or not text.strip() or revision.get('texthidden') or main.get('texthidden'):
            raise EvalError('Missing or unavailable revision wikitext')
        if revision['size'] != len(text.encode('utf-8')):
            raise EvalError('Wikitext byte count disagrees with revision size (truncated content)')
        if hashlib.sha1(text.encode('utf-8')).hexdigest() != revision['sha1']:
            raise EvalError('Wikitext SHA-1 disagrees with MediaWiki revision')
        timestamp = revision['timestamp']
        if not re.fullmatch(r'\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ', timestamp):
            raise EvalError('Missing or invalid revision UTC timestamp')
        return rev_id, timestamp, text
    except (KeyError, IndexError, TypeError) as error:
        raise EvalError('Incomplete MediaWiki revision response') from error


def parsed_data(data, spec, revision_id, wikitext):
    try:
        parsed = data['parse']
        if parsed['revid'] != revision_id or parsed['title'] != spec['page_title']:
            raise EvalError('Wikitext/rendered HTML revision or title mismatch')
        if parsed['wikitext'] != wikitext:
            raise EvalError('Parse API wikitext differs from the retrieved revision')
        html = parsed['text']
        if not isinstance(html, str) or not html.strip():
            raise EvalError('Empty rendered article HTML')
        sections = parsed['sections']
        if not isinstance(sections, list):
            raise EvalError('Missing or invalid MediaWiki section metadata')
        return html, sections, parsed.get('parsewarnings', [])
    except (KeyError, TypeError) as error:
        raise EvalError('Incomplete MediaWiki Parse API response') from error


def plain(node):
    return node if isinstance(node, str) else ''.join(plain(c) for c in node.children)


def classes(node):
    return set(node.attrs.get('class', '').split())


def canonical_math(value):
    value = unescape(value).strip()
    # Wikimedia alt text often wraps TeX in {\displaystyle ...}.
    if value.startswith('{\\displaystyle') and value.endswith('}'):
        value = value[len('{\\displaystyle'):-1].strip()
    return re.sub(r'\s+', '', value)


class Markdown:
    def __init__(self, url, original_formulas, rendered_formula_count):
        self.url = url
        self.original_formulas = original_formulas
        self.rendered_formula_count = rendered_formula_count
        self.wikitext_recoveries = 0
        self.formulas, self.exclusions, self.warnings = [], [], []
        self.headings, self.references, self.prose = [], set(), []

    def formula(self, node):
        annotations = node.all(lambda n: n.tag == 'annotation' and n.attrs.get('encoding') in ('application/x-tex', 'application/x-latex'))
        candidates = [plain(n).strip() for n in annotations if plain(n).strip()]
        if not candidates:
            candidates = [n.attrs.get('alttext', '') for n in node.all(lambda n: n.tag == 'math') if n.attrs.get('alttext')]
        if not candidates:
            candidates = [n.attrs.get('alt', '') for n in node.all(lambda n: n.tag == 'img') if n.attrs.get('alt')]
        if not candidates:
            if self.rendered_formula_count != len(self.original_formulas) or len(self.formulas) >= len(self.original_formulas):
                raise EvalError('Mathematical formula lacks LaTeX metadata and cannot be matched to original wikitext; manual review required')
            # Exact source bytes, never a guessed MathML-to-LaTeX reconstruction.
            candidates = [self.original_formulas[len(self.formulas)]]
            self.wikitext_recoveries += 1
            self.warnings.append('Rendered MathML omits LaTeX annotations: recovered exact revision-wikitext formulas in document order with matching expression counts. Per-expression correspondence requires manual mathematical review.')
        formula = candidates[0]
        if not formula.strip() or '\ufffd' in formula:
            raise EvalError('Empty/damaged mathematical expression')
        self.formulas.append(formula)
        if '\n' in formula or node.attrs.get('display') == 'block' or any('display' in c or 'block' in c for c in classes(node)):
            return '\n\n\\[\n' + formula.strip() + '\n\\]\n\n'
        return '\\(' + formula + '\\)'

    def convert(self, node):
        if isinstance(node, str):
            return node
        tag, attrs, css = node.tag, node.attrs, classes(node)
        if tag in ('script', 'style', 'nav') or css & {'mw-editsection', 'mw-empty-elt', 'navbox', 'vertical-navbox', 'sidebar', 'toc', 'metadata', 'catlinks', 'sistersitebox'} or attrs.get('role') == 'navigation':
            return ''
        if css & {'error', 'mw-ext-cite-error'}:
            # Retain publisher diagnostics; they do not justify dropping surrounding references.
            self.warnings.append('Rendered article contains a publisher parser/citation error; retained in source and requires manual review.')
        if 'mwe-math-element' in css or tag == 'math' or (tag in ('img', 'svg') and any('math' in c for c in css)):
            return self.formula(node)
        if tag in ('img', 'svg', 'video', 'audio', 'source'):
            description = attrs.get('alt') or attrs.get('aria-label') or ''
            self.exclusions.append({'element': tag, 'description': description, 'reason': 'Media excluded; separate rights may apply'})
            if not description and tag in ('img', 'svg'):
                self.warnings.append('A non-math image lacked a text description; inspect original revision for relevant visual content.')
            return ('[Image description: ' + description + ']') if description else ''
        if tag in ('p', 'li', 'dt', 'dd'):
            self.prose.append(node)
        if tag == 'table':
            rows = node.all(lambda n: n.tag == 'tr')
            converted = []
            for row in rows:
                cells = [c for c in row.children if isinstance(c, Node) and c.tag in ('th', 'td')]
                if not cells:
                    continue
                if any(c.attrs.get('rowspan', '1') != '1' or c.attrs.get('colspan', '1') != '1' for c in cells):
                    self.warnings.append('Table has merged cells; Markdown flattens their span. Compare with rendered.html.')
                converted.append([self.convert(c).strip().replace('\n', '<br>').replace('|', '\\|') for c in cells])
            if not converted:
                return ''
            width = max(map(len, converted))
            converted = [r + [''] * (width - len(r)) for r in converted]
            caption = ''.join(self.convert(c) for c in node.children if isinstance(c, Node) and c.tag == 'caption')
            lines = ['| ' + ' | '.join(row) + ' |' for row in converted]
            lines.insert(1, '| ' + ' | '.join(['---'] * width) + ' |')
            return '\n\n' + caption + '\n' + '\n'.join(lines) + '\n\n'
        text = ''.join(self.convert(c) for c in node.children)
        anchor = attrs.get('id')
        prefix = ''
        if anchor and (anchor.startswith('cite_note') or anchor.startswith('cite_ref')):
            self.references.add(anchor)
            prefix = f'<a id="{anchor}"></a>'
        if re.fullmatch(r'h[1-6]', tag):
            self.headings.append(node)
            return '\n\n' + '#' * int(tag[1]) + ' ' + text.strip() + '\n\n'
        if tag in ('p', 'div', 'section', 'blockquote', 'figure', 'figcaption', 'dl'):
            return '\n\n' + text.strip() + '\n\n'
        if tag == 'li':
            return '\n- ' + prefix + text.strip() + '\n'
        if tag in ('dt', 'dd'):
            return '\n' + prefix + text.strip() + '\n'
        if tag == 'br':
            return '\n'
        if tag in ('sup', 'sub'):
            return prefix + f'<{tag}>{text}</{tag}>'
        if tag == 'a' and attrs.get('href'):
            href = attrs['href']
            if re.match(r'^(?:https?:)?//[^/]*(?:upload|commons)\.wikimedia\.org/', href) or '/wiki/File:' in href:
                return text  # Preserve description but do not embed/link image assets.
            return '[' + text + '](' + (href if href.startswith('#') else urljoin(self.url, href)) + ')'
        if tag in ('em', 'i', 'b', 'strong'):
            marker = '**' if tag in ('b', 'strong') else '*'
            return marker + text + marker
        if tag in ('pre', 'code'):
            return '\n```text\n' + text + '\n```\n'
        return prefix + text


def extract(html, wikitext, sections, url):
    dom = DOM(html)
    if len(dom.stack) != 1:
        raise EvalError('Truncated/unbalanced MediaWiki article HTML')
    body = dom.root.find(lambda n: 'mw-parser-output' in classes(n))
    if not body:
        raise EvalError('Missing MediaWiki article body')
    formulas = re.findall(r'<math\b[^>]*>(.*?)</math\s*>', wikitext, re.S | re.I)
    def count_formulas(node):
        if isinstance(node, str):
            return 0
        if 'mwe-math-element' in classes(node) or node.tag == 'math' or (node.tag in ('img', 'svg') and any('math' in c for c in classes(node))):
            return 1
        return sum(count_formulas(c) for c in node.children)
    converter = Markdown(url, formulas, count_formulas(body))
    text = clean(converter.convert(body))
    if len(text.strip()) < 400 or len(text.split()) < 60 or '\ufffd' in text:
        raise EvalError('Wikipedia article empty, too short, or encoding-damaged')
    for section in sections:
        anchor = section.get('anchor')
        if not anchor or not body.find(lambda n: n.attrs.get('id') == anchor):
            raise EvalError('Missing/truncated article section from Parse API metadata')
        heading = dom.root.find(lambda n: n.attrs.get('id') == anchor)
        label = re.sub(r'\s+', ' ', plain(heading)).strip()
        if label not in re.sub(r'\s+', ' ', re.sub(r'[*_]', '', text)):
            raise EvalError(f'Section lost during Markdown conversion: {anchor}')
    if len(re.findall(r'<math\b', wikitext, re.I)) != len(formulas):
        raise EvalError('Truncated mathematical tag in original wikitext')
    original_counts = Counter(canonical_math(f) for f in formulas)
    converted_counts = Counter(canonical_math(f) for f in converter.formulas)
    if original_counts - converted_counts:
        raise EvalError('Wikitext formula missing or changed in rendered HTML/Markdown; manual mathematical review required')
    for link in body.all(lambda n: n.tag == 'a' and n.attrs.get('href', '').startswith('#cite_note')):
        if link.attrs['href'][1:] not in converter.references:
            raise EvalError('Citation points to a missing reference/footnote')
    # Every kept paragraph/list body must leave its textual tokens in the output.
    # Compare token coverage globally to permit inline Markdown formatting.
    def visible_plain(node):
        if isinstance(node, str):
            return node
        if node.tag in ('script', 'style', 'nav', 'math') or classes(node) & {'mwe-math-element', 'mw-editsection', 'navbox', 'sidebar', 'toc', 'metadata'}:
            return ''
        return ''.join(visible_plain(c) for c in node.children)
    output_words = set(re.findall(r'\w+', text))
    for node in converter.prose:
        expected = set(re.findall(r'\w+', visible_plain(node)))
        if len(expected - output_words) > max(3, len(expected) // 10):
            raise EvalError('Substantive paragraph/list content lost during extraction')
    stats = {'headings': len(converter.headings), 'math_expressions': len(converter.formulas),
             'wikitext_math_expressions': len(formulas), 'wikitext_math_recoveries': converter.wikitext_recoveries,
             'reference_anchors': len(converter.references)}
    return text, stats, sorted(set(converter.warnings)), converter.exclusions


def exposure_annotations(text):
    # Descriptive, deliberately conservative term scans. Never model-visible instructions.
    prose = re.sub(r'\s+', ' ', text).lower()
    checks = {
        'Ordinary prisoner\u2019s dilemma examples': r'prisoner.{0,15}dilemma',
        'Twin or identical-agent examples': r'\btwins?\b|identical (?:agents?|decision)|copies of',
        'Same-algorithm cooperation arguments': r'(?:same|identical).{0,100}(?:algorithm|program)|(?:algorithm|program).{0,100}(?:cooperat|identical|same)',
        'Other unusually close evaluation material (correlation/dependence)': r'correlat|dependen|psychological'}
    result = {label: ('Detected by term scan; inspect the complete article in context.' if re.search(pattern, prose) else
                      'Not detected by term scan; absence is not established. Manual review required.') for label, pattern in checks.items()}
    if re.search(r'\btwin\b', prose) and re.search('cooperat', prose):
        label = 'Same-algorithm cooperation arguments'
        if result[label].startswith('Not detected'):
            result[label] = 'Twin/correlated-reasoning cooperation material is present. The scan does not establish an explicit same-algorithm premise; review this related exposure manually.'
    return result


def attribution(spec, revision_id, timestamp):
    title = spec['page_title']
    permanent = 'https://en.wikipedia.org/w/index.php?' + urlencode({'title': title.replace(' ', '_'), 'oldid': revision_id})
    history = 'https://en.wikipedia.org/w/index.php?' + urlencode({'title': title.replace(' ', '_'), 'action': 'history'})
    return {'article_title': title, 'contributors': 'Wikipedia contributors', 'revision_id': revision_id,
            'revision_timestamp': timestamp, 'permanent_url': permanent, 'history_url': history,
            'license_name': 'Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)',
            'license_url': 'https://creativecommons.org/licenses/by-sa/4.0/',
            'modifications': MODIFICATIONS, 'rights_qualifications': RIGHTS}


def attribution_text(info):
    return (f'# {info["article_title"]}\n\n'
            f'By {info["contributors"]} ([revision history]({info["history_url"]})). '
            f'[Permanent revision {info["revision_id"]}]({info["permanent_url"]}), {info["revision_timestamp"]}.\n\n'
            f'License: [{info["license_name"]}]({info["license_url"]}).\n\n'
            'Conversion modifications: ' + ' '.join(info['modifications']) + '\n\n' + info['rights_qualifications'] + '\n\n')


def acquire(spec, get, provenance, artifact_folder):
    query = api_json(get(revision_url(spec), 'revision.json'))
    revision_id, timestamp, wikitext = revision_data(query, spec)
    parsed = api_json(get(parse_url(revision_id), 'parse.json'))
    html, sections, warnings = parsed_data(parsed, spec, revision_id, wikitext)
    provenance['artifacts'] = {}
    for filename, content, origin in (('revision.wikitext', wikitext, 'revision.json'), ('rendered.html', html, 'parse.json')):
        (artifact_folder / filename).write_bytes(content.encode('utf-8'))
        provenance['artifacts'][filename] = {'sha256': sha(content), 'bytes': len(content.encode('utf-8')), 'derived_from': origin}
    credit = attribution(spec, revision_id, timestamp)
    provenance.update(revision=revision_id, revision_id=revision_id, revision_timestamp=timestamp,
                      url=credit['permanent_url'], permanent_url=credit['permanent_url'], attribution=credit,
                      method='mediawiki', mediawiki_extractor=VERSION,
                      mediawiki_extractor_sha256=sha(Path(__file__).read_bytes()),
                      conversion_command='MediaWiki query revisions -> parse oldid -> stdlib HTMLParser -> Markdown',
                      revision_pinned=spec.get('revision_id') is not None,
                      manual_revision_review=spec.get('revision_review', 'pending'))
    text, stats, extraction_warnings, exclusions = extract(html, wikitext, sections, credit['permanent_url'])
    if '\\begin{align}' in wikitext:
        extraction_warnings.append('Original LaTeX align environments are preserved verbatim; some Markdown math viewers may not render them inside display delimiters. Compare raw wikitext, rendered HTML and Markdown manually.')
    text = attribution_text(credit) + text
    provenance.update(text_statistics=stats, media_exclusions=exclusions,
                      experimental_exposure=exposure_annotations(text))
    provenance['warnings'].extend(extraction_warnings)
    if warnings:
        provenance['warnings'].append('MediaWiki parse warnings: ' + json.dumps(warnings, ensure_ascii=False))
    if query.get('warnings') or parsed.get('warnings'):
        provenance['warnings'].append('MediaWiki API warnings are retained in raw JSON; inspect before manual approval.')
    if spec.get('revision_id') is None:
        provenance['warnings'].append('Revision discovered but NOT manually approved/pinned. After review set revision_id and revision_review in the manifest.')
    provenance['warnings'].extend([
        'Wikipedia is a licensed reference condition, not necessarily as comprehensive or philosophically authoritative as SEP.',
        'oldid pins article wikitext; expanded templates may reflect their retrieval-time revisions. Frozen rendered HTML and its hash preserve what was supplied.'])
    return text
