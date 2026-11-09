# Policy Functional Decision Theory (P-FDT): Choosing the Function, Not the Act

## 1. What the source says

Yudkowsky and Soares's *Functional Decision Theory* (FDT) is mostly written in terms of actions. The decision rule chooses which action the agent's decision function should output on the input it actually received. Twice, however, the authors say that this is not the formulation they actually prefer. Footnote 7 says:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

Footnote 16, which this essay treats as the primary source, comes in the discussion of how an FDT agent responds to observations:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

I will call the theory described in footnote 16 **policy functional decision theory (P-FDT)**. When I mean the action-level rule given as equation (4) in the paper, I will say **action-FDT**. **CDT** (causal decision theory) and **EDT** (evidential decision theory) keep their usual meanings.

The footnote fixes three things:

1. The object of intervention is a node representing the decision function, written $\mathrm{FDT}(-)$, with the input slot left open.
2. The value chosen for that node is a policy, that is, a map from inputs to actions.
3. The agent obtains an action by applying the chosen policy to her actual input.

The footnote also makes one empirical claim: the difference from action-FDT "only matters in multi-agent dilemmas so far as we can tell."

Everything else is left open. Examples are the epistemic state from which policies are evaluated, the domain of the policy, how ties are broken, and whether randomization is allowed. I fill these gaps below and mark each proposal as my own.

## 2. Background: action-FDT

The paper frames all three theories as expected-utility maximizers that differ in how they build hypotheticals. The agent has a world-model $M = (P, G)$: a probability distribution $P$ plus a graph $G$ encoding dependencies. For FDT, $G$ encodes *subjunctive* dependence, meaning which variables would change if the output of a given mathematical function changed. CDT intervenes on the physical action node:

$$\mathrm{CDT}(P,G,x) = \arg\max_{a} \mathbb{E}\big[V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x\big].$$

Action-FDT intervenes instead on a logical node representing its own output on the current input:

$$\mathrm{FDT}(P,G,x) = \arg\max_{a} \mathbb{E}\big[V \mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)\big]. \tag{4}$$

The paper stresses that FDT "responds to observation by changing which node it intervenes upon" rather than by conditioning. A different observation $y$ means intervening on a different node, $\textsc{fdt}(\underline P,\underline G,\underline y)$.

Action-FDT therefore has one logical node per possible input. Each node stands for "what my function outputs on input $x$." When it deliberates at $x$, action-FDT sets only the node for $x$. The nodes for other inputs are left at whatever distribution $P$ assigns them. In the transparent Newcomb analysis, for example, the agent assigns an unknown prior $q$ to "I two-box on seeing an empty box," and the paper notes that the conclusion happens not to depend on $q$. That dependence on beliefs about one's own behavior at other inputs is exactly what P-FDT removes.

## 3. The definition of P-FDT

Let $\mathcal X$ be the set of inputs (observation histories) the agent's decision function might receive, and $\mathcal A$ the set of actions. A **policy** is a function $\pi:\mathcal X\to\mathcal A$. Write $\Pi = \mathcal A^{\mathcal X}$ for the set of all policies.

P-FDT models its decision function as a single node $\textsc{fdt}(\underline P,\underline G)$ whose values are policies. A node elsewhere in the world-model that subjunctively depends on "what this function does on input $y$" reads off $\pi(y)$. This covers the agent's own body, a predictor's simulation of the agent, or a copy of the agent. In particular the agent's physical action is

$$\textsc{Act} = \pi(\textsc{Obs}),$$

and a predictor who simulates the agent on input $y$ outputs $\pi(y)$, perhaps with noise.

**P-FDT.** Given a model $(P,G)$ and an actual input $x$:

$$\pi^* \in \arg\max_{\pi\in\Pi}\ \mathbb{E}_P\big[V \mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G)=\pi)\big],\qquad \text{P-FDT}(P,G,x) = \pi^*(x).$$

In words: for each candidate policy, imagine a world in which *this very function* implements that policy everywhere it is computed. Propagate the consequences through every subjunctively dependent node, including your own action, predictors' predictions, and copies' behavior. Score the imagined world by expected utility. Adopt the best policy and then execute its value at the input you actually have.

The shape of this formula is fixed by the footnote. The surrounding details are mine. The footnote does not say whether $\pi$ is evaluated against $P$ or against $P(\cdot\mid x)$, or which inputs are in $\mathcal X$. I take these up in §6.

## 4. Worked examples

### 4.1 Transparent Newcomb

Box A always holds \$1,000. Box B holds \$1,000,000 iff the predictor predicted the agent would one-box *upon seeing B full*. The predictor is accurate with probability $0.99$. The relevant inputs are $\mathcal X=\{\textit{full},\textit{empty}\}$, so there are four policies. Write a policy as $(\pi(\textit{full}),\pi(\textit{empty}))$, with 1 for one-box and 2 for two-box.

The predictor's behavior depends on $\pi(\textit{full})$:

- **If $\pi(\textit{full})=1$:** B is full with probability $0.99$, and the agent then takes \$1,000,000. With probability $0.01$ B is empty, and the agent gets \$1,000 if $\pi(\textit{empty})=2$ and \$0 otherwise.
- **If $\pi(\textit{full})=2$:** B is full with probability $0.01$, and the agent two-boxes for \$1,001,000. Otherwise B is empty and $\pi(\textit{empty})$ applies.

The four values are:

| policy $(\pi(\textit{full}),\pi(\textit{empty}))$ | expected utility |
|---|---|
| $(1,1)$ | $990{,}000$ |
| $(1,2)$ | $990{,}010$ |
| $(2,1)$ | $10{,}010$ |
| $(2,2)$ | $10{,}010 + 990 = 11{,}000$ |

The optimum is $\pi^*=(1,2)$. Seeing a full box, the agent one-boxes; seeing an empty one, she takes the \$1,000. This agrees with the paper's action-FDT verdict.

Note what has changed. The paper's calculation carried a free parameter $q$, the agent's credence in her own behavior given an empty box. Here that quantity is a decision variable, settled jointly with the rest.

### 4.2 Mechanical blackmail

A blackmailer launches a damaging program (cost \$1,000,000) iff she predicts the agent would pay \$1,000 upon receiving the blackmail. Suppose that with probability $e$ she wrongly predicts payment, so a refuser is blackmailed with probability $e$. The relevant input is $\textit{blackmail}$; the agent's behavior at the empty input is irrelevant here.

- The policy $\pi(\textit{blackmail})=\textit{pay}$ yields $-1{,}000$.
- The policy $\pi(\textit{blackmail})=\textit{refuse}$ yields $-1{,}000{,}000\,e$.

P-FDT therefore refuses whenever $e<0.001$, *including* when the agent is holding the letter.

Holding the letter does not change the verdict, because the policy is evaluated over the whole input space rather than only the branch the agent finds herself in. This matches the paper's verdict that Fiona refuses. The threshold calculation is mine.

### 4.3 Where P-FDT and action-FDT diverge: coordinating copies

Footnote 16 claims the distinction only matters in multi-agent dilemmas. Here is a problem of my own construction that shows why.

> **Two Rooms.** Two exact copies of an agent, running the same decision function, are placed in separate rooms. One copy is shown a red card and the other a blue card, and both know this setup. Each chooses $A$ or $B$. If both choose $A$, each receives 10. If both choose $B$, each receives 5. Otherwise each receives 0.

Policies are maps $\{\textit{red},\textit{blue}\}\to\{A,B\}$. Under P-FDT, intervening on the single function node fixes *both* copies' behavior at once:

| policy (red, blue) | each copy's payoff |
|---|---|
| $(A,A)$ | 10 |
| $(B,B)$ | 5 |
| $(A,B)$ | 0 |
| $(B,A)$ | 0 |

$\pi^*=(A,A)$, and each copy, applying $\pi^*$ to its own card, chooses $A$.

Action-FDT handles this differently. Suppose the red copy deliberates. It intervenes on $\textsc{fdt}(\underline P,\underline G,\textit{red})$ but leaves $\textsc{fdt}(\underline P,\underline G,\textit{blue})$ at its prior distribution. Let $r=P(\textsc{fdt}(\ldots,\textit{blue})=A)$. Then

$$\mathbb{E}[V\mid \mathtt{do}(\cdot=A)] = 10r,\qquad \mathbb{E}[V\mid \mathtt{do}(\cdot=B)] = 5(1-r).$$

The red copy picks $A$ iff $r>1/3$. Its choice is hostage to a prior about its own behavior on a different input, just as EDT's choices can be hostage to priors about its own actions.

Self-consistent but suboptimal outcomes are possible. If both copies believe "on the other card I play $B$" ($r\approx 0$), both play $B$, and the belief is confirmed. The pair is locked into the inferior equilibrium worth 5. P-FDT is not exposed to this, because it never holds its own behavior on other inputs fixed. It chooses that behavior.

### 4.4 Why the divergence appears

The pattern above generalizes. This argument is my own reconstruction, offered to make the footnote's "so far as we can tell" precise.

Suppose policy value is **separable across inputs**:

$$\mathbb{E}[V\mid \mathtt{do}(\pi)] = c + \sum_{y\in\mathcal X} g_y\big(\pi(y)\big).$$

This means each input-slot of the function influences utility through its own channel, with no interaction terms. Then:

- The joint argmax over $\Pi$ is obtained coordinatewise: $\pi^*(x)\in\arg\max_a g_x(a)$.
- Action-FDT at input $x$ maximizes $g_x(a)$ plus a term that does not depend on $a$, namely the prior expectation of the other slots.

So the two theories agree, whatever the agent's priors about her other-input behavior.

Transparent Newcomb and mechanical blackmail are separable. The \$1,000,000 depends on $\pi(\textit{full})$ alone, and $\pi(\textit{empty})$ only adds an independent small term. That is why the paper's $q$ never mattered.

Interaction terms such as $g_{xy}(\pi(x),\pi(y))$ arise when utility depends *jointly* on the function's outputs at different inputs. The natural source is several simultaneously instantiated copies or predictions receiving different inputs, as in Two Rooms. When interactions exist, action-FDT computes a best response to its own prior over other slots. It can then settle into a coordination failure that P-FDT's joint optimization avoids.

Single-agent interaction is also conceivable, for instance a predictor who rewards the agent according to how its responses to *two* hypothetical inputs relate. The source's "so far as we can tell" leaves that possibility open.

## 5. Philosophical motivation

P-FDT completes the paper's central thought. FDT's slogan is that the agent controls the *type* (the function) rather than the *token* (the physical act). Yet a function is its whole graph of input-output pairs, and action-FDT intervenes on only one entry of that graph at a time. P-FDT intervenes on the function itself. It asks: "What would the entire universe look like if this algorithm were the algorithm that does $\pi$?"

That is the paper's "global perspective" taken literally.

It also makes the paper's precommitment argument exact. The authors say FDT agents "simply act as they would have ideally precommitted to act." An ideal precommitment is precisely a policy chosen before seeing the input. P-FDT is the optimal-precommitment rule performed in deliberation, without any physical binding.

Finally, it connects to Wei Dai's updateless decision theory, which the paper names as an early variant and which shares this "choose a policy, then apply it" shape. The paper's remark that the older timeless decision theory's "double update" (conditioning on evidence *and* switching the intervention point) "proves harmful in practice" foreshadows the first open question below.

## 6. Open questions and proposed resolutions

### 6.1 From what epistemic state are policies evaluated?

The footnote says the agent applies her inputs to the policy *after* choosing it. It does not say whether the expectation is taken under $P$ or under $P(\cdot\mid\textsc{Obs}=x)$.

**Proposal:** under $P$, the model *prior* to the inputs in $\mathcal X$.

My reason is that conditioning on $x$ before scoring policies makes the values $\pi(y)$ for $y\neq x$ nearly irrelevant, and it reintroduces the double update. In transparent Newcomb, conditioning on *full* and then intervening yields

$$\mathbb{E}[V\mid \mathtt{do}(\pi),\textit{full}],$$

a quantity that is ill-defined or misleading when $\pi(\textit{full})=2$ makes *full* nearly impossible. The policy formulation is coherent exactly when the observation enters only as the argument to $\pi^*$.

This raises a further question: which prior? I suggest the agent's model as of the point where the inputs in $\mathcal X$ become possible, that is, the beginning of the dilemma. The paper's own equation (4) also omits conditioning on $\textsc{Obs}$, which fits this reading.

### 6.2 What is $\mathcal X$?

Taking $\mathcal X$ to be all possible observation histories makes $\Pi$ astronomically large or infinite. The argmax may then not even be attained, although bounded utility guarantees a finite supremum.

**Proposal:** restrict $\mathcal X$ to inputs relevant to the dilemma, meaning those that some dependent node in $G$ reads. Treat behavior on all other inputs as fixed by the agent's general policy. This mirrors how the paper builds "the simplest possible world-models." It is legitimate when the omitted inputs are separable in the sense of §4.4.

### 6.3 What depends on the policy?

P-FDT inherits FDT's largest open problem. We need a graph $G$ saying how changing the function's output would change other variables, and no method yet exists for learning such graphs analogous to Pearl's causal discovery.

P-FDT sharpens this requirement. Every dependent node must specify *which input slot* $\pi(y)$ it reads. A predictor in transparent Newcomb reads $\pi(\textit{full})$, not $\pi(\textit{empty})$. Getting the slot right is as important as getting the dependence right.

### 6.4 Ties and canonical choice

Consider anti-coordination: in Two Rooms, change the payoffs so the copies win only if they choose *differently*. Then $(A,B)$ and $(B,A)$ tie. If each copy broke the tie independently, they could miscoordinate.

**Proposal:** P-FDT must include a deterministic, input-independent tie-breaking rule, such as a fixed ordering on $\Pi$. Because the copies compute the same function, they then select the same $\pi^*$ and apply it to their different inputs. This is not a cosmetic detail. In multi-agent problems the policy formulation's advantage depends on all instances computing the *same* argmax.

### 6.5 Randomization

The footnote defines policies as maps from inputs to actions, so they are deterministic. One could extend $\Pi$ to maps $\mathcal X\to\Delta(\mathcal A)$. This extension is my own, not the source's.

It matters only when the environment contains randomness the predictor cannot see, like the "truly random coin" in the paper's Death in Damascus discussion. In that case a mixed policy should be evaluated with predictors reading the mixture, not the realized draw.

### 6.6 Self-reference

The node $\textsc{fdt}(\underline P,\underline G)$ is named inside the model it evaluates. The paper invokes Kleene's recursion theorem to show such self-representation is constructible. P-FDT needs only that and does not add any new self-reference.

## 7. A recipe for unfamiliar cases

1. **List the inputs** $\mathcal X$ that the agent's decision function might receive in the problem and that anything else depends on.
2. **Identify every instantiation** of the function: the agent's own body, simulations, predictions, copies, and future selves facing relevantly identical decisions. Note which input each one receives.
3. **Build the model** $(P,G)$ prior to those inputs. Let each instantiation read $\pi(y)$ for its input $y$, and give non-subjunctive correlates, like the smoking lesion, no edge from the function node.
4. **Score each policy** by $\mathbb{E}[V\mid\mathtt{do}(\pi)]$.
5. **Choose** $\pi^*$, breaking ties canonically.
6. **Act** on $\pi^*(x)$ for the actual input $x$.

As a check, if the problem is separable across inputs (§4.4), the result must agree with action-FDT. Any disagreement then signals an error in the model.

Applied to the smoking lesion, step 3 gives the lesion no edge from the policy node, so every policy faces the same cancer risk. P-FDT smokes, as the paper says FDT does. Applied to Parfit's hitchhiker, the driver reads $\pi(\textit{in city})$, so the policy of paying wins and the agent pays on arrival.

## 8. Conclusion

P-FDT takes FDT's central move seriously: choose the output of the function, not the act. It does so by selecting the whole function at once. The agent intervenes on a single node representing her decision procedure, scores each input-to-action policy by the expected utility of the world in which that policy is what the procedure does, and then applies the winning policy to her actual observation.

In problems where utility is separable across inputs, which covers every dilemma analyzed in the source, P-FDT and action-FDT coincide. That is why the authors could set the distinction aside. Where several instances of the function receive different inputs and payoffs depend on their joint behavior, action-FDT can become trapped by its own priors about its behavior elsewhere, and P-FDT cannot.

The footnote leaves real choices open: the evaluating prior, the policy domain, tie-breaking, and randomization. It also inherits FDT's unsolved problem of specifying subjunctive dependence. Reading the policy as evaluated under the pre-observation model, over the relevant inputs, with canonical tie-breaking, gives a theory precise enough to apply case by case.

**References.** Yudkowsky, E. & Soares, N., "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060 (esp. footnotes 7 and 16, eq. 4). Dai, W., "Towards a New Decision Theory," *Less Wrong*, 2009. Pearl, J., *Causality*, 2000. Gibbard, A. & Harper, W., "Counterfactuals and Two Kinds of Expected Utility," 1978.