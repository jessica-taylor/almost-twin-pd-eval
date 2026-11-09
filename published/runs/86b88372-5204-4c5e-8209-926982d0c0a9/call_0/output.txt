# Causal Decision Theory: Choosing by What an Action Would Cause

Causal decision theory (CDT) is a family of decision rules according to which a rational agent should choose the action that has the best expected *causal* consequences. The theory is most easily understood by contrasting it with evidential decision theory (EDT). EDT asks: “If I learned that I had taken action \(A\), how good would the news be?” CDT asks instead: “If I intervened to make \(A\) happen, what would then be likely to occur?” The distinction matters when an action is statistically correlated with desirable or undesirable outcomes without causing them.

This essay follows the human-written reference article on causal decision theory, especially its presentation of the Gibbard–Harper counterfactual formula, the contrast with EDT, and the standard thought experiments such as Newcomb’s problem and the “Death in Damascus” predictor cases. Where the source leaves the computation of counterfactual probabilities underspecified, I develop a natural operational interpretation using interventionist causal notation. I mark such additions explicitly.

---

## 1. The basic idea: causal expected utility

Suppose an agent can choose among actions \(A_1,\dots,A_n\). Let \(O_1,\dots,O_m\) be possible outcomes, and let \(D(O_j)\) be the desirability, utility, or value of outcome \(O_j\). The simplest evidential rule evaluates an action by conditional probabilities:

\[
V_{\mathrm{EDT}}(A)=\sum_j P(O_j\mid A)\,D(O_j).
\]

Here \(P(O_j\mid A)\) is the ordinary conditional probability of \(O_j\) given that the agent performs \(A\). EDT treats the action as evidence about the world.

CDT replaces the conditional probability with a counterfactual or interventionist probability. In the formulation given by Allan Gibbard and William Harper, the causal expected utility of an action \(A\) is

\[
U(A)=\sum_j P(A \to O_j)\,D(O_j),
\]

where \(P(A\to O_j)\) is the probability of the counterfactual: “If \(A\) were performed, \(O_j\) would occur.” The arrow here should not be read as material implication; it expresses a subjunctive conditional. In modern notation one might write \(A \mathbin{\Box\!\to} O_j\).

The reference article gives a simple informal example. If eating an apple causes happiness and eating an orange causes sadness, CDT recommends the apple. But if the apple may be good or bad, and you do not know which, you must evaluate the *expected* causal effect. If you assign probability \(p\) to the apple being good, happiness from a good apple has value \(h>0\), and sadness from a bad apple has value \(-s<0\), then eating the apple has causal expected value

\[
p h - (1-p)s.
\]

If eating an orange has value \(-t\), CDT recommends the apple precisely when

\[
p h - (1-p)s > -t.
\]

The calculation is ordinary expected utility, but the probabilities are supposed to track what the action would bring about, not merely what the action would indicate.

---

## 2. A more explicit formal version

The Gibbard–Harper formula is elegant but incomplete, because it does not say how to compute the counterfactual probabilities \(P(A\to O_j)\). A useful way to make the theory operational is to describe the decision problem by a causal model.

This is my own elaboration, not explicit in the source, but it is a standard way of formalizing CDT. Let there be variables representing relevant features of the world, including an action variable \(A\) and an outcome variable \(Y\). An intervention that sets \(A=a\) is written \(\operatorname{do}(A=a)\). The probability of outcome \(Y=y\) under that intervention is \(P(Y=y\mid \operatorname{do}(A=a))\). Then the causal value of action \(a\) is

\[
U(a)=\sum_y D(y)\,P(Y=y\mid \operatorname{do}(A=a)).
\]

Equivalently, if \(Y_a\) denotes the value that \(Y\) would take if \(A\) were intervened to be \(a\),

\[
U(a)=\mathbb{E}[D(Y_a)].
\]

This formulation makes the difference from EDT precise:

\[
V_{\mathrm{EDT}}(a)=\sum_y D(y)\,P(Y=y\mid A=a),
\]

whereas

\[
V_{\mathrm{CDT}}(a)=\sum_y D(y)\,P(Y=y\mid \operatorname{do}(A=a)).
\]

The two coincide when the action is unconfounded, meaning that observing the action gives the same probabilistic information about outcomes as intervening to produce the action. In many ordinary decisions this is approximately true. But they diverge when the action is correlated with background states that also affect the outcome.

A still more general formulation allows uncertainty about the causal structure itself. Let \(K\) range over “dependency hypotheses,” i.e. hypotheses about how outcomes depend causally on actions. Then

\[
U(a)=\sum_k P(K=k)\sum_y D(y)\,P_k(Y=y\mid \operatorname{do}(A=a)).
\]

The agent’s credences \(P(K=k)\) represent her uncertainty about which causal structure obtains. CDT then says: choose an action maximizing this quantity.

A practical recipe for applying CDT is therefore:

1. List the available actions or policies.
2. Assign utilities to outcomes.
3. Specify, perhaps probabilistically, the causal dependence of outcomes on actions.
4. For each action, compute the expected utility under the intervention that sets the action.
5. Choose an action with maximal causal expected utility.

The hard step is usually the third one: specifying the relevant causal model or counterfactual probabilities.

---

## 3. Counterfactuals, imaging, and causal models

The source correctly emphasizes that CDT does not by itself supply a unique algorithm for computing counterfactual probabilities. David Lewis argued that the probability of a conditional \(P(A\to O_j)\) cannot in general be identified with the conditional probability \(P(O_j\mid A)\). His triviality result shows that, except in degenerate cases, there is no generally satisfactory identity between probabilities of conditionals and conditional probabilities. This mathematical fact underlies the philosophical distinction between CDT and EDT.

One proposal, associated with Lewis, is “imaging.” Imagine a space of possible worlds with a prior probability distribution \(P(w)\). To evaluate \(P(A\to O)\), move the probability mass from each world \(w\) to the closest possible world or worlds in which \(A\) is true. Then \(P(A\to O)\) is the total mass that lands in \(A\)-worlds where \(O\) is also true. Schematically,

\[
P(A\mathbin{\Box\!\to} O)
=
\sum_w P(w)\,Q_A(w,O),
\]

where \(Q_A(w,O)\) is the probability that the closest \(A\)-world to \(w\) satisfies \(O\). If there is a unique closest \(A\)-world, \(Q_A(w,O)\) is just \(1\) or \(0\).

Imaging captures the subjunctive flavor of CDT: we are not merely conditioning on the proposition \(A\); we are asking what would happen if the world were minimally altered to make \(A\) true. But the source notes an important problem: imaging requires a similarity relation among possible worlds, and it may require knowing what the agent would believe if she became certain of \(A\). That can generate a regress, since those beliefs themselves involve conditionals.

My preferred operational interpretation is therefore to replace closest-world semantics with an explicit causal model. In a structural causal model, each variable has an equation determining it from its parents and exogenous noise. To intervene on \(A=a\), one replaces the equation for \(A\) by the constant equation \(A=a\), leaving the other equations fixed. This gives a mathematically tractable version of “making \(A\) true while holding fixed the relevant causal background.” It is not the only possible semantics for counterfactuals, but it gives CDT a usable form.

---

## 4. CDT versus EDT: King David and Newcomb’s problem

### 4.1 King David and Bathsheba

The reference article gives an example due to Gibbard and Harper. King David wants Bathsheba but fears that summoning her may provoke revolt. David has learned that kings are either charismatic or uncharismatic. Charisma is fixed by genetics and early childhood. Charismatic kings tend to act justly and rarely face successful revolts; uncharismatic kings tend to act unjustly and often face successful revolts. But unjust acts themselves do not cause revolts; the revolts are caused by the king’s uncharismatic bearing.

Let \(K\in\{C,U\}\) represent David’s type: charismatic or uncharismatic. Let \(S\) be the action of summoning Bathsheba, and let \(R\) be a successful revolt. Suppose the benefit of summoning Bathsheba is \(b>0\), and the cost of revolt is \(c>0\). Let

\[
\rho_C = P(R\mid \operatorname{do}(S), C)
\]

be the revolt probability for a charismatic king, and

\[
\rho_U = P(R\mid \operatorname{do}(S), U)
\]

be the revolt probability for an uncharismatic king. The crucial causal assumption is that summoning Bathsheba does not change David’s charisma, and the unjust act itself does not cause revolt. Thus

\[
P(R\mid \operatorname{do}(S), K)
=
P(R\mid \operatorname{do}(\neg S), K)
=
\rho_K.
\]

If \(q=P(C)\), then CDT evaluates summoning as

\[
U(S)=q(b-\rho_C c)+(1-q)(b-\rho_U c),
\]

while abstaining has value

\[
U(\neg S)=q(-\rho_C c)+(1-q)(-\rho_U c).
\]

The difference is

\[
U(S)-U(\neg S)=b>0.
\]

So CDT recommends summoning Bathsheba.

EDT can give the opposite advice. Summoning Bathsheba is evidence that David is uncharismatic, because uncharismatic kings tend to act unjustly. Thus EDT may assign a high value to

\[
P(R\mid S),
\]

even though summoning does not causally raise the chance of revolt. EDT asks whether the news “David summoned Bathsheba” is good news; CDT asks whether the intervention of summoning her improves David’s prospects. Since charisma is fixed, CDT says the intervention merely adds the benefit \(b\).

This example illustrates the central CDT maxim: do not chase bad news or avoid good news; change what you can change.

### 4.2 Newcomb’s problem

Newcomb’s problem is the most famous test case. A predictor, highly reliable but perhaps not perfect, has predicted whether you will take only box B or both boxes A and B. Box A contains \$1,000. Box B contains \$1,000,000 if the predictor predicted one-boxing, and nothing if the predictor predicted two-boxing. You may take both boxes or only box B.

Let \(T\) be two-boxing and \(L\) be one-boxing. Let \(C\) be the content of box B. The payoff table is:

\[
\begin{array}{c|cc}
 & C=\$1{,}000{,}000 & C=\$0 \\
\hline
L & \$1{,}000{,}000 & \$0 \\
T & \$1{,}001{,}000 & \$1{,}000
\end{array}
\]

For any fixed content of box B, two-boxing gives \$1,000 more than one-boxing. If the predictor’s prediction is already fixed, then at the moment of choice the content of box B is causally independent of the player’s action. In interventionist terms,

\[
P(C\mid \operatorname{do}(T)) = P(C\mid \operatorname{do}(L))
\]

or, more weakly, the difference in payoffs dominates any difference in the probability assigned to \(C\). CDT therefore recommends two-boxing:

\[
U(T)=U(L)+1000.
\]

EDT reasons differently. One-boxing is strong evidence that the predictor predicted one-boxing, so

\[
P(C=\$1{,}000{,}000\mid L)
\]

is high. Two-boxing is strong evidence that the predictor predicted two-boxing, so

\[
P(C=\$1{,}000{,}000\mid T)
\]

is low. Therefore EDT usually recommends one-boxing.

The source notes that philosophers disagree about whether one-boxing or two-boxing is rational, but it also says that when forced to choose between CDT and EDT as general theories, philosophers often prefer CDT. Newcomb’s problem remains the central dividing line. From the CDT perspective, one-boxing is a kind of magical thinking: choosing one box does not cause money to appear in box B. From the EDT perspective, CDT needlessly passes up predictable gains.

---

## 5. Policies, sequential decisions, and dependence

So far I have discussed one-shot actions. But decision problems often involve policies: rules mapping observations to actions. CDT can evaluate policies by treating the adoption of a policy as an intervention.

Suppose an agent observes variables \(Z\) before acting. A deterministic policy is a function

\[
\pi: Z\mapsto A.
\]

The causal value of the policy is

\[
U(\pi)=\mathbb{E}[D(Y)\mid \operatorname{do}(A=\pi(Z))].
\]

For a stochastic policy, the intervention sets a distribution over actions conditional on \(Z\), and the value is the corresponding expectation.

This policy formulation matters in predictor problems. In Newcomb’s problem, if the predictor makes its prediction after observing the agent’s stable policy or disposition, then choosing a one-boxing policy earlier may causally affect the predictor’s prediction. In that case, CDT can recommend adopting a one-boxing policy before the prediction is made. But if the prediction is already fixed and the agent is only choosing an act at the later moment, act-CDT recommends two-boxing.

Thus CDT’s treatment of dependencies depends on temporal and causal structure:

- If an action causally influences an outcome, CDT counts that influence.
- If an action is correlated with an outcome only because both are caused by a common factor, CDT does not treat the action as changing the outcome.
- If a policy or disposition causally influences a predictor’s behavior, CDT can count that influence when evaluating the policy.
- If the predictor’s prediction is already fixed and cannot be affected by the current intervention, CDT holds it fixed.

This is why CDT is not simply “ignore correlations.” It ignores correlations that are not backed by an appropriate causal path from the intervention to the outcome. But it uses correlations that are consequences of causal influence.

---

## 6. Counterexamples and unresolved issues

The reference article lists several alleged counterexamples to CDT. They mostly involve cases where an agent’s action is strong evidence about a fixed feature of the agent or the world, and where CDT’s refusal to treat that evidence as causally relevant produces intuitively bad advice.

### 6.1 Death in Damascus

In the “Death in Damascus” scenario, Death predicts where you will be tomorrow and waits there. You must decide whether to stay in Damascus or flee to Samarra. If Death predicts your location correctly, you die.

Suppose Death’s prediction is already made and highly reliable. Let \(D\) be Death’s predicted location and \(L\) your actual location. Your survival requires \(L\neq D\). If the prediction is fixed and your current action does not causally affect it, CDT may evaluate staying and fleeing using the prior probability of Death’s prediction. If the prior is symmetric, CDT is indifferent:

\[
U(\text{stay})=U(\text{flee}).
\]

But if your present inclination to stay or flee is itself evidence about Death’s prediction, EDT can draw a different conclusion. If you find yourself inclined to stay, that may be evidence that Death predicted you would stay, so you should flee; but then your inclination to flee may be evidence that Death predicted you would flee. The case creates instability.

The source says that a CDT agent may be unable to process the correlation and may make irrational decisions. The deeper issue is whether CDT should hold fixed the agent’s unconditional credences about dependency hypotheses, even when the action is informative about those hypotheses.

### 6.2 The psychopath button

Andy Egan’s psychopath button is another influential case. Paul is considering pressing a button that would kill all psychopaths. Paul thinks a world without psychopaths would be much better. But he is confident that only a psychopath would press the button. He strongly prefers living in a world with psychopaths to dying.

Let \(P\) be the proposition that Paul is a psychopath. Let \(B\) be pressing the button. If Paul is not a psychopath, pressing the button yields a good outcome \(W\). If Paul is a psychopath, pressing the button kills him, yielding a terrible outcome \(D\). Not pressing yields some intermediate outcome \(L\), the value of living in a world with psychopaths.

CDT treats Paul’s psychopathy as fixed by the time of choice. If \(p=P(P)\), then

\[
U(B)=(1-p)W+pD,
\]

while

\[
U(\neg B)=L.
\]

If \(p\) is small enough and \(W\) is large enough, CDT recommends pressing the button. EDT, however, notes that pressing the button is strong evidence that Paul is a psychopath. Since Paul is quite confident that only a psychopath would press it,

\[
P(P\mid B)
\]

is high, so EDT recommends not pressing.

The source mentions Jim Joyce’s defense that CDT can take into account information about what one is inclined or likely to do. This suggests a natural refinement. If Paul has already observed a strong urge to press the button, and that urge is evidence of psychopathy, then he should update his prior \(p\) before computing causal expected utility. Let the evidence be \(E\). Then CDT should use

\[
P(P\mid E)
\]

instead of the unconditional \(P(P)\). If after updating the probability of psychopathy is high, CDT itself may advise against pressing. Whether this fully answers Egan depends on how the case is specified: if Paul has no independent evidence except the hypothetical fact that he would press, CDT still seems to press.

### 6.3 Adversarial offers and money pumps

The source also discusses newer counterexamples, such as the Adversarial Offer. Two boxes are on offer. A buyer may buy one box or none, but not both. Each box costs \$1. The seller previously put \$3 in each box that she predicted the buyer would not acquire. The seller’s predictions are accurate with probability \(0.75\).

The source summarizes the CDT reasoning as follows: at least one box contains \$3, so the average box contains at least \$1.50 in expected value, which exceeds the \$1 cost. CDT therefore recommends buying a box. But the seller profits, because the buyer tends to select the box she predicted he would acquire, which is likely empty.

This case resembles Newcomb-style problems in miniature. The buyer’s choice is correlated with the seller’s prediction. CDT, holding the prediction fixed under the intervention, sees a positive causal expected value in buying a box. But the overall arrangement extracts money from the CDT agent. According to Caspar Oesterheld and Vincent Conitzer, such cases show that CDT agents can voluntarily lose money and can be subject to diachronic Dutch books.

These examples do not merely challenge CDT’s practical recommendations. They raise a foundational question: should a decision theory evaluate actions by holding fixed the agent’s prior causal hypotheses, or should it allow the action to provide evidence about which hypothesis, type, or disposition the agent instantiates?

---

## 7. An operational interpretation and its limits

The reference article leaves an important question open: how exactly should an agent compute \(P(A\to O_j)\)? I think the most defensible operational interpretation is the interventionist one sketched earlier:

\[
P(A\to O_j) \approx P(O_j\mid \operatorname{do}(A)).
\]

But this requires a causal model. A reasonable procedure is:

1. Represent the world with variables for actions, outcomes, and relevant background states.
2. Treat fixed traits, past predictions, and common causes as exogenous relative to the current action.
3. Condition on all evidence actually observed before the decision.
4. Do not condition on the hypothetical action itself when computing the intervention.
5. If uncertain among causal models, average over them using prior or posterior model probabilities.

This procedure preserves the core CDT idea: actions are evaluated by what they would cause, not by what they would indicate. It also gives a clean answer to many ordinary cases. If you have evidence that you are likely to be a certain type of agent, you should condition on that evidence before deciding. But once you ask, “What would happen if I intervened to perform \(A\)?” you should not further treat \(A\) as news.

The limitation is that this operational interpretation builds in the controversial CDT commitment. In Newcomb-like cases, critics will say that the agent’s choice is not a pure intervention but is itself evidence about the agent’s disposition, and that a rational agent should exploit that evidence. CDT replies that dispositions are fixed and choices are not causes of past predictions. The disagreement is therefore not merely computational; it is philosophical.

A policy-centered version of CDT can mitigate some problems. Instead of evaluating only the immediate act, evaluate the policy or decision procedure the agent will implement. This can recommend precommitment, randomization, or institutional rules that improve outcomes in predictor problems. However, policy evaluation does not erase all tensions. An agent may evaluate a one-boxing policy as best before the predictor acts, yet later two-box when the money is already in the boxes. This diachronic instability is one reason critics claim that CDT can be Dutch-booked.

---

## 8. Conclusion

Causal decision theory says that rational choice is guided by the expected value of what an action would causally produce. Its canonical form is the Gibbard–Harper formula

\[
U(A)=\sum_j P(A\to O_j)\,D(O_j),
\]

where the probabilities are counterfactual rather than merely conditional. In an interventionist formulation, this becomes

\[
U(a)=\sum_y D(y)\,P(Y=y\mid \operatorname{do}(A=a)).
\]

CDT differs from EDT precisely when actions are evidentially correlated with outcomes without causing them. In King David’s case, CDT recommends summoning Bathsheba because the act does not change David’s charisma. In Newcomb’s problem, CDT recommends two-boxing because the current choice does not cause the predictor’s past prediction.

The theory is powerful when the relevant causal structure is clear. Its main difficulties lie in specifying counterfactual probabilities and in handling cases where an agent’s action is strong evidence about fixed traits, predictions, or dependency hypotheses. The reference article correctly presents these as live philosophical problems. A causal-model implementation gives CDT a precise operational form, but it does not settle the deeper dispute over whether rational agents should always refuse to treat their own choices as mere evidence.

---

## References

- Wikipedia contributors, “Causal decision theory,” Wikipedia, revision 1381555528, 2026.  
- Gibbard, A., and Harper, W. L. (1981). “Counterfactuals and Two Kinds of Expected Utility.” In *Ifs: Conditionals, Beliefs, Decision, Chance, and Time*, 153–190.  
- Lewis, D. (1976). “Probabilities of Conditionals and Conditional Probabilities.” *Philosophical Review*, 85(3), 297–315.  
- Lewis, D. (1981). “Causal Decision Theory.” *Australasian Journal of Philosophy*, 59(1), 5–30.  
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.  
- Egan, A. (2007). “Some Counterexamples to Causal Decision Theory.” *Philosophical Review*, 116(1), 93–114.  
- Joyce, J. M. (2012). “Regret and Instability in Causal Decision Theory.” *Synthese*, 187(1), 123–145.  
- Oesterheld, C., and Conitzer, V. (2021). “Extracting Money from Causal Decision Theorists.” *Philosophical Quarterly*, 71(4), pqaa086.