# Evidential Decision Theory: Choosing by What an Action Indicates

Suppose your decision is evidence about something you cannot directly control: what a predictor has already placed in a box, how a psychologically similar person will act, or whether you have an undiagnosed condition. Should that evidence influence your choice?

**Evidential decision theory** (EDT) says yes. Its central instruction is to choose the action associated with the greatest expected utility, conditional on your performing it. The supplied reference article describes this as maximizing an action’s *news value*: do what you would most want to learn that you will do.

The controversial point is not whether actions provide evidence. They plainly can. It is whether their evidential significance should guide choice even when it differs from their causal influence.

This essay develops the conditional-expectation rule, explains its characteristic recommendations, and examines several modeling questions the reference leaves open. In particular, applying EDT requires specifying what the agent already knows, what counts as an alternative, and how probabilities involving the agent’s own decisions are obtained. The policy-level extensions below are operational proposals, not additional doctrines established by the source.

## 1. The basic mathematical rule

Let:

- \(E\) represent the agent’s current information;
- \(A\) be a random variable whose values are available actions;
- \(O\) be a complete outcome;
- \(u(O)\) be the utility of that outcome.

For a finite outcome space, EDT assigns action \(a\) the value

\[
V_E(a)
=
\mathbb E[u(O)\mid A=a,E]
=
\sum_o P(O=o\mid A=a,E)u(o).
\]

It recommends any action satisfying

\[
a^*\in\operatorname*{arg\,max}_{a}V_E(a).
\]

This is the reference article’s formula, with background information made explicit and \(u\) replacing its notation \(D\) for desirability.

“Complete outcome” matters. Utility should include everything the agent values: money, health, other people’s welfare, effort, and any intrinsic significance of the action itself. EDT does not prescribe selfishness or identify utility with money. Monetary examples below assume linear utility for the amounts involved.

An equivalent formulation separates the action from an uncertain state \(S\):

\[
V_E(a)=\sum_s P(S=s\mid A=a,E)\,u(a,s).
\]

The distinctive feature is that the probabilities of states may differ between actions.

For example, consider carrying an umbrella. The utility \(u(a,s)\) depends on both whether you carry it and whether it rains. Your action might also provide evidence about rain: perhaps your decision reflects a forecast you have imperfectly remembered. EDT includes that evidential connection as well as the umbrella’s protection.

This does **not** mean choosing whichever action has the nicest reputation. The relevant evidence must bear on the actual outcomes valued by the agent, after conditioning on \(E\).

A natural operational implementation uses one joint probability model,

\[
P(S,A\mid E),
\]

to evaluate all alternatives. Assigning each action a convenient conditional distribution independently would risk constructing incompatible comparisons rather than applying EDT.

## 2. Conditioning is not intervention

The reference contrasts EDT with causal decision theory (CDT), which evaluates probabilities of counterfactual outcomes under the performance of an action.

In a standard causal-model implementation, this contrast is written

\[
V_{\mathrm{EDT}}(a)
=
\sum_o P(o\mid A=a,E)u(o),
\]

versus

\[
V_{\mathrm{CDT}}(a)
=
\sum_o P(o\mid \operatorname{do}(A=a),E)u(o).
\]

The intervention notation describes setting the action while breaking its ordinary dependence on its causes. It is one precise implementation of causal evaluation, not a definition covering every version of CDT.

Suppose an unobserved variable \(H\) influences both an action and an outcome:

\[
H\longrightarrow A,
\qquad
H\longrightarrow O.
\]

Learning \(A=a\) can change the probability of \(H\), and therefore of \(O\), even if changing \(A\) would not affect \(H\). EDT retains that information; causal intervention generally removes this route.

Bayes’ rule exposes the mechanism:

\[
P(s\mid a,E)
=
\frac{P(a\mid s,E)P(s\mid E)}{P(a\mid E)}.
\]

An action favors states in which that action was more likely.

EDT therefore need not claim that choosing now changes the past. It can instead hold that different choices indicate different pasts. Its disagreement with CDT concerns which comparison should determine a decision.

The theories agree whenever their relevant conditional and interventional distributions agree. They also agree in the state-based formulation when actions provide no additional information about the background state:

\[
P(s\mid a,E)=P(s\mid E).
\]

Ordinary causal consequences remain fully represented in EDT through the utilities and conditional outcome probabilities.

## 3. Newcomb’s problem: evidence about a fixed past

In Newcomb’s problem, a transparent box contains \(k=\$1{,}000\). An opaque box contains either \(M=\$1{,}000{,}000\) or nothing.

A predictor has already filled the opaque box:

- it contains \(M\) if the predictor predicted that you would take only that box;
- it is empty if the predictor predicted that you would take both boxes.

Let \(B\) mean taking only the opaque box, \(T\) taking both, and \(F\) the event that the opaque box is full. Define

\[
q_B=P(F\mid B,E),
\qquad
q_T=P(F\mid T,E).
\]

Then

\[
V_E(B)=Mq_B,
\qquad
V_E(T)=k+Mq_T.
\]

Thus EDT recommends taking only the opaque box exactly when

\[
M(q_B-q_T)>k.
\]

The reference’s numerical example uses

\[
q_B=0.99,\qquad q_T=0.01.
\]

Consequently,

\[
V_E(B)=\$990{,}000,
\qquad
V_E(T)=\$11{,}000.
\]

One-boxing wins decisively.

A modeling qualification is important: “the predictor is 99% accurate overall” does not by itself establish those two conditional probabilities. Overall accuracy also depends on how often each action occurs. The reference’s calculation should be understood as assuming the relevant action-conditional reliability.

Under symmetric reliability \(p\),

\[
q_B=p,\qquad q_T=1-p,
\]

so one-boxing is preferred when

\[
p>\frac{1+k/M}{2}.
\]

For these prizes, the threshold is \(0.5005\). A large enough prize makes even modest predictive dependence important.

Why does CDT disagree? Given either fixed content of the opaque box, taking both boxes yields an additional \(\$1{,}000\). An intervention on the present action does not alter the earlier prediction.

EDT accepts that causal claim but compares different conditional distributions over the box’s contents. Its recommendation is not “make the prediction change.” It is “choose the action that indicates the more favorable prediction.”

## 4. Psychological twins and correlated cooperation

The reference also considers a prisoner’s dilemma played against a psychological twin. Each player receives:

\[
\begin{array}{c|cc}
 & \text{Twin cooperates} & \text{Twin defects}\\
\hline
\text{Cooperate} & 5 & 0\\
\text{Defect} & 10 & 1
\end{array}
\]

Defection gives more money for either fixed action by the twin. But suppose your own decision perfectly predicts the twin’s:

\[
P(C_{\mathrm{twin}}\mid C,E)=1,
\qquad
P(C_{\mathrm{twin}}\mid D,E)=0.
\]

EDT then gives

\[
V_E(C)=5,\qquad V_E(D)=1,
\]

and recommends cooperation.

No communication or causal influence is required. The relevant dependence arises from the agents’ analogous reasoning.

For an imperfect twin, let

\[
p_C=P(C_{\mathrm{twin}}\mid C,E),
\qquad
p_D=P(C_{\mathrm{twin}}\mid D,E).
\]

Then

\[
V_E(C)=5p_C,
\qquad
V_E(D)=1+9p_D.
\]

Cooperation is preferred precisely when

\[
5p_C>1+9p_D.
\]

If the twin matches your action with conditional probability \(r\) under either alternative, then \(p_C=r\) and \(p_D=1-r\). The condition becomes

\[
r>\frac57.
\]

This illustrates how to generalize beyond the idealized example: identify the conditional dependence and calculate its strength. Mere resemblance between players does not establish that cooperation is best. Nor does EDT imply cooperation in every prisoner’s dilemma. With an independent opponent, \(p_C=p_D\), and defection wins.

## 5. The objection: managing the news

The reference reports Lewis’s objection that EDT encourages “managing the news,” and Joyce’s insistence that rational action should depend on causal efficacy rather than auspiciousness.

A supplementary example makes the concern concrete.

Suppose an unknown lesion causes both a desire to smoke and a serious disease. Smoking itself has no effect on the disease, but provides one unit of pleasure. Disease costs 100 utility units. Assume, conditional on the agent’s current information,

\[
P(\text{disease}\mid \text{smoke})=0.8,
\qquad
P(\text{disease}\mid \text{abstain})=0.2.
\]

Then

\[
V(\text{smoke})=1-100(0.8)=-79,
\]

whereas

\[
V(\text{abstain})=-100(0.2)=-20.
\]

EDT recommends abstaining, although smoking adds pleasure and does not cause disease.

The causal objection is sharp: abstention cannot cure the lesion. Why forgo pleasure merely because smoking would reveal bad news?

An evidentialist’s reply is that the conditional expectations really do differ. Treating the lesion’s probability as unchanged across actions would discard the stipulated evidence. The controversy concerns whether such evidence belongs in the decision criterion, not whether the arithmetic is correct.

However, this example depends critically on the information set. If the agent learns whether the lesion is present, the action no longer supplies that information. More generally, additional knowledge may *screen off* the dependence:

\[
P(\text{disease}\mid A,E)
=
P(\text{disease}\mid E).
\]

Then the disease term is identical across actions, and EDT recommends smoking for its pleasure.

One must therefore distinguish two claims:

1. an action correlates with disease in a population;
2. it remains informative about disease given this agent’s information.

Only the second supports the calculation. Whether introspective knowledge of one’s motivations screens off a proposed dependence can be a substantive modeling dispute.

## 6. What probabilities can an agent assign to its own choices?

The reference states the conditional-expectation rule but does not fully explain how agents should assign probabilities to their own deliberative acts.

Ordinary conditioning requires

\[
P(A=a\mid E)>0.
\]

If the agent is already certain that it will choose one action, the elementary formula leaves other actions undefined. Deterministic reasoning can make this especially awkward: if the agent’s procedure and circumstances completely determine its output, where does uncertainty about that output come from?

Possible implementations include:

- uncertainty about the agent’s own reasoning or implementation;
- a model with small probabilities of mistakes or perturbations;
- primitive conditional probabilities specified even for probability-zero antecedents.

These are additional modeling devices, not consequences of the source’s formula. Different treatments of zero-probability alternatives can yield different evaluations.

A reasonable operational proposal is to evaluate options **before treating the result of deliberation as settled evidence**. Hold fixed a predictive model of the decision situation and compare its action-conditionals. Do not first conclude “I will choose \(a\)” and then use that conclusion to eliminate every alternative.

This proposal avoids one immediate circularity, but it does not provide a universal theory of deliberation. In particular, a perturbation model needs justification: errors generated by an independent coin need not have the same evidential significance as ordinary deliberate choices.

EDT is consequently more than a numerical formula. A usable implementation needs a defensible account of self-prediction and counterpossible alternatives, especially when reasoning processes are deterministic.

## 7. Actions, policies, and randomization

A policy specifies what to do across possible future observations. Let

\[
\pi:h\mapsto a
\]

map each decision history \(h\) to an action.

A natural extension of EDT is to treat policy selection as the decision and maximize

\[
V_E(\pi)
=
\mathbb E[U(\text{entire history})\mid \Pi=\pi,E].
\]

This is a proposed policy-level application of the same principle. The reference does not specify a unique policy theory.

Its attraction is straightforward: a policy can itself provide evidence about other agents, earlier predictions, or future behavior. For example, selecting a cooperative policy might indicate that a similarly reasoning agent selects it too.

But the conditioning event must be modeled carefully. “I adopt policy \(\pi\)” need not provide the same information as “I perform action \(a\) once.” Likewise, deciding now and later reconsidering are distinct decisions.

A useful operational distinction is:

- **Binding policy choice:** evaluate complete policies now; later behavior is constrained by the selected policy.
- **Uncommitted future choice:** evaluate actions using the information then available; do not assume that an earlier plan binds.

An ex ante preferred policy need not prescribe an ex post preferred action. EDT’s basic formula alone does not settle which perspective should govern.

Randomization introduces a related distinction. Suppose a predictor cannot observe or predict a genuinely independent coin tossed after its prediction. Conditional on a fixed coin-flipping policy, the realized coin-directed action need not reveal the prediction:

\[
P(F\mid A=B,\Pi=\pi_{\mathrm{coin}},E)
=
P(F\mid A=T,\Pi=\pi_{\mathrm{coin}},E).
\]

One cannot simply import the original Newcomb probabilities into this modified mechanism. The dependence has changed. Conversely, the choice to adopt the randomizing policy may itself be predictable and evidentially significant.

The general lesson is to distinguish the policy-selection event, the implementation mechanism, and the realized action.

## 8. Sequential decisions and a practical procedure

The reference’s discussion of Sleeping Beauty illustrates why policy specification matters. In the familiar setup, Beauty awakens once after heads and twice after tails, with memory erased between awakenings. The source reports disagreement over whether EDT protects certain “halfer” credences from Dutch books; it notes Conitzer’s argument that it does not generally do so.

The appropriate lesson is limited. A local betting decision can provide evidence about decisions at other awakenings, but this does not automatically settle the correct probability of heads or establish immunity to guaranteed losses. One must specify the offered contracts, repeated decisions, information, and total utility across the experiment.

For unfamiliar cases, the following workflow makes EDT operational:

1. **Define the decision object.** Is the alternative a current action, a binding policy, or a choice of randomization mechanism?
2. **Specify current information \(E\).** Include relevant observations and self-knowledge, but distinguish them from the unresolved choice.
3. **Specify complete outcomes and utilities.** Include all consequences the agent values.
4. **Construct a common probability model.** Explain why actions or policies predict uncertain states, rather than merely asserting a correlation.
5. **Check support.** If an alternative has probability zero, state the additional conditional or limiting assumptions required.
6. **Calculate conditional expected utilities.**
7. **Test robustness.** Ask whether screening off, weaker correlations, different utility assumptions, or later information changes the recommendation.

Causal diagrams can help diagnose where an association comes from. EDT does not then discard every noncausal association; retaining those associations is precisely its distinguishing commitment.

## Conclusion

EDT evaluates an action by the expected utility of the world conditional on performing it. It therefore counts both causal consequences and evidential connections—including connections to predictions, hidden conditions, and other agents’ decisions.

Its attraction is that it takes predictive dependence seriously. Its central vulnerability is that favorable evidence need not be an effective means of improvement. Applying it responsibly requires more than calculating an expectation: one must justify the information set, conditional probabilities, alternatives, and treatment of policies and deliberation. Once those are specified, EDT supplies a clear decision rule, even where its recommendations remain philosophically contested.

## References

The supplied article is the source for the core formulation and reported philosophical positions. The smoking example, imperfect-correlation calculations, and operational proposals are additional exposition.

1. Wikipedia contributors. “[Evidential decision theory](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688).” Supplied revision 1373679688, licensed CC BY-SA 4.0.
2. Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.
3. Gibbard, Allan, and William L. Harper. *Counterfactuals and Two Kinds of Expected Utility*. 1976.
4. Lewis, David. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59(1), 1981: 5–30.
5. Joyce, James M. *The Foundations of Causal Decision Theory*. 1999.
6. Conitzer, Vincent. “A Dutch Book against Sleeping Beauties Who Are Evidential Decision Theorists.” *Synthese* 192, 2015: 2887–2899.