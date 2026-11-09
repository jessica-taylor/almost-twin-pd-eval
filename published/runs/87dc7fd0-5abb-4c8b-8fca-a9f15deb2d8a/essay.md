# A-FDT: Action Functional Decision Theory

## 1. What this essay covers

Yudkowsky and Soares (2017) introduce *functional decision theory* as a rival to causal decision theory (CDT) and evidential decision theory (EDT). Their central slogan is that the agent should treat her decision as the output of a fixed mathematical function and ask, "Which output of this very function would yield the best outcome?"

The paper gives one fully displayed formal rule, Equation (4) in Section 5. That rule maximizes over **actions** $a \in \mathcal A$. In two footnotes, however, the authors say that their "preferred formalization" instead has agents "iterate over *policies* (mappings from observations to actions) rather than actions."

To keep these apart, I use the following names:

- **A-FDT** (action functional decision theory) is the rule of Equation (4), maximizing over actions.
- **P-FDT** (policy-selecting functional decision theory) is the footnoted policy variant. I discuss it only for contrast.

When I quote the source, its own label "FDT" is kept verbatim. The paper uses that label for the theory whose formal rule is A-FDT.

Throughout, I mark which claims belong to the source and which are my own interpretations or proposals.

## 2. The common template: expected utility with a choice of hypothetical

The source frames EDT, CDT and A-FDT as three instances of one schema, drawing on Gibbard and Harper. The agent chooses an action $a$ maximizing

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}
$$

Here $x$ is the observation history, and $P(a \hookrightarrow o_j; x)$ is the probability of outcome $o_j$ "in the hypothetical scenario where the action $a$ is executed after receiving observations $x$."

Following Joyce, the authors treat the interpretation of the connective $\hookrightarrow$ as the free parameter that separates the theories. Procedurally, the agent holds a world-model $M$, builds a "hypothetical" $M^{a\hookrightarrow}$ for each action, and scores each hypothetical by expected utility. The theories differ only in how they build hypotheticals:

- **EDT** conditions: $\mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a)$ (Eq. 2).
- **CDT** intervenes on the physical act and conditions on observations: $\mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x)$ (Eq. 3).
- **A-FDT** intervenes on a *logical* variable, the output of the decision function itself.

## 3. The A-FDT rule

**Definition (A-FDT; Equation (4) of the source).** Let $P$ be a probability distribution over a set of variables, and let $G$ be a directed graph encoding "how changing a logical variable affects all other variables." Let $x$ be the agent's observation history. Then

$$
\text{A-FDT}(P,G,x) \;:=\; \operatorname*{arg\,max}_{a\in\mathcal A}\; \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big). \tag{4}
$$

The paper writes the left-hand side as $\mathrm{FDT}(P,G,x)$. The underlines denote dequoting: $\textsc{fdt}(\underline P,\underline G,\underline x)$ is the *name of a variable* in the model. That variable stands for "the output of this very algorithm on these very inputs."

Four features of Equation (4) deserve emphasis.

**(i) The intervention target is a type, not a token.** CDT sets the physical act. A-FDT sets the output of a function. Every physical system whose behaviour depends on that output responds to the intervention in the hypothetical, wherever it sits in spacetime. The authors invoke Peirce: CDT "intervenes on the token," A-FDT "on the *type*." Their summarizing analogy is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

**(ii) Observations select the node; they are not conditioned on.** Compare Eqs. (3) and (4). CDT includes "$\textsc{Obs}=x$" behind the conditioning bar. A-FDT does not. Instead, the observation determines *which* variable is intervened upon. In the source's words: "FDT responds to observation by changing which node it intervenes upon."

This is the formal root of A-FDT's characteristic "updateless" behaviour. One caution about the source text: in the transparent Newcomb section, the paper's displayed objective includes "$\textsc{Obs}=\textit{full}$" inside the $\mathtt{do}$. The arithmetic it then performs, however, explicitly sums over the branch where the box is *empty*. I therefore follow Equation (4) as stated: observations are not conditioned on.

**(iii) Self-reference is benign.** The model contains a variable naming its own algorithm's output on itself. The authors note that the agent "does not need to know the *value*" in order to have a variable representing it, and they cite Kleene's recursion theorem ("quining").

**(iv) $G$ is an input, not something A-FDT derives.** The ideal would be an operator $\mathtt{true}(\varphi)$ that updates on a counterpossible logical sentence. The authors admit "it's not clear how to define a $\mathtt{true}$ operator." They therefore require the dependency structure to be supplied, "in the same way that the relevant causal structure is given as an input to CDT."

### 3.1 The counterfactual semantics, made explicit

Here is how I read Equation (4) operationally. This is an interpretation, not a quotation.

Suppose $G$ is a structural model. It has exogenous noise variables $U$ with prior $P(U)$, and deterministic equations for every other node. The logical nodes take the form $F_y := \textsc{fdt}(\underline P,\underline G,\underline y)$, one for each observation $y$ the agent might receive. Then

$$
\mathbb E\big(V\mid \mathtt{do}(F_x=a)\big) \;=\; \sum_{u}\ \sum_{\mathbf f_{-x}} P(u)\,P(\mathbf f_{-x})\; V\big(\text{solve}(u,\ F_x=a,\ \mathbf F_{-x}=\mathbf f_{-x})\big).
$$

In words:

1. Fix the node for the actual input to $a$.
2. Leave every other function-output node $F_y$ ($y\neq x$) at its prior distribution.
3. Propagate through the equations, including the equations of predictors, twins, and the agent's own body.
4. Average the resulting utility.

The physical action $\textsc{Act}$ is typically a "switch" node: it copies whichever $F_y$ corresponds to the observation actually produced in that branch.

### 3.2 A recipe for building $G$ (my proposal)

The source says $G$ must preserve "all decision-relevant subjunctive dependencies." Its examples suggest the following construction steps, which I offer as a working procedure rather than as the authors' doctrine.

1. **Enumerate inputs.** List every observation history $y$ under which some instance of the agent's decision function is run, or is *modelled*, in the scenario. Create a node $F_y$ for each.
2. **Wire computations.** Draw an edge $F_y \to Z$ whenever $Z$ is computed by running, simulating, or reliably predicting the agent's function on input $y$. This covers predictors, twins, copies, and future selves facing the same input. Represent prediction error as a separate noise node, like the source's $\textsc{Accurate}$.
3. **Wire the body.** Make $\textsc{Act}$ depend on all $F_y$, together with whatever upstream variables determine which observation obtains.
4. **Keep ordinary causal structure.** Everything else enters as in a causal model. In particular, merely statistical correlates such as lesions or genes get no edge from any $F_y$.

The test the authors propose for drawing an edge is computational. Does $Z$ vary because something evaluates (a representation of) this function? Or does it merely correlate with the agent's act through a common cause? A predictor qualifies; a carcinogenic lesion does not.

## 4. Worked examples

All payoffs below are in the source's dollar-utility units.

### 4.1 Newcomb's problem

The predictor is 99% accurate. In the graph, $F$ points to both $\textsc{Act}$ and $\textsc{Prediction}$, with $\textsc{Accurate}$ as noise.

| Intervention | Probability box B is full | Expected utility |
|---|---|---|
| $\mathtt{do}(F=\textit{onebox})$ | 0.99 | $0.99\cdot 10^6 = 990{,}000$ |
| $\mathtt{do}(F=\textit{twobox})$ | 0.01 | $0.01\cdot 1{,}001{,}000+0.99\cdot 1{,}000 = 11{,}000$ |

A-FDT one-boxes. CDT's graph instead has $\textsc{Predisposition}$ as a common cause and intervenes on $\textsc{Act}$. That cuts the act off from the prediction, so for every probability $p$ that the box is full, two-boxing gains 1,000. CDT two-boxes.

The source stresses that no retrocausation is assumed. The agent "just thinks it is foolish to imagine her action changing without also imagining" the function's output changing.

### 4.2 The smoking lesion

Here the lesion causes both a taste for smoking and cancer. The source's careful treatment introduces two possible utility functions, one per lesion state, and hence two function nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ and $\textsc{fdt}(\underline{P_R},\underline G)$. $\textsc{Act}$ is a switch on $\textsc{Lesion}$.

Neither function node has an edge to $\textsc{Cancer}$. So $P(\textit{lesion}\mid\mathtt{do}(\cdot))=p$ is unchanged by the intervention. Smoking beats refraining by $p\cdot 1{,}000$, which is the probability that this node is the one controlling the act, times the value of smoking. A-FDT smokes.

This case shows the distinctive structure of A-FDT. It agrees with EDT in Newcomb and with CDT in the lesion case, and the difference comes entirely from $G$, not from the maximization rule.

### 4.3 The transparent Newcomb problem

Both boxes are visible. Box B was filled iff the predictor predicted one-boxing *upon seeing a full box*. The agent sees B full, so she intervenes on $F_{\text{full}}$. Let $q$ be her prior that $F_{\text{empty}}=\textit{twobox}$.

**Case $\mathtt{do}(F_{\text{full}}=\textit{onebox})$:**
- With probability 0.99 the prediction is correct, B is full, and she one-boxes: $10^6$.
- With probability 0.01 the prediction is wrong, B is empty, and $F_{\text{empty}}$ controls the act: $q\cdot 1{,}000$.
- Total: $990{,}000 + 10q$.

**Case $\mathtt{do}(F_{\text{full}}=\textit{twobox})$:**
- With probability 0.99 the prediction is correct, B is empty, and $F_{\text{empty}}$ controls: $q\cdot 1{,}000$.
- With probability 0.01 the prediction is wrong, B is full, and she two-boxes: $1{,}001{,}000$.
- Total: $10{,}010 + 990q$.

(The paper prints the constant as "\$110,00"; the arithmetic gives \$10,010.)

For any $q\in[0,1]$, one-boxing wins, even though she is *looking at* a full box. Point (ii) above is what makes this possible. In her two-boxing hypothetical, she mostly never sees a full box at all.

The source argues that this is the same structure as paying in Parfit's hitchhiker. It defends the verdict by three arguments:

- **Precommitment.** CDT and EDT agents would precommit to one-box.
- **Value of information.** FDT agents "do not assign negative expected value to information."
- **Utility.** One-boxers actually see full boxes.

### 4.4 Mechanical blackmail: a threshold formula

A blackmailer runs a damaging program (cost $10^6$) only if she predicts the agent will pay $10^3$ upon receiving the letter. Let $\varepsilon$ be the probability that she *wrongly* predicts payment from a refuser. On receiving the letter, A-FDT compares two interventions on $F_{\text{blackmail}}$:

$$
\mathbb E(V\mid \mathtt{do}(F=\textit{pay})) \approx -10^3,
\qquad
\mathbb E(V\mid \mathtt{do}(F=\textit{refuse})) = -\varepsilon\cdot 10^6 .
$$

So A-FDT refuses iff $\varepsilon < 10^{-3}$. This matches the source's example: at $\varepsilon=0.0009$, the agent "loses \$900 in expectation" by refusing and so refuses.

The paper then says the agent pays at an error rate of "0.011%." That figure lies *below* the threshold, so the formula says she would refuse. I take the intended figure to be one above $0.1\%$, such as 0.11%.

The source's general point holds either way. The agent may refuse "even though she *knows* that the blackmailer predicted wrongly," because the rule scores the function's output across all the situations it governs.

### 4.5 Twins and Death in Damascus

**Twin prisoner's dilemma.** Both twins' acts are children of the same node $F$. So $\mathtt{do}(F=\textit{cooperate})$ yields $10^6$, while $\mathtt{do}(F=\textit{defect})$ yields $10^3$. A-FDT cooperates.

**Death in Damascus.** Death's appointment book is a child of $F$. Under either intervention Death meets the agent, so only the \$1,000 travel cost differs. A-FDT stays in Damascus without the instability that drives CDT into ratification procedures.

## 5. When A-FDT agrees with CDT and EDT

The source states an agreement condition. Suppose every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, except for $\textsc{Act}$'s own dependence on the function node. Then

$$
\mathbb E[V\mid a] = \mathbb E[V\mid \mathtt{do}(a)] = \mathbb E[V\mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G)=a)],
$$

and all three theories coincide. Divergence therefore requires something in the world that correlates with the act *without* being caused by it, typically another process computing or predicting the agent's function.

This gives a practical triage. In an unfamiliar case, first ask whether anything other than the agent's own body depends on the agent's decision function. If nothing does, apply ordinary causal reasoning.

The source also rejects CDT's dominance argument as non-neutral: "every method for constructing hypotheticals gives rise to its own notion of dominance." Under A-FDT's notion, holding subjunctive dependencies fixed, A-FDT never chooses a dominated action.

## 6. Open questions and operational choices

### 6.1 Where does $G$ come from?

This is the gap the source itself flags as most important: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

The difficulty is that Equation (4) is fully determinate only once $G$ is fixed. The theory's verdicts are therefore only as good as the agent's dependency model.

### 6.2 Partial similarity (my proposal)

The paper treats perfect twins and noisy predictors. It does not say what to do about an opponent who runs a *similar but not identical* algorithm. A reasonable operational extension is a mixture model: add a latent node $S\in\{\textit{same},\textit{different}\}$ with $P(S=\textit{same})=\rho$, and set

$$
\textsc{OtherAct} =
\begin{cases}
F_x & \text{if } S=\textit{same},\\
\text{independent draw from } Q & \text{otherwise.}
\end{cases}
$$

In the twin prisoner's dilemma, take $Q$ to cooperate with probability $c$. Then

$$
\mathbb E[V\mid \mathtt{do}(F=C)] = \rho\cdot 10^6 + (1-\rho)\,c\cdot 10^6,
$$

$$
\mathbb E[V\mid \mathtt{do}(F=D)] = \rho\cdot 10^3 + (1-\rho)\big(c\cdot 1{,}001{,}000 + (1-c)\cdot 10^3\big).
$$

The difference simplifies to

$$
\mathbb E[V\mid \mathtt{do}(F=C)] - \mathbb E[V\mid \mathtt{do}(F=D)] = 999{,}000\,\rho - 1{,}000\,(1-\rho).
$$

So A-FDT cooperates iff $\rho > 1/1000$. The source's "noisy predictor" node $\textsc{Accurate}$ is a special case of this device. This extension is mine; the paper does not discuss graded similarity.

### 6.3 Priors on the other function nodes

Equation (4) leaves the nodes $F_y$ ($y\neq x$) at their prior. The source handles these with an arbitrary $q$. It notes that the "correct" value can be verified, and that in its examples the verdict does not depend on $q$.

In general it can depend on $q$. My operational suggestion is to require self-consistency. Each $F_y$ should be assigned the value that A-FDT itself outputs on input $y$, which makes the profile $(F_y)_y$ a fixed point of the rule.

### 6.4 A-FDT versus P-FDT

The fixed-point requirement exposes the main structural difference between A-FDT and P-FDT. Consider an example of my own construction.

Two copies of the agent are run, one shown observation $L$ and one shown $R$. Each chooses $1$ or $2$. Payoffs are:

- both choose 1: 10;
- both choose 2: 5;
- mismatch: 0.

Under input $L$, A-FDT intervenes on $F_L$ and holds $F_R$ at its prior, with $r=P(F_R=1)$. That gives

$$
\mathbb E[V\mid\mathtt{do}(F_L=1)] = 10r,\qquad \mathbb E[V\mid\mathtt{do}(F_L=2)] = 5(1-r).
$$

So A-FDT chooses 1 iff $r>1/3$. Both $(1,1)$ and $(2,2)$ are self-consistent fixed points. An agent whose prior is pessimistic about its own other-input behaviour can settle on the inferior one.

P-FDT instead optimizes the whole map $\pi:\{L,R\}\to\{1,2\}$ in one step and selects $\pi\equiv 1$. This is a plausible illustration of the authors' remark that the policy formulation "makes a difference in certain multi-agent dilemmas." It is not one they give.

When applying A-FDT to unfamiliar cases, then, the safe statement is this. A-FDT's verdict is determined by $G$, $P$, the observation, *and* the agent's beliefs about her own outputs on other inputs. Where those beliefs matter, the analyst must say how they are fixed.

### 6.5 Counterpossibles and fairness

Intervening on $F_x$ asks what would happen if a mathematical function had an output it in fact lacks. The paper argues the difficulty is "technical rather than philosophical," pointing to mathematicians' ability to reason under logical uncertainty. It also replies that CDT faces a parallel puzzle about "control" in deterministic worlds.

Finally, the source's claim of superiority is restricted to "fair" problems, those where "the outcome depends only on the agent's behavior in the dilemma at hand." It concedes that a formal definition of fairness is still lacking.

## 7. A procedure for unfamiliar cases

Collecting the above, here is how to apply A-FDT to a new problem.

1. **Model the world.** Specify variables, utilities, and a causal skeleton.
2. **Locate the function.** Identify every place where the agent's decision function, on some input, is run or modelled. Create the nodes $F_y$ and connect them as in §3.2.
3. **Fix the input.** Identify the actual observation $x$ and the corresponding node $F_x$.
4. **Evaluate.** For each $a\in\mathcal A$, compute $\mathbb E(V\mid\mathtt{do}(F_x=a))$. Do not condition on $x$. Leave the other $F_y$ at self-consistent values.
5. **Choose.** Output the maximizer. If the answer depends on the other $F_y$, report that dependence explicitly.

## 8. Conclusion

A-FDT, the rule of Equation (4), is expected-utility maximization in which the hypothetical for each option is a Pearl-style intervention on the *output of the agent's own decision function*, rather than on her physical act. Two choices give the theory its shape:

- It *intervenes on a type*, so predictors and twins move with the agent's choice while lesions do not.
- It *responds to observations by selecting the node* rather than by conditioning on them, which produces its characteristic refusal to be blackmailed and its one-boxing in front of a full box.

The source claims, with worked examples, that this single rule matches the best of CDT and EDT and beats both in problems like Parfit's hitchhiker. What the source does not supply is a method for constructing the dependency graph on which everything rests. I have proposed a construction recipe, a mixture model for partial similarity, and a self-consistency condition for the agent's other-input behaviour. I have also argued that this last condition marks where A-FDT can diverge from its policy-selecting cousin, P-FDT.

## References

- Gibbard, A. & Harper, W. (1978). Counterfactuals and two kinds of expected utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Pearl, J. (2000). *Causality*. Cambridge University Press.
- Yudkowsky, E. & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.