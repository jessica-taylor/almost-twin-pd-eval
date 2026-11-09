# A-FDT: Choosing by Intervening on Your Decision Function

## 1. The idea

Action functional decision theory (A-FDT) is the decision procedure given by Equation (4), Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." I use "A-FDT" for it throughout. Other theories are called by their own names: causal decision theory (CDT) and evidential decision theory (EDT).

The central claim is that an agent should treat her decision as the output of a fixed mathematical function. She should then ask which output of that function would yield the best outcome. She should not ask which physical act would cause the best outcome (CDT), or which act would be the best news (EDT).

All three theories maximize expected utility. They differ in how they build the "hypothetical" for each action. The source writes the common form as

$$\mathcal{EU}(a)=\sum_j P(a\hookrightarrow o_j;x)\,\mathcal U(o_j),$$

and, following Joyce, treats the connective $\hookrightarrow$ as the free parameter. The three theories read it as follows.

- **EDT, Eq. (2):** $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$. Hypotheticals come from conditioning.
- **CDT, Eq. (3):** $\arg\max_a \mathbb E(V\mid do(\mathrm{Act}=a),\mathrm{Obs}=x)$. Hypotheticals come from intervening on the physical act.
- **A-FDT, Eq. (4):**

$$\text{A-FDT}(P,G,x):=\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V\ \Big|\ do\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

Here $P$ is a probability distribution over the agent's model variables, and $G$ is a graph. The source's phrase is that $G$ "tells us how changing a logical variable affects all other variables." The node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ stands for the output of A-FDT itself when run on those inputs. The underlines mean dequoting: the variable's name depends on the model and the observation. The self-reference is harmless. The agent need not know the value of the node in order to have a variable representing it, and Kleene's recursion theorem ("quining") shows such self-representing structures can be built.

## 2. How to read the equation

**Two differences from CDT.** The source states them explicitly.

1. The intervention is on the node representing the algorithm's output, not on the physical act node.
2. Observations are handled differently. CDT conditions on $\mathrm{Obs}=x$. A-FDT instead changes *which node it intervenes on*: when the observation changes from $x$ to $y$, it moves from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$.

**What the intervention does.** Setting the algorithm node to $a$ propagates downstream through $G$. Everything that subjunctively depends on the function changes, and everything else is held fixed. This includes the agent's own act, any predictor's model of her, and a twin's choice. The source's slogan is that A-FDT is to subjunctive dependence as CDT is to causal dependence. In Peirce's terms, CDT intervenes on the token "my action is $a$," and A-FDT intervenes on the type.

**Subjunctive dependence.** Two systems subjunctively depend on a function if they compute it, or accurately model something that computes it, such as two calculators doing $6288+1048$. Causal dependence is a special case: a scribe copying a calculator's output also depends subjunctively on it. Mere statistical correlation is not subjunctive dependence. Two pink calculators in Paris and Tokyo are an example, since a green one in Paris would not change the one in Tokyo. If a predictor is imperfect, the dependence is weakened but not eliminated.

**Counterpossibles.** If the function is deterministic, then "it outputs *defect*" is, given its inputs, a logical falsehood when it in fact outputs *cooperate*. So A-FDT hypotheticals are counterpossible. The source admits that it lacks a $\mathtt{true}(\cdot)$ operator that updates $P$ on a false logical sentence, and calls this the main drawback relative to CDT. Its workaround is to *require the dependency structure $G$ as an input*, just as CDT takes causal structure as input. It adds that "figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem."

## 3. Worked applications

Procedure:
1. Build $(P,G)$ for the problem.
2. For each $a$, intervene on the relevant algorithm node and propagate.
3. Compute expected $V$.
4. Pick the maximum.

**Newcomb's problem.** The nodes are the algorithm $\mathrm{fdt}$, the Act, Prediction (driven by $\mathrm{fdt}$ and an accuracy variable that is 0.99 accurate), Box B, and $V$. Setting $\mathrm{fdt}=\textit{onebox}$ makes Act equal one-box and Box B full with probability 0.99, so expected utility is $0.99\times\$1{,}000{,}000=\$990{,}000$. Setting $\mathrm{fdt}=\textit{twobox}$ gives $0.01\times 1{,}001{,}000+0.99\times 1{,}000\approx\$11{,}000$. A-FDT one-boxes. No retrocausation is assumed: the agent just declines to imagine her act changing while the algorithm's output stays fixed.

**Smoking lesion.** Here the graph differs. Cancer is a child of the lesion, not of the algorithm, so intervening on the algorithm does not change the cancer probability. In the source's formalization the lesion also fixes which of two preference-versions of the algorithm (one valuing smoking, one not) controls the act. The agent cannot tell which, and the intervention leaves $P(\text{lesion})=p$ fixed. Smoking beats refraining by $p\cdot\$1{,}000$ in the source's calculation, so A-FDT smokes. One rule therefore gives one-boxing and smoking, even though the same probability table underlies both problems. The difference is entirely in $G$.

**Transparent Newcomb and Parfit's hitchhiker.** The agent sees a full box. The source's graph has two nodes, $\mathrm{fdt}(\ldots,\textit{full})$ and $\mathrm{fdt}(\ldots,\textit{empty})$, and the prediction determines which one controls the act. Intervening on the "full" node with *twobox* makes the prediction likely "two-box," so the box is probably empty and the agent probably runs the other node. With $q$ her credence that she two-boxes on seeing empty:

- one-box: $\$990{,}000+0.01q\cdot\$1{,}000$
- two-box: about $\$11{,}000+q\cdot\$990$

A-FDT one-boxes while looking at a full box. This is the same structure as paying the driver in Parfit's hitchhiker. The agent does not condition on what she sees; she imagines that a different output would have meant seeing something different.

**Mechanical blackmail.** After the letter arrives, paying means being blackmailed with certainty and losing $\$1{,}000$. Refusing means, in the hypothetical, almost never being blackmailed. A-FDT refuses.

The source also gives the fallible-predictor arithmetic. If the blackmailer errs with probability 0.0009, refusing costs $0.0009\times\$1{,}000{,}000=\$900$ in expectation, versus a certain $\$1{,}000$ for paying, so A-FDT refuses. If the error rate is 0.011%, the cost is about $\$1{,}100$, so A-FDT pays. Note the consequence: she may refuse while knowing this particular blackmailer erred.

**XOR blackmail.** The infestation is not downstream of the algorithm, so intervening leaves the termite probability unchanged. A-FDT refuses, whereas EDT, conditioning on the good news, pays. Carl the CDT agent also refuses, but his hypothetical has the predictor erring.

**Death in Damascus.** Death's book entry depends on the algorithm. Whatever the intervention sets, Death is where the agent goes, so fleeing only costs $\$1{,}000$. A-FDT stays. CDT's hypotheticals hold Death fixed and therefore oscillate.

**Twin dilemma and coordination.** Cooperation yields $\$1{,}000{,}000$ versus $\$1{,}000$ for defection, because the twin's node is downstream of the shared function.

## 4. Why not condition, and why not break everything?

The source's diagnosis is that EDT "respects too many" action–environment correlations and CDT "too few." Cosmic ray problem: an agent who almost always takes $\$1$ infers that taking $\$100$ means she was hit and must pay a hospital bill, so she takes $\$1$. A-FDT and CDT ignore that merely statistical correlation and take $\$100$.

For CDT, with a perfect predictor, the "what if I had one-boxed?" answer describes a world where an infallible predictor erred. A-FDT preserves the logical correlation but not the spurious one. The aim is that $G$ encodes exactly the dependencies that would persist under a counterpossible change of the function's output.

## 5. Dominance, fairness, and value of information

- **Dominance.** Every method of constructing hypotheticals induces its own dominance relation. Two-boxing dominates only under CDT-style counterfactuals. Under A-FDT counterfactuals, A-FDT never takes a dominated action. Dominance therefore cannot adjudicate between theories, and the source prefers utility achieved.
- **Fairness.** The source claims A-FDT does best on "fair" problems, where outcomes depend on the agent's behavior and not on her decision procedure as such. No formal definition is given, and footnote 15 shows an obstacle: a problem that punishes copying the A-FDT agent is unfair to it, and it is unclear how to construct the analogous problem for rivals.
- **Information and precommitment.** A-FDT acts as it would have precommitted to act, so it needs no binding mechanisms and never assigns negative value to information.

## 6. What the source leaves open, and my proposals

*Claimed by the source:* Eq. (4); the surgery analogy to CDT; the case analyses above; the claim of optimality on fair problems (stated as an empirical impression, "the authors have not been able to construct" a counterexample).

*Left open:* how to learn or define $G$; how to define counterpossible conditioning; formal fairness; and whether A-FDT is optimal.

*Footnote-level detail:* the authors' preferred formalization intervenes on **policies** (mappings from observations to actions), and the source says the difference only matters in multi-agent problems. Eq. (4) as written intervenes on the action output for a given $x$.

*My own operational proposals (not from the source):*

1. **Build $G$ by asking, "who or what computes or models this function?"** Put an edge from the algorithm node to each such thing (predictors, twins, copies, the agent's own later selves). Do not add edges for mere shared causes. This is a heuristic implementing the source's stated assumption that she imagines changes "in all and only those things that subjunctively depend on the output."
2. **Include all branches of the algorithm.** As in the transparent Newcomb graph, include a node for each possible observation, with the dependence on the other branches made explicit, so that off-path nodes with credence $q$ are handled. In the source's examples the answer is insensitive to $q$, which is a useful check.
3. **Sanity test.** Compute every hypothetical under the actual-world assumption that models are accurate. If the model implies that a predictor you believe reliable errs in some hypothetical, $G$ is probably missing an edge.
4. **Limits.** In problems that punish the algorithm itself, no theory is safe. The edges give no help there, so don't expect them to.

## 7. Conclusion

A-FDT is CDT's surgical method transplanted from the physical act to the logical output of the agent's own decision function, with observations handled by switching nodes instead of conditioning. Given a correct dependency graph, one rule recovers one-boxing, smoking, paying in Parfit's case, refusing blackmail, and staying in Damascus. The cost is that the graph, and the counterpossible reasoning behind it, are inputs the theory does not yet know how to derive.