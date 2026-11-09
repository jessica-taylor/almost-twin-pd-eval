# Intervening on the Type: A Mathematical Guide to A-FDT

## 0. What "A-FDT" names

Yudkowsky and Soares (2017) introduce *functional decision theory* as a rule that treats one's decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" They give a formal version as Equation (4) in Section 5. In that equation the variable the agent manipulates is a node whose value is an **action**. Two footnotes (7 and 16) say that the authors' *preferred* formalization instead selects a **policy**, meaning a map from observations to actions. They add that the difference "only matters in multi-agent dilemmas so far as we can tell."

This essay concerns the action-valued version, Equation (4). I call it **A-FDT**. When I mean the policy-selecting variant, I call it **policy-FDT**. I use CDT for causal decision theory and EDT for evidential decision theory. Claims attributed to "the paper" or "the source" are theirs. Claims flagged as *proposals* are mine.

## 1. The common frame: expected utility with a free connective

All three theories in the paper maximize

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}
$$

Here $a$ ranges over a finite action set $\mathcal A$, $x$ is the observation history, and $o_j$ ranges over outcomes. The connective $\hookrightarrow$ reads "in the hypothetical where $a$ is done." Following Joyce (1999), the paper treats the meaning of $\hookrightarrow$ as the free parameter that distinguishes decision theories. In Joyce's words, quoted by the paper, theories disagree "about the epistemic perspective from which actions are to be evaluated."

The paper describes this procedurally. The agent has a world-model $M$. For each action she builds a *hypothetical* $M^{a\hookrightarrow}$, scores it, and acts on the best one. The paper insists hypotheticals "are not themselves beliefs; they are decision-theoretic instruments constructed from beliefs." Each theory then makes two choices: what $M$ must contain, and what surgery turns $M$ into $M^{a\hookrightarrow}$.

Write $V := \mathcal U(\text{Outcome})$. The three rules are as follows.

**EDT (Eq. 2)** conditions on the action, ignoring actions of probability 0:
$$\mathrm{EDT}(P,x) = \arg\max_{a} \mathbb E\big(V \mid \text{Obs}=x,\ \text{Act}=a\big).$$

**CDT (Eq. 3)** performs Pearl's intervention on the physical act, using a causal graph $G$:
$$\mathrm{CDT}(P,G,x) = \arg\max_{a} \mathbb E\big(V \mid do(\text{Act}=a),\ \text{Obs}=x\big).$$

**A-FDT (Eq. 4)** intervenes on a different node:
$$
\boxed{\ \mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; do\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big)\ } \tag{4}
$$

## 2. Reading Equation (4)

### 2.1 The intervened node

$\textsc{fdt}(\underline P,\underline G,\underline x)$ is a random variable in the agent's own model. It represents *the output of the A-FDT algorithm when run on inputs $(P,G,x)$*. The underlines denote dequoting: the node's *name* is built from the actual inputs. The model therefore contains a variable about the very computation that is using the model.

The paper defends this self-reference in two ways. First, an agent does not need to know the *value* of a variable in order to represent it. Second, Kleene's recursion theorem shows such self-describing data structures can be built ("quining"). The model may contain many such nodes, one for each input the function might receive: $\textsc{fdt}(\underline P,\underline G,\textit{full})$, $\textsc{fdt}(\underline P,\underline G,\textit{empty})$, and so on.

### 2.2 The graph $G$ encodes subjunctive dependence

In CDT, $G$ is a causal graph. In A-FDT, $G$ must tell us "how changing a logical variable affects all other variables." The organizing slogan is:

> "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

Two physical systems that compute the same function both *subjunctively depend* on that function. The paper gives two illustrations. Two working calculators computing $6288+1048$ both depend on its value. A predictor that models your decision procedure depends on that procedure's output. Ordinary causal dependence is a special case: a scribe copying a calculator's output depends on that output. Mere statistical correlation is not subjunctive dependence. Two calculators that happen to be pink do not depend on each other's colour.

In graph terms, $G$ has an edge from an $\textsc{fdt}$ node into every variable whose mechanism *implements or models* that computation. That always includes the agent's own $\text{Act}$, and it includes predictors, twins, and simulations. It has no edges into variables that are merely correlated with the agent's behaviour through common causes.

### 2.3 Pearl's $do$, applied to a logical variable

Given $G$, the $do$ operator works as usual. It sets the node, severs the node's incoming dependencies, recomputes everything downstream, and leaves everything else at its prior distribution. The paper describes the ideal operation as a $\mathtt{true}(\phi)$ operator that updates on a possibly false logical sentence. It admits "it's not clear how to define a $\mathtt{true}$ operator," and uses the graph-plus-$do$ construction as a substitute. The hypotheticals are therefore openly *counterpossible*. If A-FDT in fact outputs *onebox*, the hypothetical in which it outputs *twobox* is a logically impossible world. The agent reasons about it anyway, as a mathematician reasons about what would follow if a conjecture were false.

### 2.4 Observations change the intervention point

Equation (4) contains no conditioning on $\text{Obs}=x$. The paper states the contrast with CDT directly:

> "When CDT's observation history updates from $x$ to $y$, CDT changes from conditioning its model on $\text{Obs}=x$ to conditioning its model on $\text{Obs}=y$, whereas FDT changes from intervening on the variable $\textsc{fdt}(\underline P,\underline G,\underline x)$ to $\textsc{fdt}(\underline P,\underline G,\underline y)$ instead."

This single feature produces A-FDT's most distinctive verdicts, which are those in the transparent Newcomb and blackmail problems. The hypothetical in which the agent acts differently may also be one in which she *would have observed something else*.

### 2.5 When the three theories agree

The paper notes that the three theories agree whenever every correlation between $\text{Act}$ and other variables is caused by $\text{Act}$, apart from $\text{Act}$'s own dependence on the $\textsc{fdt}$ node. In that case
$$\mathbb E[V\mid a] = \mathbb E[V\mid do(a)] = \mathbb E[V\mid do(\textsc{fdt}=a)].$$
Divergence requires something other than the agent's body that tracks her decision function, or a correlation that is not caused by her act.

## 3. A recipe for applying A-FDT

The source supplies the equation and worked graphs. The following recipe is my organization of what it does in its examples.

1. **List the possible inputs.** These are the observation histories $y\in\mathcal X$ the agent might be in at decision time, including histories that some predictor might consider.
2. **Create one node per relevant input**, $F_y := \textsc{fdt}(\underline P,\underline G,\underline y)$, with values in $\mathcal A$.
3. **Wire the body.** $\text{Act}$ is a deterministic function that selects which $F_y$ controls it, according to the observation the world actually delivers. For example, $\text{Act}=F_{\textit{full}}$ if the box is full and $F_{\textit{empty}}$ otherwise.
4. **Wire the dependents.** Any predictor, twin, or simulation that computes or models $F_y$ gets an edge from $F_y$. Model imperfect predictors with an independent noise node, such as *Accurate*.
5. **Leave mere correlates alone.** Lesions, genes, and background states connect to $\text{Act}$ only through their real causal role, for instance by determining which decision function the body runs. They receive no edge from the $F_y$.
6. **Assign priors** to exogenous nodes and to the $F_{y'}$ for $y'\neq x$.
7. **Evaluate.** For each $a$, compute $\mathbb E[V\mid do(F_x=a)]$ in the unconditioned model and take the argmax.

## 4. Worked examples

All payoffs below are utilities in dollar units.

### 4.1 Newcomb's problem and the twin prisoner's dilemma

A 99%-reliable predictor fills box B with \$1,000,000 iff she predicts one-boxing. Box A holds \$1,000. Fiona, the paper's A-FDT agent, has a graph in which $F=\textsc{fdt}(\underline P,\underline G)$ feeds both $\text{Act}$ and $\text{Prediction}$. *Accurate* feeds $\text{Prediction}$ with $P(\textit{accurate})=0.99$.

| Intervention | Value |
|---|---|
| $do(F=\textit{onebox})$ | $0.99\times 1{,}000{,}000 + 0.01\times 0 = 990{,}000$ |
| $do(F=\textit{twobox})$ | $0.01\times 1{,}001{,}000 + 0.99\times 1{,}000 = 11{,}000$ |

A-FDT one-boxes. CDT intervenes on $\text{Act}$, which is *not* upstream of $\text{Prediction}$. The probability $p$ that box B is full is therefore the same in both of its hypotheticals, and two-boxing wins by \$1,000 for every $p$.

The twin prisoner's dilemma has the same structure. A single $F$ node feeds both one's own act and the twin's act. Cooperating yields $1{,}000{,}000$ and defecting yields $1{,}000$, so A-FDT cooperates.

A common worry is this: if Fiona is nearly sure she one-boxes, and so nearly sure the box is full, why not grab the extra \$1,000? The answer is that $do(F=\textit{twobox})$ changes the predictor's input as well. In her own hypothetical, two-boxing is a world in which the box is probably empty. The paper stresses that this involves no retrocausation. No signal travels back in time. A logical variable that was always shared simply takes a different value.

### 4.2 The smoking lesion

A lesion causes both a taste for smoking and, with probability 0.99, fatal cancer. Smoking itself is harmless and worth \$1,000 to those who like it. The paper models the taste as two utility functions, $\mathcal U_S$ for smoke-likers and $\mathcal U_R$ for refrainers. These give two world-models, $P_S$ and $P_R$, and two decision nodes, $F_S$ and $F_R$. The lesion selects which node drives $\text{Act}$:
$$\text{Act}(\textit{lesion},s,r)=s,\qquad \text{Act}(\textit{nolesion},s,r)=r.$$
Cancer depends on the lesion only. No edge runs from $F_S$ to Cancer, because the lesion is not evaluating anyone's algorithm.

Let $p=P(\textit{lesion})$, and let $q$ be Fiona's prior that $F_R$ outputs *smoke*. Running $F_S$, she computes:
$$\begin{aligned}
\mathbb E[V\mid do(F_S=\textit{smoke})] &= p(10{,}000+1{,}000) + (1-p)(990{,}000+1{,}000q),\\
\mathbb E[V\mid do(F_S=\textit{refrain})] &= p(10{,}000) + (1-p)(990{,}000+1{,}000q).
\end{aligned}$$

Smoking wins by $1{,}000\,p$. A-FDT therefore smokes and one-boxes, which is the combination Gibbard and Harper (1978) argued no single rational rule could recommend. The difference from Newcomb's problem lies entirely in $G$: a predictor gets an edge from $F$, and a lesion does not.

The paper itself recommends abandoning this dilemma as "badly confused." The example still shows how A-FDT handles uncertainty about *which* function one is.

### 4.3 The transparent Newcomb problem

Both boxes are transparent. The predictor fills B iff she predicts the agent will one-box *upon seeing B full*. Suppose Fiona sees B full. She intervenes on $F_{\textit{full}}$. In her graph, $\text{Prediction}$ depends on $F_{\textit{full}}$ and *Accurate*, and $\text{Act}$ equals $F_{\textit{full}}$ or $F_{\textit{empty}}$ according to the box's contents. Let $q$ be her prior that $F_{\textit{empty}}$ outputs *twobox*.

| Intervention | Value |
|---|---|
| $do(F_{\textit{full}}=\textit{onebox})$ | $0.99(1{,}000{,}000) + 0.01(1{,}000q) = 990{,}000+10q$ |
| $do(F_{\textit{full}}=\textit{twobox})$ | $0.01(1{,}001{,}000) + 0.99(1{,}000q) = 10{,}010+990q$ |

(The printed source shows the second figure as "\$110,00", an evident typo for \$10,010.)

A-FDT one-boxes for every $q\in[0,1]$, even while looking at \$1,000,000. When she evaluates *twobox*, her hypothetical says she would most likely have been shown an empty box. These are the same sums as in Parfit's hitchhiker, where paying the driver corresponds to one-boxing. The paper argues that the two problems should be judged alike.

### 4.4 Blackmail

**XOR blackmail.** A perfect predictor sends a letter iff exactly one of two things holds: (i) there are no termites and the agent will pay \$1,000 on receiving the letter, or (ii) there are termites and the agent will not pay. Termite damage is \$1,000,000. Let $t=P(\textit{termites})$, which no $F$ node affects.

- **$do(F_{\textit{letter}}=\textit{pay})$.** With no termites, the letter comes and she pays, for $-1{,}000$. With termites, no letter comes, for $-1{,}000{,}000$. Total: $-1{,}000(1-t) - 1{,}000{,}000\,t$.
- **$do(F_{\textit{letter}}=\textit{refuse})$.** With no termites, no letter comes, for $0$. With termites, the letter comes and she refuses, for $-1{,}000{,}000$. Total: $-1{,}000{,}000\,t$.

Refusal wins by $1{,}000(1-t)$. EDT pays, because conditioning on paying drives the probability of termites to zero.

**Mechanical blackmail.** A predictor runs a damaging program, costing \$1,000,000 unless the agent pays \$1,000, only if she predicts the agent would pay. Suppose a refuser is nevertheless blackmailed with error rate $\varepsilon$. Then
$$\mathbb E[V\mid do(F=\textit{pay})] = -1{,}000,\qquad \mathbb E[V\mid do(F=\textit{refuse})] = -1{,}000{,}000\,\varepsilon.$$

A-FDT refuses iff $\varepsilon < 0.001$. That matches the paper's verdict of refusal at $\varepsilon = 0.0009$. The paper says Fiona pays at "0.011%"; given the threshold, this is presumably a slip for 0.11%. The verdict holds *even while she holds the letter and knows the prediction was wrong*. The paper bites this bullet explicitly.

### 4.5 Death in Damascus

Death perfectly predicts the agent and waits where she will be. Fleeing costs \$1,000.

- $do(F=\textit{Damascus})$: Death is in Damascus, giving $0$.
- $do(F=\textit{Aleppo})$: Death is in Aleppo, giving $-1{,}000$.

A-FDT stays, stably. CDT holds Death's location fixed while varying the act, so its preferred option flips with every update of its self-prediction. The paper further argues that CDT would refuse to pay \$1 for a genuinely random coin that gives a 50% chance of escape.

## 5. What the source leaves open, and some operational proposals

### 5.1 Where $G$ comes from

The paper is candid:

> "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

Equation (4) is a function of $(P,G,x)$. Every verdict above flows from which edges leave the $F$ nodes. Two analysts who disagree about whether some process "models my decision function" will get different A-FDT prescriptions.

*Proposal.* For practical cases, draw an edge $F_y\to Z$ when $Z$'s mechanism takes as input a representation of the agent's decision procedure, or of its behaviour on input $y$, that is reliable enough to track counterfactual changes in that behaviour. Predictors trained on the agent, simulations, copies, and one's own future selves facing the same input qualify. Bare population-level correlates do not. Graded reliability goes into a noise node, such as *Accurate*, rather than into a weaker edge. This reproduces every graph in the paper, but it is my heuristic, not the paper's definition. Hard cases remain, such as partial similarity between agents who run *related but non-identical* functions. The paper's gym example, where one assumes one's future selves will act alike "if there are no relevant differences," shows that the authors expect such judgments to be made, but it gives no metric for them.

### 5.2 Conditioning on the observation

Equation (4) as printed omits $\text{Obs}=x$. In the transparent Newcomb section, however, the paper writes the objective as $\mathbb E(V\mid do(\textsc{fdt}(\underline P,\underline G,\textit{full})=a,\ \text{Obs}=\textit{full})$, with an unbalanced parenthesis. Read literally, the expected value of *twobox* would then be at least \$1,001,000 and A-FDT would two-box. The paper's own arithmetic instead averages over worlds in which the box is empty.

*Proposal.* Follow Eq. (4) and the arithmetic: **do not condition on $x$.** The observation enters only by fixing which node is intervened on. This reading is supported by the paper's footnote noting that Timeless Decision Theory "prescribes both conditioning on evidence *and* changing the place where one intervenes," a "double update which proves harmful in practice."

### 5.3 Priors on the other decision nodes

In 4.2 and 4.3 the prior $q$ on non-intervened nodes did not matter. The paper calls the true value verifiable ($q=0$ and $q=1$ respectively). Whether $q$ matters in general is not settled.

*Proposal.* Require **self-consistency**: set $P(F_{y'}=a)$ to put mass on $\mathrm{FDT}(P,G,y')$ for each $y'\neq x$. If necessary, find this by iterating to a fixed point, since computing one node may require priors over the others. Where several fixed points exist, A-FDT as stated does not choose among them.

### 5.4 A-FDT versus policy-FDT

A-FDT evaluates one input at a time. It moves $F_x$ while holding the other $F_{y'}$ at their priors. Policy-FDT would choose $\pi:\mathcal X\to\mathcal A$ and intervene on all nodes jointly:
$$\pi^\* = \arg\max_\pi\ \mathbb E\big[V \mid do(F_y=\pi(y)\ \forall y)\big].$$

The two agree whenever the action-by-action optimum is consistent with the priors used for the other nodes, as in all the paper's examples. They can come apart when payoffs depend on interactions between the agent's responses to *different* inputs and the priors are not at the joint optimum. A-FDT then behaves like coordinate ascent, which can stall at a local optimum. The paper says only that such differences arise in "certain multi-agent dilemmas." My coordinate-ascent description is an interpretation, not their claim.

### 5.5 Further loose ends

- **Ties.** The argmax may return a set. No tie-breaking rule is given.
- **Certainty about one's own act.** Unlike EDT, A-FDT can evaluate actions it is sure it will not take, because $do$ does not require positive prior probability. This is what lets it escape Spohn-style traps and the cosmic-ray problem.
- **Tractability.** Eq. (4) is idealized. The paper expects bounded approximations to inherit its qualitative behaviour but proves nothing about this.
- **Scope of the optimality claim.** The paper claims superiority only in "fair" problems, where outcomes depend on the agent's behaviour rather than its algorithm. It concedes that fairness has no formal definition. Its footnote 15 exhibits a problem that is intuitively unfair to FDT ("punish anyone who takes the same action as" a copy of Fiona).

## 6. The philosophical core

A-FDT asks the agent to intervene on the **type**, her decision function on this input, rather than the **token** that is her physical act. Every correlation that runs *through* that type is preserved, and every other correlation is cut. The paper's diagnosis is that EDT "respects too many action-environment correlations, while CDT respects too few."

Several consequences follow from this one change:

- The agent acts as she would have precommitted to act, so she has no need for binding devices.
- She has no incentive to self-modify away from A-FDT, a property the paper calls reflective stability in fair problems.
- She never assigns negative value to information.

Against the dominance argument for two-boxing, the paper replies that dominance is always relative to some way of building hypotheticals. Under A-FDT's hypotheticals, two-boxing is dominated.

The cost is counterpossible reasoning. The paper answers that CDT's hypotheticals about a deterministic agent are no less impossible, so "control" is equally puzzling for both theories.

## 7. Conclusion

A-FDT is Equation (4): Pearl intervention, applied to the node representing *the output of this very algorithm on this very input*, in a graph that records subjunctive as well as causal dependence, with observations selecting the node rather than being conditioned on. Given $(P,G)$, the procedure is fully mechanical. Built that way, it one-boxes, smokes, pays the driver, refuses blackmail, and stays in Damascus.

What the source does not supply is a principled construction of $G$. It also leaves the behaviour of non-intervened decision nodes and the exact relation to the policy variant unsettled. I have suggested working answers: edges where reliable models of the agent exist, no conditioning on $x$, and self-consistent priors. These are proposals layered on a framework whose core equation is precise and whose foundations are openly incomplete.

## References

- Gibbard, A., & Harper, W. (1978). Counterfactuals and two kinds of expected utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge UP.
- Pearl, J. (2000). *Causality*. Cambridge UP.
- Yudkowsky, E., & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.