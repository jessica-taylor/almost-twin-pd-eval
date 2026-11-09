# Causal decision theory: choosing what makes a difference

A decision can be good news without doing any good. Seeing someone carry an umbrella may be evidence that rain is likely; carrying one does not thereby cause rain. Causal decision theory (CDT) applies this distinction to an agent’s own choices. Its central recommendation is to choose the available action with the best *expected causal consequences*, not necessarily the action whose occurrence would be the best evidence about the world.

That principle sounds straightforward when actions have familiar effects. If eating a good apple produces pleasure and eating a spoiled apple produces discomfort, the choice depends on the probabilities of those states and the utilities of their consequences. It becomes controversial when an action is correlated with a desirable state that it cannot bring about: perhaps the choice reveals something about the agent’s character, or was anticipated by a predictor who acted earlier.

The challenge is to turn “what this action would cause” into a calculation. CDT is a family of approaches rather than a complete causal model supplied in advance. To use it, one needs probabilities, utilities, available alternatives, and an account of the counterfactual consequences of each alternative.

## From consequences to expected utility

Suppose an agent has actions \(a\in\mathcal A\), and let \(Y(a)\) denote the outcome that would occur if the agent took action \(a\). The outcome should include everything the agent values that might differ between alternatives: money, health, effects on other people, and, if relevant, features of the action itself.

Given the agent’s current information \(E\), a useful formulation of CDT is

\[
V_{\mathrm C}(a)
=\mathbb E\!\left[u(Y(a))\mid E\right],
\qquad
a^*\in\operatorname*{arg\,max}_{a\in\mathcal A}V_{\mathrm C}(a).
\]

Here \(u\) is a utility function, not necessarily monetary payoff. The expectation is taken over uncertainty about what the consequences *would be* under the action. In a finite model with outcomes \(o_1,\ldots,o_n\),

\[
V_{\mathrm C}(a)
=\sum_j P(Y(a)=o_j\mid E)\,u(o_j).
\]

This is a potential-outcome interpretation of the source’s presentation of Gibbard and Harper’s formula,

\[
U(A)=\sum_j P(A\to O_j)D(O_j),
\]

where \(A\to O_j\) is a counterfactual conditional and \(D(O_j)\) is the outcome’s desirability. The relevant thought is “if \(A\) were done, \(O_j\) would result,” rather than a claim that \(A\) *logically necessitates* \(O_j\). Different theories of counterfactuals need not identify that conditional with a potential outcome in every setting; the equation above is an operational interpretation, not a resolution of every semantic dispute.

For a simple example, suppose an apple is good with probability \(0.8\). Eating it yields utility \(4\) if good and \(-6\) if bad; not eating it yields \(0\). If eating does not change whether the apple is good, then

\[
V_{\mathrm C}(\text{eat})
=0.8(4)+0.2(-6)=2,
\qquad
V_{\mathrm C}(\text{abstain})=0.
\]

Eating is recommended. Uncertainty does not make the recommendation noncausal: it concerns which causal situation the agent is in.

The outcome partition must be sufficiently detailed for utility to be well defined. If two outcomes both say “no revolt” but differ in an independently valued respect, they should not automatically receive the same utility. Likewise, expected-money calculations below assume, for illustration, that utility is linear over the relevant sums.

## Causal value versus evidential value

Evidential decision theory (EDT) instead evaluates an action using what taking it would indicate:

\[
V_{\mathrm E}(a)
=\mathbb E[u(Y)\mid E,A=a],
\]

where \(A\) is the action actually taken and \(Y\) the actual outcome. This asks: *suppose I learn that I take \(a\); what should I then expect?* CDT asks: *given what I know now, what would happen were I to take \(a\)?*

The quantities often coincide. If the action is randomized independently of all factors relevant to its potential outcomes, and the actual outcome agrees with the potential outcome of the action actually taken, then

\[
P(Y=o\mid E,A=a)=P(Y(a)=o\mid E).
\]

But correlation between an action and the conditions under which it is taken can break the equality. The source reports a related result of Gibbard and Harper: under additional axioms, independence of an action and the relevant counterfactual conditional suffices for counterfactual and conditional probabilities to coincide. Independence is a substantive assumption, not a rule of decision theory.

Consider a simplified version of King David’s problem from the source. A king is either charismatic or uncharismatic, each with prior probability \(1/2\). A successful revolt occurs with probability \(0.1\) for a charismatic king and \(0.7\) for an uncharismatic one. Suppose charismatic kings summon a particular person with probability \(0.2\), while uncharismatic kings do so with probability \(0.8\). Finally, assume summoning has *no causal effect* on revolt.

Then the act is bad news about charisma:

\[
P(\text{uncharismatic}\mid \text{summon})
=\frac{0.5(0.8)}{0.5(0.8)+0.5(0.2)}
=0.8.
\]

Consequently,

\[
P(\text{revolt}\mid \text{summon})
=0.8(0.7)+0.2(0.1)=0.58.
\]

By the same calculation, the conditional probability of revolt given abstention is \(0.22\). Yet under the stipulated causal model, either intervention leaves charisma unchanged, so

\[
P(\text{revolt under summon})
=P(\text{revolt under abstain})
=0.5(0.7)+0.5(0.1)=0.4.
\]

If the king values summoning, regards avoiding revolt as important, and assigns no other disutility to the act, CDT favors summoning: it gains the desired benefit without increasing the risk of revolt. EDT may favor abstention if the evidential difference in revolt risk outweighs that benefit.

This is not a license to ignore real costs. If the unjust act angers subjects and *thereby causes* revolt, that effect belongs in CDT’s calculation. If David intrinsically disvalues injustice, that also belongs in his utility function. The example isolates a correlation that is assumed not to be a causal consequence.

## Constructing the counterfactuals

The source emphasizes an important gap: CDT itself does not specify an algorithm for calculating counterfactual probabilities. A practical proposal is to use a structural causal model. This is not the only possible implementation of CDT, but it makes its assumptions inspectable.

Let the world be described by variables satisfying structural equations, for example

\[
T=f_T(U_T),\qquad
A=f_A(T,U_A),\qquad
R=f_R(T,A,U_R),
\]

where \(T\) is a personal trait, \(A\) an action, \(R\) an outcome, and the \(U\)'s represent background factors. In the David example, the equation for \(R\) would not actually depend on \(A\). The trait helps explain both the action and revolt, generating correlation without an action-to-revolt causal path.

To evaluate an intervention \(do(A=a)\), replace the equation for \(A\) with \(A=a\), retain the other equations, and propagate the consequences. Thus,

\[
V_{\mathrm C}(a)
=\mathbb E[u(Y)\mid E,do(A=a)]
\]

under the chosen model. The \(do\)-notation is shorthand for an intervention distribution; it is not ordinary conditioning on \(A=a\).

This procedure does **not** freeze every variable other than the action. It preserves background mechanisms and lets downstream variables change. If pressing a switch turns on a lamp, the lamp changes under the intervention. If a predictor filled a box yesterday and the model contains no backward causal influence, the earlier filling does not change merely because the present action is intervened on. What is held fixed is a model-dependent matter, not a blanket instruction to hold the world still.

To use this method in an unfamiliar case:

1. **Specify the decision and information.** What can the agent actually choose now, and what does the agent already know?
2. **Represent uncertain causal possibilities.** Identify relevant background states, mechanisms, and possible effects of each action.
3. **Intervene on the decision variable.** Change the action while allowing its consequences to propagate through the model.
4. **Calculate utilities and average.** Weight outcomes by the agent’s current probabilities, including uncertainty about the causal model itself.
5. **Compare alternatives.** Check whether the recommendation changes under plausible alternative models or utility assignments.

For instance, if there is a probability \(q\) that summoning causes unrest and \(1-q\) that it does not, CDT need not commit dogmatically to one mechanism. It can average the action’s consequences across both hypotheses, using their probabilities conditional on the information available before choosing.

Observational data alone may not identify these intervention distributions. If people who take a treatment are sicker to begin with, comparing treated and untreated outcomes may confound treatment effects with initial health. A causal model, experimental evidence, or other identifying assumptions are needed. CDT tells the agent *which kind of quantity matters*; it does not manufacture the quantity from inadequate evidence.

## Imaging and the limits of “closest worlds”

Another approach mentioned in the source is Lewis’s **imaging**. To evaluate what would happen under \(A\), shift probability mass from each possible world to a closest world in which \(A\) occurs, then examine the resulting distribution of outcomes. This can distinguish a counterfactual distribution from ordinary conditioning: conditioning discards worlds where \(A\) is false and renormalizes those where it is true, whereas imaging can move mass from the former to altered worlds.

The key question is what makes a world “closest.” A world in which an action differs might also differ in earlier causes of the action, or it might instead differ because a local intervention changes the action while preserving those causes. Those choices can lead to different answers. The source also notes a regress worry about specifying what one would believe were one certain of \(A\).

A structural model addresses some of the operational difficulty by explicitly specifying mechanisms to preserve, but it relocates rather than eliminates the philosophical question: why is that intervention, rather than another way of making \(A\) true, the relevant counterfactual? The answer may depend on the decision’s physical and temporal details.

## Newcomb’s problem: dominance against prediction

Newcomb’s problem makes the conflict between causal and evidential reasoning vivid. A transparent box contains \$1,000. An opaque box contains either \$1 million or nothing, having already been filled according to a predictor’s earlier forecast. The agent may take only the opaque box or both boxes.

Assume that the present selection cannot causally affect the earlier prediction or filling. Let \(p\) be the agent’s current probability that the opaque box is full. Then

\[
V_{\mathrm C}(\text{one box})=1{,}000{,}000p
\]

and

\[
V_{\mathrm C}(\text{two boxes})=1{,}000{,}000p+1{,}000.
\]

Two-boxing has the better causal consequence regardless of \(p\). For each fixed content of the opaque box, taking both produces exactly \$1,000 more.

Nevertheless, if the predictor is 99% accurate, taking one box may be powerful evidence that the opaque box is full. As an illustrative symmetric specification, suppose

\[
P(\text{full}\mid \text{one box})=0.99,\qquad
P(\text{full}\mid \text{two boxes})=0.01.
\]

Then EDT assigns the choices expected monetary values of \$990,000 and \$11,000 respectively. Predictor accuracy alone does not determine these two conditional probabilities without further assumptions about prediction errors and the distribution of choices; the numbers illustrate a coherent version of the problem.

The CDT recommendation does not deny the correlation. It denies that a present intervention on the choice changes what the predictor already did. Critics reply that two-boxers predictably receive less, and question the value of a rule that recommends their choice. The disagreement is therefore not primarily arithmetic. It concerns whether a rational decision should exploit correlations with an action even when the action does not cause the correlated advantage.

The temporal qualification matters. If an agent can **earlier** choose and credibly commit to a policy that the predictor observes or anticipates, the commitment can causally affect the prediction and box filling. A CDT calculation at that earlier time may favor committing to one-boxing. That is a different decision from selecting boxes after the filling is complete.

## Actions, policies, and repeated decisions

A policy is a rule for choosing actions in response to later information. To evaluate a policy \(\pi\), one can intervene on the mechanism that implements it and calculate

\[
V_{\mathrm C}(\pi)
=\mathbb E\!\left[u(Y(\pi))\mid E\right].
\]

For example, “take a medicine if a test is positive” has consequences that include the distribution of test results, the treatment’s effects, and any side effects. A policy intervention need not set every later action to the same value; it installs a rule mapping observations to actions.

The distinction between choosing a policy and choosing an action at a later moment is essential. At the policy stage, the selection may affect other agents’ expectations, contracts, or predictions. At the later stage, those effects may already have happened. A commitment device can change the later set of available actions, but merely wishing that a past commitment had been made does not do so.

Sequential cases also raise **dynamic consistency** questions. A plan preferred before receiving information may cease to be preferred after receiving it. Some changes are appropriate responses to new evidence; others arise because an earlier policy’s benefits depend on its remaining credible. CDT can evaluate each decision at its own time, but whether a particular agent should bind itself requires an explicit model of the commitment, the timing, and its costs. The source reports arguments that causal decision theorists can be vulnerable to diachronic Dutch books—sequences of individually accepted transactions producing a loss. Such arguments are challenges to particular implementations and assumptions about sequential choice, not proofs that every policy calculation loses money.

## Alleged counterexamples and self-knowledge

In Egan’s **Psychopath Button** example, Paul wants a world without psychopaths, but strongly prefers surviving to dying. He believes that pressing a button will kill all psychopaths and that only a psychopath would press it.

A simplified numerical model shows the pressure on CDT. Suppose Paul currently assigns probability \(0.1\) to being a psychopath. Pressing gives him utility \(-100\) if he is one and \(+10\) otherwise; not pressing gives \(0\). If his current action cannot change whether he is a psychopath, a straightforward causal calculation gives

\[
V_{\mathrm C}(\text{press})
=0.1(-100)+0.9(10)=-1.
\]

Here CDT does **not** recommend pressing. But if the prior probability were \(0.01\), the same calculation would give \(8.9\), and it would recommend pressing—even if pressing would be overwhelming evidence that he is a psychopath. Thus the alleged counterexample depends on quantitative and informational assumptions, not on the label “CDT” alone.

The source presents Egan’s diagnosis: a problem can arise from holding fixed initial credences in causal dependency hypotheses while evaluating actions. It also reports Joyce’s reply that CDT can use information about what one is inclined or likely to do. Paul’s awareness of a strong inclination to press might itself be evidence that he is a psychopath, raising his current probability before he evaluates either action. The unresolved issue is how such self-locating information enters deliberation and whether updating on it fully answers the objection. One must distinguish evidence already available to Paul from hypothetical news that he has pressed, which EDT and CDT treat differently.

The **Adversarial Offer** illustrates another difficulty. A seller has already put \$3 in each of two boxes predicted not to be purchased. The buyer may purchase at most one, for \$1, or buy neither. At least one box contains \$3, so the sum of their current probabilities of containing \$3 is at least \(1\). Consequently at least one box has probability at least \(1/2\) of containing \$3. If buying cannot change the contents, its causal expected net value is at least

\[
3(1/2)-1=\$0.50,
\]

whereas buying neither yields zero.

Yet if the seller predicts the eventual purchase accurately with probability \(0.75\), the purchased box is empty on correct predictions. Under the further assumption that it contains \$3 on incorrect predictions, the buyer’s actual expected net payoff is

\[
0.75(-1)+0.25(2)=-\$0.25.
\]

The causal assessment of an intervention on a particular box and the conditional distribution among boxes actually purchased are different. This is precisely the disputed point: the buyer is led to take an offer even though the predictor’s accuracy makes the practice profitable for the seller. Details about prediction errors and tie-breaking matter, but the example shows why critics regard the gap between causal value and realized performance as consequential.

## Conclusion

CDT evaluates alternatives by their expected consequences under counterfactual interventions, rather than by the news that performing them would convey. Its practical application requires a model of what changes, what remains governed by the same mechanisms, what the agent knows, and what outcomes are worth.

That framework explains both CDT’s appeal and its difficulty. It avoids treating mere correlation as causal power, yet predictive and self-referential cases make it controversial to ignore correlations between choices and desirable states. Causal decision theory provides a disciplined question to ask; determining the right counterfactual model, and whether causal value is always the right decision criterion, remains open to debate.

## References

- Wikipedia contributors, “[Causal decision theory](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528),” revision 1381555528.
- Gibbard, Allan, and William L. Harper. “Counterfactuals and Two Kinds of Expected Utility,” 1981.
- Lewis, David. “Causal Decision Theory,” *Australasian Journal of Philosophy*, 1981.
- Egan, Andy. “Some Counterexamples to Causal Decision Theory,” *The Philosophical Review*, 2007.
- Oesterheld, Caspar, and Vincent Conitzer. “Extracting Money from Causal Decision Theorists,” *The Philosophical Quarterly*, 2021.