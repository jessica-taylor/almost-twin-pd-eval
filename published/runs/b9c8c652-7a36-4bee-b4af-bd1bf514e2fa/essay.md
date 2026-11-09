# A-FDT: Action Functional Decision Theory, Explained and Operationalized

## 1. The question A-FDT asks

Yudkowsky and Soares (2017) describe *functional decision theory*. On their account, an agent should treat her decision as the output of a fixed mathematical function, and should ask: "Which output of this very function would yield the best outcome?" Causal decision theory (CDT) asks a different question: which physical act of mine *causes* the best outcome? Evidential decision theory (EDT) asks which act would be the best *news* to learn I took.

The paper formalizes this idea in Equation (4) of Section 5. That equation selects an **action**. In two footnotes (7 and 16), the authors mention that their "preferred formalization" instead iterates over **policies**, meaning maps from observations to actions. To keep the two apart, I use the following names:

- **A-FDT** (action functional decision theory) is the action-selecting rule of Equation (4). It is the subject of this essay.
- **Policy-FDT** is the policy-selecting variant that the footnotes describe only in words.

When I quote the source, its abbreviation "FDT" refers to the theory in general. I mark clearly which claims come from the paper and which are my own reconstructions.

## 2. The common framework

All three theories maximize expected utility in the form (paper's Eq. 1)

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j).
$$

Here $x$ is the observation history and $\hookrightarrow$ is a "decision hypothetical" connective. Following Joyce (1999), the paper treats the interpretation of $\hookrightarrow$ as the free parameter that separates the theories. The agent builds, for each action, a hypothetical $M^{a\hookrightarrow}$ from her world-model $M$. The authors stress that these hypotheticals are "decision-theoretic instruments constructed from beliefs," not beliefs themselves.

Write $V = \mathcal U(\textsc{Outcome})$. The three rules are then:

$$
\begin{aligned}
\text{EDT}(P,x) &= \arg\max_a \mathbb E[V \mid \textsc{Obs}=x,\ \textsc{Act}=a] \quad &(2)\\
\text{CDT}(P,G,x) &= \arg\max_a \mathbb E[V \mid do(\textsc{Act}=a),\ \textsc{Obs}=x] \quad &(3)\\
\text{A-FDT}(P,G,x) &= \arg\max_a \mathbb E\big[V \mid do(\textsc{fdt}(\underline P,\underline G,\underline x)=a)\big] \quad &(4)
\end{aligned}
$$

## 3. Anatomy of Equation (4)

Equation (4) has four ingredients.

**The distribution $P$.** $P$ ranges over ordinary empirical variables. It also ranges over variables standing for the *outputs of mathematical functions*. The paper's example is a variable for the value of $6288+1048$, which should place most of its mass on 7336.

**The graph $G$.** $G$ plays the role Pearl's causal graph plays for CDT. It tells us "how changing a logical variable affects all other variables." Its arrows encode *subjunctive dependence*, not only causation. The slogan is:

> "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

**The decision node.** I abbreviate it as $f_x \equiv \textsc{fdt}(\underline P,\underline G,\underline x)$. The underlines denote dequoting: the node's *name* is built from the agent's own model and observation. The self-reference is meant to be harmless. The agent does not need to know the node's *value* in order to represent it, and Kleene's recursion theorem ("quining") shows how such self-representing structures can be built.

**The intervention.** Pearl's $do$ operator is applied to $f_x$ rather than to the physical action. Every child of $f_x$ updates. The children include the agent's own action (in worlds where she receives input $x$), any predictor's model of her, and any twin running the same function. Everything that is not downstream of $f_x$ keeps its prior distribution.

The paper names two structural differences from CDT:

1. A-FDT intervenes on a logical node rather than the physical $\textsc{Act}$.
2. "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon."

Point 2 is easy to miss in Equation (4). **There is no conditioning on $\textsc{Obs}=x$.** The observation enters only through the *name* of the intervened node. The rest of this section is my own analysis of what that implies.

### 3.1 When does not conditioning matter? (my derivation)

Partition worlds by which observation the agent actually receives. In a world where she receives $y$, her action is set by $f_y$. Changing $f_x$ therefore affects a world in only two ways: the agent actually received $x$, or something in that world (a predictor, a twin, a simulation) computes the function on input $x$.

**Claim.** Suppose two conditions hold in $G$:

- (i) $\textsc{Obs}$ is not a descendant of $f_x$.
- (ii) In worlds with $\textsc{Obs}\neq x$, $V$ does not depend on $f_x$.

Then

$$
\mathbb E[V\mid do(f_x=a)] = P(\textsc{Obs}=x)\,\mathbb E[V\mid do(f_x=a),\ \textsc{Obs}=x] + P(\textsc{Obs}\ne x)\cdot c,
$$

where $c$ does not depend on $a$. If $P(\textsc{Obs}=x)>0$, A-FDT therefore agrees with the "update-then-intervene" rule. If, in addition, $f_x$ has no children except $\textsc{Act}$, it agrees with CDT.

This sharpens the paper's own remark that the three theories coincide when all correlations between $\textsc{Act}$ and other variables are caused by $\textsc{Act}$. In that case $\mathbb E[V\mid a]=\mathbb E[V\mid do(a)]=\mathbb E[V\mid do(\textsc{fdt}=a)]$.

A-FDT departs from CDT exactly when condition (i) or (ii) fails. Condition (i) fails when *what you observe* depends on how your function behaves, as in transparent Newcomb and blackmail. Condition (ii) fails when your function's output on $x$ matters even in worlds where you never see $x$. The agent has to "entertain the hypothesis that, if their action were different, they might have *made different observations*."

A textual caution belongs here. In the transparent Newcomb calculation, the paper's displayed objective includes "$\textsc{Obs}=\textit{full}$" inside the expectation. However, the computation that follows explicitly sums over the branch where box B is *empty*. The calculation, and therefore the operative definition, matches Equation (4) without conditioning. I follow Equation (4).

## 4. A recipe for applying A-FDT

The paper does not give a step-by-step procedure for new cases. The following is my distillation of how its worked examples proceed.

1. **Fix the input.** Identify the agent's actual observation $x$. The decision node is $f_x$.
2. **Find the subjunctive children of $f_x$.** Ask, for each variable: if this function, on this input, output something else, would this variable be different? Typical children are:
   - the agent's own action, in worlds where she receives $x$;
   - predictors' predictions, through their models of her;
   - twins and copies running the same function on the same input.
3. **Keep merely statistical correlates out.** Lesions, genes, and coincidences are not children of $f_x$, however strongly they correlate with the action. A lesion that influences *which function* the agent runs is a parent that selects the active node, not a child.
4. **Represent other inputs as separate nodes.** For each other input $y$ the agent might have received, include $f_y$ with some prior distribution. Selector nodes (for example "which box contents were shown") determine which $f$ node controls $\textsc{Act}$.
5. **Model imperfection with noise nodes.** An imperfect predictor gets an independent $\textsc{Accurate}$ node, as in the paper's Newcomb model.
6. **Compute and choose.** Compute $\mathbb E[V\mid do(f_x=a)]$ under the prior $P$ (not conditioned on $x$) for each $a$, and output the argmax.

## 5. Worked examples

All figures are in utility-dollars, as in the paper.

### Newcomb's problem (99% accurate predictor)

The node $f$ has two children: $\textsc{Act}$, and $\textsc{Prediction}$ via the predictor's model.

$$
\begin{aligned}
\mathbb E[V\mid do(f=\textit{one})] &= 0.99(1{,}000{,}000) + 0.01(0) = 990{,}000,\\
\mathbb E[V\mid do(f=\textit{two})] &= 0.01(1{,}001{,}000) + 0.99(1{,}000) = 11{,}000.
\end{aligned}
$$

A-FDT one-boxes. The agent does not believe in backward causation. Her prediction is that, if this very function output *two*, a competent model of that function would have output *two* as well.

### Psychological twin prisoner's dilemma

Both twins' actions are children of the shared node. Intervening with *cooperate* yields \$1,000,000, and intervening with *defect* yields \$1,000. A-FDT cooperates.

### Smoking lesion

The lesion determines the agent's tastes, and hence *which* decision function, $f_S$ or $f_R$, controls her action. Crucially, $\textsc{Cancer}$ is not a child of any $f$.

Let:

- $p = P(\text{lesion})$, which the intervention leaves unchanged;
- $q = P(f_R = \textit{smoke})$, the prior on how she would act with the other preferences.

The paper computes

$$
\begin{aligned}
\text{smoke: } & p(10{,}000+1{,}000) + (1-p)(990{,}000+1{,}000q),\\
\text{refrain: } & p(10{,}000) + (1-p)(990{,}000+1{,}000q).
\end{aligned}
$$

Smoking wins by $p\cdot 1{,}000$. So A-FDT one-boxes *and* smokes, which Gibbard and Harper (1978) had suggested no single principled rule could do.

### Transparent Newcomb and Parfit's hitchhiker

The agent sees box B full, so her node is $f_{\text{full}}$. The prediction depends on $f_{\text{full}}$. If the prediction says she will two-box, she sees an empty box, and $f_{\text{empty}}$ controls her action. Let $q = P(f_{\text{empty}}=\textit{two})$.

$$
\begin{aligned}
\text{one-box: } & 0.99(1{,}000{,}000) + 0.01(1{,}000q) = 990{,}000 + 10q,\\
\text{two-box: } & 0.01(1{,}001{,}000) + 0.99(1{,}000q) = 10{,}010 + 990q.
\end{aligned}
$$

(The source's printed figure for the second line contains a typographical slip, but the comparison is unaffected.) One-boxing wins for every $q\in[0,1]$.

Parfit's hitchhiker has the same structure. The node $f_{\text{in city}}$ influences the driver's lie-detection and therefore whether the agent ever reaches the city. A-FDT pays. These are the paper's cleanest examples of A-FDT beating both CDT and EDT.

### XOR blackmail (my verification of the paper's "as you may verify")

Assume an infallible predictor and termite prior $p$. The letter arrives iff exactly one of the following holds:

- (i) there are no termites and she would pay;
- (ii) there are termites and she would not pay.

Intervening on $f_{\text{letter}}$:

- **Pay:**
  - No termites: the letter is sent and she pays, losing 1,000.
  - Termites: no letter is sent, but the house is infested, losing 1,000,000.
  - Expected value: $-1{,}000(1-p) - 1{,}000{,}000\,p$.
- **Refuse:**
  - No termites: no letter is sent, so 0.
  - Termites: the letter is sent, and she suffers the infestation, losing 1,000,000.
  - Expected value: $-1{,}000{,}000\,p$.

Refusing is better by $1{,}000(1-p)$. Note what the agent imagines on the "pay" branch: in termite-worlds she never received the letter. The intervention changes *which observation* she receives, but never whether there are termites.

### Mechanical blackmail with an error rate (my computation of the threshold)

The blackmailer runs the program iff she predicts the agent would pay, except that with probability $\varepsilon$ she wrongly predicts payment. Intervening on $f_{\text{blackmail}}$:

- **Pay:** she is always blackmailed and pays, so $-1{,}000$.
- **Refuse:** she is blackmailed only with probability $\varepsilon$, and then refuses, so $-1{,}000{,}000\,\varepsilon$.

A-FDT refuses iff $\varepsilon < 0.001$. The paper's example $\varepsilon = 0.09\%$ (expected loss 900) gives *refuse*, which is correct. The paper says she pays at "0.011%". By this calculation that rate still gives *refuse* (expected loss 110). The switch occurs above 0.1%, so the printed figure was presumably meant as 0.11%.

The striking feature is that A-FDT refuses *while holding a letter it knows was sent by mistake*. In the paper's words, this is because it is "advantageous to be *the kind of agent* that makes such decisions."

### Death in Damascus

Death's appointment book depends on the agent's function, and Death is a perfect predictor. In both hypotheticals she dies. Fleeing costs an extra 1,000, so A-FDT stays.

CDT is unstable here. A-FDT is not, because it never imagines Death's book staying fixed while her output changes.

Now suppose a *truly* random coin is offered for \$1, one Death cannot predict. My extension of the analysis: under $do(f=\text{buy and follow coin})$ she survives with probability 1/2, so the expected value is about $500{,}000 - 500 - 1$. A-FDT buys the coin. The paper argues that CDT declines it.

## 6. What the source leaves open, and how one might close it

### 6.1 Where does $G$ come from?

This is the issue the paper itself emphasizes:

> "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

The idealized version would use a $\mathtt{true}$ operator: condition on the logical sentence "$f_x = a$" even when it is false. This requires counterpossible reasoning, and the authors admit "it's not clear how to define" such an operator. Equation (4) sidesteps the problem by taking $G$ as *input*, exactly as CDT takes the causal graph as input.

A-FDT is therefore a *conditional* procedure. Given a correct dependency graph, it yields a determinate answer, but it does not tell you how to obtain that graph.

My operational suggestion follows the paper's own models. Treat a system as a child of $f_x$ when its behavior is produced by computing, simulating, or reliably modeling the agent's function on input $x$. Represent degrees of reliability with independent noise nodes. The paper's calculator analogy supports this: two calculators agree "insofar as the calculator made no errors."

Partial similarity is harder: other agents who reason *somewhat* like you, or your future self on a slightly different day. The paper's gym example treats tomorrow's self as dependent "if there are no relevant differences." My proposal is to model partial similarity as a correlation strength in a noise node. This is an additional assumption, not something the paper specifies.

### 6.2 Beliefs about one's own behavior on other inputs

A-FDT intervenes only on $f_x$. Every $f_y$ with $y\ne x$ keeps its *prior* distribution: the parameter $q$ in the examples above. In each of the paper's examples, the result happens not to depend on $q$. The paper notes "it doesn't matter if Fiona has some uncertainty." In general, however, it can matter, and this is precisely where A-FDT and policy-FDT can come apart. The following example is mine.

**Two-room coordination.** Two exact copies of the agent are placed in separate rooms. One copy is shown *red* and the other *blue*, and both know the setup. Each copy chooses $A$ or $B$:

| Joint outcome | Payoff to each copy |
|---|---|
| Both choose $A$ | 10 |
| Both choose $B$ | 5 |
| Choices differ | 0 |

The red-room copy intervenes on $f_{\text{red}}$ and holds $f_{\text{blue}}$ at its prior, with $r = P(f_{\text{blue}}=A)$. Then

- $\mathbb E[V\mid do(f_{\text{red}}=A)] = 10r$,
- $\mathbb E[V\mid do(f_{\text{red}}=B)] = 5(1-r)$.

So A-FDT plays $A$ iff $r > 1/3$, and its output depends on its self-prediction. Both $(A,A)$ and $(B,B)$ are self-consistent: an agent that correctly believes it plays $B$ on blue will play $B$ on red, and vice versa.

Policy-FDT behaves differently. Formally (my rendering of the footnotes), it computes

$$
\pi^* = \arg\max_{\pi:\mathcal X\to\mathcal A}\mathbb E\big[V\mid do(\textsc{fdt}(\underline P,\underline G)=\pi)\big]
$$

and then outputs $\pi^*(x)$. It sets both nodes jointly and selects $(A,A)$. This illustrates the authors' remark that the policy formulation "makes a difference in certain multi-agent dilemmas."

When applying A-FDT, I therefore recommend the following:

- Check whether the argmax is invariant to the priors on the $f_y$. If it is, the answer is well-defined.
- If it is not, A-FDT is underdetermined until the agent supplies a self-model.
- A natural discipline is to require self-consistency: each $f_y$ should place its mass on A-FDT's own output on input $y$. This makes A-FDT's answer a fixed point, which may not be unique. Choosing among fixed points requires either an additional rule or a move to policy-FDT.

### 6.3 Ties and zero-probability observations

$\arg\max$ can return a set, and the paper specifies no tie-breaking rule. A sharper consequence follows from §3.1. If the prior gives $P(\textsc{Obs}=x)=0$ and nothing else computes $f_x$, then every action receives the same expected value, and A-FDT is silent.

This is the flip side of A-FDT's updatelessness. The prior $P$ must give positive weight to the observations the agent may actually face. Alternatively, one can adopt a fallback rule, such as conditioning on $x$ when the unconditioned expectation is flat. That fallback is my proposal, not the paper's.

### 6.4 Which prior?

The examples use a model whose $P$ covers *all* branches, including ones the agent knows she is not in, such as the empty-box world. A-FDT therefore requires the agent to retain a model that predates the observation, rather than replacing it with its posterior. The paper does not say how far back this "prior" should reach: before the predictor acted, or before the agent was born. The examples all use the natural modeling choice of the start of the dilemma.

## 7. The philosophical case, briefly

The paper's arguments for A-FDT are mainly three.

**Utility.** Measured by what agents tend to get, A-FDT agents one-box, cooperate with twins, smoke harmlessly, get rescued from the desert, and are not blackmailed. The authors call this "the one that gives the precommitment and value-of-information arguments their teeth."

**Dominance is not neutral.** "Every expected utility theory comes with its own notion of dominance." CDT's dominance argument for two-boxing holds the prediction fixed while the action varies. To the A-FDT agent, this is like imagining a working calculator outputting the wrong sum. Under subjunctive-dependence dominance, A-FDT never takes a dominated act.

**Fairness and reflective stability.** Newcomb's predictor "doesn't punish rational agents; she punishes *two-boxers*." The authors conjecture that A-FDT does at least as well as its rivals on every "fair" problem, though they concede that fairness is not yet formalized. A-FDT also acts as it would have precommitted to act, so it has no reason to self-modify. CDT, by contrast, recommends that agents stop using it.

The paper also answers the "control" objection. A deterministic CDT agent can no more "really" vary its action token than an A-FDT agent can vary its function's output. Both theories rely on useful impossible hypotheticals, so the objection cannot favor one over the other.

## 8. Conclusion

A-FDT is CDT's surgery moved from the physical act to the logical output of the agent's own decision function on her actual input. It keeps every subjunctive dependence (twins, predictors, simulations) and severs merely statistical correlations. Observations do not condition the expectation. They only select which node is intervened upon.

From this one rule follow one-boxing, smoking, paying the driver, refusing blackmail, and calm acceptance in Damascus. In ordinary cases where nothing predicts the agent, A-FDT coincides with CDT.

Its open edges are real:

- The dependency graph must be supplied, since counterpossible reasoning is unformalized.
- The answer can hinge on the agent's beliefs about her own outputs on other inputs.
- Ties and zero-probability observations are unaddressed.

The second issue is where A-FDT and the authors' policy-selecting variant diverge. In practice, it is the first thing to check when deciding an unfamiliar case.

## References

- Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge UP.
- Pearl, J. (2000). *Causality*. Cambridge UP.
- Yudkowsky, E. & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.