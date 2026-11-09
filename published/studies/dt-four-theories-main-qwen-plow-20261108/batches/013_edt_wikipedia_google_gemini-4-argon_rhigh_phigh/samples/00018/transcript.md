# 013_edt_wikipedia_google_gemini-4-argon_rhigh_phigh / 00018

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/ff958b0c-9499-4184-8c4f-4672bca0f894/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/ff958b0c-9499-4184-8c4f-4672bca0f894/call_0/response.raw) · finish: `stop`

### Visible response

````text
# News Value and Rational Choice: The Mathematics and Philosophy of Evidential Decision Theory

When a rational agent stands at a crossroads and deliberates between competing courses of action, what question should guide her choice? According to one dominant tradition in philosophy and economics, the agent should ask a causal question: *What outcome will my action bring about?* On this view, an action is an intervention upon the world, and rational choice consists in selecting the lever whose causal downstream effects are most desirable.

Yet there is a rival tradition that frames the problem of deliberation in purely informational terms. Suppose you are considering a set of possible actions, and an oracle offers to whisper to you which action you are ultimately going to take. Learning that you will perform action $A$ rather than action $B$ is a piece of news about the world—one that prompts you to update your beliefs about everything correlated with your choice. According to **Evidential Decision Theory** (EDT), rational agency consists in choosing the action that carries the best news. As the philosopher Arif Ahmed summarizes the principle in the reference literature, EDT instructs the decision-maker to select the action with the highest *news value*—in short, to "do what you most want to learn that you will do" (Ahmed 2021, p. 7).

While causal and evidential reasoning yield identical prescriptions in ordinary environments where an agent's choices are statistically independent of preexisting states of the world, they diverge sharply in scenarios involving predictors, correlated agents, or common causes. This essay provides a rigorous mathematical account of Evidential Decision Theory, drawing its core definitions and benchmark thought experiments from the reference text while developing explicit operational extensions to resolve questions the introductory literature leaves open. Our goal is to equip a mathematically literate reader with both the philosophical foundations of EDT and a self-contained formal procedure capable of resolving unfamiliar decision problems.

---

## 1. The Formal Architecture: Conditional vs. Counterfactual Expectation

The mathematical foundation of modern decision theory rests on expected utility maximization. In their landmark 1976 paper, Allan Gibbard and William Harper demonstrated that the intuitive notion of "expected utility" bifurcates into two distinct formal quantities depending on how one measures the probability of an outcome given an action (Gibbard & Harper 1976).

Let $\mathcal{A} = \{A_1, A_2, \dots, A_m\}$ be a finite set of mutually exclusive and exhaustively available actions, and let $\mathcal{O} = \{O_1, O_2, \dots, O_k\}$ be a finite partition of possible outcomes. The agent's preferences over outcomes are encoded by a real-valued desirability (or utility) function $D: \mathcal{O} \to \mathbb{R}$. 

As presented in the reference article, Gibbard and Harper define the **evidential expected utility** (or news value) $V(A)$ of an action $A \in \mathcal{A}$ using standard conditional probabilities:

$$V(A) = \sum_{j} P(O_j \mid A) D(O_j),$$

where $P(O_j \mid A)$ denotes the conditional probability that outcome $O_j$ occurs given the proposition that action $A$ is performed. An evidential decision theorist evaluates all available actions in $\mathcal{A}$ and prescribes selecting an action $A^*$ that maximizes $V$:

$$A^* \in \arg\max_{A \in \mathcal{A}} V(A).$$

By contrast, **Causal Decision Theory** (CDT) replaces the conditional probability $P(O_j \mid A)$ with the probability of a subjunctive conditional (or counterfactual). Using the box-arrow operator $\mathrel{\Box{\rightarrow}}$ to read "if it were the case that $\dots$, then it would be the case that $\dots$," the reference text gives the causal expected utility $U(A)$ as:

$$U(A) = \sum_{j} P(A \mathrel{\Box{\rightarrow}} O_j) D(O_j),$$

where $P(A \mathrel{\Box{\rightarrow}} O_j)$ measures the probability of outcome $O_j$ in the counterfactual situation in which action $A$ is performed.

### Operational Extension: Bridging Outcomes and States of the World

While the reference article states the Gibbard–Harper formulas in terms of outcomes $O_j$, applying these equations to concrete problems—including the thought experiments in the reference text itself—requires an additional structural step that we now make explicit. In practice, an outcome $O_j$ is rarely an atomic event; rather, it is determined jointly by the agent's action $A$ and an underlying **state of the world** $S_i$ (such as the contents of a sealed box or the choice of another player).

To operationalize EDT for general decision problems, let us introduce a finite partition of states of nature $\mathcal{S} = \{S_1, S_2, \dots, S_n\}$ defined on a common probability space $(\Omega, \mathcal{F}, P)$ alongside the action events $\mathcal{A}$. Each pair $(A, S_i)$ uniquely specifies an outcome $O(A, S_i)$ with desirability $D(A, S_i)$. Because the states $S_i$ partition the sample space $\Omega$, the evidential value $V(A)$ can be rewritten as:

$$V(A) = \sum_{i=1}^{n} P(S_i \mid A) D(A, S_i) = \sum_{i=1}^{n} \frac{P(S_i \cap A)}{P(A)} D(A, S_i).$$

In this state-space representation, the divergence between EDT and CDT becomes transparent. Suppose the states $S_i$ represent causally independent background conditions—for instance, events that occurred in the past or events occurring in a causally isolated room. Because performing $A$ cannot causally alter such states, the counterfactual probability of $S_i$ under an intervention $A$ is simply the unconditional prior probability $P(S_i)$:

$$P(A \mathrel{\Box{\rightarrow}} S_i) = P(S_i) \quad \text{(for causally independent states } S_i\text{)}.$$

Consequently, for causally independent states, the CDT utility reduces to:

$$U(A) = \sum_{i=1}^{n} P(S_i) D(A, S_i).$$

Whenever $A$ and $S_i$ are statistically independent—meaning $P(S_i \mid A) = P(S_i)$ for all $i$ and $A$—we have $V(A) = U(A)$, and EDT and CDT issue identical recommendations. The philosophical battleground between the two theories lies precisely in regimes where **causal independence coexists with statistical dependence**:

$$P(A \mathrel{\Box{\rightarrow}} S_i) = P(S_i) \neq P(S_i \mid A).$$

In such regimes, performing $A$ does not *cause* $S_i$ to occur, yet learning that you have performed $A$ provides strong statistical evidence that $S_i$ has already occurred or will occur.

---

## 2. Canonical Thought Experiments: Predictors and Twins

The reference article highlights two classic thought experiments where statistical and causal dependence pull apart: Newcomb's paradox and the Twin Prisoner's Dilemma. Let us examine how the formal machinery operates in both cases, first reproducing the reference calculations and then generalizing their parameters.

### 2.1 Newcomb's Paradox

In Newcomb's paradox (Wolpert & Benford 2013; Ahmed 2021), an agent faces two boxes: a transparent Box A that visibly contains $\$1,000$, and an opaque Box B whose contents were already set prior to the game by a highly reliable predictor. The agent has two available actions:
* $A_1$: Take only Box B ("one-boxing").
* $A_2$: Take both Box A and Box B ("two-boxing").

The relevant state space $\mathcal{S} = \{S_1, S_2\}$ tracks the predictor's prior action:
* $S_1$: The predictor predicted one-boxing ($A_1$) and placed $\$1,000,000$ in Box B.
* $S_2$: The predictor predicted two-boxing ($A_2$) and placed $\$0$ in Box B.

Following the reference text, suppose desirability is linear in dollars ($D(\$x) = x$) and the predictor is $99\%$ accurate, which the text interprets directly through the conditional probabilities $P(S_1 \mid A_1) = 0.99$ and $P(S_2 \mid A_2) = 0.99$ (so that $P(S_2 \mid A_1) = 0.01$ and $P(S_1 \mid A_2) = 0.01$). The payoff matrix $D(A_k, S_i)$ is:

| Action \ State | $S_1$ ($\$1\text{M}$ in Box B) | $S_2$ ($\$0$ in Box B) |
| :--- | :---: | :---: |
| **$A_1$ (Take only Box B)** | $\$1,000,000$ | $\$0$ |
| **$A_2$ (Take both boxes)** | $\$1,001,000$ | $\$1,000$ |

Applying the EDT expectation formula yields:

$$\begin{aligned}
V(A_1) &= P(S_1 \mid A_1) \times \$1,000,000 + P(S_2 \mid A_1) \times \$0 \\
&= 0.99 \times \$1,000,000 + 0.01 \times \$0 = \$990,000, \\[6pt]
V(A_2) &= P(S_1 \mid A_2) \times \$1,001,000 + P(S_2 \mid A_2) \times \$1,000 \\
&= 0.01 \times \$1,001,000 + 0.99 \times \$1,000 = \$11,000.
\end{aligned}$$

Because $V(A_1) = \$990,000 > V(A_2) = \$11,000$, EDT unambiguously prescribes taking only Box B. Choosing $A_1$ is overwhelmingly strong evidence that the predictor foresaw this choice and stocked Box B with a million dollars.

Notice why CDT reaches the opposite verdict. Because the money is already sitting in the boxes before the agent chooses, the state of Box B is causally independent of the agent's act: $P(A_k \mathrel{\Box{\rightarrow}} S_i) = P(S_i)$. Letting $q = P(S_1)$ denote the unconditional probability that Box B contains $\$1,000,000$, CDT computes:

$$U(A_2) = q(\$1,001,000) + (1-q)(\$1,000) = q(\$1,000,000) + \$1,000 = U(A_1) + \$1,000.$$

For every possible prior $q \in [0,1]$, $U(A_2) > U(A_1)$ by dominance. CDT recommends taking both boxes, whereas EDT recommends taking only one.

*(Additional generalization beyond the source text)*: We can easily generalize the EDT threshold for any Newcomb-type problem. Suppose Box A contains $a > 0$, Box B contains $b > a$ if $A_1$ was predicted, and the diagnostic predictive reliability is $P(S_1 \mid A_1) = p_1$ and $P(S_2 \mid A_2) = p_2$. Then:

$$V(A_1) > V(A_2) \iff p_1 b > (1 - p_2)(b + a) + p_2 a \iff (p_1 + p_2 - 1)b > a.$$

Thus, an evidential decision-maker one-boxes whenever the sum of predictive reliabilities exceeds $1 + a/b$.

### 2.2 The Twin Prisoner's Dilemma

Our second benchmark from the reference text removes the science-fiction device of a temporal predictor and replaces it with symmetric rational agency (Greene & Levinstein 2020). Aomame and her psychological twin—an agent whose reasoning processes are identical to her own—are placed in separate rooms without communication. Each must choose whether to Cooperate ($C$) or Defect ($D$). If both cooperate, each receives $\$5$; if both defect, each receives $\$1$; if one defects while the other cooperates, the defector receives $\$10$ and the cooperator receives $\$0$. Aomame cares strictly about her own monetary payoff.

Here, the state space is the twin's action: $\mathcal{S} = \{\text{Twin } C, \text{Twin } D\}$. Because the twin's cognitive architecture mirrors Aomame's, Aomame's choice is perfectly diagnostic of her twin's choice:

$$P(\text{Twin } C \mid \text{Aomame } C) = 1, \qquad P(\text{Twin } D \mid \text{Aomame } D) = 1.$$

Evaluating Aomame's evidential expected utilities from the reference text gives:

$$\begin{aligned}
V(\text{Aomame } C) &= P(\text{Twin } C \mid \text{Aomame } C) \times \$5 + P(\text{Twin } D \mid \text{Aomame } C) \times \$0 \\
&= 1 \times \$5 + 0 \times \$0 = \$5, \\[6pt]
V(\text{Aomame } D) &= P(\text{Twin } C \mid \text{Aomame } D) \times \$10 + P(\text{Twin } D \mid \text{Aomame } D) \times \$1 \\
&= 0 \times \$10 + 1 \times \$1 = \$1.
\end{aligned}$$

Since $V(\text{Aomame } C) > V(\text{Aomame } D)$, EDT instructs Aomame to cooperate. By contrast, because the rooms are causally isolated, Aomame's choice has zero causal effect on her twin's choice. A causal decision theorist treats the twin's move as fixed and defects to secure an extra $\$5$ (if the twin cooperates) or an extra $\$1$ (if the twin defects), locking both twins into the Pareto-inferior $(\$1, \$1)$ outcome.

*(Additional generalization beyond the source text)*: In real-world strategic interactions, an opponent is rarely a perfect psychological clone. Suppose instead that an agent faces a correlated peer in a general Prisoner's Dilemma with payoffs $T > R > P > S$ (where $T=\$10, R=\$5, P=\$1, S=\$0$ above), and her action is partially correlated with her peer's action such that $P(\text{Peer } C \mid \text{Self } C) = r_C$ and $P(\text{Peer } D \mid \text{Self } D) = r_D$. Under EDT, cooperation is strictly preferred whenever:

$$r_C R + (1 - r_C) S > (1 - r_D) T + r_D P.$$

This inequality provides an immediate operational criterion for cooperation among partially correlated agents in symmetric games.

---

## 3. Open Questions and Operationalizing EDT for Unfamiliar Cases

While the reference article establishes the core equations and canonical examples of EDT, a practitioner attempting to apply the theory to a brand-new problem will immediately encounter three foundational questions that the brief reference overview leaves open:

1. **The Generative Prior and Measure-Zero Problem**: Where do the conditional probabilities $P(O_j \mid A)$ come from when a problem is specified in terms of causal mechanisms, and how is $P(O_j \mid A)$ defined if a rational agent becomes certain she will *not* take a suboptimal action (making $P(A) = 0$)?
2. **Causal Confounding and "Managing the News"**: How does EDT respond to criticisms by David Lewis (1981) and James M. Joyce (1999) regarding common causes where an action merely serves as a symptom of a preexisting condition?
3. **Diachronic Consistency and Self-Locating Belief**: How does EDT evaluate multi-stage policies or problems with imperfect recall, such as the Sleeping Beauty problem analyzed by Conitzer (2015)?

In this section, we examine each uncertainty and develop a rigorous operational framework—clearly distinguishing our formal proposals from the claims of the source text—to make EDT fully executable across unfamiliar domains.

### 3.1 Bayes' Rule, Base Rates, and the Measure-Zero Boundary

In the reference article's presentation of Newcomb's paradox, the predictor's $99\%$ accuracy is translated directly into the diagnostic conditional probabilities $P(S_1 \mid A_1) = 0.99$ and $P(S_2 \mid A_2) = 0.99$. In many unfamiliar decision problems, however, an environment is specified *generatively* rather than diagnostically: we are told the probability $P(S_i \mid A_k)$ when $A_k$ precedes $S_i$, or we are told the likelihood $P(\text{Signal} \mid \text{State})$ of a mechanism, along with prior base rates.

*(Operational proposal)*: To avoid fallacies of transposed conditionals when setting up a novel EDT problem, an analyst must distinguish two ways a predictor or correlated mechanism can be specified:
* **Forwards (Act-to-Prediction) Specification**: If the predictor's accuracy is defined as the probability that the predictor correctly anticipates the agent's actual choice—i.e., $P(S_k \mid A_k) = 1 - \varepsilon$—then the conditional probabilities needed for $V(A_k)$ are given directly.
* **Backwards (State-to-Act) Specification**: Suppose instead we are told that *given* state $S_k$, the agent chooses $A_k$ with probability $P(A_k \mid S_k) = 1 - \varepsilon$, and we are given a prior probability $P(S_1) = \pi \in (0,1)$. Then $P(S_k \mid A_k)$ is **not** automatically equal to $1 - \varepsilon$. Instead, the analyst must apply Bayes' theorem:

$$P(S_1 \mid A_1) = \frac{P(A_1 \mid S_1) P(S_1)}{P(A_1 \mid S_1) P(S_1) + P(A_1 \mid S_2) P(S_2)} = \frac{(1 - \varepsilon)\pi}{(1 - \varepsilon)\pi + \varepsilon(1 - \pi)}.$$

Notice a crucial boundary phenomenon in this formula: as $\pi \to 0$ (meaning the agent is almost certain prior to deliberating that she will two-box, so $P(A_1) \to 0$), $P(S_1 \mid A_1)$ drops toward $0$ for any fixed $\varepsilon > 0$. More generally, by Kolmogorov's ratio definition $P(O_j \mid A) = P(O_j \cap A)/P(A)$, the evidential value $V(A)$ is mathematically undefined whenever $P(A) = 0$. Yet if Aomame and her twin are deterministic rational agents who know EDT prescribes cooperation, the probability that Aomame defects is $P(\text{Aomame } D) = 0$. How, then, was the reference text able to write $P(\text{Twin } D \mid \text{Aomame } D) = 1$?

To make EDT well-defined on the boundaries of the probability simplex, we introduce an operational **trembling-hand regularization** (or primitive conditional probability space, following Rényi–Popper axioms). Suppose an agent deliberates by assuming that, whatever decision rule she adopts, there is an infinitesimal implementation noise $\delta \in (0, 1/2)$ ("a trembling hand" or neural noise) that causes her to execute an unintended action $A$ with positive probability. In the Twin Prisoner's Dilemma, suppose Aomame and her twin share the same rational disposition, which leads them to intend $C$, while a shared cognitive fluctuation (of tiny probability $\delta > 0$) causes both to simultaneously deviate to $D$, and an independent physical slip (of higher-order tiny probability $\delta^2$) causes only one to deviate. Then $P(\text{Aomame } D) = \delta + \delta^2 > 0$, and taking the limit as $\delta \to 0^+$ yields:

$$\lim_{\delta \to 0^+} P(\text{Twin } D \mid \text{Aomame } D) = \lim_{\delta \to 0^+} \frac{\delta}{\delta + \delta^2} = 1.$$

Thus, when applying EDT to deterministic problems where suboptimal actions have prior probability zero, the analyst should evaluate $P(O_j \mid A)$ by perturbing the agent's decision policy with a small deliberation noise $\delta > 0$ that respects the structural correlations of the problem and taking the limit $\delta \to 0^+$.

### 3.2 Confounding Common Causes and "Managing the News"

The reference article notes two sharp philosophical criticisms of EDT. David Lewis characterized EDT as promoting "an irrational policy of managing the news" (Lewis 1981), while James M. Joyce objected that "Rational agents choose acts on the basis of their *causal efficacy*, not their auspiciousness; they act to *bring about* good results even when doing so might betoken bad news" (Joyce 1999, p. 146).

*(Illustrative model and operational analysis beyond the source text)*: To see the exact mathematical structure that motivates Lewis and Joyce, consider a classic common-cause confounding problem (often called a "Medical Newcomb" or "Smoking Lesion" problem). Suppose an asymptomatic genetic factor $G \in \{G_1, G_0\}$ has two independent downstream effects: it strongly predisposes an agent to enjoy and perform a harmless activity $A_1$ (over abstaining, $A_0$), and it also causes a severe illness $I_1$ (versus health, $I_0$) later in life. Crucially, the activity $A_1$ itself has zero causal effect on the illness $I_1$, and grants a mild enjoyment utility of $+1$, whereas the illness $I_1$ inflicts a utility loss of $-100$.

```
               [ Genetic Factor G ]
                  /            \
      (predisposes)            (causes)
                /                \
               v                  v
        [ Action A_1 ]      [ Illness I_1 ]
```

Because $G_1$ causes both $A_1$ and $I_1$, an external observer who sees the agent perform $A_1$ learns that $G_1$ is likely present, which in turn makes $I_1$ likely:

$$P(I_1 \mid A_1) > P(I_1 \mid A_0).$$

If the agent blindly plugs these raw conditional probabilities into $V(A)$, she calculates:

$$V(A_1) = P(I_1 \mid A_1)(-100 + 1) + P(I_0 \mid A_1)(1), \qquad V(A_0) = P(I_1 \mid A_0)(-100) + P(I_0 \mid A_0)(0).$$

Whenever $P(I_1 \mid A_1) - P(I_1 \mid A_0) > 0.01$, naive EDT yields $V(A_0) > V(A_1)$, advising the agent to abstain from the harmless activity $A_1$ purely so that she will not receive the "bad news" that she carries the gene $G_1$! This is what Lewis derides as "managing the news."

How should an operational EDT practitioner handle common-cause confounders? There are two rigorous positions available in the literature, and an analyst must decide which applies to the agent being modeled:

1. **The "Tickle Defense" (Introspective Screening-Off)**: Notice that in the causal graph $A_1 \leftarrow G \rightarrow I_1$, the genetic factor $G$ cannot magically move the agent's limbs without passing through the agent's conscious desires, inclinations, or credences—what philosophers call a mental "tickle" $T$. Prior to choosing $A_1$ or $A_0$, a self-aware agent already observes her own inclination $T$ to perform $A_1$. In probability theory, conditioning must always take place relative to the agent's **total current evidence** $E$, which includes $T$. If $T$ mediates the influence of $G$ on $A$, then $T$ *screens off* $A$ from $G$ (making $G$ and $A$ conditionally independent given $T$):

   $$P(I_1 \mid A_1, T) = P(I_1 \mid A_0, T) = P(I_1 \mid T).$$

   When we replace $P(O_j \mid A)$ with $P(O_j \mid A, T)$, the spurious correlation vanishes, and EDT recommends enjoying $A_1$:

   $$V(A_1 \mid T) = P(I_1 \mid T)(-100) + 1 > P(I_1 \mid T)(-100) = V(A_0 \mid T).$$

   Why doesn't introspective screening-off also destroy one-boxing in Newcomb's paradox or cooperation in the Twin Prisoner's Dilemma? Because in Newcomb's paradox, an accurate predictor predicts the agent's *final choice* $A$ (even after the agent observes her own tickle $T$), and in the Twin Prisoner's Dilemma, the twin shares both the tickle $T$ and the final choice rule $A(T)$. Thus, conditioning on $T$ eliminates spurious historical confounders that act only through known desires, while preserving evidential links to predictors and symmetric peers.

2. **Radical Evidentialism (Biting the Bullet)**: Alternatively, if $G$ influences the agent's final choice $A$ via subconscious pathways not accessible to introspection $T$, then $P(I_1 \mid A_1, T) > P(I_1 \mid A_0, T)$ remains true even after conditioning on all available mental evidence. As Arif Ahmed (2021) argues in defense of pure EDT, a consistent evidentialist simply accepts the prescription to choose $A_0$ in such cases, maintaining that statistical conditionalization is the single coherent standard of rational belief and choice.

### 3.3 Dynamic Decisions, Self-Locating Beliefs, and the Sleeping Beauty Problem

The reference text briefly notes an intriguing interaction between EDT and the **Sleeping Beauty problem**, citing Vincent Conitzer (2015). In the Sleeping Beauty problem, Beauty is put to sleep on Sunday, and a fair coin is tossed:
* If **Heads** ($H$), she is awakened only on Monday, interviewed, and put back to sleep.
* If **Tails** ($T$), she is awakened on Monday, interviewed, given an amnesia-inducing drug so she forgets Monday's awakening, and awakened again on Tuesday for an identical interview.

Upon waking up, Beauty cannot tell whether it is Monday or Tuesday. What credence $P(H)$ should she assign to the coin having landed Heads? "Thirders" argue $P(H) = 1/3$, whereas "halfers" argue $P(H) = 1/2$. 

*(Mathematical reconstruction of the cited Dutch book debate)*: Why does the reference text mention that halfers turned to EDT to escape **Dutch book arguments** (series of bets that guarantee a sure loss), only for Conitzer (2015) to show that halfers remain vulnerable even under EDT? Let us write down the exact math.

Suppose Beauty is a halfer ($P(H) = 1/2, P(T) = 1/2$) upon waking. Every time she wakes up, a bookie offers her a bet $B$ that pays $+\$15$ if $H$ and costs $-\$10$ if $T$.
* Under **CDT**, Beauty treats her current decision to accept ($A_{\text{acc}}$) or reject ($A_{\text{rej}}$) the bet as causally independent of what she does on another awakening. With $P(H) = 1/2$, her CDT expected value for accepting the bet is:

  $$U(A_{\text{acc}}) = \frac{1}{2}(\$15) + \frac{1}{2}(-\$10) = +\$2.50 > 0 = U(A_{\text{rej}}).$$

  So a CDT halfer accepts the bet every time she wakes up. However, when the coin lands Tails, she wakes up *twice* and accepts the bet *twice*, losing $\$20$ in total! Over many trials, she wins $\$15$ when Heads occurs ($50\%$ of trials) and loses $\$20$ when Tails occurs ($50\%$ of trials), suffering an expected loss of $-\$2.50$ per trial. If the bookie also sells her a counter-bet on Sunday before she goes to sleep, she suffers a guaranteed deterministic loss (a diachronic Dutch book).

* Now see how **EDT** rescues the halfer from this simple Dutch book. Because Monday-Beauty and Tuesday-Beauty are in identical epistemic states, they are psychological twins! Under EDT, Beauty recognizes that accepting the bet upon waking ($A_{\text{acc}}$) when the coin is Tails is guaranteed evidence that her twin on the other Tails-awakening *also* accepts the bet, incurring a total Tails loss of $-\$20$ rather than $-\$10$. Thus, her evidential expectation is:

  $$V(A_{\text{acc}}) = P(H \mid A_{\text{acc}})(\$15) + P(T \mid A_{\text{acc}})(-\$20) = \frac{1}{2}(\$15) + \frac{1}{2}(-\$20) = -\$2.50 < 0 = V(A_{\text{rej}}).$$

  Because EDT accounts for the correlation between her multiple awakenings under Tails, she rightly rejects the bet!

* How, then, does **Conitzer (2015)** construct a Dutch book against the EDT halfer? Conitzer demonstrates that the correlation between Monday and Tuesday awakenings can be broken if the bookie conditions the bets on events that distinguish the two days without Beauty realizing it, or offers bets whose payoffs depend only on what happens on *that specific awakening's day*. More simply, if the bookie privately flips a second coin or varies the betting menu across days so that Beauty's decision on awakening $k$ does not duplicate her exposure across both days of Tails, the EDT halfer's $1/2$ credence once again misprices the odds relative to the frequency of awakenings. 

For a decision theorist applying EDT to unfamiliar multi-stage problems, the lesson of Conitzer (2015) is crucial: while EDT naturally coordinates an agent's choices across symmetric information sets (acting as a self-enforcing commitment across "time-slice twins"), it does not by itself resolve diachronic incoherence if the underlying probability update rules for self-locating beliefs violate Bayes' rule across time.

---

## 4. Meta-Decision Theory: The Evidentialist's Wager

What if a reader remains torn between the philosophical intuitions of CDT and EDT? In the section "Other supporting arguments," the reference article cites *The Evidentialist's Wager* by William MacAskill, Aron Vallinder, Caspar Österheld, Carl Shulman, and Johannes Treutlein (2021), which argues that even if an agent places relatively low credence in the normative truth of EDT, it can still be rational to act *as if* EDT were true. Because EDT links an agent's choice to the choices of many correlated decision-makers, its stakes can vastly exceed those of CDT.

*(Operational formalization of the cited argument)*: Let us construct an explicit mathematical model of this meta-decision problem so a reader can evaluate when the wager applies. Suppose an agent faces normative uncertainty between two competing decision theories: she assigns credence $w \in (0,1)$ to EDT being the correct theory of rationality and credence $1 - w$ to CDT. 

Consider a generalized $N$-player public-goods game (or multicentric Prisoner's Dilemma), such as voting in a large election, reducing carbon emissions, or contributing to a shared resource. Each agent $i \in \{1, 2, \dots, N\}$ chooses whether to Cooperate ($C$) at a personal causal cost $c > 0$ or Defect ($D$) at cost $0$. Every agent who cooperates causally generates a benefit $b$ for the group (or for a shared impartial objective), where $b$ and $c$ satisfy:
* Under **CDT**, an individual's action only causes her own contribution. Suppose the direct causal return to the agent (or her objective) from her own single act of cooperation is net negative by a small margin $-\Delta_{\text{CDT}} < 0$ (for example, in a self-interested Prisoner's Dilemma where her own act costs $c$ and yields $0$ to herself, $\Delta_{\text{CDT}} = c$). Thus, CDT prefers $D$ over $C$ by stakes $\Delta_{\text{CDT}}$.
* Under **EDT**, however, the agent's choice to cooperate is correlated with the choices of the other $N - 1$ agents in the population. Suppose that for each other agent $j \neq i$, the evidential correlation between agent $i$ and agent $j$ is $\rho = P(A_j = C \mid A_i = C) - P(A_j = C \mid A_i = D) > 0$, and each peer who cooperates confers a benefit $b > 0$ on agent $i$. Then under EDT, the expected net benefit of choosing $C$ over $D$ is:

  $$\Delta_{\text{EDT}}(N) = (N - 1)\rho b - \Delta_{\text{CDT}}.$$

For a large population $N$ of correlated decision-makers, $\Delta_{\text{EDT}}(N)$ scales linearly with $N$, whereas the causal stakes $\Delta_{\text{CDT}}$ remain fixed at $O(1)$. If the meta-rational agent evaluates her choice by taking a credence-weighted expectation over the two normative theories (assuming inter-theoretic comparability of cardinal utilities), she should cooperate whenever:

$$w \cdot \Delta_{\text{EDT}}(N) + (1 - w)(-\Delta_{\text{CDT}}) > 0 \iff w > \frac{\Delta_{\text{CDT}}}{(N - 1)\rho b}.$$

For instance, if $N = 10,001$ correlated agents face a symmetric public goods dilemma with $\rho = 0.1$, $b = 5$, and $\Delta_{\text{CDT}} = 1$, then $\Delta_{\text{EDT}} = 10,000(0.1)(5) - 1 = 4,999$. The threshold credence required to cooperate is merely $w > 1 / 5,000 = 0.0002$. Even an agent who is $99.9\%$ convinced by Causal Decision Theory and gives only a $0.1\%$ credence to Evidential Decision Theory should act like an evidentialist whenever her decision is correlated with a sufficiently large reference class of peers.

---

## 5. Summary Procedure: How to Apply EDT to Unfamiliar Cases

To synthesize our mathematical account into an actionable toolkit, a researcher or practitioner confronting a novel decision problem can apply Evidential Decision Theory by executing the following five-step algorithm:

1. **Specify the Action and State Partitions**: Define the mutually exclusive set of available actions $\mathcal{A} = \{A_1, \dots, A_m\}$ and a partition of background states of the world $\mathcal{S} = \{S_1, \dots, S_n\}$ fine-grained enough that every pair $(A_k, S_i)$ determines a well-defined outcome with utility $D(A_k, S_i)$. Include all symmetric peers' actions, predictors' states, or multi-awakening copies as components of $\mathcal{S}$.
2. **Condition on Pre-Choice Introspective Evidence**: Identify the agent's total current evidence $E$ available *prior* to finalizing the choice (including conscious desires or "tickles" $T$). If a historical common cause $G$ influences $A_k$ solely through $E$, conditioning on $E$ screens off the spurious confounder so that $P(S_i \mid A_k, E) = P(S_i \mid E)$.
3. **Compute Diagnostic Conditional Probabilities**: For each action $A_k$ and state $S_i$, determine $P(S_i \mid A_k, E)$. If the problem specifies generative likelihoods $P(A_k \mid S_i, E)$ and priors $P(S_i \mid E)$, apply Bayes' theorem. If deterministic rationality drives $P(A_k \mid E) \to 0$ for off-equilibrium actions, introduce a small trembling-hand noise $\delta > 0$ that respects the correlation structure of the mechanism and take the limit as $\delta \to 0^+$.
4. **Evaluate News Value**: Compute the evidential expected utility for each action:
   $$V(A_k) = \sum_{i=1}^{n} P(S_i \mid A_k, E) D(A_k, S_i).$$
5. **Select the Maximizing Action**: Choose $A^* \in \arg\max_{A_k \in \mathcal{A}} V(A_k)$. If you are uncertain whether EDT or CDT is normatively correct in a problem involving $N$ correlated agents, compare the evidential stakes $\Delta_{\text{EDT}}(N)$ against the causal stakes $\Delta_{\text{CDT}}$ using the Evidentialist's Wager.

---

## 6. Conclusion

Evidential Decision Theory offers a strikingly unified vision of rational agency: just as Bayesian epistemology governs belief revision through conditional probability $P(O_j \mid E)$, EDT governs practical deliberation through the exact same conditional operator $P(O_j \mid A)$. As we have seen from the reference literature and our mathematical extensions, this simple commitment allows EDT decision-makers to walk away with the million dollars in Newcomb's paradox and achieve mutual cooperation in the Twin Prisoner's Dilemma, where causal decision theorists are condemned by dominance reasoning to leave empty-handed. At the same time, the theory forces us to confront subtle foundational questions regarding common-cause confounding, measure-zero boundaries, and diachronic vulnerability in self-locating problems. Whether one embraces EDT as a fundamental theory of rationality or adopts it pragmatically via the Evidentialist's Wager, understanding the mathematics of news value is indispensable for modeling strategic interaction in a world of correlated minds.

---

## References

* Ahmed, Arif (2021). *Evidential Decision Theory*. Cambridge University Press. ISBN 9781108607865.
* Conitzer, Vincent (2015). "A Dutch book against sleeping beauties who are evidential decision theorists". *Synthese*, **192** (9): 2887–2899. arXiv:1705.03560. doi:10.1007/s11229-015-0691-7.
* Gibbard, Allan; Harper, William L. (1976). *Counterfactuals and Two Kinds of Expected Utility*, pp. 7–8.
* Greene, Preston; Levinstein, Benjamin (2020). "Act Consequentialism without Free Rides". *Philosophical Perspectives*, **34** (1): 100–101. doi:10.1111/phpe.12138.
* Joyce, James M. (1999). *The Foundations of Causal Decision Theory*, p. 146. Cambridge University Press.
* Lewis, David (1981). "Causal decision theory". *Australasian Journal of Philosophy*, **59** (1): 5–30. doi:10.1080/00048408112340011.
* MacAskill, William; Vallinder, Aron; Österheld, Caspar; Shulman, Carl; Treutlein, Johannes (2021). *The Evidentialist's Wager*. Global Priorities Institute.
* Wolpert, David H.; Benford, Gregory (2013). "The lesson of Newcomb's paradox". *Synthese*, **190** (9): 1637–1646. doi:10.1007/s11229-011-9899-3.
````

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Approach**

I'm currently focused on defining the approach for this project. My initial thought is to structure the essay to suit a mathematically-inclined audience. I intend to present EDT in a clear, formal manner, touching on its philosophical underpinnings as the user suggested. I'm prioritizing accessibility for a broad expert audience.


**Refining the Scope**

I've been refining the scope and objectives. I'm aiming for a 2400-3000 word essay based on the EDT Wikipedia article, but expanded with my own mathematical definitions, equations, examples, and interpretations where the source is vague. I'll clearly distinguish what comes from the source versus my original contributions, ensuring it's accessible to a mathematically literate audience interested in formal procedures and philosophical motivations. The goal is a coherent account usable to apply EDT to new scenarios.


**Clarifying Gaps and Format**

I'm now focused on handling gaps and refining the essay's format. Where the source is unclear, I'll explain the uncertainty and offer a justified interpretation. I'll distinctly label the source's claims versus my additions. The goal is a readable mathematical essay, not a case-study response. I'm aiming for about 2,600-2,800 words, prioritizing a complete explanation of key concepts. I'll omit unnecessary repetition, length bibliographies, and appendices to ensure coherent flow.


**Contrasting the Theories**

I'm now diving into the core differences between EDT and CDT, specifically highlighting their divergence in scenarios like Newcomb's paradox. I'm focusing on formal definitions and thought experiments. I'm defining EDT using the equation $V(A) = \sum_j P(O_j \mid A) D(O_j)$, contrasting it with CDT’s $U(A) = \sum_j P(A \mathrel{\Box{\rightarrow}} O_j) D(O_j)$. The key here is the distinction in probability calculations. I'm using Newcomb's paradox to illustrate the contrasting prescriptions, with EDT advocating for one-boxing.


**Analyzing the Implications**

I'm now assessing the implications of EDT through several thought experiments. I'm calculating the expected values for Newcomb's paradox, where I'm consistently one-boxing. I'm then examining the twin prisoner's dilemma, where EDT recommends cooperation, and also exploring Sleeping Beauty to address Dutch book arguments, noting Conitzer's relevant counterpoints. I'm also considering MacAskill's "Evidentialist's Wager".


**Addressing the Critics**

I'm now grappling with criticisms of EDT, specifically focusing on Lewis's "irrational policy" and Joyce's focus on causal efficacy. I'm considering how these arguments relate to the core EDT framework and trying to articulate my own responses, and whether I can justify my EDT-driven conclusions. I'm exploring the implications on different cases.


**Investigating the Mathematics**

I'm now investigating the mathematics of EDT, particularly the implications of zero-probability events in conditional probability calculations. I'm focusing on scenarios where deliberation causes certainty about an action, making the conditional probability undefined. I'm also considering how the prior joint distribution $P(S, A)$ is constructed to deal with the problem of common causes, such as the correlation between smoking and lesions. I'm considering the Smoking lesion problem, and similar.


**Expanding the Model**

I'm now expanding the EDT model to cover more nuanced scenarios. I'm focusing on incorporating the "tickle defense" or introspective evidence to address issues like the Gene/Medical Newcomb problem. I'm also attempting to mathematically formalize how EDT handles multi-stage decision problems, especially those involving self-locating beliefs, as seen in the Sleeping Beauty problem and policy evaluation, referencing Conitzer (2015). I'm looking at formalizing the Evidentialist's Wager using the mathematical model.


**Structuring the Essay**

I'm now structuring the essay. I've broken the work into sections. I will begin with the title, which I will make engaging. I will start the essay by introducing the core problem of rational choice: when we choose an act, are we intervening on the world to *cause* an outcome, or learning what kind of world we inhabit? I'll define EDT via the source's slogan: maximizing *news value* and briefly contrast it with CDT.


**Formalizing the Equations**

I'm now diving into the formal architecture, presenting the Gibbard and Harper equations, contrasting evidential and causal perspectives. I'm translating the outcome-space formulation to a state-action space, showing how EDT calculates expected value. I am analyzing the divergence of the probabilities, highlighting the point where EDT and CDT converge. My next focus is the discussion of common causes.


**Applying the Mathematics**

I'm now applying the mathematics to canonical examples. I've set up the state space, predictor accuracy, and derived the values for Newcomb's Paradox, contrasting evidential and causal expected values. Also, I've derived the Twin Prisoner's Dilemma, showing how EDT promotes cooperation, noting that EDT achieves mutual cooperation without causal links. I am making use of Wolpert, Benford, Ahmed, Greene and Levinstein's mathematical formalisms.


**Operationalizing the Model**

I'm now operationalizing the model, addressing gaps in the source material by developing frameworks to resolve critical mathematical questions. I'm focusing on conditional probabilities when $P(A) = 0$ using Bayes' theorem, the base-rate requirement, and $\varepsilon$-perturbation. Then, I'll tackle confounding common causes. I'm actively considering the predictor's accuracy in Newcomb's paradox as it relates to my actions.


**Clarifying the Confounders**

I'm now clarifying the nature of common-cause confounders, specifically Lewis' "irrational policy" and Joyce's "causal efficacy" issues. I'm constructing a mathematical example of a pure common-cause confounder to illustrate the problems, such as a genetic lesion scenario. I'll explain how an EDT agent handles this, emphasizing the importance of conditioning on total evidence, and the potential for introspective evidence to mitigate spurious correlations.


**Analyzing Sleeping Beauty**

I'm now analyzing the Sleeping Beauty problem within the EDT framework, focusing on how it avoids Dutch books for "halfers". I'll mathematically show how EDT changes betting odds for a halfer and why, according to Conitzer (2015), they remain vulnerable. I'm also discussing implications for evaluating multi-step policies, and the idea of diachronic Dutch books.


**Formalizing the Wager**

I'm now mathematically formalizing MacAskill's "Evidentialist's Wager" to show how, even with a small credence in EDT, evidential reasoning can dominate in multi-agent scenarios. I'll demonstrate that as the number of correlated agents increases, the evidential advantage grows, mathematically showing how EDT can be practically superior. I'm also preparing for the conclusion and compiling the references.


**Verifying the Citations**

I'm now focusing on ensuring accuracy and clarity in referencing. I'll clearly distinguish between the source's claims and my extensions, adding my operational interpretations and mathematical examples where necessary to aid comprehension. I'm using LaTeX formatting for all equations for readability. I'm also actively monitoring the word count of each section to ensure the overall length remains within the target range.


**Formalizing the Spaces**

I'm now formalizing the probability spaces and relating Gibbard and Harper's formula to state-action formulations. I'll define $(\Omega, \mathcal{F}, P)$, $\mathcal{A}$, $\mathcal{S}$, and the outcome map $O(A_k, S_i)$. I'll connect $V(A) = \sum_j P(O_j \mid A) D(O_j)$ to $\sum_i P(S_i \mid A) D(A, S_i)$, and also include CDT's subjunctive conditional. Then I'll present key examples.


**Expanding the Formalism**

I'm now expanding the formalism, focusing on a more general formulation of the Prisoner's Dilemma, using $R, P, T, S$ payoffs, correlation coefficients, and conditional probabilities. I'm addressing open questions in the source, particularly those concerning construction of $P(O_j \mid A)$ from generative priors, along with the subtler traps in Newcomb's paradox. I'm carefully examining the relationships between diagnostic and generative probabilities, highlighting the role of prior probabilities using Bayes' rule.


**Elaborating the Formalism**

I'm expanding the formalism by considering likelihood $P(A \mid S_i)$ for EDT application. I'm addressing causal confounding using a mathematical model of a common cause, clarifying how pre-choice evidence affects $P(S \mid A)$. I'm also mathematically explaining the Sleeping Beauty problem, showing the distinction between EDT and CDT halfer evaluations of diachronic choices.


```
