# Policy Functional Decision Theory: Foundations, Formalisms, and Applications

In contemporary decision theory, the long-standing debate between Causal Decision Theory (CDT) and Evidential Decision Theory (EDT) centers on how rational agents should formulate hypothetical scenarios. When evaluating an act, should an agent condition on the evidence that the act was performed (as prescribed by EDT), or should she evaluate the consequences downstream of an intervention on the physical act itself (as prescribed by CDT)? Both paradigms suffer well-documented pathologies: EDT systematically conflates correlation with causation in common-cause dilemmas like the Smoking Lesion problem, whereas CDT squanders massive utility in predictive environments such as Newcomb’s Problem, Parfit’s Hitchhiker, and the Mechanical Blackmail problem.

Eliezer Yudkowsky and Nate Soares (2017) introduce *Functional Decision Theory* (FDT), proposing that an agent ought to conceive of her choice not as an intervention on a localized physical action token, but as the output of an abstract mathematical decision program—an intervention on a decision *type*. Yet within the standard presentation of FDT, an important formal fork emerges regarding the precise object of optimization. In Section 5 and Section 9 (specifically footnotes 7 and 16) of their foundational paper, the authors highlight an alternative, structurally robust formulation:

> "...the author's preferred formulation of FDT actually intervenes on the node $\text{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action." (Footnote 16)

We designate this normative model **P-FDT (Policy Functional Decision Theory)**. 

While act-based FDT evaluates hypothetical outputs for the concrete observation at hand, P-FDT steps back to a global, ex-ante computational perspective. A P-FDT agent selects an entire policy—a decision mapping from observation histories to acts—and then executes the act prescribed by that optimal policy for her current observation. This essay provides a rigorous mathematical exposition of P-FDT, delineates its treatment of subjunctive dependence and counterfactuals, clarifies the foundational ambiguities left open in the original literature, and applies the framework to canonical and unfamiliar decision dilemmas.

---

## 1. The Philosophical and Structural Motivation for Policies

Standard Causal Decision Theory operates via local, token-level interventions. Given an observation $x$, a CDT agent asks: *“Holding fixed the past and all processes not causally downstream from my muscles, which physical act $a \in \mathcal{A}$ causes the highest expected utility?”* In Newcomb-like dilemmas, this leads directly to two-boxing: the predictor has already filled or emptied the opaque box, and no causal arrows point backward from the agent’s physical hands to the past prediction.

Standard act-based FDT observes that this ignores logical and computational structure. If the predictor executed an accurate cognitive model of the agent, the prediction subjunctively depends on the agent’s decision function. In standard act-based FDT, an agent facing observation $x$ queries: *“Which output of my decision procedure on input $x$ subjunctively produces the best outcome?”* 

In many settings, this solves the dilemma. But when dilemmas feature dynamic observations, screening-off variables, or asymmetric information, conditioning on the current observation *before* selecting the counterfactual intervention can induce conceptual strain. In the Transparent Newcomb Problem or the Mechanical Blackmail, an agent who sees that Box B is full, or who receives a blackmail letter, must evaluate counterfactual outputs of her algorithm while simultaneously entertaining worlds where that very input was never observed.

P-FDT resolves this tension by shifting the locus of choice from *acts given observations* to *policies across all possible observations*. Instead of asking:
$$\text{“What should I do, given that I observed } x\text{?”}$$
P-FDT asks:
$$\text{“Which policy } \pi \in \Pi \text{ is such that its global mathematical instantiation maximizes expected utility?”}$$

Once the globally optimal policy $\pi^*$ is identified, the agent's executed act is simply $a = \pi^*(x)$.

This design internalizes several classical desiderata of instrumental rationality:
1. **Dynamic and Reflective Consistency:** A P-FDT agent automatically behaves in ongoing interactions exactly as she would have rationally bound herself to act via a prior cost-free precommitment. She never suffers from the temporal incoherence that plagues CDT (which often recommends self-modifying into non-CDT agents while continuing to execute CDT locally).
2. **Non-Negative Value of Information:** Standard EDT agents often assign negative expected value to information (for instance, preferring to be blindfolded in Transparent Newcomb to prevent themselves from defecting). P-FDT agents evaluate information globally; since a policy can ignore or condition on data as optimal, information cannot reduce expected utility under P-FDT.
3. **Updateless Stability:** In the terminology of early foundational literature (such as Wei Dai’s Updateless Decision Theory), P-FDT is an updateless formulation. It does not update its prior perspective to evaluate what *would have happened*; rather, it evaluates the counterfactuals of policy implementations across the whole probability space, preventing the "double-update" pathology identified in Timeless Decision Theory.

---

## 2. Formal Mathematical Architecture of P-FDT

We formalize P-FDT using Pearlian structural causal models augmented to represent functional/subjunctive dependencies over algorithmic types.

### 2.1 Spaces and Primitives
Let:
- $\mathcal{X}$ be a countable space of possible observation histories.
- $\mathcal{A}$ be a finite space of primitive physical acts.
- $\Pi = \mathcal{A}^\mathcal{X} = \{ \pi : \mathcal{X} \to \mathcal{A} \}$ be the space of deterministic policies.
- $\mathcal{O}$ be a countable set of world outcomes.
- $\mathcal{U} : \mathcal{O} \to \mathbb{R}$ be a bounded Von Neumann–Morgenstern utility function, inducing a real-valued utility variable $V = \mathcal{U}(\text{Outcome})$.

The agent maintains an augmented world-model $M = (P, G)$:
- $P$ is a joint probability distribution over a set of endogenous and exogenous variables, including observations $\text{Obs} \in \mathcal{X}$, actions $\text{Act} \in \mathcal{A}$, outcomes $\text{Outcome} \in \mathcal{O}$, utility $V \in \mathbb{R}$, and mathematical function nodes.
- $G = (\mathcal{V}, \mathcal{E})$ is a directed acyclic graph encoding dependencies. Crucially, $\mathcal{V}$ contains not only physical nodes but an abstract node representing the agent's policy program:
  $$\mathbf{\Pi}^* = \text{P-FDT}(\underline{P}, \underline{G})$$
  Here, the underlines denote syntactic quotes (following Kleene’s recursion theorem / quining), signifying that the world-model contains an accurate mathematical representation of the agent's own code.

### 2.2 Subjunctive Dependence and the Interventional Operator
In causal graphical models, an intervention $\text{do}(\text{Act} = a)$ severs incoming arrows to $\text{Act}$ and sets its value to $a$, propagating this change exclusively along directed causal paths. In P-FDT, the fundamental interventional locus is the policy node $\mathbf{\Pi}^*$.

Subjunctive dependence formalizes the constraint of mathematical identity: if multiple physical processes in the universe simulate, predict, or execute the agent's policy function, those nodes in $G$ are children of the logical node $\mathbf{\Pi}^*$. When a predictor builds a neural model, symbolic simulation, or deductive proof of the agent’s code, the predictor’s internal variable $\text{Prediction}$ does not causally depend on the agent’s physical arm muscles; it *subjunctively depends* on the mathematical output of $\mathbf{\Pi}^*$.

Thus, an intervention setting the policy to $\pi \in \Pi$ is formalized as:
$$\text{do}(\mathbf{\Pi}^* = \pi)$$
This surgery sets the abstract policy to $\pi$. Under this intervention:
1. Every node in the universe that computes or represents $\mathbf{\Pi}^*$ updates its behavior to evaluate $\pi$.
2. The agent’s own physical act node $\text{Act}$ is deterministically governed by the functional equation:
   $$\text{Act} = \mathbf{\Pi}^*(\text{Obs})$$
3. Any predictor predicting the agent's policy or actions adjusts according to the logical consequences of $\mathbf{\Pi}^*$ behaving as $\pi$.

### 2.3 The Core Decision Rule of P-FDT
We now define the formal selection mechanism of P-FDT. The theory proceeds in two distinct stages: Policy Selection and Action Execution.

```
       [ Prior Model (P, G) ]
                  |
                  v
       +-----------------------+
       |   Policy Selection    |  <-- Maximizes E[ V | do(Π* = π) ]
       |     Finds π* in Π     |
       +-----------------------+
                  |
                  v
       +-----------------------+
       |   Action Execution    |  <-- Evaluates a* = π*(x)
       |   Given current x     |
       +-----------------------+
                  |
                  v
           [ Physical Act a* ]
```

#### Stage 1: Global Policy Selection
The optimal policy $\pi^* \in \Pi$ is defined as the argument maximizing the unconditioned expected utility under a subjunctive policy intervention:

$$\pi^* = \text{P-FDT}(P, G) \coloneqq \operatorname*{argmax}_{\pi \in \Pi} \mathbb{E} \Big[ V \;\Big|\; \text{do}\big(\mathbf{\Pi}^* = \pi\big) \Big]$$

Here, the expectation is computed with respect to the interventional distribution:
$$\mathbb{E} \Big[ V \;\Big|\; \text{do}\big(\mathbf{\Pi}^* = \pi\big) \Big] = \sum_{o \in \mathcal{O}} \mathcal{U}(o) \cdot P\big(\text{Outcome} = o \;\big|\; \text{do}(\mathbf{\Pi}^* = \pi)\big)$$

#### Stage 2: Action Execution
Upon receiving or possessing the current concrete observation $x \in \mathcal{X}$, the P-FDT agent executes the act prescribed by $\pi^*$:
$$a^* = \pi^*(x)$$

### 2.4 Comparison to Standard Act-Based FDT, CDT, and EDT
To see the structural distinction clearly, contrast the decision rules of the four theories:

- **EDT (Evidential):**
  $$a_{\text{EDT}} = \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\big[ V \;\big|\; \text{Obs} = x, \text{Act} = a \big]$$
  *(Conditions on both observation and act; confounds correlation with causation.)*

- **CDT (Causal):**
  $$a_{\text{CDT}} = \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\big[ V \;\big|\; \text{Obs} = x, \text{do}(\text{Act} = a) \big]$$
  *(Conditions on observation; intervenes locally on the physical action token.)*

- **Act-FDT (Standard Act-Functional):**
  $$a_{\text{FDT}} = \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\big[ V \;\big|\; \text{do}\big(\mathbf{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\big) \big]$$
  *(Intervenes on the algorithm's output specifically for the observed $x$.)*

- **P-FDT (Policy-Functional):**
  $$\pi^* = \operatorname*{argmax}_{\pi \in \Pi} \mathbb{E}\big[ V \;\big|\; \text{do}(\mathbf{\Pi}^* = \pi) \big], \quad a_{\text{P-FDT}} = \pi^*(x)$$
  *(Intervenes globally on the entire mapping $\pi : \mathcal{X} \to \mathcal{A}$ without pre-conditioning on $x$, then applies $\pi^*$ to $x$.)*

---

## 3. Resolving Open Ambiguities: What Does Footnote 16 Leave Open?

Footnote 16 of Yudkowsky & Soares (2017) explicitly states the policy-selection principle, but leaves several critical operational questions unresolved:
1. **The Priors Problem (The Epistemic Anchor):** Over which distribution is the policy expectation evaluated? If an agent has already observed $x$, does she evaluate $\pi$ over her prior distribution $P$ or her posterior distribution $P(\cdot \mid \text{Obs} = x)$?
2. **The Counterfactual Logic of Counterpossibles:** If $\mathbf{\Pi}^*$ is an immutable mathematical function whose unique true code outputs $\pi^*$, what does $\text{do}(\mathbf{\Pi}^* = \pi)$ mean for $\pi \neq \pi^*$?
3. **The Multi-Agent / Self-Referential Graph Topology:** When two agents run P-FDT, how are their policy nodes connected to prevent infinite regress or circular causal graphs?

We now provide a rigorous operational interpretation for each question, explicitly demarcating where we extend the original source.

### 3.1 The Prior vs. Posterior Evaluation Dilemma
Suppose an agent is already sitting at the ATM in Parfit’s desert or staring at two open boxes in Transparent Newcomb. She knows $x = \text{city}$ or $x = \text{full}$. If she evaluates:
$$\operatorname*{argmax}_{\pi} \mathbb{E}\big[ V \;\big|\; \text{do}(\mathbf{\Pi}^* = \pi), \text{Obs} = x \big]$$
she risks collapsing back into the act-level perspective, because conditioning on $\text{Obs} = x$ inside the expectation forces the agent to assess counterfactual policies only according to how they perform *in the world where $x$ has already obtained*. 

**Our Proposal (The Canonical P-FDT Protocol):**  
To realize true updatelessness, P-FDT must define its optimization **ex-ante** relative to the agent’s base prior $P$ (the epistemic baseline prior to receiving the specific problem-differentiating observation $x$), or equivalently over the complete joint model:
$$\mathbb{E}\big[ V \;\big|\; \text{do}(\mathbf{\Pi}^* = \pi) \big] = \sum_{x \in \mathcal{X}} P(\text{Obs} = x \mid \text{do}(\mathbf{\Pi}^* = \pi)) \cdot \mathbb{E}\big[ V \;\big|\; \text{do}(\mathbf{\Pi}^* = \pi), \text{Obs} = x \big]$$

Notice how this formula treats the observation: the probability of observing $x$ is itself *endogenous* to the policy $\pi$. If choosing a defiant policy $\pi$ causes a predictor not to send a blackmail letter, then $P(\text{Obs} = \text{letter} \mid \text{do}(\mathbf{\Pi}^* = \pi)) \approx 0$. By evaluating the policy globally across all possible observation paths, the agent captures the systemic benefits of deterring adversaries, establishing credible commitments, and eliciting cooperative predictions.

### 3.2 Formalizing Counterpossibles via Augmented SCMs
A prominent theoretical objection to functional decision theories is that if an algorithm's output is mathematically necessary, evaluating an alternative output requires evaluating a *counterpossible conditional* (an antecedent that is mathematically false). 

In P-FDT, this difficulty is resolved within Pearl’s structural framework by adopting what computer scientists call an *abstract semantic interface*. We treat the algorithm’s implementation node in the physical causal network as an exogenous structural variable taking values in $\Pi$. The graphical surgery $\text{do}(\mathbf{\Pi}^* = \pi)$ does not alter the mathematical truth of arithmetic or Peano axioms; rather, it performs surgery on the *physical and subjunctive realization* of that algorithm throughout the world-model. 

Formally, let the structural equation for any system $k$ predicting the agent be:
$$\text{Prediction}_k = g_k(\mathbf{\Pi}^*, \xi_k)$$
where $\xi_k$ represents noise or unreliability. When we set $\text{do}(\mathbf{\Pi}^* = \pi)$, we replace the default identity $\mathbf{\Pi}^* \equiv \text{P-FDT}$ with the constant function $\pi$. The operation propagates through the graph $G$, altering $\text{Prediction}_k$, the agent’s actual execution $\text{Act} = \pi(\text{Obs})$, and the resulting $\text{Outcome}$. This preserves the standard probability calculus: counterpossibles are handled mechanically as graphical interventions on computational types.

---

## 4. Canonical Dilemmas Evaluated under P-FDT

To establish the operational precision of P-FDT, we analyze its behavior across classic decision problems and contrast it with CDT and EDT.

### 4.1 Newcomb’s Problem
An opaque box contains $\$1,000,000$ iff a $99\%$ reliable predictor predicted the agent would forgo a transparent box containing $\$1,000$.

- **Spaces:** $\mathcal{X} = \{ \emptyset \}$ (no non-trivial observation prior to choice). $\mathcal{A} = \{ \text{one-box}, \text{two-box} \}$.
- **Policies:** Since $|\mathcal{X}| = 1$, policies are isomorphic to actions: $\pi_1(\emptyset) = \text{one-box}$, $\pi_2(\emptyset) = \text{two-box}$.
- **Subjunctive Dependency:**
  $$P(\text{Prediction} = \text{one} \mid \text{do}(\mathbf{\Pi}^* = \pi_1)) = 0.99$$
  $$P(\text{Prediction} = \text{two} \mid \text{do}(\mathbf{\Pi}^* = \pi_2)) = 0.99$$
- **Evaluation:**
  $$\mathbb{E}[V \mid \text{do}(\mathbf{\Pi}^* = \pi_1)] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000$$
  $$\mathbb{E}[V \mid \text{do}(\mathbf{\Pi}^* = \pi_2)] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000$$
- **Selection:** $\pi^* = \pi_1$. The agent executes $a^* = \pi_1(\emptyset) = \text{one-box}$.

### 4.2 The Smoking Lesion Problem
Smoking is strongly correlated with fatal lung cancer due to an arterial lesion that causes both a desire to smoke and cancer. Smoking provides an intrinsic pleasure of $\$1,000$; cancer inflicts a loss of $\$1,000,000$. Smoking does not cause cancer.

In this dilemma, the lesion causes the agent’s preference structure. As Yudkowsky and Soares demonstrate, the lesion does not predict the algorithm $\mathbf{\Pi}^*$; rather, the biological lesion determines which utility function/model the agent runs.

```
       [ Lesion ] -----------> [ Cancer ]
           |                       |
           v                       v
     [ Agent Prefs ]            [ Death ]
           |                       |
           v                       v
     [ Action Act ] ---------> [ Outcome / Utility ]
           ^
           |
       [ Policy Π* ]
```

- **Subjunctive Independence:** The graph $G$ has no edge from $\mathbf{\Pi}^*$ to $\text{Lesion}$ or $\text{Cancer}$. Intervening on the policy changes the physical act of smoking, but the probability of the lesion remains strictly constant:
  $$P(\text{Lesion} \mid \text{do}(\mathbf{\Pi}^* = \pi_{\text{smoke}})) = P(\text{Lesion} \mid \text{do}(\mathbf{\Pi}^* = \pi_{\text{refrain}})) = p$$
- **Evaluation:** For any prior probability $p$ of having the lesion:
  $$\mathbb{E}[V \mid \text{do}(\mathbf{\Pi}^* = \pi_{\text{smoke}})] = \mathbb{E}[V \mid \text{do}(\mathbf{\Pi}^* = \pi_{\text{refrain}})] + \$1,000$$
- **Selection:** $\pi^* = \pi_{\text{smoke}}$. The P-FDT agent smokes.
Unlike EDT, P-FDT does not "manage the news" because its hypothetical surgery breaks purely evidential correlations unsupported by subjunctive/logical dependency.

### 4.3 The Transparent Newcomb Problem
The agent observes the contents of Box B (either $\text{full}$ or $\text{empty}$) *before* choosing whether to take Box A ($\$1,000$). The predictor placed $\$1,000,000$ in Box B iff she predicted that the agent, upon observing $\text{full}$, would leave Box A behind.

Here the divergence between act-based theories and P-FDT becomes vivid.
- **Spaces:** $\mathcal{X} = \{ \text{full}, \text{empty} \}$, $\mathcal{A} = \{ \text{one-box}, \text{two-box} \}$.
- **Policy Space:** $\Pi = \{ \pi_{11}, \pi_{12}, \pi_{21}, \pi_{22} \}$, where $\pi_{ij}(\text{full}) = i$ and $\pi_{ij}(\text{empty}) = j$.
  Specifically, let:
  - $\pi_{12}$: "If full, one-box; if empty, two-box."
  - $\pi_{22}$: "Always two-box."

Now evaluate the expected utility of these policies globally under the interventional distribution:
- If $\mathbf{\Pi}^* = \pi_{12}$, the predictor predicts $\pi_{12}(\text{full}) = \text{one-box}$. With $99\%$ probability, the predictor fills Box B. 
  Hence, under $\text{do}(\mathbf{\Pi}^* = \pi_{12})$:
  $$P(\text{Obs} = \text{full}) = 0.99, \quad P(\text{Obs} = \text{empty}) = 0.01$$
  $$\mathbb{E}[V \mid \text{do}(\mathbf{\Pi}^* = \pi_{12})] = 0.99(\$1,000,000) + 0.01(\$1,000) = \$990,010$$

- If $\mathbf{\Pi}^* = \pi_{22}$, the predictor predicts two-boxing, so Box B is left empty with $99\%$ probability:
  $$P(\text{Obs} = \text{full}) = 0.01, \quad P(\text{Obs} = \text{empty}) = 0.99$$
  $$\mathbb{E}[V \mid \text{do}(\mathbf{\Pi}^* = \pi_{22})] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000$$

Global policy optimization uniquely selects:
$$\pi^* = \pi_{12}$$

**Execution:** The agent opens the door and observes $\text{Obs} = \text{full}$. She executes:
$$a^* = \pi^*(\text{full}) = \text{one-box}$$

**Contrast with CDT and EDT:**
- CDT conditions on $\text{Obs} = \text{full}$ and notes that taking Box A adds $\$1,000$ causally downstream. CDT two-boxes and walks away with $\$1,000$.
- EDT conditions on $\text{Obs} = \text{full}$. Since the box is *already observed* to be full, conditioning on two-boxing yields $\$1,001,000$ while one-boxing yields $\$1,000,000$. EDT two-boxes!
- P-FDT alone recognizes that being an agent who executes the policy $\pi_{12}$ is precisely what caused the box to be full in the first place.

### 4.4 The Mechanical Blackmail
A blackmailer has incriminating material that would cost both the blackmailer and the agent $\$1,000,000$. The blackmailer only runs an automated extortion program if a reliable prediction verifies that the agent will pay $\$1,000$ upon receiving the letter. An agent receives the letter ($\text{Obs} = \text{letter}$).

- **Policies:**
  - $\pi_{\text{comply}}$: "If letter, pay $\$1,000$."
  - $\pi_{\text{defy}}$: "If letter, refuse to pay."
- **Global Consequences:**
  - Under $\text{do}(\mathbf{\Pi}^* = \pi_{\text{comply}})$, the blackmailer predicts compliance, sends the letter, and the agent pays $\$1,000$. Expected utility $\approx -\$1,000$.
  - Under $\text{do}(\mathbf{\Pi}^* = \pi_{\text{defy}})$, the blackmailer predicts defiance, aborts the program, and sends no letter. Expected utility $\approx \$0$.

P-FDT selects $\pi^* = \pi_{\text{defy}}$. If the blackmailer was imperfect and sent the letter by accident, the P-FDT agent still executes $\pi_{\text{defy}}(\text{letter}) = \text{refuse}$. The agent refuses payment, establishing reflective immunity against blackmail.

---

## 5. Decision Comparison Matrix

The structural behaviors across theories are summarized below:

| Decision Problem | EDT Prescription | CDT Prescription | Act-FDT Prescription | P-FDT Prescription | Optimal Policy $\pi^*(x)$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Newcomb’s Problem** | One-box ($\$1\text{M}$) | Two-box ($\$1\text{K}$) | One-box ($\$1\text{M}$) | One-box ($\$1\text{M}$) | $\pi^*(\emptyset) = \text{one-box}$ |
| **Smoking Lesion** | Refrain (Avoid news) | Smoke ($+\$1\text{K}$) | Smoke ($+\$1\text{K}$) | Smoke ($+\$1\text{K}$) | $\pi^*(\emptyset) = \text{smoke}$ |
| **Parfit’s Hitchhiker** | Refuse to pay (Dies) | Refuse to pay (Dies) | Pay ATM ($\$1\text{M} - \$1\text{K}$) | Pay ATM ($\$1\text{M} - \$1\text{K}$) | $\pi^*(\text{city}) = \text{pay}$ |
| **Transparent Newcomb** | Two-box ($\$1\text{K}$) | Two-box ($\$1\text{K}$) | One-box ($\$1\text{M}$) | One-box ($\$1\text{M}$) | $\pi^*(\text{full}) = \text{one-box}$ |
| **Mechanical Blackmail** | Pay ($\text{Loss } \$1\text{K}$) | Pay ($\text{Loss } \$1\text{K}$) | Refuse ($\text{Loss } \$0$) | Refuse ($\text{Loss } \$0$) | $\pi^*(\text{letter}) = \text{refuse}$ |
| **Cosmic Ray Trap** | Takes $\$1$ (Fears checkup) | Takes $\$100$ | Takes $\$100$ | Takes $\$100$ | $\pi^*(\emptyset) = \text{take } \$100$ |

---

## 6. Resolving an Unfamiliar Dilemma: The Asymmetric Twin Oracle Matrix

To demonstrate how a reader can apply P-FDT to novel, unfamiliar cases, we introduce a complex multi-stage scenario involving asymmetric information and correlated execution.

### Dilemma Definition: The Asymmetric Twin Oracle Matrix
An agent ($\alpha$) and her identical clone ($\beta$) are placed in separate rooms. A supercomputer Oracle runs an exact emulation of their decision software. The Oracle generates a hidden random state $S \in \{ s_1, s_2 \}$ with prior probabilities $P(s_1) = 0.8$ and $P(s_2) = 0.2$.

- Agent $\alpha$ receives an imperfect sensor reading of the state: $\text{Obs}_\alpha \in \{ \text{signal}_1, \text{signal}_2 \}$. 
  - If $S = s_1$, $P(\text{signal}_1) = 0.9, P(\text{signal}_2) = 0.1$.
  - If $S = s_2$, $P(\text{signal}_1) = 0.1, P(\text{signal}_2) = 0.9$.
- Twin $\beta$ receives no sensor reading at all: $\text{Obs}_\beta = \emptyset$.
- Each agent must independently choose an action from $\{ \text{Safe}, \text{Bold} \}$.
- The Oracle, having predicted the policies of both agents, intervenes in the world before the agents act:
  - If the Oracle predicted that both agents execute policies that yield $\text{Bold}$ under state $s_1$, the Oracle injects $\$500,000$ into the shared payout pool.
  - If the Oracle predicted that both agents execute $\text{Safe}$ under all conditions, the pool gets $\$100,000$.
  - However, if the agents mismatch, or if they execute $\text{Bold}$ when the true state is $s_2$, a catastrophe penalty of $-\$1,000,000$ is deducted from the payout pool.
- Any agent who plays $\text{Safe}$ receives a private bonus of $\$5,000$.

Suppose Agent $\alpha$ observes $\text{signal}_2$. The posterior probability of $s_2$ given $\text{signal}_2$ is:
$$P(s_2 \mid \text{signal}_2) = \frac{0.2 \times 0.9}{(0.2 \times 0.9) + (0.8 \times 0.1)} = \frac{0.18}{0.18 + 0.08} = \frac{18}{26} \approx 69.2\%$$
What should Agent $\alpha$ do?

### Applying P-FDT Step-by-Step

#### Step 1: Formalize Policies
The two agents are psychological twins computing the same normative decision theory. Therefore:
$$\mathbf{\Pi}^*_\alpha = \mathbf{\Pi}^*_\beta = \mathbf{\Pi}^*$$
A policy $\pi$ must specify an action for each agent's information set:
- For $\alpha$: $\pi(\text{signal}_1)$ and $\pi(\text{signal}_2)$.
- For $\beta$: $\pi(\emptyset)$.

Thus, a policy is a triple:
$$\pi = \big( \pi(\text{signal}_1), \, \pi(\text{signal}_2), \, \pi(\emptyset) \big) \in \{ \text{Safe}, \text{Bold} \}^3$$

#### Step 2: Subjunctive Evaluation of Policies
Because the Oracle emulates $\mathbf{\Pi}^*$, the Oracle's predictions subjunctively depend on the chosen policy $\pi$.
Let us evaluate two salient candidate policies:

- **Policy $\pi_{\text{coordinated-bold}}$:** 
  $$\pi = \big( \text{signal}_1 \mapsto \text{Bold}, \; \text{signal}_2 \mapsto \text{Safe}, \; \emptyset \mapsto \text{Bold} \big)$$
  - Under state $s_1$: With probability $0.9$, $\alpha$ sees $\text{signal}_1$ and plays $\text{Bold}$. $\beta$ plays $\text{Bold}$. Both match on $\text{Bold}$! The Oracle predicted this behavior and funded the pool.
  - Payout on $(s_1, \text{signal}_1)$: $\$500,000$.
  - But with probability $0.1$, $\alpha$ sees $\text{signal}_2$ and plays $\text{Safe}$, while $\beta$ plays $\text{Bold}$. Mismatch! Payout: $-\$1,000,000$.
  - Under state $s_2$: With probability $0.9$, $\alpha$ sees $\text{signal}_2$ and plays $\text{Safe}$; $\beta$ plays $\text{Bold}$ in state $s_2$. Catastrophe penalty applies: $-\$1,000,000$.
  - Total expected utility for $\pi_{\text{coordinated-bold}}$:
    $$0.8 \big[ 0.9(\$500,000) + 0.1(-\$1,000,000) \big] + 0.2 \big[ 0.9(-\$1,000,000) + 0.1(-\$1,000,000) \big] = 0.8(350,000) - 200,000 = \$80,000$$

- **Policy $\pi_{\text{all-safe}}$:**
  $$\pi = \big( \text{signal}_1 \mapsto \text{Safe}, \; \text{signal}_2 \mapsto \text{Safe}, \; \emptyset \mapsto \text{Safe} \big)$$
  - Both agents consistently execute $\text{Safe}$ in all states.
  - The Oracle predicts universal safe behavior and deposits $\$100,000$ into the shared pool.
  - Both agents collect their individual safe bonuses: $2 \times \$5,000 = \$10,000$.
  - Total expected utility:
    $$\mathbb{E}[V \mid \text{do}(\mathbf{\Pi}^* = \pi_{\text{all-safe}})] = \$100,000 + \$10,000 = \$110,000$$

- **Policy $\pi_{\text{pure-bold}}$:**
  $$\pi = \big( \text{signal}_1 \mapsto \text{Bold}, \; \text{signal}_2 \mapsto \text{Bold}, \; \emptyset \mapsto \text{Bold} \big)$$
  Under $s_2$ (probability $0.2$), both play $\text{Bold}$, triggering the catastrophe penalty. Expected utility is deeply negative.

#### Step 3: Selection and Execution
The global optimizer over all $2^3 = 8$ policies is:
$$\pi^* = \pi_{\text{all-safe}}$$
Now, Agent $\alpha$, observing $\text{Obs}_\alpha = \text{signal}_2$, executes:
$$a^*_\alpha = \pi^*(\text{signal}_2) = \text{Safe}$$

P-FDT handles the partial observational asymmetry seamlessly. The agent does not need ad-hoc coordination rules; the subjunctive policy operator evaluates the systemic coordination between all physical instances implementing $\mathbf{\Pi}^*$ across all information states.

---

## 7. Critiques, Boundaries, and Philosophical Assessment

While P-FDT provides an exceptionally powerful theory of instrumental rationality, several open questions mark the frontier of the research program.

### 7.1 Computational Complexity of Policy Spaces
In complex environments with rich observational histories, the space of policies $\Pi = \mathcal{A}^\mathcal{X}$ is doubly exponential in the time horizon. Finding $\operatorname*{argmax}_{\pi \in \Pi} \mathbb{E}[V \mid \text{do}(\mathbf{\Pi}^* = \pi)]$ directly is computationally intractable for bounded agents. An operational artificial intelligence must approximate P-FDT via heuristic policy search, gradient optimization over parameterized policy spaces (e.g., deep neural networks), or meta-level deliberation.

### 7.2 The Problem of Subjunctive Structure Learning
As Soares and Yudkowsky acknowledge, Pearl solved the problem of learning *causal* directed acyclic graphs from empirical data and interventional trials. However, there is currently no complete formal algorithm for learning *subjunctive* graphs directly from raw empirical distributions. When does a correlation between a past event and an agent's future decision reflect true subjunctive dependency (as in Newcomb's predictor) versus mere biological common cause (as in the Smoking Lesion)? P-FDT assumes the graph $G$ is provided as an input primitive. Establishing a rigorous epistemology for deducing subjunctive graphs from computational primitives remains the most important open technical hurdle in functional decision theory.

---

## 8. Conclusion

Policy Functional Decision Theory (P-FDT) represents the culmination of the functional approach to instrumental rationality. By locating the interventional calculus at the level of the *policy type* rather than the *action token*, P-FDT achieves what classical decision theories could not:
1. It matches CDT’s refusal to indulge in superstitious news-management in common-cause settings like the Smoking Lesion.
2. It matches EDT’s capacity to achieve mutual cooperation in Twin Prisoner's Dilemmas and one-boxing in Newcomb's Problem.
3. Crucially, it outperforms both CDT and EDT in dynamic and transparent predictive settings—including Parfit's Hitchhiker, Transparent Newcomb, and Mechanical Blackmail.

Under P-FDT, rationality is not defined by myopic compliance with past evidence, nor by the futile physical isolation of an agent's immediate muscular contractions. Rationality is the selection of the optimal mathematical policy—an overarching rule whose global instantiation in the fabric of reality yields the highest expected utility. As autonomous artificial agents increasingly enter environments containing accurate emulations, source-code verifiers, and reciprocal algorithmic peers, P-FDT provides the mathematical blueprint for coherent, stable, and un-blackmailable decision-making.

---

## References

- Ahmed, Arif. 2014. *Evidence, Decision and Causality*. Cambridge University Press.
- Dai, Wei. 2009. "Towards a New Decision Theory." *LessWrong*.
- Drescher, Gary L. 2006. *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
- Egan, Andy. 2007. "Some Counterexamples to Causal Decision Theory." *Philosophical Review* 116 (1): 93–114.
- Gibbard, Allan, and William L. Harper. 1978. "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, edited by C. A. Hooker, J. J. Leach, and E. F. McClennen, 125–162. Reidel.
- Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, David. 1979. "Prisoners' Dilemma is a Newcomb Problem." *Philosophy & Public Affairs* 8 (3): 235–240.
- Lewis, David. 1981. "Causal Decision Theory." *Australasian Journal of Philosophy* 59 (1): 5–30.
- Nozick, Robert. 1969. "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel*, edited by Nicholas Rescher, 114–146. Reidel.
- Parfit, Derek. 1986. *Reasons and Persons*. Oxford University Press.
- Pearl, Judea. 2000. *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
- Skyrms, Brian. 1980. *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
- Soares, Nate, and Benja Fallenstein. 2015. "Toward Idealized Decision Theory." *arXiv preprint arXiv:1507.01986*.
- Spohn, Wolfgang. 2012. "Reversing 30 Years of Discussion: Why Causal Decision Theorists Should One-Box." *Synthese* 187 (1): 95–122.
- Yudkowsky, Eliezer. 2010. "Timeless Decision Theory." *The Singularity Institute*.
- Yudkowsky, Eliezer, and Nate Soares. 2017. "Functional Decision Theory: A New Theory of Instrumental Rationality." *arXiv preprint arXiv:1710.05060v2*.