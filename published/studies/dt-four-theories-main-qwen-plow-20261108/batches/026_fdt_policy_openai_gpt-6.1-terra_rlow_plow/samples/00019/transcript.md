# 026_fdt_policy_openai_gpt-6.1-terra_rlow_plow / 00019

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/7a65909f-fc8e-4938-a7cb-4c2b244beebd/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/7a65909f-fc8e-4938-a7cb-4c2b244beebd/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: choosing a policy as the output of a decision procedure

A decision can affect more than its immediate physical consequences. A lender may decide whether to offer a contract based on a prediction of whether the borrower will repay. A bargaining partner may make a concession only if she expects it to be reciprocated. A copy of a computer program may reach the same conclusion as another copy without receiving a signal from it.

**Policy functional decision theory**, or **P-FDT**, asks an agent to take these dependencies seriously. Its central question is not simply “What happens if I perform this physical act?” but roughly:

> What would the world be like if the policy produced by this decision procedure were different?

The policy is then applied to the agent’s observations to select an action. This distinction matters when predictors or other agents respond to the policy as a whole, including what it would prescribe in situations that do not actually occur.

The primary source for P-FDT here is footnote 16 of Yudkowsky and Soares’ *Functional Decision Theory*. It says that their preferred formulation “intervenes on the node … to choose not an action but a **policy** which maps inputs to actions, to which the agent then applies her inputs in order to select an action.” The paper mostly develops an action-output formulation, which I will call **action-FDT** when distinguishing it from P-FDT. The authors say that, as far as they can tell, the difference matters only in multi-agent dilemmas. They do not supply a complete policy-level algorithm. The formal construction below is therefore an interpretation, not a theorem or a verbatim specification from the paper.

## 1. Actions, policies, and the object of intervention

Let \(X\) be a set of possible inputs or observation histories, and let \(A(x)\) be the actions available after input \(x\). A deterministic policy is a function

\[
\pi:X\longrightarrow A,\qquad \pi(x)\in A(x).
\]

It says what the agent would do at each relevant input, not merely at the one actually encountered. A policy might say:

- repay if rescued and asked for payment;
- take the extra money if the box is empty;
- cooperate if the other player has also received a specified message.

In footnote 16, the P-FDT decision procedure selects such a mapping. We can represent the selected policy by a variable \(\Pi\) in a world-model. If the actual input is \(x\), the agent performs

\[
a=\Pi(x).
\]

To evaluate a candidate policy \(\pi\), the agent constructs a hypothetical in which the output of its policy-selection computation is \(\pi\). It then asks how other variables that depend on that output would behave.

A schematic rule is

\[
\pi^*\in\arg\max_{\pi\in\mathcal P}
\mathbb E\!\left[U(O)\mid \operatorname{do}(\Pi=\pi)\right],
\qquad
a^*=\pi^*(x).
\tag{1}
\]

Here \(O\) is the outcome, \(U\) is the agent’s utility, and \(\mathcal P\) is a set of candidate policies. The notation \(\operatorname{do}\) denotes model surgery: replace the model’s equation for \(\Pi\) with \(\Pi=\pi\), then propagate the change through the dependencies represented in the model.

Equation (1) is a **proposed operational interpretation** of footnote 16. It deliberately resembles the paper’s graphical action-FDT equation, but a policy-output node is not specified there in comparable detail. In particular, the footnote does not tell us exactly which policy space to use, how to construct the dependency graph, how to treat new evidence, or how different agents’ policy computations are related.

The distinction between a *represented output* and the output itself is important. \(\Pi\) is a variable in a model that represents the result of the P-FDT computation. Setting that variable to a candidate value is an operation on a hypothetical model; it is not a claim that the agent can physically rewrite a mathematical fact or send information into the past.

## 2. What makes a dependency relevant?

The source calls the relevant relationship **subjunctive dependence**. Two physical systems can depend on the same computation: two reliable calculators given the same arithmetic problem will agree, even if no signal passes between them. Likewise, a predictor’s simulation of an agent and the agent itself may be linked because both reflect the same decision computation.

This is broader than physical causation. If a decision procedure’s hypothetical output changes, a reliable prediction made yesterday may change in the hypothetical too. But it is narrower than statistical correlation. An event does not automatically change in the hypothetical merely because observing an action would provide evidence about it.

This separates P-FDT from two familiar approaches:

- **Evidential decision theory** evaluates an action using something like \(\mathbb E[U\mid X=x,A=a]\). It asks what the action would be news about.
- **Causal decision theory** evaluates it using something like \(\mathbb E[U\mid X=x,\operatorname{do}(A=a)]\). It changes the physical action and its causal descendants.
- **P-FDT**, on the interpretation above, changes the represented output of a policy-selection computation, propagating the consequences through relevant causal, computational, predictive, and other dependencies.

Suppose a lesion causes both an agent’s desire to smoke and a high cancer risk, while smoking itself has no effect on cancer. If the agent values smoking positively, P-FDT need not treat a policy of smoking as changing the lesion or cancer. Those variables are not modeled as computations of the agent’s policy. Subject to those assumptions, smoking gains its benefit without changing the cancer risk.

By contrast, a predictor who models the policy may respond differently to different policy outputs. The distinction is not “past versus future”: both the lesion and a prediction may be in the past. It is whether the past event is represented as depending on the decision computation in the relevant hypothetical.

The paper acknowledges that identifying these dependencies is a major open problem. A graph with the right arrows can encode an answer; it does not by itself explain how to discover them. In an unfamiliar case, the modeler must ask what the predictor actually inspects, simulates, or infers; whether a purported copy receives the same inputs; and whether errors or independent randomness weaken the relationship.

## 3. P-FDT in Newcomb’s problem

In Newcomb’s problem, a transparent box contains \$1,000. An opaque box contains \$1 million if a predictor predicted that the agent would take only the opaque box. Assume that, under either candidate policy, the predictor gets the relevant prediction right with probability \(0.99\).

Let \(\pi_1\) prescribe one-boxing and \(\pi_2\) prescribe two-boxing. If the predictor’s prediction subjunctively depends on which policy P-FDT outputs, then

\[
\begin{aligned}
V(\pi_1)&=0.99(1{,}000{,}000)=990{,}000,\\
V(\pi_2)&=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\end{aligned}
\]

P-FDT selects \(\pi_1\), and the agent takes one box.

A causal decision theorist instead holds the already-filled box fixed when varying the physical act; taking both boxes then adds \$1,000. P-FDT’s different conclusion comes from a different hypothetical: changing the policy output also changes what the reliable predictor predicted.

The \(0.99\) figures in this calculation are not licensed by any generic statement that the predictor is “99% accurate” in some population. They must describe its behavior under the particular policy interventions being compared. If accuracy varies by policy, the values must use the appropriate rates.

The source describes such hypotheticals as **counterpossibilities**. A fixed deterministic computation on fixed inputs has one mathematical output. Nevertheless, the model asks what would follow if its represented output were otherwise. The paper proposes graphical surgery as a practical placeholder for this sort of reasoning, while conceding that a general account of counterpossible reasoning is not yet available.

## 4. Information and policies that change what is observed

A policy is particularly useful when the input itself depends on what the predictor expects the policy to do.

In transparent Newcomb, suppose the predictor fills the large box if it predicts that the agent will one-box *upon seeing it full*. Let a policy specify actions for both observations, \(F\) and \(E\):

\[
\pi(F)\in\{\text{one},\text{two}\},\qquad
\pi(E)\in\{\text{one},\text{two}\}.
\]

Under a perfect predictor, a policy with \(\pi(F)=\text{one}\) leads to a full box and \$1 million. A policy with \(\pi(F)=\text{two}\) leads to an empty box; its best continuation is to take both and obtain \$1,000. Thus, under a model that evaluates the policy before fixing the observation, P-FDT selects a policy that one-boxes on \(F\) and two-boxes on \(E\).

The striking feature is what happens when the agent actually sees \(F\). The competing policy need not be evaluated in a hypothetical where \(F\) remains true. If the predictor would have left the box empty had it predicted \(\pi(F)=\text{two}\), the competing hypothetical contains observation \(E\) instead.

This does **not** mean that the agent should disbelieve its actual observation. Its factual belief can be that the box is full; its decision hypothetical can describe a different observation. The source’s action-FDT treatment makes this distinction explicitly.

For P-FDT, however, the correct treatment of evidence is not fully specified by footnote 16. Equation (1) embodies one reasonable proposal: use a probability model anchored at an appropriate point *before policy-dependent observations*, while allowing the policy to respond to those observations. It should not be read as a rule to ignore all known facts. Information available before the relevant policy-prediction process, for example, might appropriately be incorporated into the model from which policies are evaluated.

Nor is a prior anchor enough by itself to settle every case. If an agent later receives an observation that was highly surprising under every available policy, it may learn that its model of the predictor was wrong. Whether and how to revise the evaluation model while preserving the policy’s earlier predictive significance is a substantive design question. The footnote does not resolve it.

The same structure appears in Parfit’s hitchhiker. A driver rescues an agent only if she predicts the agent will pay after reaching town. A policy that pays conditional on rescue can produce rescue; a policy that refuses may produce abandonment. Under the relevant predictive model, P-FDT can prescribe paying after arrival, despite the immediate advantage of keeping the money.

## 5. Why the entire policy can matter

In the previous examples, the predictor chiefly cares about one policy entry: what the agent would do after seeing a full box or receiving a ride. But a policy-level intervention can matter even when two candidates prescribe the **same actual action**.

Suppose an agent will observe either \(L\) or \(R\), and a predictor rewards it if its policy prescribes matching the observation:

\[
\pi(L)=L,\qquad \pi(R)=R.
\]

The actual observation is \(L\). Both the matching policy and a policy that always chooses \(L\) prescribe the same immediate action. Yet the predictor distinguishes them because they differ at \(R\). A procedure that compares only the physical actions at \(L\) cannot represent this difference without adding some other variable for the off-path commitment.

This illustrates why footnote 16 matters. A P-FDT candidate is not merely a label for the current action. It contains behavior at other possible inputs, and those entries can affect predictions, opportunities, or other agents’ behavior.

There are limits to this point. Two policies that differ in an observation no predictor, copy, or future process can ever encounter or inspect may be equivalent for the problem. Conversely, if the environment reacts to the *code or description* of a policy rather than just its input-output behavior, extensional mappings \(\pi:X\to A\) may not suffice: the model needs a representation of implementation as well. Footnote 16 leaves that distinction open.

## 6. P-FDT and other agents

Consider the paper’s prisoner’s dilemma against a perfect psychological twin. Each player receives \$1 million if both cooperate, \$1,000 if both defect, and an extra \$1,000 for defecting against a cooperator.

If both players implement the same policy-selection computation on the relevant inputs, and an intervention on its output changes both implementations, the comparison is

\[
V(\text{cooperate})=1{,}000{,}000,\qquad
V(\text{defect})=1{,}000.
\]

P-FDT cooperates. It is not counting the twin’s welfare unless that welfare is part of its utility; it is recognizing a dependency between their decisions.

But “the other player is also a P-FDT agent” is not, by itself, enough to establish this linkage. The agents may have different information, different utilities, different roles, or different models. They may run different computations even if both use the same abstract decision-theoretic rule.

A useful modeling discipline is to distinguish:

1. **The same output node:** two implementations run the same relevant computation on the same inputs, so both change under one intervention.
2. **Different but dependent nodes:** the opponent predicts or responds to the candidate policy; the model specifies how.
3. **Independent nodes:** the opponent’s action does not vary with the intervention, even if the agents happen to use similar reasoning.

The second case is especially important in games. An opponent may react to a whole contingent policy rather than copy the agent’s current action. The model must describe that reaction; P-FDT does not automatically turn every game into mutual cooperation.

Nor does footnote 16 say whether the policy-selection output for one agent is identical to, correlated with, or independent of another agent’s policy-selection output. Different answers can yield different prescriptions. This is not a minor technicality: the source itself flags multi-agent dilemmas as the place where the distinction between action and policy formulation may matter.

## 7. A practical procedure—and its limits

For an unfamiliar problem, the following is a workable application of the interpretation in equation (1):

1. **Specify inputs and policies.** Include observations and later decisions that could matter. State which actions each policy prescribes, including relevant off-path actions.
2. **Choose the evaluation model.** Identify the information already incorporated into it, the uncertain states, the utility of outcomes, and where the policy output is represented.
3. **Model dependencies.** For each candidate policy, ask which predictions, copies, communications, physical events, and observations change. Leave unrelated background variables governed by their ordinary distributions.
4. **Compute policy values.** For each \(\pi\), calculate the expected utility under the policy-output intervention, including outcomes in which the actual observation does not occur.
5. **Select and apply.** Choose a maximizing policy, using an explicit tie-breaker if needed, and execute its prescription at the actual input.
6. **Check robustness.** Vary prediction accuracy and disputed dependency assumptions. A recommendation that reverses under small changes should not be presented as unconditional.

A graph is useful here only if its arrows are defended. For instance, if a blackmailer starts a damaging program only when she predicts payment, then refusal can discourage blackmail. With imperfect prediction, refusal is not invariably best. Suppose payment costs \$1,000 whenever blackmailed, while refusal causes \$1 million in damage only when a predictor mistakenly blackmails a refuser. If the relevant error probability is \(\varepsilon\), the stylized values are

\[
V(\text{pay})=-1{,}000,\qquad
V(\text{refuse})=-1{,}000{,}000\varepsilon.
\]

Refusal is better exactly when \(\varepsilon<0.001\). At \(\varepsilon=0.0009\), its expected loss is \$900; at \(\varepsilon=0.0011\), it is \$1,100. These conclusions depend on the stated mechanism and on evaluating from a perspective where receipt of the threat can vary with the policy. They are not general advice to refuse every real-world threat.

Further questions remain. How large should \(\mathcal P\) be? A policy over every conceivable history is generally intractable; a small policy class may omit the best option. Should randomized policies be included? If so, whether a predictor can predict the random seed or only the distribution matters. Does the selected policy remain fixed through later decisions, or is it recomputed? Recomputing with a different model or anchor can produce a different policy, so dynamic consistency cannot simply be assumed.

Finally, the paper argues that functional decision procedures perform well in “fair” problems, where rewards depend on behavior rather than directly on the name of the decision theory. It also acknowledges that fairness is not precisely formalized and that any theory can be punished by a sufficiently tailored problem. Successful examples motivate P-FDT; they do not establish a universal optimality theorem.

## Conclusion

P-FDT treats the output of a decision procedure as a policy and evaluates alternative outputs using a model of their subjunctive consequences. Its distinctive move is to preserve relevant links to predictions, copies, and policy-dependent observations while breaking merely evidential correlations that lack such a mechanism.

Footnote 16 gives the central policy-selection idea, not a complete specification. A reader can apply P-FDT by constructing explicit policy interventions and testing their consequences, but must also make—and disclose—assumptions about dependency, evidence, policy scope, and other agents. Those assumptions are where the theory’s most interesting unresolved problems lie.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, especially §5 and footnotes 7 and 16, [arXiv:1710.05060v2](https://arxiv.org/abs/1710.05060v2).
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/cae4b6d9-f266-4566-b38a-6fefeb3b6799/call_0/request.json)

[Authoritative raw response](../../../../../../runs/cae4b6d9-f266-4566-b38a-6fefeb3b6799/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Deciding on correlation policies**

I need to think through the correlation policies, particularly how to handle different observations made by the same model. It seems like there could be common policy mapping across various names, which might be advantageous. I wonder if using shared output policy could help streamline responses, while independent randomness might introduce weaknesses. I’m considering that a full observation policy could help, but asymmetric approaches could complicate things. Trying to optimize this is key!
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/cae4b6d9-f266-4566-b38a-6fefeb3b6799/call_1/request.json)

[Authoritative raw response](../../../../../../runs/cae4b6d9-f266-4566-b38a-6fefeb3b6799/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Considering policy symmetry**

I’m thinking about how to choose a policy that maintains symmetry. It’s interesting that I could either keep things quiet or disclose information, even when actions differ. I suppose it’s about mapping observations and ensuring tasks remain symmetric. Though the inputs might not be the same, the policy selection could still work if I normalize everything. It feels plausible to cooperate under a shared computation despite the differences.
```
