# Causal Decision Theory: Choosing What to Change, Not What to Believe

An action can be good news without being a good intervention. A favorable medical diagnosis predicts recovery, but producing a favorable-looking test result does not cure the disease. Causal decision theory, or **CDT**, makes this distinction central to rational choice: choose the available action whose **expected causal consequences** have the greatest utility.

The contrast is with evidential decision theory, or **EDT**, which evaluates outcomes conditional on the action being taken. Usually the two agree. They diverge when actions provide information about circumstances they cannot change.

This essay develops CDT’s counterfactual formulation, then gives an operational interpretation using causal models. The supplied reference presents the basic theory and its controversies; the structural-model machinery and numerical examples below are explanatory additions, not a claim that every causal decision theorist accepts one implementation.

## 1. Expected utility over counterfactual outcomes

Let \(\mathcal A\) be a finite set of feasible actions, \(I\) the agent’s current information, and \(O_1,\ldots,O_n\) a mutually exclusive, exhaustive collection of outcomes. Let \(u(O_j)\) represent their utilities.

The reference gives Gibbard and Harper’s formulation:

\[
U(A)=\sum_j P(A\to O_j)D(O_j).
\]

The arrow should be understood as a **counterfactual conditional**, not material implication or a claim of logical necessity. Roughly, \(A\to O_j\) says: *if the agent were to perform \(A\), outcome \(O_j\) would occur*.

For clarity, write \(O_a\) for the outcome that would result from performing action \(a\). Then

\[
V_C(a\mid I)
=\mathbb E[u(O_a)\mid I]
=\sum_j P(O_a=O_j\mid I)u(O_j),
\]

and CDT recommends

\[
a^*\in\arg\max_{a\in\mathcal A}V_C(a\mid I).
\]

Uncertainty remains inside the expectation. If an apple might be good or spoiled, CDT averages the consequences of eating it across those possibilities. “Choose what causes the best outcome” does not mean “choose what guarantees success.”

EDT instead uses

\[
V_E(a\mid I)
=\mathbb E[u(O)\mid A=a,I].
\]

The difference is between two questions:

- **Causal:** What would happen if I made \(a\) occur?
- **Evidential:** What should I expect upon learning that I performed \(a\)?

Learning about an action can reveal something about its causes. Intervening on the action need not change those causes.

Utilities must include everything the agent values: money, health, effects on others, costs of acting, and perhaps moral considerations. CDT supplies a rule for comparing actions, not a substantive account of what is valuable. It also assumes that the relevant expectations exist; infinite utilities and other failures of expected-utility representation require additional treatment.

## 2. Making counterfactuals operational

The reference identifies an important incompleteness: CDT alone does not specify an algorithm for calculating counterfactual probabilities. A useful operational interpretation employs a **structural causal model**.

Suppose variables satisfy equations

\[
X_k=f_k(\operatorname{Pa}_k,U_k),
\]

where \(\operatorname{Pa}_k\) denotes the direct causes of \(X_k\), and \(U_k\) represents background factors. Uncertainty is represented by a probability distribution over those factors.

To evaluate action \(a\), replace the equation governing the action variable \(A\) by

\[
A:=a.
\]

Keep the other mechanisms unchanged and solve the resulting model. This intervention is written \(\operatorname{do}(A=a)\).

For example, consider

\[
C\longrightarrow A,\qquad C\longrightarrow Y,\qquad A\longrightarrow Y.
\]

Here \(C\) affects both the agent’s action and the outcome \(Y\). Observing \(A=a\) provides information about \(C\). Intervening on \(A\) removes its dependence on \(C\), while retaining both \(C\)’s influence on \(Y\) and any genuine effect of \(A\) on \(Y\).

With current, pre-action information \(I\), the causal value becomes

\[
V_C(a\mid I)
=\sum_y P(y\mid\operatorname{do}(A=a),I)u(y).
\]

When \(C\) contains sufficient pre-action common causes and the usual identification assumptions hold,

\[
P(y\mid\operatorname{do}(A=a),I)
=\sum_c P(y\mid a,c,I)P(c\mid I).
\]

By contrast,

\[
P(y\mid A=a,I)
=\sum_c P(y\mid a,c,I)P(c\mid A=a,I).
\]

The crucial difference is the weighting of background circumstances. CDT uses the agent’s current beliefs about \(C\); conditioning on the hypothetical action can reweight those circumstances.

This does **not** mean holding everything fixed. Consequences downstream of the action must change according to their mechanisms. Only factors outside the action’s causal influence retain their appropriate distributions.

Nor does uncertainty about causation disappear. If \(M\) indexes possible causal models, one natural extension is

\[
V_C(a\mid I)
=\sum_m P(M=m\mid I)
\,\mathbb E_m[u(O_a)\mid I].
\]

The model probabilities incorporate actual evidence, but are not automatically replaced by \(P(M=m\mid A=a,I)\) when merely considering \(a\).

The reference also discusses Lewis’s **imaging** approach: move probability from each possible world to a nearby world where the proposed action occurs. Structural interventions give one precise interpretation of “nearby”: preserve background circumstances and unchanged mechanisms, while replacing the action mechanism. But that interpretation adds substantive assumptions. Which mechanisms remain fixed, what counts as feasible, and whether counterfactuals should “backtrack” to different past circumstances are not settled by expected-utility maximization itself.

## 3. Common causes: the King David example

The reference’s King David example illustrates the difference between evidence and influence.

David wants to summon Bathsheba. His unknown charisma affects both his propensity to act unjustly and the probability of a successful revolt. By stipulation, summoning Bathsheba does not itself cause a revolt.

For a numerical illustration, suppose David assigns equal probability to being charismatic or uncharismatic. The revolt probabilities are \(0.1\) and \(0.8\), respectively. His probability of summoning Bathsheba is \(0.1\) if charismatic and \(0.9\) otherwise.

Before treating his hypothetical choice as evidence,

\[
P(\text{revolt}\mid I)=\tfrac12(0.1)+\tfrac12(0.8)=0.45.
\]

Under the stipulated causal model, either action leaves that probability unchanged.

But Bayes’s rule gives

\[
P(\text{uncharismatic}\mid\text{summon},I)=0.9,
\]

so

\[
P(\text{revolt}\mid\text{summon},I)=0.73.
\]

Similarly,

\[
P(\text{revolt}\mid\text{abstain},I)=0.17.
\]

Suppose summoning provides utility \(5\), and revolt costs \(100\). CDT sees a gain of \(5\) with no change in revolt risk. EDT sees a utility difference of

\[
5-100(0.73-0.17)=-51
\]

and recommends abstaining.

CDT’s lesson is that David cannot acquire charisma by choosing an action characteristic of charismatic kings. This is not a moral endorsement of his conduct: adding moral disutility could reverse the recommendation. It also depends on the stipulated causal claim. If the injustice really provokes revolt, that causal pathway must be included.

## 4. Newcomb’s problem and causal dominance

In Newcomb’s problem, a transparent box contains \(\$1{,}000\). An opaque box contains either \(\$1{,}000{,}000\) or nothing. A predictor has already filled the opaque box: it is full if the predictor predicted that the agent would take only that box, and empty if the predictor predicted that the agent would take both.

Let \(B\in\{0,1{,}000{,}000\}\) be the opaque box’s contents. Assuming utility is linear in money,

\[
O_{\text{one}}=B,\qquad
O_{\text{two}}=B+1{,}000.
\]

If the present action cannot change the earlier prediction or the contents, then

\[
V_C(\text{two}\mid I)-V_C(\text{one}\mid I)=1{,}000.
\]

Two-boxing is better in every fixed-content causal scenario. This is a dominance argument; the agent need not know the probability that the opaque box is full.

For an evidential comparison, suppose specifically that

\[
P(B=1{,}000{,}000\mid\text{one},I)=0.99,
\]

and

\[
P(B=1{,}000{,}000\mid\text{two},I)=0.01.
\]

Then

\[
V_E(\text{one})=\$990{,}000,
\qquad
V_E(\text{two})=\$11{,}000.
\]

These conditional probabilities are stronger specifications than merely saying that the predictor has 99% aggregate accuracy.

The disagreement is not that CDT fails to recognize the correlation. It recognizes it but denies that choosing differently now changes the already-filled box.

This also explains why the controversy persists. One-boxers generally become richer, yet two-boxing appears to improve the payoff with the contents held fixed. Critics question whether that counterfactual comparison captures rational choice in a predictor-controlled environment. Defenders distinguish choosing an advantageous causal intervention from belonging to an advantageous predictive category.

## 5. Policies, commitments, and randomization

An action is not always the right unit of analysis. An agent may instead choose a **policy**: a rule mapping future information histories to actions.

For a finite sequence of decisions, write

\[
\pi=(\pi_1,\ldots,\pi_T),
\qquad A_t=\pi_t(H_t),
\]

where \(H_t\) is the information available at time \(t\). A causal policy value is

\[
V_C(\pi\mid I)=\mathbb E[u(T^\pi)\mid I],
\]

where \(T^\pi\) is the trajectory generated by actually installing and following the policy.

This is a natural extension of CDT, but it requires specifying what “installing” means. A policy might be enforced by a contract, implemented in software, publicly announced, or merely intended. Those are different causal interventions.

Suppose, before a Newcomb predictor acts, the agent can install a visible, reliable commitment to one-box. If the commitment causes the predictor to fill the opaque box, CDT can favor commitment. Later, after prediction and filling, it favors taking both boxes if both remain available.

There is no contradiction between those evaluations: they concern interventions at different times with different causal powers. There can nevertheless be a practical problem of **dynamic consistency**. An earlier plan may be valuable only if the agent cannot or will not revise it later. Commitment costs and enforceability therefore matter.

Merely describing a present act as part of a policy does not give it influence over the past. To justify a policy-level causal advantage, the model needs an actual pathway from policy installation to the relevant response.

For a one-shot decision with a private randomizer that has no additional effects, randomization is linear:

\[
V_C(\mu)=\sum_a\mu(a)V_C(a).
\]

Thus randomizing cannot outperform the best pure action under a fixed causal distribution. It can matter when other agents respond to the randomization mechanism, or when a randomized policy changes future strategic interactions.

## 6. Self-knowledge and challenges to fixed-belief evaluation

The difficult cases arise when the agent’s own action is powerful evidence about a hidden characteristic.

The reference discusses Egan’s **Psychopath Button**. Paul can press a button that kills all psychopaths. He would prefer a world without psychopaths, but strongly prefers remaining alive. He also believes that almost only psychopaths would press.

Let \(p\) be Paul’s current probability of being a psychopath. Normalize not pressing to utility zero. Suppose pressing gives utility \(g>0\) if he is not a psychopath and utility \(-L\) if he is. Then

\[
V_C(\text{press})=(1-p)g-pL.
\]

CDT recommends pressing when

\[
p<\frac{g}{g+L}.
\]

EDT instead uses

\[
r=P(\text{psychopath}\mid\text{press},I),
\]

which may be much larger than \(p\), and evaluates pressing as \((1-r)g-rL\).

The example is therefore not an unconditional theorem that CDT endorses pressing. Its force depends on low prior self-risk, strong action–type correlation, and the utilities.

Egan’s objection, as reported by the reference, concerns holding fixed initial beliefs about causal dependencies even when the proposed choice seems to undermine those beliefs. The reference also reports Joyce’s response that CDT can incorporate information about what the agent is inclined or likely to do.

A reasonable operational distinction is:

- Actual introspective evidence—such as noticing a strong desire to press—can update \(p\).
- Merely entertaining the intervention “press” does not, by itself, constitute that evidence.

This distinction is useful but incomplete. Deliberation can itself reveal dispositions, and an agent may need to revise beliefs while deciding. The reference does not establish one universally accepted procedure for this process.

### The adversarial offer

The reference presents another challenge. A seller offers two boxes, each costing \(\$1\). Yesterday she put \(\$3\) in every box she predicted the buyer would **not** acquire. The buyer may purchase one box or neither.

At least one box contains \(\$3\). If \(q_L,q_R\) are the buyer’s current probabilities that the boxes contain money, then

\[
q_L+q_R\geq1.
\]

Because buying now does not change their contents,

\[
V_C(L)=3q_L-1,\qquad V_C(R)=3q_R-1.
\]

Consequently,

\[
\max\{V_C(L),V_C(R)\}\geq0.5,
\]

whereas declining gives zero. The straightforward causal evaluation recommends buying.

Yet suppose the predictor is correct with probability \(0.75\) for the resulting purchasing behavior. The purchased box is then empty with probability \(0.75\), giving average net profit

\[
0.25(3)-1=-\$0.25.
\]

The causal arithmetic and the poor observed performance use different comparisons: intervention values under fixed beliefs about contents, versus outcomes correlated with the predictor’s successful anticipation.

Critics regard this as evidence against CDT’s normative adequacy. Defenders must explain why the intervention comparison remains appropriate, or refine the treatment of deliberation and information. The source reports related money-loss and Dutch-book arguments; their existence should not be mistaken for an uncontested resolution.

## 7. A procedure for unfamiliar problems

A disciplined application of CDT can proceed as follows.

**First, identify the decision and its timing.** Are you choosing an immediate action, an enforceable commitment, or a future policy? What remains causally changeable?

**Second, specify utilities and feasible alternatives.** Include costs, side effects, and outcomes that are easy to overlook.

**Third, separate mechanisms from correlations.** Ask why the action predicts the outcome. Is there a causal pathway, a common cause, or a predictor responding to earlier evidence?

**Fourth, evaluate interventions.** For each alternative, change the relevant action mechanism and propagate its consequences. Do not change upstream circumstances simply to make the action more statistically typical.

**Fifth, average using current evidence.** Include genuine observations about dispositions and causal structure. Keep separate the evidence actually obtained and the hypothetical action being evaluated.

**Finally, test sensitivity.** If reasonable causal models recommend different actions, report the dependence rather than presenting CDT as delivering a model-free answer.

A practical warning follows: causal probabilities may not be identifiable from observational frequencies alone. Experiments, substantive causal knowledge, or explicit assumptions may be necessary.

## Sources and further reading

The main source is Wikipedia contributors, [“Causal decision theory,” supplied revision 1381555528](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528), licensed CC BY-SA 4.0. Particularly relevant works discussed there are Gibbard and Harper, “Counterfactuals and Two Kinds of Expected Utility” (1981); Lewis, “Causal Decision Theory” (1981); Egan, “Some Counterexamples to Causal Decision Theory” (2007); Joyce, “Regret and Instability in Causal Decision Theory” (2012); and Oesterheld and Conitzer, “Extracting Money from Causal Decision Theorists” (2021).

## Conclusion

CDT evaluates what actions would change, not merely what their occurrence would reveal. Its central calculation is expected utility over causally interpreted counterfactual outcomes.

That principle is powerful but not self-executing. Applying it requires a causal model, a specified decision time, and a defensible treatment of information and policy implementation. Ordinary confounding cases show its appeal; predictive and self-referential cases expose unresolved questions about deliberation and rational success. Understanding CDT means understanding both the maximization rule and the counterfactual assumptions that make its recommendations possible.