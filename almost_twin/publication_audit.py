"""Offline, value-suppressing publication scans (heuristics, not legal clearance)."""
import argparse
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

VERSION = '1'
# Deliberately avoid generic high-entropy detection: hashes, generation IDs and
# provider-encrypted reasoning are experimental data, not API credentials.
PATTERNS = {
    'provider_api_key': re.compile(rb'\bsk-(?:or-v1-|proj-|ant-api\d{2}-)?[A-Za-z0-9_-]{24,}'),
    'github_token': re.compile(rb'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,})'),
    'aws_access_key': re.compile(rb'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b'),
    'private_key': re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    'slack_token': re.compile(rb'\bxox[baprs]-[A-Za-z0-9-]{20,}'),
    'google_api_key': re.compile(rb'\bAIza[0-9A-Za-z_-]{35}\b'),
    'gitlab_token': re.compile(rb'\bglpat-[A-Za-z0-9_-]{20,}'),
    'huggingface_token': re.compile(rb'\bhf_[A-Za-z0-9]{30,}'),
    'embedded_url_password': re.compile(rb'https?://[^\s/:@]+:[^\s/@]+@'),
    'quoted_secret_assignment': re.compile(rb'''(?i)\b[A-Za-z_]*(?:api_key|access_token|client_secret|password)[A-Za-z_]*["']?\s*[:=]\s*["'][A-Za-z0-9_/+=.-]{16,}["']'''),
    'environment_secret_literal': re.compile(rb'(?m)^[A-Z_]*(?:API_KEY|ACCESS_TOKEN|CLIENT_SECRET|PASSWORD)[A-Z_]*=[A-Za-z0-9_/+=.-]{16,}$'),
    'literal_bearer': re.compile(rb'(?i)\bBearer\s+[A-Za-z0-9_-]{24,}'),
    'local_home_path': re.compile(rb'(?:/home/|/Users/|[A-Z]:\\Users\\)[A-Za-z0-9_.-]+'),
    'workstation_prompt': re.compile(rb'\b[A-Za-z0-9_.-]+@(?:LAPTOP|DESKTOP)-[A-Za-z0-9_-]+'),
    'email_address': re.compile(rb'\b[A-Za-z0-9_.+%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'),
    'cookie_value': re.compile(rb'(?i)["\']set-cookie["\']\s*:\s*["\'][^"\']{8,}'),
}
BLOCKING = set(PATTERNS)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def source_catalog(root):
    """Only hashes/anchors escape; full source text remains local."""
    result = []
    for p in sorted((Path(root) / 'data/source_cache').glob('**/article.md')):
        raw = p.read_bytes()
        if len(raw) < 2000:
            continue
        words = b' '.join(raw.split())
        anchors = [words[int((len(words)-180)*i/7):int((len(words)-180)*i/7)+180] for i in range(8)]
        result.append({'source_id': p.relative_to(Path(root) / 'data/source_cache').parts[0],
                       'sha256': digest(raw), 'raw': raw, 'anchors': anchors})
    return result


def findings(data, location, catalog=(), allow_wikipedia=False):
    result = []
    for kind, regex in PATTERNS.items():
        for m in regex.finditer(data):
            # Never return the matched credential/address/path itself.
            result.append({'kind': kind, 'location': location,
                           'line': data[:m.start()].count(b'\n') + 1,
                           'value_sha256': digest(m.group()),
                           'blocking': kind in BLOCKING})
    # Decode JSON escapes for embedded full source documents in old requests.
    texts = [data]
    try:
        obj = json.loads(data)
        def strings(x):
            if isinstance(x, str):
                yield x.encode()
            elif isinstance(x, dict):
                for v in x.values():
                    yield from strings(v)
            elif isinstance(x, list):
                for v in x:
                    yield from strings(v)
        texts.extend(s for s in strings(obj) if len(s) > 2000)
    except (ValueError, UnicodeError):
        pass
    detected = set()
    normalized_texts = [(text, b' '.join(text.split())) for text in texts]
    for source in catalog:
        if allow_wikipedia and source['source_id'].endswith('_wikipedia'):
            continue
        for text, normalized in normalized_texts:
            full = source['raw'] in text
            near = len(normalized) >= len(source['raw']) * .8 and sum(a in normalized for a in source['anchors']) >= 6
            if full or near:
                detected.add((source['source_id'], source['sha256']))
                break
    for source_id, h in sorted(detected):
        result.append({'kind': 'full_reference_article', 'location': location,
                       'source_id': source_id, 'source_sha256': h, 'blocking': True})
    return result


def scan_tree(folder, catalog=(), allow_wikipedia=False):
    folder = Path(folder)
    out = []
    paths = sorted(p for p in folder.rglob('*') if p.is_file())
    for p in paths:
        name = p.relative_to(folder).as_posix()
        out.extend(findings(p.read_bytes(), name, catalog, allow_wikipedia and name.startswith('sources/')))
    return {'schema_version': 1, 'scanner_version': VERSION, 'files_scanned': len(paths),
            'patterns': sorted(PATTERNS), 'findings': out,
            'blocking_findings': sum(f['blocking'] for f in out),
            'limitations': 'Pattern/signature scan, not proof that all secrets or third-party quotations were identified. Public-source email addresses require contextual review; fictional game observations are intentional evidence.'}


def audit_repository(root, history=True, include_untracked=False):
    root = Path(root)
    def git(*args):
        return subprocess.check_output(['git', '-C', str(root), *args])
    catalog = source_catalog(root)
    tracked = git('ls-files', '-z').decode().split('\0')
    names_to_scan = sorted(set(tracked) | (set(git('ls-files', '--others', '--exclude-standard', '-z').decode().split('\0')) if include_untracked else set()))
    current = []
    for name in names_to_scan:
        if name and (root / name).is_file():
            current.extend(findings((root / name).read_bytes(), name, catalog,
                                    allow_wikipedia=name.startswith('published/sources/')))
    result = {'schema_version': 1, 'scanner_version': VERSION,
              'audited_head': git('rev-parse', 'HEAD').decode().strip(),
              'tracked_files': len([n for n in tracked if n]), 'current_findings': current,
              'worktree_files_scanned': len([n for n in names_to_scan if n]),
              'history_scope': 'All local refs and reflogs; no remote fetch, no history rewriting.',
              'source_signatures': [{'source_id': c['source_id'], 'sha256': c['sha256']} for c in catalog],
              'history_findings': [], 'limitations': 'Heuristic credential/privacy patterns and locally available full-article signatures. Does not audit unseen remote refs, server-side logs, unknown credentials, or quotation rights.'}
    if history:
        objects = git('rev-list', '--objects', '--all', '--reflog').decode().splitlines()
        names = {}
        for line in objects:
            oid, _, name = line.partition(' ')
            names.setdefault(oid, name)
        proc = subprocess.Popen(['git', '-C', str(root), 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        nblobs = 0
        nmessages = 0
        binary_blobs = []
        try:
            for oid, name in names.items():
                proc.stdin.write((oid+'\n').encode()); proc.stdin.flush()
                header = proc.stdout.readline().decode().split()
                size = int(header[2]); data = proc.stdout.read(size); assert proc.stdout.read(1) == b'\n'
                if header[1] in ('commit', 'tag'):
                    nmessages += 1
                    fs = findings(data.partition(b'\n\n')[2], '('+header[1]+' message)', catalog)
                    result['history_findings'].extend(dict(f, object=oid) for f in fs)
                    continue
                if header[1] != 'blob':
                    continue
                nblobs += 1
                try:
                    data.decode('utf-8')
                except UnicodeError:
                    binary_blobs.append({'blob': oid, 'path': name, 'bytes': size})
                fs = findings(data, name or '(unnamed historical blob)', catalog,
                              allow_wikipedia=name.startswith('published/sources/'))
                result['history_findings'].extend(dict(f, blob=oid) for f in fs)
        finally:
            proc.stdin.close(); proc.stdout.close(); proc.wait()
        result['history_blobs_scanned'] = nblobs
        result['history_commit_tag_messages_scanned'] = nmessages
        result['binary_blobs_requiring_separate_review'] = binary_blobs
        # Commit identities are intentional Git metadata; record hashes rather
        # than copying personal addresses into a new publication artifact.
        identities = git('log', '--all', '--reflog', '--format=%an%x09%ae%x09%cn%x09%ce').decode().splitlines()
        emails = set(); identity_hashes = set()
        for line in identities:
            parts = line.split('\t')
            if len(parts) == 4:
                emails.update([parts[1], parts[3]])
                identity_hashes.add(digest(line.encode()))
        result['commit_identity_review'] = {'unique_email_addresses': len(emails),
              'github_noreply_addresses': sum(e.endswith('users.noreply.github.com') for e in emails),
              'email_sha256': sorted(digest(e.encode()) for e in emails),
              'note': 'Git author/committer identities remain in history; no identity rewriting was performed.'}
    remotes = subprocess.run(['git', '-C', str(root), 'config', '--get-regexp', r'^remote\..*\.url$'], capture_output=True, check=False)
    result['remote_configuration_review'] = []
    for line in remotes.stdout.decode().splitlines():
        key, _, url = line.partition(' ')
        parsed = urlsplit(url)
        embedded = parsed.scheme in ('http', 'https') and (parsed.username is not None or parsed.password is not None)
        result['remote_configuration_review'].append({'config_key': key, 'url_sha256': digest(url.encode()),
                'embedded_http_credentials_or_userinfo': embedded,
                'credential_pattern_matches': len([f for f in findings(url.encode(), key) if f['kind'] not in ('email_address',)])})
    result['current_counts'] = dict(Counter(f['kind'] for f in current))
    result['history_counts'] = dict(Counter(f['kind'] for f in result['history_findings']))
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', type=Path, default=Path.cwd())
    p.add_argument('--tree', type=Path)
    p.add_argument('--include-untracked', action='store_true', help='Also scan nonignored prospective additions, without staging them')
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    report = scan_tree(args.tree, source_catalog(args.root), True) if args.tree else audit_repository(args.root, include_untracked=args.include_untracked)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, sort_keys=True, indent=2)+'\n')
    print(json.dumps({k: report[k] for k in ('audited_head', 'tracked_files', 'history_blobs_scanned', 'current_counts', 'history_counts', 'blocking_findings') if k in report}, indent=2))


if __name__ == '__main__':
    main()
