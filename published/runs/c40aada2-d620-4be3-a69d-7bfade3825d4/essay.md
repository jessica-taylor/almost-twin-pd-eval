# Action Functional Decision Theory (A-FDT): Intervening on the Output of Your Own Algorithm

## 1. The idea in one sentence

Yudkowsky and Soares (2017) describe the agent's question as: "Which output of this very function would yield the best outcome?" In their framing, an agent does not ask which *physical act* would cause the best outcome, as causal decision theory (CDT) does. Nor does she ask which act would be the best *news*, as evidential decision theory (EDT) does. She treats her decision as the output of a fixed mathematical function, and she asks what would follow if that function produced each candidate output.

The paper calls its theory simply "FDT." It also states in a footnote that "in the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions." The formal rule the paper actually writes down, Equation (4) in Section 5, intervenes on an *action*-valued node, one observation history at a time. This essay calls that action-level rule **A-FDT** and treats it as the object of study. Where I discuss the policy-level variant, I call it **policy FDT (P-FDT)**.

## 2. The common frame: expected utility with a free "hypothetical" connective

The source places EDT, CDT, and A-FDT inside one template, following Gibbard and Harper and Joyce. An agent chooses an action $a$ from a finite set $\mathcal A$ to maximise

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}
$$

Here $x$ is the observation history, $o_j$ ranges over outcomes, and $P(a \hookrightarrow o_j; x)$ is the probability of $o_j$ "in the hypothetical scenario where the action $a$ is executed after receiving observations $x$." Following Joyce, the theories agree on how to value prospects. They disagree only on how to construct the hypothetical, that is, on how to interpret $\hookrightarrow$. Write $V = \mathcal U(\textsc{Outcome})$. Then:

- **EDT** (Eq. 2) conditions: $\arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a)$.
- **CDT** (Eq. 3) intervenes on the physical act and conditions on the observation: $\arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x)$.
- **A-FDT** (Eq. 4) intervenes on a *logical* node:

$$
\boxed{\;\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).\;} \tag{4}
$$

Three features of Equation (4) carry most of the theory.

1. **The intervention target is a type, not a token.** $\textsc{fdt}(\underline P,\underline G,\underline x)$ is a variable in the agent's own model. It stands for "the output of the A-FDT algorithm when run on inputs $(P,G,x)$." The underlines mark dequoting, so the variable's *name* is built from the model itself. The source argues that this self-reference is harmless: representing a value does not require knowing it, and Kleene's recursion theorem ("quining") shows how such self-representing data structures can be built. The source's slogan: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

2. **The graph $G$ encodes subjunctive dependence, not merely causation.** For CDT, $G$ is a causal graph. For A-FDT, $G$ must say "how changing a logical variable affects all other variables." Anything that computes, or reliably models, the agent's decision function on a given input gets an edge from the corresponding $\textsc{fdt}$ node. Pearl's $\mathtt{do}$ operator is then reused unchanged. It sets the node, propagates downstream, and leaves everything upstream or unconnected at its prior distribution.

3. **Observations are handled by moving the intervention point, not by conditioning.** Equation (4) contains no "$\textsc{Obs}=x$" term. The source puts it this way: "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." On seeing $y$ instead of $x$, the agent intervenes on $\textsc{fdt}(\underline P,\underline G,\underline y)$ instead. This single feature produces A-FDT's most distinctive verdicts.

### 2.1 Why not just a "$\mathtt{true}$" operator?

The cleanest statement would be $\arg\max_a \mathbb E(V \mid \mathtt{true}(\textsc{fdt}(\underline P,\underline x)=a))$: update the model on the logical sentence that the algorithm outputs $a$. For all but one $a$, that sentence is necessarily false, so this is a *counterpossible* supposition. The authors concede "it's not clear how to define a $\mathtt{true}$ operator." Their workaround is to require that $P$ come with a graph $G$ supplying the logical dependency structure, "in the same way that the relevant causal structure is given as an input to CDT." Equation (4) is therefore a rule *conditional on* a dependency graph. It is not a recipe for finding one. I return to this in §5.

## 3. A procedure for applying A-FDT

The paper presents its examples case by case. The following recipe makes the procedure explicit. It is my own systematisation, but every step is used in the paper's worked cases.

1. **List the variables.** Include world variables, the utility node $V$, the physical act $\textsc{Act}$, and one logical node $F_y := \textsc{fdt}(\underline P,\underline G,\underline y)$ for each observation history $y$ the agent might be in.
2. **Wire the graph.** $\textsc{Act}$ is a function of whichever $F_y$ is "live," and the variables that determine the agent's observation select which one that is. Any process that predicts, simulates, or duplicates the agent's computation on input $y$ gets an edge from $F_y$. Imperfect prediction is modelled with an exogenous noise node, as in the paper's $\textsc{Accurate}$ node. Mere statistical correlates, such as a lesion, get *no* edge from any $F_y$.
3. **Assign priors** to exogenous nodes, including priors over the $F_{y'}$ for $y' \neq x$ (the "off-path" nodes).
4. **For each $a$**, apply $\mathtt{do}(F_x=a)$, propagate, and compute $\mathbb E V$. Do **not** condition on having observed $x$.
5. **Output the argmax.**

## 4. Worked examples

All payoffs are in utility-dollars, as in the source.

### 4.1 Twin Prisoner's Dilemma

Both twins' acts are children of the same node $F$. Under $\mathtt{do}(F=\text{C})$ both cooperate, giving \$1,000,000. Under $\mathtt{do}(F=\text{D})$ both defect, giving \$1,000. A-FDT cooperates. CDT holds the twin's act fixed, so defection dominates.

### 4.2 Newcomb's problem

The predictor is 99% accurate. In the A-FDT graph, $F$ points to both $\textsc{Act}$ and $\textsc{Prediction}$, and $\textsc{Accurate}$ also points to $\textsc{Prediction}$:

$$
\begin{aligned}
\mathbb E[V\mid\mathtt{do}(F=\text{one})] &= 0.99(1{,}000{,}000)+0.01(0) = 990{,}000,\\
\mathbb E[V\mid\mathtt{do}(F=\text{two})] &= 0.01(1{,}001{,}000)+0.99(1{,}000) = 11{,}000.
\end{aligned}
$$

A-FDT one-boxes. The source stresses that this involves no retrocausation. When imagining two-boxing, the agent imagines the *function* having a different output. Since the predictor is "good at reasoning about FDT," the prediction changes in that imagined scenario.

### 4.3 Smoking lesion

In this case the lesion is not a model of the agent's algorithm, so no $F$ node points to $\textsc{Cancer}$. The paper's full formalisation uses two utility functions, $\mathcal U_S$ (likes smoking) and $\mathcal U_R$, and two corresponding nodes $F_S$ and $F_R$. $\textsc{Lesion}$ selects which node drives $\textsc{Act}$. Let $p$ be the prior probability of the lesion. Intervening on $F_S$ leaves $P(\text{lesion})=p$ unchanged, so the two hypotheticals differ only in the \$1,000 enjoyment term on the branch where $F_S$ is live. Smoking wins by $p\cdot\$1{,}000$. A-FDT therefore one-boxes *and* smokes, which is the pair of verdicts Gibbard and Harper suggested no single principled rule could deliver.

### 4.4 Transparent Newcomb (equivalently, Parfit's hitchhiker)

Both boxes are visible. The predictor fills B iff she predicts one-boxing *upon seeing B full*. The agent sees B full. The relevant nodes are $F_{\text{full}}$ and $F_{\text{empty}}$, and $\textsc{Prediction}$ selects which one drives $\textsc{Act}$. Let $q = P(F_{\text{empty}}=\text{two})$.

- $\mathtt{do}(F_{\text{full}}=\text{one})$: with probability 0.99 the prediction is "one," B is full, and the agent one-boxes for \$1,000,000. With probability 0.01 the prediction is wrong, B is empty, and $F_{\text{empty}}$ acts, yielding $1{,}000q$. Total: $990{,}000 + 10q$.
- $\mathtt{do}(F_{\text{full}}=\text{two})$: with probability 0.99, B is empty and the agent gets $1{,}000q$. With probability 0.01, B is full and the agent two-boxes for \$1,001,000. Total: $10{,}010 + 990q$.

For any $q\in[0,1]$ one-boxing wins, so A-FDT leaves the \$1,000 behind *while looking at a full box*. Its hypothetical for two-boxing is mostly a world in which it would have seen an empty box. Parfit's hitchhiker has the same structure: A-FDT pays the driver on arriving in the city.

**A textual point.** When the paper displays the quantity to be maximised here, it writes $\mathbb E(V\mid\mathtt{do}(F_{\text{full}}=a, \textsc{Obs}=\text{full})$, with the observation inside the conditioning bar. However, the calculation it then performs explicitly averages over the branch in which B is empty, so it does *not* condition on $\textsc{Obs}=\text{full}$. Conditioning on the observation would yield 1,000,000 versus 1,001,000 and the two-boxing verdict the paper rejects. Equation (4) itself has no observation term. I therefore read the displayed expression as a slip and follow Equation (4) and the worked numbers: **A-FDT never conditions on its observation.** The paper's footnote on "Timeless Decision Theory" supports this reading. It says that conditioning *and* moving the intervention point "creates a kind of 'double update' which proves harmful."

### 4.5 XOR blackmail (an infallible predictor)

Let $p$ be the prior that the house has termites (a \$1,000,000 loss). The letter is sent iff (no termites and the agent would pay) or (termites and she would not). The node $F_{\text{letter}}$ points to whether the letter is sent and to the act. The node $F_\varnothing$ drives the act if no letter arrives; it is irrelevant here, since there is nothing to pay. Termites point to $V$ and to the letter, but **no edge runs from $F$ to termites**.

$$
\begin{aligned}
\mathbb E[V\mid\mathtt{do}(F_{\text{letter}}=\text{pay})] &= -p(10^6) - (1-p)(10^3),\\
\mathbb E[V\mid\mathtt{do}(F_{\text{letter}}=\text{refuse})] &= -p(10^6).
\end{aligned}
$$

A-FDT refuses. CDT also refuses, but its hypothetical for paying is one in which an infallible predictor erred. EDT pays, because conditioning on paying makes "no termites" certain given the letter. In general, A-FDT is moved by correlations that pass through its function, not by correlations that merely co-occur with it.

### 4.6 Mechanical blackmail and the error-rate threshold

A blackmailer launches a \$1,000,000-damage program iff she predicts the agent would pay \$1,000 to stop it. Suppose she wrongly predicts payment with probability $\varepsilon$. Then refusing costs $\varepsilon\cdot 10^6$ in expectation, and paying costs $10^3$ (since the agent is then always blackmailed). A-FDT refuses iff

$$
\varepsilon < 10^{-3}.
$$

The paper's first figure, $\varepsilon=0.0009$, fits this: refusing costs \$900 in expectation, so the agent refuses. Its second figure, "0.011%," does not fit, because $1.1\times10^{-4}$ would still favour refusal. Presumably 0.11% was meant. The general lesson, which the source states, is that A-FDT refuses even while holding a letter it *knows* resulted from a prediction error, "because it's advantageous to be *the kind of agent* that makes such decisions." The decision is evaluated ex ante, over the whole distribution of situations in which the same function is run.

### 4.7 Death in Damascus

Death's appointment book is written from a perfect prediction of the agent's function. Under either intervention, Death is wherever the agent goes. The million is lost either way, so A-FDT stays and saves the \$1,000. There is no instability and no need for ratification or mixed strategies.

### 4.8 When the three theories agree

The source notes that if every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from $\textsc{Act}$'s own dependence on the $\textsc{fdt}$ node, then

$$
\mathbb E[V\mid a]=\mathbb E[V\mid\mathtt{do}(a)]=\mathbb E[V\mid\mathtt{do}(\textsc{fdt}=a)].
$$

A-FDT departs from CDT only when something other than the agent's own body computes or models her function: predictors, twins, copies, or her own future selves (the paper's gym example).

## 5. Open questions and operational proposals

### 5.1 Where does $G$ come from? (open in the source)

The authors are explicit: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." Equation (4) "works *given* a graph," but there is no Pearl-style identification theory for logical dependence.

*My operational proposal.* Draw an edge $F_y \to Z$ when $Z$'s mechanism, as the agent understands it, takes as an input the result of evaluating (a model of) her decision procedure on input $y$. Draw no edge when $Z$ merely co-varies with her act through shared upstream causes. Model reliability below 1 with an exogenous noise parent, as the paper does. This captures every example in the paper: predictors, Death's book, and twins get edges, while lesions and termites do not.

It leaves hard intermediate cases, however. A predictor might run a *similar* algorithm, or the agent's "function" might be described at varying levels of abstraction. Such cases need a similarity or reference-class judgment that the source does not supply. A conservative default is to give an edge with an explicit "fidelity" noise node and to treat the fidelity estimate as an empirical belief.

### 5.2 Counterpossibles

Every intervention but one sets a logical node to a value it cannot have. The source treats this difficulty as "technical rather than philosophical." It points to human reasoning about unproven conjectures and argues that CDT faces a parallel puzzle for deterministic agents. The graph-and-$\mathtt{do}$ device is precisely a way to *avoid* needing a general semantics for counterpossibles. Downstream variables are recomputed from their structural equations, and upstream ones are left alone.

### 5.3 Off-path nodes and their priors

Equation (4) intervenes only on $F_x$. The other nodes $F_{y'}$ stay at their priors, like the $q$ in §4.3–4.4. The paper shows its verdicts are robust to $q$ in those cases and remarks that the "correct" $q$ is what A-FDT itself would output. In general, though, the verdict at $x$ can depend on beliefs about off-path behaviour.

*My proposal.* Require self-consistency: set each off-path prior to the A-FDT output at $y'$, computed under those same priors, and look for a fixed point. The paper's own remarks ("the correct $q$ is 0," "is 1") suggest this, but it is an added assumption, and fixed points need not be unique.

### 5.4 Action versus policy: why the "A" matters

The authors' preferred P-FDT chooses a whole map $\pi:\mathcal X\to\mathcal A$:

$$
\pi^* = \arg\max_{\pi}\ \mathbb E\big(V \mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G)=\pi)\big),\qquad \text{act } \pi^*(x).
$$

The paper says the difference matters only "in certain multi-agent dilemmas." A small illustration shows how A-FDT's one-node-at-a-time maximisation can fail to coordinate across observations. The example is my own.

> A predictor will show the agent signal $x_1$ or $x_2$ (each with probability ½) and pays \$20 if her responses to both signals would be L, \$10 if both would be R, and \$0 if they differ.

Suppose the agent believes $F_{x_2}=\text{R}$ and sees $x_1$. Then A-FDT compares \$0 for L with \$10 for R and picks R. By symmetry, (R, R) is a self-consistent fixed point in the sense of §5.3, earning \$10. P-FDT ranges over joint policies and picks (L, L) for \$20.

So A-FDT behaves like a "player" at each information set, best-responding to its beliefs about its own other information sets. It can settle in an inferior equilibrium of a game played against itself. P-FDT is the planner's version. Under a self-consistent choice of off-path priors, every P-FDT-optimal policy is also a fixed point of A-FDT: if any single-input deviation helped, the policy would not be optimal. The converse fails, as the example shows. On the paper's examples the two coincide.

### 5.5 Ties, zero-probability nodes, and boundedness

Equation (4) is an argmax over a finite $\mathcal A$ and says nothing about tie-breaking. Unlike EDT, it does not require positive prior probability on each action, because interventions are defined even on prior-null values. The paper's analysis is idealised. It assumes accurate models and exact maximisation, and it conjectures that bounded approximations inherit the same comparative strengths.

## 6. Philosophical motivation, briefly

The source's case rests on three arguments.

- **Utility achieved.** In "fair" problems, those where outcomes depend only on the agent's *behaviour* rather than on which theory she uses, A-FDT agents end up richer. Newcomb's predictor "doesn't punish rational agents; she punishes *two-boxers*." The authors concede that "fairness" is not yet formalised.
- **Dominance is theory-relative.** Every way of building hypotheticals yields its own dominance notion. Two-boxing dominates only under CDT counterfactuals.
- **Reflective stability.** A-FDT acts as it would have precommitted to act, never assigns negative value to information, and does not want to self-modify into CDT mid-problem. CDT, by contrast, advises its own replacement.

They also argue that the charge of "controlling the past" or "controlling mathematics" cuts equally against CDT. A deterministic CDT agent also evaluates impossible alternatives to its one actual token act.

## 7. Conclusion

A-FDT, as given by Equation (4), is CDT with two substitutions. The agent intervenes on a logical node, the output of her own decision algorithm on her current input, instead of on her physical act. And she responds to observations by choosing *which* such node to intervene on rather than by conditioning. Supplied with a graph of subjunctive dependencies, it is a mechanical procedure. It one-boxes, smokes, cooperates with twins, pays the driver, refuses blackmail when the blackmailer's error rate is low enough, and does not flee Death.

What the source does not supply is equally clear: a method for constructing that graph, a semantics for counterpossibles beyond the $\mathtt{do}$ device, and a principled treatment of off-path self-beliefs. My suggestions for these gaps are an edge criterion based on whether a mechanism computes the agent's function, and self-consistent fixed points for off-path priors. They are additions, not doctrine. The policy-level P-FDT, which the authors prefer, avoids the coordination failures that the action-level rule can exhibit.

**Reference.** Yudkowsky, E. & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality.* arXiv:1710.05060.