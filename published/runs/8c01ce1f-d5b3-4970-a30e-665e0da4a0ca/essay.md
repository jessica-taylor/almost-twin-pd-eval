# A-FDT: Deciding by Intervening on a Function

## 0. Scope and conventions

This essay explains the decision procedure given as Equation (4) of Section 5 of Yudkowsky and Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*. The paper calls the theory "FDT". I call it **A-FDT** (action-level functional decision theory), because Equation (4) selects an *action*, whereas the authors' "preferred formalization" selects a *policy* (footnote 7). I treat the policy version as a separate variant and discuss it only where it matters. The other theories are CDT (causal decision theory) and EDT (evidential decision theory).

I try to mark three kinds of statement. Claims *of the source* are labelled as such. Readings I think the source supports but does not state are marked **(interpretation)**. Proposals beyond the source are marked **(my proposal)**.

## 1. The shape of the theory

All three theories, according to the source, maximize expected utility

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j).$$

They differ only in how they read the decision conditional "$\hookrightarrow$". Following Joyce, the source treats this as a free "epistemic perspective". EDT reads it as conditioning, $P(o_j\mid x,a)$. CDT reads it as Pearl's intervention on the physical act. A-FDT reads it as an intervention on a *logical* variable, the output of the agent's own decision function.

The procedure is built from a world-model $M=(P,G)$. Here $P$ is a probability distribution over variables, including variables for the outputs of mathematical functions, such as the value of $6288+1048$. $G$ is a graph saying how changing one variable, logical ones included, changes the others. Pearl's $\mathtt{do}$ operator then gives:

$$\textbf{A-FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V\;\Big|\;\mathtt{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big)\qquad\text{(Eq. 4)}$$

where $V=\mathcal U(\textsc{Outcome})$ and the underlines denote dequoting. The node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ stands for "whatever this very algorithm outputs when run on world-model $(P,G)$ and observations $x$".

The source's one-line summary is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." Setting Eq. (3) beside Eq. (4) shows the two differences from CDT:

1. **Where the intervention happens.** CDT intervenes on a node $\textsc{Act}$ for the physical behaviour of the agent's body. A-FDT intervenes on a node for the output of the agent's decision procedure. In Peirce's terms, CDT intervenes on a token and A-FDT on a type.
2. **How observation is used.** CDT conditions on $\textsc{Obs}=x$. A-FDT conditions on nothing. Observation only selects *which node* is intervened on: $\mathrm{fdt}(\cdot,\cdot,x)$ rather than $\mathrm{fdt}(\cdot,\cdot,y)$.

## 2. Why a logical node, and why the self-reference is harmless

The node is an output of a function, not a physical event. A deterministic function on a given input has exactly one output, so $\mathrm{fdt}(P,G,x)=a'$ is, if false, a counterpossible: its negation is a mathematical truth. The source says this is the "main drawback" of the theory relative to CDT. It also argues that reasoners already handle such cases. Mathematicians reason sensibly about "the twin prime conjecture is false", and A-FDT only needs a narrow class of such judgments, such as how a predictor's prediction would differ if the algorithm's output differed. The source calls the difficulty "technical rather than philosophical".

The node's name depends on the model that contains it. The source answers that the agent need not know the *value* of $\mathrm{fdt}(P,G,x)$ in order to have a variable *representing* it, and that Kleene's second recursion theorem (quining) shows how a data structure can contain an accurate representation of itself.

The source's own analogy is the calculator. If you see one calculator display $7336$ for $6288+1048$, you infer the other will too, though not with certainty, since cosmic rays exist. Asking what your calculator would do if it displayed $3159$ while holding fixed that $6288+1048=7336$ is the CDT move. Asking what the world would be like if the arithmetic function had a different value, with everything that computes it changing too, is the A-FDT move.

## 3. Subjunctive dependence: the content of $G$

Eq. (4) is only as good as $G$. The source defines two systems as *subjunctively dependent* when they compute the same function, or when one contains a model of the other's function. Several of its remarks fix the concept:

- Causal dependence is a special case. A scribe copying a calculator's display depends on it both causally and subjunctively.
- Pure statistical correlation is not subjunctive dependence. Two calculators that happen to be pink are not linked, since if one had been green the other would still be pink.
- Dependence can be imperfect: imperfect predictors and nondeterministic agents weaken the link without eliminating it.
- It need not run through a common cause. Two civilizations that independently adopt the same arithmetic are linked by a mathematical structure, not a causal path.

The bridge from this to the graph is the paper's central assumption: "when an FDT agent imagines herself taking two different actions, she imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure." So $G$ should contain an edge from the $\mathrm{fdt}$ node to a variable $Z$ exactly when $Z$ is computed, exactly or approximately, from that function or from a model of it. That includes the agent's own act, a predictor's prediction, a twin's choice, and a future self facing a relevantly identical choice. It excludes a lesion that merely co-occurs with the agent's tastes.

**The source leaves open how to find $G$.** It says: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." It says Eq. (4) "works *given* a graph", and footnote 9 says the structure must be "given as an input", just as CDT takes causal structure as input.

**(My proposal)** A working test for drawing an edge $\mathrm{fdt}\to Z$: *Would an accurate account of how $Z$ is produced mention a computation that either is this algorithm, or is a model of this algorithm's behaviour on this input?* If yes, include the edge, with noise reflecting the model's fidelity. If the only link is a shared upstream cause that is not itself a model of the algorithm, omit it. This is a heuristic and not a derivation. In unusual cases, such as a predictor that models the agent only approximately, it requires judgment about fidelity.

## 4. The procedure, step by step

Eq. (4) is a procedure. For an agent with model $(P,G)$ and observation $x$:

1. Identify the node $n_x=\mathrm{fdt}(\underline P,\underline G,\underline x)$. Other nodes $n_y$ for $y\ne x$ also exist, representing what the procedure outputs on other observations.
2. For each $a\in\mathcal A$, perform surgery by setting $n_x:=a$ and cutting $n_x$'s incoming dependence. Recompute every descendant of $n_x$ along $G$. Leave non-descendants at their prior distribution. **(Interpretation:** this includes $\textsc{Obs}$ itself if $\textsc{Obs}$ is a descendant. The source's computation of Fiona in the transparent Newcomb problem, below, lets the observation change in the hypothetical.)
3. Compute $\mathbb E[V]$ in each surgered model, then output the maximizing $a$.

Three structural features deserve mention.

**Descendants are not only the act.** In the paper's graphs, $\textsc{Act}$ is a function of one or more $\mathrm{fdt}$ nodes plus upstream variables that select *which* node governs it. In the transparent Newcomb graph, $\textsc{Prediction}$ selects whether $\mathrm{fdt}(\cdot,\cdot,\mathit{full})$ or $\mathrm{fdt}(\cdot,\cdot,\mathit{empty})$ controls $\textsc{Act}$.

**Other nodes need priors.** When the agent intervenes on $n_x$, the sibling nodes $n_y$ stay at their prior. The source's examples show the answer should not depend on these priors, and the "correct" value (say $q=1$ for "two-box on seeing an empty box") can be verified afterwards. **(My proposal)** In practice, evaluate with $q$ symbolic, check that the argmax is $q$-independent, and if it is not, solve for the fixed point in which each $n_y$'s prior equals the output the procedure would give on $y$.

**No zero-probability problem.** EDT cannot evaluate an action it is certain not to take. A-FDT's surgery sets $n_x$ by fiat, so it does not need $P(n_x=a)>0$. This is the source's point about Spohn: extreme priors let EDT be made to do anything, and A-FDT is immune.

## 5. Worked examples

All dollar figures are the source's utilities.

### 5.1 Newcomb's problem

The variables are $\textsc{Accurate}\in\{\text{accurate }(0.99),\text{inaccurate }(0.01)\}$, $\textsc{Prediction}$, $\textsc{Box B}$, $\textsc{Act}$, and $V$. $G$ has edges $\mathrm{fdt}\to\textsc{Act}$, $\mathrm{fdt}\to\textsc{Prediction}$, $\textsc{Accurate}\to\textsc{Prediction}$, $\textsc{Prediction}\to\textsc{Box B}$, and $\textsc{Act},\textsc{Box B}\to V$.

- $\mathtt{do}(\mathrm{fdt}=\textit{onebox})$: act is one-box and the box is full with probability 0.99, so $\mathbb E[V]=\$990{,}000$.
- $\mathtt{do}(\mathrm{fdt}=\textit{twobox})$: the box is full with probability 0.01, so $\mathbb E[V]=0.01\cdot 1{,}001{,}000+0.99\cdot 1{,}000=\$11{,}000$.

A-FDT one-boxes. (The source's text gives Eve's one-box value as $\$999{,}000$, which appears to be an arithmetic slip, since $0.99\cdot 10^6=990{,}000$.)

With predictor accuracy $\alpha$ in place of 0.99, one-boxing wins iff $\alpha\cdot 10^6>(1-\alpha)\,1{,}001{,}000+\alpha\cdot 1{,}000$, that is $\alpha>0.5005$. This threshold is my arithmetic, not the source's. The same threshold governs the twin prisoner's dilemma with match-probability $\rho$ between the twin's choice and the agent's: cooperate iff $\rho>0.5005$.

The CDT agent cuts the edges $\mathrm{fdt}\to\textsc{Prediction}$ and sees a constant $p$ of the box being full. Two-boxing then always gains $\$1{,}000$.

The A-FDT agent does not believe in retrocausation. She has no physical signal travelling backwards. She thinks it is incoherent to imagine her action differing while her algorithm's output, which the predictor models, stays the same.

### 5.2 Smoking lesion

Here the graph differs, and this is where A-FDT parts company with EDT. Cancer is caused by the lesion, which also determines the agent's tastes. In the source's formalization there are two possible procedures, $\mathrm{fdt}(P_S,G)$ and $\mathrm{fdt}(P_R,G)$, corresponding to the two utility functions (smoker-lover and not), and the lesion selects which one controls $\textsc{Act}$. The $\mathrm{fdt}$ node has an edge to $\textsc{Act}$ but not to $\textsc{Cancer}$, so $P(\text{lesion})=p$ is unchanged by the surgery. Smoking then gains $p\cdot\$1{,}000$ and the agent smokes.

So one rule one-boxes in Newcomb and smokes here, with the difference carried entirely by $G$. The source itself regards the formalization as contrived, because the agent is uncertain about her own desires, and it recommends that philosophers abandon the dilemma.

### 5.3 Transparent Newcomb and Parfit's Hitchhiker

The agent observes a full box. Her procedure on that observation is $n_{\textit{full}}$. When she sets $n_{\textit{full}}=\textit{twobox}$:

- if the predictor was accurate, the prediction was "two-box", the box would have been empty, and the observation would have been *empty*, so a different node $n_{\textit{empty}}$ (prior $q$ of two-boxing) controls her act and she gets $\$1{,}000\,q$;
- if the predictor erred, the box is full and she two-boxes for $\$1{,}001{,}000$.

So $\mathbb E[V\mid \textit{twobox}]=0.01\cdot 1{,}001{,}000+0.99\,q\cdot 1{,}000=10{,}010+990q$. (The source's printed "\$110,00" is evidently a typo.) For one-boxing, $\mathbb E[V]=990{,}000+10q$. The one-box action wins for every $q$.

Even holding a full box, the agent *envisions* two-boxing in a world where she probably saw an empty one. The source's grounds for accepting this are the arguments from precommitment, from the value of information, and from utility. Its main claim is that one-boxing here is exactly paying the driver in Parfit's Hitchhiker.

### 5.4 Blackmail and the observation-switch

In the mechanical blackmail problem, the blackmailer runs a program iff she predicts the agent would pay once blackmailed. Intervening on $n_{\textit{blackmail}}$ changes both what the agent does if blackmailed *and* whether the blackmail was sent. Refusing reaches a world in which blackmail is rarely sent.

The source reports that with a blackmailer error rate of 0.0009, refusing costs $0.0009\cdot 10^6=\$900$ in expectation against $\$1{,}000$ for paying. By the same arithmetic the break-even error rate is $0.001$. The source's statement that she pays at 0.011% looks like a slip for something above 0.1%. I would not rely on that sentence.

XOR blackmail works the same way: the $\mathrm{fdt}$ node affects whether the letter is sent but not whether the house has termites, so A-FDT refuses to pay. EDT pays, because conditioning on paying lowers its credence in termites.

### 5.5 Death in Damascus

Death's book entry is a descendant of $\mathrm{fdt}$, as is the agent's location. Both change together, so staying costs $0$ and fleeing costs $\$1{,}000$. The agent stays, and nothing is unstable. The agent also values a truly random coin at about half of $\$1{,}000{,}000$, because her hypotheticals contain no spurious independence from Death's location.

## 6. Where A-FDT agrees with and differs from CDT and EDT

The source's agreement claim is that on models where every correlation between $\textsc{Act}$ and another variable is caused by $\textsc{Act}$ (with the possible exception of the $\mathrm{fdt}$ node on which $\textsc{Act}$ depends),

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\mathrm{fdt}=a)],$$

so all three give the same output. They diverge when something is correlated with the act in a way the act did not cause, as with a predictor, twin, or copy.

The source's diagnosis is that EDT respects too many action-environment correlations (including merely statistical ones, as in the cosmic ray and XOR problems) and CDT respects too few (it breaks the predictor's link to the agent, so a perfect predictor "inexplicably falters" exactly when the agent decides). A-FDT keeps exactly the correlations that subjunctively depend on the algorithm.

The source also argues that dominance is not a neutral criterion. Every method of constructing hypotheticals induces its own dominance relation: CDT's "holding everything but the act fixed" tells you two-boxing dominates, whereas A-FDT's analogous dominance (holding subjunctive dependence fixed) says A-FDT agents never choose a dominated action.

## 7. Open points and how I would handle them

**(a) The graph is an input.** This is the biggest gap. For an unfamiliar problem, the practitioner must decide which variables are functions of the agent's algorithm or models of it. My heuristic above, and the extra question "is this correlation explained by a mechanism that tracks my output?", are not guaranteed to be complete, and different modelers might disagree on a hard case.

**(b) Eq. (4) versus the worked examples on observations.** Eq. (4) shows no conditioning on $x$ inside the expectation, while the transparent Newcomb example writes $\mathtt{do}(\mathrm{fdt}(\cdot,\cdot,\textit{full})=a,\ \textsc{Obs}=\textit{full})$. The narrative computation, however, lets the observation vary in the hypothetical. **(Interpretation)** The $\textsc{Obs}$ in the worked example is bookkeeping and does not condition. If one conditioned on $\textsc{Obs}=\textit{full}$ after intervening, the agent would recover CDT-like or EDT-like two-boxing. The source says the "double update" of Timeless Decision Theory (condition *and* switch nodes) "proves harmful in practice".

**(c) Action versus policy.** The authors' preferred formalization intervenes on the node that outputs a *policy*, a map from observations to actions, which the agent then applies. Eq. (4) with sibling priors approximates this in the single-agent cases here. The source says it "makes a difference in certain multi-agent dilemmas" and sets it aside. I use the action-level reading throughout, as the assignment asks. Where several nodes $n_x,n_y$ interact, I would regard the policy version as the safer reading.

**(d) Fairness.** The source claims A-FDT does at least as well as rivals on "fair" problems, where the agent's beliefs are accurate and the payoff depends only on behaviour in the problem at hand, not on which procedure produced it. It admits it has no formal criterion. Footnote 15 notes that a problem which punishes anyone who matches a copy of the A-FDT agent is unfair to A-FDT in a way no rival is. So there is no theory-neutral formal test. Claims of A-FDT's superiority are claims about the stated examples.

**(e) Counterpossible reasoning and bounded agents.** The source gives only a promissory account. A bounded agent will approximate $G$ and the surgery, and the source expects bounded approximations of each theory to retain the same relative strengths and weaknesses. That is an expectation, not a proof.

## 8. Further applications (source's claims)

Voting is one. Ten A-FDT agents with common knowledge of each other's procedure treat their votes as subjunctively dependent and each votes. They are not altruistic; they simply see that symmetric reasoners decide together. Self-coordination is another. A future self facing a relevantly identical choice is a copy, so skipping today is correlated with skipping next week, and the agent goes to the gym. These examples are sketched in the source's conclusion rather than computed. They show how $G$ encodes *which* copies exist.

## 9. Conclusion

A-FDT is Pearl-style expected-utility maximization with one change: the intervened variable is the output of the agent's own decision function, not the physical act. The graph then carries every dependency on that output, including predictors, twins and copies, and only those. Observations change which node is intervened on. In single-agent problems without predictors it collapses to CDT and EDT. In Newcomb-like problems it one-boxes, in the smoking-lesion problem it smokes, and it pays Parfit's driver and refuses blackmail, by the same rule in each case. The cost is that the rule is only as determinate as the dependency graph supplied to it, and the source honestly lists building that graph, and the logic of counterpossibles behind it, as unsolved.

**Reference:** E. Yudkowsky and N. Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality* (arXiv:1710.05060), Sections 3–9. Background sources cited there include Gibbard and Harper (1978), Joyce (1999), Pearl (2000), Nozick (1969), Parfit (1986), and Soares and Fallenstein (2015).