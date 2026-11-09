# A-FDT: Action Functional Decision Theory, Explained and Operationalized

## 1. What this essay is about

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* proposes a rule for choice under uncertainty. The rule is that an agent should treat her decision as the output of a fixed mathematical function and ask "Which output of this very function would yield the best outcome?" The paper's formal statement, Equation (4) in Section 5, selects an **action** by intervening on a node that represents the output of the agent's decision procedure. In two footnotes (7 and 16) the authors say that their "preferred formalization" instead iterates over *policies*, meaning maps from observations to actions.

To keep these apart, I call the action-selecting rule of Equation (4) **A-FDT** (action functional decision theory). I call the footnoted policy-selecting variant **P-FDT**. Evidential decision theory is **EDT** and causal decision theory is **CDT**. Unless I flag something as my own proposal, claims about the theory's content come from the paper.

## 2. The common frame: expected utility over hypotheticals

The paper places all three theories inside one expected-utility template, drawn from Gibbard and Harper:

$$
\mathcal{EU}(a) := \sum_{j} P(a \hookrightarrow o_j;\, x)\cdot \mathcal U(o_j). \tag{1}
$$

Here $a$ ranges over a finite action set $\mathcal A$, $x$ is the observation history, and $\mathcal U$ is a bounded utility function. The connective $\hookrightarrow$ ("decision hypothetical") is the free parameter. Following Joyce, the authors say the theories disagree "about the epistemic perspective from which actions are to be evaluated," not about value.

Operationally, the agent holds a world-model $M$. For each action she builds a *hypothetical* $M^{a\hookrightarrow}$, scores it, and takes the best. The paper insists that hypotheticals "are not themselves beliefs; they are decision-theoretic instruments constructed from beliefs." Writing $V := \mathcal U(\textsc{Outcome})$, the three rules are:

- **EDT (Eq. 2):** $\arg\max_a \mathbb E(V\mid \textsc{Obs}=x,\textsc{Act}=a)$. The hypothetical is formed by conditioning.
- **CDT (Eq. 3):** $\arg\max_a \mathbb E(V\mid \mathtt{do}(\textsc{Act}=a),\textsc{Obs}=x)$. The hypothetical is formed by Pearl-style surgery on the *physical act* node of a causal graph $G$.
- **A-FDT (Eq. 4):**

$$
\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\!\left(V \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right). \tag{4}
$$

## 3. Reading Equation (4)

**The intervention node.** $\textsc{fdt}(\underline P,\underline G,\underline x)$ is a variable *in the agent's own model*. It represents the logical fact "what the FDT algorithm outputs when run on inputs $(P,G,x)$." The underlines mark dequoting: the node's name is built from the model itself. The paper calls this self-reference harmless. The agent needs a variable *representing* the output, not knowledge of its value, and Kleene's recursion theorem ("quining") shows such self-representing structures exist.

**The graph.** In A-FDT, $G$ is not merely causal. It records "the logical, mathematical, computational, causal, etc. structure of the world," and in particular which variables *subjunctively depend* on the decision node. Pearl's $\mathtt{do}$ is reused on this richer graph as a stand-in for an operator $\mathtt{true}(\phi)$ that would update on a counterpossible logical sentence. The authors admit they do not know how to define $\mathtt{true}$ directly.

**Two differences from CDT.** The paper names exactly two:

1. A-FDT intervenes on the decision-function node, not on $\textsc{Act}$.
2. A-FDT responds to observations "by changing which node it intervenes upon," intervening on $\textsc{fdt}(\underline P,\underline G,\underline y)$ instead of $\textsc{fdt}(\underline P,\underline G,\underline x)$. CDT responds by Bayesian conditioning.

**Agreement condition.** Suppose every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from $\textsc{Act}$'s own dependence on the decision node. Then
$$\mathbb E[V\mid a]=\mathbb E[V\mid\mathtt{do}(a)]=\mathbb E[V\mid\mathtt{do}(\textsc{fdt}=a)],$$
and all three theories coincide. They come apart only when something outside the agent's causal future, such as a predictor or a twin, tracks her decision procedure.

### Subjunctive dependence

Two physical systems that compute the same function "subjunctively depend" on that function. The paper's illustration is two calculators computing $6288+1048$. Causal dependence is a special case: a scribe copying the calculator's output depends on it both causally and subjunctively. Mere statistical correlation is not subjunctive dependence: two calculators that happen to be pink do not depend on each other. The slogan is: "*Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*"

The normative core is stated as a condition on hypotheticals. The agent "imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

## 4. An operational recipe for building $(P,G)$

The paper gives no general procedure for constructing $G$. It calls "deducing the structure of subjunctive dependencies from observation and experiment" "perhaps the largest open problem." From its worked examples I extract the following recipe. **The recipe is my own systematization, not the paper's text.**

1. **Decision nodes.** For each observation history $y$ the agent might be in, include a node $\textsc{fdt}(\underline P,\underline G,\underline y)$ ranging over $\mathcal A$.
2. **The body.** Make $\textsc{Act}$ a deterministic selector: $\textsc{Act}=\textsc{fdt}(\underline P,\underline G,\textsc{Obs})$. The routing variables that determine $\textsc{Obs}$, such as a prediction or the lesion, are parents of $\textsc{Act}$. This is exactly how the paper's graphs for the transparent Newcomb problem, the XOR blackmail, and the mechanical blackmail are drawn.
3. **Predictors and copies.** Draw an arrow from $\textsc{fdt}(\underline P,\underline G,\underline y)$ to every variable whose mechanism computes or models the agent's decision function on input $y$. Examples are a predictor's prediction, a twin's act, or Death's appointment book. Represent imperfect modeling with an exogenous noise parent (the paper's $\textsc{Accurate}$ node).
4. **No arrows to lesion-like variables.** Variables that are merely statistically correlated with the act get no arrow from a decision node. In the paper's words, the cancer "is not evaluating the agent's future decisions."
5. **Evaluate.** For each $a$, set the node for the *actual* input $x$ to $a$. Propagate along descendants. Leave non-descendants at their prior distribution, including the decision nodes for other inputs. Compute $\mathbb E[V]$.

Two interpretive points need flagging.

**Is there conditioning on $\textsc{Obs}=x$?** Equation (4) contains none. In the transparent-Newcomb section, the paper does display $\mathbb E(V\mid\mathtt{do}(\textsc{fdt}(\ldots,\textit{full})=a,\textsc{Obs}=\textit{full})$, with an unbalanced parenthesis. However, its actual numbers are computed *without* conditioning on $\textsc{Obs}$: they include branches where the box is empty. The prose says the same thing: Fiona "does not react to observations by conditioning her distribution." I therefore read Equation (4) literally. Observations enter only by selecting the intervention node. Conditioning as well would produce the harmful "double update" the paper attributes to Timeless Decision Theory.

**What values do the other decision nodes take?** The paper leaves them at prior probabilities ($q$ in its examples) and remarks that $q$ does not matter in the cases studied. In general it can matter. My proposal is to set these priors to the agent's best estimate of what A-FDT itself outputs on those inputs, iterating if necessary. That is a fixed-point condition, which the paper neither states nor needs. Where it becomes delicate, the natural fix is to switch to P-FDT and choose all decision nodes jointly (§7).

## 5. Worked cases

All payoffs are in dollars-as-utility, as in the source. Several of the paper's printed figures contain small arithmetic typos, so I compute directly.

### Twin prisoner's dilemma

Both twins' acts are children of the single node $\textsc{fdt}$, because they run the same reasoning.

- $\mathtt{do}(\textsc{fdt}=\textit{cooperate})$ gives (C, C), worth \$1,000,000.
- $\mathtt{do}(\textsc{fdt}=\textit{defect})$ gives (D, D), worth \$1,000.

A-FDT cooperates. CDT holds the twin's act fixed, so defecting dominates and CDT defects.

### Newcomb's problem (99% predictor)

The graph has $\textsc{fdt}\to\textsc{Act}$ and $\textsc{fdt}\to\textsc{Prediction}\leftarrow\textsc{Accurate}$.

- One-box: $0.99\cdot 10^6 = 990{,}000$.
- Two-box: $0.01\cdot 1{,}001{,}000 + 0.99\cdot 1{,}000 = 11{,}000$.

A-FDT one-boxes. The paper stresses that no retrocausation is assumed. The agent simply refuses to imagine her algorithm's output changing while a competent model of that algorithm stays fixed.

### Smoking lesion

The lesion fixes both cancer risk and preferences, so the agent cannot tell which utility function she has. The paper models this with two decision nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ and $\textsc{fdt}(\underline{P_R},\underline G)$, and a lesion-controlled selector for $\textsc{Act}$. Neither decision node points to $\textsc{Cancer}$. Let $p=P(\textit{lesion})$, and let $q$ be the prior that the non-lesion version smokes. Then

$$
\mathbb E[V\mid\mathtt{do}(\textit{smoke})]-\mathbb E[V\mid\mathtt{do}(\textit{refrain})] = p\cdot 1{,}000>0,
$$

and A-FDT smokes. The paper adds that the problem is "badly confused," and it recommends dropping it.

### Transparent Newcomb, observing a full box

The prediction both routes $\textsc{Act}$ (through what the agent sees) and fills the box. Intervene on $\textsc{fdt}(\ldots,\textit{full})$, and let $q$ be the prior that the agent two-boxes when she sees an empty box.

- One-box: $0.99\cdot 10^6 + 0.01\cdot 1{,}000q = 990{,}000+10q$.
- Two-box: $0.01\cdot 1{,}001{,}000+0.99\cdot 1{,}000q = 10{,}010+990q$.

A-FDT one-boxes even while looking at \$1,001,000. The decisive feature is that the two-box hypothetical is mostly a world in which she *never saw a full box*. The paper notes this is "precisely equivalent" to paying in Parfit's hitchhiker problem, and it defends the result with arguments from precommitment, from the value of information, and above all from utility.

### XOR blackmail (infallible predictor)

Let $p=P(\textit{termites})$. The letter arrives iff (no termites and the agent pays) or (termites and the agent refuses).

- $\mathtt{do}(\textsc{fdt}(\ldots,\textit{letter})=\textit{pay})$: termites means no letter and a loss of $10^6$; no termites means a letter and a payment of 1,000. Expected value: $-p\cdot 10^6-(1-p)\cdot 1{,}000$.
- $\mathtt{do}(\ldots=\textit{refuse})$: expected value $-p\cdot 10^6$.

A-FDT refuses, because there are no arrows from the decision node to $\textsc{Infestation}$. EDT pays, since paying is "good news." CDT also refuses, but its hypothetical portrays the inerrant predictor as having erred.

### Mechanical blackmail with error rate $\varepsilon$

The blackmailer runs the program iff she predicts payment, and she wrongly predicts payment with probability $\varepsilon$.

- Paying: always blackmailed, always pays, so $-1{,}000$.
- Refusing: blackmailed only by error, so $-\varepsilon\cdot 10^6$.

A-FDT refuses iff $\varepsilon<10^{-3}$. At $\varepsilon=0.0009$ the expected loss from refusing is \$900, so it refuses even while holding a letter it knows was sent in error. For $\varepsilon>0.1\%$ it pays. CDT and EDT pay at any $\varepsilon$, which is why they get blackmailed.

### Death in Damascus

Death's book is a child of the decision node.

- Stay: die, worth 0.
- Flee: die and pay \$1,000, worth $-1{,}000$.

A-FDT stays, with none of the instability that CDT shows. Now suppose a truly random coin, independent of every decision node, is offered for \$1, and buying it is in $\mathcal A$. Then $\mathtt{do}(\textit{buy})$ yields survival with probability ½, worth $500{,}000-1$, so A-FDT buys it. The paper argues CDT declines, because its hypotheticals already credit it with at least a 50% chance of survival.

## 6. Dominance, regret, and "control"

The paper argues that dominance is not theory-neutral. CDT's "two-boxing dominates" holds only if one varies the physical action while holding fixed the decision function's output, "akin to... imagin[ing] [the calculator] outputting $3159$, holding constant the fact that $6288+1048=7336$." A-FDT has its own dominance notion: hold the subjunctive dependencies fixed and switch the algorithm's output. By that notion A-FDT never picks a dominated act.

The paper also offers a parity argument against the charge that A-FDT agents "control" mathematics. A deterministic CDT agent equally has only one possible act yet must imagine alternatives. Both theories "contain impossibilities" in their hypotheticals. The difference is practical.

## 7. What the source leaves open, and how one might proceed

**(a) Counterpossibles and the graph.** A-FDT's hypotheticals have logically impossible antecedents. The paper sidesteps the problem by taking $G$ as input, just as CDT takes the causal graph as input, and it calls the difficulty "technical rather than philosophical." For practical use, my recipe in §4 reduces the question to: *which mechanisms model my decision procedure on this input?* That question is often answerable in stylized problems. It is hard for partial similarity, such as an agent who runs a decision procedure that is merely *similar* to mine. A conservative operational choice, which is my suggestion, is to treat partial similarity like an imperfect predictor. Add a noise parent whose accuracy is set to the agent's credence that the other system's output matches hers on this input.

**(b) A-FDT vs. P-FDT.** Equation (4) sets only the node for the actual input and leaves the other decision nodes at their priors. P-FDT instead chooses a whole policy $\pi:\mathcal X\to\mathcal A$:
$$\arg\max_\pi \mathbb E\big(V\mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G)=\pi)\big),$$
then outputs $\pi(x)$. (This rendering is mine. The paper only describes the variant in words.) The two agree whenever the optimal action at $x$ does not depend on how the agent behaves at other inputs, or whenever the priors on other nodes already match the optimal policy. The authors say the difference "only matters in multi-agent dilemmas so far as we can tell."

My fixed-point reading of the priors (§4) pushes A-FDT toward a policy that is a "local optimum": no single input's action can be improved given the others. P-FDT instead finds a global optimum, and local and global optima can come apart in coordination-like structures. Readers applying A-FDT to novel cases should check whether such coupling is present.

**(c) Self-reference and probability on one's own output.** Equation (4) evaluates the do-distribution, so a sharp prior on one's own output causes no zero-probability failures of the kind that afflict EDT. The paper's Newcomb discussion makes the point explicitly. Fiona can be nearly certain she one-boxes and still evaluate two-boxing correctly, because she intervenes rather than conditions.

**(d) Fairness.** The paper claims superiority only on "fair" problems, in which outcomes depend on the agent's *behavior* rather than on her decision procedure. Its example of an unfair problem is "punish anyone who takes the same action as [a copy of Fiona]." The authors concede they lack a formal definition of fairness.

## 8. Conclusion

A-FDT is expected-utility maximization in which the hypothetical for action $a$ is built by intervening on a node representing "my decision algorithm, on this very input, outputs $a$." Everything that subjunctively depends on that node is propagated, and everything else is left alone, including merely correlated lesions and the agent's own behavior on other inputs. Observations change *where* one intervenes, not *what* one conditions on.

Given a graph of subjunctive dependence, the procedure is fully mechanical. It one-boxes, smokes, pays the driver, refuses blackmail when the error rate is below the cost of paying, and does not flee Death. Its main unsolved ingredients are a principled method for building that graph and an account of counterpossibles. For an action-based theory, it also needs a clear treatment of the decision nodes it does not intervene on. Where that last issue bites, moving to the policy formulation is the natural repair.

---

**References.** Yudkowsky, E. & Soares, N., *Functional Decision Theory: A New Theory of Instrumental Rationality* (arXiv:1710.05060). Gibbard, A. & Harper, W., "Counterfactuals and Two Kinds of Expected Utility" (1978). Joyce, J., *The Foundations of Causal Decision Theory* (1999). Pearl, J., *Causality* (2000).