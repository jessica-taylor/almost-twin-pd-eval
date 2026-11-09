# A-FDT: Choosing by Intervening on the Decision Function

## 1. The idea

Action functional decision theory (A-FDT) is the theory given by Equation (4) of Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." I use "A-FDT" for that equation. Its guiding question, in the paper's words, is "Which output of this very function would yield the best outcome?" The agent does not ask which physical act of hers would cause the best outcome (the causal decision theory question), nor which act would be the best news (the evidential decision theory question).

I will separate three things: what the paper states, what follows from it, and what I add. Additions are marked **[mine]**.

## 2. The formal definition

All three theories maximize expected utility,

$$\mathcal{EU}(a)=\sum_j P(a\hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

and differ in how the connective "$\hookrightarrow$" is read. The agent holds a world-model $M$ and builds for each action a "hypothetical" $M^{a\hookrightarrow}$ from it. EDT conditions: $\mathrm{EDT}(P,x)=\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$. CDT intervenes on the physical act in a causal graph $G$: $\mathrm{CDT}(P,G,x)=\arg\max_a\mathbb E(V\mid \mathrm{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$.

Equation (4) defines A-FDT:

$$\mathrm{FDT}(P,G,x):=\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V\ \Big|\ \mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The inputs are:

- $P$, a probability distribution that includes variables for the outputs of mathematical functions. It has, for example, a variable for $6288+1048$ concentrated on $7336$.
- $G$, a graph of "logical, mathematical, computational, causal, etc." structure. It says how changing a logical variable changes the other variables.
- $x$, the observation history.

The underlines denote dequoting. $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a node of the model standing for the output of this very procedure on these very inputs. The self-reference is harmless: the agent need not know the node's value to have a variable representing it, and Kleene's recursion theorem ("quining") shows such self-representing structures can be built.

The paper names two differences from CDT:

1. The surgery is on the node for the decision function's output, not on a node for the physical act.
2. Observation does not condition the distribution. It changes which node is intervened on: $\mathrm{fdt}(\underline P,\underline G,\underline x)$ becomes $\mathrm{fdt}(\underline P,\underline G,\underline y)$ when the observations change from $x$ to $y$.

A-FDT is therefore updateless in flavor. The paper says its early ancestor, Dai's Updateless Decision Theory, took its name from this, and that Timeless Decision Theory both conditioned and moved the intervention point, a "double update" the authors say is harmful.

The paper's footnotes state a preferred formalization that intervenes on policies (maps from observations to actions). It says this matters only in some multi-agent problems and sets it aside. Equation (4) as written is per-observation.

## 3. Reading the equation operationally

To evaluate $\mathrm{FDT}(P,G,x)$:

1. Locate the node $F_x=\mathrm{fdt}(\underline P,\underline G,\underline x)$.
2. For each action $a$, set $F_x=a$ with $\mathrm{do}$. Follow arrows out of $F_x$ and recompute everything downstream. Leave the rest alone.
3. Compute $\mathbb E[V]$ in each resulting model and output the best $a$.

Downstream of $F_x$ are the agent's own act, every predictor or copy that models the agent, and anything those affect. Upstream-independent facts, such as whether a lesion exists or whether a house has termites, are untouched.

The paper's slogan is: FDT is to subjunctive dependence as CDT is to causal dependence. Causal dependence is a special case of subjunctive dependence. Merely statistical correlation, like two calculators that happen to be pink, is not subjunctive dependence. So in the paper's phrase, A-FDT preserves "all decision-relevant subjunctive dependencies," where CDT preserves too few correlations and EDT too many.

When all correlations with the act are caused by the act, the three coincide:
$\mathbb E[V\mid a]=\mathbb E[V\mid \mathrm{do}(a)]=\mathbb E[V\mid \mathrm{do}(\mathrm{fdt}=a)]$.

## 4. Worked examples

**Newcomb's problem.** The paper's graph $G^F$ has $\mathrm{fdt}(P,G)$ pointing to both Act and Prediction. With accuracy 0.99, $\mathrm{do}(\mathrm{fdt}=\textit{onebox})$ gives Act=onebox and a full box with probability 0.99, so expected utility is \$990,000. $\mathrm{do}(\mathrm{fdt}=\textit{twobox})$ gives full-box probability 0.01, so expected utility is \$11,000. A-FDT one-boxes. The justification involves no retrocausation. The agent simply regards it as incoherent to imagine her act changing while the predictor's model of her does not.

**Smoking lesion.** The graph differs. The lesion is not downstream of the decision function; it causes the preference, which determines which of two function instances runs. Intervening on the node changes the act but leaves $P(\text{lesion})=p$ and the cancer probability fixed. Smoking beats abstaining by $p\cdot\$1000$ in the paper's calculation, so A-FDT smokes. The same equation therefore one-boxes and smokes. The only difference is the dependency structure fed in. The paper itself calls the lesion problem contrived and recommends abandoning it.

**Transparent Newcomb and Parfit's hitchhiker.** Here observations matter. For an agent who sees a full box, the intervention node is $\mathrm{fdt}(P,G,\textit{full})$. That node feeds the prediction, and the prediction determines whether the observation is "full" or "empty," so setting it to *twobox* makes the empty-box world likely. With accuracy 0.99 and $q$ the agent's credence that she two-boxes on seeing an empty box, the paper gets $\approx\$990{,}000+0.01q\cdot\$1000$ for one-boxing and $\$11{,}000+q\cdot\$990$ for two-boxing. A-FDT one-boxes even with a full box in view, and this is the same structure as paying the driver in the hitchhiker problem. The paper defends this by three arguments: the agent would endorse precommitment, information never has negative value for her, and she ends up richer.

**XOR blackmail.** EDT pays, because conditioning on paying implies no termites. CDT and A-FDT both refuse, for different reasons. For A-FDT, intervening on $\mathrm{fdt}(\ldots,\textit{letter})$ changes whether the letter is sent but not whether termites exist.

**Mechanical blackmail.** Intervening on "refuse" makes the blackmailer not run the program, so no letter exists in that hypothetical. Fiona (the paper's A-FDT agent) refuses while holding the letter. If the predictor errs with probability 0.0009, refusing costs \$900 in expectation, versus a certain \$1000 for paying, so she still refuses. At error 0.011% she pays. The paper says this is because the policy decision, not the actual-world payoff, is what is being compared.

**Death in Damascus.** Death's book entry depends on the decision function. Staying costs \$0 and fleeing costs \$1000, and survival is lost either way, so A-FDT stays. CDT oscillates, and the paper argues it will even refuse a \$1 truly random coin worth a 50% chance of survival.

**Coordination.** A group of agents running the same function treats their choices as subjunctively dependent, and so can vote or cooperate (the twin prisoner's dilemma). One agent across time can treat today's and next week's gym decisions as the same function.

## 5. Philosophical motivation

The paper makes three points.

*Utility.* Agents who follow the rule get richer in fair problems. A problem is fair if it rewards actions, including predicted actions, and not the decision procedure as such. Newcomb's predictor "punishes two-boxers," not rational agents. The paper admits it has no formal definition of fairness, and its footnote 15 shows a difficulty: a problem that punishes copies of Fiona's action is unfair to her.

*Dominance.* Every method of building hypotheticals induces its own dominance principle. Holding the prediction fixed while varying the act is, for the paper, the same as imagining a calculator outputting 3159 while $6288+1048=7336$. It restates CDT rather than giving independent support. A-FDT has its own dominance principle, under which one-boxing is not dominated.

*Control.* Critics say A-FDT "controls" mathematical facts. The paper replies that a deterministic CDT agent equally "controls" a physical act she cannot truly vary. Both imagine counter-to-fact scenarios, so the charge applies symmetrically.

## 6. What the source leaves open

The paper is explicit that Equation (4) "rests on shakier philosophical foundations" than CDT's. Three gaps follow.

1. **No theory of constructing $G$.** The paper says deducing the structure of subjunctive dependencies "from observation and experiment" is "perhaps the largest open problem." Equation (4) works only given $G$, which is an input.
2. **No $\mathtt{true}$ operator.** It is unclear how to condition on a logical falsehood. The paper sidesteps this by encoding dependence in a graph and reusing Pearl's do. It also hopes an evidential version, conditioning on $\mathrm{fdt}=a$, might eventually exist.
3. **Counterpossibles.** Setting a deterministic function to a non-actual output is impossible. The paper argues the difficulty is technical, since humans reason about uncertain logical claims, and that the agent only needs narrow questions such as how a predictor's output would change.

**Operational heuristics [mine].** These are not in the paper. They are my way of deciding unfamiliar cases.

- *Dependence test.* Ask whether the thing would differ if the agent's decision procedure, run on this input, returned something else. Predictors, simulations, and agents that reason about her or share her code do. Common-cause correlates such as lesions and the pink calculator do not. When in doubt, ask whether the other system is evaluating the same function or a model of it, or is merely correlated.
- *Imperfect dependence.* Use probabilistic edges, such as the paper's accuracy variable. This is how the 0.99 and 0.0009 figures arise.
- *Policy form.* For problems with multiple observation branches, compute the value of each policy across all branches, weighted by how the policy influences which branch occurs. The per-observation equation agrees with this in the paper's examples, and the paper's footnotes suggest policies as the preferred form.
- *Unknown graph.* Report A-FDT's verdict conditional on the assumed graph and test sensitivity to it, since the main risk is a mis-specified $G$.
- *Caveat.* If a problem punishes agents for their algorithm itself, or if the graph is wrong, no verdict is guaranteed. The paper concedes that no decision theory wins everywhere.

## 7. Conclusion

A-FDT keeps expected-utility maximization and changes only the epistemic perspective: surgery on the output of one's own decision function, with observations selecting which output node is intervened on. This puts correlations from predictors, copies, and common reasoning into the agent's imagined worlds and excludes mere statistical coincidence. The paper claims that this one rule one-boxes and smokes, pays the hitchhiker, refuses blackmail, and stays in Damascus. Its main limitation is that the dependency graph must be supplied, and no principled method for obtaining it yet exists.