# The Geometry of News: A Mathematical Exposition of Evidential Decision Theory

## 1. Introduction: Auspiciousness vs. Efficacy

Standard Bayesian decision theory formalizes instrumental rationality as the maximization of expected utility. Yet beneath this consensus lies a fundamental schism regarding how an agent ought to conceive of the relationship between their actions and the state of the world. 

When you deliberate, should you assess an action by what it **causally brings about**, or by what its occurrence **reveals** about the world you inhabit?

**Evidential Decision Theory (EDT)** takes the latter stance. Originating in the philosophical work of Richard Jeffrey (1965) and formalized in contrast to causal alternatives by Allan Gibbard and William Harper (1976), EDT posits that the rational agent maximizes *news value*. The guiding maxim of EDT, as modern proponent Arif Ahmed summarizes, is to "do what you most want to learn that you will do."

To a critic rooted in causal intuition—such as David Lewis or James Joyce—this prescription appears paradoxical, even pathological. Lewis famously charged EDT with endorsing "an irrational policy of managing the news," while Joyce argued that rationality demands choosing acts based on causal efficacy rather than mere auspiciousness. Yet EDT possesses structural elegance and practical robustness: in environments where agents are correlated with other actors, predictors, or institutions, EDT routinely outperforms competitors that ignore non-causal statistical dependencies.

This essay develops a mathematically rigorous framework for EDT. We define its core optimization mechanism, examine its behavior on classic decision problems, contrast its handling of counterfactuals with Causal Decision Theory (CDT), address open formal ambiguities—notably the conditioning problem and confounding—and develop an operational recipe that allows a practitioner to evaluate unfamiliar decision setups.

---

## 2. Formal Foundations

### 2.1 The Probability Space and Jeffrey Desirability

Let $(\Omega, \mathcal{F}, P)$ be a subjective probability space representing the agent's beliefs over possible states of the world and consequences. In standard Savage-style decision theory, the world is partitioned cleanly into states $\mathcal{S}$, acts $\mathcal{A}$ mapping states to consequences, and outcomes $\mathcal{O}$. 

EDT, following Jeffrey's formulation, adopts an unstratified, propositional approach. Acts, states, and outcomes are all treated as elements (or propositions) within the same Boolean $\sigma$-algebra $\mathcal{F}$.

Let:
- $\mathcal{A} = \{A_1, A_2, \dots, A_n\} \subset \mathcal{F}$ be an exhaustive set of mutually exclusive propositions corresponding to available actions.
- $\mathcal{O} = \{O_1, O_2, \dots, O_m\} \subset \mathcal{F}$ be a partition of mutually exclusive outcomes that completely describe everything the agent cares about.
- $D: \mathcal{O} \to \mathbb{R}$ be a bounded real-valued desirability (utility) function mapping outcomes to real numbers.

Gibbard and Harper (1976) defined the *evidential expected utility*—frequently referred to as the **V-value**—of an action $A \in \mathcal{A}$ as:

$$V(A) = \sum_{j=1}^m P(O_j \mid A) D(O_j)$$

where $P(O_j \mid A)$ denotes the standard Kolmogorov conditional probability:

$$P(O_j \mid A) = \frac{P(O_j \cap A)}{P(A)}, \quad \text{defined for } P(A) > 0.$$

If the outcome space $\mathcal{O}$ is continuous with a utility density or integrable utility function $u: \Omega \to \mathbb{R}$, this generalizes to the conditional expectation:

$$V(A) = \mathbb{E}_P [u(\omega) \mid A] = \int_\Omega u(\omega) \, dP(\omega \mid A).$$

The **EDT Choice Rule** is straightforward:

$$\operatorname{opt}_{\mathrm{EDT}}(\mathcal{A}) = \arg\max_{A \in \mathcal{A}} V(A).$$

### 2.2 EDT vs. CDT: Conditionals vs. Counterfactuals

The core mathematical distinction between EDT and Causal Decision Theory (CDT) centers on how conditioning is performed. Where EDT conditions on the indicative event that $A$ is true, CDT weights outcomes using counterfactual probabilities.

Gibbard and Harper defined the causal expected utility—the **U-value**—as:

$$U(A) = \sum_{j=1}^m P(A \mathbin{\Box\to} O_j) D(O_j)$$

where $A \mathbin{\Box\to} O_j$ is the Stalnaker-Lewis counterfactual conditional proposition: *"If action $A$ were performed, outcome $O_j$ would obtain."*

In modern causal inference (e.g., Pearl's do-calculus), this counterfactual expectation is equivalent to interventional conditioning:

$$U(A) = \mathbb{E}_P [u \mid \operatorname{do}(A)] = \sum_{j=1}^m P(O_j \mid \operatorname{do}(A)) D(O_j).$$

The divergence between the two paradigms can be stated in terms of conditional dependence:

$$\text{EDT} \neq \text{CDT} \iff \exists A \in \mathcal{A}, O_j \in \mathcal{O} \quad \text{such that} \quad P(O_j \mid A) \neq P(A \mathbin{\Box\to} O_j) \equiv P(O_j \mid \operatorname{do}(A)).$$

When an action $A$ is statistically correlated with an outcome $O_j$ via an upstream common cause, back-door path, or informational link, $P(O_j \mid A) \neq P(O_j \mid \operatorname{do}(A))$. EDT exploits this correlation; CDT truncates it by forcing an intervention that severs incoming causal arrows to $A$.

---

## 3. Benchmark Applications

### 3.1 Newcomb's Paradox

Newcomb's Paradox is the canonical arena for the clash between EDT and CDT. 

An agent faces two boxes:
- **Box A** is transparent and visibly contains $\$1{,}000$.
- **Box B** is opaque and contains either $\$1{,}000{,}000$ or $\$0$.

A reliable predictor has examined the agent beforehand:
- If the predictor anticipated the agent taking **only Box B** (one-boxing, $A_1$), they placed $\$1{,}000{,}000$ in Box B.
- If the predictor anticipated the agent taking **both Box A and Box B** (two-boxing, $A_2$), they left Box B empty.

The contents of Box B are physically fixed before the agent chooses. Let the predictor's reliability be $p \in (0.5, 1.0]$. Specifically, let:

$$P(M \mid A_1) = p, \quad P(\neg M \mid A_1) = 1 - p$$
$$P(M \mid A_2) = 1 - p, \quad P(\neg M \mid A_2) = p$$

where $M$ is the proposition that Box B contains $\$1{,}000{,}000$. 

Assuming a linear utility function $D(\$x) = x$:
- Under $A_1$, the agent receives $\$1{,}000{,}000$ if $M$ holds, and $\$0$ if $\neg M$ holds.
- Under $A_2$, the agent receives $\$1{,}001{,}000$ if $M$ holds, and $\$1{,}000$ if $\neg M$ holds.

#### The Evidential Calculation

$$V(A_1) = P(M \mid A_1) \cdot 1{,}000{,}000 + P(\neg M \mid A_1) \cdot 0 = 1{,}000{,}000 \cdot p$$

$$V(A_2) = P(M \mid A_2) \cdot 1{,}001{,}000 + P(\neg M \mid A_2) \cdot 1{,}000 = (1 - p)(1{,}001{,}000) + p(1{,}000)$$

For $p = 0.99$:
$$V(A_1) = 0.99 \times \$1{,}000{,}000 = \$990{,}000$$
$$V(A_2) = (0.01 \times \$1{,}001{,}000) + (0.99 \times \$1{,}000) = \$10{,}010 + \$990 = \$11{,}000$$

Since $V(A_1) > V(A_2)$, EDT prescribes choosing only Box B. The observation that you choose $A_1$ provides overwhelmingly good news about the pre-existing state of Box B.

#### The Causal Contrast

CDT reasons over fixed causal states: Box B either contains the million ($S_1 = M$) or it is empty ($S_2 = \neg M$). Because the past is causally settled, the action cannot causally influence the box contents:

$$P(A \mathbin{\Box\to} M) = P(M)$$

Evaluating the counterfactual payoffs:
$$U(A_1) = P(M) \cdot 1{,}000{,}000 + (1 - P(M)) \cdot 0 = 1{,}000{,}000 \, P(M)$$
$$U(A_2) = P(M) \cdot 1{,}001{,}000 + (1 - P(M)) \cdot 1{,}000 = 1{,}000{,}000 \, P(M) + 1{,}000$$

For any prior $P(M) \in [0, 1]$:
$$U(A_2) - U(A_1) = 1{,}000 > 0$$

CDT strictly dominates in favor of two-boxing: regardless of what is in Box B, taking both boxes nets $\$1{,}000$ more. Yet in a population of Newcomb players, EDT agents leave the room rich, while CDT agents leave the room with $\$1{,}000$.

```
                       Causal Graph of Newcomb's Paradox
                       
                              [ Predictor ]
                               /         \
                              /           \ (Past prediction)
                             v             v
                    [ Agent's Choice ]   [ Box B Content ]
                               \             /
                                \           /
                                 v         v
                                 [ Payoff ]

    CDT cuts the arrow Predictor -> Agent's Choice via do(Choice).
    EDT conditions on Choice, preserving the informational pathway:
            Choice <--- Predictor ---> Box B Content.
```

---

### 3.2 The Twin Prisoner's Dilemma

The power of evidential reasoning emerges vividly in non-cooperative game theory under symmetry.

Suppose agent $i$ faces an identical "psychological twin" $j$ in a Prisoner's Dilemma. The agents are separated and cannot causally communicate. The action space is $\{C, D\}$ for each agent. The payoff matrix (identical to Greene & Levinstein, 2020) is:

| | $C_j$ | $D_j$ |
|---|---|---|
| **$C_i$** | $(\$5, \$5)$ | $(\$0, \$10)$ |
| **$D_i$** | $(\$10, \$0)$ | $(\$1, \$1)$ |

Let $i$ assume that because $j$ uses the same algorithmic or cognitive structure, their decisions are perfectly correlated:

$$P(C_j \mid C_i) = 1, \quad P(D_j \mid C_i) = 0$$
$$P(D_j \mid D_i) = 1, \quad P(C_j \mid D_i) = 0$$

EDT evaluates the actions:
$$V(C_i) = P(C_j \mid C_i) \cdot 5 + P(D_j \mid C_i) \cdot 0 = 1 \cdot 5 + 0 \cdot 0 = 5$$
$$V(D_i) = P(C_j \mid D_i) \cdot 10 + P(D_j \mid D_i) \cdot 1 = 0 \cdot 10 + 1 \cdot 1 = 1$$

Since $V(C_i) > V(D_i)$, EDT prescribes cooperation. 

CDT, conversely, treats the twin's choice as an independent state of nature outside the agent's causal sphere of influence: $P(C_i \mathbin{\Box\to} C_j) = P(C_j)$. Because defecting strictly dominates cooperating under any fixed distribution over $\{C_j, D_j\}$, CDT forces defection, generating an outcome of $\$1$. 

EDT resolves the coordination dilemma without invoking magical thinking or backwards causation: it recognizes that one's choice is an informative diagnostic of what like-minded agents are doing across the universe.

---

## 4. Philosophical and Mathematical Challenges

Despite these successes, EDT encounters severe theoretical challenges that highlight deep questions in epistemology and probability kinematics.

### 4.1 The Confounding Dilemma: The Smoking Lesion

The standard counterexample leveled against EDT is the **Smoking Lesion** problem.

Suppose scientific consensus reveals:
1. Smoking ($S$) does not causally cause lung cancer ($C$).
2. Instead, an unobservable genetic lesion ($L$) causes both a predisposition to smoke and lung cancer:
   $$L \to S \quad \text{and} \quad L \to C.$$
3. Smoking provides mild sensory pleasure with utility $+1$. Lung cancer carries utility $-100$. Being healthy carries utility $0$.

```
                    Confounded Causal Graph (Smoking Lesion)
                    
                                [ Genetic Lesion (L) ]
                                    /           \
                                   /             \
                                  v               v
                            [ Smoking (S) ]    [ Cancer (C) ]
```

Because $L$ induces a positive correlation between $S$ and $C$, an agent observes:
$$P(C \mid S) \gg P(C \mid \neg S).$$

Computing the V-values:
$$V(S) = P(C \mid S)(-100) + P(\neg C \mid S)(0) + 1$$
$$V(\neg S) = P(C \mid \neg S)(-100) + P(\neg C \mid \neg S)(0) + 0$$

If $P(C \mid S) - P(C \mid \neg S) > 0.01$, then $V(\neg S) > V(S)$. EDT appears to command: *Do not smoke, because smoking is bad news about your genetics!*

Critics argue this is absurd. The lesion is either in your DNA or it is not. Refusing a cigarette does not repair your genome or remove the cancer risk. Lewis termed this the irrational desire to "manage the news."

#### The Tickle Defense (Eells' Resolution)

Evidentialists respond using the **Tickle Defense** (Ellery Eells, 1982). If the genetic lesion causes smoking, it must do so via a psychological intermediary—a subconscious craving, sensation, or "tickle" ($T$). 

If an agent has fully introspected, they already know whether they feel the tickle ($T$ or $\neg T$). Once the agent conditions on their own internal psychological state, the conditional correlation between smoking and the lesion vanishes due to conditional independence (screening off):

$$P(C \mid S \cap T) = P(C \mid \neg S \cap T) = P(C \mid T).$$

Letting $t$ be the agent's epistemic evidence regarding their desires, the expected utility becomes:

$$V(S \mid t) = P(C \mid t)(-100) + 1$$
$$V(\neg S \mid t) = P(C \mid t)(-100) + 0$$

Now, $V(S \mid t) > V(\neg S \mid t)$, and EDT permits smoking.

However, the Tickle Defense depends on an epistemic assumption: **complete introspective transparency**. If the agent's decision is influenced by subconscious factors not accessible as introspected "tickles," screening off fails, and the pathological recommendation returns.

---

### 4.2 The Conditioning Problem: Can an Agent Condition on Its Own Act?

The definition of $V(A)$ requires evaluating:

$$P(O \mid A) = \frac{P(O \cap A)}{P(A)}.$$

This formula requires $P(A) > 0$. But what is $P(A)$ from the first-person perspective of an agent actively deliberating whether to execute $A$?

Philosophers such as Spohn (1977) and Levi (1997) have argued that **deliberation crowds out prediction**: an agent cannot simultaneously deliberate about whether to do $A$ and assign an unconditional subjective probability $P(A) \in (0, 1)$ to doing it. If you believe your action is already fixed, deliberation is moot; if you are deciding, the choice cannot be treated as an already-distributed random variable.

If $P(A)$ is undefined during deliberation, $P(O \mid A)$ cannot be computed via Bayes' theorem.

---

### 4.3 Resolving the Ambiguities: Operationalization Proposal

The source document leaves open how EDT handles cases where conditional probabilities are undefined or when beliefs evolve during deliberation. Below, I develop an operational framework that resolves these ambiguities.

#### Definition: Deliberative Probability Perturbation (DPP)

To operationalize EDT mathematically for an arbitrary decision problem, we model the deliberating agent not as a static conditional distribution, but via an explicit **epistemic perturbation model**:

1. **Epistemic Base Space:** Let $\mathcal{K}$ represent the agent's background knowledge base, containing all structural models, correlational data, and historical observations.
2. **Trembling Deliberation:** For the purpose of evaluation, the agent assigns an infinitesimal prior probability $\epsilon > 0$ to every available option in the pure act set $\mathcal{A} = \{A_1, \dots, A_n\}$ such that $\sum_{i=1}^n P_\epsilon(A_i) = 1$ and $P_\epsilon(A_i) \ge \epsilon$.
3. **Operational V-Value:** The evidential value of an act is defined as the right-hand limit as $\epsilon \to 0^+$:

$$V^*(A) = \lim_{\epsilon \to 0^+} \mathbb{E}_{P_\epsilon} [u \mid A] = \lim_{\epsilon \to 0^+} \sum_{j} P_\epsilon(O_j \mid A) D(O_j).$$

#### The Screening Rule for Unfamiliar Problems

When applying EDT to a novel case, an analyst must establish the scope of conditioning. We propose the following operational rule:

> **The Full-Introspection Conditioning Principle (FICP):**  
> Let $\mathcal{I}_t$ be the total internal epistemic state (all beliefs, desires, memories, and sensory data) available to the agent at deliberation time $t$. The conditional probability governing action evaluation must always take the form:
> 
> $$P(O_j \mid A, \mathcal{I}_t).$$
> 
> If $O_j \perp\!\!\!\perp A \mid \mathcal{I}_t$, the problem reduces to a common-cause scenario where EDT agrees with CDT. If $O_j \not\perp\!\!\!\perp A \mid \mathcal{I}_t$, the correlation persists even after full introspection, and the decision must track the evidential news value.

---

## 5. Comparative Mathematical Case Study: The "Frustrated Artist"

To illustrate how to apply operationalized EDT to an unfamiliar decision problem, consider the following original case.

### Problem Formulation

Ren is an artist deciding whether to pursue a high-risk Avant-Garde project ($A$) or a Commercial design project ($C$). Ren's utility depends on two variables: financial return and intrinsic artistic genius ($G$). 

- Genius $G \in \{0, 1\}$ is an unalterable neurological trait: $P(G=1) = 0.10$.
- Intrinsic satisfaction from being a genius is valued at $100$ utils; non-genius is $0$ utils.
- Project outcomes yield the following payoffs (financial utils):
  - Avant-Garde ($A$): If $G=1$, it becomes a masterpiece ($+50$ utils). If $G=0$, it is a failure ($-20$ utils).
  - Commercial ($C$): Yields a reliable commercial income of $+10$ utils regardless of $G$.

Total utility is additive: $U = \text{Financial} + 100 \times \mathbb{I}_{\{G=1\}}$.

Crucially, an empirical study of artists shows that true geniuses almost always feel compelled to undertake Avant-Garde projects, whereas non-geniuses typically choose Commercial paths:
- $P(A \mid G=1) = 0.90 \implies P(C \mid G=1) = 0.10$
- $P(A \mid G=0) = 0.20 \implies P(C \mid G=0) = 0.80$

Ren does not know for certain whether they possess genius ($G=1$), but knows these population statistics. How should Ren choose?

### Execution under Operationalized EDT

#### Step 1: Compute Posterior Beliefs via Bayes' Rule

Ren computes the evidential import of learning that they have chosen $A$ versus $C$.

By Bayes' Rule:
$$P(G=1 \mid A) = \frac{P(A \mid G=1) P(G=1)}{P(A \mid G=1) P(G=1) + P(A \mid G=0) P(G=0)}$$

Substituting the values:
$$P(G=1 \mid A) = \frac{0.90 \times 0.10}{(0.90 \times 0.10) + (0.20 \times 0.90)} = \frac{0.09}{0.09 + 0.18} = \frac{0.09}{0.27} = \frac{1}{3} \approx 0.333$$

$$P(G=0 \mid A) = 1 - \frac{1}{3} = \frac{2}{3} \approx 0.667$$

Now for action $C$:
$$P(G=1 \mid C) = \frac{P(C \mid G=1) P(G=1)}{P(C \mid G=1) P(G=1) + P(C \mid G=0) P(G=0)}$$

$$P(G=1 \mid C) = \frac{0.10 \times 0.10}{(0.10 \times 0.10) + (0.80 \times 0.90)} = \frac{0.01}{0.01 + 0.72} = \frac{0.01}{0.73} \approx 0.0137$$

$$P(G=0 \mid C) = 1 - 0.0137 = 0.9863$$

#### Step 2: Compute Evidential Expected Utilities ($V$-values)

Under action $A$:
- If $G=1$, payoff is $50 + 100 = 150$.
- If $G=0$, payoff is $-20 + 0 = -20$.

$$V(A) = P(G=1 \mid A)(150) + P(G=0 \mid A)(-20)$$
$$V(A) = \left(\frac{1}{3} \times 150\right) + \left(\frac{2}{3} \times (-20)\right) = 50 - \frac{40}{3} = 50 - 13.33 = 36.67\text{ utils}$$

Under action $C$:
- If $G=1$, payoff is $10 + 100 = 110$.
- If $G=0$, payoff is $10 + 0 = 10$.

$$V(C) = P(G=1 \mid C)(110) + P(G=0 \mid C)(10)$$
$$V(C) = (0.0137 \times 110) + (0.9863 \times 10) = 1.507 + 9.863 = 11.37\text{ utils}$$

#### Step 3: Decision Prescription

Since $V(A) = 36.67 > V(C) = 11.37$, **EDT commands Ren to pursue the Avant-Garde project.** 

Choosing $A$ provides substantial news value: it elevates the probability that Ren is a genius from a baseline prior of $10\%$ up to $33.3\%$.

### The Causal Counterpart

How would CDT evaluate Ren's choice? Under CDT, the causal expectation treats $G$ as fixed:

$$U(A) = P(G=1)[50 + 100] + P(G=0)[-20 + 0] = 0.10(150) + 0.90(-20) = 15 - 18 = -3\text{ utils}$$
$$U(C) = P(G=1)[10 + 100] + P(G=0)[10 + 0] = 0.10(110) + 0.90(10) = 11 + 9 = +20\text{ utils}$$

CDT concludes: $U(C) = 20 > U(A) = -3$. **CDT commands Ren to choose the Commercial project.** 

CDT argues that choosing $A$ will not transform Ren into a genius; if Ren lacks genius, choosing $A$ simply wastes time and loses $20$ utils. EDT embraces the choice because an artist who chooses the commercial route virtually guarantees the depressing news that they are untalented.

---

## 6. The Evidentialist's Wager

A striking argument supporting EDT in applied settings is the **Evidentialist's Wager** (MacAskill et al., 2021). 

Suppose an agent is metacognitively uncertain about which decision theory is normative. They assign credence $\alpha \in (0, 1)$ to EDT and $(1 - \alpha)$ to CDT.

Consider a multi-agent coordination scenario or a cosmology containing infinitely many identical agents (or computational duplicates):
- If CDT is true, an agent's individual choice has only local causal reach (e.g., affecting only their immediate surroundings). The causal stakes are modest: $\mathcal{O}(1)$.
- If EDT is true, an agent's decision is correlated with the decisions of vast classes of identical or computationally symmetric agents across the cosmos. The evidential stakes scale with the entire correlation class: $\mathcal{O}(N)$ or $\mathcal{O}(\infty)$.

Under expected utility over normative theories (inter-theoretic evaluation):

$$\mathbb{E}[\text{Choice}] = \alpha \, V(\text{Choice}) + (1 - \alpha) \, U(\text{Choice}).$$

Because the stakes under evidential dependence can be astronomical—amplified by billions of correlated actors—the evidential term dominates the sum even for very small credences $\alpha$:

$$\lim_{N \to \infty} \frac{\alpha \cdot N \cdot V_{\text{unit}}}{\alpha \cdot N \cdot V_{\text{unit}} + (1 - \alpha) \cdot U_{\text{local}}} = 1.$$

Hence, under normative uncertainty, it is often rational to **act as if EDT were true**.

---

## 7. Systematic Guide: How to Solve Any Problem Using EDT

To analyze any unfamiliar decision problem using Evidential Decision Theory, apply this algorithmic procedure:

```
                  Step 1: Identify Act Partition A = {A_1, ..., A_n}
                                       |
                                       v
                  Step 2: Identify Payoff Partition O = {O_1, ..., O_m}
                          and assign Desirabilities D(O_j)
                                       |
                                       v
                  Step 3: Construct Epistemic Joint Prior P
                          over States, Acts, and Outcomes
                                       |
                                       v
                  Step 4: Check Introspective Conditioning
                          Condition on agent's known mental state I_t
                                       |
                                       v
                  Step 5: Compute Posterior Conditional Probabilities:
                          P(O_j | A_i, I_t) = P(O_j, A_i, I_t) / P(A_i, I_t)
                                       |
                                       v
                  Step 6: Calculate V-Value for Each Act:
                          V(A_i) = \sum_j P(O_j | A_i, I_t) * D(O_j)
                                       |
                                       v
                  Step 7: Prescribe Act Maximizing V(A_i)
```

1. **Formalize the Action Set:** Specify an exhaustive, mutually exclusive set of feasible actions $\mathcal{A} = \{A_1, \dots, A_n\}$.
2. **Define the Consequence Space:** Partition all possible outcomes into an exhaustive set $\mathcal{O} = \{O_1, \dots, O_m\}$ and specify the utility function $D: \mathcal{O} \to \mathbb{R}$.
3. **Establish Joint Belief Distribution:** Specify the prior probability distribution $P$ over the joint algebra generated by states, choices, and outcomes, reflecting all known correlations, predictors, and physical processes.
4. **Apply Introspective Screening (FICP):** Condition the joint distribution on the agent's current internal state $\mathcal{I}_t$. Determine whether the internal state screens off the correlation between the act and external states.
5. **Derive Posteriors:** For each candidate act $A_i$, compute the posterior distribution over outcomes:
   $$P(O_j \mid A_i, \mathcal{I}_t) = \frac{P(O_j \cap A_i \mid \mathcal{I}_t)}{P(A_i \mid \mathcal{I}_t)}.$$
   If $P(A_i \mid \mathcal{I}_t) = 0$, evaluate via the trembling limit $P_\epsilon(O_j \mid A_i, \mathcal{I}_t)$ as $\epsilon \to 0^+$.
6. **Compute News Value:** Calculate the evidential expected utility:
   $$V(A_i) = \sum_{j=1}^m P(O_j \mid A_i, \mathcal{I}_t) D(O_j).$$
7. **Select the Optimum:** Prescribe $A^* = \arg\max_{A_i \in \mathcal{A}} V(A_i)$.

---

## 8. Conclusion

Evidential Decision Theory offers a coherent, mathematically consistent framework that evaluates actions through the lens of conditional probability rather than counterfactual intervention. Where Causal Decision Theory isolates an agent from their statistical environment by treating actions as severed from historical and structural correlations, EDT treats the agent's choice as what it genuinely is: an informative data point within a linked universe.

While EDT faces intuitive resistance in common-cause scenarios like the Smoking Lesion—demanding sophisticated responses like the Tickle Defense or careful introspective conditioning—it demonstrates superior performance in Newcombian dilemmas, algorithmic coordination problems, and symmetrical games. By defining rationality through the optimization of news value, EDT provides an enduring benchmark for agents who understand that their choices do not merely modify the world—they reveal it.

---

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese*, 192(9), 2887–2899.
- Eells, E. (1982). *Rational Decision and Causality*. Cambridge University Press.
- Gibbard, A., & Harper, W. L. (1976). Counterfactuals and two kinds of expected utility. *CMSEMS Discussion Paper*, No. 194. Published in *Foundations and Applications of Decision Theory* (1978), 125–162.
- Greene, P., & Levinstein, B. (2020). Act consequentialism without free rides. *Philosophical Perspectives*, 34(1), 100–101.
- Jeffrey, R. C. (1965). *The Logic of Decision*. McGraw-Hill (2nd ed., University of Chicago Press, 1983).
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
- MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). The Evidentialist's Wager. *Global Priorities Institute Working Paper*.
- Wolpert, D. H., & Benford, G. (2013). The lesson of Newcomb's paradox. *Synthese*, 190(9), 1637–1646.