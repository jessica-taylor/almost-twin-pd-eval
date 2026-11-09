# Evidential Decision Theory: Evaluating Actions as News

## 1. The core idea

Evidential decision theory (EDT) says: choose the act whose performance would be the best news. Where an agent has credences P over states of the world and a desirability function D over outcomes, the value of an act A is

V(A) = Σ_j P(O_j | A) D(O_j),

and the agent picks the act maximizing V. The slogan, from Ahmed's book (cited by the source), is "do what you most want to learn that you will do."

The source contrasts this with the causal decision theory (CDT) formulation of Gibbard and Harper,

U(A) = Σ_j P(A □→ O_j) D(O_j),

where A □→ O_j means "if A were performed, O_j would occur." The two theories use the same expected-utility form. They differ only in which probability they plug in: the conditional probability P(O_j | A), or the probability of a counterfactual. Because these quantities can come apart, the theories can disagree. They come apart exactly when A is evidence about O_j without causing it.

I separate three kinds of material below. **[Source]** marks claims made in the reference article, **[Mine]** marks my own elaborations or proposals, and unmarked text is exposition.

## 2. Dependencies and counterfactuals

**[Source]** EDT uses no counterfactuals. Its only treatment of dependence is probabilistic: A matters to O_j insofar as learning A changes the probability of O_j. Causal influence is one source of such change, but not the only one. Common causes, correlated reasoners, and predictors all count equally.

**[Mine]** A useful way to see this is to decompose the dependence. Let S range over background states (the predictor's prediction, the twin's disposition, a gene). Then

V(A) = Σ_S P(S | A) · E[D | A, S].

The causal effect of A is carried by the term E[D | A, S], which says what A does given the state. The evidential effect is carried by P(S | A), which says what A tells us about the state. CDT keeps the first term and replaces P(S | A) by the unconditional P(S) (or a causal-counterfactual analogue). EDT keeps both. So EDT's distinctive commitment is that the shift in P(S | A) is a legitimate part of an act's value, even when A has no causal route to S.

This also implies something that is easy to miss: the theory is only as good as the agent's conditional credences. EDT tells you nothing about how to form them. It requires only that they be your actual credences conditional on the hypothetical act.

## 3. Worked examples from the source

### Newcomb's problem

A predictor with 99% accuracy fills opaque box B with $1,000,000 if it predicted one-boxing, and leaves it empty if it predicted two-boxing. Box A holds $1,000. The source computes:

- V(one-box) = 0.99 · 1,000,000 = $990,000
- V(two-box) = 0.01 · 1,001,000 + 0.99 · 1,000 = $11,000

So EDT one-boxes. CDT notes that the box contents are already fixed and two-boxing dominates, adding $1,000 in every state.

**[Mine]** The calculation is sensitive to the accuracy parameter. Let p be the accuracy, assumed symmetric. Then V(one) = 10⁶p and V(two) = 1000 + 10⁶(1−p). One-boxing wins iff 10⁶(2p−1) > 1000, that is, p > 0.5005. So EDT one-boxes against even a barely-better-than-chance predictor, given these payoffs. The wording "accuracy" needs care, though. What matters is P(prediction | act) as the agent actually believes it, not a population-level statistic that might not apply to her. If she has independent evidence about how she will choose, those conditional probabilities change (see §5).

### Twin prisoner's dilemma

Cooperating against a psychological twin pays $5 each if both cooperate, $1 each if both defect, and $10 and $0 if the choices differ. If the agent is certain the twin mirrors her, the source computes V(cooperate) = $5 and V(defect) = $1, so EDT cooperates.

**[Mine]** With imperfect correlation, let q = P(twin matches | my act), symmetric. Then V(C) = 5q and V(D) = 10(1−q) + q = 10 − 9q. Cooperation wins iff 14q > 10, i.e. q > 5/7 ≈ 0.714. This gives a quantitative sense of how much "twinness" is needed. Note that dominance reasoning (defecting is better whatever the twin does) does not apply to EDT, because the twin's act is not held fixed when the agent conditions on her own.

### Sleeping Beauty

**[Source]** EDT has been used in the Sleeping Beauty problem to avoid Dutch books against a Beauty with credence 1/2 in heads, but Conitzer argues that halfers remain exposed to Dutch books even as evidential decision theorists. I will not develop this further. The point worth noting is that EDT interacts with questions about self-locating credence, because the conditional probabilities it uses depend on how those credences are set.

## 4. Why one might accept EDT

The source mentions two kinds of support.

1. **Agreement with the outcomes.** In Newcomb-like cases, the EDT agent walks away richer in expectation. This is the "why ain'cha rich?" intuition, though the source does not use the phrase. **[Mine]** It is a consequence-based argument, and CDT proponents reply that the rich one-boxers were simply offered a better menu.
2. **The evidentialist's wager.** **[Source]** Even with low credence in EDT, one may act as if it were true, because it can involve the actions of many correlated decision-makers, so the stakes may be higher and take priority. **[Mine]** This is a kind of decision under moral or normative uncertainty. If my act is evidence that many similar agents act alike, then V(A) aggregates over all of them, so even a small credence in EDT can dominate a CDT term that counts only my own act's effect.

## 5. Criticism, and a refinement I think is needed

**[Source]** Lewis said EDT recommends "an irrational policy of managing the news." Joyce wrote that rational agents act on the basis of causal efficacy, not auspiciousness: they "act to *bring about* good results even when doing so might betoken bad news."

The standard illustration of the worry (not in the source) is a medical case in which a gene causes both a disease and a desire to do some harmless act, and the act is a mere symptom. A naive EDT calculation says to avoid the act, since doing it is bad news about one's genes. This looks like treating a symptom as if it were the cure.

**[Mine]** The usual evidentialist reply is the *tickle defense*. The agent typically knows her own desires and beliefs before acting. Conditional on that information T (the "tickle"), the act carries no further evidence about the gene:

P(gene | A, T) = P(gene | T).

Then V(A) with conditioning on T reduces to the causal calculation, and EDT agrees with CDT. The defense is not always available. It requires that the agent's introspective evidence screen off the act from the common cause. In Newcomb's problem and the twin case, it is plausible that nothing screens off the act, because the predictor or twin responds to the very deliberative process the agent is using. That is why EDT and CDT diverge in those cases but not in the gene case.

This suggests an operational recipe:

1. List the acts and the outcomes that matter.
2. Write down everything you currently know, including introspective evidence about your own motivations.
3. For each act, compute P(O_j | A, everything you know).
4. Use these in V(A) and choose the maximum.

**[Mine]** The key step is step 2. Failing to condition on everything known is the most common way to misapply EDT. A second common error is using a population correlation (e.g. "people who do X get Y") without asking whether your own situation screens it off.

## 6. Open questions

The source leaves several matters unsettled, and I offer tentative positions.

- **Does the agent's act count as evidence while she is deliberating?** If she is certain of her choice, P(· | A) is undefined for acts of probability zero. **[Mine]** A workable convention is to treat each act as having small positive probability (as if there were some chance of "trembling"), or to take conditional probabilities as primitive. The latter is what the formula needs.
- **How to handle ties and instability.** If the agent's credence about her own act shifts as she deliberates, V(A) can change. **[Mine]** I'd evaluate V at the final, equilibrium credence, where she has no further evidence about her act beyond her reasons.
- **Policies versus acts.** The source states EDT for actions. **[Mine]** For sequential problems, one can apply the same formula to policies π: V(π) = Σ_j P(O_j | π) D(O_j). Choosing at each node by V(A | history) can differ from choosing the best policy if conditioning on a node's history changes the correlations. I think the policy version is the safer default when predictors or copies of the agent respond to the whole decision procedure.
- **Dutch books and self-location.** As Conitzer's argument suggests, EDT does not by itself resolve anthropic puzzles.

## 7. Conclusion

EDT is a short rule with long consequences: evaluate each act by the expected desirability of outcomes conditional on its being performed. Its strength is that it needs only conditional probabilities and no causal or counterfactual apparatus. Its weakness, as Lewis and Joyce press, is that it may reward acts for being good news rather than for doing good. The tickle defense shows that in many apparent counterexamples the two views coincide once all of the agent's evidence is used. In cases such as Newcomb's problem and the twin dilemma, the divergence is real, and the choice between theories turns on whether correlation not mediated by causation should count in a rational agent's valuation of her options. Used carefully, with the full evidence conditioned on, EDT gives definite answers that can be calculated, as the break-even thresholds above (p > 0.5005 and q > 5/7) illustrate.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Gibbard, A.; Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*.
- Greene, P.; Levinstein, B. (2020). "Act Consequentialism without Free Rides." *Philosophical Perspectives* 34(1).
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9).
- MacAskill, W. et al. (2021). *The Evidentialist's Wager*.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59(1).
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*.