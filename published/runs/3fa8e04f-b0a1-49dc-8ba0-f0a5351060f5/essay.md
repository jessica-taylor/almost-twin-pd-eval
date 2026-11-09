# The Geometry of Subjunctive Choice: A Mathematical Account of Action Functional Decision Theory (A-FDT)

## 1. Introduction: Beyond the Causal–Evidential Stalemate

For decades, normative decision theory has been defined by a foundational schism between **Causal Decision Theory (CDT)** and **Evidential Decision Theory (EDT)**. In standard dilemmas, each theory exhibits characteristic strengths and pathologies:

* In **Newcomb's Problem** (Nozick 1969), an agent faces a transparent box $A$ containing $\$1,000$ and an opaque box $B$ containing either $\$1,000,000$ or $\$0$, determined by an accurate predictor who foresaw whether the agent would take both boxes or only box $B$. CDT agents notoriously "two-box," asserting that the money is already fixed in the past and that taking $A$ dominates leaving it behind. They routinely walk away with $\$1,000$. EDT agents "one-box," reasoning that choosing only $B$ provides excellent news regarding the contents of $B$, and walk away with $\$1,000,000$.
* In the **Smoking Lesion Problem** (Skyrms 1980), smoking is statistically correlated with terminal cancer due to a genetic lesion that acts as an unobserved common cause. Smoking itself does not cause cancer. CDT agents correctly recognize that smoking does not cause the lesion and collect the $\$1,000$ surplus of smoking. EDT agents, lacking a mechanism to sever mere statistical correlations, refrain from smoking in order to "manage the news," needlessly forfeiting utility.

Gibbard and Harper (1978) argued that rational agents cannot systematically both one-box in Newcomb's problem and smoke in the smoking lesion problem; an agent had to choose between the counterfactual surgery of CDT or the Bayesian conditioning of EDT.

**Action Functional Decision Theory (A-FDT)**—the action-interventional formulation of Functional Decision Theory presented by Yudkowsky and Soares (2017)—rejects this dichotomy. A-FDT grounds instrumental rationality not in physical interventions on physical tokens of behavior, nor in epistemic news-value, but in the counterfactual evaluation of the **mathematical function** determining the agent’s choice. 

By intervening directly on the logical identity of the decision procedure itself, A-FDT preserves *subjunctive dependencies*—dependencies mediated by logical necessity, prediction, algorithm-sharing, or simulation—while severing mere historical confounders. The result is a mathematically unified, non-ad-hoc decision rule that one-boxes in Newcomb's problem, smokes in the smoking lesion problem, pays the driver in Parfit's Hitchhiker, and stably resists extortion.

---

## 2. Decision Hypotheticals and Epistemic Perspectives

All major expected utility theories evaluate an action $a \in \mathcal{A}$ under an observation history $x \in \mathcal{X}$ relative to a set of outcomes $\mathcal{O}$ and a utility function $\mathcal{U}: \mathcal{O} \to \mathbb{R}$ via an expected utility formula:
\begin{equation}
\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \then o_j ;\, x) \cdot \mathcal{U}(o_j)
\label{eq:umax}
\end{equation}
Following Joyce’s (1999) representation theorem, expected utility theorists agree on the core axiomatic structure of valuation; they disagree fundamentally on the semantics of the conditional connective "$\then$"—that is, on the *epistemic perspective* from which hypothetical consequences are computed.

To operationalize "$\then$", an agent maintains a mental world-model $M$ and constructs, for each candidate action $a$, a hypothetical model $\mathcal{M}^{a \then}$. Expected utility is calculated within $\mathcal{M}^{a \then}$, and the agent selects the action that maximizes this value.

### 2.1 Evidential Decision Theory (EDT)
In EDT, $M = P(\cdot \mid x)$ is a standard probability distribution updated on observation $x$. EDT interprets $a \then o$ as standard Bayesian conditionalization:
\begin{equation}
P(a \then o_j ;\, x) \coloneqq P(o_j \mid x, a)
\end{equation}
The EDT decision rule (Equation 2 of Yudkowsky & Soares 2017) is:
\begin{equation}
\mathrm{EDT}(P, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\big[\mathbf{V} \mid \mathrm{Obs}=x, \, \mathrm{Act}=a\big]
\label{eq:edt}
\end{equation}
where $\mathbf{V} \coloneqq \mathcal{U}(\mathrm{Outcome})$. 

Because EDT conditions on the event $\mathrm{Act}=a$, it preserves all statistical correlations between $\mathrm{Act}$ and other variables, regardless of whether those correlations are causal, logical, or confounded by a common cause. As demonstrated by the Smoking Lesion Problem and the XOR Blackmail (Soares & Fallenstein 2015), this inability to sever spurious correlations leaves EDT vulnerable to irrational news-management and systemic extortion.

### 2.2 Causal Decision Theory (CDT)
CDT supplements the probability distribution $P$ with a causal directed acyclic graph (DAG) $G$, forming a causal theory $M = (P, G)$ in the sense of Pearl (1996, 2000). Counterfactuals are generated using Pearl's do-calculus operator, $\mathrm{do}(\mathrm{Act}=a)$, which physically severs all incoming arrows to the physical action node $\mathrm{Act}$ while keeping non-downstream variables fixed at their baseline distributions.

The CDT decision rule (Equation 3 of Yudkowsky & Soares 2017) is:
\begin{equation}
\mathrm{CDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\big[\mathbf{V} \mid \mathrm{do}(\mathrm{Act}=a), \, \mathrm{Obs}=x\big]
\label{eq:cdt}
\end{equation}
CDT succeeds in the smoking lesion problem because the unobserved lesion is not causally downstream of the physical act of smoking; the graph surgery cuts the correlation, allowing the agent to smoke and collect the free utility. 

However, CDT fails catastrophically when the environment contains accurate predictors, mental simulations, or psychological twins. When Carl (the CDT agent) faces Newcomb’s problem, his graph encodes $\mathrm{Prediction} \to \mathrm{Box\ B}$ and $\mathrm{Predisposition} \to \mathrm{Act}$, but contains no directed path from $\mathrm{Act}$ to $\mathrm{Prediction}$. The intervention $\mathrm{do}(\mathrm{Act}=a)$ severs the link with $\mathrm{Predisposition}$ and holds $\mathrm{Prediction}$ constant. Carl concludes that taking both boxes dominates taking one, completely blinding himself to the fact that his decision algorithm has already been simulated in the past.

---

## 3. The Core Formalism of Action Functional Decision Theory (A-FDT)

### 3.1 Subjunctive Dependence and Intervening on Decision Types
A-FDT resolves this failure by shifting the level of counterfactual intervention from the *token* (the physical act performed by an embodied agent at spacetime coordinates $(x, y, z, t)$) to the *type* (the mathematical decision function itself).

Consider two calculators executing the computation $6288 + 1048 = 7336$ in different rooms. If one calculator outputs $7336$, an observer knows with near certainty that the other will also output $7336$. This is not because the first calculator causally transmitted a physical signal to the second; rather, both physical systems implement the **same underlying mathematical function**. 

When two physical processes instantiate or simulate the same mathematical mapping, their outputs are bound by logical necessity. Yudkowsky and Soares (2017) define this relationship as **subjunctive dependence**:
$$\text{\textit{Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.}}$$

In A-FDT, the agent's world-model $M = (P, G)$ does not treat the agent's choice as an uncaused primitive. Instead, $P$ contains random variables representing the evaluations of mathematical algorithms, and $G$ contains directed edges from these mathematical nodes to all physical systems in the universe that compute, approximate, or simulate them.

### 3.2 The Primary Formal Presentation: Equation (4)
To evaluate candidate actions, the A-FDT agent does not ask: *"What if my physical muscles moved differently?"* She asks: *"What if the mathematical function I am currently implementing evaluated to a different output?"*

Formally, let $\mathbf{fdt}$ be a variable in the agent’s graphical model representing the output of the decision procedure when supplied with its current inputs: the probability model $\underline{P}$, the dependency graph $\underline{G}$, and the observation history $\underline{x}$. (Here, following Yudkowsky and Soares, an underline denotes the syntactic name or Gödel-style quoted code of the object, resolving formal self-reference via Kleene’s recursion theorem.)

Action Functional Decision Theory evaluates actions via **Equation (4), Section 5** of Yudkowsky and Soares (2017):
\begin{equation}
\mathbf{A\text{-}FDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\Big[\mathbf{V} \;\Big|\; \mathrm{do}\big(\mathbf{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\big)\Big]
\label{eq:fdt}
\end{equation}

### 3.3 The Two Structural Departures from CDT
Equation \eqref{eq:fdt} differs from Pearlian CDT \eqref{eq:cdt} in two crucial, mathematically precise ways:

1. **Target of Intervention (Type vs. Token):**
   Where CDT intervenes on the physical action variable $\mathrm{Act}$, A-FDT intervenes on the logical node $\mathbf{fdt}(\underline{P}, \underline{G}, \underline{x})$. In the causal-subjunctive graph $G$, this logical node is an ancestor not only of the agent's physical motor execution $\mathrm{Act}$, but also of any past, present, or distant processes that accurately modeled, anticipated, or mirrored that same computation. Intervening on the logical function propagates downstream along all edges departing from the function’s node, thereby updating past predictions without invoking physical backwards causation.

2. **Treatment of Observations (Node Shifting vs. Conditioning):**
   In CDT, when an observation is updated from history $x$ to $y$, the agent applies Bayesian conditioning to her post-intervention distribution:
   $$\mathbb{E}[\mathbf{V} \mid \mathrm{do}(\mathrm{Act}=a), \mathrm{Obs}=y]$$
   In A-FDT, the observation $x$ forms an explicit argument inside the function whose output is being varied:
   $$\mathbf{fdt}(\underline{P}, \underline{G}, \underline{x})$$
   When the agent's observations update from $x$ to $y$, A-FDT does *not* merely condition on $\mathrm{Obs}=y$. Rather, **A-FDT changes the locus of intervention in the graph**, shifting its surgery from $\mathbf{fdt}(\underline{P}, \underline{G}, \underline{x})$ to $\mathbf{fdt}(\underline{P}, \underline{G}, \underline{y})$. 
   
   This distinction is profound: it allows an A-FDT agent to evaluate hypotheticals where an alternative choice would have caused an accurate predictor to supply a completely different observation history in the first place.

---

## 4. Applying A-FDT to Classic Decision Problems

We trace the formal evaluation of Equation \eqref{eq:fdt} across canonical decision environments, demonstrating how A-FDT extracts maximal utility.

### 4.1 Newcomb's Problem
In Newcomb’s Problem, the predictor's past prediction $\mathrm{Prediction} \in \{1, 2\}$ was determined by simulating the agent's decision procedure. Box $B$ was filled with $\$1,000,000$ if $\mathrm{Prediction}=1$ (predicting one-box), and $\$0$ if $\mathrm{Prediction}=2$.

The A-FDT graph $G^F$ is structured as follows:
* The root node is the logical function evaluation $\mathbf{fdt}(\underline{P^F}, \underline{G^F})$.
* Directed edges run from $\mathbf{fdt}(\underline{P^F}, \underline{G^F})$ to both $\mathrm{Act} \in \{\mathrm{onebox}, \mathrm{twobox}\}$ and $\mathrm{Prediction} \in \{1, 2\}$.
* An independent noise node $\mathrm{Accurate} \in \{\mathrm{acc}, \mathrm{inacc}\}$ inputs into $\mathrm{Prediction}$, with $P(\mathrm{Accurate}=\mathrm{acc}) = 0.99$.
* $\mathrm{Prediction} \to \mathrm{Box\ B}$, where $\mathrm{Box\ B}(1) = \mathrm{full}$ and $\mathrm{Box\ B}(2) = \mathrm{empty}$.
* Both $\mathrm{Act}$ and $\mathrm{Box\ B}$ feed into $\mathrm{Outcome}$, which determines utility $\mathbf{V}$.

To evaluate Equation \eqref{eq:fdt}, Fiona (the A-FDT agent) evaluates two hypotheticals:

1. **Hypothetical 1:** $\mathrm{do}(\mathbf{fdt}(\underline{P^F}, \underline{G^F}) = \mathrm{onebox})$
   * By graph propagation, $\mathrm{Act} = \mathrm{onebox}$.
   * Under the predictor's reliability, $\mathrm{Prediction} = 1$ with probability $0.99$, and $\mathrm{Prediction} = 2$ with probability $0.01$.
   * Consequently, $\mathrm{Box\ B} = \mathrm{full}$ with probability $0.99$.
   * Expected utility:
     $$\mathbb{E}\big[\mathbf{V} \mid \mathrm{do}(\mathbf{fdt} = \mathrm{onebox})\big] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000$$

2. **Hypothetical 2:** $\mathrm{do}(\mathbf{fdt}(\underline{P^F}, \underline{G^F}) = \mathrm{twobox})$
   * By graph propagation, $\mathrm{Act} = \mathrm{twobox}$.
   * $\mathrm{Prediction} = 2$ with probability $0.99$, and $\mathrm{Prediction} = 1$ with probability $0.01$.
   * Consequently, $\mathrm{Box\ B} = \mathrm{empty}$ with probability $0.99$.
   * Expected utility:
     $$\mathbb{E}\big[\mathbf{V} \mid \mathrm{do}(\mathbf{fdt} = \mathrm{twobox})\big] = 0.99(\$1,000) + 0.01(\$1,001,000) = \$11,000$$

Since $\$990,000 > \$11,000$, Equation \eqref{eq:fdt} yields:
$$\mathbf{A\text{-}FDT}(P^F, G^F) = \mathrm{onebox}$$
The predictor, simulating this exact derivation, predicts $\mathrm{onebox}$, fills box $B$, and Fiona walks away with $\$1,000,000$.

### 4.2 The Psychological Twin Prisoner's Dilemma
Two identical psychological twins, separated in isolated rooms, must choose to $\mathrm{cooperate}$ or $\mathrm{defect}$. The payout matrix (in utility) is:
* Both cooperate: $\$1,000,000$ each.
* Both defect: $\$1,000$ each.
* One defects, one cooperates: Defector gets $\$1,001,000$; cooperator gets $\$0$.

CDT defects because the twin's physical action is causally disconnected across space; defection causally dominates. 

Under A-FDT, the dependency graph $G$ routes directed edges from a single logical variable, $\mathbf{fdt}(\underline{P}, \underline{G})$, to *both* $\mathrm{Act}_1$ (the agent's act) and $\mathrm{Act}_2$ (the twin's act). 
* Under $\mathrm{do}(\mathbf{fdt} = \mathrm{cooperate})$, graph propagation forces $\mathrm{Act}_1 = \mathrm{cooperate}$ and $\mathrm{Act}_2 = \mathrm{cooperate}$, yielding $\mathbb{E}[\mathbf{V}] = \$1,000,000$.
* Under $\mathrm{do}(\mathbf{fdt} = \mathrm{defect})$, graph propagation forces $\mathrm{Act}_1 = \mathrm{defect}$ and $\mathrm{Act}_2 = \mathrm{defect}$, yielding $\mathbb{E}[\mathbf{V}] = \$1,000$.

Equation \eqref{eq:fdt} straightforwardly selects $\mathrm{cooperate}$. A-FDT cooperates without assuming telepathy or retrocausality: the correlation is underwritten by the mathematical identity of the algorithms computed in both rooms.

### 4.3 The Smoking Lesion Problem
In the smoking lesion problem, an unobserved arterial lesion causes both cancer ($99\%$ probability) and a preference for smoking. Lacking the lesion, baseline cancer risk is $1\%$. Smoking confers an unconditional surplus of $\$1,000$; avoiding cancer is worth $\$1,000,000$.

Why does A-FDT smoke, avoiding the trap of EDT?
Crucially, cancer does not read, predict, or implement the agent's decision function. A biological lesion is not a predictor: it has no computational model of $\mathbf{fdt}$.

In Fiona's graph $G^F$ (formalized in Yudkowsky & Soares 2017, Section 6), whether the agent has the lesion determines which utility function is active: $\mathcal{U}_S$ (smoker preferences) or $\mathcal{U}_R$ (non-smoker preferences). There are two candidate decision functions: $\mathbf{fdt}(\underline{P_S^F}, \underline{G^F})$ and $\mathbf{fdt}(\underline{P_R^F}, \underline{G^F})$. The node $\mathrm{Lesion}$ is an exogenous root node; directed edges go from $\mathrm{Lesion} \to \mathrm{Cancer}$ and $\mathrm{Lesion} \to \mathrm{Act}$.

When evaluating $\mathrm{do}(\mathbf{fdt}(\underline{P_S^F}, \underline{G^F}) = \mathrm{smoke})$ versus $\mathrm{do}(\mathbf{fdt}(\underline{P_S^F}, \underline{G^F}) = \mathrm{refrain})$, the surgery severs the incoming connection to the decision execution. Because there is **no directed path from $\mathbf{fdt}$ to $\mathrm{Lesion}$ or $\mathrm{Cancer}$**, Pearl's graph surgery yields:
$$P\big(\mathrm{Lesion} \mid \mathrm{do}(\mathbf{fdt} = \mathrm{smoke})\big) = P\big(\mathrm{Lesion} \mid \mathrm{do}(\mathbf{fdt} = \mathrm{refrain})\big) = P(\mathrm{Lesion}) = p$$
The probability of cancer remains completely invariant across both hypotheticals. The expected utilities evaluate to:
$$\mathbb{E}\big[\mathbf{V} \mid \mathrm{do}(\mathbf{fdt}=\mathrm{smoke})\big] = p(\$10,000 + \$1,000) + (1-p)(\$990,000 + \$1,000)$$
$$\mathbb{E}\big[\mathbf{V} \mid \mathrm{do}(\mathbf{fdt}=\mathrm{refrain})\big] = p(\$10,000) + (1-p)(\$990,000)$$
Smoking yields an exact expected gain of $\$1,000$. Fiona smokes. 

A-FDT therefore achieves the dual desiderata that Gibbard and Harper deemed impossible: it one-boxes in Newcomb's problem because the predictor tracks the decision function, and it smokes in the smoking lesion problem because the lesion does not.

---

## 5. Counterpossibles, Observations, and Updatelessness

### 5.1 The Logic of Counterpossibles
The core mathematical challenge of A-FDT lies in its counterfactual antecedents. If an algorithm $\mathbf{fdt}$ on a specific input $(P, G, x)$ outputs $\mathrm{onebox}$, it does so by mathematical necessity. The hypothetical:
$$\mathbf{fdt}(\underline{P}, \underline{G}, \underline{x}) = \mathrm{twobox}$$
is an antecedent that is logically impossible—a **counterpossible**. 

In conventional possible-world semantics, an impossible proposition entails everything (ex falso quodlibet), collapsing expected utility calculations. A-FDT resolves this by bypassing the need for a generalized philosophical logic of counterpossibles. Instead, it embeds the logical function as an explicit node within a Pearlian causal-subjunctive network $G$. 

By applying Pearl's graph surgery $\mathrm{do}(\mathbf{fdt} = a)$, A-FDT operationalizes the counterpossible: it forcibly treats the logical node as a localized variable, propagates the substitution down all departing graph edges, and holds non-descendants fixed.

### 5.2 The Transparent Newcomb Problem: Shifting the Interventional Node
The radical power of A-FDT is most evident in the **Transparent Newcomb Problem** (Drescher 2006). Here, both boxes are transparent: the agent directly observes whether box $B$ is full before making her choice. The predictor placed $\$1,000,000$ in box $B$ if and only if she predicted that the agent would leave box $A$ behind *upon seeing both boxes full*.

When Fiona faces two full boxes, her observation is $x = \mathrm{full}$.
* **CDT's response:** Carl conditions on $\mathrm{Obs}=\mathrm{full}$ and intervenes via $\mathrm{do}(\mathrm{Act}=a)$. Box $B$ is already physically full; taking box $A$ nets $\$1,001,000$ versus $\$1,000,000$. Carl two-boxes. Foreseeing this, the predictor leaves box $B$ empty.
* **EDT's response:** Eve conditions on $\mathrm{Obs}=\mathrm{full}$. Given that box $B$ is already observed to be full, conditioning on two-boxing yields $\$1,001,000$, while one-boxing yields $\$1,000,000$. Eve also two-boxes, and likewise finds box $B$ empty.

**A-FDT's response:** Under Equation \eqref{eq:fdt}, Fiona does not condition on $\mathrm{Obs}=\mathrm{full}$. Instead, the observation $x = \mathrm{full}$ dictates that she must intervene on the node:
$$\mathbf{fdt}(\underline{P^F}, \underline{G^F}, \mathrm{full})$$
In Fiona's graph $G^F$ (Figure 5b in Yudkowsky & Soares 2017), the predictor’s prediction is a descendant of the full-observation policy node:
$$\mathbf{fdt}(\underline{P^F}, \underline{G^F}, \mathrm{full}) \longrightarrow \mathrm{Prediction} \longrightarrow \mathrm{Box\ B} \longrightarrow \mathrm{Obs}$$

When Fiona considers the hypothetical action $a = \mathrm{twobox}$, she computes:
$$\mathbb{E}\Big[\mathbf{V} \;\Big|\; \mathrm{do}\big(\mathbf{fdt}(\underline{P^F}, \underline{G^F}, \mathrm{full}) = \mathrm{twobox}\big)\Big]$$
In this hypothetical, the intervention propagates to $\mathrm{Prediction} = 2$, which means $\mathrm{Box\ B} = \mathrm{empty}$. If the box is empty, the agent would never have observed $\mathrm{full}$ in the first place; she would have been shunted to the empty-box decision node $\mathbf{fdt}(\dots, \mathrm{empty})$! 

Fiona recognizes that the counterfactual world in which her full-box procedure outputs $\mathrm{twobox}$ is a world where the box is empty with $99\%$ probability, yielding a paltry expected payout. Conversely, the hypothetical where her full-box procedure outputs $\mathrm{onebox}$ yields $\$1,000,000$ with $99\%$ probability. 

Fiona **one-boxes even while looking at the full box**. Because she reliably implements this logic, the predictor foresees it, fills the box, and Fiona collects $\$1,000,000$. As Yudkowsky and Soares note, Parfit’s desert is littered with the corpses of CDT and EDT agents who could not resist the temptation to take the extra thousand.

### 5.3 Updateless Behavior Without Global Policy Search
This behavior illustrates the "updateless" property of A-FDT (originating in Wei Dai’s Updateless Decision Theory [2009]). Standard agents update their probabilities upon receiving evidence and maximize utility relative to the posterior state. This makes them vulnerable to dynamic inconsistency: they fail in problems like **Parfit's Hitchhiker** (Parfit 1986), where an agent stranded in a desert must promise to pay $\$1,000$ upon reaching the city. Once safely in the city, CDT and EDT agents renege because the ride has already been provided; the driver predicts this and leaves them to die.

A-FDT achieves dynamic consistency without requiring binding precommitments. Crucially, **A-FDT achieves this without having to globally search over whole policies** (mappings $\pi: \mathcal{X} \to \mathcal{A}$). In Yudkowsky and Soares (2017), Section 5, Footnotes 7 and 16 acknowledge that while the authors' preferred background theory evaluates whole policies, Equation \eqref{eq:fdt} is strictly an **action-interventional** formula. 

It achieves updateless consistency entirely through the syntactic mechanism of shifting the targeted intervention node $\mathbf{fdt}(\underline{P}, \underline{G}, \underline{x})$ as a function of the observation history $x$.

---

## 6. Resolving Dynamic Instability and Resisting Blackmail

### 6.1 Death in Damascus: Escaping the Ratification Trap
In the **Death in Damascus** dilemma (Gibbard & Harper 1978), Death predicts where the agent will be tomorrow morning (Damascus or Aleppo) and waits there. Fleeing to Aleppo costs $\$1,000$; staying in Damascus costs $\$0$. Dying costs $\$1,000,000$.

CDT experiences severe reflective instability:
* If Carl expects to stay in Damascus, Death is predicted to be in Damascus. Causal intervention $\mathrm{do}(\mathrm{Act}=\mathrm{Aleppo})$ shows an expected survival utility of $\$1,000,000 - \$1,000 = \$999,000$. Carl decides to flee to Aleppo.
* Once Carl decides to flee to Aleppo, his expectation shifts: Death will be in Aleppo. Now causal intervention $\mathrm{do}(\mathrm{Act}=\mathrm{Damascus})$ shows an expected utility of $\$1,000,000$, prompting him to switch back.

CDT either enters an infinite loop or falls back on mixed-strategy ratification procedures (Joyce 2012; Arntzenius 2008), settling on an indifferent mixed state where the agent spends $\$1,000$ to flee roughly half the time, dying with certainty while acting as though he has a $50\%$ chance of life.

A-FDT resolves the problem instantly:
Fiona’s graph models Death’s appointment book as a descendant of $\mathbf{fdt}(\underline{P}, \underline{G})$:
$$\mathbf{fdt}(\underline{P}, \underline{G}) \longrightarrow \mathrm{Death's\ Book} \longrightarrow \mathrm{Death's\ Location}$$
* Under $\mathrm{do}(\mathbf{fdt} = \mathrm{Damascus})$, Death is in Damascus; utility is $-\$1,000,000$.
* Under $\mathrm{do}(\mathbf{fdt} = \mathrm{Aleppo})$, Death is in Aleppo; utility is $-\$1,000,000 - \$1,000 = -\$1,001,000$.

Equation \eqref{eq:fdt} deterministically selects $\mathrm{Damascus}$. Fiona recognizes that death is unavoidable and saves the $\$1,000$ travel expense, spending her final night with loved ones rather than on camelback.

### 6.2 The Mechanical Blackmail
In the **Mechanical Blackmail** (Soares & Fallenstein 2015), an automated extortion program runs if and only if an accurate predictor predicts that the agent will pay $\$1,000$ upon receiving a blackmail letter. If the program runs and the agent refuses to pay, a devastating leak costing $\$1,000,000$ is published automatically.

Suppose the agent receives the letter:
* CDT and EDT agents pay. The program is already running; paying $\$1,000$ prevents a $\$1,000,000$ catastrophe. Predictors anticipate this, meaning CDT and EDT agents are systematically extorted throughout their lifetimes.
* Fiona (A-FDT), holding the letter, evaluates:
  $$\mathrm{do}\big(\mathbf{fdt}(\underline{P^F}, \underline{G^F}, \mathrm{letter}) = \mathrm{refuse}\big)$$
  In this hypothetical, the blackmailer’s simulation predicts refusal, meaning the blackmail program was **never run in the first place**, and no letter was sent. 

Because the hypothetical of refusing corresponds to an un-blackmailed world (utility $\$0$) whereas paying corresponds to an extorted world (utility $-\$1,000$), Equation \eqref{eq:fdt} outputs $\mathrm{refuse}$. The blackmailer predicts this, runs no program, and Fiona is never blackmailed.

---

## 7. Open Mathematical and Conceptual Problems

While A-FDT demonstrates extraordinary performance across traditional paradoxes, it relies on foundational assumptions that Yudkowsky and Soares leave open. As researchers applying or extending the theory, we must clearly separate the claims formally established in the source paper from the open questions requiring further mathematical development.

### 7.1 Deducing Subjunctive Graphs from Experience
The most glaring asymmetry between CDT and A-FDT is epistemological:
* In CDT, Pearl (2000) provides a robust algorithmic theory for inducing causal DAGs from conditional independence tests, observational data, and physical interventions.
* In A-FDT, Equation \eqref{eq:fdt} operates only **given a pre-existing graph $G$** that accurately captures subjunctive dependencies. 

The source document explicitly acknowledges that there is currently **no formal calculus for inducing subjunctive graphs from raw observational data**. When does a correlation between a decision function and an environmental variable qualify as a directed subjunctive edge, and when is it a mere coincidence? 

A proposed research program to formalize this involves **algorithmic information theory and program analysis**:
* Let $M_{\mathrm{env}}$ be a program simulating the environment, and let $M_{\mathrm{agent}}$ be the agent's source code.
* If the shortest program $M_{\mathrm{env}}$ contains a non-trivial computational sub-routine provably equivalent to or bisimilar with $M_{\mathrm{agent}}$ (e.g., via Rice's theorem or bounded proof searches), a subjunctive dependency edge $M_{\mathrm{agent}} \to M_{\mathrm{env}}$ is established.
* If the correlation between the agent's act and an event can be explained by a shorter hypothesis that does not simulate $M_{\mathrm{agent}}$ (as in the smoking lesion), no subjunctive edge exists.

### 7.2 The Problem of Upstream Interventions and Algorithmic Counterpossibles
In Pearl’s causal networks, executing $\mathrm{do}(X = x)$ severs the arrows incoming to $X$, treating $X$ as an exogenous variable. But what does it mean to sever the inputs to a *mathematical function*?

If $\mathbf{fdt}(\underline{P}, \underline{G}, \underline{x})$ is a deterministic algorithm, its output is fixed by mathematical axioms (e.g., Peano Arithmetic or ZFC). An intervention $\mathrm{do}(\mathbf{fdt} = a)$ when the true output is $b \neq a$ posits a local violation of logic. 

If this logical counterfactual is not tightly quarantined, proof systems collapse into triviality. Developing a mathematically rigorous framework of **probabilistic logic under bounded reflection** (such as Gaifman 2004; Demski 2012; Hutter et al. 2013) that stably integrates Pearlian interventions remains one of the primary frontiers of theoretical computer science.

---

## 8. Summary Comparison of Decision Algorithms

To synthesize the operational prescriptions across the formal frameworks, the following table compares how EDT, CDT, and A-FDT evaluate the canonical dilemmas discussed:

| Dilemma | Evidential Decision Theory (EDT) | Causal Decision Theory (CDT) | Action Functional Decision Theory (A-FDT) |
| :--- | :--- | :--- | :--- |
| **Formal Rule** | $\argmax_a \mathbb{E}[\mathbf{V} \mid x, a]$ | $\argmax_a \mathbb{E}[\mathbf{V} \mid \mathrm{do}(\mathrm{Act}=a), x]$ | $\argmax_a \mathbb{E}[\mathbf{V} \mid \mathrm{do}(\mathbf{fdt}(\underline{P}, \underline{G}, \underline{x})=a)]$ |
| **Target of Surgery** | None (pure conditioning) | Token: physical act $\mathrm{Act}$ | Type: logical function $\mathbf{fdt}$ |
| **Newcomb’s Problem** | **One-boxes** ($\$1,000,000$) | **Two-boxes** ($\$1,000$) | **One-boxes** ($\$1,000,000$) |
| **Smoking Lesion** | **Refrains** (loses $\$1,000$) | **Smokes** (gains $\$1,000$) | **Smokes** (gains $\$1,000$) |
| **Twin Prisoner's Dilemma** | Cooperates | Defects | Cooperates |
| **Transparent Newcomb** | Two-boxes ($\$0$) | Two-boxes ($\$0$) | **One-boxes** ($\$1,000,000$) |
| **Parfit’s Hitchhiker** | Refuses to pay (dies) | Refuses to pay (dies) | **Pays** (rescued and lives) |
| **Death in Damascus** | Flees or dies in distress | Reflectively unstable / mixed coin | **Stays in Damascus** (saves $\$1,000$) |
| **Mechanical Blackmail** | Pays blackmail | Pays blackmail | **Refuses** (blackmail avoided) |

---

## 9. Conclusion

Action Functional Decision Theory (A-FDT) redefines normative decision theory by rejecting the assumption that an agent's intervention must be localized to a physical event in spacetime. By recognizing that physical agents instantiate invariant mathematical functions, A-FDT expands Pearl's interventional toolkit to encompass subjunctive, predictive, and logical structures.

Through Equation \eqref{eq:fdt}, A-FDT provides a mathematically precise, non-ad-hoc criterion that bridges the historical divide between CDT and EDT. It extracts the benefits of causal interventionism—refusing to fall victim to the spurious correlations that plague EDT in the smoking lesion and cosmic ray problems—while natively accommodating the predictive dependencies that reduce CDT to poverty in Newcombian dilemmas, Parfit's desert, and extortion markets. 

While important mathematical questions remain regarding the automated discovery of subjunctive graphs and the formal logic of counterpossibles, A-FDT stands as a powerful and mathematically coherent model of instrumental rationality for artificial and human intelligence alike.

---

## References

* Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
* Ahmed, A. (2014b). Dicing with Death. *Analysis*, 74(4), 587–592.
* Arntzenius, F. (2008). No Regrets, or: Edith Piaf Revamps Decision Theory. *Erkenntnis*, 68(2), 277–297.
* Dai, W. (2009). Towards a New Decision Theory. *LessWrong*.
* Demski, A. (2012). Logical Prior Probability. *Artificial General Intelligence (AGI 2012)*, LNCS 7716, 50–59.
* Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Eells, E. (1984). Metatickles and the Dynamics of Deliberation. *Theory and Decision*, 17(1), 71–95.
* Gaifman, H. (2004). Reasoning with Limited Resources and Assigning Probabilities to Arithmetical Statements. *Synthese*, 140(1–2), 97–119.
* Gibbard, A., & Harper, W. L. (1978). Counterfactuals and Two Kinds of Expected Utility. In *Foundations and Applications of Decision Theory* (pp. 125–162). D. Reidel.
* Hutter, M., Lloyd, J. W., Ng, K. S., & Uther, W. T. B. (2013). Probabilities on Sentences in an Expressive Logic. *Journal of Applied Logic*, 11(4), 386–420.
* Jeffrey, R. C. (1983). *The Logic of Decision* (2nd ed.). University of Chicago Press.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Joyce, J. M. (2012). Regret and Instability in Causal Decision Theory. *Synthese*, 187(1), 123–145.
* Kleene, S. C. (1938). On Notation for Ordinal Numbers. *Journal of Symbolic Logic*, 3(4), 150–155.
* Lewis, D. (1979). Prisoners' Dilemma is a Newcomb Problem. *Philosophy & Public Affairs*, 8(3), 235–240.
* Lewis, D. (1981). Causal Decision Theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
* Nozick, R. (1969). Newcomb's Problem and Two Principles of Choice. In *Essays in Honor of Carl G. Hempel* (pp. 114–146). D. Reidel.
* Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
* Pearl, J. (1996). Causation, Action, and Counterfactuals. In *Theoretical Aspects of Rationality and Knowledge (TARK '96)* (pp. 51–73). Morgan Kaufmann.
* Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Skyrms, B. (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Soares, N., & Fallenstein, B. (2015). Toward Idealized Decision Theory. *arXiv:1507.01986*.
* Yudkowsky, E., & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. *arXiv:1710.05060v2*.