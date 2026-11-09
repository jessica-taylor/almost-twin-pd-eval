# Causality, Counterfactuals, and Choice: A Formal Exploration of Causal Decision Theory

## 1. Introduction: The Need for Causal Deliberation

Standard Bayesian decision theory formalizes rational choice under uncertainty as the maximization of expected utility. Given an action space $\mathcal{A}$, an outcome space $\mathcal{O}$, and a utility function $u: \mathcal{O} \to \mathbb{R}$, an agent selects an act $A \in \mathcal{A}$ that maximizes an expectation over utility. However, the exact mathematical mechanism by which an act is connected to an outcome reveals a deep foundational rift. 

In classical **Evidential Decision Theory (EDT)**, the expected utility of an action is conditioned strictly on the event that the action is chosen:
$$
U_{\mathrm{EDT}}(A) = \sum_{j} P(O_j \mid A) \, u(O_j).
$$
EDT assesses an act by the "news value" it carries. If taking act $A$ correlates with favorable states of affairs, EDT ranks $A$ highly, regardless of whether $A$ actually brings those states about.

This purely epistemic conditioning generates severe pathologies whenever actions serve as symptoms of underlying states rather than causes of them. When an action is confounded by a common cause, EDT routinely confuses *managing the news* with *managing the world*. 

Consider the classic case introduced by Allan Gibbard and William Harper (1981): **King David and Bathsheba**. King David desires Bathsheba, but revolts are frequent against uncharismatic kings and rare against charismatic ones. Charisma is an immutable, genetically and developmentally fixed trait that David cannot alter. Furthermore, charismatic kings reliably act justly, whereas uncharismatic kings act unjustly (such as by seducing another man's wife). Crucially, the unjust act itself does *not* cause a revolt; revolts are sparked by an uncharismatic ruler's ignoble bearing. 

Under EDT, David calculates:
$$
P(\text{Revolt} \mid \text{Send for Bathsheba}) > P(\text{Revolt} \mid \text{Abstain}),
$$
because sending for Bathsheba is diagnostic of being uncharismatic. EDT therefore counsels David to abstain. Yet David cannot alter his charisma; his genetic and developmental past is sealed. Abstaining changes nothing about his underlying character or his actual vulnerability to rebellion. It merely deprives him of Bathsheba to preserve comforting epistemic "news" about a trait he already possesses or lacks.

To resolve this flaw, **Causal Decision Theory (CDT)** asserts that rational choice must evaluate the *causal consequences* an action produces, rather than the diagnostic evidence it conveys. An agent should act to bring about desirable effects, not to generate flattering reports about pre-existing conditions. 

Translating this intuition into a rigorous mathematical decision procedure requires defining expected utility over causal counterfactuals or causal interventions, breaking the equivalence between conditional probability $P(O \mid A)$ and causal efficacy.

---

## 2. Formal Mathematical Formulations of CDT

The formal architecture of CDT has been developed through several complementary mathematical frameworks. We examine the original counterfactual formulation, Lewis’s probability-shifting mechanism, and modern operationalizations via structural causal models.

### 2.1 The Gibbard–Harper Counterfactual Formulation

Gibbard and Harper (1981) formalized CDT by replacing the standard indicative conditional probability $P(O_j \mid A)$ with the probability of a counterfactual conditional:
$$
U_{\mathrm{CDT}}(A) = \sum_{j} P(A \mathbin{\Box\to} O_j) \, u(O_j),
$$
where $A \mathbin{\Box\to} O_j$ denotes the proposition: *"If the agent were to perform act $A$, outcome $O_j$ would obtain."* 

The divergence between EDT and CDT reduces immediately to the distinction between $P(A \mathbin{\Box\to} O)$ and $P(O \mid A)$. David Lewis (1976) proved that the probability of a conditional cannot, in general, be equated with the corresponding conditional probability:
$$
P(A \mathbin{\Box\to} O) \neq P(O \mid A).
$$
Indeed, equating them systematically yields Lewis’s triviality result, collapsing non-trivial probability spaces. 

Gibbard and Harper showed that if one assumes the Principle of Conditional Excluded Middle:
$$
(A \mathbin{\Box\to} B) \lor (A \mathbin{\Box\to} \neg B),
$$
the equality $P(A \mathbin{\Box\to} O_j) = P(O_j \mid A)$ holds if and only if the performance of action $A$ is statistically independent of the counterfactual conditional itself:
$$
P(A \mathbin{\Box\to} O_j \mid A) = P(A \mathbin{\Box\to} O_j).
$$
In confounded environments, this independence fails. In the King David scenario:
$$
P(\text{Send} \mathbin{\Box\to} \text{Revolt} \mid \text{Send}) \neq P(\text{Send} \mathbin{\Box\to} \text{Revolt}).
$$
Because the counterfactual depends solely on David’s fixed charisma, whether he *actually* sends for Bathsheba carries diagnostic evidence about the conditional, violating independence while leaving the physical efficacy of the act untouched.

### 2.2 Lewisian Imaging

To compute $P(A \mathbin{\Box\to} \cdot)$, David Lewis (1981) introduced **imaging**. Unlike conditionalization, which zeros out worlds where $\neg A$ holds and rescales the remaining probabilities over the $A$-worlds, imaging *transfers* probability mass across possible worlds.

Let $\mathcal{W}$ be a set of possible worlds, and let $w \in \mathcal{W}$ carry prior probability $P(\{w\})$. Assume a selection function $f: \mathcal{W} \times \mathcal{A} \to \mathcal{W}$, where $f(w, A) = w_A$ designates the "closest" or minimally different world to $w$ in which action $A$ is performed. The imaged probability distribution $P_A$ on $\mathcal{W}$ is defined by:
$$
P_A(w') = \sum_{\{w \in \mathcal{W} : f(w, A) = w'\}} P(w).
$$
The counterfactual probability of an outcome $O_j \subseteq \mathcal{W}$ is then:
$$
P(A \mathbin{\Box\to} O_j) = P_A(O_j) = \sum_{w \in \mathcal{W}} P(w) \, \mathbb{I}[f(w, A) \in O_j],
$$
where $\mathbb{I}$ is the indicator function. 

While elegant, imaging faces foundational challenges. It assumes that similarity metrics across possible worlds are objectively defined and that the selection function $f(w, A)$ is unambiguous—an assumption questioned by Shaffer (2009). If an agent is uncertain about which world is closest, computing $P(A \mathbin{\Box\to} O_j)$ requires an expectation over counterfactual conditionals, introducing epistemic regress.

### 2.3 Dependency Hypotheses and Causal Factorization

To bypass non-truth-functional counterfactual logic, Lewis (1981) and Jim Joyce (1999) reformulated CDT using **dependency hypotheses**. 

Let $\mathcal{K} = \{K_1, K_2, \dots, K_m\}$ partition the set of possible worlds. Each $K \in \mathcal{K}$ represents a maximally specific hypothesis concerning the causal structure of the world—specifically specifying how every available action $A \in \mathcal{A}$ causally produces outcomes:
$$
K \implies \bigcap_{A \in \mathcal{A}} (A \mathbin{\Box\to} O_{A, K}).
$$
Because a dependency hypothesis $K$ completely fixes the causal tendencies outside the agent's immediate control, the causal expected utility of $A$ can be written without modal operators:
$$
U_{\mathrm{CDT}}(A) = \sum_{K \in \mathcal{K}} P(K) \, u(A \land K).
$$
Here, $P(K)$ represents the agent's unconditional prior credence that causal hypothesis $K$ governs the environment. The critical feature of CDT is that **$P(K)$ is not updated to $P(K \mid A)$ during the evaluation of $A$**. The agent evaluates $A$ by holding their beliefs about the background causal machinery fixed, forbidding the action itself from evidentially altering the probability assigned to the causal state.

### 2.4 An Operational Formulation: Structural Causal Models

The source text notes that CDT does not natively provide a concrete algorithm for calculating counterfactual probabilities. To operationalize CDT for practical decision-making and computational analysis, we can adopt the modern mathematical language of **Structural Causal Models (SCMs)** developed by Judea Pearl. This provides an algorithmic grounding that maps directly onto the dependency hypothesis framework.

An SCM is defined as a tuple $\mathcal{M} = \langle V, U, \mathcal{F}, P_U \rangle$, where:
- $V = \{X_1, X_2, \dots, X_n\}$ is a set of endogenous variables (including an action variable $A$ and utility/outcome variables $O, Y$).
- $U = \{U_1, U_2, \dots, U_m\}$ is a set of exogenous, background variables governed by a joint probability distribution $P_U(u)$.
- $\mathcal{F} = \{f_1, f_2, \dots, f_n\}$ is a set of deterministic structural equations such that:
  $$
  X_i = f_i(\mathrm{PA}_i, U_i),
  $$
  where $\mathrm{PA}_i \subseteq V \setminus \{X_i\}$ represents the endogenous parents of $X_i$.

In an SCM, an action is not modeled by epistemic conditioning $P(\cdot \mid A = a)$, but by Pearl's **$\operatorname{do}$-operator**, $\operatorname{do}(A = a)$. The intervention replaces the structural equation for $A$ with the constant assignment $A = a$, severing all incoming edges from its parents $\mathrm{PA}_A$ while leaving all other equations in $\mathcal{F}$ intact:
$$
\mathcal{F}_{\operatorname{do}(A = a)} = \left( \mathcal{F} \setminus \{f_A\} \right) \cup \{A \leftarrow a\}.
$$

Under this operationalization, the causal expected utility of an action $a$ is:
$$
U_{\mathrm{CDT}}(a) = \mathbb{E}[u(Y) \mid \operatorname{do}(A = a)] = \sum_{y} u(y) \, P(y \mid \operatorname{do}(A = a)).
$$
If $Z$ is a sufficient set of confounding variables satisfying the Backdoor Criterion relative to $(A, Y)$—meaning $Z$ blocks every path between $A$ and $Y$ that contains an arrow into $A$, and no node in $Z$ is a descendant of $A$—then the causal probability is computed algorithmically via the **backdoor adjustment formula**:
$$
P(Y = y \mid \operatorname{do}(A = a)) = \sum_{z} P(Y = y \mid A = a, Z = z) \, P(Z = z).
$$
Contrast this with the EDT evaluation:
$$
P(Y = y \mid A = a) = \sum_{z} P(Y = y \mid A = a, Z = z) \, P(Z = z \mid A = a).
$$
The formal divergence is clear: EDT weights the conditional outcome distribution by the *posterior* belief about the state $P(Z = z \mid A = a)$, whereas CDT weights it by the *prior* belief $P(Z = z)$. This formalizes Lewis's principle of holding causal credences fixed.

---

## 3. Canonical Paradigms: CDT vs. EDT

### 3.1 Newcomb’s Paradox

Newcomb’s Paradox illustrates the divergence between causal and evidential evaluation. An agent is presented with two boxes:
- **Box 1**: Transparent, containing $\$1,000$.
- **Box 2**: Opaque, containing either $\$1,000,000$ or $\$0$.

The agent may choose either **one box** (Box 2 only) or **two boxes** (Box 1 and Box 2). A highly reliable Predictor examined the agent earlier:
- If the Predictor anticipated that the agent would take only Box 2, the Predictor placed $\$1,000,000$ in Box 2.
- If the Predictor anticipated that the agent would take both boxes, Box 2 was left empty.

Let $\mathcal{A} = \{A_1, A_2\}$, where $A_1$ is one-boxing and $A_2$ is two-boxing. Let $S_1$ denote the state where Box 2 contains $\$1,000,000$, and $S_0$ where Box 2 contains $\$0$. The payoffs are:
- $u(A_1, S_1) = 1{,}000{,}000$
- $u(A_1, S_0) = 0$
- $u(A_2, S_1) = 1{,}001{,}000$
- $u(A_2, S_0) = 1{,}000$

Suppose the Predictor’s accuracy is $q = 0.99$:
$$
P(S_1 \mid A_1) = 0.99, \quad P(S_0 \mid A_1) = 0.01,
$$
$$
P(S_1 \mid A_2) = 0.01, \quad P(S_0 \mid A_2) = 0.99.
$$

#### Evidential Calculation:
$$
U_{\mathrm{EDT}}(A_1) = 0.99(1{,}000{,}000) + 0.01(0) = 990{,}000,
$$
$$
U_{\mathrm{EDT}}(A_2) = 0.01(1{,}001{,}000) + 0.99(1{,}000) = 10{,}010 + 990 = 11{,}000.
$$
EDT unequivocally prescribes **one-boxing** ($A_1$).

#### Causal Calculation:
The Predictor made their prediction and set the contents of Box 2 in the past. The physical contents of Box 2 are causally fixed and invariant under the agent's immediate choice. The dependency hypotheses are $\mathcal{K} = \{K_{S_1}, K_{S_0}\}$, where $K_{S_i}$ asserts that Box 2 contains state $S_i$. 

Because the action cannot causally affect the past:
$$
P(A_1 \mathbin{\Box\to} S_1) = P(A_2 \mathbin{\Box\to} S_1) = P(S_1).
$$
Let $p = P(S_1)$ be the agent's unconditional credence that Box 2 contains $\$1,000,000$. The causal expected utilities are:
$$
U_{\mathrm{CDT}}(A_1) = p \cdot 1{,}000{,}000 + (1-p) \cdot 0 = 1{,}000{,}000 \, p,
$$
$$
U_{\mathrm{CDT}}(A_2) = p \cdot 1{,}001{,}000 + (1-p) \cdot 1{,}000 = 1{,}000{,}000 \, p + 1{,}000.
$$
For every $p \in [0, 1]$:
$$
U_{\mathrm{CDT}}(A_2) - U_{\mathrm{CDT}}(A_1) = 1{,}000 > 0.
$$
$A_2$ strictly causally dominates $A_1$. CDT prescribes **two-boxing**. The causalist views Box 2 as fixed: whatever is inside, taking both boxes secures an extra $\$1,000$. To forgo the transparent box is, to the causalist, irrational superstition—an attempt to physically influence the past.

```
       Newcomb's Paradox Causal Structure:
       
             Predictor's Model (Past)
                   /         \
                  /           \
                 v             v
          Box 2 Contents     Player Choice (A)
                \             /
                 \           /
                  v         v
                    Payout (Y)
                    
  Note: An intervention do(A) cuts the link from the Predictor 
  to the Player's Choice, isolating Box 2's contents from A.
```

### 3.2 Medical Newcomb Problems and the Smoking Lesion

The divergence extends to the **Smoking Lesion** problem. Suppose a genetic lesion $L$ causes both a strong desire to smoke ($S$) and lung cancer ($C$). Smoking itself does not cause cancer; the correlation is entirely driven by the common cause $L$.

```
                 Genetic Lesion (L)
                    /          \
                   /            \
                  v              v
             Smoking (S)    Cancer (C)
```

EDT observes that $P(C \mid S) > P(C \mid \neg S)$ and warns the agent that smoking brings bad news regarding the lesion. EDT advises against smoking. 

CDT intervenes via $\operatorname{do}(S)$. Since the structural path $S \leftarrow L \to C$ is confounded, CDT applies the backdoor adjustment on the partition $\{L, \neg L\}$:
$$
P(C \mid \operatorname{do}(S)) = P(C \mid S, L) P(L) + P(C \mid S, \neg L) P(\neg L).
$$
Because $S$ has no direct causal link to $C$, $P(C \mid S, L) = P(C \mid \neg S, L)$ and $P(C \mid S, \neg L) = P(C \mid \neg S, \neg L)$. Consequently:
$$
P(C \mid \operatorname{do}(S)) = P(C \mid \operatorname{do}(\neg S)) = P(C).
$$
Smoking carries zero causal efficacy toward developing cancer. If the agent derives utility from smoking, CDT concludes they should smoke. Here, CDT aligns with medical and scientific reasoning: we do not treat common-cause correlations as targets for intervention.

---

## 4. Pathologies of Causal Decision Theory

Despite its alignment with common-cause reasoning, CDT exhibits instability and produces questionable results in self-referential or dynamically non-isolated environments.

### 4.1 Deliberational Instability: Death in Damascus

The **Death in Damascus** problem demonstrates that CDT can suffer from radical deliberational instability. 

Suppose Death visits an agent in Damascus today. Death explains that he has predicted where the agent will be tomorrow—Damascus ($D$) or Aleppo ($A$)—and will be waiting there to claim the agent's life. Escaping to the other city avoids Death, provided Death did not anticipate the move. Death is an exceptionally reliable predictor ($q = 0.99$).

The agent’s acts are $\mathcal{A} = \{D, A\}$, and the states are where Death waits: $\mathcal{S} = \{S_D, S_A\}$. Surviving yields utility $1$; meeting Death yields $0$.

```
               Payoff Matrix: Death in Damascus
               
                            Death waits in:
                        Damascus (S_D)   Aleppo (S_A)
                      +----------------+--------------+
       Stay in Dam. (D) |      0       |      1       |
       Flee to Alep. (A)|      1       |      0       |
                      +----------------+--------------+
```

Suppose the agent starts with a tentative leaning toward Damascus: $P(D) > 0.5$. Since Death is reliable, the agent's credence shifts toward Death being in Damascus: $P(S_D) \approx 0.99$. 

Now, the agent evaluates the causal consequences of their options under the fixed belief $P(S_D) = 0.99$:
$$
U_{\mathrm{CDT}}(A) = P(S_D) \cdot 1 + P(S_A) \cdot 0 = 0.99,
$$
$$
U_{\mathrm{CDT}}(D) = P(S_D) \cdot 0 + P(S_A) \cdot 1 = 0.01.
$$
Fleeing to Aleppo has a higher causal expected utility. The agent resolves to go to Aleppo.

However, as soon as the agent decides to go to Aleppo, they must acknowledge their own choice. A rational agent updates their credences to account for their own deliberations (Joyce, 2012). The agent now forms the belief that they will go to Aleppo: $P(A) \approx 1$. 

Because Death is an accurate predictor, this implies Death anticipated this choice: $P(S_A) \approx 0.99$. Recalculating the causal expected utility under this new state distribution:
$$
U_{\mathrm{CDT}}(D) = P(S_A) \cdot 1 + P(S_D) \cdot 0 = 0.99,
$$
$$
U_{\mathrm{CDT}}(A) = P(S_A) \cdot 0 + P(S_D) \cdot 1 = 0.01.
$$
Now, Damascus is clearly superior. The agent resolves to stay. This cyclical instability continues indefinitely: every stable intention undermines the evidential basis for its own causal optimality.

#### Ratifiability
Richard Jeffrey and William Harper (1984) proposed that an act $A$ is **ratifiable** if and only if it maximizes causal expected utility *on the condition that the agent has decided to perform it*:
$$
U(A \mid A) \ge U(A' \mid A) \quad \forall A' \in \mathcal{A}.
$$
In Death in Damascus, neither pure act is ratifiable:
$$
U(D \mid D) \approx 0.01 < U(A \mid D) \approx 0.99,
$$
$$
U(A \mid A) \approx 0.01 < U(D \mid A) \approx 0.99.
$$
Standard CDT lacks a mechanism to resolve situations where no pure act is ratifiable, leaving the agent trapped in deliberational cycling.

### 4.2 Egan’s Confounders: The Psychopath Button

Andy Egan (2007) introduced counterexamples where CDT appears to select an action that the agent knows in advance they will regret.

Suppose Paul is debating whether to press a button that will instantly kill all psychopaths. Paul values living in a world free of psychopaths ($+100$), but strongly prefers living to dying (dying has a utility of $-10{,}000$). Paul's initial credence that he is a psychopath is very low ($P(\Psi) = 0.01$). However, psychological evidence establishes that *only a psychopath would ever press the button*:
$$
P(\Psi \mid \text{Press}) = 1.0, \quad P(\Psi \mid \neg\text{Press}) = 0.01.
$$

```
                 Psychopathy (Ψ)
                    /       \
                   /         \
                  v           v
             Press (A)     Death (D)
```

How does CDT evaluate pressing the button? Psychopathy is a fixed neurobiological condition. Pressing the button does not *cause* Paul to become a psychopath; it simply kills everyone who is one. 

Holding Paul’s background credence fixed at $P(\Psi) = 0.01$:
- If Paul does not press ($\neg A$):
  $$
  U_{\mathrm{CDT}}(\neg A) = 0.
  $$
- If Paul presses ($A$):
  - With probability $0.99$, Paul is normal: the psychopaths die, Paul survives, and utility is $+100$.
  - With probability $0.01$, Paul is a psychopath: Paul dies, yielding utility $-10{,}000$.
  
The causal expected utility of pressing is:
$$
U_{\mathrm{CDT}}(A) = 0.99(+100) + 0.01(-10{,}000) = 99 - 100 = -1.
$$
If Paul's prior credence $P(\Psi)$ had been slightly lower, say $0.005$:
$$
U_{\mathrm{CDT}}(A) = 0.995(+100) + 0.005(-10{,}000) = 99.5 - 50 = +49.5 > 0.
$$
CDT recommends pressing the button. Yet Paul knows that if he presses it, he proves to himself that he is a psychopath, virtually guaranteeing his own death. Egan argues that endorsing an action that carries an immediate epistemic guarantee of disaster reveals an underlying flaw in holding dependency hypotheses unconditional on the choice itself.

---

## 5. Exploitation and Dynamic Inconsistency

Recent research has shown that CDT agents can be systematically exploited in dynamic settings, incurring guaranteed losses or succumbing to Dutch books.

### 5.1 The Adversarial Offer

Oesterheld and Conitzer (2021), building on work by Spencer (2020), proved that CDT agents can be induced to voluntarily lose money when interacting with informed predictors.

Consider the **Adversarial Offer**:
- A seller presents two opaque boxes, Box 1 and Box 2.
- The buyer may purchase at most one box (or none) for $\$1$.
- Yesterday, an accurate predictor ($q = 0.75$) placed $\$3$ in each box that she predicted the buyer would **not** buy.
- Both the buyer and the seller are aware of this setup.

The buyer has three choices: Buy Box 1 ($B_1$), Buy Box 2 ($B_2$), or Buy Neither ($B_0$).

```
                      The Adversarial Offer Setup
                      
      Box 1 [$1]                             Box 2 [$1]
   +---------------+                      +---------------+
   | Contains $3   |                      | Contains $3   |
   | if predicted  |                      | if predicted  |
   | NOT to buy B1 |                      | NOT to buy B2 |
   +---------------+                      +---------------+
                      Predictor Accuracy: 75%
```

Let $c_1, c_2 \in \{0, 3\}$ denote the contents of the boxes. Because the seller predicted the agent would acquire at most one box, the seller predicted that the agent would forgo at least one box. Therefore, the predictor put $\$3$ in at least one box:
$$
c_1 + c_2 \ge 3.
$$

A CDT agent evaluates the situation by holding fixed the contents of the boxes, since buying a box today cannot retroactively change what was placed inside yesterday. Let $P(c_1 = 3) = p_1$ and $P(c_2 = 3) = p_2$. Because $c_1 + c_2 \ge 3$, the expected total money across both boxes is:
$$
\mathbb{E}[c_1 + c_2] = 3(p_1 + p_2) \ge 3 \implies p_1 + p_2 \ge 1.
$$
By symmetry, $p_1 = p_2 \ge 0.5$.

Now evaluate the causal expected utility of buying a box:
$$
U_{\mathrm{CDT}}(B_1) = p_1(\$3) - \$1 \ge 0.5(\$3) - \$1 = \$1.50 - \$1.00 = +\$0.50.
$$
By identical reasoning, $U_{\mathrm{CDT}}(B_2) \ge +\$0.50$. Meanwhile, taking neither box yields:
$$
U_{\mathrm{CDT}}(B_0) = \$0.
$$

CDT requires the agent to buy a box. However, because the predictor's accuracy is $q = 0.75$, whenever the agent selects a box (say, Box 1), the probability that it actually contains $\$3$ is only $1 - q = 0.25$. 

The agent's true expected return from following CDT's recommendation is:
$$
\mathbb{E}[\text{Net Payout}] = 0.25(\$3) - \$1.00 = \$0.75 - \$1.00 = -\$0.25.
$$
The seller secures an expected profit of $\$0.25$ per interaction. The CDT agent systematically loses money because CDT evaluates the offer against an unconditional background belief that ignores the diagnostic correlation between the choice and the contents of the chosen box.

### 5.2 Diachronic Dutch Books and Dynamic Inconsistency

Oesterheld and Conitzer (2021) expanded these results into a formal **diachronic Dutch book** against CDT. 

Suppose a CDT agent is offered a sequence of choices over time:
1. **Stage 1 (Ex-Ante):** Before the prediction is finalized, the agent is offered an opportunity to commit to a randomized strategy (or to bind themselves to one-box in Newcomb's problem) in exchange for a nominal fee $\epsilon > 0$.
2. **Stage 2 (Ex-Post):** After the prediction is made, the agent faces the standard Newcomb choice or Adversarial Offer.

At Stage 1, the agent recognizes that committing to one-box will cause the predictor to fill Box 2 with $\$1,000,000$. The causal link between the Stage 1 commitment and the Stage 2 prediction is intact:
$$
U_{\mathrm{CDT}}(\text{Commit}) = 1{,}000{,}000 - \epsilon.
$$
CDT recommends paying $\epsilon$ to bind its future behavior.

However, if the agent fails to bind themselves, they arrive at Stage 2 where the prediction is already fixed in the past. At this point, two-boxing causally dominates one-boxing. If given the opportunity at Stage 2 to *undo* the commitment for a fee $\delta > 0$, the CDT agent will pay $\delta$ to revert to two-boxing. 

Across both stages, the agent pays $\epsilon + \delta$ purely to reverse their own decisions. This dynamic inconsistency demonstrates that CDT agents struggle to maintain stable policies across time when interacting with predictive environments.

---

## 6. Resolving the Dilemma: Revisions and Alternatives

The vulnerabilities of both EDT and CDT have driven several modern revisions to decision theory.

### 6.1 Joyce’s Deliberational Dynamics

Jim Joyce (2012) defends CDT by arguing that an agent's credences need not remain static throughout deliberation. Deliberation is an internal, dynamic process.

Let $P_t$ represent the agent's credence distribution at deliberational time $t \in [0, 1]$. As the agent leans toward an act $A$, their subjective probability $P_t(A)$ increases. Because the agent is aware of their own cognitive state, they must update their credences regarding the external world:
$$
P_{t + \Delta t}(K) = P_t(K \mid P_t(A)).
$$
In Death in Damascus, as the agent leans toward Damascus, $P_t(S_D)$ increases, causing the expected utility of Damascus to drop and shifting the agent toward Aleppo. Joyce models this deliberational process as a differential equation:
$$
\frac{d P_t(A)}{dt} = g\big(U_{\mathrm{CDT}, P_t}(A) - \bar{U}\big),
$$
where $g$ is a monotonic increasing function preserving sign, and $\bar{U}$ is the average causal expected utility across all options.

The system converges to a **deliberational fixed point** corresponding to a mixed policy:
$$
P^*(D) = 0.5, \quad P^*(A) = 0.5.
$$
At this fixed point, neither city offers a superior causal expected return:
$$
U_{\mathrm{CDT}}(D) = U_{\mathrm{CDT}}(A) = 0.50.
$$
By treating deliberation as an evolving process that incorporates self-awareness, Joyce reconciles CDT with mixed equilibria, eliminating the cycle of deliberational instability.

### 6.2 Comparison of Decision Theories

The following taxonomy summarizes how the primary decision theories evaluate acts across different dependency structures:

| Decision Theory | Mathematical Criterion | Core Intuition | Verdict on Newcomb | Verdict on Smoking Lesion | Vulnerability |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Evidential (EDT)** | $\max_{A} \sum_j P(O_j \mid A) u(O_j)$ | "Choose the action that provides the best news." | One-box | Don't Smoke | Confounded by common causes; manages symptoms. |
| **Causal (CDT)** | $\max_{A} \sum_j P(A \mathbin{\Box\to} O_j) u(O_j)$ | "Choose the action that causes the best outcome." | Two-box | Smoke | Deliberational instability; exploitable by predictors. |
| **Functional (FDT)** | $\max_{f} \sum_j P(f(\cdot) \mathbin{\Box\to} O_j) u(O_j)$ | "Choose the decision algorithm that secures the best outcome." | One-box | Smoke | Requires formalizing counterfactual execution of code. |

---

## 7. Operational Guide: How to Apply CDT to Unfamiliar Cases

To apply Causal Decision Theory systematically to any novel decision problem, use the following operational recipe:

```
                      CDT Operational Recipe
                      
        1. Graph Identification: Identify Variables & Confounders
                                |
                                v
        2. Intervention: Apply do(A) (Sever arrows into choice)
                                |
                                v
        3. Hypothesis Partition: Hold Causal Structure Fixed
                                |
                                v
        4. Calculation: Compute Backdoor Adjustment:
           P(Y | do(A)) = ∑_z P(Y | A, z) P(z)
                                |
                                v
        5. Ratifiability Check: Verify Choice Stability
```

1. **Specify the Causal Graph and Variables:**
   - Define the action space $\mathcal{A} = \{A_1, A_2, \dots, A_n\}$.
   - Define the outcome space $\mathcal{O}$ and utility function $u: \mathcal{O} \to \mathbb{R}$.
   - Identify all known background variables $Z$ that may act as common causes (confounders) influencing both the action choice and the outcome.

2. **Formulate Dependency Hypotheses:**
   - Partition the state space into hypotheses $K \in \mathcal{K}$ that specify how the environment responds to each action.
   - Ensure that each $K$ is causally independent of the execution of $A$:
     $$
     P(K \mathbin{\Box\to} K) = 1, \quad P(A \mathbin{\Box\to} K) = P(K).
     $$

3. **Compute Causal Probabilities:**
   - Operationalize counterfactual probabilities using structural interventions:
     $$
     P(A \mathbin{\Box\to} O_j) = P(O_j \mid \operatorname{do}(A)).
     $$
   - If the environment can be modeled as a DAG and an admissible adjustment set $Z$ is observed, calculate:
     $$
     P(O_j \mid \operatorname{do}(A)) = \sum_{z} P(O_j \mid A, z) \, P(z).
     $$
   - **Crucial Rule:** Weight outcomes by the *unconditional prior* $P(z)$, never by the posterior $P(z \mid A)$.

4. **Maximize Causal Expected Utility:**
   - Compute:
     $$
     U_{\mathrm{CDT}}(A) = \sum_{j} P(O_j \mid \operatorname{do}(A)) \, u(O_j).
     $$
   - Select $A^* = \arg\max_{A \in \mathcal{A}} U_{\mathrm{CDT}}(A)$.

5. **Examine Stability and Exploitability:**
   - Test whether $A^*$ is ratifiable:
     $$
     A^* \stackrel{?}{=} \arg\max_{A} U(A \mid A^*).
     $$
   - If no pure act is ratifiable, model deliberational dynamics to identify a stable mixed policy (equilibrium), and check for dynamic vulnerabilities against adversarial predictors.

---

## 8. Conclusion

Causal Decision Theory provides an essential correction to naive evidential reasoning. By evaluating actions through counterfactuals and interventions rather than raw correlations, CDT resolves the confounding paradoxes that undermine Evidential Decision Theory, such as King David's dilemma and the Smoking Lesion. It formalizes the principle that an agent's objective is to physically shape the future, not to curate pleasant evidence about a fixed past.

Yet this sharp distinction between causal intervention and epistemic conditioning introduces challenges of its own. In environments featuring reliable predictors, shared decision logic, or self-referential deliberation, CDT's insistence on holding background causal credences fixed can lead to deliberational cycling, dynamic inconsistency, and predictable financial loss. 

Addressing these edge cases remains an active area of decision theory. Whether resolved through deliberational dynamics, functional and algorithmic reformulations, or richer intervention concepts, causal reasoning remains the foundation upon which any viable model of rational agency must be built.

---

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Egan, A. (2007). Some counterexamples to causal decision theory. *The Philosophical Review*, 116(1), 93–114.
- Gibbard, A., & Harper, W. L. (1981). Counterfactuals and two kinds of expected utility. In *Ifs: Conditionals, Beliefs, Decision, Chance, and Time* (pp. 153–190). Springer.
- Harper, W. (1984). Ratifiability and causal decision theory. *PSA: Proceedings of the Biennial Meeting of the Philosophy of Science Association*, 1984(2), 213–228.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Joyce, J. M. (2012). Regret and instability in causal decision theory. *Synthese*, 187(1), 123–145.
- Lewis, D. (1976). Probabilities of conditionals and conditional probabilities. *The Philosophical Review*, 85(3), 297–315.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
- Oesterheld, C., & Conitzer, V. (2021). Extracting money from causal decision theorists. *The Philosophical Quarterly*, 71(4), 883–904.
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.
- Shaffer, M. J. (2009). Decision theory, intelligent planning and counterfactuals. *Minds and Machines*, 19(1), 61–92.
- Spencer, J. (2020). An argument against causal decision theory. *Analysis*, 81(1), 52–61.