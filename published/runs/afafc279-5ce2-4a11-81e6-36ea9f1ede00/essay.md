# Action Functional Decision Theory (A-FDT): Choosing by Intervening on One's Own Decision Function

## 1. The question A-FDT asks

Every expected-utility theory has to say what the agent should imagine when she considers doing something other than what she will in fact do. Yudkowsky and Soares, following Joyce, treat this as the real point of disagreement among decision theories. All of them maximize

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),
$$

where $a \hookrightarrow o_j$ is the "decision hypothetical" in which action $a$ is taken after observation history $x$. They differ only in how they interpret the connective $\hookrightarrow$. Two standard interpretations are familiar:

- **Evidential decision theory (EDT)** conditions: $\mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a)$.
- **Causal decision theory (CDT)** intervenes on the physical act: $\mathbb E(V \mid do(\textsc{Act}=a), \textsc{Obs}=x)$.

The theory discussed here takes a third route. The source paper calls it simply *functional decision theory*. In this essay I call the specific action-level rule of its Equation (4) **A-FDT**, for *action functional decision theory*. The name separates it from a policy-level variant that the authors mention in footnotes and that I take up in §5. In the paper's words, the agent should treat her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'"

The guiding analogy, again quoted from the source, is:

> *Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*

Two physical systems that compute the same function, such as two calculators adding $6288+1048$, or an agent and a predictor's accurate model of her, both *subjunctively depend* on that function. If the function's output were different, both outputs would differ. A merely statistical correlate, such as a lesion that causes both a taste for smoking and cancer, does not. A-FDT holds that the agent's hypotheticals should vary exactly the things that subjunctively depend on her decision function and hold everything else fixed. The source puts this in type/token terms: CDT intervenes on the token "my action is $a$," whereas this theory "intervenes on the *type*."

## 2. The formal rule

### 2.1 The equation

The paper's Equation (4), which I take as the definition of A-FDT, is

$$
\boxed{\;\text{A-FDT}(P, G, x) := \operatorname*{argmax}_{a\in\mathcal A}\; \mathbb E\!\left(V \;\middle|\; do\big(\textsc{fdt}(\underline P, \underline G, \underline x) = a\big)\right)\;}
$$

The ingredients are as follows.

- **$P$** is a probability distribution over variables. These include ordinary physical variables (box contents, predictions, outcomes) and *logical* variables representing the outputs of mathematical functions.
- **$G$** is a directed graph that records how changing a logical variable propagates to other variables. In CDT the graph encodes causal structure only. In A-FDT it encodes "logical, mathematical, computational, causal, etc." structure.
- **$\textsc{fdt}(\underline P, \underline G, \underline x)$** is the node representing *what this very algorithm outputs on input $(P, G, x)$*. The underlines denote dequoting: the node's name is built from the agent's own model and observations. The source notes that this self-reference is harmless, since one need not know a value in order to have a variable that represents it. Kleene's recursion theorem ("quining") shows that such self-representing structures exist.
- **$do(\cdot)$** is Pearl's intervention operator. It sets the node, severs its incoming edges, and recomputes everything downstream in $G$.
- **$V = \mathcal U(\textsc{Outcome})$** is utility, and $\mathcal A$ is a finite set of actions.

The source motivates this rule as a stand-in for an idealized $\texttt{true}$ operator that would update $P$ on the counterpossible sentence "$\textsc{fdt}(\underline P,\underline x)=a$." We do not know how to define such an operator. A-FDT therefore requires the dependency structure as an *input*, exactly as CDT requires a causal graph.

### 2.2 Two differences from CDT

The paper itself identifies two differences between Equation (4) and the CDT rule (its Equation 3).

1. **The point of intervention.** CDT intervenes on $\textsc{Act}$, a physical fact. A-FDT intervenes on $\textsc{fdt}(\ldots)$, a logical fact. Every node that is a child of that logical fact moves with it, including predictors and twins.
2. **The role of observations.** CDT conditions on $\textsc{Obs}=x$. A-FDT does not condition at all. An observation changes *which node* is intervened on: from $\textsc{fdt}(\underline P,\underline G,\underline x)$ to $\textsc{fdt}(\underline P,\underline G,\underline y)$. Its hypotheticals can therefore include worlds in which the agent would have observed something else.

### 2.3 When the three theories agree

The source notes that if every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$ (apart from $\textsc{Act}$'s own dependence on the $\textsc{fdt}$ node), then

$$
\mathbb E[V\mid a] = \mathbb E[V \mid do(a)] = \mathbb E[V \mid do(\textsc{fdt}(\underline P,\underline G)=a)].
$$

In such problems EDT, CDT and A-FDT recommend the same act. They come apart only when something other than the act itself tracks the agent's decision. Predictors, twins, and copies of oneself at other times are the standard cases.

## 3. A recipe for applying A-FDT

The source presents the rule through worked models rather than an algorithm. The following steps are my distillation of how it is applied in Section 6 of the paper.

1. **Model the world.** Write down variables for the physical situation, together with noise variables such as a predictor's accuracy.
2. **Introduce decision-function nodes.** For each input $x'$ on which the agent's decision procedure could be run in the scenario (each possible observation, or each possible utility function the agent might have), add a node $\textsc{fdt}(\underline P,\underline G,\underline{x'})$.
3. **Wire the dependencies.**
   - $\textsc{Act}$ is a function of whichever $\textsc{fdt}$ node is actually "in control." Which one that is may itself depend on world variables, for example on what the agent sees.
   - Any system that computes or accurately predicts the decision function on input $x'$ becomes a child of $\textsc{fdt}(\ldots,\underline{x'})$.
   - Merely correlated factors are not wired to these nodes.
4. **Place priors** on root nodes, including any $\textsc{fdt}$ nodes that will *not* be intervened on.
5. **Intervene and evaluate.** For the node indexed by the actual observation $x$, compute $\mathbb E(V\mid do(\textsc{fdt}(\ldots,\underline x)=a))$ for each $a\in\mathcal A$. Do not condition on $x$.
6. **Act.** Choose the maximizer.

## 4. Worked examples

All dollar figures stand for utility, as in the source.

### 4.1 Newcomb's problem

The predictor is 99% accurate, box A holds \$1,000, and box B holds \$1,000,000 iff one-boxing was predicted. In the A-FDT graph, $\textsc{fdt}(\underline P,\underline G)$ is a parent of both $\textsc{Act}$ and $\textsc{Prediction}$, and $\textsc{Accurate}$ is an independent parent of $\textsc{Prediction}$.

$$
\begin{aligned}
\mathbb E[V\mid do(\textsc{fdt}=\textit{onebox})] &= 0.99(1{,}000{,}000) + 0.01(0) = 990{,}000,\\
\mathbb E[V\mid do(\textsc{fdt}=\textit{twobox})] &= 0.01(1{,}001{,}000) + 0.99(1{,}000) = 11{,}000.
\end{aligned}
$$

A-FDT one-boxes. CDT, whose surgery on $\textsc{Act}$ leaves $P(\textit{full})=p$ unchanged, finds two-boxing better by exactly \$1,000 for every $p$, and so two-boxes. In the source's phrasing, the A-FDT agent "does not think that a physical signal passes between her action and the predictor's prediction." She simply declines to imagine the output of her own function differing from a competent prediction of that same output.

The **twin prisoner's dilemma** has the same structure. Intervening on the shared function sets both players' moves. The comparison is \$1,000,000 (cooperate) against \$1,000 (defect), so A-FDT cooperates.

### 4.2 The smoking lesion

Here the graph differs, and that difference does all the work. The lesion is modeled as fixing which utility function the agent has, $\mathcal U_S$ (likes smoking) or $\mathcal U_R$. That in turn fixes which of two decision-function nodes controls $\textsc{Act}$:

$$
\textsc{Act}(\textit{lesion}, s, r) = s,\qquad \textsc{Act}(\textit{nolesion}, s, r)=r,
$$

where $s$ and $r$ are the values of $\textsc{fdt}(\underline{P_S},\underline G)$ and $\textsc{fdt}(\underline{P_R},\underline G)$.

$\textsc{Cancer}$ is a child of $\textsc{Lesion}$ but *not* of either $\textsc{fdt}$ node, because cancer does not evaluate the agent's algorithm. Intervening on $\textsc{fdt}(\underline{P_S},\underline G)$ therefore leaves $P(\textit{lesion})=p$ unchanged. The source computes that smoking beats refraining by $p\cdot\$1{,}000$, and so A-FDT smokes.

The prior $q$ on the non-intervened node $\textsc{fdt}(\underline{P_R},\underline G)$ appears identically in both hypotheticals and cancels out.

### 4.3 The transparent Newcomb problem

Both boxes are visible. Box B is filled iff the predictor predicts the agent would one-box *upon seeing a full box*. The graph has two decision nodes, $\textsc{fdt}_{\textit{full}}$ and $\textsc{fdt}_{\textit{empty}}$:

- $\textsc{Prediction}$ is a child of $\textsc{fdt}_{\textit{full}}$ (and of $\textsc{Accurate}$).
- $\textsc{Prediction}$ determines the box contents, and hence which node controls $\textsc{Act}$.

Let $q$ be the prior probability of two-boxing upon seeing an empty box. Facing a full box, A-FDT intervenes on $\textsc{fdt}_{\textit{full}}$:

$$
\begin{aligned}
\textit{onebox}:&\quad 0.99(1{,}000{,}000) + 0.01\cdot q(1{,}000) = 990{,}000 + 10q,\\
\textit{twobox}:&\quad 0.01(1{,}001{,}000) + 0.99\cdot q(1{,}000) = 10{,}010 + 990q.
\end{aligned}
$$

(The source's printed figure for the second line, "\$110,00 + $q\cdot$\$990", appears to be a typesetting error. The conclusion is unaffected.)

A-FDT one-boxes *while looking at a full box*. In the two-boxing hypothetical, she mostly sees an empty box. The source accepts this result and notes its equivalence to paying the driver in Parfit's hitchhiker problem.

### 4.4 Mechanical blackmail with an imperfect blackmailer

A blackmailer launches a program that will cost the agent \$1,000,000 unless she pays \$1,000. The blackmailer launches it iff she predicts the agent would pay. Let $\varepsilon$ be the probability that she wrongly predicts payment.

Having received the letter, the agent intervenes on $\textsc{fdt}_{\textit{blackmail}}$:

$$
\textit{pay}:\ -1{,}000,\qquad \textit{refuse}:\ -\varepsilon\cdot 1{,}000{,}000.
$$

She refuses iff $\varepsilon < 10^{-3}$. The source's example $\varepsilon = 0.0009$ falls below this threshold and yields refusal. Its contrasting case, which it states as "0.011%," must exceed 0.1% to yield payment as described, so the printed figure is presumably a slip.

The general lesson is that A-FDT trades off *how often you face the dilemma* against *what you do once you face it*. This is why the source says A-FDT agents act as they would have precommitted to act, without any actual precommitment.

### 4.5 Death in Damascus

Death predicts perfectly, so the agent dies wherever she goes. Intervening on the decision node moves Death's appointment book along with her location. The two hypotheticals differ only by the \$1,000 cost of fleeing, so A-FDT stays.

CDT, which holds Death's location fixed under surgery on $\textsc{Act}$, oscillates. The source argues that in this problem CDT would also decline a \$1 truly random coin that offers a genuine 50% chance of survival.

## 5. What the source leaves open, and how one might operationalize it

### 5.1 Where does $G$ come from?

The source is explicit that this is unresolved: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." Equation (4) "works *given* a graph" that is accurate. In the examples, the authors build the graphs by hand, using verbal criteria: predictor-like things depend on the function, lesion-like things do not.

*My proposed working rule:*

> Make a variable $Z$ a child of $\textsc{fdt}(\underline P,\underline G,\underline{x'})$ iff the mechanism generating $Z$, as the agent models it, contains an evaluation of her decision function on input $x'$ (or of a function of that output) whose correctness is what explains the correlation. Imperfections in that evaluation should be modeled as separate exogenous parents, like $\textsc{Accurate}$.

This rule reproduces every graph in the paper. Predictors, twins and future selves facing the same input get edges. Lesions and coincidental pink calculators do not.

Two cases need judgment:

- **Partial simulations.** The rule says to include an edge only to the extent that the simulation tracks the function's output, with the remainder pushed into noise.
- **Similar but non-identical algorithms.** I would model a shared node for the common sub-computation, but this is an additional assumption, not the paper's.

The source is clear on one point: the method of identifying dependencies is bracketed. What matters is that the agent "imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

### 5.2 Priors on decision nodes that are not intervened on

Several calculations depend on a prior $q$ for what the agent's function does on *other* inputs. In the paper's examples $q$ either cancels or is swamped by the stakes. The paper remarks that the "correct" $q$ can be verified, meaning it is what A-FDT itself would output on that input.

In general $q$ can matter. *My operational proposal* is to require **self-consistency**: priors on non-intervened $\textsc{fdt}$ nodes should equal (or concentrate on) the A-FDT outputs at those inputs. The source supplies no algorithm for finding such a fixed point, and §5.4 shows that one may not be unique.

### 5.3 Is $\textsc{Obs}=x$ conditioned on?

In Equation (4), the observation appears only as an index on the intervened node. In the transparent Newcomb discussion, the paper writes the objective with "$\textsc{Obs}=\textit{full}$" inside the expectation. However, its arithmetic gives weight to empty-box worlds, so it does *not* condition on the observation.

I follow Equation (4) and the arithmetic: **do not condition on observations**. The source explains why this is essential. It attributes harm to the "double update" of an earlier variant, Timeless Decision Theory, which both conditions on evidence *and* moves the point of intervention. If one conditioned on $\textit{full}$ here, two-boxing would win and the agent would face empty boxes.

### 5.4 Actions versus policies

Two footnotes state that "in the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions." Call that theory **policy functional decision theory (P-FDT)**. It selects

$$
\pi^* = \operatorname*{argmax}_{\pi:\mathcal X\to\mathcal A}\ \mathbb E\big(V \mid do(\textsc{fdt}(\underline P,\underline G,\underline{x'})=\pi(x')\ \ \forall x')\big)
$$

and then outputs $\pi^*(x)$. The source says the difference "will not make a difference in this paper" and matters "in certain multi-agent dilemmas."

*The following example is my own construction, not the paper's.* It shows where the gap lies. A fair coin shows the agent Red or Blue. A perfect predictor pays \$2 if the agent's function outputs $\textit{x}$ on both inputs, \$1 if it outputs $\textit{y}$ on both, and \$0 otherwise.

On seeing Red, A-FDT intervenes only on $\textsc{fdt}_{\textit{Red}}$, holding a prior $r=P(\textsc{fdt}_{\textit{Blue}}=\textit{x})$. It compares $2r$ (for $\textit{x}$) with $1-r$ (for $\textit{y}$), and chooses $\textit{y}$ whenever $r<1/3$.

Both "always $\textit{x}$" and "always $\textit{y}$" satisfy the self-consistency condition of §5.2. A-FDT can therefore settle at the inferior one, which pays \$1. P-FDT simply selects the policy (x, x) and gets \$2.

A-FDT thus behaves like a local, equilibrium-style optimizer across information sets, whereas P-FDT optimizes globally. Readers applying the theory should know which of the two they are using. This essay's subject is the action version, A-FDT.

### 5.5 Ties, zero probability, randomization

Equation (4) returns an argmax set, and no tie-breaking rule is given. Because interventions are defined even on prior-probability-zero values, A-FDT avoids EDT's problem of being unable to evaluate actions it is sure it will not take. The source notes that EDT, with extreme priors, "can be made to do *anything*."

Randomization is available only if randomized options are listed in $\mathcal A$. If they are, a predictor who can foresee the randomizer should be modeled as a child of the decision node, while a truly unpredictable coin should not. This is my reading of the source's Death in Damascus discussion.

## 6. Philosophical commitments and objections

**Counterpossibles.** A deterministic function has one output on a given input. Intervening on $\textsc{fdt}$ therefore means entertaining a logically impossible antecedent. The source calls the lack of a theory of counterpossible reasoning "the main drawback of FDT relative to CDT at this time." It argues, however, that CDT faces the same problem for deterministic agents, whose alternative physical acts are equally non-actual: "Any principled objection to the idea that FDT agents can 'control' their decision type will also imply that (deterministic) CDT agents cannot 'control' their decision token."

The source also considers an alternative, FDT′, which iterates over *other* decision functions. It argues that this does not escape the problem, because predictors of $d$ must still be imagined predicting as if $d$ behaved like $f_n$.

**Dominance.** The two-boxer's dominance argument, on the source's analysis, presupposes CDT-style counterfactuals. Every way of constructing hypotheticals induces its own dominance notion. Under A-FDT counterfactuals, which hold subjunctive dependencies fixed, A-FDT never takes a dominated act. The authors conclude that dominance gives no neutral standard, and they prefer to judge theories by utility achieved.

**Fairness.** Any theory can be punished by a problem that rewards a specific *procedure*. The source therefore restricts its claim of superiority to "fair problems." These are, informally, problems in which beliefs are accurate and outcomes depend only on the agent's behavior in the dilemma. Newcomb's predictor qualifies because "she punishes *two-boxers*," not CDT agents as such. The authors admit that formalizing fairness is open. For example, a game that punishes whoever matches a copy of an FDT agent is intuitively unfair, but no general rule yet says why.

**Global perspective and reflective stability.** On receiving blackmail, an A-FDT agent would not want to switch to CDT. Under her hypotheticals, a function that pays when blackmailed becomes a target. The source states, cautiously, that FDT is "so far as we know, reflectively stable in fair problems." It gives three supporting arguments for its stranger verdicts, such as one-boxing in front of a full box: the argument from precommitment, the argument from the value of information, and above all the argument from utility.

## 7. Conclusion

A-FDT is CDT's surgery moved one level up. Instead of intervening on the physical act, the agent intervenes on the node representing *her decision function's output on her actual input*. Everything subjunctively downstream of that node moves with it, including predictors, twins, and future copies of herself. Observations select which node to intervene on rather than being conditioned on.

The resulting rule, Equation (4), yields the verdicts the source advertises: it one-boxes in Newcomb's problem, smokes in the smoking lesion problem, pays in Parfit's hitchhiker problem, refuses blackmail, and stays in Damascus.

To apply it, one needs a model $(P, G)$, and A-FDT inherits the open problems of supplying that model:

- **Constructing $G$.** I proposed a working criterion: an edge exists iff the variable's mechanism computes the agent's function.
- **Priors on decision nodes that are not intervened on.** I proposed self-consistency.
- **The action–policy gap.** As my coordination example shows, A-FDT can settle in a suboptimal self-consistent state where policy-level P-FDT would not.

With those choices made explicit, A-FDT is a concrete, checkable procedure, and the essay's examples show how to carry it out.

## References

- Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge UP.
- Pearl, J. (2000). *Causality*. Cambridge UP.
- Yudkowsky, E. & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.