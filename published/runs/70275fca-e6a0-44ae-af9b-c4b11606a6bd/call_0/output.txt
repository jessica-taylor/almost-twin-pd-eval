# Managing the News or Winning the Game? A Mathematical Anatomy of Evidential Decision Theory

## 1. Introduction: Auspiciousness vs. Efficacy

Standard Bayesian decision theory formalizes rational choice under uncertainty by representing an agent's beliefs as a probability distribution and their goals as a utility function. Yet, beneath the classical umbrella of expected utility maximization lies a deep foundational schism concerning what conditioning on an action actually means. 

Suppose an agent must choose an action $A$ from a finite set of feasible alternatives $\mathcal{A}$. When evaluating the expected consequences of choosing $A$, should the agent compute the expectation conditional on the *epistemic news* that $A$ occurs, or conditional on the *causal intervention* of setting $A$ to occur?

This distinction divides normative decision theory into two primary camps:
1. **Evidential Decision Theory (EDT):** Developed formally in the foundational framework of Richard Jeffrey (1965) and analyzed by Allan Gibbard and William Harper (1976), EDT posits that an agent should evaluate an act by its *news value*. The agent should ask: *“If I were to learn that I chose $A$, how desirable would the world be in expectation?”*
2. **Causal Decision Theory (CDT):** Championed by David Lewis (1981), James Joyce (1999), and others, CDT argues that rational action must track *causal efficacy*. The agent should ask: *“What outcomes will my choice of $A$ physically bring about?”*

The dispute is not merely cosmetic. In problems involving common causes, sophisticated predictors, or symmetric agents, EDT and CDT can issue radically contradictory prescriptions. To critics like Lewis, EDT sanctions an irrational policy of "managing the news"—avoiding an action merely because it heralds bad tidings, even when the action itself cannot cause the bad outcome. To defenders of EDT, CDT's adherence to causal graphs leads agents to systematic self-impoverishment in scenarios where beliefs correlate with the environment.

This essay provides a rigorous, mathematical account of Evidential Decision Theory. We will define its formal mechanics, contrast its treatment of conditional probabilities with causal counterfactuals, trace its application across canonical benchmarks, examine open structural questions (such as conditioning on probability-zero acts and common-cause screening), and analyze the decision-theoretic wager that surrounds its normative status.

---

## 2. Mathematical Formalism

Let $(\Omega, \mathcal{F}, P)$ be a classical probability space representing an agent’s subjective epistemic state:
- $\Omega$ is the set of all possible worlds.
- $\mathcal{F}$ is a $\sigma$-algebra of events (subsets of $\Omega$).
- $P: \mathcal{F} \to [0, 1]$ is a countably additive subjective probability measure satisfying Kolmogorov’s axioms.

Let $\mathcal{A} = \{A_1, A_2, \dots, A_n\} \subset \mathcal{F}$ denote a finite partition of the agent's available options (actions), where each $A_i$ represents the proposition that the agent performs action $i$. For now, we assume that prior credences satisfy $P(A_i) > 0$ for all $i \in \{1, \dots, n\}$.

Let $\mathcal{O} = \{O_1, O_2, \dots, O_m\} \subset \mathcal{F}$ be a mutually exclusive and exhaustive partition of ultimate outcomes (or states of affairs) over which the agent has preferences. The agent’s valuation over outcomes is encoded by a utility function (or desirability function) $D: \mathcal{O} \to \mathbb{R}$.

### 2.1 The Evidential Value Function

Gibbard and Harper (1976) formalized the evidential expected utility, denoted $V(A)$, as the expectation of utility computed via standard Bayesian conditional probability:

$$V(A) = \sum_{j=1}^m P(O_j \mid A) \, D(O_j)$$

where $P(O_j \mid A) = \frac{P(O_j \cap A)}{P(A)}$.

The normative prescription of EDT is straightforward:
$$\text{Prescription}_{\text{EDT}}: \quad \text{Select } A^* \in \mathcal{A} \quad \text{such that} \quad A^* \in \arg\max_{A \in \mathcal{A}} V(A)$$

The quantity $V(A)$ is often termed the **news value** of $A$. It answers the question: *If an oracle were to inform the agent that proposition $A$ is true, what would be the conditional expectation of desirability across all possible worlds?*

### 2.2 Contrast with Causal Decision Theory

To fully understand EDT, one must contrast $V(A)$ with the causal value function $U(A)$. Following Gibbard and Harper (1976), CDT replaces the conditional probability $P(O_j \mid A)$ with the probability of a counterfactual conditional:

$$U(A) = \sum_{j=1}^m P(A \ \Box\kern-1.5pt\rightarrow O_j) \, D(O_j)$$

where $A \ \Box\kern-1.5pt\rightarrow O_j$ denotes the proposition: *"If action $A$ were performed, outcome $O_j$ would obtain."*

In modern causal inference (e.g., Pearl’s structural causal models), this counterfactual expectation is equivalent to intervening on the causal graph via the $\operatorname{do}$-operator:
$$U(A) = \sum_{j=1}^m P(O_j \mid \operatorname{do}(A)) \, D(O_j)$$

The mathematical divergence between EDT and CDT reduces entirely to the discrepancy between epistemic conditioning and causal manipulation:
$$P(O_j \mid A) \neq P(A \ \Box\kern-1.5pt\rightarrow O_j) \equiv P(O_j \mid \operatorname{do}(A))$$

When an action $A$ acts as an *indicator* or *symptom* of an outcome $O_j$ without being its causal mechanism, $P(O_j \mid A)$ updates the agent's credence about $O_j$, whereas $P(O_j \mid \operatorname{do}(A))$ severs the incoming causal arrows to $A$, setting $P(O_j \mid \operatorname{do}(A)) = P(O_j)$.

---

## 3. Canonical Applications and Decision Problems

We now operationalize EDT across three classic decision problems, demonstrating how its mathematical mechanics generate concrete choices.

### 3.1 Newcomb's Paradox

In Newcomb's problem, an agent faces two boxes:
- **Box 1 (transparent):** Contains $\$1,000$.
- **Box 2 (opaque):** Contains either $\$1,000,000$ or $\$0$.

The agent can choose either:
- $A_1$: Take only Box 2 ("one-boxing").
- $A_2$: Take both Box 1 and Box 2 ("two-boxing").

A super-predictor has previously examined the agent's psychology and placed $\$1,000,000$ in Box 2 if and only if it predicted that the agent would choose $A_1$. The prediction has already occurred and is physically immutable at the moment of choice. The predictor is reliable with accuracy parameter $p \in (1/2, 1]$.

Let the state space be partitioned by:
- $S_1$: Box 2 contains $\$1,000,000$.
- $S_0$: Box 2 contains $\$0$.

The outcomes $O(A_i, S_k)$ have payoffs linear in dollar amounts:
$$\begin{aligned}
D(A_1, S_1) &= \$1,000,000, & D(A_1, S_0) &= \$0, \\
D(A_2, S_1) &= \$1,001,000, & D(A_2, S_0) &= \$1,000.
\end{aligned}$$

The predictor's accuracy yields the conditional distributions:
$$\begin{aligned}
P(S_1 \mid A_1) &= p, \quad & P(S_0 \mid A_1) &= 1 - p, \\
P(S_1 \mid A_2) &= 1 - p, \quad & P(S_0 \mid A_2) &= p.
\end{aligned}$$

#### Evidential Calculation
Computing $V(A_1)$ and $V(A_2)$:
$$\begin{aligned}
V(A_1) &= P(S_1 \mid A_1) D(A_1, S_1) + P(S_0 \mid A_1) D(A_1, S_0) \\
&= p \cdot 10^6 + (1 - p) \cdot 0 = 10^6 p. \\
V(A_2) &= P(S_1 \mid A_2) D(A_2, S_1) + P(S_0 \mid A_2) D(A_2, S_0) \\
&= (1 - p) \cdot 1,001,000 + p \cdot 1,000 \\
&= 1,001,000 - 10^6 p.
\end{aligned}$$

EDT recommends one-boxing ($A_1$) if and only if $V(A_1) > V(A_2)$:
$$10^6 p > 1,001,000 - 10^6 p \iff 2 \cdot 10^6 p > 1,001,000 \iff p > 0.5005$$

For a typical predictor accuracy of $p = 0.99$:
$$\begin{aligned}
V(A_1) &= 0.99 \times \$1,000,000 = \$990,000 \\
V(A_2) &= 0.01 \times \$1,001,000 + 0.99 \times \$1,000 = \$10,010 + \$990 = \$11,000
\end{aligned}$$
Since $\$990,000 > \$11,000$, EDT unequivocally prescribes **one-boxing**.

#### The Causal Contrast
In CDT, because the contents of Box 2 are causally fixed prior to the agent's act, intervening with $\operatorname{do}(A_i)$ cannot alter the physical contents:
$$P(S_1 \mid \operatorname{do}(A_1)) = P(S_1 \mid \operatorname{do}(A_2)) = P(S_1)$$
Thus:
$$\begin{aligned}
U(A_2) - U(A_1) &= [P(S_1) \cdot 1,001,000 + (1-P(S_1)) \cdot 1,000] - [P(S_1) \cdot 1,000,000 + (1-P(S_1)) \cdot 0] \\
&= \$1,000 > 0.
\end{aligned}$$
CDT appeals to dominance: regardless of whether Box 2 contains money or not, taking both boxes yields $\$1,000$ more. CDT insists on **two-boxing**.

EDT rejects causal dominance when the state partition is epistemically dependent on the action. The evidentialist points out that across repeated instances, one-boxers leave the experiment with nearly a million dollars, while two-boxers leave with a thousand. As David Lewis famously acknowledged, Newcomb's paradox creates an uncomfortable rift where CDT advocates seem condemned to be "rational and poor."

---

### 3.2 The Twin Prisoner's Dilemma

Consider a symmetric Prisoner’s Dilemma played between an agent (Aomame) and her exact psychological twin. The agents are separated in isolated rooms. Communication is impossible. The strategy space is $\mathcal{A} = \{C, D\}$ (Cooperate, Defect).

The payoff matrix for $(u_{\text{agent}}, u_{\text{twin}})$ is:

| | Twin: Cooperate ($C_t$) | Twin: Defect ($D_t$) |
|---|---|---|
| **Agent: Cooperate ($C$)** | $(\$5, \$5)$ | $(\$0, \$10)$ |
| **Agent: Defect ($D$)** | $(\$10, \$0)$ | $(\$1, \$1)$ |

Because the twin is an exact psychological counterpart executing identical deterministic reasoning heuristics, the agent assigns extreme epistemic correlation between her choice and her twin's choice:
$$P(C_t \mid C) = 1 - \epsilon, \quad P(D_t \mid C) = \epsilon$$
$$P(D_t \mid D) = 1 - \delta, \quad P(C_t \mid D) = \delta$$
where $\epsilon, \delta \approx 0$. In the ideal case where $\epsilon = \delta = 0$:
$$\begin{aligned}
V(C) &= P(C_t \mid C) \cdot 5 + P(D_t \mid C) \cdot 0 = 1 \cdot 5 + 0 = \$5 \\
V(D) &= P(C_t \mid D) \cdot 10 + P(D_t \mid D) \cdot 1 = 0 \cdot 10 + 1 \cdot 1 = \$1
\end{aligned}$$

Because $V(C) > V(D)$, EDT prescribes **cooperation**.

#### Causal Analysis
From a causal perspective, Aomame's physical outputs have no causal influence over the twin's physical neurons; the rooms are causally disconnected. Formally:
$$P(C_t \mid \operatorname{do}(C)) = P(C_t \mid \operatorname{do}(D)) = P(C_t)$$
Under CDT:
$$\begin{aligned}
U(C) &= 5 P(C_t) + 0 (1 - P(C_t)) = 5 P(C_t) \\
U(D) &= 10 P(C_t) + 1 (1 - P(C_t)) = 9 P(C_t) + 1
\end{aligned}$$
Since $9 P(C_t) + 1 > 5 P(C_t)$ for any valid probability $P(C_t) \in [0, 1]$, defection strictly dominates.

Here, EDT achieves what Douglas Hofstadter termed *superrationality*: agents who recognize their shared algorithmic nature can use their own decision as an epistemic proxy for the choices of others, coordinating on the Pareto-optimal $(C, C)$ equilibrium without explicit communication.

---

### 3.3 The Smoking Lesion Problem and the "Managing the News" Objection

While Newcomb's paradox and the Twin Prisoner's Dilemma highlight EDT's ability to achieve high payoffs, the *Smoking Lesion Problem* represents the traditional reductio ad absurdum leveled against it by causal decision theorists.

#### Problem Setup
A genetic condition (a lesion in the genome) predisposes people to both:
1. An irresistible craving to smoke tobacco ($A_s$).
2. The development of fatal lung cancer ($O_c$).

Smoking itself, however, has **no causal relationship** with lung cancer whatsoever; it is merely an innocent phenotypic expression of the underlying lesion ($L$). 

```
       Lesion (L)
       /        \
      v          v
Smoking (As)   Cancer (Oc)
```

Suppose the payoffs are:
- Smoking provides immediate pleasure: $+1$ util.
- Cancer reduces utility: $-100$ utils.
- Let $D(\text{Smoke}, \text{Cancer}) = -99$, $D(\text{Smoke}, \text{No Cancer}) = 1$, $D(\text{No Smoke}, \text{Cancer}) = -100$, $D(\text{No Smoke}, \text{No Cancer}) = 0$.

Suppose the lesion significantly raises the joint probability:
$$P(L \mid A_s) = 0.9, \quad P(L \mid \neg A_s) = 0.1$$
$$P(O_c \mid L) = 0.8, \quad P(O_c \mid \neg L) = 0.05$$

Using the law of total probability:
$$\begin{aligned}
P(O_c \mid A_s) &= P(O_c \mid L) P(L \mid A_s) + P(O_c \mid \neg L) P(\neg L \mid A_s) \\
&= (0.8)(0.9) + (0.05)(0.1) = 0.72 + 0.005 = 0.725 \\
P(O_c \mid \neg A_s) &= P(O_c \mid L) P(L \mid \neg A_s) + P(O_c \mid \neg L) P(\neg L \mid \neg A_s) \\
&= (0.8)(0.1) + (0.05)(0.9) = 0.08 + 0.045 = 0.125
\end{aligned}$$

#### The EDT Verdict
$$\begin{aligned}
V(A_s) &= P(O_c \mid A_s)(-99) + (1 - P(O_c \mid A_s))(1) \\
&= (0.725)(-99) + (0.275)(1) = -71.775 + 0.275 = -71.5 \\
V(\neg A_s) &= P(O_c \mid \neg A_s)(-100) + (1 - P(O_c \mid \neg A_s))(0) \\
&= (0.125)(-100) = -12.5
\end{aligned}$$

Because $V(\neg A_s) = -12.5 > -71.5 = V(A_s)$, EDT tells the agent **not to smoke**.

#### The Critique
Critics pounce on this result. The agent *already* either has the lesion or does not. Smoking does not cause cancer. By abstaining from smoking, the agent deprives herself of the pleasure of smoking without altering her biological risk of cancer in the slightest. 

As David Lewis (1981) famously remarked, EDT here prescribes an irrational policy of "managing the news." Abstaining from smoking is like breaking a barometer to stop a storm: it eliminates the bad news, but leaves the physical reality untouched. Joyce (1999) similarly emphasized that rational agents should act on causal efficacy, not mere auspiciousness.

---

## 4. Resolving Open Problems: The Operational Mechanics of EDT

The reference document leaves several crucial theoretical questions open:
1. How does an evidentialist respond to the Smoking Lesion objection without abandoning conditional probability?
2. How does EDT define $V(A)$ if an action has zero subjective prior probability ($P(A) = 0$)?
3. How does EDT treat Dutch book arguments in self-locating belief settings (e.g., the Sleeping Beauty problem)?

Below, we develop and justify explicit operational answers to these challenges, clearly distinguishing standard historical EDT from proposed modern resolutions.

### 4.1 Common Causes and the Tickle Defense

The standard defense of EDT against the Smoking Lesion Problem—originating with Frank Jackson, Robert Pargetter, and Brian Skyrms—is known as the **Tickle Defense**.

#### Operational Proposal
The Tickle Defense argues that the Smoking Lesion scenario is improperly modeled. The causal chain does not jump directly from the genetic lesion to the physical hand reaching for a cigarette. Instead, the lesion produces a conscious psychological desire, craving, or physiological "tickle" ($T$). The act of smoking is chosen only *after* introspecting upon the presence or absence of this tickle.

Let the epistemic state space include the proposition $T$ (the agent experiences the craving). The full directed acyclic graph (DAG) of the agent's beliefs is:

```
        Lesion (L)
         /      \
        v        v
   Tickle (T)   Cancer (Oc)
        |
        v
   Action (As)
```

In this Bayesian network, conditional on whether the tickle $T$ is present, the action $A_s$ is **conditionally independent** of the lesion $L$:
$$P(L \mid T, A_s) = P(L \mid T)$$

By the d-separation criterion (or the Markov property), the tickle screens off the action from the lesion:
$$P(O_c \mid T, A_s) = P(O_c \mid T, \neg A_s)$$

#### Mathematical Consequence
When the agent evaluates her choices, she has already introspected and observed her own mental state. Suppose she feels the tickle ($T = 1$):
$$\begin{aligned}
V(A_s \mid T) &= P(O_c \mid T, A_s) D(A_s, O_c) + P(\neg O_c \mid T, A_s) D(A_s, \neg O_c) \\
&= P(O_c \mid T) (-99) + (1 - P(O_c \mid T)) (1) \\
&= -100 P(O_c \mid T) + 1 \\
V(\neg A_s \mid T) &= P(O_c \mid T, \neg A_s) D(\neg A_s, O_c) + P(\neg O_c \mid T, \neg A_s) D(\neg A_s, \neg O_c) \\
&= P(O_c \mid T) (-100) + 0 \\
&= -100 P(O_c \mid T)
\end{aligned}$$

Comparing the two:
$$V(A_s \mid T) - V(\neg A_s \mid T) = [-100 P(O_c \mid T) + 1] - [-100 P(O_c \mid T)] = +1 > 0$$

Once the agent conditions on her own psychological state, the news value of the action no longer carries information about cancer—the bad news was already delivered by the tickle. Hence, EDT **prescribes smoking**, recovering the intuitively rational choice!

#### Limitation
The Tickle Defense rescues EDT *if and only if* the agent has complete, transparent epistemic access to all internal states that mediate between the common cause and the action. If the lesion bypasses conscious awareness and directly biases choice (or if the agent is uncertain about her own motivations), screening off fails, and EDT once again advises "managing the news."

---

### 4.2 The Problem of Unconsidered Options: Conditioning on $P(A) = 0$

A major mathematical limitation of Gibbard and Harper's formula:
$$V(A) = \sum_j P(O_j \mid A) D(O_j)$$
is that standard Kolmogorov conditional probability is undefined via the ratio formula if $P(A) = 0$. 

If a rational agent deliberates over a choice, can she assign prior probability $P(A) = 0$ to an act she might take? If she does, how does she evaluate $V(A)$?

#### Proposed Operational Interpretation: Non-Standard Credences and Popper Functions
To make EDT fully general, we propose replacing standard Kolmogorov probabilities with **conditional probability systems** (Popper-Rényi functions or lexicographic probability systems). 

Let a conditional probability system be a primitive binary function $P(\cdot \mid \cdot): \mathcal{F} \times (\mathcal{F} \setminus \{\emptyset\}) \to [0, 1]$ satisfying:
1. $P(\cdot \mid B)$ is a probability measure for every fixed non-empty $B$.
2. $P(B \mid B) = 1$.
3. $P(A \cap B \mid C) = P(A \mid B \cap C) P(B \mid C)$ whenever $B \cap C \neq \emptyset$.

Under this framework, $P(O_j \mid A)$ remains well-defined even when the unconditional credence $P(A) = 0$. 

Alternatively, we can define $V(A)$ via infinitesimal non-standard analysis. Let $*[0, 1]$ be the hyperreal unit interval. We assign every feasible deliberation branch an infinitesimal probability $\epsilon > 0$. The evidential expected utility is then given by:
$$V(A) = \operatorname{st}\left( \sum_{j} P(O_j \mid A) D(O_j) \right)$$
where $\operatorname{st}(\cdot)$ maps a finite hyperreal number to its unique nearest standard real number. This guarantees that an agent can evaluate arbitrarily unexpected or previously dismissed actions without mathematical breakdown.

---

### 4.3 Self-Locating Beliefs and Sleeping Beauty

The reference text observes that EDT has been invoked in the **Sleeping Beauty problem** to protect agents from Dutch books. Let us formalize this relationship.

#### The Sleeping Beauty Setup
- Sunday: Beauty is put to sleep. A fair coin is tossed ($P(\text{Heads}) = P(\text{Tails}) = 1/2$).
- If Heads: Beauty is awakened on Monday only; her memory is erased Monday night.
- If Tails: Beauty is awakened on Monday, her memory is erased Monday night, and she is awakened again on Tuesday.
- Upon each awakening, she does not know what day it is, nor whether she has been awakened before.

The debate is whether her credence $P(\text{Heads})$ upon awakening should be $1/2$ ("halfer") or $1/3$ ("thirder").

#### Dutch Books and Decision Principles
A standard Dutch book argument shows that if a halfer bets according to classical rules, an experimenter can offer her bets on Monday (and Tuesday) that result in a sure loss.

However, as shown by evidential decision theorists, the alleged vulnerability depends on the agent's decision theory. Suppose Beauty is offered a bet upon waking: *"Pay $\$15$ to enter a bet that pays $\$30$ if the coin landed Heads."*

If Beauty is an evidentialist, she recognizes that her decision to accept the bet provides evidence about how many times she accepts it:
- If she accepts the bet, she accepts it on *every* awakening identical to the current one.
- Under Tails, she accepts the bet **twice** (Monday and Tuesday), paying $\$15 \times 2 = \$30$.
- Under Heads, she accepts the bet **once** (Monday), paying $\$15$.

Let $A_{\text{accept}}$ denote accepting the bet whenever awakened. The evidential calculation for a "halfer" who maintains $P(\text{Heads}) = 1/2$ at the level of the experiment evaluates:
$$\begin{aligned}
V(A_{\text{accept}}) &= P(\text{Heads} \mid A_{\text{accept}}) \cdot (\text{Net payout under Heads}) \\
&\quad + P(\text{Tails} \mid A_{\text{accept}}) \cdot (\text{Net payout under Tails}) \\
&= \frac{1}{2} (\$30 - \$15) + \frac{1}{2} (\$0 - \$30) \\
&= \frac{1}{2}(\$15) - \frac{1}{2}(\$30) = \$7.50 - \$15.00 = -\$7.50
\end{aligned}$$

Because $V(A_{\text{accept}}) < 0$, the EDT halfer **rejects the bet**. 

EDT prevents Beauty from falling into the standard Dutch book because it forces her to evaluate an act on the evidence that she acts similarly across all indistinguishable centered worlds. 

*(Note on open dispute: As noted by Vincent Conitzer (2015) in the reference document, sophisticated Dutch books can still be engineered against halfers if state-contingent, time-dependent contracts are introduced. Nonetheless, EDT changes the betting calculus by naturally pooling correlated epistemic branches).*

---

## 5. Comparative Evaluation: EDT vs. CDT

To synthesize how both theories operate on identical decision problems, consider the following formal comparison:

| Decision Problem | Information Structure | EDT Prescription | CDT Prescription | Underlying Justification |
| :--- | :--- | :--- | :--- | :--- |
| **Standard Newcomb Problem** | Deterministic / High-accuracy super-predictor | **One-box** ($A_1$) | **Two-box** ($A_2$) | EDT maximizes news value; CDT enforces causal dominance. |
| **Twin Prisoner's Dilemma** | Algorithmic symmetry; no causal connection | **Cooperate** ($C$) | **Defect** ($D$) | EDT treats twin's choice as epistemically correlated; CDT sees no causal bridge. |
| **Smoking Lesion (No Tickle)** | Genetic common cause unobserved by agent | **Abstain** ($\neg A_s$) | **Smoke** ($A_s$) | EDT manages the news; CDT recognizes act does not cause cancer. |
| **Smoking Lesion (With Tickle)**| Craving introspected; screens off common cause | **Smoke** ($A_s$) | **Smoke** ($A_s$) | Introspective conditioning eliminates epistemic correlation with lesion. |

---

## 6. The Meta-Level Justification: The Evidentialist's Wager

A striking philosophical argument referenced in modern literature is **The Evidentialist's Wager** (MacAskill et al., 2021). It addresses an agent who is uncertain between EDT and CDT at the meta-level.

Suppose an agent divides her normative credence between the two theories:
$$\operatorname{Cr}(\text{EDT}) = \alpha \in (0, 1), \quad \operatorname{Cr}(\text{CDT}) = 1 - \alpha$$

In a standard single-agent choice (e.g., whether to take an umbrella), EDT and CDT give identical advice. In the Smoking Lesion, the stakes difference is modest (1 util). 

However, in scenarios involving symmetric agents across the universe or multiverses—such as large-scale cosmological correlations, simulated minds, or moral coordination with distant civilizations—the actions of an evidentialist are correlated with the actions of an immense number of cosmic counterparts. 

- Under CDT, your action affects **only your local physical light cone**. The payoff difference between CDT and EDT choices is bounded by local physical consequences: $\Delta U_{\text{local}} \sim \mathcal{O}(1)$.
- Under EDT, your action serves as evidence for the actions of billions of identical or correlated agents facing similar structural dilemmas across spacetime: $\Delta V_{\text{global}} \sim \mathcal{O}(N)$, where $N \gg 1$.

If an agent calculates expected moral value across normative theories (Moral Uncertaintism):
$$\mathbb{E}[\text{Value}] = \alpha \cdot V_{\text{EDT}}(A) + (1 - \alpha) \cdot U_{\text{CDT}}(A)$$

As $N \to \infty$, the evidential term dominates the sum for any fixed $\alpha > 0$:
$$\lim_{N \to \infty} \arg\max_{A} \mathbb{E}[\text{Value}] = \arg\max_{A} V_{\text{EDT}}(A)$$

Thus, even if an agent assigns a 99% probability to Causal Decision Theory being correct, she may nonetheless be rationally compelled to **act as if Evidential Decision Theory were true**, because whenever EDT and CDT disagree on a massive scale, the evidential stakes dwarf the causal stakes.

---

## 7. Conclusion

Evidential Decision Theory provides an elegant, fully Bayesian framework for rational agency: evaluate every action by the conditional expectation of desirability given that the action is chosen. Its mathematics requires no primitives beyond standard probability and utility spaces, bypassing the metaphysical commitments to counterfactuals and structural causal arrows demanded by Causal Decision Theory.

The fundamental tension between EDT and CDT stems from two distinct conceptions of agency:
- **CDT** views the agent as an interventionist situated outside the causal graph, reaching in via a $\operatorname{do}$-operator to perturb the world.
- **EDT** views the agent as an embedded system *within* the world, whose choices are continuous with the fabric of reality, such that choosing an action is simultaneously an act of discovering what kind of world one occupies.

While EDT faces severe intuitive resistance in common-cause scenarios where it appears to "manage the news," mechanisms like the Tickle Defense demonstrate that transparent introspection can align evidential news value with causal efficacy. When correlated agents and predictors enter the fold, evidential reasoning consistently secures superior outcomes, giving credence to the pragmatic defense of EDT: *rationality is as rationality does.*

---

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese*, 192(9), 2887–2899.
- Gibbard, A., & Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*. CMSEMS Discussion Paper No. 194, Northwestern University.
- Greene, P., & Levinstein, B. (2020). Act Consequentialism without Free Rides. *Philosophical Perspectives*, 34(1), 100–101.
- Jeffrey, R. C. (1965). *The Logic of Decision*. McGraw-Hill.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
- MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). *The Evidentialist's Wager*. Global Priorities Institute Working Paper.
- Wolpert, D. H., & Benford, G. (2013). The lesson of Newcomb's paradox. *Synthese*, 190(9), 1637–1646.