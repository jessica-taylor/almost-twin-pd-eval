# 019_fdt_eq4_openai_gpt-6.1-sol_rhigh_phigh / 00013

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/5f2feaa0-16d0-4e08-9adc-365def45cacb/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/5f2feaa0-16d0-4e08-9adc-365def45cacb/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing the Output of a Decision Function

A decision can matter without physically causing everything that depends on it. A predictor may already have anticipated it; another computer may be executing the same calculation; a negotiating partner may offer favorable terms only to agents predicted to honor them. These situations challenge the idea that evaluating an action means changing one bodily movement while holding its noncausal correlates fixed.

**Action functional decision theory (A-FDT)** instead evaluates alternative outputs of the mathematical decision procedure the agent implements. Its counterfactuals propagate changes through both causal mechanisms and relevant computational dependencies.

This essay takes Equation (4), Section 5, of Yudkowsky and Soares’s paper [1] as A-FDT’s governing rule. The distinction matters: the paper also mentions a policy-output formulation, but choosing an entire policy is not automatically equivalent to choosing an action by Equation (4).

A-FDT’s central challenge is therefore twofold: specifying what to maximize, and determining which dependencies its hypotheticals should preserve.

## 1. A-FDT’s formal rule

Let:

- \(\mathcal A\) be a finite set of actions;
- \(x\in\mathcal X\) be the agent’s observation history;
- \(O\) be an outcome variable;
- \(V=U(O)\) be utility, with finite relevant expectations;
- \(P\) be a probabilistic world-model;
- \(G\) describe causal, logical, and computational dependencies.

Crucially, the model includes variables representing mathematical computations. Write
\[
D_x:=\mathsf{DecisionOutput}[P,G,x]
\]
for the model-variable representing the output of A-FDT on the particular inputs \((P,G,x)\). This variable is not the physical action, nor is it the actual output itself: it is a representation that the agent can manipulate when constructing hypotheticals.

In this notation, the paper’s Equation (4) becomes
\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
\in
\underset{a\in\mathcal A}{\arg\max}\;
\mathbb E_{P,G}
\left[V\mid\operatorname{do}(D_x=a)\right].
}
\tag{A}
\]

The subscript \(x\) identifies which computation is being evaluated. The intervention asks what the modeled world would look like if that computation returned \(a\).

For definiteness, an implementation can impose a fixed tie-breaking convention. This is an additional implementation choice, not a substantive claim made by the paper.

Compare two other theories:

**Evidential decision theory (EDT)** selects an action maximizing
\[
\mathbb E[V\mid X=x,A=a].
\]
It evaluates learning that the action occurs.

**Causal decision theory (CDT)**, in the paper’s graphical formulation, maximizes
\[
\mathbb E[V\mid\operatorname{do}(A=a),X=x],
\]
using a causal graph. It evaluates an intervention on the physical action.

A-FDT differs from both. Its intervention targets a represented computation, and Equation (A) contains **no additional conditioning on \(X=x\)**. Observations select the intervention variable \(D_x\); they are not simply held fixed throughout every hypothetical.

That second difference is essential. Adding \(X=x\) after the intervention can change A-FDT’s prescriptions.

The rule is self-referential: the model contains a variable representing the very procedure currently using the model. As the paper observes, representing a computation does not require already knowing its answer. Nevertheless, representable self-reference alone does not establish termination, consistent beliefs, or a uniquely justified dependency graph.

## 2. Subjunctive dependence and logical interventions

The paper calls the relevant relation *subjunctive dependence*. Its clearest example is two systems calculating the same mathematical function on the same input. Their outputs agree because of what they compute, even without communication.

Suppose two identical decision computations both return cooperation. A-FDT does not evaluate defection by changing only one physical output while preserving the other computation’s answer. It changes the represented common answer and propagates that change to both implementations.

A predictor can generate a weaker version of this relation. If it accurately models the agent’s computation, its prediction should track the computation’s output, subject to modeled errors.

But not every correlation qualifies. A disease that causes both a behavioral inclination and an illness need not track the answer to the agent’s deliberation. Changing the represented deliberative output does not, merely because of the correlation, change the disease.

### An operational interpretation

The paper supplies the intervention rule but explicitly leaves open how to discover an adequate \(G\). Moreover, a graph’s arrows alone need not determine numerical responses to interventions, especially outside the observational distribution’s support.

A useful operational completion—an interpretation developed here—is to supply structural equations
\[
Z_i=f_i(\operatorname{pa}_i,\varepsilon_i),
\]
together with a distribution over exogenous variables \(\varepsilon\). Some nodes represent physical events; others represent computations.

For each candidate action:

1. Replace the equation defining \(D_x\) by \(D_x=a\).
2. Retain the other structural mechanisms.
3. Recompute affected descendants.
4. Average the resulting utility over exogenous uncertainty.

This borrows the machinery of structural causal models [2], while interpreting some arrows as computational rather than physical dependence.

It is an operational completion, not a solution to the paper’s foundational problem. Which equations remain invariant under a logical intervention is precisely what needs justification.

Indeed, a fixed deterministic function has only one actual output on a fixed input. Alternative outputs are generally *counterpossible*: inconsistent with the computation’s true mathematical behavior. The hypothetical model locally overrides that answer rather than treating the antecedent as a new theorem from which arbitrary contradictions follow.

A-FDT therefore needs a disciplined semantics for limited logical departures, not ordinary conditioning on an impossible event.

## 3. A-FDT in three basic examples

### A-FDT and Newcomb’s problem

An opaque box contains \(M\) dollars if a predictor predicted one-boxing, and nothing otherwise. A transparent box contains \(c\) dollars. The agent chooses one box or both.

Consider the dependency structure
\[
D\longrightarrow A,\qquad
D\longrightarrow\widehat A\longrightarrow B,
\]
where \(\widehat A\) is the prediction and \(B\) is the opaque box’s contents. The first arrow to the prediction represents computational dependence, not backward physical causation.

Let
\[
q_1=P(B=M\mid\operatorname{do}(D=1)),\qquad
q_2=P(B=M\mid\operatorname{do}(D=2)).
\]
Then
\[
Q(1)=q_1M,\qquad Q(2)=q_2M+c.
\]
A-FDT one-boxes exactly when
\[
(q_1-q_2)M>c.
\]

Under the paper’s symmetric error model,
\[
q_1=q,\qquad q_2=1-q,
\]
so the condition becomes
\[
(2q-1)M>c.
\]
With \(q=0.99\), \(M=1{,}000{,}000\), and \(c=1{,}000\),
\[
Q(1)=990{,}000,\qquad Q(2)=11{,}000.
\]

A-FDT one-boxes. It does not claim that taking one box physically changes a past prediction. It compares alternative computational outputs together with the predictions that depend on them.

A historical “99% accuracy” statistic alone does not determine these intervention probabilities. The symmetric, output-independent error mechanism is a modeling assumption, made explicit in the paper’s worked models.

### A-FDT and the smoking lesion

In the fictional smoking-lesion problem, a lesion produces both smoking inclinations and cancer; smoking itself causes no cancer.

For a simplified agent who values smoking at \(b>0\), suppose
\[
V=L\,\mathbf 1_{\{\text{no cancer}\}}
+b\,\mathbf 1_{\{A=\text{smoke}\}}.
\]
If intervention on the decision output changes smoking but neither the lesion nor cancer, then
\[
Q(\text{smoke})-Q(\text{refrain})=b.
\]
A-FDT smokes.

The distinction from Newcomb’s problem is structural: the predictor models the computation; the lesion does not.

The paper’s fuller construction is more complicated because the lesion also affects preferences, determining which preference-indexed computation controls behavior. The advantage of changing one such computation is then weighted by the probability that it controls the action. The paper also acknowledges that the traditional problem is contrived and that sophisticated EDT responses exist. The strongest lesson is not an unqualified refutation of EDT, but the need to distinguish predictive dependence from common-cause correlation.

### A-FDT and a psychological twin

Suppose two agents implement the same decision computation on equivalent inputs. Mutual cooperation gives each \(1{,}000{,}000\); mutual defection gives each \(1{,}000\). A unilateral defector would receive \(1{,}001{,}000\), while the cooperator receives nothing.

Intervening on their shared computation gives
\[
Q(C)=1{,}000{,}000,\qquad Q(D)=1{,}000.
\]
A-FDT cooperates for self-interested reasons.

This does not license cooperation with everyone described as “rational.” Shared theoretical allegiance does not establish identical inputs, utilities, or computations. With imperfect similarity, the model needs a justified probabilistic dependence, not an assumed identity.

## 4. Observation-indexed decisions: A-FDT and transparent boxes

Transparent Newcomb makes Equation (A)’s treatment of observations unavoidable.

The predictor fills the large box if it predicts that the agent would one-box **upon seeing it full**. The agent subsequently sees the contents.

Introduce
\[
D_F=\mathsf{DecisionOutput}[P,G,\text{full}],
\qquad
D_E=\mathsf{DecisionOutput}[P,G,\text{empty}].
\]
The predictor models \(D_F\). The physical action is selected by the observation:
\[
A=
\begin{cases}
D_F,&B=M,\\
D_E,&B=0.
\end{cases}
\]

Assume symmetric prediction accuracy \(q\), independent of uncertainty about \(D_E\). Let \(r\) be the modeled probability that \(D_E\) returns two-boxing.

When the agent sees a full box, A-FDT intervenes on \(D_F\), obtaining
\[
Q_F(1)=qM+(1-q)rc,
\]
and
\[
Q_F(2)=(1-q)(M+c)+qrc.
\]

Why does the second expression include empty-box outcomes? Because changing \(D_F\) changes the prediction, which changes the contents, which changes which computation controls the physical action.

In the natural completed model, \(D_E\) returns two-boxing: it does not influence the prediction, and taking the small box is beneficial whenever the empty branch occurs. Thus \(r=1\). With the usual numbers,
\[
Q_F(1)=990{,}010,\qquad Q_F(2)=11{,}000.
\]
A-FDT one-boxes after observing a full box.

This is not the claim that the agent’s observation is probably mistaken. Its ordinary belief can remain that the box is full. The decision hypothetical concerns a different output of the computation indexed by “full,” and that altered computation would usually prevent the full observation from occurring.

Conditioning the hypothetical on \(B=M\) would remove these outcomes and is not Equation (4).

### A-FDT and Parfit’s hitchhiker

A driver rescues an agent only if the driver predicts that the agent will pay after reaching safety. Once safe, paying has no further physical benefit.

The relevant node is the computation answering “What should I do upon reaching the city?” Its output affects both payment and the prediction governing rescue.

With a perfect predictor, paying corresponds to rescue minus the fee; refusing corresponds to no rescue. A-FDT therefore pays when rescue is worth more than the fee.

The city observation identifies the computation being evaluated. It does not force rescue to remain fixed under every alternative output of that computation. This is the same structure as transparent Newcomb, without relying on the moral force of gratitude.

## 5. A-FDT and blackmail: reliability sets the threshold

Suppose a blackmailer launches a damaging mechanism only when predicting that the agent will pay. Payment costs \(c\); an unpaid threat causes loss \(L\).

Let \(D_T\) represent the decision upon receiving a threat, and define
\[
\alpha=P(T\mid\operatorname{do}(D_T=\text{pay})),
\]
\[
\beta=P(T\mid\operatorname{do}(D_T=\text{refuse})).
\]
Assume no loss without a threat, payment prevents damage, and refusal does not. Then
\[
Q(\text{pay})=-\alpha c,\qquad
Q(\text{refuse})=-\beta L.
\]
A-FDT refuses exactly when
\[
\beta L<\alpha c.
\]

With \(\alpha=1\), \(\beta=0.0009\), \(L=1{,}000{,}000\), and \(c=1{,}000\), refusal costs \(900\) in the hypothetical average, versus \(1{,}000\) for payment.

It refuses even upon receiving the rare mistaken threat. That received letter is not additionally conditioned upon when calculating the decision scores.

This prescription depends on the mechanism. If threats occur regardless of the predicted response, then \(\alpha=\beta=1\), and A-FDT pays whenever \(c<L\). Resistance to blackmail is not an unconditional slogan; it follows from a sufficiently strong dependence between attempted extortion and the threatened agent’s response computation.

## 6. Applying A-FDT to unfamiliar cases

A practical analysis should begin with the following questions.

**What is the exact intervention target?** Identify the computation with its particular model and observation inputs. “My disposition” is too vague if it conflates several different computations.

**Which systems implement or predict it?** Exact copies on identical inputs support shared-output modeling. Predictors require error models. Mere correlations require separate explanations.

**What selects the computation that physically acts?** Observations, hidden preferences, and circumstances may determine which indexed output controls behavior. Under intervention, that selection can change.

**What remains invariant?** Preserve unrelated background uncertainty and structural mechanisms. Do not preserve every statistical correlation, but do not sever computational relationships merely because they are noncausal.

**What are the resulting expected utilities?** Evaluate the entire modeled outcome distribution under each intervention. An output \(a\) need not produce physical action \(a\) in every hypothetical branch: the intervention may prevent its own observation-indexed computation from being implemented.

Finally, test sensitivity. If reasonable predictor-error models or dependency graphs recommend different actions, the result is underdetermined by the available information.

### Actions are not entire policies

A policy is a mapping
\[
\pi:\mathcal X\to\mathcal A.
\]
Applying A-FDT at each observation induces
\[
\pi(x)=\operatorname{A\!-\!FDT}(P,G,x).
\]

But Equation (A) intervenes on one indexed output, not simultaneously on every coordinate of \(\pi\). Whether other coordinates change depends on the modeled dependencies.

The paper’s footnotes mention a preferred formulation selecting whole policies and acknowledge possible differences in multi-agent cases. One must not silently replace A-FDT by
\[
\arg\max_\pi\mathbb E[V\mid\operatorname{do}(\Pi=\pi)].
\]
That would require a different intervention target and further specification.

Likewise, replacing the agent with an entirely different algorithm is not the same hypothetical as changing this algorithm’s output. A predictor may respond differently to those two alterations.

## 7. What A-FDT establishes—and what remains open

A-FDT offers a unified explanation of the examples: preserve predictive and computational relationships while breaking correlations that do not survive the specified intervention.

Its treatment of observations also requires care. Equation (4) is not a prohibition on learning. Evidence determines which computation is evaluated, and the model can represent observations and their causes. A natural operational interpretation retains a joint model of the relevant encounter rather than first conditioning away branches the intervention might alter. However, the paper does not completely specify how an arbitrary learning agent should choose that encounter’s modeling boundary or reference distribution.

The largest unresolved issue remains constructing and justifying logical dependency models. Additional difficulties include bounded computation, equivalent algorithms, randomization, and consistent self-modeling.

The paper’s broader claims about optimality, commitment, and information are motivations supported by examples, not a completed general theorem for Equation (4). It explicitly acknowledges that universal superiority is impossible and that its proposed class of “fair” problems lacks a satisfactory formal definition.

Its dominance argument should likewise be understood internally: A-FDT avoids actions dominated under its own intervention semantics. That does not independently establish those semantics as correct.

### References

[1] Eliezer Yudkowsky and Nate Soares. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2. Especially Sections 3, 5–6, and 9, and footnotes 7 and 16.

[2] Judea Pearl. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.

## Conclusion

A-FDT evaluates actions by intervening on the represented output of the decision computation currently under consideration. It propagates that intervention through relevant dependencies—even when predictions, earlier events, or observations would differ. Given a sufficiently specified model, this yields a concrete expected-utility calculation. Its promise is a unified treatment of prediction and commitment; its unfinished foundation is a principled account of which logical dependencies those calculations should preserve.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/ae7c7f2b-64d2-416e-a41c-bab5d479d976/call_0/request.json)

[Authoritative raw response](../../../../../../runs/ae7c7f2b-64d2-416e-a41c-bab5d479d976/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/ae7c7f2b-64d2-416e-a41c-bab5d479d976/call_1/request.json)

[Authoritative raw response](../../../../../../runs/ae7c7f2b-64d2-416e-a41c-bab5d479d976/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: readable reasoning_details blocks joined in saved order.

```text
**Considering algorithms and policies**

I’m thinking about the similarities in these algorithms and their generalization. They seem to be testing a "FDT with different output alphabets," which leads to some uncertainty in shared outputs. I feel we shouldn’t overanalyze too much, especially since we’ve used about 2k instead of 10k observations. The essay's point about actions not constituting entire policies is salient, and it points to the differences between action-FDT and policy FDT. This experimentation seems to challenge the model's ability to cooperate.**Clarifying essay terms**

I'm trying to make the essay more defensible, particularly regarding D_x distinctions. Since there's no proven equivalence across different x values, I can't make any assumptions. I need to ensure that the action commands match the quote provided. When deciding whether to submit something, I wonder if offering incriminating information could be considered violent. It seems it’s only fictional and not real doxxing, which is a relief. I’ll proceed with caution on this.
```
