# Causal Decision Theory: Choosing by Expected Causal Consequences

Causal decision theory (CDT) is a school of thought in decision theory holding that a rational agent should choose the action that causes the best expected outcome. The contrast is with evidential decision theory (EDT), which chooses the action that would be the best *news*—the action whose occurrence would be most strongly associated with good outcomes, conditional on observing that it was taken. The supplied reference article summarizes this contrast and gives the classical counterfactual formulation due to Gibbard and Harper (1981). My aim here is to make the theory precise enough to apply, to explain how it treats dependencies and counterfactuals, and to develop a reasonable operational interpretation where the source leaves the theory under-specified.

I will distinguish between claims made by the source and additional assumptions I introduce. In particular, the source gives the core CDT formula but, as it notes, does not specify an algorithm for computing counterfactual probabilities. I will suggest that modern causal-model machinery—Pearl-style interventions and structural counterfactuals—provides a natural operational reading, although this is an addition to the source rather than a claim contained in it.

---

## 1. Expected utility: evidential versus causal

Consider a finite decision problem with possible actions \(A \in \mathcal A\), outcomes \(O_j \in \mathcal O\), and a desirability or utility function \(D(O_j)\). An evidential decision theorist evaluates an action by conditional expected utility:

\[
U_E(A)=\sum_j P(O_j \mid A)D(O_j).
\]

Here \(P(O_j\mid A)\) is the ordinary conditional probability of outcome \(O_j\) given that the agent performs \(A\). This quantity captures the *evidential* bearing of the action: if we learned that the agent had done \(A\), how probable would \(O_j\) be?

CDT instead uses the formula given in the source, attributed to Gibbard and Harper:

\[
U_C(A)=\sum_j P(A \to O_j)D(O_j),
\]

where \(P(A \to O_j)\) is the probability of the counterfactual: “if the agent were to do \(A\), then \(O_j\) would obtain.” To avoid confusion with material implication, it is common to write this as \(A \mathbin{\Box\!\to} O_j\). Thus:

\[
U_C(A)=\sum_j P(A \mathbin{\Box\!\to} O_j)D(O_j).
\]

The essential claim is that rational choice should be guided by the probabilities of what the action would *bring about*, not merely by what the action would *indicate*.

The source notes that Lewis proved the probability of a conditional need not equal the corresponding conditional probability:

\[
P(A \mathbin{\Box\!\to} O_j) \neq P(O_j\mid A)
\]

in general. If equality always held, CDT and EDT would collapse into the same theory. But they can come apart when the action is evidence about background conditions that also affect outcomes, without causing those background conditions.

A simple way to express the difference is through “dependency hypotheses.” Let \(K\) be a variable describing a complete causal structure: which actions causally influence which outcomes, and with what probabilities. Then a CDT evaluation can be written schematically as

\[
U_C(A)=\sum_k P(K=k)\sum_j P(O_j \mid do(A), K=k)D(O_j),
\]

where \(do(A)\) denotes an intervention setting the action to \(A\). EDT, by contrast, effectively allows the act \(A\) to change the agent’s credence in \(K\):

\[
U_E(A)=\sum_k P(K=k \mid A)\sum_j P(O_j \mid A, K=k)D(O_j).
\]

The source does not use the \(do\)-operator; that is my modern reformulation. But it captures the idea the source expresses: CDT evaluates consequences while holding fixed the agent’s views about the causal structure of the world, whereas EDT lets the supposed act serve as evidence about that structure.

---

## 2. Counterfactual probabilities and their interpretation

The formal core of CDT is counterfactual. The quantity \(P(A \mathbin{\Box\!\to} O_j)\) is not the probability that \(A\) is followed by \(O_j\) in the actual course of events; it is the probability that, were \(A\) performed, \(O_j\) would result.

The source mentions Lewis’s “imaging” proposal. On an imaging semantics, one evaluates \(P(A \mathbin{\Box\!\to} O_j)\) by moving probability mass from each possible world \(w\) to the closest possible world \(w_A\) in which \(A\) is true, and then asking how much probability lands in worlds where \(O_j\) is true:

\[
P(A \mathbin{\Box\!\to} O_j)
=
\sum_w P(w)\,\mathbf 1[O_j \text{ holds in the closest } A\text{-world to } w].
\]

More generally one may distribute mass probabilistically among close \(A\)-worlds. The difficulty, as the source notes, is that this requires a primitive notion of closeness among worlds and may invite regress: to know what we would believe if certain of \(A\), we may need further conditional beliefs.

A more operational approach, which I propose as a supplement to the source, is to use a structural causal model. Such a model consists of variables, background exogenous variables \(U\), and structural equations determining each variable from its causes. An intervention \(do(A=a)\) replaces the structural equation for \(A\) with the constant equation \(A=a\). The counterfactual probability of outcome \(O_j\) under action \(a\) is then

\[
P(O_j(a)) = P_U\bigl(O_j(a,U)=O_j\bigr),
\]

or, conditional on evidence \(E\),

\[
P(O_j(a)\mid E)
=
\int \mathbf 1[O_j(a,u)=O_j]\,P(u\mid E)\,du.
\]

The CDT value becomes

\[
U_C(a\mid E)
=
\sum_j P(O_j(a)\mid E)D(O_j).
\]

This gives a clear recipe:

1. Specify the relevant causal structure.
2. Update on the agent’s actual evidence \(E\).
3. Intervene on the action variable.
4. Compute the resulting distribution over outcomes.
5. Take the expectation of utility.

This procedure is not stated in the source, but it is a natural way to make CDT applicable to unfamiliar cases.

---

## 3. Holding fixed what should be held fixed

The central philosophical motivation of CDT is that an action should not be chosen merely because it is evidence for favorable conditions. If a choice is correlated with a good outcome only because both are effects of a common cause, then performing the choice does not necessarily produce the good outcome.

The source’s King David example illustrates this. David wants Bathsheba but fears that summoning her may provoke revolt. He has learned that kings are either charismatic or uncharismatic. Charismatic kings tend to act justly and rarely face successful revolts; uncharismatic kings tend to act unjustly and often face successful revolts. But unjust acts themselves do not cause revolts; rather, an uncharismatic king’s bearing causes revolts. David does not know whether he is charismatic.

Let \(C\) be the proposition that David is charismatic, \(A\) the act of summoning Bathsheba, and \(R\) a successful revolt. The causal structure is roughly:

\[
C \to A,\qquad C \to R,
\]

but not

\[
A \to R.
\]

That is, charisma influences both David’s likely action and the probability of revolt, but the action itself does not cause revolt. If summoning gives David some direct benefit \(b\), and revolt has cost \(L\), with \(P(R\mid C)=r_C\) and \(P(R\mid \neg C)=r_{\neg C}\), then CDT compares:

\[
U_C(A)=b-L\bigl[P(C)r_C+P(\neg C)r_{\neg C}\bigr],
\]

\[
U_C(\neg A)=-L\bigl[P(C)r_C+P(\neg C)r_{\neg C}\bigr].
\]

Since the revolt term is the same in both expressions, CDT recommends summoning if \(b>0\). EDT, however, allows \(A\) to serve as evidence that David is uncharismatic. If summoning is highly indicative of uncharismaticness, EDT may recommend abstaining because \(P(R\mid A)\) is high. The source says EDT recommends abstention while CDT recommends sending for Bathsheba.

This example displays the characteristic CDT move: hold fixed the background causal hypothesis, especially variables such as David’s charisma that cannot be changed by the action, and evaluate only the action’s causal consequences.

---

## 4. Newcomb’s problem

The most famous test case is Newcomb’s problem. The source describes it as follows. A highly reliable predictor has already predicted whether the player will take both boxes or only one. Box A visibly contains \$1,000. Box B contains \$1,000,000 if the predictor predicted one-boxing, and nothing if the predictor predicted two-boxing. The player now chooses whether to take both boxes or only box B.

Let \(P\) denote the predictor’s prediction and \(B\) the content of box B. If the prediction has already been made and there is no backward causation, the causal graph is:

\[
U \to P,\qquad U \to A,\qquad P \to B,
\]

where \(U\) represents whatever facts about the player allow the predictor to predict. The current action \(A\) does not cause \(P\) or \(B\). Under intervention, box B’s content is fixed:

\[
U_C(\text{two-box}) = U_C(\text{one-box}) + 1000.
\]

Therefore two-boxing dominates one-boxing in every possible state of box B. If box B is empty, two-boxing yields \$1,000 while one-boxing yields \$0. If box B is full, two-boxing yields \$1,001,000 while one-boxing yields \$1,000,000. CDT therefore recommends taking both boxes.

EDT reasons differently. One-boxing is strong evidence that the predictor predicted one-boxing, so conditional on one-boxing, box B is probably full. Two-boxing is strong evidence that the predictor predicted two-boxing, so conditional on two-boxing, box B is probably empty. With a predictor accurate with probability \(q=0.99\), EDT approximately compares:

\[
U_E(\text{one-box}) \approx q\cdot 1{,}000{,}000,
\]

\[
U_E(\text{two-box}) \approx q\cdot 1{,}000 + (1-q)\cdot 1{,}001{,}000.
\]

For \(q=0.99\), EDT strongly favors one-boxing. The source notes that philosophers disagree about whether one-boxing or two-boxing is rational, but that many philosophers prefer CDT when forced to choose between the two theories.

From the CDT perspective, the crucial point is not that two-boxing yields better evidence, but that the act cannot causally improve the content of box B once the prediction is fixed. If the predictor’s prediction is already in the past, the only causal effect of taking both boxes is to add the visible \$1,000.

---

## 5. Policies, not merely one-shot actions

The source mainly discusses single actions, but decision problems often involve policies: rules mapping information states to actions. CDT can be extended naturally to policies.

Suppose a policy \(\pi\) specifies actions at one or more decision points. In a causal model, the policy corresponds to setting one or more decision variables according to \(\pi\). The expected utility of the policy is

\[
U_C(\pi\mid E)
=
\sum_u P(u\mid E)D\bigl(O_\pi(u)\bigr),
\]

where \(O_\pi(u)\) is the outcome produced when the structural equations for the decision variables are replaced by the policy \(\pi\), while the rest of the causal system operates normally.

This gives a practical procedure for evaluating policies:

1. Represent the world by a causal model, including predictors, other agents, and relevant background variables.
2. Condition on evidence \(E\) available before the policy is adopted.
3. Replace the decision rules by the candidate policy.
4. Propagate the model forward to obtain outcomes.
5. Choose the policy with maximal expected utility.

One subtlety is whether the policy is chosen before or after other agents form predictions. If a predictor has already made a prediction about the agent’s action, CDT normally holds that prediction fixed when evaluating the current action. But if the agent can choose a policy before the predictor acts, then the policy may causally influence the predictor’s prediction. In that case, CDT may recommend adopting a one-boxing disposition in Newcomb’s problem, even though it recommends two-boxing at the later moment when the boxes are already fixed. This is not a contradiction: the causal structure of the choice has changed.

This point is my own elaboration, but it follows naturally from the interventionist reading of CDT.

---

## 6. Death in Damascus and related counterexamples

The source discusses several alleged counterexamples to CDT. One is Death in Damascus. Death is a reliable predictor who will wait tomorrow where the agent will be. The agent can stay in Damascus or flee to Aleppo. If Death predicts correctly, fleeing may seem pointless; if the agent learns that Death is currently in Damascus, fleeing may seem attractive, but Death predicted that too.

The difficulty is that the agent’s action is strongly correlated with Death’s prediction, but CDT is reluctant to treat the action as causing the prediction. If Death’s prediction is fixed by prior causes, then intervening on the agent’s location does not change Death’s location. If the agent has no reason to think one location is safer than the other, CDT may be indifferent, or may be driven by small costs and benefits. But if the agent’s deliberation produces shifting expectations, CDT can appear unstable.

The source also mentions variants in which CDT agents voluntarily lose money or forgo guaranteed payoffs. These cases are important because they suggest that CDT can fail not only in exotic philosophical puzzles but in decision problems involving prediction, correlation, and strategic interaction.

A related case discussed in the source is the Psychopath Button. Paul can press a button that kills all psychopaths. Paul believes a world without psychopaths would be much better, but he also believes that only a psychopath would press the button. He strongly prefers living in a world with psychopaths to dying. According to the source, Egan argues that CDT endorses pressing the button, while almost everyone agrees Paul should not press it.

The problem again concerns evidence about one’s own type. Let \(P\) mean Paul is a psychopath. If pressing the button kills all psychopaths, then:

- If \(P\) is true, pressing causes Paul’s death.
- If \(P\) is false, pressing causes a world without psychopaths.

If Paul’s prior probability of being a psychopath is low, and the value of a psychopath-free world is sufficiently high, a naive CDT calculation may favor pressing. But Paul’s inclination to press is itself evidence that \(P\) may be true. EDT uses this evidence directly. CDT, in its strict form, may hold fixed the prior probability of \(P\) when evaluating the causal consequences of pressing.

The source notes Egan’s diagnosis: CDT requires holding fixed the agent’s unconditional credences in dependency hypotheses, and this can produce intuitively irrational decisions. The source also notes Joyce’s defense, according to which CDT can take into account information about what one is likely to do.

I think the most reasonable operational interpretation is a moderated version of CDT:

1. Before evaluating actions, the agent should condition on all *actual* evidence available at the time of choice.
2. This evidence may include facts about the agent’s inclinations, deliberative tendencies, and self-knowledge.
3. But when evaluating a counterfactual action, the agent should not treat the mere supposition “I do \(A\)” as additional evidence about fixed background variables.

Thus, in the Psychopath Button case, if Paul actually observes in himself a strong inclination to press the button, and he knows that only a psychopath would have such an inclination, he should update his probability that he is a psychopath before computing causal expected utility. If after updating the expected value of pressing is negative, he should not press. This preserves CDT’s anti-evidential core while avoiding some implausible results caused by ignoring actual self-knowledge.

This proposal is not explicitly in the source. It is a reconstruction intended to make CDT operationally defensible.

---

## 7. The Adversarial Offer and Dutch-book concerns

Another counterexample mentioned in the source is the Adversarial Offer. Two boxes are available; the buyer may buy one or none, but not both. Each box costs \$1. The seller previously put \$3 in each box she predicted the buyer would not acquire. The seller’s prediction is believed to be accurate with probability \(0.75\).

From a CDT perspective, the seller’s past prediction is fixed. If the buyer intervenes to buy one box, that intervention does not change the seller’s past action. If the buyer thinks the chosen box has expected contents greater than \$1, buying seems causally favorable. The source summarizes the reasoning as follows: CDT thinks at least one box contains \$3, so the average box contains at least \$1.50 in expected value, exceeding the \$1 cost. Hence CDT requires buying a box. But this is profitable for the seller.

The tension is that CDT evaluates the local causal effect of buying a box while treating the prediction as fixed, yet the buyer’s choice is correlated with the prediction. Across repeated or adversarially structured interactions, this can allow money to be extracted from the CDT agent. The source cites Oesterheld and Conitzer’s argument that CDT agents can be subject to diachronic Dutch books.

Here again, a causal-model approach helps clarify the issue. Suppose \(S_i\) is the seller’s prediction about whether the buyer will acquire box \(i\), and \(B_i\) is the content of box \(i\). The seller sets \(B_i=3\) if she predicts the buyer will not acquire box \(i\). The buyer’s choice \(A\) is correlated with \(S_i\) through the buyer’s psychology. If we evaluate \(do(A=\text{buy box }i)\) while holding the seller’s prediction fixed, buying can look good. But if we evaluate the entire policy by which the buyer selects boxes, and if the seller predicts that policy, the policy may have negative ex ante value.

This suggests that CDT must be careful about the unit of evaluation. Evaluating isolated actions while holding predictions fixed can produce locally attractive choices that are globally exploitable. A policy-level CDT evaluation may be more appropriate when predictors are responding to the agent’s general decision procedure.

This is my own extension of the source’s point. The source states that variants of Death in Damascus can make CDT lose money; the policy-level interpretation is one way to understand why.

---

## 8. What CDT gets right, and what remains open

CDT captures an important intuition: rational agents should care about what their actions cause, not merely about what their actions signify. If eating an apple causes happiness and eating an orange causes sadness, the apple is preferable. If an action is merely correlated with a good outcome because of a common cause, choosing the action may not produce the good outcome.

The source is clear that CDT is not a complete computational algorithm. It gives a formal expression involving counterfactual probabilities but does not say exactly how those probabilities are to be computed. The imaging proposal is one answer, but it raises difficult questions about similarity among possible worlds. The structural causal model approach I have proposed is another answer, and it is especially useful for applied problems because it gives explicit rules for intervention and counterfactual evaluation.

Still, several questions remain open:

1. **Which causal model is correct?**  
   CDT requires a representation of the causal structure. In unfamiliar problems, the choice of variables and arrows can be contested.

2. **How should an agent update on self-knowledge?**  
   If the agent’s inclination to choose an action is evidence about their type, CDT must decide whether and when to condition on that evidence.

3. **How should predictors be modeled?**  
   If a predictor predicts the agent’s action, is the prediction a fixed past event, a consequence of the agent’s stable disposition, or a function of the agent’s policy? Different representations can yield different recommendations.

4. **Should CDT evaluate actions or policies?**  
   Single-action CDT can be locally dominated or Dutch-bookable in prediction problems. Policy-level CDT may avoid some problems but becomes more complex.

The source presents these as live controversies rather than settled matters. In particular, the counterexamples due to Egan, Spencer, Oesterheld, Conitzer, and Joyce are not merely technical curiosities; they probe whether CDT’s central rule—hold fixed causal structure and maximize expected causal consequences—can be made both formally precise and intuitively satisfactory.

---

## Conclusion

Causal decision theory recommends choosing the action that would bring about the best expected outcome, where the relevant probabilities are counterfactual or interventionist rather than merely evidential. Its classical formulation is

\[
U_C(A)=\sum_j P(A \mathbin{\Box\!\to} O_j)D(O_j).
\]

This differs from EDT because the probability of a counterfactual is not generally the same as a conditional probability. CDT therefore recommends two-boxing in Newcomb’s problem and summoning Bathsheba in Gibbard and Harper’s King David case, because in those cases the action does not causally affect the predictor’s prediction or the king’s charisma.

The theory’s main weakness is that it does not by itself specify how to compute counterfactual probabilities. A plausible operational interpretation is to use causal models and interventions: update on actual evidence, intervene on the action or policy variable, and compute the expected utility of the resulting outcome distribution. This gives CDT a practical form, but it does not dissolve all philosophical difficulties. Prediction, self-knowledge, and adversarial correlation remain hard cases, and they explain why CDT continues to be debated.

---

## References

Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.

Gibbard, A., & Harper, W. L. (1981). Counterfactuals and two kinds of expected utility. In *Ifs: Conditionals, Belief, Decision, Chance, and Time* (pp. 153–190).

Lewis, D. (1976). Probabilities of conditionals and conditional probabilities. *Philosophical Review*, 85(3), 297–315.

Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.

Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.

Wikipedia contributors. (2026). Causal decision theory. In *Wikipedia, The Free Encyclopedia*. Revision 1381555528. https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528