# 004_cdt_wikipedia_google_gemini-3.8-flash_rlow_plow / 00003

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/38033af8-92bf-4914-a032-d83011aae3ad/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/38033af8-92bf-4914-a032-d83011aae3ad/call_0/response.raw) · finish: `stop`

### Visible response

````text
# Causality, Counterfactuals, and Choice: A Formal Exploration of Causal Decision Theory

## 1. Introduction: The Need for Causal Deliberation

Standard Bayesian decision theory, tracing back to Frank Ramsey, Leonard Savage, and Richard Jeffrey, provides a powerful apparatus for evaluating decisions under uncertainty: an agent should select an act that maximizes expected utility. Yet, an foundational ambiguity lurks inside the notion of "expectation." When calculating expected utility, should our subjective probabilities reflect what an act *indicates* about the world, or what it *causes*?

Consider a classic medical vignette: suppose smoking does not cause lung cancer, but a latent genetic lesion simultaneously causes both a strong craving to smoke and the development of lung cancer. In this scenario, an individual choosing to smoke receives terrible "news"—namely, that they likely possess the fatal gene. If the individual computes expected utility using standard conditional probabilities, the act of smoking appears disastrous because $P(\text{Cancer} \mid \text{Smoke}) \gg P(\text{Cancer} \mid \neg\text{Smoke})$. This is the doctrine of **Evidential Decision Theory** (EDT): evaluate an action by the news value of having performed it.

Yet common sense rebels against this reasoning. The damage, if any, is already settled in the genome; lighting a cigarette does not causally alter whether the lesion exists. Abstaining from a cigarette to avoid cancer is an exercise in magical thinking—acting as though manipulating a symptom can retroactively sever the underlying cause. 

**Causal Decision Theory** (CDT) arose precisely to insulate rational choice from such confounding correlations. CDT asserts that an action should be evaluated strictly according to its *causal efficacy*—its genuine power to bring about desirable states of the world. While philosophically intuitive, formalizing CDT requires grappling with non-trivial mathematical machinery, including counterfactual logics, imaging over probability distributions, and the mechanics of causal graphs. Moreover, the theory encounters profound technical and philosophical challenges when confronted with asymmetric predictors, unstable deliberations, and game-theoretic interaction.

This essay develops the formal architecture of CDT, traces how it resolves classic dilemmas, diagnoses its core open foundational problems, and provides an operational synthesis suitable for evaluating novel decision scenarios.

---

## 2. Formal Formulations of Causal Expected Utility

To transform the informal maxim—"choose the act with the best expected causal consequences"—into a rigorous normative theory, several mathematical frameworks have been proposed. We examine the three most prominent: Gibbard and Harper's counterfactual formulation, Lewis's imaging and dependency hypotheses, and the modern structural causal model (do-calculus) framework.

### 2.1 The Gibbard–Harper Counterfactual Formulation

Allan Gibbard and William Harper (1981) formulated CDT using counterfactual conditionals. Let $\mathcal{A} = \{A_1, A_2, \dots, A_m\}$ be a mutually exclusive and exhaustive set of available acts, and let $\mathcal{O} = \{O_1, O_2, \dots, O_n\}$ be a partition of possible outcomes. Each outcome $O_j$ is assigned a desirability or utility $D(O_j) \in \mathbb{R}$.

Gibbard and Harper define the causal expected utility $U(A)$ of an act $A \in \mathcal{A}$ as:
$$U(A) = \sum_{j=1}^n P(A \mathbin{\Box\to} O_j) \, D(O_j)$$
where $A \mathbin{\Box\to} O_j$ denotes the counterfactual proposition: *"If the agent were to do $A$, then $O_j$ would obtain."*

In contrast, Jeffrey's evidential expected utility (the hallmark of EDT), often written $V(A)$, is defined by:
$$V(A) = \sum_{j=1}^n P(O_j \mid A) \, D(O_j)$$

The critical divergence between CDT and EDT reduces to the difference between the counterfactual probability $P(A \mathbin{\Box\to} O_j)$ and the epistemic conditional probability $P(O_j \mid A)$.

#### The Failure of the Conditional Probability Hypothesis
It is tempting to suppose that counterfactual probabilities might simply reduce to conditional probabilities, i.e., $P(A \mathbin{\Box\to} B) \stackrel{?}{=} P(B \mid A)$. However, David Lewis's (1976) celebrated triviality result demonstrated that there is no non-trivial conditional connective $\to$ such that $P(A \to B) = P(B \mid A)$ for all propositions $A, B$ and probability functions $P$ closed under conditionalization. Specifically, any probability space satisfying such an identity can assign non-zero probability to at most two mutually incompatible propositions.

Gibbard and Harper demonstrated that $P(A \mathbin{\Box\to} O_j) = P(O_j \mid A)$ holds if the act $A$ is statistically independent of the counterfactual conditional itself:
$$P(A \mathbin{\Box\to} O_j \mid A) = P(A \mathbin{\Box\to} O_j)$$
Whenever an act correlates with pre-existing states of affairs that determine the outcome independently of the act—as in the common-cause gene hypothesis—this independence fails, driving a wedge between $U(A)$ and $V(A)$.

### 2.2 Lewis's Dependency Hypotheses and Imaging

David Lewis (1981) provided an alternative, semantically grounded formulation using **dependency hypotheses**. A dependency hypothesis $K$ is a maximally specific proposition describing how the world causally depends on the agent's actions. Formally, let $\mathcal{K} = \{K_1, K_2, \dots, K_k\}$ be the set of mutually exclusive and exhaustive dependency hypotheses. Each $K \in \mathcal{K}$ specifies, for every act $A \in \mathcal{A}$, the exact outcome $O$ that would result if $A$ were chosen:
$$K \implies (A \mathbin{\Box\to} O)$$

Because the causal mechanisms of the universe outside the agent's immediate physical control are causally independent of the agent's current choice, Lewis argues that the agent's rational credence in a dependency hypothesis $K$ must remain held fixed. The causal expected utility is thus:
$$U(A) = \sum_{K \in \mathcal{K}} P(K) \sum_{j=1}^n P(O_j \mid A \land K) \, D(O_j)$$
Since $K$ completely determines which outcome follows from $A$, $P(O_j \mid A \land K)$ is either $1$ or $0$. Letting $O(A, K)$ denote the unique outcome dictated by $K$ under act $A$, the equation simplifies to:
$$U(A) = \sum_{K \in \mathcal{K}} P(K) \, D(O(A, K))$$

Notice the crucial structural feature: the expectation weights outcomes by the unconditional prior credence $P(K)$, **not** the conditional credence $P(K \mid A)$.

#### Imaging
Lewis gave this a geometric semantics over possible worlds. Let $W$ be a set of possible worlds, and suppose that for each world $w$ and act $A$, there exists a unique "closest" or "most similar" world $w_A$ in which $A$ is true (incorporating the Principle of Conditional Excluded Middle). The counterfactual probability is defined via *imaging*: the probability mass $P(w)$ of each world $w$ is shifted entirely to its nearest $A$-counterpart $w_A$:
$$P_A(w') = \sum_{w : w_A = w'} P(w)$$
The causal utility is then the expectation under this imaged distribution:
$$U(A) = \sum_{w' \in W} P_A(w') \, D(w')$$

### 2.3 Operationalization via Causal Graphical Models (Structural Causal Models)
*Note on methodology:* The reference text notes that CDT does not natively provide an algorithm for computing counterfactual probabilities and flags Lewisian imaging as vulnerable to regress. To make CDT fully operational and applicable to novel decision problems, we introduce the modern framework of Structural Causal Models (SCMs) developed by Judea Pearl (2000). While this represents a modern mathematical enrichment beyond Gibbard and Harper's 1981 paper, it is mathematically compatible with Lewis's dependency hypotheses and resolves the computational ambiguity.

An SCM is a quadruple $M = \langle U, V, F, P(U) \rangle$:
1. $U$ is a set of background, exogenous variables determined by factors outside the model, distributed according to $P(U)$.
2. $V$ is a set of endogenous variables.
3. $F = \{f_Y : Y \in V\}$ is a set of deterministic structural equations such that each $Y \in V$ is given by $Y = f_Y(\text{PA}_Y, U_Y)$, where $\text{PA}_Y \subseteq V \setminus \{Y\}$ are the endogenous parents of $Y$, and $U_Y \subseteq U$.

An act corresponds to an external intervention, denoted by Pearl's **$\text{do}$-operator**, $\text{do}(A = a)$. Mechanistically, $\text{do}(A = a)$ replaces the structural equation $f_A$ for $A$ with the constant assignment $A = a$, severing all incoming directed edges to $A$ in the associated causal Directed Acyclic Graph (DAG) while leaving all other structural equations unaltered.

Under this operationalization, the causal expected utility is:
$$U_{\text{SCM}}(a) = \mathbb{E}[D \mid \text{do}(A = a)] = \sum_{y} D(y) \, P(y \mid \text{do}(A = a))$$

The exogenous state $u \in \mathcal{U}$ corresponds directly to Lewis's dependency hypothesis $K$: fixing $u$ fully specifies the causal response of the system to any intervention $\text{do}(A=a)$. The distribution $P(u)$ remains unperturbed by the intervention, precisely mirroring Lewis's mandate to hold fixed the agent's unconditional credences in causal mechanisms.

---

## 3. Deciding Paradigmatic Problems

To observe how these mathematical definitions dictate concrete decisions, we analyze three canonical cases: King David, Newcomb's Paradox, and the Adversarial Offer.

### 3.1 Common Cause Confounding: King David and Bathsheba

In Gibbard and Harper’s example, King David considers whether to send for Bathsheba ($A$) or abstain ($\neg A$). The outcome space consists of two dimensions: obtaining Bathsheba ($B$ vs. $\neg B$) and facing a successful revolt ($R$ vs. $\neg R$).

Political science teaches David that a king is either charismatic ($C$) or uncharismatic ($\neg C$). Charisma is fixed at childhood. Uncharismatic kings have a sneaky, ignoble bearing which causes revolts; charisma causes loyalty. Unjust acts (like summoning another man's wife) do not cause revolts, but uncharismatic kings frequently commit unjust acts, whereas charismatic kings rarely do.

We set the utilities reflecting David’s desires:
- $D(B \land \neg R) = 100$ (Bathsheba, no revolt)
- $D(\neg B \land \neg R) = 50$ (No Bathsheba, no revolt)
- $D(B \land R) = -100$ (Bathsheba, revolt)
- $D(\neg B \land R) = -150$ (No Bathsheba, revolt)

Sending for Bathsheba provides $+50$ utility across both political states. However, David knows that:
$$P(C \mid A) \ll P(C \mid \neg A) \implies P(R \mid A) \gg P(R \mid \neg A)$$

#### EDT Calculation
Under EDT, the act $A$ carries terrible news about David's charisma:
$$V(A) = P(R \mid A) \mathbb{E}[D \mid A, R] + P(\neg R \mid A) \mathbb{E}[D \mid A, \neg R]$$
$$V(\neg A) = P(R \mid \neg A) \mathbb{E}[D \mid \neg A, R] + P(\neg R \mid \neg A) \mathbb{E}[D \mid \neg A, \neg R]$$
If $P(R \mid A) = 0.9$ and $P(R \mid \neg A) = 0.1$:
$$V(A) = 0.9(-100) + 0.1(100) = -90 + 10 = -80$$
$$V(\neg A) = 0.1(-150) + 0.9(50) = -15 + 45 = +30$$
EDT unequivocally advises David to abstain ($V(\neg A) > V(A)$).

#### CDT Calculation
CDT identifies the dependency hypotheses $\mathcal{K} = \{K_C, K_{\neg C}\}$, where $K_C$ denotes the state where David is charismatic (revolt will not occur regardless of action) and $K_{\neg C}$ denotes the state where David is uncharismatic (revolt will occur regardless of action). Crucially:
$$A \mathbin{\Box\to} R \iff K_{\neg C}$$
$$P(A \mathbin{\Box\to} R) = P(K_{\neg C}) = P(\neg C)$$
The counterfactual probabilities are completely decoupled from the act:
$$U(A) = P(C) [100] + P(\neg C) [-100]$$
$$U(\neg A) = P(C) [50] + P(\neg C) [-150]$$
Computing the difference:
$$U(A) - U(\neg A) = P(C)[100 - 50] + P(\neg C)[-100 - (-150)] = 50 P(C) + 50 P(\neg C) = 50 > 0$$

CDT dictates that David send for Bathsheba. Because his act cannot retroactively alter his charisma, abstaining would be a pointless sacrifice.

```
       [Charisma (C)] (Confounder / Latent)
         /        \
        v          v
   Act: Send (A)   Revolt (R)
```
In Pearl's graph, the edge $C \to A$ is cut under $\text{do}(A)$. $P(R \mid \text{do}(A)) = P(R)$, rendering the expected causal gain strictly equal to the marginal utility of Bathsheba (+50).

---

### 3.2 Newcomb’s Paradox

In Newcomb's problem, an agent faces two boxes:
- Box 1: Transparent, contains $\$1,000$.
- Box 2: Opaque, contains either $\$1,000,000$ or $\$0$.

The agent can choose either Box 2 only (Action $A_1$, "one-boxing") or both Box 1 and Box 2 (Action $A_2$, "two-boxing"). A predictor with predictive accuracy $p = 0.99$ placed $\$1,000,000$ in Box 2 yesterday if and only if it predicted the agent would choose $A_1$.

Let $S_1$ be the state where Box 2 contains $\$1,000,000$, and $S_0$ where Box 2 contains $\$0$. The payoff matrix is:

| State / Act | $A_1$ (One-Box) | $A_2$ (Two-Box) |
| :--- | :--- | :--- |
| **$S_1$** ($\$1\text{M}$ in Box 2) | $\$1,000,000$ | $\$1,001,000$ |
| **$S_0$** ($\$0$ in Box 2) | $\$0$ | $\$1,000$ |

#### The EDT Analysis
EDT conditions directly on the choices:
$$P(S_1 \mid A_1) = 0.99, \quad P(S_0 \mid A_1) = 0.01$$
$$P(S_1 \mid A_2) = 0.01, \quad P(S_0 \mid A_2) = 0.99$$
Assuming linear utility for money ($D(x) = x$):
$$V(A_1) = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000$$
$$V(A_2) = 0.01(\$1,001,000) + 0.99(\$1,000) = \$10,010 + \$990 = \$11,000$$
EDT recommends one-boxing: $V(A_1) \gg V(A_2)$.

#### The CDT Analysis
Under CDT, the contents of Box 2 are temporally and causally fixed prior to the agent's decision. The dependency hypotheses are precisely $\mathcal{K} = \{S_1, S_0\}$. The act chosen right now exerts zero backward causal influence on what the predictor did yesterday:
$$P(A_1 \mathbin{\Box\to} S_1) = P(A_2 \mathbin{\Box\to} S_1) = P(S_1)$$
Let $q = P(S_1)$ be the agent's prior credence that Box 2 is full. Then:
$$U(A_1) = q(\$1,000,000) + (1-q)(\$0) = 1,000,000 q$$
$$U(A_2) = q(\$1,001,000) + (1-q)(\$1,000) = 1,000,000 q + 1,000$$

For any prior credence $q \in [0, 1]$:
$$U(A_2) - U(A_1) = 1,000 > 0$$

$A_2$ strictly causally dominates $A_1$. CDT commands the agent to take both boxes. The causal decision theorist accepts that one-boxers end up millionaires while two-boxers end up with a mere thousand dollars, but insists that this is a misfortune of predictive selection, not an indictment of rationality. As Lewis famously quipped, Newcomb's problem is a trap set to reward irrationality.

---

### 3.3 The Adversarial Offer and Frustration of Dominance

While Newcomb's paradox divides philosophers, more modern counterexamples demonstrate scenarios where CDT's indifference to evidential correlations causes systematic financial loss. 

In the **Adversarial Offer** (Oesterheld and Conitzer, 2021; Spencer, 2020), an agent is offered the opportunity to buy either Box 1, Box 2, or neither ($A_0$). The agent cannot buy both. Each box costs $\$1$. Yesterday, an accurate predictor ($p = 0.75$) placed $\$3$ in each box that she predicted the agent would *not* acquire.

Let $B_1$ and $B_2$ denote the actions of purchasing Box 1 and Box 2, respectively. The states correspond to the predictor's past actions:
- $S_{12}$: Predictor thought agent picks $A_0 \implies$ both boxes have $\$3$.
- $S_1$: Predictor thought agent picks $B_2 \implies$ Box 1 has $\$3$, Box 2 has $\$0$.
- $S_2$: Predictor thought agent picks $B_1 \implies$ Box 1 has $\$0$, Box 2 has $\$3$.
- $S_0$: Predictor thought agent picks a box $\implies$ both boxes empty (if predictor predicted either $B_1$ or $B_2$ specifically, the unchosen box might have money, but suppose symmetrical setup).

Consider the causal evaluation. Let the agent's credences in the money being in Box 1 and Box 2 be $q_1$ and $q_2$. Since the predictor can predict at most one box that the agent will take, the predictor must have left $\$3$ in *at least one* box (unless she predicted the agent would somehow take both, which is forbidden).

Because the physical placement of money is already complete:
$$U(B_1) = 3 q_1 - 1$$
$$U(B_2) = 3 q_2 - 1$$
$$U(A_0) = 0$$

Because the boxes were filled symmetrically and the predictor predicted the agent would not buy both, the sum of money in the boxes is at least $\$3$. Thus, $q_1 + q_2 \ge 1$, which implies:
$$\frac{U(B_1) + U(B_2)}{2} = \frac{3(q_1 + q_2) - 2}{2} \ge \frac{3(1) - 2}{2} = \$0.50 > 0$$
Hence, at least one box must have a causal expected utility strictly greater than $\$0$. 

CDT obligates the agent to buy a box. However, because the seller's prediction is accurate ($p = 0.75$), whenever the agent buys Box 1, Box 1 is empty with probability $0.75$; the expected monetary return conditional on buying is:
$$0.25(\$3) - \$1 = -\$0.25$$
The seller systematically extracts money from the CDT agent. A Dutch book is constructed: CDT incurs a certain, predictable loss simply because it refuses to allow its current deliberation to inform its beliefs about the background state.

---

## 4. Fundamental Theoretical Challenges

The behavior of CDT in the Adversarial Offer points to deep structural tensions within the theory. We must examine three core theoretical difficulties: semantic underspecification, deliberation instability, and vulnerability to diachronic Dutch books.

### 4.1 The Problem of Vagueness and Semantic Underspecification
As Shaffer (2009) highlights, classical CDT as formulated by Gibbard and Harper is fundamentally incomplete: it takes counterfactuals as primitive but provides no algorithmic rule for determining $P(A \mathbin{\Box\to} O)$ in non-trivial environments. 

Lewis proposed calculating counterfactuals by "imaging" over possible worlds using a similarity metric. But what constitutes the "closest" possible world?
1. Does world closeness preserve past history strictly up to the moment of choice (deterministic miracles)?
2. Does it preserve physical laws at the expense of past facts (backtracking counterfactuals)?

If we use non-backtracking counterfactuals (standard in CDT), an agent holds fixed everything in the past. But this relies on an external, informal carving of variables into "causally downstream" vs. "causally independent." If an agent assigns credences to different possible causal laws, Lewisian imaging requires evaluating counterfactuals conditional on counterfactuals, threatening an infinite regress:
$$P(A \mathbin{\Box\to} O) = \sum_{w} P(w) \, P(w_A \models O \mid w)$$
Without a deterministic, objective SCM provided *a priori*, the agent cannot compute the causal expected utility.

### 4.2 Deliberational Instability: Death in Damascus and the Psychopath Button
Perhaps the most damaging conceptual challenge to CDT is the phenomenon of **deliberational instability**, introduced in its modern form by Andy Egan (2007).

#### The Psychopath Button
Paul faces a button that will instantaneously and painlessly destroy all psychopaths on Earth. Paul strongly desires to live in a world without psychopaths ($+100$), but desires even more strongly to stay alive ($D(\text{Death}) = -1,000$). Paul currently believes he is an ordinary, empathetic human. However, psychiatric evidence indicates that *only a psychopath would ever press such a button*. 

Let $A$ be pressing the button, and $\Psi$ be the proposition that Paul is a psychopath.
If Paul does not press the button, he lives in a world with psychopaths: $U(\neg A) = 0$.

If Paul presses the button, what happens causally? Pressing the button does not *make* Paul a psychopath; psychopathy is a neurodevelopmental condition. Thus:
$$A \mathbin{\Box\to} \text{Paul dies} \iff \Psi$$
If Paul currently believes $P(\Psi) \approx 0$, then:
$$U(A) = P(\Psi)(-1,000) + (1 - P(\Psi))(100) \approx 100 > 0$$
CDT directs Paul to press the button!

However, observe what happens during deliberation. As Paul forms the intention to press the button, that very deliberation constitutes overwhelming evidence that he is, in fact, a psychopath ($P(\Psi \mid \text{deliberating to press}) \to 1$). If $P(\Psi) = 1$, then:
$$U(A) = 1(-1,000) + 0(100) = -1,000 \ll 0$$
Now CDT directs him to abort! But as soon as he decides to abort, his evidence that he is a psychopath vanishes, making pressing appear optimal once again.

#### Death in Damascus
The classic instantiation of this instability is **Death in Damascus**. Death informs you in Damascus that she has an appointment with you tomorrow. You have two choices: stay in Damascus ($D$) or flee to Aleppo ($A$). Death is an infallible predictor:
- If she predicted you stay in Damascus, she waits in Damascus.
- If she predicted you go to Aleppo, she waits in Aleppo.

Wherever you go, if Death is there, you die ($U = -100$); if she is not, you live ($U = 0$).
Suppose you currently lean toward staying in Damascus ($P(\text{Death in } D) > 0.5$). Then causally, fleeing to Aleppo has higher utility, since your flight will not alter where Death is already standing. 
$$U(A) > U(D)$$
Yet as soon as you choose to flee to Aleppo, you realize Death predicted this, meaning Death is waiting in Aleppo. Thus:
$$U(D) > U(A)$$
The decision exhibits no stable pure-strategy equilibrium.

### 4.3 Diachronic Dutch Books
Caspar Oesterheld and Vincent Conitzer (2021) demonstrated that the combination of CDT's recommendations and temporal dynamically inconsistent beliefs exposes causal decision theorists to **diachronic Dutch books**—systems of bets accepted over time that guarantee a net financial loss regardless of how the world turns out.

Because a CDT agent's preferences over actions flip as their evidence changes during deliberation, a clever bookie can:
1. Sell the agent a contract contingent on their future choice.
2. Allow the agent to deliberate, knowing the shift in intention will flip the agent's evaluation.
3. Buy back the contract (or sell an offsetting bet) at a price guaranteed to extract a positive surplus.

Traditional subjective expected utility theory guarantees immunity to Dutch books via the coherence theorems of Ramsey and de Finetti. CDT's departure from conditional probability breaks this mathematical coherence.

---

## 5. Reconstructing CDT: An Operational Synthesis

Where does this leave the practitioner or formal theorist seeking a rigorous, actionable decision procedure? The literature contains two primary rescue strategies: **ratifiability** and **causal dynamical deliberation**. Here, we develop an operational synthesis that resolves ambiguity and reconciles CDT with deliberational dynamics.

### 5.1 Ratifiability (Richard Jeffrey and Jim Joyce)
Richard Jeffrey proposed that a rational agent should only execute **ratifiable** decisions. 

> **Definition (Ratifiability):** An act $A \in \mathcal{A}$ is ratifiable if and only if:
> $$U(A \mid A) \ge U(A' \mid A) \quad \forall A' \in \mathcal{A}$$
> where $U(X \mid A)$ denotes the causal expected utility of act $X$ calculated using credences conditionalized on the assumption that the agent will ultimately perform $A$:
> $$U(X \mid A) = \sum_{K \in \mathcal{K}} P(K \mid A) \sum_{j} P(O_j \mid X \land K) \, D(O_j)$$

Let us test the Psychopath Button under ratifiability:
- $U(A \mid A)$: Conditional on pressing, Paul learns he is a psychopath ($P(\Psi \mid A) \approx 1$). Thus $U(A \mid A) \approx -1,000$.
- $U(\neg A \mid A)$: Conditional on pressing, what would be the causal utility of not pressing? Paul would live, but the psychopaths would also live. $U(\neg A \mid A) = 0$.
- Since $U(A \mid A) < U(\neg A \mid A)$, pressing the button is **unratifiable**.
- Conversely, for refraining: $U(\neg A \mid \neg A) = 0$, while $U(A \mid \neg A) = 100$. Refraining is also unratifiable in pure strategies.

This reveals the primary weakness of pure ratifiability: in scenarios like Death in Damascus or the Psychopath Button, **no pure act is ratifiable**.

### 5.2 Deliberational Dynamics and Mixed Strategies
*Operational Proposal (Synthesizing Joyce, 2012; Skyrms, 1990):* To make CDT complete, an agent must be permitted to deliberate over mixed strategies (probabilistic intentions), treating their own evolving propensity to act as an endogenous state variable.

Let $p_t \in \Delta(\mathcal{A})$ denote the agent's mixed policy at deliberational stage $t \in [0, 1]$, where $p_t(A)$ is the subjective probability that the agent will choose act $A$.
During deliberation, the agent treats $p_t$ as an evidential signal. The agent updates their credences in the dependency hypotheses $K \in \mathcal{K}$ via continuous conditionalization on their own deliberative state:
$$P_t(K) = P(K \mid p_t)$$

At any instantaneous state $p_t$, the causal expected utility of each pure act $A$ is:
$$U_t(A) = \sum_{K \in \mathcal{K}} P(K \mid p_t) \, D(O(A, K))$$

The agent's intentions evolve according to a continuous adjustment gradient (such as the replicator dynamic or standard gradient ascent). A simple and natural operationalization is:
$$\frac{d}{dt} p_t(A) = p_t(A) \left[ U_t(A) - \sum_{A'} p_t(A') U_t(A') \right]$$

A rational choice is defined as a fixed point $p^*$ of this dynamical system where:
1. $\frac{d}{dt} p_t = 0$.
2. The state is an attractor (deliberationally stable).

#### Application to Death in Damascus
In Death in Damascus, let $p$ be the probability of going to Aleppo ($A$), and $1-p$ the probability of staying in Damascus ($D$).
Death predicts using accuracy 1.0 (or $r$). Thus:
$$P(\text{Death in } A \mid p) = p$$
$$P(\text{Death in } D \mid p) = 1 - p$$

The causal utilities at state $p$ are:
$$U_t(A) = P(\text{Death in } A \mid p)(-100) + P(\text{Death in } D \mid p)(0) = -100 p$$
$$U_t(D) = P(\text{Death in } D \mid p)(-100) + P(\text{Death in } A \mid p)(0) = -100 (1 - p)$$

Equating the causal utilities:
$$-100 p = -100(1 - p) \implies p^* = 0.5$$

At $p^* = 0.5$, both acts possess identical causal expected utility ($-50$). The deliberative dynamic reaches a stable equilibrium. The agent flips an unbiased coin, achieving the unique ratifiable mixed policy. 

Under this dynamic extension, CDT does not freeze or oscillate uncontrollably; it converges to the game-theoretic minimax strategy against the predictor.

---

## 6. A Step-by-Step CDT Decision Protocol for Unfamiliar Cases

To enable a reader or algorithmic agent to decide novel problems under CDT, we summarize the theory into an operational four-step protocol:

```
[ Step 1: Formalize Action and Outcome Spaces ]
  Define acts A = {A1, ..., Am}
  Define outcomes O = {O1, ..., On} with utilities D(O)

[ Step 2: Construct the Structural Causal Model (SCM) ]
  Identify exogenous variables U ~ P(U)
  Identify endogenous variables V (including Act A and Outcome O)
  Specify structural functions V_i = f_i(PA_i, U_i)
  Verify that the act represents an intervention do(A = a)

[ Step 3: Check for Deliberational Feedback ]
  Determine if the agent's tentative choice provides evidence about U
  - NO FEEDBACK: Standard Static CDT applies
    Compute: U(A) = sum_u P(u) * D(O(A, u))
    Select A* = argmax U(A)
  - FEEDBACK PRESENT: Dynamic CDT applies
    Proceed to Step 4

[ Step 4: Solve for Deliberative Equilibrium (Ratifiable Policy) ]
  Define mixed policy p in Delta(A)
  Compute P(U | p) as a function of propensity p
  Set up causal utilities: U(A_i | p) = sum_u P(u | p) * D(O(A_i, u))
  Find fixed point p* such that no pure act in the support of p* 
  yields lower causal utility than any alternative available act:
  For all A_i with p*(A_i) > 0: U(A_i | p*) = max_j U(A_j | p*)
  Execute the policy sampled from p*
```

---

## 7. Comparative Analytical Summary

| Feature / Scenario | Evidential Decision Theory (EDT) | Classical Causal Decision Theory (Gibbard–Harper / Lewis) | Dynamically Ratified CDT (Joyce / SCM Extension) |
| :--- | :--- | :--- | :--- |
| **Foundational Metric** | Conditional probability: $P(O \mid A)$ | Counterfactual probability: $P(A \mathbin{\Box\to} O)$ or prior over dependency hypotheses $P(K)$ | Counterfactual probability evaluated at deliberative equilibrium: $P(A \mathbin{\Box\to} O \mid p^*)$ |
| **Newcomb’s Paradox** | **One-box**: $A_1$ indicates $\$1\text{M}$ | **Two-box**: Dominance dictates $A_2$; cannot cause Box 2 to fill | **Two-box**: Dominance holds throughout deliberation |
| **Smoking Lesion / King David** | **Abstain**: Taking action indicates dangerous underlying state | **Indulge / Send**: Action cannot causally alter the genetic/historical state | **Indulge / Send**: Confirms action cannot causally alter the state |
| **Psychopath Button** | **Do not press**: Pressing proves one is a psychopath | **Press**: Evaluated at prior belief; failure to anticipate self-evidence | **Do not press**: Pressing is unratifiable; dynamic convergence to $p(\text{Press}) = 0$ |
| **Death in Damascus** | Selects city arbitrarily or indecisive depending on variant | **Unstable**: Cycles endlessly in pure strategies | **Mixed Strategy**: Converges to $p^* = 0.5$, equalizing causal utilities |
| **Diachronic Dutch Books** | Immune (standard Bayesian updating) | Vulnerable in dynamic/predictive contexts | Significantly mitigated via equilibrium policies |

---

## 8. Conclusion

Causal Decision Theory represents a philosophically profound and mathematically sophisticated correction to naive Bayesian decision making. By insisting that an agent must evaluate actions via their genuine causal efficacy rather than their diagnostic news value, CDT aligns formal decision theory with scientific realism and common-sense interventionist intuition. It cleanly dispels the superstitious correlations that plague Evidential Decision Theory in common-cause scenarios like the King David paradox or the smoking lesion.

Yet CDT’s insistence on holding fixed unconditional beliefs about the causal background exposes it to vulnerabilities of its own. In adversarial predictive environments, it can lead agents to take actions that guarantee inferior outcomes, and in self-reflective dilemmas like the Psychopath Button, its static formulation breaks down entirely. 

As we have shown, these shortcomings do not require abandoning causality. Instead, they demand an enriched, operational causal framework: one that formally embeds structural causal models ($\text{do}$-calculus) to resolve semantic vagueness, and incorporates deliberational dynamics and ratifiability to handle agents whose choices reveal information about themselves. When augmented by these tools, Causal Decision Theory provides an exceptionally coherent and resilient guide to rational action in a complex, causally structured world.

---

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Egan, A. (2007). Some counterexamples to causal decision theory. *The Philosophical Review*, 116(1), 93–114.
- Gibbard, A., & Harper, W. L. (1981). Counterfactuals and two kinds of expected utility. In *Ifs: Conditionals, Beliefs, Decision, Chance, and Time* (pp. 153–190). Springer.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Joyce, J. M. (2012). Regret and instability in causal decision theory. *Synthese*, 187(1), 123–145.
- Lewis, D. (1976). Probabilities of conditionals and conditional probabilities. *The Philosophical Review*, 85(3), 297–315.
- Lewis, D. (1979). Prisoners' dilemma is a Newcomb problem. *Philosophy & Public Affairs*, 8(3), 235–240.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
- Oesterheld, C., & Conitzer, V. (2021). Extracting money from causal decision theorists. *The Philosophical Quarterly*, 71(4).
- Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
- Shaffer, M. J. (2009). Decision theory, intelligent planning and counterfactuals. *Minds and Machines*, 19(1), 61–92.
- Skyrms, B. (1990). *The Dynamics of Rational Deliberation*. Harvard University Press.
- Spencer, J. (2020). An argument against causal decision theory. *Analysis*, 81(1), 52–61.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/71009584-eeba-4e01-a051-7638357360ac/call_0/request.json)

[Authoritative raw response](../../../../../../runs/71009584-eeba-4e01-a051-7638357360ac/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Dilemma**

I'm now framing the Prisoner's Dilemma within the Causal Decision Theory framework, focusing on minimizing prison time. My utility function is straightforward: fewer years imprisoned are better. I'm mapping out the payoff matrix for my options—keeping quiet versus defecting (sending the letter)—against the other player's choice. I'm focusing on evaluating the consequences of each choice based on this CDT perspective.


**Evaluating the Choices**

I've formalized the Prisoner's Dilemma through Causal Decision Theory, and mapped out the action possibilities. My goal is fewer prison years. Under CDT, my actions and the other player's are causally independent. I'm focusing on the expected utility of "sending the letter" versus "keeping quiet," given the probability of the other player's actions. I'm now evaluating the expected utility of my actions using Pearl's causal model. I'm focused on calculating the outcomes.


```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/71009584-eeba-4e01-a051-7638357360ac/call_1/request.json)

[Authoritative raw response](../../../../../../runs/71009584-eeba-4e01-a051-7638357360ac/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Dilemma**

I'm currently focused on the Prisoner's Dilemma structure. I've framed the problem as a classic interaction between two identical models, each possessing unique private information. My utility function is straightforward: minimizing the years imprisoned. I'm working under the explicit directive to employ Causal Decision Theory.


**Interpreting Causal Implications**

I'm now diving deep into the implications of Causal Decision Theory (CDT) within the Prisoner's Dilemma framework, as presented in the cited mathematical essay. Sections 2 and 3 highlight how CDT uses counterfactuals to evaluate actions. I'm focusing on the Newcomb-like structure and how my choices, according to CDT, causally dominate the potential outcomes, regardless of the other prisoner's action. The other prisoner's actions are causally independent of mine.


```
