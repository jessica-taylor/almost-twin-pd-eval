# Choosing the Whole Function: An Essay on Policy Functional Decision Theory (P-FDT)

## 1. The source and what it says

Yudkowsky and Soares's paper *Functional Decision Theory* presents functional decision theory mainly through an equation that selects **actions**. Twice, though, the authors note that this is not their preferred version. Footnote 7 says:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

Footnote 16, which I take as the primary source, says:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

I call the theory these footnotes describe **P-FDT** (policy functional decision theory). The footnotes fix three things:

1. the object of choice is a policy, a map from inputs (observations) to actions;
2. the choice is made by *intervening* on the node representing the output of the decision function;
3. the agent then *applies* her actual input to the chosen policy to get her action.

They leave much open: which probability distribution is used, whether the agent conditions on her observation, how ties are broken, whether policies may be randomized, and what "multi-agent" means. In what follows I mark clearly where I am reporting the paper and where I am proposing an interpretation.

## 2. Background: the action-indexed formulation

To compare against P-FDT, I need a name for the formulation in the body of the paper. I will call it **action-FDT**.

The agent has a world-model consisting of a distribution $P$ and a graph $G$. The graph encodes causal structure and also *subjunctive dependence*: the relation that holds between two physical systems computing the same function. The paper's equation (4) is

$$
\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\big(V \,\big|\, \mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)\big).
$$

Here $\textsc{fdt}(\underline P,\underline G,\underline x)$ is a variable in the agent's model. It stands for the (logical) output of the FDT algorithm on input $(P,G,x)$. The $\mathtt{do}$ operator is Pearl's intervention, reused to perform surgery on a logical node instead of a physical one. Everything that subjunctively depends on that output changes in the hypothetical; everything else is held fixed.

Two features of action-FDT matter here.

- **Observations are handled without conditioning.** The paper says FDT "responds to observation by changing which node it intervenes upon." It does not condition on $\textsc{Obs}=x$.
- **Different inputs give different nodes.** The nodes $\textsc{fdt}(\underline P,\underline G,\underline{\text{full}})$ and $\textsc{fdt}(\underline P,\underline G,\underline{\text{empty}})$ are separate. When the agent intervenes on one, the others keep their prior distributions. In the transparent Newcomb analysis the paper writes $q$ for the agent's prior probability of two-boxing on seeing an empty box, and notes that the conclusion does not depend on $q$.

That second feature is exactly what P-FDT changes.

## 3. Defining P-FDT

### 3.1 The policy node

Let $\mathcal X$ be the set of possible inputs, meaning observation histories, and $\mathcal A$ the finite set of actions. A (deterministic) policy is a function $\pi:\mathcal X\to\mathcal A$, and the policy space is $\Pi=\mathcal A^{\mathcal X}$.

**Interpretive assumption 1 (mine).** The model contains a single node
$$
F := \textsc{fdt}(\underline P,\underline G),
$$
whose value lies in $\Pi$. It represents "the policy the FDT algorithm outputs on the model $(P,G)$." The observation is no longer an argument of the decision function. It is an argument of the policy the function returns.

The agent's physical action is a deterministic child of $F$ and of the observation variable:
$$
\textsc{Act} = F(\textsc{Obs}).
$$
Anything else that subjunctively depends on the decision function is also a child of $F$. Examples include a predictor's model of the agent, a twin, or a copy of the agent receiving a different input. Such a child may read any coordinate of the policy, $F(y)$ for any $y\in\mathcal X$. For instance, it may read what the agent *would* do on an input she will never actually receive.

Under this assumption, the paper's family of nodes $\{\textsc{fdt}(\underline P,\underline G,\underline x)\}_{x\in\mathcal X}$ becomes the family of coordinates of a single variable:
$$
\textsc{fdt}(\underline P,\underline G,\underline x)\ \equiv\ F(x).
$$

### 3.2 The decision rule

Define the *policy value*
$$
U(\pi) := \mathbb E\big(V \,\big|\, \mathtt{do}(F=\pi)\big),
$$
computed in the model $(P,G)$, with no conditioning on the actual observation. P-FDT is then

$$
\boxed{\ \pi^\ast := \arg\max_{\pi\in\Pi} U(\pi),\qquad \text{P-FDT}(P,G,x) := \pi^\ast(x).\ }
$$

In words: imagine the decision function's *entire input-output behavior* being set to each candidate policy. Propagate the consequences through every causal and subjunctive channel. Pick the best policy. Then do what that policy says for the input you actually have. This is the footnote's "choose ... a policy ... to which the agent then applies her inputs in order to select an action," made explicit.

### 3.3 The procedure, step by step

1. Build $(P,G)$. The graph includes a policy node $F$, the action node $\textsc{Act}=F(\textsc{Obs})$, and an edge from $F$ to every system that models or instantiates the decision function. Each such edge is annotated with which coordinates of $F$ that system reads.
2. For each $\pi\in\Pi$, compute $U(\pi)$ by intervention. Note that observations are downstream variables: different policies can change what the agent gets to see.
3. Select $\pi^\ast$. Break ties by a fixed canonical ordering of $\Pi$ that is part of the algorithm (see §6).
4. Output $\pi^\ast(x)$, where $x$ is the actual input.

### 3.4 Why the agent should not condition on $x$

The footnote does not say whether $U(\pi)$ conditions on the actual observation. I adopt the reading that it does not. This follows the paper's own treatment of action-FDT, and the transparent Newcomb problem shows the alternative fails.

Suppose the agent computed $\mathbb E(V\mid \mathtt{do}(F=\pi),\ \textsc{Obs}=\text{full})$. Given that the box is full, one-boxing yields \$1,000,000 and two-boxing yields \$1,001,000, whatever the intervention did to the *probability* of seeing a full box. Conditioning on the observation throws away exactly the dependence that makes P-FDT one-box. The paper makes the same point in prose: "FDT says that agents should entertain the hypothesis that, if their action were different, they might have *made different observations*." So in P-FDT the observation enters only at step 4.

## 4. Worked examples

### 4.1 Newcomb's problem: no difference

With no observation, $\mathcal X$ is a single point and $\Pi\cong\mathcal A$. P-FDT reduces to action-FDT. Following the paper's 99%-accurate predictor:

| Policy | Expected value |
|---|---|
| one-box | $0.99 \times 1{,}000{,}000 = \$990{,}000$ |
| two-box | $0.01 \times 1{,}001{,}000 + 0.99 \times 1{,}000 = \$11{,}000$ |

P-FDT one-boxes. In the smoking lesion problem, the paper's analysis turns on the agent being unsure which of two *models*, $P_S$ or $P_R$, she is running. Policies range over observations, not over models, so P-FDT inherits the paper's analysis unchanged and smokes.

### 4.2 Transparent Newcomb: the policy view made explicit

Now $\mathcal X=\{\text{full},\text{empty}\}$, so there are four policies. Write $(f,e)$ for the actions taken on seeing full and empty boxes. The predictor fills box B iff it predicts $F(\text{full})=\text{one}$, and it is accurate with probability 0.99. So:

- the probability that the box is filled is $0.99$ if $f=\text{one}$ and $0.01$ otherwise;
- the agent then sees the corresponding box and acts according to the corresponding coordinate.

| Policy $(f,e)$ | $U(\pi)$ |
|---|---|
| (one, two) | $0.99(1{,}000{,}000)+0.01(1{,}000) = 990{,}010$ |
| (one, one) | $0.99(1{,}000{,}000) = 990{,}000$ |
| (two, two) | $0.01(1{,}001{,}000)+0.99(1{,}000) = 11{,}000$ |
| (two, one) | $0.01(1{,}001{,}000) = 10{,}010$ |

The optimal policy is $\pi^\ast=(\text{one},\text{two})$. An agent who sees two full boxes outputs $\pi^\ast(\text{full})=\text{one}$, and so one-boxes, as action-FDT does. The paper's quantity $q$, the prior probability of two-boxing on seeing an empty box, has disappeared. P-FDT does not hold the empty-box behavior at a prior. It *chooses* that behavior together with the full-box behavior. In this problem the joint choice makes no difference, for reasons made precise in §5.

### 4.3 A coordination problem between copies: where the theories come apart

The following example is my own. It is meant to illustrate the footnote's "multi-agent dilemmas."

**Two-Room Coordination.** An agent is copied exactly; both copies share the model $(P,G)$. Each copy is placed in a separate room. A fair coin decides which room shows a red light and which shows a green light. Each copy sees only its own light and chooses $L$ or $R$. If the copies choose *differently*, each receives \$1,000,000. If they choose the same, each receives nothing. There is no communication.

**P-FDT.** We have $\Pi=\{L,R\}^{\{\text{red},\text{green}\}}$. Both copies are instances of the same function $F$, reading coordinates $F(\text{red})$ and $F(\text{green})$. Hence
$$
U(\pi)=1{,}000{,}000\cdot\mathbf 1[\pi(\text{red})\neq\pi(\text{green})].
$$
Two policies are optimal, $(L,R)$ and $(R,L)$. With a canonical tie-break, say lexicographic on the action order $L<R$, both copies compute $\pi^\ast=(L,R)$. The red copy plays $L$ and the green copy plays $R$, and both get rich. Coordination works because the two copies run *the same* argmax over *the same* policy space and then apply *different* inputs.

**Action-FDT.** The red copy intervenes on $\textsc{fdt}(\underline P,\underline G,\underline{\text{red}})$ and holds $\textsc{fdt}(\underline P,\underline G,\underline{\text{green}})$ at its prior. Let $q=P(\textsc{fdt}(\ldots,\text{green})=L)$. Then the red copy's expected values are
$$
\mathbb E[V\mid \mathtt{do}(\text{red}{=}L)] = (1-q)\cdot 10^6,\qquad \mathbb E[V\mid\mathtt{do}(\text{red}{=}R)]=q\cdot 10^6 .
$$
The green copy reasons symmetrically, with $r=P(\textsc{fdt}(\ldots,\text{red})=L)$. Two cases show the problem:

- If $q=r=0.4$, both copies choose $L$ and both get nothing.
- If $q=r=\tfrac12$, both are indifferent. A shared tie-break sends them to the same action, and again both get nothing.

Success requires the agent's priors about her own behavior on other inputs to already encode a coordinated solution. This echoes the paper's complaint that the agent of evidential decision theory (EDT) is "at the mercy of her priors." P-FDT removes the dependence: it treats behavior on unobserved inputs as something to *choose*, not something to *predict*.

## 5. When does the policy formulation matter?

The footnote's "so far as we can tell" invites a criterion. Here is one; the propositions are my own, though elementary.

Under Interpretive Assumption 1, action-FDT at input $x$ maximizes
$$
\bar U_x(a) := \mathbb E_{\pi_{-x}\sim\mu}\big[U(a,\pi_{-x})\big],
$$
where $\mu$ is the prior over the other coordinates. Intervening on one coordinate leaves the distribution of the others unchanged, as $\mathtt{do}$ on separate root nodes would.

**Proposition 1 (separability).** Suppose $U(\pi)=\sum_{x}u_x(\pi(x))$ for some functions $u_x$. Then for every prior $\mu$, action-FDT selects $\arg\max_a u_x(a)$ at each $x$. The assembled policy maximizes $U$, so action-FDT and P-FDT agree.

*Proof.* $\bar U_x(a)=u_x(a)+\text{const}$, and a separable sum is maximized coordinatewise. $\square$

**Proposition 2 (coordinatewise dominance).** Suppose there is a policy $\pi^\ast$ such that, for every $x$, every action $a$, and every $\pi_{-x}$,
$$
U(\pi^\ast(x),\pi_{-x})\ \ge\ U(a,\pi_{-x}).
$$
Then $\pi^\ast$ maximizes $U$, and action-FDT selects $\pi^\ast(x)$ at every $x$, for every prior (modulo ties).

*Proof.* Pointwise dominance survives taking expectations over $\mu$. Global optimality follows by switching an arbitrary policy to $\pi^\ast$ one coordinate at a time, which never lowers $U$. $\square$

Transparent Newcomb satisfies Proposition 2:

- "two-box on empty" is dominant, since it adds \$1,000 in the empty branch and the predictor never reads $F(\text{empty})$;
- "one-box on full" is dominant given either empty-box behavior, as the table shows.

That is why $q$ was irrelevant. The coordination game violates both propositions. The value of $F(\text{red})$ depends entirely on $F(\text{green})$.

When no dominance holds, the relationship between the two theories is the standard one from team decision theory (Marschak and Radner). If the priors $\mu$ are accurate about the agent's own behavior, then action-FDT's outputs form a *person-by-person optimal* policy: a Nash equilibrium among the function's own input-instances. P-FDT selects a *team-optimal* policy. Every team optimum is person-by-person optimal, but not conversely. The coordination game has the equilibria $(L,R)$ and $(R,L)$, but also a bad "equilibrium-in-beliefs" structure under symmetric priors.

On this analysis, "multi-agent" in the footnote is best read as *multiple instances of the same decision function, run on different inputs, whose outputs interact in determining the outcome*. Copies and twins with different information are the clearest cases. A predictor whose response depends jointly on several coordinates also qualifies, for example one that rewards the agent iff she would act the same way whether shown red or green. I cannot tell from the footnote whether its authors would count such single-agent-plus-predictor cases as "multi-agent." The criterion above suggests the relevant feature is the cross-input interaction, not the number of agents.

## 6. Unresolved choices and my proposed resolutions

Below, "source" marks claims taken from the paper and "proposal" marks my additions.

**(a) Which model counts as the prior?**
- *Source:* $P$ is the agent's model, and action-FDT intervenes without conditioning on $x$.
- *Gap:* For P-FDT, the time at which $P$ is fixed matters a great deal. If $P$ already incorporates an observation $y$, the policy can no longer vary behavior on inputs incompatible with $y$, and predictors who reacted to that behavior are treated as fixed.
- *Proposal:* $P$ should be the model from before any observation that may itself subjunctively depend on the policy. In practice, this is the model held when the problem's dependence structure was first in place: before the predictor predicted, the copy was made, or the letter was sent.

This is the formal content of the paper's claim that FDT agents "always act as they would have precommitted to act." Write $\Pi_{\text{commit}}\subseteq\Pi$ for the policies the agent could have bound herself to at the time of $P$. Since $\pi^\ast$ maximizes $U$ over all of $\Pi$, we have
$$
U(\pi^\ast)\ge \max_{\pi\in\Pi_{\text{commit}}} U(\pi),
$$
so no precommitment could do better by the agent's own ex ante lights. How much earlier a prior should be used is a substantive open question. Earlier priors make the agent pay in more "counterfactual" situations, in which her payment matters only to versions of the world she now knows she is not in. The mechanical blackmail discussion in the paper already shows this pattern: the agent refuses to pay "even though she *knows* that the blackmailer predicted wrongly."

**(b) Tie-breaking.**
- *Gap:* The source says nothing about ties.
- *Proposal:* Ties must be broken by a deterministic rule that is part of the algorithm and therefore shared by every instance. The coordination example shows this is not a technicality. Any instance-specific tie-break, one that peeks at $x$, can destroy the joint optimum.

**(c) Randomization.**
- *Source:* The footnote speaks of "a policy which maps inputs to actions," which reads most naturally as deterministic.
- *Gap:* Some problems reward randomization that predictors cannot anticipate, such as the paper's "truly random coin" in Death in Damascus, or imperfect-recall problems where one input recurs.
- *Proposal:* Where such sources are modeled, extend $\Pi$ to maps $\mathcal X\to\Delta(\mathcal A)$. The randomness must be genuinely outside the function's logical output; otherwise predictors of $F$ predict it.

**(d) What counts as "the same function"?**
- *Gap:* P-FDT unifies instances sharing $(P,G)$ that differ only in input. An agent with a slightly different model computes $\textsc{fdt}(\underline{P'},\underline G)$, a different node, so intervening on $F$ does not move it unless $G$ says otherwise.
- *Status:* The source names deducing such dependency structure as "perhaps the largest open problem," and that applies here too. P-FDT moves part of the problem (copies with different observations) into the policy space. It does not solve the general case.

**(e) Counterpossibles.**
- *Source:* Intervening on what the FDT function outputs is a counterlogical supposition, and the paper handles this by taking $G$ as given.
- *Status:* Policies do not remove this. Supposing $F=\pi$ for $\pi\ne\pi^\ast$ is exactly as counterpossible as supposing a different action. The "FDT′" variant the paper rejects, iterating over alternative functions, does not help for the reason the paper gives: predictors track $F$ itself.

**(f) Computation and infinite input spaces.**
- *Gap:* $|\Pi|=|\mathcal A|^{|\mathcal X|}$, which explodes with long observation histories. For infinite $\mathcal X$ the maximum may not even be attained.
- *Proposal:* For infinite $\mathcal X$, take near-optimal policies with $U(\pi)\ge\sup U-\varepsilon$, together with the canonical tie-break.
- *Source:* The paper already treats its equations as idealizations, expecting bounded approximations to inherit their qualitative strengths.
- *Proposal:* A practical shortcut follows from Proposition 2. Where coordinatewise dominance holds, the agent can safely optimize her current coordinate alone. Only interacting coordinates need joint search.

## 7. Using P-FDT on a new problem

Given an unfamiliar case, ask in order:

1. **Instances.** What are the inputs, and which systems compute or model the agent's decision function? Which coordinates $F(y)$ does each read?
2. **Observations as consequences.** Which observations are causally downstream of those systems? These must be modeled as consequences of the policy, not conditioned on.
3. **Policy values.** Write $U(\pi)$ for each policy, or at least for each combination of the interacting coordinates.
4. **Dominance check.** If each coordinate has a dominant choice, action-FDT and P-FDT agree, and the answer is read off directly.
5. **Joint optimum.** Otherwise, take the joint argmax with the canonical tie-break, then apply the actual input.

For the paper's own examples (Newcomb, transparent Newcomb, Parfit's hitchhiker, both blackmail problems, the twin prisoner's dilemma) step 4 succeeds, and P-FDT's verdicts coincide with those the paper reports. That is consistent with footnote 7's remark that the distinction "will not make a difference in this paper." The verdicts diverge in problems like Two-Room Coordination, where instances of one function must act differently from one another and no instance can do so by optimizing alone.

## 8. Conclusion

P-FDT takes FDT's central move, intervening on the output of one's decision function instead of on one's physical act, and applies it to the function's whole input-output behavior. Formally, the agent maximizes $U(\pi)=\mathbb E(V\mid\mathtt{do}(F=\pi))$ over policies in a model that does not condition on her observation, then applies her actual input to the result.

Where the payoff from behavior on different inputs is separable, or where each input has a dominant action, P-FDT agrees with the action-indexed equation in the paper's main text. Where instances interact, P-FDT selects a team-optimal policy, while action-FDT can stall at whatever its priors about its own other behaviors dictate.

The footnote leaves open which prior to use, how to break ties, whether to randomize, and which instances count as the same function. I have proposed resolutions for each: an early, pre-dependence prior; an algorithm-level canonical tie-break; mixed policies only for genuinely external randomness; and unification of same-model instances. The deepest open problems of FDT remain: counterpossible reasoning and learning the structure of subjunctive dependence.

## References

- Yudkowsky, E. and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060 (footnotes 7 and 16; equation (4)).
- Pearl, J. (2000). *Causality*. Cambridge University Press.
- Marschak, J. and Radner, R. (1972). *Economic Theory of Teams*. Yale University Press.