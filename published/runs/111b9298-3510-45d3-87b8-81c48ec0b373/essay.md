# A-FDT: Deciding by Intervening on One's Own Decision Function

## 1. The idea

Action functional decision theory (A-FDT) is the version of functional decision theory in which the agent chooses among *actions*. The source (Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality") presents it in Equation (4), Section 5. Its footnotes say the authors' preferred formalization iterates over *policies*, that is, maps from observations to actions. They set that aside because it matters only in some multi-agent problems. This essay follows the action version of Equation (4).

The core claim is that the agent should treat her decision as the output of a fixed mathematical function. She should ask: "Which output of this very function would yield the best outcome?" The question is not "which physical act of mine causes the best outcome" (CDT) or "which act would be the best news" (EDT).

## 2. The formal definition

All three theories maximize expected utility,

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

where "$\hookrightarrow$" is a decision-hypothetical connective. Following Joyce, the theories differ only in the "epistemic perspective", meaning how that connective is read. Writing $V=\mathcal U(\text{Outcome})$:

- EDT (Eq. 2): $\arg\max_a \mathbb E(V\mid \text{Obs}=x,\text{Act}=a)$.
- CDT (Eq. 3): $\arg\max_a \mathbb E(V\mid do(\text{Act}=a),\text{Obs}=x)$.
- A-FDT (Eq. 4):

$$\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; do\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The ingredients are as follows.

- $P$ is a probability distribution over the agent's model variables, including variables for the outputs of mathematical functions. For example, there is a variable for $6288+1048$ that puts nearly all its mass on 7336.
- $G$ is a graph encoding how changing a variable propagates to the others. It covers *logical, mathematical, computational, causal* dependencies, not only causal ones.
- $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a variable in the model representing the output of the A-FDT procedure itself on inputs $(P,G,x)$. The underlines denote dequoting, so the variable's name depends on the model. This self-reference is harmless. The agent need not know the *value* of the output to have a variable *representing* it, and Kleene's recursion theorem (quining) shows such self-representation can be built.
- $do$ is Pearl's surgery operator, re-used. Set the node to $a$, then recompute everything downstream of it in $G$ and leave everything else fixed.

So the procedure is: for each $a$, construct a hypothetical by surgery on the *logical* node, compute expected utility, and output the argmax.

## 3. Two differences from CDT

1. **Where the surgery happens.** CDT intervenes on the token "my act is $a$", a physical fact. A-FDT intervenes on the type, "this function outputs $a$". Whatever subjunctively depends on that output changes too: the agent's body, a twin's choice, a predictor's model of her.
2. **How observation enters.** CDT conditions on $\text{Obs}=x$. A-FDT does not condition. It changes *which node* it intervenes on, $\mathrm{fdt}(\ldots,x)$ versus $\mathrm{fdt}(\ldots,y)$. Observations are inputs to the function, not evidence that restricts the hypotheticals. This is why A-FDT can imagine, while holding a letter, a world where it never received the letter. Different outputs on different inputs make the observation itself vary across hypotheticals when the observation depends on the prediction.

When every correlation between action and world is caused by the action (apart from the logical node), the three equations coincide. They separate only when something correlates with the action without being caused by it, such as a predictor or twin.

## 4. Subjunctive dependence

Two physical systems that compute the same function subjunctively depend on it. Two calculators computing $6288+1048$ are constrained to agree, and a predictor's model of an agent is a "twin" of the agent. The source gives three marks of this relation:

- Causal dependence is a special case of it. A scribe copying a calculator's output depends on the calculator subjunctively as well.
- Mere statistical correlation is not subjunctive dependence. Two pink calculators are not linked. A lesion correlated with smoking is not linked either.
- Imperfect predictors weaken the dependence without eliminating it, and the probabilities in $P$ and $G$ carry the strength.

The source stresses that A-FDT's hypotheticals are "counterpossible", because a deterministic function has only one output. It argues this is a technical problem, not a philosophical one. Humans reason under logical uncertainty, and A-FDT only needs questions of the form "how would this predictor's prediction change if my algorithm output something else?"

## 5. What the source leaves open

The paper is explicit that the dependency graph $G$ is an *input*. It says that deducing the structure of subjunctive dependence from observation is "perhaps the largest open problem" for FDT. It also says there is no formal $\mathtt{true}(\cdot)$ operator for conditioning on false logical sentences. The paper concedes that Equation (4) "rests on shakier philosophical foundations" than the CDT equation.

*My operational reading* (an assumption, not in the source): to apply A-FDT to an unfamiliar case, ask for each variable whether it is a function of the agent's algorithm. This includes any model of her inside a predictor, any copy of her, and her own future self facing a relevantly identical choice. Wire an arrow from the logical node to exactly those variables. Fairly reliable predictors give stochastic arrows, with noise nodes like "Accurate". Variables that merely correlate with the agent's action through a common cause get no arrow from the logical node. The result is only as good as this wiring, and different modelers can wire differently.

## 6. Worked examples

**Newcomb's problem.** The nodes are $\mathrm{fdt}$, Act, Prediction (also depending on Accurate, with probability 0.99), Box B, and V. The node $\mathrm{fdt}$ feeds both Act and Prediction.

- $do(\mathrm{fdt}=\text{onebox})$: Act is onebox, and Box B is full with probability 0.99. Expected utility is \$990,000.
- $do(\mathrm{fdt}=\text{twobox})$: Box B is full with probability 0.01. Expected utility is \$11,000.

So A-FDT one-boxes. No retrocausation is involved. The agent simply declines to imagine her output changing while the predictor's model of that output stays fixed. CDT's Do(Act) leaves the prediction untouched, so two-boxing wins by \$1,000 for every $p$.

**Smoking lesion.** Here the graph differs, so the Newcomb graph cannot be reused. Lesion is not a function of the decision procedure and has no arrow from the logical node. In the source's formalization, the agent is uncertain whether she runs the procedure with utility $\mathcal U_S$ or $\mathcal U_R$, depending on whether she has the lesion. Intervening on her node leaves $P(\text{lesion})=p$ unchanged. Smoking is then better by $p\cdot\$1000$, and she smokes. This shows one rule giving one-boxing and smoking, with the difference carried entirely by $G$. The source admits the formalization is contrived and recommends abandoning the problem.

**Transparent Newcomb and Parfit's hitchhiker.** Observation changes the intervention node. Let $q$ be her credence that she two-boxes on seeing an empty box. Facing a full box, she evaluates $do(\mathrm{fdt}(\ldots,\text{full})=a)$. If this output is onebox and the predictor is accurate, the box is full and she takes one box. If the output is twobox, then in the accurate case the box would have been *empty*, and the agent would instead be running $\mathrm{fdt}(\ldots,\text{empty})$. Expected utilities are $990{,}000+0.01q\cdot 1000$ for one-boxing and $\approx 11{,}000+990q$ for two-boxing. She one-boxes even while looking at a full box. This is isomorphic to paying the driver in Parfit's hitchhiker. The source argues that FDT therefore acts as if it had precommitted without needing a precommitment device.

**Blackmail.** In the mechanical blackmail, paying makes her blackmailed with probability about 1 and costs \$1,000. Refusing makes her blackmailed with probability about 0. She refuses even holding the letter. For a blackmailer with error rate $\epsilon$, refusing costs about $\epsilon\cdot\$1{,}000{,}000$ against \$1,000 for paying. The source's figures give a threshold between 0.0009 (refuse) and 0.00011 (pay). In XOR blackmail, the letter changes whether she sees it, but not whether she has termites, so she refuses.

**Death in Damascus.** Death's book is a function of her decision procedure. Staying in Damascus costs nothing, and fleeing costs \$1,000. A-FDT stays, whereas CDT's instability arises from holding Death's location fixed under intervention.

**Cosmic ray.** The agent takes the \$100. She does not treat "I only take \$100 when hit by a ray" as a dependence to preserve, because it is merely statistical.

## 7. Why this rule? The source's arguments

- *Utility achieved.* The primary argument is that A-FDT agents do better in "fair" problems. Fairness here means outcomes depend on the agent's behavior in the problem, not on which decision procedure she runs. The source concedes that no formal definition of fairness exists and that unfair problems can defeat any theory.
- *Dominance.* The source argues that every hypothetical-construction method defines its own dominance. A-FDT has one, and under it two-boxing is dominated. Dominance therefore cannot adjudicate between theories neutrally.
- *Counterfactual honesty.* The source says CDT agents imagine perfect predictors erring exactly when they choose, while A-FDT's hypotheticals respect the predictor's accuracy. EDT conditions on too many correlations, CDT respects too few, and A-FDT keeps those that are logical or causal.
- *No delusion.* The source argues that A-FDT's "control" of a decision type is no more problematic than CDT's talk of choosing among physical acts in a deterministic world.

## 8. Claims versus my additions

From the source: Equation (4), the node-switching treatment of observation, the examples above with their numbers, the open problems, and the policy-versus-action footnote. My additions are the practical wiring heuristic in Section 5, and the reminder that results depend on how the modeler draws $G$. The paper itself acknowledges that issue. One further limitation: the evaluation is idealized, and the paper expects bounded agents only to approximate it.

## 9. Conclusion

A-FDT keeps the expected-utility form and Pearl's surgery, and moves the intervention from the physical act to the logical output of the agent's own decision procedure. Observations select which output node is intervened on. This yields one-boxing, paying in Parfit's problem, and refusing blackmail, while smoking in the lesion case, from a single rule. Its practical reliability depends on a dependency graph that the source does not tell us how to derive. That is the central unresolved problem.