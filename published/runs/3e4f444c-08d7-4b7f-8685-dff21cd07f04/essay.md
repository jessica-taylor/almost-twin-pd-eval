# Causal decision theory: choosing what makes a difference

A decision can be good news without being a good intervention. A patient who takes a medicine may be healthier than one who does not, not because the medicine helps, but because healthier patients are more likely to receive it. Likewise, an action may reveal something favorable about the person who takes it without producing that favorable condition.

**Causal decision theory** (CDT) asks which available action has the best *expected causal consequences*. It contrasts with **evidential decision theory** (EDT), which evaluates an action partly by asking what its occurrence would be evidence about. The distinction matters when the agent’s action is correlated with facts it cannot change: a personality trait, another person’s earlier prediction, or a partner’s independent but similar reasoning.

The central challenge is to make “what the action would cause” precise. The reference article presents CDT through probabilities of counterfactuals and emphasizes that the theory does not itself supply a complete algorithm for calculating them. A causal model provides one useful operational interpretation, but it adds assumptions that must be examined rather than mistaken for consequences of CDT alone.

## 1. From consequences to expected utility

Suppose an agent can choose an action \(a\) from a set \(\mathcal A\). Let \(Y(a)\) denote the outcome that would occur if the agent took \(a\), and let \(u\) assign a utility to each possible outcome. A compact statement of CDT is

\[
a^*\in\operatorname*{arg\,max}_{a\in\mathcal A}
\mathbb E[u(Y(a))\mid E],
\]

where \(E\) is the information available at the decision point. The expectation represents uncertainty both about the circumstances in which the action would be taken and about its effects.

For example, suppose eating an apple yields utility \(10\) if it is good and \(-20\) if it is bad. If the probability that it is good is \(0.8\), then

\[
\mathbb E[u(Y(\text{eat}))]=0.8(10)+0.2(-20)=4.
\]

If the alternative has utility \(3\), eating is preferred. Nothing here requires certainty about the outcome; it requires an assessment of what each action would do in the possible circumstances.

The reference gives Gibbard and Harper’s formulation:

\[
U(a)=\sum_j P(a\mathbin{\Box\!\!\to} O_j)\,D(O_j),
\]

where \(a\mathbin{\Box\!\!\to}O_j\) expresses the counterfactual “if \(a\) were taken, \(O_j\) would occur,” and \(D(O_j)\) is the desirability of outcome \(O_j\). The arrow should not be read as ordinary material implication, nor as the claim that \(a\) *logically necessitates* \(O_j\). It describes an outcome under a hypothetical action, given how the world would otherwise unfold. For a straightforward expected-utility calculation, the outcomes should be mutually exclusive and exhaustive under each action.

The utility function needs to represent everything the agent cares about: money, welfare, fairness, risk, and so on. In particular, “best outcome” need not mean the largest monetary payment. When examples below use money as utility, they assume linear utility in money for simplicity.

## 2. Counterfactual probability is not ordinary conditional probability

EDT instead uses

\[
V_{\mathrm{EDT}}(a)=
\sum_j P(O_j\mid A=a,E)\,u(O_j),
\]

where \(A\) is the action the agent actually takes. This asks: *if I learned that my action was \(a\), how would that news change my beliefs about the outcome?*

CDT asks a different question:

\[
V_{\mathrm{CDT}}(a)=
\sum_j P(Y(a)=O_j\mid E)\,u(O_j).
\]

The distinction is between observing \(A=a\) and considering an intervention that sets the action to \(a\). An observation can be informative about the action’s causes; an intervention need not change those causes.

Imagine that people with a hidden condition \(H\) are more likely to take a treatment and also more likely to recover. If the treatment itself has no effect, then \(P(\text{recover}\mid A=\text{take})\) can exceed \(P(\text{recover}\mid A=\text{decline})\), while

\[
P(Y(\text{take})=\text{recover})
=
P(Y(\text{decline})=\text{recover}).
\]

A causal decision maker does not count the favorable condition as a benefit produced by taking the treatment. Conversely, if the treatment really helps, its downstream effect belongs in the evaluation even if treated patients happen to have worse prognoses.

The reference notes Lewis’s result that probabilities of counterfactual conditionals cannot generally be identified with ordinary conditional probabilities. Gibbard and Harper describe conditions under which the two do coincide, including an independence condition, together with further axioms about conditionals. The practical lesson is more modest: equality is possible, but it cannot simply be assumed.

In a randomized experiment, for instance, treatment assignment may be independent of potential outcomes. Under appropriate assumptions,

\[
P(Y(a)=y\mid E)=P(Y=y\mid A=a,E).
\]

Randomization makes observed differences informative about causal differences. It does not make conditioning and intervention interchangeable in every decision problem.

## 3. An operational interpretation: intervene in a causal model

A useful way to calculate CDT values is to specify a structural causal model. This is an additional modeling proposal, not an algorithm uniquely required by the reference.

Let \(X_1,\ldots,X_n\) be variables determined by equations

\[
X_i=f_i(\operatorname{Pa}_i,\varepsilon_i),
\]

where \(\operatorname{Pa}_i\) are causal parents of \(X_i\), and \(\varepsilon_i\) represents background factors. The model includes an equation for the agent’s action \(A\), as well as equations for variables affected by that action.

To evaluate \(a\):

1. Update beliefs about the background factors and model using the available evidence \(E\).
2. Replace the equation determining \(A\) with \(A:=a\). This is the intervention written \(\operatorname{do}(A=a)\).
3. Leave the other causal equations in place and propagate the consequences.
4. Average utility over the posterior uncertainty about background factors and, if necessary, causal models.

Thus, schematically,

\[
V(a)=\mathbb E[u(Y)\mid \operatorname{do}(A=a),E].
\]

For decision-point evidence, it is safest to think of this as first updating on what is known and then simulating the intervention. Conditioning after an intervention on an event that the intervention itself changes can answer a different question.

The operation severs the usual causal inputs to the action variable; it does **not** sever outgoing effects of the action. If a purchase causes a seller to ship a product, the shipment remains in the simulated consequences. If a predictor has already filled a box, the filling ordinarily remains fixed. Uncertainty about that past filling remains uncertainty—it is not replaced by an assertion that the agent knows its value.

A causal model also forces attention to the description of an action. “Press the button” and “press the button after deliberately disabling the safety system” may have different effects. An intervention that magically sets a single variable may not represent either physically available option. The modeled intervention should correspond as closely as possible to the choice actually under consideration.

## 4. David, charisma, and evidential dependence

The reference’s King David example separates an action’s causal effects from what the action suggests about the agent. David is unsure whether he is charismatic. Uncharismatic kings are both more likely to act unjustly and more vulnerable to successful revolt; the story stipulates that the unjust act itself does not cause revolt.

Write \(H=1\) for uncharismatic, \(A=1\) for summoning Bathsheba, and \(R=1\) for successful revolt. A simplified structure is

\[
H\longrightarrow A,\qquad H\longrightarrow R,
\]

with no arrow \(A\to R\). Observing \(A=1\) can increase \(P(H=1)\), and hence increase \(P(R=1\mid A=1)\). But setting \(A:=1\) leaves \(H\) and its causal effect on revolt unchanged. Under those stipulations,

\[
P(R=1\mid \operatorname{do}(A=1))
=
P(R=1\mid \operatorname{do}(A=0)).
\]

If summoning provides David a benefit and there are no other relevant costs, CDT recommends summoning. EDT may recommend abstaining if abstention is sufficiently strong evidence of charisma.

The conclusion depends on the toy problem’s assumptions. If summoning genuinely angers subjects, harms Bathsheba, or violates a moral commitment represented in David’s utility, those consequences must be counted. CDT does not authorize ignoring them; it denies only the stipulated inference from correlation with revolt to causing revolt.

## 5. Newcomb’s problem: a fixed prediction and a correlated choice

Newcomb’s problem sharpens the same contrast. A transparent box contains \$1,000. An opaque box contains \$1 million if a predictor earlier predicted that the player would take only the opaque box, and nothing otherwise. The player chooses either one box or both.

Let \(B\) be the amount already in the opaque box. At the moment of choice, suppose the player’s action has no causal influence on \(B\). Then

\[
V_{\mathrm{CDT}}(\text{one})=\mathbb E[B\mid E],
\qquad
V_{\mathrm{CDT}}(\text{two})=\mathbb E[B\mid E]+1000.
\]

Two-boxing is better by \$1,000 in every fixed state of the opaque box. This is the familiar causal dominance argument.

Yet suppose, as an illustrative assumption, that conditional on one-boxing the opaque box is full with probability \(0.99\), and conditional on two-boxing it is full with probability \(0.01\). Then EDT calculates

\[
V_{\mathrm{EDT}}(\text{one})=0.99(1{,}000{,}000)=990{,}000,
\]

\[
V_{\mathrm{EDT}}(\text{two})=0.01(1{,}000{,}000)+1000=11{,}000.
\]

It recommends one-boxing. The predictor’s stated overall accuracy alone does not determine these two conditional probabilities; the example supplies them to make the contrast explicit.

The criticism of CDT is not that a two-boxer gets only \$1,000 in every possible instance: a two-boxer with a full opaque box gets \$1,001,000. Rather, reliable prediction makes that favorable state rare among actual two-boxers. The dispute is whether the agent should act on the evidential connection between choice and earlier prediction, or treat the already-set contents as invariant under the current intervention.

The same structure can appear with a like-minded opponent in a prisoner’s dilemma. If the opponent’s simultaneous choice is correlated with yours but is not caused by your present choice, CDT does not count the correlation itself as a causal effect. If, however, the opponent observes and responds to your move, or a prior commitment influences the opponent, those are causal pathways and belong in the model.

## 6. Actions, policies, and the time of decision

A recommendation can change when the available choice changes. Choosing an action now is different from choosing an earlier commitment or a policy for responding to later information.

Suppose a policy \(\pi\) maps observations \(x\) to actions: \(A=\pi(x)\). A causal evaluation of an available policy can be written

\[
V(\pi)=\mathbb E[u(Y(\pi))\mid E].
\]

Here the counterfactual \(Y(\pi)\) must include the effects of installing or committing to the policy. If a predictor observes a binding commitment before filling the opaque box, committing to one-box may causally produce a full box. In that modified situation, CDT can favor the commitment even though it would favor taking both boxes at a later point when the contents are already fixed and both actions remain available.

This is not a proof that CDT recommends one-boxing in the original Newcomb problem. Merely *imagining* a different policy at the final decision point does not establish a causal route to an earlier prediction. One must say what intervention is available, when it occurs, and whether it is observable or otherwise affects the predictor. A genuinely binding device changes the later feasible action set; an unenforceable intention might not.

For sequential decisions more generally, a practical method is to represent observations, actions, and consequences at their respective times. Evaluate an available policy by intervening on the mechanism that selects future actions, while preserving causal links from earlier choices to later information and behavior. Whether a plan remains desirable when reconsidered later is a separate question. The reference reports criticisms involving **diachronic Dutch books**: arrangements exploiting changes in a causal agent’s preferences over time. Their force depends on the details of the opportunities and commitments, rather than on a rule that planning is always inconsistent with CDT.

## 7. Information about one’s own decision

One might object that a person’s inclination to act is itself evidence. CDT need not ignore it. If David learns independently that he has a strong unjust impulse, that observation can update his probability of being uncharismatic *before* he evaluates his options. Likewise, a medical decision maker who notices symptoms should condition on them, even if those symptoms are correlated with the treatment they are inclined to seek.

The delicate case is information acquired through deliberation itself. What if David comes to believe that he will summon Bathsheba precisely because he judges summoning best? Does that belief provide new evidence about his character, which may change the judgment? The reference reports Joyce’s view that CDT can take information about one’s inclinations or likely behavior into account. It also reports Egan’s criticism that holding initial beliefs about causal dependencies fixed can lead to irrational choices.

These claims need not conflict: an observed inclination can be evidence, while the treatment of a conclusion reached during the very decision being evaluated remains controversial. A causal model must specify what the agent observes, how reliable that observation is, and how it relates to the action mechanism. It should not automatically identify “suppose I choose \(a\)” with “I have learned that I will choose \(a\).”

The *Psychopath Button* illustrates the tension. Paul believes that pressing a button will kill all psychopaths, strongly prefers living with psychopaths to dying, and thinks only psychopaths would press it. If Paul’s current probability of being a psychopath is low and the benefit of eliminating psychopaths is sufficiently high, a simple causal calculation can favor pressing: his type is already fixed, and pressing does not make him a psychopath, although it kills him if he is one. Conditionalizing on the act, by contrast, might make his being a psychopath very likely.

Whether Paul’s contemplating or being inclined to press should already raise his probability of being a psychopath is an important further question. The example is an alleged counterexample to CDT, not a derivation that every causal decision maker must press under every specification.

## 8. The adversarial offer

Another difficulty concerns an opponent who has predicted the agent’s decision. In the reference’s adversarial offer, two boxes cost \$1 each; the buyer may buy one or neither. Yesterday the seller put \$3 in every box she predicted the buyer would not acquire. Both parties believe her prediction is correct with probability \(0.75\).

At least one box contains \$3: if the seller predicted a purchase, the other box is filled; if she predicted no purchase, both are filled. Holding these past placements fixed, the two boxes therefore have total expected contents of at least \$3. At least one box has expected contents of at least \$1.50, so buying the better box has causal expected profit of at least \$0.50.

But if the seller accurately predicts the box actually purchased with probability \(0.75\), that box is empty on those occasions. On the remaining occasions it contains \$3, so the buyer’s average profit from purchasing is

\[
0.25(3)-1=-0.25.
\]

The argument compares an intervention-based assessment of a box with the distribution of contents *conditional on actually buying it*. The apparent loss is therefore not an arithmetic error: it exploits the correlation between prediction and purchase that the causal intervention breaks. Precisely how an agent forms stable beliefs about its own purchase, and whether randomization or prior commitment changes the prediction, are further modeling questions.

## 9. Where the counterfactuals come from

The causal-model method is useful only to the extent that its equations and probabilities are justified. Observational data alone may not distinguish a direct effect from a common cause. Nor is every counterfactual empirically identifiable. Agents may have to combine experiments, background science, expert judgment, and uncertainty over competing models:

\[
V(a)=\sum_m P(m\mid E)\,
\mathbb E_m[u(Y(a))\mid E].
\]

This expression makes causal uncertainty explicit; it does not eliminate it.

The reference also describes Lewis’s **imaging** proposal. Roughly, to evaluate a counterfactual, move probability mass from each possible world to a sufficiently close world where the action occurs, then examine the outcome there. But “closest” requires a substantive account of what stays the same and what changes. A world in which a decision differs might differ in the agent’s prior character, or instead in some local feature of the decision process. Different similarity rules can yield different verdicts. The reference notes a further concern that specifying what one would believe under the hypothetical can itself invite another conditional question.

A practical discipline for unfamiliar cases is therefore:

1. **Specify the decision point and feasible alternatives**, including any genuine commitments or policies.
2. **List available evidence and relevant utilities**, including moral and nonmonetary consequences.
3. **Draw the proposed causal dependencies**, distinguishing common causes, past predictions, and downstream effects.
4. **Model each feasible intervention**, preserving the causal mechanisms not changed by it.
5. **Average over uncertainty** about states and mechanisms, and compare expected utilities.
6. **Check sensitivity** to disputed assumptions, especially whether the action can affect an apparently fixed fact and whether new evidence about the agent’s own disposition is available.

This procedure makes CDT usable without pretending that the philosophical disputes have been resolved. In difficult cases, the answer may be conditional: *given this causal model and these credences, choose \(a\); under another plausible model, choose \(b\).*

## Conclusion

CDT evaluates an option by its expected consequences under a counterfactual intervention, not merely by the news that taking it would convey. That principle explains its treatment of confounding, its usual two-box recommendation in Newcomb’s problem, and its sensitivity to the timing of commitments. Its hardest questions concern how to construct the relevant counterfactuals and how to use information about the agent’s own likely behavior. A careful causal model clarifies those questions, even where it cannot settle them.

## References

- Wikipedia contributors, “[Causal decision theory](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528),” revision 1381555528.
- Gibbard, A., and Harper, W. L. (1981), “Counterfactuals and two kinds of expected utility.”
- Lewis, D. (1981), “[Causal decision theory](https://doi.org/10.1080/00048408112340011).”
- Egan, A. (2007), “[Some counterexamples to causal decision theory](https://doi.org/10.1215/00318108-2006-023).”
- Oesterheld, C., and Conitzer, V. (2021), “[Extracting Money from Causal Decision Theorists](https://doi.org/10.1093/pq/pqaa086).”