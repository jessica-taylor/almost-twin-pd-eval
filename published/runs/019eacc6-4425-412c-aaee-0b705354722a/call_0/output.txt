# Evidential Decision Theory: Formalism, News Value, and Dependencies

In the landscape of formal decision theory, rational choice is typically framed as the maximization of expected utility. Beneath this apparent consensus, however, lies a fundamental divide over how an agent’s potential actions relate to states of the world. What does it mean for an action to make an outcome likely? 

**Evidential Decision Theory (EDT)** answers this question epistemically: an agent should select an action that serves as the best *evidence* for a desirable outcome. Colloquially, EDT instructs an agent to *do what they would most like to learn that they have done*—maximizing what philosophers call the "news value" of their act. 

This essay provides a self-contained, mathematically rigorous account of EDT. We will formalize its decision calculus, contrast it with Causal Decision Theory (CDT), examine its application to benchmark problems, and address open technical and philosophical challenges—most notably the problem of confounding, the "Tickle Defense," and the status of counterfactual conditionals.

---

## 1. Formal Foundations

### 1.1 The Probability Space and Outcomes
Let $(\Omega, \mathcal{F}, P)$ be a subjective probability space representing an agent’s credences over possible worlds, where:
- $\mathcal{A} = \{A_1, A_2, \dots, A_n\} \subset \mathcal{F}$ is a finite, mutually exclusive, and exhaustive set of available **actions** (or acts), such that $P(A_i) > 0$ for each $i$.
- $\mathcal{O} = \{O_1, O_2, \dots, O_m\} \subset \mathcal{F}$ is a finite partition of **outcomes** (or consequences).
- $u: \mathcal{O} \to \mathbb{R}$ is a utility function (often denoted $D(O_j)$ for desirability) defined up to a positive affine transformation, capturing the agent's evaluations of final states.

In Richard Jeffrey’s framing of decision theory (and its formalization by Allan Gibbard and William Harper in 1976), actions and outcomes are elements of the very same algebra of propositions. An agent does not treat their own action as an exogenous intervention imposed from outside the probability model; rather, the action $A$ is an event within the model about which the agent can condition.

### 1.2 The Evidential Expected Utility
The evidential expected utility (or **news value**) of an action $A \in \mathcal{A}$, denoted $V(A)$, is defined as the conditional expectation of utility given that $A$ is realized:

$$V(A) = \mathbb{E}_P[u \mid A] = \sum_{j=1}^m P(O_j \mid A)\, u(O_j)$$

where $P(O_j \mid A)$ denotes standard Kolmogorov conditional probability:

$$P(O_j \mid A) = \frac{P(O_j \cap A)}{P(A)}$$

The **Evidential Decision Rule** prescribes choosing an act $A^* \in \mathcal{A}$ that maximizes news value:

$$A^* \in \arg\max_{A \in \mathcal{A}} V(A)$$

If outcomes are determined by the conjunction of an act $A$ and an external state of the world $S_k \in \mathcal{S} = \{S_1, \dots, S_r\}$, where each pair $(A_i, S_k)$ deterministically leads to an outcome $O(A_i, S_k)$, equation (1) expands to:

$$V(A) = \sum_{k=1}^r P(S_k \mid A)\, u(O(A, S_k))$$

Crucially, in EDT the probability distribution over states $\mathcal{S}$ is **action-dependent** via epistemic conditioning: $P(S_k \mid A) \neq P(S_k)$ whenever an act supplies information regarding the world's state.

---

## 2. EDT vs. CDT: Conditionals and Counterfactuals

The core debate in modern normative decision theory is between EDT and Causal Decision Theory (CDT). The divergence traces directly to the mathematical mechanism used to evaluate dependencies.

### 2.1 The CDT Counterfactual Formulation
Following Gibbard and Harper (1976), CDT replaces the conditional probability $P(O_j \mid A)$ with the probability of a counterfactual conditional:

$$U(A) = \sum_{j=1}^m P(A \mathbin{\Box\rightarrow} O_j)\, u(O_j)$$

The counterfactual proposition $A \mathbin{\Box\rightarrow} O_j$ is typically read: *"If action $A$ were chosen, outcome $O_j$ would obtain."* In Lewis-Stalnaker semantics, this proposition is true at a world $w$ if $O_j$ holds at the closest possible world(s) to $w$ where $A$ is true. 

In causal graph terminology (following Judea Pearl), CDT corresponds to intervening on the system. If the decision situation is represented as a directed acyclic graph (DAG), CDT replaces conditioning $P(\cdot \mid A)$ with the causal do-calculus operator $P(\cdot \mid \mathrm{do}(A))$, severing all incoming causal edges to $A$:

$$U_{\mathrm{CDT}}(A) = \sum_{j=1}^m P(O_j \mid \mathrm{do}(A))\, u(O_j)$$

### 2.2 The Divergence
By definition:
- $P(O_j \mid A)$ reflects **correlation**: both causal influence ($A \to O_j$) and common causes ($A \leftarrow C \to O_j$).
- $P(A \mathbin{\Box\rightarrow} O_j) = P(O_j \mid \mathrm{do}(A))$ isolates **causal efficacy**: it filters out back-door paths where $A$ merely symptoms an unobserved common cause.

When the state of the world $S$ is causally independent of act $A$, CDT asserts $P(A \mathbin{\Box\rightarrow} S_k) = P(S_k)$. Thus:

$$U_{\mathrm{CDT}}(A) = \sum_{k=1}^r P(S_k)\, u(O(A, S_k))$$

EDT does not permit this simplification if $P(S_k \mid A) \neq P(S_k)$. To an evidentialist, if performing $A$ provides statistical evidence that $S_k$ holds, that information must be incorporated into the expected payoff.

| Feature | Evidential Decision Theory (EDT) | Causal Decision Theory (CDT) |
| :--- | :--- | :--- |
| **Probability metric** | Epistemic conditional: $P(O \mid A)$ | Counterfactual / Causal: $P(A \mathbin{\Box\rightarrow} O)$ or $P(O \mid \mathrm{do}(A))$ |
| **Foundational axiom** | Jeffrey-Bolker desirability | Savage / Gibbard-Harper / Lewis |
| **Statistical focus** | Correlation / News value | Direct causal control |
| **Newcomb’s Paradox** | One-box ($B$) | Two-box ($A + B$) |
| **Twin Prisoner's Dilemma** | Cooperate | Defect |

---

## 3. Classic Decision Problems

### 3.1 Newcomb's Paradox
A predictor of near-perfect accuracy (say, $p = 0.99$) places $\$1{,}000{,}000$ in an opaque Box $B$ if and only if it predicted that the agent will take *only* Box $B$. Otherwise, Box $B$ is left empty. A transparent Box $A$ always contains visible cash of $\$1{,}000$. The agent faces two choices:
1. $A_1$: Take only Box $B$ ("one-box").
2. $A_2$: Take both Box $A$ and Box $B$ ("two-box").

Let states be $S_1$ (predictor placed $\$1\text{M}$) and $S_0$ (predictor placed $\$0$). The contents are already fixed before the choice is executed. 

#### EDT Evaluation:
Assuming linear utility for money ($u(\$x) = x$):
- If the agent chooses $A_1$:
  $$P(S_1 \mid A_1) = 0.99, \quad P(S_0 \mid A_1) = 0.01$$
  $$V(A_1) = (0.99)(\$1{,}000{,}000) + (0.01)(\$0) = \$990{,}000$$

- If the agent chooses $A_2$:
  $$P(S_1 \mid A_2) = 0.01, \quad P(S_0 \mid A_2) = 0.99$$
  $$V(A_2) = (0.01)(\$1{,}001{,}000) + (0.99)(\$1{,}000) = \$10{,}010 + \$990 = \$11{,}000$$

Because $V(A_1) > V(A_2)$, EDT uniquely prescribes **one-boxing** ($A_1$).

#### CDT Contrast:
Because the prediction was completed in the past, the contents of Box $B$ are causally fixed. That is, $A \mathbin{\Box\rightarrow} S_k$ reduces to the prior probability that the money is there, independent of $A$:
$$U_{\mathrm{CDT}}(A_2) - U_{\mathrm{CDT}}(A_1) = \$1{,}000 > 0$$
CDT recommends **two-boxing**, arguing that taking Box $A$ cannot causally alter whether the million dollars is already sitting in Box $B$.

### 3.2 The Twin Prisoner's Dilemma
Consider two agents, Aomame and her psychological twin, held in separate rooms with no communication. Each can Cooperate ($C$) or Defect ($D$). The payoff matrix to Aomame is:

| | Twin Cooperates ($C_T$) | Twin Defects ($D_T$) |
|---|---|---|
| **Aomame Cooperates ($C$)** | $\$5$ | $\$0$ |
| **Aomame Defects ($D$)** | $\$10$ | $\$1$ |

The twin is structurally and psychologically identical to Aomame; their reasoning processes are tightly coupled. Consequently, Aomame assigns:
$$P(C_T \mid C) = 1 - \epsilon, \quad P(D_T \mid C) = \epsilon$$
$$P(C_T \mid D) = \delta, \quad P(D_T \mid D) = 1 - \delta$$
where $\epsilon, \delta \approx 0$. 

#### EDT Evaluation:
$$V(C) = (1 - \epsilon)(\$5) + \epsilon(\$0) \approx \$5$$
$$V(D) = \delta(\$10) + (1 - \delta)(\$1) \approx \$1$$

Because $V(C) > V(D)$, EDT recommends **cooperation**. Aomame’s choice serves as decisive evidence about how an identical mind resolves this exact decision dilemma.

#### CDT Contrast:
Because there is no physical or causal mechanism connecting Aomame’s physical motion to her twin's hand across isolated rooms, CDT sets $P(\mathrm{do}(C) \to C_T) = P(C_T)$. For any fixed state of the twin, defecting dominates cooperating by $\$5$ (if the twin cooperates) or by $\$1$ (if the twin defects). CDT demands **defection**.

---

## 4. The Smoking Lesion and Common-Cause Confounding

The most influential objection to EDT is the *Smoking Lesion problem* (and related medical scenarios), which critics cite to accuse EDT of magical thinking or "managing the news" (Lewis, 1981; Joyce, 1999).

### 4.1 The Problem Stated
Suppose an unobserved genetic defect, a *lesion* ($L$), independently causes both:
1. A strong predisposition to smoke ($S$).
2. The development of fatal lung cancer ($C$).

Smoking itself, in this hypothetical world, is biologically harmless; it has no direct causal impact on cancer ($S \not\to C$). However, because both share the common cause $L$, smoking is strongly correlated with cancer:
$$P(C \mid S) \gg P(C \mid \neg S)$$

Let the utility of enjoying tobacco be $+1$, cancer be $-100$, and health be $0$. 
Naively calculating news value:
$$V(S) = P(C \mid S)(-100) + 1$$
$$V(\neg S) = P(C \mid \neg S)(-100) + 0$$

If $P(C \mid S) - P(C \mid \neg S) > 0.01$, then $V(\neg S) > V(S)$. EDT appears to tell the agent to refrain from smoking, even though smoking does not cause cancer. Critics assert this is absurd: abstaining from an enjoyable cigarette simply to reassure oneself that one lacks a pre-existing genetic defect is irrational self-deception.

```
       Lesion (L)
       /        \
      v          v
Smoking (S)    Cancer (C)
```

---

## 5. Resolving the Dilemma: The Tickle Defense and Operational Extensions

Can an evidential decision theorist resist this conclusion? The reference text notes the challenge but leaves the formal resolution open. The classical evidentialist response is the **Tickle Defense**, originally proposed by Ellery Eells.

### 5.1 The Tickle Defense Formalized
The core insight is that an agent does not decide in an informational vacuum. If the genetic lesion $L$ causes a desire to smoke, it must do so via some introspectible intermediate state—a psychological urge, inclination, or physical "tickle" ($T$).

Once the agent inspects their own mind and becomes aware of their desires, their state of knowledge changes:
- Let $T$ represent the presence of the urge to smoke.
- The agent's decision to actually smoke ($S$) is mediated by $T$:
  $$L \longrightarrow T \longrightarrow S$$

Under the Markov condition on belief networks, conditional on the intermediate mental state $T$, the action $S$ becomes conditionally independent of the common cause $L$:
$$P(L \mid S \cap T) = P(L \mid \neg S \cap T)$$

Since cancer $C$ depends only on $L$, we have the screening-off relation:
$$P(C \mid S \cap T) = P(C \mid \neg S \cap T) = P(C \mid T)$$

#### Calculating Conditional News Value Under Self-Awareness:
When deciding, the agent already knows whether they feel the urge ($T$ or $\neg T$). Suppose the agent feels the urge $T$. The evidential values of smoking versus refraining are evaluated conditional on current total evidence:

$$V(S \mid T) = P(C \mid S \cap T) \cdot u(\text{Cancer}) + u(\text{Smoke})$$
$$V(\neg S \mid T) = P(C \mid \neg S \cap T) \cdot u(\text{Cancer}) + u(\text{No Smoke})$$

Using the screening-off condition $P(C \mid S \cap T) = P(C \mid \neg S \cap T)$:

$$V(S \mid T) - V(\neg S \mid T) = u(\text{Smoke}) - u(\text{No Smoke}) = +1 > 0$$

Once the agent conditions on their introspective awareness ($T$), smoking provides **zero additional evidence** regarding the lesion or cancer. EDT recommends smoking, correctly aligning with causal intuition without altering the evidential formula.

### 5.2 Failure of the Tickle Defense: Why Newcomb Resists It
Why does the Tickle Defense resolve the Smoking Lesion but preserve one-boxing in Newcomb's Paradox?
- **In the Smoking Lesion:** The action is merely an *effect* of the internal urge $T$. Once $T$ is known, $S$ contains no new information about $L$.
- **In Newcomb's Paradox:** The predictor does not merely predict the agent's preliminary urge; the predictor simulates the agent's **deliberation algorithm itself**. The output of that calculation *is* the choice $A$. The agent cannot "screen off" the final choice using a preliminary urge because the predictor's accuracy tracks the ultimate resolution of the choice. Hence, $P(\text{Box B has \$1M} \mid A_1) \neq P(\text{Box B has \$1M} \mid A_2)$ remains robust, even after conditioning on all prior internal states.

---

## 6. How to Apply EDT to Unfamiliar Cases: An Operational Protocol

To operationalize EDT for general decision problems, a decision-maker can apply the following systematic procedure:

```
[Step 1: Enumerate Actions A_i]
            │
            ▼
[Step 2: Formulate Partition of Ultimate Outcomes O_j]
            │
            ▼
[Step 3: Update Credences with Total Current Evidence E]
            │
            ▼
[Step 4: Compute Posterior Probabilities P(O_j | A_i, E)]
            │  (Check for common-cause screening off)
            ▼
[Step 5: Compute News Value V(A_i | E) = ∑ P(O_j | A_i, E) u(O_j)]
            │
            ▼
[Step 6: Select A* = argmax V(A_i | E)]
```

### Protocol Steps:

1. **Specify the Act Space:**  
   Define an exhaustive and mutually exclusive set of feasible actions $\mathcal{A} = \{A_1, \dots, A_n\}$.

2. **Partition the Outcome Space:**  
   Define outcomes $\mathcal{O} = \{O_1, \dots, O_m\}$ such that each outcome completely characterizes everything the agent cares about. Assign scalar utilities $u(O_j)$.

3. **Condition on Background Evidence ($E$):**  
   Identify all background information and internal introspective states available to the agent prior to acting: $E = \text{total current introspective evidence}$.

4. **Determine the Evidential Conditional Likelihoods:**  
   Compute $P(O_j \mid A_i \cap E)$ using Bayes’ rule or structural knowledge of the environment:
   $$P(O_j \mid A_i \cap E) = \frac{P(A_i \mid O_j \cap E) P(O_j \mid E)}{\sum_{k} P(A_i \mid O_k \cap E) P(O_k \mid E)}$$
   *Operational Check:* Check whether $A_i$ is conditionally independent of $O_j$ given $E$. If internal states in $E$ screen off the action from the outcome, the distribution collapses to $P(O_j \mid E)$.

5. **Calculate the News Value:**  
   $$V(A_i \mid E) = \sum_{j=1}^m P(O_j \mid A_i \cap E) \, u(O_j)$$

6. **Choose the Maximizer:**  
   Select $A^* = \arg\max_{A_i \in \mathcal{A}} V(A_i \mid E)$.

---

## 7. Open Problems and Contemporary Developments

### 7.1 Zero-Probability Acts and Deliberation
A standard mathematical limitation of conditional probability is conditioning on zero-measure events: $P(O \mid A) = \frac{P(O \cap A)}{P(A)}$ is undefined if $P(A) = 0$.

During deliberation, if an agent becomes convinced that they will *never* take an action $A_k$ ($P(A_k) = 0$), $V(A_k)$ ceases to be well-defined. This introduces the problem of unstable deliberation: an agent cannot evaluate alternatives they are certain they will not choose. 

To make EDT operationally robust against this failure mode, modern theorists employ:
- **Popper measures / Renyi conditional probability spaces**, where $P(\cdot \mid \cdot)$ is taken as a primitive two-place function defined even when the condition has prior probability zero.
- **$\epsilon$-Trembles:** The agent assigns a small strictly positive prior $P(A_i) \ge \epsilon > 0$ to every option, ensuring all news values remain computable during the cognitive process.

### 7.2 Sleeping Beauty and Self-Locating Beliefs
As indicated in the reference text, EDT plays a prominent role in anthropic reasoning and self-locating beliefs, particularly the *Sleeping Beauty problem*. 

- **The Setup:** Beauty is put to sleep on Sunday. A fair coin is tossed. If Heads, she is awakened only on Monday. If Tails, she is awakened on Monday and Tuesday, with her memory wiped between awakenings. When awakened, she is asked her credence in Heads.
- **The Debate:** "Halfers" maintain $P(\text{Heads}) = 1/2$; "Thirders" argue $P(\text{Heads}) = 1/3$.
- **EDT's Role:** It was suggested that halfers can avoid Dutch books (gambles guaranteeing a net loss) if they make decisions using EDT, because an awakening under Tails provides multiple opportunities to bet, amplifying the evidential weight of the action across time. However, as Vincent Conitzer (2015) demonstrated, halfers remain vulnerable to specific sequences of evidential Dutch books. The exact mapping between evidential conditioning and non-standard epistemic spaces (centered worlds) remains an active research frontier.

### 7.3 The Evidentialist's Wager
A compelling argument for EDT is *The Evidentialist's Wager* (MacAskill et al., 2021). Even if an agent assigns low credence to EDT being the metaphysically "correct" theory of rational agency compared to CDT, EDT actions often involve high-stakes correlations with massive numbers of correlated decision-makers across the universe (e.g., distant alien civilizations, simulation ancestors, or parallel multiverses running similar cognitive algorithms). 

Because the expected payoffs under correlated scenarios scale with the number of correlated agents, while CDT treats identical minds as isolated non-influences, the evidential stakes can completely dominate an agent's metatheoretic expected utility:

$$\mathbb{E}[\text{Action}] = P(\text{EDT}) \cdot V_{\text{EDT}}(A) + P(\text{CDT}) \cdot U_{\text{CDT}}(A)$$

If $V_{\text{EDT}}(A)$ involves millions of correlated agents while $U_{\text{CDT}}(A)$ only affects the local environment, the evidential calculation can dictate the agent's behavior even if $P(\text{EDT}) \ll P(\text{CDT})$.

---

## 8. Conclusion

Evidential Decision Theory offers a conceptually unified approach to rational action: treat your own decisions not as uncaused interventions from outside the universe, but as integral physical events correlated with the world through common causes, psychological similarities, and predictive models. 

While critics charge EDT with an irrational desire to "manage the news," its formal framework handles complex coordination dilemmas—such as Newcomb's Paradox and the Twin Prisoner's Dilemma—naturally where causal models demand counter-intuitive defection or losses. When augmented with introspective screening-off via the Tickle Defense, EDT distinguishes between mere diagnostic correlation and actionable epistemic relevance. For mathematical agents reasoning in multi-agent or predictable environments, EDT remains one of the most powerful, principled formalisms in the theory of choice.

---

## References

1. Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
2. Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese*, 192(9), 2887–2899.
3. Eells, E. (1982). *Rational Decision and Causality*. Cambridge University Press.
4. Gibbard, A., & Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*. CMSEMS Discussion Paper No. 194, Northwestern University.
5. Greene, P., & Levinstein, B. (2020). Act Consequentialism without Free Rides. *Philosophical Perspectives*, 34(1), 100–101.
6. Jeffrey, R. C. (1983). *The Logic of Decision* (2nd ed.). University of Chicago Press.
7. Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
8. Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
9. MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). *The Evidentialist's Wager*. Global Priorities Institute Working Paper.
10. Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.
11. Wolpert, D. H., & Benford, G. (2013). The lesson of Newcomb's paradox. *Synthese*, 190(9), 1637–1646.