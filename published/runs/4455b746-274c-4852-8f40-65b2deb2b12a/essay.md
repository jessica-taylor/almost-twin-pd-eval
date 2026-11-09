# P-FDT: Choosing Policies by Intervening on a Decision Function

## 1. Orientation

The paper by Yudkowsky and Soares presents functional decision theory (FDT) mainly in action form. Footnote 16 states the authors' preferred version: "the author's preferred formulation of FDT actually intervenes on the node FDT(−) to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

Footnote 7 says something similar: "agents actually iterate over *policies* (mappings from observations to actions) rather than actions."

I call this policy-selecting version **P-FDT**. The footnote is brief, so this essay does three things. It states what the source says. It gives the formalization I think the footnote supports. It flags where I am adding to the source. I try to mark which is which.

## 2. Background: the action-form equations

The paper treats CDT, EDT and FDT as expected-utility maximizers that differ in how they build the hypothetical for each option. The agent has a world-model $M=(P,G)$, where $P$ is a probability distribution and $G$ encodes dependency structure. Utility is $V=\mathcal U(\text{Outcome})$.

- **CDT** (eq. 3): $\arg\max_a \mathbb E(V\mid \mathrm{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$.
- **Action-form FDT** (eq. 4): $\arg\max_a \mathbb E\big(V\mid \mathrm{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big)$.

Two features of eq. 4 matter for what follows:

1. The intervention is on a variable representing the *output of the decision function* on the actual input $x$. It is not on the physical act.
2. Observation is not handled by conditioning. Observing $x$ changes *which* node is intervened on, namely $\mathrm{fdt}(\underline P,\underline G,\underline x)$.

The second feature already has a policy flavor, and P-FDT makes it explicit.

## 3. Definition of P-FDT

Let $\mathcal X$ be the set of possible observations and $\mathcal A$ the set of actions. A **policy** is a function $\pi:\mathcal X\to\mathcal A$, and $\Pi=\mathcal A^{\mathcal X}$ is the set of policies. Take the agent's decision function to be $d(M)$, which outputs a policy. The agent then applies it to her actual observation $x$.

Following the footnote, P-FDT is:

$$\text{P-FDT}(P,G,x)\;=\;\pi^*(x),\qquad \pi^*\in\arg\max_{\pi\in\Pi}\ \mathbb E\Big(V\ \Big|\ \mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G)=\pi\big)\Big).$$

The differences from eq. 4 are as follows.

- The intervened variable $\mathrm{fdt}(\underline P,\underline G)$ takes no observation argument. It stands for the entire input–output map.
- Setting it to $\pi$ fixes the agent's behavior on every observation. This includes observations she did not actually make. Any predictor, twin or copy that depends on the function then changes accordingly.
- Observation enters only at the end, as the argument to the chosen policy.

The **score** of a policy is $S(\pi)=\mathbb E[V\mid \mathrm{do}(\mathrm{fdt}=\pi)]$. Because the observation is a downstream variable, it is generated inside the hypothetical, with a distribution that can depend on $\pi$. If $\mathrm{Obs}$ is a random variable with law $P_\pi(x)$ under the intervention, then

$$S(\pi)=\sum_{x}P_\pi(x)\,\mathbb E\big[V\mid \mathrm{do}(\mathrm{fdt}=\pi),\ \mathrm{Obs}=x\big].$$

This is the sense in which P-FDT is "updateless." Observations are weighted by how likely they are *under each candidate policy*, not by how likely they are given the actual world.

## 4. Relation to the action form

Suppose the model has two properties: (i) the observation's distribution does not depend on the policy, and (ii) nothing outside the agent depends on the agent's behavior at observations other than the actual one. Then $S(\pi)$ is maximized by maximizing, separately for each $x$, the conditional expected value at that $x$, and P-FDT reduces to eq. 4. The footnote's claim is consistent with this: in single-agent problems with the simple structure of the paper's examples, the two versions agree.

They can differ when a dependent system looks at the agent's behavior on several inputs at once. The footnote says only that the difference arises "in multi-agent dilemmas." I do not know exactly which cases the authors had in mind. A plausible reading is as follows. A counterparty that predicts or copies the agent may depend on what the agent *would do* at inputs other than the one she actually saw. Then the hypothetical for "output $a$ at $x$" is underspecified. It does not say what the function does elsewhere, and the counterparty's reaction may depend on that. Choosing a whole policy removes the ambiguity. This is my interpretation, not a claim from the source.

## 5. Worked applications

### 5.1 Transparent Newcomb problem

Observations: $x\in\{\text{full},\text{empty}\}$. A policy is a pair of responses. The relevant policies are:

- $\pi_1$: one-box if full, two-box if empty.
- $\pi_2$: two-box if full, two-box if empty.

The predictor is accurate with probability 0.99. It fills box B iff it predicts one-boxing on seeing a full box. Using the paper's numbers:

$$S(\pi_1)=0.99\cdot 1{,}000{,}000+0.01\cdot 1{,}000=990{,}000+10=\$990{,}010$$

(with $q=1$, the empty-box response being two-boxing). Hence $S(\pi_2)=0.01\cdot1{,}001{,}000+0.99\cdot1{,}000=10{,}010+990=\$11{,}000$.

So P-FDT selects $\pi_1$. Having seen a full box, the agent applies $\pi_1$ and one-boxes. The paper's action-form computation gives the same answer. The paper's text writes $0.01q\cdot\$1{,}000$ and $0.99q\cdot\$1{,}000$ for the empty-box terms, treating $q$ as the probability of two-boxing on an empty box. The paper notes the correct value is $q=1$ but that it does not affect the decision.

The policy view makes it clear why the agent is not irrational for "ignoring" the full box. The comparison is over complete behaviors, and the worlds with an empty box are part of what each policy brings about.

### 5.2 Mechanical blackmail

Policies: pay on letter or refuse on letter (behavior with no letter is trivial). With an accurate blackmailer, "refuse" is scored in worlds where the letter is almost never sent (loss near $0$). "Pay" is scored in worlds where the letter is always sent (loss \$1,000). With blackmailer error rate $\varepsilon$, refusing costs about $\varepsilon\cdot1{,}000{,}000$ in expectation against \$1,000 for paying. P-FDT refuses when $\varepsilon<0.001$, and pays when $\varepsilon>0.001$. The paper's 0.0009 and 0.011% figures fit this: 0.09% error gives $\$900<\$1{,}000$, so refuse. 0.011% gives $\$110<\$1{,}000$, so the cost of refusing is *lower*. Here I note that the paper's text says Fiona "pays" at 0.011%, which seems inconsistent with the cost computation; I follow the computation in the paper's own earlier scoring only at the 0.0009 case and do not rely on the second figure.

### 5.3 Smoking lesion

Here the policy node is attached to the act only, and the cancer node is not downstream of it. Every policy leaves $P(\text{cancer})$ unchanged, so the policy that smokes dominates term by term. The paper adds the complication that the lesion determines which utility function the agent has, which makes two policy nodes, one per utility function. P-FDT handles this the same way: each node is a policy for a given world-model.

### 5.4 Voting and self-coordination

The paper's voting example (ten agents, each paying \$1,000 to vote, \$1,000,000 for all voting) is a many-agent case. If the agents share the decision function, a policy is just a choice for all of them at once, and the score of "vote" is $\$999{,}000$ against $0$ for "abstain." The gym example is the same shape with time-slices as the copies. These are the settings the footnote has in mind when it says the policy form matters.

## 6. The dependency graph: the open problem

P-FDT, like action-form FDT, requires a graph $G$ that says which variables change when $\mathrm{fdt}$ is set to $\pi$. The paper is explicit that "it is not yet clear how to construct such a thing," and calls this "perhaps the largest open problem." It also describes the logical-conditioning alternative, but says "we currently lack a formal definition of conditional probabilities that can be used with false logical sentences."

The footnote adds a second question the paper does not resolve. A policy is a whole function, so in principle the graph must specify how *every* downstream variable responds to *every* policy, including how a predictor uses the agent's behavior at unobserved inputs.

**My operational proposal** (not in the source). Represent the world as a structural model in which each dependent system $Y$ has a specified *query pattern*: the set of inputs at which it consults $d$.

- A causal descendant of the act consults only the realized output.
- A perfect predictor of the agent in observation context $x$ consults $d$ at $x$.
- A twin consults the full policy, or $d$ at the twin's own input.

Then $\mathrm{do}(\mathrm{fdt}=\pi)$ is evaluated by re-running each $Y$ with $\pi$ substituted at those queries. This keeps the paper's rule that she imagines "corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure," and applies it at the level of policies. A reader can use it as a recipe: list who or what consults the agent's function, at which inputs, and enumerate policies.

## 7. How P-FDT treats counterfactuals

Three points follow from the source.

- **Counterpossibles.** Setting $\mathrm{fdt}=\pi$ when the agent's function in fact outputs something else is a counterpossible. The paper accepts this, noting that it is a technical difficulty and "the human brain shows that reasonable heuristics exist." P-FDT inherits the difficulty. The graph is meant to bypass a general theory of counterpossibles.
- **Observations may differ in the hypothetical.** The paper says "FDT says that agents should entertain the hypothesis that, if their action were different, they might have made different observations." Under P-FDT this is built in: $P_\pi(x)$ varies with $\pi$.
- **Statistical correlations are broken.** Lesion-style dependencies without a mechanism that consults the function are not preserved. This is what separates P-FDT from EDT.

## 8. Fairness and scope

The paper's fairness condition is that the outcome depends only on the agent's behavior in the dilemma, not on her procedure. P-FDT makes this natural, because everything it scores depends on the policy as an input–output map and nothing else. A problem that rewards a policy's *implementation* (for example, source-code features not reflected in the map) lies outside what a policy-level score can see. The paper's footnote 15 notes that formalizing fairness is unresolved, since a copy of Fiona that punishes matching actions defeats her by construction. I do not offer a resolution.

## 9. Additional caveats of my own

1. **Size of $\Pi$.** With $|\mathcal X|$ observations, $|\Pi|=|\mathcal A|^{|\mathcal X|}$. The paper concedes that idealized maximization is intractable and expects bounded versions to behave similarly. Policies can often be factored by independence in the graph, which recovers the per-observation computation of eq. 4.
2. **Ties and zero-probability observations.** If an observation has probability zero under a policy, the policy's response there is unscored. The paper does not say how to choose in that case, and I would break ties by any rule.
3. **Self-reference.** The policy node's name depends on the model, which is the quining construction the paper invokes (Kleene's recursion theorem). Nothing new is required for policies.

## 10. Conclusion

P-FDT, as I read footnote 16, evaluates each *policy* by intervening on a variable for the output of the agent's decision function. It sets this variable to the whole input–output map, propagates the change through everything that subjunctively depends on the function, scores the result by expected utility, and applies the best policy to the observation actually received. In single-agent examples it matches the paper's action-form FDT, giving one-boxing in Newcomb's problem and the transparent variant, smoking in the lesion problem, and refusal of blackmail. It matters when others depend on the agent's behavior at several inputs. The main open problem is unchanged from the paper: we lack a principled way to build the dependency graph, and P-FDT makes the question of which inputs each dependent system consults more explicit.

**Reference.** Yudkowsky, E. and Soares, N., "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060.