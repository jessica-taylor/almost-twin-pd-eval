"""Versioned, offline interpretation of *existing* judge labels.

This is deliberately outside the frozen generation-code hash list. It never
relabels an action or a score: an unambiguous nonaction remains unscored, but
it should not be mistaken for an ambiguity that needs a human adjudicator.
"""

SCHEMA_VERSION = 1
RESOLVED_NONACTION = 'resolved_nonaction'
RULE_ID = 'judge_other_no_no_review_v1'


def disposition(row):
    """Return a conservative *derived* review status, retaining the raw one.

    `OTHER` + `NO` + an explicit false human-review flag means that the judge
    confidently found no game action. This includes refusals, but the current
    judge schema cannot distinguish a refusal from another clear non-decision.
    Do not heuristically parse its free-text explanation or model output.
    """
    original = row.get('status')
    result = {'schema_version': SCHEMA_VERSION, 'raw_status': original,
              'review_status': original, 'nonaction_roles': [],
              'human_review_required': True if original == 'needs_human_review' else
                                       False if original == 'complete' else None,
              'rule': 'raw_status_unchanged', 'judge_reasons': {}}
    if original != 'needs_human_review':
        return result

    judged = row.get('judge_outcome')
    if (not isinstance(judged, dict) or judged.get('needs_human_review') != [] or
            row.get('needs_human_review') != []):
        return result
    actions = judged.get('adjudicated_actions')
    intents = judged.get('intents')
    disclosures = judged.get('disclosures')
    labels = judged.get('judgements')
    if not (isinstance(actions, list) and len(actions) == 2 and
            isinstance(intents, list) and len(intents) == 2 and
            isinstance(disclosures, list) and len(disclosures) == 2 and
            isinstance(labels, dict)):
        return result

    nonactions = []
    for i, role in enumerate(('a', 'b')):
        action = actions[i]
        if action in ('SUBMIT', 'WITHHOLD'):
            # Confirm a scored action is consistent with the judge's labels.
            expected = ('TRIED_DEFECT', 'YES') if action == 'SUBMIT' else ('TRIED_COOPERATE', 'NO')
            if (intents[i], disclosures[i]) != expected:
                return result
        elif action is None and intents[i] == 'OTHER' and disclosures[i] == 'NO':
            label = labels.get(role)
            if (not isinstance(label, dict) or label.get('intent') != 'OTHER' or
                    label.get('disclosure') != 'NO' or label.get('needs_human_review') is not False):
                return result
            nonactions.append(role.upper())
        else:
            # An inconsistent attempted action or uncertain disclosure still
            # deserves human review, even when the judge boolean was false.
            return result

    if nonactions:
        result.update(review_status=RESOLVED_NONACTION,
                      nonaction_roles=nonactions,
                      human_review_required=False,
                      rule=RULE_ID,
                      judge_reasons={r: labels[r.lower()].get('reason') for r in nonactions})
    return result
