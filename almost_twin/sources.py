"""Mechanical local extraction only. No LLM, TeX execution, or OCR."""
import gzip
import io
import json
import re
import shutil
import subprocess
import tarfile
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import urljoin

from .common import EvalError, load_yaml, read, sha, utc, write_json

VERSION = 'mechanical-source-extractor/1.0'
MAX_BYTES = 30_000_000


def download(url, dest):
    req = urllib.request.Request(url, headers={'User-Agent': 'AlmostTwinSourceAudit/0.1 (personal research download)'})
    with urllib.request.urlopen(req, timeout=30) as response:
        body = response.read(MAX_BYTES + 1)
        expected = response.headers.get('Content-Length')
        if not body or len(body) > MAX_BYTES or (expected and len(body) != int(expected)):
            raise EvalError(f'Empty, oversized, or truncated download: {url}')
        dest.write_bytes(body)
        return {'url': url, 'resolved_url': response.url, 'retrieved_at_utc': utc(),
                'raw_file': dest.name, 'raw_sha256': sha(body), 'bytes': len(body),
                'content_type': response.headers.get('Content-Type')}


class Node:
    def __init__(self, tag='', attrs=()):
        self.tag, self.attrs, self.children = tag, dict(attrs), []

    def find(self, predicate):
        if predicate(self):
            return self
        for c in self.children:
            if isinstance(c, Node):
                hit = c.find(predicate)
                if hit:
                    return hit
        return None

    def all(self, predicate):
        out = [self] if predicate(self) else []
        for c in self.children:
            if isinstance(c, Node):
                out.extend(c.all(predicate))
        return out


class DOM(HTMLParser):
    VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'wbr'}

    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.root = Node()
        self.stack = [self.root]
        self.feed(html)
        self.close()

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in self.VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def html_md(node, base):
    if isinstance(node, str):
        # Preserve literal TeX, including line breaks in display equations.
        return node
    tag, attrs = node.tag, node.attrs
    if tag in ('script', 'style', 'nav'):
        return ''
    s = ''.join(html_md(c, base) for c in node.children)
    if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
        return '\n\n' + '#' * int(tag[1]) + ' ' + s.strip() + '\n\n'
    if tag in ('p', 'div', 'section', 'blockquote', 'dl'):
        return '\n\n' + s.strip() + '\n\n'
    if tag == 'li':
        return '\n- ' + s.strip() + '\n'
    if tag == 'dt':
        return '\n\n' + s.strip() + '\n'
    if tag == 'dd':
        return '\n' + s.strip() + '\n'
    if tag == 'br':
        return '\n'
    if tag == 'tr':
        return '\n' + s + '\n'
    if tag in ('td', 'th'):
        return '| ' + s.strip() + ' '
    if tag in ('sup', 'sub'):
        return f'<{tag}>{s}</{tag}>'
    if tag == 'a' and attrs.get('href'):
        return f'[{s}]({urljoin(base, attrs["href"])})'
    if tag == 'img':
        alt = attrs.get('alt', '')
        if not alt.strip():
            raise EvalError('Article contains image without alt text; manual extraction required')
        return f'![{alt}]({urljoin(base, attrs.get("src", ""))})'
    if tag in ('em', 'i'):
        return f'*{s}*'
    if tag in ('b', 'strong'):
        return f'**{s}**'
    if tag in ('pre', 'code'):
        return '\n```text\n' + s + '\n```\n'
    return s


def clean(text):
    return re.sub(r'\n[ \t]*\n(?:[ \t]*\n)+', '\n\n', text).strip() + '\n'


def sep_extract(html, url, notes_html=None):
    dom = DOM(html).root
    body = dom.find(lambda n: n.attrs.get('id') == 'main-text')
    intro = dom.find(lambda n: n.attrs.get('id') == 'preamble')
    pub = dom.find(lambda n: n.attrs.get('id') == 'pubinfo')
    title = dom.find(lambda n: n.tag == 'h1')
    bib = dom.find(lambda n: n.attrs.get('id') == 'bibliography')
    if not all((body, title, pub, bib)) or not re.search(r'</html\s*>', html, re.I):
        raise EvalError('Incomplete SEP HTML: expected article, revision, bibliography and closing HTML')
    selected = [title, pub] + ([intro] if intro else []) + [body, bib]
    note_links = body.all(lambda n: n.tag == 'a' and 'notes.html#note-' in n.attrs.get('href', ''))
    if note_links:
        if not notes_html:
            raise EvalError('SEP footnotes are required but missing')
        notes = DOM(notes_html).root
        if not re.search(r'</html\s*>', notes_html, re.I):
            raise EvalError('Truncated SEP notes HTML')
        for link in note_links:
            anchor = link.attrs['href'].split('#')[1]
            if not notes.find(lambda n: n.attrs.get('id') == anchor):
                raise EvalError(f'Missing SEP footnote {anchor}')
        note_body = notes.find(lambda n: n.attrs.get('id') in ('main-text', 'aueditable'))
        if not note_body:
            raise EvalError('Missing SEP notes body')
        selected.append(note_body)
    text = clean('\n\n'.join(html_md(n, url) for n in selected))
    # Text nodes must survive conversion. This catches accidental large omissions.
    stats = {'headings': len(body.all(lambda n: bool(re.fullmatch('h[1-6]', n.tag)))),
             'footnote_links': len(note_links), 'display_math': text.count('\\[')}
    return text, clean(html_md(pub, url)).strip(), stats


def safe_unpack(body, dest):
    kind = 'tar'
    if body.startswith(b'\x1f\x8b'):
        # Bound decompression to defend against gzip bombs.
        with gzip.GzipFile(fileobj=io.BytesIO(body)) as stream:
            body = stream.read(MAX_BYTES + 1)
        if len(body) > MAX_BYTES:
            raise EvalError('Source exceeds decompression limit')
        kind = 'gzip'
    try:
        archive = tarfile.open(fileobj=io.BytesIO(body), mode='r:')
    except tarfile.ReadError:
        if b'\\documentclass' not in body or b'\\begin{document}' not in body:
            raise EvalError('Source is neither tar nor a single TeX document')
        dest.mkdir(parents=True, exist_ok=True)
        (dest / 'main.tex').write_bytes(body)
        return kind + '-single-tex'
    members = archive.getmembers()
    total = 0
    seen = set()
    for member in members:
        path = PurePosixPath(member.name)
        if path.is_absolute() or '..' in path.parts or '\\' in member.name:
            raise EvalError(f'Unsafe archive path: {member.name!r}')
        if not (member.isfile() or member.isdir()):
            raise EvalError(f'Archive link or special file rejected: {member.name!r}')
        if path in seen:
            raise EvalError(f'Duplicate archive path: {member.name!r}')
        seen.add(path)
        total += member.size
        if total > MAX_BYTES or len(members) > 2000:
            raise EvalError('Archive exceeds extraction limits')
    for member in members:
        target = dest / member.name
        if member.isdir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(archive.extractfile(member).read())
    return kind + '-tar'


def uncomment(text):
    return re.sub(r'(?<!\\)%[^\n]*', '', text)


def expand_tex(path, root, seen=None):
    seen = set() if seen is None else seen
    path = path.resolve()
    if not path.is_relative_to(root.resolve()) or path in seen:
        raise EvalError(f'Unsafe or recursive TeX include: {path.name}')
    seen = seen | {path}
    text = uncomment(read(path))
    def include(match):
        p = path.parent / match[1]
        if not p.suffix:
            p = p.with_suffix('.tex')
        if not p.is_file():
            raise EvalError(f'Missing included TeX: {p.name}')
        return expand_tex(p, root, seen)
    return re.sub(r'\\(?:input|include)\s*\{([^}]+)\}', include, text)


def group(text, pos):
    if pos >= len(text) or text[pos] != '{':
        raise EvalError('Malformed TeX group')
    level, start = 1, pos + 1
    pos += 1
    while pos < len(text):
        if text[pos] == '\\':
            pos += 2
            continue
        if text[pos] == '{':
            level += 1
        elif text[pos] == '}':
            level -= 1
            if not level:
                return text[start:pos], pos + 1
        pos += 1
    raise EvalError('Unbalanced TeX braces')


def tex_extract(folder):
    mains = [p for p in folder.rglob('*.tex') if '\\begin{document}' in uncomment(read(p))]
    if len(mains) != 1:
        raise EvalError(f'Expected one main TeX document, found {len(mains)}')
    text = expand_tex(mains[0], folder)
    if '\\end{document}' not in text:
        raise EvalError('Truncated TeX: no end of document')
    preamble, body = text.split('\\begin{document}', 1)
    body = body.split('\\end{document}', 1)[0]
    footnotes = []
    def extract_footnotes(text):
        out, last = [], 0
        while match := re.search(r'\\footnote\s*\{', text[last:]):
            start = last + match.start()
            content, end = group(text, last + match.end() - 1)
            footnotes.append(content)
            out.extend((text[last:start], f'[^{len(footnotes)}]'))
            last = end
        out.append(text[last:])
        return ''.join(out)
    body = extract_footnotes(body)
    equation_count = 0
    def equation(match):
        nonlocal equation_count
        equation_count += 1
        return f'\n\nEquation ({equation_count})\n\n\\[\n{match[1].strip()}\n\\]\n\n'
    body = re.sub(r'\\begin\{equation\}(.*?)\\end\{equation\}', equation, body, flags=re.S)
    section_count = 0
    def section(match):
        nonlocal section_count
        if match[1] == 'section':
            section_count += 1
        return '\n\n' + ('##' if match[1] == 'section' else '###') + ' ' + (f'{section_count}. ' if match[1] == 'section' else '') + match[2] + '\n\n'
    body = re.sub(r'\\(section|subsection)\{([^{}]+)\}', section, body)
    # Keep graphics/algorithms as literal source; do not invent visual graphs.
    body = re.sub(r'(\\begin\{(figure|algorithm)\}.*?\\end\{\2\})',
                  lambda m: '\n\n```latex\n' + m[1].strip() + '\n```\n\n', body, flags=re.S)
    # Formatting commands with nested arguments remain TeX; trivial wrappers can be readable.
    for command, marker in [('emph', '*'), ('textbf', '**'), ('textit', '*')]:
        body = re.sub(r'\\' + command + r'\{([^{}]+)\}', lambda m: marker + m[1] + marker, body)
    body = body.replace('\\maketitle', '').replace('\\begin{abstract}', '## Abstract\n').replace('\\end{abstract}', '')
    body = body.replace('\\printbibliography', '## Bibliography (original bbl data below)')
    notes = '\n\n## Footnotes\n\n' + '\n\n'.join(f'[^{i}]: {n}' for i, n in enumerate(footnotes, 1))
    bbls = sorted(folder.rglob('*.bbl'))
    if not bbls:
        raise EvalError('No compiled bibliography supplied; manual source conversion required')
    appendix = '\n\n## Original macro definitions and typesetting preamble\n\n```latex\n' + preamble.strip() + '\n```\n'
    appendix += '\n## Original bibliography data\n' + ''.join('\n```latex\n' + read(p) + '\n```\n' for p in bbls)
    result = clean('# Functional Decision Theory: A New Theory of Instrumental Rationality\n\n' + body + notes + appendix)
    return result, {'main_tex': str(mains[0].relative_to(folder)), 'equations': equation_count,
                    'footnotes': len(footnotes), 'sections': section_count}, [
        'Conservative Markdown/TeX conversion; macros, cross-reference labels, TikZ diagrams and bibliography markup remain literal TeX. No TeX was executed.',
        'Review original macro appendix to interpret mathematical symbols; graph drawings are retained as source, not rendered images.']


def quality(source_id, text, method):
    if len(text) < 12000 or len(text.split()) < 1500 or '\ufffd' in text:
        raise EvalError('Source is empty, too short, or has encoding replacement characters')
    if source_id == 'fdt':
        if method == 'tex':
            patterns = {
                'equation_4': r'Equation \(4\)\s+\\\[.*?\\\]',
                'observation_indexed_variable': r'.{0,200}\\FDTvar\(\\underline P,\\underline G,\\underline x\).{0,200}',
                'observation_change': r'[^\n]*(?:changing which node|changes the node)[^\n]*',
                'graph_construction': r'[^\n]*not yet clear how to construct[^\n]*largest open problem[^\n]*',
                'policy_footnote_16': r'\[\^16\]:[^\n]+',
                'conclusion': r'## \d+\. Conclusion'}
        else:
            patterns = {
                'equation_4': r'.{0,400}\(4\).{0,400}',
                'observation_indexed_variable': r'.{0,400}fdt\(.{0,100}x.{0,400}',
                'observation_change': r'[^\n]*(?:changing which node|changes the node)[^\n]*',
                'graph_construction': r'.{0,500}open problem.{0,500}',
                'policy_footnote_16': r'16\s+As mentioned earlier.{0,1000}',
                'conclusion': r'Conclusion'}
        passages = {}
        for key, pattern in patterns.items():
            match = re.search(pattern, text, re.S if key == 'equation_4' else 0)
            if not match:
                raise EvalError(f'FDT extraction missing required passage: {key}')
            passages[key] = match[0]
        # Equation's expression must be in the actual equation block, not only macro appendix.
        if method == 'tex':
            block = text.split('Equation (4)', 1)[1].split('\\]', 1)[0]
            if '\\underline x' not in block or '\\Do' not in block:
                raise EvalError('Equation 4 lost observation-indexed intervention')
            if not all(w in passages['policy_footnote_16'] for w in ('policy', 'maps inputs to actions', 'multi-agent')):
                raise EvalError('Footnote 16 lost policy selection content')
        return passages
    required = ['Expected Utility', 'Newcomb', 'Concluding Remarks'] if source_id == 'cdt' else ['3.2', 'Jeffrey', 'desirability', 'Challenges to EU theory']
    for term in required:
        if term not in text:
            raise EvalError(f'{source_id}: missing required coverage {term!r}')
    return {'coverage': ', '.join(required)}


def fetch_one(root, source_id, spec, network, reextract=False):
    base = root / 'data/source_cache' / source_id
    base.mkdir(parents=True, exist_ok=True)
    # Immutable attempt directories: old approved sources are never overwritten.
    prior = sorted(base.glob('*/provenance.json'), reverse=True)
    folder = base / utc().replace(':', '').replace('+', '_')
    folder.mkdir()
    provenance = {'source_id': source_id, 'title': spec['title'], 'extractor': VERSION,
                  'downloads': [], 'warnings': [], 'status': 'failed', 'revision': spec.get('version'),
                  'url': spec.get('url', spec.get('preferred_source_url'))}
    try:
        if not network and not reextract:
            raise EvalError('Network disabled. Use --network or --reextract.')
        def get(url, filename):
            dest = folder / filename
            if reextract:
                found = None
                for previous in prior:
                    old = json.loads(read(previous))
                    for record in old.get('downloads', []):
                        if record['url'] == url:
                            raw = previous.parent / record['raw_file']
                            if raw.is_file() and sha(raw.read_bytes()) == record['raw_sha256']:
                                found = (raw, record)
                                break
                    if found:
                        break
                if not found:
                    raise EvalError(f'No verified cached download for {url}; --reextract never downloads')
                shutil.copyfile(found[0], dest)
                provenance['downloads'].append({**found[1], 'raw_file': filename})
            else:
                provenance['downloads'].append(download(url, dest))
            return dest
        if source_id != 'fdt':
            html = read(get(spec['url'], 'raw.html'))
            notes = None
            if 'notes.html#note-' in html:
                notes = read(get(urljoin(spec['url'], 'notes.html'), 'notes.html'))
            text, revision, stats = sep_extract(html, spec['url'], notes)
            provenance.update(revision=revision, url=spec['url'], method='html', text_statistics=stats,
                              conversion_command='stdlib HTMLParser article + preamble + bibliography + linked notes -> Markdown')
            if source_id == 'edt':
                provenance['warnings'].append('Full Decision Theory entry, especially section 3.2 Jeffrey\'s theory; this is not a dedicated EDT article.')
        else:
            provenance['url'] = spec['preferred_source_url']
            try:
                raw = get(spec['preferred_source_url'], 'source.bin')
                fmt = safe_unpack(raw.read_bytes(), folder / 'tex')
                text, stats, warnings = tex_extract(folder / 'tex')
                provenance.update(method='tex', archive_format=fmt, text_statistics=stats,
                                  conversion_command='safe_unpack -> expand input/include -> conservative Markdown/TeX (no TeX execution)')
                provenance['warnings'].extend(warnings)
                quality(source_id, text, 'tex')
            except (EvalError, OSError, urllib.error.URLError, UnicodeError, tarfile.TarError, EOFError) as error:
                provenance['warnings'].append(f'TeX attempt failed: {error}; trying text PDF (no OCR)')
                pdf = get(spec['pdf_fallback_url'], 'raw.pdf')
                if not pdf.read_bytes().startswith(b'%PDF-'):
                    raise EvalError('Fallback is not a PDF')
                if not shutil.which('pdftotext'):
                    raise EvalError('PDF fallback requires pdftotext -layout; install poppler-utils')
                proc = subprocess.run(['pdftotext', '-layout', str(pdf), str(folder / 'pdf.txt')], capture_output=True, text=True)
                if proc.returncode:
                    raise EvalError('pdftotext failed: ' + proc.stderr)
                text = read(folder / 'pdf.txt')
                if len(text.strip()) < 1000:
                    raise EvalError('PDF appears non-textual. Manual review/OCR required; no OCR performed.')
                provenance.update(method='pdf', conversion_command='pdftotext -layout raw.pdf pdf.txt',
                                  text_statistics={}, url=spec['pdf_fallback_url'])
                provenance['warnings'].append('PDF text has uncertain mathematical glyph/layout fidelity; manual equation approval required.')
        passages = quality(source_id, text, provenance['method'])
        (folder / 'article.md').write_bytes(text.encode('utf-8'))
        provenance.update(normalized_sha256=sha(text), normalized_file='article.md', status='passed_automated_checks',
                          manual_approval=False, extractor_sha256=sha(Path(__file__).read_bytes()))
        provenance['text_statistics'].update(characters=len(text), words=len(text.split()), lines=len(text.splitlines()))
        report = f'# Local source QA — {source_id}\n\nAutomated checks passed; manual source/prompt approval is still required.\n\n'
        report += '\n'.join('- ' + w for w in provenance['warnings']) + '\n\n'
        for label, passage in passages.items():
            report += f'## {label}\n\n```text\n{passage}\n```\n\n'
        (folder / 'qa.md').write_text(report, encoding='utf-8')
        write_json(folder / 'provenance.json', provenance)
        write_json(base / 'current.json', {'directory': folder.name, 'normalized_sha256': sha(text)})
        return provenance, folder
    except Exception as error:
        provenance['error'] = f'{type(error).__name__}: {error}'
        write_json(folder / 'provenance.json', provenance)
        (folder / 'qa.md').write_text('# SOURCE EXTRACTION FAILED\n\n' + provenance['error'] + '\n', encoding='utf-8')
        raise EvalError(f'{source_id}: {provenance["error"]}; diagnostic: {folder / "qa.md"}') from error


def fetch_sources(root, selected, network=False, reextract=False):
    manifest = load_yaml(root / 'sources/manifest.yaml')['sources']
    if network and reextract:
        raise EvalError('Choose either --network or --reextract')
    if not network and not reextract:
        raise EvalError('fetch-sources is offline by default; pass --network to download or --reextract to reprocess verified cached bytes.')
    results, errors = [], []
    for name in selected or manifest:
        if name not in manifest:
            raise EvalError(f'Unknown source: {name}')
        try:
            record, folder = fetch_one(root, name, manifest[name], network, reextract)
            results.append({'source': name, 'status': record['status'], 'directory': str(folder),
                            'normalized_sha256': record['normalized_sha256'], 'warnings': record['warnings']})
        except EvalError as error:
            results.append({'source': name, 'status': 'failed', 'error': str(error)})
            errors.append(str(error))
    write_json(root / 'data/source_cache/report.json', results)
    report = '# Local source extraction report\n\nAutomated checks only; manual article, mathematics and prompt approval remains pending. Full source text and QA excerpts are local-only.\n\n'
    for result in results:
        report += f'## {result["source"]}: {result["status"]}\n\n'
        if 'directory' in result:
            folder = Path(result['directory'])
            meta = json.loads(read(folder / 'provenance.json'))
            report += f'Revision: {meta["revision"]}\n\n'
            report += f'[Full article]({folder / "article.md"}) · [Local QA passages]({folder / "qa.md"}) · [Provenance]({folder / "provenance.json"})\n\n'
            report += f'Normalized SHA-256: `{result["normalized_sha256"]}`\n\n'
            report += '\n'.join('- ' + w for w in result['warnings']) + '\n\n'
        else:
            report += result['error'] + '\n\n'
    (root / 'data/source_cache/report.md').write_text(report, encoding='utf-8')
    if errors:
        raise EvalError('\n'.join(errors))
    return results


def load_source(root, source_id):
    base = root / 'data/source_cache' / source_id
    try:
        current = json.loads(read(base / 'current.json'))
        folder = base / current['directory']
        if folder.parent != base or not folder.is_dir():
            raise EvalError('Invalid source cache pointer')
        info = json.loads(read(folder / 'provenance.json'))
        text = read(folder / 'article.md')
        if info['status'] != 'passed_automated_checks' or sha(text) != info['normalized_sha256'] or sha(text) != current['normalized_sha256']:
            raise EvalError('Source cache hash or QA status mismatch; fetch again')
        quality(source_id, text, info['method'])
        for raw in info['downloads']:
            if sha((folder / raw['raw_file']).read_bytes()) != raw['raw_sha256']:
                raise EvalError('Raw source hash mismatch')
        return text, info
    except (FileNotFoundError, KeyError, json.JSONDecodeError) as error:
        raise EvalError(f'Missing or incomplete source {source_id}; run fetch-sources --network and review QA') from error
