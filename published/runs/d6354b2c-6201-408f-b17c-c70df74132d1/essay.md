# Subjunctive Dependence and the Calculus of Thought: A Mathematical Exposition of Action Functional Decision Theory (A-FDT)

For over four decades, normative decision theory has been locked in an impasse between Evidential Decision Theory (EDT) and Causal Decision Theory (CDT). The fault lines are familiar: in Newcomb’s problem, EDT’s recommendation to take one box yields \$1,000,000, while CDT insists on taking two boxes, walking away with a paltry \$1,000 because the physical cash is already fixed in place. Conversely, in the Smoking Lesion problem, standard EDT forgoes the pleasure of smoking to avoid "managing the news" about an unalterable genetic predisposition to cancer, whereas CDT correctly diagnoses the absence of a causal mechanism and pockets the utility. 

To bridge this divide, Allan Gibbard and William Harper (1978) suggested that an agent must either be a two-boxing smoker (CDT) or a one-boxing abstainer (EDT). Functional Decision Theory, introduced by Eliezer Yudkowsky and Nate Soares (2017), rejects this dichotomy. 

In this essay, we examine the formal machinery, metaphysical commitments, and algorithmic execution of **Action Functional Decision Theory (A-FDT)**. A-FDT evaluates candidate choices not as physical interventions on local tokens of behavior, nor as mere conditioning events, but as counterfactual evaluations of the agent's mathematical decision function itself. Our focus will center on the primary action-level formulation of the theory—termed here **A-FDT** to distinguish this specific mathematical rule from broader policy-based proposals—grounded in Equation (4) of the foundational paper.

---

## 1. The Decision-Theoretic Landscape

The common denominator of classical expected utility theories (Joyce 1999) is the maximization of an index:
\begin{equation}
\mathcal{EU}(a) \coloneqq \sum_{j} P(a \hookrightarrow o_j ;\, x) \, \mathcal{U}(o_j)
\label{eq:umax}
\end{equation}
where $\mathcal{A}$ is a finite set of actions, $\mathcal{X}$ is a countable space of observation histories, $\mathcal{O}$ is a countable space of outcomes, $\mathcal{U}: \mathcal{O} \to \mathbb{R}$ is a bounded utility function, and $a \hookrightarrow o_j$ denotes the conditional connective representing "if action $a$ were taken, outcome $o_j$ would obtain." 

Joyce's representation theorem establishes that different decision theories do not disagree on the axiomatic foundations of preference or utility; rather, they disagree entirely on the *epistemic perspective* embedded in the connective $\hookrightarrow$.

### Evidential Decision Theory (EDT)
EDT identifies the connective $\hookrightarrow$ with standard Bayesian conditionalization:
\begin{equation}
\mathrm{EDT}(P, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\big[V \mid \textsc{Obs}=x, \textsc{Act}=a\big]
\label{eq:edt}
\end{equation}
where $V \coloneqq \mathcal{U}(\textsc{Outcome})$. EDT asks: *"Which action would be the best news to learn that I performed?"* As demonstrated by Egan (2007) and Soares & Fallenstein (2015), this epistemic perspective renders EDT vulnerable to "managing the news." If an adversary sets up an extortion dilemma whose payoffs correlate with the agent’s actions without causal efficacy (such as the XOR Blackmail), EDT systematically capitulates.

### Causal Decision Theory (CDT)
CDT rectifies this by demanding that the connective track physical interventions. Formulated via Judea Pearl’s (2000) graphical causal calculus:
\begin{equation}
\mathrm{CDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\big[V \mid \operatorname{do}(\textsc{Act}=a), \textsc{Obs}=x\big]
\label{eq:cdt}
\end{equation}
where $G$ is a directed acyclic graph (DAG) encoding the causal structure over the variables in $P$, and $\operatorname{do}(\textsc{Act}=a)$ represents graph surgery: all incoming directed edges to $\textsc{Act}$ are severed, setting $\textsc{Act}=a$ while leaving parent and non-descendant variables untouched. CDT asks: *"Which physical action of mine causes the best outcome?"* 

Because a predictor's past prediction lies causally upstream of the agent's physical choice, CDT sets $\operatorname{do}(\textsc{Act}=\textit{onebox})$, holds the contents of Box B constant, and deduces that two-boxing dominates. Consequently, in environments containing accurate predictive models of the agent, CDT agents are systematically outcompeted.

---

## 2. Formal Specification of A-FDT

A-FDT resolves this failure mode by changing the target of intervention. An A-FDT agent does not view their physical action as an uncaused primitive variable. Rather, their action is recognized as the physical execution of a mathematical computation: a decision algorithm. 

If an agent is computing a fixed decision algorithm, any external model of that agent—whether a neural network simulation run by a Newcomb predictor, an appointment entry written by Death in Damascus, or a biological twin deliberating in another room—is computing or approximating *the exact same mathematical function*. To evaluate what happens if an action is taken, the agent must evaluate the counterfactual output of that *function*.

### Primary Mathematical Definition
Let $P$ denote an agent’s joint probability distribution over physical states, histories, and algorithmic tokens. Let $G$ denote an extended dependency graph that incorporates both causal mechanisms and formal logical relationships. Let $x \in \mathcal{X}$ denote the agent's current observation history.

The formal decision rule of **Action Functional Decision Theory (A-FDT)**, defined by Equation (4), Section 5 of Yudkowsky and Soares (2017), is:
\begin{equation}
\mathrm{A\text{-}FDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left[V \;\middle|\; \operatorname{do}\left(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right]
\label{eq:afdt}
\end{equation}

Here, underline notation represents syntactic dequoting (or "quining"): if $x = \text{"seen full"}$, then $\underline{x}$ is the literal string constant naming that input within the agent’s internal language. The term $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ is a formal variable within the model representing the evaluation of the A-FDT algorithm on the exact representations $(P, G, x)$.

```
   CDT Graph Surgery: do(Act = a)         A-FDT Graph Surgery: do(fdt(P,G,x) = a)
   ==============================         =======================================

         [Predisposition]                         [ fdt(P, G, x) ]  <-- INTERVENTION
           /          \                               /          \
          v            v                             v            v
     [Prediction]   [ Act ] <-- INTERVENTION   [Prediction]    [ Act ]
          |            |                             |            |
          v            v                             v            v
       [Box B]      [Outcome]                     [Box B]      [Outcome]
          \            /                             \            /
           v          v                               v          v
             [Utility]                                  [Utility]
```

### The Two Structural Departures from CDT
Comparing Equation \eqref{eq:cdt} and Equation \eqref{eq:afdt} reveals two fundamental structural shifts:

1. **Type Intervention vs. Token Intervention:** CDT applies Pearl's $\operatorname{do}$-operator to the physical node $\textsc{Act}$. A-FDT applies the operator to the logical node $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$. While $\textsc{Act}$ is a spatiotemporally localized token, $\mathtt{fdt}$ is an abstract mathematical type. Intervening on the output of this function propagates downstream along all edges departing from the function node in the dependency graph $G$. If a predictor’s past prediction was generated by simulating this decision function, that prediction is a child of $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ in $G$. Thus, intervening on $\mathtt{fdt}$ counterfactually modulates the prediction made yesterday without positing backwards physical causation.
2. **Observation-Indexed Interventions vs. Conditioning:** In CDT, upon observing evidence $x$, the agent conditions the causal model: $P(- \mid \operatorname{do}(\textsc{Act}=a), \textsc{Obs}=x)$. In A-FDT, the agent **does not condition on $x$ across the entire network**. Instead, the observation $x$ determines *which functional node in the graph is subjected to surgery*. When the agent's observation history shifts from $x$ to $y$, an A-FDT agent switches their surgery from $\operatorname{do}(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})=a)$ to $\operatorname{do}(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{y})=a)$. 

This second departure provides A-FDT with its characteristic "updateless" flavor (Dai 2009). The counterfactual evaluation $\operatorname{do}(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})=a)$ evaluates the global consequences across the graph of the algorithm having that output on input $x$. This structure permits counterfactual branches where the agent considers: *"What if the function $\mathtt{fdt}$, when fed $x$, returned an action that would have caused the environment to never show me $x$ in the first place?"*

---

## 3. Subjunctive Dependence and Counterpossible Semantics

The conceptual core of A-FDT is **subjunctive dependence**. Yudkowsky and Soares formulate the theory via an analogy: *Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*

Two physical processes subjunctively depend on a variable $Z$ if their behavioral manifests vary in accordance with the logical value of $Z$. Consider two physical calculators programmed with standard arithmetic, deployed simultaneously in Paris and Tokyo. If the Parisian calculator outputs $7336$ when computing $6288 + 1048$, an observer can assert with near certainty that the Tokyo calculator will also output $7336$. 

There is no physical signal propagating from Paris to Tokyo; no backwards-in-time causation links them. The calculators are correlated because their outputs are concrete tokens instantiated by the same abstract computational type: the function $+: \mathbb{N} \times \mathbb{N} \to \mathbb{N}$.

### Counterpossibles and Logical Uncertainty
In Equation \eqref{eq:afdt}, the agent evaluates the hypothetical:
$$\mathbb{E}\left[V \;\middle|\; \operatorname{do}\left(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right]$$
for alternative actions $a \in \mathcal{A}$. However, if the algorithm $\mathtt{fdt}$ is deterministic, then for the given input tuple $(\underline{P}, \underline{G}, \underline{x})$, it evaluates mathematically to a single unique action $a^* \in \mathcal{A}$.

Evaluating an alternative candidate action $a' \neq a^*$ requires evaluating the consequence of a mathematical falsehood:
$$\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a' \quad (a' \neq a^*)$$
In standard classical logic, a false antecedent implies everything (the principle of explosion: *ex falso quodlibet*). In standard Lewis-Stalnaker possible-world semantics (Lewis 1973), counterfactuals with impossible antecedents—termed **counterpossibles** (Cohen 1990, Bjerring 2013)—are vacuously true.

A-FDT bypasses this semantic triviality by operationalizing subjunctive dependencies via graphical surgery over structural representations. Rather than computing truth values over unconstrained logically impossible worlds, A-FDT utilizes an augmented causal graph $G$ where logical functions are embedded as nodes with explicit structural equations. The $\operatorname{do}$-operator over a logical node is an epistemic tool: it severs the internal computational proof-steps that determine the output of $\mathtt{fdt}$, replacing it with a constant assignment $a$, and propagates the consequences along the directed edges of $G$.

The source text is explicit that this graphical construction is an engineering bridge:
> *"Instead of a $\Do$ operator, FDT needs a $\True$ operator... Unfortunately, it's not clear how to define a $\True$ operator. Fortunately, we don't have to... Given a graph $G$ that tells us how changing a logical variable affects all other variables, we can re-use Pearl's $\Do$ operator to give a decision procedure for FDT."* (Section 5)

---

## 4. Rigorous Walkthrough of Canonical Dilemmas

We now apply the primary decision formula \eqref{eq:afdt} to the core canonical decision problems, tracing the distinct calculations of Eve (EDT), Carl (CDT), and Fiona (A-FDT).

### 4.1. Newcomb's Problem
The agent is presented with two boxes:
* **Box A:** Transparent, containing \$1,000.
* **Box B:** Opaque, containing either \$1,000,000 or \$0.
A predictor, possessing a 99% accuracy record, has previously placed \$1,000,000 in Box B if and only if she predicted the agent would forgo Box A ($\textit{onebox}$). The prediction is fixed; the agent chooses between taking only Box B ($\textit{onebox}$) or taking both boxes ($\textit{twobox}$).

```
          Fiona's Graph for Newcomb's Problem
          ===================================

                [ fdt(P, G) ]  <-- do(fdt = a)
                  /        \
                 /          \
                v            v
         [Prediction]     [ Act ]
              |              |
         +----+              |
         |                   |
         v                   v
      [Box B]  ---------> [Outcome]
                             |
                             v
                         [Utility]
```

**The Graphical Model:**
Let the nodes be defined as follows:
* Logical Function: $\mathtt{fdt} \in \{\textit{onebox}, \textit{twobox}\}$.
* Physical Action: $\textsc{Act} \in \{\textit{onebox}, \textit{twobox}\}$, with deterministic structural equation $\textsc{Act} = \mathtt{fdt}$.
* Reliability: $\textsc{Accurate} \in \{\textit{acc}, \textit{inacc}\}$, with $P(\textsc{Accurate}=\textit{acc}) = 0.99$.
* Prediction: $\textsc{Pred} \in \{1, 2\}$, with structural equation:
  $$\textsc{Pred} = \begin{cases} 1 & \text{if } (\mathtt{fdt}=\textit{onebox} \land \textsc{Acc}=\textit{acc}) \lor (\mathtt{fdt}=\textit{twobox} \land \textsc{Acc}=\textit{inacc}) \\ 2 & \text{otherwise} \end{cases}$$
* Payoff: $\textsc{Box B} = \textit{full}$ (\$1,000,000) if $\textsc{Pred}=1$, else $\textit{empty}$ (\$0).
* Utility: $V(\textit{onebox}, \textit{full}) = 10^6$; $V(\textit{twobox}, \textit{full}) = 10^6 + 10^3$; $V(\textit{onebox}, \textit{empty}) = 0$; $V(\textit{twobox}, \textit{empty}) = 10^3$.

**The A-FDT Evaluation:**
Fiona applies Equation \eqref{eq:afdt} (omitting empty observations $x$):
$$\mathrm{A\text{-}FDT}(P_F, G_F) = \operatorname*{argmax}_{a \in \{\textit{onebox}, \textit{twobox}\}} \mathbb{E}\left[V \;\middle|\; \operatorname{do}\left(\mathtt{fdt}(\underline{P_F}, \underline{G_F}) = a\right)\right]$$

1. **Evaluate Hypothetical $a = \textit{onebox}$:**
   Performing graph surgery $\operatorname{do}(\mathtt{fdt} = \textit{onebox})$ sets $\textsc{Act} = \textit{onebox}$ via its structural equation. Simultaneously, because $\textsc{Pred}$ has an incoming edge from $\mathtt{fdt}$, the intervention propagates to $\textsc{Pred}$:
   $$P(\textsc{Pred}=1 \mid \operatorname{do}(\mathtt{fdt}=\textit{onebox})) = P(\textsc{Acc}=\textit{acc}) = 0.99$$
   $$P(\textsc{Box B}=\textit{full} \mid \operatorname{do}(\mathtt{fdt}=\textit{onebox})) = 0.99$$
   The expected utility evaluates to:
   \begin{align*}
   \mathbb{E}[V \mid \operatorname{do}(\mathtt{fdt}=\textit{onebox})] &= 0.99 \cdot V(\textit{onebox}, \textit{full}) + 0.01 \cdot V(\textit{onebox}, \textit{empty}) \\
   &= 0.99(\$1{,}000{,}000) + 0.01(\$0) = \$990{,}000
   \end{align*}

2. **Evaluate Hypothetical $a = \textit{twobox}$:**
   Performing $\operatorname{do}(\mathtt{fdt} = \textit{twobox})$ sets $\textsc{Act} = \textit{twobox}$. Downstream:
   $$P(\textsc{Pred}=2 \mid \operatorname{do}(\mathtt{fdt}=\textit{twobox})) = P(\textsc{Acc}=\textit{acc}) = 0.99 \implies P(\textsc{Box B}=\textit{full}) = 0.01$$
   The expected utility evaluates to:
   \begin{align*}
   \mathbb{E}[V \mid \operatorname{do}(\mathtt{fdt}=\textit{twobox})] &= 0.01 \cdot V(\textit{twobox}, \textit{full}) + 0.99 \cdot V(\textit{twobox}, \textit{empty}) \\
   &= 0.01(\$1{,}001{,}000) + 0.99(\$1{,}000) = \$10{,}010 + \$990 = \$11{,}000
   \end{align*}

**Conclusion:** Since $\$990,000 > \$11,000$, A-FDT prescribes **$\textit{onebox}$**. 

Fiona leaves the \$1,000 behind not because of backward physical causation, but because the hypothetical in which her mathematical algorithm evaluates to $\textit{twobox}$ is a hypothetical in which the predictor's simulation of that algorithm returns 2, leaving Box B empty.

---

### 4.2. The Smoking Lesion Problem
Smoking is strongly correlated with fatal lung cancer ($V = \$0$ vs. $V = \$1,000,000$). However, the correlation is entirely driven by a common genetic lesion ($\textsc{Lesion}$). The lesion directly causes cancer 99% of the time and also alters the agent's brain chemistry to make them enjoy smoking ($+\$1,000$). Smoking has no direct causal path to cancer.

```
       Fiona's Graph for the Smoking Lesion Problem
       ============================================

                   [ Lesion ]
                  /          \
                 /            v
                v          [Cancer]
      +-----> [Act]           |
      |         |             v
      |         +--------> [Death]
      |                       |
   [fdt]                      v
(no edge to Cancer)       [Utility]
```

**The Graphical Model:**
* Predisposition: $\textsc{Lesion} \in \{\textit{lesion}, \textit{nolesion}\}$.
* Taste Profiles: An agent with the lesion has utility $\mathcal{U}_S$ (prefers smoking); an agent without has $\mathcal{U}_R$.
* The graph structure dictates that $\textsc{Cancer}$ depends causally on $\textsc{Lesion}$ and an exogenous noise factor $\textsc{Luck}$.
* Crucially, the decision function node $\mathtt{fdt}(\underline{P}, \underline{G})$ connects as a direct input to $\textsc{Act}$, but **there is no edge from $\mathtt{fdt}$ to $\textsc{Cancer}$**, because the biological lesion does not simulate, predict, or subjunctively track the agent's mathematical decision function.

**The A-FDT Evaluation:**
Fiona computes Equation \eqref{eq:afdt} where $p \coloneqq P(\textsc{Lesion}=\textit{lesion})$:
$$P(\textsc{Lesion}=\textit{lesion} \mid \operatorname{do}(\mathtt{fdt}=\textit{smoke})) = P(\textsc{Lesion}=\textit{lesion}) = p$$
Because $\textsc{Cancer}$ is non-descendant from $\mathtt{fdt}$, graph surgery on $\mathtt{fdt}$ leaves the probability of having cancer entirely unchanged:
$$P(\textsc{Cancer} \mid \operatorname{do}(\mathtt{fdt}=\textit{smoke})) = P(\textsc{Cancer} \mid \operatorname{do}(\mathtt{fdt}=\textit{refrain}))$$

Evaluating the expected utility under $\mathcal{U}_S$:
\begin{align*}
\mathbb{E}[V \mid \operatorname{do}(\mathtt{fdt}=\textit{smoke})] &= p(\$10{,}000 + \$1{,}000) + (1-p)(\$990{,}000 + \$1{,}000) \\
\mathbb{E}[V \mid \operatorname{do}(\mathtt{fdt}=\textit{refrain})] &= p(\$10{,}000) + (1-p)(\$990{,}000)
\end{align*}

The difference is strictly the pleasure of smoking:
$$\Delta \mathbb{E}[V] = +\$1{,}000$$

**Conclusion:** A-FDT prescribes **$\textit{smoke}$**. 

A-FDT breaks mere statistical correlations where no computational/subjunctive mechanism exists, avoiding EDT’s error, while preserving subjunctive dependencies where computational modeling occurs, avoiding CDT’s error.

---

### 4.3. The Transparent Newcomb Problem
In Drescher’s (2006) Transparent Newcomb Problem, both boxes are made of transparent glass. The agent directly observes whether Box B contains \$1,000,000 or \$0 before making their selection. 

The predictor placed \$1,000,000 in Box B if and only if she predicted that the agent would execute $\textit{onebox}$ *upon seeing both boxes full*. The agent walks up to the table and observes $\textsc{Obs} = \textit{full}$. Should they take both boxes?

* **Carl (CDT):** Conditions on $\textsc{Obs} = \textit{full}$. Intervenes via $\operatorname{do}(\textsc{Act}=a)$. Box B is already observed full ($P(\textsc{Box B}=\textit{full})=1$). Taking both boxes yields $\$1,001,000$; taking one yields $\$1,000,000$. CDT two-boxes.
* **Eve (EDT):** Given $\textsc{Obs} = \textit{full}$, Box B is fixed. Conditioning on $\textsc{Act}=\textit{twobox}$ yields $\$1,001,000$. EDT two-boxes.
* **The Result:** The predictor anticipates that CDT and EDT agents two-box when facing full boxes. Hence, the predictor leaves Box B empty. Carl and Eve walk away with \$1,000.

**The A-FDT Evaluation:**
Here, the second formal property of Equation \eqref{eq:afdt} becomes paramount: **A-FDT does not condition its hypothetical on the observation $x$ across the network.** It uses $x = \textit{full}$ to select which variable to intervene on:
$$\mathrm{A\text{-}FDT}(P_F, G_F, \textit{full}) = \operatorname*{argmax}_{a \in \{\textit{onebox}, \textit{twobox}\}} \mathbb{E}\left[V \;\middle|\; \operatorname{do}\left(\mathtt{fdt}(\underline{P_F}, \underline{G_F}, \underline{\textit{full}}) = a\right)\right]$$

```
     Fiona's Graph for Transparent Newcomb Problem
     =============================================

          [ fdt(P, G, full) ] <-- do(fdt(..., full) = a)
            /             \
           /               v
          v             [Prediction]
       [ Act ]             /     \
          ^               /       \
          |              v         v
   [Obs = full] <--- [Box B]    [Obs]
          |              \         /
          v               v       v
      [Outcome] -------> [ Utility ]
```

In Fiona’s dependency graph $G_F$:
1. The predictor simulates the algorithm run on input $\textit{full}$: $\mathtt{fdt}(\underline{P_F}, \underline{G_F}, \underline{\textit{full}})$.
2. If that procedure returns $\textit{onebox}$, the predictor places \$1,000,000 in Box B, which causes $\textsc{Obs}$ to be $\textit{full}$.
3. If that procedure returns $\textit{twobox}$, the predictor leaves Box B empty, which causes $\textsc{Obs}$ to be $\textit{empty}$.

When Fiona evaluates the counterfactual $\operatorname{do}(\mathtt{fdt}(\underline{P_F}, \underline{G_F}, \underline{\textit{full}}) = \textit{twobox})$, she evaluates a world where the procedure run upon seeing full boxes outputs $\textit{twobox}$. In that hypothetical world:
* The predictor predicts $\textit{twobox}$.
* The predictor leaves Box B empty ($\textsc{Pred}=2$).
* **Fiona never receives the observation $\textit{full}$ in the first place.** Instead, she receives $\textsc{Obs}=\textit{empty}$, and her physical action is determined by the distinct logical branch $\mathtt{fdt}(\underline{P_F}, \underline{G_F}, \underline{\textit{empty}})$.

Let $q$ denote Fiona's probability of two-boxing when Box B is empty (where $q=1$ is optimal). Then:
\begin{align*}
\mathbb{E}[V \mid \operatorname{do}(\mathtt{fdt}(\dots, \underline{\textit{full}})=\textit{onebox})] &= 0.99(\$1{,}000{,}000) + 0.01(q \cdot \$1{,}000) = \$990{,}000 + \$10q \\
\mathbb{E}[V \mid \operatorname{do}(\mathtt{fdt}(\dots, \underline{\textit{full}})=\textit{twobox})] &= 0.01(\$1{,}001{,}000) + 0.99(q \cdot \$1{,}000) = \$10{,}010 + \$990q
\end{align*}

For any $q \in [0, 1]$, $\$990,000 + \$10q > \$10,010 + \$990q$. 

**Conclusion:** A-FDT prescribes **$\textit{onebox}$**.

Fiona stands before two full transparent boxes and takes only Box B. By being the type of agent whose algorithm computes $\textit{onebox}$ on input $\textit{full}$, she guarantees that the predictor fills Box B in the first place. As Parfit (1986) noted in the structurally isomorphic Hitchhiker problem, an agent who cannot commit to paying upon arriving in the city is left to die in the desert. A-FDT agents survive Parfit's desert and walk out of Transparent Newcomb with \$1,000,000.

---

## 5. Summary Behavior Across Decision Dilemmas

The qualitative mechanisms and formal outputs of EDT, CDT, and A-FDT across standard decision-theoretic benchmarks are summarized in Table 1 below.

| Dilemma | EDT Prescription | CDT Prescription | A-FDT Prescription (Eq. 4) | A-FDT Mechanics & Payoff Advantage |
| :--- | :--- | :--- | :--- | :--- |
| **Newcomb’s Problem** | One-box ($\$10^6$) | Two-box ($\$10^3$) | **One-box ($\$10^6$)** | $\mathtt{fdt}$ node is parent to predictor's model; graph surgery updates Box B contents. |
| **Smoking Lesion** | Refrain ($\$990 \times 10^3$) | Smoke ($\$991 \times 10^3$) | **Smoke ($\$991 \times 10^3$)** | No edge from $\mathtt{fdt}$ to $\textsc{Cancer}$; severs non-computational statistical correlations. |
| **Transparent Newcomb** | Two-box ($\$10^3$) | Two-box ($\$10^3$) | **One-box ($\$10^6$)** | Intervenes on $\mathtt{fdt}(\dots,\underline{\textit{full}})$ without global conditioning; preserves prediction link. |
| **Parfit’s Hitchhiker** | Refuse to pay (Dies) | Refuse to pay (Dies) | **Pay driver (\$999,000)** | Isomorphic to Transparent Newcomb; driver predicts counterfactual payment in the city. |
| **Twin Prisoner’s Dilemma** | Cooperate ($\$10^6$) | Defect ($\$10^3$) | **Cooperate ($\$10^6$)** | Twin runs $\mathtt{fdt}$; graph surgery sets both twins' actions simultaneously. |
| **XOR Blackmail** | Pays blackmailer | Refuses to pay | **Refuses to pay** | Refusal hypothetical models blackmailer not sending the letter; resists epistemic extortion. |

---

## 6. Open Problems, Ambiguities, and Operational Proposals

While A-FDT displays remarkable performance across these benchmarks, its mathematical foundations contain foundational gaps that must be distinguished from its informal philosophical motivations.

```
       A-FDT's Theoretical Foundations: Core vs. Frontier
       ==================================================

       FORMALIZED IN SOURCE (Sec 5)         OPEN PROBLEMS / ACTIVE RESEARCH
       +-------------------------------+    +--------------------------------+
       | * Eq 4: do(fdt(P, G, x) = a)  |    | * Deducing G from data         |
       | * Graph surgery on types      | -> | * Subjunctive causal discovery |
       | * Joyce representation framing|    | * True counterpossible calculus|
       | * Updateless input-indexing   |    | * Multi-agent reflective loops |
       +-------------------------------+    +--------------------------------+
```

### 6.1. Deducing Subjunctive Graphs from Data
In Judea Pearl’s causal framework, the causal graph $G$ is not a primitive metaphysical given; it can be learned and tested from observational data and localized physical interventions via $d$-separation, conditional independence tests, and the do-calculus (Pearl 2000).

In A-FDT, the source admits that no such discovery calculus exists for subjunctive graphs:
> *"Pearl (2000) has given a compelling philosophical account of how to deduce the structure of causation from observation and experiment, but no such formal treatment has yet been given to the problem of deducing the structure of other kinds of subjunctive dependence... Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."* (Section 5)

When does a physical node in the world subjunctively depend on $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$? If an engineer builds an imperfect simulation of Fiona, what fraction of an edge connects $\mathtt{fdt}$ to that simulation? 

#### Operational Proposal
To make A-FDT operational on arbitrary, unfamiliar computational problems without hand-crafted graphs, we can formulate an information-theoretic criterion for subjunctive edge-assignment. 

Let $\mathcal{M}$ be a Turing machine representing an agent's code, and let $\mathcal{S}$ be a physical subsystem in the environment. Define the degree of subjunctive dependence $\sigma(\mathcal{S}, \mathcal{M})$ by the algorithmic mutual information (Kolmogorov complexity) shared between the execution traces of $\mathcal{M}$ and $\mathcal{S}$ that is invariant under input transformations:
\begin{equation}
\sigma(\mathcal{S}, \mathcal{M}) \coloneqq 1 - \frac{K(\operatorname{Tr}(\mathcal{S}) \mid \operatorname{Tr}(\mathcal{M}))}{K(\operatorname{Tr}(\mathcal{S}))}
\end{equation}
A directed edge $\mathtt{fdt} \to \mathcal{S}$ with transmission weight $\sigma$ is instantiated in $G$ whenever $\sigma(\mathcal{S}, \mathcal{M}) > 1 - \epsilon$. In Pearl's structural equation framework, this maps to expressing the structural equation of node $\mathcal{S}$ as:
\begin{equation}
\mathcal{S} = g\big(\operatorname{do}(\mathtt{fdt}), \eta_{\mathcal{S}}\big) \quad \text{with probability } \sigma(\mathcal{S}, \mathcal{M})
\end{equation}
where $\eta_{\mathcal{S}}$ represents exogenous environmental noise. While speculative, this proposal grounds subjunctive dependence in algorithmic information theory rather than primitive metaphysical intuition.

### 6.2. The Self-Referential Quining Problem
Equation \eqref{eq:afdt} contains an explicit self-reference:
$$\mathrm{A\text{-}FDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left[V \;\middle|\; \operatorname{do}\left(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right]$$
The algorithm takes as input a probability distribution $P$ and graph $G$ that already contain internal random variables $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ describing the output of the very function being computed.

The authors appeal to Kleene’s Second Recursion Theorem (Kleene 1938) to prove that such self-referential programs can be constructed without circular paradox. Kleene’s theorem establishes that for any computable function $F(x, y)$, there exists a program index $e$ such that $\varphi_e(y) = F(e, y)$. Hence, an algorithm can query its own source code via quining.

However, while Kleene’s theorem secures the syntactic existence of the code, it does not guarantee the existence of a unique, stable probability assignment $P$ over the agent’s own behavior. As demonstrated in game-theoretic contexts and the Death in Damascus dilemma, self-referential loops can induce non-convergent deliberation cycles. If an agent’s beliefs about their own decisions dictate their decision, and their decision dictates their beliefs, standard Bayesian kinematics breaks down. Solving this fully requires constructing probabilistic models over self-referential sentences, a domain currently investigated through reflective oracles (Fallenstein and Soares 2015) and logical induction (Garrabrant et al. 2016).

### 6.3. Action vs. Policy Formulation
The source paper notes an important operational distinction in Section 5 (Footnote 7 and Footnote 16):
> *"In the authors' preferred formalization of FDT, agents actually iterate over policies (mappings from observations to actions) rather than actions... [A-FDT] sets that distinction aside in this paper for ease of exposition."*

In **Policy-FDT**, the agent optimizes over the entire policy space $\Pi = \{\pi: \mathcal{X} \to \mathcal{A}\}$ from an initial or prior epistemic state:
\begin{equation}
\pi^* = \operatorname*{argmax}_{\pi \in \Pi} \mathbb{E}\left[V \;\middle|\; \operatorname{do}\big(\mathtt{Policy} = \pi\big)\right]
\label{eq:pfdt}
\end{equation}
and then deterministically executes $\pi^*(x)$ upon observing $x$.

In single-agent settings with static prediction, Equation \eqref{eq:afdt} (**A-FDT**) and Equation \eqref{eq:pfdt} (**Policy-FDT**) coincide, because the observation-indexed intervention $\operatorname{do}(\mathtt{fdt}(\dots,\underline{x})=a)$ preserves counterfactual policy evaluations across observation branches. However, in extensive-form multi-agent games with asymmetric information and sequential moves, A-FDT can encounter subtle coordination failures if distinct observation nodes $\mathtt{fdt}(\dots,\underline{x_1})$ and $\mathtt{fdt}(\dots,\underline{x_2})$ are treated as independently surgically manipulable without enforcing global policy consistency across information sets. In such advanced multi-agent settings, Policy-FDT is the more robust theoretical framework.

---

## 7. Conclusion: Instrumental Rationality and the Global Perspective

The historical controversy surrounding Newcomb’s problem and its descendants stemmed from an unexamined assumption: that an agent's counterfactual evaluations must intervene upon their localized physical body. This assumption forced a wedge between instrumental success and decision-theoretic orthodoxy. Causal decision theorists were compelled to defend two-boxing by claiming that Newcomb-like environments "punish rationality," conceding that rational agents systematically end up poorer.

Action Functional Decision Theory (A-FDT) resolves this tension by realigning decision theory with instrumental rationality. By intervening on the **type** (the mathematical algorithm $\mathtt{fdt}$) rather than the **token** (the physical act $\textsc{Act}$), A-FDT constructs hypotheticals that respect the logical and subjunctive dependencies inherent in an environment containing predictors, simulations, and algorithmic copies.

Under A-FDT, rationality is evaluated from a global perspective: an agent maximizes expected utility across the world as a whole, asking:
$$\textit{"Which output of this very decision procedure produces the best overall universe?"}$$

A-FDT achieves this without the ad-hoc patches of ratification, without the superstitious self-blinding of EDT, and without the temporal incoherence of CDT precommitments. It demonstrates that a single, unified mathematical rule can one-box in Newcomb’s problem, smoke in the Smoking Lesion problem, pay the driver in Parfit's hitchhiker problem, and systematically out-compete rival theories. While foundational challenges remain in learning subjunctive dependency graphs and formalizing counterpossible logic, A-FDT represents a significant conceptual and mathematical advance toward a truly general theory of rational choice.

---

## References

* Adams, E. W. (1970). Subjunctive and indicative conditionals. *Foundations of Language*, 6(1), 89–94.
* Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
* Arntzenius, F. (2008). No regrets, or: Edith Piaf revamps decision theory. *Erkenntnis*, 68(2), 277–297.
* Bjerring, J. C. (2013). On counterpossibles. *Philosophical Studies*, 168(2), 1–27.
* Cohen, D. (1990). On what cannot be. In *Truth or Consequences: Essays in Honor of Nuel Belnap*, 123–132. Kluwer Academic Publishers.
* Dai, W. (2009). Towards a new decision theory. *LessWrong*.
* Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Eells, E. (1984). Metatickles and the dynamics of deliberation. *Theory and Decision*, 17(1), 71–95.
* Egan, A. (2007). Some counterexamples to causal decision theory. *Philosophical Review*, 116(1), 93–114.
* Fallenstein, B., & Soares, N. (2015). Toward idealized decision theory. *arXiv:1507.01986*.
* Garrabrant, S., Benson-Tilsen, T., Critch, A., Soares, N., & Taylor, J. (2016). Logical induction. *arXiv:1609.03543*.
* Gibbard, A., & Harper, W. L. (1978). Counterfactuals and two kinds of expected utility. In *Foundations and Applications of Decision Theory*, 125–162. D. Reidel.
* Jeffrey, R. C. (1983). *The Logic of Decision* (2nd ed.). University of Chicago Press.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Joyce, J. M. (2012). Regret and instability in causal decision theory. *Synthese*, 187(1), 123–145.
* Kleene, S. C. (1938). On notation for ordinal numbers. *Journal of Symbolic Logic*, 3(4), 150–155.
* Lewis, D. (1973). *Counterfactuals*. Harvard University Press.
* Lewis, D. (1979). Prisoners' dilemma is a Newcomb problem. *Philosophy & Public Affairs*, 8(3), 235–240.
* Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
* Nozick, R. (1969). Newcomb's problem and two principles of choice. In *Essays in Honor of Carl G. Hempel*, 114–146. D. Reidel.
* Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
* Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Skyrms, B. (1980). *Causal Necessity*. Yale University Press.
* Soares, N., & Fallenstein, B. (2015). Toward idealized decision theory. *arXiv:1507.01986*.
* Spohn, W. (1977). Where Luce and Krantz do really generalize Savage's decision model. *Erkenntnis*, 11(1), 113–134.
* Yudkowsky, E. (2010). Timeless decision theory. *Singularity Institute for Artificial Intelligence*.
* Yudkowsky, E., & Soares, N. (2017). Functional decision theory: A new theory of instrumental rationality. *arXiv:1710.05060*.