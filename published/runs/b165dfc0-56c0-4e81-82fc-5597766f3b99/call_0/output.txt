# Policy Functional Decision Theory (P-FDT): Choosing a Whole Mapping from Observations to Actions

## 1. The passage and the problem it raises

Yudkowsky and Soares's paper *Functional Decision Theory* presents its theory mostly in an action-selecting form. The agent intervenes on a variable representing "the output of this decision function on this input" and executes the best action. Twice, however, the authors say this is not their preferred version. Footnote 7 reads:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

Footnote 16, which this essay treats as the primary source, sharpens the point:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

I will call the theory described in that footnote **policy functional decision theory (P-FDT)**. The footnote is two sentences long and contains no equation. My aim is to turn it into a decision procedure precise enough to apply to new cases.

To keep claims separate:
- What the source says is quoted or attributed explicitly.
- I will call the paper's displayed action-selecting equation **A-FDT**. The label is mine; the paper calls it simply "FDT."
- Where I add definitions, assumptions or propositions, I say so.

## 2. Background: A-FDT as surgery on a logical node

The paper treats evidential decision theory (EDT), causal decision theory (CDT) and FDT as expected-utility theories. They differ only in how the agent constructs the hypothetical "what if I chose $a$?" Each agent holds a world-model, which consists of a probability distribution $P$ and, for CDT and FDT, a graph $G$.

- **EDT** conditions on the action.
- **CDT** applies Pearl's operator $\mathtt{do}(\textsc{Act}=a)$ to the physical action node.
- **A-FDT** applies the same operator to a node representing a *logical* fact: the output of the FDT algorithm on the agent's own inputs.

The paper's equation (4) is

$$
\mathrm{FDT}(P,G,x) \coloneqq \operatorname*{argmax}_{a\in\mathcal A}\ \mathbb E\!\left(V \,\middle|\, \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right).
$$

Here $V$ is utility, $\mathcal A$ is a finite action set, and $x$ is the observation history. The underlines denote "dequoting": the node's name is built from the model and the observation.

Two features of equation (4) matter for what follows.

1. **Observations are not conditioned on.** The paper says that "FDT responds to observation by changing which node it intervenes upon." When the observation changes from $x$ to $y$, the intervention moves from $\textsc{fdt}(\underline P,\underline G,\underline x)$ to $\textsc{fdt}(\underline P,\underline G,\underline y)$. The distribution $P$ is not updated on $\textsc{Obs}=x$.
2. **One model contains many output nodes.** The model has a separate node for each input the algorithm might receive. In the transparent Newcomb problem, Fiona's graph contains both $\textsc{fdt}(\underline{P},\underline{G},\textit{full})$ and $\textsc{fdt}(\underline{P},\underline{G},\textit{empty})$. The predictor's prediction controls which one drives $\textsc{Act}$. When Fiona intervenes on the "full" node, she must still hold some belief about the "empty" node. The paper writes $q$ for her "prior probability that she two-boxes upon seeing the box empty," and remarks that "it doesn't matter if Fiona has some uncertainty" about it.

That final remark is where A-FDT and P-FDT come apart. A-FDT changes one entry of the agent's input–output behaviour and holds the other entries at believed values. P-FDT changes all entries at once.

## 3. Defining P-FDT

The footnote's description has three parts:
- the agent "intervenes on the node $\mathrm{FDT}(-)$";
- the chosen value is "a *policy* which maps inputs to actions";
- "the agent then applies her inputs in order to select an action."

The following definition is my formalization of those words.

**Policy space.** Let $\mathcal X$ be the set of observation histories the agent might receive in the problem, and $\mathcal A$ the action set. A (deterministic) policy is a function $\pi:\mathcal X\to\mathcal A$, so the policy space is $\Pi=\mathcal A^{\mathcal X}$.

**Policy node.** The world-model $(P,G)$ contains a node $\Phi=\textsc{fdt}(\underline P,\underline G)$ taking values in $\Pi$. It represents the input–output behaviour of the agent's decision function as a whole. This node has no observation argument, which is exactly the "$\mathrm{FDT}(-)$" of the footnote.

Every node that A-FDT linked to some $\textsc{fdt}(\underline P,\underline G,\underline y)$ is now linked to $\Phi$ through evaluation at $y$:
- the agent's own action becomes $\textsc{Act}=\Phi(\textsc{Obs})$;
- a predictor that simulates the agent on input $y$ reads $\Phi(y)$;
- a copy of the agent that receives input $z$ acts on $\Phi(z)$.

**Decision rule.**

$$
\pi^\star\in \operatorname*{argmax}_{\pi\in\Pi}\ \mathbb E\!\left(V \,\middle|\, \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G)=\pi\big)\right),
\qquad
\text{P-FDT}(P,G,x)\coloneqq \pi^\star(x).
$$

The observation $x$ plays no role in the optimization. It enters only at the end, when the agent "applies her inputs."

Two consequences follow directly from the definition.

1. **The optimization is the same for every input.** Every instance of the agent, whatever it has observed, solves the same problem and so finds the same $\pi^\star$, provided ties are broken the same way (see §6). This is my precise reading of the paper's slogan that FDT agents "act as they would have precommitted to act." If the agent could commit to a policy before seeing anything, she would commit to $\pi^\star$. Seeing $x$ gives her no reason to deviate, because the problem she solves after seeing $x$ is the same one.
2. **A-FDT is coordinate-wise optimization; P-FDT is joint optimization.** Write $U(\pi)=\mathbb E(V\mid \mathtt{do}(\Phi=\pi))$.
   - A-FDT at input $x$ chooses $a$ to maximize $\mathbb E_{\pi_{-x}}\,U(a,\pi_{-x})$, where $\pi_{-x}$ (the other entries) is distributed according to the agent's beliefs.
   - P-FDT maximizes $U$ over the whole product space at once.

The second consequence gives a simple sufficient condition for the two theories to agree. The proposition is my own, though elementary.

> **Proposition.** Suppose $U$ is additively separable across inputs: $U(\pi)=c+\sum_{y\in\mathcal X} h_y(\pi(y))$. Then for every input $x$ and every belief about the other entries, A-FDT's choice maximizes $h_x$. A policy is P-FDT-optimal iff $\pi(y)\in\operatorname{argmax} h_y$ for each $y$. Hence the two theories prescribe the same actions (modulo ties).

*Proof.* Setting entry $x$ to $a$ gives $\mathbb E\,U = c + h_x(a) + \mathbb E\sum_{y\ne x}h_y(\pi(y))$. The last term does not depend on $a$. Maximizing a separable sum is the same as maximizing each summand. ∎

Separability is sufficient but not necessary; the next example is not separable, yet the theories agree. Disagreement requires interaction terms that change which action is best at $x$ depending on what is done at other inputs. The cleanest sources of such terms are environments in which several instances of the same decision function run on different inputs. That is my reconstruction of why the authors say the difference arises "in multi-agent dilemmas."

## 4. Worked example: the transparent Newcomb problem (agreement)

The setup:
- Box A holds \$1,000.
- Box B holds \$1,000,000 iff the predictor predicted that the agent one-boxes upon seeing a full box B.
- The predictor is accurate with probability 0.99.
- Both boxes are transparent, so the observation is $x\in\{\textit{full},\textit{empty}\}$.

A policy is a pair $(a_f,a_e)$: the action on seeing full, and the action on seeing empty. Evaluating each of the four policies under $\mathtt{do}(\Phi=\pi)$:

- **If $a_f=\textit{onebox}$:**
  - With probability 0.99 the prediction is correct, the box is full, and the agent one-boxes: \$1,000,000.
  - With probability 0.01 the box is empty and the agent follows $a_e$: \$1,000 if $a_e=\textit{twobox}$, \$0 otherwise.
  - So $U(\textit{one},\textit{two})=990{,}010$ and $U(\textit{one},\textit{one})=990{,}000$.
- **If $a_f=\textit{twobox}$:**
  - With probability 0.99 the box is empty and the agent follows $a_e$.
  - With probability 0.01 the box is full and the agent two-boxes: \$1,001,000.
  - So $U(\textit{two},\textit{two})=10{,}010+990=11{,}000$ and $U(\textit{two},\textit{one})=10{,}010$.

P-FDT selects $\pi^\star=(\textit{onebox on full},\ \textit{twobox on empty})$. Applying the observation *full* gives *onebox*.

The paper's A-FDT calculation reaches the same verdict. Its expressions are, respectively, $990{,}000+0.01q\cdot 1{,}000$ and $10{,}010+990q$, where $q$ is the believed probability of two-boxing on empty. For every $q\in[0,1]$ the first is larger.

The utility table is not separable: the value of two-boxing on empty is 10 when $a_f=\textit{onebox}$ and 990 when $a_f=\textit{twobox}$. The interaction is too weak, however, to flip the best action at *full*. This supports the source's claim that the distinction "will not make a difference" in the paper's examples.

The calculation also shows concretely what the paper means when it says an FDT agent "should entertain the hypothesis that, if their action were different, they might have *made different observations*." That is the sentence to which footnote 16 is attached. Under $\mathtt{do}(\Phi=(\textit{two},\cdot))$, the agent who is actually looking at a full box assigns probability 0.99 to having seen an empty one. P-FDT makes this structure explicit: the agent evaluates a policy over every observation she could have received, not an action within the observation she happens to have.

## 5. Where policies matter: instances on different inputs

### A coordination game between copies

Two copies of one agent run the same function with the same model $(P,G)$. Copy 1 observes $L$ and copy 2 observes $R$. Each chooses $\alpha$ or $\beta$, and both care about a shared payoff:

| copy L \ copy R | $\alpha$ | $\beta$ |
|---|---|---|
| $\alpha$ | 10 | 0 |
| $\beta$ | 0 | 6 |

**A-FDT.** The copy seeing $L$ intervenes on $\textsc{fdt}(\underline P,\underline G,L)$. The node $\textsc{fdt}(\underline P,\underline G,R)$ is a different node, so it holds that node at its believed distribution. Let $r$ be the believed probability that the $R$-copy plays $\alpha$. Then

$$
\mathbb E V(\alpha)=10r,\qquad \mathbb E V(\beta)=6(1-r),
$$

so A-FDT plays $\alpha$ iff $r>3/8$. The answer depends on the agent's prior about her own behaviour on the other input, and both outcomes can be self-confirming:
- If she believes $r\approx 0$, she plays $\beta$. By symmetry the $R$-copy, believing the same about the $L$-copy, also plays $\beta$. The belief is vindicated at the Pareto-dominated outcome, 6.
- If she believes $r\approx 1$, the same reasoning vindicates $(\alpha,\alpha)$.

A-FDT alone does not say which of these self-consistent belief states is correct. This is an equilibrium-selection problem, reminiscent of the dependence on priors that the paper criticizes in EDT.

**P-FDT.** P-FDT maximizes over the four policies:
- $U(\alpha,\alpha)=10$
- $U(\beta,\beta)=6$
- $U(\alpha,\beta)=U(\beta,\alpha)=0$

It selects $(\alpha,\alpha)$ whatever the prior. Each copy applies its own input and plays $\alpha$. Nothing about the agent's beliefs over her own outputs enters the calculation, because those outputs are exactly what is being intervened on.

### An anti-coordination variant

Now suppose the payoff is 10 iff the copies' outputs *differ*. A-FDT copies with symmetric beliefs face a symmetric problem and may well choose identically, which yields 0. P-FDT finds two optimal policies, $(L\mapsto\alpha,R\mapsto\beta)$ and $(L\mapsto\beta,R\mapsto\alpha)$. Either policy succeeds, because the policy itself breaks the symmetry using the inputs.

There is a catch. Both copies must select the *same* optimal policy. That requires a tie-breaking rule that is part of the shared function, which I take up in §6.

### What "multi-agent" covers

These examples suggest a reading of the footnote's phrase "multi-agent dilemmas." On my reading, it covers any problem in which the outcome depends jointly on the decision function's outputs at several inputs. The two main cases are:
- copies or instances of the agent receiving different observations;
- predictors whose rewards at one input depend on the agent's behaviour at another.

Ordinary single-agent problems with predictors (Newcomb, the transparent Newcomb problem, Parfit's hitchhiker, the blackmail problems) typically involve only weak interaction. The source's hedge "so far as we can tell" should be taken seriously: it is a conjecture about where the theories diverge, not a theorem.

## 6. Questions the footnote leaves open, with proposed resolutions

### (a) Which model names the policy node?

The node is $\textsc{fdt}(\underline P,\underline G)$, so its identity depends on $(P,G)$. In A-FDT the observation was carried separately and $P$ was not updated on it. If an agent instead applied P-FDT with a $P$ already conditioned on $x$, the policy node would differ from input to input. That would recreate the per-input fragmentation that policy selection is meant to remove.

*Proposal.* Use the model that all relevant instances share. In practice this is the agent's model before the observations that distinguish the instances, together with a specification of the input space $\mathcal X$. This fits the paper's practice of leaving $P$ un-updated and is required for the copies in §5 to share a node. It leaves a genuine open question: how should an agent that learns over time pick the "shared" prior when predictors may have modelled different stages of her? The source is silent on this.

### (b) What is the policy domain?

Taking $\Pi=\mathcal A^{\mathcal X}$ over all countable observation histories makes the argmax intractable and possibly undefined.

*Proposal.* Restrict $\mathcal X$ to the inputs that occur with positive probability in the problem as modelled. Note that "occur" here means within some hypothetical $\mathtt{do}(\Phi=\pi)$, not only in the actual world, because the empty-box observation must be included in transparent Newcomb. For finite problems the argmax then exists. Entries at inputs that occur under no policy do not affect $U$ and can be set arbitrarily.

### (c) Tie-breaking

As the anti-coordination game shows, ties among optimal policies are not harmless. Different instances choosing different maximizers can do worse than either maximizer.

*Proposal.* Make tie-breaking part of the function: a fixed canonical order on $\Pi$, known to every instance. This adds nothing to the theory's commitments, since the decision function is supposed to be a fixed mathematical object anyway.

### (d) Randomized policies

The footnote speaks of mappings from inputs to actions, which suggests deterministic policies. If predictors observe the realized policy, then expected utility is linear in any mixture over policies, so some deterministic policy is always optimal. Randomization can matter, though, when two decision points share the same observation, so that a deterministic policy must act identically at both. Imperfect-recall cases such as the absent-minded driver have this structure: an agent who cannot distinguish two intersections can only exit at both or continue at both. Allowing a behavioural policy $\pi:\mathcal X\to\Delta(\mathcal A)$ is a natural extension. It requires a model specifying whether others can predict the random outcome or only the distribution. This is my suggestion; the source does not discuss it.

### (e) Where the dependency graph comes from

P-FDT inherits A-FDT's largest open problem, which the paper states plainly: it is "not yet clear how to construct" a graph describing "how changing the value of a logical variable affects other variables." The policy form arguably makes the requirement more uniform. One no longer needs a separate dependence story for each input-node, only a story about which systems compute or model the agent's function and at which inputs. Even so, P-FDT asks for counterpossible reasoning over $|\mathcal A|^{|\mathcal X|}$ alternatives rather than $|\mathcal A|$, so the computational burden grows sharply.

## 7. How to apply P-FDT to an unfamiliar case

1. **List the inputs.** Enumerate the observation histories $\mathcal X$ that the agent, or any copy of it, could receive under any policy.
2. **Locate every use of the function.** Find each place where the agent's decision function is computed or modelled: the agent's own body, copies, predictors, simulators. Record which input each one is evaluated on.
3. **Build the graph.** Make $\Phi$ a parent of each such place, with the value read off as $\Phi(\text{input})$. Leave merely statistical correlates, such as the smoking lesion, unconnected to $\Phi$. As in the paper's lesion analysis, they are not computing the function.
4. **Evaluate each policy.** For each $\pi$, compute $U(\pi)=\mathbb E(V\mid\mathtt{do}(\Phi=\pi))$, propagating downstream as Pearl's operator prescribes.
5. **Choose and act.** Pick the maximizer, breaking ties by the canonical order, and output $\pi^\star(x)$ for the actual input $x$.

Applied to the paper's other cases, this procedure reproduces its verdicts:
- **Mechanical blackmail.** The policy "refuse when blackmailed" makes blackmail improbable, so it beats "pay when blackmailed."
- **Twin prisoner's dilemma.** Both twins read the same $\Phi$ at the same input, so the comparison is between (cooperate, cooperate) and (defect, defect). Cooperation wins.
- **Smoking lesion.** $\Phi$ has no edge to $\textsc{Cancer}$, so smoking is evaluated as \$1,000 better at no cost.

## 8. Philosophical motivation

The paper's defence of FDT rests mainly on what it calls the "argument from utility": we should prefer the decision procedure whose adopters get more of what they want in fair problems. It also stresses that FDT needs no precommitment devices and is, "so far as we know, reflectively stable in fair problems."

P-FDT carries both themes further. A-FDT already behaves as if precommitted with respect to the input currently being evaluated. P-FDT behaves as if precommitted with respect to its entire input–output behaviour, which is the object predictors and copies actually depend on. The coordination example shows the gap. A-FDT agents can be "stable" at a state that every instance would prefer to leave jointly but none prefers to leave alone. Removing that gap is exactly the job of a joint commitment.

There is also a conceptual tidiness here. The paper distinguishes CDT from FDT by Peirce's type–token distinction: CDT "intervenes on the token," FDT "on the *type*." A-FDT intervenes on one row of the type's truth table. P-FDT intervenes on the type itself, the whole function. If the motivating insight is that what other systems depend on is *which function you are*, the policy form is the more faithful implementation of it.

The costs should be stated just as clearly:
- The counterpossible antecedent "the function's entire table is $\pi$" is, if anything, stranger than the single-entry one.
- The optimization is exponentially larger.
- The theory leans heavily on a well-defined shared prior, which the source never specifies.

## 9. Conclusion

Read through footnote 16, P-FDT is the rule: intervene on the node representing the agent's decision function as a whole, choose the input-to-action mapping $\pi^\star$ that maximizes expected utility under that intervention, then apply one's actual input. Formally, it replaces A-FDT's coordinate-wise optimization over single inputs with joint optimization over the product space $\mathcal A^{\mathcal X}$.

The two theories agree whenever input-wise interactions are absent or weak. A sufficient condition is additive separability, and the paper's examples, such as transparent Newcomb, fall in this region. They diverge when several instances of the function act on different inputs and the payoff couples them, as in coordination between copies. There P-FDT reaches the jointly optimal outcome without depending on the agent's prior about her own behaviour.

The source leaves open which model indexes the policy node, how large the policy domain is, how ties and randomization are handled, and how the dependency graph is obtained. I have proposed natural resolutions for the first four: a shared pre-observation model, a restricted domain, canonical tie-breaking, and behavioural mixing where observations repeat. The fifth remains, as the authors concede, the central open problem for functional decision theories generally.

## References

- Yudkowsky, E. & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060 (footnotes 7 and 16; equations (2)–(4)).
- Pearl, J. (2000). *Causality*. Cambridge University Press.
- Gibbard, A. & Harper, W. (1978). "Counterfactuals and Two Kinds of Expected Utility."
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.