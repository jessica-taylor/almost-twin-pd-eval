# Causal Decision Theory: Choosing by Interventions, Not by News

Causal decision theory (CDT) is a family of decision rules saying that a rational agent should choose the action whose *causal consequences* are best in expectation. The reference article summarizes the core idea as follows: when an agent faces several possible actions, she should select the action that causes the best outcome in expectation. This contrasts with evidential decision theory (EDT), which says that the agent should choose the action that would be the best “news”: the action whose performance would be most strongly associated with good outcomes, conditional on learning that it was performed.

This essay reconstructs CDT in a more explicit mathematical form. I begin with the standard expected-utility framework and the Gibbard–Harper counterfactual formula. I then explain how CDT differs from EDT, how it treats dependencies and counterfactuals, and how one might operationalize it using causal models. The source article correctly notes that CDT itself does not supply a unique algorithm for computing counterfactual probabilities; where the source leaves this open, I propose an operational interpretation using structural causal models and policy interventions. That proposal is my own addition, though it is continuous with standard modern treatments of causation.

---

## 1. Expected utility: evidential versus causal

Let \(\mathcal A\) be a set of available actions, and let \(\mathcal O=\{O_1,\dots,O_n\}\) be a partition of possible outcomes. Let \(D(O_j)\) be the desirability, utility, or value of outcome \(O_j\). In the simplest finite setting, evidential decision theory evaluates an action \(A\) by

\[
V_E(A)=\sum_j D(O_j)\,P(O_j\mid A).
\]

Here \(P(O_j\mid A)\) is the ordinary conditional probability of outcome \(O_j\) given that the agent performs \(A\). The phrase “given that” is important: EDT asks what the world would probably be like if the agent received the news that \(A\) had been performed.

Causal decision theory replaces the conditional probability with a counterfactual probability. In the formulation attributed by the source to Gibbard and Harper,

\[
U(A)=\sum_j P(A \to O_j)\,D(O_j),
\]

where \(P(A\to O_j)\) is the probability of the counterfactual conditional “if \(A\) were performed, \(O_j\) would obtain.” To avoid confusion with the material conditional, it is often better to write this as

\[
V_C(A)=\sum_j D(O_j)\,P(A \mathbin{\square\!\to} O_j),
\]

where \(A\mathbin{\square\!\to}O_j\) means “if \(A\) were done, \(O_j\) would happen.” If outcomes are stochastic, the relevant quantity is the probability or chance that \(O_j\) results from doing \(A\), not merely the probability that \(O_j\) is observed after learning that \(A\) occurred.

If it were always true that

\[
P(A\mathbin{\square\!\to}O_j)=P(O_j\mid A),
\]

then CDT and EDT would coincide. But the source notes that David Lewis proved the probability of a conditional cannot generally be identified with the corresponding conditional probability. In decision-theoretic terms: what would happen if you intervened is not always what you should expect to observe conditional on the action.

Gibbard and Harper also showed that, under certain assumptions about counterfactual logic, statistical independence between the action \(A\) and the relevant counterfactual \(A\mathbin{\square\!\to}O_j\) is sufficient to make the counterfactual probability equal to the conditional probability. In those cases CDT and EDT agree. The interesting cases are precisely those where this independence fails: where performing an action is evidence about some background condition that also affects the outcome, even though the action does not causally affect that background condition.

---

## 2. Dependency hypotheses and what CDT “holds fixed”

A useful way to formalize CDT is to introduce dependency hypotheses. A dependency hypothesis \(K\) is a description of how outcomes depend causally on actions. It may specify causal structure, structural equations, chances, or the values of background variables that influence outcomes. Let \(p(K)\) be the agent’s prior probability over such hypotheses.

A natural CDT evaluation is then

\[
V_C(A)=\sum_K p(K)\sum_j D(O_j)\,P_K(O_j\mid \operatorname{do}(A)),
\]

where \(P_K(O_j\mid \operatorname{do}(A))\) is the probability of \(O_j\) under an intervention setting the action to \(A\), according to hypothesis \(K\). EDT, by contrast, evaluates

\[
V_E(A)=\sum_j D(O_j)\,P(O_j\mid A),
\]

which can be decomposed as something closer to

\[
V_E(A)=\sum_K p(K\mid A)\sum_j D(O_j)\,P_K(O_j\mid A).
\]

The important difference is this: EDT conditions on the action, so the action can change the probability assigned to \(K\). CDT uses the prior \(p(K)\), or more generally the distribution that would obtain under intervention, not the distribution obtained by treating the action as mere evidence.

This does not mean that CDT ignores evidence. Before acting, the agent may condition on all available observations. If she sees smoke, hears testimony, or remembers past data, she should update her beliefs. What CDT refuses to do is to let the hypothetical performance of the action update beliefs about variables that the action does not causally affect. If choosing \(A\) is merely symptomatic of some bad background condition, CDT does not treat that symptom as a reason against \(A\), unless \(A\) itself causally contributes to the bad outcome.

This is the sense in which CDT “holds fixed” the agent’s views about the causal structure or about causally relevant background states. The source quotes Andy Egan’s criticism that CDT’s requirement to hold fixed unconditional credences in dependency hypotheses can lead to unintuitive decisions. That criticism is important, and I return to it later.

---

## 3. Operationalizing counterfactual probabilities

The source correctly says that CDT does not itself specify a unique algorithm for calculating counterfactual probabilities. One proposal mentioned in the source is Lewis’s imaging technique: to evaluate \(P(A\mathbin{\square\!\to}O)\), move probability mass from each possible world \(w\) to the closest possible world \(w_A\) in which \(A\) holds. The source also notes a difficulty: this requires knowing what one would believe if one were certain of \(A\), which may itself be a conditional belief, inviting regress.

A more constructive operational interpretation, not explicitly present in the source but widely used in modern causal inference, is to represent the agent’s causal beliefs by a structural causal model. I will develop this as a practical reading of CDT.

A structural causal model consists of:

1. A set of variables \(V=\{X_1,\dots,X_n\}\), including an action variable \(A\) and outcome variable \(O\).
2. Exogenous variables \(U\) with probability distribution \(P(U)\).
3. Structural equations
   \[
   X_i=f_i(\operatorname{PA}_i,U_i),
   \]
   where \(\operatorname{PA}_i\) are the direct causal parents of \(X_i\).

An intervention \( \operatorname{do}(A=a) \) modifies the model by replacing the structural equation for \(A\) with the constant equation \(A=a\). The resulting model determines a counterfactual outcome \(O_a(u)\) for each value of the exogenous variables. The counterfactual or interventional probability is then

\[
P(A\mathbin{\square\!\to}O=o)=P_U(O_a=o).
\]

Thus CDT’s expected utility becomes

\[
V_C(a)=\sum_o D(o)\,P_U(O_a=o).
\]

In graphical terms, if the model is a causal Bayesian network with conditional distributions \(P(X_i\mid \operatorname{PA}_i)\), the post-intervention distribution is given by the truncated factorization formula

\[
P(v\mid \operatorname{do}(a))
=
\mathbf 1\{v_A=a\}
\prod_{X_i\ne A}P(x_i\mid \operatorname{pa}_i).
\]

Intuitively: set \(A=a\), leave the other structural mechanisms unchanged, and propagate the effects forward.

This gives a practical recipe:

1. List the available actions or policies.
2. Specify the relevant causal model: variables, causal arrows, and conditional distributions.
3. Replace the action variable by the proposed intervention.
4. Compute the resulting distribution over outcomes.
5. Take the expected utility.
6. Choose the action or policy with the highest expected utility.

When the causal graph is known and there is no unmeasured confounding, one can sometimes compute interventional probabilities from observational data. For example, if \(C\) is a set of variables satisfying the backdoor criterion relative to \(A\) and \(O\), then

\[
P(O=o\mid \operatorname{do}(A=a))
=
\sum_c P(O=o\mid A=a,C=c)\,P(C=c).
\]

This is the familiar adjustment formula. It says: to estimate the causal effect of \(A\) on \(O\), condition on the right background variables \(C\), then average over their prior distribution. Crucially, the weighting uses \(P(C)\), not \(P(C\mid A)\). That is the statistical expression of CDT’s refusal to treat the action as evidence about its own background causes.

This operationalization does not eliminate all philosophical difficulty. One still needs a causal model, and causal models are often uncertain, incomplete, or ambiguous. But it gives CDT a precise computational form once the relevant causal assumptions are supplied.

---

## 4. Policies, not merely one-shot actions

The source mostly discusses single actions, but many decision problems concern policies: rules mapping observations or histories to actions. CDT can be extended naturally to policies.

A policy \(\pi\) is a function, possibly stochastic, from information states to actions. To evaluate \(\pi\), we intervene on the decision node or nodes so that the agent follows \(\pi\). The value of the policy is

\[
V_C(\pi)=\mathbb E[D\mid \operatorname{do}(\pi)].
\]

In a sequential problem, \(\operatorname{do}(\pi)\) means replacing the agent’s decision rule at each relevant time by \(\pi\), then propagating the effects through the causal model.

This policy perspective matters because an action’s causal relevance can depend on when and how it is chosen. If a policy is publicly adopted before another agent moves, then the policy can causally influence the other agent’s behavior. CDT counts that effect. If another agent’s behavior is merely correlated with your choice because of a common cause or a prediction made before your choice, CDT does not count that correlation as a causal effect of your current action.

For example, if you can publicly commit to a course of action before a predictor forms a prediction, your policy may causally affect the predictor’s prediction. If the prediction has already been made and your current action cannot affect it, CDT treats the prediction as fixed. This distinction is central to Newcomb’s problem and related puzzles.

---

## 5. Examples

### 5.1 Apples, oranges, and expected causal effects

The source gives a simple example. Eating an apple causes happiness; eating an orange causes sadness. Then CDT recommends the apple. The complication arises when the apple may be good or bad.

Let \(G\) be the event that the apple is good, with prior probability \(p\). Eating a good apple causes happiness \(H\); eating a bad apple causes sadness \(S\). Suppose the utility of happiness is \(u_H\), the utility of sadness is \(u_S\), and eating an orange gives known utility \(u_O\). Then

\[
V_C(\text{eat apple})
=
p\,u_H+(1-p)\,u_S.
\]

CDT recommends eating the apple just in case

\[
p\,u_H+(1-p)\,u_S > u_O.
\]

This illustrates the basic structure: uncertainty about causal effects is handled by averaging over possible causal states, but the probabilities used are the probabilities appropriate to the intervention, not merely evidential associations unless those associations are causally justified.

### 5.2 King David and Bathsheba

The source gives Gibbard and Harper’s example of King David. David wants Bathsheba but fears that summoning her may provoke revolt. Kings are either charismatic or uncharismatic. Charismatic kings tend to act justly and rarely face successful revolts; uncharismatic kings tend to act unjustly and frequently face revolts. Unjust acts themselves do not cause revolt; the underlying lack of charisma does. David does not know whether he is charismatic.

Let:

- \(C\): David is charismatic.
- \(S\): David summons Bathsheba.
- \(R\): successful revolt.
- \(b>0\): direct benefit to David from summoning Bathsheba.
- \(L>0\): loss from revolt.

The causal structure is roughly:

\[
C \to R,
\qquad
C \to S \text{ (as evidence or disposition)},
\qquad
S \to b,
\]

but, by assumption,

\[
S \not\to R.
\]

CDT evaluates the intervention \(\operatorname{do}(S)\). Since \(S\) does not cause \(C\), and \(S\) does not cause \(R\), the probability of revolt under \(\operatorname{do}(S)\) is the same as under \(\operatorname{do}(\neg S)\). The difference in causal expected utility is therefore simply the direct benefit:

\[
V_C(S)-V_C(\neg S)=b.
\]

So CDT recommends summoning Bathsheba.

EDT reasons differently. Summoning is evidence that David is uncharismatic, because uncharismatic kings are more likely to act unjustly. Therefore,

\[
P(C\mid S)<P(C\mid \neg S),
\]

and hence

\[
P(R\mid S)>P(R\mid \neg S).
\]

The evidential difference is

\[
V_E(S)-V_E(\neg S)
=
b - L\bigl(P(R\mid S)-P(R\mid \neg S)\bigr),
\]

which may be negative. EDT can therefore recommend abstaining. CDT says that this mistake comes from treating David’s action as bad news about his charisma, even though the action cannot change his charisma and does not cause revolt.

### 5.3 Newcomb’s problem

In Newcomb’s problem, a reliable predictor has already predicted whether the player will take only box B or both boxes A and B. Box A contains \$1,000. Box B contains \$1,000,000 if the predictor predicted one-boxing, and \$0 if the predictor predicted two-boxing.

The payoff table is:

\[
\begin{array}{c|cc}
& \text{B full} & \text{B empty} \\
\hline
\text{One-box} & 1{,}000{,}000 & 0 \\
\text{Two-box} & 1{,}001{,}000 & 1{,}000
\end{array}
\]

Given the standard assumption that the prediction has already been made and cannot be causally affected by the current choice, CDT treats the content of box B as fixed with respect to the intervention. Relative to each causally relevant state, two-boxing is better:

- If B is full: two-boxing gives \$1,001,000, one-boxing gives \$1,000,000.
- If B is empty: two-boxing gives \$1,000, one-boxing gives \$0.

Thus two-boxing dominates one-boxing in causal expected utility. CDT recommends taking both boxes.

EDT reasons that one-boxing is strong evidence that the predictor predicted one-boxing, so box B is probably full. If the predictor is 99% accurate, EDT assigns approximately

\[
P(\text{B full}\mid \text{one-box})=0.99,
\]
\[
P(\text{B full}\mid \text{two-box})=0.01.
\]

Then

\[
V_E(\text{one-box})
\approx 0.99 \times 1{,}000{,}000
=990{,}000,
\]

while

\[
V_E(\text{two-box})
\approx
0.01 \times 1{,}001{,}000
+
0.99 \times 1{,}000
=11{,}000.
\]

EDT recommends one-boxing. The source notes that philosophers disagree about which answer is rational, but that CDT’s answer is two-boxing.

A policy perspective clarifies the assumption. If the agent could choose a policy before the predictor made its prediction, and the predictor would observe or predict that policy, then the policy might have a causal effect on the predictor’s behavior. In the standard formulation, however, the prediction is already fixed, so CDT evaluates the current act as unable to change it.

---

## 6. Criticisms, counterexamples, and unresolved questions

The source identifies two major difficulties for CDT.

First, CDT is vague about how to compute counterfactual probabilities. Lewis’s imaging is one proposal, but it raises regress problems. My structural-causal-model interpretation is one way to make CDT operational, but it transfers the burden to causal modeling. If the agent lacks a reliable causal model, CDT does not magically produce the right probabilities. It tells you how to decide once you have interventional probabilities; it does not by itself tell you how to learn or identify them.

Second, there are many alleged counterexamples. Egan’s diagnosis, quoted in the source, is that CDT’s problems stem from holding fixed the agent’s unconditional credences in dependency hypotheses. In cases where the agent’s action is strong evidence about her own type, intentions, or background traits, CDT may recommend actions that seem intuitively irrational.

The source mentions several such cases.

### 6.1 Death in Damascus

In the Death in Damascus scenario, Death predicts where you will be tomorrow and waits there. If Death is a reliable predictor, then whatever location you choose, Death is likely to be there. A simple act-based CDT evaluation may see no causal advantage of fleeing or staying, because Death’s prediction is treated as fixed. Yet intuitively, the situation seems to demand some strategic response, perhaps randomization.

A policy-based CDT might ask whether adopting a randomized policy can causally affect Death’s ability to predict. If Death predicts the outcome of your randomizer, randomization does not help. If Death can predict only deterministic dispositions, randomization may help. The source does not settle this; the right CDT response depends on the detailed causal model of prediction and choice.

### 6.2 The Adversarial Offer

The source describes an example due to Oesterheld and Conitzer. Two boxes are offered. The buyer may buy one box or none, but not both. Each box costs \$1. The seller previously put \$3 in each box that she predicted the buyer would not acquire. The seller’s prediction is believed to be accurate with probability \(0.75\).

CDT, holding the seller’s predictions fixed, can reason that at least one box likely contains \$3. If the buyer selects a box at random, the expected contents may appear to be at least \$1.50, exceeding the \$1 cost. Thus CDT may require buying a box. But because the buyer’s choice is correlated with the seller’s prediction, the chosen box is likely empty, and the seller profits. The example is meant to show that CDT can voluntarily lose money when its actions are predictable.

A policy-oriented CDT might try to evaluate the whole purchasing rule rather than the isolated act. But whether that fully resolves the example depends on how the predictor relates to the buyer’s policy, randomization, and timing. The source presents the case as a challenge, not as a solved problem.

### 6.3 The Psychopath Button

Egan’s psychopath button is another important case. Paul can press a button that kills all psychopaths. Paul thinks a world without psychopaths would be much better. However, he is confident that only a psychopath would press the button. He strongly prefers living in a world with psychopaths to dying.

If Paul is not a psychopath, pressing the button causes a good outcome: psychopaths are eliminated and Paul lives. If Paul is a psychopath, pressing the button kills him along with the others. EDT says that pressing is strong evidence that Paul is a psychopath, so he should not press. CDT, holding Paul’s psychopath status fixed, may say that if his prior probability of being a psychopath is low enough and the value of eliminating psychopaths is high enough, pressing has positive causal expected value.

The source says that, according to Egan, pretty much everyone agrees Paul should not press, yet CDT endorses pressing. This is a sharp illustration of the tension between causal efficacy and self-diagnostic evidence. CDT says: do not avoid a beneficial action merely because performing it would be bad news about your type. Critics say: when your choice reveals what kind of agent you are, that evidence cannot be so easily ignored.

### 6.4 Responses and uncertainty

The source notes that Jim Joyce, a prominent defender of CDT, argues that CDT can take into account information about what one is inclined or likely to do. One way to develop this response is to evaluate policies or dispositions rather than isolated acts, and to include the agent’s self-knowledge in the prior causal model. This is a reasonable operational direction, and it fits naturally with the policy-intervention framework described above.

Still, the source also notes stronger attacks: Oesterheld and Conitzer argue that CDT agents can be subjected to diachronic Dutch books and can voluntarily lose money in multiple predictor scenarios. These results suggest that simple act-based CDT is not always dynamically coherent. Whether a more sophisticated policy-based CDT can answer all such objections is not settled by the source, and it remains an active philosophical question.

My own view is that CDT is most defensible when understood as a rule for evaluating interventions relative to an explicitly specified causal model. Many apparent paradoxes arise because the informal description leaves the causal model underspecified. Once we ask whether the predictor observed the policy, whether the agent can randomize, whether the action is a symptom of a hidden trait, or whether the prediction is already fixed, we can often see exactly where CDT and EDT diverge. But this clarification does not prove that CDT gives the intuitively correct answer in every case. It only makes the disagreement precise.

---

## 7. Conclusion

Causal decision theory evaluates actions by their expected causal consequences. Formally, it replaces evidential conditional probabilities with counterfactual or interventional probabilities:

\[
V_C(A)=\sum_j D(O_j)\,P(A\mathbin{\square\!\to}O_j).
\]

Its central philosophical commitment is that an action should not be penalized merely because it is evidence of bad background conditions, unless the action causally contributes to the bad outcome. In cases where actions are independent of the relevant counterfactuals, CDT agrees with EDT. In Newcomb-style problems, predictor cases, and self-diagnostic cases, the two theories diverge.

The reference article leaves open the crucial computational question: how should an agent calculate counterfactual probabilities? A natural operational answer is to use structural causal models, replacing the action variable by an intervention and computing the resulting outcome distribution. For dynamic problems, the corresponding object is a policy intervention. This makes CDT precise enough for many applications, but it also reveals the theory’s dependence on causal assumptions. Where those assumptions are contested, or where predictors and self-knowledge create reflexive dependencies, CDT remains philosophically controversial.

---

## References

Gibbard, A., & Harper, W. L. (1981). Counterfactuals and two kinds of expected utility. In *Ifs: Conditionals, Beliefs, Decision, Chance, and Time* (pp. 153–190).

Lewis, D. (1976). Probabilities of conditionals and conditional probabilities. *The Philosophical Review, 85*(3), 297–315.

Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy, 59*(1), 5–30.

Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.

Wikipedia contributors. (2026). Causal decision theory. In *Wikipedia, The Free Encyclopedia*. Revision 1381555528. https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528