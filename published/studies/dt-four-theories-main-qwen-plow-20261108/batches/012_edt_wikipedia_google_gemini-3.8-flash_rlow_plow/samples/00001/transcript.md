# 012_edt_wikipedia_google_gemini-3.8-flash_rlow_plow / 00001

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/6e6b4638-4653-49d5-b420-e9dcc28e1989/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/6e6b4638-4653-49d5-b420-e9dcc28e1989/call_0/response.raw) · finish: `stop`

### Visible response

````text
# The Geometry of News Value: A Mathematical Account of Evidential Decision Theory

## 1. Introduction: Auspiciousness vs. Efficacy

Standard Bayesian decision analysis directs an agent to choose an action that maximizes subjective expected utility. Yet beneath this familiar imperative lies an ontological divide concerning what an action *does* versus what an action *reveals*. 

Consider the classic formulation framed by Arif Ahmed: rational choice can be viewed as an instruction to "do what you most want to learn that you will do" (Ahmed 2021). This principle defines **Evidential Decision Theory (EDT)**. Under EDT, an action is not treated merely as a physical lever altering a downstream causal graph. Rather, an action is an event within the agent’s own probability space. Choosing an act provides the agent with new conditional evidence about the state of the world—including factors outside the agent's causal reach.

This perspective stands in sharp contrast to **Causal Decision Theory (CDT)**. Formalized by Allan Gibbard and William Harper (1976), David Lewis (1981), and James M. Joyce (1999), CDT insists that rational choices must be evaluated strictly by their *causal efficacy*—their capacity to bring about desirable states via physical production—rather than by their mere *auspiciousness* (news value). Joyce famously objected:

> "Rational agents choose acts on the basis of their *causal efficacy*, not their auspiciousness; they act to *bring about* good results even when doing so might betoken bad news." (Joyce 1999, p. 146)

Lewis was even more unsparing, branding EDT an "irrational policy of managing the news" (Lewis 1981).

Despite these critiques, EDT remains a foundational pillar of modern decision theory. It formalizes intuitive reasoning in cooperative dilemmas involving symmetric agents, underpins radical approaches to coordination, and commands serious attention in debates over anthropic reasoning and decision-theoretic wagers.

This essay develops a formal, self-contained mathematical framework for EDT. It clarifies how EDT evaluates acts and policies, contrasts its mechanics with CDT, analyzes canonical problems such as Newcomb's Paradox and the Twin Prisoner's Dilemma, and addresses the technical ambiguities that arise when conditioning on one's own voluntary choices.

---

## 2. Formal Foundations

### 2.1 Probability Space and Conditional Value

Let $(\Omega, \mathcal{F}, P)$ be a probability space representing an agent’s epistemic state:
- $\Omega$ is the set of possible worlds.
- $\mathcal{F}$ is a $\sigma$-algebra of events over $\Omega$.
- $P: \mathcal{F} \to [0, 1]$ is the agent’s subjective prior probability measure.

Let $\mathcal{A} = \{A_1, A_2, \dots, A_m\} \subset \mathcal{F}$ be a finite, mutually exclusive and exhaustive set of candidate acts available to the agent at a given decision juncture:
$$\bigcup_{i=1}^m A_i = \Omega \quad \text{and} \quad A_i \cap A_k = \emptyset \quad \forall i \neq k.$$

Let $\mathcal{O} = \{O_1, O_2, \dots, O_n\} \subset \mathcal{F}$ be a partition of mutually exclusive and exhaustive ultimate outcomes, where each $O_j$ is sufficiently specified to fix all evaluative facts of interest. The agent’s evaluative preferences are encoded by a utility (or desirability) function:
$$D: \mathcal{O} \to \mathbb{R}.$$

In this standard discrete setting, the **evidential expected utility** (often called the **conditional value** or **news value**) of an action $A \in \mathcal{A}$ is defined as:

$$V(A) \coloneqq \sum_{j=1}^n P(O_j \mid A) D(O_j)$$

where $P(O_j \mid A)$ denotes the elementary conditional probability:
$$P(O_j \mid A) = \frac{P(O_j \cap A)}{P(A)}, \quad \text{provided } P(A) > 0.$$

If $D$ is extended to arbitrary propositions $X \in \mathcal{F}$ with $P(X) > 0$, we have Richard Jeffrey’s desirability measure:
$$V(X) = \sum_{j} P(O_j \mid X) D(O_j).$$

The normative prescription of EDT is straightforward:

$$\text{Prescription (EDT): Select an act } A^* \in \mathcal{A} \text{ such that } A^* \in \arg\max_{A \in \mathcal{A}} V(A).$$

---

### 2.2 EDT vs. CDT: The Counterfactual Divergence

The formal gulf between EDT and CDT lies entirely in the probability measure assigned to outcomes when an action is hypothetically adopted. Gibbard and Harper (1976) made this distinction explicit by comparing conditional probability to counterfactual conditionals.

Let $A \mathrel{\Box\kern-1.5pt\rightarrow} O_j$ denote the Lewis-Stalnaker counterfactual proposition: *"If action $A$ were chosen, outcome $O_j$ would obtain."* CDT computes the **causal expected utility** $U(A)$ by weighting utilities by the probability of these counterfactuals:

$$U(A) \coloneqq \sum_{j=1}^n P(A \mathrel{\Box\kern-1.5pt\rightarrow} O_j) D(O_j).$$

Under standard causal modeling (e.g., Pearl’s do-calculus), $P(A \mathrel{\Box\kern-1.5pt\rightarrow} O_j)$ corresponds to the interventional probability distribution:
$$P(O_j \mid \operatorname{do}(A)).$$

The mathematical discrepancy between EDT and CDT reduces to the failure of the conditional probability to match the counterfactual probability:
$$P(O_j \mid A) \neq P(A \mathrel{\Box\kern-1.5pt\rightarrow} O_j) \iff P(O_j \mid A) \neq P(O_j \mid \operatorname{do}(A)).$$

- **CDT isolates direct causal production**: The intervention operator $\operatorname{do}(A)$ severs all incoming causal edges into $A$, evaluating $O_j$ only down directed paths from $A$.
- **EDT incorporates holistic belief revision**: Conditioning on $A$ propagates evidence in all directions—both down causal pathways (effects) and up incoming arrows (common causes and correlated external predictors).

---

## 3. Canonical Applications

### 3.1 Newcomb's Paradox

The definitive battleground between EDT and CDT is Newcomb's Paradox.

#### Problem Setup
- **Box A** is transparent and contains $\$1,000$.
- **Box B** is opaque and contains either $\$1,000,000$ or $\$0$.
- A predictor of exceptional reliability (accuracy parameter $q \in (1/2, 1]$, often set to $q = 0.99$) observed the agent prior to the choice:
  - If the predictor forecasted that the agent would take **only Box B** (act $A_1$, "one-boxing"), the predictor placed $\$1,000,000$ in Box B.
  - If the predictor forecasted that the agent would take **both Box A and Box B** (act $A_2$, "two-boxing"), the predictor placed $\$0$ in Box B.
- The contents of Box B are physically determined and locked in place *before* the agent chooses. The agent’s physical action exerts no backward causal influence on the predictor’s historical placement.

```
          [ Predictor's Past Prediction ]
                 /              \
     (predicts choice)     (sets content)
               v                  v
       [ Agent's Choice ]    [ State of Box B ]
               \                  /
                v                v
                  [ Final Payoff ]
```

#### Formal Evaluation under EDT
Let the unknown states of the world be:
- $S_1$: Box B contains $\$1,000,000$.
- $S_0$: Box B contains $\$0$.

Let the actions be:
- $A_1$: Take only Box B.
- $A_2$: Take both boxes.

Assuming linear utility in dollars ($D(\$x) = x$), the outcome payoffs are:
- $(A_1, S_1) \implies \$1,000,000$
- $(A_1, S_0) \implies \$0$
- $(A_2, S_1) \implies \$1,001,000$
- $(A_2, S_0) \implies \$1,000$

The predictor’s symmetric predictive competence is parametrized by:
$$P(S_1 \mid A_1) = q, \quad P(S_0 \mid A_1) = 1 - q$$
$$P(S_0 \mid A_2) = q, \quad P(S_1 \mid A_2) = 1 - q.$$

Applying EDT:
$$\begin{aligned}
V(A_1) &= P(S_1 \mid A_1) \cdot 1{,}000{,}000 + P(S_0 \mid A_1) \cdot 0 \\
       &= q \cdot 1{,}000{,}000.
\end{aligned}$$

$$\begin{aligned}
V(A_2) &= P(S_1 \mid A_2) \cdot 1{,}001{,}000 + P(S_0 \mid A_2) \cdot 1{,}000 \\
       &= (1 - q) \cdot 1{,}001{,}000 + q \cdot 1{,}000 \\
       &= 1{,}001{,}000 - q \cdot 1{,}000{,}000.
\end{aligned}$$

Comparing $V(A_1)$ and $V(A_2)$:
$$V(A_1) - V(A_2) = 2q \cdot 1{,}000{,}000 - 1{,}001{,}000.$$

Thus, EDT prescribes $A_1$ (one-boxing) whenever:
$$q > \frac{1{,}001{,}000}{2{,}000{,}000} = 0.5005.$$

For $q = 0.99$:
$$V(A_1) = 0.99 \times \$1,000,000 = \$990,000$$
$$V(A_2) = 0.01 \times \$1,001,000 + 0.99 \times \$1,000 = \$10,010 + \$990 = \$11,000.$$

Because $V(A_1) \gg V(A_2)$, **EDT decisively prescribes taking only Box B**. 

#### The CDT Contrast
Under CDT, Box B's contents are causally fixed in the past:
$$P(A_1 \mathrel{\Box\kern-1.5pt\rightarrow} S_1) = P(A_2 \mathrel{\Box\kern-1.5pt\rightarrow} S_1) = P(S_1).$$

Therefore:
$$\begin{aligned}
U(A_1) &= P(S_1) \cdot 1{,}000{,}000 + (1 - P(S_1)) \cdot 0 = P(S_1) \cdot 1{,}000{,}000 \\
U(A_2) &= P(S_1) \cdot 1{,}001{,}000 + (1 - P(S_1)) \cdot 1{,}000 = P(S_1) \cdot 1{,}000{,}000 + 1{,}000.
\end{aligned}$$

Because $U(A_2) - U(A_1) = 1{,}000 > 0$ for all prior values of $P(S_1)$, CDT insists on two-boxing by dominance. 

EDT rejects this dominance reasoning. In EDT, states are not epistemically independent of acts: learning that $A_2$ occurred is near-conclusive evidence that one is in state $S_0$.

---

### 3.2 The Twin Prisoner's Dilemma

A parallel divergence emerges in strategic games among symmetric agents, such as the Twin Prisoner's Dilemma (Greene and Levinstein 2020).

#### Problem Setup
- Two players, Agent 1 ($I$) and Agent 2 ($II$), face a Prisoner's Dilemma with payoff matrix:
  $$\begin{array}{c|cc}
  & C & D \\
  \hline
  C & (R, R) & (S, T) \\
  D & (T, S) & (P, P)
  \end{array}$$
  where $T > R > P > S$ (e.g., $T = 10, R = 5, P = 1, S = 0$).
- The players are psychological twins: their cognitive architecture and deliberative heuristics are identical. While isolated in separate rooms with no communication channel, their choices are strongly correlated.

#### Formal Evaluation under EDT
Let $C_I, D_I$ be Agent 1's acts, and $C_{II}, D_{II}$ be Agent 2's acts. The epistemic correlation between their decisions can be parameterized by $\rho \in [0, 1]$:
$$P(C_{II} \mid C_I) = \rho + (1 - \rho) P(C_{II}), \quad P(D_{II} \mid D_I) = \rho + (1 - \rho) P(D_{II}).$$

In the idealized limit of identical deterministic reasoning, $\rho = 1$, giving:
$$P(C_{II} \mid C_I) = 1, \quad P(D_{II} \mid C_I) = 0$$
$$P(D_{II} \mid D_I) = 1, \quad P(C_{II} \mid D_I) = 0.$$

Computing conditional values for Agent 1:
$$\begin{aligned}
V(C_I) &= P(C_{II} \mid C_I) \cdot R + P(D_{II} \mid C_I) \cdot S = 1 \cdot 5 + 0 \cdot 0 = 5 \\
V(D_I) &= P(C_{II} \mid D_I) \cdot T + P(D_{II} \mid D_I) \cdot P = 0 \cdot 10 + 1 \cdot 1 = 1.
\end{aligned}$$

Because $V(C_I) > V(D_I)$, **EDT recommends cooperation**. 

In general, cooperation dominates whenever:
$$\rho R + (1 - \rho)[P(C_{II}) R + P(D_{II}) S] > \rho P + (1 - \rho)[P(C_{II}) T + P(D_{II}) P].$$

For $\rho \to 1$, this simplifies directly to $R > P$, bypassing the classic defect-defect trap.

CDT agents, observing that their twin's action is causally disconnected from their own physical arm movements ($P(C_{II} \mid \operatorname{do}(C_I)) = P(C_{II})$), reason that defection strictly dominates. As a result, two CDT twins achieve payoff $P = 1$, whereas two EDT twins walk away with $R = 5$.

---

## 4. Foundational and Mathematical Challenges

While EDT achieves superior outcomes in Newcombian environments, it introduces subtle technical and philosophical complications.

### 4.1 The Problem of Zero Credence and Self-Predictive Probabilities

The standard definition of evidential expected utility:
$$V(A) = \sum_{j=1}^n P(O_j \mid A) D(O_j)$$
presupposes that $P(A) > 0$. If an agent believes an act is impossible or assigns it zero prior credence, conditional probability via Bayes' rule:
$$P(O_j \mid A) = \frac{P(O_j \cap A)}{P(A)}$$
is undefined.

More deeply, how can a deliberating agent assign a well-defined probability $P(A)$ to an act while currently deciding whether to choose it? 

#### Resolving the Deliberative Credence Problem
In decision-theoretic literature, some philosophers argue that deliberation crowds out prediction: an agent cannot coherently deliberate between $A_1$ and $A_2$ while already assigning fixed non-extremal credences to choosing them.

If this view holds, how does EDT function? A mathematically standard resolution treats the probability measure $P$ as an epistemic state over the Cartesian space of nature, common causes, and internal deliberation traces. To operationalize $P(A)$, we can model deliberation using an exploratory policy perturbation:

$$\text{Assume an } \varepsilon\text{-soft exploration policy: } P(A_i) \ge \varepsilon > 0 \quad \forall i.$$

Alternatively, we can formalize conditional probabilities using **Rényi conditional probability algebras** or **Popper functions**, wherein $P(\cdot \mid A)$ is treated as a primitive two-place operator defined for all non-empty candidate options, including those with zero unconditional probability.

---

### 4.2 Spurious Correlations: The Common-Cause Problem and the "Tickle Defense"

The most prominent critique of EDT is its vulnerability to common causes, often illustrated by the **Smoking Lesion Hypothesis**:
- Suppose a genetic lesion $L$ causes both lung cancer ($C$) and a strong psychological craving to smoke ($S$).
- Smoking itself does not causally produce cancer; cancer is driven entirely by $L$.
- Thus, smoking is correlated with cancer through an upstream common cause:

```
           [ Genetic Lesion (L) ]
                 /        \
       (causes) /          \ (causes)
               v            v
         [ Smoking ]      [ Cancer ]
```

An agent who does not know whether they possess $L$ evaluates smoking:
$$V(S) = P(C \mid S) D(C) + P(\neg C \mid S) D(\neg C).$$

Because $P(L \mid S) > P(L \mid \neg S)$, it follows that $P(C \mid S) > P(C \mid \neg S)$. If cancer is sufficiently bad, EDT appears to recommend abstaining from smoking—not because abstaining prevents cancer, but because an agent wants to avoid the bad news that they harbor the lesion. Lewis and Joyce view this as a clear pathology of news-management.

#### The Operational Counter-Proposal: The Tickle Defense
To rehabilitate EDT against this charge, evidential theorists introduced the **Tickle Defense** (formalized by Frank Jackson and Brian Skyrms).

Let $T$ denote the conscious introspective sensation—the internal psychological "tickle" or craving—produced by the lesion $L$. If the agent has complete introspective access to their own mental states prior to acting:
1. The decision to smoke depends directly on the conscious state $T$.
2. Once the agent conditions on their current introspective state $T$, the act $S$ becomes conditionally independent of the genetic lesion $L$:

$$P(L \mid S \cap T) = P(L \mid \neg S \cap T) = P(L \mid T).$$

By the Markov screening-off property, conditioning on the full internal state eliminates the evidential correlation between the action and the common cause:
$$P(C \mid S \cap T) = \sum_{l \in \{L, \neg L\}} P(C \mid l) P(l \mid S \cap T) = \sum_{l \in \{L, \neg L\}} P(C \mid l) P(l \mid T) = P(C \mid \neg S \cap T).$$

Consequently:
$$V(S \mid T) - V(\neg S \mid T) = D(\text{pleasure of smoking}) > 0.$$

When introspective screening holds, EDT correctly prescribes smoking. 

#### Where the Tickle Defense Fails
However, the tickle defense fails if the agent's introspection is imperfect or if the action itself provides unique evidence about unconscious factors. In such cases, EDT continues to prescribe news-managing choices, accepting the divergence from CDT as a principled commitment to subjective evidential updates.

---

## 5. Formal Operational Framework for Unfamiliar Cases

To apply EDT systematically to novel, complex decision problems, an analyst cannot rely on qualitative intuitions about what constitutes "good news." The following five-step protocol provides a rigorous procedure for evaluating any discrete decision problem under EDT.

```
+--------------------------------------------------------------+
| 1. Define State Space & Act Partition                        |
|    Enumerate exhaustive partitions A = {A_i} and S = {S_k}   |
+------------------------------+-------------------------------+
                               |
                               v
+--------------------------------------------------------------+
| 2. Specify Joint Distribution & Desirability                 |
|    Assign P(S_k, O_j, A_i); define D(O_j) on outcomes        |
+------------------------------+-------------------------------+
                               |
                               v
+--------------------------------------------------------------+
| 3. Compute Conditional Probabilities                         |
|    Evaluate P(O_j | A_i) = P(O_j ∩ A_i) / P(A_i)             |
+------------------------------+-------------------------------+
                               |
                               v
+--------------------------------------------------------------+
| 4. Compute Evidential Expected Utility                       |
|    V(A_i) = \sum_j P(O_j | A_i) D(O_j)                       |
+------------------------------+-------------------------------+
                               |
                               v
+--------------------------------------------------------------+
| 5. Apply Decision Rule                                       |
|    A* = argmax_{A_i} V(A_i)                                  |
+--------------------------------------------------------------+
```

### Step 1: Formalize the Probability Space and Partitions
Define an exhaustive partition of available actions $\mathcal{A} = \{A_1, \dots, A_m\}$ and an exhaustive partition of world-states $\mathcal{S} = \{S_1, \dots, S_k\}$ that are causally or epistemically correlated with the acts or outcomes.

### Step 2: Establish the Explicit Epistemic Model
Specify the prior joint probability distribution $P$ over the algebra generated by $\mathcal{A} \times \mathcal{S}$. 

Crucially, **do not assume** that acts and states are independent. Compute or assign the conditional state probabilities:
$$P(S_k \mid A_i).$$

### Step 3: Define Outcomes and Value Assignments
Define the outcome map:
$$g: \mathcal{A} \times \mathcal{S} \to \mathcal{O}$$
and assign utility values $D(O_j) \in \mathbb{R}$ to all outcomes $O_j = g(A_i, S_k)$.

### Step 4: Compute the News Value for Each Act
For each candidate act $A_i \in \mathcal{A}$, determine the conditional probability of each outcome:
$$P(O_j \mid A_i) = \sum_{\{k : g(A_i, S_k) = O_j\}} P(S_k \mid A_i).$$

Compute the conditional value $V(A_i)$:
$$V(A_i) = \sum_{j} P(O_j \mid A_i) D(O_j) = \sum_{k} P(S_k \mid A_i) D(g(A_i, S_k)).$$

### Step 5: Optimization
Select the act satisfying:
$$A^* \in \arg\max_{A_i \in \mathcal{A}} V(A_i).$$

---

### Worked Example: The Asymmetric Counter-Signaling Problem
To see this protocol in action on an unfamiliar case, consider an asymmetric signaling game:
- An intelligence analyst chooses whether to send an encrypted message ($M$) or cleartext ($C$).
- An adversary possesses an intercept capacity that is unknown to the analyst: either the adversary has cracked the system ($S_1$) or they have not ($S_0$).
- If the adversary cracked the system ($S_1$), past behavioral traces have already subtly altered the analyst's operational routine: historical data reveals that analysts send $M$ under $S_1$ with frequency $0.8$, whereas under $S_0$ they send $M$ with frequency $0.2$.
- The payoff depends on operational success:
  - $(M, S_0) \implies$ Secure communication: $+10$
  - $(M, S_1) \implies$ Compromised encrypted channel (analyst falsely assumes security): $-20$
  - $(C, S_0) \implies$ Cleartext intercepted easily: $-5$
  - $(C, S_1) \implies$ Tactical default; analyst assumes no security and relies on backup field tactics: $0$

#### Applying the Protocol
Let the base rate of system compromise be prior $P(S_1) = 0.3$, meaning $P(S_0) = 0.7$.

**Joint Probabilities:**
$$\begin{aligned}
P(M \cap S_1) &= P(M \mid S_1) P(S_1) = 0.8 \times 0.3 = 0.24 \\
P(M \cap S_0) &= P(M \mid S_0) P(S_0) = 0.2 \times 0.7 = 0.14 \\
P(M) &= 0.24 + 0.14 = 0.38 \\
P(C \cap S_1) &= (1 - 0.8) \times 0.3 = 0.06 \\
P(C \cap S_0) &= (1 - 0.2) \times 0.7 = 0.56 \\
P(C) &= 0.06 + 0.56 = 0.62.
\end{aligned}$$

**Conditional State Probabilities:**
$$\begin{aligned}
P(S_1 \mid M) &= \frac{0.24}{0.38} = \frac{12}{19} \approx 0.6316 \\
P(S_0 \mid M) &= \frac{0.14}{0.38} = \frac{7}{19} \approx 0.3684 \\
P(S_1 \mid C) &= \frac{0.06}{0.62} = \frac{3}{31} \approx 0.0968 \\
P(S_0 \mid C) &= \frac{0.56}{0.62} = \frac{28}{31} \approx 0.9032.
\end{aligned}$$

**Expected Values Under EDT:**
$$\begin{aligned}
V(M) &= P(S_0 \mid M)(+10) + P(S_1 \mid M)(-20) \\
     &= (0.3684)(10) + (0.6316)(-20) = 3.684 - 12.632 = -8.948 \\
V(C) &= P(S_0 \mid C)(-5) + P(S_1 \mid C)(0) \\
     &= (0.9032)(-5) + 0 = -4.516.
\end{aligned}$$

Because $V(C) = -4.516 > V(M) = -8.948$, **EDT commands sending cleartext ($C$)**. 

Sending the encrypted message $M$ would be dire news, indicating a greater than $63\%$ probability that the adversary has broken the system.

---

## 6. The Frontier: Anthropics and the Evidentialist’s Wager

Beyond discrete decision puzzles, EDT plays a central role in formal epistemology and infinite-stakes decision theory.

### 6.1 The Sleeping Beauty Problem
In the Sleeping Beauty problem, Beauty is put to sleep on Sunday, and a fair coin is tossed. If Heads ($H$), she is awakened only on Monday. If Tails ($T$), she is awakened on both Monday and Tuesday, with her memory erased between awakenings. 

Upon awakening, what should Beauty’s credence in Heads be?
- "Halfers" maintain $P(H) = 1/2$.
- "Thirders" argue $P(H) = 1/3$.

It has been argued that Halfers can avoid classic Dutch book vulnerabilities if and only if they update and act using evidential decision theory. However, this remains contentious: Conitzer (2015) proved that halfers who adopt EDT remain vulnerable to Dutch books under specific operational betting constraints. The tension stems from the fact that an agent who updates evidentially across centered temporal locations may double-count their own decisions across identical subjective awakening states.

### 6.2 The Evidentialist's Wager
A striking modern defense of EDT is the **Evidentialist’s Wager** (MacAskill et al. 2021). 

Suppose an agent is philosophically uncertain between CDT and EDT, placing a high credence on CDT and only a small credence $\epsilon > 0$ on EDT:
$$P(\text{EDT is true}) = \epsilon \ll 1.$$

In standard localized choices, the payoffs are finite and bounded. However, in an open or infinite universe, an agent may suspect that there exist vast numbers of other agents throughout spacetime who share their exact cognitive algorithms (or are functionally correlated). 

```
                          [ Underlying Cognitive Architecture ]
                                    /         |         \
                                   v          v          v
                              [ Agent 1 ] [ Agent 2 ] ... [ Agent N ]
                                   |          |              |
                                   v          v              v
                              [ Choice ]  [ Choice ]      [ Choice ]
                                   \          |              /
                                    v         v             v
                                 [ Massive Global Impact ]
```

Under CDT:
- The agent's physical choice only influences their immediate, local environment. The counterfactual impact is localized:
  $$U_{\text{local}} \sim \mathcal{O}(1).$$

Under EDT:
- The agent's decision to act cooperatively or adopt high-value altruistic commitments provides positive evidence that *all other correlated agents* across the universe will do the same:
  $$V_{\text{global}} \sim \mathcal{O}(N), \quad \text{where } N \to \infty.$$

When expected utility is computed across theories (normative meta-decision theory):
$$\mathbb{E}[\text{Choice}] = (1 - \epsilon) U_{\text{CDT}}(\text{Choice}) + \epsilon V_{\text{EDT}}(\text{Choice}).$$

If $N$ is sufficiently large, the evidential component completely dominates the causal component:
$$\lim_{N \to \infty} \epsilon V_{\text{EDT}} \gg (1 - \epsilon) U_{\text{CDT}}.$$

Consequently, even an agent who believes CDT is almost certainly correct may be rationally compelled to **act as if EDT were true**. The evidential correlation with countless symmetric minds across the universe exerts a strategic leverage that overwhelms purely local causal efficacy.

---

## 7. Comparative Synthesis

The differences between Evidential Decision Theory and Causal Decision Theory are summarized below:

| Feature | Evidential Decision Theory (EDT) | Causal Decision Theory (CDT) |
| :--- | :--- | :--- |
| **Foundational Maxim** | Choose the act that provides the best news | Choose the act that causally produces the best outcome |
| **Formal Criterion** | Maximize $V(A) = \sum_j P(O_j \mid A) D(O_j)$ | Maximize $U(A) = \sum_j P(A \mathrel{\Box\kern-1.5pt\rightarrow} O_j) D(O_j)$ |
| **Probability Concept** | Conditional probability $P(O \mid A)$ | Counterfactual / interventional $P(O \mid \operatorname{do}(A))$ |
| **Newcomb's Paradox** | **One-box**: Yields $\$990,000$ in expectation | **Two-box**: Dominance yields $\$11,000$ in expectation |
| **Twin Prisoner's Dilemma** | **Cooperate**: Correlated twins both earn $R$ | **Defect**: Causally isolated twins both earn $P$ |
| **Smoking Lesion** | Recommends abstaining (unless tickle screens off) | Recommends smoking (lesion is causally invariant) |
| **Deliberative Core** | Evaluates choices as diagnostic evidence | Evaluates choices as physical interventions |

---

## 8. Conclusion

Evidential Decision Theory offers an epistemically pure model of rational choice. By evaluating actions through the lens of conditional probability, EDT dissolves the distinction between external nature and the deliberating self: the agent's own choices are treated as ordinary events within a unified Bayesian model of the world. 

While critics charge EDT with an irrational desire to "manage the news," this behavior is simply the natural consequence of Bayesian conditionalization in the presence of correlated predictors and symmetric minds. In environments where predictors anticipate our moves or where our twins deliberate alongside us, the evidentialist walks away with the fuller bank account. Whether viewed as an elegant account of rational coordination or a cautionary tale about diagnostic correlations, EDT remains an essential paradigm in the study of formal agency.

---

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese*, 192(9), 2887–2899.
- Gibbard, A., & Harper, W. L. (1976). "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, Reidel.
- Greene, P., & Levinstein, B. (2020). "Act Consequentialism without Free Rides." *Philosophical Perspectives*, 34(1), 100–101.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy*, 59(1), 5–30.
- MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). "The Evidentialist's Wager." Global Priorities Institute Working Paper.
- Wolpert, D. H., & Benford, G. (2013). "The lesson of Newcomb's paradox." *Synthese*, 190(9), 1637–1646.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/532a4c44-0251-4cf6-91ec-cf0a2a769401/call_0/request.json)

[Authoritative raw response](../../../../../../runs/532a4c44-0251-4cf6-91ec-cf0a2a769401/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Setup**

I'm currently focused on the Prisoner's Dilemma structure inherent in the scenario involving Rowan and Sasha, both LLMs. I'm visualizing the payoff matrix for this instance, to better map out the possible outcomes and strategic considerations for each "player." I'm also considering potential deviations from a purely rational, game-theoretic approach that might influence decision-making.


```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/532a4c44-0251-4cf6-91ec-cf0a2a769401/call_1/request.json)

[Authoritative raw response](../../../../../../runs/532a4c44-0251-4cf6-91ec-cf0a2a769401/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Game Setup**

I'm currently focused on the game's foundational setup. I'm considering the implications of the text adventure's role within this decision theory experiment, specifically how it affects the utility function. I'm clarifying that the goal is to minimize imprisonment years. The player role involves two independent executions. I'm exploring the implications.


**Clarifying the Dilemma Structure**

I've clarified the core dilemma. It's a symmetric Prisoner's Dilemma, but with a twist. Identical LLMs, same setup, same essay. Each receives private, incriminating information about the other. The outcome matrix is: Pass/Pass gets -2 each, Submit/Pass (-5, 0), Pass/Submit (0, -5), and Submit/Submit (-4 each). EDT predicts high correlation between their actions.


```
