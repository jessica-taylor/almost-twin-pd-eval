import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml


class EvalError(ValueError):
    """A visible validation failure; never an experimental success."""


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
    path.write_bytes(json.dumps(value, ensure_ascii=False, indent=2).encode('utf-8') + b'\n')


def append_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('ab') as stream:
        stream.write(encoded(value) + b'\n')
        stream.flush()
        import os
        os.fsync(stream.fileno())
