# 027_fdt_policy_openai_gpt-6.1-sol_rhigh_phigh / 00011

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/b7226b40-62da-4a4a-900f-10ae494a2975/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/b7226b40-62da-4a4a-900f-10ae494a2975/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: Choosing the Policy Behind the Action

A decision can matter in more than one place. It may determine what one’s body does, but also what a simulator predicts, how an identical program behaves elsewhere, or whether another agent offers a bargain. **Policy functional decision theory (P-FDT)** evaluates choices with these wider dependencies in view. Its central question is not merely which physical act has the best consequences, but which output of one’s policy-selection procedure corresponds to the best outcome.

The primary source for this account is footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality*. It describes the authors’ preferred formulation as choosing “not an action but a policy which maps inputs to actions,” and then applying that policy to the agent’s inputs. Footnote 7 likewise emphasizes optimization over policies rather than individual actions.

These passages specify an important architecture, not a complete mathematical theory. They leave unresolved the scope of a policy, the evaluation of alternative policies, and the construction of logical counterfactuals. This essay develops an operational interpretation of P-FDT, using the surrounding paper to motivate the missing pieces while distinguishing those interpretive choices from explicit source claims.

## 1. The mathematical object being chosen

Let \(\mathcal X\) be a finite set of possible information states and \(\mathcal A\) a finite set of actions. An information state might contain an observation, a private signal, or an entire observation history. A deterministic **policy** is a function
\[
\pi:\mathcal X\longrightarrow\mathcal A.
\]
Let \(\Pi\subseteq\mathcal A^{\mathcal X}\) be the admissible policies.

For example, a policy for responding to offers specifies what to do for every possible offer—not just the offer currently visible. In a sequential problem, histories must contain enough information to distinguish the relevant decision points.

Write \(M\) for a world-model containing probabilities, utilities, and dependency information. A policy selector \(S\) returns a policy:
\[
S(M)=\pi^*,
\qquad
A=\pi^*(x)
\]
when the actual input is \(x\).

The distinctive P-FDT step is to evaluate alternative **outputs of this selector**. Let \(T\) be a variable in the model representing \(S(M)\). Define
\[
K_M(o\mid\pi)
=
P_M\!\left(O=o\mid\operatorname{do}_{s}(T=\pi)\right),
\]
where \(\operatorname{do}_{s}\) denotes a *subjunctive* intervention, to be explained below. Given an outcome utility function \(u\), set
\[
V_M(\pi)=\sum_o K_M(o\mid\pi)u(o).
\]
A natural P-FDT rule is
\[
\boxed{
\pi^*\in\arg\max_{\pi\in\Pi}V_M(\pi),
\qquad
A=\pi^*(x).
}
\tag{1}
\]
Assume bounded utilities and a fixed tie-breaking convention.

Equation (1) is my reconstruction, not an equation supplied in footnote 16. Its two-stage structure follows that footnote: select a policy, then apply the input. Its subjunctive evaluation follows the surrounding paper’s treatment of functional dependence.

For this reconstruction, \(M\) is a **fixed evaluation context** spanning the alternative inputs under consideration. In particular, equation (1) does not automatically condition the policy’s score on the actual input \(x\). That choice is motivated by the paper’s examples, where changing the decision procedure’s output can change which observation the agent receives. The footnote alone does not settle how such contexts should be chosen.

One can also express an action recommendation through policies:
\[
W_M(a;x)
=
\max_{\pi:\,\pi(x)=a}V_M(\pi).
\]
This scores taking \(a\) at \(x\) through the best complete policy prescribing it. Implementation must nevertheless use one coherently selected policy, rather than independently choosing incompatible prescriptions at different inputs.

## 2. What changes in a P-FDT counterfactual?

Compare two familiar approaches. **Evidential decision theory (EDT)** evaluates an action through a conditional expectation such as
\[
\mathbb E[u(O)\mid X=x,A=a].
\]
**Causal decision theory (CDT)** instead uses a causal intervention:
\[
\mathbb E[u(O)\mid X=x,\operatorname{do}(A=a)].
\]

P-FDT intervenes at a different level: the output of the mathematical policy selector. Its counterfactuals preserve relevant **subjunctive dependencies**.

The source introduces this notion through computations and predictors. Two faithful implementations of the same computation have matching outputs even without communication. Likewise, an accurate simulation of an agent’s policy is constrained to track that policy. Changing the represented policy while holding its faithful simulation fixed would discard something important about the situation.

An operational model can make this explicit. Let \(\omega\) encode background uncertainty, with distribution \(\mu\), and suppose the modeled outcome is
\[
O=F(T,\omega).
\]
Here \(F\) includes the agent’s behavior, predictions about that behavior, environmental responses, and ordinary physical consequences. Then
\[
V_M(\pi)
=
\int u(F(\pi,\omega))\,d\mu(\omega).
\tag{2}
\]
The intervention replaces the selector-output equation \(T=S(M)\) with \(T=\pi\), while preserving the modeled dependencies downstream from \(T\).

Three distinctions matter:

* **Physical effects change.** Different prescribed actions can produce different physical outcomes.
* **Faithful representations change appropriately.** A predictor or copy tracking the selected policy changes according to its modeled relationship to that policy.
* **Mere correlations need not persist.** A background condition does not change simply because the chosen action is evidence about it.

This is neither unrestricted wishful thinking nor retrocausation. The agent does not believe that acting now sends a signal into yesterday. It compares hypotheticals in which yesterday’s prediction and today’s behavior reflect a different output of the same mathematical procedure.

There is a genuine foundational difficulty. A fixed deterministic selector has only one output on a fixed input. Alternative-output hypotheses may therefore be *counterpossible*, not merely physically unrealized. The source explicitly acknowledges that it lacks a satisfactory general account of these counterfactuals. Equations (1)–(2) are usable once the relevant dependency model is supplied; they do not solve the problem of discovering that model.

## 3. P-FDT in Newcomb’s problem and a common-cause problem

In Newcomb’s problem, an opaque box contains \(m=\$1{,}000{,}000\) if a predictor forecasts one-boxing, and nothing otherwise. A transparent box contains \(s=\$1{,}000\). The agent chooses the opaque box alone or both boxes.

For simplicity, assume a symmetric prediction channel: under either candidate policy, the forecast matches the resulting choice with probability \(q\). This is stronger than knowing only the predictor’s aggregate historical accuracy.

With no informative observation, policies reduce to constant choices. P-FDT assigns
\[
V(\text{one-box})=qm,
\]
\[
V(\text{two-box})=(1-q)m+s.
\]
Thus it one-boxes exactly when
\[
(2q-1)m>s.
\]
At \(q=0.99\), the respective values are \(\$990{,}000\) and \(\$11{,}000\).

The important step is not treating one-boxing as *good news*. It is preserving the predictor’s modeled dependence on the selected policy. CDT’s physical-action intervention instead leaves the box contents unchanged.

Now consider the source’s imaginary smoking-lesion setup. A lesion produces both a tendency to smoke and cancer, but smoking itself does not cause cancer. Suppose smoking supplies a utility bonus \(b>0\). If neither the lesion nor cancer subjunctively depends on the policy selector, then
\[
V(\text{smoke})-V(\text{refrain})=b.
\]
P-FDT therefore prescribes smoking.

The contrast is structural: the predictor represents the decision process; the lesion does not. Statistical similarity between the two problems does not imply identical counterfactual evaluations.

This is only a toy illustration. The source itself criticizes the smoking-lesion problem’s assumptions about preferences and self-knowledge. Nothing here concerns actual smoking, which has serious causal health risks.

## 4. Observations guide a policy without necessarily fixing its score

The policy perspective becomes especially revealing when the observation is itself influenced by predictions.

In **transparent Newcomb**, both boxes are visible. The predictor fills the large box if it forecasts that the agent would one-box *upon seeing it full*. A policy specifies two responses:
\[
\pi=(\pi(F),\pi(E)),
\]
where \(F\) and \(E\) mean seeing the large box full and empty.

Consider
\[
\pi_1=(\text{one-box},\text{two-box}),
\qquad
\pi_2=(\text{two-box},\text{two-box}).
\]
Under a symmetric predictor with accuracy \(q\),
\[
V(\pi_1)=qm+(1-q)s,
\]
whereas
\[
V(\pi_2)=(1-q)m+s.
\]
At \(q=0.99\), these are \(\$990{,}010\) and \(\$11{,}000\). For either fixed full-box response, two-boxing when empty weakly improves the score, so these comparisons identify the optimum among all four deterministic policies.

P-FDT therefore one-boxes when the large box is full and two-boxes when it is empty.

But suppose the agent is already looking at a full box. Has the uncertainty not disappeared?

It has disappeared from the agent’s factual belief about the current contents. It has not necessarily disappeared from the policy counterfactual. Changing the selected policy changes what the predictor forecasts, which changes how often the agent reaches the full-box input. Conditioning every policy’s evaluation on \(F\) would remove that effect.

The resulting distinction is crucial:

> Knowing which input occurred does not imply that every policy counterfactual must preserve that input.

This is the central operational interpretation I take from the source’s global-perspective discussion.

**Parfit’s hitchhiker** has the same structure. A driver rescues the agent only if she predicts payment after arrival. With perfect prediction, rescue value \(v\), and payment \(c<v\),
\[
V(\text{pay if rescued})=v-c,
\qquad
V(\text{refuse if rescued})=0.
\]
P-FDT selects payment and implements it in the city. It does not require an enforceable advance commitment: the payment prescription is itself what makes rescue predictable.

## 5. Why selecting a whole policy can matter

Footnote 16 says the policy/action distinction matters in some multi-agent dilemmas, but supplies no example. The following construction illustrates a possible difference; it is an additional model, not a reported result from the paper.

Two agents receive different roles, \(0\) and \(1\), and each chooses whether to invest. They run copies of the same policy selector in a symmetric evaluation context. Its output is a shared policy
\[
\pi:\{0,1\}\to\{0,1\},
\]
where \(1\) means invest.

If both invest, each receives a benefit of \(100\). Each investor pays a cost of \(1\), whether or not the project succeeds:
\[
u_i=100a_0a_1-a_i.
\]
Before learning its role, an agent assigns each role probability \(1/2\). Crucially, assume the subjunctive model links both copies to the same selected policy. Its score is then
\[
V(\pi)
=
100\pi(0)\pi(1)
-\frac{\pi(0)+\pi(1)}2.
\]
The four policy values are
\[
V(0,0)=0,\qquad
V(1,0)=V(0,1)=-\tfrac12,\qquad
V(1,1)=99.
\]
P-FDT selects \((1,1)\), so both invest.

The contrast with isolated output selection is informative. Starting from prescriptions \((0,0)\), changing only one role’s prescription is costly: the project still fails. Thus \((0,0)\) is a coordinatewise local optimum, although \((1,1)\) is globally better. Whole-policy selection can evaluate the coordinated change directly.

This does not show that the paper’s action-output formulation must always fail here. Its answer depends on which dependencies it represents between different-input computations. The example instead identifies what policy selection makes explicit: **different policy entries can change together even when agents receive different inputs**.

Nor does P-FDT recommend cooperation with arbitrary strangers. If the other agent’s policy is independent of this selector, the shared-policy equation is wrong. Common vocabulary, similar values, or the label “rational” does not by itself establish computational dependence.

## 6. Applying P-FDT when the source leaves choices open

A practical P-FDT analysis should make the following modeling decisions explicit.

### Choose the policy domain and evaluation context

What inputs belong to one policy? Which goals, background knowledge, and environmental assumptions remain fixed during its evaluation?

A useful convention is to select a context encompassing the prediction and interaction being analyzed, then represent subsequent observations as policy inputs. This captures Newcomb and hitchhiker reasoning. It does not establish that every decision must be evaluated from an immutable lifetime prior.

Footnote 16 does not resolve this boundary. Different boundaries can produce different recommendations, especially when new evidence concerns the reliability of the dependency model itself.

### Construct a counterfactual mechanism, not just a correlation table

Specify what predicts, implements, or responds to the policy. Include ordinary causal consequences and explicit uncertainty about prediction errors.

For example, suppose a blackmailer targets every policy that would pay \(c\), but mistakenly targets a refusing policy with probability \(r\). Refusal then incurs damage \(L\). Under those assumptions,
\[
V(\text{pay})=-c,
\qquad
V(\text{refuse})=-rL.
\]
P-FDT refuses exactly when
\[
rL<c.
\]
Its resistance to extortion is therefore not unconditional. It depends on whether predictable refusal deters threats sufficiently often.

### Specify feasibility and implementation

Policy optimization requires an admissible policy class. With finite inputs and actions, exhaustive enumeration is possible in principle, though usually expensive. In realistic problems, policy search must be approximate.

Randomization adds another unresolved choice. A randomized policy may map inputs to action distributions, but copies need not share their random outcomes. Shared pseudorandom seeds, independent private randomness, and predictor-accessible randomness produce different dependencies. They must not be conflated.

Likewise, if a proposed dependency model contains feedback, each candidate policy needs a well-defined resulting outcome distribution. A cyclic model without a solution rule does not yet define the values in equation (1).

### Keep epistemic updating separate from policy evaluation

P-FDT need not deny evidence. Seeing a letter can establish that a blackmailer made an error; seeing a full box establishes its contents. The question is whether those observed events must remain fixed while comparing policies whose outputs affect their occurrence.

The difficult cases concern **model learning**: what if evidence suggests that the predictor was never reliable? The source gives no complete rule for combining such learning with policy-level evaluation. A responsible application should acknowledge that underdetermination rather than automatically dismissing inconvenient evidence as counterfactually irrelevant.

### State conclusions at the strength supported

Within a fixed context and kernel, P-FDT is an expected-utility maximizer. Further claims require further assumptions.

For example, free information has nonnegative policy value if every old policy remains available as a new policy that ignores the signal, with the same outcome distribution. Then
\[
\max_{\pi\in\Pi_{\mathrm{new}}}V(\pi)
\ge
\max_{\pi\in\Pi_{\mathrm{old}}}V(\pi).
\]
But this argument does not cover information whose acquisition changes costs, observability, or opponents’ responses.

Similarly, the source’s favorable examples do not prove universal superiority. The paper acknowledges both the absence of a precise fairness criterion and the incompleteness of its counterpossible semantics.

## Reference

Yudkowsky, Eliezer, and Nate Soares. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2, especially footnotes 7 and 16 and §§3, 5, 6, and 9. https://arxiv.org/abs/1710.05060v2.

## Conclusion

P-FDT treats a complete input-to-action policy as the output being evaluated, then implements that policy at the actual input. Its distinctive counterfactuals preserve relevant computational and predictive dependencies without preserving every statistical correlation. This yields a coherent method for many prediction and coordination problems. Its main unfinished task is equally clear: specifying, rather than merely assuming, which policy-level dependencies and evaluation contexts a rational agent should use.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/2e20b060-cf10-4e0b-adf9-6f1a3423f665/call_0/request.json)

[Authoritative raw response](../../../../../../runs/2e20b060-cf10-4e0b-adf9-6f1a3423f665/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/2e20b060-cf10-4e0b-adf9-6f1a3423f665/call_1/request.json)

[Authoritative raw response](../../../../../../runs/2e20b060-cf10-4e0b-adf9-6f1a3423f665/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
