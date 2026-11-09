# A-FDT: Action Functional Decision Theory, Read Through Equation (4)

## 1. What this essay is about

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* introduces a family of decision rules built around one idea: an agent should treat her choice as the output of a fixed mathematical function, and ask

> "Which output of this very function would yield the best outcome?"

The paper gives one formal statement of this rule, Equation (4) in Section 5. In that equation the agent intervenes on a node whose values are **actions**. Two footnotes (7 and 16) say that the authors' *preferred* formalization instead iterates over **policies**, meaning maps from observations to actions. I will call the action version defined by Equation (4) **A-FDT**. I will call the footnoted variant **policy-FDT** and mention it only where the contrast matters. The other theories that appear are causal decision theory (CDT) and evidential decision theory (EDT).

The plan is as follows:

- state A-FDT precisely;
- turn it into a procedure;
- work through the paper's main cases;
- identify the points where Equation (4) underdetermines what to do, and propose operational readings.

I flag my own proposals as such.

## 2. The common frame: expected utility with a free "if"

All three theories maximize

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}
$$

Here $a$ ranges over a finite action set $\mathcal A$, $x$ is the observation history, and $\hookrightarrow$ is the connective for "the hypothetical in which $a$ is executed." Following Joyce, the paper treats the interpretation of $\hookrightarrow$ as the only real point of disagreement:

> "decision theories should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated."

The two rival interpretations are:

$$
\text{EDT: } \arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a),
\qquad
\text{CDT: } \arg\max_a \mathbb E(V \mid do(\textsc{Act}=a), \textsc{Obs}=x).
$$

EDT conditions. CDT performs Pearl-style surgery on the physical action node, so only the descendants of $\textsc{Act}$ in a causal graph $G$ change.

## 3. The definition of A-FDT

**Inputs.** A-FDT takes:

- a probability distribution $P$;
- a graph $G$ encoding *subjunctive* dependence, which covers logical and computational dependence as well as causal dependence;
- an observation history $x$.

The model must contain a variable

$$
\textsc{fdt}(\underline P, \underline G, \underline x),
$$

which is the agent's representation of "what this very algorithm outputs on these inputs." The underline means dequoting: the variable's *name* is built from the agent's own model and observation. The paper points out that this self-reference is harmless. The agent needs only a variable that *represents* the output, not knowledge of its value, and Kleene's recursion theorem guarantees such self-representing structures exist.

**The rule (Equation 4).**

$$
\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; do\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big). \tag{4}
$$

The paper names two differences from CDT:

1. **Location of the surgery.** A-FDT intervenes on the logical node $\textsc{fdt}(\cdot)$, not on the physical $\textsc{Act}$. Every node that subjunctively depends on that output therefore varies together: the agent's body, a twin, a predictor's model.
2. **Treatment of observations.** In the authors' words, "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." Notice that Equation (4), as written, contains no "$\textsc{Obs}=x$" in the conditioning bar. The observation appears only in the name of the intervened node.

**Why a graph instead of a "true" operator.** The paper first writes an idealized rule, $\mathrm{FDT}^*$. It conditions on $\mathtt{true}(\textsc{fdt}(\underline P,\underline x)=a)$, a hypothetical operator that updates $P$ "to represent the scenario where $\phi$ is true." Because "it's not clear how to define a $\mathtt{true}$ operator," the paper instead requires $G$ to be *supplied*, "in the same way that the relevant causal structure is given as an input to CDT." Equation (4) is therefore relative to a dependence graph. A-FDT says what to do *given* correct subjunctive structure. It does not say how to learn that structure, which the authors call "perhaps the largest open problem in the study of functional decision theory."

**Subjunctive dependence.** The criterion the paper uses: two physical systems computing the same function both subjunctively depend on that function, much as two working calculators both output $7336$ for $6288+1048$. Causal dependence is a special case: a scribe copying a calculator's output depends on it in both senses. Mere correlation does not count. Two calculators that happen to be pink do not depend on each other's colour. The slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

## 4. A-FDT as a procedure

Here is my operationalization of Equation (4). The steps are implicit in the source's worked examples, but this decomposition is my own.

1. **Model the problem.** Write down chance nodes (noise, lesions, predictor accuracy), outcome and utility nodes, and the physical $\textsc{Act}$.
2. **Introduce algorithm nodes.** Add one node $F_y := \textsc{fdt}(\underline P,\underline G,\underline y)$ for each observation history $y$ the agent might be in, at least for every $y$ on which something in the problem depends.
3. **Draw subjunctive edges.** Draw an edge from $F_y$ to:
   - $\textsc{Act}$, routed by whichever observation actually occurs;
   - every predictor, twin, or simulator that computes or models the algorithm on input $y$.

   Lesions, coincidences, and other merely statistical correlates get no such edge.
4. **Assign priors to the non-intervened nodes.** For every $F_{y}$ with $y\neq x$, supply a prior over its value. The paper's examples call these probabilities $q$.
5. **Evaluate.** For each $a\in\mathcal A$, compute $\mathbb E[V\mid do(F_x=a)]$ by setting $F_x=a$ and propagating forward through $G$. Do not condition on $\textsc{Obs}=x$.
6. **Act** on the argmax.

Step 5 matters most for observations. In the paper's transparent-Newcomb calculation the agent who sees a full box still assigns weight to worlds where the box is empty, which are worlds in which $F_{\text{full}}$ does not control her body. This is the sense in which the theory is (in the language of its precursor, UDT) "updateless": the observation selects the intervention point but does not prune the distribution.

There is one notational wrinkle. The paper's displayed transparent-Newcomb expression writes $do(\ldots, \textsc{Obs}=\textit{full})$ inside the conditioning. Yet the computation that follows does not condition on the box being full; it integrates over $\textsc{Accurate}$, including the empty-box branch. I therefore treat the computation, which agrees with Equation (4), as authoritative, and the inline $\textsc{Obs}$ as notational residue.

## 5. Worked cases

Utilities are in dollars, as in the paper.

### 5.1 Twin prisoner's dilemma

Both twins run the same function, so a single node $F$ feeds both $\textsc{Act}_{\text{me}}$ and $\textsc{Act}_{\text{twin}}$. The two hypotheticals are:

- $do(F=C)$: both cooperate, giving $1{,}000{,}000$;
- $do(F=D)$: both defect, giving $1{,}000$.

A-FDT cooperates. CDT holds the twin's act fixed under surgery on its own token action, so it defects by dominance.

### 5.2 Newcomb's problem (99% accurate predictor)

The graph is $F \to \textsc{Act}$ and $F \to \textsc{Prediction} \leftarrow \textsc{Accurate}$, with $\textsc{Prediction}\to\textsc{Box B}$.

$$
\mathbb E[V\mid do(F=\text{one})] = 0.99\cdot 10^6 = 990{,}000,
$$

$$
\mathbb E[V\mid do(F=\text{two})] = 0.01\cdot 1{,}001{,}000 + 0.99\cdot 1{,}000 = 11{,}000.
$$

A-FDT one-boxes. Two remarks:

- The agent's prior on her own output is irrelevant, because the intervention overrides it. EDT, by contrast, is "at the mercy of her priors."
- The paper's EDT calculation prints $\$999{,}000$. That is a typo for $990{,}000$, since EDT's conditional expectation here equals A-FDT's interventional one.

There is a standard objection. If the agent is nearly certain she one-boxes and so believes the box is full, why not take both? The paper answers that the counterfactual "I two-box" is evaluated as "the algorithm outputs *two*." In that counterpossible world the predictor, who models the algorithm, predicted *two*. Nothing travels backward in time. The decision-relevant world is chosen by varying the *type* rather than the *token*.

### 5.3 Smoking lesion

Here the graph differs in structure, not just in labels. $\textsc{Lesion}$ causes both $\textsc{Cancer}$ and the agent's *utility function*: $\mathcal U_S$ values smoking at $+1{,}000$, and $\mathcal U_R$ values it at $-1$. So there are two possible algorithm nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ and $\textsc{fdt}(\underline{P_R},\underline G)$. The lesion selects which one drives $\textsc{Act}$. No algorithm node has an edge into $\textsc{Cancer}$.

Let $p = P(\text{lesion})$, and let $q$ be the prior that the $R$-algorithm smokes. Intervening on the $S$-node leaves $p$ untouched, and smoking beats refraining by exactly $p\cdot 1{,}000$. So A-FDT smokes.

The general lesson for applying the theory is that a correlation flowing through a *common physical cause*, rather than through a computation of the agent's function, earns no subjunctive edge.

### 5.4 Transparent Newcomb (box seen full)

The agent intervenes on $F_{\text{full}}$. $\textsc{Prediction}$ depends on $F_{\text{full}}$, because the predictor predicts behaviour upon seeing a full box. The prediction then determines which observation occurs and so which node drives $\textsc{Act}$. Let $q$ be the prior that $F_{\text{empty}}$ two-boxes.

$$
\mathbb E[V\mid do(F_{\text{full}}=\text{one})] = 990{,}000 + 0.01q\cdot 1{,}000,
$$

$$
\mathbb E[V\mid do(F_{\text{full}}=\text{two})] = 0.01\cdot1{,}001{,}000 + 0.99q\cdot1{,}000 = 10{,}010+990q.
$$

The paper's "\$110,00" is a typo for $10{,}010$. A-FDT leaves the \$1,000 even while looking at it. The paper notes this is structurally identical to paying the driver in **Parfit's hitchhiker**: a million-dollar benefit is granted iff the agent is predicted to pay a thousand after receiving it.

### 5.5 XOR blackmail

A letter arrives iff exactly one of the following holds:

- there are no termites and the agent will pay;
- there are termites and she won't pay.

Under $do(F_{\text{letter}}=a)$, the choice changes whether the letter is sent but not the infestation probability $p$. Paying converts the termite-free world into a letter-receiving world at a cost of \$1,000, and the termite world loses \$1,000,000 regardless. A-FDT refuses, and so does CDT, though for a different reason. EDT pays, because conditional on paying the letter implies no termites.

### 5.6 Mechanical blackmail with predictor error $\varepsilon$

The blackmailer runs the program iff she predicts payment, and errs with probability $\varepsilon$. Compare the two hypotheticals:

- $do(F_{\text{bm}}=\text{pay})$: blackmailed always, so the expected loss is \$1,000.
- $do(F_{\text{bm}}=\text{refuse})$: blackmailed only by error, so the expected loss is $\varepsilon\cdot 10^6$.

A-FDT therefore refuses iff $\varepsilon < 10^{-3}$. The paper's examples fall on either side of this threshold. At $0.0009$, "0.09% of the time … loses \$900 in expectation," so she refuses. At its "0.011%" case, she pays. That second figure looks like a misprint for $0.0011$, since the stated verdict only follows above $10^{-3}$. The threshold is my own summary, but it follows directly from the equation.

### 5.7 Death in Damascus

Death's appointment book is written from a perfect prediction of the algorithm, so $F\to\textsc{DeathLocation}$ as well as $F\to\textsc{Act}$. Both hypotheticals contain death, and staying saves \$1,000, so A-FDT stays. There is no deliberational instability of the kind that makes CDT oscillate, or mix 50.05%/49.95% under Joyce's ratification. A-FDT would also buy a truly random coin, which Death cannot predict, for \$1. That coin node is *not* a child of $F$, so it gives an honest 50% chance at a million.

## 6. How A-FDT relates to its rivals

**Agreement condition.** The paper claims all three theories coincide on models where every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$. In that case

$$
\mathbb E[V\mid a]=\mathbb E[V\mid do(a)]=\mathbb E[V\mid do(\textsc{fdt}=a)].
$$

They diverge only when something other than the action's physical effects tracks the action, as with predictors, copies, or simulators.

**Too many vs. too few correlations.** The diagnosis is that EDT's hypotheticals keep too many correlations, so it pays the XOR blackmailer and fears cosmic rays. CDT's hypotheticals keep too few: they imagine a known-perfect predictor "inexplicably faltering" exactly at the moment of choice. A-FDT keeps exactly the subjunctive ones.

**Dominance.** The paper argues that every way of constructing hypotheticals induces its own dominance notion. Two-boxing dominates only under CDT-style counterfactuals. Under A-FDT-style counterfactuals, which hold the predictor–agent dependency fixed, one-boxing dominates. Dominance therefore cannot adjudicate between the theories, and the authors fall back on utility actually achieved in **fair** problems. They define these informally as problems where outcomes depend only on the agent's behaviour, not on her decision procedure as such. They admit the notion lacks a formal definition (footnote 15).

**Reflective stability.** The paper claims A-FDT agents act as they would have precommitted to act, so they have no reason to self-modify. It also claims they assign non-negative value to information. These are claims about the paper's cases, not theorems proved in it.

## 7. What Equation (4) leaves open, and how to fill it

### 7.1 Where $G$ comes from

This is the central gap, and the source says so plainly. My working heuristic for applying A-FDT is the following, and it is my proposal, not the paper's. Draw an edge from $F_y$ to a node $Z$ when $Z$'s value is produced by a process that evaluates, simulates, or reliably reasons about the agent's decision function on input $y$, or about a function the agent knows to be equivalent to it. Do not draw such an edge when the correlation runs through a shared physical cause of the agent's preferences or circumstances.

This reproduces every verdict in the paper. It leaves genuinely hard intermediate cases undetermined, such as an agent who is only *similar* to the predictor's model or uses a slightly different algorithm. For those cases I suggest a mixture model: let the other system's output equal $F$'s output with probability $\rho$ and be independent otherwise. The resulting expected utility then interpolates between A-FDT's and CDT's verdicts as $\rho$ falls from 1 to 0. The paper does not discuss partial dependence beyond noting that interdependence is "weakened, but not eliminated" when predictions are imperfect. It models that through noise nodes like $\textsc{Accurate}$, not through partial edges. My $\rho$-model is a natural extension of the same idea.

### 7.2 Which observation nodes to include

Equation (4) intervenes on one node, but the examples need nodes for counterfactual observations ($F_{\text{empty}}$, $F_\emptyset$). The paper does not say how many to include. Operationally, include $F_y$ for every observation $y$ that the problem's structure can route the agent into under some hypothetical. Omitting one silently conditions on $\textsc{Obs}=x$, which would collapse A-FDT back toward CDT on transparent problems.

### 7.3 Priors on the other nodes, and the action/policy gap

A-FDT treats $F_y$ for $y\neq x$ as ordinary chance nodes with priors ($q$ above). In the paper's examples $q$ "doesn't matter." That is not true in general, and here A-FDT and policy-FDT can come apart. The paper says the difference "will not make a difference in this paper" and matters mainly in "certain multi-agent dilemmas"; it gives no example.

Here is a toy case of my own construction, not from the paper. A predictor pays \$10 iff it predicts the agent will do $X$ on input 1 *and* $Y$ on input 2. Otherwise it pays \$0. Alternatively, it pays \$6 for the pair $(X', Y')$. The agent then sees input 1.

- **A-FDT** intervenes only on $F_1$, so its verdict depends on its prior over $F_2$. If it thinks $F_2=Y'$ is likely, it picks $X'$. A version of itself at input 2 with symmetric beliefs may pick the complementary option, and the pair can miscoordinate.
- **Policy-FDT** chooses the whole map $\{1\mapsto X,\, 2\mapsto Y\}$ at once and gets \$10.

A reasonable operational fix within A-FDT is to require the priors on the other $F_y$ to be the agent's best prediction of what A-FDT itself outputs at $y$, which is a fixed-point condition. Even then, multiple equilibria can survive, and the fixed point need not select the best one. This is exactly what policy selection repairs. So when you apply A-FDT, check whether the payoff depends on the *joint* behaviour across observations. If it does, flag that A-FDT's answer is prior-sensitive. If it does not, which covers every case in Section 5, A-FDT and policy-FDT agree.

### 7.4 Ties and zero-probability actions

Equation (4) is an argmax and says nothing about ties. Unlike EDT, it needs no exclusion of probability-zero actions, because $do$ is defined regardless of the prior on $F_x$. That is a genuine advantage. Its value does depend on the graph-surgery being well-defined, which Pearl's semantics guarantees for acyclic $G$. Cycles, such as two agents each simulating the other, are not addressed. I would handle them by treating the agents' shared function as a single node, as in the twin case, when their algorithms are identical. When they are not identical, the source gives no guidance.

### 7.5 Counterpossibles

Underneath the graph lies a philosophical cost. The antecedent "$\textsc{fdt}(\ldots)=a$" is false for every $a$ but one, and false as a matter of logic. The paper argues that this difficulty is "technical rather than philosophical." It also argues that deterministic CDT faces a parallel problem in making sense of "controlling" a token action that physics fixes. The graph-based Equation (4) sidesteps the problem by stipulation, and its verdicts are only as good as the stipulated $G$.

## 8. A short checklist for unfamiliar cases

1. Identify every process that computes or predicts your decision function, and on which inputs.
2. Build $G$ with algorithm nodes $F_y$, edges to those processes and to your body, and no edges to common-cause correlates.
3. Do not condition on what you observe. Intervene on $F_x$ and propagate.
4. If the payoffs depend on your joint behaviour across inputs, note that A-FDT is sensitive to the priors on the non-intervened $F_y$, and compare with the policy-level answer.
5. Ask whether the problem is "fair," meaning whether it rewards actions rather than the procedure that produced them. The paper's optimality claims extend only to fair problems.

## 9. Conclusion

A-FDT, as given by Equation (4), is CDT's interventionist machinery with two changes: the point of intervention moves from the physical act to the logical output of the agent's own algorithm, and observations change which output-node is manipulated instead of being conditioned on. With a correct subjunctive-dependence graph, this single rule:

- cooperates with twins;
- one-boxes in both opaque and transparent Newcomb problems;
- smokes in the lesion case;
- pays Parfit's driver;
- refuses both kinds of blackmail below the relevant error threshold;
- spends its last night in Damascus.

The source is candid that the hard parts sit outside the equation. One is building $G$, which requires an account of logical counterfactuals. Another is defining "fair" problems. A third, which I have emphasised, is the gap between action-level and policy-level intervention. A-FDT gives a precise, usable procedure relative to a dependence model. Its remaining indeterminacies can be located: they lie in where the model comes from and in how to price one's own behaviour at observations one is not currently facing.

**Reference.** E. Yudkowsky and N. Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060.