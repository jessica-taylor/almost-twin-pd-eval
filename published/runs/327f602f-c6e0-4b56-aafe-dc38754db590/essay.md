# A-FDT: Choosing the Output of One's Decision Function

## 1. What this essay covers

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* proposes that a rational agent should treat her decision as the output of a fixed mathematical function. On their account she should choose by asking: "Which output of this very function would yield the best outcome?"

The paper gives this idea a concrete formula, its Equation (4) in Section 5. Under that formula the agent intervenes on a single variable in her world-model: the output of her decision procedure *on the particular input she has actually received*. The intervened value is an action. Footnotes 7 and 16 add that the authors' "preferred formalization" instead selects a *policy*, meaning a map from observations to actions.

Throughout, I call the action-intervening theory defined by Equation (4) **A-FDT**. I call the policy-selecting variant mentioned in the footnotes **P-FDT** so that the two are never confused. The comparison theories are evidential decision theory (EDT) and causal decision theory (CDT).

When I quote the paper, I keep its wording, so quotations say "FDT". Everything the paper asserts is attributed to it. Proposals of my own are flagged as such.

## 2. A shared template with three ways to fill it

All three theories maximize expected utility in the general form the paper borrows from Gibbard and Harper:

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}
$$

Here $a\in\mathcal A$ is an action, $x$ is the observation history, $o_j$ ranges over outcomes, and $\hookrightarrow$ is a connective for "decision hypotheticals." Following Joyce, the paper treats the interpretation of $\hookrightarrow$ as the free parameter that separates the theories. They agree on how to value outcomes and disagree about "the epistemic perspective from which actions are to be evaluated."

Write $V := \mathcal U(\textsc{Outcome})$. The paper's formulas are:

$$
\text{EDT}(P,x) = \arg\max_a \mathbb E[V \mid \textsc{Obs}=x,\ \textsc{Act}=a], \tag{2}
$$
$$
\text{CDT}(P,G,x) = \arg\max_a \mathbb E[V \mid do(\textsc{Act}=a),\ \textsc{Obs}=x], \tag{3}
$$
$$
\boxed{\ \text{A-FDT}(P,G,x) = \arg\max_{a\in\mathcal A}\ \mathbb E\big[V \;\big|\; do\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\big]\ } \tag{4}
$$

EDT builds its hypotheticals by conditioning. CDT builds them by Pearl-style surgery on the physical action node $\textsc{Act}$, using a causal graph $G$. A-FDT also uses surgery, but on a different node.

## 3. Unpacking Equation (4)

**The world-model.** The pair $(P,G)$ is a probability distribution together with a directed graph. In A-FDT the graph encodes "the logical, mathematical, computational, causal, etc. structure of the world," not only causal structure. $P$ must contain variables whose values are *outputs of mathematical functions*. The paper's example is a variable for the value of $6288+1048$, which "(hopefully) has most of its probability on 7336."

**The intervention node.** $\textsc{fdt}(\underline P,\underline G,\underline x)$ is the variable whose value is whatever the A-FDT algorithm outputs when run on inputs $(P,G,x)$. The underlines mark "dequoting": the variable's *name* is built from the inputs. The definition is self-referential, because the model contains a variable standing for the output of the algorithm being run on that very model. The paper argues this is harmless. The agent needs a variable that *represents* the output, not knowledge of its value, and Kleene's recursion theorem ("quining") shows such self-representing structures can be built.

**Edges out of the node.** The node has an arrow to every variable that *subjunctively depends* on it. The paper's slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." Such dependents include:

- the agent's own physical action;
- a predictor's prediction;
- a twin's choice;
- anything else whose value is fixed by computing the same function on the same input.

Mere statistical correlation does not create an edge. The paper illustrates with two calculators that both happen to be pink. Their colors are correlated, but "if the scribe had bought a green calculator instead, the one in Tokyo would still be pink." Causal dependence, by contrast, is a special case of subjunctive dependence.

**What the formula leaves out.** Equation (4) does *not* condition on $\textsc{Obs}=x$. The paper says so explicitly: "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." The observation $x$ appears only inside the node's name. Concretely:

- $P$ functions as a prior over the whole problem, including branches in which the agent would have observed something else.
- The intervention changes the output of one function on one input.
- Whatever then propagates downstream, including which observation the agent would have received, is recomputed.

This single feature produces A-FDT's most distinctive verdicts, discussed in Section 5.

**The procedure.** Read as an algorithm, Equation (4) says:

1. Given $(P,G)$ and the observation $x$, locate the node $\textsc{fdt}(\underline P,\underline G,\underline x)$.
2. For each $a\in\mathcal A$, form $P(\cdot\mid do(\textsc{fdt}(\underline P,\underline G,\underline x)=a))$. That is, set the node to $a$, propagate along outgoing edges, and leave everything not downstream untouched. The paper calls the result the agent's "hypothetical for $a$."
3. Compute $\mathbb E[V]$ in each hypothetical and output the maximizer.

Because $do$ is surgery rather than conditioning, the hypothetical is well defined even when the agent's prior gives $a$ probability zero. EDT lacks this property: the paper notes EDT "cannot imagine" acting against an extreme prior.

**Agreement with the other theories.** The paper observes that when every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from $\textsc{Act}$'s own dependence on the $\textsc{fdt}$ node,

$$
\mathbb E[V\mid a] = \mathbb E[V\mid do(a)] = \mathbb E[V\mid do(\textsc{fdt}(\underline P,\underline G)=a)],
$$

so all three theories agree. A-FDT departs from the others only when something other than the agent's body depends on her decision function. The paper calls such cases Newcomblike.

## 4. Worked examples

In each case below I describe the graph, perform the intervention, and compare expected values.

### Newcomb's problem

**Setup.** The predictor is 99% accurate. The graph is
$$\textsc{fdt}\to\textsc{Act},\quad \textsc{fdt}\to\textsc{Prediction}\leftarrow\textsc{Accurate},\quad \textsc{Prediction}\to\textsc{Box B},\quad (\textsc{Act},\textsc{Box B})\to V.$$

**Hypotheticals.**
- $do(\textsc{fdt}=\textit{onebox})$ makes Box B full with probability 0.99, so $\mathbb E[V]=\$990{,}000$.
- $do(\textsc{fdt}=\textit{twobox})$ makes Box B full with probability 0.01, so $\mathbb E[V]=0.01(1{,}001{,}000)+0.99(1{,}000)=\$11{,}000$.

**Verdict.** A-FDT one-boxes.

By contrast, CDT intervenes on $\textsc{Act}$, which is not upstream of the prediction. The probability $p$ that Box B is full is then the same under both actions, and two-boxing wins by \$1,000 for every $p$.

The paper stresses that no retrocausation is assumed. The agent "does not think that a physical signal passes between her action and the predictor's prediction." She thinks the action and the prediction are two computations of one function. The psychological twin prisoner's dilemma has the same structure, with the twin's choice as a second child of $\textsc{fdt}$. A-FDT cooperates.

### Smoking lesion

**Setup.** The lesion causes both a taste for smoking and cancer. Cancer is not computed from the agent's decision function, so there is no edge $\textsc{fdt}\to\textsc{Cancer}$.

The paper's full formalization is somewhat elaborate. The lesion determines the agent's utility function, so it determines *which* of two nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ or $\textsc{fdt}(\underline{P_R},\underline G)$, controls $\textsc{Act}$. The agent does not know which node she is. She intervenes on the node named by her actual model, $\textsc{fdt}(\underline{P_S},\underline G)$.

**Hypotheticals.** Intervening on that node leaves $P(\textit{lesion})=p$ unchanged. Smoking comes out ahead by exactly $p\cdot\$1{,}000$: the probability that this node is the one controlling the action, times the value of smoking.

**Verdict.** A-FDT smokes. Together with the Newcomb result, this rebuts Gibbard and Harper's suggestion that one cannot consistently both one-box and smoke.

The paper itself then recommends that philosophers "abandon the dilemma" as confused.

### Transparent Newcomb and Parfit's hitchhiker

**Setup.** Both boxes are transparent. The predictor fills Box B iff she predicts the agent would one-box *upon seeing a full box*. There are two decision nodes: $\textsc{fdt}(\ldots,\textit{full})$ and $\textsc{fdt}(\ldots,\textit{empty})$. The prediction determines which observation occurs and hence which node drives $\textsc{Act}$.

The agent sees a full box and intervenes on $\textsc{fdt}(\ldots,\textit{full})$. Let $q$ be her prior that $\textsc{fdt}(\ldots,\textit{empty})=\textit{twobox}$.

**Hypotheticals.**
$$
\begin{aligned}
\textit{onebox}:&\quad 0.99(1{,}000{,}000)+0.01\,q\,(1{,}000) = 990{,}000+10q,\\
\textit{twobox}:&\quad 0.01(1{,}001{,}000)+0.99\,q\,(1{,}000) = 10{,}010+990q.
\end{aligned}
$$
(The extracted source prints the second line with a typographical error. The figures above are the direct computation.)

**Verdict.** One-boxing wins for every $q\in[0,1]$. A-FDT therefore leaves the visible \$1,000 behind.

The paper argues this is "precisely equivalent" to paying the driver in Parfit's hitchhiker problem, which CDT and EDT both refuse to do.

### XOR blackmail

**Setup.** An infallible predictor sends a letter iff exactly one of two things holds: (no termites and you will pay \$1,000), or (termites and you will not pay). Termites cost \$1,000,000 and have prior probability $p$. On receiving the letter the agent intervenes on $\textsc{fdt}(\ldots,\textit{letter})$. The termite node has no incoming edge from it.

**Hypotheticals.**
- *pay*: the letter arrives exactly when there are no termites. $\mathbb E[V] = -p\cdot10^6-(1-p)\cdot 10^3$.
- *refuse*: the letter arrives exactly when there are termites. $\mathbb E[V] = -p\cdot10^6$.

**Verdict.** Refusing is better by $(1-p)\cdot\$1{,}000$, so A-FDT refuses.

EDT pays. It conditions on both the letter and the act, which makes paying "good news" about termites. CDT also refuses, but its hypothetical has the infallible predictor erring.

### Mechanical blackmail

**Setup.** The blackmailer runs a damaging program, costing \$1,000,000, only if she predicts the agent would pay \$1,000 to stop it. Let $\varepsilon$ be the probability that she wrongly predicts "pays."

**Hypotheticals.**
- *pay*: the agent is blackmailed and pays, so $\mathbb E[V]=-\$1{,}000$.
- *refuse*: the agent is blackmailed only by error, so $\mathbb E[V]=-\varepsilon\cdot 10^6$.

**Verdict.** A-FDT refuses iff $\varepsilon<10^{-3}$, and does so even while holding the letter.

The paper's numerical example uses $\varepsilon=0.0009$ (refuse). Its switch-over example is printed as "0.011%", which is inconsistent with its own arithmetic. On the paper's numbers the threshold is 0.1%, so "0.11%" was presumably intended.

### Death in Damascus

**Setup.** Death predicts perfectly, so Death's location is a child of $\textsc{fdt}$.

**Hypotheticals.** Both interventions yield death. Fleeing additionally costs \$1,000.

**Verdict.** A-FDT stays in Damascus, stably and without deliberational oscillation. The paper argues CDT is "unstable" here. By its analysis, CDT can even refuse to pay \$1 for a genuinely random coin that would give a 50% chance of survival.

## 5. How A-FDT treats observations and counterfactuals

Two hypotheticals from the examples look strange at first. In one, an agent who sees a full box imagines, under the two-box option, seeing an empty one. In another, an agent holding a blackmail letter imagines never having received it. The paper embraces this: "FDT says that agents should entertain the hypothesis that, if their action were different, they might have *made different observations*."

The formal source is the missing conditioning on $\textsc{Obs}=x$ noted in Section 3. The observation tells the agent *which function-call she is*, not which world to restrict attention to.

A paper footnote explains why conditioning would go wrong. An earlier variant, Timeless Decision Theory, both conditioned on evidence and moved the intervention point. The footnote calls this a harmful "double update." In XOR blackmail, conditioning on the letter after intervening would make $\textsc{Act}$ informative about termites again, as in EDT.

The paper supplies several supporting arguments:

- **Precommitment.** CDT and EDT agents would pay to bind themselves to A-FDT's choices in advance. "FDT agents simply act as they would have ideally precommitted to act."
- **Value of information.** A-FDT does not assign negative value to information.
- **Utility.** The paper calls this argument "the one that gives the precommitment and value-of-information arguments their teeth." Predictors can see what kind of agent they face, so A-FDT agents mostly see full boxes and are rarely blackmailed.

The paper also addresses dominance. "Two-boxing dominates" is true only relative to CDT's way of holding things fixed. Every way of constructing hypotheticals induces its own notion of dominance, and A-FDT never takes an action that is dominated in its own sense.

On the metaphysics, the hypothetical $do(\textsc{fdt}=a)$ for the non-chosen $a$ is a *counterpossible*: a function has only one output on a given input. The paper concedes the lack of a good theory of counterpossibles is "the main drawback of FDT relative to CDT." It sidesteps the problem by taking $G$ as input. Its defence is a parity argument: a deterministic CDT agent equally imagines her single possible token act being otherwise.

The paper also restricts its claims of superiority to "fair" problems, in which the outcome depends on the agent's behaviour rather than on which decision procedure she uses. It admits it has no formal definition of fairness.

## 6. What the source leaves open, and how to operationalize it

### (a) Where does $G$ come from?

The paper is explicit: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." Equation (4) works *given* a correct graph, much as CDT works given a correct causal graph.

*My operational proposal* is a rule of thumb, not something the source states. Draw an edge from $\textsc{fdt}(\underline P,\underline G,\underline x)$ to a variable $Z$ exactly when $Z$'s mechanism, in your model, computes or reliably tracks the agent's decision on input $x$. Examples are a simulation, a mental model, a twin running the same reasoning, or the agent's own body. Model any unreliability as a separate noise parent of $Z$, as $\textsc{Accurate}$ does in Newcomb.

Do not draw an edge merely because $Z$ correlates with the act through a common cause that does not evaluate the decision function, as with the lesion. The test is the paper's: would $Z$ differ "if this very decision procedure produced a different conclusion"?

Edge cases remain undecided. They include partial similarity (a predictor running a crude approximation of your algorithm) and agents using different but similar functions. Representing these by noise nodes is an assumption I am adding.

### (b) The other decision nodes

In the transparent Newcomb problem and the blackmail problems, $\textsc{Act}$ can be controlled by $\textsc{fdt}$ nodes for *other* inputs. A-FDT intervenes on only one node and holds the others at their prior distributions (the $q$ above).

The paper notes that in its examples the verdict does not depend on $q$. It describes the correct $q$ as determined by the agent's actual behaviour on those inputs. The general case is not settled, and here A-FDT and P-FDT can come apart.

*My illustration*, which is not from the paper, shows how. A fair coin, independent of the agent, shows her observation $x$ or $y$. A predictor pays \$100 iff the agent's outputs on $x$ and $y$ coincide. Separately, action $R$ earns an extra \$1.

Suppose the agent observes $x$ and her prior gives probability $s$ to $\textsc{fdt}(\ldots,y)=L$. A-FDT compares:
- $L$: $\tfrac12(100s)+\tfrac12(100s)=100s$;
- $R$: $100(1-s)+1$.

So the verdict at $x$ depends on $s$. Both "$L$ everywhere" and "$R$ everywhere" are self-consistent: each is a best response to correct beliefs about the other node. But $(R,R)$ yields \$101 and $(L,L)$ yields \$100. P-FDT maximizes over the whole map $\{x,y\}\to\mathcal A$ at once and selects $(R,R)$.

This is consistent with the paper's remark that the policy version "makes a difference in certain multi-agent dilemmas." In my example the predictor plays the role of the other agent. For deciding cases with A-FDT, I recommend two steps:

1. Set the priors on other-input nodes to the agent's best estimate of her actual dispositions.
2. Check whether the verdict is robust across $s$. If it is not, report the equilibria and note that A-FDT's prescription is prior-dependent there.

### (c) Ties and mixed acts

Equation (4) is an $\arg\max$ and specifies no tie-breaking. Nothing in the source requires randomization. I would treat any maximizer as permitted.

If an action set includes a randomizing device, model the device as a node. Whether predictors can see its output is then a modelling question for $G$, as in the paper's Death in Damascus coin discussion.

## 7. A recipe for unfamiliar cases

1. **Variables.** List outcomes, utilities, observations, and every process that might model the agent's decision.
2. **Decision nodes.** Add one $\textsc{fdt}$ node per possible observation. Connect each to $\textsc{Act}$, gated by whatever determines which observation occurs.
3. **Dependence edges.** Draw edges from each node to everything that subjunctively depends on it, using the test in §6(a).
4. **Prior.** Give $P$ as a prior over the entire problem. Do not condition on the realized observation.
5. **Intervene and compare.** Intervene on the node for the actual observation, propagate, and compare $\mathbb E[V]$ across actions.
6. **Robustness.** Check sensitivity to priors over other decision nodes.

If no variable other than $\textsc{Act}$ depends on the decision function, the procedure reduces to CDT and the agent can stop early.

## 8. Conclusion

A-FDT takes the formal machinery of CDT, namely expected utility under graph surgery, and moves the point of surgery from the physical act to the logical output of the agent's decision function on her actual input. Two consequences follow:

- **Predictors and twins.** Anything that computes the same function, such as a predictor, a twin, or Death's appointment book, varies together with the agent's choice in her hypotheticals. Mere statistical correlates stay fixed.
- **Observations.** Observations select the intervention node instead of being conditioned on. The agent therefore acts as she would have precommitted to act.

The resulting verdicts are one-boxing in Newcomb's problem, smoking in the smoking lesion problem, paying in Parfit's hitchhiker problem, refusing XOR and mechanical blackmail, and staying in Damascus.

The paper is candid about what remains unfinished. There is no account of how to learn the subjunctive-dependence graph, no semantics for counterpossibles, and no formal notion of fairness. One further gap is my own observation rather than the paper's: priors over the agent's outputs on other inputs can matter, and this is where the authors' preferred policy formulation (P-FDT) improves on A-FDT. Within these limits, Equation (4) is a precise and usable decision procedure.

---

**References**

- Yudkowsky, E., and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060.
- Gibbard, A., and Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*.
- Pearl, J. (2000). *Causality*.