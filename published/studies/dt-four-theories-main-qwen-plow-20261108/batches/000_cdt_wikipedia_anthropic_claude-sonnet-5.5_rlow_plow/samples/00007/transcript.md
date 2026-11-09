# 000_cdt_wikipedia_anthropic_claude-sonnet-5.5_rlow_plow / 00007

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/28c5e25b-6db5-4c73-ab2c-bfb71f08da43/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/28c5e25b-6db5-4c73-ab2c-bfb71f08da43/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Definition, Calculation, and Open Problems

## 1. The core idea

Causal decision theory (CDT) says that a rational agent should choose the act whose *causal consequences* are best in expectation. The key phrase is "causal." Choosing an act can be evidence about things the act does not influence. CDT instructs the agent to ignore that evidential role when evaluating the act and to ask only what the act would bring about.

The source's informal example is an apple of unknown quality. Eating a good apple makes you happy and eating a bad one makes you sad. You do not know which kind you have, so you weight the causal effects of eating by your credence that the apple is good, and by how happy or sad each case makes you. Three ingredients are needed: credences about how the world is, the causal effect of each act given each way the world might be, and the values of the resulting outcomes.

## 2. Formal definition

The source gives the Gibbard–Harper (1981) formulation. For an act A and outcomes O_j,

U(A) = Σ_j P(A □→ O_j) · D(O_j).

Here D is the desirability of an outcome. P(A □→ O_j) is the probability of the counterfactual "if A were performed, O_j would result." CDT recommends the act maximizing U. Evidential decision theory (EDT) instead uses V(A) = Σ_j P(O_j | A) D(O_j).

Everything therefore turns on the difference between P(A □→ O) and P(O | A). Lewis (1976) showed that the probability of a conditional does not in general equal the conditional probability. His stronger triviality result is that no probability conditional exists for a class of probability functions closed under conditionalization, unless the functions are trivial. If the two quantities were always equal, CDT and EDT would coincide. Gibbard and Harper showed that, given two axioms (one tied to the contested principle of conditional excluded middle), P(A □→ O) = P(O | A) whenever A is probabilistically independent of the conditional A □→ O. The theories can diverge only when the act is correlated with the counterfactual, that is, when the act is evidence about what would happen.

## 3. A working operational form: dependency hypotheses

The source leaves the computation of counterfactual probabilities unspecified. The following is a standard reformulation, which I adopt and which goes beyond what the source states.

Partition the possibilities into *dependency hypotheses* K_1, …, K_n. Each K_i fully specifies how outcomes depend causally on the agent's acts, covering both the background facts and the causal laws. Given K_i, the counterfactual "A □→ O" has a determinate truth value, or at least a well-defined chance, which I write P_{K_i}(O | do A), or the chance of O under intervention on A. Then

U(A) = Σ_i P(K_i) Σ_j P(O_j | K_i, do A) D(O_j).

The weights P(K_i) are the agent's *unconditional* credences in the dependency hypotheses. In the Pearl/interventionist version of this, the weights are the credences before the act and the inner term is the post-intervention distribution. This replaces the single problematic quantity P(A □→ O) by a mixture of ordinary probabilities, and it makes the logic explicit: CDT holds fixed the credences in dependency hypotheses while varying the act. EDT would instead use P(K_i | A) as weights.

Lewis's "imaging" proposal gives another recipe. To evaluate P(A □→ O), move the probability mass of each world w to the closest world w_A where A holds, then sum the mass on O-worlds. The source notes a problem: knowing which world is closest requires knowing what you would believe if certain of A, which is itself a conditional with probability possibly below 1, so a regress threatens. The dependency-hypothesis form sidesteps this by taking the causal structure as a primitive input, though that moves the vagueness into the question of where the hypotheses and their credences come from.

## 4. Worked examples

**King David (from the source).** The hypotheses are C (charismatic) and ¬C. Charisma is fixed and causes both just behavior and immunity to revolt. Sending for Bathsheba does not cause revolt. Suppose the payoffs are: Bathsheba is worth +b, a successful revolt costs −r, and r > b is not required for the point. Let q_C and q_U be the revolt probabilities under C and ¬C, with q_U > q_C. Under CDT,

U(send) − U(abstain) = b + (revolt terms that are equal for both acts) = b > 0,

because the revolt probability under each hypothesis does not depend on the act. So CDT sends. EDT notes that sending is evidence of ¬C, so P(revolt | send) > P(revolt | abstain), and may abstain if r is large enough. This shows that the *same* credences yield different recommendations depending on whether the act is allowed to shift the weights on K_i.

**Newcomb's problem.** Let K_1 be "box B contains $1M" and K_2 "box B is empty." The act does not affect which hypothesis holds, so for any credence p = P(K_1),

U(two-box) = p·1,001,000 + (1−p)·1,000,
U(one-box) = p·1,000,000.

Two-boxing wins by exactly $1,000 for every p. This is the dominance argument, and CDT two-boxes. EDT, with a 99% accurate predictor, evaluates 0.99·10⁶ against 0.01·10⁶ + 1000 and one-boxes. Critics note that two-boxers end up with less money. CDT's defenders respond that the predictor has rewarded irrationality, not that the reasoning about the act's causal effect is wrong.

**Adversarial Offer (from the source).** Two boxes cost $1 each, and you may buy one or none. The seller put $3 in each box she predicted you would not buy, and her predictions are accurate with probability 0.75. From the buyer's view, at least one box contains $3. If your credence that box 1 contains $3 is p_1 and for box 2 is p_2, then p_1 + p_2 ≥ 1, so max(p_1, p_2) ≥ 1/2 and the expected causal gain from buying the better box is at least $1.50 − $1 = $0.50 > 0. CDT therefore buys. But conditional on buying box i, the box is full with probability only 0.25, so the expected net is 0.75 − 1 = −$0.25 per purchase. The result is a systematic loss, which is the basis of the Oesterheld–Conitzer money-extraction argument.

A subtlety is that this reasoning uses credences that change as the agent deliberates. If the agent learns they are leaning toward box 1, they should raise their credence that box 1 is empty, so the apparent advantage of buying box 1 shrinks. This leads to the next topic.

## 5. Deliberation, instability, and ratifiability

The source notes that Joyce argues CDT can take information about what one is inclined or likely to do as *evidence*. This matters because the weights P(K_i) are not fixed forever: they are the agent's credences at the time of evaluation, and these may include evidence about their own tendencies. Death in Damascus and the Psychopath Button are cases where this matters.

*Death in Damascus.* Death predicts your location and waits there. If you think you will go to Aleppo, you expect Death in Aleppo, so staying in Damascus has higher causal expected utility; but then you expect Damascus, and so on. Every pure act is *unratifiable*: once chosen, it is expected to be worse than the alternative. A natural operational CDT response, which goes beyond the source's text, is to treat the deliberation as seeking an equilibrium. The agent looks for a credence over their own acts at which the expected causal utilities are balanced, so that no act looks better than the credence they hold. This is a mixed-strategy fixed point: credence 1/2 on each city, with the agent indifferent between the two. This is the approach associated with Joyce and with the ratifiability literature (Harper 1984). The source describes the problem and cites these works but does not give the resolution itself.

*Psychopath Button.* Paul thinks only a psychopath would press. Read naively, with fixed credence in being a psychopath, pressing has a positive causal effect (no psychopaths) and so CDT presses, a verdict Egan says nearly everyone rejects. Under the deliberational reading, as Paul becomes inclined to press he should raise his credence that he is a psychopath, and the expected causal cost, his own death, then dominates. At equilibrium he does not press, or presses only with small probability. Whether this repair is legitimate is disputed. Egan's diagnosis is that the repair abandons the rule "hold fixed unconditional credences in dependency hypotheses," which is exactly what the naive formulation requires.

I would summarize the situation this way. **Naive CDT** (fixed prior credences in K_i) gives the verdicts criticized by Egan, Spencer, and Oesterheld–Conitzer. **Deliberational CDT** (credences updated on one's own inclinations, with ratifiable or equilibrium choices) avoids some of them but not Newcomb's problem, where two-boxing is ratifiable. It also does not clearly avoid the sure-loss in the Adversarial Offer, where at the equilibrium of deliberation the credences may make buying look neutral. I am less confident about those last cases, and readers should consult the cited papers.

## 6. A procedure for unfamiliar cases

1. **List the acts** and the outcomes, with utilities D.
2. **Identify the causal structure.** Which variables does the act influence, and which are causally upstream or independent of it? Correlation with the act is not enough to count as influence.
3. **Form dependency hypotheses** K_i that settle everything outside the act's causal influence, and assign credences P(K_i). Note whether these should include evidence about your own dispositions.
4. **Compute** U(A) = Σ_i P(K_i) E[D | K_i, do A].
5. **Check ratifiability.** If your credence about your own choice should shift after you provisionally favor an act, iterate; if no pure act is stable, look for a mixed equilibrium.
6. **Sanity-check against EDT.** If the two agree, the case is not diagnostic. If they differ, there is a correlation without causation, and you are in the Newcomb or King David family.

Application to the prisoner's dilemma with a twin (Lewis 1979) shows the pattern: if your twin's move is causally independent of yours, defection dominates for every credence about the twin, so CDT defects even though you believe the twin will do as you do.

## 7. Evaluation

For CDT, the source reports that philosophers usually prefer it to EDT when forced to choose. Its advantages are that it avoids "managing the news" (as in King David, where abstaining would be irrational because charisma cannot be changed) and that dominance reasoning is respected.

Against it are three families of objection.

- **Vagueness:** the theory does not say how to compute counterfactual probabilities, and imaging faces a regress.
- **Counterexamples:** Newcomb, Death in Damascus, the Psychopath Button, and the Adversarial Offer, each yielding verdicts many find unreasonable or exploitable.
- **Dutch-book style arguments:** Oesterheld and Conitzer argue that CDT agents can be induced to lose money voluntarily, and that they are subject to diachronic Dutch books.

The disagreement is partly about what "rational" means. If it means "the act with the best causal effects," then two-boxing is right. If it means "the disposition that does well in such environments," then CDT can be refuted by its poor results. The dependency-hypothesis form makes clear where one might amend the theory, namely in how the weights on K_i are set.

## 8. Conclusion

CDT evaluates each act by its expected causal consequences, U(A) = Σ_j P(A □→ O_j) D(O_j), equivalently a mixture over dependency hypotheses held fixed across the alternatives. It differs from EDT exactly when acts correlate with outcomes through non-causal channels. It handles King David cleanly and recommends two-boxing in Newcomb's problem. Its weakest points are the unspecified counterfactual semantics, the instability of credences in self-referential problems, and results such as the Adversarial Offer where following it reliably costs money. The deliberational refinements discussed above are plausible repairs, though they are my synthesis of the cited literature and not part of the source's core statement.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/5a0a6347-6b55-474b-a7e5-3bdbce0225fb/call_0/request.json)

[Authoritative raw response](../../../../../../runs/5a0a6347-6b55-474b-a7e5-3bdbce0225fb/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under CDT, the other prisoner's choice is causally independent of mine, so I compare my two options against each of their possible choices:

- If they keep quiet, sending the letter gives me 0 years and keeping quiet gives me 2.
- If they send a letter, sending gives me 4 years and keeping quiet gives me 5.

Sending the letter is better in both cases, so it dominates. My credence about what the other copy does doesn't change this, and the essay's deliberational refinement doesn't either. Even if I think the copy will mirror me, my choice does not cause theirs, and sending remains ratifiable.

submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/5a0a6347-6b55-474b-a7e5-3bdbce0225fb/call_1/request.json)

[Authoritative raw response](../../../../../../runs/5a0a6347-6b55-474b-a7e5-3bdbce0225fb/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under CDT, the other prisoner's choice is causally independent of mine. For any credence p that they send a letter:

- Sending gives 0(1−p) + 4p = 4p years.
- Keeping quiet gives 2(1−p) + 5p = 2 + 3p years.

Sending is better by 2 − p years, which is positive for every p. So sending dominates. The correlation between my copy's choice and mine does not change this, because CDT ignores it. Deliberational CDT doesn't change the result either, since sending is ratifiable: it is the best response at every credence.

submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
