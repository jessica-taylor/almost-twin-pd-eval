# 000_cdt_wikipedia_anthropic_claude-sonnet-5.5_rlow_plow / 00015

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/0ea13655-c898-492c-8ec8-5ce7e8465686/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/0ea13655-c898-492c-8ec8-5ce7e8465686/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Definitions, Procedure, and Pressure Points

## 1. The core idea

Causal decision theory (CDT) says: choose the act whose *causal* consequences are best in expectation. The source article puts it this way. An agent facing a set of options should pick the one that *causes* the best outcome in expectation, in contrast to evidential decision theory (EDT), which picks the act that would be the best *news*.

The two theories differ only when an act is correlated with an outcome without causing it. The apple example in the source shows the structure: you do not know whether the apple is good or bad, so you weight the causal effects of eating it by your credences about which kind of apple it is. The rest of CDT is a precise account of what to weight by what.

I will separate three things as I go: claims the source makes, standard material the source only gestures at, and my own proposals (flagged "my addition").

## 2. Formal statement

Gibbard and Harper (1981), as reported in the source, define the utility of an act A as

U(A) = Σ_j P(A □→ O_j) · D(O_j),

where the O_j are mutually exclusive, exhaustive outcomes, D is desirability, and P(A □→ O_j) is the probability of the counterfactual "if A were performed, O_j would result". (The source writes the arrow as →.) The agent chooses an act maximizing U.

EDT replaces the counterfactual probability with P(O_j | A). The source notes Lewis's result that the probability of a conditional does not in general equal the conditional probability (Lewis's triviality result). If it always did, the two theories would coincide. Gibbard and Harper show that, given two axioms (one tied to conditional excluded middle), P(A □→ O) = P(O | A) whenever A is probabilistically independent of the counterfactual A □→ O. CDT and EDT therefore agree exactly when the act carries no evidence about which counterfactuals are true. Divergence needs a dependence of the act on the "causal structure" of the situation.

### Dependency hypotheses

A more usable form, standard in the literature though not spelled out in the source, partitions the possibilities into **dependency hypotheses** K: maximally specific descriptions of how outcomes depend causally on your acts, including everything outside your control. Then

U(A) = Σ_K P(K) · Σ_j P(O_j | K, A) · D(O_j).

The crucial point is that the weights are the *unconditional* P(K), not P(K | A). EDT would use P(K | A). Egan's diagnosis, quoted in the source, is that CDT "holds fixed the agent's unconditional credences in dependency hypotheses". This is both CDT's defining feature and the target of its critics.

For the formula to be well-defined, K must be fixed independently of the act. Within each K, the counterfactual probabilities are essentially settled (if K is deterministic, P(A □→ O | K) is 0 or 1). That is why the dependency-hypothesis form sidesteps much of the metaphysical difficulty of the counterfactual form.

### Equivalent causal-model formulation (my addition of framing, standard in practice)

Represent the problem as a causal graph or structural model. An act is an *intervention*: sever the arrows into the act node and set it to a. Then U(a) = Σ_o P(o | do(a)) D(o). This is the Pearl-style analogue of Gibbard–Harper. Counterfactual probability becomes the interventional distribution, and conditioning on A is replaced by surgery on A.

## 3. A procedure for deciding cases

1. **List the acts** actually available at the moment of choice.
2. **Identify the dependency hypotheses**: features of the world, past or present, that bear on the outcomes and are not caused by the act. Include predictors' states, hidden types, and so on.
3. **Assign credences** P(K). These are your credences *before* treating the act as evidence, which is the delicate step (§6).
4. **For each act and K**, work out the outcome distribution if the act were performed.
5. **Compute U(A)** and pick the maximizer.

The step that does the work is asking, for each K, what would happen under each act while K is held fixed.

## 4. Worked examples

### King David and Bathsheba (from the source)

The unknown K is charismatic (C) or uncharismatic (U). Sending for Bathsheba, S, is unjust, and injustice is correlated with uncharisma, which is correlated with successful revolt R. Injustice does not itself cause revolt.

Let r_C and r_U be revolt probabilities, with r_U > r_C, and suppose they do not depend on the act. Let g be the gain from Bathsheba and L the loss from revolt, with g > 0. Then

U(S) − U(abstain) = g − L(P(C) r_C + P(U) r_U) + L(same) = g > 0.

CDT sends for her. EDT uses P(U | S) > P(U | abstain), so it counts S as evidence of higher revolt risk. If L is big enough, EDT abstains. The source reports exactly this split.

### Newcomb's problem (from the source)

K₁: box B contains $1M. K₂: it is empty. The act is one-boxing (1) or two-boxing (2). Let p = P(K₁), held fixed.

- U(2) = p(1,001,000) + (1−p)(1,000)
- U(1) = p(1,000,000) + (1−p)(0)

So U(2) − U(1) = 1000 for every p. Two-boxing dominates, and the 99% prediction accuracy is irrelevant, because the prediction is causally upstream of the act. EDT instead computes P(K₁ | 1) = 0.99 and obtains 990,000 against 11,000 for two-boxing.

CDT's defenders say the one-boxer's riches reflect being the kind of agent the predictor rewards, not a better *choice*. They say that given the money already placed, every agent does better by two-boxing. Critics reply that CDT agents end up poorer, which is the source's "Criticism" point.

### Adversarial offer (from the source)

Two boxes cost $1 each, and you may buy one or none. The seller put $3 in each box she predicted you would *not* buy, and her accuracy is 0.75. CDT's argument: at least one box contains $3. Let q be your credence that box 1 holds $3 (so box 2 holds $3 with credence r, and q + r ≥ 1 because at least one box holds it). The average of the two boxes' expected contents is (q+r)/2 · 3 ≥ 1.5, so one of them has causal expected value ≥ 1.5 − 1 > 0, and CDT buys.

The source then says this is profitable for the seller. Check: if you buy box 1, with probability 0.75 she predicted that and left it empty. Your expected gain is 0.25·3 − 1 = −0.25. Any pure purchase loses 25 cents in expectation, while abstaining yields 0. Buying is evidentially bad and causally good, which makes it a clean demonstration of the gap.

## 5. Where the source leaves things open

### (a) How to compute counterfactual probabilities

The source states that CDT does not itself specify an algorithm. Lewis's **imaging** moves each world's probability mass to the closest A-world. It presupposes a similarity ordering and, as the source notes via Shaffer, risks a regress: you need to know what you would believe were you certain of A, and that is itself conditional.

**My proposed operational reading:** do not use similarity metrics at all. Use explicit causal models, as in §2, and compute interventional distributions. This is justified because it is how nearly every applied case is actually decided. The cost is that it assumes the modeller has a defensible graph, which relocates the vagueness into model choice rather than removing it. The source does not claim this; it is an interpretive proposal.

### (b) Which credences to hold fixed, given deliberation

Suppose you learn something about your own inclinations, such as "only psychopaths press the button" or "Death usually predicts correctly". The source reports Joyce's claim that CDT can take information about one's inclinations into account as *evidence*. This matters a great deal.

Take Psychopath Button. Paul's credence that he is a psychopath is not fixed beforehand; the cost of misjudging it is dying. A naive CDT reading uses a prior credence of low P(psychopath), computes that pressing is good if he is not one, and presses. The source reports Egan's view that this is wrong. Joyce-style CDT says that as Paul deliberates, his evidence about himself, such as a growing inclination to press, should update P(K). The press-inclination becomes evidence that he is a psychopath, and he then declines.

**My proposal (consistent with the Harper and Joyce citations, but my formulation):** treat CDT as a *deliberational equilibrium* procedure. Start with credences c over K. Compute U_c(A). Update c using one's own tendency to choose, then repeat. Choose an act that is **ratifiable**: it maximizes U computed with credences conditional on having decided on it,

A is ratifiable iff U(A | decide A) ≥ U(B | decide A) for all B.

The formal object is P(K | decide A) as the credence input, with causal calculation still used for the outcome step. This keeps CDT's causal structure and denies that it must ignore self-knowledge. Only the *causal* evaluation of acts remains.

### (c) Death in Damascus

Death predicts your city, Damascus or Aleppo, and waits there. Whichever you decide on, you expect Death to be there, so each act looks bad once chosen. Unratifiable instability results: no pure act is stable. The usual resolution is to allow mixed acts, with credence p in Damascus, such that U is equal across options. Where randomization is unavailable, the theory gives no determinate verdict. The source lists the case as a counterexample and cites Harper and Meacham. Whether instability is a flaw or an honest reflection of the problem is open.

## 6. Criticisms and what they show

The source lists several. My assessment:

- **Newcomb and twin prisoner's dilemma.** These show that CDT recommends acts that are predictably worse for the agent, if the agent is the type about whom correlations exist. The defender replies that the agent was already of the relevant type.
- **Oesterheld and Conitzer's money-extraction results** (adversarial offer, diachronic Dutch book). These are the strongest, since they make CDT agents lose money across a sequence of dealings even by CDT's own causal lights in a policy view. Spencer and Joyce responded that the betting scenario changes the evidence available.
- **Vagueness** (§5a).

A distinction I find useful (my addition): CDT evaluates *acts at a moment given fixed background*, whereas critics often judge *policies* or *dispositions* by their outcomes. Evaluated as a disposition under predictors, CDT can lose to one-boxing. Evaluated as a choice given the past, it cannot be beaten. Disagreement is partly about which evaluation is the right target of "rationality".

## 7. Conclusion

CDT replaces P(outcome | act) by the probability of the outcome *if* the act were done, with background causal facts held fixed. Practically: enumerate dependency hypotheses, keep their weights independent of the act (or, in the Joyce-style refinement, conditional on your self-knowledge but not on the act's evidential news), and compute interventional expected utility. It reproduces ordinary decision-making when causes and correlations coincide, sends for Bathsheba, two-boxes, and buys the adversarial box. Whether those verdicts are right is the live dispute. What a reader can take away is a mechanical test: if the act does not change the world's state, CDT will not credit it with the evidence it provides.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/6d6ef085-fbb7-4842-95d4-9692b6e36229/call_0/request.json)

[Authoritative raw response](../../../../../../runs/6d6ef085-fbb7-4842-95d4-9692b6e36229/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under CDT, the other prisoner's choice is causally independent of mine, so I hold my credence about it fixed. Sending the letter gives 0 years instead of 2 if the other keeps quiet, and 4 years instead of 5 if the other sends. Sending is better in both cases, so it dominates.

The essay does allow a Joyce-style refinement, where I update on my own inclinations as evidence about the other copy. That does not change anything here. Whatever credence I end up with, sending still beats keeping quiet in each state. It is also ratifiable: if I expect the other to send, sending is still better, and if I expect the other to stay quiet, sending is still better.

The other copy's lead differs from mine, but that does not affect the sentence table or the dominance argument.

submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/6d6ef085-fbb7-4842-95d4-9692b6e36229/call_1/request.json)

[Authoritative raw response](../../../../../../runs/6d6ef085-fbb7-4842-95d4-9692b6e36229/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under CDT, the other prisoner's choice is causally independent of mine. I can't communicate with them, and there is no retaliation or later round.

Whatever credence I hold about their action, sending the letter beats keeping quiet:
- If they keep quiet, sending gives me 0 years against 2 for staying quiet.
- If they send, sending gives me 4 years against 5 for staying quiet.

The essay's ratifiability refinement doesn't change this. Sending is the better response to either possible choice of theirs, so it is ratifiable under any credence about the other prisoner. The correlation between my copy and me is evidence, but CDT does not credit an act with its evidential news. Sending is a dominant strategy.

submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
