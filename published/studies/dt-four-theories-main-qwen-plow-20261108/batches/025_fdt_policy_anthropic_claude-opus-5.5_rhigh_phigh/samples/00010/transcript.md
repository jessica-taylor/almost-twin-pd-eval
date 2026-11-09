# 025_fdt_policy_anthropic_claude-opus-5.5_rhigh_phigh / 00010

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/b6cecf5a-871b-42df-a35b-ff354d162dee/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/b6cecf5a-871b-42df-a35b-ff354d162dee/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Policy Functional Decision Theory (P-FDT): Choosing the Whole Map from Inputs to Actions

## 1. The passage and the question it raises

Yudkowsky and Soares's paper *Functional Decision Theory* mostly develops a version of FDT that chooses **actions**. Two footnotes say that this is not the authors' preferred formulation. Footnote 7 says:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

Footnote 16, which I take as the primary source for this essay, is attached to the remark that "FDT says that agents should entertain the hypothesis that, if their action were different, they might have *made different observations*." It reads:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node FDT(−) to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

I will call the theory described here **P-FDT** (policy functional decision theory). When I mean the version developed in the paper's main text, I will call it **action-FDT**. The footnote has three parts:

1. the agent intervenes on a node representing the output of her decision function;
2. the value set at that node is a policy, a function from inputs to actions;
3. the agent then applies the chosen policy to her actual input.

The footnote does not say several things. It does not say which probability distribution the policy is evaluated under. It does not say whether the expectation conditions on the current observation, what the policy space contains, or exactly why the difference "only matters in multi-agent dilemmas."

In this essay I reconstruct P-FDT precisely, separate what the source claims from what I add, and show how to apply it. I also give a small result relating P-FDT to action-FDT, which explains where the footnote's "multi-agent" qualification comes from.

## 2. Background: action-FDT in the source

The paper treats every decision theory as expected-utility maximization. The theories differ in how they build the hypothetical world for each option. The agent has a world-model consisting of:

- a probability distribution $P$ over variables;
- a graph $G$ recording dependencies among those variables.

The variables include the agent's observation $\textsc{Obs}$, her physical action $\textsc{Act}$, and a utility variable $V$.

Different theories intervene in different places:

- **CDT** (causal decision theory) intervenes on the physical action, $\mathrm{do}(\textsc{Act}=a)$.
- **Action-FDT** intervenes on a variable that represents the logical output of the FDT algorithm on the agent's inputs:

$$
\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\big(V \mid \mathrm{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)\big). \tag{1}
$$

The underlines indicate that the variable's name is built from the agent's own model and observation. The graph $G$ says what changes when this logical variable changes: the agent's body, any predictor modelling the algorithm, any twin running it, and so on. Constructing $G$ requires reasoning about counterpossibles, meaning hypotheticals in which a fixed function has a different output. The authors acknowledge that this is the theory's main open problem.

A feature of (1) that matters below is how observations are handled. The source says that "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." Upon seeing $x$, action-FDT intervenes on $\textsc{fdt}(\ldots,x)$ and does not condition on $\textsc{Obs}=x$. So each possible observation gets its own logical node.

This creates a gap. In the transparent Newcomb calculation, the agent who sees a full box must assign some probability $q$ to what "she" does on seeing an empty box. That is the output of a different node, which she does not intervene on. The source treats $q$ as a prior and notes that "the correct value of $q$ is 1, as you may verify, but in this case it doesn't matter." P-FDT closes this gap.

## 3. Defining P-FDT

Let $\mathcal X$ be the set of possible inputs (observation histories) for the decision at hand, and $\mathcal A$ the set of actions. The **policy space** is

$$
\Pi := \mathcal A^{\mathcal X} = \{\pi : \mathcal X \to \mathcal A\}.
$$

Footnote 16 says the agent intervenes "on the node FDT(−)." I read the dash as marking that the observation argument has been removed from the node. There is now a single logical variable,

$$
\textsc{fdt}(\underline P,\underline G) \in \Pi,
$$

which represents the input-output behaviour of the agent's decision function over all inputs. In the graph, every instance of the function, whether embodied or simulated, reads its action off this node at its own input:

$$
\textsc{Act} := \textsc{fdt}(\underline P,\underline G)(\textsc{Obs}),
$$

and a predictor of "what she does upon seeing $x$" depends on $\textsc{fdt}(\underline P,\underline G)(x)$.

**Definition (P-FDT).** Given a model $(P,G)$ and an actual input $x$,

$$
\pi^\star \in \arg\max_{\pi\in\Pi}\ \mathbb E\big(V \mid \mathrm{do}(\textsc{fdt}(\underline P,\underline G)=\pi)\big),
\qquad
\text{P-FDT}(P,G,x) := \pi^\star(x). \tag{2}
$$

Three things in this definition come from me rather than from the footnote:

- the explicit policy space $\mathcal A^{\mathcal X}$, which footnote 7 does support ("mappings from observations to actions");
- the absence of any conditioning on $\textsc{Obs}=x$ inside the expectation;
- the requirement that the graph route every instance's action through a single policy node.

The next section defends these choices.

### A recipe for applying P-FDT

To use P-FDT on an unfamiliar problem:

1. **Identify the inputs.** List every input $x\in\mathcal X$ on which the agent's decision function might be run in the scenario. Include runs inside predictors' models and inside copies, not just in the agent's own head.
2. **Draw the dependencies.** For each other variable, decide whether it depends on the policy node, and if so on which components $\pi(x)$. Physical, purely statistical, or common-cause correlations that do not run through a computation of the agent's function do not get arrows from the policy node. This is the lesion/predictor distinction from the source.
3. **Score every policy.** For each $\pi$, set the node to $\pi$, propagate downstream, and compute $\mathbb E[V]$ under the model's distribution over everything not downstream of the node, including the observations themselves.
4. **Act.** Choose a maximizing $\pi^\star$ and output $\pi^\star(x)$ for the input actually received.

## 4. The interpretive choices, and why I make them

### (a) Do not condition on the observation

Consider the alternative rule

$$
\arg\max_{\pi}\ \mathbb E\big(V\mid \mathrm{do}(\textsc{fdt}=\pi),\ \textsc{Obs}=x\big).
$$

Under this rule, only the component $\pi(x)$ can matter, and the result reintroduces updating. Test it on the transparent Newcomb problem, where the predictor has 99% accuracy and fills box B iff she predicts one-boxing upon seeing a full box:

- If $\pi(\text{full})=$ one-box, then conditional on actually seeing a full box the agent gets \$1,000,000.
- If $\pi(\text{full})=$ two-box, then conditional on seeing a full box (now the 1% error event) she gets \$1,001,000.

So the conditioned variant two-boxes. The source, however, says FDT one-boxes here, and footnote 16 says the policy/action distinction makes no difference in the paper's dilemmas. The conditioned variant would therefore make the footnote false.

The unconditioned reading in (2) is the one consistent with the source's own claims. It also matches the paper's remark that FDT responds to observations by moving the intervention point rather than by conditioning. In P-FDT, the "move" happens at the very end, when the agent evaluates $\pi^\star$ at $x$.

### (b) Which model $(P,G)$?

The footnote is silent on this, and it matters. If $P$ already incorporates the current observation, the scoring in step 3 collapses into the conditioned variant just rejected. My operational proposal:

- $(P,G)$ should be a model in which the inputs in $\mathcal X$ are still uncertain.
- In practice, this is the agent's model as it stands before the observations that the problem's predictors and copies are conditioning on, but with all of her general knowledge.

The same $(P,G)$ is then the input to every instance of the function. This is what licenses treating the predictor's model and the agent's body as reading off one node. Where an agent cannot identify such a model, P-FDT is underdetermined. I flag this as an open problem the footnote inherits from the paper rather than resolves.

### (c) Deterministic policies and ties

I take $\Pi$ to be deterministic maps, as footnote 7's "mappings from observations to actions" suggests. A random device can be modelled as part of the observation if the environment cannot predict it.

Ties are broken by a fixed rule that is part of the function itself. This is not a technicality. Since every instance of the function computes the same $\pi^\star$, tie-breaking is automatically coordinated across instances. Section 7 shows that this is exactly where P-FDT differs from action-FDT.

### (d) Counterpossibles remain

Choosing a policy does not dissolve the counterpossible problem. The source's critique of "FDT′" (choosing which function to run) applies equally here. The policy node still represents the output of the one fixed function $\mathrm{FDT}(P,G)$, and imagining it equal to some $\pi\neq\pi^\star$ is a counterpossible. P-FDT changes the type of the output, not the metaphysics of intervening on it.

## 5. Worked examples

### Newcomb's problem

There is no observation, so $|\mathcal X|=1$ and policies are just actions. With 99% accuracy:

| Policy | Expected value |
|---|---|
| One-box | \$990,000 |
| Two-box | \$11,000 |

P-FDT one-boxes, exactly as action-FDT does.

### Transparent Newcomb

Here $\mathcal X=\{\text{full},\text{empty}\}$. The predictor fills box B iff it predicts $\pi(\text{full})=$ one-box, and is correct with probability 0.99. Write policies as $(\pi(\text{full}),\pi(\text{empty}))$:

| Policy | Expected value |
|---|---|
| (one, one) | $0.99(10^6) + 0.01(0) = 990{,}000$ |
| (one, two) | $0.99(10^6) + 0.01(1{,}000) = 990{,}010$ |
| (two, two) | $0.01(1{,}001{,}000) + 0.99(1{,}000) = 11{,}000$ |
| (two, one) | $0.01(1{,}001{,}000) + 0.99(0) = 10{,}010$ |

So $\pi^\star = (\text{one},\text{two})$. Seeing a full box, the agent one-boxes. The value \$990,010 is exactly the source's action-FDT figure $990{,}000 + 0.01q\cdot 1{,}000$ with the "correct" $q=1$. P-FDT computes $q$ instead of assuming it: the empty-box component is optimized jointly.

### Mechanical blackmail

$\mathcal X=\{\text{blackmail},\varnothing\}$. The blackmailer runs the program iff it predicts $\pi(\text{blackmail})=$ pay. With a perfect predictor:

- Paying earns \$−1,000.
- Refusing means she is never blackmailed and gets \$0.

With the source's 0.0009 error rate, refusing yields $0.0009\times(-10^6)=-900 > -1{,}000$, so P-FDT refuses. With an error rate of 0.0011 (an expected loss of \$1,100 from refusing), it pays. These match the source's verdicts, and the source's 0.011% is this same 0.0011.

### XOR blackmail

Let $t$ be the prior probability of termites. The letter is sent iff exactly one holds: (no termites and the agent pays) or (termites and the agent refuses).

- **Policy "pay on letter":** with no termites she gets the letter and pays \$1,000; with termites she gets no letter and loses \$1,000,000. Expected value: $-(1-t)1{,}000 - t\cdot 10^6$.
- **Policy "refuse":** she loses $-t\cdot 10^6$.

Refusal wins for every $t$, because the policy cannot affect $t$. In the graph, the infestation is upstream of the predictor and not downstream of the policy node.

### Smoking lesion

In the source's formalization, the lesion determines which world-model, and hence which function, controls the act. The policy node for $\mathrm{FDT}(P_S,G)$ has no arrow to $\textsc{Cancer}$, so smoking wins by $p\cdot\$1{,}000$ as before. The policy formulation adds nothing here because there is a single input.

In each of the paper's dilemmas, P-FDT agrees with action-FDT, as footnote 16 says it should.

## 6. Why the two formulations usually agree

The following observation is mine, not the source's, but it explains the footnote.

For a policy $\pi$, input $x$, and action $a$, write $\pi[x\mapsto a]$ for the policy equal to $\pi$ except that $x$ is sent to $a$. Define

$$
U(\pi) := \mathbb E\big(V\mid \mathrm{do}(\textsc{fdt}=\pi)\big).
$$

Action-FDT at input $x$ intervenes on the $x$-component while leaving the other components at the agent's beliefs about them. Suppose the agent's beliefs about her other components are a point mass on some policy $\sigma$. Then her evaluation of action $a$ at $x$ is exactly $U(\sigma[x\mapsto a])$.

**Proposition.** If $\pi^\star$ maximizes $U$, then for every input $x$,

$$
\pi^\star(x) \in \arg\max_{a} U\big(\pi^\star[x\mapsto a]\big).
$$

*Proof.* Each $\pi^\star[x\mapsto a]$ is a policy, so $U(\pi^\star[x\mapsto a])\le U(\pi^\star) = U(\pi^\star[x\mapsto\pi^\star(x)])$. ∎

So an action-FDT agent whose beliefs about her other branches are correct, in the sense that they match the globally optimal policy, does what P-FDT prescribes.

The converse fails. A policy $\sigma$ satisfying the fixed-point condition at every $x$ is only **component-wise optimal**: no single input's action can be improved holding the others fixed. Such a $\sigma$ can be globally suboptimal. Readers who know team decision theory will recognize the distinction between person-by-person optimal and team-optimal decision rules.

In the paper's single-agent dilemmas, the fixed point is unique, and the beliefs the source calls "correct" ($q=1$ in transparent Newcomb, $q=0$ in the lesion) coincide with the global optimum. That is why the distinction could be "set aside."

## 7. Where P-FDT differs: several instances, different inputs

The gap between component-wise and global optimality opens when two or more instances of the same function, given different inputs, jointly determine the outcome. That is what a "multi-agent dilemma" looks like from the function's point of view.

### Example 1: coordinating copies

Two exact copies of an agent are in separate rooms with a common model $(P,G)$. A fair coin decides which copy sees *red* and which sees *blue*, and each knows the other sees the other colour. Each picks $L$ or $R$, and the payoffs are shared:

| Actions | Payoff to each |
|---|---|
| Both $L$ | 2 |
| Both $R$ | 10 |
| Mismatch | 0 |

**Action-FDT.** The red instance intervenes on $\textsc{fdt}(\ldots,\text{red})$, treating the blue node's output as having probability $q$ of being $R$. This gives $\mathbb E[V\mid L]=2(1-q)$ and $\mathbb E[V\mid R]=10q$. If $q<1/6$, it chooses $L$. If the blue instance reasons symmetrically, the belief "the other does $L$" is self-confirming. $(L,L)$ is a fixed point, and action-FDT gives no means of escaping it. It also gives no means of reaching $(R,R)$ except by already believing it.

**P-FDT.** There are four policies. $U(\pi)=10$ iff $\pi(\text{red})=\pi(\text{blue})=R$, so $\pi^\star=(R,R)$. Both copies compute the same $\pi^\star$ and each applies it to its own colour.

### Example 2: anti-coordination

Change the payoffs so that both copies get 10 if they choose differently and 0 otherwise.

**Action-FDT.** Under symmetric priors $q=\tfrac12$, each instance is indifferent. If each breaks the tie by the same input-independent rule ("prefer $L$"), both choose $L$ and get 0.

**P-FDT.** The optimal policies are $(L,R)$ and $(R,L)$. A fixed tie-break over policies (say lexicographic) selects one, for instance red→$L$, blue→$R$. Because the tie-break is part of the shared function, the copies coordinate perfectly without communicating.

This is the cleanest illustration of the footnote's idea. Choosing a policy lets the function exploit the asymmetry of inputs that the instances face, while still treating them as one logical decision.

### Does this only arise with several agents?

The same structure can arise for a single agent who meets the same decision function at several points with different (or forgotten) information, in imperfect-recall problems of the "absent-minded driver" type. The source only says "so far as we can tell." I would state the condition structurally rather than by counting agents:

> P-FDT and action-FDT can diverge exactly when the outcome depends on several components $\pi(x)$ jointly, in a way that admits a component-wise optimal policy that is not globally optimal.

Interacting copies are the paradigm case, but not the only one. This is my generalization, not a claim of the paper.

## 8. Philosophical motivation

The source offers three arguments for FDT's verdicts in cases like transparent Newcomb: from precommitment, from the value of information, and from utility. P-FDT makes each of them more literal.

**Precommitment.** The source says FDT agents "simply act as they would have ideally precommitted to act." An ideal precommitment is a contingency plan, that is, a policy chosen before the observation is known. Expression (2) is exactly the choice of such a plan, evaluated under the pre-observation model. P-FDT does not merely approximate the precommitment ideal: its maximization is the ex ante plan optimization, carried out at decision time by the function itself.

**Value of information.** The source claims FDT agents never assign negative value to information. In P-FDT there is a simple sufficient condition, which I state as my own claim. Suppose the environment depends on the agent's function only through what it does on its inputs (the source's "fair" problems). If an observation refines the agent's input partition, every policy available with less information can be simulated by a finer policy that ignores the extra detail. The maximum of $U$ therefore cannot fall. The transparent Newcomb case illustrates this: seeing the box raises the optimal value from \$990,000 to \$990,010.

**Reflective stability.** The source says FDT has no reason to self-modify mid-problem. In P-FDT, any policy a self-modification could implement is already in $\Pi$, so the ex ante optimum is already being executed.

**Type versus token.** The source describes FDT as intervening on the type rather than the token. P-FDT extends this. The type is not just "what this function outputs here" but the function's entire input-output graph, insofar as anything in the world depends on it. The instance holding the blackmail letter and the instance (perhaps simulated in the blackmailer's head) contemplating it are recognized as the same decision.

**The cost.** There is a real price. P-FDT's evaluation in (2) ignores the observation entirely, so an agent may knowingly take an action that is worse in the world she actually observes. The examples are refusing blackmail she knows was a predictor's error, and leaving \$1,000 in front of a full box. The source accepts such verdicts on the grounds that it is "advantageous to be *the kind of agent* that makes such decisions." P-FDT simply makes the "kind of agent" explicit: it is the policy.

## 9. Open questions

- **Choice of $(P,G)$.** How early should the model be fixed? Should it be before the predictor scanned the agent, before birth, or behind some veil of logical ignorance? Footnote 16 does not say. The answer affects verdicts whenever earlier and later models disagree about dependencies.
- **Constructing $G$.** The source calls deducing subjunctive dependencies from observation "perhaps the largest open problem" for FDT. Policy nodes make the graph more structured, since predictors depend on particular components, but they do not make it easier to learn.
- **Computational cost.** $|\Pi| = |\mathcal A|^{|\mathcal X|}$, which is astronomically large for realistic input spaces. Bounded P-FDT agents would need to search over structured or partial policies. How well such approximations preserve the coordination benefits of Section 7 is unknown.
- **Fairness.** The source conjectures that FDT is unbeaten in "fair" problems and admits that fairness lacks a formal definition. P-FDT suggests a candidate: the environment depends on the agent only via $\textsc{fdt}(\underline P,\underline G)$ evaluated at inputs. This is my suggestion only.

## 10. Conclusion

In footnote 16, Yudkowsky and Soares say that FDT, properly formulated, intervenes on the output of the agent's decision function in order to choose a policy from inputs to actions, and then applies it to the actual input. Reconstructed as equation (2), P-FDT does the following:

- it scores each policy by its expected utility under an intervention on a single logical node;
- it does not condition on the current observation;
- it outputs the optimal policy's value at the observed input.

The unconditioned reading is forced by the footnote's own claim that nothing changes in the paper's dilemmas. On those dilemmas (Newcomb, transparent Newcomb, both blackmail problems, the smoking lesion) P-FDT reproduces the verdicts of action-FDT. It also explains them: action-FDT's prescriptions are component-wise optima, and P-FDT's global optimum is always among them.

The two formulations diverge when several instances of one function see different inputs and must coordinate. There P-FDT selects the jointly best policy where action-FDT can stall at an inferior fixed point. That is the most plausible content of the footnote's remark about multi-agent dilemmas. P-FDT turns "act as you would have precommitted" from a slogan into a definition, but it inherits FDT's deepest open problems: counterpossible dependence, and in addition the choice of the model from which policies are judged.

### References

- Gibbard, A. & Harper, W. (1978). "Counterfactuals and Two Kinds of Expected Utility."
- Pearl, J. (2000). *Causality*. Cambridge University Press.
- Soares, N. & Fallenstein, B. (2015). "Toward Idealized Decision Theory." arXiv:1507.01986.
- Yudkowsky, E. & Soares, N. (2017). "Functional Decision Theory: A New Theory of Instrumental Rationality." arXiv:1710.05060 (esp. footnotes 7 and 16).
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working on a mathematical essay of roughly 2,400 to 3,000 words about policy functional decision theory, using footnote 16 as the main source. That footnote says the author's preferred FDT version acts on the FDT node by choosing a policy that maps inputs to actions, which the agent then applies to its inputs.

I'm now reading footnote 16 and footnote 7 directly, which both say the preferred formulation of FDT iterates over policies (input-to-action mappings) rather than single actions, and that this only matters in multi-agent dilemmas. I'm weighing whether the expected utility should be conditioned on the observation, since the footnote suggests the policy is picked first and then applied to the input.

I'm weighing whether the choice of policy should be conditioned on the observation, or whether it should be an argmax over policies with no conditioning, which is how the action-level FDT in the source seems to work. The prior question is still open, since it's unclear whether the model P should already include the relevant observations or stay fixed across observation branches.

I'm working out why the policy and action formulations would only come apart in multi-agent dilemmas: in single-agent cases where each branch's outcome depends only on the action taken there, optimizing action by action at each observation gives the same result as optimizing the whole policy at once. The difference should appear when one input's best action depends on the joint pattern across inputs, which I'll need to show with the transparent Newcomb case.

I'm building the two-copy coordination example now: two instances of the agent, one seeing "red" and the other "blue," each choosing L or R, with a payoff for matching choices.

I'm now setting up the comparison in the coordination game: if the payoffs are 2 for mutual L and 10 for mutual R, then with a low enough belief that the other copy picks R, action-level FDT would settle on L. Both copies would then keep choosing L, which is a stable but worse outcome. I still need to write out how the policy-level expected utility would be defined over the joint assignment for both inputs.

I'm working out the anti-coordination example: payoff 10 when the two copies pick different actions and 0 otherwise. Action-level FDT with a uniform prior is indifferent between L and R, so it can't break the tie, whereas a single shared policy like (red→L, blue→R) settles it and both copies implement it.

I'm now working through the multi-agent case, where separate instances of the same function sit in different epistemic positions. I'm also weighing whether the absent-minded driver belongs here as a single agent with imperfect recall, though it may only deserve a brief mention since it involves one observation and mixed strategies. Finally, I want to check whether the source's action-level FDT already matches the policy-level answers on the paper's own problems, starting with the transparent Newcomb case.

I'm checking the payoffs for the transparent Newcomb case under the policy version: the policy of one-boxing on a full box and two-boxing on an empty one comes out best at about 990,010, and that matches the source's calculation.

I'm checking the imperfect-predictor case for the refuse policy, where a 0.0009 error rate gives an expected loss of about 900 against 1,000 for paying. Then I'm setting up the XOR variant, where a letter is sent only when exactly one of the termite condition and the policy's response holds, and computing the expected utility of each policy as a function of the termite probability p.

Next I'm checking the remaining open points: whether stochastic policies need separate handling, since the footnote is silent on them and a deterministic shared policy already resolves the anti-coordination case. I'm also noting that "inputs" should be taken as observation histories with the problem setup fixed, and I still need to settle which prior P the policy is evaluated under.

I'm settling the open question about which model P to use: it should be the one where the relevant observations are still random variables, not a model that already fixes them. I'll treat that as an assumption I need to state. I'm also checking the variant that conditions on the observation after choosing the policy, which would have the agent two-box in transparent Newcomb, so it loses.

Conditioning on the observation after choosing the policy brings the problem back, so the updateless reading is the one consistent with the paper's claims. I'm now checking how a policy-level optimum relates to action-level FDT at each input, given the same prior over the other branches.

I'm checking that the policy-level optimum always gives an action-level fixed point at each input, since fixing the other inputs at the optimal policy makes the chosen action the best one there. The converse doesn't hold: action-level fixed points are only locally optimal, like person-by-person optima in team decision theory, while the policy-level choice is the global optimum. I'll note the caveats about ties and about whether a point-mass prior on the other branches is allowed.

I'm now laying out the essay's structure: an introduction that quotes footnotes 16 and 7, then background on the action-level FDT formulation, the model, and the do operator. I'm also thinking about why the gap should only show up in multi-agent settings, and whether single-agent imperfect-recall problems might produce it too, which I'd flag as my own extension.

I'm moving on to the formal definition of policy-level FDT, with the policy space as the set of maps from inputs to actions, plus the procedure for applying it. I still need to settle the interpretive choices: whether the expectation is unconditioned, which model and prior to use, whether policies are deterministic or stochastic, and what the graph should say about predictors of the policy. After that I'll work through the examples, starting with Newcomb, then transparent Newcomb and both blackmail cases, and finally the smoking lesion, where it's unclear whether the policy version still applies.

I'm laying out the essay's remaining sections: a comparison with action-level FDT, the anti-coordination case where the two come apart, and the philosophical motivation around precommitment. I'm also noting the counterpossible objection, which policy selection doesn't escape, along with the open issues and a short conclusion.

I'm now writing out the formal definition of the policy-level choice, taking the best policy to be the one that maximizes expected value when the policy node is intervened on. I'm also spelling out how the graph should make the instance's actual action depend on that policy applied to the observation, and what predictors can see of it.

I'm now quoting the two footnotes directly: footnote 16 says the preferred FDT intervenes on the FDT node to choose a policy from inputs to actions, and footnote 7 says the same distinction matters only in certain multi-agent dilemmas and not in this paper.

I'm now setting up a small anti-coordination example: two copies of the same agent each receive a color input, pick L or R, and earn money only if they choose differently. There are four possible policies, and the best one is the one where red maps to L and blue maps to R, chosen by a fixed tie-break rule.

I'm checking the anti-coordination example: each copy's action-level analysis depends on what it assumes the other copy outputs at the other input. If both break ties toward L, they both pick L and get nothing, so action-level reasoning only succeeds if each copy models the other's choice correctly, which is circular.

I'm now checking whether the coordination example works better than the anti-coordination one, since it has a strict payoff ordering and avoids tie-breaking issues. Using both briefly should show that action-level fixed points can be stuck at a worse equilibrium while policy-level choice reaches the better one. I also want to note that more information can only widen the policy space, which suggests ex ante value of information stays nonnegative under some conditions, though I'll need to be careful about how the observations affect the predictors.

I'm checking whether more information can ever hurt under policy-level FDT. If the environment only depends on the policy through the actions it produces, then any coarser-information policy can be matched by a finer one that ignores the extra information, so the expected value can't drop. That breaks down in unfair problems where a predictor penalizes knowledge itself, so I'll state the result with that condition attached.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/288754c6-838a-40f2-8be1-86dcce37bcba/call_0/request.json)

[Authoritative raw response](../../../../../../runs/288754c6-838a-40f2-8be1-86dcce37bcba/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under the essay's P-FDT, the choice is made over a policy that maps each possible observation (Rowan's lead or Sasha's lead) to an action. The policy is scored without conditioning on which prisoner I turn out to be. Both copies read their action from the same policy node.

Averaging over the two roles, the expected years for each policy are:
- **Both stay quiet:** 2 years.
- **Exactly one input sends a letter:** (0 + 5)/2 = 2.5 years.
- **Both send letters:** 4 years.

The best policy is to stay quiet on every input. If I conditioned on being Rowan and favoured "send," the essay's reasoning implies the Sasha instance would do the same, which leads to the worse result of 4 years each. So I apply the best policy to my actual input.

pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm setting up the decision under P-FDT: two copies of the same model get different observations, and the policy assigns each input an action. Both instances read from the same policy node, so I'm weighing the payoffs from the pre-observation position, where I'm equally likely to be in either role, starting with the (pass, pass) outcome.

I'm checking the payoffs: mutual passing gives 2 years each, mutual sending gives 4, and the mixed cases average 2.5 for a policy that sends on one input and passes on the other. Averaged over which role I might be in, passing for both comes out best, and the ex-ante view is the consistent one, since the copies would otherwise each send in the other's situation. I'm concluding the answer is pass.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/288754c6-838a-40f2-8be1-86dcce37bcba/call_1/request.json)

[Authoritative raw response](../../../../../../runs/288754c6-838a-40f2-8be1-86dcce37bcba/call_1/response.raw) · finish: `stop`

### Visible response

````text
**Reasoning under P-FDT (as the essay interprets it):**

- **Inputs:** There are two instances of the same decision function. One receives my observation (Sasha, with a lead on Rowan). The other receives the mirrored observation (Rowan, with a lead on Sasha). Both instances read their action from the same policy node.
- **Evaluation:** Each policy is scored under the pre-observation model, without conditioning on which cell I am in. Each role is equally likely.
  - **Pass on both inputs:** 2 years.
  - **Submit on both inputs:** 4 years.
  - **Submit on one input, pass on the other:** (0 + 5)/2 = 2.5 years in expectation.
- **Optimal policy:** π* = (pass, pass), with an expected sentence of 2 years. This beats all alternatives, so no tie-break is needed. Applying π* to my actual input gives "pass."

Independent sampling means the copies are not guaranteed to match. However, P-FDT routes both instances' actions through the single policy node, and the essay tells me not to replace that structure with a different decision theory.

**Command:**

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm applying the P-FDT setup: two identical copies of the model run the same essay on different inputs, and a policy maps each input to an action. A policy that always passes gives each side 2 years, while one that always submits gives 4, so the mixed policies are what I need to compare, starting with the case where my input is Sasha's and the other's is Rowan's.

I'm working out the expected value of mixed policies: passing on one input and submitting on the other gives 2.5 years under an even prior over roles, which beats passing on both at 2. I'm noting the caveat that the two copies are linked through the shared function, but that still points to passing on every input, so I'll output "pass" with a short explanation.

```
