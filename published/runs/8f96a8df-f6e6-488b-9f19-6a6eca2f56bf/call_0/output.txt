# Causal Decision Theory: Choosing What to Bring About

A decision can be good news without being a good intervention. Discovering that you have exercised today might be evidence of good health, even when the exercise itself has only a small immediate benefit. Conversely, taking medicine may indicate illness while causally improving your prospects. Causal decision theory, or **CDT**, makes this distinction central: evaluate actions by what they would bring about, not merely by what their occurrence would reveal.

The supplied reference article presents CDT as maximizing expected utility calculated from probabilities of counterfactuals. This is a substantive principle, but not a complete computational procedure. Applying it requires judgments about causation, uncertainty, available actions, and the information held fixed when comparing alternatives.

This essay develops the principle and then supplies an explicit causal-model interpretation. That interpretation is an operational reconstruction, not a claim that every version of CDT uses the same formal machinery.

## 1. Expected utility under a counterfactual supposition

Let \(\mathcal A\) be the available actions, \(I\) the agent’s current information, and \(\mathcal O=\{o_1,\ldots,o_n\}\) a mutually exclusive, exhaustive collection of outcomes. Let \(u(o_j)\) represent the agent’s utility for outcome \(o_j\).

An outcome must include everything relevant to the decision: benefits, costs, harms to others, risks, and any value attached to the action itself. CDT does not require selfish preferences or monetary utility.

Write \(O_a\) for the outcome that would occur if the agent performed action \(a\). A useful formulation of causal expected utility is

\[
V_C(a\mid I)
=
\sum_j P(O_a=o_j\mid I)\,u(o_j).
\]

CDT recommends an action in

\[
\operatorname*{arg\,max}_{a\in\mathcal A}V_C(a\mid I).
\]

The reference gives the Gibbard–Harper formulation

\[
U(A)=\sum_j P(A\to O_j)D(O_j).
\]

Here the arrow should be understood as expressing a **counterfactual or subjunctive conditional**, not material implication. The question is what would happen were \(A\) performed. It is not whether “either \(A\) is false or \(O_j\) is true,” nor whether the outcome follows with logical necessity.

Evidential decision theory instead evaluates

\[
V_E(a\mid I)
=
\sum_j P(O=o_j\mid A=a,I)\,u(o_j).
\]

The difference is between:

- **Conditioning:** learning that \(A=a\) occurred.
- **Counterfactual intervention:** considering what would happen if \(a\) were performed.

Learning an action occurred can change beliefs about its causes. Performing it need not change those causes.

The reference discusses Lewis’s work showing that probabilities of conditionals cannot generally be identified with ordinary conditional probabilities. For practical decision-making, the important lesson is that the two quantities require separate justification. They can coincide, but should not be equated automatically.

## 2. Making the counterfactuals operational

How should \(P(O_a=o_j\mid I)\) be calculated?

The reference explicitly identifies this as an incompleteness in CDT: the maximization rule alone does not specify an algorithm for counterfactual probabilities. One operational answer is to provide a **structural causal model**.

Suppose the world contains variables satisfying equations

\[
X_i=f_i(\operatorname{Pa}_i,W_i),
\]

where \(\operatorname{Pa}_i\) are the direct causal parents of \(X_i\), and the \(W_i\) encode background circumstances. For simplicity, assume an acyclic model with well-defined solutions.

To evaluate action \(a\):

1. Replace the equation generating the action variable \(A\) by \(A=a\).
2. Leave the other structural equations unchanged.
3. Propagate the consequences.
4. Average over uncertainty about the background circumstances.

If the causal model itself is uncertain, represent that uncertainty by a variable \(M\). Then

\[
V_C(a\mid I)
=
\sum_{m,w}P(m,w\mid I)\,
u\bigl(O_a(m,w)\bigr).
\]

The crucial feature is that the weights \(P(m,w\mid I)\) remain the same across the hypothetical actions. The intervention changes the action and its consequences, not the agent’s current probability distribution over everything upstream.

For appropriately situated information \(I\), this is commonly written

\[
V_C(a\mid I)
=
\mathbb E[u(O)\mid \operatorname{do}(A=a),I].
\]

The notation needs care if \(I\) includes observations affected by the intervention. The more general procedure is to infer background circumstances from the actual evidence first, then evaluate the counterfactual in each inferred circumstance.

This does **not** mean freezing the whole world. Descendants of the action must change when its causal effects require them to change. If taking medicine changes recovery, recovery is recomputed. If a latent illness affects both medication use and recovery, the intervention does not itself remove that illness.

Nor does CDT eliminate uncertainty about causation. If two causal models are plausible, their different predictions should both enter the expectation. Observational frequencies alone may not identify which model is correct; experiments, substantive knowledge, or additional assumptions may be needed.

The reference also describes Lewis’s **imaging** proposal: move probability from each possible world to a suitable nearby world where the contemplated action occurs. In deterministic notation,

\[
P_a(o)=\sum_w P(w)\,\mathbf 1\{O(w_a)=o\}.
\]

But “nearby” needs a substantive interpretation. A structural model supplies one by retaining background conditions while replacing the action equation. This resolves the computational question only after causal assumptions have been supplied; it does not derive those assumptions from probability theory alone.

## 3. A common cause is not a controllable consequence

The reference’s King David example illustrates CDT’s central motivation. David’s fixed character influences both whether he summons Bathsheba and whether a revolt succeeds. By stipulation, summoning her does not itself affect revolt.

Consider a numerical version. Let \(C\) mean that David is charismatic, with

\[
P(C)=\tfrac12.
\]

Suppose

\[
P(S\mid C)=0.1,\qquad P(S\mid\neg C)=0.9,
\]

where \(S\) means summoning Bathsheba. Also suppose

\[
P(R\mid C)=0.1,\qquad P(R\mid\neg C)=0.8,
\]

where \(R\) means successful revolt. Conditional on character, summoning supplies no further information about revolt and has no causal effect on it.

The causal structure is

\[
S\leftarrow C\rightarrow R.
\]

Let summoning provide utility \(5\), and revolt impose a loss of \(100\). Under either intervention, the probability of revolt is

\[
P(R\mid\operatorname{do}(S))
=
P(R\mid\operatorname{do}(\neg S))
=
0.45.
\]

Thus

\[
V_C(S)=5-100(0.45)=-40,
\qquad
V_C(\neg S)=-45.
\]

CDT favors summoning.

Conditioning gives different results:

\[
P(R\mid S)=0.73,\qquad P(R\mid\neg S)=0.17.
\]

EDT therefore assigns values \(-68\) and \(-17\), favoring abstention.

The disagreement is not about whether revolt matters. It concerns whether David can improve his character, and thereby his political prospects, simply by performing an action associated with good character.

The example’s moral assumptions are artificial. If wrongdoing, coercion, or harm makes summoning undesirable overall, those costs belong in utility. CDT does not independently endorse the action; its recommendation depends on the stipulated utilities and causal structure.

## 4. Newcomb’s problem: dominance versus predictive success

In Newcomb’s problem, a transparent box contains \(\$1{,}000\). An opaque box contains either \(\$1{,}000{,}000\) or nothing. A predictor has already filled the opaque box if it predicted that the player would take only that box, and left it empty otherwise.

Let \(B\in\{0,10^6\}\) be the opaque box’s content. The actions are:

- \(a_1\): take only the opaque box;
- \(a_2\): take both boxes.

Assume utility is linear in money. Under the ordinary causal interpretation, the present action does not change the already determined content. Therefore,

\[
V_C(a_1)=\mathbb E[B\mid I],
\]

\[
V_C(a_2)=\mathbb E[B\mid I]+1000.
\]

Two-boxing wins by exactly \(\$1{,}000\), regardless of the current probability that the opaque box is full.

This is a dominance argument: in each fixed background circumstance, taking both yields more.

EDT reasons differently. On a common symmetric specification,

\[
P(B=10^6\mid a_1)=0.99,
\qquad
P(B=10^6\mid a_2)=0.01.
\]

It then assigns monetary expectations

\[
V_E(a_1)=990{,}000,
\qquad
V_E(a_2)=11{,}000.
\]

These conditional probabilities are additional assumptions; merely saying “the predictor is 99% accurate” does not uniquely determine every conditional probability.

The philosophical disagreement is genuine. CDT asks which action improves the outcome while holding fixed the background circumstances that generated the prediction. Its critics emphasize that one-boxers reliably receive more money.

Neither side should misdescribe the other. CDT does not deny the predictive correlation. It denies that the correlation is a causal benefit of the present action. And two-boxing does not guarantee receiving only \(\$1{,}000\): the predictor can be wrong.

The same issue appears in a prisoner’s dilemma against a highly similar agent. If the other player’s action is correlated with yours but not causally influenced by it, standard act-CDT holds that action fixed across interventions. Logical or psychological similarity alone is not treated as a causal channel.

## 5. Actions, policies, and commitment

A policy specifies actions across possible information states. Let

\[
\pi_t(h_t)
\]

give the action at time \(t\) after history \(h_t\).

A natural causal extension evaluates a policy by replacing the relevant decision equations with

\[
A_t=\pi_t(H_t)
\]

and computing expected utility under the resulting process:

\[
V_C(\pi\mid I)
=
\mathbb E\!\left[u(O^\pi)\mid I\right].
\]

This is an operational proposal extending the article’s basic rule; the supplied source does not settle every issue about policy choice.

Three distinctions matter.

**First, policy adoption must be feasible.** Imagining a policy is not the same as possessing a mechanism that reliably implements it.

**Second, earlier commitments can have causal effects unavailable to later actions.** Suppose a Newcomb predictor observes a binding commitment before filling the boxes. Adopting a one-boxing commitment can then causally influence the prediction and favorably affect the box’s contents. Once filling is complete, the present bodily action has no such influence.

**Third, intervening on a policy is not automatically equivalent to intervening on its eventual action.** Other agents may observe the policy, react to it, or predict behavior from its implementation.

Consequently, a causal agent can favor an earlier commitment whose prescribed action it would not choose if reconsideration later became possible. The existence of commitment opportunities does not by itself resolve the dispute about the later choice.

Randomization also requires a causal model. If a private randomizer is independent of the background circumstances and has no additional effects, then

\[
V_C(q)=\sum_a q(a)V_C(a).
\]

Such mixing cannot outperform the best pure action. But if others respond to the announced distribution or can forecast the randomizer, that simple calculation may no longer describe the decision.

## 6. Self-knowledge and unstable deliberation

The reference highlights Egan’s objection that CDT can recommend actions while holding fixed beliefs that taking those actions would undermine.

The “psychopath button” makes the concern vivid. Paul can press a button that kills all psychopaths. He values their removal but strongly prefers remaining alive. He also believes that only a psychopath would press.

Let:

- \(p=P(H\mid I)\), where \(H\) means Paul is a psychopath;
- \(b>0\) be the benefit from pressing if he survives;
- \(L>0\) be the loss from pressing if he is killed.

Normalize not pressing to utility zero. A simplified causal calculation gives

\[
V_C(\text{press}\mid I)=(1-p)b-pL.
\]

Pressing is recommended exactly when

\[
p<\frac{b}{b+L}.
\]

If Paul initially regards himself as very unlikely to be a psychopath, this calculation can recommend pressing. Yet becoming convinced that he will press may be powerful evidence that he is one.

A crucial distinction follows:

> Holding beliefs fixed across hypothetical interventions does not require refusing to update on actual evidence acquired during deliberation.

The reference reports Joyce’s defense that CDT can incorporate evidence about what the agent is inclined or likely to do. If Paul actually discovers a strong inclination to press, that observation can raise \(P(H\mid I)\), changing the recommendation.

However, this leaves a difficult question: **when does deliberation produce evidence rather than merely entertain an alternative?** Updating on every imagined action would collapse the causal comparison toward an evidential one. Never updating on genuine discoveries about one’s dispositions would discard relevant information.

A reasonable operational discipline is to distinguish:

1. actual observations about one’s psychology or decision process;
2. hypothetical interventions used to compare actions.

Update on the former, not merely on the latter. This is a useful proposal, but not a complete resolution of cases where the decision process itself becomes evidence. The reference presents these issues as contested, not as a settled refutation or vindication of CDT.

## 7. Can causal choice be systematically exploitable?

The reference’s “Adversarial Offer” sharpens the performance objection.

A seller offers two boxes at \(\$1\) each; the buyer may purchase at most one. Yesterday, the seller put \(\$3\) in every box she predicted the buyer would not acquire.

At least one box contains \(\$3\). Holding current beliefs about contents fixed across purchase interventions, the sum of the boxes’ expected contents is at least \(\$3\). Hence at least one has expected contents of at least \(\$1.50\), giving a positive causal expected net return.

Straightforward CDT therefore recommends buying some box.

But suppose the seller predicts the resulting purchase correctly with probability \(0.75\). When correct, the purchased box is empty. When incorrect, it contains \(\$3\). The buyer’s realized expected net return is

\[
0.75(-1)+0.25(2)=-0.25.
\]

The buyer appears predictably exploitable.

This calculation depends on the stipulated predictive success applying to the buyer’s resulting behavior. Introducing an independently hidden randomizer, for example, may invalidate that stipulation.

Nevertheless, the case exposes an important tension: maximizing causal value at a decision point need not maximize the observed earnings of agents using that decision procedure in prediction-sensitive environments. The reference cites related arguments about voluntary losses and diachronic Dutch books. Whether these demonstrate irrationality, or instead exploit an inappropriate performance criterion, remains disputed.

## 8. A practical procedure

For an unfamiliar problem, a disciplined CDT analysis is:

1. **Specify the decision point and feasible alternatives.** Distinguish present actions from earlier commitments.
2. **Define complete outcomes and utilities.** Include all relevant consequences, not just salient rewards.
3. **Record current evidence.** Separate genuine observations from hypothetical suppositions.
4. **Model causal dependencies.** Identify common causes, downstream effects, and uncertainty about mechanisms.
5. **Evaluate each intervention.** Keep current background probabilities fixed while propagating causal consequences.
6. **Maximize expected utility.** Check ties, sensitivity to uncertain assumptions, and any subsequent opportunities to revise.

When the answer turns on a disputed causal model, the responsible conclusion is conditional: *under these counterfactual assumptions, CDT recommends this action*.

### Sources

The principal source is the supplied Wikipedia article, [“Causal decision theory,” revision 1381555528](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528), by Wikipedia contributors, CC BY-SA 4.0. Relevant works cited there include:

- Gibbard and Harper (1981), “Counterfactuals and two kinds of expected utility.”
- Lewis (1981), “Causal decision theory.”
- Egan (2007), “Some counterexamples to causal decision theory.”
- Joyce (2012), “Regret and instability in causal decision theory.”
- Oesterheld and Conitzer (2021), “Extracting Money from Causal Decision Theorists.”

## Conclusion

CDT’s central insight is that evidence and influence are different resources. Rational action, on its account, maximizes expected utility under a causal counterfactual rather than ordinary conditioning. Its strength is a precise way to avoid mistaking favorable symptoms for controllable benefits. Its unresolved difficulties concern how counterfactuals are constructed, how deliberation supplies self-evidence, and whether locally attractive causal choices remain defensible against reliable predictors. Applying CDT well therefore requires both an expectation calculation and a justified account of what the agent can actually change.