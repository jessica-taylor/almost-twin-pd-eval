# 013_edt_wikipedia_google_gemini-4-argon_rhigh_phigh / 00014

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/1a676e2c-74f8-4696-9d43-e2d32d5778c5/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/1a676e2c-74f8-4696-9d43-e2d32d5778c5/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Acting on Good News: The Mathematics and Philosophy of Evidential Decision Theory

When a rational agent stands at a crossroads and deliberates among competing actions, what precisely are they trying to optimize? 

At first glance, the answer seems obvious: a rational agent chooses the action with the highest expected utility. Yet buried inside the notion of "expected utility" is a profound ambiguity about how an action relates to the state of the universe. Does a rational choice require evaluating what an action will *causally bring about*, or does it require evaluating what taking that action *tells us* about the world we inhabit?

This question divides modern decision theory into two major schools of thought: **Causal Decision Theory (CDT)** and **Evidential Decision Theory (EDT)**. According to the reference account of the theory, Evidential Decision Theory holds that when confronted with a set of possible actions, a rational agent should select the action with the highest *news value*—the action that, if one were to receive the news that it had been performed, would be indicative of the best outcome in expectation. As the philosopher Arif Ahmed (2021) summarizes the principle, EDT advises you to "do what you most want to learn that you will do."

In routine decision problems—such as deciding whether to carry an umbrella or invest in an index fund—EDT and CDT issue identical prescriptions. However, in environments featuring accurate predictors, symmetric strategic agents, or correlated decision-makers, the two theories diverge sharply. Understanding how EDT works, why it diverges from causal reasoning, and how to operationalize it in unfamiliar settings is essential for anyone working at the intersection of formal epistemology, game theory, and artificial intelligence.

---

## 1. The Formal Architecture of Evidential Decision Theory

### 1.1 The Gibbard–Harper Formulation

The foundational mathematical distinction between evidential and causal expected utility was crystallized by Allan Gibbard and William Harper in their classic 1976 paper, *Counterfactuals and Two Kinds of Expected Utility*. 

As presented in the reference article, suppose an agent faces a finite set of mutually exclusive and exhaustive outcomes $\mathcal{O} = \{O_1, O_2, \dots, O_m\}$ and must choose an action $A$ from a set of available alternatives $\mathcal{A}$. Each outcome $O_j$ is assigned a numerical desirability (or utility) $D(O_j) \in \mathbb{R}$ reflecting the agent's preferences. Furthermore, the agent's epistemic state is represented by a probability measure $P$ defined over an algebra of propositions that includes both actions and outcomes.

Evidential Decision Theory proposes that the value of an action $A$, which Gibbard and Harper denote by $V(A)$ to signify its news value or auspiciousness, is calculated using standard conditional probabilities:

$$V(A) = \sum_{j} P(O_j \mid A) D(O_j)$$

Here, $P(O_j \mid A)$ is the conditional probability of outcome $O_j$ given the proposition that action $A$ occurs. An EDT agent evaluates each candidate action $A \in \mathcal{A}$ and selects an action $A^*$ that maximizes $V(A)$:

$$A^* \in \arg\max_{A \in \mathcal{A}} \sum_{j} P(O_j \mid A) D(O_j)$$

By contrast, Causal Decision Theory rejects standard conditionalization when actions and background states are non-causally correlated. Instead, CDT computes the causal expected utility $U(A)$ using counterfactual probabilities:

$$U(A) = \sum_{j} P(A \mathrel{\Box{\rightarrow}} O_j) D(O_j)$$

where the subjunctive conditional $A \mathrel{\Box{\rightarrow}} O_j$ reads "if $A$ were performed, then $O_j$ would occur," and $P(A \mathrel{\Box{\rightarrow}} O_j)$ measures the probability of outcome $O_j$ in the counterfactual situation in which action $A$ is enacted. Because the conditional probability $P(O_j \mid A)$ is not always equal to the counterfactual probability $P(A \mathrel{\Box{\rightarrow}} O_j)$, the functionals $V(A)$ and $U(A)$ are not equivalent.

### 1.2 Operational Extension: The State–Act–Outcome Decomposition

While the source text states the Gibbard–Harper equations directly over outcomes $O_j$, applying EDT to novel problems is often much easier if we decompose outcomes into *actions* and *states of the world*. *(Note: This decomposition goes beyond the brief Wikipedia text to provide a practical computational framework based on standard Savage/Jeffrey decision matrices.)*

In practical modeling, an outcome is rarely an indivisible atom; rather, it is the joint result of what the agent does and how the rest of the world is configured. Let $\mathcal{S} = \{S_1, S_2, \dots, S_n\}$ be a partition of the state space into mutually exclusive and exhaustive background states of nature. A state $S_i$ specifies all relevant features of the environment outside the immediate specification of the act itself. When the agent takes action $A$ in state $S_i$, this pair uniquely determines an outcome $O(A, S_i)$ with desirability $D(A, S_i)$.

Using this partition, the conditional probability of receiving a particular payoff given action $A$ is governed by the posterior probability distribution over states, $P(S_i \mid A)$. We can rewrite the EDT valuation functional as:

$$V(A) = \sum_{i=1}^{n} P(S_i \mid A) D(A, S_i)$$

If the state partition $\mathcal{S}$ is chosen so that each $S_i$ is causally independent of the agent's current action—meaning the agent's choice cannot physically alter which state $S_i$ obtains—then the counterfactual probability of $S_i$ given $A$ is simply the unconditional prior probability of the state: $P(A \mathrel{\Box{\rightarrow}} S_i) = P(S_i)$. Under such a partition, the CDT functional reduces to:

$$U(A) = \sum_{i=1}^{n} P(S_i) D(A, S_i)$$

Putting these two equations side by side reveals the exact mathematical locus of disagreement between EDT and CDT:

1. **CDT holds the probability of causally independent states fixed** across all actions they evaluate, weighting $D(A, S_i)$ by the prior $P(S_i)$.
2. **EDT updates the probability of states conditional on the action**, weighting $D(A, S_i)$ by the Bayesian posterior $P(S_i \mid A) = \frac{P(A \mid S_i) P(S_i)}{P(A)}$.

Consequently, EDT and CDT are guaranteed to agree whenever the background states of the world are *evidentially independent* of the agent's choice—that is, whenever $P(S_i \mid A) = P(S_i)$ for all $S_i \in \mathcal{S}$ and $A \in \mathcal{A}$. They diverge precisely when an agent's choice carries diagnostic information about which state of the world actually holds.

---

## 2. Canonical Divergences: Predictive and Symmetric Correlations

To see how evidential updating alters rational choice, we can examine the two major decision-theoretic thought experiments detailed in the reference article: Newcomb's paradox and the Twin Prisoner's Dilemma.

### 2.1 Newcomb's Paradox

Introduced by physicist William Newcomb and brought into philosophical prominence by Robert Nozick, Newcomb's paradox pits evidential conditioning against causal dominance.

As described in the source text (following Wolpert & Benford, 2013, and Ahmed, 2021), a player faces two boxes, designated **A** and **B**, and a highly reliable predictor. 
* **Box A** is transparent and visibly contains $\$1,000$.
* **Box B** is opaque. Its contents have already been placed inside by the predictor prior to the start of the game according to the following rule:
  * If the predictor predicted that the player will take **only Box B** (one-boxing), Box B contains $\$1,000,000$.
  * If the predictor predicted that the player will take **both Boxes A and B** (two-boxing), Box B contains $\$0$.

Suppose the predictor is $99\%$ accurate, meaning the conditional probability that the predictor made the corresponding prediction given the player's actual choice is $0.99$. The player knows the rules and the predictor's accuracy, but does not know what prediction was made.

Let us organize the problem into our state–act matrix. There are two actions, $\mathcal{A} = \{A_1, A_2\}$, where $A_1$ is "take only Box B" and $A_2$ is "take both boxes." There are two states of the world, $\mathcal{S} = \{S_1, S_2\}$, corresponding to the predictor's past action: $S_1$ ("$\$1\text{M}$ in Box B") and $S_2$ ("nothing in Box B"). Assuming utility is linear in dollars, the payoff and conditional probability table is:

| Action | State $S_1$: $\$1\text{M}$ in Box B | State $S_2$: $\$0$ in Box B |
| :--- | :--- | :--- |
| **$A_1$: Take only Box B** | $D(A_1, S_1) = \$1,000,000$<br>$P(S_1 \mid A_1) = 0.99$ | $D(A_1, S_2) = \$0$<br>$P(S_2 \mid A_1) = 0.01$ |
| **$A_2$: Take both boxes** | $D(A_2, S_1) = \$1,001,000$<br>$P(S_1 \mid A_2) = 0.01$ | $D(A_2, S_2) = \$1,000$<br>$P(S_2 \mid A_2) = 0.99$ |

Computing the evidential expected utilities directly from the Gibbard–Harper formula yields:

$$\begin{aligned}
V(A_1) &= P(S_1 \mid A_1) \times \$1,000,000 + P(S_2 \mid A_1) \times \$0 \\
       &= 0.99 \times \$1,000,000 + 0.01 \times \$0 = \$990,000
\end{aligned}$$

$$\begin{aligned}
V(A_2) &= P(S_1 \mid A_2) \times \$1,001,000 + P(S_2 \mid A_2) \times \$1,000 \\
       &= 0.01 \times \$1,001,000 + 0.99 \times \$1,000 = \$10,010 + \$990 = \$11,000
\end{aligned}$$

Because $V(A_1) = \$990,000 > V(A_2) = \$11,000$, EDT decisively recommends **one-boxing**. Observing oneself take only Box B is overwhelming evidence that the predictor foresaw this choice and stocked Box B with a million dollars.

Why does CDT recommend the opposite? Notice that in every column of the table, $D(A_2, S_i) = D(A_1, S_i) + \$1,000$. Because the predictor's action is already in the past, the player's present choice has zero causal influence over whether $S_1$ or $S_2$ obtains. Thus, for any fixed prior probability $P(S_1) = p$, CDT computes:

$$U(A_2) = p(\$1,001,000) + (1-p)(\$1,000) = p(\$1,000,000) + \$1,000 = U(A_1) + \$1,000$$

Under CDT, two-boxing strictly dominates one-boxing regardless of $p$. Yet if a population of CDT agents and a population of EDT agents play Newcomb's game repeatedly, $99\%$ of the EDT agents walk away millionaires, while $99\%$ of the CDT agents walk away with $\$1,000$—a disparity often called the "Why ain'cha rich?" argument in favor of EDT.

*(Operational generalization)*: We can easily generalize the source's calculation to find the exact predictive accuracy threshold required for EDT to recommend one-boxing. Let Box A contain $a > 0$, Box B contain $b > a$ when predicted to one-box, and let the predictor's diagnostic reliability be $\alpha = P(S_1 \mid A_1) = P(S_2 \mid A_2) \in [0.5, 1]$. Then:

$$V(A_1) > V(A_2) \iff \alpha b > (1-\alpha)(b + a) + \alpha a \iff (2\alpha - 1)b > a \iff \alpha > \frac{1}{2}\left(1 + \frac{a}{b}\right)$$

For $a = \$1,000$ and $b = \$1,000,000$, EDT recommends one-boxing whenever $\alpha > 0.5005$—that is, whenever the predictor is even slightly better than a fair coin toss.

### 2.2 The Twin Prisoner's Dilemma

A second major arena where EDT parts ways with CDT involves symmetric strategic interactions. In the standard Prisoner's Dilemma, two self-interested players choose between Cooperating ($C$) and Defecting ($D$). Defecting strictly dominates Cooperating causally, driving both players to the mutually destructive Nash equilibrium $(D, D)$.

In the **Twin Prisoner's Dilemma** (analyzed in the source via Greene & Levinstein, 2020), an agent named Aomame is paired against her "psychological twin"—an agent situated in a separate room whose reasoning architecture and epistemic state are identical to her own. They cannot communicate, and Aomame cares solely about her own monetary payout. The payoff structure is:
* Both cooperate $(C, C)$: each receives $\$5$.
* Both defect $(D, D)$: each receives $\$1$.
* One defects and one cooperates: the defector receives $\$10$ and the cooperator receives $\$0$.

For a causal decision theorist, the fact that the opponent is a psychological twin is irrelevant at the moment of choice: locked in separate rooms, Aomame's choice cannot causally travel through the walls to force her twin's hand. Whatever the twin is doing, defecting yields either $\$10$ instead of $\$5$, or $\$1$ instead of $\$0$. Thus, CDT prescribes defecting, securing $\$1$.

For an evidential decision theorist, however, the symmetry of their cognitive processes creates an evidential link between their actions. In the limit of an exact psychological twin, $P(\text{Twin } C \mid \text{Aomame } C) = 1$ and $P(\text{Twin } D \mid \text{Aomame } D) = 1$. Following the reference calculation:

$$\begin{aligned}
V(\text{Aomame } C) &= P(\text{Twin } C \mid \text{Aomame } C) \times \$5 + P(\text{Twin } D \mid \text{Aomame } C) \times \$0 \\
                    &= 1 \times \$5 + 0 \times \$0 = \$5
\end{aligned}$$

$$\begin{aligned}
V(\text{Aomame } D) &= P(\text{Twin } C \mid \text{Aomame } D) \times \$10 + P(\text{Twin } D \mid \text{Aomame } D) \times \$1 \\
                    &= 0 \times \$10 + 1 \times \$1 = \$1
\end{aligned}$$

Because $V(\text{Aomame } C) = \$5 > V(\text{Aomame } D) = \$1$, EDT prescribes **cooperating**.

*(Operational generalization)*: Real-world opponents are rarely perfect deterministic clones. How should a reader apply EDT when facing an opponent who is merely *statistically similar*? Suppose the game has general Prisoner's Dilemma payoffs $T > R > P > S$ (Temptation, Reward, Punishment, Sucker), and let the evidential correlation between the players be summarized by two conditional probabilities: $p_{C} = P(\text{Twin } C \mid \text{Self } C)$ and $p_{D} = P(\text{Twin } C \mid \text{Self } D)$, where positive similarity implies $p_C > p_D$. Under EDT:

$$V(C) = p_C R + (1 - p_C) S$$
$$V(D) = p_D T + (1 - p_D) P$$

EDT recommends cooperation whenever $V(C) > V(D)$, which simplifies to:

$$p_C (R - S) - p_D (T - P) > P - S$$

In the further special case of symmetric diagnosticity where $P(\text{Twin } C \mid \text{Self } C) = P(\text{Twin } D \mid \text{Self } D) = \beta \in [0.5, 1]$ (so $p_C = \beta$ and $p_D = 1 - \beta$), the condition for cooperation becomes:

$$\beta > \frac{T - S}{(R - S) + (T - P)}$$

Plugging in Aomame's payoffs ($T=10, R=5, P=1, S=0$) gives $\beta > \frac{10 - 0}{5 + 9} = \frac{10}{14} \approx 0.714$. Thus, Aomame does not need an exact clone to cooperate under EDT; she only needs to believe that her counterpart's decision process matches hers at least $71.5\%$ of the time.

---

## 3. Dependencies, Counterfactuals, and the Confounding Critique

Why don't all decision theorists embrace EDT? The reference article highlights a sharp philosophical objection raised by David Lewis (1981) and James M. Joyce (1999). Lewis famously characterized EDT as promoting "an irrational policy of managing the news," while Joyce argued that "Rational agents choose acts on the basis of their *causal efficacy*, not their auspiciousness; they act to *bring about* good results even when doing so might betoken bad news."

While the reference text notes these criticisms briefly, understanding *why* Lewis and Joyce level this charge—and how modern EDT practitioners respond—requires examining **common-cause confounding** (often called "Medical Newcomb Problems" in the literature). *(Note: The formal example and defense below are developed to explain the mechanics behind the Lewis/Joyce critique cited in the source.)*

### 3.1 The Anatomy of a Common-Cause Confounder

In Newcomb's paradox and the Twin Prisoner's Dilemma, the correlation between the agent's action and the background state arises because the predictor or twin is effectively tracking or mirroring the agent's decision algorithm. But in nature, an action $A$ and an undesirable state $S$ can also be correlated because both are downstream effects of a third variable: a **common cause**.

Suppose a patient is deciding whether to take a mild analgesic ($A_1$) or abstain ($A_2$). Let $S_1$ be the state in which the patient has a latent, dangerous arterial inflammation, and $S_2$ be the state in which their arteries are healthy. 
* The inflammation $S_1$ causes two things: it severely reduces health utility by $-100$ points, and it triggers low-grade headaches that make patients $90\%$ likely to reach for the analgesic $A_1$.
* Healthy patients ($S_2$) rarely get headaches and only take the analgesic $10\%$ of the time.
* Crucially, the analgesic $A_1$ itself has no effect on arterial inflammation, and it provides a genuine causal relief of $+5$ utility points by soothing any headache pain.

Assuming the base rate of the inflammation in the population is $P(S_1) = 0.5$, the conditional probabilities are $P(S_1 \mid A_1) = 0.90$ and $P(S_1 \mid A_2) = 0.10$. The payoff matrix is:

| Action | State $S_1$: Inflammation Present | State $S_2$: Healthy Arteries |
| :--- | :--- | :--- |
| **$A_1$: Take Analgesic** | $D(A_1, S_1) = -95$<br>$P(S_1 \mid A_1) = 0.90$ | $D(A_1, S_2) = +5$<br>$P(S_2 \mid A_1) = 0.10$ |
| **$A_2$: Abstain** | $D(A_2, S_1) = -100$<br>$P(S_1 \mid A_2) = 0.10$ | $D(A_2, S_2) = 0$<br>$P(S_2 \mid A_2) = 0.90$ |

If the patient naively applies the EDT formula using the population-level conditional probabilities $P(S_i \mid A_k)$, they calculate:

$$V(A_1) = 0.90(-95) + 0.10(5) = -85.5 + 0.5 = -85$$
$$V(A_2) = 0.10(-100) + 0.90(0) = -10$$

Because $-10 > -85$, naive EDT advises the patient to **abstain from the painkiller**! Taking the painkiller is statistically "bad news" because people who take painkillers usually have the dangerous inflammation. This is precisely what Lewis means by "an irrational policy of managing the news" and what Joyce means by choosing based on *auspiciousness* rather than *causal efficacy*. Refusing the painkiller does not erase the arterial inflammation; it merely leaves the patient with an untreated headache on top of whatever arterial state they already have.

### 3.2 Operational Resolution: Screening Off and the "Tickle Defense"

Does an EDT agent actually have to refuse the painkiller? In the philosophical literature, defenders of EDT (starting with Richard Jeffrey and Ellery Eells) argue that naive calculations like the one above misapply the probability measure $P$.

In EDT, $P(\cdot)$ is not an impersonal statistical frequency table; it is the deliberating agent's *current epistemic probability distribution*, conditioned on everything the agent knows at the moment of choice—including their own conscious desires, symptoms, and inclinations. In causal terminology, the latent state $S_1$ (inflammation) does not cause action $A_1$ (swallowing the pill) by bypassing the agent's mind. Instead, $S_1$ causes an intermediate phenomenological state $T$—a "tickle," a headache, or an urge to take the pill—which the agent consciously experiences *before* choosing:

$$S_1 \longrightarrow T \longrightarrow A_1$$

In probability theory, an intermediate variable $T$ along a causal chain **screens off** the distal cause $S_1$ from the downstream effect $A_1$. Once the agent conditionalizes their probability function on their current introspective awareness of $T$ (whether or not they feel a headache), the conditional probability of having the inflammation becomes independent of the subsequent motor act of swallowing the pill:

$$P(S_1 \mid A_1, T) = P(S_1 \mid A_2, T) = P(S_1 \mid T)$$

When the EDT valuation is computed using the updated credence function $P_T(\cdot) = P(\cdot \mid T)$, the spurious diagnostic Penalty vanishes:

$$V_T(A_1) = P(S_1 \mid T)(-95) + P(S_2 \mid T)(5) = -100 P(S_1 \mid T) + 5 = V_T(A_2) + 5$$

Thus, when properly conditionalized on pre-choice introspective evidence, EDT agrees with CDT that the patient should take the painkiller.

What if a common cause directly influences the physical act $A$ *without* passing through any conscious states $T$ accessible to the agent? Here we reach a genuine philosophical fork in the road:
1. **Strict Evidentialists** (such as Arif Ahmed, 2021) accept the radical conclusion: if the correlation cannot be screened off by anything the agent can know prior to acting, then the agent *should* one-box even in medical Newcomb problems, treating them identically to standard Newcomb problems.
2. **Causalists** (like Lewis and Joyce) treat unscreened common causes as proof that decision theory must replace $P(S_i \mid A)$ with causal counterfactuals $P(A \mathrel{\Box{\rightarrow}} S_i)$ from the start.

---

## 4. Open Questions and Operational Refinements

While the core equation $V(A) = \sum_j P(O_j \mid A) D(O_j)$ is deceptively compact, applying it to complex or unfamiliar problems exposes several foundational questions that the brief source text mentions only in passing or leaves open. Below, we examine three critical operational challenges and show how to handle them mathematically.

### 4.1 The Measure-Zero Deliberation Problem ($P(A) = 0$)

*The Open Question:* The source defines $V(A)$ via the standard conditional probability $P(O_j \mid A)$. In Kolmogorov probability theory, conditional probability is defined as a ratio:

$$P(O_j \mid A) = \frac{P(O_j \cap A)}{P(A)}$$

This ratio is mathematically well-defined only when $P(A) > 0$. However, suppose a rational agent is deliberating between two actions, $A_1$ and $A_2$, and realizes early in deliberation that $A_2$ is foolish—or suppose the agent is a deterministic program that knows it will definitely output $A_1$. Then the agent's credence that they will perform $A_2$ drops to $P(A_2) = 0$. If $P(A_2) = 0$, then $P(O_j \mid A_2) = \frac{0}{0}$ is undefined! How can the agent verify that $V(A_1) > V(A_2)$ if the very certainty of choosing $A_1$ destroys the mathematical definition of $V(A_2)$?

*Operational Proposal:* To make EDT operational across all decision states, we must supplement the source formula with one of two rigorous regularizations:

1. **The Trembling-Hand ($\epsilon$-Perturbation) Regularization:** During deliberation, a physical or computational agent should never assign exact credence $0$ or $1$ to any executable action $A \in \mathcal{A}$. Because of hardware faults, neural noise, or lapses in execution ("trembling hands"), every available action has at least a minuscule probability $\epsilon > 0$ of occurring. By evaluating $V(A)$ in the limit as execution noise vanishes,

   $$V(A) = \lim_{\epsilon \to 0^+} \sum_j P_\epsilon(O_j \mid A) D(O_j),$$

   the conditional probabilities remain strictly well-defined throughout deliberation.
2. **Popper–Rényi Primitive Conditional Probability:** Alternatively, instead of Kolmogorov's ratio definition, one can adopt a Popper–Rényi probability space $(\Omega, \mathcal{F}, \mathcal{F}_0, P(\cdot \mid \cdot))$, where conditional probability $P(E \mid C)$ is taken as the primitive axiomatic term for all conditioning events $C \in \mathcal{F}_0$ (which includes all feasible actions $\mathcal{A}$, even if $P(A \mid \Omega) = 0$). In this framework, $P(S_i \mid A)$ represents the agent's dispositional evidential update rule upon learning $A$, which remains intact even when $P(A) = 0$.

### 4.2 Dynamic Consistency and the Sleeping Beauty Problem

*The Open Question:* The source notes that EDT has been applied to the **Sleeping Beauty problem** to avoid **Dutch book arguments** (sequences of bets that guarantee a net loss across time), but cites Vincent Conitzer (2015), who argues that "halfers" remain vulnerable to Dutch books even under EDT. Why do sequential problems like Sleeping Beauty create trouble for EDT, and how should an agent evaluate multi-stage policies?

*Analysis and Operational Framework:* In the Sleeping Beauty problem, Beauty is put to sleep on Sunday. A fair coin is tossed:
* If **Heads**, she is awakened solely on Monday.
* If **Tails**, she is awakened on Monday, given an amnesia-inducing drug that erases her memory of Monday, and awakened again on Tuesday.

Whenever she wakes up, she cannot tell whether it is Monday or Tuesday. What should her credence $P(\text{Heads})$ be upon waking? "Thirders" say $1/3$; "Halfers" say $1/2$ (arguing she learned nothing new about the fair coin since Sunday).

Why does EDT enter the picture here? Because on Monday (or Tuesday), Beauty's *act of accepting a bet* happens inside an awakening. If the coin landed **Tails**, any deterministic betting rule she follows upon waking will be executed **twice** (both Monday and Tuesday), whereas if **Heads**, it will be executed only **once** (Monday). 

For a Causal Decision Theorist, accepting a bet on Monday does *not* cause her to accept the bet on Tuesday (she won't even remember Monday). Thus, a Halfer using CDT evaluates Monday's bet in isolation with $P(\text{Heads}) = 1/2$, leading her to accept bets that lose money twice on Tails for every once they win on Heads—a classic diachronic Dutch book!

If a Halfer switches to EDT, she recognizes that her decision upon waking is *perfectly correlated* with her twin awakening on Tuesday if the coin landed Tails. Just as in the Twin Prisoner's Dilemma, an EDT agent accounts for the fact that deciding to accept a bet now is evidence that she also accepts the bet on the other awakening day if Tails occurred. This evidential correlation rescues Naive Halfers from standard Dutch books.

However, as Conitzer (2015) demonstrates, if the bookie has access to asymmetric information (or offers bets structured carefully across indexical states where Beauty's actions across days can be decorrelated), an EDT Halfer can still be Dutch-booked. 

*Operational Lesson for Sequential Problems:* When applying EDT to multi-stage or self-locating problems, an agent cannot simply treat every local decision node in isolation if their credences violate conditionalization over time. When evaluating a sequential policy $\pi$, the agent must specify the reference class of correlated decision points $\{t_1, t_2, \dots, t_k\}$ that share the same epistemic state $E$, and compute the expected utility of the *joint evidential consequence* of adopting policy $\pi$ upon observing state $E$:

$$V(\pi \mid E) = \sum_{j} P(O_j \mid \text{all instances in } E \text{ execute } \pi, E) D(O_j)$$

### 4.3 Normative Uncertainty and the Evidentialist's Wager

*The Open Question:* Suppose a decision-maker finds CDT's causal intuitions compelling, yet cannot completely rule out the philosophical coherence of EDT. The reference article notes an intriguing argument by MacAskill, Vallinder, Österheld, Shulman, and Treutlein (2021), titled *The Evidentialist's Wager*: even if one assigns a low credence to EDT being the true normative theory of rationality, it may be reasonable to act *as if* EDT were true because EDT involves the correlated actions of many decision-makers, making its stakes much higher than CDT's.

*Mathematical Derivation:* We can formalize the mechanics of this wager using a symmetric collective action problem (such as voting, climate mitigation, or open-source contribution). *(Note: This mathematical model unpacks the two-sentence summary of MacAskill et al., 2021 in the source text.)*

Suppose there are $N$ rational agents facing a symmetric binary choice between Cooperating ($C$) and Defecting ($D$).
* Choosing $C$ imposes a direct personal cost $c > 0$ on the actor, but generates a public benefit $b > 0$ for **every** one of the $N$ agents (including the actor).
* Suppose $b < c < N b$ (for example, $c = 10$, $b = 1$, and $N = 1,000$).

How do CDT and EDT evaluate the difference in expected value between $C$ and $D$ for a single agent $i$?
* **Under CDT**, agent $i$'s action has zero causal influence on the choices of the other $N - 1$ agents. By cooperating, agent $i$ pays cost $c$ and receives only their own causal contribution $b$:

  $$\Delta U = U(C) - U(D) = b - c < 0$$

  Since $b < c$, CDT says Defecting dominates by a margin of $c - b$.
* **Under EDT**, agent $i$'s decision provides diagnostic evidence about how the other $N - 1$ like-minded agents decide. Let $\rho \in (0, 1]$ be the evidential correlation coefficient representing the expected fraction of the remaining $N - 1$ agents whose choice shifts from $D$ to $C$ conditional on agent $i$ choosing $C$:

  $$\rho = P(\text{Agent } k \text{ chooses } C \mid \text{Agent } i \text{ chooses } C) - P(\text{Agent } k \text{ chooses } C \mid \text{Agent } i \text{ chooses } D)$$

  Then the evidential value difference for agent $i$ includes the expected benefits generated by all correlated peers:

  $$\Delta V = V(C) - V(D) = (b - c) + \rho (N - 1) b$$

Now suppose our agent is **normatively uncertain**: they assign a small credence $q \in (0, 1)$ to EDT being the correct decision theory, and a large credence $1 - q$ to CDT being correct. If they maximize expected normative value across the two theories, the meta-expected gain of cooperating over defecting is:

$$\Delta \mathcal{M} = (1 - q) \Delta U + q \Delta V = (1 - q)(b - c) + q \big[ (b - c) + \rho (N - 1) b \big] = (b - c) + q \rho (N - 1) b$$

Hence, the normatively uncertain agent should cooperate ($\Delta \mathcal{M} > 0$) whenever:

$$q \rho (N - 1) b > c - b \iff N > 1 + \frac{c - b}{q \rho b}$$

Using our numerical parameters ($c = 10, b = 1$) with a modest correlation $\rho = 0.2$ and only a $q = 5\%$ credence in EDT ($95\%$ in CDT), the threshold is $N > 1 + \frac{9}{0.05 \times 0.2 \times 1} = 901$. Because $N = 1,000 > 901$, the agent should cooperate! Because CDT only ever counts the causal impact of *one* agent while EDT scales with the size $N$ of the correlated reference class, EDT's stakes swamp CDT's stakes in large-scale collective dilemmas.

---

## 5. Summary Protocol: How to Apply EDT to Unfamiliar Cases

When confronted with a new decision problem, you can apply Evidential Decision Theory systematically by following a five-step operational procedure:

1. **Specify the Action Space and State Space:** List the feasible actions $\mathcal{A} = \{A_1, \dots, A_m\}$ and partition the relevant external environment into mutually exclusive, exhaustive states $\mathcal{S} = \{S_1, \dots, S_n\}$. Ensure each pair $(A_k, S_i)$ suffices to fix the outcome desirability $D(A_k, S_i)$.
2. **Condition on All Pre-Choice Evidence:** Update your prior probability distribution $P$ on all sensory and introspective evidence $T$ available *prior* to the moment of execution (including your own felt inclinations or symptoms). As discussed in Section 3.2, this screens off spurious common-cause confounders that mediate their influence through conscious states.
3. **Determine Diagnostic Likelihoods:** For each state $S_i$ and action $A_k$, evaluate the posterior conditional probability $P(S_i \mid A_k, T)$. Ask: *"If I were to learn that I ultimately chose $A_k$, what would that imply about whether state $S_i$ holds?"* Account for predictors, shared algorithms, or symmetric peers who are likely to mirror or anticipate your reasoning. (If $P(A_k) = 0$, apply an $\epsilon$-trembling-hand perturbation so the conditional probability remains well-defined.)
4. **Compute News Value:** For each action $A_k \in \mathcal{A}$, calculate the evidential expected utility:

   $$V(A_k) = \sum_{i=1}^{n} P(S_i \mid A_k, T) D(A_k, S_i)$$

5. **Select the Most Auspicious Action:** Choose an action $A^* \in \arg\max_{A_k \in \mathcal{A}} V(A_k)$.

---

## 6. Conclusion

Evidential Decision Theory offers a mathematically elegant and philosophically striking perspective on agency. By evaluating actions through standard Bayesian conditionalization $P(O_j \mid A)$ rather than causal interventions $P(A \mathrel{\Box{\rightarrow}} O_j)$, EDT treats decision-making as seamlessly continuous with probabilistic inference. 

While critics like Lewis and Joyce warn against conflating diagnostic auspiciousness with causal efficacy, EDT shines in environments where an agent's reasoning process is transparent to predictors or replicated across symmetric peers. In a world increasingly populated by predictive algorithms, AI clones, and large-scale collective action problems, the ability to recognize yourself as part of a correlated reference class—and to act on the best news—may be one of the most powerful tools in a rational agent's arsenal.

---

## References

* Ahmed, Arif (2021). *Evidential Decision Theory*. Cambridge University Press. ISBN 9781108607865.
* Conitzer, Vincent (2015). "A Dutch book against sleeping beauties who are evidential decision theorists". *Synthese*, 192(9): 2887–2899. doi:10.1007/s11229-015-0691-7.
* Gibbard, Allan; Harper, William L. (1976). *Counterfactuals and Two Kinds of Expected Utility*, pp. 7–8.
* Greene, Preston; Levinstein, Benjamin (2020). "Act Consequentialism without Free Rides". *Philosophical Perspectives*, 34(1): 100–101. doi:10.1111/phpe.12138.
* Joyce, James M. (1999). *The Foundations of Causal Decision Theory*, p. 146. Cambridge University Press.
* Lewis, David (1981). "Causal decision theory". *Australasian Journal of Philosophy*, 59(1): 5–30. doi:10.1080/00048408112340011.
* MacAskill, William; Vallinder, Aron; Österheld, Caspar; Shulman, Carl; Treutlein, Johannes (2021). *The Evidentialist's Wager*. Global Priorities Institute Working Paper.
* Wolpert, David H.; Benford, Gregory (2013). "The lesson of Newcomb's paradox". *Synthese*, 190(9): 1637–1646. doi:10.1007/s11229-011-9899-3.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Task**

I'm solidifying the core objective: crafting a mathematically rigorous yet accessible explanation of Evidential Decision Theory (EDT). The emphasis will be on both formal procedures and their philosophical underpinnings for a technically proficient audience. I'm aiming for a balance of clarity and depth.


**Clarifying the Framework**

I am now focusing on the essay's scope and structure, specifically the word count (2,400–3,000 words). It's crucial to be readable and precise to cover EDT's key aspects: evaluating actions, managing dependencies/counterfactuals, and addressing open questions. I'm prioritizing accessibility for a technically proficient audience, and am contrasting CDT and EDT, including the concept of "news value." I am now focusing on the Gibbard & Harper formulas.


**Analyzing Key Examples**

I'm now examining several thought experiments that illustrate EDT's principles, specifically Newcomb's paradox, the twin prisoner's dilemma, and the Sleeping Beauty problem. By considering these, I'm aiming to showcase how EDT arrives at different recommendations compared to CDT. This involves clarifying the probabilistic calculations involved, and the different value assignments to demonstrate the contrasting decisions prescribed by EDT. I am now prioritizing the Gibbard & Harper formulas.


**Addressing Meta-Decision**

I'm now thinking about the implications of normative uncertainty and meta-decision making, and I'm noting the potential dominance of EDT, even with low initial credence, in situations with correlated decision-makers. My focus includes examining critiques of EDT as "managing the news" and highlighting the concept of causal efficacy versus auspiciousness. I am now trying to bridge the gap between the source's outcome formulation and the standard state-act-outcome tables to assist the reader in practical applications. I'm prioritizing the Gibbard & Harper formulas.


**Operationalizing Deliberation**

I'm now grappling with the operationalization of conditional probabilities, specifically when the prior probability of an action is zero. The standard definition becomes problematic. I need to explain how EDT handles this within deliberation, clarifying this and considering extensions to resolve it. I'm also now analyzing the "smoking gene" and tick defense examples to contrast statistical confounding with predictive correlation.


**Investigating EDT Dynamics**

I'm now investigating dynamic consistency through examples like Sleeping Beauty and Dutch Books, to understand Conitzer's result and evaluate multi-stage policies. I'm also formalizing the mathematical implications of normative uncertainty, highlighting how correlated reference classes amplify expected value in EDT compared to CDT, as shown in MacAskill et al. (2021). I'm structuring the essay to highlight the core tension between causing desired futures and selecting actions that strongly *evidence* a desirable world, presenting the formal architecture of EDT.


**Formalizing Probabilities**

I'm now detailing the Gibbard & Harper (1976) equations and their components. I'm focusing on clarifying the algebra of events and conditional probability, and contrasting it with the counterfactual probability. Importantly, I'm extending the outcome-based formula into a State-Act Matrix for practical application. I'll define mutually exclusive states and acts, showing the connection between conditional and counterfactual probabilities, and highlighting when EDT and CDT align.


**Expanding the Framework**

I am now focusing on expanding the framework, specifically looking at the decision to one-box or two-box in Newcomb's problem based on parameters established by (Wolpert & Benford, 2013; Ahmed, 2021). I'm deriving the indifference threshold where EDT switches strategies. I'm also formalizing Aomame's decision in the Twin Prisoner's Dilemma, showing how EDT achieves the Pareto-efficient outcome through evidential symmetry. I am aiming to generalize this with partial correlation.



**Addressing Edge Cases**

I'm now focusing on a specific edge case. I'm tackling situations where actions have zero prior probability. Standard probability breaks, so I'm investigating operational solutions: Rényi-Popper conditionals, or trembling-hand $\epsilon$-perturbations during deliberation to resolve this. I'm also planning to explore how to handle the "bad action" and "bad outcome" with a causal relief example.


**Refining Conclusions**

I'm now outlining a concluding section, aiming for a step-by-step application protocol for EDT in new problems, followed by reflection. I'm incorporating the role of self-locating credences and sequential policies by discussing Conitzer (2015). I am also formalizing MacAskill et al. (2021) to show the advantage of EDT even with low initial credence in situations with correlated decision-makers, and Dutch Books. I'm targeting about 200 words.


**Formalizing Definitions**

I am now structuring the derivation to ensure an optimal word count of around 2,600–2,800. I'm focusing on the clear demarcation between source material and original derivations, and clarifying mathematical notations, and am focusing on state-space decompositions.


**Calculating Expected Value**

I am now focusing on the value of actions using formulas. I've broken down expected value calculations for EDT and CDT, clarifying the posterior vs. counterfactual probability weighting. I'm using a generalized Newcomb's Paradox to showcase the differences, defining parameters and establishing how EDT uses the posterior probability to choose between actions.


**Analyzing the Model**

I'm now generalizing the mathematical model for EDT. Specifically, I am now calculating the conditions for one-boxing in Newcomb's problem, and finding the indifference threshold to show how EDT switches strategies. I'm also analyzing the Twin Prisoner's Dilemma with a correlation parameter, focusing on the payoff matrix and the exact condition where cooperation becomes the dominant strategy.


```
