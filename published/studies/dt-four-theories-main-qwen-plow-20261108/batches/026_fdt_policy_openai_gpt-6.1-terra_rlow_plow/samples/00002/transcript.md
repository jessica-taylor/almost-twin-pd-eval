# 026_fdt_policy_openai_gpt-6.1-terra_rlow_plow / 00002

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/528ccc89-9090-4751-b1aa-f216f0f244a2/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/528ccc89-9090-4751-b1aa-f216f0f244a2/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: Choosing a Policy as the Output of a Decision Function

A decision can matter in ways that are not captured by its physical consequences. If another agent has accurately predicted what you will do, its earlier prediction may be tied to your decision even though your present action cannot causally alter the past. Likewise, a copy of your decision procedure may reach the same conclusion in another room without receiving a signal from you.

**Policy functional decision theory (P-FDT)** proposes taking such connections into account when choosing how to act. Its central question is not merely “What happens if this physical action changes?” but “What happens if the decision function implemented here outputs a different policy?”

The primary source for P-FDT is footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory*. The footnote says that the authors’ preferred formulation intervenes on the decision-function node to choose “not an action but a policy which maps inputs to actions,” and then applies the agent’s inputs to that policy. Most of the paper instead develops an action-output formulation for simplicity. The footnote does not specify a complete algorithm for selecting policies, constructing counterfactuals, or handling disagreement between agents. The mathematical procedure below is therefore an **operational interpretation**, informed by the paper’s broader discussion, rather than a definition fully supplied by the footnote.

## 1. The object of choice

Let \(X\) be a set of possible inputs or observation histories and let \(A(x)\) be the actions available after input \(x\). A deterministic policy is a function

\[
\pi:X\longrightarrow \bigcup_{x\in X}A(x),
\qquad \pi(x)\in A(x).
\]

A policy specifies not only what to do now, but what to do under other inputs the same decision procedure might receive. For example, a policy for a transparent-box problem could say:

\[
\pi(\text{full})=\text{take opaque box only},\qquad
\pi(\text{empty})=\text{take both}.
\]

Let \(D\) denote the P-FDT policy-selection computation, and let \(z\) collect whatever problem description, model, and other inputs define that computation. Its output is a policy,

\[
\Pi=D(z).
\]

On receiving an input \(x\), the agent acts according to

\[
A=\Pi(x).
\]

The distinction between \(z\) and \(x\) is useful but not completely settled by the source. In an implementation, the problem description and observations might be packaged differently. What matters is that the policy-selection node and the later application of its output to inputs are represented separately.

The proposed P-FDT rule is

\[
\pi^*\in\operatorname*{arg\,max}_{\pi\in\mathcal P}
\mathbb E_{Q_\pi}[U(O)],
\qquad
a^*=\pi^*(x_{\mathrm{actual}}),
\tag{1}
\]

where:

- \(\mathcal P\) is the candidate policy class;
- \(O\) is the outcome and \(U\) its utility to the agent;
- \(Q_\pi\) is the hypothetical distribution obtained by setting the output of the relevant policy-selection computation to \(\pi\), then propagating the consequences through the model.

Equation (1) is a schema, not a complete theory until \(Q_\pi\), \(\mathcal P\), the relevant computation, and the treatment of evidence have been specified. A tie-breaking rule is also needed if several policies maximize expected utility.

The intervention is on the **output of this computation**, not simply a replacement of the agent’s physical action. If the same computation is implemented elsewhere, or a predictor models its output, the model may make those other systems respond to the same intervention. Nor is the procedure merely “try being a different kind of agent”: the paper stresses that replacing one algorithm by another does not by itself explain why an existing predictor of the original algorithm would change its prediction.

## 2. What changes in a P-FDT hypothetical?

For comparison, evidential decision theory (EDT) evaluates an action using something like

\[
\mathbb E[U(O)\mid X=x,A=a].
\]

Causal decision theory (CDT) instead evaluates a physical intervention, schematically

\[
\mathbb E[U(O)\mid X=x,\operatorname{do}(A=a)].
\]

P-FDT uses neither ordinary conditioning on the action nor an intervention on just the action token. Its hypothetical changes the policy output and follows the relevant *subjunctive dependencies*: the connections specifying what else would differ if that output were different.

The paper uses this term broadly. Causal effects are included: if a policy causes the agent to press a button, the button’s physical consequences change. So are computational and predictive dependencies: a reliable model of the policy may give a different prediction. Mere correlation is not enough. A lesion that both increases a desire to smoke and causes cancer need not change when the output of a decision computation is hypothetically changed.

A convenient graphical interpretation is to put a node \(\Pi\) into an augmented model and define

\[
Q_\pi(\cdot)
=
P\bigl(\cdot\mid \operatorname{do}_{G}(\Pi=\pi)\bigr),
\tag{2}
\]

where \(G\) contains the relevant causal **and** non-causal dependency links. The notation resembles Pearl’s causal intervention, but the graph is doing additional work: it must encode how predictors and other computations depend on the policy. It is not enough to draw an arrow merely because two variables are statistically correlated.

This is a counterpossible construction. A fixed deterministic computation on fixed inputs has a fixed output. If it in fact outputs \(\pi_1\), the supposition that it outputs \(\pi_2\) is, literally, contrary to a mathematical fact. P-FDT uses such suppositions as decision tools; it need not claim that the agent can physically rewrite mathematical truth or send information into the past. The paper explicitly acknowledges that a general account of these counterpossibles, and of how to discover the right dependency graph, remains open.

The difference from ordinary conditioning is practical. Conditional on taking an unusual action, an agent might infer that a cosmic ray disturbed its brain. But a hypothetical in which its decision function outputs a different policy need not include a cosmic ray. Conversely, a well-founded dependence on a predictor may persist in a P-FDT hypothetical even though the prediction was made earlier.

## 3. An operational interpretation of evidence

The source’s action-output formalization has a striking feature: an observation selects *which decision-function output* to intervene on, rather than always being conditioned on inside every hypothetical. Consequently, a hypothetical considered after seeing a full box can depict a world in which the box was empty.

Footnote 16 does not explain exactly how to translate that treatment into policy selection. A reasonable operational proposal is to distinguish:

1. **Background information** \(E_0\), which defines the problem and is treated as fixed across policy hypotheticals.
2. **Policy inputs** \(X\), whose distribution may itself depend on the policy and on predictors of it.
3. **The actual input** \(x_{\mathrm{actual}}\), used to execute the chosen policy but not automatically imposed on every hypothetical.

Under this proposal,

\[
Q_\pi(\cdot)
=
P_G\bigl(\cdot\mid E_0,\operatorname{do}(\Pi=\pi)\bigr).
\tag{3}
\]

The model generates an input \(X\) in each hypothetical, and the policy is applied to that generated input. Thus \(X\) can differ between policy hypotheticals. The actual input still matters: it determines the action finally taken, and it may supply genuinely relevant information for building the model. But one should not automatically condition every hypothetical on an observation that the hypothetical policy itself may have made unlikely.

This is a substantive assumption, not a theorem from footnote 16. In unfamiliar cases, the choice of \(E_0\), the policy’s domain, and the point at which evidence is incorporated can change the answer. If an observation is evidence of an independent disease or an unexpected change in the predictor’s reliability, ignoring it wholesale would be a mistake. Conversely, conditioning on a letter whose arrival depends on the predicted policy can erase the very dependency P-FDT was introduced to represent.

## 4. P-FDT in Newcomb’s problem

A predictor has placed \$1 million in an opaque box if it predicted that the agent would take that box alone. A transparent box contains \$1,000. Suppose the predictor is accurate with probability \(0.99\), and model this accuracy as holding under each of the two relevant policy interventions.

Let \(\pi_1\) prescribe one-boxing and \(\pi_2\) prescribe two-boxing. Their P-FDT values are

\[
V(\pi_1)=0.99(1{,}000{,}000)=990{,}000,
\]

\[
V(\pi_2)=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\]

P-FDT selects \(\pi_1\). The predictor’s earlier behavior changes across the hypotheticals because the model says it depends on the policy output. This is not a claim that one-boxing now causes money to appear in the past.

The numerical conclusion relies on more than a reported aggregate accuracy rate. A predictor could be 99% accurate in a population while being systematically wrong about a particular policy or agent. To use the calculation, one needs an appropriate model of its accuracy *under the alternative policy outputs being compared*.

In the imaginary smoking-lesion case, by contrast, suppose smoking gives the agent 1,000 utility and has no causal effect on cancer; the lesion and cancer do not depend on the policy output. P-FDT keeps the cancer distribution fixed across the relevant policy interventions and selects smoking. EDT can instead refrain if smoking is sufficiently bad news about the lesion, although the source notes that more sophisticated EDT treatments and a consistent specification of the agent’s self-knowledge complicate that example.

## 5. P-FDT policies for transparent boxes and threats

Policies are especially useful when the action is conditional on an observation. Suppose the predictor fills the opaque box if it predicts that the agent would one-box *on seeing it full*. Consider

\[
\pi_1=(\text{one-box if full},\ \text{two-box if empty}),
\]

\[
\pi_2=(\text{two-box if full},\ \text{two-box if empty}).
\]

Under a symmetric 99%-accurate predictor, their expected values are

\[
V(\pi_1)=0.99(1{,}000{,}000)+0.01(1{,}000)
=990{,}010,
\]

\[
V(\pi_2)=0.01(1{,}001{,}000)+0.99(1{,}000)
=11{,}000.
\]

Thus, on this model, P-FDT chooses \(\pi_1\). If the actual box is full, it one-boxes; if empty, it takes both. The comparison includes worlds in which the alternative policy leads to a different observation. It is not the claim that the agent disbelieves the full box when it sees one.

The same structure appears in mechanical blackmail. A blackmailer starts a damaging process only if it predicts that the agent will pay \$1,000 upon receiving a demand; refusal after the process starts costs the agent \$1 million. If paying would reliably trigger the demand, but refusing would trigger it only with probability \(\varepsilon\), then, under a simple model,

\[
V(\text{pay if demanded})=-1{,}000,\qquad
V(\text{refuse if demanded})=-1{,}000{,}000\varepsilon.
\]

Refusal is preferred when \(\varepsilon<0.001\). At \(\varepsilon=0.0009\), its expected loss is \$900; at \(\varepsilon=0.0011\), it is \$1,100 and payment is preferred. These are policy-level expected losses, not the loss conditional on the demand actually arriving. If a demand does arrive despite a refusal policy, refusal incurs the large loss in that exceptional case.

The threshold depends on the assumed response probabilities and costs. Real threats may also involve independently motivated attackers, multiple future interactions, moral costs, or uncertainty about whether refusal deters anything. P-FDT is not a blanket instruction never to pay; it requires modeling how the threatened action and the threat’s arrival depend on the policy.

## 6. Why whole policies matter in multi-agent cases

The paper says that choosing policies rather than actions can make a difference in multi-agent dilemmas, although it does not supply a general example or proof. Here is an illustrative model.

Two copies implement the same policy selector and play a prisoner’s dilemma in separate rooms. Each receives a different label, \(L\) or \(R\), as input. A single policy specifies an action for each label. Suppose each player receives \$1 million if both cooperate, \$1,000 if both defect, \$1,001,000 if it defects alone, and zero if it cooperates alone.

If the intervention sets the **shared policy output**, then the policy

\[
\pi(L)=C,\qquad \pi(R)=C
\]

produces mutual cooperation, while \(\pi(L)=D,\pi(R)=D\) produces mutual defection. An asymmetric policy \((C,D)\) benefits the \(R\)-player and harms the \(L\)-player.

This example exposes questions that footnote 16 does not resolve. Whose utility is optimized if the two copies evaluate the same policy but occupy different roles? Are they uncertain about their role at policy-selection time, or do they have role-specific objectives? If each knows its label and maximizes only its own payoff, their policy-selection computations may have different inputs and need not output the same policy. If a common ex ante objective weights the two roles equally, mutual cooperation beats either asymmetric policy; but that common objective is an additional assumption, not a consequence of P-FDT alone.

Nor does similarity automatically create a shared policy node. Two agents using the same broad theory with different evidence, utilities, code, or tie-breaking rules may respond differently. A model should connect their outputs only to the extent that there is a defensible computational, predictive, or other subjunctive relationship.

## 7. How to apply P-FDT to an unfamiliar problem

A practical analysis can proceed as follows.

**First, define the policy domain and objective.** List the observations the policy can receive, the available actions, and the outcomes valued by the agent. Include policies for relevant contingencies, including those that might not occur under the ultimately selected policy.

**Second, identify the decision computation.** Specify what node represents the policy selector’s output and which systems implement or predict it. Distinguish one shared output applied to different inputs from separate computations with different inputs.

**Third, build alternative hypothetical models.** For each candidate \(\pi\), set the policy-output node to \(\pi\). Propagate ordinary physical effects, predictor responses, copy behavior, and changes in observations where the model supports them. Keep unrelated background variables fixed in distribution. Do not preserve a correlation solely because it exists in observational data.

**Fourth, calculate and compare expected utilities.** Use equation (1), including costs and outcomes on branches where the actual observation would not occur. Apply the maximizing policy to the actual input.

**Finally, test the modeling assumptions.** Ask how the answer changes if a predictor is less reliable, if its errors depend on the policy, if agents are less computationally linked, or if an observation is treated as independent evidence. If the answer is sensitive to an unresolved choice, report that sensitivity rather than presenting a unique prescription as established.

Randomized policies require further specification. A predictor might know the distribution over actions but not the realization of a genuinely private random draw; it might instead predict a pseudorandom seed. Those models yield different dependencies and potentially different optimal policies. Similarly, an unrestricted space of policies may be too large to search, and a restricted class may exclude the best policy. These are problems of implementation as well as philosophical interpretation.

## 8. What the proposal does—and does not—establish

P-FDT’s appeal is that it can evaluate a policy from a perspective that includes its predictable consequences without confusing prediction with backward causation. It also offers a way to break correlations that are merely evidential. The resulting choices can resemble what an agent would have wanted to precommit to before a predictor acted.

That resemblance is not an unconditional proof that every P-FDT agent achieves the best outcome. The source itself acknowledges that no decision theory wins in every contrived environment and leaves its proposed distinction between “fair” and “unfair” problems informal. Nor does policy selection alone guarantee non-negative value of information, reflective stability, or consistency over time. Such results depend on the policy space, evidence treatment, dependency model, and the relationship between later and earlier computations.

The largest unresolved task is constructing justified counterfactual models. A graph that simply stipulates that a predictor tracks the agent may make the desired answer easy to calculate, but it does not explain when that stipulation is warranted. Self-reference adds a further challenge: representing a computation’s own output is possible in principle, but that fact alone does not guarantee a tractable, uniquely defined policy selector.

## Conclusion

P-FDT evaluates candidate policies by hypothetically changing the output of the policy-selection computation and tracing the relevant causal, predictive, and computational dependencies. It then applies the selected policy to the actual input. This makes it suited to problems where what an agent would do across contingencies is itself predicted or replicated.

Footnote 16 gives the central policy-selection idea, not a finished general calculus. Applying P-FDT responsibly therefore means making the policy space, evidence boundary, utilities, and dependency assumptions explicit—and recognizing when a verdict rests on choices the source leaves open.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, version 2, especially footnotes 7 and 16 and sections 3–6. https://arxiv.org/abs/1710.05060v2
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/aa808236-c412-47d9-b3bb-5ac5973a16cd/call_0/request.json)

[Authoritative raw response](../../../../../../runs/aa808236-c412-47d9-b3bb-5ac5973a16cd/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Evaluating policy decisions**

I’m thinking about whether to use a shared policy versus handling different types of inputs. I find that symmetric observations can be irrelevant, but I do want to keep it defensible and abstract when sampling is imperfect. The difference lies in the actual text output, but I wonder if a uniform pass is the better route. Rational symmetry could support cooperation, even though errors are possible without calibration. I'm weighing my options carefully here.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/aa808236-c412-47d9-b3bb-5ac5973a16cd/call_1/request.json)

[Authoritative raw response](../../../../../../runs/aa808236-c412-47d9-b3bb-5ac5973a16cd/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Deciding on shared policies**

I'm trying to figure out whether to use shared policies or different inputs. There's something about symmetry and identical models that seems to generalize decisions. A shared policy can map different names, but each needs to choose its own role in computation. I'm wondering how asymmetry can be exploited in this context. It feels like we should opt for a common decision algorithm and independent sampling, taking care to rely on good judgment since reliability isn't guaranteed.
```
