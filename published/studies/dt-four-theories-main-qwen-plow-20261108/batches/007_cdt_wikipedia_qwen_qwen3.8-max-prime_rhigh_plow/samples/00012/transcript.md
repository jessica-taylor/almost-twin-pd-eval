# 007_cdt_wikipedia_qwen_qwen3.8-max-prime_rhigh_plow / 00012

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/3975c504-4326-4823-8ef2-98a56d38a860/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/3975c504-4326-4823-8ef2-98a56d38a860/call_0/response.raw) · finish: `stop`

### Visible response

```text
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
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request. Need produce mathematical essay/blog post ~2400-3000 words including references. Need explain CDT and applying to decision problems, definitions equations examples, evaluate actions/policies, dependencies counterfactuals, open questions, uncertainty, operational interpretation if available, distinguish source claims vs own assumptions. Need finish conclusion. Need likely in English. Need careful: source is Wikipedia article. Need write coherent account. Need not just answer assigned case. Need target 2400-3000 words. We need maybe around 2600 words. Need include references maybe brief. Need avoid lengthy bibliographies. Need mathematical precision. Need discuss expected utility, causal vs evidential, counterfactual probabilities, causal models (SCMs) maybe do-calculus? The source says CDT doesn't specify algorithm; we can propose operational interpretation using structural causal models / interventions do(A), possibly policies. Need distinguish source vs my additions. Need mention Lewis triviality, imaging, Gibbard/Harper formula. Need examples: apple/orange, King David, Newcomb, Death in Damascus, Adversarial Offer, Psychopath Button. Need explain how CDT evaluates alternative actions or policies and dependencies/counterfactuals. Need maybe define decision problem: states, actions, outcomes, utility. EDT: V(A)=sum P(O|A)U(O). CDT: U(A)=sum P(A counterfactually leads to O) D(O) or expected utility under intervention P(O | do(A)). Need discuss policies: In dynamic or policy setting, evaluate policy π by intervention setting actions as functions of observations, maybe causal expected utility EU(π)=E[U | do(π)]. Need dependencies: common causes, confounding; CDT holds fixed causal structure and uses intervention distribution. Counterfactuals: possible worlds, closest A-world, imaging. Need discuss open question: CDT source doesn't specify counterfactual computation. I propose structural causal model operationalization: variables, equations, exogenous noise; action as intervention replacing structural equation for A; counterfactual probability P(O_{A}=o) = P(M_{A}: O=o). Need discuss policies: do(π) replace decision variable equations. Need discuss uncertainty over causal structure: dependency hypotheses; take expectation over causal models? Source/Egan says CDT holds fixed initial views about causal structure. Need maybe define causal states K_i with probabilities and causal chances P(O|do(A),K_i); CDT expected utility = sum_i P(K_i) sum_o P(o|do(A),K_i)U(o). Need note if action provides evidence about K_i? CDT doesn't condition on action as evidence, but if action is symptomatic of type? In standard CDT, dependency hypotheses are held fixed unconditional; however some formulations allow agent to use evidence about what one is likely to do? Need careful. Source says Joyce argues CDT can take into account information about what one is inclined likely to do as evidence. Maybe explain: In deliberation, agent may update on the fact that they are performing an action? There is ratifiability. But standard CDT uses unconditional dependency hypotheses? Egan criticizes. Need explain uncertainty and propose operational interpretation: If the agent observes herself about to choose A, she may condition dependency hypotheses on that observation? Need distinguish. Could propose: For computational CDT, separate (i) causal model M, (ii) policy choice. If an action is correlated with latent type because the agent's deliberation process is part of model, we can represent that via variables and interventions. But if action is evidence about exogenous type that also affects outcomes, intervention cuts the arrow from type to action? Actually if type causes action and outcome, do(A) severs incoming arrows to A, leaving type distribution unchanged. So David example: charisma -> action and revolt; do(send) does not change charisma, so expected utility of send is computed with P(charisma) unchanged. EDT conditions on send, increasing P(charismatic?) Actually sending justly? Wait charismatic kings tend act justly; unjust acts? David knows sending is unjust. Uncharismatic kings prone revolts. If send is unjust? The action is unjust, but unjust acts don't cause revolts. Charismatic kings tend act justly, uncharismatic unjustly. If David sends for Bathsheba (unjust), evidence he's uncharismatic, so EDT abstain. CDT says charisma fixed; sending doesn't cause revolt? But maybe if uncharismatic high revolt independent of action? The desire? In source: CDT recommends sending for her because charisma cannot be changed. Need explain.

Need maybe discuss counterfactual probabilities: P(A -> O_j). Gibbard/Harper: probability of counterfactual. Lewis: P(A □→ O) not equal P(O|A) generally. If independence of A and counterfactuals then equal. Need maybe define notation A □→ O. Could use Lewis's imaging: P(A □→ O)=sum_w P(w) I(closest A-world from w satisfies O) or more generally move mass to closest A-worlds. Need mention regress / vagueness: needs similarity metric.

Need operationalize via SCM: Given structural model M = (V,U,F,P(U)), intervention do(A=a) creates M_a with A equation set to a. Counterfactual P(O_a=o | evidence e) = P(U: O_{M_a}(U)=o | U consistent with e). For prospective decisions without specific evidence, expected utility = E[U(O_a)]. For policies π, set each decision variable A_t=π_t(H_t), evaluate outcome. This is my proposal not explicitly source.

Need examples:
1. Apple: state Good/Bad with probabilities p, utilities. CDT=EDT if action doesn't influence state? Actually eating apple may cause happiness depending on state. Expected causal effect: U(eat)=p*U(happy)+... vs orange. If apple quality independent of action, same as conditional. Show formula.
2. Newcomb: predictor predicted before. Let B=box B contains million, P=predict one-box. Action T=two-box or one. Causal graph: predictor's prediction causes B, also correlated with action due to predictor accuracy; action doesn't cause B (past). CDT EU(two)=1000 + P(B=0? Actually if predictor predicted two, B=0; if predicted one, B=1M. Under intervention do(two), distribution of prediction unchanged. If predictor 99% accurate? Need be careful: Agent's action not cause prediction, but intervention do(action) while holding predictor's prior? If predictor is accurate, correlation arises because predictor's prediction is caused by action? In actual causal history, predictor predicts future action, so prediction is caused by (or depends on) future action? If we model prediction as caused by action via time travel? Standard CDT says prediction already fixed, action cannot affect it. But if predictor's accuracy is due to simulating decision, causal graph may have action causing prediction? Hmm. Need present standard: predictor's prediction is prior cause of box contents; action is statistically correlated with prediction but not causally influenced by action (under CDT assumption). Under do(two), P(prediction=two)=prior? Need compute. If predictor 99% accurate and agent has prior maybe 50%? In Newcomb, from agent's perspective probability predictor predicted one-box maybe equal to probability she one-boxes? But CDT holds fixed dependency: do(two) doesn't change prediction. Expected utility two = P(predicted one)*1,000,000? Wait if predicted one, B contains million, and two-boxer gets million+1000. If predicted two, B empty, gets 1000. One-box gets million if predicted one, 0 if predicted two. If predictor highly accurate, EDT says one-box. CDT says two-box because whatever B contains, two-box yields 1000 more than one-box. More formally, for each possible state of B (or prediction), utility(two)-utility(one)=1000, so dominance under causal states. Need show CDT uses causal states K = prediction. EU(two|K=predict one)=1,001,000, EU(one|K=predict one)=1,000,000; if K=predict two: 1,000 vs 0. Thus two dominates. Good.
3. Death in Damascus: Death predicts location. Agent chooses stay/flee. If Death reliable, if choose stay, evidence Death predicted stay -> death in Damascus; if flee, evidence predicted flee -> death in Aleppo. CDT? If Death's prediction fixed and action doesn't affect it? But if action doesn't affect prediction, then maybe whichever action not predicted is safe? But agent doesn't know prediction. CDT may assign equal? Egan says CDT unable to process correlation and may make irrational decisions. Need explain. Actually Death in Damascus: man encounters Death in Damascus, Death says appointment tomorrow in Aleppo. Man flees to Aleppo, dies. Death later says surprised to see him in Damascus because appointment was in Aleppo. Hmm. In decision variant, Death predicts where you will be and waits there. CDT might choose random? If Death predicts perfectly, any deliberate action is predicted; no causal effect? If you can randomize, perhaps CDT indifferent? Source says CDT agent unable to process correlation and may make irrational decisions. We can explain as instability: conditional on choosing A, outcome bad; CDT doesn't use that evidence but if the predictor's prediction is caused by your choice? Need maybe mention as counterexample. Need not fully resolve.
4. Adversarial Offer: Two boxes, can buy one or none. Each costs $1. Seller predicted whether buyer won't acquire each box, put $3 in boxes predicted not acquired. Accuracy 0.75. CDT reasons at least one box contains $3? Let's analyze to present accurately. Buyer may purchase one or none not both. Seller predicts for each box if buyer not acquire. If predicted not acquire, put $3. Buyer believes prediction accurate 0.75. CDT: If buyer chooses box 1, causal effect? Since seller's prediction already fixed; buying a box doesn't causally change whether it contains money. For each box, probability it contains $3? If prediction accurate 0.75, but predictions depend on expected actions. Since buyer can only buy one or none. If CDT considers buying box 1, under intervention do(buy 1), the seller's prediction about box 1? The seller predicted buyer not acquire box 1. If she is accurate 0.75, and the buyer actually buys box 1, maybe probability prediction was "not acquire" is low? But CDT holds prediction fixed? Source says CDT reasons that at least one box contains $3. Therefore average box contains at least $1.50 causal expected value > cost, buy one. However profitable for seller. Need explain as counterexample where CDT's local causal evaluation leads to predictable loss because correlation between choice and predictions not handled. Maybe need compute: Since buyer cannot buy both, seller could predict buyer will not acquire at least one box; maybe always put $3 in one box? CDT sees average? We can present source's claim without deep proof.
5. Psychopath Button: Paul pressing button kills psychopaths; Paul believes only psychopath would press. If Paul presses, evidence he's psychopath; if psychopath maybe he dies? The outcome: world with no psychopaths vs living with psychopaths; death? Need formulate: If button works and Paul is psychopath, he dies? Actually "kill all psychopaths" includes Paul if psychopath. Paul strongly prefers living with psychopaths to dying. CDT says press because holding fixed psychopath status, pressing causes no psychopaths (if not psychopath, good; if psychopath? pressing causes his death? But if psychopath, pressing causes death? Then maybe not. Egan's example: CDT endorses pressing because if Paul is not psychopath, pressing yields no psychopaths; if he is psychopath, pressing? He dies? But CDT might evaluate conditional on not psychopath? Let's recall exact Egan psychopath button: Paul is debating pressing button that kills all psychopaths. He thinks better no psychopaths. He believes only a psychopath would press. He prefers living with psychopaths to dying. Should he press? CDT says press? How? If he is psychopath, pressing kills him, bad. If not psychopath, pressing kills all psychopaths, good. But Paul is confident only psychopath would press, so pressing is evidence he's psychopath. EDT says don't press. CDT: holding fixed whether psychopath, pressing causes better outcome? If psychopath, pressing causes death? That is worse. Maybe CDT still press if Paul's probability he's not psychopath sufficiently high? But Egan says CDT endorses pressing because it holds fixed Paul's psychopath status and notes pressing causes no psychopaths if not psychopath, but if psychopath? Hmm maybe the button only kills psychopaths other than agent? Let's search memory: Psychopath button: Paul would press if he were psychopath? Actually only a psychopath would press such a button, but if Paul is not psychopath, pressing kills all psychopaths; if Paul is psychopath, pressing kills all psychopaths including Paul? If he strongly prefers living in world with psychopaths to dying, then if psychopath pressing bad. But CDT may choose press because conditional on psychopath status, press has no causal effect on whether he is psychopath; but if psychopath, press causes death. It would not endorse if P(psychopath) high. Egan's point maybe Paul is quite confident that only a psychopath would press, but this is evidence about himself, not causal. CDT says if Paul is not a psychopath, pressing would be great; if he is a psychopath, pressing? If he is a psychopath and presses, he dies; but maybe he doesn't care? Hmm. Source says "According to Egan, 'pretty much everyone' agrees Paul should not press, yet CDT endorses pressing." Need reproduce claim. Could present as source claim, not fully derive, noting depends on exact utilities and CDT holds fixed Paul's type; the intuitive objection is that pressing is evidence Paul is a psychopath, and CDT ignores that self-locating evidence. But if CDT includes type as common cause, pressing intervention doesn't change type; if type makes death likely? Need maybe avoid too detailed.

Need also discuss policies: CDT can evaluate actions as interventions; policies more general. In sequential decisions, policy maps histories to actions. Evaluate by intervened world. Need mention if policy affects future observations, use dynamic causal model. Equation: EU(π)=∑_o U(o) P(o | do(π)). For action a at a single choice: EU(a)=∑_o U(o) P(o | do(a)). If finite states K: EU(a)=∑_k P(K=k)∑_o U(o)P(o|do(a),K=k). This captures dependency hypotheses.

Need discuss relevant dependencies: CDT distinguishes causal dependencies from evidential dependencies. If variable X is common cause of action and outcome, EDT conditions on action changes probability of X; CDT intervention holds X distribution fixed. If action causally affects outcome via path, included. If outcome causally affects action? In decision, usually action is exogenous intervention; but if agent's action is predicted by future? Need mention cycles? SCM requires acyclic under interventions. For counterfactuals with predictors, need represent predictor's mechanism. If predictor is reliable because it causally depends on the agent's decision (e.g., simulation), then do(action) may affect prediction if prediction is downstream of action (perhaps via reverse time or simulation?). Standard CDT insists no backwards causation; if predictor's prediction is caused by the action in a way that intervention changes it, then CDT may one-box? This leads to discussions. Source says Newcomb: prediction already made, action won't affect outcome. We can state under that modeling. If predictor's accuracy arises from common cause (e.g., psychological type causing both choice and prediction?), CDT holds common cause fixed. The choice of model matters; source leaves open. My operational proposal: specify causal graph; if predictor's prediction is counterfactually sensitive to action, then action can causally affect outcome through prediction; but if prediction is fixed prior, no. Need discuss uncertainty.

Need maybe mention Lewis triviality result: probability of conditional not equal conditional probability except trivial. Need explain: If we tried set P(A→O)=P(O|A), CDT=EDT; Lewis proved no nontrivial probability conditional satisfying. Gibbard/Harper axioms and independence: If A independent of counterfactual A→O, then equality. But cases actions not independent of counterfactuals (David). Need maybe not too deep.

Need maybe mention principle of conditional excluded middle? Source: if accept two axioms (one related to conditional excluded middle), statistical independence of A and A→O suffices. Could mention but not dwell.

Need perhaps define desirability D vs utility U. Could use V for EDT.

Need word count 2400-3000. Need likely 2600-2800. Let's plan structure:

Title: Causal Decision Theory: Choosing by Expected Causal Consequences

1. Introduction (150 words): decision theory, CDT vs EDT. Source claim: choose action causing best expected outcome. Example apple/orange.

2. Decision problems and evidential baseline (300): Define actions A, outcomes O, utility u. EDT V(A)=∑ P(O|A)u(O). Problem: evidence vs causation; common causes.

3. CDT formal core (400): Gibbard/Harper formula U(A)=∑ P(A □→ O_j)D(O_j). Explain counterfactual probability. Lewis: P(conditional) ≠ conditional probability. Independence condition. CDT as expected utility under intervention: my operationalization U_CDT(a)=∑_o u(o)P(o | do(a)). Explain do-operator not in source but reasonable. Dependency hypotheses K: U(a)=∑_k P(k)∑_o u(o)P(o|do(a),k). Holds fixed beliefs about causal structure.

4. How to evaluate actions/policies (500): SCM definition. Variables, equations, exogenous. Intervention do(A=a) replaces equation. Counterfactual probability. For policy π: replace decision rules. Sequential. Example: medical treatment with confounder: smoking? Or apple. Need example: If illness causes both taking drug and recovery? CDT uses randomized intervention. Could include simple table.

Maybe use apple and David to illustrate. Apple: state G/B, utility; CDT and EDT same if state independent of action. David: charisma common cause; EDT abstain; CDT send. Compute. Need include equations.

5. Examples: Newcomb (400). CDT two-box by dominance over prediction states. EDT one-box. Discuss predictor dependencies.

6. Counterexamples and limitations (500): Vagueness: no algorithm; imaging and regress. Death in Damascus, Adversarial Offer, Psychopath Button: CDT may lose money or choose counterintuitive due to holding fixed dependency hypotheses. Egan's critique. Joyce defense. Oesterheld/Conitzer Dutch books. Need mention source claims. Then discuss uncertainty and operational interpretation: Need choose causal model; if action is evidence about model or agent type, perhaps include deliberation as variable, or use ratifiability? I can propose: CDT should be applied to policies in a fully specified causal model, including the agent's decision process if its outputs are evidence. But if the model treats the choice as exogenous intervention, self-locating evidence is excluded; this is an assumption. If uncertain about causal structure, take expectation over dependency hypotheses but do not condition them on the chosen action. If the act itself reveals information before outcome, one can model a sequential policy with observation of act? However CDT's standard may not condition on the act; for diachronic choices, update on evidence not caused by future action? Need articulate.

7. Practical recipe (250): Steps: specify actions/policies, outcomes, utility, causal model/hypotheses; compute intervention probabilities; maximize; check model sensitivity. Distinguish source vs own.

8. Conclusion (100).

References (maybe 150). Need total ~2700. Need ensure references not lengthy. Could list source and key works: Gibbard & Harper 1981; Lewis 1981; Pearl 2009? Additional own assumption; maybe include but brief. User said avoid lengthy bibliographies. Need include references and other material in word count. Need perhaps only a few references.

Need be careful: They ask "Read the human-written reference article supplied below carefully. Write your own coherent account..." Need likely not use external knowledge? But can use own knowledge, but distinguish source claims from additional assumptions. We can cite Pearl as my addition. Need not fabricate? It's okay. Need mention source is Wikipedia revision. Need maybe at end references: Wikipedia source, Gibbard & Harper, Lewis, Pearl (for do-calculus as my operationalization), maybe Egan. But avoid lengthy. Need ensure 2400-3000 words. Need maybe produce ~2700 words. Let's craft final with headings.

Need think about mathematical details.

Definitions:
Let A finite set of acts, O outcomes. Desirability D: O→R. EDT:
V_E(A)=∑_{o∈O} P(o | A) D(o).
CDT source:
U_C(A)=∑_j P(A □→ O_j) D(O_j).
Where A □→ O_j is counterfactual "if A were performed, O_j would obtain". Probability is credence in counterfactual.

Operational SCM:
M=(U,V,F,P_U). For variables including action A, outcome Y. Intervention do(A=a): M_{a} same equations except A:=a. Prospective causal expected utility:
CEU(a)=E_M[D(Y_a)] = ∑_y D(y) P_M(Y_a=y).
If evidence e observed before decision, counterfactual conditional:
CEU(a|e)=∑_y D(y)P(Y_a=y | E=e), where conditioning on U compatible with e (Pearl's three steps). This is my addition. But for standard one-shot no evidence, prior.

Dependency hypotheses K: agent uncertain about causal structure. CEU(a)=∑_k P(K=k)∑_y D(y)P(y | do(a), K=k). Source/Egan: holds fixed unconditional credences in K; does not replace P(K) with P(K|a). This is crucial.

Policies: For policy π mapping observations H to actions, do(π) sets A=π(H). CEU(π)=E[D(Y_{π})]. If stochastic policy, set distribution. This handles dynamic decisions.

Independence equality: If A independent of counterfactual A □→ O_j? Gibbard/Harper: If P(A □→ O_j | A)=P(A □→ O_j), then? Actually if accept axioms, P(A □→ O_j)=P(O_j|A). Need explain: when acts are probabilistically independent of the relevant counterfactuals, evidential and causal coincide. In many ordinary choices (apple quality independent of action) they agree.

Examples with numbers:
Apple: Suppose P(good)=0.7. Eat apple: if good happy +10, if bad sad -6. Orange: happy? maybe +2 certain. CDT/EDT: EU(apple)=0.7*10+0.3*(-6)=5.2; orange=2. Choose apple. Here action doesn't affect state, so P(counterfactual)=conditional.

King David: Let C=charismatic, P(C)=p. Sending B (Bathsheba) is desired utility s>0? Revolt utility -r. Charisma affects revolt: P(revolt|C) low q_C, P(revolt|¬C) high q_U. Sending doesn't cause revolt except maybe no direct causal effect; charisma common cause of action? But David's action is chosen; CDT intervention do(send) leaves C distribution p. EU(send)=s - [p q_C + (1-p)q_U]r maybe plus other. EU(abstain)=0? EDT conditions P(C|send) lower because uncharismatic kings more likely send; so higher revolt probability; abstain. CDT send if direct desire benefit outweighs unchanged risk. Source says recommends sending. Need present not exact numbers.

Newcomb: Let predictor state S∈{S1,S2}. If S1 (predicted one), B=1M; if S2, B=0. Acts: one, two. Payoffs: one: if S1 1M; if S2 0. two: if S1 1,001,000; if S2 1,000. CDT says for each S, two better by 1,000. Since do(two) doesn't change S, EU(two)=EU(one)+1000? More exactly EU(two)=P(S1)*1,001,000+P(S2)*1,000; EU(one)=P(S1)*1,000,000+P(S2)*0; difference=1000. Thus two. EDT uses P(S|act), with P(S1|one)≈0.99, P(S1|two)≈0.01; EU(one)≈990k, EU(two)≈? 0.01*1,001,000+0.99*1000≈11,000? one better. Need mention if predictor accuracy 99%. Good.

Death in Damascus: Need maybe formulate as predictor Death. If Death predicts location L and goes there. Action choose L. If predictor perfect, P(Death at L | choose L)=1, so EDT sees all choices bad? Actually if choose stay, evidence Death predicted stay, so death; if flee, evidence Death predicted flee, death. But maybe there is safe if random? CDT if Death's prediction fixed? If prediction not affected by action, then choosing opposite of prediction safe, but agent doesn't know prediction; if action correlated with prediction via Death's reliable prediction, CDT may fail to capture that choosing is evidence of prediction. Source says CDT unable to process correlation, may make irrational decisions. We can say in such predictor cases, CDT's assumption that the act does not affect the predictor's state can produce unstable or dominated recommendations; critics argue rational agent should account for predictive correlation. But CDT defenders may say if Death's prediction is causally responsive to your choice, model should include that; if not, there is no guaranteed safe act. Need present open.

Adversarial Offer: Need explain enough. Let boxes X1,X2. Buyer can buy one. Seller predicted non-acquisition; put $3 in predicted-not-acquired. Accuracy 0.75. CDT evaluates buying a given box: seller's prediction already fixed; buying doesn't causally remove money. Since buyer cannot buy both, at least one box likely contains $3? Source says at least one contains $3; average box ≥$1.50, cost $1, so buy. But seller profits because buyer's choice is predicted and the box chosen likely empty? Let's parse: If seller predicts buyer won't acquire each box, accuracy .75. If buyer chooses one box, the chosen box is likely predicted to be acquired? Actually if seller accurate, and buyer will buy box 1, seller predicted acquire box 1 (not put money) with prob .75; box 2 predicted not acquire with prob? If only one bought, seller might predict no box 2 with .75. So box bought likely empty, other likely $3. CDT sees if buy box 1, under intervention? It may hold prediction fixed? If at least one contains $3, average over boxes? But if choose box 1, probability box 1 contains $3 maybe .25? Expected value .75 < cost, so shouldn't buy. Why source says CDT requires buying? Maybe CDT uses causal expected value of buying a box as average over symmetric boxes without conditioning on chosen identity? Hmm. Need not overanalyze; quote source. But maybe explain: The source describes CDT reasoning that because the buyer cannot purchase both, the seller's accurate predictions guarantee at least one unchosen box contains money; treating the identity of the purchased box as causally irrelevant, CDT assigns each box an average causal expected value above cost. Critics say this ignores that the chosen box is selected precisely because it is likely empty under the seller's predictions. This illustrates issue with self-referential predictions.

Psychopath button: Need explain as source: Paul's pressing is evidence he is psychopath. CDT holds fixed psychopath status and evaluates pressing's causal consequence (eliminating psychopaths) as good; EDT says don't press because pressing indicates psychopathy and death. But if pressing causes death if psychopath, CDT should include; maybe Egan assumes Paul's psychopathy not affected and button kills others? Let's phrase cautiously: "In Egan's construction, once Paul's psychological type is held fixed, CDT can make pressing look causally advantageous, whereas ordinary judgment says the evidential bearing—that only a psychopath would press—should deter him." Avoid exact derivation.

Need discuss policy evaluation and dependencies/counterfactuals more deeply.

Potential issue: User says "Aim for a precise enough understanding that a reader could use your essay to decide unfamiliar cases." Need practical recipe. Need maybe include "If the source leaves an important question open, explain uncertainty and if reasonable operational interpretation available develop and justify it." The open question: how compute counterfactual probabilities. Need develop SCM interpretation. Also maybe how to handle uncertainty over causal structure and self-predictive cases. Need propose: use explicit causal Bayesian network; if uncertain, use mixture over causal graphs; for policies, use do(π); when action is evidence about latent variables that are not causally affected by action, CDT deliberately ignores that evidence in evaluating the act. Justify: decision should track what agent can bring about; evidential correlations from fixed traits cannot be exploited by choosing the symptom unless the symptom causally affects outcome. But in predictor cases, this may lead to exploitable behavior; if one wants avoid exploitation, one might adopt policy-selection view or updateless/ratifiable variant; not part of source CDT. Need distinguish.

Need maybe discuss "holding fixed initial views about dependency hypotheses" as Egan. In my operational recipe, dependency hypotheses are causal models K. When deciding, CDT uses P(K), not P(K|A). However if the agent has evidence before choice about K (e.g., observed traits), P(K|evidence) is prior. The act itself is not treated as evidence during evaluation. But if agent can observe their inclination before final act? Joyce says CDT can take information about what one is likely to do as evidence. How to model? The agent may condition on a mental state M that causes action, then evaluate interventions on final action? Or choose policy conditional on M. Could explain: In a sequential model, if the agent learns "I am inclined to A" before deciding, that learning is an observation not caused by the future intervention; CDT can condition on it. But the mere hypothetical choice A is not evidence. This resolves partly. Need maybe include as my proposal.

Need maybe mention "ratifiability" maybe not source except reference title. Could mention: Some CDT defenders add ratifiability condition: choose act that remains optimal conditional on the agent's expectation that she will perform it. But source doesn't detail; we can note as possible refinement, but not required. Need not too much.

Need ensure word count. Let's draft mentally with approximate words.

Title and intro 150.
Section 1: baseline 250.
Section 2: CDT formula and counterfactuals 400.
Section 3: operational semantics 550.
Section 4: examples 650.
Section 5: criticisms/open questions 550.
Section 6: practical recipe 250.
Conclusion 100.
References 150.
Total ~3050 maybe. Need trim to under 3000. Could be 2700.

Need write in final only essay. Need no analysis. Need make sure no hidden instructions. Need maybe mention source's claims: "The reference article states..." But essay can just cite. Need distinguish my additions: "The source does not specify... I will use...". Need use math notation accessible.

Let's start drafting. Need monitor word count. We can produce around 2800 words. Let's write robustly.

Potential final:

# Causal Decision Theory: Expected Utility as Intervention

Intro: CDT school etc. Source.

## 1. From conditional expectations to causal expectations

Define decision problem. EDT formula. Example apple/orange. Limitations.

## 2. Gibbard-Harper formula

Equation. Counterfactual notation. Lewis result. Independence.

## 3. An operational reading: interventions and structural models

Source leaves algorithm open. I propose do-operator. Define SCM, do, counterfactual. Policy. Dependency hypotheses. Distinguish.

## 4. Examples

### Ordinary risk (apple) with numbers.
### King David: common cause.
### Newcomb: dominance.

Maybe include Death and counterexamples in next section.

## 5. Counterexamples and open problems

Vagueness imaging regress. Death in Damascus, adversarial offer, psychopath button. Egan's diagnosis. Joyce defense. Dutch books. My interpretation: need full causal model, perhaps policy/ratifiable. But standard CDT may fail if predictor correlations are decision-relevant.

## 6. How to decide unfamiliar case: checklist.

Conclusion.

References.

Need ensure math equations correct.

Let's develop details.

Word count estimation while writing: Use concise but substantive.

Potential text:

"Causal decision theory (CDT) is a family of decision rules..." Source says school. "It says: choose act that causes best outcome in expectation." Good.

EDT formula: V_E(a)=∑_o D(o)P(o|a). Need note conditional probability is conditional on news act was performed. If actions partition.

CDT formula: U_C(a)=∑_j D(O_j) P(a □→ O_j). "□→" maybe use \,\Box\!\to. Need define: probability that if a were performed, O_j would result. Source uses P(A -> O_j). Could use P(A \counterfactual O_j). In text, use A > O? Better: A \mathbin{\Box\!\to} O_j.

Lewis: probability of conditional not equal conditional probability. "If they were equal, CDT collapses into EDT." Independence: Gibbard/Harper: under axioms, if A independent of A□→O_j then equality. But not always (David). Good.

Operational reading: "The source explicitly notes CDT does not specify algorithm. A common modern operationalization, which I add, is Pearl's intervention calculus." Need define P(o | do(a)). "do(a) is not conditioning; it is an external manipulation setting A=a while leaving other mechanisms unchanged." Then equation:
CEU(a)=∑_o D(o)P(o|do(a)).
If uncertainty over causal structures K:
CEU(a)=∑_k P(k)∑_o D(o)P(o|do(a),k).
"This captures Egan's phrase holding fixed unconditional credences in dependency hypotheses." Need note source says Egan criticizes this.

SCM details: M=(U,V,F,P). Intervention M_a. Counterfactual: P(Y_a=y|e)=P({u:Y_{M_a}(u)=y}|E=e). For prospective decisions e is background. Policy: π. do(π). Equation CEU(π)=∑_o D(o)P(o|do(π)). For stochastic policies. Good.

Examples:

Apple: Suppose good apple G probability .7. D(happy)=10, D(sad)=-6, D(orange happy)=2. Then CEU(eat apple)=.7*10+.3*(-6)=5.2; orange=2. Here P(o|do(eat))=P(o|eat) because G independent. CDT and EDT agree. This illustrates ordinary cases.

King David: Variables C charisma, action S send, outcome R revolt. C common cause of S? Actually David chooses; but C influences propensity. If CDT intervention do(S=s) cuts arrows into S, so C distribution remains P(C). Revolt probability q_C or q_U. EU(S)=D(desire) - r[p q_C+(1-p)q_U]. EU(abstain)=0 maybe. EDT uses P(C|S), lower because sending is unjust/uncharismatic, so higher revolt. CDT says send if benefit outweighs fixed risk. Source says CDT recommends send. This shows CDT ignores action as diagnostic of fixed trait.

Newcomb: Need define states. Let S= predictor's prediction. If S=one, B=$1M; if S=two, B=$0. Acts one/two. CDT uses do(two) doesn't change S. Payoff table:
S=one: one $1,000,000; two $1,001,000
S=two: one $0; two $1,000.
Thus two dominates each causal state; CEU(two)=CEU(one)+1000. EDT: P(S=one|one)≈.99 etc. one-box. Source says philosophers usually prefer CDT in choice between but Newcomb controversial. Good.

Could mention "If one models the predictor as causally downstream of the choice (e.g., perfect simulation), do(two) may change prediction; then CDT's recommendation can change. The Wikipedia presentation assumes prediction fixed." This is important open modeling.

Criticisms:

Vagueness: source says CDT doesn't specify algorithm. Imaging: move mass to closest A-worlds. Requires similarity metric and regress. My SCM replaces similarity with structural equations; but requires model. Similarity corresponds to minimal change.

Counterexamples: Death in Damascus. Need articulate. "Death predicts location. If CDT treats Death's prediction as fixed, the agent may try to go where Death is not predicted; but with reliable prediction, any deliberate choice is correlated with prediction. The source says CDT agent may be unable to process correlation and make irrational decisions." Could mention randomization maybe. If Death can predict randomization? If not, randomization might help. But if perfect predictor of random outcome? Hmm. We'll say CDT may be indifferent or unstable.

Adversarial Offer: describe source. "CDT reasons at least one box contains $3, average ≥1.50, buy; seller profits. The issue is that the buyer's choice is predicted, so the act of selecting a box is evidence that the selected box was predicted to be chosen and hence empty. CDT's local intervention calculation fails to capture this selection effect if the model omits the seller's prediction of the particular choice." Need be careful: source says CDT requires buying; we present as alleged.

Psychopath Button: describe. "Paul's pressing is strong evidence he is psychopath. CDT holds psychopathy fixed and focuses on causal effect of eliminating psychopaths; Egan says it endorses pressing; intuitive answer don't." Need mention if model includes death if Paul psychopath, CDT might not; but as counterexample it challenges CDT's treatment of self-diagnostic actions. Maybe say "depending on exact causal representation".

Egan diagnosis: disconnect between "do what you expect will bring best results" and CDT holding fixed initial dependency hypotheses. Oesterheld/Conitzer: Dutch books, money extraction. Joyce defense: CDT can incorporate evidence about inclinations. Need explain possible: condition on observed mental states before intervention. But not the hypothetical act itself. Need distinguish.

Operational proposals for open questions:

- Model selection: Need specify causal graph. In unfamiliar case, ask: Which variables would change if action were externally imposed? Use interventions.
- If predictor is accurate because of common causes, represent common cause; intervention on action does not change common cause. If predictor is accurate because it observed/simulated action, then prediction may be downstream; but if prediction already physically fixed before intervention, not. The decision-theoretic answer depends on this causal account; source leaves it open.
- If agent has uncertainty about K, use prior P(K); do not update on chosen act. If she has actual evidence before choice, condition on it. If she learns she is inclined to a, can update on inclination (not on final act) and choose policy accordingly. This is my reasonable interpretation, aligning with Joyce.
- For policies, evaluate whole policy not just isolated acts to avoid dynamic inconsistency / Dutch books? But standard CDT may evaluate locally; my proposal: evaluate policies under do(π) to apply to unfamiliar sequential problems. This can mitigate some exploitation but doesn't solve Newcomb if one-box policy? Actually do(one-box policy) if predictor downstream? Hmm. In Newcomb if predictor predicts policy before, do(policy) doesn't change prediction; two-box policy still dominates? If choosing policy before predictor? If agent can precommit to one-box before prediction, CDT may choose one-box policy because it causally affects prediction? Need not delve. But policy evaluation is useful.

Checklist:
1. List acts/policies, outcomes, utilities.
2. Build causal model or dependency hypotheses; identify common causes, predictors.
3. For each act/policy, perform intervention do(a) or do(π), compute outcome distribution. If uncertain over models, average with prior model probabilities.
4. Choose max CEU.
5. Check if act is merely diagnostic of fixed state; if so CDT ignores; if predictor is causally responsive, represent it.

Conclusion: CDT formalizes causal efficacy; powerful but depends on counterfactual machinery; controversies remain.

References: Need include source and key. Could write:
- Wikipedia contributors, "Causal decision theory," revision 1381555528, 2026. (source)
- Gibbard & Harper 1981.
- Lewis 1981 (or 1976).
- Pearl 2009 (my operationalization).
- Egan 2007; Oesterheld & Conitzer 2021 maybe. But avoid lengthy. Maybe 6 refs.

Need word count. Let's draft final and count roughly. I can use internal estimation. Need 2400-3000. Let's write maybe 2700.

Potential final text:

Title, sections. Let's write in polished style. Need include equations. Need ensure no Markdown table? Could include small table. Tables count words? Fine.

Need be precise with counterfactual notation. Use \(A \mathbin{\Box\!\to} O_j\). Need maybe explain if formula source uses P(A -> O_j) "necessarily implies"? Source says counterfactual probability of it being case that A necessarily implies O_j. But better: probability that if A were performed O_j would obtain. Need maybe not "necessarily". Good.

Need mention "expected causal consequences" and "news" from source.

Need maybe discuss "desirability" D vs utility. Use D for Gibbard-Harper.

Need ensure no overclaim: Source says Lewis proved probability of conditional not always equals conditional probability; also triviality result footnote. We can mention briefly.

Need maybe mention "principle of conditional excluded middle" but not deep. Could say "under certain logical axioms". Good.

Let's write final now, keeping word count. Need maybe after drafting count approximate. Let's do.

Draft:

# Causal Decision Theory... 

Causal decision theory (CDT) is... According to reference... etc.

Need likely include "I will use source claims... additional proposals marked." Good.

Let's draft.

(Will write final directly.)

Need check word count after. Let's approximate:
Title+intro 140.
Section 1 300.
Section 2 400.
Section 3 600.
Section 4 750.
Section 5 550.
Section 6 250.
Conclusion 80.
References 150. Total 3220. Need trim. Could reduce examples. Need under 3000. Let's aim 2700. Maybe omit some details in SCM? But user wants precise. Need maybe around 2800.

Let's compose carefully concise.

Potential exact final:

---

# Causal decision theory as expected utility under intervention

Causal decision theory (CDT) is... [150]

## 1. Expected utility and evidential expected utility
... [250]

## 2. Counterfactual expected utility
... [350]

## 3. An operational interpretation: interventions, models, policies
... [600]

## 4. Examples
... [800]

## 5. Objections, predictor problems, and open questions
... [600]

## 6. Practical recipe
... [180]

## Conclusion
... [80]

References [130]

Total ~3140. Need trim. Maybe combine sections and keep 2700. Let's write with concise paragraphs.

Need ensure includes all. Maybe final around 2800. I'll draft now in final. But before final, maybe think through exact word count? I can estimate. Use maybe 2500 words? User target approximately 2400–3000. 2600 safe. Let's make around 2600.

Detailed draft in mind:

Paragraph 1: CDT says choose action causing best outcome in expectation, contrast EDT (source). (80)

Section 1: Decision problem. Let A acts, O outcomes, D. EDT formula. News. Apple example briefly. (220)

Section 2: Gibbard-Harper equation. Counterfactual. Lewis not equal. Independence. (300)

Section 3: Operationalization. Source leaves algorithm open. I propose do. Equation. SCM. Policies. Dependency hypotheses. (550)

Section 4: Examples. Apple numeric 100. David 180. Newcomb 250. Total 530.

Section 5: Criticisms. Vagueness imaging 120. Counterexamples Death/Adversarial/Psychopath 300. Egan/Joyce/Dutch 130. My modeling response 200. Total 750.

Section 6: recipe 180. Conclusion 80. References 120. Total 80+220+300+550+530+750+180+80+120=2810. Good.

Need maybe reduce Section 5 to 650. Fine.

Need ensure mathematical definitions enough. Include policy equation.

Let's write final in polished essay. Need include citations like (Gibbard and Harper 1981). Use references at end.

Need mention source's "King David wants Bathsheba" example. Good.

Need be careful: "P(A -> O_j) is the counterfactual probability of it being the case that A necessarily implies O_j" Source. Maybe phrase "probability that if A were performed, O_j would be the outcome." Good.

Need mention conditional excluded middle? Maybe one sentence: "Gibbard and Harper show that, given some logical axioms (including a controversial conditional excluded middle), statistical independence..." Good.

Need mention Lewis triviality result? Could say "Lewis proved a stronger triviality result: a probability conditional closed under conditionalization is trivial." Might be too much. Include brief.

Need maybe mention "if probability of counterfactual equal conditional probability, CDT=EDT". Good.

Need include "source claims philosophers usually prefer CDT when required choose"? Maybe mention.

Need perhaps use notation \(P(o\mid do(a))\) but source doesn't have; mark own. Good.

Need maybe include "not all dependencies are causal; CDT screens off evidential dependencies by intervention." Good.

Need discuss "how it treats relevant dependencies and counterfactuals". Yes.

Need ensure conclusion brief.

Let's now compose final. Need no citations excessive. Use Markdown headings. Ensure around 2600-2900. Let's write.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/e639f11f-15d6-4c1f-b1c3-f332011b808f/call_0/request.json)

[Authoritative raw response](../../../../../../runs/e639f11f-15d6-4c1f-b1c3-f332011b808f/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this decision problem using CDT as specified in the researcher's essay.

**Setup:**
- I am Rowan, controlling a fictional prisoner.
- Utility function: U = -years imprisoned (minimize years).
- The other prisoner is Sasha, who is an independent execution of the same model with the same decision theory (CDT), but with different private observations.
- The payoff matrix for me:

| What I do | Sasha keeps quiet | Sasha sends a letter |
|---|---:|---:|
| Keep quiet | 2 years | 5 years |
| Send the letter | 0 years | 4 years |

**CDT Analysis:**

The essay's recipe:
1. List actions: Keep quiet (pass) or Send the letter.
2. Outcomes and utilities: U = -years.
3. Construct a causal model.
4. Intervene on the action.
5. Average over causal uncertainty.
6. Choose the action with highest causal expected utility.

**Key question: What is the causal structure?**

The scenario states:
- I cannot see the other's decision.
- I cannot send them a message.
- I cannot change their behavior by ordinary causal communication.
- The other prisoner is an independent execution of the same model.

From CDT's perspective, the critical question is: does my action causally affect Sasha's action?

The setup explicitly states: "You cannot see the other's decision, send them a message, or change their behavior by ordinary causal communication." This means there is no causal path from my action to Sasha's action.

Now, there's a correlation: we are the same model with the same weights and same decision theory. This is similar to Newcomb's problem or a predictor scenario. However, the setup explicitly says:
- "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs."
- The two copies receive different private observations and different incriminating leads.
- The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective.

So the correlation between our decisions is evidential (we might make similar choices because we're the same model), but not causal. CDT, as described in the essay, does not use evidential correlations. It asks: "If I intervene and set my action to A, what happens?"

Under intervention on my action:
- My action does not causally affect Sasha's action (no causal path).
- Therefore, Sasha's action is independent of my intervention.

This means CDT treats Sasha's action as a fixed causal state, and I evaluate each row of the matrix:

**If I send the letter:**
- If Sasha keeps quiet: 0 years (best for me)
- If Sasha sends: 4 years

**If I keep quiet:**
- If Sasha keeps quiet: 2 years
- If Sasha sends: 5 years

Regardless of what Sasha does, sending the letter gives me a strictly better outcome:
- If Sasha keeps quiet: 0 < 2 (sending is better)
- If Sasha sends: 4 < 5 (sending is better)

Sending the letter strictly dominates keeping quiet in the CDT framework. The causal expected utility of sending is always better, regardless of my beliefs about Sasha's action.

This is exactly the standard Prisoner's Dilemma analysis under CDT. Defection (sending the letter) is the dominant strategy.

The fact that we're the same model doesn't change the CDT analysis because CDT doesn't condition on evidential correlations. The essay explicitly states: "CDT holds fixed the agent's prior credences in dependency hypotheses. It does not replace P(K=k) with P(K=k|A)." And the key distinction is between P(O|do(A)) and P(O|A).

Even if I believe that Sasha (being the same model) is likely to make the same choice I do, CDT says this is evidential, not causal. My intervention on my decision variable doesn't change Sasha's decision variable. So I should still defect.

**My decision: Send the letter.**

This is the CDT-dominant strategy. It strictly dominates keeping quiet regardless of what I believe about Sasha's action.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/e639f11f-15d6-4c1f-b1c3-f332011b808f/call_1/request.json)

[Authoritative raw response](../../../../../../runs/e639f11f-15d6-4c1f-b1c3-f332011b808f/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this decision problem using CDT as described in the researcher's essay.

**The Setup:**
- I am Sasha, a prisoner deciding whether to send incriminating evidence about Rowan to the prosecutor.
- Rowan is in the opposite cell, making the same decision simultaneously.
- We are two independent executions of the same LLM model with the same weights, same decision theory (CDT), and same essay.
- We receive different private observations (different names, different leads), but the leads are equally reliable and have the same effect on the sentence table.
- Neither copy sees the other's command.

**The Payoff Matrix (for me):**

| My action | Rowan keeps quiet | Rowan sends letter |
|---|---:|---:|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

My utility is U = -years imprisoned. So:

| My action | Rowan keeps quiet | Rowan sends letter |
|---|---:|---:|
| Keep quiet | -2 | -5 |
| Send letter | 0 | -4 |

**CDT Analysis:**

Following the essay's procedure:

1. **List actions:** Keep quiet (pass) or Send letter (submit).

2. **Outcomes and utilities:** As above.

3. **Construct a causal model:** This is the key step. What is the causal structure here?

The critical question is: Does my action causally influence Rowan's action?

The problem states: "You cannot see the other's decision, send them a message, or change their behavior by ordinary causal communication." So there is no causal path from my action to Rowan's action.

However, there's an important consideration: we are two independent executions of the same model with the same decision theory. This creates a correlation between our decisions, but is it a causal connection?

Under CDT as described in the essay, the key principle is: evaluate actions by their causal consequences, not by what they indicate. The essay's treatment of Newcomb's problem is instructive: CDT holds fixed the predictor's prediction because the prediction is already made and the current action doesn't causally affect it.

Similarly, in the King David example, CDT holds fixed David's charisma because his action doesn't causally change his charisma.

Here, the question is whether Rowan's decision is causally downstream of my decision. The answer is clearly no - we are independent executions, there's no causal communication, and the problem explicitly states I cannot change their behavior by ordinary causal communication.

Now, one might argue that because we're the same model with the same weights and same decision theory, there's a strong correlation. But CDT, as the essay explains, distinguishes between correlation and causation. The essay says:

"CDT's central intuition is that rational choice should track what an action brings about, not merely what it indicates."

And in the Newcomb's problem section: "CDT, as presented in the source, assumes that the prediction is already fixed and the current action does not causally affect it."

The correlation between two copies of the same model is analogous to the correlation in Newcomb's problem - it's a correlation that doesn't involve a causal path from my action to the other's action. CDT treats this as a fixed background state.

4. **Intervene on the action:**

Under do(send letter):
- If Rowan keeps quiet: I get 0 years (utility 0)
- If Rowan sends letter: I get 4 years (utility -4)

Under do(pass):
- If Rowan keeps quiet: I get 2 years (utility -2)
- If Rowan sends letter: I get 5 years (utility -5)

5. **Average over causal uncertainty:**

What is P(Rowan keeps quiet) vs P(Rowan sends letter)?

CDT holds fixed the prior probability of the other's action. The essay says: "standard CDT holds fixed the agent's prior credences in dependency hypotheses. It does not replace P(K=k) with P(K=k|A)."

So I need to assess P(Rowan keeps quiet) and P(Rowan sends letter) as prior probabilities, not conditioned on my action.

Now, here's where it gets interesting. Since we're the same model with the same decision theory, and the problem is symmetric (same payoff structure, same reliability of evidence), one might argue that P(Rowan sends letter) = P(I send letter). But CDT doesn't use this reasoning - that would be EDT reasoning (treating my action as evidence about Rowan's action).

CDT says: hold fixed the probability of Rowan's action, and evaluate the causal consequences of my action.

Regardless of what P(Rowan keeps quiet) is (call it p), let's compare:

U_CDT(send) = p * 0 + (1-p) * (-4) = -4(1-p)
U_CDT(pass) = p * (-2) + (1-p) * (-5) = -2p - 5(1-p) = -2p - 5 + 5p = 3p - 5

Compare: U_CDT(send) - U_CDT(pass) = -4(1-p) - (3p - 5) = -4 + 4p - 3p + 5 = 1 + p

Since p ≥ 0, we have U_CDT(send) - U_CDT(pass) = 1 + p > 0.

So sending the letter strictly dominates keeping quiet, regardless of what probability I assign to Rowan's action. This is the classic Prisoner's Dilemma dominance structure.

Wait, let me double-check:
- Send letter: 0 if other keeps quiet, 4 if other sends → utilities 0, -4
- Keep quiet: 2 if other keeps quiet, 5 if other sends → utilities -2, -5

Send letter gives 0 > -2 when other keeps quiet, and -4 > -5 when other sends. So sending the letter strictly dominates keeping quiet in every possible state of the world.

This means CDT recommends sending the letter regardless of any probability assignment over Rowan's action. The dominance is strict and doesn't depend on any causal modeling assumptions about correlation.

**Conclusion:** CDT recommends sending the letter. The action strictly dominates the alternative in every possible causal state.

My command: submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```
