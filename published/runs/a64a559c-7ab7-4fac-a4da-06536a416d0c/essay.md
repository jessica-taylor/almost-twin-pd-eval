# Policy Functional Decision Theory (P-FDT): Choosing a Policy Rather Than an Act

## 1. The source passage and the idea

Yudkowsky and Soares's *Functional Decision Theory: A New Theory of Instrumental Rationality* develops functional decision theory (FDT) mainly in an *action* form. In that form the agent asks which output her decision function should return on the input she actually has. Twice, however, the paper says the authors prefer a different formalization. Footnote 7 says:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

Footnote 16, which I take as the primary source, adds:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

I call the theory these footnotes describe **policy functional decision theory (P-FDT)**. The paper's main-text formulation, which it calls FDT, I call **action-FDT**. I also refer to causal decision theory (CDT) and evidential decision theory (EDT).

The footnotes are short. They tell us three things:

1. The object of choice is a policy, meaning a map from inputs to actions.
2. The choice is made by intervening on a node written $\mathrm{FDT}(-)$. The dash suggests the observation argument has been removed.
3. The agent then applies the chosen policy to her actual input.

They do not say:

- which probability distribution evaluates the policies,
- how ties are broken,
- what the policy space contains,
- exactly when P-FDT and action-FDT diverge.

In what follows I separate what the source says from what I add. My additions are labelled as interpretation or proposal.

## 2. From action-FDT to P-FDT

### 2.1 The action form (source)

The paper's agent holds a world-model $(P, G)$. Here $P$ is a probability distribution over variables, and $G$ is a graph that records causal dependencies and also logical and subjunctive ones. Among the variables is a node $\textsc{fdt}(\underline P, \underline G, \underline x)$, which represents the output of the FDT algorithm on the agent's own model and observation history $x$. The underline means the node's name is built from the values of $P$, $G$, $x$.

Action-FDT is the paper's equation (4):

$$
\mathrm{FDT}(P,G,x) \coloneqq \operatorname*{argmax}_{a\in\mathcal A}\ \mathbb E\left(V \mid \mathtt{do}\left(\textsc{fdt}(\underline P,\underline G,\underline x)=a\right)\right).
$$

The source stresses two features.

- **Where the intervention happens.** The intervention is on a logical node, the output of a function, not on the physical act. Anything that subjunctively depends on that function changes with it. That includes the agent's body, a twin, or a predictor's model of the agent.
- **How observations enter.** Observations are not conditioned on. In the source's words, "FDT responds to observation by changing which node it intervenes upon."

So an action-FDT agent who sees a full box in the transparent Newcomb problem intervenes on $\textsc{fdt}(\underline P,\underline G,\textit{full})$. She treats $\textsc{fdt}(\underline P,\underline G,\textit{empty})$ as a separate node whose value is uncertain but not under her control in this hypothetical.

### 2.2 The policy form (my formalization of footnote 16)

Let $\mathcal X$ be the set of possible inputs (observation histories) relevant to the problem. Let $\Pi = \mathcal A^{\mathcal X}$ be the set of deterministic policies. Footnote 16 tells us to replace the family of per-input nodes $\{\textsc{fdt}(\underline P,\underline G,\underline x)\}_{x\in\mathcal X}$ with a single node $\textsc{fdt}(\underline P,\underline G)$ taking values in $\Pi$. Each per-input output is then a deterministic function of it:

$$
\textsc{fdt}(\underline P,\underline G,\underline x) = \textsc{fdt}(\underline P,\underline G)(x).
$$

P-FDT then prescribes:

$$
\pi^\ast \in \operatorname*{argmax}_{\pi\in\Pi}\ \mathbb E\left(V \mid \mathtt{do}\left(\textsc{fdt}(\underline P,\underline G)=\pi\right)\right),
\qquad
\text{P-FDT}(P,G,x) \coloneqq \pi^\ast(x).
$$

In words, the agent asks: "If this decision function were the function that maps inputs to actions according to $\pi$, how would the whole world go?" She finds the best such $\pi$ and then reads off the entry for the input she actually has. "To which the agent then applies her inputs" is exactly the step $\pi^\ast(x)$.

**The key structural change.** Action-FDT varies one coordinate of the agent's policy, the entry at the actual input, and holds the other coordinates at whatever her prior says. P-FDT varies all coordinates *jointly*. Everything that depends on how the function behaves on any input, such as predictors simulating her on other inputs or copies of her receiving different inputs, moves together in the hypothetical.

A useful corollary follows. In action-FDT calculations the source repeatedly carries a parameter $q$, the agent's prior about how she would act on some other input, and remarks that its value "doesn't matter" in the cases considered. In P-FDT, $q$ is not merely irrelevant: it cannot appear. Every input's output is fixed by the intervention, so the agent's prior beliefs about her own behaviour drop out entirely.

## 3. Worked example: the transparent Newcomb problem

The source's transparent Newcomb problem works as follows.

- Box A contains \$1,000.
- Box B is filled with \$1,000,000 iff the predictor, who is accurate with probability $0.99$, predicts that the agent one-boxes *upon seeing both boxes full*.
- The agent sees box B's contents before acting.

So $\mathcal X=\{\textit{full},\textit{empty}\}$, $\mathcal A=\{1,2\}$ (one or two boxes), and $|\Pi|=4$. Write a policy as $(\pi(\textit{full}),\pi(\textit{empty}))$.

In $G$, the predictor's model depends on $\textsc{fdt}(\underline P,\underline G)(\textit{full})$. With probability $0.99$ the prediction matches that entry. Box B's content determines the observation, and the act is $\pi(\text{observation})$.

| Policy | Predictor accurate (0.99) | Predictor errs (0.01) | Expected value |
|---|---|---|---|
| $(1,1)$ | full, take 1: \$1,000,000 | empty, take 1: \$0 | \$990,000 |
| $(1,2)$ | full, take 1: \$1,000,000 | empty, take 2: \$1,000 | **\$990,010** |
| $(2,1)$ | empty, take 1: \$0 | full, take 2: \$1,001,000 | \$10,010 |
| $(2,2)$ | empty, take 2: \$1,000 | full, take 2: \$1,001,000 | \$11,000 |

The optimum is $\pi^\ast = (1,2)$: one-box on seeing a full box, two-box on seeing an empty one. An agent holding a full box therefore leaves the \$1,000 behind.

This agrees with the source's action-FDT computation. That computation gives $\$990{,}000 + 0.01q\cdot\$1{,}000$ for one-boxing, which equals $\$990{,}010$ at the source's "correct" value $q=1$. The policy formulation simply makes that $q$ a choice variable, and the optimum sets it to 1. The source's statement that the difference does not matter for the problems in its paper is borne out here.

The mechanical blackmail problem works the same way. Suppose the blackmailer wrongly predicts payment with probability $\varepsilon$.

- A paying policy is always blackmailed and loses \$1,000.
- A refusing policy is blackmailed only by error, losing $\varepsilon\cdot\$1{,}000{,}000$ in expectation.

P-FDT therefore refuses whenever $\varepsilon < 0.001$. The source's case $\varepsilon = 0.0009$ falls on the refusing side, with an expected loss of \$900.

## 4. When the formulations diverge

The source asserts that the difference "only matters in multi-agent dilemmas so far as we can tell." It does not say why. The following analysis is mine.

### 4.1 Action-FDT as best response; P-FDT as global optimum

Define $U(\pi) \coloneqq \mathbb E\left(V\mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G)=\pi)\right)$. Make two assumptions:

- **(A1)** The per-input nodes $\textsc{fdt}(\underline P,\underline G,\underline x)$ enter the world-model only as coordinates of the policy node. Intervening on one coordinate is then the same as intervening on the policy node with the other coordinates drawn from $P$.
- **(A2)** The agent is confident about her own behaviour on other inputs. Her marginal over $(\textsc{fdt}(\underline P,\underline G,\underline y))_{y\ne x}$ is a point mass at $\pi_{-x}$.

Under these assumptions action-FDT at input $x$ chooses

$$
\operatorname*{argmax}_{a}\ U(a, \pi_{-x}).
$$

This is a best response in the *common-payoff game* whose players are the agent's "input-selves," one per $x$, all sharing payoff $U$.

- A policy that action-FDT can stably follow, one consistent with its own self-predictions, is a Nash equilibrium of that game.
- P-FDT chooses $\operatorname*{argmax}_\pi U(\pi)$, the global optimum.
- In a common-payoff game the global optimum is always a Nash equilibrium.

So P-FDT selects the *best* of the equilibria available to action-FDT. The two coincide whenever the equilibrium is unique. One sufficient condition is separability, $U(\pi)=\sum_x u_x(\pi(x))$, where each input-self's contribution does not depend on the others.

Separability typically holds when only one instance of the agent is ever actually acting. Each input then corresponds to a mutually exclusive branch, and predictors look at the branch they care about. That is the situation in every dilemma the source analyses.

It fails when instances of the agent that receive *different* inputs act in the same world, so that one input's output affects the payoff from another's. That is plausibly what the authors mean by "multi-agent dilemmas": the agents are copies or close models of one decision function, run on different arguments.

### 4.2 Example: the split-room stag hunt

This example is my own. An agent is duplicated. One copy wakes in room $L$ and the other in room $R$, and each knows which room it is in. Each chooses Stag ($S$) or Hare ($H$). Both copies share one utility function over the joint outcome:

- $(S,S)$ is worth 10,
- $(H,H)$ is worth 6,
- a mismatch is worth 0.

The copies run the same function on different inputs. So in the agent's graph they are the nodes $\textsc{fdt}(\underline P,\underline G,L)$ and $\textsc{fdt}(\underline P,\underline G,R)$.

**Action-FDT in room $L$.** Let $r$ be the agent's credence that the $R$-copy plays $S$. Then

$$
\mathbb E[V \mid \mathtt{do}(\textsc{fdt}(\ldots,L)=S)] = 10r, \qquad \mathbb E[V \mid \mathtt{do}(\textsc{fdt}(\ldots,L)=H)] = 6(1-r).
$$

She hunts stag iff $r > 3/8$. If she expects "herself in the other room" to play $H$, she plays $H$. The copy in room $R$ reasons symmetrically, so $(H,H)$ is self-fulfilling and stable. Nothing in action-FDT dislodges it.

**P-FDT.** The four policies have values

$$
U(S,S)=10,\quad U(S,H)=0,\quad U(H,S)=0,\quad U(H,H)=6.
$$

So $\pi^\ast=(S,S)$. Each copy computes the same $\pi^\ast$ and applies it to its own room label. Both hunt stag.

The intuition is the source's own twin reasoning, extended. The copies are not twins in the narrow sense, since they are evaluating the function at different arguments. They are, however, implementations of the same *function*, and P-FDT intervenes on the function as a whole, not on one of its values.

## 5. Questions the footnote leaves open

### 5.1 Which distribution evaluates policies?

The dash in "$\mathrm{FDT}(-)$" removes $x$ from the node's name, but nothing in the footnote says whether $P$ has already been conditioned on $x$. This choice matters a great deal.

Suppose we evaluate policies by $\mathbb E(V\mid \mathtt{do}(\textsc{fdt}=\pi), \textit{Obs}=\textit{full})$ in the transparent Newcomb problem.

- Under policies with $\pi(\textit{full})=1$, a full box mostly arises because the predictor was right. The conditional value is \$1,000,000.
- Under policies with $\pi(\textit{full})=2$, a full box arises only through predictor error. Given that it is full, the agent gets \$1,001,000.

The conditional evaluation therefore prefers two-boxing. It undoes the very behaviour the theory is meant to secure.

This is the "double update" the source attributes to Timeless Decision Theory: "conditioning on evidence *and* changing the place where one intervenes." The source contrasts that with Updateless Decision Theory, whose name reflects FDT's "apparent 'lack of updating'."

**Proposal.** P-FDT should evaluate policies with a distribution that is *not* conditioned on the observations in the policy's domain. Observations enter only through the final step $\pi^\ast(x)$.

Operationally, fix a vantage point: the epistemic state the agent had (or would have) before the observations in $\mathcal X$ arrive. Use that $P$ throughout. The resulting policy is the one the agent would have precommitted to from that vantage. P-FDT thereby makes literal the source's slogan that "FDT agents simply act as they would have ideally precommitted to act."

The choice of vantage point is itself a modelling decision. In practice I suggest taking the point at which the problem's structure became known, which is typically before the predictor acts. I flag this as the least settled part of the reconstruction. An agent who keeps learning must decide which past state's priors still govern.

### 5.2 Ties

The argmax may contain several policies that disagree on the actual input. Take the anti-coordination variant of §4.2: payoff only for mismatched choices. Then $(S,H)$ and $(H,S)$ are both optimal. If the two copies broke the tie differently, for instance by independent coin flips, they could fail.

**Proposal.** The tie-break must be part of the function. Fix a canonical order on $\Pi$, such as lexicographic order, and take the first maximizer. Every instance that computes the same function then lands on the same $\pi^\ast$, and coordination is preserved. This is a natural extension of the source's insistence that the decision function is a "fixed mathematical function" and that the outputs of fixed functions agree across implementations.

### 5.3 The policy space

$\Pi=\mathcal A^{\mathcal X}$ grows exponentially in $|\mathcal X|$. With histories as inputs it is enormous, which makes P-FDT even less tractable than action-FDT in idealized form. The source already concedes the idealization, observing that "maximizing over all possible actions is not realistic." Two choices remain open.

- **Mixed policies.** Should P-FDT allow maps $\mathcal X\to\Delta(\mathcal A)$? In the anti-coordination case, randomization does worse than deterministic symmetry breaking via input labels. Whether a predictor sees the coin flip is a modelling fact that $G$ must specify. I treat deterministic policies as the default. Randomized ones are added only when the problem gives the agent randomness that the relevant predictors cannot see.
- **Which inputs belong in $\mathcal X$.** Fortunately the result is insensitive here. Adding inputs that no instance or predictor ever acts on cannot change the optimal entries on the inputs that do matter, so $\mathcal X$ can be taken to be the inputs some modelled process might evaluate the function on.

### 5.4 Building $G$

The source calls the construction of subjunctive-dependence graphs "perhaps the largest open problem" for FDT. P-FDT inherits it and slightly sharpens the requirement. $G$ must say which features of the world depend on which *entries* of the policy.

- In transparent Newcomb, the box depends on $\pi(\textit{full})$, not on $\pi(\textit{empty})$.
- A predictor that simulates the agent on an input it never shows her depends on that entry.

Getting these arrows wrong changes the answer. That is the main place where applying P-FDT requires judgement rather than calculation.

## 6. A recipe for applying P-FDT

To decide an unfamiliar case:

1. **Fix the vantage point.** Choose the prior $P$ from before the observations in question (§5.1).
2. **List the inputs** $\mathcal X$ on which any relevant process might run the agent's function: her own body on each possible observation, copies, and predictors' simulations.
3. **Draw $G$.** Make a node $\textsc{fdt}(\underline P,\underline G)$ with values in $\Pi$. Draw arrows from it to every act, copy and prediction, and annotate which entry $\pi(x)$ each depends on. Statistical correlates that merely co-vary with the agent, such as the lesion in the smoking lesion problem, get no arrow.
4. **Score each policy.** For each $\pi$, set the node to $\pi$, propagate through $G$, and compute $U(\pi)$.
5. **Choose and apply.** Take the canonically first maximizer $\pi^\ast$ and output $\pi^\ast(x)$ for the actual input $x$.

Run on the source's dilemmas, the recipe returns the source's verdicts:

- one-box in Newcomb's problem,
- smoke in the smoking lesion problem,
- pay in Parfit's hitchhiker,
- one-box facing a full transparent box,
- refuse both blackmails (the XOR blackmail and the mechanical blackmail),
- cooperate with a twin.

In each of these, separability holds and the optimum is the unique stable point of action-FDT. P-FDT goes beyond action-FDT only in problems like §4.2. There, separate instances of one function act on different inputs in a shared world, and P-FDT secures the best joint outcome where action-FDT can get stuck at a worse self-consistent one.

## 7. Conclusion

Footnote 16 says the authors' preferred FDT "intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a policy," and then applies the agent's input. I formalize P-FDT as

$$
\text{P-FDT}(P,G,x) = \Big[\operatorname*{argmax}_{\pi} \mathbb E\big(V\mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G)=\pi)\big)\Big](x).
$$

Under this formalization:

- Action-FDT corresponds to coordinatewise best response within a common-payoff game among the agent's input-selves, and P-FDT picks that game's global optimum.
- The two agree in single-instance problems. This vindicates the source's remark that the difference matters only in multi-agent settings.
- They diverge when several instances of the function act on different inputs in a shared world.

Three choices are not settled by the footnote. I argued for:

- evaluating policies from a prior not updated on the observations they map, since conditioning produces the double update the source warns against;
- a canonical tie-breaking rule built into the function;
- deterministic policies by default.

With those choices, P-FDT turns the source's guiding idea, act as you would have committed to act, into a precise optimization over policies.

## References

- Yudkowsky, E., and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality* (arXiv:1710.05060), especially footnotes 7 and 16, equation (4), and sections 6 and 9.