# Causal decision theory: choosing by intervention

A decision can be good news without being a good cause. A doctor’s decision to order a test may be evidence that a patient is seriously ill, although the test does not cause the illness. Conversely, refusing the test would not make the underlying disease less likely. Causal decision theory (CDT) builds its account of rational choice around this distinction.

Its central recommendation is to choose the available action with the best **expected causal consequences**. Evidential decision theory (EDT), by contrast, evaluates an action partly by asking what its occurrence would tell the agent about the world. The two theories agree in many ordinary decisions, but they can disagree sharply when an action is correlated with a desirable or undesirable condition that it does not cause.

The distinction sounds simple. Applying it requires care about what is being held fixed, what information the agent already has, and what counts as an alternative action. CDT is best understood not as a complete causal model, but as a principle for choosing once an appropriate account of causal counterfactuals has been supplied.

## 1. From consequences to expected utility

Suppose an agent must choose an action \(a\) from a set \(\mathcal A\). The agent cares about outcomes \(o\), represented by a utility function \(u(o)\). If an apple is good, eating it may be enjoyable; if it is bad, eating it may be unpleasant. With uncertainty about its quality, the causal value of eating it is a weighted average of those possible consequences.

Gibbard and Harper’s formulation, quoted in the reference article, expresses this idea using counterfactual probabilities:

\[
V_C(a)=\sum_o P(a\mathbin{\Box\!\!\to}o)\,u(o).
\]

Here \(a\mathbin{\Box\!\!\to}o\) means, roughly, “if the agent were to take action \(a\), outcome \(o\) would obtain.” CDT recommends an action in

\[
\operatorname*{arg\,max}_{a\in\mathcal A} V_C(a).
\]

The outcomes should be mutually exclusive and collectively exhaustive, and the counterfactuals should be specified consistently enough to yield a probability distribution over them. The notation is not meant to say that \(a\) *logically* entails \(o\). It concerns what would happen under a hypothetical action in the circumstances under consideration.

For example, suppose the apple is good with probability \(0.8\). Eating it yields utility \(10\) if good and \(-20\) if bad; declining it yields utility \(0\). If eating does not affect its prior quality, then

\[
V_C(\text{eat})=0.8(10)+0.2(-20)=4,
\qquad
V_C(\text{decline})=0.
\]

Eating is recommended. This conclusion depends on the probabilities and utilities, not on a guarantee of happiness.

Utility need not mean pleasure or money alone. It can represent the agent’s preferences over complete outcomes, including risk, fairness, other people’s welfare, and any moral costs the agent accepts. In monetary examples below, I assume utility is linear in money unless stated otherwise. That assumption is convenient but substantive: with nonlinear utility, expected dollars and expected utility can rank actions differently.

## 2. Conditioning is not intervening

EDT uses an apparently similar calculation:

\[
V_E(a)=\sum_o P(o\mid A=a,E)\,u(o),
\]

where \(E\) is the agent’s present evidence and \(A\) is the action actually taken. This asks: *If I learned that I took \(a\), what outcomes would I expect?*

A common operational form of CDT instead uses

\[
V_C(a)=\sum_o P(o\mid \operatorname{do}(A=a),E)\,u(o).
\]

The expression \(\operatorname{do}(A=a)\) represents an intervention that sets the action to \(a\), rather than an observation that the action happened to be \(a\). This equation is a useful structural-causal interpretation of CDT, not a uniquely mandated algorithm in the reference article. It presupposes that the intervention and causal model are appropriate to the decision.

Consider a hidden condition \(H\) that affects both an agent’s action and an outcome:

\[
H\longrightarrow A,\qquad H\longrightarrow O,\qquad A\longrightarrow O.
\]

Observing \(A=a\) can provide evidence about \(H\). Intervening on \(A\) breaks its normal dependence on \(H\), while leaving \(H\)’s influence on \(O\) intact. Thus, in general,

\[
P(O\mid A=a,E)\ne P(O\mid \operatorname{do}(A=a),E).
\]

This does **not** mean that CDT ignores evidence about \(H\). The agent should use all evidence already available at the decision point to form \(P(H\mid E)\). The difference is that, for the purpose of comparing interventions, it does not treat the hypothetical action’s occurrence as additional news about \(H\).

The reference article notes a related formal point: probabilities of counterfactual conditionals are not generally ordinary conditional probabilities. Gibbard and Harper give sufficient conditions for equality, including a suitable independence condition and further assumptions about conditionals. Lewis’s results show why one cannot simply identify probabilities of conditionals with corresponding conditional probabilities in general.

### A king and a revolt

The article’s example of King David illustrates the distinction. David desires to summon Bathsheba but fears a successful revolt. He believes charisma is fixed by genetics and childhood. Charismatic kings tend to act justly and rarely face successful revolts; uncharismatic kings tend to act unjustly and more often face successful revolts. The unjust act itself, however, is assumed not to cause revolt.

To make the structure explicit, let \(H\) be charisma, \(A\) the decision to summon, and \(R\) revolt. If summoning is correlated with low charisma, then

\[
P(R\mid A=\text{summon})>P(R\mid A=\text{abstain})
\]

may hold even though

\[
P(R\mid\operatorname{do}(\text{summon}))
=
P(R\mid\operatorname{do}(\text{abstain})).
\]

The first comparison concerns evidence about the king’s character; the second concerns the effect of his action. On the example’s stipulated causal assumptions, and assuming the desire to summon outweighs any moral disutility assigned to it, CDT recommends summoning. EDT may recommend abstaining because abstention is evidence of charisma and hence of safety.

The assumptions matter. If injustice actually makes revolt more likely, a causal model must include that effect. If David values justice for its own sake, the outcome utility must include that cost. Neither theory gives a recommendation from the correlation alone.

## 3. An operational recipe

The reference article observes that CDT does not itself specify an algorithm for calculating counterfactual probabilities. A practical interpretation is to use a structural causal model when one is available. The following procedure is a proposal for applying the principle, rather than an additional axiom asserted by the article.

1. **Fix the decision point and feasible alternatives.** Specify whether the choice is an immediate act, a rule for later action, or a commitment mechanism. An alternative that is physically or institutionally unavailable should not silently enter the comparison.

2. **Record current evidence \(E\).** Include observations about the environment and, where relevant, about the agent’s own inclinations or reasoning.

3. **Model causal dependencies.** Identify variables, their causal relations, and uncertainty about those relations. Distinguish causes of the action from effects of the action.

4. **Intervene separately on each alternative.** Replace the equation determining the action with the proposed action, while allowing downstream variables to respond according to the model.

5. **Calculate expected utility.** Average the outcomes under each intervention using beliefs informed by \(E\), then choose a maximizer.

For example, let \(H\) be an uncertain background state and let \(O=f_O(A,H,U)\), where \(U\) captures other uncertainty. A simple calculation is

\[
V_C(a\mid E)
=\sum_{h,u}P(h,u\mid E)\,
u_{\!O}\!\left(f_O(a,h,u)\right).
\]

This expression holds fixed the distribution of background variables, not the outcomes those variables help produce. A common mistake is to “hold the world fixed” so aggressively that consequences of the action cannot change. If pressing a switch turns on a light, the light’s state must be allowed to change when the action is intervened on.

Nor does CDT require certainty about the causal model. If \(M\) ranges over possible models, one may average:

\[
V_C(a\mid E)
=\sum_m P(m\mid E)
\sum_o P_m(o\mid\operatorname{do}(a),E)u(o).
\]

This makes causal uncertainty explicit. It does not resolve disagreements over which models or prior probabilities are justified.

There are further limitations. Observational data alone need not identify an intervention distribution: a correlation between treatment and recovery, for instance, does not by itself reveal the treatment’s causal effect. Hidden common causes, selection effects, or an incorrectly specified intervention can alter the answer. CDT tells the agent which sort of quantity to seek; it does not manufacture causal knowledge.

## 4. Newcomb’s problem

The most famous challenge to the causal approach is Newcomb’s problem. A transparent box \(A\) contains \$1,000. An opaque box \(B\) contains either \$1 million or nothing. A predictor has already filled \(B\): it put in the million if it predicted that the player would take only \(B\), and left it empty if it predicted that the player would take both boxes. The predictor is highly accurate.

At the decision point, assume the contents of \(B\) are already fixed and the present act cannot affect them. Let \(p\) be the agent’s current probability that \(B\) is full. Then

\[
V_C(\text{one box})=1{,}000{,}000p,
\]

\[
V_C(\text{two boxes})=1{,}000{,}000p+1{,}000.
\]

Two-boxing has a causal advantage of \$1,000 regardless of \(p\). In each fixed state of the opaque box, taking both gives \$1,000 more.

EDT focuses on a different dependency. If one-boxing is strong evidence that the predictor filled \(B\), while two-boxing is strong evidence that it left \(B\) empty, the evidential expected payoff of one-boxing can be much higher. For illustration, if

\[
P(B\text{ full}\mid\text{one box})=0.99,\qquad
P(B\text{ full}\mid\text{two boxes})=0.01,
\]

then the evidential values are \$990,000 and \$11,000 respectively. These conditional probabilities are an illustrative specification; a bare statement of 99% overall predictive accuracy does not by itself determine both of them.

The disagreement is not about arithmetic. It is about the relevant counterfactual: should changing the act be imagined while leaving the earlier prediction fixed, or should the fact that a different act would have been predicted count in favor of the alternative? Standard CDT takes the former view at the moment of choice. Critics reply that its recommendation is associated with a substantially worse payoff against a reliable predictor.

The causal recommendation also depends on timing. If an earlier agent can visibly bind itself to one-box, and the predictor responds to that commitment before filling the box, choosing the commitment can causally increase the chance of a full box. That is a different intervention from choosing a box after the prediction. CDT can favor the earlier commitment while favoring two-boxing if a later unconstrained choice is reached. This potential conflict between earlier plans and later incentives is a central issue, not a contradiction that can be dismissed by calling both decisions “one choice.”

## 5. Policies, sequences, and other agents

In unfamiliar problems, identifying the decision variable is often the hardest part. A **policy** \(\pi\) is a rule mapping possible observations or histories to actions. If an agent can now install a policy, CDT can evaluate

\[
V_C(\pi\mid E)
=\mathbb E\!\left[u(O)\mid\operatorname{do}(\Pi=\pi),E\right].
\]

The intervention is on the policy-setting variable \(\Pi\). Its consequences may include later actions and other people’s responses to the installed policy. For example, committing to a costly retaliation policy can deter an attack if an opponent observes and believes the commitment. Evaluating only the eventual act of retaliation, after the attack has happened, omits that earlier causal effect.

A policy is not automatically a commitment. If the agent can freely revise it later, its installation may not have the effects attributed to an irreversible device. Conversely, if an earlier predictor observes a genuine policy-setting intervention, the predictor’s response may be causally downstream. The model must say which of these situations obtains.

The same distinction matters in games. In a one-shot prisoner’s dilemma, suppose defection yields a better payoff against either fixed choice of the other player, and the other player’s simultaneous decision is not caused by yours. CDT recommends defection. If the other player is a highly similar “twin,” your decisions may be correlated: cooperating may be evidence that the twin cooperates. EDT can therefore favor cooperation even without a causal influence between the acts. But if the twin observes your commitment, or both players respond to a common policy that you can genuinely set, additional causal pathways can change the CDT calculation.

“Other agents are correlated with me” is consequently not enough to settle a case. One must ask whether the alternative intervention changes their behavior, changes something they observe, or merely gives evidence about a common cause.

## 6. Uncertainty about counterfactuals

The structural approach leaves a philosophical question: which intervention represents “what would happen if I chose otherwise”? Different causal models can agree on observed behavior while disagreeing on that counterfactual. Moreover, ordinary interventions on a decision variable may be awkward when the agent knows much about its own decision procedure.

The reference article discusses Lewis’s *imaging* proposal. Roughly, to evaluate an action, move probability mass from each possible world to a nearby world in which that action occurs, then read off the outcome distribution. This differs from conditioning: probability mass is relocated rather than merely restricted to worlds where the action already occurs.

But “nearby” needs an account. Which features of a world should be preserved when the action changes? A past prediction? The agent’s psychological makeup? The laws and causal mechanisms? The article reports a further worry that determining what one would believe under certainty of the action can itself require a conditional judgment, threatening regress. Imaging therefore illustrates the open problem rather than eliminating it.

My operational suggestion is to make those choices explicit in a causal model and test the conclusion’s sensitivity to them. If two plausible models yield opposite recommendations, the decision problem has not been solved merely by writing \(\operatorname{do}(A=a)\). The notation records an assumption about a counterfactual; it does not justify that assumption.

## 7. Self-prediction and alleged counterexamples

The reference article reports Egan’s concern that holding fixed initial credences in causal dependency hypotheses can separate CDT’s formal calculation from the intuitive instruction to do what will bring about the best result.

In the **Psychopath Button** case, Paul believes that only a psychopath would press a button that kills all psychopaths. He prefers a world without psychopaths, but prefers living with them to dying. If his present probability of being a psychopath is low, a simple causal calculation may assign pressing the button positive value: it removes psychopaths, and only a low-probability background state makes Paul a victim. Yet the contemplated act seems highly diagnostic of that very state.

The issue is not whether Paul may use psychological evidence. The article notes Joyce’s view that CDT can take information about one’s inclinations or likely actions into account. Paul can update on his actual feelings, deliberation and other observations before calculating. The disputed question is whether he must additionally update on the *hypothetical fact* that he presses when evaluating pressing. Doing so resembles EDT; refusing to do so can yield the troubling recommendation. How self-locating evidence enters deliberation is thus a live dispute, not something settled by the slogan “ignore correlations.”

The **Adversarial Offer** makes the problem vivid in monetary terms. A seller offers two boxes for \$1 each; the buyer may buy at most one. Yesterday the seller put \$3 in each box she predicted the buyer would not buy. At least one box therefore contains \$3. With linear monetary utility and the box contents treated as fixed, the two boxes’ causal gross values sum to at least \$3, so one has gross value at least \$1.50. Standard CDT consequently recommends buying some box rather than none.

Yet if the seller predicts the buyer’s acquisition correctly with probability \(0.75\), the acquired box is empty on a correct prediction. If an incorrect prediction places \$3 in the acquired box, the buyer’s expected net payoff is

\[
0.75(-1)+0.25(3-1)=-0.25.
\]

Buying nothing guarantees zero. The causal calculation and the loss rate describe different perspectives: the former compares interventions against the current distribution of fixed contents; the latter describes outcomes across plays in which predictions and purchases are correlated. Critics take the loss as evidence against CDT; defenders may dispute the relevant model, the treatment of information, or the inference from observed loss to irrationality. The example is not resolved merely by repeating either calculation.

## Conclusion

CDT evaluates an alternative by asking what would causally follow from taking it, given the agent’s present evidence and uncertainty. Its strength is the disciplined separation of an action’s consequences from what the action merely signals. Its difficulty is that counterfactual interventions—especially on one’s own decisions and policies—are not supplied by the decision rule itself. Applying CDT responsibly therefore requires an explicit causal model, a clear decision point, and attention to how conclusions change when those assumptions change.

## References

- Wikipedia contributors, [“Causal decision theory,” revision 1381555528](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528), CC BY-SA 4.0.
- Gibbard, A., and Harper, W. L. (1981), “Counterfactuals and Two Kinds of Expected Utility.”
- Lewis, D. (1981), “Causal Decision Theory,” *Australasian Journal of Philosophy* 59, 5–30.
- Egan, A. (2007), “Some Counterexamples to Causal Decision Theory,” *The Philosophical Review* 116, 93–114.
- Oesterheld, C., and Conitzer, V. (2021), “Extracting Money from Causal Decision Theorists,” *The Philosophical Quarterly* 71.