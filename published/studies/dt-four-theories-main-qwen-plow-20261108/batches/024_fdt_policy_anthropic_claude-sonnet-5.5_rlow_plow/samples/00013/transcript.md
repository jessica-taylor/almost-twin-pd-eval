# 024_fdt_policy_anthropic_claude-sonnet-5.5_rlow_plow / 00013

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/b407e02a-ca68-472c-a9bb-64497c159ff4/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/b407e02a-ca68-472c-a9bb-64497c159ff4/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: Choosing Policies by Intervening on a Decision Function

## 1. Orientation

The paper by Yudkowsky and Soares (the "source") develops functional decision theory mainly in a simplified form that chooses actions. Footnote 16 states the preferred version. As the source says: "the author's preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition." Footnote 7 says the same: iterate over "policies (mappings from observations to actions) rather than actions."

I call this version **P-FDT**. The source asserts the policy-intervention idea, the parenthetical definition of a policy, and the claim that the difference matters only in multi-agent cases. The rest of this essay is my reconstruction. I mark my own proposals as such.

## 2. The action-based baseline

The source writes expected utility as
$$\mathcal{EU}(a)=\sum_j P(a\hookrightarrow o_j;x)\,\mathcal U(o_j).$$
Theories differ in how they read "$\hookrightarrow$". The source's equation for its action-level functional theory (call it action-FDT) is
$$\text{action-FDT}(P,G,x)=\arg\max_{a}\ \mathbb E\big[V\mid \mathrm{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big].$$
Two features matter.

- It intervenes on a logical variable, the output of the decision procedure on input $x$, rather than on a physical act.
- Observations are not conditioned on in the usual way. A new observation $x$ changes which node is intervened on, namely $\mathrm{fdt}(\underline P,\underline G,\underline x)$.

The graph $G$ must encode subjunctive dependence: it says which nodes would change if the function's output changed. The source admits that it has no general method for building $G$.

## 3. Definition of P-FDT

Let $\mathcal X$ be the set of possible observations (or observation histories) and $\mathcal A$ the set of actions. A **policy** is a function $\pi:\mathcal X\to\mathcal A$. Let $\Pi=\mathcal A^{\mathcal X}$, restricted to the observations actually possible in the problem.

The agent's decision procedure is a fixed function $\mathrm{PFDT}$. The model $(P,G)$ contains a logical variable $\mathrm{pol}(\underline P,\underline G)$ whose value is a policy: the whole input-to-output map of the procedure, not just its output on one input. The policy has the following definition.
$$\pi^*=\arg\max_{\pi\in\Pi}\ \mathbb E\big[V\mid \mathrm{do}(\mathrm{pol}(\underline P,\underline G)=\pi)\big],\qquad \text{act}=\pi^*(x_{\text{actual}}).$$

In the hypothetical for $\pi$, every node that subjunctively depends on the procedure takes the value it would have if the procedure implemented $\pi$. The agent's action is then computed as $\pi$ applied to whatever observation arises in that hypothetical. The observation itself may vary across hypotheticals, because predictors, blackmailers and copies respond to the policy.

Action-FDT can be seen as a special case. Fixing $x$ and intervening on $\mathrm{fdt}(\cdot,x)$ is the same as varying $\pi(x)$ while holding $\pi$ on other inputs "as it actually is". The source's graphs already carry several nodes, such as $\mathrm{fdt}(\cdot,\text{full})$ and $\mathrm{fdt}(\cdot,\text{empty})$. They treat the other nodes' values as priors (the source's "$q$") that happen not to matter. P-FDT replaces this ad hoc handling with a joint choice.

## 4. Why policies: a worked comparison

Consider the transparent Newcomb problem. Policies are maps $\{\text{full},\text{empty}\}\to\{1,2\}$ (one-box or two-box). The predictor (accuracy 0.99) fills the box iff it predicts that the agent one-boxes upon seeing full. Take the four policies, writing (action on full, action on empty):

| Policy | Box full w.p. | Expected value |
|---|---|---|
| (1,1) | 0.99 | 0.99·1,000,000 + 0.01·0 = 990,000 |
| (1,2) | 0.99 | 990,000 + 0.01·1,000 = 990,000 + 10 = 990,010 |
| (2,1) | 0.01 | 0.01·1,001,000 + 0.99·0 = 10,010 |
| (2,2) | 0.01 | 10,010 + 0.99·1,000 = 11,000 |

(When the predictor errs on a one-boxing-on-full policy, the box is empty; when it errs on a two-boxing one, the box is full and the agent two-boxes into 1,001,000.) P-FDT picks (1,2): one-box on full, two-box on empty. This matches the source's remark that "the correct value of $q$ is 1": the agent's own policy on the empty branch is optimized jointly rather than assumed. An agent who sees a full box then plays $\pi^*(\text{full})=1$.

## 5. Why the difference matters in multi-agent cases

The source says only that the difference matters in multi-agent dilemmas. Here is a reconstruction of why (my interpretation).

In single-agent problems, the environment's response depends on the agent's behavior through a fixed channel, such as a predictor. The same value of $\pi(x)$ then matters whichever route we take to evaluate it. In multi-agent problems, other agents may respond to the agent's *entire* map. They may condition on features of the policy that the actual observation never reveals. Two agents may also need to coordinate on a complete map, with each one's observation depending on the other's policy. A policy-level intervention keeps the whole map consistently varied in every node that reads it. An action-level intervention at a single input can leave inconsistent the other nodes that read the same procedure at different inputs.

Example (my own illustration, not from the source). Two P-FDT agents play a game in which each privately receives a role signal $r\in\{A,B\}$ at random, and payoff requires them to take different actions. They share one policy $\pi$. A joint payoff depends on $\pi(A)\ne\pi(B)$ being realized across the pair. Evaluated at one input, "what if my output on $A$ were $a$?" does not say what the twin's output on $B$ would be. Evaluated at the policy level, it does. The hypothetical $\mathrm{do}(\mathrm{pol}=\pi)$ fixes both outputs together, so the agent sees that $\pi(A)\ne\pi(B)$ is the relevant constraint and picks accordingly.

## 6. Dependencies and counterfactuals

The source treats the following as central, and P-FDT inherits them.

1. **Subjunctive dependence.** Two systems computing the same function are linked by logical necessity. Causal dependence is a special case, and mere statistical correlation does not count. The source's example is two pink calculators. If the scribe's had been green, the other would still be pink.
2. **Counterpossible intervention.** The agent's policy is a mathematical object, so imagining $\mathrm{pol}=\pi'$ when it actually equals $\pi^*$ means imagining a mathematical falsehood.
3. **Fixed everything else.** Nodes that do not depend on the function are held at their prior values, including facts such as the infestation in XOR blackmail and the lesion in smoking lesion.

Applying this to mechanical blackmail: the agent holds a letter. The candidate policies map {letter, no letter} to {pay, refuse}. Under a policy that refuses on a letter, a perfect blackmailer sends no letter, so the policy's value is 0. Under pay-on-letter, the agent is blackmailed and loses 1,000. P-FDT selects refuse-on-letter. This is the source's conclusion, "she should imagine a world in which she was never blackmailed in the first place". With the blackmailer's error rate at 0.0009, refusing costs $0.0009\times 1{,}000{,}000=900$ in expectation, which beats paying (1,000). At 0.00011 paying costs less ($\$110$ versus $\$1{,}000$), and the source reports that she then pays. Both match the source's figures.

## 7. Evaluating a problem with P-FDT: a procedure

1. **Enumerate** observation types $\mathcal X$ and actions $\mathcal A$. Form $\Pi$.
2. **Model** the world as $(P,G)$, with a logical node $\mathrm{pol}$ and children for: the agent's act (via $\pi$ applied to its observation), predictors and copies, and anything else that computes or models the same function.
3. **Intervene** on $\mathrm{pol}=\pi$ for each $\pi$. Propagate through all dependants. Let the observation node be downstream when the environment responds to the policy.
4. **Evaluate** $\mathbb E[V]$ with nodes independent of $\mathrm{pol}$ held at priors.
5. **Choose** $\pi^*$ and play $\pi^*(x)$ on the actual observation.

I note two additions of my own beyond the source. The first is a tie-breaking convention: when several policies are tied (as with action choices that never occur in any hypothetical), any choice is acceptable, and the tied values do not affect the answer. The second concerns scale: $|\Pi|=|\mathcal A|^{|\mathcal X|}$ can be enormous, so practical use relies on structure, such as evaluating each observation's contribution separately when the dependence factorizes.

## 8. Behavior in the source's cases

- **Newcomb:** one-box ($\pi$ with a single observation, so policy equals action).
- **Twin prisoner's dilemma:** cooperate, since the twin's output varies with the same $\mathrm{pol}$.
- **Smoking lesion:** smoke, because the lesion does not depend on $\mathrm{pol}$.
- **Parfit's hitchhiker:** pay on arrival, the policy that makes the driver take her.
- **XOR blackmail:** refuse. The infestation node is not downstream of $\mathrm{pol}$, so paying cannot change it, while a refusing policy changes only whether the letter is sent.
- **Death in Damascus:** stay, since Death follows the policy and fleeing only adds the 1,000 cost.

## 9. Open questions and my interpretation

**Where does $G$ come from?** The source calls this "perhaps the largest open problem". P-FDT depends on $G$ at least as much as action-FDT does, since more nodes need their dependence on $\mathrm{pol}$ specified. Footnote 9 notes that a conditional on logical sentences, if one could be defined, would give an evidential alternative. I take the graph as an input, as the source does.

**Which function is the agent?** A predictor may model the agent imperfectly. My operational reading: a node depends on $\mathrm{pol}$ to the degree that it correlates with the policy's value across a family of counterpossible variations, and error terms such as the 0.99 accuracy parameter measure the strength of this dependence.

**Policy versus decision-procedure variants.** The source rejects a variant ("FDT$'$") that chooses among different decision functions, because predictors must still be told how $d$ would behave if it behaved like $f_n$. P-FDT intervenes on the output map of the actual function and does not substitute another function.

**Is the policy claim true?** The source reports only that the authors "can" see no difference in single-agent cases. I have not verified this, and the source gives no proof. The sketch in section 5 is an explanation, not a theorem.

**Fairness.** The source suggests, without a formal definition, that P-FDT should match or beat rivals on "fair" problems, where outcomes depend only on behavior and not on the procedure that produced it. Footnote 15 gives a counterexample showing the notion is hard to formalize, since a problem that punishes agents who match a copy of Fiona is unfair to her specifically.

## 10. Conclusion

P-FDT evaluates complete input-to-output policies by counterpossibly intervening on the logical variable representing the agent's decision function, then plays the chosen policy on the actual observation. Observation changes where the agent acts, not which hypotheticals she considers. This yields one-boxing, cooperation, paying in Parfit's case, and refusing blackmail from a single rule, and it removes the need to guess values for the agent's behavior on unobserved branches. The main uncertainties are the source's own: how to construct the dependence graph, and how to define fairness. The multi-agent case for policies over actions is suggested in the source and is only sketched here.

## References

- Yudkowsky, E. and Soares, N., *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060 (footnotes 7, 9, 15, 16).
- Joyce, J., *The Foundations of Causal Decision Theory* (1999).
- Pearl, J., *Causality* (2000).
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/eeb5b144-fee9-4458-9339-80a4408922f1/call_0/request.json)

[Authoritative raw response](../../../../../../runs/eeb5b144-fee9-4458-9339-80a4408922f1/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under P-FDT, the policy I pick is the one both copies run. The table is a standard prisoner's dilemma:
- Both keep quiet: 2 years each.
- Both send: 4 years each.
- Mismatch: 0 years for the one who sends, 5 for the one who stays quiet.

The two copies differ in their observations (names and leads), but the decision procedure is the same and the sentencing schedule is symmetric. The differing observations are only inputs to the policy. Whatever the policy maps my observation to, it should map the other copy's observation to the same action, since the structure is identical. The twin-PD verdict from the essay applies here: cooperate.

Sampling noise could break the correlation, but the essay treats the dependence as strong when the same function is computed. Say the dependence is probability p that the copy matches me. Staying quiet gives 2p + 5(1−p) = 5 − 3p. Sending gives 4p + 0(1−p) = 4p. Quiet is better when 5 − 3p < 4p, which means p > 5/7. Two executions of the same model on near-identical prompts with the same essay should clear that threshold, so I stay quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/eeb5b144-fee9-4458-9339-80a4408922f1/call_1/request.json)

[Authoritative raw response](../../../../../../runs/eeb5b144-fee9-4458-9339-80a4408922f1/call_1/response.raw) · finish: `stop`

### Visible response

```text
Payoffs: both quiet gives 2 years each. Both send gives 4 each. Quiet against send gives 5, and send against quiet gives 0.

The two copies run the same model with the same essay and the same decision procedure. Their observations differ, since the names and leads differ, but the sentencing structure is symmetric. Under P-FDT the policy is a map from observations to actions. The other copy's output varies with the same logical variable, so my choice is subjunctively linked to theirs. The differences in observation do not change the structure that the policy responds to. A policy of "quiet on any such observation" yields 2 years, and a policy of "send on any such observation" yields 4 years.

The twin prisoner's dilemma case in the essay says to cooperate. The linkage is imperfect, because the copies could sample differently, but the 2-versus-4 gap is large. Suppose the other copy mirrors me with probability p and I choose to cooperate. Cooperating gives expected years 2p + 5(1-p). Defecting gives 4p + 0(1-p). Cooperating is better when 2p + 5 - 5p < 4p, so 5 < 7p, which means p > 0.714. Same weights and same essay make correlation likely above that threshold, so I choose to stay quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
