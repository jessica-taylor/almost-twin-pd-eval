# 020_fdt_eq4_google_gemini-3.8-flash_rlow_plow / 00005

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/c106fa44-1fc6-4a74-aa8b-d2ae2aae9bc6/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/c106fa44-1fc6-4a74-aa8b-d2ae2aae9bc6/call_0/response.raw) · finish: `stop`

### Visible response

````text
# Action Functional Decision Theory (A-FDT): Mathematical Foundations, Subjunctive Dependence, and Operational Decision Procedures

## 1. Introduction: Beyond Causal and Evidential Orthodoxy

Normative decision theory has long been divided between two paradigms: **Evidential Decision Theory (EDT)** and **Causal Decision Theory (CDT)**. The core of the dispute lies in how an agent evaluates counterfactual or hypothetical choices. Broadly speaking, an expected utility maximizer selects an action $a \in \mathcal{A}$ to maximize:
\begin{equation}
\mathcal{EU}(a) \coloneqq \sum_{j} P(a \then o_j ;\, x) \, \mathcal{U}(o_j), \label{eq:general_eu}
\end{equation}
where $\mathcal{U}$ is a bounded von Neumann–Morgenstern utility function over a countable set of outcomes $\mathcal{O}$, $x \in \mathcal{X}$ is the agent’s observation history, and $P(a \then o_j ;\, x)$ is the probability that outcome $o_j$ obtains under the decision hypothetical where $a$ is executed given history $x$.

As James Joyce observed in his axiomatic treatment of expected utility, standard representation theorems show that agents with coherent preferences agree on the structure of valuation; they disagree solely on the *epistemic perspective* from which alternatives are evaluated—namely, the interpretation of the hypothetical connective “$\then$”.

* In **EDT**, the hypothetical is interpreted as standard Bayesian conditionalization:
  \begin{equation}
  \mathrm{EDT}(P, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left[\mathcal{V} \mid \text{Obs}=x, \, \text{Act}=a\right], \label{eq:edt}
  \end{equation}
  where $\mathcal{V} \coloneqq \mathcal{U}(\text{Outcome})$. EDT asks: *“Which physical act would be the best news to learn that I took?”*
* In **CDT**, formalizable via Judea Pearl’s do-calculus on an augmented causal graph $G$, the hypothetical is interpreted as a local physical intervention severing incoming causal edges to the physical act $\text{Act}$:
  \begin{equation}
  \mathrm{CDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left[\mathcal{V} \mid \mathtt{do}(\text{Act}=a), \, \text{Obs}=x\right]. \label{eq:cdt}
  \end{equation}
  CDT asks: *“Which physical act of mine causes the best outcome downstream?”*

Both theories suffer catastrophic failures in classic decision dilemmas. EDT notoriously succumbs to the *Smoking Lesion Problem*, where smoking is causally benign but statistically correlated with an incurable arterial lesion; EDT agents irrationally suppress smoking merely to "manage the news," confusing correlation with causation. Conversely, CDT predictably walks away poor in *Newcomb's Problem*, in the *Psychological Twin Prisoner’s Dilemma*, in *Parfit’s Hitchhiker*, and in blackmail scenarios. In Newcomb's problem, an agent faces two boxes: Box A containing $\$1,000$ and Box B containing either $\$1,000,000$ or $\$0$. A predictor, accurate $99\%$ of the time, placed $\$1,000,000$ in Box B if and only if she predicted the agent would forgo Box A. CDT reasons that because the contents of Box B are already physically fixed, taking both boxes dominates taking only Box B. The predictor anticipates this, leaving Box B empty; the CDT agent receives $\$1,000$, whereas an agent who reliably one-boxes receives $\$1,000,000$.

**Action Functional Decision Theory (A-FDT)**—formalized in Equation (4), Section 5 of Yudkowsky and Soares (2017)—resolves this impasse. A-FDT posits that normative choice centers not on intervening upon a physical token action $\text{Act}$ (as in CDT), nor on conditioning upon evidence (as in EDT), but on evaluating the outputs of the **fixed mathematical decision function** that the agent’s physical hardware instantiates.

---

## 2. The Core Formalism of A-FDT

### 2.1 The Mathematical Decision Function as an Object of Intervention
In A-FDT, the deliberating agent does not view herself merely as a localized physical actuator. Rather, her deliberation is an execution of an algorithm: a deterministic mapping from an epistemic state and observation history to an action. 

Let the world model $M = (P, G)$ consist of:
1. A subjective joint probability distribution $P$ over a set of discrete and continuous variables. Crucially, $P$ is defined not merely over empirical states of affairs, but also over **logical variables** representing mathematical truths and algorithmic evaluations (such as arithmetical identities or the outputs of programs).
2. A directed acyclic graph $G = (V, E)$, where the vertex set $V$ includes both physical variables (e.g., $\text{Act}$, $\text{Prediction}$, $\text{Box B}$, $\text{Outcome}$, $\mathcal{V}$) and logical variables representing mathematical functions evaluated at specific inputs. The edges $E$ encode dependencies—causal, computational, and logical.

To denote self-referential algorithmic variables within the agent’s own model, let quotation and dequoting be defined formally. If $\underline{z}$ denotes the syntactic constant encoding the value of object $z$, the variable $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ is a formal node in $V$ representing the output of the mathematical function $\text{A-FDT}$ when evaluated on the inputs $(P, G, x)$. By Kleene’s Second Recursion Theorem, an algorithm can manipulate representations of its own source code and mathematical specification without paradox.

### 2.2 Equation (4): The Primary Formal Presentation
The formal definition of A-FDT (Equation 4, Section 5) specifies the action selected by an agent with prior distribution $P$, dependency graph $G$, and observation history $x$:

\begin{equation}
\label{eq:fdt}
\mathrm{A\text{-}FDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left[\mathcal{V} \;\middle|\; \mathtt{do}\left(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right].
\end{equation}

Equation \eqref{eq:fdt} contains two decisive mathematical shifts that separate A-FDT from CDT (Equation \ref{eq:cdt}) and EDT (Equation \ref{eq:edt}):

1. **Intervention on the Decision Type rather than the Token Action:** Where CDT applies Pearl’s physical intervention $\mathtt{do}(\text{Act} = a)$, severing incoming causal parents of the physical node $\text{Act}$, A-FDT applies the intervention operator $\mathtt{do}(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)$ to the **logical node** corresponding to the decision algorithm itself. If the physical action node $\text{Act}$ is a child of $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ in $G$, the intervention sets the algorithm's output to $a$, which then propagates down to $\text{Act}$ *and* simultaneously propagates across every other node in the network that subjunctively depends on that same mathematical output.
2. **Observation by Node Selection rather than Conditioning:** In CDT, upon observing evidence $x$, the agent conditions the distribution via $P(- \mid \text{Obs}=x)$ and maximizes $\mathbb{E}[\mathcal{V} \mid \mathtt{do}(\text{Act}=a), \text{Obs}=x]$. In A-FDT, the observation $x$ determines **which variable in the graph is subjected to surgery**. If the observation history shifts from $x$ to $y$, A-FDT shifts its target of intervention from $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ to $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{y})$. Bayesian conditionalization on $\text{Obs}=x$ inside the expectation is omitted in the canonical form of Equation \eqref{eq:fdt}; the observation is baked directly into the identity of the function instance being queried.

---

## 3. Subjunctive Dependence and Counterpossible Reasoning

### 3.1 Causal vs. Subjunctive Dependence
At the heart of A-FDT is the concept of **subjunctive dependence**. Standard causal dependence requires a chain of physical mechanisms propagating energy or signals forward through spacetime. Two calculators computing $6288 + 1048$ on opposite sides of the globe do not communicate causally; yet their outputs are not independent. If one outputs $7336$, the probability that the other outputs $7336$ is near certainty. Their behaviors subjunctively depend upon the underlying arithmetic truth of the addition function.

In Charles Sanders Peirce’s terminology, CDT intervenes on the *token* (the physical motion of the agent’s arm), whereas A-FDT intervenes on the *type* (the abstract mathematical calculation). 

* **Definition (Subjunctive Dependence in A-FDT):** A variable $Y$ subjunctively depends on a decision function $f$ evaluated at input $w$ if, within the agent’s dependency structure $G$, there exists a directed path from the logical node $f(w)$ to $Y$.

Causal dependence is simply a special case of subjunctive dependence where the path consists purely of physical, time-directed causal mechanisms. Mere statistical correlation, however, does not constitute subjunctive dependence. In the Smoking Lesion Problem, an arterial lesion causes both a desire to smoke and lung cancer. The physical cancer does not read, simulate, or instantiate the agent's decision algorithm; its presence is invariant under counterfactual changes to what the decision algorithm outputs.

### 3.2 The Semantics of Counterpossibles and the $\mathtt{true}$ Operator
A profound theoretical question arises: if the mathematical function $\text{A-FDT}(P, G, x)$ is deterministic, it logically outputs a unique action $a^* \in \mathcal{A}$. What does it mean, mathematically, to evaluate the hypothetical $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a$ for $a \neq a^*$?

This requires an evaluation of a **counterpossible conditional**—a conditional whose antecedent is logically impossible. In philosophical logic (Cohen 1990; Bjerring 2013), standard Lewis-Stalnaker possible-world semantics renders any counterpossible vacuously true ($\Box (p \rightarrow q)$ if $\neg \Diamond p$). For A-FDT, counterpossibles must be non-trivial: learning that Fermat's Last Theorem was false ought to lead a mathematician to revise beliefs about elliptic curves, not conclude that $0=1$.

Ideally, A-FDT would invoke a formal logical updating operator, denoted $\mathtt{true}(\phi)$, which updates a distribution $P$ over mathematical sentences upon the counterfactual assumption that the sentence $\phi$ holds:
\begin{equation}
\mathrm{A\text{-}FDT}^*(P, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left[\mathcal{V} \;\middle|\; \mathtt{true}\left(\mathtt{fdt}(\underline{P}, \underline{x}) = a\right)\right].
\end{equation}
However, as Yudkowsky and Soares acknowledge, a complete, rigorous theory of assigning coherent probabilities to logically inconsistent antecedents remains an open mathematical challenge. 

A-FDT circumvents this foundational obstacle by importing Pearl’s graph-theoretic surgery. Rather than defining an unconstrained $\mathtt{true}$ operator across arbitrary mathematical sentences, A-FDT takes the dependency graph $G$ as an **explicit input**. Once logical dependencies are encoded as directed edges in an acyclic graph, Pearl's physical intervention operator $\mathtt{do}(\cdot)$ can be repurposed without formal modification. The mathematical mechanics of graph surgery—cutting incoming edges to the intervention node and recalculating downstream expectations via standard probability propagation—operate identically whether the node represents a physical switch or a logical truth.

---

## 4. Applying A-FDT: Canonical Dilemmas

To see how Equation \eqref{eq:fdt} operates in practice, we examine how an A-FDT agent (traditionally named Fiona) resolves classic decision-theoretic puzzles in contrast to an EDT agent (Eve) and a CDT agent (Carl).

### 4.1 Newcomb’s Problem
In Newcomb's Problem, the predictor constructs an accurate internal model or simulation of the agent's decision process prior to the choice.

```
       [ fdt(P, G) ] <--- Intervention Target for A-FDT
         /        \
        v          v
     [ Act ]    [ Prediction ] <--- [ Accurate (0.99) ]
        \          /
         v        v
        [ Outcome / Box B ]
              |
              v
             [ V ]
```

* **The Model:** $V = \{\mathtt{fdt}(\underline{P}, \underline{G}), \text{Act}, \text{Prediction}, \text{Accurate}, \text{Box B}, \mathcal{V}\}$.
  * $\text{Accurate} \in \{\text{acc}, \text{inacc}\}$ with $P(\text{acc}) = 0.99$.
  * Directed edges: $\mathtt{fdt} \rightarrow \text{Act}$, $\mathtt{fdt} \rightarrow \text{Prediction}$, $\text{Accurate} \rightarrow \text{Prediction}$, $\text{Prediction} \rightarrow \text{Box B}$, $\{\text{Act}, \text{Box B}\} \rightarrow \mathcal{V}$.
  * The deterministic structural equations specify:
    $$\text{Act} = \mathtt{fdt}(\underline{P}, \underline{G}),$$
    $$\text{Box B} = \begin{cases} \$1,000,000 & \text{if } \text{Prediction} = \text{onebox} \\ \$0 & \text{if } \text{Prediction} = \text{twobox} \end{cases}$$
    $$\text{Prediction} = \begin{cases} \mathtt{fdt} & \text{if } \text{Accurate} = \text{acc} \\ \neg \mathtt{fdt} & \text{if } \text{Accurate} = \text{inacc} \end{cases}$$
* **CDT Evaluation:** Carl performs $\mathtt{do}(\text{Act}=a)$. Because Box B is not causally downstream of $\text{Act}$ (the arrow points $\mathtt{Predisposition} \rightarrow \text{Prediction} \rightarrow \text{Box B}$ and $\mathtt{Predisposition} \rightarrow \text{Act}$), severing incoming arrows to $\text{Act}$ leaves $P(\text{Box B}=\text{full})$ invariant at some baseline $p$. CDT compares:
  $$\mathbb{E}[\mathcal{V} \mid \mathtt{do}(\text{twobox})] = p(\$1,001,000) + (1-p)(\$1,000) = p(\$1,000,000) + \$1,000,$$
  $$\mathbb{E}[\mathcal{V} \mid \mathtt{do}(\text{onebox})] = p(\$1,000,000).$$
  CDT rigidly selects $\text{twobox}$.
* **A-FDT Evaluation:** Fiona solves Equation \eqref{eq:fdt}. She evaluates the intervention on the logical node $\mathtt{fdt}$:
  $$\mathtt{do}\left(\mathtt{fdt}(\underline{P}, \underline{G}) = \text{onebox}\right) \implies \begin{cases} \text{Act} = \text{onebox} \\ P(\text{Box B} = \$1,000,000) = 0.99 \end{cases}$$
  $$\mathbb{E}\left[\mathcal{V} \mid \mathtt{do}(\mathtt{fdt} = \text{onebox})\right] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000.$$
  Conversely, for two-boxing:
  $$\mathtt{do}\left(\mathtt{fdt}(\underline{P}, \underline{G}) = \text{twobox}\right) \implies \begin{cases} \text{Act} = \text{twobox} \\ P(\text{Box B} = \$1,000,000) = 0.01 \end{cases}$$
  $$\mathbb{E}\left[\mathcal{V} \mid \mathtt{do}(\mathtt{fdt} = \text{twobox})\right] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$
  A-FDT unambiguously outputs $\text{onebox}$. Fiona collects $\$1,000,000$, outperforming Carl.

### 4.2 The Smoking Lesion Problem
In the Smoking Lesion Problem, an unknown genetic or arterial lesion causes both an increased probability of smoking and lung cancer.

```
            [ Lesion ]
             /      \
            v        v
     [ Preferences ]  [ Cancer ]
            |            |
            v            v
     [ fdt(P_S, G) ]  [ Death ]
            |            |
            v            v
         [ Act ] ----> [ V ]
```

* **The Model:** The agent’s utility function is uncertain: $\mathcal{U}_S$ (prefers smoking, $+1,000$) or $\mathcal{U}_R$ (prefers refraining). The presence of the lesion dictates the utility function. Thus, there are two potential functions: $\mathtt{fdt}(\underline{P_S}, \underline{G})$ and $\mathtt{fdt}(\underline{P_R}, \underline{G})$.
* **Crucial Dependency Property:** In graph $G$, the directed edge runs $\text{Lesion} \rightarrow \text{Preferences} \rightarrow \mathtt{fdt}$, and $\text{Lesion} \rightarrow \text{Cancer}$. There is **no directed path** from $\mathtt{fdt}(\underline{P_S}, \underline{G})$ to $\text{Lesion}$ or to $\text{Cancer}$. Cancer does not simulate, compute, or track the agent's decision algorithm.
* **A-FDT Evaluation:** Under Equation \eqref{eq:fdt}, Fiona intervenes on $\mathtt{do}(\mathtt{fdt}(\underline{P_S}, \underline{G}) = a)$. Because $\text{Lesion}$ is an *ancestor* of $\mathtt{fdt}$, Pearl’s graph surgery severs the incoming dependency:
  $$P(\text{Lesion} \mid \mathtt{do}(\mathtt{fdt} = \text{smoke})) = P(\text{Lesion}) = p.$$
  The probability of contracting fatal cancer remains identically fixed at $P(\text{Cancer} \mid \text{Lesion})p + P(\text{Cancer} \mid \neg\text{Lesion})(1-p)$ under both interventions. Smoking yields an unconditional $+1,000$ utility premium:
  $$\mathbb{E}\left[\mathcal{V} \mid \mathtt{do}(\mathtt{fdt} = \text{smoke})\right] - \mathbb{E}\left[\mathcal{V} \mid \mathtt{do}(\mathtt{fdt} = \text{refrain})\right] = p(\$1,000) > 0.$$
  A-FDT prescribes smoking. 

Thus, A-FDT achieves what Gibbard and Harper claimed was impossible: it one-boxes in Newcomb’s Problem while smoking in the Smoking Lesion Problem under a single, unified decision rule.

### 4.3 The Transparent Newcomb Problem and Parfit’s Hitchhiker
A dramatic illustration of A-FDT’s divergence from both CDT and EDT occurs when the agent receives an observation *revealing* the predictor's past action before the choice is made.

In the **Transparent Newcomb Problem**, Box A contains $\$1,000$ and Box B is transparent, visibly containing $\$1,000,000$ or $\$0$. The predictor placed $\$1,000,000$ in Box B iff she predicted that the agent would leave Box A behind *upon seeing that both boxes are full*. Suppose the agent looks and observes $\text{Obs} = \text{full}$.

* **The EDT and CDT Response:** Both theories two-box. For CDT, the contents are fixed and taking Box A dominates. For EDT, conditional on already observing $\text{Obs} = \text{full}$, the "good news" is already in hand; conditioning on two-boxing yields $\$1,001,000$, whereas conditioning on one-boxing yields $\$1,000,000$. Both CDT and EDT agents predictably two-box, meaning the predictor leaves Box B empty, netting them $\$1,000$.
* **The A-FDT Response:** Fiona does *not* condition on $\text{Obs} = \text{full}$ to evaluate her action. Instead, the observation determines which node to intervene upon: $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{\text{full}})$.
  In Fiona’s dependency graph:
  $$\mathtt{fdt}(\underline{P}, \underline{G}, \underline{\text{full}}) \longrightarrow \text{Prediction} \longrightarrow \text{Box B} \longrightarrow \text{Obs}.$$
  The predictor’s past action depends subjunctively on what the algorithm outputs *when faced with the observation 'full'*.
  Fiona evaluates:
  1. If $\mathtt{do}(\mathtt{fdt}(\dots, \underline{\text{full}}) = \text{onebox})$:
     $$\text{Prediction} = \text{full} \implies \text{Box B} = \text{full} \implies \mathcal{V} = \$1,000,000 \quad (\text{with probability } 0.99).$$
  2. If $\mathtt{do}(\mathtt{fdt}(\dots, \underline{\text{full}}) = \text{twobox})$:
     $$\text{Prediction} = \text{empty} \implies \text{Box B} = \text{empty} \implies \mathcal{V} \approx \$1,000.$$
     (If the box is empty, the agent is routed to evaluate $\mathtt{fdt}(\dots, \underline{\text{empty}})$, taking whatever Box A contains).

  Fiona one-boxes despite staring at a full box. Because she reliably implements this algorithm, the predictor fills Box B, and Fiona leaves with $\$1,000,000$.

* **Equivalence to Parfit’s Hitchhiker:** In Parfit’s Hitchhiker, an agent is dying in a desert. A driver will rescue her and take her to the city only if the driver predicts the agent will withdraw and pay $\$1,000$ upon arrival at an ATM. The driver is an exceptional lie detector (accuracy $0.99$).
  Upon reaching the city, both CDT and EDT refuse to pay: the rescue has already occurred, and paying $\$1,000$ is pure loss. Foreseeing this, the driver abandons them to die in the desert.
  An A-FDT agent in the city recognizes that her decision algorithm's output on input $\text{city}$, $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{\text{city}})$, subjunctively determined whether the driver rescued her in the desert. Evaluating $\mathtt{do}(\mathtt{fdt}(\dots, \underline{\text{city}}) = \text{refuse})$ maps to a counterfactual world where she was left to die. A-FDT pays the $\$1,000$, ensuring her rescue in expectation.

---

## 5. Formal Comparison: EDT, CDT, and A-FDT

The distinct mechanics of the three theories can be codified across four formal axes:

| Feature | Evidential Decision Theory (EDT) | Causal Decision Theory (CDT) | Action Functional Decision Theory (A-FDT) |
| :--- | :--- | :--- | :--- |
| **Mathematical Object** | Joint distribution $P(V)$ | Distribution + Causal DAG $(P, G)$ | Distribution + Subjunctive DAG $(P, G)$ |
| **Locus of Evaluation** | Observation of physical act $\text{Act} = a$ | Physical intervention $\mathtt{do}(\text{Act} = a)$ | Logical intervention $\mathtt{do}(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)$ |
| **Response to Evidence $x$** | Bayesian update: $P(- \mid \text{Obs}=x)$ | Bayesian update: $P(- \mid \text{Obs}=x)$ | Indexical node selection: $\mathtt{fdt}(\dots, \underline{x})$ |
| **Treated Correlations** | Preserves all statistical correlations | Preserves only physical downstream effects | Preserves all logical and causal dependencies |
| **Newcomb’s Problem** | One-boxes | Two-boxes | One-boxes |
| **Smoking Lesion** | Refrains (irrationally) | Smokes | Smokes |
| **Parfit’s Hitchhiker** | Refuses to pay (dies) | Refuses to pay (dies) | Pays (survives) |
| **Susceptibility to Extortion** | Vulnerable (XOR Blackmail) | Vulnerable (Mechanical Blackmail) | Invulnerable / Resists |

---

## 6. Open Problems, Unsettled Foundations, and Operational Extensions

While A-FDT demonstrates compelling pragmatic superiority, the source document leaves several key mathematical and operational questions unresolved. Below, we distinguish the strict claims of the source document from necessary mathematical extensions.

### 6.1 The Construction of the Subjunctive Graph $G$
* **The Gap:** In CDT, Pearl provides a mature operational framework for inducing causal DAGs from passive observational data and active randomized controlled interventions via the $d$-separation criterion and the do-calculus. The authors of A-FDT explicitly admit that *no such discovery procedure exists for subjunctive dependency graphs*. The graph $G$ must currently be supplied as an unmodeled primitive.
* **Operational Proposal:** How might an agent induce subjunctive dependencies algorithmically?
  A mathematically rigorous interpretation requires formalizing models of computation within the causal network. If another entity $Y$ makes an action based on a prediction of the agent, $Y$ must physically instantiate a program $\pi_Y$ that simulates or approximates the agent's source code $\pi_{\text{agent}}$. 
  Subjunctive dependence can be operationalized via **program compilation semantics and proof theory**:
  Let two nodes $X$ and $Y$ in a computational environment be defined. A directed subjunctive edge $\mathtt{fdt}(\underline{\pi}, \underline{x}) \rightarrow Y$ exists if there exists a valid deductive verification within a formal system (e.g., Peano Arithmetic) showing that the state of $Y$ functionally depends on the output of $\pi(x)$:
  $$\mathcal{T} \vdash Y = \mathcal{C}(\pi(x)),$$
  where $\mathcal{C}$ is a known context or compiler. In this framework, subjunctive dependencies are discovered not through physical randomization, but through **static code analysis, cryptographic verification, and bounded automated theorem proving**.

### 6.2 Updatelessness: Action-Selection vs. Policy-Selection
* **The Gap:** Equation \eqref{eq:fdt} is an *action-functional* formulation: it maximizes over primitive actions $a \in \mathcal{A}$ while using observation $x$ to locate the specific function instance $\mathtt{fdt}(\dots, \underline{x})$. However, in Footnote 7 and Footnote 16, the authors hint at an alternative, strictly stronger formulation: **Policy-FDT (or Updateless Decision Theory, UDT)**.
* **The Conflict:** Under Equation \eqref{eq:fdt}, an agent holding a blackmail letter in the *Mechanical Blackmail* problem evaluates an intervention on $\mathtt{fdt}(\dots, \underline{\text{letter}})$. In doing so, she observes that if this node outputs $\text{refuse}$, the probability that the letter was ever sent drops to $\approx 0$. 
  This introduces a conceptual strain: the agent is physically executing deliberation *conditional on having received the letter*, yet her counterfactual hypothetical assigns near-zero probability to the observation she is currently experiencing.
* **Operational Resolution (Policy-FDT):** To make this mathematically consistent without conceptual strain, A-FDT should be formalized as selecting a global **decision policy** $\Pi: \mathcal{X} \rightarrow \mathcal{A}$ *prior* to observations:
  \begin{equation}
  \Pi^* \coloneqq \operatorname*{argmax}_{\Pi \in \mathcal{A}^{\mathcal{X}}} \mathbb{E}\left[\mathcal{V} \;\middle|\; \mathtt{do}\left(\mathtt{FDT}_{\text{policy}}(\underline{P}, \underline{G}) = \Pi\right)\right],
  \end{equation}
  followed by the execution of $a = \Pi^*(x)$.
  Under Policy-FDT, the agent never has to imagine "erasing" an observation she already holds; she simply asks which comprehensive mapping from sensory inputs to motor outputs maximizes global expected utility across all possible observation branches.

### 6.3 Self-Referential Stability and Algorithmic Fixed Points
* **The Gap:** Equation \eqref{eq:fdt} evaluates the utility of setting $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a$. But what if the distribution $P$ or the graph $G$ must assign a probability to the very statement that A-FDT outputs $a$?
* **Operational Resolution:** If an agent attempts to predict herself or other symmetrical A-FDT agents, naive circular evaluation causes non-terminating loops (as seen in Carl's conniptions during *Death in Damascus*).
  To ensure mathematical consistency, the evaluation of Equation \eqref{eq:fdt} must be grounded in **algorithmic game theory and logical fixed-point theorems**. 
  Following the work of Demski (2012) and Soares & Fallenstein (2015), an A-FDT agent operating in multi-agent environments must use a continuous probabilistic logic (such as assigning probabilities over Gödel sentences via a consistent scoring rule). When two identical A-FDT agents play a coordination game or a Prisoner's Dilemma, they compute their choices using modal fixed-point theorems (such as the Gödel-Löb theorem in provability logic). This guarantees that both agents provably cooperate because each agent's proof of cooperation reflects and validates the other's proof, completely bypassing the infinite loops of unratified CDT.

---

## 7. A Step-by-Step Operational Procedure for Unfamiliar Decision Problems

To allow an analyst or autonomous system to apply A-FDT to an unfamiliar decision problem, we synthesize Equation \eqref{eq:fdt} into an algorithmic protocol:

### Step 1: Specify the State Space and Utility
Define the set of available actions $\mathcal{A}$, the countable set of outcomes $\mathcal{O}$, the observation space $\mathcal{X}$, and a bounded utility function $\mathcal{U}: \mathcal{O} \rightarrow \mathbb{R}$.

### Step 2: Construct the Subjunctive World-Model $(P, G)$
1. Identify all physical variables: the agent's observation $\text{Obs}$, physical actuation $\text{Act}$, intermediate environmental mechanisms, and the outcome node $\text{Outcome}$.
2. Identify all computational and cognitive entities in the environment that model, predict, simulate, or share source code with the agent.
3. For each observation state $x \in \mathcal{X}$, instantiate a formal logical node $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$.
4. Draw directed edges representing physical causation (e.g., $\text{Act} \rightarrow \text{Outcome}$).
5. Draw directed edges representing **computational/logical dependencies**:
   * Add a directed edge $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) \rightarrow \text{Act}$.
   * If an environmental process $k$ sets a variable $Y$ based on an algorithm that predicts or simulates $\mathtt{fdt}$ on input $x$, add a directed edge $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) \rightarrow Y$.
   * **Crucial Pruning Rule:** Do *not* add edges between $\mathtt{fdt}$ and background variables that are merely statistically correlated (such as the arterial lesion or cosmic rays). Edges must correspond to computational simulations or algorithmic identity.

### Step 3: Identify the Active Locus of Intervention
Given the agent's current real-time observation history $x_{\text{obs}}$, select the specific node:
$$\mathcal{N}^* \coloneqq \mathtt{fdt}\left(\underline{P}, \underline{G}, \underline{x_{\text{obs}}}\right).$$

### Step 4: Perform Graph Surgery via Pearl’s $\mathtt{do}$-Calculus
For each candidate action $a \in \mathcal{A}$:
1. Form the surgically altered graph $G_{\bar{\mathcal{N}^*}}$ by deleting all incoming edges to $\mathcal{N}^*$.
2. Fix the value $\mathcal{N}^* = a$.
3. Compute the downstream probability distribution over the outcome node using the mutilated network:
   $$P\left(\text{Outcome} = o_j \;\middle|\; \mathtt{do}\left(\mathcal{N}^* = a\right)\right).$$
   Propagate updates forward through both the physical action path $\text{Act}$ and every predictive path $Y$ stemming from $\mathcal{N}^*$.

### Step 5: Execute the Maximizing Act
Calculate the functional expected utility for each candidate action:
$$\mathcal{EU}_{\text{A-FDT}}(a) = \sum_{j} P\left(\text{Outcome} = o_j \;\middle|\; \mathtt{do}\left(\mathcal{N}^* = a\right)\right) \mathcal{U}(o_j).$$
Output and physically execute:
$$a^* = \operatorname*{argmax}_{a \in \mathcal{A}} \mathcal{EU}_{\text{A-FDT}}(a).$$

---

## 8. Conclusion

Action Functional Decision Theory (A-FDT), crystallized in Equation \eqref{eq:fdt}, provides an elegant, formally unified alternative to the decades-old division between Causal and Evidential Decision Theory. By re-anchoring expected utility maximization on the **mathematical decision function** rather than the physical act token, A-FDT reconciles the fundamental tension between Newcomb-like dilemmas and common-cause dilemmas. 

A-FDT agents do not indulge in magical thinking, retrocausality, or fatalistic news-management. Rather, they operate from a globally consistent perspective, recognizing that they are physical implementations of abstract mathematical functions embedded in a universe that frequently predicts, models, and responds to those very computations. Where CDT fails by tearing down logically necessary correlations between predictions and actions, and EDT fails by preserving correlations devoid of computational or causal backing, A-FDT achieves optimal utility across all fair decision problems by respecting the true logical and subjunctive structure of reality.

---

## References

* Ahmed, Arif. 2014. *Evidence, Decision and Causality*. Cambridge University Press.
* Arntzenius, Frank. 2008. “No Regrets, or: Edith Piaf Revamps Decision Theory.” *Erkenntnis* 68 (2): 277–297.
* Bjerring, Jens Christian. 2013. “On Counterpossibles.” *Philosophical Studies* 168 (2): 327–353.
* Cohen, Daniel. 1990. “On What Cannot Be.” In *Truth or Consequences: Essays in Honor of Nuel Belnap*, edited by J. M. Dunn and A. Gupta, 123–132. Kluwer Academic Publishers.
* Demski, Abram. 2012. “Logical Prior Probability.” In *Artificial General Intelligence (AGI 2012)*, LNCS 7716: 50–59. Springer.
* Drescher, Gary L. 2006. *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Eells, Ellery. 1984. “Metatickles and the Dynamics of Deliberation.” *Theory and Decision* 17 (1): 71–95.
* Gibbard, Allan, and William L. Harper. 1978. “Counterfactuals and Two Kinds of Expected Utility.” In *Foundations and Applications of Decision Theory*, edited by C. A. Hooker et al., 125–162. D. Reidel.
* Jeffrey, Richard C. 1983. *The Logic of Decision*. 2nd ed. University of Chicago Press.
* Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Joyce, James M. 2012. “Regret and Instability in Causal Decision Theory.” *Synthese* 187 (1): 123–145.
* Lewis, David. 1979. “Prisoners’ Dilemma is a Newcomb Problem.” *Philosophy & Public Affairs* 8 (3): 235–240.
* Lewis, David. 1981. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59 (1): 5–30.
* Nozick, Robert. 1969. “Newcomb’s Problem and Two Principles of Choice.” In *Essays in Honor of Carl G. Hempel*, edited by N. Rescher, 114–146. D. Reidel.
* Parfit, Derek. 1986. *Reasons and Persons*. Oxford University Press.
* Pearl, Judea. 2000. *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Skyrms, Brian. 1980. *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Soares, Nate, and Benja Fallenstein. 2015. “Toward Idealized Decision Theory.” *arXiv:1507.01986 [cs.AI]*.
* Spohn, Wolfgang. 2012. “Reversing 30 Years of Discussion: Why Causal Decision Theorists Should One-Box.” *Synthese* 187 (1): 95–122.
* Yudkowsky, Eliezer, and Nate Soares. 2017. “Functional Decision Theory: A New Theory of Instrumental Rationality.” *arXiv:1710.05060v2 [cs.AI]*.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/97d3a872-ae60-4b8d-93ec-eea226a3fe1f/call_0/request.json)

[Authoritative raw response](../../../../../../runs/97d3a872-ae60-4b8d-93ec-eea226a3fe1f/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/97d3a872-ae60-4b8d-93ec-eea226a3fe1f/call_1/request.json)

[Authoritative raw response](../../../../../../runs/97d3a872-ae60-4b8d-93ec-eea226a3fe1f/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
