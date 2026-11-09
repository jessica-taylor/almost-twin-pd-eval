# Causal decision theory: choosing what makes a difference

A decision can be good news without being a good intervention. Suppose a medical test is usually ordered for seriously ill patients. Patients who receive it may have worse outcomes than those who do not, even if the test improves treatment. Observing that a patient was tested is evidence of illness; ordering the test does not itself cause the illness.

Causal decision theory (CDT) builds its account of rational choice around this distinction. It recommends the action with the best *expected causal consequences*, rather than the action whose occurrence would be the best news about the world. The distinction becomes especially provocative when an action is correlated with facts it cannot change: a person’s character, another player’s similar reasoning, or a prediction made before the choice.

The guiding idea is simple. Its application requires more work. One must specify what is being chosen, what the agent knows, how outcomes depend on the choice, and which features of the world remain fixed when alternatives are considered. The reference article presents CDT as a family of views and notes that it does not by itself supply an algorithm for calculating the relevant counterfactual probabilities. The structural-model procedure developed below is one useful operational interpretation, not an extra axiom established by the article.

## From outcomes to counterfactual outcomes

Let \(A\) be a set of available actions and let \(O_1,\ldots,O_n\) be mutually exclusive and exhaustive outcomes. Write \(u(O_j)\) for the agent’s utility for outcome \(O_j\). Utility need not be money: it can incorporate risk, health, obligations, and the welfare of others, provided these can be represented by the relevant expected-utility scale.

The reference gives Gibbard and Harper’s causal expected utility in the form

\[
V_{\mathrm C}(a)
 =\sum_{j=1}^n P(a\mathbin{\Box\!\!\to}O_j)\,u(O_j),
\]

where \(a\mathbin{\Box\!\!\to}O_j\) is read as the counterfactual “if action \(a\) were performed, outcome \(O_j\) would occur.” CDT selects an action in

\[
\operatorname*{arg\,max}_{a\in A}V_{\mathrm C}(a).
\]

The arrow here should not be understood as ordinary material implication, nor as the assertion that \(a\) logically or necessarily entails \(O_j\). It concerns what would happen under the alternative action in the circumstances being considered. The probabilities express uncertainty about those counterfactual consequences.

Equivalently, introduce the *potential outcome* \(O(a)\): the outcome that would result were \(a\) performed. Given the agent’s present information \(E\), a convenient expression is

\[
V_{\mathrm C}(a\mid E)
   =\mathbb E\!\left[u(O(a))\mid E\right].
\]

This form makes an important distinction visible. We condition on the information the agent actually has, \(E\), but we do not generally condition on the proposition that the agent in fact performs \(a\). The latter proposition may be evidence about the world in ways that the intervention itself does not reproduce.

For comparison, evidential decision theory (EDT) evaluates an action by

\[
V_{\mathrm E}(a\mid E)
   =\mathbb E\!\left[u(O)\mid A=a,E\right],
\]

when this conditional expectation is defined. EDT asks what an action’s occurrence would indicate; CDT asks what doing it would bring about. The reference notes Lewis’s result that probabilities of conditionals cannot in general be identified with ordinary conditional probabilities. In decision-theoretic terms, there is no general rule equating \(P(O(a)=o\mid E)\) with \(P(O=o\mid A=a,E)\).

They can coincide. If, given \(E\), the actual action is independent of the relevant potential outcomes, and the actual outcome agrees with the potential outcome for the action actually taken, then

\[
P(O(a)=o\mid E)=P(O=o\mid A=a,E).
\]

Randomized treatment assignment is designed to create a version of this independence. But voluntary choices are often informative about people and their circumstances, so independence cannot simply be assumed.

### A small calculation

Suppose an apple is good with probability \(0.8\). Eating a good apple has utility \(10\), eating a bad one has utility \(-20\), and declining has utility \(0\). If eating does not change whether the apple was already good, then

\[
V_{\mathrm C}(\text{eat})
 =0.8(10)+0.2(-20)=4.
\]

CDT recommends eating it. The point is not that the outcome is certain, but that the expected utility of the intervention is higher. A further inspection could be valuable if it supplies information that changes the subsequent choice; its cost and effects would have to be included in a separate evaluation.

## A causal model as a working tool

To apply CDT to an unfamiliar case, it is helpful to describe a causal model. Let \(X\) represent background conditions, \(A\) the action, and \(Y\) an outcome. A simple model might have equations

\[
A=f_A(X,U_A),\qquad Y=f_Y(A,X,U_Y),
\]

where \(U_A,U_Y\) represent other influences. The first equation describes how the action ordinarily comes about; the second describes how action and background jointly produce the outcome.

To evaluate action \(a\), replace the action equation with

\[
A:=a
\]

and leave the other equations in place. This is the intervention written \(\operatorname{do}(A=a)\). It cuts the ordinary causal inputs into \(A\), not the causal effects of \(A\) on its descendants. In this model the value is

\[
V_{\mathrm C}(a\mid E)
 =\mathbb E\!\left[u(Y)\mid \operatorname{do}(A=a),E\right],
\]

with the understanding that the distribution of background variables is first informed by the evidence available at the decision point. If \(E\) includes a variable that would itself be affected by the contemplated intervention, this notation can be ambiguous: one must specify its timing and how evidence about the actual world enters the counterfactual calculation.

The model clarifies what “holding fixed” does and does not mean. An intervention normally holds fixed the underlying background conditions and causal mechanisms, while allowing downstream variables to change. If taking medicine causes nausea as well as recovery, both effects belong in the evaluation. Holding the observed level of nausea fixed across actions would erase part of the causal effect.

Conversely, if an action is correlated with a prior condition because that condition influences the action, setting the action does not automatically alter the prior condition. The relevant contrast is between changing the world *through* the action and learning something *from* the fact that it occurred.

A causal graph and observational data may not determine the answer on their own. Confounding, limited data, or uncertainty about the graph may leave intervention effects unidentified. A decision-maker can represent that uncertainty by averaging over models \(M\):

\[
V_{\mathrm C}(a\mid E)
 =\sum_m P(M=m\mid E)\,
   \mathbb E_m[u(O(a))\mid E].
\]

This is a proposal for implementing expected causal utility under model uncertainty. It does not make the model probabilities easy to obtain, and different agents with different evidence may rationally calculate different values.

## Correlation without causal control

The reference’s King David example illustrates the contrast with EDT. David wants to summon Bathsheba but fears a revolt. He believes kings have stable personality types: charismatic kings tend to act justly and rarely face successful revolts; uncharismatic kings tend to act unjustly and face revolts more often. In the stipulated story, unjust acts do not themselves cause successful revolt. Both are associated with personality type.

Imagine, for illustration, that half of kings are charismatic. A charismatic king summons with probability \(0.1\) and faces revolt with probability \(0.05\); an uncharismatic king summons with probability \(0.9\) and faces revolt with probability \(0.50\). Then summoning is strong evidence of being uncharismatic:

\[
P(\text{uncharismatic}\mid\text{summon})=0.9.
\]

Consequently, the conditional probability of revolt given summoning is

\[
0.9(0.50)+0.1(0.05)=0.455,
\]

whereas the probability given abstention is \(0.095\). EDT treats this difference as relevant to the evidential value of the two acts.

For CDT, under the stated causal assumptions, summoning does not change David’s personality or the revolt risk generated by it. Before learning anything further about his type, the risk under either intervention is

\[
0.5(0.50)+0.5(0.05)=0.275.
\]

Thus, *so far as revolt risk is concerned*, the actions have the same causal value. If David values summoning and assigns no sufficient countervailing moral or other cost to it, CDT recommends summoning, as in the reference. That conclusion is conditional on the story’s causal and utility assumptions. If injustice itself incites revolt, or if David assigns disutility to the injustice, the calculation changes.

The example also shows why causal analysis is not permission to disregard correlations. The correlation is evidence for a common-cause model; it may help estimate David’s type. CDT’s point is narrower: the correlation does not, by itself, establish that changing the action changes the cause of the correlation.

## Newcomb’s problem and the value of a fixed past

In Newcomb’s problem a predictor has already filled an opaque box with either \(\$1{,}000{,}000\) or nothing. A transparent box contains \(\$1{,}000\). The predictor filled the opaque box if it predicted that the player would take only that box, and left it empty if it predicted that the player would take both. Assume there is no backwards causal effect from the current choice to the already completed prediction and filling.

Let \(p\) be the player’s present probability that the opaque box is full. With money as utility, CDT gives

\[
V_{\mathrm C}(\text{one box})=p(1{,}000{,}000),
\]
\[
V_{\mathrm C}(\text{two boxes})=p(1{,}000{,}000)+1{,}000.
\]

Two-boxing adds \(\$1{,}000\) whichever way the opaque box was filled. It is therefore causally preferred for every \(p\).

An EDT calculation can favor one-boxing because the choice is evidence of the prediction. For example, suppose that in the joint distribution of predictor outputs and choices,

\[
P(\text{full}\mid\text{one box})=0.99,\qquad
P(\text{full}\mid\text{two boxes})=0.01.
\]

Then EDT values one-boxing at \(\$990{,}000\) and two-boxing at \(\$11{,}000\). These conditional probabilities are stronger, more specific assumptions than merely saying that the predictor is 99% accurate overall.

The philosophical dispute is not resolved by observing that one-boxers usually receive more in such a population, nor by observing that two-boxing adds \(\$1{,}000\) for a fixed box state. Each observation supports a different way of assessing the choice. Nor does CDT imply that every two-boxer receives only \(\$1{,}000\): an inaccurate predictor can have filled the opaque box. The criticism is that the procedure tends to recommend an action associated with an unfavorable prior prediction, even though the prior prediction is not an effect of the present act.

## Choosing policies, not just immediate acts

The timing and identity of the object chosen matter. Suppose that *before* the predictor examines the player, the player can install an enforceable commitment to take only the opaque box. If the predictor detects that commitment and responds to it, the commitment can causally affect the later prediction and box filling. CDT can then recommend committing to one-box, even though it recommends taking both boxes if an uncommitted player reaches the later choice with the boxes already filled.

There is no contradiction: “install the commitment” and “take one box now” are different interventions at different times.

More generally, a policy \(\pi\) maps later observations \(h\) to actions \(\pi(h)\). To evaluate adopting it, one can write

\[
V_{\mathrm C}(\pi\mid E)
 =\mathbb E\!\left[u(O(\pi))\mid E\right],
\]

where \(O(\pi)\) includes the effects of adopting the policy, the observations subsequently received, and the actions the policy prescribes. A policy can be valuable because it reacts to information, or because other agents causally respond to its adoption.

One must not, however, assign a current policy choice causal influence over an earlier predictor merely because the predictor’s output correlates with the policy. The causal story must include an appropriate channel: an earlier commitment, a signal, access to the agent’s decision process, or some other mechanism. Whether selecting a decision procedure should be treated as changing logically similar computations elsewhere is a further philosophical question; it is not settled by ordinary CDT’s instruction to follow causal consequences.

Sequential decisions can also be dynamically unstable. An earlier self may pay to bind a later self precisely because the later self, evaluating only the options then available, would choose differently. Whether that is a defect depends partly on whether one judges rationality at each decision point, over whole plans, or both.

## Predictors, twins, and adversarial offers

The same issues arise without boxes. In a prisoner’s dilemma, defection gives a higher individual payoff than cooperation for either fixed choice of the other player. If the other player’s act is not causally affected by yours, straightforward CDT therefore recommends defection. If the other player is a psychological twin whose reasoning is strongly correlated with yours, cooperation may nevertheless be associated with mutual cooperation, while defection is associated with mutual defection. Correlation alone does not reverse the causal dominance argument; a causal response to your act or policy could.

The reference describes the **Adversarial Offer**, which makes the tension numerical. A seller has put \(\$3\) in each of two boxes she predicted the buyer would *not* acquire. The buyer may purchase one box for \(\$1\), or purchase neither. At least one box contains \(\$3\). At the point of purchase, assume the contents are fixed and buying a box does not change them.

If \(p_1,p_2\) are the buyer’s current probabilities that the respective boxes contain \(\$3\), then

\[
p_1+p_2\geq 1.
\]

At least one box has causal expected net value at least

\[
3\left(\frac12\right)-1=\$0.50,
\]

so buying a suitably chosen box beats buying neither, which has value zero. Yet if the seller correctly predicts the acquired box with probability \(0.75\), the buyer receives \(\$3\) only on the remaining \(0.25\) of purchases. The average net return from purchasing is then

\[
0.25(3)-1=-\$0.25.
\]

The two calculations use different distributions: the first assesses each intervention against the buyer’s current beliefs about fixed contents; the second describes the correlation between the actual purchase and the seller’s prior prediction. A precise analysis must also specify the buyer’s information, symmetry, randomization, and what the seller predicted if no purchase occurs. The example is nevertheless a sharp challenge to the thought that locally maximizing causal expected value must secure a favorable return over predictor-selected cases.

## Information, self-knowledge, and unstable deliberation

CDT does not require an agent to ignore evidence about what they are inclined to do. As the reference notes, defenders including Joyce allow such information to update beliefs. The difficult question is how deliberation and learning about one’s own disposition interact.

In Egan’s “Psychopath Button” case, Paul wants to live in a world without psychopaths but believes that only a psychopath would press a button killing them all. He strongly prefers living with psychopaths to dying. A simple causal calculation might assign a low prior probability \(q\) to Paul’s being a psychopath and hold that probability fixed under the intervention of pressing. If the benefit of eliminating psychopaths is \(B\), and the loss from Paul’s death is \(L\), a stylized value is

\[
V_{\mathrm C}(\text{press})=B-qL,
\]

relative to not pressing. For sufficiently small \(q\), this is positive. But Paul’s recognition that he is seriously inclined to press may itself be evidence that he is a psychopath, increasing \(q\) enough to reverse the recommendation.

There is an important difference between **learning of an inclination** and **conditioning on a hypothetical act**. The former can be actual evidence available to the deliberator; the latter is exactly the move CDT resists when comparing interventions. Nevertheless, as the agent deliberates, the evidence available may change. An initial recommendation can produce or reveal an inclination that undermines the recommendation. The reference reports this family of cases as a criticism of holding initial credences in dependency hypotheses fixed. How best to handle such feedback, including whether one needs a stable or “ratifiable” decision, remains disputed rather than settled by the basic formula.

## Where do counterfactual probabilities come from?

The central practical limitation is that CDT needs counterfactuals, while ordinary observation supplies facts about what actually happened. A causal model is one way to bridge the gap, but its equations and intervention semantics are assumptions to be justified, not consequences of the CDT maximization rule.

The reference also mentions Lewis’s **imaging** proposal. Roughly, to evaluate “if \(a\), then \(O\),” move probability mass from each possible world to a sufficiently close world in which \(a\) occurs, and add the mass landing in worlds where \(O\) occurs. This makes explicit that alternative actions must be evaluated against some account of which features of the world are preserved. But “closest” is not automatically well defined, and the reference reports worries that specifying the relevant beliefs under the hypothetical can lead to regress.

For practical work, an explicit causal model is often preferable because it exposes these choices. A disciplined application proceeds as follows:

1. **Fix the decision point and information.** Record what the agent actually knows, including any evidence about their own dispositions.
2. **Define feasible interventions.** Distinguish an immediate act, a randomized act, an advance commitment, and a policy.
3. **Model causal dependencies.** Include common causes, effects of the action, other agents’ responses, and uncertainty about the mechanisms.
4. **Calculate counterfactual utilities.** For each intervention, propagate its effects while retaining the appropriate background uncertainty.
5. **Compare and test sensitivity.** Check whether a different causal graph, utility assignment, or information state changes the recommendation.

These steps implement the source’s central idea; they do not eliminate its philosophical uncertainties. In particular, one should ask whether the intervention being imagined is genuinely available and whether a predictor’s behavior is causally downstream of it. The answer can change when the decision is reframed earlier or later.

## Conclusion

CDT evaluates actions by their expected effects, not merely by what their occurrence would reveal. Its power lies in separating evidence of a condition from control over that condition. Its controversial cases arise when actions are correlated with valuable outcomes through predictors, shared dispositions, or prior choices that an immediate intervention cannot alter.

Used carefully, CDT is a precise method once a causal model, information state, and utility function are supplied. The hard questions are often upstream of the maximization: which counterfactual model is appropriate, what counts as an available policy, and whether local causal improvement is the right standard when agents know their choices are predictably correlated with the world.

### References

- Wikipedia contributors, [“Causal decision theory,” revision 1381555528](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528), licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- Gibbard, A., and Harper, W. L. (1981), “Counterfactuals and two kinds of expected utility.”
- Lewis, D. (1981), “Causal decision theory,” *Australasian Journal of Philosophy* 59, 5–30.
- Egan, A. (2007), “Some counterexamples to causal decision theory,” *The Philosophical Review* 116, 93–114.
- Oesterheld, C., and Conitzer, V. (2021), “Extracting Money from Causal Decision Theorists,” *The Philosophical Quarterly* 71.