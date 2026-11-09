# P-FDT: Choosing Policies by Intervening on a Decision Function

## 1. Orientation

The source is Yudkowsky and Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*. Its main text mostly presents an action-based version of FDT for ease of exposition. Footnote 16 (and the parallel footnote 7) says what the authors actually prefer. Footnote 16 reads: "the author's preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

I call this preferred formulation **P-FDT**. This essay uses footnote 16 as its primary source. I reconstruct a precise version of P-FDT, apply it to examples, and flag where the footnote is silent and I am supplying an interpretation. Claims from the paper are marked "source"; proposals of mine are marked "my reading."

## 2. The core definition

**Source.** The paper's action-level rule (its Equation 4) is
$$\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\big[V\mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big].$$
The agent has a world-model $(P,G)$ and an observation $x$. She intervenes on a variable representing the output of her own decision function on that input. She does not intervene on a physical "Act" node, and she does not condition. A different observation changes *which* node is intervened on.

**Footnote 16's change (source).** The intervened node outputs a *policy*, a map $\pi:\mathcal X\to\mathcal A$ from observations to actions. The agent then applies the chosen policy to her actual observation.

**My formalization of P-FDT.** Let $\Pi=\mathcal A^{\mathcal X}$ be the set of policies, assumed finite or suitably restricted. Define
$$\pi^*=\arg\max_{\pi\in\Pi}\ \mathbb E\big[V\mid \mathtt{do}(\mathrm{FDT}_{\Pi}(\underline P,\underline G)=\pi)\big],\qquad \text{act } a=\pi^*(x).$$
Here $\mathrm{FDT}_\Pi(\underline P,\underline G)$ is a node standing for the output of the very procedure being run, quined as in the paper so that the self-reference is harmless. Everything downstream of that node in $G$ is recomputed. This includes the agent's own action in each possible observation-branch, any predictor or twin that models the procedure, and the observations themselves when they depend on predictions. The remaining nodes are held fixed. Crucially, the evaluation is **ex ante**. The policy is scored against the prior over everything, including which observation you end up with. You do not condition the model on the observation you actually received before choosing.

Two features follow immediately.

1. **Observation-as-index.** In the action version, $x$ selects which node $\mathrm{fdt}(\ldots,x)$ is intervened on. In P-FDT, $x$ is used only at the last step, to apply $\pi^*$. The ranking of policies never conditions on $x$. This makes the "updatelessness" of the theory explicit.
2. **Equivalence in single-agent cases.** If the observation is causally and subjunctively upstream of nothing the agent can influence, then maximizing over policies and maximizing action-by-action coincide, because the policy objective decomposes as a sum over observations weighted by their probabilities. The footnote's remark that the difference "only matters in multi-agent dilemmas" is compatible with this decomposition when the observation distribution is policy-independent. It is a claim about where the formulations diverge. It is not a claim that they never diverge, and the source states it with hedging ("so far as we can tell").

## 3. Why the policy version differs in multi-agent settings

**My reading.** The action-level rule treats the intervened node for observation $x$ as separate from the nodes for other observations $x'$. When other agents (or a predictor) depend on how the procedure behaves on *several* inputs, evaluating one input at a time can mishandle the coupling. Typical cases:

- A predictor simulates you on an input you won't actually see, as in the transparent Newcomb problem and blackmail.
- Several copies or teammates run the same procedure on *different* inputs, so that a joint output pattern matters.

The policy node is the joint object, so all couplings are intervened on together. The paper's own treatment gestures at this. In the transparent Newcomb and blackmail graphs it already introduces separate nodes $\mathrm{fdt}(\ldots,\textit{full})$, $\mathrm{fdt}(\ldots,\textit{empty})$, with the prediction determining which one controls the action. P-FDT is the natural packaging of that device. Instead of a family of per-observation nodes, there is one node whose value is the whole table.

## 4. Worked examples

### Newcomb's problem (no observation)

$\mathcal X$ is trivial, so a policy is an action. $\mathtt{do}(\mathrm{fdt}=\textit{onebox})$ gives box B full with probability 0.99, so
$$\mathbb E[V]=0.99\cdot 1{,}000{,}000=\$990{,}000.$$
$\mathtt{do}(\mathrm{fdt}=\textit{twobox})$ gives full with probability 0.01, so
$$\mathbb E[V]=0.01\cdot1{,}001{,}000+0.99\cdot 1{,}000=\$11{,}000.$$
These are the paper's numbers. P-FDT one-boxes.

### Transparent Newcomb

Policies are maps $\{\textit{full},\textit{empty}\}\to\{1,2\}$ (one-box or two-box). Write $\pi=(\pi_f,\pi_e)$. The predictor fills B iff it predicts $\pi_f=1$. Under the 0.99-accurate predictor model, with a wrong prediction flipping the box state:

| Policy | Value |
|---|---|
| $(1,\cdot)$, one-box on full, $\pi_e=\textit{two-box}$ | $0.99\cdot1{,}000{,}000+0.01\cdot 1{,}000=\$990{,}010$ |
| $(2,2)$, two-box always | $0.01\cdot 1{,}001{,}000+0.99\cdot 1{,}000=\$11{,}000$ |

The first row takes $\pi_e=\textit{two-box}$, which the paper identifies as the right empty-box behavior. Its value uses the paper's formula $990{,}000+0.01q\cdot1{,}000$ with $q=1$. The best policy is $(\textit{one-box},\textit{two-box})$. Seeing a full box, the agent applies $\pi^*(\textit{full})=\textit{one-box}$. This reproduces the paper's verdict with a transparent bookkeeping: the possibility of an empty box is not discarded just because it did not occur.

### Parfit's hitchhiker and mechanical blackmail

These have the same structure. The policy "pay when in the city" makes the driver rescue you, at probability about 0.99, so its value is roughly $0.99\cdot(1{,}000{,}000-1{,}000)$ (taking the paper's valuations, where being left to die costs $1{,}000{,}000$). The policy "don't pay" yields rescue only about 1% of the time. P-FDT pays.

For mechanical blackmail with a perfect predictor, the policy *refuse* is never blackmailed. The policy *pay* is always blackmailed and loses $1{,}000$. P-FDT refuses even holding the letter.

The paper also works an imperfect-predictor variant, and its numbers are worth recomputing. With false-positive rate $\epsilon$, refusing costs $\epsilon\cdot 1{,}000{,}000$ in expectation, while paying costs $1{,}000$. The break-even is $\epsilon=0.001$, and the paper's 0.0009 versus 0.00011 examples fall on either side of it. Refusing is better below $0.1\%$ error and paying is better above.

### Smoking lesion

The relevant dependency graph has the policy node connected to the act but *not* to cancer. Intervening on the policy leaves the lesion probability unchanged, so smoking gains $1{,}000$ in every branch. P-FDT smokes. The dependency structure fed in, not the policy formalism, does the work here.

## 5. Where "policy" earns its keep: a multi-agent illustration

**My example** (the source states only that such cases exist). Two agents run the same procedure. Agent 1 sees signal $s_1\in\{L,R\}$, and agent 2 sees $s_2\in\{L,R\}$, with the two signals independent and uniform. They get a payoff only if they pick *different* sides when signals match and the *same* side when signals differ. A per-observation action rule must choose the node for the actual $s_i$ while treating the other agent's response to the other signal pattern as fixed or as inherited from the same node. A policy rule evaluates the entire map $\pi:\{L,R\}\to\{L,R\}$, which both agents instantiate, and then finds the best joint behavior across all four signal pairs. The best symmetric policy depends on the whole table. Optimizing one entry at a time can land on a worse fixed point, a point that is stable under single-entry changes but not under changes to the whole table.

This is my own construction, but it is the natural reason a policy node would matter. Because both agents are subjunctively linked through the *entire* function, the intervention must be on the entire function.

## 6. Treatment of dependencies and counterfactuals

**Source.** P-FDT inherits the paper's three-way contrast:

- EDT conditions, so it preserves *all* correlations, including merely statistical ones.
- CDT intervenes on the physical act, so it preserves only causal structure.
- FDT intervenes on the decision function's output, so it preserves all *subjunctive* dependencies. These cover causal ones as a special case, plus logical correlates such as twins and predictors, and exclude mere statistical correlations such as the lesion.

The counterfactual "what if my procedure output $\pi'$?" is a counterpossible when the procedure in fact outputs $\pi^*$. The paper admits there is no satisfactory general account of counterpossibles. It sidesteps this by requiring that a graph $G$ of subjunctive dependencies be supplied as an input, just as CDT is supplied a causal graph. Footnote 9 notes that a logical analogue of conditioning would need conditional probabilities on false logical sentences, which are currently undefined.

**My reading on the footnote's open questions.** The footnote leaves several matters unspecified, and I fill them in as follows.

1. **Policy space.** Quantifying over all of $\mathcal A^{\mathcal X}$ can be infeasible. I would take $\Pi$ to be the set of policies the agent can represent and evaluate, and score the result as an approximation. The paper itself says bounded agents would only approximate the ideal equations.
2. **Observation probabilities in the objective.** Because the observation can depend on the policy (through a predictor), the weight on each branch must be computed *inside* the intervention, not before it. Using the prior over observations is wrong exactly in cases like blackmail, where the policy changes whether the letter arrives.
3. **Logically impossible branches.** Under a deterministic perfect predictor, branches in which the observation is inconsistent with the policy have probability zero and drop out. The agent's choices at those observations still matter for how the predictor models her, so their values must still be specified. The paper's remark that "the correct value of $q$ is 1 ... but it doesn't matter" fits this reading.
4. **Which dependencies count.** A node is downstream of the policy only if it varies with the *output* of the function, not merely with the agent's identity, species, or other features of the implementation. This matches the paper's fairness remark: a predictor that rewards *actions* is fair, while one that rewards having a certain *decision procedure* is not, and nothing guarantees P-FDT is optimal in the latter.
5. **Ties and non-uniqueness.** If several policies have equal value, the footnote gives no tie-break. I would adopt any fixed deterministic rule known to the agent, since the paper assumes the procedure is a fixed function.

## 7. Philosophical motivation

**Source.** Utility has primacy. The paper argues that a theory endorsing its own use, acting as one would have ideally precommitted, avoids ad-hoc binding, never assigns negative value to information, and resists extortion. The paper also argues that the sense in which an FDT agent "controls" a function is no more problematic than the sense in which a deterministic CDT agent "controls" a physical act.

**My reading on P-FDT.** The policy formulation is the cleanest statement of the "would-have-precommitted" idea. A policy is exactly the object one would precommit to. Evaluating policies against the prior, then applying the winner to the realized observation, makes the equivalence with ideal precommitment literal. It also explains why P-FDT avoids the reflective instability the paper attributes to CDT: there is no point at which new information makes a different policy look better, since the ranking of policies never conditions on that information.

## 8. Limits and open problems

- **Subjunctive dependence graphs** are not derivable from observation by any known method. This is the paper's largest stated open problem and applies equally to P-FDT. P-FDT gives correct answers *given* $G$.
- **Fairness** has no formal definition. The paper claims FDT does at least as well as rivals on "fair" problems but has found no formal criterion. Footnote 15 gives a problem, "punish whoever acts like a copy of Fiona", that is unfair to FDT and shows how hard it is to transport a problem across theories.
- **Policy-level dominance** exists: with FDT-style counterfactuals, no policy chosen by P-FDT is dominated. But like CDT's dominance it is relative to its own hypotheticals, so it cannot arbitrate between theories.
- **Policy-vs-action divergence.** The paper says it has not found cases outside multi-agent dilemmas where the difference matters. My formalization suggests it could also arise with policy-dependent observation distributions, but I flag this as conjecture.

## 9. Conclusion

P-FDT, as I reconstruct it from footnote 16, is expected-utility maximization over *policies*. Each candidate policy is evaluated by a Pearl-style surgery on a node representing the output of the agent's own decision function, with every subjunctively dependent variable updated and the rest held fixed. The chosen policy is then applied to the actual observation. It matches CDT and EDT where action-correlations coincide with causation, one-boxes in Newcomb and the transparent variant, pays in Parfit's hitchhiker, refuses blackmail, and smokes in the lesion case because the right dependency graph says the lesion does not depend on the output. Its credibility rests on the supplied dependency graph and on a counterpossible reasoning method that the source explicitly leaves undeveloped. Where I have gone beyond the footnote (the formal policy objective, the treatment of observation probabilities, the symmetric-coordination example, and the tie-breaking and policy-space restrictions), these are my interpretive proposals and not claims of the paper.

## Reference

Yudkowsky, E., and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060.