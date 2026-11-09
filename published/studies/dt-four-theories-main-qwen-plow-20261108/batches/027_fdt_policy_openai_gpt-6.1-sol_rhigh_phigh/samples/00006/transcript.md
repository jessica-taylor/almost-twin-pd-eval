# 027_fdt_policy_openai_gpt-6.1-sol_rhigh_phigh / 00006

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/6c9c13ea-bef2-480d-84f4-cc3885c57df5/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/6c9c13ea-bef2-480d-84f4-cc3885c57df5/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: Choosing the Policy Behind the Action

A decision can matter in more ways than by causing events downstream of a bodily movement. Another agent may have predicted it; a simulation may reproduce it; several copies of the same program may compute related decisions. **Policy functional decision theory (P-FDT)** evaluates choices while preserving these computational dependencies.

Its distinctive object of choice is a **policy**: a function specifying actions for different inputs. The guiding question is not merely, “What would happen if I performed this act?” It is, “What would happen if this very policy-selection procedure returned this policy?”

The primary source for this account is footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality* (arXiv:1710.05060v2). That passage says their preferred formulation intervenes on the decision-function node to “choose not an action but a policy which maps inputs to actions,” after which the agent applies its inputs to select an action. Footnote 7 similarly describes policies as mappings from observations to actions.

This is a short specification, not a complete formal theory. Below, I distinguish its central commitment from an operational reconstruction that makes it usable.

## 1. From Actions to Policies

Let \(\mathcal X\) be a finite set of possible inputs and \(\mathcal A\) a finite action set. A deterministic policy is a function

\[
\pi:\mathcal X\longrightarrow\mathcal A.
\]

Write \(\Pi\subseteq\mathcal A^{\mathcal X}\) for the available policies. An input can encode an observation history, private information, or a role in a game. Sequential problems can be represented by policies mapping histories to next actions.

Two functions must be kept separate:

- the **policy selector** \(\mathsf S\), which returns a policy;
- the selected policy \(\pi\), which returns an action.

Given a model \(M\), the architecture is

\[
\pi^\star=\mathsf S(M),
\qquad
a^\star=\pi^\star(x).
\]

Choosing a policy does **not** mean selecting a rival decision theory and pretending to implement it. The selector remains fixed. P-FDT evaluates alternative outputs of that same selector, including corresponding changes in systems that represent or reproduce its output.

For comparison, causal decision theory (CDT) ordinarily evaluates an intervention on the physical action:

\[
a_{\mathrm{CDT}}\in
\arg\max_a
\mathbb E[U(O)\mid \operatorname{do}(A=a),X=x].
\]

Evidential decision theory (EDT), in its straightforward form, instead evaluates

\[
a_{\mathrm{EDT}}\in
\arg\max_a
\mathbb E[U(O)\mid A=a,X=x].
\]

P-FDT changes both the object of intervention—from an action to a policy-valued computational output—and the dependency structure preserved under intervention. Merely optimizing over policies is therefore insufficient: one could also construct causal or evidential policy-selection theories.

## 2. A Mathematical Reconstruction of P-FDT

Let \(M\) contain:

1. uncertain facts about the environment;
2. an outcome variable \(O\) and bounded utility function \(U\);
3. representations of relevant computations;
4. instructions for constructing counterfactuals about those computations.

Let \(Q_M\) be a variable **inside the model** representing the policy returned by \(\mathsf S(M)\). Distinguish this representation from the actual returned policy.

For each candidate \(\pi\), suppose the model supplies a probability distribution

\[
K_M^\pi(o)
=
P_M\!\left(
O=o\mid \operatorname{do}_{s}(Q_M=\pi)
\right).
\]

Here \(\operatorname{do}_{s}\) denotes a **subjunctive intervention**, not necessarily a physical causal intervention. It means: construct a hypothetical in which the policy selector returns \(\pi\), then propagate that supposition through the relevant dependencies.

The resulting rule is

\[
\boxed{
\begin{aligned}
V_M(\pi)&=\sum_o K_M^\pi(o)U(o),\\
\mathsf S(M)&=\operatorname{TieBreak}
\left(\arg\max_{\pi\in\Pi}V_M(\pi)\right),\\
\mathrm{P\text{-}FDT}(M,x)&=[\mathsf S(M)](x).
\end{aligned}}
\]

Finite policy sets and bounded utilities ensure that the maximization exists. A specified tie-breaker makes the selector a function, which matters when other systems predict it.

This equation is **my reconstruction**, not an equation printed in footnote 16. The footnote establishes policy-valued selection; the paper’s broader discussion motivates subjunctive intervention and expected-utility maximization. It does not uniquely determine the kernels \(K_M^\pi\).

One operational implementation uses structural equations. Let \(W\sim\mu_M\) represent background uncertainty, and specify equations for observations, predictions, actions, and outcomes. Schematically,

\[
Y=h(Q_M,W),\qquad
X=g(Y,W),\qquad
A=Q_M(X),\qquad
O=f(A,Y,W).
\]

To evaluate \(\pi\), override \(Q_M\) with \(\pi\) and recompute the dependent variables. Then

\[
V_M(\pi)=
\mathbb E_{W\sim\mu_M}[U(O_\pi(W))].
\]

The arrows here can express computational dependence, not just temporal causation. A prediction made yesterday may depend on the same abstract policy that controls tomorrow’s action.

## 3. Which Dependencies Should Change?

The source calls the relevant relation **subjunctive dependence**. Roughly, systems computing or reliably representing the same function should continue to correspond in decision hypotheticals.

Three cases illustrate the distinction.

**Ordinary causal effects.** If the policy produces an action that opens a door, changing the policy can change whether the door opens. P-FDT includes ordinary causal consequences.

**Computational correspondence.** If another machine runs the same policy selector on the same model, its selected policy must change together with \(Q_M\). If it then receives a different input, however, its action is \(\pi(x')\), not necessarily \(\pi(x)\). Sharing a policy does not require identical actions.

**Statistical common causes.** Suppose an illness causes both a behavioral inclination and a medical outcome. Changing the policy selector’s output does not thereby remove the illness. The policy intervention should not preserve every correlation found by conditioning on observed behavior.

These distinctions require a mechanistic model. Two agents’ both being intelligent—or both endorsing P-FDT—does not establish that their policies move together. Their information, utilities, models, and implementations may differ. Similarly, a predictor’s historical accuracy does not automatically specify how its predictions vary across candidate policies.

There is also an unavoidable logical difficulty. A fixed deterministic selector has only one output on a fixed input. Supposing otherwise may be **counterpossible**, rather than merely physically unrealized. The paper explicitly acknowledges that satisfactory general semantics for such suppositions remain undeveloped.

The structural approach handles a restricted version: override one represented computational output while retaining specified relationships elsewhere. It does not require believing that contradictions are genuinely possible, nor that actions send signals backward in time. Nevertheless, choosing the right structural relationships remains substantive work.

## 4. P-FDT in Newcomb’s Problem

An opaque box contains \(M=\$1{,}000{,}000\) if a predictor predicts one-boxing, and nothing otherwise. A transparent box contains \(c=\$1{,}000\). The agent can take only the opaque box or both.

With no decision-relevant variation in inputs, the policies reduce to two constant functions. Assume that under either policy the predictor correctly predicts its action with probability \(p\), and otherwise predicts the opposite. This symmetric error model is an additional specification, stronger than simply reporting aggregate accuracy.

P-FDT assigns

\[
V(\pi_{\mathrm{one}})=pM,
\qquad
V(\pi_{\mathrm{two}})=(1-p)M+c.
\]

Thus one-boxing is selected exactly when

\[
(2p-1)M>c.
\]

At \(p=0.99\), the values are \(\$990{,}000\) and \(\$11{,}000\).

The predictor’s earlier behavior varies in these hypotheticals because its prediction represents the selected policy. This is not a claim that taking one box physically changes yesterday’s box-filling.

Contrast a fictional medical problem in which a lesion causes both a preference for smoking and cancer, while smoking itself has no medical effect. If smoking provides benefit \(b>0\), and neither the lesion nor cancer subjunctively depends on the policy output, then

\[
V(\pi_{\mathrm{smoke}})
-
V(\pi_{\mathrm{refrain}})
=b.
\]

P-FDT selects smoking in that fictional model. Statistical evidence of illness is not a benefit obtainable by selecting abstention.

The source itself notes substantial complications in formalizing the smoking-lesion example, particularly about self-knowledge and preferences. Its useful lesson is the dependency distinction, not an unqualified verdict on every formulation—and certainly not advice about real smoking.

## 5. Observations: Selecting a Response Without Freezing the Input

The most delicate issue concerns evidence. In the reconstruction above, the selector evaluates whole policies using a common model \(M\); the actual input \(x\) is then supplied to the selected policy. Why not condition every candidate on \(X=x\)?

Because \(X\) may itself depend on which policy is selected. Conditioning on it can eliminate precisely the dependency that makes one policy preferable.

Consider **P-FDT in transparent Newcomb’s problem**. Both boxes are visible. The predictor fills the large box if it predicts that the agent would one-box **upon seeing it full**.

Write \(F,E\) for the inputs “full” and “empty,” and \(1,2\) for the actions. A policy specifies both \(\pi(F)\) and \(\pi(E)\). Assume symmetric prediction accuracy \(p\) concerning \(\pi(F)\).

For any fixed full-box response, two-boxing when the large box is empty is optimal whenever that branch has positive probability. Compare

\[
\pi_+=(1,2),
\qquad
\pi_-=(2,2).
\]

Their values are

\[
V(\pi_+)=pM+(1-p)c,
\]

and

\[
V(\pi_-)=(1-p)(M+c)+pc=(1-p)M+c.
\]

For \(p=0.99\), these are \(\$990{,}010\) and \(\$11{,}000\). P-FDT selects \(\pi_+\): one-box if full, two-box if empty.

Having observed a full box, the agent executes \(\pi_+(F)=1\). It does not replace policy evaluation with a fresh optimization that treats the full box as independent of the response being predicted.

This does not mean believing the observed box might secretly be empty. **Beliefs about actuality and decision hypotheticals have different jobs.** The actual input is full; the hypothetical generated by a different policy can predominantly contain an empty-box input.

Parfit’s hitchhiker has the same structure. A driver rescues someone only if the driver predicts payment after arrival. A policy specifies payment conditional on rescue. Evaluated across rescue and non-rescue branches, a reliably predicted paying policy can be preferable, even though payment has no further causal benefit once the passenger reaches the city.

This interpretation follows the source’s global treatment of observations, but footnote 16 leaves its exact scope unresolved. I have assumed that \(M\) is held fixed across candidate-dependent inputs. That is not yet a rule saying which information belongs in \(M\), which belongs in \(x\), or how far back the evaluation standpoint extends.

## 6. Why Whole Policies Matter in Multi-Agent Problems

Footnote 16 says the policy/action distinction matters in multi-agent dilemmas, without supplying an example. The following construction illustrates a possible reason.

Two agents implement the same policy selector and share its model before receiving private role labels. Exactly one receives \(L\), the other \(R\), with either assignment equally likely. Their common policy maps labels to actions:

\[
\pi:\{L,R\}\longrightarrow\{I,N\},
\]

where \(I\) means invest and \(N\) means decline.

Each investor pays \(c>0\). Each agent receives benefit \(B>c\) if both invest; otherwise there is no benefit. Evaluate matters from one agent’s perspective, before its random label.

The four common policies have values

| \(\pi(L)\) | \(\pi(R)\) | Expected utility |
|---|---|---:|
| \(N\) | \(N\) | \(0\) |
| \(I\) | \(N\) | \(-c/2\) |
| \(N\) | \(I\) | \(-c/2\) |
| \(I\) | \(I\) | \(B-c\) |

Because both agents’ policy-valued outputs depend on the same computation, the intervention changes their common policy together. P-FDT therefore chooses \((I,I)\).

Now consider changing only one policy entry while holding the other fixed at noninvestment. Moving from \((N,N)\) to either \((I,N)\) or \((N,I)\) makes things worse. Thus \((N,N)\) is a local optimum under single-entry changes, although \((I,I)\) is globally better.

This demonstrates how separately optimizing responses at individual inputs can miss a beneficial coordinated policy change. It does **not** prove that the paper’s action-selection formulation must always select noninvestment here; that would require specifying its dependency graph and resolving its self-reference.

The example also identifies an important boundary. Cooperation follows from the stipulated shared computation. Against an unrelated opponent whose policy does not vary with this selector, the same investment may be wasteful. P-FDT does not license assuming that everyone will cooperate whenever cooperation would be convenient.

## 7. Applying P-FDT to Unfamiliar Cases

A practical analysis can proceed in five stages.

**First, define the policy boundary.** Specify inputs, feasible actions, and the candidate policy class. Include relevant responses at inputs that may not actually occur.

**Second, identify the shared computation.** Determine which selector output is being varied and which predictors, copies, or implementations represent it. Do not infer computational identity from superficial similarity.

**Third, construct policy counterfactuals.** For each candidate, recompute dependent predictions, observations, actions, and outcomes. Preserve background uncertainty not affected by that intervention.

**Fourth, compare expected utilities.** Evaluate complete outcomes, including branches where the candidate policy changes whether the current decision situation occurs.

**Fifth, execute the selected policy at the actual input.** Do not silently substitute a different intervention that freezes policy-dependent observations.

This procedure makes several unresolved choices visible.

### The policy boundary

A policy might govern one encounter, a repeated interaction, or an entire life. Broader policies permit more coordination but require more extensive counterfactual assumptions. Footnote 16 does not select a universal boundary.

A reasonable working proposal is to include the contingencies explicitly represented by the predictors and shared computations in the problem. This is a modeling convention, not a theorem.

### Approximate dependence

Real predictors are imperfect. Their behavior should be represented by explicit mechanisms or intervention kernels, not by preserving an unexplained correlation. When several mechanisms fit the evidence, one can average over them:

\[
V(\pi)=
\sum_\theta P(\theta)
\mathbb E_\theta[
U(O)\mid\operatorname{do}_{s}(Q=\pi)
].
\]

The uncertainty concerns the counterfactual model itself.

### Randomization and self-reference

Randomized policies require specifying whether random seeds are shared, independent, or predictable. Identical randomized programs need not produce identical realized actions.

Likewise, representing the selector inside its own model does not automatically guarantee a consistent solution to every predictor interaction. The maximization is well-defined once the kernels are supplied; establishing a globally coherent self-referential model is a separate task.

Finally, the source’s claims about superior performance should not be inflated into universal optimality. It acknowledges that arbitrary environments can reward or punish particular procedures, and that a satisfactory formal definition of “fair” comparison remains open. Policy selection also motivates nonnegative value of information when information can simply be ignored, but that argument requires compatible policy classes and unchanged external consequences of obtaining it.

## Conclusion

P-FDT treats an action as the application of a selected policy, and evaluates policies by varying the output of the selector while preserving relevant computational dependencies. Its central insight is that predictors and copies can make whole patterns of response consequential, including responses at inputs not actually received.

Footnote 16 supplies that architecture, not a finished counterfactual calculus. Applied carefully, P-FDT offers a disciplined method: specify the policy, model what depends on it, compare complete outcomes, and then act. Its hardest remaining questions concern exactly how those dependencies—and the appropriate policy boundary—should be determined.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/e08eab36-0c44-4dc2-b5ca-d871a002895c/call_0/request.json)

[Authoritative raw response](../../../../../../runs/e08eab36-0c44-4dc2-b5ca-d871a002895c/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/e08eab36-0c44-4dc2-b5ca-d871a002895c/call_1/request.json)

[Authoritative raw response](../../../../../../runs/e08eab36-0c44-4dc2-b5ca-d871a002895c/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
