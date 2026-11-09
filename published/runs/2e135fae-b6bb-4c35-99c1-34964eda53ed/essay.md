# A-FDT: Action Functional Decision Theory

*How to choose by intervening on the output of your own decision function*

## 1. What this essay covers

Yudkowsky and Soares's "Functional Decision Theory: A New Theory of Instrumental Rationality" offers one formal criterion, its Equation (4). That criterion picks a single **action** for the agent's current observation history. In footnotes, the authors say their "preferred formalization" picks *policies* instead. To keep the two apart, I call the action-selecting criterion of Equation (4) **A-FDT**. I call the policy-selecting variant **P-FDT**. The rival theories are **CDT** (causal decision theory) and **EDT** (evidential decision theory).

The abstract states the guiding idea. The agent should treat her decision as the output of a fixed mathematical function that asks: "Which output of this very function would yield the best outcome?" The rest of this essay turns that slogan into a procedure. It first states the formal ingredients, then works through examples, then marks where the source leaves the procedure underdetermined. Where I propose ways to fill those gaps, I flag them as my own.

## 2. Ingredients

### The common template

All three theories maximize expected utility. They share the template

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j).$$

Here $x$ is the observation history and $\hookrightarrow$ is a "decision hypothetical" connective. Following Joyce, the authors treat the meaning of $\hookrightarrow$ as the free parameter that separates the theories.

- **EDT** reads $\hookrightarrow$ as conditioning:
$$\mathrm{EDT}(P,x)=\arg\max_a \mathbb E(V\mid \textsc{Obs}=x,\textsc{Act}=a).$$
- **CDT**, in Pearl's framework, reads it as an intervention on the physical action node:
$$\mathrm{CDT}(P,G,x)=\arg\max_a \mathbb E(V\mid \mathtt{do}(\textsc{Act}=a),\textsc{Obs}=x).$$

### The world model for A-FDT

The agent's model is a pair $(P,G)$.

- $P$ is a probability distribution over variables. These include ordinary physical variables (box contents, a predictor's prediction, the agent's bodily act) and **logical variables** that stand for the outputs of mathematical functions.
- $G$ is a graph saying how changing a variable propagates to other variables.

The crucial logical variable is

$$F_x \;:=\; \textsc{fdt}(\underline P,\underline G,\underline x).$$

$F_x$ is a variable whose *name* encodes the agent's own model and observations, and whose *value* is whatever the A-FDT algorithm outputs on those inputs. The underlines mark dequotation.

The model therefore contains a representation of the algorithm that is currently using the model. The authors call this self-reference "harmless". The agent needs a variable that *represents* the output, not knowledge of what the output is. Kleene's recursion theorem ("quining") shows that such self-representing structures can be built.

For each other possible observation history $y \neq x$, the model may also contain a variable $F_y$. Each $F_y$ represents what the same algorithm would output had the agent observed $y$.

### What the graph encodes

$G$ is not purely causal. The source requires it to encode "the logical, mathematical, computational, causal, etc. structure of the world more broadly". Its edges represent **subjunctive dependence**: two physical systems that compute the same function both depend on that function. The authors' summary is:

> *Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*

Two contrasts mark the boundary of the notion:

- Causal dependence is a special case. A scribe copying a calculator's output depends on it in both senses.
- Mere statistical correlation is not subjunctive dependence. Two calculators that both happen to be pink do not depend on each other's colour.

## 3. The A-FDT criterion

Equation (4) of the source reads, in my notation:

$$\boxed{\;\text{A-FDT}(P,G,x) \;:=\; \arg\max_{a\in\mathcal A}\; \mathbb E\big(V \,\big|\, \mathtt{do}(F_x = a)\big)\;}$$

Read as a procedure, it says:

1. Locate the node $F_x$ that represents "the output of this very algorithm on my current inputs."
2. For each candidate action $a$, perform Pearl surgery. Cut $F_x$ off from its parents, set it to $a$, and recompute everything downstream of it in $G$. Leave everything not downstream at its prior distribution.
3. Compute the expected utility $V$ in each surgically modified model, which the paper calls the *hypothetical* for $a$.
4. Output the maximizing $a$.

Equation (4) differs from CDT's Equation (3) in two ways, and the authors name both.

**(i) The point of intervention.** CDT intervenes on the token: the physical act. A-FDT intervenes on the type: the logical output. Anything else downstream of $F_x$ moves with the agent's act in the hypothetical. That includes a twin's act, a predictor's prediction, or Death's appointment book.

**(ii) The treatment of observations.** The expectation in (4) is *not* conditioned on $\textsc{Obs}=x$. Observations enter only through *which node* gets intervened on. When the observation changes from $x$ to $y$, A-FDT switches from intervening on $F_x$ to intervening on $F_y$. The paper describes this as FDT responding to observation "by changing which node it intervenes upon."

The second difference is easy to misread, so it deserves care.

> **A note on the source's notation.** In the transparent Newcomb section the paper writes the objective as $\mathbb E(V\mid \mathtt{do}(F_{\textit{full}}=a,\ \textsc{Obs}=\textit{full})$. The parenthesis is unbalanced, and the display seems to include the observation. However, the calculation that follows explicitly sums over the branch in which box B is *empty*. That calculation is only coherent if the expectation is **not** conditioned on $\textsc{Obs}=\textit{full}$. I therefore follow Equation (4) as stated and read the transparent-Newcomb display as a typographical slip.

### When the theories agree

The paper notes when all three theories coincide. Suppose every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from $\textsc{Act}$'s own dependence on $F$. Then

$$\mathbb E[V\mid a] = \mathbb E[V\mid \mathtt{do}(a)] = \mathbb E[V\mid \mathtt{do}(F=a)].$$

The theories come apart only when something other than the agent's body also "computes" her decision function. Predictors, twins, simulations, and earlier or later copies of herself are all examples.

## 4. Worked examples

All utilities are in dollars.

### Twin prisoner's dilemma

The graph has $F \to \textsc{Act}_{\text{me}}$ and $F \to \textsc{Act}_{\text{twin}}$. A-FDT compares the two interventions:

- $\mathtt{do}(F=\textit{cooperate})$ sets both acts to cooperate, so $V=1{,}000{,}000$.
- $\mathtt{do}(F=\textit{defect})$ sets both acts to defect, so $V=1{,}000$.

A-FDT cooperates. CDT holds the twin's act fixed under its intervention, so defection dominates and CDT defects.

### Newcomb's problem (99% reliable predictor)

The graph has $F\to\textsc{Act}$ and $F\to\textsc{Prediction}\to\textsc{Box B}$. A noise node $\textsc{Accurate}$ also feeds into $\textsc{Prediction}$.

$$\mathbb E[V\mid\mathtt{do}(F=\text{one})]=0.99(1{,}000{,}000)=990{,}000,$$
$$\mathbb E[V\mid\mathtt{do}(F=\text{two})]=0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000.$$

A-FDT one-boxes. (The source's EDT passage gives \$999,000 for one-boxing. The correct figure is \$990,000, as its own A-FDT passage states. The conclusion is unaffected.)

Nothing in this calculation is retrocausal. The prediction moves in the hypothetical because the prediction and the act are two computations of the same function. The act does not reach back in time to change the prediction.

### Transparent Newcomb and Parfit's hitchhiker

Here observations matter. The agent's act is wired as follows:

- $\textsc{Act}=F_{\textit{full}}$ if $\textsc{Box B}=\textit{full}$;
- $\textsc{Act}=F_{\textit{empty}}$ otherwise.

The predictor fills the box iff it predicts that $F_{\textit{full}}=\text{one}$. Let $q$ be the agent's prior probability that $F_{\textit{empty}}$ two-boxes. Seeing a full box, A-FDT intervenes on $F_{\textit{full}}$:

$$\mathtt{do}(F_{\textit{full}}=\text{one}):\quad 0.99(1{,}000{,}000)+0.01\,q(1{,}000)=990{,}000+10q,$$
$$\mathtt{do}(F_{\textit{full}}=\text{two}):\quad 0.01(1{,}001{,}000)+0.99\,q(1{,}000)=10{,}010+990q.$$

(The source prints the second line as "\$110,00 + $q\cdot$\$990", a typo for $10{,}010+990q$.)

A-FDT leaves the \$1,000 behind even while looking at it. In the two-box hypothetical, the agent most likely would never have seen a full box at all.

Parfit's hitchhiker has the same form with the signs rearranged. Let dying be $-1{,}000{,}000$, rescue be $0$, and paying be $-1{,}000$. The driver is 99% accurate about $F_{\textit{city}}$.

$$\mathtt{do}(F_{\textit{city}}=\text{pay}):\quad 0.99(-1{,}000)+0.01(-1{,}000{,}000)=-10{,}990,$$
$$\mathtt{do}(F_{\textit{city}}=\text{refuse}):\quad -990{,}000.$$

A-FDT pays. The source stresses that these two problems are structurally identical. On its view, the intuition that pays the driver but two-boxes is a framing effect.

### Smoking lesion

This case shows what A-FDT does *not* do. The lesion is not a predictor and computes nothing about the agent's algorithm, so $G$ contains no edge from any $F$ to $\textsc{Cancer}$.

The paper's full formalization lets the lesion fix which utility function the agent has:

- with the lesion, $\mathcal U_S$, which values smoking;
- without the lesion, $\mathcal U_R$, which values smoking at $-1$.

There are correspondingly two nodes, $F_S$ and $F_R$, and $\textsc{Act}$ copies whichever one the lesion selects. Intervening on $F_S$ leaves $P(\textit{lesion})=p$ unchanged. Smoking therefore beats refraining by exactly $p\cdot 1{,}000$. A-FDT smokes, while EDT refrains.

The general lesson: correlations that are not mediated by a computation of the agent's function are cut by the surgery, just as in CDT.

### Mechanical blackmail and a threshold

A blackmailer runs a damaging program only if she predicts that the agent pays on receiving the letter. The damage is \$1,000,000, and paying costs \$1,000. Let $\epsilon$ be the probability that she wrongly predicts payment.

- $\mathtt{do}(F_{\textit{bm}}=\text{pay})$: the agent is always blackmailed and pays. Expected loss is \$1,000.
- $\mathtt{do}(F_{\textit{bm}}=\text{refuse})$: the agent is blackmailed only by error. Expected loss is $\epsilon\cdot 1{,}000{,}000$.

A-FDT refuses iff $\epsilon < 0.001$, so the indifference point is $\epsilon=0.1\%$. The source's example of $\epsilon=0.0009$, a 0.09% error rate, gives refusal, as the paper says. The paper then says the agent pays at "0.011%". By this arithmetic that is a slip: 0.011% is below the threshold and still yields refusal. Something like 0.11% would flip the decision.

### Death in Damascus

Death's book depends on $F$. Under either intervention Death is wherever the agent is, so survival is lost in both hypotheticals. Staying saves \$1,000, so A-FDT stays, stably and immediately.

CDT, by contrast, oscillates. Each time it settles on a belief about where it will go, the intervention holds Death's location fixed at that belief, which makes the other city look better.

## 5. Where the source stops: constructing $G$

Equation (4) is complete *given* $(P,G)$. The source is candid that it does not say how to obtain $G$:

> "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

The deeper ideal would be a $\mathtt{true}$ operator that updates on counterpossible logical sentences such as "this function outputs $a_2$" when it in fact outputs $a_1$. Using the graph and $\mathtt{do}$ is an explicit workaround for not having such an operator.

To decide unfamiliar cases, a reader therefore needs a working rule for drawing $G$. The following is **my proposal**, not the source's. It distils what the paper does in its examples.

**Provenance criterion.** Draw an edge $F_x \to Z$ iff the mechanism that produces $Z$ consults a computation, model, or simulation whose output on input $x$ is intended to track, or reliably tracks, the output of $\textsc{fdt}$ on $x$. Model imperfect tracking by adding a noise parent. The 99%-accurate node in Newcomb is an example: $Z = F_x$ with probability $\rho$, and otherwise $Z$ follows some fallback distribution.

Applying the criterion requires a few further rules:

1. **Bodily act.** $\textsc{Act}$ is a multiplexer. It equals $F_y$ where $y$ is the observation actually realized, so whatever determines $\textsc{Obs}$ must be a parent of $\textsc{Act}$. This is exactly how the source wires transparent Newcomb and both blackmail problems.

2. **Correlation without provenance.** If a correlation between $Z$ and the act exists only through common causes that do not compute the function, such as genes, lesions, or coincidences, draw no edge from $F$. Treat it as CDT would.

3. **Similar but distinct agents.** Edges to the decisions of other agents need a judgment of *how much* of their decision process is my function. A reasonable operationalization is a mixture: with probability $\sigma$, the other agent's output equals $F$; with probability $1-\sigma$, it is drawn independently. The source's voting and gym examples gesture at this, with "similar decisions" by nine fellow voters or by one's future selves. It gives no rule for $\sigma$, so any choice of $\sigma$ is an added assumption.

4. **A test question.** For each candidate variable $Z$, ask: "If, counterpossibly, this algorithm returned something else on this input, would $Z$ be different, holding fixed $Z$'s other inputs?" This is the subjunctive version of Pearl's interventionist question. The test is only as good as the agent's counterpossible judgment. The paper argues that humans handle such questions tolerably, for instance in noticing when they are being predicted, but it gives no algorithm.

The criterion inherits a known looseness. "Computing the same function" comes in degrees, and the source offers no metric. Two agents that run *slightly different* decision procedures might or might not share an $F$-node. A-FDT's verdicts in such cases are only as determinate as the modeller's choice.

## 6. Where the source stops: beliefs about one's other outputs

A second, subtler gap is specific to A-FDT as opposed to P-FDT. When the agent intervenes on $F_x$, the nodes $F_y$ for $y\ne x$ keep their *prior* distribution. In the transparent Newcomb and lesion cases, the source remarks that the correct values of $q$ are 0 or 1, but that "it won't matter" or "doesn't matter" if the agent is uncertain about them. That is true in those examples. It is not true in general.

### A counterexample (my construction)

A predictor flips a fair coin, which the agent then observes as $x_1$ or $x_2$. The predictor pays \$1,000,000 iff the agent's algorithm outputs $L$ on $x_1$ *and* $R$ on $x_2$. Each of those actions costs \$1; the alternatives are free. Let $r = P(F_{x_2}=R)$. On observing $x_1$, A-FDT compares:

$$\mathtt{do}(F_{x_1}=L): \;\; r\cdot 10^6 - 1, \qquad \mathtt{do}(F_{x_1}=\neg L):\;\; 0.$$

The verdict hinges on whether $r > 10^{-6}$. Two belief states are self-consistent:

- **Good fixed point.** The agent confidently expects herself to play $R$ on $x_2$. Each node then justifies the other, and she wins.
- **Bad fixed point.** The agent is certain she will not play $R$ on $x_2$. Then $L$ is not worth \$1, and symmetrically $R$ is not worth \$1 on $x_2$. That belief is borne out, and she earns nothing.

So A-FDT behaves like a team of separate "observation-selves" who each best-respond to beliefs about the others. Such a team can get stuck in a Pareto-inferior equilibrium. This mirrors, at the level of the agent's own function, the coordination worries the paper raises for groups of agents.

### Two ways to close the gap (my proposals)

1. **Adopt the paper's preferred formalization, P-FDT.** Footnote 7 says: "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions." P-FDT intervenes on the entire map $\pi:\mathcal X\to\mathcal A$ at once, choosing $\pi^*=\arg\max_\pi \mathbb E(V\mid\mathtt{do}(\textsc{fdt}(\underline P,\underline G)=\pi))$, and then plays $\pi^*(x)$. In the example above, P-FDT compares the joint policy $(L,R)$ with the alternatives and picks it at once. The paper says the difference "makes a difference in certain multi-agent dilemmas" but sets it aside. My example suggests that it can matter even for a single agent who faces a predictor whose payoff depends on several input–output pairs jointly.

2. **Keep A-FDT, but discipline the priors on $F_y$.** Require the agent's beliefs about $F_y$ to be a *best* self-consistent profile: the fixed point with the highest prior expected utility. With that refinement, A-FDT's output coincides with $\pi^*(x)$ whenever the optimal policy is a fixed point of the coordinate-wise best responses. That holds in every problem the paper analyses. Note that it is a coherence condition I am adding; Equation (4) does not supply it.

In the paper's own examples, the two formulations agree. The off-path nodes either do not affect $V$ or affect it in a way that does not reverse the comparison.

### Smaller gaps

Equation (4) is also silent on two further matters:

- **Ties.** It gives an $\arg\max$ set with no tie-breaking rule.
- **Mixed actions.** The paper's Death in Damascus discussion implies the agent can buy a "truly random coin" that a predictor cannot anticipate. That coin is naturally modelled as a variable *not* downstream of $F$, so A-FDT values it at its true 50% survival rate. A *pseudo*random coin is computed from the agent's state, so it belongs downstream of $F$ and buys nothing. This treatment is consistent with the source but is not spelled out there.

## 7. Philosophical motivation

### Type, not token

CDT asks what would happen if *this physical act* were different. A-FDT asks what would happen if *this function's output* were different. Both are hypotheticals about things that, in a deterministic world, could not actually be different.

The authors press this symmetry. Any objection that an FDT agent cannot "control" a logical fact applies equally to a deterministic CDT agent "controlling" her act. Hypotheticals in their sense are "decision-theoretic instruments constructed from beliefs". They are not claims about real possible worlds.

### Diagnosing the rivals

The authors place A-FDT between the two standard theories:

- **EDT** keeps too many correlations. It "manages the news", which is how it comes to pay in the XOR blackmail case and to refrain from smoking.
- **CDT** keeps too few. Its hypotheticals contain predictors that are known to be reliable yet "inexplicably falter exactly when Carl makes his current decision."
- **A-FDT** keeps exactly the correlations that run through the agent's function.

### Dominance is theory-relative

The causal dominance argument for two-boxing holds the prediction fixed while varying the act. That is CDT's own hypothetical, restated. Under A-FDT hypotheticals, two-boxing is the dominated option.

### Reflective stability and precommitment

A-FDT agents act as they would have precommitted to act. They have no motive to self-modify mid-problem, and they do not place negative value on information. Precommitment is the paper's argument; the final word belongs to utility: "Utility has primacy."

### Fairness

A dilemma can punish *any* theory by name. The authors restrict the comparison to "fair" problems: those in which outcomes depend only on the agent's *behaviour* in the dilemma, as Newcomb's do, rather than on the procedure that produced it. They report knowing no fair dilemma in which FDT loses to a rival. They also admit that "fair" has not yet been formalized.

## 8. Conclusion

A-FDT is CDT with the surgery moved. It applies Pearl's $\mathtt{do}$ operator to a logical node, the output of the agent's own algorithm on her current inputs. It handles observations by choosing *which* node to intervene on, not by conditioning. Given a graph that encodes subjunctive dependence, Equation (4) is a fully explicit procedure. It one-boxes, smokes, cooperates with twins, pays the driver, refuses blackmail below a computable error threshold (0.1% in the paper's numbers), and stays in Damascus.

Two things are left open. The first, acknowledged by the source, is how to construct $G$. I proposed a provenance criterion as a working rule. The second, implicit in choosing actions rather than policies, is how to set beliefs about one's outputs on other observations. My coordination example shows this can change verdicts, and either P-FDT or a best-fixed-point condition resolves it. Applied with these assumptions made explicit, A-FDT is a usable tool for unfamiliar cases. Keeping them explicit also marks the boundary between what the theory itself says and what its user has supplied.

**Reference.** E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060v2. Background cited there: Gibbard & Harper (1978); Joyce (1999); Pearl (2000).