# A-FDT: Action Functional Decision Theory, Explained and Applied

## 1. The core idea

Yudkowsky and Soares's paper "Functional Decision Theory: A New Theory of Instrumental Rationality" presents a family of decision procedures. For this essay, **A-FDT** is the version given by **Equation (4), Section 5**, which selects an *action*. The paper's footnotes say its authors prefer a policy-selecting version, and I note below where that matters. The source says that treating one's decision as "the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" is the normative principle.

A-FDT is an expected-utility theory that differs from causal decision theory (CDT) and evidential decision theory (EDT) only in how it builds its hypotheticals. Section 1 contrasts three questions:
- CDT: "Which physical act of mine causes the best outcome?"
- EDT: "Which physical act of mine would be the best news to hear I took?"
- A-FDT: "Which output of this decision procedure causes the best outcome?"

## 2. The formal definition

All three theories maximize Equation (1),

$$\mathcal{EU}(a)=\sum_j P(a\hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

and differ in how they read the connective "$\hookrightarrow$". Writing $V=\mathcal U(\textsc{Outcome})$:

- EDT (2): $\arg\max_a \mathbb E(V\mid \textsc{Obs}=x,\textsc{Act}=a)$.
- CDT (3): $\arg\max_a \mathbb E(V\mid \mathtt{do}(\textsc{Act}=a),\textsc{Obs}=x)$.
- **A-FDT (4):**
$$\mathrm{FDT}(P,G,x)\coloneqq\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V\mid \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The inputs are:
- $P$, a probability distribution over the world-model's variables. These include variables for the outputs of mathematical functions, such as the value of $6288+1048$.
- $G$, a graph encoding how changing a *logical* variable changes other variables. It records causal, logical, computational and other subjunctive structure, and it is supplied as input.
- $x$, the observation.

$\textsc{fdt}(\underline P,\underline G,\underline x)$ is a node representing the output of A-FDT itself on those inputs. The underlines mean dequoting, so the variable's name depends on the model. This self-reference is harmless. The agent need not know the *value* of $\mathrm{FDT}(P,G,x)$ to have a variable *representing* it, and Kleene's recursion theorem ("quining") shows such self-representing structures can be built.

Equation (4) differs from CDT in two ways:
1. The intervention is on the node for the *decision function's output*, not on the physical act node.
2. Observation is handled differently. CDT conditions on $\textsc{Obs}=x$. A-FDT changes *which node* it intervenes on: moving from $x$ to $y$ shifts the intervention from $\textsc{fdt}(\underline P,\underline G,\underline x)$ to $\textsc{fdt}(\underline P,\underline G,\underline y)$.

The second difference is what makes A-FDT behave as if it does not update. Counterfactual worlds in which the output differs can be worlds where the agent saw something else.

## 3. Subjunctive dependence

A-FDT is to subjunctive dependence as CDT is to causal dependence. Two systems subjunctively depend on a function when both compute it, or when one contains an accurate representation of it. A predictor's model of the agent is the standard case, which the paper compares to two calculators computing $6288+1048$.

The paper claims:
- Causal dependence is a special case of subjunctive dependence.
- Mere statistical correlation does not entail subjunctive dependence. Two coincidentally pink calculators are not linked.
- A-FDT agents imagine "corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

A hypothetical in which a deterministic function outputs something other than what it does is a *counterpossible*. The paper concedes that lacking a satisfactory account of counterpossible reasoning is "the main drawback" relative to CDT. Its strategy is to avoid defining a $\mathtt{true}$ operator and instead take the dependence graph as given, "in the same way that the relevant causal structure is given as an input to CDT." It calls how to infer subjunctive structure from observation "perhaps the largest open problem."

## 4. How to apply A-FDT

The paper does not give a general procedure for constructing $G$, so I offer a working recipe. This is my own operationalization.

1. List the variables and their deterministic or stochastic relations.
2. Identify every process that computes or models the agent's decision function: twins, predictors, simulators, and the agent's own later or earlier selves where relevant.
3. Draw the node $\textsc{fdt}(\ldots,x)$ with edges into the agent's action and into each such process. Do not draw edges to merely correlated variables, such as a common-cause lesion.
4. If observations vary, include one node per observation value. A node earlier in the graph, such as the prediction, selects which of them controls the act.
5. For each action $a$, set the node to $a$, propagate along the edges, hold the rest fixed, and compute expected utility. Take the argmax.

A test for step 3: if the process would behave differently had the algorithm produced a different output, add an edge. If it would not, as with a lesion, do not.

## 5. Worked examples

Dollar figures are the paper's.

**Newcomb's problem.** Fiona (the paper's name for the agent following Equation (4)) intervenes on $\textsc{fdt}(\underline{P^F},\underline{G^F})$, which feeds both $\textsc{Act}$ and $\textsc{Prediction}$. Setting the node to *onebox* makes the box full with probability 0.99, giving EU $\approx\$990{,}000$. Setting it to *twobox* makes the box full with probability 0.01, giving $\approx\$11{,}000$. So she one-boxes. No retrocausality is invoked. She simply refuses to imagine her action changing while the predictor's model of her stays fixed.

**Smoking lesion.** The graph differs. The lesion is a common cause of the act and of cancer, and it determines which of two procedures, $\mathrm{FDT}(P_S,G)$ or $\mathrm{FDT}(P_R,G)$, controls the act. Intervening on the procedure leaves $P(\text{lesion})=p$ unchanged. Smoking beats refraining by $p\cdot\$1{,}000$, so she smokes. One rule yields one-boxing and smoking, because the graphs encode different dependencies.

**Transparent Newcomb and Parfit's hitchhiker.** Fiona sees a full box. She intervenes on $\textsc{fdt}(\ldots,\textit{full})$. Setting it to *twobox* makes the prediction probably *empty*, so the control passes to $\textsc{fdt}(\ldots,\textit{empty})$ and she probably gets $\$1{,}000$. Taking $q$ as her credence that she two-boxes on seeing an empty box, EU(onebox) $=\$990{,}000+0.01q\cdot\$1{,}000$ and EU(twobox) $=\$10{,}000+q\cdot\$990$ (the source prints "\$110,00", which looks like a typo, since $0.01\times\$1{,}001{,}000=\$10{,}010$). One-boxing wins. Paying the hitchhiker is the same structure.

**Blackmail.** Take the mechanical blackmail. If she pays on receiving the letter, she is blackmailed with probability near 1 and loses \$1,000. If she refuses, she is blackmailed with probability near 0. With a blackmailer who errs with probability $\epsilon$, refusing costs $\epsilon\cdot\$1{,}000{,}000$ in expectation. The paper's numbers are $\epsilon=0.0009$, giving \$900 against \$1,000, so she refuses. At $\epsilon=0.00011$ the cost of refusing is \$110, which the paper uses to say she then pays. That figure does not follow from the problem as stated. I read it as a loose break-even claim: the threshold under this arithmetic is $\epsilon=0.001$, and the paper's own stated 0.011% is below it, which would imply refusing, not paying. The source is therefore inconsistent here, and the principle (compare expected utility across the two hypotheticals) is what to rely on.

**XOR blackmail and Death in Damascus.** In both the infestation or the destination is not downstream of her algorithm's output, but the letter or Death's book is. A-FDT therefore refuses to pay in XOR blackmail, and it stays in Damascus because "wherever she goes, Death will be." CDT is unstable here, and EDT pays.

**Voting and gym.** In the paper's voting problem, ten agents run the same function and A-FDT agents vote. In the gym problem, her future selves run a similar function, so she goes. These are brief illustrations in the source, not worked derivations.

## 6. Relation to CDT and EDT

Where all correlations between action and other variables are caused by the action, the three theories agree. The paper writes this as $\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)]$. They diverge when correlations are not caused by the action. The paper summarizes: EDT respects too many action–environment correlations, CDT too few, and A-FDT "gets the balance right."

The paper also argues that dominance reasoning is not neutral, because every method of constructing hypotheticals has its own dominance notion. It argues that A-FDT never takes an action dominated in its own sense. It further argues that the right criterion is utility achieved, and that A-FDT is reflectively stable in fair problems.

## 7. What the source leaves open

1. **Constructing $G$.** Equation (4) works only given a graph; the paper has no method for deriving one. My recipe above is heuristic, and the source says it is unclear whether Pearl's framework can do this satisfactorily at all.
2. **Counterpossibles.** Whether a $\mathtt{true}$-style operator exists is unresolved. Footnote 9 says an evidential variant is hoped for but undefined.
3. **Fairness.** The paper's claim that A-FDT does best on "fair" problems (those where the outcome depends only on the agent's behavior in the dilemma at hand) is informal. It admits there is no formal criterion, and gives a counterexample showing the notion is hard to make precise: a problem that punishes copying Fiona's action is unfair to her.
4. **Actions versus policies.** Footnotes 7 and 16 say the preferred formalization iterates over policies, mapping observations to actions, and that this matters in multi-agent cases. Equation (4) as written takes the action for the actual observation. My view is that the observation-indexed nodes already encode much of the policy structure in single-agent problems, but the source does not establish equivalence in general.
5. **Hybrid dependence and uncertainty.** If the predictor is imperfect, the paper gives probabilistic edges, as in the 0.99 accuracy. It does not say how to weight uncertainty about the graph itself. A natural proposal, which is mine and not the paper's, is to average the computed EU over candidate graphs weighted by credence, though that is not obviously what the theory prescribes.

## 8. Philosophical motivation and objections

The paper's central argument is utility: the agent following the rule ends up richer in fair problems. It also argues that precommitment and value-of-information considerations support the same behavior. The theory acts as one would have precommitted to act, and never assigns negative expected value to information.

To the charge that A-FDT agents believe in controlling the past or mathematics, the paper replies that the charge applies equally to deterministic CDT agents "controlling" their action token. Both imagine counter-to-fact worlds for decision purposes. The paper claims no particular metaphysics of free will.

## 9. Conclusion

A-FDT, as defined by Equation (4), is expected-utility maximization with counterfactuals formed by intervening on the output of the agent's own decision function. It propagates that change through a graph of subjunctive dependencies: predictors, twins and copies move, while lesions and coincidences stay put. The result recovers one-boxing, smoking, paying the hitchhiker and refusing blackmail from one rule. The main limitation is that the dependency graph must be supplied, and no principled account yet exists of how to learn it. Anyone using A-FDT on a new case should treat the drawing of that graph as the central modeling decision, and should state what they assume about it.