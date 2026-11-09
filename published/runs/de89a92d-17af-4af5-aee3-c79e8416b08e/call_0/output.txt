# A-FDT: Choosing the Output of a Fixed Function

## 0. Scope and naming

The source paper (Yudkowsky and Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*) calls its proposal "functional decision theory." This essay is about the specific procedure the paper gives as Equation (4) of Section 5, which I call **A-FDT**. I read the "A" as marking that the procedure selects an *action*. The paper's footnotes 7 and 16 say the authors' preferred formalization selects a *policy* (a map from observations to actions) and that "the difference only matters in multi-agent dilemmas so far as we can tell." Equation (4) and everything below are the action version.

I try to keep three things apart:

- **Source**: what the paper defines or claims.
- **Derived**: what follows by calculation from the source.
- **Proposed**: my own interpretive or operational additions, marked as such.

Other theories appear under distinct names. CDT is causal decision theory and EDT is evidential decision theory. The paper also mentions FDT$'$ (a rejected variant), Wei Dai's updateless decision theory, and Yudkowsky's timeless decision theory.

## 1. The idea in one paragraph

The paper's slogan is that a decision should be treated "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" CDT intervenes on a physical act and lets only its causal consequences vary. A-FDT intervenes on a *logical* variable, the output of the agent's own decision procedure on its actual inputs. Everything that *subjunctively depends* on that output varies with it: the agent's body, a twin's choice, a predictor's model of the agent. Everything else is held fixed.

## 2. The formal definition

### 2.1 Shared scaffolding

All three theories are expected-utility theories. Equation (1) says to maximize
$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\cdot \mathcal U(o_j),$$
where $P(a\hookrightarrow o_j; x)$ is the probability of outcome $o_j$ "in the hypothetical scenario where the action $a$ is executed after receiving observations $x$." The theories differ only in how they interpret $\hookrightarrow$. The paper leans on Joyce's representation theorem here: the theories disagree about "the epistemic perspective from which actions are to be evaluated," not about value.

For each action $a$ the agent builds a *hypothetical*, a scratch-paper object derived from her world-model $M$, and scores it. Hypotheticals are "decision-theoretic instruments constructed from beliefs," not beliefs themselves.

With $V := \mathcal U(\textsc{Outcome})$:

- **EDT** (Eq. 2): $\arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a)$. It conditions.
- **CDT** (Eq. 3): $\arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x)$. It intervenes on the act and conditions on observations. The model is a pair $(P,G)$, where $G$ is a causal graph.

### 2.2 Equation (4)

$$\textbf{A-FDT}(P,G,x) \;:=\; \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsf{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

Here $\textsf{fdt}(\underline P,\underline G,\underline x)$ is a node in the model. It stands for the value of A-FDT itself when run on inputs $P$, $G$, $x$. The underlines denote "dequoting": the node's name is built from the actual inputs. This looks circular, since the model contains a variable named after a function of the model. The paper answers that the self-reference is harmless. The agent need not know the *value* of $\textsf{fdt}(P,G,x)$ to have a variable *representing* it, and Kleene's second recursion theorem ("quining") shows how a data structure can contain an accurate representation of itself.

Two things distinguish A-FDT from CDT, as the paper says:

1. **Different intervention site.** CDT intervenes on a physical-act node. A-FDT intervenes on the node for its procedure's output.
2. **Observation changes the node, not the distribution.** When CDT's observation changes from $x$ to $y$, it changes what it conditions on. When A-FDT's observation changes, it changes *which node it intervenes on*, from $\textsf{fdt}(\underline P,\underline G,\underline x)$ to $\textsf{fdt}(\underline P,\underline G,\underline y)$. Equation (4) contains no $\textsf{Obs}=x$ conditioning term.

The paper also writes a conceptual version, $\arg\max_a \mathbb E(V\mid \mathtt{true}(\textsf{fdt}(\underline P,\underline x)=a))$. For it, "it's not clear how to define a $\mathtt{true}$ operator," since the sentence being made true is a (counter)logical falsehood. Equation (4) avoids the problem by requiring the model to arrive with a graph $G$ "that tells us how changing a logical variable affects all other variables." Pearl's $\mathtt{do}$ is then reused as is. In other words, the logical dependency structure is an *input*, as causal structure is for CDT (footnote 9).

### 2.3 Semantics of the intervention (derived from Pearl)

Setting a node by $\mathtt{do}$ means:

1. Fix the node's value to $a$.
2. Cut its incoming edges, so its own parents no longer influence it.
3. Recompute every descendant from its structural equation, using the new value.
4. Leave every non-descendant with its prior distribution.

In the paper's graphs the $\textsf{fdt}$ node has arrows into $\textsc{Act}$ and into any node that models or copies the agent. Stochastic nodes such as $\textsc{Accurate}$ (predictor reliability) stay at their priors, and the other variables are deterministic functions of their parents.

**Agreement with CDT and EDT in simple cases (source).** If every correlation between $\textsc{Act}$ and the rest of the world is caused by $\textsc{Act}$, then $\mathbb E[V\mid a]=\mathbb E[V\mid\mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\textsf{fdt}=a)]$, and all three theories agree.

**Observations (derived, my own short argument).** Suppose the observation $\textsc{Obs}$ does *not* depend on the $\textsf{fdt}$ nodes, for instance a fair coin that the payoff depends on. Each $\textsf{fdt}(\cdot,\cdot,y)$ governs $\textsc{Act}$ only in worlds where $\textsc{Obs}=y$. Intervening on $\textsf{fdt}(\cdot,\cdot,x)$ therefore changes $V$ only in $\textsc{Obs}=x$ worlds, and the other worlds add an $a$-independent constant. So $\arg\max_a$ of the unconditioned expectation equals $\arg\max_a$ of the expectation conditioned on $\textsc{Obs}=x$. A-FDT then looks like CDT with ordinary updating. It departs from updating only when the *observation itself* is downstream of the $\textsf{fdt}$ nodes, as when a predictor decides which observation the agent sees. That is exactly the transparent Newcomb and blackmail cases below.

One loose end in the source. In the transparent Newcomb calculation the paper writes the expectation as $\mathbb E(V\mid\mathtt{do}(\textsf{fdt}(\ldots,\textit{full})=a,\ \textsc{Obs}=\textit{full}))$, but the arithmetic it then performs sums over both the full-box and empty-box branches. So $\textsc{Obs}=\textit{full}$ is not used as a conditioning event; it labels which node is intervened on. I follow the calculation and Equation (4).

### 2.4 The procedure as an algorithm

1. Take the model $(P,G)$ and the actual observation $x$.
2. Locate (or construct) the node $\textsf{fdt}(\underline P,\underline G,\underline x)$. $G$ must show which variables depend on it.
3. For each $a\in\mathcal A$, perform $\mathtt{do}(\textsf{fdt}(\underline P,\underline G,\underline x)=a)$ and compute $\mathbb E(V)$.
4. Output the maximizer.

The paper stresses that $P$ and $G$ describe the agent's *model* of her situation, and that its evaluations assume the models are accurate. Nothing in A-FDT corrects a wrong model.

## 3. Subjunctive dependence: what is given and what is open

### 3.1 What the source says

Subjunctive dependence is the relation that holds between two systems when they compute the same function, or when one contains an accurate representation of the other's computation. The standard illustration is two calculators computing $6288+1048$. The source's claims about it are these:

- Causal dependence is a special case: a scribe copying a calculator's output depends on it subjunctively as well as causally.
- Mere statistical correlation does not entail subjunctive dependence. Two calculators that are both pink by coincidence are not subjunctively linked, because with a different Paris calculator, Tokyo's would stay pink.
- Weakened versions exist. A noisy predictor or a nondeterministic agent weakens the dependence without eliminating it.
- Evaluating "what if this function output something else?" requires reasoning about *counterpossibles*. The source says this is "the main drawback" of the theory and that "the difficulty here is technical rather than philosophical."

The paper rejects FDT$'$, the variant that asks "what if I used a different decision function $f_n\in\mathcal F$?" The predictor still predicts $d$, so FDT$'$ would have to imagine all predictors of $d$ predicting as if $d$ behaved like $f_n$, which is the same counterpossible task.

### 3.2 What is open

The paper says that "figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem." Equation (4) works *given* an accurate $G$, and the paper does not say how to get one, "nor even whether it can be done in a satisfactory manner within Pearl's framework." So A-FDT as written is a decision procedure *relative to* a dependency graph, not a method for discovering one. Different graphs will give different recommendations, and the source offers no criterion beyond the examples.

### 3.3 A proposed operational heuristic (mine, not the paper's)

For a candidate variable $Z$ in a decision problem, ask three questions:

1. **Computation.** Is some process that sets $Z$ computing, simulating, or reasoning from a representation of *this very procedure on these inputs*? If so, draw an edge $\textsf{fdt}\to Z$. The edge is deterministic if the representation is perfect and noisy if not. A twin or a predictor passes. A lesion does not.
2. **Proxy test.** If $Z$ merely correlates with the agent's choice, would the correlation survive if the procedure's output were different but the process generating $Z$ were unchanged? A lesion's cancer-risk effect survives; a predictor's prediction does not. Keep edges only for dependencies that fail this test.
3. **Which node.** If the observation is itself downstream of a prediction, as when the predictor decides what you see, model the observation as a child of the predictor and give the agent one $\textsf{fdt}$ node per possible observation.

This is not a general theory. It encodes the paper's own contrast between predictors and lesions, and it will be hard to apply when the "predictor" is a murky physical process or a human. The paper's remark that people "have some ability to notice when they are being predicted" suggests that such judgment is routinely exercised, but does not formalize it.

## 4. Worked applications

I use the paper's dollar-denominated utilities.

### 4.1 Newcomb's problem

The graph has $\textsf{fdt}\to\textsc{Act}$ and $\textsf{fdt}\to\textsc{Prediction}\to\textsc{Box B}$. Predictor reliability is 0.99.

- $\mathtt{do}(\textsf{fdt}=\textit{onebox})$: $\textsc{Act}=\textit{onebox}$ and the box is full with probability 0.99. $\mathbb E V = 0.99\cdot 10^6 = 990{,}000$.
- $\mathtt{do}(\textsf{fdt}=\textit{twobox})$: the box is full with probability 0.01. $\mathbb E V = 0.01\cdot 1{,}001{,}000 + 0.99\cdot 1000 = 11{,}000$.

A-FDT one-boxes. (The paper reports EDT's figure for one-boxing as $999{,}000$, but $0.99\times 10^6 = 990{,}000$; the ranking is unaffected.)

The agent is not claiming retrocausation. In the paper's words, "she just thinks it is foolish to imagine her action changing without also imagining $\textsf{fdt}$ taking on a different value, since she thinks the predictor is good at reasoning about" her. The objection "she's nearly sure the box is full, so shouldn't she two-box?" fails because the question "what if I two-boxed?" is answered by the do-hypothetical, not by her current credences.

### 4.2 Twin prisoner's dilemma, with a noisy twin (my extension)

If the twin runs the same function, $\textsf{fdt}$ sets both acts. Cooperating yields $10^6$ and defecting yields $10^3$, so A-FDT cooperates. Now suppose the twin copies the output only with probability $r$, and otherwise does the opposite. This noise model is my assumption.

$$\mathbb E[V\mid\text{C}] = r\cdot 10^6,\qquad \mathbb E[V\mid\text{D}] = r\cdot 10^3 + (1-r)\cdot 1{,}001{,}000.$$

Cooperation wins iff $2{,}000{,}000\,r > 1{,}001{,}000$, that is, $r>0.5005$. So the dependency must be better than a coin flip by a small margin before A-FDT cooperates.

### 4.3 Transparent Newcomb and Parfit's hitchhiker

Here the observation (full or empty box) is downstream of the prediction. $\textsc{Act}$ is controlled by $\textsf{fdt}(\ldots,\textit{full})$ when the predictor predicted one-boxing and by $\textsf{fdt}(\ldots,\textit{empty})$ otherwise. Let $q$ be the agent's credence that she two-boxes on seeing an empty box. The paper computes:

- $\mathtt{do}(\textsf{fdt}(\textit{full})=\textit{onebox})$: $990{,}000 + 10\,q$.
- $\mathtt{do}(\textsf{fdt}(\textit{full})=\textit{twobox})$: $10{,}010 + 990\,q$.

(The paper's printed "$110{,}00$" seems to be a typo for $10{,}010$; this follows from its own setup.) The difference is $979{,}990 - 980q>0$ for all $q\in[0,1]$, so A-FDT one-boxes even when the box is visibly full. When it imagines two-boxing, it imagines a world where it "instead (with high probability) sees that the box is empty." The paper argues this is the same structure as paying the driver in Parfit's hitchhiker problem.

### 4.4 Smoking lesion

The paper models the lesion as determining which of two decision procedures runs: $\textsf{fdt}(P_S,G)$ if she has the lesion and $\textsf{fdt}(P_R,G)$ if not. Intervening on $\textsf{fdt}(P_S,G)$ changes $\textsc{Act}$ but not $\textsc{Cancer}$, since the lesion is not downstream. Smoking beats refraining by $p\cdot\$1000$, where $p$ is the probability that this procedure is the one controlling her action. A-FDT smokes. So one criterion both one-boxes and smokes, with no ratification or tickle defense. The paper itself says the problem is contrived and recommends that philosophers abandon it.

### 4.5 Blackmail, and where the thresholds fall

*Mechanical blackmail.* The blackmailer runs her program iff she predicts the agent would pay. Intervening on $\textsf{fdt}(\ldots,\textit{blackmail})$ moves both the agent's action and the probability of being blackmailed. If the blackmailer errs with probability $\varepsilon$:

- Refuse: blackmailed with probability $\varepsilon$, losing $10^6$, so the expected loss is $10^6\varepsilon$.
- Pay: blackmailed with probability $\approx 1-\varepsilon$, losing $1000$ each time, so the expected loss is $\approx 1000$.

The break-even is $\varepsilon\approx 0.1\%$. The paper's example with $\varepsilon=0.0009$ (expected loss $\$900$ from refusing) gives refusal, which matches. Its second example, "0.011%", would give an expected loss of only $\$110$ from refusing, so by this arithmetic A-FDT would still refuse. I read it as a typo for roughly 0.11%, which would flip the decision to paying. Either way the logic stands: the agent takes whichever action corresponds to the better *hypothetical*, even while holding the letter. The source says explicitly that this "even means imagining worlds in which her observations were different."

*XOR blackmail.* The infestation is not downstream of $\textsf{fdt}$, but the letter's arrival is. Intervening on $\textsf{fdt}(\ldots,\textit{letter})$ changes whether she gets the letter, not whether she has termites. A-FDT refuses. EDT pays, because conditioning on $\textsc{Act}=\textit{pay}$ drives the termite probability to 0.

*Death in Damascus.* The appointment-book entry depends on the agent's procedure. Staying yields $-\$0$ relative to a lost life and fleeing costs an extra $\$1000$, so A-FDT stays. There is no oscillation, because the hypothetical moves Death along with the choice.

### 4.6 Counterfactual mugging (my application, not in the paper)

A fair coin is flipped. On tails, a predictor asks for $\$100$. On heads, it pays $\$10{,}000$ iff it predicts that the agent would pay on tails. Model the coin as exogenous and the predictor as a child of $\textsf{fdt}(\ldots,\textit{tails})$. The agent has seen tails and must decide.

Intervening on $\textsf{fdt}(\ldots,\textit{tails})=\textit{pay}$ gives $\tfrac12(10{,}000)+\tfrac12(-100)=4{,}950$. Refusing gives $0$. A-FDT pays. This follows the structure of the paper's blackmail analysis. It requires $P$ to be the model as it stood *before* the coin result was incorporated, with the coin an ordinary random node. This is an assumption I flag in §5. The paper does not discuss this case, but treating observations as selecting an intervention node rather than as evidence points the same way.

## 5. Interpretive issues the source leaves open

**The prior $P$.** Because A-FDT does not condition on $x$, the model $P$ must treat the observation as a random variable that can be upstream or downstream of the decision. The paper's examples do this. A model that is *already* conditioned on $x$ would destroy the dependence A-FDT is meant to exploit. So the right $P$ is the agent's best model of the situation as a stochastic process containing her observation, not her posterior. That is an assumption, but one the paper's calculations require.

**Beliefs about other nodes.** A-FDT intervenes on one node, $\textsf{fdt}(\ldots,x)$. The nodes for other observations keep priors, the $q$ in the transparent Newcomb calculation. In the paper's examples the answer does not depend on $q$, and "the correct $q$" is stated, but the paper does not say what $q$ should be in general. A reasonable rule (my proposal) is for the agent to set it to her best estimate of what the same procedure outputs on that other input, or to check that the choice is robust across $q\in[0,1]$. Where robustness fails, the policy version the authors prefer (footnotes 7 and 16) would be the cleaner object. A-FDT as written is silent.

**Dominance.** A-FDT agents do not accept the CDT argument that two-boxing dominates. The paper's reply is that "every method for constructing hypotheticals gives rise to its own notion of dominance." Two-boxing dominates under CDT counterfactuals and refraining dominates under EDT ones. Holding fixed the subjunctive dependency instead, A-FDT agents never take a dominated action. The paper concludes that dominance is not a neutral arbiter between theories and prefers utility achieved as the criterion.

**Fairness.** The paper restricts its superiority claim to "fair" problems: those where the agent's beliefs are accurate and the payoff depends only on her behavior in the problem at hand, not on which procedure she implements. A predictor who rewards only agents who run CDT is unfair to A-FDT. The paper admits it has no formal criterion for fairness (footnote 15 gives a copy-punishing counterexample). So the paper's claim that it knows of no fair dilemma where the theory loses is an *empirical* claim, not a theorem.

**"Delusion."** One objection is that an agent who treats her decision procedure's output as variable is deluded, since a deterministic function has one output. The paper replies that CDT faces the same problem in a deterministic world. If "control" over the type is problematic, so is control over the token. Both theories rely on imagined worlds that cannot all be actual.

**What A-FDT does not do.** It does not tell you the graph. It does not choose utilities. It does not fix an agent whose model is wrong. It does not resolve counterpossible reasoning in general. The paper makes only the weaker claim that agents need to reason about questions like "how would this predictor's prediction change if the algorithm had a different output?"

## 6. Conclusion

A-FDT is an expected-utility rule that differs from CDT in exactly two places: it intervenes on the node for the decision procedure's output instead of the physical act, and it responds to observation by switching which node it intervenes on rather than by conditioning. Given a model $(P,G)$ in which the graph encodes subjunctive dependence, the rule is a short mechanical computation, and it yields the paper's verdicts on the problems above. It one-boxes in Newcomb's problem, smokes in the smoking lesion problem, pays in Parfit's hitchhiker problem, refuses blackmail, and stays in Damascus. The cost of this simplicity is that all the hard work is pushed into constructing $G$, which the source treats as an open problem. The heuristics in §3.3 and the readings in §5 are my best attempt to make the rule usable on new cases. A reader applying A-FDT should always state the graph explicitly, check that the answer survives plausible changes to it, and be clear that the recommendation is only as good as the dependency structure fed in.