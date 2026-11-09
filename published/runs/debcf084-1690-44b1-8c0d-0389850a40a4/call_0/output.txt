# Causal decision theory: choosing what makes a difference

A decision can be informative without being effective. Carrying an umbrella is evidence that rain is likely, but carrying one does not usually cause rain. Likewise, a medical test may indicate a disease without producing it. Causal decision theory (CDT) applies this distinction to choice: an action should be assessed by what it would *bring about*, not merely by what its occurrence would reveal.

The central prescription is to choose an available action with the greatest expected causal utility. Uncertainty still matters: an action may succeed in some circumstances and fail in others. But the probabilities relevant to CDT describe outcomes under alternative actions, rather than outcomes conditional on receiving the news that an action occurred.

That distinction is philosophically attractive and sometimes consequential. It also leaves work to be done. A decision theory needs a way to represent the consequences of actions, including situations in which an action is correlated with features of the world that it cannot change. The reference article presents CDT as a family of approaches, not as a complete algorithm for constructing those counterfactuals. The structural-model procedure developed below is one useful operational interpretation; it is an additional modelling proposal, not a uniquely mandated definition of CDT.

## Actions, outcomes, and counterfactuals

Suppose an agent must choose an action \(a\) from a set \(\mathcal A\). Let \(O_1,\ldots,O_n\) be mutually exclusive and exhaustive possible outcomes, and let \(u(O_j)\) be the agent’s utility for outcome \(O_j\). In the formulation attributed by the reference article to Gibbard and Harper, the causal value of \(a\) is

\[
V_C(a)=\sum_j P(a \mathbin{\Box\!\!\to} O_j)\,u(O_j).
\]

Here \(a \mathbin{\Box\!\!\to} O_j\) expresses a counterfactual: *if action \(a\) were taken, outcome \(O_j\) would occur*. CDT recommends an action in

\[
\operatorname*{arg\,max}_{a\in\mathcal A}V_C(a).
\]

The probability in the formula reflects uncertainty about which counterfactual is true. It need not mean that taking \(a\) logically necessitates \(O_j\). For instance, eating an apple may make the agent happy if it is good and unhappy if it is rotten. If the agent assigns probability \(0.8\) to its being good, and utilities \(10\) and \(-20\) to the respective results, then its expected utility is

\[
0.8(10)+0.2(-20)=4.
\]

The agent should compare this with the value of the alternatives, including not eating the apple. “Causes the best outcome” means *best in expectation*, not best in every possible state.

The outcome description must include everything the agent values. If the cost of an action, the welfare of others, or the fact that a promise was broken matters, those features belong in the outcomes or utility function. CDT is a theory of how to evaluate choices given utilities; it does not by itself supply an ethical theory, nor does it require utility to be measured in money.

### Counterfactual probability is not conditional probability

Evidential decision theory (EDT) instead uses

\[
V_E(a)=\sum_j P(O_j\mid A=a)\,u(O_j),
\]

where \(A\) is the action actually taken. This asks: *what should I expect if I learn that I took \(a\)?* CDT asks: *what would happen if I took \(a\)?*

The answers can coincide. If the action is randomized independently of all relevant background factors, and the model correctly describes the consequences, observing an action can tell us the same thing as considering an intervention. But they need not coincide when a common cause influences both action and outcome. The reference article cites Lewis’s results on the distinction between probabilities of conditionals and conditional probabilities; in general, one cannot simply substitute \(P(O_j\mid A=a)\) for the probability of the counterfactual.

For an elementary example, suppose a genetic trait \(G\) makes both smoking and a disease more likely, but smoking has no effect on the disease. Then \(P(\text{disease}\mid\text{smoke})\) may exceed \(P(\text{disease}\mid\text{abstain})\). If the causal assumptions are correct, however, choosing whether to smoke leaves one’s genetic trait and disease risk unchanged. A causal evaluation should still count any *other* effects of smoking, but not an illusory reduction in genetic risk.

The reference article’s example of King David has the same structure. David’s unknown charisma influences both whether he tends to act unjustly and whether a revolt succeeds. Sending for Bathsheba is an unjust action, but the example stipulates that the action itself does not cause revolt. Abstaining can be evidence of charisma without causing it. If David values summoning Bathsheba and has no offsetting moral or other costs, CDT favors summoning; EDT may instead favor abstaining because of what that choice indicates. The stipulations about causation and utility are essential to the result.

## An operational interpretation: interventions in a model

To apply CDT in an unfamiliar case, one needs a disciplined answer to “what would happen if?” A useful way to supply one is a structural causal model.

Let \(Z\) collect background variables, and let the equations of a model \(M\) describe how actions and other variables generate an outcome \(Y\). For example,

\[
A=f_A(Z,\varepsilon_A),\qquad
Y=f_Y(A,Z,\varepsilon_Y).
\]

The variables \(\varepsilon_A,\varepsilon_Y\) represent further influences, potentially correlated where the model warrants it. The observational equation for \(A\) explains how the agent’s actual action is associated with the rest of the world. To evaluate the alternative \(a\), replace that equation by \(A=a\), leaving the other equations in force. This is written \(\operatorname{do}(A=a)\).

Given information \(I\) available at the decision, a practical causal value is

\[
V_C(a\mid I)
=\mathbb E\!\left[u(Y)\mid \operatorname{do}(A=a),I\right].
\]

Equivalently, if \(Y_a\) denotes the outcome that would result from setting \(A\) to \(a\),

\[
V_C(a\mid I)=\mathbb E[u(Y_a)\mid I].
\]

The expectation averages over the agent’s uncertainty about background circumstances and, if necessary, about the causal model itself. If models \(M_k\) have probabilities \(p_k\), then one can use

\[
V_C(a\mid I)=\sum_k p_k\,\mathbb E_k[u(Y_a)\mid I].
\]

This procedure is not something that the label “CDT” automatically provides. Its verdicts depend on the proposed equations, the interpretation of the intervention, the evidence, and the utilities. Different plausible models can produce different recommendations.

The intervention does **not** mean freezing everything except the action. Variables downstream of the action should change according to their equations: pulling a lever may move a switch, stop a machine, and save a worker. Variables causally upstream of the action are ordinarily not changed merely because one considers a different action. Nor should one independently freeze variables whose responses are linked: if a policy changes a market price and the price changes demand, both effects must be represented consistently.

A simple calculation makes the distinction visible. Let \(Z\in\{0,1\}\) be a background condition with \(P(Z=1)=1/2\), let the actual action be \(A=Z\), and let the outcome be \(Y=Z\). Then

\[
P(Y=1\mid A=1)=1,\qquad P(Y=1\mid A=0)=0.
\]

Yet intervening on the action does not alter \(Z\), so

\[
P(Y=1\mid\operatorname{do}(A=1))
=P(Y=1\mid\operatorname{do}(A=0))=\tfrac12.
\]

Observationally, the action perfectly predicts the outcome; causally, it makes no difference.

### What information is held fixed?

The model should incorporate information the agent already possesses. If an apple has a visible bruise, the agent should update its probability of rot before evaluating eating it. Likewise, evidence about one’s own motives or likely behavior may reveal something about oneself. The reference article notes Joyce’s defense of CDT as able to use such information.

But care is needed with evidence that would itself have been different under the contemplated intervention. For example, suppose an indicator lights up *because* an agent presses a button. It would generally be inconsistent to evaluate the counterfactual of not pressing while simply holding fixed the observed illumination as though it were an unaffected background fact. A structural counterfactual can instead use the observation to infer background variables, intervene on the button, and recompute its descendants.

At the moment of choice, this distinction can be subtle. An agent’s experience of being strongly inclined to act may be genuine evidence about their disposition. Whether that experience would remain unchanged under a contemplated alternative depends on the model. CDT’s slogan alone does not settle that question.

## Newcomb’s problem: a choice that predicts the past

Newcomb’s problem dramatizes the difference between evidence and causation. A transparent box contains \$1,000. An opaque box contains either \$1 million or nothing, depending on a prediction made earlier. The predictor put \$1 million in it if it predicted the player would take only the opaque box; otherwise it left it empty. The player now chooses one box or both.

Assume that the contents are already fixed and that the present act cannot alter the earlier prediction or box contents. For each possible content of the opaque box, taking both yields exactly \$1,000 more than taking only it. With money treated as utility and \(q\) the current probability that the opaque box is full,

\[
V_C(\text{one})=q(1{,}000{,}000),
\qquad
V_C(\text{two})=q(1{,}000{,}000)+1{,}000.
\]

Thus CDT recommends taking both.

For an evidential comparison, add a particular statistical assumption: conditional on one-boxing, the prediction is correct with probability \(0.99\), and conditional on two-boxing it is also correct with probability \(0.99\). Then

\[
V_E(\text{one})=0.99(1{,}000{,}000)=990{,}000,
\]

\[
V_E(\text{two})=1{,}000+0.01(1{,}000{,}000)=11{,}000.
\]

EDT recommends one-boxing. An overall 99% accuracy rate by itself does not guarantee these two conditional accuracy figures; they are additional assumptions for the calculation.

The apparent force of each recommendation comes from a different comparison. CDT says that, whatever the predictor has already done, the extra box adds money. Its critic replies that reliable predictors are precisely the circumstances in which the people who two-box tend to get little. CDT does not deny that correlation; it denies that the later act changes the already-filled box. Whether that is the right way to reason remains contested.

## Policies and earlier decisions

An action at the final choice point is not the same object as an earlier policy or commitment. A policy \(\pi\) specifies what to do in each information state: \(A=\pi(S)\), where \(S\) is the signal or situation later encountered. A causal evaluation of adopting a policy can be written

\[
V_C(\pi\mid I)
=\mathbb E[u(Y_\pi)\mid I],
\]

where the counterfactual changes the relevant policy-setting mechanism and allows its downstream effects to unfold.

Timing matters. If an agent can make a binding commitment to one-box *before* the predictor forms its prediction, and the predictor responds to that commitment, adopting the policy may causally cause the opaque box to be filled. If the prediction is already complete, adopting a policy cannot, under ordinary causal assumptions, change that past event. An earlier commitment can therefore be attractive even when, at the later uncommitted choice point, taking both boxes is causally preferable.

This is not a free license to replace a present decision with a hypothetical earlier one. The model must say which commitments are actually available, whether they bind, and whether the predictor can observe or infer them. A policy that exists only in the analyst’s description has no causal effect by itself. Conversely, when a present action changes how other agents will respond in the future—for instance, by establishing a reputation—those responses are genuine causal consequences and belong in the evaluation.

The same distinction helps with games. In a one-shot prisoner’s dilemma against an independent opponent, defection may yield more regardless of the opponent’s choice. Against a highly similar “twin,” cooperation may be strong evidence that the twin cooperates too. If changing one’s present act does not cause a change in the twin’s act, ordinary CDT still evaluates the acts holding the relevant background distribution fixed. But if the players can commit to observable policies, communicate, or influence each other, those mechanisms can change the causal analysis.

## Counterexamples and the problem of self-knowledge

The reference article surveys objections that challenge whether holding fixed prior beliefs about causal dependencies always gives reasonable advice.

In Egan’s “Psychopath Button,” Paul would prefer a world without psychopaths, but pressing a button kills all psychopaths. He strongly prefers survival and thinks only a psychopath would press it. A simple CDT model might assign Paul a low prior probability \(p\) of being a psychopath and reason that pressing is worthwhile when

\[
(1-p)B-pL>0,
\]

where \(B>0\) is the benefit if he survives and \(L>0\) is the loss from dying. Yet the fact that he is seriously inclined to press may itself be evidence that \(p\) is much higher. A CDT agent who already has that evidence should update on it.

The unresolved issue is how far this response goes. If the contemplated or chosen act itself would be powerful evidence about Paul’s type, should that evidence alter the probabilities used to evaluate the act? A straightforward intervention model separates the action from its evidential association with type; other causal theorists may emphasize evidence gained during deliberation or impose further requirements on acceptable decisions. The example exposes a real question about the boundary between using available self-knowledge and conditioning on the very action being evaluated.

The *Adversarial Offer* makes the difficulty especially concrete. A buyer can purchase one of two boxes for \$1, or buy neither. Yesterday a seller put \$3 in each box she predicted the buyer would not acquire. Assume the seller’s prediction is correct with probability \(0.75\).

At least one box contains \$3: if she predicted a purchase, the other box does; if she predicted no purchase, both do. Consequently, under the buyer’s current distribution, the two boxes’ probabilities of containing \$3 sum to at least one. At least one box has probability at least \(1/2\) of containing \$3. If buying a box cannot change its contents, its causal expected net value is therefore at least

\[
3\left(\tfrac12\right)-1=\$0.50,
\]

which exceeds the zero payoff from buying neither. A straightforward CDT calculation recommends buying some box.

Yet, if the buyer does buy one and the seller’s prediction is correct 75% of the time, the purchased box is empty when the prediction is correct. Its actual expected net payoff is then

\[
0.25(3)-1=-\$0.25.
\]

Buying neither would guarantee zero. This is not a contradiction in arithmetic: the causal calculation evaluates a contemplated purchase against a fixed prior distribution over already-filled boxes, while the accuracy assumption describes the correlation between the actual purchase and the seller’s earlier prediction. Whether the resulting recommendation is indefensible, or illustrates the cost of predictive correlation rather than a decision-theoretic error, is disputed.

## Counterfactuals require causal judgment

The reference article identifies a foundational vagueness: CDT itself does not specify a unique algorithm for counterfactual probabilities. Lewis’s *imaging* is one proposal. Roughly, to evaluate action \(a\), move probability mass from each possible world to a suitably close world in which \(a\) occurs, and then calculate the probability of outcomes there. But “closest” must be defined, and the article reports worries about how the beliefs used to select such worlds are themselves justified.

Structural models replace some of that vagueness with explicit assumptions, but do not eliminate it. Observational data alone may not identify whether a correlation is causal; unobserved common causes can make different causal models fit the same data. Nor is every proposed intervention physically coherent. “Set the action while leaving its causes unchanged” is a useful idealization only when it represents the alternative the agent is entitled to consider. Sensitivity analysis—checking whether the preferred action changes across plausible models—is often more informative than reporting one precise answer.

A workable application therefore proceeds as follows: specify the available acts or policies and their timing; record the evidence presently available; model the causal dependencies and possible outcomes; assign utilities and probabilities to the relevant uncertainties; evaluate each intervention; and inspect whether the recommendation depends on disputed assumptions. This procedure makes a CDT argument auditable, even where the underlying counterfactuals remain debatable.

## References

- Wikipedia contributors, “[Causal decision theory](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528),” revision 1381555528.
- Gibbard, A. and Harper, W. L., “Counterfactuals and two kinds of expected utility,” *Ifs: Conditionals, Beliefs, Decision, Chance, and Time* (1981).
- Egan, A., “Some counterexamples to causal decision theory,” *The Philosophical Review* 116 (2007), 93–114.
- Oesterheld, C. and Conitzer, V., “Extracting Money from Causal Decision Theorists,” *The Philosophical Quarterly* 71 (2021).

## Conclusion

CDT asks what difference an available choice would make, averaging its consequences over uncertainty. Its strength is the separation of causal influence from mere evidence. Its hardest cases arise when an action is highly diagnostic of an agent’s situation, or predictable by others, yet cannot causally change the facts it predicts. Applying the theory responsibly requires not only maximizing an equation, but also defending the causal model and counterfactuals that give the equation meaning.