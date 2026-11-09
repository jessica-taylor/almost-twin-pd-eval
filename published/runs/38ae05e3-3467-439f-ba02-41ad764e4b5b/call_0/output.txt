# Policy Functional Decision Theory (P-FDT): Choosing the Whole Input–Output Map

## 1. What the source says

Yudkowsky and Soares's *Functional Decision Theory: A New Theory of Instrumental Rationality* presents its theory mostly at the level of actions. The agent, holding a model of the world and an observation, intervenes on a variable standing for "the output of my decision function on this input" and picks the best action. Two footnotes say that this is not the authors' preferred formulation. Footnote 7 reads:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

Footnote 16, which I take as the primary source, reads:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

I call the theory described there **P-FDT** (policy functional decision theory). I call the version formalized in the body of the paper (its Equation 4) **A-FDT** (action-level FDT).

The source commits to four claims:

1. The object of choice is a policy, meaning a mapping from inputs (observations) to actions.
2. Choice works by intervening on a node representing the decision function, written $\mathrm{FDT}(-)$.
3. After choosing the policy, the agent applies her actual input to it to obtain an action.
4. The difference from A-FDT matters only in (certain) multi-agent dilemmas, "so far as we can tell."

Almost everything else in this essay is reconstruction. That includes exactly what the node ranges over, whether the agent conditions on her observation, how ties are broken, and when the two formulations agree. I flag those parts as my proposals.

## 2. Background: how A-FDT works

The paper models an agent as holding a probability distribution $P$ over variables, together with a graph $G$ recording dependencies. These include ordinary causal dependencies and also *subjunctive* ones: two physical systems computing the same function both depend on that function's output.

The model contains logical variables such as $\textsc{fdt}(\underline P,\underline G,\underline x)$. The underlining marks dequoting: this is the variable whose value is "what the FDT algorithm outputs on inputs $(P,G,x)$." Equation 4 of the paper defines

$$
\mathrm{FDT}(P,G,x) \;:=\; \operatorname*{argmax}_{a\in\mathcal A}\; \mathbb E\!\left[V \,\middle|\, \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right].
\tag{A}
$$

Two features matter for what follows.

- **Observations change the intervention point.** Observations do not enter by conditioning. The paper says FDT "responds to observation by changing which node it intervenes upon." Seeing a full box means intervening on $\textsc{fdt}(\underline P,\underline G,\textit{full})$ rather than $\textsc{fdt}(\underline P,\underline G,\textit{empty})$.
- **Other input-nodes are left alone.** When A-FDT intervenes on the node for input $x$, the nodes for other inputs $x'$ keep whatever distribution $P$ gives them. The paper's own transparent Newcomb calculation contains a free parameter $q$ for exactly this reason: "Fiona's prior probability that she two-boxes upon seeing the box empty."

The second feature is what P-FDT changes.

## 3. Defining P-FDT

### 3.1 The policy node

Let $\mathcal X_M$ be the set of observation histories the model treats as possible inputs to the agent's algorithm, and $\mathcal A$ the action set. The policy space is

$$
\Pi := \mathcal A^{\mathcal X_M}=\{\pi:\mathcal X_M\to\mathcal A\}.
$$

Footnote 16's notation $\mathrm{FDT}(-)$, with a blank where the input goes, suggests a single function-valued variable rather than one variable per input. I write

$$
\Phi := \textsc{fdt}(\underline P,\underline G)\in\Pi,
$$

meaning "the input–output behaviour of the FDT algorithm, run with this model, as a function of the observation." The observation is no longer an argument of the node's name. It is the argument the policy gets applied to.

### 3.2 Structural requirements on $G$

The following requirements are my proposal, made concrete so the theory can be applied:

- **(S1) The agent's act reads the policy.** The agent's action node is $\textsc{Act} := \Phi(\textsc{Obs})$. This is the footnote's "to which the agent then applies her inputs."
- **(S2) Every subjunctive dependent reads the policy at some argument.** Each process that subjunctively depends on the agent's algorithm reads $\Phi$ at some argument, possibly noisily. A predictor modelling "what she does on seeing a full box" depends on $\Phi(\textit{full})$. A copy of the agent that sees $x'$ acts as $\Phi(x')$.
- **(S3) Lesion-like variables do not depend on $\Phi$.** Everything that merely correlates with the agent's behaviour, without computing or modelling her algorithm, is not a descendant of $\Phi$. Such variables are held fixed under intervention, exactly as in A-FDT.

Under these requirements, A-FDT's nodes $\textsc{fdt}(\underline P,\underline G,\underline x)$ become coordinates $\Phi(x)$ of a single object. The difference between the theories is then whether you intervene on one coordinate or on all of them at once.

### 3.3 The decision rule

$$
\pi^\star \in \operatorname*{argmax}_{\pi\in\Pi}\; \mathbb E\!\left[V \,\middle|\, \mathtt{do}(\Phi=\pi)\right],
\qquad
\text{P-FDT}(P,G,x) := \pi^\star(x).
\tag{P}
$$

As a procedure:

1. Build the model $(P,G)$ satisfying S1–S3.
2. For each policy $\pi$, set $\Phi=\pi$ by surgery and propagate downstream. This sets the predictors' predictions, the copies' actions, and the agent's own action as $\pi(\textsc{Obs})$.
3. Compute expected utility.
4. Pick the best policy, using a canonical tie-break (see §3.4).
5. Apply it to the observation actually received.

### 3.4 Interpretive choices the footnote leaves open

**(i) No conditioning on the observation.** In (P) the expectation is not conditioned on $\textsc{Obs}=x$. I think this is the right reading, for three reasons:

- Equation 4 already omits conditioning on $x$. Observations enter A-FDT only through where it intervenes.
- The footnote says inputs are applied after the policy is chosen.
- The paper warns, in a footnote on Timeless Decision Theory, that conditioning on evidence *and* changing the intervention point "creates a kind of 'double update' which proves harmful in practice."

Conditioning on $x$ and then optimizing a whole policy would be a different hybrid theory.

The model $P$ is then the agent's model *as an input to the algorithm*: the state of belief that predictors and copies are modelling. In the paper's examples this is the pre-observation description of the dilemma. Exactly which "prior" this should be for an agent with a long history is not settled by the source. I return to this in §6.

**(ii) A finite domain.** The paper allows countable $\mathcal X$, which makes $\Pi$ uncountable, so the argmax may not exist. Operationally, I restrict $\mathcal X_M$ to the observations the model actually distinguishes. Nodes that don't depend on $\Phi$ at a given input are unaffected by how $\pi$ is defined there.

**(iii) Canonical tie-breaking.** Distinct instances of the algorithm must select the *same* $\pi^\star$. If two instances broke ties independently, they could implement incoherent combinations of policies. So the tie-break must be a fixed, deterministic part of the algorithm, for example the lexicographically first optimal policy. A-FDT never needed to say this. P-FDT does, as the example in §4.2 shows.

**(iv) Pure versus mixed policies.** The footnote speaks of mappings to actions. I take policies to be deterministic by default. Randomization should be admitted only when the model contains a randomness source and specifies whether predictors can see it.

## 4. Worked examples

### 4.1 Transparent Newcomb (one instance; same verdict as A-FDT)

The setup, following the paper:

- Box A holds \$1,000.
- Box B holds \$1,000,000 iff the predictor (99% accurate) predicts the agent would one-box *on seeing a full box*.
- The agent sees box B's contents before choosing.

The predictor reads $\Phi(\textit{full})$, possibly erring. The agent's act is $\Phi(\textsc{Obs})$, and $\textsc{Obs}$ is the box state. Write a policy as $(\pi(\textit{full}),\pi(\textit{empty}))$, with 1 for one-box and 2 for two-box.

| Policy | Accurate prediction (0.99) | Inaccurate prediction (0.01) | Expected utility |
|---|---|---|---|
| (1,1) | full, take 1: \$1,000,000 | empty, take 1: \$0 | \$990,000 |
| (1,2) | full, take 1: \$1,000,000 | empty, take 2: \$1,000 | **\$990,010** |
| (2,1) | empty, take 1: \$0 | full, take 2: \$1,001,000 | \$10,010 |
| (2,2) | empty, take 2: \$1,000 | full, take 2: \$1,001,000 | \$11,000 |

P-FDT selects "one-box if full, two-box if empty." On seeing a full box it one-boxes, which matches the paper's verdict.

The paper's free parameter $q$ has disappeared. The behaviour on seeing an empty box is now chosen rather than guessed at, and it comes out as $q=1$, the value the paper says "you may verify" is correct. This is the general pattern: P-FDT closes the loose ends A-FDT leaves to the prior.

### 4.2 Copies with different inputs (a multi-agent case where the theories split)

The following example is mine. It illustrates the footnote's claim that the difference arises in multi-agent problems.

**The setup.** Two physical instances run the same algorithm with the same model $(P,G)$. Instance 1 observes $L$ and instance 2 observes $R$; for example, the rooms are labelled differently. Each chooses $A$ or $B$, with no communication. Each receives:

- 2 if both choose $A$,
- 1 if both choose $B$,
- 0 otherwise.

**A-FDT.** Let $\beta := P(\textsc{fdt}(\underline P,\underline G,R)=A)$. The instance at $L$ intervenes only on its own node, leaving $\beta$ untouched:

$$
\mathbb E[V\mid \mathtt{do}(\textsc{fdt}_L=A)]=2\beta,\qquad
\mathbb E[V\mid \mathtt{do}(\textsc{fdt}_L=B)]=1-\beta .
$$

So it plays $A$ iff $\beta>1/3$, and symmetrically for $R$ with $\alpha := P(\textsc{fdt}_L=A)$. Suppose the agent's model expects $B$, say $\alpha=\beta=0.1$. Then both instances play $B$, and the beliefs were correct. The A-FDT fixed point $(B,B)$ is self-consistent and yields 1.

A-FDT treats its own behaviour at the other input as an exogenous fact about the world. Its sibling instances therefore face each other like Nash players and can get stuck in a dominated equilibrium.

**P-FDT.** Here $\Phi\in\{A,B\}^{\{L,R\}}$, and $\mathbb E[V\mid\mathtt{do}(\Phi=\pi)]=U(\pi(L),\pi(R))$, independently of any prior over the agent's own behaviour. The unique optimum is $(A,A)$, giving 2. Both instances compute it, and each applies its input.

This is the paper's "intervene on the type, not the token" idea, extended. The type is the whole input–output map, not its value at one input.

**Anti-coordination and tie-breaking.** Change the payoffs so that mismatching pays 1 and matching pays 0. Then $\pi=(A,B)$ and $\pi=(B,A)$ tie. Suppose instance $L$ broke the tie toward $(A,B)$ and instance $R$ toward $(B,A)$. Then $L$ plays $A$ and $R$ plays $A$, and they fail. With the canonical tie-break of §3.4(iii), both select the same policy and succeed. The tie-break is not decoration; it is part of what makes the instances one function.

### 4.3 A single-agent case with the same structure

I add a cautionary note on the source's "so far as we can tell." Suppose a predictor pays \$1,000,000 iff it predicts the agent *would* take a costly action $c$ (cost \$10) in *both* of two circumstances $x_1$ and $x_2$, and the agent will face only one of them.

The predictor reads $\Phi(x_1)$ and $\Phi(x_2)$ jointly. Formally, this is the coordination game of §4.2 with the predictor's two queries playing the role of the two instances. If the agent's prior assigns low probability to $c$ at the input she does not see, A-FDT declines $c$, and that prior is again self-confirming. P-FDT pays.

The source's hedge therefore seems apt, provided "multi-agent" is read broadly. Anything that consults the policy at several inputs non-separably behaves like several instances.

## 5. When do P-FDT and A-FDT agree?

Write $W(\pi) := \mathbb E[V\mid \mathtt{do}(\Phi=\pi)]$. The following facts are mine. They assume S1–S3, and that A-FDT's intervention on $\Phi(x)$ leaves the other coordinates distributed according to $P$.

**Proposition 1 (separability).** Suppose $W(\pi)=\sum_{x\in\mathcal X_M} f_x(\pi(x))$ for some functions $f_x$, and suppose that intervening on the coordinate $\Phi(x)$ alone changes expected utility only through $f_x$. Then for every $x$, P-FDT and A-FDT choose the same action at $x$, modulo ties, whatever $P$ believes about the agent's behaviour elsewhere.

*Proof sketch.* Maximizing a sum of terms each depending on one coordinate is coordinatewise maximization. Under A-FDT, the other coordinates contribute only an additive constant to the comparison at $x$. ∎

Separability is sufficient but not necessary. Transparent Newcomb is not separable: the payoff on seeing an empty box interacts with the full-box coordinate through the error branch. Yet A-FDT reaches the right answer there because the interaction is small.

**Proposition 2 (optimal policies are A-FDT fixed points).** Let $\pi^\star$ maximize $W$. If $P$ places probability 1 on $\Phi(x')=\pi^\star(x')$ for all $x'\neq x$, then $\pi^\star(x)$ is A-FDT-optimal at $x$.

*Proof.* Under these beliefs, the A-FDT value of choosing $a$ at $x$ is $W$ evaluated at $\pi^\star$ with its $x$-coordinate replaced by $a$. That is at most $W(\pi^\star)$. ∎

The converse fails, as §4.2 shows. In team-decision-theory terms (Marschak and Radner), A-FDT finds *person-by-person optimal* policies, while P-FDT finds *team-optimal* ones. This gives a clean statement of what footnote 16 changes. P-FDT does not alter which dependencies count, what to hold fixed, or how predictors and lesions are treated. It changes the *granularity* of the intervention, from one input-node to the whole function. That removes the agent's dependence on its own prior about how it behaves elsewhere.

**A test for unfamiliar cases.** Ask whether anything in the model consults the agent's algorithm at more than one input. If it does, check whether that consultation is non-separable and whether the agent's prior about its other-input behaviour could be wrong. If neither condition holds, A-FDT and P-FDT agree, and you can reason at the action level as the paper does. If both hold, solve (P).

## 6. Open questions and the uncertainty they leave

**Whose prior, and when?** The footnote does not say relative to which belief state $P$ the policy is chosen.

- In the paper's dilemmas, the natural $P$ is the agent's model of the dilemma before observing its contents, which is what predictors simulate.
- For an agent with a lifetime of experience, one could take $P$ as late as possible, conditioned on everything learned before the dilemma began, or as early as possible, an ur-prior. Earlier choices give more "updateless" behaviour and more opportunities for coordination. They also mean acting on stale beliefs.
- The paper links its "lack of updating" to Wei Dai's Updateless Decision Theory, a distinct but related theory. Choosing the cut-point is a substantive open problem.

My operational proposal: use the model the relevant predictors and copies are themselves running. This is the model in which the subjunctive dependencies were set up, and the one the paper uses in its examples.

**Building $G$.** P-FDT inherits FDT's central gap: there is no general method for learning subjunctive-dependence structure, which the paper calls "perhaps the largest open problem". It sharpens the gap, because $G$ must now say *which coordinates* of $\Phi$ each dependent process reads. A predictor that misreads "on seeing a full box" as "on seeing anything" changes the answer.

**Computation.** $|\Pi|=|\mathcal A|^{|\mathcal X_M|}$. Exhaustive search is hopeless for realistic observation spaces, so practical P-FDT agents will need structure: factored policies, or exploiting the separability of Proposition 1 wherever it holds.

**Logical counterfactuals.** The intervention $\mathtt{do}(\Phi=\pi)$ is a counterpossible for every $\pi$ except the one the algorithm actually outputs, exactly as with A-FDT. P-FDT neither helps nor hurts on this front. The paper's FDT′ discussion already shows that "choosing a different function" doesn't dodge the problem.

**Fairness.** The paper's conjecture that FDT is unbeaten on "fair" problems is not reformulated by the footnote. Policies make the natural fairness criterion cleaner, though: "the outcome depends only on the agent's policy." Rewards that depend on behaviour in non-actual circumstances (§4.3) count as fair under this criterion. That is presumably why the policy form is the one the authors prefer.

## 7. Conclusion

P-FDT keeps everything distinctive about functional decision theory:

- expected-utility maximization,
- counterfactuals built by surgery on a model enriched with subjunctive dependencies,
- treating predictors and copies as depending on the agent's algorithm, and lesions as not.

It changes one thing: the intervened variable is the algorithm's entire input–output map, $\Phi=\textsc{fdt}(\underline P,\underline G)$, rather than its output at the current input. The agent chooses $\pi^\star=\operatorname{argmax}_\pi \mathbb E[V\mid\mathtt{do}(\Phi=\pi)]$ and then applies her observation, $a=\pi^\star(x)$.

In separable problems, which include most of the paper's single-instance dilemmas, this agrees with action-level FDT. Where the algorithm is consulted at several inputs at once, as with copies seeing different things or predictors querying several circumstances, P-FDT coordinates the agent's own instances by construction. Action-level FDT, by contrast, can lock itself into a self-confirming but suboptimal equilibrium.

The footnote leaves open which prior to choose from, how to break ties, and how to learn the dependency graph. I have proposed answers to the first two (the predictors' model, and a canonical deterministic tie-break). The third remains FDT's main unsolved problem.

## References

- Yudkowsky, E. and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060 (esp. footnotes 7 and 16, Eq. 4, §6, §9).
- Dai, W. (2009). "Towards a New Decision Theory." *Less Wrong*.
- Pearl, J. (2000). *Causality*. Cambridge University Press.
- Marschak, J. and Radner, R. (1972). *Economic Theory of Teams*. Yale University Press.