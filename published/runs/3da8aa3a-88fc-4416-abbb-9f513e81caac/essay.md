# Action Functional Decision Theory (A-FDT): Choosing the Output of Your Own Decision Function

## 1. The idea in one sentence

Yudkowsky and Soares (2017) propose a decision theory built around one question. In their words, a rational agent should treat her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" The paper calls this *functional decision theory*. Its official formal statement, Equation (4) in Section 5, selects an **action** by intervening on a node that represents the output of the agent's decision function on her current input. The authors also mention, in footnotes, a "preferred formalization" that selects **policies** instead. To keep the two apart, I call the action-valued rule of Equation (4) **A-FDT**, and I call the footnoted variant **policy-FDT**.

This essay sets out the formal machinery of A-FDT, works through the paper's examples, and then turns to the questions Equation (4) leaves open. Where I go beyond the source, I say so explicitly.

## 2. The common template: expected utility with a hypothetical connective

The paper presents A-FDT, causal decision theory (CDT) and evidential decision theory (EDT) as three readings of one formula. An agent with observation history $x$ chooses an action $a \in \mathcal A$ maximizing

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}$$

The connective $\hookrightarrow$ ("if $a$ were done") is left open. Following Joyce, the authors treat the choice of $\hookrightarrow$ as the *epistemic perspective* from which actions are evaluated, not as a disagreement about value. Operationally, the agent holds a world-model $M$ and, for each $a$, builds a *hypothetical* $M^{a\hookrightarrow}$, which the paper describes as a scratch-paper object rather than a belief. She then scores each hypothetical by expected utility.

Writing $V := \mathcal U(\textsc{Outcome})$, the three theories are:

$$\mathrm{EDT}(P,x) = \arg\max_a \mathbb E\big(V \mid \textsc{Obs}=x,\ \textsc{Act}=a\big) \tag{2}$$
$$\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E\big(V \mid \mathtt{do}(\textsc{Act}=a),\ \textsc{Obs}=x\big) \tag{3}$$
$$\textbf{A-FDT:}\quad \mathrm{FDT}(P,G,x) = \arg\max_a \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big). \tag{4}$$

Here $\mathtt{do}$ is Pearl's intervention operator: it sets a node's value, recomputes everything downstream of it in $G$, and leaves everything else alone.

## 3. Anatomy of Equation (4)

Each ingredient of (4) deserves a careful reading.

**The model $(P,G)$.** $P$ is a probability distribution over variables, and $G$ is a directed graph. Unlike CDT's graph, $G$ may contain *logical* variables, meaning nodes that stand for the outputs of mathematical functions. The paper's slogan is: "*Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*" An edge out of a logical node marks a *subjunctive* dependence: if that function had a different output, this variable would differ.

**The decision node $\textsc{fdt}(\underline P,\underline G,\underline x)$.** This is a variable whose intended referent is the output of the A-FDT algorithm itself, run on inputs $(P,G,x)$. Underlining denotes de-quoting, so the variable's *name* contains the model. The self-reference is resolved by Kleene's recursion theorem ("quining"). The agent needs a variable representing her own output, not knowledge of its value. Because $\mathtt{do}$ overrides the node, its prior distribution is irrelevant to the computation. The paper says this explicitly in the smoking lesion analysis.

**Intervening on a type, not a token.** CDT sets the physical act. A-FDT sets the output of the function. Every physical system that implements or accurately models that function then varies with it, including the agent's own body, a twin, or a predictor's simulation. Statistical correlates that do not compute the function, such as a lesion, stay fixed.

**Observations change the intervention point, not the distribution.** Equation (4) contains no conditioning on $\textsc{Obs}=x$. In the paper's words, "FDT responds to observation by changing which node it intervenes upon." This is the most unusual structural feature of the rule, and it produces the theory's most striking verdicts. The source also notes that the older Timeless Decision Theory both conditioned *and* moved the intervention point, a "double update" that "proves harmful in practice."

**What the formula is not.** The authors would prefer a $\mathtt{true}(\phi)$ operator that updates $P$ on the counterpossible "$\textsc{fdt}(\ldots)=a$". Since no satisfactory account of counterpossible conditioning exists, Equation (4) instead *requires the dependency graph as input*, just as CDT requires a causal graph.

### A step-by-step procedure

The paper models each dilemma in a consistent way, and the following recipe is my synthesis of that practice:

1. **Variables.** Include world variables, $\textsc{Act}$, the outcome, $V$, and one decision node $D_y := \textsc{fdt}(\underline P,\underline G,\underline y)$ for each observation history $y$ the agent might have at the moment of choice.
2. **The switch.** $\textsc{Act} = D_{\textsc{Obs}}$. Whatever observation the world actually produces selects which decision node drives the body. In the paper's transparent-Newcomb and blackmail graphs, $\textsc{Act}$ has incoming edges from every $D_y$ and from whatever generates the observation.
3. **Subjunctive edges.** Draw $D_y \to Z$ whenever $Z$ is produced by a process that computes or reliably models the agent's response to $y$. Add exogenous noise nodes for imperfect accuracy.
4. **Priors.** Put ordinary priors on exogenous variables, and beliefs on the decision nodes $D_{y'}$ for the observations $y' \neq x$ that the agent did not receive.
5. **Evaluate.** For each $a$, apply $\mathtt{do}(D_x=a)$, propagate, and compute $\mathbb E[V]$ under the *unconditioned* $P$.
6. **Choose** the argmax. The paper does not specify tie-breaking. Any fixed rule will do, but the predictors in the model should be assumed to know it.

## 4. Subjunctive dependence and the construction of $G$

The paper's examples supply the intuitions. Two calculators computing $6288+1048$ subjunctively depend on that sum, whether or not they share a causal history. A scribe copying one calculator's output depends on it both causally and subjunctively. Two calculators that merely happen to share a colour do not depend on each other at all. Causal dependence is therefore a special case of subjunctive dependence.

Equation (4) is only as good as $G$, and the authors say so directly: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." For their own examples they supply the graph by hand.

**My operational proposal.** In textbook-style dilemmas, read the subjunctive edges off the specification of the problem. If a variable's value is defined, up to stated noise, as a function of *what the agent would do given input $y$*, then it receives an edge from $D_y$. Phrases such as "predicted that she would…", "iff she predicts you will…", and "her twin reasons the same way" mark such edges. Variables defined by mechanisms that do not consult the agent's response, such as lesions, genes, or the termite infestation, receive no such edge, even when they are correlated with $\textsc{Act}$. This test reproduces every graph in the paper. It is a reconstruction for well-posed problems, however, not a solution to the general problem of discovering dependencies in the wild.

## 5. Worked examples

In all examples I use the paper's payoffs, in dollars as utility.

### Newcomb's problem (99% accurate predictor)

The graph is $D \to \textsc{Act}$ and $D \to \textsc{Prediction} \leftarrow \textsc{Accurate}$, with $\textsc{Prediction} \to \textsc{Box B}$. Intervening on $D$ gives:

$$\mathbb E[V\mid \mathtt{do}(D=\text{one})] = 0.99(1{,}000{,}000) = 990{,}000,$$
$$\mathbb E[V\mid \mathtt{do}(D=\text{two})] = 0.01(1{,}001{,}000)+0.99(1{,}000) = 11{,}000.$$

A-FDT one-boxes. (The paper's EDT discussion reports \$999,000 for one-boxing, which appears to be a typo. Its A-FDT computation gives the correct \$990,000.) Under CDT, $\mathtt{do}(\textsc{Act})$ leaves $P(\text{full})=p$ fixed, so two-boxing wins by \$1,000 for every $p$. The source stresses that the A-FDT agent believes in no retrocausation. She simply declines to imagine her action changing while the predictor's model of the same function stays put.

The **twin prisoner's dilemma** has the same structure: both prisoners' acts hang off one node $D$. $\mathtt{do}(D=\text{C})$ yields \$1,000,000 and $\mathtt{do}(D=\text{D})$ yields \$1,000, so A-FDT cooperates.

### Smoking lesion

The paper resolves the problem's latent ambiguity by giving the agent one of two utility functions, $\mathcal U_S$ (lesion, enjoys smoking) or $\mathcal U_R$ (no lesion, values smoking at $-\$1$). There are correspondingly two decision nodes, with $\textsc{Act}=D_S$ under the lesion and $\textsc{Act}=D_R$ otherwise. Neither node points at $\textsc{Cancer}$. Let $p=P(\text{lesion})$ and $q=P(D_R=\text{smoke})$. Then

$$\mathbb E[V\mid\mathtt{do}(D_S=\text{smoke})] - \mathbb E[V\mid\mathtt{do}(D_S=\text{refrain})] = p\cdot 1{,}000 > 0,$$

because the intervention changes nothing except the act in the lesion branch. A-FDT smokes. The paper's point is that a single rule one-boxes *and* smokes, against Gibbard and Harper's claim that the two verdicts must come apart.

### Transparent Newcomb

The agent sees box B full. The decision nodes are $D_{\text{full}}$ and $D_{\text{empty}}$. The prediction concerns $D_{\text{full}}$ and determines what the agent sees, and $\textsc{Act}=D_{\textsc{Obs}}$. Let $q=P(D_{\text{empty}}=\text{two})$. Without conditioning on "full":

$$\mathtt{do}(D_{\text{full}}=\text{one}):\ 0.99(1{,}000{,}000)+0.01\cdot q(1{,}000) = 990{,}000+10q,$$
$$\mathtt{do}(D_{\text{full}}=\text{two}):\ 0.01(1{,}001{,}000)+0.99\cdot q(1{,}000) = 10{,}010+990q.$$

A-FDT one-boxes for every $q\in[0,1]$. (The source prints the second line as "\$110,00 + $q\cdot$\$990", a typo for \$10,010.) The hypothetical in which she takes both boxes is one in which she mostly *sees an empty box*. Parfit's hitchhiker has exactly this structure, so A-FDT pays the driver.

One textual caution: the paper's displayed expression for this case writes the observation inside the $\mathtt{do}$, but its computation does *not* condition on $\textsc{Obs}$. Equation (4) and the computation agree, so I follow them.

### XOR blackmail

The letter is sent iff (no termites ∧ the agent would pay) or (termites ∧ the agent would refuse). Infestation has no edge from $D$. With $p=P(\text{termites})$:

$$\mathtt{do}(D_{\text{letter}}=\text{pay}):\ -(1-p)1{,}000 - p\,1{,}000{,}000; \qquad \mathtt{do}(D_{\text{letter}}=\text{refuse}):\ -p\,1{,}000{,}000.$$

A-FDT refuses, by a margin of $(1-p)\cdot 1{,}000$. EDT pays, because conditioning on paying makes termites impossible given the letter.

### Death in Damascus

Death's appointment book is a perfect prediction of $D$. $\mathtt{do}(D=\text{Damascus})$ yields death at no extra cost, and $\mathtt{do}(D=\text{Aleppo})$ yields death minus \$1,000. A-FDT stays, stably. CDT oscillates, because its hypotheticals hold Death's location fixed while the action varies.

### Mechanical blackmail and threshold behaviour

The blackmailer runs the program iff she predicts the agent would pay. Suppose she wrongly predicts payment with probability $\varepsilon$. Then paying costs \$1,000, while refusing costs $\varepsilon\cdot 1{,}000{,}000$ in expectation, since refusers are blackmailed only by mistake. A-FDT refuses iff $\varepsilon < 0.001$. The paper's figure of $\varepsilon=0.0009$ correctly gives refusal. Its claim that at "0.011%" the agent pays must be a slip for roughly 0.11%, since 0.011% lies below the threshold. The general lesson is that A-FDT is a genuine expected-value calculation, not a blanket policy of "never negotiate." Its verdict tracks the predictor's reliability.

### When A-FDT agrees with CDT and EDT

If every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from the dependence of $\textsc{Act}$ on its own decision node, then $\mathbb E[V\mid a]=\mathbb E[V\mid\mathtt{do}(a)]=\mathbb E[V\mid\mathtt{do}(D=a)]$, and all three theories coincide. Divergence requires predictors, copies, or other systems whose behaviour depends on the agent's function.

## 6. Open points and how I would operationalize them

### 6.1 The decision nodes for observations you did not receive

Equation (4) intervenes only on $D_x$. In every one of the paper's examples, the beliefs about other nodes (the $q$'s) turned out to be inconsequential, and the authors note in passing what the "correct" values are: $q=0$ in the lesion case and $q=1$ in transparent Newcomb. The equation itself does not settle how these beliefs should be formed.

**My proposal.** Treat $P(D_y)$ for $y\neq x$ as a self-prediction. Ideally it should be *consistent*, meaning that each $D_y$ puts its mass on what Equation (4) itself outputs at $y$. In practice, run a sensitivity check over $q$, as the paper implicitly does. If the argmax is constant across $q$, as in all the cases above, the verdict is robust.

### 6.2 Where A-FDT and policy-FDT can come apart

The source flags, without an example, that its preferred formalization iterates over "*policies* (mappings from observations to actions) rather than actions," and that "This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper." The following example is my own illustration of how such a difference can arise.

Two copies of the agent receive different inputs, $L$ and $R$. Each copy shares a common payoff of 2 if both choose $\alpha$, 1 if both choose $\beta$, and 0 otherwise. The copy holding $L$ computes:

$$\mathbb E[V\mid\mathtt{do}(D_L=\alpha)] = 2\,P(D_R=\alpha),\qquad \mathbb E[V\mid\mathtt{do}(D_L=\beta)] = P(D_R=\beta).$$

It therefore picks $\alpha$ iff $P(D_R=\alpha)>1/3$. Both $(\alpha,\alpha)$ and $(\beta,\beta)$ are self-consistent fixed points: if each copy confidently expects the other to play $\beta$, A-FDT rationally plays $\beta$. Policy-FDT, which optimizes over the whole map $\pi:\{L,R\}\to\{\alpha,\beta\}$, picks $(\alpha,\alpha)$ directly. A-FDT is thus best understood as a best response *given beliefs about one's other-input outputs*. When those outputs interact strategically, the rule can settle on inferior self-consistent assignments.

A reasonable operational fix, again my proposal, is to choose among the self-consistent assignments the one with the highest prior expected value. In effect this is policy selection, so in such cases I would defer to policy-FDT.

### 6.3 What is $P$?

Because A-FDT does not condition on the current observation, $P$ must be the model from the standpoint *before* the dilemma's observations: the epistemic state that predictors modeled. The paper models each dilemma that way but gives no general rule for when "before" begins. My working rule is that $P$ should represent beliefs at the point when the relevant predictions were made, while still incorporating background knowledge acquired earlier.

### 6.4 Counterpossibles

If A-FDT in fact outputs one-boxing, then "$D=$ two" is a logical falsehood. The source admits that A-FDT thereby relies on counterpossible reasoning and calls this "the main drawback of FDT relative to CDT at this time." Supplying $G$ is the pragmatic workaround. The authors add that an agent who instead imagines adopting a *different* function, which they call FDT$'$, does not escape the problem, because predictors of the actual function $d$ would still have to be imagined as predicting differently.

## 7. Dominance, fairness and reflective stability (the source's arguments)

**Dominance.** The paper argues that every construction of hypotheticals induces its own dominance relation. Two-boxing dominates only under CDT counterfactuals. Under counterfactuals that hold subjunctive dependencies fixed, A-FDT never chooses a dominated act. Dominance therefore cannot adjudicate between theories without begging the question. The authors appeal instead to utility actually achieved.

**Fairness.** One can always build a problem that punishes some decision theory, for instance by rewarding only agents who follow EDT. The authors restrict their claim to "fair problems," those in which "the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the dilemma at hand." Newcomb's predictor punishes *two-boxers*, not CDT as such. The authors report no fair dilemma in which FDT loses, but they concede that "fair" lacks a formal definition.

**Precommitment and stability.** CDT and EDT agents would pay for binding precommitments in transparent Newcomb or blackmail. A-FDT agents "simply act as they would have precommitted to act." The authors describe the theory as "so far as we know, reflectively stable in fair problems": holding the blackmail letter, an A-FDT agent would not wish to self-modify into a CDT agent.

**Control.** To the objection that the agent cannot "control" a mathematical fact, the authors reply that a deterministic CDT agent equally cannot do otherwise at the token level. Both theories evaluate imagined variations, and they differ only in which variations they imagine.

## 8. Conclusion

A-FDT is CDT with the point of surgery relocated. Instead of $\mathtt{do}(\textsc{Act}=a)$ conditioned on the evidence, it applies $\mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)$ and uses the observation only to select the node. This one change accounts for every verdict in the paper:

- Predictors, twins and appointment books vary with the agent's choice in her hypotheticals, while lesions and infestations do not.
- Observed boxes and letters can fail to appear in the hypotheticals for non-optimal choices.

The rule therefore one-boxes, smokes, cooperates with twins, pays the driver, refuses extortion when the predictor is accurate enough, and stays in Damascus.

Applying A-FDT to a new case comes down to three tasks: build $(P,G)$ with decision nodes indexed by observation, draw subjunctive edges to whatever computes the agent's response, and evaluate interventions on the node for the actual input without conditioning. The source leaves two burdens open: discovering $G$ in general, and grounding counterpossible reasoning. I have added a third caution of my own. Because A-FDT optimizes one input at a time, problems in which outputs at different inputs must coordinate call for policy-level selection.

## References

- Yudkowsky, E. & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality.* arXiv:1710.05060.
- Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory.*
- Pearl, J. (2000). *Causality.*