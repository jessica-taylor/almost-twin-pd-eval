# A-FDT: Choosing as if You Were Setting the Output of a Function

*A mathematical essay on action functional decision theory, as formalized in Equation (4) of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality."*

## 1. The question A-FDT asks

Every expected-utility decision theory answers the same question in its own way: *what would the world look like if I chose $a$?* The theories differ in how they construct that hypothetical.

- **Evidential decision theory (EDT)** conditions on the act. It asks which act "would be the best news to hear I took."
- **Causal decision theory (CDT)** intervenes on the act as a physical event. It asks "Which physical act of mine causes the best outcome?"
- **Functional decision theory**, in the paper's words, holds that a rational agent treats "one's decision as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'"

The paper's formal statement of this idea, its Equation (4), intervenes on a variable whose value is the *action* that the decision function outputs on the agent's actual input. I will call the theory defined by that equation **A-FDT** (action functional decision theory). The name separates it from a variant the authors mention only in footnotes. In that variant the agent "actually iterate[s] over *policies* (mappings from observations to actions) rather than actions." I will call the footnoted variant **policy-selection FDT**. The authors say the difference "will not make a difference in this paper" but "makes a difference in certain multi-agent dilemmas." Section 6 shows where it bites.

Throughout, I separate three kinds of claim: what the paper asserts, what follows from Equation (4), and operational choices that are my own.

## 2. The formal definition

The paper first writes generic expected utility as

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),$$

where $\hookrightarrow$ is a "decision hypothetical" connective. Following Joyce, the theories are cast as rival interpretations of $\hookrightarrow$:

- EDT reads $P(a \hookrightarrow o;\,x)$ as $P(o \mid x, a)$.
- CDT, using Pearl's machinery, uses $\mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x)$. This is Equation (3).

A-FDT keeps Pearl's $\mathtt{do}$ operator but moves the point of surgery:

$$\boxed{\;\mathrm{A\text{-}FDT}(P, G, x) \;:=\; \operatorname*{argmax}_{a\in\mathcal A}\; \mathbb E\!\left(V \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline P, \underline G, \underline x) = a\big)\right)\;}\tag{4}$$

The ingredients are as follows.

- **$P$** is a joint distribution over world variables, including $V := \mathcal U(\textsc{Outcome})$. Unlike a CDT model, it must also contain variables standing for *outputs of mathematical functions*. The paper's example is a variable for the value of $6288+1048$.
- **$G$** is a graph over those variables. It "tells us how changing a logical variable affects all other variables." In CDT, $G$ encodes causal structure only. In A-FDT it encodes "the logical, mathematical, computational, causal, etc. structure of the world more broadly." The paper calls this broader relation *subjunctive dependence*.
- **$\textsc{fdt}(\underline P,\underline G,\underline x)$** is a node whose value is whatever the A-FDT procedure outputs when given the agent's own model and observation history $x$. The underlines mark dequoting. The node's *name* contains the model, and the paper notes that this self-reference is harmless by Kleene's recursion theorem ("quining"). The agent does not need to know the node's *value* in order to represent it.

Two structural differences from CDT stand out, and the paper states both explicitly.

1. **Locus of intervention.** CDT sets a physical event (the token act). A-FDT sets a logical fact: the output of a function on a given input, which is the type. Every physical system whose behavior depends on that output moves with it. This includes the agent's own body, an accurate predictor's model, and a twin running the same computation.
2. **Treatment of observations.** "Where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." Learning $y$ instead of $x$ changes the target node from $\textsc{fdt}(\ldots,x)$ to $\textsc{fdt}(\ldots,y)$.

The second point is easy to misread, so note it carefully: **Equation (4) contains no conditioning on $\textsc{Obs}=x$.** The paper does once write the transparent-Newcomb objective with "$, \textsc{Obs}=\textit{full}$" inside the expectation (with an unbalanced parenthesis). However, its worked numbers for that case average over worlds in which the box is *empty*. So the computation the paper actually performs matches Equation (4) as printed: the observation selects which node to intervene on, and it is not conditioned on. I adopt this reading throughout. It is what produces A-FDT's distinctive "updateless" behavior.

## 3. The rule as an algorithm

Equation (4) can be read in three ways. It is a Joyce-style constraint on $\hookrightarrow$. It is advice on how to build hypotheticals from a world model. It is also a step-by-step procedure. Read as a procedure, it says:

1. Build $(P,G)$. Include a node $F_y := \textsc{fdt}(\underline P,\underline G,\underline y)$ for every input $y$ on which some physical process computes or models your decision function. Draw an edge $F_y \to Z$ whenever $Z$ would differ if that output differed.
2. Identify your actual input $x$.
3. For each $a\in\mathcal A$, perform $\mathtt{do}(F_x=a)$. Recompute everything downstream of $F_x$ in $G$ and leave all other variables at their prior distribution. This includes the *other* nodes $F_{y\ne x}$.
4. Compute $\mathbb E[V]$ in each hypothetical and output the argmax.

In this graphical setting, the "subjunctive dependence" of Section 3 of the paper is simply descent from $F_x$ in $G$. The paper's slogan follows: "*Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*"

**Agreement in ordinary cases.** The paper notes that when every correlation between $\textsc{Act}$ and the rest of the world is caused by $\textsc{Act}$ (apart from $\textsc{Act}$'s own dependence on the function node), we have

$$\mathbb E[V\mid a] = \mathbb E[V\mid \mathtt{do}(a)] = \mathbb E[V\mid \mathtt{do}(F=a)],$$

and all three theories coincide. A-FDT diverges only when something other than the agent's own body depends on the decision function. Predictors, twins, and copies are the paradigm cases.

## 4. Worked examples

I use the paper's payoffs (in dollars as utility) and a predictor accuracy of 0.99 unless stated otherwise.

### 4.1 Twin prisoner's dilemma

Both prisoners' acts are children of the same node $F$.

- $\mathtt{do}(F=\textit{cooperate})$: both cooperate, giving $V = 1{,}000{,}000$.
- $\mathtt{do}(F=\textit{defect})$: both defect, giving $V = 1{,}000$.

A-FDT cooperates. EDT also cooperates, but for a different reason: correlation as news. A-FDT gets there through surgery, which makes its method "more resemblance to CDT's."

### 4.2 Newcomb's problem

The graph is $F \to \textsc{Act}$ and $F \to \textsc{Prediction} \leftarrow \textsc{Accurate}$, with $\textsc{Prediction}\to\textsc{Box B}$.

$$\mathbb E[V\mid\mathtt{do}(F=\textit{one})] = 0.99(1{,}000{,}000) = 990{,}000,$$
$$\mathbb E[V\mid\mathtt{do}(F=\textit{two})] = 0.01(1{,}001{,}000) + 0.99(1{,}000) = 11{,}000.$$

A-FDT one-boxes. The same arithmetic gives EDT's one-boxing value of 990,000; the paper prints \$999,000 for Eve at one point, which looks like a slip. CDT's graph has no edge from its intervention node to the prediction, so it two-boxes.

The paper anticipates an objection: if the agent is nearly sure the box is full, why not grab both? Its answer is that the hypothetical for two-boxing is one in which the function itself outputs two-box. A predictor that is "good at reasoning about FDT" then predicts differently, so the box is likely empty in that hypothetical. No retrocausation is assumed: "she does not think that a physical signal passes between her action and the predictor's prediction."

### 4.3 Smoking lesion

Here the lesion is not a model of the agent's function, so there is no edge from any $F$ node to $\textsc{Cancer}$. The paper formalizes the "love of smoking" as two possible utility functions, $\mathcal U_S$ and $\mathcal U_R$. That gives two possible function nodes:

- $F_S = \textsc{fdt}(\underline{P_S},\underline G)$, which controls the act if the agent has the lesion;
- $F_R$, which controls the act otherwise.

Intervening on $F_S$ leaves $P(\textit{lesion}) = p$ unchanged. The smoke and refrain hypotheticals differ only by the smoking bonus in the lesion branch, a difference of $p\cdot 1{,}000$. A-FDT smokes.

This single rule therefore one-boxes *and* smokes. Gibbard and Harper had argued that no rational agent could consistently do both.

### 4.4 Transparent Newcomb and Parfit's hitchhiker

The agent sees box B full, so $x=\textit{full}$. The graph contains $F_{\textit{full}}\to\textsc{Prediction}$. The prediction determines which observation occurs, and therefore which $F$ node drives $\textsc{Act}$. Let $q$ be the prior probability that $F_{\textit{empty}} = \textit{two}$. Then:

$$\mathbb E[V\mid \mathtt{do}(F_{\textit{full}}=\textit{one})] = 0.99(1{,}000{,}000) + 0.01\,q(1{,}000) = 990{,}000 + 10q,$$
$$\mathbb E[V\mid \mathtt{do}(F_{\textit{full}}=\textit{two})] = 0.01(1{,}001{,}000) + 0.99\,q(1{,}000) = 10{,}010 + 990q.$$

The paper's printed "\$110,00" appears to be a typo for \$10,010. For every $q\in[0,1]$, A-FDT one-boxes *while looking at a full box*. In the two-box hypothetical, the agent most likely would never have seen a full box at all.

The paper argues that this is exactly isomorphic to paying the driver in Parfit's hitchhiker. The driver rescues you iff she predicts that you pay once in the city, just as the predictor fills the box iff she predicts that you leave the \$1,000 once you see two full boxes. The paper offers three defenses of this behavior:

- **Precommitment.** CDT and EDT agents would bind themselves to it in advance.
- **Value of information.** A-FDT never pays to avoid information.
- **Utility.** Agents of this type see full boxes.

### 4.5 XOR blackmail

The letter is sent iff exactly one of two things holds: no termites and the agent would pay, or termites and the agent would refuse. Let $p$ be the prior probability of termites; the paper's Figure 7 makes $\textsc{Infestation}$ independent of $F_{\textit{letter}}$.

- $\mathtt{do}(F_{\textit{letter}}=\textit{pay})$: with termites, no letter is sent, giving $-10^6$. Without termites, the letter comes and the agent pays, giving $-10^3$. Expected value: $-p\cdot10^6-(1-p)10^3$.
- $\mathtt{do}(F_{\textit{letter}}=\textit{refuse})$: with termites, the letter comes and the agent refuses, giving $-10^6$. Without termites, no letter, giving $0$. Expected value: $-p\cdot10^6$.

Refusing is better by $(1-p)\cdot 1{,}000$, so A-FDT refuses. CDT also refuses, but its hypothetical for paying has an inerrant predictor erring. EDT pays, because conditional on paying the letter is good news.

### 4.6 Mechanical blackmail with a fallible predictor

The blackmailer launches the program iff she predicts that the agent pays, and she errs toward "predicts pay" with probability $\varepsilon$.

- A disposition to pay means the agent is always blackmailed, for an expected value of $-1{,}000$.
- A disposition to refuse means the agent is blackmailed only by error, for an expected value of $-\varepsilon\cdot 10^6$.

So A-FDT refuses iff $\varepsilon < 10^{-3}$. The paper's $\varepsilon=0.0009$ gives \$900 and refusal, as it says. Its claim that A-FDT pays at "0.011%" does not fit this arithmetic: that rate gives \$110 and still favors refusal. The intended figure was presumably 0.11%. The threshold derivation here is mine. Note what the rule implies: A-FDT may refuse while holding a letter it *knows* was sent in error, "because it's advantageous to be *the kind of agent* that makes such decisions."

### 4.7 Death in Damascus

Death's appointment book is a child of $F$.

- $\mathtt{do}(F=\textit{stay})$: Death is in Damascus, the agent dies, $V=0$.
- $\mathtt{do}(F=\textit{flee})$: Death is in Aleppo, the agent dies, $V=-1{,}000$.

A-FDT stays, stably, with no ratification loop. CDT, by contrast, oscillates, because its hypotheticals hold Death's location fixed while the act varies.

## 5. Counterfactuals, counterpossibles, and dominance

### Counterpossibles

A deterministic function has exactly one output on a given input. So $\mathtt{do}(F_x=a)$ for a non-actual $a$ is a *counterpossible*: its antecedent is logically false. The paper's ideal operator would be $\mathtt{true}(\phi)$, which updates $P$ as if the sentence $\phi$ held. The paper admits "it's not clear how to define a $\mathtt{true}$ operator." Equation (4) avoids defining one by taking the dependence graph $G$ as given input, in the same way that CDT takes the causal graph as given.

The paper calls the problem of learning $G$ "perhaps the largest open problem in the study of functional decision theory." Its defense has two parts. First, the difficulty is "technical rather than philosophical." Second, CDT faces a parallel puzzle: a deterministic agent's token act is equally fixed. In the paper's words, "Any principled objection to the idea that FDT agents can 'control' their decision type will also imply that (deterministic) CDT agents cannot 'control' their decision token."

### Dominance

The CDT argument from dominance holds the prediction fixed while the act varies. The paper argues that this argument assumes CDT's own hypotheticals. Every surgery rule induces its own dominance notion. Under A-FDT's notion, which holds subjunctive dependencies fixed, A-FDT never takes a dominated act. Dominance is therefore not neutral between theories, and the paper falls back on a single criterion: utility achieved in "fair" problems. Fair problems are those in which outcomes depend only on the agent's *behavior*, not on which procedure produced it.

## 6. What Equation (4) leaves open, and how I propose to fill it

Equation (4) is a real algorithm, but only relative to inputs it does not tell you how to construct. Applying it to unfamiliar cases requires decisions about at least five points.

**(a) Building $G$.** The paper gives criteria by example rather than by definition:

- A system that "builds an accurate model of the agent and reasons about her behavior" depends on $F$.
- A lesion that merely correlates with the agent's behavior does not.
- Causal dependence counts as a special case of subjunctive dependence.

*My operational proposal:* draw an edge $F_y\to Z$ iff $Z$'s mechanism takes as input a computation or simulation of the agent's procedure on input $y$, or something reliably equivalent to one. Model imperfect fidelity with an exogenous accuracy node, as the paper does with $\textsc{Accurate}$. When fidelity is partial, for example a predictor who models agents like you rather than you exactly, the paper offers no recipe. A reasonable extension is to treat fidelity as an uncertain parent with a prior, but that is my assumption.

**(b) Priors on the non-intervened function nodes.** In the transparent Newcomb and smoking lesion cases, the paper introduces a prior $q$ on the agent's *other* function node. It then remarks that the "correct" value is 0 or 1 "as you may verify, but it won't matter." In those examples it doesn't. In general it can, and this is exactly where A-FDT and policy-selection FDT come apart.

Here is a coordination example of my own. The agent receives input $r$ or $b$ with probability ½ each and must output $\alpha$ or $\beta$. Payoffs depend on the joint behavior of the function across both inputs, which a predictor evaluates:

| Output on $r$ | Output on $b$ | Payoff |
|---|---|---|
| $\alpha$ | $\alpha$ | 2 |
| $\beta$ | $\beta$ | 1 |
| mismatched | mismatched | 0 |

Suppose the agent sees $r$, and its prior on the sibling node is $P(F_b=\beta)=s$. Then

$$\mathbb E[V \mid \mathtt{do}(F_r=\alpha)] = 2(1-s), \qquad \mathbb E[V \mid \mathtt{do}(F_r=\beta)] = s.$$

So A-FDT picks $\beta$ whenever $s>2/3$. Both $(\alpha,\alpha)$ and $(\beta,\beta)$ are self-consistent: if the agent believes it plays $\beta$ elsewhere, it plays $\beta$ here, and the belief is correct. A-FDT can therefore lock into the inferior equilibrium. Policy-selection FDT maximizes over the pair $(F_r,F_b)$ jointly and picks $(\alpha,\alpha)$. This is my reconstruction of why the authors prefer policies. It is consistent with their footnotes but not demonstrated in the paper.

*My operational proposal for A-FDT as written:* require the sibling priors to be *reflectively consistent*, that is, a fixed point at which each $F_y$'s prior matches what A-FDT outputs on $y$. When several fixed points exist, acknowledge that Equation (4) alone does not select among them. In such cases A-FDT's verdict, like EDT's, is hostage to priors over its own behavior, though in a much narrower class of problems.

**(c) Ties and zero-probability branches.** Equation (4) uses argmax without a tie-breaking rule. Unlike EDT, it never conditions on the act, so a zero prior on an action does not exclude that action from consideration. This is a real advantage over EDT, which in the paper's cosmic-ray problem "cannot imagine taking \$100." If a tie-break is needed, any fixed rule is consistent with the paper.

**(d) Observations.** As argued in Section 2, I read Equation (4) literally and do not condition on $x$. A version that both conditions *and* moves the intervention point is, according to the paper, the "double update" of Timeless Decision Theory, "which proves harmful in practice."

**(e) Fairness.** The paper conjectures that A-FDT is optimal on "fair" problems. It concedes that it has not formalized fairness: a problem that punishes anyone who acts like a copy of Fiona defeats her trivially. Any claim of A-FDT optimality on a new problem class is therefore conjectural.

## 7. Philosophical motivation in brief

The paper's central picture is the calculator. Two well-functioning calculators on opposite sides of the globe agree on $6288+1048$. This is not because one causes the other but because they compute the same function. An accurate predictor is a calculator running your function, so it is "foolish to imagine her action changing without also imagining $\mathrm{FDT}(P, G)$ taking on a different value."

On this view:

- EDT's hypotheticals "respect too many correlations," including merely statistical ones like the lesion.
- CDT's hypotheticals "respect too few," breaking logically necessary correlations with predictors and twins.
- A-FDT tries to preserve "all and only" the dependencies on the agent's function.

The paper adds a "global perspective": the agent asks "What would the entire universe look like if the FDT algorithm behaved differently?" It also offers a reflective-stability argument. CDT advises self-modification away from CDT, whereas A-FDT, "so far as we know, [is] reflectively stable in fair problems."

The remaining discomfort is real, and the paper acknowledges it. Refusing a mechanical blackmailer while the program is already running, or leaving \$1,000 beside a visibly full box, are "odd conclusions." The defense rests on the primacy of achieved utility: "Parfit's desert is stacked high with the corpses of such agents."

## 8. Conclusion

A-FDT is CDT with the surgery moved. Instead of intervening on a physical act and conditioning on observations, it intervenes on the logical node "what this decision function outputs on my actual input." It then propagates that intervention through a graph that tracks every system depending on that output, including predictors, twins, and one's own future observations.

Applied with the paper's graphs, Equation (4) one-boxes in Newcomb's problem, smokes in the smoking lesion problem, pays the hitchhiker's driver, refuses both kinds of blackmail, cooperates with a twin, and stays in Damascus. It does all of this with one rule and no ratification.

Its open parameters are its weak points. Constructing the dependence graph, assigning priors to its own non-actual function nodes, and selecting among self-consistent fixed points are left unspecified. The last two are exactly where the authors' preferred policy-selection variant diverges from A-FDT. For new cases, the recipe of Section 3, together with the operational conventions of Section 6, is enough to compute a verdict. Readers should hold that verdict with confidence proportional to how clearly the problem determines who is computing, or modeling, their function.

---

**References**

- Yudkowsky, E. & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality.* arXiv:1710.05060.
- Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory.* Cambridge University Press.
- Pearl, J. (2000). *Causality.* Cambridge University Press.