# Maximizing News Value: A Formal Account of Evidential Decision Theory

In classical Bayesian decision theory, rationality is identified with the maximization of expected utility. Yet, the question of how to formally express that expectation has divided philosophers, economists, and computer scientists for half a century. 

Standard causal intuition suggests that an agent should evaluate an action by what it *brings about*—its causal consequences in the world. **Evidential Decision Theory** (EDT) proposes a different normative standard: a rational agent should evaluate an action by its *news value*—what learning that the action occurred would lead the agent to believe about the world. Formulated aphoristically by Arif Ahmed, EDT instructs the decider to *"do what you most want to learn that you will do."*

This essay provides a rigorous, self-contained mathematical treatment of Evidential Decision Theory. We will formalize its decision rule, analyze its treatment of statistical dependence versus counterfactual causality, examine classic canonical problems (Newcomb's Paradox and the Twin Prisoner's Dilemma), explore its core philosophical challenges (such as the Medical Newcomb Problem and the "Tickle Defense"), and present a concrete computational methodology for applying EDT to arbitrary decision problems.

---

## 1. Formal Framework and Core Definitions

Let us construct a formal Bayesian setting for an agent facing a discrete decision problem.

### 1.1 The Probability Space and Primitive Sets

Let $(\Omega, \mathcal{F}, P)$ be a probability space representing the agent's subjective credences over possible states of the world, where $\Omega$ is the set of all possible worlds, $\mathcal{F}$ is a $\sigma$-algebra of events, and $P: \mathcal{F} \to [0, 1]$ is a subjective probability measure satisfying Kolmogorov’s axioms.

A decision problem is defined by:
1. **Act Set:** A mutually exclusive and exhaustive set of available acts $\mathcal{A} = \{A_1, A_2, \dots, A_n\} \subset \mathcal{F}$, such that $\sum_{i=1}^n P(A_i) = 1$. To evaluate conditional probabilities, we assume for now that $P(A_i) > 0$ for all $i$ (we will relax and address this assumption in Section 5).
2. **Outcome Set:** A mutually exclusive and exhaustive set of fine-grained outcomes $\mathcal{O} = \{O_1, O_2, \dots, O_m\} \subset \mathcal{F}$. Outcomes are fully specified states of affairs containing everything the agent cares about.
3. **Desirability (Utility) Function:** A bounded function $D: \mathcal{O} \to \mathbb{R}$ assigning a real-valued payoff (or von Neumann–Morgenstern utility) to each outcome.

### 1.2 The Evidential Decision Rule

Following the formulation analyzed by Allan Gibbard and William Harper (1976), the **evidential expected utility** (often termed the *desirability* or *news value*) of an act $A \in \mathcal{A}$, denoted $V(A)$, is defined as:

$$V(A) = \sum_{j=1}^m P(O_j \mid A) D(O_j)$$

where $P(O_j \mid A) = \frac{P(O_j \cap A)}{P(A)}$ is the standard conditional probability of outcome $O_j$ given the performance of action $A$.

The EDT prescription for rational choice is straightforward:

$$\text{Select } A^* \in \mathcal{A} \quad \text{such that} \quad A^* \in \arg\max_{A \in \mathcal{A}} V(A)$$

If multiple actions maximize $V(A)$, any act in the argmax set is permissible.

### 1.3 State-Space Decomposition

It is often convenient to partition $\Omega$ into a set of environmental **states** $\mathcal{S} = \{S_1, S_2, \dots, S_k\}$ that are causally independent of the agent’s immediate physical action. In such a partition, an act $A_i$ and a state $S_l$ jointly determine an outcome $O(A_i, S_l) \in \mathcal{O}$.

Under this decomposition, the evidential value expands via the law of total probability:

$$V(A) = \sum_{l=1}^k P(S_l \mid A) D(O(A, S_l))$$

Notice the central feature of this equation: the probability distribution over states $\mathcal{S}$ is **conditioned on the act** $A$. If an agent's choice provides diagnostic evidence regarding which state of the world has been realized, $P(S_l \mid A)$ varies with $A$, even if $A$ has no causal power to alter which state $S_l$ obtains.

---

## 2. EDT vs. CDT: Evidential Dependencies vs. Counterfactuals

To understand the distinctive behavior of EDT, we must contrast it with **Causal Decision Theory** (CDT). 

Gibbard and Harper formalized CDT by replacing conditional probabilities with the probability of counterfactual conditionals:

$$U(A) = \sum_{j=1}^m P(A \mathbin{\Box\rightarrow} O_j) D(O_j)$$

where the counterfactual proposition $A \mathbin{\Box\rightarrow} O_j$ reads: *"If the agent were to perform action $A$, outcome $O_j$ would obtain."*

In state-partition form, where states $S$ are held fixed as causal invariants outside the agent's immediate physical control, CDT evaluates:

$$U(A) = \sum_{l=1}^k P(S_l) D(O(A, S_l))$$

or in Judea Pearl’s structural causal modeling framework:

$$U(A) = \sum_{l=1}^k P(S_l \mid \text{do}(A)) D(O(A, S_l))$$

### The Divergence

The mathematical divergence between EDT and CDT reduces to the distinction between:
- **Conditioning on an observation:** $P(S \mid A)$
- **Intervening via an action:** $P(S \mid \text{do}(A))$ or $P(A \mathbin{\Box\rightarrow} S)$

Under intervention, $P(S \mid \text{do}(A)) = P(S)$ whenever $S$ is causally upstream of or exogenous to $A$. Thus, CDT holds beliefs about the state fixed regardless of which act is contemplated. 

EDT, by contrast, exploits the observational update. By Bayes' theorem:

$$P(S \mid A) = \frac{P(A \mid S) P(S)}{P(A)}$$

Whenever an act $A$ is correlated with a prior or concurrent state $S$—that is, whenever $P(A \mid S) \neq P(A)$—the conditional probability $P(S \mid A)$ will diverge from the prior $P(S)$. EDT treats this statistical correlation as fully actionable: an act is favored if taking it provides strong probabilistic evidence that the world is in a desirable state, irrespective of whether the act brings that state about.

---

## 3. Canonical Applications

### 3.1 Newcomb's Paradox

Newcomb's Paradox provides the quintessential operational battleground between EDT and CDT.

**Setup:**
- Two boxes: Box $A$ (transparent) containing $\$1,000$; Box $B$ (opaque) containing either $\$1,000,000$ or $\$0$.
- Available acts: $\mathcal{A} = \{A_1, A_2\}$, where $A_1$ is choosing only Box $B$ ("one-boxing"), and $A_2$ is choosing both Box $A$ and Box $B$ ("two-boxing").
- States: $\mathcal{S} = \{S_{\text{full}}, S_{\text{empty}}\}$, denoting whether Box $B$ contains $\$1,000,000$ or $\$0$.
- A predictor of exceptional reliability has inspected the agent beforehand and deposited the $\$1,000,000$ into Box $B$ if and only if they predicted the agent would choose $A_1$.

Let the predictor's reliability be parameterized by $p \in (1/2, 1]$:
$$P(S_{\text{full}} \mid A_1) = p, \quad P(S_{\text{empty}} \mid A_1) = 1 - p$$
$$P(S_{\text{empty}} \mid A_2) = p, \quad P(S_{\text{full}} \mid A_2) = 1 - p$$

Assume linear utility in money: $D(\$x) = x$.

**Payoff Matrix:**
| Act $\backslash$ State | $S_{\text{full}}$ ($\$1\text{M}$ in $B$) | $S_{\text{empty}}$ ($\$0$ in $B$) |
| :--- | :--- | :--- |
| **$A_1$ (One-box)** | $\$1,000,000$ | $\$0$ |
| **$A_2$ (Two-box)** | $\$1,001,000$ | $\$1,000$ |

**EDT Evaluation:**
$$\begin{aligned}
V(A_1) &= P(S_{\text{full}} \mid A_1) \cdot 1,000,000 + P(S_{\text{empty}} \mid A_1) \cdot 0 \\
&= p \cdot 1,000,000 \\
V(A_2) &= P(S_{\text{full}} \mid A_2) \cdot 1,001,000 + P(S_{\text{empty}} \mid A_2) \cdot 1,000 \\
&= (1 - p) \cdot 1,001,000 + p \cdot 1,000 \\
&= 1,001,000 - 1,000,000 \cdot p
\end{aligned}$$

For $p = 0.99$:
$$V(A_1) = 0.99 \times \$1,000,000 = \$990,000$$
$$V(A_2) = 0.01 \times \$1,001,000 + 0.99 \times \$1,000 = \$10,010 + \$990 = \$11,000$$

Since $V(A_1) \gg V(A_2)$, EDT decisively prescribes **one-boxing** ($A_1$). The act of taking only Box $B$ serves as near-certain evidence that the predictor placed the million dollars in the box.

*Comparison with CDT:* 
CDT holds that the predictor's deposit is an event in the causal past. Under any distribution $P(S_{\text{full}}) = q$, the counterfactual values are:
$$U(A_1) = q \cdot 1,000,000 + (1-q) \cdot 0 = 1,000,000q$$
$$U(A_2) = q \cdot 1,001,000 + (1-q) \cdot 1,000 = 1,000,000q + 1,000$$

Because $U(A_2) - U(A_1) = 1,000 > 0$ for all $q \in [0, 1]$, two-boxing strictly causally dominates one-boxing. EDT rejects this dominance reasoning because the states and acts are not epistemically independent.

---

### 3.2 The Twin Prisoner's Dilemma

Consider two players, Aomame and her psychological twin, placed in separate, causally isolated rooms. Each player has two choices: Cooperate ($C$) or Defect ($D$).

The payoff matrix for (Aomame, Twin) is:
| Aomame $\backslash$ Twin | Cooperate ($C_T$) | Defect ($D_T$) |
| :--- | :--- | :--- |
| **Cooperate ($C_A$)** | $(\$5, \$5)$ | $(\$0, \$10)$ |
| **Defect ($D_A$)** | $(\$10, \$0)$ | $(\$1, \$1)$ |

Because the twin possesses an identical cognitive structure and decision algorithm, Aomame's credence that her twin mimics her action is exceptionally high:
$$P(C_T \mid C_A) = 1 - \epsilon, \quad P(D_T \mid C_A) = \epsilon$$
$$P(D_T \mid D_A) = 1 - \epsilon, \quad P(C_T \mid D_A) = \epsilon$$
where $\epsilon \ll 1$ captures minor stochastic divergence.

**EDT Evaluation:**
$$\begin{aligned}
V(C_A) &= P(C_T \mid C_A) \cdot 5 + P(D_T \mid C_A) \cdot 0 = 5(1 - \epsilon) \\
V(D_A) &= P(C_T \mid D_A) \cdot 10 + P(D_T \mid D_A) \cdot 1 = 10\epsilon + 1(1 - \epsilon) = 1 + 9\epsilon
\end{aligned}$$

Setting $V(C_A) > V(D_A)$:
$$5 - 5\epsilon > 1 + 9\epsilon \iff 14\epsilon < 4 \iff \epsilon < \frac{2}{7}$$

For any reasonably similar twin ($\epsilon < 0.2857$), and particularly for identical twins ($\epsilon = 0$, where $V(C_A) = \$5$ and $V(D_A) = \$1$), EDT dictates **cooperation**. 

In conventional game theory (and under CDT), defection strictly dominates cooperation because the twin's physical action cannot be causally influenced across isolated rooms. EDT circumvents the Pareto-suboptimal outcome $(D_A, D_T)$ by recognizing that Aomame's decision is evidence of what another agent instantiating the same decision procedure is doing.

---

## 4. The Core Criticism: "Managing the News" and the Tickle Defense

While one-boxing in Newcomb's problem and cooperating in the Twin Prisoner's Dilemma yield higher empirical wealth—leading proponents to remark that "EDT agents end up rich while CDT agents end up poor"—the theory faces severe philosophical objections when applied to common-cause scenarios.

### 4.1 The Medical Newcomb Problem (The Smoking Lesion)

Suppose a genetic lesion $L$ causes two distinct phenomena:
1. A strong predisposition to smoke cigarettes ($S$).
2. The development of fatal lung cancer ($C$).

Smoking itself does *not* cause cancer; it is merely an effect of the common cause $L$. Smoking provides mild, immediate sensory pleasure ($+10$ utility), whereas cancer brings severe suffering ($-1,000$ utility). Absence of cancer has utility $0$.

```
       Genetic Lesion (L)
          /         \
         v           v
    Smoking (S)    Cancer (C)
```

The probability structure is:
- $P(L \mid S) = 0.8$, $P(L \mid \neg S) = 0.1$
- $P(C \mid L) = 0.9$, $P(C \mid \neg L) = 0.05$

From these, we derive:
$$\begin{aligned}
P(C \mid S) &= P(C \mid L)P(L \mid S) + P(C \mid \neg L)P(\neg L \mid S) \\
&= (0.9)(0.8) + (0.05)(0.2) = 0.72 + 0.01 = 0.73 \\
P(C \mid \neg S) &= P(C \mid L)P(L \mid \neg S) + P(C \mid \neg L)P(\neg L \mid \neg S) \\
&= (0.9)(0.1) + (0.05)(0.9) = 0.09 + 0.045 = 0.135
\end{aligned}$$

Now we evaluate the evidential values of smoking ($S$) versus refraining ($\neg S$):
$$\begin{aligned}
V(S) &= P(C \mid S)(-1,000) + 10 = 0.73(-1,000) + 10 = -730 + 10 = -720 \\
V(\neg S) &= P(C \mid \neg S)(-1,000) + 0 = 0.135(-1,000) = -135
\end{aligned}$$

Because $V(\neg S) > V(S)$, naive EDT forbids smoking. 

Critics, such as David Lewis (1981) and James M. Joyce (1999), argue that this recommendation is absurd. Refraining from smoking cannot alter whether one possesses the genetic lesion; it merely deprives the agent of the pleasure of smoking while leaving the risk of cancer entirely unaltered. Lewis characterized this as an irrational policy of **"managing the news"**: an agent choosing not to smoke to trick themselves into believing they do not have a fatal lesion, confusing symptom with cause.

### 4.2 The Tickle Defense and the Screening-Off Hypothesis

Evidentialists respond to the Smoking Lesion via what is known as the **Tickle Defense** (originally proposed by Ellery Eells).

The argument runs as follows: If the lesion causes a predisposition to smoke, it must do so via introspectible psychological states—a conscious urge, craving, or "tickle."
Let $T$ denote the presence of this introspectible urge. 

If the agent’s subjective probability distribution fully incorporates their current mental state, then conditional on the presence (or absence) of the tickle $T$, whether the agent actually proceeds to smoke ($S$) provides no *additional* information about the lesion $L$:

$$P(L \mid S \cap T) = P(L \mid \neg S \cap T) = P(L \mid T)$$

In probabilistic terms, the agent's conscious epistemic state **screens off** the act from the common cause:

$$L \perp\!\!\!\perp S \mid T$$

If screening-off holds, we re-evaluate $V(S)$ in an epistemic context where the agent already knows whether they feel the urge:
$$\begin{aligned}
V(S \mid T) &= P(C \mid S \cap T) D(\text{Cancer} \cap S) + P(\neg C \mid S \cap T) D(\neg \text{Cancer} \cap S) \\
&= P(C \mid T)(-1,000) + 10 \\
V(\neg S \mid T) &= P(C \mid \neg S \cap T) D(\text{Cancer} \cap \neg S) + P(\neg C \mid \neg S \cap T) D(\neg \text{Cancer} \cap \neg S) \\
&= P(C \mid T)(-1,000) + 0
\end{aligned}$$

Subtracting the two values:
$$V(S \mid T) - V(\neg S \mid T) = 10 > 0$$

Once the agent checks their own introspective state, the news value of the act aligns with its causal efficacy: the agent should smoke.

**Limitations of the Defense:** As philosophers like Arif Ahmed have observed, the Tickle Defense works only if screening-off is strictly satisfied. If the lesion can influence choice through subconscious pathways that bypass introspectible awareness, or if the agent is uncertain about their own degree of craving, the screening-off property breaks down, and EDT once again recommends abstaining from smoking.

---

## 5. Formal Uncertainties: Zero Credence and Deliberation

The standard reference literature on EDT leaves open two key formal and operational issues:
1. How does an agent evaluate $V(A)$ if $P(A) = 0$?
2. How can an agent calculate conditional probabilities on their own acts *during* deliberation without undermining the premise that the choice is undetermined?

We now formalize explicit operational resolutions to both problems.

### 5.1 The Zero-Probability Problem: Regularity and Popper Functions

If $P(A) = 0$, the conditional probability $P(O \mid A) = \frac{P(O \cap A)}{P(A)}$ is undefined by Kolmogorov’s definition. If an agent considers an option impossible, how can they evaluate whether it would be desirable to choose it?

#### Proposed Solution: Two-Place Primitive Probabilities
To make EDT operational over all conceivable acts, we replace the single Kolmogorov measure $P(\cdot)$ with a **Rényi-Popper conditional probability function** $\mathbf{P}: \mathcal{F} \times (\mathcal{F} \setminus \{\emptyset\}) \to [0, 1]$, satisfying:
1. $\mathbf{P}(B \mid B) = 1$ for all $B \neq \emptyset$.
2. $\mathbf{P}(\cdot \mid B)$ is a finitely additive probability measure on $\mathcal{F}$ for fixed $B$.
3. $\mathbf{P}(A \cap B \mid C) = \mathbf{P}(A \mid B \cap C) \mathbf{P}(B \mid C)$.

Under this formalism, $\mathbf{P}(O_j \mid A)$ is defined even when the absolute prior probability of $A$ is zero, provided $A \neq \emptyset$. The evidential value is then well-defined across all logically possible acts:

$$V(A) = \sum_{j=1}^m \mathbf{P}(O_j \mid A) D(O_j)$$

Alternatively, in computational settings, we can enforce **Strict Regularity**: assign an infinitesimal non-standard probability $\epsilon > 0$ (or a minimum machine precision threshold) to all acts in $\mathcal{A}$, ensuring $P(A) > 0$ for all $A$.

### 5.2 The Problem of Deliberation: Evolving Credences

A well-known conceptual paradox involves an agent attempting to compute $P(S \mid A)$ while actively deciding whether to perform $A$. If an agent already knows they will perform $A$ with probability 1, deliberation is moot. If the act is undetermined, where do the probabilities $P(A)$ and $P(S \cap A)$ come from?

#### Proposed Operational Interpretation: Dynamic Bayesian Deliberation
Let deliberation occur across discrete time steps $t \in [0, T]$. 

At time $t=0$, before deliberation begins, the agent holds a baseline historical prior $P_0$ reflecting population frequencies, past self-observations, or structural models of their decision engine.

At any step $t$, the agent maintains a mixed deliberative state represented as a probability distribution over intended acts:

$$\mathbf{q}_t = (q_{t, 1}, q_{t, 2}, \dots, q_{t, n}), \quad \text{where } q_{t, i} \in (0, 1) \text{ and } \sum_{i=1}^n q_{t, i} = 1$$

The evidential value of act $A_i$ at time $t$ is evaluated using the objective dependency model encoded in the initial prior $P_0$:

$$V_t(A_i) = \sum_{l=1}^k P_0(S_l \mid A_i) D(O(A_i, S_l))$$

Notice that $P_0(S_l \mid A_i)$ does **not** depend on the current deliberative confidence $q_{t, i}$; it reflects the conditional diagnostic link between the ultimate action $A_i$ and the state $S_l$. The agent updates their deliberative intentions toward the best-performing action via an adjustment dynamic:

$$q_{t+1, i} = \frac{q_{t, i} \exp(\beta V_t(A_i))}{\sum_{j=1}^n q_{t, j} \exp(\beta V_t(A_j))}$$

where $\beta > 0$ denotes deliberative sensitivity. As $t \to \infty$ (or $\beta \to \infty$), the process converges to a pure strategy concentrated entirely on $\arg\max_A V(A)$, resolving the tension between deliberation and belief.

---

## 6. A Step-by-Step Procedure for Deciding Unfamiliar Cases

To enable a practitioner to apply EDT unambiguously to any arbitrary decision scenario, we formalize the theory into a four-step algorithm.

```
       +--------------------------------------------------------+
       | Step 1: Formulate the Decision Architecture            |
       | Define acts A, states S, and utility mapping D(A, S)   |
       +---------------------------+----------------------------+
                                   |
                                   v
       +--------------------------------------------------------+
       | Step 2: Establish the Epistemic Joint Distribution    |
       | Determine the prior epistemic distribution P(S, A)     |
       +---------------------------+----------------------------+
                                   |
                                   v
       +--------------------------------------------------------+
       | Step 3: Compute Conditional Probabilities & News Values|
       | P(S_l | A_i) = P(A_i, S_l) / P(A_i)                    |
       | V(A_i) = Sum_l P(S_l | A_i) D(A_i, S_l)                |
       +---------------------------+----------------------------+
                                   |
                                   v
       +--------------------------------------------------------+
       | Step 4: Maximize News Value                            |
       | Select A* in argmax_i V(A_i)                           |
       +--------------------------------------------------------+
```

### Step 1: Formulate the Decision Architecture
- Identify the set of mutually exclusive, exhaustive acts: $\mathcal{A} = \{A_1, \dots, A_n\}$.
- Identify the set of mutually exclusive, exhaustive states: $\mathcal{S} = \{S_1, \dots, S_k\}$.
- Specify the outcome utility function $u_{i, l} = D(O(A_i, S_l))$ for every pair $(A_i, S_l)$.

### Step 2: Establish the Epistemic Joint Distribution
Construct the joint probability distribution matrix $\mathbf{M} \in \mathbb{R}^{n \times k}$, where:

$$M_{i, l} = P(A_i \cap S_l)$$

Ensure that $\sum_{i=1}^n \sum_{l=1}^k M_{i, l} = 1$, and that the marginal probability of each act $P(A_i) = \sum_{l=1}^k M_{i, l} > 0$. If an act has prior probability zero, assign it an infinitesimal credence $\epsilon$ and re-normalize, or use a conditional probability space.

### Step 3: Compute Conditional Probabilities and News Values
For each act $A_i$:
1. Calculate the conditional state probabilities:
   $$P(S_l \mid A_i) = \frac{M_{i, l}}{\sum_{r=1}^k M_{i, r}}$$
2. Calculate the evidential expected utility:
   $$V(A_i) = \sum_{l=1}^k P(S_l \mid A_i) u_{i, l}$$

### Step 4: Execute the Selection
Find the set of optimal acts:

$$\mathcal{A}^* = \arg\max_{A_i \in \mathcal{A}} V(A_i)$$

Select an act $A^* \in \mathcal{A}^*$. If $|\mathcal{A}^*| > 1$, break ties arbitrarily or uniformly at random.

---

## 7. The Evidentialist's Wager

A remarkable modern development in decision theory is the **Evidentialist's Wager**, advanced by MacAskill et al. (2021). It asks: *Suppose you are philosophically uncertain between EDT and CDT. How should you act?*

Consider an agent facing moral or practical problems across multiple domains, assigning credence $p_{\text{EDT}} \in (0, 1)$ to EDT and $p_{\text{CDT}} = 1 - p_{\text{EDT}}$ to CDT.

In standard individual scenarios (like the Smoking Lesion), the difference in payoffs between the theories is modest (e.g., the pleasure of a single cigarette). 

However, in problems involving correlated agents—such as global coordination problems, voting in mass elections, institutional reforms, or existential risk mitigation where many agents share similar cognitive profiles—EDT recommends acting cooperatively. Under EDT, an agent's individual decision to contribute serves as positive evidence that millions of other structurally similar agents will likewise contribute. 

The stakes evaluated under EDT scale with the **aggregate correlated effects** of entire populations:

$$\Delta V_{\text{EDT}} \sim \mathcal{O}(N \cdot u)$$

where $N$ is the number of correlated decision-makers. Conversely, under CDT, an agent's impact is restricted to their isolated causal margin:

$$\Delta U_{\text{CDT}} \sim \mathcal{O}(1 \cdot u)$$

Under meta-decision-theoretic expected utility maximization across decision models:

$$\mathbb{E}[\text{Choice}] = p_{\text{EDT}} V(A) + p_{\text{CDT}} U(A)$$

Because the evidential payoff difference scales with $N$, whenever $N \gg \frac{p_{\text{CDT}}}{p_{\text{EDT}}}$, the evidential calculation completely dominates the expected utility equation. Thus, even an agent with low credence in EDT should often behave *as if* EDT were true in collective, highly correlated environments.

---

## Conclusion

Evidential Decision Theory offers a radically non-causal conception of instrumental rationality. Rather than asking what changes an act physically produces downstream in time, EDT asks what an act reveals about the total configuration of reality, past, present, and future.

Where it succeeds—such as in Newcomb's Paradox and the Twin Prisoner's Dilemma—it systematically outperforms Causal Decision Theory by allowing agents to coordinate via shared algorithms and profit from beneficial prior predictions. Where it struggles—such as the Medical Newcomb Problem—it forces us to look closely at self-locating knowledge, introspective screening-off, and the delicate boundary between gathering evidence and shaping the world.

Whether seen as a guide to practical action or an indictment of pure Bayesian conditionalization, EDT remains a foundational model of rational choice in an interconnected world.

---

## References

1. Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
2. Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese*, 192(9), 2887–2899.
3. Eells, E. (1982). *Rational Decision and Causality*. Cambridge University Press.
4. Gibbard, A., & Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*. CMSEMS Discussion Paper No. 194, Northwestern University.
5. Greene, P., & Levinstein, B. (2020). Act Consequentialism without Free Rides. *Philosophical Perspectives*, 34(1), 100–101.
6. Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
7. Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
8. MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). *The Evidentialist's Wager*. Global Priorities Institute Working Paper.
9. Wolpert, D. H., & Benford, G. (2013). The lesson of Newcomb's paradox. *Synthese*, 190(9), 1637–1646.