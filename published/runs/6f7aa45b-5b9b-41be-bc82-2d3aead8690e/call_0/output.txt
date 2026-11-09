# The Mechanics of Agency: A Mathematical Exegesis of Causal Decision Theory

## 1. Introduction: The Need for Causal Expected Utility

Classical Bayesian decision theory, in the tradition of Frank Ramsey, Leonard Savage, and Richard Jeffrey, formalizes rational choice as the maximization of expected utility. In Jeffrey’s evidential framework—termed **Evidential Decision Theory (EDT)**—the desirability of an act $A$ is computed conditional on the proposition that $A$ is realized:

$$V_{\text{EDT}}(A) = \sum_{j} P(O_j \mid A) \, u(O_j),$$

where $\{O_j\}$ is a partition of mutually exclusive and exhaustive outcomes, $P(\cdot)$ is the agent's subjective probability distribution, and $u(\cdot)$ is a utility function defined on outcomes.

EDT prescribes choosing the act that provides the best *epistemic news*: if learning that one performed $A$ increases the posterior probability of favorable outcomes, $A$ receives a high valuation. However, probability theory treats conditioning as purely symmetrical correlation. It does not distinguish whether $P(O \mid A) > P(O)$ holds because $A$ *causes* $O$, or because $A$ and $O$ share a common cause.

When correlation comes apart from causation, EDT can recommend actions that do not causally promote the agent's interests. **Causal Decision Theory (CDT)** was formulated precisely to correct this defect. CDT posits that rational action must be evaluated not by what taking the action would *indicate*, but by what taking the action would *bring about*.

---

## 2. Formal Frameworks of Causal Decision Theory

Multiple mathematical formalisms have been developed to articulate CDT. Three prominent formulations are:
1. Counterfactual conditionals (Gibbard & Harper),
2. Causal dependency hypotheses / Lewisian imaging (Lewis, Skyrms),
3. Structural causal models and intervention calculi (Pearl).

### 2.1. The Counterfactual Formulation (Gibbard & Harper)

Allan Gibbard and William Harper (1981) formulated CDT using the logic of counterfactual conditionals, commonly symbolized by the corner conditional operator $A \mathbin{\Box\to} O$ (or $A \to O$ in the source text), denoting the subjunctive conditional: *"If the agent were to do $A$, outcome $O$ would obtain."*

Let $\mathcal{A} = \{A_1, A_2, \dots, A_m\}$ be a finite set of mutually exclusive and exhaustive actions available to the agent, and let $\mathcal{O} = \{O_1, O_2, \dots, O_n\}$ be a finite partition of possible outcomes. The causal expected utility $U(A)$ of an action $A \in \mathcal{A}$ is:

$$U(A) = \sum_{j=1}^n P(A \mathbin{\Box\to} O_j) \, u(O_j),$$

where $P(A \mathbin{\Box\to} O_j)$ is the subjective probability assigned to the counterfactual proposition that $O_j$ would occur if $A$ were chosen, and $u(O_j)$ represents the utility (desirability) of $O_j$.

#### Lewis's Triviality and Conditional Probabilities
A foundational question is whether the probability of a counterfactual conditional can simply be identified with the conditional probability:
$$P(A \mathbin{\Box\to} O) \stackrel{?}{=} P(O \mid A).$$

David Lewis (1976) proved that this equality cannot hold in general. Specifically, if a non-trivial probability measure closed under conditioning satisfies $P(A \to B) = P(B \mid A)$ for all propositions $A, B$ where $P(A) > 0$, the probability function collapses to assigning positive probability to at most two mutually incompatible propositions (Lewis's Triviality Result).

Gibbard and Harper demonstrated that $P(A \mathbin{\Box\to} O) = P(O \mid A)$ holds if and only if the act $A$ is statistically independent of the conditional $A \mathbin{\Box\to} O$:
$$P(A \mathbin{\Box\to} O \mid A) = P(A \mathbin{\Box\to} O).$$

In standard decision problems without confounding, this independence holds. However, in scenarios with common causes or predictors, the independence breaks down, driving a wedge between EDT and CDT.

### 2.2. Dependency Hypotheses and Lewisian Imaging

To make counterfactual probabilities operational, David Lewis (1981) and Brian Skyrms formalized CDT using **causal dependency hypotheses**.

Let $\mathcal{K} = \{K_1, K_2, \dots, K_r\}$ be a partition of propositions specifying how outcomes depend causally upon the agent's choices. Each $K \in \mathcal{K}$ represents a maximally specific specification of factors outside the agent's causal control. Under a given hypothesis $K$, the choice of act $A$ deterministically (or with fixed objective chance) yields a specific outcome $O(A, K)$. 

Under this view, the causal expected utility is:

$$U(A) = \sum_{k=1}^r P(K_k) \sum_{j=1}^n P(O_j \mid A \land K_k) \, u(O_j).$$

Because $K_k$ fixes all causal factors beyond the agent's control, $P(O_j \mid A \land K_k)$ represents the genuine causal efficacy of $A$ under state $K_k$. The crucial structural feature of CDT is that the weight assigned to $K_k$ is the **unconditional** prior credence $P(K_k)$, *not* the conditional credence $P(K_k \mid A)$.

#### The Imaging Algorithm
Lewis provided a semantic basis for counterfactual probability via **imaging**. Let $W$ be a set of possible worlds, and let $w \in W$ possess a prior probability measure $P(w)$. Define a selection function $f: W \times \mathcal{A} \to W$, where $f(w, A) = w_A$ is the "closest" or "most similar" possible world to $w$ in which proposition $A$ is true. 

The probability measure *imaged* on $A$, denoted $P_A$, shifts each world's probability mass entirely to its image $w_A$:

$$P_A(w') = \sum_{\{w \in W : f(w, A) = w'\}} P(w).$$

The counterfactual probability is then defined as:
$$P(A \mathbin{\Box\to} O) = P_A(O) = \sum_{w' \in O} P_A(w').$$

Unlike Bayesian conditioning, which zeroes out the mass of all $\neg A$-worlds and renormalizes the remaining $A$-worlds (epistemic belief revision), imaging keeps the probability mass intact and transports it along causal lines to the nearest counterfactual alternatives (causal intervention).

---

## 3. An Operational Extension: Structural Causal Models

The source article notes an important criticism: CDT does not uniquely specify a computational algorithm for calculating counterfactual probabilities, and Lewisian imaging suffers from ambiguity regarding the metric of "similarity" across possible worlds. 

Here we develop an operational formulation that bridges classical CDT with modern structural causal modeling (Pearl, 2000). While this structural interpretation is an addition to the classical formulations reviewed in the source, it provides a rigorous, computable calculus for arbitrary decision graphs.

### 3.1. Definition: Structural Causal Model (SCM)
A Structural Causal Model is a quadruple $\mathcal{M} = \langle \mathcal{U}, \mathcal{V}, \mathcal{F}, P(\mathcal{U}) \rangle$, where:
- $\mathcal{U} = \{U_1, \dots, U_p\}$ is a set of exogenous (unobserved background) variables governed by probability distribution $P(\mathcal{U})$.
- $\mathcal{V} = \{V_1, \dots, V_q\}$ is a set of endogenous variables, including the decision variable $A$ and the utility variable $U$.
- $\mathcal{F} = \{f_1, \dots, f_q\}$ is a collection of deterministic functions such that each $V_i \in \mathcal{V}$ is determined by $v_i = f_i(\mathbf{pa}_i, \mathbf{u}_i)$, where $\mathbf{pa}_i \subseteq \mathcal{V} \setminus \{V_i\}$ are the endogenous parents of $V_i$, and $\mathbf{u}_i \subseteq \mathcal{U}$.

### 3.2. Causal Intervention: The $\text{do}$-operator
An action setting variable $A$ to value $a$ corresponds to the intervention $\text{do}(A = a)$. Mathematically, the intervention replaces the structural equation $f_A(\mathbf{pa}_A, \mathbf{u}_A)$ with the constant assignment $A \leftarrow a$, severing all incoming causal arrows into $A$ in the associated directed acyclic graph (DAG).

Under the SCM framework, the probability distribution of an outcome $O$ under counterfactual intervention $A = a$ is:

$$P(a \mathbin{\Box\to} O) \equiv P(O \mid \text{do}(A = a)).$$

The CDT objective function becomes:

$$U_{\text{CDT}}(a) = \mathbb{E}[u \mid \text{do}(A = a)] = \sum_{o} P(O = o \mid \text{do}(A = a)) \, u(o).$$

By contrast, EDT computes:
$$V_{\text{EDT}}(a) = \mathbb{E}[u \mid A = a] = \sum_{o} P(O = o \mid A = a) \, u(o).$$

If a set of variables $\mathbf{Z}$ satisfies the **back-door criterion** relative to $(A, O)$ (i.e., no node in $\mathbf{Z}$ is a descendant of $A$, and $\mathbf{Z}$ blocks every path between $A$ and $O$ that contains an arrow into $A$), the counterfactual distribution is identified by the back-door adjustment formula:

$$P(O \mid \text{do}(A = a)) = \sum_{\mathbf{z}} P(O \mid A = a, \mathbf{Z} = \mathbf{z}) P(\mathbf{Z} = \mathbf{z}).$$

This provides a computable algorithm for CDT: to evaluate an act, identify the confounding causal ancestors $\mathbf{Z}$, compute the conditional likelihoods within each stratum $\mathbf{z}$, and aggregate them weighted by the *marginal* distribution $P(\mathbf{Z})$, precisely matching Lewis's requirement of holding dependency hypotheses fixed.

---

## 4. Benchmark Decisions: CDT vs. EDT

We now apply this formal apparatus to canonical decision problems.

### 4.1. Confounding Without Prediction: The King David Problem
In Gibbard and Harper's historical thought experiment:
- David desires Bathsheba ($u(\text{Bathsheba}) = b > 0$).
- David fears a successful revolt ($u(\text{Revolt}) = -r < 0$).
- Let $C \in \{1, 0\}$ denote whether David has a charismatic personality ($P(C=1) = p$).
- Let $A \in \{1, 0\}$ denote summoning Bathsheba ($A=1$) or abstaining ($A=0$).
- Let $R \in \{1, 0\}$ denote whether a revolt occurs.

The causal assumptions are:
1. Personality $C$ is determined in childhood and cannot be altered by $A$: $C \to A$.
2. Charismatic kings act justly ($P(A=1 \mid C=1) = \epsilon_1 \approx 0$), whereas uncharismatic kings act unjustly ($P(A=1 \mid C=0) = 1 - \epsilon_0 \approx 1$).
3. Revolts depend causally on personality (bearing), *not* on the act: $P(R=1 \mid C=1, A) = \rho_C$, $P(R=1 \mid C=0, A) = \rho_U$, with $\rho_U \gg \rho_C$. Formally, $R \perp\!\!\perp A \mid C$.

```
     Personality (C)
       /         \
      v           v
 Action (A)     Revolt (R)
```

#### EDT Evaluation:
EDT calculates:
$$V_{\text{EDT}}(A=1) = b - r \, P(R=1 \mid A=1),$$
$$V_{\text{EDT}}(A=0) = - r \, P(R=1 \mid A=0).$$

By Bayes' rule:
$$P(C=0 \mid A=1) = \frac{P(A=1 \mid C=0)P(C=0)}{P(A=1)} \approx 1.$$
Because summoning Bathsheba is strong evidence that David is uncharismatic, $P(R=1 \mid A=1) \approx \rho_U$. Abstaining is strong evidence of charisma, so $P(R=1 \mid A=0) \approx \rho_C$. For sufficiently large $r$, $V_{\text{EDT}}(A=0) > V_{\text{EDT}}(A=1)$. EDT prescribes abstention: David should deny himself the woman to maintain the comforting belief that he is charismatic.

#### CDT Evaluation:
In CDT, the dependency hypotheses are $K_1: C=1$ and $K_0: C=0$. Intervening via $\text{do}(A=a)$ cuts the link $C \to A$.
$$P(R=1 \mid \text{do}(A=1)) = \sum_{c \in \{0, 1\}} P(R=1 \mid C=c) P(C=c) = \rho_C p + \rho_U (1-p).$$
Similarly,
$$P(R=1 \mid \text{do}(A=0)) = \rho_C p + \rho_U (1-p).$$

Thus, the causal expected utilities are:
$$U_{\text{CDT}}(A=1) = b - r [\rho_C p + \rho_U (1-p)],$$
$$U_{\text{CDT}}(A=0) = 0 - r [\rho_C p + \rho_U (1-p)].$$

Because $b > 0$, $U_{\text{CDT}}(A=1) > U_{\text{CDT}}(A=0)$ strictly. CDT correctly diagnoses that David's decision cannot causally alter his personality trait $C$, and therefore recommends summoning Bathsheba.

### 4.2. Newcomb's Paradox
A predictor presents two boxes:
- Box 1: Transparent, contains $\$1,000$.
- Box 2: Opaque, contains either $\$1,000,000$ ($M$) or $\$0$.

The actions are:
- $A_1$: One-box (take Box 2 only).
- $A_2$: Two-box (take Box 1 and Box 2).

The predictor placed $\$1,000,000$ in Box 2 yesterday if and only if she predicted $A_1$. Let $S_1$ be the state where Box 2 contains $\$1,000,000$, and $S_0$ where Box 2 contains $\$0$. Assume linear utility $u(\$x) = x$, and predictor accuracy $P(S_1 \mid A_1) = P(S_0 \mid A_2) = q = 0.99$.

#### EDT Calculation:
$$V_{\text{EDT}}(A_1) = q \cdot 1,000,000 + (1-q) \cdot 0 = 990,000,$$
$$V_{\text{EDT}}(A_2) = (1-q)(1,000,000 + 1,000) + q(1,000) = 10,000 + 1,000 = 11,000.$$
EDT emphatically recommends **one-boxing** ($A_1$).

#### CDT Calculation:
The contents of Box 2 are causally fixed yesterday; no backward causation is physically possible. The causal dependency hypotheses are simply the states of Box 2: $\mathcal{K} = \{S_0, S_1\}$.
Under counterfactuals:
$$A_1 \mathbin{\Box\to} \text{Receive } \$0 \quad (\text{under } S_0), \qquad A_1 \mathbin{\Box\to} \text{Receive } \$1,000,000 \quad (\text{under } S_1),$$
$$A_2 \mathbin{\Box\to} \text{Receive } \$1,000 \quad (\text{under } S_0), \qquad A_2 \mathbin{\Box\to} \text{Receive } \$1,001,000 \quad (\text{under } S_1).$$

Let the agent's prior credence that Box 2 is full be $P(S_1) = p$.
$$U_{\text{CDT}}(A_1) = p(1,000,000) + (1-p)(0) = 1,000,000 \, p,$$
$$U_{\text{CDT}}(A_2) = p(1,001,000) + (1-p)(1,000) = 1,000,000 \, p + 1,000.$$

For any $p \in [0, 1]$:
$$U_{\text{CDT}}(A_2) - U_{\text{CDT}}(A_1) = 1,000 > 0.$$

Two-boxing strictly causally dominates one-boxing: in every state of the world, choosing $A_2$ causes the agent to receive $\$1,000$ more than choosing $A_1$. CDT mandates **two-boxing**.

---

## 5. Pathologies and Counterexamples: The Problem of Decision Instability

While CDT handles common cause problems like King David gracefully, critics (such as Andy Egan) have advanced scenarios where CDT's strict separation between choice and dependency hypotheses produces intuitively irrational or self-defeating behavior.

### 5.1. The Psychopath Button
Paul faces a button:
- If pressed ($B=1$), all psychopaths die. Paul believes a world without psychopaths is worth $+100$ utility.
- If not pressed ($B=0$), the status quo yields $0$ utility.
- However, Paul is certain that only a psychopath would press the button ($P(\text{Psy} \mid B=1) = 0.99$, $P(\text{Psy} \mid B=0) = 0.01$).
- If Paul is a psychopath, pressing the button will kill him ($u(\text{Dead}) = -1,000$).

Let state $K_1$ be "Paul is a psychopath" and $K_0$ be "Paul is normal." Paul cannot causally alter his neurological constitution by pressing the button: the causal arrow runs $\text{Psy} \to B$.

Suppose Paul begins with prior credence $P(K_1) = p = 0.05$.
Evaluating with CDT:
$$U(B=1) = p \, u(\text{Dead}) + (1-p) u(\text{World improved}) = 0.05(-1,000) + 0.95(100) = -50 + 95 = +45.$$
$$U(B=0) = 0.$$

CDT advises Paul to **press the button** ($45 > 0$). But notice the epistemic consequence: as soon as Paul decides to press, he learns that he is almost certainly a psychopath, meaning he anticipates that pressing will kill him.

### 5.2. Death in Damascus and Dynamic Instability
In the classic tale of *Death in Damascus*:
- Death predicts whether you will be in Damascus ($D$) or Aleppo ($A$) tomorrow, and travels there.
- You can go to Damascus ($a_D$) or Aleppo ($a_A$).
- Dying yields utility $-100$; surviving yields $0$.
- Death's prediction accuracy is $P(S_D \mid a_D) = P(S_A \mid a_A) = 0.99$, where $S_D$ is Death waiting in Damascus.

Suppose the agent currently plans to go to Damascus (credence $P(a_D) \approx 1$). Then $P(S_D) \approx 0.99$.
Under CDT, fixing the dependency hypothesis $P(S_D) = 0.99$:
$$U(a_D) = 0.99(-100) + 0.01(0) = -99,$$
$$U(a_A) = 0.01(-100) + 0.99(0) = -1.$$
Since $-1 > -99$, CDT commands the agent to flee to Aleppo ($a_A$).

Yet as soon as the agent decides on Aleppo, her credences shift: $P(S_A) \approx 0.99$. Now:
$$U(a_A) = -99, \qquad U(a_D) = -1.$$
CDT now commands the agent to turn back to Damascus. The preference structure is dynamically unstable: every available pure act is unratifiable.

### 5.3. Ratifiability and Deliberational Dynamics
To resolve this instability, Richard Jeffrey introduced the concept of **ratifiability**:
An act $A$ is ratifiable if and only if $A$ maximizes causal expected utility relative to the probability distribution updated on the assumption that $A$ will be performed:

$$U(A \mid A) \ge U(A' \mid A) \quad \forall A' \in \mathcal{A},$$

where $U(A' \mid A) = \sum_k P(K_k \mid A) \sum_j P(O_j \mid A' \land K_k) u(O_j)$.

In Death in Damascus, neither $a_D$ nor $a_A$ is ratifiable in pure strategies. 

#### Operational Extension: Deliberational Dynamics (Joyce, Skyrms)
Modern defenders of CDT (notably James M. Joyce) resolve this by treating deliberation as a continuous-time dynamical system over the probability simplex $\Delta^{m-1}$ of mixed policies $\mathbf{p} = (p_1, \dots, p_m)$, where $p_i = P(A_i)$.

As the agent deliberates, her tentative inclination toward an action provides epistemic evidence about her own internal state. The credence vector evolves according to a velocity field governed by causal expected utility:

$$\dot{p}_i = p_i \left[ U(A_i \mid \mathbf{p}) - \bar{U}(\mathbf{p}) \right],$$

where $\bar{U}(\mathbf{p}) = \sum_j p_j U(A_j \mid \mathbf{p})$ is the average causal utility, and $U(A_i \mid \mathbf{p})$ evaluates the causal utility of $A_i$ using credences conditioned on current mixed propensity $\mathbf{p}$.

In Death in Damascus, this dynamical system possesses a unique, stable fixed point at $p_D = p_A = 0.5$. At this equilibrium:
$$U(a_D \mid \mathbf{p}^*) = U(a_A \mid \mathbf{p}^*) = 0.5(-100) = -50.$$
By internalizing self-governing evidence during deliberation, CDT stabilizes on mixed strategies, resolving the infinite regress of vacillation.

---

## 6. Exploitation: Money Pumps and Dutch Books

A major challenge to CDT highlighted in recent literature (e.g., Spencer, Oesterheld & Conitzer) is vulnerability to Dutch books and guaranteed financial losses in adversarial prediction contexts.

### 6.1. The Adversarial Offer
Consider the game formalized by Oesterheld and Conitzer:
- Two boxes: Box 1 and Box 2.
- The player may purchase at most one box: $\mathcal{A} = \{\text{None}, \text{Buy}_1, \text{Buy}_2\}$.
- The cost to purchase a box is $\$1$.
- Yesterday, a seller with prediction accuracy $q = 0.75$ predicted the buyer's choice.
- The seller placed $\$3$ in each box predicted *not* to be acquired.
- If the seller predicts $\text{None}$, both boxes receive $\$3$.
- If the seller predicts $\text{Buy}_1$, Box 2 receives $\$3$ and Box 1 receives $\$0$.
- If the seller predicts $\text{Buy}_2$, Box 1 receives $\$3$ and Box 2 receives $\$0$.

Let $X_1, X_2 \in \{0, 3\}$ denote the money in Boxes 1 and 2, respectively.
Notice an invariant of the game: because the seller predicts at most one choice, she places $\$3$ in at least one box. Therefore:
$$X_1 + X_2 \ge 3 \implies \frac{X_1 + X_2}{2} \ge 1.50.$$

Now consider the reasoning of a standard CDT agent confronting this choice with symmetric prior credences $P(X_1 = 3) = P(X_2 = 3) = p$.
Because the contents are fixed in the past:
$$U_{\text{CDT}}(\text{None}) = 0,$$
$$U_{\text{CDT}}(\text{Buy}_1) = P(X_1 = 3) \cdot 3 - 1 = 3p - 1,$$
$$U_{\text{CDT}}(\text{Buy}_2) = P(X_2 = 3) \cdot 3 - 1 = 3p - 1.$$

What is the value of $p$? The average box contains $(X_1 + X_2)/2 \ge \$1.50$. By symmetry, the agent's expectation of a randomly chosen box must satisfy:
$$\mathbb{E}[X_1] = \mathbb{E}[X_2] \ge 1.50 \implies p \ge 0.50.$$

Substituting $p \ge 0.50$:
$$U_{\text{CDT}}(\text{Buy}_1) = 3(0.50) - 1 = 0.50 > 0 = U_{\text{CDT}}(\text{None}).$$

Hence, CDT strictly prefers buying a box to buying nothing. If the agent randomizes or picks Box 1, she buys a box. But the seller predicted this with $75\%$ accuracy! 
Consequently:
$$\mathbb{E}_{\text{actual}}[\text{Net Payoff}] = (0.25 \times \$3) - \$1 = \$0.75 - \$1.00 = -\$0.25.$$

The agent incurs an expected net loss of $\$0.25$ on a game where refusing to play ($\text{None}$) guarantees $\$0$. 

### 6.2. Diachronic Dutch Books
Oesterheld and Conitzer showed that this property allows an exploiter to run a **diachronic Dutch book** against a CDT agent. By offering a sequence of choices over time—first offering an option that CDT accepts because it holds causal dependency hypotheses fixed, and then offering a subsequent bet that hedges that choice—the exploiter can extract guaranteed risk-free money.

The CDT defender's response (e.g., Joyce, 2020) is that Newcomb-like setups are fundamentally adversarial games against mind-readers, not standard single-agent decision problems. CDT is designed to answer: *"What does my act causally produce in the physical world given how the world is?"* If the world is configured by an adversary who penalizes agents whose deliberation leads them to choose according to dominance, CDT accepts the lower payoff as the inevitable cost of being predictable, rather than a failure of rationality.

---

## 7. Comparative Summary

The essential differences between the major decision theories can be formalized by their evaluation of an action $A$ with respect to state/outcome distributions:

| Decision Theory | Mathematical Criterion | Conditioning Type | Stance on Newcomb ($q \approx 1$) |
| :--- | :--- | :--- | :--- |
| **Evidential (EDT)** | $\sum_j P(O_j \mid A) u(O_j)$ | Epistemic Bayesian conditionalization | One-box ($A_1$) |
| **Causal (CDT)** | $\sum_j P(A \mathbin{\Box\to} O_j) u(O_j) = \sum_k P(K_k) \sum_j P(O_j \mid A \land K_k) u(O_j)$ | Counterfactual imaging / Causal intervention $\text{do}(A)$ | Two-box ($A_2$) |
| **Ratifiable CDT** | $\arg\max_A U(A \mid A)$ subject to equilibrium in deliberation dynamics | Self-reflective causal conditioning | Mixed / Equilibrium strategy |

---

## 8. Conclusion

Causal Decision Theory represents a mathematically principled attempt to formalize rational human agency. By decoupling the epistemic news value of an action from its physical efficacy, CDT immunizes decision-makers from confusing correlation with causation. It ensures that an agent will not adopt superstitious rituals or suppress benign desires simply because they happen to be symptomatically linked to adverse, uncontrollable conditions.

Nonetheless, CDT’s insistence on evaluating actions by holding fixed the unconditional credences in past states leaves it vulnerable in environments featuring highly accurate predictors. The ongoing development of ratifiability criteria, deliberational dynamics, and structural intervention models illustrates that CDT is not a closed dogma, but an evolving, foundational program at the intersection of causal inference, probability theory, and mathematical philosophy.

---

## References

1. Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
2. Egan, A. (2007). Some counterexamples to causal decision theory. *The Philosophical Review*, 116(1), 93–114.
3. Gibbard, A., & Harper, W. L. (1981). Counterfactuals and two kinds of expected utility. In *Ifs: Conditionals, Beliefs, Decision, Chance, and Time* (pp. 153–190). Springer.
4. Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
5. Joyce, J. M. (2012). Regret and instability in causal decision theory. *Synthese*, 187(1), 123–145.
6. Lewis, D. (1976). Probabilities of conditionals and conditional probabilities. *The Philosophical Review*, 85(3), 297–315.
7. Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
8. Oesterheld, C., & Conitzer, V. (2021). Extracting money from causal decision theorists. *The Philosophical Quarterly*, 71(4), pqaa086.
9. Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
10. Skyrms, B. (1984). *Pragmatics and Empiricism*. Yale University Press.
11. Spencer, J. (2020). An argument against causal decision theory. *Analysis*, 81(1), 52–61.