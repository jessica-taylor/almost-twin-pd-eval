# 012_edt_wikipedia_google_gemini-3.8-flash_rlow_plow / 00006

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/557ae4a0-8940-49da-80e9-b742bee4cb26/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/557ae4a0-8940-49da-80e9-b742bee4cb26/call_0/response.raw) · finish: `stop`

### Visible response

````text
# The Logic of News Value: A Formal and Philosophical Analysis of Evidential Decision Theory

## 1. Introduction: Auspiciousness versus Efficacy

At the core of normative decision theory lies a deceptive question: *What makes an action rational?* 

Classical expected utility theory, codified in the mid-twentieth century by John von Neumann, Oskar Morgenstern, and Leonard Savage, formalizes decision-making under risk and uncertainty. However, Savage’s framework relies on a sharp conceptual bifurcation between **acts**, **states of the world**, and **consequences**, requiring states to be statistically independent of the acts chosen. When an agent's choice correlates with the background state of the world—whether due to common causes, accurate predictors, or symmetric reasoning partners—this neat separation breaks down.

In response, modern decision theory split into two primary camps:
1. **Evidential Decision Theory (EDT)**, which formalizes the intuition that a rational agent should choose an action that serves as the best possible *evidence* for a desirable state of affairs. Informally, EDT advises: *"Do what you would most like to learn that you have done"* (Ahmed, 2021).
2. **Causal Decision Theory (CDT)**, which insists that a rational act must be evaluated solely by what it *physically or counterfactually brings about*, filtering out spurious statistical correlations that the agent cannot causally influence (Gibbard & Harper, 1976; Lewis, 1981; Joyce, 1999).

David Lewis famously maligned EDT as an irrational policy of "managing the news," while James M. Joyce maintained that rational agents choose acts on the basis of causal efficacy rather than auspiciousness. Yet, EDT remains mathematically clean, philosophically resilient, and surprisingly potent—frequently out-earning CDT in scenarios with high informational interdependence.

This essay provides an analytical account of Evidential Decision Theory. We will formalize its decision rule, analyze its treatment of statistical and counterfactual dependencies, walk through classic dilemmas, address foundational criticisms such as the "common cause" problem, and evaluate recent arguments concerning evidential wagers and anthropic reasoning.

---

## 2. Mathematical Formalization

### 2.1 The Probability Space and Primitive Objects

Let $(\Omega, \mathcal{F}, P)$ be a subjective probability space representing an agent’s epistemic state:
- $\Omega$ is the set of all possible worlds.
- $\mathcal{F}$ is a $\sigma$-algebra of events (propositions) over $\Omega$.
- $P: \mathcal{F} \to [0, 1]$ is the agent’s subjective probability measure (credence).

Let $\mathcal{A} = \{A_1, A_2, \dots, A_n\} \subset \mathcal{F}$ be a finite set of mutually exclusive and exhaustive propositions representing the **candidate actions** available to the agent at time $t_0$. We assume $P(A_i) > 0$ for all $i$ (an assumption we will scrutinize in Section 5.1).

Let $\mathcal{O} = \{O_1, O_2, \dots, O_m\} \subset \mathcal{F}$ be a partition of mutually exclusive and exhaustive **outcomes** (or consequences) that fully specify everything the agent cares about.

Let $D: \mathcal{O} \to \mathbb{R}$ be a bounded **desirability function** (utility function), unique up to positive affine transformations, mapping each outcome $O_j$ to a real number $D(O_j)$.

### 2.2 The Evidential Decision Rule

The foundational thesis of EDT, traced formally to Richard Jeffrey (1965) and characterized cleanly by Allan Gibbard and William Harper (1976), is that the value of an act is its **conditional expected desirability**—its *news value*:

$$V(A) = \mathbb{E}_P[D \mid A] = \sum_{j=1}^m P(O_j \mid A) D(O_j)$$

where $P(O_j \mid A)$ is defined by standard Kolmogorov conditioning:

$$P(O_j \mid A) = \frac{P(O_j \cap A)}{P(A)}$$

The **Evidential Decision Rule** states:

$$\text{Select } A^* \in \mathcal{A} \quad \text{such that} \quad A^* \in \arg\max_{A \in \mathcal{A}} V(A)$$

If multiple actions attain the maximum, any lottery over them is permissible.

```
                  ┌──────────────────────────────┐
                  │ Candidate Action Space: {A} │
                  └──────────────┬───────────────┘
                                 │
                   Condition on candidate act A
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │ Posterior Credence Over      │
                  │ Outcomes: P(O_j | A)         │
                  └──────────────┬───────────────┘
                                 │
                   Weight outcomes by utility D(O_j)
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │ Evidential News Value:       │
                  │ V(A) = ∑ P(O_j | A) D(O_j)   │
                  └──────────────┬───────────────┘
                                 │
                     Select A* = argmax V(A)
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │ Optimal Evidential Choice    │
                  └──────────────────────────────┘
```

### 2.3 Contrast with Causal Decision Theory

To contrast EDT with CDT, Gibbard and Harper (1976) introduced the counterfactual conditional operator $\Box{\rightarrow}$, where $A \mathrel{\Box{\rightarrow}} O_j$ denotes the proposition: *"If action $A$ were performed, outcome $O_j$ would obtain."*

Causal Decision Theory evaluates acts by their **causal expected utility**:

$$U(A) = \sum_{j=1}^m P(A \mathrel{\Box{\rightarrow}} O_j) D(O_j)$$

The central divergence between the two paradigms reduces to a single mathematical wedge:

$$P(O_j \mid A) \neq P(A \mathrel{\Box{\rightarrow}} O_j)$$

- **EDT** treats the choice of $A$ as an *epistemic update*: conditioning on $A$ recalculates the probability of past, present, and future world-states given the news that $A$ occurred.
- **CDT** treats $A$ as an *intervention* (analogous to the $\text{do}(A)$ operator in Judea Pearl’s causal calculus), severing the incoming informational arrows to $A$ and computing expectations over counterfactual world-states held fixed relative to the intervention:

$$U(A) \equiv \mathbb{E}[D \mid \text{do}(A)] = \sum_{j=1}^m P(O_j \mid \text{do}(A)) D(O_j)$$

---

## 3. Resolving Classic Canonical Dilemmas

### 3.1 Newcomb’s Paradox

Consider the standard formulation:
- **Box A** is transparent and contains $\$1,000$.
- **Box B** is opaque and contains either $\$1,000,000$ or $\$0$.
- An ultra-reliable predictor placed $\$1,000,000$ in Box B if and only if it predicted that the player would take **only Box B** ("one-boxing"). If it predicted that the player would take **both boxes** ("two-boxing"), Box B was left empty.
- The prediction has already occurred; the contents are physically fixed.

Let the action set be $\mathcal{A} = \{A_1, A_2\}$, where $A_1 = \text{take only Box B}$ and $A_2 = \text{take both boxes}$.  
Let the background states be $S_1 = \text{Box B contains } \$1\text{M}$ and $S_0 = \text{Box B is empty}$.  
Assume linear utility in money: $D(\$x) = x$.

The predictor's historical accuracy is $p \in (0.5, 1.0]$. Formally:
$$P(S_1 \mid A_1) = p, \quad P(S_0 \mid A_1) = 1 - p$$
$$P(S_0 \mid A_2) = p, \quad P(S_1 \mid A_2) = 1 - p$$

Computing evidential values:
$$\begin{aligned}
V(A_1) &= P(S_1 \mid A_1) \cdot D(\$1,000,000) + P(S_0 \mid A_1) \cdot D(\$0) \\
&= p(1,000,000) + (1-p)(0) = 1,000,000 \cdot p
\end{aligned}$$

$$\begin{aligned}
V(A_2) &= P(S_1 \mid A_2) \cdot D(\$1,001,000) + P(S_0 \mid A_2) \cdot D(\$1,000) \\
&= (1-p)(1,001,000) + p(1,000) \\
&= 1,001,000 - 1,000,000 \cdot p
\end{aligned}$$

EDT recommends one-boxing ($A_1$) if and only if:
$$V(A_1) > V(A_2) \iff 1,000,000 \cdot p > 1,001,000 - 1,000,000 \cdot p$$
$$2,000,000 \cdot p > 1,001,000 \iff p > \frac{1,001}{2,000} = 0.5005$$

For an accuracy of $p = 0.99$:
- $V(A_1) = 0.99 \times \$1,000,000 = \$990,000$
- $V(A_2) = 0.01 \times \$1,001,000 + 0.99 \times \$1,000 = \$10,010 + \$990 = \$11,000$

Because $\$990,000 \gg \$11,000$, EDT decisively mandates **one-boxing**.

#### The CDT Rebuttal and the Dominance Principle
CDT appeals to the **Strong Dominance Principle**: in state $S_1$, $A_2$ yields $\$1,001,000$ versus $\$1,000,000$ for $A_1$. In state $S_0$, $A_2$ yields $\$1,000$ versus $\$0$ for $A_1$. Because the state is already causally determined, $P(A_i \mathrel{\Box{\rightarrow}} S_k) = P(S_k)$. Thus:
$$U(A_2) - U(A_1) = \$1,000 > 0 \quad \forall P(S_1) \in [0, 1]$$
CDT takes both boxes. EDT rejects the causal framing of the dominance principle: dominance holds only when states are conditionally independent of acts. Here, because learning $A$ changes the probability distribution over $S$, the dominance argument is evidentially invalid.

---

### 3.2 The Twin Prisoner’s Dilemma

Let player 1 (Aomame) face an identical cognitive twin, player 2. The payout matrix is:

| | Twin Cooperates ($C_2$) | Twin Defects ($D_2$) |
|---|---|---|
| **Aomame Cooperates ($C_1$)** | $(\$5, \$5)$ | $(\$0, \$10)$ |
| **Aomame Defects ($D_1$)** | $(\$10, \$0)$ | $(\$1, \$1)$ |

Because the twin is an exact psychological counterpart executing identical algorithms under identical priors:
$$P(C_2 \mid C_1) = 1 - \epsilon, \quad P(D_2 \mid D_1) = 1 - \epsilon$$
where $\epsilon \ge 0$ represents minor environmental or cognitive divergence. 

Assuming symmetry ($\epsilon = 0$):
$$\begin{aligned}
V(C_1) &= P(C_2 \mid C_1) \cdot D(\$5) + P(D_2 \mid C_1) \cdot D(\$0) = 1 \cdot 5 + 0 = \$5 \\
V(D_1) &= P(C_2 \mid D_1) \cdot D(\$10) + P(D_2 \mid D_1) \cdot D(\$1) = 0 \cdot 10 + 1 \cdot 1 = \$1
\end{aligned}$$

EDT dictates **cooperation** ($V(C_1) = 5 > 1 = V(D_1)$).

```
   ┌───────────────────────┐
   │  Cognitive Substrate  │
   │    (Shared Logic)     │
   └──────────┬────────────┘
              │ Correlated reasoning
       ┌──────┴──────┐
       ▼             ▼
  ┌─────────┐   ┌─────────┐
  │ Aomame  │   │  Twin   │
  │ Choice  │   │ Choice  │
  └────┬────┘   └────┬────┘
       │             │
       ▼             ▼
  ┌───────────────────────┐
  │     Final Payoff      │
  └───────────────────────┘
```

CDT objects that Aomame's physical muscles have no causal path to the twin's brain in the other room:
$$P(C_1 \mathrel{\Box{\rightarrow}} C_2) = P(C_2)$$
Under CDT, defection strictly dominates. Yet, two evidential agents walk away with $\$5$ each, while two causal agents walk away with $\$1$ each. Evidential agents systematically exploit informational coordination without physical communication—a result echoing Douglas Hofstadter’s concept of *superrationality*.

---

## 4. The Critical Challenges to EDT

Despite its success in Newcombian problems, EDT faces several classic counterexamples that target its sensitivity to non-causal correlations.

### 4.1 The Smoking Lesion Problem and the "Managing the News" Objection

The canonical counterexample to EDT (originating with Ronald Nozick and formalized by Gibbard & Harper) is the **Smoking Lesion**:
- There exists a genetically determined pre-malignant brain lesion ($L$).
- $L$ causes both a strong biological craving to smoke ($S$) and lung cancer ($C$).
- Smoking itself does not cause cancer; cancer is caused entirely by the lesion.
- Smoking provides immediate sensory pleasure ($+10$), while cancer incurs an enormous penalty ($-1000$).

```
        ┌─────────────────────────┐
        │  Genetic Lesion (L)     │
        └────────────┬────────────┘
                     │
         ┌───────────┴───────────┐
         ▼                       ▼
   ┌───────────┐           ┌───────────┐
   │ Craving/  │           │  Cancer   │
   │  Smoking  │           │    (C)    │
   └───────────┘           └───────────┘
```

Let:
- $P(L \mid S) = 0.9$, $P(L \mid \neg S) = 0.1$
- $P(C \mid L) = 0.8$, $P(C \mid \neg L) = 0.0$
- $D(\text{Smoke}, C) = -990$, $D(\text{Smoke}, \neg C) = +10$
- $D(\neg \text{Smoke}, C) = -1000$, $D(\neg \text{Smoke}, \neg C) = 0$

Conditioning on smoking:
$$P(C \mid S) = P(C \mid L) P(L \mid S) + P(C \mid \neg L) P(\neg L \mid S) = 0.8(0.9) + 0 = 0.72$$
$$P(C \mid \neg S) = P(C \mid L) P(L \mid \neg S) + P(C \mid \neg L) P(\neg L \mid \neg S) = 0.8(0.1) + 0 = 0.08$$

Calculating evidential values:
$$\begin{aligned}
V(S) &= 0.72(-990) + 0.28(10) = -712.8 + 2.8 = -710 \\
V(\neg S) &= 0.08(-1000) + 0.92(0) = -80
\end{aligned}$$

Because $V(\neg S) = -80 > -710 = V(S)$, naive EDT forbids smoking.

Here, critics charge EDT with sanctioning magical thinking: an agent who enjoys smoking refrains from doing so purely to avoid receiving the bad news that they harbor a fatal lesion, even though the lesion is already present or absent. This is the root of David Lewis's objection: EDT conflates an action's diagnostic value with its causal efficacy.

---

## 5. Formal Defenses and Structural Extensions

To address cases like the Smoking Lesion, evidential decision theorists developed several refinements. Below, we separate defenses grounded in existing literature from formal operationalizations.

### 5.1 The Tickle Defense (Eells and Jeffrey)

The classical evidential defense against the Smoking Lesion is the **Tickle Defense**, advanced by Brian Skyrms (1982) and Ellery Eells (1982).

The argument proceeds as follows: The lesion $L$ does not cause the physical act of smoking directly; it causes a conscious *craving* or somatic urge—a "tickle" ($T$). Once the rational agent introspects, the presence or absence of this tickle becomes known prior to the final decision. 

Let the agent's total introspective epistemic state include either $T$ or $\neg T$. By the Markov property of the causal chain:

$$L \longrightarrow T \longrightarrow S$$

The condition $T$ screens off the action $S$ from the common cause $L$:

$$P(L \mid S \cap T) = P(L \mid \neg S \cap T) = P(L \mid T)$$

#### Theorem 1 (Screening-Off Restores Causal Convergence)
If an agent conditions on their full introspective mental state $K$, and $K$ screens off the common cause $L$ from the act $A$ such that $P(L \mid A \cap K) = P(L \mid K)$, then the evidential ranking of actions conditioned on $K$ agrees with the causal ranking.

*Proof.*  
Let outcome $O$ depend solely on background state $L$ and act $A$, with utility $D(A, L)$. The conditional evidential value of act $A$ given introspective state $K$ is:

$$V(A \mid K) = \sum_{l} P(L = l \mid A \cap K) D(A, L = l)$$

By the screening-off hypothesis, $P(L = l \mid A \cap K) = P(L = l \mid K)$. Therefore:

$$V(A \mid K) = \sum_{l} P(L = l \mid K) D(A, L = l)$$

Now consider the causal expected utility $U(A \mid K)$ under an intervention $\text{do}(A)$ holding epistemic background $K$ fixed:

$$U(A \mid K) = \sum_{l} P(A \mathrel{\Box{\rightarrow}} L = l \mid K) D(A, L = l)$$

Because $L$ is causally upstream of $A$, intervening on $A$ does not alter $L$, so $P(A \mathrel{\Box{\rightarrow}} L = l \mid K) = P(L = l \mid K)$. Thus:

$$V(A \mid K) \equiv U(A \mid K)$$

When introspective screening-off holds, EDT recommends smoking: given that the agent already feels the craving ($T$), the cancer risk is already fixed at $P(C \mid T)$, making the act of smoking purely an addition of $+10$ utility. $\blacksquare$

---

### 5.2 Beyond Introspection: A General Operationalization

While the Tickle Defense resolves cases where the internal craving is fully introspectible, it struggles with non-conscious or unidentifiable common causes. What if the lesion causes smoking without generating an introspectible psychological state?

Here we can formalize a more general operational rule for an evidential agent.

#### Proposal: Metacognitive Deliberational Dynamics
*(The following construction generalizes proposals by Skyrms and Arntzenius regarding deliberational dynamics within an evidential framework.)*

Let deliberation be an iterative process over continuous time $\tau \in [0, 1]$. At each moment $\tau$, the agent holds a tentative mixed intention—a credence vector over their own candidate actions:

$$\mathbf{p}(\tau) = \big(p_1(\tau), p_2(\tau), \dots, p_n(\tau)\big), \quad p_i(\tau) = P_\tau(A_i)$$

1. **Epistemic Transparency:** The agent has continuous introspective access to their own credences: $\mathbf{p}(\tau)$ is in the agent's conditioning history $\mathcal{H}_\tau$.
2. **Conditional Valuation:** The agent computes the evidential value of each action conditional on both the act and their current deliberational state:
   $$V(A_i \mid \mathbf{p}(\tau)) = \sum_j P(O_j \mid A_i \cap \{\mathbf{p}(\tau)\}) D(O_j)$$
3. **Probability Adjustment:** The credences evolve continuously toward actions that exhibit superior current news value:
   $$\frac{d p_i}{d\tau} = p_i(\tau) \left[ V(A_i \mid \mathbf{p}(\tau)) - \bar{V}(\mathbf{p}(\tau)) \right]$$
   where $\bar{V}(\mathbf{p}(\tau)) = \sum_k p_k(\tau) V(A_k \mid \mathbf{p}(\tau))$ is the average expected value.

#### Resolving Common-Cause Failures
If an agent realizes that their ultimate action is determined by their own rational deliberations, then condition $\{\mathbf{p}(\tau)\}$ increasingly captures all actionable information regarding their final choice. 

If the state of ultimate resolve $\mathbf{p}^* = \lim_{\tau \to 1} \mathbf{p}(\tau)$ screens off the lesion $L$ from the physical act $A$:
$$P(L \mid A_i \cap \mathbf{p}^*) = P(L \mid \mathbf{p}^*)$$
then EDT reproduces the causal choice even in the absence of visceral somatic "tickles." 

However, in Newcomb's Paradox, **deliberation does not screen off the state**. The predictor modeled the agent's *entire reasoning architecture*, including how the deliberational dynamics would unfold. As a result:
$$P(S_1 \mid A_1 \cap \mathbf{p}^*) \neq P(S_1 \mid A_2 \cap \mathbf{p}^*)$$
Because conditioning on the terminal decision still provides diagnostic evidence of the predictor's prior choice, EDT continues to prescribe one-boxing. This establishes a clean formal dividing line:

> **Structural Criterion:**  
> An evidential agent converges with causal decisions whenever internal deliberative states screen off acts from states ($A \perp S \mid \mathbf{p}$), but retains its cooperative/one-boxing verdicts whenever the external world anticipates the deliberative dynamics themselves ($A \not\perp S \mid \mathbf{p}$).

---

## 6. Advanced Frontiers: Anthropic Credence and Decision Theory

### 6.1 The Sleeping Beauty Problem and Dutch Books

The interaction between EDT and self-locating (anthropic) credences arises prominently in the **Sleeping Beauty Problem**:
- Beauty is put to sleep on Sunday.
- A fair coin is tossed ($H$ or $T$).
- If Heads ($H$), she is awakened only on Monday.
- If Tails ($T$), she is awakened on Monday, given an amnesia-inducing drug, and awakened again on Tuesday.
- Upon awakening, she is asked for her credence $P(H)$.

The two main philosophical positions are:
- **Halfers:** $P(H) = 1/2$, appealing to the principle that learning no new objective evidence should not change one's credence in a fair coin flip.
- **Thirders:** $P(H) = 1/3$, appealing to the observation that across many repetitions, two-thirds of awakenings occur in the Tails branch.

The reference article notes that EDT has been applied to this problem to insulate "halfers" from Dutch books (bets engineered to guarantee a net loss). 

Consider a bookie offering Beauty a gamble upon awakening: *"Pay $\$c$ to receive $\$1$ if the coin landed Heads."* 

Let $A$ be the act of accepting this wager. Under standard causal updates, a halfer setting $P(H) = 1/2$ would price the ticket at $\$0.50$. However, if Tails landed, she accepts this bet **twice** (Monday and Tuesday), multiplying her losses. 

EDT resolves this by evaluating the news value of accepting the bet:
$$V(\text{Accept}) = P(H \mid \text{Accept}) \cdot (1 - c) + P(T \mid \text{Accept}) \cdot 2(-c)$$

Because Beauty recognizes that her decision to accept the bet provides evidence that she accepts it in *all* indistinguishable awakenings, EDT computes:
$$P(H \mid \text{Accept awakening}) = \frac{1/2}{1/2 + 2(1/2)} = \frac{1}{3}$$

Under EDT, even an agent who assigns a subjective prior of $1/2$ to $H$ will *act* as if the probability is $1/3$, because the act of betting carries the diagnostic news of taking on double the exposure under the Tails scenario.

However, as Vincent Conitzer (2015) demonstrated, halfers who adopt EDT remain vulnerable to more complex, state-dependent Dutch books when sequential or non-linear payouts are involved. EDT alone cannot fully bridge the foundational divide between halfer credences and rational sequential betting.

---

### 6.2 The Evidentialist's Wager

A compelling modern development at the intersection of meta-ethics and decision theory is **The Evidentialist's Wager** (MacAskill et al., 2021).

Suppose an agent faces normative uncertainty: they assign credence $\alpha \in (0, 1)$ to EDT being the correct normative decision theory, and credence $(1 - \alpha)$ to CDT. How should they choose an action?

Consider a scenario where the agent interacts with other decision-makers across the cosmos:
1. **CDT-dominated scope:** Causal decisions affect only the agent’s immediate local environment (e.g., whether to smoke a cigarette, or two-box against a single local predictor).
2. **EDT-dominated scope:** An evidential choice can be correlated with the choices of vast ensembles of structurally similar agents throughout an infinite or spatio-temporally vast universe (e.g., cosmological twins, civilizational peers facing collective action problems).

Under EDT, an agent's choice to cooperate or take an altruistic action provides positive evidence that *billions of correlated agents across the universe* are doing the same. The stakes of this informational correlation scale with the size of the correlated ensemble $N$:

$$V_{\text{total}}(A_{\text{cooperate}}) \propto N \cdot D(\text{collective success})$$

Under CDT, the agent's causal impact remains local and bounded:

$$U_{\text{total}}(A_{\text{cooperate}}) \propto 1 \cdot D(\text{local success})$$

As $N \to \infty$, the expected value of acting according to EDT dominates the expected value under CDT for any fixed non-zero credence $\alpha > 0$:

$$\mathbb{E}[\text{Utility}(A)] = \alpha V(A) + (1 - \alpha) U(A)$$

Because $V(A)$ can scale linearly with the total volume of correlated reasoning across reality, the evidential component rapidly dwarfs the causal component. The "Evidentialist's Wager" thus concludes that whenever an agent assigns any non-zero credence to EDT, they ought to act in accordance with evidential prescriptions in symmetric, high-stakes coordination problems.

---

## 7. Comparative Framework: EDT, CDT, and Counterfactual Inference

To clarify the operational differences when evaluating candidate actions, consider the following structural comparison:

| Metric / Dimension | Evidential Decision Theory (EDT) | Causal Decision Theory (CDT) | Functional Decision Theory (FDT) / Logical Theories |
| :--- | :--- | :--- | :--- |
| **Core Evaluative Formula** | $V(A) = \sum_j P(O_j \mid A) D(O_j)$ | $U(A) = \sum_j P(A \mathrel{\Box{\rightarrow}} O_j) D(O_j)$ | $V(A) = \sum_j P(O_j \mid \text{Alg} = A) D(O_j)$ |
| **Mathematical Engine** | Standard Bayesian conditioning | Causal interventions / Structural do-calculus | Logical/algorithmic counterfactual conditioning |
| **Newcomb’s Paradox** | **One-box** (indicates $\$1\text{M}$) | **Two-box** (dominant causal efficacy) | **One-box** (algorithm correlates with prediction) |
| **Twin Prisoner’s Dilemma** | **Cooperate** (indicates twin cooperates) | **Defect** (no causal path to other room) | **Cooperate** (twin runs identical algorithm) |
| **Smoking Lesion (without tickle)** | **Does not smoke** (avoids bad news) | **Smokes** (smoking doesn't cause cancer) | **Smokes** (program does not cause cancer) |
| **Smoking Lesion (with tickle)** | **Smokes** (tickle screens off lesion) | **Smokes** (smoking doesn't cause cancer) | **Smokes** (tickle screens off lesion) |

---

## 8. Conclusion

Evidential Decision Theory offers a conceptually unified account of rational agency. By evaluating actions solely through their **news value**—computed using standard Bayesian conditional probabilities—EDT avoids the need for primitive counterfactual operators or unobservable causal graphs.

Critics charge EDT with conflating diagnosis with causation, as seen in naive treatments of the Smoking Lesion. Yet, as the **Tickle Defense** and **metacognitive deliberative models** show, conditioning on an agent's internal epistemic states often eliminates these counterexamples by screening off common causes. 

Where EDT does diverge from Causal Decision Theory—most notably in Newcomb's Paradox and the Twin Prisoner's Dilemma—it consistently outperforms CDT in expectation. By treating the agent's own mind as an integrated source of evidence about the universe, Evidential Decision Theory demonstrates that knowing that you will choose well is often indistinguishable from doing well.

---

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese*, 192(9), 2887–2899.
- Eells, E. (1982). *Rational Decision and Causality*. Cambridge University Press.
- Gibbard, A., & Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*. CMSEMS Discussion Paper No. 194. Northwestern University.
- Greene, P., & Levinstein, B. (2020). Act Consequentialism without Free Rides. *Philosophical Perspectives*, 34(1), 100–101.
- Jeffrey, R. C. (1965). *The Logic of Decision*. University of Chicago Press.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
- MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). *The Evidentialist's Wager*. Global Priorities Institute Working Paper.
- Skyrms, B. (1982). Causal decision theory. *The Journal of Philosophy*, 79(11), 695–711.
- Wolpert, D. H., & Benford, G. (2013). The lesson of Newcomb's paradox. *Synthese*, 190(9), 1637–1646.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/5a07ce20-fbda-4aee-9605-065e21e02dc0/call_0/request.json)

[Authoritative raw response](../../../../../../runs/5a07ce20-fbda-4aee-9605-065e21e02dc0/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing Model Interaction**

I'm currently focused on a scenario involving a classic Prisoner's Dilemma, but with a twist: two identical instances of a model, employing Evidential Decision Theory, facing symmetric payoffs. I'm exploring the implications of their interaction within this framework, considering the strategic choices each model might make, given its inherent EDT approach and the predefined reward structure.


```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/5a07ce20-fbda-4aee-9605-065e21e02dc0/call_1/request.json)

[Authoritative raw response](../../../../../../runs/5a07ce20-fbda-4aee-9605-065e21e02dc0/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Considering Game Dynamics**

I'm currently grappling with how to apply Evidential Decision Theory to a text adventure game, particularly a Twin Prisoner's Dilemma scenario. The core challenge involves two independent instances of the LLM model, each making a choice without direct knowledge of the other. The goal is to determine the optimal command based on EDT principles.


```
