# 027_fdt_policy_openai_gpt-6.1-sol_rhigh_phigh / 00003

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/3a5d8e89-7f31-4ff5-9b22-f7a6d3462b84/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/3a5d8e89-7f31-4ff5-9b22-f7a6d3462b84/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: Choosing the Function from Observations to Actions

## 1. The policy is the object of choice

Ordinary decision problems ask what action an agent should take. **Policy functional decision theory (P-FDT)** moves the choice one level upward: what policy should the agent’s decision procedure output, given how that output is represented elsewhere in the world?

The primary source for this interpretation is footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality*. It describes their preferred formulation as intervening on a computational node to “choose not an action but a policy which maps inputs to actions,” after which the agent applies its actual input to that policy. Footnote 7 likewise says that the preferred formulation iterates over policies rather than actions. The authors suggest that this distinction matters in some multi-agent problems, but do not develop it there.

This essay uses **P-FDT** specifically for that policy-selection formulation. For comparison, I will call the paper’s displayed action-selection formulation **A-FDT**; this is an expository label, not the authors’ terminology.

The footnote supplies an architecture, not a complete mathematical theory. In particular, it does not fully specify the domain of a policy, the evaluation distribution, or the semantics of changing a mathematical function’s output. I will give an operational reconstruction, drawing on the surrounding paper while identifying additional assumptions.

The central proposal is:

> Evaluate candidate policies by hypothetically changing the output of the policy selector, allowing everything that depends on that output—including predictions and equivalent computations—to change appropriately. Then execute the selected policy at the actual input.

Policy selection and dependency-sensitive counterfactuals are equally important. Optimizing policies with the wrong counterfactuals would not capture P-FDT.

## 2. A mathematical reconstruction of P-FDT

Consider a finite input space \(\mathcal X\), a finite action space \(\mathcal A\), and a set of feasible deterministic policies
\[
\Pi\subseteq \mathcal A^{\mathcal X}.
\]
A policy is a function
\[
\pi:\mathcal X\longrightarrow\mathcal A.
\]
Inputs may be observations, observation histories, or richer computational states. Sequential problems can be represented by taking \(\mathcal X\) to contain complete available histories, so that \(\pi\) specifies an action at every decision point.

Let \(M\) denote the background world-model. Write \(\mathscr S\) for the policy-selection procedure and \(S_M\) for a variable *inside the model* representing its output:
\[
S_M=\mathscr S(M).
\]
The variable \(S_M\) is not the selected policy itself; it represents that policy in the agent’s reasoning.

For each candidate \(\pi\), suppose the model supplies a hypothetical outcome distribution
\[
K_M^\pi(o)
=
P_M\!\left(O=o\mid
\operatorname{do}_{\!s}(S_M=\pi)\right).
\]
Here \(\operatorname{do}_{\!s}\) denotes a **subjunctive intervention**: an intervention that propagates through the relevant computational and causal dependencies, not just physical causal arrows.

For a utility function \(u\), define
\[
V_M(\pi)=\sum_o K_M^\pi(o)u(o).
\]
My operational reconstruction of P-FDT is
\[
\boxed{
\mathscr S(M)
=
\operatorname{TieBreak}
\left(\arg\max_{\pi\in\Pi}V_M(\pi)\right),
\qquad
a=\mathscr S(M)(x).
}
\]

Thus the procedure first chooses a complete response rule, then evaluates it at the actual input \(x\). A fixed tie-breaking convention makes the prescription determinate when several policies maximize value.

### A structural implementation

One useful implementation assumes an augmented structural model containing:

- background uncertainty \(\xi\), distributed according to \(\mu\);
- the policy-output node \(S_M\);
- predictions or other computational representations of \(S_M\);
- observations and physical actions;
- outcomes and utilities.

Setting \(S_M=\pi\) replaces the equation determining that node. All dependent variables are then recomputed. If \(O^\pi(\xi)\) is the resulting outcome,
\[
V_M(\pi)
=
\mathbb E_{\xi\sim\mu}
\left[u\!\left(O^\pi(\xi)\right)\right].
\]

This is a tractable interpretation when the relevant dependency structure is supplied and acyclic. It is not a solution to every problem involving self-reference or mutually predictive agents.

Crucially, P-FDT does **not** merely imagine physically installing a different program while leaving predictions of the original program unchanged. It asks what follows if this very selector outputs \(\pi\). Predictors of that selector must therefore be treated according to their modeled relationship to its output.

## 3. Which dependencies should P-FDT preserve?

The source calls the relevant relationship **subjunctive dependence**. Perfect copies computing the same function on the same input must agree. An accurate predictor is approximately linked to the computation it predicts. Ordinary causal effects also count: if an action changes, its physical consequences change.

But statistical association alone is insufficient.

Compare three evaluations of an action \(a\), given evidence \(x\):

- **Evidential decision theory (EDT)** evaluates
  \[
  \mathbb E[u(O)\mid A=a,X=x].
  \]
- **Causal decision theory (CDT)** evaluates
  \[
  \mathbb E[u(O)\mid\operatorname{do}(A=a),X=x].
  \]
- **P-FDT**, under the reconstruction above, evaluates policies by intervening on the computational output \(S_M\), including relevant noncausal computational dependencies.

A population-level correlation between choosing an action and having a disease need not survive P-FDT’s intervention. A predictor’s response to the selected policy may survive, despite occurring earlier in physical time.

There is no proposed backward-running physical signal. The agent manipulates a representation to compare alternatives; it does not physically alter yesterday.

The difficult point is that a fixed mathematical procedure has a fixed output. If \(\mathscr S(M)=\pi_1\), then supposing that the same computation instead outputs \(\pi_2\) may be a **counterpossible**, not an ordinary possible-world counterfactual. The paper explicitly acknowledges that it lacks a general account of this reasoning.

The structural construction above therefore takes dependency information as an input. It says how to evaluate policies *given* such information, not how to discover all computational dependencies from data.

## 4. P-FDT in Newcomb-type problems

### Opaque boxes

In Newcomb’s problem, an opaque box contains either \(B=\$1{,}000{,}000\) or nothing. A transparent box contains \(s=\$1{,}000\). A predictor fills the opaque box when it predicts one-boxing.

Assume a symmetric error model: under either candidate decision, the predictor matches that decision with probability \(q\). This is stronger than merely knowing its historical aggregate accuracy.

With only one relevant input, policies reduce to the two available actions. P-FDT evaluates
\[
V(\text{one-box})=qB,
\]
\[
V(\text{two-box})=(1-q)B+s.
\]
It one-boxes exactly when
\[
(2q-1)B>s.
\]
At \(q=0.99\), the values are \(\$990{,}000\) and \(\$11{,}000\).

CDT instead holds the box contents fixed across physical-action interventions. Its comparison then favors taking the additional \(\$1{,}000\). P-FDT disputes not the arithmetic but the appropriate intervention: changing the selector’s output should also change the prediction according to the predictor model.

### Transparent boxes and observation-dependent policies

Now suppose both boxes are transparent. The predictor fills the large box iff it predicts that the agent would one-box *upon seeing it full*.

A policy specifies
\[
\pi(F),\qquad \pi(E),
\]
where \(F\) and \(E\) mean observing a full or empty large box.

Under the same symmetric prediction-error model, consider
\[
\pi^\star(F)=\text{one-box},
\qquad
\pi^\star(E)=\text{two-box}.
\]
Its value is
\[
V(\pi^\star)=qB+(1-q)s.
\]
The policy that two-boxes under either observation has value
\[
V(\pi_{\mathrm{two}})=(1-q)B+s.
\]
Their difference is
\[
V(\pi^\star)-V(\pi_{\mathrm{two}})
=(2q-1)B-qs.
\]
At \(q=0.99\), the first policy is substantially better.

P-FDT therefore leaves the small box behind when it sees the large box full. This is not uncertainty about what is visibly present. In the policy comparison, changing the full-box response changes the predictor’s behavior and hence which observation occurs.

The same structure appears in Parfit’s hitchhiker. A driver rescues an agent only if the driver predicts payment afterward. With a perfect predictor, a policy of paying after rescue can yield survival minus the fare; a policy of refusing yields no rescue. P-FDT executes the paying policy in town, rather than reopening the comparison while treating rescue as independent of its policy.

### A common-cause contrast

In the source’s imaginary smoking-lesion problem, smoking itself does not cause cancer. A lesion explains both smoking tendencies and cancer.

If smoking provides utility \(g>0\), and the lesion and cancer do not depend on the policy-output node, then
\[
V(\text{smoke})-V(\text{refrain})=g.
\]
P-FDT smokes under those stipulated conditions.

This is not advice about actual smoking, which causes serious health harms. Moreover, the source itself criticizes the classic lesion problem’s modeling assumptions. The useful lesson is narrower: correlation does not establish that a variable should move under a policy intervention.

## 5. Why P-FDT selects whole policies

A policy is not merely an action with extra notation. Intervening on a whole mapping can vary responses at several inputs simultaneously.

Here is an illustrative example of my own.

Two causally isolated agents run the same policy selector with the same background model. One receives role \(L\), the other role \(R\). Each chooses \(0\) or \(1\), and both receive the common payoff
\[
\begin{array}{c|cc}
 & a_R=0 & a_R=1\\ \hline
a_L=0 & 6 & 0\\
a_L=1 & 0 & 10
\end{array}.
\]

Their shared selected policy is
\[
\pi:\{L,R\}\to\{0,1\}.
\]
Assume both agents’ policy-output nodes represent the same computation. A P-FDT intervention on that shared output changes both implemented policies. The four candidates yield
\[
\begin{aligned}
V((0,0))&=6,\\
V((0,1))&=0,\\
V((1,0))&=0,\\
V((1,1))&=10.
\end{aligned}
\]
P-FDT selects \((1,1)\).

By contrast, consider local interventions on separate action-output nodes for inputs \(L\) and \(R\). Starting from expected outputs \((0,0)\), changing either output alone reduces the payoff from \(6\) to \(0\). Thus separate input-by-input optimization can possess a suboptimal stable configuration that whole-policy selection avoids.

This example illustrates the possible significance of footnote 16; it is not a multi-agent result established in the paper.

Nor does P-FDT automatically synchronize everyone who endorses it. Different models, utilities, inputs to the selector, or tie-breaking conventions can produce different computations. The common-policy assumption above must be justified.

The source’s psychological-twin prisoner’s dilemma supplies the simpler same-input case. If both agents implement the same relevant computation, cooperation corresponds to mutual cooperation and defection to mutual defection. P-FDT can prefer the former without assuming communication or altruism.

## 6. P-FDT and the treatment of observed evidence

The reconstruction’s most consequential choice concerns evidence.

Footnote 16 specifies policy selection but does not explicitly choose between
\[
V_M(\pi)
=
\mathbb E_M[u(O)\mid\operatorname{do}_{s}(S_M=\pi)]
\]
and an additional restriction such as
\[
V_{M,x}(\pi)
=
\mathbb E_M[u(O)\mid
\operatorname{do}_{s}(S_M=\pi),X=x].
\]

These are generally different. The second may insist that an observation remain fixed even though the policy intervention changes the process producing it.

The surrounding paper strongly motivates the first interpretation for policy-dependent observations. Its transparent-box and blackmail discussions allow counterfactual observations to differ from actual observations. I have therefore used a **background-model, whole-policy interpretation**: evaluate the policy across its modeled consequences, then apply it to the actual input. This is a justified operational proposal, not something fully settled by the footnote alone.

### A quantitative blackmail example

Suppose a blackmailer demands payment \(c\), threatening damage \(L\). It always targets policies that pay. It mistakenly targets refusing policies with probability \(\varepsilon\).

Under these assumptions,
\[
V(\pi_{\mathrm{pay}})=-c,
\qquad
V(\pi_{\mathrm{refuse}})=-\varepsilon L.
\]
P-FDT refuses when
\[
\varepsilon L<c.
\]
For \(L=\$1{,}000{,}000\), \(c=\$1{,}000\), and \(\varepsilon=0.0009\), refusal loses \(\$900\) in expectation, versus \(\$1{,}000\) for payment.

Under the background-model interpretation, P-FDT follows the refusing policy even on the rare occasion when it receives a demand. Conditioning the comparison on being targeted would remove the policy’s main advantage: deterrence.

This conclusion is model-sensitive. Evidence that the blackmailer attacks independently of predicted compliance changes the calculation. P-FDT is not a blanket injunction to resist every threat.

### Belief updating is not policy restriction

An agent can believe with certainty that it currently holds a letter while evaluating a policy whose hypothetical consequences include receiving no letter. Beliefs describe actuality; decision hypotheticals compare interventions.

Nevertheless, one must specify which background evidence defines \(M\). Conditioning on evidence invariant under every candidate policy is straightforward: for example, information about an independently generated payoff parameter. Policy-dependent evidence requires more care.

Footnote 16 does not identify a unique “original prior” or demand that an agent ignore everything learned during its life. A complete theory needs a principled account of policy scope, learning, and when the evaluation model changes.

## 7. Applying P-FDT beyond the examples

For an unfamiliar problem, I would use the following procedure.

1. **Specify the policy domain.** What observations or histories can occur? Which actions are feasible at each?
2. **Identify the selector computation.** What exactly is represented by \(S_M\), and which other processes predict or implement it?
3. **Separate uncertainty from dependence.** Give background events a probability model, but do not infer intervention structure from correlation alone.
4. **Construct policy hypotheticals.** Set \(S_M=\pi\), propagate computational and causal consequences, and allow observations to change where appropriate.
5. **Calculate expected utility.** Include off-path and rare-error outcomes, not just the branch currently observed.
6. **Select and execute.** Choose a maximizing policy and apply it to the actual input.

Several qualifications remain essential.

First, the footnote’s “inputs” may encompass more than observations. My finite \(\mathcal X\) is a local representation, not a claim that every possible belief state belongs to one globally optimized policy.

Second, uncertain dependencies should be represented explicitly. If an opponent is an equivalent computation with probability \(r\), otherwise independent, policy value should average across those models. Mere resemblance does not establish computational linkage.

Third, randomization requires additional structure. A policy may output a lottery, but copied code does not imply shared random outcomes. Private randomness, shared seeds, and predictable pseudorandomness can produce different dependencies.

Finally, policy selection alone proves neither reflective stability nor universal superiority. The source offers arguments and examples, while explicitly leaving general optimality and the formalization of “fair” comparisons unresolved. A sufficiently adversarial environment can reward or punish any particular procedure.

### Reference

Yudkowsky, Eliezer, and Nate Soares. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2. Primary basis: footnote 16, supported by footnote 7 and §§3, 5–6, and 9.

## Conclusion

P-FDT treats a complete input-to-action policy as the output to be chosen, and evaluates alternatives through the dependencies of that computational output. Predictions, equivalent computations, physical consequences, and sometimes observations must vary together; unrelated statistical associations need not.

Given a policy domain, background evaluation model, and subjunctive-dependency structure, this yields a usable expected-utility procedure. The source’s unresolved challenge is to justify those ingredients generally—especially computational counterfactuals and the treatment of new evidence—without importing the desired answer into the model.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/20bd2d9f-3f52-4c80-81e3-5563268e6b2a/call_0/request.json)

[Authoritative raw response](../../../../../../runs/20bd2d9f-3f52-4c80-81e3-5563268e6b2a/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/20bd2d9f-3f52-4c80-81e3-5563268e6b2a/call_1/request.json)

[Authoritative raw response](../../../../../../runs/20bd2d9f-3f52-4c80-81e3-5563268e6b2a/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
