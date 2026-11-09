# Evidential Decision Theory: Choosing Actions as News

## 1. The core idea

Evidential decision theory (EDT) says: among the available actions, pick the one whose *news value* is highest. The news value of an action A is the expected desirability of the world, given that you learn A was performed. The slogan, which the source attributes to Ahmed, is "do what you most want to learn that you will do."

The formula, from Gibbard and Harper (1976), is

V(A) = Σ_j P(O_j | A) · D(O_j),

where the O_j are mutually exclusive, exhaustive outcomes, D is desirability (utility), and P(O_j | A) is the ordinary conditional probability of O_j given A. The recommendation is argmax_A V(A).

The contrast, also from the source, is causal decision theory (CDT):

U(A) = Σ_j P(A □→ O_j) · D(O_j),

where A □→ O_j is the counterfactual "if A were performed, O_j would occur." The two quantities differ whenever A is correlated with O_j by something other than A's causal influence on O_j.

I will separate three things: (i) claims from the source, (ii) standard material I add, and (iii) my own operational suggestions. I flag these as they come up.

## 2. How EDT treats dependence

The key feature is that EDT uses *all* probabilistic dependence between act and outcome, with no distinction among its sources. Suppose A and O are dependent. There are three typical reasons:

1. A causes O (the usual, welcome case).
2. A common cause C influences both (a "common-cause" correlation).
3. A and O are both outputs of similar processes, or one is a reliable predictor of the other (Newcomb-type and twin-type cases).

For EDT, all three contribute to P(O | A) and therefore to V(A). CDT counts only the first. This is why the theories agree in "ordinary" decisions, where the correlations you care about are causal, and diverge in decisions where non-causal correlation is strong.

Mathematically, write the unknown state of the world as S with P(S), and suppose outcome is a function of (A, S), O = f(A, S). Then

V(A) = Σ_S P(S | A) · D(f(A, S)).

A CDT-style calculation with the same state partition (with S causally independent of A) would be

U(A) = Σ_S P(S) · D(f(A, S)).

The only difference is P(S | A) versus P(S). Thus EDT differs from CDT exactly through the evidential relevance of the act to the states. When A is probabilistically independent of S, the two coincide.

## 3. Worked examples from the source

### Newcomb's problem

Box A holds $1,000 visibly. Box B holds $1,000,000 if the predictor predicted you would take only B, and $0 otherwise. The predictor is 99% accurate. Then

V(one-box) = 0.99 · 1,000,000 + 0.01 · 0 = $990,000,
V(two-box) = 0.01 · 1,001,000 + 0.99 · 1,000 = $11,000.

EDT one-boxes. CDT argues the contents are already fixed, so two-boxing yields $1,000 more in either state, and recommends two-boxing.

A general threshold: let the predictor's accuracy be p (assume symmetric). V(one) = p·M, V(two) = (1−p)(M+K) + pK = (1−p)M + K, with M = 1,000,000 and K = 1,000. One-boxing wins iff p·M > (1−p)M + K, i.e. p > ½ + K/(2M) = 0.5005. So EDT one-boxes against any predictor barely better than chance, which is worth noticing. (This computation is my own extension.)

### Twin prisoner's dilemma

Payoffs: (C,C) gives $5 each, (D,D) gives $1 each, and unilateral defection gives $10 to the defector and $0 to the cooperator. If Aomame's twin is a perfect copy, P(twin C | I C) = 1, so V(C) = 5 and V(D) = 1. EDT cooperates. CDT defects, since her choice does not causally affect the twin's room and defection dominates.

With imperfect correlation, let q = P(twin matches me). Then V(C) = 5q, V(D) = 10(1−q) + q = 10 − 9q. Cooperation is better iff 5q > 10 − 9q, i.e. q > 5/7 ≈ 0.714. (Again my own computation.) So the degree of evidential coupling matters quantitatively, and the verdict flips at a definite threshold.

### Sleeping Beauty

The source notes that EDT has been invoked to defuse Dutch-book arguments against a credence of ½ in heads, but Conitzer argues that halfers who are evidential decision theorists remain exploitable. I take no stand here beyond noting that the case shows EDT interacting with questions about credence, not only with utilities. The dispute is about which probabilities enter V, and V is only as good as the P it is fed.

## 4. A practical procedure

Here is how I would apply EDT to an unfamiliar case. This is my operationalization, not a procedure stated in the source.

1. **List the actions** available, as precisely as possible.
2. **Choose outcome descriptions** fine-grained enough to capture everything you value.
3. **Model your credences as a joint distribution** over actions, hidden states and outcomes.
4. **Condition on each action** and compute expected desirability.
5. **Pick the maximum.**

The delicate step is 3–4: what is the correct conditional distribution P(· | A)? The source says "the conditional probability of O_j given that action A occurs," but does not say what information you condition against. That brings us to the main open question.

## 5. An open question: what counts as evidence when the agent is deliberating?

If you already know your own mind well, then your act carries little news. In that case P(S | A) ≈ P(S), and EDT collapses to CDT. This is the idea behind the "tickle defense" (standard literature, not in the source): in a case such as a medical correlation between a gene and a disposition, if the agent can introspect the desire or belief that causes the choice, the act is screened off from the hidden state by that introspective information. The conditional probability given both the act and the tickle equals that given only the tickle.

The source is silent on this. Here is the operational interpretation I would defend:

- Condition on **everything you actually know at decision time**, including introspective knowledge of your own beliefs and desires. Then evidential relevance remains only to the extent the act reveals something *beyond* what you know.
- In Newcomb's problem as stated, the predictor is described as reliably predicting *the player's choice*, with no assumption that the player's inner state screens it off. So the dependence survives conditioning and EDT one-boxes. The same holds in the twin case, where the twin's behavior is by stipulation determined by the same reasoning as yours.
- In medical-style cases where the correlation runs through a trait you can already inspect, the dependence disappears under conditioning and EDT behaves like CDT.

This reading justifies the theory's verdicts in a principled way and shows the divergence from CDT is confined to cases where the correlation truly survives your self-knowledge. It is an interpretation, however, and critics dispute whether real agents ever lack such screening-off, or conversely whether deliberation can ever be fully transparent.

A related uncertainty: **is the "act" a decision, a disposition, or a physical event?** Conditioning on "I choose A" versus "I execute A" changes which correlations are live (for instance, trembling-hand failures weaken the link between decision and predicted behavior). I would take the act to be the decision-relevant event the predictor or twin is correlated with, and model any slip between choice and execution explicitly.

## 6. Treatment of counterfactuals

EDT does not use counterfactuals in its valuation. This is a structural point: V(A) needs only a probability distribution and conditioning. CDT needs additionally either causal graphs or counterfactual conditionals with their own probabilities. Hence EDT is, in one sense, more parsimonious: no causal model is required. In another sense, this is a cost, since it ignores information in a causal model that a decision-maker may have and that seems relevant to "bringing about" outcomes.

The causal-model version of CDT can be expressed as Pearl's do-operator: U(A) = Σ_j P(O_j | do(A)) D(O_j). EDT replaces do(A) by observing A. In a graph where A has no parents that are confounders, these coincide. Where there is a confounder C → A and C → O, conditioning gives P(O | A) = Σ_C P(C | A) P(O | A, C), while intervention gives Σ_C P(C) P(O | A, C). The extra weight shift from P(C) to P(C | A) is exactly the evidential "news" effect.

## 7. An illustration where the verdicts split sharply, and a case where EDT looks good

Consider a toy confounding example (mine). A hidden gene G (probability 0.5) raises both the chance of choosing to smoke and the chance of cancer; smoking itself has no causal effect on cancer but gives a small pleasure ε. Suppose the gene fully determines the act (no tickle, no screening). Then P(G | smoke) = 1, and EDT predicts that smoking is bad news: it avoids smoking if the cancer loss exceeds ε. CDT smokes, since smoking does not cause cancer. Many find CDT right here, and this is the standard objection to EDT (Lewis's "managing the news": you are acting to receive reassuring evidence rather than to change anything). If instead the gene works through a desire you can feel, screening-off reduces EDT to CDT, as in section 5. So the strength of the objection depends on how plausible it is that the correlation truly bypasses deliberation.

On the other side, in cases where correlations come from shared reasoning, as with twins, copies of an agent, or accurate predictors of your reasoning, dismissing the dependence seems the less natural position. Defecting against an exact copy and receiving $1 where cooperation yields $5 looks like a systematic loss.

## 8. Arguments for and against

**Supporting (from the source).** Even if one's credence in EDT is below one half, the "evidentialist's wager" (MacAskill et al.) argues that acting as if EDT were true may be reasonable, because EDT recommendations can involve the actions of many correlated decision-makers, so the stakes are higher and dominate in expected-choiceworthiness terms under moral/decision-theoretic uncertainty. I add a caveat: that argument depends on the correlations being large and on the stakes comparison being appropriate under theory uncertainty, both of which are contestable.

**Criticism (from the source).** Lewis: EDT promotes "an irrational policy of managing the news." Joyce: rational agents act on causal efficacy rather than auspiciousness: "they act to *bring about* good results even when doing so might betoken bad news."

**My assessment.** The dispute is partly about what rationality is *for*. If it is for causing good outcomes, the causalist is right in the smoking-gene case. If it is for being the kind of agent who does well in the situations one actually faces, including ones with predictors, the evidentialist has the better record in Newcomb and twin cases. A possible reconciliation is to treat the agent's choice as the output of a policy, so correlations arising from the policy count, which is a move later theories explore; this goes beyond the source.

## 9. Summary of the procedure and pitfalls

- Compute V(A) = Σ P(O | A) D(O), using conditional probabilities given the act *and* your relevant self-knowledge.
- Check whether the act is probabilistically relevant to the states beyond what you know. If not, EDT agrees with CDT.
- If so, quantify the dependence (accuracy p, correlation q); verdicts typically flip at a threshold, as in the Newcomb value p > 0.5005 and the twin value q > 5/7.
- Remember that EDT is only as good as the conditional probabilities supplied, especially in anthropic settings such as Sleeping Beauty.

## 10. Conclusion

EDT replaces the question "what will my act cause?" with "what would my act tell me?" Its formal core is a single change, conditioning on A rather than intervening on A, and this one change yields one-boxing in Newcomb, cooperation with a twin, and sometimes counterintuitive abstention in confounded cases. How troubling those verdicts are depends largely on one issue the source leaves open: how much of the correlation between act and world survives the agent's knowledge of her own deliberation. Where it survives, EDT's advice is often compelling; where it does not, EDT and CDT converge, and the remaining disagreement is mainly philosophical.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Gibbard, A., & Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy* 59(1).
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese* 192(9).
- MacAskill, W., et al. (2021). *The Evidentialist's Wager*.
- Greene, P., & Levinstein, B. (2020). Act consequentialism without free rides. *Philosophical Perspectives* 34(1).
- Wolpert, D. H., & Benford, G. (2013). The lesson of Newcomb's paradox. *Synthese* 190(9).