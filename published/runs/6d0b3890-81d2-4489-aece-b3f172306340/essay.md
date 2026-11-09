# Causal decision theory: choosing by consequences rather than news

A decision can be revealing without being influential. Carrying an umbrella is evidence that rain is likely, but ordinarily it does not make rain more likely. Similarly, a medical treatment may be associated with poor outcomes because it is given to the sickest patients, even though it improves their prospects.

Causal decision theory (CDT) builds its advice around this distinction. It says, roughly, to choose the available action whose **causal consequences** have the greatest expected utility. Evidential decision theory (EDT), by contrast, evaluates an action partly by asking what its occurrence would tell the agent about the world. The two approaches often agree. They diverge when an action is evidence about facts that it does not itself change.

This essay develops one operational version of CDT using causal models. The reference article presents the central counterfactual idea but emphasizes that CDT does not, by itself, specify an algorithm for calculating counterfactual probabilities. Structural equations provide a useful implementation, not a uniquely mandatory interpretation. The philosophical disagreements become clearest when we state both the causal model and the point in time at which a decision is being evaluated.

## 1. Expected consequences

Suppose an agent must choose an action \(a\) from a set \(\mathcal A\). Let \(Y_a\) denote the outcome that would occur **if the agent were to take \(a\)**, and let \(u\) be a utility function representing the agent’s preferences over outcomes. Given the agent’s current information \(I\), an intuitive formulation of CDT is

\[
V_{\mathrm C}(a\mid I)
=
\mathbb E[u(Y_a)\mid I],
\qquad
a^*\in\operatorname*{arg\,max}_{a\in\mathcal A}
V_{\mathrm C}(a\mid I).
\]

The expectation matters because an agent can be uncertain about both the world and the consequences of an action. If an apple has probability \(0.8\) of being good, yields utility \(5\) when good and utility \(-3\) when bad, eating it has expected utility

\[
0.8(5)+0.2(-3)=3.4.
\]

That number should be compared with the expected utility of the available alternatives, not with zero unless doing nothing really has utility zero.

The reference article reports Gibbard and Harper’s formulation in terms of probabilities of counterfactuals:

\[
U(a)=\sum_j P(a\mathbin{\Box\!\!\to} O_j)\,D(O_j).
\]

Here \(a\mathbin{\Box\!\!\to}O_j\) is read “if \(a\) were taken, outcome \(O_j\) would occur,” and \(D(O_j)\) is the desirability of that outcome. It is helpful to treat the outcomes as mutually exclusive and exhaustive and to understand the arrow as a *counterfactual conditional*, rather than as ordinary logical implication. On that reading, \(P(a\mathbin{\Box\!\!\to}O_j)\) is the agent’s credence that the relevant counterfactual is true.

If utilities depend directly on the action as well as on its consequences—for example, if a person intrinsically values keeping a promise—one can include the action in the outcome description or write \(u(a,Y_a)\). CDT does not require utility to be money, pleasure, or selfish welfare. It requires a way of comparing the consequences that the agent cares about.

EDT’s corresponding calculation is ordinarily written

\[
V_{\mathrm E}(a\mid I)
=
\mathbb E[u(Y)\mid A=a,I],
\]

where \(A\) is the action actually taken. This asks what outcome to expect *on learning that the action was taken*. By contrast, \(Y_a\) asks what outcome would result under the counterfactual choice of \(a\). These quantities need not agree.

## 2. A causal model as an operational interpretation

A practical way to calculate \(Y_a\) is to describe the situation with a structural causal model. Let variables \(X_1,\ldots,X_n\) satisfy equations

\[
X_i=f_i(\operatorname{Pa}_i,U_i),
\]

where \(\operatorname{Pa}_i\) are the modeled direct causes of \(X_i\), and \(U_i\) collects background factors. The joint distribution of the \(U_i\) expresses uncertainty about the situation. To evaluate an intervention \(\operatorname{do}(A=a)\), replace the normal equation for \(A\) by

\[
A:=a,
\]

while retaining the other equations. Then calculate the resulting distribution of outcomes.

This is a disciplined way of implementing the thought: *what would happen if this action were different, with the relevant background circumstances and causal mechanisms otherwise unchanged?* It removes the ordinary causes of the action in the hypothetical evaluation, while preserving its effects. It does not remove effects merely because they are statistically dependent on the action.

For a decision made with information \(I\), the order matters. First update beliefs about background factors on the information actually available; then evaluate each intervention using that updated distribution:

\[
V_{\mathrm C}(a\mid I)
=
\sum_{\mathbf u} P(\mathbf U=\mathbf u\mid I)\,
u\!\left(a,Y_a(\mathbf u)\right),
\]

with an integral replacing the sum when appropriate. This is an “abduction–intervention–prediction” procedure: infer the situation, change the action equation, and propagate the consequences.

This formula is a proposal for applying CDT under a specified causal model. It assumes, among other things, that the interventions are well defined and that the equations correctly represent the relevant counterfactual dependencies. CDT does not itself tell us which variables to include, which arrows to draw, or how to estimate the background distribution.

### A numerical illustration

Suppose a disease \(S\) influences both treatment \(A\) and recovery \(R\). Patients with severe disease are much more likely to receive treatment. Imagine the following recovery rates:

| Disease state | Probability | Recovery if treated | Recovery if untreated |
|---|---:|---:|---:|
| Severe | \(0.5\) | \(0.4\) | \(0.2\) |
| Mild | \(0.5\) | \(0.9\) | \(0.8\) |

If treatment is assigned to 90% of severe patients but only 10% of mild patients, observed recovery among treated patients is

\[
P(R=1\mid A=1)
=0.9(0.4)+0.1(0.9)=0.45,
\]

whereas recovery among untreated patients is

\[
P(R=1\mid A=0)
=0.1(0.2)+0.9(0.8)=0.74.
\]

Yet intervening to treat everyone gives recovery probability

\[
P(R=1\mid\operatorname{do}(A=1))
=0.5(0.4)+0.5(0.9)=0.65,
\]

versus \(0.5\) without treatment. The observational association is unfavorable because treatment identifies sicker patients. Under the stipulated model, treatment helps in both disease states.

A particular patient who knows their disease state should of course condition on that knowledge rather than use the population averages. And treatment costs, side effects, and uncertainty about the model might alter the utility comparison.

## 3. Why counterfactual probability is not conditional probability

The treatment example shows why

\[
P(Y_a=y\mid I)
\quad\text{and}\quad
P(Y=y\mid A=a,I)
\]

can differ. The former evaluates the consequences of setting the action; the latter also selects cases in which the action naturally occurred. Selection can change the distribution of hidden causes.

The reference article notes a result associated with David Lewis: probabilities of counterfactual conditionals cannot generally be identified with ordinary conditional probabilities. Gibbard and Harper also give conditions under which they coincide: under their stated axioms, independence between an action and the corresponding counterfactual suffices. In an intervention model, a familiar sufficient condition is that, given current information, the natural action is independent of the relevant potential outcomes, together with consistency: when \(A=a\), the observed outcome is \(Y_a\). Then

\[
P(Y=y\mid A=a,I)=P(Y_a=y\mid I).
\]

Randomized assignment can make such independence plausible, but it is not automatic in an ordinary decision. Nor does causal dependence require physical contact or immediate effects: an action can affect another person through a message, a rule, or an institution. The relevant question is whether changing the action changes the outcome through a causal pathway in the model.

The reference article’s King David example illustrates the reverse of the treatment case. Suppose a king’s fixed charisma influences both his tendency toward unjust actions and the likelihood of revolt. Suppose further that an unjust act has *no causal effect* on revolt, even though it is evidence that the king is uncharismatic. Abstaining may be good news about charisma; it does not thereby make the king charismatic. If the king values the contemplated act and assigns no independent disutility to its injustice, CDT recommends it under those stipulations, while EDT may recommend abstention because abstention is evidence of safety.

This is a conditional lesson, not a claim that injustice never provokes revolt or that morality has no utility. Change either assumption and the recommendation can change.

## 4. Newcomb’s problem and fixed predictions

Newcomb’s problem makes the disagreement unusually stark. A transparent box contains \$1,000. An opaque box already contains either \$1 million or nothing. A predictor previously filled the opaque box if it predicted that the player would take only that box, and left it empty if it predicted that the player would take both.

Let \(B\) be the money already in the opaque box. At the moment of choice, the causal payoffs are

\[
Y_{\text{one}}=B,\qquad
Y_{\text{two}}=B+1000.
\]

On the assumptions that the present choice cannot change the earlier prediction or box contents, and that utility is linear in these amounts,

\[
V_{\mathrm C}(\text{two})-V_{\mathrm C}(\text{one})=1000.
\]

Two-boxing causally dominates: whatever is already in the opaque box, it adds \$1,000.

An evidential calculation can favor one-boxing. For example, suppose the conditional probability that the opaque box is full is \(0.99\) given one-boxing and \(0.01\) given two-boxing. Then

\[
V_{\mathrm E}(\text{one})=0.99(1{,}000{,}000)=990{,}000,
\]

\[
V_{\mathrm E}(\text{two})
=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\]

The stated overall prediction accuracy alone does not always imply these two conditional probabilities; they are additional illustrative assumptions.

The force of the objection to CDT is that reliable predictors tend to leave two-boxers poor and one-boxers rich. The causal reply is that a present choice does not retroactively fill the box. Neither response is a simple mathematical correction of the other: they use different principles for relating a decision to correlated facts.

Nor does CDT imply that every two-boxer receives only \$1,000. A wrong prediction can leave the opaque box full, and a two-boxer then receives \$1,001,000. Likewise, an inaccurate predictor can leave a one-boxer with nothing.

## 5. Actions, policies, and the time of choice

A recurring mistake is to treat “choose an action now” and “choose a policy earlier” as the same intervention. They may have different causal consequences.

Let a policy \(\pi\) map later observations \(x\) to actions \(\pi(x)\). If an agent can now install or commit to such a policy, its causal value can be represented as

\[
V_{\mathrm C}(\pi\mid I)
=
\mathbb E[u(Y_\pi)\mid I].
\]

In a structural model, evaluating \(\pi\) means replacing the relevant future decision rule with \(A:=\pi(X)\), while allowing the effects of selecting or publicizing the policy to propagate. A policy can affect what other agents expect, how they respond, and what information becomes available.

In Newcomb’s problem, if a commitment to one-boxing can be made **before** the predictor makes its prediction, and the predictor responds accurately to that commitment, the commitment may causally lead to a filled box. Once the box is filled or empty, the local two-boxing advantage remains. This is a potential conflict between an attractive earlier commitment and the action preferred at the later decision point.

The timing distinction is essential, but it does not dissolve all disputes. A merely hypothetical present resolution may not be an available binding commitment. Nor can one simply assume that changing a policy now changes a prediction already made. An analysis must specify what is controllable, when it is controllable, and whether the predictor’s behavior is downstream of that control.

This applies to strategic settings too. In an ordinary prisoner’s dilemma, if the other player’s simultaneous choice is causally unaffected by yours and defection yields a better payoff against either choice, CDT recommends defection. Against a highly similar “twin,” however, your choice may be evidence about the twin’s choice. Evidential and causal recommendations can then diverge. If there is instead a genuine causal channel—your move is observed, or a prior commitment influences the twin—CDT should include it.

## 6. Uncertainty about the causal structure

An agent need not pretend to know the causal model. Let \(H_k\) be hypotheses about how actions affect outcomes. A natural Bayesian version of CDT averages over them:

\[
V_{\mathrm C}(a\mid I)
=
\sum_k P(H_k\mid I)\,
\mathbb E[u(Y_a)\mid H_k,I].
\]

For example, a drug might have a 70% chance of being effective and a 30% chance of causing severe harm; the causal evaluation weights the outcomes under each hypothesis by the current credences. More information can change those weights, and an action that gathers information can itself be valuable.

The contentious issue is *which information* to use when comparing actions. In the straightforward formulation above, the same current distribution \(P(H_k\mid I)\) is used for each intervention. One does not replace it with \(P(H_k\mid I,A=a)\) merely because the agent is imagining taking \(a\). The latter may import the evidential significance of the action into a calculation intended to measure what the action causes.

But “use current information” does not mean “ignore knowledge of one’s own psychology.” If an agent already knows that they are strongly inclined to take an action, and that inclination is evidence about an underlying trait, CDT can update on that observation before evaluating the alternatives. The reference article reports Jim Joyce’s defense along these lines. The difficult question is how such self-knowledge changes as deliberation proceeds, and whether an agent can stably maintain the credences used in the original calculation.

Consider the article’s “psychopath button.” Paul believes that pressing would eliminate psychopaths, that he is probably not a psychopath, but also that only psychopaths would press. If he uses a low current probability of being a psychopath, assigns sufficient benefit to eliminating psychopaths, and treats pressing as unable to change his own type, a straightforward causal calculation can favor pressing. Yet if his serious inclination to press is already strong evidence that he is a psychopath, updating on that inclination may make pressing unattractive because he would be killed.

The example exposes a real unresolved issue rather than establishing one universal CDT answer. The result depends on the utilities, prior credences, causal assumptions, and evidence available before the choice. It also asks whether discovering one’s preferred action is itself evidence that should revise the calculation, potentially producing instability: an action may look best before that discovery and worst afterward.

## 7. Adversarial predictions and mixed choices

The reference article presents an “Adversarial Offer” that shows why correlated predictions can be troubling even when past facts are held fixed. A buyer can purchase one of two boxes for \$1, or buy neither. Yesterday the seller put \$3 in each box she predicted the buyer would not acquire.

At least one box contains \$3, regardless of the prediction. If \(p_1,p_2\) are the buyer’s current probabilities that the respective boxes contain money, then

\[
p_1+p_2\geq 1.
\]

Hence at least one box has \(p_i\geq \tfrac12\), and its causal expected net value from buying is at least

\[
3\left(\tfrac12\right)-1=\$0.50.
\]

Buying neither has value zero. On a fixed-credence causal comparison, the buyer therefore purchases a box.

Yet if the seller predicts the purchased box correctly with probability \(0.75\), then the buyer receives \$3 only when the prediction is wrong and has expected net payoff

\[
0.25(3)-1=-\$0.25.
\]

The first calculation holds the current contents fixed across hypothetical purchases; the second describes the actual correlation between prediction and purchase. They need not be contradictory. Together they raise a challenge: a decision rule that regards purchase as favorable at the choice point can be exploitable in a population or setup where choices are reliably predicted.

Randomization and commitment need careful modeling here. A genuinely unpredictable random choice might reduce the seller’s accuracy, but the claimed 75% accuracy cannot simply be retained or discarded without specifying what the seller predicts and when. Conversely, if a randomization policy is established early enough to affect the seller’s earlier behavior, its causal value may differ from that of a random draw made after the boxes are filled.

## 8. Where do the counterfactuals come from?

The preceding examples were manageable because their causal structure was stipulated. In unfamiliar cases, obtaining it is usually the hard part.

Observational data alone may not determine what would happen under intervention: several causal models can fit the same correlations while making different predictions about \(\operatorname{do}(A=a)\). Randomized experiments, background science, temporal information, and natural experiments can help, but each relies on assumptions about measurement and transport to the present situation. A CDT calculation can be precise conditional on a model and still be wrong because the model is wrong.

The reference article mentions Lewis’s **imaging** proposal as another way to assign counterfactual probabilities. Roughly, for each possible world, shift its probability mass to a closest world in which the contemplated action occurs, and sum the mass arriving at worlds with each outcome. This makes the meaning of “if the action were taken” depend on a similarity relation between worlds. The hard question becomes which changes count as minimal: should a world preserve an earlier prediction, a decision mechanism, or something else? The article also reports a regress concern about determining the relevant beliefs under the imagined action.

Structural models make many of these choices explicit by specifying which equations survive an intervention. They do not eliminate the underlying philosophical problem: deciding which equations should survive is itself a substantive counterfactual judgment. When plausible models disagree, a responsible application should report sensitivity to those assumptions rather than present a single number as an output of CDT alone.

A practical checklist follows:

1. **Specify the decision point and available alternatives.** Include commitment and information-gathering actions only if they are actually available.
2. **Record current evidence.** This may include observations of one’s own inclinations, but not hypothetical news that a contemplated act has occurred.
3. **Draw the causal dependencies.** Separate causes of the action, effects of the action, and common causes of both action and outcome.
4. **Intervene on each action or policy.** Preserve the background and mechanisms that the chosen model says the intervention does not change.
5. **Compute expected utility**, averaging over uncertainty about states and, where appropriate, causal models.
6. **Test robustness.** Ask how the recommendation changes under plausible alternative causal structures, utilities, timing assumptions, and predictor accuracies.

## Conclusion

CDT recommends actions by their expected causal consequences, not simply by the good or bad news associated with taking them. This distinction explains its treatment of confounding, fixed predictions, and correlated opponents. It also creates its most difficult cases: an action can be causally advantageous under each fixed background state while being strongly associated with an unfavorable state.

A causal model turns the guiding idea into a usable calculation, but it does not settle every question about counterfactuals, self-knowledge, or commitment. Applying CDT well requires both mathematical evaluation and explicit judgment about what an alternative action would—and would not—change.

## References

- Wikipedia contributors, “[Causal decision theory](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528),” revision 1381555528, CC BY-SA 4.0.
- Gibbard, A., and Harper, W. L. (1981), “Counterfactuals and two kinds of expected utility.”
- Lewis, D. (1981), “Causal decision theory,” *Australasian Journal of Philosophy* 59, 5–30.
- Egan, A. (2007), “Some counterexamples to causal decision theory,” *The Philosophical Review* 116, 93–114.
- Oesterheld, C., and Conitzer, V. (2021), “Extracting money from causal decision theorists,” *The Philosophical Quarterly* 71.