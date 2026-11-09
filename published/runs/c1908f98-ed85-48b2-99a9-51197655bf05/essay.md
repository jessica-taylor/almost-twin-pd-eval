# Causal Decision Theory: Evaluating What an Action Would Change

A decision can be good news without being a good intervention. Discovering that you exercised yesterday might be evidence that you are healthy, but exercising cannot improve yesterday’s health. Conversely, an unpleasant medical treatment may indicate serious illness while nevertheless improving your prospects.

**Causal decision theory** (CDT) makes this distinction central to rational choice. Its guiding instruction is to choose the available action with the greatest expected utility under a causal counterfactual: *What would happen if I performed this action?* Evidential decision theory (EDT), by contrast, evaluates what outcomes to expect conditional on taking the action.

The distinction is straightforward in ordinary treatment decisions. It becomes controversial when an action provides evidence about its own consequences, an agent’s hidden characteristics, or a predictor’s earlier behavior.

## 1. The mathematical decision rule

Suppose an agent has current information \(I\), a finite set of available actions \(\mathcal A\), and a utility function \(u\) over outcomes. Utilities should include everything the agent values: benefits, costs, risks, effects on other people, and any intrinsic significance of the action itself. CDT does not supply these values.

Let \(O_a\) denote the outcome that would result if action \(a\) were performed. A standard formulation is

\[
V_C(a\mid I)=\mathbb E[u(O_a)\mid I],
\qquad
a^*\in\arg\max_{a\in\mathcal A}V_C(a\mid I).
\]

For mutually exclusive and exhaustive outcomes \(o_1,\ldots,o_n\),

\[
V_C(a\mid I)
=
\sum_j P(O_a=o_j\mid I)\,u(o_j).
\]

The supplied reference presents Gibbard and Harper’s formulation using probabilities of counterfactual conditionals:

\[
U(A)=\sum_j P(A\to O_j)D(O_j).
\]

The arrow should be read counterfactually—“if \(A\) were performed, \(O_j\) would result”—not as ordinary material implication. Nor does the formula require certainty about an action’s effects. Uncertainty about the relevant counterfactuals is precisely what its probabilities represent.

EDT instead evaluates

\[
V_E(a\mid I)
=
\sum_j P(O=o_j\mid A=a,I)\,u(o_j),
\]

where \(A\) is the actual action variable. Thus CDT asks about **making \(a\) happen**, whereas EDT asks about **learning that \(a\) happens**.

These can agree. Under consistency, meaning that the actual outcome equals the potential outcome for the actual action, the condition

\[
O_a\perp A\mid I
\]

implies

\[
P(O_a=o\mid I)=P(O=o\mid A=a,I),
\]

provided the conditioning event has positive probability. Informally, the action must convey no additional information about its potential outcome.

This is a sufficient condition, not a universal truth. The reference discusses related independence conditions and Lewis’s results against generally identifying probabilities of conditionals with conditional probabilities.

## 2. An operational interpretation: intervene on a causal model

The reference emphasizes an important limitation: CDT alone does not provide an algorithm for calculating counterfactual probabilities. A usable decision procedure therefore requires an account of causal counterfactuals.

Here is one operational interpretation, additional to the reference’s abstract formulation. Represent the situation by an acyclic structural causal model:

\[
X_i=f_i(\operatorname{Pa}_i,Z_i).
\]

Each variable is determined by its causal parents and background factors \(Z_i\). A joint distribution over the background factors represents uncertainty.

Ordinarily, the action variable also has a mechanism:

\[
A=f_A(\operatorname{Pa}_A,Z_A).
\]

To evaluate action \(a\), replace this equation by

\[
A:=a,
\]

while leaving the other equations intact. This intervention is written \(\operatorname{do}(A=a)\).

For information \(I\) acquired before the intervention, the practical procedure is:

1. Update beliefs about the background situation using \(I\).
2. Replace the action-generating mechanism with \(A:=a\).
3. Propagate the consequences through the remaining equations.
4. Average the resulting utilities.

If \(m\) indexes possible causal models and \(z\) their background states, this gives

\[
V_C(a\mid I)
=
\sum_{m,z}P(m,z\mid I)\,
u\!\left(O_a(m,z)\right).
\]

This formulation accommodates uncertainty about both circumstances and causal structure. What stays fixed across candidate actions is the current posterior over background possibilities—not every variable in the world. Variables causally downstream of the intervention are allowed to change.

For example, in the graph

\[
S\longrightarrow A,\qquad
S\longrightarrow O,\qquad
A\longrightarrow O,
\]

\(S\) influences both the action and the outcome. Intervention removes the arrow into \(A\), while retaining the action’s effect on \(O\). Under the corresponding assumptions,

\[
P(o\mid\operatorname{do}(A=a),I)
=
\sum_s P(o\mid a,s,I)P(s\mid I).
\]

Conditioning on the action instead uses \(P(s\mid A=a,I)\). That difference is where many disputes arise.

This structural interpretation is not a proof that every philosophical version of CDT is equivalent to intervention calculus. It is a precise implementation for settings with clearly specified action mechanisms.

The reference also describes Lewis’s **imaging** proposal: move probability mass from each possible world to the nearest world where the proposed action occurs. But “nearest” needs substantive interpretation. Should a changed action leave a hidden personality trait fixed, or require revising it? Structural equations answer such questions by specifying which mechanisms the intervention replaces.

Neither approach extracts causal structure from observational probabilities alone. Different causal models can fit the same observations while recommending different actions.

## 3. Common causes: the King David example

The reference’s King David example isolates the evidential–causal distinction. Charisma influences both whether David acts justly and whether a revolt succeeds. Summoning Bathsheba is evidence of low charisma, but, by stipulation, the unjust act itself does not cause a successful revolt.

Consider this numerical version. Let \(S\) indicate that David is uncharismatic, with

\[
P(S)=\tfrac12.
\]

Suppose

\[
P(R\mid S)=0.7,\qquad P(R\mid\neg S)=0.1,
\]

where \(R\) is a successful revolt. Summoning Bathsheba has utility benefit \(5\), and a successful revolt costs \(100\). For simplicity, assume no other utility differences.

Because summoning does not change charisma or revolt risk,

\[
P(R\mid\operatorname{do}(\text{summon}))
=
P(R\mid\operatorname{do}(\text{abstain}))
=0.4.
\]

Therefore,

\[
V_C(\text{summon})=5-40=-35,
\qquad
V_C(\text{abstain})=-40.
\]

CDT recommends summoning.

Now suppose uncharismatic kings summon with probability \(0.9\), while charismatic kings do so with probability \(0.1\). Bayes’s theorem gives

\[
P(S\mid\text{summon})=0.9,
\qquad
P(S\mid\text{abstain})=0.1.
\]

Consequently,

\[
V_E(\text{summon})=5-100(0.64)=-59,
\]

whereas

\[
V_E(\text{abstain})=-100(0.16)=-16.
\]

EDT recommends abstention because abstention is favorable evidence about David’s character.

This example is not an ethical endorsement of summoning Bathsheba. Its stipulated utility omits harms and moral costs that a realistic evaluation should include. Its purpose is to show that changing an indicator of an underlying condition need not change the condition itself.

## 4. Newcomb’s problem: prediction without causal control

In Newcomb’s problem, a transparent box contains \$1,000. An opaque box contains \$1,000,000 if a reliable predictor previously predicted that the agent would take only the opaque box; otherwise it is empty.

The agent now chooses between one-boxing and two-boxing.

Let \(F\) mean that the opaque box is full, and write

\[
q=P(F\mid I).
\]

Assume ordinary forward causation: the present action does not alter the earlier prediction or box filling. Also assume utility is linear in money. Then

\[
V_C(\text{one})=10^6q,
\]

\[
V_C(\text{two})=10^6q+1000.
\]

Two-boxing gains \$1,000 under either fixed box-content hypothesis. CDT therefore recommends two-boxing.

For an evidential calculation, suppose more specifically that

\[
P(F\mid\text{one},I)=0.99,\qquad
P(F\mid\text{two},I)=0.01.
\]

These conditional reliability assumptions are stronger than merely specifying 99% overall predictive accuracy. They yield

\[
V_E(\text{one})=\$990{,}000,
\qquad
V_E(\text{two})=\$11{,}000.
\]

EDT recommends one-boxing.

CDT does not deny the correlation or deny that one-boxers tend to become richer. It denies that the present box-taking intervention changes the already established contents. A causal model may explain predictive success through common antecedents of the prediction and the agent’s action, while holding those antecedents fixed under the final intervention.

The dispute concerns which comparison rational choice should privilege: the better outcome within each fixed causal background, or the better outcomes associated with the kind of action actually selected.

The reference presents this as a continuing philosophical disagreement, not a settled refutation of either theory.

## 5. Policies, commitments, and the timing of control

An action and a policy are different objects of intervention.

A policy \(\pi\) specifies an action for each possible information history \(h_t\):

\[
a_t=\pi(h_t).
\]

For a sequential problem, a natural causal policy value is

\[
V_C(\pi\mid I)
=
\mathbb E\!\left[
\sum_{t=0}^{T}\gamma^t r_t
\;\middle|\;
\operatorname{do}(\Pi=\pi),I
\right],
\]

where \(r_t\) is utility received at time \(t\), and \(\gamma\) is an optional discount factor.

This extends the intervention-based interpretation above; the reference does not itself provide this policy formula. Its meaning depends on what installing or adopting \(\pi\) actually changes.

Suppose, before the Newcomb predictor acts, the agent can install a binding mechanism that permits only one-boxing. If the predictor can observe or otherwise respond causally to that mechanism, adopting it can cause the opaque box to be filled. CDT may then recommend the commitment, even though it recommends taking both boxes when no commitment was made and the contents are already fixed.

There is no contradiction: the two decisions control different parts of the causal process.

By contrast, merely redescribing a late action as “choosing a policy” does not create influence over the past. One must specify:

- when the policy is adopted;
- how it is implemented;
- what the predictor or other agents can detect;
- whether it can later be revised.

Randomization requires similar care. For a private randomizer independent of the relevant background state, used after everything else is fixed,

\[
V_C(\mu)=\sum_a\mu(a)V_C(a).
\]

Such mixing cannot exceed the highest-valued pure action. But if an opponent observes the randomization policy before responding, choosing a distribution becomes a different strategic intervention. The earlier linear comparison need not describe it.

Thus CDT’s advice is sensitive not merely to the available labels—“cooperate,” “one-box,” “randomize”—but to the concrete mechanism and timing of control.

## 6. Self-knowledge and unstable deliberation

The reference reports Egan’s criticism that CDT can fail by holding fixed an agent’s credences about causal dependencies while evaluating actions that themselves provide evidence about those dependencies.

The **Psychopath Button** illustrates the issue. Paul can press a button that kills all psychopaths. He values their elimination but strongly prefers survival. He also believes that only a psychopath would press the button.

Let \(p\) be Paul’s current probability of being a psychopath. Normalize not pressing to utility zero. Suppose pressing produces benefit \(B>0\) if Paul is not a psychopath, but utility \(-L\) if he is one. Straightforward causal evaluation gives

\[
V_C(\text{press})=(1-p)B-pL.
\]

It recommends pressing whenever

\[
p<\frac{B}{B+L}.
\]

Pressing does not cause Paul to become a psychopath. Nevertheless, discovering that he is willing to press might strongly increase his probability of already being one. The criticism is that the favorable evaluation may rely on a self-assessment that cannot survive the deliberation producing the action.

This reveals an important distinction:

\[
P(S\mid I)
\quad\text{versus}\quad
P(S\mid I,\text{observed inclination to press}).
\]

CDT need not ignore the second distribution. As the reference notes, Joyce argues that causal decision theorists can use information about their own inclinations as evidence.

A reasonable operational interpretation is therefore:

> Update on genuine information obtained during deliberation, including reliable self-observation, before evaluating the remaining causal interventions.

But this is not a complete solution. What counts as an observation rather than merely entertaining a candidate action? Can the agent repeatedly change its mind, updating on each change? Does the resulting process stabilize?

The reference’s **Death in Damascus** example exposes a related problem. If Death predicts the agent’s destination and waits there, the agent may prefer whichever destination it currently considers less likely to contain Death. Yet forming that intention may change its beliefs about Death’s prediction, reversing the preference.

These problems are not adequately described as CDT being unable to represent correlations. CDT can represent them perfectly well. The difficulty is coordinating causal evaluation with action-dependent information about oneself.

The reference also reports predictor-based offers and diachronic Dutch-book arguments in which causal agents allegedly lose money. Such objections concern the coherence of decisions across stages, not merely a single expected-utility calculation. Their assessment requires explicit assumptions about deliberation, learning, commitment, and what the agent can control. The source does not establish one universally accepted resolution.

## 7. A practical procedure for unfamiliar cases

A disciplined application of CDT can follow six steps:

1. **Specify the alternatives.** Identify actions or implementable policies, not merely desirable outcomes.
2. **Specify the decision time.** Separate established facts from variables the intervention can still affect.
3. **Specify utility.** Include action costs, external effects, and risk attitudes.
4. **Build the causal model.** Distinguish causal paths from common causes and predictive associations.
5. **Update on available evidence.** Include relevant self-knowledge, while not automatically conditioning on every hypothetical action being evaluated.
6. **Intervene, average, and compare.** Compute \(V_C(a\mid I)\), or the corresponding policy value, under a common current information state.

If plausible causal models disagree, report that dependence. CDT supplies a criterion for choosing given causal beliefs; it does not guarantee that those beliefs are identifiable from the problem’s observational information.

## References and scope

The principal source is Wikipedia contributors, “Causal decision theory,” supplied revision [1381555528](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528), licensed CC BY-SA 4.0.

Key works discussed there include Gibbard and Harper, “Counterfactuals and Two Kinds of Expected Utility” (1981); Lewis, “Causal Decision Theory” (1981); Egan, “Some Counterexamples to Causal Decision Theory” (2007); and Joyce, “Regret and Instability in Causal Decision Theory” (2012). The structural-model implementation, numerical illustrations, and policy formulation above are explanatory developments rather than formulas supplied by the reference.

## Conclusion

CDT evaluates actions by the outcomes they would causally produce, not merely by the outcomes they predict. Applying it requires utilities, causal counterfactuals, and a precise specification of what the agent controls. Its strength is separating effective intervention from favorable evidence. Its hardest cases arise when prediction and self-knowledge make the beliefs used in evaluation sensitive to the deliberation itself. A useful causal analysis must therefore explain both what changes under an action and why everything else is held fixed.