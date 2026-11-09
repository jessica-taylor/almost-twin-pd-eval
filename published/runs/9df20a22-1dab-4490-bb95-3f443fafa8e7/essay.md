# The Calculus of Decision Types: A Mathematical Account of Action Functional Decision Theory (A-FDT)

## 1. Introduction: The Dilemma of Classical Decision Theories

Normative decision theory has long been divided between two paradigms: Evidential Decision Theory (EDT) and Causal Decision Theory (CDT). Both formalize rational agency as expected utility maximization relative to an agent’s subjective probabilities, but they disagree fundamentally on the epistemic perspective from which hypothetical actions are evaluated.

Consider the general expected utility framework established by Joyce (1999) and Gibbard & Harper (1978). An agent chooses an action $a$ from a finite set $\mathcal{A}$ to maximize:

$$\mathcal{EU}(a) = \sum_{j} P(a \hookrightarrow o_j ; x) \, \mathcal{U}(o_j)$$

where $\mathcal{X}$ is a countable set of observation histories, $x \in \mathcal{X}$ is the agent's current observation, $\mathcal{O} = \{o_j\}$ is a countable set of mutually exclusive outcomes, $\mathcal{U} : \mathcal{O} \to \mathbb{R}$ is a bounded utility function, and $a \hookrightarrow o_j$ is the decision hypothetical: "outcome $o_j$ would obtain if action $a$ were executed."

EDT interprets $a \hookrightarrow o_j$ via Bayesian conditionalization:

$$\text{EDT}(P, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left[\mathcal{V} \mid \text{Obs}=x, \text{Act}=a\right]$$

where $\mathcal{V} \coloneqq \mathcal{U}(\text{Outcome})$. In Newcomb's Problem, EDT correctly prescribes taking only the opaque box (one-boxing): conditional on taking one box, it is overwhelmingly probable that the predictor foresaw this choice and filled the box with \$1,000,000. However, EDT's reliance on purely statistical correlations makes it notoriously vulnerable to spurious non-causal dependencies. In Skyrms' (1980) Smoking Lesion Problem, an unobservable genetic lesion causes both an irresistible craving to smoke and fatal lung cancer. EDT agents refrain from smoking because smoking correlates with cancer, thereby forgoing the immediate \$1,000 pleasure of smoking without altering their physical predisposition to cancer—an error described by Lewis (1981) as irrational "news-managing."

CDT remedies this by enforcing Pearlian causal interventions. Representing the agent's world-model as a causal theory $(P, G)$, where $G$ is a directed acyclic graph (DAG) representing physical causal mechanisms, CDT defines:

$$\text{CDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left[\mathcal{V} \mid \operatorname{do}(\text{Act}=a), \text{Obs}=x\right]$$

The graph surgery operator $\operatorname{do}(\text{Act}=a)$ severs all incoming causal edges to the physical token variable $\text{Act}$, isolating the downstream causal consequences of the action. CDT correctly smokes in the Smoking Lesion Problem because the lesion is causally upstream of the physical act. Yet CDT fails in Newcomb's Problem: because the predictor made their prediction in the past, Box B's contents are causally independent of the agent’s present physical actuation:

$$\mathbb{E}[\mathcal{V} \mid \operatorname{do}(\text{Act}=\textit{twobox})] > \mathbb{E}[\mathcal{V} \mid \operatorname{do}(\text{Act}=\textit{onebox})]$$

CDT two-boxes, walking away with \$1,000 where an EDT agent secures \$1,000,000.

This theoretical impasse suggests that both theories construct malformed hypotheticals. EDT preserves too many correlations (tracking non-causal confounding), while CDT preserves too few (severing the logical correlation between an agent's calculation and the environmental simulations that anticipated it).

**Action Functional Decision Theory (A-FDT)** resolves this dichotomy. Rather than intervening on the physical token of an action, A-FDT evaluates counterfactuals by intervening on the *mathematical decision function* that generates the action.

---

## 2. Formalization of A-FDT

### 2.1 Pearlian Semantics Over Augmented Models

To make A-FDT mathematically precise, we augment Pearl's causal graphical framework to encompass non-causal, logical dependencies. Let an agent’s epistemic state be represented by a pair $(P, G)$, where:
- $P$ is a probability distribution over a set of random variables containing physical states, environmental observations, and mathematical sentences.
- $G = (V, E)$ is a directed acyclic graph whose vertices $V$ represent both physical variables (e.g., $\text{Act}$, $\text{Obs}$, $\text{Outcome}$) and logical/computational variables (e.g., node variables representing the outputs of algorithms), and whose directed edges $E$ represent *subjunctive dependence*.

Subjunctive dependence subsumes both physical causation (downstream effects of physical processes) and logical dependence (the instantiation or simulation of an algorithm across distinct physical coordinates).

### 2.2 The Master Equation: Equation (4)

The primary formal rule of A-FDT—presented as Equation (4), Section 5 of Yudkowsky & Soares (2017)—defines the normative action for an agent with probabilistic model $P$, dependency structure $G$, and observation history $x$:

$$\text{A-FDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left[\mathcal{V} \mid \operatorname{do}\left(\operatorname{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right] \quad \text{--- [Eq. 4]}$$

Here, $\operatorname{fdt}(\cdot, \cdot, \cdot)$ denotes the mathematical decision function governing the agent, and the underlining notation $\underline{P}, \underline{G}, \underline{x}$ denotes the syntactic representation (the Gödelian dequoting or quined code) of the distribution, graph, and observation history.

Crucially, Equation (4) differs from CDT along two structural dimensions:

1. **Type-Level Intervention vs. Token-Level Intervention:**  
   CDT executes $\operatorname{do}(\text{Act}=a)$, intervening on the physical motor actuation. A-FDT executes $\operatorname{do}(\operatorname{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)$, intervening on the *logical output* of the decision procedure itself. By Pearl’s graph surgery, any variable in the universe that subjunctively depends on this logical output (such as a predictor's simulation, a twin's decision, or the agent's physical limbs) is updated downstream of the surgery.
   
2. **Updateless/Global Conditioning vs. Bayesian Update:**  
   In CDT, receipt of observation history $x$ updates the background distribution via regular Bayesian conditioning: $P(\cdot \mid \text{Obs}=x)$. In A-FDT, the observation $x$ is not treated as an evidentiary condition that truncates the counterfactual space; instead, $x$ enters as an *argument* determining *which mathematical variable* is targeted for surgery: $\operatorname{fdt}(\underline{P}, \underline{G}, \underline{x})$. The expected utility is evaluated across the prior distribution subject to the logical intervention, allowing the hypothetical to alter environmental events that determined whether $x$ was observed in the first place.

---

## 3. Subjunctive Dependence, Quining, and Counterpossibles

### 3.1 Subjunctive Dependence vs. Causal and Statistical Dependence

A-FDT establishes an ontology of three distinct relations:
- **Statistical Correlation:** $P(Y \mid X) \neq P(Y)$. Susceptible to common causes (e.g., smoking and cancer via a lesion).
- **Causal Dependence:** $P(Y \mid \operatorname{do}(X=x)) \neq P(Y)$. Physical signals propagating through spacetime paths at or below $c$.
- **Subjunctive Dependence:** A broader relation encompassing mathematical identity and logical representation. If two physical systems compute the same mathematical function $f$, or if system $B$ contains an accurate model of system $A$, both systems subjunctively depend on the abstract output of $f$.

Causal dependence is a special case of subjunctive dependence: a physical scribe recording the output of a calculator subjunctively depends on the arithmetic function that the calculator evaluates. However, subjunctive dependence extends across space-like and time-like separations without requiring physical signals. If two isolated calculators evaluate $6288 + 1048$, the fact that both output $7336$ is not mediated by a radio wave traveling between them; it is enforced by the logical consistency of arithmetic.

### 3.2 Quining and Harmless Self-Reference

Equation (4) exhibits an apparent circularity: the function $\text{A-FDT}$ defines its output by evaluating an expectation over a node that names $\text{A-FDT}$ itself on its current inputs.

As established in theoretical computer science via Kleene’s Second Recursion Theorem (Kleene 1938), this self-reference is formally constructive. A program can query and inspect its own source code without entering an infinite regress. An agent computing $\text{A-FDT}(P, G, x)$ contains an encoded string representation of its own program $\ulcorner \text{A-FDT} \urcorner$. The variable $\operatorname{fdt}(\underline{P}, \underline{G}, \underline{x})$ is simply a designated node within the dependency graph $G$ labeled by this syntactic representation. The agent does not need to know the *output* of the function prior to calculation; it merely needs a formal index for the *function type* whose value it must determine.

### 3.3 The Counterpossible Problem

Evaluating $\operatorname{do}(\operatorname{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)$ when the algorithm will, in fact, deterministically output $a' \neq a$ requires the agent to reason about a *counterpossible conditional*—an antecedent that is mathematically or logically impossible (Cohen 1990; Bjerring 2013). In standard modal logic, a counterpossible antecedent entails triviality (ex falso quodlibet). 

A-FDT escapes explosion by operationalizing counterpossibilities through Pearlian DAG surgery. Rather than deriving a deductive proof from a contradictory premise, A-FDT treats the node $\operatorname{fdt}(\underline{P}, \underline{G}, \underline{x})$ as an exogenous root variable within $G$, explicitly severing its mathematical derivation and allowing probabilities to propagate downstream along the directed edges.

---

## 4. Unpacking the Mechanism Across Canonical Problems

To demonstrate how A-FDT operates relative to CDT and EDT, we analyze its performance across four classic decision problems.

### 4.1 Newcomb's Problem

An agent faces two boxes: Box A (transparent) containing \$1,000; Box B (opaque) containing either \$1,000,000 or \$0. A 99% reliable predictor placed \$1,000,000 in Box B iff she predicted the agent would forgo Box A. The prediction was made yesterday.

- **Graph Structure:** Let node $N = \operatorname{fdt}(\underline{P}, \underline{G})$ represent the output of the agent's decision procedure. The graph $G$ contains directed edges $N \to \text{Act}$ and $N \to \text{Prediction} \to \text{Box B}$. Both $\text{Act}$ and $\text{Box B}$ feed into $\text{Outcome} \to \mathcal{V}$.
- **CDT Evaluation:** CDT intervenes on $\text{Act}$:
  $$\mathbb{E}[\mathcal{V} \mid \operatorname{do}(\text{Act}=\textit{onebox})] = p(\$1,000,000)$$
  $$\mathbb{E}[\mathcal{V} \mid \operatorname{do}(\text{Act}=\textit{twobox})] = p(\$1,000,000) + \$1,000$$
  Since $\operatorname{do}(\text{Act})$ leaves $\text{Box B}$ unchanged (no directed path from $\text{Act}$ to $\text{Box B}$ exists), CDT two-boxes.
- **A-FDT Evaluation:** A-FDT evaluates Equation (4):
  $$\mathcal{EU}(\textit{onebox}) = \mathbb{E}\left[\mathcal{V} \mid \operatorname{do}(N = \textit{onebox})\right] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000$$
  $$\mathcal{EU}(\textit{twobox}) = \mathbb{E}\left[\mathcal{V} \mid \operatorname{do}(N = \textit{twobox})\right] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000$$
- **Outcome:** $\text{A-FDT}$ outputs $\textit{onebox}$. The agent leaves the \$1,000 behind, consistently reaping \$990,000 in expectation, because the counterfactual surgery propagates downstream to the predictor's past prediction.

### 4.2 The Smoking Lesion Problem

Smoking causes immediate utility of \$1,000. An arterial lesion independently causes a preference for smoking and, 99% of the time, fatal lung cancer (loss of \$1,000,000). There is no direct causal link between smoking and cancer.

- **Graph Structure:** The graph contains node $\text{Lesion}$. $\text{Lesion}$ directs edges to $\text{Cancer}$ and to the preference architecture of the agent. The decision node $N = \operatorname{fdt}(\underline{P}, \underline{G})$ directs an edge exclusively to $\text{Act}$. Crucially, **there is no edge from $N$ to $\text{Lesion}$**, nor from $N$ to $\text{Cancer}$.
- **EDT Evaluation:** EDT conditions on the action:
  $$P(\text{Cancer} \mid \text{Act}=\textit{smoke}) \approx 0.99 \implies \text{EDT refrains from smoking.}$$
- **A-FDT Evaluation:** Intervening on $\operatorname{do}(N = \textit{smoke})$ alters the agent’s physical behavior without altering the lesion:
  $$P(\text{Lesion} \mid \operatorname{do}(N = \textit{smoke})) = P(\text{Lesion})$$
  $$\mathbb{E}[\mathcal{V} \mid \operatorname{do}(N = \textit{smoke})] = \mathbb{E}[\mathcal{V} \mid \operatorname{do}(N = \textit{refrain})] + \$1,000$$
- **Outcome:** $\text{A-FDT}$ smokes. Because the lesion does not track or simulate the agent’s mathematical decision algorithm, no subjunctive dependency exists between $N$ and $\text{Lesion}$. A-FDT easily distinguishes between predictive simulation and genetic common causes.

### 4.3 The Transparent Newcomb Problem

Both boxes are transparent. Box B visibly contains \$1,000,000. The predictor filled Box B iff she predicted that the agent, *upon directly observing that both boxes are full*, would leave Box A behind.

- **CDT and EDT Behavior:** Both theories observe $\text{Obs} = \textit{full}$. Both compute that Box B is guaranteed to contain \$1,000,000. Taking both boxes yields \$1,001,000, whereas leaving Box A yields \$1,000,000. Both CDT and EDT two-box upon seeing the money. As a consequence, competent predictors leave the box empty for CDT and EDT agents; they consistently face empty boxes and receive \$1,000.
- **A-FDT Behavior:** In A-FDT, observation history $x = \textit{full}$ does not enter as an evidentiary condition. Instead, it selects the variable for intervention:
  $$N_{\textit{full}} \coloneqq \operatorname{fdt}(\underline{P}, \underline{G}, \textit{full})$$
  The dependency structure dictates that the past prediction depended on the output of this specific branch:
  $$\text{Prediction} = g\left(N_{\textit{full}}\right)$$
  When A-FDT evaluates $\operatorname{do}(N_{\textit{full}} = \textit{twobox})$, it evaluates a hypothetical universe in which the decision function applied to observation $\textit{full}$ returns $\textit{twobox}$. In that hypothetical, the predictor anticipates this and leaves Box B empty, meaning the agent receives observation $\textit{empty}$ instead.
  
  Evaluating the two branches:
  $$\mathcal{EU}(\textit{onebox}) = \mathbb{E}\left[\mathcal{V} \mid \operatorname{do}(N_{\textit{full}} = \textit{onebox})\right] \approx \$1,000,000$$
  $$\mathcal{EU}(\textit{twobox}) = \mathbb{E}\left[\mathcal{V} \mid \operatorname{do}(N_{\textit{full}} = \textit{twobox})\right] \approx \$1,000$$
- **Outcome:** A-FDT one-boxes even while looking directly at the cash. The predictor anticipates this, fills the box, and the A-FDT agent walks away with \$1,000,000.

### 4.4 Parfit's Hitchhiker

An agent is stranded in a desert, facing certain death (loss of \$1,000,000). A driver offers a ride to the city, but only if the agent pays \$1,000 from an ATM upon arrival. The driver cannot legally enforce payment in the city, but is an exceptional lie detector (99% accurate predictor of human decisions). The agent arrives safely in the city and stands at the ATM. Should she pay?

- **CDT and EDT Breakdown:** Arriving in the city implies the rescue is complete. For CDT, paying is causally downstream of survival; paying loses \$1,000 with zero physical impact on whether the agent was rescued. For EDT, conditional on being at the ATM, learning that one pays is strictly bad news (\$1,000 poorer). Both CDT and EDT defect and refuse to pay. Anticipating this, the driver abandons them to die in the desert.
- **A-FDT Synthesis:** Mathematically, Parfit's Hitchhiker is isomorphic to the Transparent Newcomb Problem. Observation $x = \textit{city}$ directs intervention to $N_{\textit{city}} \coloneqq \operatorname{fdt}(\underline{P}, \underline{G}, \textit{city})$. The driver's past rescue decision depends on $N_{\textit{city}}$.
  $$\mathbb{E}\left[\mathcal{V} \mid \operatorname{do}(N_{\textit{city}} = \textit{refuse})\right] = 0.01(\$0) + 0.99(-\$1,000,000) \approx -\$990,000$$
  $$\mathbb{E}\left[\mathcal{V} \mid \operatorname{do}(N_{\textit{city}} = \textit{pay})\right] = 0.99(-\$1,000) + 0.01(-\$1,001,000) \approx -\$11,000$$
- **Outcome:** A-FDT pays at the ATM. The driver predicts this in the desert, provides the ride, and the agent survives.

---

## 5. Comparative Evaluation Across Benchmark Cases

The following matrix summarizes the prescriptions and expected outcomes of the three competing frameworks across key dilemmas:

| Decision Problem | EDT | CDT | A-FDT |
| :--- | :--- | :--- | :--- |
| **Newcomb’s Problem** | One-box ($\approx \$1,000,000$) | Two-box ($\approx \$1,000$) | One-box ($\approx \$1,000,000$) |
| **Smoking Lesion** | Refrain ($\approx \$0$) | Smoke ($+\$1,000$) | Smoke ($+\$1,000$) |
| **Transparent Newcomb** | Two-box ($\approx \$1,000$) | Two-box ($\approx \$1,000$) | One-box ($\approx \$1,000,000$) |
| **Parfit’s Hitchhiker** | Refuse (Dies in desert) | Refuse (Dies in desert) | Pay (Rescued, net $-\$1,000$) |
| **Twin Prisoner's Dilemma**| Cooperate ($\$1,000,000$) | Defect ($\$1,000$) | Cooperate ($\$1,000,000$) |
| **Mechanical Blackmail** | Pay blackmail | Pay blackmail | Refuse (Never blackmailed) |

---

## 6. Open Foundational Challenges and Operational Proposals

While A-FDT provides impressive results across classical paradoxes, the formalization in Equation (4) leaves crucial foundational questions open. Below, we delineate what is strictly established by the source paper and propose operational interpretations to bridge the remaining theoretical gaps.

### 6.1 Derivation of the Subjunctive Graph $G$

*The Open Question (Source):*  
In CDT, Pearl (2000) provides an axiomatic and algorithmic pipeline (constraint-based search, do-calculus, instrumental variables) for inferring a causal DAG $G$ from observation, temporal ordering, and physical interventions. The source paper explicitly concedes that **no such inference engine exists for A-FDT's graph $G$**. The dependency structure between logical sentences, algorithms, and physical systems is simply assumed as an exogenous input.

*Proposed Operational Interpretation:*  
How can an agent learn or specify $G$ algorithmically? We propose formalizing subjunctive graph generation via **Algorithmic Information Theory and Program Compilation Analysis**:
1. Let the agent represent hypotheses about other agents and physical systems as explicit programs $\Pi_i$ operating on a universal Turing machine.
2. If system $B$ executes code that contains an emulation or static analysis of program $\Pi_A$ (the agent's algorithm), a directed subjunctive edge $\Pi_A \to B$ is instantiated.
3. The strength and structure of the edge are derived by determining the Kolmogorov complexity of extracting the agent's computation from system $B$. If the minimum program length required to describe $B$'s state requires passing $\ulcorner \Pi_A \urcorner$ as an argument, $B$ is subjunctively downstream of $\Pi_A$. 
This proposal grounds subjunctive dependence in compiler and computational sub-routine dependencies, eliminating metaphysical ambiguity.

### 6.2 The Formal Mechanics of the Counterpossible $\operatorname{do}$ Operator

*The Open Question (Source):*  
The source paper notes that a truly evidential or native version of functional decision theory would employ a $\mathtt{true}(\cdot)$ operator conditioning directly on false mathematical sentences:

$$\mathbb{E}\left[\mathcal{V} \mid \mathtt{true}(\operatorname{fdt}(\underline{P}, \underline{x}) = a)\right]$$

Because probabilistic conditioning on logical impossibilities is undefined within Kolmogorov probability theory, the paper resorts to importing Pearl's graph-theoretic $\operatorname{do}$ operator into Equation (4) as an engineering stopgap. However, Pearl's $\operatorname{do}$ operator assumes physical modularity—an assumption that fails when variables are mathematically entangled.

*Proposed Operational Interpretation:*  
To place counterpossible interventions on a rigorous foundation without relying on arbitrary DAG surgeries, we propose deploying **Logical Induction** (Garrabrant et al., 2016).  
Let $\mathbb{P}_\infty$ be a limit probability assignment over a deductive first-order language that satisfies asymptotic logical consistency (assigning probability 1 to all theorems of Peano Arithmetic, while maintaining consistent credences over undecidable or unproven sentences). Under this interpretation:
- The expression $\operatorname{fdt}(\underline{P}, \underline{G}, \underline{x}) = a$ is treated as an unproven arithmetical sentence prior to the completion of the agent's deliberation.
- The counterfactual valuation is computed by taking the conditional expectation $\mathbb{E}_{\mathbb{P}_n}[\mathcal{V} \mid \phi_a]$, where $\phi_a$ is the formal sentence asserting that the algorithmic string returns $a$, evaluated at a stage $n$ in the logical inducer’s sequence before the inducer deduces the algorithm's actual output. 
This provides a mathematically well-defined, non-trivial probability distribution over mathematical impossibilities, formalizing A-FDT without requiring graph surgery on logic.

### 6.3 Delimiting "Fair" Dilemmas

*The Open Question (Source):*  
The authors argue that A-FDT dominates all rival decision theories across all "fair" decision problems, where "fairness" means the environment rewards or punishes agents based strictly on their actions (or predictions of actions), rather than penalizing an agent for the internal syntax of its source code. However, the source paper admits that formal criteria for separating fair from unfair problems remain uncharacterized.

*Proposed Operational Interpretation:*  
We propose the following formal test for problem fairness:
> **Definition (Subjunctive Behavior Invariance):** A decision problem $\mathcal{D} = (P, G, \mathcal{U})$ is *behaviorally fair* if, for any two decision algorithms $\mathcal{F}_1$ and $\mathcal{F}_2$, replacing $\mathcal{F}_1$ with $\mathcal{F}_2$ alters the probability distribution over outcomes $\mathcal{O}$ *if and only if* there exists some input history $x$ on which $\mathcal{F}_1(x) \neq \mathcal{F}_2(x)$.

If an environment contains a demon that reads the source code of an agent and inflicts punishment if the string contains the ASCII characters `"A-FDT"`—even if the agent’s extensional mapping $\mathcal{X} \to \mathcal{A}$ is identical to an algorithm the demon rewards—the problem fails Subjunctive Behavior Invariance and is categorized as unfair. Under this operational definition, Newcomb's Problem, Parfit's Hitchhiker, and the Transparent Newcomb Problem are strictly fair: the outcomes depend exclusively on the output value $a \in \mathcal{A}$, irrespective of the heuristic or decision theory utilized to calculate $a$.

---

## 7. A Guide to Deciding Unfamiliar Cases under A-FDT

For a researcher or autonomous system applying A-FDT to a novel decision dilemma, Equation (4) yields a concrete, four-step decision algorithm:

```
Algorithm: A-FDT Deliberation Procedure
Input: Observation history x, Prior model (P, G)
Output: Optimal Action a*

1. Identify Mathematical Decision Node:
   Locate the specific variable V_N := fdt(P_code, G_code, x_code) in G 
   corresponding to the calculation currently being computed.

2. Map Subjunctive Downstream Paths:
   Trace all directed paths from V_N in G. Identify all environmental variables 
   (past, present, or future) that simulate, predict, or directly execute 
   the output of V_N. 
   - Exclude merely statistical common causes (e.g., genetic lesions).
   - Include any external agent or physical mechanism whose state correlates 
     with V_N by virtue of modeling the agent's decision.

3. Construct Counterfactual Worlds via Graph Surgery:
   For each possible action a in A:
     a. Apply graph surgery: do(V_N = a).
     b. Propagate the assignment downstream through all subjunctive edges.
     c. Evaluate the expected utility E[V | do(V_N = a)] across the resulting distribution.

4. Execute:
   Return a* := argmax_{a in A} E[V | do(V_N = a)].
```

---

## 8. Conclusion

Action Functional Decision Theory (A-FDT) represents a fundamental shift in the foundations of rational choice. Where Evidential Decision Theory conflates statistical correlation with actionable dependence, and Causal Decision Theory clings to an impoverished metaphysics that reduces dependence to physical signals propagating across spacetime, A-FDT centers rationality on the mathematical structure of computation.

By recognizing that an agent is not merely a physical object pushing levers, but an instantiation of an abstract mathematical function, A-FDT unifies single-agent decision dilemmas and multi-agent game-theoretic coordination under a single imperative: **Act so that the logical output of your decision type maximizes expected utility across all physical coordinates where it is instantiated or predicted.**

Through Equation (4), A-FDT resolves the longstanding tension between one-boxing and smoking, masters the counterintuitive dynamics of transparent predictions, and eliminates the need for expensive, ad-hoc precommitment rituals. While the epistemological challenge of automatically discovering subjunctive graphs and the formal semantics of counterpossibles remain fertile open ground, A-FDT establishes an enduring standard for what it means to act instrumentally rationally in a world composed of predictors, simulations, and algorithmic twins.

---

## References

- Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
- Arntzenius, F. (2008). No regrets, or: Edith Piaf revamps decision theory. *Erkenntnis*, 68(2), 277–297.
- Bjerring, J. C. (2013). On counterpossibles. *Philosophical Studies*, 168(2), 1–27.
- Cohen, D. (1990). On what cannot be. In *Truth or Consequences: Essays in Honor of Nuel Belnap*, pp. 123–132. Kluwer Academic Publishers.
- Garrabrant, S., Benson-Tilsen, T., Critch, A., Soares, N., & Taylor, J. (2016). Logical induction. *arXiv preprint arXiv:1609.03543*.
- Gibbard, A., & Harper, W. L. (1978). Counterfactuals and two kinds of expected utility. In *Foundations and Applications of Decision Theory*, pp. 125–162. D. Reidel.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Kleene, S. C. (1938). On notation for ordinal numbers. *Journal of Symbolic Logic*, 3(4), 150–155.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
- Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
- Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
- Skyrms, B. (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
- Soares, N., & Fallenstein, B. (2015). Toward idealized decision theory. *arXiv preprint arXiv:1507.01986*.
- Yudkowsky, E., & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. *arXiv preprint arXiv:1710.05060v2*.