# A-FDT: Choosing as the Output of a Function

## 1. What A-FDT is

Decision theorists in the Newcomb tradition largely agree on one formula: choose the act that maximizes expected utility. They disagree about which probabilities belong inside it. Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* proposes a third answer, alongside evidential decision theory (EDT) and causal decision theory (CDT). An agent should treat her decision as the output of a fixed mathematical function and ask, in the abstract's words, "Which output of this very function would yield the best outcome?"

This essay concerns the version formalized as Equation (4) in Section 5 of that paper. There the maximization ranges over **actions**: the agent intervenes on a node representing her decision function's output on her actual input, and sets it to each candidate action in turn. I call this **A-FDT** (action functional decision theory). The paper itself simply writes "FDT". The label matters because two footnotes (7 and 16) say the authors' *preferred* formalization iterates over **policies**, meaning maps from observations to actions. I will call that variant **policy-FDT**. The label is mine, not the paper's. The two variants diverge in some cases, and Section 7 constructs one.

Throughout, I separate three things: what the source says, what follows from it, and what I add as operational proposals.

## 2. The common frame: expected utility with a free "hypothetical" connective

The paper starts from a schema drawn from Gibbard and Harper:

$$
\mathcal{EU}(a) := \sum_{j} P(a \hookrightarrow o_j;\, x)\cdot \mathcal U(o_j). \tag{1}
$$

Here $x$ is the observation history, and $P(a\hookrightarrow o_j; x)$ is the probability of outcome $o_j$ "in the hypothetical scenario where the action $a$ is executed after receiving observations $x$." Following Joyce, the paper treats the connective $\hookrightarrow$ as the free parameter that distinguishes rival expected-utility theories. Joyce puts it this way: they "disagree about the epistemic perspective from which actions are to be evaluated."

Operationally, the agent holds a world-model $M$. For each act $a$ she builds a *hypothetical* $M^{a\hookrightarrow}$, scores it, and takes the best. The paper insists that hypotheticals are "decision-theoretic instruments constructed from beliefs", like "notes on scratch paper", and not claims about real possible worlds.

The two baselines are as follows. Write $V := \mathcal U(\textsc{Outcome})$.

- **EDT** conditions: $\arg\max_a \mathbb E(V\mid \textsc{Obs}=x, \textsc{Act}=a)$.
- **CDT** (in Pearl's formulation) intervenes on the physical act and conditions on observations: $\arg\max_a \mathbb E(V\mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x)$.

## 3. The definition

A-FDT requires a richer model. $P$ must contain variables for the outputs of mathematical functions, including a variable for the output of the agent's own decision procedure. $G$ is a graph that records not only causal structure but "the logical, mathematical, computational, causal, etc. structure of the world more broadly." Equation (4) then reads:

$$
\text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big). \tag{4}
$$

The underlines denote *dequoting*. $\textsc{fdt}(\underline P,\underline G,\underline x)$ is the name of a variable in the model. That variable represents what the decision function outputs when it is run on these very inputs. The agent does not need to know its value in order to represent it, and the paper appeals to Kleene's recursion theorem ("quining") to argue that the self-reference is harmless. For brevity I write $F_x$ for this node.

The paper names exactly two differences from CDT:

1. The point of intervention is a node for the *output of the decision procedure* (the type), not the physical act (the token).
2. "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon."

The paper's slogan for the resulting relation is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

**Subjunctive dependence.** Two physical systems that compute the same function, such as two working calculators summing $6288+1048$, have outputs that depend "subjunctively" on that function. A reliable predictor contains a model of the agent's function, so its prediction depends on $F_x$. A lesion that merely correlates with smoking does not. Ordinary causal dependence is a special case of subjunctive dependence. Mere correlation, such as two calculators that happen to be pink, is not.

**The procedure, step by step.** This is my reconstruction, faithful to Eq. (4):

1. Build $(P,G)$ with a node $F_{x'}$ for each input $x'$ on which some system in the world runs or models your procedure. Let $\textsc{Act}$ depend on whichever $F_{x'}$ corresponds to the input you actually receive.
2. Draw arrows from $F_{x'}$ to every variable whose mechanism computes or reliably predicts that output.
3. For each $a$, perform $\mathtt{do}(F_x=a)$ on your *actual* input $x$. Propagate downstream, leave everything else at its prior, and compute $\mathbb E V$.
4. Output the maximizer.

The CDT and A-FDT hypotheticals are both surgeries that preserve some correlations and sever others. CDT preserves only correlations caused by the act. A-FDT preserves every correlation that flows from the function's output. When every correlate of the act is downstream of it, the paper shows that the three theories agree:

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(F=a)].$$

## 4. Worked examples

All dollar figures stand in for utility, as in the source.

**Psychological twin prisoner's dilemma.** Both twins' acts are children of the same node $F$. $\mathtt{do}(F=C)$ yields mutual cooperation, worth $\$1{,}000{,}000$. $\mathtt{do}(F=D)$ yields mutual defection, worth $\$1{,}000$. A-FDT cooperates. CDT severs the twin's act from the agent's and defects by dominance.

**Newcomb's problem (99% accurate predictor).** In the graph, $F$ points to both $\textsc{Act}$ and $\textsc{Prediction}$, and $\textsc{Accurate}$ is an independent noise parent of $\textsc{Prediction}$:

$$
\begin{aligned}
\mathbb E[V\mid\mathtt{do}(F=\textit{onebox})] &= 0.99(10^6)+0.01(0)=\$990{,}000,\\
\mathbb E[V\mid\mathtt{do}(F=\textit{twobox})] &= 0.01(1{,}001{,}000)+0.99(1{,}000)=\$11{,}000.
\end{aligned}
$$

A-FDT one-boxes. (The source's text gives \$999,000 for Eve's EDT value, but the same arithmetic yields \$990,000. Nothing turns on this.) CDT's $\mathtt{do}(\textsc{Act})$ leaves $P(\textit{full})=p$ fixed, so two-boxing wins by \$1,000 for every $p$.

The paper anticipates an objection: if Fiona is nearly sure the box is full, why not grab both? Its reply is that asking what *would* happen if she two-boxed means imagining the FDT algorithm outputting *twobox*. In that counterpossible world the predictor, which models the same function, predicted differently. No retrocausation is invoked.

**Smoking lesion.** Here the graph has no arrow from any $F$ node to $\textsc{Cancer}$. The paper formalizes the lesion as altering the agent's utility function. Fiona does not know whether she is running $\text{A-FDT}(P_S,G)$ (a smoker's utilities) or $\text{A-FDT}(P_R,G)$, so $\textsc{Act}$ copies $F_S$ under *lesion* and $F_R$ otherwise. Intervening on $F_S$ leaves $P(\textit{lesion})=p$ untouched, and smoking beats refraining by $p\cdot\$1{,}000$. A-FDT smokes.

This example shows something easy to miss. The agent intervenes on the node indexed by her *actual* inputs even when she cannot introspect which node that is. The node's influence is weighted by the probability that it controls her body.

**Transparent Newcomb, observing a full box.** This is where Eq. (4)'s treatment of observation does real work. The graph has $F_{\textit{full}}\to\textsc{Prediction}$, and $\textsc{Prediction}$ selects whether $F_{\textit{full}}$ or $F_{\textit{empty}}$ sets $\textsc{Act}$. Let $q=P(F_{\textit{empty}}=\textit{twobox})$:

$$
\begin{aligned}
\mathbb E[V\mid\mathtt{do}(F_{\textit{full}}=\textit{onebox})] &= 0.99(10^6) + 0.01(1{,}000q) = 990{,}000+10q,\\
\mathbb E[V\mid\mathtt{do}(F_{\textit{full}}=\textit{twobox})] &= 0.01(1{,}001{,}000)+0.99(1{,}000q)=10{,}010+990q.
\end{aligned}
$$

(The source prints the second line as "\$110,00", evidently a typesetting slip.) For every $q\in[0,1]$ one-boxing wins, even though the agent sees a full box. The calculation includes the branch in which the box is empty. So the agent does **not** condition on her observation; she only uses it to select $F_{\textit{full}}$.

**Parfit's hitchhiker** has the same structure, with $F_{\textit{in city}}=\textit{pay}$ playing the role of one-boxing. A-FDT pays the driver. Both CDT and EDT refuse and are left in the desert.

**XOR blackmail (infallible predictor, $P(\textit{termites})=p$).** The letter arrives iff (no termites and the agent pays on receiving it) or (termites and the agent does not pay):

$$
\begin{aligned}
\mathtt{do}(F_{\textit{letter}}=\textit{pay}) &: \ -p\cdot 10^6-(1-p)\cdot 10^3,\\
\mathtt{do}(F_{\textit{letter}}=\textit{refuse}) &: \ -p\cdot 10^6 .
\end{aligned}
$$

A-FDT refuses. The intervention changes whether the letter arrives, but it never touches the termites. EDT, conditioning on the letter, pays.

**Mechanical blackmail.** With error rate $\varepsilon$, a refuser is blackmailed only by mistake, losing $\varepsilon\cdot10^6$ in expectation. A payer is reliably blackmailed and loses $10^3$. A-FDT refuses iff $\varepsilon<10^{-3}$. The paper's example $\varepsilon=0.0009$ correctly yields refusal. Its contrasting "0.011%" is below the threshold, so as printed it would also yield refusal, not payment. The intended figure was presumably $0.11\%$.

**Death in Damascus (perfect predictor).** $F$ determines both the agent's location and the entry in Death's appointment book. Every hypothetical ends in death, so the only difference is the \$1,000 travel cost. A-FDT stays put, stably. CDT oscillates as described by Gibbard and Harper. With Joyce-style ratification it randomizes nearly 50/50, and it even declines a truly random coin that would give a genuine 50% survival chance for \$1.

## 5. Dominance and reflective stability

The source argues that "dominance" is always defined relative to some way of constructing hypotheticals. Two-boxing dominates only under CDT's surgery, where the act changes while the predictor's model of the function is held fixed. The paper likens this to imagining a working calculator outputting a wrong sum.

A-FDT has its own dominance notion: hold the subjunctive dependencies fixed and vary the function's output. By that standard it never picks a dominated option. On this view, dominance cannot adjudicate neutrally between theories, so the authors appeal to utility achieved in "fair" problems. These are problems in which outcomes depend only on the agent's behavior in the dilemma, not on which procedure produced it.

They also argue that A-FDT agents "act as they would have precommitted to act." Such agents have no reason to self-modify, unlike CDT agents, who would bind themselves before a Newcomb problem if they could. And A-FDT agents never assign negative value to information, unlike EDT agents, who would pay to blindfold themselves.

## 6. Where the source is underdetermined

### 6.1 Constructing $G$

Equation (4) takes $G$ as given. The paper is explicit: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." It also offers no account of the $\mathtt{true}$ operator, the counterpossible conditioning that $G$ is meant to approximate.

So A-FDT's verdicts are only as determinate as the modeler's judgment about which mechanisms "compute or model" the agent's function. In clean cases (simulators, twins, copies of the source code) this is easy. In murky cases it is not: humans predicting from character traits, functions that are similar but not identical, an agent's own future self in the paper's gym example.

**Proposal (mine).** Use a graded test. Add an arrow $F_x\to Z$ iff, holding the noise variables fixed, your credence in $Z$ would shift if you learned (counterpossibly) that the function's output on $x$ were different. Equivalently, ask whether $Z$'s mechanism takes the function's output as an input. Imperfect predictors fit this test naturally: the arrow is present and the imperfection lives in noise parents, as $\textsc{Accurate}$ does in the source's examples. Statistical correlations that would persist under any output of the function (lesions, pink calculators) get no arrow.

### 6.2 Observations: intervene, do not condition

Eq. (4) contains no "$\mid \textsc{Obs}=x$". However, the transparent Newcomb section writes $\mathbb E(V\mid \mathtt{do}(F_{\textit{full}}=a, \textsc{Obs}=\textit{full})$, with an unclosed parenthesis. Read literally, that would conditionalize on the observation. But the calculation that immediately follows does not condition: it averages over the empty-box branch. Section 5 also says observation is handled by "changing which node it intervenes upon". And a footnote warns that Timeless Decision Theory, which conditions *and* switches nodes, suffers a harmful "double update."

**Interpretation (mine, but strongly supported).** In A-FDT, $x$ affects the computation *only* through the index of the intervened node. The distribution $P$ is the agent's epistemic state *before* the observations on which relevant predictors key.

This leaves a residual ambiguity. The paper elsewhere describes $M$ as possibly "updated on her observations thus far." A workable operational rule is to update $P$ on everything that no modeled system's behavior depends on the agent's response to, and to pass everything else as $x$. Getting this split wrong reintroduces the double update.

### 6.3 Beliefs about one's own other nodes

Under $\mathtt{do}(F_x=a)$, the nodes $F_{x'}$ for $x'\neq x$ stay at their priors. These are parameters like $q$ above. In the source's examples, $q$ never changes the verdict, and the paper says it "doesn't matter." In general it can matter, and the paper gives no rule for setting it. One natural option, my own, is to set $P(F_{x'}=\cdot)$ by actually running A-FDT on $x'$ when that is tractable, and to iterate toward a fixed point otherwise.

### 6.4 Ties and tractability

The argmax may be a set, and the paper specifies no tie-breaking rule. Ties do not create the zero-probability pathology that EDT faces, because $\mathtt{do}$ is defined even for acts with prior probability zero. The paper also concedes that exact maximization over realistic models is intractable. It expects bounded approximations to inherit the relative strengths of the idealized theory.

## 7. A-FDT versus policy-FDT

The footnotes say that intervening on policies rather than actions "makes a difference in certain multi-agent dilemmas." The paper does not give such a case, so here is one of my own.

A host runs your exact procedure twice, once on input $x$ and once on input $y$. You actually receive $x$; a copy of you receives $y$. You receive 10 if both runs output $L$, 5 if both output $R$, and 0 otherwise. Suppose your prior is $P(F_y=L)=0.3$. Then A-FDT compares:

$$\mathtt{do}(F_x=L):\ 10(0.3)=3, \qquad \mathtt{do}(F_x=R):\ 5(0.7)=3.5,$$

and chooses $R$. If the copy reasons symmetrically, the pair coordinates on the worse equilibrium $(R,R)$. Policy-FDT intervenes on the whole map $\pi:\{x,y\}\to\{L,R\}$, sees that $\pi=(L,L)$ yields 10, and then applies $\pi(x)=L$.

The general point is this. A-FDT optimizes each input's output while holding the function's behavior on other inputs at its prior. That is a coordinate-wise optimization, and it can lock into inferior equilibria whenever the function's outputs on different inputs interact. Policy-FDT optimizes jointly. The fixed-point suggestion in 6.3 does not fully close the gap, since the bad equilibrium $(R,R)$ is itself a fixed point.

## 8. Philosophical motivation in brief

The paper frames its case around three arguments. The first is **utility**: A-FDT agents reliably get rich in Newcomb's problem, survive Parfit's desert, and deter blackmailers. The second is **precommitment**: they behave as CDT and EDT agents would bind themselves to behave. The third is **value of information**, noted in Section 5.

To the charge that A-FDT agents believe they "control" mathematical facts or the past, the paper replies with parity. A deterministic CDT agent equally imagines its single physically possible act varying. "Any principled objection to the idea that FDT agents can 'control' their decision type will also imply that (deterministic) CDT agents cannot 'control' their decision token."

The costs are acknowledged. A-FDT relies on counterpossible reasoning that currently has no formal theory, and on a notion of fairness that has not been made precise. The paper's own footnote example shows the difficulty: a host that punishes whoever matches a copy of Fiona.

## 9. Conclusion

A-FDT is CDT's surgical method aimed at a different target. It intervenes on a node representing *the output of one's own decision function on one's actual input*, it propagates that change through every subjunctively dependent variable, and it does not condition on observations. Given a correct dependency graph, the rule mechanically yields a single set of verdicts: one-box, smoke, cooperate with a twin, pay the driver, refuse both blackmailers, and stay in Damascus.

Its genuine open joints are four:

- how to build $G$, which the source calls the largest open problem;
- the exact division between what belongs in $P$ and what is passed as $x$;
- how to set beliefs about one's outputs on other inputs;
- the action-versus-policy choice, where A-FDT can fail to coordinate across one's own copies.

A reader who can draw the graph can apply Eq. (4) to an unfamiliar case. A reader who cannot will find that the theory has relocated the hard question, not dissolved it.

**References**

- Yudkowsky, E. & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060.
- Gibbard, A. & Harper, W. (1978). "Counterfactuals and Two Kinds of Expected Utility."
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*.
- Pearl, J. (2000). *Causality*.