# 004_cdt_wikipedia_google_gemini-3.8-flash_rlow_plow / 00001

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/1e14f7c8-5ea0-44da-b38d-61ee960f197d/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/1e14f7c8-5ea0-44da-b38d-61ee960f197d/call_0/response.raw) · finish: `stop`

### Visible response

````text
# Causation, Correlation, and Counterfactual Expected Utility: A Mathematical Exposition of Causal Decision Theory

In standard Bayesian decision theory, a rational agent selects an action that maximizes expected utility. When formalized naively via standard conditional probabilities, however, this prescription yields **Evidential Decision Theory (EDT)**: it advises agents to choose the action that provides the most welcome *news* about the state of the world. While computationally straightforward, EDT frequently conflates correlation with causation. In scenarios featuring common causes, reliable predictors, or genetic pleiotropy, evidential reasoning can compel an agent to manage symptoms rather than effect cures.

**Causal Decision Theory (CDT)** arose to align rational choice with causal efficacy. Rather than evaluating what an action *indicates*, CDT evaluates what an action *brings about*. 

This essay provides a self-contained, mathematically rigorous treatment of CDT. We develop its foundational formulations—from Gibbard and Harper's counterfactual conditionals to Lewis's imaging and Pearl's modern structural causal models—derive its divergence from EDT, examine canonical decision problems, and analyze the central theoretical challenges that occupy contemporary researchers.

---

## 1. The Core Divergence: Causation vs. News Value

Let $\mathcal{A} = \{A_1, A_2, \dots, A_m\}$ be a mutually exclusive and exhaustive set of available acts, $\mathcal{S} = \{S_1, S_2, \dots, S_n\}$ a partition of possible states of the world, and $\mathcal{O} = \{O_1, O_2, \dots, O_k\}$ the set of possible outcomes. The agent possesses a utility function $u: \mathcal{O} \to \mathbb{R}$ (or a desirability function $D(O)$) reflecting preferences over outcomes, and an epistemic probability measure $P$ defined over an algebra containing states, acts, and outcomes.

Under **Evidential Decision Theory (EDT)**, the value of an act $A \in \mathcal{A}$ is its conditional expected utility, often called its *news value*:

$$V_{\text{EDT}}(A) = \sum_{j} P(O_j \mid A) \, u(O_j)$$

Under this metric, an agent prefers act $A$ over act $A'$ if and only if learning that $A$ was chosen warrants higher confidence in a desirable outcome than learning that $A'$ was chosen.

The foundational critique of EDT is that $P(O_j \mid A)$ reflects both causal influence and spurious evidential correlation. If a common cause $C$ independently influences both the propensity to choose $A$ and the realization of $O_j$, then $P(O_j \mid A) \neq P(O_j)$ even if $A$ exerts zero physical influence on $O_j$.

**Causal Decision Theory (CDT)** asserts that an agent should optimize *expected causal consequence*. Rational deliberation requires an operator that isolates the outcome distribution produced by *intervening* to set the action to $A$, holding fixed those background conditions that the agent's action cannot causally affect.

---

## 2. Formal Formulations of CDT

The formalization of CDT has taken several distinct mathematical routes. Below, we review the counterfactual approach of Gibbard and Harper, the imaging framework of Lewis, and the modern operationalization via Structural Causal Models.

### 2.1 The Gibbard–Harper Counterfactual Formulation

Allan Gibbard and William Harper (1981) formalized CDT using counterfactual conditionals. Let $A \to O_j$ denote the subjunctive proposition: *"If the agent were to perform act $A$, outcome $O_j$ would obtain."*

The causal expected utility $U_{\text{CDT}}(A)$ is defined as:

$$U(A) = \sum_{j} P(A \to O_j) \, u(O_j)$$

Here, $P(A \to O_j)$ is the agent's subjective probability assigned to the counterfactual conditional. 

#### Lewis's Triviality and Conditional Probability
A natural initial thought might be to equate the probability of a conditional with a conditional probability: $P(A \to B) \stackrel{?}{=} P(B \mid A)$. However, David Lewis (1976) proved that this equivalence cannot hold generally without reducing the probability space to triviality (where no more than two mutually incompatible propositions have positive probability). 

Gibbard and Harper demonstrated that $P(A \to O_j) = P(O_j \mid A)$ holds if the act $A$ is statistically independent of the counterfactual conditional $A \to O_j$:

$$P\big((A \to O_j) \mid A\big) = P(A \to O_j)$$

When an agent's choice correlates with the causal background—such as when a predictor anticipates the agent's choice—this independence fails. In such regimes, $P(A \to O_j) \neq P(O_j \mid A)$, driving an explicit mathematical Wedge between CDT and EDT.

---

### 2.2 Lewis's Formulation: Dependency Hypotheses and Imaging

David Lewis (1981) articulated CDT without primitive counterfactual operators by using the concept of **dependency hypotheses**. 

Let a dependency hypothesis $K \in \mathcal{K}$ be a maximally specific proposition describing how outcomes causally depend on the agent's actions. Formally, a dependency hypothesis completely specifies a function $f_K: \mathcal{A} \to \mathcal{O}$. Because an agent cannot causally influence which dependency hypothesis actually governs the world, Lewis argues that the agent's subjective credences across $\mathcal{K}$ must be held invariant when evaluating the efficacy of $A$.

The causal utility is thus given by:

$$U(A) = \sum_{K \in \mathcal{K}} P(K) \, u\big(f_K(A)\big) = \sum_{K \in \mathcal{K}} \sum_{j} P(K) \, \mathbb{I}\big(f_K(A) = O_j\big) \, u(O_j)$$

where $\mathbb{I}$ is the indicator function.

#### Probability Kinematics via Imaging
To construct $P(A \to \cdot)$, Lewis proposed probability kinematics known as **imaging**. Instead of standard Bayesian conditioning (which zeroes out worlds where $\neg A$ holds and rescales the remaining probabilities over the $A$-worlds), imaging shifts the probability mass of each possible world $w \in \Omega$ to the "closest" or "most similar" world $w_A$ in which $A$ is true:

$$P_A(w') = \sum_{\{w \in \Omega \,:\, w_A = w'\}} P(w)$$

Then, $P(A \to O_j) = P_A(O_j)$. While elegant, imaging requires a metric of similarity over possible worlds, an issue that critics argue introduces semantic vagueness or circular reliance on counterfactual intuitions.

---

### 2.3 An Operational Proposal: Structural Causal Models (SCMs)

*(Note: While the reference text notes that CDT does not uniquely specify an algorithm for calculating counterfactual probabilities, modern causal inference provides an exact operational framework via Pearl's Structural Causal Models. We detail this formulation to make CDT actionable for unfamiliar decision problems.)*

Let a decision problem be represented by an SCM $\mathcal{M} = \langle U, V, \mathcal{F}, P(U) \rangle$, where:
- $U$ is a set of exogenous background variables distributed according to $P(U)$.
- $V$ is a set of endogenous variables containing the action variable $X \in \mathcal{A}$, outcome variable $Y \in \mathcal{O}$, and intermediate causal states.
- $\mathcal{F} = \{f_v\}_{v \in V}$ is a set of deterministic structural equations $v = f_v(\text{PA}_v, U_v)$, where $\text{PA}_v \subseteq V \setminus \{v\}$.

Under Pearl's causal calculus, intervening on an action is modeled by the $\text{do}(X = A)$ operator, which replaces the structural equation for $X$ with the constant assignment $X \leftarrow A$, severing all incoming edges to $X$ while preserving the remainder of the causal graph:

$$U_{\text{SCM}}(A) = \mathbb{E}\big[u(Y) \mid \text{do}(X = A)\big] = \sum_{y} P(y \mid \text{do}(X = A)) \, u(y)$$

If the joint distribution of exogenous variables $U$ is independent of the intervention, the causal effect can be computed by adjusting for a sufficient covariate set $Z$ satisfying the back-door criterion:

$$P(y \mid \text{do}(X = A)) = \sum_{z} P(y \mid A, z) \, P(z)$$

This operationalization matches Lewis’s dependency hypotheses: each realization $u$ of the exogenous background variables $U$ determines a deterministic mapping from $X$ to $Y$, serving as a concrete mathematical instantiation of a dependency hypothesis $K$.

---

## 3. Deciding Classic Problems

To demonstrate the mechanical differences between CDT and EDT, we examine three classical decision problems.

### 3.1 King David and Bathsheba (Common Cause)

Gibbard and Harper introduce King David, who contemplates summoning Bathsheba ($A$). A revolt ($R$) may occur, carrying heavy disutility. David knows:
1. Kings possess fixed personality types: charismatic ($C$) or uncharismatic ($\neg C$), determined early in life and unalterable.
2. Uncharismatic kings tend to commit unjust acts like summoning another man's wife ($P(A \mid \neg C) > P(A \mid C)$).
3. Revolts occur almost exclusively against uncharismatic kings because of their ignoble bearing, not because of their specific acts ($P(R \mid \neg C) \gg P(R \mid C)$, but $A$ does not causally produce $R$).

Let utilities be:
- Bathsheba summoned, no revolt: $u(A, \neg R) = 10$
- Bathsheba summoned, revolt: $u(A, R) = -100$
- Abstain, no revolt: $u(\neg A, \neg R) = 0$
- Abstain, revolt: $u(\neg A, R) = -110$

Summoning Bathsheba is worth $+10$ utils regardless of whether a revolt occurs:
$$u(A, R) - u(\neg A, R) = 10, \quad u(A, \neg R) - u(\neg A, \neg R) = 10$$

```
       Charisma (C) [Common Cause]
       /          \
      v            v
Summon (A)      Revolt (R)
```

#### EDT Analysis
Because David does not know his charisma type, choosing $A$ provides strong evidence that he is uncharismatic ($\neg C$), which in turn provides strong evidence of an impending revolt ($R$):
$$P(R \mid A) = \sum_{c \in \{C, \neg C\}} P(R \mid c) P(c \mid A) \gg P(R \mid \neg A)$$

If $P(R \mid A) = 0.8$ and $P(R \mid \neg A) = 0.1$:
$$V_{\text{EDT}}(A) = 0.8(-100) + 0.2(10) = -80 + 2 = -78$$
$$V_{\text{EDT}}(\neg A) = 0.1(-110) + 0.9(0) = -11$$

EDT recommends **abstaining** ($V_{\text{EDT}}(\neg A) > V_{\text{EDT}}(A)$) to preserve the comforting belief that David is charismatic.

#### CDT Analysis
Under CDT, David holds fixed his credences in the dependency hypotheses. Since $A$ does not causally influence $C$ or $R$, the counterfactual probabilities decouple from the action:
$$P(A \to R) = P(\neg A \to R) = P(R \mid \text{do}(A)) = P(R)$$

Calculating causal expected utility:
$$U(A) = P(R)(-100) + (1 - P(R))(10) = 10 - 110\,P(R)$$
$$U(\neg A) = P(R)(-110) + (1 - P(R))(0) = -110\,P(R)$$

Subtracting yields:
$$U(A) - U(\neg A) = 10 > 0$$

CDT unambiguously prescribes **summoning Bathsheba**. Because his action cannot alter his charisma or causally trigger a revolt, David should not sacrifice a net gain of $10$ utils merely for self-flattering news.

---

### 3.2 Newcomb's Paradox

A reliable predictor presents an agent with two boxes:
- **Box 1 (transparent)**: contains $\$1,000$.
- **Box 2 (opaque)**: contains either $\$1,000,000$ or $\$0$.

The agent may choose:
- **One-box ($B_1$)**: Take only Box 2.
- **Two-box ($B_2$)**: Take both Box 1 and Box 2.

The predictor placed $\$1,000,000$ in Box 2 yesterday if and only if she predicted the agent would choose $B_1$. The prediction is accurate with probability $p = 0.99$.

Let $M$ denote the state where Box 2 contains $\$1,000,000$, and $\neg M$ denote the state where it contains $\$0$. Assume linear utility in cash.

```
       Predictor's Model (Past)
       /                      \
      v                        v
Box 2 Content (M)        Agent's Choice (B_1 or B_2)
```

#### EDT Recommendation
EDT computes conditional expectations:
$$V_{\text{EDT}}(B_1) = P(M \mid B_1) \cdot 10^6 + P(\neg M \mid B_1) \cdot 0 = 0.99 \times 10^6 = \$990,000$$
$$V_{\text{EDT}}(B_2) = P(M \mid B_2) \cdot (10^6 + 10^3) + P(\neg M \mid B_2) \cdot 10^3 = 0.01(1,001,000) + 0.99(1,000) = \$11,000$$

EDT firmly prescribes **one-boxing** ($B_1$).

#### CDT Recommendation
The dependency hypotheses correspond to the fixed contents of Box 2:
- $K_1$: Box 2 contains $\$1,000,000$ ($M$).
- $K_2$: Box 2 contains $\$0$ ($\neg M$).

Because the predictor made her deposit in the past, the agent's current choice has no backwards-causal effect on the presence of the money:
$$P(B_1 \to M) = P(B_2 \to M) = P(M)$$
$$P(B_1 \to \neg M) = P(B_2 \to \neg M) = 1 - P(M)$$

Evaluating the causal expected utility:
$$U(B_1) = P(M) \cdot 10^6 + (1 - P(M)) \cdot 0 = 10^6 P(M)$$
$$U(B_2) = P(M) \cdot (10^6 + 10^3) + (1 - P(M)) \cdot 10^3 = 10^6 P(M) + 1,000$$

Comparing the two:
$$U(B_2) - U(B_1) = \$1,000 > 0$$

Regardless of the value of $P(M)$, $B_2$ strictly dominates $B_1$ causally. The causal architecture implies that the money is already in the box or it isn't. Taking both boxes yields $\$1,000$ more in every causally possible state of affairs. CDT therefore dictates **two-boxing**.

---

### 3.3 The Adversarial Offer

Recent literature has highlighted setups where CDT's causal dominance reasoning leads to structural losses. Consider the **Adversarial Offer** (Oesterheld and Conitzer, 2021; Spencer, 2020):

- A seller offers two opaque boxes: Box Left ($L$) and Box Right ($R$).
- The buyer may purchase at most one box for $\$1$, or purchase neither ($N$) for $\$0$.
- Yesterday, the seller placed $\$3$ in each box she predicted the buyer would **not** acquire.
- Both the seller and buyer know the seller's predictions are accurate with probability $p = 0.75$.

The buyer evaluates three acts: $\mathcal{A} = \{L, R, N\}$.

Let the state space denote the seller's prediction: $\mathcal{S} = \{S_L, S_R, S_N\}$. 
The contents of the boxes under each state are:
- If $S_L$: $L$ has $\$0$, $R$ has $\$3$.
- If $S_R$: $L$ has $\$3$, $R$ has $\$0$.
- If $S_N$: $L$ has $\$3$, $R$ has $\$3$.

Notice that under every state $s \in \mathcal{S}$, at least one box contains $\$3$. Therefore, the total money contained across both boxes is always at least $\$3$, meaning the average content per box is at least $\$1.50$.

#### CDT Evaluation for the Buyer
Let $P(S_L) = q_L$, $P(S_R) = q_R$, $P(S_N) = q_N$.
Since the contents were fixed yesterday, the buyer's action cannot causally alter the presence of money:
$$U(L) = -1 + 3 \cdot P(\text{Box } L \text{ contains } \$3) = -1 + 3 \cdot \big(P(S_R) + P(S_N)\big) = -1 + 3(q_R + q_N)$$
$$U(R) = -1 + 3 \cdot P(\text{Box } R \text{ contains } \$3) = -1 + 3(q_L + q_N)$$
$$U(N) = 0$$

Summing the causal expected payoffs of buying either box:
$$U(L) + U(R) = -2 + 3(q_R + q_N + q_L + q_N) = -2 + 3(1 + q_N) = 1 + 3q_N$$

Since $q_N \ge 0$:
$$U(L) + U(R) \ge 1 > 0$$

Because the sum of $U(L)$ and $U(R)$ is strictly positive, it is mathematically impossible for both $U(L) \le 0$ and $U(R) \le 0$ to hold simultaneously. At least one box **must** have a causal expected utility greater than zero ($U(N) = 0$). 

Hence, CDT strictly forbids choosing $N$; the agent must buy one of the boxes.

Yet, when the buyer chooses a box (say, by symmetry, Box $L$), the seller has predicted this with $75\%$ accuracy ($P(S_L \mid L) = 0.75$). The buyer's realized expected payoff is:
$$\mathbb{E}[\text{Payoff} \mid L] = -1 + 3 \cdot P(S_R \text{ or } S_N \mid L) = -1 + 3(0.25) = -1 + 0.75 = -\$0.25$$

The CDT agent is locked into taking a bet that yields a net loss of $25$ cents in expectation, handing guaranteed long-run profit to the seller.

---

## 4. Theoretical Complications and Internal Tensions

While CDT resolves the "symptom-treating" pathologies of EDT, its insistence on uncoupling choice from predictive correlation generates deep structural dilemmas.

### 4.1 Andy Egan's Counterexamples and Instability

Andy Egan (2007) highlighted a class of decision problems where CDT's recommendations are unstable under deliberation.

#### The Psychopath Button
Paul deliberates over whether to press a button that kills all psychopaths ($B$).
- Living in a world without psychopaths is highly desirable ($+100$).
- Living with psychopaths is neutral ($0$).
- Dying is catastrophic ($-1,000$).
- Paul is confident that only a psychopath would press such a button: $P(\text{Paul is a psychopath} \mid B) \approx 1$, whereas $P(\text{Paul is a psychopath} \mid \neg B) \approx 0$.

```
           Paul's True Neural State
           /                      \
          v                        v
Press Button (B)             Die if Psychopath
```

Let $p$ be Paul's prior credence that he is a psychopath. Paul cannot causally change his genetic and neurological wiring by pressing the button.
The causal expected utility of pressing is:
$$U(B) = (1 - p)(100) + p(-1000) = 100 - 1100p$$
The causal utility of refraining is:
$$U(\neg B) = (1 - p)(0) + p(0) = 0$$

If Paul starts deliberation with a low credence that he is a psychopath (e.g., $p = 0.05$):
$$U(B) = 100 - 1100(0.05) = 100 - 55 = +45 > U(\neg B) = 0$$

CDT advises Paul to press the button. 

However, as Paul forms the intention to press $B$, that intention provides immediate evidence about his own nature, driving $p \to 1$. Once $p$ updates, $U(B)$ collapses to:
$$U(B) \approx 100 - 1100(1) = -1000 \ll 0$$
Now CDT commands him to abort. But once he resolves to abort ($\neg B$), his credence that he is a psychopath drops back toward zero, making the button attractive again.

CDT encounters a limit cycle: the act that maximizes causal expected utility changes the moment the agent deliberates toward performing it.

### 4.2 Joyce's Deliberational Dynamics and Ratifiability

To address this instability, causal decision theorists have proposed formal models of deliberation:

#### Ratifiability (Richard Jeffrey / William Harper)
An act $A$ is **ratifiable** if and only if $A$ maximizes causal expected utility relative to the probability distribution updated on the assumption that $A$ will be performed:

$$U(A \mid A) \ge U(A' \mid A) \quad \forall A' \in \mathcal{A}$$

In the Psychopath Button, pressing $B$ is not ratifiable: $U(B \mid B) \approx -1000$, whereas $U(\neg B \mid B) = 0$. However, refraining is ratifiable: $U(\neg B \mid \neg B) = 0 > U(B \mid \neg B) = 45$? Wait: if Paul knows he will not press, $U(B \mid \neg B) = 45 > 0$, so $\neg B$ is also unratifiable! In games like *Death in Damascus*, **no** pure action is ratifiable.

#### Joyce's Deliberational Dynamics
James Joyce (2012) defends CDT by modeling deliberation as a continuous-time dynamical system. The agent maintains a mixed deliberation vector $\mathbf{p}_t = (p_1, \dots, p_m)$, where $p_i = P(A_i)$ represents the agent's current propensity to choose act $A_i$. 

As propensities shift, the agent conditionalizes their background credences on these evolving propensities. The system follows a gradient process:

$$\frac{d p_i}{dt} = g_i\big(U(A_i; \mathbf{p}_t) - \bar{U}(\mathbf{p}_t)\big)$$

Under this defense, when pure acts lack equilibrium, the system converges to a mixed-strategy fixed point where the agent is indifferent between options. 

Critics counter that requiring an agent to deliberately randomize (or converge to indifference) in deterministic single-agent decision problems concedes the very point CDT set out to prove: that pure causal dominance should govern rational choice.

---

### 4.3 Diachronic Dutch Books and Money Pumps

A consequential theoretical challenge to CDT is its vulnerability to diachronic Dutch books (Oesterheld and Conitzer, 2021). 

Because a CDT agent refuses to let their current act be constrained by correlations with past predictions, an adversary who can predict the agent's behavior can offer a series of sequential bets. At each isolated stage, the CDT agent selects the option with the highest causal expected utility, yet the end-to-end sequence results in a sure financial loss relative to alternative behavioral policies.

In the Adversarial Offer discussed above:
1. The predictor anticipates the CDT agent's choice and leaves Box $L$ empty.
2. The CDT agent reasons that the contents are physically fixed and that buying Box $L$ has positive causal expectation relative to their prior.
3. The transaction executes, and the agent loses $\$0.25$ in expectation per round.

Evidential decision theorists argue that an agent who consistently finishes poorer than an EDT agent across predictive scenarios cannot lay claim to a superior standard of practical rationality. Causal decision theorists counter that this disparity is simply an artifact of an unfavorable environment: the predictor rewards agents who *harbor irrational dispositions*, making it an unfair indictment of rationality itself.

---

## 5. Comparative Mathematical Summary

The operational architectures of the leading decision frameworks can be contrasted directly:

| Property | Evidential Decision Theory (EDT) | Causal Decision Theory (Gibbard–Harper / Lewis) | Causal Decision Theory (SCM / Pearl) |
| :--- | :--- | :--- | :--- |
| **Mathematical Criterion** | $\max_A \sum_j P(O_j \mid A) u(O_j)$ | $\max_A \sum_K P(K) u(f_K(A))$ | $\max_A \mathbb{E}[u(Y) \mid \text{do}(X = A)]$ |
| **Probability Shift Under Action** | Bayesian Conditionalization $P(\cdot \mid A)$ | Counterfactual Imaging $P_A(\cdot)$ | Graph Mutilation / Interventional Distribution |
| **Treatment of Common Causes** | Conflates correlation with efficacy | Adjusts for dependency hypotheses | Blocks non-causal paths via back-door criterion |
| **Newcomb's Problem** | One-box ($\$1,000,000$) | Two-box ($\$1,001,000$ counterfactually) | Two-box (intervenes on choice node) |
| **Vulnerabilities** | Delusional behavior (managing signs) | Instability (Egan cases), Adversarial exploitation | Requires explicit graphical / structural model |

---

## 6. Practical Decision Procedure for Unfamiliar Cases

To apply Causal Decision Theory systematically to any unfamiliar decision problem, use the following operational protocol:

1. **Map the Causal Graph**: Explicitly identify variables and direct causal influences. Distinguish between:
   - What the action $A$ physically affects downstream.
   - What causes or correlates with $A$ via upstream common causes or past predictions.
2. **Partition into Dependency Hypotheses**: Identify the set of maximally specific background states $\mathcal{K}$ that determine how outcomes respond to actions. Verify that for every $K \in \mathcal{K}$, the choice of act $A$ has no physical power to alter $K$.
3. **Assign Unconditional Credences**: Evaluate $P(K)$ *before* conditioning on the choice of $A$. Do not allow the evidential news of taking $A$ to alter the distribution over $K$.
4. **Compute Causal Expected Utility**: For each act $A$, evaluate:
   $$U(A) = \sum_{K \in \mathcal{K}} P(K) \, u\big(A, K\big)$$
   *(Equivalently: calculate $\sum_y P(y \mid \text{do}(A)) u(y)$ by adjusting for back-door paths).*
5. **Check for Deliberational Stability**: Verify whether updating credences on the tentative choice of $A$ reverses the preference ordering. If instability emerges, compute the mixed-strategy equilibrium over acts.

---

## 7. Conclusion

Causal Decision Theory provides an intuitive correction to the news-value maximization of Evidential Decision Theory. By grounding rational agency in counterfactual conditionals, dependency hypotheses, and physical interventions, CDT ensures that rational agents pursue outcomes they can actually bring about, rather than settling for actions that merely supply reassuring signs.

Yet, this adherence to causal autonomy comes at a well-documented cost. In environments where accurate predictors anticipate agent behavior, or where deliberation provides feedback about an agent's own fixed nature, CDT faces persistent challenges: deliberational instability, money pumps, and lower cumulative payoffs than evidential competitors. 

Whether these properties represent genuine failures of rationality or simply the inevitable tax that hostile environments impose on causally coherent actors remains one of the central debates in formal philosophy and decision sciences.

---

### References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Egan, A. (2007). Some counterexamples to causal decision theory. *The Philosophical Review*, 116(1), 93–114.
- Gibbard, A., & Harper, W. L. (1981). Counterfactuals and two kinds of expected utility. In *Ifs: Conditionals, Beliefs, Decision, Chance, and Time* (pp. 153–190). Springer.
- Joyce, J. M. (2012). Regret and instability in causal decision theory. *Synthese*, 187(1), 123–145.
- Lewis, D. (1976). Probabilities of conditionals and conditional probabilities. *The Philosophical Review*, 85(3), 297–315.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
- Oesterheld, C., & Conitzer, V. (2021). Extracting money from causal decision theorists. *The Philosophical Quarterly*, 71(4).
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.
- Spencer, J. (2020). An argument against causal decision theory. *Analysis*, 81(1), 52–61.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/b77da651-9afa-4916-aba9-061d6ca174b2/call_0/request.json)

[Authoritative raw response](../../../../../../runs/b77da651-9afa-4916-aba9-061d6ca174b2/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Dilemma**

I've framed the scenario as a Prisoner's Dilemma, focusing on the character's utility, which is directly tied to years of imprisonment, as defined by the prompt. I'm adopting Causal Decision Theory (CDT) principles, as outlined, to evaluate potential actions and their causal consequences, specifically concerning the U value.


```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/b77da651-9afa-4916-aba9-061d6ca174b2/call_1/request.json)

[Authoritative raw response](../../../../../../runs/b77da651-9afa-4916-aba9-061d6ca174b2/call_1/response.raw) · finish: `stop`

### Visible response

````text
```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing Sasha's Dilemma**

I'm focusing on the core challenge: selecting Sasha's best action within a Causal Decision Theory framework, given a Prisoner's Dilemma scenario. I am also making sure I am aware that the game is between two identical LLM instances. This is a crucial detail for determining an optimal strategy under the given conditions.


**Refining Payoff Analysis**

I've carefully calculated the payoffs, factoring in the utility function of minimizing prison time. The breakdown is clear: both quiet equals two years, Sasha sends while Rowan keeps quiet means freedom for Sasha, Sasha keeps quiet and Rowan sends means five years for Sasha, and both send results in four years for Sasha. My strategy now hinges on applying CDT principles, specifically addressing the causal independence of our actions, even as twin LLM instances.


```
