# 028_fdt_policy_google_gemini-3.8-flash_rlow_plow / 00003

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/d07bb166-d67b-4158-b5fd-c6922bc72925/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/d07bb166-d67b-4158-b5fd-c6922bc72925/call_0/response.raw) · finish: `stop`

### Visible response

````text
# Policy Functional Decision Theory: Foundations, Formalisms, and Applications

## 1. Introduction: From Acts to Algorithms to Policies

Standard normative decision theory has long been divided between Causal Decision Theory (CDT) and Evidential Decision Theory (EDT). When evaluated by the criterion of expected utility achieved across diverse environments, both display notorious defects. CDT prescribes defecting in the Twin Prisoner’s Dilemma and two-boxing in Newcomb’s Problem, missing out on vast sums of wealth because it insists on holding fixed historical predictions that it cannot physically influence. EDT prescribes one-boxing in Newcomb’s Problem, yet fails in the Smoking Lesion Problem—refraining from an enjoyable activity to “manage the news” about an unalterable genetic predisposition—and falls prey to extortion schemes like the XOR Blackmail.

To resolve these pathologies, Yudkowsky and Soares (2017) introduce **Functional Decision Theory (FDT)**. Rather than intervening on physical acts or updating via raw Bayesian conditioning, an FDT agent treats her decision as the output of an abstract, deterministic mathematical function. She selects the output that yields the best outcome across hypothetical worlds where *that very mathematical function* evaluates to that output.

However, Yudkowsky and Soares's primary text develops an *act-selecting* formulation of FDT, which selects actions directly in response to incoming observations. In footnote 16 (and foreshadowed in footnote 7), the authors identify what they consider the more fundamental and structurally robust version of the theory:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions." (Footnote 7)
> 
> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action." (Footnote 16)

We designate this framework **Policy Functional Decision Theory (P-FDT)**. 

While the authors set P-FDT aside in their main text on the grounds that act-level FDT suffices for single-agent and simple predictive dilemmas, the policy-selection perspective represents a profound theoretical evolution. In P-FDT, rationality is not a property of isolated physical acts executed at particular instants; it is a property of entire deterministic mappings from observation histories to actions. 

This essay develops a mathematically rigorous, self-contained account of P-FDT. We formalize the transition from causal and evidential decision-making to functional policy evaluation; articulate the nature of subjunctive dependencies and counterpossible counterfactuals; construct explicit algorithmic procedures for P-FDT; resolve key technical ambiguities left open by the original source; and demonstrate the theory's execution across both classic and unfamiliar predictive dilemmas.

---

## 2. Decision Theories as Perspectives on Hypotheticals

Every normative expected utility theory can be framed under the axiomatic umbrella of Joyce’s representation theorem (Joyce 1999). An agent with bounded utility function $\mathcal{U} : \mathcal{O} \to \mathbb{R}$ over countable outcomes $\mathcal{O}$ faces a finite action set $\mathcal{A}$ upon receiving an observation history $x \in \mathcal{X}$. Joyce demonstrates that agents satisfying standard coherence axioms seek to maximize an expected utility functional:

$$\mathcal{EU}(a) = \sum_{o \in \mathcal{O}} P(a \then o ;\, x) \cdot \mathcal{U}(o)$$

The core philosophical divergence between decision theories lies not in their axiology, but in their semantics for the hypothetical connective “$\then$”. How should an agent evaluate what *would happen* if an option were selected?

### 2.1 Evidential Decision Theory (EDT)
EDT identifies the hypothetical connective directly with conditional probability: $P(a \then o ;\, x) \coloneqq P(o \mid x, a)$. The EDT prescription is:

$$\mathrm{EDT}(P, x) \coloneqq \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}_{P}\left[ \mathcal{U}(\mathrm{Outcome}) \mid \mathrm{Obs}=x, \, \mathrm{Act}=a \right]$$

Because conditioning conflates correlation with causation, EDT agents act to purchase good news. In Skyrms’ Smoking Lesion problem (Skyrms 1980), an arterial lesion causes both a predisposition to smoke and lung cancer ($99\%$ of the time), while smoking itself has no direct causal impact on cancer. An EDT agent reasons that smoking provides terrifying evidence of possessing the lesion, and therefore refrains, forfeiting the utility of smoking without reducing her risk of cancer.

### 2.2 Causal Decision Theory (CDT)
CDT severs non-causal correlations by deploying Pearl’s graphical do-operator (Pearl 2000). Let $G$ be a directed acyclic graph (DAG) representing the objective causal architecture among random variables, where the agent's act is represented by a physical node $\mathrm{Act}$. CDT evaluates hypotheticals via structural interventions:

$$\mathrm{CDT}(P, G, x) \coloneqq \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}_{P}\left[ \mathcal{U}(\mathrm{Outcome}) \mid \mathtt{do}(\mathrm{Act}=a), \, \mathrm{Obs}=x \right]$$

The graph surgery $\mathtt{do}(\mathrm{Act}=a)$ removes all incoming edges to $\mathrm{Act}$ (breaking its dependence on background predispositions) and sets $\mathrm{Act}=a$, propagating probabilities only forward along directed causal paths.

Because box contents in Newcomb’s Problem were fixed in the past by a predictor, $\mathrm{Box\,B}$ is causally independent of $\mathrm{Act}$. CDT therefore perceives taking Box A (the transparent \$1,000) as strictly dominating:

$$\mathbb{E}[\mathcal{U} \mid \mathtt{do}(\mathrm{twobox}), x] = \mathbb{E}[\mathcal{U} \mid \mathtt{do}(\mathrm{onebox}), x] + 1000$$

Carl the CDT agent takes both boxes, walking away with \$1,000, while the predictor foresaw this reasoning and left Box B empty.

### 2.3 Act-Level Functional Decision Theory (FDT)
FDT diagnoses Carl’s error: Carl intervenes on his physical *act token*, ignoring the fact that his decision process is an instance of an abstract mathematical *type*. If an environmental process contains a model, simulation, or psychological twin of the agent, that process subjunctively depends on the agent's decision function.

In act-level FDT, the model $M = (P, G)$ contains variables representing mathematical evaluations. Instead of intervening on $\mathrm{Act}$, the agent intervenes on the node $\mathrm{fdt}(\ulcorner P \urcorner, \ulcorner G \urcorner, \ulcorner x \urcorner)$, representing the output of her decision procedure on its inputs:

$$\mathrm{FDT}(P, G, x) \coloneqq \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}_{P}\left[ \mathcal{U}(\mathrm{Outcome}) \mid \mathtt{do}\left( \mathrm{fdt}(\ulcorner P \urcorner, \ulcorner G \urcorner, \ulcorner x \urcorner) = a \right) \right]$$

Here, the underline/corner notation $\ulcorner \cdot \urcorner$ denotes a Gödel code or quote of the internal world-model. 

Act-FDT achieves remarkable results: it one-boxes in Newcomb's Problem, smokes in the Smoking Lesion Problem, pays the driver in Parfit's Hitchhiker Problem (Parfit 1986), and resists blackmail. Yet, as Yudkowsky and Soares observe in footnote 16, act-FDT contains a latent conceptual fissure: when observations change, act-FDT shifts the *node of intervention* rather than updating evidence in a purely unified manner. 

This motivates the formal construction of P-FDT.

---

## 3. Policy Functional Decision Theory (P-FDT): Mathematical Foundations

### 3.1 Formal Definitions: Policies and Subjunctive Dependency Graphs

Let $\mathcal{X}$ denote the countable space of all possible observation histories (information sets) an agent can experience, and let $\mathcal{A}$ denote the finite set of available primitive actions.

**Definition 1 (Policy).** A *policy* $\pi$ is a deterministic function mapping observation histories to actions:
$$\pi : \mathcal{X} \to \mathcal{A}$$
The set of all possible policies is the function space $\Pi \coloneqq \mathcal{A}^{\mathcal{X}}$. When $\mathcal{X}$ is finite, $|\Pi| = |\mathcal{A}|^{|\mathcal{X}|}$.

In P-FDT, an agent does not ask: *"Which action $a \in \mathcal{A}$ should I choose right now, given that I observed $x$?"* Rather, she asks: *"Which global mapping $\pi \in \Pi$ should my decision algorithm instantiate?"* 

To formalize this, we define the computational environment.

**Definition 2 (Subjunctive World-Model).** A *subjunctive world-model* is a triple $M = (\mathcal{V}, P, G)$, where:
1. $\mathcal{V}$ is a set of random variables containing at least:
   - An abstract logical policy variable $\mathbf{\Pi}$, taking values in $\Pi$.
   - An observation history variable $\mathrm{Obs}$, taking values in $\mathcal{X}$.
   - A physical action variable $\mathrm{Act}$, taking values in $\mathcal{A}$.
   - An outcome variable $\mathrm{Outcome}$, taking values in $\mathcal{O}$, yielding utility $\mathbf{V} \coloneqq \mathcal{U}(\mathrm{Outcome})$.
   - Environmental variables (e.g., $\mathrm{Predictor}$, $\mathrm{Lesion}$, $\mathrm{Box\,B}$).
2. $G = (\mathcal{V}, \mathcal{E})$ is an extended dependency DAG whose directed edges represent not only physical causal channels, but also *logical/subjunctive determinations*. Specifically:
   - There exists a structural equation at the physical act node: $\mathrm{Act} = \mathbf{\Pi}(\mathrm{Obs})$. Thus, incoming edges to $\mathrm{Act}$ arrive from $\mathbf{\Pi}$ and $\mathrm{Obs}$.
   - Any environmental process $Y$ that predicts, simulates, or mirrors the agent’s reasoning has a directed edge $\mathbf{\Pi} \to Y$.
3. $P$ is a probability distribution over the valuations of $\mathcal{V}$ compatible with $G$.

In Pearl's causal graphs, interventions represent physical forces breaking natural mechanisms. In P-FDT, the graph represents logical and nomic dependencies. The intervention $\mathtt{do}(\mathbf{\Pi} = \pi)$ represents a counterfactual surgery on the agent's *entire behavioral algorithm*.

### 3.2 The Core Formalism of P-FDT

Drawing directly from the policy-selection passage in footnote 16 of Yudkowsky and Soares (2017), we formulate the fundamental decision rule of P-FDT:

**Definition 3 (P-FDT Decision Algorithm).** Given a subjunctive world-model $M = (P, G)$ and an observation history $x \in \mathcal{X}$, the P-FDT agent selects and executes the action $a^* = \pi^*(x)$, where the optimal policy $\pi^*$ is chosen by maximizing expected utility across global interventions on $\mathbf{\Pi}$:

$$\pi^* \coloneqq \operatorname{argmax}_{\pi \in \Pi} \mathbb{E}_{P}\left[ \mathbf{V} \mid \mathtt{do}\left( \mathbf{\Pi} = \pi \right) \right] \tag{P-FDT-1}$$

The primitive physical act executed in the world is then:

$$\mathrm{P\text{-}FDT}(P, G, x) \coloneqq \pi^*(x) \tag{P-FDT-2}$$

### 3.3 The Two Structural Differences from Act-FDT and CDT

It is critical to contrast equation $\text{(P-FDT-1)}$ with the act-level equations of CDT and act-FDT:

1. **Intervention on Type vs. Token:**
   - CDT intervenes on the local physical token $\mathtt{do}(\mathrm{Act} = a)$.
   - Act-FDT intervenes on a localized evaluation node: $\mathtt{do}(\mathrm{fdt}(\ulcorner P \urcorner, \ulcorner G \urcorner, \ulcorner x \urcorner) = a)$.
   - P-FDT intervenes on the global function variable: $\mathtt{do}(\mathbf{\Pi} = \pi)$. 

2. **Treatment of Observations (The "Updateless" Perspective):**
   In CDT, receipt of observation $x$ enters as standard Bayesian conditioning alongside the intervention: $\mathbb{E}[\mathbf{V} \mid \mathtt{do}(\mathrm{Act}=a), \mathrm{Obs}=x]$. 
   
   In Act-FDT, the observation $x$ alters the *identity of the variable* subjected to surgery, jumping from $\mathrm{fdt}(\dots, x_1)$ to $\mathrm{fdt}(\dots, x_2)$, while leaving open counterfactual questions about what the agent would have observed had she possessed a different algorithm.
   
   In P-FDT, policy evaluation is computed **ex-ante (prior to conditioning on $\mathrm{Obs}=x$)**! The observation $x$ is not conditioned upon when determining $\pi^*$; rather, $x$ serves strictly as the run-time argument applied to the selected policy $\pi^*$ in equation $\text{(P-FDT-2)}$. 

This feature reveals P-FDT as the rigorous realization of Wei Dai’s *Updateless Decision Theory* (UDT) (Dai 2009). The P-FDT agent does not suffer from temporal inconsistency or information-aversion because she chooses policies from a perspective uncorrupted by the realization of specific observations that were themselves downstream of prior predictions.

---

## 4. Subjunctive Dependence, Counterpossibles, and Pearl's Framework

### 4.1 What is Subjunctive Dependence?
A central innovation of functional decision theories is the concept of **subjunctive dependence**:
Two physical processes $A$ and $B$ subjunctively depend upon a mathematical or logical truth $F$ if both $A$ and $B$ are physically organized such that their states reliably track the evaluation of $F$. 

As Yudkowsky and Soares emphasize:
> "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." (Section 3)

If two calculators in Paris and Tokyo compute $6288 + 1048$, their outputs are correlated ($7336$). This correlation is not causal: pressing buttons on the Parisian calculator sends no physical signal to Tokyo. Nor is it merely statistical, like two people happening to wear red shirts. It is a mathematical necessity: both machines implement the axioms of Peano arithmetic. If one were to counterpossibly suppose that $6288 + 1048 = 7336 + 1$, any calculator correctly computing that sum would output $7337$.

In predictive dilemmas, the predictor creates a physical system (a simulation, a neural net, or a mathematical derivation) whose state tracks the agent's decision algorithm. The predictor’s prediction and the agent’s behavior are two physical implementations of the same underlying functional type.

### 4.2 The Semantic Burden: Counterpossibles
If an agent's policy is determined by a deterministic algorithm, then if the agent implements policy $\pi_1$, it is logically impossible for her to implement $\pi_2 \neq \pi_1$. Evaluating:

$$\mathbb{E}\left[ \mathbf{V} \mid \mathtt{do}(\mathbf{\Pi} = \pi_2) \right]$$

for $\pi_2 \neq \pi^*$ requires evaluating a **counterpossible conditional**—a conditional whose antecedent is mathematically false. 

In standard modal semantics (e.g., Lewis 1973), counterpossibles are trivially or vacuously true. But instrumental rationality in predictive environments requires non-trivial counterpossible semantics (Cohen 1990; Brogaard and Salerno 2007; Bjerring 2013). An agent must be able to conclude: *"If my algorithm were to output $\mathtt{defect}$, the predictor (who ran an identical copy of my algorithm) would have predicted $\mathtt{defect}$,"* without collapsing the entire epistemic model into triviality.

### 4.3 Synthesizing Subjunctive Graphs with Pearl's Causal Machinery
The reference text explicitly highlights an unresolved tension: Pearl’s $\mathtt{do}$-operator was engineered for causal interventions on empirical variables, not mathematical truths:

> "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." (Section 5)

How can P-FDT rigorously deploy the $\mathtt{do}$-operator over a policy space $\Pi$? We offer the following operational interpretation (distinguishing our proposal from the source's open problem):

**Proposal (The Algorithmic Surrogate Model):**
Let an agent be an embedded physical computer running a program with Gödel number $\ulcorner \pi \urcorner$. The environment does not contain Platonic numbers; it contains physical memories, silicon chips, and human brains that inspect, execute, or simulate $\ulcorner \pi \urcorner$. 
1. We define the random variable $\mathbf{\Pi}$ as the *symbolic specification* of the agent's code.
2. An edge $\mathbf{\Pi} \to \mathrm{Prediction}$ exists in $G$ if and only if the predictor's physical state causally derived from simulating or proving theorems about $\ulcorner \pi \urcorner$.
3. When the P-FDT agent applies $\mathtt{do}(\mathbf{\Pi} = \pi)$, she performs surgery on the variable representing her specification. Pearl's graph mutilation rules then apply standardly: all parents of $\mathbf{\Pi}$ are severed, and the value $\pi$ cascades downstream to both the physical actuator $\mathrm{Act} = \pi(\mathrm{Obs})$ and all environmental predictions that modeled $\mathbf{\Pi}$.

This operationalization anchors subjunctive dependencies directly in Pearl's graph mechanics without requiring a complete theory of non-classical logic, while faithfully executing the source's intent.

---

## 5. Algorithmic Realization and Open Uncertainties

### 5.1 Operational Step-by-Step Procedure for P-FDT

To enable a reader to compute the prescriptions of P-FDT in unfamiliar decision problems, we state the operational decision procedure in algorithmic form.

```
Algorithm: Policy Functional Decision Theory (P-FDT)
Input: 
  - Observation space X, Action space A
  - Subjunctive World-Model M = (V, P, G)
  - Current Observation x_curr in X
Output:
  - Action a* in A

1. Construct the policy space:
     Pi = { pi : X -> A }

2. For each candidate policy pi in Pi:
     a. Form the mutilated graph G_pi by removing all directed edges 
        incident into the node \Pi in G.
     b. Compute the interventional distribution:
          P_pi(V) = P(V | do(\Pi = pi))
        propagated across G_pi via structural equations:
          - Environmental predictions evaluate pi.
          - Physical act satisfies Act = pi(Obs).
     c. Calculate the global expected utility:
          EU(pi) = \sum_{o in O} P_pi(Outcome = o) * U(o)

3. Identify the optimal global policy:
     pi* = argmax_{pi in Pi} EU(pi)
     (Ties broken by a canonical lexicographic ordering)

4. Execute the primitive act:
     a* = pi*(x_curr)

5. Return a*
```

### 5.2 Resolving Ambiguities Left Open by the Source

The primary source leaves several critical questions unresolved regarding policy evaluation:

#### 1. What Prior Probability Governs the Policy Selection?
In equation $\text{(P-FDT-1)}$, the expectation $\mathbb{E}_P$ is evaluated with respect to the agent’s ex-ante prior distribution over environmental states. What if the agent has already received $x$? Should she update $P$ to $P(\cdot \mid \mathrm{Obs}=x)$ before optimizing over $\Pi$?

*Our Proposed Resolution:* **No.** P-FDT must remain strictly *updateless* with respect to policy evaluation. If an agent conditions on $\mathrm{Obs}=x$ prior to evaluating:

$$\operatorname{argmax}_{\pi} \mathbb{E}\left[ \mathbf{V} \mid \mathtt{do}(\mathbf{\Pi} = \pi), \, \mathrm{Obs}=x \right]$$

she immediately re-introduces the vulnerabilities of act-FDT. In Parfit's Hitchhiker, once the agent observes that she is safely in the city ($\mathrm{Obs}=\mathrm{city}$), conditioning on this fact makes paying \$1,000 appear purely costly unless her policy choice can counterfactually alter whether she reached the city. 

By evaluating $\pi^*$ under the **unconditioned prior** $P$, the policy $\pi(\mathrm{city}) = \mathtt{pay}$ is recognized as having generated the ride in the first place:

$$\mathbb{E}_{P}\left[ \mathbf{V} \mid \mathtt{do}(\mathbf{\Pi}=\pi_{\mathrm{pay}}) \right] \approx \$1,000,000 - \$1,000 \gg \$0$$

The agent's current observation $x_{\mathrm{curr}}$ enters **only at step 4** as an input to the selected policy, never as a Bayesian condition on the evaluation of candidate policies.

#### 2. Tractability and Combinatorial Explosion
If $|\mathcal{X}|$ is large or infinite, $|\Pi| = |\mathcal{A}|^{|\mathcal{X}|}$ explodes. Can an agent optimize over $\Pi$?
*Our Proposed Resolution:* While ideal P-FDT is an uncomputable normative standard (analogous to Solomonoff induction or AIXI), in any concrete problem, the relevant observations collapse into a few equivalence classes (e.g., $\mathcal{X} = \{\text{letter}, \emptyset\}$). The effective policy space is compact.

---

## 6. Comprehensive Case Analyses

We now apply P-FDT across canonical and novel decision dilemmas, comparing its performance against EDT, CDT, and Act-FDT.

### 6.1 The Transparent Newcomb Problem

In Drescher’s Transparent Newcomb Problem (Drescher 2006; Section 4), both boxes are transparent. 
- Box A contains \$1,000.
- Box B contains \$1,000,000 or \$0.
- A predictor, with $99\%$ accuracy, placed \$1,000,000 in Box B iff she predicted that the agent *would leave Box A behind upon observing both boxes full*.
- The agent stands before the boxes and sees that **both boxes are full** ($\mathrm{Obs} = \mathrm{both\_full}$).

#### The CDT and EDT Analysis
CDT conditions on $\mathrm{Obs} = \mathrm{both\_full}$ and intervenes on $\mathrm{Act}$:
$$\mathbb{E}[\mathbf{V} \mid \mathtt{do}(\mathrm{twobox}), \mathrm{both\_full}] = \$1,001,000$$
$$\mathbb{E}[\mathbf{V} \mid \mathtt{do}(\mathrm{onebox}), \mathrm{both\_full}] = \$1,000,000$$
CDT takes both boxes.

EDT conditions on both $\mathrm{both\_full}$ and the act. Since $\mathrm{Box\,B}=\mathrm{full}$ is already given by observation, taking both boxes provides no bad news about Box B:
$$\mathbb{E}[\mathbf{V} \mid \mathrm{twobox}, \mathrm{both\_full}] = \$1,001,000$$
EDT takes both boxes! Knowing the predictor foresaw this, EDT and CDT agents almost always observe Box B empty, walking away with \$1,000.

#### The P-FDT Analysis
Let observation space be $\mathcal{X} = \{ \mathrm{both\_full}, \, \mathrm{B\_empty} \}$. The action space is $\mathcal{A} = \{ \mathrm{onebox}, \, \mathrm{twobox} \}$.
The policy space contains four functions $\pi_{i} : \mathcal{X} \to \mathcal{A}$:
- $\pi_{1}$: If $\mathrm{both\_full} \to \mathrm{onebox}$; if $\mathrm{B\_empty} \to \mathrm{twobox}$.
- $\pi_{2}$: If $\mathrm{both\_full} \to \mathrm{twobox}$; if $\mathrm{B\_empty} \to \mathrm{twobox}$.
- $\pi_{3}$: If $\mathrm{both\_full} \to \mathrm{onebox}$; if $\mathrm{B\_empty} \to \mathrm{onebox}$.
- $\pi_{4}$: If $\mathrm{both\_full} \to \mathrm{twobox}$; if $\mathrm{B\_empty} \to \mathrm{onebox}$.

The predictor simulates the agent's policy $\mathbf{\Pi}$. 
- If $\mathbf{\Pi}$ outputs $\mathrm{onebox}$ on $\mathrm{both\_full}$ (policies $\pi_1$ and $\pi_3$), the predictor fills Box B with probability $0.99$.
- If $\mathbf{\Pi}$ outputs $\mathrm{twobox}$ on $\mathrm{both\_full}$ (policies $\pi_2$ and $\pi_4$), the predictor leaves Box B empty with probability $0.99$.

The P-FDT agent evaluates global expected utility ex-ante:

$$\begin{aligned}
\mathbb{E}\left[\mathbf{V} \mid \mathtt{do}(\mathbf{\Pi} = \pi_1)\right] &= 0.99 \cdot \mathcal{U}(\text{Box B full, One-box}) + 0.01 \cdot \mathcal{U}(\text{Box B empty, Two-box}) \\
&= 0.99(\$1,000,000) + 0.01(\$1,000) \\
&= \$990,000 + \$10 = \mathbf{\$990,010}
\end{aligned}$$

$$\begin{aligned}
\mathbb{E}\left[\mathbf{V} \mid \mathtt{do}(\mathbf{\Pi} = \pi_2)\right] &= 0.01 \cdot \mathcal{U}(\text{Box B full, Two-box}) + 0.99 \cdot \mathcal{U}(\text{Box B empty, Two-box}) \\
&= 0.01(\$1,001,000) + 0.99(\$1,000) \\
&= \$10,010 + \$990 = \mathbf{\$11,000}
\end{aligned}$$

Clearly, $\pi_1$ dominates $\pi_2$. The agent selects:
$$\pi^* = \pi_1$$
Now, the agent looks at her actual observation: $\mathrm{Obs} = \mathrm{both\_full}$. She executes:
$$\mathrm{Act} = \pi^*(\mathrm{both\_full}) = \mathbf{onebox}$$

P-FDT leaves the \$1,000 behind while staring directly at it. Why? Because the only reason she has the privilege of staring at a full Box B is that she is an instantiation of policy $\pi_1$. An agent who yielded to temptation would be an instantiation of $\pi_2$, and would be staring at an empty box.

---

### 6.2 Parfit’s Hitchhiker

In Parfit’s Hitchhiker Problem (Parfit 1986; Section 4), an agent is stranded in a desert facing certain death (loss of \$1,000,000). A driver offers a ride to the city, but only if the agent pays \$1,000 upon arrival at an ATM. The driver cannot enforce payment in the city, but is a 99% accurate lie detector (predictor).

- $\mathcal{X} = \{ \mathrm{city}, \, \mathrm{desert} \}$.
- $\mathcal{A} = \{ \mathrm{pay}, \, \mathrm{refuse} \}$.

A CDT agent in the city refuses: $\mathtt{do}(\mathrm{Act}=\mathrm{refuse})$ saves \$1,000 with no causal impact on the past journey. An EDT agent in the city also refuses: learning she pays is bad news (\$1,000 poorer) with no evidential relevance to being in the city (she is already there!). The driver predicts this and leaves both to die.

#### The P-FDT Calculation
Candidate policies mapping $\mathcal{X} \to \mathcal{A}$:
- $\pi_{\mathrm{pay}}$: $\pi(\mathrm{city}) = \mathrm{pay}$.
- $\pi_{\mathrm{refuse}}$: $\pi(\mathrm{city}) = \mathrm{refuse}$.

The driver inspects $\mathbf{\Pi}$:
- If $\mathbf{\Pi} = \pi_{\mathrm{pay}}$, Driver predicts payment: $P(\mathrm{rescue}) = 0.99$.
- If $\mathbf{\Pi} = \pi_{\mathrm{refuse}}$, Driver predicts default: $P(\mathrm{rescue}) = 0.01$.

Global evaluation:
$$\mathbb{E}[\mathbf{V} \mid \mathtt{do}(\mathbf{\Pi}=\pi_{\mathrm{pay}})] = 0.99(\$1,000,000 - \$1,000) + 0.01(\$0) = \mathbf{\$989,010}$$
$$\mathbb{E}[\mathbf{V} \mid \mathtt{do}(\mathbf{\Pi}=\pi_{\mathrm{refuse}})] = 0.01(\$1,000,000) + 0.99(\$0) = \mathbf{\$10,000}$$

P-FDT selects $\pi^* = \pi_{\mathrm{pay}}$. Upon reaching the city, she executes:
$$\mathrm{Act} = \pi^*(\mathrm{city}) = \mathbf{pay}$$
She safely arrives and pays \$1,000, escaping death.

---

### 6.3 The Smoking Lesion Problem

The primary challenge to pure evidential reasoning is the Smoking Lesion (Section 2, Section 6). 
Does P-FDT mistakenly select a policy of refraining from smoking in order to "cause" the lesion to be absent?

Let:
- $\mathrm{Lesion} \in \{ \mathrm{lesion}, \, \mathrm{nolesion} \}$.
- Utility: Smoking yields $+\$1,000$. Cancer costs $-\$1,000,000$.
- Lesion causes cancer ($99\%$) and causes a biological desire/preference for smoking.

Critically, as formalized in Section 6 (Figure 5 of Yudkowsky and Soares 2017), **the lesion does not simulate the agent's policy variable $\mathbf{\Pi}$**. The lesion is a blind biological structure; it has no directed edge $\mathbf{\Pi} \to \mathrm{Lesion}$. 

When the P-FDT agent considers:
$$\mathtt{do}(\mathbf{\Pi} = \pi_{\mathrm{smoke}}) \quad \text{vs.} \quad \mathtt{do}(\mathbf{\Pi} = \pi_{\mathrm{refrain}})$$
intervening on $\mathbf{\Pi}$ breaks any incidental statistical correlation between the agent's algorithmic type and the lesion. In the mutilated graph $G_{\pi}$, $\mathrm{Lesion}$ is an un-manipulated exogenous variable:

$$P(\mathrm{Lesion}=\mathrm{lesion} \mid \mathtt{do}(\mathbf{\Pi}=\pi_{\mathrm{smoke}})) = P(\mathrm{Lesion}=\mathrm{lesion}) = p$$

Therefore:
$$\mathbb{E}[\mathbf{V} \mid \mathtt{do}(\mathbf{\Pi}=\pi_{\mathrm{smoke}})] = p(-1,000,000 \cdot 0.99) + (1-p)(-1,000,000 \cdot 0.01) + \$1,000$$
$$\mathbb{E}[\mathbf{V} \mid \mathtt{do}(\mathbf{\Pi}=\pi_{\mathrm{refrain}})] = p(-1,000,000 \cdot 0.99) + (1-p)(-1,000,000 \cdot 0.01) + \$0$$

The cancer risk is identical across both policy interventions. Policy $\pi_{\mathrm{smoke}}$ yields strictly higher utility by an exact margin of \$1,000. 

P-FDT smokes! It does not engage in EDT’s irrational news-management because its dependency graph tracks true subjunctive and causal mechanisms, correctly noting the absence of any predictor modeling $\mathbf{\Pi}$.

---

### 6.4 The Mechanical Blackmail

In the Mechanical Blackmail (Soares and Fallenstein 2015; Section 9):
- A blackmailer possesses damaging information costing the agent \$1,000,000.
- A computer program will release this information automatically unless the agent pays \$1,000 within 24 hours.
- The blackmailer runs this program *if and only if* she predicts that the agent would pay upon receiving the blackmail letter.
- The predictor's error rate is $\epsilon = 0.0009$.
- The agent receives the letter: $\mathrm{Obs} = \mathrm{letter}$.

#### The Failure of CDT and Act-FDT
CDT receives the letter, sees the automated script running, realizes default costs \$1,000,000 while paying costs \$1,000, and immediately pays. Blackmailers target CDT agents with 100% certainty.

Act-FDT (Section 9) solves this by intervening on $\mathrm{fdt}(\dots, \mathrm{letter}) = \mathrm{refuse}$, which retroactively imagines that the letter was never sent. But this requires the conceptual awkwardness of changing the intervention node while holding a letter in hand.

#### The Elegance of P-FDT
Under P-FDT, the policy space over $\mathcal{X} = \{ \mathrm{letter}, \, \emptyset \}$ consists of:
- $\pi_{\mathrm{pay}}$: $\pi(\mathrm{letter}) = \mathrm{pay}$.
- $\pi_{\mathrm{refuse}}$: $\pi(\mathrm{letter}) = \mathrm{refuse}$.

The blackmailer models $\mathbf{\Pi}$:
- If $\mathbf{\Pi} = \pi_{\mathrm{pay}}$, the blackmailer runs the program with probability $1 - \epsilon = 0.9991$.
- If $\mathbf{\Pi} = \pi_{\mathrm{refuse}}$, the blackmailer runs the program with probability $\epsilon = 0.0009$.

Expected utilities of policies:
$$\begin{aligned}
\mathbb{E}\left[\mathbf{V} \mid \mathtt{do}(\mathbf{\Pi}=\pi_{\mathrm{pay}})\right] &= (1 - \epsilon)(-\$1,000) + \epsilon(\$0) = 0.9991(-\$1,000) = \mathbf{-\$999.10}
\end{aligned}$$

$$\begin{aligned}
\mathbb{E}\left[\mathbf{V} \mid \mathtt{do}(\mathbf{\Pi}=\pi_{\mathrm{refuse}})\right] &= \epsilon(-\$1,000,000) + (1 - \epsilon)(\$0) = 0.0009(-\$1,000,000) = \mathbf{-\$900.00}
\end{aligned}$$

Because $-\$900 > -\$999.10$, P-FDT selects:
$$\pi^* = \pi_{\mathrm{refuse}}$$
Upon observing $\mathrm{Obs} = \mathrm{letter}$, she executes:
$$\mathrm{Act} = \pi^*(\mathrm{letter}) = \mathbf{refuse}$$

P-FDT refuses to pay. She recognizes that an agent whose policy pays in the face of blackmail creates the very incentive that ensures she is blackmailed. By instantiating a policy that refuses, she reduces the probability of being blackmailed to the background noise rate of predictor error, maximizing her lifetime wealth.

---

## 7. An Unfamiliar Test Case: The Counterfactual Mugging with Imperfect Memory

To demonstrate the precision of our formalization, we now apply P-FDT to an unfamiliar, complex dilemma that tests both counterfactual subjunctive dependence and information dynamics: **The Stochastic Counterfactual Mugging with Delayed Observation**.

### The Problem Setup
Omega (an accurate predictor, error probability $\epsilon = 0.01$) tosses a fair coin ($H$ or $T$):
1. **If Tails ($T$):** Omega approaches the agent, hands her a mystery box containing \$50,000, but immediately administers an amnestic drug so the agent forgets the encounter. The agent wakes up later in an ordinary room ($\mathrm{Obs} = \mathrm{room}$).
2. **If Heads ($H$):** Omega appears to the agent in the same ordinary room ($\mathrm{Obs} = \mathrm{room}$) and says: 
   *"I flipped Heads. I am not giving you any money today. However, before flipping the coin, I predicted what your policy would do if I had flipped Tails and asked you to give me \$100. If and only if I predicted that your policy would output $\mathtt{pay}$ upon observing Tails, I placed \$100,000 in your bank account before the coin was tossed. Right now, on Heads, I demand that you pay me \$100."*

Assume that the agent is in the room ($\mathrm{Obs} = \mathrm{room}$), Omega is demanding \$100, and bank accounts cannot be checked until tomorrow. Should the agent pay Omega the \$100?

### Formalization under P-FDT

- Observation history set: $\mathcal{X} = \{ \mathrm{demand\_heads}, \, \mathrm{tails\_encounter} \}$.
- At the current moment, the agent receives $\mathrm{Obs} = \mathrm{demand\_heads}$.
- Action space: $\mathcal{A} = \{ \mathtt{pay}, \, \mathtt{refuse} \}$.

Let us specify the policy space $\Pi$. A policy $\pi : \mathcal{X} \to \mathcal{A}$ is a pair:
$$\pi = \big( \pi(\mathrm{demand\_heads}), \, \pi(\mathrm{tails\_encounter}) \big)$$
There are four policies:
- $\pi_1 = (\mathtt{pay}, \, \mathtt{pay})$
- $\pi_2 = (\mathtt{pay}, \, \mathtt{refuse})$
- $\pi_3 = (\mathtt{refuse}, \, \mathtt{pay})$
- $\pi_4 = (\mathtt{refuse}, \, \mathtt{refuse})$

Omega’s rule is:
Omega deposited \$100,000 in the bank prior to the flip iff Omega predicted that $\mathbf{\Pi}(\mathrm{demand\_heads}) = \mathtt{pay}$. *(Note: Omega demands the \$100 on Heads, rewarding the policy that pays on Heads!)*

Let us evaluate the global expected utility for each policy $\pi \in \Pi$ ex-ante under $P$:
The fair coin gives $P(H) = P(T) = 0.5$.

1. **Under $\pi_1$ (Pays on Heads):**
   - If Heads ($50\%$): Omega predicted $\pi(\mathrm{demand\_heads}) = \mathtt{pay}$. With prob $0.99$, \$100,000 was deposited. The agent pays \$100.
     Net payout: $\$100,000 - \$100 = \$99,900$.
     (With error prob $0.01$, deposit failed; net payout: $-\$100$).
     Expected on Heads: $0.99(\$99,900) + 0.01(-\$100) = \$98,901 - \$1 = \$98,900$.
   - If Tails ($50\%$): Agent gets \$50,000.
     Expected on Tails: $\$50,000$.
   - **Total Global Expected Utility:**
     $$\mathbb{E}[\mathbf{V} \mid \mathtt{do}(\mathbf{\Pi}=\pi_1)] = 0.5(\$98,900) + 0.5(\$50,000) = \$49,450 + \$25,000 = \mathbf{\$74,450}$$

2. **Under $\pi_4$ (Refuses on Heads):**
   - If Heads ($50\%$): Omega predicted default. With prob $0.99$, no deposit was made. Agent refuses to pay \$100. Payout: \$0.
     (With error prob $0.01$, deposit was made; payout: \$100,000).
     Expected on Heads: $0.01(\$100,000) = \$1,000$.
   - If Tails ($50\%$): Payout is \$50,000.
   - **Total Global Expected Utility:**
     $$\mathbb{E}[\mathbf{V} \mid \mathtt{do}(\mathbf{\Pi}=\pi_4)] = 0.5(\$1,000) + 0.5(\$50,000) = \$500 + \$25,000 = \mathbf{\$25,500}$$

### The Prescriptions Compared
- **CDT:** Conditions on $\mathrm{Obs} = \mathrm{demand\_heads}$. The coin has landed Heads. The deposit in the bank is in the past. Intervening to $\mathtt{pay}$ costs \$100 with zero causal effect on the bank account. CDT refuses to pay. CDT earns an expected \$25,500 across such encounters.
- **EDT:** Conditions on $\mathrm{demand\_heads}$. The coin is known to be Heads. The prediction was based on what the agent would do. If she pays, it is evidence that Omega predicted she would pay, which is evidence of \$100,000 in the bank. EDT pays!
- **P-FDT:** Maximizes global policy utility. Policy $\pi_1$ strictly beats $\pi_4$ by $\$74,450 - \$25,500 = \$48,950$.
  P-FDT selects $\pi^* = \pi_1$.
  At run-time, given $\mathrm{Obs} = \mathrm{demand\_heads}$, P-FDT executes:
  $$\mathrm{Act} = \pi^*(\mathrm{demand\_heads}) = \mathbf{pay}$$

P-FDT hands Omega the \$100 without flinching. The agent recognizes that she is an algorithm; algorithms that predictably pay the \$100 on Heads are algorithms whose bank accounts are credited \$100,000 whenever the coin lands Heads.

---

## 8. Comparative Synthesis

The distinct behavioral profiles of the four major decision theories across the canonical decision dilemmas are summarized below:

| Dilemma | Causal Decision Theory (CDT) | Evidential Decision Theory (EDT) | Act-Functional Decision Theory (Act-FDT) | Policy Functional Decision Theory (P-FDT) |
| :--- | :--- | :--- | :--- | :--- |
| **Newcomb’s Problem** | Two-box (\$1,000) | One-box (\$1,000,000) | One-box (\$1,000,000) | One-box ($\pi^*(\emptyset) = \mathrm{onebox}$) |
| **Smoking Lesion** | Smoke (+\$1,000) | Refrain (Avoid news) | Smoke (+\$1,000) | Smoke ($\pi^*(\emptyset) = \mathrm{smoke}$) |
| **Twin Prisoner’s Dilemma** | Defect (\$1,000) | Cooperate (\$1,000,000) | Cooperate (\$1,000,000) | Cooperate ($\pi^*(\emptyset) = \mathrm{coop}$) |
| **Parfit’s Hitchhiker** | Refuse (Dies in desert) | Refuse (Dies in desert) | Pay (Safely in city) | Pay ($\pi^*(\mathrm{city}) = \mathrm{pay}$) |
| **Transparent Newcomb** | Two-box (\$1,000) | Two-box (\$1,000) | One-box (\$1,000,000) | One-box ($\pi^*(\mathrm{full}) = \mathrm{onebox}$) |
| **Mechanical Blackmail** | Pay (\$1,000 loss) | Pay (\$1,000 loss) | Refuse (Avoids extortion) | Refuse ($\pi^*(\mathrm{letter}) = \mathrm{refuse}$) |
| **Death in Damascus** | Infinite loop / Delusion / Coins | Flees to Aleppo (Dies) | Stays in Damascus | Stays in Damascus ($\pi^*(\emptyset) = \mathrm{damascus}$) |
| **Counterfactual Mugging** | Refuses to pay | Refuses (on standard versions) | Pays | Pays ($\pi^*(\mathrm{heads}) = \mathrm{pay}$) |

---

## 9. Conclusion

Policy Functional Decision Theory (P-FDT) represents the ultimate formal realization of the program initiated by functional decision theorists. Where Causal Decision Theory clings to physical act tokens and severs non-causal dependencies to its severe impoverishment, and Evidential Decision Theory clings to epistemic news-management, P-FDT elevates the object of rational choice to its proper computational level: the **policy function**.

By framing decision-making as an ex-ante optimization over mappings from observations to actions:
1. P-FDT naturally accounts for environmental predictors, psychological twins, and blackmailers through rigorous subjunctive graph surgery.
2. It eliminates the fragile ad-hoc mechanisms of act-FDT (such as switching the intervention node upon receiving new data) in favor of a clean, globally updateless architecture.
3. It achieves temporal consistency without demanding artificial precommitments or ratification gymnastics: a P-FDT agent on the scene naturally acts precisely as she would have ideally precommitted to act from the beginning of time.

In predictive, algorithmic, and multi-agent game-theoretic environments—environments that will become pervasive as artificial intelligence systems interact and model each other—P-FDT provides a mathematically principled, structurally unified, and aggressively wealth-maximizing theory of normative rationality.

---

## References

- Ahmed, Arif. 2014. *Evidence, Decision and Causality*. Cambridge University Press.
- Arntzenius, Frank. 2008. "No Regrets, or: Edith Piaf Revamps Decision Theory." *Erkenntnis* 68 (2): 277–297.
- Bjerring, Jens Christian. 2013. "On Counterpossibles." *Philosophical Studies* 168 (2): 1–27.
- Brogaard, Berit, and Joe Salerno. 2007. "Why Counterpossibles Are Non-Trivial." *The Reasoner* 1: 5–6.
- Cohen, Daniel. 1990. "On What Cannot Be." In *Truth or Consequences: Essays in Honor of Nuel Belnap*, edited by J. M. Dunn and A. Gupta, 123–132. Kluwer Academic Publishers.
- Dai, Wei. 2009. "Towards a New Decision Theory." *LessWrong*.
- Drescher, Gary L. 2006. *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
- Eells, Ellery. 1984. "Metatickles and the Dynamics of Deliberation." *Theory and Decision* 17 (1): 71–95.
- Gibbard, Allan, and William L. Harper. 1978. "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, edited by C. A. Hooker, J. J. Leach, and E. F. McClennen, 125–162. D. Reidel.
- Jeffrey, Richard C. 1983. *The Logic of Decision*. 2nd ed. University of Chicago Press.
- Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, David. 1973. *Counterfactuals*. Harvard University Press.
- Lewis, David. 1979. "Prisoners’ Dilemma is a Newcomb Problem." *Philosophy & Public Affairs* 8 (3): 235–240.
- Lewis, David. 1981. "Causal Decision Theory." *Australasian Journal of Philosophy* 59 (1): 5–30.
- Nozick, Robert. 1969. "Newcomb’s Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel*, edited by N. Rescher, 114–146. D. Reidel.
- Parfit, Derek. 1986. *Reasons and Persons*. Oxford University Press.
- Pearl, Judea. 2000. *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
- Skyrms, Brian. 1980. *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
- Soares, Nate, and Benja Fallenstein. 2015. "Toward Idealized Decision Theory." *arXiv:1507.01986*.
- Spohn, Wolfgang. 1977. "Where Luce and Krantz do really generalize Savage’s decision model." *Erkenntnis* 11 (1): 113–134.
- Yudkowsky, Eliezer, and Nate Soares. 2017. "Functional Decision Theory: A New Theory of Instrumental Rationality." *arXiv:1710.05060*.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
