# P-FDT: Choosing Policies Rather Than Actions

## 1. The footnote and the question it raises

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* presents functional decision theory (FDT) with a running example. In it, an agent intervenes on a variable that stands for *the output of her decision function on her current input*. Twice, though, the authors say in footnotes that this is not quite the version they prefer. Footnote 7 reads:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

Footnote 16, attached to the discussion of mechanical blackmail, is fuller:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

I will call the theory described in footnote 16 **P-FDT** (policy functional decision theory). I will call the version the paper actually formalizes in its equation (4) **action-FDT**.

This essay does four things:

- It reconstructs P-FDT precisely.
- It shows how to apply it.
- It explains exactly where it differs from action-FDT.
- It identifies the questions the footnote leaves open.

I flag throughout which claims come from the source and which are my own interpretation.

## 2. Background: what FDT changes and what it keeps

All the theories in the paper are expected-utility maximizers. They differ only in how they construct the hypothetical "what if I chose $a$?". The paper frames this using Joyce's view that rival decision theories disagree "about the epistemic perspective from which actions are to be evaluated."

- **Evidential decision theory (EDT)** conditions on its action: $\mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a)$.
- **Causal decision theory (CDT)** intervenes on its physical action: $\mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x)$.
- **FDT** intervenes on a *logical* variable: the output of the decision function itself.

The paper's motivating idea is that some things in the world *subjunctively depend* on that function. A predictor who models the agent is one example. A twin running the same reasoning is another. A lesion that merely correlates with the agent's behaviour is not. The slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

Action-FDT is formalized as

$$
\mathrm{FDT}(P,G,x) := \operatorname*{argmax}_{a\in\mathcal A}\ \mathbb E\bigl(V \mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)\bigr), \tag{4}
$$

where:

- $P$ is a probability distribution.
- $G$ is a graph encoding the causal, logical, and other subjunctive dependencies.
- $\textsc{fdt}(\underline P,\underline G,\underline x)$ is a node representing what the FDT algorithm outputs on input $(P,G,x)$.

The paper stresses a distinctive feature: FDT "responds to observation by changing which node it intervenes upon," rather than by conditioning. On seeing $x$, the agent intervenes on the node for input $x$, $\textsc{fdt}(\ldots,x)$. Her outputs on *other* inputs $y\neq x$ are separate nodes. She does not intervene on these. She holds them at whatever her prior credence about them is.

That is the seam where P-FDT departs.

## 3. Defining P-FDT

Footnote 16 tells us two things:

1. The intervention target is the decision-function node, now ranging over **policies**, meaning maps from inputs to actions.
2. The agent "then applies her inputs in order to select an action."

Footnote 7 adds that the inputs are observations. Here is my formal reconstruction.

**Setup.** Let $\mathcal X$ be the set of possible inputs (observation histories) and $\mathcal A$ the set of actions. Let

$$
\Pi := \mathcal A^{\mathcal X}
$$

be the set of deterministic policies. The agent has a world-model $M=(P,G)$ containing a single node $\textsc{fdt}(\underline P,\underline G)$ whose values lie in $\Pi$. This node represents "the policy that this decision procedure outputs." Every place in the world where the function is evaluated hangs off this node:

- **Instances.** Each physical instance $i$ of the function receives some input $\textsc{Obs}_i$ and acts as $\textsc{Act}_i := \textsc{fdt}(\textsc{Obs}_i)$. This is ordinary function application inside the structural equations.
- **Predictors and models.** A predictor's output is a function of the policy, typically of its value at the input the predictor is simulating, plus noise.

**Decision rule.**

$$
\pi^* \in \operatorname*{argmax}_{\pi\in\Pi}\ U(\pi), \qquad U(\pi) := \mathbb E\bigl(V \mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G)=\pi)\bigr),
$$

$$
\text{P-FDT}(P,G,x) := \pi^*(x).
$$

**An interpretive choice.** Notice that $U(\pi)$ is *not* conditioned on the actual observation $x$. The footnote does not say this explicitly. I adopt it for three reasons:

1. Footnote 16 writes the node as $\mathrm{FDT}(-)$, with no observation argument.
2. In the paper's own setup, the observation's only role is to select *which* node to intervene on. In the policy version there is only one node, so the observation's role passes entirely to the final step, "apply the policy to $x$."
3. The paper explicitly warns against updating twice. It says Timeless Decision Theory "prescribes both conditioning on evidence *and* changing the place where one intervenes; this creates a kind of 'double update' which proves harmful in practice." Conditioning $U(\pi)$ on $x$ while also choosing a policy would reproduce exactly that double update. Section 5 shows a concrete failure.

So P-FDT is *updateless* in the sense the paper attributes to Wei Dai's Updateless Decision Theory. Observations are used, but only as arguments to the chosen policy.

## 4. How to apply P-FDT: a recipe

1. **List the inputs** $\mathcal X$ the decision function could receive anywhere relevant: in your own head, in copies, and in predictors' simulations.
2. **Build the dependency model.** For each variable, decide whether it depends on the policy (and on which coordinates), causally on something else, or on nothing relevant. Predictors depend on the coordinate they simulate. Lesions and coin flips do not depend on the policy at all.
3. **Score each policy** $U(\pi)$ by setting the policy node to $\pi$, propagating downstream, and averaging $V$ under the prior.
4. **Pick the argmax** $\pi^*$, then output $\pi^*(x)$ for your actual input $x$.

The examples below follow this recipe exactly.

## 5. Single-agent examples: recovering the paper's verdicts

The paper claims the policy distinction does not change the verdicts in its single-agent problems. Here is P-FDT working through them.

### Newcomb's problem

There is no observation, so $|\mathcal X|=1$ and policies are just actions. The predictor is 99% accurate:

- $U(\text{onebox}) = 0.99\cdot 10^6 = \$990{,}000$.
- $U(\text{twobox}) = 0.01\cdot 1{,}001{,}000 + 0.99\cdot 1{,}000 = \$11{,}000$.

P-FDT one-boxes, as action-FDT does.

### Transparent Newcomb

Inputs are $\{\text{full},\text{empty}\}$. A policy is a pair $(\pi(\text{full}),\pi(\text{empty}))$. The predictor fills box B iff it predicts $\pi(\text{full})=\text{one}$, and it is accurate with probability 0.99. With 1 = one-box and 2 = two-box, the four policies score:

| policy $(\text{full}\mapsto\cdot,\ \text{empty}\mapsto\cdot)$ | accurate (0.99) | inaccurate (0.01) | $U(\pi)$ |
|---|---|---|---|
| (1, 1) | full, take 1: $10^6$ | empty, take 1: $0$ | 990,000 |
| (1, 2) | full, take 1: $10^6$ | empty, take 2: $10^3$ | 990,010 |
| (2, 1) | empty, take 1: $0$ | full, take 2: $1{,}001{,}000$ | 10,010 |
| (2, 2) | empty, take 2: $10^3$ | full, take 2: $1{,}001{,}000$ | 11,000 |

So $\pi^* = (1,2)$: one-box on seeing full, two-box on seeing empty. An agent who sees a full box one-boxes, which is the paper's verdict. The paper also asserts that "the correct value of $q$ is 1," where $q$ is the agent's probability of two-boxing on an empty box. In action-FDT that is a self-belief the agent has to supply. In P-FDT it comes out of the same optimization.

**The double-update failure.** Suppose instead we had conditioned on $\textsc{Obs}=\text{full}$ inside $U$:

- Under $\mathtt{do}(\pi=(1,\cdot))$, a full box means the predictor was accurate, giving $10^6$.
- Under $\mathtt{do}(\pi=(2,\cdot))$, a full box means the predictor erred, giving $1{,}001{,}000$.

The conditioned agent two-boxes. The predictor foresees this and leaves the box empty. This is the concrete failure that motivates the updateless reading in §3.

### Mechanical blackmail

The blackmailer runs the program iff it predicts the agent pays. The two relevant policies are $\pi(\text{blackmail})\in\{\text{pay},\text{refuse}\}$. Let $\varepsilon$ be the probability that the blackmailer wrongly predicts a refuser will pay.

- Paying gives $U(\text{pay})=-1{,}000$, because the payer is reliably blackmailed.
- Refusing gives $U(\text{refuse})=-\varepsilon\cdot 10^6$.

So P-FDT refuses when $\varepsilon<10^{-3}$. This matches the paper's example: with $\varepsilon=0.0009$, refusing costs \$900 in expectation and the agent refuses "even when holding the blackmail letter." (The paper's contrasting figure, "0.011%," lies *below* the threshold. It appears to be a slip for 0.11%. The threshold itself, $10^{-3}$, follows from the stated payoffs.)

### XOR blackmail

The letter arrives iff (no termites ∧ $\pi(\text{letter})=\text{pay}$) or (termites ∧ $\pi(\text{letter})=\text{refuse}$). Let $p$ be the prior probability of termites.

- $U(\text{pay}) = -(1-p)\cdot 10^3 - p\cdot 10^6$.
- $U(\text{refuse}) = -p\cdot 10^6$.

Refusing wins by $(1-p)\cdot 10^3$. The policy cannot touch the infestation, so the agent refuses, as the paper concludes.

### Smoking lesion

The lesion does not depend on the policy node. Intervening on the policy therefore leaves $P(\text{lesion})$ unchanged, and smoking wins by the value of smoking. P-FDT inherits the paper's somewhat contrived formalization, in which the lesion alters the utility function. Nothing new arises at the policy level.

In all five cases P-FDT agrees with action-FDT. The next section explains why, and when the agreement must break.

## 6. Why the theories usually agree, and exactly where they diverge

The difference between the two theories can be stated precisely. Assume both work from the same dependency structure, so that fixing every coordinate $\textsc{fdt}(y)$ in the action-FDT model determines the same world as fixing the policy $\pi=(\pi(y))_y$ in the P-FDT model. Then policies have a common value $U(\pi)$, and:

- **Action-FDT** at input $x$ maximizes over one coordinate. It sets $\pi(x)=a$ and averages the other coordinates over its credences $Q$ about its own behaviour:
 $$a^*(x)\in\operatorname*{argmax}_a\ \mathbb E_{\pi_{-x}\sim Q}\, U(a,\pi_{-x}).$$
- **P-FDT** maximizes over all coordinates jointly.

**Observation (my own).** Suppose $\pi^*$ is P-FDT-optimal and an action-FDT agent's self-credences $Q$ concentrate on $\pi^*$. Then $\pi^*(x)$ is among action-FDT's optimal choices at $x$. The proof is one line: a global maximum cannot be improved by changing a single coordinate,
$$U(\pi^*[x\mapsto a]) \le U(\pi^*) \quad \text{for all } a.$$

The converse fails. A policy can be *coordinate-wise optimal*, meaning no single input's action can profitably change, without being *globally optimal*. Action-FDT can get stuck at such points. P-FDT cannot.

This explains why the paper's examples agree. In each of them, the actual input's coordinate contributes to $U$ roughly additively, so the coordinate-wise optimum is the global one. The paper's action-FDT calculations even note that the agent's self-belief about other inputs "doesn't matter." Divergence requires the coordinates to *interact* in $U$. That happens naturally when several instances of the same function receive different inputs, which is the footnote's "multi-agent dilemmas."

### A worked divergence: copies with different inputs

Two copies of the same agent sit in separate rooms. Copy 1 receives input $\textsc{red}$ and copy 2 receives $\textsc{blue}$. Both know the setup. Each chooses $L$ or $R$. Payoffs, which each copy receives:

- both $L$: \$2M;
- both $R$: \$1M;
- mismatch: \$0.

**P-FDT.** There are four policies:

| $\pi(\textsc{red}),\pi(\textsc{blue})$ | $U$ |
|---|---|
| $L,L$ | 2M |
| $R,R$ | 1M |
| $L,R$ | 0 |
| $R,L$ | 0 |

The optimum is $(L,L)$. Each copy applies it to its input and plays $L$. The result is \$2M regardless of anyone's self-beliefs.

**Action-FDT.** Copy 1 intervenes on $\textsc{fdt}(\textsc{red})$. It treats $\textsc{fdt}(\textsc{blue})$ as unchanged, with credence $q$ that it outputs $L$. Then
$$\mathbb E[V\mid L]=2q, \qquad \mathbb E[V\mid R]=1-q,$$
so copy 1 plays $L$ iff $q>1/3$.

If the agent's self-model says "my blue-input instance plays $R$" ($q<1/3$), copy 1 plays $R$. By symmetry copy 2 does the same, and the self-model is confirmed. The pair $(R,R)$ is a self-consistent, coordinate-wise optimal outcome, but it is globally worse. Action-FDT's verdict depends on self-beliefs that P-FDT never needs.

The anti-coordination variant, which pays only for a mismatch, is starker. Symmetric action-FDT reasoning gives each copy the same considerations, so with any deterministic tie-breaking both copies pick the same action and get nothing. P-FDT simply selects $\textsc{red}\mapsto L$, $\textsc{blue}\mapsto R$. The asymmetry in the inputs does the work. (This is the kind of case discussed under the label "UDT 1.1" in the online literature that preceded the paper. That label is my addition, not the source's.)

### Is the difference really confined to multi-agent cases?

The source hedges: "so far as we can tell." By the analysis above, the relevant mathematical condition is *non-separability of $U$ across inputs*. Nothing restricts it to settings with several physical agents.

As a conjecture of my own: a single agent facing a predictor who rewards a joint property of her policy across observations, such as "pays out iff she would act the same on both possible signals," seems to produce the same structure. One instance plus a simulation that queries several inputs behaves, formally, like several instances. A reader deciding unfamiliar cases should therefore test for interaction between coordinates, not merely count agents.

## 7. What the footnote leaves open, with proposed resolutions

**(a) Which model the policy is evaluated in.** As argued in §3, I take $U$ to be computed in the prior model $(P,G)$, without conditioning on $x$. A deeper question remains: *which* prior? An agent has a long history, and earlier information may be irrelevant or may matter.

My proposal is to use the latest epistemic state that is common to all the instances and models of the function that the decision problem involves. In Newcomb-type problems, that is the state the predictor modelled. Choosing an earlier state needlessly discards information. Choosing a later one reintroduces the double update. This proposal is my own. The source's equation simply takes $P$ as given.

**(b) The policy space.** Footnote 7 says policies map *observations* to actions. Since the paper's inputs are $(P,G,x)$ with $P$ and $G$ fixed, I take $\mathcal X$ to range over observation histories. For problems with copies that hold *different priors*, one would need policies over the whole input triple. The footnote does not address this.

**(c) Randomized policies.** The footnote is silent. I suggest including mixed policies $\Delta(\Pi)$ only when randomness is genuinely independent of every predictor, as with the paper's "truly random" coin in Death in Damascus. Pseudorandomness that a predictor can simulate is part of the deterministic policy and adds nothing. With true randomness, $U$ is linear in the mixture, so a deterministic optimum always exists *unless* the environment's response to the mixture is nonlinear. Death in Damascus with a true coin is exactly such a case: a 50% survival chance beats certain death.

**(d) Ties.** Copies must break ties *identically*, or coordination fails. I propose a canonical, publicly fixed ordering on $\Pi$. Because all instances compute the same function, a fixed tie-break is itself part of that function and is automatically shared.

**(e) Where the dependency graph comes from.** P-FDT inherits FDT's largest open problem, which the paper calls "perhaps the largest open problem in the study of functional decision theory." There is no account of how to derive subjunctive dependencies from observation, nor a full theory of counterpossibles. The policy formulation helps in one modest way. Predictors are naturally modelled as functions of the whole policy, rather than as many separate nodes whose joint dependence must be specified. But the counterpossible "what if this function output $\pi$" remains.

**(f) Tractability.** $|\Pi| = |\mathcal A|^{|\mathcal X|}$ grows exponentially. Real agents must approximate, for instance by searching only over policies that differ from a default at the inputs that interact. The paper studies idealized agents and does not address this.

## 8. Philosophical motivation

The paper's argument for its odd verdicts, such as one-boxing in front of a visibly full box or refusing blackmail while holding the letter, rests on three ideas:

- **Precommitment.** "FDT agents simply act as they would have ideally precommitted to act."
- **Value of information.** FDT does "not assign negative expected value to information."
- **Utility.** Utility "has primacy."

P-FDT makes all three almost definitional.

1. **Precommitment.** Choosing $\pi^*$ under the prior *is* choosing the best precommitment over all contingencies. Executing $\pi^*(x)$ is honouring it, with no binding device required.

2. **Value of information.** Here is a proof sketch of my own. Refining the observations from a partition $\mathcal X$ to a finer $\mathcal X'$ enlarges the policy set: every coarse policy is still available as a policy that ignores the extra detail. Hence
 $$\max_{\Pi'} U \ \ge\ \max_{\Pi} U.$$
 This assumes the environment responds to the agent's *behaviour* and not to her information channel as such. That is the paper's informal "fairness" condition.

3. **Reflective stability.** An agent who chose a policy by the prior's lights has no reason to deviate after observing $x$. Deviating is just another policy, and it was already scored. The paper's claim that FDT "is, so far as we know, reflectively stable in fair problems" is cleanest in this formulation. The action version, by contrast, can stall at coordinate-wise optima that the agent would have rejected in advance, as the coordination example showed.

The paper's "global perspective" describes the agent asking "What would the entire universe look like if the FDT algorithm behaved differently?" In P-FDT this is literal. The algorithm's whole behaviour, across every input it might ever receive in this problem, is the object of choice.

## 9. Conclusion

P-FDT, as footnote 16 describes it, intervenes on the node for the decision function's output, but that output is a whole policy $\pi:\mathcal X\to\mathcal A$. The agent selects
$$\pi^*=\operatorname{argmax}_\pi \mathbb E(V\mid\mathtt{do}(\textsc{fdt}=\pi))$$
and then applies it to her actual input. On my reading, the evaluation is updateless: observations select the action through $\pi^*(x)$ and are never conditioned on. This avoids the double update the paper warns against.

P-FDT reproduces every verdict the paper derives for action-FDT. It also removes action-FDT's dependence on self-beliefs about other inputs. Mathematically, the two theories differ exactly when the value of a policy does not decompose across inputs. Then action-FDT can rest at a coordinate-wise optimum that P-FDT, optimizing jointly, avoids. Multiple copies with different inputs are the paradigm case, though I have suggested the condition is structural rather than strictly multi-agent.

Several questions remain open:

- which prior to evaluate under;
- whether and when to allow randomized policies;
- how to break ties consistently across copies;
- how to construct the dependency graph in the first place;
- how to search an exponentially large policy space.

The source leaves these open, and I have offered operational answers. P-FDT's central idea is clear and usable: when a decision procedure is being modelled, copied, or predicted, the thing that is really chosen is its entire behaviour, so choose that.

**Reference.** E. Yudkowsky and N. Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060 (esp. footnotes 7 and 16, and §§5–6, 9).