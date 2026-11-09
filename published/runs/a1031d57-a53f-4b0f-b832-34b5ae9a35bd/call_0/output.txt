# Causal Decision Theory: Foundations, Formalisms, and Paradoxes

### Abstract

Standard Bayesian decision theory formalizes rational choice as the maximization of expected utility. However, the standard calculus of conditional probability fails to distinguish between an action that *causes* a favorable outcome and an action that merely *signals* one. Causal Decision Theory (CDT) was developed to resolve this pathology by decoupling causal efficacy from epistemic news-value. This essay provides a comprehensive mathematical and philosophical account of CDT. We examine the classical counterfactual formulation of Gibbard and Harper, investigate the underlying semantics of imaging and dependency hypotheses, contrast the framework rigorously with Evidential Decision Theory (EDT), and bridge these historical formulations with modern causal graphical models ($do$-calculus). Finally, we examine the structural limits of CDT—including decision instability, ratifiability, and dynamic exploitation via Dutch books—and assess contemporary defenses.

---

## 1. Introduction: The Efficacy–Indication Divide

A rational agent chooses an action not merely to receive good news about the state of the world, but to bring about good states of the world. In classical decision theory following Richard Jeffrey, an agent evaluates an act $A$ by its conditional expected utility:

$$V(A) = \sum_{j} P(O_j \mid A) \, u(O_j)$$

where $P$ denotes the agent's subjective probability distribution over possible outcomes $O_j$, and $u(O_j)$ is the utility (or desirability) of $O_j$. 

While mathematically elegant, this evidential approach treats an action $A$ as an epistemic condition: $V(A)$ measures how desirable it would be to *learn* that $A$ has been performed. Whenever an act is correlated with an antecedent or exogenous state that the act cannot influence, evidential conditioning conflates correlation with causation. 

Consider the classic diagnostic dilemma. Suppose a benign genetic marker causes both an irresistible craving for dark chocolate ($A$) and immunity to a fatal cardiovascular disease ($H$). Chocolate consumption itself has no direct causal impact on cardiovascular health. An agent evaluating chocolate consumption under Jeffrey's formula observes:

$$P(\text{Immunity} \mid \text{Eats Chocolate}) \gg P(\text{Immunity} \mid \neg\text{Eats Chocolate})$$

Because learning that she ate chocolate provides strong evidence that she possesses the protective gene, evidential decision theory (EDT) advises eating chocolate purely for its diagnostic value—even if the agent dislikes chocolate or if eating chocolate carries a minor, real physical cost. 

Intuitively, this is irrational: eating chocolate cannot *cause* the protective gene to appear. The agent cannot influence whether she has the gene; the gene is causally fixed. Causal Decision Theory (CDT) arose precisely to insulate rational choice from such "spurious" epistemic correlations, asserting that an action must be evaluated solely on the basis of what it *causally produces*.

---

## 2. Formal Formulations of Causal Decision Theory

To formalize causal efficacy, decision theorists replace evidential conditioning, $P(O_j \mid A)$, with an operation that tracks the counterfactual consequences of an intervention.

### 2.1. The Gibbard–Harper Counterfactual Formulation

In their foundational 1981 paper, Allan Gibbard and William Harper formulated CDT using counterfactual conditionals. Let $A \to O_j$ denote the subjunctive conditional: *"If the agent were to perform act $A$, then outcome $O_j$ would obtain."* 

The causal expected utility $U(A)$ of an act $A \in \mathcal{A}$ is defined as:

$$U(A) = \sum_{j} P(A \to O_j) \, u(O_j)$$

where $P(A \to O_j)$ is the agent's subjective probability assigned to the counterfactual proposition.

Under classical truth-functional logic, conditionals cannot capture this relationship. Following David Lewis and Robert Stalnaker, counterfactuals are evaluated across possible worlds equipped with a metric or ordering of comparative similarity: $A \to O_j$ is true at world $w$ if and only if $O_j$ holds in the closest (most similar) possible world to $w$ where $A$ is true.

### 2.2. Lewis's Triviality Result and the Need for Subjunctive Probability

One might hope to avoid counterfactual semantics by defining the probability of a conditional as the standard conditional probability: $P(A \to B) \stackrel{?}{=} P(B \mid A)$. However, David Lewis (1976) proved that no non-trivial conditional connective can satisfy this identity across all probability functions closed under conditionalization. Specifically, Lewis proved that if $P(A \to B) = P(B \mid A)$ universally, the probability function must be trivial—it can assign non-zero probability to at most two mutually exclusive propositions.

Consequently, $P(A \to O_j)$ cannot be reduced to $P(O_j \mid A)$. Gibbard and Harper demonstrated that $P(A \to O_j) = P(O_j \mid A)$ holds if and only if the act $A$ is statistically independent of the counterfactual conditional $A \to O_j$:

$$P(A \to O_j \mid A) = P(A \to O_j)$$

When an agent believes that her choice of $A$ provides evidence about the causal structure of the world, $A$ and $A \to O_j$ become statistically dependent. In such cases, CDT and EDT diverge.

### 2.3. Lewis's Imaging and Dependency Hypotheses

How should an agent compute $P(A \to O_j)$? Lewis (1981) introduced two complementary formal mechanisms: **imaging** and **dependency hypotheses**.

#### Imaging
Let $W$ be a set of possible worlds, and let $w_A$ denote the world most similar to $w$ in which $A$ is true (assuming Stalnaker's Uniqueness Assumption). If the agent’s prior credence distribution over worlds is $P$, the probability distribution *imaged* on $A$, denoted $P_A$, shifts each world's probability mass entirely to its closest $A$-counterpart:

$$P_A(w') = \sum_{\{w \in W : w_A = w'\}} P(w)$$

The causal utility is then the expectation under this shifted distribution:

$$U(A) = \sum_{w \in W} P_A(w) \, u(w)$$

Unlike Bayesian conditionalization, which zeros out worlds where $\neg A$ holds and redistributes probability mass proportionally among remaining worlds, imaging *moves* probability mass across modal space. It leaves untouched the background structural facts of each world, altering only what is minimally necessary to make $A$ true.

#### Dependency Hypotheses
Alternatively, Lewis, Brian Skyrms, and others partition modal space into maximally specific propositions regarding how outcomes depend causally on the agent's acts. Let $\mathcal{K} = \{K_1, K_2, \dots, K_m\}$ be a mutually exclusive and exhaustive set of **dependency hypotheses**. A dependency hypothesis $K$ completely specifies the counterfactual truth-values for every available act:

$$K = \bigwedge_{A_i \in \mathcal{A}} (A_i \to O_{j(i)})$$

Because a dependency hypothesis describes factors completely outside the agent's causal reach at decision time, the agent's causal evaluation must hold these hypotheses fixed. The causal expected utility is evaluated by weighting the utility of performing $A$ within each hypothesis $K$ by the agent's *unconditional* credence in $K$:

$$U(A) = \sum_{K \in \mathcal{K}} P(K) \, u(A \wedge K)$$

Because $K$ specifies the exact outcome that follows from $A$, $u(A \wedge K)$ is deterministic. 

---

## 3. Operationalizing CDT: Structural Causal Models

A persistent critique noted in the literature (e.g., Shaffer 2009) is that Gibbard, Harper, and Lewis leave the evaluation of counterfactuals procedurally underspecified. Deciding which possible world is "closest" often rests on intuitive, subjective judgments of similarity, exposing the theory to charges of vagueness.

To make CDT fully operational and applicable to unfamiliar, complex decision problems, we can formalize dependency hypotheses through Judea Pearl’s framework of **Structural Causal Models (SCMs)** and the $do$-calculus.

### 3.1. SCM Definition

A Structural Causal Model $\mathcal{M}$ is a 4-tuple $\langle U, V, \mathcal{F}, P(U) \rangle$:
1. $U = \{U_1, \dots, U_m\}$ is a set of exogenous (background) variables determined outside the model, governed by a joint probability distribution $P(U)$.
2. $V = \{V_1, \dots, V_n\}$ is a set of endogenous variables.
3. $\mathcal{F} = \{f_1, \dots, f_n\}$ is a set of deterministic structural equations such that each endogenous variable is a function of its parents: $V_i = f_i(\text{PA}_i, U_i)$, where $\text{PA}_i \subseteq V \setminus \{V_i\}$.
4. The causal graph $\mathcal{G}$ induced by $\mathcal{M}$ is a directed acyclic graph (DAG) where directed edges point from parent variables to child variables.

### 3.2. Counterfactuals via the Intervention Operator ($do$)

In an SCM, an action is not treated as an epistemic conditioning event ($V_i = a$), which merely restricts attention to the subpopulation where $V_i$ naturally assumed value $a$. Instead, an action is an **intervention**, denoted $\text{do}(V_i = a)$. 

Formally, the intervention $\text{do}(V_i = a)$ replaces the structural equation $V_i = f_i(\text{PA}_i, U_i)$ with the constant equation $V_i = a$, severing all incoming edges from $\text{PA}_i$ to $V_i$ in $\mathcal{G}$ while leaving all other equations $\mathcal{F} \setminus \{f_i\}$ unchanged.

```
Evidential Conditioning: Observe A = a     Causal Intervention: do(A = a)
          [ U ]                                      [ U ]
         /     \                                    /     \
        v       v                                  x       v
      [ A ] --> [ Y ]                            [ A ] --> [ Y ]
  (Correlation flows:                        (Backdoor path severed:
   Y <- U -> A and A -> Y)                    only A -> Y remains)
```

The distribution of an outcome variable $Y$ under this intervention is $P(Y \mid \text{do}(A = a))$. Pearl's counterfactual semantics computes the probability of the conditional $A \to Y_y$ via a rigorous three-step algorithm:
1. **Abduction:** Update the prior distribution over exogenous variables with available evidence $E = e$, obtaining $P(U \mid E = e)$.
2. **Action:** Modify the model $\mathcal{M}$ by replacing the structural equation for $A$ with $A = a$, yielding the sub-model $\mathcal{M}_a$.
3. **Prediction:** Compute the probability distribution of $Y$ in $\mathcal{M}_a$ using the updated exogenous distribution $P(U \mid E = e)$.

### 3.3. Mathematical Unification

Under the SCM framework, Lewis’s abstract dependency hypotheses find an exact mathematical realization: each configuration of the exogenous variables $u \in \text{Domain}(U)$ corresponds precisely to a dependency hypothesis $K_u$. The structural equations $\mathcal{F}$ deterministically map the pair $(u, a)$ to a unique outcome $y = f_Y(a, u)$. 

Consequently, we can state the operational CDT rule without modal ambiguity:

$$U_{\text{CDT}}(A = a) = \sum_{y} u(y) \, P(Y = y \mid \text{do}(A = a)) = \sum_{u} P(U = u) \, u\big(f_Y(a, u)\big)$$

In contrast, the EDT decision rule is:

$$U_{\text{EDT}}(A = a) = \sum_{y} u(y) \, P(Y = y \mid A = a) = \sum_{y} u(y) \frac{\sum_{\{u : f_A(u) = a, f_Y(a, u) = y\}} P(U = u)}{\sum_{\{u : f_A(u) = a\}} P(U = u)}$$

Equations (5) and (6) rigorously distinguish the two frameworks: EDT conditions on the event $f_A(u) = a$, shifting credences over the background state $U$; CDT holds the distribution over background states $P(U)$ fixed, intervening surgically on the action variable.

---

## 4. Benchmark Problems and Structural Application

To understand how CDT evaluates choices relative to EDT, we examine several classic and modern decision problems.

### 4.1. King David and Bathsheba

Gibbard and Harper illustrate the divergence between EDT and CDT using an adaptation of the biblical story of King David. 

#### Setup
David desires Bathsheba ($A$). However, he knows that kings belong to one of two unalterable psychological types: Charismatic ($C$) or Uncharismatic ($\neg C$). Charisma is fixed in early childhood and cannot be altered. David's historical data indicates:
- Charismatic kings act justly; uncharismatic kings act unjustly. Summoning another man's wife is unjust.
- Uncharismatic kings face frequent, successful revolts ($R$) due to their ignoble bearing. Charismatic kings rarely face revolts.
- An unjust act *does not cause* a revolt; revolts are causally triggered solely by an ignoble bearing.

Let the payoffs be:
- Obtaining Bathsheba without revolt: $+10$
- Obtaining Bathsheba with revolt: $-10$
- Abstaining without revolt: $0$
- Abstaining with revolt: $-20$

Summoning Bathsheba provides a net utility boost of $+10$ across all states, but introduces a major negative correlation with charisma.

```
       [ Charisma (C) ]
          /        \
         v          v
   [ Act: A ]   [ Revolt: R ]
```

#### Evaluation
- **EDT:** The agent notes that $P(C \mid A)$ is low, while $P(C \mid \neg A)$ is high. Consequently, $P(R \mid A) \gg P(R \mid \neg A)$. Conditioning on $A$ brings terrible news regarding the stability of his reign. EDT recommends abstaining ($\neg A$).
- **CDT:** The causal graph reveals that the path $A \leftarrow C \to R$ is a "backdoor" path. The intervention $\text{do}(A)$ severs $C \to A$. The probability of revolt given the intervention is:
  $$P(R \mid \text{do}(A)) = P(R \mid C)P(C) + P(R \mid \neg C)P(\neg C) = P(R \mid \text{do}(\neg A))$$
  Because $A$ has no directed path to $R$, David's choice has zero causal influence on whether a revolt occurs. The causal utility simplifies to:
  $$U_{\text{CDT}}(A) = U_{\text{CDT}}(\neg A) + 10$$
  CDT unambiguously recommends sending for Bathsheba. David recognizes that if he is uncharismatic, a revolt is already brewing; abstaining will not cure his ignoble bearing.

### 4.2. Newcomb's Problem

Newcomb's Paradox (Nozick 1969) is the central battleground between CDT and EDT.

#### Setup
An agent is presented with two boxes:
- **Box 1:** Transparent, containing $\$1,000$.
- **Box 2:** Opaque, containing either $\$1,000,000$ or $\$0$.

The agent may choose:
- $A_1$: Take only Box 2 ("one-boxing").
- $A_2$: Take both Box 1 and Box 2 ("two-boxing").

A super-intelligent Predictor, possessing a 99% predictive accuracy rate, examined the agent yesterday:
- If the Predictor anticipated $A_1$, she placed $\$1,000,000$ in Box 2.
- If the Predictor anticipated $A_2$, she left Box 2 empty.

The prediction and box preparation occurred in the past and are physically fixed.

```
     [ Predictor's Past State ]
             /        \
            v          v
   [ Box 2 Contents ]  [ Agent's Choice ]
```

#### Evaluation
- **EDT (One-Boxing):**
  $$V(A_1) = P(\text{Full} \mid A_1) \cdot 10^6 + P(\text{Empty} \mid A_1) \cdot 0 = 0.99 \cdot 10^6 = \$990,000$$
  $$V(A_2) = P(\text{Full} \mid A_2) \cdot 10^6 + 1,000 = 0.01 \cdot 10^6 + 1,000 = \$11,000$$
  EDT prescribes taking only Box 2.

- **CDT (Two-Boxing):**
  The dependency hypotheses correspond to the contents of Box 2: $K_{\text{Full}}$ (Box 2 contains $\$1,000,000$) and $K_{\text{Empty}}$ (Box 2 contains $\$0$). Crucially, the contents of Box 2 are causally independent of the agent's current physical action:
  $$P(A_1 \to K_{\text{Full}}) = P(A_2 \to K_{\text{Full}}) = P(K_{\text{Full}})$$
  Evaluating the acts yields:
  $$U(A_1) = P(K_{\text{Full}}) \cdot 10^6 + (1 - P(K_{\text{Full}})) \cdot 0 = 10^6 \, P(K_{\text{Full}})$$
  $$U(A_2) = P(K_{\text{Full}}) \cdot (10^6 + 1,000) + (1 - P(K_{\text{Full}})) \cdot 1,000 = 10^6 \, P(K_{\text{Full}}) + 1,000$$
  
  For *any* prior probability $P(K_{\text{Full}}) \in [0, 1]$:
  $$U(A_2) - U(A_1) = \$1,000 > 0$$

$A_2$ strictly dominates $A_1$ across all causal dependency hypotheses. CDT mandates two-boxing: whatever is in the box is already there; choosing Box 1 cannot causally alter the past contents of Box 2.

---

## 5. Critical Vulnerabilities and Counterexamples

Despite its intuitive causal foundation, CDT faces severe theoretical challenges. In particular, critics argue that CDT fails when an agent's deliberations or actions correlate with outcomes through self-locating beliefs or continuous updates during deliberation.

### 5.1. The Psychopath Button

Proposed by Andy Egan (2007), the Psychopath Button challenges CDT's insistence on holding unconditional credences in dependency hypotheses constant.

#### Setup
Paul can press a button ($A$) that will kill all psychopaths on Earth. Paul strongly prefers living in a world without psychopaths. However:
- Paul assigns a 99% probability to the proposition that *only a psychopath would press the button*.
- Paul strongly prefers living with psychopaths over dying.
- Whether Paul is a psychopath ($S$) is a biologically fixed, unalterable fact.

Let the utilities be:
- Normal, abstain ($\neg S \wedge \neg A$): $0$
- Psychopath, abstain ($S \wedge \neg A$): $0$
- Normal, press ($\neg S \wedge A$): $+100$ (All psychopaths dead, Paul lives)
- Psychopath, press ($S \wedge A$): $-\infty$ (Paul dies)

#### The CDT Dilemma
Because Paul's psychopathy is causally fixed, his decision to press the button cannot *cause* him to be a psychopath:
$$\text{do}(A) \text{ does not cause } S$$

If Paul enters the deliberation assigning an initial prior credence $P(S) = 0.01$ (he thinks it is very unlikely he is a psychopath), his causal evaluation is:
$$U(A) = P(\neg S) \cdot u(\neg S \wedge A) + P(S) \cdot u(S \wedge A) = 0.99(100) + 0.01(-\infty) = -\infty$$

However, suppose Paul's utility of dying is finite: $u(S \wedge A) = -10,000$. Then:
$$U(A) = 0.99(100) + 0.01(-10,000) = 99 - 100 = -1$$
Here, $U(A) < U(\neg A) = 0$.

Now suppose Paul begins with a very low prior credence that he is a psychopath, say $P(S) = 0.001$:
$$U(A) = 0.999(100) + 0.001(-10,000) = 99.9 - 10 = +89.9$$

Because $+89.9 > 0$, CDT instructs Paul to press the button. 

Yet Egan observes the profound incoherence: the moment Paul decides to press the button, he acquires decisive evidence that he *is* a psychopath, guaranteeing an outcome he disvalues catastrophically. CDT forces Paul to initiate an action while knowing that doing so indicates his own doom, because the causal expectation holds the *initial* prior $P(S)$ fixed rather than updating on the evidence supplied by Paul's own choice.

### 5.2. Death in Damascus and Decision Instability

In the classic *Death in Damascus* scenario (Gibbard and Harper 1981), an agent faces an omniscient, inescapable predictor:

#### Setup
Death visits an agent in Damascus and informs him that they have an appointment tomorrow. The agent can spend tomorrow in Damascus ($D$) or flee to Aleppo ($A$). Death is an exceptional predictor:
- If Death predicts Damascus, Death waits in Damascus.
- If Death predicts Aleppo, Death waits in Aleppo.
- The cost of fleeing to Aleppo is $1$ unit of utility. Dying yields $-100$; surviving yields $0$.

#### The Instability Loop
Suppose the agent contemplates staying in Damascus:
$$P(\text{Death in } D \mid D) \approx 1 \implies U(D) \approx -100$$
Fleeing to Aleppo appears superior: since Death is currently anticipated to be in Damascus, fleeing to Aleppo should yield $-1$ (survival minus travel cost). 

However, as soon as the agent resolves to go to Aleppo ($A$), he acquires the evidence that Death anticipated this move and is waiting in Aleppo:
$$P(\text{Death in } A \mid A) \approx 1 \implies U(A) \approx -101$$
Now Damascus appears superior (yielding $-100$ vs $-101$). 

CDT exhibits **decision instability**: no pure act is causally stable. This phenomenon led Richard Jeffrey to formulate the concept of **ratifiability**.

```
    Contemplates Damascus --------> Resolves to go to Aleppo
            ^                                  |
            |                                  |
            v                                  v
    Resolves to stay in Damascus <-------- Contemplates Aleppo
```

---

## 6. Ratifiability, Deliberational Dynamics, and Dutch Books

### 6.1. Ratifiability Defined

An act $A$ is **ratifiable** if and only if $A$ maximizes causal expected utility relative to the probability distribution updated on the news that the agent will perform $A$:

$$\text{Ratifiable}(A) \iff U(A \mid A) \ge U(A' \mid A) \quad \forall A' \in \mathcal{A}$$

where:

$$U(A' \mid A) = \sum_{j} P(A' \to O_j \mid A) \, u(O_j)$$

In *Death in Damascus*, neither pure act is ratifiable:
- $U(A \mid D) = -1 > U(D \mid D) = -100$ (Damascus is unratifiable).
- $U(D \mid A) = 0 > U(A \mid A) = -101$ (Aleppo is unratifiable).

In the *Psychopath Button*, pressing the button is unratifiable: once Paul conditionally assumes he will press, $P(S \mid A) \approx 1$, which craters the expected causal utility of pressing.

### 6.2. Deliberational Dynamics: The Defense of James Joyce

James Joyce (2012, 2020) defends CDT against Egan's counterexamples by framing decision-making not as a static, single-step computation, but as an iterative dynamical process of belief revision.

Joyce posits that during deliberation, an agent treats their own prospective choices as evidence. Let $p_t = P_t(A)$ be the agent's subjective probability that they will ultimately execute act $A$ at deliberative step $t$. 

1. At time $t$, the agent computes causal expected utilities using current credences: $U_t(A)$.
2. The agent adjusts their intention $p_{t+1}$ upward if $U_t(A) > U_t(\neg A)$, and downward otherwise.
3. As $p_t$ shifts, the agent updates their credence in the background states via Bayes' rule: $P_{t+1}(K) = P(K \mid P(A) = p_{t+1})$.
4. This adjustment continues until the system reaches a **deliberative fixed point** where $U(A) = U(\neg A)$, or an absorbing boundary.

In *Death in Damascus*, the agent converges to a mixed strategy equilibrium:
$$p^* = P(\text{Damascus}) = \frac{101}{201}$$
At this precise mixed credence, the expected causal utility of going to Damascus equals the expected causal utility of fleeing to Aleppo. Joyce argues that CDT agents do not make self-destructive choices; rather, when faced with symmetric predictive dilemmas, they recognize that their deliberation provides continuous self-locating evidence, driving them to an indifferent equilibrium state.

### 6.3. The Adversarial Offer and Diachronic Dutch Books

Recent work by Caspar Oesterheld and Vincent Conitzer (2021) demonstrates that the Joyce defense does not shield standard CDT agents from being systematically exploited. They prove that CDT agents can be subjected to **diachronic Dutch books** (guaranteed money pumps) in sequential decision environments.

Consider the **Adversarial Offer** (Spencer 2020, Oesterheld & Conitzer 2021):

#### Rules
- Two boxes ($B_1$ and $B_2$) are presented. An agent may buy at most one box for $\$1$, or buy neither.
- Yesterday, a 75% accurate predictor placed $\$3$ in each box that she predicted the agent would **not** acquire.
- If the predictor predicted the agent would acquire $B_1$, she put $\$3$ in $B_2$ and $\$0$ in $B_1$.
- If the predictor predicted the agent would acquire $B_2$, she put $\$3$ in $B_1$ and $\$0$ in $B_2$.
- If the predictor predicted the agent would acquire nothing, she put $\$3$ in both boxes.

#### CDT Reasoning
Let $b_1, b_2, \emptyset$ denote the actions of buying $B_1$, buying $B_2$, or buying neither. The agent knows that the predictor placed $\$3$ in at least one box:

$$\text{State space: } S \in \{(3, 0), (0, 3), (3, 3)\}$$

Notice that the sum of contents across both boxes is at least $\$3$:

$$\text{Contents}(B_1) + \text{Contents}(B_2) \ge \$3$$

By symmetry, from a pure causal perspective, the boxes have already been filled. The agent's purchase cannot retroactively change the bank notes inside the boxes. Taking the expectations across the unalterable causal states:

$$\mathbb{E}[\text{Contents}(B_1)] + \mathbb{E}[\text{Contents}(B_2)] \ge \$3 \implies \max\Big(\mathbb{E}[\text{Contents}(B_1)], \, \mathbb{E}[\text{Contents}(B_2)]\Big) \ge \$1.50$$

Because each box costs only $\$1.00$, the causal expected net utility of purchasing the higher-value box is:

$$U(B_i) = \mathbb{E}[\text{Contents}(B_i)] - 1.00 \ge 1.50 - 1.00 = +\$0.50 > 0$$

CDT strictly forbids choosing $\emptyset$ (which yields $\$0$). CDT mandates buying one of the two boxes. 

Yet, because the predictor has 75% accuracy:
$$P(\text{Targeted box is empty} \mid \text{Agent buys it}) = 0.75$$
The real expected return from buying a box is:
$$0.25(\$3) - \$1 = \$0.75 - \$1.00 = -\$0.25$$

The seller extracts $\$0.25$ in expectation from the CDT agent on every run. Oesterheld and Conitzer generalize this to a formal Dutch book theorem: any agent whose decisions systematically neglect the evidential link between current choice and antecedent states can be forced into a sequence of bets that guarantees a sure financial loss.

---

## 7. Comparative Analysis: CDT, EDT, and FDT

The enduring debate over CDT has catalyzed alternative foundational frameworks. The following table contrasts how the leading decision theories handle causal and correlational structures:

| Dimension | Evidential Decision Theory (EDT) | Causal Decision Theory (CDT) | Functional Decision Theory (FDT) |
| :--- | :--- | :--- | :--- |
| **Core Formula** | $\sum_j P(O_j \mid A) u(O_j)$ | $\sum_j P(A \to O_j) u(O_j)$ | $\sum_j P(f_{dec} \ \square\to O_j) u(O_j)$ |
| **Mathematical Operator** | Bayesian conditioning | Interventional calculus ($do$) | Subjunctive algorithm replacement |
| **Newcomb's Problem** | One-box ($\$1,000,000$) | Two-box ($\$1,001,000$ or $\$1,000$) | One-box ($\$1,000,000$) |
| **David and Bathsheba** | Abstain (irrational caution) | Send for Bathsheba (correct) | Send for Bathsheba (correct) |
| **Psychopath Button** | Does not press (avoids trap) | Presses (under static priors) | Does not press (avoids trap) |
| **Death in Damascus** | Predictable mixed strategy | Deliberative instability / unratifiable | Optimal mixed strategy |
| **Resistance to Exploitation**| Resists Adversarial Offer | Vulnerable to Dutch books | Resists Adversarial Offer |

Whereas EDT uses simple conditionalization (falling prey to mere correlation in common-cause cases) and CDT uses physical interventions (severing past correlations and falling prey to adversarial predictors), modern alternatives like Functional Decision Theory (Yudkowsky and Soares 2017) treat the agent's decision *algorithm* as an invariant mathematical function, intervening on the execution of the function across all modal instantiations simultaneously.

---

## 8. Applying CDT: An Algorithmic Recipe for the Practitioner

To evaluate an unfamiliar decision problem under CDT without falling into informal ambiguities, the decision theorist should apply the following sequential protocol:

```
                  Step 1: Construct Causal DAG
                   (Identify endogenous/exogenous)
                                |
                                v
                  Step 2: Check Backdoor Paths
                  (Look for confounding variables)
                                |
                                v
                  Step 3: Apply Intervention do(A)
                   (Sever incoming edges to choice)
                                |
                                v
                  Step 4: Compute Counterfactual P
                  (Lewis imaging or Pearl's calculus)
                                |
                                v
                  Step 5: Maximize Causal Expectation
                    U(A) = Sum P(do(A)) * u(O)
                                |
                                v
                  Step 6: Perform Ratifiability Audit
                     (Verify dynamic stability)
```

1. **Construct the Structural Model:** Specify the set of endogenous variables $V$, exogenous variables $U$, and structural equations $\mathcal{F}$. Construct the directed acyclic graph (DAG).
2. **Identify Common Causes:** Determine if there are unblocked backdoor paths between the decision variable $A$ and the outcome variable $Y$ (e.g., predictors, genes, psychological traits).
3. **Execute the Intervention:** Apply the Pearl intervention operator $\text{do}(A = a)$, setting the value of $A$ and severing all incoming directed edges $\text{PA}_A \to A$.
4. **Compute Counterfactual Distributions:** For each action $a \in \mathcal{A}$, determine the post-intervention distribution over outcomes:
   $$P(Y = y \mid \text{do}(A = a)) = \sum_{u} P(U = u) \, \mathbb{I}\big(f_Y(a, u) = y\big)$$
   where the distribution over exogenous states $P(U)$ remains unconditioned by $a$.
5. **Optimize:** Select the act that maximizes causal expected utility:
   $$A^* = \arg\max_{a \in \mathcal{A}} \sum_{y} u(y) \, P(Y = y \mid \text{do}(A = a))$$
6. **Perform a Ratifiability Audit:** Check whether $A^*$ satisfies $U(A^* \mid A^*) \ge U(A \mid A^*)$ for all $A$. If $A^*$ is unratifiable, model the deliberation dynamically to locate the stable deliberative fixed point.

---

## 9. Conclusion

Causal Decision Theory represents a profound philosophical insight: rational agency is defined by the capacity to alter the world, not merely to observe it. By replacing conditional probabilities with counterfactual probabilities—formalized via Lewisian imaging, dependency hypotheses, or Pearlian structural interventions—CDT successfully immunizes decision-making against spurious common-cause correlations, resolving diagnostic anomalies such as the King David dilemma.

Yet, this surgical detachment from epistemic correlation proves to be both CDT's greatest strength and its primary vulnerability. In environments characterized by highly accurate predictors, self-reflective deliberation, or adversarial mechanisms, CDT's refusal to let current actions update credences in causally fixed background states exposes the agent to chronic decision instability and systematic economic exploitation. 

Whether CDT's vulnerabilities can be fully remediated through Joyce's deliberational dynamics or require a complete transition to alternative paradigms remains one of the most vibrant open debates in formal epistemology and theoretical artificial intelligence.

---

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge: Cambridge University Press.
- Egan, A. (2007). Some counterexamples to causal decision theory. *The Philosophical Review*, 116(1), 93–114.
- Gibbard, A., & Harper, W. L. (1981). Counterfactuals and two kinds of expected utility. In *Ifs: Conditionals, Beliefs, Decision, Chance, and Time* (pp. 153–190). Springer, Dordrecht.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge: Cambridge University Press.
- Joyce, J. M. (2012). Regret and instability in causal decision theory. *Synthese*, 187(1), 123–145.
- Lewis, D. (1976). Probabilities of conditionals and conditional probabilities. *The Philosophical Review*, 85(3), 297–315.
- Lewis, D. (1979). Prisoners' dilemma is a Newcomb problem. *Philosophy & Public Affairs*, 8(3), 235–240.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
- Nozick, R. (1969). Newcomb's problem and two principles of choice. In *Essays in Honor of Carl G. Hempel* (pp. 114–146).
- Oesterheld, C., & Conitzer, V. (2021). Extracting money from causal decision theorists. *The Philosophical Quarterly*, 71(4), pqaa086.
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*. 2nd ed. Cambridge: Cambridge University Press.
- Shaffer, M. J. (2009). Decision theory, intelligent planning and counterfactuals. *Minds and Machines*, 19(1), 61–92.
- Spencer, J. (2020). An argument against causal decision theory. *Analysis*, 81(1), 52–61.
- Yudkowsky, E., & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. Technical Report, Machine Intelligence Research Institute.