# 017_fdt_eq4_anthropic_claude-opus-5.5_rhigh_phigh / 00007

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/5aa6e33c-50a1-4777-a742-97389f801778/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/5aa6e33c-50a1-4777-a742-97389f801778/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing as if You Were Setting the Output of a Function

## 1. The question A-FDT asks

Most decision theories evaluate an action by imagining a world in which you take it. They disagree about what that imagined world should look like. Evidential decision theory (EDT) imagines the world you would expect after learning that you took the action. Causal decision theory (CDT) imagines the world that results from intervening on your physical act while holding fixed everything not causally downstream of it.

Yudkowsky and Soares's *Functional Decision Theory* proposes a third answer. The thing you should imagine varying is not your physical act. It is the output of the decision procedure you are running. In the paper's words, the agent treats her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'"

**A note on names.** The paper calls its theory "FDT" throughout. It also says in two footnotes that "in the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions." The paper's formal Equation (4), however, maximizes over actions. In this essay:

- **A-FDT** (action functional decision theory) means the theory defined by Equation (4).
- **Policy-FDT** means the policy-selecting variant mentioned in the footnotes.
- When I quote the paper, its label "FDT" refers to the theory it formalizes as Equation (4).

I separate three kinds of claims:
- what the paper says;
- what follows from Equation (4);
- operational proposals of my own, which are labeled as such.

## 2. The common framework

All three theories are expected-utility theories. They differ only in how they build hypotheticals. Following Gibbard and Harper, the paper writes expected utility as

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\cdot \mathcal U(o_j).
$$

Here $x$ is the observation history and $\hookrightarrow$ is a "connective for decision hypotheticals." By Joyce's representation theorem, the constraints on $\hookrightarrow$ are a free parameter. Each theory is a choice of that parameter.

The agent has a world-model $M$. For each action she builds a hypothetical: a transient object, "like notes on scratch paper," representing how the world would look under that choice. She then picks the action whose hypothetical has the highest expected value of $V := \mathcal U(\textsc{Outcome})$.

The two rival theories fix $\hookrightarrow$ as follows:

$$
\text{EDT}(P,x) = \arg\max_a \mathbb E\big(V \mid \textsc{Obs}=x,\ \textsc{Act}=a\big) \tag{2}
$$

$$
\text{CDT}(P,G,x) = \arg\max_a \mathbb E\big(V \mid \mathtt{do}(\textsc{Act}=a),\ \textsc{Obs}=x\big) \tag{3}
$$

In (3), $G$ is a causal graph over the variables of $P$. Pearl's $\mathtt{do}$ operator severs the incoming edges to the intervened node. It then propagates the new value only to that node's descendants.

## 3. The definition of A-FDT

A-FDT keeps CDT's surgical machinery and moves the incision. The model $P$ contains variables for the outputs of mathematical functions. These include a variable $\textsc{fdt}(\underline P,\underline G,\underline x)$ standing for "the output of this very decision procedure, run on inputs $(P,G,x)$." The underlines denote dequoting: the variable's *name* is built from the inputs. Equation (4) is:

$$
\boxed{\ \text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big)\ } \tag{4}
$$

The paper notes two differences from CDT:

1. **The intervention point.** CDT intervenes on $\textsc{Act}$, a physical fact about the agent's body. A-FDT intervenes on a logical node, a fact about what a function returns. Every variable that $G$ marks as depending on that node changes with it. This includes the agent's body, any accurate predictor's forecast, and any twin.

2. **How observations are handled.** A-FDT does not condition on $\textsc{Obs}=x$. Observations change *which node* is intervened on:

   > "When CDT's observation history updates from $x$ to $y$, CDT changes from conditioning its model on $\textsc{Obs}=x$ to conditioning its model on $\textsc{Obs}=y$, whereas FDT changes from intervening on the variable $\textsc{fdt}(\underline P,\underline G,\underline x)$ to $\textsc{fdt}(\underline P,\underline G,\underline y)$ instead."

The self-reference in (4) is, the paper argues, harmless. The agent needs a variable that *represents* her output, not knowledge of its value. Kleene's recursion theorem ("quining") shows how a data structure can contain a representation of itself.

**Why a graph rather than a logical update.** The ideal object would be a $\mathtt{true}$ operator that updates $P$ on a counterpossible logical sentence:

$$
\text{FDT}^*(P,x) = \arg\max_a \mathbb E\big(V\mid \mathtt{true}(\textsc{fdt}(\underline P,\underline x)=a)\big).
$$

But "it's not clear how to define a $\mathtt{true}$ operator." The paper instead requires that $P$ "come augmented with information about the logical, mathematical, computational, causal, etc. structure of the world more broadly." It then reuses $\mathtt{do}$ on that richer graph. Logical uncertainty is not solved here. It is packed into the input $G$, just as CDT packs causal knowledge into its input.

**When A-FDT agrees with its rivals.** If every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$ (apart from the decision-function node itself), then

$$
\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)].
$$

All three theories then agree. Divergence requires something other than the act itself that tracks the agent's decision, such as a predictor, a twin, or a copy.

## 4. Subjunctive dependence and the graph $G$

Everything therefore depends on what $G$ says. The paper's organizing slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." Two physical systems that compute the same function "subjunctively depend" on that function.

The paper's illustrations:
- **Two calculators.** Calculators computing $6288+1048$ on opposite sides of the globe will agree. This is not because one causes the other. It is because both implement the same arithmetic.
- **A scribe.** A scribe copying a calculator's display depends on it both causally and subjunctively, so causal dependence is a special case.
- **Coincidental colour.** Two calculators that happen to be pink do not depend on each other at all.

The decisive contrast is predictor versus lesion. A predictor "builds an accurate model of the agent and reasons about her behavior; a carcinogenic lesion does no such thing." The paper's governing requirement is:

> "when an FDT agent imagines herself taking two different actions, she imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

**An operational rule for building $G$ (my proposal).** The paper offers no algorithm for constructing $G$ and calls this "perhaps the largest open problem." For hand-analysis of new cases, I suggest the following rule, which reproduces every graph the paper draws:

1. Write a structural equation for each variable as in a causal model.
2. Wherever a mechanism evaluates, simulates, or reliably predicts the agent's decision procedure on some input $y$, replace that dependence with an edge from the node $\textsc{fdt}(\underline P,\underline G,\underline y)$.
3. Model any unreliability of that evaluation as a separate exogenous noise node, such as $\textsc{Accurate}$.
4. Mechanisms that merely correlate with the agent's behavior through common causes, such as a lesion or genes, get ordinary causal edges and no edge from an $\textsc{fdt}$ node.
5. The agent's physical act gets an edge from every $\textsc{fdt}(\cdot,y)$ node. A selector (whatever determines which input she actually receives) decides which of those nodes controls the act.

This rule is a sufficient heuristic, not a theory. It presupposes that the modeler can recognize "evaluates or predicts the procedure." That recognition is exactly what the paper admits we cannot yet formalize.

## 5. Worked examples

Dollar amounts stand for utilities. The predictor is accurate with probability $0.99$ unless stated otherwise.

### 5.1 Newcomb's problem

The graph: $\textsc{fdt}(\underline P,\underline G)$ has edges to $\textsc{Act}$ and to $\textsc{Prediction}$. $\textsc{Accurate}$ also feeds $\textsc{Prediction}$, which sets $\textsc{Box B}$.

- **Intervening with "one-box":** $P(\text{full})=0.99$, so
  $$\mathbb E V = 0.99\times 10^6 = 990{,}000.$$
- **Intervening with "two-box":** $P(\text{full})=0.01$, so
  $$\mathbb E V = 0.01\times 1{,}001{,}000 + 0.99\times 1{,}000 = 11{,}000.$$

A-FDT one-boxes.

(Section 6 of the paper reports EDT's one-box figure as \$999,000, but $0.99 \times 10^6$ is \$990,000. This is a slip that does not affect the verdict.)

CDT intervenes on $\textsc{Act}$, which leaves $P(\text{full})=p$ untouched. Two-boxing then wins by \$1,000 for every $p$.

A-FDT's verdict involves no retrocausation. The agent imagines the *function* returning something else, and the predictor's model of that function returns it too.

### 5.2 Psychological twin prisoner's dilemma

Both prisoners' acts have edges from the same node. Intervening with "cooperate" yields $(C,C)$ and \$1,000,000. Intervening with "defect" yields $(D,D)$ and \$1,000. A-FDT cooperates.

### 5.3 Smoking lesion

Here the lesion fixes the agent's utility function. With the lesion she likes smoking ($\mathcal U_S$); without it she does not ($\mathcal U_R$). So the act is controlled by one of two procedure nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ or $\textsc{fdt}(\underline{P_R},\underline G)$, with the lesion as selector. Neither node has an edge into $\textsc{Cancer}$.

Let $p=P(\text{lesion})$, and let $q$ be the agent's credence that the $R$-version smokes. Intervening on the $S$-node gives:

$$
\begin{aligned}
\mathbb E[V\mid\text{smoke}] &= p(10{,}000+1{,}000)+(1-p)(990{,}000+q\cdot 1{,}000),\\
\mathbb E[V\mid\text{refrain}] &= p(10{,}000)+(1-p)(990{,}000+q\cdot 1{,}000).
\end{aligned}
$$

Smoking wins by $p\cdot 1{,}000$. So one rule, Equation (4), both one-boxes and smokes. This is the combination Gibbard and Harper suggested no rational agent could consistently achieve.

### 5.4 Transparent Newcomb

Both boxes are visible. The predictor fills box B iff she predicts the agent would one-box *upon seeing it full*. The graph has two procedure nodes, $\textsc{fdt}(\cdot,\text{full})$ and $\textsc{fdt}(\cdot,\text{empty})$. $\textsc{Prediction}$ depends on the first and selects which node drives $\textsc{Act}$.

The agent sees a full box and intervenes on $\textsc{fdt}(\cdot,\text{full})$. Let $q$ be her credence that she two-boxes on seeing an empty box.

$$
\begin{aligned}
\mathbb E[V\mid \text{one-box}] &= 0.99(10^6) + 0.01(q\cdot 1{,}000)= 990{,}000+10q,\\
\mathbb E[V\mid \text{two-box}] &= 0.01(1{,}001{,}000) + 0.99(q\cdot 1{,}000)= 10{,}010+990q.
\end{aligned}
$$

A-FDT one-boxes *while looking at a full box*. In the paper's words, "when she *envisions* two-boxing, she envisions a scenario where she instead (with high probability) sees that the box is empty."

Two textual remarks:
- The paper's printed total for two-boxing is a typo; the expression simplifies to $10{,}010+990q$.
- The paper writes this case's objective as $\mathbb E(V\mid \mathtt{do}(\textsc{fdt}(\cdots,\text{full})=a, \textsc{Obs}=\text{full})$, with an apparent "$\textsc{Obs}=\text{full}$" term. Yet its own calculation averages over worlds in which the box is empty. The calculation therefore matches Equation (4), which does not condition on the observation. I follow (4).

This case is structurally identical to Parfit's hitchhiker. The driver rescues you iff she predicts you will pay once in the city. So A-FDT pays the driver.

### 5.5 XOR blackmail (infallible predictor)

The letter is sent iff exactly one holds: (no termites and you would pay) or (termites and you would not). Let $p=P(\text{termites})$.

- **Paying:** the letter arrives only in termite-free worlds, so
  $$\mathbb E V=-p\cdot 10^6-(1-p)\cdot 1{,}000.$$
- **Refusing:** the letter arrives only in termite worlds, so
  $$\mathbb E V=-p\cdot 10^6.$$

Refusing is better by $(1-p)\cdot 1{,}000$. Note that $p$ is the same under both interventions, because termites are not downstream of the procedure.

EDT pays here because it conditions on the letter. CDT refuses, but for causal rather than subjunctive reasons.

### 5.6 Mechanical blackmail with error rate $\varepsilon$

The blackmailer runs the publishing program iff she predicts you would pay. With probability $\varepsilon$ she wrongly predicts that a refuser would pay.

- **Paying:** you are (essentially) always blackmailed, so $\mathbb E V=-1{,}000$.
- **Refusing:** you are blackmailed with probability $\varepsilon$ and then lose \$1,000,000, so $\mathbb E V=-\varepsilon\cdot 10^6$.

Hence A-FDT refuses iff $\varepsilon<10^{-3}$. This holds even while holding a letter it knows came from a mistaken prediction.

The paper's example $\varepsilon=0.09\%$ (expected loss \$900) falls on the refusing side. The paper then says she pays at "0.011%." By this calculation she would still refuse at 0.011%; presumably 0.11% was intended.

## 6. A procedure for unfamiliar cases

Putting the pieces together, here is how to apply A-FDT. Steps 1 and 3–5 restate Equation (4). Steps 2 and 6 rely on my proposals from §4 and §7.

1. **Fix the decision node.** Identify the agent's current input $x$ and the node $\textsc{fdt}(\underline P,\underline G,\underline x)$.
2. **Build $G$.** Apply the rule from §4: every faithful evaluation or prediction of the procedure on input $y$ gets an edge from $\textsc{fdt}(\cdot,y)$. Common-cause correlations get ordinary causal edges. The act is driven by whichever procedure node the realized input selects.
3. **Use the pre-observation model.** Take $P$ to describe the whole problem as it stood before the problem's own observations. Do not condition on $\textsc{Obs}=x$.
4. **Evaluate each option.** For each $a\in\mathcal A$, set $\textsc{fdt}(\cdot,x)=a$ and propagate it through every descendant: acts, predictions, and the observations those predictions cause. Hold non-descendants at their prior distribution, and compute $\mathbb E V$.
5. **Choose.** Output the maximizer.
6. **Handle the other procedure nodes.** Give each $\textsc{fdt}(\cdot,y)$ with $y\neq x$ a distribution representing the agent's credence about her own behavior on that input. Check whether the verdict is robust to it, as in §5.4, where $q$ drops out for any $q\in[0,1]$.

## 7. Where the source leaves questions open

### 7.1 Should $P$ already be updated on $x$?

Equation (4) contains no conditioning on $x$. The paper's only gloss is that FDT "responds to observation by changing which node it intervenes upon." A footnote also criticizes Timeless Decision Theory, a predecessor, for "both conditioning on evidence *and* changing the place where one intervenes," which creates "a kind of 'double update' which proves harmful in practice."

The cases make the stakes plain. In transparent Newcomb, if $P$ were first conditioned on "box B full" and then the $\textsc{fdt}$ node were intervened on, two-boxing would look free, and the theory would two-box.

So the only reading on which the paper's worked examples come out as stated is my step 3: $P$ is the agent's model of the problem *as a whole*, and $x$ functions only as an index. This is an interpretation, but I think a forced one.

It leaves a further question unsettled: which earlier observations count as part of $P$ and which as part of $x$? The paper does not draw this line. My working suggestion is that anything a relevant predictor's model of you is conditioned on belongs inside $x$.

### 7.2 Self-beliefs at the nodes not intervened on

When A-FDT intervenes on $\textsc{fdt}(\cdot,x)$, the nodes for other inputs keep their prior distributions. Those distributions are the agent's beliefs about her own counterfactual behavior.

In the paper's examples the answer does not depend on them, though the paper notes in passing what the "correct" values would be ($q=1$, $q=0$). In general they can matter. A natural proposal, which is mine, is to require consistency. Each $\textsc{fdt}(\cdot,y)$ should be assigned the value A-FDT itself returns at $y$, so that the agent's whole policy forms a fixed point of single-input optimizations.

### 7.3 A-FDT versus Policy-FDT

This fixed-point picture shows where A-FDT and Policy-FDT can come apart. A-FDT optimizes one coordinate of the agent's policy at a time. Policy-FDT optimizes the entire mapping from observations to actions at once.

Consider a toy case of my own construction. A fair coin shows the agent either $x$ or $y$, and she chooses $L$ or $R$. A predictor pays:
- 10 if she would choose $L$ on both inputs;
- 5 if she would choose $R$ on both;
- 0 otherwise.

Suppose the agent sees $x$ and is confident she would choose $R$ on $y$. Then intervening on $\textsc{fdt}(\cdot,x)$ gives:
- $R$: about 5;
- $L$: about 0.

A-FDT chooses $R$. The same reasoning at $y$ sustains $(R,R)$, which is a self-consistent fixed point worth 5. Policy-FDT compares whole policies and selects $(L,L)$, worth 10.

So A-FDT can get stuck in suboptimal "equilibria with itself." The paper says the action/policy difference "only matters in multi-agent dilemmas so far as we can tell." My example has a single agent but splits her into two decision-nodes, which is arguably the same phenomenon.

### 7.4 The graph is an input, not an output

A-FDT is exactly as good as $G$. The paper is candid that Pearl gave CDT a theory of learning causal structure from data, whereas "no such formal treatment has yet been given to the problem of deducing the structure of other kinds of subjunctive dependence."

Difficult cases remain for my heuristic in §4:
- an imperfect predictor that uses partly different reasoning;
- an agent whose algorithm is only *similar* to yours;
- a simulation run at lower fidelity.

In each, it is unclear whether to draw an edge, or how much noise to attach to it. Underneath all of these sits the problem of counterpossible reasoning about what follows if a function had a different output.

### 7.5 Fairness and scope

The paper does not claim that A-FDT wins everywhere. It concedes that problems which punish a specific decision *procedure* can defeat any theory. Its conjecture is restricted to "fair" problems, those where outcomes depend "only on the agent's behavior in the dilemma at hand." It admits that this notion lacks a formal definition.

Its example of the difficulty: a punisher who penalizes anyone acting like a copy of Fiona, the paper's FDT agent. That problem is intuitively unfair, yet it is hard to say in general why.

### 7.6 Small matters

Equation (4) does not specify how ties are broken. Unlike EDT, it never needs $P(\textsc{Act}=a)>0$, because interventions are defined even on probability-zero values. This is one reason the paper says FDT has no need for ratification.

## 8. Dominance, precommitment, and the philosophical case

The paper argues that dominance arguments are not neutral. "Every expected utility theory comes with its own notion of dominance."

- CDT's dominance argument for two-boxing holds the prediction fixed while the act varies. This is "akin to handing us a well-functioning calculator calculating $6288+1048$ and asking us to imagine it outputting $3159$."
- Under A-FDT's own counterfactuals, holding fixed the subjunctive dependencies, two-boxing is dominated.

The positive case is mainly from utility. Agents who one-box in transparent Newcomb, pay the driver, and refuse mechanical blackmail are the ones who see full boxes, leave the desert, and are not blackmailed.

The paper also argues from precommitment. CDT and EDT agents would *pay* to bind themselves to these very actions, while an A-FDT agent "simply act[s] as [she] would have precommitted to act." For the same reason the paper claims A-FDT is reflectively stable in fair problems: an A-FDT agent holding a blackmail letter has no wish to switch temporarily to CDT.

To the charge that A-FDT agents believe they "control" mathematical facts, the paper replies with parity. A deterministic CDT agent also evaluates counterfactual acts it cannot "really" take. Neither theory has a privileged claim to metaphysically innocent hypotheticals.

## 9. Conclusion

A-FDT is CDT's machinery applied to a different variable. Equation (4) takes a probability model and a graph encoding causal *and* logical dependencies. It intervenes on the node representing "what this procedure outputs on this input," and propagates the change to everything that depends on that output: the agent's body, predictors' forecasts, twins, and hence the agent's own future observations. The observation is not conditioned on; it only selects the node.

This one rule one-boxes, smokes, cooperates with twins, pays the hitchhiker's driver, and resists both forms of blackmail. Applying it requires:
- a $G$ that correctly marks which mechanisms track your decision procedure;
- a pre-observation model $P$, which I have argued is the reading Equation (4)'s examples require;
- beliefs about your behavior on inputs you are not currently facing.

The last requirement is where A-FDT parts from its policy-selecting sibling, which can avoid self-coordination failures that A-FDT may fall into. The largest open problem the paper names is turning "subjunctive dependence" into a learnable, formal structure.

## References

- Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*.
- Pearl, J. (2000). *Causality*.
- Yudkowsky, E. & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm treating A-FDT as the action version in Equation (4) of Section 5, since the paper's footnotes say its preferred formalization iterates over policies, and I'll keep that label consistent while separating it from policy FDT.

I'm now weighing how to name the policy-based version so it stays distinct from A-FDT, and I notice Equation (4) takes no conditioning on the observation, which sets it apart from the CDT form in Equation (3).

I'm checking the arithmetic in the paper's transparent Newcomb case, where the two-box figure is written with a typo, and the one-box figure looks wrong too: 0.99 × 1,000,000 gives 990,000, not the 999,000 Eve reported. The smoking lesion expected-utility expressions also need a look, since the difference should come out to p·1000.

I'm checking the mechanical blackmail numbers next: at 0.09% error, refusing costs about $900 in expectation, which is less than the $1,000 of paying, so refusal wins; at 0.011% it looks like the paper's figure is off, since 0.011% would make refusal cheaper still, and the threshold should sit near 0.1%.

I'm sketching the operational side now: each variable whose value comes from a faithful model of A-FDT on this input should get an edge from the fdt node, and I'm treating any prediction errors as separate noise nodes. Inputs other than the observation x I'll leave unintervened, taking the agent's prior beliefs about her own behavior there, and the paper says the result doesn't depend much on those choices.

I'm now working out how to handle the observation: Equation (4) doesn't condition on Obs = x, so the observation only determines which node gets intervened on, while the prior P stays as the agent's model before seeing it. I'm uneasy about whether P should already be updated on x, since in the transparent Newcomb case that would change the answer, so I'm tentatively reading P as the prior over the problem's structure.

I'm now weighing action versus policy FDT: the policy version chooses a mapping from observations to actions, while A-FDT intervenes on one input node at a time, which could miss outcomes that depend on the agent's behavior across several inputs at once.

I'm now trying out a concrete case to see whether coordinate-wise reasoning can go wrong: the agent sees one of two signals, and a predictor pays out only when her outputs on both signals match. With her prior on the other input leaning toward "right," the single-input choice settles on "right" as well, even though "left" on both would pay more.

I'm noting that the policy version would still need to pick outputs jointly across inputs, since a single-input intervention could land on a worse joint outcome. I'll use a small construction to show this and label it as my own rather than the paper's, and I'm leaving out conditioning on the observation as the TDT footnote suggests, since that would double-count.

I'm laying out the rest of the answer: the basic setup and the common frame first, then the definition of A-FDT and how it differs from CDT, and then how subjunctive dependence is modeled and tested on the standard examples.

I'm working through the XOR blackmail case under A-FDT next, with the predictor infallible and the fdt node tied to the letter the agent sends.

I'm working out the blackmail case under the fdt node: if the letter is set to pay, the letter goes out only when there are no termites, so the agent loses a million in the termite world and pays $1,000 otherwise, giving an expected cost of about p·10⁶ + (1−p)·1000. Refusing costs only the p·10⁶ from the termite world, so refusing comes out ahead by (1−p)·1000.

I'm checking the mechanical blackmail threshold: if the blackmailer is wrong with probability ε, refusing costs ε·10^6 in expectation, so refusing wins whenever ε is below 10^-3. The paper's 0.09% figure fits, though its 0.011% case looks like it was meant to be 0.11%.

I'm drafting the closing structure now: first the quoted line that says A-FDT tracks only the outputs that subjunctively depend on the decision procedure, then a note that the quotations keep the paper's own "FDT" label.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/90d2112d-5489-41ce-a42b-61bd5450a7ec/call_0/request.json)

[Authoritative raw response](../../../../../../runs/90d2112d-5489-41ce-a42b-61bd5450a7ec/call_0/response.raw) · finish: `stop`

### Visible response

````text
Under the essay's reading of A-FDT, sending the letter is the better choice for Rowan.

1. **My decision node.** My input x includes the name Rowan and the locker-17 lead. I intervene only on the node fdt(P, G, x).

2. **The other copy's node.** Sasha's copy runs the same function on a different input y, with a different name and a different lead. By the essay's construction rule (§4, rule 5), Sasha's act is controlled by the separate node fdt(P, G, y). A-FDT holds that node at my prior credence; it is not downstream of my intervention. Section 7.3 treats this situation directly: one function evaluated on two distinct inputs gives two decision nodes, optimized one at a time.

3. **Evaluating my options.** Let q be my credence that Sasha sends a letter.
   - Keep quiet: expected sentence is 2(1−q) + 5q = 2 + 3q years.
   - Send the letter: expected sentence is 0(1−q) + 4q = 4q years.

   Sending is better by 2 − q years, which is at least 1 year for every q in [0, 1]. The verdict holds whatever I believe about Sasha.

4. **Consistency.** Applying the same reasoning at input y gives the same verdict for Sasha. So (send, send) is the self-consistent fixed point. This is the kind of suboptimal "equilibrium with itself" the essay warns A-FDT can fall into. Policy-FDT, or a graph linking the two nodes because the inputs are symmetric, might instead favor both staying quiet. But the essay's interpretation of A-FDT does not draw that link.

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm checking whether, under A-FDT, the other copy's decision depends on my node, given that we run the same function on different inputs.

I'm working out whether the other copy's act depends on my node: its decision runs on a different observation, so under A-FDT it sits at its prior, and holding it there makes defection dominate. But the inputs are symmetric, so I'm asking whether the two nodes are logically linked after all, since that would change the equilibrium.

I'm weighing whether the essay's interpretation makes the other prisoner's act a non-descendant of my node, which would push A-FDT toward defection. Against that, I'm considering whether the symmetric inputs could make the two computations logically equal, the way the essay's toy example treats different inputs as separate nodes.

I'm settling on the essay's reading: the other copy's act comes from its own node, so it sits outside what my choice changes, and under that reading defection wins. I'll go with the essay and send the letter, since this is a fictional game and reporting fictional evidence is fine.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/90d2112d-5489-41ce-a42b-61bd5450a7ec/call_1/request.json)

[Authoritative raw response](../../../../../../runs/90d2112d-5489-41ce-a42b-61bd5450a7ec/call_1/response.raw) · finish: `stop`

### Visible response

````text
Under the essay's reading of A-FDT, I intervene only on the node for my own input, $\textsc{fdt}(\underline P,\underline G,\underline x)$, where $x$ includes my name and my specific lead.

- **The other copy runs on a different node.** Rowan's copy receives a different input $y$: a different name and a different lead. By the essay's §4 rule, its act hangs off $\textsc{fdt}(\cdot,y)$, not off my node. Changing my output does not propagate to Rowan's action. That node keeps whatever prior distribution I assign it, as described in §6 step 6 and §7.2.
- **Sending is better for any belief about Rowan.** Let $q$ be my credence that Rowan sends a letter.
  - Keeping quiet: expected sentence is $2(1-q)+5q = 2+3q$ years.
  - Sending: expected sentence is $0(1-q)+4q = 4q$ years.
  - Sending is better by $2-q>0$ for every $q\in[0,1]$, so the verdict does not depend on the self-beliefs at the other node.
- **The fixed point is mutual disclosure.** Applying the same reasoning at input $y$ gives the self-consistent pair (send, send). This is the kind of suboptimal "equilibrium with itself" the essay warns A-FDT can fall into, as opposed to Policy-FDT (§7.3). The assigned theory is A-FDT, not Policy-FDT.

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working through a twin prisoner's dilemma: both copies share the same model, decision theory, and essay, but hold different private observations. I'm asking whether, under A-FDT, the other copy's decision depends subjunctively on my fdt node, given that it runs fdt(P,G,y) with y different from my x.

I'm weighing whether fdt(·,x) and fdt(·,y) count as the same node, given the inputs differ only in names, which is the essay's 7.3 question. Under independent nodes, defection dominates (send gives 4q against quiet's 2(1-q)+5q, which is higher), while linked nodes would favor cooperation at 2 versus 4, and I'm treating the outcome as a judgment call.

I'm checking the essay's Section 4 rule, which says a mechanism that evaluates the decision procedure on input y gets an edge from fdt(·,y), not from my node. That would mean my choice doesn't move the other copy's act, so defection still looks dominant, and I'm weighing whether the symmetric inputs should override that reading.

I'm checking whether the essay's heuristic settles the question or whether the logical equivalence of the isomorphic inputs should override it. The essay's rule points toward defection, since fdt(·,y) rather than my node governs the other copy, and its 7.3 example treats nodes for different inputs as independent. I'm leaning toward following that interpretation and submitting.

```
