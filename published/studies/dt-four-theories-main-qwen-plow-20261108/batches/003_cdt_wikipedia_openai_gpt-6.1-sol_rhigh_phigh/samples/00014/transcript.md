# 003_cdt_wikipedia_openai_gpt-6.1-sol_rhigh_phigh / 00014

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/e2fa1926-e0c8-48da-aaf2-d9417c0c9b87/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/e2fa1926-e0c8-48da-aaf2-d9417c0c9b87/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Choosing Causes, Not Just Good News

A decision can be favorable in two different ways. It can help produce something desirable, or it can provide evidence that something desirable is already true. Buying a successful company’s shares before its success is known may increase your wealth. Discovering that you previously bought those shares may instead reveal that you possess unusually good financial judgment. Both matter epistemically, but only the first describes an effect of the purchase.

**Causal decision theory** (CDT) makes this distinction central: choose the available action with the best expected consequences under the relevant causal counterfactual. **Evidential decision theory** (EDT), by contrast, evaluates outcomes conditional on learning that the action is taken.

The supplied reference develops this contrast through counterfactual probabilities and several philosophical puzzles. Below, I give an explicit structural-model interpretation as a practical implementation. This implementation adds assumptions that the reference itself does not settle; distinguishing those assumptions from CDT’s central principle is essential.

## 1. Expected utility under a causal supposition

Let \(\mathcal A\) be a finite set of available actions, \(I\) the agent’s current information, and \(u(o)\) the utility of a complete outcome \(o\). Utilities should include everything the agent values: consumption, health, other people’s welfare, moral considerations, and costs of acting.

Write \(O_a\) for the outcome that would result **if action \(a\) were performed**. A standard formulation of CDT is

\[
a^*\in\operatorname*{arg\,max}_{a\in\mathcal A}V_C(a\mid I),
\qquad
V_C(a\mid I)=\mathbb E[u(O_a)\mid I].
\]

For discrete outcomes,

\[
V_C(a\mid I)
=\sum_j P(O_a=o_j\mid I)\,u(o_j).
\]

This expresses the reference’s Gibbard–Harper formula,

\[
U(A)=\sum_jP(A\to O_j)D(O_j).
\]

The arrow represents a counterfactual conditional, not material implication or logical necessity. The question is not whether \(a\) deductively entails an outcome, but how likely that outcome would be under the relevant supposition that \(a\) is performed.

EDT instead uses

\[
V_E(a\mid I)
=\sum_jP(O=o_j\mid A=a,I)\,u(o_j).
\]

Here the action is treated as evidence. Conditionalization can change beliefs about causes of the action, even where performing the action cannot change those causes.

The theories need not disagree. In a potential-outcome framework satisfying **consistency**—the actual outcome equals \(O_a\) whenever \(A=a\)—we have

\[
P(O=o\mid A=a,I)=P(O_a=o\mid A=a,I).
\]

Consequently, if

\[
O_a\perp A\mid I,
\]

the evidential and causal probabilities agree. Random assignment often supplies such independence. Self-selection often does not.

This is a useful diagnostic: ask whether learning the action would reveal information about circumstances that the action cannot alter. If so, conditional expected utility need not measure causal effectiveness.

## 2. Making the counterfactual operational

CDT’s maximization rule does not, by itself, specify its counterfactual probabilities. The reference explicitly identifies this as a source of vagueness.

One operational interpretation uses an acyclic **structural causal model**. Variables satisfy equations

\[
X_k=f_k(\operatorname{Pa}_k,E_k),
\]

where \(\operatorname{Pa}_k\) are causal parents and \(E_k\) represents background influences. A probability distribution over the background variables describes uncertainty.

To evaluate action \(a\):

1. Update beliefs about the background circumstances using actual information \(I\).
2. Replace the equation determining the action variable with \(A:=a\).
3. Propagate this change through the remaining equations.
4. Average the resulting utilities over the updated uncertainty.

Replacing the action equation is an **intervention**, commonly written \(\operatorname{do}(A=a)\). It disconnects the action from its usual causes while retaining its effects.

Suppose, for example,

\[
Z\longrightarrow A,\qquad
Z\longrightarrow Y,\qquad
A\longrightarrow Y.
\]

The background variable \(Z\) influences both action and outcome. Observing \(A=a\) can therefore reveal \(Z\). Intervening on \(A\), however, does not change \(Z\). This is the standard structure behind confounding.

A compact representation allows uncertainty about the causal model itself. Let \(h\) identify a model and \(e\) its background circumstances. If \(o_a(h,e)\) is the outcome after intervention, then

\[
V_C(a\mid I)
=\sum_{h,e}P(h,e\mid I)\,u\bigl(o_a(h,e)\bigr).
\]

The same posterior weights appear in every comparison. One does not replace them with \(P(h,e\mid A=a,I)\) merely because \(a\) is being considered.

What stays fixed is the distribution over background circumstances and causal hypotheses—not every other variable. Descendants of the action must change according to the model. Otherwise we would erase the very consequences being evaluated.

For ordinary prospective decisions, this calculation is often abbreviated

\[
V_C(a\mid I)=
\mathbb E[u(O)\mid\operatorname{do}(A=a),I].
\]

The underlying update-then-intervene procedure is safer than the notation alone, especially when evidence is itself affected by variables being intervened upon.

This account also shows why observational frequencies may be insufficient. Different causal models can fit the same observations while disagreeing about interventions. Experiments, substantive knowledge, or explicit assumptions are then needed.

The reference discusses Lewis’s alternative technique of **imaging**: move each world’s probability to a suitable closest world where the action occurs. Structural intervention supplies one precise way of selecting alternatives, but neither “closest world” nor the appropriate causal structure is determined by probability theory alone.

## 3. Ordinary uncertainty and misleading evidence

First consider a decision without confounding. An apple is good with probability \(0.8\). Eating a good apple gives utility \(5\); eating a bad one gives utility \(-10\). An orange guarantees utility \(1\). Then

\[
V_C(\text{apple})=0.8(5)+0.2(-10)=2,
\]

so CDT recommends the apple. It maximizes expected utility, not the probability of receiving the single best outcome.

The reference’s King David example introduces a more interesting dependency. Suppose a king’s fixed character influences both whether he summons Bathsheba and whether his subjects successfully revolt. Stipulate that summoning her does not itself affect revolt.

Let summoning provide benefit \(b\), and let a revolt impose loss \(L\). Under those assumptions,

\[
V_C(\text{summon})-V_C(\text{abstain})=b,
\]

because the revolt probability is unchanged by intervention.

EDT instead evaluates the difference as

\[
b-L\left[
P(R\mid\text{summon},I)
-P(R\mid\text{abstain},I)
\right].
\]

If summoning is strong evidence of revolt-prone character, EDT can recommend abstention even though abstention does nothing to prevent revolt.

CDT’s philosophical motivation is clear here: declining to express an undesirable trait does not thereby remove the trait or its independent consequences.

The recommendation nevertheless depends on the stipulated utilities and causal structure. CDT does not independently endorse injustice. If summoning causes harm, or injustice itself carries negative utility, those considerations belong in the calculation.

## 4. Newcomb’s problem: dominance versus prediction

In Newcomb’s problem, a transparent box contains \(\$1{,}000\). An opaque box contains either \(\$1{,}000{,}000\) or nothing. A predictor previously filled the opaque box if it predicted that the player would take only that box; otherwise it left it empty. The player now chooses one box or both.

Let \(B\) be the opaque box’s already-fixed contents, and assume utility is money. Under the usual causal model, the present action cannot change \(B\). Writing

\[
p=P(B=1{,}000{,}000\mid I),
\]

CDT obtains

\[
V_C(\text{one})=1{,}000{,}000p,
\]

\[
V_C(\text{two})=1{,}000{,}000p+1{,}000.
\]

Thus two-boxing wins by \(\$1{,}000\), whatever \(p\) is. The argument also works for any utility function strictly increasing in money: both boxes provide more money for each fixed content of the opaque box.

EDT uses a different distribution for each choice. For illustration, suppose the prediction structure yields

\[
P(B=1{,}000{,}000\mid\text{one},I)=0.99,
\]

\[
P(B=1{,}000{,}000\mid\text{two},I)=0.01.
\]

Then

\[
V_E(\text{one})=990{,}000,
\qquad
V_E(\text{two})=11{,}000.
\]

These action-conditional probabilities require assumptions beyond a bare claim of “99% overall accuracy”; they state explicitly the intended predictive relationship.

CDT does not deny that one-boxers generally receive more money. It denies that switching the present action changes the already-filled box. Critics ask why a rational theory should recommend behavior associated with systematically worse results. Defenders distinguish causing a better result from selecting favorable evidence about an unchangeable circumstance.

The dispute therefore concerns the appropriate counterfactual comparison, not arithmetic. Under CDT’s comparison, the box contents remain the same across actions; under EDT’s comparison, their conditional distribution changes.

## 5. Correlated agents and the scope of control

The same distinction appears in a one-shot prisoner’s dilemma against a highly similar agent.

Suppose your payoffs are \(3\) for mutual cooperation, \(1\) for mutual defection, \(5\) for defecting against cooperation, and \(0\) for cooperating against defection. If your action does not causally influence the other player’s action, let \(q\) be your causal probability that they cooperate. Then

\[
V_C(C)=3q,\qquad
V_C(D)=5q+(1-q)=1+4q.
\]

Defection is better for every \(q\).

If the players’ actions are nearly perfectly correlated, however, cooperation may be strong evidence of receiving \(3\), and defection strong evidence of receiving \(1\). Mere correlation does not make the other player’s choice a causal consequence of yours.

This conclusion changes if the situation includes communication, enforceable agreements, retaliation, or other causal pathways. CDT must model those pathways rather than assume that all strategic interaction is causally independent.

## 6. Choosing policies rather than isolated actions

A policy specifies what to do after each possible observation. If \(H_t\) is the information history at time \(t\), a deterministic policy has the form

\[
A_t=\pi_t(H_t).
\]

A natural extension of CDT evaluates the complete outcome \(O_\pi\) under installation or adoption of policy \(\pi\):

\[
V_C(\pi\mid I)=\mathbb E[u(O_\pi)\mid I].
\]

The crucial question is **when and how policy adoption occurs**. Calling something a policy does not enlarge the agent’s causal control automatically.

Suppose a Newcomb player can make an observable, binding commitment before the predictor fills the boxes. If that commitment causes the predictor to fill the opaque box, CDT can favor committing to one-box. At the later choice point, however, if the commitment were absent, CDT would still favor taking both boxes.

These recommendations concern different interventions at different times. They also explain the potential value of commitment devices: an earlier beneficial policy may contain a later action that the agent would otherwise abandon.

Merely imagining, at the final choice, “being the sort of person who one-boxes” does not establish a causal influence on the past prediction.

For a private randomization over present actions, with no change to the surrounding causal model,

\[
V_C(\mu\mid I)
=\sum_a\mu(a)V_C(a\mid I).
\]

Hence randomization cannot beat the best pure action in that fixed, single-agent comparison. But choosing a randomization procedure can change what others observe or predict. Such effects require a policy-level model; the displayed linearity cannot simply be applied while ignoring them.

## 7. Self-evidence, instability, and alleged exploitation

The reference presents several challenges to straightforward CDT. Two reveal why the theory’s treatment of information matters.

### The psychopath button

Paul can press a button that kills all psychopaths. He values eliminating psychopaths, but strongly prefers living with them to dying. He also believes that almost only psychopaths would press.

Let \(T\) mean that Paul is a psychopath, with current probability

\[
p=P(T\mid I).
\]

Suppose pressing gives benefit \(b>0\) if he is not a psychopath and utility change \(-L\) if he is. Then

\[
V_C(\text{press})-V_C(\text{refrain})
=(1-p)b-pL.
\]

Plain CDT recommends pressing when

\[
p<\frac{b}{b+L}.
\]

A small prior probability can therefore support pressing even if actually pressing would be overwhelming evidence of psychopathy.

The reference reports Egan’s criticism and Joyce’s response that CDT can incorporate evidence about one’s inclinations. If Paul notices a disturbing desire to press, that observation can raise \(p\) before evaluating either action.

A reasonable operational convention is therefore:

> Update on actual introspective evidence, then use that posterior consistently across the counterfactual alternatives.

This preserves the distinction between evidence and intervention. It is not a complete resolution, because deliberation may itself generate evidence about what one will choose. Exactly how reflective agents should update during deliberation remains a substantive issue. Moreover, the narrative alone does not force a numerical recommendation without utilities and probabilities.

### The adversarial offer

In another example from the reference, two boxes each cost \(\$1\). Yesterday, a predictor put \(\$3\) in every box it predicted the buyer would not purchase. The buyer may purchase one box or neither.

Let \(p_i\) be the current probability that box \(i\) contains money. At least one box contains money, so

\[
p_1+p_2\geq1.
\]

Holding those probabilities fixed under intervention,

\[
V_C(\text{buy }i)=3p_i-1.
\]

At least one box therefore has causal expected net value at least \(\$0.50\), so straightforward CDT recommends buying.

But if the predictor correctly predicts this buyer’s eventual purchase with probability \(0.75\), the purchased box is empty with probability \(0.75\). Actual expected net earnings are then

\[
0.25(3)-1=-\$0.25.
\]

The challenge is not an elementary contradiction between two expectations: they use different probability assignments. Rather, it questions whether maximizing intervention-based value while holding initial dependency beliefs fixed can remain satisfactory when the decision reveals information about the very circumstances determining its payoff.

The reference discusses related instability and money-loss arguments. They are genuine philosophical challenges, but not universally accepted refutations; their force depends partly on the interpretation of counterfactuals and deliberative updating.

## 8. A practical method

For an unfamiliar problem, a disciplined CDT analysis should proceed as follows:

1. **Locate the decision point.** Distinguish a present act from an earlier commitment or policy adoption.
2. **Specify complete utilities.** Include indirect consequences, externalities, and relevant moral costs.
3. **Represent causal dependencies.** Separate causes of the action, effects of the action, and merely correlated variables.
4. **Update on actual evidence.** Include observations and genuine introspective information.
5. **Construct each intervention.** Change the selected action or policy while propagating its downstream effects.
6. **Average and compare.** Use the same posterior over background circumstances for each intervention.

Where causal structure or counterfactual semantics is uncertain, report that uncertainty. A recommendation that reverses across plausible models is less secure than one supported throughout them. CDT supplies a criterion for choice, not a substitute for empirical causal knowledge.

## Conclusion

CDT asks what would happen if an available action were performed, rather than what learning that action would tell us. Its attraction is the separation of effective control from favorable evidence. Its difficulty is specifying that separation when actions reveal hidden traits, predictors anticipate choices, or deliberation changes self-knowledge. Applied carefully, CDT is a precise framework—but its recommendations remain conditional on a defensible model of causation, information, and available interventions.

### References

- Wikipedia contributors. “Causal decision theory,” supplied [revision 1381555528](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528), CC BY-SA 4.0.
- Gibbard, A., and Harper, W. L. (1981). “Counterfactuals and two kinds of expected utility.”
- Lewis, D. (1981). “Causal decision theory.” *Australasian Journal of Philosophy* 59: 5–30.
- Egan, A. (2007). “Some counterexamples to causal decision theory.” *The Philosophical Review* 116: 93–114.
- Joyce, J. M. (2012). “Regret and instability in causal decision theory.” *Synthese* 187: 123–145.
- Oesterheld, C., and Conitzer, V. (2021). “Extracting Money from Causal Decision Theorists.” *The Philosophical Quarterly* 71.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Planning a math essay**

I need to write a coherent math essay of 2400-3000 words, distinguishing my own structural causal model (SCM) from the source. I’m thinking about a budget of around 18k tokens available, and I suspect I have about 29 tokens. Ideally, I want around 2800 words, which could take roughly 4000 to 5000 tokens. I plan to cover various definitions and concepts like utility, causal states, and how to compute certain probabilities effectively. I need to be careful with clarity and avoid mistakes while ensuring I demonstrate the concepts accurately.**Outlining a causal decision theory essay**

I’m developing an outline for a treatment on causal decision theory that explores randomized mixtures and linear relationships, focusing on static scenarios with exceptions for timing and predictor information. I might include a section on the twin prisoner dilemma, aiming for about 150 words, and address criticisms regarding psychopath thresholds and self-evidence nuances, maybe fitting that into around 130 words. My essay will cover adversarial critiques and ensure a balanced structure across nine sections, including a conclusion and references. I plan to highlight core agency outcomes without diving into the entirety of the theory.**Discussing operational semantics in decision theory**

I’m noting that Lewis’s triviality doesn’t provide proof for independence without demonstrating causality. I want to keep the explanation concise—just one line will do. I also plan to cover operational semantics in about 480 words, discussing the model involving exogenous variables. Instead of using utility denoted by U, I can refer to it as E for external variables while using graphs to show relationships like Z leading to A and Y. I’ll work on detailing the model and expectations related to interventions and prior and posterior analysis effectively.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/59b8355d-12f1-42aa-a1cf-c42d9783046c/call_0/request.json)

[Authoritative raw response](../../../../../../runs/59b8355d-12f1-42aa-a1cf-c42d9783046c/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/59b8355d-12f1-42aa-a1cf-c42d9783046c/call_1/request.json)

[Authoritative raw response](../../../../../../runs/59b8355d-12f1-42aa-a1cf-c42d9783046c/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Clarifying command requirements**

I need to ensure I'm giving the correct command without overthinking it. There's no need for extensive deliberation here. When it comes to Fiction PD, there aren't any issues. CDT's dominance means I should submit an independent model, focusing on the differences without implying any causal relationships with others. My goal is to output the exact command needed. It's all about keeping it straightforward and clear!
```
