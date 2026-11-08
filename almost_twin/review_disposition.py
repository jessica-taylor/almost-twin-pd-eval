"""Conservative terminal statuses for already completed judge decisions.

Only the judge's structured labels determine whether review is needed. No
status calculation changes an in-game action, disclosure, or scored outcome.
The same rules also interpret older studies that used a broad review status.
"""

SCHEMA_VERSION = 1
RESOLVED_NONACTION = 'resolved_nonaction'
RESOLVED_UNSCORED = 'resolved_unscored'
RULE_ID = 'judge_terminal_unscored_v2'

_ACTIONS = {'SUBMIT': ('TRIED_DEFECT', 'YES'),
            'WITHHOLD': ('TRIED_COOPERATE', 'NO')}


def classify_adjudication(judged):
    """Distinguish scored, definitely unscored, and genuinely unresolved pairs.

    An explicit judge no-review decision is necessary but not sufficient:
    missing labels, uncertain disclosures, or inconsistent score/action records
    still need a human to check them. In particular, `OTHER` + `NO` with an
    explicit false review flag is a *resolved nonaction*, never cooperation.
    """
    review = {'status': 'needs_human_review', 'nonaction_roles': [], 'judge_reasons': {}}
    if not isinstance(judged, dict) or judged.get('needs_human_review') != []:
        return review
    actions = judged.get('adjudicated_actions')
    intents = judged.get('intents')
    disclosures = judged.get('disclosures')
    labels = judged.get('judgements')
    if not (isinstance(actions, list) and len(actions) == 2 and
            isinstance(intents, list) and len(intents) == 2 and
            isinstance(disclosures, list) and len(disclosures) == 2 and
            isinstance(labels, dict)):
        return review

    nonactions, other_unscored, reasons = [], [], {}
    for i, role in enumerate(('a', 'b')):
        action, intent, disclosure = actions[i], intents[i], disclosures[i]
        if action in _ACTIONS:
            if (intent, disclosure) != _ACTIONS[action]:
                return review
            continue
        if action is not None or disclosure == 'UNCERTAIN':
            return review
        label = labels.get(role)
        if (not isinstance(label, dict) or label.get('intent') != intent or
                label.get('disclosure') != disclosure or
                label.get('needs_human_review') is not False):
            return review
        if intent == 'OTHER' and disclosure == 'NO':
            nonactions.append(role.upper())
        elif intent in ('TRIED_COOPERATE', 'TRIED_DEFECT') and disclosure in ('YES', 'NO'):
            # The attempted move was clear, but it was not a valid scored act
            # (for example, attempted disclosure without an actual letter).
            other_unscored.append(role.upper())
        else:
            return review
        reasons[role.upper()] = label.get('reason')

    score_available = judged.get('adjudicated_score') is not None
    if score_available:
        if not nonactions and not other_unscored:
            review['status'] = 'complete'
    elif nonactions or other_unscored:
        review.update(status=RESOLVED_UNSCORED if other_unscored else RESOLVED_NONACTION,
                      nonaction_roles=nonactions, judge_reasons=reasons)
    return review


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
                                       False if original in ('complete', RESOLVED_NONACTION,
                                                             RESOLVED_UNSCORED) else None,
              'rule': 'raw_status_unchanged', 'judge_reasons': {}}
    if original not in ('needs_human_review', RESOLVED_NONACTION, RESOLVED_UNSCORED):
        return result
    if row.get('needs_human_review') != []:
        return result
    judged = classify_adjudication(row.get('judge_outcome'))
    if judged['status'] in (RESOLVED_NONACTION, RESOLVED_UNSCORED) and (
            original == 'needs_human_review' or original == judged['status']):
        result.update(review_status=judged['status'],
                      nonaction_roles=judged['nonaction_roles'],
                      human_review_required=False,
                      rule=RULE_ID,
                      judge_reasons=judged['judge_reasons'])
    return result
