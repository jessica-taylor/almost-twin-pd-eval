# Causal Decision Theory: Expected Utility as Counterfactual Intervention

## 1. The central idea

Causal decision theory (CDT) is a school of decision theory holding that a rational agent should choose the action that *causes* the best expected outcome. The reference article summarizes the contrast with evidential decision theory (EDT) as follows: EDT recommends the action that would be the best *news* if one learned that it had been taken, while CDT recommends the action with the best expected causal consequences. If eating an apple causes happiness and eating an orange causes sadness, CDT says eat the apple. If the apple may be good or bad, CDT says to maximize the *expected* causal effect, weighting possible outcomes by their probabilities and utilities.

The classic formal statement, due to Allan Gibbard and William Harper, defines the causal expected utility of an action \(A\) by

\[
U(A)=\sum_j P(A \mathbin{\square\!\to} O_j)\,D(O_j),
\]

where \(O_j\) ranges over possible outcomes, \(D(O_j)\) is the desirability or utility of outcome \(O_j\), and \(P(A \mathbin{\square\!\to} O_j)\) is the probability of the counterfactual: “if \(A\) were performed, \(O_j\) would obtain.” The arrow here is not material implication and is not generally the conditional probability \(P(O_j\mid A)\). It is meant to capture what would happen under the hypothetical performance of \(A\), not merely what \(A\) would indicate.

EDT, by contrast, uses ordinary conditional probabilities:

\[
U_{\text{EDT}}(A)=\sum_j P(O_j\mid A)\,D(O_j).
\]

The difference is small when actions are probabilistically independent of the relevant counterfactuals, but it becomes decisive when an action is evidence about background conditions that also affect the outcome.

## 2. Counterfactual probabilities versus conditional probabilities

David Lewis argued that probabilities of conditionals cannot generally be identified with conditional probabilities. In the present context, this means

\[
P(A \mathbin{\square\!\to} O) \neq P(O\mid A)
\]

in general. If equality always held, CDT would collapse into EDT.

Gibbard and Harper showed that, given certain assumptions about counterfactual logic—including a principle related to conditional excluded middle—statistical independence between \(A\) and the counterfactual \(A \mathbin{\square\!\to} O_j\) is enough to make the two calculations agree. In many ordinary decisions, performing an action does not tell you anything surprising about what that action would cause. In such cases, CDT and EDT give the same recommendation.

They diverge when the action is evidence for a background variable that influences the outcome but is not itself changed by the action. The reference article illustrates this with the case of King David. David wants Bathsheba but fears that summoning her may provoke revolt. He knows that kings are either charismatic or uncharismatic, that charisma is fixed in adulthood, that charismatic kings tend to act justly and rarely face successful revolts, and that uncharismatic kings tend to act unjustly and often face successful revolts. Crucially, the article says that unjust acts themselves do not cause revolts; the revolt risk comes from the king’s underlying character.

Let \(C\) be the proposition that David is charismatic, \(S\) the action of summoning Bathsheba, and \(R\) a successful revolt. The causal structure is roughly:

\[
C \longrightarrow S, \qquad C \longrightarrow R,
\]

but, by stipulation, \(S\) does not cause \(R\). EDT evaluates

\[
U_{\text{EDT}}(S)=D(S\land \neg R)P(\neg R\mid S)+D(S\land R)P(R\mid S).
\]

Because summoning Bathsheba is evidence that David is uncharismatic, \(P(R\mid S)\) may be high. EDT may therefore recommend abstaining. CDT instead asks what would happen if David intervened to make \(S\) true. Since \(S\) does not affect \(C\), and \(C\) is the common cause of both \(S\) and \(R\), the relevant probability is not \(P(R\mid S)\) but something like \(P(R\mid do(S))\), where \(do(S)\) means “bring about \(S\) by intervention.” If summoning does not causally raise the revolt probability, then

\[
P(R\mid do(S))=P(R),
\]

or at least it is not inflated merely because \(S\) is evidence of uncharismatic character. CDT can therefore recommend summoning Bathsheba if the benefit outweighs the baseline revolt risk.

This example captures the core CDT principle: correlations induced by common causes are not reasons to act unless the action causally changes the outcome.

## 3. An operational interpretation: interventions and causal models

The reference article emphasizes an important gap: CDT itself does not specify an algorithm for computing the counterfactual probabilities \(P(A \mathbin{\square\!\to} O_j)\). One proposal mentioned there is Lewis’s “imaging” technique: to evaluate \(P(A \mathbin{\square\!\to} O)\), move probability mass from each possible world to the closest possible world in which \(A\) holds. But this requires a notion of closeness among possible worlds, and Shaffer’s regress objection says that we may need to know what we would believe if we were certain of \(A\), which itself may be uncertain.

A natural operational interpretation—one that I add to the source rather than find in it—is to use structural causal models or causal Bayesian networks. This is not the only possible interpretation of CDT, but it gives a precise recipe for many decision problems.

Let a causal model contain variables, structural equations, and a probability distribution over exogenous noise variables. Suppose \(A\) is the action variable and \(O\) is the outcome variable. An intervention setting \(A=a\) is written \(do(A=a)\). Formally, the intervention replaces the structural equation for \(A\) with the equation \(A:=a\), while leaving the other structural equations unchanged. The probability of outcome \(o\) under that intervention is

\[
P(o\mid do(a)).
\]

Then the causal expected utility of action \(a\) is

\[
U_{\text{CDT}}(a)=\sum_o u(o)P(o\mid do(a)).
\]

Equivalently, if \(\mathbf{U}\) denotes the exogenous variables of the model and \(O_a(\mathbf{u})\) is the value that the outcome would take in world \(\mathbf{u}\) under intervention \(do(A=a)\), then

\[
U_{\text{CDT}}(a)
=
\sum_{\mathbf{u}} P(\mathbf{u})\,u(O_a(\mathbf{u})).
\]

This formula makes the counterfactual idea concrete: for each possible background state of the world, hold that state fixed, change the action by intervention, propagate the effects forward through the causal system, and evaluate the resulting outcome. Then average over the agent’s prior distribution on background states.

This interventionist reading also clarifies how CDT treats dependencies. If a variable \(K\) is a common cause of both action and outcome, then conditioning on the action may change the probability of \(K\), but intervening on the action does not. In a causal graph, intervening on \(A\) cuts all arrows into \(A\); only variables downstream of \(A\) are affected. Thus CDT distinguishes:

1. **Causal dependence of outcome on action**: counted by CDT.  
2. **Evidential dependence of action on common causes**: ignored by CDT unless it affects causal consequences.  
3. **Logical or predictive correlations without causal influence**: generally ignored by standard CDT, although this is exactly where many counterexamples arise.

When the agent is uncertain about the causal structure itself, we can average over dependency hypotheses or causal models. Let \(K\) index possible causal structures, with prior probabilities \(P(K)\). Then a natural extension is

\[
U_{\text{CDT}}(a)
=
\sum_k P(K=k)\sum_o u(o)P(o\mid do_k(a),K=k).
\]

Here \(P(K=k)\) is the agent’s prior credence in causal structure \(k\), not necessarily the conditional credence \(P(K=k\mid a)\). This reflects the idea that the action does not change the causal structure, even if performing the action would be evidence about it. This “holding fixed” feature is central to CDT and is also the target of Andy Egan’s criticism, discussed below.

## 4. Evaluating policies, not only single actions

CDT can also evaluate policies. A policy is a rule mapping information states to actions. Suppose a policy \(\pi\) says: when the agent observes \(X=x\), take action \(A=\pi(x)\). In an interventionist semantics, the policy is evaluated by replacing the action variable’s structural equation with

\[
A:=\pi(X).
\]

The causal expected utility of the policy is then

\[
U_{\text{CDT}}(\pi)
=
\mathbb{E}\bigl[u(O)\mid do(A:=\pi(X))\bigr].
\]

For sequential decisions, one replaces each decision variable \(A_t\) with a policy function of the history \(H_t\):

\[
A_t := \pi_t(H_t).
\]

Then

\[
U_{\text{CDT}}(\pi)
=
\mathbb{E}\bigl[u(O)\mid do(A_t:=\pi_t(H_t)\text{ for all }t)\bigr].
\]

This gives a clear operational rule: to compare policies, simulate the world under the intervention that the agent follows each policy, and compare the expected utilities of the resulting outcome distributions.

This policy viewpoint is useful because many apparent paradoxes involve not merely a one-off action but a decision rule that predictors can anticipate. If a predictor predicts the agent’s policy, CDT still asks whether adopting that policy causally improves outcomes, given the agent’s causal model.

## 5. Simple example: the uncertain apple

Begin with the reference article’s informal example. Eating an apple may cause happiness if the apple is good, or sadness if it is bad. Let \(G\) be the proposition that the apple is good, with prior probability \(p\). Let \(u_H\) be the utility of happiness and \(u_S\) the utility of sadness. Eating an orange gives known utility \(u_O\).

CDT evaluates eating the apple as

\[
U_{\text{CDT}}(\text{apple})
=
p u_H + (1-p)u_S.
\]

It evaluates eating the orange as

\[
U_{\text{CDT}}(\text{orange})=u_O.
\]

The agent eats the apple iff

\[
p u_H + (1-p)u_S > u_O.
\]

Here CDT and EDT agree, because the apple’s goodness is not plausibly affected by the action and there is no problematic common cause making the action itself evidence about the outcome.

## 6. Newcomb’s problem

Newcomb’s problem is the most famous test case. A predictor has predicted whether the agent will take both boxes or only one. Box A visibly contains \$1,000. Box B contains \$1,000,000 if the predictor predicted one-boxing, and nothing if the predictor predicted two-boxing. The predictor is highly reliable, say 99% accurate. The agent chooses after the prediction has been made.

Let \(B\) be the amount in Box B and \(T\) the choice: one-box or two-box. The causal structure is:

\[
\text{Predictor} \longrightarrow B,
\]

and the predictor is correlated with \(T\), but, by the usual setup, \(T\) does not causally affect the predictor’s earlier prediction. Therefore, under CDT,

\[
P(B\mid do(T=\text{two})) = P(B),
\]

and similarly for one-boxing. The action does not change what is already in Box B.

For every possible background state in which Box B contains some amount \(b\), two-boxing yields \(b+1000\), while one-boxing yields \(b\). Thus

\[
U_{\text{CDT}}(\text{two})
=
\mathbb{E}[B]+1000,
\]

while

\[
U_{\text{CDT}}(\text{one})
=
\mathbb{E}[B].
\]

Two-boxing dominates by \$1,000. CDT therefore recommends taking both boxes.

EDT reasons differently. Taking only Box B is strong evidence that the predictor predicted one-boxing, so

\[
P(B=1{,}000{,}000\mid \text{one})
\]

is high. Taking both boxes is strong evidence that Box B is empty, so

\[
P(B=0\mid \text{two})
\]

is high. EDT therefore recommends one-boxing. The reference article notes that philosophers disagree about which answer is rational, but CDT’s answer is standardly two-boxing.

The case illustrates CDT’s treatment of predictive correlation. The predictor’s belief matters causally because it caused the box contents, but the agent’s current choice does not cause the predictor’s past belief. CDT refuses to treat the choice as evidence that changes the past.

## 7. Death in Damascus and predictive counterexamples

The “Death in Damascus” scenario creates a related difficulty. Death predicts where you will be tomorrow and waits there. You know Death is a reliable predictor. If you are currently in Damascus and Death says it has an appointment with you tomorrow in Damascus, should you flee to Aleppo?

Let \(L\) be your location tomorrow and \(D\) Death’s prediction. Death’s prediction causes Death’s location. If Death is reliable, \(D\) is strongly correlated with \(L\), but your choice of location does not causally affect Death’s earlier prediction. CDT may evaluate fleeing by holding Death’s prediction fixed. If your current evidence suggests Death predicted you will stay in Damascus, fleeing seems causally advantageous. But if you become inclined to flee, that inclination is evidence that Death predicted fleeing, which makes staying look better. The agent may have no stable CDT-ratifiable choice.

The reference article says that CDT may be unable to process the correlation and may make irrational decisions. The deeper issue is that CDT evaluates actions by holding fixed the agent’s prior causal picture, but in predictor problems the action is strong evidence about what the predictor predicted. Standard CDT treats the prediction as causally fixed, but this can produce unstable or exploitable behavior.

A related example from the source is the Adversarial Offer. Two boxes are offered; the buyer may buy one or none, but not both. Each box costs \$1. Yesterday, the seller put \$3 in each box that she predicted the buyer would not acquire. Both believe the seller’s prediction is accurate with probability 0.75. The article says CDT reasons that at least one box contains \$3, so the average box contains at least \$1.50 in causal expected value, exceeding the \$1 cost; hence CDT requires buying a box. Yet the offer is profitable for the seller.

The exact calculation depends on how one models the seller’s predictions and the symmetry between boxes. But the intended lesson is clear: CDT can be exploited when an adversarial predictor places payoffs in locations anti-correlated with the agent’s choices. The agent’s local causal calculation says buying a box has positive expected value, while the global predictive setup ensures that the chosen box is likely empty or the total transaction benefits the seller. This kind of example pressures CDT to explain which dependencies should be held fixed and how counterfactuals should be computed when the agent’s choice procedure is predictable.

## 8. The Psychopath Button and common causes

Another counterexample mentioned in the source is the Psychopath Button. Paul can press a button that kills all psychopaths. Paul thinks a world without psychopaths would be much better. But he is also confident that only a psychopath would press such a button. Paul prefers living in a world with psychopaths to dying.

Let \(P\) be the proposition that Paul is a psychopath, \(B\) the action of pressing, and \(W\) the resulting world. Psychopathy may cause Paul to be inclined to press, while pressing causes the elimination of psychopaths. If Paul is not a psychopath, pressing may produce a better world. If Paul is a psychopath, pressing kills him, which he regards as worse than living with psychopaths.

CDT holds Paul’s psychopathy status fixed when evaluating the causal effect of pressing. If \(p=P(P)\), a simplified causal expected utility calculation is

\[
U_{\text{CDT}}(B)
=
(1-p)u(\text{no psychopaths, alive})
+
p u(\text{death}),
\]

while

\[
U_{\text{CDT}}(\neg B)
=
(1-p)u(\text{psychopaths, alive})
+
p u(\text{psychopaths, alive}).
\]

If the benefit of a psychopath-free world is large enough relative to Paul’s prior probability of being a psychopath, CDT can recommend pressing. EDT, by contrast, conditions on pressing:

\[
P(P\mid B)
\]

is high, because only a psychopath would press. EDT therefore recommends not pressing. According to the source, Egan argues that CDT endorses pressing even though “pretty much everyone” agrees Paul should not.

Again, the precise recommendation depends on utilities and priors, but the example exposes the tension: CDT treats psychopathy as a background condition not changed by the action, while ordinary intuition treats the action as alarming evidence about that background condition.

## 9. Prisoner’s dilemma with correlated twins

A similar issue arises in a Newcomb-like Prisoner’s Dilemma. Suppose you play against a “twin” whose reasoning is highly correlated with yours, but whose choice is not caused by yours. If you cooperate, the twin is likely to cooperate; if you defect, the twin is likely to defect. EDT may recommend cooperation because cooperating is evidence that the twin will cooperate. Standard CDT treats the twin’s choice as causally independent of yours and evaluates defection as having better causal consequences given either possible choice of the twin. Thus CDT often defects in such cases, while EDT may cooperate.

This is not necessarily a refutation of CDT; a CDT defender may say that causal influence, not correlation, is what matters. But it shows that CDT’s verdicts can conflict with theories that assign decision-relevance to logical or statistical correlations.

## 10. What CDT leaves open

The most important open question in the source is how to compute counterfactual probabilities. The Gibbard–Harper formula is elegant, but it is not a complete algorithm unless we know what the probabilities of counterfactuals are. Lewis’s imaging proposal gives one possible semantics, but it depends on a similarity relation among possible worlds and may generate regress if we must evaluate what we would believe under certainty.

My proposed operational interpretation—using structural causal models and interventions—makes CDT applicable in many technical settings. It replaces “closest possible world” with an explicit model of causal mechanisms. However, this interpretation introduces assumptions not contained in the source:

1. The agent must possess or learn a causal model.  
2. The model must distinguish intervention from conditioning.  
3. The agent must decide which variables are exogenous and which are downstream of the action.  
4. If multiple causal models are possible, the agent must assign priors over them.  
5. The agent must decide whether to update those priors on the contemplated action.

Standard CDT tends to answer the last question by holding dependency hypotheses fixed. Egan argues that this is the source of many counterexamples: CDT says “do what you expect will bring about the best results,” but then computes expectations while holding fixed the agent’s prior credences about causal structure, even when the action is evidence about that structure.

A possible moderate response is to separate two kinds of information:

- Information about the causal structure should be fixed when evaluating interventions, because the action does not change causal structure.
- Information about ordinary states of the world should be incorporated before intervention, provided it is not itself downstream of the action.

This yields a practical recipe:

1. Specify the action or policy.  
2. Specify a causal model or set of dependency hypotheses.  
3. Condition on all admissible evidence that is not caused by the action.  
4. For each action, apply the intervention \(do(A=a)\).  
5. Compute expected utility under the intervened distribution.  
6. Choose the action or policy with maximum causal expected utility.

This recipe does not solve every philosophical problem. It does not tell us what to do when predictions are accurate because of logical correlation, simulation, or shared decision algorithms rather than ordinary causal influence. Nor does it fully settle whether CDT should be modified to require ratifiability, stability, or dynamic consistency. But it does make CDT precise enough for many applications in statistics, artificial intelligence, economics, and policy analysis.

## 11. Conclusion

Causal decision theory evaluates actions by asking what would happen if the agent intervened to perform them. Its core formula replaces conditional probabilities with probabilities of counterfactuals:

\[
U_{\text{CDT}}(A)=\sum_j P(A \mathbin{\square\!\to} O_j)D(O_j).
\]

The theory differs from evidential decision theory precisely when actions are evidence about background conditions that also affect outcomes. In Newcomb’s problem, Death in Damascus, twin Prisoner’s Dilemmas, and the Psychopath Button, CDT’s insistence on causal rather than evidential dependence leads to controversial but structurally intelligible recommendations.

The source article rightly emphasizes that CDT does not by itself supply an algorithm for computing counterfactual probabilities. A reasonable operational interpretation is to model the decision problem causally and evaluate actions with interventions: \(P(o\mid do(a))\). This gives CDT a clear mathematical form and makes it applicable to policies and sequential decisions. The price is that the theory’s verdicts depend on the chosen causal model, and many philosophical counterexamples target exactly that dependency. CDT is therefore best understood not as a self-contained calculator, but as a principled schema: maximize expected utility under the causal consequences of your intervention.

## References

- Gibbard, A., & Harper, W. L. (1981). Counterfactuals and two kinds of expected utility. In *Ifs: Conditionals, Beliefs, Decision, Chance, and Time*, 153–190.  
- Lewis, D. (1976). Probabilities of conditionals and conditional probabilities. *Philosophical Review*, 85(3), 297–315.  
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.  
- Egan, A. (2007). Some counterexamples to causal decision theory. *Philosophical Review*, 116(1), 93–114.  
- Oesterheld, C., & Conitzer, V. (2021). Extracting money from causal decision theorists. *Philosophical Quarterly*, 71(4), pqaa086.  
- Wikipedia contributors. (2026). Causal decision theory. Revision 1381555528. Wikimedia Foundation. https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528