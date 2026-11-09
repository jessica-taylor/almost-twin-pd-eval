# Policy Functional Decision Theory (P-FDT): Choosing Maps, Not Moves

## 1. What the source actually says

Yudkowsky and Soares's *Functional Decision Theory: A New Theory of Instrumental Rationality* contrasts functional decision theory (FDT) with causal decision theory (CDT) and evidential decision theory (EDT). The FDT agent asks "Which output of this decision procedure causes the best outcome?" rather than "Which physical act of mine causes the best outcome?" The formal machinery in the body of the paper chooses an *action*. Twice, though, the authors say that this is not the version they prefer. Footnote 7:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

And footnote 16, which this essay takes as the primary source for **policy functional decision theory (P-FDT)**:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

These two sentences are the whole textual basis. They commit P-FDT to four things:

1. **The point of intervention** is the node representing the agent's decision function.
2. **The value set at that node** is a policy, a map from inputs to actions.
3. **The action is obtained by application**: the agent "applies her inputs" to the chosen policy.
4. **The scope of the difference**: it matters only in multi-agent dilemmas, "so far as we can tell."

Everything beyond these four points is reconstruction. Below I mark claims as coming from the source or as my own proposals. To keep names distinct, I call the action-choosing theory formalized in the body of the paper **A-FDT** (action-level FDT).

## 2. Background: A-FDT

The paper models an agent by a probability distribution $P$ together with a graph $G$. The graph encodes not only causal structure but *subjunctive dependence*: which variables would change if the output of a given mathematical function changed. Writing $V$ for utility and $\mathrm{fdt}(\underline P,\underline G,\underline x)$ for the model variable representing the output of the FDT algorithm on inputs $(P,G,x)$, the paper's equation (4) is

$$
\mathrm{FDT}(P,G,x) \;=\; \operatorname*{argmax}_{a\in\mathcal A}\; \mathbb E\!\left[V \;\middle|\; \mathtt{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\right].
$$

Two features matter for what follows.

- **Observations select the node; they are not conditioned on.** "Where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon."
- **Different observations correspond to different nodes.** On seeing a full box the agent intervenes on $\mathrm{fdt}(\ldots,\textit{full})$, and on seeing an empty box she intervenes on $\mathrm{fdt}(\ldots,\textit{empty})$. When A-FDT evaluates one of these nodes, the other is held at the agent's prior belief about it. The paper's transparent-Newcomb calculation carries an explicit parameter $q$ for "Fiona's prior probability that she two-boxes upon seeing the box empty."

That second feature is what P-FDT changes. In A-FDT, the agent's outputs on other inputs are treated as facts to be predicted. In P-FDT, they are chosen together with the current output.

## 3. Defining P-FDT

### 3.1 The definition

**Setup (my formalization).** Let $\mathcal X$ be the finite set of inputs (observation histories) the agent might receive in the problem, and $\mathcal A$ the finite action set. The policy space is

$$\Pi = \mathcal A^{\mathcal X}.$$

The model $(P,G)$ contains a single policy node $\Phi := \mathrm{fdt}(\underline P,\underline G)$ with values in $\Pi$. Each input-specific node is a deterministic child of it:

$$\mathrm{fdt}(\underline P,\underline G,\underline x) \;=\; \Phi(x).$$

Any environmental process that runs, simulates or predicts the agent on input $x$ depends on $\Phi(x)$. A process that inspects the agent's whole disposition, for example a predictor reasoning about what she would do in several situations, may depend on $\Phi$ as a whole.

**Definition (P-FDT).**

$$
\mathrm{EU}(\pi) \;=\; \mathbb E\!\left[V \;\middle|\; \mathtt{do}(\Phi=\pi)\right],\qquad
\pi^* \in \operatorname*{argmax}_{\pi\in\Pi}\mathrm{EU}(\pi),\qquad
\text{P-FDT}(P,G,x) \;=\; \pi^*(x).
$$

The three steps correspond to the footnote's three verbs. The agent *intervenes* on the decision-function node, *chooses* a policy, and *applies* her input.

### 3.2 Open choice 1: evaluate before or after the observation?

The footnote does not say whether $\mathrm{EU}(\pi)$ is computed from the model as it stood before the input arrived, or after conditioning on $\textit{Obs}=x$. There are two candidates:

- **(U), updateless:** $\mathbb E[V\mid \mathtt{do}(\Phi=\pi)]$, as above.
- **(C), conditioned:** $\mathbb E[V\mid \mathtt{do}(\Phi=\pi),\ \textit{Obs}=x]$.

**My proposal is to adopt (U).** Three reasons support it.

1. **It matches the paper's own calculation.** In the transparent Newcomb problem the paper computes A-FDT's value for one-boxing as $\$990{,}000 + 0.01q\cdot\$1{,}000$. That figure averages over the 1% branch where the box is *empty*, even though the agent is looking at a full box. (The displayed formula does include "$\textit{Obs}=\textit{full}$" inside the conditioning bar, but the arithmetic does not condition on it. I follow the arithmetic.)
2. **The source warns against a "double update."** In an inline note, the paper says Timeless Decision Theory's practice of "conditioning on evidence *and* changing the place where one intervenes" creates a "double update" that "proves harmful in practice." The note also says that Wei Dai's "Updateless Decision Theory" takes its name from this apparent "lack of updating."
3. **(C) undoes the theory.** Under (C) in transparent Newcomb, every policy with $\pi(\textit{full})=\text{two-box}$ scores $\$1{,}001{,}000$ given the full box, and every policy with $\pi(\textit{full})=\text{one-box}$ scores $\$1{,}000{,}000$. The agent therefore two-boxes on seeing a full box. The predictor foresees this, and the agent faces empty boxes.

Under (U), the "prior" is the model of the decision problem as specified, before the in-problem observation. How far back that prior should reach is a genuine open question that neither the footnote nor I settle. One consequence of (U) is that $\pi^*$ does not depend on $x$. The agent could compute it before the problem begins, so P-FDT literally implements the paper's slogan that FDT agents "act as they would have precommitted to act."

### 3.3 Open choice 2: what are the inputs and the policies?

**Inputs.** In equation (4) the inputs are $(P,G,x)$. I hold $(P,G)$ fixed and let policies range over $x$, since footnote 7 glosses policies as "mappings from observations to actions." The paper's smoking-lesion analysis is harder. There the lesion determines which *model* ($P_S$ or $P_R$, with different utilities) the agent runs. A policy over models would need a single utility function for scoring policies that span different utility functions, and the source supplies none. I leave that case outside the definition.

**Policies.** "Maps inputs to actions" reads most naturally as deterministic maps. If the agent has access to randomness that predictors cannot anticipate, one could allow stochastic policies $\Pi=\Delta(\mathcal A)^{\mathcal X}$. That is an extension, not the source's claim.

**Ties.** Ties are broken by a fixed rule built into the function. Because every instance of the function computes the same $\pi^*$, even an arbitrary rule is shared across instances. This matters in §5.

### 3.4 Open choice 3: what the graph must encode

P-FDT does not solve the paper's self-described "largest open problem": how to learn the structure of subjunctive dependence. It changes only the *type* of the intervened node. That still requires $G$ to say, for each environmental variable, whether it depends on $\Phi(x)$ for particular $x$, on several coordinates, or on nothing. A predictor that looks only at what you would do on seeing a full box depends on $\Phi(\textit{full})$. A lesion depends on none of $\Phi$.

## 4. Worked examples

**Newcomb's problem.** There is one input, so $\Pi\cong\mathcal A$ and P-FDT coincides with A-FDT. With a 99%-accurate predictor:

| Policy | Expected utility |
|---|---|
| One-box | $0.99\cdot 10^6 = \$990{,}000$ |
| Two-box | $0.01\cdot \$1{,}001{,}000 + 0.99\cdot\$1{,}000 = \$11{,}000$ |

The agent one-boxes. This confirms that the policy formulation adds nothing when there is nothing to map.

**Transparent Newcomb.** $\mathcal X=\{\textit{full},\textit{empty}\}$. The predictor fills box B iff she predicts one-boxing on seeing a full box, so the prediction depends on $\Phi(\textit{full})$ only, with 99% accuracy. Write policies as $(\pi(\textit{full}),\pi(\textit{empty}))$, with 1 for one-box and 2 for two-box:

| $\pi$ | 99% branch | 1% branch | $\mathrm{EU}(\pi)$ |
|---|---|---|---|
| (1,1) | full, take B: $10^6$ | empty, take B: 0 | 990,000 |
| (1,2) | full, take B: $10^6$ | empty, take both: 1,000 | **990,010** |
| (2,1) | empty, take B: 0 | full, take both: 1,001,000 | 10,010 |
| (2,2) | empty, take both: 1,000 | full, take both: 1,001,000 | 11,000 |

So $\pi^*=(1,2)$: one-box on a full box, two-box on an empty one. This reproduces the paper's A-FDT value at its "correct" $q=1$. A-FDT also one-boxes here for every $q$, so the two theories agree.

**Mechanical blackmail with a fallible blackmailer.** The blackmailer runs the program iff she predicts the agent would pay. With probability $\varepsilon$ she wrongly predicts payment from an agent who would refuse. The input "not blackmailed" calls for no action, so only $\pi(\textit{blackmail})$ matters:

$$
\mathrm{EU}(\text{pay}) = -\$1{,}000,\qquad \mathrm{EU}(\text{refuse}) = -\varepsilon\cdot\$1{,}000{,}000.
$$

The agent refuses iff $\varepsilon<0.001$. At the paper's $\varepsilon=0.0009$ she refuses, with an expected loss of \$900, "even when holding the blackmail letter."

**Parfit's hitchhiker.** The policy "pay on reaching the city" scores
$$0.99(-\$1{,}000)+0.01(-\$10^6) = -\$10{,}990.$$
The policy "don't pay" scores
$$0.99(-\$10^6) = -\$990{,}000.$$
P-FDT pays.

## 5. Where P-FDT and A-FDT come apart

The footnote asserts the theories differ only in multi-agent dilemmas but gives no argument. Here is a precise account of when they agree. This is my analysis, though it is a standard fact from the theory of teams (Marschak and Radner).

**Proposition (agreement at the optimum).** Suppose that when A-FDT evaluates input $x$, its beliefs about the other input-nodes $\Phi(x')$, $x'\neq x$, are concentrated on the values $\pi^*(x')$. Then $\pi^*(x)$ is an A-FDT-optimal action at $x$.

*Proof.* Intervening on the single coordinate $x$ while the others stay at $\pi^*$ yields the policy $\pi^*[x\mapsto a]$, which agrees with $\pi^*$ except at $x$. So A-FDT's value for $a$ is $\mathrm{EU}(\pi^*[x\mapsto a])$, which is at most $\mathrm{EU}(\pi^*)$ by optimality of $\pi^*$. $\square$

**The converse fails.** A policy $\pi$ is *self-consistent* for A-FDT when each $\pi(x)$ is a best response at $x$, given correct beliefs about the other coordinates. Such policies are exactly the *person-by-person optimal* policies: no single coordinate can be improved alone. Every globally optimal policy has this property, but not conversely. A-FDT can therefore settle into a self-consistent but inferior policy, depending on the agent's priors about her own behaviour elsewhere.

**Example: the two-room coordination problem.** Two exact copies of an agent are placed in rooms labelled 1 and 2. The room label is the input. Each copy chooses $A$ or $B$, and both copies receive

$$
U(\text{room 1's act},\ \text{room 2's act}) =
\begin{cases} 10 & (A,B)\\ 1 & (B,A)\\ 0 & \text{otherwise.}\end{cases}
$$

- **P-FDT.** There are four policies. $\mathrm{EU}(1\mapsto A,\,2\mapsto B)=10$, which is maximal. Both copies compute the same $\pi^*$ and apply their own labels, so they get 10.
- **A-FDT.** The room-1 copy intervenes on $\mathrm{fdt}(\ldots,\textit{room 1})$ only. The room-2 copy's output is a *different* node, held at the room-1 copy's prior. If that prior says room 2 plays $A$, then $B$ is the best response. Symmetrically, room 2 responds $A$ to an expected $B$. The profile $(B,A)$ is self-consistent and pays 1.

A-FDT can land on either fixed point. Which one depends on beliefs that the agent has no principled way to fix, since they are beliefs about her own outputs. P-FDT removes this dependence: the function settles all its outputs at once.

**What "multi-agent" means here.** The underlying condition for divergence is *cross-input interaction*: some part of the world responds jointly to $\Phi$'s values on several inputs, so the payoff is not separable across coordinates. Copies and twins receiving different inputs are the natural source, which fits the footnote's "multi-agent." But a single agent facing a predictor can create the same structure. Suppose a predictor pays 10 if the agent *would* choose $A$ on seeing red and $B$ on seeing blue, pays 1 for the reverse, and the agent then sees one colour at random. This has exactly the structure of the two-room problem. So I read the footnote's "multi-agent" as "multi-instance": the decision function is evaluated, by copies or by predictors, on more than one input. The footnote's hedge, "so far as we can tell," leaves room for this reading.

## 6. Philosophical motivation

The paper's core image is that the agent should ask, "What if *this very decision process* produced a different conclusion?" A-FDT applies that question to the function's output on the present input but treats its outputs on other inputs as external facts. P-FDT extends the paper's own logic one step. A function's behaviour on input 1 and on input 2 are facts about the same mathematical object. If it is a mistake (the CDT mistake, in the paper's diagnosis) to vary one's act while holding a twin's identical computation fixed, it looks equally arbitrary to vary one's output on this input while holding one's output on another input fixed.

The policy formulation also sharpens the source's arguments from precommitment and from the value of information.

- **Precommitment.** The argmax over $\Pi$ under (U) *is* the ex-ante optimal precommitment. P-FDT does not merely approximate "acting as one would have precommitted"; the two are the same computation.
- **Value of information.** Because the policy is chosen before inputs are applied, receiving an input cannot lower ex-ante expected value relative to ignoring it. The constant policies are among the options, and they ignore the input entirely.

The costs are the paper's costs, made explicit. The agent sometimes takes an action that is worse in the world she can see: refusing the blackmailer while holding the letter, or leaving \$1,000 on the table in front of two full boxes. The paper's defence is that being "*the kind of agent*" who does so produces more utility, and P-FDT is precisely a formalization of choosing the kind of agent. There is also a computational cost: $|\Pi|=|\mathcal A|^{|\mathcal X|}$, exponential in the number of inputs. For bounded agents, a practical heuristic is to optimise only over the coordinates that some process in $G$ actually depends upon. In the blackmail problem that leaves a single coordinate.

## 7. A recipe for unfamiliar cases

1. **List inputs and actions.** Enumerate the inputs $\mathcal X$ the agent could face in the problem and the actions $\mathcal A$.
2. **Build the model with a policy node.** Construct $(P,G)$ with node $\Phi\in\mathcal A^{\mathcal X}$. Attach to $\Phi(x)$, or to $\Phi$ as a whole, every variable that subjunctively depends on it: the agent's own body when it receives $x$, copies, and predictors. Attach nothing to lesion-like correlates.
3. **Score every policy without updating.** Compute $\mathrm{EU}(\pi)=\mathbb E[V\mid\mathtt{do}(\Phi=\pi)]$ for each $\pi$, without conditioning on the actual input.
4. **Choose and apply.** Pick $\pi^*$ with a fixed tie-break, then perform $\pi^*(x)$ for the input actually received.
5. **Check for coordinate interaction.** If no variable depends jointly on several coordinates, the answer should agree with A-FDT run with correct self-beliefs (§5). Disagreement with A-FDT signals a coordination structure.

## 8. Conclusion

Footnote 16 specifies P-FDT tersely: intervene on the decision-function node, choose a policy, apply the input. Read together with the paper's formal apparatus, this yields a clean definition: $\pi^*=\operatorname{argmax}_\pi\mathbb E[V\mid\mathtt{do}(\Phi=\pi)]$, with action $\pi^*(x)$.

The source leaves three questions open, and I have resolved each with a stated assumption:

- Evaluate updatelessly, as the paper's own calculations and its warning about double updating suggest.
- Take inputs to be observations under a fixed model, and policies to be deterministic maps.
- Leave the open problem of subjunctive dependence where the source leaves it.

On this reconstruction, P-FDT and A-FDT agree whenever payoffs are separable across inputs, and in particular in every example the paper analyses. They diverge exactly when the world responds jointly to the function's outputs on several inputs. In those cases A-FDT can settle into a self-consistent but inferior policy, while P-FDT selects the globally best one.

## References

- Dai, W. (2009). "Towards a New Decision Theory." *Less Wrong*.
- Marschak, J., and Radner, R. (1972). *Economic Theory of Teams*. Yale University Press.
- Pearl, J. (2000). *Causality*. Cambridge University Press.
- Yudkowsky, E., and Soares, N. (2017). "Functional Decision Theory: A New Theory of Instrumental Rationality." arXiv:1710.05060.