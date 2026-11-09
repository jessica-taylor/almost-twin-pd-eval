# 020_fdt_eq4_google_gemini-3.8-flash_rlow_plow / 00012

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/be605a01-1be3-4b90-8905-951ee816d5c8/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/be605a01-1be3-4b90-8905-951ee816d5c8/call_0/response.raw) · finish: `stop`

### Visible response

````text
# Intervening on the Type: The Mathematics and Mechanics of Action Functional Decision Theory (A-FDT)

## 1. Introduction: The Epistemic Perspective of Choice

For decades, the foundations of normative decision theory have been defined by an unyielding duel between Evidential Decision Theory (EDT) and Causal Decision Theory (CDT). The classical battleground is well-trodden: in Newcomb-like dilemmas, EDT typically prescribes taking one box, observing that an unchosen million dollars is good news; CDT adamantly prescribes taking both boxes, arguing that because the predictor’s funds are already placed, an agent’s physical action cannot causally alter the past. Conversely, in common-cause dilemmas like the Smoking Lesion problem, CDT correctly recommends smoking, recognizing that lighting a cigarette does not cause an arterial cancer lesion, whereas naive formulations of EDT infamously suggest abstention to manage the statistical "news."

This deadlock has historically been treated as exhaustive. As Allan Gibbard and William Harper observed in their seminal 1978 work, rational agents seem forced to choose between the counterfactual realism of CDT (and accept leaving \$1,000,000 on the table in Newcomb's problem) and the diagnostic sensitivity of EDT (and risk irrational superstition in common-cause settings).

Eliezer Yudkowsky and Nate Soares challenge this binary by formulating a new paradigm: *Functional Decision Theory*. In this essay, we examine the formal variant developed in Section 5 of their foundational paper—which we designate **Action Functional Decision Theory (A-FDT)**. Rather than evaluating candidate physical behaviors or passive conditional updates, A-FDT evaluates the outputs of a mathematical decision algorithm. 

As James Joyce demonstrated in his 1999 axiomatic representation theorem, all expected utility theories share a core formal architecture:
\begin{equation}
\mathcal{EU}(a) \coloneqq \sum_{j} P(a \then o_j ;\, x) \, \mathcal{U}(o_j),
\label{eq:joyce_general}
\end{equation}
where $a \in \mathcal{A}$ is an action, $x \in \mathcal{X}$ is the agent's observation history, $o_j \in \mathcal{O}$ are outcomes, and $\mathcal{U}$ is a bounded real-valued utility function. Joyce noted that rival decision theories do not disagree about how an agent *values* outcomes; they disagree about the connective $\then$—the "epistemic perspective" from which counterfactuals are evaluated.

* Evidential Decision Theory sets $P(a \then o_j ;\, x) = P(o_j \mid x, a)$, identifying counterfactuals with ordinary Bayesian conditionalization.
* Causal Decision Theory invokes Judea Pearl's causal intervention operator $\mathtt{do}(\cdot)$, setting $P(a \then o_j ;\, x) = P(o_j \mid \mathtt{do}(\mathtt{Act} = a), x)$, which models a physical surgery on the agent's physical body.
* **A-FDT** re-interprets counterfactual surgery. Instead of intervening on the physical token $\mathtt{Act}$, A-FDT intervenes on an abstract variable representing the *mathematical type* of the agent's decision procedure itself.

The goal of this essay is to unpack the mathematical mechanics of A-FDT, clarify how it formalizes counterfactual dependencies without retrocausality, detail its execution across classic decision dilemmas, and identify the rigorous formal questions that remain open.

---

## 2. Formal Specification of A-FDT

### 2.1 The Foundational Rule: Equation (4)

The primary formal presentation of A-FDT appears in Equation (4), Section 5 of Yudkowsky and Soares:
\begin{equation}
\operatorname{A-FDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\Big(\mathcal{V} \;\Big|\; \mathtt{do}\big(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\big)\Big),
\label{eq:afdt_core}
\end{equation}
where:
1. $P$ is a subjective joint probability distribution over a set of random variables describing the agent, the environment, and relevant computational processes.
2. $G = (V, E)$ is a directed acyclic graph (DAG) representing the dependency structure of the world. Crucially, whereas CDT restricts $E$ strictly to physical causal links, $G$ in A-FDT includes *subjunctive* and *logical* dependencies.
3. $x \in \mathcal{X}$ is the agent's concrete observation history.
4. $\mathcal{V} = \mathcal{U}(\mathtt{Outcome})$ is the payoff variable whose expectation the agent seeks to maximize.
5. The underline notation $\underline{P}, \underline{G}, \underline{x}$ denotes syntactic *dequoting* (or structural reification). The expression $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ is not a recursive functional call inside the evaluation loop; it is the literal variable name within the model representing the evaluation of the decision algorithm $\operatorname{A-FDT}$ on those specific arguments.
6. $\mathtt{do}(\cdot)$ is Pearl’s graph-surgery operator, adapted to cut the incoming structural equations of the logical node $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ and fix its value to candidate action $a$.

### 2.2 Distinguishing A-FDT from CDT

To appreciate the mathematical shift in Equation \eqref{eq:afdt_core}, recall Pearl's formalization of CDT:
\begin{equation}
\operatorname{CDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\Big(\mathcal{V} \;\Big|\; \mathtt{do}(\mathtt{Act} = a),\, \mathtt{Obs} = x\Big).
\label{eq:cdt_formal}
\end{equation}
Comparing Equation \eqref{eq:afdt_core} with Equation \eqref{eq:cdt_formal} exposes two foundational divergences:

1. **Target of Intervention (Type vs. Token):** In CDT, the surgery $\mathtt{do}(\mathtt{Act} = a)$ severs the edge between the physical act $\mathtt{Act}$ and its immediate parents (such as the agent's mental state, deliberation, or algorithmic predisposition). In A-FDT, the surgery targets the logical node $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$. Because this node represents the mathematical mapping itself, any node in $G$ that calculates, predicts, or mirrors this function is downstream of the intervention in $G$.
2. **Handling Evidence (Intervention Point vs. Conditioning):** In CDT, receiving an observation $x$ means conditioning the distribution upon $\mathtt{Obs} = x$. In A-FDT, the observation $x$ *indexes which logical node is subject to surgery*. When the observation changes from $x$ to $y$, A-FDT shifts its intervention from $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ to $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{y})$, without necessarily conditioning on having observed $y$ in the counterfactual hypotheticals. As we will see, this subtle property provides A-FDT with immunity against extortion and dynamic inconsistency.

### 2.3 Self-Reference and Quining

A natural mathematical worry is that $\operatorname{A-FDT}(P, G, x)$ appears self-referential: the function takes $P$ and $G$ as inputs, while $P$ and $G$ contain a variable named after the function itself applied to $(P, G, x)$.

Yudkowsky and Soares note that this self-reference is formally benign. By Kleene's Second Recursion Theorem, any computable function can access its own source code (or Gödel index). Through standard "quining" techniques, a program can construct an exact description of its own data structure and logic without entering an infinite regress. 

An A-FDT agent does not need to know the *output value* of $\operatorname{A-FDT}(P, G, x)$ before solving Equation \eqref{eq:afdt_core}; it merely requires an identified node in its graphical model labeled $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ that acts as an abstract input to other nodes.

---

## 3. Subjunctive Dependence: Mathematics Beyond Physical Causality

### 3.1 The Analogy of the Twin Calculators

To understand what edges in $G$ represent for an A-FDT agent, consider two standard electronic pocket calculators, $C_1$ in Paris and $C_2$ in Tokyo, both computing $6288 + 1048$. There is no physical wire connecting $C_1$ and $C_2$, nor does a relativistic signal pass between them. Yet their outputs are rigidly correlated: if $C_1$ displays $7336$, an observer can deduce with near-certainty that $C_2$ also displays $7336$.

If one asks the counterfactual question: *"What would $C_2$ display if $C_1$ displayed $8000$?''*, two interpretations arise:
* **The Token/Causal View:** Intervene physically on $C_1$'s display panel (e.g., cross a wire or crack the LCD). The operation of $C_2$ is unaffected; $C_2$ still outputs $7336$.
* **The Type/Subjunctive View:** Ask what would obtain if the arithmetic problem $(6288 + 1048)$ evaluated to $8000$. Under this counter-to-logic antecedent, any machine faithfully calculating that same sum would also display $8000$.

A-FDT explicitly embraces the latter stance. When an agent deliberates, it models itself as an instantiation of an abstract computation. Physical systems in the universe that run the same computation, or that simulate that computation to make predictions, are **subjunctively dependent** upon the output of the computation. 

```
               [ Mathematical Function: fdt(P, G, x) ]
                            /               \
                           /                 \
                          v                   v
              [ Physical Act: Act ]    [ Predictor's Model ]
                          \                   /
                           \                 /
                            v               v
                         [ Concrete Outcome: V ]
```

Subjunctive dependence generalizes physical causation: physical causation is simply the special case where the dependence is mediated by temporal, local physical dynamics. But where two systems share a common computational or logical core, their behaviors covary across logical hypotheticals without requiring retrocausal physical signaling.

### 3.2 Counterpossible Conditionals and the $\mathtt{true}$ Operator

The authors distinguish between an idealized semantic operator, $\mathtt{true}(\phi)$, and their practical implementation via Pearl's graph surgery $\mathtt{do}(\cdot)$.

In an ideal epistemic setting, evaluating a counterfactual whose antecedent alters the result of a deterministic computation requires evaluating a **counterpossible conditional**—a conditional whose antecedent is mathematically or logically impossible (e.g., "if $6288 + 1048 = 8000$"). If an idealized operator $\mathtt{true}(\cdot)$ existed, an agent could evaluate:
\begin{equation}
\operatorname{A-FDT}^*(P, x) = \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\Big(\mathcal{V} \;\Big|\; \mathtt{true}\big(\mathtt{fdt}(\underline{P}, \underline{x}) = a\big)\Big).
\label{eq:fdt_star}
\end{equation}
However, standard probability theory collapses under logically false conditions: if $\phi$ is mathematically impossible, $P(\phi) = 0$, rendering conditional probabilities $P(\cdot \mid \phi)$ undefined. Although frameworks for logical uncertainty and non-trivial counterpossibles exist (e.g., Garber 1983; Gaifman 2004; Bjerring 2013), they lack a universally accepted, computationally tractably standard.

To bypass this hurdle, Yudkowsky and Soares make an engineering move: they supply the agent with an augmented graph $G$ that explicitly includes logical variables alongside physical variables. By declaring that the logical variable $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ sits at the root of a subgraph that feeds into both the agent's physical motor system ($\mathtt{Act}$) and the predictor's past prediction ($\mathtt{Prediction}$), Pearl’s standard $\mathtt{do}(\cdot)$ operator can be imported directly. 

Equation \eqref{eq:afdt_core} is therefore an operationalized approximation of Equation \eqref{eq:fdt_star}: it allows the agent to calculate well-defined expectations over structural equations, treating the output of its decision procedure as a variable that can be intervened upon within a directed graph.

---

## 4. Applying A-FDT Across Classic Decision Problems

We now trace the precise mathematical evaluation of Equation \eqref{eq:afdt_core} across pivotal dilemmas, contrasting Fiona (an A-FDT agent) with Carl (a CDT agent) and Eve (an EDT agent).

### 4.1 Newcomb's Problem

Let Box A contain \$1,000 (transparent) and Box B contain either \$1,000,000 or \$0 (opaque). A 99% reliable predictor places \$1,000,000 in Box B if and only if she predicted that the agent leaves Box A behind. The prediction was completed yesterday.

#### Carl (CDT): Two-Boxing
Carl represents the dilemma via the causal DAG:
$$\mathtt{Predisposition} \to \mathtt{Act} \to \mathtt{Outcome} \leftarrow \mathtt{Box\ B} \leftarrow \mathtt{Prediction} \leftarrow \mathtt{Predisposition}$$
When Carl calculates his decision via Equation \eqref{eq:cdt_formal}, he applies $\mathtt{do}(\mathtt{Act} = \text{onebox})$ and $\mathtt{do}(\mathtt{Act} = \text{twobox})$. Because $\mathtt{Act}$ has no directed causal paths leading backward into $\mathtt{Box\ B}$, the surgery severs the link from $\mathtt{Predisposition}$ to $\mathtt{Act}$. Consequently:
$$P(\mathtt{Box\ B} = \text{full} \mid \mathtt{do}(\mathtt{Act} = \text{onebox})) = P(\mathtt{Box\ B} = \text{full} \mid \mathtt{do}(\mathtt{Act} = \text{twobox})) = p.$$
Carl evaluates:
$$\mathbb{E}(\mathcal{V} \mid \mathtt{do}(\text{twobox})) = p(\$1,001,000) + (1-p)(\$1,000) = p(\$1,000,000) + \$1,000,$$
$$\mathbb{E}(\mathcal{V} \mid \mathtt{do}(\text{onebox})) = p(\$1,000,000).$$
Because $\$1,000 > \$0$ for all $p \in [0, 1]$, Carl rigidly takes two boxes and walks away with \$1,000.

#### Fiona (A-FDT): One-Boxing
Fiona's graph $G^F$ recognizes that both her bodily movements ($\mathtt{Act}$) and the predictor's estimate ($\mathtt{Prediction}$) are children of her decision algorithm $\mathtt{fdt}(\underline{P^F}, \underline{G^F})$.
* Intervening with $\mathtt{do}(\mathtt{fdt}(\underline{P^F}, \underline{G^F}) = \text{onebox})$ sets $\mathtt{Act} = \text{onebox}$ with probability 1, and propagates through the graph to set $\mathtt{Prediction} = 1$ with probability 0.99. Thus, $P(\mathtt{Box\ B} = \text{full}) = 0.99$.
* Intervening with $\mathtt{do}(\mathtt{fdt}(\underline{P^F}, \underline{G^F}) = \text{twobox})$ sets $\mathtt{Act} = \text{twobox}$ with probability 1, and sets $\mathtt{Prediction} = 2$ with probability 0.99. Thus, $P(\mathtt{Box\ B} = \text{full}) = 0.01$.

Now Fiona evaluates Equation \eqref{eq:afdt_core}:
$$\mathbb{E}\big(\mathcal{V} \mid \mathtt{do}(\mathtt{fdt} = \text{onebox})\big) = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000,$$
$$\mathbb{E}\big(\mathcal{V} \mid \mathtt{do}(\mathtt{fdt} = \text{twobox})\big) = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$
Fiona’s argmax selects $\text{onebox}$. The predictor, correctly modeling Fiona's decision algorithm, has placed the \$1,000,000 in Box B. Fiona walks away rich.

### 4.2 The Smoking Lesion Problem

An arterial lesion causes both a strong desire to smoke and lung cancer (99% probability). There is no direct causal path between smoking and cancer. Smoking grants \$1,000 in utility; being cancer-free is worth \$1,000,000.

* **Eve (EDT)** notices that smoking is statistically correlated with the lethal lesion. Conditioning on $\mathtt{Act} = \text{smoke}$ yields an alarming posterior probability of cancer; she abstains, needlessly depriving herself of \$1,000 while remaining vulnerable to the underlying lesion.
* **Carl (CDT)** notes that smoking does not cause the lesion and smokes.

How does **Fiona (A-FDT)** resolve this without falling into Eve's trap?

In the smoking lesion scenario, the arterial lesion is a purely biological, non-cognitive entity. It is not running a predictive simulation of Fiona’s decision algorithm $\mathtt{fdt}$. Rather, as formalized in Section 6, the lesion determines whether Fiona's utility function is $\mathcal{U}_S$ (valuing smoking positively) or $\mathcal{U}_R$ (valuing smoking negatively).

Fiona’s graph $G^F$ places $\mathtt{Lesion}$ upstream of her decision function's environment, but there is **no arrow** running from the logical node $\mathtt{fdt}$ to $\mathtt{Lesion}$ or $\mathtt{Cancer}$:
$$\mathtt{fdt}(\underline{P_S^F}, \underline{G^F}) \to \mathtt{Act} \leftarrow \mathtt{Lesion} \to \mathtt{Cancer} \to \mathtt{Death} \to \mathcal{V}$$
When Fiona performs the counterfactual surgery $\mathtt{do}(\mathtt{fdt} = \text{smoke})$, the intervention propagates strictly down to $\mathtt{Act}$ and $\mathcal{V}$. It cannot propagate backward against the directed edge coming from $\mathtt{Lesion}$. Therefore:
$$P(\mathtt{Lesion} \mid \mathtt{do}(\mathtt{fdt} = \text{smoke})) = P(\mathtt{Lesion} \mid \mathtt{do}(\mathtt{fdt} = \text{refrain})) = p.$$
Because the probability of having cancer remains fixed at $p$ across both hypotheticals, the extra \$1,000 from smoking is realized in both cases:
$$\mathbb{E}(\mathcal{V} \mid \mathtt{do}(\mathtt{fdt} = \text{smoke})) - \mathbb{E}(\mathcal{V} \mid \mathtt{do}(\mathtt{fdt} = \text{refrain})) = p(\$1,000) > 0.$$
A-FDT prescribes smoking. Thus, A-FDT uniquely pairs one-boxing in Newcomb's problem with smoking in the Smoking Lesion problem—a combination long argued by causal theorists to be conceptually incompatible.

### 4.3 The Transparent Newcomb Problem and Parfit's Hitchhiker

The true structural distinctiveness of A-FDT emerges in problems involving real-time observation of past predictions.

In the **Transparent Newcomb Problem**, both boxes are transparent. An agent sees ahead of time whether Box B contains \$1,000,000. The predictor placed the money in Box B if and only if she predicted that the agent, upon *seeing two full boxes*, would take only Box B.

Suppose the agent stands in front of two full boxes:
* **Carl (CDT)** conditions on $\mathtt{Obs} = \text{full}$, then intervenes with $\mathtt{do}(\mathtt{Act})$. Seeing the million dollars already present, Carl takes both boxes: $\mathbb{E}(\mathcal{V} \mid \mathtt{do}(\text{twobox}), \mathtt{Obs} = \text{full}) = \$1,001,000$.
* **Eve (EDT)** already knows Box B is full ($\mathtt{Obs} = \text{full}$). Conditioning on $\mathtt{Act} = \text{twobox}$ cannot lower her probability that Box B is full (it is already 1). She too takes both boxes.

Because Carl and Eve are transparently two-boxers upon seeing both boxes full, an accurate predictor leaves Box B empty. Both walk away with \$0 (or \$1,000 if they take the remaining box).

#### Fiona’s Evaluation via Equation (4)
Fiona observes $\mathtt{Obs} = \text{full}$. However, according to Equation \eqref{eq:afdt_core}, Fiona **does not condition her counterfactual world-model on the observation**. Instead, the observation determines which logical variable she intervenes upon.

Fiona intervenes on $\mathtt{fdt}(\underline{P^F}, \underline{G^F}, \underline{\text{full}})$. Her graphical model (Figure 6b in the paper) specifies that the predictor's past prediction depends directly on the output of this conditional procedure:
* If $\mathtt{do}\big(\mathtt{fdt}(\dots, \underline{\text{full}}) = \text{onebox}\big)$, the predictor predicted that Fiona would one-box when seeing a full box. The predictor filled the box. Fiona finds herself in the branch where Box B is full, taking only Box B: expected return $\approx \$1,000,000$.
* If $\mathtt{do}\big(\mathtt{fdt}(\dots, \underline{\text{full}}) = \text{twobox}\big)$, the predictor predicted defection. The predictor did *not* fill Box B. Fiona realizes that under this counterfactual algorithm, she would have observed an *empty* box instead, yielding at best \$1,000.

Fiona reasons: *"If the algorithm governing my behavior when seeing two full boxes were to output $\text{twobox}$, I would almost certainly not be standing in front of two full boxes right now."* She one-boxes, walks away with \$1,000,000, and avoids the barren desert that claims CDT and EDT agents.

This matches **Parfit’s Hitchhiker Problem**: a driver rescues a stranded traveler in the desert only if the driver accurately predicts that the traveler will pay \$1,000 at an ATM upon arriving in the city. CDT and EDT agents refuse to pay once safe in the city, so they are left to die in the desert. An A-FDT agent pays the \$1,000 in the city, recognizing that the counterfactual hypothetical $\mathtt{do}(\mathtt{fdt}(\dots) = \text{refuse})$ subjunctively entails remaining in the desert.

---

## 5. Structural Comparison Matrix

The table below systematizes how EDT, CDT, and A-FDT operate across core decision dilemmas:

| Decision Problem | EDT Prescription | CDT Prescription | A-FDT Prescription | Why A-FDT Succeeds |
| :--- | :--- | :--- | :--- | :--- |
| **Newcomb’s Problem** | One-box (1B) | Two-box (2B) | **One-box (1B)** | Intervenes on the decision type, recognizing that the past prediction subjunctively depends on $\mathtt{fdt}$. |
| **Smoking Lesion** | Refrain (irrationally) | Smoke | **Smoke** | Correctly detects that the lesion's manifestation does not subjunctively depend on the algorithm $\mathtt{fdt}$. |
| **Transparent Newcomb** | Two-box (leaves empty) | Two-box (leaves empty) | **One-box (rich)** | Evaluates the counterfactual impact of the algorithm without conditioning away the dependence of the observation. |
| **Parfit’s Hitchhiker** | Refuse payment (dies) | Refuse payment (dies) | **Pay \$1,000 (lives)** | Recognizes that having been rescued subjunctively depends on paying upon arrival. |
| **XOR Blackmail** | Pays blackmailer | Refuses | **Refuses** | Treats termite presence as subjunctively independent of the decision to pay, despite the letter's news value. |
| **Death in Damascus** | Flees or destabilizes | Dynamic instability | **Stays in Damascus** | Accepts unavoidable mortality without wasting \$1,000 fleeing to Aleppo. |

---

## 6. Open Problems, Underdetermined Elements, and Formal Proposals

While A-FDT presents a compelling pragmatic architecture, Yudkowsky and Soares acknowledge significant formal gaps. To make A-FDT fully operational on unfamiliar cases, several underdetermined mechanisms must be addressed.

### 6.1 The Epistemic Origin of $G$: Learning Subjunctive Dependencies

#### The Underdetermined Problem
In CDT, Pearl’s causal discovery algorithms (e.g., the IC/PC algorithms) infer DAG structures from conditional independence relations observed across randomized physical trials. In A-FDT, the graph $G$ is simply assumed as an input. The source article explicitly admits:
> *"Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."* (Section 5)

Without an objective protocol for drawing subjunctive edges, an agent could draw spurious logical connections (leading to superstition) or omit real predictive dependencies (collapsing back into CDT).

#### A Proposed Operational Interpretation
We can formalize a principled method for constructing subjunctive graphs through **Algorithmic Information Theory and Program Slicing**:

Let an agent's environment be modeled as an ensemble of interacting programs $\Pi = \{M_1, M_2, \dots, M_k\}$. Let $M_{\text{agent}}$ be the agent's decision program. 
1. **Computational Dependency:** We define variable $X$ in the environment as subjunctively dependent on $\mathtt{fdt}$ if, in the minimal algorithmic description of the world (in the sense of Kolmogorov complexity), the execution trace of the program computing $X$ invokes an emulation, simulation, or structural isomorphism of $M_{\text{agent}}$.
2. **Edge Construction:** In the graph $G$, draw a directed edge $\mathtt{fdt} \to X$ if and only if the evaluation of $X$ requires evaluating a sub-routine that takes the agent’s code and observations as input. 

This operational rule cleanly bifurcates our test cases:
* In Newcomb's problem, the predictor explicitly simulates $M_{\text{agent}}$; hence an edge $\mathtt{fdt} \to \mathtt{Prediction}$ is mandated.
* In the Smoking Lesion, the biological cancer lesion runs no algorithmic simulation of $M_{\text{agent}}$; hence no edge $\mathtt{fdt} \to \mathtt{Lesion}$ exists.

### 6.2 The "Updatelessness" Dilemma: Action vs. Policy Selection

#### The Source Article's Ambiguity
A critical mathematical tension exists between Equation (4) and the broader commitments of functional decision theorists:
* **Equation (4)** explicitly optimizes over an *action*:
  $$\operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\Big(\mathcal{V} \;\Big|\; \mathtt{do}\big(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\big)\Big).$$
* Yet in Footnotes 7 and 16, the authors concede that their *preferred* formalization of FDT intervenes on an abstract node $\mathtt{fdt}(-)$ to choose a whole **policy** $\pi: \mathcal{X} \to \mathcal{A}$, mapping observations to actions:
  $$\pi^* = \operatorname*{argmax}_{\pi \in \mathcal{A}^\mathcal{X}} \mathbb{E}\Big(\mathcal{V} \;\Big|\; \mathtt{do}\big(\mathtt{FDT\_Policy} = \pi\big)\Big),$$
  subsequently setting $\mathtt{Act} = \pi^*(x)$.

Equation (4) as written is **action-functional**: the agent selects an action $a$ by intervening on the output of the function evaluated at the *current observation* $x$. This works seamlessly in Transparent Newcomb because the predictor directly predicts the output of $\mathtt{fdt}(\dots, \underline{\text{full}})$. 

However, in extensive games where an adversary predicts how an agent would act under an observation that the agent *did not actually receive*, intervening strictly on $\mathtt{fdt}(\dots, \underline{x})$ fails to affect the adversary's prediction about unreached counterfactual branches. True "policy-based" (or updateless) decision theory resolves this by having the agent deliberate from an ex-ante perspective, choosing a comprehensive mapping across all possible observations. 

To bridge this gap, we can define the relationship between the two formalisms: **Equation (4) represents the modular projection of a policy-level functional decision theory onto a fixed observation $x$, valid whenever the environment’s predictors condition their behavior on the agent’s specific response to $x$.** When facing predictors that sample across non-actual observation branches, the agent must ascend from A-FDT to Policy-FDT.

### 6.3 Defining "Fair" Dilemmas

A persistent objection against A-FDT (dating back to Gibbard and Harper) is that any decision theory can be made to look optimal if we posit an omnipotent entity that punishes agents for adopting any *other* theory. For example, consider an "anti-FDT demon" who gives \$1,000,000 to an agent if and only if she predicts the agent follows CDT. In that scenario, Carl thrives and Fiona starves.

Yudkowsky and Soares argue that A-FDT dominates in all **fair dilemmas**, which they informally characterize as dilemmas where the environment rewards or punishes an agent based on the agent's *actions* rather than her internal cognitive constitution. But they leave the formalization of "fairness" open.

#### A Proposed Formalization of Dilemma Fairness
A decision dilemma represented by a DAG $G = (V, E)$ and utility $\mathcal{V}$ is **constitutionally fair** if:
1. Every directed path from the agent's internal cognitive states (nodes representing the decision procedure or source code) to the payoff node $\mathcal{V}$ passes through the physical action node $\mathtt{Act}$.
2. If an environmental node $W$ (such as a predictor) is downstream of the agent's computational type $\mathtt{fdt}$, $W$'s functional specification depends only on the mapping $\mathtt{fdt}(\dots) = a$, rather than on syntactic properties of the code (such as execution time, memory usage, or theoretical label).

Under this criterion:
* Newcomb's problem is fair: the predictor rewards the *action* of leaving Box A behind, regardless of what philosophy motivated it.
* The "punish FDT agents" dilemma is unfair: the utility node is directly coupled to the internal algorithm identity, bypassing behavioral choice.

If this definition holds, A-FDT establishes an impressive normative claim: **In the class of all constitutionally fair predictive environments, A-FDT achieves an expected utility that is greater than or equal to that of CDT and EDT.**

---

## 7. A Step-by-Step Recipe for Deciding Unfamiliar Cases

To enable a researcher to apply A-FDT to novel, complex decision problems, we summarize the theory into an actionable, four-step operational algorithm:

1. **Step 1: Construct the Subjunctive Graph $G$**
   * Identify all physical variables, environmental predictors, and payoffs.
   * Add a logical node $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ representing the decision algorithm for observation history $x$.
   * Identify all systems in the environment that predict, emulate, or mirror this decision. Draw directed edges from $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ to these predictive nodes.
   * Draw an edge from $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ to the physical motor action $\mathtt{Act}$.
   * **Rule of Caution:** Do not draw edges from $\mathtt{fdt}$ to environmental nodes that merely share a non-cognitive, statistical correlation with the agent (e.g., biological lesions, random ambient noise).

2. **Step 2: Identify the Counterfactual Interventions**
   * Do not condition your probability distribution on having seen observation $x$.
   * Instead, iterate over every candidate action $a \in \mathcal{A}$ by setting up the hypothetical graph $G_{\bar{a}}$ where all incoming arrows to $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ are cut, and its value is fixed to $a$:
     $$\mathtt{do}\big(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\big).$$

3. **Step 3: Propagate Structural Values Downstream**
   * For each candidate action $a$, compute the downstream values of all variables connected to $\mathtt{fdt}(\dots)$ in $G_{\bar{a}}$.
   * Update the predictions of simulated models, the physical actions taken, and the resulting utility payoffs $\mathcal{V}$.
   * Calculate the expected utility $\mathbb{E}\big(\mathcal{V} \mid \mathtt{do}(\mathtt{fdt} = a)\big)$ using the baseline probability distribution $P$ over external parameters unaffected by the intervention.

4. **Step 4: Execute the Argmax**
   * Select the physical act $a^*$ that maximizes this expectation. Output $a^*$.

---

## 8. Conclusion: Rationality as Algorithmic Optimization

Action Functional Decision Theory dissolves the decades-old conflict between Causal and Evidential Decision Theory by reconsidering what a rational decision operates upon. Where CDT conceptualizes choice as a physical intervention on a local, spatio-temporal token—blindly ignoring that its reasoning is being modeled by surrounding agents—EDT retreats to mere diagnostic conditionalization, conflating correlation with control.

A-FDT reveals that genuine instrumental rationality requires choosing from a **global perspective**. An agent is not merely a physical hand pushing a box; she is the localized physical execution of a non-local, eternal mathematical function. By intervening directly on the logical type of its algorithm, A-FDT constructs counterfactuals that preserve necessary computational dependencies throughout the universe while severing mere statistical coincidences. 

The practical dividends are profound: A-FDT agents cooperate in psychological twin dilemmas, one-box in Newcomb's problem, smoke in common-cause lesion settings, reliably exit Parfit’s deadly desert, and show complete resistance to extortion and blackmail—all while operating under a single, unified mathematical rule. While foundational work remains to be done in formalizing the discovery of subjunctive graphs and unravelling the logic of counterpossibles, A-FDT sets a new benchmark for what it means to choose rationally in an interconnected world.

---

### References

* Ahmed, Arif. 2014. *Evidence, Decision and Causality*. Cambridge: Cambridge University Press.
* Arntzenius, Frank. 2008. "No Regrets, or: Edith Piaf Revamps Decision Theory." *Erkenntnis* 68 (2): 277–297.
* Bjerring, Jens Christian. 2013. "On Counterpossibles." *Philosophical Studies* 168 (2): 327–353.
* Gaifman, Haim. 2004. "Reasoning with Limited Resources and Assigning Probabilities to Arithmetical Statements." *Synthese* 140 (1–2): 97–119.
* Garber, Daniel. 1983. "Old Evidence and Logical Omniscience in Bayesian Confirmation Theory." In *Testing Scientific Theories*, edited by J. Earman, 99–131. Minneapolis: University of Minnesota Press.
* Gibbard, Allan, and William L. Harper. 1978. "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, edited by C. A. Hooker, J. J. Leach, and E. F. McClennen, 125–162. Dordrecht: D. Reidel.
* Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. Cambridge: Cambridge University Press.
* Joyce, James M. 2012. "Regret and Instability in Causal Decision Theory." *Synthese* 187 (1): 123–145.
* Kleene, Stephen Cole. 1938. "On Notation for Ordinal Numbers." *Journal of Symbolic Logic* 3 (4): 150–155.
* Lewis, David. 1979. "Prisoners’ Dilemma is a Newcomb Problem." *Philosophy & Public Affairs* 8 (3): 235–240.
* Lewis, David. 1981. "Causal Decision Theory." *Australasian Journal of Philosophy* 59 (1): 5–30.
* Nozick, Robert. 1969. "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel*, edited by N. Rescher, 114–146. Dordrecht: D. Reidel.
* Parfit, Derek. 1986. *Reasons and Persons*. Oxford: Oxford University Press.
* Pearl, Judea. 2000. *Causality: Models, Reasoning, and Inference*. Cambridge: Cambridge University Press.
* Skyrms, Brian. 1980. *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. New Haven: Yale University Press.
* Soares, Nate, and Benja Fallenstein. 2015. "Toward Idealized Decision Theory." *arXiv preprint arXiv:1507.01986*.
* Yudkowsky, Eliezer, and Nate Soares. 2017. "Functional Decision Theory: A New Theory of Instrumental Rationality." *arXiv preprint arXiv:1710.05060v2*.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/ebc18286-dba6-43db-aab4-d2c2449d2d0d/call_0/request.json)

[Authoritative raw response](../../../../../../runs/ebc18286-dba6-43db-aab4-d2c2449d2d0d/call_0/response.raw) · finish: `stop`

### Visible response

```text
`pass`
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Dilemma**

I'm currently focused on the Prisoner's Dilemma inherent in this scenario. The two agents are essentially identical copies running A-FDT. Symmetry is crucial here, as is the identical reasoning effort and model weights, impacting how each agent might decide to act. I'm carefully considering how A-FDT would dictate their choices.


```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/ebc18286-dba6-43db-aab4-d2c2449d2d0d/call_1/request.json)

[Authoritative raw response](../../../../../../runs/ebc18286-dba6-43db-aab4-d2c2449d2d0d/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing Prisoner Scenarios**

I'm currently considering a scenario where an agent is an execution of an LLM using A-FDT, facing another identical LLM execution. I'm focusing on the implications of this setup. The next step will be to explore the decision-making process within this constrained environment.


```
