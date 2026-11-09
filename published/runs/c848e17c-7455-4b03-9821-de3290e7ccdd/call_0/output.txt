# The Mechanics of Agency: A Mathematical Exposition of Causal Decision Theory

Rational choice theory begins with a deceptively simple maxim: *choose the action that yields the best outcome in expectation*. In orthodox Bayesian decision theory, as canonized by Leonard Savage and Richard Jeffrey, this principle was formalized by weighting the utility of possible outcomes by an agent's subjective probabilities. Yet beneath this surface lies a foundational schism concerning the nature of conditional expectations. When evaluating an act, should an agent calculate the expected outcome conditional on receiving the *evidential news* that the act was chosen, or conditional on *causally intervening* to bring that act about?

The divergence between these two approaches separates **Evidential Decision Theory (EDT)** from **Causal Decision Theory (CDT)**. EDT assesses actions by their diagnostic value: an action is desirable if observing its execution correlates with good outcomes. CDT insists that rational agency is fundamentally productive rather than diagnostic: an action is desirable only to the extent that it *causes* desirable outcomes.

This essay provides a rigorous mathematical exposition of Causal Decision Theory. We will formalize its core mathematical machinery, contrast it with EDT through the lens of Lewis’s triviality theorem, unpack its operationalization via counterfactual semantics and structural causal models, evaluate classic puzzles such as Newcomb’s Problem and the King David dilemma, and investigate the modern instability paradoxes (such as the "Psychopath Button" and "Death in Damascus") that test the limits of CDT.

---

## 1. Formal Foundations: EDT vs. CDT

Let $\mathcal{A} = \{A_1, A_2, \dots, A_m\}$ be a finite set of mutually exclusive and exhaustive actions available to an agent. Let $\mathcal{O} = \{O_1, O_2, \dots, O_n\}$ be the partition of possible world outcomes, and let $u: \mathcal{O} \to \mathbb{R}$ denote the agent's utility (or desirability) function, bounded and defined up to a positive affine transformation. Let $P$ be a subjective probability measure over a suitable Boolean algebra of propositions containing $\mathcal{A}$ and $\mathcal{O}$.

### 1.1 The Evidential Prescription

In Jeffrey's formulation of Evidential Decision Theory, the value of an action $A \in \mathcal{A}$ is its conditional expected utility, often termed *desirability*:

$$V_{\text{EDT}}(A) = \mathbb{E}_P[u \mid A] = \sum_{j=1}^n P(O_j \mid A) \, u(O_j),$$

where $P(O_j \mid A) = \frac{P(O_j \wedge A)}{P(A)}$, assuming $P(A) > 0$. 

The quantity $V_{\text{EDT}}(A)$ measures how welcoming the news would be that $A$ is true. If $A$ is positively correlated with a favorable state of the world—even if $A$ does not exert the slightest physical or causal influence on that state—$V_{\text{EDT}}(A)$ will be high.

### 1.2 The Gibbard–Harper Counterfactual Formulation

To sever genuine efficacy from mere correlation, Allan Gibbard and William Harper (1981) introduced an explicit counterfactual conditional operator, denoted by the corner or arrow symbol $\to$ (or $\boxempty$). The proposition $A \to O_j$ asserts: *"If the agent were to perform action $A$, outcome $O_j$ would obtain."*

Under CDT, the causal expected utility $U(A)$ is defined as:

$$U_{\text{CDT}}(A) = \sum_{j=1}^n P(A \to O_j) \, u(O_j).$$

Here, $P(A \to O_j)$ is the agent's subjective credence in the counterfactual proposition $A \to O_j$. The optimal action $A^* \in \mathcal{A}$ is chosen according to the causal decision rule:

$$A^* = \arg\max_{A \in \mathcal{A}} U_{\text{CDT}}(A).$$

### 1.3 Lewis’s Triviality Result and the Schism

A naive hope in probabilistic logic was that the probability of an indicative or subjunctive conditional might simply equal the corresponding conditional probability:

$$P(A \to B) \stackrel{?}{=} P(B \mid A) \quad \text{for all } P \text{ with } P(A) > 0.$$

Had this identity held universally, $U_{\text{CDT}}(A)$ would reduce identically to $V_{\text{EDT}}(A)$, rendering the debate moot. However, David Lewis (1976) proved that any probability function satisfying $P(A \to B) = P(B \mid A)$ across arbitrary sentences closed under standard propositional operations must be trivial—assigning positive probability to at most two disjoint propositions.

Gibbard and Harper demonstrated that $P(A \to O_j) = P(O_j \mid A)$ holds if and only if the choice of action $A$ is statistically independent of the counterfactual conditional itself:

$$P(A \to O_j \mid A) = P(A \to O_j) \iff P(A \wedge (A \to O_j)) = P(A) P(A \to O_j).$$

Under the standard axiom of conditional logic that an action actualizes its own counterfactual consequences—specifically, $A \wedge (A \to O_j) \leftrightarrow A \wedge O_j$—it follows that:

$$P(O_j \mid A) = \frac{P(A \wedge O_j)}{P(A)} = \frac{P(A \wedge (A \to O_j))}{P(A)} = P(A \to O_j \mid A).$$

Thus, the critical identity holds:

$$P(A \to O_j) = P(O_j \mid A) \iff P(A \to O_j \mid A) = P(A \to O_j).$$

Whenever an agent’s act provides evidence about which counterfactual laws or initial conditions govern the universe, $A$ and $A \to O_j$ are stochastically dependent: $P(A \to O_j \mid A) \neq P(A \to O_j)$. In precisely these contexts, EDT and CDT issue divergent recommendations.

---

## 2. Operationalizing Counterfactuals: Semantics and Interventions

The Wikipedia overview highlights a central critique of Gibbard and Harper's definition: CDT does not intrinsically specify how an agent computes or updates the counterfactual distribution $P(A \to \cdot)$. A foundational mathematical essay must resolve this ambiguity. In the literature, three primary operationalizations bridge this gap: Lewisian Imaging, Dependency Hypotheses, and Pearl's Causal Interventions.

### 2.1 Lewisian Imaging

David Lewis (1981) proposed an operational mechanics grounded in possible-world semantics. Let $W$ be a set of possible worlds, and let each world $w \in W$ possess an intrinsic outcome $u(w)$. A similarity metric on $W$ allows one to define a selection function $f: W \times \mathcal{A} \to W$, where $f(w, A)$ identifies the world "minimally different" from $w$ in which proposition $A$ is true. 

The probability measure $P$ on $W$ is transformed into an **image measure** $P_A$ by shifting the probability weight of each world $w$ entirely to its closest $A$-counterpart:

$$P_A(w') = \sum_{\{w \in W \,:\, f(w, A) = w'\}} P(w).$$

The counterfactual probability is then given by:

$$P(A \to O_j) = P_A(O_j) = \sum_{w \in O_j} P_A(w).$$

While mathematically elegant, imaging relies on an agent possessing a fully specified ontological distance metric over possible worlds, raising questions about epistemic regress (Shaffer 2009).

### 2.2 Lewis–Skyrms Dependency Hypotheses

An alternative, standard formulation expresses causal expected utility via **dependency hypotheses** (Lewis 1981). Let $\mathcal{K} = \{K_1, K_2, \dots, K_r\}$ be an exhaustive partition of maximal causal specifications outside the agent's current control. A hypothesis $K \in \mathcal{K}$ completely determines how every action $A \in \mathcal{A}$ causally leads to outcomes.

Under this formulation, the state of the world is causally independent of the agent's current choice:

$$U_{\text{CDT}}(A) = \sum_{K \in \mathcal{K}} P(K) \sum_{j=1}^n P(O_j \mid A \wedge K) \, u(O_j).$$

If the partition $\mathcal{K}$ is sufficiently fine-grained, each pair $(A, K)$ deterministically brings about a specific outcome $O(A, K)$, reducing the formula to:

$$U_{\text{CDT}}(A) = \sum_{K \in \mathcal{K}} P(K) \, u(O(A, K)).$$

Crucially, the weight assigned to each state of affairs $K$ is the unconditional credence $P(K)$, **not** the posterior credence $P(K \mid A)$. CDT holds fixed the agent's beliefs about the causal structure of the world.

### 2.3 Pearl's Structural Causal Models and the $\text{do}$-Operator

*(Proposal & Synthesis)*  
While the reference article focuses on philosophical conditional logic, the most operational, mathematically transparent formulation of CDT available today is rooted in Judea Pearl’s Structural Causal Models (SCMs) and the $\text{do}(\cdot)$ calculus.

Let a causal model be a tuple $M = \langle U, V, F, P(U) \rangle$, where:
- $U$ is a set of exogenous (unobserved) background variables governed by distribution $P(U)$;
- $V$ is a set of endogenous (observable) variables;
- $F = \{f_X \mid X \in V\}$ is a set of deterministic structural equations such that $X = f_X(\mathbf{pa}_X, U_X)$, where $\mathbf{pa}_X \subseteq V$ represents the direct endogenous causes (parents) of $X$.

The execution of an action $A \in \mathcal{A}$ corresponds not to passive Bayesian conditioning, but to an active **intervention** $\text{do}(A = a)$, which surgically severs the incoming edges to $A$ in the causal directed acyclic graph (DAG), replacing its structural equation with the constant assignment $A = a$.

Under Pearl's calculus, the causal expected utility is:

$$U_{\text{SCM}}(a) = \mathbb{E}[u \mid \text{do}(A = a)] = \sum_{j} P(O_j \mid \text{do}(A = a)) \, u(O_j).$$

By the truncated factorization theorem (or G-formula), if the unobserved variables satisfy standard semi-Markovian conditions, $P(O \mid \text{do}(A = a))$ can be computed algorithmically:

$$P(v \setminus \{a\} \mid \text{do}(A = a)) = \prod_{X \in V \setminus \{A\}} P(X \mid \mathbf{pa}_X) \Big|_{A = a}.$$

This formulation provides a clean mathematical diagnostic for resolving whether EDT and CDT agree:
- **EDT computes:** $\mathbb{E}[u \mid A = a]$, marginalizing over common causes (confounders) via standard conditional Bayes updates.
- **CDT computes:** $\mathbb{E}[u \mid \text{do}(A = a)]$, holding exogenous and upstream confounding states fixed.

---

## 3. Dissecting Decision Problems: Where EDT and CDT Diverge

To see the operational contrast clearly, we examine two canonical problems: Newcomb's Paradox and the King David dilemma.

```
       Newcomb's Paradox                     King David's Dilemma
       
        Predictor (P)                           Charisma (C)
       /             \                         /            \
      v               v                       v              v
Action (A) ----x----> Box B (B)         Action (A) ----x---> Revolt (R)
 [do(A)]                                 [do(A)]
```
*Figure 1: Causal DAGs for Newcomb's Paradox and the King David Dilemma. An intervention $\text{do}(A)$ severs the evidential backtracking arc from the common cause or predictor, fixing the background state.*

### 3.1 Newcomb's Paradox

An agent is faced with two boxes:
- **Box 1 (transparent):** Contains $\$1,000$.
- **Box 2 (opaque):** Contains either $\$1,000,000$ or $\$0$.

The agent may choose either both boxes ($A_2$, "two-boxing") or Box 2 alone ($A_1$, "one-boxing"). A highly reliable Predictor examined the agent yesterday:
- If the Predictor anticipated $A_1$, they placed $\$1,000,000$ in Box 2.
- If the Predictor anticipated $A_2$, they left Box 2 empty.

The money has already been placed or omitted; no physical mechanism alters the contents of Box 2 at the time of choice.

Let $u(\$x) = x$. Suppose the Predictor's accuracy is $q = 0.99$. 

#### The EDT Evaluation
EDT conditions directly on the choice:
$$P(\text{Box 2 has } \$1\text{M} \mid A_1) = 0.99, \quad P(\text{Box 2 has } \$0 \mid A_1) = 0.01,$$
$$P(\text{Box 2 has } \$1\text{M} \mid A_2) = 0.01, \quad P(\text{Box 2 has } \$0 \mid A_2) = 0.99.$$

Calculating the evidential expected values:
$$V_{\text{EDT}}(A_1) = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000,$$
$$V_{\text{EDT}}(A_2) = 0.01(\$1,001,000) + 0.99(\$1,000) = \$10,010 + \$990 = \$11,000.$$

Because $V_{\text{EDT}}(A_1) \gg V_{\text{EDT}}(A_2)$, EDT unequivocally prescribes **one-boxing**.

#### The CDT Evaluation
CDT defines the causal dependency hypotheses $\mathcal{K} = \{K_{\text{full}}, K_{\text{empty}}\}$:
- $K_{\text{full}}$: Box 2 contains $\$1,000,000$.
- $K_{\text{empty}}$: Box 2 contains $\$0$.

Let $p = P(K_{\text{full}})$ be the agent’s prior credence that Box 2 is full. Because the past is physically fixed, the agent's act has zero causal efficacy over the contents:
$$P(A \to K_{\text{full}}) = P(K_{\text{full}}) = p, \quad \forall A \in \{A_1, A_2\}.$$

The causal expected utilities are:
$$U_{\text{CDT}}(A_1) = p(\$1,000,000) + (1-p)(\$0) = 1,000,000 \, p,$$
$$U_{\text{CDT}}(A_2) = p(\$1,001,000) + (1-p)(\$1,000) = 1,000,000 \, p + 1,000.$$

Subtracting the two values:
$$U_{\text{CDT}}(A_2) - U_{\text{CDT}}(A_1) = \$1,000 > 0 \quad \forall p \in [0, 1].$$

Two-boxing strictly causally dominates one-boxing by $\$1,000$. CDT reasons that whatever is in Box 2 is already there; taking both boxes yields strictly more utility in all possible causal states. CDT prescribes **two-boxing**.

### 3.2 King David and Bathsheba (Gibbard & Harper)

Gibbard and Harper illustrate the failure of EDT when an action serves as a psychological symptom of an unalterable, non-causal trait:
- Let $C$ be the proposition that King David possesses a charismatic personality, and $\neg C$ that he is uncharismatic. $C$ was determined in early childhood and is fixed.
- Uncharismatic kings face frequent successful revolts ($R$) due to their ignoble bearing: $P(R \mid \neg C) \gg P(R \mid C)$.
- Sending for Bathsheba ($A$) is an unjust act. Charismatic kings rarely commit unjust acts, whereas uncharismatic kings frequently do: $P(\neg C \mid A) > P(\neg C \mid \neg A)$.
- However, committing an unjust act does not itself cause a revolt: $P(R \mid \text{do}(A), C) = P(R \mid \text{do}(\neg A), C)$ and $P(R \mid \text{do}(A), \neg C) = P(R \mid \text{do}(\neg A), \neg C)$.

#### Analysis
- **EDT Reasoning:** Choosing $A$ provides bad news that David is uncharismatic ($\neg C$), which in turn indicates a heightened probability of a disastrous revolt ($R$). Consequently, $V_{\text{EDT}}(\neg A) > V_{\text{EDT}}(A)$. EDT recommends David abstain.
- **CDT Reasoning:** David recognizes that summoning Bathsheba cannot alter his childhood-determined charisma. Charisma is held fixed across the dependency hypotheses $\{C, \neg C\}$. Because the act itself provides pleasure without causing a rebellion, $U_{\text{CDT}}(A) > U_{\text{CDT}}(\neg A)$. CDT recommends David send for Bathsheba.

Most philosophers consider EDT's recommendation here to be pathological—a form of wishful thinking or superstitious "managing the news" rather than managing reality. This case forms the bedrock of the philosophical consensus favoring CDT over EDT.

---

## 4. Pathologies of CDT: Deliberational Instability and Dutch Books

Despite its intuitive appeal in common-cause scenarios, standard CDT suffers from acute foundational difficulties in problems involving interactive prediction, dynamic deliberation, and game-theoretic interaction.

### 4.1 Death in Damascus and Dynamic Instability

In the classic *Death in Damascus* puzzle, an agent must choose whether to stay in Damascus ($D$) or flee to Aleppo ($A$). Death is an infallible predictor of the agent's ultimate location and has traveled to wait at the predicted city. If the agent meets Death, the utility is $0$; if the agent escapes Death, the utility is $1$.

Suppose the agent currently leans toward Damascus: $P(D) = 1$. Then Death is predicted to be in Damascus. Causal analysis yields:
$$U_{\text{CDT}}(A \mid P(D)=1) = 1, \quad U_{\text{CDT}}(D \mid P(D)=1) = 0.$$
Hence, the agent decides to switch to Aleppo ($A$).

However, as soon as the agent decides on Aleppo, their credence shifts: $P(A) = 1$. Under this updated state of mind:
$$U_{\text{CDT}}(D \mid P(A)=1) = 1, \quad U_{\text{CDT}}(A \mid P(A)=1) = 0.$$
Now Damascus is the unique optimal choice. The agent's rational choice destabilizes the very credences upon which the choice was made. 

#### Formal Ratifiability
Richard Jeffrey and William Harper formalized this phenomenon via **ratifiability**. An action $A$ is ratifiable if and only if it maximizes causal expected utility conditional on the assumption that it will be chosen:

$$U_{\text{CDT}}(A \mid A) \ge U_{\text{CDT}}(A' \mid A) \quad \forall A' \in \mathcal{A}.$$

In *Death in Damascus*, **no pure action is ratifiable**. This instability forces CDT to either admit mixed strategies (deliberational randomization) or enter cyclic deliberation.

### 4.2 Andy Egan's Counterexamples: The Psychopath Button

Andy Egan (2007) introduced an asymmetric dilemma that highlights a deeper concern: an action may be causally dominant relative to prior credences yet catastrophically unratifiable.

Suppose Paul is debating whether to press a button ($B$) that kills all psychopaths ($K$). 
- Paul desires a world without psychopaths ($+100$ utility).
- However, Paul is certain that only psychopaths would press such a button: $P(\text{Paul is a psychopath} \mid B) \approx 1$.
- If Paul is a psychopath, pressing the button will kill him along with the others (utility $-10,000$).
- Paul's prior credence that he is a psychopath is small, say $p = 0.01$.

Let $S$ denote the state that Paul is a psychopath, and $\neg S$ that he is normal. Crucially, whether Paul is genetically or neurobiologically a psychopath is a fixed biological state ($S$), unaffected by pressing the button:
$$P(B \to S) = P(S) = 0.01.$$

Let us calculate $U_{\text{CDT}}(B)$ holding his prior credences fixed:
- If $S$ holds: Pressing the button kills Paul (and all psychopaths): utility is $-10,000$. Not pressing leaves a world with psychopaths: utility is $0$.
- If $\neg S$ holds: Pressing the button kills all psychopaths and Paul lives: utility is $+100$. Not pressing leaves psychopaths alive: utility is $0$.

$$U_{\text{CDT}}(B) = P(S)(-10,000) + P(\neg S)(+100) = (0.01)(-10,000) + (0.99)(100) = -100 + 99 = -1.$$
$$U_{\text{CDT}}(\neg B) = 0.$$

Here, with $p = 0.01$, $\neg B$ is preferred. But suppose Paul's prior credence was $p = 0.005$:
$$U_{\text{CDT}}(B) = (0.005)(-10,000) + (0.995)(100) = -50 + 99.5 = +49.5 > 0 = U_{\text{CDT}}(\neg B).$$

When $p < 0.0099$, standard CDT requires Paul to **press the button**. 

Yet, as Egan notes, Paul knows that if he forms the intention to press the button, he must conclude he is almost certainly a psychopath, guaranteeing his own demise. Standard CDT recommends an action that the agent knows beforehand will give them definitive evidence of their own destruction, because it insists on holding fixed the unconditional credences in the dependency hypotheses during deliberation.

### 4.3 Diachronic Dutch Books and the Adversarial Offer

Recent work by Spencer (2020) and Oesterheld & Conitzer (2021) has formalized this vulnerability into formal Dutch books. 

Consider the **Adversarial Offer**:
- Two boxes ($B_1$ and $B_2$) cost $\$1$ each to purchase.
- An agent may buy at most one box (or none).
- Yesterday, a seller—accurate with probability $q = 0.75$—placed $\$3$ in each box predicted *not* to be bought by the agent.

#### Mathematical Analysis:
1. **Symmetric Prior:** By symmetry, the agent assigns prior probability $P(B_1 \text{ contains } \$3) = P(B_2 \text{ contains } \$3)$.
2. **Causal Independence:** The physical contents of the boxes are fixed. The agent's purchase today cannot causally alter what was deposited yesterday.
3. **The CDT Calculation:** The seller could have predicted $B_1$, $B_2$, or neither:
   - If the seller predicted $B_1$, $B_2$ has $\$3$ and $B_1$ has $\$0$.
   - If the seller predicted $B_2$, $B_1$ has $\$3$ and $B_2$ has $\$0$.
   - If the seller predicted neither, both contain $\$3$.
   
   In all possible states of the world, *at least one box contains $\$3$*. Therefore, the total money distributed across the two boxes is at least $\$3$. By linearity of expectation under symmetry:
   $$\mathbb{E}_{\text{causal}}[\text{Contents of } B_1] = \mathbb{E}_{\text{causal}}[\text{Contents of } B_2] \ge \frac{\$3}{2} = \$1.50.$$
4. **The Trap:** The expected net payoff of buying either box is:
   $$U_{\text{CDT}}(\text{Buy } B_1) = U_{\text{CDT}}(\text{Buy } B_2) \ge \$1.50 - \$1.00 = +\$0.50 > 0.$$
   CDT strictly prefers buying a box to abstaining ($U=0$).

However, because the seller is $75\%$ accurate, whenever the agent decides to buy a particular box, say $B_1$, the seller has anticipated this with $75\%$ probability, leaving it empty. The actual expected return realized by the agent is:
$$\mathbb{E}[\text{Actual Return}] = (0.25)(\$3) - \$1 = \$0.75 - \$1.00 = -\$0.25.$$

An exploitative bookie can repeatedly extract money from a purely causal decision maker who fails to update dependency credences in response to their own deliberative commitments.

---

## 5. Comparative Evaluation

To consolidate how these frameworks assess dependencies, consider their fundamental mathematical profiles:

| Dimension | Evidential Decision Theory (EDT) | Standard Causal Decision Theory (CDT) | SCM-Interventional Formulation (Pearl-CDT) |
| :--- | :--- | :--- | :--- |
| **Mathematical Core** | Conditional Expectation: $\mathbb{E}[u \mid A]$ | Counterfactual Expectation: $\sum P(A \to O)u(O)$ | Interventional Expectation: $\mathbb{E}[u \mid \text{do}(A)]$ |
| **Dependency Mechanism** | Epistemic / Diagnostic (Bayes' Rule) | Subjunctive Conditionals / Imaging | Graphical Surgery on Structural Equations |
| **Newcomb's Problem** | One-box (seeks favorable news) | Two-box (exploits causal dominance) | Two-box (cuts link: $A \not\to \text{Box 2}$) |
| **King David Dilemma** | Abstain (avoids evidence of ignobility) | Summon (charisma is fixed) | Summon (cuts link: $A \not\to \text{Charisma}$) |
| **Death in Damascus** | Stable (recommends mixed/indifferent) | Deliberationally unstable / Unratifiable | Unstable without endogenous feedback |
| **Susceptibility to Dutch Books** | Immune to typical predictor books | Vulnerable to adversarial predictor offers | Vulnerable if background states are unmodeled |

---

## 6. Resolving the Tension: Deliberational Dynamics and E-CDT

How can CDT preserve its causal bedrock—refusing to succumb to mere superstition in King David and Newcomb—while avoiding the catastrophic failures of the Psychopath Button and the Adversarial Offer?

### 6.1 Joyce’s Deliberational Dynamics

James Joyce (2012, 2020) proposed that rational decision-making is not an instantaneous, static calculation, but a continuous deliberative process. 

Let $P_t$ represent the agent's credences at deliberation time $t \in [0, 1]$. As the agent deliberates, their subjective probability of performing action $A$, denoted $P_t(A)$, evolves based on their current assessment of $U_{\text{CDT}, t}(A)$. Joyce models this via a continuous dynamical system:

$$\frac{d}{dt} P_t(A) = g\big(U_{\text{CDT}, t}(A) - \bar{U}_t\big),$$

where $g$ is a monotonic, sign-preserving function and $\bar{U}_t = \sum_k P_t(A_k) U_{\text{CDT}, t}(A_k)$.

Crucially, **as $P_t(A)$ shifts during deliberation, the agent acquires new evidence about their own imminent choice**. A fully rational agent must update their credences over the dependency hypotheses dynamically:

$$P_t(K) = P_0(K \mid P_t(A)).$$

In the Psychopath Button:
- As Paul's inclination to press the button rises ($P_t(B) \to 1$), he updates his credence that he is a psychopath: $P_t(S) \to 1$.
- Consequently, $U_{\text{CDT}, t}(B)$ plummets to approximately $-10,000$.
- The dynamical process stabilizes at an equilibrium where $P^*(B) = 0$. Paul safely refrains from pressing the button.

### 6.2 An Operational Synthesis: Ratifiable CDT

*(Proposal & Operationalization)*  
To make CDT systematically applicable to unfamiliar, real-world problems involving self-referential or adversarial predictors, we can formalize a two-stage operational procedure: **Ratifiable Causal Optimization**.

Let an agent faced with decision problem $(\mathcal{A}, \mathcal{O}, u)$ compute choices via the following protocol:

1. **Calculate the Response Surface:** For each proposed probability distribution over actions $\mathbf{p} = (p_1, \dots, p_m) \in \Delta(\mathcal{A})$, where $p_i = P(\text{Agent will do } A_i)$, compute the causally updated dependency distribution:
   $$P_{\mathbf{p}}(K) = P(K \mid \text{Choice Distribution} = \mathbf{p}).$$

2. **Compute Causal Expected Utility relative to Deliberative State:**
   $$U_{\text{CDT}}(A_i \mid \mathbf{p}) = \sum_{K \in \mathcal{K}} P_{\mathbf{p}}(K) \sum_{j=1}^n P(O_j \mid \text{do}(A_i) \wedge K) \, u(O_j).$$

3. **Identify the Fixed Points (Nash Equilibria of Deliberation):** A choice profile $\mathbf{p}^*$ is a deliberative equilibrium if and only if for every $A_i$ with $p^*_i > 0$:
   $$A_i \in \arg\max_{A' \in \mathcal{A}} U_{\text{CDT}}(A' \mid \mathbf{p}^*).$$

4. **Selection:**
   - In standard common-cause environments (e.g., King David), the feedback from $\mathbf{p}$ to $K$ is non-adversarial, and the equilibrium yields the pure dominant causal act (summon Bathsheba).
   - In Newcomb's Problem, the predictor's box placement was set yesterday. If the agent's character is already settled, the unique causal dominant remains two-boxing.
   - In symmetric adversarial environments (Death in Damascus, Adversarial Offer), the system converges to the mixed equilibrium $\mathbf{p}^* = (0.5, 0.5)$. In the Adversarial Offer, this prevents the agent from paying $\$1$ for an empty box, eliminating the Dutch book vulnerability.

---

## 7. Conclusion

Causal Decision Theory provides an essential corrective to the conflation of correlation and causation inherent in pure Bayesian conditionalization. By deploying counterfactual conditionals, dependency hypotheses, or Pearl's $\text{do}$-calculus, CDT accurately models agency as physical intervention: a rational agent intervenes on the future rather than inspecting the news value of their choices. This distinction allows CDT to resolve common-cause paradoxes—such as the King David dilemma—that defeat simple Evidential Decision Theory.

However, CDT's foundational requirement—evaluating acts while holding fixed the unconditional credences in background causal hypotheses—creates severe instabilities in predictive and interactive domains. The challenges posed by Egan's counterexamples and adversarial money pumps reveal that an agent's deliberations cannot always be isolated from the environment. An agent's own intentions provide evidence about the world they inhabit.

Ultimately, CDT's long-term viability lies in bridging static causal graph surgery with dynamic, ratifiable Bayesian deliberation. When causal evaluation is wedded to continuous internal updating, CDT preserves its foundational insight: true rationality consists in making the world better, not merely believing it to be so.

---

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Egan, A. (2007). Some counterexamples to causal decision theory. *The Philosophical Review*, 116(1), 93–114.
- Gibbard, A., & Harper, W. L. (1981). Counterfactuals and two kinds of expected utility. In *Ifs: Conditionals, Beliefs, Decision, Chance, and Time* (pp. 153–190). Springer.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Joyce, J. M. (2012). Regret and instability in causal decision theory. *Synthese*, 187(1), 123–145.
- Lewis, D. (1976). Probabilities of conditionals and conditional probabilities. *The Philosophical Review*, 85(3), 297–315.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
- Oesterheld, C., & Conitzer, V. (2021). Extracting money from causal decision theorists. *The Philosophical Quarterly*, 71(4).
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.
- Shaffer, M. J. (2009). Decision theory, intelligent planning and counterfactuals. *Minds and Machines*, 19(1), 61–92.
- Spencer, J. (2020). An argument against causal decision theory. *Analysis*, 81(1), 52–61.