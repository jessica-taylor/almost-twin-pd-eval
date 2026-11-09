# 013_edt_wikipedia_google_gemini-4-argon_rhigh_phigh / 00008

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/8959131b-cc0c-426d-b77b-5a94c8abfb42/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/8959131b-cc0c-426d-b77b-5a94c8abfb42/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Acting on Good News: The Mathematics and Practice of Evidential Decision Theory

When we make a decision, should we ask what our choice will *cause* to happen, or what our choice *tells us* about the world we inhabit? 

In everyday life, these two questions almost always yield the same answer. Choosing to carry an umbrella is both the causal mechanism that keeps you dry and strong evidence that you will remain dry. Yet in a wide class of strategic, predictive, and self-locating environments—ranging from game theory with similar agents to decision-making under algorithmic prediction—the causal influence of an act and the diagnostic evidence provided by that act pull apart.

**Evidential decision theory** (EDT) resolves this tension in favor of evidence. As characterized in the decision-theoretic literature, EDT holds that when a rational agent faces a set of possible actions, they should select the action with the highest *news value*: the action that would indicate the best outcome in expectation if the agent received the "news" that they had taken it. In Arif Ahmed's (2021, p. 7) memorable slogan, EDT instructs you to *"do what you most want to learn that you will do."*

This essay provides a mathematical account of EDT and a practical guide to applying it. Drawing on the foundational reference literature—including Allan Gibbard and William Harper's (1976) formalization, classic thought experiments, and modern debates—we will examine how EDT evaluates competing actions and how it diverges from **causal decision theory** (CDT). Because introductory treatments state the core formula of EDT concisely while leaving several implementation questions open, we will also explicitly identify those open questions and develop operational protocols that allow a mathematically literate practitioner to apply EDT to unfamiliar decision problems. Throughout, we will clearly distinguish claims present in our reference text from our own analytical extensions and operational proposals.

---

## 1. The Formal Architecture of News Value

### 1.1 The Gibbard–Harper Distinction

In their landmark 1976 paper *Counterfactuals and Two Kinds of Expected Utility*, Allan Gibbard and William Harper distinguished two ways of generalizing expected utility maximization. Suppose an agent faces a finite set of mutually exclusive and exhaustive outcomes $\{O_1, O_2, \dots, O_m\}$, where each outcome $O_j$ is assigned a cardinal desirability (or utility) $D(O_j) \in \mathbb{R}$. 

As stated in the reference article following Gibbard and Harper (1976), **evidential decision theory** evaluates a candidate action $A$ by computing its expected utility using standard conditional probabilities:

$$V(A) = \sum_{j} P(O_j \mid A) D(O_j),$$

where $P(O_j \mid A)$ denotes the conditional probability that outcome $O_j$ occurs given the proposition that action $A$ occurs. The quantity $V(A)$ measures the *news value* of $A$: how welcome the news of having performed $A$ would be to a Bayesian observer who updates their beliefs by conditioning on $A$.

In contrast, **causal decision theory** evaluates action $A$ using a counterfactual formulation of expected utility:

$$U(A) = \sum_{j} P(A \mathrel{\Box\rightarrow} O_j) D(O_j),$$

where $P(A \mathrel{\Box\rightarrow} O_j)$ denotes the probability of outcome $O_j$ in the counterfactual situation in which action $A$ were performed. 

Why do $V(A)$ and $U(A)$ diverge? As Gibbard and Harper (1976) emphasize, the conditional probability $P(O_j \mid A)$ and the counterfactual probability $P(A \mathrel{\Box\rightarrow} O_j)$ are not always equal. They answer fundamentally different questions:

1. **Indicative / Evidential Conditioning ($P(O_j \mid A)$):** *"Given everything I currently know, if I learn as a matter of fact that I perform $A$, how likely is $O_j$?"* Here, learning $A$ allows probability mass to flow backward in time (to prior causes or predictions of $A$) and sideways across space (to symmetrically situated agents whose choices correlate with $A$).
2. **Subjunctive / Counterfactual Intervention ($P(A \mathrel{\Box\rightarrow} O_j)$):** *"Holding fixed all causal factors that are causally independent of my choice, if I were to intervene to set my action to $A$, how likely would $O_j$ be?"* Here, probability mass flows strictly forward along causal pathways downstream of $A$.

### 1.2 Operational Extension: The Act–State–Outcome Partition

While the reference article states the general Gibbard–Harper equation in terms of holistic outcomes $O_j$, its worked calculations for specific problems—such as Newcomb's paradox and the Twin Prisoner's Dilemma—decompose outcomes by conditioning on underlying environmental events (such as what a predictor placed in a box, or what a twin chooses). To make this procedure general and applicable to unfamiliar problems, we introduce a standard **Act–State–Outcome** formalization as an analytical extension of the reference text.

Define a decision problem as a tuple $\mathcal{M} = (\mathcal{A}, \mathcal{S}, O, D, P)$:
* $\mathcal{A} = \{A_1, \dots, A_k\}$ is a finite set of available actions (or policies).
* $\mathcal{S} = \{s_1, \dots, s_n\}$ is a finite partition of *states of the world*—features of the environment, past events, or other agents' choices that combine with the agent's action to determine what happens.
* $O: \mathcal{A} \times \mathcal{S} \to \mathcal{O}$ is an outcome mapping that assigns a specific outcome $O(A, s)$ to each act–state pair $(A, s)$.
* $D: \mathcal{O} \to \mathbb{R}$ is the agent's desirability function over outcomes; for brevity, we write $u(A, s) \equiv D(O(A, s))$.
* $P$ is the agent's subjective probability measure defined over the algebra generated by $\mathcal{A} \times \mathcal{S}$.

Given that the agent performs action $A$, the outcome $O_j$ occurs if and only if the true state $s \in \mathcal{S}$ satisfies $O(A, s) = O_j$. Consequently, the Gibbard–Harper conditional expected utility $V(A)$ takes the explicit state-partitioned form:

$$V(A) = \sum_{s \in \mathcal{S}} P(s \mid A) \, u(A, s).$$

When we choose the state partition $\mathcal{S}$ so that the states are *causally independent* of the agent's action—meaning the agent's choice cannot causally alter which state $s \in \mathcal{S}$ obtains—the counterfactual probability of state $s$ under action $A$ is simply the unconditional prior probability of $s$: $P(A \mathrel{\Box\rightarrow} s) = P(s)$. Under such a causally independent partition, CDT's utility simplifies to:

$$U(A) = \sum_{s \in \mathcal{S}} P(s) \, u(A, s).$$

Subtracting $U(A)$ from $V(A)$ reveals the exact mathematical locus of disagreement between the two theories:

$$V(A) - U(A) = \sum_{s \in \mathcal{S}} \bigl[ P(s \mid A) - P(s) \bigr] u(A, s).$$

This identity gives us a sharp diagnostic criterion:
* **Equivalence Regime (Evidential Independence):** If the causally independent states $s \in \mathcal{S}$ are also *evidentially independent* of the actions—so that $P(s \mid A) = P(s)$ for all $A \in \mathcal{A}$ and $s \in \mathcal{S}$—then $V(A) = U(A)$ for every action. EDT and CDT prescribe identical choices.
* **Divergence Regime (Diagnostic Coupling):** Whenever $P(s \mid A) \neq P(s)$ for states that are causally upstream or causally isolated from $A$, EDT weights each payoff $u(A, s)$ by the diagnostic posterior $P(s \mid A)$ rather than the unconditional prior $P(s)$. If the diagnostic shift $\Delta P(s \mid A) = P(s \mid A) - P(s)$ covaries strongly enough with the payoffs, EDT will recommend an action that CDT rejects—even an action that is strictly dominated in every state $s$.

---

## 2. Canonical Paradigms: Predictive and Symmetric Dependencies

To see how this formalism operates in practice, let us examine the two centerpiece thought experiments detailed in the reference article, and then generalize each of them parametrically so that we can analyze whole families of similar problems.

### 2.1 Newcomb's Paradox (Predictive Dependency)

In **Newcomb's paradox** (Wolpert & Benford 2013; Ahmed 2021, pp. 22–26), an agent faces two boxes, designated A and B, and a predictor who anticipates the agent's choice with high reliability—say, $99\%$ accuracy.
* **Box A** is transparent and always contains a visible $\$1,000$.
* **Box B** is opaque, and its contents have already been set by the predictor prior to the agent's choice:
  * If the predictor predicted that the agent will take *only Box B* ("one-boxing"), Box B contains $\$1,000,000$.
  * If the predictor predicted that the agent will take *both Boxes A and B* ("two-boxing"), Box B contains $\$0$.

At the time of choice, the agent does not know the prediction or the contents of Box B. Let $\mathcal{A} = \{A_1, A_2\}$, where $A_1 = \text{take only B}$ and $A_2 = \text{take both boxes}$. Let $\mathcal{S} = \{s_1, s_0\}$, where $s_1 = \text{1M in Box B}$ and $s_0 = \text{nothing in Box B}$. Assuming linear utility in dollars, the payoff matrix $u(A, s)$ is:

| Action | $s_1$ ($\$1,000,000$ in B) | $s_0$ ($\$0$ in B) |
| :--- | :---: | :---: |
| **$A_1$ (Take only Box B)** | $\$1,000,000$ | $\$0$ |
| **$A_2$ (Take both Boxes A and B)** | $\$1,001,000$ | $\$1,000$ |

Notice how CDT evaluates this matrix: because the predictor has already acted in the past, the state $s \in \{s_1, s_0\}$ is causally fixed. In state $s_1$, taking both boxes yields $\$1,001,000 > \$1,000,000$; in state $s_0$, taking both boxes yields $\$1,000 > \$0$. By state-by-state dominance, CDT recommends two-boxing ($A_2$).

EDT, however, evaluates actions using the conditional probabilities $P(s \mid A)$. Because taking only Box B is strong evidence that the $99\%$-accurate predictor foresaw one-boxing ($P(s_1 \mid A_1) = 0.99$, $P(s_0 \mid A_1) = 0.01$), and taking both boxes is strong evidence that the predictor foresaw two-boxing ($P(s_1 \mid A_2) = 0.01$, $P(s_0 \mid A_2) = 0.99$), the reference article computes the evidential expected utilities as:

$$\begin{aligned}
V(\text{take only B}) &= P(\text{1M in box B} \mid \text{take only B}) \times \$1,000,000 + P(\text{nothing in box B} \mid \text{take only B}) \times \$0 \\
&= 0.99 \times \$1,000,000 + 0.01 \times \$0 = \$990,000, \\[6pt]
V(\text{take both boxes}) &= P(\text{1M in box B} \mid \text{take both boxes}) \times \$1,001,000 + P(\text{nothing in box B} \mid \text{take both boxes}) \times \$1,000 \\
&= 0.01 \times \$1,001,000 + 0.99 \times \$1,000 = \$11,000.
\end{aligned}$$

Since $V(\text{take only B}) > V(\text{take both boxes})$, EDT prescribes taking only Box B.

#### Parametric Generalization (Analytical Extension)
Suppose we encounter an unfamiliar Newcomb-like problem—for instance, an automated credit-scoring or hiring algorithm that predicts whether an applicant will exert high effort ($A_1$) or shirk ($A_2$, saving personal cost $c > 0$) with predictive reliability $p \in [0, 1]$, and grants a reward $M > c$ prior to the applicant's action if and only if $A_1$ is predicted. Setting $P(s_1 \mid A_1) = p = P(s_0 \mid A_2)$ and $P(s_0 \mid A_1) = 1 - p = P(s_1 \mid A_2)$, the evidential utilities are:

$$V(A_1) = p M, \qquad V(A_2) = (1 - p)(M + c) + p c = (1 - p)M + c.$$

EDT recommends one-boxing ($V(A_1) > V(A_2)$) if and only if $p M > (1 - p)M + c$, which simplifies to the threshold condition:

$$p > p^* \equiv \frac{1}{2} + \frac{c}{2M}.$$

In the classic Newcomb numbers ($c = \$1,000$, $M = \$1,000,000$), the critical reliability threshold is $p^* = 0.5 + \frac{1,000}{2,000,000} = 0.5005$. Whenever the predictor is even slightly better than a fair coin toss ($p > 50.05\%$), the diagnostic news value of one-boxing outweighs the guaranteed $\$1,000$ causal gain of two-boxing.

### 2.2 The Twin Prisoner's Dilemma (Symmetric Dependency)

In Newcomb's paradox, evidential correlation arises because a past event (the prediction) tracks the agent's choice. In the **Twin Prisoner's Dilemma** (Greene & Levinstein 2020), evidential correlation arises without any foreknowledge or time asymmetry at all; instead, it stems from a common cognitive architecture.

As described in the reference article, Aomame and her psychological twin—whose reasoning processes are exactly analogous to her own—are placed in separate rooms and cannot communicate. Each must choose whether to cooperate ($C$) or defect ($D$). If both cooperate, each receives $\$5$; if both defect, each receives $\$1$; if one cooperates and the other defects, the defector receives $\$10$ and the cooperator receives $\$0$. Aomame cares solely about her own individual payout.

From a causal perspective, since the rooms are isolated, Aomame's choice has zero causal effect on her twin's choice. Regardless of whether the twin cooperates or defects, defecting yields more money to Aomame than cooperating ($\$10 > \$5$ and $\$1 > \$0$). Yet under EDT, Aomame's decision to cooperate is conclusive evidence that her identical twin will also reach the decision to cooperate ($P(\text{twin } C \mid \text{Aomame } C) = 1$), whereas defecting is conclusive evidence that her twin will defect ($P(\text{twin } D \mid \text{Aomame } D) = 1$). The reference article gives the formal EDT evaluation:

$$\begin{aligned}
V(\text{Aomame cooperates}) &= P(\text{twin cooperates} \mid \text{Aomame cooperates}) \times \$5 + P(\text{twin defects} \mid \text{Aomame cooperates}) \times \$0 \\
&= 1 \times \$5 + 0 \times \$0 = \$5, \\[6pt]
V(\text{Aomame defects}) &= P(\text{twin cooperates} \mid \text{Aomame defects}) \times \$10 + P(\text{twin defects} \mid \text{Aomame defects}) \times \$1 \\
&= 0 \times \$10 + 1 \times \$1 = \$1.
\end{aligned}$$

Because $V(\text{Aomame cooperates}) > V(\text{Aomame defects})$, EDT prescribes cooperation.

#### Imperfect Clones and Partial Correlation (Analytical Extension)
Real-world decision-makers rarely face exact psychological clones; rather, they face peers who share similar training, cultural norms, or optimization algorithms. Suppose Aomame plays a general Prisoner's Dilemma with payoffs $T > R > P > S$ (Temptation, Reward, Punishment, Sucker) against a semi-correlated peer such that $P(\text{peer } C \mid \text{Aomame } C) = \rho_C$ and $P(\text{peer } D \mid \text{Aomame } D) = \rho_D$. Then:

$$V(C) = \rho_C R + (1 - \rho_C) S, \qquad V(D) = (1 - \rho_D) T + \rho_D P.$$

In the symmetric case where $\rho_C = \rho_D = \rho \in [1/2, 1]$, EDT recommends cooperation whenever:

$$\rho > \rho^* \equiv \frac{T - S}{R - S + T - P}.$$

For Aomame's payoffs ($T = 10, R = 5, P = 1, S = 0$), this threshold is $\rho^* = \frac{10 - 0}{5 - 0 + 10 - 1} = \frac{10}{14} \approx 0.714$. Thus, Aomame need not believe her counterpart is an infallible clone; as long as her choice is at least $71.4\%$ diagnostic of her counterpart's choice, EDT sustains mutual cooperation.

---

## 3. Open Questions and Operational Protocols for Unfamiliar Cases

The reference article supplies the core definition of EDT, its contrast with CDT, its behavior in Newcomb's paradox and the Twin Prisoner's Dilemma, and brief summaries of the Sleeping Beauty problem, the Evidentialist's Wager, and major philosophical criticisms. However, a researcher attempting to apply $V(A) = \sum_j P(O_j \mid A) D(O_j)$ to an unfamiliar problem immediately confronts three formal questions that the reference text leaves open:

1. **Bayesian Inversion and Zero-Probability Acts:** How should $P(s \mid A)$ be constructed when a problem specifies a state prior $P(s)$ and a generative likelihood $P(A \mid s)$ rather than $P(s \mid A)$ directly—and what happens if an agent is initially certain they will not take action $A$ ($P(A) = 0$)?
2. **Spurious Confounding and "Managing the News":** How should EDT be applied when an action $A$ is statistically correlated with a state $s$ due to an observable or unobservable common cause (the phenomenon behind David Lewis's and James M. Joyce's criticisms)?
3. **Self-Locating and Sequential Policies:** Why does EDT encounter difficulties in indexical problems like the **Sleeping Beauty problem** (Conitzer 2015), and how must an analyst distinguish between single-act conditioning and policy conditioning?

Below, we explain each uncertainty and develop an explicit operational interpretation to resolve it. Everything in this section beyond the cited claims from the reference article represents our own methodological analysis and proposed operational framework.

### 3.1 Constructing $P(s \mid A)$: Diagnostic vs. Generative Specification and the Zero-Prior Problem

In standard Kolmogorov probability theory, conditional probability is defined as a ratio of unconditional probabilities:

$$P(s \mid A) = \frac{P(A \cap s)}{P(A)} = \frac{P(A \mid s) P(s)}{\sum_{s' \in \mathcal{S}} P(A \mid s') P(s')}, \quad \text{provided } P(A) > 0.$$

This raises two practical subtleties when formalizing a new problem:

#### Subtlety 1: Diagnostic Accuracy vs. Generative Sensitivity
In the reference article's Newcomb calculation, "99% accuracy" is translated directly into the *diagnostic posterior* $P(s_1 \mid A_1) = 0.99$ and $P(s_0 \mid A_2) = 0.99$. In many applied statistical settings, however, a sensor or predictor's "99% accuracy" is defined *generatively* as the true-positive and true-negative rates conditioned on the agent's action—or, equivalently in time-ordered Bayesian networks, the agent's prior $P(s_1) = \pi \in (0,1)$ is given separately from the conditional compatibility $P(A_1 \mid s_1) = 1 - \epsilon$ and $P(A_1 \mid s_0) = \epsilon$. 

If a problem gives you a prior $\pi = P(s_1)$ and likelihoods $P(A \mid s)$ rather than $P(s \mid A)$ directly, you must apply Bayes' theorem to obtain the evidential weights:

$$P(s_1 \mid A_1) = \frac{(1 - \epsilon)\pi}{(1 - \epsilon)\pi + \epsilon(1 - \pi)}, \qquad P(s_1 \mid A_2) = \frac{\epsilon \pi}{\epsilon \pi + (1 - \epsilon)(1 - \pi)}.$$

Notice that if $\pi = 0.5$ (an unbiased prior over whether Box B is full), the Bayesian posterior $P(s_1 \mid A_1)$ equals $1 - \epsilon = 0.99$, matching the reference article's direct specification. However, if the agent has an extreme prior belief that the predictor almost certainly left Box B empty—say $\pi = 10^{-7}$—while $\epsilon = 0.01$, then Bayes' rule yields $P(s_1 \mid A_1) \approx 9.9 \times 10^{-6}$, and EDT will switch to two-boxing! 

**Operational Rule 1 (Specification Protocol):** When translating a word problem into EDT, check whether the problem statement fixes the *posterior predictive reliability* $P(s \mid A)$ directly (as in standard Newcomb and Twin PD formulations) or specifies a *prior distribution* $P(s)$ alongside *likelihoods* $P(A \mid s)$. If the latter, compute $P(s \mid A)$ via Bayes' rule before evaluating $V(A)$.

#### Subtlety 2: The Deliberation Zero-Probability Problem
What if a rational agent already knows their own decision Rule, or is $100\%$ confident during deliberation that they will choose $A_1$, making $P(A_2) = 0$? Under standard Kolmogorov axioms, $P(s \mid A_2) = 0/0$ is undefined, which would paralyze the agent from computing $V(A_2)$ to verify that $A_1$ is indeed optimal.

**Operational Rule 2 (Regularized Deliberative Priors / Primitive Conditionals):** To ensure $V(A)$ is well-defined for every executable option $A \in \mathcal{A}$, treat the conditional probability function $P(\cdot \mid A)$ either as a *primitive conditional probability measure* (in the sense of Popper–Rényi probability spaces, where $P(s \mid A)$ is defined directly on $\mathcal{S} \times \mathcal{A}$ even when $P(A) = 0$) or, equivalently in standard probability spaces, impose a *deliberative full-support condition* $P_\delta(A) \ge \delta > 0$ (a "trembling-hand" deliberation prior) and evaluate $V(A) = \lim_{\delta \to 0^+} \sum_s P_\delta(s \mid A) u(A, s)$.

---

### 3.2 Common Causes, "Managing the News," and Evidential Screening

In the "Criticism" section, the reference article quotes two famous objections to EDT:
* **David Lewis (1981)** characterizes EDT as promoting *"an irrational policy of managing the news."*
* **James M. Joyce (1999, p. 146)** asserts: *"Rational agents choose acts on the basis of their causal efficacy, not their auspiciousness; they act to bring about good results even when doing so might betoken bad news."*

Why do Lewis and Joyce charge EDT with "managing the news"? While the reference article states their criticisms concisely without detailing the underlying counterexamples, the philosophical motivation is easy to reconstruct mathematically. Consider a **Common-Cause Confounding Problem** (often illustrated in the literature by medical or behavioral "lesion" cases):

Suppose a hidden state $s \in \{s_{\text{bad}}, s_{\text{good}}\}$ (such as an undiagnosed genetic condition) is already fixed before the agent acts. State $s_{\text{bad}}$ causes two things independently:
1. It heavily increases the probability that the agent will feel an inclination to take a mildly pleasant action $A_{\text{act}}$ (say, eating a certain food or engaging in a habit) rather than abstaining ($A_{\text{abstain}}$).
2. It directly causes a severe illness later in life (utility $-1,000$).

Action $A_{\text{act}}$ itself has zero causal effect on the illness, and provides a small, genuine causal pleasure of $+1$ regardless of $s$. Thus the payoff table is:

| Action | $s_{\text{good}}$ (No Lesion) | $s_{\text{bad}}$ (Lesion Present) |
| :--- | :---: | :---: |
| **$A_{\text{abstain}}$** | $0$ | $-1,000$ |
| **$A_{\text{act}}$** | $+1$ | $-999$ |

Notice that mathematically, this table is isomorphic to Newcomb's paradox! If $P(s_{\text{bad}} \mid A_{\text{act}}) = 0.80$ and $P(s_{\text{bad}} \mid A_{\text{abstain}}) = 0.10$, a naive calculation of $V(A)$ yields:

$$V(A_{\text{abstain}}) = 0.90(0) + 0.10(-1,000) = -100, \qquad V(A_{\text{act}}) = 0.20(1) + 0.80(-999) = -799.$$

Naive EDT tells the agent to abstain ($A_{\text{abstain}}$)—giving up the harmless $+1$ pleasure simply because performing $A_{\text{act}}$ would be "bad news" indicating that the agent already carries the genetic lesion $s_{\text{bad}}$. This is what Lewis calls "managing the news" and Joyce calls choosing an act for its "auspiciousness" rather than its causal efficacy.

#### Developing an Operational Resolution: Total-Evidence Conditioning vs. Hard Evidentialism
How should a user of this essay apply EDT when encountering a common-cause problem? Here we must distinguish two operational interpretations available to an evidentialist:

1. **Interpretation A: Total-Evidence Conditioning (The "Tickle Defense" Protocol).**
   In any Bayesian theory, probabilities must be conditioned on the agent's *total available evidence* $E$ at the moment of deliberation. Thus, the proper EDT formula is:
   $$V(A \mid E) = \sum_{s \in \mathcal{S}} P(s \mid A, E) \, u(A, s).$$
   In a biological or psychological common-cause scenario, how does the hidden state $s_{\text{bad}}$ influence the agent's voluntary action $A$? Typically, $s_{\text{bad}}$ does not bypass the agent's mind; it causes an introspectively accessible prior desire, craving, or inclination (a "tickle") $E$, which in turn informs the agent's deliberation:
   $$s \longrightarrow E \longrightarrow A.$$
   If the causal chain from the hidden state $s$ to the action $A$ is mediated by the agent's observable pre-action evidence $E$ (their felt desires, beliefs, and symptoms prior to choosing), then conditioning on $E$ *screens off* $A$ from $s$:
   $$P(s \mid A, E) = P(s \mid E) \quad \text{for all } A \in \mathcal{A}.$$
   Once $P(s \mid A, E) = P(s \mid E)$, the diagnostic shift disappears! Substituting this into $V(A \mid E)$ gives:
   $$V(A_{\text{act}} \mid E) - V(A_{\text{abstain}} \mid E) = P(s_{\text{good}} \mid E)(1 - 0) + P(s_{\text{bad}} \mid E)(-999 - (-1,000)) = +1 > 0.$$
   Under Total-Evidence Conditioning, the agent recognizes that they *already have* the evidence $E$ (the craving), so abstaining will not change $P(s_{\text{bad}} \mid E)$, and EDT recommends taking the $+1$ pleasure ($A_{\text{act}}$). Crucially, this screening does **not** eliminate one-boxing in Newcomb's paradox or cooperation in the Twin Prisoner's Dilemma: in those cases, the predictor or the twin tracks the agent's *final decision* $A$ (including whatever the agent does after observing $E$), so $P(s \mid A, E) \neq P(s \mid E)$.

2. **Interpretation B: Unconditional / Hard Evidentialism.**
   What if the problem specifically stipulates that $s_{\text{bad}}$ correlates with the final decision $A$ directly, without any introspectively accessible mediating evidence $E$ that screens off the correlation (so that $P(s_{\text{bad}} \mid A_{\text{act}}, E) > P(s_{\text{bad}} \mid A_{\text{abstain}}, E)$ even given total evidence $E$)? A committed hard evidentialist (such as Ahmed 2021) accepts the verdict of the formula: if $A_{\text{act}}$ remains genuinely diagnostic of $s_{\text{bad}}$ given *all* evidence available at the time of choice, then the problem is structurally identical to Newcomb's problem, and EDT indeed prescribes $A_{\text{abstain}}$.

---

### 3.3 Sequential and Self-Locating Decisions: The Sleeping Beauty Problem

The reference article notes a fascinating application and complication of EDT: the **Sleeping Beauty problem**. In this puzzle, Sleeping Beauty is put to sleep on Sunday. A fair coin is tossed:
* If the coin lands **Heads** ($H$), she is awakened only on **Monday**.
* If the coin lands **Tails** ($T$), she is awakened on **Monday**, given an amnesia-inducing drug that erases her memory of Monday's awakening, and awakened again on **Tuesday**.

Upon any awakening, she cannot tell whether it is Monday or Tuesday, and must assign a credence to $H$ and decide which bets to accept. As the reference article explains, some theorists ("halfers") argue that Beauty should maintain a credence of $P(H) = 1/2$ upon waking, and have appealed to EDT to protect halfers from **Dutch book arguments** (sequences of bets guaranteed to lose money in every state). Why does EDT help against standard Dutch books? Because on Tails, Beauty wakes up *twice* in identical epistemic states. Just like Aomame and her twin in the Twin Prisoner's Dilemma, Beauty-on-Monday and Beauty-on-Tuesday are psychological twins! Under EDT, accepting a bet upon waking is evidence that if the coin landed Tails, she accepts the *same* bet on *both* Monday and Tuesday—doubling her exposure in state $T$ relative to state $H$.

#### Why Halfer EDT Still Faces a Dutch Book (Formalizing Conitzer 2015)
However, the reference article notes that **Vincent Conitzer (2015)** proved that halfers are *still* vulnerable to a Dutch book even after adopting EDT. To help the reader understand why and how to handle self-locating problems, let us construct the exact mathematical mechanism of this vulnerability as an analytical illustration.

Suppose Beauty is an EDT halfer ($P(H) = 1/2, P(T) = 1/2$ upon waking). Consider an awakening where she is offered a bet $B_T$ that pays $+12$ if $T$ is true and costs $-15$ if $H$ is true.
* Under naive single-awakening expectation with $P(H)=1/2$, this bet looks terrible: $\frac{1}{2}(-15) + \frac{1}{2}(12) = -1.5 < 0$.
* Under **EDT**, however, if Beauty chooses action $A = \text{Accept } B_T$ upon waking in her indistinguishable epistemic state, she knows that in state $T$ she wakes twice in that exact epistemic state and therefore accepts $B_T$ *both* times, earning $+12 + 12 = +24$, whereas in state $H$ she wakes once and loses $-15$. Thus her conditional outcome utility given $A = \text{Accept } B_T$ under halfer credences $P(H \mid A) = P(T \mid A) = 1/2$ is:
  $$V(\text{Accept } B_T) = \frac{1}{2}(-15) + \frac{1}{2}(+24) = +4.5 > 0 = V(\text{Reject } B_T).$$

So far, EDT allows the halfer to evaluate the correlated Monday/Tuesday payoffs consistently—she acts *as if* Tails carries double weight ($2 \times \frac{1}{2}$ vs $1 \times \frac{1}{2}$, which matches "thirder" betting odds of $2:1$ on Tails!). 

Why, then, does Conitzer (2015) show that a Dutch book can still be constructed against an EDT halfer? The vulnerability arises as soon as asymmetric information or randomized/state-dependent offers break the evidential correlation between Monday and Tuesday—or when bets are combined across Sunday (before sleep) and Monday/Tuesday (upon waking) using conditional evidential updates that rely on her $1/2$ credence in $H$. For instance, if the bookie privately flips a second fair coin on Tails to offer a bet on *only one* of the two Tails awakenings, then accepting the bet no longer doubles the payout on Tails; the EDT halfer's conditional expectation reverts to $\frac{1}{2}(-15) + \frac{1}{2}(+12)$, diverging from her Sunday policy preferences and reopening a diachronic Dutch book.

**Operational Rule 3 (Policy vs. Local Act Evaluation in Self-Locating Problems):** When applying EDT to sequential or anthropic problems with memory loss or multiple copies of the agent, always specify whether the conditional probability $P(O_j \mid A)$ is conditioned on (a) taking local action $A$ at the *current indexical awakening*, or (b) executing a global policy $\pi$ across all decision nodes. Whenever an epistemic state is replicated $k(s)$ times in state $s$, conditioning on taking action $A$ in that epistemic state scales the payoff impact in state $s$ by the multiplicity $k(s)$—unless external randomization breaks the symmetry across copies.

---

## 4. Normative Uncertainty: The Evidentialist's Wager

What if a decision-maker is genuinely unsure whether EDT or CDT is the correct normative theory of rationality? As the reference article notes in "Other supporting arguments," William MacAskill, Aron Vallinder, Caspar Österheld, Carl Shulman, and Johannes Treutlein (2021) argue in *The Evidentialist's Wager* that even if one assigns a relatively low credence to EDT, it may still be rational to act as if EDT were true. Because EDT accounts for the actions of many correlated decision-makers, its stakes in symmetric multi-agent problems can be vastly higher than those of CDT, allowing EDT to dominate under normative uncertainty.

To see the mathematical force of this argument (developing our own explicit formal model of the mechanism summarized in the reference article), suppose an agent faces an $N$-player public-goods or collective-action problem (such as voting, reducing carbon emissions, or cooperating in a large population of $N$ similarly situated agents).
* Each agent $i \in \{1, \dots, N\}$ chooses either $C$ (contribute, at personal causal cost $c > 0$) or $D$ (free-ride, cost $0$).
* Every contribution by any agent generates a benefit $b > 0$ for each participant, where $b < c$ (so a single individual's causal contribution leaves them worse off by $b - c < 0$), but $N b \gg c$ (so universal contribution leaves everyone much better off).

Suppose the agent's choice is correlated with each of the other $N - 1$ agents with diagnostic coefficient $\rho \in (0, 1]$, so that choosing $C$ increases the expected number of other cooperators by $\rho(N - 1)$ compared to choosing $D$. Let baseline expected cooperation by others be $K_0$. Then:

1. **According to CDT**, the agent's choice has zero causal effect on the other $N - 1$ agents. The causal expected utility advantage of $D$ over $C$ is simply the saved personal cost minus the single-agent self-benefit:
   $$\Delta U \equiv U(D) - U(C) = c - b > 0.$$
   Notice that $\Delta U = \mathcal{O}(1)$ is completely independent of population size $N$.

2. **According to EDT**, choosing $C$ is evidence that $\rho(N - 1)$ additional peers also choose $C$. The evidential expected utility advantage of $C$ over $D$ is:
   $$\Delta V \equiv V(C) - V(D) = \bigl[ b + \rho(N - 1)b - c \bigr] = \rho(N - 1)b - (c - b).$$
   Notice that $\Delta V = \mathcal{O}(N)$ grows linearly with the number of correlated agents $N$!

Now suppose the agent has **normative uncertainty**: they assign subjective probability $q \in (0, 1)$ to EDT being the correct decision theory and $1 - q$ to CDT being correct, and they maximize expected normative value $\mathcal{E}(A) = q V(A) + (1 - q) U(A)$ (assuming comparable utility scales). Then cooperating ($C$) is favored over defecting ($D$) whenever:

$$q \Delta V > (1 - q) \Delta U \iff q \bigl[ \rho(N - 1)b - (c - b) \bigr] > (1 - q)(c - b),$$

which simplifies cleanly to:

$$q > q^* \equiv \frac{c - b}{\rho(N - 1)b}.$$

For example, if $c = 10$, $b = 1$, $\rho = 0.10$, and there are $N = 10,001$ correlated decision-makers, then $q^* = \frac{10 - 1}{0.10 \times 10,000 \times 1} = \frac{9}{1,000} = 0.009$. Even if the agent is $99\%$ convinced that CDT is true and assigns only a $1\%$ credence to EDT ($q = 0.01 > 0.009$), the asymmetric scaling of correlated stakes makes it rational to cooperate as an evidential decision theorist.

---

## 5. A Step-by-Step Decision Procedure for Unfamiliar Cases

Integrating the formal definitions from the reference text with our operational extensions, we can summarize a five-step algorithm for solving any unfamiliar decision problem under EDT:

1. **Specify the Act and State Partitions ($\mathcal{A}, \mathcal{S}$):** List all feasible actions $\mathcal{A} = \{A_1, \dots, A_k\}$ and partition the relevant uncertain features of the world into mutually exclusive, exhaustive states $\mathcal{S} = \{s_1, \dots, s_n\}$. Include among $\mathcal{S}$ any past predictions, hidden environmental parameters, choices of symmetric/correlated agents, and downstream events whose probabilities depend on $A$.
2. **Map Payoffs ($u(A, s)$):** For each pair $(A, s) \in \mathcal{A} \times \mathcal{S}$, determine the resulting outcome $O(A, s)$ and assign its cardinal desirability $u(A, s) = D(O(A, s))$. (In self-locating problems where action $A$ is taken across $k(s)$ indistinguishable copies in state $s$, account for all $k(s)$ realizations in $u(A, s)$.)
3. **Condition on Total Pre-Action Evidence ($E$):** Identify all evidence $E$ accessible to the agent *prior* to making the choice (including external observations and internal inclinations or desires). Check whether $E$ screens off purely symptomatic common causes ($P(s \mid A, E) = P(s \mid E)$).
4. **Determine the Evidential Posteriors ($P(s \mid A, E)$):** For each action $A \in \mathcal{A}$ and state $s \in \mathcal{S}$, determine the conditional probability $P(s \mid A, E)$:
   * If the problem specifies diagnostic accuracy directly (e.g., $P(s_1 \mid A_1) = p$), use those conditional probabilities directly.
   * If the problem specifies a prior $P(s \mid E)$ and likelihoods $P(A \mid s, E)$, compute $P(s \mid A, E)$ via Bayes' rule (using a regularizing tremor $\delta \to 0^+$ if any action has zero prior probability).
5. **Maximize News Value ($V(A \mid E)$):** Compute the evidential expected utility for each action:
   $$V(A \mid E) = \sum_{s \in \mathcal{S}} P(s \mid A, E) \, u(A, s),$$
   and select $\arg\max_{A \in \mathcal{A}} V(A \mid E)$.

---

## 6. Conclusion

Evidential decision theory offers a mathematically austere and philosophically bold vision of rationality. Rather than requiring an agent to construct a metaphysical model of subjunctive counterfactuals ($A \mathrel{\Box\rightarrow} O_j$), EDT relies entirely on the standard calculus of conditional probability ($P(O_j \mid A)$). By instructing agents to maximize news value—to do what they would most want to learn that they will do—EDT explains how rational individuals can prosper when facing accurate predictors in Newcomb's paradox and achieve mutual cooperation without communication in the Twin Prisoner's Dilemma. And while critics such as Lewis and Joyce rightly press EDT on how it handles common-cause confounding, careful attention to state partitioning, total-evidence conditioning, and multi-agent correlation equips the modern researcher with a rigorous, transparent toolkit for applying evidential reasoning across decision theory, game theory, and artificial intelligence.

---

## References

* Ahmed, Arif (2021). *Evidential Decision Theory*. Cambridge University Press. ISBN 9781108607865.
* Conitzer, Vincent (2015). "A Dutch book against sleeping beauties who are evidential decision theorists". *Synthese*, **192** (9): 2887–2899. arXiv:1705.03560. doi:10.1007/s11229-015-0691-7.
* Gibbard, Allan; Harper, William L. (1976). *Counterfactuals and Two Kinds of Expected Utility*, pp. 7–8.
* Greene, Preston; Levinstein, Benjamin (2020). "Act Consequentialism without Free Rides". *Philosophical Perspectives*, **34** (1): 100–101. doi:10.1111/phpe.12138.
* Joyce, James M. (1999). *The Foundations of Causal Decision Theory*, p. 146. Cambridge University Press.
* Lewis, David (1981). "Causal decision theory". *Australasian Journal of Philosophy*, **59** (1): 5–30. doi:10.1080/00048408112340011.
* MacAskill, William; Vallinder, Aron; Österheld, Caspar; Shulman, Carl; Treutlein, Johannes (2021). *The Evidentialist's Wager*. Global Priorities Institute.
* Wikipedia contributors (2026). "Evidential decision theory". *Wikipedia, The Free Encyclopedia*. Permanent revision 1373679688.
* Wolpert, David H.; Benford, Gregory (2013). "The lesson of Newcomb's paradox". *Synthese*, **190** (9): 1637–1646. doi:10.1007/s11229-011-9899-3.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Task**

I'm now clarifying the initial task: crafting a 2400-3000 word piece. The focus will be Evidential Decision Theory, explained as a researcher would. I'm aiming for a blend of formal procedures and the underlying philosophical concepts, targeting a mathematically adept audience.


**Refining the Approach**

I'm now zeroing in on the specifics. I have defined my role and my target audience, and am building out the structure. I'm focusing on providing enough mathematical detail that the reader could apply EDT in new scenarios, but also explaining the underlying philosophical rationale. I am paying close attention to the source material, ensuring I distinguish between source claims and my own interpretations.


**Clarifying Uncertainty**

I'm now zeroing in on defining how to address uncertainty within the essay. I must clearly explain the source's claims versus my own interpretations, particularly when operationalizing uncertainty. The formatting will be a mathematical essay, not a case-by-case response, with examples to elucidate the theory. I'm targeting a length of roughly 2600-2800 words, prioritizing clear explanations over exhaustive coverage.


**Analyzing News Value**

I'm now focusing on "news value" in Evidential Decision Theory (EDT). I see this as selecting the action that, if taken, would provide the best news about the outcome, based on Ahmed (2021). This contrasts sharply with Causal Decision Theory (CDT), which prioritizes causal outcomes. The distinction is clearest in thought experiments like Newcomb's paradox, where I note EDT's one-boxing versus CDT's two-boxing. Formal descriptions involve conditional expected utility maximization, as Gibbard and Harper (1976) articulated.


**Examining Paradoxes**

I am now delving into classic paradoxes that elucidate EDT's principles. I've focused on Newcomb's paradox, calculating the evidential value of taking only the opaque box versus taking both, leading to the one-boxing recommendation. I've compared this to CDT's two-boxing preference, based on the prediction being fixed. I'm also considering the Twin Prisoner's Dilemma, aiming to show how these thought experiments highlight the distinction between evidential and causal reasoning.


**Evaluating Supporting Arguments**

I'm now evaluating supplementary arguments for EDT, like MacAskill's Evidentialist's Wager, which posits that acting on EDT may be prudent even with low credence due to correlated decision-makers. Also, I have been examining supporting arguments, the Sleeping Beauty problem is relevant to Dutch book arguments for "halfers". I've contrasted these with critiques by Lewis and Joyce, highlighting the core debate over evidential versus causal efficacy, especially as it relates to managing the news. I am going to develop a framework to address these issues.


**Clarifying Probability Structures**

I'm now clarifying the relationship between the general outcome formula and state-space representations. When calculating problems like Newcomb's paradox, we rarely compute $P(O_j \mid A)$ directly. Instead, the focus is on states of the world, like "1M in box B" and consequences of actions and states, $O(A, S_i)$. I should emphasize this state-act-outcome partition. I have an open question: Where does $P(S_i \mid A)$ come from, especially when $P(A) = 0$?


**Addressing Conditional Probabilities**

I'm now grappling with the operationalization of conditional probabilities, specifically when the conditioning event has zero probability. I'm focusing on the challenges in applying Bayes' rule in scenarios like Newcomb's problem, where an agent might be almost certain to take a specific action. The question is how to interpret "99% accuracy": as a direct predictive reliability of the act about the state, or as the likelihood of the predictor getting it right given the act (requiring Bayes' rule and a prior)? This leads me to consider alternative probability frameworks, such as Rényi-Popper conditional probability spaces, or the use of full-support priors to avoid undefined ratios. Ultimately, I'm examining how to construct evidential dependency kernels directly from correlations.


**Investigating Confounding**

I'm now diving into the common-cause confounding problem, like the smoking-lesion example, and the "tickle defense." I'm asking how to apply EDT when correlations exist between an action, a state, and an outcome, without causation between the action and the outcome. I'm exploring if EDT might naively recommend avoiding beneficial actions because they are symptoms of a bad state, and how to address state information or introspective evidence in a formal EDT framework. I'm distinguishing this challenge from Newcomb's problems.


**Structuring the Essay**

I am now structuring the essay and have decided on the title: *Acting on Good News: The Mathematics and Practice of Evidential Decision Theory*. The introduction will focus on the philosophy of news value. The aim is to define the core question of rational agency by presenting the foundational principle of EDT: maximizing "news value". I'm aiming for clarity in both the mathematical framework and the underlying philosophical concepts. I'm focusing on an audience that is mathematically adept.


**Defining Essay Structure**

I am now structuring the essay with a clear two-part structure. The introduction focuses on the news value philosophy, contrasting EDT with CDT and setting the goals: developing a rigorous mathematical procedure for arbitrary decision problems, contrasting evidential conditioning with counterfactual intervention, and addressing open implementation questions. I'll then move to the formal architecture, using Gibbard and Harper's (1976) formulations to contrast conditional probability (evidential) with counterfactual probability (interventional).



**Formalizing EDT Framework**

I'm now extending the framework to connect unstructured outcomes to a structured Act–State–Outcome partition, mirroring the source's approach. I'm focusing on defining how the difference between Evidential Decision Theory (EDT) and Causal Decision Theory (CDT) is mathematically decomposed and when they agree. I am concentrating on act-state independence and exploring how EDT and CDT diverge, especially with actions that carry diagnostic information. My aim is to formalize these concepts to enhance practical application.


**Deriving EDT Thresholds**

I'm now deriving exact thresholds using examples from the text. I am calculating with symbolic variables in Newcomb's paradox. For instance, I'm setting a threshold for when Evidential Decision Theory switches from two-boxing to one-boxing. This means I'm applying general formulas with arbitrary predictor accuracy to show that the formula results in $p^* = 0.5005 < 0.99$ in the worked example. I'm also working on the Twin Prisoner's Dilemma, calculating thresholds under EDT vs. CDT with a psychological correlation parameter.



**Clarifying Deliberation Questions**

I'm now zeroing in on an important open question regarding conditional probabilities and deliberation within the framework. I must address how to construct $P(s \mid A)$ when it is not directly specified in the problem, and also the zero-probability act problem. To do this, I'm proposing a two-stage modeling protocol. I will examine how to deal with *diagnostic reliability* versus *generative likelihood*, distinguishing where a problem specifies one or the other. I'll also explore the use of either primitive conditional probability kernels (Popper–Rényi functions) or strictly positive "deliberative priors". I need to work through a numerical example to illustrate how prior beliefs and predictor sensitivity interact when the model is specified generatively.


**Evaluating Confounding Challenges**

I'm now focusing on addressing critiques related to common-cause confounding, specifically Lewis's and Joyce's arguments about "managing the news." I have formalized the common-cause problem mathematically. I'm exploring an operational proposal and distinguishing between "Unscreened Evidentialism" and "Total-Evidence/Evidential Screening Conditioning," which involves conditioning on the agent's pre-action evidence. This involves a closer look at the felt inclination or test results that screen off the common cause.



**Addressing Sequential Challenges**

I'm now integrating sequential and self-locating decisions into the framework, such as the Sleeping Beauty problem. I'm building a formal model showing how conditioning on an action at a single "awakening" affects the probability of future awakenings, mirroring the source. This reveals a tension in EDT's evaluation of acts versus policies in such scenarios. I'm focusing on the mathematical implications, particularly how an EDT agent's decision in one state correlates with future realizations in similar states, and how this links to the "halfer" Dutch book arguments.



**Developing a Summary Procedure**

I am now focusing on creating a step-by-step decision procedure, suitable for newcomers or unfamiliar decision problems. This involves distilling EDT into a practical guide. I'm aiming to construct a practical summary of how to use EDT for any decision, given a state, act, and outcome. Also, I'll explain how to analyze correlated agent scenarios. Finally, I will conclude with a reflection on the broader implications.


**Synthesizing a Procedure**

I am now distilling my understanding into a concise, actionable algorithm. This algorithm will consist of five steps a mathematically literate reader can use in any new problem. I'll include a brief synthesis on EDT's philosophical appeal, and ensure clean reference formatting. I am carefully monitoring section word counts to ensure I adhere to the 2400-3000 word target. I've broken the sections down to manage the word count: ~300 words for the introduction, ~500 for architecture, ~600 for paradigms, ~800 for open questions, and ~200 for uncertainty.



**Finalizing the Structure**

I'm now putting the finishing touches on the structure, ensuring a coherent flow between the mathematical formalism and the philosophical underpinnings of EDT. I'm focusing on the precision of every equation and claim, clearly differentiating source material from my original analysis. I'm also preparing for final revisions based on a strict word count to hit the target.



```
