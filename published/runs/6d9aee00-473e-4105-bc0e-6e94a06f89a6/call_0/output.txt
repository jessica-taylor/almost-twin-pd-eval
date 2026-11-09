# A-FDT: Action Functional Decision Theory, Explained and Operationalized

## 1. What this essay is about

Yudkowsky and Soares (2017) propose a decision theory they call *functional decision theory*. Their core instruction is to treat one's decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" Their primary formal statement is Equation (4) of their Section 5. That equation chooses an **action**. Two footnotes (7 and 16) add that "in the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions."

To keep these two versions apart, I use the following names:

- **A-FDT** (action functional decision theory) is the rule of Equation (4), which picks an action given the current observation. It is the subject of this essay.
- **P-FDT** is the policy-selecting variant mentioned in the footnotes.
- **EDT** is evidential decision theory, and **CDT** is causal decision theory.

When I quote the paper, its label "FDT" is reproduced faithfully. In the paper's formal sections that label refers to what I am calling A-FDT.

Throughout, I mark which claims come from the source and which are my own interpretations or proposals.

## 2. The common skeleton: expected utility with a free "hypothetical" connective

All three theories in the paper are expected-utility theories. Following Gibbard and Harper, the source writes

$$
\mathcal{EU}(a) := \sum_j P(a \hookrightarrow o_j;\, x)\cdot \mathcal U(o_j), \tag{1}
$$

where $x$ is the observation history and $P(a \hookrightarrow o_j; x)$ is "the probability that $o_j$ will obtain in the hypothetical scenario where the action $a$ is executed after receiving observations $x$."

The source invokes Joyce's representation theorem. On that view, the theories share an account of value and differ only in how they read the connective $\hookrightarrow$. Joyce's phrase for this is that they disagree "about the epistemic perspective from which actions are to be evaluated."

Operationally, the source describes an agent who holds a world-model $M$ and, for each candidate action $a$, builds a *hypothetical* $M^{a\hookrightarrow}$. Hypotheticals are "decision-theoretic instruments constructed from beliefs," not beliefs. They are comparable to "notes on scratch paper." The agent then takes the action whose hypothetical has the highest expected value of $V := \mathcal U(\textsc{Outcome})$.

The three theories differ in how they construct hypotheticals:

$$
\text{EDT}(P,x) = \arg\max_a \mathbb E(V \mid \textsc{Obs}=x,\ \textsc{Act}=a) \tag{2}
$$

$$
\text{CDT}(P,G,x) = \arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a),\ \textsc{Obs}=x) \tag{3}
$$

EDT conditions on the action. CDT performs Pearl's $\mathtt{do}$-surgery on the physical action node in a causal graph $G$. This surgery cuts the action from its parents and propagates the change only downstream.

## 3. The A-FDT rule

Equation (4), the primary definition, reads

$$
\boxed{\ \text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big)\ } \tag{4}
$$

Each ingredient deserves comment.

**The node $\textsc{fdt}(\underline P,\underline G,\underline x)$.** The model $P$ is required to contain variables standing for outputs of mathematical functions. Among them is a variable whose *name* is "the output of the A-FDT algorithm on inputs $(P,G,x)$." The underlines denote dequoting: the node name is built from the agent's actual model and observation.

This is self-referential. The source argues that the self-reference is harmless because one need not know a variable's *value* to represent it. It cites Kleene's second recursion theorem ("quining") to show that such self-representing structures exist.

**The graph $G$.** In A-FDT, $G$ is not just a causal graph. It is a graph of *subjunctive dependence*, which tells "how changing a logical variable affects all other variables." The source says plainly that $G$ is an input: "we require that the relevant logical dependency structure be given as an input to FDT, in the same way that the relevant causal structure is given as an input to CDT."

**The operator.** Pearl's $\mathtt{do}$ is reused. Ideally one would have a $\mathtt{true}(\phi)$ operator that updates on a possibly false logical sentence. The source's view is that "it's not clear how to define a $\mathtt{true}$ operator. Fortunately, we don't have to." The graph $G$ stands in for it.

**Where the observation goes.** Note what is absent from Equation (4): there is no conditioning on $\textsc{Obs}=x$. The source identifies two differences from CDT:

1. A-FDT intervenes on the function-output node rather than on $\textsc{Act}$.
2. "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon."

This second point is the hinge of the theory's most distinctive verdicts.

**Agreement with rivals.** When every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$ (apart from its dependence on the function node), the source notes that

$$
\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)].
$$

In that case all three theories agree. They come apart only when something else in the world tracks the agent's decision procedure, as predictors and twins do.

## 4. Subjunctive dependence: what $G$ must encode

The basic concept is that "when two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." The source's touchstone is two calculators computing $6288+1048$. Neither causes the other's output, yet if the sum were (counterpossibly) different, both displays would differ. The source makes three further points:

- Causal dependence is a special case of subjunctive dependence. A scribe copying a calculator's output depends on it in both senses.
- Mere statistical correlation is not subjunctive dependence. Two calculators that happen to be pink is the example.
- The slogan: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." CDT "intervenes on the token," and FDT "on the *type*."

The source commits to a single criterion for good hypotheticals. When the agent imagines different outputs, she "imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

**An operational heuristic (my proposal).** The paper offers no algorithm for building $G$. To decide unfamiliar cases, I suggest drawing an edge from $\textsc{fdt}(\underline P,\underline G,\underline x)$ to a variable $Z$ when, and only when, one of the following holds:

1. **Self-implementation.** $Z$ is the agent's physical action in circumstances where her body actually runs the procedure on input $x$.
2. **Modelling.** $Z$ is computed by some process (a predictor, a simulation, a blackmailer's forecast) that evaluates or accurately models this very function *on this very input*. The model's imperfection goes in as an independent noise parent, like $\textsc{Accurate}$ in the source's Newcomb graph.
3. **Replication.** $Z$ is the output of another system running the same function on the same input, such as a twin.

Variables correlated with the action only through a shared physical cause (a lesion, a gene, an upbringing), and not through evaluating the function, get no edge. Causal descendants of edged variables are then updated as usual.

Every example below is consistent with this heuristic. It nonetheless goes beyond what the paper says, and Section 7 lists cases where it is underdetermined.

## 5. Worked examples

All figures are in dollars of utility, as in the source.

### Twin Prisoner's Dilemma

Both twins run the same function on the same input, so both actions are children of the one $\textsc{fdt}$ node:

- $\mathtt{do}(\textsc{fdt}=\textit{cooperate})$ gives both players $\$1{,}000{,}000$.
- $\mathtt{do}(\textsc{fdt}=\textit{defect})$ gives both players $\$1{,}000$.

A-FDT cooperates. EDT also cooperates, but for the evidential reason that cooperation is good news. CDT defects.

### Newcomb's Problem (99% accurate predictor)

In the source's graph $G^F$, the node $\textsc{fdt}(\underline P,\underline G)$ is a parent of both $\textsc{Act}$ and $\textsc{Prediction}$, and $\textsc{Accurate}$ is an independent noise parent of $\textsc{Prediction}$.

$$
\begin{aligned}
\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=\textit{onebox})] &= 0.99(1{,}000{,}000)+0.01(0) = 990{,}000,\\
\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=\textit{twobox})] &= 0.01(1{,}001{,}000)+0.99(1{,}000) = 11{,}000.
\end{aligned}
$$

A-FDT one-boxes. (The source's EDT paragraph states \$999,000 for one-boxing. That appears to be a typo for \$990,000, and it does not affect any verdict.)

A-FDT does not two-box "on reflection" even when it is confident the box is full. Its hypotheticals vary the *function's* output, and "for her to two-box, the FDT algorithm would have to output *twobox*," in which case the predictor would have predicted accordingly. No retrocausation is involved. The source notes Fiona "does not think that a physical signal passes between her action and the predictor's prediction."

### Smoking Lesion

The lesion causes cancer, and it also determines which preferences, and hence which instance of the function, controls the act. It does not evaluate the function. So the $\textsc{fdt}$ node has no edge to $\textsc{Cancer}$.

The source formalizes the problem as two utility functions, $\mathcal U_S$ (likes smoking) and $\mathcal U_R$ (does not). There are correspondingly two function nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ and $\textsc{fdt}(\underline{P_R},\underline G)$, and $\textsc{Lesion}$ selects which one drives $\textsc{Act}$. Intervening on $\textsc{fdt}(\underline{P_S},\underline G)$ leaves $P(\textit{lesion})=p$ untouched, so smoking beats refraining by $p\cdot 1{,}000$.

A-FDT smokes. A single rule therefore one-boxes and smokes, which the paper says Gibbard and Harper had argued was impossible for a rational agent to do consistently.

### Transparent Newcomb: observation as a choice of node

This is the example where the observation mechanics matter most. The agent sees that box B is full. In the source's graph $G^F$:

- the two nodes $\textsc{fdt}(\ldots,\textit{full})$ and $\textsc{fdt}(\ldots,\textit{empty})$ are both parents of $\textsc{Act}$;
- $\textsc{Prediction}$ determines which of them controls $\textsc{Act}$;
- $\textsc{Prediction}$ itself depends on $\textsc{fdt}(\ldots,\textit{full})$ through the predictor's model, together with noise.

Having seen *full*, A-FDT intervenes on $\textsc{fdt}(\ldots,\textit{full})$. Let $q$ be the prior that the *empty*-node outputs *twobox*.

$$
\begin{aligned}
\text{onebox:}\quad & 0.99(1{,}000{,}000) + 0.01\,(1{,}000q) = 990{,}000+10q,\\
\text{twobox:}\quad & 0.01(1{,}001{,}000) + 0.99\,(1{,}000q) = 10{,}010+990q.
\end{aligned}
$$

A-FDT one-boxes for every $q\in[0,1]$. (The source prints the second line as "\$110,00 + q·\$990"; the intended figure is \$10,010.) While looking at a full box, the agent's twobox hypothetical places most of its weight on worlds where the box is *empty*.

There is a notational wrinkle here. The source writes the objective for this case as $\mathbb E(V\mid \mathtt{do}(\textsc{fdt}(\ldots,\textit{full})=a, \textsc{Obs}=\textit{full})$, which has an unbalanced parenthesis and contains an $\textsc{Obs}$ term. If $\textsc{Obs}=\textit{full}$ were conditioned on, the worlds with an empty box would vanish and the calculation would collapse to EDT's two-boxing verdict. The source's actual computation keeps those worlds, and Equation (4) contains no conditioning. I therefore read Equation (4) as authoritative: observations select the intervention node and are never conditioned on.

The source supports this reading with a remark on Timeless Decision Theory. That earlier theory "prescribes both conditioning on evidence *and* changing the place where one intervenes; this creates a kind of 'double update' which proves harmful in practice."

The source treats Parfit's hitchhiker as "precisely equivalent" to this case, so A-FDT pays the driver.

### XOR Blackmail (perfect predictor, prior $p$ of termites)

The letter is sent iff exactly one of these holds: (no termites and the agent would pay) or (termites and the agent would not pay). Intervening on $\textsc{fdt}(\ldots,\textit{letter})$:

$$
\begin{aligned}
\text{pay:}\quad & -1{,}000{,}000\,p - 1{,}000(1-p),\\
\text{refuse:}\quad & -1{,}000{,}000\,p.
\end{aligned}
$$

A-FDT refuses, because the intervention changes whether the letter arrives but not whether there are termites. EDT pays. CDT refuses for a different reason: in CDT's hypothetical the letter still arrives and the predictor "erred."

### Mechanical Blackmail (error rate $\varepsilon$)

The blackmailer runs the program iff she predicts the agent would pay upon receiving the letter, and she errs toward "will pay" with probability $\varepsilon$.

- Paying means being blackmailed almost surely and losing \$1,000.
- Refusing means being blackmailed only with probability $\varepsilon$ and losing $\varepsilon\cdot 1{,}000{,}000$ in expectation.

The threshold is therefore $\varepsilon^\ast = 0.1\%$.

The source's $\varepsilon = 0.09\%$ yields an expected loss of \$900 from refusing, so A-FDT refuses, as the source says. The source also says Fiona pays at "0.011%." That gives an expected loss of only \$110, so by its own arithmetic she should still refuse. The intended figure was presumably $0.11\%$.

### Death in Damascus

Death's appointment book is an accurate prediction of the agent's function, so Death's location is a child of the $\textsc{fdt}$ node. Both hypotheticals end in death, and fleeing also costs \$1,000. A-FDT stays.

The instability that the source attributes to CDT does not arise. The source argues that CDT, having settled on a belief state, would refuse to pay \$1 for a truly random coin. Under my reading of $G$, such a coin is *not* a child of the $\textsc{fdt}$ node, because Death cannot model it. A-FDT therefore values the coin at a 50% survival chance, worth roughly \$500,000, and buys it. The source does not perform this computation, but it follows directly from Equation (4).

## 6. A recipe for unfamiliar cases

The following procedure is mine, assembled from Section 5 of the source:

1. **List the variables.** Include the outcome, the agent's action, every other agent or process whose behavior might track the agent, and the observations.
2. **Name the function nodes.** Create one node for each input on which the agent's procedure may be run: each possible observation, and each possible preference profile if the agent is uncertain about her own utilities.
3. **Wire $G$.** Use the heuristic of Section 4. Add selector edges to $\textsc{Act}$ from whatever determines which observation, and hence which function node, is operative.
4. **Specify $P$.** This includes priors over function nodes the agent is *not* currently intervening on (the source's $q$).
5. **Intervene.** On the node for your *actual* observation $x$, set each candidate value $a$, propagate through $G$, and compute $\mathbb E[V]$ without conditioning on $\textsc{Obs}=x$.
6. **Choose the argmax.** Ties are not addressed by the source. Any fixed tie-breaker is consistent with Equation (4).

## 7. What the source leaves open, and how one might close it

**(a) Building $G$.** The source calls this "perhaps the largest open problem in the study of functional decision theory." Pearl showed how to learn causal structure from observation and experiment; nothing comparable exists for logical dependence. Hard cases include:

- an imperfect predictor that models a *similar but not identical* algorithm;
- a predictor that runs the function on a *different* input;
- deciding when two functions count as "the same."

My Section 4 heuristic handles the paper's examples. For partial similarity, a natural extension is a mixture: with probability $s$ the other system's output copies the $\textsc{fdt}$ node, and otherwise it is independent. This treats similarity exactly as the source treats predictor error. It is an assumption of mine, not a result of the source.

**(b) Counterpossibles.** Intervening on a function's output asks what would happen if a mathematical fact were otherwise. The source concedes that this is "the main drawback of FDT relative to CDT at this time," but calls the difficulty "technical rather than philosophical." Its evidence is that mathematicians reason sensibly under logical uncertainty. It also considers an alternative, FDT′, which would reason about *which* function to implement rather than what this function outputs, and rejects it because predictors of $d$ would still have to be imagined as predicting differently, which returns the problem to the same counterpossible.

**(c) Priors on non-intervened function nodes.** In the source's examples, the prior on the other node (the $q$ above) does not affect the verdict. That is a feature of those examples, not a theorem.

When it does matter, I propose a consistency requirement. The prior on $\textsc{fdt}(\underline P,\underline G,\underline y)$ for $y\neq x$ should place mass 1 on what Equation (4) would output at $y$, and the resulting fixed point should be found by iteration. This parallels how the source says $q$'s "correct" value is computable ("as you may verify").

This proposal exposes a real limitation of A-FDT, which leads to the next point.

**(d) A-FDT versus P-FDT.** A-FDT sets one input's output at a time and holds the others at their priors. That procedure can settle into a poor *self-consistent* configuration. The following example is my own construction.

Two copies of an agent receive different labels, *red* and *blue*.

- If both choose $A$, each gets 2.
- If both choose $B$, each gets 1.
- Mismatched choices give 0.

Suppose the red-copy reasons with a prior that the blue-node outputs $B$. Intervening on the red-node, $B$ yields 1 and $A$ yields 0, so it outputs $B$. The symmetric reasoning holds for blue. The profile $(B,B)$ is a fixed point of A-FDT.

P-FDT instead chooses a whole mapping from observations to actions in a single intervention. It compares the policy $(A,A)$, worth 2, against $(B,B)$, worth 1, and selects $(A,A)$.

This fits the source's own remark that the action/policy difference "makes a difference in certain multi-agent dilemmas." It is also why the authors prefer the policy formulation. For the source's own examples, A-FDT suffices.

**(e) Fairness.** The source does not claim A-FDT wins everywhere. Dilemmas that punish a particular *procedure* defeat every theory. The source's claim is that FDT does at least as well as its rivals in "fair problems," where the outcome depends only on the agent's behavior. It admits that formalizing fairness is open and gives a counterexample that complicates it (footnote 15).

## 8. The philosophical case

The source's motivation rests on several arguments.

**Utility achieved.** "Newcomb's problem doesn't punish rational agents; it punishes *two-boxers*." Agents who reason by A-FDT reliably see full boxes, hitch rides out of the desert, and receive no blackmail. The source treats this argument "from utility" as primary.

**Precommitment.** CDT and EDT agents would pay to bind themselves to A-FDT's choices. A-FDT simply "act[s] as [it] would have precommitted to act," with no need for ratification or self-modification. The source calls it "reflectively stable in fair problems."

**Dominance is not neutral.** "Every expected utility theory comes with its own notion of dominance." CDT's dominance argument for two-boxing restates CDT's way of building hypotheticals rather than giving independent support. Under A-FDT counterfactuals, A-FDT never takes a dominated act.

**Diagnosis of the rivals.** "EDT's hypotheticals respect too many correlations between variables; CDT's hypotheticals respect too few." EDT preserves merely statistical correlations, which is why it pays in the XOR blackmail. CDT severs logical ones, which is why it imagines perfect predictors failing.

**Control.** The objection that A-FDT agents falsely think they "control" mathematical facts cuts equally against deterministic CDT agents "controlling" their action token. On the source's view, both theories rely on useful impossibilities.

## 9. Conclusion

A-FDT is CDT with the point of surgery moved. Instead of intervening on the physical action and conditioning on observations, it intervenes on the node representing *the output of this very decision function on this very input*, and lets the observation decide which node that is. Given a model $P$ and a subjunctive-dependence graph $G$, Equation (4) is fully mechanical.

The resulting verdicts are: cooperate with twins, one-box, smoke, pay the driver, one-box even with transparent boxes, refuse both kinds of blackmail, and stay in Damascus.

The theory's real content is concentrated in $G$, and the source openly gives no method for constructing it. I have proposed a working rule (edges to whatever implements or accurately models the function on the same input) and a consistency condition for the agent's beliefs about its own behavior on other inputs. I have also shown that A-FDT, unlike the policy-selecting P-FDT the authors prefer, can settle into poor self-consistent configurations in coordination problems. Within these limits, A-FDT can be applied with the same discipline as Pearl-style CDT.

## References

- Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. CUP.
- Pearl, J. (2000). *Causality*. CUP.
- Yudkowsky, E. & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.