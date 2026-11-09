# A-FDT: Choosing the Output of Your Own Decision Function

## 1. What this essay covers, and the name

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* proposes a rule for choosing actions that differs from both causal decision theory (CDT) and evidential decision theory (EDT). Their abstract summarizes the idea: the agent should "treat one's decision as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'"

The paper's formal statement is its Equation (4), in Section 5. That equation intervenes on a variable whose value is an **action**. Footnotes 7 and 16 say the authors actually prefer a variant that chooses a **policy**, meaning a map from observations to actions. They set that variant aside because, in their words, "the difference only matters in multi-agent dilemmas so far as we can tell."

I call the Equation (4) theory **A-FDT** (action functional decision theory). For the footnoted policy variant I use my own label, **P-FDT** (policy-selection FDT). The other theories are CDT and EDT, as in the source. When the paper writes "FDT" and I am reporting its claims, those claims are about the Equation (4) formalism, so I attribute them to A-FDT.

Throughout, I mark which claims come from the source and which are my own interpretations or proposals.

## 2. The common frame: expected utility over hypotheticals

All three theories are expected-utility maximizers in the following sense (source, Eq. 1). The agent picks the action $a$ that maximizes

$$
\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),
$$

where $x$ is the agent's observation history and $\hookrightarrow$ is a "decision hypothetical" connective that is left unspecified.

Following Joyce, the paper treats the reading of $\hookrightarrow$ as the only free parameter. The theories then differ as follows:

- **EDT** reads $\hookrightarrow$ as conditioning: $\mathbb E(V\mid \text{Obs}=x,\text{Act}=a)$.
- **CDT** reads it as Pearl intervention on the physical act, given a causal graph $G$: $\mathbb E(V\mid do(\text{Act}=a),\text{Obs}=x)$.

The paper describes the procedure operationally. The agent holds a world-model $M$. For each action she builds a *hypothetical* $M^{a\hookrightarrow}$. The paper calls these "decision-theoretic instruments constructed from beliefs," not beliefs. She scores each hypothetical and takes the best action. A-FDT keeps this frame and changes two things: what the agent intervenes on, and how observations enter.

## 3. The definition

**Equation (4)** (source):

$$
\mathrm{FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\;\mathbb E\!\left(V \,\middle|\, do\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right).
$$

The ingredients are:

- **$P$**: a probability distribution over world variables. It includes *logical* variables that represent the outputs of mathematical functions. One such variable is $\textsc{fdt}(\underline P,\underline G,\underline x)$, the output of the A-FDT algorithm on the agent's own inputs. The underlines mean dequoting: the variable's *name* is built from the inputs.
- **$G$**: a graph that says how changing a logical variable affects other variables. CDT's graph encodes only causal structure. $G$ is meant to encode *subjunctive* dependence as well.
- **$do(\cdot)$**: Pearl's operator, reused unchanged. It sets the chosen node, recomputes its descendants in $G$, and leaves non-descendants at their prior distribution.
- **$V=\mathcal U(\text{Outcome})$**: the utility variable.

The paper identifies two differences from CDT's Equation (3):

1. **Point of intervention.** CDT intervenes on the physical act, the *token*. A-FDT intervenes on the function's output, the *type*. Everything that implements or reliably models that function moves together in the hypothetical.
2. **Role of observation.** CDT conditions on $\text{Obs}=x$. A-FDT does not. Instead, the observation selects *which node* is intervened on: $\textsc{fdt}(\underline P,\underline G,\underline x)$ rather than $\textsc{fdt}(\underline P,\underline G,\underline y)$.

The self-reference is benign, the paper argues. The agent needs a variable *representing* her output, not knowledge of its value, and Kleene's recursion theorem ("quining") shows such self-representing structures exist.

**A-FDT as an algorithm.** Read operationally:

1. Build $P$ and $G$. The graph should contain a node $F_x:=\textsc{fdt}(\underline P,\underline G,\underline x)$ for the current input. It should also contain nodes $F_y$ for any other inputs whose outputs matter to the outcome.
2. For each $a\in\mathcal A$, form $P(\cdot\mid do(F_x=a))$ and compute the expected value of $V$.
3. Output the maximizer.

Because $F_x$ is set by intervention, its prior probability does not matter. An agent who is nearly certain she will one-box can still evaluate two-boxing. The paper presents this as an advantage over EDT, where zero-probability actions cannot be conditioned on.

## 4. Subjunctive dependence: what goes into $G$

The paper's governing analogy is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

Two physical systems *subjunctively depend* on a function when both compute it. Examples are two calculators summing $6288+1048$, or an agent and a predictor's accurate model of her. The paper treats causal dependence as a special case: a scribe copying a calculator's output would have written something different had the output differed. Mere correlation does not count. Two coincidentally pink calculators do not subjunctively depend on each other.

The normative core is stated as an assumption about hypotheticals. When the agent imagines a different output, "she imagines corresponding changes in all and only those things that subjunctive depend on the output of her decision-making procedure."

The source is candid that it gives no procedure for building $G$: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." Equation (4) is therefore a function of a graph supplied from outside, exactly as CDT takes a causal graph as given.

**An operational rule (my proposal).** To use A-FDT on unfamiliar cases, I suggest drawing $G$ as follows.

- **(R1)** Add an edge $F_x\to Z$ if the mechanism producing $Z$ computes, simulates, or reasons accurately about the agent's decision procedure on input $x$. Model any unreliability as a separate exogenous noise node. The source's *Accurate* node in Newcomb's problem works this way.
- **(R2)** Treat the agent's own body as such a mechanism. Draw $F_x\to\text{Act}$, gated by whatever determines that $x$ is the input actually received.
- **(R3)** Add no edge from $F_x$ to variables that are merely statistically correlated with the act through common physical causes, such as lesions or genes. Those causes stay upstream and are held fixed.
- **(R4)** Give each relevant input $y\neq x$ its own root node $F_y$, with no edge between $F_x$ and $F_y$. This matches every graph in the paper, but it is a substantive choice; §7 discusses it.
- **(R5)** Treat another agent as computing the *same* node only if she runs the same function on an input that is isomorphic to the agent's own under relabeling. The paper's twin "reason[s] the same way," and I read that as this isomorphism condition. Strictly, the twin's model refers to *her*, so her literal input is different.

Rule R3 is what separates predictor-like correlations from lesion-like ones. In the paper's words, the predictor "builds an accurate model of the agent," whereas the lesion "is not evaluating the agent's future decisions."

## 5. Worked cases

All dollar figures stand in for utility. Most numbers below are the source's; the derivations and the general formulas are mine.

### 5.1 Newcomb's problem and the twin prisoner's dilemma

The graph has $F\to\text{Act}$ and $F\to\text{Prediction}$, with *Accurate* (probability 0.99) as noise on the prediction.

$$
\mathbb E[V\mid do(F=\text{one})]=0.99(10^6)=990{,}000,\qquad
\mathbb E[V\mid do(F=\text{two})]=0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000.
$$

A-FDT one-boxes. CDT intervenes on Act alone, holds $P(\text{full})=p$ fixed, and finds two-boxing better by $1{,}000$ for every $p$.

In the **twin prisoner's dilemma**, both twins' acts are children of the same node $F$ (rule R5). Setting $F$ to cooperate yields mutual cooperation and $10^6$. Setting it to defect yields $10^3$. A-FDT cooperates.

The paper stresses that no retrocausation is involved. The agent "does not think that a physical signal passes between her action and the predictor's prediction." She simply declines to imagine her function's output changing while a faithful model of that same function stays fixed.

### 5.2 Smoking lesion

Here $F\to\text{Act}$ only. *Lesion* is a common cause of Act and Cancer, and it is upstream of the intervention (rule R3).

The paper models the lesion as determining which utility function, and therefore which instance of the A-FDT node, controls the act. Write $p=P(\text{lesion})$. The intervention leaves $p$ unchanged, so the cancer terms are identical in the two hypotheticals. The source computes that smoking beats refraining by $p\cdot\$1{,}000$, so A-FDT smokes.

The paper then judges the dilemma "badly confused," because a correct formalization requires the agent to be uncertain about her own desires. It recommends retiring the case.

### 5.3 Transparent Newcomb: observations change the node, not the measure

Both boxes are visible, and box B is full. The predictor fills B iff it predicts one-boxing *upon seeing a full box*.

The graph has nodes $F_{\text{full}}$ and $F_{\text{empty}}$. *Prediction* depends on $F_{\text{full}}$, and *Prediction* also decides which node drives Act. Let $q$ be the prior probability that $F_{\text{empty}}$ takes the extra $1{,}000$. Evaluating Equation (4) without conditioning on Obs:

$$
\mathbb E[V\mid do(F_{\text{full}}=\text{one})]=0.99(10^6)+0.01(1{,}000q)=990{,}000+10q,
$$
$$
\mathbb E[V\mid do(F_{\text{full}}=\text{two})]=0.01(1{,}001{,}000)+0.99(1{,}000q)=10{,}010+990q.
$$

The paper prints the second constant as "\$110,00", which appears to be a typo for \$10,010.

The difference is $979{,}990-980q>0$ for every $q\in[0,1]$, so A-FDT one-boxes even while looking at the full box. In the paper's gloss, when she imagines two-boxing she "envisions a scenario where she instead (with high probability) sees that the box is empty."

**A source inconsistency.** The displayed objective in this subsection writes $\mathbb E(V\mid do(F_{\text{full}}=a,\ \text{Obs}=\text{full})$, with an unbalanced parenthesis. Read literally as conditioning on $\text{Obs}=\text{full}$, it would make one-boxing worth $10^6$ and two-boxing worth $1{,}001{,}000$, so A-FDT would two-box. The worked calculation instead sums over the empty-box world. The calculation agrees with Equation (4) as stated. It also agrees with the paper's warning that a theory which "prescribes both conditioning on evidence *and* changing the place where one intervenes" suffers a harmful "double update." I therefore treat Equation (4), with no conditioning, as authoritative.

The same structure is Parfit's hitchhiker, which the paper calls "precisely equivalent." There A-FDT pays the driver.

### 5.4 Blackmail

**XOR blackmail** (perfect predictor, termite prior $p$). A-FDT receives the letter and intervenes on $F_{\text{letter}}$. Infestation is upstream and stays fixed. Using the letter's rule, I compute:

$$
\text{pay: } -p(10^6)-(1-p)(10^3),\qquad \text{refuse: } -p(10^6).
$$

Refusing is better by $(1-p)\cdot 1{,}000$. The intervention changes *whether the letter arrives*, not whether there are termites. EDT pays here; CDT and A-FDT refuse, but for different reasons.

**Mechanical blackmail.** Now let the blackmailer mistakenly predict "pay" with probability $\varepsilon$. A refusing policy is then blackmailed with probability $\varepsilon$ and loses $10^6$; a paying policy is (essentially always) blackmailed and loses $10^3$. A-FDT therefore refuses iff

$$
\varepsilon\cdot 10^6<10^3, \quad\text{i.e.}\quad \varepsilon<10^{-3}.
$$

The paper's example $\varepsilon=0.0009$ falls below this threshold, so A-FDT refuses even while holding the letter and knowing the prediction was wrong. The paper says that at "0.011%" A-FDT pays. By the formula above, the threshold is $0.1\%$, so the printed figure must be intended as some rate above $0.1\%$. Both CDT and EDT pay, and so they invite blackmail.

### 5.5 Death in Damascus

Death predicts perfectly, so $F\to\text{Act}$ and $F\to\text{Death's location}$. Intervening on $F$ moves both together, so the agent dies in either case. Staying saves the \$1,000, and A-FDT stays.

The paper shows CDT oscillating instead. Each tentative choice makes the other look better, because CDT holds Death's location fixed. Ratified CDT then randomizes and refuses to pay \$1 for a truly random coin.

The following extension is mine, under rule R3. A genuinely random coin is not a child of $F$. So $do(F=\text{use coin})$ gives survival probability $\tfrac12$, worth about $500{,}000$, and A-FDT buys the coin. This matches the paper's verdict that declining the coin is "*wildly* irrational."

## 6. Dominance, control, and the "global perspective"

**Dominance.** The paper's reply to the dominance argument for two-boxing is that "every method for constructing hypotheticals gives rise to its own notion of dominance." CDT's dominance holds the predictor's prediction fixed while the act varies. That is like imagining a working calculator printing 3159 "holding constant the fact that $6288+1048=7336$."

Under FDT-style dominance, one holds the subjunctive dependencies fixed instead. Then A-FDT never takes a dominated action. So dominance cannot be a neutral tie-breaker between theories. The paper instead appeals to utility achieved in *fair* problems: those where outcomes depend only on the agent's behavior in the dilemma, not on which procedure produced it. It concedes that "fairness" lacks a formal definition.

**Control.** On whether one can "control" a logical fact, the paper argues parity. A deterministic CDT agent also has only one possible act, yet profits from imagining alternatives. Any principled objection to type-level control therefore applies equally to token-level control.

**Counterpossibles.** The genuine cost of the theory is that $do(F_x=a)$ is a *counterpossible* antecedent for every $a$ except one. The paper's proposed "true" operator for conditioning on logical sentences is admittedly undefined. Equation (4) sidesteps the problem by requiring $G$ as input.

## 7. Where Equation (4) underdetermines verdicts, and how to fix it

### 7.1 The sibling-node problem

Every example above contains other A-FDT nodes $F_y$ for $y\neq x$: the "empty box" node, the no-letter node, the other-preference node. Equation (4) leaves these at their *prior*. The source assigns them arbitrary values $q$ and remarks that the choice "doesn't matter." That remark is true of its examples, but it is not true in general.

**Formalization (mine).** Assume rule R4: the nodes $F_y$ are roots. Assume also that $V$ is a function of the joint assignment $\pi=(F_y)_{y\in X}$ and exogenous noise $U$. Define the policy value

$$
W(\pi)=\mathbb E_U\, V(\pi,U).
$$

Let $Q$ be the agent's prior over the other nodes $\pi_{-x}$. Then

$$
\text{A-FDT}(x)=\arg\max_a \;\mathbb E_{\pi_{-x}\sim Q}\,W(a,\pi_{-x}),\qquad
\text{P-FDT}=\arg\max_{\pi} W(\pi),\ \text{applied at }x.
$$

So A-FDT optimizes one coordinate of the policy against beliefs about the others, while P-FDT optimizes the whole policy jointly.

**Sufficient condition for agreement.** If the A-FDT argmax is the same for every $Q$, call the case *$Q$-robust*. In a $Q$-robust case, A-FDT's verdict is determinate. The transparent-Newcomb inequality above holds for all $q$, which is an instance of this. All of the paper's worked cases appear to be $Q$-robust.

**A case where they come apart (my construction).** An agent and an exact copy sit in a red room and a blue room. Each sees only its own room's color. Each picks ♣ or ♠. Both receive 10 if both pick ♣, 1 if both pick ♠, and 0 if they mismatch.

In the red room, with $r=Q(F_{\text{blue}}=♣)$, A-FDT compares $10r$ against $1-r$. It picks ♠ whenever $r<1/11$.

Now require the prior to be accurate, so that $Q$ is concentrated on what A-FDT actually outputs at the other input. Both $(♣,♣)$ and $(♠,♠)$ are then self-confirming fixed points. A-FDT, as defined, can rationally sit at the payoff-1 equilibrium. P-FDT picks $(♣,♣)$.

In general, any global maximizer of $W$ is an A-FDT fixed point, but the converse fails. A-FDT delivers only *coordinate-wise* optimality: each branch's output is optimal given the outputs of the other branches. This is presumably the "multi-agent" divergence that footnote 16 alludes to.

### 7.2 Proposed operational completion

To make A-FDT determinate in unfamiliar cases, I propose four conventions.

- **(C1) Reflective consistency.** The prior on each $F_y$ should equal A-FDT's actual output at $y$. This is a fixed-point requirement, satisfiable by the recursion-theorem construction the paper invokes.
- **(C2) Report indeterminacy.** When several consistent fixed points exist, state that Equation (4) does not settle the case. Selecting the $W$-maximal fixed point is permissible, but it is a P-FDT import and should be labeled as one.
- **(C3) Do not condition on Obs.** Observations only select the node, as discussed in §5.3.
- **(C4) Ties and randomization.** Break ties by a fixed ordering. Model mixing only through randomizers that are not children of $F$; otherwise a predictor of $F$ also predicts the "random" draw.

None of these conventions is in the source. They are the minimal additions I found necessary to turn Equation (4) into a total procedure.

### 7.3 Other open questions

- **R4 is a modeling choice.** Logically, $F_x$ and $F_y$ are the same function evaluated at different arguments, so a richer $G$ might link them. The paper's graphs do not.
- **Approximate implementations.** It is unclear how much similarity counts as "the same function" for imperfect copies. One natural extension is to treat partial similarity like the *Accurate* node: a noisy edge whose reliability is an empirical parameter.
- **Bounded agents.** The paper studies idealized maximization and expects bounded approximations to inherit the same qualitative strengths.

## 8. Conclusion

A-FDT, as given by Equation (4), is CDT's machinery with the point of surgery moved. The agent intervenes on the logical node $\textsc{fdt}(\underline P,\underline G,\underline x)$, the output of her own decision function on her actual input, rather than on her physical act. Observations select which node is intervened on rather than being conditioned on.

Given a graph that encodes subjunctive dependence, the theory has several consequences. It one-boxes, smokes, and cooperates with a twin. It pays in Parfit's desert and one-boxes in transparent Newcomb. It refuses both XOR and mechanical blackmail, as long as the blackmailer's error rate is below the critical value $10^{-3}$. It stays in Damascus.

The source openly leaves two things undetermined: how to construct the dependency graph, and how to make sense of counterpossible interventions. My analysis adds a third gap. Because Equation (4) holds sibling observation-nodes at their priors, A-FDT is only coordinate-wise optimal over policies, and it can be indeterminate in coordination problems. In those cases the policy-selection variant, P-FDT, gives sharper answers. With the operational rules R1–R5 and the conventions C1–C4, a reader can apply A-FDT to new cases and also tell when the theory, as written, does not yet fix a verdict.

## References

- Yudkowsky, E. & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060.
- Gibbard, A. & Harper, W. (1978). "Counterfactuals and Two Kinds of Expected Utility."
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*.
- Pearl, J. (2000). *Causality*.