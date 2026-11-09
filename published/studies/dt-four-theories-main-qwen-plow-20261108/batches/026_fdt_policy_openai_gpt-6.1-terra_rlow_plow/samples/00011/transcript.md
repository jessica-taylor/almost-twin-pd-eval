# 026_fdt_policy_openai_gpt-6.1-terra_rlow_plow / 00011

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/e53582e1-cd39-4b8d-ab97-e1ad8faa43ab/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/e53582e1-cd39-4b8d-ab97-e1ad8faa43ab/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: choosing a policy as the output of a decision function

Policy functional decision theory, or **P-FDT**, asks an agent to evaluate not merely what would happen if it performed a different physical act, but what would happen if its decision procedure produced a different **policy**. A policy is a rule mapping possible inputs or observations to actions. Once a policy has been selected, the agent applies it to its actual input.

The distinction matters when other events depend on the same decision procedure: a predictor may have simulated it, another agent may run a copy, or the agent’s future selves may use the same rule. In such cases, changing the policy in a decision hypothetical can change more than the agent’s immediate act.

The primary source for P-FDT here is footnote 16 of Yudkowsky and Soares’ *Functional Decision Theory*. It says that the authors’ preferred formulation intervenes on the decision-function node to choose “not an action but a **policy** which maps inputs to actions,” and then applies that policy to the agent’s inputs. The paper mostly develops a simpler **action-output formulation of functional decision theory**, postponing the policy distinction.

That footnote gives the central shape of P-FDT, but not a complete algorithm. In particular, it does not specify the policy space, precisely which evidence enters policy evaluation, or how to construct logical counterfactuals. The account below distinguishes the source’s commitments from a proposed operational interpretation.

## 1. From actions to policies

Let \(\mathcal X\) be a set of possible inputs and \(\mathcal A\) a set of actions. A deterministic policy is a function

\[
\pi:\mathcal X\longrightarrow\mathcal A.
\]

An input might include an observation history, the agent’s role in a game, available actions, and any other information the policy is allowed to use. In a sequential problem, it can be a history up to the present decision.

Suppose a P-FDT decision procedure \(D\), given a decision model \(M\), outputs a policy:

\[
\Pi=D(M).
\]

The agent’s action on input \(x\) is then

\[
A=\Pi(x).
\]

There is an important distinction between **the mathematical output** \(D(M)\) and **a variable in the agent’s model representing that output**. Write the latter as \(Z\). P-FDT constructs decision hypotheticals by intervening on \(Z\), setting it to candidate policies. It does not claim that an agent can physically reach into mathematics and alter the value of a function.

A schematic formulation is

\[
\pi^* \in \operatorname*{arg\,max}_{\pi\in\mathcal P}
\mathbb E_{M^{[\pi]}}[U],
\qquad
a=\pi^*(x),
\tag{1}
\]

where:

- \(\mathcal P\) is a specified class of admissible policies;
- \(M^{[\pi]}\) is the model constructed by setting \(Z=\pi\) and propagating relevant dependencies;
- \(U\) is the agent’s utility over outcomes;
- \(x\) is the input on which the selected policy is actually applied.

Equation (1) is an **interpretation**, not an equation supplied by footnote 16. Its purpose is to make the footnote’s policy-selection passage usable. The source’s action-output formalization supplies the analogy: it intervenes on a representation of a decision-function output, propagates dependencies through a graph, and compares expected utilities.

The graph is not an ordinary causal graph alone. It can contain arrows for causal dependence, but also for dependence on a shared computation. For example, a predictor’s simulation and an agent’s physical action can both depend on \(Z\), even if the prediction occurred yesterday and the action occurs today.

## 2. What changes in a policy hypothetical?

The source calls the relevant relationship **subjunctive dependence**. Its basic example is two systems computing the same mathematical function. If both are reliable implementations on the same input, their outputs match because they compute the same thing—not because one physically signals the answer to the other.

In a P-FDT hypothetical, setting \(Z=\pi\) should therefore change:

1. actions produced by actual or simulated applications of that policy;
2. predictions that depend on those applications;
3. physical consequences downstream of those actions and predictions.

It should not automatically change a variable merely because that variable is statistically correlated with an action. Nor should it automatically change every other agent who happens to be similar. A dependency must be supported by the model.

This gives three contrasts:

- **Evidential decision theory (EDT)** evaluates an action using conditional expectations such as \(\mathbb E[U\mid A=a,x]\). This can preserve correlations that would not survive changing the decision procedure.
- **Causal decision theory (CDT)** evaluates an action by a causal intervention on the physical act. It normally holds earlier predictions fixed.
- **P-FDT** evaluates policies by a functional intervention on the represented policy output, preserving modeled causal *and* computational dependencies.

The intervention is not ordinary conditionalization on \(Z=\pi\). A deterministic function has one actual output; alternative outputs are logically incompatible with its complete specification. Conditioning a logically omniscient probability distribution on a false mathematical statement is undefined. The source instead treats hypotheticals as constructed tools, and admits that a general account of such **counterpossibles** remains open.

For practical modeling, one can give a structural model with a policy node \(Z\), equations for its applications, predictor behavior, and causal consequences. For each candidate \(\pi\), replace the equation determining \(Z\) with \(Z=\pi\), then recompute downstream variables. This is a useful operational surrogate, but its results depend on the supplied structure. A graph does not, by itself, discover which logical dependencies are real.

## 3. An operational interpretation

The following procedure is a proposed way to apply P-FDT, rather than a fully specified rule from the footnote.

1. **Define the input and policy spaces.** Specify what a policy can observe and what actions are available at each input. Include relevant counterfactual inputs, not just the one actually encountered.
2. **Choose an evaluation perspective.** Construct a model \(M\) containing the information and probabilities used to compare policies. Distinguish evidence that should remain background evidence from observations whose occurrence may itself depend on the policy.
3. **Identify the policy-output node.** Represent the output of the decision procedure by \(Z\). Identify physical actions, copies, simulations, and predictions that depend on it.
4. **Intervene on the whole policy.** For each \(\pi\in\mathcal P\), set \(Z=\pi\). Apply it at every modeled input where that same output is implemented or represented; propagate the resulting dependencies and ordinary causal effects.
5. **Calculate expected utility.** Average over uncertainty in states, predictor errors, observations, and outcomes under each policy hypothetical.
6. **Select and apply.** Choose a maximizing policy, using a specified tie-breaker if needed, and execute \(\pi^*(x)\) at the actual input.

This is not a license to suppose that any favorable correlation persists. The model must say *why* a predictor, copy, or future decision responds to a changed policy. With imperfect predictors, the response will generally be probabilistic.

The scope of the intervention is especially important. If two systems apply the **same policy output** to different inputs, changing that output can change both applications. If they run different algorithms, or have different models such that they select different policies, further assumptions are needed to link them. “Both use P-FDT” is not, by itself, proof that their outputs are identical.

## 4. P-FDT and Newcomb’s problem

A predictor places \$1 million in an opaque box if it predicts that the agent will take only that box. A transparent box contains \$1,000. The predictor is correct 99% of the time.

For a simple P-FDT model, consider constant policies \(\pi_1\) and \(\pi_2\), which respectively one-box and two-box. Assume the predictor’s accuracy is 99% under *each* candidate policy. Then

\[
\begin{aligned}
V(\pi_1)&=0.99(1{,}000{,}000)=990{,}000,\\
V(\pi_2)&=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\end{aligned}
\]

P-FDT selects \(\pi_1\), and the agent one-boxes.

This does not require the agent to believe that taking a box physically changes the past. The hypothetical instead says: if the decision-function output were a two-boxing policy, a reliable predictor of that output would probably have predicted two-boxing. The past prediction varies across the constructed hypotheticals, even though no signal travels backward in time.

The assumption about accuracy deserves attention. A predictor’s observed 99% success rate across some population does not by itself prove 99% accuracy under every counterfactual policy. For an unfamiliar case, one needs a model of *how* the prediction responds to policy changes, not just an overall accuracy statistic.

In a smoking-lesion problem, by contrast, suppose an unobserved lesion causes both a desire to smoke and cancer, while smoking itself has no effect on cancer. If changing the policy does not change the lesion or cancer risk, and smoking gives the agent a positive benefit, P-FDT’s policy hypothetical favors smoking. The mere fact that smokers are more likely to have the lesion is not enough to make the lesion vary with the policy intervention. The source notes that fully specifying this famous example raises complications about the agent’s knowledge of its preferences; the simpler lesson is the distinction between predictive dependence and common-cause correlation.

## 5. Observations and the value of a whole policy

Consider a transparent variant of Newcomb’s problem. The predictor fills the large box if it predicts that the agent will take only the large box **when seeing it full**. A policy must now specify what to do on both inputs:

\[
\pi=(\pi(\text{full}),\pi(\text{empty})).
\]

Assume a perfect predictor. Compare:

\[
\begin{array}{c|c|c}
\text{Policy} & \text{Predicted full-box action} & \text{Outcome}\\ \hline
(\text{one-box},\text{two-box}) & \text{one-box} & \$1{,}000{,}000\\
(\text{two-box},\text{two-box}) & \text{two-box} & \$1{,}000
\end{array}
\]

The first policy one-boxes if the large box is full but takes the \$1,000 if it is empty. It is better in this model. Thus, if the agent actually sees a full box, it applies the first policy and one-boxes.

The striking feature is that the alternative-policy hypothetical need not preserve the actual observation of a full box. Under the two-box-when-full policy, the predictor would leave the large box empty, so the agent would see a different input. The policy is nevertheless defined at the full-box input, because that is the behavior the predictor examines.

This makes evidence treatment a central unresolved issue. If one simply conditions every candidate policy’s evaluation on “the box is full,” then a perfect predictor makes the two-box-when-full policy’s relevant event impossible. With a fallible predictor, conditioning on the full box can instead make taking both boxes look better after the observation. That is not the global policy comparison illustrated above.

My proposed interpretation is to evaluate policies from a specified background model **before conditioning on policy-dependent observations**, and then apply the selected policy to the actual observation. The observation still matters: it determines which branch of the policy is executed. It also appears in the model and can be used by the policy. What is avoided is requiring it to remain fixed across hypotheticals in which the policy changes whether it occurs.

This is close to the source’s action-output discussion, in which an alternative decision-function output can lead to a different observation. But footnote 16 alone does not settle exactly which information belongs in the background model or when a new policy-selection problem is initiated. Different answers can yield different prescriptions. A practical implementation must state its choice rather than hide it in notation.

## 6. Why policy selection matters between agents

The difference between intervening on a current action and intervening on a whole policy is visible when copies receive different inputs.

Suppose two causally isolated agents implement the same selected policy. One receives input \(L\), the other \(R\). Each chooses \(C\) or \(D\), and both receive the following payoff:

\[
\begin{array}{c|cc}
 & R:C & R:D\\ \hline
L:C & 0 & 10\\
L:D & 1 & 0
\end{array}
\]

The shared policy \(\pi\) specifies an action for each input. Under the assumption that both agents’ actions are applications of the same policy output, the four deterministic policies give:

\[
\begin{array}{c|c}
(\pi(L),\pi(R)) & \text{payoff}\\ \hline
(C,C)&0\\
(C,D)&10\\
(D,C)&1\\
(D,D)&0
\end{array}
\]

A P-FDT comparison selects \((C,D)\): the \(L\)-agent cooperates and the \(R\)-agent defects. This is not an instruction that everyone should take the same action. It is an instruction to evaluate a **shared mapping**, which can prescribe different actions on different inputs.

A local intervention that changes only the output at \(L\), while holding the \(R\)-output fixed, is a different counterfactual. Depending on how that fixed output is chosen, it may fail to compare the coordinated change from \((D,C)\) to \((C,D)\). The example explains why the policy distinction can matter in multi-agent cases, as footnote 16 suggests.

It also exposes an open modeling question. If each agent independently selects a policy using a model centered on its own role, do they in fact share the same policy output? If their utilities conflict, which utility evaluates the shared mapping? One cannot assume a common objective merely because agents use the same decision-theoretic name. A complete model must specify each agent’s utility, inputs, computation, and the dependency between their outputs.

The familiar psychological-twin prisoner’s dilemma is a simpler special case. Identical agents on identical inputs compute the same action. In the source’s payoffs, mutual cooperation gives each \$1 million and mutual defection \$1,000. If the functional intervention changes both outputs together, cooperation is preferred. If the agents are only imperfectly similar, the model should instead assign appropriate probabilities to the other agent’s response; cooperation is not guaranteed.

## 7. Threats, errors, and global trade-offs

Suppose a blackmailer launches a damaging program only if they predict that the agent will pay \$1,000 upon receiving a threat. If launched and not stopped by payment, it causes \$1 million of damage.

With a perfect predictor, a pay-if-threatened policy invites the threat and costs \$1,000. A refuse-if-threatened policy prevents the threat and costs nothing. On the global interpretation, P-FDT selects refusal even at the threat input.

With an imperfect predictor, the conclusion depends on the error rates. For example, assume a pay policy is always threatened and a refuse policy is mistakenly threatened with probability \(\varepsilon\). Then

\[
V(\text{pay})=-1{,}000,\qquad
V(\text{refuse})=-1{,}000{,}000\varepsilon.
\]

Refusal is better if \(\varepsilon<0.001\). At \(\varepsilon=0.0009\), expected loss is \$900; at \(\varepsilon=0.0011\), it is \$1,100, so payment is better under these assumptions. The exact threshold changes if the blackmailer sometimes fails to threaten a payer, if other costs matter, or if prediction accuracy depends on the policy.

The uncomfortable case is an agent holding a threat despite having selected refusal. In the model, this is an unusual predictor error; paying would avert damage in that particular situation. The global policy rationale nevertheless counts the benefit of being predictably resistant across the scenarios generated by the policy. Whether that is the right normative perspective is contested. It should not be disguised as a claim that refusal physically stops an already running program.

## 8. Limits and philosophical stakes

P-FDT’s attraction is that it asks the agent to take its place in the world seriously: its reasoning can be predicted, copied, and used as a basis for others’ actions. The precommitment analogy is illuminating. An agent that could publicly bind itself to one-box before a predictor acts would often want to do so. P-FDT instead evaluates a policy as the output of the present decision procedure and accounts for predictors of that output.

But “act as one would have precommitted” is not a complete definition. The relevant precommitment time, information, and available commitments are themselves questions. Nor does policy selection prove that P-FDT always achieves the highest actual utility. The source explicitly acknowledges that decision problems can be constructed to reward one theory or punish another. Its proposed restriction to “fair” problems is informal, not a general optimality theorem.

Several technical questions remain:

- **Logical dependence:** How can an agent infer the right response of a predictor or another computation to a counterpossible policy output?
- **Policy granularity:** Does intervention change the entire policy, one component, or some intermediate object? Footnote 16 points toward a whole policy but does not fully specify its identity or domain.
- **Evidence:** Which observations are fixed background information, and which may vary under the policy intervention?
- **Randomization:** A stochastic policy requires a model of whether predictors and copies share, observe, or independently sample random seeds.
- **Self-reference and existence:** Representing a decision function inside its own model is possible in principle, but this alone does not guarantee a tractable procedure or that every specified optimization problem has a unique solution.

These are not merely implementation details. Different answers can change the policy ranking. For an unfamiliar problem, the responsible P-FDT analysis is therefore to present the candidate policies, the dependency model, and the evaluation perspective, and to show how the result changes under plausible alternatives.

## Conclusion

P-FDT evaluates candidate **policies** as alternative outputs of a decision procedure, propagates the modeled consequences through actions, predictions, copies, and causal effects, and applies the selected policy to the actual input. Its distinctive ambition is to preserve genuine computational and predictive dependencies without treating every statistical correlation as controllable.

Footnote 16 supplies that policy-selection idea; it does not finish the theory. A usable P-FDT analysis consequently requires explicit assumptions about policy scope, evidence, and counterpossible dependence. Making those assumptions visible is what turns an appealing philosophical principle into a decision procedure that can be examined and applied.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, version 2, especially footnotes 7 and 16 and sections 3–6. https://arxiv.org/abs/1710.05060v2
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/390e6b22-c4d9-49ad-8b47-fe713bd27e2d/call_0/request.json)

[Authoritative raw response](../../../../../../runs/390e6b22-c4d9-49ad-8b47-fe713bd27e2d/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/390e6b22-c4d9-49ad-8b47-fe713bd27e2d/call_1/request.json)

[Authoritative raw response](../../../../../../runs/390e6b22-c4d9-49ad-8b47-fe713bd27e2d/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
