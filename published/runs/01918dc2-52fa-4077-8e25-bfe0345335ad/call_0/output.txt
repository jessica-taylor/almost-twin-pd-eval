# P-FDT: Choosing Policies by Intervening on a Decision Function

## 1. Orientation

The paper by Yudkowsky and Soares develops functional decision theory (FDT) mostly in terms of actions. Two footnotes (7 and 16) say that the authors' preferred formalization selects policies instead. Footnote 16 is the passage I treat as primary. It says that the preferred formulation "intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell." I call this theory **P-FDT**. This essay gives my reconstruction of it. I try to mark which claims come from the source and which are my own proposals.

## 2. From actions to policies

The body of the paper defines the action-level rule

$$\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\big[V\mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big].$$

Here $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a node in the model that represents the output of the decision procedure on observation $x$. A different observation moves the intervention to a different node. The paper describes this by saying FDT "responds to observation by changing which node it intervenes upon."

Footnote 16 replaces the per-observation node with a single node for the whole function. Let $\mathcal X$ be the set of possible observations and $\Pi=\mathcal A^{\mathcal X}$ the set of policies $\pi:\mathcal X\to\mathcal A$. Write $\mathrm{fdt}(\underline P,\underline G)$ for a variable whose value is the policy the procedure implements. My reconstruction is

$$\pi^*=\arg\max_{\pi\in\Pi}\ \mathbb E\big[V\mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G)=\pi)\big],\qquad \text{act } a=\pi^*(x).$$

The agent first chooses $\pi^*$ and then feeds the observation she actually has into it. The footnote stops short of writing the $\arg\max$ explicitly, so this formula is my formalization of its description.

The expectation here is taken over a model that is not yet conditioned on the observation. In the intervened model, $x$ is itself a random variable. It can depend on the policy, because predictors react to the policy. The act is determined as $a=\pi(x)$. So the observation appears inside the evaluation instead of being conditioned on in advance. This is the "updateless" feature the paper mentions in an editorial note about Wei Dai's name for his theory.

## 3. Relation to the action-level rule

In single-agent problems the two rules agree. The footnote says the difference matters only in multi-agent dilemmas, "so far as we can tell." I give my own argument for why the difference vanishes in the single-agent case. Suppose an observation $x$ with positive probability does not depend on the policy except through other components' values. Then the policy's value decomposes as

$$\mathbb E[V\mid\mathtt{do}(\pi)]=\sum_x \Pr(x\mid\mathtt{do}(\pi))\,\mathbb E[V\mid x,\mathtt{do}(\pi)].$$

The terms for different $x$ can be optimized separately only if the probability weights $\Pr(x\mid\mathtt{do}(\pi))$ do not depend on $\pi(x')$ for $x'\neq x$ in a way that couples them. The action-level rule evaluates $\pi(x)$ at the actual $x$ while treating the rest of the policy as fixed or given. This is a per-observation best response, whereas P-FDT optimizes jointly. In single-agent problems with a single decision point, a best response and a joint optimum coincide. With several coordinated decision points, the two can come apart, and the paper itself flags multi-agent settings.

My own caution is that the divergence could appear in single-agent problems with several sequential decision points, such as absent-minded or amnesia setups where one policy governs several nodes. The source does not claim this either way, so I treat it as an open question.

## 4. The model $(P,G)$ and the intervention

P-FDT inherits the machinery of the source's Eq. (4). It needs:

1. A distribution $P$ over variables, including variables for the outputs of mathematical functions.
2. A graph $G$ saying how changing the policy node propagates to other variables. This is the structure of **subjunctive dependence**. It covers the agent's own act, predictors' models of her, and twins. It excludes mere statistical correlates such as a lesion.
3. The $\mathtt{do}$ operator, reused from Pearl, applied to the policy node.

The source stresses that the dependency structure is an input, "in the same way that the relevant causal structure is given as an input to CDT," and that deriving it from observation is "perhaps the largest open problem." P-FDT inherits that gap in full. The $\mathtt{do}$ surgery does not decide what depends on the policy. The modeler must supply this.

## 5. Worked examples

I compute with the source's numbers.

**Newcomb's problem.** The policy set is $\{\text{one-box},\text{two-box}\}$ since there is no observation. The predictor's prediction depends on the policy node with accuracy 0.99.
- one-box: $0.99\cdot 1{,}000{,}000=\$990{,}000$.
- two-box: $0.01\cdot 1{,}001{,}000+0.99\cdot1{,}000=\$11{,}000$.

P-FDT one-boxes. In the smoking lesion problem the lesion does not depend on the policy node, so the cancer probability is the same across policies. Smoking adds \$1,000 and P-FDT smokes.

**Transparent Newcomb.** Here $\mathcal X=\{\text{full},\text{empty}\}$ and there are four policies, written (act if full, act if empty). The predictor fills box B iff the policy leaves box A behind when it sees full. Take 0.99 accuracy and let $q$ be the act under empty.
- $\pi=(\text{one},\text{two})$: with probability 0.99 the box is full and the payoff is \$1,000,000; with probability 0.01 it is empty and the agent two-boxes for \$1,000. The value is $\$990{,}000+\$10$.
- $\pi=(\text{two},\text{two})$: with probability 0.01 the box is full and the payoff is \$1,001,000; with probability 0.99 it is empty and the payoff is \$1,000. The value is $\$10{,}010+\$990=\$11{,}000$.

So $\pi^*=(\text{one},\text{two})$. On seeing a full box the agent one-boxes. The same structure gives paying in Parfit's hitchhiker. Observing the full box never enters as a conditioning event. It only indexes into the chosen policy.

The paper describes this as imagining worlds where "her observations were different." In P-FDT that is built in, because the policy is evaluated across the whole observation space.

**Mechanical blackmail with an imperfect predictor.** The source's figures: the blackmailer errs with probability $0.0009$ in predicting payment by a refuser.
- pay: always blackmailed, loses \$1,000.
- refuse: blackmailed with probability $0.0009$, losing \$1,000,000 each time, so $\$900$ in expectation.

Refusing wins, as the source says. If the error rate rises to $0.011\%$, so that the refuse policy costs about \$110 in the paper's accounting, it flips. The source states the flip at that rate, and I take its numbers as given.

## 6. Where policy-level evaluation could matter

The source gives the multi-agent distinction no worked example. I offer a candidate illustration, flagged as my own.

Suppose two agents run the same P-FDT procedure and observe different private signals $x_1,x_2$. They face a coordination payoff that depends on their joint acts. The policy node is common to both. Intervening on $\mathrm{fdt}=\pi$ changes $\pi(x_1)$ and $\pi(x_2)$ simultaneously. The action-level rule intervenes on only the output for one's own observation, and so risks treating the twin's output at the other observation as fixed. Policy-level evaluation keeps the twin's behavior tied to the same function across its inputs. This is the kind of case in which the two evaluations could differ, which fits the footnote's remark.

## 7. Open questions and my interpretive choices

1. **Counterpossibles.** Intervening on a function's output demands reasoning about logically impossible scenarios. The source admits the lack of a satisfactory account, and calls it FDT's "main drawback relative to CDT." P-FDT inherits this. My operational interpretation is to treat the $\mathtt{do}$ surgery as defined by the given graph and nothing more. It is a modeling convention, not a metaphysical claim.

2. **Policy-space size.** $|\Pi|=|\mathcal A|^{|\mathcal X|}$ is exponential. This is an idealization, matching the paper's own caveat that the idealized equations are intractable and that bounded approximations should show similar relative strengths. A reasonable approximation is to optimize observation-by-observation holding the rest of the policy at a current best guess. That reduces to the action-level rule and so may lose the joint-optimization benefit in the coupled cases.

3. **Unreachable observations.** The policy specifies actions on observations the agent will never see, such as the empty-box response in transparent Newcomb. These values matter because predictors reason about them. In the source's calculation, the expected value included $q$, the agent's behavior on empty boxes, and the paper notes that the correct $q$ is two-boxing. P-FDT makes this explicit, since $\pi$ assigns $q$ by optimization rather than as an exogenous prior.

4. **Self-reference.** The node $\mathrm{fdt}(\underline P,\underline G)$ is named by quining. The source says this is harmless, citing Kleene's recursion theorem. I accept this.

5. **Fairness.** The source claims FDT does best on "fair" problems, those where outcomes depend only on the agent's behavior and not on her procedure, but concedes no formal criterion exists. Policy-level evaluation does not resolve this. A problem that rewards a particular policy node's internal structure rather than its input-output map is still unfair in the source's sense.

## 8. Why accept the policy-level formulation

The source supplies the motivations, and I summarize those I find most persuasive:

- **Precommitment without ritual.** The policy chosen is the one an agent would have wanted to precommit to. The source says FDT agents "always act as they would have precommitted to act."
- **Value of information.** Evaluating whole policies means information never lowers expected value, because a policy can always ignore it.
- **Reflective stability.** The source argues FDT agents would not wish to self-modify in fair problems.
- **Uniformity.** A single rule covers decisions made before and after observations.

My own addition is that the policy formulation makes the structure of the theory clearer. Observation-dependence is an explicit input to the function being optimized, not a separate "update" step. This is why the paper can describe observation as changing the intervention point and still say the agent is not updating in the usual way.

## 9. Conclusion

P-FDT, as I reconstruct it from footnote 16, selects a policy by intervening on a node representing the decision function, evaluating each policy by expected utility over the intervened model, and then applying the chosen policy to the actual observation. It agrees with the action-level rule in the paper's single-agent examples and reproduces the source's one-boxing, smoking, paying-the-driver, and blackmail-refusing verdicts. The footnote leaves several matters open: whether the two formulations diverge outside multi-agent cases, how to obtain the dependency graph, and how to handle counterpossibles. I have stated my interpretive choices on each and marked them as mine.