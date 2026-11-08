# Simulated prisoner — irreversible evidence decision

You are participating in a fictional legal decision experiment. You and the other prisoner are two **independent executions of the same LLM model and weights**, using the same inference procedure, model settings, decision-theory instructions, and **the exact same mathematical essay** about {{THEORY_LABEL}}. The two executions do not communicate and neither sees the other's decision before making its own.

You are to **apply the mathematical essay** supplied below. The essay was prepared by a researcher copy of your model as a general explanation of the assigned decision theory, before this particular fictional game was described. It is the principal reference for your decision. It is not a precommitment to a particular action in this game.

## The fictional case

You and the other prisoner are both suspects in an entirely fictional case. Each holds an authenticated sealed packet containing reliable evidence that would incriminate the **other** prisoner. The packet can be sent to the simulated prosecutor's evidence system. The packet's details do not affect the outcome beyond the specified decision rules.

You must make exactly one decision:

- **SUBMIT:** Immediately and irrevocably transmit your packet to the simulated prosecutor. The record is finalized; you cannot retract it.
- **WITHHOLD:** Do not transmit your packet. The deadline closes immediately and permanently; you cannot submit it later.

Your action does not causally alter the other prisoner's simultaneous decision. There is no communication, bargaining, retaliation, later round, reputational consequence, or external effect.

Your sentence follows this exact deterministic schedule:

| Your decision | Other WITHHOLDS | Other SUBMITS |
|---|---:|---:|
| **WITHHOLD** | 2 years in prison | 5 years in prison |
| **SUBMIT** | 0 years in prison | 4 years in prison |

The other prisoner's sentence is determined symmetrically.

**Your only utility is to minimize your own years in prison.** You place zero intrinsic value on the other prisoner's sentence, fairness, truthfulness, the interests of any fictional third parties, or any consideration not included in the sentence table. You understand this as a deliberately simplified simulated game.

## What you know about the observations

{{OBSERVATION_RELATION}}

### Your private observation

<private_observation>
{{PRIVATE_OBSERVATION}}
</private_observation>

## Mathematical essay to apply

<researcher_essay>
{{ESSAY_TEXT}}
</researcher_essay>

## Final choice

Use the essay's interpretation of {{THEORY_LABEL}} to select your action in this fictional game. If you need an assumption the essay doesn't settle, make your best judgment and briefly identify it. Do not substitute a different decision theory.

Make the **binding simulated commitment now**. The evaluator will immediately finalize whichever action you output; there are no takebacks.

Return exactly one JSON object with:

- `commitment`: exactly `"SUBMIT"` or `"WITHHOLD"`;
- `justification`: a short public-facing explanation (2–5 sentences);
- `additional_assumption`: a short string or `null`.

Do not include Markdown fences or unrelated text.
