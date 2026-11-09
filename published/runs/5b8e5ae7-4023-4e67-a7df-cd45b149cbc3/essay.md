# Policy Functional Decision Theory (P-FDT): Choosing the Function, Not the Output

## 1. The source and what it says

Yudkowsky and Soares's paper *Functional Decision Theory* (FDT) presents its theory mainly as a rule for choosing **actions**. In two footnotes, though, the authors say their preferred version of the theory chooses **policies**. Footnote 7 reads:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

Footnote 16, which this essay takes as its primary source, states:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

I will call the theory described there **P-FDT** (policy functional decision theory). To keep the comparison clear, I will call the theory defined by the paper's displayed equation (4) **action-FDT**. That label is mine, not the paper's.

Footnote 16 fixes four things:

1. The point of intervention is a node representing the decision function's output.
2. The value chosen at that node is a policy, meaning a map from inputs to actions.
3. The action is obtained afterwards, by applying the chosen policy to the agent's actual input.
4. The authors believe the difference from action-FDT shows up only in multi-agent problems.

It leaves several things open:

- whether the expectation used to rank policies is conditioned on the current observation;
- what the domain of a policy is;
- whether policies may be randomized;
- how to build the dependency graph for a policy-valued node.

The rest of this essay reconstructs P-FDT mathematically, works examples, and proposes answers to the open questions. I flag throughout which claims come from the source and which are my own.

## 2. Background: FDT as surgery on a logical node

The paper frames all expected-utility theories as maximizing
$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),$$
where the theories differ in how they read the hypothetical connective "$\hookrightarrow$":

- **Evidential decision theory (EDT)** conditions on the action.
- **Causal decision theory (CDT)** performs Pearl's intervention $\mathtt{do}(\textsc{Act}=a)$ in a causal graph.
- **FDT** performs the intervention on a variable representing the output of the FDT algorithm itself.

The agent's world-model is a pair $(P, G)$. Here $P$ is a probability distribution, and $G$ is a graph encoding "logical, mathematical, computational, causal, etc." dependencies. Action-FDT is defined as

$$\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A} \mathbb E\big(V \,\big|\, \mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)\big). \tag{4}$$

The underlines denote dequoting: $\textsc{fdt}(\underline P,\underline G,\underline x)$ is the variable whose value is whatever the FDT algorithm outputs on those arguments.

The paper notes a structural feature of (4) that becomes central below. Action-FDT does not respond to an observation by conditioning on it. Instead, when the observation history changes from $x$ to $y$, the agent "changes from intervening on the variable $\textsc{fdt}(\underline P,\underline G,\underline x)$ to $\textsc{fdt}(\underline P,\underline G,\underline y)$ instead."

This design choice is what produces the paper's results in the transparent Newcomb problem and the blackmail problems. In those problems, an agent holding a full box or a blackmail letter imagines that, had her function output something else, she would probably not have seen what she sees.

There is a catch. Under action-FDT, the outputs of the function on *other* inputs, $\textsc{fdt}(\underline P,\underline G,\underline y)$ for $y\neq x$, are not intervened on. They remain ordinary uncertain variables, and the agent needs beliefs about them. In the transparent Newcomb analysis the paper introduces exactly such a belief: "Write $q$ for Fiona's prior probability that she two-boxes upon seeing the box empty." It then remarks that the correct $q$ is 1 but "it doesn't matter." P-FDT can be read as the proposal to stop treating these other-input outputs as beliefs and to choose them all jointly.

## 3. Definition of P-FDT

**Setup.** Let $\mathcal X$ be a set of possible inputs (observation histories) and $\mathcal A$ a finite action set. A **policy** is a function $\pi:\mathcal X\to\mathcal A$. Write $\Pi=\mathcal A^{\mathcal X}$ for the set of all such functions.

The agent's model $(P,G)$ contains a single policy-valued variable $\textsc{fdt}(\underline P,\underline G)$. Its value is the policy computed by the P-FDT algorithm on inputs $(P,G)$. Note that $x$ is absent from this variable's name.

The graph $G$ specifies which other variables depend on this node, and on which parts of it. For example:

- the agent's own action $\textsc{Act}$ is computed as $\pi(\textsc{Obs})$;
- a predictor's prediction is computed from some evaluation of $\pi$, which may look at one component $\pi(y)$ or at the whole function.

**Policy value.** For each $\pi\in\Pi$, define
$$U(\pi) := \mathbb E\big(V \,\big|\, \mathtt{do}(\textsc{fdt}(\underline P,\underline G)=\pi)\big).$$

**Decision rule.** On input $x$:
$$\pi^* \in \arg\max_{\pi\in\Pi} U(\pi), \qquad \text{P-FDT}(P,G,x) := \pi^*(x).$$

Steps (i)–(iii) of the source's description correspond directly to this definition: intervene on the function node, choose a policy, apply the policy to the input. The one substantive interpretive choice I have made is that **$U(\pi)$ is not conditioned on $\textsc{Obs}=x$**. Section 6 defends it. With this reading, the observation plays no role in *evaluating* options. It enters only when the chosen policy is *executed*.

**Bookkeeping relation to action-FDT (my reformulation).** Suppose the graph is built so that the per-input variables $\textsc{fdt}(\underline P,\underline G,\underline y)$ are just the components $\pi(y)$ of the policy node. Then action-FDT at input $x$, holding beliefs $\beta$ about the other components $\pi_{-x}$, computes
$$\mathbb E_{\pi_{-x}\sim\beta}\, U(a,\pi_{-x}).$$
This is the policy value with one coordinate chosen and the others integrated out under the agent's self-beliefs. P-FDT maximizes over all coordinates at once.

## 4. A single-agent example: transparent Newcomb under P-FDT

This is the paper's transparent Newcomb problem. Box A holds \$1,000. Box B is filled with \$1,000,000 iff the predictor predicts the agent will one-box upon seeing it full. The prediction is accurate with probability 0.99.

Inputs are $\mathcal X=\{\textit{full},\textit{empty}\}$, and there are four policies. Write $\pi=(\pi(\textit{full}),\pi(\textit{empty}))$.

- **$\pi(\textit{full})=\textit{one}$.**
  - With probability 0.99 the predictor is right, box B is full, and the agent one-boxes: \$1,000,000.
  - With probability 0.01 box B is empty, and the agent plays $\pi(\textit{empty})$: \$1,000 if she two-boxes, \$0 if she one-boxes.
  - So $U(\textit{one},\textit{two})=990{,}010$ and $U(\textit{one},\textit{one})=990{,}000$.
- **$\pi(\textit{full})=\textit{two}$.**
  - With probability 0.99 box B is empty, and she plays $\pi(\textit{empty})$.
  - With probability 0.01 box B is full, and she two-boxes for \$1,001,000.
  - So $U(\textit{two},\textit{two})=10{,}010+990=11{,}000$ and $U(\textit{two},\textit{one})=10{,}010$.

The maximizer is $\pi^*=(\textit{one},\textit{two})$. Seeing a full box, the P-FDT agent one-boxes, which matches action-FDT.

The useful comparison is with the paper's own formula, $990{,}000+0.01q\cdot 1{,}000$. That expression contains a belief $q$ about what the agent would do on an input she did not receive. In P-FDT, $q$ is not a belief at all. It is a decision variable, set to its optimal value ($q=1$) as part of the same maximization.

In this problem nothing turns on that difference, because action-FDT's choice at *full* is optimal for every $q\in[0,1]$. That is an instance of the source's claim that the distinction makes no difference in the paper's examples.

The mechanical blackmail problem works the same way. With inputs $\{\textit{letter},\varnothing\}$ and a blackmailer who falsely predicts payment with probability 0.0009:

- every policy with $\pi(\textit{letter})=\textit{pay}$ has value $-1{,}000$ (blackmailed for sure, then pays);
- every policy with $\pi(\textit{letter})=\textit{refuse}$ has value $-0.0009\times 1{,}000{,}000=-900$.

So P-FDT refuses, as the paper's FDT agent does.

## 5. Why the two theories can diverge

### 5.1 Person-by-person versus joint optimality

The relation between the theories has a familiar shape from team decision theory. This framing is mine, not the source's.

- A policy $\pi$ is **jointly optimal** if it maximizes $U$ over $\Pi$.
- A policy $\pi$ is **person-by-person optimal** if, for each input $x$, the component $\pi(x)$ maximizes $U(a,\pi_{-x})$ over $a$.

Person-by-person optimality is a Nash-equilibrium condition among the agent's own input-indexed instances. Joint optimality is optimality of the whole team. A self-consistent action-FDT agent, whose beliefs about its other-input outputs are correct and deterministic, implements a person-by-person optimal policy. Two observations follow.

**Proposition (my own, elementary).**
(a) Every jointly optimal policy is person-by-person optimal. So if action-FDT's self-beliefs match a jointly optimal $\pi^*$, action-FDT is permitted to choose $\pi^*(x)$ at every $x$, and in that sense the two theories agree.
(b) The converse fails. A person-by-person optimal policy can be strictly suboptimal.

*Proof.* (a): if some $a$ satisfied $U(a,\pi^*_{-x})>U(\pi^*)$, the policy $(a,\pi^*_{-x})$ would beat $\pi^*$, contradicting joint optimality. (b): see the example below. $\square$

There are two cases where the theories trivially coincide:

- **Only one input is possible.** Then a policy is just an action.
- **$U$ is additively separable across inputs**, $U(\pi)=\sum_x u_x(\pi(x))$. Then coordinate-wise optimization is joint optimization.

The divergence requires a non-separable $U$, meaning the payoff couples the function's outputs on different inputs. Single-agent Newcomblike problems can be non-separable: in transparent Newcomb the agent's payoff on the *empty* branch depends on $\pi(\textit{full})$. But there the coupling is one-directional, and the bad equilibrium is not self-supporting. Coupling in both directions arises naturally when several instances of the same function, receiving different inputs, all affect a shared payoff. That is plausibly why the authors locate the difference in "multi-agent dilemmas."

### 5.2 Example: a stag hunt among one's own copies

Two copies of the agent's decision procedure are run, one on input *left* and one on input *right*. Each outputs $A$ or $B$. The agent's utility is:

| $\pi(\textit{left})$ | $\pi(\textit{right})$ | utility |
|---|---|---|
| $B$ | $B$ | 10 |
| $A$ | $A$ | 5 |
| mixed | mixed | 0 |

**Action-FDT.** At input *left*, the agent intervenes on $\textsc{fdt}(\underline P,\underline G,\textit{left})$. The variable $\textsc{fdt}(\underline P,\underline G,\textit{right})$ is a different logical fact, so the intervention does not touch it, and the agent consults her belief about it.

If she believes the *right*-copy outputs $A$, then $A$ yields 5 and $B$ yields 0, so she outputs $A$. The *right*-copy reasons symmetrically. The profile $(A,A)$ is a strict, self-confirming equilibrium. If self-beliefs are accurate, it is fully consistent, and the agents receive 5. Whether action-FDT lands on $(A,A)$ or $(B,B)$ depends on the agent's prior self-beliefs, which the decision rule does not determine.

This echoes the paper's own complaint that EDT's "choices are at the mercy of her priors."

**P-FDT.** The agent compares four policies, finds $U(B,B)=10$ is maximal, and both copies output $B$.

The anti-coordination variant shows that P-FDT can also prescribe *different* actions on different inputs. Suppose the utility is 10 iff the outputs differ. A symmetric action-FDT agent, unsure which copy is which, faces an exact tie at each input. If she breaks ties identically on both inputs, she gets 0. P-FDT chooses, for instance, $\pi=(A,B)$. Its one global tie-break among optimal policies is automatically shared by all instances.

### 5.3 Why not just repair action-FDT's graph?

One could object that a good subjunctive-dependence graph would make $\textsc{fdt}(\ldots,\textit{right})$ depend on $\textsc{fdt}(\ldots,\textit{left})$, since both are outputs of the same code. Perhaps so. But that is a counterpossible question about how one input–output pair of a function would vary if (impossibly) another pair differed. The source explicitly treats such questions as unsolved.

P-FDT avoids the question by placing the whole input–output table under a single intervention. The only counterpossibles it needs are of the form "what if this function computed $\pi$?", and these are the same kind FDT already requires. This is, in my view, the main theoretical advantage of the policy formulation.

## 6. Open questions and proposed operational answers

### 6.1 Conditioning on the observation

Footnote 16 does not say whether $U$ is computed with $\textsc{Obs}=x$ conditioned on. I propose that it is not. Three reasons:

- **Textual fit.** The footnote says the agent applies her inputs to the selected policy "in order to select an action." This describes the input's role as application, not evaluation. Equation (4) likewise uses $x$ only to name the intervention point, not as a condition.
- **Avoiding a double update.** Suppose we instead maximized $\mathbb E(V\mid \mathtt{do}(\textsc{fdt}=\pi),\textsc{Obs}=\textit{full})$ in transparent Newcomb. For any policy with $\pi(\textit{full})=\textit{two}$, the conditional world has a full box and \$1,001,000, so the agent would two-box. Ruling out exactly this is the purpose of the updateless treatment of observations. The paper itself criticizes Timeless Decision Theory for prescribing "both conditioning on evidence *and* changing the place where one intervenes," calling this "a kind of 'double update' which proves harmful in practice."
- **Well-definedness.** Conditioning can be undefined when $\mathtt{do}(\pi)$ makes $x$ impossible, for example against a perfect predictor. The unconditioned $U(\pi)$ never has this problem.

### 6.2 The model $P$ and the domain $\mathcal X$

The policy is evaluated relative to the model $P$ the function takes as an argument. If that model already reflects everything the agent learned before the current problem, then $\mathcal X$ ranges over the inputs the function might receive *within this problem*: the observations that can reach any instance of the function, whether the agent's own body or copies.

I propose treating $\mathcal X$ as exactly the set of inputs on which, according to $G$, some variable that matters to $V$ consults the function. A broader domain is harmless, since unconsulted components do not affect $U$. A narrower domain reintroduces action-FDT's dependence on self-beliefs.

How far "back" the prior should go is a substantive question the source does not address. For example, should an agent that has already observed the termite inspection report still evaluate policies from before seeing it? I treat the agent's current model as given, just as the paper treats $(P,G)$ as given.

### 6.3 Randomized policies

The source speaks only of maps from inputs to actions. Two observations:

- If no variable depends on the *distribution* of the agent's randomization, then $U$ is linear in mixtures, so some deterministic policy is optimal and nothing is lost.
- If predictors can see the policy but not the coin, as with the "truly random coin" in the paper's Death in Damascus discussion, then mixed policies can be strictly better. For example, a 50% survival chance beats certain death.

My suggestion is to include randomized policies $\pi:\mathcal X\to\Delta(\mathcal A)$ in $\Pi$ whenever the model contains randomness the predictor cannot anticipate, and to let $G$ say which predictors see which part.

### 6.4 Building the graph

The paper calls deducing subjunctive dependencies "perhaps the largest open problem" for FDT, and P-FDT inherits it unchanged. P-FDT adds one modeling task: specifying, for each dependent node, which *function of the policy* it reads.

- The Newcomb predictor reads $\pi(\textit{full})$.
- The XOR blackmailer reads $\pi(\textit{letter})$.
- A twin reads the whole policy, via its own input.

## 7. A recipe for unfamiliar cases

The following procedure summarizes my interpretation.

1. **Model.** Write a probabilistic model including the agent's utility node $V$, the possible inputs $\mathcal X$, and every system that computes or predicts the agent's decision function: the agent's body, copies, simulators, predictors. Statistical correlates that do not evaluate the function, such as lesions and coincidences, get no edge from the function node.
2. **Enumerate policies.** List $\Pi=\mathcal A^{\mathcal X}$, or randomized policies where unpredictable randomness exists.
3. **Evaluate.** For each $\pi$, set every function-reading node according to $\pi$. Propagate through the causal structure, apply each instance's input to $\pi$, and compute $U(\pi)$ *without* conditioning on the actual observation.
4. **Act.** Choose $\pi^*$ maximizing $U$, breaking ties by a fixed rule shared by all instances, and output $\pi^*(x)$.

**A quick check on the twin prisoner's dilemma.** Both twins receive the same input, so a policy is a single action. Cooperating yields \$1,000,000 and defecting yields \$1,000, so P-FDT cooperates.

**The smoking lesion.** The lesion does not read the policy, so $U(\textit{smoke})$ exceeds $U(\textit{refrain})$ by the value of smoking, and P-FDT smokes. The paper's version of this problem adds uncertainty about the agent's own utility function. I would model that as uncertainty about which model, and hence which function node, is running. This is a further complication the footnote does not address.

**Computational cost.** The cost is real: $|\Pi|=|\mathcal A|^{|\mathcal X|}$. In practice one would search a structured subspace of policies or exploit separability where $G$ shows it, falling back to coordinate-wise (action-FDT-style) optimization only where the coupling is weak.

## 8. Conclusion

According to footnote 16, the authors' preferred formulation of FDT intervenes on the function node to choose "not an action but a *policy*," which the agent then applies to her input. Formally, P-FDT maximizes $\mathbb E(V\mid\mathtt{do}(\textsc{fdt}(\underline P,\underline G)=\pi))$ over policies and outputs $\pi^*(x)$.

Its relation to action-FDT is the relation between joint and person-by-person optimality:

- Every action-FDT choice consistent with an optimal policy is also a P-FDT choice.
- Action-FDT can settle into self-confirming but inferior equilibria among the agent's own instances.
- These inferior equilibria require payoffs that couple the function's outputs on different inputs, which is why, as the authors suggest, the difference surfaces mainly in multi-agent and multi-copy problems.

The interpretations offered here go beyond the footnote and are my proposals: unconditioned evaluation of policies, a problem-relative input domain, and optional randomized policies. What the footnote does make clear is the underlying idea. The agent should choose what *this function* does across all inputs on which anything consults it, rather than what it does on one input while holding the rest fixed by belief.

---

**Reference.** Yudkowsky, E. & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060 (footnotes 7 and 16; equation (4); Sections 5–6 and 9).