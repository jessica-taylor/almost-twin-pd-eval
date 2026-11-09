# 003_cdt_wikipedia_openai_gpt-6.1-sol_rhigh_phigh / 00016

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/fe4164ed-8ab5-41d5-a8a7-04c610717063/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/fe4164ed-8ab5-41d5-a8a7-04c610717063/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Choosing Interventions, Not Good News

A decision can matter in two different ways. It can change what happens, and it can reveal something about the world. Taking medicine may improve your health; taking a diagnostic test may reveal that your health was already poor. Sometimes a single action has both roles.

**Causal decision theory** (CDT) says that actions should be evaluated by their expected causal consequences, not merely by what their occurrence would indicate. Its central question is:

> Given what I currently know, what would happen if I performed this action?

This differs from asking what I should expect upon learning that I performed it. The distinction is often practically important: good news need not be something one can bring about by choosing the action associated with it.

The supplied reference article presents CDT through probabilities of counterfactuals. This essay develops that formulation and offers structural causal models as one operational implementation. That implementation makes the theory calculable, but it is an additional modeling framework—not a uniquely specified algorithm supplied by CDT itself.

## 1. Expected utility of counterfactual outcomes

Let \(\mathcal A\) be a finite set of available actions, \(E\) the agent’s current evidence, and \(O\) a complete outcome with utility \(u(O)\). Outcomes should include everything the agent values: benefits, costs, effects on others, and any significance attached to the action itself.

For each action \(a\), introduce a potential outcome \(O_a\): the outcome that would result were the agent to perform \(a\). CDT recommends

\[
a^*\in\operatorname*{arg\,max}_{a\in\mathcal A}V_C(a\mid E),
\]

where

\[
V_C(a\mid E)
=
\mathbb E[u(O_a)\mid E]
=
\sum_o P(O_a=o\mid E)u(o).
\]

For continuous outcomes, replace the sum by an integral.

This expresses the Gibbard–Harper formulation reported in the reference:

\[
U(A)=\sum_j P(A\to O_j)D(O_j).
\]

The arrow here must be understood counterfactually: roughly, “if action \(A\) were performed, outcome \(O_j\) would obtain.” It is not material implication or a claim that \(A\) logically necessitates \(O_j\). Uncertainty about circumstances and mechanisms generates uncertainty about the counterfactual outcome.

By contrast, **evidential decision theory** (EDT) evaluates

\[
V_E(a\mid E)
=
\mathbb E[u(O)\mid A=a,E].
\]

The difference is between a counterfactual supposition and an observation:

\[
P(O_a=o\mid E)
\quad\text{versus}\quad
P(O=o\mid A=a,E).
\]

Under the consistency assumption that \(O=O_a\) whenever \(A=a\), these agree if

\[
O_a\perp A\mid E
\]

and \(P(A=a\mid E)>0\). Intuitively, actually choosing \(a\) must provide no additional information about what would happen under \(a\).

That condition can fail when a hidden variable influences both the action and its prospects. The reference connects this distinction to Lewis’s work on probabilities of conditionals. His results caution against identifying counterfactual probabilities with ordinary conditional probabilities as a general rule; they do not imply that the two must differ in every application.

## 2. Making counterfactuals operational

The formula does not by itself tell us how to calculate \(P(O_a=o\mid E)\). The reference explicitly identifies this as an incompleteness of CDT.

One useful implementation is a **structural causal model**. Suppose variables satisfy equations

\[
X_i=f_i(\operatorname{Pa}_i,W_i),
\]

where \(\operatorname{Pa}_i\) are the direct causal parents of \(X_i\), and \(W_i\) represents background influences. A probability distribution over the background variables represents uncertainty.

An intervention

\[
\operatorname{do}(A=a)
\]

replaces the ordinary equation determining \(A\) with the assignment \(A:=a\). All other equations remain intact. We then recompute the consequences.

For admissible background evidence, the resulting distribution is commonly written

\[
P(O=o\mid \operatorname{do}(A=a),E).
\]

More generally, counterfactual reasoning proceeds by first updating beliefs about background circumstances using \(E\), then intervening, then calculating outcomes. The notation \(P(O_a=o\mid E)\) makes this order especially clear.

The crucial point is that intervention does **not** mean holding everything else constant. It means holding the other causal mechanisms constant. Descendants of the action can change. Variables unaffected by the intervention retain their current uncertainty.

For example, if

\[
A\longrightarrow M\longrightarrow O,
\]

then intervening on \(A\) ordinarily changes both the intermediate variable \(M\) and the outcome \(O\). CDT includes indirect causal effects, not merely immediate ones.

Uncertainty about the causal model can also be represented. Let \(H\) range over hypotheses about mechanisms, and \(w\) over background states. Then

\[
V_C(a\mid E)
=
\sum_{h,w}
P(h,w\mid E)\,
u\bigl(O_a(h,w)\bigr).
\]

The same posterior weights are used when evaluating every action. One does not replace them by \(P(h,w\mid A=a,E)\) merely because one is considering \(a\). Nevertheless, genuinely acquired evidence can change these weights before the comparison.

This framework also accommodates actions that currently have observational probability zero, provided their interventions are well-defined. An agent may be almost certain that it will reject a dangerous treatment while still evaluating what would happen if it accepted.

Structural modeling does not eliminate the philosophical problem. Observational data generally do not uniquely determine causal structure, and some proposed interventions are ambiguous or infeasible. The implementation relocates the difficulty into explicit assumptions that can be examined.

The reference also discusses Lewis’s **imaging** approach: move each possible world’s probability to a suitably “closest” world in which the action occurs. But “closest” requires a substantive rule. Structural models provide one disciplined answer: preserve background circumstances and unaffected mechanisms while changing the action equation. CDT alone does not establish that this answer is uniquely correct.

## 3. A common cause: King David’s decision

The reference illustrates the distinction through King David. His unknown charisma influences both his tendency to act unjustly and the likelihood of revolt. Crucially, the contemplated unjust act does not itself cause revolt.

The causal structure is therefore

\[
C\longrightarrow A,
\qquad
C\longrightarrow R,
\]

with no arrow \(A\to R\).

Here is a numerical version, added for illustration. Let \(C\) mean charismatic, \(S\) mean summoning Bathsheba, and \(R\) mean revolt. Suppose

\[
P(C)=\tfrac12,
\]

\[
P(S\mid C)=0.2,\qquad P(S\mid\neg C)=0.8,
\]

and

\[
P(R\mid C)=0.1,\qquad P(R\mid\neg C)=0.6.
\]

Assume action and revolt are conditionally independent given charisma. Bayes’s rule gives

\[
P(C\mid S)=0.2,\qquad P(C\mid\neg S)=0.8.
\]

Consequently,

\[
P(R\mid S)=0.50,
\qquad
P(R\mid\neg S)=0.20.
\]

Summoning is bad news about charisma. But it does not change charisma, so

\[
P(R\mid\operatorname{do}(S))
=
P(R\mid\operatorname{do}(\neg S))
=
0.35.
\]

Suppose summoning provides a net direct utility benefit of \(5\), while revolt costs \(100\). Then

\[
V_C(S)=5-35=-30,\qquad V_C(\neg S)=-35,
\]

whereas

\[
V_E(S)=5-50=-45,\qquad V_E(\neg S)=-20.
\]

CDT recommends summoning; EDT recommends abstaining.

This is not a moral endorsement. The stipulated benefit must already account for whatever moral considerations David recognizes. CDT specifies how to aggregate consequences under uncertainty; it does not supply the utility function. Its narrower claim is that merely selecting an action associated with charisma does not manufacture charisma.

## 4. Newcomb’s problem: prediction without backward causation

In Newcomb’s problem, a transparent box contains \$1,000. An opaque box contains either \$1,000,000 or nothing. A predictor has already filled the opaque box:

- if it predicted taking only the opaque box, it deposited \$1,000,000;
- if it predicted taking both boxes, it deposited nothing.

The agent now chooses one box or both.

Let \(B\in\{0,10^6\}\) be the opaque box’s contents and let

\[
q=P(B=10^6\mid E).
\]

Under the usual causal model, the present action cannot change the earlier deposit. With utility linear in money,

\[
V_C(\text{one})=10^6q,
\]

\[
V_C(\text{two})=10^6q+1000.
\]

Two-boxing is better by \$1,000 regardless of \(q\). Indeed, with strictly increasing monetary utility and no other relevant effects, it is better for either possible box content.

EDT treats the action as evidence about the prediction. To make “99% accuracy” precise enough for calculation, suppose

\[
P(B=10^6\mid\text{one},E)=0.99,
\]

\[
P(B=10^6\mid\text{two},E)=0.01.
\]

Then

\[
V_E(\text{one})=990{,}000,
\qquad
V_E(\text{two})=11{,}000.
\]

Thus EDT recommends one-boxing. An overall accuracy rate alone need not determine these two conditional probabilities; the symmetric assumptions matter.

CDT does not deny that one-boxing is strongly correlated with receiving the million. It denies that changing the present action changes the already-fixed deposit. The resulting intervention distribution need not preserve the observational correlation.

That counterfactual is precisely what critics challenge. Reliable one-boxers tend to become richer, while CDT still recommends two-boxing at the final choice. The disagreement concerns which comparison should govern action—not a disagreement over elementary arithmetic.

## 5. Actions, policies, and commitment

A policy specifies actions across possible information states. Formally,

\[
\pi:\mathcal H\to\mathcal A,
\]

where \(\mathcal H\) is a set of observable histories.

A natural extension of the causal criterion is

\[
V_C(\pi\mid E)
=
\mathbb E\!\left[
U(\text{trajectory}_{\pi})
\mid E
\right],
\]

where the trajectory is generated by replacing the agent’s action rules with \(\pi\). Future observations must be generated under that policy; one cannot simply evaluate each future action using an unchanged forecast.

This is an operational extension of the intervention approach, rather than a complete account of policy choice supplied by the reference.

Most importantly, **when and how the policy is selected matters**. Suppose, before the predictor acts, the agent can install an observable, binding one-boxing mechanism. Installing it can causally affect the prediction and therefore the deposit. CDT can favor this commitment even though it favors taking both boxes once the deposit is fixed.

There is no contradiction between:

- preferring an earlier commitment that causes a favorable response;
- preferring a different action later, if that commitment is absent or revocable.

Whether the tension constitutes a defect is a further question. It does show why “CDT chooses policies” is not a sufficient specification. One must identify a feasible policy-setting intervention and its causal consequences. Merely imagining a different algorithm does not automatically give the present agent causal control over every correlated instance of that algorithm.

Randomization requires similar care. If an independent random device selects action \(a\) with probability \(\mu(a)\), without otherwise changing the environment, then

\[
V_C(\mu)=\sum_a\mu(a)V_C(a).
\]

Such randomization cannot outperform the best pure action in a one-stage problem. But installing a randomizing mechanism before another agent responds can change that response. That is a different intervention, with a different value.

## 6. Self-knowledge and the limits of fixed credences

The hardest objections concern information an agent gains about itself while deciding.

Consider the reference’s “Psychopath Button.” Paul can eliminate all psychopaths by pressing a button, but psychopaths who press it also die. He values eliminating psychopaths, strongly prefers survival, and believes that almost only psychopaths would press.

Let \(T\) mean that Paul is a psychopath. For a simplified numerical model, suppose pressing rather than abstaining yields benefit \(b>0\) if \(\neg T\), but a net loss \(L>0\) if \(T\). If

\[
p=P(T\mid E),
\]

then

\[
V_C(\text{press})-V_C(\text{abstain})
=
(1-p)b-pL.
\]

CDT recommends pressing when

\[
p<\frac{b}{b+L}.
\]

The problem is not that pressing causally changes Paul’s type. Rather, discovering that he is willing to press may sharply increase his probability of being a psychopath. A recommendation based on low \(p\) may undermine the beliefs supporting it.

The reference attributes this criticism to Egan and notes Joyce’s response: CDT can use evidence about what an agent is inclined or likely to do. One operational distinction is therefore:

1. **Observed inclination:** “I notice that I am eager to press.” This can legitimately update \(p\).
2. **Hypothetical intervention:** “Suppose I press.” This does not by itself license conditioning on the action as an observation.

That distinction preserves CDT’s causal rationale while allowing self-knowledge. It does not uniquely determine how deliberation should settle when successive observations of one’s intentions keep changing the preferred action. Requirements of stability or “ratifiability” add substantive machinery beyond the basic maximization rule.

The reference’s **Adversarial Offer** creates a related challenge. Two boxes each cost \$1. Yesterday, a predictor placed \$3 in every box it predicted the buyer would not purchase. The buyer may purchase one box or neither.

Let \(X_L,X_R\) be their contents. At least one contains \$3, so

\[
X_L+X_R\ge 3.
\]

With contents causally fixed,

\[
V_C(L)+V_C(R)
=
\mathbb E[X_L+X_R\mid E]-2
\ge 1.
\]

At least one purchase therefore has causal expected net value at least \$0.50; declining yields zero.

Nevertheless, if the predictor is correct on 75% of resulting purchases, the buyer’s observed average profit is

\[
0.75(-1)+0.25(2)=-0.25.
\]

A correct prediction makes the purchased box empty; an incorrect prediction makes it full.

The causal calculation and the losing observed record evaluate different distributions. Critics regard that mismatch as evidence against CDT; defenders must explain why the intervention comparison remains normatively appropriate. Neither simply repeating “correlation is not causation” nor citing the observed losses settles the dispute.

## 7. A practical procedure

For an unfamiliar problem, the following workflow makes the commitments explicit:

1. **Specify the decision point.** What evidence is already available, and which actions or commitments remain feasible?
2. **Specify utility.** Include action costs, indirect effects, risks, and effects on others.
3. **Model dependencies.** Distinguish causal influence from prediction, shared causes, and mere correlation.
4. **Construct each intervention.** Change the action rule and propagate its consequences without rewriting unaffected mechanisms.
5. **Average over uncertainty.** Use the current posterior over background conditions and causal hypotheses for every candidate intervention.
6. **Check self-information and timing.** Has deliberation produced genuine new evidence? Is the alternative an immediate act, an earlier commitment, or a policy installation?
7. **Test robustness.** If plausible causal models disagree, report that dependence rather than presenting one numerical answer as forced by CDT.

The procedure is useful only to the extent that its interventions and causal assumptions are defensible. Expected-utility maximization cannot repair a misspecified causal model.

## Sources

The main source is Wikipedia contributors, “[Causal decision theory](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528),” supplied revision 1381555528, licensed CC BY-SA 4.0. Principal works cited there include Gibbard and Harper, “Counterfactuals and Two Kinds of Expected Utility” (1981); Lewis, “Causal Decision Theory” (1981); Egan, “Some Counterexamples to Causal Decision Theory” (2007); Joyce, “Regret and Instability in Causal Decision Theory” (2012); and Oesterheld and Conitzer, “Extracting Money from Causal Decision Theorists” (2021). The numerical examples and structural-model presentation above are explanatory additions.

## Conclusion

CDT evaluates what actions would bring about, rather than what their occurrence would reveal. Its strength is a disciplined separation of intervention from evidence, especially when common causes make attractive news causally ineffective. Its central difficulty is specifying the counterfactual intervention—and the beliefs held fixed during evaluation—when prediction, self-knowledge, and commitment interact. Applying CDT well therefore requires more than an expected-value calculation: it requires an explicit account of what the agent can change, what remains uncertain, and why.
```

### Available readable reasoning

Extraction: readable reasoning_details blocks joined in saved order.

```text
**Structuring the essay**

I’m thinking about shooting for approximately 2800 words, keeping in mind our budget and word count limits. We have a 16k budget but only need about 6500 tokens. I plan to draft an essay structured into 8 sections, aiming for around 350 words each. It's important to clearly distinguish between claims and sources; for example, I’ll phrase it like, “The source presents…” We also need to include normative aspects to ensure we're not endorsing wrongdoing.

**Exploring CDT and decision-making**

I’m considering how CDT handles decision-making with indifferent or defect twins. It’s interesting to note that it behaves similarly to one-shot prisoner dilemmas, where identical code doesn't imply causation. The payoff matrix could include values like 3, 0, 5, and 1, which raises useful discussions around dependencies. While it might be redundant since Newcomb’s problem already addresses this, it could leave space for a deeper conclusion.

**Clarifying essay structure**

I should include a CC BY-SA attribution if I'm heavily adapting a source, but I don’t need to copy it directly. The user wants an essay, not a legal license mention. When it comes to the reference list, I could include the main sources like Gibbard. 

Now, about the structure: the user asked for a brief conclusion after references. So, I might consider having "References and source note" before the conclusion for clarity. It feels a bit unconventional, but I want to make sure it's fitting for the user's request.**Planning the essay structure**

I’m thinking about how to structure the essay. It’s probably best to place the references before the conclusion to be safe. I need to keep track of my word count too; I aim for around 15,000 words total, but I can produce about 2,800 words now, with a max of 3,000.

I’ve broken down the target count for each section: 135 for the introduction, then varying counts for formal, model, king, Newcomb, policies, hard cases, workflow, and conclusion. I'll compose around 2,800 words total.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/7794638d-665d-4360-b8df-305b0d3ef16d/call_0/request.json)

[Authoritative raw response](../../../../../../runs/7794638d-665d-4360-b8df-305b0d3ef16d/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/7794638d-665d-4360-b8df-305b0d3ef16d/call_1/request.json)

[Authoritative raw response](../../../../../../runs/7794638d-665d-4360-b8df-305b0d3ef16d/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
