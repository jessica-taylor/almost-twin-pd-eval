# 027_fdt_policy_openai_gpt-6.1-sol_rhigh_phigh / 00017

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/f11271a3-eaad-4802-a230-9928381c40d8/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/f11271a3-eaad-4802-a230-9928381c40d8/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: Choosing Policies Through Functional Counterfactuals

A decision can matter without physically causing everything that depends on it. A predictor may already have anticipated it; another agent may be running the same computation; a simulation may reproduce it elsewhere. **Policy functional decision theory (P-FDT)** asks how to choose when these dependencies extend beyond the causal consequences of one’s immediate action.

The primary source here is footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory*. It describes a formulation that intervenes on the decision procedure’s output “to choose not an action but a policy which maps inputs to actions,” after which the agent applies that policy to its inputs. Footnote 7 makes a similar observation. The authors say that policy selection matters in some multi-agent dilemmas, although they set it aside in the main exposition.

These passages specify an architecture, not a complete mathematical theory. In particular, they do not fully determine the domain of policies, the treatment of evidence, or the counterfactual operator. This essay develops one operational reconstruction, identifying where additional assumptions enter.

## 1. The object of choice in P-FDT

Let \(\mathcal X\) be a finite set of possible inputs and \(\mathcal A\) a finite set of actions. An input might be an observation, an observation history, or a richer description of the agent’s information. A deterministic **policy** is a function
\[
\pi:\mathcal X\longrightarrow\mathcal A.
\]
Write \(\mathcal P\subseteq\mathcal A^{\mathcal X}\) for the feasible policies.

A policy specifies more than what to do now. It also specifies what to do on inputs that are not currently received, including inputs that might arise under alternative predictions of the agent.

Let \(M\) be an evaluation model containing probabilities, utilities, and dependency information. Introduce a variable \(\Pi\) representing the policy output by the agent’s policy-selection computation \(S(M)\). P-FDT compares hypotheses of the form
\[
\text{“This very policy selector outputs }\pi\text{.”}
\]
This is not merely the hypothesis that the agent physically executes a particular action. Nor is it the hypothesis that an unrelated decision algorithm replaces the existing selector while predictions of that selector remain unchanged.

For each candidate policy, suppose we can construct a counterfactual outcome distribution
\[
Q_M^\pi(o)
=
P_M\!\left(
O=o\mid\operatorname{sdo}(\Pi=\pi)
\right).
\]
Here \(\operatorname{sdo}\) denotes a **subjunctive intervention**, notation introduced for this reconstruction. It changes the selector’s represented output and propagates that change through the relevant functional and causal dependencies. It is not ordinary Bayesian conditioning or necessarily a physical intervention.

Given utility \(u(o)\), define
\[
V_M(\pi)=\sum_o Q_M^\pi(o)u(o).
\]
The reconstructed rule is
\[
\pi_M^*
=
\underset{\pi\in\mathcal P}{\operatorname{argmax}}\,V_M(\pi),
\qquad
\operatorname{P\!-\!FDT}(M,x)=\pi_M^*(x),
\]
with a specified tie-breaking convention.

The crucial order is:

1. Evaluate complete policies.
2. Select one policy.
3. Apply the actual input to it.

Choosing policies alone is insufficient to characterize P-FDT. A causal policy optimizer might hold an earlier prediction fixed while changing its policy. P-FDT instead preserves the appropriate dependence between the selected policy and predictions of that selection.

For comparison, evidential decision theory (EDT) evaluates actions using quantities such as
\[
\mathbb E[u(O)\mid X=x,A=a],
\]
while causal decision theory (CDT) uses quantities such as
\[
\mathbb E[u(O)\mid X=x,\operatorname{do}(A=a)].
\]
P-FDT changes both the object being varied—a policy—and the dependencies preserved while varying it.

## 2. Which dependencies should P-FDT preserve?

The paper calls the relevant relation **subjunctive dependence**. Its central examples are implementations of the same computation and sufficiently accurate predictors of that computation.

Suppose two computers execute the same deterministic policy selector on the same evaluation model. Their physical actions may be causally independent, yet their policy outputs coincide. In a P-FDT hypothetical where the selector outputs \(\pi\), both implementations should therefore output \(\pi\).

Likewise, if a predictor models that selector, changing its counterfactual output should normally change the prediction. Imperfect prediction weakens this correspondence rather than eliminating it.

By contrast, a statistical association need not survive. If a medical condition causes both a behavioral inclination and an illness, varying the policy selector’s conclusion need not change the condition.

An operational representation can use background uncertainty \(W\), with distribution \(\mu\). For each candidate policy, the model generates
\[
X^\pi=H(\pi,W),\qquad
A^\pi=\pi(X^\pi),\qquad
O^\pi=F(\pi,W).
\]
The functions incorporate predictions, other agents, physical consequences, and any relevant implementations of the selector. Then
\[
V_M(\pi)=\mathbb E_{W\sim\mu}[u(O^\pi)].
\]

Holding \(W\) fixed across comparisons expresses the idea that unrelated background conditions do not change. But observations can change: \(X^\pi\) may depend on the policy through a predictor’s response.

This representation is an additional modeling proposal, not a counterfactual calculus supplied by footnote 16. It is useful only when \(H\) and \(F\) correctly encode the dependencies.

There is also a foundational difficulty. A fixed deterministic selector has one mathematically determined output. Asking it to output something else can therefore be a **counterpossible** supposition. The paper acknowledges that a satisfactory general account is missing. The notation above brackets that problem; it does not solve it.

The practical requirement is narrower than arbitrary reasoning from contradictions: construct useful, nontrivial alternatives that preserve specified computational relationships without treating every proposition as following from an impossible antecedent.

## 3. P-FDT in Newcomb’s problem and the smoking lesion

In Newcomb’s problem, an opaque box contains \(m\) dollars if a predictor anticipated one-boxing and nothing otherwise. A transparent box contains \(b\) dollars. The predictor acts before the agent chooses.

For simplicity, assume the predictor tracks each candidate policy’s action correctly with probability \(p\), symmetrically across actions. Historical accuracy alone would not establish this assumption; it is part of the model.

With only one relevant input, the two policies reduce to one-boxing and two-boxing:
\[
V(\pi_{\mathrm{one}})=pm,
\qquad
V(\pi_{\mathrm{two}})=(1-p)m+b.
\]
Thus P-FDT one-boxes when
\[
(2p-1)m>b.
\]
For \(p=0.99\), \(m=\$1{,}000{,}000\), and \(b=\$1{,}000\), the values are respectively
\[
\$990{,}000
\quad\text{and}\quad
\$11{,}000.
\]

No backwards physical influence is assumed. The comparison concerns different conclusions of a computation that the earlier predictor was modeling.

The familiar causal dominance argument holds the box contents fixed while changing the physical action. P-FDT evaluates a different variation, under which the prediction also changes. Consequently, causal dominance does not settle the dispute without first settling which counterfactual comparison is appropriate.

Now consider the source’s imaginary smoking-lesion problem. A lesion causes both an inclination to smoke and cancer; smoking itself does not cause cancer. Suppose the agent values smoking by \(s>0\).

Under the stipulated dependency structure,
\[
P^\pi(\mathrm{cancer})=q
\]
for both smoking and abstaining policies. Hence
\[
V(\pi_{\mathrm{smoke}})
-
V(\pi_{\mathrm{abstain}})
=s.
\]
P-FDT smokes.

The difference is structural: the predictor responds to a representation of the decision computation; the lesion does not. P-FDT neither preserves every observed correlation nor severs every noncausal one.

The paper itself later criticizes the smoking-lesion formulation, particularly its assumptions about preferences and self-knowledge. Its safest role here is illustrative, not a decisive empirical argument against every version of EDT.

## 4. P-FDT, evidence, and contingent policies

Footnote 16 does not explicitly specify whether policy values are conditioned on the actual input. This omission matters greatly.

My reconstruction uses a fixed evaluation distribution over the modeled interaction, rather than automatically conditioning that distribution on every policy-dependent observation. This fits the main text’s treatment of transparent Newcomb and blackmail, but remains an interpretive choice.

Consider a perfect predictor and transparent boxes. Let the inputs be \(F\), seeing a full opaque box, and \(E\), seeing an empty one. A policy specifies
\[
\pi(F),\pi(E)\in\{\mathrm{one},\mathrm{two}\}.
\]
The predictor fills the opaque box exactly when it predicts
\[
\pi(F)=\mathrm{one}.
\]

The policy
\[
\pi(F)=\mathrm{one},
\qquad
\pi(E)=\mathrm{two}
\]
produces a full box and payoff \(m\). Any policy with \(\pi(F)=\mathrm{two}\) produces an empty box and earns at most \(b\). P-FDT therefore selects the former policy and one-boxes when seeing the full box.

The alternative is not “take the extra money while preserving everything currently observed.” It is “have this selector output a different complete policy,” which changes what the predictor arranges.

Parfit’s hitchhiker has the same structure. A driver rescues an agent only if the driver predicts payment after arrival. With perfect prediction, the paying policy yields rescue value \(L\) minus payment \(c\); the refusing policy yields no rescue. P-FDT pays when \(L>c\), including after reaching safety.

This does not mean observations are useless. The selected policy is explicitly a function of observations. Indeed, when \(X\) is independent of the policy intervention and consequences separate by input,
\[
V(\pi)
=
\sum_x P(x)\,
\mathbb E[u(O)\mid x,\pi(x)].
\]
If every input-contingent action is feasible, maximization decomposes into ordinary optimal decisions at each input.

The distinctive cases are those where policy changes alter which observations occur, or link behavior across inputs and implementations.

## 5. Why whole-policy selection matters for P-FDT

The following example is my own illustration of the policy-selection architecture.

Two agents run the same policy selector. One receives role \(L\), the other role \(R\), with each assignment equally likely. They cannot communicate. Each chooses whether to contribute.

Both receive benefit \(3\) if both contribute. Each contributor pays cost \(1\), regardless of whether the other contributes. Utility is
\[
u_i
=
3\,\mathbf 1\{\text{both contribute}\}
-
\mathbf 1\{i\text{ contributes}\}.
\]

Their common selected policy maps roles to actions. Because their selector computations are identical, a subjunctive intervention on the selected policy changes both implementations together.

There are four policies:

| Contributing roles | Expected utility per agent |
|---|---:|
| Neither | \(0\) |
| Only \(L\) | \(-\tfrac12\) |
| Only \(R\) | \(-\tfrac12\) |
| Both | \(2\) |

P-FDT selects contribution in both roles.

This demonstrates why comparing complete policies can matter. Starting from noncontribution everywhere, changing only one policy entry makes things worse. Changing both entries makes things better. Coordinate-by-coordinate policy improvement can therefore get stuck at a policy that whole-policy optimization rejects.

This example is not offered as a theorem about every action-selection formulation. It illustrates a distinction that footnote 16 leaves undeveloped: the unit of counterfactual variation can encompass responses to multiple inputs.

Nor does P-FDT recommend unconditional cooperation. If the other agent is an independent, fixed noncontributor, changing one’s selected policy does not change that agent. Contributing then merely costs \(1\).

A shared theory label is not enough to establish dependence. The relevant questions concern shared computations, inputs, models, and reliable predictive relationships.

## 6. P-FDT and imperfect blackmail

Policy evaluation also explains the source’s resistance to mechanical blackmail.

Suppose a blackmailer launches a damaging mechanism if it predicts payment. Payment costs \(c\); refusing after launch causes loss \(K\). Assume:

- a paying policy is always correctly identified and targeted;
- a refusing policy is mistakenly targeted with probability \(\varepsilon\);
- without a launch, there is no loss.

The policy values, expressed as negative losses, are
\[
V(\pi_{\mathrm{pay}})=-c,
\qquad
V(\pi_{\mathrm{refuse}})=-\varepsilon K.
\]
P-FDT refuses precisely when
\[
\varepsilon K<c.
\]

With \(c=\$1{,}000\), \(K=\$1{,}000{,}000\), and \(\varepsilon=0.0009\), refusal loses \(\$900\) in expectation, versus \(\$1{,}000\) for payment.

On this reconstruction, the agent refuses even on the rare occasion when the mistaken threat actually arrives. Its action implements the policy selected across the predictive interaction; it does not reoptimize after conditioning away that policy’s deterrent effect.

But if targeting is independent of the selected policy, the deterrence argument disappears. P-FDT is not a general command to resist threats regardless of consequences.

## 7. Applying P-FDT without hiding the open questions

For an unfamiliar problem, a workable procedure is:

1. **Specify utility and feasible policies.** Include the relevant observation-contingent responses, not just the current action.
2. **Fix the evaluation information.** Identify which background facts belong in \(M\) and which observations are generated within the interaction.
3. **Identify the policy-selection computation.** Determine which implementations and predictions depend on its output.
4. **Construct each policy hypothetical.** Preserve those dependencies while holding unrelated uncertainty fixed.
5. **Generate observations and actions anew.** Evaluate \(A^\pi=\pi(X^\pi)\), including branches different from the actual one.
6. **Maximize expected utility and execute the selected policy.**

Several unresolved choices remain.

**Policy scope.** Does one policy cover observations in one problem, complete belief states, future histories, or all possible decision inputs? Footnote 16 does not settle this. My finite-domain treatment fixes one modeled interaction. Broader domains require additional arguments about which decisions share a selector output.

**Evaluation information.** A reasonable convention is to model the predictive interaction before its policy-dependent observations are generated, while incorporating settled background knowledge into \(M\). This need not mean physically deciding earlier. Nevertheless, the source does not supply a general rule for choosing that informational standpoint or revising it during learning. Arbitrarily discarding inconvenient evidence would not be justified.

**Dependency identification.** Predictor accuracy is not enough by itself. One needs a model of how predictions respond to alternative selector outputs. Likewise, superficially similar agents may have different inputs or objectives. Uncertain dependencies can be represented by uncertainty over models, but their identification remains a substantive task.

**Computation and randomization.** Finite policy spaces make the optimization well-defined, not tractable. Randomized policies additionally require specifying whether random seeds are private, shared, or predictable. Otherwise one may accidentally preserve dependencies between random outcomes that should be independent.

P-FDT also gives a conditional argument for the nonnegative value of information. If richer inputs allow every old policy to be reproduced by ignoring the extra information, and doing so preserves its counterfactual outcome distribution, then expanding the policy space cannot lower the maximum value. The invariance condition matters: this is not an unrestricted theorem about every information channel or updating convention.

Finally, optimality relative to a supplied model is not universal superiority. The paper acknowledges that environments can reward particular algorithms or punish particular computations. Its proposed distinction between “fair” and “unfair” problems remains informal. Neither universal dominance nor unrestricted reflective stability follows from the policy-selection footnote.

## Reference

Yudkowsky, Eliezer, and Nate Soares. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2, especially footnotes 7 and 16 and §§3, 5–6, 9. https://arxiv.org/abs/1710.05060v2.

## Conclusion

P-FDT evaluates complete input-to-action policies through counterfactual changes to the policy-selection computation. Its distinctive ambition is to preserve genuine computational and predictive dependencies without preserving mere statistical associations.

That architecture yields concrete answers once a policy domain, evaluation distribution, and dependency model are supplied. It explains coordinated behavior, credible payment, and resistance to predictive extortion. The central unfinished work is equally concrete: determining which policy counterfactuals are warranted, from which informational standpoint, and with what computationally usable semantics.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Designing a cooperative game**

I need an example that showcases a mathematical scenario where agents cooperate instead of using an unfair code reward. So, I'm thinking about creating two agents in a cooperative game. Each agent will have a private cost—let's say possible costs are 1 or 3, with a probability of 1/2. If both agents decide to contribute, they can each benefit from a total of 4. This setup highlights the dynamics of cooperation effectively!
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/5f5ca3ab-7aef-4f2a-83ea-8b881f06adc2/call_0/request.json)

[Authoritative raw response](../../../../../../runs/5f5ca3ab-7aef-4f2a-83ea-8b881f06adc2/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/5f5ca3ab-7aef-4f2a-83ea-8b881f06adc2/call_1/request.json)

[Authoritative raw response](../../../../../../runs/5f5ca3ab-7aef-4f2a-83ea-8b881f06adc2/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
