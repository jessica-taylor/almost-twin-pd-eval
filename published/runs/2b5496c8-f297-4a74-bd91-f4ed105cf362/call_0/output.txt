# A-FDT: Action Functional Decision Theory, Explained and Operationalized

## 1. What A-FDT is, and why the name

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* introduces a family of decision rules built on one idea. The agent should treat her decision as the output of a fixed mathematical function and ask, in the abstract's words, "Which output of this very function would yield the best outcome?"

This essay concerns one precise member of that family: the rule given as **Equation (4) in Section 5** of the paper. I call it **A-FDT** (action functional decision theory). In A-FDT the agent intervenes on a variable whose values are *actions*. The paper itself calls Equation (4) simply "FDT". It also notes that it is not the authors' favoured version: "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions." I call that preferred variant **policy FDT**, which is my own label. Other theories appear under their usual names: **CDT** (causal decision theory) and **EDT** (evidential decision theory).

Where I quote the paper, its word "FDT" in Section 5 refers to what I call A-FDT. Throughout, I mark which claims come from the source and which are my interpretation.

## 2. The common frame: expected utility with a choice of hypothetical

All three theories in the paper maximize

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}
$$

Here $a$ ranges over a finite action set $\mathcal A$, $x$ is the observation history, and $P(a \hookrightarrow o_j; x)$ is the probability of outcome $o_j$ "in the hypothetical scenario where the action $a$ is executed after receiving observations $x$."

Following Joyce, the paper treats the interpretation of the connective $\hookrightarrow$ as a free parameter. The theories agree on how to value prospects. They disagree about the "epistemic perspective" from which actions are evaluated. Writing $V := \mathcal U(\textsc{Outcome})$:

$$
\mathrm{EDT}(P,x) = \arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a), \tag{2}
$$
$$
\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x). \tag{3}
$$

In (3), $G$ is a causal graph and $\mathtt{do}$ is Pearl's intervention operator. The intervention severs the arrows into the intervened node and propagates the new value only downstream.

The paper frames each theory as instructions for turning a world-model $M$ into a *hypothetical* $M^{a\hookrightarrow}$ for each action $a$. Hypotheticals "are not themselves beliefs; they are decision-theoretic instruments constructed from beliefs."

## 3. The definition of A-FDT

**Equation (4), Section 5** (source notation, with my name for the rule):

$$
\boxed{\;\mathrm{A\text{-}FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big)\;} \tag{4}
$$

The ingredients are as follows.

- **$P$** is a probability distribution over the agent's world-model. Unlike the distribution in EDT or CDT, it contains variables for the *outputs of mathematical functions*. The paper's example is a variable for $6288+1048$ that "(hopefully) has most of its probability on $7336$."
- **$G$** is a graph that, in the paper's words, "tells us how changing a logical variable affects all other variables." It encodes causal structure and also what the paper calls *subjunctive dependence*. "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function."
- **$\textsc{fdt}(\underline P,\underline G,\underline x)$** is the node representing the output of the A-FDT procedure itself on the inputs $(P,G,x)$. The underline denotes dequoting: the node's *name* is built from the actual inputs. The self-reference is harmless, according to the paper. To have a variable *representing* the output, the agent does not need to know its *value*, and Kleene's recursion theorem ("quining") shows how such self-representing structures can be built.
- **$\mathtt{do}$** is Pearl's operator, reused unchanged. It is applied to a logical node instead of a physical one.

The paper names exactly **two differences from CDT**:

1. **Intervention point.** CDT intervenes on the physical action $\textsc{Act}$. A-FDT intervenes on the node for its decision function's output. Borrowing Peirce, CDT intervenes on the token and A-FDT on the type. Anything downstream of that node in $G$ moves with it: the agent's body, a twin, a predictor's model of the agent.
2. **Treatment of observations.** "Where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." The observation $x$ appears in (4) only inside the name of the intervened node. There is no "$, \textsc{Obs}=x$" term.

The second point is easy to miss and does a great deal of work. I return to it in §5.

**Agreement theorem (source).** Suppose every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from the dependence of $\textsc{Act}$ on the $\textsc{fdt}$ node. Then
$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)],$$
so EDT, CDT and A-FDT coincide. The theories come apart only when something other than the action's own effects correlates with the action, typically because something *computes or predicts* the agent's decision.

## 4. A working procedure

The following recipe is my operationalization. Each step is either taken from the paper's worked examples or flagged as an assumption.

1. **Enumerate decision nodes.** For each observation history $y$ the agent could be facing, add a node $\textsc{fdt}(\underline P,\underline G,\underline y)$. Add an arrow from it to $\textsc{Act}$, gated by whichever variables determine which observation actually occurs. In the paper's figures the gating variable is, for example, the predictor's prediction, which decides whether the agent sees a full or an empty box.
2. **Add subjunctive arrows.** Draw an arrow from $\textsc{fdt}(\cdot,y)$ to every variable whose value is computed from the output of that function on that input: twins, accurate predictors, simulations. Model imperfect prediction as an independent noise node feeding the prediction, like the paper's $\textsc{Accurate}$ node.
3. **Do *not* draw arrows for mere statistical correlation or common causes.** A lesion, or a pink calculator in Tokyo, does not get an arrow. This is the line the paper draws between "predictor-like" and "lesion-like" things.
4. **Fix the actual observation $x$.** For each $a\in\mathcal A$, set $\textsc{fdt}(\cdot,x)=a$ by intervention. Leave the nodes for *other* observations at their prior distributions. Compute $\mathbb E(V)$ over the whole model, *including worlds in which the agent would not have observed $x$*.
5. **Output the argmax.** The paper does not specify tie-breaking.

The following examples, all taken from the paper, show the recipe at work. I re-derive the numbers.

## 5. Worked examples

### 5.1 Newcomb's problem (A-FDT one-boxes)

The setup is as follows. Box A holds \$1,000. Box B holds \$1,000,000 iff the predictor, who is 99% accurate, predicted one-boxing.

In the graph, $\textsc{fdt}\to\textsc{Act}$ and $\textsc{fdt}\to\textsc{Prediction}\leftarrow\textsc{Accurate}$. Then $\textsc{Prediction}\to\textsc{Box B}$, and $\textsc{Act},\textsc{Box B}\to V$.

$$
\begin{aligned}
\mathbb E[V\mid\mathtt{do}(\textsc{fdt}=\textit{onebox})] &= 0.99(1{,}000{,}000)+0.01(0) = 990{,}000,\\
\mathbb E[V\mid\mathtt{do}(\textsc{fdt}=\textit{twobox})] &= 0.01(1{,}001{,}000)+0.99(1{,}000) = 11{,}000.
\end{aligned}
$$

A-FDT one-boxes. CDT intervenes on $\textsc{Act}$, which leaves $P(\textit{full})=p$ fixed, so two-boxing wins by \$1,000 for every $p$.

The A-FDT agent's reasoning involves no retrocausation. She "does not think that a physical signal passes between her action and the predictor's prediction." She simply declines to imagine her decision function's output changing while an accurate model of that same function stays put.

### 5.2 Smoking lesion (A-FDT smokes)

A lesion causes both a love of smoking and, 99% of the time, cancer. Smoking itself is harmless and worth \$1,000. The paper formalizes the lesion as fixing *which utility function* the agent has, and therefore which decision node controls her act:

$$\textsc{Act}(\textit{lesion},s,r)=s,\qquad \textsc{Act}(\textit{nolesion},s,r)=r,$$

where $s,r$ are the outputs of $\textsc{fdt}(\underline{P_S},\underline G)$ and $\textsc{fdt}(\underline{P_R},\underline G)$.

Crucially, there is no arrow from either $\textsc{fdt}$ node to $\textsc{Cancer}$. Intervening on $s$ therefore leaves $P(\textit{lesion})=p$ unchanged. Let $q$ be the prior that the non-lesion node outputs *smoke*. Then:

$$
\begin{aligned}
\text{smoke: }&\ p(10{,}000+1{,}000)+(1-p)(990{,}000+1{,}000q),\\
\text{refrain: }&\ p(10{,}000)+(1-p)(990{,}000+1{,}000q).
\end{aligned}
$$

Smoking wins by $p\cdot\$1{,}000$, whatever $q$ is. One rule thus one-boxes and smokes, the combination Gibbard and Harper argued no consistent agent could have. The paper also argues that the smoking lesion problem itself is confused and recommends abandoning it.

### 5.3 Transparent Newcomb (A-FDT one-boxes even when seeing \$1M)

Both boxes are transparent. Box B is filled iff the predictor predicts the agent leaves box A behind *upon seeing both boxes full*. The agent sees two full boxes.

There are two decision nodes, $\textsc{fdt}(\cdot,\textit{full})$ and $\textsc{fdt}(\cdot,\textit{empty})$. The prediction depends on the *full*-node and gates which node drives $\textsc{Act}$. Let $q$ be the prior that the *empty*-node outputs *twobox*.

$$
\begin{aligned}
\mathtt{do}(\textsc{fdt}(\cdot,\textit{full})=\textit{onebox}):&\ 0.99(1{,}000{,}000)+0.01(1{,}000q) = 990{,}000+10q,\\
\mathtt{do}(\textsc{fdt}(\cdot,\textit{full})=\textit{twobox}):&\ 0.01(1{,}001{,}000)+0.99(1{,}000q) = 10{,}010+990q.
\end{aligned}
$$

The printed text gives the second line as "\$110,00 + $q\cdot$\$990". This is evidently a typesetting slip for \$10,010 + 990$q$. The conclusion is unaffected: A-FDT one-boxes.

This calculation settles an interpretive point. The paper's display here reads "$\mathbb E(V \mid \mathtt{do}(\textsc{fdt}(\cdot,\textit{full})=a, \textsc{Obs}=\textit{full})$". Taken literally, that would condition on the box being full. But the paper's own computation includes the inaccurate-prediction branch, in which the box is *empty*. So the computation does **not** condition on $\textsc{Obs}=x$. This matches Equation (4), which contains no observation term, and the explicit statement that A-FDT reacts to observations only by switching nodes.

The paper's footnote on Timeless Decision Theory confirms that conditioning and switching nodes together would be a mistake. It describes TDT as prescribing "both conditioning on evidence *and* changing the place where one intervenes," which "creates a kind of 'double update' which proves harmful in practice."

**Operational rule (supported by the source):** under A-FDT, the observation selects the intervention node and is otherwise *not* conditioned on.

### 5.4 Mechanical blackmail and a threshold calculation

A blackmailer runs a damaging program, costing \$1,000,000, iff she predicts the agent would pay \$1,000 upon being blackmailed. Suppose she wrongly predicts payment with probability $\varepsilon$. Intervening on $\textsc{fdt}(\cdot,\textit{blackmail})$:

$$
\text{pay: } -1{,}000 \quad(\text{always blackmailed}),\qquad \text{refuse: } -\varepsilon\cdot 1{,}000{,}000 .
$$

A-FDT refuses iff $\varepsilon < 0.001$. The paper's example $\varepsilon=0.0009$ gives $-\$900 > -\$1{,}000$, so the agent refuses, as stated.

The paper then says that at "0.011%" the agent pays. By the same arithmetic, $\varepsilon = 0.00011$ gives $-\$110$, and refusal still wins. The intended figure was presumably 0.11%, which gives $-\$1{,}100 < -\$1{,}000$. The general lesson is that A-FDT's verdict depends on a threshold, here $\varepsilon^\ast=\text{cost of paying}/\text{damage}$, not on what the letter reveals about this particular world.

The paper's XOR blackmail is handled the same way. The $\textsc{fdt}(\cdot,\textit{letter})$ node affects whether the letter is sent but has no arrow to $\textsc{Infestation}$. A-FDT therefore refuses, as CDT does, though for a different reason. EDT pays.

### 5.5 Death in Damascus

Death predicts perfectly, and fleeing costs \$1,000. The $\textsc{fdt}$ node feeds both $\textsc{Act}$ and Death's appointment book. Under either intervention the agent dies, and fleeing adds the \$1,000 loss, so A-FDT stays.

There is no instability and no ratification. CDT, by contrast, cycles: each belief about its own choice recommends the other city.

The paper also discusses a truly random coin that Death cannot predict, offered for \$1. In the natural A-FDT model, that coin is a node with no arrow from $\textsc{fdt}$, so buying it is worth about $0.5\times 10^6 - 1$. The paper's analysis implies that CDT declines the coin. My modelling inference is that A-FDT accepts it.

## 6. What the source leaves open, and how to proceed

### 6.1 Where $G$ comes from

This is the largest gap, and the paper says so: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

The cleaner formulation would be a $\mathtt{true}$ operator that updates $P$ on a counterpossible: "if, contrary to fact, this function output $a$." The paper admits "it's not clear how to define a $\mathtt{true}$ operator." Equation (4) sidesteps the problem by taking $G$ as given input, just as CDT takes its causal graph as given.

A-FDT is therefore precisely defined only *relative to* a graph. Two agents with the same beliefs but different $G$ can disagree. My working criterion, which follows the paper's calculator analogy but is not a theorem of the paper, is to draw $\textsc{fdt}\to Z$ exactly when $Z$ is produced by a process that *computes* the agent's decision function on the relevant input, or computes an accurate model of it. Prediction error should be modelled as exogenous noise. This yields the paper's graphs in all its examples. Hard cases remain, such as partial algorithmic similarity, or a predictor using crude statistics instead of simulation. For these the criterion gives no sharp answer, and the source does not supply one.

### 6.2 The values of the other decision nodes

In every two-node example, the paper introduces a prior $q$ on the output of the *non*-intervened decision node. It remarks that the "correct" value is 0 or 1 "as you may verify" but that it "doesn't matter." In those examples it genuinely does not matter. In general it can.

Equation (4) is silent on how $q$ should be set, because it intervenes on one node at a time. A natural proposal, which is mine, is to require **self-consistency**. Compute A-FDT for every input $y$, set each node's prior to the computed output, and seek a fixed point. Multiple fixed points may exist, and the paper offers no selection rule.

### 6.3 Why "action" matters: A-FDT versus policy FDT

Policy FDT intervenes on a single node whose values are maps $\pi:\mathcal X\to\mathcal A$, chooses the best $\pi$, and applies it to $x$. The source says the difference "makes a difference in certain multi-agent dilemmas" but sets it aside.

Here is my own illustration. Two copies of one algorithm are shown different labels, *red* and *blue*. Each picks L or R, and both receive \$1 iff they pick *different* letters. Under A-FDT, the red copy intervenes on $\textsc{fdt}(\cdot,\textit{red})$ while the blue-node keeps its prior $q=P(\text{blue}\mapsto L)$. Choosing L earns $1-q$ and choosing R earns $q$. With symmetric priors the red copy is indifferent, and the outcome rests on tie-breaking or on the fixed-point question of §6.2. Policy FDT simply selects $\pi=\{\textit{red}\mapsto L,\textit{blue}\mapsto R\}$ and guarantees \$1.

So A-FDT is fully determinate when the payoff-relevant dependencies all run through the single node for the actual input. When outputs on several inputs must be *jointly* chosen, the answer may depend on the unresolved $q$'s.

### 6.4 Smaller gaps

The paper does not address:

- tie-breaking;
- whether mixed actions belong in $\mathcal A$;
- how a bounded agent should approximate (4). It argues only that bounded approximations should inherit the idealized theories' relative strengths.

It also uses an informal notion of "fair problems": dilemmas where "the outcome depends only on the agent's behavior in the dilemma at hand." The paper concedes this notion lacks a formal definition.

## 7. Philosophical motivation

**Subjunctive dependence.** Two well-functioning calculators computing $6288+1048$ agree. This is not because one causes the other. It is because both are constrained by the same arithmetic fact. On the paper's view, a predictor's accurate model of you stands to you as one calculator to the other. The paper states the analogy directly: "FDT is to subjunctive dependence as causal decision theory is to causal dependence." Causal dependence is a special case of subjunctive dependence, and merely statistical correlation is not a case at all.

**Too many versus too few correlations.** EDT's hypotheticals keep every correlation, including the lesion's, and so EDT "manages the news." CDT's hypotheticals cut every non-causal correlation, including the predictor's. The result is that CDT imagines "hypothetical scenario[s] in which a perfect predictor made an incorrect prediction." A-FDT keeps exactly those correlations that run through its own decision function.

**Dominance is theory-relative.** The CDT dominance argument for two-boxing holds the prediction fixed while the action varies, which is just CDT's way of forming hypotheticals. If instead one holds the subjunctive dependency fixed, one-boxing is undominated. The paper concludes that "every method for constructing hypotheticals gives rise to its own notion of dominance," so dominance cannot neutrally decide between theories. Utility achieved is the criterion it prefers.

**Precommitment and reflective stability.** Agents following CDT or EDT would pay for a binding precommitment to one-box in transparent Newcomb, or to refuse blackmail. A-FDT already acts as such a precommitment would dictate. The paper reports that it is, "so far as we know, reflectively stable in fair problems," and that it assigns non-negative value to information. EDT, by contrast, would pay to blindfold itself.

**The "control" objection.** One may object that no agent can "control" a mathematical fact. The paper replies that a deterministic CDT agent equally cannot do otherwise than it does. Both theories evaluate imagined alternatives that will not occur. The question is which imagined alternatives track the structure of the world.

## 8. Conclusion

A-FDT is Equation (4): maximize expected utility under Pearl's $\mathtt{do}$ applied to the node representing *one's own decision function's output on the actual input*. The world-model's graph must route that node to everything that computes or accurately predicts it.

The rule has two operative features. It intervenes on the type instead of the token. And observations select the intervention node instead of being conditioned on. Together these yield one-boxing in Newcomb's problem, smoking in the lesion problem, one-boxing even before full transparent boxes, refusal under blackmail (with a computable error threshold), and stable behaviour in Death in Damascus.

The theory is exact *given* $P$ and $G$. Its open edges are three: how to construct $G$ (the counterpossible problem), how to set priors on decision nodes for other inputs, and the action-level restriction that separates A-FDT from the authors' preferred policy FDT. For problems where all relevant dependence runs through the single node for the actual input, the recipe in §4 decides cases mechanically. For multi-input coordination, users should either adopt a self-consistency assumption, flagged as such, or move to policy FDT.

**Reference.** Yudkowsky, E. and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060v2. (Cited works such as Gibbard & Harper 1978, Joyce 1999, and Pearl 2000 are as referenced there.)