# A-FDT: Action Functional Decision Theory, Explained and Operationalized

## 1. What this essay is about

Yudkowsky and Soares introduce *functional decision theory* in "Functional Decision Theory: A New Theory of Instrumental Rationality." They describe its normative principle as treating one's decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" The paper gives several formal and informal versions of this idea. This essay treats one of them as primary: **Equation (4) of Section 5**, in which the agent intervenes on a node representing the *action* output by its decision function, given its actual observation.

I call this version **A-FDT** (action functional decision theory). The source simply calls it "FDT." I use the separate label because the authors say that their own preferred formalization is a different one:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper." (footnote 7)

I will call that alternative **policy FDT**. I also discuss **CDT** (causal decision theory) and **EDT** (evidential decision theory).

Throughout, I separate two kinds of claim. Some come from the paper. Others are my own operational proposals, which I flag explicitly.

## 2. The common skeleton: expected utility over hypotheticals

The paper presents EDT, CDT and A-FDT as three instances of one schema. Given an observation history $x$, the agent executes an action $a \in \mathcal{A}$ that maximizes

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}
$$

Here $P(a \hookrightarrow o_j; x)$ is the probability of outcome $o_j$ "in the hypothetical scenario where the action $a$ is executed after receiving observations $x$."

Following Joyce, the authors treat the connective $\hookrightarrow$ as the free parameter. The theories agree about how to value prospects. They disagree about the "epistemic perspective" from which actions are evaluated.

Operationally, the agent holds a world-model $M$. For each candidate $a$ it builds a *hypothetical* $M^{a\hookrightarrow}$, which the paper describes as "decision-theoretic instruments constructed from beliefs," not beliefs in their own right. It then scores each hypothetical by expected utility. The theories differ in two places: what $M$ must contain, and how hypotheticals are built from it.

With $V := \mathcal U(\textsc{Outcome})$:

$$
\mathrm{EDT}(P,x) = \arg\max_{a} \mathbb E\big(V \mid \textsc{Obs}=x,\ \textsc{Act}=a\big) \tag{2}
$$

$$
\mathrm{CDT}(P,G,x) = \arg\max_{a} \mathbb E\big(V \mid \mathtt{do}(\textsc{Act}=a),\ \textsc{Obs}=x\big) \tag{3}
$$

EDT conditions. CDT performs Pearl-style surgery on the physical action node of a causal graph $G$.

## 3. The definition of A-FDT

Equation (4) of the paper reads:

$$
\boxed{\;\mathrm{A\text{-}FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big)\;} \tag{4}
$$

The ingredients are as follows.

- **$P$** is a probability distribution over variables. Some of these variables represent *logical* facts: the outputs of mathematical functions on particular inputs.
- **$\textsc{fdt}(\underline P,\underline G,\underline x)$** is a variable in the model whose value represents what the A-FDT algorithm outputs when run on this very model and this very observation. The underlines denote dequoting, so the variable's *name* is built from the inputs. The self-reference is defended as harmless. The agent need not know the variable's value in order to represent it, and Kleene's recursion theorem ("quining") shows how such self-representing structures can be built.
- **$G$** is a graph telling the agent "how changing a logical variable affects all other variables." It is the analogue of CDT's causal graph, extended to logical, computational and causal structure.
- **$\mathtt{do}$** is Pearl's intervention operator, reused unchanged. The node is set to $a$, everything downstream in $G$ is recomputed, and everything else keeps its prior distribution.

Ideally one would write $\mathbb E(V \mid \mathtt{true}(\textsc{fdt}(\ldots)=a))$, a "counterpossible" update on a logical sentence that may be false. The authors concede, "it's not clear how to define a $\mathtt{true}$ operator." Equation (4) sidesteps the problem by requiring that the dependency structure be *given* in $G$, just as CDT requires causal structure to be given.

**Two differences from CDT** (stated in the source):

1. *Point of intervention.* CDT intervenes on the token $\textsc{Act}$. A-FDT intervenes on the type: the output of the decision function. Everything that subjunctively depends on that output moves with it. This includes the agent's own body, but also twins, predictors and simulations.
2. *Treatment of observations.* CDT conditions on $\textsc{Obs}=x$. A-FDT instead uses $x$ to *select which node to intervene on*. When the observation changes from $x$ to $y$, A-FDT switches from intervening on $\textsc{fdt}(\underline P,\underline G,\underline x)$ to intervening on $\textsc{fdt}(\underline P,\underline G,\underline y)$.

The second point has a consequence that is easy to miss: **Equation (4) contains no conditioning on $\textsc{Obs}=x$**. I return to this in §6.

**Agreement in ordinary cases.** The paper observes that the three theories coincide whenever every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, except for $\textsc{Act}$'s own dependence on the $\textsc{fdt}$ node. In that case

$$
\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid\mathtt{do}(\textsc{fdt}=a)].
$$

Divergence requires something else in the world that tracks the agent's decision function, such as a predictor or a copy.

## 4. Subjunctive dependence: what the graph must encode

The conceptual core of A-FDT is **subjunctive dependence**. The source says that "when two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." It offers three reference points:

- **Causal dependence is a special case.** A scribe copying a calculator's output would write something different if the output were different.
- **Mere correlation is not dependence.** Two coincidentally pink calculators illustrate this: repainting one leaves the other pink.
- **Imperfect computation still counts.** If a predictor's model is noisy, "the interdependence is weakened, but not eliminated."

The paper's central normative assumption is that

> "when an FDT agent imagines herself taking two different actions, she imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

The paper is candid that it gives no general procedure for building $G$:

> "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

### A recipe for building the graph (my proposal)

To apply A-FDT to unfamiliar cases, I suggest the following recipe. It is consistent with every example in the paper, but it is my reconstruction, not the source's.

1. **Identify the decision function and its possible inputs.** For every observation $y$ the agent might face in the problem, include a logical node $f_y := \textsc{fdt}(\underline P,\underline G,\underline y)$.
2. **Find every process that computes, simulates or predicts $f_y$.** This includes the agent's motor system, predictors, twins and future selves facing the same input. Draw an edge from $f_y$ to each such process. Model imperfect fidelity with an independent noise node, as in the paper's $\textsc{Accurate}$ node.
3. **Connect action to observation.** Make $\textsc{Act}$ a deterministic selector: $\textsc{Act}=f_y$ when the observation that actually arises is $y$. The variables that determine which observation arises, such as the box contents or whether a letter was sent, become parents of $\textsc{Act}$.
4. **Leave lesion-like factors upstream.** Common causes that do not evaluate the function, such as a genetic lesion, are *not* children of any $f_y$. The test question is: "if this function's output on this input were different, holding fixed everything not computed from it, would this variable differ?"
5. **Give non-intervened nodes their prior.** The nodes $f_y$ for $y \neq x$ keep the agent's prior beliefs about what A-FDT would output on those inputs.
6. **Compute Equation (4).** Intervene on $f_x$ and propagate downstream, without conditioning on $x$.

## 5. Worked examples

### Psychological twin prisoner's dilemma

Both twins' acts are children of the same node $f$.

- $\mathtt{do}(f=\textit{cooperate})$ yields mutual cooperation, worth \$1,000,000.
- $\mathtt{do}(f=\textit{defect})$ yields mutual defection, worth \$1,000.

A-FDT cooperates. EDT also cooperates, but by conditioning. CDT defects, because surgery on the token $\textsc{Act}$ leaves the twin's behavior untouched.

### Newcomb's problem (99% accurate predictor)

The graph is $f\to\textsc{Act}$ and $f\to\textsc{Prediction}\leftarrow\textsc{Accurate}$, with $\textsc{Prediction}\to\textsc{Box B}$.

$$
\begin{aligned}
\mathbb E[V\mid\mathtt{do}(f=\textit{onebox})] &= 0.99(1{,}000{,}000) = 990{,}000,\\
\mathbb E[V\mid\mathtt{do}(f=\textit{twobox})] &= 0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000.
\end{aligned}
$$

A-FDT one-boxes. (The source's text gives Eve's EDT figure as "\$999,000," evidently a typo for \$990,000.)

The authors stress that no retrocausation is assumed. The agent simply refuses to imagine her action diverging from a competent prediction of the same function. They use the analogy of "two well-functioning calculators" computing $6288+1048$.

A notable feature is that the prior on $f$ is irrelevant. The $\mathtt{do}$ operator overrides it. A-FDT therefore avoids EDT's problem with zero-probability actions and needs no ratification step.

### Smoking lesion

The lesion determines which utility function the agent has, and so which of two nodes, $f_S$ or $f_R$, controls the action. $\textsc{Cancer}$ hangs off $\textsc{Lesion}$, not off either node.

Intervening on $f_S$ leaves $P(\textit{lesion})=p$ unchanged. The two hypotheticals differ only by the smoking bonus in the branch where $f_S$ controls the act. Smoking wins by $p\cdot\$1{,}000$.

Here A-FDT smokes, and it one-boxes in Newcomb's problem. This combination is exactly what Gibbard and Harper thought no coherent rule could deliver. The difference lies entirely in $G$: a predictor evaluates the function, whereas a lesion does not.

### Transparent Newcomb (observation: both boxes full)

There are two nodes, $f_F$ (the output on seeing a full box) and $f_E$ (the output on seeing an empty box). The predictor fills box B iff it predicts one-boxing-on-full, so $\textsc{Prediction}$ is a child of $f_F$ and $\textsc{Accurate}$. The action is $f_F$ if the box is full and $f_E$ otherwise. Let $q=P(f_E=\textit{twobox})$.

$$
\begin{aligned}
\mathbb E[V\mid\mathtt{do}(f_F=\textit{onebox})] &= 0.99(1{,}000{,}000)+0.01\,q(1{,}000)=990{,}000+10q,\\
\mathbb E[V\mid\mathtt{do}(f_F=\textit{twobox})] &= 0.01(1{,}001{,}000)+0.99\,q(1{,}000)=10{,}010+990q.
\end{aligned}
$$

One-boxing wins for every $q\in[0,1]$. (The paper's printed second figure, "\$110,00 + q·\$990," is a typo for \$10,010 + 990q.)

A-FDT leaves the visible \$1,000 behind. The source treats this as equivalent to paying the driver in **Parfit's hitchhiker** problem, which A-FDT also does.

### XOR blackmail

Infestation, with prior $p$, is upstream of everything else. The letter is sent iff either (no termites and $f_L=\textit{pay}$) or (termites and $f_L=\textit{refuse}$).

$$
\begin{aligned}
\mathbb E[V\mid\mathtt{do}(f_L=\textit{pay})] &= -p\cdot 10^6-(1-p)\cdot 10^3,\\
\mathbb E[V\mid\mathtt{do}(f_L=\textit{refuse})] &= -p\cdot 10^6.
\end{aligned}
$$

A-FDT refuses, because the intervention cannot touch the termites. EDT pays. CDT also refuses, but its hypothetical for paying depicts an infallible predictor erring.

### Mechanical blackmail with fallible blackmailer

The blackmailer runs the program iff it predicts payment, but wrongly predicts payment with probability $\varepsilon$.

- $\mathtt{do}(f_B=\textit{pay})$: the agent is blackmailed almost surely and loses about \$1,000.
- $\mathtt{do}(f_B=\textit{refuse})$: the agent is blackmailed with probability $\varepsilon$ and then loses \$1,000,000.

A-FDT therefore refuses exactly when $\varepsilon\cdot 10^6 < 10^3$, that is, when $\varepsilon<0.001$. This matches the source's verdict at $\varepsilon=0.0009$: refuse, with expected loss \$900.

The source's second case is printed as "0.011%." That would still recommend refusal, so the intended figure must be about 1.1%, at which paying is correct.

The threshold shows how A-FDT handles imperfect predictors. Dependence weakens continuously with $\varepsilon$, and the verdict tracks it. A-FDT may refuse even while holding a letter it *knows* was sent in error, because "it's advantageous to be *the kind of agent* that makes such decisions."

### Death in Damascus

Death's appointment book is a perfect prediction, so Death's location is a child of $f$.

$$
\mathbb E[V\mid\mathtt{do}(f=\textit{Damascus})]=0,\qquad \mathbb E[V\mid\mathtt{do}(f=\textit{Aleppo})]=-1{,}000.
$$

A-FDT stays home, and the verdict does not depend on its prior about its own action. CDT instead oscillates between the two options, or falls back on mixed ratification. The paper argues CDT will even refuse a \$1 truly random coin that offers a 50% survival chance.

## 6. Interpretive questions the source leaves open

### (a) Does A-FDT condition on the observation?

The boxed Equation (4) does not condition on $x$. In the transparent Newcomb section, however, the displayed objective is written as $\mathbb E(V\mid\mathtt{do}(\textsc{fdt}(\ldots,\textit{full})=a,\ \textsc{Obs}=\textit{full})$, with an unbalanced parenthesis.

The arithmetic decides the matter. If we conditioned on $\textsc{Box B}=\textit{full}$ inside the $\mathtt{do}(f_F=\textit{twobox})$ hypothetical, we would condition on the predictor having erred. The value would then be \$1,001,000, and A-FDT would two-box. The paper's numbers, $990{,}000+10q$ against roughly $10{,}010+990q$, are the *unconditioned* values.

The paper also warns that the earlier timeless decision theory "prescribes both conditioning on evidence *and* changing the place where one intervenes," producing a harmful "double update." I therefore read Equation (4) literally: **the observation selects the node and is never conditioned on.** This is the reading the source's own calculations require.

### (b) Beliefs about one's other-input outputs

Equation (4) intervenes only on $f_x$. The other nodes $f_y$ keep prior probabilities, such as $q$ above. In the paper's examples the verdict is robust to $q$, and the authors note that "it doesn't matter if Fiona has some uncertainty." Nothing guarantees this robustness in general. A full specification of A-FDT therefore needs a rule for these priors.

My suggestion is to treat them as part of $P$ and to require them, ideally, to be **self-consistent**: the prior on $f_y$ should match what A-FDT actually outputs on $y$. That turns the collection $\{f_y\}$ into a fixed-point problem.

### (c) Where A-FDT and policy FDT can come apart (my example)

Footnote 16 says the policy formulation "intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy*" and that "the difference only matters in multi-agent dilemmas so far as we can tell." The fixed-point view in (b) shows one mechanism by which the two can diverge.

Consider a predictor who, at random, shows the agent signal $x$ or signal $y$. It pays \$10 if the agent's predicted policy is $(L\text{ on }x,\ L\text{ on }y)$, \$1 if it is $(R,R)$, and \$0 otherwise. Suppose the agent, at $x$, is confident that $f_y=R$.

- Intervening on $f_x$ alone, $R$ yields \$1 and $L$ yields \$0. A-FDT chooses $R$.
- Symmetric reasoning at $y$ also yields $R$.
- The pair $(R,R)$ is self-consistent, so the priors are even correct. Yet it is dominated by $(L,L)$.

Policy FDT, which maximizes over whole maps $\pi:\mathcal X\to\mathcal A$, selects $(L,L)$.

The general point is that per-input action intervention finds *equilibria* among the agent's own information sets, while policy intervention finds the *global optimum*. This is my analysis, not a claim made in the paper. It fits the footnote in one respect: the gap appears only when another party conditions on how the agent behaves across several inputs.

### (d) Counterpossibles and the construction of the graph

Every hypothetical in which $f_x$ takes a value other than its actual one is logically impossible. The paper accepts this cost. It calls the difficulty "technical rather than philosophical" and observes that CDT's hypotheticals about deterministic agents are equally impossible.

For applications, what matters is that A-FDT's verdicts are only as good as $G$. Two agents with identical $P$ but different judgments about which processes "compute the same function" will choose differently. The recipe in §4 is a heuristic, not a resolution of the open problem.

### (e) Fairness

The source does not claim that A-FDT wins everywhere. Problems that punish a specific algorithm, for example "punish anyone who acts like a copy of Fiona," defeat any theory. The claim is restricted to "fair" problems, where outcomes depend "only on the agent's behavior in the dilemma at hand." The authors admit this notion is not yet formalized.

## 7. Using A-FDT on a new case: a checklist

1. Write down the outcomes and the utility function $\mathcal U$.
2. List the possible observations and create one node $f_y$ for each. Identify the actual observation $x$.
3. For every other system in the problem, ask whether it computes or predicts $f_y$. If so, add an edge, with a noise node if the computation is imperfect. If it is merely correlated, leave it upstream.
4. Make $\textsc{Act}$ select among the $f_y$ according to which observation arises.
5. For each $a$, compute $\mathbb E[V\mid\mathtt{do}(f_x=a)]$ without conditioning on $x$. Use priors (ideally self-consistent ones) for the $f_{y\neq x}$.
6. Choose the argmax. If verdicts depend on cross-input coordination, check them against policy FDT.

## 8. Conclusion

A-FDT is CDT with the intervention moved. The agent no longer intervenes on the physical token "my act." It intervenes on the logical type "this function's output on this input." Its observation selects which such node it intervenes on, rather than being conditioned on.

This one change lets a single rule do all of the following: one-box and smoke; cooperate with a twin; pay in Parfit's desert; refuse XOR and mechanical blackmail; and stay calmly in Damascus. The decisive input is the graph $G$, which encodes which parts of the world track one's decision function. Building that graph is the theory's acknowledged open problem.

Applying the theory carefully also requires two interpretive commitments that the paper's calculations support but its notation leaves implicit. First, the agent does not condition on the observation. Second, it needs a principled account of its beliefs about its own outputs on other inputs. Where those beliefs matter, the policy-selecting variant that the authors prefer can do strictly better than A-FDT.

## References

- Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge UP.
- Pearl, J. (2000). *Causality*. Cambridge UP.
- Yudkowsky, E. & Soares, N. Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.