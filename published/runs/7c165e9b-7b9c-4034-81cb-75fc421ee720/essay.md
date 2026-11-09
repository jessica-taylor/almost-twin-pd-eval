# A-FDT: Choosing Actions by Intervening on Your Decision Function

## 1. Scope and naming

This essay explains the decision theory that I call **A-FDT** (action functional decision theory). The source paper, Yudkowsky and Soares's *Functional Decision Theory: A New Theory of Instrumental Rationality*, calls its theory "FDT". I use "A-FDT" for the specific procedure in the paper's **Equation (4), Section 5**. That procedure selects an *action* by intervening on a node that represents the output of the agent's decision function. I read the "A" as marking this contrast with the policy-selecting variant that the authors say they prefer (footnotes 7 and 16). Other theories are named separately: CDT (causal), EDT (evidential), and the paper's variants FDT$'$, "Updateless Decision Theory", and "Timeless Decision Theory".

I will separate three kinds of claim:

- **[Source]**: what the paper states or computes.
- **[Mine]**: my gloss, extension, or correction.
- **[Open]**: what the paper explicitly leaves undetermined.

## 2. The shared template: expected utility with a hypothetical connective

All three theories (EDT, CDT, A-FDT) are, in the paper's words, expected utility theories. They choose the action $a \in \mathcal A$ maximizing

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j) \tag{1}$$

Here $x$ is the observation history and $\mathcal U$ is a bounded utility function. The connective "$\hookrightarrow$" marks a *decision hypothetical*. The paper follows Joyce in treating the theories as disagreeing "about the epistemic perspective from which actions are to be evaluated". They share the valuation machinery and differ in how "$a \hookrightarrow o$" is interpreted.

Operationally, an agent keeps a world-model $M$. For each action $a$ she builds a hypothetical $M^{a\hookrightarrow}$ from $M$. She then computes a value $V_a$ from it and takes the action with the highest value. The paper stresses that hypotheticals are "decision-theoretic instruments constructed from beliefs", like "notes on scratch paper", and not beliefs themselves. This matters for what follows. A-FDT does not ask the agent to *believe* anything exotic about causation. It asks her to *imagine* a particular family of scenarios.

The two predecessors are:

$$\mathrm{EDT}(P,x) = \arg\max_a \mathbb E[V \mid \mathrm{Obs}=x,\ \mathrm{Act}=a] \tag{2}$$

$$\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E[V \mid \mathrm{do}(\mathrm{Act}=a),\ \mathrm{Obs}=x] \tag{3}$$

EDT conditions. CDT performs Pearl-style surgery on a causal graph $G$. In Pearl's do-operator, everything causally downstream of the intervened variable is recomputed and everything else is left alone.

## 3. Equation (4)

A-FDT keeps the surgical form of CDT but changes *where* the surgery is applied and *how observations enter*:

$$\mathrm{A\text{-}FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big[V \,\Big|\, \mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x) = a\big)\Big] \tag{4}$$

The ingredients are:

1. **A probabilistic model $P$** over variables that include not only physical facts but also *logical* ones: "the value of $6288+1048$", or the output of some program. [Source]
2. **A graph $G$** that says how changing a logical variable affects all the other variables. The source says it must encode "the logical, mathematical, computational, causal, etc. structure of the world more broadly". [Source]
3. **A distinguished node $\mathrm{fdt}(\underline P,\underline G,\underline x)$**, representing the output of the very procedure being run, on inputs $(P,G,x)$. Underlines denote dequoting, so the node's name depends on the model that contains it.
4. **The do-operator**, reused from Pearl: set that node to $a$, propagate along $G$'s arrows, and leave the rest fixed.

Three features deserve emphasis.

**Self-reference is harmless.** The model contains a variable naming the output of the algorithm that consumes the model. The paper argues the agent need not know the *value* of $\mathrm{A\text{-}FDT}(P,G,x)$ in order to have a variable *representing* it. It invokes Kleene's second recursion theorem ("quining") to show that such self-representing data structures can be built. [Source] Footnote 12 warns against conflating the variable $\mathrm{fdt}(\underline P,\underline G)$, which the agent manipulates, with the action $\mathrm{A\text{-}FDT}(P,G)$ that results.

**Observation is handled by choosing which node to intervene on.** Equation (4) has no $\mathrm{Obs}=x$ conditioning term. The paper says: "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." Seeing $y$ instead of $x$ moves the intervention from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$. [Source] Since a different input yields a different node, and the observation can itself depend on what the function outputs on other inputs, hypotheticals can be ones in which the agent *saw something else*.

**The actual-world action is an effect, not the intervention point.** Because the intervention is on the function's output, the physical $\mathrm{Act}$ is a descendant of the intervened node. So are the prediction, the twin's move, and so on, whenever $G$ says they subjunctively depend on that output.

In summary: CDT intervenes on the *token* "my action is $a$", and A-FDT intervenes on the *type*, the output of the function that the agent's body, her twins, and her predictors all instantiate or model. The paper's slogan is "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." In well-behaved cases all three theories agree. If every correlation between $\mathrm{Act}$ and other variables is caused by $\mathrm{Act}$, then

$$\mathbb E[V\mid a] = \mathbb E[V\mid \mathrm{do}(a)] = \mathbb E[V\mid \mathrm{do}(\mathrm{fdt}=a)].$$

They come apart only when something correlates with the action without being caused by it.

## 4. Subjunctive dependence and the graph $G$

**Definition [Source].** When two physical systems compute the same function, their behaviors "subjunctively depend" on that function. Two calculators computing $6288+1048$ agree; if one displayed something else, a competent inference would say the other would too, modulo error. A predictor holding an accurate model of the agent is, in effect, a calculator running the agent's function. Causal dependence is a special case, since a scribe copying a calculator's output would write something different if it were different. Statistical correlation is *not* subjunctive dependence. Two coincidentally pink calculators are not linked: had one been green, the other would still be pink.

**Counterpossibles [Source].** If the function outputs *cooperate* on an input, it does so necessarily. Evaluating "what if it output *defect*?" is therefore a counterpossible, like "what if $6288+1048\neq 7336$?" The paper says the lack of a satisfactory account of counterpossibles is "the main drawback of FDT relative to CDT at this time". It argues the difficulty is "technical rather than philosophical". Mathematicians reason sensibly under logical uncertainty, and the agent need only answer narrow questions of the form "how would this predictor's prediction change if my algorithm's output were different?"

**Why Equation (4) sidesteps the problem [Source].** The paper first writes an idealized $\mathrm{FDT}^*$ using a $\mathtt{true}(\cdot)$ operator that conditions on logical sentences. It admits "it's not clear how to define a $\mathtt{true}$ operator". Its remedy is to demand that $G$ come as an *input*, as CDT demands a causal graph. Counterpossible reasoning is thereby outsourced to whoever supplies $G$. Footnote 9 is explicit that this is a stopgap, and that an evidential version conditioning on logical facts remains hoped-for but undefined.

**The paper's variant FDT$'$.** One might try to avoid counterpossibles by asking "what if I used a different decision function $f_n$?" The paper argues this fails. Any predictor of the true function $d$ would have to be imagined as predicting as if $d$ behaved like $f_n$, which is the same counterpossible again.

**[Open].** The paper says: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." It is not even clear whether this can be done within Pearl's framework. Equation (4) "works *given* a graph that accurately describes how changing the value of a logical variable affects other variables".

### A working recipe for constructing $G$ [Mine]

The paper says nothing definitive about construction, but its worked examples suggest a recipe. This is my systematization, not the authors' method.

1. **Find the instances and models.** List every process in the situation that either runs the agent's decision procedure (the agent's own controller, twins, copies) or contains a representation of it that determines behavior (a predictor's simulation, a driver's lie-detection, an adversary's reasoning about you).
2. **Introduce one function-output node per relevant input.** If the agent could receive several observations, make a node $\mathrm{fdt}(\underline P,\underline G,\underline{x_i})$ for each plausible $x_i$. Add edges so that whatever determines *which observation she gets* (often a predictor's output) determines which node controls $\mathrm{Act}$. Footnote 7's remark that the authors' preferred formalization intervenes on whole policies gives a natural check: the node for each input is a component of a single policy.
3. **Draw edges from these nodes to exactly the things that would change if the function's output changed, with physics held fixed.** Include the predictor's record, the twin's move, and the observations the agent would see. Represent imperfect fidelity with explicit noise variables, as the paper does with $\mathrm{Accurate}$.
4. **Omit edges for merely statistical links.** A common cause that does not *evaluate* the agent's decision gets no edge. The lesion is the example.
5. **Handle graph uncertainty by mixing.** If the agent is unsure whether a predictor models her function or only correlates with her disposition, she could compute the value under each candidate $G$ and weight by credence. The paper does not endorse this. It is my proposal, and it makes A-FDT's output depend on a prior over dependence structures, which the paper leaves unspecified.

The decisive diagnostic is the paper's own: ask whether the thing in question "evaluates" or models the agent's decision. A predictor does and a lesion does not.

## 5. A-FDT applied

### Newcomb's problem

The model has a stochastic $\mathrm{Accurate}$ node ($0.99$), $\mathrm{Prediction}$ and $\mathrm{Box\,B}$ as deterministic functions, and $\mathrm{Act}$. In Fiona's graph (the paper's A-FDT-agent), $\mathrm{fdt}(\underline P,\underline G)$ has arrows to both $\mathrm{Act}$ and $\mathrm{Prediction}$. Then:

- $\mathrm{do}(\mathrm{fdt}=\textit{onebox})$: the body one-boxes, and $P(\text{full})=0.99$. $\mathbb E[V] = 0.99\times 1{,}000{,}000 = \$990{,}000$.
- $\mathrm{do}(\mathrm{fdt}=\textit{twobox})$: $P(\text{full})=0.01$, so $\mathbb E[V] = 0.01\times 1{,}001{,}000 + 0.99\times 1{,}000 = \$11{,}000$.

So A-FDT one-boxes. Carl's graph has $\mathrm{Act}$ causally independent of $\mathrm{Box\,B}$. Whatever $p=P(\text{full})$ is, two-boxing gains $\$1{,}000$, so CDT two-boxes. Eve's conditioning gives one-boxing unless her prior on one-boxing is $0$ or $1$. (The paper reports Eve's one-box value as $\$999{,}000$. Given $P(\text{full}\mid\text{onebox})=0.99$ I get $\$990{,}000$, matching Fiona's figure.)

A frequent objection: Fiona is nearly certain the box is already full, so shouldn't she take both? The paper answers that her hypotheticals make "the FDT algorithm itself behave differently", and hence the box probably empty. She appeals to no retrocausal physics. She just thinks it foolish "to imagine her action changing without also imagining $\mathrm{FDT}(P^F,G^F)$ taking on a different value".

### Twin prisoner's dilemma

Both players' moves hang off the same node. $\mathrm{do}(\mathrm{fdt}=\textit{cooperate})$ gives $\$1{,}000{,}000$ and $\mathrm{do}(\mathrm{fdt}=\textit{defect})$ gives $\$1{,}000$. A-FDT cooperates, and the paper's point is that it does so by surgery, unlike EDT, which conditions.

### Smoking lesion

Here the graph must differ from Newcomb's. The paper's formalization has two utility functions, $\mathcal U_S$ (smoking valued at $+\$1{,}000$) and $\mathcal U_R$ (at $-\$1$), and two decision-function nodes. The lesion selects which node controls $\mathrm{Act}$, and neither node has an arrow to $\mathrm{Cancer}$. So intervening leaves $P(\text{lesion})=p$ unchanged, and smoking beats refraining by $p\cdot\$1{,}000$. This is the paper's demonstration that one criterion yields one-boxing *and* smoking. It also shows that the graph, not the equation, carries the Newcomb/lesion asymmetry. The paper adds that the problem is "badly confused" and recommends abandoning it.

### Transparent Newcomb and Parfit's hitchhiker

This is where "observation changes the node" matters. The agent sees a full box, so she is running $\mathrm{fdt}(\cdot,\textit{full})$. $\mathrm{Prediction}$ depends on that node, and $\mathrm{Prediction}$ determines whether the body is controlled by $\mathrm{fdt}(\cdot,\textit{full})$ or $\mathrm{fdt}(\cdot,\textit{empty})$. Let $q$ be her credence that she two-boxes on seeing an empty box. Then:

- Output *onebox*: $\mathbb E[V] = 0.99\times 1{,}000{,}000 + 0.01\,q\times 1{,}000 = 990{,}000 + 10q$.
- Output *twobox*: $\mathbb E[V] = 0.01\times 1{,}001{,}000 + 0.99\,q\times 1{,}000 = 10{,}010 + 990q$.

(The paper's printed formulas contain a typo, "$\$110,00$"; the algebra above is mine.) For any $q\in[0,1]$ one-boxing wins by a wide margin. Note the envisioned scenario: when she imagines two-boxing, she imagines *seeing an empty box*.

The paper says one-boxing here is "precisely equivalent to paying the driver in Parfit's hitchhiker problem", but gives no calculation. Here is one under my own symmetric-error assumption. The driver errs with probability $0.01$, dying costs $\$1{,}000{,}000$, paying costs $\$1{,}000$, and the driver's prediction depends on $\mathrm{fdt}(\cdot,\textit{city})$:

- Output *pay*: $\mathbb E[V] \approx 0.99(-1{,}000) + 0.01(-1{,}000{,}000) = -\$10{,}990$.
- Output *refuse*: $\mathbb E[V] \approx 0.99(-1{,}000{,}000) = -\$990{,}000$.

So she pays, even though in the city the cost is a sunk-benefit loss from the viewpoint of her actual observation.

### Blackmail

In the paper's mechanical blackmail, the blackmailer perfectly predicts what the agent would do upon receiving a letter. Intervening on $\mathrm{fdt}(\cdot,\textit{blackmail})$ changes both what she does if blackmailed *and* whether she is blackmailed. Paying yields blackmail with probability $\approx 1$ and a loss of $\$1{,}000$. Refusing yields blackmail with probability $\approx 0$. So she refuses, even while holding the letter. Equation (4) does not condition on having been blackmailed, so the hypothetical for refusal contains a world without a letter.

For an imperfect predictor, the paper gives an example with a $0.0009$ false-positive rate: refusal costs $0.0009\times 1{,}000{,}000 = \$900$ in expectation versus $\$1{,}000$ for paying, so she refuses. The paper then says that at $0.011\%$ she pays. By the same arithmetic the break-even error rate is $10^{-3}$ ($0.1\%$), so I read "$0.011\%$" as a slip for something like $0.11\%$. The mechanism is what matters: A-FDT compares *policies' consequences across observation-differing worlds*.

For XOR blackmail, the letter's existence is correlated with termites only through the predictor's reading of the agent's disposition. The infestation node has no arrow from $\mathrm{fdt}$, so the infestation probability is invariant across hypotheticals. Paying only changes whether she gets letters in the termite-free world. She refuses. EDT, conditioning on a letter in hand, pays, and the paper notes neither the tickle defense nor ratification helps EDT here.

### Death in Damascus

Death's book depends on $\mathrm{fdt}$ via an accurate prediction. Staying yields $\mathbb E[V]=0$ (Death is in Damascus), and fleeing yields $-\$1{,}000$. A-FDT stays. There is no instability, because the hypotheticals never imagine Death's location fixed while her action moves. CDT, by contrast, cycles between beliefs. The paper adds that a CDT agent even declines a \$1 truly random coin, which in fact gives a 50% chance of survival, because its hypotheticals treat Death's location as independent of its choice. (This is a longer argument that I only gesture at here.)

## 6. Why this is a principled rule, not a trick

**The utility argument [Source].** The paper's central justification is performance: A-FDT's imagined worlds track the dependencies that actually obtain between agents and predictors, so agents who use it tend to get richer in *fair* problems. CDT agents imagine "a hypothetical scenario in which a perfect predictor made an incorrect prediction", and EDT agents respect too many correlations: "EDT's hypotheticals respect too many correlations between variables; CDT's hypotheticals respect too few."

**Dominance is not neutral [Source].** Two-boxing "dominates" only if dominance is judged with CDT-style counterfactuals. Every method for building hypotheticals induces its own dominance notion. Conditioning makes refraining from smoking "dominate". A-FDT's own notion holds fixed all relevant subjunctive dependencies, and by that criterion A-FDT never takes a dominated action. The paper concludes dominance cannot independently adjudicate between theories.

**Precommitment and value of information [Source].** Because A-FDT "always act[s] as [it] would have precommitted to act", it needs no costly binding mechanisms. It is reflectively stable in fair problems, since the A-FDT agent holding a blackmail letter does not wish to switch to CDT. It also does not assign negative value to information. The paper reads the apparent oddness of "paying the driver" or "one-boxing on full" as framing effects.

**Fairness [Source, Open].** The paper's boundary: a problem is fair if outcomes depend only on the agent's *behavior in that problem* (including predictions of it), and not on which algorithm produced the behavior. A predictor who rewards agents for one-boxing is fair. One who rewards agents for *being CDT* is not. The authors report no fair problem where A-FDT loses to a rival theory, but they flag that no formal fairness criterion exists. Footnote 15 notes an obstacle: a problem that punishes copying Fiona's action is intrinsically unfair to her and not to Carl, and it is unclear how to transform that into an analogous unfair-to-Carl problem.

**No metaphysical commitment [Source].** The paper claims that A-FDT agents are "no more deluded" than CDT agents. A deterministic CDT agent also imagines hypothetical worlds where her action token differs. The paper's response to "control over mathematical functions" is that the same objection would also deny control over decision tokens. The practical content is: "weigh different imaginary worlds in which her decision procedure has different logical outputs, and execute the action corresponding to the best such world."

## 7. Applying A-FDT to an unfamiliar case: a checklist [Mine]

1. Write the outcome, utility, and all variables, including observations and any agents' predictions or copies.
2. Identify which variables are physical consequences of $\mathrm{Act}$, which are functions of the decision procedure (copies, models, predictors), and which are merely correlated (common causes, coincidences). Apply the "evaluates or models the agent" test.
3. Build $G$ with $\mathrm{fdt}$ nodes for each relevant input. Route the selection of the controlling node through whatever determines the observation.
4. For each action $a$, perform $\mathrm{do}(\mathrm{fdt}(\cdot,x)=a)$. Propagate; do not condition on $x$ over and above its place in the graph. Compute $\mathbb E[V]$.
5. Choose the argmax. If the answer depends on unknown quantities such as $q$ (credence about one's behavior on other inputs), check sensitivity. In the worked examples the sign of the comparison did not depend on them.
6. Stress-test $G$. If the result flips when you add or remove an edge, the case is hostage to the unresolved dependence-structure question, not to Equation (4) itself.

## 8. Limits and open questions

- **Where does $G$ come from?** This is the paper's own "largest open problem". Everything A-FDT recommends is conditional on $G$ being correct. A bad dependence graph produces confident bad advice just as a bad causal graph does for CDT.
- **Counterpossibles.** Equation (4) outsources them to $G$. A principled semantics (what would a predictor of *this* algorithm output if it output something else?) is missing.
- **Action versus policy.** The paper says the policy-selecting formalization "only matters in multi-agent dilemmas so far as we can tell". I flag that A-FDT as defined here handles observation-dependence by node-switching, which already approximates policy selection. But a full account would intervene on whole input-to-action maps.
- **Fairness and optimality.** No formal criterion exists, and the paper admits not knowing "whether FDT is optimal among decision theories, or even (on a formal level) what optimality consists in."
- **Approximation.** The worked examples use minimal models; bounded agents would approximate. The paper expects approximate versions of the theories to keep their relative character.

## 9. Conclusion

A-FDT is an expected-utility rule with one distinctive move: evaluate each action by intervening on the output of the decision function, and let a supplied dependency graph say what else would change. When the graph has only causal edges it coincides with CDT and EDT. When predictors, twins, or observation-contingent offers appear, the extra edges produce one-boxing, cooperation with twins, paying the hitchhiker, refusing blackmail, and calm acceptance in Damascus, while the lesion's lack of an edge yields smoking. The theory's strength is a single rule that behaves well on these cases. Its weakness is that the rule is only as good as the graph, and the paper is candid that nobody yet knows how to derive the graph from evidence.

**Reference.** E. Yudkowsky and N. Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060.