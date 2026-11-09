# Causal Decision Theory: Choosing What to Bring About

A decision can be good news without being a good intervention. Taking a medication might indicate serious illness even when the medication improves survival. Conversely, an action might be evidence of favorable circumstances without doing anything to produce them.

**Causal decision theory** (CDT) makes this distinction central. It recommends maximizing expected utility under counterfactual changes to one’s action, rather than maximizing utility conditional on discovering which action one takes. Its guiding question is:

> Given what I currently know, what would happen if I performed this action?

The mathematical challenge is specifying what changes—and what remains fixed—in answering that question.

## 1. The basic decision rule

Let \(\mathcal A\) be a finite set of available actions, let \(E\) represent the agent’s current evidence, and let \(O_1,\ldots,O_n\) be mutually exclusive, exhaustive outcomes. A utility function \(u(O_j)\) represents the agent’s preferences. Outcomes should include everything relevant: monetary rewards, suffering, moral concerns, action costs, and so forth.

Write \(O_a\) for the outcome that would result if action \(a\) were performed. CDT assigns the action the value

\[
V_C(a\mid E)
=
\mathbb E[u(O_a)\mid E]
=
\sum_j
\Pr(O_a=O_j\mid E)u(O_j),
\]

and recommends any maximizer:

\[
a^*\in\operatorname*{arg\,max}_{a\in\mathcal A}V_C(a\mid E).
\]

The reference article presents Gibbard and Harper’s formulation using probabilities of counterfactuals:

\[
U(A)=\sum_j P(A\to O_j)D(O_j).
\]

Here the arrow should be understood counterfactually: roughly, “if \(A\) were performed, \(O_j\) would result.” It is not material implication, nor a claim that \(A\) logically necessitates \(O_j\).

By contrast, **evidential decision theory** evaluates

\[
V_E(a\mid E)
=
\sum_j
\Pr(O=O_j\mid A=a,E)u(O_j).
\]

This asks how desirable the world would probably be upon learning that the action occurs. Conditional observation and counterfactual intervention need not yield the same probabilities.

A useful representation introduces a background state \(H\), sufficiently detailed to determine the result \(o(a,h)\) of every available action. Then

\[
V_C(a\mid E)
=
\sum_h\Pr(h\mid E)u(o(a,h)),
\]

whereas, assuming consistency between actual and counterfactual outcomes,

\[
V_E(a\mid E)
=
\sum_h\Pr(h\mid A=a,E)u(o(a,h)).
\]

The distinction is visible in the weights. CDT uses the agent’s current beliefs about the background; EDT updates those beliefs using the contemplated action as evidence. If \(H\) and \(A\) are conditionally independent given \(E\), the two calculations coincide. They can also coincide despite dependence—for example, when the dependence makes no difference to expected utility.

## 2. Making counterfactuals operational

The reference article emphasizes that CDT does not, by itself, supply an algorithm for determining counterfactual probabilities. This is a substantive limitation: the decision rule needs a theory of causal dependence.

One operational interpretation is a **structural causal model**. This is an additional modeling framework, not something uniquely specified by the source.

Suppose the world is represented by an acyclic collection of equations

\[
X_i=f_i(\operatorname{Pa}_i,Z_i),
\]

where \(\operatorname{Pa}_i\) are the direct causal parents of \(X_i\), and \(Z_i\) represents background influences. Uncertainty about the background variables \(Z=(Z_1,\ldots,Z_m)\) is represented probabilistically.

To evaluate action \(a\), replace the equation ordinarily determining the action variable \(A\) by

\[
A:=a.
\]

This intervention is written \(\operatorname{do}(A=a)\). Other equations remain unchanged. The modified model determines an outcome \(O_a(z)\) for each background realization \(z\), giving

\[
\Pr(O_a=o\mid E)
=
\sum_z
\mathbf 1\{O_a(z)=o\}\Pr(z\mid E).
\]

Operationally, this involves three steps:

1. Infer the background distribution from actual evidence.
2. Replace the action-generating mechanism with the proposed action.
3. Propagate its consequences through the remaining equations.

This explains what “holding the background fixed” means. It does **not** mean holding every outcome fixed. If pressing a switch illuminates a room, the room’s illumination changes. What remains fixed is the distribution of background conditions and the mechanisms not replaced by the intervention.

Nor does CDT require pretending that causes are known with certainty. If \(M\) indexes competing causal models, one can average:

\[
V_C(a\mid E)
=
\sum_M\Pr(M\mid E)
\mathbb E_M[u(O_a)\mid E].
\]

Uncertainty about treatment effectiveness, hidden traits, or other people’s behavior belongs inside the calculation.

Another approach, discussed in the source, is Lewis’s **imaging**: move each possible world’s probability mass to a suitably “closest” world where the contemplated action occurs. But “closest” needs interpretation. Should changing an action also change earlier circumstances that normally explain it? CDT generally favors a non-backtracking interpretation: alter the action without revising its causal antecedents merely to make it more typical.

Structural intervention supplies one precise version of that idea. It does not prove that this is the uniquely correct counterfactual semantics for every philosophical problem.

## 3. Common causes: the King David example

The source illustrates CDT’s motivation with King David’s uncertainty about his charisma. Charisma affects both his tendency to act justly and his vulnerability to revolt. Summoning Bathsheba is stipulated not to cause revolt, although it is evidence of the uncharismatic personality associated with revolt.

Consider a numerical version. Let \(H\) mean “charismatic,” \(S\) mean “summon,” and \(R\) mean “successful revolt.” Suppose

\[
\Pr(H)=\tfrac12,
\]

\[
\Pr(S\mid H)=0.1,
\qquad
\Pr(S\mid \neg H)=0.9,
\]

and

\[
\Pr(R\mid H)=0.1,
\qquad
\Pr(R\mid\neg H)=0.9.
\]

Assume that, conditional on charisma, summoning has no effect on revolt. The causal graph is

\[
S\leftarrow H\rightarrow R,
\]

with no arrow \(S\to R\).

Intervening on \(S\) leaves charisma unchanged, so

\[
\Pr(R\mid\operatorname{do}(S))
=
\Pr(R\mid\operatorname{do}(\neg S))
=
0.5.
\]

But observationally,

\[
\Pr(R\mid S)=0.82,
\qquad
\Pr(R\mid\neg S)=0.18.
\]

If summoning provides utility \(1\), while revolt costs \(10\), CDT prefers summoning by \(1\). EDT prefers abstaining, because summoning is sufficiently bad news about charisma.

These recommendations depend on the stipulated preferences and causal model. If David assigns substantial negative utility to injustice, or if summoning actually increases revolt risk, CDT can recommend abstention. CDT is not an ethical endorsement of the action; it is a rule for combining utilities with causal beliefs.

The general lesson is broader: changing a symptom, marker, or behavioral manifestation need not change the underlying condition that makes it predictive.

## 4. Newcomb’s problem: prediction without influence

In Newcomb’s problem, a transparent box contains \(\$1{,}000\). An opaque box contains either nothing or \(\$1{,}000{,}000\). A predictor has already filled the opaque box if it predicted that the agent would take only that box, and left it empty if it predicted that the agent would take both.

Let \(B\in\{0,10^6\}\) be the opaque box’s contents. The monetary outcomes are

\[
O_{\text{one}}=B,
\qquad
O_{\text{two}}=B+1000.
\]

Under the standard CDT interpretation, intervening on the present choice does not change the already determined contents. Thus, with linear utility in money,

\[
V_C(\text{two}\mid E)
-
V_C(\text{one}\mid E)
=1000.
\]

Two-boxing is better in every fixed state of the boxes. Indeed, strictly increasing monetary utility suffices for this statewise preference.

EDT instead considers how the action predicts the contents. For illustration, suppose

\[
\Pr(B=10^6\mid\text{one})=0.99,
\qquad
\Pr(B=10^6\mid\text{two})=0.01.
\]

These conditional probabilities are an additional specification; a statement of “99% accuracy” alone need not determine them. With linear utility,

\[
V_E(\text{one})=990{,}000,
\qquad
V_E(\text{two})=11{,}000.
\]

EDT therefore one-boxes.

The disagreement is not that CDT fails to recognize the predictive correlation. It declines to treat that correlation as an effect of intervening on the present action. Critics reply that a recommendation systematically associated with much worse results is difficult to defend. Defenders distinguish choosing a causally beneficial action from having the kind of disposition that receives favorable predictions.

The causal specification matters. If the predictor instead observes the action and fills the box afterward, the action can cause the contents. CDT may then recommend one-boxing.

A similar dispute arises in a prisoner’s dilemma against a highly correlated “twin.” If one’s action does not cause the twin’s action, CDT holds the twin’s move fixed across comparisons and defects when defection strictly dominates. Shared reasoning or common origins can make cooperation evidentially attractive without making it causally effective.

## 5. Actions, policies, and commitment

Many decisions concern policies rather than isolated movements. A policy \(\pi\) assigns an action to each possible information history:

\[
\pi:h\mapsto a.
\]

A causal evaluation replaces the relevant decision mechanisms with this history-dependent rule and computes

\[
V_C(\pi\mid E)
=
\mathbb E[u(O_\pi)\mid E].
\]

Histories themselves may depend on the policy. A medical testing policy, for example, changes what information becomes available and which treatments follow. It would be mistaken to evaluate every policy using the same distribution of subsequent observations regardless of those effects.

Commitment also changes the decision problem. Suppose that, before the Newcomb predictor operates, an agent can install a binding one-boxing mechanism that the predictor will inspect. Installing it can causally influence the prediction and therefore the box’s contents. CDT can recommend this commitment while still recommending two-boxing at the later choice point if no commitment was installed.

There is no contradiction: these are different interventions at different times.

However, calling a present choice a “policy” does not give it causal power over the past. A policy evaluation must specify:

- when implementation occurs;
- which mechanisms it replaces;
- what others can observe;
- which consequences genuinely depend on it.

Randomization requires similar care. For a private random draw that leaves the surrounding mechanisms unchanged,

\[
V_C(\lambda)=\sum_a\lambda(a)V_C(a).
\]

Such a lottery cannot beat its best component action. But publicly announcing a randomized policy may alter another agent’s response, and a predictor may forecast dispositions differently from fresh random outcomes. Those are different causal arrangements, not exceptions to linearity.

The source does not establish a unique treatment of all policy-selection and commitment problems. The intervention-based account here is a proposed operational extension. In particular, optimizing an implementable commitment must not be conflated with assuming that future selves will follow a nonbinding plan.

## 6. Self-knowledge and the psychopath button

CDT becomes especially controversial when the agent’s own deliberation supplies evidence about hidden traits.

In the source’s “psychopath button” example, Paul can press a button that kills all psychopaths. He wants fewer psychopaths but strongly prefers living to dying. He also believes that almost only psychopaths would press the button.

Let \(T\) mean that Paul is a psychopath. Normalize not pressing to utility zero. Suppose pressing gives utility \(b>0\) if he is not a psychopath, and utility \(-L\) if he is, where \(L>0\). Writing

\[
q=\Pr(T\mid E),
\]

CDT evaluates pressing as

\[
V_C(\text{press}\mid E)=(1-q)b-qL.
\]

It recommends pressing exactly when

\[
q<\frac{b}{b+L}.
\]

Yet Paul might believe

\[
\Pr(T\mid A=\text{press},E)
\]

is very high. If the unconditional probability \(q\) remains low enough, straightforward CDT can recommend an action that would itself constitute alarming evidence.

This is not simply the claim that pressing cannot change Paul’s type. His type matters enormously to the button’s causal effect: if he is a psychopath, pressing kills him. The controversy concerns which probability of that type should govern deliberation.

The source reports Joyce’s response that CDT can use information about one’s inclinations or likely behavior as evidence. If Paul notices a disturbing eagerness to press, that observation can enter \(E\), raise \(q\), and reverse the recommendation.

This response has limits. Observing an inclination is not automatically the same as conditioning on every hypothetical action. Doing the latter indiscriminately would erase the distinction from EDT. One might additionally demand **ratifiability**: a recommendation should remain acceptable after learning that one will follow it. But this is an extra deliberative requirement, not a consequence of the basic expected-utility formula, and its implementation remains disputed.

## 7. Predictive exploitation: the adversarial offer

The reference gives another challenge. A buyer may purchase either of two boxes for \(\$1\), or purchase neither. Yesterday, a seller put \(\$3\) into each box she predicted the buyer would not acquire.

At least one box contains money. Consequently, holding the contents fixed across interventions,

\[
\Pr(L\text{ full}\mid E)+
\Pr(R\text{ full}\mid E)\geq 1.
\]

Therefore at least one purchase has causal expected net value at least

\[
3\left(\frac12\right)-1=\$0.50.
\]

Straightforward CDT recommends buying a box rather than declining.

But suppose the seller predicts the eventual choice correctly with probability \(0.75\). When the prediction is correct, the purchased box is empty; when incorrect, it is full. Since the buyer purchases, the stipulated predictive performance gives average net earnings

\[
0.25(3)-1=-\$0.25.
\]

Declining guarantees zero.

The tension concerns the relationship between a fixed deliberative assessment and the evidential implications of the eventual choice. The predictive-accuracy assumption must apply to the actual decision procedure; it cannot automatically be carried over to an externally imposed lottery or a different commitment mechanism.

The source presents this family of cases as an objection to CDT, alongside arguments about diachronic monetary exploitation. They are not merely arithmetic mistakes. They challenge whether maximizing causal value at each deliberative snapshot is an adequate account of rational agency when predictions track the deliberation itself.

## 8. A practical method

For an unfamiliar case, begin by specifying the decision time, feasible actions, and complete utility-relevant outcomes. Separate actual evidence from facts learned only under a hypothetical choice.

Next, identify causal mechanisms and common causes. For each action, ask what would change under intervention—not merely what would probably accompany observing it. Average those consequences using current beliefs, including uncertainty about the causal model.

Finally, test the modeling assumptions. Does a purported commitment genuinely bind? Can others observe the action before responding? Does self-knowledge change the background probabilities? Are prediction and causal influence being confused?

Often the hardest part is not maximizing expected utility, but determining which counterfactual decision problem one has actually described.

## References and provenance

The primary reference is Wikipedia contributors, “[Causal decision theory](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528),” supplied revision 1381555528, licensed CC BY-SA 4.0. The structural-model implementation and numerical elaborations above are additional exposition.

Selected works listed by that source:

- Gibbard, A., and Harper, W. L. (1981). “Counterfactuals and Two Kinds of Expected Utility.”
- Lewis, D. (1981). “Causal Decision Theory.”
- Egan, A. (2007). “Some Counterexamples to Causal Decision Theory.”
- Joyce, J. M. (2012). “Regret and Instability in Causal Decision Theory.”
- Oesterheld, C., and Conitzer, V. (2021). “Extracting Money from Causal Decision Theorists.”

## Conclusion

CDT evaluates actions by their expected counterfactual consequences, not by the favorable news their occurrence would provide. Its strength is a disciplined distinction between influencing the world and learning about it. Its unresolved difficulties concern counterfactual modeling, self-evidence, predictive dependence, and commitment over time. Applied carefully, CDT is therefore both a precise maximization rule and a demand for an explicit account of what an agent’s choices can actually change.