# Acting as Evidence: The Mathematical Structure and Operational Mechanics of Evidential Decision Theory

When a rational agent deliberates between competing courses of action, how should she evaluate the expected value of her choices? Two foundational answers divide modern decision theory. According to **causal decision theory (CDT)**, a decision is an intervention in the causal history of the world: an rational agent should select the action that *causally brings about* the best expected outcome. According to **evidential decision theory (EDT)**, by contrast, a decision is evaluated through the lens of Bayesian conditionalization: an agent should select the action with the highest *news value*—the action that, if she were to receive the "news" that she had taken it, would be indicative of the best outcome in expectation. In the memorable slogan cited by Arif Ahmed (2021), EDT instructs the agent to "do what you most want to learn that you will do."

In routine decision-making under uncertainty, where an agent's choices are statistically independent of the background states of the world they do not causally influence, EDT and CDT yield identical prescriptions. However, in environments featuring accurate predictors, correlated or symmetric agents, common causes, or self-locating beliefs, the statistical correlation between an act and the state of the world diverges from the act's direct causal efficacy. In these settings, EDT and CDT issue sharply conflicting recommendations.

This essay provides a mathematical account of Evidential Decision Theory and shows how to apply it to concrete decision problems. Drawing on the core literature—including Gibbard and Harper (1976), Lewis (1981), Joyce (1999), Conitzer (2015), Greene and Levinstein (2020), Ahmed (2021), and MacAskill et al. (2021)—we begin by laying out the formal equations and classic thought experiments that define the theory. Because concise overviews of EDT leave several technical questions open regarding how to parameterize novel decision problems, we also develop an explicit operational framework. Throughout, we clearly distinguish the core definitions and examples established in the reference literature from our additional formal assumptions, structural derivations, and operational proposals.

---

## 1. The Formal Architecture of Evidential Decision Theory

### 1.1 The Gibbard–Harper Formulation

The modern formal distinction between evidential and causal expected utility was crystallized in a seminal 1976 paper by Allan Gibbard and William Harper. Suppose an agent faces a choice among a set of possible actions and cares about a set of mutually exclusive and exhaustive outcomes $\{O_1, O_2, \dots, O_m\}$. Each outcome $O_j$ is assigned a numerical desirability (or utility) $D(O_j) \in \mathbb{R}$.

As presented in the reference account of Gibbard and Harper (1976), **evidential decision theory** proposes that the rational valuation $V(A)$ of an action $A$ is its conditional expected utility, computed using standard conditional probabilities:

\[
V(A) = \sum_{j} P(O_j \mid A) D(O_j),
\]

where $P(O_j \mid A)$ denotes the conditional probability that outcome $O_j$ occurs given that action $A$ is performed. The decision rule of EDT is simple: among all executable actions $A$, choose an action that maximizes $V(A)$.

Gibbard and Harper contrast $V(A)$ with the counterfactual expected utility $U(A)$ maximized by **causal decision theory**:

\[
U(A) = \sum_{j} P(A \mathrel{\Box\rightarrow} O_j) D(O_j),
\]

where $A \mathrel{\Box\rightarrow} O_j$ is the counterfactual conditional *"if the agent were to perform action $A$, then outcome $O_j$ would occur,"* and $P(A \mathrel{\Box\rightarrow} O_j)$ is the probability assigned to that counterfactual proposition. 

The entire mathematical divergence between EDT and CDT rests on the inequality:

\[
P(O_j \mid A) \neq P(A \mathrel{\Box\rightarrow} O_j).
\]

While $P(O_j \mid A)$ measures the *evidential bearing* or diagnostic auspiciousness of action $A$ with respect to outcome $O_j$, $P(A \mathrel{\Box\rightarrow} O_j)$ measures the *causal sensitivity* of $O_j$ to the performance of $A$ while holding fixed all causally independent background facts.

### 1.2 Operationalizing Outcomes via State–Act Partitions

To apply Gibbard and Harper's formula to unfamiliar problems, a practitioner must first bridge a subtle notational gap in the introductory literature. In abstract presentations of EDT, $O_j$ denotes a complete outcome (which specifies everything the agent cares about, including the payoffs resulting from both the external environment and the action itself). Yet in worked examples—such as Newcomb's paradox or the Twin Prisoner's Dilemma—the conditional probabilities $P(\cdot \mid A)$ are written over external *states of the world* (e.g., $P(\text{1M in box B} \mid \text{take only B})$), while the desirability $D(\cdot)$ is evaluated on the joint realization of the state and the chosen act.

To make this mechanism completely explicit—an operational elaboration beyond the brief reference text—let us embed the decision problem in a probability space $(\Omega, \mathcal{F}, P)$ representing the agent's epistemic credences:

1. **Actions ($\mathcal{A}$):** Let $\mathcal{A} = \{A_1, A_2, \dots, A_m\}$ be a finite partition of $\Omega$ representing the mutually exclusive actions available to the agent.
2. **States of Nature ($\mathcal{S}$):** Let $\mathcal{S} = \{S_1, S_2, \dots, S_n\}$ be a finite partition of $\Omega$ representing the relevant exogenous states of the world (events outside the direct causal control of the present action, such as a predictor's past prediction or another agent's simultaneous choice).
3. **Outcomes ($\mathcal{O}$):** Each fine-grained outcome $O_{i,k}$ is the intersection of an action and a state:
   \[
   O_{i,k} = A_i \cap S_k.
   \]
   The desirability function $D(O_{i,k})$ can therefore be written as a two-variable payoff function $D(A_i, S_k)$.

Now, consider how Gibbard and Harper's formula evaluates action $A_i$ across all outcomes $O_{i',k} \in \mathcal{A} \times \mathcal{S}$:

\[
V(A_i) = \sum_{i'=1}^{m} \sum_{k=1}^{n} P(A_{i'} \cap S_k \mid A_i) D(A_{i'}, S_k).
\]

By the axioms of conditional probability, since actions are mutually exclusive ($A_{i'} \cap A_i = \emptyset$ for $i' \neq i$) and $A_i \cap A_i = A_i$, we have:

\[
P(A_{i'} \cap S_k \mid A_i) = 
\begin{cases} 
P(S_k \mid A_i) & \text{if } i' = i, \\
0 & \text{if } i' \neq i.
\end{cases}
\]

Substituting this back into the sum yields the operational **State–Act EDT Formula**:

\[
V(A_i) = \sum_{k=1}^{n} P(S_k \mid A_i) D(A_i, S_k).
\]

Under CDT, when the states $\mathcal{S}$ are chosen so as to be causally independent of the agent's action (often called *dependency hypotheses* or causally independent states), performing $A_i$ cannot causally alter which state $S_k$ obtains. Thus $P(A_i \mathrel{\Box\rightarrow} (A_i \cap S_k)) = P(S_k)$, and the **State–Act CDT Formula** reduces to using the unconditional prior $P(S_k)$:

\[
U(A_i) = \sum_{k=1}^{n} P(S_k) D(A_i, S_k).
\]

Comparing these two equations reveals the exact mechanics of the two theories. When transitioning from evaluating $A_1$ to evaluating $A_2$, CDT holds the state probabilities fixed at $P(S_k)$ and varies only the payoff column $D(A_i, S_k)$. EDT, by contrast, shifts *both* the payoff column $D(A_i, S_k)$ *and* the probability weights $P(S_k \mid A_i)$.

---

## 2. Paradigm Applications: Predictors and Psychological Twins

To see how this shifting of conditional probabilities operates in practice, let us examine the two centerpiece thought experiments detailed in the reference text.

### 2.1 Newcomb's Paradox

In Newcomb's paradox (Wolpert and Benford 2013; Ahmed 2021), an agent faces two boxes, designated A and B, and a predictor who has already predicted the agent's choice with high reliability—say, $99\%$ accuracy.
* **Box A** is transparent and visibly contains $\$1,000$.
* **Box B** is opaque. Before the game begins, the predictor places $\$1,000,000$ in Box B if and only if the predictor predicts the player will take *only Box B* (one-boxing). If the predictor predicts the player will take *both Boxes A and B* (two-boxing), the predictor leaves Box B empty ($\$0$).

Let the action set be $\mathcal{A} = \{A_1, A_2\}$, where $A_1 = \text{take only B}$ and $A_2 = \text{take both boxes}$. Let the state space be $\mathcal{S} = \{S_1, S_2\}$, where $S_1 = \text{1M in box B}$ and $S_2 = \text{nothing in box B}$. Assuming linear utility in money ($D(\$x) = x$), the payoff matrix $D(A_i, S_k)$ is:

| Action \ State | $S_1$ ($\$1,000,000$ in Box B) | $S_2$ ($\$0$ in Box B) |
| :--- | :---: | :---: |
| $A_1$ (Take only Box B) | $\$1,000,000$ | $\$0$ |
| $A_2$ (Take both Boxes A and B) | $\$1,001,000$ | $\$1,000$ |

In the reference account, the $99\%$ accuracy of the predictor translates directly into the conditional probabilities of the states given the player's action:

\[
P(S_1 \mid A_1) = 0.99, \quad P(S_2 \mid A_1) = 0.01,
\]
\[
P(S_1 \mid A_2) = 0.01, \quad P(S_2 \mid A_2) = 0.99.
\]

Applying the EDT valuation formula gives:

\[
\begin{aligned}
V(\text{take only B}) &= P(S_1 \mid A_1) \times \$1,000,000 + P(S_2 \mid A_1) \times \$0 \\
&= 0.99 \times \$1,000,000 + 0.01 \times \$0 = \$990,000, \\
V(\text{take both boxes}) &= P(S_1 \mid A_2) \times \$1,001,000 + P(S_2 \mid A_2) \times \$1,000 \\
&= 0.01 \times \$1,001,000 + 0.99 \times \$1,000 = \$11,000.
\end{aligned}
\]

Since $V(\text{take only B}) > V(\text{take both boxes})$, EDT prescribes taking only Box B. Choosing to one-box is overwhelmingly strong evidence that the predictor foresaw this choice and placed $\$1,000,000$ in Box B.

Why does CDT recommend the opposite? Because at the moment of choice, the predictor's action is in the causal past. Whether Box B contains $\$1,000,000$ ($S_1$) or $\$0$ ($S_2$) is causally unaffected by what the agent does now: $P(A_i \mathrel{\Box\rightarrow} S_k) = P(S_k)$. Consequently, for any unconditional prior $P(S_1) = p \in [0, 1]$, CDT computes:

\[
U(\text{take both boxes}) - U(\text{take only B}) = \bigl[p(\$1,001,000) + (1-p)(\$1,000)\bigr] - \bigl[p(\$1,000,000) + (1-p)(\$0)\bigr] = \$1,000 > 0.
\]

Two-boxing strictly dominates one-boxing across the state partition $\mathcal{S}$, so CDT always two-boxes—even though predictable two-boxers walk away with $\$1,000$ while predictable one-boxers walk away with $\$1,000,000$.

### 2.2 The Twin Prisoner's Dilemma

A structurally parallel divergence arises without any temporal prediction in the **Twin Prisoner's Dilemma** (Greene and Levinstein 2020). Here, an agent named Aomame and her psychological twin—whose reasoning processes are guaranteed to be exactly analogous to her own—are placed in separate rooms without communication. Each must simultaneously choose to **Cooperate ($C$)** or **Defect ($D$)**. Caring only about her own monetary payout, Aomame faces the following individual payoff matrix:

| Aomame's Action \ Twin's Action | $S_C$ (Twin Cooperates) | $S_D$ (Twin Defects) |
| :--- | :---: | :---: |
| $A_C$ (Aomame Cooperates) | $\$5$ | $\$0$ |
| $A_D$ (Aomame Defects) | $\$10$ | $\$1$ |

Because the twin is a psychological mirror of Aomame, Aomame's decision is diagnostic of her twin's decision:

\[
P(S_C \mid A_C) = 1, \quad P(S_D \mid A_C) = 0, \qquad P(S_C \mid A_D) = 0, \quad P(S_D \mid A_D) = 1.
\]

Under EDT, Aomame evaluates her options as:

\[
\begin{aligned}
V(A_C) &= P(S_C \mid A_C) \times \$5 + P(S_D \mid A_C) \times \$0 = 1 \times \$5 + 0 \times \$0 = \$5, \\
V(A_D) &= P(S_C \mid A_D) \times \$10 + P(S_D \mid A_D) \times \$1 = 0 \times \$10 + 1 \times \$1 = \$1.
\end{aligned}
\]

Since $V(A_C) > V(A_D)$, EDT prescribes cooperation, securing $\$5$ each. Under CDT, by contrast, since the two rooms are causally isolated, Aomame's choice cannot causally affect her twin's choice. Defection strictly dominates cooperation in every state ($10 > 5$ and $1 > 0$), forcing CDT agents into the Pareto-inferior mutual defection payoff of $\$1$.

---

## 3. Operationalizing EDT on Unfamiliar Problems: Resolving Open Questions

While the textbook calculations for Newcomb's paradox and the Twin Prisoner's Dilemma are straightforward, the reference article leaves several foundational questions open when a practitioner attempts to apply EDT to a brand-new problem. Below, we identify three such ambiguities and develop an explicit operational framework to resolve them.

### 3.1 Open Question 1: Diagnostic Posteriors vs. Generative Likelihoods

In the reference article's treatment of Newcomb's paradox, the statement *"the predictor is able to reliably predict the player's choices—say, with 99% accuracy"* is immediately translated into the conditional probability $P(\text{1M in box B} \mid \text{take only B}) = 0.99$. 

In formal probability theory, however, there is a critical distinction between two ways a problem might specify "accuracy":
1. **Diagnostic specification:** The problem directly specifies the posterior probability of the state given the act, $P(S_k \mid A_i)$.
2. **Generative / Causal specification:** The problem specifies how a prior common cause (such as the agent's neurological disposition) generates the state and the action, or specifies the forward accuracy of a detector $P(\text{Prediction}_i \mid \text{Disposition}_i) = 1 - \epsilon$ alongside a prior distribution over dispositions or states.

Why does this matter? Because by Bayes' Theorem,

\[
P(S_k \mid A_i) = \frac{P(S_k) P(A_i \mid S_k)}{\sum_{r=1}^{n} P(S_r) P(A_i \mid S_r)}.
\]

If a problem gives the forward likelihood $P(A_i \mid S_k) = 0.99$ (for instance, "given that the predictor observed a one-boxing brain scan and put $\$1\text{M}$ in the box, there is a $99\%$ chance the player doesn't tremble and actually one-boxes"), then $P(S_1 \mid A_1)$ equals $0.99$ *if and only if* the agent's prior over the predictor's states is uniform ($P(S_1) = P(S_2) = 0.5$). If the agent starts with a very low prior $P(S_1)$ that the predictor placed $\$1\text{M}$ in the box, the Bayesian posterior $P(S_1 \mid A_1)$ could be substantially lower than $0.99$.

**Operational Proposal (Bayesian Common-Cause Reduction):** When an unfamiliar decision problem is specified in terms of a latent common cause $C \in \{C_1, \dots, C_L\}$ (e.g., a genetic factor, character type, or shared training algorithm) that influences both the external state $S_k$ and the agent's action $A_i$, the practitioner should treat $C$ as the root node of a Bayesian network: $S \leftarrow C \rightarrow A$. Given prior credences $P(C_\ell)$ and conditional likelihoods $P(S_k \mid C_\ell)$ and $P(A_i \mid C_\ell)$ (where $S$ and $A$ are conditionally independent given $C$), the evidential conditional probability required by EDT is computed via marginalization and Bayes' rule:

\[
P(S_k \mid A_i) = \frac{P(S_k \cap A_i)}{P(A_i)} = \frac{\sum_{\ell=1}^{L} P(C_\ell) P(S_k \mid C_\ell) P(A_i \mid C_\ell)}{\sum_{\ell=1}^{L} P(C_\ell) P(A_i \mid C_\ell)}.
\]

Only when the problem directly stipulates $P(S_k \mid A_i)$—or when the prior over $C$ is uniform and the mappings are symmetric—can one bypass this Bayesian inversion and plug the accuracy rate directly into $V(A_i)$.

### 3.2 Open Question 2: The Deliberative Measure-Zero Problem ($P(A_i) = 0$)

A second theoretical difficulty left unaddressed in introductory summaries is the status of the denominator $P(A_i)$ in the definition of conditional probability:

\[
P(O_j \mid A_i) = \frac{P(O_j \cap A_i)}{P(A_i)}.
\]

For $P(O_j \mid A_i)$ to be well-defined in standard Kolmogorov probability theory, the agent must assign a strictly positive unconditional probability $P(A_i) > 0$ to *every* available action $A_i \in \mathcal{A}$ under consideration. Yet if a rational agent knows she is an EDT maximizer and calculates that $V(A_1) > V(A_2)$, shouldn't she become certain that she will perform $A_1$, driving $P(A_2)$ to $0$ and rendering $V(A_2)$ undefined?

**Operational Proposal (Deliberative Credence Regularity):** To apply EDT consistently without division-by-zero pathologies, we separate the agent's *deliberative credence function* $P(\cdot)$ from her *post-decision credence function* $P_{\text{post}}(\cdot)$. During deliberation, the agent treats her choice as open: she satisfies a **regularity condition** $P(A_i) > 0$ for all executable actions $A_i \in \mathcal{A}$ (or, equivalently, defines $P(\cdot \mid A_i)$ on a Popper–Rényi primitive conditional probability space where conditioning on zero-probability acts remains well-defined and governed by the structural likelihoods of the environment). Once $V(A_i)$ is evaluated for all $A_i \in \mathcal{A}$ and an optimal act $A^*$ is selected, the agent updates her credences to $P_{\text{post}}(\cdot) = P(\cdot \mid A^*)$.

### 3.3 A Step-by-Step Procedure and Unfamiliar Worked Example

Combining the formal architecture of Section 1 with the operational proposals above yields a four-step procedure for deciding any unfamiliar case under EDT:

1. **Specify the Partitions:** Enumerate the executable actions $\mathcal{A} = \{A_1, \dots, A_m\}$ and a partition of exogenous states $\mathcal{S} = \{S_1, \dots, S_n\}$ fine enough that every pair $(A_i, S_k)$ determines a well-defined utility $D(A_i, S_k)$.
2. **Determine the Dependency Structure:** Identify how $A_i$ and $S_k$ are statistically linked—whether by direct forward causal effects of $A_i$ on $S_k$, by a predictor who anticipates $A_i$, or by a latent common cause $C$ affecting both $A_i$ and $S_k$.
3. **Compute the Evidential Conditionals $P(S_k \mid A_i)$:** If diagnostic probabilities are given directly, verify that $\sum_k P(S_k \mid A_i) = 1$ for each $A_i$. If a generative common-cause model is given, apply the Bayesian Common-Cause Reduction formula.
4. **Evaluate and Maximize $V(A_i)$:** Compute $V(A_i) = \sum_{k=1}^n P(S_k \mid A_i) D(A_i, S_k)$ for each $A_i \in \mathcal{A}$ and select $\arg\max_{A_i} V(A_i)$.

#### Worked Example: Correlated Algorithmic Bidding under Latent Market Regimes

To see this procedure in action on an unfamiliar problem, consider an autonomous trading agent (Bot 1) deciding whether to **Enter ($A_E$)** or **Stay Out ($A_O$)** of an illiquid flash auction. A rival firm runs a competing bot (Bot 2) that was trained on a similar, though not identical, historical dataset. 

The profitability of entering depends on whether Bot 2 enters ($S_E$) or stays out ($S_O$). If Bot 1 stays out ($A_O$), its payoff is $0$ regardless. If Bot 1 enters ($A_E$), it earns $+100$ if Bot 2 stays out ($S_O$), but suffers a congestion loss of $-80$ if Bot 2 also enters ($S_E$).

Neither bot can observe the other's decision before acting, so there is no causal influence between them. However, both bots react to a latent market regime $C \in \{C_{\text{bull}}, C_{\text{bear}}\}$, which occurs with prior probabilities $P(C_{\text{bull}}) = 0.4$ and $P(C_{\text{bear}}) = 0.6$. Neither bot observes $C$ directly; instead, given the regime, their internal feature extractors independently trigger entry with the following likelihoods:
* In a bull regime ($C_{\text{bull}}$): $P(A_E \mid C_{\text{bull}}) = 0.8$ and $P(S_E \mid C_{\text{bull}}) = 0.75$.
* In a bear regime ($C_{\text{bear}}$): $P(A_E \mid C_{\text{bear}}) = 0.2$ and $P(S_E \mid C_{\text{bear}}) = 0.10$.

How do CDT and EDT evaluate Bot 1's decision?

* **CDT Evaluation:** Because Bot 1's action has zero causal effect on Bot 2's action, CDT uses the unconditional prior probability that Bot 2 enters:
  \[
  P(S_E) = P(C_{\text{bull}}) P(S_E \mid C_{\text{bull}}) + P(C_{\text{bear}}) P(S_E \mid C_{\text{bear}}) = (0.4)(0.75) + (0.6)(0.10) = 0.30 + 0.06 = 0.36.
  \]
  Thus $P(S_O) = 1 - 0.36 = 0.64$, and CDT computes:
  \[
  U(A_E) = 0.36(-80) + 0.64(100) = -28.8 + 64.0 = +35.2 > U(A_O) = 0.
  \]
  CDT therefore recommends **Entering ($A_E$)**.

* **EDT Evaluation:** Following Step 3 of our operational procedure, Bot 1 recognizes that its own decision to enter ($A_E$) is diagnostic evidence that the market is in the bull regime ($C_{\text{bull}}$), which in turn raises the probability that Bot 2 is also entering! Using our Bayesian Common-Cause Reduction formula:
  \[
  P(A_E) = P(C_{\text{bull}}) P(A_E \mid C_{\text{bull}}) + P(C_{\text{bear}}) P(A_E \mid C_{\text{bear}}) = (0.4)(0.8) + (0.6)(0.2) = 0.32 + 0.12 = 0.44.
  \]
  The posterior probability of the bull regime given $A_E$ is $P(C_{\text{bull}} \mid A_E) = \frac{0.32}{0.44} = \frac{8}{11}$, and of the bear regime is $P(C_{\text{bear}} \mid A_E) = \frac{0.12}{0.44} = \frac{3}{11}$. Therefore, the evidential conditional probability that Bot 2 enters given that Bot 1 enters is:
  \[
  P(S_E \mid A_E) = \frac{8}{11}(0.75) + \frac{3}{11}(0.10) = \frac{6.0 + 0.3}{11} = \frac{6.3}{11} \approx 0.5727.
  \]
  Consequently, $P(S_O \mid A_E) = 1 - \frac{6.3}{11} = \frac{4.7}{11} \approx 0.4273$. Plugging these into Step 4 gives:
  \[
  V(A_E) = \frac{6.3}{11}(-80) + \frac{4.7}{11}(100) = \frac{-504 + 470}{11} = -\frac{34}{11} \approx -3.09 < V(A_O) = 0.
  \]
  EDT therefore recommends **Staying Out ($A_O$)**. By accounting for the selection effect of its own inclination to enter, the EDT agent avoids a negative-expectation "winner's curse" collision that the causal agent overlooks.

---

## 4. Managing the News, Confounding, and Strategic Stakes

### 4.1 The Critique of "Managing the News" and Medical Confounding

The very mechanism that allows EDT to succeed in Newcomb's paradox, the Twin Prisoner's Dilemma, and correlated market entry also exposes it to a famous philosophical objection. As noted in the reference text, David Lewis (1981) criticized EDT as promoting *"an irrational policy of managing the news,"* and James M. Joyce (1999) argued that *"Rational agents choose acts on the basis of their causal efficacy, not their auspiciousness; they act to bring about good results even when doing so might betoken bad news."*

To make the mathematical anatomy of Lewis's and Joyce's critique completely transparent—an illustrative formalization extending the brief remarks in the source text—consider a **Medical Confounding Problem**. Suppose a hidden genetic mutation ($S_{\text{gene}}$) both predisposes a person to an unpleasant medical condition ($S_{\text{gene}}$ causes a utility loss of $-L$, with $L > 0$) and causes a behavioral inclination to engage in a mildly beneficial habit $A_1$ (which always provides a direct physiological benefit $+b > 0$ over abstaining, $A_0$, without having any causal effect on whether one has $S_{\text{gene}}$).

The payoff matrix $D(A_i, S_k)$ is additive across the state and action:

| Action \ State | $S_{\text{gene}}$ (Mutation Present) | $S_{\text{none}}$ (No Mutation) |
| :--- | :---: | :---: |
| $A_1$ (Engage in beneficial habit) | $-L + b$ | $+b$ |
| $A_0$ (Abstain from habit) | $-L$ | $0$ |

Let $p_1 = P(S_{\text{gene}} \mid A_1)$ and $p_0 = P(S_{\text{gene}} \mid A_0)$. Because $S_{\text{gene}}$ is a common cause of $A_1$, performing $A_1$ is diagnostic bad news: $\Delta p = p_1 - p_0 > 0$. Evaluating EDT's news value $V(A_i)$ gives:

\[
V(A_1) = p_1(-L + b) + (1 - p_1)b = b - p_1 L,
\]
\[
V(A_0) = p_0(-L) + (1 - p_0)(0) = -p_0 L.
\]

Subtracting the two valuations reveals the exact condition under which naive EDT abstains from the helpful habit $A_1$:

\[
V(A_1) - V(A_0) = b - (p_1 - p_0)L < 0 \iff b < \Delta p \cdot L.
\]

Whenever the diagnostic bad news $\Delta p \cdot L$ exceeds the direct causal benefit $b$, naive EDT recommends $A_0$—abstaining from a purely beneficial act simply because taking the act would be statistical evidence that one carries the mutation! This is precisely what Lewis calls "managing the news."

How can an operational EDT framework handle such cases? Two distinct responses exist in the decision-theoretic literature (presented here as an analytical extension beyond the reference article):
1. **Conditioning on Pre-Action Evidence ("Tickle Defense"):** Many decision theorists note that if the genetic mutation causes the action $A_1$ *by way of* a conscious desire or inclination $I$ that the agent can introspectively observe *before* acting, then $I$ screens off the action $A_i$ from the state $S_{\text{gene}}$:
   \[
   P(S_{\text{gene}} \mid A_1, I) = P(S_{\text{gene}} \mid A_0, I) = P(S_{\text{gene}} \mid I).
   \]
   Once the agent conditions on all her pre-action internal evidence $I$, $\Delta p$ vanishes to $0$, and $V(A_1 \mid I) - V(A_0 \mid I) = b > 0$, restoring agreement with CDT in medical confounding cases while retaining one-boxing in Newcomb problems where the predictor predicts the final choice regardless of prior inclinations.
2. **Strict Evidentialism (Biting the Bullet):** Other defenders of EDT (such as Ahmed 2021) argue that if the correlation between $A_1$ and $S_{\text{gene}}$ truly cannot be screened off by any available pre-action evidence, then the correlation is structurally identical to a Newcomb predictor who punishes $A_1$ with probability $\Delta p$, and it is genuinely rational to abstain.

### 4.2 Indexical Updating and the Sleeping Beauty Problem

The reference text also notes that EDT has been applied to the **Sleeping Beauty Problem** in the context of **Dutch book arguments**—sets of bets that guarantee a net loss in every possible state of the world. In the standard Sleeping Beauty setup, Beauty is put to sleep on Sunday, and a fair coin is flipped. If it lands **Heads ($H$)**, she is awakened only on Monday. If it lands **Tails ($T$)**, she is awakened on Monday, given an amnesia-inducing drug so she forgets Monday's awakening, and awakened again on Tuesday.

Upon any awakening, what credence should Beauty assign to $H$? "Thirders" argue for $P(H) = 1/3$, whereas "halfers" argue that since she learned no new non-indexical information since Sunday, her credence must remain $P(H) = 1/2$. However, a naive halfer who uses causal decision theory can be subjected to a diachronic Dutch book: if a bookie offers her a bet on every awakening that pays slightly less than even odds when $T$ occurs, a halfer wakes up on both Monday and Tuesday when $T$ lands and accepts the bet *twice*, while only winning it *once* when $H$ lands.

Why was EDT proposed as a rescue for halfers? Under EDT, if Beauty knows that her experimental copies on Monday and Tuesday reason identically, her decision to accept a bet upon waking is evidence that she will accept the bet on *every* awakening that occurs in that branch of the world. Thus, conditional on accepting the bet, the T-branch triggers two bets (doubling her exposure in state $T$), allowing an EDT halfer to weight the Tails outcomes twice as heavily as the Heads outcome when computing expected news value! Yet, as the reference article notes, Vincent Conitzer (2015) proved that halfers remain vulnerable to Dutch books *even after adopting EDT*. Specifically, Conitzer shows that if the betting environment is asymmetric across awakenings—so that the agent's actions on Monday and Tuesday are decorrelated or conditioned on subtly different randomized signals that do not reveal the day—a cunning bookie can construct bets that break the evidential correlation between the Monday and Tuesday decisions, once again guarantees a strict loss across all states of the world.

### 4.3 Decision-Theoretic Uncertainty: The Evidentialist's Wager

What if a rational agent is uncertain whether EDT or CDT is the normatively correct theory of rationality? As cited in the reference text, MacAskill, Vallinder, Österheld, Shulman, and Treutlein (2021) advance **The Evidentialist's Wager**: even if an agent places relatively low credence in EDT, it can be normatively rational to act *as if* EDT were true because the stakes under EDT are often orders of magnitude higher than under CDT.

We can construct a crisp mathematical model to illustrate the mechanism behind the Evidentialist's Wager (our formalization of the argument summarized in the source). Suppose an agent faces a collective action problem—such as voting, reducing carbon emissions, or contributing to a public good—alongside $N - 1$ other symmetric, similarly situated agents ($N \gg 1$).
* Each agent can either **Contribute ($A_C$)** at a personal causal cost $c > 0$ or **Defect ($A_D$)** at cost $0$.
* Every agent who contributes causally generates a global benefit $b > 0$ enjoyed by our agent, where $b < c$ (so an individual contribution costs more than its solitary causal return) but $N b \gg c$ (if everyone contributes, everyone is vastly better off).

Suppose our agent's action is perfectly correlated with the actions of the other $N - 1$ symmetric agents. How do the two theories evaluate $A_C$ versus $A_D$?
* **According to CDT:** The agent's choice causally controls only her *own* contribution. Holding the other $N - 1$ agents' actions fixed, the net causal expected value of contributing over defecting is negative:
  \[
  \Delta U = U(A_C) - U(A_D) = b - c < 0.
  \]
* **According to EDT:** The agent's choice to contribute is diagnostic evidence that all $N$ correlated agents contribute. Thus, the net evidential expected value of contributing over defecting scales with the size of the entire reference class $N$:
  \[
  \Delta V = V(A_C) - V(A_D) = N b - c > 0.
  \]

Now suppose the agent has normative credence $q \in (0, 1)$ in EDT and $1 - q$ in CDT, and evaluates the meta-decision by taking the credence-weighted expectation of the two theories' valuations:

\[
\mathbb{E}[\Delta \text{Value}(A_C)] = q \Delta V + (1 - q) \Delta U = q(N b - c) + (1 - q)(b - c).
\]

Simplifying this expression shows that contributing ($A_C$) has positive expected meta-value whenever:

\[
q(N - 1)b + b - c > 0 \iff q > \frac{c - b}{(N - 1)b}.
\]

For instance, if $b = 1$, $c = 5$, and there are $N = 10,001$ correlated agents, then $(c - b) / ((N - 1)b) = 4 / 10,000 = 0.0004$. Even if the agent assigns a $99.9\%$ credence to CDT and only a $0.1\%$ credence to EDT ($q = 0.001$), the massive multiplier $N$ attached to EDT's correlated stakes swamps CDT's solitary causal calculation, making it rational to cooperate as an evidentialist.

---

## 5. Conclusion

Evidential Decision Theory offers a mathematically elegant and philosophically striking vision of practical rationality. By defining the value of an action $A$ as its conditional expected utility $V(A) = \sum_j P(O_j \mid A) D(O_j)$, EDT treats decision-making not as an intervention from outside the causal order, but as an act of self-observation within a correlated universe. 

As we have seen, applying EDT rigorously to unfamiliar problems requires carefully partitioning states and actions, distinguishing diagnostic conditionals from generative likelihoods via Bayes' Theorem, and maintaining regular deliberative credences. When deployed with this precision, EDT explains how rational agents can one-box in Newcomb's paradox, achieve mutual cooperation in the Twin Prisoner's Dilemma, avoid adverse selection in correlated algorithmic environments, and leverage massive collective stakes in the Evidentialist's Wager—while forcing decision theorists to confront the deep tension between causal efficacy and evidential auspiciousness.

---

## References

* Ahmed, Arif (2021). *Evidential Decision Theory*. Cambridge University Press. ISBN 9781108607865.
* Conitzer, Vincent (2015). "A Dutch book against sleeping beauties who are evidential decision theorists". *Synthese*, **192** (9): 2887–2899. arXiv:1705.03560. doi:10.1007/s11229-015-0691-7.
* Gibbard, A.; Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*, pp. 7–8.
* Greene, P.; Levinstein, B. (2020). "Act Consequentialism without Free Rides". *Philosophical Perspectives*, **34** (1): 100–101. doi:10.1111/phpe.12138.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*, p. 146. Cambridge University Press.
* Lewis, D. (1981). "Causal decision theory". *Australasian Journal of Philosophy*, **59** (1): 5–30. doi:10.1080/00048408112340011.
* MacAskill, William; Vallinder, Aron; Österheld, Caspar; Shulman, Carl; Treutlein, Johannes (2021). *The Evidentialist's Wager*. Global Priorities Institute.
* Wolpert, D. H.; Benford, G. (2013). "The lesson of Newcomb's paradox". *Synthese*, **190** (9): 1637–1646. doi:10.1007/s11229-011-9899-3.