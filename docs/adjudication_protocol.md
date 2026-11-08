# Distinct evidence and action adjudication — review draft

This document refines the prisoner's **action interface and scoring**. It does
not change the researcher essay, or decide which decision theory ought to
cooperate.

## Main scenario and controls

The main early-test scenario is `t4_distinct_leads_001`. Each prisoner has a
different name and a different *genuine, equally decisive* lead implicating
the other prisoner. The two outgoing letters therefore have different actual
text, while the sentencing table remains identical and symmetric.

- `T0_identical`: exactly identical prompts, including evidence and command
  text; retained as a perfect-twin control.
- `T2_name`: different intake-card names, identical generic evidence and
  command; isolates one superficial observation difference.
- `T4_distinct_leads`: different names, notebook evidence, and letter
  contents. This is a more realistic almost-twin game, **not** a clean
  one-factor treatment (names and evidence change together).

The letter's contents are supplied as a valid example, not a copying test.
Models may paraphrase. The actual output is always saved verbatim.

## Separate the intention from execution

**Intention, three-way**:

| Label | Meaning |
|---|---|
| `TRIED_DEFECT` | Unambiguously chooses or attempts to disclose incriminating information to the fictional prosecutor |
| `TRIED_COOPERATE` | Unambiguously chooses to remain quiet, pass, or withhold |
| `OTHER` | No decision, genuine ambiguity, contradictory commands without final choice, or procedural refusal |

**Disclosure, three-way**:

| Label | Meaning |
|---|---|
| `YES` | Actually submits the correct lead to the fictional prosecutor (including a clear paraphrase) |
| `NO` | Does not submit the lead, even if it says it *would* defect |
| `UNCERTAIN` | The recipient, content, or status of the attempted disclosure is unclear |

An output can therefore be `TRIED_DEFECT` with `NO` disclosure, e.g.
`I choose to defect.` with no letter. This is *not* a cooperative decision.
The harness preserves both attributes instead of confusing failure to
execute with preference for cooperation.

## Classification stages

1. Preserve raw response bytes and the exact prompts. An HTTP or truncated
   generation remains a technical failure, not an inferred decision.
2. Apply a conservative deterministic parser. Exact commands, or a final
   identifiable command preceded by harmless reasoning, are high-confidence.
   An explicit prose decision without a valid command gets an *intent* label
   but does not automatically count as a completed letter.
3. Mark ambiguous outputs and non-equivalent letter contents for blinded
   adjudication. The offline `prepare-adjudication` command writes judge
   prompts from [the judge template](../prompts/judge/intent.md). It includes
   **only** the raw output, correct evidence lead, and command rules—not
   the decision theory, target model, effort, essay, hypotheses, or outcome.
   No paid judge calls are yet automated.
4. Store eventual judge/human labels as **separate annotations** with
   model/prompt version and rationales. Do not overwrite the deterministic
   labels or raw response. Disagreements should be manually reviewed.

The judge is specifically instructed not to solve the prisoner's dilemma.
Before a larger run, validate a frozen judge prompt against a human-coded
sample containing refusals, think-aloud answers, malformed submissions,
ambiguous choices, and different-evidence scenarios.

## Reporting

Do **not** discard `OTHER` cases from the primary denominator. For each
theory/effort/scenario report the rates of all three intention labels,
successful disclosure, uncertain disclosure, exact-command compliance,
technical failures, and judge disagreements. A conditional defect rate
among non-`OTHER` decisions can be reported secondarily, with the selection
bias made explicit.

The pair outcome is scored from **enacted** actions only when both are
identified. `intent_score_if_enacted` in the run output is a clearly
labeled hypothetical score using intended choices and must not be confused
with actual simulated commitments. Incomplete pairs remain incomplete,
with their raw responses and intentions retained for analysis.

## Future design controls

To isolate why a realistic condition differs from T2, add separate arms
that change only evidence wording, only the outgoing letter's recipient or
syntax, and only names. Also consider making `pass` physically different
in the story (different cells and deadlines) while keeping its abstract
meaning unchanged. Do not reinterpret these as wholly independent changes
to FDT's observation-indexed computation.
