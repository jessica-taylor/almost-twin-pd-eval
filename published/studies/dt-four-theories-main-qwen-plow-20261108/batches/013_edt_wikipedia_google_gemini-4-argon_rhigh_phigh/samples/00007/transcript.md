# 013_edt_wikipedia_google_gemini-4-argon_rhigh_phigh / 00007

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/9607367c-b424-4dbd-9dee-00be005c1586/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/9607367c-b424-4dbd-9dee-00be005c1586/call_0/response.raw) · finish: `stop`

### Visible response

````text
# News Value and Rational Choice: The Mathematics and Philosophy of Evidential Decision Theory

When we deliberate about what to do, how should we evaluate the consequences of our choices? At first glance, the answer offered by classical expected utility theory seems straightforward: catalog the possible outcomes of each available action, weight the desirability of each outcome by its probability given the action, and choose the option with the largest sum. 

Yet beneath this seemingly innocent prescription lies a profound philosophical and mathematical fork in the road. When we ask for the "probability of an outcome given an action," do we mean the probability that the action will *causally bring about* that outcome, or do we mean the conditional probability that the outcome holds *given the evidence* that we perform the action?

**Evidential decision theory** (EDT) takes the latter path. As summarized by Arif Ahmed (2021), EDT holds that when a rational agent confronts a set of possible actions, she should select the action with the highest *news value*—that is, the action that would be indicative of the best outcome in expectation if one received the "news" that it had been taken. In Ahmed's memorable slogan, EDT instructs the deliberating agent to *"do what you most want to learn that you will do."*

This stands in sharp contrast to **causal decision theory** (CDT), which insists that rational agents should choose actions based on their capacity to causally produce good outcomes, regardless of what performing those actions might diagnostically reveal about the preexisting state of the world. While EDT and CDT issue identical recommendations in standard everyday gambles, their prescriptions diverge dramatically in problems involving predictors, correlated agents, and self-locating beliefs.

In this essay, we will develop the formal machinery of evidential decision theory, examine its behavior in canonical thought experiments, and provide an operational framework that allows a mathematically literate practitioner to apply EDT to unfamiliar decision problems. Where the foundational literature leaves operational questions open—such as how to handle zero-probability acts during deliberation, how to model confounding variables, or how to formalize multi-agent stakes—we will explicitly identify those gaps and construct rigorous mathematical extensions to resolve them.

---

## 1. The Formal Architecture of EDT

The modern mathematical distinction between evidential and causal expected utility was crystallized by Allan Gibbard and William Harper in their landmark 1976 paper, *Counterfactuals and Two Kinds of Expected Utility*. 

Suppose an agent faces a finite set of mutually exclusive and exhaustive candidate actions $\mathcal{A} = \{A_1, A_2, \dots, A_m\}$ and cares about a finite partition of possible outcomes $\mathcal{O} = \{O_1, O_2, \dots, O_n\}$. Each outcome $O_j$ is assigned a numerical desirability (or utility) $D(O_j) \in \mathbb{R}$, and the agent's epistemic state is represented by a probability measure $P$ defined over an algebra of propositions containing both $\mathcal{A}$ and $\mathcal{O}$.

As set out by Gibbard and Harper (1976), evidential decision theory evaluates an action $A \in \mathcal{A}$ by its conditional expected utility, which we denote by $V(A)$:

$$V(A) = \sum_{j} P(O_j \mid A) D(O_j)$$

Here, $P(O_j \mid A)$ is the standard Kolmogorov conditional probability of outcome $O_j$ given that action $A$ occurs:

$$P(O_j \mid A) = \frac{P(O_j \cap A)}{P(A)}$$

By contrast, causal decision theory replaces the conditional probability $P(O_j \mid A)$ with the probability of a counterfactual conditional. Writing $A \mathrel{\Box{\rightarrow}} O_j$ for the proposition *"if action $A$ were performed, outcome $O_j$ would occur,"* CDT evaluates $A$ according to its causal expected utility $U(A)$:

$$U(A) = \sum_{j} P(A \mathrel{\Box{\rightarrow}} O_j) D(O_j)$$

Because $P(O_j \mid A)$ and $P(A \mathrel{\Box{\rightarrow}} O_j)$ need not coincide, $V(A)$ and $U(A)$ represent genuinely distinct decision criteria.

### Bridging Outcomes and Background States (Operational Extension)

While the reference formulation in terms of outcomes $O_j$ is compact, applying EDT to novel problems is often much easier if we explicitly decompose outcomes into *actions* and *background states of nature*. Let us introduce this standard formal bridge as an operational tool.

Suppose the relevant features of the world outside the agent's immediate motor control are captured by a partition of mutually exclusive and exhaustive states of nature $\mathcal{S} = \{S_1, S_2, \dots, S_k\}$. Once a state $S_i \in \mathcal{S}$ and an action $A \in \mathcal{A}$ are both fixed, they jointly determine a specific outcome $O(A, S_i)$ with desirability $D(A, S_i)$. Assuming the states $S_i$ are causally independent of the agent's action—meaning that performing $A$ does not causally alter which state $S_i$ holds—the counterfactual probability of $S_i$ under intervention $A$ is simply its unconditional prior probability: $P(A \mathrel{\Box{\rightarrow}} S_i) = P(S_i)$. Under this partition, the EDT and CDT valuations take a particularly transparent form:

$$V(A) = \sum_{i=1}^{k} P(S_i \mid A) D(A, S_i) \quad \text{versus} \quad U(A) = \sum_{i=1}^{k} P(S_i) D(A, S_i)$$

This state-space formulation immediately explains why the reference article notes that EDT and CDT *"agree in many cases."* Specifically, we can state an exact mathematical equivalence condition:

> **The Coincidence Condition:** For any decision problem partitioned into causally action-independent states $\mathcal{S}$, EDT and CDT assign identical expected utilities to action $A$ if and only if the states $S_i$ are *evidentially independent* of $A$—or more generally, whenever the covariance between the likelihood ratio $\frac{P(S_i \mid A)}{P(S_i)}$ and the payoff $D(A, S_i)$ vanishes:
> $$\Delta(A) \equiv V(A) - U(A) = \sum_{i=1}^{k} \left[ P(S_i \mid A) - P(S_i) \right] D(A, S_i) = 0$$

When you bet on a roulette wheel or decide whether to carry an umbrella based on a weather forecast, your choice of action $A$ provides zero diagnostic information about the state of the wheel or the atmosphere: $P(S_i \mid A) = P(S_i)$. Consequently, $\Delta(A) = 0$, and evidential and causal decision theories walk hand in hand. They diverge precisely when $\Delta(A) \neq 0$—that is, when learning what you choose tells you something new about the state of the world.

### The Zero-Probability Deliberation Problem

Before examining specific paradoxes, a rigorous practitioner must confront a technical ambiguity left unspoken in the basic formula $V(A) = \sum_j P(O_j \mid A) D(O_j)$. By definition, $P(O_j \mid A) = P(O_j \cap A) / P(A)$ is well-defined in standard probability theory only if $P(A) > 0$. 

What happens if a deliberating agent is already certain about what she will do—or certain that a clearly inferior option $A_{\text{bad}}$ will not be chosen, assigning $P(A_{\text{bad}}) = 0$? If $P(A_{\text{bad}}) = 0$, its news value $V(A_{\text{bad}})$ becomes an undefined $0/0$ expression, paralyzing the formal comparison required to justify rejecting $A_{\text{bad}}$ in the first place.

To make EDT operationally complete, we must supplement the bare Gibbard–Harper equation with a regularity assumption regarding the agent's epistemic state during deliberation. Two mathematical resolutions are available:

1. **Deliberative Regularity (Strict Positivity):** We stipulate that for an action $A$ to belong to the set of genuinely open options $\mathcal{A}$ during active deliberation, the agent must assign it a strictly positive prior credence: $P(A) \in (0, 1)$ for all $A \in \mathcal{A}$. Once deliberation concludes, $P(A^*)$ may converge to $1$ for the chosen act $A^*$, at which point deliberation is over.
2. **Primitive Conditional Probability (Popper–Rényi Measures):** Alternatively, one can treat the two-place conditional probability function $P(\cdot \mid \cdot)$ as primitive rather than defining it as a ratio of unconditional probabilities, allowing $P(O_j \mid A)$ to remain well-defined even on conditioning events of measure zero.

In practical modeling, adopting **Deliberative Regularity** is the simplest operational rule: when setting up a joint probability table over $\mathcal{A} \times \mathcal{S}$, ensure every candidate action has non-zero probability mass before computing conditional expectations.

---

## 2. Canonical Thought Experiments: Predictors and Twins

To see how EDT operates when $P(S_i \mid A) \neq P(S_i)$, let us examine the two foundational thought experiments presented in the source text—Newcomb's paradox and the Twin Prisoner's Dilemma—and generalize their mathematics so they can be applied to arbitrary parameter regimes.

### Newcomb's Paradox

Introduced by physicist William Newcomb and analyzed extensively in the philosophical literature (Wolpert & Benford 2013; Ahmed 2021), Newcomb's paradox pits diagnostic news value directly against dominance reasoning.

An agent faces two boxes:
* **Box A** is transparent and visibly contains $\$1,000$.
* **Box B** is opaque and contains either $\$1,000,000$ or $\$0$.

The agent must choose between two actions: taking only Box B ($A_1$, "one-boxing"), or taking both Box A and Box B ($A_2$, "two-boxing"). Yesterday, a predictor with a $99\%$ accuracy rate predicted the agent's choice. If the predictor foresaw one-boxing ($A_1$), she placed $\$1,000,000$ in Box B. If she foresaw two-boxing ($A_2$), she left Box B empty. The agent knows this setup, does not know what prediction was made, and must now choose.

```
[Predictor's Assessment] ──(causes)──> [Contents of Box B: $1M or $0]
          │                                         │
   (99% correlation)                                ▼
          ▼                                  [Final Payoff O_j]
[Agent's Choice: A_1 or A_2] ──(causes)─────────────┘
```

Following the reference text, let us compute $V(A_1)$ and $V(A_2)$ assuming desirability scales linearly with dollar payoff ($D(\$x) = x$). Because the predictor is $99\%$ accurate, the conditional probabilities of Box B's contents given the agent's choice are $P(\text{1M in B} \mid A_1) = 0.99$ and $P(\text{nothing in B} \mid A_2) = 0.99$. Thus:

$$\begin{aligned}
V(\text{take only B}) &= P(\text{1M in box B} \mid \text{take only B}) \times \$1,000,000 + P(\text{nothing in box B} \mid \text{take only B}) \times \$0 \\
&= 0.99 \times \$1,000,000 + 0.01 \times \$0 = \$990,000 \\[6pt]
V(\text{take both boxes}) &= P(\text{1M in box B} \mid \text{take both boxes}) \times \$1,001,000 + P(\text{nothing in box B} \mid \text{take both boxes}) \times \$1,000 \\
&= 0.01 \times \$1,001,000 + 0.99 \times \$1,000 = \$11,000
\end{aligned}$$

Since $V(\text{take only B}) > V(\text{take both boxes})$, EDT unequivocally prescribes one-boxing. Receiving the news that you took only Box B is overwhelmingly good news: it is strong evidence that you are walking away a millionaire.

By contrast, CDT reasons that the predictor's action lies in the fixed past. Whatever is currently sitting in Box B—call its state $S_{\text{1M}}$ or $S_{0}$—will not change regardless of what you do now. Thus $P(A_1 \mathrel{\Box{\rightarrow}} S_{\text{1M}}) = P(A_2 \mathrel{\Box{\rightarrow}} S_{\text{1M}}) = P(S_{\text{1M}})$. Consequently, CDT calculates:

$$U(\text{take both boxes}) - U(\text{take only B}) = P(S_{\text{1M}})(\$1,001,000 - \$1,000,000) + P(S_0)(\$1,000 - \$0) = \$1,000 > 0$$

CDT recommends taking both boxes, guaranteeing $\$1,000$ more than one-boxing in every counterfactual world—yet predictably leaving the two-boxer with $\$1,000$ while the EDT one-boxer walks away with $\$1,000,000$.

#### Parametric Generalization of Newcomb's Problem
To apply EDT to Newcomb-like scenarios with less reliable predictors or varying stakes, let us generalize the source calculation. Suppose Box A contains $c > 0$, Box B contains $M > 0$ if one-boxing is predicted, and the predictor's diagnostic accuracy is $P(\text{1M} \mid A_1) = P(\text{0} \mid A_2) = p \in [0.5, 1]$. Then:

$$V(A_1) = pM, \qquad V(A_2) = (1 - p)(M + c) + pc = (1 - p)M + c$$

EDT recommends one-boxing ($V(A_1) > V(A_2)$) if and only if:

$$pM > (1 - p)M + c \iff p > \frac{1}{2} + \frac{c}{2M}$$

In the classic setup where $c = \$1,000$ and $M = \$1,000,000$, the critical threshold is $p^* = 0.5005$. As long as the agent's action gives even the slightest positive diagnostic signal above $50.05\%$ about the predictor's move, EDT favors leaving the $\$1,000$ behind.

### The Twin Prisoner's Dilemma

While Newcomb's paradox relies on a chronologically prior prediction, evidential dependencies arise just as naturally between simultaneous, causally isolated agents who share similar decision-making architectures.

Consider the **Twin Prisoner's Dilemma** (Greene & Levinstein 2020). Aomame and her psychological twin—an agent whose reasoning processes are exactly analogous to her own—are placed in separate, causally isolated rooms. Each must choose whether to Cooperate ($C$) or Defect ($D$). The individual payoffs to Aomame are summarized in the following matrix:

| Aomame \ Twin | Twin Cooperates ($C_T$) | Twin Defects ($D_T$) |
| :--- | :---: | :---: |
| **Aomame Cooperates ($C_A$)** | $\$5$ | $\$0$ |
| **Aomame Defects ($D_A$)** | $\$10$ | $\$1$ |

Assuming Aomame cares purely about her own financial payout, what should she do? From a causal standpoint, her choice cannot affect her twin's choice on the other side of the wall; whatever the twin does, defecting yields $\$10$ instead of $\$5$ (if the twin cooperates) or $\$1$ instead of $\$0$ (if the twin defects). Thus CDT prescribes defection, locking both twins into the dismal $(\$1, \$1)$ outcome.

EDT evaluates the situation differently. Because her twin's reasoning process mirrors her own, Aomame's choice is pristine evidence of her twin's choice: $P(C_T \mid C_A) = 1$ and $P(D_T \mid D_A) = 1$. As given in the reference article, the evidential expected utilities are:

$$\begin{aligned}
V(C_A) &= P(C_T \mid C_A) \times \$5 + P(D_T \mid C_A) \times \$0 = 1 \times \$5 + 0 \times \$0 = \$5 \\
V(D_A) &= P(C_T \mid D_A) \times \$10 + P(D_T \mid D_A) \times \$1 = 0 \times \$10 + 1 \times \$1 = \$1
\end{aligned}$$

Since $V(C_A) > V(D_A)$, EDT prescribes cooperation, allowing psychological twins to achieve the Pareto-superior $(\$5, \$5)$ outcome without communication or binding contracts.

#### Generalizing to Imperfectly Correlated Agents
In real-world applications—such as voting, public goods contributions, or algorithmic trading—other agents are rarely exact clones, though their choices remain statistically correlated with ours due to shared backgrounds, training data, or norms. Let us extend the source's Twin Prisoner's Dilemma to arbitrary correlation strengths.

Consider a standard symmetric Prisoner's Dilemma with payoffs $T > R > P > S$ (where in Aomame's case $T=10, R=5, P=1, S=0$). Suppose that given Aomame chooses action $X \in \{C, D\}$, the conditional probability that her counterpart also chooses $X$ is $q \in [0.5, 1]$. Then:

$$V(C_A) = qR + (1 - q)S, \qquad V(D_A) = (1 - q)T + qP$$

EDT prescribes cooperation whenever $V(C_A) > V(D_A)$, which simplifies to:

$$q > \frac{T - S}{(T - S) + (R - P)}$$

Plugging in Aomame's payoffs yields $q > \frac{10 - 0}{10 + 4} = \frac{5}{7} \approx 0.714$. Thus, Aomame does not need a perfect clone to justify cooperating under EDT; she merely needs her decision to be at least $71.4\%$ diagnostic of her counterpart's choice.

---

## 3. Confounding, Counterfactuals, and the "Managing the News" Critique

If EDT triumphs in Newcomb's paradox and the Twin Prisoner's Dilemma, why do so many decision theorists reject it in favor of CDT? 

The central philosophical objection is captured concisely in the reference text by David Lewis (1981) and James M. Joyce (1999). Lewis famously characterized EDT as promoting *"an irrational policy of managing the news,"* while Joyce argued:

> *"Rational agents choose acts on the basis of their causal efficacy, not their auspiciousness; they act to bring about good results even when doing so might betoken bad news."* (Joyce 1999, p. 146)

Because the reference article states these criticisms without detailing the formal structure of the counterexamples that motivate them, let us construct a concrete mathematical model of a **common-cause confounding problem** (often illustrated in the literature by medical or genetic "lesion" cases) to see exactly how this tension arises and how an operational EDT framework responds.

### A Mathematical Model of Confounding (Operational Illustration)

Suppose a pre-existing, unobservable genetic factor $G \in \{G_1, G_0\}$ acts as a common cause of two things:
1. It strongly predisposes an agent to enjoy and choose a benign habit $A_{\text{habit}}$ over abstaining $A_{\text{abstain}}$.
2. Independently of what the agent actually chooses to do, possessing $G_1$ causes a severe illness later in life (utility $-100$), whereas $G_0$ leaves the agent healthy (utility $0$).
3. Indulging in $A_{\text{habit}}$ provides a mild, direct causal pleasure worth $+1$ unit of utility in both states.

```
         [Unobserved Genetic Factor: G_1 or G_0]
               /                         \
    (correlates with)                  (causes)
             /                             \
            ▼                               ▼
[Action: A_habit vs. A_abstain]       [Health State: Ill (-100) vs. Well (0)]
            \                               /
       (+1 direct joy)               (base utility)
              \                           /
               ▼                         ▼
                 [Total Desirability D]
```

Suppose the agent's joint credences yield $P(G_1 \mid A_{\text{habit}}) = 0.80$ and $P(G_1 \mid A_{\text{abstain}}) = 0.10$, while the unconditional prior is $P(G_1) = 0.50$. Let us evaluate both actions under naive EDT and CDT:

$$\begin{aligned}
V(A_{\text{habit}}) &= P(G_1 \mid A_{\text{habit}})(-100 + 1) + P(G_0 \mid A_{\text{habit}})(0 + 1) = 0.80(-99) + 0.20(1) = -79.0 \\
V(A_{\text{abstain}}) &= P(G_1 \mid A_{\text{abstain}})(-100 + 0) + P(G_0 \mid A_{\text{abstain}})(0 + 0) = 0.10(-100) + 0.90(0) = -10.0
\end{aligned}$$

Meanwhile, because the gene $G$ is already fixed at birth, $P(A \mathrel{\Box{\rightarrow}} G_1) = P(G_1) = 0.50$ for both actions, so CDT computes:

$$U(A_{\text{habit}}) = 0.50(-99) + 0.50(1) = -49.0 > U(A_{\text{abstain}}) = 0.50(-100) + 0.50(0) = -50.0$$

Here we see the sharp bite of Lewis's and Joyce's objection. Abstaining does nothing to cure or prevent the genetic illness; it merely deprives the agent of $+1$ unit of harmless pleasure. Yet a naive application of EDT recommends $A_{\text{abstain}}$ ($-10.0 > -79.0$) because abstaining would be "good news" indicating that the agent lacks the gene $G_1$.

### Operational Interpretations: Screening Off vs. Strict Evidentialism

How should a practitioner applying EDT handle such cases? Because the reference article leaves this question open, we must carefully distinguish two operational approaches available in the decision-theoretic toolkit:

1. **Conditioning on Pre-Action Evidence (The "Screening Off" Interpretation):** Notice that if the genetic factor $G$ causes the action $A_{\text{habit}}$ only by first causing a conscious craving or inclination $I$ that the agent can introspect *prior* to acting, then the agent should first update her probability distribution $P(\cdot)$ on her observed inclination $I$. In probability theory, when $G \to I \to A$ forms a Markov chain, observing the intermediate variable $I$ **screens off** the action $A$ from the state $G$:
   $$P(G_1 \mid A, I) = P(G_1 \mid I)$$
   Once the probability measure $P_I(\cdot) \equiv P(\cdot \mid I)$ incorporates all introspectively accessible pre-choice evidence, the evidential correlation between the act and the gene vanishes, and EDT recommends $A_{\text{habit}}$ just as CDT does!
2. **Strict Evidentialism (Biting the Bullet):** What if $G$ influences the choice $A$ directly without any introspectible mediating cue $I$—or what if an ideal predictor in Newcomb's problem bypasses $I$ by simulating the agent's exact final choice? In that regime, screening off cannot eliminate the correlation without also destroying one-boxing in Newcomb's problem. A strict evidentialist (following Ahmed 2021) maintains that if an agent genuinely knows that people who perform $A_{\text{abstain}}$ remain healthy $90\%$ of the time while those who perform $A_{\text{habit}}$ fall ill $80\%$ of the time—even after accounting for every introspectible desire—then choosing $A_{\text{abstain}}$ is the rational way to align oneself with the survivors.

For practical modeling, the lesson is crucial: **before computing $V(A) = \sum_j P(O_j \mid A) D(O_j)$, always condition the probability measure $P$ on the full body of evidence $E$ available to the agent at the moment of choice.** Only correlations between $A$ and $O_j$ that survive conditioning on $E$ should enter the EDT valuation.

---

## 4. Diachronic Consistency and the Sleeping Beauty Problem

Beyond one-shot games against predictors or twins, EDT plays a fascinating and contested role in problems of **self-locating belief** and diachronic consistency—most notably the **Sleeping Beauty Problem**. 

As the reference article notes, EDT has been invoked in the Sleeping Beauty problem to rescue "halfers" from **Dutch book arguments** (sequences of bets that guarantee a net financial loss in every state of the world), though Vincent Conitzer (2015) demonstrates that halfers remain vulnerable to a modified Dutch book even after adopting EDT. Let us reconstruct the mathematical mechanics behind both claims so the reader can see how EDT operates across multiple decision points.

### The Setup and the Standard Halfer Dilemma

In the standard Sleeping Beauty problem, Beauty is put to sleep on Sunday. A fair coin is tossed:
* If it lands **Heads ($H$)**, she is awakened briefly on Monday, and then sleeps until the experiment ends on Wednesday.
* If it lands **Tails ($T$)**, she is awakened on Monday, given an amnesia-inducing drug that erases her memory of Monday's awakening, and awakened again on Tuesday.

Whenever she wakes up, she cannot tell whether it is Monday or Tuesday. What credence $P(H)$ should she assign to the coin having landed Heads upon waking? **Thirders** argue for $P(H) = 1/3$, whereas **Halfers** insist that because she learned no new non-indexical facts since Sunday, her credence must remain $P(H) = 1/2$ (and $P(T) = 1/2$).

Now suppose a bookie offers Beauty a bet every time she wakes up. How does her choice of decision theory affect which bets she accepts?

### Why EDT Protects Halfers Against Naive Dutch Books (Formal Reconstruction)

Suppose a CDT-using halfer wakes up and is offered a bet $B_{\text{Tails}}$ that costs $\$10$ and pays $\$25$ if the coin landed Tails (so net gain on Tails is $+\$15$, and net loss on Heads is $-\$10$). 

A **CDT halfer** reasons that her choice right now only causes a bet to be placed *today* (this single awakening). Since she assigns $P(H) = 1/2$ and $P(T) = 1/2$, her causal expected utility for accepting the bet today is:

$$U(\text{Accept}) = \frac{1}{2}(-\$10) + \frac{1}{2}(+\$15) = +\$2.50 > U(\text{Reject}) = \$0$$

So a CDT halfer accepts the bet upon waking. However, because the Monday and Tuesday awakenings under Tails are subjectively indistinguishable, she will accept the exact same bet on *both* Monday and Tuesday whenever the coin lands Tails! Her actual net payoff across the whole experiment is therefore:
* **If Heads:** She wakes on Monday and loses $-\$10$.
* **If Tails:** She wakes on Monday and Tuesday, winning $+\$15 + \$15 = +\$30$.

Knowing this, a clever bookie can pair this waking bet with an opposite Sunday bet (e.g., on Sunday, when $P(H)=1/2$, offering her $+\$12$ if Heads and $-\$20$ if Tails, which has positive Sunday expectation $\frac{1}{2}(12) + \frac{1}{2}(-20) = -\$4$—or rather, $+\$20$ if Heads and $-\$18$ if Tails, which has positive Sunday expectation $+\$1$). Combining the Sunday bet ($+\$20$ on $H$, $-\$18$ on $T$) with selling the waking bet (say she bets *against* Tails upon waking, paying $\$15$ on $T$ per awakening to gain $\$10$ on $H$), the CDT halfer suffers a guaranteed loss on both Heads ($20 + 10 = +30$ vs. if reversed) — let us write the exact Dutch Book cleanly:
* Suppose upon waking, the CDT halfer is offered a bet *on Heads* ($A_{\text{bet}}$): she wins $+\$12$ if $H$, and loses $-\$10$ if $T$. Since $P(H)=1/2$, $U(A_{\text{bet}}) = \frac{1}{2}(12) + \frac{1}{2}(-10) = +\$1 > 0$, so she accepts.
* Yet if $T$ occurred, she wakes *twice* and accepts the bet *twice*, losing $-\$10 - \$10 = -\$20$ in total, whereas if $H$ occurred, she wakes once and wins $+\$12$.
* If on Sunday the bookie also offers her a bet on Tails that loses $-\$15$ if $H$ and wins $+\$17$ if $T$ (Sunday expectation $\frac{1}{2}(-15) + \frac{1}{2}(17) = +\$1 > 0$), she accepts both! Her combined net payoff is $\$12 - \$15 = -\$3$ on Heads, and $-\$20 + \$17 = -\$3$ on Tails—a strict Dutch Book!

Why does adopting **EDT** block this classic Dutch Book? Because for an EDT agent, the Monday awakening and the Tuesday awakening under Tails are **psychological twins**! When Beauty deliberates upon waking whether to accept $A_{\text{bet}}$, she recognizes that accepting the bet *now* is conclusive evidence ($P = 1$) that she accepts the bet *at every subjectively identical awakening*. Thus, conditional on accepting $A_{\text{bet}}$, the outcome under Tails is not $-\$10$, but the double loss $-\$20$:

$$V(A_{\text{bet}}) = P(H \mid A_{\text{bet}})(+\$12) + P(T \mid A_{\text{bet}})(-\$20) = \frac{1}{2}(+\$12) + \frac{1}{2}(-\$20) = -\$4 < V(\text{Reject}) = \$0$$

By accounting for the evidential correlation between her present self and her other waking self, the EDT halfer rejects $A_{\text{bet}}$ and escapes the standard diachronic Dutch Book.

### Conitzer's Dutch Book Against EDT Halfers

Why, then, does Conitzer (2015) conclude that EDT halfers can *still* be Dutch-booked? The vulnerability re-emerges as soon as the bookie breaks the informational symmetry between the awakenings—or manipulates the conditional probabilities across states—so that the agent's choices across awakenings are no longer transparently coupled as identical twins, or by offering bets contingent on centered propositions (such as *"it is currently Monday"*) where halfer credences ($P(H)=1/2$, split across Monday and Tuesday) create an inconsistency between evidential expected value upon waking and prior expected value on Sunday. 

Specifically, if an EDT halfer must evaluate bets whose payoffs depend not merely on the coin toss $\{H, T\}$ but on the current day $\{ \text{Mon}, \text{Tue} \}$, her current choice on Monday is only correlated with her Tuesday choice if the two states remain epistemically indistinguishable. By structuring bets across distinguishable or asymmetric epistemic partitions, a bookie can still extract a sure loss across the experiment. The broader mathematical lesson for EDT practitioners is that evidential twin-coupling only shields an agent against exploitation when the correlated decision nodes share the exact same informational state.

---

## 5. Normative Uncertainty and the Evidentialist's Wager

Suppose you have studied the arguments for both EDT and CDT and remain philosophically torn. Perhaps, moved by Lewis's and Joyce's causal intuitions, you assign a fairly low probability—say, $10\%$—to EDT being the normatively correct theory of rationality, and $90\%$ to CDT. How should you act in the face of this *decision-theoretic uncertainty*?

As highlighted in the reference text, William MacAskill, Aron Vallinder, Caspar Österheld, Carl Shulman, and Johannes Treutlein (2021) advance a striking argument known as **The Evidentialist's Wager**: *even if one puts much lower credence in EDT than in CDT, it can be rational to act as if EDT were true, because EDT's stakes are often orders of magnitude higher than CDT's.*

Let us construct a formal mathematical model of this wager to see why the stakes of EDT scale with the number of correlated decision-makers.

### Formalizing the Wager (Mathematical Extension)

Consider a large-scale collective action problem—such as reducing global catastrophic risk, voting in an election, or curbing carbon emissions—involving $N$ symmetric, like-minded agents. Each agent $i \in \{1, \dots, N\}$ can either choose an altruistic act $A_{\text{coop}}$ at a personal causal cost of $c > 0$, or defect $A_{\text{def}}$ at cost $0$. Every agent who chooses $A_{\text{coop}}$ causally generates a public benefit $b > 0$ shared by the world. Crucially, suppose an individual's single contribution fails to cover its personal cost ($b < c$), so for any isolated actor, $b - c < 0$.

However, suppose that if one agent chooses $A_{\text{coop}}$, this is diagnostic evidence that on average a fraction $\alpha \in (0, 1]$ of the other $N - 1$ correlated agents also choose $A_{\text{coop}}$. Let us compute the expected net value of choosing $A_{\text{coop}}$ over $A_{\text{def}}$ according to CDT and EDT:

1. **Under CDT:** Your action only causally controls your own contribution ($+b - c$) and has zero causal effect on the other $N - 1$ agents. Thus, the net causal gain of cooperating is negative:
   $$\Delta U = U(A_{\text{coop}}) - U(A_{\text{def}}) = b - c < 0$$
   If you follow CDT instead of EDT (by choosing $A_{\text{def}}$), the stake at risk according to CDT is simply $c - b$.

2. **Under EDT:** Choosing $A_{\text{coop}}$ is news not only that you contribute $b - c$, but that $\alpha(N - 1)$ other correlated agents also contribute $b$ each! Thus, the net evidential gain of cooperating is:
   $$\Delta V = V(A_{\text{coop}}) - V(A_{\text{def}}) = (b - c) + \alpha(N - 1)b$$

Now suppose you have normative credence $w_{\text{EDT}} \in (0, 1)$ in EDT and $w_{\text{CDT}} = 1 - w_{\text{EDT}}$ in CDT. Under a standard expected-value meta-rule for normative uncertainty, you should choose $A_{\text{coop}}$ whenever the credence-weighted net value is positive:

$$w_{\text{EDT}} \Delta V + (1 - w_{\text{EDT}}) \Delta U > 0 \iff w_{\text{EDT}} \left[ (b - c) + \alpha(N - 1)b \right] + (1 - w_{\text{EDT}})(b - c) > 0$$

Simplifying this inequality yields a remarkably clean threshold for the minimum credence $w_{\text{EDT}}$ required to act like an evidential decision theorist:

$$w_{\text{EDT}} > \frac{c - b}{\alpha(N - 1)b}$$

Consider what happens when the population of correlated decision-makers $N$ is large. Even if $c = 10$ and $b = 1$ (so your isolated action loses $9$ units of value), if there are $N = 10,001$ correlated agents with correlation $\alpha = 0.10$, the threshold is:

$$w_{\text{EDT}} > \frac{10 - 1}{0.10 \times 10,000 \times 1} = \frac{9}{1,000} = 0.009$$

As long as you assign at least a $0.9\%$ chance to EDT being the right decision theory, the massive evidential stakes across the $10,000$ correlated agents swamp CDT's local cost, compelling you to cooperate!

---

## 6. A Practical Protocol for Applying EDT to Unfamiliar Cases

To synthesize our theoretical analysis into a usable tool, here is a step-by-step mathematical protocol for applying Evidential Decision Theory to any novel decision problem:

1. **Specify the Action and State Partitions:** List the mutually exclusive and exhaustive candidate actions $\mathcal{A} = \{A_1, \dots, A_m\}$ and the relevant background states of the world $\mathcal{S} = \{S_1, \dots, S_k\}$ (which may include the choices of predictors, psychological twins, or other correlated agents).
2. **Condition on Pre-Choice Evidence ($E$):** Identify all information $E$ available prior to the decision (including introspectible desires, physical cues, or past observations) and update the prior distribution to $P_E(\cdot) = P(\cdot \mid E)$. This eliminates spurious confounding that can be screened off prior to action.
3. **Verify Deliberative Regularity:** Ensure that every genuinely available option satisfies $P_E(A_r) > 0$.
4. **Determine Diagnostic Likelihoods:** For each action $A_r \in \mathcal{A}$ and state $S_i \in \mathcal{S}$, determine the conditional probability $P_E(S_i \mid A_r)$. Ask: *"If I were handed a newspaper report from five minutes in the future stating that I chose $A_r$, what probability would I assign to state $S_i$ holding?"*
   * If $S_i$ involves a predictor or correlated twin, incorporate the predictor's accuracy $p$ or correlation $q$.
   * If $S_i$ involves future or parallel copies of yourself in identical epistemic states (as in Sleeping Beauty), bind their actions to match $A_r$ with probability $1$.
5. **Compute News Value and Maximize:** Map each pair $(A_r, S_i)$ to its resulting outcome $O(A_r, S_i)$ and desirability $D(A_r, S_i)$, and select the action $A^*$ that maximizes:
   $$V(A_r) = \sum_{i=1}^{k} P_E(S_i \mid A_r) D(A_r, S_i)$$

---

## 7. Conclusion

Evidential decision theory offers a mathematically austere yet philosophically radical vision of rational agency. By grounding expected utility purely in conditional probability, $V(A) = \sum_j P(O_j \mid A) D(O_j)$, EDT dispenses with the metaphysical apparatus of counterfactual worlds ($A \mathrel{\Box{\rightarrow}} O_j$) required by causal decision theory. 

As we have seen, this shift in formalism transforms how an agent interacts with a world that anticipates, mirrors, or correlates with her choices. In Newcomb's paradox and the Twin Prisoner's Dilemma, maximizing news value enables one-boxers to walk away rich and isolated twins to achieve mutual cooperation where causalists defect into poverty. At the same time, the debate sparked by Lewis, Joyce, and Conitzer reminds us that treating actions as diagnostic signals requires immense care when disentangling genuine agency from background confounding and diachronic shifts in information. Whether one embraces EDT as the true standard of rationality or engages with it via the Evidentialist's Wager, understanding the calculus of news value remains indispensable to modern decision theory.

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
````

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Target Audience**

I'm now zeroing in on defining the target audience's background. I believe I need to craft the explanations with the assumption they have a solid grasp of mathematical concepts but might not be familiar with EDT. I'm focusing on striking a balance between rigorous explanation and reader accessibility. This involves considering which examples will work best.


**Clarifying Key Distinctions**

I'm presently focusing on clearly differentiating EDT from Causal Decision Theory (CDT). I'm emphasizing that EDT prioritizes actions with the highest news value, contrasting this with CDT's causal approach. I'm also delving into the formalism of Gibbard & Harper (1976), particularly the maximization of conditional expected utility. I plan to derive clear explanations for experts in the field.


**Analyzing Decision Paradigms**

I'm now diving into the core distinction: EDT's focus on maximizing the expected value, given the observed outcomes of an action, versus CDT's counterfactual approach. I am concentrating on the contrast of these two approaches. I'm currently using Newcomb's Paradox and the Twin Prisoner's Dilemma to highlight how EDT diverges from CDT's causal thinking. Specifically, the differing recommendations in these thought experiments reveal the fundamental disparity in their core principles.


**Evaluating EDT Strategies**

I'm now examining several key arguments for and against Evidential Decision Theory (EDT). I'm currently assessing EDT's implications in the Twin Prisoner's Dilemma, using the Sleeping Beauty Problem and the Evidentialist's Wager as supporting arguments, and assessing criticisms from Lewis and Joyce. I am exploring the impact of acting as if EDT is true even with low credence.


**Bridging Formalisms of EDT**

I'm working on connecting the outcome-focused view of EDT to the state-action partition framework. I need to make the math rigorous. It's crucial to explicitly show this transition for broader applicability. I'm focusing on handling situations where $P(A) = 0$, a crucial challenge for EDT. This involves addressing the operational gaps in the theory, particularly during deliberation before a decision is made.


**Operationalizing EDT Principles**

I'm now formulating operational criteria for Evidential Decision Theory, addressing the epistemic status of $P(A)$. I'm considering requiring strictly positive credences, a "deliberative openness" condition, or utilizing primitive conditional probability. I'm exploring how EDT handles situations like managing the news, specifically in cases with confounding variables like the Smoking Gene. I'm aiming to formalize the mathematical conditions under which EDT and CDT align and building a model to address Lewis and Joyce's critiques.


**Extending EDT Frameworks**

I'm now extending EDT to include evidentially correlated states, specifically addressing pre-choice evidence and the "Tick Defense," while clearly labeling this as an extension. I'm building a mathematical model for the Evidentialist's Wager, which will clarify the stakes argument by MacAskill et al. I'm also mathematically reconstructing how action-conditioning interacts with self-locating beliefs in the Sleeping Beauty problem.


**Constructing Decision Frameworks**

I'm now outlining a formal decision-theoretic framework, contrasting EDT's evidential approach with CDT's causal approach, using the tuple $(\mathcal{A}, \mathcal{S}, \mathcal{O}, P, D)$. I'm focusing on defining the terms: actions, states, outcomes, probabilities, and desirabilities. I'm aiming to operationalize EDT's news-value maximizing principle and formalize the distinction between conditional probability and counterfactual probability to highlight the differences between the two theories. I'm clarifying how each theory uses these components to arrive at an optimal action.


**Analyzing Divergences Formally**

I'm working on formalizing how actions, states, and outcomes interact mathematically, focusing on reformulating $V(A)$ over a partition of background states. I'm deriving the exact mathematical condition for when EDT and CDT are equivalent, highlighting why they usually agree and defining divergence $\Delta(A)$. I'm addressing the $P(A) = 0$ boundary problem for operationalizing EDT. I'm now exploring Newcomb's Paradox and generalizing it parametrically.


**Formalizing Dilemmas**

I'm now generalizing the Twin Prisoner's Dilemma to incorporate imperfect psychological similarity, using correlation parameters to allow for EDT applications in diverse scenarios. I'm focusing on the Aomame calculation, considering a common-cause confounding scenario and constructing a formal example to address Lewis and Joyce's criticisms. My aim is to clearly illustrate the divergence of $P(O_j \mid A)$ from $P(A \mathrel{\Box\rightarrow} O_j)$.


**Clarifying Evidential Pitfalls**

I am now delving into the application of the EDT formula when actions are symptoms of pre-existing states, focusing on two operational interpretations: strict evidentialism versus conditioning on complete pre-action evidence. I'm noting the limitations of screening off in Newcomb-like scenarios. I'm also addressing diachronic consistency and the Sleeping Beauty Problem. I'm mathematically reconstructing Dutch book arguments in correlated waking states, demonstrating EDT's evidential linkage and exploring how asymmetric information can break the protection it offers.


**Synthesizing Meta-Decision Rules**

I am now focusing on the implications of the Evidentialist's Wager, working to build a mathematical model of normative uncertainty. I'm exploring how a meta-decision rule, which maximizes expected value across theories, can result in "acting as if EDT were true," especially when multiple correlated agents are involved. I'm also planning a step-by-step algorithm to apply EDT to novel problems. I'm reviewing the tone, math, and attribution and finalizing the list of references.


**Defining Extensions Precisely**

I'm now focusing on clear signposting. I'll explicitly differentiate between sourced principles and my extensions with parametric generalizations. I am now working on the Newcomb threshold, ensuring the math for the equations are crystal clear and error-free. I'll maintain a word count tracker, aiming for 2400-3000 words. My aim is to make the explanations thorough and readable.


**Refining Mathematical Models**

I'm now diving into the math behind the one-box/two-box decision in Newcomb's Paradox and verifying the Twin Prisoner's Dilemma thresholds. I'm checking that the values of each state are consistent with my source. I'm focusing on clarifying and verifying the implications of the correlation parameters in the Prisoner's Dilemma model for different scenarios.


**Verifying Article Length**

I'm now keeping a close eye on the word count as I draft, aiming for the target range of 2600-2800 words. I am also working to ensure each section has enough analytical depth. I'm carefully verifying all the citations for accuracy. I'm focusing on incorporating analytical depth and verified source citations.


```
