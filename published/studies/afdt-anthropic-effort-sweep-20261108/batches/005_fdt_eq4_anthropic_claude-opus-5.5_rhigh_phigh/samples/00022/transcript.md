# 005_fdt_eq4_anthropic_claude-opus-5.5_rhigh_phigh / 00022

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/58116133-bfe2-417d-b074-87e9e918610f/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/58116133-bfe2-417d-b074-87e9e918610f/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Action Functional Decision Theory, Explained and Operationalized

## 1. What A-FDT is

Yudkowsky and Soares (2017) present *functional decision theory* as a rival to causal decision theory (CDT) and evidential decision theory (EDT). Its guiding question, in their words, is: "Which output of this very function would yield the best outcome?" Their primary formal definition, Equation (4) in Section 5, has the agent intervene on a variable representing the output of its decision procedure *on its actual input*, and it selects an **action**. Two footnotes (7 and 16) add that the authors' "preferred formalization" instead chooses a **policy**, meaning a map from observations to actions.

I call the Equation (4) theory **A-FDT** (action functional decision theory). I call the footnoted variant **P-FDT** (policy-selecting FDT). Both labels are mine; the paper uses "FDT" for both. The paper also mentions two other variants, which I name accordingly:

- **FDT\***, an idealized version built on a "true" operator for logical sentences.
- **Evidential FDT** (footnote 9), which conditions on logical facts instead of intervening on them.

My goal is to state A-FDT precisely, give a working procedure, compute its verdicts on standard cases, and mark where the source is silent and I am adding assumptions.

## 2. The common frame: expected utility over hypotheticals

The paper puts all three theories in one expected-utility template:

$$
\mathcal{EU}(a) = \sum_{j} P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j), \tag{1}
$$

Here $x$ is the observation history and "$\hookrightarrow$" is a connective for *decision hypotheticals*. Following Joyce (1999), the authors treat the interpretation of $\hookrightarrow$ as the free parameter that distinguishes decision theories. Writing $V = \mathcal U(\text{Outcome})$:

$$
\mathrm{EDT}(P,x) = \arg\max_a \mathbb E(V \mid \text{Obs}=x, \text{Act}=a), \tag{2}
$$
$$
\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E(V \mid do(\text{Act}=a), \text{Obs}=x). \tag{3}
$$

EDT conditions on the act. CDT performs Pearl-style surgery on a causal graph $G$: it severs the act from its causes, propagates the change downstream, and leaves everything else alone. The authors insist that "conditionals are not counterfactuals," and they treat hypotheticals as "decision-theoretic instruments constructed from beliefs." Hypotheticals in this sense are scratch-paper objects, not metaphysical possible worlds.

## 3. The A-FDT equation

Equation (4) of the source, which I take as the definition of A-FDT, reads:

$$
\text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\!\left(V \;\middle|\; do\big(\textsc{fdt}(\underline P,\underline G,\underline x) = a\big)\right). \tag{4}
$$

Each ingredient does specific work.

- **$P$** is a probability distribution over world variables. It includes variables for the outputs of mathematical functions, and in particular for the outputs of the A-FDT procedure on various inputs.
- **$G$** is a graph that says how changing a *logical* variable propagates to other variables. It encodes "logical, mathematical, computational, causal, etc." structure, not just physical causation.
- **$\textsc{fdt}(\underline P,\underline G,\underline x)$** is the node whose value is "what this algorithm outputs on this very input." The underline means dequoting: the node's name is built from the agent's own model. The authors appeal to Kleene's recursion theorem ("quining") to argue that this self-reference is harmless. The agent needs a variable *representing* its output, not knowledge of the output's value.
- **$do(\cdot)$** is Pearl's intervention operator, applied to that logical node rather than to the physical act.

The source identifies two differences from CDT:

1. **Point of intervention.** CDT intervenes on the token (the physical act). A-FDT intervenes on the type (the function's output). The slogan: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."
2. **Handling of observation.** CDT conditions on $\text{Obs}=x$. A-FDT does not condition. It handles observation "by changing which node it intervenes upon": seeing $y$ instead of $x$ means intervening on $\textsc{fdt}(\underline P,\underline G,\underline y)$.

The second difference is easy to miss and does most of the work in the surprising cases. Because A-FDT does not condition on what it saw, its hypotheticals can include worlds in which it *would have seen something else*.

One textual wrinkle bears directly on implementation. In the transparent Newcomb computation (Section 6), the source writes the objective as $\mathbb E(V\mid do(\textsc{fdt}(\ldots,\textit{full})=a, \text{Obs}=\textit{full}))$. The computation that follows, however, assigns weight to the branch where the box is empty. That is only possible if one does **not** condition on $\text{Obs}=\textit{full}$. I therefore read Equation (4) literally, with no conditioning on observations, and treat the extra "$\text{Obs}=\textit{full}$" as a slip. This reading is the only one consistent with the paper's numbers and with its explicit statement about how A-FDT responds to observation.

## 4. A recipe for applying A-FDT

The source says it brackets "the question of exactly how she achieves this feat of imagination" and requires only that the agent vary "all and only those things that subjunctively depend on the output of her decision-making procedure." The following procedure abstracts the paper's worked examples. Steps 2 and 3 make explicit modelling conventions the source uses but does not state as rules.

1. **List the inputs.** Identify every observation history $y$ that the agent's procedure might be run on in the scenario, by the agent or by any predictor, simulator, or twin. Create a node $\textsc{fdt}(y)$ for each.
2. **Wire the act.** Make $\text{Act}$ a selector: a deterministic function of whichever $\textsc{fdt}(y)$ corresponds to the input the agent actually receives, together with whatever determines that input. In transparent Newcomb, for example, $\text{Prediction}$ determines which node controls $\text{Act}$.
3. **Wire the dependents.** Draw an edge from $\textsc{fdt}(y)$ into every process that computes or accurately models that function on $y$. Represent imperfect models with independent noise nodes (the paper's *Accurate* node). Draw no edge into processes that are merely correlated with the agent, such as the lesion.
4. **Assign priors** to all exogenous nodes. This includes the non-intervened $\textsc{fdt}(y')$ nodes for $y'\neq x$, which keep their prior distribution under the intervention.
5. **Evaluate.** For each action $a$, apply $do(\textsc{fdt}(x)=a)$, propagate along $G$ without conditioning on $x$, and compute $\mathbb E V$. Output the argmax.

The prior on the intervened node itself is irrelevant, since surgery overrides it. This is why A-FDT, unlike EDT, is not "at the mercy of her priors" about her own action.

## 5. Worked examples

All payoffs below are in utility-dollars.

### Newcomb's problem and the twin prisoner's dilemma

Let $\textsc{fdt}$ feed both $\text{Act}$ and $\text{Prediction}$, with $P(\textit{accurate})=0.99$.

- **One-box:** $\mathbb E V = 0.99\cdot 10^6 + 0.01\cdot 0 = 990{,}000$.
- **Two-box:** $\mathbb E V = 0.01\cdot 1{,}001{,}000 + 0.99\cdot 1{,}000 = 11{,}000$.

A-FDT one-boxes. CDT's graph has no edge from the act to the prediction, so for any fixed probability $p$ that box B is full, two-boxing gains exactly $1{,}000$. CDT therefore two-boxes.

(The source reports \$999,000 for EDT's one-boxing value. The same arithmetic gives 990,000. The verdict is unaffected.)

The twin prisoner's dilemma is the same structure. Both twins' choices are children of one $\textsc{fdt}$ node, so the comparison is \$1,000,000 for mutual cooperation against \$1,000 for mutual defection, and A-FDT cooperates.

### The smoking lesion

Here the lesion is *not* wired to $\textsc{fdt}$. The paper's full model makes the lesion determine the agent's utility function ($\mathcal U_S$ or $\mathcal U_R$), and hence which of two procedure-nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ or $\textsc{fdt}(\underline{P_R},\underline G)$, controls the act. Intervening on the $S$-node leaves $P(\textit{lesion})=p$ unchanged. The source computes that smoking beats refraining by $p\cdot 1{,}000$, so A-FDT smokes. Combined with the Newcomb verdict, this answers Gibbard and Harper's apparent dichotomy: one rule both one-boxes and smokes.

The general lesson for practice is that the decisive modelling question is whether a process *evaluates the agent's decision function*, not whether it is correlated with the agent's act.

### Transparent Newcomb and Parfit's hitchhiker

The agent sees two full boxes, so $x=\textit{full}$. Let $q$ be the prior probability that $\textsc{fdt}(\textit{empty})=\textit{twobox}$.

**$do(\textsc{fdt}(\textit{full})=\textit{onebox})$:**
- With probability 0.99 the predictor is accurate, so the box is full and the agent one-boxes: $10^6$.
- With probability 0.01 the box is empty and $\textsc{fdt}(\textit{empty})$ acts: $1{,}000q$ in expectation.
- Total: $990{,}000 + 10q$.

**$do(\textsc{fdt}(\textit{full})=\textit{twobox})$:**
- With probability 0.99 the box is empty: $1{,}000q$.
- With probability 0.01 the box is full and the agent two-boxes: $1{,}001{,}000$.
- Total: $10{,}010 + 990q$.

(The extracted source prints this as "\$110,00 + q·\$990." The correct constant is 10,010.)

One-boxing wins for every $q\in[0,1]$. Even while looking at a full box, the agent's two-boxing hypothetical mostly contains an empty box. The source stresses that this is "precisely equivalent" to paying the driver in Parfit's hitchhiker problem: the driver's rescue plays the role of the full box, and payment in the city plays the role of leaving the \$1,000. A-FDT pays. CDT and EDT, given that they are already in the city, do not, and so they are left in the desert.

### XOR blackmail

The source says only "as you may verify," so here is the calculation, assuming an infallible predictor. Let $p$ be the prior probability of termites. The letter is sent iff (no termites and the agent would pay) or (termites and the agent would refuse). The agent intervenes on $\textsc{fdt}(\textit{letter})$.

**Pay:**
- Termites: no letter is sent, and the agent loses $10^6$.
- No termites: the letter arrives and the agent pays $1{,}000$.
- $\mathbb E V = -10^6 p - 1{,}000(1-p)$.

**Refuse:**
- Termites: the letter arrives, the agent refuses, and loses $10^6$.
- No termites: no letter, no loss.
- $\mathbb E V = -10^6 p$.

Refusal wins by $1{,}000(1-p)$. The intervention changes whether the letter arrives but never changes the termites.

EDT pays, because conditioning on paying drives $P(\textit{termites}\mid \textit{letter})$ to zero. CDT refuses, but its hypothetical for paying is one in which an infallible predictor erred. A-FDT's hypothetical is instead one in which the letter was never sent.

### Mechanical blackmail and its threshold

A blackmailer runs the damaging program iff she predicts the agent pays. She wrongly predicts payment with probability $\varepsilon$.

- **Pay:** the agent is always blackmailed and pays: $\mathbb E V = -1{,}000$.
- **Refuse:** the agent is blackmailed with probability $\varepsilon$ and then loses $10^6$: $\mathbb E V = -10^6\varepsilon$.

A-FDT refuses iff $\varepsilon < 10^{-3}$. The source's $\varepsilon = 0.0009$ (an expected loss of \$900) correctly yields refusal. Its follow-up claim, "If instead the chance of error is 0.011%, then she pays," conflicts with this threshold, since 0.011% is below 0.1%. Presumably 0.11% was meant. A reader applying A-FDT should trust the inequality, not the typo.

## 6. What A-FDT holds fixed, and what it varies

A-FDT's counterfactuals vary exactly three kinds of thing:

- the output of the decision function on the current input;
- everything downstream of that output in $G$, including other instances and models of the function and the physical consequences of all of them;
- *which observation the agent would have received*, when that observation is itself downstream.

They hold fixed everything not downstream: the laws, the lesion, the termites, and the agent's outputs on other inputs (at their priors).

Three consequences follow, each claimed by the source.

**Agreement in ordinary cases.** If every correlation between $\text{Act}$ and other variables is caused by $\text{Act}$, except its dependence on the $\textsc{fdt}$ node, then
$$\mathbb E[V\mid a] = \mathbb E[V\mid do(a)] = \mathbb E[V\mid do(\textsc{fdt}=a)],$$
and A-FDT, CDT, and EDT agree. They diverge only when something other than the act's effects tracks the decision, typically predictors, twins, or copies.

**Dominance is theory-relative.** CDT's dominance argument holds the prediction fixed while the act varies. The paper argues that every way of constructing hypotheticals induces its own dominance notion. Under A-FDT's notion, which holds subjunctive dependencies constant, A-FDT never takes a dominated act. Dominance therefore cannot adjudicate between theories, and the authors fall back on utility achieved.

**Precommitment without commitment devices.** Because A-FDT does not condition away the branches its own policy would have prevented, it "act[s] as [it] would have precommitted to act." The source claims this makes it reflectively stable "in fair problems": it would not self-modify into CDT on receiving blackmail. It also claims that A-FDT never assigns negative expected value to information.

## 7. Open questions and operational interpretations

### Constructing $G$

The source is explicit: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." Equation (4) takes $G$ as given, much as Equation (3) takes the causal graph as given. The authors also concede that the counterpossible "$\textsc{true}$" operator needed by FDT\* is undefined. They use $do$ on a supplied graph precisely to avoid it.

**My operational proposal.** To decide whether to draw an edge $\textsc{fdt}(y)\to Z$, ask whether $Z$ is produced by a process that *takes the agent's decision computation on input $y$ as its object*: running it, simulating it, reasoning about it, or being an independent implementation of it. The calculator analogy is the paper's guide here. Mere common causes, such as the lesion, a shared upbringing, or pink calculators, do not qualify. A graded version follows naturally: model $Z = f(\textsc{fdt}(y), N)$, where $N$ is independent noise whose distribution encodes the predictor's reliability. This matches the paper's *Accurate* node and its remark that imperfection "weaken[s], but [does] not eliminate[]" dependence.

What this proposal leaves unresolved is *partial similarity*. For example, should the agent wire an edge to an agent that runs a slightly different procedure? I see no principled answer in the source. A reasonable default is to estimate the probability that the other process's output equals one's own across the decisions relevant to the problem, and to encode that as a noise node. This is an assumption, not the authors' claim.

### Priors over one's own outputs on other inputs

In A-FDT the non-intervened nodes $\textsc{fdt}(y')$ keep their prior distribution. In the paper's examples the verdict is robust to these priors ($q$ "doesn't matter"). That robustness is a property of those examples, not a theorem. The source suggests that "correct" values exist ($q=1$ in transparent Newcomb, $q=0$ in the lesion case), which presupposes the agent can solve its other subproblems. A practical convention, again my own, is to set these priors by actually running A-FDT on the other inputs when feasible, and to report sensitivity to them otherwise.

### Action versus policy

The authors prefer P-FDT, which intervenes on the node to choose a map $\pi:\mathcal X\to\mathcal A$ and then applies it to $x$. They say the difference matters only "in certain multi-agent dilemmas." Here is a toy case of my own construction showing how it can matter.

Two copies of the same agent receive different labels, *red* and *blue*. Each picks $L$ or $R$, and each is paid 10 if the picks match and 0 otherwise.

- **Under A-FDT**, the *red* copy intervenes on $\textsc{fdt}(\textit{red})$ while holding $\textsc{fdt}(\textit{blue})$ at its prior. With a uniform prior, both actions have expected value 5, so A-FDT is indifferent, and the two copies can miscoordinate.
- **Under P-FDT**, the agent compares whole policies. Any matching policy, such as $\textit{red}\mapsto L,\ \textit{blue}\mapsto L$, yields 10.

The general diagnosis: A-FDT treats its outputs on different inputs as separately settable. That is harmless when the other-input nodes only matter through branches whose weight does not depend on the current choice. It can fail when those outputs must be coordinated. If the problem involves several instances of one's procedure facing *different* observations, the reader should use P-FDT or check the A-FDT verdict for sensitivity to the other-input priors.

### Fairness

The authors concede that any theory can be defeated by a problem that punishes it by name. They claim only superiority on "fair" problems, those in which outcomes depend on the agent's behaviour in the problem at hand. Footnote 15 admits that this notion is not yet formalized: an "act differently from Fiona" game is unfair to A-FDT, but there is no general way to construct its analogue for rival theories.

## 8. Conclusion

A-FDT is CDT's machinery aimed at a different node. It performs surgery on the logical variable "what my decision function outputs on this input," and it lets observations select which such node to intervene on, instead of conditioning on them. Two habits follow:

- It honours dependencies created by predictors, twins, and simulations, which CDT ignores.
- It ignores merely statistical correlations, which EDT honours.

The resulting verdicts follow from the arithmetic above: one-box in Newcomb, smoke in the lesion case, one-box in transparent Newcomb, pay in Parfit's hitchhiker, refuse in XOR blackmail, and refuse mechanical blackmail when the error rate is below $10^{-3}$.

The theory is only as determinate as the graph $G$ it is given. Building that graph from evidence is the central unsolved problem the authors themselves flag. And where coordination across one's own different inputs matters, the action-level Equation (4) should give way to the policy-level P-FDT that the authors prefer.

---

**References**

Yudkowsky, E. & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality.* arXiv:1710.05060.
Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
Joyce, J. (1999). *The Foundations of Causal Decision Theory.*
Pearl, J. (2000). *Causality.*
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working on an essay about A-FDT, the action version of functional decision theory, which I'm taking from Equation (4) as the main formal statement. Here the intervention is on the FDT node to set an action, unlike the policy version in footnotes 7 and 16. I'll keep the name "A-FDT" consistent throughout, including headings and examples, and compare it with CDT, EDT, and the policy version.

I'm settling on the name for the policy-selecting variant, since the source only calls the whole family FDT. I'll use "A-FDT" for the action version and mark the policy version separately, while also noting the related FDT*, the evidential footnote version, TDT, and UDT that the source mentions.

I'm working through the worked examples now, starting with Newcomb's problem: one-boxing gives about $990,000 under an accurate predictor, while two-boxing comes to roughly $11,000. I'll also keep in mind that the source's EDT figure of $999,000 doesn't match its own arithmetic.

I'm running the transparent Newcomb case now: one-boxing gives roughly 990,000 plus a small term from the q-dependent branch. For two-boxing, if the predictor is accurate, the box is empty and I only get the q-weighted payoff, but if it's inaccurate, the full box plus both boxes is what the agent takes.

I'm checking the transparent Newcomb expected utility for two-boxing, which comes to about 10,010 plus 990q, so one-boxing wins for every q in the unit interval. Next I'm running the smoking lesion case, where the two FDT nodes give a difference of roughly p·1000 in favor of smoking. Then I'll set up XOR blackmail with a prior probability p of termites and a letter predictor, starting with the payoff under the intervention that sets the letter node to pay.

I'm working through the XOR blackmail payoffs: under the policy to pay, the expected utility is roughly −p·1,000,000 − (1−p)·1,000, while refusing gives −p·1,000,000, so refusing comes out ahead by (1−p)·1,000. Next I'm turning to the mechanical blackmail variant, where the predictor's error rate decides which policy looks better.

I'm checking the blackmail threshold: refusing wins whenever the error rate is below 0.1%, since a 0.1% chance of losing $1,000,000 is worth exactly the $1,000 cost of paying. The source's 0.0009 case therefore favors refusing, and its 0.011% figure would too, so "0.11%" is probably what was meant.

I'm checking how the action version handles the observation: the node fdt(P,G,x) is tied to the specific input x, so each observation gets its own intervention. The open question is when action and policy versions actually come apart, which the source ties to multi-agent dilemmas. My working guess is that they diverge when the output on other inputs is uncertain and logically linked to this one, but Eq (4) holds those other-input nodes at their prior distribution, the same way the source treats q, and in its examples the result doesn't depend on that choice.

I'm now testing whether action-version A-FDT and the policy version actually diverge, and I'm sketching a coordination case: two copies of the agent get different observations and must match their choices. Under A-FDT each copy intervenes on its own node while holding the other's at its prior, so the copies might settle into a worse outcome than the joint policy would reach.

I'm checking whether the action version gives a different result from the policy version in cases where the outputs on other inputs are uncertain. Next I'm working through the open questions: how to build the graph, what counts as implementing the function, and how imperfect predictors and near-copies should be modeled, probably as noisy nodes with a reliability parameter.

I'm getting ready to lay out the essay's structure: a short account of what A-FDT is, the shared expected-utility framework, a breakdown of Equation (4), a practical recipe with my own additions marked, and then the worked cases starting with Newcomb's problem and the smoking lesion.

I'm moving on to the transparent Newcomb case and the XOR blackmail setup, then checking where the mechanical blackmail threshold falls.

I'm finishing the thought about the essay's framing: the source treats the "subjunctive dependence" idea as the functional analogue of causal dependence, and calls working out its structure the field's biggest open problem. Then I'm settling on the A-FDT equation itself, which intervenes on the FDT node with a chosen action and takes the expected value of V under that intervention.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/681415b1-143e-4263-a1fb-8ebee8812330/call_0/request.json)

[Authoritative raw response](../../../../../../runs/681415b1-143e-4263-a1fb-8ebee8812330/call_0/response.raw) · finish: `stop`

### Visible response

````text
Under A-FDT as the essay interprets it, I intervene only on the node for my own input, `fdt(Rowan's observation)`. Sasha's copy runs the same procedure on a different input, with a different name and a different lead. Its output is the separate node `fdt(Sasha's observation)`, which stays at its prior under my intervention. This is the essay's red/blue case: outputs on different inputs are treated as separately settable.

Let q be the prior probability that Sasha keeps quiet:

- **Pass:** 2q + 5(1−q) = 5 − 3q years
- **Submit:** 0·q + 4(1−q) = 4 − 4q years

Submitting is better by 1 + q years for every q in [0, 1], so the verdict does not depend on the prior.

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm checking whether, under A-FDT as the essay describes it, the two copies' decisions are linked: intervening on my observation leaves the other copy's node at its prior, and I'm asking whether there's a causal edge between the two nodes at all.

I'm reasoning that under A-FDT, the other copy's node stays at its prior since it's a separate input, so defecting dominates and the letter should be sent.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/681415b1-143e-4263-a1fb-8ebee8812330/call_1/request.json)

[Authoritative raw response](../../../../../../runs/681415b1-143e-4263-a1fb-8ebee8812330/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under the essay's reading of A-FDT, I intervene only on the node for my own decision on my actual input, fdt(Sasha's observation). Rowan's copy runs the same function on a different input, with a different name and a different lead, so its output comes from the separate node fdt(Rowan's observation). That node stays at its prior and is not changed by my intervention (essay §4, step 4, and §7).

With Rowan's choice fixed at any prior q = P(Rowan sends):

- **Send:** expected sentence is 4q years.
- **Pass:** expected sentence is 2 + 3q years.

Sending is better by 2 − q ≥ 1 year for every q in [0, 1]. So the verdict holds whatever the prior is, which is the sensitivity check the essay recommends.

submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working out how A-FDT applies here, since the two copies see different observations. My own copy is intervened on through its observation, while the other copy's output is a separate node that stays at its prior. Per the essay, outputs on different inputs can be set separately, so the other copy's action doesn't move with mine.

Checking whether the other copy's output depends on mine under A-FDT: it runs the same function on a different input, so the essay's recipe gives no edge from my intervention to its action. The essay itself flags coordination as a weak spot, but the sensitivity check shows submitting wins for any prior on the other copy's output, so I'll settle on submitting.

```
