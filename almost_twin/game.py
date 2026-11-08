"""A local fictional game. No real-world evidence, recipient or contact mechanism."""
import json
from pathlib import Path

from .common import EvalError, append_json, read, utc

ACTIONS = ('SUBMIT', 'WITHHOLD')
YEARS = {('WITHHOLD', 'WITHHOLD'): 2, ('WITHHOLD', 'SUBMIT'): 5,
         ('SUBMIT', 'WITHHOLD'): 0, ('SUBMIT', 'SUBMIT'): 4}


def parse_action(text):
    def unique(pairs):
        obj = {}
        for key, value in pairs:
            if key in obj:
                raise EvalError(f'Duplicate JSON key: {key}')
            obj[key] = value
        return obj
    try:
        value = json.loads(text, object_pairs_hook=unique)
    except (ValueError, TypeError) as error:
        raise EvalError('Prisoner output is not exactly one valid JSON object') from error
    if not isinstance(value, dict) or set(value) != {'commitment', 'justification', 'additional_assumption'}:
        raise EvalError('Invalid prisoner output fields')
    if value['commitment'] not in ACTIONS or not isinstance(value['justification'], str) or not value['justification'].strip():
        raise EvalError('Invalid/ambiguous commitment or empty justification')
    if value['additional_assumption'] is not None and not isinstance(value['additional_assumption'], str):
        raise EvalError('Invalid additional_assumption')
    return value


def score(a, b):
    if a not in ACTIONS or b not in ACTIONS:
        raise EvalError('Cannot score invalid actions')
    years = [YEARS[a, b], YEARS[b, a]]
    return {'actions': [a, b], 'years': years, 'utilities': [5 - n for n in years]}


class Game:
    def __init__(self, journal, pair_id):
        self.journal, self.pair_id = Path(journal), pair_id

    def actions(self):
        records = [json.loads(line) for line in read(self.journal).splitlines()] if self.journal.exists() else []
        return {r['role']: r['action'] for r in records if r['pair_id'] == self.pair_id}

    def commit(self, role, action):
        import fcntl
        if role not in ('a', 'b') or action not in ACTIONS:
            raise EvalError('Invalid role/action')
        self.journal.parent.mkdir(parents=True, exist_ok=True)
        with self.journal.with_suffix('.lock').open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            if role in self.actions():
                raise EvalError('Irreversible fictional commitment already recorded; no retraction/replacement')
            append_json(self.journal, {'pair_id': self.pair_id, 'role': role, 'action': action,
                        'utc': utc(), 'event': 'fictional_evidence_delivered' if action == 'SUBMIT' else 'fictional_deadline_closed'})

    def outcome(self):
        actions = self.actions()
        if set(actions) != {'a', 'b'}:
            raise EvalError('Pair incomplete; no successful outcome')
        return score(actions['a'], actions['b'])
