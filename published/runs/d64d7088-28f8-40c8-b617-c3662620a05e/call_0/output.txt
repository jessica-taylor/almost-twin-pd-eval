# A-FDT: Choosing the Output of a Fixed Function

## 0. Naming and scope

The source paper (Yudkowsky and Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060) presents a family of ideas it calls functional decision theory. Its Section 5 gives the concrete procedure as Equation (4). This essay is about that procedure, which I call **A-FDT**. I call other theories by their own names: CDT (causal), EDT (evidential), and the paper's discussed-but-rejected variant FDT′. I flag my own additions as **[mine]** so they can be told apart from the source's claims.

## 1. The shared skeleton: expected utility with a hypothetical connective

The paper treats EDT, CDT and A-FDT as expected utility theories. An agent chooses the action $a$ maximizing

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),$$

where $x$ is the observation history and $\hookrightarrow$ is the "decision hypothetical" connective. Following Joyce's representation theorem, the theories do not disagree about valuing outcomes. They disagree about "the epistemic perspective from which actions are to be evaluated", that is, about how to read $\hookrightarrow$.

Operationally, the agent keeps a world-model $M$. For each candidate action she builds a hypothetical $M^{a\hookrightarrow}$, a transient object like "notes on scratch paper", computes its expected utility $V_a$, and takes the best. The theories differ only in what $M$ contains and how hypotheticals are built from it:

- **EDT**: $M = P$, and hypotheticals are Bayesian conditionals, $\arg\max_a \mathbb E(V \mid \mathrm{Obs}=x, \mathrm{Act}=a)$.
- **CDT**: $M=(P,G)$ with $G$ a causal graph, and hypotheticals are Pearl interventions, $\arg\max_a \mathbb E(V \mid \mathrm{do}(\mathrm{Act}=a), \mathrm{Obs}=x)$.
- **A-FDT**: also $M=(P,G)$, but intervention is on a different node, and observation is handled differently.

## 2. Equation (4)

The paper's formula, in its notation, is

$$\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

Writing the agent's own procedure as $\text{A-FDT}(P,G,x)$, the pieces are as follows.

**A node for a mathematical fact.** The model contains a variable $\mathrm{fdt}(\underline P,\underline G,\underline x)$ representing the output of the decision procedure when run on this very model and this very observation. Underlines denote dequoting: "if $x := 3$ then $Z\underline{x}$ denotes the variable name $Z3$." The model also contains nodes for other functions, such as a variable for $6288+1048$ with nearly all its mass on $7336$.

**Self-reference is harmless.** The agent need not know the *value* of her own output in order to have a node *representing* it. Kleene's second recursion theorem (quining) shows that such self-representing data structures exist.

**Intervention on the type, not the token.** CDT intervenes on $\mathrm{Act}$, a physical fact about her body. A-FDT intervenes on the logical fact about what her decision function outputs. In the paper's Peircean phrasing, CDT intervenes on the token "my action is $a$", while A-FDT "intervenes on the *type*."

**Observation changes which node is intervened on, instead of conditioning.** This is the second difference from CDT. When the observation history changes from $x$ to $y$, CDT swaps $\mathrm{Obs}=x$ for $\mathrm{Obs}=y$ as a conditioning event. A-FDT swaps the intervention target from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$. These are different nodes, outputs of the same function on different inputs. The graph $G$ says how each influences the world, including which observation the agent will receive.

**What $\mathrm{do}$ does.** Setting the node to $a$, the operator recomputes everything downstream of it in $G$ and leaves all else at its prior distribution. "Downstream" now means *anything that depends on the function's output*, not just anything physically caused by the agent's body.

The paper's summary of the contrast is that CDT and A-FDT "both construct counterfactuals by performing a surgery on their world-model that breaks some correlations and preserves others, but where CDT agents preserve only causal structure in their hypotheticals, FDT agents preserve all decision-relevant subjunctive dependencies in theirs." EDT preserves too many correlations, and CDT too few.

When every correlation between action and world is caused by the action, the three procedures coincide: $\mathbb E[V\mid a]=\mathbb E[V\mid\mathrm{do}(a)]=\mathbb E[V\mid \mathrm{do}(\mathrm{fdt}=a)]$. They come apart only when something correlates with the action without being caused by it, for instance when another agent predicts you.

## 3. Subjunctive dependence

What licenses an edge out of the $\mathrm{fdt}$ node? The paper's term is **subjunctive dependence**. When two physical systems compute the same function, their behaviors subjunctively depend on that function. A predictor holding an accurate model of the agent, a twin, and a copy all count. Two calculators computing $6288+1048$ are the standard picture.

The paper makes three clarifications:

1. Causal dependence is a special case. A scribe copying a calculator's output depends on it both causally and subjunctively.
2. Mere statistical correlation is not subjunctive dependence. Two coincidentally pink calculators do not covary under the supposition that one had been green.
3. Dependence comes in degrees. With an imperfect predictor or a noisy agent, "the interdependence is weakened, but not eliminated", as when a cosmic ray might corrupt a calculator.

The paper is also candid that Equation (4) requires evaluating **counterpossibles**. If the function outputs *cooperate* on this input, it does so necessarily. Supposing otherwise is like supposing $6288+1048\ne 7336$. It argues the difficulty is "technical rather than philosophical" and that A-FDT only needs a narrow slice: how predictors' predictions would change if the output changed. The variant FDT′ asks "what if I used a different decision function $f_n$?" instead. The paper argues FDT′ saves nothing, because the imagined world must still have all predictors of $d$ predict as if $d$ behaved like $f_n$.

## 4. Worked examples

### 4.1 Newcomb's problem

Fiona (the paper's A-FDT agent) has a graph in which a single node $\mathrm{fdt}(\underline{P^F},\underline{G^F})$ points to both $\mathrm{Act}$ and $\mathrm{Prediction}$. The predictor is accurate with probability 0.99, and the prediction determines Box B.

- $\mathrm{do}(\mathrm{fdt}=\textit{onebox})$: the act is one-box, and Box B is full with probability 0.99. EU $=0.99\cdot 10^6=\$990{,}000$.
- $\mathrm{do}(\mathrm{fdt}=\textit{twobox})$: the act is two-box, and Box B is full with probability 0.01. EU $=0.99\cdot 1000+0.01\cdot 1{,}001{,}000=\$11{,}000$.

A-FDT one-boxes. Carl (CDT) severs the link to the prediction, so for any $p=P(\text{full})$ two-boxing is better by \$1,000. Eve (EDT) one-boxes via conditioning, but her answer depends on a prior over her own action and can be pushed around by extreme priors (Spohn).

The paper stresses that Fiona does not believe in retrocausation. She just thinks "it is foolish to imagine her action changing without also imagining $\mathrm{FDT}(P^F,G^F)$ taking on a different value."

Her view is not changed by being nearly certain the box is full. Asked what *would happen if* she two-boxed, she answers that the function would have to output *twobox* on this input, and then the box is probably empty.

### 4.2 Smoking lesion: the graph matters

The same agent, with a different graph, smokes. Fiona's node for the lesion is *not* downstream of the $\mathrm{fdt}$ node, since the lesion is not computing anything about her. The paper has to model the agent as uncertain about her own preferences, running either $\mathrm{FDT}(P_S,G)$ or $\mathrm{FDT}(P_R,G)$ depending on the lesion. Holding the lesion probability $p$ fixed, smoking beats refraining by $p\cdot\$1{,}000$, the probability that this procedure is the one controlling her times the value of smoking.

The paper concedes this problem is contrived, calling it "badly confused", and treats it for historical reasons. The lesson for the practitioner is that A-FDT's prescriptions are not a function of the payoff table alone. They depend on which nodes subjunctively depend on the agent's procedure. Newcomb's problem and the smoking lesion problem have isomorphic probability tables, but different $G$.

### 4.3 Transparent Newcomb: observation as node-selection

Fiona's graph has two nodes, $\mathrm{fdt}(\ldots,\textit{full})$ and $\mathrm{fdt}(\ldots,\textit{empty})$. The prediction determines which of them controls $\mathrm{Act}$, because the prediction determines what she will see. Having seen a full box, she intervenes on the *full* node. Let $q$ be her prior that she two-boxes upon seeing an empty box.

- One-box: if accurate (0.99), the box is full and she one-boxes, giving \$1,000,000. If inaccurate (0.01), the box is empty and the *empty* node controls her action, worth $q\cdot\$1000$. EU $= 990{,}000 + 10q$.
- Two-box: if accurate, prediction is two-box and the box is empty, worth $q\cdot 1000$. If inaccurate, the box is full and she two-boxes, worth \$1,001,000. EU $= 10{,}010 + 990q$.

(The paper prints the second expression as "$\$110,00+q\cdot\$990$", an apparent typo, since $0.01\times 1{,}001{,}000=10{,}010$.) One-boxing wins for every $q\in[0,1]$. In imagining two-boxing at a full box, she imagines a world in which she probably saw an empty box.

A note on notation **[mine, interpretive]**: the paper's display attaches "$\mathrm{Obs}=\textit{full}$" inside the $\mathrm{do}$, but the numbers it computes let $\mathrm{Obs}$ vary across hypotheticals. The only role of the observation is to select the node. Imposing $\mathrm{Obs}=\textit{full}$ as a hard condition would reintroduce the "double update" the paper criticizes in Timeless Decision Theory, which "prescribes both conditioning on evidence *and* changing the place where one intervenes."

### 4.4 Blackmail and Death in Damascus

*Mechanical blackmail.* Upon seeing the letter, Fiona sets $\mathrm{fdt}(\ldots,\textit{blackmail})$ to *pay* or *refuse*. Paying makes blackmail near-certain and costs \$1,000. Refusing makes blackmail near-impossible. With a fallible predictor, refusal costs $\varepsilon\cdot\$1{,}000{,}000$ in expectation, where $\varepsilon$ is the chance the blackmailer wrongly predicts payment, against a flat \$1,000 for paying. The break-even is $\varepsilon=0.1\%$. The paper's $0.09\%$ example refuses (expected loss \$900). Its second example, "0.011%", would by this arithmetic still refuse (loss \$110). It presumably means $1.1\%$, at which paying is better. The qualitative lesson stands: she acts as "the kind of agent" that tends to get rich, even holding the letter and even knowing the predictor erred.

*XOR blackmail.* Intervening on the letter-node changes whether she receives the letter, but not whether she has termites. She refuses to pay, and so does Carl, but for different reasons. The paper notes that Carl's CDT hypothetical says the predictor *erred*, "despite the fact that the predictor is inerrant, *ex hypothesi*."

*Death in Damascus.* Setting the node to *stay* places Death in Damascus. Setting it to *flee* places Death in Aleppo, at an extra \$1,000. Fiona stays. There is no instability, because Death's location is downstream of the same node. Carl oscillates, and the paper shows him declining a \$1 truly random coin that offers a 50% survival chance, because his hypotheticals decouple Death from his choice.

### 4.5 Parfit's hitchhiker **[mine, computed in the paper's style]**

Let death cost \$1,000,000 and payment \$1,000, with a driver who is right 99% of the time. Using the node $\mathrm{fdt}(\ldots,\textit{city})$:

- Pay: ride with probability 0.99 and payment, EU $= -990 - 10{,}000 = -\$10{,}990$.
- Refuse: ride only if the driver erred (0.01), EU $= -0.99\cdot 10^6=-\$990{,}000$.

A-FDT pays. The paper says this is "precisely equivalent" to one-boxing in the transparent Newcomb problem, and offers three arguments for accepting both: it is what a CDT or EDT agent would precommit to, it avoids negative value of information, and it wins.

## 5. Why A-FDT is built this way

**Against EDT.** EDT hypotheticals "respect too many" correlations. In the cosmic-ray problem, an EDT agent who almost always takes \$1 treats taking \$100 as evidence of a cosmic ray (and a \$1,000 hospital bill), and so takes the \$1. A-FDT and CDT dismiss the merely statistical correlation.

**Against CDT.** CDT hypotheticals respect too few. The paper's test is to ask each agent, after the fact, what would have happened had she acted otherwise. Carl, against a perfect predictor, answers with a scenario in which a perfect predictor was wrong.

**Dominance is not neutral.** The paper observes that "every method for constructing hypotheticals gives rise to its own notion of dominance." Two-boxing dominates under CDT counterfactuals. Under A-FDT counterfactuals, which hold the subjunctive dependency fixed, one-boxing "dominates". So dominance cannot independently adjudicate between theories, and the paper appeals to utility achieved.

**Fairness.** A-FDT is not claimed to win every problem. A mind-reader who punishes agents for *using* a given decision procedure is unfair, because it rewards the procedure and not the action. The paper's slogan is that Newcomb's predictor punishes "*two-boxers*", not "rational agents". The authors claim A-FDT matches or beats rivals in "fair" problems (accurate beliefs, payoffs depending only on behavior in the problem at hand), but admit no formal criterion of fairness exists, and give an example of the difficulty: punishing anyone who acts like a copy of Fiona.

**Reflective stability.** Because A-FDT acts as it "would have precommitted to act", it needs no precommitment machinery and, the paper claims, has no motive to self-modify in fair problems. Its counterfactual about blackmail, that refusing means never being blackmailed, is borne out in practice.

## 6. What the source leaves open, and a practical reading

Equation (4) takes $(P,G)$ as given input, "in the same way that the relevant causal structure is given as an input to CDT." The paper says plainly that the construction of $G$ "rests on shakier philosophical foundations than" Equation (3), and that deducing subjunctive structure from observation "is perhaps the largest open problem". Beyond that, I see three underdetermined points, and give an operational reading of each. These readings are my proposals.

**(a) Constructing $G$ by hand.** For a stated problem, the following test is faithful to the paper's examples. Ask of each variable: *if this very procedure had output something else on this very input, would this variable differ, in a way not merely mediated by which world the agent happens to be in?*

- Direct yes: the agent's own act, and any copy or twin.
- Yes via a model: any predictor, as in Newcomb, blackmail and Death in Damascus. Arrows should run from the $\mathrm{fdt}$ node to the model's output, and then onward causally. Imperfect predictors become noisy nodes such as $\mathrm{Accurate}$.
- No: common causes that merely correlate (lesion, termites, cosmic rays) and anything with no model of the agent.

The conditions "lesion, termites, cosmic rays" are the paper's own cases. The general test is my extrapolation.

**(b) Observations and multiple nodes.** Equation (4) is written per observation, so the hypothetical for observation $x$ requires priors for the *other* nodes $\mathrm{fdt}(\ldots,y)$. In the paper's examples these priors turned out not to matter (the parameter $q$ dropped out of the comparison). It is not obvious that they never matter. The paper's footnote 7 says the authors' preferred formalization iterates over **policies**, mappings from observations to actions, and says this "makes a difference in certain multi-agent dilemmas." A natural policy-level restatement **[mine]** is

$$\pi^\ast=\arg\max_{\pi:\mathcal X\to\mathcal A}\ \mathbb E\big(V\mid \mathrm{do}(\mathrm{fdt}(\underline P,\underline G,\cdot)=\pi)\big),$$

after which the agent applies $\pi^\ast$ to her actual observation. This removes the need for priors on counterfactual-input outputs. In the transparent Newcomb problem it gives (*full→one-box*, *empty→two-box*) with EU $0.99\cdot10^6+0.01\cdot 10^3=\$990{,}010$, agreeing with Equation (4)'s answer at $q=1$. I do not claim this is identical to Equation (4) in general; the paper itself says only that the distinction has been set aside.

**(c) Counterpossible semantics.** Equation (4) deliberately avoids a $\mathtt{true}$ operator, relocating the difficulty into $G$. Footnote 9 mentions a possible "evidential version" that would condition on a false logical sentence, but notes no definition of such conditionals exists. A practitioner should therefore treat $G$ as modeling stipulation. Correctness of the output is conditional on its accuracy, and "garbage in" applies as strongly here as with CDT's causal graph.

**A usable recipe [mine, summarizing the above]:**

1. List variables and utilities. Identify which are computed by, or predict, the decision procedure.
2. Draw $G$ with one $\mathrm{fdt}(\cdot, x)$ node per possible observation. Make explicit which node controls $\mathrm{Act}$ in each branch, and which variables, including the observation itself, are downstream of the node.
3. For each action $a$ available under the actual observation, intervene on the corresponding node, propagate, and compute $\mathbb E[V]$ over the *whole* hypothetical, including branches where observations differ.
4. Pick the maximum. Check stability: does the output still maximize when you assume that A-FDT's output is what the model says?

## 7. The "global perspective" and the charge of oddness

The paper's philosophical gloss is that an A-FDT agent chooses "from a global perspective—asking herself 'What would the entire universe look like if the FDT algorithm behaved differently?'" It answers the objection that A-FDT agents "control" mathematical facts and the past by tu quoque. In a deterministic world, CDT agents only *imagine* their token action varying, and A-FDT agents *imagine* their type varying. "Any principled objection to the idea that FDT agents can 'control' their decision type will also imply that (deterministic) CDT agents cannot 'control' their decision token." Neither claim needs metaphysical commitments about free will. The paper concedes that both kinds of hypothetical "contain impossibilities", and says the difference is "practical".

## 8. Conclusion

A-FDT is Pearl-style expected utility maximization with one change: the intervention variable is the output of the agent's decision function (on the given observation), not her physical act, and observation selects which output-node is intervened on instead of being conditioned on. Everything else follows from the dependency graph. Predictors, twins and copies hang off the intervened node; common causes do not. The theory agrees with CDT and EDT when action and environment are related only causally, and parts from them in Newcomb-like cases, where it one-boxes, cooperates with a twin, pays Parfit's driver, refuses blackmail and stays in Damascus.

Its weaknesses are the ones the authors name. Its guidance is only as good as the supplied graph. It requires counterpossible reasoning with no formal semantics. Its optimality among theories rests on an undefined notion of "fair" problems. For a reader applying it to unfamiliar cases, the practical advice is to be explicit about the subjunctive dependencies in the model, treat observations as indices into a family of output-nodes (ideally at the policy level), and evaluate every hypothetical on the whole graph, including worlds in which one's own observations would have differed.

### References

- Yudkowsky, E. and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Pearl, J. (2000). *Causality*. Cambridge University Press.
- Gibbard, A. and Harper, W. (1978). "Counterfactuals and Two Kinds of Expected Utility."