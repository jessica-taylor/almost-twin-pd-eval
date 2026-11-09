# Causal Decision Theory: Choosing What to Change

A decision can be good news without being a good intervention. Suppose taking a certain action would strongly suggest that you are healthy, wealthy, or unusually fortunate. It does not follow that taking the action would make you any of those things. Causal decision theory (CDT) turns this distinction into a rule for rational choice: evaluate an action by the outcomes it would cause, not merely by the outcomes its occurrence would predict.

The reference article presents CDT through probabilities of counterfactuals and contrasts it with evidential decision theory (EDT). It also emphasizes an important limitation: CDT does not, by itself, supply an algorithm for determining those probabilities. A usable account therefore needs both a decision rule and a model of causal dependence.

This essay develops that distinction. The counterfactual rule comes from the article; the structural-model formulation below is an operational interpretation, not a uniquely mandated definition of CDT.

## 1. The counterfactual decision rule

Let \(\mathcal A\) be a finite set of available actions, \(I\) the agent’s present information, and \(O_1,\ldots,O_n\) mutually exclusive and exhaustive outcomes. Let \(u(O_j)\) denote the utility of outcome \(O_j\), including costs, benefits, risks, and any moral considerations the agent values.

Write
\[
A=a\mathbin{\Box\!\!\to}O_j
\]
for the counterfactual proposition that, **if the agent were to perform \(a\), outcome \(O_j\) would obtain**. CDT assigns the action the value
\[
V_C(a\mid I)
=
\sum_j
P(A=a\mathbin{\Box\!\!\to}O_j\mid I)\,u(O_j),
\]
and recommends an action in
\[
\operatorname*{arg\,max}_{a\in\mathcal A}V_C(a\mid I).
\]

This is the form attributed in the article to Gibbard and Harper. Although the article describes the connective in terms of implication, it should not be read as ordinary material implication or as a claim of logical necessity. It concerns what would happen under a hypothetical action.

An equivalent notation uses a potential outcome \(O_a\): the outcome that would result from performing \(a\). Then
\[
V_C(a\mid I)=\mathbb E[u(O_a)\mid I].
\]
This notation assumes that each relevant possible situation supplies a determinate outcome under each action; uncertainty is represented by probabilities over those situations.

EDT instead evaluates
\[
V_E(a\mid I)
=
\sum_jP(O_j\mid A=a,I)\,u(O_j).
\]
Its question is: “How desirable would the world probably be, upon learning that I performed \(a\)?” CDT asks: “How desirable would the world probably become, were I to perform \(a\)?”

Neither theory requires selfishness or risk neutrality. Utilities may represent concern for others and nonlinear attitudes toward money. Their disagreement concerns which probabilities should weight those utilities.

## 2. Making the counterfactuals operational

The article discusses Lewis’s *imaging* proposal: move probability from each possible world to a suitable nearby world in which the contemplated action occurs. The challenge is specifying “nearby.” Should changing my action also change my personality, a predictor’s earlier forecast, or another person’s decision?

A structural causal model supplies one precise answer. Consider variables satisfying equations
\[
X_k=f_k(\operatorname{Pa}_k,E_k),
\]
where \(\operatorname{Pa}_k\) are the causal parents of \(X_k\), and \(E_k\) represents background influences. Assume, for simplicity, an acyclic model with well-defined solutions.

An intervention
\[
\operatorname{do}(A=a)
\]
replaces the ordinary equation determining the action with
\[
A:=a.
\]
All other equations remain intact.

To evaluate an action:

1. Update beliefs about background circumstances using the information already available.
2. Replace the action mechanism with the proposed intervention.
3. Recompute its consequences.
4. Average their utilities.

If \(e\) specifies the background circumstances and \(o_a(e)\) is the resulting outcome, this gives
\[
V_C(a\mid I)=
\sum_eP(e\mid I)\,u(o_a(e)).
\]

This procedure captures a crucial principle: **hold fixed the background circumstances, not every other variable**. Descendants of the action must change when the model says they change. A medicine may alter recovery, which alters future earnings; CDT counts both effects. What it does not automatically alter is a pre-existing condition merely because people taking the medicine tend to have that condition.

Unknown causal structure can also be represented. If \(M\) ranges over candidate models,
\[
V_C(a\mid I)
=
\sum_M P(M\mid I)
\sum_eP(e\mid M,I)\,u(o_a^M(e)).
\]
CDT therefore need not pretend that the causal model is certain. It averages over uncertainty about causation as well as uncertainty about circumstances.

These equations are a proposed implementation of the article’s counterfactual rule. Their substantive assumptions include the legitimacy of replacing the action equation while preserving the other mechanisms. In ordinary treatment decisions this can be natural; in self-prediction puzzles it can be precisely what is disputed.

Where \(I\) is suitable pre-action evidence, the calculation is commonly written
\[
\mathbb E[u(O)\mid\operatorname{do}(A=a),I].
\]
For evidence affected by the action, counterfactual inference requires more care: infer the underlying circumstances from the evidence, then evaluate the alternative action. Ordinary conditioning after an intervention is not always an adequate substitute.

### When conditioning is enough

CDT and EDT agree when observing the action provides no additional information about its potential consequences. A sufficient condition is
\[
O_a\perp A\mid I,
\]
together with consistency—if \(A=a\), the observed outcome equals \(O_a\)—and positive probability of the action. Then
\[
P(O_a=O_j\mid I)=P(O_j\mid A=a,I).
\]

Randomized experiments are designed to secure this sort of separation. Outside such settings, observational frequencies may confound causal effects with selection.

## 3. Common causes: evidence is not a benefit

The article illustrates confounding through King David. His fixed personality influences both his inclination to summon Bathsheba and the probability of a successful revolt. The stipulated story says that summoning her does not itself cause revolt.

Here is a numerical version, with invented probabilities. Let \(H\) mean that David is charismatic, \(S\) that he summons Bathsheba, and \(R\) that a revolt succeeds. Suppose
\[
P(H)=\tfrac12,
\]
\[
P(S\mid H)=0.2,\qquad P(S\mid\neg H)=0.8,
\]
and
\[
P(R\mid H)=0.1,\qquad P(R\mid\neg H)=0.8.
\]
Assume \(H\) screens off the association between summoning and revolt.

Let summoning supply net utility \(1\), after accounting for all its other benefits and costs, and let successful revolt cost \(10\).

Observationally,
\[
P(H\mid S)=0.2,\qquad P(H\mid\neg S)=0.8.
\]
Consequently,
\[
P(R\mid S)=0.66,\qquad P(R\mid\neg S)=0.24.
\]
EDT assigns
\[
V_E(S)=1-10(0.66)=-5.6,
\qquad
V_E(\neg S)=-10(0.24)=-2.4,
\]
and recommends abstention.

Causally, however, neither action changes David’s charisma. Under either intervention,
\[
P(R\mid\operatorname{do}(S))
=
P(R\mid\operatorname{do}(\neg S))
=0.45.
\]
Thus
\[
V_C(S)=-3.5,\qquad V_C(\neg S)=-4.5.
\]
CDT recommends summoning.

The point is not that CDT excuses wrongdoing: additional moral disutility could reverse the decision. The point is that choosing an action associated with charisma does not thereby acquire charisma.

Equally, CDT’s recommendation depends on the causal stipulation. If the summons could provoke revolt, that pathway must enter the calculation. Causal reasoning does not license ignoring inconvenient consequences.

## 4. Newcomb’s problem: prediction without control

In Newcomb’s problem, a transparent box contains \(\$1{,}000\). An opaque box contains either nothing or \(\$1{,}000{,}000\). A reliable predictor has already filled the opaque box if it predicted that the agent would take only that box; otherwise it left it empty.

The agent now chooses between one-boxing and taking both boxes.

Let \(B\) denote the opaque box’s contents. Under the standard causal model, changing the present action does not change \(B\). Therefore, assuming utility equals money,
\[
V_C(\text{one})=\mathbb E[B\mid I],
\]
\[
V_C(\text{two})=\mathbb E[B\mid I]+1000.
\]
Two-boxing wins regardless of the present probability that the opaque box is full. Indeed, it gives an additional \(\$1{,}000\) in either fixed box state.

For a numerical EDT comparison, suppose specifically that
\[
P(B=10^6\mid\text{one})=0.99,
\qquad
P(B=10^6\mid\text{two})=0.01.
\]
These are stronger specifications than merely saying that the predictor has 99% overall accuracy. They yield
\[
V_E(\text{one})=990{,}000,
\qquad
V_E(\text{two})=11{,}000.
\]
EDT therefore one-boxes.

CDT does not deny the predictive association. It denies that exploiting that association by changing the present action changes the already-filled box. The standard causal picture can represent both forecast and action as effects of earlier features of the agent.

This explains the philosophical disagreement. CDT compares alternative actions against a common distribution over fixed box contents. Its critics emphasize that agents disposed to one-box tend to receive much more money.

The article’s suggestion that two-boxing results in only \(\$1{,}000\) should thus be understood as a typical result under accurate prediction, not an unconditional guarantee. A mistaken prediction can leave a two-boxer with \(\$1{,}001{,}000\).

## 5. Actions, policies, and the time of choice

A policy is a rule assigning actions to information histories:
\[
\pi:h_t\mapsto a_t.
\]
One operational extension of CDT evaluates an implementable policy by replacing the relevant future action mechanisms:
\[
V_C(\pi\mid I)
=
\mathbb E[u(O_\pi)\mid I].
\]

The word *implementable* matters. Choosing a binding commitment now is not the same intervention as imagining that one has always possessed a different disposition.

Suppose that before the predictor examines the agent, the agent can install an observable, binding commitment to one-box. If that installation causally affects the forecast, it can make the opaque box likely to be full. CDT may favor paying for the commitment. Later, once the boxes are filled, it still favors taking both boxes if that remains available.

There is no formal contradiction: the two decisions occur at different times and have different causal consequences. Nevertheless, the contrast raises a practical concern about whether a decision theory recommends dispositions it later wishes to abandon.

Conversely, an agent cannot obtain a different recommendation merely by renaming a present action “choosing a policy.” If the supposed policy choice cannot affect the earlier prediction, the standard causal evaluation remains unchanged. The model must specify when a policy is selected, who can observe it, and whether it binds future behavior.

Randomization also requires care. If a private, independent lottery selects among actions and has no other effects, then
\[
V_C(\mu\mid I)=\sum_a\mu(a)V_C(a\mid I).
\]
Such mixing cannot outperform the best pure action. But an observable commitment to randomize can change another agent’s behavior; that is a different causal intervention.

## 6. Self-knowledge and the difficult counterexamples

The article reports Egan’s criticism that CDT holds fixed the agent’s initial probabilities of causal “dependency hypotheses,” even when the contemplated action would be powerful evidence about those hypotheses. Two examples show why this is more than ordinary confounding.

### The psychopath button

Paul can press a button that kills all psychopaths. He values eliminating psychopaths but strongly prefers survival. He also believes that almost anyone who presses the button is a psychopath.

Let \(T\) mean that Paul is a psychopath, and let
\[
p=P(T\mid I).
\]
Relative to not pressing, suppose pressing gives utility \(b>0\) if Paul is not a psychopath and utility \(-d<0\) if he is. A straightforward causal calculation gives
\[
V_C(\text{press}\mid I)=(1-p)b-pd.
\]
It recommends pressing exactly when
\[
p<\frac{b}{b+d}.
\]

By contrast, conditioning on pressing may make Paul’s probability of being a psychopath very high, producing a strongly negative evidential evaluation.

Thus CDT’s endorsement is parameter-dependent, not automatic. The troubling cases combine a low prior probability of psychopathy with a very high probability conditional on pressing.

The article reports Joyce’s response that CDT can use information about what one is inclined or likely to do as evidence. If Paul notices an intense desire to press, that observation can raise \(p\) before he evaluates the intervention.

This distinguishes two operations:

- learning something about oneself during deliberation;
- treating every hypothetical action as evidence that it has actually occurred.

CDT permits the first without generally accepting the second. The unresolved issue is how to model deliberation when acquiring an intention itself supplies important evidence. A sensible operational approach is to update on genuine observations of one’s deliberative state and then reevaluate. But that is not, by itself, a complete theory of stable deliberation.

### The adversarial offer

The article also describes two boxes, each costing \(\$1\). Yesterday, a seller put \(\$3\) into every box she predicted the buyer would not acquire. The buyer may purchase one box or neither.

At least one box is full. Holding the distribution of existing contents fixed, the sum of the boxes’ expected contents is at least \(\$3\). Hence one box has expected contents of at least \(\$1.50\), and straightforward CDT recommends buying some box.

Yet if the seller accurately predicts the buyer’s eventual choice with probability \(0.75\), the purchased box is empty on accurate predictions and full on inaccurate ones. The resulting expected net payoff is
\[
0.75(-1)+0.25(2)=-0.25.
\]

The puzzle contrasts the causal valuation of fixed boxes with the performance of a choice procedure that the seller predicts. Its detailed force depends on the calibration and self-knowledge assumptions: the accuracy claim concerns the action eventually selected, while CDT evaluates interventions against a common distribution over contents.

This is not simply a failure to understand correlation. It challenges whether that common-background comparison is the appropriate standard for choosing a predictably exploitable decision procedure.

## 7. A practical discipline for unfamiliar problems

A useful application of CDT should make five things explicit.

**First, locate the decision.** What can actually be changed now: an act, a commitment, a strategy, or a future decision mechanism?

**Second, specify utility.** Include implementation costs and effects on others, not just the most conspicuous payoff.

**Third, construct the causal model.** Identify common causes, downstream effects, feedback, and uncertainty about mechanisms.

**Fourth, separate evidence from intervention.** Update on information already obtained. Do not automatically update on a hypothetical action merely because actually observing it would be informative.

**Fifth, test sensitive assumptions.** If the answer changes depending on whether a predictor responds causally to a commitment, report that dependence rather than presenting a model-dependent recommendation as unconditional.

Where the model is disputed, expected-utility differences can be evaluated across plausible models. CDT supplies a comparison rule; it cannot replace empirical or philosophical judgment about which counterfactuals are appropriate.

## Conclusion

CDT evaluates actions by their expected effects under intervention. Its central insight is that being evidence of a desirable condition is not the same as bringing that condition about.

A precise application therefore requires more than multiplying probabilities by utilities: it requires specifying what changes with the action and what remains fixed. Structural models offer a workable implementation, while prediction and self-knowledge puzzles expose its contested boundaries. CDT is clearest as a disciplined method of counterfactual comparison—not as a model-free recipe guaranteed to settle every decision problem.

### References

- Wikipedia contributors. “Causal decision theory,” supplied revision 1381555528. [Reference article](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528), licensed CC BY-SA 4.0.
- Gibbard, A., and Harper, W. L. (1981). “Counterfactuals and two kinds of expected utility.” *Ifs*, 153–190.
- Lewis, D. (1981). “Causal decision theory.” *Australasian Journal of Philosophy* 59: 5–30.
- Egan, A. (2007). “Some counterexamples to causal decision theory.” *The Philosophical Review* 116: 93–114.
- Joyce, J. M. (2012). “Regret and instability in causal decision theory.” *Synthese* 187: 123–145.
- Oesterheld, C., and Conitzer, V. (2021). “Extracting Money from Causal Decision Theorists.” *The Philosophical Quarterly* 71.