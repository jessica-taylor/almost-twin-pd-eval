# P-FDT: Choosing Policies by Intervening on a Decision Function

## 1. Orientation

The source paper (Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality") mostly presents an action-based version of functional decision theory. Two footnotes point to a different "preferred formalization" in which the agent chooses a *policy*. Footnote 16 reads:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

Footnote 7 says something similar. I call the policy-selecting theory **P-FDT**. This essay has three parts. Section 2 gives the paper's action-indexed procedure as background. Sections 3 and 4 give my reading of P-FDT as a mathematical object. Sections 5 to 7 apply it and discuss what the footnote leaves open. I label each claim as *source* or *my proposal*.

## 2. Background: the action-indexed procedure (source)

The paper treats expected-utility theories as differing only in how they build a "hypothetical" for each option. Evidential decision theory (EDT) conditions on the action. Causal decision theory (CDT) applies Pearl's $\mathtt{do}$ to a physical action node $\textsc{Act}$. The paper's FDT instead applies $\mathtt{do}$ to a node $\textsc{fdt}(\underline{P},\underline{G},\underline{x})$, the output of the decision function on inputs (world-model, observation $x$):

$$\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\big[V\mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)\big].$$

Here $G$ is a graph encoding *subjunctive dependence*: which quantities would change if that function had a different output. Two features of this procedure matter below. First, observation does not enter by conditioning. It only selects *which* node is intervened on. Second, the graph $G$ must be supplied as input, because the paper admits that no account exists of how to learn subjunctive dependence structure. Footnote 9 notes that no formal $\mathtt{true}$ operator for logical counterfactuals exists.

## 3. P-FDT: definition (my formalization of footnote 16)

The footnote says the agent intervenes on $\textsc{fdt}(-)$ itself to choose a policy, and then applies her input to the chosen policy. I formalize this as follows.

- $\mathcal X$ is the set of possible observations, or inputs, and $\mathcal A$ the set of actions.
- A **policy** is a function $\pi:\mathcal X\to\mathcal A$, and $\Pi=\mathcal A^{\mathcal X}$ is the set of policies. Randomized policies map into distributions over $\mathcal A$ and are an extension.
- $\textsc{fdt}(\underline P,\underline G)$ is a variable whose value is a policy. It names the whole input-output behavior of the decision procedure, given the model.

P-FDT is the following two-step rule:

$$\pi^*\in\arg\max_{\pi\in\Pi}\ \mathbb E\big[V\mid \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G)=\pi\big)\big],\qquad \text{act } a=\pi^*(x_{\text{actual}}).$$

The score of $\pi$ is a sum over the observations that might arise, weighted according to how the *intervened* model generates them:

$$\mathcal{EU}(\pi)=\sum_{o}P\big(o\mid \mathtt{do}(\textsc{fdt}=\pi)\big)\,\mathcal U(o).$$

Everything else, including what the agent actually observes, is a downstream variable. Observations are not conditioned on first. Seeing a letter, a full box, or a rescuer is itself an event whose probability depends on $\pi$ whenever some predictor or copy of the agent subjunctively depends on $\pi$.

**Relation to the action-indexed version.** In the action-indexed version, the agent holding observation $x$ intervenes on the variable $\textsc{fdt}(\underline P,\underline G,\underline x)$, one variable per possible input. Footnote 16 says the difference "only matters in multi-agent dilemmas so far as we can tell." My reading of why they usually agree has two parts.

1. The policy value decomposes by observation. Suppose the intervention's effects factor through the per-input outputs. Then $\mathcal{EU}(\pi)=\sum_x P(x\mid\mathtt{do}(\pi))\cdot\mathbb E[V\mid x,\mathtt{do}(\pi)]$.
2. In a single-agent problem where the agent's *policy* is evaluated by the same procedure that evaluates the action, each input is reached with probability that depends on $\pi$ only through earlier outputs. The optimal policy is then approximately consistent with the action-indexed optimum at the actually realized input.

My proposal is to treat this as a conjecture to check case by case, not a theorem. The footnote itself only says "so far as we can tell."

Why would the two diverge with several agents? Suppose another agent's behavior depends on the agent's output at an input the agent never sees. The per-input intervention gives the agent no way to choose coordinated outputs across inputs, and the policy-level intervention does. The footnote does not give an example, so any specific example below is my reconstruction.

## 4. How dependencies and counterfactuals enter

**Source claims.**

- Counterfactuals are made by surgery on a model. FDT intervenes on a *logical* variable, the output of a fixed function, while CDT intervenes on a physical act.
- The hypothetical keeps all and only the things that subjunctively depend on that output: predictors, twins, agent-modeling processes, and the agent's own actions at the relevant inputs.
- Statistical correlations without subjunctive dependence, such as the lesion–smoking link, are broken, as in CDT.
- Hypotheticals "are not themselves beliefs." They are instruments, like scratch paper.

**Consequence for P-FDT.** The graph $G$ must give each node's dependence on the *policy* variable, not on one output. The agent's action node is $\textsc{Act}=\pi(\textsc{Obs})$. A predictor that simulates the agent on input $x'$ depends on $\pi(x')$. Choosing $\pi$ therefore fixes the agent's behavior everywhere at once, including on inputs she does not receive in the actual world. This is why P-FDT reasons without a precommitment ritual: the "commitment" is the policy, and the policy is selected by the rule the agent is running.

## 5. Worked examples

All numbers follow the paper's conventions.

### 5.1 Newcomb's problem (no observation)

$\mathcal X=\{\emptyset\}$, so $\Pi\cong\mathcal A$ and P-FDT reduces to the action rule. Predictor accuracy is 0.99.

- $\pi=$ one-box: $P(\text{full})=0.99$, so $\mathcal{EU}=0.99\cdot 10^6=\$990{,}000$.
- $\pi=$ two-box: $P(\text{full})=0.01$, so $\mathcal{EU}=0.01\cdot1{,}001{,}000+0.99\cdot 1{,}000=\$11{,}000$.

One-boxing wins. (The paper reports exactly these two numbers for its Fiona.)

### 5.2 Transparent Newcomb (observation matters)

$\mathcal X=\{\textit{full},\textit{empty}\}$ and there are four policies. The predictor fills box B iff $\pi(\textit{full})=$ one-box, accurately with probability 0.99. Write $q=\pi(\textit{empty})$ when it is two-box.

| $\pi(\textit{full})$ | $\pi(\textit{empty})$ | what happens | $\mathcal{EU}$ |
|---|---|---|---|
| one-box | one-box | 0.99: full, one-box, \$1M; 0.01: empty, one-box, \$0 | \$990,000 |
| one-box | two-box | 0.99: \$1M; 0.01: empty, two-box, \$1,000 | \$990,010 |
| two-box | either | 0.01: full and two-box, \$1,001,000; 0.99: empty | \$10,010 + 0.99·(\$1,000 if $\pi(\textit{empty})$ = two-box) = \$11,000 |

The best policy is $(\text{one-box},\text{two-box})$. Applying it to the observation *full* gives one-boxing. This matches the paper: when envisioning two-boxing on a full box, the agent envisions with high probability a world where she saw an empty box. Parfit's hitchhiker has the same structure, so the policy "pay if in the city" scores about $0.99\cdot\$1{,}000{,}000-\$1{,}000$ against about $\$10{,}000$-scale losses for refusing.

### 5.3 Blackmail with a fallible predictor

The paper's mechanical blackmail example gives these figures. If the blackmailer errs with probability 0.0009 in favor of sending, then refuse-policy loses $0.0009\times\$1{,}000{,}000=\$900$ in expectation, and pay-policy loses \$1,000. Refusing wins. At error 0.00011 the refusing loss is \$110, which is under \$1,000, so refusing should still win; the paper's statement that Fiona then pays at 0.011% is hard to reconcile with its own numbers (the \$110 figure and the 0.0009 case suggest the intended threshold is 0.1%). I follow the arithmetic and flag this as an apparent slip in the source.

### 5.4 Smoking lesion (no subjunctive dependence)

The policy variable is a parent of the action, not of cancer. Every policy has the same cancer probability, so P-FDT picks the policy that smokes (+\$1,000). This is the same verdict as CDT.

### 5.5 A multi-agent case (my illustration)

Consider two copies of the agent that each receive a private input $x\in\{H,T\}$ chosen independently at random, and are paid only if they play the same action when $x_1\neq x_2$. A policy $\pi$ (say "play $x$" or "always play A") determines both copies' behavior, since both run the same function. The score of $\pi$ is computed with *both* copies' outputs set to $\pi$ on their respective inputs. Intervening on one input at a time would let each copy treat the other's output as fixed at a different input. This is the kind of case where the footnote's remark suggests policy-level intervention is the right object, but I stress that it is my reconstruction, not an example from the source.

## 6. Open questions the footnote leaves

1. **Subjunctive dependence is an input.** The source states this plainly. P-FDT needs a graph $G$ over policies, and nobody knows how to learn one. My operational suggestion: build $G$ from explicit modeling facts in the problem, namely which processes are stated to contain a copy or accurate model of the agent. When the dependence is graded, use the stated accuracy as the edge strength, as the paper does with 0.99.
2. **Counterpossibles.** Intervening on a policy the agent will not in fact output is a counterlogical. The source brackets this and appeals to human competence. I add no new formal account.
3. **Size of $\Pi$.** $|\Pi|=|\mathcal A|^{|\mathcal X|}$ is exponential. For bounded agents I suggest evaluating the policy only on the inputs that have non-negligible probability under some candidate policy. This is an engineering proposal, and the source expresses only a general expectation that bounded agents resemble the idealized ones.
4. **Conditioning on non-policy-dependent information.** The paper's examples keep some information fixed, such as the accuracy variable or the payoff structure. The footnote doesn't say how to distinguish it from policy-dependent observations. My rule: an observation is conditioned on only if no node subjunctively dependent on $\pi$ is upstream of it. In every example above this rule reproduces the source's verdicts.
5. **Ties and self-reference.** The source notes a harmless quining self-reference and says the agent needs no knowledge of the value of $\textsc{fdt}$. Tie-breaking among equal-value policies is not discussed. I suggest any fixed rule, since the value is the same.
6. **Fairness.** The source claims FDT does well on "fair" problems, those where outcomes depend only on the agent's behavior and not on her procedure, and admits it lacks a formal definition (footnote 15). The same is true of P-FDT. Footnote 15 also shows that a problem punishing agents who match a copy of Fiona is unfair to her.

## 7. Why one might prefer P-FDT

Three of the paper's arguments transfer directly to the policy formulation. Utility: the policy that scores highest over the whole model is by construction the one that does best in expectation across observations, so no later temptation to deviate arises. Precommitment: the optimal policy is what a precommitting agent would pick, so P-FDT agents act as they would have committed to act, without paying for commitment devices. Value of information: because the policy is chosen over all inputs, an observation never reduces the score of the chosen policy. These are the source's arguments for FDT, and my claim is only that they are naturally stated at the policy level.

## 8. Conclusion

P-FDT is expected-utility maximization over policies, with counterfactuals produced by intervening on the decision function's output (a policy) and propagating through subjunctive dependence, not through causation alone and not through mere correlation. Applied to an observed input at the end, it matches the paper's action-indexed FDT in all single-agent examples I checked, and it differs, according to the source's cautious remark, only in some multi-agent settings. Its main limits are the same as the source's: the dependence graph must be supplied, the logical counterfactual is informal, and the notion of fair problem is unformalized. Footnote 16 is brief, so the formalization in Section 3 and the proposals in Section 6 are my interpretation and should be read as such.