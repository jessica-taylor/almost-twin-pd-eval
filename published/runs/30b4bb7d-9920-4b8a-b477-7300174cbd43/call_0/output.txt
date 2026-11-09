# A-FDT: Choosing by Intervening on One's Own Decision Function

## 1. The idea

A-FDT is the decision theory given by Equation (4) of Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." This essay uses "A-FDT" for that equation and the procedure around it. The paper itself writes "FDT" and mentions a policy-based variant, which I call P-FDT where I discuss it. I mark my own proposals as such.

The paper's slogan is that the agent treats her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" A-FDT is a decision rule of the same expected-utility form as causal decision theory (CDT) and evidential decision theory (EDT). It differs only in how it builds the hypothetical for each action.

## 2. The formal definition

All three theories maximize

$$\mathcal{EU}(a)=\sum_j P(a\hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

where $\hookrightarrow$ is the connective for decision hypotheticals. Following Joyce, the paper says the theories disagree about the "epistemic perspective", that is, about how to read $\hookrightarrow$.

- **EDT** (Eq. 2) reads it as conditioning: $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$.
- **CDT** (Eq. 3) reads it as Pearl's intervention on the physical act: $\arg\max_a\mathbb E(V\mid \mathrm{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$.
- **A-FDT** (Eq. 4) is

$$\text{A-FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V\;\Big|\;\mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The inputs are:

- $P$, a probability distribution over variables, including variables for the outputs of mathematical functions. One such variable might represent $6288+1048$ and put nearly all its mass on $7336$.
- $G$, a graph describing how changing a variable, *including a logical one*, propagates to the other variables. It encodes "the logical, mathematical, computational, causal, etc. structure of the world."
- $x$, the observation history.

The underlined symbols are dequoted names. The node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ represents the output of the A-FDT algorithm itself when run on exactly these inputs. This self-reference is harmless. The agent need not know the value of the node in order to have a variable representing it, and Kleene's second recursion theorem ("quining") shows how a structure can contain an accurate representation of itself.

The paper names two differences from CDT.

1. A-FDT intervenes on the node for the decision function's output, not on the physical act. In Peirce's terms, CDT intervenes on the token and A-FDT on the type.
2. A-FDT does not respond to observations by conditioning. It responds by changing which node it intervenes on, from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$.

## 3. Subjunctive dependence

The governing slogan is "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." Two systems subjunctively depend on a function when both compute it, as with two calculators summing the same numbers, or a predictor holding an accurate model of the agent. Three facts about this relation matter.

- Causal dependence is a special case. A scribe copying a calculator's output depends on it both causally and subjunctively.
- Mere statistical correlation does not suffice. Two calculators that happen to be pink are not subjunctively linked.
- The relation is graded. An imperfect predictor, or a stochastic agent, weakens it without eliminating it.

The agent's hypotheticals therefore change "all and only those things that subjunctively depend on the output of her decision-making procedure," and everything else is held fixed. The graph $G$ encodes exactly this.

## 4. The procedure

1. Build $(P,G)$ for the problem, containing the node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ for the actual observation.
2. For each action $a$, form the hypothetical by setting that node to $a$ and propagating along $G$.
3. Compute $\mathbb E[V]$ in each hypothetical.
4. Output the maximizer.

Observation enters only by selecting the node. An agent who sees different things is running a differently-indexed instance of the function. In the hypothetical, the agent's observations may therefore differ from the actual ones.

## 5. Worked examples

**Newcomb's problem.** The paper's model has $\mathrm{fdt}$ as a parent of both Act and Prediction, with Prediction feeding Box B. The setup includes a 99% accuracy variable.

- $\mathrm{do}(\mathrm{fdt}=\text{onebox})$ gives $0.99\cdot 10^6=\$990{,}000$.
- $\mathrm{do}(\mathrm{fdt}=\text{twobox})$ gives $0.01\cdot 1{,}001{,}000+0.99\cdot 1000=\$11{,}000$ (the paper's figure; it is $\$11{,}000$).

A-FDT one-boxes. It posits no retrocausation. It merely refuses to imagine the function's output changing while the predictor's model of that function stays fixed.

**Smoking lesion.** Here Cancer is a child of Lesion and Luck, not of the decision function. Intervening on the function moves Act but not Cancer, so smoking gains $p\cdot\$1000$ and A-FDT smokes. One rule thus one-boxes and smokes. The graph differs between the two problems, and the paper stresses that it must differ. The paper formalizes the lesion's effect on the agent's desires by giving the agent two possible utility functions and hence two function-nodes. It admits this makes the problem contrived.

**Transparent Newcomb and Parfit's hitchhiker.** The agent sees a full box. The A-FDT node is $\mathrm{fdt}(\underline P,\underline G,\text{full})$. Setting it to *twobox* makes the predictor, who simulates that very node, leave the box empty with probability 0.99. The agent then actually runs the "empty" node. The paper computes $\$990{,}000+0.01q\cdot 1000$ for one-boxing against $\$110{,}000+q\cdot 990$ for two-boxing. (The paper prints "\$110,00"; $0.01\cdot 1{,}001{,}000=\$10{,}010$, so the second expression as printed appears to contain slips. The ordering is not in doubt.) A-FDT one-boxes and, by the same structure, pays the hitchhiker.

**Blackmail.** In mechanical blackmail the node $\mathrm{fdt}(\ldots,\text{blackmail})$ feeds the blackmailer's decision. Setting it to *refuse* leads to a hypothetical in which no letter was sent. A-FDT refuses even while holding the letter. With a predictor erring with probability $0.0009$, paying costs $\$1000$ for certain while refusing costs $0.0009\cdot\$1{,}000{,}000=\$900$ in expectation, so it still refuses. At $0.00011$ the expected cost of refusing is $\$110$, and it pays. In XOR blackmail the node feeds the letter's existence but not the infestation, so A-FDT refuses.

**Death in Damascus.** Death's book depends on the function's output, so wherever A-FDT goes, Death goes. It stays and saves the \$1000. CDT, by contrast, cycles or ratifies.

**Agreement cases.** When all correlations between Act and the world are causal, the three equations coincide. They diverge only when predictors, twins or copies create non-causal links.

## 6. Why the construction is defensible

The paper argues from utility. Predictors who read the algorithm give CDT and EDT agents empty boxes, so followers of A-FDT do better in expectation. Three supporting points:

- **Reflective stability.** A-FDT "always acts as it would have precommitted to act," so it needs no costly binding and has no reason to self-modify.
- **Value of information.** Observation changes only which node is used, so information never hurts in the way it can for EDT. This is the source of the name "updateless."
- **Dominance.** CDT's dominance argument presupposes CDT counterfactuals. A-FDT has its own notion: "holding constant all relevant subjunctive dependencies," it never takes a dominated action. The paper concludes that dominance cannot adjudicate between theories.

On the charge that A-FDT imagines impossibilities, the reply is parity. A deterministic CDT agent imagines a physical act that would not occur, and A-FDT imagines a function output that would not occur. CDT imagines a perfect predictor erring, and A-FDT imagines the agent seeing different observations. Neither "control" claim is more metaphysical than the other.

## 7. What the source leaves open, and how to proceed

**The graph is an input.** The paper says plainly that deducing the structure of subjunctive dependence "is perhaps the largest open problem" and that Equation (4) "works *given* a graph." There is no Pearl-style discovery theory for logical dependence. It also notes that a genuine $\mathrm{true}(\cdot)$ operator for counterpossible conditioning is not defined. Equation (4) sidesteps this by reusing $\mathrm{do}$ on a supplied graph. Everything below is my own operational suggestion, not the paper's.

*A usable test.* To decide whether variable $Z$ is a descendant of the function node, ask whether $Z$'s value is fixed by a process that computes, or accurately models, this algorithm on this input.

- A predictor who simulates the agent, a twin, or a mind-reader passes the test.
- A lesion, a coincidence of colors, or a correlation produced by a common cause does not.

Because the question is whether the process tracks the output, reliability should enter as a graded edge: a predictor with accuracy $\alpha$ copies the output with probability $\alpha$. The 99% and 0.0009 calculations above are this recipe applied. Two cases are more delicate:

- If a predictor reads the agent's *procedure* but not its output, the paper calls the problem unfair, and the test may misclassify it.
- If a predictor's reliability rests on a common cause that the agent could break, the dependence is arguably only statistical. The agent must then decide how her own algorithm would change the cause.

**Observation nodes.** Each possible observation gets its own node, and the graph must say which node governs Act given the realized world. In the transparent problem, Prediction selects between $\mathrm{fdt}(\ldots,\text{full})$ and $\mathrm{fdt}(\ldots,\text{empty})$. Unobserved nodes need priors over how the agent would act in cases she does not face. The paper notes this uncertainty ($q$) is harmless in its examples.

**Actions versus policies.** The paper's footnotes say the authors' preferred formalization intervenes on a *policy* mapping observations to actions, and that this matters only in some multi-agent problems. Equation (4) as written is the action version. If you must decide a multi-agent case, the paper gives no more than this hint. My own suggestion is to compare the two versions and flag any divergence.

**Fairness.** The paper claims A-FDT does best on "fair" problems, where outcomes depend on the agent's behavior and not directly on her algorithm, but admits no formal criterion exists. It also gives a copy-punishing counterexample showing that fairness is relative to the theory being tested. Treat the claim of optimality as conjecture.

**Complexity.** The idealized equations are intractable for realistic models, and the authors only conjecture that bounded approximations would keep the same qualitative behavior.

## 8. Conclusion

A-FDT keeps expected-utility maximization and Pearl-style surgery, and changes two things: the node it intervenes on and the way it reacts to observation. It intervenes on the output of its own decision function, and it handles evidence by switching nodes, not by conditioning. Its verdicts (one-box, smoke, pay the hitchhiker, refuse blackmail, stay in Damascus) come from one rule applied to different dependency graphs. Its weak point is acknowledged in the source: the graphs are supplied, not derived. For unfamiliar cases the practical advice is to draw $G$ by asking which variables track the agent's algorithm, to intervene on that node for the observation actually received, and to compare expected utilities.