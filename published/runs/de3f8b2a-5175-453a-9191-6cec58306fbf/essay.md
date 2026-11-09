# A-FDT: Choosing by Intervening on One's Own Decision Function

## 1. The idea

Decision theories can be seen as expected-utility maximizers that differ in how they build the hypothetical "what if I did a?". The source paper (Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality") states the general form as

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

and, following Joyce, treats the connective "↪" as the free parameter. Evidential decision theory (EDT) reads it as conditioning. Causal decision theory (CDT) reads it as Pearl's intervention on the physical act. This essay is about the third reading, which I call **A-FDT**, following the paper's Equation (4):

$$\text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

Here $P$ is a probability model of the world, and $G$ is a graph encoding dependence structure. $x$ is the observation history, $V=\mathcal U(\text{Outcome})$, and $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a variable inside the model that represents the output of the very procedure being computed. The underlines mean dequoting: the variable's name is built from the model and observation, so the procedure refers to itself by quining, which the paper justifies via Kleene's recursion theorem. The agent need not know the value of the variable in order to have a variable representing it.

In words, the A-FDT agent asks "which output of this very function would yield the best outcome?" and then executes that output.

## 2. Two departures from CDT

Equation (4) differs from CDT's $\mathbb E(V\mid \mathtt{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$ in two ways, both stressed by the source.

1. **Where the intervention happens.** CDT intervenes on the token "my physical act is $a$". A-FDT intervenes on the type, the logical output of the decision function. Everything that depends on that output in $G$ changes with it: my body's act, a twin's act, a predictor's prediction. Everything else is held fixed.
2. **How observations enter.** CDT conditions on $\mathrm{Obs}=x$. A-FDT does not condition. A new observation changes *which node is intervened on*, from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$. Hence an A-FDT agent can imagine that, had her output been different, she would have seen different things. The paper notes that its authors' preferred formalization intervenes on whole policies (maps from observations to actions); this makes no difference in the paper's examples.

Whenever every correlation between action and world is causally produced by the action, all three theories coincide. The paper states $\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\mathrm{fdt}=a)]$ in that case. They diverge when something correlates with the action without being caused by it, such as a predictor or a twin.

## 3. Subjunctive dependence: the input A-FDT needs

A-FDT's hypotheticals respect **subjunctive dependence**. Two systems subjunctively depend on a function when they compute it, so that changing the function's output would change both. Calculators computing $6288+1048$ are the paper's model case. Causal dependence is a special case: a scribe copying a calculator's output depends on it both causally and subjunctively. Mere statistical correlation is not dependence: two pink calculators do not covary counterfactually in colour.

Note that the paper says its notion requires evaluating counterpossibles, since the function's output is logically fixed. It argues the difficulty is technical rather than philosophical. A-FDT as written sidesteps it by taking $G$ as given, as CDT takes its causal graph as given.

**What the source leaves open (it says so itself):** how to learn or deduce $G$, that is, the structure of subjunctive dependencies, from observation. It calls this "perhaps the largest open problem" for the theory. So A-FDT is a procedure *conditional on* a correct dependence graph. A $\mathtt{true}$ operator over logical sentences, the paper says, is not yet definable.

## 4. How to apply it

The paper's worked examples suggest a recipe. This is my systematization, not a quoted algorithm.

1. List the places where the decision procedure, or a reliable model of it, is instantiated: your body, twins, predictors, future selves, simulations.
2. Draw $G$ with a node $\mathrm{fdt}(\ldots,x)$ for each observation $x$ you might receive, with arrows into every instantiation it controls. Include arrows that determine *which* observation you receive when a predictor decides that.
3. For each $a$, set the node for your actual observation to $a$, propagate, and leave non-dependent variables, such as the lesion or infestation, at their prior.
4. Compute expected utility and take the argmax.

## 5. Examples

**Newcomb's problem.** The only nodes dependent on the A-FDT variable are Act and Prediction (hence Box B). Intervening with one-boxing gives box-full probability 0.99 and expected value $0.99\times 1{,}000{,}000=\$990{,}000$. Two-boxing gives box-full probability 0.01 and $0.01\times1{,}001{,}000+0.99\times1{,}000\approx\$11{,}000$. A-FDT one-boxes. No retrocausation is involved: the agent merely declines to imagine her output changing while the predictor's model of that output stays fixed.

**Smoking lesion.** The lesion is not a function of the decision procedure, so the A-FDT variable connects to Act but not to Cancer. Lesion probability $p$ is unchanged by intervention, and smoking gains $\$1{,}000\cdot p$ by the paper's calculation, so the agent smokes. The paper's formalization involves two utility functions (lesion makes smoking attractive) and hence two candidate procedures, $\mathrm{fdt}(P_S,G)$ and $\mathrm{fdt}(P_R,G)$, with the lesion selecting which controls Act. The paper concedes the setup is contrived and recommends abandoning it. The same equation yields one-boxing and smoking, which the paper credits to using different graphs, since the dependence structure of a predictor differs from that of a lesion.

**Transparent Newcomb and Parfit's hitchhiker.** Seeing a full box, the agent intervenes on $\mathrm{fdt}(\ldots,\textit{full})$. Setting that node to two-box makes the predictor probably leave the box empty, in which case she would be running the *empty* node instead. With $q$ her credence that she two-boxes on seeing empty, one-boxing yields $\$990{,}000+0.01q\cdot\$1{,}000$ while two-boxing yields about $\$11{,}000+q\cdot\$990$. She one-boxes even though she sees the full box. The hitchhiker is structurally identical, so she pays. Likewise in mechanical blackmail she refuses: paying makes blackmail near-certain, while refusing makes it near-absent. With a fallible blackmailer erring with probability 0.0009, refusing costs about $0.0009\times\$1{,}000{,}000 = \$900$ in expectation versus a sure \$1,000 for paying, so she still refuses. At error 0.011% paying is cheaper and she pays (the paper's figures).

**XOR blackmail.** The infestation node does not depend on the output, but the letter's arrival does. Refusing is correct, because the letter carries no causal or subjunctive handle on termites.

**Death in Damascus.** Death's book entry depends on the decision function, so wherever the agent decides to go, Death is there. She stays and saves \$1,000, avoiding CDT's instability.

**Coordination.** In a voting game where each of ten agents pays \$1,000 and all must participate for a \$1,000,000 prize, A-FDT agents treat their decisions as subjunctively linked and vote. For a gym habit, today's decision and next week's are instances of one function.

## 6. Dominance, fairness, and the "global perspective"

A CDT-style dominance argument holds the prediction fixed while switching the act. The paper replies that this simply restates CDT's counterfactual method, and that every hypothetical-construction has its own dominance notion. A-FDT's dominance holds the dependence relations fixed and switches the output; by that notion two-boxing is dominated.

Because A-FDT's hypotheticals depend on how others model it, the source restricts its superiority claim to "fair" problems, where outcomes depend on the agent's behaviour rather than on which procedure she uses. It admits it lacks a formal criterion for fairness and no theory wins in all problems. Its claim of A-FDT's superiority rests on empirical performance in cases it has examined; it states no theorem.

## 7. My own assumptions and interpretations

These go beyond the source.

- **Graph construction heuristic.** A reasonable operational rule: put an arrow from the decision node to any variable that is computed by a process that would be run on the same function or on an accurate model of it, and omit arrows to variables that only correlate by common cause. Such a rule is a stand-in for the unsolved dependence-learning problem and can go wrong if the agent's model of the predictor is wrong.
- **Imperfect predictors.** Treat accuracy as a stochastic node (as in the paper's "Accurate" variable) between the decision node and the prediction. Then errors stay inside the intervention rather than being "held fixed".
- **Partial dependence and uncertainty about $G$.** The source gives no method. A natural proposal is to average A-FDT values over a distribution on graphs. I flag this as unvalidated.
- **Policy-level evaluation.** Evaluating whole policies, as footnote 7 of the paper prefers, is the safer reading whenever different observation branches can feed back into each other, as in blackmail.

## 8. Conclusion

A-FDT keeps the expected-utility skeleton common to the standard theories and changes only the epistemic perspective: intervene on the output of one's own decision function and let that ripple through every subjunctively dependent quantity, leaving everything else at its prior. This one rule gives cooperation with twins, one-boxing, smoking, paying the hitchhiker, and refusing blackmail, with no need for ratification or precommitment. Its main weakness is also its main input: it needs a correct dependence graph, and the source offers no principled way to produce one. Applying A-FDT to unfamiliar cases therefore reduces to a modelling question, namely which parts of the world run, or reliably model, your decision procedure.