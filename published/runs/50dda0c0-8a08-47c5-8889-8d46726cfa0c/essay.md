# P-FDT: Choosing a Policy by Intervening on the Decision Function

## 1. Where the source stands

Yudkowsky and Soares's paper develops functional decision theory (FDT) mostly in terms of *actions*. Two footnotes record that this is a simplification. Footnote 7 says that "in the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions." Footnote 16, the primary source for this essay, is more explicit:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

I call the policy-selecting version **P-FDT**. The paper gives no separate equation for it. Everything below that goes beyond the footnote, including the equation in §3, is my reconstruction. I flag these points as I go.

## 2. The action-level theory as a baseline

The paper's FDT is an expected-utility rule with a special way of building hypotheticals. Given a world-model $(P,G)$, where $P$ is a distribution and $G$ a graph of logical, causal and computational structure, and an observation $x$:

$$\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\big[V \mid \mathrm{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big].$$

Here $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a variable in the model standing for the output of the algorithm on that input. The intervention is a Pearl-style surgery on this logical variable, not on the physical act. Anything that subjunctively depends on the algorithm's output, such as a predictor's forecast, a twin's choice, or the agent's own later action, changes with it. Mere statistical correlates, such as a lesion, do not.

Observation enters in a distinctive way. The agent does not condition on $x$. Instead, each possible observation selects a different node to intervene on. This is the source of the "updateless" flavour the paper notes.

## 3. P-FDT: definition

Let $\mathcal X$ be the set of possible observations and $\mathcal A$ the set of actions. A **policy** is a function $\pi:\mathcal X\to\mathcal A$. The set of policies is $\Pi=\mathcal A^{\mathcal X}$, finite when both sets are.

P-FDT's decision function takes $(P,G)$ and an observation $x$. It does two things:

1. It chooses a policy by intervening on the single node $\Phi=\mathrm{fdt}(\underline P,\underline G)$, whose value is a whole policy:

$$\pi^*=\arg\max_{\pi\in\Pi}\ \mathbb E\big[V\mid \mathrm{do}(\Phi=\pi)\big].$$

2. It applies the policy to its actual input and acts: $a=\pi^*(x)$.

In the graph, every node that depends on the agent's algorithm hangs off $\Phi$. A predictor's forecast depends on $\Phi$, usually through the predicted action $\Phi(x')$ for whatever $x'$ the predictor simulates. The agent's own action, in each possible observation-branch, is $\Phi(x)$ for that branch's $x$. The observation itself may depend on $\Phi$ too, since a predictor's behaviour can determine what the agent sees. That is exactly how the transparent Newcomb graph works.

Footnote 12's warning applies here. The node $\Phi$ is a variable in the model representing the output, a policy. The thing the agent finally executes is a different object, namely that policy applied to $x$.

**What changes relative to action-level FDT.** The action-level rule evaluates $\mathrm{do}(\mathrm{fdt}(P,G,x)=a)$ separately for each $x$. It treats the outputs on different inputs as separate nodes. For example, in the paper's transparent Newcomb graph there are nodes $\mathrm{fdt}(\cdot,\text{full})$ and $\mathrm{fdt}(\cdot,\text{empty})$. P-FDT replaces these with one node whose value fixes all of them at once.

## 4. Why the footnote says the difference is small

The footnote reports that the difference matters only in multi-agent dilemmas, "so far as we can tell." Here is a reconstruction of why.

For a single decision problem with one predictor and the agent's own action, the paper's action-level evaluation already holds the other branches fixed at the agent's actual or expected behaviour. Suppose the agent's own policy is $\pi$, and the action-level evaluation fixes the branch outputs $\pi(x')$ for $x'\neq x$ at their believed values $q$ (the paper uses a "prior probability $q$" for the empty-box branch). Then it maximises over $\pi(x)$ alone. If the believed values $q$ are what the agent would in fact choose, as they are in the paper's examples (the "correct $q$" is stated for each), then the two procedures agree.

They can disagree when the other branches are *not* fixed independently of the choice at $x$. That happens when several instances of the algorithm, in different roles or on different inputs, are all affected by the choice. In multi-agent settings each agent's policy is part of what others predict, and the best policy may not be recoverable by optimising one input at a time given beliefs about the rest. This is the standard coordination issue: the best joint assignment is not always found by best-responding coordinate by coordinate. I take this as the likely meaning of the footnote, but the paper does not spell it out.

## 5. Worked examples

**Transparent Newcomb.** $\mathcal X=\{\text{full},\text{empty}\}$, $\mathcal A=\{1,2\}$ boxes. There are four policies. Write $\pi=(\pi(\text{full}),\pi(\text{empty}))$. The predictor, accurate with probability 0.99, fills the box iff it predicts $\pi(\text{full})=1$. The agent sees full iff the box is full. Scoring with the paper's payoffs:

- $(1,1)$: $0.99\cdot 10^6 + 0.01\cdot 0 = 990{,}000$.
- $(1,2)$: $0.99\cdot 10^6 + 0.01\cdot 1000 = 990{,}010$.
- $(2,2)$: $0.99\cdot 1000 + 0.01\cdot 1{,}001{,}000 = 11{,}000$.
- $(2,1)$: $0.99\cdot 1000 + 0.01\cdot 10^6 = 10{,}990$.

The maximiser is $(1,2)$, with value \$990,010. It one-boxes on full and two-boxes on empty. This matches the paper's statement that "the correct value of $q$ is 1" for empty. Observing full, P-FDT executes one-boxing. It never conditions on "full" in order to decide.

**Mechanical blackmail.** The policies are $\pi(\text{letter})\in\{\text{pay},\text{refuse}\}$. The blackmailer sends the letter iff she predicts pay. Refusing gives a letter with probability near 0 (the paper's imperfect-predictor numbers: error 0.0009 gives an expected loss of \$900 for refusal against a certain \$1,000 for paying). P-FDT selects "refuse," then applies it on seeing the letter.

**Twin prisoner's dilemma.** Both players run the same algorithm and the same node $\Phi$, so choosing $\Phi=\text{cooperate}$ fixes both moves. P-FDT cooperates.

**Smoking lesion.** The lesion is not downstream of $\Phi$, so choosing a policy leaves its probability fixed. The policy "smoke" beats "refrain" by the value of smoking times the probability the policy is actually controlling the act.

## 6. Open questions in the footnote, and my proposals

The footnote leaves several matters open. Each of the following is my interpretation, not a claim of the source.

**(a) What counts as an "input" of the policy?** The footnote says the policy maps "inputs" to actions. The paper's formal inputs are the observation history $x\in\mathcal X$. The paper also lets the model $M$ be an input. My operational proposal is that the policy ranges over everything the agent will condition behaviour on at decision time, so that fixing $\Phi$ fixes behaviour in every situation the model considers possible. A coarse input space means fewer policies and a coarser choice, but any consistent choice is still a function from inputs to actions.

**(b) Observations as downstream variables.** Since predictors can influence what is observed, the observation node must sit downstream of $\Phi$ in the graph where the problem demands it. I propose that the graph always include $\Phi$'s influence on $\mathrm{Obs}$ explicitly, as the transparent Newcomb graph does. Failing to do so would reintroduce conditioning on $x$, and the "updateless" behaviour would be lost.

**(c) Ties and probability-zero branches.** Some observations may have probability zero under every policy, so the policy's value does not constrain its output there. I suggest breaking ties arbitrarily, or by any rule one likes, since the choice affects no expected utility.

**(d) The counterpossible machinery.** Footnote 9 says the paper requires "the relevant logical dependency structure be given as an input," and no way of deducing that structure is supplied. P-FDT inherits this unchanged. The set of policies makes the structure harder to specify rather than easier, because $G$ must say how every predictor's behaviour varies with the whole function, not only with its value at one input. The paper names inferring such structure as perhaps the largest open problem.

**(e) Computational cost.** $|\Pi|=|\mathcal A|^{|\mathcal X|}$ grows quickly. The paper already notes that exact maximisation is idealised for realistic world-models. For P-FDT I propose that one can exploit structure. If the problem decomposes, the utility is a sum over observation-branches weighted by probabilities that depend on $\Phi$ only through a few values, and policies can be optimised branch by branch, which is one way the action-level and policy-level answers coincide.

**(f) Reflective stability.** The paper stresses that FDT agents act as they would have precommitted to act. P-FDT makes this literal, since the policy is exactly the object one would precommit to. This is my reading, but it fits the paper's argument from precommitment and from the value of information. Selecting a policy before seeing $x$ can never make the agent worse off in expectation than any fixed alternative policy, by construction, because the maximisation is over all policies.

## 7. How to apply P-FDT to an unfamiliar case

1. List the observations $\mathcal X$ the agent may receive and the actions $\mathcal A$ available after each.
2. Build $(P,G)$. Include a node $\Phi$ for the agent's algorithm and mark everything that depends on it: the agent's actions, predictors' forecasts, twins, and the observations those influence. Leave purely statistical correlates, such as the lesion, off $\Phi$'s descendants.
3. For each policy $\pi$, compute $\mathbb E[V\mid\mathrm{do}(\Phi=\pi)]$ by propagating through the graph.
4. Pick the best policy $\pi^*$.
5. Execute $\pi^*(x)$ for the observation actually received.

A check on the result: a good P-FDT answer should not change when the agent learns her actual observation, except through step 5.

## 8. Claims and caveats

Claims taken from the source: the policy-selection version exists and is the authors' preferred one; it intervenes on the FDT node and chooses a policy rather than an action; the policy is then applied to the agent's inputs; the difference is, as far as the authors can tell, confined to multi-agent dilemmas.

My own additions: the explicit maximisation formula, the four-policy transparent Newcomb calculation, the explanation of why single-agent cases coincide, and the proposals in §6. I have not proved the claimed coincidence, only argued it informally. The source also does not say that P-FDT and action-level FDT always agree outside multi-agent cases, only that the authors have not found a difference.

## 9. Conclusion

P-FDT keeps the paper's central idea, imagining the decision function giving a different output and tracing only the subjunctive dependencies, and applies it to the whole input-to-action mapping. In ordinary cases the results match action-level FDT, and the footnote locates the gap in multi-agent problems. The policy view clarifies why FDT never needs to update on the observation in the usual way: the decision is made at the level of the function, and the observation only picks out which of its outputs gets used. Its hardest unsolved problem is unchanged: it requires a trustworthy account of how the world's structure depends on that function.