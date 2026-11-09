# A-FDT: Action Functional Decision Theory

*An essay on the decision rule in Equation (4) of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality"*

## 1. The question A-FDT asks

Consider an agent and her psychological twin who each choose, in separate rooms, whether to cooperate or defect in a prisoner's dilemma. If both cooperate, each gets \$1,000,000. If both defect, each gets \$1,000. A lone defector gets \$1,001,000.

- **Causal decision theory (CDT)** notes that her choice cannot cause the twin's choice. Since defection dominates, she defects.
- **Evidential decision theory (EDT)** notes that cooperating would be good news about the twin, so she cooperates.

The theory examined here gives a third answer, for a third reason. The twin is running the same reasoning, so the real question is what that reasoning should output. In the source's words, the agent asks "Which output of this decision procedure causes the best outcome?" If the procedure outputs *cooperate*, both cooperate. If it outputs *defect*, both defect. So it outputs *cooperate*.

The source paper calls its theory *functional decision theory* (FDT). Its main formal statement is Equation (4) of Section 5. In that equation the agent intervenes on a variable whose value is an **action**. Two footnotes (7 and 16) say the authors actually prefer a variant that chooses **policies**. I write **A-FDT** for the action-valued rule of Equation (4), and **policy-FDT** for the policy variant, which is my own label. Quotations keep the source's wording, which says "FDT".

## 2. The common skeleton

The paper presents EDT, CDT, and A-FDT as expected-utility theories that differ only in how they build hypotheticals. Following Gibbard and Harper, an agent executes an action $a$ maximizing

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j), \tag{1}
$$

where $x$ is the observation history and $a\hookrightarrow o_j$ is the "decision hypothetical": outcome $o_j$ obtains if $a$ is done after observing $x$. Joyce's representation theorem leaves the interpretation of $\hookrightarrow$ open. The three theories fill it in differently. Writing $V=\mathcal U(\textsc{Outcome})$:

$$
\mathrm{EDT}(P,x) = \arg\max_a \mathbb E\big(V \mid \textsc{Obs}=x, \textsc{Act}=a\big), \tag{2}
$$

$$
\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E\big(V \mid \mathrm{do}(\textsc{Act}=a), \textsc{Obs}=x\big). \tag{3}
$$

In (3), $G$ is a causal graph over the variables of $P$. Pearl's $\mathrm{do}$ operator sets $\textsc{Act}=a$, recomputes everything downstream, and leaves everything else (including upstream correlates) untouched.

The paper treats the per-action hypothetical $M^{a\hookrightarrow}$ as "a decision-theoretic instrument constructed from beliefs", like notes on scratch paper. It is not a belief about a mind-independent possible world. I return to why this matters in §7.

## 3. The definition of A-FDT

Equation (4) of the source is, under my label:

$$
\boxed{\;\mathrm{A\text{-}FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathrm{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).\;} \tag{4}
$$

The ingredients are as follows.

1. **$P$** is a probability distribution containing ordinary physical variables (box contents, actions, predictions). It also contains variables representing the outputs of mathematical functions. The paper's example is a variable for the value of $6288+1048$, which "(hopefully) has most of its probability on 7336."

2. **$\textsc{fdt}(\underline P,\underline G,\underline x)$** is one such logical variable. It stands for "the output of this decision procedure, run on model $(P,G)$ and observation $x$."
   - Underlining means dequoting: the variable's *name* is built from the agent's own model.
   - The paper calls this self-reference harmless. The agent needs a variable that *represents* her output, not knowledge of its *value*, and Kleene's recursion theorem ("quining") shows such self-representing structures can be built.
   - I abbreviate $\textsc{fdt}(\underline P,\underline G,\underline y)$ as $F_y$.

3. **$G$** is a graph of *subjunctive* dependence, not only causal dependence. Its edges say how changing a logical variable changes other variables. It is the extra input A-FDT needs, just as CDT needs a causal graph. The paper would prefer a $\mathtt{true}(\phi)$ operator that updates $P$ on a counterpossible logical sentence. Since no satisfactory one is known, it reuses Pearl's $\mathrm{do}$ on this broader graph.

4. **The observation $x$ is not conditioned on.** This is the most important formal feature. In the authors' words: "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." Observing $x$ tells the agent *which* logical variable, $F_x$, is under her control. The hypothetical created by $\mathrm{do}(F_x=a)$ may put substantial weight on worlds in which $x$ is never observed.

A-FDT therefore differs from CDT on two counts: where it intervenes (the decision function's output rather than the bodily act), and how it uses observations (to select the node rather than to update).

**When the three theories agree.** Suppose every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from $\textsc{Act}$'s dependence on $F$ itself. Then

$$
\mathbb E[V\mid a]=\mathbb E[V\mid \mathrm{do}(a)]=\mathbb E[V\mid \mathrm{do}(F=a)],
$$

and the three theories recommend the same action. They come apart only when something other than the act's effects correlates with the act. The typical case is a predictor, twin, or copy that models the agent's decision function.

## 4. Subjunctive dependence: what goes into $G$

The source's key notion is this: "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." Its slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

Three reference cases fix what belongs in $G$.

- **Common computation.** Two working calculators computing $6288+1048$, even on opposite sides of the universe, both depend on the arithmetical fact. If the fact were different, both outputs would be different. A twin running the agent's reasoning, or a predictor holding an accurate model of it, is a child of $F$ in $G$.
- **Causal dependence as a special case.** A scribe copying a calculator's output depends both causally and subjunctively on it. Ordinary causal descendants of the agent's act remain descendants in $G$.
- **Mere correlation.** Two calculators that happen to both be pink do not depend on each other. Repainting one leaves the other pink. A lesion that correlates with smoking without modelling the agent's reasoning is *not* a child of $F$.

Imperfect predictors are handled with an exogenous noise variable. The prediction equals $F$ when $\textsc{Accurate}=$ *accurate*, and differs from it otherwise. The dependence is weakened but not removed.

## 5. Worked examples

The paper's examples use simple models that are accurate about the problem. Each computation below follows Equation (4).

### 5.1 Newcomb's problem

Box A holds \$1,000. Box B holds \$1,000,000 iff the predictor (99% accurate) predicted one-boxing. In $G$, $F$ is a parent of both $\textsc{Act}$ and $\textsc{Prediction}$, and $\textsc{Accurate}$ is a parent of $\textsc{Prediction}$.

$$
\mathbb E[V\mid\mathrm{do}(F=\textit{onebox})] = 0.99(1{,}000{,}000)=990{,}000,
$$
$$
\mathbb E[V\mid\mathrm{do}(F=\textit{twobox})] = 0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000.
$$

A-FDT one-boxes. CDT's graph cuts $\textsc{Act}$ off from $\textsc{Prediction}$, so for any fixed probability $p$ that the box is full, two-boxing adds exactly \$1,000. CDT two-boxes.

Nothing here invokes backward causation. The agent simply refuses to imagine her decision function's output changing while an accurate model of that same function stays fixed.

### 5.2 The smoking lesion

A lesion causes both a love of smoking and cancer. Smoking itself is harmless and worth \$1,000.

The paper models the lesion as fixing which utility function, $\mathcal U_S$ or $\mathcal U_R$, the agent has. It therefore fixes which of two decision-function nodes controls the act. Let $p$ be the probability of the lesion and $q$ the probability that the other node outputs *smoke*. Intervening on the node for her (unknown) actual model, the agent finds:

- smoking is worth $p(10{,}000+1{,}000)+(1-p)(990{,}000+1{,}000q)$;
- refraining is worth $p(10{,}000)+(1-p)(990{,}000+1{,}000q)$.

Smoking is strictly better by $p\cdot 1{,}000$, and the value of $q$ does not affect the comparison. Cancer is not a child of any $F$ node, so the intervention cannot touch it.

A-FDT thus one-boxes *and* smokes. Gibbard and Harper argued that no rational agent can consistently do both. The paper's own verdict on the lesion problem is that it is "badly confused" and should be abandoned, partly because a correctly specified EDT agent's correlations would be inaccurate.

### 5.3 Transparent Newcomb: observations select the node

Both boxes are transparent. The predictor fills B iff she predicts the agent would one-box *upon seeing B full*. The agent sees B full, so she intervenes on $F_{\text{full}}$.

In $G$, $F_{\text{full}}$ drives the prediction (subject to noise). The prediction determines what the agent sees, and thus which of $F_{\text{full}}$ or $F_{\text{empty}}$ controls $\textsc{Act}$. Let $q$ be the prior that $F_{\text{empty}}=\textit{twobox}$.

| intervention | accurate (0.99) | inaccurate (0.01) | expectation |
|---|---|---|---|
| $F_{\text{full}}=\textit{onebox}$ | full, one-box: 1,000,000 | empty, $F_{\text{empty}}$ acts: $1{,}000q$ | $990{,}000+10q$ |
| $F_{\text{full}}=\textit{twobox}$ | empty, $F_{\text{empty}}$ acts: $1{,}000q$ | full, two-box: 1,001,000 | $10{,}010+990q$ |

A-FDT one-boxes while looking at a full box. When it imagines two-boxing, it imagines a world in which it probably saw an empty box.

Two textual remarks:

- The printed figure for the second row is "\$110,00 + $q\cdot$\$990", evidently a typo for \$10,010 + $q\cdot$\$990.
- The displayed objective in this section is typeset with "$\textsc{Obs}=\textit{full}$" inside the conditioning bar, with an unbalanced parenthesis. But the paper's own calculation sums over the branch where the box is *empty*, so it does not condition on the observation. Only the unconditioned reading matches Equation (4), and I adopt it.

Parfit's hitchhiker has the same structure. Paying in the city corresponds to $F_{\text{city}}=\textit{pay}$, which (via the driver's lie detection) makes reaching the city likely.

### 5.4 Blackmail

**Mechanical blackmail.** The blackmailer runs a damaging program (costing the agent \$1,000,000) only if she predicts the agent would pay \$1,000 to stop it. Suppose she wrongly predicts payment with probability $\varepsilon$.

- $\mathrm{do}(F_{\text{blackmail}}=\textit{pay})$: blackmail is certain and the agent loses \$1,000.
- $\mathrm{do}(F_{\text{blackmail}}=\textit{refuse})$: blackmail occurs with probability $\varepsilon$, costing $10^6\varepsilon$ in expectation.

A-FDT refuses iff $\varepsilon<10^{-3}$. This fits the paper's $\varepsilon=0.09\%$ example, where the agent refuses "even though she knows that the blackmailer predicted wrongly." The paper says she pays at an error rate of "0.011%". That conflicts with its own arithmetic, under which the threshold is 0.1%, so it is presumably a typo for 0.11%.

**XOR blackmail.** A predictor sends a letter iff exactly one holds: (i) no termites and the agent will pay \$1,000; (ii) termites and she will not pay. Let $p$ be the probability of termites, which cost \$1,000,000.

- $\mathrm{do}(F_{\text{letter}}=\textit{pay})$ gives $-10^6 p - 1{,}000(1-p)$.
- $\mathrm{do}(F_{\text{letter}}=\textit{refuse})$ gives $-10^6 p$.

A-FDT refuses, because the termites are not a child of $F$. CDT also refuses, but with the strange counterfactual that, had it paid, an infallible predictor would have erred. EDT pays.

### 5.5 Death in Damascus

Death predicts perfectly and waits wherever the agent will be. Fleeing costs \$1,000.

Death's appointment book is a child of $F$. Under $\mathrm{do}(F=\textit{stay})$ the agent dies in Damascus (value 0). Under $\mathrm{do}(F=\textit{flee})$ she dies in Aleppo ($-1{,}000$). A-FDT stays, calmly.

CDT instead oscillates. Whatever it expects to do, it judges the other city safer. The paper argues that once it settles, it will even refuse a truly random coin offering a 50% chance of survival for \$1. Its hypotheticals make it behave as though its chance of survival is at least 50% already, even though its beliefs know otherwise.

## 6. Applying A-FDT to unfamiliar cases

The source specifies Equation (4) *given* $(P,G)$. It explicitly does not say how to obtain $G$: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

What follows is my own operational recipe, distilled from the paper's examples. Each step is labelled by its basis.

**Step 1: Identify the controlled node** *(from the source).* Fix the actual observation history $x$. The decision variable is $F_x$, not the bodily act.

**Step 2: Enumerate the implementations of the decision function** *(my systematization of the paper's figures).* For each relevant input $y$, list every system whose behaviour is a function of $F_y$:
- the agent's own body when she observes $y$;
- predictors, simulators, and the driver's lie detector;
- twins and copies;
- the agent's future selves facing relevantly identical choices (the paper's gym example).

Draw an edge from $F_y$ to each. Model imperfect fidelity with an independent noise parent, as $\textsc{Accurate}$ does in Newcomb.

**Step 3: Exclude mere correlates** *(from the source).* Common causes that do not compute or model the function, such as lesions or genes, are not children of any $F_y$. They remain upstream variables with their ordinary prior.

**Step 4: Route the observation channel** *(from the source).* If what the agent observes depends on a prediction, the observation must appear as a variable that determines which $F_y$ controls $\textsc{Act}$. Do **not** condition on $\textsc{Obs}=x$.

**Step 5: Set priors on the non-intervened decision nodes** *(partly open).* In every example the paper gives, the choice of prior on the other nodes ($q$ in §5.2–5.3) does not affect the verdict. In general it could.

My proposal is to require self-consistency: set each $F_y$ ($y\neq x$) to the action A-FDT itself would choose at $y$, iterating to a fixed point if necessary. The paper's remark that "the correct $q$" is $0$ in the lesion case and $1$ in transparent Newcomb is consistent with this.

**Step 6: Compute and maximize** *(from the source).* For each $a$, evaluate $\mathbb E[V\mid \mathrm{do}(F_x=a)]$ and take the argmax.

The source does not discuss tie-breaking. Any fixed rule seems acceptable, provided predictors are modelled as knowing it.

**Partial similarity** is the hardest residual question. Suppose the "twin" runs a slightly different algorithm. The paper's calculator analogy suggests treating the other system as a noisy copy, a child of $F$ with match probability $\rho$. Estimating $\rho$ is exactly the unsolved problem of discovering subjunctive structure. The noise-node treatment is my extrapolation, not a source claim.

**Which $P$?** Equation (4) evaluates hypotheticals with the agent's model $P$, and the examples treat $P$ as not updated on $x$. The source does not say *when* $P$ is fixed relative to the agents who modelled her.

A reasonable reading is that $P$ must still contain, as live variables, the observations that the relevant predictors' models make depend on $F$. If $P$ had already been updated on "box B is full," the transparent Newcomb calculation would collapse into CDT's. The paper flags a related failure of its predecessor, Timeless Decision Theory, which both conditions on evidence and changes the intervention point. It calls this a "double update."

## 7. A-FDT versus policy-FDT

Footnote 7 says: "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

Policy-FDT would intervene jointly on the whole map $y\mapsto F_y$. A-FDT intervenes on one coordinate $F_x$ and holds the others at their prior.

The paper does not say exactly when the two diverge. A plausible case (my analysis) is coordination between copies that receive different inputs. Suppose two instances of the same function see $y_1$ and $y_2$ and are rewarded for matching. Single-coordinate optimization can then lock in a self-consistent but inferior pair of outputs. Each coordinate is best given the other, but a joint switch would be better for both.

With a sensible prior, coordinate-wise optimization can be expected to recover the policy optimum whenever the problem has a single relevant observation node, which covers every example in the paper. Readers applying A-FDT to multi-input coordination problems should treat this as a known gap.

## 8. Counterpossibles and philosophical motivation

$F_x$ is a logical fact. If the procedure in fact outputs *onebox*, then "$F_x=\textit{twobox}$" is necessarily false, so A-FDT's hypotheticals are counterpossible. The paper concedes this is "the main drawback of FDT relative to CDT at this time."

Its replies:

- Humans already reason fluently about, for example, what would follow if the twin prime conjecture were false.
- A-FDT needs only narrow counterpossibles of the form "how would this predictor's model behave if my algorithm output differently?"
- Supplying $G$ as an input sidesteps the general problem in the same way CDT takes a causal graph as given.
- CDT is no better off. A deterministic agent also has only one possible action token, so "any principled objection to the idea that FDT agents can 'control' their decision type will also imply that (deterministic) CDT agents cannot 'control' their decision token."

The paper's normative case is primarily **utility achieved**. It also offers two supporting arguments:

- **Precommitment.** CDT and EDT agents would pay to bind themselves to one-box, to pay the driver, or to refuse blackmail. A-FDT behaves as though it had already done so.
- **Reflective stability.** A-FDT does not want to self-modify away from itself in fair problems, whereas CDT recommends replacing itself for future dilemmas.

**Dominance** is reinterpreted rather than abandoned. Every method of building hypotheticals induces its own dominance notion. Under the A-FDT notion (vary the function's output while holding subjunctive dependencies fixed), A-FDT never takes a dominated action.

**Fairness.** Any theory can be punished by a problem that rewards a named decision procedure. The paper restricts its superiority claim to "fair" problems, in which "the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the dilemma at hand." Newcomb qualifies: "Newcomb's predictor doesn't punish rational agents; she punishes *two-boxers*."

The paper admits that fairness has not been formalized. A predictor who punishes whoever matches a copy of an A-FDT agent beats A-FDT, and it is unclear how to transpose such a problem fairly across theories. So the claim "A-FDT is optimal on fair problems" remains a conjecture, supported by the authors' failure to find a counterexample.

## 9. Conclusion

A-FDT is CDT with two modifications.

1. It intervenes on the logical variable $\textsc{fdt}(\underline P,\underline G,\underline x)$ representing the output of the agent's decision function, using a graph that tracks subjunctive as well as causal dependence.
2. It uses observations to choose which such variable to intervene on, not to condition on.

Its hypotheticals keep correlations that run through the decision function: twins, predictors, lie detectors, Death's appointment book. They break correlations that run through mere common causes such as lesions. The result one-boxes, smokes, pays the driver, refuses blackmail, and stays in Damascus.

Applying A-FDT to a new case comes down to building $G$:

- find every system that computes or models the agent's function on each input;
- make each a (possibly noisy) child of the corresponding $F_y$;
- route predicted observations through the graph instead of conditioning on them.

How to learn such a graph, how to handle imperfectly similar algorithms, how to fix priors on the non-intervened nodes, and how A-FDT relates to policy-FDT in coordination problems are the open questions on which a complete theory depends. The paper is explicit about the first. The others are, I have argued, the natural next ones.

### References

- Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*.
- Pearl, J. (2000). *Causality*.
- Yudkowsky, E. & Soares, N. Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.