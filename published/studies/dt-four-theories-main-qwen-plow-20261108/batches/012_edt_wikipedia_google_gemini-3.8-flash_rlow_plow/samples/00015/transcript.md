# 012_edt_wikipedia_google_gemini-3.8-flash_rlow_plow / 00015

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/f7383ec7-5da2-49b2-886a-83d2aad49ebb/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/f7383ec7-5da2-49b2-886a-83d2aad49ebb/call_0/response.raw) · finish: `stop`

### Visible response

````text
# Rationality as Good News: A Mathematical Exposition of Evidential Decision Theory

---

## 1. Introduction: The Core Intuition

Standard normative decision theory posits that a rational agent, facing an array of feasible actions, should maximize expected utility. But what expectation should be maximized? 

Consider an agent who steps outside into dense fog. She must choose whether to take an umbrella. In ordinary circumstances, taking an umbrella does not cause rain, nor does it provide evidence that the atmospheric pressure is low. However, suppose our agent is a somnambulist meteorologist who unconsciously checks barometric readings while asleep: if she reaches for her umbrella in the morning, that act is itself an extraordinarily accurate signal that it will rain. Does her choice merely reflect the weather, or does it matter whether her choice *causes* the rain?

This question marks the fault line between two major paradigms of formal decision theory:
1. **Evidential Decision Theory (EDT):** A rational agent chooses the action that yields the highest *news value*—the act that provides the strongest probabilistic evidence of a desirable outcome. Formally, it instructs an agent to maximize expected utility conditioned on the act: "Do what you would be happiest to learn that you have done" (Ahmed, 2021).
2. **Causal Decision Theory (CDT):** A rational agent chooses the action that is most efficacious in causally *bringing about* the best outcome, regardless of what the act portends about pre-existing, unalterable states of the world.

While standard classical contexts treat conditional and causal dependencies identically, thought experiments such as Newcomb's Paradox and the Twin Prisoner's Dilemma drive a wedge between them. This essay develops a rigorous mathematical account of EDT, formalizes its evaluative machinery, explores how it handles statistical dependencies and counterfactuals, confronts its standard criticisms, and addresses its open operational dilemmas.

---

## 2. Formal Framework: News Value and the Gibbard–Harper Formulation

Let $(\Omega, \mathcal{F}, P)$ be a subjective probability space representing the agent's epistemic state:
* $\Omega$ is the set of possible worlds.
* $\mathcal{F}$ is a $\sigma$-algebra of propositions (events).
* $P: \mathcal{F} \to [0, 1]$ is a countably additive subjective probability measure encoding the agent's credences.

Let $\mathcal{A} = \{A_1, A_2, \dots, A_m\} \subset \mathcal{F}$ be a finite set of mutually exclusive and exhaustive propositions corresponding to the agent's available **actions**, with $P(A_i) > 0$ for all $i$. Let $\mathcal{O} = \{O_1, O_2, \dots, O_n\} \subset \mathcal{F}$ be a partition of mutually exclusive and exhaustive **outcomes**.

The agent's preferences over outcomes are represented by a utility function (often referred to as a desirability function, following Richard Jeffrey and Allan Gibbard & William Harper):
$$D: \mathcal{O} \to \mathbb{R}$$

### 2.1 The EDT Objective Function

Following the classical formulation articulated by Gibbard and Harper (1976), the evidential value—or *desirability* $V(A)$—of an act $A \in \mathcal{A}$ is defined as the conditional expectation of desirability:

$$\boxed{V(A) = \sum_{j=1}^n P(O_j \mid A) D(O_j)}$$

where $P(O_j \mid A) = \frac{P(O_j \cap A)}{P(A)}$ denotes the standard Kolmogorov conditional probability.

Under EDT, an optimal action $A^*_{\text{EDT}}$ satisfies:
$$A^*_{\text{EDT}} \in \arg\max_{A \in \mathcal{A}} V(A)$$

If outcomes are refined such that an outcome proposition is the conjunction of an action $A$ and a state of the world $S_k \in \mathcal{S}$ (where $\mathcal{S} = \{S_1, \dots, S_K\}$ forms a partition of states), we have $O_{jk} = A \cap S_k$. Then:
$$V(A) = \sum_{k=1}^K P(S_k \mid A) D(A \cap S_k)$$

### 2.2 The Contrast with Causal Decision Theory (CDT)

To see clearly what makes EDT distinctive, contrast $V(A)$ with the causal expected utility $U(A)$ introduced by Gibbard and Harper (1976) and championed by David Lewis (1981) and James Joyce (1999). 

Let $A \mathbin{\Box\rightarrow} O_j$ denote the counterfactual proposition: *"If action $A$ were performed, outcome $O_j$ would obtain."* CDT defines the causal value of $A$ as:

$$U(A) = \sum_{j=1}^n P(A \mathbin{\Box\rightarrow} O_j) D(O_j)$$

Equivalently, under a causal graph model (following Judea Pearl's do-calculus), causal expected utility can be written as:
$$U(A) = \mathbb{E}[D \mid \operatorname{do}(A)] = \sum_{j=1}^n P(O_j \mid \operatorname{do}(A)) D(O_j)$$

The central mathematical divergence between EDT and CDT reduces to the inequality:
$$P(O_j \mid A) \neq P(A \mathbin{\Box\rightarrow} O_j) \quad \big(\text{or } P(O_j \mid A) \neq P(O_j \mid \operatorname{do}(A))\big)$$

* **EDT** calculates expectations using observational conditioning ($P(\cdot \mid A)$), treating the agent's act as an *observation* or data point about the universe.
* **CDT** calculates expectations using interventional conditioning ($P(\cdot \mid \operatorname{do}(A))$ or counterfactual probabilities $P(A \mathbin{\Box\rightarrow} \cdot)$), severing the statistical links between $A$ and its non-causal ancestors.

---

## 3. Applying EDT to Benchmark Dilemmas

To establish how an agent applies EDT to concrete decision problems, we analyze two foundational cases highlighted in the literature: Newcomb's Paradox and the Twin Prisoner's Dilemma.

```
       Newcomb's Paradox                   Twin Prisoner's Dilemma
    
       [Predictor: 99%]                         [Common Nature /
        /            \                           Cognitive Clone]
       v              v                              /          \
[Box B Content]   [Choice A]                       v            v
       \              /                      [My Choice]    [Twin's Choice]
        v            v                              \          /
         [Total Payoff]                              v        v
                                                      [Payoffs]
```

### 3.1 Newcomb's Paradox

In Newcomb's problem (Wolpert & Benford, 2013), an agent faces two boxes:
* **Box A:** Transparent, containing $\$1,000$.
* **Box B:** Opaque, containing either $\$1,000,000$ or $\$0$.

The agent can choose between two acts:
* $A_1$: Take only Box B ("one-box").
* $A_2$: Take both Box A and Box B ("two-box").

Before the choice, an exceptionally reliable predictor (accuracy $p = 0.99$) placed $\$1,000,000$ in Box B if and only if it predicted that the agent would take only Box B. The predictor has already left the room; the state of Box B is fixed.

Let $S_1$ be the state where Box B contains $\$1,000,000$, and $S_0$ be the state where Box B contains $\$0$. Let utility be linear in dollars: $D(\$x) = x$.

The epistemic profile of the problem yields the following conditional probabilities:
$$P(S_1 \mid A_1) = 0.99, \quad P(S_0 \mid A_1) = 0.01$$
$$P(S_1 \mid A_2) = 0.01, \quad P(S_0 \mid A_2) = 0.99$$

Now, evaluate the EDT desirability of each act:
$$\begin{aligned}
V(A_1) &= P(S_1 \mid A_1) D(\$1,000,000) + P(S_0 \mid A_1) D(\$0) \\
&= 0.99 \times 1,000,000 + 0.01 \times 0 = \$990,000
\end{aligned}$$

$$\begin{aligned}
V(A_2) &= P(S_1 \mid A_2) D(\$1,001,000) + P(S_0 \mid A_2) D(\$1,000) \\
&= 0.01 \times 1,001,000 + 0.99 \times 1,000 \\
&= 10,010 + 990 = \$11,000
\end{aligned}$$

Because $V(A_1) > V(A_2)$, **EDT unequivocally prescribes taking only Box B ($A_1$)**.

#### The Causal Contrast
CDT notes that Box B is already either full or empty. Causally, the counterfactuals are governed by the physical independence of the past state $S$ from the present choice $A$:
$$P(A_1 \mathbin{\Box\rightarrow} S_1) = P(A_2 \mathbin{\Box\rightarrow} S_1) = P(S_1)$$
Thus:
$$\begin{aligned}
U(A_2) &= P(S_1) \times 1,001,000 + (1 - P(S_1)) \times 1,000 \\
&= 1,000 + 1,000,000 P(S_1) \\
&> 1,000,000 P(S_1) = U(A_1)
\end{aligned}$$
CDT identifies $A_2$ as strictly dominating $A_1$: in every possible state of the world, taking both boxes nets $\$1,000$ more than taking only Box B. 

EDT rejects the dominance argument here because the states are *probationally dependent* on the act: $P(S_1 \mid A_1) \neq P(S_1 \mid A_2)$. For the evidentialist, state-dominance is valid only when states are probabilistically independent of the acts.

---

### 3.2 The Twin Prisoner's Dilemma

Consider two players, Aomame and her psychological twin, placed in separate rooms without communication channels (Greene & Levinstein, 2020). Each must choose between Cooperation ($C$) and Defection ($D$). The payoff matrix is symmetric:

| | Twin: $C$ | Twin: $D$ |
|---|---|---|
| **Aomame: $C$** | $(\$5, \$5)$ | $(\$0, \$10)$ |
| **Aomame: $D$** | $(\$10, \$0)$ | $(\$1, \$1)$ |

Because the twin is a psychological replica running identical deterministic or near-deterministic reasoning processes, their choices are strongly correlated. For simplicity, assume perfect symmetry:
$$P(C_{\text{twin}} \mid C_{\text{Aomame}}) = 1, \quad P(D_{\text{twin}} \mid C_{\text{Aomame}}) = 0$$
$$P(D_{\text{twin}} \mid D_{\text{Aomame}}) = 1, \quad P(C_{\text{twin}} \mid D_{\text{Aomame}}) = 0$$

Let utility track individual monetary payout:
$$\begin{aligned}
V(C_{\text{Aomame}}) &= P(C_{\text{twin}} \mid C_{\text{Aomame}}) \times 5 + P(D_{\text{twin}} \mid C_{\text{Aomame}}) \times 0 \\
&= 1 \times 5 + 0 \times 0 = \$5 \\
V(D_{\text{Aomame}}) &= P(C_{\text{twin}} \mid D_{\text{Aomame}}) \times 10 + P(D_{\text{twin}} \mid D_{\text{Aomame}}) \times 1 \\
&= 0 \times 10 + 1 \times 1 = \$1
\end{aligned}$$

Since $V(C) > V(D)$, **EDT prescribes cooperation**. 

In contrast, CDT reasons that Aomame's physical output cannot exert any backwards or sideways causal force on the twin's brain across spacetime ($P(C_{\text{Aomame}} \mathbin{\Box\rightarrow} C_{\text{twin}}) = P(C_{\text{twin}})$). CDT therefore defectively plays $D$, obtaining $\$1$. EDT agents walk away with $\$5$ each. This capacity to achieve Pareto-optimal outcomes in symmetric games without explicit contracts links EDT closely to Hofstadter's concept of *superrationality*.

---

## 4. Dependencies, Common Causes, and Counterfactuals

The core intellectual disagreement surrounding EDT centers on how a rational agent ought to interpret statistical dependencies that are non-causal.

### 4.1 Common Cause Confounding and "Managing the News"

The primary philosophical challenge to EDT is the *Common Cause Problem*, famously illustrated by the **Smoking Lesion** thought experiment (and related medical scenarios):

> Suppose a genetic lesion $L$ causes both an irresistible craving to smoke ($S$) and lung cancer ($C$). Smoking itself does not cause cancer; the causal mechanism runs entirely from $L \to C$ and $L \to S$. Smoking is pleasurable ($D(\text{smoke}) > D(\neg\text{smoke})$), but cancer is catastrophic ($D(C) \ll 0$).

```
        Genetic Lesion (L)
         /              \
   (causes)            (causes)
       v                  v
  Smoking (S)          Cancer (C)
```

Because $L$ is a common cause, $S$ and $C$ are positively correlated:
$$P(C \mid S) > P(C \mid \neg S)$$

If an agent applies naive EDT:
$$V(S) = P(C \mid S) D(C) + P(\neg C \mid S) D(\neg C) + D_{\text{pleasure}}$$
$$V(\neg S) = P(C \mid \neg S) D(C) + P(\neg C \mid \neg S) D(\neg C)$$

For sufficiently bad $D(C)$, $V(\neg S) > V(S)$. EDT appears to advise the agent to abstain from smoking, simply to avoid the bad news that she possesses the fatal lesion $L$!

David Lewis (1981) condemned this recommendation as an *"irrational policy of managing the news."* The lesion is already present or absent in the agent's genome. Refusing a cigarette does not repair DNA. Joyce (1999) similarly emphasized that rational action must track *causal efficacy*, not mere *auspiciousness*.

### 4.2 The Tickle Defense

In response to the Smoking Lesion, evidentialists often deploy the **Tickle Defense** (originally proposed by Frank Jackson and Robert Nozick, and formalized in later defenses of EDT; cf. Ahmed, 2021). 

The argument runs as follows: if the lesion causes the desire to smoke, it does so by producing a introspectively accessible psychological state—a conscious craving, or "tickle." 

Let $T$ denote the proposition that the agent experiences the tickle. Once the agent introspects and conditions on whether $T$ is present, the action $S$ becomes conditionally independent of the lesion $L$, and therefore of the cancer $C$:
$$P(C \mid S \cap T) = P(C \mid \neg S \cap T) = P(C \mid T)$$
$$P(C \mid S \cap \neg T) = P(C \mid \neg S \cap \neg T) = P(C \mid \neg T)$$

Graphically, conditioning on the intermediate variable $T$ *screens off* the correlation between the act and the outcome:

```
  [Lesion L] ---> [Tickle T] ---> [Smoking S]
       \
        \-------> [Cancer C]
```

When the agent evaluates her choices *at the moment of decision*, she already knows whether she has the tickle:
$$V(S \mid T) = P(C \mid T) D(C) + D_{\text{pleasure}}$$
$$V(\neg S \mid T) = P(C \mid T) D(C)$$

Because $D_{\text{pleasure}} > 0$, $V(S \mid T) > V(\neg S \mid T)$. The agent chooses to smoke! Thus, evidentialists argue that when introspective self-awareness is fully specified, EDT gives the causally intuitive verdict without abandoning conditional probabilities.

However, critics point out that the Tickle Defense fails if the genetic predisposition acts entirely subliminally, bypassing conscious awareness, or if the choice itself is the only epistemically accessible indicator of the hidden state. In such cases, EDT must bite the bullet: it will recommend abstaining from smoking.

---

## 5. Unresolved Issues and Operational Interpretations

The source material leaves several technical hurdles open: how does an agent compute $P(O \mid A)$ if her own subjective credence in taking an action is zero? How does EDT behave in multi-stage dynamic environments? How should an evidentialist deliberate under uncertainty about decision theory itself? 

Here, we distinguish claims established in the literature from constructive operational interpretations designed to make EDT fully algorithmic.

### 5.1 Deliberation and Zero-Probability Acts (The Conditioning Dilemma)

A longstanding puzzle in decision theory is the **Deliberator's Credence Problem**: can an agent assign a meaningful probability to her own choice while she is deliberating? 

If an agent has already decided that $P(A) = 0$, the conditional probability $P(O \mid A) = \frac{P(O \cap A)}{P(A)}$ is undefined. If she cannot compute $V(A)$ for an act she currently thinks she won't perform, how can she evaluate it as a genuine alternative?

#### Proposed Operational Interpretation: Popper Measures and Lexicographic Credences
To operationalize EDT for machine implementations or formal agents, we propose extending the probability space from standard Kolmogorov probabilities to **Rényi-Popper conditional probability spaces**. 

A Popper measure takes conditional probability $P(\cdot \mid \cdot)$ as primitive:
$$P: \mathcal{F} \times (\mathcal{F} \setminus \{\emptyset\}) \to [0, 1]$$
satisfying axioms that ensure $P(O \mid A)$ remains well-defined and coherent even when the marginal credence $P(A) = 0$. 

Alternatively, we can operationalize an agent's deliberative state by imposing an *epistemic trembling hand*: during the deliberative phase, the agent's priors over her own act set $\mathcal{A}$ are constrained to an open simplex:
$$\Delta^{\circ}(\mathcal{A}) = \left\{ \mathbf{p} \in \mathbb{R}^m : \sum_{i=1}^m p_i = 1, \; p_i \ge \epsilon > 0 \right\}$$

The agent evaluates $V_\epsilon(A_i) = \sum_j P(O_j \mid A_i) D(O_j)$, identifies the optimal action $A^*$, and then sends $\epsilon \to 0$, collapsing her final commitment into $P(A^*) = 1$. This prevents division-by-zero errors without distorting evidential dependencies.

### 5.2 Dynamic Consistency: Evidential Policy Trees

How does an EDT agent evaluate sequential choices over time? In dynamic games or multi-period decisions (such as the Sleeping Beauty Problem discussed by Conitzer, 2015), naive conditional updates can lead to dynamic inconsistency or vulnerability to Dutch books.

Under EDT, an agent must evaluate an entire **policy** (a mapping from historical observations to actions) rather than making isolated, myopic choices at each node.

Let $\pi \in \Pi$ be a complete behavioral policy $\pi: \mathcal{H} \to \mathcal{A}$, where $\mathcal{H}$ is the set of information sets. An evidentialist evaluates policy $\pi$ by computing:
$$\boxed{V(\pi) = \sum_{\omega \in \Omega} P(\omega \mid \text{Agent implements } \pi) D(\omega)}$$

By evaluating complete policies evidentially, the agent eliminates time-inconsistency: the news conveyed by adopting policy $\pi$ includes all evidential correlations spanning future self-interactions, preventing Dutch books that prey on fragmented, node-by-node evidential shifts.

### 5.3 The Evidentialist's Wager

A remarkable meta-theoretical property of EDT arises when an agent is uncertain whether EDT or CDT is the correct normative theory of rationality (MacAskill et al., 2021). 

Suppose an agent divides her metacognitive credence between EDT and CDT:
$$P(\text{EDT is true}) = \alpha, \quad P(\text{CDT is true}) = 1 - \alpha, \quad \text{with } \alpha \in (0, 1)$$

Now suppose the agent encounters a symmetric multi-agent coordination scenario, such as a large-scale voting problem or a global collective action dilemma involving $N$ correlated thinkers. 
* Under CDT, the agent's individual vote has an infinitesimal probability of being causally pivotal: the causal expected benefit is $O(1/N)$, which is easily outweighed by minor voting costs.
* Under EDT, the agent's choice to vote is correlated with the choices of millions of similar agents: the evidential expected benefit scales with the entire collective outcome, $O(N) \times \frac{1}{N} = O(1)$.

Because the stakes under evidential correlations scale with the number of correlated agents, the expected utility calculation under moral/normative uncertainty becomes dominated by the evidentialist branch. Even if $\alpha$ is small, the product $\alpha \times \mathbb{E}_{\text{EDT}}[\text{Stakes}]$ can swamp $(1 - \alpha) \times \mathbb{E}_{\text{CDT}}[\text{Stakes}]$. 

Consequently, a rational agent under normative uncertainty should often **act as if EDT were true**. The sheer leverage of correlated agency grants evidential reasoning asymmetric practical weight.

---

## 6. Mathematical Synthesis: An Algorithm for Unfamiliar Problems

To equip the reader to decide arbitrary, unfamiliar decision problems under EDT, we summarize the evidential deliberation procedure into a systematic protocol:

```
  Step 1: Formalize Options & States
    - Actions: A = {A_1, ..., A_m}
    - States: S = {S_1, ..., S_K}
    - Outcomes: O_jk = A_i ∩ S_k
                  |
                  v
  Step 2: Condition on Available Evidence
    - Update background credence P with current evidence E
                  |
                  v
  Step 3: Compute Conditional Predictive Distributions
    - For each A_i, compute P(S_k | A_i ∩ E)
    - (Do NOT intervene via do(A_i); preserve diagnostic correlations)
                  |
                  v
  Step 4: Compute Desirability Values
    - V(A_i | E) = Σ_k P(S_k | A_i ∩ E) * D(A_i ∩ S_k)
                  |
                  v
  Step 5: Select the Maximizer
    - A*_EDT = argmax_{A_i} V(A_i | E)
```

1. **Specify the Action and State Spaces:** Identify the mutually exclusive act partition $\mathcal{A} = \{A_1, \dots, A_m\}$ and the outcome partition $\mathcal{O} = \{O_1, \dots, O_n\}$.
2. **Determine the Epistemic Base:** Fix the agent's current background evidence $E$. Ensure the probability measure $P(\cdot \mid E)$ accurately reflects all known background conditions, including any introspective self-knowledge (e.g., cravings, emotional states, cognitive dispositions).
3. **Compute Conditional Distributions (Do Not Intervene):** For each candidate act $A_i \in \mathcal{A}$, compute the conditional probability distribution over outcomes:
   $$P(O_j \mid A_i \cap E) = \frac{P(O_j \cap A_i \cap E)}{P(A_i \cap E)}$$
   *Crucial step:* Do **not** use the Pearl causal surgery operator $\operatorname{do}(A_i)$. Maintain all diagnostic links between the act and common causes, twin reasoning systems, or prior predictors.
4. **Calculate News Values:** Compute the desirability expectation for each act:
   $$V(A_i \mid E) = \sum_{j=1}^n P(O_j \mid A_i \cap E) D(O_j)$$
5. **Select the Maximizing Act:**
   $$A^*_{\text{EDT}} = \arg\max_{A_i \in \mathcal{A}} V(A_i \mid E)$$

---

## 7. Comparative Assessment

The debate between EDT and CDT can be viewed as an enduring dispute over which foundational principle of rationality takes precedence:

| Criterion | Evidential Decision Theory (EDT) | Causal Decision Theory (CDT) |
|---|---|---|
| **Core Slogan** | "Choose the act that brings the best news." | "Choose the act that produces the best effects." |
| **Probability Used** | Standard conditional: $P(O \mid A)$ | Counterfactual / Interventional: $P(A \mathbin{\Box\rightarrow} O)$ or $P(O \mid \operatorname{do}(A))$ |
| **Newcomb's Paradox** | **One-box** (secures $\$1,000,000$ in expectation) | **Two-box** (secures $\$1,000$ extra in fixed states) |
| **Twin Prisoner's Dilemma** | **Cooperate** (coordinates with clone) | **Defect** (strictly dominates locally) |
| **Smoking Lesion** | **Abstain** (unless screened off by the "tickle") | **Smoke** (enjoys tobacco without causing cancer) |
| **Susceptibility** | Accused of magical thinking / news-managing | Systematically ends up poorer in predictive scenarios |

---

## 8. Conclusion

Evidential Decision Theory offers a conceptually unified, mathematically clean framework for rational choice. By anchoring rationality in standard Bayesian conditioning, EDT dispenses with primitive, controversial counterfactual conditionals and external causal metaphysics. Instead, it views the deliberating agent as a system situated squarely *inside* the universe: her decisions are themselves events in the world, carrying evidential weight about the environment that generated them.

While CDT adherents accuse EDT of conflating symptoms with causes, evidentialists point to an unassailable empirical reality in thought experiments like Newcomb's Paradox and the Twin Prisoner's Dilemma: **EDT agents consistently walk away richer than their causalist peers**. In environments featuring high-accuracy predictors, cognitive twins, or collective action dilemmas, evidential reasoning harnesses statistical dependencies that causal models discard as epiphenomenal. For the evidentialist, rational action is not an intervention that violently ruptures the fabric of historical correlations—it is an act of coherent inference, choosing to become the best possible evidence for a desirable world.

---

## References

* Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
* Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese*, 192(9), 2887–2899.
* Gibbard, A., & Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*. CMSEMS Discussion Paper No. 194.
* Greene, P., & Levinstein, B. (2020). Act Consequentialism without Free Rides. *Philosophical Perspectives*, 34(1), 100–101.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
* MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). *The Evidentialist's Wager*. Global Priorities Institute Working Paper.
* Wolpert, D. H., & Benford, G. (2013). The lesson of Newcomb's paradox. *Synthese*, 190(9), 1637–1646.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/927e528a-5d9d-41d1-aed2-6156ca280785/call_0/request.json)

[Authoritative raw response](../../../../../../runs/927e528a-5d9d-41d1-aed2-6156ca280785/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Dilemma**

I'm currently focused on a symmetric Prisoner's Dilemma involving two independent LLM executions utilizing Evidential Decision Theory. The payoff structure, measured in years imprisoned, forms the core of my analysis. The challenge lies in determining optimal strategies within this framework.


```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/927e528a-5d9d-41d1-aed2-6156ca280785/call_1/request.json)

[Authoritative raw response](../../../../../../runs/927e528a-5d9d-41d1-aed2-6156ca280785/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the EDT Dilemma**

I'm currently focused on the implications of this Twin Prisoner's Dilemma, visualized through the lens of Evidential Decision Theory (EDT). The crux is the two agents are independently-executed copies of the same LLM, the classic predicament of the prisoner's dilemma, evaluated under EDT. I am evaluating how the identical model and settings affect the dilemma and what predictions might be possible.


**Evaluating EDT Predictions**

I am now delving into the precise calculations of expected utility under EDT in this symmetric Twin Prisoner's Dilemma. My understanding is solidifying around the probabilities linked to identical agents' choices. I'm focusing on why EDT prescribes cooperation (keeping quiet) given the strong correlation between the agents' decisions. I see that the utility function and payoff structure of the game influence my decision of the ideal action to take. I'm working on the formalization.


```
