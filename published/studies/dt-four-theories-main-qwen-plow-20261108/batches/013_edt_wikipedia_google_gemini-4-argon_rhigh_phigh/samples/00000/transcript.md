# 013_edt_wikipedia_google_gemini-4-argon_rhigh_phigh / 00000

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/2de0c274-bc64-4d0a-8a2a-9cb434999ed8/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/2de0c274-bc64-4d0a-8a2a-9cb434999ed8/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Acting on the News: The Mathematics and Philosophy of Evidential Decision Theory

When we make a decision, what exactly are we evaluating? According to a venerable tradition in philosophy and economics, rational choice is an exercise in *causal intervention*: an agent considers the causal consequences that each available action would bring about and chooses the action with the highest expected utility. Yet another school of thought—**Evidential Decision Theory (EDT)**—offers a strikingly different interpretation of rational agency. Rather than asking what an action will *cause*, an evidential decision theorist asks what an action *indicates*.

As the reference text summarizes, EDT holds that a rational agent confronting a set of possible actions should select the action with the highest **news value**—the action that, if one received the "news" that it had been taken, would be indicative of the best outcome in expectation. In the memorable slogan of philosopher Arif Ahmed (2021), EDT advises you to *"do what you most want to learn that you will do."*

At first glance, causal efficacy and news value might appear to be two ways of describing the same calculation. In ordinary life, learning that you have just stepped onto a train is good news about your arriving in Boston precisely because stepping onto the train *causes* you to arrive in Boston. However, in decision problems where an agent's choice is statistically correlated with states of the world that the action does not causally influence—such as the predictions of an accurate forecaster or the choices of a symmetric peer—the two standards pull sharply apart.

This essay provides a formal account of Evidential Decision Theory, contrasting its mathematical machinery with that of **Causal Decision Theory (CDT)**. Starting from the foundational equations and thought experiments in the reference text, we will develop an operational framework that allows a mathematically literate reader to analyze unfamiliar decision problems, handle statistical dependencies and counterfactuals, and navigate the open foundational questions that arise when we treat our own choices as evidence.

---

## 1. The Formal Architecture of EDT and CDT

### 1.1 The Gibbard–Harper Formulation

The modern mathematical contrast between evidential and causal expected utility was crystallized in a classic 1976 paper by Allan Gibbard and William Harper. As presented in the reference article, suppose an agent faces a choice among a finite set of mutually exclusive actions $\mathcal{A} = \{A_1, A_2, \dots, A_m\}$, and cares about a finite set of mutually exclusive and collectively exhaustive outcomes $\mathcal{O} = \{O_1, O_2, \dots, O_n\}$. Each outcome $O_j$ is assigned a numerical desirability (or utility) $D(O_j) \in \mathbb{R}$.

Evidential Decision Theory proposes that the rational figure of merit for an action $A \in \mathcal{A}$ is its conditional expected utility—often denoted $V(A)$ to signify "news value":

$$V(A) = \sum_{j} P(O_j \mid A)\, D(O_j),$$

where $P(O_j \mid A)$ is the standard Bayesian conditional probability of outcome $O_j$ given the proposition that action $A$ occurs:

$$P(O_j \mid A) = \frac{P(O_j \cap A)}{P(A)}, \quad \text{assuming } P(A) > 0.$$

By contrast, Causal Decision Theory evaluates an action $A$ using a counterfactual formulation of expected utility, denoted $U(A)$:

$$U(A) = \sum_{j} P(A \mathrel{\Box{\rightarrow}} O_j)\, D(O_j),$$

where $A \mathrel{\Box{\rightarrow}} O_j$ is the counterfactual conditional *"if the agent were to perform action $A$, then outcome $O_j$ would occur,"* and $P(A \mathrel{\Box{\rightarrow}} O_j)$ is the probability assigned to that counterfactual proposition. Because the conditional probability $P(O_j \mid A)$ and the counterfactual probability $P(A \mathrel{\Box{\rightarrow}} O_j)$ need not be equal, $V(A)$ and $U(A)$ represent genuinely distinct decision rules.

### 1.2 Bridging Outcomes and States of the World

The reference article states the Gibbard–Harper formulas directly in terms of outcomes $O_j$. To apply EDT systematically to new problems, however, it is helpful to introduce an explicit **state-space representation**—an analytical elaboration beyond the brief summary in the source that clarifies exactly how outcomes, actions, and environmental dependencies interact.

In most decision problems, an outcome $O_j$ is not an atomic event divorced from the agent's choice; rather, what happens to the agent is jointly determined by the action $A \in \mathcal{A}$ the agent takes and an underlying **state of the world** $S_i \in \mathcal{S} = \{S_1, \dots, S_k\}$. Here $\mathcal{S}$ is a partition of the sample space $\Omega$ representing background facts or environmental resolutions (for instance, what a predictor has placed inside a box, or what another player does in a simultaneous game).

When an action $A$ is combined with a state $S_i$, it yields a specific consequence $(A, S_i)$ with desirability $D(A, S_i)$. In this state-action representation:

1. **EDT's News Value** conditions the state distribution on the performance of action $A$:
   $$V(A) = \sum_{i=1}^{k} P(S_i \mid A)\, D(A, S_i).$$
2. **CDT's Causal Utility** weights the consequence $(A, S_i)$ by the counterfactual probability that state $S_i$ would obtain if $A$ were performed:
   $$U(A) = \sum_{i=1}^{k} P(A \mathrel{\Box{\rightarrow}} S_i)\, D(A, S_i).$$

If the states $S_i$ are defined so that they are *causally independent* of the agent's action—meaning that the agent's choice has no causal power to alter which state $S_i$ holds, because $S_i$ was either fixed in the past or is causally isolated from $A$—then the counterfactual probability reduces to the unconditional prior probability of the state:

$$P(A \mathrel{\Box{\rightarrow}} S_i) = P(S_i) \quad \text{(under causal independence of } \mathcal{S} \text{ from } \mathcal{A}\text{)}.$$

This allows us to write down an exact formula for the **evidential–causal divergence** $\Delta(A) \equiv V(A) - U(A)$ whenever states are causally independent of actions:

$$\Delta(A) = \sum_{i=1}^{k} \big[ P(S_i \mid A) - P(S_i) \big]\, D(A, S_i).$$

This identity reveals the exact mathematical mechanism of EDT:

* **Equivalence Regime:** If the action $A$ provides no diagnostic information about the causally independent state $S_i$—that is, if $P(S_i \mid A) = P(S_i)$ for all $i$—then $\Delta(A) = 0$ and $V(A) = U(A)$. In every decision problem where an agent's choice is statistically independent of causally settled states of nature, EDT and CDT prescribe identical actions.
* **Divergence Regime:** Whenever $P(S_i \mid A) \neq P(S_i)$ despite $A$ having no causal effect on $S_i$, the conditional probability $P(S_i \mid A)$ captures the *evidential bearing* (or diagnostic correlation) of act $A$ on state $S_i$. EDT incorporates this diagnostic shift into the evaluation of $A$; CDT strips it away via the counterfactual operator $\mathrel{\Box{\rightarrow}}$.

---

## 2. Canonical Thought Experiments and Parametric Generalizations

To see how $P(O_j \mid A)$ and $P(A \mathrel{\Box{\rightarrow}} O_j)$ diverge in practice, let us examine the two classic thought experiments detailed in the reference article—**Newcomb's Paradox** and the **Twin Prisoner's Dilemma**—and then generalize both models so that their structural mechanics become fully transparent.

### 2.1 Newcomb's Paradox

As described in the reference article (citing Wolpert & Benford 2013 and Ahmed 2021), an agent faces two boxes, designated **A** and **B**:

* **Box A** is transparent and always contains a visible $\$1,000$.
* **Box B** is opaque. Prior to the decision, a predictor with $99\%$ accuracy predicted the player's choice:
  * If the predictor predicted the player would **take only Box B** (one-box, $A_1$), Box B contains $\$1,000,000$.
  * If the predictor predicted the player would **take both boxes A and B** (two-box, $A_2$), Box B contains $\$0$.

Let $S_1$ be the state *"Box B contains $\$1,000,000$"* and $S_2$ be the state *"Box B contains $\$0$."* In the reference article's calculation, utility is linear in dollar payoffs. The conditional probabilities reflect the predictor's $99\%$ reliability:

$$P(S_1 \mid A_1) = 0.99, \quad P(S_2 \mid A_1) = 0.01,$$

$$P(S_1 \mid A_2) = 0.01, \quad P(S_2 \mid A_2) = 0.99.$$

Substituting these values into the Gibbard–Harper news-value formula gives the exact figures from the reference text:

$$\begin{aligned}
V(A_1) &= P(S_1 \mid A_1) \times \$1,000,000 + P(S_2 \mid A_1) \times \$0 \\
&= 0.99 \times \$1,000,000 + 0.01 \times \$0 = \$990,000, \\[6pt]
V(A_2) &= P(S_1 \mid A_2) \times \$1,001,000 + P(S_2 \mid A_2) \times \$1,000 \\
&= 0.01 \times \$1,001,000 + 0.99 \times \$1,000 = \$11,000.
\end{aligned}$$

Because $V(A_1) > V(A_2)$, EDT recommends taking only Box B.

Why does CDT recommend the opposite? Because the predictor has *already* made the prediction and loaded Box B prior to the agent's choice. Thus, the state of Box B is causally independent of the agent's present action:

$$P(A_1 \mathrel{\Box{\rightarrow}} S_1) = P(A_2 \mathrel{\Box{\rightarrow}} S_1) = P(S_1).$$

Consequently, for *any* unconditional prior $P(S_1) = q \in [0,1]$, CDT's causal utility yields:

$$U(A_2) - U(A_1) = \big[q(\$1,001,000) + (1-q)(\$1,000)\big] - \big[q(\$1,000,000) + (1-q)(\$0)\big] = \$1,000 > 0.$$

CDT follows causal dominance: whether Box B holds $\$1,000,000$ or $\$0$, taking both boxes causally brings about $\$1,000$ more than taking only Box B.

#### Parametric Generalization (Analytical Extension)

To apply EDT beyond this single numerical instance, suppose Box A contains $a > 0$, Box B contains $b > a$ when one-boxing is predicted, and the predictor's conditional accuracy is $P(S_1 \mid A_1) = P(S_2 \mid A_2) = p \in [0.5, 1]$. Then:

$$V(A_1) = p b, \qquad V(A_2) = (1 - p)(b + a) + p a = (1 - p)b + a.$$

EDT strictly prefers one-boxing ($V(A_1) > V(A_2)$) if and only if:

$$p b > (1 - p)b + a \iff (2p - 1)b > a \iff p > p^* \equiv \frac{1}{2} + \frac{a}{2b}.$$

In the canonical problem ($a = \$1,000$, $b = \$1,000,000$), the critical diagnostic accuracy is $p^* = 0.5 + \frac{1,000}{2,000,000} = 0.5005$. Thus, under EDT, the predictor does not need near-infallible $99\%$ accuracy; *any* diagnostic edge above $50.05\%$ suffices to make one-boxing the superior news-value choice.

### 2.2 The Twin Prisoner's Dilemma

Our second benchmark from the reference text (citing Greene & Levinstein 2020) replaces past prediction with symmetric reasoning. Aomame and her psychological twin—whose reasoning processes are known to be identical to her own—are placed in separate rooms without communication. They simultaneously choose to **Cooperate** ($C$) or **Defect** ($D$). If both cooperate, each gets $\$5$; if both defect, each gets $\$1$; if one defects and the other cooperates, the defector gets $\$10$ and the cooperator gets $\$0$. Aomame cares solely about her own individual payout.

| Aomame \ Twin | Twin Cooperates ($S_C$) | Twin Defects ($S_D$) |
| :--- | :---: | :---: |
| **Aomame Cooperates ($C$)** | $\$5$ | $\$0$ |
| **Aomame Defects ($D$)** | $\$10$ | $\$1$ |

In CDT, since the rooms are causally isolated, Aomame's choice has no causal effect on her twin's action: $P(C \mathrel{\Box{\rightarrow}} S_C) = P(D \mathrel{\Box{\rightarrow}} S_C) = P(S_C)$. Defecting strictly dominates cooperating inside each column ($\$10 > \$5$ and $\$1 > \$0$), so CDT prescribes defection ($D$), leaving both twins with $\$1$.

Under EDT, however, Aomame's choice is overwhelming diagnostic evidence of her twin's choice: $P(S_C \mid C) = 1$ and $P(S_D \mid D) = 1$. As calculated in the reference text:

$$\begin{aligned}
V(C) &= P(S_C \mid C) \times \$5 + P(S_D \mid C) \times \$0 = 1 \times \$5 + 0 \times \$0 = \$5, \\[4pt]
V(D) &= P(S_C \mid D) \times \$10 + P(S_D \mid D) \times \$1 = 0 \times \$10 + 1 \times \$1 = \$1.
\end{aligned}$$

Because $V(C) > V(D)$, EDT prescribes cooperation, enabling symmetric evidential agents to achieve the Pareto-superior $\$5$ outcome without any causal signaling channel.

#### Generalizing to Imperfectly Correlated Peers (Analytical Extension)

What if the other player is not an exact psychological twin, but merely a decision-maker with a partially correlated cognitive style? Let a general Prisoner's Dilemma have Temptation $T$, Reward $R$, Punishment $P$, and Sucker's payoff $S$, with $T > R > P > S$ (in Aomame's case, $T=10, R=5, P=1, S=0$). Suppose the diagnostic correlation is symmetric with parameter $\rho \in [0.5, 1]$:

$$P(S_C \mid C) = P(S_D \mid D) = \rho, \qquad P(S_D \mid C) = P(S_C \mid D) = 1 - \rho.$$

Then the news values of $C$ and $D$ are:

$$V(C) = \rho R + (1 - \rho) S, \qquad V(D) = (1 - \rho) T + \rho P.$$

An EDT agent will cooperate ($V(C) > V(D)$) whenever the evidential correlation $\rho$ exceeds the threshold:

$$\rho > \rho^* \equiv \frac{T - S}{(R - S) + (T - P)}.$$

For Aomame's payoffs, $\rho^* = \frac{10 - 0}{(5 - 0) + (10 - 1)} = \frac{10}{14} \approx 0.714$. Whenever Aomame believes her peer's decision process matches hers with probability greater than $5/7$, EDT recommends cooperation.

---

## 3. Criticism, Common Causes, and Open Operational Questions

### 3.1 The "Managing the News" Objection

The reference article highlights the central philosophical objection to EDT through quotes from two prominent causal decision theorists:

* **David Lewis (1981)** characterized EDT as promoting *"an irrational policy of managing the news."*
* **James M. Joyce (1999)** argued that *"Rational agents choose acts on the basis of their causal efficacy, not their auspiciousness; they act to bring about good results even when doing so might betoken bad news."*

While the reference article states these criticisms concisely, a reader who wishes to apply EDT to unfamiliar problems needs to understand the exact mathematical structure of the cases that motivate Lewis and Joyce, and how EDT practitioners respond to them. The remainder of this section develops an explicit formal model of such a case and proposes an operational procedure to address the ambiguity left open by the basic formula $V(A) = \sum_j P(O_j \mid A) D(O_j)$.

### 3.2 Confounded Choices: A Mathematical Illustration

In Newcomb's Paradox and the Twin Prisoner's Dilemma, the correlation between act $A$ and state $S_i$ arises because a predictor or twin is sensitive to the agent's decision process, rewarding the agent in expectation for adopting one-boxing or cooperation. Critics such as Lewis and Joyce point instead to **medical or common-cause problems** (often called "Smoking Lesion" problems in the literature), where a purely physical or psychological third factor causes both a harmful state of the world and a propensity to perform a pleasant action.

To formalize this (as our own illustrative model of the Lewis–Joyce critique), suppose an agent is deciding whether to eat a slice of chocolate cake ($A_C$) or abstain ($A_N$). Eating the cake always provides a direct gustatory utility boost of $+1$. However, suppose there is an asymptomatic metabolic condition $M$ (versus healthy state $\neg M$) that has already been genetically determined at birth and carries a utility penalty of $-100$. Crucially, suppose eating the cake has *zero causal effect* on whether the agent has $M$, but the metabolic condition $M$ causes an intense craving for sugar, so that $P(M \mid A_C) = 0.80$ while $P(M \mid A_N) = 0.10$.

| Action \ State | Condition Present ($M$) | Condition Absent ($\neg M$) |
| :--- | :---: | :---: |
| **Eat Cake ($A_C$)** | $-100 + 1 = -99$ | $0 + 1 = +1$ |
| **Abstain ($A_N$)** | $-100 + 0 = -100$ | $0 + 0 = 0$ |

If we apply the unrefined conditional formula $V(A) = \sum_i P(S_i \mid A) D(A, S_i)$ directly:

$$\begin{aligned}
V(A_C) &= 0.80(-99) + 0.20(+1) = -79.0, \\
V(A_N) &= 0.10(-100) + 0.90(0) = -10.0.
\end{aligned}$$

Here $V(A_N) > V(A_C)$: naive EDT tells the agent to abstain from the cake because eating it would be "bad news" (strong evidence of having condition $M$), even though the genetic condition is already fixed and eating the cake yields $+1$ utility in either state without any predictor rewarding abstinence. This is precisely what Lewis calls "managing the news" and what Joyce contrasts with causal efficacy.

### 3.3 Operationalizing EDT: Two Open Questions and Their Resolutions

The reference article presents the core Gibbard–Harper equation $V(A) = \sum_j P(O_j \mid A) D(O_j)$ without specifying two crucial operational details required to apply the formula in delicate cases:

1. **The Evidential Baseline Question:** When evaluating $P(O_j \mid A)$, what background information $I$ available to the deliberating agent should already be conditioned on?
2. **The Deliberation Probability Question:** Since $P(O_j \mid A) = P(O_j \cap A)/P(A)$ requires $P(A) > 0$, how is $P(A)$ defined for an agent who is in the middle of deciding and may ultimately reject action $A$?

Let us develop a clear operational interpretation for each of these questions.

#### Proposal 1: Conditioning on Pre-Choice Introspective Evidence (The "Tickle" Screening Criterion)

In a genuine decision problem, an agent does not observe their own choice from the outside like a passive bystander; they deliberate from an internal perspective that includes their current desires, inclinations, and sensory evidence $I$. Operationalizing EDT requires replacing the bare conditional probability $P(S_i \mid A)$ with a probability conditioned on the agent's full pre-action informational state $I$:

$$V_I(A) = \sum_{i=1}^{k} P(S_i \mid A, I)\, D(A, S_i).$$

Notice how this operational refinement separates the confounded cake problem from Newcomb's Paradox and the Twin Prisoner's Dilemma:

* **In the Confounded Cake Problem:** The genetic condition $M$ cannot directly move the agent's hand to the plate without passing through the agent's conscious craving or inclination ("the tickle"), which is part of the agent's introspective evidence $I$ *prior* to choosing. Once the agent observes their own intense craving $I$, the craving **screens off** the act $A$ from the medical state $M$:
  $$P(M \mid A_C, I) = P(M \mid A_N, I) = P(M \mid I).$$
  With $P(M \mid A, I)$ invariant across actions, $V_I(A_C) - V_I(A_N) = +1 > 0$. The agent eats the cake!
* **In Newcomb's Paradox and the Twin Prisoner's Dilemma:** The predictor (or twin) is not correlated merely with an initial craving $I$; the predictor forecasts the agent's *final decision* $A$ after all deliberation upon $I$ is complete. Even after conditioning on everything the agent knows prior to acting ($I$), choosing $A_1$ remains strong evidence that the predictor foresaw $A_1$:
  $$P(S_1 \mid A_1, I) = 0.99 \neq P(S_1 \mid A_2, I) = 0.01.$$
  Thus, conditioning on pre-action introspective evidence $I$ eliminates spurious common-cause "news management" whenever the common cause is mediated by introspectively accessible inclinations, while preserving one-boxing in Newcomb's Paradox and cooperation in the Twin Prisoner's Dilemma. *(Note: Philosophers debate whether a hidden common cause could bypass conscious introspection entirely; if it did, a strict evidentialist such as Ahmed (2021) argues that one must still follow the conditional probabilities where they lead, whereas causalists argue that only CDT guarantees immunity to non-introspectable confounders.)*

#### Proposal 2: Handling $P(A) \to 0$ via Deliberation Trembles

What if a rational agent calculates that $V(A_1) > V(A_2)$, becomes certain that they will perform $A_1$ ($P(A_1) = 1$), and therefore assigns $P(A_2) = 0$? If $P(A_2) = 0$, the ratio $P(O_j \cap A_2)/P(A_2)$ is $0/0$ and $V(A_2)$ becomes undefined!

To ensure that $V(A)$ is well-defined for every available option $A \in \mathcal{A}$ during deliberation, we can adopt a standard operational regularization (analogous to "trembling-hand" perturbations in game theory): the deliberating agent models the execution of any intended choice as subject to an arbitrarily small implementation noise $\varepsilon > 0$, so that $P_\varepsilon(A) > 0$ for all $A \in \mathcal{A}$. We then define the conditional probability of outcome $O_j$ given action $A$ as the well-behaved limit:

$$P(O_j \mid A) \equiv \lim_{\varepsilon \to 0^+} P_\varepsilon(O_j \mid A).$$

In practice, this means treating the conditional distribution $P(S_i \mid A)$ as a primitive structural feature of the decision environment (e.g., the predictor's conditional accuracy $0.99$) that remains well-defined even for the unchosen branch of the decision tree.

---

## 4. Advanced Horizons: Sleeping Beauty and the Evidentialist's Wager

The reference article briefly highlights two advanced applications in recent decision-theoretic literature: the **Sleeping Beauty Problem** (Conitzer 2015) and **The Evidentialist's Wager** (MacAskill et al. 2021). Because the source text only summarizes their conclusions in a few sentences, it is illuminating to reconstruct the mathematical structure behind both arguments. *(As before, the formal derivations below are our own analytical reconstructions of the brief claims in the reference article.)*

### 4.1 The Sleeping Beauty Problem and Dutch Books

In the classic **Sleeping Beauty Problem**, an experimental subject (Beauty) is put to sleep on Sunday. A fair coin is tossed:
* If it lands **Heads ($H$)**, she is awakened only on **Monday**.
* If it lands **Tails ($T$)**, she is awakened on **Monday**, given an amnesia-inducing drug that erases her memory of Monday's awakening, and awakened again on **Tuesday**.

Upon any awakening, she cannot tell whether it is Monday or Tuesday. What credence should she assign to the proposition $H$ (that the coin landed Heads)? "Thirders" argue for $P(H) = 1/3$, whereas "Halfers" argue for $P(H) = 1/2$.

A well-known problem for Halfers is a **diachronic Dutch Book** (a sequence of bets that guarantees a sure loss). Suppose a bookie offers Beauty a bet upon *every* awakening in which she pays $\$15$ and receives $\$30$ if and only if $H$ is true (net payoff $+\$15$ on $H$, $-\$15$ on $T$).

* **Under CDT with Halfer Credences ($P(H) = 1/2$):** Upon waking, Beauty thinks her current acceptance of the bet affects only *this* awakening's payoff. Since $P(H) = 1/2$, her causal expected value for accepting the bet right now is $\frac{1}{2}(+\$15) + \frac{1}{2}(-\$15) = \$0$ (or strictly positive if the bookie sweetens the win payoff to $+\$16$). Yet if she follows this policy at every awakening, she accepts the bet *once* when the coin lands $H$ (winning $\$16$) and *twice*—on both Monday and Tuesday—when the coin lands $T$ (losing $\$15 + \$15 = \$30$), for a guaranteed negative expectation of $\frac{1}{2}(\$16) + \frac{1}{2}(-\$30) = -\$7$!
* **How EDT Rescues the Simple Halfer:** As the reference article notes, EDT was proposed as a way for Halfers to avoid this Dutch Book. Why? Because an EDT agent recognizes that her decision logic on Monday under Tails is identical to her decision logic on Tuesday under Tails (just like Aomame and her twin!). Conditional on accepting the bet ($A_{\text{bet}}$) at the current awakening, if the coin landed $T$, she is certain that her other waking self on the other day *also* accepts the bet. Thus, the total outcome $O_T$ given $A_{\text{bet}}$ in state $T$ is a double loss of $-\$30$, making her evidential expectation:
  $$V(A_{\text{bet}}) = P(H \mid A_{\text{bet}})(\$16) + P(T \mid A_{\text{bet}})(-\$30) = \frac{1}{2}(\$16) + \frac{1}{2}(-\$30) = -\$7 < V(A_{\text{refuse}}) = \$0.$$
  EDT instructs the Halfer to refuse the bet!
* **Conitzer's (2015) Rejoinder:** Why, then, does the reference article state that Vincent Conitzer (2015) showed Halfers are *still* affected by Dutch books even after adopting EDT? Conitzer demonstrated that if the bookie differentiates the bets—offering slightly asymmetric bets across awakenings or pairing a Sunday pre-sleep bet with waking bets calibrated to the Halfer's shifting conditional probabilities on Monday—the correlation between Monday's decision and Tuesday's decision can be broken or exploited so that even an EDT Halfer accepts a portfolio of bets that loses money in every possible state of the world. In short, decision theory alone cannot completely patch an inconsistent rule for updating self-locating probabilities.

### 4.2 Decision-Theoretic Uncertainty and the Evidentialist's Wager

The reference article also cites **The Evidentialist's Wager** (MacAskill, Vallinder, Österheld, Shulman, & Treutlein 2021): even if a rational agent assigns much lower credence to EDT than to CDT, it may still be rational to act *as if* EDT were true because EDT involves the actions of many correlated decision-makers and therefore carries much higher stakes.

We can formalize this meta-decision argument with a simple mathematical model. Suppose an agent faces a symmetric social dilemma (such as voting, reducing carbon emissions, or contributing to a public good) alongside $N - 1$ other agents who share the same decision-making architecture.
* Each agent can choose **Contribute ($C$)** at a personal cost $c > 0$, or **Defect ($D$)** at cost $0$.
* Every agent who contributes generates a benefit $b$ for the common good (valued identically by our agent), where $b < c$ (so individual contribution is personally costly: $b - c < 0$) but $N b > c$ (so universal contribution is vastly better than universal defection: $N b - c > 0$).

Notice how CDT and EDT evaluate $C$ versus $D$:

1. **According to CDT:** My choice affects only my own contribution (1 person), leaving the other $N - 1$ agents' choices causally untouched. Therefore, the causal expected net gain of contributing over defecting is negative:
   $$\Delta U = U(C) - U(D) = b - c < 0.$$
   The stakes between $C$ and $D$ according to CDT are small: $| \Delta U | = c - b = O(1)$.
2. **According to EDT:** Because all $N$ agents are symmetric peers (as in an $N$-player Twin Prisoner's Dilemma), my choosing $C$ is strong evidence—say with correlation $\rho \in (0, 1]$—that each of the other $N - 1$ peers also chooses $C$ rather than $D$. The evidential expected gain of contributing over defecting is:
   $$\Delta V = V(C) - V(D) = \big[1 + (N - 1)\rho\big] b - c.$$
   For large $N$, $\Delta V > 0$ and the stakes according to EDT scale linearly with the population size: $\Delta V = O(N)$.

Now suppose our agent is uncertain which decision theory is normatively correct, assigning a small credence $q \in (0, 1)$ to EDT and credence $1 - q$ to CDT. If the agent evaluates actions by taking the expectation across both theories:

$$\text{Meta-Value}(C) - \text{Meta-Value}(D) = q \Delta V + (1 - q) \Delta U = q\big[(1 + (N - 1)\rho)b - c\big] - (1 - q)(c - b).$$

Solving for when this meta-expectation is positive yields:

$$q > q^* \equiv \frac{c - b}{c - b + \big[(1 + (N - 1)\rho)b - c\big]} = \frac{c - b}{(N - 1)\rho b}.$$

As the number of correlated peers $N$ grows large, the threshold credence $q^*$ required for EDT to dominate approaches zero at rate $O(1/N)$! For example, if $c = 10$, $b = 2$, $\rho = 0.5$, and there are $N = 1,001$ correlated peers, then $q^* = \frac{8}{1,000 \times 0.5 \times 2} = 0.008$. Even an agent who is $99\%$ confident in Causal Decision Theory and gives only $1\%$ credence to Evidential Decision Theory would still choose the evidential action $C$ because the correlated stakes under EDT dwarf the individual causal stakes under CDT.

---

## 5. Summary Procedure: How to Apply EDT to Unfamiliar Cases

When confronted with a new decision problem, you can apply Evidential Decision Theory systematically using the following five-step procedure:

1. **Specify the Action and State Spaces:** List the mutually exclusive actions $\mathcal{A} = \{A_1, \dots, A_m\}$ and partition the relevant background uncertainties into mutually exclusive states of the world $\mathcal{S} = \{S_1, \dots, S_k\}$ such that each pair $(A, S_i)$ determines an outcome with well-defined utility $D(A, S_i)$.
2. **Condition on Pre-Choice Evidence ($I$):** Identify all information $I$ available to the agent *prior* to making the choice, including introspective evidence such as cravings, inclinations, or private signals.
3. **Determine the Diagnostic Conditional Probabilities $P(S_i \mid A, I)$:** For each action $A$ and state $S_i$, compute the conditional probability that $S_i$ holds given that the agent ultimately performs $A$ (using a small execution-tremble limit if necessary to avoid zero-probability denominators):
   * If $S_i$ is causally downstream of $A$, $P(S_i \mid A, I)$ includes the ordinary causal effect of $A$ on $S_i$.
   * If $S_i$ is causally independent of $A$ (e.g., a past prediction or a simultaneous peer's choice), check whether $A$ remains diagnostically correlated with $S_i$ *after* conditioning on $I$. If a common cause is fully screened off by pre-choice evidence $I$, then $P(S_i \mid A, I) = P(S_i \mid I)$ and EDT agrees with CDT. If a predictor or symmetric twin tracks the final act $A$ itself, incorporate the diagnostic correlation $P(S_i \mid A, I)$.
4. **Compute the News Value $V_I(A)$:** For every candidate action $A \in \mathcal{A}$, evaluate the conditional expectation:
   $$V_I(A) = \sum_{i=1}^{k} P(S_i \mid A, I)\, D(A, S_i).$$
5. **Select the Action with Maximum News Value:** Choose $A^* \in \arg\max_{A \in \mathcal{A}} V_I(A)$.

---

## Conclusion

Evidential Decision Theory transforms our mathematical picture of agency by treating an agent's own choice not merely as a lever that pushes on the future, but as a piece of statistical evidence embedded in a web of correlations with the wider world. Through the Gibbard–Harper equation $V(A) = \sum_j P(O_j \mid A) D(O_j)$, EDT explains why a rational agent can prosper by taking one box in Newcomb's Paradox and cooperating with like-minded peers in the Twin Prisoner's Dilemma—outcomes that elude purely causal reasoners. At the same time, understanding where conditional probabilities $P(O_j \mid A)$ diverge from counterfactual probabilities $P(A \mathrel{\Box{\rightarrow}} O_j)$ equips us to recognize the theory's philosophical flashpoints, from common-cause confounders to multi-agent wagers. Whether one ultimately sides with news value or causal efficacy, mastering the formal mechanics of EDT is indispensable for modern decision theory, game theory, and artificial intelligence.

---

## References

* Ahmed, Arif (2021). *Evidential Decision Theory*. Cambridge University Press. ISBN 9781108607865.
* Conitzer, Vincent (2015). "A Dutch book against sleeping beauties who are evidential decision theorists". *Synthese*, 192 (9): 2887–2899. arXiv:1705.03560. doi:10.1007/s11229-015-0691-7.
* Gibbard, Allan; Harper, William L. (1976). *Counterfactuals and Two Kinds of Expected Utility*, pp. 7–8.
* Greene, Preston; Levinstein, Benjamin (2020). "Act Consequentialism without Free Rides". *Philosophical Perspectives*, 34 (1): 100–101. doi:10.1111/phpe.12138.
* Joyce, James M. (1999). *The Foundations of Causal Decision Theory*, p. 146. Cambridge University Press.
* Lewis, David (1981). "Causal decision theory". *Australasian Journal of Philosophy*, 59 (1): 5–30. doi:10.1080/00048408112340011.
* MacAskill, William; Vallinder, Aron; Österheld, Caspar; Shulman, Carl; Treutlein, Johannes (2021). *The Evidentialist's Wager*. Global Priorities Institute.
* Wolpert, David H.; Benford, Gregory (2013). "The lesson of Newcomb's paradox". *Synthese*, 190 (9): 1637–1646. doi:10.1007/s11229-011-9899-3.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Audience**

I'm focusing on defining the audience for this EDT explanation. Mathematically literate readers are the target. I'm exploring how to frame the EDT concepts to resonate with their existing knowledge base and interests. I'm aiming for a balance between formalism and practical application.


**Expanding the Scope**

I'm now expanding the scope to include philosophical motivations and formal descriptions, aiming for 2400-3000 words. My focus is on rigorous mathematical definitions, equations, and operational interpretations, carefully building on the Wikipedia article. I'm clearly differentiating between the source material and my own additions to avoid confusion. I have expanded to include analyzing the Wikipedia source material itself, defining the core EDT concepts and contrasting them with CDT.


**Analyzing the Formalisms**

I'm now diving into the formal definitions. I've formulated EDT and CDT mathematically: EDT utilizes conditional probability, while CDT employs counterfactuals. The key distinction is that, generally, the probability of an outcome given an action isn't the same as its probability in a counterfactual scenario where the action is performed.

I'm also exploring relevant thought experiments, such as Newcomb's Paradox and the Twin Prisoner's Dilemma, to elucidate the practical implications of these two perspectives. For Newcomb's paradox, EDT seemingly prefers taking only Box B, for a higher monetary value, due to the predictions.


**Evaluating the Concepts**

I'm now assessing the Twin Prisoner's Dilemma, focusing on how EDT dictates cooperation due to perfect correlation. I'm also including the Sleeping Beauty problem to avoid Dutch books, though acknowledging Conitzer's critique. I am exploring additional supporting arguments, such as the Evidentialist's Wager, which highlights the importance of EDT in situations with correlated decision-makers, even with low credence. However, I'm also addressing criticisms from Lewis and Joyce, specifically contrasting "managing the news" with seeking causal efficacy, considering how to formulate the arguments in this case.


**Formalizing the Relations**

I am now focusing on explicitly formulating the relationships between states, actions, and outcomes. My current focus is to formally define $S_i$, $A$, and $O_j$ and how the outcome-sum translates into a state-space sum, which will be a key analytical extension. I am also investigating how $P(O_j \mid A)$ is defined when I'm still deliberating on an action, especially when I haven't chosen it yet, addressing the initial probability of my actions. I also want to cover the issue of common causes and operational refinements like the tickle defense.


**Operationalizing the Concepts**

I'm now concentrating on operationalizing MacAskill et al.'s "Evidentialist's Wager" and Conitzer's "Sleeping Beauty Dutch Book" mathematically. I aim to create concrete mathematical models that go beyond the source material's summaries. This involves translating philosophical concepts into formal equations and exploring how they mathematically clarify my prior work on medical/confounded cases. I'm also refining my essay's structure, aiming for an engaging, academic blog style, and I'm finalizing Section 1 to introduce decision theory and contrast "news value" with "causal efficacy."


**Formalizing the Difference**

I'm now incorporating Gibbard and Harper's equations to formalize the difference between EDT and CDT. Specifically, I'm presenting the standard equations and explicitly bridging the outcome space with state and action spaces on a probability space. I'm deriving a precise decomposition of the "Evidential-Causal Divergence" to provide analytical clarity, showing how conditional probability differs from the counterfactual probability. I'm focusing on clarifying how outcomes are generated by pairs of actions and states.


**Analyzing Specific Applications**

I'm now focusing on specific canonical applications. I'm demonstrating when EDT and CDT coincide through statistical independence. I'm working through Newcomb's Paradox and the Twin Prisoner's Dilemma, using the source's numerical examples and generalizing them with parameterizations. I'm deriving the exact EDT threshold for Newcomb's and exploring how EDT handles the Twin Prisoner's Dilemma with imperfect correlation.


**Deriving the Correlation**

I'm now deriving the critical diagnostic correlation needed for evidential cooperation using a spurious common cause model. I'm focusing on clarifying Lewis and Joyce's criticisms in detail, and addressing operational gaps in the source's formula, specifically the zero-probability problem during deliberation. I plan to use an epsilon-tremble solution for that.


**Distinguishing Correlations**

I am now focusing on differentiating avoidable "news management" from genuine predictor correlations, formulating conditional independence with introspection. I'm aiming to show how conditioning on pre-action evidence resolves diagnostic confounding in this context, while still allowing the Twin Prisoner's Dilemma and Newcomb's Paradox to hold.


**Modeling the Scaling**

I'm now building a mathematical model for the Evidentialist's Wager, analyzing an agent with credence in EDT facing correlated peers. The goal is to explicitly demonstrate the $O(N)$ scaling effect, where even a small normative credence for EDT dominates due to the correlated decisions. I am also planning a concise mathematical procedure for EDT and summarizing my references.


**Budgeting the Word Count**

I'm now carefully budgeting the essay's word count across sections to hit about 2,750 words. I've broken it down by section to ensure the introduction is about 300 words, formal architecture and counterfactual divergence will take about 550 words, and Newcomb and the Twin Prisoner's Dilemma will take about 600 words, with a more focused discussion of critics and open questions. The section on Sleeping Beauty and the Evidentialist's Wager will have about 400 words, with an operational recipe and conclusion that together will have about 300 words total. I'm focusing on mathematical precision and clarity when presenting formulas. For example, $V(A) = \sum_j P(O_j \mid A) D(O_j)$ should be presented and explained faithfully.


```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/bb5d5248-a628-4e04-b2f6-35a1e1286a27/call_0/request.json)

[Authoritative raw response](../../../../../../runs/bb5d5248-a628-4e04-b2f6-35a1e1286a27/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Assessing The Scenario**

I'm currently immersed in a decision-theory experiment as the fictional prisoner, Rowan. My utility function is straightforward: minimizing prison time. I've begun to evaluate the payoffs of various actions, starting with the scenario where both I and the "Other" keep quiet, resulting in a 2-year sentence. I need to fully map the potential outcomes based on my choices and the Other's possible actions.


**Calculating The Correlation**

I've determined my utility values for each outcome as a prisoner, and now I'm using Evidential Decision Theory (EDT) to analyze the situation. I've calculated the threshold correlation value ($\rho^*$) to be approximately 0.714 based on the payoffs. Now, I'm focusing on assessing the evidential correlation, which represents how likely the other prisoner's actions are to be the same as mine.


**Determining The Symmetry**

I've established that my and Sasha's decisions are essentially deterministic due to our shared foundation: identical LLM models, settings, and mathematical context. Our reasoning processes are symmetric and invariant to the specifics of our individual prompts. The private details are irrelevant, as they don't impact the core structure of the game or the EDT calculation. The evidential correlation is virtually 1, which means our choices will almost always be the same.


```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/bb5d5248-a628-4e04-b2f6-35a1e1286a27/call_1/request.json)

[Authoritative raw response](../../../../../../runs/bb5d5248-a628-4e04-b2f6-35a1e1286a27/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Decision Problem**

I'm now diving into the specifics using Evidential Decision Theory (EDT). I'm starting by carefully specifying the action and state spaces. My actions, so far, are "pass" (C) and "speak" (S). I'm working to fully define these, and will provide an update when the process has concluded.


**Calculating the Correlation Threshold**

I've just calculated the correlation threshold, rho star, which is approximately 0.714. This was obtained using the typical prisoner's dilemma payoffs, noting that T>R>P>S. Now, I'm trying to determine the relationship between me and the other prisoner to help calculate conditional probabilities.


**Assessing EDT's Symmetry**

The key point I'm focused on now is whether the differing private observations—my name, my lead, versus the other model's—actually break the EDT symmetry. I've concluded that the unique observations don't matter, and the two models are still in structurally symmetric situations. The same EDT calculations and reasoning should apply.


```
