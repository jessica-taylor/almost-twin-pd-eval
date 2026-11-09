# Causal Decision Theory: Choosing Effects, Not Evidence

A decision can matter in two different ways. It can change what happens, and it can reveal what was already likely to happen. Causal decision theory—CDT—insists that rational choice should track the first relationship: choose the action with the best expected causal consequences.

This distinction is unobjectionable in ordinary examples. Taking an effective medicine may improve your health; merely taking a substance associated with healthy people may not. But when an action reveals something about its chooser, or has been accurately predicted, causation and evidence can point toward different choices.

CDT provides a framework for separating these considerations. Its main difficulty is not expected-utility arithmetic. It is specifying the counterfactual question: **What should remain fixed when we imagine acting differently?**

## 1. The central mathematical rule

Let \(\mathcal A\) be a finite set of available actions, \(I\) the agent’s current information, and \(u(o)\) the utility of outcome \(o\). Outcomes should include everything the agent values: money, health, other people’s welfare, moral considerations, and so forth.

Write \(O_a\) for the outcome that would result if the agent performed action \(a\). A standard causal evaluation is

\[
V_C(a\mid I)
=
\mathbb E[u(O_a)\mid I]
=
\sum_j P(O_a=o_j\mid I)u(o_j).
\]

CDT recommends

\[
a^*\in\operatorname*{arg\,max}_{a\in\mathcal A}V_C(a\mid I).
\]

The supplied article presents Gibbard and Harper’s formulation using probabilities of counterfactuals:

\[
U(A)=\sum_j P(A\to O_j)D(O_j).
\]

Here the arrow should be understood counterfactually: “If this action were performed, this outcome would occur.” It is not a material implication, nor a claim that the outcome follows with logical necessity.

The uncertainty concerns which consequences an action would have. Suppose an apple is good with probability \(0.8\). Eating it yields utility \(5\) if good and \(-10\) if bad; declining it yields \(0\). Then

\[
V_C(\text{eat})=0.8(5)+0.2(-10)=2,
\]

so CDT recommends eating. It does not demand certainty or maximize the best possible outcome.

Evidential decision theory, by contrast, evaluates

\[
V_E(a\mid I)
=
\mathbb E[u(O)\mid A=a,I].
\]

The difference is between **making \(a\) happen** and **learning that \(a\) happens**. Learning an action can change beliefs about its background causes. Performing it need not change those causes.

These evaluations coincide under suitable assumptions. In a potential-outcome model, suppose consistency holds—\(O=O_a\) when \(A=a\)—and

\[
O_a\perp A\mid I.
\]

Then, provided the conditioning event has positive probability,

\[
P(O_a=o\mid I)=P(O=o\mid A=a,I).
\]

Disagreement therefore requires a relevant dependence between the action and its counterfactual consequences. Correlation is not always misleading; sometimes it accurately tracks causation. CDT asks which dependence is present.

## 2. Making counterfactuals operational

The article explicitly notes that CDT does not, by itself, supply an algorithm for calculating counterfactual probabilities. One useful operational interpretation is a **structural causal model**. This is an implementation of CDT, not a claim that every formulation of CDT uses this machinery.

Consider a model with background variables \(X\), action \(A\), and outcome \(O\):

\[
X=f_X(\varepsilon_X),\qquad
A=f_A(X,\varepsilon_A),\qquad
O=f_O(A,X,\varepsilon_O).
\]

The disturbances \(\varepsilon\) represent background uncertainty. Their distribution can encode dependencies not represented by additional explicit variables.

To evaluate action \(a\), replace the equation governing \(A\) with

\[
A:=a,
\]

while retaining the other equations. This intervention is written \(\operatorname{do}(A=a)\).

For information \(I\) appropriately fixed before the action, the resulting causal value can be written

\[
V_C(a\mid I)
=
\mathbb E[u(O)\mid \operatorname{do}(A=a),I].
\]

Operationally:

1. Update beliefs using the information actually available.
2. Replace the action-generating equation with the proposed action.
3. Propagate its effects through the remaining equations.
4. Average the resulting utilities.

The intervention removes the action’s usual dependence on its causes. It does **not** freeze its effects. If choosing a different treatment changes recovery, employment, and later income, those consequences must all be recomputed.

This interpretation uses *non-backtracking* counterfactuals: changing the action does not require rewriting its ordinary background causes. Imagining that I decline a cigarette need not involve imagining different genes or a different childhood.

Causal uncertainty can also be represented. If \(M\) indexes possible causal models,

\[
V_C(a\mid I)
=
\sum_m P(M=m\mid I)
\mathbb E_m[u(O_a)\mid I].
\]

The posterior weights remain fixed while comparing actions. Replacing them with \(P(M=m\mid A=a,I)\) would use the contemplated action as new evidence.

That restriction does not forbid learning about oneself. Actual observations of symptoms, intentions, or dispositions belong in \(I\). It separates such learning from the hypothetical manipulation used to compare actions.

Crucially, the causal model requires justification. Observational data alone may not identify whether an association reflects an effect, a common cause, or selection. Structural equations make assumptions explicit; they do not manufacture the correct assumptions.

## 3. Common causes: the King David example

The reference article illustrates the distinction with King David. His underlying charisma affects both his likelihood of acting unjustly and his vulnerability to revolt. Summoning Bathsheba is evidence of lacking charisma, but the story stipulates that the unjust act itself does not cause revolt.

Here is a numerical reconstruction.

Let \(K\) denote charismatic or uncharismatic, each initially having probability \(1/2\). Suppose

\[
P(\text{summon}\mid K=\text{charismatic})=0.1,
\qquad
P(\text{summon}\mid K=\text{uncharismatic})=0.9.
\]

Revolt probabilities are respectively \(0.1\) and \(0.8\), generated independently of the action once charisma is fixed. The causal structure is

\[
K\longrightarrow A,\qquad K\longrightarrow R,
\]

with no arrow \(A\to R\).

Let summoning provide benefit \(1\), and revolt impose loss \(10\). These utilities are assumptions for the example, not moral judgments endorsed by CDT.

Under either action, the causal revolt probability remains

\[
P(R\mid\operatorname{do}(A=a))
=
\tfrac12(0.1)+\tfrac12(0.8)=0.45.
\]

Thus

\[
V_C(\text{summon})=1-10(0.45)=-3.5,
\]

whereas

\[
V_C(\text{abstain})=-10(0.45)=-4.5.
\]

CDT prefers summoning.

Evidentially, summoning makes uncharismatic David \(90\%\) likely, giving revolt probability \(0.73\). Abstention gives revolt probability \(0.17\). Consequently,

\[
V_E(\text{summon})=1-10(0.73)=-6.3,
\qquad
V_E(\text{abstain})=-10(0.17)=-1.7.
\]

EDT prefers abstention.

CDT’s rationale is that abstention cannot purchase charisma. It rejects manipulating the evidence of a pre-existing condition as though doing so manipulated the condition itself.

However, the recommendation depends on the stipulations. If injustice genuinely increases revolt risk, that effect counts. If David assigns a sufficiently large moral cost to summoning, CDT can recommend abstention. The theory supplies a decision rule, not a particular utility function.

## 4. Prediction: Newcomb’s problem and correlated opponents

In Newcomb’s problem, a transparent box contains \(\$1{,}000\). An opaque box contains either \(\$1{,}000{,}000\) or nothing. A predictor has already filled the opaque box if it predicted that you would take only that box; otherwise it left it empty.

Your options are one-boxing and two-boxing.

Let \(F=1\) mean that the opaque box is full, and let

\[
q=P(F=1\mid I).
\]

Under the ordinary causal interpretation, your present action cannot change the already-set contents. Taking dollars as utility,

\[
V_C(\text{one})=1{,}000{,}000q,
\]

\[
V_C(\text{two})=1{,}000{,}000q+1{,}000.
\]

CDT therefore recommends two-boxing, whatever \(q\) is.

This is a statewise dominance argument: with the box full, two-boxing yields an extra thousand; with it empty, two-boxing also yields an extra thousand.

EDT instead uses action-conditioned probabilities. For illustration, assume symmetric conditional reliability:

\[
P(F=1\mid A=\text{one})=0.99,
\qquad
P(F=1\mid A=\text{two})=0.01.
\]

Then

\[
V_E(\text{one})=990{,}000,
\qquad
V_E(\text{two})=11{,}000.
\]

These conditional probabilities are stronger assumptions than merely saying that aggregate prediction accuracy is \(99\%\).

The disagreement is genuine. CDT does not deny that one-boxers generally receive more money under these assumptions. It distinguishes the success of people who perform an action from the improvement caused by changing one’s action now. Critics question whether that distinction supports the right notion of rational choice in predictor-controlled environments.

A similar issue arises in a prisoner’s dilemma against a highly correlated but causally isolated counterpart. Suppose cooperation yields \(3\) against cooperation and \(0\) against defection; defection yields \(5\) and \(1\). If the opponent’s causal probability of cooperating is \(q\),

\[
V_C(C)=3q,\qquad V_C(D)=5q+(1-q)=1+4q.
\]

CDT defects. If the players’ choices are sufficiently correlated, evidential reasoning can instead favor cooperation. A causal channel through communication, commitment, or repeated interaction would change the calculation.

## 5. Actions, policies, and commitment

A policy specifies actions across possible observations. If \(H_t\) is the history available at time \(t\), a deterministic policy has the form

\[
A_t=\pi(H_t).
\]

To evaluate an implementable policy causally, replace the relevant action equations by this rule and calculate

\[
V_C(\pi\mid I_0)=\mathbb E[u(O_\pi)\mid I_0].
\]

This extension follows the same intervention principle, although the supplied article does not develop a complete policy-selection framework.

The important question is **what policy adoption can actually influence**.

Suppose that, before Newcomb’s predictor acts, you can install an enforceable commitment to one-box. If the predictor observes and trusts the commitment, adopting it causally changes the later prediction and box contents. CDT can favor such a commitment, even at a substantial cost.

Later, after the boxes are filled, the causal situation differs. If the commitment can be discarded without other consequences, a local CDT evaluation again favors taking both boxes.

This creates a distinction between:

- selecting a policy before others respond to it;
- carrying out an action after their responses are fixed;
- selecting a policy that remains enforceable later.

One must not erase these distinctions by renaming today’s action a “policy.” Changing a present intention does not automatically change a past prediction. Likewise, treating the same choice in every similar agent or computer as jointly altered requires additional counterfactual assumptions; ordinary causal intervention does not supply that connection.

For randomized policies, independently generated randomization gives a convex combination of fixed action values in a single-stage problem. But randomization can matter strategically if opponents observe the policy or cannot predict its fresh random input. Those effects belong in the model rather than being added after the calculation.

## 6. Where CDT remains controversial

### Counterfactual selection

The article discusses Lewis’s proposal of *imaging*: move probability mass from each possible world to a nearby world in which the contemplated action occurs.

The difficulty is choosing the relevant nearby world. Should changing my action preserve my psychology, alter my deliberation, or change what an earlier predictor inferred about me?

Structural intervention offers one answer: preserve background circumstances and non-action mechanisms, while replacing the action equation. This is transparent and useful, but its adequacy is itself disputed. The article also reports concerns that judgments about closest worlds may depend on further conditional judgments.

Thus CDT is best understood as a family of approaches sharing a causal maximization principle, rather than a universally agreed counterfactual calculator.

### The psychopath button

Egan’s “psychopath button,” described in the article, exposes a problem concerning self-knowledge.

Paul can press a button that kills all psychopaths. He values their absence, but strongly prefers living with psychopaths to dying. He also believes that only psychopaths would be inclined to press.

Let \(S=1\) mean Paul is a psychopath. Normalize not pressing to utility \(0\). Suppose pressing yields \(b>0\) if he survives, and \(-L\) if he dies. With current probability

\[
p=P(S=1\mid I),
\]

the static causal evaluation is

\[
V_C(\text{press})=(1-p)b-pL.
\]

It recommends pressing whenever

\[
p<\frac{b}{b+L}.
\]

Yet pressing may be overwhelming evidence that Paul is a psychopath.

The objection is not that pressing causes his pre-existing condition. It is that a recommendation based on his initial self-assessment may undermine that assessment: becoming inclined to press should alarm him.

The article reports Joyce’s response that CDT can incorporate information about what an agent is inclined or likely to do. A reasonable operational interpretation is therefore:

> Update on genuine evidence produced during deliberation, then evaluate interventions using the updated beliefs.

That interpretation distinguishes observing an inclination from hypothetically imposing an action. But it leaves difficult questions about deliberative stability. Repeated reconsideration need not produce a uniquely settled recommendation. The source does not establish a general solution.

### The adversarial offer

Another example in the article offers two boxes, each costing \(\$1\). Yesterday, a predictor placed \(\$3\) in every box it predicted the buyer would not acquire. The buyer may purchase one box or neither.

At least one box contains \(\$3\). If their contents are \(X_L,X_R\), then

\[
X_L+X_R\ge3.
\]

Holding current beliefs about contents fixed,

\[
\max\{\mathbb E[X_L\mid I],\mathbb E[X_R\mid I]\}\ge1.5.
\]

Consequently, some purchase has causal expected net value at least \(\$0.50\), while declining yields \(0\).

Nevertheless, across purchases for which the predictor correctly anticipates the selected box \(75\%\) of the time, the average net return is

\[
0.75(-1)+0.25(2)=-0.25.
\]

The tension is between a favorable fixed-belief causal evaluation and an unfavorable outcome distribution in which the selected action is correlated with the box contents.

This challenges CDT’s ability to avoid systematic exploitation. It does not show that causal arithmetic is inconsistent; it challenges whether that arithmetic provides the right deliberative standard. Fresh unpredictable randomization might change the predictor’s accuracy, but then that changed accuracy must be modeled explicitly.

## 7. A practical procedure

For an unfamiliar case, a disciplined CDT analysis asks:

1. **What is controllable?** Identify feasible acts, commitments, or policies.
2. **What matters?** Specify utility over complete consequences.
3. **What is already known?** Include genuine evidence about the world and oneself.
4. **What causes what?** Separate causal arrows from predictive associations.
5. **What changes under intervention?** Recompute descendants, not background causes.
6. **How uncertain is the model?** Average over causal hypotheses without reweighting them merely because an action is being contemplated.
7. **Is the recommendation stable?** Check whether new self-information, future reconsideration, or enforceability changes the problem.

When plausible causal models recommend different actions, the conclusion should be conditional on those assumptions. That is more informative than hiding uncertainty behind a single expected-utility number.

### Sources

This essay draws on Wikipedia contributors, “[Causal decision theory](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528),” supplied revision, CC BY-SA 4.0. Structural-model formulations and numerical reconstructions are explanatory additions.

Key works identified by that article include Gibbard and Harper, “Counterfactuals and Two Kinds of Expected Utility” (1981); Egan, “Some Counterexamples to Causal Decision Theory” (2007); Joyce, “Regret and Instability in Causal Decision Theory” (2012); and Oesterheld and Conitzer, “Extracting Money from Causal Decision Theorists” (2021).

## Conclusion

CDT asks what an action would accomplish, not merely what performing it would reveal. Once counterfactual consequences are specified, its mathematics is ordinary expected-utility maximization. The difficult work lies in specifying interventions, updating self-knowledge, and distinguishing present actions from earlier commitments. Those distinctions make CDT practically useful—and explain why prediction and self-referential deliberation remain its most demanding tests.