import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml


class EvalError(ValueError):
    """A visible validation failure; never an experimental success."""


class GenerationError(EvalError):
    """A failed generation with an auditable, machine-readable cause."""

    def __init__(self, category, message):
        super().__init__(message)
        self.category = category


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha(value):
    if isinstance(value, str):
        value = value.encode('utf-8')
    return hashlib.sha256(value).hexdigest()


def encoded(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')


def read(path):
    # Preserve newlines verbatim, including a model's CRLF output.
    return Path(path).read_bytes().decode('utf-8')


def load_yaml(path):
    return yaml.safe_load(read(path))


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    # A concurrent batch status export must never see half a freshly written
    # state file. Replace the complete JSON atomically on the same filesystem.
    import os
    import tempfile
    payload = json.dumps(value, ensure_ascii=False, indent=2).encode('utf-8') + b'\n'
    name = None
    try:
        with tempfile.NamedTemporaryFile(prefix=f'.{path.name}.', suffix='.tmp',
                                         dir=path.parent, delete=False) as stream:
            name = stream.name
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
    finally:
        if name is not None and os.path.exists(name):
            os.unlink(name)


def append_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('ab') as stream:
        stream.write(encoded(value) + b'\n')
        stream.flush()
        import os
        os.fsync(stream.fileno())

