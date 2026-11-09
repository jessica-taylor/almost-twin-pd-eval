# 027_fdt_policy_openai_gpt-6.1-sol_rhigh_phigh / 00010

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/bbf11054-0f2d-4043-9a37-48dde5e1dc9b/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/bbf11054-0f2d-4043-9a37-48dde5e1dc9b/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: Choosing the Policy Behind the Action

A decision can matter beyond its immediate physical consequences. A predictor may already have acted on a forecast of it; another agent may be running the same computation; future encounters may depend on whether one is predictably cooperative or exploitable. **Policy functional decision theory (P-FDT)** asks us to evaluate decision-making at the level of an input–output policy while preserving these dependencies.

The primary source for this account is footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality*. It describes their preferred formulation as choosing not an action but “a policy which maps inputs to actions,” and then applying that policy to the agent’s inputs. Most of the paper instead develops an action-selection formulation for expositional convenience. The authors say that policy selection can make a difference in multi-agent dilemmas, but do not fully formalize those differences.

That distinction matters. P-FDT is not merely a recommendation to plan ahead. Its characteristic proposal is to evaluate alternative policies as hypothetical outputs of the agent’s policy-selection computation, allowing predictors and other computationally dependent systems to respond accordingly. The following develops a mathematical interpretation of that proposal, distinguishing the source’s commitments from additional modeling choices.

## 1. The object of choice in P-FDT

Let \(\mathcal X\) be a finite set of possible decision inputs and \(\mathcal A\) a finite action set. A deterministic policy is a function
\[
\pi:\mathcal X\longrightarrow\mathcal A.
\]
An input may represent a current observation, an observation history, a private signal, or another decision-relevant circumstance. For sequential problems, \(\mathcal X\) can contain histories, making a policy a complete contingent plan.

Write \(\mathcal P\subseteq\mathcal A^{\mathcal X}\) for the admissible policies. At actual input \(x\), executing policy \(\pi\) means taking action \(\pi(x)\).

Policy comparison therefore differs from comparing only currently available physical actions. Two policies can prescribe the same action at \(x\) but different actions elsewhere. Those differences may affect another agent’s prediction, whether an encounter occurs, or how a computational counterpart behaves on a different input.

The footnote does not settle exactly what counts as an “input,” or how broad the policy’s domain should be. I will initially treat \(\mathcal X\) as a specified family of contingencies within one decision problem. Extending it to every possible future circumstance introduces substantial questions about learning, changing preferences, and computational feasibility.

## 2. A mathematical rule for P-FDT

Let \(M\) be a world-model containing:

- probabilities over unresolved background conditions;
- a utility function \(U\) on outcomes;
- causal and computational dependency information;
- representations of the agent, relevant predictors, and computational counterparts.

Suppose a selector \(\mathsf S\) takes \(M\) and returns a policy. Within \(M\), let \(\boldsymbol\Pi_M\) denote the represented output of that very selector:
\[
\boldsymbol\Pi_M\quad\text{represents}\quad\mathsf S(M).
\]

For each candidate \(\pi\), construct a counterfactual outcome distribution
\[
Q_M^\pi(o)
=
P_M\!\left(
O=o\mid
\operatorname{do}_{\mathrm{sub}}(\boldsymbol\Pi_M=\pi)
\right).
\]
Here \(\operatorname{do}_{\mathrm{sub}}\) denotes a **subjunctive intervention**: a hypothetical alteration of the selector’s output, propagated through the model’s relevant dependencies. It is not automatically an ordinary physical intervention.

A natural P-FDT reconstruction is
\[
V_M(\pi)=\sum_o Q_M^\pi(o)U(o),
\]
\[
\pi_M^*
=
\operatorname{TieBreak}
\left(
\arg\max_{\pi\in\mathcal P}V_M(\pi)
\right),
\qquad
\mathrm{P\text{-}FDT}(M,x)=\pi_M^*(x).
\]

This captures the footnote’s selection-and-application structure. The precise notation, policy domain, and tie-breaking convention are additions to the source.

To make the proposal operational, consider a simple structural model:
\[
W\sim\mu,\qquad
Y=f(W,\boldsymbol\Pi_M),\qquad
X=g(W,Y),
\]
\[
A=\boldsymbol\Pi_M(X),\qquad
O=h(W,Y,X,A).
\]
Here \(W\) contains background uncertainty; \(Y\) may include predictions or other agents’ responses. Evaluating \(\pi\) replaces the represented selector output by \(\pi\), recomputes downstream variables, and averages utility over \(W\).

Importantly, \(X\) can itself vary between policy counterfactuals. A policy might induce rescue rather than abandonment, or deter an encounter that another policy invites.

This finite, acyclic construction supplies a usable calculation procedure. It does not solve the general problem of constructing the right dependency model.

## 3. Which dependencies does P-FDT preserve?

The paper calls the relevant relationship **subjunctive dependence**. Its central examples are computations, copies, and predictors whose outputs track the same decision procedure.

Three relationships must be distinguished.

**Causal dependence.** If the selected policy makes the agent press a button, and pressing it rings a bell, the bell changes in the policy counterfactual.

**Computational dependence.** If a perfect simulation computes how the selected policy responds to input \(x\), changing that response changes the simulation’s answer—even if the simulation ran yesterday.

**Merely statistical dependence.** If an unrelated background condition correlates with the agent’s action without responding to its policy computation, the intervention need not change that condition.

For comparison, evidential decision theory (EDT) evaluates actions using conditional expectations such as
\[
\mathbb E[U(O)\mid X=x,A=a].
\]
Causal decision theory (CDT) instead uses causal interventions, schematically
\[
\mathbb E[U(O)\mid X=x,\operatorname{do}(A=a)].
\]
P-FDT changes both the object varied—a policy rather than a physical action—and the dependencies preserved.

This requires more information than an observed correlation. A predictor’s historical accuracy does not by itself determine how its forecast changes under every policy intervention. We need a model of what it predicts and how its errors arise.

Nor does sharing a decision theory automatically synchronize agents. Identical policies can receive different inputs. Imperfectly similar reasoners require an explicit account of their computational relationship.

There is also a foundational difficulty. A fixed deterministic selector has only one actual output on fixed input \(M\). Hypothesizing another output can therefore be **counterpossible**, contrary to a mathematical fact. The paper acknowledges that it lacks a general theory of these counterpossibles.

Operationally, one can treat an intervention as a controlled model rewrite: suspend the equation defining the selector’s output while retaining specified dependencies elsewhere. One does not reason from a contradiction using unrestricted classical logic. Whether such rewrites admit a uniquely satisfactory general semantics remains open.

## 4. P-FDT in Newcomb’s problem and the smoking lesion

In Newcomb’s problem, an opaque box contains \(B\) dollars if a predictor forecasts one-boxing and nothing otherwise. A transparent box contains \(s\). The agent may take only the opaque box or both.

Assume a symmetric prediction-error model with accuracy \(p\), and that the predictor tracks the selected policy’s response to this encounter. Then
\[
V(\text{one-box policy})=pB,
\]
\[
V(\text{two-box policy})=(1-p)B+s.
\]
P-FDT one-boxes exactly when
\[
(2p-1)B>s.
\]
For \(p=0.99\), \(B=1{,}000{,}000\), and \(s=1{,}000\), the values are \(990{,}000\) and \(11{,}000\).

This is not a claim that taking one box physically changes the past. The hypotheses concern alternative outputs of a computation that the predictor was modeling. The action and earlier forecast vary together because of their shared computational dependency.

Contrast the imaginary smoking-lesion problem. Suppose smoking provides \(1{,}000\) utility, while a lesion causes both a tendency to smoke and cancer. Smoking itself does not cause cancer, and the lesion does not consult the policy selector.

Under those stipulated dependencies,
\[
Q^{\pi_{\mathrm{smoke}}}(\text{cancer})
=
Q^{\pi_{\mathrm{refrain}}}(\text{cancer}).
\]
P-FDT therefore smokes: the health term cancels, leaving the stipulated enjoyment.

This is a diagnostic illustration, not medical advice. The source itself warns that formalizing the lesion problem raises difficulties concerning preferences and self-knowledge. The important lesson is narrower: correlation with an action does not establish responsiveness to the selected policy.

## 5. Observation and P-FDT policy evaluation

The most consequential interpretive choice concerns observations. Should policies be ranked conditional on everything currently observed?

The paper’s action-selection formulation sometimes evaluates hypotheses in which the agent would have made different observations. Footnote 16 places policy selection against that background, but does not independently specify a complete updating rule.

A reasonable operational interpretation is:

> Evaluate complete policies from a specified reference model, allowing policy-dependent observations to vary; then apply the selected policy to the actual observation.

This is the interpretation used in the examples below. It does **not** mean that the agent disbelieves its observations. Factual inference and policy evaluation have different tasks.

Consider Parfit’s hitchhiker with a perfect predictor. A driver rescues a stranded agent only if she predicts payment of \(c\) upon reaching the city. Abandonment costs the agent \(D\), where \(D>c\).

The relevant policies include
\[
\pi_{\mathrm{pay}}(\text{city})=\text{pay},
\qquad
\pi_{\mathrm{refuse}}(\text{city})=\text{refuse}.
\]
Their policy-level values are
\[
V(\pi_{\mathrm{pay}})=-c,
\qquad
V(\pi_{\mathrm{refuse}})=-D.
\]
P-FDT selects payment.

Upon reaching the city, an exclusively local causal comparison favors keeping the money. But changing the policy’s response to arrival also changes the driver’s earlier prediction and hence whether arrival occurs. P-FDT implements the policy whose predicted response secured rescue.

Transparent Newcomb has the same structure. Suppose the predictor fills the large box exactly when she predicts that the policy would leave the small box behind upon seeing both full. A policy prescribing one-boxing on that input earns the large reward. A policy prescribing two-boxing there normally encounters an empty large box instead.

These recommendations depend on allowing policy-dependent observations to vary. If one instead conditions policy evaluation on “I am already in the city” or “the large box is full,” the result can differ. Thus the evaluation baseline is substantive, not an innocuous notational choice.

## 6. Why P-FDT selects whole policies

The policy-selection distinction becomes especially clear when computational counterparts receive different private inputs.

Consider two agents implementing the same selected policy. Each independently receives a uniformly random bit \(x_i\in\{0,1\}\), then chooses **invest** or **skip**. Each agent receives
\[
u_i
=
10\,\mathbf 1\{\text{both invest}\}
-
6\,\mathbf 1\{\text{agent }i\text{ invests}\}.
\]
The policy counterfactual changes the shared policy used by both agents. This dependency is part of the stipulated model, not a consequence of merely labeling both agents P-FDT agents.

There are four deterministic policies. If a policy invests on a fraction \(q\) of inputs, then
\[
q\in\left\{0,\frac12,1\right\}.
\]
Because the private bits are independent, expected utility for either agent is
\[
V(q)=10q^2-6q.
\]
Therefore,
\[
V(0)=0,\qquad
V(1/2)=-\frac12,\qquad
V(1)=4.
\]
P-FDT selects “invest on both inputs.”

This example also shows why complete-policy optimization cannot always be replaced by changing one policy entry at a time. Starting from “skip on both inputs,” changing either single entry lowers value from \(0\) to \(-1/2\). Changing both raises it to \(4\).

The example is my illustration, not one supplied by the footnote. It demonstrates a mathematical distinction between whole-policy search and one-entry-at-a-time improvement; it does not prove that every action-selection formulation must fail here.

Notice also that a shared policy need not produce identical actions. Under a mixed policy, different private bits can yield different choices. P-FDT preserves the common input–output rule, not an unconditional requirement that everyone act alike.

## 7. P-FDT and imperfect blackmail

Policy evaluation can recommend resisting a threat despite occasional costly mistakes.

Suppose a blackmailer normally targets an agent exactly when she predicts payment. Paying costs \(c\); refusing after being targeted causes loss \(L\). Assume the blackmailer always targets a payer but mistakenly targets a refuser with probability \(\varepsilon\).

For the two response policies,
\[
V(\pi_{\mathrm{pay}})=-c,
\qquad
V(\pi_{\mathrm{refuse}})=-\varepsilon L.
\]
Hence P-FDT refuses when
\[
\varepsilon L<c.
\]
With \(L=1{,}000{,}000\), \(c=1{,}000\), and \(\varepsilon=0.0009\), refusal has expected loss \(900\), compared with payment’s \(1{,}000\).

Under the reference-model interpretation, P-FDT implements refusal even in the rare case where the demand arrives. The policy accepts occasional losses in exchange for deterring most attempts.

But refusal is not categorical. If \(\varepsilon L>c\), payment is preferable in this model. And if targeting is wholly independent of the response policy, the deterrence benefit disappears; paying may then minimize loss.

The dependency model does the work. P-FDT is neither blanket defiance nor an instruction to reinterpret every unwelcome observation as avoidable.

## 8. Applying P-FDT—and recognizing its open questions

For an unfamiliar case, the procedure is:

1. **Specify the policy domain.** Identify the inputs and admissible actions.
2. **Locate the represented selector output.** Distinguish the mathematical policy from a particular bodily action.
3. **Model responsiveness.** Determine which predictions, counterparts, observations, and consequences vary with the policy.
4. **Choose an evaluation baseline.** State which evidence is incorporated into the reference model and which observations can vary counterfactually.
5. **Evaluate complete policies.** Compute expected utility under each policy intervention.
6. **Execute the selected policy at the actual input.**

Several unresolved issues limit this recipe.

First, **the reference model is not uniquely specified by footnote 16**. The interpretation developed here holds fixed a model spanning the policy-dependent observations under comparison. It should not be mistaken for a fully specified requirement to retain one original prior forever. How to incorporate unexpected discoveries without destroying useful policy commitments remains a central question.

Second, **logical intervention structure must be justified**. One should not infer a dependency merely because assuming it would produce a desirable result. Exact copies and explicit simulations provide comparatively clear cases; partial similarity and unfamiliar predictors do not.

Third, **self-reference is not automatically harmless in every model**. Representing the selector’s own output is possible, but this alone does not establish the existence, uniqueness, or computability of a satisfactory selection rule in arbitrary interactive settings.

Fourth, **policy representation matters**. Extensional functions are sufficient when the environment responds only to input–output behavior. If an opponent rewards particular source code, proof methods, or architectures, a bare policy may omit relevant information. The paper explicitly recognizes that no decision theory wins against every possible procedure-targeting environment.

Finally, **computational limits matter**. Even finite policy spaces grow exponentially with the number of inputs. Practical P-FDT would require restricted policy classes and approximate dependency models, with approximation costs included where relevant.

One attractive implication survives under clear assumptions: costless information cannot reduce optimal policy value if the enlarged policy space includes ignoring it and doing so leaves the environment unchanged. Every old policy remains available. This is a conditional result, not a universal theorem covering every predictor-sensitive setting.

## Reference

Yudkowsky, Eliezer, and Nate Soares. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2. Especially footnotes 7 and 16, and §§3, 5–6, and 9.

## Conclusion

P-FDT evaluates actions through complete policies and evaluates policies through counterfactuals that preserve relevant causal and computational dependencies. It can therefore account for prediction, conditional rescue, coordinated counterparts, and deterrence without treating every correlation as controllable. Its central unresolved task is equally clear: specify principled policy counterfactuals and evaluation baselines. Given those inputs, P-FDT offers a concrete instruction—select the policy with greatest expected utility, then apply it to the situation actually observed.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/10ac914b-8306-4f15-98fc-da09cd622e59/call_0/request.json)

[Authoritative raw response](../../../../../../runs/10ac914b-8306-4f15-98fc-da09cd622e59/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/10ac914b-8306-4f15-98fc-da09cd622e59/call_1/request.json)

[Authoritative raw response](../../../../../../runs/10ac914b-8306-4f15-98fc-da09cd622e59/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
