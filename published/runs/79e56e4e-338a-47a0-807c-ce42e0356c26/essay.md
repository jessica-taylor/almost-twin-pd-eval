# Policy Functional Decision Theory (P-FDT): Choosing the Function, Not the Output

## 1. The source and its status

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* develops functional decision theory (FDT) mostly as a theory that selects **actions**. The agent intervenes on a variable that represents the output of her decision function on her *current* input. Twice, in footnotes, the authors say that this is not the version they actually prefer. Footnote 16, which this essay treats as the primary source, reads:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

The earlier footnote 7 it refers back to says:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

I will call the theory described in these footnotes **P-FDT** (policy functional decision theory). The action-selecting theory of the paper's main text, its equation (4), I will call **action-FDT**. I also mention causal decision theory (CDT) and evidential decision theory (EDT) where useful.

The footnotes are short. They fix three things:

1. the object of choice is a policy, meaning a map from inputs (observations) to actions;
2. the choice is made by intervening on a node representing the decision function;
3. the agent then applies the chosen policy to her actual input.

Much else is left open. Section 5 lists what is undetermined and proposes resolutions. These resolutions are marked as mine.

## 2. Background: action-FDT

The paper models the agent's beliefs as a probability distribution $P$ together with a graph $G$. The graph encodes "subjunctive dependencies": which variables would change if the output of a given mathematical function changed. Causal dependence is a special case. Two physical systems computing the same function, such as an agent and a predictor's accurate model of her, both depend subjunctively on that function's output.

Let $V = \mathcal{U}(\textsc{Outcome})$ be the utility variable and $x \in \mathcal{X}$ the agent's observation history. Action-FDT is the paper's equation (4):

$$
\mathrm{FDT}(P,G,x) \;:=\; \operatorname*{argmax}_{a\in\mathcal{A}} \; \mathbb{E}\!\left(V \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline{P},\underline{G},\underline{x}) = a\big)\right).
$$

Here $\textsc{fdt}(\underline P, \underline G, \underline x)$ is a variable in the agent's own model, standing for "what the FDT algorithm outputs on these inputs." The $\mathtt{do}$ operator is Pearl's intervention, applied to a logical variable rather than a physical one. The source admits that this involves counterpossible reasoning. If the function in fact outputs $a_1$, then "it outputs $a_2$" is a logical falsehood. The source handles this by requiring $G$ to be supplied as input, just as CDT requires a causal graph.

Two features of equation (4) matter for what follows.

- **No conditioning on the observation.** The expectation is not conditioned on $\textsc{Obs}=x$. In the source's words, "FDT responds to observation by changing which node it intervenes upon." Observing $x$ instead of $y$ moves the intervention from $\textsc{fdt}(\underline P,\underline G,\underline x)$ to $\textsc{fdt}(\underline P,\underline G,\underline y)$.
- **Other inputs are held at prior beliefs.** When intervening on the node for input $x$, the nodes for other inputs $y \neq x$ are left alone. They keep whatever distribution $P$ assigns them. In the transparent Newcomb analysis, the source writes $q$ for "Fiona's prior probability that she two-boxes upon seeing the box empty," and remarks that its exact value "doesn't matter" there.

The second feature is exactly what P-FDT changes.

## 3. Defining P-FDT

### 3.1 The policy node

Read "the node $\mathrm{FDT}(-)$" literally. The dash marks an unfilled input slot. The node therefore represents the decision function's behavior across all inputs, not its output on one input.

Concretely, introduce a variable $\textsc{fdt}(\underline P,\underline G)$ whose values are policies:

$$
\pi \in \Pi := \mathcal{A}^{\mathcal{X}}, \qquad \pi : \mathcal{X}\to\mathcal{A}.
$$

The per-input nodes of action-FDT become deterministic children of this node:

$$
\textsc{fdt}(\underline P,\underline G,\underline x) \;=\; \pi(x)\quad\text{whenever } \textsc{fdt}(\underline P,\underline G)=\pi.
$$

Anything in the world that implements or predicts the agent's decision function sits downstream of the policy node. That includes the agent's own body, twins, copies, and predictors' models. Some of these depend on the whole policy. Others depend on particular components $\pi(x)$.

### 3.2 The decision rule

P-FDT selects

$$
\boxed{\;\pi^\star \in \operatorname*{argmax}_{\pi\in\Pi} \; \mathbb{E}\!\left(V \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G)=\pi\big)\right),\qquad \text{then act } \pi^\star(x).\;}
$$

As a procedure, this runs in four steps:

1. Take the model $(P,G)$ as input. Do not condition on the observation.
2. For each policy $\pi$, set the policy node to $\pi$. Propagate through $G$, so that every implementation and prediction of the function now behaves according to $\pi$. Compute expected utility.
3. Choose a maximizing policy $\pi^\star$, breaking ties canonically (see §5.3).
4. Apply $\pi^\star$ to the actual observation $x$ and output $\pi^\star(x)$.

The observation $x$ plays no role in steps 1–3. Every instance of the agent, in every observational situation, computes the same $\pi^\star$ and differs only in step 4. This is the precise sense in which the footnote's agent chooses a policy "to which the agent then applies her inputs."

### 3.3 Philosophical gloss

The source's main argument for FDT is that it "simply act[s] as [it] would have ideally precommitted to act." P-FDT makes this literal. Choosing $\pi^\star$ from the unconditioned model is choosing the plan you would bind yourself to before seeing anything. The difference from real precommitment is that no binding is needed. Every instance of the function recomputes the same plan and follows it.

The source's "global perspective" asks "What would the entire universe look like if the FDT algorithm behaved differently?" P-FDT takes "behaved differently" to mean differently *as a whole function*, not just at the current input.

## 4. A worked single-agent case: transparent Newcomb

Box A always holds \$1,000. The predictor fills box B with \$1,000,000 iff she predicts the agent would one-box upon seeing two full boxes. She is accurate with probability $0.99$. Inputs are $\mathcal{X}=\{\textit{full},\textit{empty}\}$, actions are $\{1,2\}$ (one-box, two-box), so there are four policies.

Model the predictor as reading the component $\pi(\textit{full})$:

- if accurate, she fills B iff $\pi(\textit{full})=1$;
- if inaccurate, she does the opposite.

The agent then sees the box's state $s$ and acts $\pi(s)$.

| Policy $(\pi(\textit{full}),\pi(\textit{empty}))$ | Accurate (0.99) | Inaccurate (0.01) | $\mathbb{E}V$ |
|---|---|---|---|
| (1, 2) | full → 1: \$1,000,000 | empty → 2: \$1,000 | **\$990,010** |
| (1, 1) | full → 1: \$1,000,000 | empty → 1: \$0 | \$990,000 |
| (2, 2) | empty → 2: \$1,000 | full → 2: \$1,001,000 | \$11,000 |
| (2, 1) | empty → 1: \$0 | full → 2: \$1,001,000 | \$10,010 |

So $\pi^\star = (1,2)$: one-box on seeing full, two-box on seeing empty. An agent facing two full boxes leaves the \$1,000 behind.

This matches the source's action-FDT result. Its value for one-boxing, $\$990{,}000 + 0.01q\cdot\$1{,}000$, equals the top row when $q=1$, which the source says is "the correct value of $q$." The agreement is no accident, as the next subsection shows.

The same tabulation handles the source's other cases.

- **Parfit's hitchhiker.** Policies map *in-city* to pay/refuse. The driver reads the *in-city* component, so "pay" wins.
- **Mechanical blackmail with a 0.0009 false-positive rate.** "Refuse when blackmailed" costs $0.0009 \times \$1{,}000{,}000 = \$900$ in expectation. "Pay" costs \$1,000. At a 0.011% error rate, wherever the computation is set up so that refusing costs more than \$1,000 in expectation, the ordering flips. The source reports that at that rate "she pays."

### 4.1 When P-FDT and action-FDT agree, and when they need not

The following observation is mine, not the source's.

**Proposition (global ⇒ coordinatewise).** Assume:

- the model's dependency structure is the policy-node structure of §3.1;
- the agent's prior beliefs about her other-input behavior are correct, i.e. $P$ assigns probability 1 to $\textsc{fdt}(\underline P,\underline G,\underline y)=\pi^\star(y)$ for all $y\neq x$.

Then $\pi^\star(x)$ is an action-FDT-optimal choice at $x$.

*Proof sketch.* Under these assumptions, intervening on the single node $\textsc{fdt}(\underline P,\underline G,\underline x)=a$ yields the same distribution as intervening on the policy node with the policy $\pi^\star[x\mapsto a]$, which is $\pi^\star$ with its $x$-component replaced by $a$. Since $\pi^\star$ maximizes over all policies, no single-coordinate deviation does better. $\square$

The converse fails. Action-FDT optimizes one coordinate while holding beliefs about the others fixed. It therefore finds coordinatewise optima, which are equilibrium-like points. P-FDT finds a global optimum.

In transparent Newcomb the two coincide, because the other coordinate barely matters. When several coordinatewise optima exist, or when the agent's beliefs about her other-input behavior are not pinned down in advance, the two theories can diverge. This explains the footnote's claim that the difference "only matters in multi-agent dilemmas so far as we can tell." Divergence requires several distinct inputs to the same function whose outputs must be *jointly* right. That situation most naturally arises when several instances of the function face different inputs.

## 5. A case where the policy matters: asymmetric coordination between copies

The following example is my own illustration.

Two physically separate instances of the same agent run the same decision function on the same model $(P,G)$. They cannot communicate. One is shown *red*, the other *blue*, and each knows the setup. Each outputs $X$ or $Y$. Each instance receives \$1,000,000 if their outputs **differ**, and nothing otherwise.

**P-FDT.** Policies are maps $\{\textit{red},\textit{blue}\}\to\{X,Y\}$. Under $\mathtt{do}(\textsc{fdt}(\underline P,\underline G)=\pi)$, the red instance outputs $\pi(\textit{red})$ and the blue instance outputs $\pi(\textit{blue})$. So

$$
\mathbb{E}V(\pi) = \$1{,}000{,}000\cdot \mathbf{1}[\pi(\textit{red})\neq\pi(\textit{blue})].
$$

Two policies tie: $(X,Y)$ and $(Y,X)$. Steps 1–3 of the procedure do not use the observation, so both instances compute the same argmax with the same tie-breaker, say lexicographic order, and select the same policy, say $(X,Y)$. Red outputs $X$, blue outputs $Y$, and both collect the money. The asymmetry of the inputs is exploited exactly because the choice is made *before* the inputs are consulted.

**Action-FDT.** The red instance intervenes on $\textsc{fdt}(\underline P,\underline G,\underline{\textit{red}})$. Blue's action is a different node, held at the prior $q = P(\textsc{fdt}(\underline P,\underline G,\underline{\textit{blue}})=X)$. Then

$$
\mathbb{E}V(X) = (1-q)\cdot \$10^6, \qquad \mathbb{E}V(Y) = q\cdot \$10^6.
$$

With no principled reason for $q\neq \tfrac12$, the two actions tie. If each instance breaks the tie the same canonical way, both output $X$ and both get nothing.

Action-FDT can succeed only if its self-model already contains the right asymmetric beliefs about itself. For example, red would need to believe blue outputs $Y$, and blue would need to believe red outputs $X$. But that amounts to having already solved the coordination problem that the decision procedure was supposed to solve. P-FDT gets the asymmetry for free.

Three remarks follow.

- **The money is not for altruism.** Each instance is paid only if the joint outcome is right. Self-interest suffices. This parallels the source's voting example, in which an FDT agent votes "not out of altruism, but out of an awareness that the other members of the group will reason symmetrically."
- **"Multi-agent" should be read broadly.** This is my interpretive proposal. The same structure arises for a single agent at two times with different inputs, for instance if payoff depends on her morning and evening actions being complementary. The source's gym example of an agent "coordinat[ing] with herself over time" shows the authors already treat temporally separated instances of one agent as quasi-agents. I suggest reading footnote 16's "multi-agent" as "multi-instance": several instances of the function receiving distinct inputs whose outputs interact. The footnote's hedge "so far as we can tell" leaves room for this reading.
- **Twins with identical inputs.** In the twin prisoner's dilemma, both twins receive the same input. The policy and action formulations then agree, because only one coordinate of $\pi$ is ever exercised.

## 6. What the footnote leaves open, and proposed resolutions

### 6.1 What is the policy node, graph-theoretically?

The footnote says the agent "intervenes on the node $\mathrm{FDT}(-)$" but gives no graph. I proposed (§3.1) a single policy-valued node whose children are the per-input output nodes.

An alternative is to keep the per-input nodes as roots and intervene on all of them simultaneously. That is a joint $\mathtt{do}$ on the vector $(\textsc{fdt}(\underline P,\underline G,\underline x))_{x\in\mathcal X}$. In finite problems the two are equivalent: a joint assignment to the vector is a policy. I prefer the single node because some predictors plausibly depend on the function *as an object* rather than on individual outputs. For example, a predictor might inspect the agent's source code and act on a property of the whole input–output map.

### 6.2 Is the expectation conditioned on the observation?

The footnote is silent here. Equation (4) does not condition on $\textsc{Obs}=x$. The source also endorses Fiona's reasoning that "if their action were different, they might have *made different observations*." I therefore take P-FDT to evaluate policies under the **unconditioned** model $P$.

This choice is essential. If one conditioned on $x$ and also intervened on the policy, the problem the source attributes to Timeless Decision Theory reappears: "a kind of 'double update' which proves harmful in practice." In transparent Newcomb, conditioning on *full* while choosing a policy would make the predictor's accuracy look irrelevant, because box B is already known to be full. The agent would then drift toward two-boxing.

### 6.3 Ties

In action-FDT, ties are a nuisance. In P-FDT they are structurally important: §5 succeeds only because all instances break ties identically. The source does not specify a tie-breaking rule. I propose that the rule be:

- deterministic,
- a fixed part of the function, such as a canonical ordering of $\Pi$, and
- independent of $x$.

These conditions guarantee that all instances sharing $(P,G)$ select the same $\pi^\star$.

### 6.4 Deterministic or randomized policies?

The footnote speaks of a policy "which maps inputs to actions," which suggests deterministic maps. I recommend deterministic policies as the default. Randomization that the environment cannot predict can be modelled as an explicit chance node whose outcome forms part of the input. A coin flip then becomes an observation, and the policy maps flip outcomes to actions.

Whether P-FDT should range over mixed policies directly is genuinely open. The answer depends on what predictors are assumed to know about the agent's randomness. The source's Death in Damascus discussion shows how much depends on that assumption.

### 6.5 What counts as an input, and which instances share a function?

Footnote 7 identifies inputs with observations, so $\mathcal X$ is the space of observation histories. Instances share a function only if they share $(P,G)$, since the node is $\textsc{fdt}(\underline P,\underline G)$.

This leaves open a hard question. Do agents with slightly different models still count as "the same function"? The source's smoking lesion analysis separates $\textsc{fdt}(\underline{P_S},\underline G)$ from $\textsc{fdt}(\underline{P_R},\underline G)$ when the agent's utility functions differ. That supports a strict reading: different models give different functions, and any similarity between them must be captured explicitly in $G$. I adopt this reading. It means that cooperation between *non-identical* agents depends entirely on $G$ correctly representing how their functions relate. That is part of the problem the source calls "perhaps the largest open problem in the study of functional decision theory," namely deducing subjunctive dependencies.

### 6.6 Tractability

$|\Pi| = |\mathcal A|^{|\mathcal X|}$ is astronomically large for realistic observation spaces. The source already treats FDT as an idealization: "maximizing over all possible actions is not realistic." For P-FDT the idealization is more severe still. Any bounded approximation must decide which coordinates of the policy to optimize jointly. A natural heuristic is to optimize jointly only over inputs that the agent believes some dependent process, such as a predictor or a copy, actually reads.

## 7. A recipe for deciding unfamiliar cases

Putting the pieces together, here is how to apply P-FDT to a new problem.

1. **List inputs.** Enumerate every observation history any instance of your function might receive. Include counterfactual ones, such as "empty box" or "no blackmail letter."
2. **Locate dependents.** Identify every process that depends on your function: your own body at each input, copies, and predictors. For each, note which inputs' outputs it depends on.
3. **Score policies.** For each policy $\pi$, propagate it to all dependents and compute $\mathbb{E}V$ under your *prior*, without updating on what you have seen.
4. **Choose and act.** Choose $\pi^\star$ with a fixed tie-breaker, then do $\pi^\star(x)$.

The resulting verdicts:

- **Newcomb's problem:** one-box.
- **Smoking lesion:** smoke, because the lesion does not depend on the function.
- **XOR blackmail:** refuse, because the termites do not depend on the function. The source notes that action-FDT agrees, and the payment policy only changes whether the letter arrives.
- **Asymmetric coordination problems:** jointly optimal profiles, where action-FDT may stall.

## 8. Conclusion

P-FDT is the authors' preferred form of functional decision theory, stated only in footnotes 7 and 16. It replaces "which output should this function give on this input?" with "which input–output map should this function be?" Formally, it intervenes on a policy-valued node $\textsc{fdt}(\underline P,\underline G)$, maximizes unconditioned expected utility over $\Pi=\mathcal A^{\mathcal X}$, and executes $\pi^\star(x)$.

I have argued that, given correct self-beliefs, P-FDT's choices are always action-FDT-optimal as well. The reverse can fail when several instances of the function receive different inputs and must coordinate. This is the content behind the footnote's "multi-agent" qualification, which I suggest reading as "multi-instance."

The footnotes leave several matters open: the exact graph structure, the treatment of observations, tie-breaking, randomization, and the identity conditions for "the same function." I have proposed definite answers: a single policy node, no conditioning on observations, deterministic canonical tie-breaking, deterministic policies by default, and strict identity of $(P,G)$. These are interpretations, not the authors' stated commitments. What P-FDT inherits unchanged from action-FDT is its deepest open problem, which is how to construct the graph $G$ of subjunctive dependencies on which every evaluation relies.

---

**References**

- Yudkowsky, E. & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060 (primary source; footnotes 7 and 16).
- Pearl, J. (2000). *Causality*. Cambridge University Press.
- Gibbard, A. & Harper, W. (1978). "Counterfactuals and Two Kinds of Expected Utility."
- Dai, W. (2009). "Towards a New Decision Theory," *Less Wrong*.