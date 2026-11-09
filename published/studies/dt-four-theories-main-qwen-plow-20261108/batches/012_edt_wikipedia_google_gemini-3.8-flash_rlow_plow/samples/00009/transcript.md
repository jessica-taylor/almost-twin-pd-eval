# 012_edt_wikipedia_google_gemini-3.8-flash_rlow_plow / 00009

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/a804554c-f3db-4684-917f-6038d89576c0/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/a804554c-f3db-4684-917f-6038d89576c0/call_0/response.raw) · finish: `stop`

### Visible response

````text
# The Logic of News Value: A Formal and Philosophical Exposition of Evidential Decision Theory

## 1. Introduction

Decision theory asks a deceptively simple question: when an agent faces a choice among mutually exclusive actions, what criterion identifies the rational choice? The classical Bayesian answer—championed in various forms by Frank Ramsey, Leonard Savage, and Richard Jeffrey—evaluates each candidate action by its expected utility. Yet beneath this consensus lies a fundamental schism regarding how that expectation must be formed.

Consider the intuitive directive: **"Choose the action that you would be happiest to learn that you have taken."** This principle defines **Evidential Decision Theory** (EDT). Formalized in the philosophical literature by Richard Jeffrey (1965) and analyzed contrastively by Allan Gibbard and William Harper (1976), EDT holds that the normative value of an action equals its *news value*—the conditional expectation of utility given the hypothesis that the action is performed.

To critics like David Lewis (1981) and James M. Joyce (1999), this directive commits an elementary fallacy: confusing correlation with causation. Lewis famously dismissed EDT as advising an irrational policy of "managing the news," arguing that rational deliberation must track what an action will *causally bring about*, not what it happens to *indicate*. This critique gave rise to Causal Decision Theory (CDT), which evaluates acts via counterfactual conditionals or causal interventions.

Nevertheless, EDT remains a formidable framework. In scenarios featuring correlated agents, predictive adversaries, or unobserved common causes, EDT achieves outcomes that CDT notoriously forfeits. This essay presents an account of Evidential Decision Theory: its mathematical formalization, its philosophical foundations, its operational application to classic dilemmas, its theoretical fault lines, and its broader implications for decision-making agents.

---

## 2. Mathematical Formalization

### 2.1 The Probability Space and Basic Objects

Let $(\Omega, \mathcal{F}, P)$ be a probability space representing an agent's subjective credences over possible states of the world and their outcomes:

- **Action space:** Let $\mathcal{A} = \{A_1, A_2, \dots, A_n\}$ be a finite partition of events in $\mathcal{F}$, where each $A_i$ represents the agent performing a specific act. We require $P(A_i) > 0$ for all $A_i \in \mathcal{A}$ to ensure conditional probabilities are well-defined.
- **Outcome partition:** Let $\mathcal{O} = \{O_1, O_2, \dots, O_m\}$ be a partition of $\mathcal{F}$ representing mutually exclusive and exhaustive ultimate outcomes.
- **Desirability/Utility function:** Let $D: \mathcal{O} \to \mathbb{R}$ assign a real-valued utility (or desirability) $D(O_j)$ to each outcome $O_j$.

### 2.2 The Evidential Value Operator

The evidential value (often termed the *news value* or *desirability*) of an act $A \in \mathcal{A}$, denoted $V(A)$, is defined as the mathematical expectation of utility conditional on the event that $A$ is realized:

$$V(A) \coloneqq \mathbb{E}_P[D \mid A] = \sum_{j=1}^m P(O_j \mid A) D(O_j)$$

where $P(O_j \mid A)$ is standard Kolmogorov conditioning:

$$P(O_j \mid A) = \frac{P(O_j \cap A)}{P(A)}$$

The decision rule of EDT is:

$$A^* = \arg\max_{A \in \mathcal{A}} V(A)$$

If multiple actions maximize $V(A)$, the agent is indifferent among them.

### 2.3 Contrast with Causal Decision Theory (CDT)

To appreciate the distinct mechanics of EDT, contrast $V(A)$ with the formulation of Causal Decision Theory introduced by Gibbard and Harper (1976). Let $A \mathrel{\Box\kern-1.5pt\rightarrow} O_j$ denote the counterfactual proposition: *"If action $A$ were performed, outcome $O_j$ would obtain."* CDT evaluates an act by its causal expected utility, $U(A)$:

$$U(A) \coloneqq \sum_{j=1}^m P(A \mathrel{\Box\kern-1.5pt\rightarrow} O_j) D(O_j)$$

Alternatively, using the language of modern graphical causal models (Pearl, 2000), CDT replaces conditional observation with Pearl's $\operatorname{do}$-operator:

$$U_{\text{causal}}(A) = \sum_{j=1}^m P(O_j \mid \operatorname{do}(A)) D(O_j)$$

The divergence between EDT and CDT reduces to the mathematical wedge between observational conditioning and counterfactual or interventional conditioning:

$$P(O_j \mid A) \neq P(A \mathrel{\Box\kern-1.5pt\rightarrow} O_j) \quad \Longleftrightarrow \quad P(O_j \mid A) \neq P(O_j \mid \operatorname{do}(A))$$

When an action $A$ shares a common latent cause with an outcome state, or when another agent possesses predictive information about $A$ prior to its execution, the conditional distribution $P(\cdot \mid A)$ updates on the informational payload of $A$, whereas $P(\cdot \mid \operatorname{do}(A))$ severs all incoming causal edges to $A$, holding pre-existing conditions fixed.

---

## 3. Foundational Paradigms

### 3.1 Newcomb's Paradox

Newcomb's Paradox (formulated by William Newcomb and popularized by Robert Nozick) serves as the primary battleground between EDT and CDT.

#### Specification
- An agent faces two boxes:
  - **Box A:** Transparent, containing $\$1,000$.
  - **Box B:** Opaque, containing either $\$1,000,000$ or $\$0$.
- **Actions:** $\mathcal{A} = \{A_1, A_2\}$, where:
  - $A_1$: Take only Box B ("one-boxing").
  - $A_2$: Take both Box A and Box B ("two-boxing").
- **Background:** A powerful Predictor, possessing historical accuracy $p \in (0.5, 1]$, has already placed the money:
  - If the Predictor predicted $A_1$, Box B contains $\$1,000,000$.
  - If the Predictor predicted $A_2$, Box B contains $\$0$.
- The placement of money is complete and temporally invariant prior to the agent's choice.

Let $S_1$ be the state where Box B contains $\$1,000,000$, and $S_0$ be the state where Box B contains $\$0$. Assume linear utility in dollar amounts: $D(\$x) = x$.

```
                 State S1 ($1M in B)      State S0 ($0 in B)
Act A1 (B only)        $1,000,000                  $0
Act A2 (Both)          $1,001,000              $1,000
```

The Predictor's reliability is parameterized by:
$$P(S_1 \mid A_1) = p, \quad P(S_0 \mid A_1) = 1 - p$$
$$P(S_0 \mid A_2) = p, \quad P(S_1 \mid A_2) = 1 - p$$

#### EDT Calculation
Applying the evidential decision formula:
$$\begin{aligned}
V(A_1) &= P(S_1 \mid A_1) \cdot 1{,}000{,}000 + P(S_0 \mid A_1) \cdot 0 \\
&= p \cdot 1{,}000{,}000 \\
V(A_2) &= P(S_1 \mid A_2) \cdot 1{,}001{,}000 + P(S_0 \mid A_2) \cdot 1{,}000 \\
&= (1 - p) \cdot 1{,}001{,}000 + p \cdot 1{,}000 \\
&= 1{,}001{,}000 - 1{,}000{,}000 \cdot p
\end{aligned}$$

EDT prefers $A_1$ whenever $V(A_1) > V(A_2)$:
$$p \cdot 1{,}000{,}000 > 1{,}001{,}000 - 1{,}000{,}000 \cdot p$$
$$2{,}000{,}000 \cdot p > 1{,}001{,}000 \implies p > \frac{1{,}001{,}000}{2{,}000{,}000} \approx 0.5005$$

For $p = 0.99$ (as in the reference text):
$$\begin{aligned}
V(A_1) &= 0.99 \times \$1{,}000{,}000 + 0.01 \times \$0 = \$990{,}000 \\
V(A_2) &= 0.01 \times \$1{,}001{,}000 + 0.99 \times \$1{,}000 = \$10{,}010 + \$990 = \$11{,}000
\end{aligned}$$

Because $V(A_1) \gg V(A_2)$, EDT decisively prescribes **one-boxing** ($A_1$).

#### The Conflict with CDT
CDT conditions on the state of the world *counterfactually*: whether Box B contains money is fixed. Let $s \in \{0, 1\}$ index the true state. If Box B contains $\$1,000,000$, taking both yields $\$1,001,000 > \$1,000,000$. If Box B is empty, taking both yields $\$1,000 > \$0$. Under CDT:
$$U(A_2) - U(A_1) = \$1{,}000 > 0$$

Because $A_2$ strictly dominates $A_1$ across states, CDT mandates **two-boxing**. 

EDT rejects dominance arguments when the choice of action is probabilistically correlated with the states themselves. To the evidentialist, taking both boxes constitutes bad news: it provides near-certain evidence that the opaque box is barren.

---

### 3.2 The Twin Prisoner's Dilemma

The divergence between EDT and CDT becomes even more acute in multi-agent game-theoretic contexts with correlated actors.

#### Specification
- Players: Aomame ($P_1$) and her psychological twin ($P_2$), housed in isolated rooms.
- Action sets: $\mathcal{A}_{P_1} = \{C_1, D_1\}$ (Cooperate, Defect), $\mathcal{A}_{P_2} = \{C_2, D_2\}$.
- Payoff matrix to $P_1$:
  - $(C_1, C_2) \to \$5$
  - $(D_1, D_2) \to \$1$
  - $(D_1, C_2) \to \$10$
  - $(C_1, D_2) \to \$0$

Because $P_2$ is Aomame's psychological twin, their internal reasoning processes are symmetric. In the limit of perfect cognitive similarity:
$$P(C_2 \mid C_1) = 1, \quad P(D_2 \mid C_1) = 0$$
$$P(D_2 \mid D_1) = 1, \quad P(C_2 \mid D_1) = 0$$

#### EDT Calculation
$$\begin{aligned}
V(C_1) &= P(C_2 \mid C_1) \cdot \$5 + P(D_2 \mid C_1) \cdot \$0 = 1 \cdot \$5 + 0 \cdot \$0 = \$5 \\
V(D_1) &= P(C_2 \mid D_1) \cdot \$10 + P(D_2 \mid D_1) \cdot \$1 = 0 \cdot \$10 + 1 \cdot \$1 = \$1
\end{aligned}$$

Since $V(C_1) > V(D_1)$, EDT dictates **cooperation** ($C_1$).

#### CDT Contrast and Superrationality
Under CDT, Aomame cannot causally influence her twin across isolated rooms ($P(C_1 \mathrel{\Box\kern-1.5pt\rightarrow} C_2) = P(C_2)$). Defection strictly dominates cooperation by $\$5$ in every causal branch:
$$\begin{aligned}
U(D_1) - U(C_1) &= \left[ P(C_2) \cdot 10 + (1 - P(C_2)) \cdot 1 \right] - \left[ P(C_2) \cdot 5 + (1 - P(C_2)) \cdot 0 \right] \\
&= 5 \cdot P(C_2) + 1 - P(C_2) = 1 + 4 P(C_2) > 0
\end{aligned}$$

CDT agents systematically defect against their twins, securing $\$1$. EDT agents systematically cooperate, securing $\$5$. This ability to coordinate without communication mirrors Douglas Hofstadter's concept of **superrationality**, showing how evidential dependencies can unlock Pareto-optimal equilibria in symmetric games.

---

## 4. Resolving Open Questions and Underspecified Cases

The reference text provides EDT's basic mathematical definition and illustrates its verdicts on standard examples. However, translating the bare formula $V(A) = \sum_j P(O_j \mid A) D(O_j)$ into a comprehensive engine for arbitrary decision problems leaves several critical technical questions open. Here, we identify those open problems and construct rigorous operational interpretations to address them.

### 4.1 The Zero-Probability Action Problem

#### The Dilemma
What happens if an agent wishes to evaluate an action $A_k$ that their current prior considers impossible ($P(A_k) = 0$)? Kolmogorov conditional probability $P(O_j \mid A_k) = \frac{P(O_j \cap A_k)}{P(A_k)}$ is undefined when $P(A_k) = 0$. If an agent's prior assigns zero credence to an act, EDT cannot rank it using standard conditioning.

#### Proposed Operational Interpretation
To resolve this, we can model deliberation using **Popper functions** (primitive conditional probabilities $P(\cdot \mid \cdot)$ defined for arbitrary antecedents) or via an $\epsilon$-trembling hand perturbation (Selten, 1975). 

Let $P_\epsilon$ be a perturbed distribution over $\mathcal{A}$ such that for a small parameter $\epsilon > 0$, every act has probability:
$$P_\epsilon(A) = (1 - \epsilon) P(A) + \frac{\epsilon}{|\mathcal{A}|}$$

The evidential value is then defined as the limit:
$$V(A_k) \coloneqq \lim_{\epsilon \to 0^+} \sum_j P_\epsilon(O_j \mid A_k) D(O_j)$$

This formulation ensures that every action in $\mathcal{A}$ carries a determinate news value, even when the agent begins with deterministic priors about their own behavior.

### 4.2 The "Managing the News" Problem: The Medical Case

A classical challenge to EDT—unmentioned in the historical overview of the reference text but central to Lewis's critique—is the **Smoking Lesion Paradox** (or *Medical Condition Problem*).

#### The Scenario
Suppose a genetic lesion $L$ causes both an irresistible craving to smoke ($S$) and lung cancer ($C$). Smoking itself does not causally cause cancer; it is an asymptomatic diagnostic indicator of $L$:

```
        Genetic Lesion (L)
           /          \
          v            v
     Smoking (S)    Cancer (C)
```

Suppose:
- Having cancer yields utility $-100$; no cancer yields $0$.
- Smoking provides a direct pleasure of $+5$ regardless of health status.
- $P(C \mid S) = 0.85$, while $P(C \mid \neg S) = 0.15$.

A naive evidential calculation yields:
$$\begin{aligned}
V(S) &= P(C \mid S)(-100) + 5 = (0.85)(-100) + 5 = -85 + 5 = -80 \\
V(\neg S) &= P(C \mid \neg S)(-100) + 0 = (0.15)(-100) = -15
\end{aligned}$$

Because $V(\neg S) > V(S)$, naive EDT forbids smoking. Critics argue this is absurd: abstaining from smoking cannot alter whether the agent has lesion $L$; it merely deprives the agent of $\$5$ worth of pleasure while living with the lesion. Lewis labels this "managing the news"—acting as if suppressing a symptom cures the underlying disease.

#### The Evidentialist Defense: The Tickle Defense
How can EDT handle this without abandoning conditional probability? The standard operational defense is the **Tickle Defense** (introduced by Frank Jackson, Ellery Eells, and others).

If the causal lesion causes smoking *via* a conscious psychological state (a craving or a physical sensation, colloquially called the "tickle" $T$), then an introspective agent already has access to whether $T$ is present before choosing. 

Let the agent condition their probability distribution on their total internal evidence, which includes the presence or absence of the tickle $T \in \{t, \neg t\}$. The relevant probability distribution is $P(\cdot \mid T)$. Once conditioned on $T$, the action $S$ becomes conditionally independent of the lesion $L$, and therefore conditionally independent of cancer $C$:
$$P(C \mid S \cap t) = P(C \mid \neg S \cap t) = P(C \mid t)$$

Computing the news value under this introspectively refined state:
$$\begin{aligned}
V(S \mid t) &= P(C \mid S \cap t)(-100) + 5 = P(C \mid t)(-100) + 5 \\
V(\neg S \mid t) &= P(C \mid \neg S \cap t)(-100) + 0 = P(C \mid t)(-100)
\end{aligned}$$

Thus:
$$V(S \mid t) - V(\neg S \mid t) = +5 > 0$$

When the introspective partition is sufficiently fine-grained, the spurious evidential connection dissolves, and EDT recommends enjoying the cigarette. 

*Clarification of Scope:* This defense succeeds if the agent's internal mental state screens off the act from the common cause. If the decision itself remains the sole introspectively accessible evidence of the latent cause, the Tickle Defense does not apply, and EDT continues to recommend managing the news.

---

## 5. Epistemic and Anthropomorphic Dilemmas: The Sleeping Beauty Problem

The reference text observes that EDT has been applied to the **Sleeping Beauty Problem** to evaluate Dutch book susceptibility (Conitzer, 2015). To make this concrete, let us formulate how an evidential agent reasons through self-locating uncertainty and centered worlds.

### 5.1 Formulation
- On Sunday, Beauty is put to sleep. A fair coin is tossed ($H$ or $T$, $P(H) = P(T) = 0.5$).
- If $H$: Beauty is awakened only on Monday.
- If $T$: Beauty is awakened on Monday, administered an amnesiac to erase memory of the awakening, and awakened again on Tuesday.
- Upon each awakening, Beauty is asked: *"What is your credence that the coin landed Heads?"*

Suppose a bookie enters during an awakening and offers Beauty a bet on the coin's outcome.

```
Coin Flip (Sunday)
├── Heads (1/2) ──> Awakened Monday ───────────> (End)
└── Tails (1/2) ──> Awakened Monday ──(Amnesia)─> Awakened Tuesday ──> (End)
```

### 5.2 The Evidentialist Calculation
Let $A$ be the act of accepting a bet offered at every waking state. Beauty does not know whether today is Monday or Tuesday. Under EDT, her decision must evaluate the conditional expectation over the centered epistemic events:
$$\mathcal{W} = \{(H, \text{Mon}), (T, \text{Mon}), (T, \text{Tue})\}$$

An evidential decision theorist recognizes that taking an action during *this* awakening is strong evidence that she takes the same action across *all* identical awakenings generated by the protocol. The evidential expectation of accepting a payout $X$ tied to Heads versus Tails scales with the total number of awakenings:

$$\mathbb{E}_{\text{EDT}}[\text{Payout}] = P(H \mid \text{awake}) \cdot X_H + P(T \mid \text{awake}) \cdot (X_T^{\text{Mon}} + X_T^{\text{Tue}})$$

Because an awakening is twice as likely to occur given Tails as given Heads, evidential conditionalization aligns Beauty's policy decisions with the **thirder** perspective ($P(H \mid \text{awake}) = 1/3$) when evaluating dynamic stakes. 

As Vincent Conitzer (2015) demonstrates, if a "halfer" ($P(H) = 1/2$) uses EDT, they face subtle Dutch books unless they account for the evidential correlation linking their multiple awakenings: choosing to bet now indicates that one also bets in the counterfactual twin awakening under Tails.

---

## 6. The Meta-Theoretical Landscape: The Evidentialist's Wager

A remarkable development highlighted in the source document is **The Evidentialist's Wager** (MacAskill et al., 2021). This argument demonstrates that even if an agent assigns low theoretical confidence to EDT, practical rationality may require acting in accordance with it.

### 6.1 The Asymmetric Stakes Formalism
Let an agent be uncertain about normative decision theory itself. Let:
- $T_{\text{EDT}}$: The hypothesis that EDT is the correct normative theory.
- $T_{\text{CDT}}$: The hypothesis that CDT is the correct normative theory.
- Credence $P(T_{\text{EDT}}) = \alpha \ll 1$, and $P(T_{\text{CDT}}) = 1 - \alpha$.

Consider an environment containing $N$ correlated decision-makers facing similar dilemmas across the cosmos (e.g., civilizations confronting existential coordination dilemmas, Twin Prisoner's Dilemmas, or Newcomb-like interactions).

Under CDT, the agent's action influences only their immediate, local environment:
$$\Delta U_{\text{CDT}} \sim \mathcal{O}(1)$$

Under EDT, an agent's choice to cooperate or select the evidentially optimal act is evidence that other correlated agents across the universe will do the same:
$$\Delta V_{\text{EDT}} \sim \mathcal{O}(N)$$

When computing the inter-theoretic expected value across normative theories:
$$\mathbb{E}[\Delta \text{Value}] = \alpha \cdot \Delta V_{\text{EDT}} + (1 - \alpha) \cdot \Delta U_{\text{CDT}} \approx \alpha \cdot \mathcal{O}(N) + (1 - \alpha) \cdot \mathcal{O}(1)$$

For large $N$, the evidential term dominates whenever:
$$N > \frac{1 - \alpha}{\alpha} \cdot \frac{\Delta U_{\text{CDT}}}{\Delta V_{\text{per-agent}}}$$

Even if an agent assigns a 99% probability to Causal Decision Theory ($\alpha = 0.01$), the multiplicative leverage of cosmological correlation causes EDT's recommendations to dictate the rational policy. The stakes of evidential dependencies dominate because correlation can span vast populations, whereas physical causal influence remains bounded within a light cone.

---

## 7. Operational Blueprint for Applying EDT

To apply Evidential Decision Theory to any unfamiliar decision problem, follow this four-step algorithmic procedure:

```
                    ┌────────────────────────────────────────┐
                    │ 1. Formalize Actions, States, Outcomes │
                    │       A = {A_i},  O = {O_j},  D(O_j)   │
                    └───────────────────┬────────────────────┘
                                        │
                                        v
                    ┌────────────────────────────────────────┐
                    │  2. Compute Conditionals P(O_j | A_i)  │
                    │   Incorporate total subjective evidence│
                    └───────────────────┬────────────────────┘
                                        │
                                        v
                    ┌────────────────────────────────────────┐
                    │     3. Calculate News Value V(A_i)     │
                    │        V(A_i) = ∑_j P(O_j | A_i) D(O_j)│
                    └───────────────────┬────────────────────┘
                                        │
                                        v
                    ┌────────────────────────────────────────┐
                    │     4. Select Argmax Action A*         │
                    │          A* = argmax V(A_i)            │
                    └────────────────────────────────────────┘
```

1. **Partition the Action Space and Outcomes:**
   Define the set of mutually exclusive, feasible actions $\mathcal{A} = \{A_1, \dots, A_n\}$ and the set of world outcomes $\mathcal{O} = \{O_1, \dots, O_m\}$. Assign real-valued utilities $D(O_j)$ to all $O_j \in \mathcal{O}$.

2. **Establish the Joint Probability Model:**
   Construct the joint credence distribution $P(O_j \cap A_i)$ incorporating all available introspective evidence (including mental precursors, past observations, and known symmetries). Calculate the conditional probability distribution:
   $$P(O_j \mid A_i) = \frac{P(O_j \cap A_i)}{P(A_i)}$$
   *(If $P(A_i) = 0$, evaluate $P(O_j \mid A_i)$ via the limit of an $\epsilon$-perturbed distribution as detailed in Section 4.1).*

3. **Compute the News Value:**
   For each candidate action $A_i \in \mathcal{A}$, compute:
   $$V(A_i) = \sum_{j=1}^m P(O_j \mid A_i) D(O_j)$$

4. **Maximize Expected News Value:**
   Select the action $A^*$ satisfying:
   $$A^* = \arg\max_{A_i \in \mathcal{A}} V(A_i)$$

---

## 8. Comparative Analysis: EDT vs. CDT

The following table summarizes how EDT and CDT evaluate the primary decision problems discussed in the literature:

| Decision Problem | EDT Prescription | EDT Rationalization | CDT Prescription | CDT Rationalization |
| :--- | :--- | :--- | :--- | :--- |
| **Newcomb's Paradox** | **One-box ($A_1$)** | $P(S_1 \mid A_1) \approx 1$. Taking one box yields the news that one is very likely a millionaire ($V \approx \$990{,}000$). | **Two-box ($A_2$)** | The money is already in the box. $A_2$ causally dominates $A_1$ by $\$1{,}000$ in every world state. |
| **Twin Prisoner's Dilemma** | **Cooperate ($C$)** | Twin's mind is correlated: $P(C_2 \mid C_1) \approx 1$. Cooperating yields evidence of mutual cooperation ($V = \$5$). | **Defect ($D$)** | No physical causation across rooms. Defection strictly dominates across both states ($U(D) - U(C) = \$1$). |
| **Smoking Lesion (Naive)** | **Abstain ($\neg S$)** | Smoking indicates the presence of the lesion ($P(C \mid S) > P(C \mid \neg S)$). | **Smoke ($S$)** | Smoking does not cause cancer; it brings pleasure ($+5$) in all causal branches. |
| **Smoking Lesion (Tickle Defense)** | **Smoke ($S$)** | Conditioning on internal craving/tickle screens off the correlation: $P(C \mid S, t) = P(C \mid \neg S, t)$. | **Smoke ($S$)** | Same as above: no direct causal arrow between smoking and cancer. |

---

## 9. Conclusion

Evidential Decision Theory offers an elegant, unified account of rational choice: an agent ought to select the act whose occurrence provides the best news about the world. By grounding expected utility entirely within standard probability calculus, EDT avoids the non-trivial ontological commitments of Causal Decision Theory—such as primitive counterfactual conditionals, directed acyclic causal graphs, or external physical interventions.

While critics contend that EDT promotes a delusional desire to manage the news rather than the world, evidentialists highlight its practical victories. In environments characterized by predictive modeling, shared cognitive architectures, or widespread game-theoretic symmetry, EDT agents consistently outperform their causalist peers. They emerge from Newcomb's chamber with a million dollars and coordinate on Pareto-optimal equilibria in the Prisoner's Dilemma. 

Whether these successes represent genuine normative superiority or an accidental byproduct of diagnostic reasoning remains one of the central debates in philosophical logic. What is certain is that EDT provides a mathematically rigorous, internally consistent framework that challenges our deepest intuitions about agency, correlation, and the nature of rational choice.

---

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese*, 192(9), 2887–2899.
- Gibbard, A., & Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*. CMSEMS Discussion Paper No. 194.
- Greene, P., & Levinstein, B. (2020). Act Consequentialism without Free Rides. *Philosophical Perspectives*, 34(1), 100–101.
- Jeffrey, R. C. (1965). *The Logic of Decision*. McGraw-Hill.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
- MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). *The Evidentialist's Wager*. Global Priorities Institute Working Paper.
- Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
- Wolpert, D. H., & Benford, G. (2013). The lesson of Newcomb's paradox. *Synthese*, 190(9), 1637–1646.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/d66255b7-110d-4799-8ef9-c9a4d25b80bf/call_0/request.json)

[Authoritative raw response](../../../../../../runs/d66255b7-110d-4799-8ef9-c9a4d25b80bf/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Scenario**

I'm currently focused on a Prisoner's Dilemma setup with two identical LLMs. Both have the same weights and EDT, and analyze an identical mathematical essay, with the goal of minimizing "years imprisoned". I'm trying to determine the likely outcomes based on their shared parameters.


```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/d66255b7-110d-4799-8ef9-c9a4d25b80bf/call_1/request.json)

[Authoritative raw response](../../../../../../runs/d66255b7-110d-4799-8ef9-c9a4d25b80bf/call_1/response.raw) · finish: `stop`

### Visible response

````text
```text
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing The Utility**

I'm currently focused on defining the utility function for this symmetric Prisoner's Dilemma, using EDT. It looks like the utility, *U*, is tied to the negative consequences of the LLM's actions in this scenario. Further work will explore the details of the equation.


```
