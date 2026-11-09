# Causal decision theory as expected utility under intervention

Causal decision theory (CDT) is a school of thought in decision theory holding that a rational agent should choose the action that causes the best outcome in expectation. The reference article contrasts this with evidential decision theory (EDT), which recommends the action that would be the best “news”: the action whose being taken would be evidence of the best outcome (Wikipedia contributors 2026). CDT’s central intuition is that rational choice should track what an action brings about, not merely what it indicates.

This essay reconstructs CDT formally, explains how it evaluates actions and policies, and develops an operational interpretation using interventionist causal models. The source article supplies the core counterfactual formulation and several classic examples, but it leaves open how counterfactual probabilities are to be computed. I will distinguish the source’s claims from my own proposed operationalization.

---

## 1. Expected utility and the evidential alternative

A simple decision problem consists of:

- a set of possible actions \(A\);
- a set of possible outcomes \(O_1,\dots,O_n\);
- a desirability or utility function \(D(O_j)\) measuring how good outcome \(O_j\) is.

Standard expected utility theory evaluates an action by averaging the utilities of possible outcomes weighted by probabilities. EDT uses ordinary conditional probabilities:

\[
V_{\text{EDT}}(A)=\sum_j P(O_j\mid A)D(O_j).
\]

Here \(P(O_j\mid A)\) is the probability of outcome \(O_j\) conditional on receiving the news that action \(A\) was performed.

EDT is attractive in ordinary cases. If eating an apple makes you happy with high probability and eating an orange makes you less happy, EDT tells you to eat the apple. But EDT can also recommend actions because they are symptoms of good outcomes, not because they produce them. If a certain action is correlated with success only because successful people tend to take that action, EDT may recommend imitating the symptom rather than producing the cause.

CDT is meant to avoid this mistake. It asks not “What would the world probably be like if I learned that I had done \(A\)?” but “What would the world probably become if I actually did \(A\)?”

---

## 2. Gibbard and Harper’s counterfactual formulation

The reference article gives the classical formal statement of CDT in Gibbard and Harper (1981). The causal expected utility of an action \(A\) is

\[
U(A)=\sum_j P(A \to O_j)D(O_j),
\]

where \(D(O_j)\) is the desirability of outcome \(O_j\), and \(P(A\to O_j)\) is the probability of the counterfactual claim that if \(A\) were performed, \(O_j\) would obtain. I will write this counterfactual as

\[
A \mathbin{\Box\!\to} O_j.
\]

Thus the CDT value of \(A\) is

\[
U_{\text{CDT}}(A)=\sum_j P(A \mathbin{\Box\!\to} O_j)D(O_j).
\]

The crucial difference from EDT is that \(P(A \mathbin{\Box\!\to} O_j)\) is not generally the conditional probability \(P(O_j\mid A)\). David Lewis proved that probabilities of conditionals cannot in general be identified with conditional probabilities without triviality (Lewis 1976). If one did identify them, CDT would collapse into EDT.

Gibbard and Harper showed that under certain logical assumptions, including a controversial principle related to conditional excluded middle, statistical independence between the action \(A\) and the relevant counterfactual \(A \mathbin{\Box\!\to} O_j\) is sufficient to make

\[
P(A \mathbin{\Box\!\to} O_j)=P(O_j\mid A).
\]

So in cases where the act is independent of the counterfactual structure, CDT and EDT agree. They diverge when an action is evidence about some underlying state that also affects the outcome, but the action does not causally affect that state.

The source’s King David example illustrates this. David wants to summon Bathsheba but fears revolt. Kings are either charismatic or uncharismatic; charisma is fixed. Charismatic kings rarely face successful revolts; uncharismatic kings often do. Unjust acts do not themselves cause revolt; uncharismatic kings simply tend both to act unjustly and to suffer revolts. EDT says David should abstain, because summoning Bathsheba would be evidence that he is uncharismatic. CDT says that charisma cannot be changed by the decision, so David should evaluate the act by its causal consequences, not by what it reveals about his fixed type. The source says CDT recommends sending for her.

---

## 3. An operational interpretation: interventions and causal models

The reference article emphasizes an important gap: CDT does not itself specify an algorithm for computing the counterfactual probabilities \(P(A\mathbin{\Box\!\to}O_j)\). One proposal mentioned in the source is Lewis’s “imaging”: to evaluate the probability of a counterfactual, move probability mass from each possible world to the closest possible world in which \(A\) holds. But imaging requires a similarity metric over possible worlds and may lead to regress, since we must know what we would believe if we were certain of \(A\).

A natural modern operationalization, which I add to the source rather than find explicitly stated there, is to interpret CDT using causal interventions. Let

\[
P(O_j\mid do(A))
\]

denote the probability of outcome \(O_j\) under an intervention that sets the action to \(A\). Then CDT’s value becomes

\[
U_{\text{CDT}}(A)=\sum_j P(O_j\mid do(A))D(O_j).
\]

The symbol \(do(A)\) is important. It is not conditioning on \(A\). Conditioning asks what is probable given evidence that \(A\) occurred. Intervention asks what would happen if \(A\) were imposed on the world by an external manipulation.

A structural causal model gives this idea precise content. Such a model contains variables, structural equations describing how variables depend on their causes, and a probability distribution over exogenous noise variables. To intervene on \(A\), one replaces the structural equation for \(A\) by the fixed assignment \(A:=a\), leaving the other equations unchanged. The resulting intervened model determines the counterfactual distribution of outcomes.

If the agent is uncertain about which causal model is correct, we can average over “dependency hypotheses” \(K\). A dependency hypothesis specifies the relevant causal structure: which variables influence which outcomes, and how. Then CDT evaluates

\[
U_{\text{CDT}}(A)
=
\sum_k P(K=k)
\sum_j P(O_j\mid do(A), K=k)D(O_j).
\]

This formula captures an important feature emphasized by critics such as Egan: standard CDT holds fixed the agent’s prior credences in dependency hypotheses. It does not replace \(P(K=k)\) with \(P(K=k\mid A)\). The act may be evidence about which dependency hypothesis is true, but CDT does not treat the hypothetical performance of the act as evidence to be conditionalized on when evaluating the act’s causal efficacy.

This interventionist reading also extends naturally to policies. In sequential problems, an agent does not merely choose a single action but a rule mapping observations or histories to actions. Let \(\pi\) be such a policy. Then CDT can evaluate

\[
U_{\text{CDT}}(\pi)
=
\sum_j P(O_j\mid do(\pi))D(O_j),
\]

where \(do(\pi)\) means intervening so that the agent’s decision variables are set according to \(\pi\). This is my proposed operational extension. It is not explicitly contained in the source article, but it makes CDT applicable to unfamiliar dynamic problems: specify the causal model, replace the decision rule by the proposed policy, compute the resulting outcome distribution, and maximize expected desirability.

---

## 4. Examples

### 4.1 Ordinary uncertainty

Suppose you may eat an apple or an orange. The apple may be good or bad. If good, eating it causes happiness with utility \(10\); if bad, it causes sadness with utility \(-6\). You believe the apple is good with probability \(0.7\). The orange gives utility \(2\) regardless.

If the apple’s quality is independent of your action, then causal and conditional probabilities coincide:

\[
U_{\text{CDT}}(\text{apple})
=
0.7(10)+0.3(-6)
=
5.2.
\]

Since \(5.2>2\), CDT recommends the apple. EDT agrees. This is typical when actions do not diagnose hidden causes of outcomes.

### 4.2 King David as a common-cause problem

Let \(C\) be David’s charisma, \(S\) the action of summoning Bathsheba, and \(R\) a successful revolt. Charisma is fixed. It influences both David’s tendency to act unjustly and the probability of revolt. The causal structure is roughly:

\[
C \rightarrow S,
\qquad
C \rightarrow R.
\]

But summoning does not causally affect charisma. In interventionist notation,

\[
P(C\mid do(S))=P(C),
\]

whereas EDT uses

\[
P(C\mid S),
\]

which may differ sharply. If summoning Bathsheba is typical of uncharismatic kings, then \(P(C=\text{uncharismatic}\mid S)\) is high, making EDT fear revolt. CDT holds \(P(C)\) fixed and asks only whether the direct benefits of summoning outweigh the revolt risk associated with David’s prior probability of being uncharismatic. The source says CDT recommends summoning.

### 4.3 Newcomb’s problem

In Newcomb’s problem, a predictor has already predicted whether the agent will take only box B or both boxes A and B. Box A visibly contains \$1,000. Box B contains \$1,000,000 if the predictor predicted one-boxing, and nothing if the predictor predicted two-boxing.

Let \(S\) be the predictor’s prediction. If \(S=\text{one}\), box B contains \$1,000,000; if \(S=\text{two}\), box B contains nothing. The payoffs are:

| Prediction | One-box | Two-box |
|---|---:|---:|
| Predicted one-box | \$1,000,000 | \$1,001,000 |
| Predicted two-box | \$0 | \$1,000 |

CDT, as presented in the source, assumes that the prediction is already fixed and the current action does not causally affect it. Therefore the agent evaluates each causal state separately. In both states, two-boxing yields \$1,000 more than one-boxing. Thus two-boxing causally dominates one-boxing:

\[
U_{\text{CDT}}(\text{two-box})
=
U_{\text{CDT}}(\text{one-box})+1000.
\]

EDT reasons differently. One-boxing is strong evidence that the predictor predicted one-boxing, so EDT assigns a high probability to box B containing \$1,000,000. Two-boxing is strong evidence that box B is empty. With a sufficiently accurate predictor, EDT recommends one-boxing.

The source notes that philosophers often prefer CDT to EDT when forced to choose, but Newcomb’s problem remains controversial. The interventionist interpretation makes the modeling assumption explicit: CDT two-boxes only if the predictor’s state is not downstream of the agent’s intervention. If the predictor’s accuracy depends on causally simulating or depending on the agent’s choice, the causal model may be different, and the CDT recommendation could change. The source does not settle this modeling question.

---

## 5. Objections, predictor problems, and open questions

The reference article identifies two broad difficulties for CDT: vagueness about counterfactual computation, and counterexamples involving predictors or self-diagnostic actions.

### 5.1 Vagueness and imaging

CDT’s formal core uses counterfactual probabilities, but it does not say how an agent should compute them. Lewis’s imaging proposal moves probability mass to the closest worlds where the action is performed. This gives an intuitive picture: counterfactual reasoning is a kind of minimal revision of one’s beliefs. But it requires a notion of closeness between possible worlds. Different similarity metrics can yield different counterfactual probabilities. Moreover, if we must ask what we would believe if we were certain of \(A\), we face a potential regress: that question itself involves a conditional belief.

The structural-model approach I proposed avoids some of this vagueness by replacing similarity with explicit causal equations. Intervention is defined by changing the equation for the action variable. But this merely shifts the burden: one must still specify the correct causal model. CDT itself does not tell us which causal representation is right.

### 5.2 Death in Damascus and predictor problems

In the “Death in Damascus” scenario, Death predicts where you will be tomorrow and waits there. If Death is a reliable predictor, your choice of location is strongly correlated with Death’s prediction. The source says a CDT agent may be unable to process this correlation and may make irrational decisions.

The problem is that CDT wants to evaluate actions by their causal consequences, but in predictor cases the action may be diagnostic of a prediction that determines the outcome. If the prediction is fixed before the action, CDT may treat it as a causal state. But if the predictor is accurate precisely because it tracks the agent’s choice, then the correlation between choice and prediction seems decision-relevant. Critics argue that CDT’s insistence on holding fixed the agent’s prior dependency hypotheses can make it blind to this kind of instability.

### 5.3 Adversarial offers and money extraction

The source describes an “Adversarial Offer” case. Two boxes are offered; the buyer may buy one or none, but not both. Each box costs \$1. The seller put \$3 in each box she predicted the buyer would not acquire. The seller’s prediction is believed to be accurate with probability \(0.75\). According to the source, CDT reasons that at least one box contains \$3, so the average box contains at least \$1.50 in causal expected value, which exceeds the \$1 cost. Hence CDT requires buying a box. But this is profitable for the seller.

The broader point is that CDT agents can be exploited when their choices are predictable and the environment is arranged to punish the locally causal calculation. Oesterheld and Conitzer argue that such cases show CDT agents can voluntarily lose money and can be subject to diachronic Dutch books.

### 5.4 The psychopath button

Egan’s psychopath button case concerns Paul, who is deciding whether to press a button that would kill all psychopaths. Paul thinks a world without psychopaths would be better, but he is confident that only a psychopath would press the button. He prefers living in a world with psychopaths to dying.

The intuitive verdict, according to Egan, is that Paul should not press the button. Pressing would be strong evidence that Paul is a psychopath, and therefore that pressing would kill him or otherwise be disastrous. Yet Egan argues that CDT endorses pressing. The reason is that CDT holds fixed whether Paul is a psychopath and evaluates the causal effect of pressing given that fixed type. The action’s evidential bearing on Paul’s type is not allowed to change the causal expected utility calculation.

This example highlights a tension. Ordinary rationality often says that if an action would reveal something bad about you, that matters. CDT replies that rational action should change the world, not merely infer facts about it. But when the agent’s own type is uncertain, and the action is diagnostic of that type, this reply can seem unsatisfactory.

### 5.5 A possible refinement

The source mentions Jim Joyce’s defense of CDT: CDT can take into account information about what one is inclined or likely to do as evidence. This suggests a reasonable operational refinement, which I propose as follows.

Before making a decision, the agent may condition on any genuine evidence she has: observations, memories, known psychological tendencies, or even evidence about her likely deliberative outcome. That evidence can update her probabilities over dependency hypotheses. But once she evaluates a candidate action or policy, she should not treat the hypothetical performance of that very action as additional evidence about the causal structure. Instead, she should intervene on the decision variable.

In sequential form, this means CDT can evaluate policies conditional on information available before implementation. If Paul has evidence that he is psychopathic before deciding, he should condition on that evidence. If he has evidence only that he is tempted to press the button, he can condition on the temptation, but the final intervention is still evaluated by \(do(\text{press})\). This refinement does not fully dissolve every counterexample, but it clarifies where CDT draws the line between evidence used before choice and evidence manufactured by the hypothetical choice itself.

---

## 6. A practical recipe for applying CDT

A reader trying to apply CDT to an unfamiliar case can use the following procedure.

1. **List the actions or policies.** Decide whether the problem is a one-shot act or a policy mapping information to actions.

2. **Specify outcomes and utilities.** Assign desirabilities \(D(O_j)\) to the relevant outcomes.

3. **Construct a causal model.** Identify the variables that determine outcomes. Distinguish causal paths from mere evidential correlations. Include predictors, common causes, and background traits if they matter.

4. **Intervene on the action or policy.** Replace the decision variable’s normal determining equation with the proposed action or policy. Compute the resulting outcome distribution \(P(O_j\mid do(A))\) or \(P(O_j\mid do(\pi))\).

5. **Average over causal uncertainty if needed.** If there are multiple plausible dependency hypotheses \(K\), use prior probabilities \(P(K)\), not probabilities conditioned on the act being evaluated.

6. **Choose the action or policy with highest causal expected utility.**

This procedure makes CDT operationally usable, but it also reveals its sensitivity to causal modeling. Many disputes about CDT are really disputes about the correct causal representation of the decision problem.

---

## Conclusion

Causal decision theory says that rational choice should maximize expected desirability computed from counterfactual or interventionist probabilities, not from ordinary conditional probabilities. Its core formula, due to Gibbard and Harper, replaces EDT’s \(P(O_j\mid A)\) with \(P(A\mathbin{\Box\!\to}O_j)\). The theory captures the intuition that actions should be judged by what they cause, not merely by what they indicate.

The difficulty is that CDT needs a theory of counterfactuals or interventions. The source article leaves this open. An interventionist structural-model interpretation gives CDT a workable mathematical form and extends naturally to policies, but it requires explicit causal assumptions. In predictor problems, self-diagnostic actions, and adversarial environments, those assumptions become contentious. CDT remains powerful and philosophically central, but its verdicts depend heavily on how one represents the causal structure of the world.

---

## References

Gibbard, A., and Harper, W. L. 1981. “Counterfactuals and Two Kinds of Expected Utility.” In *Ifs: Conditionals, Beliefs, Decision, Chance, and Time*, 153–190.

Lewis, D. 1976. “Probabilities of Conditionals and Conditional Probabilities.” *Philosophical Review* 85 (3): 297–315.

Lewis, D. 1981. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59 (1): 5–30.

Pearl, J. 2009. *Causality*. 2nd ed. Cambridge University Press. Used here as an operational gloss on CDT’s counterfactual probabilities.

Wikipedia contributors. 2026. “Causal Decision Theory.” Revision 1381555528. Wikimedia Foundation.