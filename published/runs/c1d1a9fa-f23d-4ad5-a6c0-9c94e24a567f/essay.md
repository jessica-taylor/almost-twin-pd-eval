# A-FDT: Deciding by Intervening on Your Own Algorithm

*An expository essay on Equation (4) of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality"*

## 1. The question A-FDT asks

Every expected-utility theory answers the same schematic question: *what would happen if I chose $a$?* They differ in what "if" means. Yudkowsky and Soares put the contrast as a single sentence. A rational agent asks "Which output of this decision procedure causes the best outcome?", whereas causal decision theory (CDT) asks "Which physical act of mine causes the best outcome?" and evidential decision theory (EDT) asks "Which physical act of mine would be the best news to hear I took?"

In this essay I call the theory **A-FDT** (action functional decision theory). The name refers to the version formalized in Equation (4) of Section 5 of the paper. That version selects an *action* for the observations actually received. The authors say in a footnote that their "preferred formalization" instead iterates over *policies*, meaning maps from observations to actions. I return to that difference in §7. Everything up to then concerns A-FDT as Equation (4) states it.

The central idea is this. An agent's decision is the output of a fixed mathematical function. Other things in the world can also depend on that function's output: a twin running the same reasoning, or a predictor holding an accurate model of the agent. When the agent deliberates, it should vary the *output of the function* and propagate the change to everything that depends on it. It should not vary its physical act alone while holding the function's other "instances" fixed.

## 2. Background: three ways to build a hypothetical

The paper starts from a Joyce-style expected-utility template:

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j).$$

Here $x$ is the observation history and $\hookrightarrow$ is a "decision hypothetical" connective that each theory interprets in its own way. The authors follow Joyce in saying the theories share a theory of value and differ only in "the epistemic perspective from which actions are to be evaluated."

Write $V = \mathcal U(\textsc{Outcome})$. The three rules are then:

- **EDT** (Eq. 2): $\operatorname{argmax}_a \mathbb E(V \mid \textsc{Obs}=x,\ \textsc{Act}=a)$. The agent conditions on the act.
- **CDT** (Eq. 3): $\operatorname{argmax}_a \mathbb E(V \mid \mathrm{do}(\textsc{Act}=a),\ \textsc{Obs}=x)$. The agent performs Pearl surgery on the physical-act node, given a causal graph $G$.
- **A-FDT** (Eq. 4):

$$\boxed{\ \mathrm{FDT}(P,G,x) \;:=\; \operatorname*{argmax}_{a\in\mathcal A}\ \mathbb E\!\left(V \;\middle|\; \mathrm{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right)\ }$$

The underlines mark dequoting. $\textsc{fdt}(\underline P,\underline G,\underline x)$ is a *variable* in the agent's own model. Its name encodes the inputs, and it stands for "what the A-FDT algorithm outputs when run on this model and these observations." The model therefore contains a representation of its own decision procedure. The authors call this self-reference "harmless," citing Kleene's recursion theorem: the agent needs a variable that *represents* the output, not knowledge of its value. The paper also warns against confusing the variable $\textsc{fdt}(\underline P,\underline G)$ with the action $\mathrm{FDT}(P,G)$ that is eventually produced.

## 3. Reading Equation (4) precisely

The definition has three components.

**The world-model $P$.** This is a joint distribution over ordinary variables (box contents, lesions, letters) and *logical* variables, i.e. outputs of mathematical functions. The paper notes that $P$ should contain, for example, a variable for $6288+1048$ that "(hopefully) has most of its probability on $7336$."

**The dependency graph $G$.** For A-FDT, $G$ is not just a causal graph. It records "the logical, mathematical, computational, causal, etc. structure of the world more broadly." In particular, it says which nodes are children of the algorithm node: the agent's physical act, a predictor's prediction, a twin's choice, and so on. The paper calls the relation encoded by these edges *subjunctive dependence*: "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." Causal dependence is a special case of it, and mere statistical correlation does not imply it.

**The intervention.** Pearl's $\mathrm{do}$ is applied to the algorithm node. It sets that node to $a$, cuts the node off from its parents, and recomputes every descendant, leaving non-descendants at their prior distribution. The authors would ideally use a $\mathrm{true}(\phi)$ operator that updates on a possibly false logical sentence. But "it's not clear how to define a $\mathrm{true}$ operator," so A-FDT supplies the logical structure through $G$ and reuses $\mathrm{do}$.

**How observations enter.** The paper highlights two differences from CDT:

> "First, where CDT intervenes on a node $\textsc{Act}$ representing the physical action of the agent, FDT intervenes on a node $\textsc{fdt}(\underline P, \underline G, \underline x)$ representing the outputs of its decision procedure given its inputs. Second, where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon."

The second difference drives the theory's most surprising verdicts. Equation (4) does **not** condition on $\textsc{Obs}=x$. The observation only selects *which* algorithm node, $\textsc{fdt}(\cdot,\cdot,x)$ rather than $\textsc{fdt}(\cdot,\cdot,y)$, gets intervened on. The expectation is then taken over the whole prior. This includes worlds in which the agent would have seen something else, which is exactly the situation when a predictor's behavior determines what the agent observes.

**A practical recipe.** The following steps are my own summary of how the paper's worked examples proceed.

1. List the decision-relevant variables, including one algorithm node $\textsc{fdt}(\cdot,\cdot,y)$ for each observation $y$ the agent might receive in the problem.
2. Draw an edge from each algorithm node to everything that computes or accurately models that output: the physical act (when that observation obtains), predictors' predictions, twins.
3. Assign priors to exogenous nodes, including the agent's credence about what it would do on observations other than $x$.
4. For each $a$, set $\textsc{fdt}(\cdot,\cdot,x)=a$, recompute the descendants, and compute $\mathbb E[V]$.
5. Output the argmax.

## 4. Worked examples

### 4.1 Twin prisoner's dilemma

Both players run the same function, so $G$ has $\textsc{fdt}\to\textsc{Act}_{\rm me}$ and $\textsc{fdt}\to\textsc{Act}_{\rm twin}$. Intervening to set *cooperate* yields $(C,C)$ and \$1,000,000. Intervening to set *defect* yields $(D,D)$ and \$1,000. A-FDT cooperates. CDT holds the twin fixed, finds that defection dominates, and defects.

### 4.2 Newcomb's problem

The predictor is 99% accurate. Fiona, the paper's A-FDT agent, uses a graph in which $\textsc{fdt}(\underline P,\underline G)$ has two children: $\textsc{Act}$, and $\textsc{Prediction}$ (which also depends on an $\textsc{Accurate}$ noise node). Box B is a child of the prediction.

$$\mathbb E[V\mid \mathrm{do}(\textsc{fdt}=\textit{onebox})] = 0.99(10^6) = \$990{,}000,$$
$$\mathbb E[V\mid \mathrm{do}(\textsc{fdt}=\textit{twobox})] = 0.01(1{,}001{,}000)+0.99(1{,}000)=\$11{,}000.$$

A-FDT one-boxes. A small editorial point: the paper's EDT paragraph reports \$999,000 for one-boxing, but its own numbers give \$990,000. This does not affect any verdict.

The paper also answers the obvious objection. Fiona is nearly certain she one-boxes, so she is nearly certain the box is full; why not take both? Because her hypothetical for two-boxing is a world in which the *algorithm* outputs two-box, and in that world the predictor modeled it as doing so. In the authors' words, she "does not think that a physical signal passes between her action and the predictor's prediction," and so no retrocausation is assumed.

### 4.3 Smoking lesion

This example shows that A-FDT is not EDT in disguise. The lesion does not compute or model Fiona's algorithm, so $G$ has no edge from the algorithm node to $\textsc{Cancer}$.

The paper's formalization is somewhat elaborate. The lesion changes Fiona's *utility function*, so there are two possible algorithm nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ and $\textsc{fdt}(\underline{P_R},\underline G)$. Which one controls the act depends on the lesion. Intervening on the node for her actual model leaves $P(\textit{lesion})=p$ unchanged. Smoking then beats refraining by $p\cdot\$1{,}000$, and A-FDT smokes. The authors go on to call the dilemma "badly confused" and recommend that philosophers abandon it. Its role here is historical: it shows that a single rule can both one-box and smoke, contrary to the Gibbard–Harper framing.

### 4.4 Transparent Newcomb (and Parfit's hitchhiker)

Both boxes are visible. Box B is full iff the predictor predicted one-boxing *upon seeing it full*. Fiona's graph has two algorithm nodes:

- $\textsc{fdt}(\cdot,\cdot,\textit{full})$, which feeds both the prediction and the act;
- $\textsc{fdt}(\cdot,\cdot,\textit{empty})$, which feeds only the act.

The prediction selects which node controls the act. Seeing *full*, she intervenes on the first node. Let $q$ be her prior that she two-boxes on seeing empty (the correct value is $1$). Then

$$\text{onebox: } 0.99(10^6)+0.01\,q(1{,}000)=990{,}000+10q,$$
$$\text{twobox: } 0.01(1{,}001{,}000)+0.99\,q(1{,}000)=10{,}010+990q.$$

The paper prints the second figure as "\$110,00 + $q\cdot$\$990"; the correct total is $\$10{,}010+990q$. One-boxing wins for every $q\in[0,1]$.

Although she *sees* a full box, Fiona evaluates two-boxing by imagining a world where she probably saw an empty one. This is possible only because Eq. (4) does not condition on $\textsc{Obs}$. The paper argues that this case is structurally identical to Parfit's hitchhiker (pay the driver once you are in the city), and that intuitions treating the two differently are "so sensitive to framing effects" that they deserve little weight.

### 4.5 Blackmail

**XOR blackmail.** A-FDT refuses. Intervening on $\textsc{fdt}(\cdot,\cdot,\textit{letter})$ changes whether the letter is sent but not whether the termites exist, so paying buys nothing. CDT also refuses, though with a different hypothetical: Carl imagines that an inerrant predictor erred. EDT pays.

**Mechanical blackmail.** A-FDT refuses, while CDT and EDT pay. In the $\textit{refuse}$ hypothetical the program is never run. The paper adds a fallible version. If the blackmailer wrongly predicts payment with probability $\epsilon$, the comparison is

$$\text{pay: } -\$1{,}000 \quad\text{vs.}\quad \text{refuse: } -\epsilon\cdot \$10^6.$$

So the agent refuses iff $\epsilon<0.001$. The paper's two cases sit on either side of this threshold: $0.0009$ gives refuse, and $0.011\%=0.00011$… here the stated payment verdict holds only if the figure is read as roughly $0.11\%$. On the formula, the threshold is $0.1\%$. I flag this as my own reading of an apparent misprint.

### 4.6 Death in Damascus

Death's appointment book is a child of the algorithm node. Under either intervention, death is certain, so A-FDT simply avoids the \$1,000 cost of fleeing and stays. CDT, by contrast, is "unstable," and with ratification it will not even pay \$1 for a truly random coin that gives a 50% chance of survival. A-FDT, whose hypotheticals keep Death correlated with its algorithm but not with a truly random coin, values the coin at about \$500,000 and buys it. That last verdict is my own straightforward application of the equation, not a calculation stated in the paper.

## 5. When the three theories agree

The paper states a clean sufficient condition. If every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$ (apart from the algorithm node itself), then

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathrm{do}(a)]=\mathbb E[V\mid \mathrm{do}(\textsc{fdt}=a)].$$

In ordinary problems A-FDT is therefore just expected-utility maximization. It diverges only when something outside the agent's causal future tracks its decision function: predictors, copies, other agents reasoning symmetrically, or the agent's own future selves. The paper's gym and voting examples are of this last kind.

## 6. Dominance, fairness, and the philosophical case

**Dominance is relative.** The authors argue that "every method for constructing hypotheticals gives rise to its own notion of dominance." CDT-dominance favors two-boxing. FDT-dominance holds the subjunctive dependencies fixed while switching the output, and A-FDT never violates it. So dominance cannot adjudicate between the theories without begging the question. The paper falls back on *utility achieved*: "Utility has primacy."

**Fairness.** Any theory can be punished by a problem that inspects the agent's procedure; for example, "reward non-FDT agents." The authors restrict their claim to "fair problems," where "the outcome depends only on the agent's behavior in the dilemma at hand," and the agent's beliefs are accurate. They claim not to know of a fair problem in which FDT loses. They admit that fairness is not formalized. Their footnote example, punishing anyone who acts like a copy of Fiona, shows why this is hard.

**Precommitment and stability.** In the cases discussed, A-FDT "acts as it would have precommitted to act." According to the authors, it does not want to self-modify into something else in fair problems; CDT, by contrast, recommends abandoning itself for future dilemmas. They also claim A-FDT never assigns negative value to information.

**The "control" worry.** Is it delusional to treat a mathematical output as something one can vary? The authors reply with a parity argument. A deterministic CDT agent also has exactly one possible physical act yet profitably imagines alternatives, so "any principled objection to the idea that FDT agents can 'control' their decision type will also imply that (deterministic) CDT agents cannot 'control' their decision token."

## 7. What Equation (4) leaves open, and how I would operationalize it

The following points mark where the source stops and my own proposals begin.

**(a) Where $G$ comes from.** The paper says plainly that "figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem," and that Eq. (4) works only "given a graph that accurately describes how changing the value of a logical variable affects other variables." It therefore gives no algorithm for deciding whether a given process depends on your function.

As an operational rule, I propose the following test, which goes beyond the source. Draw an edge from $\textsc{fdt}(\cdot,\cdot,y)$ to a variable $Z$ iff $Z$ is produced by a process that computes, or accurately models, *that function on that input*. Its correlation with your output then holds "insofar as it made no errors," in the paper's calculator analogy, and is not inherited from a common physical cause such as a lesion or a gene.

Imperfect modeling should be represented by an accuracy noise node, as the paper does for the Newcomb predictor, rather than by weakening the edge in some other way. Ambiguous cases, such as a predictor that uses only crude demographic statistics, should be modeled as a mixture: one branch with the edge and one without, weighted by credence. This keeps the computation inside Pearl's framework. It is a modeling convention, not something the authors endorse.

**(b) Priors on the other algorithm nodes.** In the transparent and blackmail problems, the agent needs credences such as $q$ about what it would do on observations it did not receive. The paper shows that the verdict there is robust to $q$, but in general it need not be. A natural fixed-point convention is my suggestion: set $q$ to the output A-FDT itself returns on that other input. This is the "correct" $q$ the paper mentions.

**(c) Action versus policy.** Equation (4) optimizes one action with the other observation-nodes held at their priors. The authors' preferred variant chooses a whole policy $\pi:\mathcal X\to\mathcal A$ by intervening once on $\textsc{fdt}(\underline P,\underline G)=\pi$. They say the difference "only matters in multi-agent dilemmas so far as we can tell." Roughly, coordination across one's own observation-nodes can fail when each node is optimized separately against fixed beliefs about the others.

So, applying the assigned theory: always compute Eq. (4) as written. If the answer depends sensitively on the assumed behavior at other nodes, report that sensitivity, and note that the policy formulation, which is a different theory, may diverge.

**(d) Counterpossibles.** For a deterministic algorithm, "$\textsc{fdt}=a$" is false for all but one $a$. The graph-plus-$\mathrm{do}$ device sidesteps this formally. The authors note that a satisfying account of counterpossible reasoning is lacking and call this "the main drawback of FDT relative to CDT at this time." They also reject the workaround FDT′, which iterates over alternative functions: predictors model *your* function, so the counterpossible problem simply reappears.

## 8. Conclusion

A-FDT is expected-utility maximization in which the hypothetical for action $a$ is built by Pearl surgery on the node representing *your decision function's output on your actual observations*. Everything that subjunctively depends on that output then moves with it. Observations select which node to intervene on; the theory does not condition on them.

This single change yields cooperation with twins, one-boxing in Newcomb's problem, smoking in the lesion case, paying in Parfit's desert, one-boxing in transparent Newcomb, and refusing blackmail. Ordinary decisions are left exactly as CDT and EDT treat them.

The cost is that A-FDT's inputs are richer and less well understood than CDT's. One needs a graph of logical dependence that no one yet knows how to learn, and a tolerance for counterpossible antecedents. Applying A-FDT to a new case is mechanical once that graph is fixed. Fixing the graph, by deciding what really computes your function, is where most of the remaining work lies.

**Reference.** E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060 (2017).