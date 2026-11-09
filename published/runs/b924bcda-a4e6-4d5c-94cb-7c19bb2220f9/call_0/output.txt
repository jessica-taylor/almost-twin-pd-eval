# A-FDT: Choosing as if You Were the Function

## 1. What this essay covers

Yudkowsky and Soares (2017) propose *functional decision theory* as an alternative to causal decision theory (CDT) and evidential decision theory (EDT). Its guiding question, in their words, is: "Which output of this very function would yield the best outcome?"

The paper offers more than one formalization. Its main equation, Equation (4) in Section 5, has the agent intervene on a variable representing the output of its decision procedure on its actual input, and maximize over **actions**. Two footnotes (7 and 16) say that "in the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions." To keep these apart, this essay uses:

- **A-FDT** (action functional decision theory) for the theory defined by Equation (4);
- **policy-selecting FDT** for the footnoted variant.

When I quote the paper, its "FDT" in Section 5 refers to what I call A-FDT. I mark clearly which claims come from the source and which are my own interpretations or proposals.

## 2. The shared framework: expected utility with a free parameter

The paper places EDT, CDT and A-FDT in one expected-utility template (its Equation 1). The agent chooses the action $a$ that maximizes

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),
$$

where:

- $x$ is the agent's observation history;
- $\mathcal U$ is the utility function;
- $P(a \hookrightarrow o_j; x)$ is the probability of outcome $o_j$ in "the hypothetical scenario where the action $a$ is executed."

Following Joyce, the authors treat the interpretation of $\hookrightarrow$ as the one free parameter. The three theories differ only in how they build hypotheticals from a world model. Writing $V = \mathcal U(\textsc{Outcome})$:

$$
\mathrm{EDT}(P,x) = \arg\max_a \mathbb E[V \mid \textsc{Obs}=x,\ \textsc{Act}=a], \qquad
\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E[V \mid do(\textsc{Act}=a),\ \textsc{Obs}=x].
$$

- **EDT** conditions on the act. It therefore respects every correlation, including merely statistical ones.
- **CDT** performs Pearl-style surgery on the physical act node. It keeps only correlations that run causally downstream of the act.

The paper's diagnosis is that EDT respects too many correlations and CDT too few.

## 3. The definition of A-FDT

A-FDT is defined by:

$$
\boxed{\ \text{A-FDT}(P,G,x) = \arg\max_{a\in\mathcal A}\ \mathbb E\!\left[V \;\middle|\; do\!\left(\mathsf{fdt}(\underline P,\underline G,\underline x)=a\right)\right]\ } \tag{4}
$$

The ingredients are as follows.

- **$P$** is a joint distribution over world variables. Crucially, it includes variables for the *outputs of mathematical functions*, such as the output of A-FDT itself on various inputs.
- **$G$** is a graph that, as the paper puts it, "tells us how changing a logical variable affects all other variables." It encodes **subjunctive dependence**: "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." Causal dependence is a special case. Mere statistical correlation is not included.
- **$\mathsf{fdt}(\underline P,\underline G,\underline x)$** is a node naming "the output of A-FDT when run on inputs $P,G,x$." The underlines denote dequoting: the node's *name* is built from the model itself. The authors call this self-reference harmless. The agent needs only a variable *representing* its output, not knowledge of the output, and Kleene's recursion theorem guarantees that such self-representing data structures exist.
- **$do(\cdot)$** is Pearl's intervention, reused unchanged. The surgery now severs the node's ordinary parents and propagates the change to everything downstream in $G$. That includes the agent's physical act *and* any predictor, twin or simulation that computes or models the same function.

The slogan is the paper's own: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." CDT intervenes on the *token* act. A-FDT intervenes on the *type*: the output of the function that the agent's brain, and anything else computing it, instantiates.

### Two structural differences from CDT

Comparing (3) and (4), the paper notes two differences.

1. **Point of intervention.** CDT intervenes on $\textsc{Act}$; A-FDT intervenes on $\mathsf{fdt}(\cdot)$.
2. **Treatment of observations.** "Where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon."

Equation (4) contains no "$\textsc{Obs}=x$" term. The observation $x$ appears only as an index selecting the intervention node.

The second difference is easy to overlook, and it does most of the work in transparent Newcomb and blackmail cases. If $\mathsf{fdt}(\ldots,x)=a$ makes it less likely that the agent observes $x$ at all, A-FDT counts that against $a$. In the paper's phrase, agents "should entertain the hypothesis that, if their action were different, they might have *made different observations*."

### Where the theories agree

The paper notes that when every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$ (apart from its dependence on the decision node), we have

$$
\mathbb E[V\mid a]=\mathbb E[V\mid do(a)]=\mathbb E[V\mid do(\mathsf{fdt}=a)].
$$

So the three theories diverge only when something other than the act's causal effects correlates with the act. The typical case is a predictor.

## 4. A-FDT as a procedure

Read as an algorithm, A-FDT requires the following steps. Steps 2 and 3 involve modelling choices the paper leaves partly implicit; I flag them in §6.

1. **Model.** Write down variables for the environment, the agent's physical act, and the outcome, together with a utility node $V$.
2. **Decision nodes.** For each input the decision function might receive in the problem (observation $x$, alternative observations $x'$, and in the smoking lesion case alternative utility functions), add a node $\mathsf{fdt}(\cdot, x')$.
3. **Subjunctive edges.** Draw an edge from $\mathsf{fdt}(\cdot,x)$ to every process whose behavior depends on what that function outputs on that input:
   - the agent's own act, gated by whichever input it actually receives;
   - accurate predictors, with separate noise nodes for their error rates;
   - copies and twins.

   Do *not* draw edges to things merely correlated with the act through common causes that do not model the function, such as lesions or genes.
4. **Priors.** Give probabilities to exogenous nodes, including the decision nodes for inputs the agent is *not* currently facing.
5. **Evaluate.** For each $a\in\mathcal A$, perform $do(\mathsf{fdt}(\underline P,\underline G,\underline x)=a)$, propagate the change, and compute $\mathbb E[V]$.
6. **Act.** Output the argmax.

## 5. Worked examples

### Twin prisoner's dilemma

Two causally isolated agents run the same decision function. One node, $\mathsf{fdt}$, feeds both acts. Intervening on it gives:

- $do(\mathsf{fdt}=C)$: both cooperate, yielding \$1,000,000;
- $do(\mathsf{fdt}=D)$: both defect, yielding \$1,000.

A-FDT cooperates. EDT also cooperates, but by conditioning. CDT defects, because it severs the twin's act from its own.

### Newcomb's problem

The predictor is 99% accurate. The graph has $\mathsf{fdt}\to\textsc{Act}$ and $\mathsf{fdt}\to\textsc{Prediction}\to\textsc{Box B}$, with an accuracy node feeding into $\textsc{Prediction}$.

$$
\begin{aligned}
\mathbb E[V\mid do(\mathsf{fdt}=\textit{one})] &= 0.99(10^6) = \$990{,}000,\\
\mathbb E[V\mid do(\mathsf{fdt}=\textit{two})] &= 0.01(1{,}001{,}000)+0.99(1{,}000)=\$11{,}000.
\end{aligned}
$$

A-FDT one-boxes, and the paper's figures match these. The paper explicitly answers the "but the box is already full" objection: the agent invokes no retrocausation. A-FDT simply refuses to imagine its action differing while a competent model of its decision function stays fixed. Doing so would be like imagining a working calculator outputting something other than $6288+1048$.

### Smoking lesion

Here the lesion causes both a taste for smoking and cancer. In the paper's formalization, the lesion determines *which* decision node controls the act: $\mathsf{fdt}(P_S,\cdot)$ if the agent has the lesion, $\mathsf{fdt}(P_R,\cdot)$ if not. Cancer has no edge from either node, because the lesion does not model the function.

Intervening therefore leaves $P(\textit{lesion})=p$ unchanged. The paper computes that smoking beats refraining by $p\cdot\$1{,}000$. A-FDT smokes, agreeing with CDT and disagreeing with EDT. This is the paper's headline result: one rule both one-boxes and smokes.

### Transparent Newcomb

Both boxes are visible, and box B is full iff the predictor foresaw one-boxing *upon seeing it full*. The graph has two decision nodes, $\mathsf{fdt}(\ldots,\textit{full})$ and $\mathsf{fdt}(\ldots,\textit{empty})$. The prediction determines which observation occurs, and hence which node controls the act. Let $q$ be the prior that the agent two-boxes on seeing an empty box. Intervening on the *full* node:

$$
\begin{aligned}
\text{one-box: } & 0.99(10^6) + 0.01\,q\,(1{,}000) = 990{,}000 + 10q,\\
\text{two-box: } & 0.01(1{,}001{,}000) + 0.99\,q\,(1{,}000) = 10{,}010 + 990q.
\end{aligned}
$$

A-FDT one-boxes for every $q\in[0,1]$. The paper prints the second figure as "\$110,00 + q·\$990." The correct value is \$10,010 + q·\$990, and the conclusion is unaffected.

The paper's displayed objective for this case includes "$\textsc{Obs}=\textit{full}$" inside the intervention. The calculation it actually performs, however, gives weight to worlds where the box is *empty*. If one genuinely conditioned on seeing a full box, two-boxing would win by \$1,000. I therefore treat Equation (4) as authoritative: **the observation selects the node and is not conditioned on.**

### Blackmail

**XOR blackmail.** An infallible predictor sends a letter iff exactly one of these holds:

- there are no termites and the agent would pay upon receiving the letter;
- there are termites and the agent would not pay.

Let $p=P(\textit{termites})$; termite damage costs \$10⁶. Under $do(\mathsf{fdt}(\ldots,\textit{letter})=\textit{pay})$, the letter arrives exactly when there are no termites. Expected loss is $p\cdot 10^6+(1-p)\cdot 1{,}000$. Under *refuse*, the letter arrives exactly when there are termites, and the expected loss is $p\cdot 10^6$. A-FDT refuses, as does CDT, though for different counterfactual reasons. EDT pays.

**Mechanical blackmail.** The blackmailer starts the program (costing \$10⁶ unless the agent pays \$1,000) only if she predicts payment. She wrongly expects payment from a refuser with probability $\varepsilon$.

- *Pay:* the agent is always blackmailed and loses \$1,000.
- *Refuse:* the agent is blackmailed with probability $\varepsilon$ and loses $\varepsilon\cdot 10^6$.

A-FDT refuses iff $\varepsilon<10^{-3}$. The paper's case of $\varepsilon=0.09\%$ (an expected loss of \$900) correctly yields refusal. Its claim that A-FDT pays when the error is "0.011%" does not follow, since that gives an expected loss of \$110. The intended figure was presumably 0.11%. In general, A-FDT refuses even while holding the letter and knowing the prediction was wrong, "because it's advantageous to be *the kind of agent* that makes such decisions."

### Death in Damascus

Death predicts perfectly, so both $do(\mathsf{fdt}=\textit{stay})$ and $do(\mathsf{fdt}=\textit{flee})$ lead to death. Staying saves \$1,000, so A-FDT stays, with none of CDT's instability.

The paper argues that CDT would refuse a \$1 truly random coin offering a 50% chance of survival. It does not spell out A-FDT's response. The natural extension is as follows. If the coin's outcome is genuinely not computed by Death, then $\textsc{Coin}$ is a node with no edge from $\mathsf{fdt}$. Intervening on "buy and follow the coin" yields $0.5\cdot10^6-1$, so A-FDT buys it.

## 6. What the paper leaves open, and how to operate anyway

### (a) Where does $G$ come from?

This is the deepest gap, and the authors say so: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." Equation (4) is only as good as the graph supplied to it.

**My operational proposal.** Draw an edge from $\mathsf{fdt}(\cdot,x)$ to process $Z$ when $Z$'s behavior is produced by evaluating, simulating or reliably reasoning about that function on that input. Model the reliability of $Z$ with an independent noise node. Treat everything else as ordinary causal structure.

This test explains the paper's lesion/predictor asymmetry: "the cancer is not evaluating the agent's future decisions." It also gives a usable heuristic for new cases. Ask *how* the correlated variable comes to match your act. If the answer is "it models your reasoning," draw the edge. If the answer is "a shared upstream cause shapes both," do not.

The proposal leaves partial cases unresolved, such as a predictor who uses a crude heuristic correlated with your function. I would handle these with the noise-node accuracy, but the paper gives no principled account.

### (b) Is $P$ already updated on $x$?

Equation (4) takes $P$ and $x$ as separate arguments and never conditions on $\textsc{Obs}$. The transparent Newcomb and blackmail calculations only work if $P$ still assigns weight to the worlds the observation rules out. The paper also warns, in a draft note on "Timeless Decision Theory," that conditioning on evidence *and* switching intervention nodes "creates a kind of 'double update' which proves harmful in practice."

**My reading.** $P$ should be the agent's model as of before the problem's decision-relevant observations, with $x$ entering only through the node index. This reading is strongly suggested by the source but is not stated as a definition.

### (c) Nodes for other inputs: priors or choices?

This is where A-FDT differs from policy-selecting FDT. In A-FDT, the nodes $\mathsf{fdt}(\cdot,x')$ for $x'\neq x$ are exogenous and carry prior probabilities: the paper's $q$ in the smoking lesion and transparent Newcomb cases. The paper remarks parenthetically that "the correct $q$ is 1, as you may verify," and shows that the verdict does not depend on $q$ in those cases. In general, though, it can.

**An example of my own construction.** Two copies of an A-FDT agent are separated. One is shown a red card, the other a blue card. Each picks $L$ or $R$, and each earns 1 if they match and 0 otherwise.

- The red copy intervenes on $\mathsf{fdt}(\cdot,\textit{red})$. Its partner is governed by the distinct node $\mathsf{fdt}(\cdot,\textit{blue})$, held at prior $r=P(L)$.
- The red copy therefore picks $L$ iff $r>1/2$. With a symmetric prior it is indifferent, and miscoordination is possible.
- Policy-selecting FDT instead chooses a map $\pi:\{\textit{red},\textit{blue}\}\to\{L,R\}$ and immediately sees that any constant policy earns 1.

This is consistent with the paper's remark that the action/policy distinction "only matter[s] in multi-agent dilemmas so far as we can tell." Here, the "multi-agent" structure is two instances of one function receiving different inputs.

**A proposed repair (my addition).** Require the priors on other-input nodes to be *self-consistent*: they should equal the outputs A-FDT would actually produce on those inputs. This is a fixed-point condition, which the paper's "as you may verify" remarks tacitly invoke. In the coordination game, $(L,L)$ and $(R,R)$ are both fixed points, so self-consistency narrows the answer but does not select one. When such ambiguity matters, I would suggest that policy-selecting FDT, rather than A-FDT, is the better-specified tool.

### (d) Counterpossibles and ties

A function's output on a fixed input is logically necessary, so intervening on it is counterpossible. The paper sidesteps the problem by supplying $G$ as input, deferring a true $\mathsf{true}(\phi)$ operator to future work.

Equation (4) also returns an argmax *set*. The paper is silent on ties. Any implementation needs a tie-breaking rule, and per (c), that rule can itself matter to anyone predicting the agent.

### (e) Fairness

The paper concedes that problems which punish a particular *procedure* can defeat any theory. For example, a mind reader might reward only agents who would two-box in Newcomb's problem. The authors conjecture that A-FDT is optimal on "fair" problems, those where outcomes depend only on behavior, but they have no formal definition of fairness. Footnote 15 shows why one is hard to give: punishing whoever matches a copy of the agent is intuitively unfair, yet it is defined purely in terms of behavior.

## 7. Philosophical motivation in brief

The paper's case rests on three arguments.

1. **Utility.** A-FDT agents get rich in Newcomb's problem, escape Parfit's desert by paying the driver (structurally identical to one-boxing in transparent Newcomb), and are not targeted by blackmailers.
2. **Precommitment.** CDT and EDT agents would *pay* to bind themselves to A-FDT's choices. A-FDT simply "act[s] as [it] would have precommitted to act," and so is reflectively stable on fair problems, where CDT recommends self-modification.
3. **Dominance is not neutral.** Each way of constructing hypotheticals generates its own dominance notion. CDT's dominance argument for two-boxing restates CDT rather than independently supporting it.

On "control," the authors argue parity. Any objection that an agent cannot control its function's output applies equally to a deterministic CDT agent "controlling" its token act. Both theories rely on imagined variation in something fixed.

## 8. Conclusion

A-FDT is CDT's surgery applied at a different place: on the node representing one's decision function's output on one's actual input, inside a graph that tracks subjunctive dependence as well as causal dependence. Observations select which node to intervene on rather than being conditioned on.

Given an accurate $(P,G)$, Equation (4) is a fully mechanical procedure. It one-boxes, smokes, cooperates with twins, pays the driver, refuses blackmail, and stays in Damascus.

Its open joints are real:

- how to build $G$;
- whether $P$ is pre-observation;
- how to set priors on the function's outputs for other inputs, including the coordination failures this can cause relative to policy-selecting FDT;
- how to define counterpossibles and fairness.

The operational interpretations proposed here are offered as reasonable working rules, not as claims of the source: a modelling test for subjunctive edges, a pre-observation reading of $P$, and fixed-point consistency for other-input nodes.

**Reference.** Yudkowsky, E. & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality.* arXiv:1710.05060.