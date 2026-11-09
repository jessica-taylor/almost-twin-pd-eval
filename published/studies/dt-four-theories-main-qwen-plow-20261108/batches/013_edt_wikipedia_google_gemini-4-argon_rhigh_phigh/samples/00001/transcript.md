# 013_edt_wikipedia_google_gemini-4-argon_rhigh_phigh / 00001

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/37d5e8e7-b66a-4987-8f07-95d712fc84f0/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/37d5e8e7-b66a-4987-8f07-95d712fc84f0/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Acting on Good News: The Mathematics and Philosophy of Evidential Decision Theory

When a rational agent stands at a crossroads and deliberates between competing courses of action, what makes one choice better than another? The intuitive answer is that a good action *causes* good results. Yet in a wide class of decision problems—ranging from game-theoretic interactions with similar reasoners to environments containing predictive algorithms—an agent’s choice does more than push causal levers in the future. It also provides statistical evidence about the state of the world as it already is, or as other agents elsewhere are simultaneously making it.

**Evidential decision theory** (EDT) is the school of thought within formal decision theory that takes this informational role of action as foundational. As characterized in the philosophical literature, EDT holds that when an agent confronts a set of possible actions, she should select the action with the highest *news value*: the option that would be most indicative of a favorable outcome in expectation if she were to receive the "news" that she had taken it. In Arif Ahmed’s compact maxim, EDT counsels the agent to "do what you most want to learn that you will do" (Ahmed 2021, p. 7).

This essay provides a mathematical and philosophical guide to Evidential Decision Theory. Drawing on the core concepts, formulas, and thought experiments established in the foundational literature, we will examine how EDT evaluates actions, why it diverges from **causal decision theory** (CDT), and how it handles classic puzzles like Newcomb’s paradox and the Twin Prisoner’s Dilemma. Where the introductory literature leaves operational questions open—such as how to parameterize state spaces, how to handle zero-probability actions during deliberation, how to diagnose confounding common causes, and how to formalize multi-agent stakes—we will explicitly step beyond the reference text to construct a rigorous operational manual capable of resolving unfamiliar decision problems.

---

## 1. The Formal Architecture of EDT and CDT

The formal distinction between evidential and causal expected utility maximization was crystallized in a landmark 1976 paper by Allan Gibbard and William Harper. As summarized in the reference text, both theories evaluate an action $A$ by taking a probability-weighted average of the desirabilities of possible outcomes $O_j$, but they disagree on which probability measure governs the weighting.

Under Evidential Decision Theory, the value $V(A)$ of performing action $A$ is computed using standard **conditional probabilities**:

$$V(A) = \sum_{j} P(O_j \mid A) D(O_j)$$

where $D(O_j) \in \mathbb{R}$ represents the agent's cardinal desirability (or utility) assigned to outcome $O_j$, and $P(O_j \mid A)$ is the conditional probability that outcome $O_j$ obtains given the proposition that action $A$ occurs (Gibbard & Harper 1976).

Causal Decision Theory, by contrast, replaces conditional probabilities with **counterfactual probabilities**. Its utility function $U(A)$ is written as:

$$U(A) = \sum_{j} P(A \mathrel{\Box{\rightarrow}} O_j) D(O_j)$$

where the subjunctive conditional $A \mathrel{\Box{\rightarrow}} O_j$ reads "if $A$ were performed, then $O_j$ would occur," and $P(A \mathrel{\Box{\rightarrow}} O_j)$ denotes the probability of $O_j$ in the counterfactual situation in which $A$ is enacted (Gibbard & Harper 1976). Because $P(O_j \mid A)$ and $P(A \mathrel{\Box{\rightarrow}} O_j)$ are not always equal, the two maximization criteria are not equivalent.

### Extending the Formalism: State-Action Factorization

While the source text states the Gibbard–Harper formulas directly in terms of holistic outcomes $O_j$, applying these equations to concrete, unfamiliar problems requires a slight formal elaboration. Notice that in the source’s worked examples (such as Newcomb's paradox), the probabilities conditioned on $A$ are not complete outcomes, but rather *states of the environment* (e.g., "$1M in box B"), while the payoffs depend jointly on the state and the chosen action.

To make this implicit step fully general—an operational formalism we introduce here—let us define a decision problem as a tuple $(\mathcal{A}, \mathcal{S}, P, D)$, where:
* $\mathcal{A} = \{A_1, A_2, \dots, A_n\}$ is a finite, mutually exclusive, and collectively exhaustive set of available actions.
* $\mathcal{S} = \{S_1, S_2, \dots, S_m\}$ is a finite partition of the exogenous states of the world (events outside the agent's direct definition of her act).
* Each fine-grained outcome $O_{i,k}$ is the conjunction of an action and a state: $O_{i,k} = A_i \land S_k$.
* $D(A_i, S_k)$ is the utility the agent receives when she performs $A_i$ and the world is in state $S_k$.

Because actions are mutually exclusive ($P(A_i \mid A_r) = 1$ if $i=r$ and $0$ otherwise), any outcome $O_{r,k}$ with $r \neq i$ has conditional probability $P(A_r \land S_k \mid A_i) = 0$. Consequently, the Gibbard–Harper EDT equation simplifies to a sum over environmental states:

$$V(A_i) = \sum_{k=1}^{m} P(S_k \mid A_i) D(A_i, S_k) \quad \text{where} \quad P(S_k \mid A_i) = \frac{P(S_k \land A_i)}{P(A_i)}$$

Similarly, under the standard assumption that an agent's counterfactual intervention fixes $A_i$ with certainty, the CDT equation becomes:

$$U(A_i) = \sum_{k=1}^{m} P(A_i \mathrel{\Box{\rightarrow}} S_k) D(A_i, S_k)$$

In problems where the states $S_k$ are causally independent of the agent’s present action—meaning that what the agent does *now* cannot causally alter whether $S_k$ obtains—CDT holds that $P(A_i \mathrel{\Box{\rightarrow}} S_k) = P(S_k)$ for all $A_i$. In such causally independent environments, we can isolate the exact mathematical wedge between the two theories by subtracting $U(A_i)$ from $V(A_i)$:

$$\Delta(A_i) \equiv V(A_i) - U(A_i) = \sum_{k=1}^{m} \big[ P(S_k \mid A_i) - P(S_k) \big] D(A_i, S_k)$$

We may call $\Delta(A_i)$ the **pure diagnostic premium** of action $A_i$. Whenever $P(S_k \mid A_i) = P(S_k)$—that is, when states and actions are statistically independent—$\Delta(A_i) = 0$, and EDT and CDT issue identical prescriptions. The two theories diverge precisely when an action carries statistical information about causally independent states of the world ($P(S_k \mid A_i) \neq P(S_k)$).

---

## 2. Canonical Thought Experiments and Their Generalizations

To see how the diagnostic premium drives decision-making, let us examine the two centerpiece thought experiments presented in the reference article—Newcomb's paradox and the Twin Prisoner's Dilemma—and generalize their algebraic conditions so they can be applied across whole families of structurally similar problems.

### Newcomb's Paradox

In Newcomb's paradox (Wolpert & Benford 2013; Ahmed 2021), an agent faces two boxes, designated A and B, and a predictor who has already forecast the agent's choice with high accuracy (specifically, $99\%$ in the source text). The rules are common knowledge:
* **Box A** is transparent and visibly contains $\$1,000$.
* **Box B** is opaque. Before the game begins, the predictor places $\$1,000,000$ inside Box B if and only if she predicts the agent will take *only Box B* ("one-boxing"). If she predicts the agent will take *both boxes A and B* ("two-boxing"), she leaves Box B empty ($\$0$).

The agent must choose between $A_1 = \text{take only B}$ and $A_2 = \text{take both boxes}$. The relevant states of the world are $S_1 = \text{1M in box B}$ and $S_2 = \text{nothing in box B}$. Following the source text, EDT evaluates the two options by conditioning directly on the choice:

$$\begin{aligned}
V(\text{take only B}) &= P(\text{1M in box B} \mid \text{take only B}) \times \$1,000,000 + P(\text{nothing in box B} \mid \text{take only B}) \times \$0 \\
&= 0.99 \times \$1,000,000 + 0.01 \times \$0 = \$990,000
\end{aligned}$$

$$\begin{aligned}
V(\text{take both boxes}) &= P(\text{1M in box B} \mid \text{take both boxes}) \times \$1,001,000 + P(\text{nothing in box B} \mid \text{take both boxes}) \times \$1,000 \\
&= 0.01 \times \$1,001,000 + 0.99 \times \$1,000 = \$11,000
\end{aligned}$$

Because $V(\text{take only B}) > V(\text{take both boxes})$, EDT decisively recommends taking only Box B (Ahmed 2021, p. 22). Taking only Box B is overwhelming evidence that the predictor foresaw this choice and stocked Box B with $\$1,000,000$. Conversely, CDT notes that the predictor's action lies in the fixed past: whether the agent takes one box or two cannot causally alter the contents of Box B. Under CDT, $P(\text{take only B} \mathrel{\Box{\rightarrow}} S_1) = P(\text{take both} \mathrel{\Box{\rightarrow}} S_1) = P(S_1)$. Because $\$1,001,000 > \$1,000,000$ and $\$1,000 > \$0$, two-boxing strictly dominates one-boxing in every state, yielding $U(\text{take both}) = U(\text{take only B}) + \$1,000$.

**Generalizing the Newcomb Threshold (Analytical Extension):** Suppose we encounter an unfamiliar predictive environment where the opaque reward is $M > 0$, the guaranteed transparent reward is $c > 0$ (assuming linear utility in money), and the predictor's conditional accuracy is $p = P(S_1 \mid A_1) = P(S_2 \mid A_2) \in [0, 1]$. Then:

$$V(A_1) = p M + (1 - p)(0) = p M$$

$$V(A_2) = (1 - p)(M + c) + p c = (1 - p)M + c$$

Setting $V(A_1) > V(A_2)$ yields the general decision boundary for an evidentialist:

$$p M > (1 - p)M + c \iff (2p - 1)M > c \iff p > \frac{1}{2} + \frac{c}{2M}$$

In the classic setup where $M = \$1,000,000$ and $c = \$1,000$, EDT recommends one-boxing whenever the predictor's accuracy exceeds $p^* = 0.5005$. If the predictor is barely better than a coin flip, the evidential news value of one-boxing is too weak to offset the guaranteed $\$1,000$, and EDT switches to recommending two-boxing! This illustrates an important feature of EDT: it does not blindly reject dominance reasoning; rather, it trades off direct payoff increments against the informational shift $P(S_k \mid A_1) - P(S_k \mid A_2)$.

### The Twin Prisoner's Dilemma

Whereas Newcomb's problem involves a past prediction of a present act, the **Twin Prisoner's Dilemma** (Greene & Levinstein 2020) involves a symmetric, simultaneous correlation between two agents who share an identical decision architecture.

In the source's formulation, Aomame and her psychological twin—whose reasoning processes are exactly analogous to her own—are placed in separate rooms unable to communicate. Each must choose whether to **Cooperate** ($C$) or **Defect** ($D$). Caring only about her own individual payout, Aomame faces the following payoff matrix:

| Aomame \ Twin | Twin Cooperates ($S_C$) | Twin Defects ($S_D$) |
| :--- | :---: | :---: |
| **Aomame Cooperates ($C$)** | $\$5$ | $\$0$ |
| **Aomame Defects ($D$)** | $\$10$ | $\$1$ |

Because the twin cannot hear or see Aomame, Aomame's choice has zero causal effect on the twin's choice. CDT therefore treats the twin's action as fixed and recommends defecting ($\$10 > \$5$ if the twin cooperates; $\$1 > \$0$ if the twin defects), locking both twins into the mutually destructive $(D, D)$ outcome of $\$1$ each.

Under EDT, however, Aomame treats her own decision as a diagnostic sample of what her twin is simultaneously deciding. In the limit of an exact psychological twin, $P(S_C \mid C) = 1$ and $P(S_D \mid D) = 1$. As given in the source text:

$$\begin{aligned}
V(\text{Aomame cooperates}) &= P(\text{twin cooperates} \mid \text{Aomame cooperates}) \times \$5 + P(\text{twin defects} \mid \text{Aomame cooperates}) \times \$0 \\
&= 1 \times \$5 + 0 \times \$0 = \$5
\end{aligned}$$

$$\begin{aligned}
V(\text{Aomame defects}) &= P(\text{twin cooperates} \mid \text{Aomame defects}) \times \$10 + P(\text{twin defects} \mid \text{Aomame defects}) \times \$1 \\
&= 0 \times \$10 + 1 \times \$1 = \$1
\end{aligned}$$

Since $V(C) = \$5 > V(D) = \$1$, EDT prescribes cooperation, allowing evidentialists to achieve the Pareto-superior $\$5$ outcome without communication or binding contracts.

**Generalizing to Partial Correlation (Analytical Extension):** Real-world counterparts—such as competing firms using similar machine-learning pricing algorithms, or citizens with shared ideological commitments—are rarely perfect twins. To apply EDT to imperfect counterparts, consider a general Prisoner's Dilemma with payoffs $T > R > P > S$ (in Aomame's case, $T=10, R=5, P=1, S=0$). Let the diagnostic similarity between the agent and her counterpart be parameterized by $\rho = P(S_C \mid C) = P(S_D \mid D) \in [0.5, 1]$. Then:

$$V(C) = \rho R + (1 - \rho) S \quad \text{and} \quad V(D) = (1 - \rho) T + \rho P$$

EDT prescribes cooperation whenever $V(C) > V(D)$, which simplifies to:

$$\rho (R - S + T - P) > T - S \iff \rho > \frac{T - S}{(T - S) + (R - P)}$$

For Aomame's payoffs, this threshold is $\rho^* = \frac{10 - 0}{(10 - 0) + (5 - 1)} = \frac{10}{14} \approx 0.714$. Whenever Aomame's choice is at least $71.4\%$ indicative of her twin's choice, EDT sustains cooperation.

---

## 3. Dependencies, Counterfactuals, and the "Managing the News" Critique

Why do many philosophers and decision theorists resist EDT despite its lucrative payoffs in Newcomb's problem and the Twin Prisoner's Dilemma? The source article highlights the sharp criticism leveled by architects of Causal Decision Theory:
* **David Lewis (1981)** characterized EDT as promoting "an irrational policy of managing the news."
* **James M. Joyce (1999, p. 146)** argued that "Rational agents choose acts on the basis of their *causal efficacy*, not their auspiciousness; they act to *bring about* good results even when doing so might betoken bad news."

To understand the force of this criticism—and to equip a practitioner to analyze how EDT and CDT diverge in general causal structures—we need to formalize how non-causal dependencies arise. (The structural model and diagnostic example below are our own analytical elaboration designed to make the Lewis–Joyce critique mathematically explicit.)

### Structural Confounding vs. Causal Efficacy

In probability theory, Reichenbach's Common Cause Principle tells us that if two events $A$ (an action) and $S$ (a state of the world) are correlated ($P(S \mid A) \neq P(S)$), then either $A$ causes $S$, $S$ causes $A$ (impossible if $S$ is fixed prior to or independently of the act without mediating signals), or there exists a third factor $C$—a **common cause** or **confounder**—that causally influences both $A$ and $S$:

$$A \longleftarrow C \longrightarrow S$$

In Newcomb's paradox, $C$ is the agent's prior psychological disposition, which both guides the predictor's forecast ($C \to S$) and guides the agent's eventual choice ($C \to A$). In the Twin Prisoner's Dilemma, $C$ is the shared cognitive architecture of the twins.

However, the identical causal graph $A \leftarrow C \to S$ also governs mundane medical and diagnostic decisions where "managing the news" seems manifestly dangerous. Consider a stylized **Confounded Prophylaxis Problem**:
* Suppose an undiscovered genetic mutation $C \in \{c_1, c_0\}$ (with base rate $P(c_1) = 0.2$) has two independent effects: first, it causes a severe metabolic syndrome $S_1$ later in life with probability $0.8$ (whereas without the gene, $P(S_1 \mid c_0) = 0.1$); second, it causes mild acid reflux in early adulthood, prompting $90\%$ of carriers to take an over-the-counter antacid $A_1$ (whereas only $10\%$ of non-carriers take $A_1$).
* Taking the antacid $A_1$ has no causal effect on the metabolic syndrome $S_1$, and successfully relieves the annoying reflux (adding $+1$ utility). Developing the metabolic syndrome $S_1$ inflicts a utility loss of $-100$ (so $S_0$, remaining healthy, has utility $0$).

Let us compute the probabilities if an agent evaluates $A_1$ (take antacid) vs. $A_0$ (refuse antacid) using raw conditional probabilities $P(S_1 \mid A)$ without knowing her genetic status $C$. By Bayes' theorem:

$$P(c_1 \mid A_1) = \frac{P(A_1 \mid c_1)P(c_1)}{P(A_1 \mid c_1)P(c_1) + P(A_1 \mid c_0)P(c_0)} = \frac{0.9 \times 0.2}{(0.9 \times 0.2) + (0.1 \times 0.8)} = \frac{0.18}{0.26} \approx 0.692$$

$$P(c_1 \mid A_0) = \frac{P(A_0 \mid c_1)P(c_1)}{P(A_0 \mid c_1)P(c_1) + P(A_0 \mid c_0)P(c_0)} = \frac{0.1 \times 0.2}{(0.1 \times 0.2) + (0.9 \times 0.8)} = \frac{0.02}{0.74} \approx 0.027$$

Propagating these posterior credences to the disease state $S_1$ via $P(S_1 \mid A_i) = P(S_1 \mid c_1)P(c_1 \mid A_i) + P(S_1 \mid c_0)P(c_0 \mid A_i)$:

$$P(S_1 \mid A_1) = 0.8(0.692) + 0.1(0.308) \approx 0.584$$

$$P(S_1 \mid A_0) = 0.8(0.027) + 0.1(0.973) \approx 0.119$$

Now compare the naive EDT evaluation $V(A)$ against the CDT evaluation $U(A)$:
* **Naive EDT:**
  $$V(A_1) = 0.584(-100 + 1) + 0.416(0 + 1) = -57.4$$
  $$V(A_0) = 0.119(-100) + 0.881(0) = -11.9$$
  Because $V(A_0) > V(A_1)$, a naive application of EDT tells the agent to endure the painful acid reflux and refuse the antacid, purely because taking the antacid is "bad news" indicating she likely carries the gene $c_1$!
* **CDT:** Counterfactual conditioning $P(A_i \mathrel{\Box{\rightarrow}} S_1)$ severs the incoming causal arrow $C \to A$ (analogous to Judea Pearl's causal intervention operator $P(S_1 \mid \text{do}(A_i))$), holding the prior distribution of the background cause $C$ fixed at $P(c_1) = 0.2$. Thus, $P(A_1 \mathrel{\Box{\rightarrow}} S_1) = P(A_0 \mathrel{\Box{\rightarrow}} S_1) = 0.2(0.8) + 0.8(0.1) = 0.24$. Consequently:
  $$U(A_1) = -24 + 1 = -23 > U(A_0) = -24$$
  CDT rightly recommends taking the antacid to relieve the reflux.

This contrast reveals the exact mathematical mechanics behind Lewis's and Joyce's objection: standard conditionalization $P(S \mid A)$ transmits probability updates backwards along the causal arrow $A \leftarrow C$ and then forwards along $C \to S$, whereas counterfactual imaging $P(A \mathrel{\Box{\rightarrow}} S)$ blocks backward inference through pre-existing causes.

---

## 4. Open Questions and Operational Proposals for Unfamiliar Cases

The reference article outlines the core equation $V(A) = \sum_j P(O_j \mid A) D(O_j)$, the canonical thought experiments, and the brief philosophical debate over news value and Dutch books. However, if a mathematically minded researcher attempts to use the source article alone as an algorithm for arbitrary, unfamiliar decision problems, three critical operational gaps emerge. Here, we identify those gaps and develop concrete mathematical proposals to resolve them.

### Open Question 1: How Do We Evaluate Actions with Zero (or Near-Zero) Prior Probability?

In Kolmogorov probability theory, conditional probability is defined as a ratio:

$$P(O_j \mid A) = \frac{P(O_j \land A)}{P(A)}$$

This ratio is well-defined *only if* $P(A) > 0$. Yet during rational deliberation, an agent who knows her own preferences and rationality may already be virtually certain that she will perform the optimal action $A^*$ and will not perform a suboptimal action $A'$, driving $P(A') \to 0$. Even worse, if the agent operates under deterministic self-knowledge, $P(A') = 0$ for every unchosen option, rendering $V(A')$ mathematically undefined ($0/0$). The reference article does not specify how $P(O_j \mid A)$ is defined when $P(A) = 0$.

**Operational Proposal (The $\varepsilon$-Tremble Regularization):** To apply EDT to any decision problem without division by zero, we propose modeling deliberation within a perturbed "trembling-hand" probability space $P_\varepsilon$, parameterized by a small execution noise rate $\varepsilon \in (0, 1)$. Specifically, suppose that whatever action $A^*$ the agent's deliberation endorses, physical or cognitive noise causes a uniform random action from $\mathcal{A}$ (with $|\mathcal{A}| = n$) to be executed with probability $\varepsilon$:

$$P_\varepsilon(A_i) = (1 - \varepsilon)\mathbb{I}(A_i = A^*) + \frac{\varepsilon}{n}$$

Because $P_\varepsilon(A_i) \ge \varepsilon / n > 0$ for all $A_i \in \mathcal{A}$, every conditional probability $P_\varepsilon(S_k \mid A_i)$ is strictly well-defined. We then define the operational evidential value $V^*(A_i)$ by taking the limit as the tremble vanishes:

$$V^*(A_i) = \lim_{\varepsilon \to 0^+} \sum_{k=1}^{m} P_\varepsilon(S_k \mid A_i) D(A_i, S_k)$$

Crucially, in this formulation, how the environment responds to a tremble depends on the physical mechanism of correlation:
* If a predictor or twin correlates only with the agent's *underlying intention* $A^*$ and cannot foresee a last-millisecond motor tremble $\varepsilon$, then $P_\varepsilon(S_k \mid A_i)$ for an unintended action $A_i \neq A^*$ will reflect the state distribution induced by $A^*$.
* Conversely, if the predictor simulates the agent *including* the physical cause of the deviation, or if we interpret $P(S_k \mid A_i)$ via a primitive conditional probability space (a Popper–Rényi probability function $P(\cdot \mid \cdot)$ where conditioning on measure-zero events is primitive), $P(S_k \mid A_i)$ tracks the hypothesis that the agent genuinely deliberated her way to $A_i$. In applied modeling, the analyst must explicitly specify which noise mechanism applies; standard EDT thought experiments assume the latter (deliberative conditioning), where $P(S_k \mid A_i)$ evaluates the world in which the agent's rational deliberation itself culminates in $A_i$.

### Open Question 2: Can EDT Distinguish Spurious Medical Confounding from Newcomb-Like Correlation?

In Section 3, we saw that naive application of $V(A)$ to the Confounded Prophylaxis Problem recommended refusing a beneficial antacid so as not to receive "bad news" about one's genetics. Does committing to EDT require biting the bullet on medical self-deception (as hardline evidentialists like Ahmed 2021 sometimes argue when all intermediary variables are hidden), or can an operational version of EDT separate spurious common-cause confounding from genuine algorithmic correlation?

**Operational Proposal (Introspective Screening Conditioning):** In most real-world confounding scenarios—unlike Newcomb's paradox—a genetic or environmental common cause $C$ can only influence a rational agent's voluntary action $A$ by first producing an *introspectively accessible proximate symptom or desire* $I$ (such as feeling heartburn or craving a substance):

$$C \longrightarrow I \longrightarrow A \quad \text{and} \quad C \longrightarrow S$$

In this Markov chain, the internal state $I$ **d-separates** (screens off) the action $A$ from the hidden cause $C$ and the disease state $S$. That is, once the agent already knows she has heartburn ($I = i_1$), her subsequent choice to take the antacid ($A_1$) provides *no additional evidence* about whether she carries the gene $C$:

$$P(S_k \mid A_i, I = i_1) = P(S_k \mid I = i_1) \quad \forall A_i \in \mathcal{A}$$

We therefore propose that before computing $V(A_i)$ in any unfamiliar problem, the analyst must expand the conditioning base to include the agent's maximal introspectively accessible pre-choice information set $\mathcal{I}$:

$$V_{\text{screened}}(A_i \mid \mathcal{I}) = \sum_{k=1}^{m} P(S_k \mid A_i, \mathcal{I}) D(A_i, S_k)$$

Notice how neatly this operational rule partitions decision problems into two classes:
1. **Screened Confounding (e.g., Medical/Smoking Lesions):** Because the agent already experiences the symptom or desire $\mathcal{I}$ prior to choosing $A_i$, conditioning on $\mathcal{I}$ renders $S_k$ conditionally independent of $A_i$. The diagnostic premium $\Delta(A_i \mid \mathcal{I})$ collapses to zero, and EDT agrees with CDT: take the antacid!
2. **Unscreened Algorithmic Correlation (e.g., Newcomb's Paradox and Twin PD):** Why doesn't $\mathcal{I}$ screen off $A_i$ in Newcomb's problem or the Twin Prisoner's Dilemma? Because the predictor (or twin) is not merely correlating with a prior urge; she is replicating the exact mapping from $\mathcal{I}$ to the final output $A_i$. Even holding $\mathcal{I}$ fixed, learning which final output $A_i$ the deliberative algorithm produces reveals which output the twin or predictor's simulation produced: $P(S_k \mid A_i, \mathcal{I}) \neq P(S_k \mid \mathcal{I})$. Thus, $V_{\text{screened}}(A_i \mid \mathcal{I})$ preserves one-boxing in Newcomb's paradox and cooperation in the Twin Prisoner's Dilemma while eliminating superstitious news management whenever proximate causes are observable.

### Open Question 3: Sequential Decisions, Indexicals, and the Sleeping Beauty Problem

The reference text briefly notes a third battleground: the **Sleeping Beauty problem**, an epistemic puzzle in which an experimental subject (Beauty) is put to sleep on Sunday, a fair coin is flipped, and she is awakened once (on Monday) if the coin lands Heads ($H$), but awakened twice (on Monday and Tuesday, with her memory of Monday erased in between) if the coin lands Tails ($T$). Upon waking, with no knowledge of whether it is Monday or Tuesday, what credence should Beauty assign to $H$, and what bets should she accept?

The source notes that some theorists invoke EDT to protect "halfers" (those who maintain $P(H) = 1/2$ upon waking) from **Dutch book arguments**—sequences of bets conducted across time that guarantee a deterministic net loss in every state of the world—while Vincent Conitzer (2015) demonstrates that halfers remain vulnerable to Dutch books even after adopting EDT. The source leaves open *why* this vulnerability arises and how an EDT practitioner should evaluate sequential bets involving self-locating ("indexical") uncertainty.

**Operational Proposal (Ex-Ante Policy Evaluation vs. De Se Awakening Bets):** To diagnose why EDT behaves delicately in Sleeping Beauty, we must mathematicalize how betting frequency interacts with evidential conditioning. Suppose upon each awakening, Beauty is offered a bet $B$ that pays $+x$ if $H$ is true and costs $-y$ if $T$ is true.
* Why was EDT originally thought to save the halfer? Under CDT, if Beauty wakes up and has credence $P(H) = 1/2$, she treats her decision to accept the bet *now* as causally independent of what she does in a Tuesday awakening. She will accept any bet with $x > y$. Meanwhile, on Sunday (when $P(H) = 1/2$), a bookie can sell her a hedging bet that triggers once on $H$ and once on $T$. Because the awakening bet triggers *twice* when $T$ occurs (both Monday and Tuesday) and only *once* when $H$ occurs, a CDT halfer ends up losing $-2y$ on Tails and winning only $+x$ on Heads, suffering a guaranteed loss whenever $y < x < 2y$.
* Under EDT, however, Beauty is functionally in a Twin dilemma with her other possible awakening self! If she decides to accept the bet upon waking, she knows that if the coin landed $T$, her identical epistemic twin in the other awakening also accepts the bet. Therefore, conditional on accepting the bet ($A_{\text{bet}}$) at an awakening, the total net payoff of the experiment on Tails is $-2y$, not $-y$. Even if she maintains $P(H \mid A_{\text{bet}}) = 1/2$, her evidential expectation over total experimental outcomes is:

$$V(A_{\text{bet}}) = P(H \mid A_{\text{bet}})(+x) + P(T \mid A_{\text{bet}})(-2y) = \frac{1}{2}x - y$$

Thus, an EDT halfer who evaluates global outcomes rejects the bet unless $x > 2y$ (behaving behaviorally just like a "thirder" who assigns $P(H) = 1/3$!).
* How, then, does Conitzer (2015) construct a Dutch book against an EDT halfer? As Conitzer shows, if the bets offered upon waking pay off in *local/centered goods* (consumption experienced only during *that specific* awakening, or bets conditioned on subtle asymmetries in indexical evidence across awakenings) so that the agent evaluates only the news value for her *current awakening* rather than the sum of correlated awakenings, the wedge between $P(H) = 1/2$ and the $1\text{:}2$ frequency of Heads-to-Tails awakenings resurfaces.

To prevent Dutch books in sequential and self-locating problems, we propose the following operational rule: an evidential decision theorist must evaluate **complete conditional policies** $\pi : \mathcal{H} \to \mathcal{A}$ (mappings from information histories $\mathcal{H}$ to actions) using ex-ante global utilities, computing:

$$V(\pi) = \sum_{k=1}^{m} P(S_k \mid \pi) D(\pi, S_k)$$

Evaluating global policies $\pi$ automatically accounts for the multiplicity of awakenings within each state $S_k$, rendering the agent immune to diachronic Dutch books.

---

## 5. Multi-Agent Correlation and the Evidentialist's Wager

Even if a researcher remains philosophically torn between EDT and CDT, there is a compelling meta-decision argument mentioned in the reference article: **The Evidentialist's Wager** (MacAskill et al. 2021). The source notes that even if one places low credence in Evidential Decision Theory as the true normative standard of rationality, it may still be reasonable to act *as if* EDT were true, because EDT incorporates the actions of many correlated decision-makers, making its stakes much higher than those of CDT.

While the source states this conclusion qualitatively, we can construct a formal mathematical model of this meta-decision to show exactly how the wager operates in practice.

### Formalizing the Meta-Decision Under Normative Uncertainty

Consider a large-scale collective action problem—such as voting in an election, reducing carbon emissions, or adhering to safety standards in artificial intelligence research—involving $N$ agents who face a similar decision environment. Suppose our focal agent must choose between a costly cooperative action $C$ (which incurs a personal cost $c > 0$ and contributes a public benefit $b > 0$, where $b < c$ so that individual contribution is personally net-costly) and defecting $D$ (which costs $0$ and contributes $0$).

Let $K \in \{0, 1, \dots, N-1\}$ be the random variable denoting how many of the *other* $N-1$ agents choose $C$. The total utility to our agent is the total public good generated minus her own cost:

$$D(C, K) = (K + 1)b - c \quad \text{and} \quad D(D, K) = K b$$

Now compare how CDT and EDT evaluate $C$ versus $D$:
1. **Under CDT:** Because the other $N-1$ agents do not observe our agent's choice prior to making their own, her action has zero causal effect on $K$. The counterfactual expectation of $K$ is simply its unconditional mean $\mathbb{E}[K] = \mu$. Thus:
   $$U_{\text{CDT}}(C) - U_{\text{CDT}}(D) = \big[(\mu + 1)b - c\big] - \mu b = b - c < 0$$
   CDT strictly recommends defection ($D$), with a net causal stake of $|b - c|$.
2. **Under EDT:** Suppose each of the other $N-1$ agents has an excess statistical correlation $\rho \in (0, 1]$ with our agent's decision, such that $\mathbb{E}[K \mid C] - \mathbb{E}[K \mid D] = \rho (N - 1)$. Then:
   $$V_{\text{EDT}}(C) - V_{\text{EDT}}(D) = \big(\mathbb{E}[K \mid C] - \mathbb{E}[K \mid D] + 1\big)b - c = \big[1 + \rho(N - 1)\big]b - c$$
   Whenever the reference class is sufficiently large that $[1 + \rho(N - 1)]b > c$, EDT recommends cooperation ($C$).

Now suppose the agent is uncertain which decision theory is normatively correct: she assigns credence $q \in (0, 1)$ to EDT and $1 - q$ to CDT. Under a standard expected-choice-worthiness maximization rule across theories, she should cooperate if and only if the credence-weighted advantage of $C$ is positive:

$$\mathcal{M}(C) - \mathcal{M}(D) = q \big[V_{\text{EDT}}(C) - V_{\text{EDT}}(D)\big] + (1 - q)\big[U_{\text{CDT}}(C) - U_{\text{CDT}}(D)\big] > 0$$

Substituting the expressions above yields:

$$q \big[(1 + \rho(N - 1))b - c\big] + (1 - q)(b - c) > 0 \iff \big[1 + q \rho (N - 1)\big]b > c$$

Solving for the minimum normative credence $q^*$ required to tip the agent into cooperating:

$$q^* = \frac{c - b}{\rho(N - 1)b}$$

Suppose an individual climate or policy contribution has $c = 10$ and $b = 1$ (so an individual loses $9$ units of utility under CDT), but the agent belongs to a reference class of $N = 100,001$ similar decision-makers with a modest diagnostic correlation of $\rho = 0.05$. Then $\rho(N - 1) = 5,000$, and the critical threshold is:

$$q^* = \frac{10 - 1}{5,000 \times 1} = 0.0018$$

Even if the agent is $99.8\%$ convinced that Causal Decision Theory is right and places less than a $0.2\%$ credence in Evidential Decision Theory, the amplification factor $\rho(N - 1)$ makes the EDT stakes tower over the CDT stakes, compelling her to act like an evidentialist!

---

## 6. Summary Recipe: Deciding Unfamiliar Cases with EDT

To consolidate the formal theory and our operational extensions into a practical workflow, an analyst confronting a novel decision problem can apply Evidential Decision Theory in five structured steps:

1. **Specify the Partition $(\mathcal{A}, \mathcal{S})$ and Payoffs $D(A_i, S_k)$:** List the mutually exclusive actions $\mathcal{A} = \{A_1, \dots, A_n\}$ and partition the relevant external environment into exhaustive states $\mathcal{S} = \{S_1, \dots, S_m\}$. If the problem is sequential or involves self-locating uncertainty (like Sleeping Beauty), define $\mathcal{A}$ over complete conditional policies $\pi$.
2. **Isolate Pre-Choice Introspective Evidence $\mathcal{I}$:** Identify all symptoms, signals, and desires $\mathcal{I}$ observable by the agent prior to acting. Condition the prior distribution of states on $\mathcal{I}$ to obtain $P(S_k \mid \mathcal{I})$.
3. **Map the Diagnostic Dependencies $P(S_k \mid A_i, \mathcal{I})$:** For each candidate action $A_i$ (using an $\varepsilon$-tremble limit if $P(A_i \mid \mathcal{I}) = 0$), determine whether learning that deliberation resulted in $A_i$ updates the probability of $S_k$ beyond what $\mathcal{I}$ already reveals.
   * If the link between $A_i$ and $S_k$ is mediated entirely by $\mathcal{I}$ (screened confounding), set $P(S_k \mid A_i, \mathcal{I}) = P(S_k \mid \mathcal{I})$.
   * If $S_k$ represents the output of a predictor, twin, or correlated reference class of size $N$ that tracks the final choice $A_i$ itself, compute $P(S_k \mid A_i, \mathcal{I})$ via Bayes' theorem.
4. **Compute Evidential Expected Utility $V(A_i)$:** Evaluate $V(A_i) = \sum_{k} P(S_k \mid A_i, \mathcal{I}) D(A_i, S_k)$ for each action (and, if operating under normative uncertainty with credence $q$ in EDT, weigh $V(A_i)$ against $U(A_i)$).
5. **Select the Maximizer:** Choose $A^* = \arg\max_{A_i \in \mathcal{A}} V(A_i)$.

---

## 7. Conclusion

Evidential Decision Theory offers a mathematically elegant and philosophically provocative answer to the question of rational agency. By grounding expected utility in the standard conditional probability $P(O_j \mid A)$ rather than the counterfactual conditional $P(A \mathrel{\Box{\rightarrow}} O_j)$, EDT treats an agent's own choices not merely as levers that push the future, but as diagnostic windows into the structure of the world. While critics from David Lewis to James Joyce have warned against the perils of "managing the news," EDT's capacity to secure one-boxing fortunes in Newcomb's paradox, achieve mutual cooperation in the Twin Prisoner's Dilemma, and leverage collective stakes in the Evidentialist's Wager ensures its enduring centrality in decision theory, game theory, and the foundations of artificial intelligence.

---

## References

* Ahmed, Arif (2021). *Evidential Decision Theory*. Cambridge University Press. ISBN 9781108607865.
* Conitzer, Vincent (2015). "A Dutch book against sleeping beauties who are evidential decision theorists". *Synthese*, 192 (9): 2887–2899. doi:10.1007/s11229-015-0691-7.
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
**Defining the Task**

I'm now clarifying the requirements, focusing on the essay or blog post about Evidential Decision Theory. I need to ensure a mathematically literate audience can grasp and apply the concepts. I'm aiming for a clear, concise explanation.


**Expanding the Formalism**

I am now focusing on expanding the formalism of Evidential Decision Theory. I'm taking the foundational definition, and its contrast with Causal Decision Theory, as the core. I'm diving into the formal description, aiming to unpack the implications of the EDT formula ($V(A) = \sum_j P(O_j \mid A) D(O_j)$). I am working to clarify the conditional probability ($P(O_j \mid A)$) in this context. I will also contrast it with the CDT formula.


**Contrasting EDT with CDT**

Now, I'm focusing on the core difference: counterfactual probability versus conditional probability.  I'm exploring how these distinct perspectives manifest in specific thought experiments. Newcomb's Paradox and the Twin Prisoner's Dilemma are providing compelling examples. I'm actively unpacking how EDT and CDT arrive at diverging recommendations in these scenarios, aiming to clarify the underlying logic and rationale of each decision theory.


**Analyzing EDT Implications**

I'm now diving into implications. I'm focusing on the Sleeping Beauty problem and its link to Dutch books, also the evidentialist's wager, where normative uncertainty can favor EDT. I'm also considering criticisms of EDT, particularly Lewis's view of it as managing the news and Joyce's focus on causal efficacy. My current focus is to ensure a balanced view of both the benefits and limitations of EDT.


**Elaborating EDT's Core**

I am clarifying how EDT assesses actions, including its treatment of dependencies and counterfactuals. I am working to identify the open questions from the source, and to articulate operational interpretations to resolve them. I need to be precise and to clearly separate the source's claims from my own additional assumptions and mathematical expansions. I'll maintain a substantive, mathematical essay format, aiming for conciseness and readability. I am also working to ensure the word count falls within the 2,400–3,000 word target.


**Formalizing Conditional Probabilities**

I'm now wrestling with the practical application of EDT, particularly regarding state-action partitioning. I'm focused on the difference between outcomes and states of the world and how they are used in the EDT formula. I'm working to formalize the connection, drawing inspiration from Savage and Jeffrey's frameworks. This includes addressing cases where actions are deemed impossible by the agent and standard conditional probability is undefined. The "measure-zero" problem leads me to consider epsilon-perturbations, primitive conditional probability spaces, and Popper functions, to allow operational interpretations.


**Clarifying EDT Limitations**

I am now focusing on contrasting EDT and causal models in scenarios with common-cause confounding, like the Smoking Gene example. I'm developing an illustrative extension to the EDT model to show the divergence between $P(O_j \mid A)$ and $P(A \mathrel{\Box{\rightarrow}} O_j)$ when using a Bayesian network. I'm also now reviewing implications for operationalizing policy evaluation and normative uncertainty.


**Formalizing Meta-Decisions**

I'm now working to express mathematically the expectation in multi-agent correlated reference classes, and to formalize the meta-decision or "wager" between EDT and CDT. Additionally, I am investigating how indexical updating interacts oddly with EDT in the context of the Sleeping Beauty problem. This includes clarifying Dutch books and what limitations persist in sequential decision problems.


**Developing the Core Framework**

I am now structuring the essay's foundation, contrasting EDT and CDT at a high level. My goal is to establish a robust mathematical framework for analyzing decision problems. I am expanding the Gibbard and Harper equations, mapping the outcome space to environmental states and actions. I'm introducing the divergence term to clarify the difference between the evidential and causal approach.


**Analyzing EDT Scenarios**

I'm now focusing on specific scenarios to illustrate EDT's application. I am generalizing Newcomb's Paradox and the Twin Prisoner's Dilemma mathematically, with specific numbers, extending the models to analyze different levels of prediction accuracy and correlation. I am working towards a more complete formalization of the scenarios, identifying the critical thresholds at which EDT and CDT diverge, and demonstrating the divergence through both.


**Addressing EDT's Critics**

I'm now diving into the "managing the news" critique of EDT, and Joyce's focus on causal efficacy, working through numerical examples to make the difference clearer. I am formulating a structural causal model with an unobserved common cause to illustrate the problem. The goal is to mathematically show how EDT, through conditional probability, can lead to different recommendations than CDT, using a specific medical diagnosis case. I'm focusing on why evidential reasoning might seem counterintuitive.


**Operationalizing Unfamiliar Problems**

I'm now identifying operational gaps and generating solutions. I'm focusing on the measure-zero problem, where actions with zero prior probability create issues for conditional probability. I'm exploring $\epsilon$-perturbations and Rényi-Popper spaces to address this. Additionally, I'm thinking about the algorithmic correlation problem, and the need to distinguish screening off from genuine dependencies. I'll need to explore how I can use soft-max or noisy execution to implement $\epsilon$-perturbations.


**Formalizing Meta-Rules**

I'm now formulating a modified conditioning rule, evaluating actions ($A$) given internal credences and desires ($I$). I am working to illustrate the distinction between transparent psychological confounding and structural correlations, like in Newcomb's problem, in which the predictor/twin correlates with the final act $A$, even with the addition of the agent's internal state. Then, I'm focusing on Sleeping Beauty, addressing the potential Dutch book vulnerabilities for "halfers," and developing a policy-level evaluation to diagnose sequential problems.


**Analyzing the Collective Action**

I'm now formulating a meta-utility function based on MacAskill et al. (2021) to clarify the evidentialist's wager. I'm focusing on the collective action problem with correlated agents. I'm working to show how even small normative credence in EDT can dominate in scenarios with a large correlation and group size. I will then be able to synthesize the procedure for applying EDT, and summarize the final philosophical standing.


```
