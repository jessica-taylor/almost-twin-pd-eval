# The Geometry of Intervention: A Mathematical Account of Causal Decision Theory

## 1. Introduction: The Efficacy-News Dilemma

Standard decision theory formalizes rational choice under uncertainty by evaluating an action through its expected utility. However, standard subjective expected utility hides a foundational ambiguity: should an action be valued for what it *indicates* or for what it *brings about*?

In ordinary scenarios—such as choosing whether to carry an umbrella based on morning barometric pressure—observational correlation matches causal efficacy. Carrying the umbrella does not cause rain, but neither does it correlate with rain in a way that suggests the weather depends on the choice itself. However, when an agent's choice correlates with state variables that the choice cannot causally influence, this alignment collapses.

**Evidential Decision Theory (EDT)** values an action $A$ according to its *news value*: how favorable the world is expected to be upon learning that $A$ was performed:
$$V_{\mathrm{EDT}}(A) = \sum_{j} P(O_j \mid A)\, u(O_j),$$
where $P(\cdot \mid A)$ denotes standard epistemic conditioning and $u(O_j)$ is the utility of outcome $O_j$.

**Causal Decision Theory (CDT)** rejects this criterion. Under CDT, an agent ought not to choose an action merely because taking it would be welcome news; rather, the agent should choose an action if and only if the action *physically causes* the superior outcome. When correlation and causation pull apart, EDT recommends managing one's evidence ("managing the news"), whereas CDT insists on acting solely to effect changes in the physical world.

This essay develops the formal architecture of CDT, traces how it separates counterfactual consequence from conditional credence, evaluates classic dilemmas and modern pathologies, and addresses the open operational questions surrounding counterfactual evaluation.

---

## 2. Formal Foundations of CDT

The canonical formulation of CDT was introduced by Allan Gibbard and William Harper (1981), building on David Lewis’s semantics for counterfactual conditionals. 

### 2.1 The Gibbard–Harper Formulation

Let $\mathcal{A} = \{A_1, A_2, \dots, A_n\}$ be a mutually exclusive and exhaustive set of available acts, and $\mathcal{O} = \{O_1, O_2, \dots, O_m\}$ a partition of possible outcomes. Each outcome $O_j$ is assigned a utility $u(O_j) \in \mathbb{R}$ (termed "desirability" $D(O_j)$ by Gibbard and Harper).

Gibbard and Harper express the causal expected utility $U(A)$ in terms of probabilities of counterfactual conditionals:
$$U_{\mathrm{CDT}}(A) = \sum_{j} P(A \to O_j)\, u(O_j),$$
where $A \to O_j$ is the conditional proposition: *"If the agent were to perform $A$, then outcome $O_j$ would obtain."*

Crucially, the connective $\to$ is not material implication ($A \implies O_j \equiv \neg A \lor O_j$), nor is $P(A \to O_j)$ equal to the conditional probability $P(O_j \mid A)$.

### 2.2 Dependency Hypotheses and Causal Partitions

An alternative, mathematically clarifying framing introduced by David Lewis (1981) avoids explicit modal conditionals by invoking a partition of **dependency hypotheses** $\mathcal{K} = \{K_1, K_2, \dots, K_r\}$.

A dependency hypothesis $K \in \mathcal{K}$ is a maximal proposition specifying how every potential action $A \in \mathcal{A}$ causally leads to a specific outcome $O \in \mathcal{O}$. That is, $K$ completely fixes the causal response function of the world to the agent's interventions:
$$K \implies \bigwedge_{i=1}^n (A_i \to O(A_i, K)).$$

Because a rational agent's current choice cannot retroactively or non-locally cause the state of nature $K$ to be true, the hypothesis $K$ is causally independent of $A$. Under this formulation:
$$U_{\mathrm{CDT}}(A) = \sum_{K \in \mathcal{K}} P(K)\, u(O(A, K)).$$
In Lewis's framing, the agent weights the value of the outcome brought about by $A$ under condition $K$ by their *unconditional* credence $P(K)$, refusing to update $P(K)$ to $P(K \mid A)$.

---

## 3. Conditionals vs. Conditional Probabilities: The Lewis Wedge

The mathematical divergence between CDT and EDT stems from the relationship between $P(A \to B)$ and $P(B \mid A)$.

### 3.1 Lewis’s Triviality Result

It is tempting to assume that the probability of a counterfactual conditional is simply the conditional probability, a thesis known as *The Equation* or Stalnaker's Hypothesis:
$$P(A \to B) \stackrel{?}{=} P(B \mid A) \quad \text{for all } P \text{ with } P(A) > 0.$$

David Lewis (1976) proved that this equation is mathematically untenable. Specifically, if a probability measure $P$ supports non-trivial propositions and is closed under conditionalization, equating conditional credences with probabilities of conditionals collapses the probability space into a trivial algebra where $P$ can take at most four distinct values. Counterfactual truth cannot be modeled as epistemic updating.

### 3.2 When Does CDT Coincide with EDT?

Gibbard and Harper established conditions under which the two theories agree. Suppose the domain satisfies the **Principle of Conditional Excluded Middle (CEM)**:
$$(A \to B) \lor (A \to \neg B) \quad \text{is valid}.$$
If an act $A$ is statistically independent of the counterfactual conditionals it governs—that is, for all $j$:
$$P(A \to O_j \mid A) = P(A \to O_j),$$
then by Bayes' theorem and the definition of counterfactuals:
$$P(A \to O_j) = P(A \to O_j \mid A) = P(O_j \mid A).$$

Under causal and statistical independence, $U_{\mathrm{CDT}}(A) = V_{\mathrm{EDT}}(A)$. The two theories diverge precisely when an action $A$ provides evidence about the truth of counterfactuals without causally determining them: $P(A \to O_j \mid A) \neq P(A \to O_j)$.

---

## 4. Canonical Demonstrations

### 4.1 The Common Cause: King David and Bathsheba

Gibbard and Harper illustrate this distinction using the biblical narrative of King David. David desires Bathsheba, the wife of Uriah. He knows the political landscape:
1. Kings are either *charismatic* ($C$) or *uncharismatic* ($\neg C$). Charisma is fixed early in childhood and cannot be altered in adulthood ($P(A \to C) = P(C)$).
2. Uncharismatic kings have an ignoble bearing, which causes frequent, successful revolts ($R$). Charismatic kings project authority, making revolts rare.
3. Unjust acts ($A$, summoning Bathsheba) do not themselves cause revolts; rather, the ignoble bearing of uncharismatic kings causes revolts.
4. However, uncharismatic kings are far more inclined to commit unjust acts than charismatic kings: $P(C \mid A) \ll P(C \mid \neg A)$.

David faces a choice between $A$ (summon Bathsheba) and $\neg A$ (abstain). The causal graph is a classic common cause fork:

```
          Charisma (C)
          /          \
         v            v
    Act (A)        Revolt (R)
```

Because $A$ does not cause $R$, the counterfactual outcome of revolt is causally fixed by $C$:
$$A \to R \equiv \neg C, \qquad \neg A \to R \equiv \neg C.$$

Therefore, under CDT:
$$P(A \to R) = P(\neg C) = P(\neg A \to R).$$
Let the baseline utility of having Bathsheba be $+b$, and the penalty of a revolt be $-r$, with $r \gg b > 0$. The causal expected utility of summoning Bathsheba is:
$$U_{\mathrm{CDT}}(A) = b - r\,P(\neg C),$$
while abstaining yields:
$$U_{\mathrm{CDT}}(\neg A) = 0 - r\,P(\neg C).$$
Because $U_{\mathrm{CDT}}(A) - U_{\mathrm{CDT}}(\neg A) = b > 0$, CDT unambiguously recommends taking Bathsheba: summoning her cannot *cause* David to become uncharismatic, nor does it cause a revolt.

Conversely, EDT observes that $P(\neg C \mid A)$ is high. The evidential expectation is:
$$V_{\mathrm{EDT}}(A) = b - r\,P(R \mid A) \approx b - r\,P(\neg C \mid A),$$
$$V_{\mathrm{EDT}}(\neg A) = 0 - r\,P(R \mid \neg A) \approx - r\,P(\neg C \mid \neg A).$$
Because $P(\neg C \mid A) \gg P(\neg C \mid \neg A)$, $V_{\mathrm{EDT}}(\neg A) > V_{\mathrm{EDT}}(A)$. EDT recommends abstention, treating David's decision as news about his inherent charisma. CDT diagnoses this as an irrational attempt to suppress the symptom of an unalterable condition.

### 4.2 Newcomb’s Problem

In Newcomb’s Problem, an agent faces two boxes:
- **Box 1**: Transparent, containing $\$1,000$.
- **Box 2**: Opaque, containing either $\$1,000,000$ or $\$0$.

The agent can choose either Box 2 only (one-boxing, $A_1$) or both Box 1 and Box 2 (two-boxing, $A_2$). Yesterday, an extraordinarily accurate predictor (accuracy $p = 0.99$) predicted the agent’s choice:
- If predicted to choose $A_1$, the predictor placed $\$1,000,000$ in Box 2.
- If predicted to choose $A_2$, the predictor left Box 2 empty.

The money is already in the boxes; the contents cannot be causally altered by the agent's current act.

Let the dependency hypotheses be:
- $K_1$: Box 2 contains $\$1,000,000$.
- $K_0$: Box 2 contains $\$0$.

Under CDT, the agent evaluates the causal consequences holding fixed the state of the world:
$$U_{\mathrm{CDT}}(A_1) = P(K_1)\,u(\$1,000,000) + P(K_0)\,u(\$0),$$
$$U_{\mathrm{CDT}}(A_2) = P(K_1)\,u(\$1,001,000) + P(K_0)\,u(\$1,000).$$

Assuming linear utility $u(x) = x$:
$$U_{\mathrm{CDT}}(A_2) - U_{\mathrm{CDT}}(A_1) = P(K_1)(1,001,000 - 1,000,000) + P(K_0)(1,000 - 0) = \$1,000.$$
Because $U_{\mathrm{CDT}}(A_2) - U_{\mathrm{CDT}}(A_1) = \$1,000 > 0$ for *any* probability distribution $(P(K_1), P(K_0))$, two-boxing strictly dominates one-boxing causally. The predictor's past actions are causally invariant with respect to the present choice:
$$A_1 \to K_1 \iff K_1 \quad \text{and} \quad A_2 \to K_1 \iff K_1.$$

By contrast, EDT conditions on the act:
$$V_{\mathrm{EDT}}(A_1) = P(K_1 \mid A_1)(10^6) = 0.99 \times 10^6 = \$990,000,$$
$$V_{\mathrm{EDT}}(A_2) = 1,000 + P(K_1 \mid A_2)(10^6) = 1,000 + 0.01 \times 10^6 = \$11,000.$$
EDT strongly recommends one-boxing. CDT proponents characterize one-boxing as an irrational attempt to retroactively rewrite the past.

---

## 5. Computing Counterfactuals: Operationalizing CDT

The Wikipedia reference highlights a critical critique: **Gibbard and Harper’s basic formulation leaves open the algorithm for computing $P(A \to O)$.** To turn CDT into an operational theory, one must formally ground counterfactual probabilities.

### 5.1 Lewisian Imaging

David Lewis (1981) proposed the method of **imaging**. Let $W$ be a set of possible worlds, and let $P$ be a probability distribution over $W$. Assume a metric or similarity relation on worlds such that for each world $w \in W$ and proposition $A \neq \emptyset$, there is a unique closest world $w_A$ in which $A$ is true. 

The probability distribution obtained by *imaging on $A$*, denoted $P_A$, transfers the probability mass of each world $w$ entirely to its most similar $A$-world $w_A$:
$$P_A(w') = \sum_{w \in W \,:\, w_A = w'} P(w).$$
Under this construction, the counterfactual probability is defined as:
$$P(A \to O_j) = P_A(O_j) = \sum_{w \in O_j} P_A(w).$$

While mathematically elegant, imaging faces an operational regress pointed out by Shaffer (2009): determining which world is "closest" requires evaluating counterfactual assertions about physical laws and initial conditions. If an agent is uncertain about the underlying similarity metric, they must assign credences over metrics, yielding a meta-level counterfactual regress.

### 5.2 Pearlian Interventions: Structural Causal Models

To make CDT rigorously computable and bridge philosophy with computer science, we propose an operationalization using Judea Pearl’s Structural Causal Models (SCMs). While this formulation goes beyond the historical Gibbard–Harper text, it provides a mathematically well-defined realization of CDT that eliminates ambiguities regarding "world similarity."

An SCM is a 4-tuple $M = \langle U, V, F, P(U) \rangle$, where:
- $U$ is a set of background, exogenous variables determined outside the model, distributed according to $P(U)$.
- $V$ is a set of observable, endogenous variables.
- $F = \{f_X\}_{X \in V}$ is a set of deterministic structural equations:
  $$X = f_X(\mathrm{PA}_X, U_X),$$
  where $\mathrm{PA}_X \subseteq V \setminus \{X\}$ are the endogenous parents of $X$, and $U_X \subseteq U$.

In this framework, an action is formalized not as an event conditioning the distribution, but as an **intervention**, denoted by the $\mathrm{do}$-operator:
$$\mathrm{do}(A = a).$$
The operation $\mathrm{do}(A = a)$ surgically replaces the structural equation $A = f_A(\mathrm{PA}_A, U_A)$ with the constant assignment $A = a$, severing all incoming directed edges to $A$ while leaving the rest of the network intact.

```
Standard Graph (EDT):            Intervention Graph (CDT):
     U                                    U
   /   \                                    \
  v     v                                    v
  A ---> Y                              a    Y
```

Under this proposal, the counterfactual probability is defined as:
$$P(A \to O_j) \equiv P(O_j \mid \mathrm{do}(A)).$$
Using Pearl’s truncated factorization (or the G-formula), the causal expected utility of an action $a \in \mathcal{A}$ on a set of outcome variables $Y$ simplifies to:
$$U_{\mathrm{SCM}}(a) = \mathbb{E}[u(Y) \mid \mathrm{do}(A = a)] = \sum_{y} u(y) \sum_{x \setminus \{A, Y\}} P(y \mid a, \mathrm{pa}_A) \prod_{X_i \in V \setminus \{A\}} P(x_i \mid \mathrm{pa}_i).$$

When latent confounders exist (as in Newcomb's problem, where the predictor’s psychological model $U$ causes both prediction $S$ and action $A$), the joint distribution factors as $P(S, A, Y) = P(U)P(S \mid U)P(A \mid U)P(Y \mid S, A)$. 

Intervening on $A$ breaks the link $U \to A$:
$$P(S = s \mid \mathrm{do}(A = a)) = P(S = s).$$
Thus, the Pearlian formulation reproduces the two-boxing result directly: Box 2's contents $S$ are completely independent of $\mathrm{do}(A)$, rendering $P(S \mid \mathrm{do}(A)) = P(S)$.

---

## 6. Pathologies, Instabilities, and Counterexamples

Despite its causal clarity, CDT faces significant structural challenges. When an agent's causal decision informs their own beliefs about their type or desires, severe pathologies can emerge.

### 6.1 The Psychopath Button

Introduced by Andy Egan (2007), the Psychopath Button highlights CDT's vulnerabilities:
- Paul can push a button ($B$) that will instantly kill all psychopaths.
- Paul strongly prefers living in a world without psychopaths to living in a world with them.
- However, Paul desires living above all else: dying is catastrophic.
- Paul believes that only a psychopath would ever push the button: $P(\text{Paul is a psychopath} \mid B) \approx 1$.
- Pushing the button does not *cause* Paul to become a psychopath; his neurology is genetically fixed.

Let $C$ denote the state that Paul is a psychopath, and $\neg C$ that he is normal. The payoff matrix is:

| State | Press ($B$) | Refrain ($\neg B$) |
| :--- | :--- | :--- |
| **Psychopath ($C$)** | Dead ($-100$) | Live with psychopaths ($0$) |
| **Normal ($\neg C$)** | Live, no psychopaths ($+10$) | Live with psychopaths ($0$) |

Under CDT, Paul evaluates the choice using his *current* unconditional credence that he is a psychopath, $P(C)$. Suppose Paul initially believes $P(C) = 0.01$:
$$U_{\mathrm{CDT}}(B) = P(C)(-100) + P(\neg C)(+10) = 0.01(-100) + 0.99(10) = -1 + 9.9 = +8.9,$$
$$U_{\mathrm{CDT}}(\neg B) = P(C)(0) + P(\neg C)(0) = 0.$$

Because $U_{\mathrm{CDT}}(B) > U_{\mathrm{CDT}}(\neg B)$, CDT directs Paul to press the button. 

Yet Paul knows that as soon as he decides to press the button, he must update his credence: $P(C \mid B) \approx 1$. He will know he has almost certainly committed suicide. Egan terms this a breakdown of rationality: CDT directs an agent to take an action that the agent can foresee will result in disaster.

### 6.2 Death in Damascus and Dynamic Instability

In the classic *Death in Damascus* problem, Death informs an agent in Damascus that they have an appointment tomorrow. The agent can stay in Damascus ($D$) or flee to Aleppo ($A$). Death is an infallible predictor:
- If Death predicts $D$, Death waits in Damascus.
- If Death predicts $A$, Death waits in Aleppo.

Meeting Death yields utility $-100$; avoiding Death yields $0$. The act of traveling does not causally dictate Death's location, which was fixed earlier that morning.

Let $L_D$ and $L_A$ denote Death's presence in Damascus and Aleppo, respectively.
- If the agent currently plans to stay in Damascus ($P(D) \approx 1$), they infer that Death predicted $D$, so $P(L_D) \approx 1$.
  Then:
  $$U_{\mathrm{CDT}}(D) = -100, \qquad U_{\mathrm{CDT}}(A) = 0.$$
  The agent rationally decides to flee to Aleppo ($A$).
- But as soon as the agent decides to flee to Aleppo ($P(A) \approx 1$), they infer that Death predicted $A$, so $P(L_A) \approx 1$.
  Now:
  $$U_{\mathrm{CDT}}(A) = -100, \qquad U_{\mathrm{CDT}}(D) = 0.$$
  The agent shifts their preference back to Damascus ($D$).

This produces **deliberational instability**: no pure action is stable under causal evaluation.

### 6.3 Operational Extension: Deliberational Dynamics and Ratifiability

To resolve this instability, Richard Jeffrey proposed the concept of **ratifiability**, developed formally by Harper (1984):

> **Definition (Ratifiability):** An action $A$ is ratifiable if and only if it maximizes causal expected utility relative to the probability distribution updated on the premise that $A$ will be performed:
> $$U(A \mid A) \ge U(A' \mid A) \quad \text{for all } A' \in \mathcal{A}.$$

In *Death in Damascus*, neither pure act is ratifiable:
$$U(D \mid D) = -100 < U(A \mid D) = 0,$$
$$U(A \mid A) = -100 < U(D \mid A) = 0.$$

To preserve an operational decision procedure, CDT must be extended. Modern causal theorists (notably Jim Joyce) expand the decision space to mixed strategies (probability distributions over pure actions) accompanied by a dynamic model of deliberation:
1. Let $p_t = P_t(A)$ be the agent's subjective probability that they will choose $A$ at deliberation time $t$.
2. The agent updates their credences about background states $K$ continuously based on this deliberation: $P_t(K) = \sum_a P_t(K \mid A_a) p_{t, a}$.
3. Pure causal utilities become time-dependent: $U_t(A) = \sum_K P_t(K) u(O(A, K))$.
4. Probabilities evolve along a gradient driven by causal utility differences:
   $$\frac{dp_{t, i}}{dt} = p_{t, i} \left( U_t(A_i) - \bar{U}_t \right),$$
   where $\bar{U}_t = \sum_j p_{t, j} U_t(A_j)$.

In *Death in Damascus*, this deliberational dynamic possesses a unique, stable fixed point at $p^* = P(D) = 0.5$. At this equilibrium, the causal expected utilities equalize:
$$U(D) = 0.5(-100) = -50 = U(A).$$
By formalizing deliberation as an internal dynamical system, CDT agents can reach stable, mixed-strategy equilibria in otherwise cyclical dilemmas.

---

## 7. Adversarial Dilemmas and Diachronic Dutch Books

Recent work by Spencer (2020) and Oesterheld & Conitzer (2021) demonstrates that CDT’s vulnerability extends beyond unstable preferences to structural money pumps.

### 7.1 The Adversarial Offer

Consider the scenario formalized by Oesterheld and Conitzer:
- Two boxes, 1 and 2, are available. An agent may purchase at most one box for $\$1$.
- Yesterday, an accurate predictor ($p = 0.75$) placed $\$3$ in each box that she predicted the agent would **not** buy.
- If she predicted the agent would buy Box 1, she placed $\$3$ in Box 2 (and $\$0$ in Box 1).
- If she predicted the agent would buy Box 2, she placed $\$3$ in Box 1 (and $\$0$ in Box 2).
- If she predicted the agent would buy nothing, she placed $\$3$ in both boxes.

The agent reasons causally. Let $M_1, M_2 \in \{0, 3\}$ denote the money in each box. The agent knows that the predictor cannot have predicted the agent to buy *both* boxes. Therefore, at least one box contains $\$3$:
$$M_1 + M_2 \ge 3.$$
By symmetry and the linearity of expectation:
$$\mathbb{E}[M_1] + \mathbb{E}[M_2] \ge 3 \implies \frac{\mathbb{E}[M_1] + \mathbb{E}[M_2]}{2} \ge \$1.50.$$
Because the cost of purchasing a box is only $\$1.00$, the average causal expected return across the two boxes is at least $\$1.50 - \$1.00 = +\$0.50$. 

Consequently, CDT requires the agent to purchase a box: abstaining yields $\$0$, whereas at least one of the boxes offers positive causal expected value.

However, the predictor anticipated the choice with $75\%$ accuracy. Whichever box the agent selects, it will contain $\$0$ with probability $0.75$, and $\$3$ with probability $0.25$. The true expected return is:
$$\mathbb{E}[\text{Return}] = 0.25(\$3) - \$1 = \$0.75 - \$1.00 = -\$0.25.$$
The seller systematically extracts money from the CDT agent. Because CDT evaluates the contents of the boxes as causally fixed, it ignores the predictable negative correlation between its choice and the reward, making it vulnerable to diachronic Dutch books.

---

## 8. Comparative Synthesis

The central characteristics of the major frameworks are contrasted below:

| Feature | Evidential Decision Theory (EDT) | Causal Decision Theory (Gibbard–Harper / Lewis) | Operational CDT (Pearlian SCM) |
| :--- | :--- | :--- | :--- |
| **Governing Quantity** | $V(A) = \sum_j P(O_j \mid A) u(O_j)$ | $U(A) = \sum_j P(A \to O_j) u(O_j)$ | $U(A) = \mathbb{E}[u(Y) \mid \mathrm{do}(A)]$ |
| **Newcomb's Problem** | 1-box (maximize news value) | 2-box (exploit causal dominance) | 2-box (cut graph edge from predictor) |
| **Bathsheba Problem** | Abstain (avoid bad news) | Summon Bathsheba (exploit lack of causal link) | Summon Bathsheba (intervene independently of charisma) |
| **Psychopath Button** | Does not press | Presses (under standard non-ratified formulation) | Presses (requires deliberational dynamics to resist) |
| **Computational Basis** | Epistemic conditioning | World-similarity metrics / Imaging | Structural equations & edge-breaking |
| **Vulnerability** | Manipulated by benign correlation | Adversarial Dutch books, dynamic instability | Vulnerable to predictors modeling the agent's code |

---

## 9. Conclusion

Causal Decision Theory provides an intuitive, physically grounded account of rational agency. By breaking free from the naive news value of conditional probability, CDT reflects how human and artificial agents interact with an external physical environment: we deliberate to make changes in the world, not to console ourselves with flattering evidence.

Yet, this fidelity to causal realism creates deep formal challenges. Lewis’s triviality results demonstrate that probabilities of counterfactuals cannot simply be derived from standard conditional credences. While Structural Causal Models resolve the operational computational vagueness of Lewisian imaging, they cannot rescue CDT from its deeper behavioral paradoxes. When an agent faces adversarial predictors or common causes linked to their own internal deliberation—as seen in the Psychopath Button, Death in Damascus, and Adversarial Offers—pure CDT struggles to account for the evidence provided by its own pending decisions. 

To remain viable in interactive and adversarial settings, CDT must look beyond static causal evaluations toward unified deliberational and game-theoretic dynamics, where the agent's internal choice process is treated as an integrated part of the world it seeks to influence.

---

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Egan, A. (2007). Some counterexamples to causal decision theory. *The Philosophical Review*, 116(1), 93–114.
- Gibbard, A., & Harper, W. L. (1981). Counterfactuals and two kinds of expected utility. In *Ifs* (pp. 153–190). Springer, Dordrecht.
- Harper, W. (1984). Ratifiability and causal decision theory: Comments on Eells and Seidenfeld. *PSA: Proceedings of the Biennial Meeting of the Philosophy of Science Association*, 1984(2), 213–228.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Joyce, J. M. (2012). Regret and instability in causal decision theory. *Synthese*, 187(1), 123–145.
- Lewis, D. (1976). Probabilities of conditionals and conditional probabilities. *The Philosophical Review*, 85(3), 297–315.
- Lewis, D. (1979). Prisoners' dilemma is a Newcomb problem. *Philosophy & Public Affairs*, 8(3), 235–240.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
- Oesterheld, C., & Conitzer, V. (2021). Extracting money from causal decision theorists. *The Philosophical Quarterly*, 71(4).
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.
- Shaffer, M. J. (2009). Decision theory, intelligent planning and counterfactuals. *Minds and Machines*, 19(1), 61–92.
- Spencer, J. (2020). An argument against causal decision theory. *Analysis*, 81(1), 52–61.