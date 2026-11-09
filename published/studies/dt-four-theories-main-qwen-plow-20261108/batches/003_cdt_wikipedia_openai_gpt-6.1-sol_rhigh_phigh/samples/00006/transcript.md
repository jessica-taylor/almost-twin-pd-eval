# 003_cdt_wikipedia_openai_gpt-6.1-sol_rhigh_phigh / 00006

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/cb4602f2-8451-496e-9d07-56d45a54b19f/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/cb4602f2-8451-496e-9d07-56d45a54b19f/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Choosing What to Bring About

A decision can be good news without being a good intervention. Discovering that you declined a dangerous activity might indicate that you are unusually healthy or cautious. It does not follow that declining the activity produces those favorable characteristics. Causal decision theory, or **CDT**, makes this distinction central: choose the action with the best expected causal consequences, rather than the action whose occurrence would be the most encouraging evidence.

The distinction is straightforward when evaluating medical treatments or public policies. It becomes philosophically difficult when the evidence supplied by an action concerns the agent’s own character, a predictor’s earlier forecast, or another agent’s correlated decision.

This essay develops CDT’s counterfactual criterion, gives an operational interpretation using causal models, and explains its recommendations and limitations. The supplied reference presents CDT as a family of approaches, not a complete algorithm for constructing counterfactual probabilities. The causal-model implementation below is therefore an explicit modeling proposal, not something uniquely settled by the reference.

## 1. The decision criterion

Let \(\mathcal A\) be a finite set of feasible actions, \(E\) the agent’s current evidence, and \(O_1,\ldots,O_n\) mutually exclusive and exhaustive outcomes. Let \(u(O_j)\) represent the agent’s preferences. Outcomes should include everything relevant: monetary gains, effort, harm to others, and any intrinsic value assigned to acting in a particular way.

Write \(O_a\) for the outcome that would occur **if action \(a\) were performed**. CDT assigns \(a\) the value

\[
V_C(a\mid E)
=
\sum_j P(O_a=O_j\mid E)\,u(O_j),
\]

and recommends

\[
a^*\in\operatorname*{arg\,max}_{a\in\mathcal A}V_C(a\mid E).
\]

The reference presents Gibbard and Harper’s formulation using probabilities of counterfactuals:

\[
V_C(a)=\sum_j P(a\mathbin{\Box\!\to}O_j)\,u(O_j).
\]

Here \(a\mathbin{\Box\!\to}O_j\) means roughly, “Were \(a\) performed, \(O_j\) would occur.” It is not material implication, nor does it say that the outcome is logically necessary. Uncertainty concerns which counterfactual is true.

By contrast, **evidential decision theory**, or EDT, evaluates

\[
V_E(a\mid E)
=
\sum_j P(O_j\mid A=a,E)\,u(O_j).
\]

EDT asks what outcomes to expect upon learning that the action occurs. CDT asks what outcomes performing the action would bring about. The first uses observational conditioning; the second requires a counterfactual interpretation.

Both theories can accommodate uncertain outcomes and risk aversion. Risk preferences belong in the utility function: maximizing expected utility does not generally mean maximizing expected money.

A useful distinction is between uncertainty about outcomes and uncertainty about causal effects. An apple might be spoiled, and eating a spoiled apple might have an uncertain effect on health. CDT averages over both uncertainties. It does not require certainty about causation.

## 2. Giving counterfactuals an operational meaning

The formula alone does not tell us how to calculate \(P(O_a\mid E)\). This is the principal incompleteness emphasized in the reference.

One operational interpretation uses a **structural causal model**. Suppose variables satisfy equations

\[
X_i=f_i(\operatorname{Pa}_i,W_i),
\]

where \(\operatorname{Pa}_i\) are causal parents and \(W_i\) represent background conditions or disturbances. For simplicity, assume the equations form an acyclic system.

Ordinarily, the action variable also has a generating equation:

\[
A=f_A(\operatorname{Pa}_A,W_A).
\]

To evaluate action \(a\), replace this equation by \(A:=a\), leaving the other mechanisms intact. This intervention is written \(\operatorname{do}(A=a)\). Then use

\[
V_C(a\mid E)
=
\mathbb E[u(O)\mid \operatorname{do}(A=a),E].
\]

The procedure has three stages:

1. Update beliefs about background conditions using the evidence actually available.
2. Replace the action-generating mechanism with the proposed action.
3. Propagate its consequences through the remaining causal mechanisms.

Crucially, intervening does **not** hold every other variable fixed. Descendants of the action may change. Administering medicine can change blood chemistry and subsequently recovery. What remains fixed is the background against which the intervention is assessed, not its downstream effects.

If the causal model itself is uncertain, let \(H\) index candidate models. An implementation is

\[
V_C(a\mid E)
=
\sum_h P(h\mid E)
\sum_w P(w\mid h,E)\,
u\!\left(O_a(h,w)\right).
\]

The same posterior distribution over \(H\) and background state \(w\) is used to compare every action. Merely entertaining an action does not update beliefs about which model is true.

This is a substantive interpretation of CDT, not an automatic translation of every philosophical account. It assumes that feasible actions can be represented as interventions and that the relevant mechanisms remain stable under those interventions.

The reference also describes Lewis’s **imaging** approach: move each world’s probability to a suitably “closest” world where the proposed action occurs. A structural model supplies one principled interpretation of closeness—retain the background circumstances, alter the action, and recompute its effects. But it does not eliminate the underlying modeling question: which mechanisms should remain invariant?

### When do causal and evidential evaluations agree?

Suppose **consistency** holds: whenever the actual action is \(a\), the actual outcome equals \(O_a\). If additionally

\[
O_a\perp A\mid E,
\]

then, provided \(P(A=a\mid E)>0\),

\[
P(O=O_j\mid A=a,E)
=
P(O_a=O_j\mid E).
\]

Thus CDT and EDT agree when choosing \(a\) supplies no additional evidence about what would happen under \(a\). Random assignment often supports this independence.

The reference connects the broader distinction to Lewis’s results about probabilities of conditionals. Those results caution against universally identifying counterfactual probabilities with ordinary conditional probabilities; they do not, by themselves, provide a causal model for a particular problem.

## 3. Common causes: the King David example

The reference’s King David example separates an action’s causal consequences from evidence about a stable personal characteristic. David wants to summon Bathsheba but fears revolt. His unknown charisma influences both his tendency to act unjustly and his vulnerability to revolt. The stipulated injustice does not itself cause revolt.

Here is a numerical version, with illustrative probabilities added to the source’s qualitative story.

Let \(C\) mean charismatic, \(S\) summoning, and \(R\) revolt. Suppose

\[
P(C)=\tfrac12,
\]

\[
P(S\mid C)=0.1,\qquad P(S\mid\neg C)=0.9,
\]

and

\[
P(R\mid C)=0.05,\qquad P(R\mid\neg C)=0.55.
\]

Assume that, conditional on charisma, summoning and revolt are independent. The causal structure is

\[
S\leftarrow C\rightarrow R,
\]

with no arrow from \(S\) to \(R\).

Suppose David assigns utility

\[
u=10\,\mathbf 1_S-100\,\mathbf 1_R.
\]

The benefit \(10\) must be understood as net of whatever moral and interpersonal costs his preferences recognize. CDT does not establish that those costs should be ignored.

Intervening on summoning leaves charisma unchanged, so the causal probability of revolt is \(0.30\) under either action. Consequently,

\[
V_C(S)=10-100(0.30)=-20,
\qquad
V_C(\neg S)=-30.
\]

CDT recommends summoning.

Observationally, however, summoning is evidence of low charisma. Bayes’s rule gives

\[
P(C\mid S)=0.1,\qquad P(C\mid\neg S)=0.9.
\]

Therefore,

\[
P(R\mid S)=0.50,\qquad P(R\mid\neg S)=0.10,
\]

and EDT assigns

\[
V_E(S)=-40,\qquad V_E(\neg S)=-10.
\]

EDT recommends abstention.

The lesson is not that CDT ignores correlations. It uses them when learning about the world. Its distinctive claim is that an intervention should not be credited with changing a common cause merely because observing the intervention would reveal information about that cause.

Change the causal assumptions and the recommendation may change. If summoning actually provokes unrest, that pathway belongs in the model.

## 4. Prediction and Newcomb’s problem

Newcomb’s problem isolates the disagreement more sharply. An opaque box contains either nothing or \$1,000,000. A transparent box contains \$1,000. A reliable predictor has already filled the opaque box: it is full if the predictor forecast that you would take only that box, and empty if the forecast was that you would take both.

Let \(B\) be the opaque box’s contents and

\[
q=P(B=1{,}000{,}000\mid E).
\]

Under the standard causal interpretation, your present action cannot alter the earlier filling. Thus

\[
V_C(\text{one box})=1{,}000{,}000q,
\]

\[
V_C(\text{two boxes})=1{,}000{,}000q+1{,}000.
\]

CDT recommends two-boxing. Whatever the opaque box contains, taking the transparent box adds \$1,000.

EDT instead uses the action’s evidential relationship to the prediction. Suppose, more specifically, that

\[
P(B=1{,}000{,}000\mid\text{one box})=0.99,
\]

\[
P(B=1{,}000{,}000\mid\text{two boxes})=0.01.
\]

Then the evidential expected monetary payoffs are \$990,000 and \$11,000 respectively. These conditional probabilities are an additional specification: an overall accuracy rate alone does not necessarily determine both.

The dispute is not whether prediction is reliable. CDT accepts the correlation but denies that changing the present action changes the earlier prediction. Critics object that this recommendation systematically fares badly among agents facing reliable predictors.

This exposes two competing standards: choosing what improves the outcome with the past held causally fixed, and choosing the action associated with the best outcome across predicted agents. Calling two-boxing “dominant” settles the first comparison, not whether that comparison exhausts rational choice.

### Correlated opponents

A similar issue arises in a prisoner’s dilemma against a highly similar “twin.” Suppose your payoffs are \(3\) for mutual cooperation, \(1\) for mutual defection, \(5\) for defecting against cooperation, and \(0\) for cooperating against defection.

If your current action does not cause the twin’s action, let \(q\) be the twin’s probability of cooperation under either intervention. Then

\[
V_C(\text{cooperate})=3q,
\qquad
V_C(\text{defect})=5q+(1-q)=1+4q.
\]

Defection wins for every \(q\). Strong noncausal similarity does not change this calculation. Communication, enforceable agreements, or repeated interaction may change it because they introduce additional causal consequences.

## 5. Actions, policies, and commitment

A policy is a rule assigning actions to future observations. If \(h_t\) denotes the information available at time \(t\), write

\[
a_t=\pi(h_t).
\]

A natural extension of the intervention interpretation evaluates a feasible policy by

\[
V_C(\pi\mid E)
=
\mathbb E[u(\text{trajectory})\mid\operatorname{do}(\pi),E],
\]

where the intervention installs the policy in the relevant future decision mechanisms.

But “choose a policy” is not a license to alter arbitrary facts. We must specify **when and how** the policy is installed.

Before a Newcomb predictor makes its forecast, purchasing a credible commitment to one-box may causally influence the prediction. CDT can therefore favor that commitment. Later, after the boxes have been filled, taking both boxes can still be locally preferable if commitment has not removed that option.

These recommendations concern different interventions at different times. They nevertheless create a genuine issue: a policy preferred in advance may require behavior the agent will later want to abandon. Binding devices, reputational effects, and future self-modification must be included explicitly rather than assumed.

Randomization requires similar care. If an independent lottery simply selects among actions with already fixed causal values, its value is

\[
V_C(\mu)=\sum_a\mu(a)V_C(a),
\]

so it cannot outperform the best pure action. Randomization can matter strategically when adopting or revealing the randomized policy changes another agent’s behavior. That is a different causal setup.

## 6. Self-knowledge and the limits of fixed beliefs

The hardest objections arise when actions reveal information about the agent’s own dispositions.

In Egan’s “Psychopath Button,” discussed in the reference, Paul can press a button that kills all psychopaths. He values their absence but strongly prefers living with psychopaths to dying. He also believes that pressing is characteristic of psychopaths.

Let \(p\) be Paul’s current probability that he is a psychopath. Relative to not pressing, suppose pressing gives a nonpsychopath benefit \(b>0\) and gives a psychopath loss \(-L\). Then

\[
V_C(\text{press})=(1-p)b-pL.
\]

CDT recommends pressing exactly when

\[
p<\frac{b}{b+L}.
\]

Thus endorsement is not unconditional: the prior and utilities matter. For \(p=0.001\), \(b=10\), and \(L=1000\), pressing has causal value \(8.99\).

Yet suppose

\[
P(\text{psychopath}\mid\text{press})=0.99.
\]

Learning that Paul presses would then be alarming evidence. The objection is that a deliberating agent should not dismiss this connection when deciding whether to press.

The reference reports Joyce’s response that CDT can incorporate evidence about what one is inclined or likely to do. This suggests a defensible operational distinction:

- **Actual evidence of an inclination** can update the agent’s beliefs before the alternatives are compared.
- **Merely considering an action counterfactually** does not itself supply new evidence that the action will occur.

If Paul notices a strong, diagnostic desire to press, he should update \(p\), perhaps enough to reject pressing. But updating on every hypothetical action would replace causal evaluation with evidential evaluation.

This distinction does not settle everything. Deliberation can itself generate information about dispositions, so the point at which beliefs should be fixed is disputed. Egan’s criticism targets precisely CDT’s practice of comparing actions while holding fixed credences in causal dependency hypotheses.

### What remains underspecified?

Three modeling gaps deserve emphasis.

**Causal identification.** Observational probabilities need not determine intervention probabilities. Different causal models can fit the same observations while recommending different actions.

**Counterfactual similarity.** Imaging requires a standard of which action-worlds count as closest. Structural models replace that question with assumptions about invariant mechanisms; those assumptions still need justification.

**Dynamic consistency.** Updating, commitment, and prediction can produce tensions between earlier and later recommendations. A static maximization formula does not by itself settle every sequential problem.

The practical response is not to conceal these choices. Specify the evidence, utility function, causal hypotheses, feasible intervention, and time of evaluation. Where the recommendation depends on uncertain causal assumptions, vary those assumptions and report the sensitivity rather than presenting one answer as inevitable.

## Sources

The principal source is Wikipedia contributors, “[Causal decision theory](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528),” supplied revision 1381555528, CC BY-SA 4.0. Central works discussed there include Gibbard and Harper, “Counterfactuals and Two Kinds of Expected Utility” (1981); Lewis, “Causal Decision Theory” (1981); Egan, “Some Counterexamples to Causal Decision Theory” (2007); and Joyce, “Regret and Instability in Causal Decision Theory” (2012). The structural-model implementation and numerical illustrations above are additional exposition.

## Conclusion

CDT evaluates actions by their expected consequences under causal counterfactuals, not by the favorable evidence their occurrence would provide. Applied carefully, it distinguishes learning about a common cause from changing it, and choosing a present action from installing an earlier policy. Its central practical demand is explicit causal modeling. Its unresolved challenge is explaining how that modeling should interact with prediction, self-knowledge, and deliberation without either ignoring relevant evidence or collapsing into evidential decision theory.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Planning the essay structure**

I need to create a comprehensive 2400-3000 word essay focusing on math operational labels and assumptions. I plan for a word budget of around 2750. Key content will address the expected utility and counterfactuals without overly relying on material necessities. I’ll consider evidence and moral utility examples, possibly using King David as a central figure. I’m aiming for concise coverage on causal policies and adversarial situations while ensuring everything aligns effectively in my writing.**Addressing adversarial accuracy**

I need to focus on handling the adversarial fine aggregate accuracy at 0.75 while considering what happens if I abstain from predictions. It's crucial that at least one box is filled for the expected total to be greater than or equal to three. I want to mention the conditional accuracy during buying, and how randomization affects predictions. I might prefer to footnote some assumptions to keep things concise without adding unnecessary clutter, although it's a subtle case.**Structuring the essay**

I’m concentrating on developing a strong essay centered on Newcomb's problem, twin scenarios, psychopaths, and uncertainty in causal models and policies. I think about aiming for around 2800 words, structuring it into 5-7 sections with a substantive title. I'll plan specific word counts for each section: introduction (150), criteria (400), causal semantics (470), confounding examples (320), Newcomb's twin (380), policies (300), self-evidence and adversarial issues (480), operational (180), references (100), and conclusion (80). Overall, I’ll likely hit around 2900 words.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/21086557-29b3-4755-aaf0-6a1d351d4b22/call_0/request.json)

[Authoritative raw response](../../../../../../runs/21086557-29b3-4755-aaf0-6a1d351d4b22/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/21086557-29b3-4755-aaf0-6a1d351d4b22/call_1/request.json)

[Authoritative raw response](../../../../../../runs/21086557-29b3-4755-aaf0-6a1d351d4b22/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
