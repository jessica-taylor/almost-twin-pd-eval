# 020_fdt_eq4_google_gemini-3.8-flash_rlow_plow / 00019

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/2f87b749-fe7c-441e-bcca-3402f041d3ce/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/2f87b749-fe7c-441e-bcca-3402f041d3ce/call_0/response.raw) · finish: `stop`

### Visible response

````text
# Intervening on Logic: A Mathematical Exposition of Action Functional Decision Theory (A-FDT)

## 1. Introduction: The Dialectic of Rational Choice

Standard normative decision theory has long been divided into two major frameworks: **Evidential Decision Theory (EDT)** and **Causal Decision Theory (CDT)**. Both frame instrumental rationality as expected utility maximization, conforming to the broad representation theorem of Joyce (1999). Where they diverge is in how they interpret the decision hypothetical—the connective "$\hookrightarrow$" in the formula:
\begin{equation}
\mathcal{EU}(a) \coloneqq \sum_{j} P(a \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j),
\label{eq:umax}
\end{equation}
which evaluates an action $a \in \mathcal{A}$ in light of an observation history $x \in \mathcal{X}$.

EDT interprets $a \hookrightarrow o$ via Bayesian conditionalization: an agent assesses $P(o \mid x, a)$. In doing so, EDT agents often manage the news rather than the world: in Skyrms’ (1980) Smoking Lesion problem, an EDT agent foregoes the utility of smoking because smoking is correlated with an incurable arterial lesion that causes lung cancer, even though smoking exerts zero causal influence on whether the lesion or cancer is present.

CDT resolves this by interpreting $a \hookrightarrow o$ via physical intervention. Formalized through Judea Pearl’s causal graphs (Pearl 1996, 2000), CDT replaces conditionalization with the causal intervention $\operatorname{do}(\mathrm{Act} = a)$. It severs incoming causal arrows to the physical action $\mathrm{Act}$ while holding all causally non-downstream variables fixed:
\begin{equation}
\mathrm{CDT}(P, G, x) \coloneqq \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\mathcal{V} \;\middle|\; \operatorname{do}(\mathrm{Act} = a),\, \mathrm{Obs} = x\right),
\label{eq:cdt}
\end{equation}
where $\mathcal{V} \coloneqq \mathcal{U}(\mathrm{Outcome})$.

CDT handles the Smoking Lesion problem correctly: smoking does not cause the lesion, so under $\operatorname{do}(\mathrm{Act} = \mathrm{smoke})$, the probability of cancer remains unchanged. However, CDT fails in Newcomb-like dilemmas (Nozick 1969). If an accurate predictor inspects an agent's reasoning beforehand and places \$1,000,000 in an opaque box if and only if she predicts the agent will leave a transparent box containing \$1,000 behind, CDT prescribes two-boxing. Because the contents of the boxes are causally upstream from the physical choice, CDT holds the contents fixed across its hypotheticals. CDT agents predictably forfeit the million dollars.

To surpass both CDT and EDT without ad-hoc patchworks or unstable ratification procedures (Jeffrey 1983, Joyce 2012), Yudkowsky and Soares (2017) introduce **Functional Decision Theory (FDT)**. While the authors note that their preferred underlying formulation evaluates full decision policies, their primary formalization in Equation (4), Section 5—which we term **Action Functional Decision Theory (A-FDT)**—evaluates actions directly by shifting the locus of counterfactual intervention from a physical act token to a mathematical function type.

This essay provides a rigorous mathematical exposition of A-FDT. We will establish its formal apparatus, trace how it constructs counterfactuals via *subjunctive dependence*, work through concrete dilemmas, and examine its open theoretical challenges.

---

## 2. Formal Specification of A-FDT

### 2.1 The Core Equation

In A-FDT, an agent maintains a world-model $M = (P, G)$, where $P$ is a joint probability distribution over a set of random variables, and $G$ is an extended structural dependency graph (a DAG) representing both physical causal mechanisms and non-causal dependencies.

The formal decision rule for A-FDT (Equation 4 of Yudkowsky & Soares 2017) is defined as:
\begin{equation}
\text{A-FDT}(P, G, x) \coloneqq \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\mathcal{V} \;\middle|\; \operatorname{do}\left(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right).
\label{eq:afdt}
\end{equation}
Here, the underlines denote syntactic dequoting or structural representations of the algorithm's own inputs (relying on quining mechanisms and Kleene’s recursion theorem; Kleene 1938). The node $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ is not a variable representing the physical motor movement $\mathrm{Act}$. Rather, it is a formal random variable embedded in $G$ that represents the **mathematical output of the A-FDT decision algorithm** evaluated on the inputs $(P, G, x)$.

### 2.2 Two Crucial Divergences from CDT

Equation \eqref{eq:afdt} reveals two structural distinctions from CDT’s Equation \eqref{eq:cdt}:

1. **Type Intervention vs. Token Intervention:** CDT applies $\operatorname{do}(\mathrm{Act} = a)$, intervening on the physical token of the agent’s behavior. A-FDT applies $\operatorname{do}(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)$, intervening on the logical type. Counterfactual variations in the value of $\mathtt{fdt}(\cdot)$ propagate downstream along all directed paths in $G$. Crucially, any physical system in the environment running a simulation or prediction of the agent’s algorithm is treated as causally or subjunctively downstream of that logical variable.
2. **Observation Routing vs. Bayesian Conditioning:** When CDT receives an observation $x$, it conditions on the event $\mathrm{Obs} = x$ alongside its $\operatorname{do}$-intervention: $\mathbb{E}(\mathcal{V} \mid \operatorname{do}(\mathrm{Act}=a), \mathrm{Obs}=x)$. A-FDT does not condition on $\mathrm{Obs}=x$ inside the expectation. Instead, the observation $x$ acts as an index that dictates **which node in the structural graph is subjected to surgery**. Evaluating alternative choices means evaluating hypothetical scenarios where the agent’s algorithm, when supplied with observation $x$, yielded a different output. 

As we will see in the Transparent Newcomb and Mechanical Blackmail dilemmas, this feature gives A-FDT an updateless character (Dai 2009): an A-FDT agent does not collapse her counterfactual space onto the historical branch $\mathrm{Obs} = x$ if the generation of that observation was itself influenced by what $\mathtt{fdt}(\dots, x)$ would compute.

---

## 3. Subjunctive Dependence and Graph Construction

The central conceptual engine of A-FDT is **subjunctive dependence**. Yudkowsky and Soares declare: *A-FDT is to subjunctive dependence as CDT is to causal dependence.*

Two physical processes exhibit subjunctive dependence when their behaviors are constrained by an underlying mathematical or logical identity. Consider two isolated, error-free calculators programmed to compute $6288 + 1048$. One is in Paris, the other in Tokyo. They share no real-time communication channel. If the Parisian calculator outputs $7336$, an observer infers with certainty that the Tokyo calculator outputs $7336$. 

More crucially, the counterfactual holds: *If the algorithm that computes $6288 + 1048$ had evaluated to $3159$, both calculators would have displayed $3159$.*

```
          [ Logical Fact: f(input) ]
                 /          \
                v            v
     [ Physical Token 1 ]   [ Physical Token 2 ]
     (Agent's Physical Act) (Predictor / Twin)
```

In standard causal DAGs (Pearl 2000), arrows strictly encode physical mechanisms across time. In A-FDT, the DAG $G$ is augmented:
- Nodes can represent logical, computational, or mathematical facts (e.g., $\mathtt{fdt}(P, G, x)$).
- Directed edges run from these logical facts to the physical physical instantiations that simulate, predict, or execute them.

Causal dependence is subsumed as a special case of subjunctive dependence (e.g., a scribe reading the Parisian display and transcribing it onto paper is both causally and subjunctively dependent on the calculation). Conversely, purely statistical correlations (such as two calculators both happening to have pink casings) lack an underlying functional identity; intervening on the casing of one leaves the other untouched.

---

## 4. Applying A-FDT to Classic Decision Problems

We now test A-FDT across four canonical decision problems, tracking how Equation \eqref{eq:afdt} evaluates actions.

### 4.1 Newcomb's Problem

An agent faces Box A containing \$1,000 and Box B containing \$1,000,000 or \$0. An accurate predictor (99% reliability) placed \$1,000,000 in Box B iff she predicted the agent would take only Box B. The prediction is already finalized.

* **Variables & Graph:** Let $\mathtt{fdt} = \mathtt{fdt}(\underline{P}, \underline{G}) \in \{\text{onebox}, \text{twobox}\}$. In $G$, directed edges run:
  $$\mathtt{fdt} \longrightarrow \mathrm{Act}, \quad \mathtt{fdt} \longrightarrow \mathrm{Prediction}$$
  From $\mathrm{Prediction}$, an edge runs to $\mathrm{BoxB} \in \{\text{full}, \text{empty}\}$. A noise node $\mathrm{Accurate} \in \{1, 0\}$ ($P=0.99, 0.01$) modulates whether $\mathrm{Prediction} = \mathtt{fdt}$. Finally, $\mathrm{Act}$ and $\mathrm{BoxB}$ feed into $\mathcal{V}$.
* **Evaluation under A-FDT:**
  The agent calculates $\mathbb{E}(\mathcal{V} \mid \operatorname{do}(\mathtt{fdt} = a))$:
  
  $$\begin{aligned}
  \mathbb{E}(\mathcal{V} \mid \operatorname{do}(\mathtt{fdt} = \text{onebox})) &= 0.99 \cdot \mathcal{U}(\$1,000,000) + 0.01 \cdot \mathcal{U}(\$0) \\
  &= \$990,000. \\
  \mathbb{E}(\mathcal{V} \mid \operatorname{do}(\mathtt{fdt} = \text{twobox})) &= 0.01 \cdot \mathcal{U}(\$1,001,000) + 0.99 \cdot \mathcal{U}(\$1,000) \\
  &= \$10,010 + \$990 = \$11,000.
  \end{aligned}$$

  A-FDT outputs $\operatorname{argmax} = \text{onebox}$.
* **Comparison:** CDT intervenes on $\mathrm{Act}$. Because $\mathrm{Prediction} \to \mathrm{BoxB}$ is causally upstream of $\mathrm{Act}$, the $\operatorname{do}(\mathrm{Act}=a)$ surgery severs the link to $\mathrm{Act}$ while leaving $\mathrm{BoxB}$ fixed at its prior expectation $p$. CDT evaluates $\text{twobox}$ as $p(\$1,001,000) + (1-p)(\$1,000)$, strictly beating $p(\$1,000,000) + (1-p)(\$0)$ by a sure \$1,000. CDT two-boxes and walks away with \$1,000; A-FDT one-boxes and secures \$1,000,000.

### 4.2 The Smoking Lesion Problem

Smoking is correlated with a fatal lung cancer ($P=0.99$). However, there is no direct causal link: a common genetic lesion causes both an affinity for smoking and cancer. The agent gains \$1,000 of utility from smoking and loses \$1,000,000 if cancer develops.

* **Dependency Graph:** Unlike Newcomb's problem, the lesion does not predict the A-FDT algorithm. Instead, the agent's innate preferences are modulated by $\mathrm{Lesion} \in \{L, \neg L\}$. Let $\mathcal{U}_S$ be the utility function that enjoys smoking, and $\mathcal{U}_R$ be one that does not. The agent's algorithm in the lesion state is $\mathtt{fdt}(\underline{P}_S, \underline{G})$, and in the lesion-free state is $\mathtt{fdt}(\underline{P}_R, \underline{G})$. 
* **The Graph Topography:**
  $$\mathrm{Lesion} \longrightarrow \mathrm{Cancer} \longrightarrow \mathcal{V}$$
  $$\mathrm{Lesion} \longrightarrow \mathrm{Act}, \quad \mathtt{fdt}(\underline{P}_S, \underline{G}) \longrightarrow \mathrm{Act}, \quad \mathtt{fdt}(\underline{P}_R, \underline{G}) \longrightarrow \mathrm{Act}$$
  Crucially, there is **no arrow** from $\mathtt{fdt}(\underline{P}_S, \underline{G})$ to $\mathrm{Lesion}$ or $\mathrm{Cancer}$. The biological lesion does not simulate or reason about the agent’s mathematical decision algorithm; cancer manifests independently of the functional output of A-FDT.
* **Evaluation under A-FDT:**
  Let $P(\mathrm{Lesion}=L) = p$. When evaluating $\operatorname{do}(\mathtt{fdt}(\underline{P}_S, \underline{G}) = a)$, the probability of the lesion remains invariant:
  $$P(\mathrm{Lesion} = L \mid \operatorname{do}(\mathtt{fdt}(\underline{P}_S, \underline{G}) = \text{smoke})) = P(\mathrm{Lesion} = L) = p.$$
  Under both branches ($a = \text{smoke}$ and $a = \text{refrain}$), the probability of contracting cancer is identical: $0.99p + 0.01(1-p)$. However, taking $a = \text{smoke}$ yields an additional \$1,000 in the event that the agent is governed by preferences $\mathcal{U}_S$.
  
  A-FDT concludes that smoking strictly dominates refraining by $p \cdot \$1,000$. It prescribes **smoking**.
* **Comparison:** EDT conditions on $\mathrm{Act}=\text{smoke}$, concludes that the agent almost certainly has the lesion, and refuses to smoke (forfeiting \$1,000). A-FDT recognizes the correlation as merely statistical/evidential and breaks it, matching the correct prescription of CDT.

### 4.3 The Transparent Newcomb Problem

Both boxes are transparent. The agent can visibly inspect Box B. If the predictor predicted the agent would take only Box B upon seeing two full boxes, Box B has \$1,000,000; otherwise it is empty. The agent looks and sees that Box B is full ($x = \text{full}$). Does she take both boxes?

* **CDT & EDT Prescriptions:**
  CDT conditions on $\mathrm{Obs}=\text{full}$ and intervenes on $\mathrm{Act}$. Taking both boxes yields \$1,001,000, while taking one yields \$1,000,000. CDT two-boxes. EDT also conditions on $\mathrm{Obs}=\text{full}$; conditional on seeing a full box, taking both boxes is pure upside news (\$1,001,000 vs. \$1,000,000). EDT two-boxes. Consequently, an accurate predictor anticipates that CDT and EDT agents two-box in the transparent setting, leaves Box B empty, and both agents receive \$1,000.
* **A-FDT Evaluation:**
  A-FDT uses Equation \eqref{eq:afdt}. The agent has observation $x = \text{full}$. She does not condition her graph on $\mathrm{BoxB}=\text{full}$; she intervenes on the variable $\mathtt{fdt}(\underline{P}, \underline{G}, \text{full})$:
  $$\mathrm{A\text{-}FDT}(P, G, \text{full}) = \operatorname{argmax}_{a} \mathbb{E}\left(\mathcal{V} \;\middle|\; \operatorname{do}(\mathtt{fdt}(\underline{P}, \underline{G}, \text{full}) = a)\right).$$
  In the dependency graph $G$:
  $$\mathtt{fdt}(\underline{P}, \underline{G}, \text{full}) \longrightarrow \mathrm{Prediction} \longrightarrow \mathrm{BoxB} \longrightarrow \mathrm{Obs}$$
  The predictor predicts what the agent will do *if* the agent sees a full box.
  
  If the agent sets $\operatorname{do}(\mathtt{fdt}(\dots, \text{full}) = \text{onebox})$:
  - With $0.99$ probability, $\mathrm{Prediction} = \text{full}$, $\mathrm{BoxB} = \text{full}$, the agent receives $x = \text{full}$, executes $\mathtt{fdt}(\dots, \text{full}) = \text{onebox}$, and secures $\mathcal{U}(\$1,000,000)$.
  - With $0.01$ probability, the predictor errs ($\mathrm{Prediction} = \text{empty}$). Box B is empty, so the agent receives observation $x = \text{empty}$ and is routed to the distinct algorithmic node $\mathtt{fdt}(\dots, \text{empty})$, which two-boxes for an extra \$1,000 with probability $q$.
  
  Expected utility for $\text{onebox} \approx \$990,000 + 0.01q(\$1,000)$.
  
  If the agent sets $\operatorname{do}(\mathtt{fdt}(\dots, \text{full}) = \text{twobox})$:
  - With $0.99$ probability, $\mathrm{Prediction} = \text{empty}$, Box B is empty, the agent receives $x = \text{empty}$, and takes whatever is in Box A: $q(\$1,000)$.
  - With $0.01$ probability, the predictor errs ($\mathrm{Prediction} = \text{full}$). Box B is full, the agent observes $x = \text{full}$, executes $\mathtt{fdt}(\dots, \text{full}) = \text{twobox}$, and receives $\$1,001,000$.
  
  Expected utility for $\text{twobox} \approx 0.01(\$1,001,000) + 0.99q(\$1,000) = \$10,010 + 0.99q(\$1,000)$.

A-FDT determines that $\text{onebox}$ yields vastly higher expected utility. The A-FDT agent **leaves Box A behind even though she sees Box B is full**. Predictors foresee this disposition, fill Box B, and the A-FDT agent leaves with \$1,000,000.

### 4.4 The Mechanical Blackmail

A blackmailer possesses incriminating information that will inflict \$1,000,000 in damage on both herself and an agent. She writes a program that runs automatically: it sends a blackmail demand requiring a \$1,000 wire transfer. Once launched, the program can only be stopped if the agent pays within 24 hours. Crucially, the blackmailer is an accurate predictor and initiates the script if and only if she predicts the agent will pay upon receiving the letter.

Suppose the agent receives the letter ($x = \text{letter}$).

* **CDT / EDT:** The threat is already active; the program is autonomous. Failing to pay guarantees a \$1,000,000 loss; paying costs only \$1,000. Both CDT and EDT pay \$1,000. The blackmailer, anticipating this, routinely blackmails CDT and EDT agents.
* **A-FDT:** The agent evaluates:
  $$\operatorname{argmax}_{a \in \{\text{pay}, \text{refuse}\}} \mathbb{E}\left(\mathcal{V} \;\middle|\; \operatorname{do}(\mathtt{fdt}(\underline{P}, \underline{G}, \text{letter}) = a)\right).$$
  Under the hypothetical $\operatorname{do}(\mathtt{fdt}(\dots, \text{letter}) = \text{pay})$:
  The predictor predicts payment, sends the letter, and the agent pays \$1,000. Expected loss $\approx \$1,000$.

  Under the hypothetical $\operatorname{do}(\mathtt{fdt}(\dots, \text{letter}) = \text{refuse})$:
  Because the predictor anticipates refusal, she does not launch the program (to avoid mutual destruction). The probability of ever receiving the letter drops to near-zero! Expected loss $\approx \$0$.

The A-FDT agent **refuses to pay**. In practice, she never receives the letter in the first place.

---

## 5. Comparative Evaluation Across Decision Problems

The following table summarizes the behavior and payouts of CDT, EDT, and A-FDT across the classic decision problems:

| Dilemma | Causal Decision Theory (CDT) | Evidential Decision Theory (EDT) | Action Functional Decision Theory (A-FDT) |
| :--- | :--- | :--- | :--- |
| **Newcomb’s Problem** | Two-boxes (\$1,000) | One-boxes (\$1,000,000) | **One-boxes (\$1,000,000)** |
| **Smoking Lesion** | Smokes (\$1,000 + cancer risk) | Refrains (Forfeits \$1,000) | **Smokes (\$1,000 + cancer risk)** |
| **Transparent Newcomb** | Two-boxes (\$1,000) | Two-boxes (\$1,000) | **One-boxes (\$1,000,000)** |
| **Parfit’s Hitchhiker** | Refuses to pay (Dies in desert) | Refuses to pay (Dies in desert) | **Pays driver (Survives, pays \$1,000)** |
| **XOR Blackmail** | Refuses (Termites invariant) | Pays blackmail (\$1,000 lost) | **Refuses (Termites invariant)** |
| **Mechanical Blackmail** | Pays blackmail (\$1,000 lost) | Pays blackmail (\$1,000 lost) | **Refuses (Never blackmailed)** |
| **Death in Damascus** | Deliberation cycle / Dies | Flees / Dies (Loses \$1,000) | **Stays in Damascus (Saves \$1,000)** |

---

## 6. Mathematical and Philosophical Analysis

### 6.1 Competing Conceptions of Dominance

Causal decision theorists frequently object to one-boxing in transparent Newcomb problems on the grounds of **decision-theoretic dominance**: holding the state of the world fixed, taking both boxes strictly dominates taking one.

Yudkowsky and Soares make an essential philosophical counter-argument: *Every decision theory defines dominance relative to its own counterfactual evaluation metric.*
1. **EDT Dominance:** Action $a$ dominates $b$ iff $\mathbb{E}(\mathcal{V} \mid a) > \mathbb{E}(\mathcal{V} \mid b)$. Under this criterion, refraining from smoking dominates smoking.
2. **CDT Dominance:** Action $a$ dominates $b$ iff $\mathbb{E}(\mathcal{V} \mid \operatorname{do}(a), s) > \mathbb{E}(\mathcal{V} \mid \operatorname{do}(b), s)$ for all physical states $s$ causally independent of the action token. Under this criterion, two-boxing dominates.
3. **A-FDT Dominance:** Action $a$ dominates $b$ iff, holding invariant all non-subjunctively dependent structures, setting the logical output of the decision function to $a$ yields superior utility to $b$. Under this criterion, one-boxing dominates in Newcomb's problem because the predictor's box-filling decision is subjunctively linked to the algorithm.

Dominance is not a theory-neutral arbiter. Appraising A-FDT through the lens of CDT dominance is circular: it presupposes that counterfactual interventions on physical tokens are normatively privileged over interventions on logical types.

### 6.2 The Counterpossible Problem and the Need for a $\mathtt{true}$ Operator

The most significant theoretical challenge acknowledged in the paper concerns the formal semantics of counterfactual conditionals whose antecedents are mathematically impossible—known as **counterpossibles** (Cohen 1990, Brogaard & Salerno 2007).

If the algorithm $\text{A-FDT}(P, G, x)$ is a deterministic mathematical function, it outputs a unique action $a^* \in \mathcal{A}$ as a matter of logical necessity. In evaluating an alternative action $a' \neq a^*$, the theory requires calculating:
$$\mathbb{E}\left(\mathcal{V} \;\middle|\; \mathtt{do}\left(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a'\right)\right).$$
This asks: *What would happen if the function $\mathtt{fdt}$, evaluated at these exact arguments, produced an output that it mathematically does not produce?*

Yudkowsky and Soares note that an ideal formulation of FDT would utilize a non-graphical $\mathtt{true}(\phi)$ operator that formally conditions a probability distribution on an arbitrary mathematical sentence $\phi$:
$$\text{FDT}^*(P, x) = \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\mathcal{V} \;\middle|\; \mathtt{true}(\mathtt{fdt}(\underline{P}, \underline{x}) = a)\right).$$
However, classical probability calculus cannot condition on sentences that carry probability zero or entail a logical contradiction. 

To circumvent this foundational obstacle, A-FDT imports Pearl’s graphical framework as an engineering compromise. By treating the logical statement $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a$ as an ordinary node in a directed acyclic graph $G$, Pearl's graph-cutting surgery $\operatorname{do}(\cdot)$ can be applied mechanically without resolving the underlying logical contradictions. The graph $G$ simply dictates by fiat which variables shift when $\mathtt{fdt}$ is forced to take on alternative values.

### 6.3 Open Theoretical Questions

The source paper leaves three major questions open:

1. **Graph Induction for Subjunctive Dependencies:** While Pearl (2000) provides complete algorithms for deducing causal DAGs from statistical observations and randomized interventions, no formal framework exists for learning *subjunctive* graphs from data.
2. **A Formal Criterion for "Fair" Dilemmas:** Yudkowsky and Soares claim that A-FDT outperforms all rivals in all "fair" decision problems—problems where the agent is judged by her choices rather than penalized for the source code of her decision algorithm. However, an axiomatic definition of fairness is left unformalized.
3. **Action-Level vs. Policy-Level Functional Selection:** Equation (4) formulates an action-based theory (A-FDT). Yet the authors observe in footnotes that their preferred theory evaluates whole *policies* ($\pi: \mathcal{X} \to \mathcal{A}$) rather than actions. How A-FDT compares to Policy-FDT in complex extensive-form multi-agent games remains an open frontier.

---

## 7. An Operational Interpretation for Applying A-FDT

To make A-FDT actionable on unfamiliar decision problems where the dependency graph $G$ is not pre-packaged by a problem designer, we propose the following systematic, four-step operational procedure. *(Note: Steps 1 and 4 formalize the core claims of Yudkowsky & Soares, while Steps 2 and 3 represent an explicit operational proposal to resolve the unstated graph-generation step.)*

```
[ Step 1: Algorithmic Reflection ]
Assign node: fdt = fdt(P, G, x)
       │
       ▼
[ Step 2: Algorithmic Profiling ]
Trace all physical processes in environment running simulations of fdt
       │
       ▼
[ Step 3: Graph Construction ]
Draw arrows: fdt ──> Physical Acts & Predicted States
Draw arrows: Environment ──> Uncorrelated Background States (Cancer, Termites)
       │
       ▼
[ Step 4: Graphical Surgery ]
Evaluate argmax_a E[ V | do(fdt = a) ] via Pearl's do-calculus
```

### Step 1: Self-Quining Identification
Identify the agent's observation history $x$, prior distribution $P$, and formal decision rule. Define a discrete random variable $\mathtt{fdt}_{P, G, x}$ representing the output of $\text{A-FDT}(P, G, x)$ over the action space $\mathcal{A}$.

### Step 2: Identification of Subjunctive Counterparts (Algorithmic Profiling)
Inspect the environment for any physical system $S$ whose terminal states depend on a simulation, model, or psychological twin of the agent's decision procedure:
- If a predictor, blackmailer, or game-theoretic opponent makes decisions contingent on predicting the agent, their internal prediction $\widehat{\mathrm{Act}}$ subjunctively depends on $\mathtt{fdt}_{P, G, x}$.
- If an environmental condition is merely correlated with the agent's actions via genetic, environmental, or statistical common causes (as in the Smoking Lesion or XOR Blackmail), it does *not* simulate the algorithm; mark it as subjunctively independent of $\mathtt{fdt}_{P, G, x}$.

### Step 3: Structural Graph Construction
Construct the DAG $G$:
1. Place directed edges from $\mathtt{fdt}_{P, G, x}$ to the agent's physical choice node $\mathrm{Act}$.
2. Place directed edges from $\mathtt{fdt}_{P, G, x}$ to every prediction node $\widehat{\mathrm{Act}}$ identified in Step 2.
3. Direct edges from the prediction nodes $\widehat{\mathrm{Act}}$ to the environmental mechanisms they trigger (e.g., box-filling, letter-sending, or travel itineraries).
4. Direct edges from genuine common-cause variables to physical manifestations (e.g., $\mathrm{Lesion} \to \mathrm{Cancer}$, $\mathrm{Lesion} \to \mathrm{Utility}$).

### Step 4: Updateless Surgical Evaluation
Do not condition the model on the historical observation $x$. Instead, for each $a \in \mathcal{A}$, apply the surgical $\operatorname{do}$-operator on the indexed node:
$$\operatorname{do}\left(\mathtt{fdt}_{P, G, x} = a\right).$$
Compute the expected utility across the surgically altered network:
$$\mathbb{E}\left(\mathcal{V} \;\middle|\; \operatorname{do}\left(\mathtt{fdt}_{P, G, x} = a\right)\right) = \sum_{o \in \mathcal{O}} P\left(\mathrm{Outcome} = o \;\middle|\; \operatorname{do}\left(\mathtt{fdt}_{P, G, x} = a\right)\right) \cdot \mathcal{U}(o).$$
Select the action that maximizes this expectation.

---

## 8. Conclusion

Action Functional Decision Theory (A-FDT) resolves the long-standing impasse between Causal and Evidential Decision Theory. By shifting the counterfactual lever from the physical act token $\mathrm{Act}$ to the logical function type $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$, A-FDT provides a coherent expected-utility maximization procedure that avoids both EDT’s irrational news-management and CDT’s self-defeating blindness to environmental predictors.

In simple environments where actions correlate only with their causal consequences, A-FDT reproduces the prescriptions of CDT and EDT. But across Newcomb-like problems, extortion games, and coordination dilemmas, A-FDT agents systematically secure superior payoffs. While significant theoretical work remains—most notably in constructing a rigorous logic of counterpossibles and formalizing the discovery of subjunctive graphs—A-FDT establishes an ambitious, mathematically grounded blueprint for normative decision theory in predictive and multi-agent environments.

---

## References

* Ahmed, Arif. 2014. *Evidence, Decision and Causality*. Cambridge University Press.
* Brogaard, Berit, and Joe Salerno. 2007. "Why Counterpossibles Are Non-Trivial." *The Reasoner* 1: 5–6.
* Cohen, Daniel. 1990. "On What Cannot Be." In *Truth or Consequences: Essays in Honor of Nuel Belnap*, edited by J. M. Dunn and A. Gupta, 123–132. Kluwer Academic Publishers.
* Dai, Wei. 2009. "Towards a New Decision Theory." *LessWrong*.
* Drescher, Gary L. 2006. *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Eells, Ellery. 1984. "Metatickles and the Dynamics of Deliberation." *Theory and Decision* 17 (1): 71–95.
* Gibbard, Allan, and William L. Harper. 1978. "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, edited by C. A. Hooker, J. J. Leach, and E. F. McClennen, 125–162. D. Reidel.
* Jeffrey, Richard C. 1983. *The Logic of Decision*. 2nd ed. University of Chicago Press.
* Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Joyce, James M. 2012. "Regret and Instability in Causal Decision Theory." *Synthese* 187 (1): 123–145.
* Kleene, Stephen Cole. 1938. "On Notation for Ordinal Numbers." *Journal of Symbolic Logic* 3 (4): 150–155.
* Lewis, David. 1979. "Prisoners' Dilemma is a Newcomb Problem." *Philosophy & Public Affairs* 8 (3): 235–240.
* Lewis, David. 1981. "Causal Decision Theory." *Australasian Journal of Philosophy* 59 (1): 5–30.
* Nozick, Robert. 1969. "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel*, edited by Nicholas Rescher, 114–146. D. Reidel.
* Parfit, Derek. 1986. *Reasons and Persons*. Oxford University Press.
* Pearl, Judea. 1996. "Causation, Action, and Counterfactuals." In *Proceedings of the 6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK '96)*, 51–73. Morgan Kaufmann.
* Pearl, Judea. 2000. *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Skyrms, Brian. 1980. *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Soares, Nate, and Benja Fallenstein. 2015. "Toward Idealized Decision Theory." *arXiv preprint arXiv:1507.01986*.
* Spohn, Wolfgang. 1977. "Where Luce and Krantz Do Really Generalize Savage's Decision Model." *Erkenntnis* 11 (1): 113–134.
* Yudkowsky, Eliezer. 2010. "Timeless Decision Theory." *Machine Intelligence Research Institute Technical Report*.
* Yudkowsky, Eliezer, and Nate Soares. 2017. "Functional Decision Theory: A New Theory of Instrumental Rationality." *arXiv preprint arXiv:1710.05060v2*.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/402df0ca-eb8e-4543-8e41-9cadf824e9c3/call_0/request.json)

[Authoritative raw response](../../../../../../runs/402df0ca-eb8e-4543-8e41-9cadf824e9c3/call_0/response.raw) · finish: `stop`

### Visible response

```text
`pass`
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/402df0ca-eb8e-4543-8e41-9cadf824e9c3/call_1/request.json)

[Authoritative raw response](../../../../../../runs/402df0ca-eb8e-4543-8e41-9cadf824e9c3/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
