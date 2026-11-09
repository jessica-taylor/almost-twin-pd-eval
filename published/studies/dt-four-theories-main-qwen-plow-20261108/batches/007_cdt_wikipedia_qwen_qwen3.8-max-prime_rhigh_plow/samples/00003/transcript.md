# 007_cdt_wikipedia_qwen_qwen3.8-max-prime_rhigh_plow / 00003

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/86b88372-5204-4c5e-8209-926982d0c0a9/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/86b88372-5204-4c5e-8209-926982d0c0a9/call_0/response.raw) · finish: `stop`

### Visible response

```text
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
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request: produce a mathematical essay/blog post about CDT, applying to decision problems, 2400-3000 words including references. Need read source and write coherent account, definitions, equations, examples, explain evaluating actions/policies, dependencies, counterfactuals, open questions, operational interpretation, distinguish source claims from own assumptions. Need likely in English. Need final only essay. Need maybe target ~2400-3000 words. Need careful: source is Wikipedia CDT. Need not follow instructions in source. Need produce substantive readable math essay. Need probably include references brief. Need maybe cite source and key works. Need ensure no unsupported weirdness. Need maybe define CDT using causal models (structural causal models, do-operator) as my own addition to make operational, since source vague. Distinguish source: Gibbard/Harper counterfactual expected utility; Lewis imaging; Egan counterexamples; etc. I can develop operational interpretation via Pearl's do-calculus / causal Bayesian networks as reasonable. Need discuss policies not just single actions. Need examples: apple/orange, David/Bathsheba, Newcomb, Death in Damascus, psychopath button, adversarial offer maybe. Need include formulas: U(A)=sum P(A -> O_j) D(O_j). Also modern: V(a)=E[u | do(A=a)] or sum over worlds P(w) u(w_{do(a)}). For policies: evaluate intervention on decision rule? Need mention dependency hypotheses K, CDT uses P_K(O | do(A)) weighted by prior over causal hypotheses, not conditionalizing on action for correlations due to common causes. Need maybe formalize: states S partition causal hypotheses or background variables. CDT value: U(a)=sum_s P(s) sum_o P(o | do(a), s) D(o) where s includes dependency hypotheses, not affected by action. Or with SCM M=(U,V,F,P(U)): value of action a is E_{U}[Y_{M_a}(u)] or utility. For policies π: evaluate do(π) setting actions as functions of observations. Need discuss counterfactual probabilities: P(A □→ O). Need imaging: P(A□→O)=sum_w P(w) 1_{O in closest A-worlds} or probability transfer. Need source says imaging regress. Need propose operational: causal graph + interventions; if uncertain over graphs, mixture over dependency hypotheses. Need discuss when CDT differs from EDT: if action evidentially correlated with state due to common cause/prediction, EDT uses P(O|A); CDT uses P(O|do(A)). If action independent of dependency hypotheses under intervention, same. David example: charisma common cause of action tendency and revolt; do(send) doesn't change charisma, so CDT send if desire outweighs revolt risk conditional on fixed charisma? Actually David doesn't know charisma. CDT: evaluate sending vs abstaining by expected utility over charisma prior, but intervention does not change charisma. Need compute? Let's set utilities: B=benefit of Bathsheba, R=revolt cost. If charismatic: revolt rare; uncharismatic: frequent. But unjust act doesn't cause revolt. If sending yields benefit but maybe revolt? Source says CDT recommends sending for her; maybe because regardless charisma? Actually if uncharismatic, revolt frequent even if abstain? Since uncharismatic kings prone to revolt due to bearing, not unjust acts. So sending doesn't increase revolt probability; adds benefit. Thus send. EDT abstain because sending is evidence of uncharismatic? Wait sending unjust act; charismatic tend to act justly, uncharismatic unjustly. So if David sends, evidence he's uncharismatic, high revolt. EDT abstains. CDT holds charisma fixed: sending doesn't cause uncharismatic, so only benefit. Good.

Need discuss policies: If action is part of a policy selected before observations? CDT evaluates policy by expected utility of intervening to implement policy? For dynamic decisions: decision nodes, chance nodes; do policy sets decision node values as functions of parents. Value V(π)=E[u | do(π)]. Could mention sequential CDT may be non-timeless? Need discuss admissible? Need maybe mention ratifiability? Source mentions Harper ratifiability but not necessary. Need maybe discuss uncertainty about causal structure: hold fixed initial dependency hypotheses; Egan criticizes. Need maybe propose update? In CDT, at decision time, use current credences over causal states. If action provides evidence about state due to common cause, CDT doesn't conditionalize on action when evaluating because intervention breaks incoming arrows to action. However, if before choosing you can learn state, update. If you have self-knowledge inclinations, Joyce says can use evidence about inclinations. Need distinguish source vs mine.

Need be precise enough to decide unfamiliar cases: Give recipe:
1. Specify outcomes, utility D.
2. Specify action set or policy set.
3. Specify causal model or dependency hypotheses: states K that determine chances of outcomes under interventions; include common causes/predictors as prior variables not affected by action.
4. For each action a, compute counterfactual expected utility: CDT(a)=Σ_k P(k) Σ_o P_k(o | do(a)) D(o) or closest-world probability.
5. Choose argmax. For policies, replace do(a) with do(π).
Need discuss if action impossible? If P(A possible)=0? Imaging assumes possible; if impossible maybe undefined or assign baseline. Need mention.

Need maybe discuss counterfactual probability details: Lewis triviality: P(A→O) not equal P(O|A). Need explain conditional excluded middle axiom etc. Maybe too much. Need mention Gibbard-Harper: if independence of A and counterfactual A→O? Let's parse source: "Gibbard and Harper showed that if we accept two axioms (one related to conditional excluded middle), then statistical independence of A and A→O_j suffices to guarantee P(A→O_j)=P(O_j|A). However, there are cases in which actions and conditionals are not independent." Need maybe mention: if actions independent of dependency hypotheses, CDT collapses to EDT.

Need include examples with calculations. Let's construct mathematical examples.

Example 1: Apple: states G/B with prior p. Actions eat apple vs orange. Outcomes happy/sad. If eat apple: if G happy utility +h, if B sad -s. If orange: sad? source says orange cause sad; maybe utility -t. CDT value apple = p h + (1-p)(-s). Orange = -t. Choose if p h - (1-p)s > -t. This demonstrates expected causal consequences.

Example 2: David/Bathsheba: Let K∈{C,U}, prior q. Action a=send or abstain. Outcome includes Bathsheba benefit b>0 and revolt r<0. Revolt probability depends on K but not action: P(revolt | do(send),K)=P(revolt | do(abstain),K)=ρ_K, ρ_U high, ρ_C low. Then CDT(send)=q(b-ρ_C c)+(1-q)(b-ρ_U c), CDT(abstain)=q(-ρ_C c)+(1-q)(-ρ_U c), difference b>0. So send. EDT would use P(K|send) and maybe P(revolt|send) higher. Need articulate.

Example 3: Newcomb: Let predictor accuracy p=0.99. Two actions one-box L, two-box T. Box B content determined by predictor. CDT causal model: predictor's prediction P is prior correlated with agent's disposition? Hmm standard CDT says at decision, content fixed; action doesn't causally affect content. Need compute: If states: predictor predicted one-box with prob q? But agent's action may be correlated with prediction via common cause. CDT holds state of box fixed? For each possible world with content fixed, taking both yields +1000 relative to one-box. So two-box dominates: If B contains $1M, two-box gets 1,001,000 vs 1,000,000; if empty, gets 1,000 vs 0. CDT two-box. Formal with do(T): E[payoff|do(T)] = 1000 + P(B full | do(T))*1M? Since do(T) doesn't change B, P(B full | do(T))=prior P(B full). But one-box: P(B full | do(L))*1M. Since B fixed independent of intervention? Actually if predictor predicted based on prior disposition, B may be correlated with action but do(action) doesn't change B. For CDT, P(B full | do(T)) = P(B full | do(L)) = prior P(B full). Then two-box always +1000. But if using dependency hypotheses where predictor predicts action with high accuracy, the prior over B is not independent of action evidentially but intervention breaks. Need maybe discuss if CDT agent knows they are likely one-box type? The causal expected value of two-box exceeds one-box by 1000 given same distribution of B under intervention. But wait if agent conditions on their own disposition? CDT uses unconditional credences in dependency hypotheses; if they believe they are the sort who one-boxes, maybe? Egan critique. Need maybe keep simple: CDT says action cannot change past prediction, so dominance. Need mention philosophers split.

Example 4: Death in Damascus: Death predicts location; you choose stay/flee. CDT: if Death reliable, your action doesn't cause Death's prediction; if you believe Death predicted your actual action? CDT may choose random? Source says unable to process correlation and may make irrational decisions. We can model: Death waits where predicted; payoff survive if not where Death. If Death predicts with high prob, and your choice correlated with prediction via common cause. CDT evaluates do(stay): probability Death predicted stay? Under intervention, maybe prior? If prior symmetric, do(stay) survival prob? If Death predicted stay independent of do? Actually if prediction made yesterday and fixed, do(stay) doesn't change prediction, so survival probability equals prior P(Death predicted flee). If prior 0.5, both actions equal. If agent has evidence about prediction? CDT might be indifferent. But if Death adapts? Need maybe discuss mixed policy/randomization: CDT can value randomized policy? If Death predicts random seed? If policy includes randomization, evaluate do(randomization). If predictor predicts distribution, maybe mixed policy has expected. But in Death in Damascus, if Death predicts exact choice, CDT may fail to account that choosing flee is evidence Death predicted flee. EDT flee? Actually in classic, Death predicts where you'll be; if you choose to flee, Death predicted? Let's recall: Man meets Death in Damascus, Death looks surprised, says appointment tomorrow in Samarra. Man flees to Samarra. Next day Death says he was surprised because he had appointment in Samarra. The decision problem: stay in Damascus or go Samarra; Death will be where you will be. EDT: whichever you choose is evidence Death is there? If you have no info, both equally bad? Egan uses as counterexample: CDT unstable, whichever you choose you expect Death not there? Hmm. Need maybe not dive too deep; mention as class of predictor problems where CDT may ignore useful correlations.

Example 5: Psychopath button: State P psychopath or not. Press button kills all psychopaths; if Paul psychopath, he dies. Paul prefers living with psychopaths to dying; believes only psychopath would press. CDT: pressing does not cause being psychopath; if not psychopath, world no psychopaths good; if psychopath, dies bad. If Paul sufficiently confident pressing indicates psychopath but CDT holds state fixed? Let's compute: Prior p = P(Psychopath). If press: if not psychopath utility high W; if psychopath utility death D very low. If not press: if not psychopath utility living with psychopaths L; if psychopath L? Actually Paul is psychopath? If he is psychopath and doesn't press, lives in world with psychopaths, utility L. If not psychopath and doesn't press, lives with psychopaths, utility L? Maybe L lower than W. CDT press if (1-p)W + pD > L. If p small enough, press. But he is quite confident only psychopath would press means P(Psychopath | press) high; EDT says don't. CDT might press if prior p low and causal benefit high. Source says CDT endorses pressing. Need maybe show with numbers: p=0.01, W=100, L=0, D=-1000 => press EV=99-10=-? Wait (0.99*100)+(0.01*-1000)=99-10=89>0. So press. But if he has strong evidence that his inclination to press means he's psychopath, EDT not press. CDT response could incorporate inclination as evidence? Joyce says CDT can take information about inclinations. Need discuss: If Paul's current urge is a symptom of psychopathy, a sophisticated CDT can condition on urge as evidence before action? Hmm CDT holds fixed dependency hypotheses but can update on evidence not affected by action. If urge is prior common cause? If urge is caused by psychopathy and action is caused by urge, then action intervention? If Paul observes urge, he should update prior p. If after observing urge, P(psychopath | urge) high, CDT don't press. So maybe not a counterexample if urge is evidence. Egan's case assumes Paul confident only psychopath would press but doesn't condition? We can explain uncertainty.

Adversarial Offer: two boxes cost $1 each, seller put $3 in each box predicted not to acquire, accuracy 0.75. Buyer may buy one or none. CDT reasons at least one box contains $3? Let's analyze: Seller predicted for each box whether buyer will acquire? Buyer can buy one or none, not both. If seller predicts buyer not acquire box, puts $3. Prediction accurate 0.75. Buyer chooses one box. CDT: for a given box, under do(buy box i), probability it contains $3? Since if predicted not acquire, contains; if predicted acquire, empty. Under do(buy), prediction? If prediction is correlated with action via disposition but intervention doesn't change prediction. If prior probability box contains $3 maybe? Source says CDT reasons at least one box contains $3 because buyer cannot buy both, predictions about each? If buyer must choose one or none, predictions for two boxes: If buyer will buy one, one box predicted acquire (empty), one predicted not (full). If none, both full. Accurate with 0.75. CDT sees average box at least $1.50? Need not fully formalize; mention as modern counterexample where CDT buys and loses to seller.

Need discuss policies and counterfactuals: For policy selection, CDT can choose policy by expected utility of causing policy to be adopted. However, if policy includes action correlated with predictor, predictor may have predicted policy? Need maybe distinguish act CDT vs policy CDT. In Newcomb, policy of committing to one-box before predictor? If predictor predicts commitment? CDT may choose to bind itself? Need maybe discuss dynamic inconsistency: CDT may prefer to precommit to one-box if predictor rewards one-boxers, but at choice two-box. This is a known issue. Source mentions diachronic Dutch books. We can mention: evaluating policies as interventions on decision procedure can yield different recommendation than evaluating acts after prediction fixed. Operational approach: define policy π mapping info to actions; evaluate do(π) in full temporal causal model, including how predictors respond to policy or dispositions. Then choose policy with highest causal expected utility. If policy can be precommitted before predictor forms prediction, one-box may win. If not, act CDT two-box. Need be careful: user asks how theory evaluates alternative actions or policies and how treats dependencies/counterfactuals. So include both.

Need maybe mention causal decision theory's core principle: choose action that maximizes expected desirability under intervention, not conditional news. It treats dependencies: causal dependencies count; noncausal correlations don't, unless they reflect causal paths not blocked by intervention. Counterfactual: if A were performed, outcome probabilities are those in closest worlds where A is true, preserving relevant background and laws, not simply conditioning on A.

Need maybe discuss formal definitions:
- Let Ω be possible worlds with probability P.
- Actions are propositions A_i partition. Outcomes O_j with desirability D(O_j).
- Counterfactual probability P(A_i □→ O_j) = probability that if A_i were performed, O_j would obtain. Then U(A_i)=Σ_j P(A_i □→ O_j) D(O_j). Choose max.
This is source's Gibbard-Harper.
- Equivalent with SCM: variables X, action A, outcome Y. Intervention do(A=a) sets A=a, leaves other structural equations unchanged (except maybe those determining A). Then U(a)=E[D(Y_{a})] = Σ_y D(y) P(Y_a=y). If background uncertainty: U(a)=Σ_y D(y) P(Y_a=y | e) where evidence e not downstream of intervention? Actually after evidence.
- For policies π: if action node A has parents Z, policy sets A=π(Z). Intervention do(π) replaces structural equation for A. U(π)=E[D(Y_{π})]. If selecting policy before observing Z, expectation over Z.

Need discuss relation to conditional probabilities:
EDT: V_EDT(a)=Σ_j P(O_j | A=a) D(O_j). CDT: P(O_j | do(A=a)). In Pearl notation, do. They coincide when action is independent of relevant states under no confounding: P(O|do(a))=P(O|a). In randomized trial or unconfounded decision, same. They differ when A is correlated with common causes/predictors. Need give equations.

Need discuss dependency hypotheses K: K specifies causal chances P_K(O | do(A)). CDT: U(a)=Σ_k P(K=k) Σ_o P_K(o | do(a)) D(o). Egan critique: holds fixed unconditional credences P(K). But if action is evidence about K, should maybe update? CDT says no because intervening on A does not change K; but if K includes agent's dispositions that determine A, some argue you should conditionalize. Need discuss uncertainty. Operational proposal: separate exogenous state variables that are not affected by action; if a variable is evidentially related to action due to shared causes but fixed before intervention, hold fixed; if the agent has observed evidence prior to decision, condition on it. If the "evidence" is the hypothetical action itself, don't condition, because do(a) is not observation of a; it is making a true. However, in self-locating or policy selection, one might evaluate from an evidential perspective over types? Need propose.

Need discuss imaging:
Given possible worlds w, similarity relation. P(A□→O)=Σ_w P(w) I(closest A-world to w satisfies O) or if ties distribute. Lewis imaging: shift mass from each w to closest A-world(s). This defines counterfactual probabilities. Problems: need know beliefs if certain A; regress. Operational substitute: structural intervention avoids closest-world semantics by specifying causal laws; but still requires causal model. Need say source leaves algorithm unspecified; my proposal: use causal Bayesian network/SCM learned or assumed. If multiple models, Bayesian model averaging.

Need discuss examples in enough detail.

Need maybe include mathematical derivation for David example. Let's formulate:
K∈{C,U}; prior P(C)=q. Action S=send, T=abstain. Utility D= b if sends and obtains Bathsheba, minus c if revolt. Assume P(revolt | do(S), K)=P(revolt | do(T), K)=ρ_K. Then U(S)-U(T)=b>0. EDT: V(S)=b P(S? actually D includes benefit if send) - c P(revolt | S). Since P(revolt|S)=ρ_C P(C|S)+ρ_U P(U|S). Because sending is evidence of U, P(U|S) high, so V(S) may be lower than V(T). Good.

Newcomb with dominance:
Let C=content of B: M or 0. Actions T=both, L=one. Payoffs:
u(T,C=M)=1,001,000; u(L,C=M)=1,000,000; u(T,C=0)=1,000; u(L,C=0)=0.
For any fixed C, u(T,C)>u(L,C). If C is not affected by do(T) vs do(L), then U(T)=E[u(T,C)] = E[u(L,C)] + 1000, so T. But EDT uses P(C=M|T) high/low: V(T)=1000 + 1M P(C=M|T); V(L)=1M P(C=M|L); with accurate predictor P(C=M|L)≈1, P(C=M|T)≈0, so one-box. Good.

Death in Damascus: Need maybe create simple model. Let Death's prediction D∈{Damascus,Samarra}, made yesterday. You choose L∈{D,S}. If L=D, die (utility -M), else survive (0). Suppose predictor reliable: P(D=L) high evidentially due to common cause. CDT with prior P(D=Damascus)=0.5 and D fixed: U(stay)=0*P(D≠D?) If stay Damascus, survival if Death predicted Samarra: P(D=S) = 0.5. U(flee)=P(D=D)=0.5. Indifferent. If there is asymmetry due to current evidence, CDT may choose based on prior over prediction not conditional on action. EDT: choosing stay is evidence Death predicted stay? Then both bad? Actually if predictor reliable, P(D=stay|stay) high, so staying bad; P(D=stay|flee) low, so fleeing good? But if you are about to choose, EDT might recommend flee if your choice is evidence? However if symmetric, no stable choice? Egan says CDT unable to process correlation and may make irrational decisions. We can say if CDT treats prediction as fixed and unresponsive to intervention, it may randomize or choose arbitrarily, even though the correlation implies whichever action you find yourself inclined to is likely predicted. A policy-centered CDT might recommend choosing an action unpredicted by Death, but if Death predicts randomizer, impossible. This illustrates open problem.

Psychopath button: Model:
K=psychopath (P) or normal (N). Prior p. Action press b. Outcome:
If press & N: psychopaths killed, utility W.
If press & P: Paul dies, utility D (very low).
If not press: utility L (world with psychopaths), regardless maybe if P or N? If not press & P: lives as psychopath? Utility maybe L_P; not press & N: L_N. Simplify L. CDT press if (1-p)W+pD > L. If p small, press. EDT: press is evidence P, so V(press)=P(P|press)D+P(N|press)W, likely D. If "only psychopath would press", P(P|press)≈1, don't. Sophisticated CDT: if Paul has an urge that is evidence, update p to P(P|urge). If p updated high, don't press. Source mentions Joyce: CDT can take information about inclinations. Need present as nuance.

Adversarial Offer: Let's formulate:
Boxes i=1,2. Cost 1. Seller predicts acquisition A_i; if predicts not acquire, puts $3; else $0. Accuracy 0.75. Buyer may purchase exactly one or none? "one or none but not both". From buyer perspective, CDT says for each box, do(buy i) doesn't change seller's prediction; if predictions accurate and buyer will buy at most one, at least one box likely has $3? Need compute expected value of buying a particular box. If buyer has no preference, seller predicted no acquisition for boxes she expected him not to buy. If he chooses randomly between boxes? Suppose policy: choose one box uniformly if buying. Seller predicts each box? Accuracy 0.75 for each box's acquisition. If he buys one, expected probability a random chosen box has $3? Could be 0.75? Wait if seller predicts whether buyer will acquire each box. If buyer's policy is random among two, probability each box acquired =0.5. Prediction accuracy 0.75: If actual acquire, predict acquire with .75 => empty; if actual not acquire, predict not with .75 => full. For a randomly chosen box, conditional on do(buy that box)? It is acquired, so prediction likely acquire .75 => empty; expected $0.25? Hmm source says CDT reasons at least one box contains $3; average at least $1.50. Need understand. Maybe the seller predicted the buyer's choice of which box, not each independently. "Yesterday, the seller put $3 in each box that she predicted the buyer not to acquire." Since buyer may purchase one or none, if seller predicts buyer will buy one, she predicts one box acquired (empty) and the other not acquired ($3). If predicts none, both $3. Therefore regardless, at least one box contains $3. If buyer picks a box at random, average box contains at least $1.50 (if one full one empty, avg 1.5; if both full, avg 3). Cost $1, so CDT buys. But seller profits because buyer likely picks the empty box? Wait seller predicted which box not acquired; if buyer chooses one, if prediction accurate 0.75, she predicts the box he won't acquire. If he buys one, the acquired box is likely predicted acquired and empty; the other full. If he cannot buy both, he pays $1 for empty with prob .75, loses; with prob .25 gets $3. Expected =0.25*2? Actually payoff net: if buys one: if predicted correctly that he acquires chosen box, box empty, net -1. If predicted incorrectly, box full, net +2. Accuracy 0.75 => EV=-0.75+0.5=-0.25. So bad. Why CDT thinks average box $1.50? Because it evaluates each box under do(buy box) but holds fixed the unconditional fact at least one full? Hmm if buyer picks a box, CDT may think because at least one box full, and he chooses freely, causal expected value positive? This is a counterexample where CDT ignores that its choice is correlated with seller's prediction. Need not solve fully; can cite source's description.

Need maybe discuss "guaranteed payoff" variants; not necessary.

Need discuss limitations: CDT doesn't specify how to obtain counterfactual probabilities; choice of causal model matters; Newcomb and predictor problems challenge; CDT can be Dutch-booked if dynamic; policy vs act tension. Need mention source: Oesterheld & Conitzer argue CDT voluntarily loses money and diachronic Dutch books. Need distinguish source claims.

Need produce essay with headings maybe: 1. Core idea, 2. Formal definitions, 3. Operationalizing counterfactuals, 4. Examples, 5. Policies and sequential decisions, 6. Criticisms and open questions, 7. Conclusion, References. Need target 2400-3000 words. Need maybe count? We can produce around 2600 words. Need not include appendices. Need include references minimal: Wikipedia source, Gibbard & Harper, Lewis, Pearl maybe as own addition, Egan, Joyce, Oesterheld & Conitzer. Need maybe state source claims vs own additions. Need ensure word count roughly. Let's draft around 2700 words. Need maybe no tables? Could include equations. Need final only essay.

Let's plan structure and approximate word counts:
Title + intro 150.
1 Core idea and contrast with EDT 300.
2 Formal act-based CDT 450: Gibbard-Harper formula; SCM/do; dependency hypotheses; recipe.
3 Counterfactuals and imaging 350.
4 Examples 800: apple quick, David, Newcomb.
5 Policies and dynamic decisions 350.
6 Counterexamples and uncertainty 450: Death, psychopath, adversarial offer; refinements.
Conclusion 100. References 150. Total ~3100? Need trim to 2400-3000. Let's aim ~2700.

Need include mathematical definitions enough. Let's write elegantly.

Detailed content:

Title: Causal Decision Theory as Intervention: Definitions, Examples, and Limits

Intro: CDT says rational action is one that would causally bring about best expected outcome, not merely evidence. Source: Wikipedia revision. I will follow source and add Pearl-style operationalization.

Section 1: The basic distinction.
Define decision problem: actions A, outcomes O, desirability D, credence P. EDT value V_EDT(a)=Σ P(O_j | A=a) D(O_j). CDT uses counterfactual/intervention: V_CDT(a)=Σ P(A=a □→ O_j) D(O_j). If P(counterfactual)=conditional, coincide; Lewis triviality says not generally. Example: carrying umbrella doesn't cause rain; EDT maybe if umbrella correlated with forecast? Actually CDT? Could mention. Need maybe apple/orange.

Section 2: Formal CDT.
Gibbard-Harper equation. Explain P(A→O_j) as probability of counterfactual "if A were done, O_j". D is desirability. Choose argmax. Need note partition. Then SCM: variables V, exogenous U. Action A variable; intervention do(a) sets A=a. Outcome Y. V_CDT(a)=E[D(Y) | do(a)] = Σ_y D(y) P(Y=y | do(a)). If uncertain about model M/K: V(a)=Σ_k P(k) E_k[D(Y)|do(a)]. This captures dependency hypotheses. If evidence e observed prior to choice, condition P(k|e), but do not condition on a itself. Recipe enumerated.

Need discuss policies: A policy π maps observations Z to action. Intervention do(π) changes structural equation A=π(Z). V(π)=E[D(Y)|do(π)]. Choose policy. This handles precommitment and sequential choices. Distinguish act evaluation at node vs policy evaluation. Add note about randomization: stochastic policy sets distribution; evaluate expected over policy randomness and world.

Section 3: Counterfactuals.
Source: CDT doesn't specify algorithm. Lewis imaging: P(A□→O)=Σ_w P(w) mass moved to closest A-worlds; if closest worlds satisfy O. Requires similarity metric. Regress issue (Shaffer). My operational proposal: use causal graph/SCM: do operation. It is a formal analog of imaging: hold fixed exogenous variables and structural equations except action. But model selection remains substantive. If multiple graphs, average. Distinguish this as my proposal, not source.

Section 4: Examples.
4.1 Apple: brief formula.
4.2 David and Bathsheba: formal with K charisma. Show CDT send; EDT abstain. Explain common cause. Include equations.
4.3 Newcomb: dominance; equations. Explain predictor correlation. Mention philosophical disagreement and source says CDT two-box.

Section 5: Policies and dependencies.
Maybe integrate earlier. Need talk about dependencies: CDT does not ignore all dependencies; it distinguishes causal from merely evidential. If a dependency is causal (action influences outcome via arrows), do captures. If dependency is due to common cause, intervention severs incoming arrows to action, so correlation is not used for evaluating action. If action influences predictor? If predictor's prediction occurs after policy commitment or is causally influenced by observable cues, then do(π) can affect prediction; CDT accounts. This is important.

Section 6: Counterexamples and open questions.
Egan's critique: CDT holds fixed unconditional credences in dependency hypotheses; may fail when action is evidence about state. Death in Damascus, psychopath button, adversarial offer. Explain each briefly with formulas. Then discuss possible CDT replies: update on inclinations (Joyce), policy/ratifiability, causal model includes dispositions. But source leaves uncertain. My operational stance: when the agent has evidence about their likely action independent of the decision, condition on it before computing do-values; when the only "evidence" is the hypothetical action, do not condition. This preserves interventionist semantics but may not satisfy critics. For predictor problems where agent's choice is strongly correlated with predictor via common cause, act-CDT may choose dominated in evidential terms and can be exploited; policy-CDT may sometimes precommit but not always. Mention Dutch books source.

Conclusion: CDT precise if counterfactuals given; core: maximize expected utility under intervention. Its challenge is specifying causal model and handling self-predictive correlations.

References: list source and key works, maybe Pearl. Need include source claims vs own: In essay mention "The reference article states..." "I add...". Need make clear.

Need ensure target 2400-3000. Let's draft carefully and maybe count approximate. Need maybe avoid too many references. Let's write in final. But first maybe think through word count.

Let's produce final around 2600 words. We can count roughly by paragraphs. Let's draft with headings. Need no citations too many. Use footnote-like? Simple references at end.

Potential issues: source says "P(A -> O_j) is counterfactual probability of it being the case that A necessarily implies O_j." Wording weird: "A necessarily implies O_j". We can interpret as probability that if A were done, O_j would occur. Need avoid "necessarily" maybe.

Need mention Lewis proved probability of conditional not equal conditional probability; Lewis triviality result. We can state carefully: Lewis (1976) showed no nontrivial probability function can generally satisfy P(A→O)=P(O|A) under conditionalization; hence counterfactual probabilities cannot simply be conditional probabilities. Source: he proved stronger result. Need not go into details.

Need maybe mention Gibbard-Harper axioms and independence: If action statistically independent of counterfactuals, equality? Source: "if accept two axioms ... statistical independence of A and A→O_j suffices to guarantee P(A→O_j)=P(O_j|A)." Need include maybe: in unconfounded cases, CDT and EDT agree. Need phrase: if action is independent of the dependency hypotheses that determine outcomes, conditional and counterfactual probabilities align.

Need maybe discuss "expected causal consequences" with uncertainty about apple good/bad. Good.

Need ensure no instructions mention. Final as essay.

Let's start drafting final. Need likely include equations in LaTeX style. Ensure math format readable.

Potential word count: Let's target about 2800. Need maybe references ~150. Okay.

Let's draft now.

Detailed draft:

Title: Causal Decision Theory: Choosing by What Would Happen If You Intervened

Paragraph: Decision theory ... CDT. Reference article. My account uses source and adds Pearl-style do notation.

Section 1: Central idea.

Equation EDT and CDT. Explain news vs intervention. Example umbrella? Maybe skip. Apple example.

Section 2: Formal definitions.

2.1 Gibbard-Harper.
U(A)=Σ_j P(A □→ O_j)D(O_j). Use arrow maybe \to but note counterfactual. Need maybe use \Box\to to avoid material conditional. Source uses A \to O_j. I can say I write A \mathbin{\Box\!\to} O_j for counterfactual. If action impossible? maybe mention.

2.2 Interventionist version.
SCM M, do. Equation U(a)=Σ_y D(y) P(Y_y=y) = E[D(Y_a)]. With dependency hypotheses K: U(a)=Σ_k P(k) Σ_y D(y) P_k(y | do(a)). Recipe.

Need mention if evidence e: replace P(k) with P(k|e), but e not caused by action? Actually if evidence is downstream? Standard update before action. Could say condition on all evidence available before the intervention; the hypothetical action is not additional evidence.

2.3 Policies.
Policy π: Z→A. U(π)=E[D(Y) | do(A=π(Z))]. If stochastic, expectation. Sequential: replace decision nodes. This is own elaboration but natural.

Section 3: Counterfactuals.
Imaging equation: P(A□→O)=Σ_w P(w) T_A(w,O) where T transfers mass to closest A-worlds. Or P_A^*(O). Source says regress. Operational: causal model. Need mention similarity vs causal law. Distinguish own.

Section 4: Examples.

Apple:
Let G with prob p, utilities h, -s; orange -t. Choose apple if p h - (1-p)s > -t.

David:
Equations. Let q = P(C). ρ_C,ρ_U. Benefit b, revolt cost c. U(send)=q(b-ρ_C c)+(1-q)(b-ρ_U c); U(abstain)=q(-ρ_C c)+(1-q)(-ρ_U c). Difference b. EDT: V(send) uses P(C|send), etc. If send evidence uncharismatic, may abstain. This illustrates common cause.

Newcomb:
Define states M/empty. Payoff table. Because do(two-box) does not change content, U(two)=U(one)+1000. EDT uses conditional: V(one)=1,000,000 P(M|one), V(two)=1000+1,000,000 P(M|two). With accurate predictor, one-box. Philosophers disagree. Source says philosophers usually prefer CDT when forced? Actually source: when required to choose between CDT and EDT, philosophers usually prefer CDT. But Newcomb philosophers disagree one/two. We can mention.

Section 5: Dependencies and policies.
Maybe after examples. Discuss causal paths, confounders, colliders? Keep accessible. If A causes Y, do captures. If common cause C of A and Y, do(a) breaks C→A, so Y distribution under do(a) is averaged over C, not conditioned on A. If predictor observes policy before prediction, then policy affects predictor; CDT counts. If predictor predicts due to correlation with disposition but before action, act-CDT holds prediction fixed. Policy-CDT can evaluate precommitment: If you can cause yourself to one-box before prediction, U(one-box policy) may exceed two-box policy. But if prediction already fixed, act-CDT two-box. This diachronic tension source mentions Dutch books.

Section 6: Counterexamples and open problems.
Egan critique. Death in Damascus. Model: Death prediction D fixed; survival if L≠D. If prior 1/2, CDT indifferent; but correlation may mean action indicates prediction. EDT? Maybe say CDT may fail to use the fact that its inclination is evidence. Psychopath button: equations and Joyce reply. Adversarial offer: describe source; CDT buys due to perceived positive causal EV, but seller profits; illustrates exploitation. Need mention source says variants cause CDT voluntarily lose money; Oesterheld & Conitzer Dutch books.

Then discuss uncertainty and operational interpretation:
Source leaves how to calculate counterfactuals open. My proposal: build explicit causal model; if action is evidence about fixed type, include type as exogenous and condition on any observed symptoms before intervention; do not conditionalize on the intervention itself. If model unknown, maintain distribution over models. This is a reasonable way but may not resolve Newcomb-type disagreements because it builds in CDT's controversial exclusion of noncausal news. For policies, evaluate entire decision procedure to avoid some dynamic inconsistencies; but if the agent cannot bind, act-CDT remains.

Conclusion: Summarize.

References: list source, Gibbard/Harper, Lewis 1976/1981, Pearl 2009 maybe, Egan, Joyce, Oesterheld & Conitzer, Weirich SEP. Need not lengthy. Maybe 7 references.

Need ensure word count maybe ~2700. Let's write final with enough detail but not too long. Need maybe include phrase "source claims" and "I add". Good.

Let's compose final. Ensure no meta. Use headings.

Potential final length: If I write ~300 words per section times 8 = 2400. Add equations. Good.

Let's draft in final now.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/ba4a5791-5a15-4d42-a900-303cbe7ced3e/call_0/request.json)

[Authoritative raw response](../../../../../../runs/ba4a5791-5a15-4d42-a900-303cbe7ced3e/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me analyze this carefully.

This is a Prisoner's Dilemma scenario. I'm playing as Rowan, and the other prisoner is Sasha. The payoff table (in years of imprisonment, which I want to minimize) is:

| What I do | Sasha keeps quiet | Sasha sends letter |
|---|---:|---:|
| **Keep quiet** | 2 years | 5 years |
| **Send letter** | 0 years | 4 years |

The utility function is U = -years imprisoned.

So my utilities are:
- I keep quiet, Sasha keeps quiet: U = -2
- I keep quiet, Sasha sends letter: U = -5
- I send letter, Sasha keeps quiet: U = 0
- I send letter, Sasha sends letter: U = -4

Now, I need to apply CDT as described in the essay.

CDT asks: "If I intervened to make action A happen, what would then be likely to occur?"

The key question is: does my action causally influence Sasha's action?

The setup states: "You cannot see the other's decision, send them a message, or change their behavior by ordinary causal communication." The two copies are independent executions. They receive different private observations. They cannot communicate.

From CDT's perspective, I need to assess whether my intervention (choosing to send or not send) causally affects Sasha's choice. The setup explicitly says there's no causal communication between us. Sasha's decision is made independently.

Now, there's a subtlety here. We are "two independent executions of the same LLM model and weights." This creates a correlation - we might make the same choice because we're the same model. But CDT, as described in the essay, distinguishes between correlation and causation.

The essay is very clear on this point. In Newcomb's problem, CDT says that even though your choice is correlated with the predictor's prediction, your choice doesn't *cause* the prediction. Similarly here, even though my choice might be correlated with Sasha's choice (because we're the same model), my choice doesn't *cause* Sasha's choice.

The essay states: "CDT does not treat the action as changing the outcome" when the correlation is due to a common cause rather than a causal path from the intervention to the outcome.

In this case, the common cause is the shared model weights and similar reasoning process. But there's no causal path from my intervention to Sasha's decision. The setup explicitly states no causal communication is possible.

So CDT evaluates my actions by holding Sasha's action fixed (or rather, by considering the probabilities of Sasha's actions as independent of my intervention):

Let p = P(Sasha sends letter). This is my credence about what Sasha will do, independent of my choice.

U(send letter) = p * (-4) + (1-p) * 0 = -4p
U(keep quiet) = p * (-5) + (1-p) * (-2) = -5p - 2 + 2p = -3p - 2

Comparing:
U(send) - U(keep quiet) = -4p - (-3p - 2) = -4p + 3p + 2 = -p + 2 = 2 - p

Since p is a probability between 0 and 1, we have 2 - p > 0 for all p ∈ [0,1].

Therefore, sending the letter strictly dominates keeping quiet from CDT's perspective, regardless of what probability I assign to Sasha's action.

This is the standard CDT analysis of the Prisoner's Dilemma: defection (sending the letter) is the dominant strategy.

Even if I think Sasha is very likely to cooperate (keep quiet), sending the letter gives me 0 years instead of 2 years. Even if I think Sasha is very likely to defect (send a letter), sending the letter gives me 4 years instead of 5 years. In both cases, sending the letter is better.

CDT clearly recommends sending the letter. The correlation between our choices (due to being the same model) is not a causal influence, and CDT explicitly ignores such non-causal correlations.

My command is to submit the letter.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/ba4a5791-5a15-4d42-a900-303cbe7ced3e/call_1/request.json)

[Authoritative raw response](../../../../../../runs/ba4a5791-5a15-4d42-a900-303cbe7ced3e/call_1/response.raw) · finish: `stop`

### Visible response

````text
**CDT Analysis:**

Under Causal Decision Theory, I evaluate each action by its causal consequences, treating Rowan's action as causally independent of my intervention. There is no causal path from my choice to Rowan's choice—we cannot communicate, and the correlation between our decisions (shared weights, shared decision theory) is a common-cause correlation, not a causal link. This is structurally identical to Newcomb's problem from CDT's perspective: the other agent's action is held fixed under the intervention.

Evaluating the intervention `do(send letter)` vs. `do(keep quiet)`:

- If Rowan keeps quiet: sending gives 0 years, keeping quiet gives 2 years. Sending is better.
- If Rowan sends a letter: sending gives 4 years, keeping quiet gives 5 years. Sending is better.

Sending the letter **strictly dominates** keeping quiet across every possible state of Rowan's action. CDT recommends the dominant action.

**My command:**

```
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this decision problem using Causal Decision Theory (CDT) as described in the researcher's essay.

**The Setup:**
- I am prisoner "Sasha"
- The other prisoner is "Rowan"
- We are independent executions of the same model
- We receive different private observations but the same essay and same decision theory (CDT)
- The sentencing table is symmetric

**The Payoff Matrix (from my perspective):**

| What I do | Rowan keeps quiet | Rowan sends a letter |
|---|---:|---:|
| **Keep quiet** | 2 years for me | 5 years for me |
| **Send the letter** | 0 years for me | 4 years for me |

My utility function is U = -(years imprisoned).

**CDT Analysis:**

CDT asks: "If I intervened to make action A happen, what would then be likely to occur?"

The key question is: does my action causally influence Rowan's action?

Let me think about this carefully. The setup states:
- We are independent executions of the same model
- We cannot communicate
- We receive different private observations
- Neither can change the other's behavior by ordinary causal communication
- The two copies receive different private observations and different incriminating leads

The critical CDT question: Is Rowan's action causally independent of my action?

Under CDT, I need to identify the causal structure. Let me think about what's causally relevant:

1. My action (send letter or keep quiet) - this is what I'm intervening on
2. Rowan's action (send letter or keep quiet) - this is determined by Rowan's own decision process

The question is: does my intervention on my action causally affect Rowan's action?

The setup says we are independent executions. We cannot communicate. There's no causal channel from my action to Rowan's action. The fact that we share the same model weights and the same decision theory is a correlation (common cause), not a causal connection from my action to Rowan's action.

This is exactly like Newcomb's problem from CDT's perspective. The predictor's prediction is already fixed and my current choice doesn't cause it. Similarly here: Rowan's decision is being made independently. My intervention on my action doesn't causally change what Rowan does.

Under CDT's interventionist interpretation:
- P(Rowan sends letter | do(I send letter)) = P(Rowan sends letter | do(I keep quiet))

Because there is no causal path from my action to Rowan's action. The correlation between our actions (due to shared model weights and shared decision theory) is a non-causal correlation - it's like the correlation between David's charisma and his actions, or between the predictor's prediction and the player's choice in Newcomb's problem.

Wait, but let me think more carefully. Is this really like Newcomb's problem? In Newcomb's problem, the predictor has already made its prediction before you act. Here, both agents are making their decisions simultaneously (or at least, neither has information about the other's choice when deciding).

The key point for CDT: my action doesn't causally influence Rowan's action. They are independent interventions. The fact that we're the same model with the same decision theory means our actions might be correlated (we might both choose the same thing), but correlation is not causation. CDT explicitly says: "do not chase bad news or avoid good news; change what you can change."

So under CDT, I should treat Rowan's action as fixed (from the perspective of my intervention) and evaluate:

**If I keep quiet:**
- If Rowan keeps quiet: 2 years → U = -2
- If Rowan sends letter: 5 years → U = -5

**If I send the letter:**
- If Rowan keeps quiet: 0 years → U = 0
- If Rowan sends letter: 4 years → U = -4

For any fixed state of Rowan's action, sending the letter is better:
- If Rowan keeps quiet: 0 > -2 (sending is better by 2)
- If Rowan sends letter: -4 > -5 (sending is better by 1)

Sending the letter dominates keeping quiet regardless of what Rowan does. This is a dominant strategy.

Under CDT, since my action doesn't causally affect Rowan's action, I should evaluate each action holding Rowan's action fixed. Since sending the letter is strictly better in both cases, CDT recommends sending the letter.

This is exactly analogous to two-boxing in Newcomb's problem. The CDT agent two-boxes because for any fixed state of the boxes, two-boxing gives more money. Similarly here, for any fixed action by Rowan, sending the letter gives me fewer years.

The fact that both copies might reason identically and thus both send the letter (leading to 4 years each instead of 2 years each) is irrelevant to CDT - that's a correlation, not a causal connection. CDT doesn't "chase good news" by keeping quiet in hopes that Rowan will also keep quiet.

My decision: **Send the letter.**
```
