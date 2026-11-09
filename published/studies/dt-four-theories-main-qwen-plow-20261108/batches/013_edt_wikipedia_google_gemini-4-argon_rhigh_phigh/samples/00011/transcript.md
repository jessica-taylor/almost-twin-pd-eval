# 013_edt_wikipedia_google_gemini-4-argon_rhigh_phigh / 00011

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/7445a3c6-a4ef-40da-8a76-4da17f4c5943/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/7445a3c6-a4ef-40da-8a76-4da17f4c5943/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Acting on News Value: The Mathematics and Operational Mechanics of Evidential Decision Theory

When a rational agent stands at a fork in the road, what makes one action better than another? The everyday intuition of agency is interventionist: you choose an action in order to *push* the world into a preferred state. Yet in a wide class of decision problems—ranging from predictors who anticipate your choices to strategic interactions with agents who reason like you—your choice does more than push the future. It also reveals information about the past or the present. 

**Evidential decision theory** (EDT) takes this informational relationship as the foundation of rational choice. As summarized in the reference literature (specifically Arif Ahmed's 2021 monograph *Evidential Decision Theory*), EDT holds that when a rational agent is confronted with a set of possible actions, they should select the action with the highest *news value*: the action that would be indicative of the best outcome in expectation if the agent received the "news" that they had taken it. In Ahmed's memorable phrase, EDT instructs you to "do what you most want to learn that you will do."

This essay provides a rigorous mathematical account of evidential decision theory and a practical guide for applying it to unfamiliar decision problems. Following the baseline account in our source text, we begin with the formal equations of Allan Gibbard and William Harper (1976) that separate EDT from its chief rival, **causal decision theory** (CDT), and examine the canonical thought experiments where the two theories diverge. Because the introductory reference material states the core formula concisely and leaves several operational questions open—such as how to parameterize states versus outcomes, how to assign conditional probabilities when deliberating over one's own actions, how to evaluate multi-step policies, and how to separate genuine strategic correlation from spurious common-cause confounding—we will explicitly identify where the source text stops and develop our own formal operational frameworks to bridge those gaps.

---

## 1. The Formal Architecture: Conditional Probability vs. Counterfactuals

In their landmark 1976 paper, *Counterfactuals and Two Kinds of Expected Utility*, Allan Gibbard and William Harper demonstrated that the traditional Savage-style expected utility framework conceals an ambiguity between two distinct ways of weighting outcomes. 

As reported in the reference article, let an agent choose an action $A$ from a finite repertoire of available actions, and let $\{O_j\}$ be a set of possible outcomes, each assigned a cardinal numerical desirability (or utility) $D(O_j) \in \mathbb{R}$. Evidential decision theory evaluates each candidate action $A$ by computing its expected utility using standard **conditional probabilities**:

$$V(A) = \sum_{j} P(O_j \mid A) D(O_j), \tag{1}$$

where $P(O_j \mid A)$ is the conditional probability that outcome $O_j$ occurs given the proposition that action $A$ is performed. An EDT agent selects an action $A^* \in \arg\max_A V(A)$.

Causal decision theory, by contrast, replaces conditional probabilities with **counterfactual probabilities**. In Gibbard and Harper's formulation, CDT evaluates action $A$ via the utility function $U(A)$:

$$U(A) = \sum_{j} P(A \mathrel{\Box\rightarrow} O_j) D(O_j), \tag{2}$$

where $A \mathrel{\Box\rightarrow} O_j$ denotes the counterfactual conditional *"if the agent were to perform action $A$, then outcome $O_j$ would occur,"* and $P(A \mathrel{\Box\rightarrow} O_j)$ is the agent's credence in that counterfactual proposition. 

Why are Equations (1) and (2) not equivalent? As Gibbard and Harper observe, $P(O_j \mid A)$ and $P(A \mathrel{\Box\rightarrow} O_j)$ measure fundamentally different relationships:
* **Conditional probability** $P(O_j \mid A) = \frac{P(O_j \cap A)}{P(A)}$ measures purely *epistemic or statistical correlation*. Updating on $A$ propagates information backward in time (to prior causes of $A$), sideways in time (to symmetric processes correlated with $A$), and forward in time (to the causal effects of $A$).
* **Counterfactual probability** $P(A \mathrel{\Box\rightarrow} O_j)$ measures *forward causal sensitivity*. Evaluating what would happen if $A$ were performed holds fixed all causally independent background facts—including past predictions and the independent choices of distant agents—and tracks only the downstream consequences of intervening to set $A$.

### An Operational Elaboration: Separating States from Outcomes

Before we examine the canonical thought experiments, it is helpful to highlight a subtle gap between how the reference text states Equation (1) and how it actually calculates expected utilities in its examples. 

In Equation (1), the index $j$ ranges directly over complete outcomes $O_j$. However, when the reference text works through Newcomb's paradox and the Twin Prisoner's Dilemma, it writes conditional probabilities over *background states of the world*—such as $P(\text{1M in box B} \mid \text{take only B})$ or $P(\text{twin cooperates} \mid \text{Aomame cooperates})$—and multiplies them by the monetary payoff generated jointly by the state and the chosen action.

To apply EDT cleanly to unfamiliar cases, we need to make this state-space decomposition explicit. *(Note: The following state-act-outcome translation is our own mathematical elaboration of the source's notation, designed to make the theory straightforward to implement.)*

Suppose a decision problem is specified by three components:
1. A finite set of mutually exclusive actions $\mathcal{A} = \{A_1, A_2, \dots, A_m\}$.
2. A finite partition of mutually exclusive and exhaustive background **states of the world** $\mathcal{S} = \{S_1, S_2, \dots, S_n\}$ that represent facts outside the direct causal control of the agent's present action (such as a predictor's prior move or a twin's concurrent choice).
3. A consequence mapping $f: \mathcal{A} \times \mathcal{S} \to \mathcal{O}$ that assigns a fine-grained outcome $O_{ik} = f(A_i, S_k)$ with desirability $D(A_i, S_k) \equiv D(f(A_i, S_k))$ to every action-state pair.

Because action $A_i$ and state $S_k$ uniquely determine the outcome $O_{ik}$ once $A_i$ is given, the conditional probability of obtaining the outcome associated with state $S_k$ given that action $A_i$ is taken is simply $P(S_k \mid A_i)$. Equation (1) therefore rewrites in state-space form as:

$$V(A_i) = \sum_{k=1}^{n} P(S_k \mid A_i) D(A_i, S_k). \tag{3}$$

Meanwhile, when the states $S_k \in \mathcal{S}$ are chosen so that the agent's action $A_i$ has *no causal influence* over which state $S_k$ obtains, the counterfactual probability of $S_k$ under any intervention $A_i$ reduces to the unconditional prior probability of the state: $P(A_i \mathrel{\Box\rightarrow} S_k) = P(S_k)$. Thus, for causally independent states, CDT's Equation (2) simplifies to:

$$U(A_i) = \sum_{k=1}^{n} P(S_k) D(A_i, S_k). \tag{4}$$

Comparing Equations (3) and (4) exposes the exact mathematical mechanism of every disagreement between EDT and CDT. Whenever an action $A_i$ is causally powerless over the state $S_k$ ($P(A_i \mathrel{\Box\rightarrow} S_k) = P(S_k)$) yet statistically correlated with $S_k$ ($P(S_k \mid A_i) \neq P(S_k)$), the evidential weight $P(S_k \mid A_i)$ diverges from the causal weight $P(S_k)$. We can define the **evidential divergence** between two actions $A_1$ and $A_2$ relative to CDT as:

$$\Delta_{\text{EDT}-\text{CDT}}(A_1, A_2) = \bigl[V(A_1) - V(A_2)\bigr] - \bigl[U(A_1) - U(A_2)\bigr] = \sum_{k=1}^{n} \Bigl[ \bigl(P(S_k \mid A_1) - P(S_k)\bigr) D(A_1, S_k) - \bigl(P(S_k \mid A_2) - P(S_k)\bigr) D(A_2, S_k) \Bigr]. \tag{5}$$

Whenever $\Delta_{\text{EDT}-\text{CDT}}(A_1, A_2)$ is large enough to flip the sign of $U(A_1) - U(A_2)$, EDT and CDT issue conflicting prescriptions.

---

## 2. Canonical Thought Experiments: Predictors and Twins

The reference article illustrates the divergence between EDT and CDT through two foundational thought experiments: Newcomb's paradox and the Twin Prisoner's Dilemma. Let us review the exact calculations from the source and then generalize them into parametric decision rules that can be applied to broader classes of problems.

### 2.1 Newcomb's Paradox

As described in the source text (referencing Wolpert & Benford 2013 and Ahmed 2021), Newcomb's paradox involves a player, a reliable predictor, a transparent Box A, and an opaque Box B. The player must choose between two actions:
* $A_1$ (**One-box**): Take only Box B.
* $A_2$ (**Two-box**): Take both Box A and Box B.

The player knows the following setup:
* Box A is transparent and visibly contains $\$1,000$.
* Box B is opaque, and its contents have already been fixed by the predictor prior to the player's choice:
  * State $S_1$ ($\text{1M in box B}$): If the predictor predicted the player would take only Box B ($A_1$), Box B contains $\$1,000,000$.
  * State $S_2$ ($\text{nothing in box B}$): If the predictor predicted the player would take both boxes ($A_2$), Box B contains $\$0$.
* The predictor is $99\%$ accurate: $P(S_1 \mid A_1) = 0.99$ and $P(S_2 \mid A_2) = 0.99$ (so $P(S_2 \mid A_1) = 0.01$ and $P(S_1 \mid A_2) = 0.01$).

Assuming linear utility in dollars ($D(\$x) = x$), the source computes the evidential expected utilities directly from Equation (3):

$$\begin{aligned}
V(\text{take only B}) &= P(\text{1M in box B} \mid \text{take only B}) \times \$1,000,000 + P(\text{nothing in box B} \mid \text{take only B}) \times \$0 \\
&= 0.99 \times \$1,000,000 + 0.01 \times \$0 = \$990,000, \\[6pt]
V(\text{take both boxes}) &= P(\text{1M in box B} \mid \text{take both boxes}) \times \$1,001,000 + P(\text{nothing in box B} \mid \text{take both boxes}) \times \$1,000 \\
&= 0.01 \times \$1,001,000 + 0.99 \times \$1,000 = \$11,000.
\end{aligned}$$

Because $V(\text{take only B}) = \$990,000 > V(\text{take both boxes}) = \$11,000$, EDT recommends one-boxing. Taking only Box B is overwhelming evidence that the predictor foresaw this choice and placed $\$1,000,000$ in Box B. Conversely, CDT recommends two-boxing because the prediction lies in the fixed past: for any prior credence $p = P(S_1) \in [0, 1]$, CDT evaluates $U(\text{take both boxes}) = p(\$1,001,000) + (1-p)(\$1,000) = p(\$1,000,000) + \$1,000 = U(\text{take only B}) + \$1,000$.

#### Parametric Generalization (Author's Extension)
To decide unfamiliar Newcomb-like problems—such as algorithmic trading against a counterparty that models your code, or interacting with a machine-learning classifier trained on your behavioral history—we can generalize the source's numbers. Let Box A contain $c > 0$, Box B contain $M > c$ when one-boxing is predicted, and let the predictor have conditional accuracies $\alpha_1 = P(S_1 \mid A_1)$ and $\alpha_2 = P(S_2 \mid A_2)$ for $A_1 = \text{One-box}$ and $A_2 = \text{Two-box}$. Then:

$$V(A_1) = \alpha_1 M, \qquad V(A_2) = (1 - \alpha_2)(M + c) + \alpha_2 c = (1 - \alpha_2)M + c.$$

Thus, an EDT agent strictly prefers one-boxing ($V(A_1) > V(A_2)$) if and only if:

$$\alpha_1 + \alpha_2 - 1 > \frac{c}{M}. \tag{6}$$

Notice the quantity $\mathcal{I} = \alpha_1 + \alpha_2 - 1 = P(S_1 \mid A_1) - P(S_1 \mid A_2)$, known in probability theory as *Youden's $J$ statistic* or the *evidential diagnosticity* of the action for the state. Equation (6) yields a universal rule for Newcomb problems: **EDT sacrifices a guaranteed causal gain $c$ for an uncertain prize $M$ whenever the evidential diagnosticity of the action exceeds the cost-to-prize ratio $c/M$.** In the Symmetric accuracy case ($\alpha_1 = \alpha_2 = \alpha$), this reduces to $\alpha > \frac{1}{2} + \frac{c}{2M}$. With $c = \$1,000$ and $M = \$1,000,000$, any predictor accuracy above $\alpha^* = 0.5005$ suffices to make one-boxing evidentially optimal.

### 2.2 The Twin Prisoner's Dilemma

Correlation between actions and states need not arise from a prior prediction; it can also arise from a *common cause*, such as shared cognitive architecture. The reference article presents the **Twin Prisoner's Dilemma** (citing Greene & Levinstein 2020), in which Aomame and her psychological twin—whose reasoning processes are exactly analogous to her own—are placed in separate rooms without communication. Each must choose to Cooperate ($C$) or Defect ($D$). The individual payoffs are given by the symmetric payoff matrix:

| Aomame \ Twin | Twin Cooperates ($S_C$) | Twin Defects ($S_D$) |
| :--- | :---: | :---: |
| **Aomame Cooperates ($A_C$)** | $\$5$ | $\$0$ |
| **Aomame Defects ($A_D$)** | $\$10$ | $\$1$ |

In the reference text's exact twin scenario, symmetry of reasoning implies perfect evidential correlation: $P(S_C \mid A_C) = 1$ (so $P(S_D \mid A_C) = 0$) and $P(S_D \mid A_D) = 1$ (so $P(S_C \mid A_D) = 0$). Applying Equation (3), the source computes:

$$\begin{aligned}
V(\text{Aomame cooperates}) &= P(\text{twin cooperates} \mid \text{Aomame cooperates}) \times \$5 + P(\text{twin defects} \mid \text{Aomame cooperates}) \times \$0 \\
&= 1 \times \$5 + 0 \times \$0 = \$5, \\[6pt]
V(\text{Aomame defects}) &= P(\text{twin cooperates} \mid \text{Aomame defects}) \times \$10 + P(\text{twin defects} \mid \text{Aomame defects}) \times \$1 \\
&= 0 \times \$10 + 1 \times \$1 = \$1.
\end{aligned}$$

Since $V(\text{Aomame cooperates}) > V(\text{Aomame defects})$, EDT prescribes cooperation. Even though Aomame cannot causally affect her twin in the other room—and CDT therefore recommends defecting because $\$10 > \$5$ and $\$1 > \$0$—learning that she cooperates is decisive news that her twin also cooperates.

#### Parametric Generalization to Noisy Twins (Author's Extension)
In real-world applications, agents are rarely exact psychological clones; instead, they are *imperfectly correlated peers* (e.g., citizens sharing similar civic norms, or firms using similar optimization heuristics). Consider a general Prisoner's Dilemma with payoffs $T > R > P > S$ (where $R = \text{Reward for mutual cooperation}$, $P = \text{Punishment for mutual defection}$, $T = \text{Temptation to defect}$, and $S = \text{Sucker's payoff}$). Suppose the conditional probabilities of matching are $P(S_C \mid A_C) = 1 - \epsilon_C$ and $P(S_D \mid A_D) = 1 - \epsilon_D$. Then:

$$V(A_C) = (1 - \epsilon_C) R + \epsilon_C S, \qquad V(A_D) = \epsilon_D T + (1 - \epsilon_D) P.$$

Under symmetric diagnosticity ($1 - \epsilon_C = 1 - \epsilon_D = \rho \in [1/2, 1]$), EDT recommends cooperation whenever $V(A_C) > V(A_D)$, which rearranges to:

$$\rho > \frac{P - S}{(R - S) + (P - T)} \quad \text{or equivalently} \quad \rho (R - S) + (1 - \rho)(P - T) > 0.$$

In Aomame's payoff matrix ($T = 10, R = 5, P = 1, S = 0$), $V(A_C) = 5\rho$ and $V(A_D) = 10(1 - \rho) + \rho = 10 - 9\rho$. Cooperation is evidentially optimal whenever $5\rho > 10 - 9\rho$, or $\rho > \frac{10}{14} \approx 0.7143$.

---

## 3. Open Questions in the Source and Operational Proposals

While the reference article clearly presents the core expected-utility equation and the two classic puzzles above, a mathematically literate practitioner who tries to apply Equation (1) to novel decision problems immediately encounters two foundational questions that the brief reference article does not resolve:

1. **The Deliberation Paradox and Zero-Probability Acts**: How is $P(O_j \mid A)$ defined during deliberation, especially for suboptimal actions that a rational agent knows they will not take (where $P(A) = 0$)?
2. **Spurious Confounding ("Managing the News")**: How does EDT respond to the sharp criticisms cited in the reference text from David Lewis (1981) and James M. Joyce (1999)? Specifically, when an action is merely a *symptom* of an undesirable pre-existing state without predicting a decision-responsive partner or predictor, does EDT force the agent to take a causally harmful action just to get "good news"?

In this section, we explain both uncertainties and develop concrete operational rules to resolve them. *(All mathematical models and operational criteria in this section beyond the cited quotes from Lewis and Joyce are our own proposals and extensions.)*

### 3.1 Resolving the Deliberation Paradox: Conditional Kernels and $\epsilon$-Trembles

By Kolmogorov's definition, the conditional probability $P(S_k \mid A_i) = \frac{P(S_k \cap A_i)}{P(A_i)}$ exists only if the agent assigns a strictly positive prior probability $P(A_i) > 0$ to performing action $A_i$. This poses two problems for a practitioner:
* First, some philosophers argue that an agent who is actively deliberating cannot simultaneously hold a probabilistic belief $P(A_i)$ about what they will choose ("deliberation crowds out prediction").
* Second, if an agent knows they are an expected-utility maximizer and computes $V(A_1) > V(A_2)$, they will immediately become certain that they will choose $A_1$, driving $P(A_2) \to 0$ and leaving $V(A_2)$ undefined!

**Operational Proposal**: To make $V(A_i)$ well-defined across all candidate actions in $\mathcal{A}$ regardless of the agent's post-deliberation certainty, we should treat $P(S_k \mid A_i)$ not as a fragile ratio of unconditional credences, but as a **structural Markov transition kernel** (or Rényi-Popper primitive conditional probability) obtained via an $\epsilon$-tremble model of deliberation.

Specifically, suppose the relationship between the background state $S_k$ and the agent's decision process is governed by a joint generative model where, during deliberation, every feasible action $A_i \in \mathcal{A}$ has a small positive execution noise or prior exploratory weight $\epsilon_i > 0$ (similar to trembling-hand perfection in game theory). Under this perturbed measure $P_\epsilon$, $P_\epsilon(A_i) > 0$ for all $A_i \in \mathcal{A}$. We then define the operational evidential conditional probability as the limit:

$$K(S_k \mid A_i) \equiv \lim_{\epsilon \to 0^+} P_\epsilon(S_k \mid A_i). \tag{7}$$

In practice, you do not even need to assign a prior probability $P(A_i)$ to your own acts to compute $K(S_k \mid A_i)$. Instead, you ask an observer-perspective question: *"If a third-party Bayesian observer knew the structural correlation mechanism linking my decision process to the environment, and learned only the datum that my deliberation terminated in action $A_i$, what posterior distribution $K(S_k \mid A_i)$ would they assign to the state space $\mathcal{S}$?"* This formulation guarantees that every available action has a well-defined evidential value $V(A_i) = \sum_k K(S_k \mid A_i) D(A_i, S_k)$.

### 3.2 Criticisms of "Managing the News" and Diagnostic Confounding

In the *Criticism* section of our reference document, two influential objections to EDT are quoted:
* **David Lewis (1981)** characterized evidential decision theory as promoting *"an irrational policy of managing the news."*
* **James M. Joyce (1999)** asserted: *"Rational agents choose acts on the basis of their causal efficacy, not their auspiciousness; they act to bring about good results even when doing so might betoken bad news."*

Why do Lewis and Joyce level this charge? In Newcomb's paradox and the Twin Prisoner's Dilemma, the correlation between your action $A_i$ and the state $S_k$ exists because the predictor or twin is sensitive to the very decision process you are currently executing—and one-boxing agents actually walk away richer than two-boxing agents ($990,000 vs. $11,000 on average). 

However, the reference text does not spell out the class of examples that motivated Lewis and Joyce: **purely diagnostic (or medical) common-cause problems**, often called *Smoking Lesion* or *Symptom-Management* problems in the decision-theory literature. Let us construct a concrete mathematical example of such a problem—explicitly noting that this scenario is our own illustrative model added to explain Lewis and Joyce's critique—and then show how an operational EDT framework handles it.

#### A Diagnostic Confounding Scenario (Author's Illustrative Example)
Suppose a patient must decide between taking a mild prophylactic aspirin ($A_{\text{take}}$) or abstaining ($A_{\text{abstain}}$). Taking the aspirin causally relieves minor discomfort, adding $+1$ unit of utility regardless of the patient's underlying vascular state. However, medical statistics show that a congenital arterial condition ($S_{\text{ill}}$)—which carries a utility penalty of $-100$ compared to being healthy ($S_{\text{well}}$, utility $0$)—also causes a subtle biochemical craving for aspirin prior to diagnosis. 

Consequently, in the general population, $80\%$ of people who choose to take the aspirin have the congenital illness ($P(S_{\text{ill}} \mid A_{\text{take}}) = 0.80$), whereas only $10\%$ of people who abstain have the illness ($P(S_{\text{ill}} \mid A_{\text{abstain}}) = 0.10$). 

If the patient applies Equation (3) naively using the raw population conditional probabilities $P(S_k \mid A_i)$, they compute:

$$\begin{aligned}
V_{\text{naive}}(A_{\text{take}}) &= 0.80(-100 + 1) + 0.20(0 + 1) = -79.2 + 0.2 = -79, \\
V_{\text{naive}}(A_{\text{abstain}}) &= 0.10(-100) + 0.90(0) = -10.
\end{aligned}$$

Because $-10 > -79$, a naive application of Equation (3) tells the patient to abstain from the aspirin! Yet the congenital state $S_{\text{ill}}$ is already fixed in the patient's body, and unlike Newcomb's predictor, a congenital gene did not foresee the patient's rational utility calculation—it merely caused an initial craving. Refusing the aspirin to avoid the "bad news" that one has the gene is precisely what Lewis calls *"an irrational policy of managing the news"* and what Joyce calls choosing acts for their *auspiciousness* rather than their *causal efficacy*.

#### Operational Resolution: Conditioning on the Pre-Choice Evidential State (The "Tickle" Protocol)
How should an EDT practitioner decide an unfamiliar problem where an action correlates with an undesirable background state? Does EDT genuinely compel the patient to refuse the aspirin, or does a careful specification of the conditional probability $P(S_k \mid A_i)$ distinguish medical confounding from Newcomb's paradox?

To resolve this, we must recognize that in Equation (1), the probability measure $P(\cdot)$ is not an anonymous population frequency; it is the **agent's current credal probability function conditioned on all internal and external evidence $E_{\text{pre}}$ available to the agent immediately prior to acting**.

Let us formalize the causal-evidential structure of the two cases:
1. **Case A: Symptom / Common-Cause Confounding ($S \to I \to A$)**. In the medical problem, the hidden congenital state $S$ causes an internal inclination, symptom, or craving $I$ (often called a "tickle" in the literature following Eells 1982), and that inclination $I$ influences the action $A$. Crucially, an introspective agent *already has epistemic access* to their own desires, cravings, and beliefs $I$ before they finalize their choice $A$. Once we condition on the agent's pre-choice mental state $I \subseteq E_{\text{pre}}$, the mental state $I$ **d-separates** (screens off) the action $A$ from the congenital state $S$:
   
   $$P(S_k \mid A_i, I) = P(S_k \mid I) \quad \forall A_i \in \mathcal{A}. \tag{8}$$
   
   Substituting the properly conditioned probability $P(S_k \mid A_i, I)$ into Equation (3), the state probabilities become invariant across actions:
   
   $$V(A_{\text{take}} \mid I) = P(S_{\text{ill}} \mid I)(-100 + 1) + P(S_{\text{well}} \mid I)(0 + 1) = V(A_{\text{abstain}} \mid I) + 1.$$
   
   Thus, when $I$ screens off $A$ from $S$, EDT agrees with CDT and recommends taking the aspirin!

2. **Case B: Predictor or Twin Correlation ($C \to (\text{Full Deliberation Output } A) \text{ and } C \to S$)**. Why does conditioning on $I$ *not* screen off the correlation in Newcomb's paradox or the Twin Prisoner's Dilemma? Because Newcomb's predictor and Aomame's psychological twin do not merely correlate with an initial pre-rational craving $I$; they simulate or mirror the *entire rational calculation* that maps $(I, \text{Decision Rule}) \mapsto A$. Even given full introspection of one's pre-choice inclinations $I$, the final action $A$ remains a decisive epistemic signal of what the predictor's simulation or the twin's identical deliberation produced:
   
   $$P(S_k \mid A_i, I) \neq P(S_k \mid I). \tag{9}$$

*(Note: While some stringent proponents of EDT—such as Ahmed 2021—argue that even if a hypothetical medical case were constructed where $I$ could not be introspected, an EDT agent should still stand their ground and refuse the symptom-correlated act, distinguishing screened-off correlations via Equation (8) from unscreened decision correlations via Equation (9) gives the mathematical practitioner a clean, operational tool to diagnose any unfamiliar dependency structure.)*

---

## 4. Evaluating Policies, Diachronic Consistency, and Normative Uncertainty

So far, we have examined isolated, single-shot actions. However, the reference article also points to two deeper contexts where EDT plays a pivotal role:
1. **Sequential and indexical problems**, specifically the **Sleeping Beauty problem**, where EDT is invoked to analyze Dutch book vulnerabilities (citing Vincent Conitzer 2015).
2. **Meta-decision problems under normative uncertainty**, specifically the **Evidentialist's Wager** (citing MacAskill et al. 2021), where an agent who is unsure whether EDT or CDT is true must choose a policy across correlated decision-makers.

Because the reference text summarizes each of these results in a single paragraph without presenting their underlying equations, let us develop the mathematical mechanics of both. *(The formal derivations in Sections 4.1 and 4.2 are our own mathematical reconstructions of the arguments summarized in the reference article.)*

### 4.1 The Sleeping Beauty Problem and Diachronic Dutch Books

The reference article notes that EDT has been applied to the **Sleeping Beauty problem** to avoid **Dutch book arguments**—series of bets, each acceptable to an agent at the time it is offered, that collectively guarantee a sure loss—for "halfers" (who assign a credence of $1/2$ to the coin landing Heads), though Vincent Conitzer (2015) demonstrates that halfers remain vulnerable to Dutch books even after adopting EDT.

Why does the choice between EDT and CDT matter for Sleeping Beauty, and how does Conitzer's result work mathematically? Let us set up the standard protocol:
* On Sunday, Sleeping Beauty is put to sleep and a fair coin is tossed ($P(\text{Heads}) = P(\text{Tails}) = 1/2$).
* If the coin lands **Heads** ($H$), she is awakened only on **Monday**.
* If the coin lands **Tails** ($T$), she is awakened on **Monday**, given an amnesia-inducing drug that erases her memory of Monday's awakening, and awakened again on **Tuesday**.

Whenever Beauty wakes up, she cannot tell whether it is Monday or Tuesday. A "halfer" holds that upon waking, her credence that the coin landed Heads remains $P(H) = 1/2$, and $P(T) = 1/2$.

Now see what happens when a bookie offers Beauty a bet upon every awakening—say, selling her a ticket that pays $\$1$ if Heads and costs $\$c$ (so net payoff is $1 - c$ if $H$, and $-c$ if $T$).
* **Under CDT**: Because Beauty's decision to accept the bet ($A_{\text{accept}}$) today does not *causally compel* her Tuesday self to accept the bet if the coin landed Tails, CDT evaluates the single awakening's bet in isolation. If $P(H) = 1/2$, CDT accepts any bet with cost $c < 1/2$ (say, $c = 0.40$). Yet if the coin lands Tails, Beauty wakes up *twice* and accepts that same bet on both Monday and Tuesday! Thus, on Heads she wins $1 - 0.40 = +\$0.60$, while on Tails she loses $-0.40 \times 2 = -\$0.80$. Combined with an opposite bet on Sunday (where she sells Heads at price $0.55$, losing $-\$0.45$ on Heads and winning $+\$0.55$ on Tails), she suffers a guaranteed Dutch book loss in every state of the world ($+0.60 - 0.45 = -\$0.15$ on Heads? Wait: if she buys Heads on Monday/Tuesday for $0.40$ and sells a double-stake Heads bet on Sunday for $0.90$ that pays $2$ on Heads, she nets $2(0.60) - 1.10$? More simply: on Sunday, $P(H)=1/2$, so she is willing to pay $\$0.70$ for a contract that pays $\$1.40$ if Tails, netting $-\$0.70$ on $H$ and $+\$0.70$ on $T$. Combined with her awakening bets, she nets $+0.60 - 0.70 = -\$0.10$ on $H$ and $-0.80 + 0.70 = -\$0.10$ on $T$—a sure loss!).
* **How EDT Rescues the Naive Halfer**: Notice that Beauty on Monday and Beauty on Tuesday are **psychological twins**, just like Aomame and her twin! If the coin landed Tails ($T$), Beauty wakes up twice in identical epistemic states. Under EDT, accepting the bet upon waking ($A_{\text{accept}}$) is conclusive evidence that if the state is $T$, she accepts the bet *twice*, incurring a total portfolio payoff of $-2c$ rather than $-c$. Using Equation (3) over global outcomes:
  
  $$V(A_{\text{accept}}) = P(H \mid A_{\text{accept}})(1 - c) + P(T \mid A_{\text{accept}})(-2c). \tag{10}$$
  
  With $P(H \mid A_{\text{accept}}) = P(T \mid A_{\text{accept}}) = 1/2$, Equation (10) yields:
  
  $$V(A_{\text{accept}}) = \frac{1}{2}(1 - c) + \frac{1}{2}(-2c) = \frac{1}{2} - \frac{3}{2}c.$$
  
  Therefore, an EDT halfer accepts the bet upon waking only if $\frac{1}{2} - \frac{3}{2}c > 0 \iff c < \frac{1}{3}$! Even though her belief is $P(H) = 1/2$, the **evidential amplification of correlated awakenings** makes her bet *as if* her credence were $1/3$, blocking the standard Dutch book.

* **Why Conitzer (2015) Shows Dutch Books Persist**: As the reference text notes, Conitzer proves that EDT does not fully immunize halfers against Dutch books. Why? Because if the bookie differentiates the two awakenings using **asymmetric information or randomized bet offers**—or if a halfer must evaluate bets conditioned on indexical propositions like *"Today is Monday"* where $P(H \text{ and Monday}) = 1/2$ vs. $P(T \text{ and Monday}) = 1/4$ (giving conditional credence $P(H \mid \text{Monday}) = 2/3$)—the evidential symmetry between Monday and Tuesday breaks down. When the bookie offers a bet only on one randomly selected awakening or conditions bets on revealed calendar days, the multiplicity factor of $2$ in Equation (10) disappears without restoring martingale consistency between Sunday and Monday credences, allowing a Dutch bookie to extract a guaranteed profit again.

The operational lesson for evaluating **policies** under EDT is crucial: whenever an agent faces repeated decision nodes across time or across amnesia boundaries, EDT does not evaluate the current node's action $A_t$ in isolation. Instead, it evaluates $A_t$ by conditioning on the entire *correlated trajectory of actions* $(A_1, \dots, A_T)$ that the agent's reasoning process will generate in each state $S_k$.

### 4.2 The Evidentialist's Wager: Normative Uncertainty and Correlated Stakes

In the section *Other supporting arguments*, the reference article highlights a striking meta-theoretical argument by William MacAskill, Aron Vallinder, Caspar Österheld, Carl Shulman, and Johannes Treutlein (2021), titled *The Evidentialist's Wager*:

> "Even if one puts less credence on evidential decision theory, it may be reasonable to act as if EDT were true. Namely, because EDT can involve the actions of many correlated decision-makers, its stakes may be higher than causal decision theory and thus take priority."

Let us formalize this wager mathematically so that a reader can apply it when they are uncertain between EDT and CDT.

Suppose you are a **normatively uncertain** agent: you assign subjective credence $q \in (0, 1)$ to the proposition that EDT is the normatively correct decision theory, and credence $1 - q$ to the proposition that CDT is correct. Even if you find CDT philosophically compelling and set $q$ quite low—say, $q = 0.05$ ($5\%$ credence in EDT)—how should you act in a symmetric multi-agent problem?

Consider an $N$-player symmetric public-goods or collective-action game (such as voting, reducing carbon emissions, or cooperating in an $N$-player Prisoner's Dilemma). There are $N$ decision-makers who reason similarly. Each agent $i \in \{1, \dots, N\}$ chooses between two actions:
* **Contribute ($A_C$)**: Incurs a private causal cost $c > 0$ to agent $i$, and causally generates a public benefit $b > 0$ shared by the world (where $b < c < N b$, so contributing is individually costly to a single agent, $b - c < 0$, but socially optimal if everyone contributes, $N b - c > 0$).
* **Free-ride ($A_F$)**: Incurs cost $0$ and generates benefit $0$.

Let $M_{-i} \in \{0, 1, \dots, N-1\}$ denote the number of *other* agents who choose to contribute.
1. **Evaluation under CDT**: Because agent $i$'s choice in isolation does not *causally force* the other $N-1$ agents to contribute, the random variable $M_{-i}$ is causally independent of $A_i$. For any prior expectation $\mu = \mathbb{E}[M_{-i}]$, CDT evaluates:
   
   $$U(A_C) = (\mu + 1)b - c, \qquad U(A_F) = \mu b.$$
   
   The net causal advantage of contributing is strictly negative:
   
   $$\Delta U = U(A_C) - U(A_F) = b - c < 0. \tag{11}$$
   
   Thus, CDT says free-riding beats contributing by $c - b$, regardless of how large the population $N$ is.

2. **Evaluation under EDT**: Suppose that under EDT, your decision to contribute ($A_C$) vs. free-ride ($A_F$) is positively correlated with the choices of the other $N-1$ similarly situated decision-makers, with pairwise evidential diagnosticity $\rho = P(\text{peer } m \text{ chooses } A_C \mid A_C) - P(\text{peer } m \text{ chooses } A_C \mid A_F) > 0$. By linearity of expectation, learning that you choose $A_C$ rather than $A_F$ shifts the expected number of other contributors by $\mathbb{E}[M_{-i} \mid A_C] - \mathbb{E}[M_{-i} \mid A_F] = (N - 1)\rho$. Therefore, the evidential expected utility difference is:
   
   $$\Delta V = V(A_C) - V(A_F) = \bigl[1 + (N - 1)\rho\bigr]b - c. \tag{12}$$

3. **Combining Under Normative Uncertainty (The Wager)**: If we evaluate actions by taking the **meta-expected value** across our normative credences $q$ (for EDT) and $1 - q$ (for CDT), the meta-utility advantage of contributing is:
   
   $$\mathbb{E}_{\text{meta}}[\Delta(A_C, A_F)] = q \Delta V + (1 - q) \Delta U = q \bigl[(N - 1)\rho b + b - c\bigr] + (1 - q)(b - c) = q(N - 1)\rho b - (c - b). \tag{13}$$

Setting $\mathbb{E}_{\text{meta}}[\Delta(A_C, A_F)] > 0$ yields the threshold for the Evidentialist's Wager:

$$q > \frac{c - b}{(N - 1)\rho b}. \tag{14}$$

Look closely at Equation (14). As the number of correlated decision-makers $N$ grows large, the right-hand side $\frac{c - b}{(N - 1)\rho b}$ shrinks at rate $O(1/N)$. For instance, suppose $c = 10$, $b = 1$, $\rho = 0.20$, and there are $N = 1,001$ correlated agents. Then CDT prefers free-riding by $c - b = 9$ units, whereas EDT prefers contributing by $(1 + 1000 \times 0.20)(1) - 10 = +191$ units. By Equation (14), as long as your credence in EDT exceeds $q^* = \frac{9}{200} = 4.5\%$, the high stakes of the $1,000$ correlated agents under EDT swamp the single-agent stakes of CDT, and meta-rationality recommends acting as an evidential decision theorist.

---

## 5. A Practical Protocol for Deciding Unfamiliar Cases

To synthesize our mathematical account into a directly usable tool, here is a five-step operational procedure for applying Evidential Decision Theory to any unfamiliar decision problem:

1. **Specify the Action-State-Outcome Space**:
   List the feasible actions $\mathcal{A} = \{A_1, \dots, A_m\}$ and partition the relevant background uncertainties into mutually exclusive and exhaustive states $\mathcal{S} = \{S_1, \dots, S_n\}$ such that each pair $(A_i, S_k)$ determines an outcome with cardinal desirability $D(A_i, S_k)$.
2. **Condition on Full Pre-Choice Evidence ($E_{\text{pre}}$)**:
   Identify all information, observations, and introspective inclinations $I \subseteq E_{\text{pre}}$ available to the agent *prior* to finalizing the decision.
3. **Audit the Dependency Structure (Screening-Off vs. Decision Correlation)**:
   For each state $S_k$ and action $A_i$, determine the structural conditional probability $K(S_k \mid A_i) = \lim_{\epsilon \to 0^+} P_\epsilon(S_k \mid A_i, E_{\text{pre}})$:
   * *Purely Causal Case*: If $S_k$ is a downstream causal consequence of $A_i$, $K(S_k \mid A_i)$ equals the causal intervention probability $P(A_i \mathrel{\Box\rightarrow} S_k)$, and EDT agrees with CDT.
   * *Screened-Off Common Cause*: If $A_i$ and $S_k$ share a physical common cause that acts exclusively through an already-introspected inclination $I \in E_{\text{pre}}$, then $K(S_k \mid A_i) = P(S_k \mid E_{\text{pre}})$, and EDT again reduces to CDT.
   * *Unscreened Evidential Correlation*: If $S_k$ represents the output of a predictor, algorithmic twin, or symmetric peer group whose state correlates with the final rational output $A_i$ even given $E_{\text{pre}}$, quantify the diagnosticity $\mathcal{I} = K(S_k \mid A_1) - K(S_k \mid A_2) \neq 0$.
4. **Account for Policy Multiplicity (If Sequential/Indexical)**:
   If the problem involves multiple indistinguishable awakenings or repeated symmetric nodes within a single state $S_k$, make sure $D(A_i, S_k)$ aggregates the cumulative payoff of all correlated action instances triggered in state $S_k$ (as in Equation 10).
5. **Compute News Value and Maximize**:
   Calculate the evidential expected utility for each action:
   
   $$V(A_i) = \sum_{k=1}^{n} K(S_k \mid A_i) D(A_i, S_k),$$
   
   and select $A^* \in \arg\max_{A_i \in \mathcal{A}} V(A_i)$ (or apply the meta-decision threshold in Equation 14 if operating under normative uncertainty between EDT and CDT).

---

## 6. Conclusion

Evidential decision theory offers a mathematically elegant and philosophically provocative answer to the problem of rational agency. By grounding expected utility in standard conditional probability $P(O_j \mid A)$ rather than counterfactual intervention $P(A \mathrel{\Box\rightarrow} O_j)$, EDT treats decision-making as seamlessly integrated with Bayesian inference: the rational agent chooses the act whose performance carries the best expected news about the world. 

While critics like David Lewis and James M. Joyce rightly warn against conflating auspicious symptoms with causal efficacy, careful probabilistic modeling—separating pre-choice introspective evidence from genuine decision-level correlations with predictors and peers—clarifies why EDT achieves superior outcomes in Newcomb's paradox and the Twin Prisoner's Dilemma. And as the Evidentialist's Wager demonstrates, in an interconnected world populated by correlated minds and predictive algorithms, the mathematics of news value demands our attention even when we are not fully certain that evidentialism is the final word on rationality.

---

## References

* Ahmed, Arif (2021). *Evidential Decision Theory*. Cambridge University Press. ISBN 9781108607865.
* Conitzer, Vincent (2015). "A Dutch book against sleeping beauties who are evidential decision theorists". *Synthese*, **192** (9): 2887–2899. arXiv:1705.03560. doi:10.1007/s11229-015-0691-7.
* Gibbard, Allan; Harper, William L. (1976). *Counterfactuals and Two Kinds of Expected Utility*, pp. 7–8.
* Greene, Preston; Levinstein, Benjamin (2020). "Act Consequentialism without Free Rides". *Philosophical Perspectives*, **34** (1): 100–101. doi:10.1111/phpe.12138.
* Joyce, James M. (1999). *The Foundations of Causal Decision Theory*, p. 146. Cambridge University Press.
* Lewis, David (1981). "Causal decision theory". *Australasian Journal of Philosophy*, **59** (1): 5–30. doi:10.1080/00048408112340011.
* MacAskill, William; Vallinder, Aron; Österheld, Caspar; Shulman, Carl; Treutlein, Johannes (2021). *The Evidentialist's Wager*. Global Priorities Institute Working Paper.
* Wikipedia contributors (2026). "Evidential decision theory". *Wikipedia, The Free Encyclopedia*. Permanent revision 1373679688.
* Wolpert, David H.; Benford, Gregory (2013). "The lesson of Newcomb's paradox". *Synthese*, **190** (9): 1637–1646. doi:10.1007/s11229-011-9899-3.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining Evidential Reasoning**

I'm now zeroing in on defining "Evidential Reasoning" for the essay. It's becoming clearer I need to highlight its distinction from other probabilistic methods and formal logic. I am also working on clearly outlining the core components and principles that differentiate it from the others. The writing process is currently centered on establishing this foundational understanding for the piece.


**Elaborating EDT's Principles**

I'm now delving into the core tenets of Evidential Decision Theory (EDT). My focus is clarifying "news value" as the central concept. I am now contrasting it with Causal Decision Theory (CDT) and ensuring a clear distinction between the two. The objective is to make all ideas accessible to a mathematically literate audience, and I am careful to separate claims from the Wikipedia article with my own elaborations.


**Contrasting EDT with CDT**

I'm currently working to highlight the formal distinctions between Evidential Decision Theory (EDT) and Causal Decision Theory (CDT). I'm focusing on the mathematical formalisms, namely the expected utility calculations. EDT leverages conditional probabilities, while CDT employs counterfactual probabilities. My analysis is aiming to clarify how these different probability assessments lead to divergent recommendations in scenarios, such as Newcomb's paradox.


**Analyzing EDT's Applications**

My current focus is examining real-world applications and critical evaluations of Evidential Decision Theory (EDT). I've analyzed EDT's implications in several scenarios, including Newcomb's problem, the Twin Prisoner's Dilemma, and the Sleeping Beauty problem. I am also investigating the Evidentialist's Wager and considering potential weaknesses like those pointed out by David Lewis.


**Defining EDT's Framework**

I am now structuring the essay around James Joyce's view of Evidential Decision Theory as a seemingly irrational policy of managing the news. I'm building on Joyce's assertion that rational agents make decisions based on causal efficacy rather than mere auspiciousness. The primary goal is to produce a readable technical piece that mathematically defines EDT with clear equations, examples, and the underlying motivations.


**Refining Framework's Clarity**

I'm making a conscious effort to clearly distinguish the source's claims from my own extrapolations, assumptions, and proposed mathematical structures. I'm aiming for a concise conclusion with references. I'm targeting a length of 2,600-2,800 words. Furthermore, I'm working to expand the source's formula $V(A) = \sum_j P(O_j \mid A) D(O_j)$ into a useful decision framework for unfamiliar cases. I am also investigating the source, noting where the source leaves questions open, such as the state-space vs outcome-space representation of the formula.


**Formalizing Outcome Structure**

I'm now zeroing in on formalizing the state-act-outcome relationship within the EDT framework. I realized we typically don't directly specify probabilities over final outcomes, but rather through states of the world. Therefore, I need to elaborate on the source's formula by explicitly defining how the outcomes $O_{ij}$ are determined by the combination of an action and a state, and formalizing the state-act-outcome matrix translation as my own operational elaboration of the source's equations.


**Addressing EDT's Challenges**

I am now tackling how to handle conditional probabilities when actions become improbable or when faced with common-cause confounding. I aim to propose operational interpretations for practitioners, like regularizing priors with epsilon-trembles, or employing primitive conditional credences to manage the news. I'm investigating why critics claim EDT "manages the news" poorly, and how to model EDT for common-cause confounding like genetic predispositions.


**Clarifying Correlations and Causalities**

I am currently focusing on distinguishing predictor correlations from causal factors, and carefully noting examples as my own extensions beyond the original text. I need to clearly define the difference between smoking-lesion correlations and medical diagnostic examples, while simultaneously analyzing screening-off analysis via introspection. I am taking care to clearly identify these as my own elaborations, so that any claims or analysis remains consistent and accurate.

\n\n

My current effort centers on formalizing the source's ideas on policies, sequential choices, and the Evidentialist's Wager. I'm focusing on the source's brief introductions to the Sleeping Beauty problem and MacAskill et al.'s Evidentialist's Wager to formally build from their existing foundations. I intend to expand the analysis beyond the summaries by formalizing the mathematical equations underlying each scenario to help build a more comprehensive understanding.


**Formalizing Sequential Choices**

I'm now zeroing in on formalizing the source's ideas on policies, sequential choices, and the Evidentialist's Wager. I'm focusing on the source's brief introductions to the Sleeping Beauty problem and MacAskill et al.'s Evidentialist's Wager to formally build from their existing foundations. I intend to expand the analysis beyond the summaries by formalizing the mathematical equations underlying each scenario to help build a more comprehensive understanding. I'm also planning the essay structure, aiming for a blog-style tone that balances technical depth with accessibility. The introduction will frame decision-making as news management, contrasting causal intervention with evidential learning.


**Expanding EDT's Utility**

I'm now zeroing in on expanding the source material's formula by adapting Gibbard and Harper's formulations. My focus is now on applying EDT to novel decision problems, and distinguishing the baseline commitments of the source from our own extensions. I'm noting the source's tendency to sum over outcomes, even while its examples often deal with states and actions. I'm aiming to bridge the mathematical gaps for a more practical understanding.



**Formalizing Conditional Probabilities**

I am now formulating how conditional probabilities are actually written over background states, and linking that back to the outcome calculation. I am now working on formalizing the State-Act-Outcome translation with a formal definition of the action space, state space, and outcome mapping with utility. I am making sure the formalism shows how my version of $V(A_i) = \sum_k P(S_k \mid A_i) D(A_i, S_k)$ maps to the source's formula for outcomes. Furthermore, I am investigating how it is that separating states $\mathcal{S}$ from outcomes $\mathcal{O}$ is essential for deciding unfamiliar problems. Finally, I'm working on explaining the divergence between EDT and CDT in terms of stochastic dependence and counterfactual dependence.


**Analyzing EDT's Paradoxes**

I am now performing a detailed, mathematical walkthrough of Newcomb's Paradox and the Twin Prisoner's Dilemma as presented in the source, as a way to clarify EDT's implications. I'm focusing on deriving a generalized parametric analysis, which I will mark as my own analytical generalization. I am currently working on generalizing the model with an opaque prize $M$, a transparent prize $c$, and varying predictor accuracy $\alpha$. My main goal is to determine the point at which EDT switches its preference from two-boxing to one-boxing, for the purpose of contrasting EDT's decisions with CDT.


**Formalizing Paradox Solutions**

I'm now expanding the analysis by including the generalization of Newcomb's Paradox and the Twin Prisoner's Dilemma. My main goal is to determine the point at which EDT switches its preference from two-boxing to one-boxing, for the purpose of contrasting EDT's decisions with CDT. The goal of this phase is generalizing the Twin Prisoner's Dilemma into a reusable rule for correlated strategic interactions. I'm also adding boxes for all $\alpha$ because $c > 0$.



**Modeling Diagnostic Confounding**

I'm now integrating the use of primitive conditional probability functions or epsilon-tremble perturbed priors. I'm focusing on framing common-cause confounding using a structural correlation kernel. I need to explain the "managing the news" criticism through a diagnostic confounding example, which I will flag as my own illustrative addition, in order to show an example where EDT's recommendations seem counterintuitive.


**Clarifying Screening-Off**

I am now focusing on the importance of conditioning on an agent's initial state $I$ to screen off spurious correlations in EDT, and building from a previous example that uses raw probabilities which leads to a naive version of EDT. I am working towards formalizing this by demonstrating how to condition on the agent's pre-action state, which helps to screen off medical confounding and preserve genuine predictor correlations. I will then explain *evidential screening-off* or *pre-choice state conditioning* protocol, to show how my approach resolves challenges in the source material.


**Formalizing EDT's Wager**

I'm now working through a mathematical reconstruction to address gaps in the source material. I'm focusing on the mechanics of the Sleeping Beauty problem. I'm reconstructing why there is an evidential correlation between acceptance across awakenings. I'm formalizing the multi-step policy's impact. Furthermore, I am formalizing the meta-decision problem where an agent with normative credence $q$ in EDT and $1-q$ in CDT faces repeated decisions.


**Formalizing Strategic Interactions**

I'm now extending my analysis to strategic interactions, contrasting CDT and EDT in multi-agent scenarios. I am now formalizing a version of the Prisoner's Dilemma with $N$ agents. Under EDT, the expected news value scales linearly with $N$ and the correlation $\rho$. This formalism is essential to explore under what conditions a meta-expected utility favors EDT over CDT, which reveals under what conditions we can avoid the typical prisoner's dilemma.


```
