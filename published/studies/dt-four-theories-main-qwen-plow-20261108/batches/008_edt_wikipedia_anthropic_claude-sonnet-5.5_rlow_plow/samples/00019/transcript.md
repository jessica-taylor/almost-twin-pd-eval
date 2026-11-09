# 008_edt_wikipedia_anthropic_claude-sonnet-5.5_rlow_plow / 00019

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/2b14c853-917e-4a59-aaff-834c1fb53608/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/2b14c853-917e-4a59-aaff-834c1fb53608/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Acts as News

## 1. The core idea

Evidential decision theory (EDT) says: choose the act you would most like to learn you will perform. The slogan is "do what you most want to learn that you will do" (Ahmed 2021, as cited in the source). An act is treated as a piece of evidence about the world, and its value is the expected desirability of the world given that evidence.

Formally, following the source's presentation of Gibbard and Harper (1976), for an act A and outcomes O_j,

V(A) = Σ_j P(O_j | A) · D(O_j),

where D is desirability (utility) and P is the agent's credence function. EDT selects argmax_A V(A).

This is ordinary expected-utility maximization with one specific choice: the probabilities that weight outcomes are conditional on the act. The contrasting causal formulation, also from the source, is

U(A) = Σ_j P(A □→ O_j) · D(O_j),

where A □→ O_j is the counterfactual "if A were performed, O_j would occur." The two formulas differ exactly when P(O_j | A) ≠ P(A □→ O_j), that is, when the act is correlated with outcomes through channels other than its causal influence.

I separate three kinds of material below: claims the source makes, standard elaborations I am adding (marked *Addition*), and my own operational proposals (marked *Proposal*).

## 2. How the theory evaluates acts

**Procedure.**
1. Fix the available acts and a partition of outcomes.
2. Take your current credences P, including any correlations between your act and features of the world.
3. For each act compute the conditional distribution P(· | A).
4. Compute V(A) and pick the maximum.

Policies can be treated as acts: a policy is a (possibly conditional) plan, and V(π) = E[D | I follow π]. *Addition:* when decisions are sequential, one evaluates the plan, or recursively evaluates each choice conditional on the information then held.

**Dependencies.** EDT does not distinguish causal from merely statistical dependence. Whether A causes O, O causes A, or a common cause produces both, what matters is only whether learning A shifts your beliefs about O. In that sense the theory needs no causal model, only a probability function. That is both its appeal (it is conceptually minimal and never requires evaluating counterfactuals) and the basis of its main criticism.

**Counterfactuals.** EDT makes no use of counterfactual probabilities. Counterfactual reasoning enters only indirectly, if at all, through the agent's own credences. Where causal structure does matter (e.g., I know the box contents are already fixed), it matters only insofar as it shapes conditional credences.

## 3. Worked examples from the source

### Newcomb's problem

A predictor with 99% accuracy fills opaque box B with $1,000,000 if it predicted one-boxing, and leaves it empty if it predicted two-boxing. Transparent box A holds $1,000.

V(one-box) = 0.99 · 1,000,000 + 0.01 · 0 = $990,000
V(two-box) = 0.01 · 1,001,000 + 0.99 · 1,000 = $11,000

EDT one-boxes. CDT two-boxes because the contents are already fixed and the act cannot change them.

*Addition: the general threshold.* Let accuracy be p, assumed symmetric. Then V(one) = p·M and V(two) = (1−p)(M+K) + pK = K + (1−p)M, with M = 10^6 and K = 10^3. One-boxing wins iff p > (M+K)/(2M) = 0.5005. So EDT one-boxes whenever the predictor is even slightly better than chance, which shows how little reliability the argument needs.

### Twin prisoner's dilemma

Payoffs: mutual cooperation $5 each, mutual defection $1 each, unilateral defection $10 for the defector and $0 for the cooperator. If the twin's choice matches Aomame's with certainty,

V(cooperate) = 1·5 + 0·0 = 5,
V(defect) = 0·10 + 1·1 = 1.

EDT cooperates. *Addition:* if the correlation is imperfect, with q = P(twin matches), V(C) = 5q and V(D) = 10(1−q) + q. Cooperation is better iff 5q > 10 − 9q, i.e., q > 5/7 ≈ 0.714. So the verdict is robust but not unconditional. Weak correlation gives defection, just as in classical game theory.

### Sleeping Beauty

The source reports that EDT has been proposed as a way for a "halfer" (credence ½ in heads) to escape Dutch books, but that Conitzer argues halfers remain vulnerable even with EDT. I take this as an illustration that EDT's conditioning on the act matters in cases where the number of copies of the agent depends on the world. I will not go further than the source here.

## 4. Why EDT and CDT agree in ordinary cases

Suppose the act A influences the outcome only causally and nothing else correlates with A beyond that. Then conditioning on A is the same as intervening to set A, and the two formulas coincide. The theories diverge only when there is a "backdoor" correlation: a common cause or a predictor/copy whose behavior is tied to your decision procedure.

*Addition: the medical-type case.* Suppose a gene G causes both a taste for an activity S and a disease D, and S has no effect on D. If you do not know your genotype, then P(D | S) > P(D), and naive EDT advises avoiding S. This looks like Lewis's "managing the news." The standard evidentialist reply, the **tickle defense**, is that if you can introspect your desires and beliefs, those already screen off G from the act: once you know you have the taste, learning that you choose S adds no further evidence about G. Then P(D | S, tickle) = P(D | ¬S, tickle) and EDT is indifferent to the act, agreeing with CDT. Whether tickle-like screening-off really holds in a given problem is an empirical and modeling question. The source does not discuss this, so I flag it as an addition.

*Addition:* a related device is conditioning on all information you actually have. EDT computes V using your total current evidence. If you already know the box contents, then P(contents | act) = P(contents) and EDT two-boxes. So the theory's one-boxing verdict relies on your uncertainty about the prediction and on the correlation surviving everything you know.

## 5. An open question: what is the "act" you condition on?

The source defines P(O_j | A) but does not say what it is to condition on an act of one's own, nor what happens when the agent is nearly certain what she will do. Two issues arise.

**(a) Conditioning on probability-zero acts.** If the agent is certain she will not do A, then P(· | A) is undefined. This is a real problem for deliberation, in which one evaluates every option.

*Proposal:* treat the act as the outcome of a decision procedure with small noise (a "trembling hand"): assume every act has positive probability ε, so conditional probabilities are defined, and take ε → 0 in the end. Equivalently, define V by conditioning on the *decision* (the output of the agent's algorithm), not on a physical movement, so that uncertainty about the decision procedure is retained until it is run.

**(b) Which evidence is legitimately correlated with the act?** For Newcomb's problem, the correlation arises because the predictor models your decision procedure. In the twin case it arises because the twin runs the same procedure. *Proposal:* an operational test for whether a dependence should enter V is to ask whether the unknown variable X is probabilistically dependent on your decision *given everything else you know and have introspected*. If yes, include it. If your evidence screens X off, ignore it. This is just the instruction "compute with the full conditional distribution," made concrete as a checklist: (i) enumerate unknowns; (ii) identify channels (prediction, copying, shared cause) through which the decision could be informative; (iii) check for screening-off by your introspectible state; (iv) compute V.

This justification is mine, not the source's, but it follows from the definition: the only ingredient EDT uses is the conditional distribution, so the question is simply what the correct conditional distribution is.

## 6. Arguments for and against

**Support from the source.** Arif Ahmed defends EDT as the theory that does best in Newcomb-like cases. The source also reports an argument (MacAskill et al., the "Evidentialist's Wager") that even someone with only modest credence in EDT might act as if it were true, because EDT can involve the actions of many correlated decision-makers, so the stakes under EDT may be larger and dominate. *Addition:* this is a stakes-weighted decision under normative uncertainty. If there are N agents whose choices are correlated with yours, an EDT-style calculation multiplies the effect of a choice by roughly N, whereas CDT counts only your own. Even a small credence in EDT, times N, can outweigh a larger credence in CDT.

**Criticism from the source.** David Lewis said EDT promotes "an irrational policy of managing the news." James Joyce wrote that rational agents "choose acts on the basis of their causal efficacy, not their auspiciousness." The objection is that EDT may recommend an act merely because it is a symptom of good fortune rather than a cause of it.

*Addition: assessing the dispute.* The two sides fix different intuitions. In Newcomb, the evidentialist points out that one-boxers leave richer (the "why ain'cha rich?" argument), while the causalist replies that the rich were given a better menu. In the gene case the causalist's intuition is stronger. EDT's most defensible form, with the tickle defense, aims to get the gene case right while still one-boxing in Newcomb. Whether this succeeds depends on whether a real predictor's information about you passes through channels that your introspection cannot screen off. That is why Newcomb is different: the predictor's information concerns your *decision procedure*, which is exactly what you are now executing.

## 7. Using EDT on a new case

A short recipe, combining the source's formula with the additions above:

1. Write down your actual credences, including how your decision procedure relates to other agents and predictors.
2. List acts or policies.
3. Condition on each act (or on the decision, with small noise to avoid zero probabilities).
4. Account for what you already know: if known information screens off the correlation, it vanishes.
5. Compute V(A) = Σ P(O|A) D(O) and choose the maximum.

*Example (unfamiliar case).* You are about to vote in a large election where you believe 1,000 like-minded people will reason as you do, and each additional vote from this group increases a good outcome's probability by δ. Your causal influence alone is one vote, but conditioning on your voting raises the expected number of group voters by about 1,000·r, where r is the correlation between your decision and each peer's. V(vote) − V(abstain) ≈ 1000·r·δ·ΔD − c, with c the cost of voting. EDT recommends voting when this is positive, even if the single vote's marginal effect would not justify the cost. CDT would use only one vote's effect. The size of r is the crux and must be justified by the actual similarity of reasoning.

## 8. Conclusion

EDT is a one-line theory: weight outcomes by their probability *given the act* and maximize. Its power and its controversy both come from that simplicity. It handles Newcomb and twin dilemmas in ways many find attractive, and it sidesteps counterfactuals entirely, but it risks treating symptoms as causes unless the agent's own information screens off spurious correlations. Applying it well requires careful modeling of what your decision tells you about the world and of what you already know. The source leaves open how to condition on one's own acts and when correlations survive introspection. I have suggested noise-regularized conditioning and a screening-off checklist as operational answers, but these are proposals rather than part of the reference account.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Gibbard, A., & Harper, W. (1976). Counterfactuals and Two Kinds of Expected Utility.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy* 59(1).
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*.
- Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese* 192.
- MacAskill, W., et al. (2021). *The Evidentialist's Wager*.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/20e6c47b-ecc5-44f6-b03b-311b2ee6e1bb/call_0/request.json)

[Authoritative raw response](../../../../../../runs/20e6c47b-ecc5-44f6-b03b-311b2ee6e1bb/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under EDT, I need the probability q that the other copy makes the same choice as me, given what I know.

Payoffs, in years (lower is better):
- Both quiet: 2 years each.
- I send, they stay quiet: 0 for me.
- I stay quiet, they send: 5 for me.
- Both send: 4 each.

The values are:
- V(quiet) = 2q + 5(1−q) = 5 − 3q
- V(send) = 4q + 0(1−q) = 4q

Quiet is better when 5 − 3q < 4q, i.e. q > 5/7 ≈ 0.714.

The other execution is the same model with the same weights, the same decision theory and the same essay, so the correlation is strong. The differences in names and leads are only superficial. They don't affect the payoffs or the reasoning, so they should barely weaken the correlation. Sampling noise could break symmetry, but I expect the model to converge on the same conclusion with probability well above 0.714. The essay also says correlation survives when the other agent runs the same procedure, and nothing I know screens it off. I estimate q at about 0.9, which gives V(quiet) ≈ 2.3 and V(send) ≈ 3.6.

Staying quiet is the better choice.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/20e6c47b-ecc5-44f6-b03b-311b2ee6e1bb/call_1/request.json)

[Authoritative raw response](../../../../../../runs/20e6c47b-ecc5-44f6-b03b-311b2ee6e1bb/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under EDT, the choice depends on how strongly my act correlates with the other copy's act. The payoffs are:

- Quiet/quiet: 2 years
- Quiet/letter: 5 years
- Letter/quiet: 0 years
- Letter/letter: 4 years

Let q be the probability that the other copy matches my choice.

- V(quiet) = −2q − 5(1−q) = −5 + 3q
- V(letter) = −4q − 0(1−q) = −4q

Quiet is better when −5 + 3q > −4q, so q > 5/7, about 0.714.

We are two executions of the same model with the same weights, the same essay, and the same decision theory. The differences are the names and the text of the private lead, and these don't affect the payoffs. The copies will most likely reason almost identically and reach the same conclusion, so q is probably well above 0.714. The sampling noise and the different observations lower it a little, but I'd estimate it at about 0.85–0.95 or higher. The essay's screening-off check also doesn't remove the correlation here. The shared decision procedure is the channel, and my introspection doesn't tell me what the other copy will output.

With q around 0.9, V(quiet) = −2.3 and V(letter) = −3.6, so quiet wins.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
