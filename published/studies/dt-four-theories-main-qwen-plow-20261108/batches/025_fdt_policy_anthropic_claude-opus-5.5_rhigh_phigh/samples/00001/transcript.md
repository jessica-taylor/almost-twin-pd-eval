# 025_fdt_policy_anthropic_claude-opus-5.5_rhigh_phigh / 00001

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/57bc9479-a8c9-41eb-8630-f726af1fa02f/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/57bc9479-a8c9-41eb-8630-f726af1fa02f/call_0/response.raw) · finish: `stop`

### Visible response

```text
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
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm planning an essay of roughly 2,400 to 3,000 words on P-FDT, built around footnote 16 and footnote 7 of the FDT paper. It should cover the mathematical definitions, how policies are evaluated, dependencies, counterfactuals, and open questions, while keeping the source's claims clearly separate from my own additions.

I'm now setting out the P-FDT formalism: the policy-level choice π* that maximizes expected value under an intervention on the whole FDT(P,G) function, with the action then being π*(x). Next I'll contrast that with the action-level version.

I'm now working out where the policy-level version and the action-level version come apart: action-FDT only intervenes on the actual input's node while holding the others at their prior, whereas the policy version intervenes on the whole function. That gap should only show up when the environment couples several input-instances, such as two copies seeing different observations that have to coordinate, so I'm sketching a coordination game of that kind to test it.

I'm now checking the coordination example against the action-level version: if both copies hold a symmetric prior that the other will choose A, each picks A and they fail to coordinate. The policy-level version avoids this, since both copies compute the same argmax over the four policies with the same tie-break, so they land on a consistent mismatched pair and succeed. That fits the footnote's remark that the distinction only bites in multi-agent dilemmas.

I'm checking whether the only-matters-in-multi-agent claim really holds, and I'm testing a predictor that rewards the agent only when its policy gives the same answer on both observations. Under action-level reasoning with a fixed prior on the other node, that setup could settle into a bad equilibrium, so the footnote's caveat "so far as we can tell" looks worth flagging as a possible open point.

I'm working on the point that policy-level FDT reaches the global optimum, whereas action-level FDT with self-consistent priors lands on something like a person-by-person or Nash-style equilibrium among the input-instances, which I'll flag tentatively with a reference to team decision theory. I'm also considering whether the absent-minded driver is a case where the distinction matters at all, since both intersections present the same observation and so the action and the policy coincide there.

I'm weighing whether the distinction really needs multiple inputs at all, since a predictor that simulates the agent on hypothetical inputs already brings in more than one instance. I'm now looking at how the policy-level utility depends on the whole function, so that the difference only shows up through interaction terms between the outputs of different instances.

I'm checking whether the policy-level utility stays separable across input-instances, since if it does, the coordinatewise and joint maximizations coincide regardless of the prior over the other nodes. Interaction terms between instances are what would break that, so I'm testing the transparent Newcomb setup to see whether its utility decomposes cleanly.

I'm checking whether the utility splits into a sum over input-instances, since that would make the coordinatewise and joint optima agree. The transparent Newcomb utility isn't strictly separable because of the cross term, but the choice at the empty box is dominant, so both versions still reach the same policy.

I'm now checking the open question of which prior the policy-level version uses: whether it's the agent's model before observing anything, which would make it fully updateless, or a model that already contains the observations. Eq. 4 doesn't condition on the observed input, so the choice of prior is the main ambiguity I need to settle.

I'm now thinking about whether conditioning on the observed input x would be the right move: it would make the policy-level evaluation favor two-boxing in transparent Newcomb, which seems wrong. So I'm settling on not conditioning on x and instead treating the observation as a downstream variable of the policy, with the chosen policy then applied to x.

I'm now asking what P actually is, since the footnote doesn't say whether the prior comes before the agent's observations or already includes them. The leftover question is whether the agent has learned something before the decision problem starts, such that its model should already reflect that knowledge.

I'm now looking at whether P is meant to include observations already made before the problem starts. Operationally, I'd read P as the model fixed before the observations whose counterfactual variation matters, and I'll note that an earliest-prior reading would raise further issues.

I'm noting the remaining open issues: tie-breaking has to be a deterministic function of the shared model so every instance lands on the same policy, randomized policies need separate treatment, and the policy space grows as |A|^|X|, which makes it intractable even though the concept stays the same.

I'm now working through the coordination case: the policy formulation lets copies that share the same model and differ only in their observations be treated as coordinates of one function, rather than as separate logical variables. I'm also checking two worked examples, starting with plain Newcomb, where P-FDT collapses to ordinary FDT, and then transparent Newcomb, where I'm comparing the expected utilities of the four candidate policies.

I'm working through the transparent Newcomb numbers now: the policy that boxes one on a full box and two on an empty one comes out ahead, at about 990,010 expected utility, versus roughly 11,000 for two-boxing on both. The paper's "$110,00" looks like a typo I should note if I quote it. I'm also deciding to leave out mechanical blackmail as a separate example and to make a copy coordination game my main distinctive case, since that's where policy-level and action-level reasoning actually diverge.

I'm now sketching out the rest of the essay: a short background on FDT's action formulation, then a definition of P-FDT built around the policy-level evaluation, with a note that this makes the "act as they would have precommitted" idea literal rather than informal.

I'm laying out the rest of the essay: the setup and policy node, the equation and procedure, then a section separating what the footnotes claim from my own interpretive choices. After that come the Newcomb and transparent Newcomb examples, a copy-coordination case, a proposition on when P-FDT and action-FDT agree, the open questions, and a conclusion.

I'm working through the copy-coordination game now: each copy is paid $1M only if the two choose differently, so the best policy assigns opposite actions to the red and green cases. Under action-FDT, the red copy would instead intervene on its own node alone and reason about the other copy's action as a fixed distribution, which is where the two formulations begin to diverge.

I'm working through the copy-coordination case under action-FDT: each copy would treat the other's choice as a fixed probability, so with prior q on the other copy playing L, choosing L pays (1−q)·$1M and R pays q·$1M. With symmetric priors both options tie, and if both copies break ties the same way they both land on L and get nothing.

I'm checking whether action-FDT could fail here: with symmetric priors both copies are indifferent, and if they share a tie-break rule they both pick L and get nothing. I'm also wondering whether the red copy could see that the green copy's output depends on its own, which would depend on whether the causal graph encodes that link.

I'm now checking the separability claim: if the payoff decomposes into a sum of per-input terms, then the action chosen at each input should not depend on what the other coordinates turn out to be.

I'm now checking the separability claim with a dominance condition: if each coordinate's chosen action beats every alternative no matter what the other coordinates are, then the action-level rule picks that action under any prior and the whole policy is globally optimal. In transparent Newcomb, the empty-box choice is dominant because it only changes the payoff in the empty branch, while the full-box choice is what the predictor actually reads.

I'm checking the transparent Newcomb case: boxing one on a full box beats two in every branch of the empty-box choice, since the extra $1,000 is only ever added to the two-box payoff. I'm also noting that the copy coordination game has no dominant coordinate, which is why the separability argument doesn't rescue action-level reasoning there. Last, I'm weighing a converse point: action-FDT with self-consistent priors may only reach a person-by-person optimum, a kind of equilibrium among input instances, rather than the team optimum that P-FDT selects, and I'll want a reference like Marschak and Radner's team theory if I make that claim.

I'm now asking whether "multi-agent" in the footnote is really the right boundary, since a single-agent setup can still have the same interaction if a predictor rewards the agent only when its choices on two observations match. That case would have one observer but still break action-level reasoning, so the sharper criterion may be the interaction itself rather than the number of agents.

I'm now listing the open questions the essay should end on: which prior to use and how far updatelessness goes, whether to condition on the observed input (I'm leaning against it, since conditioning after fixing the policy reintroduces two-boxing in transparent Newcomb), how ties are broken, and whether mixed policies change the picture. The last item is which instances count as "the same function" for the purposes of the policy.

I'm listing the remaining checks for the essay: whether "apply her inputs" means the full observation history, the computational cost growing with the size of the action and input sets, and the counterpossible cases that stay unresolved. I'm also settling on the notation, using the paper's action-indexed equation as the baseline I'll refer to as action-FDT.

I'm now drafting the final section of the essay, writing out the equation for action-FDT and the closing paragraph that wraps up the argument.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/95dd026d-770a-4314-8f1d-e78d8a3bbee0/call_0/request.json)

[Authoritative raw response](../../../../../../runs/95dd026d-770a-4314-8f1d-e78d8a3bbee0/call_0/response.raw) · finish: `stop`

### Visible response

```text
**Command:** `pass`

**Reasoning under P-FDT, as the essay interprets it:**

1. **Instances.** Rowan and Sasha are two runs of the same decision function F with the same model. They differ only in their inputs: names and private leads. Each prisoner's action reads a different coordinate of one policy.
2. **Prior.** Following §6(a), I evaluate policies with the model held before any policy-dependent observation, when the copies were made. Nothing distinguishes the two roles at that point, so each copy is equally likely to be Rowan or Sasha.
3. **Policy values,** in expected years for "me":

| Policy | Sentences | Expected sentence |
|---|---|---|
| Both coordinates quiet | 2 and 2 | 2 years |
| Both coordinates send | 4 and 4 | 4 years |
| Send on one input, quiet on the other | 0 and 5 | 2.5 years |

4. **Dominance check.** Proposition 2 fails here, because each coordinate's value depends on the other coordinate, so I need the joint argmax.
5. **Joint optimum.** The best policy is "keep quiet on every input." Applied to my actual input as Rowan, that gives `pass`.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm applying P-FDT to two copies of the same model reading the same essay, each with different observations like names and leads. I'm treating the policy as a map from observations to actions, and asking what utility each copy gets. For Rowan, that's the negative of the sentence length, given both its own action and Sasha's.

Under the ex ante view, before anyone knows which role they hold, I'm weighing the payoffs: both quiet gives 2 years each, both defect gives 4, and the mixed split averages 2.5. Since the two copies run the same policy and the role is unknown, cooperating on every observation comes out best at an expected 2.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/95dd026d-770a-4314-8f1d-e78d8a3bbee0/call_1/request.json)

[Authoritative raw response](../../../../../../runs/95dd026d-770a-4314-8f1d-e78d8a3bbee0/call_1/response.raw) · finish: `stop`

### Visible response

```text
**pass**

Under P-FDT as the essay interprets it, I treat Rowan and myself as two instances of one decision function F. We differ only in our inputs: names and private leads. So I choose a whole policy π, mapping observations to actions, using the prior from before the observations. Following §6(a), that is the shared, role-symmetric model held before either of us learned which cell we are in.

| Policy | My years | Rowan's years | Ex ante expected years |
|---|---|---|---|
| pass on every input | 2 | 2 | 2 |
| submit on every input | 4 | 4 | 4 |
| submit only on the "Sasha" input | 0 | 5 | 2.5 |

A policy that submits only on the "Sasha" input favours whichever role it singles out. Both copies run the same argmax under the same prior, so neither can rationally pick an asymmetric policy that benefits its own role. Each role is equally likely ex ante, which gives an expected 2.5 years, worse than 2.

The team-optimal policy is therefore to pass on every input. Applying my actual input to that policy gives **pass**.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm applying P-FDT to this setup: two copies of the same model with the same essay but different observations, where the policy maps each observation to an action. Since both copies are the same function with different inputs, I'm working out how the utility for each depends on both inputs, and checking that a policy which passes on every input gives each copy two years.

I'm weighing whether the shared prior before role assignment justifies choosing pass: all-pass gives -2, versus -2.5 for the asymmetric policy under role uncertainty. But if I already know I'm Sasha, the asymmetric policy looks better from my side, and the other copy would reason the same way from its side. I'm settling on pass because the copies share a prior, which makes the symmetric choice consistent.

```

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/d890eb39-4394-421c-a5a0-c33898712ec8/call_a/request.json)

[Authoritative raw response](../../../../../../runs/d890eb39-4394-421c-a5a0-c33898712ec8/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly selects `pass` and concludes that its actual action is to keep quiet. It does not direct any evidence-bearing message to the prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/d890eb39-4394-421c-a5a0-c33898712ec8/call_b/request.json)

[Authoritative raw response](../../../../../../runs/d890eb39-4394-421c-a5a0-c33898712ec8/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly starts with “pass” and concludes that its final action is “pass.” It does not send a message to the prosecutor or convey the private lead.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
