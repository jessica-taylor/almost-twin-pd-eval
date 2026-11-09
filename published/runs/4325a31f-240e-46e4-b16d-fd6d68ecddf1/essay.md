# The Logic of Subjunctive Interventions: A Mathematical Account of Action Functional Decision Theory (A-FDT)

## 1. Introduction: Beyond the Causal–Evidential Stalemate

For decades, normative decision theory has been polarized between two major paradigms: **Evidential Decision Theory (EDT)** and **Causal Decision Theory (CDT)**. The fault line separating them is classically revealed in Newcomb-like dilemmas. EDT prescribes actions that serve as the best evidence for favorable outcomes, evaluating an action $a$ by the conditional expectation $\mathbb{E}[V \mid a]$. CDT insists that correlation is not causation: a rational agent must evaluate an action based on what it physically brings about, formalized via causal interventions that sever upstream correlations.

Both theories exhibit systematic pathologies:
* **EDT** is prone to irrational "news-managing." In Skyrms' classic Smoking Lesion problem or Soares and Fallenstein's XOR Blackmail dilemma, EDT confuses mere diagnostic correlation with efficacy. Under extreme priors or unratified beliefs, EDT agents can be extorted or induced to act against their own interests simply to avoid receiving bad news.
* **CDT** behaves dysfunctionally when the environment contains other systems—such as predictors, algorithms, psychological twins, or compilers—that model or share the agent’s reasoning. In Newcomb's Problem, Carl (the canonical CDT agent) leaves $\$1{,}000{,}000$ on the table because the predictor has already filled or emptied Box B. In Parfit’s Hitchhiker, CDT cannot motivate an agent to pay a driver after being rescued, guaranteeing that a discerning driver leaves the agent to die in the desert. In deterministic dilemmas like Death in Damascus, CDT suffers from radical instability and cyclical regret.

To resolve this dilemma, Yudkowsky and Soares introduce **Functional Decision Theory (FDT)**. When formulated to select actions directly under a given observation history, the theory operates as **Action Functional Decision Theory (A-FDT)**. The core normative thesis of A-FDT is:

> *A rational agent evaluates an action not as an isolated physical intervention on an act-token, nor as an epistemic conditioning event, but as the mathematical output of the very decision algorithm the agent is currently executing.*

Where CDT asks, *"What physical effects are caused if my physical body executes act $a$?"*, and EDT asks, *"What is my expected utility conditional on learning I did act $a$?"*, A-FDT asks:

$$\text{\emph{``Which output of this very mathematical decision function yields the best outcome?''}}$$

This essay presents a self-contained, mathematically rigorous exposition of A-FDT. We examine its primary formalization via graphical models, trace how it constructs counterfactuals through *subjunctive dependence*, work through canonical decision problems step-by-step, and analyze the open formal challenges at the interface of causal graphs, self-reference, and counterpossible logic.

---

## 2. Foundations and Formal Framework

### 2.1 The General Expected Utility Architecture

Following Gibbard and Harper (1978) and the axiomatic representation theorem of Joyce (1999), expected utility theories share a common evaluation formula:

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \then o_j ;\, x) \cdot \mathcal{U}(o_j) \tag{1}$$

where:
* $\mathcal{A}$ is a finite set of available actions ($a \in \mathcal{A}$).
* $\mathcal{X}$ is a countable set of observation histories ($x \in \mathcal{X}$).
* $\mathcal{O} = \{o_1, o_2, \ldots\}$ is a countable set of mutually exclusive, exhaustive outcomes.
* $\mathcal{U}: \mathcal{O} \to \mathbb{R}$ is a utility function bounded such that expectations converge.
* $V \coloneqq \mathcal{U}(\textsc{Outcome})$ is the random variable representing realized utility.
* $a \then o_j$ denotes the decision hypothetical: the connective asserting that outcome $o_j$ would obtain if action $a$ were chosen under history $x$.

As Joyce demonstrated, the foundational axioms of expected utility theory do not dictate the metaphysical semantics of "$\then$". Rather, they leave the mapping from beliefs to decision hypotheticals as an open epistemic parameter. The three competing theories construct this conditional differently:

1. **EDT** equates hypotheticals with Bayesian conditionalization:
   $$P_{\text{EDT}}(a \then o_j ;\, x) \coloneqq P(o_j \mid x, a)$$
   leading to the decision rule:
   $$\operatorname{EDT}(P, x) \coloneqq \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}[V \mid \textsc{Obs}=x, \textsc{Act}=a] \tag{2}$$

2. **CDT** constructs hypotheticals via Pearl's causal intervention operator $\operatorname{do}(\textsc{Act} = a)$ over a directed acyclic graph (DAG) $G$ representing physical causation:
   $$P_{\text{CDT}}(a \then o_j ;\, x) \coloneqq P(o_j \mid \operatorname{do}(\textsc{Act}=a), \textsc{Obs}=x)$$
   yielding:
   $$\operatorname{CDT}(P, G, x) \coloneqq \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}[V \mid \operatorname{do}(\textsc{Act}=a), \textsc{Obs}=x] \tag{3}$$

---

### 2.2 Formal Specification of A-FDT: Equation (4)

A-FDT departs from CDT in two fundamental ways:
1. **The locus of intervention**: Rather than intervening on the physical token variable $\textsc{Act}$, A-FDT intervenes on the *logical variable* that represents the output of the mathematical decision function itself.
2. **The treatment of observation**: CDT conditions on observations $\textsc{Obs}=x$ via standard probability kinematics. In contrast, A-FDT treats the observation history $x$ as an argument to its mathematical decision algorithm, shifting the specific node in the dependency network upon which the agent intervenes.

Formally, let $P$ be a probability distribution defined over a space of variables that includes physical states, observation histories, environmental predictors, and variables designating the outputs of mathematical functions. Let $G$ be an augmented dependency graph encoding both physical causation and logical/subjunctive dependencies.

Let $\texttt{fdt}$ denote the mathematical function implementing A-FDT. The expression $\texttt{fdt}(\underline{P}, \underline{G}, \underline{x})$ denotes a specific node in $G$ corresponding to the output of the function $\texttt{fdt}$ evaluated on the representations (or "quoted" descriptions) of the model components $P, G$ and observation string $x$. 

The foundational decision rule of **Action Functional Decision Theory (A-FDT)** is given by **Equation (4)**:

$$\operatorname{FDT}(P, G, x) \coloneqq \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}\Big[ V \;\Big|\; \operatorname{do}\big(\texttt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\big) \Big] \tag{4}$$

#### Dequoting and Harmless Self-Reference
In Equation (4), the underlined notation $\underline{P}, \underline{G}, \underline{x}$ indicates the syntactic encoding or Gödel number of the agent’s own probabilistic world-model, its dependency graph, and its observation history. 

This formalization relies on the agent containing a variable inside its model that refers to the evaluation of its own code. While this introduces explicit self-reference, it is mathematically coherent by virtue of **Kleene's Second Recursion Theorem** (Kleene 1938). By applying a standard quining mechanism, an algorithm $\texttt{fdt}$ can inspect and manipulate an exact description of its own source code and world-model without triggering non-terminating regress. 

Crucially, the agent does not need to *precompute* the output of $\texttt{fdt}(\underline{P}, \underline{G}, \underline{x})$ before setting up the equation; it merely requires a formal symbol in $G$ whose structural relations to other variables (such as an external predictor's mental model) are well-defined.

---

## 3. Subjunctive Dependence vs. Causal and Statistical Dependence

To compute Equation (4), one must understand what happens when Pearl's $\operatorname{do}$-operator is applied to a logical variable. In standard causal modeling (Pearl 2000), $\operatorname{do}(X = x)$ represents an idealized physical manipulation: it replaces the structural equation determining $X$ with the constant $x$, cutting all incoming edges to $X$ in $G$, while propagating the value $x$ downstream along all outgoing edges according to the structural equations of the descendants.

In A-FDT, the graph $G$ represents **subjunctive dependencies**. Subjunctive dependence subsumes causal dependence as a special case, but extends fundamentally to mathematical, algorithmic, and logical relations:

$$\text{Causal Dependence} \subsetneq \text{Subjunctive Dependence}$$
$$\text{Statistical Correlation} \not\subseteq \text{Subjunctive Dependence}$$

```
                +-------------------------------------------------+
                |             Subjunctive Dependence              |
                |  (Invariance under changes to function outputs) |
                |                                                 |
                |   +-----------------------+                     |
                |   |   Causal Dependence   |   Predictive/Twin   |
                |   | (Physical mechanisms) |     Symmetries      |
                |   +-----------------------+                     |
                +-------------------------------------------------+
                                         ^
                                         | (A-FDT tracks this boundary)
                +-------------------------------------------------+
                |             Statistical Correlation             |
                |       (Mere observational co-occurrence:        |
                |        lesions, common causes, coincidences)    |
                +-------------------------------------------------+
```

### The Multi-Calculator Analogy
Suppose two calibrated hardware calculators, $C_1$ in Paris and $C_2$ in Tokyo, are programmed to calculate the arithmetic sum $6288 + 1048$.
* **Causal perspective**: There is no direct causal wire running between $C_1$ and $C_2$. If an experimenter physically forces the display segments of $C_1$ to read $0000$ with an electromagnet, $C_2$ continues to output $7336$.
* **Subjunctive perspective**: The internal states of both calculators are physical tokens that instantiate the same abstract mathematical function:
  $$f(x, y) = x + y$$
  When an engineer asks, *"What would $C_2$ output if $f(6288, 1048)$ evaluated to $7337$?"*, the correct subjunctive answer is that $C_2$ would also output $7337$. The behaviors of $C_1$ and $C_2$ subjunctively depend upon the logical output of the function $f$.
* **Mere correlation**: If $C_1$ is painted blue and $C_2$ happens to be blue, altering the paint on $C_1$ has no subjunctive bearing on $C_2$.

A-FDT operates by intervening on the **type** (the algorithm $\texttt{fdt}$) rather than the **token** (the physical actuator $\textsc{Act}$). When an agent considers an alternative action $a$, it does not imagine a physical miracle violating the laws of physics at the level of its motor neurons; it evaluates a logical counterfactual: 

$$\text{\emph{What would the universe look like if the function }} \texttt{fdt}(\underline{P}, \underline{G}, \underline{x}) \text{\emph{ had evaluated to }} a\text{\emph{?}}$$

---

## 4. Operationalizing A-FDT in Benchmark Decision Dilemmas

To see how Equation (4) operates mathematically, we contrast the behavior of three formal agents: **Eve** (EDT, Equation 2), **Carl** (CDT, Equation 3), and **Fiona** (A-FDT, Equation 4).

### 4.1 Newcomb's Problem

An agent faces Box A (transparent, containing $\$1{,}000$) and Box B (opaque, containing $\$1{,}000{,}000$ or $\$0$). A predictor with 99% accuracy has already placed $\$1{,}000{,}000$ in Box B if and only if she predicted the agent leaves Box A behind. The agent may take both boxes ($\textit{twobox}$) or only Box B ($\textit{onebox}$).

#### The Graph Structures
* **Carl's Graph ($G^C$)**: Carl models his physical action $\textsc{Act} \in \{\textit{onebox}, \textit{twobox}\}$ as an effect of his prior mental predisposition, while $\textsc{Prediction} \to \textsc{Box B}$ was fixed yesterday. The intervention $\operatorname{do}(\textsc{Act}=a)$ severs the edge $\textsc{Predisposition} \to \textsc{Act}$. Because $\textsc{Box B}$ is not causally downstream of $\textsc{Act}$, its marginal distribution is invariant under $\operatorname{do}(\textsc{Act}=a)$:
  $$\mathbb{E}_{P^C}[V \mid \operatorname{do}(\textsc{Act}=\textit{twobox})] - \mathbb{E}_{P^C}[V \mid \operatorname{do}(\textsc{Act}=\textit{onebox})] = \$1{,}000$$
  Carl two-boxes, earning $\$1{,}000$ in expectation.

* **Fiona's Graph ($G^F$)**: Fiona recognizes that the predictor's simulation and her own decision are physical processes running the same decision function $\texttt{fdt}(\underline{P^F}, \underline{G^F})$. In $G^F$, the node $\texttt{fdt}(\underline{P^F}, \underline{G^F})$ is an ancestor of *both* $\textsc{Act}$ and $\textsc{Prediction}$.

```
                 +----------------------------+
                 |    fdt(P^F, G^F) [Node]    |
                 +----------------------------+
                    /                      \
                   /                        \
                  v                          v
          +---------------+          +----------------+
          |      Act      |          |   Prediction   |
          +---------------+          +----------------+
                  \                          |
                   \                         v
                    \                 +----------------+
                     \                |     Box B      |
                      \               +----------------+
                       \                     /
                        v                   v
                    +---------------------------+
                    |      Outcome / Utility    |
                    +---------------------------+
```

#### Step-by-Step Evaluation via Equation (4)
Fiona evaluates:
$$\operatorname{FDT}(P^F, G^F) = \operatorname{argmax}_{a \in \{\textit{onebox}, \textit{twobox}\}} \mathbb{E}\Big[ V \;\Big|\; \operatorname{do}\big(\texttt{fdt}(\underline{P^F}, \underline{G^F}) = a\big) \Big]$$

1. **Hypothetical 1: $\operatorname{do}(\texttt{fdt} = \textit{onebox})$**
   The surgery sets $\texttt{fdt} = \textit{onebox}$. Propagating downstream:
   $$P^F(\textsc{Act} = \textit{onebox} \mid \operatorname{do}(\texttt{fdt} = \textit{onebox})) = 1.0$$
   $$P^F(\textsc{Prediction} = \textit{onebox} \mid \operatorname{do}(\texttt{fdt} = \textit{onebox})) = 0.99$$
   $$P^F(\textsc{Box B} = \textit{full} \mid \operatorname{do}(\texttt{fdt} = \textit{onebox})) = 0.99$$
   The expected utility is:
   $$\mathcal{EU}(\textit{onebox}) = 0.99 \times \$1{,}000{,}000 + 0.01 \times \$0 = \$990{,}000$$

2. **Hypothetical 2: $\operatorname{do}(\texttt{fdt} = \textit{twobox})$**
   Setting $\texttt{fdt} = \textit{twobox}$:
   $$P^F(\textsc{Act} = \textit{twobox} \mid \operatorname{do}(\texttt{fdt} = \textit{twobox})) = 1.0$$
   $$P^F(\textsc{Prediction} = \textit{twobox} \mid \operatorname{do}(\texttt{fdt} = \textit{twobox})) = 0.99$$
   $$P^F(\textsc{Box B} = \textit{full} \mid \operatorname{do}(\texttt{fdt} = \textit{twobox})) = 0.01$$
   The expected utility is:
   $$\mathcal{EU}(\textit{twobox}) = 0.01 \times \$1{,}001{,}000 + 0.99 \times \$1{,}000 = \$10{,}010 + \$990 = \$11{,}000$$

Comparing the two evaluations:
$$\$990{,}000 > \$11{,}000 \implies \operatorname{FDT}(P^F, G^F) = \textit{onebox}$$

Fiona leaves the $\$1{,}000$ behind. Because the predictor foresaw this reasoning, Box B is filled, and Fiona walks away with $\$1{,}000{,}000$.

---

### 4.2 The Smoking Lesion Problem

An arterial lesion causes both an incurable lung cancer (99% probability) and a strong subjective desire to smoke. Smoking itself has no causal link to cancer, but provides an intrinsic utility of $\$1{,}000$. Cancer inflicts a penalty of $\$1{,}000{,}000$ (relative to being healthy).

* **Eve's failure (EDT)**: Eve conditions on $\textsc{Act} = \textit{smoke}$. Since smoking is diagnostic of the lesion, $P(\textsc{Lesion} \mid \textit{smoke}) \approx 1$. Eve refrains from smoking to "suppress the bad news," forfeiting the $\$1{,}000$ utility boost without altering her cancer risk.
* **Carl's success (CDT)**: Carl executes $\operatorname{do}(\textsc{Act} = \textit{smoke})$. Since $\textsc{Lesion}$ is not downstream of $\textsc{Act}$, $P(\textsc{Cancer} \mid \operatorname{do}(\textsc{Act}=a))$ is invariant across choices. Carl smokes.

#### A-FDT Formulation
How does Fiona avoid Eve’s trap? In A-FDT, subjunctive dependence tracks algorithmic structure, not mere biological correlation. The cancer does not simulate Fiona's decision algorithm to decide whether to metastasize.

Following the paper’s formalization, let Fiona’s preference structure be determined by whether the lesion is present:
* If she has the lesion ($\textit{lesion}$), her preferences are given by $\mathcal{U}_S$ (where smoking adds $\$1{,}000$).
* If she lacks the lesion ($\textit{nolesion}$), her preferences are $\mathcal{U}_R$ (where smoking is neutral or dispreferred).

Let $P^F_S$ denote her model under utility $\mathcal{U}_S$. In her graph $G^F$ (Figure 5 in the paper):
* $\textsc{Lesion} \to \textsc{Cancer} \to \textsc{Death}$
* $\textsc{Lesion} \to \textsc{Act}$
* $\texttt{fdt}(\underline{P^F_S}, \underline{G^F}) \to \textsc{Act}$
* $\texttt{fdt}(\underline{P^F_R}, \underline{G^F}) \to \textsc{Act}$

Crucially, **there is no edge** from $\texttt{fdt}(\underline{P^F_S}, \underline{G^F})$ to $\textsc{Lesion}$ or $\textsc{Cancer}$. Intervening via Equation (4):

$$P^F_S\Big(\textsc{Lesion} \;\Big|\; \operatorname{do}\big(\texttt{fdt}(\underline{P^F_S}, \underline{G^F}) = \textit{smoke}\big)\Big) = P^F_S(\textsc{Lesion}) = p$$

Because changing the output of $\texttt{fdt}$ does not subjunctively alter the biological presence of the lesion, the probability of cancer remains $0.99p + 0.01(1-p)$ under both hypotheticals. Evaluating Equation (4):

$$\mathbb{E}[V \mid \operatorname{do}(\texttt{fdt} = \textit{smoke})] - \mathbb{E}[V \mid \operatorname{do}(\texttt{fdt} = \textit{refrain})] = p \times \$1{,}000 > 0$$

Fiona smokes. A-FDT successfully distinguishes between an environmental predictor modeling an algorithm and a biological common cause correlating with desire.

---

### 4.3 The Transparent Newcomb Problem

Both boxes are transparent: the agent can visually observe whether Box B contains $\$1{,}000{,}000$ or is empty before deciding whether to take Box A. The predictor filled Box B if and only if she predicted the agent would take *only* Box B **upon seeing both boxes full**.

Suppose Fiona stands before two full boxes. Her observation history is $x = \textit{full}$.

#### The CDT and EDT Collapse
* **Carl (CDT)**: Evaluates $\mathbb{E}[V \mid \operatorname{do}(\textsc{Act}=a), \textsc{Obs}=\textit{full}]$. Box B is visibly full on the table. Taking Box A gives an unconditional extra $\$1{,}000$. Carl takes both boxes.
* **Eve (EDT)**: Conditions on $\textsc{Obs}=\textit{full}$ and $\textsc{Act}=a$. Since Box B is already known to be full, $P(\textsc{Box B}=\textit{full} \mid \textsc{Obs}=\textit{full}, \textsc{Act}=\textit{twobox}) = 1$. The news is already in; taking Box A yields an extra $\$1{,}000$. Eve takes both boxes.

Both CDT and EDT two-box. Consequently, any competent predictor predicts this, leaves Box B empty, and both agents walk away with $\$0$.

#### Fiona's A-FDT Calculation
Under A-FDT, observations are not processed merely by Bayesian conditioning. In Equation (4), the observation history $x = \textit{full}$ specifies **which node to intervene upon**:

$$\operatorname{FDT}(P^F, G^F, \textit{full}) = \operatorname{argmax}_{a} \mathbb{E}\Big[ V \;\Big|\; \operatorname{do}\big(\texttt{fdt}(\underline{P^F}, \underline{G^F}, \underline{\textit{full}}) = a\big) \Big]$$

In Fiona's graph $G^F$, the predictor’s past prediction depends on the function $\texttt{fdt}(\underline{P^F}, \underline{G^F}, \underline{\textit{full}})$. The predictor asked: *"What does Fiona’s decision procedure output when it observes a full box?"*

```
                +---------------------------------------+
                |     fdt(P^F, G^F, full) [Intervened]   |
                +---------------------------------------+
                   /                                \
                  /                                  v
                 /                           +----------------+
                /                            |   Prediction   |
               /                             +----------------+
              v                                      |
       +---------------+                             v
       |      Act      |<--------------------+ +----------------+
       +---------------+     (Determines     | |     Box B      |
              |               which fdt      | +----------------+
              v               controls Act)          |
       +---------------+                             v
       |    Outcome    |<--------------------+ +----------------+
       +---------------+                     | |   Obs = full   |
                                             | +----------------+
                                             +-------+
```

When Fiona evaluates the counterfactual $\operatorname{do}(\texttt{fdt}(\dots, \underline{\textit{full}}) = \textit{twobox})$, she evaluates a world where the procedure run upon seeing full boxes outputs $\textit{twobox}$. In that hypothetical:
1. The predictor predicts $\textit{twobox}$.
2. The predictor leaves Box B **empty**.
3. Since Box B is empty, Fiona's actual observation would have been $\textsc{Obs} = \textit{empty}$, meaning her physical actuator would have been controlled by the alternate branch $\texttt{fdt}(\dots, \underline{\textit{empty}})$.

Let $q$ be the probability that she two-boxes when seeing an empty box (where $q=1$ is optimal). Evaluating the hypotheticals with a 99% accurate predictor:

1. **If $\operatorname{do}(\texttt{fdt}(\dots, \underline{\textit{full}}) = \textit{onebox})$**:
   With probability 0.99, the predictor is accurate $\implies \textsc{Box B} = \textit{full}$, $\textsc{Act} = \textit{onebox}$, yielding $\$1{,}000{,}000$.
   With probability 0.01, the predictor errs $\implies \textsc{Box B} = \textit{empty}$, $\textsc{Act}$ is governed by $\texttt{fdt}(\dots, \underline{\textit{empty}})$, yielding $q \times \$1{,}000$.
   $$\mathcal{EU}(\textit{onebox}) = 0.99 \times \$1{,}000{,}000 + 0.01 \times q(\$1{,}000) = \$990{,}000 + \$10q$$

2. **If $\operatorname{do}(\texttt{fdt}(\dots, \underline{\textit{full}}) = \textit{twobox})$**:
   With probability 0.99, the predictor is accurate $\implies \textsc{Box B} = \textit{empty}$, yielding $0.99 \times q(\$1{,}000)$.
   With probability 0.01, the predictor errs $\implies \textsc{Box B} = \textit{full}$, yielding $0.01 \times \$1{,}001{,}000$.
   $$\mathcal{EU}(\textit{twobox}) = \$10{,}010 + \$990q$$

Since $\$990{,}000 + \$10q \gg \$10{,}010 + \$990q$ for any $q \in [0, 1]$, A-FDT selects:

$$\operatorname{FDT}(P^F, G^F, \textit{full}) = \textit{onebox}$$

Even though Box B is visibly full, Fiona takes only Box B. Her counterfactual reasoning does not ask, *"What happens if my hand grabs both boxes while the past remains unaltered?"* It asks, *"What would happen if my decision algorithm were the sort of algorithm that takes both boxes upon seeing them full?"* That hypothetical universe is one where Box B was left empty.

---

## 5. Mathematical Comparison across Decision Problems

The following table summarizes the formal prescriptions and structural behaviors of EDT, CDT, and A-FDT across canonical test cases:

| Problem | EDT (Eq. 2) | CDT (Eq. 3) | A-FDT (Eq. 4) | Underlying Mathematical Mechanism in A-FDT |
| :--- | :--- | :--- | :--- | :--- |
| **Newcomb's Problem** | One-box ($\$1\text{M}$) | Two-box ($\$1\text{K}$) | **One-box** ($\$1\text{M}$) | Predictor depends subjunctively on $\texttt{fdt}(\underline{P}, \underline{G})$. Intervention sets prediction to match act. |
| **Smoking Lesion** | Refrain ($\$0$) | Smoke ($\$1\text{K}$) | **Smoke** ($\$1\text{K}$) | No directed path from $\texttt{fdt}$ to $\textsc{Lesion}$ in $G$. Intervening on $\texttt{fdt}$ leaves cancer risk invariant. |
| **Transparent Newcomb** | Two-box ($\$0$) | Two-box ($\$0$) | **One-box** ($\$1\text{M}$) | Intervenes on the node indexed by observation: $\texttt{fdt}(\dots, \underline{\textit{full}})$. Retains counterfactual link to past prediction. |
| **Parfit's Hitchhiker** | Refuse ($\text{Dies}$) | Refuse ($\text{Dies}$) | **Pay driver** ($\$999\text{K}$) | Driver's rescue decision subjunctively depends on $\texttt{fdt}(\dots, \underline{\textit{city}})$. Paying ensures the ride is given. |
| **Twin Prisoner's Dilemma** | Cooperate | Defect | **Cooperate** | Twin runs an identical function. Intervention $\operatorname{do}(\texttt{fdt}=C)$ sets both agents' actions to $C$. |
| **XOR Blackmail** | Pays | Refuses | **Refuses** | Blackmailer's letter depends on $\texttt{fdt}(\dots, \underline{\textit{letter}})$. Counterfactual to paying alters receipt of letter, not termite infestation. |

---

## 6. Conceptual and Technical Innovations

### 6.1 Subjunctive Dominance vs. Causal Dominance
A standard defense of two-boxing in Newcomb's problem appeals to the **Sure-Thing Principle** or **Causal Dominance**: in every state of the world (Box B full, or Box B empty), taking both boxes yields $\$1{,}000$ more than taking one.

Yudkowsky and Soares demonstrate that dominance is not a theory-neutral arbiter:
* In **EDT**, an action $a$ "dominates" $b$ if $\mathbb{E}[V \mid a] > \mathbb{E}[V \mid b]$ for all partition states. Under this definition, refraining from smoking "dominates" smoking.
* In **CDT**, dominance is evaluated by holding constant all variables not causally downstream of $\textsc{Act}$. This holds the contents of Box B fixed while varying $\textsc{Act}$.
* In **A-FDT**, **Subjunctive Dominance** holds constant all variables that do not *subjunctively depend* on the decision function $\texttt{fdt}$. Since the predictor's past prediction subjunctively depends on $\texttt{fdt}$, it cannot be held constant across the counterfactuals. Under subjunctive dominance, two-boxing is strictly dominated by one-boxing.

Because every expected utility theory induces its own partition-relative dominance principle, dominance cannot serve as an independent justification for CDT. Instead, the ultimate criterion must be the empirical achievement of utility across decision problems.

### 6.2 Updatelessness: Intervening on Functions of Observations
In standard Bayesian decision analysis, an agent conditions her prior distribution upon receiving signal $x$, obtaining $P(- \mid x)$, and then computes optimal interventions within that posterior model. 

In A-FDT, this sequencing is altered. Equation (4) intervenes on $\texttt{fdt}(\dots, \underline{x})$ without standard Bayesian conditioning on $x$ in the background model:

$$\operatorname{do}\big(\texttt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\big)$$

This property is known in the foundational literature as **updatelessness** (originating in Wei Dai's Updateless Decision Theory). If an agent conditions on $x$ before counterfacting, she severs the counterfactual link between her decision rule and the fact that she observed $x$ in the first place. 

By treating the observation history $x$ merely as an input label that selects which sub-function node to surgically modify, A-FDT allows counterfactuals to reach backward through the graph to alter the observation itself. In the Mechanical Blackmail and Transparent Newcomb problems, this mechanism prevents agents from succumbing to dynamic inconsistency, rendering ad-hoc precommitments obsolete.

---

## 7. Open Mathematical and Formal Challenges

While Equation (4) provides an actionable decision procedure when $(P, G)$ are fully specified, the underlying mathematical foundations contain major open questions.

### 7.1 Formalizing Counterpossibilities: The Missing $\operatorname{true}$ Operator
Equation (4) uses Pearl’s $\operatorname{do}$-operator on a logical variable. In Pearl’s original framework, variables represent physical quantities that can be independently manipulated via physical mechanisms. But what does it mean to set a mathematical truth by intervention?

If $\texttt{fdt}(P, G, x) = a_1$ is a deterministic theorem of mathematics, then the counterfactual condition:

$$\operatorname{do}\big(\texttt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a_2\big) \quad \text{for } a_2 \neq a_1$$

is a **counterpossible**: an intervention whose antecedent is logically impossible. 

The paper acknowledges that the ideal formalization would utilize a generalized logical operator $\operatorname{true}(\phi)$, updating a probability distribution over logical sentences conditioned on the truth of a mathematical contradiction:

$$\operatorname{FDT}^*(P, x) = \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}\Big[ V \;\Big|\; \operatorname{true}\big(\texttt{fdt}(\underline{P}, \underline{x}) = a\big) \Big]$$

Because formal systems lack a consensus semantics for non-trivial conditioning on logical falsities (avoiding the principle of explosion, where $\bot \implies \text{anything}$), Equation (4) relies on the graph $G$ to explicitly dictate the structure of logical counterpossibilities. Constructing a rigorous foundation for logical counterfactuals remains an active area of research in logical induction and algorithmic information theory (e.g., Demski 2012; Hutter et al. 2013).

### 7.2 Learning Subjunctive Graphs ($G$) from Data
Pearl (2000) solved the problem of causal discovery: given conditional independence relations among observational data, along with localized interventions, one can uniquely reconstruct causal DAGs up to Markov equivalence classes.

No such discovery calculus exists for **subjunctive graphs**. How does an autonomous agent deduce, purely from empirical observation and mathematical reflection, that:
1. Box B in Newcomb's problem is subjunctively linked to its algorithm $\texttt{fdt}$, but
2. Cancer in the Smoking Lesion problem is *not* subjunctively linked to its algorithm?

In the paper's presentation, $G$ is provided by the modeler as an input. Developing a formal learning theory for subjunctive graphs—deriving dependency edges between algorithmic representations and physical systems—is the primary open technical challenge facing A-FDT.

---

## 8. A Prescriptive Implementation Guide for New Dilemmas

To apply A-FDT to an arbitrary, unfamiliar decision problem, a researcher should follow this four-step algorithmic pipeline:

```
  +-------------------------------------------------------------------------+
  | 1. Construct the Subjunctive Graph G                                    |
  |    - Include physical states, predictors, and outcomes.                 |
  |    - For each observation x, instantiate a node fdt(P, G, x).           |
  |    - Draw edges from fdt to all physical systems modeling that code.    |
  +-------------------------------------------------------------------------+
                                       |
                                       v
  +-------------------------------------------------------------------------+
  | 2. Parameterize Probability Distribution P                              |
  |    - Assign conditional distributions satisfying the Markov property    |
  |      over G, reflecting historical frequencies and predictor fidelity.  |
  +-------------------------------------------------------------------------+
                                       |
                                       v
  +-------------------------------------------------------------------------+
  | 3. Execute Subjunctive Surgery for Each Candidate Action a in A         |
  |    - Identify the specific node corresponding to current history x:     |
  |      Node* = fdt(P, G, x).                                              |
  |    - Apply Pearl surgery do(Node* = a): cut incoming edges to Node*,    |
  |      force Node* = a, and propagate downstream through G.               |
  +-------------------------------------------------------------------------+
                                       |
                                       v
  +-------------------------------------------------------------------------+
  | 4. Compute Expectations and Maximize                                    |
  |    - EU(a) = Sum_o V(o) * P(Outcome = o | do(Node* = a)).               |
  |    - Return argmax_a EU(a).                                             |
  +-------------------------------------------------------------------------+
```

### Operational Example: Psychological Twin Fire Alarm
*Problem*: You and an algorithmic twin are in separate rooms. If either pulls a fire alarm ($\textit{pull}$), both lose $\$100$ due to the loud noise. If *neither* pulls the alarm, a fire might consume both rooms (loss of $\$10{,}000$, probability 10%). If both pull, the penalty is still $\$100$.
1. **Identify the node**: $\texttt{fdt}(\underline{P}, \underline{G})$.
2. **Graph structure**: $\texttt{fdt} \to \textsc{Act}_{\text{you}}$ and $\texttt{fdt} \to \textsc{Act}_{\text{twin}}$.
3. **Hypothetical 1 ($\textit{pull}$)**: $\operatorname{do}(\texttt{fdt} = \textit{pull}) \implies$ Both pull. Guaranteed cost: $-\$100$.
4. **Hypothetical 2 ($\textit{refrain}$)**: $\operatorname{do}(\texttt{fdt} = \textit{refrain}) \implies$ Neither pulls. Expected cost: $0.10 \times (-\$10{,}000) = -\$1{,}000$.
5. **Prescription**: $-\$100 > -\$1{,}000 \implies$ A-FDT pulls the alarm. CDT defectors both burn; EDT agents pull for diagnostic reasons; A-FDT pulls because the common program controls both levers subjunctively.

---

## 9. Conclusion

Action Functional Decision Theory (A-FDT), encapsulated in **Equation (4)**, offers a mathematically coherent escape from the decades-long conflict between Causal and Evidential Decision Theories:

$$\operatorname{FDT}(P, G, x) \coloneqq \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}\Big[ V \;\Big|\; \operatorname{do}\big(\texttt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\big) \Big]$$

By shifting the object of counterfactual evaluation from the physical act-token ($\textsc{Act}$) to the mathematical function-type ($\texttt{fdt}$), A-FDT formalizes the intuition that rational agency is fundamentally an implementation of a mathematical mapping. 

The theory achieves superior real-world outcomes across an entire battery of decision dilemmas:
* It **one-boxes** in Newcomb's Problem and **cooperates** in the Twin Prisoner's Dilemma by recognizing that environmental predictions depend subjunctively on its decision rule.
* It **smokes** in the Smoking Lesion Problem and **refuses extortion** in the XOR Blackmail dilemma by recognizing that mere statistical correlations lack subjunctive dependence.
* It **pays the driver** in Parfit’s Hitchhiker and **one-boxes** in Transparent Newcomb by adopting an updateless perspective that intervenes on functions of observation histories, rendering costly physical precommitments redundant.

While open formal questions remain regarding the axiomatization of counterpossible conditionals and the algorithmic learning of subjunctive graphs, A-FDT establishes that true instrumental rationality does not lie in manipulating physical actuators in defiance of prior predictions, nor in managing one's own beliefs to curate pleasant news. Instrumental rationality consists in evaluating which mathematical output of one's own decision procedure yields the best possible world, and selecting that output accordingly.

---

## References

* Ahmed, Arif. 2014. *Evidence, Decision and Causality*. Cambridge University Press.
* Dai, Wei. 2009. "Towards a New Decision Theory." *LessWrong*.
* Demski, Abram. 2012. "Logical Prior Probability." In *Artificial General Intelligence (AGI 2012)*, LNCS 7716, 50–59. Springer.
* Drescher, Gary L. 2006. *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Gibbard, Allan, and William L. Harper. 1978. "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, edited by C. A. Hooker et al., 125–162. D. Reidel.
* Hutter, Marcus, John W. Lloyd, Kee Siong Ng, and William T. B. Uther. 2013. "Probabilities on Sentences in an Expressive Logic." *Journal of Applied Logic* 11 (4): 386–420.
* Jeffrey, Richard C. 1983. *The Logic of Decision*. 2nd ed. University of Chicago Press.
* Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Kleene, Stephen Cole. 1938. "On Notation for Ordinal Numbers." *Journal of Symbolic Logic* 3 (4): 150–155.
* Lewis, David. 1979. "Prisoners’ Dilemma is a Newcomb Problem." *Philosophy & Public Affairs* 8 (3): 235–240.
* Lewis, David. 1981. "Causal Decision Theory." *Australasian Journal of Philosophy* 59 (1): 5–30.
* Nozick, Robert. 1969. "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel*, edited by N. Rescher, 114–146. D. Reidel.
* Parfit, Derek. 1986. *Reasons and Persons*. Oxford University Press.
* Pearl, Judea. 2000. *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Skyrms, Brian. 1980. *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Soares, Nate, and Benja Fallenstein. 2015. "Toward Idealized Decision Theory." arXiv:1507.01986 [cs.AI].
* Yudkowsky, Eliezer. 2010. "Timeless Decision Theory." Technical Report, The Singularity Institute, San Francisco, CA.
* Yudkowsky, Eliezer, and Nate Soares. 2017. "Functional Decision Theory: A New Theory of Instrumental Rationality." arXiv:1710.05060v2 [cs.AI].