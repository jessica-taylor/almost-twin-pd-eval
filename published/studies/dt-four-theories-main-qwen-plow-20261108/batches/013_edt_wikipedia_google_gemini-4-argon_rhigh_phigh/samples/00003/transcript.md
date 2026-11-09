# 013_edt_wikipedia_google_gemini-4-argon_rhigh_phigh / 00003

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/cbf6c832-9d12-4192-bfbf-38601dd3f1e1/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/cbf6c832-9d12-4192-bfbf-38601dd3f1e1/call_0/response.raw) · finish: `stop`

### Visible response

```text
# News Value and Rational Choice: The Formal Machinery of Evidential Decision Theory

## 1. Introduction: The Geometry of Rational Choice and "News Value"

Every formal theory of decision-making attempts to answer a single foundational question: how should an agent combine beliefs about the world with preferences over outcomes to select an optimal action? In standard expected utility theory, an agent assigns probabilities to uncertain events, assigns numerical utilities (or desirabilities) to consequences, and chooses the action that maximizes expected value. Beneath this seemingly settled surface, however, lies a deep cleavage regarding how an action’s probability distribution over outcomes should be evaluated.

When I contemplate performing an action $A$, should I evaluate $A$ by asking what outcomes $A$ will *causally bring about*? Or should I evaluate $A$ by asking what outcomes become *statistically likely* given the observation that I have chosen $A$?

**Evidential decision theory** (EDT) champions the second approach. As summarized in our reference material, EDT holds that a rational agent confronting a set of possible actions should select the option with the highest *news value*—the action that would be indicative of the best outcome in expectation if the agent received the "news" that the action had been taken. In the memorable aphorism of Arif Ahmed (2021), EDT instructs you to "do what you most want to learn that you will do."

This principle stands in sharp opposition to **causal decision theory** (CDT), which insists that rational agents must choose actions based on their downstream causal efficacy rather than their statistical auspiciousness (Joyce, 1999; Lewis, 1981). In ordinary decision problems—where your choice is statistically independent of everything that precedes it—evidential and causal evaluations coincide. Learning that you took an umbrella is good news about staying dry precisely because the umbrella causally blocks the rain. Yet in environments populated by accurate predictors, symmetrical peers, or shared pre-existing causes, an action can carry vital diagnostic information about states of the world over which the agent has no causal control. In such environments, EDT and CDT diverge dramatically.

In this essay, we will examine the mathematical architecture of Evidential Decision Theory, trace its application across canonical philosophical puzzles, and address several foundational questions that the concise reference formulation leaves open. To make the theory fully actionable for unfamiliar decision problems, I will carefully separate the core principles and equations established in the reference text from my own formal extensions and operational proposals. By the end of this exposition, you will have both the philosophical context and an explicit algorithmic protocol for applying EDT to novel strategic environments.

---

## 2. The Formal Architecture: Gibbard-Harper Expected Utility

### 2.1 The Reference Formulation

The mathematical distinction between evidential and causal expected utility was crystallized in a seminal 1976 paper by Allan Gibbard and William Harper. Following the reference text, let an agent face a choice among candidate actions $A$, and let $\{O_j\}$ denote a collection of possible outcomes, each assigned a numerical desirability $D(O_j) \in \mathbb{R}$.

Evidential decision theory evaluates an action $A$ by computing its expected desirability using standard conditional probabilities:

$$V(A) = \sum_{j} P(O_j \mid A) D(O_j)$$

Here, $V(A)$ represents the *news value* (or evidential expected utility) of action $A$, and $P(O_j \mid A)$ is the conditional probability that outcome $O_j$ obtains given that action $A$ occurs.

By contrast, causal decision theory replaces the conditional probability $P(O_j \mid A)$ with a counterfactual probability:

$$U(A) = \sum_{j} P(A \mathrel{\Box\rightarrow} O_j) D(O_j)$$

where the expression $P(A \mathrel{\Box\rightarrow} O_j)$ denotes the probability of outcome $O_j$ in the counterfactual situation in which action $A$ were performed. As Gibbard and Harper (1976) demonstrated, $P(O_j \mid A)$ and $P(A \mathrel{\Box\rightarrow} O_j)$ need not be equal. Whenever an action $A$ provides evidence about the state of the world without causally influencing that state, the conditional probability diverges from the counterfactual probability, and the rankings induced by $V(\cdot)$ and $U(\cdot)$ can conflict.

### 2.2 Formal Extension: State-Act Partitions and Bayesian Mechanics

*(Note: While the reference article presents the Gibbard-Harper formulas directly in terms of outcomes $O_j$, applying the theory to arbitrary decision problems requires specifying the internal structure of these outcomes and the underlying probability space. The following measure-theoretic formalization is my own analytical elaboration of the source equations.)*

To apply $V(A)$ systematically to unfamiliar cases, it is helpful to decompose abstract "outcomes" into actions and background states of nature. Let $(\Omega, \mathcal{F}, P)$ be a probability space representing the agent's epistemic state prior to completing deliberation. Within the event algebra $\mathcal{F}$, we identify two finite partitions of the sample space $\Omega$:

1. **The Action Partition** $\mathcal{A} = \{A_1, A_2, \dots, A_n\}$, where each $A_k \in \mathcal{F}$ is the proposition that the agent performs action $k$, with $\bigcup_{k=1}^n A_k = \Omega$ and $A_k \cap A_l = \emptyset$ for $k \neq l$.
2. **The State Partition** $\mathcal{S} = \{S_1, S_2, \dots, S_m\}$, where each $S_i \in \mathcal{F}$ represents a mutually exclusive and exhaustive specification of all relevant external circumstances—such as the contents of an opaque box, the strategy chosen by a counterpart, or a hidden biological condition.

An individual outcome $O_j$ is then a fine-grained conjunction $O_{k,i} = A_k \cap S_i$, which fully determines the payoff $D(A_k \cap S_i)$ (often written simply as $D(A_k, S_i)$). Notice that if the agent conditions on taking action $A_k$, any outcome $O_{l,i} = A_l \cap S_i$ with $l \neq k$ is disjoint from $A_k$, yielding $P(O_{l,i} \mid A_k) = 0$. For $l = k$, the definition of conditional probability gives:

$$P(O_{k,i} \mid A_k) = \frac{P((A_k \cap S_i) \cap A_k)}{P(A_k)} = \frac{P(A_k \cap S_i)}{P(A_k)} = P(S_i \mid A_k)$$

assuming $P(A_k) > 0$. Substituting this decomposition into the Gibbard-Harper formula yields the workhorse state-partition equation of EDT:

$$V(A_k) = \sum_{i=1}^{m} P(S_i \mid A_k) D(A_k, S_i)$$

What makes EDT distinctive is its reliance on the ordinary Bayesian ratio $P(S_i \mid A_k) = P(S_i \cap A_k) / P(A_k)$. Standard conditional probability is entirely symmetric with respect to causal direction. By Bayes' Theorem, we can write:

$$P(S_i \mid A_k) = \frac{P(A_k \mid S_i) P(S_i)}{\sum_{r=1}^{m} P(A_k \mid S_r) P(S_r)}$$

Consider what this equation implies about dependencies and counterfactuals:
* **Purely Evidential Dependencies:** Suppose $S_i$ is fixed in the past (so $A_k$ cannot causally affect $S_i$), yet $S_i$ and $A_k$ share a common cause $C$, or $S_i$ was generated by a process that predicted $A_k$. Then the likelihood $P(A_k \mid S_i)$ varies across states $S_i$, ensuring that $P(S_i \mid A_k) \neq P(S_i)$. EDT incorporates this correlation directly into the valuation of $A_k$.
* **The Counterfactual Contrast:** In CDT, if $S_i$ is causally independent of $A_k$, the counterfactual probability severs the backtracking statistical link between action and state: $P(A_k \mathrel{\Box\rightarrow} S_i) = P(S_i)$. Thus, under causal independence of states from acts, CDT evaluates $U(A_k) = \sum_{i=1}^m P(S_i) D(A_k, S_i)$, treating the probability of every background state as invariant across the agent's choices. EDT rejects this invariance whenever the agent's choice is statistically informative about which state actually obtains.

---

## 3. Canonical Thought Experiments: Tracing the Mechanics

The reference article highlights two classic decision problems that expose the mechanics of evidential conditioning: **Newcomb's Paradox** and the **Twin Prisoner's Dilemma**. Let us walk through both using our formal state-act framework.

### 3.1 Newcomb's Paradox

Introduced into philosophy by Robert Nozick and analyzed extensively in the decision theory literature (Wolpert & Benford, 2013; Ahmed, 2021), Newcomb's paradox involves an agent, two boxes (designated A and B), and a highly reliable predictor. 

As specified in the reference text, the rules are known to the player:
* **Box A** is transparent and always contains a visible $\$1,000$.
* **Box B** is opaque, and its content has already been set by the predictor prior to the decision:
  * If the predictor predicted the player will take *only Box B* (one-boxing), Box B contains $\$1,000,000$.
  * If the predictor predicted the player will take *both Boxes A and B* (two-boxing), Box B contains $\$0$.
* The predictor is $99\%$ accurate.

Let us map this into our state-act partition. The action space is $\mathcal{A} = \{\text{take only B}, \text{take both boxes}\}$. The state space tracks the content of Box B: $\mathcal{S} = \{\text{1M in box B}, \text{nothing in box B}\}$. Assuming desirability scales linearly with dollar payoffs, the payoff matrix $D(A_k, S_i)$ is:

| Action \ State | $S_1$: 1M in box B | $S_2$: Nothing in box B |
| :--- | :---: | :---: |
| **$A_1$: Take only B** | $\$1,000,000$ | $\$0$ |
| **$A_2$: Take both boxes** | $\$1,001,000$ | $\$1,000$ |

Notice that in every column, taking both boxes yields strictly more money ($\$1,000$ more) than taking only Box B. Because the predictor has already placed the money and walked away, the player's present choice has zero causal effect on whether $S_1$ or $S_2$ obtains. Consequently, Causal Decision Theory applies dominance reasoning—or equivalently notes that $P(A_k \mathrel{\Box\rightarrow} S_i) = P(S_i)$—and recommends taking both boxes:

$$U(\text{take both boxes}) = P(S_1)(\$1,001,000) + P(S_2)(\$1,000) > P(S_1)(\$1,000,000) + P(S_2)(\$0) = U(\text{take only B})$$

Evidential Decision Theory reaches the opposite verdict because it conditions on the action. As stated in the reference text, the $99\%$ reliability of the predictor implies the conditional probabilities $P(\text{1M in box B} \mid \text{take only B}) = 0.99$ and $P(\text{nothing in box B} \mid \text{take both boxes}) = 0.99$. Plugging these directly into the Gibbard-Harper news-value equation gives:

$$\begin{aligned}
V(\text{take only B}) &= P(\text{1M in box B} \mid \text{take only B}) \times \$1,000,000 + P(\text{nothing in box B} \mid \text{take only B}) \times \$0 \\
&= 0.99 \times \$1,000,000 + 0.01 \times \$0 = \$990,000
\end{aligned}$$

$$\begin{aligned}
V(\text{take both boxes}) &= P(\text{1M in box B} \mid \text{take both boxes}) \times \$1,001,000 + P(\text{nothing in box B} \mid \text{take both boxes}) \times \$1,000 \\
&= 0.01 \times \$1,001,000 + 0.99 \times \$1,000 = \$11,000
\end{aligned}$$

Because $V(\text{take only B}) = \$990,000 > \$11,000 = V(\text{take both boxes})$, EDT unambiguously prescribes taking only Box B. Learning that you are a one-boxer is overwhelmingly good news about the state of Box B; learning that you are a two-boxer is catastrophic news.

### 3.2 The Twin Prisoner's Dilemma

Our second canonical example from the source is the **Twin Prisoner's Dilemma** (Greene & Levinstein, 2020). Here, an agent named Aomame is placed in an isolated room and must choose whether to cooperate ($C$) or defect ($D$) in a one-shot game against her psychological twin, who sits in a separate room and cannot communicate with her. Because they are psychological twins, their reasoning processes are completely analogous.

Assuming Aomame cares purely about her own individual financial payout, the payoff structure given in the reference text is:
* If both cooperate, each receives $\$5$.
* If both defect, each receives $\$1$.
* If one cooperates and the other defects, the defector receives $\$10$ and the cooperator receives $\$0$.

In a standard Prisoner's Dilemma against an independent opponent, defection strictly dominates cooperation ($10 > 5$ and $1 > 0$). Because Aomame and her twin are physically isolated in separate rooms, Aomame's choice cannot causally affect her twin's action. Thus, CDT treats the twin's action as causally independent of Aomame's choice and prescribes defection—locking both twins into the dismal $(\$1, \$1)$ outcome.

EDT evaluates the situation through the lens of diagnostic symmetry. Because the twin's cognitive architecture mirrors Aomame's, Aomame's decision is near-certain (or in the idealized limit, certain) evidence of her twin's decision:

$$P(\text{twin cooperates} \mid \text{Aomame cooperates}) = 1, \quad P(\text{twin defects} \mid \text{Aomame defects}) = 1$$

Computing the evidential expected utilities exactly as shown in the reference text:

$$\begin{aligned}
V(\text{Aomame cooperates}) &= P(\text{twin cooperates} \mid \text{Aomame cooperates}) \times \$5 + P(\text{twin defects} \mid \text{Aomame cooperates}) \times \$0 \\
&= 1 \times \$5 + 0 \times \$0 = \$5
\end{aligned}$$

$$\begin{aligned}
V(\text{Aomame defects}) &= P(\text{twin cooperates} \mid \text{Aomame defects}) \times \$10 + P(\text{twin defects} \mid \text{Aomame defects}) \times \$1 \\
&= 0 \times \$10 + 1 \times \$1 = \$1
\end{aligned}$$

Since $V(\text{Aomame cooperates}) = \$5 > \$1 = V(\text{Aomame defects})$, EDT prescribes cooperation. Without any physical signaling channel, evidential conditioning transforms a non-cooperative social dilemma into a cooperative coordination equilibrium among symmetrically reasoning agents.

---

## 4. Open Questions in the Reference Text and Operational Proposals

While the reference article succinctly states the Gibbard-Harper formula and summarizes its flagship applications, criticisms, and extensions, a mathematically literate practitioner who attempts to apply this brief summary to real-world or unfamiliar decision problems will immediately encounter four major operational gaps. In this section, I identify where the source material leaves crucial technical questions open and develop rigorous mathematical interpretations of my own to make the theory fully operational.

### 4.1 Open Question 1: How are Conditional Probabilities Derived from Prior Beliefs?

Look closely at the Newcomb calculation in the reference text. The article states that the predictor is "$99\%$ accurate" and immediately substitutes $P(\text{1M in box B} \mid \text{take only B}) = 0.99$ into $V(\text{take only B})$. 

**The Unresolved Uncertainty:** In probability theory, "predictor accuracy" is most naturally defined as the *forward likelihood* that the predictor predicts correctly given the agent's actual disposition or action—that is, $P(\text{Predicted } A_k \mid A_k) = 0.99$—or the conditional probability of the action given the prediction, $P(A_k \mid \text{Predicted } A_k) = 0.99$. By Bayes' Theorem, the inverse probability $P(\text{Predicted } A_k \mid A_k)$ equals $0.99$ *only under specific assumptions about the prior distribution* $P(A_k)$ or $P(\text{Predicted } A_k)$! Moreover, what happens if an agent is already nearly certain during deliberation that they will choose one option, driving $P(A_{\text{other}}) \to 0$ and threatening to leave $P(S_i \mid A_{\text{other}}) = 0/0$ undefined? The reference text leaves the derivation of these conditional probabilities—and the handling of boundary priors—completely unspecified.

**Operational Proposal (Deliberative Priors and Trembling-Hand Conditioning):** To apply EDT to unfamiliar problems where you are given causal or generative parameters rather than pre-computed inverse probabilities, we must explicitly model the joint probability distribution over states and actions under a *deliberative prior*.

Suppose a predictor observes your cognitive state and predicts $S_1$ (one-boxing) or $S_2$ (two-boxing) with symmetric diagnostic sensitivity $\alpha \in (0.5, 1)$ (where $\alpha = 0.99$ in our example), meaning $P(S_k \mid A_k) = \alpha$ when the agent's pre-deliberative prior over actions is uniform, $P(A_1) = P(A_2) = 1/2$. What if the problem instead specifies the generative accuracy of the predictor as $P(A_k \mid S_k) = \alpha$ alongside a prior belief $P(S_1) = p$ that the predictor expects one-boxing? Then a practitioner must use Bayes' rule to compute the evidential weights:

$$P(S_1 \mid A_1) = \frac{P(A_1 \mid S_1) P(S_1)}{P(A_1 \mid S_1) P(S_1) + P(A_1 \mid S_2) P(S_2)} = \frac{\alpha p}{\alpha p + (1 - \alpha)(1 - p)}$$

Furthermore, to prevent $P(S_i \mid A_k)$ from becoming undefined when an agent settles on a deterministic policy (so $P(A_k) \to 0$ for rejected actions), we can operationalize EDT using a **trembling-hand deliberative measure** $P_\epsilon$. Assume that regardless of the agent's final preference, biological or computational noise ensures each available action $A_k \in \mathcal{A}$ has a minimum baseline probability $\epsilon > 0$ of being executed via an independent "tremble" event $E_{\text{tremble}}$, while with probability $1 - n\epsilon$ the action reflects the agent's authentic cognitive disposition (which correlates with external predictors or twins). We then define the news value via the well-defined limit:

$$V(A_k) = \lim_{\epsilon \to 0^+} \sum_{i=1}^{m} P_\epsilon(S_i \mid A_k) D(A_k, S_i)$$

This operationalization guarantees that $P(O_j \mid A)$ is strictly well-defined across all candidate actions and recovers the exact numbers of the reference text when $p = 1/2$ and $\alpha = 0.99$.

### 4.2 Open Question 2: "Managing the News" vs. Diagnostic Screening-Off

In its **Criticism** section, the reference article quotes two famous objections to EDT:
1. David Lewis (1981) characterizes EDT as promoting "an irrational policy of managing the news."
2. James M. Joyce (1999) asserts: "Rational agents choose acts on the basis of their *causal efficacy*, not their auspiciousness; they act to *bring about* good results even when doing so might betoken bad news."

**The Unresolved Uncertainty:** Why do Lewis and Joyce accuse EDT of "managing the news"? The reference article states their criticism but does not explain the structure of the counterexamples that motivate it, nor how an EDT practitioner should evaluate everyday confounding. 

Consider a classic *Medical Newcomb Problem* (a standard philosophical test case not detailed in the source text, which we introduce here to operationalize the Lewis/Joyce critique): Suppose a hidden genetic mutation $G$ causes both a devastating future illness $I$ and a harmless behavioral craving $A$ (say, an urge to eat a particular bitter herb that has zero causal effect on the illness). If you observe a population member eating the herb, that action is strong statistical evidence that they carry gene $G$ and will suffer illness $I$: $P(I \mid A) \gg P(I \mid \neg A)$. Does EDT therefore tell an agent who craves the herb to abstain from eating it, merely to avoid receiving the "bad news" that they carry the gene? If EDT forces you to suppress harmless desires just to manipulate your own self-diagnosis, Lewis and Joyce's criticism seems devastating.

**Operational Proposal (Introspective Conditioning and the Screening-Off Test):** To give EDT its strongest and most coherent operational interpretation in unfamiliar cases, we must specify *what background information the agent conditions on prior to evaluating actions*. 

In our formal setup, probability $P(\cdot)$ is not the detached probability distribution of an outside statistician; it is the *epistemic probability distribution of the agent at the moment of deliberation*, already conditioned on everything the agent can introspectively observe about their own desires, cravings, and beliefs. Let $C$ denote the agent's conscious introspective state (the craving or "tickle" to eat the herb) right before choosing $A$. 

Look at the causal graph of the Medical Confounding problem versus Newcomb's Paradox:
* **Case A: Medical Confounding (Mediated by Introspectable Urges).** Here, the gene $G$ causes the conscious craving $C$, and the craving $C$ inclines the agent to choose action $A$:
  $$I \longleftarrow G \longrightarrow C \longrightarrow A$$
  In this structure, the conscious craving $C$ **screens off** the action $A$ from the genetic state $G$ and the illness $I$. Once the agent notices inside their own mind, "I strongly crave this bitter herb" (conditioning on $C$), choosing to indulge the craving ($A$) or grimly forcing themselves to abstain ($\neg A$) provides *no further information* about $G$:
  $$P(I \mid A, C) = P(I \mid \neg A, C) = P(I \mid C)$$
  When we evaluate news value conditional on the agent's current introspective evidence $C$:
  $$V(A \mid C) = \sum_{S_i} P(S_i \mid A, C) D(A, S_i) = \sum_{S_i} P(S_i \mid C) D(A, S_i)$$
  Because $P(S_i \mid C)$ is invariant across $A$ and $\neg A$, the spurious diagnostic correlation vanishes! The EDT agent eats the herb and enjoys it, completely immune to Lewis's charge of "managing the news."

* **Case B: Direct Algorithmic Prediction (Newcomb and Twin PD).** Why doesn't introspective conditioning screen off the predictor in Newcomb's Paradox or the twin in the Twin Prisoner's Dilemma? Because the predictor is not merely detecting a pre-choice craving $C$; the predictor (or twin) is simulating or mirroring *the final transition from deliberation to action itself* ($C \to A$). Even given the agent's initial introspective state $C$, the final choice $A$ remains directly correlated with the predictor's output $S$:
  $$P(S \mid A, C) \neq P(S \mid \neg A, C)$$

**The Operational Rule:** This distinction gives our readers a sharp mathematical test for unfamiliar cases. Before computing $V(A)$, always condition your probability distribution on your full pre-action introspective evidence $C$. If the external state $S$ is conditionally independent of $A$ given $C$ ($S \perp A \mid C$), EDT reduces to CDT. Only when the correlation between $A$ and $S$ survives conditioning on all pre-choice evidence—as occurs when facing predictors, algorithmic clones, or correlated rational peers—does EDT depart from causal expected utility.

### 4.3 Open Question 3: Dynamic Consistency and the Sleeping Beauty Problem

In its brief section on the **Sleeping Beauty problem**, the reference article notes that EDT has been applied to the problem to avoid **Dutch book arguments** (systems of bets that guarantee a sure loss). Specifically, it states that some argue Sleeping Beauty is vulnerable to Dutch books if she assigns a credence of $1/2$ to the coin landing heads ("halfer" position) but can avoid them by adopting EDT—while noting that Vincent Conitzer (2015) proved that halfers remain vulnerable to a Dutch book even after adopting EDT.

**The Unresolved Uncertainty:** Because the reference article summarizes this debate in two sentences without defining the Sleeping Beauty setup or explaining how EDT alters betting behavior across awakenings, a reader cannot see *why* EDT blocks standard diachronic Dutch books for halfers, nor how Conitzer's counter-construction circumvents that protection.

**Operational Proposal (Modeling Self-Locating Evidential Correlations):** Let us reconstruct the mathematical mechanics to make this application transparent. In the standard Sleeping Beauty problem:
* Beauty is put to sleep on Sunday, and a fair coin is tossed ($P(\text{Heads}) = 1/2, P(\text{Tails}) = 1/2$).
* If **Heads** ($H$), she is awakened on **Monday** only.
* If **Tails** ($T$), she is awakened on **Monday**, has her memory of Monday erased by an amnesia drug, and is awakened again on **Tuesday**.
* Upon each awakening, she has no memory of which day it is.

Suppose Beauty is a "halfer": upon waking, she maintains credence $P(H) = 1/2$ and $P(T) = 1/2$. Why does a causal decision theorist who is a halfer fall prey to a trivial Dutch book? 
Because if $P(T) = 1/2$, a CDT agent upon waking is willing to accept a bet $B_T$ that pays $+\$10$ if $T$ and costs $-\$11$ if $H$ (since causal expected value is $\frac{1}{2}(10) + \frac{1}{2}(-11) = -\$0.50$, wait—reverse the signs: a bet that pays $+\$11$ if $H$ and $-\$10$ if $T$ has positive causal expectation $\frac{1}{2}(11) - \frac{1}{2}(10) = +\$0.50$). However, if the bookie offers this identical bet *every time Beauty wakes up*, notice what happens in the actual world:
* If $H$ occurs, Beauty wakes up **once** (Monday) and wins $+\$11$.
* If $T$ occurs, Beauty wakes up **twice** (Monday and Tuesday), accepts the bet both times, and loses $-\$10 + (-\$10) = -\$20$!

Measured from Sunday before going to sleep, accepting this bet upon waking yields an objective expected payout of $\frac{1}{2}(\$11) + \frac{1}{2}(-\$20) = -\$4.50$. By combining this waking bet with a Sunday hedge bet (e.g., paying Beauty $\$15$ if $T$ and charging $-\$13$ if $H$, which has Sunday expected value $+\$1.00$), the bookie inflicts a guaranteed net loss on the CDT halfer in every state of the world ($-\$2$ on Heads, $-\$5$ on Tails).

**How EDT Protects the Halfer:** Now watch what happens when Beauty uses Evidential Decision Theory upon waking! When Beauty wakes up and deliberates whether to accept ($A_{\text{acc}}$) or reject ($A_{\text{rej}}$) the bet that pays $+\$11$ on $H$ and $-\$10$ on $T$, she recognizes that her Monday self and her Tuesday self (if $T$ obtains) are **psychological twins** facing the exact same epistemic state. Therefore, choosing $A_{\text{acc}}$ during the current awakening is certainty-level evidence ($P = 1$) that if the coin landed Tails, her counterpart on the other awakening *also* chooses $A_{\text{acc}}$!

Thus, conditional on $A_{\text{acc}}$ and state $T$, the outcome is not a single loss of $-\$10$, but a *double loss* of $-\$20$:

$$V(A_{\text{acc}}) = P(H \mid A_{\text{acc}})(\$11) + P(T \mid A_{\text{acc}})(-\$20) = \frac{1}{2}(\$11) + \frac{1}{2}(-\$20) = -\$4.50 < 0 = V(A_{\text{rej}})$$

Because $V(A_{\text{acc}}) < V(A_{\text{rej}})$, the EDT halfer refuses the waking bet, blocking the classic diachronic Dutch book! (As Conitzer (2015) demonstrated, however, if the bookie introduces asymmetric information or randomized visual cues across awakenings that break the exact evidential symmetry between Monday and Tuesday while preserving the halfer's marginals, a more sophisticated Dutch book can still be constructed.)

### 4.4 Open Question 4: Formalizing "The Evidentialist's Wager"

In the section **Other supporting arguments**, the reference text notes a remarkable meta-theoretical claim due to MacAskill, Vallinder, Österheld, Shulman, and Treutlein (2021): even if an agent places less credence in EDT than in CDT, it may still be rational to act as if EDT were true. Because EDT accounts for the actions of many correlated decision-makers, its stakes are often vastly higher than those of CDT, allowing EDT to dominate in meta-expectation.

**The Unresolved Uncertainty:** The reference text summarizes the qualitative conclusion of *The Evidentialist's Wager* without writing down the meta-decision matrix or showing mathematically how the number of correlated peers tips the scales.

**Operational Proposal (A Mathematical Model of Normative Uncertainty):** Let us formalize this wager so a reader can compute the exact threshold at which a CDT-leaning agent should switch to EDT policies.

Suppose an agent is uncertain which decision theory is normatively correct, assigning credence $q \in (0, 1)$ to EDT and credence $1 - q$ to CDT. The agent faces a generalized symmetric social dilemma (such as contributing to a global public good, voting, or refraining from polluting) alongside $N$ psychologically similar agents.
* **Cost of Cooperating ($C$) vs. Defecting ($D$):** Choosing $C$ imposes a direct personal causal cost of $c > 0$ on the agent, but generates a public benefit $b > 0$ for everyone (including the agent), where $0 < b < c$ (so a single isolated contribution is a net personal loss of $b - c < 0$, while mutual cooperation yields $(N+1)b - c > 0$).
* **Correlation:** If the agent chooses $C$, the expected fraction of the $N$ peers who also choose $C$ is $\rho_C$; if the agent chooses $D$, the expected fraction of peers who choose $C$ is $\rho_D$, with $\Delta\rho = \rho_C - \rho_D > 0$.

Now compare how the two candidate theories measure the net benefit of choosing $C$ over $D$:
1. **According to CDT:** Your choice does not causally affect the $N$ peers. Therefore, choosing $C$ over $D$ has a strictly negative causal expected value equal to the isolated personal net cost:
   $$\Delta U = U(C) - U(D) = b - c < 0$$
2. **According to EDT:** Choosing $C$ is evidence that an additional $\Delta\rho \cdot N$ peers also choose $C$, each contributing $b$ to your payoff. Thus, the evidential expected advantage of $C$ over $D$ scales linearly with $N$:
   $$\Delta V = V(C) - V(D) = (b - c) + N \cdot \Delta\rho \cdot b$$

If the meta-agent evaluates actions by taking the credence-weighted average of their normalized theoretical values:

$$\mathcal{M}(C) - \mathcal{M}(D) = q \cdot \Delta V + (1 - q) \cdot \Delta U = q \big[(b - c) + N \Delta\rho b\big] + (1 - q)(b - c) = (b - c) + q N \Delta\rho b$$

Consequently, choosing $C$ maximizes meta-expected value whenever:

$$q > q^* = \frac{c - b}{N \cdot \Delta\rho \cdot b}$$

Notice the behavior of the threshold $q^*$ as the population of correlated peers $N$ grows large: $q^* = \mathcal{O}(1/N)$. Even if you are $99\%$ confident in Causal Decision Theory ($q = 0.01$), if $c = 2$, $b = 1$, $\Delta\rho = 0.5$, and you are one of $N = 1,000$ correlated decision-makers, your threshold is $q^* = \frac{1}{500} = 0.002 < 0.01$. Because CDT cares only about your solitary $\mathcal{O}(1)$ causal footprint while EDT tracks the $\mathcal{O}(N)$ correlated ensemble, the high stakes of the evidentialist perspective overwhelm the agent's high credence in causalism.

---

## 5. An Algorithmic Protocol for Unfamiliar Cases (With a Worked Example)

To synthesize the reference framework and our operational extensions into a practical tool, here is a five-step protocol for resolving any unfamiliar decision problem using Evidential Decision Theory:

1. **Specify the Action and State Partitions:** Define the set of mutually exclusive available actions $\mathcal{A} = \{A_1, \dots, A_n\}$ and the partition of relevant external states $\mathcal{S} = \{S_1, \dots, S_m\}$.
2. **Construct the Desirability Matrix:** Assign utilities $D(A_k, S_i) \in \mathbb{R}$ to every action-state pair $(A_k, S_i)$.
3. **Apply the Introspective Screening-Off Filter:** Identify your complete pre-decision introspective evidence $C$ (conscious desires, symptoms, and prior observations). Ask whether the statistical correlation between $A_k$ and $S_i$ is completely mediated by $C$. For any state component where $P(S_i \mid A_k, C) = P(S_i \mid C)$, replace the conditional probability with the constant baseline $P(S_i \mid C)$.
4. **Compute Surviving Evidential Likelihoods via Bayes' Rule:** For states $S_i$ that remain correlated with $A_k$ even conditional on $C$ (e.g., predictors, algorithmic twins, self-locating duplicates), use the problem's prior $P(S_i \mid C)$ and predictive accuracy $P(A_k \mid S_i, C)$ to calculate:
   $$P(S_i \mid A_k, C) = \frac{P(A_k \mid S_i, C) P(S_i \mid C)}{\sum_{r=1}^m P(A_k \mid S_r, C) P(S_r \mid C)}$$
5. **Maximize News Value:** Compute $V(A_k \mid C) = \sum_{i=1}^m P(S_i \mid A_k, C) D(A_k, S_i)$ for each $A_k \in \mathcal{A}$ and select $\arg\max_{A_k} V(A_k \mid C)$.

### Worked Example: The Correlated Algorithmic Liquidity Crisis

*(Note: The following problem is an original scenario designed to demonstrate how our five-step protocol resolves a realistic, multi-layered decision case.)*

Suppose you manage an automated quantitative trading desk. A sudden macroeconomic shock hits the market, and you must decide within milliseconds whether to **Hold ($A_H$)** your leveraged portfolio or **Liquidate ($A_L$)** into cash.
* **Confounding Factor (Screened Off):** Market rumors suggest that funds experiencing high internal server latency during this shock also happen to hold toxic subprime assets. You observe your own server latency $C$ directly before making the decision, and you know your portfolio's asset composition.
* **Symmetric Peers (Unscreened):** Across the financial system, there are $M$ other quantitative funds running the exact same open-source risk-management architecture and trained on the same historical data as your desk. Because they face the identical market feed, your decision is diagnostic of whether the broader quant cohort liquidates ($S_{\text{crash}}$: a flash crash occurs) or holds ($S_{\text{stable}}$: the market stabilizes).
* **Parameters:** Conditional on your pre-choice observation $C$, your prior probability of a flash crash is $P(S_{\text{crash}} \mid C) = 0.40$ and stability is $P(S_{\text{stable}} \mid C) = 0.60$. Given the shared algorithmic architecture, if the quant cohort triggers a flash crash ($S_{\text{crash}}$), there is an $85\%$ probability that your analysis also leads you to liquidate: $P(A_L \mid S_{\text{crash}}, C) = 0.85$ (so $P(A_H \mid S_{\text{crash}}, C) = 0.15$). Conversely, if the cohort holds and the market stabilizes ($S_{\text{stable}}$), there is an $80\%$ probability that your analysis leads you to hold: $P(A_H \mid S_{\text{stable}}, C) = 0.80$ (so $P(A_L \mid S_{\text{stable}}, C) = 0.20$).
* **Payoffs $D(A_k, S_i)$:**
  * If $S_{\text{stable}}$ and you **Hold ($A_H$)**, your portfolio rebounds for $+100$ utility.
  * If $S_{\text{stable}}$ and you **Liquidate ($A_L$)**, you lock in transaction costs for $-10$ utility.
  * If $S_{\text{crash}}$ and you **Hold ($A_H$)**, margin calls wipe you out for $-200$ utility.
  * If $S_{\text{crash}}$ and you **Liquidate ($A_L$)**, you pay a steep fire-sale penalty alongside the crowd for $-40$ utility.

Let us execute the protocol:

**Steps 1–3:** We have $\mathcal{A} = \{A_H, A_L\}$ and $\mathcal{S} = \{S_{\text{stable}}, S_{\text{crash}}\}$. By conditioning on $C$ (our observed latency and portfolio), the confounding rumor about toxic assets is screened off and drops out of the differential analysis. However, the correlation with the $M$ peer algorithms acts on the mapping from $C$ to $\mathcal{A}$ itself and therefore survives conditioning on $C$.

Notice first what **Causal Decision Theory** would do if your single fund is too small to causally trigger the flash crash on its own: CDT uses the unconditional baseline priors $P(S_{\text{stable}} \mid C) = 0.60$ and $P(S_{\text{crash}} \mid C) = 0.40$:

$$U(A_H) = 0.60(100) + 0.40(-200) = 60 - 80 = -20$$

$$U(A_L) = 0.60(-10) + 0.40(-40) = -6 - 16 = -22$$

Because $-20 > -22$, a CDT manager **Holds ($A_H$)**, gambling on the $60\%$ prior probability of stability while ignoring what their own impulse to liquidate or hold implies about the correlated quant cohort.

**Step 4 (Evidential Conditioning via Bayes' Rule):** Let us compute the conditional probabilities for EDT. First, find the marginal probabilities of each action given $C$:

$$P(A_H \mid C) = P(A_H \mid S_{\text{stable}}, C)P(S_{\text{stable}} \mid C) + P(A_H \mid S_{\text{crash}}, C)P(S_{\text{crash}} \mid C) = (0.80)(0.60) + (0.15)(0.40) = 0.48 + 0.06 = 0.54$$

$$P(A_L \mid C) = P(A_L \mid S_{\text{stable}}, C)P(S_{\text{stable}} \mid C) + P(A_L \mid S_{\text{crash}}, C)P(S_{\text{crash}} \mid C) = (0.20)(0.60) + (0.85)(0.40) = 0.12 + 0.34 = 0.46$$

Now invert the probabilities using Bayes' rule:
* Conditional on **Holding ($A_H$)**:
  $$P(S_{\text{stable}} \mid A_H, C) = \frac{0.48}{0.54} = \frac{8}{9} \approx 0.889, \quad P(S_{\text{crash}} \mid A_H, C) = \frac{0.06}{0.54} = \frac{1}{9} \approx 0.111$$
* Conditional on **Liquidating ($A_L$)**:
  $$P(S_{\text{stable}} \mid A_L, C) = \frac{0.12}{0.46} = \frac{6}{23} \approx 0.261, \quad P(S_{\text{crash}} \mid A_L, C) = \frac{0.34}{0.46} = \frac{17}{23} \approx 0.739$$

**Step 5 (Maximize News Value):** Substitute these posteriors into the Gibbard-Harper formula:

$$V(A_H \mid C) = \frac{8}{9}(100) + \frac{1}{9}(-200) = \frac{800 - 200}{9} = \frac{600}{9} \approx +66.67$$

$$V(A_L \mid C) = \frac{6}{23}(-10) + \frac{17}{23}(-40) = \frac{-60 - 680}{23} = -\frac{740}{23} \approx -32.17$$

Here, $V(A_H \mid C) \approx +66.67 \gg -32.17 \approx V(A_L \mid C)$. In fact, whereas CDT saw holding as a grim negative-expectation gamble ($-20$), EDT recognizes that choosing to hold is powerful evidence ($88.9\%$) that the shared quantitative architecture across the market is also holding, stabilizing prices and generating a high positive expected return ($+66.67$). Conversely, if the numbers were shifted so that holding during a crash carried a lesser penalty (say $-50$) while liquidating in a crash gained $+80$ via short rebates, EDT would accurately price the crowd amplification of whichever policy is adopted.

---

## 6. Conclusion

Evidential Decision Theory offers a mathematically austere and philosophically bold vision of agency. Rather than relying on metaphysical counterfactuals ($A \mathrel{\Box\rightarrow} O_j$) that attempt to isolate an agent from the web of cosmic and social correlations surrounding their choices, EDT grounds rational choice entirely in standard Bayesian conditionalization: $V(A) = \sum_j P(O_j \mid A) D(O_j)$. 

As we have seen, when we supplement the foundational Gibbard-Harper equation with rigorous operational rules—conditioning on pre-choice introspective evidence to screen off spurious physical confounders, deriving inverse likelihoods via Bayes' Theorem, and accounting for symmetric peers across time and space—EDT avoids naive "news management" while unlocking cooperative equilibria in the Twin Prisoner's Dilemma, securing millions in Newcomb's Paradox, and dominating meta-theoretical wagers across large populations. In a world increasingly populated by predictive algorithms, shared decision architectures, and correlated strategic actors, asking what your actions *signify* is just as vital as asking what they *cause*.

---

## References

* Ahmed, Arif (2021). *Evidential Decision Theory*. Cambridge University Press. ISBN 9781108607865.
* Conitzer, Vincent (2015). "A Dutch book against sleeping beauties who are evidential decision theorists". *Synthese*, 192 (9): 2887–2899. doi:10.1007/s11229-015-0691-7.
* Gibbard, A.; Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*, pp. 7–8.
* Greene, P.; Levinstein, B. (2020). "Act Consequentialism without Free Rides". *Philosophical Perspectives*, 34 (1): 100–101. doi:10.1111/phpe.12138.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*, p. 146.
* Lewis, D. (1981). "Causal decision theory". *Australasian Journal of Philosophy*, 59 (1): 5–30. doi:10.1080/00048408112340011.
* MacAskill, William; Vallinder, Aron; Österheld, Caspar; Shulman, Carl; Treutlein, Johannes (2021). *The Evidentialist's Wager*.
* Wolpert, D. H.; Benford, G. (2013). "The lesson of Newcomb's paradox". *Synthese*, 190 (9): 1637–1646. doi:10.1007/s11229-011-9899-3.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Project Scope**

I'm now zeroing in on defining the project scope, specifically focusing on how to represent the user's request for an essay on Evidential Decision Theory in the context of a mathematical or technical blog post. I'm considering the desired length and tone for this piece, ensuring I capture the essence of EDT for a knowledgeable audience.


**Clarifying the Core Principles**

I'm now diving into the core principles, analyzing EDT's "news value" concept. It highlights the contrast with Causal Decision Theory, and it's essential to define the formal distinctions between the two. The Gibbard & Harper (1976) framework, and the crucial distinction between types of expected utility maximization will form the crux of the discussion. I'm focusing on clarity of presentation.


**Analyzing Decision Theory Equations**

I'm now deeply engaged with comparing the mathematical formalizations of Evidential Decision Theory (EDT) and Causal Decision Theory (CDT). I'm focusing on the expected utility equations, specifically the conditional probability and the counterfactual probability aspects. I'm exploring the implications of their inequivalence, illustrating these distinctions with Newcomb's paradox.


**Evaluating EDT Advantages and Disadvantages**

I'm now focusing on evaluating the arguments for and against Evidential Decision Theory, specifically its behavior in game-theoretic scenarios. I'm analyzing the Prisoner's Dilemma example where EDT suggests cooperation. I'm contrasting this with critiques, particularly Lewis's and Joyce's arguments, to provide a well-rounded evaluation of EDT. The Sleeping Beauty Problem and the Evidentialist's Wager are also being considered as supporting evidence.


**Defining Target Audience and Scope**

I'm now honing in on defining the target audience: mathematically inclined readers who value both formal precision and philosophical reasoning. I need actionable precision, meaning the essay should be detailed enough for readers to apply EDT in real-world scenarios. I will cover how the theory evaluates actions, deals with dependencies, and handle open questions. The focus will be on distinguishing source claims from my interpretations, aiming for approximately 2,500-2,800 words.


**Structuring the Mathematical Essay**

I'm now building the structure of the mathematical essay, aiming for clarity and practical application. I've chosen a title: *News Value and Rational Choice: The Formal Machinery of Evidential Decision Theory*. The introduction will set the stage, contrasting EDT's news value with CDT's causal efficacy. My focus is on unpacking the formal machinery from Gibbard and Harper's framework to provide a framework for a knowledgeable reader.


**Operationalizing the Framework**

I'm now zeroing in on the operational framework for Gibbard-Harper's expected utility equations. I'm focusing on rigorously defining the formal elements of the propositions and state space to bridge the gap between textbook presentations and real-world applicability. This will involve defining the finite algebra of propositions, state space, probability measure, and desirability function, ensuring a robust and clear mathematical presentation.


**Formalizing the Equations**

I'm now detailing the utility function, $D$. I'm elucidating how outcomes, $O_j$, stem from actions, $A$, and background states, $S_i$. I'm showing how $O_{i,A} = A \cap S_i$ integrates state-based decision matrices, and how $P(O_j \mid A) = \frac{P(O_j \cap A)}{P(A)}$ handles dependencies.


**Illustrating with Game Theory**

I'm now integrating Newcomb's Paradox and the Twin Prisoner's Dilemma to illustrate EDT's application. I'm carefully setting up the state space, action space, and probabilities to show the divergence between conditional and counterfactual probabilities in Newcomb's. I'm also detailing Aomame and her twin in the Prisoner's Dilemma, demonstrating how EDT transforms a non-cooperative game into a coordination mechanism by leveraging logical symmetry.


**Addressing Open Questions**

I'm now zeroing in on three key open questions left unresolved by my references. Specifically, the zero-probability problem, the distinction between objective and subjective probabilities, and the appropriate selection of states. To resolve the zero-probability problem, I'm proposing an epsilon-perturbation model. The operational proposal will introduce $P_\epsilon(A) > 0$ and then take the limit. I'm hoping to show how this clarifies $V(A)$ for all choices.


**Clarifying Confounding Issues**

I'm currently addressing how an EDT agent navigates classic confounding situations. I'm focusing on the "Tickle Defense," building on Eells and Jeffrey's work. My goal is to outline an operational extension to manage cases where a common cause influences both action and outcome via the agent's internal state. It should allow them to distinguish between genuine correlations and spurious confounding factors. I'm exploring how to condition on full introspective states to assess the situation.


**Analyzing Screening-Off Conditions**

I'm now focusing on rigorously formalizing screening-off conditions within EDT, expanding on Eells and Jeffrey's work to handle common-cause scenarios. I'm aiming to capture the exact mathematical conditions under which $P(S \mid A, T) = P(S \mid T)$ holds. I'm clarifying when screening-off occurs due to introspectable states versus when it fails due to exact predictors, providing readers with a robust test for unfamiliar cases.


**Formalizing EDT Advantages**

I'm now building up to a detailed discussion of the Evidentialist's Wager, analyzing the expected value equation when an agent has credences in both Evidential Decision Theory (EDT) and Causal Decision Theory (CDT). I'm showing how the EDT term scales with the number of correlated peers, while the CDT term remains constant, demonstrating the meta-decision advantage of acting like an evidentialist in large, correlated scenarios. I'm focusing on why "halfers" can be Dutch-booked. I intend to provide a step-by-step algorithm.


**Defining the Algorithm**

I'm now detailing an explicit protocol to illustrate EDT. I will use example problems like **The Distributed Consensus / Correlated Bot Dilemma** to compute conditional probabilities and check the screening-off conditions. I'm working to derive the optimal policy and will conclude by summarizing the philosophical and mathematical core of EDT. I plan to clarify how conditioning baselines and correlated agent classes are essential for cleanly applying EDT. I'm also ensuring the target word count of 2,400–3,000 words.


**Calibrating Essay Word Count**

I'm now recalibrating the essay structure with estimated word counts for each section to stay within the 2,400–3,000 word range. I'm aiming for about 300 words in the introduction, 550 for the formal architecture, another 550 for the canonical thought experiments, 950 for open questions, 400 for the algorithmic protocol, and 200 for the conclusion, totaling roughly 2,900 words. I am carefully watching the total count. I am also detailing the utility function with the Gibbard-Harper equations.


**Refining State-Act Formulations**

I'm now detailing how outcomes, $O_j$, can be refined into state-act pairs ($S_i, A_k$). The derivation of a news-value formula for a reader to build decision tables is key. I've re-derived Gibbard-Harper's formula in terms of background states, $S_i$, and actions, $A_k$. This allows for the state-act formulation which makes unfamiliar decision problems dramatically easier. I'm aiming for clarity in applying this framework. I'm verifying the specific numbers for Newcomb's Paradox.


**Refining Application Examples**

I'm now zeroing in on a detailed numerical example based on Newcomb's Paradox and the Twin Prisoner's Dilemma to clarify EDT's practical application. My goal is a concrete presentation of how to build utility matrices for both scenarios. I am working through the equations and verifying the expected values for each action. The key is in clearly laying out the state spaces. I am trying to emphasize the crucial differences in how EDT makes its decisions.



**Operationalizing Tickle Defense**

I'm now zeroing in on an operational extension for the "Tickle Defense", incorporating an introspective information state, *I*. I'm showing that if a background factor *C* causes both an action inclination and a bad outcome *S*, then conditioning on *I* yields *P(S|A,I) = P(S|I)*, allowing the bad news to be dropped from the action comparison in *V(A|I)*. I'm contrasting this with cases where predictors or twin models directly map *I* to *A*.


```
