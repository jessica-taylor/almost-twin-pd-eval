# 013_edt_wikipedia_google_gemini-4-argon_rhigh_phigh / 00013

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/1a87e3f4-64e6-46e1-8ff5-86c8f4982579/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/1a87e3f4-64e6-46e1-8ff5-86c8f4982579/call_0/response.raw) · finish: `stop`

### Visible response

```text
# News Value and Rational Choice: The Mathematics and Philosophy of Evidential Decision Theory

When a rational agent deliberates between competing courses of action, what question is she trying to answer? According to one natural picture, deliberation is an exercise in forward-looking causal engineering: the agent asks which action will *bring about* the best state of affairs in the future. According to a rival picture, deliberation is an exercise in Bayesian self-observation: the agent treats her own impending choice as a piece of information about the world and asks which action she would *most welcome learning* that she is about to perform.

This second approach is **Evidential Decision Theory (EDT)**. As summarized in the reference literature, EDT instructs a rational agent confronting a set of possible actions to select the option with the highest *news value*—the action that is indicative of the best outcome in expectation if one received the "news" that it had been taken. In Arif Ahmed's memorable phrase, EDT recommends that you "do what you most want to learn that you will do" (Ahmed, 2021, p. 7).

While EDT and its principal rival, **Causal Decision Theory (CDT)**, prescribe identical behavior in routine decision environments, they diverge sharply in problems involving predictors, correlated rational agents, or common causes. This essay provides a self-contained mathematical account of EDT, contrasts its formal machinery with CDT, examines the classic thought experiments that separate them, and develops explicit operational procedures to resolve the theoretical ambiguities that arise when applying EDT to unfamiliar decision problems. Throughout, we will carefully distinguish the core claims established in the reference text from the additional mathematical structures and operational assumptions we introduce to make the theory fully applicable.

---

## 1. The Formal Architecture of EDT

### 1.1 The Gibbard–Harper Formulation

The modern mathematical contrast between evidential and causal expected utility traces back to Allan Gibbard and William Harper's foundational 1976 paper, *Counterfactuals and Two Kinds of Expected Utility*. Following the reference article's presentation of Gibbard and Harper (1976), suppose an agent faces a finite set of mutually exclusive and exhaustive outcomes $\{O_1, O_2, \dots, O_m\}$ and must choose an action $A$ from a set of available alternatives $\mathcal{A}$. Each outcome $O_j$ is assigned a numerical desirability (or utility) $D(O_j) \in \mathbb{R}$.

Evidential Decision Theory evaluates each candidate action $A \in \mathcal{A}$ by computing its conditional expected utility—often called its *news value* and denoted $V(A)$:

$$V(A) = \sum_{j} P(O_j \mid A) D(O_j)$$

Here, $P(O_j \mid A)$ is the standard conditional probability of outcome $O_j$ given that action $A$ occurs:

$$P(O_j \mid A) = \frac{P(O_j \cap A)}{P(A)}, \quad \text{assuming } P(A) > 0.$$

By contrast, Causal Decision Theory evaluates an action $A$ by replacing the conditional probability $P(O_j \mid A)$ with the probability of a counterfactual conditional, yielding the causal expected utility $U(A)$:

$$U(A) = \sum_{j} P(A \mathrel{\Box{\rightarrow}} O_j) D(O_j)$$

where $P(A \mathrel{\Box{\rightarrow}} O_j)$ denotes the probability that outcome $O_j$ would occur in the counterfactual situation in which action $A$ were performed. Because standard conditional probability $P(O_j \mid A)$ and counterfactual probability $P(A \mathrel{\Box{\rightarrow}} O_j)$ do not always coincide, $V(A)$ and $U(A)$ represent genuinely distinct maximization criteria.

### 1.2 Operationalizing the State-Action Space

The reference article defines $V(A)$ directly over outcomes $O_j$. However, to apply EDT systematically to novel problems—and to diagnose precisely where and why $P(O_j \mid A)$ diverges from $P(A \mathrel{\Box{\rightarrow}} O_j)$—it is helpful to introduce an explicit state-space decomposition. *(Note: This decomposition and the resulting coincidence criterion are our own mathematical elaboration of the Gibbard–Harper framework presented in the source.)*

Let $(\Omega, \mathcal{F}, P)$ be a probability space representing the agent's epistemic state prior to completing deliberation. We partition the relevant features of the world outside the agent's immediate motor control into a finite set of mutually exclusive and exhaustive **states of nature** $\mathcal{S} = \{S_1, S_2, \dots, S_n\} \subset \mathcal{F}$. The agent's candidate **actions** $\mathcal{A} = \{A_1, A_2, \dots, A_k\} \subset \mathcal{F}$ are likewise treated as measurable events in the same sigma-algebra $\mathcal{F}$.

In any concrete decision problem, the combination of an action $A \in \mathcal{A}$ and a state of nature $S_i \in \mathcal{S}$ uniquely determines a fine-grained outcome $O_{A, i} = A \cap S_i$ with desirability $D(A, S_i)$. Because the states $S_i$ partition the sample space $\Omega$, the conditional probability of any outcome given action $A$ reduces to the conditional probability of the corresponding state $S_i$ given $A$. We can therefore rewrite the EDT valuation functional as:

$$V(A) = \sum_{i=1}^{n} P(S_i \mid A) D(A, S_i)$$

Under this state-action representation, Bayes' theorem reveals how EDT treats dependencies between an agent's choice and the external world:

$$P(S_i \mid A) = \frac{P(A \mid S_i) P(S_i)}{\sum_{m=1}^{n} P(A \mid S_m) P(S_m)}$$

Notice what this equation does. Even if state $S_i$ was settled in the distant past or in a causally isolated room, so long as the likelihood $P(A \mid S_i)$ varies across states $S_i$, observing one's own action $A$ forces a Bayesian update on the probability of $S_i$. EDT incorporates this *diagnostic* or *evidential* shift directly into the valuation of $A$.

In contrast, if the states $S_i$ are chosen so that the agent's action has no causal influence over which state obtains, CDT evaluates action $A$ by holding the prior state probabilities fixed across all counterfactual interventions:

$$U(A) = \sum_{i=1}^{n} P(A \mathrel{\Box{\rightarrow}} S_i) D(A, S_i) = \sum_{i=1}^{n} P(S_i) D(A, S_i)$$

From these two equations, we obtain an immediate necessary and sufficient condition for the equivalence of the two theories:

> **The Act–State Independence Criterion.** If every relevant state of nature $S_i \in \mathcal{S}$ is both causally independent of the available actions (so $P(A \mathrel{\Box{\rightarrow}} S_i) = P(S_i)$) and statistically independent of the available actions under the agent's credence function (so $P(S_i \mid A) = P(S_i)$ for all $A \in \mathcal{A}$), then $V(A) = U(A)$ for all $A \in \mathcal{A}$.

Whenever you bet on a fair roulette wheel or decide whether to carry an umbrella based on a meteorologist's forecast, your decision is statistically independent of the physical state of the wheel or the weather: $P(\text{Rain} \mid \text{Take Umbrella}) = P(\text{Rain})$. In all such ordinary problems, EDT and CDT speak with one voice. Divergence requires a mechanism that makes $P(S_i \mid A) \neq P(S_i)$ without $A$ causally bringing about $S_i$.

---

## 2. Dependencies, Counterfactuals, and Classic Thought Experiments

The reference text highlights two canonical environments in which actions provide strong evidence about states of the world that the agent cannot causally alter: **predictive asymmetry** (Newcomb's paradox) and **agential symmetry** (the Twin Prisoner's Dilemma). Let us analyze the formal mechanics of both.

### 2.1 Predictive Asymmetry: Newcomb's Paradox

In Newcomb's paradox (Wolpert & Benford, 2013; Ahmed, 2021), an agent confronts two boxes:
* **Box A** is transparent and contains a visible $\$1,000$.
* **Box B** is opaque and contains either $\$1,000,000$ or $\$0$.

The agent has two available actions:
* $A_1$: Take only Box B ("one-boxing").
* $A_2$: Take both Box A and Box B ("two-boxing").

Prior to the decision, a predictor with $99\%$ accuracy predicted the agent's choice. If the predictor predicted $A_1$, she placed $\$1,000,000$ in Box B (state $S_1$). If the predictor predicted $A_2$, she placed $\$0$ in Box B (state $S_2$). The decision matrix of payoffs $D(A, S)$ is:

| Action \ State | $S_1$ ($\$1\text{M}$ in Box B) | $S_2$ ($\$0$ in Box B) |
| :--- | :---: | :---: |
| **$A_1$ (Take only Box B)** | $\$1,000,000$ | $\$0$ |
| **$A_2$ (Take both boxes)** | $\$1,001,000$ | $\$1,000$ |

Following the calculation in the reference article (assuming desirability scales linearly with dollar payoffs), the conditional probabilities reflect the predictor's $99\%$ reliability given the agent's action:

$$P(S_1 \mid A_1) = 0.99, \qquad P(S_2 \mid A_1) = 0.01$$

$$P(S_1 \mid A_2) = 0.01, \qquad P(S_2 \mid A_2) = 0.99$$

Substituting these into the EDT formula yields:

$$\begin{aligned}
V(A_1) &= P(S_1 \mid A_1) \times \$1,000,000 + P(S_2 \mid A_1) \times \$0 \\
&= 0.99 \times \$1,000,000 + 0.01 \times \$0 = \$990,000
\end{aligned}$$

$$\begin{aligned}
V(A_2) &= P(S_1 \mid A_2) \times \$1,001,000 + P(S_2 \mid A_2) \times \$1,000 \\
&= 0.01 \times \$1,001,000 + 0.99 \times \$1,000 = \$11,000
\end{aligned}$$

Since $V(A_1) = \$990,000 > V(A_2) = \$11,000$, EDT decisively recommends one-boxing ($A_1$).

To see how differently EDT and CDT treat counterfactuals here, let us write out the corresponding CDT calculation *(expanding on the reference text's qualitative statement that CDT recommends taking both boxes)*. Because the predictor has already placed the money and walked away before the agent chooses, the contents of Box B are causally independent of the agent's present action. Let $p = P(S_1) \in [0, 1]$ be the agent's unconditional prior probability that Box B contains $\$1,000,000$. Under CDT, the counterfactual probabilities are invariant across actions:

$$P(A_1 \mathrel{\Box{\rightarrow}} S_1) = P(A_2 \mathrel{\Box{\rightarrow}} S_1) = p, \qquad P(A_1 \mathrel{\Box{\rightarrow}} S_2) = P(A_2 \mathrel{\Box{\rightarrow}} S_2) = 1 - p.$$

Thus, the causal expected utilities are:

$$U(A_1) = p(\$1,000,000) + (1 - p)(\$0) = \$1,000,000p$$

$$U(A_2) = p(\$1,001,000) + (1 - p)(\$1,000) = \$1,000,000p + \$1,000$$

For *every* prior $p \in [0,1]$, $U(A_2) - U(A_1) = \$1,000 > 0$. CDT reasons by dominance: "Whatever is inside Box B is already fixed; taking both boxes guaranteed me an extra $\$1,000$ in either state." EDT rejects dominance reasoning whenever the states are evidentially dependent on the actions, reasoning instead: "One-boxing is overwhelming evidence that I am in state $S_1$, whereas two-boxing is overwhelming evidence that I am in state $S_2$."

### 2.2 Agential Symmetry: The Twin Prisoner's Dilemma

A second major class of divergence does not require a godlike predictor; it requires only that two or more agents share similar decision-making algorithms. As described in the reference article (drawing on Greene & Levinstein, 2020), consider Aomame and her psychological twin, placed in causally isolated rooms with no communication. Each must choose simultaneously whether to **Cooperate ($C$)** or **Defect ($D$)**, caring solely about her own individual payout:

| Aomame \ Twin | Twin Cooperates ($S_C$) | Twin Defects ($S_D$) |
| :--- | :---: | :---: |
| **Aomame Cooperates ($C$)** | $\$5$ | $\$0$ |
| **Aomame Defects ($D$)** | $\$10$ | $\$1$ |

In the reference article's baseline case, the twin's reasoning process is an exact mirror of Aomame's: $P(S_C \mid C) = 1$ and $P(S_D \mid D) = 1$. The news values are therefore:

$$V(C) = 1 \times \$5 + 0 \times \$0 = \$5$$

$$V(D) = 0 \times \$10 + 1 \times \$1 = \$1$$

Because $V(C) > V(D)$, EDT prescribes cooperation, whereas CDT prescribes defection (since $D$ strictly dominates $C$ by $\$5$ if the twin cooperates and by $\$1$ if the twin defects).

#### Generalizing to Imperfect Correlation (An Operational Extension)

In real-world applications, an agent rarely faces a literal psychological clone. Rather, she interacts with peers whose cognitive architecture, training, or normative commitments are *partially* correlated with her own. *(To make the source's Twin Prisoner's Dilemma applicable to unfamiliar strategic environments, we now generalize the deterministic $0/1$ conditional probabilities to arbitrary symmetricgames.)*

Suppose an agent plays a generalized Prisoner's Dilemma with payoffs $T > R > P > S$ (where $T$ is Temptation to defect, $R$ is Reward for mutual cooperation, $P$ is Punishment for mutual defection, and $S$ is Sucker's payoff; in Aomame's case, $T=10, R=5, P=1, S=0$). Let the diagnostic correlation between the agent and her counterpart be parameterized by the conditional probabilities:

$$\alpha = P(S_C \mid C), \qquad \beta = P(S_D \mid D)$$

Then the EDT valuations are:

$$V(C) = \alpha R + (1 - \alpha) S$$

$$V(D) = (1 - \beta) T + \beta P$$

An EDT agent will cooperate if and only if $V(C) > V(D)$, which simplifies to:

$$\alpha R + (1 - \alpha) S > (1 - \beta) T + \beta P \iff \alpha (R - S) + \beta (T - P) > T - S$$

In the symmetric diagnostic case where $\alpha = \beta = r \in [0, 1]$ (meaning the agent's action predicts the counterpart's matching action with accuracy $r$), cooperation is rational under EDT whenever:

$$r > r^* = \frac{T - S}{(R - S) + (T - P)}$$

Plugging in Aomame's payoffs ($T=10, R=5, P=1, S=0$), we find:

$$r^* = \frac{10 - 0}{(5 - 0) + (10 - 1)} = \frac{10}{14} = \frac{5}{7} \approx 0.714.$$

Thus, Aomame does not need a perfect psychological twin to cooperate under EDT; she only needs her decision process to be at least $71.4\%$ diagnostically predictive of her counterpart's choice. Notice also how this relates to Douglas Hofstadter's concept of *superrationality* (mentioned in the reference's cross-references): EDT achieves the cooperative equilibrium not by postulating a separate axiom of collective rationality, but directly through standard conditional probability over correlated agents.

---

## 3. Open Questions and Operational Proposals for Unfamiliar Cases

While the reference article establishes the core equation $V(A) = \sum_j P(O_j \mid A) D(O_j)$ and its behavior in Newcomb's paradox and the Twin Prisoner's Dilemma, it leaves several critical theoretical and operational questions only briefly sketched or open. If a practitioner wishes to use EDT to decide unfamiliar cases, three major questions must be resolved:

1. **Common-Cause Confounding:** How does EDT respond to the criticism (voiced by David Lewis and James Joyce in the reference text) that maximizing conditional probability leads to irrational "news management" in medical or observational confounding scenarios?
2. **The Measure-Zero Problem:** How is $P(O_j \mid A)$ defined when an agent's deliberation makes the probability of suboptimal actions approach zero, or how are prior credences over one's own actions assigned?
3. **Sequential Policies and Normative Stakes:** How does EDT evaluate multi-stage policies under indexical uncertainty (such as the Sleeping Beauty problem), and how do we formalize the "Evidentialist's Wager" when an agent is uncertain whether EDT itself is the right decision theory?

In this section, we explain what the reference text says on each point and develop concrete operational interpretations to resolve the remaining uncertainties.

### 3.1 Common-Cause Confounding and the "Managing the News" Critique

In the reference article's *Criticism* section, two foundational objections to EDT are quoted:
* **David Lewis (1981)** characterizes EDT as promoting "an irrational policy of managing the news."
* **James M. Joyce (1999, p. 146)** argues: "Rational agents choose acts on the basis of their *causal efficacy*, not their auspiciousness; they act to *bring about* good results even when doing so might betoken bad news."

The reference text does not spell out the formal structure of the examples that motivate Lewis and Joyce's objection. *(To understand why this poses an acute problem for naive applications of EDT—and how modern evidentialists operationalize a defense—we construct a mathematical model of a classic common-cause confounding problem.)*

Suppose an agent is deciding whether to take a mild palliative supplement ($A_1$) or abstain ($A_2$). Unknown to the agent, there is a latent genetic condition $G \in \{S_1, S_2\}$, where $S_1$ means the gene is present and $S_2$ means it is absent. The gene $S_1$ has two independent effects:
1. It causes a severe illness later in life, imposing a utility loss of $-100$.
2. It causes a mild biochemical craving for the supplement, so that $80\%$ of people with $S_1$ take $A_1$, whereas only $10\%$ of people without the gene ($S_2$) take $A_1$.

Crucially, the supplement itself has **zero causal effect** on the illness, and provides a direct hedonic/palliative benefit of $+1$ regardless of genetic state:

| Action \ State | $S_1$ (Gene Present / Illness) | $S_2$ (Gene Absent / Healthy) |
| :--- | :---: | :---: |
| **$A_1$ (Take supplement)** | $-99$ | $+1$ |
| **$A_2$ (Abstain)** | $-100$ | $0$ |

Suppose the prior prevalence of the gene is $P(S_1) = 0.20$ and $P(S_2) = 0.80$, with behavioral likelihoods $P(A_1 \mid S_1) = 0.80$ and $P(A_1 \mid S_2) = 0.10$. By Bayes' theorem:

$$P(S_1 \mid A_1) = \frac{0.80 \times 0.20}{0.80 \times 0.20 + 0.10 \times 0.80} = \frac{0.16}{0.24} = \frac{2}{3} \approx 0.667$$

$$P(S_1 \mid A_2) = \frac{0.20 \times 0.20}{0.20 \times 0.20 + 0.90 \times 0.80} = \frac{0.04}{0.76} = \frac{1}{19} \approx 0.053$$

If we apply the naive EDT formula directly to these numbers, we obtain:

$$V_{\text{naive}}(A_1) = \frac{2}{3}(-99) + \frac{1}{3}(+1) = -66 + 0.33 = -65.67$$

$$V_{\text{naive}}(A_2) = \frac{1}{19}(-100) + \frac{18}{19}(0) = -5.26$$

Naive EDT recommends abstaining ($A_2$)—forgoing the beneficial $+1$ supplement solely because taking it is "bad news" about one's genome! This is precisely what Lewis calls "managing the news" and what Joyce means by choosing on *auspiciousness* rather than *causal efficacy*.

#### Operational Resolution: Deliberation Conditioning vs. Hard Evidentialism

How should a practitioner applying EDT handle such cases? In the philosophical literature, two distinct operational responses exist *(both of which go beyond the brief summary in the source article)*:

1. **The Evidential Screening ("Tickle Defense") Approach:** In most natural confounding problems, the latent state $S_1$ does not bypass the agent's conscious mind to move her limbs directly; rather, $S_1$ causes a conscious *craving* or *inclination* $I$ (the "tickle"), which the agent can introspecively observe *before* choosing. If the agent conditions on her full pre-action introspective evidence $I$ prior to evaluating $V(A)$, the inclination $I$ d-separates (screens off) the action $A$ from the genetic state $S_1$:
   
   $$P(S_1 \mid A, I) = P(S_1 \mid I)$$
   
   Once $P(S_1 \mid A, I)$ becomes invariant across $A_1$ and $A_2$, the Act–State Independence Criterion holds conditional on $I$, and EDT agrees with CDT that taking the supplement ($A_1$) is optimal ($V(A_1 \mid I) - V(A_2 \mid I) = +1$).

2. **The Hard-Line Evidentialist Approach (Ahmed, 2021):** What if the genetic state $S_1$ influences the agent's final choice directly without any introspectively accessible intermediate inclination (or what if the predictor in Newcomb's problem is structurally isomorphic to a common cause)? Hard-line proponents of EDT argue that if $P(S_1 \mid A_1, E) > P(S_1 \mid A_2, E)$ persists even after conditioning on **all available pre-choice evidence $E$**, then Newcomb's paradox and the common-cause problem have the exact same conditional probability structure. On this view, a consistent evidentialist must either screen off the correlation via introspective evidence $E$ or accept the recommendation to abstain.

For practical applications, our operational rule is straightforward: **Always condition $P(S_i \mid A, E)$ on the maximal body of pre-action evidence $E$ available to the deliberating agent (including introspective desires and inclinations).** Only correlations that survive conditioning on $E$—such as algorithmic correlations with a predictor or a twin—should enter the calculation of $V(A)$.

### 3.2 The Measure-Zero Problem and Deliberation Credences

A second mathematical subtlety left unaddressed by the reference text concerns the denominator of $P(O_j \mid A) = P(O_j \cap A) / P(A)$. For $V(A)$ to be well-defined across all candidate actions $A \in \mathcal{A}$, the agent must assign strictly positive prior probability $P(A) > 0$ to every option under consideration.

Yet suppose a rational agent knows the payoff matrix of Newcomb's paradox and knows that she is an EDT maximizer. Before she even finishes calculating, she might be $100\%$ certain that she will one-box ($P(A_1) = 1$), which implies that two-boxing has probability zero ($P(A_2) = 0$). If $P(A_2) = 0$, the standard Kolmogorov ratio $P(O_j \cap A_2) / P(A_2) = 0/0$ is undefined, and the agent cannot compute $V(A_2)$ to verify that $A_1$ is indeed better than $A_2$!

*(To make EDT mathematically rigorous in such cases, we introduce the following operational regularization.)*

> **Operational Assumption: The $\varepsilon$-Trembling Hand Regularization.** When evaluating a finite action set $\mathcal{A}$, model the implementation of the agent's decision as subject to an arbitrarily small "tremble" or execution noise $\varepsilon \in (0, 1)$, such that every action $A \in \mathcal{A}$ has positive probability $P_\varepsilon(A) \ge \varepsilon / |\mathcal{A}| > 0$. Define the news value of action $A$ as the limit:
> 
> $$V(A) = \lim_{\varepsilon \to 0^+} \sum_{i=1}^{n} P_\varepsilon(S_i \mid A) D(A, S_i)$$

Equivalently, one may treat $P(S_i \mid A)$ not as a derived ratio from an unconditional prior $P(A)$, but as a primitive conditional probability measure (a Popper–Rényi function) representing the diagnostic likelihood of state $S_i$ given the supposition that action $A$ is selected. In practice, this means that to apply EDT, **you never need to guess your own unconditional prior probability $P(A)$ of acting**; you only need to specify the conditional distribution $P(S_i \mid A)$ for each candidate action $A$.

### 3.3 Sequential Policies, Sleeping Beauty, and the Evidentialist's Wager

The reference article briefly introduces two fascinating extensions of EDT without providing their mathematical details: the **Sleeping Beauty Problem** (Conitzer, 2015) and **The Evidentialist's Wager** (MacAskill et al., 2021). Let us examine why both matter for policy evaluation and formalize their mechanics.

#### Indexical Uncertainty and Sequential Dutch Books (Sleeping Beauty)

In the Sleeping Beauty problem, Beauty is put to sleep on Sunday. A fair coin is tossed:
* If **Heads ($H$)**, she is awakened only on **Monday**.
* If **Tails ($T$)**, she is awakened on **Monday**, given an amnesia-inducing drug that erases her memory of Monday's awakening, and awakened again on **Tuesday**.

Upon any awakening, Beauty cannot tell whether it is Monday or Tuesday. "Thirders" argue her credence in Heads upon waking should be $P(H) = 1/3$, whereas "Halfers" argue it should remain $P(H) = 1/2$. As the reference text notes, a well-known problem for Halfers is that they Appear vulnerable to **diachronic Dutch books** (sequences of bets offered across awakenings that guarantee a net monetary loss across both states $H$ and $T$).

Why does EDT enter this debate? *(Here we unpack the formal mechanism behind the reference article's citation of Conitzer, 2015.)* Because on Tails, Beauty wakes up *twice* in identical epistemic states! If Beauty is a Halfer who uses **Causal Decision Theory**, she treats her decision to accept a bet on Monday as causally independent of what she does on Tuesday. A clever bookie can exploit this by offering her a bet against Heads on every awakening: under CDT, she evaluates the single awakening in isolation, overlooking the fact that on Tails she will accept the bet *twice*, doubling her Tails losses.

If Beauty instead adopts **Evidential Decision Theory**, she recognizes an agential correlation across time: because her Tuesday self has the exact same memories and reasoning process as her Monday self, her decision to accept a bet right now is perfect evidence ($P = 1$) that on Tails she accepts the bet *on both Monday and Tuesday*. Thus, conditioning on her action automatically weights the Tails outcome by the multiplicity of awakenings, shielding her from standard diachronic Dutch books!

However, as the reference text notes, **Vincent Conitzer (2015)** proves that even an EDT-Halfer can be Dutch-booked if the environment breaks the symmetry between the awakenings—for example, by offering different betting menus or randomization devices that decouple the evidential link between Monday's choice and Tuesday's choice without revealing the day. The operational lesson for sequential decision-making is critical: **When evaluating multi-stage problems under EDT, evaluating isolated stage-actions $A_t$ can conflict with evaluating global pre-committed policies $\pi = (A_1, A_2, \dots, A_T)$.** Whenever binding pre-commitment is feasible, an agent should apply the EDT functional $V(\pi)$ to complete policies $\pi \in \Pi$ at the ex-ante stage.

#### Normative Uncertainty: The Evidentialist's Wager

The reference article also cites *The Evidentialist's Wager* (MacAskill et al., 2021), noting that "even if one puts less credence on evidential decision theory, it may be reasonable to act as if EDT were true. Namely, because EDT can involve the actions of many correlated decision-makers, its stakes may be higher than causal decision theory and thus take priority."

*(To show how a reader can apply this meta-decision rule quantitatively, let us construct a formal model of the Wager.)*

Suppose an agent faces a symmetric decision problem (such as contributing to a public good or cooperating in a large-scale prisoner's dilemma) alongside $N - 1$ other decision-makers whose choices are diagnostically correlated with hers with probability $r \in (0, 1]$. Suppose the agent cares about total welfare across all $N$ agents: each cooperative act costs the actor $c > 0$ and generates a benefit $b > c$ for the group.
* Under **CDT**, the agent's action causally affects only her own decision (1 agent). Choosing to cooperate ($C$) over defecting ($D$) yields a net causal gain of:
  $$\Delta U = U(C) - U(D) = b - c$$
  Or, if the personal cost $c$ exceeds the marginal return to oneself and one only counts personal payoff plus a small altruism weight $\gamma$ where $\gamma b < c$, CDT may even favor defection ($\Delta U < 0$) while cooperation remains collectively optimal.
* Under **EDT**, the agent's choice to cooperate is evidence that $1 + (N - 1)r$ agents in total cooperate rather than defect. Thus, the difference in news value between $C$ and $D$ scales with the population size $N$:
  $$\Delta V = V(C) - V(D) = \big(1 + (N - 1)r\big) \Delta u_{\text{individual}}$$

Now suppose the agent is uncertain which decision theory is normatively correct: she assigns credence $q \in (0, 1)$ to EDT and $1 - q$ to CDT. If she maximizes expected normative value across the two theories, the effective weight of EDT's recommendation relative to CDT's scales as:

$$\frac{\text{Expected Stakes under EDT}}{\text{Expected Stakes under CDT}} \propto \frac{q \big(1 + (N - 1)r\big)}{1 - q}$$

Whenever the number of correlated peers $N$ is large—so that $(N - 1)r \gg \frac{1 - q}{q}$—the EDT expectation dominates the meta-decision calculation, even if the agent's philosophical credence $q$ in EDT is very small!

---

## 4. A Step-by-Step Procedure for Deciding Unfamiliar Cases

Synthesizing the Gibbard–Harper formalism from the reference text with our operational clarifications, we can formulate a general five-step algorithm for deciding any unfamiliar decision problem using Evidential Decision Theory:

1. **Specify the Action Set $\mathcal{A}$:** Enumerate the mutually exclusive actions (or, if binding pre-commitment is available in a sequential game, complete policies) $\mathcal{A} = \{A_1, \dots, A_k\}$ open to the agent.
2. **Identify the Maximal Pre-Action Evidence $E$:** Record all information available to the agent *prior* to the choice, including introspective awareness of desires, symptoms, or inclinations. (This step screens off spurious common-cause confounders wherever introspective intermediates exist.)
3. **Partition the Relevant States of Nature $\mathcal{S}$:** Define a mutually exclusive and exhaustive set of states $\mathcal{S} = \{S_1, \dots, S_n\}$ that specify all external factors—including past predictions and the concurrent choices of other agents—needed to determine the outcome of each action.
4. **Assign Payoffs and Diagnostic Probabilities:** For each pair $(A_m, S_i)$, specify the desirability $D(A_m, S_i) \in \mathbb{R}$ and the conditional probability $P(S_i \mid A_m, E)$ representing how likely state $S_i$ would be if you learned that you chose $A_m$ given background evidence $E$ (using an $\varepsilon$-tremble limit if any $P(A_m \mid E) = 0$).
5. **Maximize News Value $V(A)$:** For each $A_m \in \mathcal{A}$, compute:
   $$V(A_m) = \sum_{i=1}^{n} P(S_i \mid A_m, E) D(A_m, S_i)$$
   Select any action $A^* \in \arg\max_{A_m \in \mathcal{A}} V(A_m)$.

### Worked Example: An Unfamiliar Algorithmic Market Game

To see this five-step procedure in action on an unfamiliar case, consider an automated trading researcher deploying a pricing bot $B_1$ into an electronic market populated by two other competing bots, $B_2$ and $B_3$, trained by rival firms on overlapping open-source codebases.

* **Step 1 (Actions):** Each bot must simultaneously select either a **Low-Fee ($L$)** or **High-Fee ($H$)** liquidity schedule for the day: $\mathcal{A} = \{L, H\}$.
* **Step 2 (Pre-Action Evidence $E$):** Market volatility and public order-book data are observed and conditioned upon; no further private signals exist.
* **Step 3 (States $\mathcal{S}$):** The relevant external state is the number of rival bots ($B_2, B_3$) that choose the cooperative High-Fee schedule $H$:
  * $S_2$: Both rivals choose $H$.
  * $S_1$: Exactly one rival chooses $H$.
  * $S_0$: Neither rival chooses $H$ (both undercut with $L$).
* **Step 4 (Payoffs and Diagnostic Probabilities):** Suppose the market revenue (in thousands of dollars) to our bot $B_1$ depends on whether it undercuts the rivals ($L$) or maintains margins ($H$):
  * If $B_1$ plays $H$: it earns $\$12\text{k}$ in $S_2$ (all three keep high fees), $\$4\text{k}$ in $S_1$, and $\$0\text{k}$ in $S_0$.
  * If $B_1$ plays $L$ (undercutting): it captures volume and earns $\$15\text{k}$ in $S_2$, $\$7\text{k}$ in $S_1$, and $\$3\text{k}$ in $S_0$.
  
  Notice that $L$ strictly dominates $H$ by $\$3\text{k}$ in every state $S_i$ (so CDT immediately prescribes $L$). However, because the bots share training data and architectural biases, $B_1$'s choice is diagnostically correlated with each rival's choice independently with matching probability $r = 0.70$:
  * Conditional on $B_1$ choosing $H$, each rival chooses $H$ with probability $0.70$:
    $$P(S_2 \mid H) = (0.7)^2 = 0.49, \quad P(S_1 \mid H) = 2(0.7)(0.3) = 0.42, \quad P(S_0 \mid H) = (0.3)^2 = 0.09.$$
  * Conditional on $B_1$ choosing $L$, each rival chooses $L$ with probability $0.70$ (so chooses $H$ with probability $0.30$):
    $$P(S_2 \mid L) = (0.3)^2 = 0.09, \quad P(S_1 \mid L) = 2(0.3)(0.7) = 0.42, \quad P(S_0 \mid L) = (0.7)^2 = 0.49.$$
* **Step 5 (Maximize $V(A)$):** We compute the news value of each policy:
  $$V(H) = 0.49(12) + 0.42(4) + 0.09(0) = 5.88 + 1.68 + 0 = \$7.56\text{k}$$
  $$V(L) = 0.09(15) + 0.42(7) + 0.49(3) = 1.35 + 2.94 + 1.47 = \$5.76\text{k}$$
  Since $V(H) = \$7.56\text{k} > V(L) = \$5.76\text{k}$, EDT recommends deploying the High-Fee schedule $H$, earning an expected $\$1,800$ more than the dominance-driven CDT choice $L$.

---

## 5. Conclusion

Evidential Decision Theory offers a remarkably austere and unified vision of practical rationality. By defining the value of an action purely through standard Bayesian conditioning—$V(A) = \sum_j P(O_j \mid A) D(O_j)$—it dispenses with primitive counterfactual primitives ($\mathrel{\Box{\rightarrow}}$) and evaluates every choice by the expected desirability of the world in which that choice occurs.

As we have seen, this austerity comes with profound philosophical commitments. When an agent's deliberation is correlated with external predictors or symmetric peers—as in Newcomb's paradox, the Twin Prisoner's Dilemma, or algorithmic multi-agent environments—EDT enables agents to secure higher payoffs than causal maximizers by leveraging diagnostic correlations. Conversely, when facing unobserved common causes or indexical uncertainties, applying EDT safely requires careful attention to pre-action introspective conditioning and policy-level evaluation. Whether one ultimately embraces EDT as a foundational theory of rationality or deploys it pragmatically via the Evidentialist's Wager, mastering its formal mechanics is indispensable for modern decision analysis.

---

## References

* Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
* Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese*, 192(9), 2887–2899.
* Gibbard, A., & Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*, pp. 7–8.
* Greene, P., & Levinstein, B. (2020). Act Consequentialism without Free Rides. *Philosophical Perspectives*, 34(1), 100–101.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*, p. 146. Cambridge University Press.
* Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
* MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). *The Evidentialist's Wager*. Global Priorities Institute.
* Wolpert, D. H., & Benford, G. (2013). The lesson of Newcomb's paradox. *Synthese*, 190(9), 1637–1646.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Task**

I'm currently focused on defining the precise parameters of this project. The primary goal is to produce either a mathematical essay or a technical blog post. The target audience is mathematically literate individuals, and the core subject is Evidential Decision Theory (EDT) and its application to decision problems. I am thinking about how to frame this to make it useful.


**Refining the Scope**

I've been drilling down on the scope, now targeting a mathematical essay/technical blog post for mathematically literate readers, and those interested in philosophy. I'm focusing on providing formal definitions, equations, examples, and explanations to allow readers to evaluate EDT in unfamiliar situations. I plan to clarify how EDT evaluates actions, and the handling of dependencies and counterfactuals.


**Analyzing the Source**

I'm now analyzing the source document, focusing on definitions and contrasts. EDT emphasizes maximizing "news value," selecting actions with the best expected outcome upon learning one will take them. This contrasts with Causal Decision Theory, though they agree in many scenarios. I'm noting key differences and the core intuition behind EDT.


**Contrasting the Theories**

I'm now diving into the divergence of EDT and CDT, especially in thought experiments. The Newcomb's Paradox example really highlights the difference. I'm focusing on the formal descriptions of each theory, using the Gibbard & Harper (1976) framework, and the mathematics used to show why EDT chooses only Box B, calculating conditional and counterfactual expected utilities. I am paying close attention to the implications of these differences.


**Evaluating Examples**

I'm now deep-diving into examples to solidify my understanding of EDT. I've worked through Newcomb's Paradox and the Twin Prisoner's Dilemma, and have a good grasp of how EDT makes decisions in these cases. I'm also considering the Sleeping Beauty problem. I'm noting supportive arguments like the Evidentialist's Wager, but I am also aware of criticism regarding managing the news.


**Addressing Open Questions**

I'm now identifying critical open questions and gaps to allow for operational application. I'm wrestling with the interplay of actions, states, and outcomes in probability space and how to define that. Specifically, I'm trying to figure out how to specify the probability space $(\Omega, \mathcal{F}, P)$ so that both actions $A$ and states $S$ are events within the same algebra, given that outcomes are determined by state-action pairs $O = f(A, S)$. I also have to figure out how to handle zero or undefined action probabilities.


**Clarifying Assumptions**

I'm now clarifying crucial assumptions to make the framework practically usable, such as how to model scenarios where an agent is unable to choose a particular action, i.e., $P(A) = 0$. I am also considering how an agent assigns probabilities to free choices during deliberation. In addition, I am figuring out how to handle the medical and confounded cases, such as smoking lesions, where an evidential link may be screened off by learning one's state.

I'm now evaluating policies and sequential decisions, and how EDT evaluates multistage policies against isolated actions, incorporating pre-commitments, and policies with sequential updates. I'm focusing on the mechanics of these evaluations, including the role of Dutch books and correlated decision-makers.

I'm also working on operationalizing the differences between CDT and EDT.


**Formalizing Relationships**

I'm now formalizing the relationship between outcomes and actions, focusing on conditional probabilities and the distinctions between EDT and CDT. Specifically, I'm working on how to formally express the difference between $\mathrel{\Box{\rightarrow}}$ and $\mid$ using state partitions and causal Bayesian networks. I am getting close to defining exactly *when* EDT and CDT coincide and *why* they diverge.


**Defining the Core Equations**

I'm now zeroing in on the fundamental equations from Gibbard and Harper (1976), contrasting EDT's evidential calculation with its causal counterpart. I'm expanding this into a measurable space, demonstrating how to handle actions, states, and outcomes formally. The goal is to provide a precise mathematical grounding for EDT, using conditional probabilities and Bayes' theorem. I'm also working on proving the coincidence criterion when state partitions are fine enough.


**Analyzing Divergences**

I'm now analyzing key structural cases to illustrate when EDT and CDT diverge, starting with predictive asymmetry in Newcomb's Paradox, using precise numerical examples to demonstrate the diagnostic dependency. I'm also examining symmetric agential correlation, exemplified by the Twin Prisoner's Dilemma, showing how EDT evaluates correlated decisions.


**Operationalizing Correlation**

I'm now generalizing the Twin Prisoner's Dilemma to imperfect correlation, defining threshold parameters for cooperation. I'm deriving the minimal evidential correlation needed for cooperation. This involves calculating precise probabilities, working through the inequalities, and finding an explicit numerical threshold for the probability of the other player cooperating, given that I cooperate. I also have to define the operational gaps in the text.


**Operationalizing Solutions**

I am now focusing on operational resolutions, particularly evidential screening via deliberation conditioning. My current focus is on defining and applying EDT, distinct from the source material. I'm also grappling with the measure-zero problem, proposing solutions such as trembling-hand limits and primitive conditional probability spaces. Finally, I'm examining policies, uncertainty, and norms in sequential decision-making.


**Evaluating Policies**

I am now evaluating policies, which is an important evolution in my thought process. I'm focusing on the technical gaps, particularly concerning sequential/indexical problems like Sleeping Beauty. I'm grappling with how to evaluate whole policies when pre-commitment is possible versus using backwards induction when it's not. I'm also preparing to formalize the Evidentialist's Wager using math.


**Operationalizing Correlation**

I'm now zeroing in on generalizing my analysis of the Twin Prisoner's Dilemma to imperfect correlation. I'm actively defining threshold parameters for cooperation, and deriving the minimal evidential correlation needed to induce cooperation. This requires careful probability calculations and working through inequalities to find a numerical threshold. My current effort is focused on the text's operational gaps.



**Formalizing Calculations**

I'm now drafting the technical details, section by section. The math for Newcomb's Paradox is working well. I've explicitly included both the EDT and CDT calculations, and I'm using the formulas from Gibbard and Harper (1976). I also intend to work on making the calculations much more explicit. I'm focusing on providing more context to demonstrate how the two decision theories diverge.


**Calculating Correlation**

I am now deep in the math of the Twin Prisoner's Dilemma, working to generalize the analysis to imperfect correlation. I've successfully calculated the threshold correlation coefficient, using a conditional reliability parameter for cooperation, for EDT to recommend cooperation. The calculations rely on the equation 5α + 9β > 10, which I am now applying to an alpha-beta parameterization, where α = β = r, which simplifies to the expression of 14r > 10.


**Constructing Medical Example**

I'm now constructing a mathematical example to illustrate criticisms of EDT, inspired by Lewis and Joyce. I'm focusing on an unobserved common cause increasing both the propensity to take an action and the incidence of illness. My goal is to show how a naive EDT evaluation leads to an incorrect decision. I'll then demonstrate a refinement handling this, using deliberation conditioning or distinguishing confounding and algorithmic correlation.


```
