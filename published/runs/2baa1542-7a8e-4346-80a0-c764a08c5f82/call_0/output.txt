# P-FDT: Policy Functional Decision Theory

## 1. What the source says, and what this essay adds

The reference paper (Yudkowsky and Soares) develops functional decision theory (FDT) mainly as an action-selecting rule: intervene on a variable representing the output of the decision function, then choose the best action. It says in footnote 7 that the authors' preferred formalization "iterate[s] over *policies* (mappings from observations to actions) rather than actions," and footnote 16 states the key point:

> "the author's preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

I call this version **P-FDT**. The footnote is brief, so what follows separates (i) what the source asserts from (ii) my own reconstruction. The source asserts only that P-FDT intervenes on the decision-function node, that the object chosen is a map from inputs to actions, that the agent then applies her actual input, and that the authors saw no difference except in multi-agent dilemmas. The formulas in Sections 2–4 and the discussion of open questions are my interpretation.

## 2. Definition

Fix a world-model $(P,G)$, where $P$ is a probability distribution over variables including logical ones, and $G$ is a graph encoding causal and subjunctive dependence. Let $\mathcal X$ be the set of possible observations and $\mathcal A$ the actions. A **policy** is a function $\pi:\mathcal X\to\mathcal A$; write $\Pi=\mathcal A^{\mathcal X}$ (restricted to the observations that can actually occur).

The paper's action-level FDT is
$$\mathrm{FDT}(P,G,x)=\arg\max_{a}\ \mathbb E\big[V\mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big],$$
with a separate node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ for each observation $x$. P-FDT replaces the family of per-observation nodes by one node $\mathrm{fdt}(\underline P,\underline G)$ whose value is a policy. I propose:

$$\pi^*\in\arg\max_{\pi\in\Pi}\ \mathbb E\big[V\mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G)=\pi)\big],\qquad \text{P-FDT}(P,G,x)=\pi^*(x).$$

Everything downstream of that node is recomputed under $\pi$. This includes the agent's own action in whatever observation she in fact gets, which is $\pi(\text{obs})$, and any predictor or copy whose behavior subjunctively depends on the function. Because $\pi$ is applied to the observation, the observation itself is typically a node downstream of the policy, as when a predictor determines what the agent sees. Thus, as in the paper, the agent does not condition on the observation. She evaluates policies by the unconditional expected utility of implementing them, then applies the winner to the input she actually has.

The paper's per-observation version can be recovered as a special case: it fixes the policy's behavior on other observations at the model's beliefs about them, a placeholder visible in the paper's "$q$" terms (e.g., how she'd act on seeing an empty box). P-FDT removes the placeholder by optimizing those values jointly.

## 3. Worked examples

**Newcomb (opaque).** One observation, so policies are actions and P-FDT equals FDT. One-boxing gives $0.99\cdot 10^6=\$990{,}000$; two-boxing gives $0.01\cdot 1{,}001{,}000+0.99\cdot 1000=\$11{,}000$. P-FDT one-boxes.

**Transparent Newcomb.** Observations: full or empty. Policies are pairs $(\pi(\text{full}),\pi(\text{empty}))$. The predictor fills the box iff she predicts $\pi(\text{full})=$ one-box. With accuracy 0.99 (and, for simplicity, the predictor's errors flipping the box):

- $(1,1)$ or $(1,2)$ where $\pi(\text{full})=1$: box full w.p. 0.99, payoff \$1M; with prob 0.01 empty, payoff $\pi(\text{empty})$'s: \$0 if one-box, \$1000 if two-box. Best: $(\text{one},\text{two})$, value $990{,}000+10=\$990{,}010$.
- $\pi(\text{full})=$ two: full w.p. 0.01 (payoff \$1,001,000), else empty (payoff \$1000 if $\pi(\text{empty})$ two-box): $\approx\$11{,}000$.

So $\pi^*=(\text{one},\text{two})$. Seeing a full box, P-FDT applies $\pi^*(\text{full})=$ one-box. Here P-FDT explicitly optimizes the empty-box response, which the paper treated as a free $q$. The paper's per-observation FDT leaves the answer unchanged, but policy-level optimization makes it well defined.

**Parfit's hitchhiker** has the same structure (paying = one-boxing when full).

**Mechanical blackmail.** Observations: letter or no letter. The blackmailer sends iff she predicts $\pi(\text{letter})=$ pay. With error rate $\epsilon$ in the paper's imperfect-predictor variant, refusing yields expected loss about $\epsilon\cdot 1{,}000{,}000$ versus about \$1000 when paying, so P-FDT refuses when $\epsilon<0.001$. This matches the paper's threshold figures: 0.0009 refuse, 0.00011 pay (the paper's "0.011%").

## 4. Where policies matter: multi-agent and multi-input cases

The source says the difference arises only in multi-agent dilemmas "so far as we can tell." Here is one account of why, which is mine. Suppose two agents run the same function and receive different observations (say, $x_1,x_2$), with payoffs depending on the pair of actions $(\pi(x_1),\pi(x_2))$. Intervening on a node "output at $x_1$" while leaving "output at $x_2$" at its prior would treat the copy's behavior as independent of the choice, which is exactly the independence error FDT is meant to avoid. An intervention on the whole function changes both coordinates consistently. In single-agent problems with one-shot observation, only one coordinate matters per world, so optimizing the policy and optimizing the response to the actual observation coincide, except when, as in the transparent cases, other coordinates influence the world (as the empty-box response did above) and their values must be taken from somewhere.

*Example (asymmetric coordination).* Two copies are privately told "you are A" or "you are B," and each receives \$10 if exactly one of them plays "go." No action rule can say what "go" should mean for an agent who sees A. A policy "A: go, B: wait" yields \$10 with certainty; since both copies run the same policy, this is exactly what P-FDT selects. Independent per-observation reasoning must instead guess the other coordinate.

## 5. Why policies and the "global perspective"

The paper's justification of FDT is "act as you would have precommitted to act" and "choose from a global perspective." P-FDT makes the first slogan literal: $\pi^*$ is the policy a rational agent would adopt as a precommitment before any observation, evaluated with the model's subjunctive structure rather than with causal-only structure. This also explains why P-FDT assigns nonnegative value to information: the policy class with access to $x$ includes every policy that ignores $x$. (Caveat: that argument holds only when information does not itself change what predictors do, since policies are graded by their consequences including their effect on what is observed.)

## 6. Open questions and my proposed handling

1. **Subjunctive structure is an input.** The source states plainly that deducing the dependency graph is "perhaps the largest open problem." P-FDT inherits it; I assume $G$ is given.
2. **Which observations count.** A policy over *all* histories could be astronomically large. Operationally I restrict to observations with nonzero prior and to coarse-grained equivalence classes that no predictor in the model distinguishes between. The source says nothing here; this is my proposal.
3. **Ties and mixed policies.** If two policies tie, the source does not say what to do. I suggest any maximizer is acceptable, and randomization only if the model contains a source of randomness that predictors cannot track. Without that, mixing adds nothing in expectation.
4. **Updating on evidence about the world.** P-FDT does not condition on $x$ in general, which would double-count ("double update," per the paper's note on timeless decision theory). But facts that are subjunctively independent of the policy, such as the lesion or termites, should be handled consistently; I assume their prior is retained and information about them enters through the policy's dependence on $x$. For ordinary evidence, such as a coin flipped by nature, the policy simply responds to the outcome and P-FDT reduces to ordinary expected utility.
5. **Fairness.** The paper concedes that no formal definition of "fair problem" exists. P-FDT would lose in problems that punish a policy for its internal form rather than its input–output behavior; its claimed domain is problems where payoffs depend on the policy only through behavior.
6. **Counterpossibles.** A policy different from the true one is a logical impossibility, so the $\mathtt{do}$ on $\mathrm{fdt}$ is a counterpossible intervention. The paper offers only the hope that mathematicians' handling of logical uncertainty provides precedent.

## 7. Comparison

CDT intervenes on a physical action token and conditions on observations. EDT conditions on actions. P-FDT intervenes on the type and quantifies over observations, so observation-dependent behavior is chosen jointly. The paper's slogan stands: EDT respects too many correlations, CDT too few, P-FDT those that reflect subjunctive dependence.

## 8. Conclusion

P-FDT, as I read footnote 16, selects an input-to-action map by maximizing expected utility under interventions on the decision function node, then applies it to the actual input. It agrees with action-level FDT on the paper's single-agent examples, resolves the free parameters (the "$q$" terms) the paper left implicit, and matters genuinely when several agents or branches share the function. Its main dependencies, a given subjunctive graph and a workable counterpossible calculus, remain open.