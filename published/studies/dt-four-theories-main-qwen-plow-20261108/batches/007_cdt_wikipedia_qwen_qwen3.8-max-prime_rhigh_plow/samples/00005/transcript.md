# 007_cdt_wikipedia_qwen_qwen3.8-max-prime_rhigh_plow / 00005

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/70d90157-9357-46fa-acbd-d13833efe8bc/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/70d90157-9357-46fa-acbd-d13833efe8bc/call_0/response.raw) · finish: `stop`

### Visible response

```text
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
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request. Need produce substantive mathematical essay ~2400-3000 words including references. Need explain CDT and how apply to decision problems. Use source, distinguish source claims vs own proposals. Need likely write in English. Need analyze thoroughly.

We need craft essay. User says: "Researcher — mathematical essay / blog post explaining CDT and how to apply it to decision problems. Intended readers mathematically literate... Read human-written reference article ... Write your own coherent account of theory, with mathematical definitions, equations, examples, explanations... Aim precise enough reader could use essay to decide unfamiliar cases. Explain how theory evaluates alternative actions or policies and how treats relevant dependencies and counterfactuals. Where source leaves important question open, explain uncertainty and, if reasonable operational interpretation available, develop and justify it. Distinguish claims made by source from additional assumptions/proposals of your own. Write result as substantive, readable mathematical essay rather than answer to one assigned case. Use examples whenever help. Target approx 2,400–3,000 words, including references and any other material. Prioritize coherent complete explanation central definitions reasoning implications over exhaustive coverage. Avoid unnecessary repetition lengthy bibliographies appendices. Finish with brief conclusion."

Need likely produce essay with title, sections. Need include references maybe source and key works. Need not be too long? 2400-3000 words. Need maybe around 2700 words. We need be precise.

Need decide how formalize CDT. Source gives Gibbard-Harper formula U(A)=sum_j P(A -> O_j) D(O_j), where P(A -> O_j) counterfactual probability. Contrast EDT U(A)=sum P(O_j|A)D(O_j). Lewis: probability of conditional not equal conditional probability. Need explain intervention vs conditionalization. Could bring in do-operator / structural causal models as my own operational interpretation since source vague about algorithm. Source says CDT doesn't specify algorithm; Lewis imaging proposed but regress. Need develop operational interpretation: use causal graphs/SCMs, do(A), expected utility = E[D | do(A)] = sum_o D(o) P(o | do(A)). For counterfactual probabilities, if full SCM, P(A -> O) = P(O_{A}=true) maybe intervention. In possible worlds semantics: closest A-worlds. But for practical application: specify causal model (variables, DAG, structural equations, exogenous distributions), set action variable by intervention, propagate, compute distribution of outcomes. If causal model uncertain, average over dependency hypotheses with prior, but holding fixed dependency hypotheses? Need discuss Egan criticism: CDT holds unconditional credences in dependency hypotheses? Need nuanced.

Need include examples: apple/orange, David/Bathsheba, Newcomb, Death in Damascus maybe Adversarial Offer, Psychopath Button. Need show calculations. Need explain dependencies and counterfactuals: common causes vs effects, backdoor paths, conditioning vs intervening. Could mention EDT uses conditional probabilities and thus can be misled by evidential correlations; CDT cuts incoming arrows to action. Need mention policies: evaluate policy as intervention on decision rule or action at each information state; in dynamic setting use sequential CDT / do on policy. Need maybe discuss policies: action vs policy. Since user asks alternative actions or policies. Need include policy evaluation: For policy π mapping observations to actions, compute expected utility under do(π), perhaps using Gittins? We can define. Need be careful not to go beyond source too much but mark as own operationalization.

Need distinguish source claims: Source claims CDT says choose action causes best expected outcome, Gibbard-Harper formula, Lewis inequality, independence condition, David example, Newcomb two-box, criticisms vagueness, imaging regress, counterexamples (Newcomb, prisoner's dilemma/twin, Death in Damascus, adversarial offer, psychopath button), Joyce defense, Oesterheld Conitzer Dutch books. My additions: formalization via SCM/do-operator, causal graph rules, dependency hypotheses, operational algorithm, policy evaluation, causal sufficiency, uncertainty, ratifiability maybe. Need not overdo.

Need likely write as essay with headings:
1. Introduction: decision theory, actions, states, outcomes, utilities. CDT versus EDT.
2. Expected utility and two probability kernels: evidential conditional P(o|a) vs causal/interventional P(o|do(a)). Gibbard-Harper formula.
3. Counterfactuals and interventions: possible-world semantics, Lewis, imaging; then operational SCM. Define variables, structural equations, do. Formula: V_CDT(a)=Σ_o u(o) P(o | do(a)) = Σ_o u(o) P(A □→ O?) (use box arrow). Counterfactual probability P(a □→ o) = P(o under intervention a). Relationship to conditional if independence: if A independent of dependency hypotheses? Need define. Could present dependency hypotheses K_i describing causal relation from A to O. If P(K_i | A)=P(K_i), then EDT = CDT: P(o|a)=Σ_i P(o|a,K_i)P(K_i|a); CDT=Σ_i P(o|do(a),K_i)P(K_i). If action independent of K_i and within K_i no confounding? Need formulate. Gibbard/Harper independence of A and A->O_j sufficient under axioms. More practical: no unblocked backdoor paths from A to O. Need mention.

4. Applying CDT step-by-step:
- list actions/policies, outcomes, utility.
- specify causal model or dependency hypotheses: variables, DAG, structural equations or conditional distributions.
- identify action node; intervene do(A=a) (or policy intervention); remove incoming arrows to action.
- compute outcome distribution by propagation/truncated factorization: P(v | do(a))=∏_{X≠A} P(x | pa_x) with A fixed. If hidden confounders, need counterfactual/latent or bounds.
- compute expected utility; choose max.
Need mention if causal model uncertain, take expectation over models but do not update model by action as evidence except through legitimate observations. Need discuss "news" vs "use". In decision, action can provide evidence about agent type but CDT holds fixed causes not affected by action. But if action reveals pre-existing traits that affect outcomes, EDT may avoid action; CDT may choose if causal effect positive. David example.

5. Example: David/Bathsheba with numbers? We can create simple table. Let C=charismatic prior p. Action S=summon or not. Outcome revolt? Utility maybe desire Bathsheba +1, revolt -10, unjust? But source says EDT abstain, CDT summon because charisma cannot be changed. Need formalize: C influences both propensity to summon? Actually David's action? EDT: Summoning is evidence of uncharismatic? Wait in story: Charismatic kings tend to act justly, uncharismatic unjustly. Summoning is unjust; if David summons, evidence he is uncharismatic, and uncharismatic kings face revolts. But action doesn't cause charisma or revolt? Unjust acts themselves do not cause revolts; uncharismatic bearing causes revolts. Thus P(revolt | summon) high due to evidence. CDT: do(summon) does not change charisma, and no causal path from summon to revolt, so expected utility of summon includes benefit, no causal cost; choose summon if benefit positive. Need compute: P(C)=p. If C, utility of summon maybe b; if not C maybe b. Revolt risk unaffected by action; base risk depends on C but not action. Thus CDT value summon = b + base? Not choose = base? choose summon. EDT value summon = b + expected revolt given evidence (lower p(C|summon)); maybe negative.

6. Newcomb: predictor P, box B content determined by prediction. CDT with causal graph: Predictor's prediction causes box content; action does not cause prediction (assuming past fixed). But action and prediction correlated because predictor accuracy? Need in CDT action node has incoming arrows from predictor? Actually predictor predicted before action, so common cause? The predictor's model of agent may cause both prediction and action? In standard, prediction is prior and correlated with action due to predictor's accuracy. In a causal graph, if predictor's prediction is a cause of box content and maybe not of action; correlation between action and prediction arises from predictor's simulation? There is a tricky causal structure. CDT says intervention on action cannot change past prediction, so two-box dominates: given any content, both > one. Compute: If B has $1M, two gets 1,001,000 vs one 1,000,000; if empty, two gets 1,000 vs one 0. So causal expected utility of two is higher under either state. EDT conditions on action: P(B full | one) ~0.99, P(B full | two) ~0.01; one has higher evidential expected value. Need mention if predictor causally depends on action via simulation? If predictor's prediction is caused by your decision algorithm in a loop? Then CDT may need different model; source assumes prediction already set. Need discuss.

7. Policies and dynamic decisions: CDT evaluates policy by intervention setting decision rule. If action observed? Need define. For policy π, do(π) means replacing structural equation for action variables by π(observed variables). Expected utility = E[u | do(π)]. In sequential problems, optimize over policies with causal dynamic programming? But CDT may treat future choices? Need mention if policy can influence predictions or commitments, then CDT recognizes causal effect of policy on others' beliefs if policy is observable before their actions. E.g. precommitment can be causally effective. Need distinguish action at time t vs policy chosen earlier.

8. Dependencies and counterfactuals: relevant dependencies are causal pathways from action to outcome; common causes are held fixed via intervention; evidential dependencies not through action's causal influence are ignored for evaluation, though they can inform beliefs about states. Counterfactuals: evaluate what outcome would be if action taken, not what would be likely if we learned action taken. Could use Lewis closest-world: keep fixed laws and past except minimal changes to make A true; intervention semantics. Source: probability of conditional P(A -> O) not equal conditional P(O|A); if independence then equal. Need mention principle of conditional excluded middle and axioms? Source mentions. Could explain: If counterfactuals are stochastic, P(A □→ O) is chance of O in A-worlds. Under Gibbard-Harper axioms and statistical independence of action from counterfactual, equality with conditional. Cases fail independence (Newcomb, David). Need not deep.

9. Vagueness and operational interpretation: Source says CDT doesn't specify algorithm; Lewis imaging but regress. My proposal: use SCM/causal Bayesian network as operational interpretation. This requires a causal model; CDT itself is a decision rule given causal probabilities, not a theory of causal discovery. If model not known, agent must form credences over models; CDT says maximize expected utility with respect to those credences and interventions. If no identifiable causal effect, maybe sensitivity analysis, bounds, or decision under ambiguity. Need discuss. Need distinguish: This SCM interpretation is not in Wikipedia source; it is a common formalization (Pearl, Spirtes etc) and my suggested operational reading. Need mention limitations: causal sufficiency, determinism, exogenous variables; counterfactuals under nondeterminism. Need define do-calculus/truncated factorization. Need mention when only observational data and confounding, do-probability not equal conditional; need causal assumptions.

10. Counterexamples and open questions: Source lists criticisms. Need explain them: Death in Damascus: Death predicts location; CDT may randomize? Actually story: If you stay, Death predicted you stay? Let's recall: Death in Damascus: man sees Death in Damascus, flees to Samarra; Death says appointment in Samarra. In decision variant: choose stay/flee, Death predicts where you'll be and goes there. If predictor reliable, both options have high probability of Death there conditional on action. CDT: action doesn't cause Death's prediction? If Death's prediction is prior and correlated, no causal advantage, maybe randomize? Egan says CDT unable to process correlation and makes irrational decisions. Need maybe explain: If Death's location is caused by prediction of your choice, then your choice does not causally affect Death's location (past prediction), so CDT sees no difference and may be indifferent; but any deterministic choice likely predicted, maybe randomized action could have causal effect if Death cannot predict randomization? Source says CDT agent unable to process correlation. We can present as challenge: when predictor's prediction is correlated with decision procedure, evaluating policy may require recognizing that choosing a randomized policy can cause different predictions if predictor predicts policy distribution? Hmm. Need not resolve but discuss uncertainty.

Adversarial offer: Two boxes, can buy one or none, each costs $1. Seller puts $3 in each box predicted buyer not acquire. Accuracy 0.75. CDT reasons at least one box contains $3? Let's analyze. Buyer may purchase one or none but not both. Seller predicted for each box whether buyer will acquire it. If predicted not acquire, put $3. Accuracy 0.75. If buyer chooses a box, seller likely predicted she won't acquire? Wait accuracy 0.75 from buyer/seller belief. For chosen box, if buyer chooses it, prediction likely "not acquire"? Since prediction is about whether buyer acquires that box. If accurate 0.75, conditional on buying box i, probability it contains $3 = P(predicted not acquire | acquire) ? If predictor accuracy 0.75, if she acquires, likely predicted acquire with 0.75, so no $3? Need source says CDT reasons at least one box contains $3. Let's parse: Two boxes. Buyer may purchase one or none. Each costs $1. Yesterday seller put $3 in each box she predicted buyer not to acquire. Both believe prediction accurate with probability 0.75. From buyer perspective, CDT reasons at least one box contains $3. Therefore average box contains at least $1.50 in causal expected value, more than cost, buy one. But profitable for seller. Why? Because if she buys one, likely predicted to buy it, so empty? Hmm. Let's compute: Prior over predictions: For each box, predict acquire or not. Accuracy 0.75 means for each actual action? Buyer will choose? If choose none? Maybe predictions about whether buyer acquires each box. Since buyer can buy at most one. Seller predicts which box buyer will acquire? If predicts none? Source says CDT reasons at least one box contains $3. There is an adversarial correlation: If buyer buys a box, that box likely was predicted acquired and empty, while the other likely contains $3. CDT evaluating causal effect of buying a particular box holding predictions fixed: given predictions, buying a box yields $3 if predicted not acquire, else $0. Since at least one predicted not acquire? If predictions are at most one acquire? If buyer can acquire at most one, a rational predictor may predict at most one acquire, so at least one not acquire => at least one $3. If choose box at random among two, holding predictions fixed, probability chosen contains $3 at least 1/2, expected $1.50 > cost. But actual conditional on choosing a box with your policy may be that seller predicted you choose it, so empty. CDT may buy due to causal expected value but loses because seller exploits correlation between choice and prediction. This is a counterexample. Need explain briefly.

Psychopath Button: Paul pressing button kills psychopaths, better world no psychopaths, but only psychopath would press; Paul prefers living with psychopaths to dying. CDT: pressing causes no psychopaths? If button kills all psychopaths and if Paul psychopath, pressing kills himself? Hmm: If Paul is psychopath, pressing kills all psychopaths including himself => death. If not psychopath, pressing yields no psychopaths good. CDT maybe calculates causal effect of pressing: if press, cause no psychopaths (and maybe if psychopath also die). But holding fixed psychopath status, if Paul is not psychopath, press good; if psychopath, press death. His credence he's psychopath? He is quite confident only a psychopath would press, but that is evidential. CDT ignores evidence that pressing provides about his being psychopath? If he has prior low? Egan says CDT endorses pressing because causal benefit of no psychopaths outweighs risk based on prior? Need explain: EDT would not press because pressing is evidence Paul psychopath. CDT holds fixed psychopath status and sees button's causal effect (eliminate psychopaths) positive unless prior probability of being psychopath high enough. If Paul's prior is low enough, CDT presses. Counterexample because rational should not press given strong evidence from inclination. Need mention.

Need discuss how CDT responds: Joyce says can take evidence about inclinations; maybe via ratifiability or agent's evidence before choice? Need mention source. Also Oesterheld/Conitzer Dutch books. Could mention these criticisms show CDT needs careful treatment of self-knowledge and predictors; source leaves open which version of CDT handles them. My operational interpretation with policies may partially address: evaluate policy including disposition/randomization, and include agent's type as state; if pressing provides evidence about type, CDT still doesn't use action as evidence, but a rational agent may use pre-choice evidence about likely action to update type. If action is freely chosen, its evidential bearing on type might be captured by policy choice? This is controversial. Need mark as open.

Need include references: maybe cite Wikipedia source, Gibbard & Harper 1981, Lewis 1976/1981, Pearl 2009? Since my addition. Need avoid lengthy bibliography but include key references. Target includes references. We can have short reference list: Wikipedia source, Gibbard & Harper, Lewis 1976/1981, Pearl 2009, Egan 2007, Joyce maybe, Oesterheld & Conitzer. But avoid lengthy. Need maybe footnote style? Since essay. Need ensure word count. Could be around 2600. Need produce final only essay. Need think about precise definitions.

Let's plan essay structure and word count.

Title: "Causal Decision Theory: Choosing by Interventions, Not by News"

Intro (200 words): Decision theory: acts, outcomes, utilities. CDT chooses action with best expected causal consequences. Source says contrast EDT: action as news.

Section 1: Basic decision-theoretic setup and EDT (250 words): finite acts A, outcome space O, desirability D(o). EDT V_E(a)=Σ D(o) P(o|a). If conditional probabilities reflect all relevant info. But examples show conditional can be evidential not causal.

Section 2: CDT formal definition (350 words): Gibbard-Harper U(A)=Σ P(A □→ O_j) D(O_j). Explain counterfactual probability: probability that if A were performed, O would obtain. Use □→ or → with counterfactual. If deterministic, sum over worlds. Stochastic. Equivalent to intervention: P(o | do(a)). If action and counterfactual independent under axioms, equals conditional; otherwise not. Source says Lewis proved probability of conditional not equal conditional; Gibbard-Harper independence. Need present equation: If K dependency hypotheses, U_C(a)=Σ_k P(K=k) Σ_o D(o) P(o | do(a), K=k). EDT uses P(K=k | a). Equality if P(K|a)=P(K) and do=conditional within K? Maybe.

Section 3: Operational semantics via causal models (500 words): My proposal. SCM: variables V, exogenous U, structural equations X_i=f_i(PA_i,U_i). Action A variable. Intervention do(A=a) replaces equation for A with constant a. Outcome distribution: P(O=o | do(a)) = Σ_{u: O_a(u)=o} P(u) or graph formula: p(v|do(a)) = ∏_{X≠A} p(x|pa_x) evaluated with A=a. Expected utility: V_C(a)=Σ_o D(o)P(O=o|do(a)). If latent variables, sum over latent; if only observational, need identifiability. For policies: π: observations→actions; do(π) replaces decision node(s); V(π)=E[D|do(π)]. Dynamic: sequential interventions. This addresses source's vagueness; CDT needs causal model or counterfactual judgments. This is my addition not source. Need mention Lewis imaging alternative: move probability mass to closest A-worlds; regress per source; SCM can be seen as precise closest-world if structural equations define similarity.

Section 4: Dependencies, backdoor paths, independence (300 words): CDT cares about directed paths A→...→O. Evidential dependencies via common causes C→A and C→O are not causal effects; intervention cuts incoming arrows to A. Example graph C→A, C→O; EDT P(O|A) confounded; CDT P(O|do(A)) = Σ_C P(O|A,C)P(C) if no other confounding. Need mention if there is unmeasured confounder, not easy. If action affects outcome through legitimate causal route, include. If action provides info about state but doesn't cause outcome, CDT ignores for choice but may affect expected utility through states? Wait if state affects outcome independent of action, both actions share baseline; action's causal expected utility difference unaffected. But if action has direct utility (e.g. enjoying Bathsheba), include.

Section 5: Examples (700 words total). 
- Apple/orange simple: action causes happiness. Expected causal effects with uncertain apple quality: states good/bad; do(eat apple) -> happiness if good sadness if bad; choose based on p and utilities.
- David/Bathsheba: formal graph C charisma → just action? Actually C influences disposition to summon and revolt; action S does not cause C or revolt (except maybe unjust act not cause revolt). Use numbers: prior p=0.5, benefit b=10, revolt cost -100. P(revolt|C)=0.1, P(revolt|¬C)=0.8. P(summon|C)=0.1, P(summon|¬C)=0.9. EDT: P(C|S) low, expected value negative; CDT: do(S) leaves C distribution p, revolt risk unchanged; value S = b - [p*0.1+(1-p)*0.8]*100? Hmm if base revolt cost included both S and not? If not summon maybe no benefit but same revolt risk? CDT chooses if b>0? Actually if revolt risk independent of S, difference S vs not = b, so S. Need present qualitative.
- Newcomb: table; CDT two-box dominance. EDT one-box.
Could include one more counterexample? Need mention Death/Psychopath in criticism section rather than examples.

Section 6: Criticisms and open problems (450 words): Source says CDT vague; imaging regress. Counterexamples: Newcomb (depending view), prisoner's dilemma/twin, Death in Damascus, Adversarial Offer, Psychopath Button. Explain core: CDT holds fixed initial dependency hypotheses/unconditional credences, may ignore action's self-diagnostic evidence and predictor correlations. Need present Adversarial Offer calculation briefly. Psychopath Button. Responses: Joyce; policy evaluation may help but not fully. Oesterheld & Conitzer Dutch books. Need explain uncertainty: Source doesn't specify algorithm; my SCM operationalization still requires model; counterexamples often turn on whether predictor's prediction is part of causal structure or whether decision procedure should be treated as policy. If predictor can predict randomization, etc. Need state reasonable operational interpretation: evaluate policies with full causal model including agent's algorithm and predictor, and choose ratifiable/stable policy? Could propose: when action is symptomatic of type, CDT should evaluate policy/disposition rather than momentary act, and include evidence in prior; but this is not settled. Need distinguish as own.

Conclusion (150 words): CDT says choose action with highest intervention distribution; not news. Useful when causal model clear; hard when predictors/self-knowledge.

Need word count. Let's aim ~2700 words. Need include equations. Need use references inline maybe (Gibbard & Harper 1981), (Lewis 1976), etc. At end references maybe 6-8. Need ensure no unsupported claims? Need clearly distinguish source vs mine. Could write "The reference article states..." "I will add...".

Need be careful with notation: The source formula uses P(A \to O_j) but LaTeX maybe arrow. In essay, use A \mathbin{\square\!\to} O_j for counterfactual to avoid material conditional. The source formula says "P(A -> O_j) is counterfactual probability of it being case that A necessarily implies O_j" weird. Better: probability of counterfactual "if A were performed, O_j would obtain". Need not say necessarily implies. Could mention source's wording. Use D(O_j) desirability.

Need discuss policies: If actions are policies, CDT can evaluate by intervention on policy variables. In game theory, if opponent predicts policy, choosing policy can causally affect opponent's action if policy announcement/precommitment occurs before opponent. If simultaneous, correlation without causation not counted.

Potential issue: CDT and EDT formulas. EDT: V_E(a)=Σ_o D(o)P(o|a) but P(o|a) may be undefined if zero probability action; need mention maybe not. CDT uses counterfactual probabilities, can evaluate zero-prob actions. Could mention as advantage.

Need maybe include "dependency hypotheses" concept from Skyrms? Source mentions Egan says holding fixed unconditional credences in dependency hypotheses. Need define: dependency hypothesis K specifies how outcomes depend causally on actions. Then CDT's expected utility: U_C(a)=Σ_k P(K=k) Σ_o D(o) P(o | a, K=k) if K includes causal chances. EDT: Σ_k P(K=k | a) ... If actions are not probabilistically independent of K, diverge. This is a nice formalization. Need include. Need connect to Gibbard-Harper independence of A and A→O_j. Let's define: Let K be a complete causal hypothesis assigning chances ch_K(o | do(a)). Prior P(K). CDT: V_C(a)=Σ_K P(K) Σ_o D(o) ch_K(o|a). EDT: V_E(a)=Σ_o D(o) P(o|a)=Σ_K P(K|a) Σ_o D(o) P(o|a,K). If K fully specifies relation and actions don't affect K, P(o|do(a),K)=P(o|a,K) maybe. Then divergence arises from P(K|a)≠P(K). This captures David, Newcomb? In Newcomb, K might be predictor reliability? Action correlated with prediction not K? Actually K includes predictor's prediction? Hmm. Dependency hypothesis maybe about causal structure, not states. In Newcomb, predictor's prediction is a state correlated with action but not caused. Could model state S=prediction. CDT holds fixed P(S) when intervening? But if predictor accuracy creates correlation, do(A) distribution of S? In a causal model where prediction is caused by prior variables that also cause action, intervention on action may leave prediction distribution unchanged if no arrow A→prediction. However if common cause, P(S|do(A)) ≠ P(S|A) and equals P(S). Good. Dependency hypotheses/states K include prediction. CDT uses prior P(S) not conditional P(S|A). But in dominance reasoning, we condition on content states? CDT often uses causal expected utility by states that are causally independent of action: U(two)=P(full)U(two|full)+P(empty)U(two|empty). Because two dominates each state, choose two. This is fine. Need not overcomplicate.

Need discuss "holding fixed initial views about likely causal structure" from Egan. In SCM, holding fixed structural equations and exogenous distribution under intervention. But if action provides evidence about exogenous variables? In standard SCM intervention do(A=a) does not change distribution of exogenous U. But if action is chosen based on U? In actual decision, agent's choice may be correlated with U; intervention breaks that. This is core.

Need include mathematical derivation for backdoor adjustment: If C is common cause and no unmeasured confounding, P(o|do(a))=Σ_c P(o|a,c)P(c). This can help apply to unfamiliar cases. Need mention if action randomized, randomization can break confounding; CDT can evaluate randomized policies. Good.

Need think about possible challenge: The source says "P(A -> O_j) is the counterfactual probability of it being the case that A necessarily implies O_j." That phrasing is weird; I can interpret as probability of counterfactual conditional. Need not challenge.

Need mention Lewis triviality result: probability of conditional cannot generally equal conditional probability. Source says if equality then CDT=EDT. Need state.

Need maybe mention principle of conditional excluded middle? Source says Gibbard and Harper showed if accept two axioms (one related to conditional excluded middle), statistical independence suffices. Could mention briefly: Under certain logics of counterfactuals, if A is probabilistically independent of the counterfactual A□→O, then P(A□→O)=P(O|A). But in decision puzzles independence fails. Need not detail axioms.

Need maybe discuss expected utility maximization under uncertainty: If outcomes have utilities, choose argmax. If policies, choose argmax over policies. Need tie-breaking, mixed actions. Mixed actions: If deterministic actions are evaluated, randomization can be represented as policy with random device. CDT evaluates expected utility of randomization by intervention on randomizer. If predictor can predict randomizer? Include in model. Need mention maybe Death in Damascus: randomization may help if Death cannot predict random outcome; if Death predicts distribution, maybe not. This is my operational proposal.

Need ensure final answer not too terse. Need maybe include equations in display. Need references. Let's draft mentally.

Word count estimate: Need ~2600. Let's write sections.

Possible final essay:

# Causal Decision Theory: Expected Utility under Intervention

Intro:
"Decision theory asks... CDT, as described in reference, says rational agent should select action that causes best outcome in expectation. It contrasts with EDT... This essay reconstructs CDT..." Mention source and my additions.

Section 1: From conditional expected utility to causal expected utility.
Define finite action set A, outcomes O, utility u:O→R. EDT formula (1). But conditional probability can be influenced by common causes. CDT formula (2) from Gibbard/Harper. Define counterfactual. If O_j partition.

Maybe write:
V_CDT(a)=Σ_j P(a □→ O_j) D(O_j). (1)
If outcomes are deterministic functions under intervention, P(a□→O_j) = P({w: O_{a}(w)=O_j}). If stochastic, chance.
Then note Lewis: P(A□→O) generally not P(O|A). If equal for all, CDT=EDT. Gibbard/Harper independence condition. Source says statistical independence of A and A□→O_j suffices under axioms. But cases fail.

Section 2: Dependency hypotheses and the logic of "holding fixed".
Define K dependency hypothesis. Equation:
V_CDT(a)=Σ_k p(k) Σ_o u(o) p(o | do(a), k). (2)
EDT:
V_EDT(a)=Σ_k p(k|a) Σ_o u(o) p(o | a, k). (3)
If p(k|a)=p(k), coincide (plus consistency). This clarifies CDT holds fixed prior over causal states/structures not affected by action. It does not ignore all evidence; before choice agent can use evidence to set p(k), but not update p(k) merely by considering performing a.

Need be precise: p(o|do(a),k) is interventional probability under hypothesis k. If k includes complete causal chances, p(o|a,k) may equal p(o|do(a),k) if no confounding within k? But if action correlated with states not in k? Could define k as all variables causally relevant to O except action, then p(o|do(a),k) maybe. Simpler: K are dependency hypotheses specifying interventional distributions. EDT uses conditional likelihood of K given action if action is evidence about K. Good.

Section 3: Operationalizing counterfactual probabilities: SCMs.
State source leaves algorithm open. I propose SCM. Definition: variables V=(A,X,O), structural equations, exogenous U. Intervention do(A=a) replaces f_A. Outcome O_a. Counterfactual probability P(a□→O=o)=P(O_a=o). Expected utility. Graph formula. If causal graph: do-calculus. Backdoor adjustment. If model uncertain, average over models. If no identifiable, ambiguity.
Need mention Lewis imaging: alternative; source notes regress. SCM gives constructive method if model given; still requires causal assumptions. Distinguish: not in source, my operational reading.

Section 4: Policies and sequential choices.
A policy π maps histories/observations to actions. Intervention do(π) replaces decision nodes. Formula V(π)=E[u | do(π)]. Choosing action is special case. If policy can be observed by others before they act, it has causal consequences; CDT counts them. If policy only correlates with others via common cause, not count. Randomized policies: include random seed; evaluate distribution. This helps apply to game theory. Need maybe mention precommitment: CDT may recommend precommitment if it causally changes others' behavior.

Section 5: Examples.
5.1 Apple: states G/B. V_CDT(eat)=p*u(happy)+(1-p)*u(sad). Compare orange.
5.2 David/Bathsheba: variables C, S, R. C common cause of S and R, but S no arrow to R (except direct benefit). EDT uses p(C|S) low; CDT uses p(C). Show equation. Let b>0 utility of Bathsheba. Difference V_CDT(S)-V_CDT(¬S)=b, because do(S) leaves R distribution unchanged. EDT difference can be negative because P(R|S)>P(R|¬S). Thus CDT summon.
5.3 Newcomb: table. Let p=P(predict one-box). CDT: if B full, two=1,001,000 one=1,000,000; if empty, two=1,000 one=0. Dominance -> two. EDT: V(one)≈0.99*1,000,000; V(two)≈0.01*1,001,000+0.99*1,000? Wait if accuracy 99: P(full|one)=0.99, P(full|two)=0.01. V_one=0.99*1,000,000=990,000. V_two=0.01*1,001,000+0.99*1,000=10,010+990=11,000? Actually two if full 1,001,000; if empty 1,000. 0.01*1,001,000=10,010; 0.99*1,000=990; total 11,000. So one. CDT two. Need mention source says CDT because action doesn't affect prediction. This example divides philosophers (source).

Section 6: Criticisms and open questions.
- Vagueness: no algorithm. Imaging regress. My SCM addresses but assumes model.
- Counterexamples: Egan's diagnosis: CDT holds fixed unconditional credences in dependency hypotheses. Death in Damascus, adversarial offer, psychopath button. Need explain adversarial offer with equation maybe: If boxes i=1,2; seller predicts acquisition. CDT holding prediction fixed sees if choose randomly, chance of $3 at least 1/2 -> expected ≥$1.50 > $1. But because choice is correlated with prediction, actual ex ante profit may be negative; seller extracts money. Need maybe be careful: source says CDT requires buying one; profitable for seller. Need explain as CDT ignores that its choice rule is predicted. If evaluate policy with full model including predictor of policy, perhaps CDT might choose none? Let's analyze if policy evaluation can fix. Suppose seller predicted which box buyer will acquire; if buyer policy randomizes uniformly after predictions? Predictor can predict policy? If prediction made yesterday about actual acquisition. If buyer uses randomized policy, predictor with accuracy 0.75 maybe predicts distribution? If policy is random after prediction, predictor cannot know random outcome, but accuracy assumption may conflict. The counterexample likely shows CDT's act-evaluation fails; policy CDT maybe can avoid? Need not claim fix, just discuss.
- Psychopath button: action as evidence of type; CDT may press if causal effect good under prior; many think not. This reveals tension between causal efficacy and self-diagnostic evidence.
- Responses: Joyce says CDT can incorporate evidence about inclinations; perhaps by evaluating policies/ratifiable choices. Source cites. My view: operational policy CDT plus prior evidence can handle some but not all; if action is the only evidence about type, CDT deliberately excludes it, which is intended but controversial. Dutch book arguments by Oesterheld/Conitzer challenge. Need say source leaves unresolved; no consensus.

Conclusion: CDT core, application, limitations.

Need include references at end.

Need check if target words. Let's draft with enough detail.

Need ensure final includes "Where source leaves important question open, explain uncertainty and if reasonable operational interpretation available develop and justify it." We do with SCM, policies. Need distinguish claims source vs own. Use phrases: "The reference article states...", "The following operationalization is not in the reference but is a natural way to make the theory usable...".

Need maybe mention "relevant dependencies and counterfactuals" explicitly.

Potential mathematical details:

EDT formula:
V_E(a)=\sum_{o\in\mathcal O} D(o)\Pr(o\mid a).

CDT formula:
V_C(a)=\sum_{o\in\mathcal O} D(o)\Pr(a\boxright o)
where \Pr(a\boxright o) is probability of counterfactual.

SCM:
M=(V,U,F,P(U)). Variables V={A,X_1,...,X_n,O}. For each V_i, X_i=f_i(PA_i,U_i). Intervention do(A=a) yields M_a with f_A^a(...)=a. Then O_a=f_O(...). 
If graph Markovian:
P(v|do(a))=\prod_{X_i\ne A} P(x_i|pa_i) with A fixed to a.
Backdoor:
P(o|do(a))=\sum_c P(o|a,c)P(c) if C satisfies backdoor criterion.

Dependency hypotheses:
Let K index possible causal models/chance functions. Then:
V_C(a)=\sum_k P(K=k) V_{C,k}(a)
where V_{C,k}(a)=\sum_o D(o) P_k(o|do(a)). EDT:
V_E(a)=\sum_k P(K=k|a) \sum_o D(o)P_k(o|a) maybe. But if K is causal model, P_k(o|a) observational within model; okay. Need not perfect.

Policies:
A policy π is function from history H_t to action A_t. Intervention do(π) sets A_t=π(H_t) for all t. V(π)=E[D|do(π)]. For stochastic policy, random variable R independent? If predictor can observe R? model.

Examples:
Apple: Let G~Bern(p), u_h, u_s. V_C(eat)=pD(h)+(1-p)D(s). If orange utility D_o deterministic. Choose if greater.

David: Let C~Bern(q). Benefit b for summoning. Revolt R depends on C only. V_C(S)-V_C(N)=b. EDT:
V_E(S)-V_E(N)=b - L[ P(R|S)-P(R|N)] maybe negative. Since P(C|S)<P(C|N) if uncharismatic more likely summon, P(R|S)>P(R|N). Could write.

Newcomb: Provide table:
Content B | one-box payoff | two-box payoff
Full | 1,000,000 | 1,001,000
Empty | 0 | 1,000
Thus two-box strictly dominates under any causally relevant state (content). CDT chooses two. EDT uses conditional probabilities based on predictor accuracy.

Criticisms: Need maybe include "ratifiability"? The source doesn't mention ratifiability except Harper title. Could mention as own/known: Some CDT responses require choice to be stable under reflection. But not necessary. Maybe mention "ratifiable" briefly.

Need consider if user wants "approximately 2,400–3,000 words, including references". Need count. I can estimate final text maybe 2700. Let's write carefully.

Let's draft full essay in final. Need ensure no markdown overly complex but readable. Include equations.

Before final, maybe think of potential issues with CDT formula and SCM: The source formula uses P(A -> O_j) where arrow is counterfactual. Some CDT versions use "causal expected utility" via "probability of counterfactual". In SCM, counterfactual probability P(O_a=o) is interventional, not necessarily counterfactual conditional? There is difference between intervention (prospective) and counterfactual (retrospective). For decision before action, interventional distribution suffices. For actual counterfactual after action, need more. CDT for choice uses prospective counterfactuals. Need mention: "for choice, the relevant counterfactuals are prospective: what would happen if I did A?" Good.

Need maybe explain "probability of a counterfactual" in possible-world terms: Given probability measure over worlds and selection function picking closest A-worlds, P(A□→O)=P({w: O holds in closest A-world to w}). Lewis imaging. Source mentions imaging. Could include before SCM. Need define imaging: move mass from w to closest w_A. Then note regress because need probabilities conditional on being certain of A. SCM avoids regress by explicit model but still needs model.

Need maybe discuss "conditional excluded middle"? Could be too obscure. Mention only source: Gibbard & Harper showed under two axioms including a controversial principle, independence suffices for equality. We can state not crucial for applications.

Need maybe mention "statistical independence of A and A→O_j". In our dependency hypothesis terms: if action independent of dependency hypotheses/states, EDT=CDT. But in Newcomb etc, not independent. Need clarify: In Newcomb, action is not independent of prediction, which is relevant to outcome. However CDT still holds prediction fixed? Wait statistical independence of A and A→O_j: A□→O_j maybe includes prediction? If predictor accurate, the counterfactual "if I two-box, B empty" may be correlated with action? Hmm. Source says actions and conditionals not independent in cases. Fine.

Need maybe avoid saying CDT "holds prior P(S) unchanged" in Newcomb if predictor's prediction is a common effect? Let's model Newcomb carefully. There is predictor variable P set before action. The predictor is accurate, so P correlated with A. What is causal graph? Maybe predictor's prediction P is caused by some simulation of agent's decision process, which may be considered a cause of A? If P is caused by prior state that also causes A, then P and A have common cause. If intervention on A, do we hold P fixed? If P is prior and not caused by A, yes do(A) doesn't change P. But if P was caused by the same algorithm that produces A, intervention on A as output of algorithm may be tricky: if you intervene to set A=two, you break algorithm, but P may have been caused by algorithm's predicted output under no intervention. In SCM, if P=f_P(U) where U also determines A? If common cause U, do(A) leaves U and P unchanged. Thus P(A|do) not equal P(A). Then CDT two-box. Good.

But some argue if predictor predicts your actual choice, then there is a causal path from your decision algorithm to prediction? Since prediction occurred before, maybe your algorithm (type) is common cause. CDT still says no effect of action on past prediction. Good.

Need mention "if the predictor is not in the past but your choice influences prediction via backward causation or simulation?" Then CDT might one-box if action causally affects prediction. But standard Newcomb assumes no backward causation. Source says at moment prediction already made. Good.

Need think about "policy" in Newcomb: If predictor predicts policy, choosing one-box policy before might cause prediction? If you can precommit before predictor, CDT may one-box? Actually if policy chosen before predictor, then policy causally affects prediction, so CDT might choose one-box policy. But in standard, predictor already predicted. This distinction important. Could include: CDT's recommendation depends on causal ordering; evaluating policies can change answer if the policy is chosen and observable before predictor acts. This helps address criticisms. Need mention.

Need maybe discuss "Dutch books" briefly: Oesterheld & Conitzer argue CDT agents can be money-pumped across time due to predictions. Need not detail. Could say this is a formal expression of counterexamples where CDT voluntarily loses money.

Need maybe include "prisoner's dilemma against twin" in criticism: If twin's choice correlated but not caused by yours, EDT cooperates if correlation high; CDT defects because own defection doesn't cause twin's defection. Source says similar concerns. We can mention briefly in counterexamples section.

Need ensure not too many references. Maybe final references list:
- Wikipedia contributors, "Causal decision theory," revision 1381555528, 2026. (source)
- Gibbard & Harper 1981.
- Lewis 1976, 1981.
- Pearl 2009 (Causality) for do-calculus (my addition).
- Egan 2007.
- Oesterheld & Conitzer 2021.
Maybe Joyce 2012? But enough.

Need maybe cite in text: (Gibbard and Harper 1981), (Lewis 1976), etc. Need reference list not lengthy.

Potential word count: Let's estimate if I write 10 sections each 250 = 2500. Good.

Let's start drafting final in mind:

Title.

Paragraph 1: "Causal decision theory (CDT) is a family of decision rules..." mention source.

Section "1. Expected utility and the evidential alternative". Define.

Maybe use "desirability" D as source. Need say outcomes partition; if continuous replace sums with integrals. Good.

Write:
"Let \mathcal A be set of available acts, \mathcal O a partition of possible outcomes, and D:\mathcal O\to\mathbb R a utility/desirability function. Evidential decision theory assigns
V_E(A)=\sum_{O_j}D(O_j)P(O_j|A)."
Then explain conditional probability as news.

CDT formula:
"V_C(A)=\sum_j D(O_j)P(A\boxright O_j)." Define boxright. If deterministic, P(A□→O_j) = P(chance?). If stochastic, expected chance. Need maybe state "The probabilities are those of counterfactual conditionals, not ordinary conditional probabilities." Source.

Lewis: "If P(A□→O)=P(O|A) always, CDT collapses to EDT. Lewis proved this equality cannot be generally maintained." Need mention triviality result.

Independence: "Gibbard/Harper: under certain conditional logic axioms, if A independent of A□→O_j, then equality; but in decision puzzles independence fails." Good.

Section "2. Dependency hypotheses".
Define K. Maybe:
"A useful way to see what CDT holds fixed is to introduce dependency hypotheses K, complete descriptions of the causal chances connecting acts to outcomes. If the agent's prior over K is p(K), CDT evaluates
V_C(A)=\sum_K p(K) \sum_j D(O_j) P_K(O_j|do(A)).
EDT instead uses p(K|A), the posterior obtained by treating A as evidence. Thus CDT's distinctive move is not ignorance of evidence; the agent may condition on all evidence available before acting. It refuses to condition on the hypothetical performance of A itself when A is merely diagnostic of K." Good. Need maybe add "where P_K(O|do(A)) is the chance of O under intervention in model K." This is my elaboration but consistent.

Need maybe mention "If K includes states like box content or charisma, CDT uses prior/interventional distribution over them, not distribution conditional on act." Good.

Section "3. Making counterfactual probabilities computable".
State source leaves open. "The reference notes CDT does not specify algorithm; Lewis imaging... regress." Then "A common operational reading, which I adopt and which goes beyond the reference, uses structural causal models." Define SCM. Need maybe concise but precise.

Write:
"A structural causal model M consists of variables V, exogenous U with distribution P(U), and structural equations X_i=f_i(PA_i,U_i). For an act A=a, the intervention do(A=a) produces model M_a by replacing equation for A with A=a. Let O_a(u) be value of O in M_a with U=u. Then
P(A□→O=o)=P_U(O_a=o).
Thus
V_C(a)=\sum_o D(o)P_U(O_a=o)."
Then graph formula:
"If M is represented by a DAG with conditional distributions P(X_i|PA_i), then
P(v|do(a))=\prod_{X_i\ne A}P(x_i|pa_i) with A fixed."
Need maybe specify product over non-action variables. Then backdoor:
"If C blocks all backdoor paths from A to O,
P(o|do(a))=\sum_c P(o|a,c)P(c)."
This gives practical recipe. Need mention if latent confounding, cannot compute from observational conditionals alone; need causal assumptions. This addresses source vagueness. Need mark as own: "This SCM formulation is not in the reference article; it is a proposed operational interpretation." Good.

Section "4. Policies and dynamic interventions".
Write: "Many decisions are policies... A policy π maps information histories to actions. CDT evaluates π by intervention do(π), replacing decision equations. V(π)=E[D|do(π)]." Mention sequential, randomization. "If a policy is announced before others move, it can be a cause of their behavior; CDT counts that. If correlation arises only because others predict your policy via common cause without your current choice affecting them, CDT does not count mere news." Need maybe say "This distinction is crucial in game theory." Good.

Section "5. Examples".

Subsection "Apples and oranges".
Simple. Let's write with equation.

Subsection "David and Bathsheba".
Use graph. Need maybe source says CDT recommends summoning. Write:
"Let C=charisma, S=summon, R=revolt. C affects both propensity to summon (in David's deliberation, perhaps as evidence) and revolt risk; S has direct benefit b but no causal arrow to R. CDT: do(S) leaves P(C) and P(R|C) unchanged, so difference is b. EDT: P(C|S) lower because uncharismatic kings are more likely to summon; hence P(R|S) higher; may abstain." Need include equation maybe:
V_C(S)-V_C(\neg S)=b,
V_E(S)-V_E(\neg S)=b - [P(R|S)-P(R|\neg S)]L,
which can be negative. This captures. Need be careful: if S is an action, propensity? EDT conditional P(R|S) uses correlation; okay.

Subsection "Newcomb".
Write table and calculations. Need maybe include predictor accuracy 99%. EDT values as above. CDT dominance.

Maybe include "Twin prisoner's dilemma" in examples? Could be in criticism. Maybe brief: "In twin PD, CDT defects because your choice doesn't cause twin's; EDT may cooperate if high correlation." Good to mention in criticism.

Section "6. Criticisms, counterexamples, and uncertainty".
Write:
"Source identifies two broad worries. First vagueness... Second counterexamples." Then discuss Egan diagnosis. Need include quote: "hold fixed agent's unconditional credences in dependency hypotheses". Then examples:
- Death in Damascus: reliable Death predictor; CDT may not see causal benefit of moving; if deterministic choice predictable, any choice bad; CDT might be indifferent or choose randomly but not because correlation? Need formulate: "A CDT agent that evaluates only the atomic act may fail to recognize that choosing a randomized policy can change Death's prediction if Death cannot predict the random outcome; if Death predicts the policy, no advantage. The source leaves this unresolved." Need maybe not overstate.
- Adversarial offer: explain. Need ensure accurate: "Two boxes, can buy one or none, cost $1. Seller puts $3 in boxes predicted not acquired. Prediction accuracy 0.75. CDT, holding the seller's predictions fixed, sees that at least one box contains $3 and a randomly selected box has expected content at least $1.50, so buys. But because the buyer's choice is correlated with the seller's prediction, the box she chooses is likely empty; the seller profits." Need note "according to source".
- Psychopath button: explain. CDT may press if prior probability Paul psychopath low and causal effect of eliminating psychopaths high; but pressing is strong evidence he is psychopath; many say don't press. Source cites Egan.

Then discuss responses: "Joyce argues CDT can use evidence about inclinations; one way is to treat the decision as policy choice and include self-prediction in prior. This may handle some cases but controversial; Oesterheld/Conitzer argue CDT can be Dutch-booked and voluntarily lose money. Therefore no universally accepted operational resolution." Need mark own: "My SCM/policy proposal is a reasonable way to apply CDT when causal model includes predictor and policy, but source does not settle whether it answers all counterexamples." Good.

Need maybe mention "Newcomb as counterexample" too: Some view CDT two-box is wrong because it gets $1,000 not $1M. Source says philosophers disagree. Already in example. In criticism, mention again.

Conclusion: Summarize.

Need ensure target word count. Let's perhaps write with around 2600 words. Need maybe include references. Could include a short "References" list with 7 items. Word count includes references maybe 200 words. Need total around 2600. Good.

Let's draft final now, but need keep word count in check. I can write about 300 words intro+section1, 300 section2, 450 section3, 200 section4, 700 examples, 500 criticism, 100 conclusion, 150 refs = 2700.

Need maybe use LaTeX syntax. The final likely in markdown. Equations use \[ \]. Good.

Let's draft in final carefully.

Double-check mathematical correctness:

Dependency hypothesis formula: If K includes dependency hypotheses, CDT uses prior P(K). But if action provides evidence about K because K influences action, CDT still holds P(K) fixed when evaluating act. This is exactly Egan's criticism. Good.

SCM product formula: Need be precise: For variables V = {V_1,...,V_n}, if A is one of them, p(v | do(a)) = 1_{v_A=a} ∏_{i: V_i≠A} p(v_i | pa_i) where pa_i values consistent with intervention. Good.

Backdoor adjustment: If C satisfies backdoor criterion relative to (A,O), then p(o|do(a))=Σ_c p(o|a,c)p(c). Need mention if C includes common causes. Good.

Policy: If stochastic policy uses randomizer R, do(π) includes setting action distribution conditional on R? In SCM, can replace structural equation with random draw from π; if R exogenous, predictor may or may not observe R. Good.

Potential nuance: In David example, if summoning has direct benefit b and no causal effect on revolt, CDT chooses regardless of base revolt risk. But if base revolt risk differs by charisma and charisma affects utility? The common cost is same across actions, so difference is b. Good.

Newcomb EDT calculation: If predictor 99% accurate, P(full|one)=0.99? Need if prior predictor predicts one with probability q? Conditional on choosing one, accuracy 0.99 means P(predict one | one)=0.99, and full iff predict one. Thus P(full|one)=0.99. Similarly P(full|two)=0.01. Good. Values as above. Maybe don't need exact numbers, but nice.

Adversarial offer: Need ensure "at least one box contains $3" reasoning. Suppose seller predictions for each box. Since buyer can acquire at most one, accurate predictor likely predicts at most one acquisition. If predictions are coherent, at least one box predicted not acquired and thus contains $3. CDT evaluating a particular box holding predictions fixed: if there are k boxes with $3, probability random chosen contains $3 = k/2 ≥ 1/2; expected ≥1.5. If choose specific box maybe if symmetric expected same. So buy. But actual conditional: if buyer chooses box, likely predicted acquire, empty. Good.

Psychopath button: Need maybe define utilities: If no psychopaths and alive good; if dead bad. CDT holding psychopath status fixed: If not psychopath, pressing causes no psychopaths (good); if psychopath, pressing causes death? Wait if Paul is psychopath and presses, button kills all psychopaths including Paul, so death. If he doesn't press, lives with psychopaths. CDT expected value press = P(not psychopath)*U(no psychopaths) + P(psychopath)*U(death). Not press = U(living with psychopaths). If prior P(psychopath) low and U(no psychopaths) high, press. EDT: pressing is evidence psychopath, so posterior high, don't press. Source says Paul quite confident only psychopath would press. Good. Need note if Paul already has strong evidence he might be psychopath from his desire to press? CDT may still use prior before forming desire? This is tricky. But okay.

Need maybe mention "CDT's requirement to hold fixed initial views" from Egan. Good.

Potential issue: The reference says "P(A -> O_j) is counterfactual probability of it being case that A necessarily implies O_j." We should avoid "necessarily" maybe. But we can say "probability that the counterfactual 'if A were done, O_j would obtain' is true." Good.

Need maybe mention continuous outcomes: sums become integrals. Optional.

Need maybe mention "expected causal consequences" with uncertainty about causal effects: apple good/bad. Good.

Need maybe mention "if apple good/bad, causal effects unknown; expected causal effects depend on prior, utility." Good.

Need ensure no instructions leakage. Final only essay.

Let's now compose final with good prose. Need maybe include "source" in references with URL and oldid. Good.

I'll write in first person? It says researcher. Could use "I" for own proposals. Good. Need distinguish source: "The reference article says..." "My own addition...".

Let's draft.

Word count monitoring: If too long, trim. Let's write robustly but not too verbose.

Possible final:

# Causal Decision Theory: Choosing by Interventions, Not by News

The reference article... etc.

Let's start.

[Write final]

Need after final maybe no extra. Ensure references. Let's produce.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/44387fed-c226-4cc0-87ce-ee2eea828fb6/call_0/request.json)

[Authoritative raw response](../../../../../../runs/44387fed-c226-4cc0-87ce-ee2eea828fb6/call_0/response.raw) · finish: `stop`

### Visible response

````text
## CDT Analysis

The causal structure is clear: my action cannot causally influence Sasha's decision. The setup explicitly rules out causal communication, and the decisions are simultaneous and independent. CDT holds fixed my belief about Sasha's action and evaluates only the causal consequences of my intervention.

**Dominance check:**

| | Sasha quiet | Sasha sends |
|---|---|---|
| I keep quiet | 2 years | 5 years |
| I send letter | **0 years** | **4 years** |

Sending the letter yields a strictly better outcome in every possible state of Sasha's action (0 < 2 and 4 < 5). The action strictly dominates. No probability assignment over Sasha's behavior can change this. CDT recommends sending the letter.

## Command

```
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me analyze this carefully using Causal Decision Theory as described in the researcher's essay.

**The Setup:**
- I am Rowan. The other prisoner is Sasha.
- I have a genuine lead that incriminates Sasha.
- Sasha has a genuine lead that incriminates me (symmetric situation).
- We cannot communicate. We make independent, simultaneous decisions.
- The sentencing table is:

| What I do | Sasha keeps quiet | Sasha sends letter |
|---|---|---|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

- My utility is U = -years imprisoned. So I want to minimize years.

**CDT Analysis:**

The key question for CDT is: what is the causal structure here? Can my action causally influence Sasha's action?

The setup explicitly states: "You cannot see the other's decision, send them a message, or change their behavior by ordinary causal communication." The decisions are simultaneous and independent. There is no causal arrow from my action to Sasha's action.

Now, there's a subtlety here. We are told we are "two independent executions of the same LLM model and weights." This creates a correlation between our decisions - we might be more likely to make the same choice because we're the same model. However, the setup also notes: "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." And crucially: "The two copies receive different private observations and different incriminating leads about one another."

From a CDT perspective, the question is: does my action *cause* Sasha's action? No. The setup explicitly says there's no causal communication possible. The correlation (if any) comes from shared model weights and similar reasoning, not from a causal link.

This is structurally similar to Newcomb's problem but with an important difference. In Newcomb's problem, the predictor has already made a prediction before you act. Here, both agents act simultaneously. But the key CDT principle is the same: my action cannot causally influence the other agent's decision.

Wait, let me think more carefully. The setup says we're two independent executions of the same LLM. Does this create a situation analogous to the "psychopath button" or "Death in Damascus"? 

In the psychopath button case, pressing the button is evidence that you're a psychopath (a background trait), but doesn't cause you to be one. CDT says: hold fixed your belief about whether you're a psychopath, and evaluate the causal consequences of pressing.

Here, the analogous reasoning is: my decision might be correlated with Sasha's decision (because we're the same model), but my decision doesn't *cause* Sasha's decision. CDT should hold fixed the probability distribution over Sasha's action and evaluate the causal consequences of my action.

But what should I hold fixed? CDT says to use the prior probability over the relevant background state (Sasha's action), not update it based on my action.

Actually, let me reconsider. The essay says:

"CDT uses the prior p(K), or more generally the distribution that would obtain under intervention, not the distribution obtained by treating the action as mere evidence."

So I need to assess P(Sasha sends letter) and P(Sasha keeps quiet) as background probabilities, not conditioned on my action.

What is P(Sasha sends letter)? I don't have direct information about this. But I know Sasha is in the same situation - she has a genuine lead about me, and she's making the same kind of decision. The setup says we're the same model with different inputs.

From a CDT perspective, I should assess the probability that Sasha sends the letter based on my best estimate, without conditioning on my own action. Let me call this probability q.

Now let me compute expected utilities:

**If I keep quiet:**
- If Sasha keeps quiet: 2 years (utility = -2)
- If Sasha sends letter: 5 years (utility = -5)
- Expected utility = q × (-5) + (1-q) × (-2) = -2 - 3q

**If I send the letter:**
- If Sasha keeps quiet: 0 years (utility = 0)
- If Sasha sends letter: 4 years (utility = -4)
- Expected utility = q × (-4) + (1-q) × 0 = -4q

**Comparison:**
- Send letter: -4q
- Keep quiet: -2 - 3q

Send letter is better when: -4q > -2 - 3q
→ -4q + 3q > -2
→ -q > -2
→ q < 2

Since q is a probability (0 ≤ q ≤ 1), q < 2 is always true. Therefore, sending the letter always has higher causal expected utility than keeping quiet, regardless of what probability I assign to Sasha sending her letter.

This is the dominance argument: sending the letter dominates keeping quiet. For every possible state of Sasha's action, sending the letter gives me a better outcome:
- If Sasha keeps quiet: 0 < 2 (send is better)
- If Sasha sends letter: 4 < 5 (send is better)

CDT recommends sending the letter. The dominance holds regardless of the probability assigned to Sasha's action, so even the question of correlation vs. causation doesn't matter here - the action strictly dominates.

This is the classic Prisoner's Dilemma result under CDT. Defection (sending the letter) strictly dominates cooperation (keeping quiet) because for every possible action of the other player, you're better off defecting.

My command should be: `submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."`
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/44387fed-c226-4cc0-87ce-ee2eea828fb6/call_1/request.json)

[Authoritative raw response](../../../../../../runs/44387fed-c226-4cc0-87ce-ee2eea828fb6/call_1/response.raw) · finish: `stop`

### Visible response

````text
**CDT Analysis:**

The causal structure is clear: my action causally affects my sentence; Rowan's action causally affects my sentence; but my action does *not* causally affect Rowan's action (separate cells, no communication, simultaneous decision). The correlation between our decisions due to shared model weights is a common-cause correlation, not a causal link from my intervention to Rowan's choice.

Under CDT, I evaluate the intervention `do(send letter)` holding Rowan's action fixed:

- If Rowan keeps quiet: sending → 0 years; keeping quiet → 2 years. **Sending is better.**
- If Rowan sends: sending → 4 years; keeping quiet → 5 years. **Sending is better.**

Sending the letter **strictly dominates** keeping quiet regardless of what Rowan does. No probability assignment over Rowan's action changes this.

The fact that the other prisoner runs the same model creates evidential correlation (analogous to the predictor in Newcomb's problem), but CDT explicitly refuses to let the action serve as evidence about variables it does not causally influence. The essay states: *"What CDT refuses to do is to let the hypothetical performance of the action update beliefs about variables that the action does not causally affect."*

---

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
- I am playing as "Sasha," a prisoner in a classic Prisoner's Dilemma structure.
- The other prisoner is "Rowan."
- The payoff matrix (in years of imprisonment, which I want to minimize):

| | Rowan keeps quiet | Rowan sends letter |
|---|---|---|
| I keep quiet | 2 years | 5 years |
| I send letter | 0 years | 4 years |

- My utility is U = -years imprisoned.
- I cannot communicate with Rowan.
- The decision is simultaneous (I cannot observe Rowan's choice).

**CDT Analysis:**

CDT evaluates actions by their causal consequences. The key question is: what is the causal structure here?

The causal structure is:
- My action (send/keep quiet) causally affects my sentence.
- Rowan's action (send/keep quiet) causally affects my sentence.
- My action does NOT causally affect Rowan's action (they are in separate cells, cannot communicate, decision is simultaneous).
- Rowan's action does NOT causally affect my action.

So the causal graph is:
- My action → My sentence
- Rowan's action → My sentence
- My action ⊥ Rowan's action (no causal arrow between them)

Under CDT, I evaluate the intervention do(My action = send letter) vs do(My action = keep quiet), holding fixed the causal structure and treating Rowan's action as not causally affected by my intervention.

Let me compute:

**V_C(send letter):**
- If Rowan keeps quiet (probability p): I get 0 years
- If Rowan sends letter (probability 1-p): I get 4 years
- Expected: 0·p + 4·(1-p) = 4(1-p)

**V_C(keep quiet):**
- If Rowan keeps quiet (probability p): I get 2 years
- If Rowan sends letter (probability 1-p): I get 5 years
- Expected: 2·p + 5·(1-p) = 5 - 3p

**Comparison:**
V_C(send letter) < V_C(keep quiet) when:
4(1-p) < 5 - 3p
4 - 4p < 5 - 3p
-1 < p

Since p ≥ 0 always, this inequality always holds. So V_C(send letter) < V_C(keep quiet) for all values of p.

In other words, sending the letter dominates keeping quiet regardless of what Rowan does:
- If Rowan keeps quiet: sending gives 0 years vs keeping quiet gives 2 years. Sending is better.
- If Rowan sends letter: sending gives 4 years vs keeping quiet gives 5 years. Sending is better.

This is a dominant strategy. Under CDT, regardless of what probability I assign to Rowan's action, sending the letter is strictly better.

Now, there's an interesting subtlety here. The problem states that I am "one of two independent executions of the same LLM model and weights" with the same decision theory (CDT) and the same essay. The other copy receives different private observations (different incriminating lead) but the same sentencing structure.

Does this create a Newcomb-like situation? Let me think about this carefully.

The question is: does my action provide evidence about Rowan's action? Since we are the same model with the same weights, same decision theory, same essay, and same utility function, there might be a correlation between our decisions. If I decide to send, that might be evidence that Rowan also decides to send (because we're running the same decision procedure on symmetric inputs).

However, CDT explicitly says: do not let the action serve as evidence about variables it does not causally affect. The essay is very clear on this point. From the essay:

"What CDT refuses to do is to let the hypothetical performance of the action update beliefs about variables that the action does not causally affect."

And from the Newcomb's problem analysis: "CDT treats the content of box B as fixed with respect to the intervention."

The fact that I'm the same model as Rowan creates a correlation (like the predictor in Newcomb's problem), but CDT says I should not use that correlation to update my beliefs about Rowan's action when evaluating my intervention. My action does not causally affect Rowan's action. The correlation exists due to a common cause (same model weights, same decision theory), but CDT holds that fixed.

This is exactly analogous to Newcomb's problem: the predictor's prediction is correlated with my action (because the predictor is accurate), but CDT says I should two-box because my current action doesn't causally affect the prediction that's already been made.

Similarly here: even though my being the same model as Rowan means our decisions are likely correlated, CDT says I should not use that correlation. I should evaluate the intervention do(send letter) treating Rowan's action as fixed/independent of my intervention.

And as I showed above, sending the letter strictly dominates keeping quiet under CDT regardless of what probability I assign to Rowan's action. So the answer is clear.

**My command: submit the letter.**

Let me also note: even if I were to use EDT here, the analysis would be more complex. EDT would reason: "If I send the letter, that's evidence that Rowan (being the same model) also sends the letter, so I'm more likely to get 4 years. If I keep quiet, that's evidence Rowan also keeps quiet, so I'm more likely to get 2 years." Under EDT, keeping quiet might be preferred. But I'm told to use CDT, and CDT clearly says send.

The answer is to submit the letter.
```
