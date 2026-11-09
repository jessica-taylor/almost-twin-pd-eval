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