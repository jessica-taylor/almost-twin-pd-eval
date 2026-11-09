# Intervening on the Logical Type: The Formal Architecture and Philosophy of Action Functional Decision Theory (A-FDT)

## 1. Introduction: The Instrumental Impasse

Normative decision theory seeks a formal criterion for instrumental rationality: how should an agent choose among available options to best fulfill their preferences? For decades, the debate has been dominated by two paradigms: Evidential Decision Theory (EDT) and Causal Decision Theory (CDT). 

Both theories can be understood within the generalized expected utility framework axiomatized by Joyce (1999). An agent selects an action $a$ from a finite set $\mathcal{A}$ to maximize:
\begin{equation}
  \mathcal{EU}(a) \coloneqq \sum_{j} P(a \then o_j ;\, x) \, \mathcal{U}(o_j),
  \label{eq:general_eu}
\end{equation}
where $o_j \in \mathcal{O}$ represents the possible outcomes, $x \in \mathcal{X}$ is the agent's observation history, $\mathcal{U}$ is a bounded real-valued utility function, and $a \then o_j$ is a decision hypothetical encoding the probability that outcome $o_j$ will obtain if the agent takes action $a$. As Joyce demonstrates, foundational axioms of rational preference fix the formal structure of expected utility maximization, leaving the connective "$\then$"—the epistemic perspective from which hypothetical actions are evaluated—as a free parameter.

The dispute between EDT and CDT reduces to their choice of this connective:
1. **Evidential Decision Theory (EDT)** identifies $P(a \then o_j ;\, x)$ with standard Bayesian conditionalization:
   \begin{equation}
     \mathrm{EDT}(P, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(V \mid \mathrm{Obs}=x, \, \mathrm{Act}=a\right),
     \label{eq:edt}
   \end{equation}
   where $V \coloneqq \mathcal{U}(\mathrm{Outcome})$. EDT asks: *Which action would be the best news to learn that I took?*
2. **Causal Decision Theory (CDT)** formalizes counterfactual conditionals through Pearl's (1996, 2000) causal graphical models $(P, G)$. It applies an intervention operator $\mathrm{do}(\mathrm{Act}=a)$ that severs all incoming causal edges to the physical action $\mathrm{Act}$:
   \begin{equation}
     \mathrm{CDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(V \mid \mathrm{do}(\mathrm{Act}=a), \, \mathrm{Obs}=x\right).
     \label{eq:cdt}
   \end{equation}
   CDT asks: *Which physical act of mine causes the best outcome?*

Neither paradigm achieves consistent instrumental success across decision dilemmas. In Newcomb's Problem, a reliable predictor fills an opaque box with \$1,000,000 if and only if it predicted the agent would leave behind an open box containing \$1,000. EDT agents predictably take one box and walk away with \$1,000,000, while CDT agents—reasoning that their physical act cannot retrocausally alter the past contents of the box—two-box and walk away with only \$1,000. 

Conversely, in the Smoking Lesion Problem, a genetic arterial lesion causes both a desire to smoke and fatal lung cancer, without smoking causally contributing to cancer. Here, CDT correctly prescribes smoking (reaping the direct utility of tobacco without causing cancer), whereas standard EDT pathologically prescribes refraining to "manage the news" of one's own genetic health. In Parfit's Hitchhiker Problem, an agent stranded in the desert is rescued by an accurate lie-detecting driver only if the driver predicts the agent will subsequently withdraw \$1,000 to pay them upon reaching the city. Upon arriving in the city, both CDT and EDT agents refuse to pay—since the rescue is already past, paying causes or indicates no further benefit—causing them to be abandoned to die in the desert.

This essay examines **Action Functional Decision Theory (A-FDT)**, formulated by Yudkowsky and Soares (2017). A-FDT is the formalization of Functional Decision Theory where the agent's optimization problem operates over *actions* while evaluating counterfactuals as interventions on the *logical decision procedure itself*. A-FDT reconciles these dilemmas under a single, non-ad-hoc decision rule: it one-boxes in Newcomb's Problem, smokes in the Smoking Lesion Problem, pays the driver in Parfit's Hitchhiker, and systematically outperforms both CDT and EDT in strategic and multi-agent dilemmas.

---

## 2. Philosophical Motivation: Subjunctive Dependence and Token vs. Type Interventions

The core insight of A-FDT lies in a radical reinterpretation of what an agent's counterfactual intervention modifies. Standard causal decision theory treats the agent's decision as a localized physical event—a *token* action occurring in spacetime. A-FDT instead recognizes that an agent's choice is an instantiation of an abstract mathematical mapping from epistemic states to actions—a *logical type*.

### 2.1 The Analogy of Distributed Calculators
Consider two pocket calculators programmed with the exact same arithmetic algorithm, situated in Paris and Tokyo. If the calculator in Paris evaluates the expression $6288 + 1048$, it displays $7336$. If we observe the Paris calculator displaying $7336$, we immediately infer that the Tokyo calculator, given the same arithmetic input, will also output $7336$. 

Does the Paris calculator *cause* the Tokyo calculator to output $7336$? Physically and relativistically, no: there is no causal wire or timelike signal passing between them. Nor is this relation a mere statistical coincidence (like both calculators happening to be painted green). Rather, both physical devices instantiate the same abstract mathematical function:
$$\operatorname{Add}(6288, 1048) = 7336.$$
Their behaviors are bound by what Yudkowsky and Soares term **subjunctive dependence**. If, per impossible, the function $\operatorname{Add}(6288, 1048)$ had evaluated to $7337$, *both* physical devices would have displayed $7337$. 

A-FDT asserts that an agent standing before Newcomb's boxes, or facing a psychological twin in a Prisoner's Dilemma, is structurally identical to one of these calculators. An accurate predictor constructing a simulation or cognitive model of an agent is running an algorithm logically correlated with the agent's own decision procedure. The agent's physical choice in the present and the predictor's past prediction do not share a backwards-in-time causal link; rather, both physical tokens *subjunctively depend* on the output of the identical decision function.

### 2.2 Diagnosing the Failures of CDT and EDT
Through this lens, the structural pathologies of CDT and EDT become transparent:
* **CDT preserves too few dependencies.** When evaluating a counterfactual alternative, CDT holds the past fixed, severing the logical connection between the agent's choice and environmental models of that choice. In Newcomb's Problem, CDT asks what happens if its physical hand reaches for both boxes while the predictor's prediction remains held fixed. This counterfactual is logically impossible: it imagines the Paris calculator outputting 7337 while the Tokyo calculator continues to output 7336. CDT fails because it intervenes on the *physical token* rather than the *logical type*.
* **EDT preserves too many dependencies.** When EDT evaluates an action by simple conditioning, it treats *all* statistical correlations as decision-relevant evidence. In the Smoking Lesion Problem, the correlation between smoking and cancer is purely epistemic and non-manipulable; smoking does not logically or mathematically govern the lesion. EDT fails because it mistreats mere evidential relevance as actionable leverage, forcing the agent to act as if they are manipulating an unmanipulable background state.

A-FDT resolves this tension by stating:
$$\text{\textit{Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.}}$$

---

## 3. Mathematical Formalization of A-FDT

To formalize this perspective, A-FDT extends Pearl's graphical causal framework to encompass logical and computational dependencies.

### 3.1 World-Models with Quined Logical Variables
Let an agent maintain a world-model $M = (P, G)$, where $P$ is a probability distribution over a set of discrete random variables, and $G = (V_G, E_G)$ is a directed acyclic graph encoding structural dependencies among these variables. 

Unlike standard causal Bayesian networks where vertices denote exclusively spatio-temporal physical states, the vertex set $V_G$ of an A-FDT agent includes **logical variables** representing the outputs of deterministic mathematical and computational functions. Specifically, let $\mathtt{fdt}$ denote the agent's own decision procedure. The agent's network contains an explicit variable:
$$\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}),$$
which designates the output of the mathematical function $\text{A-FDT}$ evaluated on the specific inputs $(P, G, x)$.

Here, the underlined terms $\underline{P}$, $\underline{G}$, and $\underline{x}$ represent syntactic encodings (Gödel numbers or quotes) of the inputs. The apparent paradox of an algorithm manipulating a model that contains an explicit representation of the algorithm itself is formally resolved via Kleene's Second Recursion Theorem (Kleene 1938). By constructing self-referential programs via *quining*, an algorithm can inspect its own code and evaluate hypothetical statements about its own mathematical behavior without falling into non-terminating circularity. The agent does not need to know the *evaluated value* of $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ in advance; it merely possesses a node within $G$ *representing* that logical output.

### 3.2 The Primary Formal Definition of A-FDT
In Causal Decision Theory (Equation \ref{eq:cdt}), the agent conditions on their observation history $\mathrm{Obs}=x$ and applies Pearl's $\mathrm{do}$-operator directly to the physical action node: $\mathrm{do}(\mathrm{Act}=a)$.

In Action Functional Decision Theory, the agent formalizes the counterfactual not as an intervention on the physical movement of their muscles, but as an intervention on the output of their decision function itself. Formally, A-FDT evaluates the action according to **Equation (4)** of Yudkowsky and Soares (2017):

\begin{equation}
  \text{A-FDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(V \;\middle|\; \mathrm{do}\left(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right).
  \label{eq:afdt}
\end{equation}

### 3.3 Two Structural Differences Between A-FDT and CDT
Comparing Equation (\ref{eq:cdt}) and Equation (\ref{eq:afdt}) reveals two foundational mathematical departures:

1. **The Target of Intervention (Type vs. Token):**
   CDT performs surgery on $\mathrm{Act}$. In the causal graph, setting $\mathrm{do}(\mathrm{Act}=a)$ severs the edge $\mathrm{Predisposition} \to \mathrm{Act}$, leaving any past prediction node intact. In contrast, A-FDT performs surgery on the logical node $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$. Because environmental predictors and psychological twins base their forecasts directly on simulations of this very function, the directed edges in $G$ flow outward from $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ to *both* the agent's physical action $\mathrm{Act}$ *and* the environmental nodes (e.g., $\mathrm{Prediction}$). Pearl's graph surgery propagation rule ensures that intervening on $\mathtt{fdt}$ simultaneously propagates downstream along all subjunctive paths.

2. **The Processing of Observations (Updatelessness vs. Bayesian Conditioning):**
   When a CDT or EDT agent receives an observation $x$, they condition their entire probability distribution on the event $\mathrm{Obs}=x$, computing $\mathbb{E}(V \mid \dots, \mathrm{Obs}=x)$. 
   
   A-FDT responds to evidence in a fundamentally different way: **it changes the node of intervention rather than conditioning the background state**. When observation changes from $x$ to $y$, an A-FDT agent does not collapse their probability space around $\mathrm{Obs}=y$; they transition from intervening on $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ to intervening on $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{y})$. As shown below, this allows the agent to entertain counterfactuals in which alternative actions would have caused them to *receive entirely different observations*, preserving optimal commitments without ad-hoc dynamic patching.

---

## 4. Applying A-FDT Across Classic Decision Dilemmas

We now demonstrate the operational mechanics of Equation (\ref{eq:afdt}) by walking through four canonical decision problems.

### 4.1 Newcomb's Problem

Let Box A contain \$1,000 and Box B contain either \$1,000,000 or \$0. The predictor fills Box B if and only if it predicted the agent one-boxes. Let the predictor's reliability be $0.99$.

* **The A-FDT Graph $\boldsymbol{G^F}$:**
  The graph contains nodes:
  * The logical decision node: $F \coloneqq \mathtt{fdt}(\underline{P^F}, \underline{G^F})$.
  * The physical action: $\mathrm{Act} \in \{\text{onebox}, \text{twobox}\}$, with deterministic functional relationship $\mathrm{Act} = F$.
  * The prediction: $\mathrm{Prediction} \in \{1, 2\}$, where $\mathrm{Prediction} = F$ with probability $0.99$.
  * Box B contents: $\mathrm{BoxB} \in \{\text{full}, \text{empty}\}$, where $\mathrm{BoxB} = \text{full}$ if $\mathrm{Prediction}=1$.
  * Utility $V \coloneqq \mathcal{U}(\mathrm{Act}, \mathrm{BoxB})$, where $V(\text{onebox}, \text{full}) = 10^6$, $V(\text{twobox}, \text{full}) = 1.001 \times 10^6$, $V(\text{twobox}, \text{empty}) = 10^3$, and $V(\text{onebox}, \text{empty}) = 0$.

```
      [ fdt(P, G) ] (Intervention Node)
        /        \
       v          v
    [ Act ]    [ Prediction ]
       \          /
        v        v
      [ Outcome / V ]
```

* **Execution of A-FDT:**
  The agent calculates the expected utility for each candidate value $a \in \{\text{onebox}, \text{twobox}\}$ under $\mathrm{do}(F = a)$:
  
  1. For $a = \text{onebox}$:
     $$\mathrm{do}(F = \text{onebox}) \implies P(\mathrm{Act} = \text{onebox}) = 1, \quad P(\mathrm{Prediction} = 1) = 0.99.$$
     $$\mathbb{E}\left(V \mid \mathrm{do}(F = \text{onebox})\right) = 0.99 \times \$1{,}000{,}000 + 0.01 \times \$0 = \$990{,}000.$$

  2. For $a = \text{twobox}$:
     $$\mathrm{do}(F = \text{twobox}) \implies P(\mathrm{Act} = \text{twobox}) = 1, \quad P(\mathrm{Prediction} = 2) = 0.99.$$
     $$\mathbb{E}\left(V \mid \mathrm{do}(F = \text{twobox})\right) = 0.01 \times \$1{,}001{,}000 + 0.99 \times \$1{,}000 = \$10{,}010 + \$990 = \$11{,}000.$$

Since $\$990{,}000 > \$11{,}000$, Equation (\ref{eq:afdt}) evaluates to:
$$\text{A-FDT}(P^F, G^F) = \text{onebox}.$$
A-FDT leaves Box A behind and reliably attains \$1,000,000.

### 4.2 The Smoking Lesion Problem

In the Smoking Lesion Problem, a genetic lesion determines whether an agent suffers from lung cancer ($P(\text{cancer} \mid \text{lesion}) = 0.99$, $P(\text{cancer} \mid \neg\text{lesion}) = 0.01$) and simultaneously gives the agent an innate preference for smoking. Smoking yields an extra \$1,000 in direct utility, while living without cancer is worth \$1,000,000.

* **The A-FDT Graph $\boldsymbol{G^F}$:**
  Unlike Newcomb's predictor, a genetic lesion does not model or compute the agent's decision function. The causal/subjunctive graph reflects this asymmetry. The presence of the lesion dictates which utility function the agent possesses: $\mathcal{U}_S$ (valuing smoking) or $\mathcal{U}_R$ (disliking smoking). 
  
  Consequently, there are two distinct mathematical functions the agent could be running: $\mathtt{fdt}(\underline{P_S^F}, \underline{G^F})$ or $\mathtt{fdt}(\underline{P_R^F}, \underline{G^F})$. Let the agent have preferences $\mathcal{U}_S$. In $G^F$, the variable $\mathrm{Lesion}$ has an outgoing edge to $\mathrm{Cancer}$ and an edge to $\mathrm{Act}$ (by selecting which utility module drives behavior). However, **there is no edge from $\mathtt{fdt}(\underline{P_S^F}, \underline{G^F})$ to $\mathrm{Lesion}$ or $\mathrm{Cancer}$**.

```
    [ Lesion ] -----------> [ Cancer / Death ]
     /      \                      |
    v        v                     v
 [ Act ] <-- [ fdt(P_S, G) ] ---> [ V ]
```

* **Execution of A-FDT:**
  Under the intervention $\mathrm{do}\left(\mathtt{fdt}(\underline{P_S^F}, \underline{G^F}) = a\right)$, the distribution of $\mathrm{Lesion}$ remains entirely invariant:
  $$P\left(\mathrm{Lesion} \;\middle|\; \mathrm{do}\left(\mathtt{fdt} = \text{smoke}\right)\right) = P\left(\mathrm{Lesion} \;\middle|\; \mathrm{do}\left(\mathtt{fdt} = \text{refrain}\right)\right) = P(\mathrm{Lesion}) = p.$$
  
  Evaluating expected utilities for an agent with preferences $\mathcal{U}_S$:
  $$\mathbb{E}\left(V \mid \mathrm{do}(\mathtt{fdt} = \text{smoke})\right) = p(\$10{,}000 + \$1{,}000) + (1-p)(\$990{,}000 + q \cdot \$1{,}000),$$
  $$\mathbb{E}\left(V \mid \mathrm{do}(\mathtt{fdt} = \text{refrain})\right) = p(\$10{,}000) + (1-p)(\$990{,}000 + q \cdot \$1{,}000),$$
  where $q$ is the probability that $\mathtt{fdt}_R$ smokes.

  Subtracting the two evaluations reveals:
  $$\mathbb{E}\left(V \mid \mathrm{do}(\mathtt{fdt}=\text{smoke})\right) - \mathbb{E}\left(V \mid \mathrm{do}(\mathtt{fdt}=\text{refrain})\right) = p \cdot \$1{,}000 > 0.$$
  $$\text{A-FDT}(P_S^F, G^F) = \text{smoke}.$$
A-FDT correctly smokes, avoiding the news-managing pathology of EDT while preserving the ability to one-box in Newcomb's Problem.

### 4.3 The Transparent Newcomb Problem

In Drescher's (2006) Transparent Newcomb Problem, Box A contains \$1,000 and Box B contains \$1,000,000 or \$0, but both boxes are completely transparent. The agent directly observes whether Box B is full *before* deciding whether to take one or both boxes. The predictor filled Box B if and only if it predicted that the agent, *upon directly observing both boxes full*, would take only Box B.

Suppose an agent observes that Box B is full ($x = \text{full}$).
* **CDT Evaluation:** 
  $$\mathbb{E}\left(V \mid \mathrm{do}(\mathrm{Act}=\text{twobox}), \, \mathrm{Obs}=\text{full}\right) = \$1{,}001{,}000 > \$1{,}000{,}000 = \mathbb{E}\left(V \mid \mathrm{do}(\mathrm{Act}=\text{onebox}), \, \mathrm{Obs}=\text{full}\right).$$
  CDT two-boxes, and knowing this, the predictor leaves Box B empty.
* **EDT Evaluation:**
  Conditional on seeing Box B full, the good news has already arrived. EDT calculates:
  $$\mathbb{E}\left(V \mid \mathrm{Act}=\text{twobox}, \, \mathrm{Obs}=\text{full}\right) = \$1{,}001{,}000 > \$1{,}000{,}000 = \mathbb{E}\left(V \mid \mathrm{Act}=\text{onebox}, \, \mathrm{Obs}=\text{full}\right).$$
  EDT two-boxes as well.

* **A-FDT Evaluation:**
  The A-FDT agent does not condition on $\mathrm{Obs}=\text{full}$. Instead, observing $x=\text{full}$ designates the intervention node:
  $$\mathtt{fdt}(\underline{P^F}, \underline{G^F}, \text{full}).$$
  In graph $G^F$, the predictor's past prediction depends on the output of this exact conditional node. If $\mathtt{fdt}(\dots, \text{full}) = \text{twobox}$, the predictor would have anticipated that the agent, upon facing two full boxes, would take both, and thus would have left the box empty in the first place!

```
    [ fdt(P, G, full) ] (Intervened)    [ fdt(P, G, empty) ]
            |      \                          /
            |       v                        v
            |     [ Prediction ] ---------> [ Act ]
            |           |                     ^
            v           v                     |
          [ Box B ] ---> [ Obs ] --------------
```

  Evaluating Equation (\ref{eq:afdt}) with $99\%$ predictor accuracy:
  1. For $a = \text{onebox}$:
     Intervening to set $\mathtt{fdt}(\dots, \text{full}) = \text{onebox}$ implies the predictor predicted one-boxing with $0.99$ probability. Thus Box B is full, the agent observes $\mathrm{full}$, and the node $\mathtt{fdt}(\dots, \text{full})$ controls $\mathrm{Act}$.
     $$\mathbb{E}\left(V \mid \mathrm{do}(\mathtt{fdt}(\dots, \text{full})=\text{onebox})\right) \approx 0.99 \times \$1{,}000{,}000 + 0.01 \times (q \cdot \$1{,}000) \approx \$990{,}000.$$
  2. For $a = \text{twobox}$:
     Intervening to set $\mathtt{fdt}(\dots, \text{full}) = \text{twobox}$ implies the predictor predicted two-boxing with $0.99$ probability. Box B is therefore empty with probability $0.99$. The agent would receive observation $\mathrm{empty}$, and their action would be governed by the alternate node $\mathtt{fdt}(\dots, \text{empty})$ (which takes the remaining \$1,000).
     $$\mathbb{E}\left(V \mid \mathrm{do}(\mathtt{fdt}(\dots, \text{full})=\text{twobox})\right) \approx 0.01 \times \$1{,}001{,}000 + 0.99 \times \$1{,}000 \approx \$11{,}000.$$

Consequently:
$$\text{A-FDT}(P^F, G^F, \text{full}) = \text{onebox}.$$
Even with \$1,000,000 visibly gleaming inside Box B, the A-FDT agent leaves the \$1,000 behind. By executing this logic, A-FDT agents are predicted to one-box, finding Box B filled $99\%$ of the time, while CDT and EDT agents repeatedly find an empty box.

### 4.4 The Psychological Twin Prisoner's Dilemma
Two identical agents, Alice and Bob, are placed in separate interrogation rooms with no means of communication. Each must choose to Cooperate ($C$) or Defect ($D$). The payoffs are:
* Both Cooperate: $(\$1{,}000{,}000, \, \$1{,}000{,}000)$
* Both Defect: $(\$1{,}000, \, \$1{,}000)$
* One Defects, One Cooperates: $(\$1{,}001{,}000, \, \$0)$

Both agents know they run identical cognitive architectures: $\mathtt{fdt}_A \equiv \mathtt{fdt}_B \equiv \mathtt{fdt}$.

* **CDT Analysis:** CDT defects. Alice's hand cannot causally send a physical signal to Bob's body. Defection strictly dominates cooperation by \$1,000 regardless of Bob's choice. Both defect and receive \$1,000.
* **A-FDT Analysis:** Alice's graph models both $\mathrm{Act}_A$ and $\mathrm{Act}_B$ as child nodes of the single mathematical function node $\mathtt{fdt}$.
  * Under $\mathrm{do}(\mathtt{fdt} = C)$, $\mathrm{Act}_A = C$ and $\mathrm{Act}_B = C$, yielding $\$1{,}000{,}000$.
  * Under $\mathrm{do}(\mathtt{fdt} = D)$, $\mathrm{Act}_A = D$ and $\mathrm{Act}_B = D$, yielding $\$1{,}000$.

Equation (\ref{eq:afdt}) directly selects:
$$\text{A-FDT}(P^F, G^F) = C.$$
A-FDT achieves mutual cooperation without requiring metaphysical backwards causation or psychological telepathy.

---

## 5. Comparative Evaluation

The systematic differences among EDT, CDT, and A-FDT across canonical decision problems are summarized in the table below:

| Decision Problem | EDT Prescription | CDT Prescription | A-FDT Prescription | Optimal Payout Behavior |
| :--- | :--- | :--- | :--- | :--- |
| **Newcomb's Problem** | One-box (\$1M) | Two-box (\$1k) | One-box (\$1M) | One-box |
| **Smoking Lesion** | Refrain (Loss) | Smoke (Optimal) | Smoke (Optimal) | Smoke |
| **Parfit's Hitchhiker** | Refuse to pay (Dies) | Refuse to pay (Dies) | Pay (\$999k net) | Pay |
| **Transparent Newcomb** | Two-box (\$1k) | Two-box (\$1k) | One-box (\$1M) | One-box |
| **Twin Prisoner's Dilemma** | Cooperate (\$1M) | Defect (\$1k) | Cooperate (\$1M) | Cooperate |
| **XOR Blackmail** | Pays blackmail | Refuses (Optimal) | Refuses (Optimal) | Refuses |
| **Death in Damascus** | Flees (Costly) | Instability / Dices | Stays (Saves \$1k) | Stays |

### The Death in Damascus Dilemma and Reflective Instability
In Death in Damascus, Death tells Carl (a CDT agent) he is scheduled to die tomorrow. Death can predict where Carl will be with $100\%$ accuracy. If Carl stays in Damascus, he dies tomorrow; if he flees to Aleppo at a cost of \$1,000, he also dies tomorrow.

CDT encounters fatal dynamic instability here:
* If Carl expects to stay in Damascus, his counterfactual $\mathrm{do}(\mathrm{Act}=\text{Aleppo})$ shows him escaping Death (since Death's appointment book is held fixed in the past). Thus he flees to Aleppo.
* Once he sets out for Aleppo, he updates his expectations, which immediately renders staying in Damascus look superior. 

Carl enters an infinite deliberation loop, requiring complex mixed-strategy "ratification" procedures (Joyce 2012) that ultimately lead him to pay \$1,000 to die on camelback in Aleppo with $\approx 50\%$ probability.

Fiona, an A-FDT agent, evaluates the intervention on her decision procedure $\mathrm{do}(\mathtt{fdt} = a)$. She recognizes that Death's appointment book subjunctively tracks $\mathtt{fdt}$. Under $\mathrm{do}(\mathtt{fdt}=\text{Damascus})$, Death meets her in Damascus. Under $\mathrm{do}(\mathtt{fdt}=\text{Aleppo})$, Death meets her in Aleppo. The survival prize of \$1,000,000 is unreachable under both interventions, but staying saves the \$1,000 travel fee:
$$\mathbb{E}\left(V \mid \mathrm{do}(\mathtt{fdt}=\text{Damascus})\right) = \$0 > -\$1{,}000 = \mathbb{E}\left(V \mid \mathrm{do}(\mathtt{fdt}=\text{Aleppo})\right).$$
Fiona calmly stays in Damascus. A-FDT experiences none of CDT's deliberation instability.

---

## 6. Open Problems, Formal Limitations, and Concrete Proposals

While A-FDT exhibits remarkable instrumental performance, its formal architecture leaves several theoretical questions open. In this section, we clearly distinguish between claims made in the source text and additional formal proposals required to make A-FDT fully operational.

### 6.1 The Epistemology of Subjunctive Dependency Graphs (The Inference Problem)
In Pearl's causal discovery theory, causal directed acyclic graphs can be learned from observational data and localized physical experiments via the Causal Markov Condition and Faithfulness assumptions (Pearl 2000).

* **Source Gap:** Yudkowsky and Soares explicitly identify that **no analogous formal discovery calculus exists for learning subjunctive dependencies**. While they take the graph $G^F$ containing logical nodes as an exogenous input parameter to Equation (\ref{eq:afdt}), they leave open the exact mechanism by which an agent constructs $G^F$ from empirical data.
* **Our Proposal (Algorithmic Mutual Information and Program Slicing):**
  How can an agent empirically or computationally determine whether an environmental variable $Y$ subjunctively depends on a decision function $\mathtt{fdt}$? We propose that an agent can operationalize subjunctive dependence via **algorithmic program analysis**:
  
  Let the predictor be an physical process whose state transition function can be modeled as a Turing machine $\mathcal{M}_P$. The agent constructs an edge $\mathtt{fdt} \to Y$ in $G^F$ if and only if:
  1. A formal representation (source code or bytecode) of the algorithm $\mathtt{fdt}$ appears as an active computational subroutine within the execution trace of $\mathcal{M}_P$ that generates $Y$; and
  2. The algorithmic mutual information $I_K(\mathtt{fdt} ; Y)$ is non-trivial under program slicing—meaning that replacing the return register of the $\mathtt{fdt}$ subroutine within $\mathcal{M}_P$ with an alternative value $a'$ alters the computed state of $Y$.
  
  This proposal grounds subjunctive dependence in concrete computer science: environmental nodes depend on $\mathtt{fdt}$ precisely when the environment executes a simulation containing the agent's decision code.

### 6.2 Counterpossible Conditioning and the $\mathtt{true}$ Operator
Equation (\ref{eq:afdt}) uses Pearl's physical $\mathrm{do}$-operator over a logical variable: $\mathrm{do}(\mathtt{fdt}=a)$. However, as Yudkowsky and Soares note, this is an engineering placeholder.

* **Source Gap:** In classical logic, a mathematical function $\mathtt{fdt}$ given inputs $(P, G, x)$ deterministically evaluates to a unique output $a^*$. If $a \neq a^*$, the sentence $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a$ is a **logical contradiction**. Evaluating probabilities conditional on mathematical falsehoods is the problem of **counterpossible reasoning** (Cohen 1990). Under standard probability axioms, conditioning on a logical falsehood causes catastrophic deductive explosion: $P(X \mid \bot)$ is undefined or trivial. The source article acknowledges that an ideal theory would use an axiomatic $\mathtt{true}(\phi)$ operator rather than Pearl's causal $\mathrm{do}$, but brackets its formal construction.
* **Our Proposal (Logical Induction Integration):**
  A natural mathematical foundation for the A-FDT hypothetical operator is Garrabrant et al.'s (2016) framework of **Logical Induction**. A logical inductor assigns coherent, non-extreme probabilities $P_n$ to mathematical sentences over time while outperforming any polynomial-time deductive predictor. Within a logical inductor:
  1. Counterpossible conditionals can be assigned rigorous, non-trivial subjective probabilities by evaluating limits of finite deductive systems where mathematical statements are treated as structurally unproven sentences until an explicit proof is derived.
  2. Counterfactual evaluation under A-FDT can be formalized as an intervention on a proof system: assigning a temporary truth-value assignment to the output register of the quined algorithm $\mathtt{fdt}$ and extracting the logical inductor's conditioned distribution over subsequent execution sentences.

### 6.3 A-FDT (Actions) vs. Policy-FDT (P-FDT)
Footnotes 7 and 16 in the source text mention that the authors' preferred long-term formulation of FDT evaluates **policies** (mappings $\pi: \mathcal{X} \to \mathcal{A}$) rather than raw actions:
$$\pi^* = \operatorname*{argmax}_{\pi \in \Pi} \mathbb{E}\left(V \;\middle|\; \mathrm{do}(\mathtt{fdt} = \pi)\right).$$

* **Why Action-FDT (A-FDT) Suffices:**
  In Section 5, Equation (4), the paper establishes **A-FDT** as the primary formalization. A-FDT evaluates actions directly at decision time by intervening on $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a$. 
  
  As proven by our analysis of the Transparent Newcomb Problem, A-FDT fully achieves the benefits of policy-level reasoning without requiring an explicit ex-ante optimization stage. Because A-FDT switches the *point of intervention* upon receiving observation $x$, it evaluates how changes to *this specific conditional response* propagate through the predictor's past simulation. A-FDT achieves dynamic consistency and respects the true value of information without requiring binding precommitments or external enforcement mechanisms.

---

## 7. Conclusion: Instrumental Rationality Naturalized

Action Functional Decision Theory (A-FDT) represents a fundamental paradigm shift in formal epistemology and rational choice. By shifting the target of decision-theoretic counterfactual intervention from the spatio-temporal **token action** to the abstract **logical decision type**, A-FDT reconciles the historical schism between Causal and Evidential Decision Theories.

Under the unified mathematical rule of Equation (\ref{eq:afdt}):
$$\text{A-FDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(V \;\middle|\; \mathrm{do}\left(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right),$$
the agent achieves maximal expected utility across every major class of decision dilemma. It one-boxes in Newcomb's Problem, smokes in the Smoking Lesion Problem, pays its debts in Parfit's desert, cooperates in Twin Prisoner's Dilemmas, and remains impervious to extortion in Blackmail scenarios. 

A-FDT demystifies these achievements: it does not violate relativistic physics with backward causation, nor does it indulge in magical news-management. Instead, it embeds the decision-maker firmly within the universe as a physical machine running a mathematical computation—a computation that other intelligent agents in the environment can simulate, anticipate, and respond to. In an era increasingly populated by algorithmic agents, multi-agent artificial systems, and game-theoretic interactions mediated by code, A-FDT provides an indispensable, mathematically robust foundation for the theory of instrumental rationality.

---

## References

* Adams, Ernest W. 1970. "Subjunctive and Indicative Conditionals." *Foundations of Language* 6 (1): 89–94.
* Ahmed, Arif. 2014. *Evidence, Decision and Causality*. Cambridge University Press.
* Arntzenius, Frank. 2008. "No Regrets, or: Edith Piaf Revamps Decision Theory." *Erkenntnis* 68 (2): 277–297.
* Cohen, Daniel. 1990. "On What Cannot Be." In *Truth or Consequences: Essays in Honor of Nuel Belnap*, edited by J. Michael Dunn and Anil Gupta, 123–132. Kluwer Academic Publishers.
* Drescher, Gary L. 2006. *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Eells, Ellery. 1984. "Metatickles and the Dynamics of Deliberation." *Theory and Decision* 17 (1): 71–95.
* Garrabrant, Scott, Tsvi Benson-Tilsen, Nate Soares, and Jessica Taylor. 2016. "Logical Induction." *arXiv preprint arXiv:1609.03543*.
* Gibbard, Allan, and William L. Harper. 1978. "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, edited by C. A. Hooker, J. J. Leach, and E. F. McClennen, 13:125–162. Reidel.
* Jeffrey, Richard C. 1983. *The Logic of Decision*. 2nd ed. University of Chicago Press.
* Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Joyce, James M. 2012. "Regret and Instability in Causal Decision Theory." *Synthese* 187 (1): 123–145.
* Kleene, Stephen Cole. 1938. "On Notation for Ordinal Numbers." *Journal of Symbolic Logic* 3 (4): 150–155.
* Lewis, David. 1979. "Prisoners' Dilemma is a Newcomb Problem." *Philosophy & Public Affairs* 8 (3): 235–240.
* Lewis, David. 1981. "Causal Decision Theory." *Australasian Journal of Philosophy* 59 (1): 5–30.
* Nozick, Robert. 1969. "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel*, edited by Nicholas Rescher, 114–146. Reidel.
* Parfit, Derek. 1986. *Reasons and Persons*. Oxford University Press.
* Pearl, Judea. 1996. "Causation, Action, and Counterfactuals." In *Proceedings of the 6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK '96)*, 51–73.
* Pearl, Judea. 2000. *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Skyrms, Brian. 1980. *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Soares, Nate, and Benja Fallenstein. 2015. "Toward Idealized Decision Theory." *arXiv preprint arXiv:1507.01986*.
* Spohn, Wolfgang. 1977. "Where Luce and Krantz Do Really Generalize Savage's Decision Model." *Erkenntnis* 11 (1): 113–134.
* Yudkowsky, Eliezer, and Nate Soares. 2017. "Functional Decision Theory: A New Theory of Instrumental Rationality." *arXiv preprint arXiv:1710.05060v2*.