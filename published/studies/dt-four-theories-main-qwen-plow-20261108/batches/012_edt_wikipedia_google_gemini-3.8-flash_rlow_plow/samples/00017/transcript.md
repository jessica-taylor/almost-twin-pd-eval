# 012_edt_wikipedia_google_gemini-3.8-flash_rlow_plow / 00017

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/45c9681f-cfdc-4384-a0c0-69e48abcb387/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/45c9681f-cfdc-4384-a0c0-69e48abcb387/call_0/response.raw) · finish: `stop`

### Visible response

````text
# The Calculus of News Value: A Formal Exposition of Evidential Decision Theory

## 1. Introduction: Auspiciousness versus Efficacy

At the foundation of modern normative decision theory lies a core question: *When an agent deliberates, should she choose the action that causes the best outcomes, or the action whose occurrence would provide the best evidence about the world?*

Standard Bayesian decision analysis often treats these two criteria as interchangeable. In textbook settings—such as deciding whether to carry an umbrella given a weather forecast—the statistical correlations between an action and an outcome exist precisely because the action causally influences the outcome (or fails to influence a background state that is unconditionally independent of the choice). In non-trivial interactive, predictive, or symmetric environments, however, correlation and causation dramatically diverge.

**Evidential Decision Theory (EDT)** is the school of thought holding that rational agency consists entirely in maximizing *news value*. Formulated informally, EDT advises the agent to:

> *Do what you would be happiest to learn that you have done.*

If an observer were to inform you, after the fact, that you chose action $A$, how desirable would your world be in expectation? EDT asserts that this epistemic expectation is the sole criterion for rational choice. 

This posture stands in direct contrast to **Causal Decision Theory (CDT)**, which insists that rationality concerns *efficacy* rather than *auspiciousness*. As James M. Joyce famously put it, rational agents must choose acts to bring about good results, not merely to welcome the good news that favorable states of affairs obtain. Causalists, echoing David Lewis, accuse evidentialists of practicing an irrational policy of "managing the news."

This essay provides a rigorous mathematical exposition of Evidential Decision Theory. We will formalize its decision rule, trace the divergence between conditional and counterfactual probabilities, examine classic decision problems (including Newcomb’s Paradox and the Twin Prisoner’s Dilemma), scrutinize the theory's boundary conditions (such as the Medical Newcomb / Smoking Lesion problem and the Tickle Defense), and explore the modern decision-theoretic puzzle known as the Evidentialist’s Wager. Finally, we will propose an operational framework for conditioning on deliberate acts when standard conditional probability threatens to become ill-defined.

---

## 2. Formal Foundations

### 2.1 The Probability Space and State–Consequence Architecture

Let $(\Omega, \mathcal{F}, P)$ be a subjective probability space representing an agent’s beliefs about the world. We assume a finite or countably infinite partition of **actions** $\mathcal{A} = \{A_1, A_2, \dots, A_n\} \subset \mathcal{F}$, where each $A_i$ represents the proposition that the agent performs act $i$. We assume throughout that prior credences in actions are strictly positive: $P(A_i) > 0$ for all $i$, reserving discussion of zero-probability acts for Section 6.

Let $\mathcal{O} = \{O_1, O_2, \dots, O_m\} \subset \mathcal{F}$ be a mutually exclusive and exhaustive partition of **outcomes** (or consequences). The agent possesses a von Neumann–Morgenstern desirability (or utility) function:

$$D: \mathcal{O} \to \mathbb{R}$$

which maps each complete outcome $O_j$ to a real-valued payoff.

### 2.2 The EDT Expected Utility: $V(A)$

Following the seminal distinction articulated by Allan Gibbard and William Harper (1976), the evidential expected utility (conventionally denoted $V$) of an action $A \in \mathcal{A}$ is computed via standard conditional probability:

$$V(A) = \sum_{j=1}^m P(O_j \mid A) D(O_j)$$

where:

$$P(O_j \mid A) = \frac{P(O_j \cap A)}{P(A)}$$

The **Evidential Decision Rule** is straightforward:

$$A^*_{\text{EDT}} = \arg\max_{A \in \mathcal{A}} V(A)$$

If multiple actions achieve the maximum, the agent is indifferent among them.

### 2.3 Contrast with Causal Decision Theory: $U(A)$

To see why $V(A)$ is distinctive, consider the causal alternative. CDT evaluates an action not by conditioning on its occurrence, but by evaluating the distribution over outcomes across counterfactual branches of reality where $A$ is forced to occur. 

Using the Stalnaker–Lewis counterfactual conditional $A \ \square\to O_j$ ("if $A$ were chosen, $O_j$ would obtain"), Gibbard and Harper express the causal expected utility $U(A)$ as:

$$U(A) = \sum_{j=1}^m P(A \ \square\to O_j) D(O_j)$$

Alternatively, under Judea Pearl’s causal modeling framework, this can be written via the $do$-operator:

$$U(A) = \sum_{j=1}^m P(O_j \mid do(A)) D(O_j)$$

The central divergence between EDT and CDT reduces to a single mathematical inequality:

$$P(O_j \mid A) \neq P(A \ \square\to O_j) \quad \big[\text{or } P(O_j \mid A) \neq P(O_j \mid do(A))\big]$$

When an act $A$ shares a common cause with an outcome $O_j$, or when $A$ is correlated with a pre-existing state of the world through a reliable predictor, conditioning on $A$ transmits diagnostic information about that state. Intervening on $A$ (or evaluating the counterfactual $A \ \square\to O_j$) severs the incoming evidential arrows, holding the background state fixed.

```
       Causal (CDT) Evaluation:              Evidential (EDT) Evaluation:
       
         [Common Cause / State S]               [Common Cause / State S]
              /            \                         /            \
             v              v                       v              v
        [Action A]     [Outcome O]             [Action A] <......> [Outcome O]
            |                                       \              ^
            +==================>                     +=============+
              Causal link only                      Total correlation
            (Ignores S <- A path)                 (Updates along S <- A)
```

---

## 3. Canonical Applications

To observe the mechanics of EDT, we analyze two classic decision problems highlighted in the philosophical literature: Newcomb's Paradox and the Twin Prisoner's Dilemma.

### 3.1 Newcomb's Paradox

An agent is presented with two boxes:
- **Box A**: Transparent, containing $\$1,000$.
- **Box B**: Opaque, containing either $\$1,000,000$ or $\$0$.

The agent can choose between two acts:
1. $A_1$: Take **only Box B** ("one-boxing").
2. $A_2$: Take **both Box A and Box B** ("two-boxing").

A superintelligent predictor has already placed $\$1,000,000$ in Box B if and only if it predicted that the agent would choose $A_1$. If it predicted $A_2$, Box B was left empty. The prediction was completed yesterday; the physical contents of the boxes are currently immutable.

Let $S_1$ be the state where Box B contains $\$1,000,000$, and $S_0$ be the state where Box B is empty. Suppose the agent assigns credence $p = 0.99$ to the predictor's accuracy:

$$P(S_1 \mid A_1) = 0.99, \quad P(S_0 \mid A_1) = 0.01$$
$$P(S_0 \mid A_2) = 0.99, \quad P(S_1 \mid A_2) = 0.01$$

Assuming linear utility in money ($D(\$x) = x$), we calculate the evidential values:

$$\begin{aligned}
V(A_1) &= P(S_1 \mid A_1) D(\$1,000,000) + P(S_0 \mid A_1) D(\$0) \\
&= 0.99 \times 1,000,000 + 0.01 \times 0 = \$990,000
\end{aligned}$$

$$\begin{aligned}
V(A_2) &= P(S_1 \mid A_2) D(\$1,001,000) + P(S_0 \mid A_2) D(\$1,000) \\
&= 0.01 \times 1,001,000 + 0.99 \times 1,000 \\
&= 10,010 + 990 = \$11,000
\end{aligned}$$

Because $V(A_1) \gg V(A_2)$, **EDT unambiguously prescribes one-boxing ($A_1$)**.

#### The CDT Divergence
CDT reasons that the state of Box B is causally independent of the agent's current choice: 

$$P(A_1 \ \square\to S_k) = P(A_2 \ \square\to S_k) = P(S_k)$$

Thus:

$$U(A_2) - U(A_1) = D(\$1,000) > 0$$

Regardless of the prior $P(S_1)$, two-boxing strictly dominates in causal expected utility. CDT takes both boxes and leaves with $\$1,000$ (since the predictor foresaw this), while the EDT agent departs with $\$1,000,000$.

### 3.2 The Twin Prisoner's Dilemma

Consider Aomame and her psychological twin, placed in separate rooms with no means of communication. Each must choose to **Cooperate ($C$)** or **Defect ($D$)**. The payoffs are:
- Both Cooperate: $\$5$ each.
- Both Defect: $\$1$ each.
- One Cooperates, the other Defects: Defector gets $\$10$, Cooperator gets $\$0$.

Let $C_T$ and $D_T$ denote the Twin's actions. Because the Twin is psychological clone running identical algorithmic and cognitive procedures, Aomame believes their choices are tightly correlated. In the idealized symmetric case:

$$P(C_T \mid C) = 1 - \epsilon, \quad P(D_T \mid C) = \epsilon$$
$$P(D_T \mid D) = 1 - \epsilon, \quad P(C_T \mid D) = \epsilon$$

For $\epsilon = 0$ (perfect symmetry):

$$V(C) = 1 \cdot D(\$5) + 0 \cdot D(\$0) = 5$$
$$V(D) = 0 \cdot D(\$10) + 1 \cdot D(\$1) = 1$$

Since $V(C) > V(D)$, **EDT commands cooperation**. 

CDT, by contrast, observes that Aomame's physical outputs cannot causally influence the Twin across space-like separation:

$$P(C \ \square\to C_T) = P(D \ \square\to C_T) = P(C_T)$$

For any fixed probability $q = P(C_T)$, CDT calculates:

$$U(D) - U(C) = [10q + 1(1-q)] - [5q + 0(1-q)] = 5q + (1-q) = 1 + 4q > 0$$

CDT defects, earning $\$1$, whereas two EDT agents earn $\$5$ each.

---

## 4. The Classic Counterargument: The Smoking Lesion and the Tickle Defense

The primary indictment against EDT in the 20th-century literature is the **Smoking Lesion Problem** (often called the Medical Newcomb Problem).

### 4.1 The Setup
Suppose an unobservable genetic lesion $L$ causes two distinct effects:
1. It strongly predisposes an individual to smoke ($S$).
2. It causes fatal lung cancer ($C$).

Smoking itself does *not* causally contribute to cancer; it is an inert side-effect of $L$. The causal graph is a classic fork:

```
          [Genetic Lesion L]
              /        \
             v          v
       [Smoking S]   [Cancer C]
```

Suppose:
- $D(\text{Smoking}, \neg C) = 10$
- $D(\text{No Smoking}, \neg C) = 0$
- $D(\text{Smoking}, C) = -100$
- $D(\text{No Smoking}, C) = -110$

Smoking provides an intrinsic pleasure of $+10$ utils across all states. Cancer imposes a penalty of $-110$ utils. 

However, because smoking is correlated with the lesion, $P(C \mid S) \gg P(C \mid \neg S)$. For instance, let:

$$P(C \mid S) = 0.85, \quad P(C \mid \neg S) = 0.15$$

Evaluating evidential expected utilities:

$$\begin{aligned}
V(S) &= 0.85 \times (-100) + 0.15 \times 10 = -85 + 1.5 = -83.5 \\
V(\neg S) &= 0.15 \times (-110) + 0.85 \times 0 = -16.5
\end{aligned}$$

Because $V(\neg S) > V(S)$, **EDT advises the agent not to smoke**, even though smoking is completely harmless and provides an unconditional utility boost of $+10$. 

To critics like Lewis and Joyce, this recommendation is pathological: the agent foregoes a pleasant cigarette merely to suppress evidence that they have an incurable genetic condition.

### 4.2 The Tickle Defense
Evidentialists—beginning with Ellery Eells (1982)—responded with the **Tickle Defense**. 

Eells argues that a genetic lesion cannot compel a rational agent to act without manifesting in the agent's internal mental state. Before deciding to smoke, the agent experiences a conscious psychological desire, urge, or physiological "tickle" ($T$). 

Once the agent introspects and conditions on the presence of the tickle $T$, the act of smoking becomes conditionally independent of the lesion:

$$P(L \mid T \cap S) = P(L \mid T \cap \neg S) = P(L \mid T)$$

Under the Markov property with respect to the agent’s conscious epistemic state:

$$P(C \mid T \cap S) = P(C \mid T \cap \neg S)$$

Consequently, holding the introspection fixed:

$$\begin{aligned}
V(S \mid T) &= P(C \mid T) D(\text{Smoking}, C) + P(\neg C \mid T) D(\text{Smoking}, \neg C) \\
&= P(C \mid T)(-100) + [1 - P(C \mid T)](10) \\
&= 10 - 110 P(C \mid T)
\end{aligned}$$

$$\begin{aligned}
V(\neg S \mid T) &= P(C \mid T) D(\text{No Smoking}, C) + P(\neg C \mid T) D(\text{No Smoking}, \neg C) \\
&= P(C \mid T)(-110) + [1 - P(C \mid T)](0) \\
&= -110 P(C \mid T)
\end{aligned}$$

Thus:

$$V(S \mid T) - V(\neg S \mid T) = 10 > 0$$

When the tickle is properly conditioned upon, the evidential link between the choice and the cancer vanishes, and EDT agrees with CDT: the agent should smoke.

#### Fragility of the Tickle Defense
The tickle defense relies entirely on the assumption of **cognitive screening**: that the agent's internal credences can fully screen off their ultimate decisions from non-causal common ancestors. If an agent does not have transparent access to their subconscious impulses, or if the predictor in Newcomb's problem models the agent's final deliberate calculation better than the agent can introspect in real time, screening off fails. In that case, EDT continues to recommend managing the news.

---

## 5. Global Stakes: The Evidentialist's Wager

A compelling modern argument in favor of adopting EDT in practice, even for agents who place low prior probability on its philosophical correctness, is **The Evidentialist's Wager** (MacAskill et al., 2021).

### 5.1 Formulation of the Wager
Suppose an agent faces normative uncertainty regarding whether EDT or CDT is the correct theory of practical rationality. Let the agent assign meta-credence:

$$P(\text{EDT is true}) = \alpha, \quad P(\text{CDT is true}) = 1 - \alpha \quad (0 < \alpha < 1)$$

Consider an asymmetric choice environment:
- Under CDT, your action affects only your local environment, yielding bounded payoffs bounded by $[-M, M]$.
- Under EDT, your action correlates with the actions of a vast ensemble of similar decision-makers across the universe (e.g., cosmological twins, other rational agents facing equivalent dilemmas in distant galaxies, or future artificial minds running identical reasoning routines).

Let the number of correlated agents be $N$. Under EDT, choosing the cooperative act $C$ provides evidence that all $N$ agents also choose $C$, producing an aggregate payoff proportional to $N \cdot u(C)$. Under CDT, your unilateral deviation affects only your individual payoff, scaling as $1 \cdot u(D)$.

As $N \to \infty$:

$$\mathbb{E}_{\text{normative}}[U(C)] = \alpha \cdot \mathcal{O}(N) + (1-\alpha) \cdot \mathcal{O}(1)$$
$$\mathbb{E}_{\text{normative}}[U(D)] = \alpha \cdot \mathcal{O}(1) + (1-\alpha) \cdot \mathcal{O}(1)$$

For sufficiently large $N$:

$$\mathbb{E}_{\text{normative}}[U(C)] \gg \mathbb{E}_{\text{normative}}[U(D)]$$

Even if $\alpha = 0.001$, the evidential leverage across correlated populations dwarfs the bounded causal benefits of defection. Consequently, an agent under normative uncertainty should act as if EDT were true whenever correlated multi-agent decisions are at stake.

---

## 6. Mathematical and Operational Open Questions

The standard definition of EDT presented in the reference literature:

$$V(A) = \sum_j P(O_j \mid A) D(O_j)$$

leaves several mathematical and operational questions unresolved. Below, we formalize three of these ambiguities and propose constructive resolutions.

---

### Open Question 1: Conditioning on Null Acts ($P(A) = 0$)

#### The Problem
In standard Kolmogorov probability theory, conditional probability $P(O_j \mid A) = \frac{P(O_j \cap A)}{P(A)}$ is undefined if $P(A) = 0$. 

If an EDT agent initially assigns $P(A_k) = 0$ to an available physical option $A_k$ (perhaps believing it to be radically irrational or physically impossible), $V(A_k)$ cannot be computed via the standard Gibbard–Harper formula. This creates an epistemic trap: an agent cannot evaluate whether deviating to $A_k$ is optimal because the news value of doing so is mathematically undefined.

#### Operational Interpretation & Proposed Resolution
To make EDT globally well-defined over all candidate acts, we introduce **Popper functions** (or Rényi conditional probability spaces). 

Let a conditional probability structure be a primitive two-place function:

$$P: \mathcal{F} \times (\mathcal{F} \setminus \emptyset) \to [0, 1]$$

satisfying the standard axioms of conditional probability even when the conditioning event has zero unconditional probability. 

Alternatively, we can operationalize this via a **trembling-hand regularization** (familiar from Selten’s game-theoretic equilibria). Let the deliberate policy space be perturbed by an $\epsilon$-mixture over all available actions $\mathcal{A}$:

$$P_\epsilon(A_i) = (1 - \epsilon) \pi(A_i) + \frac{\epsilon}{|\mathcal{A}|}, \quad \epsilon > 0$$

where $\pi(A_i)$ is the agent's nominal policy. The evidential utility is then evaluated in the limit:

$$V^*(A) \equiv \lim_{\epsilon \to 0^+} \sum_{j=1}^m P_\epsilon(O_j \mid A) D(O_j)$$

This guarantees that the conditional distribution $P(O_j \mid A)$ is derived from the structural support of the agent's epistemic world-model rather than collapsing into division by zero.

---

### Open Question 2: The Deliberation Crowds Out Prediction Problem

#### The Problem
Can an agent maintain non-trivial credences $P(A)$ in their own actions *during* the process of deliberation?

Under the philosophical principle that **"deliberation crowds out prediction"** (Levi, Spohn), an agent cannot simultaneously deliberate about whether to do $A$ and hold a settled subjective credence that they *will* do $A$. If an agent does not yet know what they will do, assigning a well-defined joint distribution $P(A \cap O_j)$ during deliberation threatens cognitive incoherence. 

Conversely, if the agent's deliberation leads them to conclude that $A_1$ is the unique rational choice, does their credence $P(A_1)$ immediately jump to $1$? If $P(A_1) = 1$, then for any alternative action $A_2$, $P(A_2) = 0$, sending us straight back to Open Question 1.

#### Operational Interpretation & Proposed Resolution
We can formalize deliberation in EDT as a fixed-point process over an agent’s policy mixed strategy $\mathbf{p} = (p_1, \dots, p_n) \in \Delta^{n-1}$, where $p_i = P(A_i)$.

1. The agent maintains an internal predictive model $P(O_j \mid A_i)$ that maps hypothetical action selections to outcome probabilities.
2. The agent treats $A_i$ as an epistemic hypothesis: "Suppose the output of my deliberation algorithm is $A_i$."
3. Under this hypothesis, Bayes' theorem yields:

$$P(S_k \mid A_i) = \frac{P(A_i \mid S_k) P(S_k)}{\sum_l P(A_i \mid S_l) P(S_l)}$$

Here, $P(A_i \mid S_k)$ is the likelihood function representing the predictor's reliability (or the twin's symmetry) given background state $S_k$. 

This likelihood is fixed by the agent's model of the physics/psychology of the scenario and remains completely independent of the agent’s instantaneous credence in choosing $A_i$. Thus, the conditional expectation:

$$V(A_i) = \sum_k P(S_k \mid A_i) D(O(A_i, S_k))$$

is well-defined and invariant to the agent's dynamic deliberative uncertainty. Deliberation simply evaluates the vector $\mathbf{V} = (V(A_1), \dots, V(A_n))$ and outputs the policy concentrated entirely on $\arg\max_{i} V(A_i)$.

---

### Open Question 3: Dynamic Inconsistency and Evidential Traps

#### The Problem
Does EDT lead to dynamic inconsistency in sequential games with partial information?

Consider an agent who knows that taking action $A_1$ at time $t_1$ reveals that they have an unfavorable character trait (e.g., cowardice or low intelligence), even though $A_1$ provides an immediate physical reward. If the agent can commit at time $t_0$ before the choice arises, they might pay a costly penalty to bind their hands, avoiding the "bad news." 

Causalists charge that EDT agents are prone to paying money to remain ignorant or to restrict their future options solely to avoid self-incrimination.

#### Operational Interpretation & Proposed Resolution
Let us analyze an explicit two-stage decision tree:

```
                  [Stage 0: Commitment?]
                      /            \
           Commit (Pay $c)      Do Not Commit ($0)
                 /                      \
      Forced to choose A2           Stage 1: Choose
        (No bad news)               /            \
                                  A1              A2
                             (Gain $b,       (Gain $0,
                             Bad News)       No Bad News)
```

Suppose:
- State $S_B$: Agent has a bad genetic trait ($P(S_B) = 0.5$).
- State $S_G$: Agent has a good genetic trait ($P(S_G) = 0.5$).
- Trait $S_B$ creates a strong temptation to choose $A_1$ (which pays $+b$).
- The desirability is $D(\text{Outcome}) = \text{Wealth} + D(\text{Trait})$, where $D(S_G) = +100$ and $D(S_B) = 0$.

If the agent does not commit, and at Stage 1 chooses $A_1$, they learn bad news: $P(S_B \mid A_1) \approx 1$. 

Can an EDT agent pay a cost $c$ at Stage 0 to remove the option $A_1$?
- If the agent commits to $A_2$ at Stage 0, does *the act of committing itself* constitute bad news?
- Crucially, yes: if only individuals with trait $S_B$ have an incentive to bind their hands, then choosing to commit at Stage 0 provides the exact same bad news:

$$P(S_B \mid \text{Commit}) \approx 1$$

Under a fully specified EDT model, **the agent cannot escape the informational shadow of their meta-choices**. Any action taken to avoid bad news is itself an action that signals the underlying condition. 

Once this higher-order informational equilibrium is modeled, EDT agents do not waste resources on superficial self-censorship unless the commitment mechanism truly breaks the diagnostic correlation with the underlying state.

---

## 7. Comparative Summary: EDT vs. CDT

The following table summarizes the structural differences across key decision paradigms:

| Dimension | Evidential Decision Theory (EDT) | Causal Decision Theory (CDT) |
| :--- | :--- | :--- |
| **Guiding Maxim** | "Choose the act that signals the best outcome." | "Choose the act that causally produces the best outcome." |
| **Mathematical Metric** | $V(A) = \sum_j P(O_j \mid A) D(O_j)$ | $U(A) = \sum_j P(A \ \square\to O_j) D(O_j) = \sum_j P(O_j \mid do(A)) D(O_j)$ |
| **Newcomb’s Paradox** | **One-box**: $V(\text{One-box}) \approx \$990,000$ | **Two-box**: $U(\text{Two-box}) - U(\text{One-box}) = \$1,000$ |
| **Twin Prisoner's Dilemma** | **Cooperate**: Correlated play signals mutual cooperation. | **Defect**: Unilateral play cannot causally influence twin. |
| **Smoking Lesion** | **Don't Smoke** (without Tickle Defense); **Smoke** (with Tickle Defense). | **Smoke**: Smoking has no causal link to cancer. |
| **Treatment of Correlations** | Treats all statistical dependencies symmetrically via conditioning. | Screens out non-causal confounding correlations. |
| **Dominance Principle** | Rejects causal dominance when states are action-dependent. | Strictly respects causal state-dominance. |

---

## 8. Conclusion

Evidential Decision Theory offers an elegant and mathematically parsimonious foundation for rational agency: expected utility is simply conditional expectation. It dispenses with primitive counterfactual conditionals, causal directed acyclic graphs, and non-observational interventions ($do$-calculus), deriving the value of an action directly from standard probability theory.

Its prescriptions align with deep intuitions in symmetric dilemmas: EDT agents emerge as rich Newcomb-problem winners and successful cooperators in Twin Prisoner's Dilemmas, outperforming their causalist peers in environments populated by predictive algorithms or structural peers.

Yet, this power comes at a clear philosophical cost. When unshielded by the Tickle Defense, EDT conflates correlation with causation, prescribing that agents act to "suppress bad symptoms" rather than cure diseases. 

Ultimately, EDT forces us to confront a fundamental question about the nature of choice: Is deliberation an intervention upon the world from the outside, or is the deliberating agent simply an epistemic node within the world, updating her forecast of reality as her choice unfolds? For the evidentialist, you are inseparable from your news—and the highest form of rationality is to become the best possible evidence for the universe you wish to inhabit.

---

## References

1. Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
2. Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese*, 192(9), 2887–2899.
3. Eells, E. (1982). *Rational Decision and Causality*. Cambridge University Press.
4. Gibbard, A., & Harper, W. L. (1976). Counterfactuals and two kinds of expected utility. *CMSEMS Discussion Paper*, No. 194.
5. Greene, P., & Levinstein, B. (2020). Act consequentialism without free rides. *Philosophical Perspectives*, 34(1), 100–101.
6. Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
7. Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
8. MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). *The Evidentialist's Wager*. Global Priorities Institute Working Paper.
9. Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.
10. Wolpert, D. H., & Benford, G. (2013). The lesson of Newcomb's paradox. *Synthese*, 190(9), 1637–1646.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/295ba09d-7df1-4215-b857-edc1acd6a35a/call_0/request.json)

[Authoritative raw response](../../../../../../runs/295ba09d-7df1-4215-b857-edc1acd6a35a/call_0/response.raw) · finish: `stop`

### Visible response

````text
```text
pass
```
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/295ba09d-7df1-4215-b857-edc1acd6a35a/call_1/request.json)

[Authoritative raw response](../../../../../../runs/295ba09d-7df1-4215-b857-edc1acd6a35a/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
