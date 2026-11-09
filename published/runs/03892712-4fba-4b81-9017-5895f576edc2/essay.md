# A-FDT: Choosing the Output of a Function, One Observation at a Time

## 1. What this essay is about

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* proposes that a rational agent should treat her decision as the output of a fixed mathematical function. On this view the deliberating agent asks: "Which output of this very function would yield the best outcome?" The paper gives this idea a precise form in Equation (4) of Section 5. That equation selects an **action** for the observation actually received. Footnotes 7 and 16 say that the authors' *preferred* formalization instead selects a **policy**, meaning a map from observations to actions.

To keep the two apart, this essay uses **A-FDT (action functional decision theory)** for the theory defined by Equation (4), which is my primary object. I use **P-FDT** for the policy-selecting variant mentioned in the footnotes. **CDT** (causal decision theory) and **EDT** (evidential decision theory) keep their usual names. When I quote the paper, its own label "FDT" appears unchanged.

The essay has four goals:

- reconstruct A-FDT precisely;
- give a recipe for applying it;
- work through the main examples;
- identify which parts of the recipe the source fixes and which parts I supply.

## 2. The common template: expected utility over hypotheticals

The paper treats EDT, CDT and FDT as variants of a single scheme. Each picks an action maximizing

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),$$

where $x$ is the observation history and $\hookrightarrow$ is a "decision hypothetical" connective. Following Joyce, the theories agree about how to value outcomes and disagree about the "epistemic perspective", that is, how to construct the hypothetical world in which $a$ is chosen. Writing $V = \mathcal U(\textsc{Outcome})$, the three rules are:

- **EDT (Eq. 2):** $\arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a)$. This is ordinary conditioning.
- **CDT (Eq. 3):** $\arg\max_a \mathbb E(V \mid do(\textsc{Act}=a), \textsc{Obs}=x)$. This is a Pearl intervention on the physical act inside a causal graph $G$.
- **A-FDT (Eq. 4):**
$$\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\big(V \mid do(\textsc{fdt}(\underline P,\underline G,\underline x)=a)\big).$$

A-FDT has the same shape as CDT. It also uses an intervention and an argmax over actions. The two theories differ in two ways, and the paper states both explicitly:

1. **Locus of intervention.** CDT intervenes on $\textsc{Act}$, a physical variable describing what the agent's body does. A-FDT intervenes on $\textsc{fdt}(\underline P,\underline G,\underline x)$, a *logical* variable that represents the output of the A-FDT procedure itself when run on the inputs $(P,G,x)$. The underlines mark dequoting: the variable's name is built from the agent's own model and observation. The paper argues that this self-reference is harmless, citing Kleene's recursion theorem. An agent can have a variable that *represents* the output of her procedure without knowing its value.

2. **Treatment of observation.** In the paper's words, "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." In Eq. (4) the observation $x$ appears only inside the name of the intervened node. It does not appear as a conditioning event.

The graph $G$ now has to encode more than causal structure. It must encode what the paper calls *subjunctive dependence*: how "changing a logical variable affects all other variables." Two physical systems that compute the same function both subjunctively depend on that function. Examples are an agent and a predictor's accurate model of her, or two calculators computing $6288+1048$. A lesion that merely correlates with smoking does not depend on the agent's function in this way. The slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

## 3. The structure of an A-FDT model

The paper never states a general schema, but its worked examples share one. I make it explicit here. This is my reconstruction and I take it to be faithful to Figures 4–7 of the paper.

**Ingredients.**

- **Observations.** A set $\mathcal X$ of inputs that the agent's decision function might receive in the problem, for example {*full*, *empty*} or {*letter*, $\emptyset$}.
- **Function nodes.** For each $y\in\mathcal X$, a logical node $F_y := \textsc{fdt}(\underline P,\underline G,\underline y)$ taking values in $\mathcal A$.
- **Exogenous chance nodes.** Variables such as predictor accuracy, the lesion, or termites, with prior probabilities.
- **Dependent nodes.** Variables that are functions of the $F_y$ and of chance nodes. Examples are a prediction, a twin's act, or Death's appointment book.
- **The act.** $\textsc{Act} = F_{\textsc{Obs}}$, where $\textsc{Obs}$ is itself determined by other nodes, often by a prediction. The physical act is therefore a *downstream* variable, and which function node "controls" it depends on what the agent actually sees.
- **Utility.** $V$ is a function of the act and the state.

**Evaluation.** The agent has actually observed $x$. For each $a\in\mathcal A$ she does the following:

1. Set $F_x := a$ by intervention. This cuts its incoming edges and gives it a point mass.
2. Leave the other function nodes $F_y$ ($y\neq x$) and all exogenous nodes at their prior distributions.
3. Propagate the change forward through every node that depends on $F_x$, whether causally or subjunctively.
4. Compute $\mathbb E[V]$ over the remaining uncertainty, including uncertainty about *which observation would have occurred*.

She then chooses the maximizing $a$.

Two features follow directly and are worth stressing.

- **A-FDT does not condition on $x$.** The hypothetical world for "$F_x=a$" may be one in which the agent would *not* have observed $x$ at all. The paper embraces this result: FDT agents "entertain the hypothesis that, if their action were different, they might have *made different observations*."
- **Probability-zero actions are not a problem.** Unlike EDT, A-FDT never conditions on the act, so an action the agent is nearly certain she won't take can still be evaluated. The intervention defines the hypothetical regardless of the prior.

## 4. Worked examples

All payoffs are in dollars-as-utility, as in the paper.

### 4.1 Twin Prisoner's Dilemma

There is no observation, so only one node $F$ exists. The agent's act and her twin's act both equal $F$, because they run the same reasoning.

- $do(F=C)$: both cooperate, so $\mathbb E V = 1{,}000{,}000$.
- $do(F=D)$: both defect, so $\mathbb E V = 1{,}000$.

A-FDT cooperates. CDT intervenes on its own act alone, holds the twin fixed, finds that defection dominates, and defects.

### 4.2 Newcomb's problem

There is one node $F$. The predictor's prediction equals $F$ with probability 0.99 (node *Accurate*) and is wrong otherwise. Box B is full iff the prediction is "one-box".

$$\mathbb E[V\mid do(F=\text{one})] = 0.99(1{,}000{,}000) = 990{,}000,$$
$$\mathbb E[V\mid do(F=\text{two})] = 0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000.$$

A-FDT one-boxes. (The paper's EDT computation reports \$999,000 for one-boxing. That is evidently a slip for \$990,000, which is the figure it gives for FDT.) CDT computes $p\cdot 10^6$ versus $p\cdot 10^6 + 1000$ for any fixed $p$ and two-boxes.

The paper insists on how the agent understands these hypotheticals. When she imagines two-boxing, she imagines the FDT algorithm itself outputting *twobox*. That is a counterpossible, since the algorithm's actual output is fixed by logic. She does not imagine a backward causal signal: "Nowhere in Fiona's reasoning above is there any appeal to a belief in retrocausal physics."

### 4.3 Smoking lesion

Here the graph is different, and this difference is how A-FDT separates itself from EDT. *Cancer* depends on the *Lesion* node, not on any function node. The paper's formalization adds a twist: the lesion fixes which utility function, and hence which model $P_S$ or $P_R$, the agent is running. So $\textsc{Act} = \textsc{fdt}(\underline{P_S},\underline G)$ if lesion, and $\textsc{Act} = \textsc{fdt}(\underline{P_R},\underline G)$ otherwise.

Intervening on the $P_S$ node does not change $P(\text{lesion})=p$. With $q$ the prior that the $P_R$-version smokes, the two hypotheticals are:

- smoke: $p(10{,}000 + 1{,}000) + (1-p)(990{,}000 + 1{,}000q)$;
- refrain: $p(10{,}000) + (1-p)(990{,}000 + 1{,}000q)$.

Smoking wins by $p\cdot 1000$, so A-FDT smokes. The general lesson is that A-FDT agrees with CDT wherever correlations are merely statistical. The paper notes that all three theories coincide whenever every correlation between the act and the world is caused by the act (or runs through the agent's function).

### 4.4 Transparent Newcomb

This is the first case where observation matters. There are two nodes, $F_{\text{full}}$ and $F_{\text{empty}}$. The prediction is about $F_{\text{full}}$ (with 1% error). The box is full iff the prediction is "one-box", and $\textsc{Act}=F_{\textsc{Obs}}$. The agent sees *full* and intervenes on $F_{\text{full}}$. Let $q = P(F_{\text{empty}}=\text{two})$.

- $do(F_{\text{full}}=\text{one})$: $0.99(1{,}000{,}000) + 0.01\cdot q\cdot 1{,}000 = 990{,}000 + 10q$.
- $do(F_{\text{full}}=\text{two})$: $0.01(1{,}001{,}000) + 0.99\cdot q\cdot 1{,}000 = 10{,}010 + 990q$.

A-FDT one-boxes while looking at a full box. (The paper prints the second value as "\$110,00 + q·\$990". The correct arithmetic is \$10,010 + 990q.) CDT and EDT both two-box once the box is seen to be full. Because the predictor anticipates this, they see empty boxes.

This case is structurally identical to **Parfit's hitchhiker**. Paying in the city corresponds to one-boxing, and the driver's 99%-accurate lie detection corresponds to the predictor. A-FDT therefore pays. The paper's defence of this verdict rests on three arguments:

- **Precommitment:** CDT and EDT agents would *precommit* to this behaviour if they could.
- **Value of information:** acting this way means the agent never assigns negative value to information.
- **Utility:** it is simply what makes agents rich.

### 4.5 XOR blackmail

Termites are present with probability $p$. There are nodes $F_L$ (letter) and $F_\emptyset$. An infallible predictor sends the letter iff (no termites and $F_L=$pay) or (termites and $F_L=$refuse). The agent has received the letter.

- $do(F_L=\text{pay})$: with termites, no letter arrives and she loses $10^6$. Without termites, the letter arrives and she pays 1000. Value: $-10^6p - 1000(1-p)$.
- $do(F_L=\text{refuse})$: with termites, the letter arrives and she loses $10^6$. Without termites, there is no letter and no loss. Value: $-10^6 p$.

A-FDT refuses, by a margin of $1000(1-p)$. The intervention does not move $p$, because termites do not subjunctively depend on the agent's function. It only moves *whether the letter is sent*. EDT pays, because conditioning on paying "sends her probability on termites to 0." CDT refuses, but for a different reason. Its hypothetical in which she pays has the infallible predictor erring.

### 4.6 Mechanical blackmail and Death in Damascus

In the **mechanical blackmail** case, the blackmailer runs the program iff she predicts the agent would pay. With perfect prediction:

- $do(F_{\text{bm}}=\text{pay})$ yields blackmail and a payment: $-1000$.
- $do(F_{\text{bm}}=\text{refuse})$ yields no blackmail: $0$.

A-FDT refuses, even with the letter in hand. With error rate $\varepsilon$ (false predictions of paying), refusing costs $\varepsilon\cdot 10^6$ against 1000 for paying, so the threshold is $\varepsilon = 0.1\%$. The paper's example of 0.09% agrees: she refuses. Its follow-up figure, "0.011%", does not fit this threshold and is probably a typo for 0.11%.

In **Death in Damascus**, Death's book equals $F$ exactly. Both $do(F=\text{stay})$ and $do(F=\text{flee})$ yield death, and fleeing costs an extra 1000. A-FDT stays, and it reaches this answer without the instability, ratification loops or randomization that CDT needs.

## 5. A recipe for unfamiliar cases

The examples suggest the following procedure. Steps 1–4 and 6 follow the paper. Step 5 contains my additions.

1. **Enumerate the inputs** $\mathcal X$ that the agent's decision procedure might face in the scenario. Create a node $F_y$ for each.
2. **Locate every copy and every model of the procedure.** Twins, predictors, simulations, lie detectors and earlier or later selves facing an identical decision all get edges from the relevant $F_y$, plus noise nodes for imperfect accuracy. Mere correlates, such as lesions, genes or demographic statistics, get no such edges. Ask whether the process works by representing the agent's reasoning or only shares a cause with her action.
3. **Wire the act** as $\textsc{Act}=F_{\textsc{Obs}}$, and model how $\textsc{Obs}$ is produced. In particular, check whether the observation itself depends on a prediction.
4. **Intervene on the node for the actual input**, propagate forward, and compute $\mathbb E V$ without conditioning on $x$.
5. **Assign distributions to the non-intervened function nodes** (see §6.2), and break ties by a fixed rule.
6. **Choose the argmax.**

The paper's own gym example shows step 2 applied across time. If today's decision is relevantly identical to next week's, the A-FDT agent treats both as outputs of the same function. Going to the gym today then "comes with" going in future weeks.

## 6. What the source leaves open, and how one might operationalize it

### 6.1 The graph $G$

The paper is frank that this is the crux. Eq. (4) "works *given* a graph that accurately describes how changing the value of a logical variable affects other variables, but it is not yet clear how to construct such a thing." It also writes: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

The underlying semantics, a $true(\cdot)$ operator for counterpossibles, is explicitly left undefined. Eq. (4) substitutes Pearl's $do$ on a supplied graph. A-FDT is therefore a *conditional* decision procedure: it is fully determinate once $G$ is given, and silent about where $G$ comes from.

My operational heuristic is the one in step 2 of the recipe: draw an edge from $F_y$ to a variable iff that variable's value is computed, wholly or partly, by evaluating a representation of the agent's decision procedure on input $y$. Accuracy goes into noise nodes. Hard cases remain where this criterion gives no clear verdict. Examples are predictors who use crude behavioural statistics, or agents who run *similar but not identical* algorithms. A natural extension, which is mine and not the paper's, gives such agents a partial dependence: a node that copies $F_y$ with probability $\rho$ and is otherwise independent. $\rho$ then becomes an explicit modelling parameter.

### 6.2 Priors on the function nodes not being intervened on

When the agent intervenes on $F_x$, the other nodes $F_y$ keep their priors. In the smoking lesion and transparent Newcomb cases the paper notes that the "correct" values are $q=0$ and $q=1$ respectively, "as you may verify". It adds that in those cases the value of $q$ does not change the verdict.

In general, however, it can matter. Here is my own illustration. An agent sees *red* or *blue* with probability ½ each, and must output A or B. A perfect predictor pays 2 if her outputs on both colours are B, pays 1 if both are A, and pays 0 if they differ. On seeing red, A-FDT intervenes on $F_{\text{red}}$, holding $P(F_{\text{blue}}=A)=r$:

$$\mathbb E[V\mid do(F_{\text{red}}=A)] = r, \qquad \mathbb E[V\mid do(F_{\text{red}}=B)] = 2(1-r).$$

If $r>2/3$, she picks A. By symmetry the same happens on blue, so she ends up at the inferior "both A" outcome, worth 1. P-FDT instead optimizes over the whole map $\{\text{red},\text{blue}\}\to\{A,B\}$ and picks "always B", worth 2. In this sense A-FDT is a *coordinate-wise* optimizer across its own possible inputs. It is guaranteed only to reach a fixed point, not the global optimum. The paper suggests the action/policy distinction matters "in certain multi-agent dilemmas". The example shows that a single agent facing a predictor can also exhibit it.

Two operational choices are available for A-FDT as defined:

- **(a) Self-consistent priors.** Set the distribution of each $F_y$ to the output A-FDT itself would give on $y$. This requires solving for a fixed point across inputs, which matches the paper's "correct $q$" remarks. Multiple fixed points may exist, as in the example above.
- **(b) Report the dependence.** Treat the result as conditional on stated beliefs about the other nodes, and flag cases where the argmax changes with those beliefs.

I recommend (a), together with an explicit check for multiple equilibria. Where the equilibria differ, the gap between A-FDT and P-FDT is exactly the issue the footnotes set aside.

### 6.3 Conditioning on the observation

There is a textual wrinkle. In the transparent Newcomb discussion the paper writes the objective as $\mathbb E(V\mid do(\textsc{fdt}(\ldots,\textit{full})=a, \textsc{Obs}=\textit{full})$, with an unclosed parenthesis. Read literally, this conditions on the box being full. However, the paper's *computation* gives weight 0.01 to scenarios in which the box is empty, which shows it does not condition. Eq. (4) also contains no conditioning term. Finally, the paper says that Timeless Decision Theory, which "prescribes both conditioning on evidence *and* changing the place where one intervenes," suffers a harmful "double update."

I therefore read A-FDT as **not** conditioning on $x$. Under the alternative reading, transparent Newcomb would yield two-boxing and the paper's headline verdicts would collapse.

### 6.4 Ties, mixed actions, and boundedness

Eq. (4) uses an argmax over a finite action set. It specifies neither tie-breaking nor randomization. A deterministic tie-breaking rule, which predictors can then model, seems the right default. Mixed actions can be added as extra pure options when a genuinely random device is available. The Death in Damascus discussion shows that A-FDT, unlike CDT, values such a device correctly: buying a truly random coin raises survival to 50%.

The paper also notes that exact maximization over realistic world-models is intractable. A-FDT is presented as an idealization, which bounded agents are expected to approximate.

## 7. Philosophical motivation in brief

The paper's case rests on utility actually achieved in what it calls "fair" problems, meaning problems where outcomes depend only on the agent's *behaviour*, not on her decision procedure as such. Newcomb's predictor counts as fair because it "doesn't punish rational agents; she punishes *two-boxers*."

The paper also rebuts dominance arguments against one-boxing. Every way of constructing hypotheticals induces its own notion of dominance, so dominance cannot neutrally adjudicate between theories. It adds a parity argument about "control": a deterministic CDT agent controls her action token no more and no less than an FDT agent controls her decision type.

Beyond this, the paper claims, without formal proof, that FDT is reflectively stable in fair problems, never pays for ignorance, and needs no precommitment devices, because it already acts as it would have precommitted to act. It also concedes that "fairness" lacks a formal definition and that FDT's optimality is unproven.

## 8. Conclusion

A-FDT, as given by Equation (4), is CDT with two changes. The intervention moves from the physical act to the logical output of the agent's own decision procedure on her actual input. And observations select *which* such output to intervene on instead of being conditioned upon. Given a graph encoding subjunctive dependence, the procedure is fully mechanical. It cooperates with twins, one-boxes in both opaque and transparent Newcomb problems, pays in Parfit's desert, smokes, refuses both kinds of blackmail, and stays in Damascus.

The theory's determinacy is borrowed from that graph, however, and the paper offers no general method for building it. Its action-level form also leaves the treatment of the agent's *other* possible inputs underdetermined. I have argued that this gap is best filled by a self-consistency (fixed-point) condition. Where that condition admits multiple equilibria, A-FDT can fall short of the policy-selecting P-FDT that the authors themselves prefer.

*Reference:* E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060v2.