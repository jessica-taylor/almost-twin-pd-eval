# Choosing the Function, Not the Act: An Essay on Policy Functional Decision Theory (P-FDT)

## 1. The footnote and the theory it names

In "Functional Decision Theory: A New Theory of Instrumental Rationality," Yudkowsky and Soares develop functional decision theory around a single equation. The agent intervenes on a variable representing *the output of her own decision function on her current input*. In two footnotes they say that this is not quite the version they prefer. Footnote 16, which I take as the primary source here, reads in full:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

Footnote 7 adds that "agents actually iterate over *policies* (mappings from observations to actions) rather than actions," and that this "makes a difference in certain multi-agent dilemmas."

I will call the theory described in footnote 16 **policy functional decision theory (P-FDT)**. I will call the version the paper actually formalizes in its equation (4) **action-FDT**. I also discuss causal decision theory (CDT) and evidential decision theory (EDT) by those names.

The footnote is two sentences long. It fixes three things:
- the object of choice (a policy, i.e., a map from inputs to actions);
- the mechanism (intervention on the node representing the decision function);
- the final step (apply the policy to one's actual input).

It leaves open which probability distribution the policy is evaluated under, how the policy node connects to the rest of the world-model, how large the policy space is, how ties and randomization are handled, and why the difference should arise "only" in multi-agent cases. This essay:
- reconstructs P-FDT mathematically;
- proposes operational answers to those open questions, marked as my own;
- explains exactly when and why P-FDT and action-FDT come apart.

## 2. Background: action-FDT and its counterfactuals

The paper places EDT, CDT and FDT in one template. Each theory maximizes expected utility, but each interprets the decision-hypothetical "if I did $a$" differently.

- **EDT** conditions: $\mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a)$.
- **CDT** performs a Pearl-style intervention on the physical act: $\mathbb E(V \mid \mathrm{do}(\textsc{Act}=a), \textsc{Obs}=x)$.
- **Action-FDT** intervenes on a *logical* variable. The agent's world-model $(P,G)$ contains a node $\textsc{fdt}(\underline P,\underline G,\underline x)$ standing for the output of the FDT algorithm on the agent's own model and observation. The theory prescribes

$$\mathrm{FDT}(P,G,x) \coloneqq \operatorname*{argmax}_{a\in\mathcal A}\ \mathbb E\big(V \,\big|\, \mathrm{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)\big). \tag{1}$$

The graph $G$ encodes *subjunctive dependence*: which things would differ if this mathematical function had a different output. A predictor's prediction depends subjunctively on the agent's function. A carcinogenic lesion does not.

The paper offers a slogan for this: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." Intervening on the function rather than the act is what makes the agent one-box in Newcomb's problem while still smoking in the smoking lesion problem.

Equation (1) has a feature that matters for everything that follows. The paper says that action-FDT "responds to observation by changing which node it intervenes upon." It does not condition on the observation. On seeing $x$, it intervenes on $\textsc{fdt}(\ldots,\underline x)$. On seeing $y$, it would intervene on a *different* node, $\textsc{fdt}(\ldots,\underline y)$.

In the transparent Newcomb problem, Fiona (the paper's action-FDT agent) intervenes on the "full" node. She treats her behavior on the "empty" node as a fixed unknown, with prior probability $q$ of two-boxing.

So action-FDT treats the function's behavior on *other* inputs as background held fixed. That is the opening P-FDT closes.

## 3. Defining P-FDT

### 3.1 The core equation

Let $\mathcal X$ be the set of inputs the decision function might receive in the problem, and let $\mathcal A$ be the action set. A (deterministic) policy is a map $\pi:\mathcal X\to\mathcal A$. Write $\Pi=\mathcal A^{\mathcal X}$ for the set of all policies.

Following footnote 16, the world-model contains a single node $\textsc{fdt}(\underline P,\underline G)$ whose values are policies. It stands for "what the decision function does, as a whole, on every input." P-FDT is then:

$$\pi^* \in \operatorname*{argmax}_{\pi\in\Pi}\ \mathbb E\big(V \,\big|\, \mathrm{do}(\textsc{fdt}(\underline P,\underline G)=\pi)\big), \qquad \text{P-FDT}(P,G,x) \coloneqq \pi^*(x). \tag{2}$$

The two stages track the footnote's wording exactly. First, "intervenes … to choose not an action but a *policy*". Second, "to which the agent then applies her inputs in order to select an action".

### 3.2 How the policy node feeds the graph

For (2) to mean anything, $G$ must say how the policy node reaches the rest of the world. The paper's figures show the pattern for action-FDT. In the transparent Newcomb graph, $\textsc{Act}$ is fed by both observation-indexed nodes, with $\textsc{Prediction}$ "determining which of the two $\textsc{fdt}$ variables controls $\textsc{Act}$."

The natural policy-level generalization, which is my reconstruction, is this. For every *instance* $k$ of the decision function in the world, add a structural equation

$$\textsc{Act}_k = \textsc{fdt}(\underline P,\underline G)\big(\textsc{Obs}_k\big)$$

or a noisy version of it. Instances include:
- the agent's body at each decision point;
- a twin or copy;
- the simulation inside a predictor's head.

Here $\textsc{Obs}_k$ is whatever input that instance receives. A predictor who simulates the agent on input $x_{\text{pred}}$ has $\textsc{Prediction} = \textsc{fdt}(\underline P,\underline G)(x_{\text{pred}})$, perturbed by an $\textsc{Accurate}$-style noise variable.

Intervening on the policy node therefore changes, at once and consistently, every instance's behavior on every input. Everything not subjunctively downstream (lesions, physical constants, other people's independent choices) is held fixed, as in CDT.

### 3.3 Which distribution? The updatelessness question

The most consequential open question is which distribution $P$ appears in (2). Two readings are possible.

- **(U) Updateless reading.** Evaluate policies under the agent's model *before* the problem's observations. The observation $x$ enters only at the application step $\pi^*(x)$.
- **(C) Conditioned reading.** Evaluate $\mathbb E(V\mid \mathrm{do}(\textsc{fdt}=\pi), \textsc{Obs}=x)$, conditioning on the observation as well.

I adopt (U), for three reasons.

1. **The text.** The footnote says the agent "then applies her inputs." That phrasing places the inputs after policy selection, not inside it.
2. **The paper's architecture.** Action-FDT already refuses to condition on observations. The paper says observations work by switching the intervention point. A policy node has no observation index to switch, so the only role left for $x$ is the application step.
3. **Reading (C) breaks the theory's signature verdicts.** Condition on "box B is full" after intervening on a policy that two-boxes on full. With a reliable predictor, you are now conditioning on the predictor's rare error, so two-boxing looks attractive.

On the third point, the paper itself warns that conditioning on evidence *and* changing the intervention point "creates a kind of 'double update' which proves harmful in practice." It says this about Timeless Decision Theory, in a passage marked in the source as a draft note.

Reading (U) raises a residual question: *how early* is "before"? Agents arrive at every problem with a lifetime of updates already absorbed. My operational proposal is to use the model as it stood when the relevant dependents first modeled the agent's function. In practice this means the model at the start of the problem, before any problem-internal observations. For the standard dilemmas this is unambiguous. For problems whose stakes were set by predictions made long ago, it is a real choice, and the source does not resolve it.

## 4. Worked examples

### 4.1 Transparent Newcomb: P-FDT agrees with action-FDT

The setup:
- Inputs are $\mathcal X=\{\textit{full},\textit{empty}\}$.
- The predictor simulates the agent on input *full* and is accurate with probability $0.99$.
- Box B is filled iff the prediction is "one-box."

Each policy is a pair $(\pi(\textit{full}),\pi(\textit{empty}))$. Under $\mathrm{do}(\textsc{fdt}=\pi)$, the expected values are:

| Policy | Accurate (0.99) | Inaccurate (0.01) | Expected value |
|---|---|---|---|
| (one, two) | full → one-box → \$1,000,000 | empty → two-box → \$1,000 | \$990,010 |
| (one, one) | \$1,000,000 | empty → one-box → \$0 | \$990,000 |
| (two, two) | empty → two-box → \$1,000 | full → two-box → \$1,001,000 | \$11,000 |
| (two, one) | empty → one-box → \$0 | full → two-box → \$1,001,000 | \$10,010 |

The optimum is $\pi^*=(\text{one-box on full},\ \text{two-box on empty})$. An agent who sees two full boxes applies $\pi^*$ and leaves the \$1,000 behind.

This reproduces the paper's action-FDT calculation, \$990,000 + 0.01q·\$1,000 with $q=1$. The difference is that the "correct value of $q$," which the paper invites the reader to verify, is now *computed* as part of the policy rather than supplied as a prior.

### 4.2 Mechanical blackmail with a fallible predictor

The setup:
- The blackmailer runs the incriminating program if she predicts the agent pays.
- With probability $\varepsilon$ she wrongly predicts payment.
- Publication costs \$1,000,000.
- Paying costs \$1,000.

The relevant policies are "pay if blackmailed" and "refuse if blackmailed."
- "Pay" gets blackmailed essentially always, so it loses \$1,000.
- "Refuse" is blackmailed only by error, so it loses $\varepsilon\cdot\$1{,}000{,}000$ in expectation.

P-FDT refuses iff $\varepsilon < 0.001$. With the paper's $\varepsilon=0.0009$, refusing costs \$900 in expectation against \$1,000 for paying, so the agent refuses even while holding the letter. This matches the source.

One discrepancy deserves mention. The source then says that with an error rate of "0.011%" the agent pays. By the arithmetic above the threshold is $0.1\%$, so an error rate of $0.011\%$ would still favor refusal. I read the source's second figure as a slip, probably for something like $0.11\%$.

In single-agent cases like these, P-FDT and action-FDT agree. The next example shows where they come apart.

### 4.3 Where the two diverge: copies with different inputs

Two exact copies of an agent run the same decision function. A referee shows copy 1 the label "1" and copy 2 the label "2." Each chooses $L$ or $R$, and both receive the same payoff:

$$U = \begin{cases} 10 & \text{copy 1 plays } L,\ \text{copy 2 plays } R,\\ 5 & \text{copy 1 plays } R,\ \text{copy 2 plays } L,\\ 0 & \text{otherwise.}\end{cases}$$

**P-FDT.** The agent evaluates the four policies $(\pi(1),\pi(2))$: $(L,R)$ scores 10, $(R,L)$ scores 5, and the others score 0. She picks $(L,R)$. Copy 1 applies it to input 1 and plays $L$; copy 2 applies it to input 2 and plays $R$. The payoff is 10, with no communication.

**Action-FDT.** Copy 1 intervenes on the node $\textsc{fdt}(\ldots,\underline 1)$. She holds $\textsc{fdt}(\ldots,\underline 2)$ fixed at her prior $q = P(\text{copy 2 plays } R)$. Her expected values are $\mathrm{EU}(L)=10q$ and $\mathrm{EU}(R)=5(1-q)$, so she plays $L$ iff $q>1/3$. Copy 2 reasons symmetrically with $r=P(\text{copy 1 plays }L)$ and plays $R$ iff $r>1/3$.

Suppose both start with $q=r=0.2$. Then copy 1 plays $R$, copy 2 plays $L$, and the payoff is 5. These beliefs are not even refuted, because each copy's prediction of the other's play comes true.

With $q=0.2$ and $r=0.5$, both play $R$ and the payoff is 0.

Action-FDT's outcome thus depends on priors about the function's own behavior on other inputs. This is a mild echo of the dependence on priors the paper criticizes in EDT. P-FDT has no such dependence.

This is exactly the kind of "multi-agent dilemma" the footnotes gesture at. The copies are distinct agents that share one function but receive different inputs.

If the copies received the *same* input, a policy would reduce to an action and the two theories would coincide. What creates the gap is distinct inputs, not multiple bodies.

## 5. The precise relationship between P-FDT and action-FDT

Footnote 16 asserts that the difference "only matters in multi-agent dilemmas so far as we can tell." Here is a way to make that claim exact. This is my own analysis, not the source's.

**Observation (coordinate-wise vs. global optimality).** Fix a model in which the policy node determines all instances, as in §3.2. Suppose action-FDT's beliefs about its behavior on other inputs are point masses at the values $\pi(y)$ for $y \ne x$. Then intervening on the $x$-node with value $a$ produces the same hypothetical as intervening on the policy node with $\pi[x\mapsto a]$, i.e., $\pi$ with its $x$-coordinate replaced by $a$. Therefore:

1. If $\pi^*$ maximizes (2), then $\pi^*(x)$ maximizes action-FDT's objective at every $x$, given point-mass beliefs at $\pi^*$. Global optima are self-consistent action-FDT states.
2. The converse fails. A policy can be a *coordinate-wise* optimum, meaning no single-input change improves it, without being a global optimum. The policy $(R,L)$ in §4.3 is an example.

So action-FDT is coordinate ascent on the policy landscape: a Nash equilibrium among the function's own input-indexed nodes. P-FDT is global maximization over that landscape. The two can diverge only when the expected-utility landscape over $\Pi$ has more than one coordinate-wise optimum. That requires strong interaction between what the function does on different inputs, i.e., value depending jointly on $\pi(x)$ and $\pi(y)$.

When is such interaction strong enough to produce multiple local optima?
- **Single-agent prediction problems** (Newcomb, transparent Newcomb, blackmail) usually have weak interaction. In transparent Newcomb, $\pi(\textit{empty})$ matters only through the 1% error branch, so the landscape has a single peak.
- **Problems with several simultaneously active instances on different inputs** (copies, coordination games among same-algorithm agents, voting coalitions) produce genuine joint terms and multiple equilibria.

That fits the footnote's "so far as we can tell." My own extension is that the same structure can arise *intrapersonally*. An agent's selves at different times, receiving different observations, are instances of one function with different inputs. The paper's gym example points this way. Under P-FDT, the sequence of choices is optimized as one plan rather than as an equilibrium among time-slices. I flag this as a reasonable reading, not a claim the footnote makes.

## 6. Further open choices and my proposals

**Size of the policy space.** The paper allows countable observation sets, so $\mathcal A^{\mathcal X}$ may be uncountable and the argmax may not exist. Operationally, I restrict $\mathcal X$ to the inputs any instance of the function could receive *in the modeled problem*. For bounded agents, one should search a structured subfamily (threshold rules, finite automata) and accept approximate optimality.

**Randomization.** The source never discusses mixed policies. My proposal is to treat any randomness source as part of the input. A coin flip becomes a component of $x$, and the policy maps (observation, coin) to actions. Whether predictors can see the coin is then a modeling question about $G$, and Death-in-Damascus-style cases are settled by what the graph says about that coin.

**Ties.** In the symmetric version of §4.3, where $(L,R)$ and $(R,L)$ both pay 10, P-FDT needs a tie-break. Because every copy computes the same argmax, any *deterministic* tie-breaking rule shared by the function coordinates the copies automatically. A randomized tie-break would not. I therefore recommend a fixed canonical ordering of $\Pi$ as part of the function's specification.

**Self-reference.** The node $\textsc{fdt}(\underline P,\underline G)$ refers to the function being computed. The paper's remark carries over unchanged: the agent need not know the node's value to represent it, and quining (Kleene's recursion theorem) makes this coherent.

**Counterpossibles.** The policy node takes values that are, in fact, logically impossible, since the function has only one actual output on each input. P-FDT therefore inherits FDT's main acknowledged gap: there is no general account of how to build $G$, the structure of subjunctive dependence. Moving from actions to policies makes the counterpossible antecedent larger, a whole function instead of one output. It does not make it worse in kind.

## 7. Philosophical motivation, sharpened by policies

The paper's case for FDT rests on three arguments: from precommitment, from the value of information, and from utility. P-FDT turns each into something close to a definition.

**Precommitment.** The paper says FDT agents "simply act as they would have ideally precommitted to act." Under the updateless reading, choosing $\pi^*$ *is* choosing the best ex-ante contingency plan, and then executing it on whatever input arrives. There is no gap between the plan one would bind oneself to and the act one performs. This is also why P-FDT has no incentive to self-modify mid-problem: any modification is just another policy, and it was already in the argmax.

**Value of information.** Suppose the environment depends on the agent only through the function's behavior (the paper's informal notion of "fair" problems), and the agent is offered an extra observation.

Every old policy can be simulated by a new policy that ignores the extra observation. That simulating policy induces the same behavior at every instance, so it yields the same outcome distribution. The maximum over the enlarged policy space is therefore at least the old maximum. This is my derivation, but it formalizes the paper's claim that functional decision theorists "do not assign negative expected value to information." It also shows where the claim needs the fairness assumption: an environment that rewards *not having seen* something, regardless of behavior, could break it.

**Utility.** The paper's ultimate standard is how much utility agents of a given type obtain. A P-FDT agent maximizes, by construction, the expected utility of the function's behavior across all its instances. The §4.3 example shows that this standard favors P-FDT over action-FDT in exactly the cases where they differ.

## 8. A procedure for unfamiliar cases

To apply P-FDT to a new problem:

1. **List instances.** Identify every place the decision function is computed or accurately modeled: the agent's body at each decision point, copies, and predictors' simulations. Record each instance's input.
2. **Fix the input set** $\mathcal X$ as the union of those inputs, and the policy space $\Pi=\mathcal A^{\mathcal X}$.
3. **Build $(P,G)$.** Use the pre-observation model. Write $\textsc{Act}_k=\pi(\textsc{Obs}_k)$ for each instance, with noise for imperfect predictors. Leave lesion-like correlates outside the policy node's influence.
4. **Score each policy** by $\mathbb E(V\mid \mathrm{do}(\textsc{fdt}=\pi))$, propagating only along subjunctive-dependence edges.
5. **Choose $\pi^*$** with a fixed deterministic tie-break, then **act** $\pi^*(x)$ on the observed input.
6. **Sanity check.** If one instance and one input are in play, the answer should match action-FDT. If not, look for coordination gains that action-FDT would miss.

## 9. Conclusion

Footnote 16 changes the object of the FDT intervention from an act to a whole input–output map. On the reading developed here, the change has three consequences:

- **It makes updatelessness explicit.** Observations select which entry of the chosen policy to execute; they are not evidence to condition on.
- **It reveals action-FDT as coordinate-wise optimization** over the function's behavior on different inputs. P-FDT is global optimization over the same landscape.
- **It locates the divergence.** The two theories agree whenever that landscape has a unique local optimum, as in the paper's single-agent dilemmas. They come apart when distinct instances on distinct inputs must coordinate, as with copies and same-algorithm agents. That matches, and explains, the footnote's remark that the difference matters in multi-agent dilemmas.

What remains open is what was open for FDT generally: how to construct the graph of subjunctive dependencies, and how to reason about counterpossible outputs of one's own function. P-FDT does not solve those problems. Given a model, though, it states clearly what to compute.

**References**

- Yudkowsky, E. & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality.* arXiv:1710.05060 (footnotes 7 and 16; equation 4).
- Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Pearl, J. (2000). *Causality.* Cambridge University Press.