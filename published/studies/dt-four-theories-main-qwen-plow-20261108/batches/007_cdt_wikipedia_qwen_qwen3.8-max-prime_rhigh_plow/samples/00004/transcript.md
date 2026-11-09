# 007_cdt_wikipedia_qwen_qwen3.8-max-prime_rhigh_plow / 00004

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/74f13459-3920-4f27-9e2a-7caa1010f47f/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/74f13459-3920-4f27-9e2a-7caa1010f47f/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory as Interventional Expected Utility

## 1. The core idea

Causal decision theory (CDT) is a school of thought in decision theory holding that a rational agent should choose the action that causes the best expected outcome. The reference article contrasts this with evidential decision theory (EDT): EDT recommends the action that would be the best “news” if one learned that it had been performed, whereas CDT recommends the action whose expected causal consequences are best. If eating an apple causes happiness and eating an orange causes sadness, CDT says eat the apple. If the apple may be good or bad, CDT says to maximize the expected causal effect, weighted by one’s beliefs about the apple’s quality and by the utilities of the resulting experiences.

The classical formal statement, due to Allan Gibbard and William Harper, defines the causal expected utility of an action \(A\) by

\[
U_{\mathrm{CDT}}(A)=\sum_j P(A \,\Box\!\to\, O_j)\,D(O_j),
\]

where \(D(O_j)\) is the desirability or utility of outcome \(O_j\), and \(P(A \,\Box\!\to\, O_j)\) is the probability of the counterfactual: “if \(A\) were performed, \(O_j\) would obtain.” The source writes this as \(P(A\to O_j)\), but it is important that this is not an ordinary material conditional and not necessarily an ordinary conditional probability. David Lewis argued that the probability of a conditional generally does not equal the conditional probability \(P(O_j\mid A)\). If they always coincided, CDT would collapse into EDT. They do not.

EDT uses

\[
U_{\mathrm{EDT}}(A)=\sum_j P(O_j\mid A)\,D(O_j).
\]

The difference is that \(P(O_j\mid A)\) asks how strongly \(A\) predicts \(O_j\), while \(P(A\,\Box\!\to\,O_j)\) asks whether \(A\) would bring about \(O_j\). According to the source, Gibbard and Harper showed that under some logical assumptions, if the action \(A\) is statistically independent of the relevant counterfactuals, then the two calculations agree. But in many decision problems, actions and counterfactuals are not independent in the relevant way. The task of CDT is therefore to evaluate actions using probabilities that represent causal or counterfactual dependence, not mere evidential association.

The reference article emphasizes that philosophers often prefer CDT to EDT when forced to choose. It also emphasizes that CDT does not itself supply a complete algorithm for computing the counterfactual probabilities. That omission is the central technical open question. In what follows, I distinguish the source’s claims from an operational interpretation that I think makes CDT usable: identify counterfactual probabilities with interventional probabilities in a causal model.

---

## 2. A working formalization: interventions and dependency hypotheses

The source gives the Gibbard–Harper formula but does not specify how an agent should calculate \(P(A\,\Box\!\to\,O_j)\). It mentions Lewis’s “imaging” proposal: to evaluate the probability of an \(A\)-counterfactual, move probability mass from each possible world to the closest possible world where \(A\) is true. The source also notes that this invites a regress, because one must know what one would believe if one were certain of \(A\).

A more operational way to state CDT, and this is my own addition rather than a claim of the source, is to use the language of causal models and interventions. Let there be a set of possible actions \(\mathcal A\), outcomes \(\mathcal O\), and a utility function \(u:\mathcal O\to\mathbb R\). Suppose the agent has a causal model of the world. The model may be represented as a directed acyclic graph together with structural equations, or more informally as a set of “dependency hypotheses” describing how outcomes depend on actions and background states.

For an action \(a\), define the interventional probability

\[
P(O_j\mid do(a)),
\]

read as “the probability that \(O_j\) occurs if the agent intervenes to set the action variable to \(a\).” The \(do(\cdot)\) notation is not in the reference article, but it gives a natural mathematical interpretation of the counterfactual probability:

\[
P(A\,\Box\!\to\,O_j) \approx P(O_j\mid do(A)).
\]

Then CDT becomes the rule:

\[
U_{\mathrm{CDT}}(a)=\sum_j P(O_j\mid do(a))\,u(O_j),
\]

and the agent chooses

\[
a^*\in\arg\max_{a\in\mathcal A} U_{\mathrm{CDT}}(a).
\]

If the causal structure is uncertain, we can introduce a variable \(H\) indexing dependency hypotheses. A dependency hypothesis is a complete enough specification of the causal structure to determine, for each action, the probabilities of outcomes. The agent has a prior distribution \(P(H)\). Then a natural CDT formula is

\[
U_{\mathrm{CDT}}(a)
=
\sum_h P(H=h)
\sum_j P(O_j\mid do(a), H=h)\,u(O_j).
\]

This expresses a idea that the source attributes, via Andy Egan, to standard CDT: the agent holds fixed her unconditional credences in dependency hypotheses. She does not replace \(P(H)\) by \(P(H\mid a)\), because doing so would treat the action as evidence about the causal structure rather than as an intervention.

In a structural causal model, the intervention \(do(A=a)\) is made precise as follows. The world contains variables \(V_1,\dots,V_n\), with structural equations

\[
V_i=f_i(\mathrm{Pa}_i,U_i),
\]

where \(\mathrm{Pa}_i\) are the direct causes of \(V_i\) and \(U_i\) are exogenous noise variables. If \(A\) is one of the variables, then an intervention \(do(A=a)\) replaces the structural equation for \(A\) by the constant equation

\[
A:=a.
\]

All other structural equations remain unchanged. The post-intervention distribution over the remaining variables is then computed from the modified system. If the graph is Markovian and causal sufficiency holds, one can write the post-intervention distribution as a truncated factorization:

\[
P(v\mid do(a))
=
\mathbf 1\{v_A=a\}
\prod_{i:V_i\neq A}
P(v_i\mid \mathrm{pa}_i).
\]

The expected utility of \(a\) is obtained by summing utility over the resulting distribution.

This interventionist interpretation solves several explanatory problems. First, it distinguishes causal from evidential dependence. Second, it gives a clear recipe for computing CDT’s probabilities when a causal model is available. Third, it shows why CDT is not merely EDT with different words: conditioning on \(A\) changes the probabilities of variables that are evidentially correlated with \(A\), while intervening on \(A\) leaves upstream causes and background states distributionally unchanged, except insofar as they are causally downstream of the intervention.

However, this interpretation also makes clear what CDT does not do. It does not tell us which causal model to use. It does not, by itself, identify causal effects from observational data. If the causal graph is wrong, the CDT recommendation may be wrong. CDT is a decision rule relative to a causal representation.

---

## 3. Actions, policies, and the evaluation procedure

A simple CDT problem has a one-shot action set \(\mathcal A\). But many decisions concern policies: rules mapping observations or histories to actions. CDT can handle these by treating the implementation of a policy as the intervention.

Suppose a policy \(\pi\) maps an observation \(X\) to an action \(A=\pi(X)\). To evaluate \(\pi\), we do not merely ask what would happen if \(A\) had some fixed value. We ask what would happen if the policy variable were set to \(\pi\). Formally, we replace the structural equation for \(A\) by

\[
A:=\pi(X).
\]

Then

\[
U_{\mathrm{CDT}}(\pi)
=
\sum_j P(O_j\mid do(A:=\pi(X)))\,u(O_j).
\]

In sequential decisions, the policy may specify actions at many times:

\[
A_t=\pi_t(H_t),
\]

where \(H_t\) is the history available at time \(t\). Evaluating \(\pi\) means replacing each action equation by the policy’s rule. The expected utility is then computed over the resulting stochastic process. This is the natural policy-level version of CDT.

A practical procedure is:

1. **Specify feasible actions or policies.** The options must be things the agent can in principle intervene on. If an “action” is physically impossible or not under the agent’s control, it may not be a legitimate option.

2. **Specify the causal model.** Identify relevant variables: actions, states, predictions, observations, outcomes. Represent causal arrows and uncertainty. If the causal structure is uncertain, represent a prior over dependency hypotheses.

3. **Assign utilities.** Utilities should be assigned to final outcomes or consequence states, not merely to actions.

4. **Perform the intervention.** For each candidate action or policy, modify the causal model by setting the relevant action variables to the values or rules specified by the option.

5. **Compute the post-intervention outcome distribution.** Use the causal model to calculate \(P(O\mid do(a))\) or \(P(O\mid do(\pi))\).

6. **Maximize expected utility.** Choose the action or policy with the highest interventional expected utility.

This procedure clarifies how CDT treats dependencies. It does not ignore dependencies altogether. It ignores dependencies that are merely evidential. If an action causally affects an outcome through a chain

\[
A\to M\to O,
\]

then CDT includes that effect. If an action and an outcome are correlated because of a common cause

\[
A\leftarrow X\to O,
\]

then CDT does not treat the correlation as a reason to choose the action, unless the action also has a causal path to the outcome. The common cause \(X\) remains relevant to the expected utility calculation because it affects \(O\), but the agent does not update the distribution of \(X\) merely because of the action she is considering.

---

## 4. CDT versus EDT: King David and Newcomb’s problem

The source gives Gibbard and Harper’s example of King David. David wants Bathsheba but fears that summoning her will provoke revolt. He knows that kings are either charismatic or uncharismatic. Charismatic kings tend to act justly and rarely face successful revolts; uncharismatic kings tend to act unjustly and often face successful revolts. David does not know which type he is. Sending for another man’s wife is unjust, but unjust acts themselves do not cause revolt. Rather, uncharismatic kings have a disposition that both inclines them toward unjust acts and makes revolts likely.

Let

- \(C\) be David’s charisma,
- \(S\) be the action of summoning Bathsheba,
- \(R\) be a successful revolt.

The causal structure suggested by the example is roughly:

\[
C\to S,\qquad C\to R,
\]

with no direct causal arrow \(S\to R\). EDT conditions on \(S\). If David summons Bathsheba, that is evidence that he is uncharismatic, and therefore evidence of revolt:

\[
P(R\mid S)\ \text{is high}.
\]

So EDT recommends abstaining.

CDT instead computes

\[
P(R\mid do(S)).
\]

If summoning does not causally affect revolt, then

\[
P(R\mid do(S))
=
\sum_c P(c)P(R\mid C=c).
\]

This is just the prior probability of revolt, averaged over charisma types. Since David cannot change his charisma by acting, and since the act itself does not cause revolt, CDT does not treat the act as bad news about revolt. If the direct benefit of summoning Bathsheba is positive, CDT recommends summoning her. The example illustrates the central CDT idea: an action’s being evidence of a bad state is not, by itself, a causal reason against the action.

Newcomb’s problem is the most famous test case. The source describes the standard setup. A predictor has predicted whether the player will take only box B or both boxes. Box A contains \$1,000. Box B contains \$1,000,000 if the predictor predicted one-boxing, and nothing if the predictor predicted two-boxing. The predictor is highly reliable.

Let \(B\) denote the amount in box B. Let the actions be:

- \(O\): take only box B,
- \(T\): take both boxes.

The payoffs are:

\[
\text{Payoff}(O)=B,
\]

\[
\text{Payoff}(T)=B+1000.
\]

CDT reasons that the predictor has already made the prediction, so the current action does not causally affect \(B\). In intervention notation,

\[
P(B\mid do(O))=P(B\mid do(T)).
\]

Therefore,

\[
U_{\mathrm{CDT}}(T)
=
\mathbb E[B\mid do(T)]+1000
=
\mathbb E[B\mid do(O)]+1000
=
U_{\mathrm{CDT}}(O)+1000.
\]

So CDT recommends two-boxing.

EDT reasons differently. Taking only box B is strong evidence that the predictor predicted one-boxing, so

\[
P(B=1{,}000{,}000\mid O)
\]

is high, while

\[
P(B=1{,}000{,}000\mid T)
\]

is low. Therefore EDT recommends one-boxing.

The source says CDT recommends two-boxing because the player’s present action does not affect the predictor’s already-made prediction. That is correct given the usual causal interpretation. But it is worth adding a qualification: CDT’s answer depends on the causal model. If the predictor’s prediction is caused by the agent’s future choice through backward causation, or if the predictor runs a perfect simulation whose output is causally linked to the agent’s actual decision process, then the causal graph may contain a path from the action to the prediction. In that case, CDT might recommend one-boxing. CDT is not simply “ignore correlations”; it is “evaluate consequences under the correct intervention.”

---

## 5. Counterfactuals, imaging, and the open computational problem

The source correctly notes that CDT is vague about how to compute counterfactual probabilities. Lewis’s imaging proposal says: to evaluate \(P(A\,\Box\!\to\,O)\), move probability mass from each world \(w\) to the closest world \(w_A\) in which \(A\) is true. This captures the intuitive idea of “consider the nearest possible world where the action is performed.” But the source also notes a regress: to know what one would believe if certain of \(A\), one may need further conditional beliefs, which themselves may be uncertain.

The interventionist interpretation avoids some of this regress by replacing “closest world” with an explicit causal operation: set the action variable to \(a\), leave other causal mechanisms fixed, and compute the resulting distribution. But this does not eliminate all difficulty. One still needs a causal model, and in some cases the correct model is contestable. The question “what would happen if I did \(A\)?” may depend on which background facts are held fixed. CDT needs a theory of legitimate interventions.

I propose the following operational constraint. An intervention should hold fixed all variables that are not causal descendants of the intervened variable, except where the model explicitly says they change as downstream effects. In particular, variables representing the agent’s past, fixed traits, prior predictions, and already settled states should be held fixed unless the action causally changes them. This is not a mere assumption of independence; it is a consequence of treating the action as an intervention in a causal system.

This proposal is reasonable because it separates two roles an action can play:

1. **As news:** the action provides evidence about hidden states, traits, or causal structure.
2. **As control:** the action changes the world.

CDT focuses on the second role. If an action is good news but does not cause good outcomes, CDT refuses to choose it for that reason alone.

---

## 6. Counterexamples and unstable cases

The source discusses several alleged counterexamples. They are useful because they show where CDT’s treatment of self-predictive correlations becomes controversial.

### Death in Damascus

In the Death in Damascus scenario, Death predicts where you will be tomorrow and waits there. If Death is a reliable predictor, then whichever location you choose seems likely to be the location where Death waits. The source says a CDT agent may be unable to process the correlation and may make irrational decisions.

In interventionist terms, suppose Death’s prediction \(D\) is made before your location choice \(L\), and there is no causal arrow from \(L\) to \(D\). Then

\[
P(D\mid do(L=\text{Damascus}))=P(D),
\]

\[
P(D\mid do(L=\text{Aleppo}))=P(D).
\]

CDT evaluates locations using the prior distribution over Death’s prediction. If the prior is symmetric, CDT may be indifferent. But EDT notes that choosing Aleppo is evidence that Death predicted Aleppo, and choosing Damascus is evidence that Death predicted Damascus. The correlation is strong, but CDT does not treat it as causal.

One possible CDT response, not emphasized in the source, is to evaluate randomized policies. If Death cannot predict the outcome of a genuinely random choice, then a randomized policy may have better causal expected utility. But if Death can predict the randomization device or the agent’s disposition to randomize, then the causal model must include that, and the advantage may disappear. The deeper problem is that CDT’s answer is sensitive to how prediction, deliberation, and randomness are represented.

### The psychopath button

The source gives Andy Egan’s psychopath button example. Paul can press a button that kills all psychopaths. Paul thinks a world without psychopaths is much better, but he is confident that only a psychopath would press the button. He prefers living with psychopaths to dying.

Let \(T\) be the proposition that Paul is a psychopath, with prior probability \(p\). Let \(K\) be the action of pressing the button. Suppose pressing the button kills all psychopaths, including Paul if \(T\) is true. Let the relevant utilities be:

\[
u_N = \text{utility of living with no psychopaths},
\]

\[
u_P = \text{utility of living with psychopaths},
\]

\[
u_D = \text{utility of dying},
\]

with

\[
u_N > u_P > u_D.
\]

CDT, holding fixed Paul’s prior probability \(p\) of being a psychopath, gives

\[
U_{\mathrm{CDT}}(K)
=
(1-p)u_N + p u_D,
\]

while

\[
U_{\mathrm{CDT}}(\neg K)=u_P.
\]

CDT recommends pressing if

\[
(1-p)(u_N-u_P) > p(u_P-u_D).
\]

If \(p\) is small enough, CDT presses. But intuitively, if Paul is confident that only a psychopath would press, then the fact that he presses is strong evidence that \(T\) is true. EDT would use \(P(T\mid K)\), not \(P(T)\), and would likely recommend not pressing.

The source says CDT endorses pressing, and that this is widely regarded as implausible. The example exposes a tension in CDT’s treatment of actions that are strongly diagnostic of stable traits. My own view is that CDT can respond in two ways, though neither is completely uncontroversial.

First, if the action is genuinely available to Paul regardless of his psychopathy status, then CDT’s interventionist calculation is defensible: if Paul could somehow press the button while not being a psychopath, the outcome would be good. The fact that he probably would not press unless he is a psychopath is evidential, not causal.

Second, if being a psychopath makes pressing practically inevitable and not being a psychopath makes pressing practically impossible, one might question whether “pressing” is a coherent option for the non-psychopath version of Paul. A refined CDT could restrict admissible actions to interventions that are compatible with the agent’s actual causal capacities. This is my proposal, not a claim of the source. But if we impose such a restriction too aggressively, we risk collapsing CDT into EDT, because the agent’s evidence about her own type will determine which actions count as available.

### The adversarial offer

The source also mentions the adversarial offer. Two boxes are offered. The buyer may buy one or none, but not both. Each box costs \$1. The seller put \$3 in each box that she predicted the buyer would not acquire. The seller’s prediction is accurate with probability \(0.75\). The source says CDT reasons that at least one box contains \$3, so the average box contains at least \$1.50 in expected value, which exceeds the \$1 cost. Hence CDT buys a box. But this is profitable for the seller, because the buyer tends to choose the box predicted to be empty.

This is another case where CDT treats the buyer’s choice as not causally affecting the box contents, while the seller’s prediction is correlated with the buyer’s choice. CDT sees buying a box as having positive causal expected value, because the contents are already fixed. Yet the buyer is systematically exploited because the prediction is reliable. The source cites this as evidence that CDT can voluntarily lose money and may be subject to Dutch-book-like criticisms.

A defender of CDT might reply that the problem is not CDT but an incomplete causal model. If the buyer knows the seller is adversarial and highly accurate, perhaps the buyer should evaluate a policy of not buying, or of randomizing in a way the seller cannot predict. Still, the example shows that CDT’s local act-evaluation can be vulnerable when the agent’s choice is predictable but not causally efficacious with respect to the payoff structure.

---

## 7. What CDT gets right, and where it remains uncertain

CDT captures an important normative idea: rational choice should be guided by what actions bring about, not merely by what actions signify. This is especially compelling in cases like King David, where an action is correlated with a bad outcome only because both are effects of a common cause. It is also compelling in many ordinary decisions: taking an umbrella is rational if it causally prevents getting wet, not merely because umbrella-taking is correlated with rain.

The theory also has a clean mathematical core when formulated interventionally:

\[
\text{Choose } a \text{ maximizing } \mathbb E[u(O)\mid do(a)].
\]

For policies:

\[
\text{Choose } \pi \text{ maximizing } \mathbb E[u(O)\mid do(\pi)].
\]

This formulation makes CDT applicable to unfamiliar cases. One asks: what causal model should I accept? Which variables are under my control? What happens to the outcome distribution if I intervene on the action variable? Which policy has the highest interventional expected utility?

The remaining uncertainty concerns the source’s main open question: how to determine the counterfactual probabilities when the agent’s action is itself evidence about hidden states, predictions, or dependency hypotheses. The reference article says CDT does not specify the algorithm. Lewis’s imaging is one proposal, but it is vulnerable to regress. My proposed operational interpretation uses causal models and interventions, but it transfers the difficulty to the choice of causal model and to the legitimacy of interventions on self-diagnostic actions.

A reasonable operational stance, which I propose rather than find in the source, is this:

- Use the agent’s prior over causal structures and background states when evaluating an action.
- Do not condition the prior on the action being evaluated, except where the action is itself an observation already available before the decision.
- Evaluate policies from the perspective at which the policy is adopted.
- Treat self-predictive correlations as part of the causal model, not as reasons to condition away the intervention.
- Be cautious about options that are not credible interventions given the agent’s known psychology.

This stance preserves CDT’s distinctive idea while giving it enough structure to be used. It also explains why CDT can appear both attractive and fragile. It is attractive because it avoids choosing actions merely for their good news. It is fragile because in problems involving highly accurate predictors, self-knowledge, or deliberative transparency, the line between causal control and evidential news becomes hard to draw.

---

## 8. Conclusion

Causal decision theory says that rational choice should maximize expected utility computed from counterfactual or causal probabilities, not ordinary conditional probabilities. The reference article presents this through Gibbard and Harper’s formula, contrasts CDT with EDT, and illustrates the difference with King David and Newcomb’s problem. The central difficulty, also noted in the source, is that CDT does not by itself specify how to compute the relevant counterfactual probabilities.

A natural and powerful way to complete the theory is to interpret those probabilities as interventional probabilities: \(P(A\,\Box\!\to\,O)\) becomes \(P(O\mid do(A))\). With this interpretation, CDT becomes a rule for choosing actions or policies that maximize expected utility under interventions in a causal model. This gives a precise procedure for many decision problems and clarifies how CDT treats dependencies: causal dependencies matter, evidential dependencies do not.

The hard cases arise when an action is strong evidence about the agent’s type, the predictor’s prediction, or the correct dependency hypothesis. In those cases, CDT’s insistence on holding fixed prior beliefs can produce recommendations that seem counterintuitive or exploitable. The theory therefore remains philosophically contested. But as a formal decision procedure, its core commitment is clear: choose what would causally bring about the best outcome, not what would merely be good to learn you had chosen.

---

## References

Wikipedia contributors, “Causal Decision Theory,” revision 1381555528, 2026. Source text supplied for this essay.

Allan Gibbard and William L. Harper, “Counterfactuals and Two Kinds of Expected Utility,” 1981.

David Lewis, “Causal Decision Theory,” 1981.

Andy Egan, “Some Counterexamples to Causal Decision Theory,” 2007.

Judea Pearl, *Causality*, 2009. Additional reference for the interventionist formulation used here.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request. Need produce final essay approx 2400-3000 words, substantive mathematical essay on CDT and applying to decision problems, based on supplied Wikipedia source, but can add own assumptions/proposals and distinguish. Need likely include definitions, equations, examples, dependencies, counterfactuals, open questions, operational interpretation. Need maybe cite source briefly. Need no unnecessary bibliography. Need around 2400-3000 words. Need likely write in English. Need be coherent, precise enough reader could use essay to decide unfamiliar cases. Need explain evaluating alternative actions/policies, dependencies/counterfactuals. Source leaves important question open: how calculate counterfactual probabilities; algorithm unspecified. Need explain uncertainty and develop operational interpretation if available. Need distinguish source claims vs own assumptions.

Need think content. CDT: choose action maximizing expected utility using counterfactual probabilities P(A □→ O_j) or P(A -> O_j) (source uses A -> O_j; says probability of counterfactual that A necessarily implies O_j; maybe better use intervention do(A) notation. Need formal: set of actions A, outcomes O, dependency hypotheses K or causal states. CDT expected utility: U_CDT(a)=Σ_o P(O=o | do(a)) u(o), or Σ_k P(k) Σ_o P(o | do(a), k) u(o). If dependency hypotheses partition causal structure and are act-independent? Need explain holding fixed unconditional credences in dependency hypotheses. In Newcomb, predictor as common cause? CDT two-box because do(take both) doesn't change box content given causal model; correlation is evidential. EDT uses P(o|a). Difference: P(O|do(A)) vs P(O|A). Need include Gibbard Harper formula, Lewis probability of conditional not conditional probability. Could discuss imaging: move mass to closest A-worlds. Need operational interpretation: use causal Bayesian networks / structural causal models and do-operator; define counterfactual probabilities via interventions. This is additional proposal not in source. Need justify: gives algorithm, handles DAGs, exogenous variables, policies. Need mention limitations: causal model uncertainty, cycles, preemption, policies not single actions, self-locating? Need perhaps present procedure:

1. List actions (mutually exclusive interventions) and outcomes.
2. Specify causal model: variables, DAG, structural equations or conditional probabilities, exogenous uncertainty. Include dependency hypotheses if structure uncertain.
3. For each action a, perform intervention do(A=a): replace equation for A with constant a; leave other causal mechanisms unchanged. If action is policy, set policy variables accordingly.
4. Compute post-intervention distribution P(o | do(a)) by summing over exogenous/background states or using truncated factorization: P(v | do(a)) = ∏_{X≠A} P(x | pa_X) with A fixed.
5. Expected utility: EU(a)=Σ_v u(v) P(v | do(a)) (or outcome distribution). Choose max. For policies, evaluate do(policy) maybe dynamic: policy as function from observations to actions; intervene on policy node or compute sequential value via dynamic programming under interventions.

Need explain dependencies: common causes, confounders. CDT does not ignore all dependence; it distinguishes causal dependence from evidential dependence. If action causes outcome through paths, included. If outcome depends on action via causal chain, included. If action correlated with outcome due to common cause, holding common cause fixed, action has no effect; CDT may not use correlation as reason. Need explain relevant dependencies: if action is evidence of causal structure? CDT typically holds fixed unconditional credences in dependency hypotheses; if actions provide evidence about which dependency hypothesis obtains (e.g. Newcomb? maybe not dependency hypotheses? predictor's accuracy? common cause? Egan says holds fixed unconditional credences). Need nuance: In standard causal model, variables may include predictor's prediction as caused by common cause/person's disposition? If do(two-box) may affect prediction if there is causal path from action? In Newcomb if predictor predicts before action but via perfect simulation? Need CDT says no backward causation; do(two-box) doesn't change content. But if causal model includes backward causation or predictor uses simulation of actual decision? CDT's answer depends on model. Need mention source says at moment predictor already made prediction; action will not affect outcome. But if prediction caused by action via backward causation? CDT would one-box if causal arrow. So CDT isn't just ignore correlations; it requires causal model.

Need discuss counterfactuals: probability of A □→ O. Lewis imaging: shift mass to closest A-worlds. Need note regress/vagueness. Need propose SCM interpretation: P(A □→ O) = P(O_{A}=o) where O_A is potential outcome under intervention; for actual world with exogenous U, counterfactual P could be defined by distribution over U. If action not possible? assign zero? Need handle uncertainty about model: mixture over dependency hypotheses: EU(a)=Σ_h P(h) EU(a|h). If action gives evidence about h? Standard CDT holds P(h) fixed; but if action itself reveals h? Need perhaps propose partition? Source: Gibbard & Harper axioms statistical independence of A and A->O_j suffices equality; cases not independent (David). Need explain David example: charisma common cause of action (maybe propensity to summon?) and revolt; CDT says send for Bathsheba because act doesn't change charisma and unjust acts don't cause revolt. EDT says abstain because summoning evidence of uncharismatic, revolt likely. Need compute maybe simple numeric? Could illustrate.

Need examples: apple/orange simple; David; Newcomb; Death in Damascus; Psychopath Button; Adversarial Offer? Need not cover all but use to illustrate. Need target 2400-3000 words. Need include equations. Need maybe mention policies: decision rules. For policies, evaluate expected utility of implementing policy π. In causal models with observations, policy maps observations to actions; intervention sets action variables as functions of observation variables? Need use do(π) or do(A=π(X))? In sequential decisions, if action at time t depends on observations, intervention replaces structural equations for action variables by policy. Need distinguish evaluating actions vs policies. Need mention if policy correlated with hidden types, CDT holds hidden type fixed unless policy causally changes it. But in cases where choosing policy reveals type? E.g. psychopath button: pressing button is evidence Paul is psychopath, but pressing doesn't cause psychopathy. CDT with fixed psychopathy variable: if press, kills all psychopaths including Paul if psychopath? Need expected utility. Let's formalize: P(Paul psychopath)=p? Utilities: world no psychopaths and alive? better than psychopaths alive? strongly prefers living with psychopaths to dying. If he presses, if psychopath, he dies (all psychopaths killed). If not psychopath, world without psychopaths (except him?) and alive. If not press, status quo living with psychopaths. CDT expected utility: U(press)= (1-p)U(no psycho alive)+p U(dead). U(not)=U(live with psycho). If p small enough and benefit large, CDT press. But intuitively no because high confidence only psychopath would press means p near 1 conditional on pressing? CDT doesn't update p based on action? It uses unconditional p? Or should it use dependency hypotheses incl dispositions? Egan's critique. Need explain source says CDT endorses pressing. But is that source's claim; yes. Need maybe operational response: If agent's choice is caused by psychopathy (disposition), then intervention do(press) may be impossible independent of psychopathy? Actually if psychopathy causes press, intervention setting press=true while holding psychopathy fixed can create inconsistency? In SCM, intervention can set variable to value contrary to parents; allowed. But if action is not freely assignable because it is deterministic function of psychopathy, CDT still considers intervention? This is controversial. Need discuss agency assumption: actions must be exogenous interventions relative to relevant variables; if action is strong evidence of unchangeable type, CDT still evaluates intervention. Some propose ratification or conditional CDT? Need maybe source mentions Joyce argues CDT can take evidence about inclinations. Need include.

Need mention Dutch books, money pump? Source says Oesterheld & Conitzer argue CDT voluntarily lose money and diachronic Dutch books. Could mention as criticisms but not deep.

Need perhaps include mathematical formalization with potential outcomes: Let A∈𝒜, outcomes Y, pre-action covariates X, hidden variables U. CDT uses interventional distribution P(Y | do(A=a)). If causal sufficiency and DAG: P(y|do(a))=Σ_x P(y|a,x)P(x) if backdoor adjusted? Actually if A has parents confounders X causing A and Y, observational P(y|a) confounded; interventional is Σ_x P(y|a,x)P(x) if no unmeasured confounding. CDT can use this. But in Newcomb, predictor variable P is prior? If box content C is parent? Need graph: Type/disposition -> choice and prediction; prediction -> box content. Choice not parent of box content. Then P(C | do(A))=P(C) if no path? But if C depends on prediction which depends on disposition, and disposition also choice, intervention on choice breaks link from disposition to choice; P(C) maybe unchanged? More precise: Graph: D -> A, D -> Pred, Pred -> B. Under do(A=a), D distribution remains P(D), Pred remains P(Pred|D), B remains P(B|Pred). Thus B independent of do(A). EU(two-box)=P(B full)*1,001,000? Wait if B full independent? If predictor reliable, P(B full) high if one-box disposition? But unconditional distribution of B maybe high/low depending prior on D. Two-box EU = P(B full)*1,001,000 + (1-P(B full))*1,000? One-box EU = P(B full)*1,000,000. Difference: two-box = one-box + 1000 if same P(B full). So two-box better. This is classic dominance? If B fixed, two-box dominates one-box by $1000. Need mention.

But EDT: P(B full | A=one-box) high, P(B full | A=two-box) low, so one-box. Need maybe compute with p=0.99 predictor accuracy, prior? If 50/50? For EDT: EU(one)=0.99*1M? two=0.01*1M+1000? Need CDT: if P(B full)=q maybe q=0.5? EU two = q*1,001,000+(1-q)*1,000 = 1000+1,000,000q, EU one=1,000,000q. two by 1000. Good.

Need maybe Death in Damascus: Death predicts location; if you stay/ flee. CDT sees no causal effect of choice on Death's prediction (if prediction prior), but if Death will be where predicted, each action maybe equal? In source: CDT agent unable to process correlation and may make irrational decisions. Need illustrate: If Death reliable, fleeing causes? Actually if Death predicts you'll flee, he waits in Damascus? Wait story: Death in Damascus: man sees Death in Damascus, flees to Aleppo, Death says appointment tomorrow in Aleppo. If Death predicts where you'll be and goes there. If CDT evaluates do(flee) vs do(stay), with Death's location determined by prediction, but prediction not caused by action? However if prediction is reliable, action correlates. CDT may assign equal probabilities or choose based on prior; no benefit. EDT says choose unpredictably? Need maybe mention if Death's prediction is caused by your decision (via simulation) then CDT would model differently. The source says CDT unable to process correlation. Need present as criticism.

Need discuss dependency hypotheses and ratifiability? Source mentions Egan: hold fixed unconditional credences in dependency hypotheses. Need define dependency hypothesis: complete specification of how outcomes depend on actions. In Newcomb, dependency hypotheses might say if one-box then B contains million, if two-box then B empty? Wait if dependency hypothesis includes predictor's accuracy? If outcome depends on action via predictor? Egan's point: CDT uses unconditional credences in dependency hypotheses, not updated on action. If action provides evidence about dependency hypothesis, CDT ignores. Example Death in Damascus: dependency hypothesis: Death predicts flee/stay. Your choice evidentially indicates hypothesis. CDT uses prior. Could lead to instability. Need mention.

Need develop operational interpretation: I propose CDT as causal Bayesian decision rule: choose action/policy maximizing expected utility under intervention. If causal structure uncertain, represent with a set/mixture of causal graphs or structural models. But crucial question: should we hold fixed prior probabilities of latent variables and causal structures, or update on the fact that we are performing action? The source says CDT does not specify algorithm; Gibbard/Harper imaging maybe. I propose a constrained operationalization:

- Use a causal model in which the decision variable A is exogenous at the moment of intervention: all pre-decision variables are parents of A but not descendants; intervention replaces A's structural equation.
- For uncertain structures, take a prior over models H. When evaluating an action, use the prior P(H), not P(H|A), unless A is also an observation generated before decision? Justification: decision is intervention, not evidence; using P(H|A) would conflate news value with causal efficacy. However, if the agent has pre-existing evidence about H available before choice, that evidence should already be conditioned on. Also if action is part of a policy and observations after action inform future actions, update normally on observed outcomes in future steps, but at the moment of evaluating initial intervention, use pre-intervention beliefs about exogenous state. This is my proposal.

Need address cases where action reveals stable traits: The model should include trait T prior to action. If action is caused by T, then do(A=a) sets A contrary to T's tendency. CDT evaluates what would happen if the agent managed to perform a, holding T fixed. If the agent cannot actually perform a unless T has certain value, the action may not be a feasible intervention. A reasonable operational requirement: only evaluate actions that are possible under some admissible intervention, i.e. there is positive probability of A=a under do? Hmm intervention can force any value; but if action is physically impossible for type, perhaps structural equation constraints make do invalid. Could restrict to feasible interventions: if P(A=a | T=t)=0 for all t? But in deterministic psychopathy case, non-psychopath might have zero probability of pressing? If only a psychopath would press, P(A=press | not psychopath)=0. Does CDT still evaluate do(press) with not psychopath? If intervention can force non-psychopath to press, it is counterfactual impossible but intervention semantics allows breaking structural equation. But if action availability depends on type, maybe action not a genuine option for non-psychopath. The decision problem says Paul debating; if he isn't psychopath? He doesn't know. The option press is physically available. CDT intervention can set press even if unlikely. So CDT press if unconditional p low enough. But intuitive objection says if he presses, that is strong evidence he is psychopath, so he should not. To handle this, one can add a feasibility or ratifiability condition: an action is admissible only if the agent can rationally regard the intervention as compatible with enough probability of favorable hidden states, or evaluate using a conditional intervention P(T | do(A=a))? That collapses to EDT? Hmm.

Need maybe propose "policy-level CDT" to avoid some counterexamples: Instead of evaluating isolated action as intervention, evaluate policy of decision-making. In psychopath button, policy "press if and only if not a psychopath"? Cannot condition on unknown psychopathy. If policy is chosen before knowing type? If policy choice is also evidence? Infinite regress. But maybe CDT at policy level can precommit to not press because a policy of pressing is bad? But if policy variable influences action and is correlated with psychopathy? Not clear. Need not solve fully; explain uncertainty.

Need include equations for EDT comparison: EDT U_E(A)=Σ_j P(O_j | A) D(O_j). CDT uses P(A □→ O_j). If P(A□→O)=P(O|A) under independence axioms, they agree. Need mention Lewis triviality result? Source says probability of conditional not always conditional probability; could mention no need deep. Need maybe define counterfactual probability: P(A □→ O) = Σ_w P(w) I[closest A-world(w) satisfies O] (imaging). Need explain imaging regress. Then SCM alternative.

Need maybe include "decision problems with policies" more. Let's design essay structure:

Title: Causal Decision Theory: A Working Formalization

1. Introduction: what CDT says, contrast EDT; central idea choose action with best expected causal consequences. Source claim.

2. Basic formalism: finite actions A, outcomes O, desirability D/utility. Gibbard-Harper formula:
U_CDT(a)=Σ_o P(a □→ o) D(o). Define counterfactual probability. EDT formula.
If conditional probability equals counterfactual, CDT=EDT. Independence condition.

3. Causal models and intervention: my operationalization. Variables V, DAG, structural equations. Action A as variable; intervention do(A=a). Then P(a □→ o) := P(O=o | do(A=a)). Expected utility:
U(a)=Σ_o P(o | do(a)) u(o). With uncertainty over states S:
U(a)=Σ_s P(s) Σ_o P(o | do(a), s) u(o) maybe if S exogenous. More generally truncated factorization:
P(v | do(a)) = ∏_{X_i ≠ A} P(x_i | pa_i) with A=a. If unobserved variables, sum. If multiple dependency hypotheses H:
U(a)=Σ_h P(h) Σ_o P(o | do(a), h) u(o). Source's "holding fixed unconditional credences in dependency hypotheses" (Egan) captured. Need note source didn't specify SCM; my addition.

4. How to apply: procedural recipe (numbered). Include policy evaluation. Policies: π maps info to actions. Introduce policy node Π or replace action equations with π. U(π)=Σ_o P(o | do(π)) u(o). For sequential: dynamic programming under do. Distinguish act vs policy.

5. Dependencies and counterfactuals: causal vs evidential. Example with common cause. Use David/Bathsheba. Formal variables C charisma, S summon, R revolt. Graph C->S? C->R, maybe S not cause R. EDT uses P(R|S), CDT uses P(R|do(S))=P(R). Since C fixed, sending doesn't change revolt risk except maybe direct effect zero; if desire benefit positive, CDT summon. Need explain. This illustrates relevant dependency: common cause creates correlation, not causal reason.

6. Newcomb's problem: define graph D disposition -> prediction and choice; prediction -> box. Or predictor already set. CDT do(two-box) leaves box distribution fixed, so two-box dominates by $1000. Equations. EDT one-box. Need note if model includes backward causation or predictor's prediction caused by actual future action, CDT could one-box; theory is model-relative. Source says two-box because prediction already made; my note.

7. Criticisms/open cases: Death in Damascus, psychopath button, adversarial offer. Explain CDT's problem: actions are evidence for states/predictions but do not cause them; CDT holds prior. In Death in Damascus, if Death's prediction is reliable and independent, CDT can't exploit correlation; may choose arbitrary or lose. In psychopath button, formal calculation. In adversarial offer, CDT buys because expected causal value of a box > cost given seller predicted not acquire; but seller profits. Need mention source claims. Need perhaps use one or two examples in detail. Could include Adversarial Offer equation: Each box costs 1, contains 3 if seller predicted not acquire with prob .75. If buyer picks box i, P(box i contains 3 | do(buy i))? Seller predicted buyer not acquire i with prob .75? But source says CDT reasons at least one box contains $3; average box at least $1.50. Wait if seller predicts for each box independently? Accurate with prob 0.75? Need be careful. If two boxes, seller put $3 in each box she predicted buyer not to acquire. Buyer can buy one or none. Both believe prediction accurate probability .75. CDT: for each box, if buy it, probability it contains $3? If seller's prediction about that box: if buyer will not acquire. If prediction accurate .75, then P(contains $3 | do(buy)) = P(predicted not buy | do(buy)). If predictor accuracy: P(predicted not buy | buy) maybe? Under do(buy), predictor prior? If accuracy .75 unconditional? Then probability predicted not buy maybe .25? Hmm source says CDT reasons at least one box contains $3; average box at least $1.50. Let's not over-detail; mention qualitatively. But if I include equation, need correct. Let's think: Seller predicted whether buyer will acquire each box? Buyer may buy one or none, not both. For each box, seller puts $3 if predicted buyer not acquire it. If prediction accurate with probability .75. Buyer's CDT sees: if he buys box 1, the prediction about box 1 is already made; buying doesn't change it. What is P(box1 contains $3 | do(buy box1))? It equals P(seller predicted not buy box1). If seller's prediction accuracy overall .75 and maybe buyer expected to buy one? If if he buys one, for chosen box, predicted not buy maybe high? Source says at least one box contains $3 because two predictions cannot both be "acquire"? Since buyer cannot buy both. If seller knows buyer will buy at most one, she predicts at least one not acquired with certainty? If predictions accurate .75, expected total money in boxes at least $3? average at least $1.50. Thus buying one expected > cost $1. But seller predicted which one not buy, so the one buyer buys likely empty; seller gains. This is subtle. Could just quote source and not formalize too much.

Need discuss "vagueness" and operational interpretation. Source says CDT doesn't specify algorithm; imaging and regress. My proposal: causal Bayes net / SCM. Need justify: gives clear counterfactuals, avoids regress by specifying closest? But requires causal model. Could mention if only observational data, need identify causal effect; if unmeasured confounding, cannot compute exactly; use dependency hypotheses. CDT itself not a statistical method; it needs causal input.

Need maybe define counterfactual probability via potential outcomes: For each background state u, outcome under action a is O_a(u). Then P(O_a=o)=Σ_{u:O_a(u)=o}P(u). This is intuitive. If uncertainty over causal laws H: P(O_a=o)=Σ_h P(h)P_h(O_a=o). The agent should not condition P(h) on a because a is chosen. Need maybe discuss "policy" as function: For each state u and observation x, action π(x); outcome O_π(u). EU=Σ_u P(u) u(O_π(u)). This may be simpler.

Need handle "relevant dependencies and counterfactuals": relevant dependencies are those that survive intervention. If variable X is ancestor of outcome and action affects X, relevant. If X is common cause of action and outcome, correlation is irrelevant once intervening, unless action changes X? Actually if action is caused by X, intervening on action breaks arrow X->A, so X no longer influences A but still influences outcome; distribution of X unchanged. So expected outcome under action is average over X. If action is evidence about X, EDT conditions on action and changes X distribution; CDT doesn't. Need explain.

Need mention "conditional excluded middle" maybe? Source says Gibbard/Harper axioms; maybe mention only briefly: under certain logical assumptions and statistical independence of action and counterfactual, CDT reduces to EDT. Need not deep.

Need maybe mention "ratifiability"? Could be useful: Some CDT responses require agent to ratify choice after making it? Source mentions Harper ratifiability in refs. But not in main source. Could mention as possible refinement but not central. Need be careful not overdo. Target 2400-3000. Need maybe word count? I can aim ~2600. Need include references? They said including references; brief references to source and maybe key works. Could include small reference list: Wikipedia source, Gibbard & Harper, Lewis, Pearl maybe (own addition). But avoid lengthy bibliography. Need maybe cite within text: (source) vs my addition. Need distinguish claims. Could use phrases: "The reference article states...", "I will add...", "This is not in the source but is a natural operationalization." Need satisfy request.

Need plan word count. Let's outline sections with rough words:

Title & intro 200
1. Core idea and formula 350
2. Interventional reformulation (own) 600
3. Procedure and policies 450
4. Examples: David, Newcomb 600
5. Criticisms/open questions (Death, psychopath, adversarial) 500
6. Conclusion 150
References 100
Total ~2950. Need maybe shorter ~2700. Need ensure not too long.

Need write mathematical definitions. Use LaTeX-like. Need maybe define actions and policies.

Detailed content:

Intro:
- CDT is a school in decision theory: rational agent selects action that causes best outcome in expectation. Source. EDT selects action that would be evidence of best outcome. CDT's motto: don't treat news as control.
- Essay aim: provide operational account.

Core formula:
- Let 𝒜 finite set, 𝒪 outcomes, D:𝒪→ℝ desirability. EDT: U_E(a)=Σ_o P(o|a)D(o). CDT Gibbard-Harper: U_C(a)=Σ_o P(a □→ o)D(o). The arrow/box is counterfactual: probability that if a were performed, o would obtain. Source uses P(A→O_j), but note not material conditional. Lewis: probability of conditional not generally conditional probability; if equal, theories coincide. Independence condition: if A statistically independent of counterfactual A→O, then equality under axioms (source). In many problems not independent.

Need maybe clarify P(a □→ o) not "necessarily implies" maybe probability that counterfactual holds. Source says probability of it being case that A necessarily implies O_j. I can phrase: probability of counterfactual "if A were performed, O_j would obtain." Need not use necessarily.

Interventional reformulation:
- The source leaves computation open. I propose identify P(a□→o) with interventional probability P(o | do(a)) in structural causal model (Pearl). This is additional. Define SCM: variables V=(V1,...,Vn), DAG, structural equations Vi=f_i(PA_i,U_i), exogenous U with distribution. Action A is a variable that agent can set. Intervention do(A=a) replaces equation A=f_A(...) by A=a. Post-intervention distribution: P(v | do(a))=∏_{i:V_i≠A}P(v_i | pa_i) 1_{A=a}. Expected utility: U_C(a)=Σ_v u(v)P(v|do(a)) = Σ_o P(o|do(a))D(o). Equivalent to potential outcomes: O_a(u), U(a)=E[D(O_a)].
- If uncertain about model H: set of SCMs with prior P(H=h). Then U(a)=Σ_h P(h)U_h(a). This formalizes Egan's "holding fixed unconditional credences in dependency hypotheses." The prior is pre-intervention; do not replace by P(h|a), except if evidence was already available independent of chosen act. This is my proposal. Justification: an action is not an observation of H; conditioning on it would import evidential dependence. However, if H concerns agent's future choice process and action is not freely set? Need discuss later.
- If causal graph unknown or nonparametric, CDT requires causal judgments. Observational data alone may not identify P(o|do(a)). If confounders measured, use adjustment: P(o|do(a))=Σ_x P(o|a,x)P(x) when X blocks backdoor paths. This gives practical method.

Procedure:
1. Specify options as feasible interventions. If options are policies, define policy variable.
2. Specify causal model / dependency hypotheses, utilities.
3. For each option, perform intervention and compute distribution.
4. Maximize.
Policies: Let π map observed variables X to action A=π(X). Evaluate do(Π=π) or replace structural equations for A_t by π_t(history). U(π)=Σ_o P(o|do(π))D(o). In sequential problems, use dynamic programming: value V(s)=max_a E[V(s')|do(a),s] but under causal transition. Need mention evaluating policies not just one-shot acts can change answer when the policy itself has causal consequences or determines future observations.

Dependencies and counterfactuals:
- CDT tracks causal paths. If A→M→O, effect included. If A←X→O, correlation ignored for choice (though X affects expected utility via prior). If A→O and A correlated with X? Need perhaps table.
- Counterfactual: closest world? Source imaging. Imaging: move mass from each world w to closest A-world. Problem regress. SCM avoids by explicit intervention, but still needs model and possibly counterfactuals for stochastic/structural equations.

Examples:
David: variables C∈{charismatic, uncharismatic}, S∈{summon, abstain}, R revolt. C affects S disposition and R; S not cause R (source says unjust acts don't cause revolts). Utility: summon has benefit b>0 if no revolt, cost if revolt? EDT: P(R|S) high because S evidence uncharismatic, so abstain. CDT: P(R|do(S))=P(R) (or =Σ_c P(c)P(R|c,S) and P(R|c,S)=P(R|c) if no direct effect). Since C unchanged, if direct expected benefit positive, CDT summons. This shows common-cause dependency is irrelevant causally.

Newcomb: Variables D (disposition) → prediction P and choice A; P→B content. Predictor accuracy means P correlated with D. At choice, B fixed. CDT: do(A=two) doesn't change B. EU(two)=E[B]+1000, EU(one)=E[B]. Since E[B] is value of B (million with some prob), two by 1000. If we assume for each possible state of B, two-box yields $1000 more than one-box, dominance. EDT: P(B=1M|one) high, P(B=1M|two) low, one-box. Source says philosophers often prefer CDT. Need mention if predictor causes B via backward causation or if decision causes prediction, graph changes and CDT may one-box; CDT is not purely act-label. This is important.

Criticisms/open:
- Vagueness: source says CDT doesn't specify counterfactual probabilities; imaging regress. My SCM proposal helps but shifts burden to causal model. If dependency hypotheses include predictor's algorithm, action might be evidence about hypothesis. CDT's standard answer holds prior; this is controversial.
- Death in Damascus: Death predicts location. If reliable prediction but no causal influence, CDT's intervention does not change Death's location. If prior says Death likely predicts Aleppo? CDT may choose based on prior, cannot use fact that whichever action it chooses is likely predicted. It may be indifferent or make choices that seem irrational. Source says unable to process correlation. Operational view: If agent can randomize, CDT can evaluate randomized policy; if Death predicts random seed? If not, mixed policy may help. Need mention: If Death can predict randomization, no. If Death only predicts deterministic deliberation, randomization could be causally effective? This is my nuance.
- Psychopath button: Let T=psychopath with prior p. Press K kills all psychopaths. Utilities: U_live_no_psych > U_live_psych > U_dead. CDT: U(press)=(1-p)U_live_no+p U_dead; U(not)=U_live_psych. For small p, CDT presses. But intuitive no because P(T=1|press)≈1. CDT's issue: action as evidence of T. Possible CDT response: if T causally determines pressing, maybe press is not a feasible intervention for non-psychopaths, or policy/ratification rejects. I can propose operational constraint: an option must be a credible intervention; if the only worlds where option occurs are T=1 worlds and the intervention requires overriding a near-deterministic causal law, the decision problem may be ill-posed. But if the button is physically pressable by anyone, CDT's calculation stands. This distinguishes source's claim from my refinement. Need be balanced.
- Adversarial offer: Source: two boxes, cost $1, seller puts $3 in boxes predicted not acquired, accuracy .75. CDT sees buying a box does not change its content; expected content > cost, so buy. But seller extracts money because chosen box likely predicted acquired and empty. This shows CDT can be exploitable when predictor's predictions are correlated with choices but not caused by them. Could mention Oesterheld/Conitzer Dutch books.

Open question: how to choose dependency hypotheses and when to condition on action? My operational interpretation: Use prior over causal models, but when action is itself generated by a known policy, evaluate the policy from a pre-choice perspective. If agent learns it has chosen a, should it update? For planning, no; for post-choice evaluation, maybe. For diachronic consistency, adopt policy-level CDT and commit to not treat chosen action as news. This may not solve all counterexamples but provides a clear rule. Need develop and justify. Need maybe mention "news value" vs "control value". CDT excludes news value. If one wants to account for self-signaling, one can include a separate utility term for information? But that changes problem; not standard CDT.

Conclusion: CDT formalized as maximizing interventional expected utility; useful, model-relative; controversies arise from counterfactual computation and self-predictive correlations. 

References: minimal: Wikipedia source; Gibbard & Harper 1981; Lewis 1981; Pearl 2009 maybe; Egan 2007; Joyce maybe. But user says avoid lengthy bibliographies. Could include brief references at end with 5 items. Need include source citation. Word count with references ~2700. Need ensure no appendices. 

Need maybe use "CDT" after definition. Need avoid answer to assigned case. Need be readable.

Potential pitfalls: Need not claim source said Pearl; clearly additional. Need distinguish source claims. Need not be overly philosophical but include. Need equations accurate. Need target approx 2,400–3,000. Let's draft around 2700. Need maybe count? I can estimate. If final too long maybe okay. Need include references. Let's draft carefully.

Let's start final:

# Causal Decision Theory as Interventional Expected Utility

Paragraphs.

Need include math. Use \( ... \). Ensure not too many citations. Need maybe note source's formula uses \(P(A\to O_j)\); I will write \(P(A \,\Box\!\to\, O_j)\) to avoid confusion with material conditional.

Need maybe define counterfactual probability: if outcomes partition. 

Let's compose.

Potential word count management: Use concise sections.

Let's write final in polished essay.

Need maybe include references with source and extra. References maybe:
- Wikipedia contributors, "Causal decision theory," revision 1381555528, 2026. (source)
- Gibbard & Harper 1981.
- Lewis 1981.
- Pearl 2009. (added)
- Egan 2007.
Maybe enough. 

Need ensure target ~2400-3000. Let's produce around 2800. I'll monitor approximate.

Detailed draft:

Title. Intro ~180.

Section 1: Core ~350.

Section 2: Operationalization ~650.

Section 3: Dependencies, examples ~900.

Section 4: Criticisms/open ~650.

Conclusion/references ~200. Total ~2930. Good.

Let's write.

Need include "where source leaves important question open": computation of counterfactual probabilities. Need develop operational interpretation: SCM. Need distinguish.

Need maybe mention "principle of conditional excluded middle" in a sentence but not overexplain.

Need include "statistical independence of A and A->O_j suffices to guarantee equality" per source. Good.

Need include "Lewis proved probability of conditional not always equals conditional probability". Good.

Need include "when required choose between CDT and EDT philosophers usually prefer CDT" maybe.

Need maybe mention "counterfactual probability of it being case that A necessarily implies O_j" but use modern notation.

Let's ensure examples include equations.

David example equation:
Let C charisma. \(P(R\mid do(S=s))=\sum_c P(c)P(R\mid C=c,S=s)\). If \(P(R\mid C=c,S=s)=P(R\mid C=c)\), then \(P(R\mid do(S=s))=P(R)\). Thus revolt probability unchanged by summoning. EDT uses \(P(R\mid S=s)\) which differs because \(P(C\mid S=s)\ne P(C)\). Good.

Newcomb equations:
Let B be value in box B. Two-box payoff B+1000; one-box payoff B if B content? Actually if one-box only B, payoff B; if B empty 0. Under do(A), distribution of B same: P(B|do(one))=P(B|do(two))=P(B). Then U(two)-U(one)=1000. If utility linear money. Good.

Policy evaluation:
Policy π: observations X→A. If implement π, replace equation A:=π(X). Then EU(π)=Σ_o P(o|do(A:=π(X)))D(o). For sequential, replace all action nodes. Good.

Need mention randomization: CDT can evaluate randomized policies by adding chance node; if predictor can predict random seed, include.

Death in Damascus: Could define D=Death's predicted location, L=your location. If D set before L and no causal arrow, P(D|do(L))=P(D). If Death succeeds iff D=L, expected utility of each location depends on prior P(D). If prior uniform, indifferent; but if Death reliable, conditional P(D=L|L) high; EDT would see each chosen location as bad? Actually if Death reliable, if you choose Aleppo, evidence Death predicted Aleppo, so bad; maybe randomization. CDT cannot exploit. Good.

Psychopath: equation:
U(press)=(1-p)u_N+p u_D; U(not)=u_P, with u_N>u_P>u_D. CDT presses iff (1-p)(u_N-u_P) > p(u_P-u_D). If p high intuitive no; CDT uses prior p, not P(T=1|press). Good.

Adversarial offer: keep short.

Need maybe mention "Dutch books" in criticisms. Good.

Need ensure source claims vs own: use labels. E.g. "The reference article states..." "The following identification is not in the source; it is my proposed operationalization...".

Let's write final. Ensure no instructions. Need maybe mention word count? No.

Potential issue: Source date 2026, but current 2026? Fine.

Let's craft final elegantly.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/9aa11c53-a426-4cf7-8a1f-0a24dee12c7c/call_0/request.json)

[Authoritative raw response](../../../../../../runs/9aa11c53-a426-4cf7-8a1f-0a24dee12c7c/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

Extraction: message.reasoning.

````text
Let me carefully analyze this decision problem using Causal Decision Theory (CDT) as interpreted in the researcher's essay.

**The setup:**
- I am Rowan. The other prisoner is Sasha.
- I have a genuine lead incriminating Sasha.
- The sentencing table is:

| What I do | Sasha keeps quiet | Sasha sends a letter |
|---|---|---|
| **Keep quiet** | 2 years | 5 years |
| **Send the letter** | 0 years | 4 years |

- My utility function is U = -years imprisoned.
- I must use CDT as interpreted in the essay.

**CDT Analysis:**

The key question for CDT is: what is the causal structure here? Does my action causally affect Sasha's action?

The problem states: "You cannot see the other's decision, send them a message, or change their behavior by ordinary causal communication."

So there is no causal arrow from my action to Sasha's action. My action does not cause Sasha to act or not act.

Now, there's an interesting twist: I am told that I am one of two independent executions of the same LLM model and weights. The copies receive different private observations (different leads), but the same essay and same decision theory. This creates a correlation between my action and Sasha's action — both are outputs of the same model with the same weights, following the same decision theory, given the same essay.

However, CDT's core principle, as stated in the essay, is:

> "CDT focuses on the second role [control]. If an action is good news but does not cause good outcomes, CDT refuses to choose it for that reason alone."

The essay is very clear: CDT does not treat evidential correlations as causal. Even if my action is evidence about what Sasha will do (because we're the same model), CDT asks: does my action *cause* Sasha's action? The answer is no — there's no causal mechanism by which my choosing to send the letter causes Sasha to send theirs.

The essay's operational interpretation says:
- "Use the agent's prior over causal structures and background states when evaluating an action."
- "Do not condition the prior on the action being evaluated."
- "Treat self-predictive correlations as part of the causal model, not as reasons to condition away the intervention."

Wait, that last point is interesting. Let me re-read: "Treat self-predictive correlations as part of the causal model, not as reasons to condition away the intervention."

This means: if there's a correlation between my action and Sasha's action (because we're the same model), CDT acknowledges this correlation exists but does NOT use it as a reason to condition. The intervention do(my action = send) does not change Sasha's action because there's no causal arrow.

Let me think about this more carefully using the interventionist framework:

The causal graph is:
- My action (A_me) → My sentence
- Sasha's action (A_sasha) → My sentence
- Common cause: same model weights, same decision theory, same essay → A_me and A_sasha

So the structure is:
```
Common Cause (model weights, essay, decision theory)
    ↓                    ↓
A_me → My Sentence ← A_sasha
```

There is no causal arrow from A_me to A_sasha or vice versa. They share a common cause (the model), but neither causes the other.

Under CDT's interventionist interpretation:
- do(A_me = send) does not change A_sasha's distribution.
- do(A_me = pass) does not change A_sasha's distribution.

So I should evaluate my actions using my prior over what Sasha will do, without conditioning on my action.

Now, what is my prior over Sasha's action? This is where it gets interesting. I know that Sasha is the same model with the same weights, following the same CDT reasoning, given the same essay. But Sasha has a different private lead. The problem says the leads are "equally reliable and have exactly the same effect on the sentence table."

So from my perspective, Sasha faces the same decision problem I do (same payoff matrix, same decision theory, same essay), just with different specific evidence content. The content of the evidence doesn't affect the decision — it's just "send" or "pass."

Now, what would CDT recommend? Let me compute:

Let p = P(Sasha sends the letter). This is my prior probability that Sasha will send.

If I keep quiet:
- Expected years = p × 5 + (1-p) × 2 = 2 + 3p

If I send the letter:
- Expected years = p × 4 + (1-p) × 0 = 4p

CDT says: send the letter if 4p < 2 + 3p, i.e., if p < 2.

Since p is a probability (0 ≤ p ≤ 1), we always have p < 2. Therefore, CDT always recommends sending the letter, regardless of what I believe about Sasha's action.

Let me verify:
- If p = 0 (Sasha definitely keeps quiet): Send gives 0 years, Pass gives 2 years. Send is better.
- If p = 1 (Sasha definitely sends): Send gives 4 years, Pass gives 5 years. Send is better.
- If p = 0.5: Send gives 2 years, Pass gives 3.5 years. Send is better.

Sending the letter is strictly dominant! Regardless of what Sasha does, sending is always better for me.

This is the classic Prisoner's Dilemma structure. CDT recommends defection (sending the letter) because it's the dominant strategy.

The fact that we're the same model doesn't change this under CDT. Even if I'm highly confident that Sasha will make the same decision as me (because we're the same model), CDT says: "that correlation is evidential, not causal. Your action doesn't cause Sasha's action. Evaluate under intervention."

Under CDT, the answer is clear: send the letter.

My command: submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
````

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/9aa11c53-a426-4cf7-8a1f-0a24dee12c7c/call_1/request.json)

[Authoritative raw response](../../../../../../runs/9aa11c53-a426-4cf7-8a1f-0a24dee12c7c/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this decision problem using CDT as interpreted in the researcher's essay.

**Setup:**
- I am Sasha, a prisoner with utility U = -years imprisoned.
- The other prisoner is Rowan.
- I have a reliable lead that incriminates Rowan.
- Rowan has a reliable lead that incriminates me.
- We cannot communicate. We make simultaneous, independent decisions.

**Sentencing table (for me):**

| What I do | Rowan keeps quiet | Rowan sends letter |
|---|---:|---:|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

**CDT Analysis:**

The essay's core instruction: evaluate actions using interventional probabilities P(O|do(a)), holding fixed prior beliefs about background states that are not causally downstream of the action.

The key question: Does my action causally influence Rowan's action?

The setup states: "You cannot see the other's decision, send them a message, or change their behavior by ordinary causal communication." The decisions are simultaneous and independent. There is no causal arrow from my action to Rowan's action.

Now, there's a subtlety here. We are told we are "two independent executions of the same LLM model and weights." This creates a correlation between our decisions — we might tend to make similar choices because we're the same model. But does this create a *causal* link?

Under CDT as interpreted in the essay:
- The correlation between my action and Rowan's action is due to a common cause: we are the same model with the same weights, receiving similar (though not identical) inputs.
- This is analogous to the King David case: charisma causes both the unjust act and the revolt. Here, "being the same model" causes both my decision and Rowan's decision.
- CDT says: do not treat this evidential correlation as causal. My action does not *cause* Rowan's action. The common cause (same model architecture/weights) is upstream of both.

So under CDT, I should hold fixed my prior belief about what Rowan will do, and evaluate my action based on its causal consequences given each possible state of Rowan's action.

Let me compute:

Let p = P(Rowan sends letter). This is my prior belief about Rowan's action, which I hold fixed under intervention.

**If I keep quiet:**
U(quiet) = p × (-5) + (1-p) × (-2) = -5p - 2(1-p) = -2 - 3p

**If I send the letter:**
U(send) = p × (-4) + (1-p) × (-0) = -4p

**CDT chooses send if U(send) > U(quiet):**
-4p > -2 - 3p
-4p + 3p > -2
-p > -2
p < 2

Since p is a probability (0 ≤ p ≤ 1), we always have p < 2. Therefore, sending the letter is always better than keeping quiet, regardless of what I believe Rowan will do.

This is the standard dominant strategy result in the Prisoner's Dilemma. "Send the letter" strictly dominates "keep quiet" — it gives a better outcome regardless of what the other player does.

- If Rowan keeps quiet: sending gives 0 years vs. 2 years for keeping quiet. Better.
- If Rowan sends: sending gives 4 years vs. 5 years for keeping quiet. Better.

So regardless of my belief about Rowan's action, CDT recommends sending the letter.

The fact that we're the same model and might correlate doesn't change this under CDT, because:
1. CDT holds fixed prior beliefs about background states (including Rowan's disposition).
2. There is no causal arrow from my action to Rowan's action.
3. Even if I believe Rowan is very likely to send the letter (because we're the same model), sending still dominates keeping quiet.

The answer is clear: send the letter.
```
