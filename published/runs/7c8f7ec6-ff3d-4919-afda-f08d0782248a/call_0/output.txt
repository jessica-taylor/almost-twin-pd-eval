# The Mechanics of Agency: A Mathematical Exposition of Causal Decision Theory

Rational choice theory rests upon an intuitive maxim: an agent faced with several mutually exclusive courses of action ought to choose the one that brings about the best outcome in expectation. Yet formalizing what it means to *bring about* an outcome has provoked one of the most foundational schisms in modern decision theory. 

The orthodox Bayesian approach, codified in Evidential Decision Theory (EDT), evaluates an action by calculating the expected utility of the world conditional on the evidence that the action has been chosen. While computationally straightforward, EDT can conflate *correlation* with *causation*. When an action serves as a diagnostic sign of an unalterable state of affairs, EDT can recommend taking or avoiding that action merely to "manage the news" of what kind of world the agent inhabits.

**Causal Decision Theory (CDT)** emerged as an explicit mathematical correction to this flaw. CDT insists that an act must be evaluated not by what its performance portends, but by what its physical intervention counterfactually causes. 

Below, we develop the mathematical foundations of CDT, formalize its mechanics across classic decision puzzles, contrast it with EDT, explore operational interpretations (such as Lewisian imaging and Judea Pearl’s structural causal models), and assess the serious theoretical challenges—from instability to diachronic exploitation—that define contemporary debates in the foundations of rational agency.

---

## 1. Mathematical Foundations and the Core Formalism

Let $\mathcal{A} = \{A_1, A_2, \dots, A_m\}$ be a finite set of mutually exclusive and exhaustive actions available to an agent, and let $\mathcal{O} = \{O_1, O_2, \dots, O_n\}$ be a partition of possible outcomes. The desirability of each outcome is represented by a von Neumann–Morgenstern utility function $u: \mathcal{O} \to \mathbb{R}$, which Gibbard and Harper denote as $D(O_j)$.

### 1.1 The Gibbard–Harper Formulation

In their seminal 1981 formulation, Allan Gibbard and William Harper define the causal expected utility $U(A)$ of an act $A \in \mathcal{A}$ in terms of the probabilities of counterfactual conditionals:

$$U_{\mathrm{CDT}}(A) = \sum_{j=1}^n P(A \mathbin{\Box\to} O_j) \, u(O_j)$$

Here, $A \mathbin{\Box\to} O_j$ is the counterfactual proposition: *"If the agent were to perform act $A$, then outcome $O_j$ would obtain."* The function $P$ represents the agent’s subjective credence function defined over an algebra of propositions including these conditionals.

This contrasts directly with the evidential expected utility $V(A)$ advanced by Richard Jeffrey:

$$V_{\mathrm{EDT}}(A) = \sum_{j=1}^n P(O_j \mid A) \, u(O_j) = \sum_{j=1}^n \frac{P(A \cap O_j)}{P(A)} \, u(O_j)$$

The central divergence between CDT and EDT reduces mathematically to the divergence between the probability of a counterfactual conditional $P(A \mathbin{\Box\to} O_j)$ and the standard conditional probability $P(O_j \mid A)$.

### 1.2 Lewis's Triviality Result and the Non-Identity of Conditionals

One might ask whether a special conditional connective could be constructed such that the probability of the conditional equals the conditional probability:

$$P(A \mathbin{\to} B) \stackrel{?}{=} P(B \mid A) \quad \text{for all } P \text{ with } P(A) > 0$$

David Lewis (1976) proved that this equality cannot hold generally without collapsing the underlying probability algebra. Specifically, if a non-trivial probability function (one assigning positive probability to more than two mutually disjoint propositions) is closed under conditionalization, no conditional connective $\to$ can satisfy $P(A \to B) = P(B \mid A)$ universally. Consequently, causal expected utility cannot simply be reduced to evidential conditioning; evaluating counterfactuals demands an independent formal apparatus.

Gibbard and Harper demonstrated that $P(A \mathbin{\Box\to} O_j) = P(O_j \mid A)$ holds if the act $A$ is statistically independent of the counterfactual conditional $A \mathbin{\Box\to} O_j$:

$$P\bigl((A \mathbin{\Box\to} O_j) \mid A\bigr) = P(A \mathbin{\Box\to} O_j)$$

Under this condition, and assuming the Principle of the Conditional Excluded Middle—which asserts that $(A \mathbin{\Box\to} B) \lor (A \mathbin{\Box\to} \neg B)$ is a tautology—the evidential and causal calculations coincide. However, when an agent's choice correlates with the background conditions that govern the consequences of that choice (without the choice causing those conditions), statistical independence fails, and the recommendations of CDT and EDT diverge.

### 1.3 Causal Dependency Hypotheses and the K-Partition

David Lewis (1981) and Paul Weirich provided an alternative, highly tractable formulation that bypasses counterfactual logics by conditioning on **dependency hypotheses**. 

Let $\mathcal{K} = \{K_1, K_2, \dots, K_r\}$ be a mutually exclusive and exhaustive partition of maximal causal specifications of the world. A dependency hypothesis $K \in \mathcal{K}$ completely describes all factors that are causally independent of the agent's current choice but which, in conjunction with the chosen act $A$, deterministically or probabilistically dictate the outcome.

Under this partition, the causal expected utility can be rewritten as:

$$U_{\mathrm{CDT}}(A) = \sum_{k=1}^r P(K_k) \sum_{j=1}^n P(O_j \mid A \land K_k) \, u(O_j)$$

If $A$ and $K_k$ deterministically yield an outcome $O(A, K_k)$, the equation simplifies to:

$$U_{\mathrm{CDT}}(A) = \sum_{k=1}^r P(K_k) \, u\bigl(O(A, K_k)\bigr)$$

Notice the crucial structural feature of this equation: the weighting assigned to state $K_k$ is the **unconditional** prior credence $P(K_k)$, *not* the conditional credence $P(K_k \mid A)$. CDT holds fixed the agent's beliefs about the background state of the world when evaluating an action, precisely because the act cannot exert backwards or common-cause influence on which $K_k$ obtains.

---

## 2. Classic Divergences: Newcomb's Problem and Common Causes

To see how these formalisms operate in practice, we examine two canonical problems: Newcomb's Paradox and the case of David and Bathsheba.

### 2.1 Newcomb's Paradox

An agent is presented with two boxes:
- **Box A** is transparent and contains $\$1,000$.
- **Box B** is opaque and contains either $\$1,000,000$ or $\$0$.

The agent can choose either to take both boxes (**Two-Boxing**, $A_2$) or only the opaque box (**One-Boxing**, $A_1$). 
A highly reliable Predictor examined the agent's brain state yesterday:
- If the Predictor predicted the agent would choose $A_1$, she placed $\$1,000,000$ in Box B.
- If the Predictor predicted the agent would choose $A_2$, she left Box B empty.

Assume the Predictor's accuracy is $q = 0.99$, and let utility be linear in dollars: $u(\$x) = x$.

```
                      [ Predictor's Prediction ]
                             /          \
                            v            v
                 [ Box B Contents ]   [ Agent's Choice ]
                  ($1M or $0)          (A1 or A2)
```

#### The Evidential Calculation:
EDT calculates:
$$V(A_1) = P(B = \$1\mathrm{M} \mid A_1) \cdot 1{,}000{,}000 + P(B = \$0 \mid A_1) \cdot 0 = (0.99)(1{,}000{,}000) = \$990{,}000$$

$$V(A_2) = P(B = \$1\mathrm{M} \mid A_2) \cdot 1{,}001{,}000 + P(B = \$0 \mid A_2) \cdot 1{,}000 = (0.01)(1{,}001{,}000) + (0.99)(1{,}000) = \$11{,}000$$

Since $V(A_1) \gg V(A_2)$, EDT decisively recommends **One-Boxing**. Choosing $A_1$ provides exceptional news: it indicates that the agent is almost certainly a millionaire.

#### The Causal Calculation:
CDT models the world using the dependency hypotheses $\mathcal{K} = \{K_{\mathrm{full}}, K_{\mathrm{empty}}\}$, denoting whether Box B currently contains $\$1,000,000$ or $\$0$. The contents of Box B were fixed yesterday; the agent's immediate physical choice cannot causally alter Box B's contents.

Let $p = P(K_{\mathrm{full}})$ be the agent's subjective probability that Box B is full. CDT evaluates:
$$U(A_1) = p \cdot u(O(A_1, K_{\mathrm{full}})) + (1-p) \cdot u(O(A_1, K_{\mathrm{empty}})) = p(1{,}000{,}000) + (1-p)(0) = 1{,}000{,}000p$$

$$U(A_2) = p \cdot u(O(A_2, K_{\mathrm{full}})) + (1-p) \cdot u(O(A_2, K_{\mathrm{empty}})) = p(1{,}001{,}000) + (1-p)(1{,}000) = 1{,}000{,}000p + 1{,}000$$

For any prior credence $p \in [0, 1]$:
$$U(A_2) - U(A_1) = 1{,}000 > 0$$

Taking both boxes strictly dominates taking only one box across all causal states of the world. CDT insists that Box B is already either full or empty. If it is full, two-boxing yields $\$1,001,000$ versus $\$1,000,000$. If it is empty, two-boxing yields $\$1,000$ versus $\$0$. Because the agent cannot causally reach back in time to alter the predictor's past entry, leaving Box A behind is, from the causal perspective, needlessly discarding $\$1,000$.

### 2.2 Common Cause and Medical Newcomb Problems: David and Bathsheba

The superiority of CDT is often defended using scenarios where an act is merely symptomatic of a pre-existing condition. Consider Gibbard and Harper's example of King David:

1. Kings are either *charismatic* ($C$) or *uncharismatic* ($\neg C$). Charisma is fixed genetically and cannot be modified.
2. Charismatic kings rarely face successful revolts ($R$); uncharismatic kings face revolts frequently.
3. Unjust acts (such as summoning Bathsheba, denoted by $A$) do not cause revolts; revolts are caused entirely by a king's general ignoble bearing, which is an involuntary manifestation of lacking charisma.
4. However, uncharismatic kings are far more inclined to commit unjust acts than charismatic kings: $P(\neg C \mid A) \gg P(\neg C \mid \neg A)$.

David strongly desires Bathsheba ($u_{\text{appetite}}$), but fears a successful revolt (a severe penalty $-L$).

#### EDT's Reasoning:
Because committing the unjust act $A$ is a strong statistical indicator of lacking charisma, $P(R \mid A) \approx P(R \mid \neg C) P(\neg C \mid A)$ is high. EDT computes:
$$V(A) = u_{\text{appetite}} - L \cdot P(R \mid A)$$
$$V(\neg A) = 0 - L \cdot P(R \mid \neg A)$$
If $L$ is large, $V(\neg A) > V(A)$. EDT counsels David to abstain from summoning Bathsheba, treating restraint as reassuring evidence that he possesses charisma.

#### CDT's Reasoning:
CDT identifies the dependency partition $\mathcal{K} = \{C, \neg C\}$. Because summoning Bathsheba cannot causally produce or erase charisma, the counterfactual conditionals are:
$$P(A \mathbin{\Box\to} R \mid C) = P(\neg A \mathbin{\Box\to} R \mid C) = P(R \mid C)$$
$$P(A \mathbin{\Box\to} R \mid \neg C) = P(\neg A \mathbin{\Box\to} R \mid \neg C) = P(R \mid \neg C)$$

Thus:
$$U(A) = P(C)\bigl[u_{\text{appetite}} - L \cdot P(R \mid C)\bigr] + P(\neg C)\bigl[u_{\text{appetite}} - L \cdot P(R \mid \neg C)\bigr] = u_{\text{appetite}} - L \cdot P(R)$$
$$U(\neg A) = P(C)\bigl[- L \cdot P(R \mid C)\bigr] + P(\neg C)\bigl[- L \cdot P(R \mid \neg C)\bigr] = - L \cdot P(R)$$

Since $u_{\text{appetite}} > 0$, we have $U(A) > U(\neg A)$. CDT correctly diagnoses that David's abstention has zero prophylactic effect on whether his subjects will revolt. Refusing to summon Bathsheba would be pure self-deception—an exercise in superstitious "news-seeking."

---

## 3. Operationalizing Counterfactuals: Lewisian Imaging vs. Judea Pearl's do-Calculus

A recurring critique noted in Shaffer (2009) is that CDT's abstract counterfactual operator $A \mathbin{\Box\to} O$ remains algebraically underspecified without a concrete recipe for computing counterfactual credences. Two primary operational interpretations address this challenge.

### 3.1 Lewisian Imaging

David Lewis (1981) proposed the method of **imaging** on possible worlds. Let $W$ be a set of maximally specific possible worlds. For any world $w \in W$ and act $A$, let $w_A$ denote the "closest" or minimally different world to $w$ where $A$ is true. 

The image of a probability distribution $P$ under $A$, denoted $P_A$, is formed by shifting the probability mass of every world $w$ entirely onto its closest $A$-counterpart $w_A$:

$$P_A(w') = \sum_{\{w \in W \mid w_A = w'\}} P(w)$$

Then, the counterfactual probability is defined directly as:
$$P(A \mathbin{\Box\to} O) = P_A(O) = \sum_{w' \in O} P_A(w')$$

```
Prior Distribution P:
   w1 [¬A, O1] (mass 0.4) --------> moves to w1_A [A, O1]
   w2 [¬A, O2] (mass 0.6) --------> moves to w2_A [A, O2]
Resulting Imaged Distribution P_A concentrated entirely on A-worlds.
```

While elegant, Lewisian imaging faces significant conceptual hurdles. As Shaffer emphasizes, identifying the unique "closest" world requires specifying an absolute metric of similarity across worlds. Furthermore, an agent may be uncertain about which world is the closest, necessitating higher-order conditionals that risk infinite regress or severe computational intractability.

### 3.2 A Modern Proposal: Pearlian Structural Causal Models and the Interventional Operator

*(Note: While the reference article focuses on counterfactual logics and Lewisian imaging, we can provide a rigorous, operational foundation for CDT by interpreting it through Judea Pearl’s modern causal calculus.)*

We can formalize a decision problem as a **Structural Causal Model (SCM)** $\mathcal{M} = \langle U_E, V, F, P(U_E)\rangle$, where:
- $U_E$ is a set of exogenous background variables distributed according to $P(U_E)$.
- $V$ is a set of endogenous variables, containing an action variable $X \in \mathcal{A}$ and an outcome/utility variable $Y$.
- $F = \{f_i\}$ is a set of deterministic structural equations $v_i = f_i(\mathrm{pa}_i, u_i)$ mapping parents and exogenous factors to their effects.

In Pearl's framework, taking an action $A$ is modeled not by standard probabilistic conditioning $P(Y \mid X = A)$, but by an **intervention** denoted by the $\mathrm{do}$-operator: $\mathrm{do}(X = A)$. 

The operation $\mathrm{do}(X = A)$ replaces the structural equation for $X$ with the constant assignment $X = A$, effectively severing all incoming directed edges to $X$ in the causal DAG while preserving all other mechanisms intact:

```
  Observational Model (EDT):            Interventional Model (CDT):
         U (Confounder)                         U (Confounder)
         /            \                                \
        v              v                                v
     Action X ------> Outcome Y              Action X ------> Outcome Y
                                           [do(X = A)]
```

Under this operationalization, the causal expected utility is precisely the expectation under the interventional distribution:

$$U_{\mathrm{CDT}}(A) = \mathbb{E}\bigl[u(Y) \mid \mathrm{do}(X = A)\bigr] = \sum_y u(y) \, P(Y = y \mid \mathrm{do}(X = A))$$

By the truncated factorization formula (or g-formula), if $Z$ is a sufficient set of confounders satisfying the back-door criterion relative to $(X, Y)$, the interventional distribution is computed via standard probabilities as:

$$P(Y = y \mid \mathrm{do}(X = A)) = \sum_z P(Y = y \mid X = A, Z = z) \, P(Z = z)$$

Notice how the term $P(Z = z)$ is unconditional on $X = A$. This yields an exact, computable realization of Lewis’s dependency partition $\mathcal{K}$, cleanly demonstrating why CDT holds background causes fixed.

---

## 4. The Pathologies of CDT: Instability and Egan's Counterexamples

Despite its compelling resolution of Newcomb-style common-cause dilemmas, CDT encounters severe difficulties in problems featuring **endogenous feedback**—scenarios where an act reveals evidence about causal states that depend on the agent's ultimate inclination.

Andy Egan (2007) exposed a deep structural pathology in CDT: in certain decision landscapes, CDT cannot stabilize on any rational choice because its evaluation algorithm requires holding initial beliefs about causal states fixed.

### 4.1 The Psychopath Button

Consider Egan's **Psychopath Button**:
- Paul can either press a button ($A$) to eliminate all psychopaths from the world, or do nothing ($\neg A$).
- Living in a psychopath-free world is valued at $+100$ utility.
- Dying has a utility of $-10,000$.
- Surviving in the status quo has a utility of $0$.
- Crucially, Paul knows that **only psychopaths have the psychological constitution required to press the button**.
- Let $S$ denote the state that Paul is a psychopath, and $\neg S$ that he is normal.

```
                  [ Paul's Underlying Type: S or ¬S ]
                             /          \
                            v            v
                 [ Inclination to Press ]  [ Susceptibility to Button ]
                            |                        |
                            v                        v
                   [ Action: Press (A) ] ---> [ Dies if S ]
```

Paul initially assigns a small credence to being a psychopath: $P(S) = 0.01$, hence $P(\neg S) = 0.99$.

#### CDT’s Step-1 Evaluation:
Using the partition $\mathcal{K} = \{S, \neg S\}$, Paul evaluates the causal expected utility of pressing:
- If he is normal ($\neg S$), pressing the button eliminates psychopaths and leaves him alive: $u(O(A, \neg S)) = +100$.
- If he is a psychopath ($S$), pressing the button kills him: $u(O(A, S)) = -10,000$.

Holding his initial credences fixed, CDT computes:
$$U(A) = P(\neg S)(+100) + P(S)(-10{,}000) = (0.99)(100) + (0.01)(-10{,}000) = 99 - 100 = -1$$
$$U(\neg A) = 0$$

At $P(S) = 0.01$, CDT counsels Paul to abstain: $U(\neg A) > U(A)$.

Now suppose Paul's prior credence in being a psychopath is lower, say $P(S) = 0.005$:
$$U(A) = (0.995)(100) + (0.005)(-10{,}000) = 99.5 - 50 = +49.5$$
$$U(\neg A) = 0$$

Because $U(A) > U(\neg A)$, **CDT commands Paul to press the button**. 

Yet the moment Paul forms the intention to press the button, that very decision provides overwhelming evidence about his personality type: $P(S \mid A) \approx 1$. He now knows that he is almost certainly a psychopath, meaning his act is virtually guaranteed to kill him. Almost everyone shares the intuition that Paul should not press the button; yet CDT endorses pressing whenever the unconditional credence $P(S)$ falls below a threshold $\tau \approx 0.0099$.

### 4.2 Death in Damascus and Dynamic Instability

The canonical illustration of dynamic instability is the ancient tale of **Death in Damascus**:
- An agent is in Damascus. He can either stay in Damascus ($D$) or flee to Aleppo ($A$).
- Death is waiting in either Damascus ($K_D$) or Aleppo ($K_A$).
- Death is a nearly infallible predictor ($q = 0.99$) of the agent's destination.
- Dying yields $u = -100$; surviving yields $u = 0$.

Suppose the agent currently leans toward Damascus ($P(D) \approx 1$). Then he must believe Death anticipated this and is waiting in Damascus ($P(K_D) \approx 0.99$, $P(K_A) \approx 0.01$).

CDT evaluates the alternatives holding these background states fixed:
$$U(D) = P(K_D)(-100) + P(K_A)(0) = (0.99)(-100) = -99$$
$$U(A) = P(K_D)(0) + P(K_A)(-100) = (0.01)(-100) = -1$$

Since $-1 > -99$, CDT mandates: **Flee to Aleppo!**

However, as soon as the agent decides to go to Aleppo, his credences update: he now believes Death anticipated this change of plans and is waiting in Aleppo ($P(K_A) \approx 0.99, P(K_D) \approx 0.01$). 

Recalculating causal expected utilities under these new beliefs yields:
$$U(D) = (0.01)(-100) = -1$$
$$U(A) = (0.99)(-100) = -99$$

Now CDT mandates: **Stay in Damascus!**

The agent enters an endless deliberative cycle. Every pure action undermines its own rationale the instant it is adopted.

| Deliberative State | Believed Location of Death | $U_{\mathrm{CDT}}(\text{Damascus})$ | $U_{\mathrm{CDT}}(\text{Aleppo})$ | CDT Directive |
| :--- | :--- | :--- | :--- | :--- |
| Contemplating Damascus | Damascus ($P(K_D) \approx 0.99$) | $-99$ | **$-1$** | Flee to Aleppo |
| Contemplating Aleppo | Aleppo ($P(K_A) \approx 0.99$) | **$-1$** | $-99$ | Return to Damascus |

---

## 5. Defense, Deliberation, and Exploitation

The vulnerability of CDT to Egan-style counterexamples has driven significant theoretical developments. Defenses generally fall into two broad categories: deliberative self-knowledge and dynamic game-theoretic modeling.

### 5.1 Joyce's Deliberational Dynamics and Ratifiability

Richard Jeffrey originally introduced the notion of **ratifiability**: an action $A$ is ratifiable if and only if it maximizes expected utility once the agent has fully updated on the premise that they will perform $A$:

$$U(A \mid A) \ge U(A' \mid A) \quad \forall A' \in \mathcal{A}$$

In Death in Damascus and the Psychopath Button, *no pure act is ratifiable*. 

Jim Joyce (2012, 2020) defends CDT by arguing that standard formulations assume an artificially static deliberative framework. Joyce contends that during deliberation, an agent acquires evidence about their own inclinations. A fully rational agent undergoes a dynamic process of reflection:

$$\vec{p}^{(t)} \longrightarrow \vec{P}^{(t)}(\mathcal{K}) \longrightarrow \vec{U}^{(t)}(\mathcal{A}) \longrightarrow \vec{p}^{(t+1)}$$

where $\vec{p}^{(t)}$ represents the agent's probability of choosing each act at deliberation step $t$.

This dynamic process naturally converges to a mixed-strategy equilibrium where no alternative offers a superior causal expected return. In Death in Damascus, the unique stable equilibrium occurs when the agent is completely indifferent between the two destinations, randomizing with equal probability $P(D) = P(A) = 0.5$. Under this mixed policy, both choices carry an identical expected utility of $-50$. Joyce argues that CDT should not be judged deficient for failing to guarantee survival when confronting an adversarial, near-omniscient predictor; rather, recognizing the impossibility of escape reflects rational appraisal of the situation.

### 5.2 Diachronic Exploitation and Dutch Books

Despite Joyce’s defense, a serious structural flaw remains: CDT agents can be systematically exploited over time. Caspar Oesterheld and Vincent Conitzer (2021), along with Jack Spencer (2020), have demonstrated that CDT's refusal to heed evidential correlations allows outside bookies to extract money from them via **diachronic Dutch books**.

Consider the **Adversarial Offer** (Oesterheld & Conitzer, 2021):
- A seller presents two boxes, Box 1 and Box 2.
- The buyer may purchase at most one box (or none) at a price of $\$1$.
- Yesterday, the seller placed $\$3$ in each box that she predicted the buyer would **not** purchase.
- Both the buyer and seller know the seller's predictions are accurate with probability $0.75$.

```
                     [ Adversarial Offer State Space ]
                     
      Predictor's Belief               Actual Contents
      ------------------               ---------------
      Buyer takes None   ---------->   Box 1: $3 | Box 2: $3
      Buyer takes Box 1  ---------->   Box 1: $0 | Box 2: $3
      Buyer takes Box 2  ---------->   Box 1: $3 | Box 2: $0
```

#### Analysis of the Buyer's Dilemma:
The dependency partition consists of four configurations of box contents:
- $K_{(3,3)}$: Both contain $\$3$ (Predictor expected "None")
- $K_{(0,3)}$: Box 1 empty, Box 2 full (Predictor expected "Box 1")
- $K_{(3,0)}$: Box 1 full, Box 2 empty (Predictor expected "Box 2")
- $K_{(0,0)}$: Impossible under the rules.

Notice that under every possible state of the world, **at least one box contains $\$3$**. Therefore, the total sum of money across the two boxes is at least $\$3$:

$$\mathrm{Contents}(\text{Box 1}) + \mathrm{Contents}(\text{Box 2}) \ge \$3 \quad \forall K$$

By linearity of expectation, regardless of the agent's prior distribution over $\mathcal{K}$:

$$\mathbb{E}[\mathrm{Contents}(\text{Box 1})] + \mathbb{E}[\mathrm{Contents}(\text{Box 2})] \ge \$3$$

Consequently, the average causal value of a box is strictly greater than its cost:

$$\frac{U_{\mathrm{CDT}}(\text{Buy 1}) + U_{\mathrm{CDT}}(\text{Buy 2})}{2} \ge \frac{\$3}{2} - \$1 = \$1.50 - \$1.00 = +\$0.50$$

Because the average exceeds zero, it is mathematically impossible for both boxes to have negative causal expected utility simultaneously. Therefore, **CDT requires the buyer to purchase a box**.

#### The Resulting Exploitation:
The seller anticipates this causal reasoning. Knowing a CDT buyer will buy a box, the seller predicts which one he will select (say, Box 1) with 75% accuracy and leaves that box empty.

The buyer's realized expected net payoff is:
$$\mathbb{E}[\text{Payoff}] = (0.25)(\$3) + (0.75)(\$0) - \$1.00 = \$0.75 - \$1.00 = -\$0.25$$

The CDT agent willingly enters a transaction with a strictly negative expected return, voluntarily transferring money to the seller. 

An evidential decision theorist, by contrast, notes immediately that:
$$V(\text{Buy 1}) = P(\text{Full} \mid \text{Buy 1})(\$3) - \$1 = (0.25)(\$3) - \$1 = -\$0.25$$
$$V(\text{Buy 2}) = P(\text{Full} \mid \text{Buy 2})(\$3) - \$1 = (0.25)(\$3) - \$1 = -\$0.25$$
$$V(\text{Buy None}) = \$0$$

EDT comfortably selects "Buy None," safely avoiding systematic losses. The CDT agent is trapped by a rigid causal atomism: unable to treat their own decision as an informative symptom of their environment, they fall victim to predictable exploitation.

---

## 6. Summary Comparison: CDT vs. EDT

The structural divergence between Causal and Evidential Decision Theory can be summarized across three foundational dimensions:

| Theoretical Dimension | Evidential Decision Theory (EDT) | Causal Decision Theory (CDT) |
| :--- | :--- | :--- |
| **Mathematical Objective** | $\max_A \sum_j P(O_j \mid A) u(O_j)$ | $\max_A \sum_j P(A \mathbin{\Box\to} O_j) u(O_j) = \sum_k P(K_k) u(O(A, K_k))$ |
| **Core Philosophical Maxim** | "Act so as to welcome the news that you have chosen the act." | "Act so as to produce the best possible physical consequences." |
| **Newcomb's Problem** | **One-box**: $A_1$ provides strong evidence that Box B contains $\$1\mathrm{M}$. | **Two-box**: Choice cannot causally affect past placement; $A_2$ strictly dominates. |
| **Common-Cause Problems** | Vulnerable to spurious news-seeking (e.g., King David needlessly abstains). | Correctly insulates action evaluation from non-causal confounding. |
| **Endogenous Predictors** | Stable; avoids self-defeating choices by incorporating diagnostic updates. | Prone to deliberative instability (Death in Damascus) and dynamic Dutch books. |

---

## 7. Conclusion

Causal Decision Theory provides an indispensable corrective to the naïve Bayesianism of early decision theory. By requiring that alternative actions be evaluated strictly through their prospective causal efficacy—formalized via Gibbard–Harper counterfactuals, Lewisian dependency hypotheses, or Pearlian interventions—CDT successfully immunizes rational agents against the superstition of managing diagnostic symptoms rather than controlling physical outcomes.

Yet this sharp separation of agency from diagnosis incurs heavy costs. By treating the agent's current act as an uncaused intervention that cannot inform beliefs about fixed background states, CDT struggles when facing predictors who possess accurate foreknowledge of the agent's decision-making process. 

Whether these challenges can be overcome through sophisticated deliberational dynamics, or whether they point toward an alternative synthesis—such as Functional Decision Theory or other non-standard decision paradigms—remains an active, fertile debate at the intersection of mathematical statistics, causal modeling, and formal philosophy.

---

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Egan, A. (2007). Some counterexamples to causal decision theory. *The Philosophical Review*, 116(1), 93–114.
- Gibbard, A., & Harper, W. L. (1981). Counterfactuals and two kinds of expected utility. In *Ifs: Conditionals, Beliefs, Decision, Chance, and Time* (pp. 153–190). Springer.
- Joyce, J. M. (2012). Regret and instability in causal decision theory. *Synthese*, 187(1), 123–145.
- Joyce, J. M. (2020). *Yet Another Refutation of Causal Decision Theory?*
- Lewis, D. (1976). Probabilities of conditionals and conditional probabilities. *The Philosophical Review*, 85(3), 297–315.
- Lewis, D. (1979). Prisoners' dilemma is a Newcomb problem. *Philosophy & Public Affairs*, 8(3), 235–240.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
- Oesterheld, C., & Conitzer, V. (2021). Extracting money from causal decision theorists. *The Philosophical Quarterly*, 71(4), pqaa086.
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.
- Shaffer, M. J. (2009). Decision theory, intelligent planning and counterfactuals. *Minds and Machines*, 19(1), 61–92.
- Spencer, J. (2020). An argument against causal decision theory. *Analysis*, 81(1), 52–61.
- Weirich, P. (2016). Causal Decision Theory. In E. N. Zalta (Ed.), *The Stanford Encyclopedia of Philosophy*.