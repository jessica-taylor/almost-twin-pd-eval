# 002_cdt_wikipedia_openai_gpt-6.1-terra_rlow_plow / 00008

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/2dffcfc8-bab0-4cc5-8644-5855545f0143/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/2dffcfc8-bab0-4cc5-8644-5855545f0143/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal decision theory: choosing by what you can change

Suppose a medical test shows that patients who receive a certain treatment have worse outcomes than patients who do not. Should a newly diagnosed patient refuse it? Not necessarily. The treatment may be given mainly to the sickest patients: receiving it is bad *news* about a patient’s condition, even if the treatment itself helps.

Causal decision theory (CDT) applies this distinction to choice. It asks not merely what tends to accompany an action, but what would happen **if the agent performed it**. Its guiding idea is to choose the available action with the best expected causal consequences. Evidential decision theory (EDT), by contrast, evaluates an action by the desirability of the world conditional on learning that the action was taken.

Usually these approaches agree. They can disagree sharply when an action is correlated with something it does not cause: an underlying illness, a personality trait, another person’s prediction, or a similar agent’s choice. Such cases expose both CDT’s motivation and the objections to it.

## Actions, outcomes, and counterfactuals

Let \(\mathcal A\) be the set of actions available at a decision point. Let \(O_1,\ldots,O_n\) be mutually exclusive and exhaustive outcomes, with utilities \(u(O_j)\). The outcome descriptions should include everything the agent cares about: money, health, the welfare of others, and any relevant moral costs.

Following the Gibbard–Harper formulation presented in the reference article, the causal expected utility of \(a\) is

\[
V_C(a)=\sum_{j=1}^{n}P(a\mathbin{\Box\!\!\to}O_j\mid I)\,u(O_j),
\qquad
a^*\in\arg\max_{a\in\mathcal A}V_C(a),
\]

where \(I\) is the information available when the choice is made. The expression

\[
a\mathbin{\Box\!\!\to}O_j
\]

means roughly: *if the agent were to do \(a\), outcome \(O_j\) would occur*. The probability is the agent’s credence in that counterfactual, given current information.

This is a probability of a counterfactual proposition, not a claim that the outcome follows from the action by logical necessity. The agent can be uncertain about what an action would bring about. Nor must every feature of the outcome be caused by the action: a full outcome can include background facts that would remain unchanged.

For example, suppose eating an apple gives utility \(+8\) if it is good and \(-12\) if it is bad; declining it gives utility \(0\). If the probability that the apple is good is \(0.7\), and the act of eating does not affect its prior quality, then

\[
V_C(\text{eat})=0.7(8)+0.3(-12)=2.
\]

Eating is preferable under these utilities. The calculation combines uncertainty about the world with judgments about the consequences of each possible action.

The corresponding evidential calculation is

\[
V_E(a)=\sum_j P(O_j\mid A=a,I)\,u(O_j),
\]

where \(A\) is the agent’s actual action. This asks what the agent should expect upon receiving the information that \(A=a\). In general,

\[
P(a\mathbin{\Box\!\!\to}O_j\mid I)
\ne
P(O_j\mid A=a,I).
\]

The distinction is not just a notational preference. A person’s action can reveal information about a hidden cause without changing it. The reference article notes Lewis’s results against generally identifying probabilities of conditionals with conditional probabilities; it also reports Gibbard and Harper’s sufficient conditions for equality involving independence between an action and the relevant counterfactual. Independence is a substantive assumption, not a rule that holds in every decision problem.

## A causal model as an operational interpretation

The reference article observes that CDT does not by itself provide an algorithm for finding counterfactual probabilities. One useful way to make the theory operational is to supply a **structural causal model**. This is an additional modelling choice, not a procedure uniquely dictated by the source.

Suppose variables in a model are determined by equations

\[
X_i=f_i(\operatorname{Pa}_i,U_i),
\]

where \(\operatorname{Pa}_i\) are causal parents of \(X_i\), and \(U_i\) are background variables. The model includes an ordinary equation for the action \(A\), perhaps reflecting the agent’s information, dispositions, and reasoning.

To evaluate an action \(a\), replace the equation for \(A\) with

\[
A:=a,
\]

while retaining the other equations. This intervention is denoted \(\operatorname{do}(A=a)\). On this interpretation,

\[
V_C(a)=\mathbb E[u(O)\mid \operatorname{do}(A=a),I].
\]

The information \(I\) is used to form a posterior over background variables and uncertain models. Each candidate intervention is then evaluated against that posterior. The model lets consequences downstream of the action change while leaving unaffected background variables governed by their original equations.

Consider treatment \(A\), disease severity \(S\), and health outcome \(Y\). If severity influences both treatment and outcome, then observing \(A=1\) changes beliefs about \(S\). Intervening to set \(A=1\), however, does not change the patient’s pre-existing severity. A treatment can therefore have

\[
\mathbb E[Y\mid A=1]<\mathbb E[Y\mid A=0]
\]

while also having

\[
\mathbb E[Y\mid\operatorname{do}(A=1)]
>
\mathbb E[Y\mid\operatorname{do}(A=0)].
\]

The first comparison may be confounded; the second represents the causal effect in the model.

This recipe has limits. Interventions must represent actions the agent can meaningfully consider, and a model can be wrong. If the agent is uncertain between causal models \(M\), a natural extension is

\[
V_C(a)=\sum_M P(M\mid I)\,
\mathbb E_M[u(O)\mid \operatorname{do}(A=a),I].
\]

A decision may consequently be sensitive to uncertainty about the causal structure, not just uncertainty within a fixed structure. Observational correlations alone do not always identify intervention effects; experimental evidence or further causal assumptions may be required.

There is also a subtlety about \(I\). Information obtained before acting—including evidence about one’s inclinations—can legitimately change the posterior over background states. What the basic causal calculation does *not* automatically do is treat the hypothetical selection of each candidate action as fresh observational news about those states. That distinction becomes controversial in cases where an agent’s intended action itself seems highly revealing.

## Common causes and the case of King David

The reference article illustrates CDT’s disagreement with EDT through a case due to Gibbard and Harper. King David wants to summon Bathsheba but worries about a revolt. Suppose that charisma is fixed by genetics and childhood. Charismatic kings tend to act justly and rarely face successful revolts; uncharismatic kings tend to act unjustly and often face them. Crucially, the example stipulates that injustice itself does not cause revolt. Both injustice and revolt are symptoms of charisma.

A simple causal diagram is

\[
C\longrightarrow A,
\qquad
C\longrightarrow R,
\]

where \(C\) is charisma, \(A\) is the decision to summon, and \(R\) is successful revolt. There is no arrow from \(A\) to \(R\).

If David’s summoning would be evidence that he is uncharismatic, then he may have

\[
P(R\mid A=\text{summon})
>
P(R\mid A=\text{abstain}).
\]

But under the stipulated causal structure,

\[
P(R\mid\operatorname{do}(A=\text{summon}))
=
P(R\mid\operatorname{do}(A=\text{abstain})).
\]

Summoning changes the action, not the earlier causes of charisma. If David values the encounter and assigns no overriding disutility to the injustice, the causal comparison favors summoning; the evidential comparison may favor abstention because abstention is better news about revolt.

Those qualifications matter. CDT does not instruct agents to disregard moral harm. If the wrong done to Bathsheba and her family is included in utility, or if unjust acts actually increase the risk of revolt, the recommendation may change. The example isolates a particular distinction by stipulating away those causal and evaluative complications.

## Newcomb’s problem: a prediction already made

In Newcomb’s problem, a transparent box contains \$1,000. An opaque box contains either \$1 million or nothing. A highly accurate predictor has already filled the opaque box if it predicted that the player would take only that box, and left it empty if it predicted that the player would take both.

At the time of choice, the contents have been fixed. If the player takes both boxes, the payoff is

\[
B+1000;
\]

if the player takes only the opaque box, it is

\[
B,
\]

where \(B\) is its already-determined content. Under the standard causal model, the present choice does not change \(B\). Hence

\[
V_C(\text{both})-V_C(\text{opaque only})=1000.
\]

Assuming money is valued in this range and there are no other relevant effects, CDT recommends taking both, regardless of the current probability that the opaque box is full.

EDT reaches the opposite conclusion under sufficiently strong predictive correlation. To see the calculation, add the illustrative assumptions that the predictor is correct with probability \(0.99\) *conditional on either action* and that utility is linear in dollars. Then

\[
V_E(\text{opaque only})=0.99(1{,}000{,}000)=990{,}000,
\]

whereas

\[
V_E(\text{both})=1{,}000+0.01(1{,}000{,}000)=11{,}000.
\]

EDT treats one-boxing as excellent news about the contents.

A reported **overall** accuracy of 99% alone does not establish both conditional probabilities used here; base rates matter. But the example shows why a strong enough association yields disagreement.

It would also be misleading to say that two-boxing in an individual case necessarily produces only \$1,000. If the opaque box is full, two-boxing produces \$1,001,000. The criticism is instead about performance across cases in which predictors reliably anticipate agents: one-boxers tend to face full boxes, while two-boxers tend to face empty ones. The causal theorist replies that, once facing the boxes, taking the extra \$1,000 does not empty the opaque box.

## Actions versus policies

A *policy* is a rule for acting across possible information states. If \(H\) denotes information that may become available, a policy can be written

\[
\pi:H\mapsto A.
\]

Evaluating a policy requires specifying when and how it is selected. For example, before a medical test, a policy might say “treat if positive, do not treat if negative.” Its causal value is the expected utility produced by intervening on the rule while allowing the test result and subsequent actions to unfold according to the model.

The timing is especially important in Newcomb-like cases. Suppose an agent could, **before the predictor makes its forecast**, causally commit to one-boxing, and the predictor could detect this commitment. Then the intervention on the commitment can change the predictor’s behavior and the box’s contents. CDT may favor that earlier commitment. At the later choice, without an enforceable commitment, CDT still favors taking both boxes.

Thus an earlier preference for commitment is not a proof that CDT must one-box at the later moment: the available interventions differ. Conversely, calling a present choice a “policy choice” does not by itself make it causally influence an earlier prediction. A model must explain how the policy is selected, what can observe it, and whether it is binding.

This produces a familiar tension between plans and later incentives. A commitment can be valuable precisely because it prevents a later decision-maker from following an otherwise attractive local option. Whether the agent actually has such a device is a feature of the problem, not a consequence of CDT alone.

## Correlated opponents and adverse prediction

The same structure appears in a prisoner’s dilemma played against a highly similar “twin.” Suppose the payoffs to the agent are:

| | Twin cooperates | Twin defects |
|---|---:|---:|
| Cooperate | 3 | 0 |
| Defect | 5 | 1 |

For either fixed choice by the twin, defection gives the agent the higher payoff. If the twin’s decision is correlated with the agent’s but is not caused by it, ordinary CDT recommends defection. Yet if the two choices are almost always alike, cooperation is strong evidence of the mutually beneficial \((3,3)\) outcome, whereas defection is evidence of \((1,1)\).

Again, the causal story is decisive. If a visible commitment or communication can influence the twin, the twin’s response is downstream of that intervention and belongs in the causal calculation. If the only connection is a shared decision procedure or common upbringing, the standard CDT calculation does not count the twin’s matching choice as caused by the agent’s act.

The reference article also describes an **adversarial offer**. A seller offers two boxes for \$1 each; the buyer may buy one or neither. The seller has put \$3 in every box she predicted the buyer would not acquire. At least one box therefore contains \$3. If the buyer’s present action cannot change the contents, then, whatever the buyer’s credences, the expected contents of the two boxes sum to at least \$3. At least one has expected content at least \$1.50, so its causal expected net value is at least

\[
1.50-1=0.50.
\]

Buying that box causally dominates buying nothing in the basic calculation.

But if the seller correctly predicts the box actually acquired with probability \(0.75\), the acquired box contains \$3 only when that prediction is wrong. Its realized average net return is then

\[
0.25(3)-1=-0.25.
\]

The seller profits on average. The contrast relies on the stipulated prediction relationship and on applying the fixed-credence causal calculation; it is not an arithmetic inconsistency. The buyer’s evaluation compares interventions holding fixed beliefs about the past filling, while the accuracy statistic describes the correlation between the actual purchase and that filling.

## Self-locating evidence and unstable decisions

Egan’s “psychopath button,” also reported in the source, brings the problem closer to the agent’s self-knowledge. Paul can press a button that kills all psychopaths. He strongly prefers a world without psychopaths to one with them, but strongly prefers living with psychopaths to dying. He also believes that only a psychopath would press the button.

Suppose, for illustration, that Paul’s current probability of being a psychopath is \(0.01\). Pressing yields \(+10\) if he is not one and \(-100\) if he is; not pressing yields \(0\). A fixed-credence causal calculation gives

\[
V_C(\text{press})=0.99(10)+0.01(-100)=8.9,
\qquad
V_C(\text{not press})=0.
\]

It recommends pressing. But if the fact that Paul is about to press is compelling evidence that he is a psychopath, then learning this would make pressing look disastrous.

The example tests how CDT should handle deliberation itself. The reference article reports a defense associated with Joyce: evidence about what one is inclined or likely to do can be included in the agent’s information. If Paul notices a genuine inclination to press, he should update his probability of being a psychopath before calculating consequences.

That response does not settle every case. If evaluating the button favorably makes Paul more inclined to press, and that inclination changes his beliefs enough to make pressing unfavorable, deliberation can become unstable. Different causal theorists may propose different treatments of such feedback, mixed strategies, or conditions for a recommendation to be stable. The basic formula does not, by itself, specify a unique solution.

## Counterfactuals require a theory of similarity

A structural model is one way to interpret “what would happen if.” Another proposal discussed in the reference article is Lewis’s **imaging**: move probability mass from each possible world to a sufficiently similar world in which the contemplated action occurs, then evaluate outcomes there.

The difficulty is deciding which worlds count as similar in the relevant way. In Newcomb’s problem, a world where the player chooses differently might also be a world where the predictor made a different prediction. Standard CDT instead holds the already-filled box fixed under the present intervention. A defensible similarity rule must explain that choice rather than merely assume it.

The article also notes a possible regress in describing imaging through what the agent would believe if certain of the action: that description itself invokes a conditional belief. More generally, counterfactuals about unusual interventions can be underdetermined by ordinary observations. No decision formula eliminates the need for substantive assumptions about causation, evidence, and what is held fixed.

For practical use, the most useful discipline is therefore:

1. **Specify the decision point and available interventions.** Distinguish an immediate act from an earlier commitment or a contingent policy.
2. **List relevant outcomes and utilities.** Include harms and side effects, not merely the most salient payoff.
3. **Model dependencies.** Separate common causes and correlations from effects of the intervention; include uncertainty over the model where appropriate.
4. **Condition on the agent’s actual information**, including relevant evidence about dispositions, then calculate consequences under each intervention.
5. **Check sensitivity and stability.** Ask whether different plausible causal models, utility judgments, or treatments of deliberative evidence change the recommendation.

This is an operational proposal for applying CDT, not a claim that all causal decision theorists resolve the philosophical disputes in the same way.

## References

- Wikipedia contributors, [“Causal decision theory,” revision 1381555528](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528), licensed CC BY-SA 4.0.
- Gibbard, A., and Harper, W. L. (1981), “Counterfactuals and Two Kinds of Expected Utility.”
- Lewis, D. (1981), “Causal Decision Theory,” *Australasian Journal of Philosophy* 59, 5–30.
- Egan, A. (2007), “Some Counterexamples to Causal Decision Theory,” *The Philosophical Review* 116, 93–114.
- Oesterheld, C., and Conitzer, V. (2021), “Extracting Money from Causal Decision Theorists,” *The Philosophical Quarterly* 71.

## Conclusion

CDT evaluates an action by the expected outcome of doing it, rather than by the news that doing it would convey. This makes it a powerful response to confounding and mere correlation. Its hardest cases arise when actions reveal information about fixed background facts or are reliably predicted by others. Applying CDT requires not only maximizing an expectation, but also specifying the available intervention, the relevant causal model, the agent’s information, and the counterfactuals those choices support.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/08c278e7-b4ea-43e3-a6bf-1625d00f7c96/call_0/request.json)

[Authoritative raw response](../../../../../../runs/08c278e7-b4ea-43e3-a6bf-1625d00f7c96/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/08c278e7-b4ea-43e3-a6bf-1625d00f7c96/call_1/request.json)

[Authoritative raw response](../../../../../../runs/08c278e7-b4ea-43e3-a6bf-1625d00f7c96/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
