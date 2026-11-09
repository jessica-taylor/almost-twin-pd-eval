# A-FDT: Choosing as the Output of a Function

## 1. The question A-FDT asks

Standard decision theory asks what an agent should *do*. Yudkowsky and Soares's paper "Functional Decision Theory: A New Theory of Instrumental Rationality" changes the object of choice. Its abstract describes the agent as one who should

> "treat one's decision as the output of a fixed mathematical function that answers the question, ``Which output of this very function would yield the best outcome?''"

The paper calls its theory FDT. In this essay, **A-FDT** (action functional decision theory) means the specific formalization in Equation (4) of the paper's Section 5. In that equation, the agent intervenes on the node representing her decision function's output and sets it to an *action*. I use the separate name because the authors also mention, in footnotes 7 and 16, a preferred variant in which the agent chooses a *policy* rather than an action. I call that variant **policy-FDT**. When I quote the paper, its word "FDT" refers to the theory as the paper presents it, and Equation (4) is A-FDT.

The other theories discussed here are evidential decision theory (EDT) and causal decision theory (CDT).

## 2. The common expected-utility template

The paper treats EDT, CDT and A-FDT as variants of a single expected-utility scheme (Eq. 1, after Gibbard and Harper):

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j).
$$

The symbols are as follows:

- $a$ ranges over a finite action set $\mathcal A$.
- $x$ is the observation history.
- $\mathcal U$ is the utility function.
- $P(a \hookrightarrow o_j; x)$ is the probability of outcome $o_j$ "in the hypothetical scenario where the action $a$ is executed."

Following Joyce, the three theories agree about how to value prospects. They disagree only about how to read the connective $\hookrightarrow$.

Operationally, the agent holds a world-model $M$. For each action $a$ she builds a *hypothetical* $M^{a\hookrightarrow}$, which the paper describes as "decision-theoretic instruments constructed from beliefs," not beliefs themselves. She then picks the action whose hypothetical has the highest expected value of $V := \mathcal U(\textsc{Outcome})$. The three theories build their hypotheticals differently:

- **EDT** (Eq. 2) conditions: $\arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a)$.
- **CDT** (Eq. 3) intervenes on the physical act in a causal graph $G$: $\arg\max_a \mathbb E(V \mid \mathrm{do}(\textsc{Act}=a), \textsc{Obs}=x)$.

## 3. The A-FDT equation

The world-model is a pair $(P,G)$. $P$ is a probability distribution, and it now includes variables for the outputs of mathematical functions. $G$ is a graph saying how changing such a logical variable affects other variables. The paper's Equation (4) reads, in its notation:

$$
\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\!\left(V \;\middle|\; \mathrm{do}\!\left(\textsc{fdt}(\underline P,\underline G,\underline x)=a\right)\right). \tag{4}
$$

This is what I call A-FDT. Several features need unpacking.

**The intervention node.** $\textsc{fdt}(\underline P,\underline G,\underline x)$ is a variable in the agent's own model. It represents the output of the A-FDT algorithm on exactly this input. The underlines denote dequoting: the variable's *name* is built from the model itself.

The self-reference is deliberate. The paper argues it is harmless because the agent only needs a variable *representing* her output, not knowledge of its value. Quining (Kleene's recursion theorem) shows that such self-representing data structures exist. The prior probability the agent assigns to this node does not matter, because the do-operator overwrites it.

**Propagation.** Pearl's $\mathrm{do}$ sets the node to $a$ and recomputes everything downstream of it in $G$. Everything else keeps its prior distribution. The node typically has several children:

- the agent's physical act, and
- any other process that, per $G$, depends on the same function (a twin's act, a predictor's prediction).

So a single intervention moves the act and the prediction together. The paper's slogan for this is that CDT "intervenes on the token," whereas A-FDT intervenes "on the *type*."

**Observations change the intervention point; they are not conditioned on.** This is the second difference from CDT that the paper emphasizes:

> "When CDT's observation history updates from $x$ to $y$, CDT changes from conditioning its model on $\textsc{Obs}=x$ to conditioning its model on $\textsc{Obs}=y$, whereas FDT changes from intervening on the variable $\textsc{fdt}(\underline P, \underline{G}, \underline x)$ to $\textsc{fdt}(\underline P, \underline{G}, \underline y)$ instead."

Equation (4) accordingly has no "$\textsc{Obs}=x$" on the right of the bar. The observation enters only through which node is intervened on. One minor inconsistency in the source: when the paper computes the transparent Newcomb case, it writes $\mathbb E(V \mid \mathrm{do}(\textsc{fdt}(\ldots,\textit{full})=a, \textsc{Obs}=\textit{full}))$. The calculation it then performs nonetheless does *not* condition on the box being full; it weighs worlds where the box is empty. So I read Equation (4), and that calculation, as unconditioned. That is the reading I use throughout.

**Relation to the other theories.** The paper notes that when every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$ (apart from its dependence on the $\textsc{fdt}$ node), the three expectations coincide:

$$
\mathbb E[V\mid a]=\mathbb E[V\mid \mathrm{do}(a)]=\mathbb E[V\mid \mathrm{do}(\textsc{fdt}=a)].
$$

A-FDT is therefore a conservative extension of ordinary decision-making. It diverges only when something other than the act's own effects (paradigmatically a predictor or a copy) tracks the agent's decision function.

## 4. Applying A-FDT: a recipe

Equation (4) can be read as a procedure. Steps 1–2 make explicit what the paper leaves to "defining $P$ and $G$"; steps 3–5 are Equation (4) itself.

1. **List the variables** relevant to the outcome: states of nature, other agents' predictions or acts, the agent's act, outcome, and utility $V$.
2. **Introduce decision nodes.** Add one node $\textsc{fdt}(\underline P,\underline G,\underline y)$ for each observation history $y$ the agent might be computing on. Draw an arrow from each node to every variable whose value is fixed by that computation's output: the agent's act (gated by which observation she actually receives), and any accurate model of her running on that input. Noise in a model enters as a separate parent such as $\textsc{Accurate}$.
3. **Assign priors** to all non-intervened root nodes, including the decision nodes for observations *other* than the actual $x$.
4. **For each $a\in\mathcal A$**, apply $\mathrm{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)$, propagate, and compute $\mathbb E[V]$.
5. **Output the argmax.**

## 5. Worked examples

### Newcomb's problem and the twin

The predictor is 99% accurate. Box B holds \$1,000,000 iff one-boxing was predicted, and box A holds \$1,000. In the agent's graph, the single node $\textsc{fdt}(\underline P,\underline G)$ feeds both $\textsc{Act}$ and $\textsc{Prediction}$, and $\textsc{Accurate}$ is a second parent of $\textsc{Prediction}$. Then:

$$
\mathbb E[V\mid \mathrm{do}(\textsc{fdt}=\textit{onebox})] = 0.99(1{,}000{,}000) = 990{,}000,
$$

$$
\mathbb E[V\mid \mathrm{do}(\textsc{fdt}=\textit{twobox})] = 0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000.
$$

A-FDT one-boxes. CDT's graph has no arrow from the decision to the prediction, so CDT holds $P(\textit{full})=p$ fixed and two-boxes for every $p$.

The psychological twin prisoner's dilemma has the same structure. The twin's act is a second child of the same node, so A-FDT compares (C,C), worth \$1,000,000, with (D,D), worth \$1,000, and cooperates.

### Smoking lesion

The lesion causes cancer and a taste for smoking, and nothing tracks the agent's decision function. The paper formalizes the lesion as fixing which of two utility functions, and hence which of two world-models $P_S$ or $P_R$, the agent runs. The act is then

$$
\textsc{Act}=\begin{cases}\textsc{fdt}(\underline{P_S},\underline G) & \text{if lesion},\\ \textsc{fdt}(\underline{P_R},\underline G) & \text{if no lesion.}\end{cases}
$$

Intervening on $\textsc{fdt}(\underline{P_S},\underline G)$ leaves $P(\textit{lesion})=p$ unchanged, because the lesion is upstream and $\textsc{Cancer}$ has no arrow from any decision node. Write $q$ for the agent's prior that the other node outputs *smoke*. The paper's two expected utilities are:

$$
\text{smoke: } p(10{,}000+1{,}000) + (1-p)(990{,}000+1{,}000q),
$$

$$
\text{refrain: } p(10{,}000) + (1-p)(990{,}000+1{,}000q).
$$

They differ by exactly $p\cdot\$1{,}000$, so A-FDT smokes. The general lesson is that *A-FDT's verdict is driven entirely by which arrows leave the decision node.* Newcomb and the smoking lesion share a probability distribution (Gibbard and Harper's renaming) but not a dependency graph.

### Transparent Newcomb (and Parfit's hitchhiker)

Both boxes are transparent, and B is filled iff the predictor expects the agent to one-box *upon seeing B full*. There are now two decision nodes, $\textsc{fdt}(\ldots,\textit{full})$ and $\textsc{fdt}(\ldots,\textit{empty})$. $\textsc{Prediction}$ depends on the first, and it also selects which node controls the act.

Seeing a full box, the agent intervenes on the *full* node. Let $q$ be her prior that she two-boxes on seeing empty. Then:

$$
\mathrm{do}(\textit{onebox}):\ 0.99(1{,}000{,}000) + 0.01\,q(1{,}000)= 990{,}000+10q,
$$

$$
\mathrm{do}(\textit{twobox}):\ 0.01(1{,}001{,}000)+0.99\,q(1{,}000)=10{,}010+990q.
$$

The paper prints the second line as "\$110,00 + $q\cdot$\$990", evidently a typo for \$10,010 + 990$q$. For any $q\in[0,1]$, one-boxing wins.

The striking feature is that the agent *sees* a full box, yet her two-boxing hypothetical is mostly a world where the box is empty. That is the consequence of not conditioning on $\textsc{Obs}$. Parfit's hitchhiker is the same structure, with paying the driver in the role of one-boxing.

### Blackmail

**XOR blackmail.** The letter is sent iff exactly one of these holds: no termites and the agent will pay, or termites and she will not. Intervening on $\textsc{fdt}(\ldots,\textit{letter})$ changes whether the letter is sent but not whether there are termites. Paying therefore just costs \$1,000, and A-FDT refuses. EDT pays, because conditioning on paying makes termites impossible.

**Mechanical blackmail.** The blackmailer runs the program (and the agent receives a letter) only if she predicts payment. Suppose she errs toward predicting payment with probability $\varepsilon$:

- **Pay:** the agent is always blackmailed and loses \$1,000.
- **Refuse:** the agent is blackmailed with probability $\varepsilon$ and then loses \$1,000,000, an expected loss of $10^6\varepsilon$.

So A-FDT refuses iff $\varepsilon<0.001$. The paper's example of $\varepsilon=0.0009$ (an expected loss of \$900) fits this threshold. Its claim that the agent pays when the error rate is "0.011%" does not, since that would give an expected loss of \$110. The intended figure is presumably 0.11%. Either way, the structure is clear: A-FDT weighs the counterfactual frequency of being blackmailed, not just the loss given the letter in hand.

## 6. What gets an arrow? Operationalizing subjunctive dependence

Everything hinges on $G$. The paper defines the relevant relation informally:

> "When two physical systems are computing the same function, we will say that their behaviors ``subjunctively depend'' upon that function."

It states the key normative constraint as follows:

> "The important assumption behind our proposed decision theory is that when an FDT agent imagines herself taking two different actions, she imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

Two further points come from the source:

- **Causal dependence is a special case.** Anything causally downstream of the act is downstream of the decision node.
- **Mere correlation does not suffice.** The pink-calculator example makes this point, as does the lesion.

The paper also admits that it does not know how to construct $G$ in general:

> "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

For working through unfamiliar cases, I propose the following rules of thumb. They are my own additions, not the paper's.

**(R1) The model test.** Draw an edge from $\textsc{fdt}(\underline P,\underline G,\underline y)$ to a variable $Z$ iff the mechanism producing $Z$ consults a computation that, when it functions correctly, returns that function's output on input $y$. Simulations, predictions, copies, and the agent's own body all qualify. Imperfection belongs in a separate noise parent, not in a missing edge.

**(R2) The counterfactual-output test.** Ask: "If this algorithm (counterpossibly) returned $a'$ on input $y$, would $Z$'s mechanism, operating as it actually operates, produce a different value?" If yes, draw the edge. The lesion fails this test. Newcomb's predictor passes it.

**(R3) Input specificity.** A predictor of "what she does on seeing B full" depends on the *full* node, not the *empty* node. Getting the input right is exactly what generates the transparent-Newcomb and blackmail verdicts.

**(R4) Partial similarity.** If another agent runs a *similar but not identical* algorithm, the paper's framework offers no exact rule. A reasonable approximation is to model that agent's output as a noisy child of the decision node, with the noise level reflecting one's credence that the two computations diverge on this input. This keeps Equation (4) intact while making the hard question an explicit modelling choice.

These rules do not dissolve the underlying philosophical problem. Equation (4) presupposes counterpossible reasoning: the algorithm's output on a given input is a logical fact, and the hypothetical with the other output is a logically impossible world. The paper sidesteps this by taking $G$ as given, just as CDT takes the causal graph as given. It also explicitly considers an "evidential" variant that would condition on logical facts, and leaves it undefined for lack of a theory of conditioning on false logical sentences.

## 7. Actions versus policies: where A-FDT is underdetermined

Footnote 7 of the paper says:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

The structural difference is easy to state.

- **A-FDT** intervenes on one node $\textsc{fdt}(\ldots,x)$ and holds the decision nodes for other inputs $y\neq x$ at their priors. These are the $q$'s above.
- **Policy-FDT** chooses a whole mapping $\pi:\mathcal X\to\mathcal A$, so all those nodes are set jointly.

In every example in the paper, the prior $q$ washes out. This is not guaranteed in general. Here is an illustration of my own:

> **Split copies.** The agent is duplicated. Copy 1 is shown *red*; copy 2 is shown *blue*. Each picks $A$ or $B$. If both pick $A$, each gets 100; if both pick $B$, each gets 60; otherwise 0.

Copy 1 intervenes on $\textsc{fdt}(\ldots,\textit{red})$ while holding $\textsc{fdt}(\ldots,\textit{blue})$ at its prior. Let $r$ be her prior probability that the blue node outputs $A$. Then

$$
\mathbb E[V\mid\mathrm{do}(A)]=100r,\qquad \mathbb E[V\mid\mathrm{do}(B)]=60(1-r),
$$

so A-FDT picks $B$ whenever $r<0.375$. If both copies hold such priors, both play $B$, and the prior is self-confirming: $(B,B)$ is a stable but inferior outcome. Policy-FDT compares the policy (red↦$A$, blue↦$A$), worth 100, against (red↦$B$, blue↦$B$), worth 60, and selects the first regardless of priors.

So A-FDT's recommendation can depend on the agent's beliefs about her *own* behaviour on other inputs. Equation (4) does not say where those beliefs come from. A natural repair is to require the priors on sibling decision nodes to be consistent fixed points: each node's prior should equal what A-FDT would output there. That narrows the answer to equilibria but does not select among them. Policy selection removes the indeterminacy. This, I take it, is the reason the authors prefer policies. For the single-observation and "predictor-gates-observation" problems that make up the paper's catalogue, the two variants agree.

## 8. Evaluation and open questions

The paper offers several arguments for the theory. These are its claims, which I only summarize.

- **Utility in "fair" problems.** A-FDT agents, as the source puts it, "achieve more utility in expectation" in problems where the outcome depends only on the agent's behaviour. The authors report that they cannot construct an intuitively fair dilemma where FDT loses, while admitting that "fairness" lacks a formal definition.
- **Acting as one would have precommitted.** A-FDT agents behave this way without needing binding devices, and the paper argues the theory is reflectively stable in fair problems.
- **A matching dominance principle.** "Dominance" is relative to a choice of hypotheticals. Under A-FDT's hypotheticals, the agent never takes a dominated action.
- **No instability.** In Death in Damascus, A-FDT simply stays and saves \$1,000, whereas CDT oscillates or must randomize.

The main open issues are:

1. **Constructing $G$.** No theory says how to learn subjunctive-dependence structure; rules like R1–R4 are heuristics.
2. **Counterpossibles.** The hypotheticals are logically impossible worlds, and no satisfactory semantics is supplied.
3. **Fairness.** The central performance claim is relative to an informal class of problems.
4. **Sibling-node priors.** A-FDT specifically inherits the indeterminacy shown in Section 7.

Equation (4) also leaves smaller details open, such as tie-breaking and how fine-grained the input $x$ should be (full history versus a summary). I would resolve these by convention: break ties arbitrarily, and use the full observation history as input, since a coarser summary could merge decision nodes that predictors distinguish.

## Conclusion

A-FDT is CDT with the surgery moved. Instead of setting the physical act, the agent sets the output of her own decision algorithm on her current input. Instead of conditioning on observations, she lets the observation choose which algorithmic node to set. Everything then propagates through a graph encoding all dependencies on that output, causal and subjunctive alike. With the right graph, one rule one-boxes in Newcomb's problem, smokes in the smoking lesion, cooperates with a twin, pays the driver in the desert, and refuses blackmail.

The work lies in building that graph. A reader can decide a new case by asking which mechanisms compute the agent's function on which inputs, drawing those edges, and maximizing. The answer is reliable to the extent that the graph is right and that beliefs about one's behaviour on other inputs do not matter. Where they do matter, A-FDT gives way to its policy-selecting sibling.

**Reference.** Yudkowsky, E. & Soares, N. "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060v2.