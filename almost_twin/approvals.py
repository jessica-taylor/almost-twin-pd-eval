"""Hash-bound request approvals and optional legacy source acknowledgements."""
import json

from .common import EvalError, append_json, encoded, read, sha, utc
from .sources import load_source, source_identity


def source_scope(identity):
    return {key: identity.get(key) for key in ('source_id', 'source_revision', 'source_permanent_url', 'source_sha256')}


def approval_key(kind, scope):
    return sha(encoded({'kind': kind, 'scope': scope}))


def has_approval(root, kind, scope):
    path = root / 'data/approvals.jsonl'
    key = approval_key(kind, scope)
    if not path.exists():
        return False
    for line in read(path).splitlines():
        record = json.loads(line)
        if record.get('key') == key and record.get('kind') == kind and record.get('scope') == scope:
            return True
    return False


def approve(root, kind, scope, acknowledged=False):
    if has_approval(root, kind, scope):
        return approval_key(kind, scope)
    if kind == 'source_terms' and not acknowledged:
        return None  # Legacy acknowledgement is optional and never gates execution.
    if not acknowledged:
        raise EvalError('These exact requests are not approved. Inspect the rendered Markdown/JSON and cost, then pass --prompts-approved. Any change to messages, model, endpoint, effort or decoding settings requires new approval.')
    key = approval_key(kind, scope)
    append_json(root / 'data/approvals.jsonl', {'utc': utc(), 'kind': kind, 'key': key, 'scope': scope,
                'acknowledgement': 'User acknowledged article transmission rights' if kind == 'source_terms' else 'User approved exact serialized requests'})
    return key


def approve_source(root, source_id, acknowledged=False):
    source, info = load_source(root, source_id)
    identity = source_identity(source_id, source, info)
    approve(root, 'source_terms', source_scope(identity), acknowledged)
    return identity
