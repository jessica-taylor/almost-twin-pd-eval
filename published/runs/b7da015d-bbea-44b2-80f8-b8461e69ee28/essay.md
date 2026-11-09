# Causal Decision Theory: Foundations, Formalisms, and Dilemmas

Decision theory formalizes what it means for an agent to choose rationally among alternative courses of action. While classical Bayesian decision theory dictates that an agent should maximize expected utility, the precise mathematical definition of "expectation" exposes a fundamental philosophical fault line. Does a rational agent choose an action because it serves as an auspicious omen of good fortune, or because the physical enactment of that action actively brings about a desirable state of affairs?

**Causal Decision Theory (CDT)** formalizes the latter principle: a rational choice must be guided solely by the causal consequences an action produces, rather than the news value it conveys. In contrast, **Evidential Decision Theory (EDT)** evaluates acts according to what learning that one has performed them would portend.

This essay provides a rigorous exposition of CDT. We examine its mathematical formulations, trace its divergence from EDT through probability theory and modal logic, formalize its decision rule across canonical dilemmas, and explore modern operationalizations and critiques.

---

## 1. The Core Divergence: Causation vs. Correlation

To understand CDT, consider Richard Jeffrey's classic formulation of evidential expected utility ($V$):
$$V(A) = \sum_{j} P(O_j \mid A)\, u(O_j)$$
where $A$ denotes an action, $O_j$ an outcome, and $u(O_j)$ the utility (or desirability) of that outcome. 

Under EDT, an agent weights outcomes by their ordinary Bayesian posterior probabilities, conditional on the event that $A$ occurs: $P(O_j \mid A)$. This formulation performs admirably in games of chance and isolated physical environments. However, it falters in the presence of confounding variables—common causes that induce a statistical correlation between an action and an outcome without any direct causal link.

### The King David and Bathsheba Dilemma
Gibbard and Harper (1981) illustrate this through the story of King David. David desires Bathsheba, but worries that summoning her will precipitate a palace revolt. Historical studies available to David establish that:
1. Kings are either *charismatic* ($C$) or *uncharismatic* ($\neg C$), determined entirely at birth.
2. Charismatic kings govern justly; uncharismatic kings govern unjustly. David knows that summoning another man's wife is unjust ($A$).
3. Revolts ($R$) occur frequently under uncharismatic kings and rarely under charismatic ones. Critically, unjust acts *do not cause* revolts; revolts are sparked by an uncharismatic ruler's fundamentally ignoble, weak demeanor.

Graphically, the causal graph is a fork:
$$\text{Charisma } (C) \longrightarrow \text{Summon Bathsheba } (A)$$
$$\text{Charisma } (C) \longrightarrow \text{No Revolt } (\neg R)$$

Because $A$ correlates negatively with $C$, observing that $A$ has occurred provides strong evidence that David is uncharismatic:
$$P(C \mid A) \ll P(C \mid \neg A) \implies P(R \mid A) \gg P(R \mid \neg A)$$
EDT calculates:
$$V(A) = P(R \mid A) u(A \wedge R) + P(\neg R \mid A) u(A \wedge \neg R)$$
Because $P(R \mid A)$ is high, EDT instructs David to abstain from summoning Bathsheba to preserve the comforting belief that he is charismatic.

Yet David's charisma is already fixed in the past; his present choice has no causal influence over his genetic endowment or childhood upbringing. Choosing not to summon Bathsheba cannot transmute an uncharismatic king into a charismatic one. CDT maintains that an agent should not manage their symptoms: an action must be judged strictly by what it *causes*, not what it *signifies*.

---

## 2. Formal Mathematical Formulations of CDT

CDT formalizes this distinction by replacing the epistemic conditional probability $P(O_j \mid A)$ with an objective or counterfactual measure of causal efficacy. Literature provides two primary formalisms: the counterfactual conditional approach of Gibbard and Harper, and the causal dependency hypothesis approach of Lewis.

### 2.1 The Gibbard–Harper Counterfactual Formulation
Gibbard and Harper (1981) define the causal expected utility $U(A)$ of an act $A \in \mathcal{A}$ via counterfactual conditionals:
$$U(A) = \sum_{j} P(A \mathbin{\Box\rightarrow} O_j)\, D(O_j)$$
where:
* $A \mathbin{\Box\rightarrow} O_j$ is the subjunctive conditional: "If the agent were to do $A$, then $O_j$ would occur."
* $P(A \mathbin{\Box\rightarrow} O_j)$ is the agent's subjective credence in the truth of that counterfactual.
* $D(O_j)$ is the desirability (utility) of outcome $O_j$.

The crucial mathematical question is whether $P(A \mathbin{\Box\rightarrow} O_j)$ reduces to the standard conditional probability $P(O_j \mid A)$. 

#### Lewis's Triviality Result
One might hope to define a conditional connective $\rightarrow$ such that for any probability function $P$ and propositions $A, B$, the identity $P(A \rightarrow B) = P(B \mid A)$ holds universally. David Lewis (1976) proved that this is mathematically impossible for non-trivial probability spaces. Specifically, if a probability measure $P$ supports $P(A \rightarrow B) = P(B \mid A)$ for all propositions and is closed under Bayesian conditionalization, then $P$ cannot assign non-zero probability to more than two mutually exclusive, non-empty events. Hence, counterfactual credences *cannot* generally be equated with standard conditional credences.

#### Conditional Excluded Middle and Independence
Gibbard and Harper demonstrated that $P(A \mathbin{\Box\rightarrow} B) = P(B \mid A)$ holds if and only if the act $A$ is statistically independent of the counterfactual conditional $A \mathbin{\Box\rightarrow} B$:
$$P((A \mathbin{\Box\rightarrow} B) \mid A) = P(A \mathbin{\Box\rightarrow} B)$$
This derivation relies on the **Principle of the Conditional Excluded Middle (CEM)**:
$$(A \mathbin{\Box\rightarrow} B) \vee (A \mathbin{\Box\rightarrow} \neg B)$$
which asserts that among possible worlds, there is a uniquely closest world (or that all closest worlds agree on whether $B$ holds). Under CEM:
$$P(B \mid A) = \frac{P(A \wedge B)}{P(A)} = \frac{P(A \wedge (A \mathbin{\Box\rightarrow} B))}{P(A)} = P((A \mathbin{\Box\rightarrow} B) \mid A)$$
If the performance of $A$ provides evidence about the truth of the conditional $A \mathbin{\Box\rightarrow} B$ itself—as in Newcomb's paradox or the King David problem—independence fails:
$$P((A \mathbin{\Box\rightarrow} B) \mid A) \neq P(A \mathbin{\Box\rightarrow} B)$$
causing EDT and CDT to prescribe diverging actions.

---

### 2.2 Lewis's Dependency Hypotheses Formulation
David Lewis (1981) introduced a formulation that avoids direct counterfactual logic by partitioning the state space into **causal dependency hypotheses**. 

Let $\mathcal{K} = \{K_1, K_2, \dots, K_m\}$ be a mutually exclusive and exhaustive partition of maximal propositions concerning how outcomes causally depend on the agent's actions. Each $K \in \mathcal{K}$ specifies a complete deterministic or propensist causal map from acts to outcomes: for any act $A_i$, $K$ completely fixes the objective chance $P_K(O_j \mid A_i)$ that outcome $O_j$ will occur if $A_i$ is executed.

Under this formulation, the causal expected utility is:
$$U(A) = \sum_{K \in \mathcal{K}} P(K) \sum_{j} P_K(O_j \mid A)\, u(A \wedge K \wedge O_j)$$
If the dependency hypotheses are deterministic, each pair $(A, K)$ uniquely entails a specific outcome $O(A, K)$, simplifying the formula to:
$$U(A) = \sum_{K \in \mathcal{K}} P(K)\, u(A \wedge K)$$

The key operational rule of CDT is that the probabilities $P(K)$ are the agent’s **unconditional prior credences** in the dependency hypotheses. The agent **holds fixed** these credences across all evaluated acts $A$. In contrast, EDT computes:
$$V(A) = \sum_{K \in \mathcal{K}} P(K \mid A)\, u(A \wedge K)$$
EDT allows the choice of $A$ to update the probability of which causal state $K$ actually obtains.

---

## 3. Structural Comparison: Newcomb's Paradox

Newcomb's Paradox serves as the central proving ground for CDT.

### Problem Specification
* **Act $A_1$ (One-box):** Take Box B only.
* **Act $A_2$ (Two-box):** Take both Box A and Box B.
* Box A transparently contains $\$1,000$.
* Box B contains either $\$1,000,000$ or $\$0$.
* A superintelligent predictor, with known predictive accuracy $p = 0.99$, placed $\$1,000,000$ into Box B yesterday if and only if it predicted the agent would choose $A_1$.

Let:
* $S_1$: State where Box B contains $\$1,000,000$.
* $S_0$: State where Box B contains $\$0$.

The payoffs (assuming linear utility in dollars) are:
* $u(A_1 \wedge S_1) = 10^6$
* $u(A_1 \wedge S_0) = 0$
* $u(A_2 \wedge S_1) = 10^6 + 10^3$
* $u(A_2 \wedge S_0) = 10^3$

```
                   State S_1 ($1M in B)      State S_0 ($0 in B)
Act A_1 (One-box)        $1,000,000                    $0
Act A_2 (Two-box)        $1,001,000                $1,000
```

### The EDT Calculation
An evidentialist conditions on the act:
$$P(S_1 \mid A_1) = 0.99, \quad P(S_0 \mid A_1) = 0.01$$
$$P(S_1 \mid A_2) = 0.01, \quad P(S_0 \mid A_2) = 0.99$$

Evaluating evidential expected utilities:
$$V(A_1) = (0.99)(10^6) + (0.01)(0) = 990,000$$
$$V(A_2) = (0.01)(10^6 + 10^3) + (0.99)(10^3) = 10,010 + 990 = 11,000$$
Because $V(A_1) \gg V(A_2)$, EDT recommends **one-boxing**.

### The CDT Calculation
Under CDT, the dependency hypotheses correspond precisely to the pre-existing contents of Box B, since the predictor made the deposit in the past:
* $K_1$: Box B contains $\$1,000,000$.
* $K_0$: Box B contains $\$0$.

Because the agent's present physical choice has no backwards-in-time causal power over whether money was placed in the box yesterday, the counterfactuals are:
$$P(A_1 \mathbin{\Box\rightarrow} S_1) = P(K_1), \quad P(A_2 \mathbin{\Box\rightarrow} S_1) = P(K_1)$$
$$P(A_1 \mathbin{\Box\rightarrow} S_0) = P(K_0), \quad P(A_2 \mathbin{\Box\rightarrow} S_0) = P(K_0)$$

Let $q = P(K_1)$ be the agent's credence that Box B contains the million dollars. We compute:
$$U(A_1) = q(10^6) + (1-q)(0) = 10^6 q$$
$$U(A_2) = q(10^6 + 10^3) + (1-q)(10^3) = 10^6 q + 10^3$$

For every value of $q \in [0, 1]$:
$$U(A_2) - U(A_1) = 1,000 > 0$$

Taking both boxes strictly **causally dominates** taking only Box B. The extra $\$1,000$ in Box A is yours for the taking regardless of whether the million is in Box B or not. CDT instructs the agent to **two-box**.

---

## 4. Operationalizing CDT: Lewisian Imaging vs. Pearlian Interventions

The Wikipedia source notes a key criticism: CDT itself does not mandate a single algorithm for computing counterfactual probabilities $P(A \mathbin{\Box\rightarrow} O)$. Historically, two major mathematical formalisms have emerged to fill this operational gap.

### 4.1 Lewisian Imaging
David Lewis (1981) proposed **imaging** as an alternative to Bayesian conditionalization. 

Let $W$ be a set of possible worlds, and let $P$ be a probability distribution over $W$. Assume a metric or selection function $f_A: W \to W$, where $f_A(w)$ selects the world closest to $w$ where proposition $A$ is true. 

When an agent calculates the probability of an outcome under the counterfactual assumption of $A$, they do not eliminate worlds where $\neg A$ holds and renormalize (as in conditionalization). Instead, they *shift* the probability mass of each world $w$ directly onto its nearest $A$-counterpart $f_A(w)$:
$$P_A(w') = \sum_{\{w \in W \mid f_A(w) = w'\}} P(w)$$
The counterfactual probability is then:
$$P(A \mathbin{\Box\rightarrow} O_j) = P_A(O_j) = \sum_{w \in W} P(w) \cdot \mathbb{I}(f_A(w) \models O_j)$$

#### The Infinite Regress Problem
As Shaffer (2009) critiques, imaging assumes an agent possesses an unambiguous distance metric over possible worlds and knows their beliefs conditional on $A$ being actualized. If an agent has uncertainty regarding which world is the closest $A$-world, they must assign probabilities to similarity functions themselves. This creates second-order conditionals, threatening an infinite regress of probabilistic evaluations.

### 4.2 Pearl's Causal Graphs and the $\text{do}$-Operator
A modern, rigorous operationalization of CDT that resolves this ambiguity is Judea Pearl's Structural Causal Model (SCM) framework. While omitted in classical 1980s philosophy texts, Pearl's calculus provides an operational engine for causal expected utility.

An SCM is a triple $M = \langle U, V, F \rangle$:
* $U$ is a set of exogenous background variables distributed according to $P(u)$.
* $V$ is a set of endogenous observable variables.
* $F = \{f_X \mid X \in V\}$ is a set of deterministic structural equations:
  $$x_i = f_i(\mathbf{pa}_i, u_i)$$
  where $\mathbf{pa}_i \subseteq V \setminus \{X_i\}$ are the direct causal parents of $X_i$.

In Pearl's calculus, taking an action $A = a$ is formalized not by conditioning on the event $A = a$, but by the **surgical intervention** $\text{do}(A = a)$. This intervention removes the structural equation for $A$ and sets $A$ to the constant value $a$, breaking all incoming edges from $A$'s parents:
$$f_A(\mathbf{pa}_A, u_A) \quad \Longrightarrow \quad A := a$$

```
    Normal Observation (EDT)                 Surgical Intervention (CDT)
      P(O | A) via Conditioning               P(O | do(A)) via Truncated Factorization
      
          [ Common Cause ]                         [ Common Cause ]
             /        \                                /        \
            v          v                              |          v
        [ Act A ] --> [ Outcome O ]              [ Act A := a ]  [ Outcome O ]
                                                 (incoming edge severed)
```

The resulting causal distribution $P(O \mid \text{do}(A = a))$ is derived from the truncated factorization formula:
$$P(v_1, \dots, v_n \mid \text{do}(A = a)) = \prod_{X_i \neq A} P(X_i \mid \mathbf{pa}_i)\Big|_{A=a}$$

Thus, CDT's decision rule can be operationalized as:
$$\text{CDT}(A) = \arg\max_{a} \sum_{o} P(O = o \mid \text{do}(A = a))\, u(o)$$
Whereas EDT calculates:
$$\text{EDT}(A) = \arg\max_{a} \sum_{o} P(O = o \mid A = a)\, u(o)$$

In Newcomb's problem, the predictor's past action $X_{\text{pred}}$ is an ancestor of $A$ via psychological traits $U$, and an ancestor of Box B's contents $B$:
$$U \to X_{\text{pred}} \to B \quad \text{and} \quad U \to A$$
The $\text{do}(A)$ operation severs the edge $U \to A$. Under this graph surgery:
$$P(B \mid \text{do}(A = a)) = P(B)$$
The state of Box B becomes completely independent of the choice of $A$. Pearl's formal graph surgery provides an exact mathematical realization of Lewis's requirement that the agent hold fixed their priors over causal hypotheses.

---

## 5. Counterexamples and Causal Instability

Despite its structural elegance, CDT faces serious challenges in scenarios where actions convey self-incriminating evidence about previously hidden, unavoidable states.

### 5.1 The Death in Damascus Scenario
In *Death in Damascus*, Death tells an agent, Paul, that he will visit him tomorrow. Paul can spend tomorrow in either Damascus ($D$) or Aleppo ($A$). Death is a near-perfect predictor of Paul's locations ($p = 0.99$). If Paul goes to where Death predicts he will be, he dies ($u = -100$); if he escapes Death, he lives ($u = 0$).

Suppose Paul currently leans toward going to Damascus: $P(D) \approx 1$.
* If Paul goes to Damascus, he counterfactually assumes Death is already waiting in Damascus. Thus, moving to Aleppo causally guarantees safety:
  $$U(A \mid \text{Death in Damascus}) = 0 > -100 = U(D \mid \text{Death in Damascus})$$
* However, as soon as Paul decides to go to Aleppo, this very deliberation updates his evidence about where Death is: Death, anticipating this, is almost certainly waiting in Aleppo!
* Now, holding fixed the belief that Death is in Aleppo, Damascus yields utility $0$ and Aleppo yields $-100$. CDT commands Paul to flee back to Damascus.

Paul enters an infinite cycle of deliberation: whichever choice he intends to make instantly becomes the causally worse choice.

#### Mathematical Instability: Ratifiability
To address this instability, Richard Jeffrey introduced the concept of **ratifiability**. An act $A$ is ratifiable if and only if $A$ maximizes causal expected utility *given the evidence that one has decided to perform $A$*:
$$U(A \mid A) \ge U(A' \mid A) \quad \forall A' \in \mathcal{A}$$

In Death in Damascus, neither pure act is ratifiable:
* Given that Paul will go to Damascus, $U(A \mid D) = 0 > -100 = U(D \mid D)$ (Damascus is unratifiable).
* Given that Paul will go to Aleppo, $U(D \mid A) = 0 > -100 = U(A \mid A)$ (Aleppo is unratifiable).

Standard CDT offers no stable pure strategy for such problems.

---

### 5.2 Egan's Psychopath Button
Andy Egan (2007) proposed the *Psychopath Button* to show that ratifiability fails to save CDT from perverse recommendations.

#### The Problem
* Paul can press a button ($B$) or abstain ($\neg B$).
* Pressing the button kills all psychopaths on Earth. Paul believes the world would be significantly better off without psychopaths ($+10$ utility).
* However, only psychopaths are psychologically capable of pressing the button. If Paul presses the button, he must be a psychopath, meaning he will die as well (yielding a catastrophic utility of $-100$).
* If Paul is not a psychopath, pressing the button would kill all other psychopaths while leaving him alive.

Let $S$ denote the state that Paul is a psychopath. Paul's initial credence is $P(S) = 0.01$.

#### Payoffs
* $u(\neg B \wedge S) = 0$
* $u(\neg B \wedge \neg S) = 0$
* $u(B \wedge S) = -100$ (Paul dies)
* $u(B \wedge \neg S) = +10$ (Paul lives, psychopaths eliminated)

#### CDT Evaluation
Because Paul's current physical act of pressing the button cannot causally change his underlying neurobiology, Paul evaluates the act holding his prior $P(S) = 0.01$ constant:
$$U(B) = P(S)\, u(B \wedge S) + P(\neg S)\, u(B \wedge \neg S)$$
$$U(B) = (0.01)(-100) + (0.99)(10) = -1 + 9.9 = +8.9$$
$$U(\neg B) = (0.01)(0) + (0.99)(0) = 0$$

Because $U(B) = 8.9 > 0 = U(\neg B)$, **CDT commands Paul to press the button**.

Yet Paul knows that pressing the button is definitive proof that he is a psychopath, condemning himself to death. Egan argues that holding fixed the agent's unconditional credences in dependency hypotheses forces CDT agents into self-destructive decisions.

---

### 5.3 The Adversarial Offer and Diachronic Dutch Books
Recent work by Oesterheld and Conitzer (2021) shows that CDT's refusal to factor in the news value of its actions renders agents vulnerable to dynamic exploitation.

#### The Adversarial Offer Game
* Two boxes, 1 and 2, cost $\$1$ each. The agent can buy Box 1, Box 2, or neither (buying both is forbidden).
* Yesterday, a seller with predictive accuracy $p = 0.75$ put $\$3$ into each box that she predicted the buyer would **not** buy.

**The CDT Reasoning:**
The buyer reasons that the contents of the boxes are physically fixed. 
* Case 1: The seller predicted the buyer will buy Box 1. Then Box 2 contains $\$3$, Box 1 contains $\$0$.
* Case 2: The seller predicted the buyer will buy Box 2. Then Box 1 contains $\$3$, Box 2 contains $\$0$.
* Case 3: The seller predicted the buyer will buy neither. Then both boxes contain $\$3$.

In every possible state of the world, the total amount of money across the two boxes is at least $\$3$. Therefore, by the pigeonhole principle, the average box contains at least $\$1.50$. Since each box costs only $\$1.00$, CDT concludes that buying a box has a strictly positive expected net gain:
$$\mathbb{E}[\text{Gain}] \ge 1.50 - 1.00 = +0.50$$
CDT mandates purchasing one of the boxes.

**The Reality:**
Because the seller is a reliable predictor ($p = 0.75$), whenever the buyer chooses Box 1, Box 1 is empty $75\%$ of the time. The buyer's expected return is:
$$\mathbb{E}[\text{Payoff}] = (0.25 \times \$3) + (0.75 \times \$0) = \$0.75$$
Net profit:
$$\$0.75 - \$1.00 = -\$0.25$$

The seller extracts money from the CDT agent with mathematical certainty over repeated iterations. As Oesterheld and Conitzer demonstrate, an agent whose choices do not condition on the predictive link to their own internal deliberation can be trapped in a **diachronic Dutch book**—a sequence of trades over time that guarantees a net financial loss.

---

## 6. Structural Summary

The analytical divide between the major decision paradigms can be codified through their formal operators and recommendations across test cases:

| Feature / Scenario | Evidential Decision Theory (EDT) | Causal Decision Theory (CDT) |
| :--- | :--- | :--- |
| **Foundational Metric** | Bayesian Conditioning: $P(O \mid A)$ | Counterfactual / Causal Intervention: $P(A \mathbin{\Box\rightarrow} O)$ or $P(O \mid \text{do}(A))$ |
| **Newcomb's Problem** | **One-box**: Secures strong evidence of $1M | **Two-box**: Dominance argument; choice cannot alter the past |
| **King David Dilemma** | **Abstain**: Avoids confirming uncharismatic personality | **Summon**: Charisma is predetermined; summon causes no revolt |
| **Psychopath Button** | **Do Not Press**: Pressing proves one is a psychopath | **Press**: Evaluates choice holding prior low psychopathy credence fixed |
| **Death in Damascus** | Stable mixed policy based on updating | Unstable deliberation; pure acts lack ratifiability |
| **Exploitation Vulnerability** | Immune to predictive Dutch books; vulnerable to smoking lesion confounds | Vulnerable to adversarial predictors exploiting deliberative blindness |

---

## Conclusion

Causal Decision Theory provides an essential corrective to the naive application of conditional probability in decision-making. By insisting that rational agents should manage the causes of outcomes rather than their symptoms, CDT formalizes the distinction between statistical correlation and physical intervention.

Through the formulations of Gibbard, Harper, and Lewis—and its natural expression in Judea Pearl's structural intervention calculus—CDT offers an intuitive decision framework for Conflicted scenarios like King David's dilemma and Newcomb's paradox. 

Yet, as the paradoxes of Egan, Spencer, and Oesterheld illustrate, CDT's strict insulation of dependency hypotheses from deliberative self-evidence creates vulnerabilities of its own. When an agent faces an adversarial environment populated by predictive counterparts, treating one's own impending action as causally inert relative to the background state can systematically bleed resources. 

The enduring challenge for modern decision theory lies in synthesizing CDT's causal sanity with EDT's acute self-awareness—constructing an agent that respects physical causality without blinding itself to the informative mirror of its own choices.

---

### References
* Egan, A. (2007). Some counterexamples to causal decision theory. *The Philosophical Review*, 116(1), 93–114.
* Gibbard, A., & Harper, W. L. (1981). Counterfactuals and two kinds of expected utility. In *Ifs: Conditionals, Beliefs, Decision, Chance, and Time* (pp. 153–190). Springer.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Lewis, D. (1976). Probabilities of conditionals and conditional probabilities. *The Philosophical Review*, 85(3), 297–315.
* Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
* Oesterheld, C., & Conitzer, V. (2021). Extracting money from causal decision theorists. *The Philosophical Quarterly*, 71(4).
* Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.
* Shaffer, M. J. (2009). Decision theory, intelligent planning and counterfactuals. *Minds and Machines*, 19(1), 61–92.