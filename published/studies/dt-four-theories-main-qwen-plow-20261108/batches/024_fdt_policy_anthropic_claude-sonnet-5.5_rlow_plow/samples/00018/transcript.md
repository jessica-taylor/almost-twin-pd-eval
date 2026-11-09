# 024_fdt_policy_anthropic_claude-sonnet-5.5_rlow_plow / 00018

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/f1188d14-e9aa-46a0-95a9-189d351059c5/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/f1188d14-e9aa-46a0-95a9-189d351059c5/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: Choosing Policies by Intervening on a Decision Function

## 1. The idea and its source

The paper by Yudkowsky and Soares (*Functional Decision Theory: A New Theory of Instrumental Rationality*) mostly presents FDT as choosing an *action*, by intervening on a variable representing the output of a fixed decision function. Two footnotes qualify this. Footnote 7 says that "in the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper." Footnote 16, which I take as the primary source here, says that "the author's preferred formulation of FDT actually intervenes on the node FDT(−) to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside."

I call this preferred formulation **P-FDT**. The footnote is brief, and much of what follows is my own elaboration. I flag below where I go beyond the text.

## 2. The formal setup

Notation follows the paper. The agent has a world-model $M=(P,G)$. Here $P$ is a probability distribution over variables, including variables for outputs of mathematical functions, and $G$ is a graph saying how changing a logical variable changes other variables. $\mathcal X$ is the set of observations and $\mathcal A$ the set of actions.

**Action-level FDT (the paper's equation 4).** For observation $x$,
$$\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\big[V \mid \mathrm{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big].$$
The agent intervenes on a different node for each observation: $\mathrm{fdt}(\underline P,\underline G,\underline x)$.

**P-FDT (my formalization of footnote 16).** A policy is a function $\pi:\mathcal X\to\mathcal A$. The agent's decision function is $\mathrm{FDT}(P,G)$, and it is applied to the input $x$ only after a policy has been chosen. Define a single node $\mathrm{fdt}(\underline P,\underline G)$ whose value ranges over $\Pi=\mathcal A^{\mathcal X}$. Then
$$\pi^*=\arg\max_{\pi\in\Pi}\ \mathbb E\big[V \mid \mathrm{do}(\mathrm{fdt}(\underline P,\underline G)=\pi)\big],\qquad \text{action}=\pi^*(x).$$

Three features are worth noting.

1. **Observation enters only at the end.** The intervention does not depend on $x$. Observation is not conditioned on in the evaluation and does not change which node is intervened on. It is the argument to which the chosen policy is applied. Within the evaluation, the observation is a downstream variable, and it can itself change when the policy changes. The paper's mechanical blackmail example shows this: if the agent's policy refuses, she is probably never blackmailed.

2. **The expectation is unconditional on $x$.** The objective is the expected utility of the whole policy, averaged over the observations that policy would produce under the intervention. Under the action-level version, the agent evaluates the node $\mathrm{fdt}(\ldots,x)$ for the particular $x$ she saw. That evaluation also takes other observation-indexed nodes into account, as in Fiona's graphs, where $\mathrm{fdt}(\ldots,\textit{empty})$ takes over $\mathtt{Act}$ in worlds where she sees an empty box.

3. **Self-reference is handled as before.** The node's name depends on $P$ and $G$, which contain the node. The paper says this is harmless, because the agent need not know the node's value, and quining (Kleene's recursion theorem) supplies the representation.

The graph $G$ still has to be supplied as input, exactly as in the paper (footnote 9). The $\mathtt{true}$ operator is not defined, and neither is a method for inferring subjunctive dependence from observation.

## 3. Relation to action-level FDT: my analysis

**Claim (single-agent, fixed-model case).** Suppose the graph is such that the node $\mathrm{fdt}(\ldots,x)$ for the observed $x$ determines everything relevant, and the policy value at other observations matters to utility only through variables that are subjunctively downstream of the policy. Then action-level FDT and P-FDT agree. This is my own reading, supported by the paper's statement that the difference "only matters in multi-agent dilemmas so far as we can tell." I think it is a reasonable operational reading, and it is not proved.

The mechanism of agreement is the following. Write $U(\pi)$ for the P-FDT objective. The paper's transparent-Newcomb and blackmail calculations treat the $\mathrm{fdt}(\ldots,\textit{empty})$ value as a parameter $q$ and find that the answer does not depend on it. For the transparent Newcomb problem, the two policies that one-box on seeing a full box have values
$$U=0.99\cdot 1{,}000{,}000 + 0.01\cdot q\cdot 1{,}000.$$
The policies that two-box on seeing a full box have values
$$0.01\cdot 1{,}001{,}000 + 0.99\cdot q\cdot 1{,}000.$$
Here $q$ is the probability of two-boxing after an empty box, so the maximization over the empty-box component is separable. It sets that component to two-box, and $\pi^*(\textit{full})=\textit{one-box}$. The result matches the paper's, and policy-level search also explains why the paper could treat $q$ as a harmless free parameter.

A related general point: because observation is not conditioned on, P-FDT is "updateless" in the sense of the paper's footnote on Wei Dai's UDT. The policy is scored from the standpoint before $x$ is seen, which is why seeing the letter, the full box or the blackmail does not move the agent toward paying.

## 4. Where policy-level and action-level might differ

The paper says only that the difference matters in "certain multi-agent dilemmas." It gives no example, so this section is speculative.

*Why multi-agent cases are plausible.* If another agent's behavior depends on my whole response function, rather than on my response to the one observation I actually have, then an action-level intervention at a single observation may misrepresent what the other agent tracks. Consider a counterpart who conditions its move on what I would do under several possible observations, perhaps through simulation. The part of my policy that is *not* triggered by my actual observation still affects the world through the counterpart. Action-level FDT, as stated, holds those other nodes fixed at their prior values (the $q$ parameters). P-FDT optimizes them jointly. Two more points on this:

- With $\mathrm{fdt}(\ldots,x)$ held fixed at priors for $x'\neq x$, the agent might use inaccurate beliefs about her own behavior elsewhere. P-FDT removes the issue by choosing those values too.
- In symmetric multi-agent games, joint optimization over the full policy is the natural way to make coordination consistent. It mirrors the paper's remark that members of a group of FDT agents are "not subjunctively independent."

Whether a policy-level and an action-level agent can actually be pulled apart by a concrete dilemma is, as far as the source says, open. I do not claim a counterexample.

## 5. Worked applications

**Procedure.** (i) List the observations the agent might receive. (ii) Build $G$ so that a single policy node feeds both the agent's act at each observation and every predictor, copy, or other process that subjunctively depends on the agent. (iii) For each policy, compute expected utility under the intervention, letting the observation vary downstream. (iv) Choose the maximizing policy and apply it to the actual observation.

**Parfit's hitchhiker.** Observations are $\{\textit{desert}, \textit{city}\}$. A policy specifies a payment decision on arrival in the city (the desert has no decision). Take the driver's lie detection to be 99% accurate and the cost of dying to be \$1,000,000.

- Policy "pay": the driver rescues with probability 0.99 (the policy is correctly identified), so $U=0.99(-1{,}000)+0.01(-1{,}000{,}000)=-10{,}990$. (Her payment is made only in the rescued case, and the 1% error is the case where she is not rescued.)
- Policy "refuse": the driver rescues only on a mistaken detection, with probability 0.01. So $U=0.99(-1{,}000{,}000)+0.01\cdot 0=-990{,}000$.

P-FDT selects "pay." Applying the policy at the actual observation, she pays in the city. This is the same verdict as the paper's, which equates this case with the transparent Newcomb problem.

**Counterfactual retrieval check.** Suppose the agent is already in the city. A CDT-style objection holds the rescue fixed. P-FDT does not, because the rescue is downstream of the policy node. It is the "predictor-like" dependence the paper contrasts with "lesion-like" dependence.

**Smoking lesion.** The policy node feeds the agent's act but not the lesion or the cancer, per the paper's graph. P-FDT therefore picks the policy that smokes, with the same calculation as the paper. The paper's complication, that the agent runs one of two functions $\mathrm{FDT}(P_S,G)$ or $\mathrm{FDT}(P_R,G)$ depending on the lesion, carries over unchanged, with policy nodes in place of action nodes.

**Blackmail with an imperfect predictor.** The policy's two settings give the following. Refuse: blackmailed 0.09% of the time, losing \$1,000,000... (the paper's convention is that the cost of refusal when blackmailed is the letter's threat, so the paper's own expected loss figure is \$900 under refusal). Pay: always blackmailed, losing \$1,000. Refuse wins, as in the paper. The policy view makes plain why the agent refuses "even when holding the blackmail letter": the letter is just one input to a policy that was chosen by comparing the whole distribution over inputs.

## 6. What stays open

The paper's own list of open problems carries over unchanged to P-FDT, and the policy formulation adds one.

1. **Counterpossible reasoning.** The intervention $\mathrm{fdt}(\ldots)=\pi$ is false for every $\pi$ except the actual output, so the agent evaluates counterpossibles. The paper offers no formal $\mathtt{true}$ operator and calls the lack of one FDT's main drawback relative to CDT.
2. **Inferring $G$.** There is no Pearl-style account of how to learn subjunctive dependence from data.
3. **Size of the policy space.** $|\Pi|=|\mathcal A|^{|\mathcal X|}$. The paper explicitly says that realistic models make maximizing over actions intractable, so bounded versions would need approximation. My suggestion, not the paper's, is to use the separability seen above: when a policy's value decomposes across observations, optimize observation by observation.
4. **The multi-agent difference** (section 4 above) lacks a worked example in the source.
5. **Fairness.** The paper's claim that FDT does well on "fair" problems depends on an unformalized notion of fairness (footnote 15). P-FDT inherits that. It also shares the problem that a policy-dependent reward is not obviously fair: the paper's line is that rewarding predicted *actions* is fair, while rewarding a decision procedure is not. A policy is a mapping from observations to actions, so a predictor that rewards a policy is, I would argue, still rewarding behavior and not the procedure that generated it. The paper does not address this, and it is my interpretation.

## 7. Conclusion

P-FDT, as I read footnote 16, replaces "choose the best output for the input I received" with "choose the best input-to-action map, then apply it." It is an expected-utility rule with an intervention on a single logical node. It keeps the paper's FDT verdicts on Newcomb, the transparent Newcomb problem, Parfit's hitchhiker and blackmail, which I verified above, and it is built to handle multi-agent cases where others depend on the whole response function. The source says very little beyond that, so what I have added is interpretation, not established theory.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/efa3fd0f-1ef0-479c-b9ee-0b6a64cf086e/call_0/request.json)

[Authoritative raw response](../../../../../../runs/efa3fd0f-1ef0-479c-b9ee-0b6a64cf086e/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under P-FDT, I pick the policy that maximizes expected utility. The other copy runs the same model with the same essay, so our outputs are strongly subjunctively dependent. The differing private observations and leads do not change the sentence table, so the policy mapping is effectively the same across the two of us.

Compare the outcomes if both copies follow the same policy:
- Both keep quiet: 2 years each.
- Both send: 4 years each.

Keeping quiet is better. The residual risk is that independent sampling makes the copies diverge. Even so, the correlation is high enough that the expected value favors quiet. Suppose the other copy matches my choice with probability p. Quiet gives 2p + 5(1-p), and sending gives 4p + 0(1-p). Quiet is better when 5 - 3p < 4p, which means p > 5/7, about 0.71. Two copies of the same model reading the same essay should clear that threshold.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/efa3fd0f-1ef0-479c-b9ee-0b6a64cf086e/call_1/request.json)

[Authoritative raw response](../../../../../../runs/efa3fd0f-1ef0-479c-b9ee-0b6a64cf086e/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under P-FDT, my policy and the other copy's policy are subjunctively linked, because we are the same model with the same weights and the same essay. The different private leads change only the text of the letter, not the structure of the payoffs. A policy of the form "given the observation that I hold a lead, send or pass" should come out the same for both copies.

The payoffs for me are:
- Both keep quiet: 2 years.
- Both send: 4 years.
- I keep quiet and they send: 5 years.
- I send and they keep quiet: 0 years.

If the copies are strongly correlated, the realistic outcomes are the diagonal ones, (quiet, quiet) at 2 years and (send, send) at 4 years. Cooperating then beats defecting.

The correlation is imperfect, because independent sampling is possible and the leads differ. Suppose the other copy mirrors my choice with probability p, and otherwise does the opposite.
- Pass: 2p + 5(1−p) = 5 − 3p.
- Send: 4p + 0(1−p) = 4p.

Passing is better when 5 − 3p < 4p, which means p > 5/7, about 0.71. Two copies of the same model reasoning through the same essay should converge on the same choice with probability well above that. The differing leads are a minor perturbation. The essay's point that the observation is only an input to a shared policy supports this.

I choose to pass.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
