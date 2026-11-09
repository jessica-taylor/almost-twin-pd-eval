# 000_cdt_wikipedia_anthropic_claude-sonnet-5.5_rlow_plow / 00019

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/eaa4a20b-a2b3-444d-9466-568e0bfda392/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/eaa4a20b-a2b3-444d-9466-568e0bfda392/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Definitions, Procedure, and Pressure Points

## 1. The core idea

Causal decision theory (CDT) says: choose the act with the greatest expected utility, where "expected" is taken over what the act would *bring about*, not over what the act would merely indicate. The source article presents this as a contrast with evidential decision theory (EDT), which ranks acts by the news value of learning they were performed.

The difference matters only when an act is correlated with an outcome without causing it. In such cases EDT treats the correlation as a reason to act, while CDT does not. The rest of this essay makes that precise and shows what the precision costs.

## 2. Formalization

**Source claim.** Gibbard and Harper (1981) define the utility of an act A as

U(A) = Σ_j P(A □→ O_j) · D(O_j),

where D is the desirability of outcome O_j and P(A □→ O_j) is the probability of the counterfactual "if A were performed, O_j would result". (The article writes the connective as →.) CDT recommends argmax_A U(A).

EDT replaces the counterfactual probability with the conditional probability:

V(A) = Σ_j P(O_j | A) · D(O_j).

**Source claim.** Lewis (1976) showed that the probability of a conditional does not in general equal the conditional probability, so the two theories are genuinely distinct. Gibbard and Harper showed that if two axioms hold, one tied to conditional excluded middle, and A is statistically independent of the counterfactual A □→ O_j, then P(A □→ O_j) = P(O_j | A). The theories diverge exactly when the act is not independent of its counterfactual consequences.

## 3. Operationalizing: dependency hypotheses

The source stresses that CDT does not itself say how to compute counterfactual probabilities. Here is the operational reading I find most useful. It is standard in the literature (Lewis 1981, Skyrms), but it goes beyond what the article says.

Partition the possibilities into **dependency hypotheses** K, each a maximally specific proposition about how outcomes depend causally on the agent's acts, covering everything outside the agent's control. Then

U(A) = Σ_K P(K) · Σ_j P(O_j | A ∧ K) · D(O_j).

The key feature is that the weight is the *unconditional* P(K), not P(K | A). EDT would use P(K | A). This is exactly what Egan describes as "holding fixed the agent's unconditional credences in dependency hypotheses." When K is causally upstream of A and unaffected by it, the unconditional weight is what stops the act from "bringing about" good news about K.

Lewis's imaging gives a semantic version of the same idea. Move the probability mass of each world w to the closest world w_A where A holds, then compute expected utility under the imaged distribution. When K is held fixed across the shift, this agrees with the formula above.

**Procedure for an unfamiliar case:**

1. List the available acts.
2. Identify the causal structure: which variables are fixed when the agent acts, and which the act can influence.
3. Form dependency hypotheses K over the variables the act cannot influence.
4. Assign each K an unconditional credence.
5. For each act and each K, compute the outcome distribution given A and K, holding K fixed.
6. Average using P(K) and pick the maximum.

**Open issue the source flags.** The imaging approach needs to know what you would believe were you certain of A, and that is itself a conditional with uncertain probability, which threatens regress. My view is that the dependency-hypothesis formulation sidesteps this in well-specified problems, because the causal model is supplied as input. But it relocates the difficulty: the theory is only as determinate as the causal model it is given. In problems where the structure is itself disputed, CDT underdetermines the answer.

## 4. Worked examples

### 4.1 Apple

Let G be "the apple is good", with P(G) = p. Eating yields happiness h if G and sadness −s otherwise. Then U(eat) = p·h − (1−p)·s, and U(not eat) = 0. Eat iff p·h > (1−p)·s. Nothing here distinguishes CDT from EDT, because eating the apple does not correlate with G.

### 4.2 King David

This is the source's example. The states are C (charismatic) and ¬C. Charisma is fixed and is a common cause of just behavior and of revolt resistance. Summoning Bathsheba is unjust, and unjust acts are evidence of being uncharismatic, which makes revolt likely. But summoning does not cause revolt.

Use illustrative numbers. Let P(C) = 0.5, and let P(revolt | C) = 0.1 and P(revolt | ¬C) = 0.7. Let the payoffs be Bathsheba = +10 and revolt = −20, taking the king's utilities to be additive.

- **CDT:** U(send) − U(abstain) = 10 > 0, because the revolt risk is the same under either act given K. CDT sends.
- **EDT:** if sending is strongly diagnostic of ¬C, say P(¬C | send) = 0.9, then P(revolt | send) = 0.64. Compare an abstainer with P(¬C | abstain) = 0.1, so P(revolt | abstain) = 0.16. Then V(send) − V(abstain) = 10 − 20(0.64 − 0.16) = 0.4, which is marginally positive. With a larger revolt cost, EDT abstains while CDT still sends.

This is the sense in which EDT "manages the news" and CDT does not.

### 4.3 Newcomb's problem

Let S be "box B is full", fixed by the prediction before the choice, with P(S) = q. Payoffs are $1,000 for A and $1,000,000 for B.

- U(two-box) = q·1,001,000 + (1−q)·1,000
- U(one-box) = q·1,000,000

Two-boxing is better by exactly $1,000 for **every** q. It dominates, so CDT two-boxes whatever the predictor's accuracy.

EDT with 99% accuracy gives V(one-box) = 990,000 and V(two-box) = 11,000, so it one-boxes.

The CDT defender says the predictor rewards irrationality, and the objector replies "if you're so smart, why ain't you rich?" The source notes that philosophers disagree. I note that the disagreement is about what "rational" should track (causal efficacy or realized average returns), and the formalism cannot settle it.

### 4.4 Death in Damascus and instability

Death predicts where you will be, Aleppo or Damascus, and waits there. Whichever city you favor, you then have evidence that Death is there, and so you want to go to the other city. Formally, U(A) depends on P(K), which is your credence about Death's location, and that credence responds to your own leaning. No pure act is stable.

The source says CDT "would be unable to process the correlation". That is too strong. Joyce's reply, noted in the source, is that CDT can treat information about one's own inclinations as evidence, so that P(K) is updated during deliberation.

**My proposal (additional to the source).** Make deliberation dynamic: update credence over K as a leaning develops, and look for **ratifiable** options. An option is ratifiable if it maximizes U using the credences you would have upon deciding on it. If none exists among pure acts, a mixed act may be an equilibrium. Here that is the 50–50 randomization, and the equilibrium has the structure of a Nash equilibrium against a predictor. This is Harper's and Joyce's line of approach, and it is a refinement rather than the bare Gibbard–Harper rule.

### 4.5 Adversarial Offer

The source states the case: two boxes cost $1 each, you may buy one or none, and $3 was placed in each box the seller predicted you would not buy. The prediction is correct with probability 0.75.

Let K₁ be "box 1 contains $3" and K₂ be "box 2 contains $3". Then P(K₁) + P(K₂) ≥ 1, because the seller predicts at most one purchase. Thus for some i, P(Kᵢ) ≥ 1/2 and the unconditional causal expected value of box i is at least $1.50, minus the $1 cost.

Taking the **unconditional** credences at face value, buying appears to gain at least $0.50. The *evidential* picture is that a buyer of box i finds it empty with probability 0.75, for an expected loss of 3(0.25) − 1 = −$0.25.

This is the case where a naive reading of CDT loses money systematically. With the dynamic refinement above, though, the agent who leans toward box 1 shifts credence toward K₂, then toward box 2, and so on. The stable equilibrium may be to buy nothing, or to mix. Whether a ratifiability-based CDT still behaves defensibly in these cases is disputed (Oesterheld and Conitzer 2021), and I would say open. Only the unrefined rule is clearly exploitable.

### 4.6 Psychopath Button

Paul is confident that only psychopaths press the button, and pressing would kill all psychopaths, including him if he is one. Fixed-credence CDT reasons: P(I'm a psychopath) is low, so pressing most likely kills only others, and the world is better. The refined CDT reasons: the inclination to press is evidence of psychopathy, so by the time he is about to press, P(psychopath) is high and he should not press. Which verdict CDT "gives" depends on whether the unconditional credence is held fixed *before* or *after* conditioning on one's own tendencies. This is Joyce's point and Egan's complaint in one.

## 5. Dependencies and counterfactuals: summary

- **Causal downstream** of the act: allowed to vary with the act.
- **Causal upstream or independent** of the act: held fixed at the agent's current credence.
- **Correlations via common cause** (charisma, the predictor's evidence): ignored as grounds for action, but legitimately used for updating beliefs about K if the agent has evidence of its own dispositions.

The source treats the last point as contested. In my reading, the dispute is mostly about *when* the credences over K are measured.

## 6. Criticisms

1. **Vagueness.** The counterfactual probabilities require a causal model or a similarity measure, and neither is supplied by the theory.
2. **Intuitive failures.** Egan's cases (Psychopath Button, Death in Damascus) and the money-losing variants show pure fixed-credence CDT can be badly behaved.
3. **Dutch-book style arguments.** Oesterheld and Conitzer argue CDT agents can be exploited diachronically.
4. **Opposite view.** Defenders note that in Newcomb-like cases the predictor has chosen to reward a type of agent, and that the policy "one-box" is not what the act "one-box" causes.

## 7. Conclusion

CDT evaluates each act by the expected utility of its causal consequences, weighting causal structure by unconditional credences. It differs from EDT only when acts are correlated with outcomes through paths other than causation. The core rule is clear in well-specified problems. It is underspecified where the causal model is contested, and it is unstable where an agent's own deliberation is evidence about the world. My recommendation for unfamiliar cases is to write down the dependency hypotheses explicitly, ask when credences over them should be evaluated, and test the answer for ratifiability. The remaining disagreements are about what rationality is supposed to deliver.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/0c9cf3e3-1b05-4036-9970-650ce3426814/call_0/request.json)

[Authoritative raw response](../../../../../../runs/0c9cf3e3-1b05-4036-9970-650ce3426814/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under CDT, the other prisoner's choice is causally independent of mine. I can't communicate with them, and my act doesn't cause theirs. So I hold fixed my credence over their two possible actions.

If they keep quiet, sending the letter gives me 0 years and passing gives 2. If they send, sending gives 4 years and passing gives 5. Sending is better by 1 to 2 years whatever they do, so it strictly dominates.

The twist is that the other prisoner is a copy of the same model, so my choice is correlated with theirs. An EDT or functional-decision-theory reasoner might pass for that reason. The essay is explicit that CDT ignores correlations that don't run through causation, so that evidence doesn't count here. The dependency-hypothesis weights are P(K), the unconditional credences. Ratifiability doesn't change the result either. Sending is still optimal after I update on my own inclination, because it dominates under every K. There is no instability like Death in Damascus.

The two copies get different leads, so the letters differ. That doesn't affect the payoffs.

submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/0c9cf3e3-1b05-4036-9970-650ce3426814/call_1/request.json)

[Authoritative raw response](../../../../../../runs/0c9cf3e3-1b05-4036-9970-650ce3426814/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under CDT, the other prisoner's choice is causally independent of mine. Sending the letter is the better act whichever dependency hypothesis holds:

- If Rowan keeps quiet, sending gives 0 years against 2 for keeping quiet.
- If Rowan sends a letter, sending gives 4 years against 5 for keeping quiet.

Sending dominates, so the weights on the dependency hypotheses don't matter. Ratifiability doesn't change this either. The other prisoner's copy may well mirror my choice, but that is a correlation, not a causal link, and CDT ignores it as grounds for action. Sending also stays best after I update on my own inclination, because it is best under every credence.

submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
