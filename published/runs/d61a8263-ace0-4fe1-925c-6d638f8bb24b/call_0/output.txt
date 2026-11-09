# Choosing the Function, Not the Act: An Essay on Policy Functional Decision Theory (P‑FDT)

## 1. What the source actually says

Yudkowsky and Soares's paper *Functional Decision Theory* spends most of its length on a theory that chooses **actions**. At two points, though, it says that the authors prefer a different formulation. Footnote 7 says:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

Footnote 16, which I treat as the primary source for this essay, says:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

I will call the theory described in this footnote **P‑FDT** (policy functional decision theory). The theory formalized in the body of the paper, its Equation (4), I will call **action-level FDT**. That label is mine; the paper simply calls it FDT. I will also refer to causal decision theory (**CDT**) and evidential decision theory (**EDT**).

Footnote 16 fixes three things:

1. The object of choice is a policy, meaning a map from inputs to actions.
2. The choice is made by intervening on a node representing the output of the decision function.
3. The agent then applies the chosen policy to her actual input.

The footnote leaves several things open. It does not say exactly which node is intervened on, or whether the expectation is conditioned on the agent's observation. It does not say how ties are broken, whether policies may be stochastic, or why the difference should matter only in multi-agent problems. The rest of this essay reconstructs the theory from the paper's machinery and fills these gaps. Each gap-filling choice is flagged as my own.

## 2. Background: the expected-utility skeleton

The paper treats EDT, CDT and FDT as expected-utility theories that differ only in how they construct *hypotheticals*. The agent holds a world-model $M=(P,G)$, where $P$ is a probability distribution over variables and $G$ is a graph of dependencies. Utility enters through a variable $V=\mathcal U(\text{Outcome})$. The three theories differ in what they do to $M$ before taking an expectation of $V$:

- **EDT** conditions on the act: $\arg\max_a \mathbb E(V\mid \text{Obs}=x,\text{Act}=a)$.
- **CDT** intervenes on the physical act: $\arg\max_a \mathbb E(V\mid \mathrm{do}(\text{Act}=a),\text{Obs}=x)$.
- **Action-level FDT** intervenes on a *logical* node, the output of the FDT algorithm on the agent's own inputs:
$$\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\big(V \mid \mathrm{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)\big). \tag{4}$$

The underlying idea is *subjunctive dependence*. Anything that computes or accurately models the agent's decision function, such as a twin, a predictor, or a simulation, varies with that function's output in the hypothetical. Things that are merely statistically correlated with the act, like the smoking lesion, do not.

The paper concedes that these are counterpossible hypotheticals: a deterministic function has only one output on a given input. It deliberately sidesteps the question of how to evaluate them by taking the dependency graph $G$ as an input. P‑FDT inherits this arrangement unchanged.

One feature of Equation (4) matters for what follows. Observations enter it in only one place: they change *which node* is intervened on. In the paper's words, "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." In the transparent Newcomb and blackmail graphs, there is a separate node $\textsc{fdt}(\underline P,\underline G,x)$ for each possible observation $x$. Another variable, such as the predictor's prediction or the blackmailer's decision, determines which of these nodes actually drives the body's action.

## 3. The definition of P‑FDT

**Setup.** Let $\mathcal X$ be the set of possible inputs (observation histories) relevant to the problem, and $\mathcal A$ the set of actions. A policy is a function $\pi:\mathcal X\to\mathcal A$. Write $\Pi=\mathcal A^{\mathcal X}$ for the set of all policies.

**The policy node.** Footnote 16 says the intervention is on "the node $\mathrm{FDT}(-)$". I read the dash as follows. There is a single node
$$\Phi := \textsc{fdt}(\underline P,\underline G),$$
which takes values in $\Pi$ and represents *which policy the FDT function computes* given the model, with no observation argument. Every implementation $i$ of the function (the agent's body, a predictor's model of her, an exact copy) has an input variable $\text{Obs}_i$. Its action satisfies the structural equation
$$\text{Act}_i = \Phi(\text{Obs}_i),$$
possibly with noise if the implementation is imperfect, as with a fallible predictor. This equation is "to which the agent then applies her inputs" written in graphical form.

**The rule.** Define the policy value
$$U(\pi) := \mathbb E_P\big(V \mid \mathrm{do}(\Phi=\pi)\big),$$
and then
$$\pi^\star \in \arg\max_{\pi\in\Pi} U(\pi), \qquad \text{P-FDT}(P,G,x) := \pi^\star(x).$$

**A structural observation (mine).** The paper's family of observation-indexed nodes $\{\textsc{fdt}(\underline P,\underline G,x)\}_{x\in\mathcal X}$ is exactly a policy written coordinate by coordinate. Its tuple of values *is* an element of $\mathcal A^{\mathcal X}$. This gives a clean way to compare the two theories:

- **P‑FDT** performs one *joint* intervention that sets all coordinates at once.
- **Action-level FDT** intervenes on the *single coordinate* $x$ that the agent actually observes. The other coordinates $\pi_{-x}$ are left distributed according to the prior $P$.

Formally, action-level FDT at input $x$ solves
$$\max_{a}\ \mathbb E_{\pi_{-x}\sim P}\big[U(a,\pi_{-x})\big],$$
while P‑FDT solves $\max_\pi U(\pi)$ and reads off coordinate $x$. One is a coordinate-wise best response. The other is a global optimization. Every difference between the two theories comes from the gap between these two.

## 4. Interpretive choices the footnote leaves open

### 4.1 Is the expectation conditioned on the observation?

Neither Equation (4) nor footnote 16 conditions $P$ on $\text{Obs}=x$. (The paper's displayed expression for transparent Newcomb writes "$\mathrm{do}(\ldots, \text{Obs}=\text{full})$". Its accompanying calculation, however, averages over both the "full" and "empty" branches, so the computation is unconditioned.)

I adopt the **unconditioned (updateless) reading**: $U(\pi)$ is computed under the model *before* the problem's observations. Observations influence the act only through the final application $\pi^\star(x)$. I have three reasons.

1. **The source's own warnings.** The paper says Timeless Decision Theory, which both conditions on evidence and moves the point of intervention, suffers a harmful "double update." Conditioning inside a policy evaluation would recreate exactly that problem.

2. **It is needed to get the paper's verdicts.** In transparent Newcomb, condition on "full" and compare the policies that differ at "full." Given that the box is full, two-boxing yields \$1,001,000 against \$1,000,000, so the conditioned theory two-boxes. The paper rejects that answer.

3. **It is needed for the multi-agent case that motivates P‑FDT (§6).** Suppose two copies conditioned on different inputs. Their models would differ, $P(\cdot\mid x_1)\neq P(\cdot\mid x_2)$, so they would be computing *different* functions $\textsc{fdt}(P\mid x_1,G)$ and $\textsc{fdt}(P\mid x_2,G)$. The single shared policy node, which is the whole point of the construction, would split into two. Coordination through a shared function requires that every instance evaluate policies from the *same* model.

Updatelessness has a cost: the theory must specify *which* prior. The source does not say. My operational proposal is this. Use the agent's model as it stood at the point where the problem's dependency structure was fixed. In practice, that means the information shared by every implementation of the function, including the predictors' models of it. Observations that arrive later, and that some implementation might not share, belong to $\mathcal X$, not to $P$.

### 4.2 Ties

Ties among policies are common, especially in symmetric multi-agent problems. If different instances broke ties differently, they would no longer be computing one function. I therefore add a requirement: **ties are broken by a fixed canonical ordering of $\Pi$ that is part of the function.** All instances then compute the same $\pi^\star$.

### 4.3 Stochastic policies

The footnote says only "policy." If predictors and copies respond to *realized* outputs, then $U$ is linear in mixtures over $\Pi$, and some deterministic policy is always optimal. Restricting to $\mathcal A^{\mathcal X}$ then loses nothing. If instead some process responds to the agent's *randomization probabilities*, the policy space should be $\Delta(\mathcal A)^{\mathcal X}$. Here the source is silent, and I leave the question open.

### 4.4 Where the dependency graph comes from

The paper says that "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." P‑FDT does not solve this problem. It only changes what is placed at the root of the graph.

## 5. Single-agent problems: P‑FDT reproduces the paper's verdicts

**Newcomb, twin prisoner's dilemma.** The relevant input set is a singleton, so policies are just actions and $\Phi$ is the paper's node. In Newcomb's problem, $U(\text{onebox})=0.99\times\$1{,}000{,}000=\$990{,}000$ and $U(\text{twobox})=0.01\times\$1{,}001{,}000+0.99\times\$1{,}000=\$11{,}000$. P‑FDT one-boxes. In the twin prisoner's dilemma, the twin's act is also $\Phi$ applied to the same input, so P‑FDT cooperates.

**Smoking lesion.** The lesion is not downstream of $\Phi$, because nothing about the lesion computes the decision function. Intervening on $\Phi$ therefore leaves $P(\text{cancer})$ unchanged, and the policy "smoke" gains its \$1,000.

**Transparent Newcomb.** Here $\mathcal X=\{\text{full},\text{empty}\}$, and a policy is written as a pair $(\pi(\text{full}),\pi(\text{empty}))$. The predictor fills box B iff it predicts $\pi(\text{full})=$ one-box, and it is accurate with probability $0.99$. Writing 1 for one-box and 2 for two-box:

| $\pi$ | $U(\pi)$ |
|---|---|
| $(1,2)$ | $0.99(1{,}000{,}000)+0.01(1{,}000)=990{,}010$ |
| $(1,1)$ | $0.99(1{,}000{,}000)+0.01(0)=990{,}000$ |
| $(2,2)$ | $0.99(1{,}000)+0.01(1{,}001{,}000)=11{,}000$ |
| $(2,1)$ | $0.99(0)+0.01(1{,}001{,}000)=10{,}010$ |

So $\pi^\star=(1,2)$. Seeing a full box, the agent applies $\pi^\star(\text{full})$ and one-boxes, matching the paper. Note what the evaluation does. While holding a full box, the agent scores each policy partly by what happens in worlds where she would have seen an empty one. That is exactly the paper's claim that the agent should "entertain the hypothesis that, if their action were different, they might have *made different observations*."

**Parfit's hitchhiker** has the same structure. A policy that pays upon reaching the city gets the ride with probability 0.99. A policy that refuses is left in the desert with probability 0.99. P‑FDT pays.

**Mechanical blackmail with error rate $\varepsilon$.** The relevant coordinate is $\pi(\text{blackmailed})$. Assume, as in the paper's calculation, that a paying policy is always blackmailed, and that a refusing policy is blackmailed only by mistake, with probability $\varepsilon$. Then $U(\text{pay})=-\$1{,}000$ and $U(\text{refuse})=-\varepsilon\cdot\$1{,}000{,}000$. P‑FDT refuses iff $\varepsilon<0.001$. This agrees with the paper's example, where $\varepsilon=0.0009$ gives "\$900 in expectation" and refusal. The agent refuses even while holding the letter, because she evaluates *policies*, not her current predicament.

Why does P‑FDT agree with action-level FDT in all these cases? The following proposition is my explanation; it is not a claim made in the source.

> **Proposition (coordinate-wise dominance).** Suppose there is a policy $\pi^\dagger$ such that, for every $x$ and every $\pi_{-x}$, $U(\pi^\dagger(x),\pi_{-x}) \ge U(a,\pi_{-x})$ for all $a$. Then (i) $\pi^\dagger$ maximizes $U$, and (ii) action-level FDT at input $x$ chooses $\pi^\dagger(x)$ whatever its prior over $\pi_{-x}$.
>
> *Proof.* (i) Take any $\pi$ and replace its coordinates by those of $\pi^\dagger$ one at a time. By hypothesis, no step decreases $U$, so $U(\pi)\le U(\pi^\dagger)$. (ii) $\pi^\dagger(x)$ is optimal against every realization of $\pi_{-x}$, hence against any mixture of realizations. $\square$

Transparent Newcomb satisfies the hypothesis. With $q$ the probability of two-boxing on "empty," one-boxing on "full" gives $990{,}000+10q$, against $10{,}010+990q$ for two-boxing on "full." One-boxing wins for every $q\in[0,1]$. Likewise, two-boxing on "empty" wins for every value of $\pi(\text{full})$. This is why the paper could note that Fiona's uncertainty about her behavior at the other input "doesn't matter."

The proposition suggests a sharper version of the footnote's claim. The two theories come apart exactly when $U$ *couples* the coordinates, so that the best action at one input depends on what the function does at another. Single-agent problems with perfect recall rarely have this coupling. It arises naturally when several instances of the same function act on *different* inputs within one world, which is the "multi-agent dilemmas" the footnote mentions.

## 6. Where P‑FDT and action-level FDT diverge

The footnote names no example, so I construct one.

**Copy coordination.** An agent and an exact copy, perhaps a duplicated program, are placed in separate rooms. A known procedure gives one of them input $1$ and the other input $2$. Each chooses $A$ or $B$. Each receives \$1 if both choose $A$, \$2 if both choose $B$, and \$0 otherwise. Both copies run the same function on the same model, and each cares about its own payoff, which is symmetric.

*Action-level FDT.* The copy with input $1$ intervenes on $\Phi_1=\textsc{fdt}(\underline P,\underline G,1)$. The other copy's act is driven by $\Phi_2$, a different node that is not downstream of $\Phi_1$. So $\Phi_2$ stays at its prior, $P(\Phi_2=A)=q$, giving
$$\mathbb E[V\mid \mathrm{do}(\Phi_1=A)] = q,\qquad \mathbb E[V\mid \mathrm{do}(\Phi_1=B)] = 2(1-q).$$
The copy chooses $A$ iff $q>2/3$, and the other copy reasons symmetrically. If the agent's model predicts that it plays $A$ on both inputs, then it does play $A$, the prediction is borne out, and both copies get \$1. The bad equilibrium is self-confirming. This is the same vulnerability the paper diagnoses in EDT: the choice is hostage to the agent's prior beliefs about its own behavior. Here the prior that matters concerns the function's output at the *other* input.

*P‑FDT.* With a single node $\Phi$ ranging over policies,
$$U(A,A)=1,\quad U(B,B)=2,\quad U(A,B)=U(B,A)=0.$$
So $\pi^\star=(B,B)$ whatever $q$ is, and each copy applies it to its own input. Both receive \$2.

**Anti-coordination.** Change the payoff to \$1 iff the copies choose *differently*. P‑FDT finds $U(A,B)=U(B,A)=1$, a tie. Under the canonical tie-breaking of §4.2, both copies select the same $\pi^\star$, say $(A,B)$, and succeed with certainty. Action-level FDT with symmetric beliefs ($q=1/2$) is indifferent at each input and has no mechanism that guarantees success.

These examples show what the footnote's preference for policies buys. Action-level FDT already lets the agent see that her twin "is a *twin*." But when the twins receive different inputs, it treats each one's input-specific output as fixed background. It therefore recreates within the self a version of the independence assumption the paper criticizes in CDT. P‑FDT closes this gap by making the whole input-output map the object of control.

## 7. A procedure for unfamiliar cases

Collecting the definition and my supplementary assumptions, P‑FDT can be applied as follows.

1. **Fix the input set and the actions.** List every input $x\in\mathcal X$ that any implementation of your decision function might receive in the problem, and the available actions $\mathcal A$.
2. **Locate the implementations.** Identify everything that computes or accurately models your function: your body, predictors, simulations, copies. Record which input each receives, and how reliably it reproduces $\Phi$ applied to that input.
3. **Build $(P,G)$ from the shared prior.** Place the policy node $\Phi$ upstream of each implementation's action via $\text{Act}_i=\Phi(\text{Obs}_i)$. Keep merely correlated factors, such as lesions or coincidental features, outside $\Phi$'s descendants.
4. **Evaluate each policy.** For each $\pi\in\Pi$, compute $U(\pi)=\mathbb E(V\mid \mathrm{do}(\Phi=\pi))$ without conditioning on your actual observation.
5. **Choose and act.** Select $\pi^\star$, breaking ties canonically, and perform $\pi^\star(x)$ for your actual input $x$.
6. **Shortcut.** If coordinate-wise dominance holds, you can optimize your own input's coordinate alone and get the same answer.

A quick illustration of applying the procedure: the paper's voting example, with ten agents who each receive \$1,000,000 iff all ten pay \$1,000 to vote. If all ten agents run P‑FDT on the same model, the policy "vote" is one coordinate shared by all ten implementations. Its value is $1{,}000{,}000-1{,}000$ against $0$, so all ten vote. (The source reaches the same verdict for FDT generally.)

## 8. Philosophical assessment

P‑FDT expresses the paper's slogan more faithfully than the action-level formalism the paper actually writes down. The paper says FDT agents "simply act as they would have ideally precommitted to act," and that "FDT agents always act as they would have precommitted to act." A precommitment is naturally a *policy*: a specification of what to do in each contingency, fixed before the contingencies are observed. Under the updateless reading, $\pi^\star$ is exactly the best precommitment available from the shared prior. In the transparent Newcomb and blackmail cases, the paper had to argue that action-level FDT happens to match this ideal. P‑FDT matches it by construction.

The paper's "global perspective" also fits naturally: "What would the entire universe look like if the FDT algorithm behaved differently?" An algorithm's behavior is its whole input-output map. Intervening on one entry while holding the others at their prior is a partial version of that global question.

The costs are real, and the source does not settle them.

- **Computation.** $|\Pi|=|\mathcal A|^{|\mathcal X|}$ grows exponentially. Any practical P‑FDT must exploit structure, such as the dominance shortcut, or search policies approximately.
- **Choice of prior.** The updateless reading needs a principled answer to "updateless with respect to what?" I proposed the information shared by all implementations at the time the dependency structure was fixed. That is a working rule, not something the source states.
- **Counterpossibles.** The policy node is a logical variable. Intervening on it is as counterpossible as intervening on a single output, and the theory still depends on a supplied graph $G$.
- **Multi-agent scope.** The source says the difference matters "only" in multi-agent dilemmas "so far as we can tell." My proposition states a sufficient condition for agreement, but it does not prove that agreement holds in every single-agent problem. Problems with imperfect recall, where one agent receives several inputs at different times, are a natural place to test that hedge.

## 9. Conclusion

As footnote 16 describes it, P‑FDT replaces the question "which output should this function give on *this* input?" with "which input-to-output map should this function be?" The agent answers by intervening on a node representing the function's policy, takes the expected utility of each policy under her model, and applies the winner to her actual input.

On the paper's own single-agent examples, the two formulations agree. Newcomb, smoking lesion, transparent Newcomb, Parfit's hitchhiker and blackmail all have a coordinate-wise dominant structure. They come apart when several implementations act on different inputs and the payoff couples their behavior. There, action-level FDT's dependence on prior self-predictions can lock in bad equilibria, while P‑FDT optimizes jointly.

The source only gestures at the theory. To make it operational I added four assumptions:

- an unconditioned (updateless) evaluation from a shared prior;
- canonical tie-breaking;
- deterministic policies when predictors respond to realized outputs;
- the explicit structural equation $\text{Act}_i=\Phi(\text{Obs}_i)$.

With these in place, P‑FDT is a precise procedure that formalizes the paper's guiding idea: a rational agent should act as she would have precommitted to act, and she should treat what she controls as the behavior of a function.

## References

- Yudkowsky, E. & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality* (arXiv:1710.05060), esp. footnotes 7 and 16 and Equation (4).
- Dai, W. (2009). "Towards a New Decision Theory." *Less Wrong.*
- Gibbard, A. & Harper, W. (1978). "Counterfactuals and Two Kinds of Expected Utility."
- Pearl, J. (2000). *Causality.* Cambridge University Press.