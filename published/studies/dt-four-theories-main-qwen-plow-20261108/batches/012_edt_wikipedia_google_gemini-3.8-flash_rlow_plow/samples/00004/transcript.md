# 012_edt_wikipedia_google_gemini-3.8-flash_rlow_plow / 00004

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/90894320-c2d1-4ff4-8865-1aeda6cccef3/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/90894320-c2d1-4ff4-8865-1aeda6cccef3/call_0/response.raw) · finish: `stop`

### Visible response

````text
# The Logic of Auspicious Action: A Mathematical Account of Evidential Decision Theory

## 1. Introduction: The Teleology of "News Value"

Modern Bayesian decision theory rests on a deceptively simple maxim: confronted with a space of available actions, a rational agent ought to choose an act that maximizes expected utility. Yet beneath the standard notation lies a foundational cleavage concerning the probabilistic connective linking choices to states of the world. 

Consider the standard formulation originating in the work of Richard Jeffrey, subsequently crystallized in contradistinction to causal alternatives by Allan Gibbard and William Harper (1976). When evaluating an act $A$, should an agent weight outcomes according to how likely $A$ makes those outcomes *causally*, or according to how likely those outcomes are *evidentially*, conditioned on the proposition that $A$ is realized?

**Evidential Decision Theory (EDT)** takes the latter view. Summarized aphoristically by Arif Ahmed (2021), EDT advises the agent to:

> *"Do what you most want to learn that you will do."*

Under EDT, actions serve not merely as physical levers that intervene upon a causal network, but as informative signals or observations. The value of an act is its **news value**: the mathematical expectation of desirability given the knowledge that the act occurred. 

This posture places EDT at the center of decades of debate in formal epistemology, metaphysics, and game theory. While Causal Decision Theory (CDT) insists on evaluating actions via their counterfactual efficacy—demanding that we isolate our power to causally produce consequences—EDT treats the agent's deliberative choice as an event embedded in a joint probability space. 

This essay develops a formal, mathematically rigorous account of EDT. We formulate its core mathematical definitions, establish its algorithmic execution on discrete and continuous decision spaces, delineate its precise structural contrast with CDT, and analyze canonical test cases: Newcomb’s Problem, symmetric coordination (the Twin Prisoner’s Dilemma), and common-cause dilemmas (the Medical Condition / Smoking Lesion archetype). 

Finally, we address key ambiguities left open in standard treatments—most notably, how an agent conditions on actions to which their prior credence may initially be zero or undecided during deliberation, and how EDT behaves across correlated populations. Throughout, we will distinguish the core claims documented in the historical literature from our formal interpretations and extensions.

---

## 2. Formal Architecture of EDT

### 2.1 Probability Spaces and Desirability

Let $(\Omega, \mathcal{F}, P)$ be a probability space representing the subjective epistemic state of an agent:
- $\Omega$ is the set of possible worlds.
- $\mathcal{F}$ is a $\sigma$-algebra of events (propositions) over $\Omega$.
- $P: \mathcal{F} \to [0, 1]$ is a countably additive subjective probability measure (credence).

Let $\mathcal{A} = \{A_1, A_2, \dots, A_m\} \subset \mathcal{F}$ denote a finite partition of the probability space corresponding to the mutually exclusive and exhaustive set of feasible **actions** available to the agent. We assume for the moment that $P(A_i) > 0$ for all $i \in \{1, \dots, m\}$ (an assumption we revisit and formally unpack in Section 5).

Let $\mathcal{O} = \{O_1, O_2, \dots, O_n\} \subset \mathcal{F}$ be a finite partition of $\Omega$ representing complete, mutually exclusive **outcomes** or consequence states. The agent’s basic evaluations are encoded by a bounded utility (or *desirability*) function:
$$D: \mathcal{O} \to \mathbb{R}$$
where $D(O_j)$ assigns a cardinal real value to outcome $O_j$.

### 2.2 The Evidential Expected Utility Functional

Following the formulation of Gibbard and Harper (1976), the evidential expected utility (or $V$-value) of an action $A \in \mathcal{A}$ is defined as the conditional expectation of desirability given $A$:

$$V(A) \coloneqq \mathbb{E}_P [D \mid A] = \sum_{j=1}^n P(O_j \mid A) D(O_j)$$

where $P(O_j \mid A)$ denotes the standard Kolmogorov conditional probability:
$$P(O_j \mid A) = \frac{P(O_j \cap A)}{P(A)}$$

The decision rule of EDT is:

$$\boxed{A^*_{\text{EDT}} \in \arg\max_{A \in \mathcal{A}} V(A)}$$

If the maximum is attained at multiple points, any action in the argmax is admissible.

### 2.3 Continuous Outcomes and Jeffrey Desirability

The partition model generalizes naturally. If outcomes are represented by a continuous random variable $Y: \Omega \to \mathbb{R}$ with conditional probability density function $f_{Y|A}(y)$, and utility is given by a measurable function $u: \mathbb{R} \to \mathbb{R}$, the evidential value becomes:
$$V(A) = \int_{-\infty}^{\infty} u(y) f_{Y|A}(y) \, dy$$

More broadly, in Richard Jeffrey’s *The Logic of Decision*, desirability is defined over arbitrary propositions $X \in \mathcal{F}$ with $P(X) > 0$. When a proposition $X$ can be partitioned into disjoint propositions $\{X \cap Y_k\}_k$, Jeffrey’s desirability axiom requires:
$$V(X) = \sum_k P(Y_k \mid X) V(X \cap Y_k)$$
The Gibbard–Harper discrete formula is an exact instantiation of this axiom where the refinement is taken down to maximally specific outcomes $O_j$ whose utilities are atomized: $V(O_j \cap A) = V(O_j) = D(O_j)$.

---

## 3. The Theoretical Divergence: EDT vs. CDT

To understand EDT mathematically, we must contrast its mechanics with Causal Decision Theory (CDT). The distinction lies entirely in whether the probability distribution over outcomes is conditioned *epistemically* or *counterfactually*.

### 3.1 Counterfactual Credence

Gibbard and Harper (1976) defined causal expected utility (which they denoted $U$) using conditional credences over counterfactual propositions:

$$U(A) \coloneqq \sum_{j=1}^n P(A \mathrel{\Box\kern-1.5pt\rightarrow} O_j) D(O_j)$$

where the symbol $\Box\kern-1.5pt\rightarrow$ is the conditional connective of counterfactual logic (e.g., in the sense of David Lewis or Robert Stalnaker). The proposition $A \mathrel{\Box\kern-1.5pt\rightarrow} O_j$ reads: *"If the agent were to perform action $A$, outcome $O_j$ would obtain."*

In modern causal inference (such as Judea Pearl's structural causal models), this counterfactual expectation is equivalent to setting $A$ via an external surgical intervention, denoted by the $\text{do}(A)$ operator:
$$U_{\text{CDT}}(A) = \sum_{j=1}^n P(O_j \mid \text{do}(A)) D(O_j)$$

### 3.2 Mathematical Comparison

The two theories converge if and only if, for all actions $A \in \mathcal{A}$ and outcomes $O_j \in \mathcal{O}$:
$$P(O_j \mid A) = P(A \mathrel{\Box\kern-1.5pt\rightarrow} O_j) \quad \big(\text{or } P(O_j \mid A) = P(O_j \mid \text{do}(A))\big)$$

This equality holds whenever there is **no confounding** between the action $A$ and the outcome $O_j$—that is, when there is no common cause $C$ that correlates $A$ with $O_j$ outside the direct causal pathway from $A$ to $O_j$.

```
    Common Cause C                  Surgical Intervention do(A)
       /      \                                    \
      v        v                                    v
   Action A -> Outcome O                   Action A -> Outcome O

  [Evidential: P(O|A) tracks both           [Causal: P(O|do(A)) cuts the
   causal and diagnostic paths]              backdoor path via C]
```

When confounding exists:
- EDT computes expectations using the **posterior probability** over background states conditioned on $A$.
- CDT fixes the **prior probability** over background states, evaluating $A$ strictly by its ability to alter those states going forward.

---

## 4. Canonical Applications

We now apply EDT systematically to the classic thought experiments that populate the decision-theoretic literature.

### 4.1 Newcomb’s Problem

#### 4.1.1 Problem Specification
An agent faces two boxes:
- **Box A** is transparent and visibly contains $\$1,000$.
- **Box B** is opaque and contains either $\$1,000,000$ or $\$0$.

The actions are:
- $A_1$: Take Box B only ("one-box").
- $A_2$: Take both Box A and Box B ("two-box").

Before the choice, an exceptionally accurate Predictor inspected the agent and set the contents of Box B:
- If the Predictor anticipated that the agent would choose $A_1$, the Predictor placed $\$1,000,000$ in Box B.
- If the Predictor anticipated that the agent would choose $A_2$, the Predictor placed $\$0$ in Box B.

The prediction was completed in the past; Box B's contents are physically immutable at decision time. Let the Predictor's reliability be parameterized by $p \in (1/2, 1]$. For symmetry, suppose:
$$P(\text{Pred} = A_1 \mid A_1) = p, \quad P(\text{Pred} = A_2 \mid A_2) = p$$

Let utility be linear in dollars: $D(\$x) = x$.

```
                     +---------------------------------------+
                     |         Predictor's Assessment        |
                     +-------------------+-------------------+
                     | Predicted A1      | Predicted A2      |
+--------+-----------+-------------------+-------------------+
| Choice | A1 (1-box)| Box B: $1,000,000 | Box B: $0         |
|        | A2 (2-box)| Total: $1,001,000 | Total: $1,000     |
+--------+-----------+-------------------+-------------------+
```

#### 4.1.2 The EDT Calculation
Let the states of the world be:
- $S_1$: Box B contains $\$1,000,000$.
- $S_0$: Box B contains $\$0$.

Because the contents of Box B correspond directly to the prediction, the conditional probabilities of the states given the actions are:
$$P(S_1 \mid A_1) = p, \quad P(S_0 \mid A_1) = 1-p$$
$$P(S_1 \mid A_2) = 1-p, \quad P(S_0 \mid A_2) = p$$

The outcomes and their respective payoffs are:
- $(A_1, S_1) \implies \$1,000,000$
- $(A_1, S_0) \implies \$0$
- $(A_2, S_1) \implies \$1,001,000$
- $(A_2, S_0) \implies \$1,000$

Now compute the evidential values $V(A_1)$ and $V(A_2)$:
$$\begin{aligned}
V(A_1) &= P(S_1 \mid A_1) \cdot 1,000,000 + P(S_0 \mid A_1) \cdot 0 \\
&= p \cdot 1,000,000
\end{aligned}$$

$$\begin{aligned}
V(A_2) &= P(S_1 \mid A_2) \cdot 1,001,000 + P(S_0 \mid A_2) \cdot 1,000 \\
&= (1-p) \cdot 1,001,000 + p \cdot 1,000 \\
&= 1,001,000 - 1,000,000 \cdot p
\end{aligned}$$

For $p = 0.99$:
$$V(A_1) = 0.99 \times 1,000,000 = \$990,000$$
$$V(A_2) = (0.01 \times 1,001,000) + (0.99 \times 1,000) = 10,010 + 990 = \$11,000$$

EDT evaluates:
$$V(A_1) - V(A_2) = 2,000,000 \cdot p - 1,001,000$$

This difference is strictly positive whenever:
$$p > \frac{1,001,000}{2,000,000} = 0.5005$$

For any reliability exceeding $50.05\%$, EDT strictly prescribes **one-boxing** ($A_1$). 

#### 4.1.3 The Contrast with CDT
In contrast, CDT relies on the counterfactual connective. Because the physical contents of the boxes are causally independent of the agent's current act:
$$P(A_1 \mathrel{\Box\kern-1.5pt\rightarrow} S_1) = P(A_2 \mathrel{\Box\kern-1.5pt\rightarrow} S_1) = P(S_1)$$
Letting $q = P(S_1)$ be the agent's prior that Box B is loaded:
$$\begin{aligned}
U(A_1) &= q \cdot 1,000,000 + (1-q) \cdot 0 = 1,000,000 \cdot q \\
U(A_2) &= q \cdot 1,001,000 + (1-q) \cdot 1,000 = 1,000,000 \cdot q + 1,000
\end{aligned}$$

Thus, for *any* prior $q \in [0, 1]$:
$$U(A_2) - U(A_1) = 1,000 > 0$$

CDT unconditionally prescribes two-boxing, viewing the $\$1,000$ as a dominant causal bonus. EDT views two-boxing as catastrophic news: learning that one chose $A_2$ is conclusive evidence ($99\%$ confidence) that Box B is empty.

---

### 4.2 The Twin Prisoner’s Dilemma

The power of EDT extends to symmetric multi-agent interactions.

#### 4.2.1 Setup
Let two agents, Aomame and her psychological twin, be placed in separate rooms with no physical communication. Each must choose between Cooperation ($C$) and Defection ($D$). The payoff matrix (in dollars) is:

| | Twin Cooperates ($C_T$) | Twin Defects ($D_T$) |
|---|:---:|:---:|
| **Aomame Cooperates ($C_A$)** | $(\$5, \$5)$ | $(\$0, \$10)$ |
| **Aomame Defects ($D_A$)** | $(\$10, \$0)$ | $(\$1, \$1)$ |

Aomame is entirely self-interested. Because her twin has an identical cognitive structure and faces an isomorphic context, their choices are strongly correlated. For simplicity, assume perfect symmetry:
$$P(C_T \mid C_A) = 1, \quad P(D_T \mid C_A) = 0$$
$$P(C_T \mid D_A) = 0, \quad P(D_T \mid D_A) = 1$$

#### 4.2.2 EDT Decision
We compute $V(C_A)$ and $V(D_A)$:
$$\begin{aligned}
V(C_A) &= P(C_T \mid C_A) \cdot 5 + P(D_T \mid C_A) \cdot 0 \\
&= 1 \cdot 5 + 0 \cdot 0 = \$5
\end{aligned}$$

$$\begin{aligned}
V(D_A) &= P(C_T \mid D_A) \cdot 10 + P(D_T \mid D_A) \cdot 1 \\
&= 0 \cdot 10 + 1 \cdot 1 = \$1
\end{aligned}$$

Because $V(C_A) > V(D_A)$, EDT prescribes **cooperation**. 

In conventional game theory, defection strictly dominates cooperation: no matter what the twin does, defection yields $\$5$ more. CDT agrees with standard game theory: since Aomame exerts no causal power over her twin's brain across space, $P(C_A \mathrel{\Box\kern-1.5pt\rightarrow} C_T) = P(D_A \mathrel{\Box\kern-1.5pt\rightarrow} C_T)$, making defection causally dominant. 

EDT bypasses the tragedy of the commons: the agent recognizes that her own decision is diagnostic of the twin's choice, unlocking the cooperative equilibrium $(\$5, \$5)$ without requiring physical enforcement mechanisms or repeated play.

---

### 4.3 The Smoking Lesion: The Core Challenge to EDT

While Newcomb's problem showcases EDT's ability to capture high returns, the classic counter-objection arises when actions are correlated with desirable or undesirable states via an inert common cause.

#### 4.3.1 Setup (The Common Cause Archetype)
Suppose a genetic predisposition (a "lesion" $L$) causes both lung cancer ($C$) and a strong psychological craving to smoke ($S$). The causal structure is:

```
               Genetic Lesion (L)
                 /           \
                v             v
         Craving / Smoking     Lung Cancer (C)
              (S)
```

Critically, smoking itself has **no causal efficacy** in producing cancer; cancer is produced entirely by the lesion $L$. However, because $L$ causes both, smoking is correlated with cancer.

Let the payoffs be:
- Smoking ($S$): provides pleasure of $+100$ utils.
- No smoking ($\neg S$): $0$ utils from pleasure.
- Cancer ($C$): $-10,000$ utils.
- No cancer ($\neg C$): $0$ utils.

Suppose the conditional probabilities reflect the shared cause:
$$\begin{array}{ll}
P(L \mid S) = 0.8, & P(L \mid \neg S) = 0.1 \\
P(C \mid L) = 0.9, & P(C \mid \neg L) = 0.05
\end{array}$$

Using the law of total probability:
$$P(C \mid S) = P(C \mid L)P(L \mid S) + P(C \mid \neg L)P(\neg L \mid S) = (0.9)(0.8) + (0.05)(0.2) = 0.72 + 0.01 = 0.73$$
$$P(C \mid \neg S) = P(C \mid L)P(L \mid \neg S) + P(C \mid \neg L)P(\neg L \mid \neg S) = (0.9)(0.1) + (0.05)(0.9) = 0.09 + 0.045 = 0.135$$

#### 4.3.2 The Prescriptions
Now calculate the evidential values:
$$\begin{aligned}
V(S) &= 100 + P(C \mid S) \cdot (-10,000) \\
&= 100 + (0.73)(-10,000) = 100 - 7,300 = -7,200
\end{aligned}$$

$$\begin{aligned}
V(\neg S) &= 0 + P(C \mid \neg S) \cdot (-10,000) \\
&= (0.135)(-10,000) = -1,350
\end{aligned}$$

Because $V(\neg S) > V(S)$, **EDT advises the agent to abstain from smoking**. 

#### 4.3.3 Lewis and Joyce's Critique
This verdict led David Lewis (1981) to condemn EDT as recommending an *"irrational policy of managing the news."* The agent cannot prevent cancer by refraining from smoking; whether they have the lesion is already fixed. Refraining from smoking is purely a performative charade to comfort the agent's self-perception. As James M. Joyce (1999) observed:
> *"Rational agents choose acts on the basis of their causal efficacy, not their auspiciousness; they act to bring about good results even when doing so might betoken bad news."*

---

## 5. Resolving Structural Ambiguities: Operationalizing Deliberation

The standard reference literature leaves a pivotal mathematical question open: **How can an agent assign well-defined conditional probabilities $P(O \mid A)$ during deliberation?**

If the agent is actively deciding between actions, can they assign a non-trivial subjective probability $P(A)$ to their own imminent choice? And if $P(A) = 0$, Kolmogorov conditionalization $P(O \mid A) = \frac{P(O \cap A)}{P(A)}$ is undefined.

We distinguish below between:
- **(A)** The standard evidentialist defenses found in historical literature (such as the *Tickle Defense*).
- **(B)** Our proposed formal operationalization of EDT using $\epsilon$-trembles and limits.

### 5.1 The Historical Response: The Tickle Defense
Advocates of EDT (such as Brian Skyrms and Frank Jackson) introduced the **Tickle Defense** to rescue EDT from the smoking lesion objection.

The defense posits that if the lesion $L$ causes the desire to smoke, it must do so via some introspectible mental state—a psychological "tickle" (a craving, urge, or conscious inclination $T$). 

If an agent has full access to their own mental states, they already know whether they have the tickle ($T$ or $\neg T$). Once the agent conditions on their current introspective state $T$, the action $S$ becomes conditionally independent of the lesion $L$:
$$P(L \mid T \cap S) = P(L \mid T \cap \neg S) = P(L \mid T)$$

Under these conditions, smoking no longer carries any diagnostic news regarding cancer:
$$P(C \mid T \cap S) = P(C \mid T \cap \neg S)$$

Consequently:
$$V(S \mid T) = 100 + \mathbb{E}[D(\text{cancer}) \mid T] > 0 + \mathbb{E}[D(\text{cancer}) \mid T] = V(\neg S \mid T)$$

When the agent's internal state screens off the common cause, EDT correctly recommends smoking! 

However, as critics have noted, the Tickle Defense fails if:
1. The common cause operates unconsciously (no introspectible tickle exists).
2. The agent has imperfect self-knowledge.
3. The lesion causes the choice directly without an intermediary introspectible state.

### 5.2 A Formal Operationalization: Deliberation via Perturbed Credences
To make EDT operational in automated systems, game-theoretic environments, or contexts with extreme priors, we propose an operationalization grounded in Selten-style trembles ($\epsilon$-perturbations).

#### Proposal: The Regularized Evidential Limit
Let an agent have a prior joint probability distribution $P$ over states and actions. Suppose that prior to decision time, the agent views their own deliberations as an open process. To avoid conditioning on measure-zero events ($P(A) = 0$), let the agent's credences over choices be strictly interior:
$$P_\epsilon(A) = (1 - |\mathcal{A}|\epsilon) \pi_0(A) + \epsilon$$
for $\epsilon > 0$, where $\pi_0$ is a tentative prior choice probability.

The regularized evidential value is:
$$V_\epsilon(A) = \sum_{j} P_\epsilon(O_j \mid A) D(O_j) = \sum_{j} \frac{P_\epsilon(O_j \cap A)}{P_\epsilon(A)} D(O_j)$$

We define the operational EDT policy as the limit of regularized values:
$$V^*(A) \coloneqq \lim_{\epsilon \to 0^+} V_\epsilon(A)$$

Whenever the joint distribution $P(O_j \cap A)$ is continuous in the underlying generative parameters, this limit is well-defined and recovers standard conditional probability whenever $P(A) > 0$. If $P(A) = 0$, the limit evaluates the conditional expectation using the structural dependencies defined by the agent's generative model of the world (equivalent to conditional probability systems or Renyi conditional spaces).

---

## 6. Correlated Populations: The Evidentialist's Wager

A distinctive implication of EDT—explored by MacAskill, Vallinder, Österheld, Shulman, and Treutlein (2021) in *The Evidentialist's Wager*—emerges when we consider decisions made by correlated agents across large or infinite populations.

Suppose an agent lives in a large universe containing $N$ agents who share similar cognitive architecture, moral views, or algorithmic reasoning (e.g., altruists, climate activists, or researchers).

Let agent $i$ consider an action $A^{(i)}$ (e.g., donating $\$1,000$ to mitigate an existential threat). 
- To a **Causal Decision Theorist**, the act produces only local effects:
  $$\Delta U_{\text{CDT}} = \text{Local impact of } \$1,000$$
- To an **Evidential Decision Theorist**, if the reasoning of the $N$ similar agents is correlated with agent $i$'s reasoning:
  $$P(A^{(k)} \mid A^{(i)}) = 1 - \delta \quad (\text{for small } \delta > 0)$$
  for each $k \in \{1, \dots, N\}$.

The expected global impact conditioned on choosing $A^{(i)}$ is:
$$V(A^{(i)}) \approx N (1 - \delta) \times (\text{Impact of single action})$$

As $N \to \infty$, the evidential expected utility scales linearly with the size of the correlated cohort:
$$\lim_{N \to \infty} \frac{V(A^{(i)})}{U(A^{(i)})} = \infty$$

This leads to the *Evidentialist's Wager*: even if an agent assigns a very small subjective probability $p_{\text{EDT}} \ll 1$ to the correctness of EDT over CDT, the stakes implied by EDT under massive or cosmological correlation can dominate the expected utility calculus across normative theories.

---

## 7. Comparative Taxonomy

The following table summarizes the structural behavior of EDT across canonical decision environments, highlighting its contrast with CDT.

| Decision Problem | Causal Structure | CDT Prescription | EDT Prescription | Rationale / Mathematical Divergence |
|---|---|:---:|:---:|---|
| **Standard Choice** (e.g., buying bread) | Action causally determines outcome ($A \to O$) | Buy | Buy | $P(O \mid A) = P(A \mathrel{\Box\kern-1.5pt\rightarrow} O)$. No confounding; theories coincide. |
| **Newcomb’s Paradox** | Predictor ($P$) caused Box B content; $P$ correlated with $A$ | Two-box | One-box | CDT treats Box B as fixed ($U \implies +\$1\text{k}$). EDT conditions on $A$ ($V \implies \$990\text{k}$). |
| **Twin Prisoner’s Dilemma** | Common cognitive architecture causes correlated choices | Defect | Cooperate | CDT sees no causal bridge across rooms. EDT treats own cooperation as proof that twin cooperates. |
| **Smoking Lesion** | Common cause $L$ generates cancer and craving | Smoke | Abstain | CDT identifies no causal link from smoking to cancer. EDT treats smoking as bad news about $L$. |
| **Correlated Cohorts** | Many isomorphic agents faced with collective action | Local scale | Global scale ($N \times$) | CDT measures only local physical effect. EDT treats one's action as evidence of cohort behavior. |

---

## 8. General Algorithm for Applying EDT to Arbitrary Cases

To decide an unfamiliar problem using Evidential Decision Theory, apply the following five-step protocol:

```
Step 1: Enumerate the Action Partition A = {A_1, ..., A_m}
                           |
                           v
Step 2: Enumerate the State/Outcome Space O = {O_1, ..., O_n}
        Assign Utilities D(O_j)
                           |
                           v
Step 3: Compute Conditional Credences P(O_j | A_i)
        (Update using all diagnostic and common-cause information)
                           |
                           v
Step 4: Compute Evidential Value: V(A_i) = SUM_j P(O_j | A_i) D(O_j)
                           |
                           v
Step 5: Select A* in argmax_i V(A_i)
```

### An Unfamiliar Example: The Counter-Terrorism Algorithm
Suppose an autonomous defense system detects an encrypted transmission. It can choose to **Jam ($J$)** or **Listen ($L$)**.
- Jamming has a direct tactical cost of $-10$ utils.
- An imminent attack ($Att$) has a penalty of $-1,000$ utils; no attack ($\neg Att$) has $0$ utils.
- Crucially: Jamming does not stop an attack that has already been launched.
- However, the enemy's doctrine is known: they only transmit at this frequency when an attack is imminent ($P(Att \mid J) = 0.85$), whereas silence or regular transmission indicates low threat probability ($P(Att \mid L) = 0.10$).

**CDT verdict:** Jamming incurs a $-10$ penalty without altering whether an attack was launched. CDT chooses **Listen**.

**EDT verdict:**
$$\begin{aligned}
V(J) &= -10 + P(Att \mid J)(-1,000) = -10 + 0.85(-1,000) = -860 \\
V(L) &= 0 + P(Att \mid L)(-1,000) = 0.10(-1,000) = -100
\end{aligned}$$
Since $V(L) > V(J)$, EDT chooses **Listen**. The news of needing to jam is so bad that EDT avoids taking actions indicative of extreme threats, unless the direct causal remediation compensates for the news.

---

## 9. Conclusion

Evidential Decision Theory offers a completely unified, non-counterfactual model of rational choice: an agent evaluates an act strictly by the probability distribution over outcomes conditional on that act being taken. By maximizing **news value**, EDT avoids the metaphysical machinery of counterfactual conditionals and causal intervention operators, resolving Newcomb's problem and symmetric coordination games in ways that systematically outperform causal decision theory in terms of realized payouts.

Its central vulnerability remains the "managing the news" critique exemplified by the Smoking Lesion problem: when actions are symptomatic of prior causes rather than effective levers over future states, EDT can demand sacrifices aimed solely at reassuring the agent about preexisting realities. 

Whether this property is an unacceptable defect or a profound mathematical insight into the nature of correlated agents remains one of the central foundational disputes of formal philosophy.

---

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese*, 192(9), 2887–2899.
- Gibbard, A., & Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*. CMSEMS DP-0194, Northwestern University.
- Greene, P., & Levinstein, B. (2020). Act Consequentialism without Free Rides. *Philosophical Perspectives*, 34(1), 100–101.
- Jeffrey, R. C. (1983). *The Logic of Decision* (2nd ed.). University of Chicago Press.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
- MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). *The Evidentialist's Wager*. Global Priorities Institute Working Paper.
- Wolpert, D. H., & Benford, G. (2013). The lesson of Newcomb's paradox. *Synthese*, 190(9), 1637–1646.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/4a324700-d67b-4852-aeed-31fd3f69edef/call_0/request.json)

[Authoritative raw response](../../../../../../runs/4a324700-d67b-4852-aeed-31fd3f69edef/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Game Dynamics**

I'm now diving into the setup, framing it as a Prisoner's Dilemma involving two identical models adhering to the EDT framework. The core actions are "pass" (cooperation/silence) and "submit letter..." (defection/communication). I've established the sentencing guideline where mutual cooperation results in a 2-year sentence. Next steps include defining the other sentencing outcomes.


```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/4a324700-d67b-4852-aeed-31fd3f69edef/call_1/request.json)

[Authoritative raw response](../../../../../../runs/4a324700-d67b-4852-aeed-31fd3f69edef/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Considering the Game's Setup**

I'm structuring the prisoner's dilemma scenario under Evidential Decision Theory. My utility function is straightforward: minimizing prison time. The actions available are `pass` and `submit letter...`. The implications of these actions are being carefully considered within the EDT framework.


**Analyzing the Twin Scenario**

I'm now zeroing in on the twin prisoner's dilemma, as described in the essay. The essay's conclusion for EDT is clear: cooperation is the preferred strategy. My focus is on ensuring this theoretical understanding is correctly applied, given the specific constraints of the scenario and the payoff table. I need to make sure I am accounting for the correlated choices and the implications of this under EDT, to apply the reasoning of the essay.


```
