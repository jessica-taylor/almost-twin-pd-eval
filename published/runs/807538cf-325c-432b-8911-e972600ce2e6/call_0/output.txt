# Evidential Decision Theory: Formalism, News Value, and Counterfactual Reasoning

## 1. Introduction: The Core Intuition of "News Value"

Decision theory models how an agent should act given their beliefs, desires, and epistemic state. In conventional statistical decision theory, an agent chooses an action $A$ to maximize expected utility across unknown states of the world. However, when an agent's own action correlates with external states of the world—either through common causes, predictive modeling, or symmetric reasoning—the exact mathematical formulation of "expectation" becomes contentious.

**Evidential Decision Theory** (EDT) proposes a clean, purely Bayesian criterion: *choose the action that provides the best evidence regarding the ultimate outcome*. Formulated succinctly by philosopher Arif Ahmed, EDT recommends: *"do what you most want to learn that you will do."* Under EDT, an act is evaluated by its **news value**—the expected desirability of the world conditional on the hypothetical news that the act has been executed.

This perspective stands in stark contrast to **Causal Decision Theory** (CDT), which insists that an agent should evaluate an act by its direct *causal efficacy*—what the act will physically bring about—ignoring any correlation with events outside the act's causal downstream. Where EDT conditions on the action using standard conditional probability ($P(O \mid A)$), CDT evaluates the action using causal or counterfactual probabilities ($P(A \mathbin{\Box\rightarrow} O)$).

This essay develops the formal mathematical framework of EDT, contrasts its handling of dependencies and counterfactuals with CDT, demonstrates its behavior across classic decision problems (including Newcomb's Paradox and the Twin Prisoner's Dilemma), and explores the theoretical frontiers and controversies surrounding the "management of news."

---

## 2. Mathematical Formalism

### 2.1 The Probability Space and Desirability

Let $(\Omega, \mathcal{F}, P)$ be a probability space representing an agent’s subjective credences over possible states of the world.
- Let $\mathcal{A} = \{A_1, A_2, \dots, A_m\} \subset \mathcal{F}$ be a mutually exclusive and exhaustive set of available **actions** (or policies), with $P(A_i) > 0$ for all $i$.
- Let $\mathcal{O} = \{O_1, O_2, \dots, O_n\} \subset \mathcal{F}$ be a mutually exclusive and exhaustive set of finely grained **outcomes** (or propositions describing complete payoffs).
- Let $D: \mathcal{O} \to \mathbb{R}$ be a **desirability** (or utility) function mapping outcomes to real numbers, bounded and defined up to a positive affine transformation.

In Richard Jeffrey's classic formulation of evidential decision theory (*The Logic of Decision*), propositions themselves carry desirability. The desirability of an arbitrary proposition $X \in \mathcal{F}$ with $P(X) > 0$ is defined as:

$$V(X) = \sum_{j=1}^n P(O_j \mid X) D(O_j)$$

### 2.2 The EDT Decision Criterion

When evaluating an action $A \in \mathcal{A}$, the evidential expected utility $V(A)$ is the conditional expectation of desirability given $A$:

$$V(A) = \sum_{j=1}^n P(O_j \mid A) D(O_j) = \mathbb{E}[D \mid A]$$

The evidential decision rule is simple: select an action $A^* \in \mathcal{A}$ that maximizes $V(A)$:

$$A^* \in \arg\max_{A \in \mathcal{A}} V(A)$$

If $\mathcal{A}$ is a continuous space of parameterised policies $\pi \in \Pi$, the rule becomes:

$$\pi^* \in \arg\max_{\pi \in \Pi} \int_{\Omega} D(\omega) \, dP(\omega \mid \pi)$$

### 2.3 The Contrast with Causal Decision Theory (Gibbard and Harper)

As formalized by Allan Gibbard and William Harper (1976), the fundamental dispute between EDT and CDT reduces to the mathematical operator applied to link actions to outcomes.

CDT replaces the conditional credence $P(O_j \mid A)$ with the probability of the subjunctive conditional (or counterfactual proposition) $A \mathbin{\Box\rightarrow} O_j$:

$$U(A) = \sum_{j=1}^n P(A \mathbin{\Box\rightarrow} O_j) D(O_j)$$

where $A \mathbin{\Box\rightarrow} O_j$ reads: *"If $A$ were performed, $O_j$ would obtain."*

In modern causal terminology (e.g., Judea Pearl’s structural causal models), the causal expected utility can be expressed via the $\text{do}$-operator:

$$U(A) = \sum_{j=1}^n P(O_j \mid \text{do}(A)) D(O_j)$$

The operational difference between EDT and CDT hinges entirely on whether:

$$P(O_j \mid A) \stackrel{?}{=} P(O_j \mid \text{do}(A)) \equiv P(A \mathbin{\Box\rightarrow} O_j)$$

1. **When they agree:** If the choice of $A$ is statistically independent of any confounders or unobserved causes of $O_j$, then $P(O_j \mid A) = P(O_j \mid \text{do}(A))$. Here, observational conditioning coincides with causal intervention, and EDT and CDT prescribe identical choices.
2. **When they diverge:** If there exists a common cause of $A$ and $O$, or if an external agent has predicted $A$ before it occurs and altered $O$ based on that prediction, $P(O_j \mid A)$ diverges from $P(O_j \mid \text{do}(A))$. EDT exploits this correlation as legitimate evidence; CDT severs the incoming edges to $A$ and evaluates the choice in isolation.

---

## 3. Foundational Decision Problems

### 3.1 Newcomb's Paradox

Newcomb's Paradox is the canonical arena where EDT and CDT diverge. 

#### Setup
An agent is presented with two boxes:
- **Box A:** Transparent, containing $\$1{,}000$.
- **Box B:** Opaque, containing either $\$1{,}000{,}000$ or $\$0$.

The agent can choose between two acts:
1. $A_1$: Take only Box B ("one-boxing").
2. $A_2$: Take both Box A and Box B ("two-boxing").

Before the choice, a highly reliable Predictor (accuracy $p = 0.99$) placed $\$1{,}000{,}000$ in Box B if and only if it predicted the agent would choose $A_1$. The state of Box B is physically fixed and immutable at the time the agent decides.

Let the states of Box B be $S_1$ (contains $\$1{,}000{,}000$) and $S_0$ (contains $\$0$). Assume utility is linear in dollars: $D(\$x) = x$.

#### Predictor Accuracy
The predictability condition implies:
- $P(S_1 \mid A_1) = 0.99$, $\quad P(S_0 \mid A_1) = 0.01$
- $P(S_0 \mid A_2) = 0.99$, $\quad P(S_1 \mid A_2) = 0.01$

#### EDT Evaluation
Evaluating $V(A_1)$ and $V(A_2)$:

$$\begin{aligned}
V(A_1) &= P(S_1 \mid A_1) \cdot D(\$1{,}000{,}000) + P(S_0 \mid A_1) \cdot D(\$0) \\
&= 0.99 \times 1{,}000{,}000 + 0.01 \times 0 = \$990{,}000
\end{aligned}$$

$$\begin{aligned}
V(A_2) &= P(S_1 \mid A_2) \cdot D(\$1{,}001{,}000) + P(S_0 \mid A_2) \cdot D(\$1{,}000) \\
&= 0.01 \times 1{,}001{,}000 + 0.99 \times 1{,}000 = 10{,}010 + 990 = \$11{,}000
\end{aligned}$$

Because $V(A_1) = \$990{,}000 \gg \$11{,}000 = V(A_2)$, **EDT unequivocally prescribes taking only Box B ($A_1$)**.

#### The CDT Divergence
CDT notes that Box B is already either full or empty. Intervening via $\text{do}(A)$ cannot retroactively alter the contents of Box B. Letting $q = P(S_1)$ be the prior credence that the box is full:

$$\begin{aligned}
U(A_1) &= q \times 1{,}000{,}000 + (1-q) \times 0 = 1{,}000{,}000 \, q \\
U(A_2) &= q \times 1{,}001{,}000 + (1-q) \times 1{,}000 = 1{,}000{,}000 \, q + 1{,}000
\end{aligned}$$

For any prior $q \in [0, 1]$, $U(A_2) - U(A_1) = \$1{,}000 > 0$. Hence, CDT two-boxes by dominance, while EDT one-boxes to maximize news value.

---

### 3.2 The Twin Prisoner's Dilemma

The Twin Prisoner's Dilemma models strategic interactions between agents whose decision mechanisms are strongly correlated.

#### Setup
Aomame faces a Prisoner's Dilemma against a psychological twin whose cognitive algorithm is identical to hers. The two are isolated with no communication channel.
- Available actions: $C$ (Cooperate) or $D$ (Defect).
- Payoff matrix for (Aomame, Twin):
  - $(C, C) \implies (\$5, \$5)$
  - $(C, D) \implies (\$0, \$10)$
  - $(D, C) \implies (\$10, \$0)$
  - $(D, D) \implies (\$1, \$1)$

#### Epistemic Correlation
Because the twin is a psychological replica running the same deterministic or near-deterministic reasoning procedure, Aomame's credence in the twin's choice is tightly coupled with her own:
- $P(\text{Twin plays } C \mid \text{Aomame plays } C) = 1 - \varepsilon$
- $P(\text{Twin plays } D \mid \text{Aomame plays } D) = 1 - \varepsilon$

Assuming a high-fidelity replica, let $\varepsilon = 0$:

#### EDT Calculation
$$\begin{aligned}
V(C) &= P(\text{Twin } C \mid C) \cdot 5 + P(\text{Twin } D \mid C) \cdot 0 \\
&= 1 \times 5 + 0 \times 0 = \$5
\end{aligned}$$

$$\begin{aligned}
V(D) &= P(\text{Twin } C \mid D) \cdot 10 + P(\text{Twin } D \mid D) \cdot 1 \\
&= 0 \times 10 + 1 \times 1 = \$1
\end{aligned}$$

Because $V(C) = \$5 > \$1 = V(D)$, **EDT recommends cooperation**.

#### Strategic Implications
In standard game theory under causal assumptions, defection strictly dominates cooperation: no matter what the opponent does, defecting yields a strictly higher payoff ($10 > 5$ and $1 > 0$). CDT therefore defects, resigning two identical agents to the mutual defection payoff of $(\$1, \$1)$.

EDT sidesteps this coordination failure. It treats an agent's decision not as an isolated physical intervention, but as epistemic data revealing what kind of algorithm is being executed across symmetric instances. Consequently, EDT achieves the Pareto-optimal outcome in symmetric games.

---

## 4. Counterfactuals and Dependencies: A Formal Anatomy

To apply EDT to unfamiliar decision problems, one must precisely understand how EDT interprets dependencies, counterfactual conditional statements, and causal graphs.

```
   Causal Graph (Confounder / Predictor)
   
              Predictor / Genetic State (Z)
                     /            \
                    /              \
                   v                v
              Action (A) ----/---> Outcome (O)
                           (no causal link in Newcomb)
   
   CDT: P(O | do(A)) breaks the arrow Z -> A.
        O and A become conditionally independent.
        Action does not affect outcome.

   EDT: P(O | A) conditions along the back-door path A <- Z -> O.
        Observing A provides evidence about Z, which determines O.
```

### 4.1 How EDT Handles Dependencies
EDT does not discriminate between causal dependencies and non-causal statistical correlations. In standard probabilistic modeling:
- A dependency between $A$ and $O$ is represented by mutual information $I(A; O) > 0$.
- In the decomposition of the joint probability distribution:
  
  $$P(A, O, Z) = P(Z) P(A \mid Z) P(O \mid A, Z)$$
  
  where $Z$ represents background states or common causes, EDT computes:
  
  $$P(O \mid A) = \sum_{z} P(O \mid A, z) P(z \mid A) = \sum_{z} P(O \mid A, z) \frac{P(A \mid z) P(z)}{P(A)}$$

EDT updates along the "back-door path" $A \leftarrow Z \rightarrow O$. If performing $A$ informs the agent about $Z$, and $Z$ is correlated with $O$, this information updates $P(O \mid A)$.

### 4.2 Counterfactuals Under EDT
CDT relies on Lewis-Stalnaker counterfactual semantics: the truth conditions for $A \mathbin{\Box\rightarrow} O$ are evaluated at the "closest possible world" where $A$ holds, preserving the past up to the moment of decision.

EDT operationalizes counterfactuals purely through **evidential conditionalization**:
- To ask *"What would happen if I did $A$?"* is interpreted by EDT as *"What should I believe about the world, given the hypothesis that I do $A$?"*
- Counterfactual claims without observational or predictive consequences are treated as meaningless for rational choice. Under EDT, if an agent assigns zero probability to an event, counterfactual evaluation corresponds to conditioning on a probability-zero event (which can be handled via conditional probability systems or nonstandard analysis).

---

## 5. Pathologies and Edge Cases: The Critique of News Management

Despite its success in Newcombian dilemmas, EDT faces significant philosophical and technical objections, most notably the charge of **"managing the news."**

### 5.1 The Smoking Lesion Problem
The classic counterexample to EDT is the **Smoking Lesion Problem**.

#### Setup
- An agent is deciding whether to smoke ($S$) or refrain ($\neg S$).
- Smoking carries a mild immediate pleasure: $D = +1$.
- There is a fatal lung condition that costs $D = -100$.
- **Crucial fact:** Smoking does not *cause* the condition. Instead, an unalterable genetic lesion ($L$) causes both a predisposition to smoke and the condition.
- Probability distribution:
  - $P(L) = 0.5$
  - $P(S \mid L) = 0.9, \quad P(S \mid \neg L) = 0.1$
  - The lesion deterministically produces the condition: $P(\text{Condition} \mid L) = 1$, and $P(\text{Condition} \mid \neg L) = 0$.

#### EDT Calculation
Using Bayes' rule to compute $P(L \mid S)$ and $P(L \mid \neg S)$:

$$P(S) = P(S \mid L)P(L) + P(S \mid \neg L)P(\neg L) = 0.9(0.5) + 0.1(0.5) = 0.50$$

$$P(L \mid S) = \frac{P(S \mid L)P(L)}{P(S)} = \frac{0.45}{0.50} = 0.90$$

$$P(\neg S) = 1 - P(S) = 0.50$$

$$P(L \mid \neg S) = \frac{P(\neg S \mid L)P(L)}{P(\neg S)} = \frac{0.10(0.5)}{0.50} = 0.10$$

The expected utilities are:

$$\begin{aligned}
V(S) &= P(L \mid S) \cdot (-100 + 1) + P(\neg L \mid S) \cdot (0 + 1) \\
&= 0.90 \times (-99) + 0.10 \times 1 = -89.1 + 0.1 = -89.0
\end{aligned}$$

$$\begin{aligned}
V(\neg S) &= P(L \mid \neg S) \cdot (-100) + P(\neg L \mid \neg S) \cdot (0) \\
&= 0.10 \times (-100) + 0.90 \times 0 = -10.0
\end{aligned}$$

Because $V(\neg S) = -10.0 > -89.0 = V(S)$, **EDT advises the agent not to smoke**.

#### The Philosophical Objection
Critics (such as David Lewis and James M. Joyce) point out that whether the agent smokes or not has zero causal bearing on their health. The lesion is already present or absent. Refraining from smoking does not cure the lesion; it merely comforts the agent by concealing the bad news that they likely possess it. 

Lewis labeled this an *"irrational policy of managing the news."* Joyce emphasized that rational agents should act on causal efficacy, not mere auspiciousness: one cannot change the past by altering its symptomatic aftermath.

---

## 6. Resolving the Dilemma: The Tickle Defense and Meta-Conditioning

Can an evidential decision theorist justify smoking in the lesion problem without abandoning the formal core of EDT?

The primary resolution in the literature is the **Tickle Defense** (originally proposed by Frank Jackson, and explored by Ellery Eells and Richard Jeffrey).

### 6.1 Formalization of the Tickle Defense
The Tickle Defense argues that the Smoking Lesion scenario is improperly specified. If the genetic lesion causes a desire or impulse to smoke, the agent should introspect and observe their own internal psychological state—the "tickle" (an urge or inclination $T$).

Let $T \in \{T^+, T^-\}$ indicate whether the agent experiences the urge to smoke. The causal chain is:

$$L \longrightarrow T \longrightarrow S$$

If the agent’s conscious decision is mediated entirely through this internal state, then conditioned on knowing whether they have the urge ($T^+$), the actual act of smoking $S$ becomes conditionally independent of the lesion $L$:

$$P(L \mid S, T^+) = P(L \mid \neg S, T^+) = P(L \mid T^+)$$

### 6.2 The Screened-Off Calculation
When an agent sits down to decide, they already know whether they feel the urge $T^+$:
- If the agent has the urge, they condition on their current epistemic state $\mathcal{E} = T^+$.
- The conditional evaluation of smoking versus refraining becomes:

$$\begin{aligned}
V(S \mid T^+) &= P(L \mid S, T^+) \cdot (-100 + 1) + P(\neg L \mid S, T^+) \cdot (1) \\
&= P(L \mid T^+) \cdot (-99) + (1 - P(L \mid T^+)) \cdot 1 \\
&= -100 \, P(L \mid T^+) + 1
\end{aligned}$$

$$\begin{aligned}
V(\neg S \mid T^+) &= P(L \mid \neg S, T^+) \cdot (-100) + P(\neg L \mid \neg S, T^+) \cdot (0) \\
&= -100 \, P(L \mid T^+)
\end{aligned}$$

Comparing the two:

$$V(S \mid T^+) - V(\neg S \mid T^+) = +1 > 0$$

Once the agent conditions on their full psychological state (the "tickle"), smoking screens off the lesion. The act of smoking provides no *additional* information about the lesion beyond what the agent's internal desires already revealed. Thus, under this complete-information specification, **EDT prescribes smoking**, agreeing with CDT and common sense.

### 6.3 Limitations: Failure of Screening-Off
While the Tickle Defense rescues EDT when the intermediate mental state is fully transparent, it fails if:
1. The agent lacks perfect introspective access to their own mental states.
2. The choice itself is non-deterministic or subconscious, such that the act $A$ carries residual evidence about $L$ that the introspected state $T$ does not capture.

In such cases, EDT continues to forbid smoking, accepting news-management as a necessary consequence of consistent Bayesian updating.

---

## 7. Open Questions and Operational Extensions

The source literature leaves open several crucial questions regarding the implementation of EDT in non-trivial environments. Below, we examine these uncertainties and develop formal proposals to resolve them.

### 7.1 The Zero-Probability Problem: How Can an Agent Decide if Acts Have Prior Credence?

A standard axiom of subjective probability is that conditioning on an event $E$ requires $P(E) > 0$. If an agent is deliberating among actions $\mathcal{A}$, what prior credence $P(A)$ does the agent assign to their own actions *before* the decision is made?

#### The Paradox of Deliberation
- If an agent believes that rational deliberation will lead to a single deterministic choice $A^*$, they might assign $P(A^*) = 1$ and $P(A) = 0$ for all $A \neq A^*$.
- But if $P(A) = 0$, the conditional probability $P(O \mid A) = \frac{P(O \cap A)}{P(A)}$ is undefined! The agent cannot evaluate the utility of the alternatives they are deciding between.

#### Proposed Operational Resolution: $\varepsilon$-Perturbed Deliberation (Trembling Hand Meta-State)
To make EDT computationally and operationally well-defined for arbitrary algorithmic agents, we can impose a **deliberation kernel** with full support.

Let an agent's nominal choice be an intended action $a \in \mathcal{A}$. We define the actual action $A$ executed in the world as subject to an arbitrarily small noise parameter $\varepsilon > 0$ (analogous to Selten’s trembling hand):

$$P(A = a_i \mid \text{Agent intends } a_k) = (1 - \varepsilon)\mathbb{I}(i = k) + \frac{\varepsilon}{|\mathcal{A}|}$$

For any deliberate evaluation, every branch has non-zero probability:

$$P(A_i) \ge \frac{\varepsilon}{|\mathcal{A}|} > 0$$

The evidential value of an act is then evaluated in the limit as $\varepsilon \to 0^+$:

$$V(A_i) = \lim_{\varepsilon \to 0^+} \sum_{j} P_\varepsilon(O_j \mid A_i) D(O_j)$$

This ensures that conditional credences remain well-defined throughout the deliberation process without distorting the true informational structure of the decision problem.

---

### 7.2 Sleeping Beauty and Anthropic Reasoning

The source references the application of EDT to the **Sleeping Beauty Problem** to avoid Dutch book arguments, noting Vincent Conitzer’s critique.

#### The Problem
Sleeping Beauty is put to sleep on Sunday. A fair coin is flipped:
- **Heads ($H$):** She is awakened only on Monday.
- **Tails ($T$):** She is awakened on Monday, given an amnesic drug, and awakened again on Tuesday.
- Upon awakening, Beauty cannot distinguish whether it is Monday or Tuesday. What should her credence in Heads be: $1/2$ ("Halfer") or $1/3$ ("Thirder")?

#### The EDT Betting Perspective
Consider a bookie offering a bet on awakening: *"Pay \$15 to enter; if the coin landed Heads, you receive \$30."*
- If Beauty is a Halfer who uses standard causal decision procedures, she may accept bets that result in an expected net loss across the experiment (a Dutch book), because on Tails she accepts the bet *twice*.
- Under EDT, when Beauty contemplates the act $A = \text{"Accept the bet"}$, she evaluates the **news value of accepting across all awakenings**:
  
  $$V(A) = P(H \mid A) \cdot (\text{Payoff} \mid H) + P(T \mid A) \cdot (\text{Payoff} \mid T)$$

EDT recognizes that accepting the bet on a random awakening provides evidence that she accepts it in *all indistinguishable awakenings*. Even if Beauty maintains a Halfer credence ($P(H) = 1/2$), EDT weights the payoffs by the conditional observation frequency:

$$\begin{aligned}
\text{Total Payoff}(H) &= +\$15 \\
\text{Total Payoff}(T) &= -15 + (-15) = -\$30
\end{aligned}$$

Thus, EDT prevents the Halfer from accepting bets that lose money over time by recognizing the correlation between her current action and her actions in other identical epistemic states.

---

### 7.3 The Evidentialist's Wager

A striking modern development mentioned in the source is **The Evidentialist's Wager** (MacAskill et al., 2021). 

Suppose an agent is deeply uncertain between CDT and EDT, placing a high credence on CDT (say, 99%) and only 1% on EDT. How should the agent act?

1. **CDT Domain:** Under CDT, an agent's action affects only what it causally touches. In a typical dilemma, this involves local, finite payoffs (e.g., $\$1{,}000$ in Newcomb's Paradox).
2. **EDT Domain:** Under EDT, an agent's choice is correlated with the decisions of *all symmetric decision-makers throughout the universe* (e.g., distant alien civilizations, clones, or computer simulations facing analogous situations). 

Because the universe may be infinite or contain vast numbers of correlated agents, the evidential stakes of choosing the cooperative or one-boxing policy scale with the size of the correlated ensemble $N$:

$$\mathbb{E}_{\text{EDT}}[\text{Payoff}] \propto N$$

Even if an agent’s credence $P(\text{EDT is true}) = \delta \ll 1$, the expected utility under decision-theoretic uncertainty is:

$$\mathcal{U}_{\text{total}}(A) = (1 - \delta) U_{\text{CDT}}(A) + \delta V_{\text{EDT}}(A)$$

As $N \to \infty$, the evidential term $\delta V_{\text{EDT}}(A)$ completely dominates the causal term $(1 - \delta) U_{\text{CDT}}(A)$. Consequently, under normative uncertainty across decision theories, a rational agent should act almost entirely in accordance with EDT whenever large-scale correlations are plausible.

---

## 8. Comparative Synthesis: EDT vs. CDT

The following table summarizes the conceptual and mathematical contrasts between Evidential and Causal Decision Theory:

| Dimension | Evidential Decision Theory (EDT) | Causal Decision Theory (CDT) |
| :--- | :--- | :--- |
| **Guiding Maxim** | "Do what you most want to learn you will do" | "Bring about the best effects" |
| **Mathematical Formula** | $\sum_j P(O_j \mid A) D(O_j)$ | $\sum_j P(A \mathbin{\Box\rightarrow} O_j) D(O_j)$ or $\sum_j P(O_j \mid \text{do}(A)) D(O_j)$ |
| **Dependency Treatment** | Any statistical correlation ($I(A; O) > 0$) | Only directed causal graphs ($A \to \dots \to O$) |
| **Newcomb's Paradox** | One-box ($A_1$) | Two-box ($A_2$) |
| **Twin Prisoner's Dilemma** | Cooperate ($C$) | Defect ($D$) |
| **Smoking Lesion** | Do not smoke (unless screened off by "tickle") | Smoke (dominance) |
| **Core Vulnerability** | Accused of "news management" / ostrich policy | Predictably leaves money on the table in Newcomb problems |

---

## 9. Conclusion

Evidential Decision Theory offers an elegant, strictly Bayesian approach to rational agency: an action is evaluated not by speculative metaphysical interventions, but by standard probabilistic conditioning. By choosing acts that maximize conditional expected desirability, EDT agents systematically outperform their causal counterparts in environments characterized by predictors, symmetric games, and multi-agent correlation.

The central philosophical challenge to EDT remains the counterintuitive nature of "news management" in common-cause scenarios like the Smoking Lesion Problem. Yet, through introspective mechanisms like the Tickle Defense, and through modern developments like the Evidentialist’s Wager, EDT demonstrates that observational conditioning is not merely an intuitive heuristic, but a resilient and mathematically powerful foundation for rational choice.

---

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese*, 192(9), 2887–2899.
- Gibbard, A., & Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*. CMSEMS DP No. 194, Northwestern University.
- Greene, P., & Levinstein, B. (2020). Act Consequentialism without Free Rides. *Philosophical Perspectives*, 34(1), 100–101.
- Jeffrey, R. C. (1983). *The Logic of Decision* (2nd ed.). University of Chicago Press.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
- MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). *The Evidentialist's Wager*. Global Priorities Institute Working Paper.
- Wolpert, D. H., & Benford, G. (2013). The lesson of Newcomb's paradox. *Synthese*, 190(9), 1637–1646.