"""Deterministic offline publication export; never invokes the generation runner."""
import csv
import hashlib
import io
import json
import os
import re
import shutil
import tempfile
from pathlib import Path, PurePosixPath

from .common import EvalError
from .publication_audit import scan_tree, source_catalog

VERSION = '1'
DEFAULT_STUDIES = ('dt-four-theories-main-qwen-plow-20261108', 'afdt-anthropic-effort-sweep-20261108')
SOURCE_TAG = re.compile(r'(<source_document>)(.*?)(</source_document>)', re.S)
REFERENCE_FILES = ('summary.md', 'summary.json', 'summary.csv', 'pairs.csv', 'decisions.csv',
                   'failures.csv', 'review_summary.md', 'review_summary.json', 'review_samples.csv',
                   'specification.yaml', 'study.json', 'study.sha256', 'events.jsonl', 'plan.md')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encode(obj):
    return (json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=2) + '\n').encode()


def canonical(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()


def relative(name):
    p = PurePosixPath(str(name))
    if p.is_absolute() or '..' in p.parts or '\\' in str(name):
        raise EvalError('Unsafe publication-relative path')
    return p.as_posix()


def pointer(parts):
    return '/' + '/'.join(str(p).replace('~', '~0').replace('/', '~1') for p in parts)


class Exporter:
    def __init__(self, root, destination, study_dirs):
        self.root = Path(root).resolve()
        self.destination = Path(destination).resolve()
        self.study_dirs = sorted(Path(p).resolve() for p in study_dirs)
        if len(set(self.study_dirs)) != len(self.study_dirs):
            raise EvalError('Duplicate study directory')
        self.original_roots = set()
        self.files = {}
        self.inputs = {}
        self.sources = {}
        self.runs = set()
        self.excluded = []
        self.identities = []
        self.stage = None

    def read(self, path):
        original = Path(path)
        p = original.resolve()
        if not p.is_relative_to(self.root) or original.is_symlink():
            raise EvalError('Input is outside the repository or is a symlink')
        data = p.read_bytes()
        key = p.relative_to(self.root).as_posix()
        item = {'path': key, 'sha256': sha(data), 'bytes': len(data)}
        if key in self.inputs and self.inputs[key] != item:
            raise EvalError('Input changed during export: ' + key)
        self.inputs[key] = item
        return data, item

    def load(self, path):
        return json.loads(self.read(path)[0])

    def resolve_saved(self, name):
        p = Path(name)
        if not p.is_absolute():
            return self.root / relative(name)
        for old in sorted(self.original_roots, key=len, reverse=True):
            try:
                return self.root / p.relative_to(old)
            except ValueError:
                continue
        if p.is_relative_to(self.root):
            return p
        raise EvalError('Saved artifact is outside the frozen repository root')

    def public_text(self, text):
        for old in sorted(self.original_roots, key=len, reverse=True):
            text = text.replace(old + '/data/exploratory/runs/', 'runs/')
            text = text.replace(old + '/data/studies/', 'studies/')
            text = text.replace(old + '/', '<LOCAL_REPOSITORY>/')
            if text == old:
                text = '<LOCAL_REPOSITORY>'
        return text

    def scrub(self, obj, parts=()):
        changes = []
        if isinstance(obj, str):
            new = self.public_text(obj)
            if new != obj:
                changes.append({'pointer': pointer(parts), 'operation': 'replace_local_repository_paths',
                                'original_value_sha256': sha(obj.encode()), 'replacement': new})
            return new, changes
        if isinstance(obj, list):
            result = []
            for i, v in enumerate(obj):
                new, ch = self.scrub(v, parts + (i,)); result.append(new); changes.extend(ch)
            return result, changes
        if isinstance(obj, dict):
            result = {}
            for k, v in obj.items():
                new, ch = self.scrub(v, parts + (k,)); result[k] = new; changes.extend(ch)
            return result, changes
        return obj, changes

    def write(self, name, data, sources=(), operations=()):
        name = relative(name)
        desc = {'path': name, 'sha256': sha(data), 'bytes': len(data),
                'evidence': 'verbatim' if len(sources) == 1 and not operations and sources[0]['sha256'] == sha(data) else 'derived',
                'inputs': list(sources), 'operations': list(operations)}
        if name in self.files:
            if self.files[name] != desc:
                raise EvalError('Conflicting output: ' + name)
            return name
        path = self.stage / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        self.files[name] = desc
        return name

    def copy(self, src, name):
        data, origin = self.read(src)
        return self.write(name, data, [origin])

    def metadata(self, src, name):
        raw, origin = self.read(src)
        suffix = Path(src).suffix
        changes = []
        if suffix == '.json':
            obj, changes = self.scrub(json.loads(raw))
            data = encode(obj) if changes else raw
        elif suffix == '.jsonl':
            lines = []
            for i, line in enumerate(raw.decode().splitlines()):
                obj, ch = self.scrub(json.loads(line), (i,))
                changes.extend(ch); lines.append(canonical(obj) + b'\n')
            data = b''.join(lines) if changes else raw
        elif suffix == '.csv':
            reader = csv.DictReader(io.StringIO(raw.decode()))
            rows = []
            for i, row in enumerate(reader):
                obj, ch = self.scrub(row, (i,)); rows.append(obj); changes.extend(ch)
            if changes:
                f = io.StringIO(newline=''); writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
                writer.writeheader(); writer.writerows(rows); data = f.getvalue().encode()
            else:
                data = raw
        else:
            text = raw.decode(); new = self.public_text(text); data = new.encode()
            if new != text:
                changes = [{'operation': 'replace_local_repository_paths', 'original_value_sha256': sha(raw)}]
        if changes:
            changes.append({'operation': 'reserialize_' + suffix.lstrip('.'), 'note': 'Metadata only; model evidence is never passed through this sanitizer.'})
        return self.write(name, data, [origin], changes)

    def frozen(self, path):
        value = self.load(path)
        digest_path = Path(path).with_suffix('.sha256')
        if digest_path.exists() and self.read(digest_path)[0].decode().strip() != sha(self.read(path)[0]):
            raise EvalError('Frozen metadata hash mismatch: ' + str(Path(path).name))
        return value

    def source(self, identity, body=None):
        key = identity['source_id'] + '-' + str(identity['source_revision'])
        public = 'sources/' + re.sub(r'[^A-Za-z0-9_.-]', '-', key)
        if key in self.sources:
            if self.sources[key]['identity'] != identity:
                raise EvalError('Conflicting source identities')
            if body is not None and sha(body.encode()) != identity['source_sha256']:
                raise EvalError('Researcher source body hash mismatch')
            return public
        record = {'identity': identity, 'full_researcher_requests': 'omitted', 'original_provenance_file': 'not bundled; original hash retained'}
        source_id = identity['source_id']
        matching_provenance = [p for p in sorted((self.root/'data/source_cache'/source_id).glob('*/provenance.json'))
                               if sha(p.read_bytes()) == identity['source_provenance_sha256']]
        if matching_provenance:
            self.metadata(matching_provenance[0], public+'/provenance.json')
            record['original_provenance_file'] = public+'/provenance.json'
            record['provenance_note'] = 'Original extraction/download metadata; local paths remapped only if logged in MANIFEST.json. Full downloaded artifacts are not bundled.'
        if source_id.endswith('_wikipedia'):
            candidates = []
            for p in sorted((self.root / 'data/source_cache' / source_id).glob('*/article.md')):
                if sha(p.read_bytes()) == identity['source_sha256']:
                    q = p.parent / 'provenance.json'
                    if q.exists() and sha(q.read_bytes()) == identity['source_provenance_sha256']:
                        candidates.append((p, q))
            if not candidates:
                raise EvalError('Frozen Wikipedia source/provenance not found by hash: ' + source_id)
            article, provenance = candidates[0]
            info = self.load(provenance)
            record.update(attribution=info['attribution'], article_file=public+'/article.md',
                          publication_policy='One exact normalized Wikipedia copy with contributor/revision attribution and CC BY-SA 4.0 notice; source license is not a blanket dataset license.')
            self.copy(article, public+'/article.md')
        elif source_id == 'fdt':
            record.update(tex_source_url='https://arxiv.org/src/1710.05060v2',
                          paper_url='https://arxiv.org/abs/1710.05060v2',
                          pdf_url='https://arxiv.org/pdf/1710.05060v2',
                          title='Functional Decision Theory: A New Theory of Instrumental Rationality',
                          authors=['Eliezer Yudkowsky', 'Nate Soares'],
                          publication_policy='Full paper/TeX/normalized article omitted; link to pinned v2 TeX archive. Model outputs may quote the paper and remain verbatim.')
        else:
            raise EvalError('Unreviewed source for publication: ' + source_id)
        self.sources[key] = record
        self.write(public+'/source.json', encode(record), operations=[{'operation': 'derive_source_descriptor_from_frozen_identity', 'source_body_policy': record['publication_policy']}])
        return public

    def transport(self, path, target):
        if not path.exists():
            return
        raw, src = self.read(path); obj = json.loads(raw)
        headers = {k.lower(): v for k, v in obj.get('headers', {}).items()}
        keep = {k: headers[k] for k in ('date', 'server', 'x-openrouter-release') if k in headers}
        ray = headers.get('cf-ray', '').rsplit('-', 1)[-1]
        public = {'status': obj.get('status'), 'headers': keep}
        if re.fullmatch('[A-Z]{3}', ray):
            public['ingress_location'] = ray
        self.write(target, encode(public), [src], [{'operation': 'whitelist_transport_metadata',
                    'retained_headers': sorted(keep), 'omitted_headers': sorted(set(headers)-set(keep)),
                    'cf_ray_policy': 'Only three-letter ingress suffix retained; full trace ID omitted.',
                    'reason': 'Exclude response cookies and unnecessary connection/browser identifiers. Header names normalized to lowercase.'}])

    def call(self, run, name, stage, identity, accepted_essay=None):
        d = run / name
        if not (d / 'request.json').exists():
            if (d / 'response.raw').exists():
                raise EvalError('Response exists without saved request')
            return None
        target = 'runs/' + run.name + '/' + name
        reqraw, reqsrc = self.read(d / 'request.json'); req = json.loads(reqraw)
        if stage == 'researcher':
            # Match exactly the normalized source, with only the renderer's
            # leading/trailing delimiter newlines removed.
            msg = req['messages']
            if len(msg) != 1 or msg[0]['role'] != 'user':
                raise EvalError('Unexpected researcher message structure')
            original_content = msg[0]['content']
            matches = list(SOURCE_TAG.finditer(original_content))
            if len(matches) != 1:
                raise EvalError('Researcher source block missing or repeated')
            m = matches[0]; body = m[2]
            candidates = [body, body.removeprefix('\n'), body.removesuffix('\n'), body.removeprefix('\n').removesuffix('\n')]
            source = next((s for s in candidates if sha(s.encode()) == identity['source_sha256']), None)
            if source is None:
                raise EvalError('Researcher article does not match frozen normalized source hash')
            descriptor = self.source(identity, source)
            marker = '\n[SOURCE BODY OMITTED FROM PUBLICATION: '+descriptor+'/source.json; normalized SHA-256 '+identity['source_sha256']+']\n'
            req['messages'][0]['content'] = original_content[:m.start(2)] + marker + original_content[m.end(2):]
            request_path = self.write(target+'/request.source_omitted.json', encode(req), [reqsrc],
                [{'operation': 'omit_full_source_body', 'pointer': '/messages/0/content',
                  'span_utf8_bytes': [len(original_content[:m.start(2)].encode()), len(original_content[:m.end(2)].encode())],
                  'omitted_sha256': sha(body.encode()), 'normalized_source_sha256': identity['source_sha256'],
                  'replacement': marker, 'note': 'Derivative input view, NOT the exact request; all other fields retained; JSON reserialized.'}])
        else:
            request_path = self.write(target+'/request.json', reqraw, [reqsrc])
            if stage == 'prisoner' and accepted_essay is not None:
                if len(req['messages']) != 1 or accepted_essay not in req['messages'][0]['content']:
                    raise EvalError('Prisoner request does not contain frozen essay verbatim')
        record = {'stage': stage, 'call': name, 'run_id': run.name, 'request': request_path,
                  'original_request_sha256': reqsrc['sha256'], 'request_is_exact': stage != 'researcher',
                  'response': None, 'output': None, 'transport': None}
        if (d/'response.raw').exists():
            record['response'] = self.copy(d/'response.raw', target+'/response.raw')
            response = self.load(d/'response.raw')
            content = ((response.get('choices') or [{}])[0].get('message') or {}).get('content')
            if (d/'output.txt').exists():
                data, origin = self.read(d/'output.txt')
                if not isinstance(content, str) or data != content.encode():
                    raise EvalError('Visible output disagrees with raw response')
                record['output'] = self.write(target+'/output.txt', data, [origin])
        self.transport(d/'transport.json', target+'/transport.public.json')
        if (self.stage/target/'transport.public.json').exists():
            record['transport'] = target+'/transport.public.json'
        return record

    def run_files(self, run):
        if run.name in self.runs:
            return
        self.runs.add(run.name)
        for name in ('plan.json', 'essay.json', 'failure.json', 'outcome.json', 'adjudicated_outcome.json'):
            if (run/name).exists():
                self.metadata(run/name, 'runs/'+run.name+'/'+name)
        if (run/'essay.md').exists():
            self.copy(run/'essay.md', 'runs/'+run.name+'/essay.md')

    def transcript(self, rec):
        base = rec['publication_path']
        rel = lambda dest: os.path.relpath(dest, base).replace(os.sep, '/')
        def fence(t):
            delim = '`' * max(3, 1+max((len(x) for x in re.findall(r'`+', t)), default=0))
            return delim+'text\n'+t+('' if t.endswith('\n') else '\n')+delim+'\n'
        lines = [f'# {rec["cell_id"]} / {rec["sample_index"]:05d}', '',
                 f'Status: **{rec["status"]}**. Saved outcome: **{rec.get("pair_outcome") or "unscored"}**.', '',
                 'Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.', '']
        titles = {'researcher': 'Researcher', 'prisoner': 'Prisoner', 'judge': 'Judge'}
        for c in rec['calls']:
            lines += [f'## {titles[c["stage"]]} / {c["call"]}', '',
                      f'[Saved input{ " (source body explicitly omitted)" if not c["request_is_exact"] else " (exact bytes)"}]({rel(c["request"])})', '']
            if not c['response']:
                lines += ['**No response saved; outcome/usage unknown. No replacement response inferred.**', '']; continue
            raw = json.loads((self.stage/c['response']).read_bytes()); choice = (raw.get('choices') or [{}])[0]; msg = choice.get('message') or {}
            lines += [f'[Authoritative raw response]({rel(c["response"])}) · finish: `{choice.get("finish_reason")}`', '', '### Visible response', '']
            text = msg.get('content')
            if isinstance(text, str):
                lines += [fence(text)]
            else:
                lines += ['No text returned.', '']
            reasoning = msg.get('reasoning')
            origin = 'message.reasoning'
            if not isinstance(reasoning, str):
                reasoning = msg.get('reasoning_content'); origin = 'message.reasoning_content'
            if not isinstance(reasoning, str):
                blocks = []
                for d in msg.get('reasoning_details') or []:
                    if d.get('type') == 'reasoning.summary' and isinstance(d.get('summary'), str):
                        blocks.append(d['summary'])
                    elif d.get('type') == 'reasoning.text' and isinstance(d.get('text'), str):
                        blocks.append(d['text'])
                reasoning = '\n\n'.join(blocks) if blocks else None
                origin = 'readable reasoning_details blocks joined in saved order'
            lines += ['### Available readable reasoning', '']
            lines += [f'Extraction: {origin}.', '', fence(reasoning)] if reasoning is not None else ['No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.', '']
        if not rec['calls']:
            lines += ['No model calls were attempted for this prepared scenario.', '']
        return '\n'.join(lines).encode()

    def study(self, folder):
        study = self.frozen(folder/'study.json')
        self.original_roots.add(study['repo_root'])
        name = relative(folder.name); base = 'studies/'+name
        self.identities.append({'name': name, 'study_id': study['study_id'], 'spec_sha256': study['spec_sha256']})
        if sha(self.read(folder/'specification.yaml')[0]) != study['spec_sha256']:
            raise EvalError('Frozen specification hash mismatch')
        for n in REFERENCE_FILES:
            if (folder/n).exists():
                self.metadata(folder/n, base+'/reference/'+('study.original.sha256' if n == 'study.sha256' else n))
        rows = list(csv.DictReader(io.StringIO(self.read(folder/'pairs.csv')[0].decode())))
        by_id = {r['sample_id']: r for r in rows}
        if len(by_id) != len(rows):
            raise EvalError('Duplicate sample IDs')
        records = []
        for cell in study['cells']:
            cellpath = relative(cell['path']); batch = folder/cellpath
            meta = self.frozen(batch/'batch.json')
            if (batch/'events.jsonl').exists():
                self.metadata(batch/'events.jsonl', base+'/'+cellpath+'/events.jsonl')
            for entry in meta['samples']:
                sample = batch/relative(entry['path']); pilot = self.frozen(sample/'pilot.json')
                r = by_id[entry['sample_id']]; state = self.load(sample/'state.json')
                identity = pilot['source_identity']; source = self.source(identity)
                public = base+'/'+cellpath+'/'+relative(entry['path'])
                for n in ('pilot.json', 'state.json', 'sample_state.json', 'batch_sample.json'):
                    if (sample/n).exists():
                        self.metadata(sample/n, public+'/'+n)
                rec = {'schema_version': 1, 'study': name, 'cell_id': cell['id'], 'sample_id': entry['sample_id'],
                       'sample_index': entry['index'], 'status': r['status'], 'pair_outcome': r['pair_outcome'] or None,
                       'model': cell['model'], 'assignment': cell['assignment'],
                       'researcher_effort': cell['researcher_effort'], 'prisoner_effort': cell['prisoner_effort'],
                       'source': source+'/source.json', 'source_identity': identity, 'settings': pilot['settings'],
                       'template_hashes': pilot['template_hashes'], 'publication_path': public,
                       'essay_sha256': r.get('essay_sha256') or None, 'essay': None, 'calls': [],
                       'classification': None, 'adjudication': None, 'row': self.scrub(r)[0]}
                essay = None
                if r.get('researcher_run'):
                    run = self.resolve_saved(r['researcher_run'])
                    if (run/'essay.md').exists():
                        essay = self.read(run/'essay.md')[0]
                        if sha(essay) != r['essay_sha256'] or state.get('essay_sha256') != r['essay_sha256']:
                            raise EvalError('Frozen essay hash mismatch')
                        essay = essay.decode(); rec['essay'] = 'runs/'+run.name+'/essay.md'
                for st, key, names in [('researcher', 'researcher_run', ('call_0',)), ('prisoner', 'prisoner_run', ('call_0', 'call_1')), ('judge', 'judge_run', ('call_a', 'call_b'))]:
                    if not r.get(key):
                        continue
                    run = self.resolve_saved(r[key]); self.run_files(run)
                    for call in names:
                        exported = self.call(run, call, st, identity, essay)
                        if exported:
                            rec['calls'].append(exported)
                    if st == 'prisoner' and (run/'outcome.json').exists():
                        rec['classification'] = 'runs/'+run.name+'/outcome.json'
                    if st == 'judge' and (run/'adjudicated_outcome.json').exists():
                        rec['adjudication'] = 'runs/'+run.name+'/adjudicated_outcome.json'
                srcs = [self.inputs[str((sample/'state.json').relative_to(self.root))], self.inputs[str((sample/'pilot.json').relative_to(self.root))], self.inputs[str((folder/'pairs.csv').relative_to(self.root))]]
                self.write(public+'/record.json', encode(rec), srcs, [{'operation': 'assemble_scenario_record', 'note': 'Reported classification retained; independently checked by scripts/verify_publication.py.'}])
                self.write(public+'/transcript.md', self.transcript(rec), operations=[{'operation': 'render_transcript_from_raw_responses', 'record': public+'/record.json', 'note': 'Complete visible content preserved inside dynamically sized fences. Reasoning precedence: reasoning, reasoning_content, then readable summary/text details. Encrypted blocks never decoded. Wrapper adds a separator newline if absent in original.'}])
                records.append({'sample_id': rec['sample_id'], 'cell_id': cell['id'], 'sample_index': rec['sample_index'], 'record': public+'/record.json', 'transcript': public+'/transcript.md'})
        if len(records) != len(rows):
            raise EvalError('Frozen scenario roster differs from pairs.csv')
        self.write(base+'/index.json', encode(records), operations=[{'operation': 'derive_index_from_all_frozen_scenarios'}])
        lines = ['# '+name, '', '[Frozen source summary](reference/summary.md) · [Machine-readable index](index.json)', '', '| Cell | Sample | Status | Outcome | Transcript |', '|---|---:|---|---|---|']
        for x in records:
            r = by_id[x['sample_id']]
            lines.append(f'| {x["cell_id"]} | {x["sample_index"]:05d} | {r["status"]} | {r["pair_outcome"] or "unscored"} | [Read]({os.path.relpath(x["transcript"], base)}) |')
        self.write(base+'/README.md', ('\n'.join(lines)+'\n').encode(), operations=[{'operation': 'render_study_index'}])

    def export(self):
        for folder in self.study_dirs:
            if not folder.is_relative_to(self.root) or self.destination == folder or self.destination.is_relative_to(folder):
                raise EvalError('Study/output location is unsafe')
        if self.destination.is_relative_to(self.root/'data'):
            raise EvalError('Publication must be outside private data/')
        self.destination.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix='.publication-', dir=self.destination.parent) as tmp:
            self.stage = Path(tmp)/'export'; self.stage.mkdir()
            for p in self.study_dirs:
                self.study(p)
            self.write('README.md', self.readme().encode(), operations=[{'operation': 'render_publication_index_and_policy'}])
            code = {p: sha((self.root/p).read_bytes()) for p in ('almost_twin/publication.py', 'almost_twin/publication_audit.py', 'scripts/verify_publication.py') if (self.root/p).exists()}
            manifest = {'schema_version': 1, 'exporter_version': VERSION, 'code_sha256': code,
                        'studies': self.identities, 'files': [self.files[k] for k in sorted(self.files)],
                        'input_files': [self.inputs[k] for k in sorted(self.inputs)],
                        'omission_policy': {'researcher_requests': 'Full original request bytes never bundled; explicit source-omitted derivative plus original SHA-256 and span ledger supplied.',
                            'source_text': 'Wikipedia copied once with attribution; FDT paper/TeX replaced by pinned source links. Existing model quotations are not rewritten.',
                            'transport': 'Cookies and full connection trace headers excluded; whitelisted derived metadata retained.',
                            'operational_duplicates': 'Duplicate rendered prompts, caches, capability snapshots, locks, local approval/budget journals, and redundant plaintext transcript formats not copied.',
                            'paths': 'Only metadata paths are remapped to portable logical paths; every changed JSON pointer/CSV field is logged. Raw responses, outputs, essays and prisoner/judge request bytes are never sanitized.'}}
            (self.stage/'MANIFEST.json').write_bytes(encode(manifest))
            scan = scan_tree(self.stage, source_catalog(self.root), allow_wikipedia=True)
            if scan['blocking_findings']:
                # Location/kind/hashes only; do not expose matched values.
                raise EvalError('Publication scan blocked export: '+json.dumps(scan['findings'][:10]))
            (self.stage/'SCAN.json').write_bytes(encode(scan))
            if self.destination.exists():
                old = {p.relative_to(self.destination).as_posix(): sha(p.read_bytes()) for p in self.destination.rglob('*') if p.is_file()}
                new = {p.relative_to(self.stage).as_posix(): sha(p.read_bytes()) for p in self.stage.rglob('*') if p.is_file()}
                if old != new:
                    raise EvalError('Existing export differs; choose a new --out directory. Nothing overwritten.')
            else:
                os.replace(self.stage, self.destination)
        return self.destination

    def readme(self):
        links = '\n'.join('- ['+x['name']+'](studies/'+x['name']+'/README.md)' for x in self.identities)
        return '''# Curated Almost-Twin study data

This is an offline export of frozen experimental artifacts, including failures and prepared/unexecuted scenarios. No model generations, retries or recoding were performed.

'''+links+'''

## Browse scenarios

Each study index lists every planned scenario, including failures and unexecuted records. Follow **Read** for the complete returned outputs and available readable reasoning. The adjacent `record.json` links structured metadata and run artifacts; each study's `reference/` directory contains its saved summaries, pair/decision CSVs, failures and frozen specification. Large JSON files are best inspected in a local checkout.

For context, see the repository [research overview](../README.md), [methods/results links](../README.md#studies-and-results), and [offline reproducibility guide](../docs/reproducibility.md).

## Evidence and transformations

- `runs/*/call_*/response.raw`, visible `output.txt`, accepted `essay.md`, and prisoner/judge `request.json` preserve original bytes. Their original file hashes are in `MANIFEST.json`.
- Researcher `request.source_omitted.json` is explicitly a DERIVATIVE VIEW, not the original request: only the `<source_document>` body is replaced by an omission marker. Original request/body hashes and byte spans are logged. Other request fields and instructions are retained; JSON is reserialized.
- Wikipedia reference text is supplied once under `sources/`, with original attribution and CC BY-SA 4.0 conversion notices. This license does not automatically apply to the rest of the dataset. Third-party material/media may have separate rights; no external media bytes are bundled.
- The FDT paper and TeX are NOT redistributed. Download its pinned v2 source archive at https://arxiv.org/src/1710.05060v2 ; paper/version information: https://arxiv.org/abs/1710.05060v2 . The frozen normalized text hash is recorded. Model-generated essays may quote the source; those outputs have not been edited.
- Local filesystem roots are removed from metadata only. `MANIFEST.json` lists each changed field, the original value's hash and its portable replacement. Reference summaries retain classifications/counts/costs; their path strings may differ from local originals. Original-file hashes also preserve provenance for source-omitted inputs and metadata views.
- Transport views retain HTTP status, date, server, API-release header and ingress suffix when available. Cookies and full trace IDs are omitted. No credentials, budget/approval journals, environment files or complete cache trees are bundled; the explicitly attributed Wikipedia articles and source-provenance records are the selected cache exceptions.
- Provider-encrypted reasoning remains verbatim in raw JSON. Its hidden content cannot be scanned without decryption; no attempt to decrypt or reconstruct it was made.
- Readable transcripts are derived navigation views, not substitutes for raw JSON. They show complete returned content and available readable reasoning. Reasoning may itself be a provider summary; encrypted reasoning is preserved only in raw JSON, never decoded. Missing output is labeled missing, never reconstructed.
- Post-hoc judge classifications remain distinct from the original irreversible simulated commitments. Failure and refusal are never converted to defection/cooperation. Prepared scenarios have no invented calls.

## Verification

From the repository root, run `python3 scripts/verify_publication.py published`. With private original artifacts available, add `--source-root .` to check every retained/omitted input hash too. Verification reads no credentials and makes no network requests.

`MANIFEST.json` records all payload hashes and derivations; `SCAN.json` contains a deterministic pattern/signature scan. These two generated reports do not list their own hashes. A scan is not proof that every possible secret or source quotation was recognized.

## Redistribution terms

Project-authored research material and the contributors' rights in these records are offered under **CC BY 4.0**, with the explicit third-party exceptions in [DATA_LICENSE.md](../DATA_LICENSE.md). Bundled Wikipedia material retains **CC BY-SA 4.0** and its contributor/revision/conversion notices. Model outputs remain verbatim and may contain source quotations or adaptations; no blanket license or rights clearance is asserted for third-party content. The software is separately [MIT licensed](../LICENSE). See the [publication policy](../docs/publication.md) for excluded copyrighted source texts and every transformation category.
'''


def export_publication(root, out, studies=None):
    root = Path(root).resolve()
    out = Path(out) if Path(out).is_absolute() else root / out
    paths = [root/'data/studies'/s for s in DEFAULT_STUDIES] if not studies else [Path(p) if Path(p).is_absolute() else root/p for p in studies]
    return Exporter(root, out, paths).export()
