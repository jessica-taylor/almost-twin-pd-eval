# 003_cdt_wikipedia_openai_gpt-6.1-sol_rhigh_phigh / 00019

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/2d063014-dee7-4a55-a759-e7bbc7241d00/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/2d063014-dee7-4a55-a759-e7bbc7241d00/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Evaluating What an Action Would Change

A decision can be good news without being a good intervention. Learning that someone bought running shoes may suggest that they are healthy; buying shoes need not produce the health that this observation predicts. Causal decision theory (CDT) makes this distinction central to rational choice.

Its guiding principle is:

> Choose the available action whose causal consequences have the greatest expected utility.

The difficulty lies not in maximizing an expectation, but in specifying the counterfactual experiment behind it. What changes when we suppose that an action is performed? What remains fixed? And how should an agent handle information about its own likely behavior?

The reference article presents CDT through probabilities of counterfactuals and contrasts it with evidential decision theory (EDT). This essay develops that presentation into an operational framework. Structural causal models and policy interventions below are additional modeling proposals, not machinery fully specified by the source.

## 1. Expected utility under causal counterfactuals

Let \(\mathcal A\) be a finite set of available actions, \(E\) the agent’s current evidence, and \(O_1,\ldots,O_n\) mutually exclusive, exhaustive outcomes. Let \(u(O_j)\) represent their utilities. Outcomes should include everything relevant: benefits, costs, risks, effects on others, and any intrinsic value assigned to the action itself.

Write

\[
q_a(O_j\mid E)
\]

for the probability that outcome \(O_j\) would occur **if the agent were to perform action \(a\)**. CDT recommends

\[
a^*\in\operatorname*{arg\,max}_{a\in\mathcal A}
V_{\mathrm C}(a\mid E),
\qquad
V_{\mathrm C}(a\mid E)
=\sum_j q_a(O_j\mid E)u(O_j).
\]

The Gibbard–Harper formulation reported in the source writes these probabilities as probabilities of counterfactual conditionals:

\[
V_{\mathrm C}(a\mid E)
=\sum_j P(a\mathbin{\Box\!\to}O_j\mid E)u(O_j).
\]

Here the conditional means “if \(a\) were performed, \(O_j\) would occur.” It should not be read as an ordinary material implication or as a claim that \(a\) logically necessitates the outcome. Uncertainty remains because the agent may not know which circumstances or causal mechanisms obtain.

An equivalent representation, when well-defined potential outcomes are available, is

\[
V_{\mathrm C}(a\mid E)=\mathbb E[u(O_a)\mid E],
\]

where \(O_a\) denotes the outcome under action \(a\).

Alternatively, let \(h\) specify a complete causal response pattern: what would happen under each available action. Then

\[
V_{\mathrm C}(a\mid E)
=\sum_h P(h\mid E)\,u(O(a,h)).
\]

The same weights \(P(h\mid E)\) appear when comparing every action. What changes is the outcome produced within each hypothesis, not the agent’s initial probability of that hypothesis merely because a different action is being considered.

This does not mean holding every consequence fixed. If taking medicine reduces the probability of illness, illness must vary across the relevant counterfactuals. What remains fixed is the background uncertainty against which those effects are assessed.

CDT also does not prescribe risk neutrality. Maximizing expected utility differs from maximizing expected money; monetary calculations below assume linear utility for simplicity.

## 2. Intervention is not observation

EDT instead evaluates

\[
V_{\mathrm E}(a\mid E)
=\sum_j P(O_j\mid A=a,E)u(O_j).
\]

It asks what outcomes would be expected upon learning that the action occurred. CDT asks what outcomes the action would produce.

A common cause can separate these questions. Suppose an underlying trait influences both an action and an outcome:

\[
H\longrightarrow A,
\qquad
H\longrightarrow O.
\]

Observing \(A\) provides information about \(H\), and therefore about \(O\). Intervening on \(A\), however, need not change \(H\) or \(O\).

A sufficient condition for agreement is that the action supplies no additional information about its potential consequences. Assuming consistency—when \(A=a\), the observed outcome equals \(O_a\)—we have

\[
P(O=o\mid A=a,E)
=P(O_a=o\mid A=a,E).
\]

If additionally \(O_a\) and \(A\) are independent conditional on \(E\), this becomes

\[
P(O=o\mid A=a,E)=P(O_a=o\mid E).
\]

Appropriately randomized actions often satisfy this condition. Thus CDT and EDT agree in many ordinary decision problems. Their disagreement concerns action-dependent information that is not itself an effect of acting.

### An operational causal model

The source notes that CDT does not itself provide a complete algorithm for assigning counterfactual probabilities. A useful implementation is an acyclic structural causal model:

\[
X_i=f_i(\operatorname{Pa}_i,U_i),
\]

where \(\operatorname{Pa}_i\) are the direct causal parents of \(X_i\), and \(U_i\) are background variables.

To evaluate \(a\):

1. Update uncertainty about the background variables using the evidence \(E\).
2. Replace the equation determining \(A\) with \(A:=a\).
3. Recompute the variables causally affected by this replacement.
4. Average the resulting utilities.

This replacement is written \(\operatorname{do}(A=a)\), giving

\[
V_{\mathrm C}(a\mid E)
=\mathbb E[u(O)\mid \operatorname{do}(A=a),E].
\]

For pre-action evidence, uncertainty over both models \(M\) and background states \(U\) can be represented by

\[
q_a(o\mid E)
=\sum_{m,u}P(m,u\mid E)
\,\mathbf 1\{O_{m,a}(u)=o\}.
\]

This makes an important distinction explicit: uncertainty about causal structure is allowed, but each proposed intervention is evaluated against the same current distribution over structures.

The implementation assumes that the intervention is meaningful and that unaltered mechanisms remain stable. A causal graph is therefore substantive input, not something automatically recoverable from correlations.

The source also describes Lewis’s *imaging*: move each world’s probability to a suitable nearby world where the action occurs. This raises the analogous question of which worlds count as nearby. A structural model answers by preserving background circumstances and replacing the action mechanism. Neither approach removes the need to justify the counterfactual construction.

## 3. A common-cause example: King David

The reference’s King David example isolates the difference between information and influence. David’s fixed personality affects both his tendency to act unjustly and the probability of revolt. By stipulation, the unjust action itself does not cause revolt.

Consider this numerical version. David is equally likely to be charismatic or uncharismatic. Let \(S\) mean summoning Bathsheba and \(R\) mean revolt:

\[
P(S\mid \text{uncharismatic})=0.9,
\qquad
P(S\mid \text{charismatic})=0.1,
\]

\[
P(R\mid \text{uncharismatic})=0.8,
\qquad
P(R\mid \text{charismatic})=0.1.
\]

Assume revolt is unaffected by summoning within either personality type. Then

\[
P(R\mid \operatorname{do}(S))
=P(R\mid \operatorname{do}(\neg S))
=0.45.
\]

If summoning provides utility \(1\), while revolt costs \(10\), the causal values are

\[
V_{\mathrm C}(S)=1-10(0.45)=-3.5,
\qquad
V_{\mathrm C}(\neg S)=-10(0.45)=-4.5.
\]

CDT recommends summoning.

But observing summoning would raise the probability that David is uncharismatic to \(0.9\), whereas observing abstention would lower it to \(0.1\). Consequently,

\[
P(R\mid S)=0.73,
\qquad
P(R\mid \neg S)=0.17.
\]

EDT therefore recommends abstention under these utilities.

The causal argument is that abstaining cannot acquire the favorable personality that abstention would indicate. This is not an ethical endorsement of David’s conduct: moral costs belong in the utility function and can reverse the recommendation.

## 4. Newcomb’s problem: causally fixed, evidentially responsive

In Newcomb’s problem, a transparent box contains \(\$1{,}000\). An opaque box contains either \(\$1{,}000{,}000\) or nothing. A predictor has already filled the opaque box if it predicted that the agent would take only that box, and left it empty if it predicted that the agent would take both.

Let \(F\) indicate that the opaque box is full:

| Action | \(F=1\) | \(F=0\) |
|---|---:|---:|
| One-box | \$1,000,000 | \$0 |
| Two-box | \$1,001,000 | \$1,000 |

Under the standard causal interpretation, the current action cannot change the completed prediction or the contents. Writing

\[
p=P(F=1\mid E),
\]

CDT assigns

\[
V_{\mathrm C}(\text{one})=1{,}000{,}000p,
\]

\[
V_{\mathrm C}(\text{two})=1{,}000{,}000p+1{,}000.
\]

Two-boxing is better by \(\$1{,}000\) in either causally fixed state, hence in expectation.

EDT instead uses action-conditioned probabilities. For illustration, assume

\[
P(F=1\mid \text{one})=0.99,
\qquad
P(F=1\mid \text{two})=0.01.
\]

Then

\[
V_{\mathrm E}(\text{one})=\$990{,}000,
\qquad
V_{\mathrm E}(\text{two})=\$11{,}000.
\]

These symmetric conditional probabilities are an additional specification: an overall prediction-accuracy figure alone does not determine both.

CDT does not deny the predictor’s success. It denies that the correlation should be treated as a causal effect of the present action. Recomputing the prediction when changing the action would evaluate a different counterfactual from holding the already completed prediction fixed.

This exposes the philosophical disagreement. Should rationality track the extra money obtainable in each fixed state, or the superior rewards received by agents whose choices correlate favorably with predictions? The source reports continuing disagreement. With an imperfect predictor, one should also avoid saying that every two-boxer gets only \(\$1{,}000\): the claim concerns a characteristic pattern, not an exceptionless outcome.

## 5. Policies, commitments, and the time of choice

An action is not the only possible object of causal evaluation. A policy maps available information to actions:

\[
A_t=\pi_t(H_t),
\]

where \(H_t\) is the observed history at time \(t\).

A natural extension of the intervention framework evaluates an implementable policy by

\[
V_{\mathrm C}(\pi\mid E_0)
=
\mathbb E\!\left[
\sum_{t=0}^{T}\gamma^t r_t
\;\middle|\;
\operatorname{do}(A_t=\pi_t(H_t)\text{ for all }t),E_0
\right],
\]

with \(0<\gamma\leq1\). Here the intervention replaces the relevant decision mechanisms, while observations and environmental responses follow their causal equations.

This operational extension requires care. Choosing a policy must mean implementing something, not merely declaring that several future decisions should be evaluated together.

Before a Newcomb predictor observes the agent, installing a reliable one-boxing commitment may causally affect its prediction and hence the opaque box’s contents. CDT can favor such a commitment, subject to its cost. After the box has been filled, taking both boxes remains preferable under the earlier fixed-state calculation.

There is no contradiction between these evaluations: committing earlier and choosing later have different causal effects. But if the commitment is unenforceable, later reconsideration can undermine the plan. Merely relabeling a present act as a “policy” does not create influence over the past.

Similarly, logical resemblance between agents is not automatically a causal connection. Against a causally isolated twin in a one-shot prisoner’s dilemma, standard act-CDT defects when defection dominates for each fixed twin action. If selecting a shared controller actually controls both players, the intervention is different and cooperation may become optimal.

The lesson is to specify exactly which mechanism a purported policy choice changes.

## 6. Self-evidence and the limits of a fixed evaluation

The source’s strongest criticisms concern actions that reveal information about the agent itself.

### The psychopath button

Suppose pressing a button kills all psychopaths. Paul values eliminating psychopaths but strongly prefers remaining alive. He assigns a small prior probability \(q\) to being a psychopath, while believing that almost only psychopaths would press.

Normalize not pressing to utility \(0\). Suppose pressing gives utility \(B>0\) if Paul is not a psychopath and \(-L\) if he is. Holding his type fixed under intervention gives

\[
V_{\mathrm C}(\text{press})=(1-q)B-qL.
\]

Thus pressing is recommended whenever

\[
q<\frac{B}{B+L}.
\]

Yet pressing would be powerful evidence that Paul belongs to the group the button kills. Egan’s criticism, reported in the source, is that the initial, unconditioned probability of Paul’s type can be inappropriate for evaluating an action that reveals that type.

A response associated with Joyce is that CDT can use evidence about the agent’s inclinations. If Paul discovers a strong desire to press, that discovery can rationally increase \(q\) before he evaluates the intervention.

These operations should be distinguished:

- **Learning about an actual inclination** supplies evidence about Paul.
- **Supposing an intervention that makes Paul press** does not, by itself, change his underlying type.

This distinction offers a reasonable operational approach: incorporate genuine introspective evidence into \(E\), then compare interventions. It does not completely settle the issue. Deliberation may itself produce new evidence about the agent, and the source does not provide a unique rule for where that process ends. Simply conditioning on each contemplated action would instead recover the evidential calculation.

### The adversarial offer

The source also presents an offer involving two boxes, each costing \(\$1\). Yesterday, a seller put \(\$3\) in every box she predicted the buyer would not purchase. The buyer may purchase one box or neither.

Let \(G\) be the predicted purchase, possibly “neither.” Since at least one box contains \(\$3\), their contents satisfy

\[
B_1+B_2\geq3.
\]

Under fixed causal credences, their expected net purchase values therefore obey

\[
V_{\mathrm C}(1)+V_{\mathrm C}(2)
=\mathbb E[B_1+B_2\mid E]-2\geq1.
\]

At least one purchase has causal expected value at least \(\$0.50\), so this calculation recommends buying.

Nevertheless, in an ensemble where the seller correctly predicts the purchased box with probability \(0.75\), buyers receive only \(\$0.75\) on average while paying \(\$1\): a loss of \(\$0.25\).

There is no algebraic contradiction. Causal evaluation uses a fixed marginal distribution over predictions; realized performance depends on the association between predictions and selected actions. The challenge is whether those fixed credences remain appropriate as a self-aware agent deliberates. The source reports arguments that such problems permit money extraction and diachronic Dutch books, alongside continuing causalist responses.

These examples show why “maximize causal expected utility” is not yet a complete theory of reflective deliberation.

## 7. A practical procedure

For an unfamiliar problem, a disciplined application of CDT should proceed as follows:

1. **Specify the decision point and available interventions.** Distinguish a present action from an earlier commitment or implemented policy.
2. **Define complete outcomes and utilities.** Include costs and effects on others.
3. **Separate evidence from suppositions.** Update on observations and genuine self-knowledge before evaluating alternatives.
4. **State the causal model.** Identify common causes, downstream effects, and mechanisms preserved under intervention.
5. **Calculate each intervention’s expected utility using the same current background credences.**
6. **Check sensitivity.** If plausible causal models or treatments of self-evidence recommend different actions, report that uncertainty rather than concealing it.

## Conclusion

CDT separates making a favorable outcome happen from learning that a favorable outcome is likely. Its mathematical rule is straightforward once causal counterfactuals are specified: intervene, propagate consequences, and maximize expected utility.

Its unresolved difficulties concern that specification—especially when choices predict, reveal, or help constitute the agent’s own dispositions. A careful application therefore needs more than a payoff table: it needs an explicit account of what the choice changes, what it merely indicates, and when the relevant intervention occurs.

## References

1. Wikipedia contributors. “[Causal decision theory](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528).” Supplied reference revision. CC BY-SA 4.0.
2. Gibbard, A., and Harper, W. L. (1981). “Counterfactuals and two kinds of expected utility.” *Ifs*, 153–190.
3. Lewis, D. (1981). “Causal decision theory.” *Australasian Journal of Philosophy*, 59(1), 5–30.
4. Egan, A. (2007). “Some counterexamples to causal decision theory.” *The Philosophical Review*, 116(1), 93–114.
5. Joyce, J. M. (2012). “Regret and instability in causal decision theory.” *Synthese*, 187(1), 123–145.
6. Oesterheld, C., and Conitzer, V. (2021). “Extracting Money from Causal Decision Theorists.” *The Philosophical Quarterly*, 71(4).
```

### Available readable reasoning

Extraction: readable reasoning_details blocks joined in saved order.

```text
**Clarifying concepts in prediction**

I'm grappling with the idea that there's no clear dominance between certain states — like none versus buy. It seems that a mixture isn't uniformly or independently predictive. I need to steer clear of mistakenly applying a fixed correlation of 0.75, especially when it contradicts stable actions. This ties into a self-knowledge issue, and I recognize that acknowledging the relationship between predictor accuracy and self-knowledge is part of a more complex modeling discussion.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/d5500b7f-6924-400a-8873-cd3e70e2997c/call_0/request.json)

[Authoritative raw response](../../../../../../runs/d5500b7f-6924-400a-8873-cd3e70e2997c/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/d5500b7f-6924-400a-8873-cd3e70e2997c/call_1/request.json)

[Authoritative raw response](../../../../../../runs/d5500b7f-6924-400a-8873-cd3e70e2997c/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
