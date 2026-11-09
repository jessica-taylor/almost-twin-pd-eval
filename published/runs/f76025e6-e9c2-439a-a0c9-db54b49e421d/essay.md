# The Mechanics and Philosophy of Causal Decision Theory

Decision theory formalizes what it means for an agent to choose rationally among alternative courses of action. For several decades, the dominant formal paradigm was **Evidential Decision Theory (EDT)**, rooted in the foundational work of Richard Jeffrey and Leonard Savage. EDT advises an agent to select the action that provides the best *news* about the state of the world—formally, the action that maximizes expected utility conditioned on the action having occurred. 

However, beginning in the late 1960s with Robert Nozick’s popularization of Newcomb’s Problem, philosophers and logicians realized that maximizing conditional expectation systematically conflates *acting as a cause* with *acting as a symptom*. In response, **Causal Decision Theory (CDT)** was developed by figures such as Allan Gibbard, William Harper, David Lewis, and Brian Skyrms. CDT insists that an agent’s choices should be guided strictly by what those actions will *causally bring about*, rather than what they merely *evince*.

This essay offers a rigorous mathematical and philosophical account of Causal Decision Theory. We will formalize its central equations, contrast its mechanics with EDT, trace how it operationalizes counterfactual dependencies, walk through canonical decision problems, examine the modern challenges confronting it, and outline how the theory can be given a concrete operational semantics.

---

## 1. Formal Foundations: From Conditional Evidence to Causal Intervention

### 1.1 The Evidential Baseline
Let $\mathcal{A} = \{A_1, A_2, \dots, A_m\}$ be a finite set of mutually exclusive and exhaustive actions available to an agent. Let $\mathcal{O} = \{O_1, O_2, \dots, O_n\}$ be a partition of possible outcomes, and let $u: \mathcal{O} \to \mathbb{R}$ represent the agent’s utility function (or desirability, denoted $D(O)$ in Gibbard and Harper's notation).

In Evidential Decision Theory, the value of choosing action $A \in \mathcal{A}$ is given by its conditional expected utility:
$$
V_{\text{EDT}}(A) = \sum_{j=1}^n P(O_j \mid A)\, u(O_j)
$$
where $P$ is the agent's subjective probability distribution over a suitable algebra of propositions. EDT evaluates an action by asking: *"Supposing I learn that I have performed $A$, what is my updated expectation of value?"*

### 1.2 The Gibbard–Harper Formulation of CDT
Gibbard and Harper (1981) observed that conditioning on $A$ incorporates spurious correlations: if $A$ and $O_j$ share a common cause, learning that $A$ occurred provides evidence that $O_j$ will occur, even if $A$ does not causally produce $O_j$.

To insulate rational deliberation from mere statistical correlation, Gibbard and Harper proposed evaluating actions using **counterfactual conditionals**. Let $A \to O_j$ represent the conditional proposition: *"If action $A$ were to be taken, outcome $O_j$ would obtain."* (In philosophical logic, this is typically written with Robert Stalnaker and David Lewis's corner operator, $A \ \square\hspace{-1.5pt}\to O_j$).

The causal expected utility $U(A)$ of an action $A$ is defined as:
$$
U_{\text{CDT}}(A) = \sum_{j=1}^n P(A \to O_j)\, u(O_j)
$$
Here, $P(A \to O_j)$ is the agent's credence in the counterfactual proposition itself, rather than the conditional probability $P(O_j \mid A)$. 

### 1.3 Lewis’s Triviality and the Divergence of EDT and CDT
A natural question arises: why can we not simply equate the probability of a counterfactual conditional with the standard conditional probability, setting $P(A \to O_j) = P(O_j \mid A)$?

David Lewis (1976) demonstrated his celebrated **Triviality Result**: there is no non-trivial conditional connective $\to$ such that for an arbitrary probability distribution $P$ (closed under conditionalization) and all propositions $A, B$ with $P(A) > 0$, the identity
$$
P(A \to B) = P(B \mid A)
$$
holds universally. If one demands this equality in general, the underlying probability measure collapses to assigning non-zero probability to at most two mutually exclusive events (at most four-valued measures).

Consequently, $P(A \to B)$ and $P(B \mid A)$ must represent distinct epistemic quantities:
- $P(B \mid A)$ reflects the agent’s belief in $B$ upon updating their credence via conditionalization after learning the news that $A$ is true.
- $P(A \to B)$ reflects the agent’s credence that the world is configured such that an intervention making $A$ true would culminate in $B$.

Gibbard and Harper demonstrated that if one assumes standard modal axioms for conditionals (specifically including the Principle of Conditional Excluded Middle: $(A \to B) \vee (A \to \neg B)$), $P(A \to B) = P(B \mid A)$ holds if and only if the choice of $A$ is **statistically independent** of the conditional itself:
$$
P(A \to B \mid A) = P(A \to B) \iff P(A \to B) = P(B \mid A)
$$
Whenever an agent's choice of action carries evidential information about what *would* happen anyway—as occurs in common-cause scenarios—this independence fails, and CDT and EDT diverge sharply.

---

## 2. Dependency Hypotheses and Lewisian Imaging

While Gibbard and Harper framed CDT in terms of counterfactuals, David Lewis (1981) and Brian Skyrms reformulated the theory using partitions of **dependency hypotheses**. This framework clarifies how CDT evaluates policies without requiring an agent to deliberate directly on primitive counterfactual propositions.

### 2.1 The Dependency Hypothesis Formulation
Let $\mathcal{K} = \{K_1, K_2, \dots, K_r\}$ be a partition of maximally specific hypotheses concerning how the world causally depends on the agent's actions. Each $K \in \mathcal{K}$ specifies, for every possible action $A \in \mathcal{A}$, exactly which outcome $O \in \mathcal{O}$ would result if $A$ were enacted. That is, under $K$, the causal conditional $A \to O$ is completely determined.

Because $\mathcal{K}$ is a mutually exclusive and exhaustive partition of states outside the causal control of the agent's current act, an agent's unconditional credence in $K$ represents their belief about the causal structure of reality prior to acting. The causal expected utility of $A$ can be rewritten as:
$$
U_{\text{CDT}}(A) = \sum_{K \in \mathcal{K}} P(K) \sum_{j=1}^n P(O_j \mid A \wedge K)\, u(O_j)
$$
Because a dependency hypothesis $K$ completely fixes the causal mapping from acts to outcomes, $P(O_j \mid A \wedge K)$ is typically deterministic ($0$ or $1$), reducing the formula to:
$$
U_{\text{CDT}}(A) = \sum_{K \in \mathcal{K}} P(K)\, u(O(A, K))
$$
where $O(A, K)$ is the unique outcome guaranteed by action $A$ in state $K$.

Notice the crucial contrast with EDT. In EDT, the expectation over states conditions on the act:
$$
V_{\text{EDT}}(A) = \sum_{K \in \mathcal{K}} P(K \mid A)\, u(O(A, K))
$$
CDT uses the **unconditional** credence $P(K)$, deliberately refusing to update credences about pre-existing causal states based on the act chosen.

### 2.2 Lewisian Imaging
To formalize the semantics of $P(A \to O)$, Lewis introduced the concept of **imaging**. 

Let $W$ be the set of possible worlds, and let $P$ be a probability measure over $W$. For any world $w \in W$ and proposition $A$, let $w_A$ denote the "closest" or "most similar" world to $w$ where $A$ is true (adopting the Stalnakerian assumption that a unique closest world exists). 

The probability distribution **imaged on $A$**, denoted $P_A$, is obtained by shifting the probability weight of each world $w$ entirely to its closest $A$-counterpart $w_A$:
$$
P_A(w') = \sum_{\{w \in W \mid w_A = w'\}} P(w)
$$
The counterfactual probability $P(A \to O)$ is then defined as the imaged probability of $O$:
$$
P(A \to O) = P_A(O) = \sum_{w \in O} P_A(w)
$$
Whereas *conditionalization* updates beliefs by zeroing out non-$A$ worlds and renormalizing over the remaining $A$-worlds ($P(w \mid A) = P(w)/P(A)$ for $w \in A$), *imaging* keeps the total probability mass intact and displaces it across modal space to satisfy $A$ with minimal causal disruption.

---

## 3. Canonical Applications and Divergences

To understand the practical execution of CDT, we consider how it evaluates classic decision problems.

### 3.1 Common Causes: King David and Bathsheba
Consider Gibbard and Harper's example drawn from political history: King David desires Bathsheba. He knows the following:
- Kings are genetically and unalterably either *charismatic* ($C$) or *uncharismatic* ($\neg C$). David does not know his type; let $P(C) = 0.5$.
- Charismatic kings have an innate regal bearing that deters rebellion; revolts against them are rare ($R = \text{revolt}$, $P(R \mid C) = 0.1$). Uncharismatic kings appear ignoble, leading to frequent revolts ($P(R \mid \neg C) = 0.8$).
- Sending for another man's wife ($A$) is an unjust act. Charismatic kings rarely act unjustly; uncharismatic kings frequently act unjustly. Thus, David's choice of $A$ is strongly correlated with being uncharismatic:
  $$
  P(\neg C \mid A) = 0.9, \quad P(C \mid A) = 0.1
  $$
- Crucially, **the unjust act does not cause the revolt**. The revolt is caused solely by the king's bearing (determined by $C$). Whether David summons Bathsheba or abstains ($\neg A$), a charismatic king faces a $0.1$ revolt chance, and an uncharismatic king faces a $0.8$ revolt chance.

Let the utilities be:
- Bathsheba summoned, no revolt: $u(A \wedge \neg R) = 20$
- Bathsheba summoned, revolt: $u(A \wedge R) = -10$
- Abstain, no revolt: $u(\neg A \wedge \neg R) = 10$
- Abstain, revolt: $u(\neg A \wedge R) = -20$

Summoning Bathsheba provides a constant marginal utility of $+10$ regardless of whether a revolt occurs.

#### EDT Calculation
Under EDT, David evaluates $A$ by conditioning his type on his choice:
$$
P(R \mid A) = P(R \mid C)P(C \mid A) + P(R \mid \neg C)P(\neg C \mid A) = (0.1)(0.1) + (0.8)(0.9) = 0.01 + 0.72 = 0.73
$$
$$
P(R \mid \neg A) = P(R \mid C)P(C \mid \neg A) + P(R \mid \neg C)P(\neg C \mid \neg A)
$$
Assuming $P(C \mid \neg A) = 0.9$ and $P(\neg C \mid \neg A) = 0.1$:
$$
P(R \mid \neg A) = (0.1)(0.9) + (0.8)(0.1) = 0.09 + 0.08 = 0.17
$$
The evidential expected utilities are:
$$
V_{\text{EDT}}(A) = (0.27)(20) + (0.73)(-10) = 5.4 - 7.3 = -1.9
$$
$$
V_{\text{EDT}}(\neg A) = (0.83)(10) + (0.17)(-20) = 8.3 - 3.4 = +4.9
$$
EDT advises David to abstain: summoning Bathsheba is terrible *news*, indicating that he is an uncharismatic king doomed to face a revolt.

#### CDT Calculation
CDT evaluates the counterfactual probabilities holding David's causal type fixed:
$$
P(A \to R) = P(C) P(A \to R \mid C) + P(\neg C) P(A \to R \mid \neg C)
$$
Because $A$ does not cause revolts, $P(A \to R \mid C) = P(R \mid C) = 0.1$, and $P(A \to R \mid \neg C) = P(R \mid \neg C) = 0.8$. David's prior is $P(C) = 0.5$. Thus:
$$
P(A \to R) = (0.5)(0.1) + (0.5)(0.8) = 0.45
$$
By identical reasoning:
$$
P(\neg A \to R) = (0.5)(0.1) + (0.5)(0.8) = 0.45
$$
The causal expected utilities are:
$$
U_{\text{CDT}}(A) = (0.55)(20) + (0.45)(-10) = 11.0 - 4.5 = +6.5
$$
$$
U_{\text{CDT}}(\neg A) = (0.55)(10) + (0.45)(-20) = 5.5 - 9.0 = -3.5
$$
CDT recommends summoning Bathsheba ($U_{\text{CDT}}(A) > U_{\text{CDT}}(\neg A)$). David's action cannot alter his genome or childhood history; refraining from summoning Bathsheba is mere "news-management." Rationality demands pursuing the real $+10$ causal advantage.

---

### 3.2 Newcomb’s Paradox
In Newcomb's Problem, an agent faces two boxes:
- **Box A** (transparent): contains $\$1,000$.
- **Box B** (opaque): contains either $\$1,000,000$ or $\$0$.

The agent may choose **one-box** ($B_1$, taking only Box B) or **two-box** ($B_2$, taking both Box A and Box B). Yesterday, an exceptionally reliable predictor (say, accuracy $q = 0.99$) predicted the agent’s choice:
- If the predictor anticipated $B_1$, Box B was loaded with $\$1,000,000$.
- If the predictor anticipated $B_2$, Box B was left empty ($\$0$).

The contents of Box B are physically determined and sealed prior to the decision.

#### Formal Matrix
Let $S_1$ be the state where Box B contains $\$1,000,000$, and $S_0$ where Box B contains $\$0$. The payoffs (assuming linear utility in dollars) are:

| Action | State $S_1$ (Loaded) | State $S_0$ (Empty) |
| :--- | :--- | :--- |
| **$B_1$ (One-Box)** | $\$1,000,000$ | $\$0$ |
| **$B_2$ (Two-Box)** | $\$1,001,000$ | $\$1,000$ |

#### The EDT Recommendation
Because the predictor is $99\%$ accurate:
$$
P(S_1 \mid B_1) = 0.99, \quad P(S_0 \mid B_1) = 0.01
$$
$$
P(S_1 \mid B_2) = 0.01, \quad P(S_0 \mid B_2) = 0.99
$$
Evaluating conditional expected utilities:
$$
V_{\text{EDT}}(B_1) = 0.99(1,000,000) + 0.01(0) = \$990,000
$$
$$
V_{\text{EDT}}(B_2) = 0.01(1,001,000) + 0.99(1,000) = 10,010 + 990 = \$11,000
$$
EDT unambiguously dictates taking only Box B ($B_1$).

#### The CDT Recommendation
In CDT, the dependency hypotheses are simply $\mathcal{K} = \{S_1, S_0\}$. The physical content of Box B was fixed in the past; an agent's current reach toward the boxes carries no backward causal efficacy. 
Therefore, for any fixed state $S \in \{S_1, S_0\}$:
$$
P(B_2 \to S) = P(B_1 \to S) = P(S)
$$
Let $p = P(S_1)$ be the agent's prior belief that the box is loaded. The causal expected utilities are:
$$
U_{\text{CDT}}(B_1) = p(1,000,000) + (1-p)(0) = 1,000,000\,p
$$
$$
U_{\text{CDT}}(B_2) = p(1,001,000) + (1-p)(1,000) = 1,000,000\,p + 1,000
$$
For every probability distribution $p \in [0, 1]$:
$$
U_{\text{CDT}}(B_2) - U_{\text{CDT}}(B_1) = 1,000 > 0
$$
Action $B_2$ strictly dominates $B_1$ across all causal dependency hypotheses. Taking both boxes guarantees $\$1,000$ more than taking Box B alone, regardless of whether the predictor turned out to be right or wrong. Thus, CDT recommends **two-boxing**.

---

## 4. Modern Pathologies: Instability and Adversarial Exploitation

Despite its intuitive appeal in common-cause cases, CDT encounters severe challenges when an agent's beliefs about the world interact dynamically with their own deliberative process.

### 4.1 Death in Damascus and Deliberational Instability
In the classic tale of *Death in Damascus*, an agent currently in Damascus must decide whether to stay in Damascus ($D$) or flee to Aleppo ($A$). Death has predicted where the agent will be tomorrow morning and is waiting at that location. Escaping Death yields utility $0$; being captured by Death yields utility $-100$. Suppose Death has prediction accuracy $q = 0.99$.

Crucially, Death is already located either in Damascus or Aleppo. The agent's physical motion today does not retroactively move Death. 

Suppose the agent tentatively decides to stay in Damascus ($D$). If the agent believes they will do $D$, their credence that Death is in Damascus climbs to $0.99$. Under this dependency hypothesis:
- $U_{\text{CDT}}(D) \approx 0.99(-100) + 0.01(0) = -99$
- $U_{\text{CDT}}(A) \approx 0.99(0) + 0.01(-100) = -1$

Seeing that $U_{\text{CDT}}(A) > U_{\text{CDT}}(D)$, the agent switches their intention to Aleppo ($A$). But as soon as the agent resolves to go to Aleppo, they must rationally believe that Death anticipated this move and is waiting in Aleppo! Under this updated belief:
- $U_{\text{CDT}}(A) \approx -99$
- $U_{\text{CDT}}(D) \approx -1$

The agent now switches back to Damascus. CDT enters an endless, unstable cycle. 

#### Egan's Psychopath Button
Andy Egan (2007) formalized this instability through the **Psychopath Button**. 
- Paul can choose to press a button ($B$) that eliminates all psychopaths from Earth, or refrain ($\neg B$).
- Paul strongly desires a world free of psychopaths ($u = +100$), but desires his own survival above all; if he dies, $u = -1,000$. Living with psychopaths yields $u = 0$.
- Paul is completely confident that *only a psychopath would press the button*.
- Paul does not know whether he himself is a psychopath; his initial prior is $P(\text{Psy}) = 0.01$.

Because pressing the button does not *make* Paul a psychopath (psychopathy is an entrenched neurological condition), CDT holds the hypothesis fixed:
$$
U_{\text{CDT}}(B) = P(\text{Psy})(-1000) + P(\neg \text{Psy})(100) = 0.01(-1000) + 0.99(100) = -10 + 99 = +89
$$
$$
U_{\text{CDT}}(\neg B) = 0
$$
CDT directs Paul to press the button. Yet, Paul knows that if he forms the intention to press it, he will be virtually certain he is a psychopath, meaning he is intentionally triggering his own death! As Egan argues, CDT appears to mandate an action that the agent knows, as soon as they decide upon it, will produce catastrophe.

### 4.2 Adversarial Offers and Dutch Books
Recent work by Spencer (2020) and Oesterheld & Conitzer (2021) demonstrates that CDT agents can be lured into diachronic Dutch books—systematic exploitation resulting in guaranteed losses.

Consider the **Adversarial Offer**:
- Two boxes ($1$ and $2$) are presented. An agent may purchase at most one box for $\$1$.
- Yesterday, a seller, predicting the agent's choice with probability $0.75$, placed $\$3$ into whichever box the seller predicted the buyer would **not** acquire. If the seller predicted the agent buys Box 1, the $\$3$ went into Box 2; if Box 2, into Box 1; if neither, both boxes were loaded.

Let us evaluate the buyer's reasoning under CDT:
At the time of purchase, the money is already placed. There is $\$3$ in at least one box; hence the total money in the boxes is at least $\$3$. By symmetry, the average causal contents of a box is at least $\$1.50$. Since the purchase price is only $\$1.00$, CDT determines that buying a box has an expected causal return of $\$1.50 - \$1.00 = +\$0.50$. Hence, CDT forbids choosing "neither box" and strictly requires buying a box. 

Yet, because the seller is $75\%$ accurate, whichever box the CDT agent purchases contains $\$3$ with only a $25\%$ probability:
$$
\mathbb{E}[\text{Net Profit}] = 0.25(\$3) - \$1.00 = \$0.75 - \$1.00 = -\$0.25
$$
The CDT agent willingly engages in an exchange that systematically extracts money, violating the fundamental principle that rational decision rules should avoid guaranteed or predictable losses against predictable environments.

---

## 5. Bridging the Gaps: An Operational Synthesis

The standard literature notes two recurring gaps in CDT:
1. **Algorithmic Vagueness:** How should an agent evaluate counterfactual probabilities in arbitrary, unfamiliar environments without relying on metaphysical notions of "closest possible worlds"?
2. **Deliberational Instability:** How can CDT resolve the cycling seen in Death in Damascus and the Psychopath Button?

Below, we present concrete operational proposals to resolve both questions.

```
       Prior Knowledge & Observational Data
                         │
                         ▼
       ┌───────────────────────────────────┐
       │     Structural Causal Model       │
       │     M = <U, V, F, P(u)>           │
       └───────────────────────────────────┘
                         │
                         ▼
        Pearl's do-operator / Interventions
                         │
                         ▼
       ┌───────────────────────────────────┐
       │   Causal Utility Computation      │
       │   U_CDT(A) = Σ P(O | do(A)) u(O)  │
       └───────────────────────────────────┘
                         │
                         ▼
       ┌───────────────────────────────────┐
       │     Ratification Dynamics         │
       │    Mixed Equilibrium / Fixed Pt   │
       └───────────────────────────────────┘
                         │
                         ▼
           Stable, Rational Decision
```

### 5.1 Operationalizing Counterfactuals: Structural Causal Models
The critique that Lewis's imaging leads to infinite regress or subjective ambiguity can be addressed by anchoring CDT in Judea Pearl's framework of **Structural Causal Models (SCMs)**.

*(Proposal)*: We operationalize Gibbard and Harper's counterfactual probability $P(A \to O)$ as an **interventional distribution** via the Pearlian $\text{do}$-calculus:
$$
P(A \to O) \equiv P(O \mid \text{do}(A))
$$
Formally, define a causal model as a tuple $\mathcal{M} = \langle \mathbf{U}, \mathbf{V}, \mathbf{F}, P(\mathbf{u}) \rangle$, where:
- $\mathbf{U}$ is a set of exogenous, unobserved background variables distributed according to prior $P(\mathbf{u})$.
- $\mathbf{V}$ is a set of endogenous observable variables (including the agent's act $A$ and outcome $O$).
- $\mathbf{F} = \{f_V \mid V \in \mathbf{V}\}$ is a set of deterministic structural equations such that each $v \in \mathbf{V}$ is assigned by $v = f_V(\mathbf{pa}_V, \mathbf{u}_V)$, where $\mathbf{pa}_V \subseteq \mathbf{V} \setminus \{V\}$ are the direct parents of $V$.

To compute $P(O \mid \text{do}(A = a))$:
1. **Graph Surgery:** Sever all incoming causal edges to variable $A$ in the model's directed acyclic graph (DAG), replacing the structural equation $f_A$ with the constant assignment $A = a$. This formalizes the idea that the action is chosen freely as an intervention, preventing any upstream evidence from flowing back into common ancestors.
2. **Forward Propagation:** Evaluate the probability of $O$ using the truncated structural equations:
$$
P(O = o \mid \text{do}(A = a)) = \sum_{\{\mathbf{u} \mid O^{\mathcal{M}[A=a]}(\mathbf{u}) = o\}} P(\mathbf{u})
$$
where $O^{\mathcal{M}[A=a]}(\mathbf{u})$ is the solution for $O$ under the modified system of equations given exogenous shocks $\mathbf{u}$.

#### Applying the SCM to Newcomb's Problem
The model has three variables:
- $U \in \{1, 0\}$: The agent's cognitive disposition or algorithm (exogenous, $P(U=1) = 0.5$).
- $M \in \{10^6, 0\}$: Box B contents, determined by the predictor: $M = f_M(U)$. Let $f_M(u) = 10^6$ if $u=1$, else $0$.
- $A \in \{B_1, B_2\}$: The agent's act, which naturally correlates with disposition: $A = f_A(U)$.
- Payoff $Y = f_Y(A, M)$, where $Y = M + 1000 \cdot \mathbb{I}(A = B_2)$.

When evaluating EDT, we condition on $A$:
$$
P(M = 10^6 \mid A = B_1) = P(M = 10^6 \mid U = 1) = 1.0 \implies \mathbb{E}[Y \mid A=B_1] = 10^6
$$
When evaluating CDT via Pearl's intervention, we replace $A = f_A(U)$ with $\text{do}(A = B_2)$. The link between $U$ and $A$ is severed:
$$
P(M = 10^6 \mid \text{do}(A = B_2)) = \sum_u P(M = 10^6 \mid U = u) P(U = u) = P(U = 1) = 0.5
$$
The value of $M$ is unperturbed by the surgical operation on $A$. CDT calculates:
$$
\mathbb{E}[Y \mid \text{do}(A = B_2)] = 0.5(10^6) + 1000 = 501,000
$$
$$
\mathbb{E}[Y \mid \text{do}(A = B_1)] = 0.5(10^6) = 500,000
$$
CDT picks $B_2$ unambiguously, based on an explicit, finite algorithmic procedure over the causal DAG.

---

### 5.2 Resolving Deliberational Instability: Ratificationism
To resolve cyclic dilemmas like Death in Damascus, Richard Jeffrey and later James M. Joyce proposed introducing **ratification dynamics**.

An action $A$ is **ratifiable** if and only if $A$ maximizes causal expected utility *on the assumption that one has decided to perform $A$*:
$$
A \text{ is ratifiable} \iff U(A \mid A) \ge U(A' \mid A) \quad \forall A' \in \mathcal{A}
$$
where $U(A' \mid A)$ denotes the causal expected utility of performing $A'$ evaluated with respect to credences updated on the proposition that the agent intends to do $A$:
$$
U(A' \mid A) = \sum_{K \in \mathcal{K}} P(K \mid A)\, u(O(A', K))
$$
In Death in Damascus:
- $U(D \mid D) = -99$, but $U(A \mid D) = -1$. Staying in Damascus is **unratifiable**.
- $U(A \mid A) = -99$, but $U(D \mid A) = -1$. Fleeing to Aleppo is **unratifiable**.

Neither pure action is ratifiable. 

*(Proposal)*: The natural mathematical resolution is to extend the decision space to **mixed strategies (probabilistic policies)**. Let $p = P(D)$ be the probability with which the agent intends to choose Damascus. 

As the agent deliberates, their intention $p$ updates their belief about Death's location. Death's location probabilities become $P(\text{Death in } D) = p$ and $P(\text{Death in } A) = 1-p$. The causal expected utility of the pure actions, evaluated relative to the deliberational state $p$, is:
$$
U(D; p) = p(-100) + (1-p)(0) = -100p
$$
$$
U(A; p) = p(0) + (1-p)(-100) = -100(1-p)
$$
A policy $p^*$ is **in deliberational equilibrium** (a ratifiable mixed state) if and only if the agent has no incentive to perturb $p^*$. Equating the two expected utilities:
$$
-100p^* = -100(1-p^*) \implies p^* = 0.5
$$
At $p^* = 0.5$, Death is equally likely to be in either city ($P = 0.5$). Both actions yield identical causal expected utilities:
$$
U(D; 0.5) = U(A; 0.5) = -50
$$
By flipping an unbiased coin, the agent achieves an expected outcome of $-50$, avoiding the deterministic death ($-99$) predicted by unratified single-action cycling. Ratificationism transforms CDT from an unstable rule into a well-defined fixed-point operator over the simplex of mixed strategies.

---

## 6. Summary Comparison: EDT vs. CDT

The following table summarizes the mathematical and structural distinctions between Evidential and Causal Decision Theory:

| Dimension | Evidential Decision Theory (EDT) | Causal Decision Theory (CDT) |
| :--- | :--- | :--- |
| **Guiding Intuition** | Choose the action that provides the best *news*. | Choose the action that produces the best *effects*. |
| **Core Formalism** | $V(A) = \sum_j P(O_j \mid A) u(O_j)$ | $U(A) = \sum_j P(A \to O_j) u(O_j)$ |
| **State Weighting** | Action-conditioned: $P(K \mid A)$ | Unconditional dependency: $P(K)$ |
| **Modal Operator** | Standard conditionalization | Interventional / Imaged ($P_A$ or $\text{do}(A)$) |
| **Newcomb’s Paradox** | **One-box**: $B_1$ ($+\$1,000,000$ news) | **Two-box**: $B_2$ (Dominance: $+\$1,000$ bonus) |
| **King David & Bathsheba** | **Abstain**: Avoids bad omen of revolt | **Summon**: Realizes causal benefit ($+10$) |
| **Primary Failure Mode** | Conflates correlation with causation | Vulnerable to deliberational instability / Dutch books |

---

## 7. Conclusion

Causal Decision Theory emerged to correct a fundamental flaw in classical expected utility maximization: the confusion of symptomatic news with physical consequence. By formalizing expected utility through counterfactual conditionals $P(A \to O)$, Lewisian imaging, or structural causal models $P(O \mid \text{do}(A))$, CDT provides an intuitive defense of dominance reasoning in common-cause settings like Newcomb’s Paradox and King David's dilemma.

Yet, CDT's insistence on holding pre-existing dependency hypotheses fixed leaves it vulnerable to deliberational instability (as in the Psychopath Button and Death in Damascus) and dynamic exploitation (as in Adversarial Offers). Resolving these tensions requires supplementing pure CDT with algorithmic mechanics—such as causal graphical surgeries for computing counterfactual probabilities and mixed-strategy ratification dynamics for stabilizing beliefs. Formulated this way, CDT remains one of our sharpest frameworks for exploring the boundary between rational choice, causal inference, and belief update.

---

## References

1. Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
2. Egan, A. (2007). Some counterexamples to causal decision theory. *The Philosophical Review*, 116(1), 93–114.
3. Gibbard, A., & Harper, W. L. (1981). Counterfactuals and two kinds of expected utility. In *Ifs: Conditionals, Beliefs, Decision, Chance, and Time* (pp. 153–190). Springer.
4. Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
5. Joyce, J. M. (2012). Regret and instability in causal decision theory. *Synthese*, 187(1), 123–145.
6. Lewis, D. (1976). Probabilities of conditionals and conditional probabilities. *The Philosophical Review*, 85(3), 297–315.
7. Lewis, D. (1979). Prisoners' dilemma is a Newcomb problem. *Philosophy & Public Affairs*, 8(3), 235–240.
8. Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
9. Oesterheld, C., & Conitzer, V. (2021). Extracting money from causal decision theorists. *The Philosophical Quarterly*, 71(4).
10. Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.
11. Spencer, J. (2020). An argument against causal decision theory. *Analysis*, 81(1), 52–61.
12. Weirich, P. (2016). Causal Decision Theory. In E. N. Zalta (Ed.), *The Stanford Encyclopedia of Philosophy*.