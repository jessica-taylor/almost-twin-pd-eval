# 024_fdt_policy_anthropic_claude-sonnet-5.5_rlow_plow / 00006

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/ae8d6020-4188-42ab-ab71-ae6afa2ed9f1/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/ae8d6020-4188-42ab-ab71-ae6afa2ed9f1/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: Choosing Policies by Intervening on a Decision Function

## 1. Orientation and sources

The paper "Functional Decision Theory" (Yudkowsky and Soares) mostly presents a simplified version of its theory that selects *actions*. Two footnotes say the authors' "preferred formalization" is different. Footnote 16 states: "the author's preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition." Footnote 7 makes a similar remark: agents "iterate over *policies* (mappings from observations to actions) rather than actions."

I call this policy-selecting version **P-FDT**. Everything the paper says about it is in those two footnotes. The rest of this essay is my reconstruction, built from the paper's action-level machinery. I mark which claims come from the source and which are mine.

## 2. The action-level theory that P-FDT modifies

The paper treats the theories as expected-utility maximizers that differ in how they build "hypotheticals". For FDT (Eq. 4):

$$\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\big[V \mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big].$$

Here $(P,G)$ is a probability model together with a graph of "subjunctive dependence". The variable $\mathrm{fdt}(\underline P,\underline G,\underline x)$ stands for the output of the decision function on this model and this observation. The $\mathtt{do}$ operator is Pearl's surgery. Observation does not enter by conditioning. Instead it changes *which* node is intervened on. In the transparent Newcomb problem, for example, the agent who sees a full box intervenes on $\mathrm{fdt}(\cdot,\text{full})$. The node $\mathrm{fdt}(\cdot,\text{empty})$ is left to govern the world where the box is empty.

This already looks policy-like. The model contains one node per possible observation, and the agent's action in the world is determined by whichever node matches the observation that world delivers. The source's Figure for transparent Newcomb has $\textsc{Act}$ depending on both $\mathrm{fdt}(\cdot,\text{full})$ and $\mathrm{fdt}(\cdot,\text{empty})$, with $\textsc{Prediction}$ selecting which one applies.

## 3. Definition of P-FDT (my formalization)

The footnote implies the following. Let $\mathcal X$ be the set of observations and $\mathcal A$ the set of actions. A **policy** is a function $\pi:\mathcal X\to\mathcal A$, and $\Pi=\mathcal A^{\mathcal X}$. The agent's decision function $d$ takes the model $(P,G)$ and returns a whole policy:

$$d(P,G)=\pi^*\in\arg\max_{\pi\in\Pi}\ \mathbb E\big[V\mid \mathtt{do}\big(\mathrm{fdt}(\underline P,\underline G)=\pi\big)\big].$$

Then $\pi^*$ is applied to the actual observation $x$, giving the action $\pi^*(x)$.

Three features matter.

1. The intervened node is now a single node $\Phi=\mathrm{fdt}(\underline P,\underline G)$ with values in $\Pi$. It does not depend on $x$. A node $\mathrm{fdt}(\cdot,x)$ for each $x$ is no longer needed, since $\Phi(x)$ plays that role.
2. Observation affects the choice only at the final step, when the policy is applied. It does not affect which policy is chosen. This is the strongest sense in which P-FDT is "updateless". The source says the action-level version responds to observation by changing the intervention point. Under P-FDT the intervention point is fixed, and the observation selects a component of the chosen object.
3. The downstream model is defined by structural equations in which each variable that a predictor, twin or copy computes from the agent's decision function reads $\Phi$ or some evaluation of it. Where a variable is influenced by $\Phi(x')$ for an observation $x'$ that did not occur, $\Phi$ still enters through the other-branch structure. This is the "different observations in the counterfactual" feature the source stresses ("if their action were different, they might have *made different observations*").

The objective is the expected utility of the whole policy, taken over the model's distribution of observations *under that intervention*:

$$\mathcal{EU}(\pi)=\sum_{x}\ \sum_{o}\ P\big(X=x,\ O=o\mid \mathtt{do}(\Phi=\pi)\big)\,U(o).$$

The distribution over $X$ is itself allowed to depend on $\pi$, because predictors can condition on $\pi$.

## 4. How the definition behaves

**Newcomb (no observation).** $\mathcal X$ is trivial, so policies are actions and P-FDT coincides with FDT. With the source's 99% accuracy, $\mathcal{EU}(\text{one-box})=0.99\cdot 10^6=\$990{,}000$ and $\mathcal{EU}(\text{two-box})=0.01\cdot1{,}001{,}000+0.99\cdot1000=\$11{,}000$ (the source writes the latter as $\$11{,}000$). The agent one-boxes.

**Transparent Newcomb.** $\mathcal X=\{\text{full},\text{empty}\}$. Four policies: $(\text{full}\mapsto a,\ \text{empty}\mapsto b)$. Take the predictor to fill the box iff $\Phi(\text{full})=$ one-box, with accuracy 0.99. Then:

| policy (full, empty) | expected utility |
|---|---|
| (one, one) | $0.99\cdot 10^6 + 0.01\cdot 0=\$990{,}000$ |
| (one, two) | $0.99\cdot10^6+0.01\cdot1000=\$990{,}100$ |
| (two, one) | $0.01\cdot 0.\!\!\;$ see note |
| (two, two) | $0.99\cdot1000+0.01\cdot1{,}001{,}000=\$11{,}000$ |

Note on row three: with probability 0.99 the box is empty and the agent plays "one" for $\$0$, and with probability 0.01 it is full and she plays "two" for $\$1{,}001{,}000$, giving $\$10{,}010$. The best policy is (one, two): one-box on seeing a full box, two-box on seeing an empty one. This matches the source's remark that the correct $q$ for the empty branch is 1. P-FDT does not need a probabilistic guess about the other branch's behavior, because it optimizes over both branches jointly. The source treats the other branch as a prior parameter $q$ that "doesn't matter". In P-FDT it is the second coordinate of the maximization.

**Parfit's hitchhiker and mechanical blackmail.** These work the same way. The policy "pay if in the city" is evaluated together with its effect on whether the driver picks her up. Likewise "refuse if blackmailed" is evaluated with its effect on whether the letter is sent. The source's numbers for imperfect blackmailers (error rate 0.0009: refuse, since expected loss is about \$900 versus \$1,000; error rate 0.011%: pay) come out as comparisons of policy values.

**Single-agent problems with no dependence.** If nothing in the world depends on $\Phi$ except the agent's own action, then $\mathcal{EU}(\pi)=\sum_x P(x)\,\mathbb E[V\mid x,\mathtt{do}(a=\pi(x))]$. This is maximized pointwise, by choosing the best action for each observation. So P-FDT agrees with action-level FDT, CDT and EDT in simple settings, as the source says of FDT.

## 5. Where policy and action versions come apart

The source says only that the difference "only matters in multi-agent dilemmas so far as we can tell". I can say how this could happen.

In single-agent problems the source works with, the observation is fixed by the world and the intervention affects it through predictors. The action-level theory handles this by choosing, for the observed $x$, the value of $\mathrm{fdt}(\cdot,x)$ and treating the values at other $x'$ as fixed parameters ($q$ in the source). The policy theory optimizes all of them jointly. These differ when the optimal value at $x$ depends on what is done at $x'$ *and* the agent at $x'$ is a copy or predicted counterpart whose behavior at $x'$ is not a free parameter.

Suppose two agents run the same function, receive different observations (say, roles), and payoffs depend on the pair of actions. The action-level equation intervenes at $\mathrm{fdt}(\cdot,x_1)$ for one agent, but the twin's action is governed by $\mathrm{fdt}(\cdot,x_2)$, a different node. The surgery then leaves the twin's action fixed. The policy version intervenes on the single node $\Phi$, which both agents apply, so the twin's action moves in the counterfactual. That is the sense in which joint optimization matters. It lets a symmetric coordination problem with asymmetric roles be solved as one optimization over $\Phi$.

This is my interpretation of why the footnote's remark about multi-agent dilemmas is plausible. The source does not give this argument.

## 6. Open questions and my proposals

**Subjunctive-dependence graph.** The source says that deducing the structure of subjunctive dependence from observation is "perhaps the largest open problem". P-FDT inherits it unchanged. It still requires $(P,G)$ as an input. P-FDT only changes what is intervened on.

**Size of the policy space.** $|\Pi|=|\mathcal A|^{|\mathcal X|}$ is exponential. The source acknowledges idealization and expects "bounded versions" to behave similarly. A reasonable operational reading is to optimize only over policies that factor through coarse features of the observation. I flag that as my own suggestion.

**Observations the model gives probability zero.** The policy value $\mathcal{EU}(\pi)$ does not depend on $\pi(x)$ for observations $x$ that have probability zero under $\mathtt{do}(\Phi=\pi)$. Ties then occur. I suggest a lexicographic tiebreak: evaluate the final action on the actual observation under the same $\mathcal{EU}$, treating the model's prior distribution over observations as a tie-breaker for the unreachable branches. The source says nothing on this.

**Observations that the agent has actually made, but that her model of the policy deems unlikely.** The transparent Newcomb case is exactly this. P-FDT follows the policy even though the realized branch is "improbable" under its own choice. The source defends the analogous behavior ("it's advantageous to be *the kind of agent* that makes such decisions"). That is the same behavior, now built in rather than recovered by changing the intervention point.

**Evidential versus intervention reading.** Footnote 9 notes a possible "evidential version" with conditioning on logical facts, but says no formal definition of conditioning on false logical sentences exists. I use the $\mathtt{do}$ reading throughout, as the source does.

**Fairness.** The source claims FDT does well in "fair" problems, where outcomes depend on the agent's behavior and not directly on her decision procedure. Footnote 15 shows that formalizing this is hard: punishing anyone who matches a copy of Fiona is unfair to her but not to others. P-FDT inherits that limitation. In particular a problem that rewards a particular *policy* is fair in the paper's sense only if the reward depends on the input-output behavior and not on how it is computed. Policies are by definition extensional, which fits this restriction nicely, though the source does not make the point.

## 7. How to use P-FDT on an unfamiliar case

1. List the observations $\mathcal X$ the agent might receive and the actions available.
2. Draw the dependence graph with a single node $\Phi$. Attach to $\Phi$ the agent's own action, every predictor or copy that models her, and anything that conditions on her possible observations.
3. Write each outcome as a function of $\Phi$ and the exogenous noise (predictor accuracy, luck).
4. For each policy, compute $\mathcal{EU}(\pi)$ under $\mathtt{do}(\Phi=\pi)$, including the probability of each observation.
5. Choose $\pi^*$ and play $\pi^*(x)$ for the observation actually received.

For the smoking lesion, the lesion is not downstream of $\Phi$ and so the policy "smoke" wins. For XOR blackmail, the letter's existence depends on $\Phi(\text{letter})$ but the termites do not. Policy "refuse" makes the letter come only when termites are present, but termites are unchanged, so refusing avoids the \$1,000 payment and wins.

## 8. Conclusion

The source specifies P-FDT only by a footnote: intervene on the decision-function node to select a policy, then apply it to the observation. I have read that as joint maximization of expected utility over input-output mappings with a single intervention point, which agrees with action-level FDT where there is a single decision and no dependence on other inputs. It shifts the treatment of unobserved branches from fixed parameters to variables being optimized, and it plausibly matters when copies or predictors respond to the agent's behavior under different inputs. All the open problems the source lists, dependence-graph construction, counterpossibles and fairness, remain.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/0e4f85d8-c013-4aae-b83e-59607823bb8d/call_0/request.json)

[Authoritative raw response](../../../../../../runs/0e4f85d8-c013-4aae-b83e-59607823bb8d/call_0/response.raw) · finish: `stop`

### Visible response

```text
Reasoning under P-FDT: the two copies run the same decision function, so the policy I choose is effectively the policy the other copy applies. The observations differ (names, leads), but the policy can ignore those details, and the payoffs are symmetric.

If both copies keep quiet, each gets 2 years. If both send, each gets 4 years. Mixed outcomes aren't reachable if the policy is shared, since the chosen policy fixes both actions. The best joint outcome is mutual silence at 2 years against 4 for mutual sending.

The essay admits that independent sampling could produce divergence. Even so, the policy-level evaluation favors "pass" for any reasonable correlation between the copies. With correlation p that the other copy matches me, quiet gives 2p + 5(1-p) and sending gives 4p + 0(1-p). Quiet is better when 5 - 3p < 4p, which means p > 5/7. Same weights and the same essay make the copies' outputs highly correlated, so p is above that threshold.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/0e4f85d8-c013-4aae-b83e-59607823bb8d/call_1/request.json)

[Authoritative raw response](../../../../../../runs/0e4f85d8-c013-4aae-b83e-59607823bb8d/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under P-FDT the choice is a policy applied to my observation, and the other copy runs the same policy function on its own observation. The two observations differ in names and leads, but the policy is a single node, so the copy's action moves with mine under the intervention. The payoff table is symmetric.

The only question is whether the policy maps both observations to the same action. A policy that depends on surface features such as the names would be unnatural. The essay's idea of coarse-feature policies points to "cooperate-type" versus "defect-type" policies.

Outcomes if both copies play the same action:
- Both keep quiet: 2 years each.
- Both send: 4 years each.

Mutual quiet is better, so if the copies correlate perfectly, passing wins.

The uncertainty is that independent sampling could break the correlation. Suppose the probability that the copy matches my action is p. Then:
- Quiet: 2p + 5(1−p) = 5 − 3p.
- Send: 0·p + 4(1−p)... wait, with the copy quiet, send gives 0, and with the copy sending, it gives 4. If the copy matches me, send gives 4. If it doesn't match, I send and the copy is quiet, which gives 0. So send = 4p + 0(1−p) = 4p.

Quiet is better when 5 − 3p < 4p, which means p > 5/7, about 0.71. The two copies share the same model, weights, essay and a nearly identical situation, so I expect the match probability to be well above that. Passing is the right choice.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
