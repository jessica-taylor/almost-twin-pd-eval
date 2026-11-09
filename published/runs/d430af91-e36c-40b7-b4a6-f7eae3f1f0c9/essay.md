# Evidential Decision Theory: Choosing Actions as News

## 1. The core idea

Evidential decision theory (EDT) says to treat your own action as a piece of evidence about the world and to pick the action whose occurrence you would most welcome learning about. The source puts it as "do what you most want to learn that you will do." Each act is scored by its *news value*: the expected desirability of outcomes, conditional on the act being performed.

This is a claim about how to evaluate acts, not a claim that acts cause good outcomes. The theory is interesting because the two notions come apart. An act can be good news without being causally efficacious, and the reverse.

## 2. Formal definition

Fix a set of available acts 𝒜, a set of mutually exclusive and exhaustive outcomes {O_j}, a credence function P, and a desirability (utility) function D. The source, following Gibbard and Harper (1976), gives

V(A) = Σ_j P(O_j | A) · D(O_j).

EDT recommends argmax_{A∈𝒜} V(A).

The contrasting causal formulation replaces the conditional probability with the probability of a counterfactual:

U(A) = Σ_j P(A □→ O_j) · D(O_j).

The source's point is that P(O_j | A) and P(A □→ O_j) need not be equal, so V and U can rank acts differently.

**A useful decomposition (my addition).** Introduce a partition of background states S_k that are causally independent of the act, such as "the box already contains the money." Then

V(A) = Σ_k P(S_k | A) · E[D | A, S_k].

CDT uses the same inner terms but weights states by the unconditional P(S_k). EDT and CDT therefore differ exactly when the act is evidentially relevant to causally upstream or independent states, that is, when P(S_k | A) ≠ P(S_k). If the act carries no information about such states, the two agree. This explains the source's remark that the theories "agree in many cases."

## 3. How EDT treats dependencies and counterfactuals

EDT uses no counterfactuals. Every dependency, whether causal, common-cause, or correlational through similarity of reasoners, enters only through the conditional distribution P(· | A). Two consequences follow.

1. **Causal influence is not privileged.** If A raises the probability of a good outcome, it does so in P(· | A) like any other correlation. EDT needs no separate causal model, although a causal model is often a convenient way to compute the conditional probabilities.
2. **Correlation is not discounted.** Evidence that flows backward through a common cause, or sideways to a similar agent, counts fully. This is what Lewis calls "managing the news" and what Joyce criticizes: rational agents, he says, "act to *bring about* good results even when doing so might betoken bad news."

## 4. Worked examples from the source

**Newcomb's problem.** The predictor is 99% accurate. Box A holds $1,000, and box B holds $1,000,000 iff one-boxing was predicted.

- V(one-box) = 0.99 · 10⁶ = $990,000.
- V(two-box) = 0.01 · 1,001,000 + 0.99 · 1,000 = $11,000.

EDT one-boxes. Writing a for the predictor's accuracy, one-boxing wins when a·10⁶ > (1−a)·10⁶ + 1000, that is, a > 0.5005. So the answer is robust across almost all predictor accuracies.

**Twin prisoner's dilemma.** Payoffs are (C,C) = $5 each, (D,D) = $1 each, and (D,C) = $10 for the defector and $0 for the cooperator. If the twin's action matches mine with certainty, V(C) = 5 and V(D) = 1, so EDT cooperates. With imperfect correlation, let q = P(twin matches | my act). Then V(C) = 5q and V(D) = 10(1−q) + q = 10 − 9q. Cooperation wins when 5q > 10 − 9q, i.e. q > 5/7. The threshold shows that EDT is sensitive to the *strength* of evidential coupling, not merely its presence.

**Sleeping Beauty.** The source notes only that EDT has been invoked to defuse Dutch books against a credence of 1/2 in heads, and that Conitzer argues halfers remain exploitable even so. This shows that EDT's conditioning on one's own act interacts with questions about self-locating credence, which the formalism above does not settle.

## 5. Where the source leaves questions open

The source gives the formula and examples but is silent on several matters that are important in practice. The following are my own proposals, not claims of the source.

**5.1 What counts as "the act"?** Conditioning on "A is performed" is ambiguous. Is it the physical event, the decision, or the disposition behind it? In Newcomb's problem the predictor tracks the agent's dispositions, so the evidence is carried by the kind of agent one is, and the act is merely a symptom.

**5.2 The "tickle defense" and screening off.** Suppose a common cause C (a gene, a mood, a disposition) influences both the act and the outcome, as in the standard smoking-gene case. If the agent can introspect C, or the beliefs and desires that C operates through, then P(O | A, C) = P(O | C), and the act carries no further evidence. EDT then agrees with CDT. A principled operational rule is therefore:

> Compute V(A) using the agent's *full* current credal state, including everything introspectively known. Condition on A only in addition to that.

In the formulas, P is always the agent's actual credence, and information the agent already has should not be treated as unknown. In Newcomb's problem this does not screen anything off, because the predictor's evidence is not something the agent can access except through the choice itself. This is why EDT one-boxes there while the tickle defense can make it indifferent to evidentially symptomatic acts elsewhere. Whether this defense always succeeds is contested; I treat it as a default that is plausible but not guaranteed.

**5.3 Deliberation dynamics.** If the agent's credence about their own act is part of P, then deliberation can shift P(A) toward 0 or 1, and conditioning on a probability-zero act is undefined. A standard repair is to assume small positive probabilities for all acts (as if from "trembling hands"), or to define V(A) through a limit. I propose the first, since it is simple and keeps V well defined.

**5.4 Policies.** For sequential problems, EDT can be applied to whole policies π, with V(π) = Σ_j P(O_j | I follow π) D(O_j), or to acts at each node. These can diverge when the later self's evidence differs from the earlier one's. I suggest evaluating policies when other agents (predictors, copies) respond to the agent's type rather than to individual choices, and acts when only the present choice is evidentially relevant.

## 6. Applying EDT to unfamiliar cases: a procedure

1. List the acts and outcomes, and specify D.
2. Specify your actual credences, including everything you introspectively know and any correlation with predictors, copies, or similar reasoners.
3. For each act, compute P(O_j | A). If a causal graph is available, identify which paths run backward (via common causes) and sideways (via similar agents). Check whether known variables screen them off.
4. Compute V(A) and choose the maximum, breaking ties arbitrarily.
5. Sanity check: if the act has no evidential bearing on anything beyond its causal effects, V should coincide with the causal expectation.

**Example, the smoking lesion.** Suppose a lesion causes both a taste for smoking and cancer, while smoking is harmless but enjoyable. Without screening off, smoking is bad news, so a naive EDT calculation would abstain. If the agent knows their own desires, which mediate the lesion's effect, then P(cancer | smoke, desire) = P(cancer | desire), and V favors smoking. This agrees with intuition, and it shows that EDT's verdicts depend on what the agent already knows, not only on population statistics.

**Example, many correlated agents.** Suppose a million similar voters each decide whether to vote, with strong mutual correlation. Under EDT my choice is evidence about everyone's, so V(vote) includes the shifted expectation over their votes. This is the structure behind the source's remark (MacAskill et al.) that EDT can involve many correlated decision-makers and so may have higher stakes. The "Evidentialist's Wager" argues that even someone with modest credence in EDT should weight it heavily because the stakes are larger. That is an argument about decision-making under normative uncertainty and is not itself a defense of EDT's correctness.

## 7. Criticisms and replies

Lewis's charge is that EDT recommends "managing the news": choosing acts for the good tidings they signal rather than the good they do. Joyce's version is that rational choice tracks causal efficacy rather than auspiciousness.

A defender (Ahmed, in the source's primary reference) can respond in two ways. First, in the paradigm cases, the "news" is not an illusion. In Newcomb's problem one-boxers really do end up richer on average, so the policy EDT endorses is the one that does better. Second, in the cases where managing the news seems absurd (smoking lesion), the tickle defense suggests EDT does not recommend it after all.

The critic can reply that when the agent really lacks screening-off information, EDT does recommend evidentially-motivated acts, such as paying to avoid learning bad news or acting in ways that cannot influence the outcome. Whether such recommendations are irrational is where the theories fundamentally disagree. I think the honest summary is that EDT is hostage to how much the agent can introspect, which is both its flexibility and its vulnerability.

## 8. Conclusion

EDT evaluates each act by V(A) = Σ_j P(O_j | A) D(O_j), using only the agent's conditional credences and no counterfactuals. Its verdicts differ from those of causal decision theory exactly when acts are evidentially correlated with causally independent features of the world. In the source's examples this yields one-boxing and cooperation with a twin, with thresholds (a > 0.5005, q > 5/7) that quantify how strong the correlation must be. Operationally, one must be careful about what the agent already knows, because screening off can dissolve apparent conflicts with CDT, and about zero-probability acts. The philosophical dispute remains whether good news, rather than good causation, is the proper guide to action.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Gibbard, A. & Harper, W. (1976). Counterfactuals and Two Kinds of Expected Utility.
- Lewis, D. (1981). Causal decision theory. *Australasian J. Philosophy* 59(1).
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese* 192(9).
- MacAskill, W. et al. (2021). *The Evidentialist's Wager*.