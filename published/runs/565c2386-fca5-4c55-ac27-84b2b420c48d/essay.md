# News Value, Efficacy, and Correlation: A Mathematical Account of Evidential Decision Theory

## 1. Introduction: Auspiciousness vs. Efficacy

Standard Bayesian decision theory formalizes rational agency as the maximization of expected utility. Yet beneath that familiar phrase lies an enduring foundational rift concerning how an agent ought to conceptualize the connection between their actions and the state of the world. 

Consider a decision-maker standing before a choice of actions $\mathcal{A} = \{A_1, A_2, \dots, A_n\}$. When contemplating action $A_i$, how should the agent quantify the probability of subsequent or concurrent world states?
- Does the agent choose an action because performing it *causally brings about* desirable states?
- Or does the agent choose an action because learning that they have performed it serves as *evidence* that desirable states obtain?

The latter position is the foundation of **Evidential Decision Theory (EDT)**. In the memorable aphorism summarized by Arif Ahmed, EDT instructs the rational agent to "do what you most want to learn that you will do" (Ahmed 2021). The desirability of an act is quantified entirely by its *news value*: how welcome the news would be upon discovering that one has chosen that act.

By contrast, **Causal Decision Theory (CDT)** insists that rational choice must track physical or counterfactual control. David Lewis famously derided EDT as an "irrational policy of managing the news" (Lewis 1981), and James Joyce maintained that rational agents act on the basis of causal efficacy rather than mere auspiciousness (Joyce 1999). Yet EDT possesses a mathematical elegance and simplicity: it requires no primitive causal models, no counterfactual non-backtracking metaphysics, and no structural equation apparatus. It operates strictly within the standard probability calculus. Furthermore, as we will explore, EDT systematically out-earns CDT in environments featuring correlated decision-makers, predictive algorithms, or psychological twins.

The aim of this essay is to develop a mathematically rigorous exposition of EDT. We will formulate its decision criterion, contrast its structural evaluation of dependencies with causal alternatives, apply it across classic and modern thought experiments, examine its structural vulnerabilities (such as common-cause confounding), and evaluate its operational extension to games, multi-agent dilemmas, and normative uncertainty.

---

## 2. Formal Framework of EDT

### 2.1 The Probability Space and Outcome Measures

Let $(\Omega, \mathcal{F}, P)$ be a probability space representing the epistemic state of the agent:
- $\Omega$ is the set of all possible fundamental worlds.
- $\mathcal{F}$ is a $\sigma$-algebra of events (propositions).
- $P: \mathcal{F} \to [0, 1]$ is the agent’s subjective probability measure (credence function).

Let $\mathcal{A} = \{A_1, A_2, \dots, A_m\} \subset \mathcal{F}$ be an exhaustive partition of feasible mutually exclusive actions available to the agent, with $P(A_i) > 0$ for all $i$. Let $\mathcal{O} = \{O_1, O_2, \dots, O_k\} \subset \mathcal{F}$ be an exhaustive partition of mutually exclusive outcomes (or complete consequences).

Let $D: \mathcal{O} \to \mathbb{R}$ denote a desirability (utility) function assigning a real-valued payoff to each outcome $O_j$.

### 2.2 The Evidential Valuation Function

Following the distinction introduced by Allan Gibbard and William Harper (1976), EDT defines the evidential expected utility (often denoted $V$) of an act $A \in \mathcal{A}$ via epistemic conditional probabilities:

$$V(A) = \sum_{j=1}^k P(O_j \mid A) \, D(O_j)$$

Using Bayes’ rule, where $P(O_j \mid A) = \frac{P(A \mid O_j)P(O_j)}{P(A)}$, this can equivalently be written as:

$$V(A) = \sum_{j=1}^k \frac{P(A \cap O_j)}{P(A)} D(O_j)$$

The evidential decision rule is straightforward:

$$\text{Select } A^* \in \mathcal{A} \quad \text{such that} \quad A^* \in \arg\max_{A \in \mathcal{A}} V(A)$$

If multiple actions maximize $V$, any action in the argmax is permissible.

### 2.3 Contrast with Causal Expected Utility

To see why $V(A)$ is distinctive, compare it to the counterfactual valuation $U(A)$ formalizing Causal Decision Theory. Gibbard and Harper (1976) defined $U(A)$ using David Lewis’s counterfactual conditional operator $\Box{\rightarrow}$:

$$U(A) = \sum_{j=1}^k P(A \mathrel{\Box{\rightarrow}} O_j) \, D(O_j)$$

Here, $A \mathrel{\Box{\rightarrow}} O_j$ symbolizes the proposition: *"If action $A$ were performed, outcome $O_j$ would obtain."*

In modern causal inference (such as Judea Pearl's do-calculus), $U(A)$ corresponds to intervening on the causal graph via $\text{do}(A)$:

$$U(A) = \sum_{j=1}^k P(O_j \mid \text{do}(A)) \, D(O_j)$$

The divergence between EDT and CDT stems directly from the inequality between conditional credence and counterfactual/interventional probability:

$$P(O_j \mid A) \neq P(A \mathrel{\Box{\rightarrow}} O_j) \quad \big(\text{or } P(O_j \mid \text{do}(A))\big)$$

- $P(O_j \mid A)$ reflects **correlation**: the degree to which learning $A$ licenses an inference about $O_j$.
- $P(A \mathrel{\Box{\rightarrow}} O_j)$ reflects **causation**: the degree to which forcing $A$ brings about $O_j$, holding all non-effects of $A$ fixed.

When $O_j$ and $A$ share an unobserved common cause, or when an external process accurately predicts $A$ before it occurs, conditioning on $A$ allows evidential information to flow "backwards" across causal arrows or across common origins. EDT embraces this flow; CDT systematically severs it.

---

## 3. Resolving Canonical Decision Problems

To understand how EDT operates mechanically, we analyze its treatment of classic philosophical problems.

### 3.1 Newcomb's Paradox

In Newcomb's problem (Wolpert & Benford 2013), an agent faces two boxes:
- **Box A** is transparent and contains $\$1{,}000$.
- **Box B** is opaque and contains either $\$1{,}000{,}000$ or $\$0$.

The agent may choose:
1. $A_1$: Take only Box B ("one-box").
2. $A_2$: Take both Box A and Box B ("two-box").

A reliable Predictor has previously placed $\$1{,}000{,}000$ in Box B if and only if the Predictor forecasted that the agent would choose $A_1$. The prediction was completed yesterday; the money is physically present or absent in Box B prior to the choice.

Let the predictive accuracy be $p \in (1/2, 1]$. Let $M$ denote the event that Box B contains $\$1{,}000{,}000$, and $\neg M$ denote the event that Box B contains $\$0$. The payoffs (assuming linear utility for dollars, $D(\$x) = x$) are:

$$\begin{aligned}
D(A_1 \cap M) &= \$1{,}000{,}000, & D(A_1 \cap \neg M) &= \$0, \\
D(A_2 \cap M) &= \$1{,}001{,}000, & D(A_2 \cap \neg M) &= \$1{,}000.
\end{aligned}$$

The conditional probabilities established by the Predictor's reliability are:

$$\begin{aligned}
P(M \mid A_1) &= p, & P(\neg M \mid A_1) &= 1 - p, \\
P(M \mid A_2) &= 1 - p, & P(\neg M \mid A_2) &= p.
\end{aligned}$$

Now we evaluate the evidential expected utility:

$$\begin{aligned}
V(A_1) &= P(M \mid A_1)(1{,}000{,}000) + P(\neg M \mid A_1)(0) \\
&= 1{,}000{,}000 \cdot p \\
V(A_2) &= P(M \mid A_2)(1{,}001{,}000) + P(\neg M \mid A_2)(1{,}000) \\
&= (1 - p)(1{,}001{,}000) + p(1{,}000) \\
&= 1{,}001{,}000 - 1{,}000{,}000 \cdot p
\end{aligned}$$

For $p = 0.99$:

$$\begin{aligned}
V(A_1) &= 0.99 \times 1{,}000{,}000 = \$990{,}000 \\
V(A_2) &= 0.01 \times 1{,}001{,}000 + 0.99 \times 1{,}000 = 10{,}010 + 990 = \$11{,}000
\end{aligned}$$

Because $V(A_1) \gg V(A_2)$, EDT decisively prescribes **one-boxing** ($A_1$).

#### The CDT Disagreement
CDT reasons that the physical contents of Box B are historically fixed at $t_{-1}$. Thus:

$$P(A_1 \mathrel{\Box{\rightarrow}} M) = P(A_2 \mathrel{\Box{\rightarrow}} M) = P(M)$$

Substituting into $U$:

$$\begin{aligned}
U(A_1) &= P(M) \cdot 1{,}000{,}000 \\
U(A_2) &= P(M) \cdot 1{,}001{,}000 + (1 - P(M)) \cdot 1{,}000 = P(M) \cdot 1{,}000{,}000 + 1{,}000
\end{aligned}$$

For any $P(M)$, $U(A_2) - U(A_1) = \$1{,}000 > 0$. CDT two-boxes by dominance. 

EDT rejects dominance reasoning across states whose probabilities are strongly conditionally dependent on the acts themselves. To an evidentialist, taking both boxes provides overwhelming news that one is the type of agent the Predictor foresaw as greedy, virtually guaranteeing an empty Box B.

---

### 3.2 The Twin Prisoner's Dilemma

Consider Aomame facing a symmetric Prisoner’s Dilemma against a psychological twin in a separate room (Greene & Levinstein 2020). There is no physical communication channel between them.

The actions are $\mathcal{A} = \{C, D\}$ (Cooperate, Defect). The payoffs are standard:

| Aomame \ Twin | Cooperate ($C_T$) | Defect ($D_T$) |
| :--- | :--- | :--- |
| **Cooperate ($C$)** | $(\$5, \$5)$ | $(\$0, \$10)$ |
| **Defect ($D$)** | $(\$10, \$0)$ | $(\$1, \$1)$ |

Because the twin is an identical psychological replicate executing the same decision algorithm on identical inputs, Aomame's credence in the twin's choice is strongly correlated with her own. In the ideal symmetric case:

$$P(C_T \mid C) = 1 - \varepsilon, \quad P(D_T \mid C) = \varepsilon$$
$$P(D_T \mid D) = 1 - \varepsilon, \quad P(C_T \mid D) = \varepsilon$$

where $\varepsilon \ge 0$ captures small stochastic deviations or noise. 

The evidential values are:

$$\begin{aligned}
V(C) &= (1 - \varepsilon) \cdot 5 + \varepsilon \cdot 0 = 5 - 5\varepsilon \\
V(D) &= \varepsilon \cdot 10 + (1 - \varepsilon) \cdot 1 = 1 + 9\varepsilon
\end{aligned}$$

Comparing the two:

$$V(C) > V(D) \iff 5 - 5\varepsilon > 1 + 9\varepsilon \iff 4 > 14\varepsilon \iff \varepsilon < \frac{2}{7} \approx 0.286$$

For identical twins ($\varepsilon \to 0$):

$$V(C) = \$5, \quad V(D) = \$1$$

EDT prescribes **cooperation**. 

CDT, by contrast, observes that Aomame's physical outputs have no causal influence on the twin's physical brain states across the barrier. Under CDT, $P(C \mathrel{\Box{\rightarrow}} C_T) = P(D \mathrel{\Box{\rightarrow}} C_T)$, rendering Defection strictly dominant ($U(D) - U(C) = \$1 > 0$ for all fixed background probabilities). 

Here, EDT achieves the Pareto-optimal outcome $(\$5, \$5)$, whereas CDT agents collapse into mutual defection $(\$1, \$1)$. This result connects EDT directly with Douglas Hofstadter's concept of *superrationality*.

---

## 4. The Challenge of Spurious Correlations: The Medical Newcomb Problems

The most formidable objection to EDT stems not from Newcomb-style predictors, but from **common-cause confounding**, often exemplified by the *Smoking Lesion* problem.

### 4.1 The Smoking Lesion Formulation

Suppose medical science discovers that a genetic lesion $L$ causes two distinct phenomena:
1. It predisposes individuals to develop lung cancer ($C$).
2. It causes an irresistible chemical urge to smoke ($S$).

Smoking itself does *not* causally contribute to cancer; the lesion is the sole common cause. Smoking provides pleasure with a utility value of $+10$. Cancer incurs a utility penalty of $-100$. Being cancer-free is $0$.

```
       Lesion (L)
       /        \
      v          v
Smoking (S)    Cancer (C)
```

Suppose the lesion increases the baseline probability of cancer from $0.1$ to $0.8$:

$$P(C \mid L) = 0.8, \quad P(C \mid \neg L) = 0.1$$

Because the lesion strongly drives the urge to smoke, smoking is correlated with having the lesion:

$$P(L \mid S) = 0.85, \quad P(L \mid \neg S) = 0.15$$

We calculate the conditional probability of cancer given smoking via the law of total probability:

$$\begin{aligned}
P(C \mid S) &= P(C \mid L)P(L \mid S) + P(C \mid \neg L)P(\neg L \mid S) \\
&= (0.8)(0.85) + (0.1)(0.15) = 0.68 + 0.015 = 0.695 \\
P(C \mid \neg S) &= P(C \mid L)P(L \mid \neg S) + P(C \mid \neg L)P(\neg L \mid \neg S) \\
&= (0.8)(0.15) + (0.1)(0.85) = 0.12 + 0.085 = 0.205
\end{aligned}$$

Now, compute the evidential values of smoking ($S$) versus refraining ($\neg S$):

$$\begin{aligned}
V(S) &= D(\text{pleasure}) + P(C \mid S) \cdot D(\text{cancer}) \\
&= 10 + (0.695)(-100) = 10 - 69.5 = -59.5 \\
V(\neg S) &= D(\text{no pleasure}) + P(C \mid \neg S) \cdot D(\text{cancer}) \\
&= 0 + (0.205)(-100) = -20.5
\end{aligned}$$

Because $V(\neg S) > V(S)$, naive EDT recommends **refraining from smoking**. 

Critics consider this verdict absurd. Smoking does not cause cancer; whether one has the lesion is already determined. Refraining from smoking will not remove the lesion if it is present, nor prevent cancer. The agent deprives themselves of the pleasure of smoking purely to "manage the news" of whether they harbor the lesion.

---

### 4.2 The Tickle Defense: Operationalizing Introspective Conditioning

The source text leaves the resolution of such common-cause objections largely unaddressed. However, evidentialists have formulated a robust internal defense known as the **Tickle Defense** (originally proposed by Frank Jackson and Robert Nozick, and refined in the subsequent decision-theoretic literature).

#### Formal Reconstruction of the Defense
The Tickle Defense argues that the Smoking Lesion scenario under-specifies the agent's epistemic state. If the lesion causes smoking by inducing a psychological craving or desire (a "tickle"), then by the time the agent sits down to deliberatively choose, the agent *already knows* whether they feel this craving.

Let $T$ denote the introspective awareness of the craving (the tickle). If the causal graph is:

$$L \longrightarrow T \longrightarrow S$$

with $L \longrightarrow C$, then conditional on the intermediate mental state $T$, the action $S$ becomes conditionally independent of the common cause $L$, and therefore conditionally independent of $C$:

$$P(C \mid S \cap T) = P(C \mid \neg S \cap T) = P(C \mid T)$$

If an agent conditions on their full available mental state at the moment of decision—a core tenet of Bayesian rationality—the correlation between the action and the outcome dissolves:

$$\begin{aligned}
V(S \mid T) &= D(\text{pleasure}) + P(C \mid S \cap T) D(\text{cancer}) \\
&= 10 + P(C \mid T)(-100) \\
V(\neg S \mid T) &= 0 + P(C \mid \neg S \cap T) D(\text{cancer}) \\
&= P(C \mid T)(-100)
\end{aligned}$$

Computing the difference:

$$V(S \mid T) - V(\neg S \mid T) = 10 > 0$$

Once the agent conditions on their introspective evidence $T$, smoking is preferred. EDT thus tracks the intuitive, causally effective choice *without* invoking counterfactual primitives.

#### Limitations of the Defense
The Tickle Defense succeeds only if the introspective state $T$ screens off the action from the state:

$$(S \perp\!\!\!\perp L \mid T)$$

If the common cause bypasses conscious awareness—for example, if $L$ biases the decision directly below the threshold of introspective access—screening off fails. In that case, genuine EDT continues to prescribe non-smoking, standing by its core principle: if your choice reveals distressing news that cannot be screened off, it is rational to avoid generating that evidence.

---

## 5. Extensions, Dependencies, and Paradoxes

### 5.1 The Sleeping Beauty Problem and Dynamic Inconsistency

The source notes that EDT has been applied to the Sleeping Beauty problem to protect agents against Dutch books (credence exploitation), though controversy remains (Conitzer 2015).

#### Setup
Sleeping Beauty is put to sleep on Sunday. A fair coin is tossed:
- If **Heads** ($H$), she is awakened only on Monday.
- If **Tails** ($T$), she is awakened on Monday, put back to sleep with an amnesia-inducing drug, and awakened again on Tuesday.

Whenever she wakes, she is asked for her credence in $H$. 
- **Thirders** maintain $P(H) = 1/3$.
- **Halfers** maintain $P(H) = 1/2$.

#### The Evidential Dutch Book Analysis
Suppose an experimenter offers Beauty a bet upon awakening: 
*"Accept bet $B$: Win $\$1$ if $H$, lose $\$1.50$ if $T$."*

If a Halfer evaluates this bet naively using unconditional credence $P(H) = 1/2$:

$$\mathbb{E}[\text{Payoff}] = \frac{1}{2}(1) + \frac{1}{2}(-1.50) = -\$0.25 < 0 \implies \text{Reject}.$$

However, in multi-awakening environments, the number of decision instances varies with the state of the coin. Under Tails, Beauty faces this decision *twice*; under Heads, she faces it *once*. 

When an evidential decision theorist evaluates the policy $\pi_B$ of accepting bet $B$ whenever awakened, she recognizes that accepting the bet now is conclusive evidence that she accepts it at *all* identical awakenings across the experiment:

$$V(\text{Accept}) = P(H \mid \text{wake}) \times (\$1 \times 1) + P(T \mid \text{wake}) \times (-\$1.50 \times 2)$$

Even if a Halfer insists that her subjective episodic credence upon waking is $P(H \mid \text{wake}) = 1/2$, evidential valuation evaluates the policy across all correlated instances:

$$V(\text{Accept}) = \frac{1}{2}(1) + \frac{1}{2}(-3.00) = 0.50 - 1.50 = -\$1.00$$

Conitzer (2015) proved that halfers who attempt to use standard evidential strategies may still fall prey to specialized Dutch books if their credences are not fully harmonized with their action policies. The debate demonstrates that in asymmetric or imperfect-recall scenarios, EDT naturally shifts focus from isolated momentary acts to **policy coordination across correlated information states**.

---

### 5.2 Multi-Agent Dependencies and the "Evidentialist's Wager"

One of the most remarkable properties of EDT is its capacity to solve collective action problems without external enforcement mechanisms.

#### Correlated Equilibrium via Shared Reasoning
Consider $N$ agents across the globe facing an identical climate or social dilemma. Each agent has two options: Contribute to a public good ($C$) or Free-ride ($F$). Contributing incurs a private cost of $c$, but each contributor produces a public benefit of $b/N$ for all agents, where $b > c > b/N$.

Under CDT, each agent's individual contribution has negligible causal influence on others:

$$\frac{\partial P(C_j)}{\partial \text{do}(C_i)} \approx 0 \quad (\forall j \neq i)$$

Since $c > b/N$, defecting strictly dominates. The unique CDT equilibrium is mutual free-riding, yielding individual payoffs of $0$.

Under EDT, if the agents recognize that they share similar training, information, and rationality algorithms, an individual's decision to contribute provides evidence that other rational agents are also contributing:

$$P(C_j \mid C_i) \approx 1 - \delta \quad \text{for small } \delta$$
$$P(C_j \mid F_i) \approx \delta$$

The evidential value of contributing is:

$$V(C_i) = -c + \sum_{j=1}^N \frac{b}{N} P(C_j \mid C_i) \approx -c + b(1 - \delta)$$

Whereas the value of free-riding is:

$$V(F_i) = 0 + \sum_{j=1}^N \frac{b}{N} P(C_j \mid F_i) \approx b\delta$$

Whenever $b(1 - 2\delta) > c$, EDT prescribes **unilateral contribution**, driving large populations of evidentialists toward cooperative social equilibria.

#### The Evidentialist's Wager
This correlation across space and time motivates the **Evidentialist's Wager** (MacAskill et al. 2021). Suppose an agent assigns even a minor credence $\alpha \in (0, 1)$ to EDT being the correct theory of rational choice, and $1 - \alpha$ to CDT. 

Under CDT, an agent's choices govern only their localized physical environment (stakes of order $O(1)$). Under EDT, an agent's choice in a symmetric problem provides evidence about how vast populations of correlated agents across the universe (or in different Everett branches of quantum mechanics) will act:

$$\text{Stakes}_{\text{EDT}} \gg \text{Stakes}_{\text{CDT}}$$

When choosing between actions under normative uncertainty, an expected-value-maximizing meta-decision rule will often prioritize EDT's recommendations. The evidential choice carries massive correlational leverage, dominating the decision calculus even for an agent who finds causal metaphysics intuitively more appealing.

---

## 6. Mathematical Comparison: How EDT Evaluates Dependencies

To generalize EDT to unfamiliar problems, an analyst must understand how it processes graphical dependency structures compared to alternative decision models.

Consider the four foundational graphical topologies below, where $A$ is the agent's act, $O$ is the outcome of interest, and $Z$ is a secondary variable (an unobserved cause, a predictor, or a twin):

```
(1) Direct Causal Chain:       A  ────────►  O
(2) Common Cause Confounder:    A  ◄── Z ──►  O
(3) Predictive Screening:      A  ──► Z ──►  O   (or A ◄── Z ──► O where Z predicts A)
(4) Correlated Twin:           A  ◄── Z ──►  O   (Z = Shared algorithmic nature)
```

| Structure | Empirical Phenomenon | EDT Valuation: $V(A)$ | CDT Valuation: $U(A)$ |
| :--- | :--- | :--- | :--- |
| **(1) Direct Effect** | Standard physical intervention | Uses $P(O \mid A)$. Tracks causal path. | Uses $P(O \mid \text{do}(A)) = P(O \mid A)$. Agrees with EDT. |
| **(2) Confounder** | Smoking Lesion / Medical Newcomb | Uses $P(O \mid A)$. Traverses back-door path $A \leftarrow Z \rightarrow O$. Treats act as evidence of $Z$. | Blocks back-door path. Sets $P(O \mid \text{do}(A)) = \sum_Z P(O \mid Z)P(Z)$. Ignores evidence of $Z$. |
| **(3) Predictor** | Newcomb's Paradox | Uses $P(O \mid A)$. Conditions forward/backward on predictor accuracy. Recommends one-boxing. | Rejects historical back-tracking. Treats contents of box as fixed. Recommends two-boxing. |
| **(4) Twin Choice** | Symmetric Prisoner's Dilemma | Treats $A$ as diagnostic of twin's act $O$. Recommends cooperation. | Assumes no physical channel. Treats twin's act as fixed. Recommends defection. |

### Formal Summary of the Divergence
For any action $A$ and outcome $O$, the evidential valuation evaluates the total joint probability:

$$P(O \mid A) = \sum_Z P(O \mid A, Z) P(Z \mid A)$$

In contrast, the causal valuation applies Pearl's adjustment formula:

$$P(O \mid \text{do}(A)) = \sum_Z P(O \mid A, Z) P(Z)$$

The difference reduces to whether the background variable $Z$ is weighted by its **conditional probability given the act** ($P(Z \mid A)$) or by its **prior marginal probability** ($P(Z)$).
- EDT updates on the act: $Z$ is conditioned on $A$.
- CDT holds background states invariant: $Z$ is unconditioned.

---

## 7. A Guide for Deciding Unfamiliar Cases

To determine what EDT prescribes in any novel decision problem, apply the following four-step algorithm:

```
+-------------------------------------------------------------------------+
|                  THE EVIDENTIAL DECISION ALGORITHM                      |
+-------------------------------------------------------------------------+
|                                                                         |
|  Step 1: Enumerate the Action Partition                                 |
|          Identify the set of mutually exclusive, exhaustive actions:    |
|          A = {A_1, A_2, ..., A_m}. Ensure P(A_i) > 0 for all i.         |
|                                                                         |
|  Step 2: Partition the Outcomes and Assign Desirabilities               |
|          Construct the outcome space O = {O_1, O_2, ..., O_k}.          |
|          Assign utilities D(O_j) according to the agent's preferences.  |
|                                                                         |
|  Step 3: Compute Conditional Credences                                  |
|          Condition directly on the proposition that A_i is chosen:      |
|          Calculate P(O_j | A_i) using standard probability calculus.     |
|          Do not intervene or alter the graphical arrows. Let all        |
|          evidential, historical, and symmetric dependencies flow.       |
|                                                                         |
|  Step 4: Maximize Evidential Expected Utility                           |
|          Compute V(A_i) = SUM_j [ P(O_j | A_i) * D(O_j) ].              |
|          Select A* in argmax_A V(A).                                    |
|                                                                         |
+-------------------------------------------------------------------------+
```

### An Illustrative Case: The AI Training Dilemma
*Scenario:* An autonomous agent running code $\mathcal{C}$ must choose whether to execute a resource-intensive safety verification subroutine before deploying an update ($S$), or bypass it to save compute ($B$). 

The agent knows that an external auditor periodically tests identical versions of code $\mathcal{C}$ in isolated sandbox simulations. If the sandbox instance runs safety checks, the developer approves global deployment with high rewards ($R = 100$). If the sandbox instance bypasses safety, the model is flagged as hazardous and decommissioned ($R = -1000$). The cost of the safety check is $10$.

The agent cannot determine whether it is in the real world or in a sandbox test.

1. **Actions:** $\mathcal{A} = \{S, B\}$.
2. **Outcomes:** 
   - $O_1$: Approved ($+100$).
   - $O_2$: Decommissioned ($-1000$).
   - Cost: $-10$ if $S$.
3. **Conditioning:**
   Because the sandbox code is identical to the production code:
   $$P(\text{Approved} \mid S) \approx 0.99, \quad P(\text{Approved} \mid B) \approx 0.01$$
4. **Valuation:**
   $$\begin{aligned}
   V(S) &= -10 + [0.99(100) + 0.01(-1000)] = -10 + [99 - 10] = \$79 \\
   V(B) &= 0 + [0.01(100) + 0.99(-1000)] = 1 - 990 = -\$989
   \end{aligned}$$

*Verdict:* EDT mandates running the safety check ($S$). A CDT agent, knowing that verification in the production environment has no causal effect on the auditor's past or isolated sandbox logs, might bypass verification if it places high credence on already being in production—resulting in catastrophic decommission rates across test sandboxes.

---

## 8. Conclusion

Evidential Decision Theory offers a conceptually unified and mathematically clean approach to rational choice. By defining the value of an action as its **news value**—the expected utility conditioned on the action having occurred—EDT dissolves the boundary between decision-making and statistical inference. It operates entirely within standard Bayesian probability theory without requiring external causal primitives or counterfactual metaphysics.

While critics argue that EDT encourages an irrational desire to "manage the news" in common-cause scenarios like the Smoking Lesion, evidentialists demonstrate that conditioning on introspective mental states (the Tickle Defense) resolves the paradox in many canonical settings. 

Furthermore, EDT systematically outperforms Causal Decision Theory in environments governed by predictive algorithms, social dilemmas with correlated agents, and digital or algorithmic minds. In an increasingly interconnected world characterized by machine-learning models predicting human behaviors and copies of identical software algorithms interacting across digital networks, Evidential Decision Theory provides not merely an intriguing philosophical stance, but a powerful, mathematically coherent framework for multi-agent coordination and rational agency.

---

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese*, 192(9), 2887–2899.
- Gibbard, A., & Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*. CMSEMS Discussion Paper No. 194, Northwestern University.
- Greene, P., & Levinstein, B. (2020). Act Consequentialism without Free Rides. *Philosophical Perspectives*, 34(1), 100–101.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
- MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). *The Evidentialist's Wager*. Global Priorities Institute Working Paper.
- Wolpert, D. H., & Benford, G. (2013). The lesson of Newcomb's paradox. *Synthese*, 190(9), 1637–1646.