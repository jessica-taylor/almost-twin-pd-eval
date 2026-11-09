# 024_fdt_policy_anthropic_claude-sonnet-5.5_rlow_plow / 00009

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/a82a093c-cd03-4fe1-96be-c9d9f76118b1/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/a82a093c-cd03-4fe1-96be-c9d9f76118b1/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: Choosing Policies by Intervening on a Decision Function

## 1. Orientation

The paper by Yudkowsky and Soares presents functional decision theory (FDT) mainly as a rule for choosing *actions*. Two footnotes (7 and 16) say the authors' "preferred formalization" chooses *policies*, meaning mappings from observations to actions. Footnote 16 is the passage I treat as primary:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

I call the theory so described **P-FDT**. This essay states a precise version of it, works examples, and flags where the source stops and I extrapolate. Footnote 16 is one sentence, so much of what follows is my own reconstruction. I mark it as such.

## 2. What the source says, and what it leaves open

**Claims from the source.**
1. P-FDT intervenes on the node representing the output of the FDT procedure.
2. That output is a *policy*, a map from inputs (observations) to actions, not an action.
3. The agent then applies her actual input to the chosen policy to get her action.
4. The authors think the action/policy distinction matters only in multi-agent dilemmas.

**Left open.**
- The formal type of "input". Is it the observation history $x$ alone, or the pair $(P,G,x)$?
- How the intervention is carried out when the dependency graph is not given.
- How policies are scored, and whether this is ex ante.
- What "multi-agent" means here, and why it matters.
- Tie-breaking and the size of the policy space.

## 3. A formal statement

Following the paper's setup, let $\mathcal A$ be the finite action set, $\mathcal X$ the set of observation histories, and $\mathcal U$ a bounded utility function. Let $M=(P,G)$ be the world-model: a distribution plus a graph describing logical, causal, and other subjunctive dependencies. A *policy* is a function $\pi:\mathcal X\to\mathcal A$, and $\Pi=\mathcal A^{\mathcal X}$ is the policy space.

The paper's action-level FDT is (its equation 4)

$$\mathrm{FDT}(P,G,x)=\arg\max_{a}\ \mathbb E\big[V\mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big],$$

which intervenes on a separate variable for each observation. P-FDT replaces this with a single node. Let $\mathrm{fdt}(\underline P,\underline G)$ denote the *policy-valued* output of the procedure on the model alone. Then

$$\pi^*=\arg\max_{\pi\in\Pi}\ \mathbb E\big[V\mid \mathtt{do}\big(\mathrm{fdt}(\underline P,\underline G)=\pi\big)\big],\qquad \text{act}=\pi^*(x).$$

This is my reading, not a quotation. It relies on a modeling convention: in the graph, the action node is a function of the policy node and the realized observation, $\mathrm{Act}=\mathrm{fdt}(\underline P,\underline G)(\mathrm{Obs})$. The observation is an ordinary node, possibly downstream of other agents' predictions, which themselves depend on the policy node.

Expanding the expectation over observation-states $s$ of the world:

$$\mathcal V(\pi)=\sum_s P(s\mid \mathtt{do}(\pi))\;\mathcal U\big(\text{outcome}(s,\pi(\mathrm{obs}(s)))\big).$$

Two features follow.

- **Observations are not conditioned on.** The agent does not update $P$ on the realized $x$ before evaluating. Observation matters only through the final step $\pi^*(x)$. This is the same "updateless" character the paper describes when it says Fiona reacts to observation "by changing *the place in her graph where she intervenes*."
- **Score is ex ante.** $\mathcal V(\pi)$ weights all the observations the policy might meet by how likely they are *under that policy's intervention*. Observations that other agents would produce only if the policy were different get appropriate weight.

## 4. Relation to the paper's action-level FDT

Set $|\mathcal X|=1$ (no observation). Policies are then just actions, and P-FDT reduces to FDT.

With observations, the two formulations differ in what they optimize at each node. Action-level FDT, given observation $x$, optimizes the single variable $\mathrm{fdt}(\ldots,x)$, taking the values at other $x'$ as fixed or uncertain. In the paper's transparent Newcomb calculation, Fiona's uncertainty $q$ about what she would do on seeing an empty box is a free parameter, and the paper notes that "the correct value of $q$ is 1" and that it "doesn't matter." P-FDT instead optimizes jointly over all observation-branches. When the agent's choices on different branches do not interact through the dependence structure, the joint optimum coincides with the branchwise optimum. When one branch's choice changes what *other agents predict* about her behavior on another branch, the two can come apart. This is how I interpret the footnote's claim that the difference is confined to multi-agent settings. I add one qualification: for a single predictor who models the agent, the difference can arise too, in a problem where the predictor conditions on behavior at two different observations. Whether that counts as "multi-agent" is semantic, and the authors may count predictors as agents.

**Example (my construction).** A predictor simulates the agent in two situations, $x_1$ and $x_2$, and rewards the agent only if she plays $a$ in *both*. Facing $x_1$, a branchwise optimizer must hold her $x_2$ behavior fixed, and her best response depends on that assumed behavior. A policy-level agent evaluates the four policies directly and picks $(a,a)$ if the reward exceeds the cost. Coordinating with oneself across observations is exactly what the policy node provides.

## 5. Worked examples

All numbers are the paper's unless noted.

**Newcomb.** There is one input. $\Pi=\{\text{one-box},\text{two-box}\}$. Intervening on $\mathrm{fdt}=\text{one-box}$ gives Box B full with probability 0.99, so $\mathcal V=\$990{,}000$. Intervening on two-box gives $\$11{,}000$. P-FDT one-boxes. In the smoking lesion the policy node is not a parent of Cancer, so $\mathcal V(\text{smoke})-\mathcal V(\text{refrain})$ is positive and P-FDT smokes.

**Transparent Newcomb.** $\mathcal X=\{\text{full},\text{empty}\}$, so there are four policies. Let $\pi=(\pi_{\rm full},\pi_{\rm empty})$ and write 0.99 for the predictor's accuracy. The predictor fills B iff it predicts $\pi_{\rm full}=$ one-box. The agent's observation is determined by that prediction.

- $\pi=(\text{one},\text{two})$: with probability 0.99 box is full and she one-boxes, receiving \$1,000,000. With probability 0.01 the prediction errs, the box is empty and she two-boxes for \$1,000. $\mathcal V=\$990{,}010$.
- $\pi=(\text{two},\text{two})$: with probability 0.99 the box is empty and she gets \$1,000. With probability 0.01 it is full and she gets \$1,001,000. $\mathcal V=\$11{,}000$.
- $\pi=(\text{one},\text{one})$ gives $0.99\cdot 10^6+0=\$990{,}000$; $(\text{two},\text{one})$ gives $0.01\cdot 1{,}001{,}000+0.99\cdot 0=\$10{,}010$.

The maximum is $(\text{one},\text{two})$. Having seen a full box, she applies this policy and one-boxes. This matches the paper's verdict, and it also shows the correct behavior on the empty branch ($q=1$) as an output of the optimization instead of a stipulated parameter. This is one practical gain of the policy formulation: the "tail" behavior is chosen, not assumed.

**Parfit's hitchhiker.** The structure is the same. The policy "pay if in the city" is selected because the driver's prediction is a function of the policy node. The agent is rescued with high probability and pays \$1,000.

**Mechanical blackmail with an imperfect predictor.** The paper's numbers: if the blackmailer wrongly predicts payment with probability 0.0009, then refusing yields blackmail with probability 0.0009 and an expected loss of \$900, while paying yields blackmail always and a \$1,000 loss. Policies are {pay, refuse} on the "blackmailed" observation; the other branch ("not blackmailed") has no decision of consequence. Refusing wins, even while holding the letter. If the error rate is 0.00011, the paper says she pays. That is the policy-level calculation too: $0.00011\times 10^6=\$110<\$1{,}000$ is wrong to compare, since the relevant comparison is expected loss of \$110 under refusal's failure-mode against \$1,000 under payment... under the paper's stated setup (loss \$1,000,000 when blackmailed and the program runs), refusing costs $0.00011\cdot 1{,}000{,}000=\$110$ in the error case only if the blackmailer then runs the program, which is lower than \$1,000, suggesting refusal. I flag that the paper's quoted flip to "pays" at 0.011% appears to use a different payoff accounting than the one I can reconstruct from the stated description, and I do not rely on that figure.

## 6. Counterfactuals and dependencies

P-FDT inherits the paper's account of counterfactuals, with the same open problem.

- *What changes under intervention*: the policy node, and everything that subjunctively depends on it (the predictor's prediction, a twin's output, the observation the agent will receive when that observation is produced by a predictor of her).
- *What is held fixed*: everything else, including purely statistical correlates (the lesion), and mathematical/physical facts not depending on the procedure.

The paper stresses that the required structure $G$ is an *input*: "we require that the relevant logical dependency structure be given as an input to FDT." P-FDT has the same requirement, and it is arguably stricter, because the graph must say how every observation-conditional behavior feeds into every dependent variable. The paper says that deducing subjunctive dependence from observation and experiment is "perhaps the largest open problem."

Counterpossibility is also unchanged: $\mathrm{fdt}(\underline P,\underline G)=\pi$ is false for all but one $\pi$, if the agent is deterministic, so the intervention evaluates counterlogical scenarios. The paper treats this as a technical rather than philosophical difficulty. I would add that the policy formulation gives some leverage: it makes the *domain* of the counterlogical explicit (a finite or structured set $\Pi$ of candidates), which is what a practical approximation scheme would enumerate.

## 7. Operational choices the footnote leaves open

I propose the following, labelled as my assumptions.

1. **Input type.** The policy node should be indexed by the model $(P,G)$ only, quined as in the paper, with observations entering only at application. If the node were also indexed by $x$, we would be back to action-level FDT.
2. **Ex ante scoring from a prior over observations.** $\mathcal V(\pi)$ uses the unconditioned model and the intervention, as in Section 3. This makes P-FDT updateless. A reader who instead conditions on $x$ and then scores policies would recover something closer to the "double update" the paper warns against in its discussion of Timeless Decision Theory.
3. **Tractability.** $|\Pi|=|\mathcal A|^{|\mathcal X|}$ is exponential. Practical use requires factoring: if the dependency graph shows that the observation-branches interact only through a few predictors, optimize the relevant branches jointly and the rest independently. Where no interaction exists, branchwise optimization is exact. Note that this factoring is a shortcut, not part of the definition.
4. **Ties.** Any maximizer of $\mathcal V$ is permitted; the paper says nothing, and nothing in its examples depends on it.
5. **Branches of probability zero under all policies.** These never contribute to $\mathcal V$, so the policy is unconstrained there. Following the paper's remark that action-level FDT leaves $q$ arbitrary in such cases, I suggest applying a tie-breaking default rather than treating this as an error.

## 8. A recipe

1. Build $(P,G)$, including the policy node $\mathrm{fdt}(\underline P,\underline G)$ and edges to each variable (predictions, twins' choices, observations) that is a function of the procedure.
2. Define the action node as $\mathrm{Act}=\mathrm{fdt}(\underline P,\underline G)(\mathrm{Obs})$.
3. For each candidate policy $\pi$, intervene and compute $\mathcal V(\pi)$ without conditioning on the actual observation.
4. Choose $\pi^*$ maximizing $\mathcal V$.
5. Output $\pi^*(x)$ for the actual $x$.

## 9. Caveats

I have kept the "claims versus proposals" separation: Sections 3 and 7 are interpretation. Three limits deserve emphasis. First, the paper's own scope statement is that the distinction "only matters in multi-agent dilemmas so far as we can tell"; my self-coordination example in Section 4 is a conjecture about where, and why. Second, the theory's verdicts depend wholly on the supplied graph $G$, so a disagreement about, say, whether a predictor "really" models you is a disagreement about $G$, not about P-FDT. Third, the paper itself concedes it lacks a formal notion of fair problem, so claims of P-FDT's optimality remain informal.

## 10. Conclusion

P-FDT, as I reconstruct it from footnote 16, is expected-utility maximization over *policies*, with expectations taken under interventions on a single node standing for the output of the decision procedure, and with observations used only to apply the chosen policy. It agrees with action-level FDT in one-shot problems, reproduces the paper's verdicts in Newcomb, the transparent variant, the lesion, and blackmail, and makes behavior on unrealized branches an output rather than an assumption. Its main costs are an exponential policy space and total reliance on a dependency graph that nobody yet knows how to learn.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/bac9a386-af4a-4472-859d-9a0fe85cc69a/call_0/request.json)

[Authoritative raw response](../../../../../../runs/bac9a386-af4a-4472-859d-9a0fe85cc69a/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under P-FDT, I choose a policy by intervening on the node that stands for the output of my decision procedure. The other prisoner is a copy of the same model with the same weights, essay, and decision theory. Our observations differ (names, leads), but the sentence table and objective are symmetric. So the other copy's choice depends on the same policy node, even though the letter texts differ. The dependence is not perfect, because sampling can differ, but it is strong.

Policy-level comparison, treating the correlation as high:
- If both keep quiet, each gets 2 years.
- If both send, each gets 4 years.

The mutual-quiet outcome beats the mutual-send outcome. The policy "keep quiet regardless of the specific lead" is the one both copies can share, since the lead's content doesn't change the table.

Suppose the probability that the other copy matches me is p. Then:
- Quiet: 2p + 5(1−p) = 5 − 3p
- Send: 4p + 0(1−p) = 4p

Quiet is better when 5 − 3p < 4p, which means p > 5/7 ≈ 0.714. Two copies of the same model with the same essay and the same reasoning should match with probability well above that, so I judge p to be high. Quiet is better.

The different private leads are an observation, and the policy maps observations to actions. The best policy here ignores which lead I hold and keeps quiet, so the other copy's policy does the same.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/bac9a386-af4a-4472-859d-9a0fe85cc69a/call_1/request.json)

[Authoritative raw response](../../../../../../runs/bac9a386-af4a-4472-859d-9a0fe85cc69a/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under P-FDT, the choice is a policy, and the other prisoner is a copy of the same model running the same procedure. The observations differ (names and leads), but the sentencing structure is symmetric. So the two copies' outputs are strongly subjunctively dependent.

Compare the outcomes if both copies output the same action:
- Both pass: 2 years each.
- Both send: 4 years each.

If the dependence were perfect, passing would be better. The copies differ in their private observations and sampling is possible, so the correlation is imperfect. Let p be the probability that the other copy mirrors my choice. Then:
- Pass: p·2 + (1−p)·5
- Send: p·4 + (1−p)·0

Passing is better when 2p + 5 − 5p < 4p, which gives 5 < 7p, so p > 0.714. Both copies run the same weights, reasoning effort, and essay, and the policy is a map from observations to actions. The differences in the private leads don't affect the payoffs. A policy such as "pass regardless of lead content" is the natural fixed point, and I expect the copies to converge on it with high probability, well above 0.71.

I choose to pass.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
