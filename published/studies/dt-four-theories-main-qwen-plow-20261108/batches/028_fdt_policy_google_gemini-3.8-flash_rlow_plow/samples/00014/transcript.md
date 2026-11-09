# 028_fdt_policy_google_gemini-3.8-flash_rlow_plow / 00014

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/d7422978-e3be-4572-9391-98f21efcd1f8/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/d7422978-e3be-4572-9391-98f21efcd1f8/call_0/response.raw) · finish: `stop`

### Visible response

````text
# Deliberating Over Programs: A Mathematical Account of Policy Functional Decision Theory (P-FDT)

## 1. Introduction: From Act Selection to Policy Selection

The standard debate in normative decision theory has long been framed as a dialectic between Evidential Decision Theory (EDT; Jeffrey 1983) and Causal Decision Theory (CDT; Gibbard and Harper 1978; Lewis 1981; Joyce 1999). EDT evaluates an action by asking what news its execution would convey, formalizing hypotheticals via conditional probability:
$$P(\text{Outcome} \mid \text{Observation}, \text{Act}).$$
CDT objects that conditionalization confuses correlation with causation, prescribing that an agent instead evaluate physical interventions on her bodily actions via Judea Pearl’s $\Do$-calculus (Pearl 2000):
$$P(\text{Outcome} \mid \Do(\text{Act} = a), \text{Observation}).$$

Yet both frameworks exhibit severe pathologies when confronted with predictable agents, algorithmic copies, or strategic adversaries:
* CDT famously defects against psychological twins, two-boxes in Newcomb’s problem (Nozick 1969), succumbs to extortion in mechanical blackmail (Soares and Fallenstein 2015), and is driven into reflective instability or self-destructive mixed strategies in *Death in Damascus* (Gibbard and Harper 1978; Joyce 2012; Ahmed 2014b).
* EDT one-boxes in Newcomb's problem and cooperates with twins, but falters on the smoking lesion problem (Skyrms 1980) and collapses in scenarios like the XOR blackmail or cosmic ray problems, where it irrationally attempts to "manage the news" (Lewis 1981; Soares and Fallenstein 2015).

To overcome these pathologies, Yudkowsky and Soares (2017) introduce **Functional Decision Theory (FDT)**. The core conceptual insight of FDT is that a rational agent should not evaluate an isolated physical *token* of an action ($\Act = a$), but rather the mathematical *type*—the fixed mathematical function that the agent instantiates. In their baseline formalism, an agent with world-model $M = (P, G)$ and current observation $x$ computes:
$$\FDT(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left[ V \;\middle|\; \Do\left(\FDTvar(\underline{P}, \underline{G}, \underline{x}) = a\right) \right],$$
where $\FDTvar(\underline{P}, \underline{G}, \underline{x})$ is a variable in the agent's graphical model representing the output of her decision algorithm on inputs $(P, G, x)$.

However, Yudkowsky and Soares note an important architectural alternative in footnotes 7 and 16. In footnote 16, they write:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

We refer to this canonical, policy-level formulation as **Policy Functional Decision Theory (P-FDT)**. 

While Yudkowsky and Soares relegate policy intervention to a footnote because act-level FDT and P-FDT coincide across standard single-stage Newcomblike dilemmas, moving from act-level intervention to policy-level intervention marks a profound foundational advance. It reconciles FDT with the classic principle of dynamic consistency, provides a principled resolution to the problem of "updatelessness" (Dai 2009), eliminates the need for *ad hoc* precommitments, and supplies an elegant foundation for game-theoretic coordination.

The purpose of this essay is to provide a rigorous mathematical and philosophical account of P-FDT. We will:
1. Define the formal architecture of P-FDT, contrasting its mathematical mechanics with both CDT and standard act-level FDT.
2. Characterize *subjunctive dependence* under policy interventions.
3. Walk through classical decision dilemmas to demonstrate how P-FDT operates step-by-step.
4. Formally address the theoretical ambiguities left open in footnote 16—specifically the problem of the prior evaluation distribution and the representation of algorithmic self-reference.
5. Analyze the implications of P-FDT for game theory and dynamic consistency.

---

## 2. Formalizing P-FDT

### 2.1 Basic Formalism: States, Observations, Policies, and Graphs

Let us fix the mathematical primitives:
* $\mathcal{X}$: a countable set of possible observation histories (inputs).
* $\mathcal{A}$: a finite set of available physical actions.
* $\Pi \coloneqq \mathcal{A}^{\mathcal{X}} = \{ \pi : \mathcal{X} \to \mathcal{A} \}$: the set of pure deterministic *policies* (mappings from observations to actions).
* $\mathcal{O}$: a countable set of world outcomes.
* $\mathcal{U} : \mathcal{O} \to \mathbb{R}$: a bounded utility function, with $V \coloneqq \mathcal{U}(\Outcome)$ denoting the utility random variable.

An agent maintains a world-model $M = (P, G)$, where:
* $P$ is a joint subjective probability distribution over a set of random variables $\mathcal{V}$.
* $G = (\mathcal{V}, \mathcal{E})$ is a directed acyclic graph (DAG) representing the agent’s beliefs about causal and logical dependence structures.

In standard Pearlian causal modeling (Pearl 2000), variables represent physical events, and arrows represent physical causal mechanisms. In P-FDT, the variable set $\mathcal{V}$ is expanded to include **logical and computational entities**. Specifically, $\mathcal{V}$ includes:
1. An un-parameterized policy node, denoted $\mathbf{\Pi}^*$, representing the mathematical output of the agent's policy-selection algorithm:
   $$\mathbf{\Pi}^* \in \Pi.$$
2. Observation variables $\Obs \in \mathcal{X}$.
3. Physical action variables $\Act \in \mathcal{A}$.
4. Environmental variables, including predictions made by third parties ($\Var{Prediction}$), background facts, and outcomes ($\Outcome \in \mathcal{O}$).

In a P-FDT model, the physical action $\Act$ is causally determined by evaluating the selected policy on the actual observation:
$$\Act = \mathbf{\Pi}^*(\Obs).$$

```
        +-----------------------------------------+
        |  P-FDT Policy Node:                     |
        |  pi* = P-FDT(P, G)                      |
        +-----------------------------------------+
             |                               |
             | (Subjunctive                  | (Physical
             |  Dependence)                  |  Execution)
             v                               v
    +-----------------+             +-----------------+
    | Third-Party     |             | Physical Action |
    | Simulations /   |             | Act = pi*(Obs)  |
    | Predictions     |             +-----------------+
    +-----------------+                      |
             |                               |
             +---------------+---------------+
                             |
                             v
                    +-----------------+
                    |     Outcome     |
                    |    V = U(Out)   |
                    +-----------------+
```

### 2.2 The P-FDT Decision Rule

In act-level FDT (Equation 4 of Yudkowsky and Soares 2017), the agent performs surgery on an observation-indexed node:
$$\FDT(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left[ V \;\middle|\; \Do\left(\FDTvar(\underline{P}, \underline{G}, \underline{x}) = a\right) \right].$$
Notice that this requires the agent's graph to contain a infinite family of separate nodes $\{\FDTvar(\underline{P}, \underline{G}, \underline{x})\}_{x \in \mathcal{X}}$ (or at least one for every potential observation), and the intervention is performed *after* receiving $x$.

In contrast, **P-FDT** formalizes the agent's deliberative choice as an optimization over the global mapping $\pi \in \Pi$. The decision procedure consists of two logically distinct phases: **Policy Selection** and **Policy Execution**.

#### Phase 1: Policy Selection (Deliberation)
The agent determines the optimal policy $\pi^* \in \Pi$ by intervening globally on the policy variable $\mathbf{\Pi}^*$:

$$\text{P-FDT}(P, G) \coloneqq \argmax_{\pi \in \Pi} \mathbb{E}_{P}\left[ V \;\middle|\; \Do\left(\mathbf{\Pi}^* = \pi\right) \right]. \tag{1}$$

Crucially, this expectation is evaluated across the *entire* distribution, without conditioning on the realized observation $x$ inside the intervention operator.

#### Phase 2: Policy Execution (Action)
Upon receiving observation history $x \in \mathcal{X}$, the agent's bodily action $a \in \mathcal{A}$ is simply the evaluation of the chosen policy on that observation:

$$\Act = \pi^*(x), \quad \text{where } \pi^* = \text{P-FDT}(P, G). \tag{2}$$

If the maximizing policy in (1) is not unique, an arbitrary deterministic tie-breaking rule (e.g., lexicographic ordering under a canonical encoding) is applied to ensure that $\text{P-FDT}(P, G)$ is a well-defined mathematical function.

---

## 3. Subjunctive Dependence and Counterpossible Counterfactuals

To understand why P-FDT outperforms CDT and EDT, one must understand how it evaluates the expression:
$$\mathbb{E}\left[ V \;\middle|\; \Do(\mathbf{\Pi}^* = \pi) \right].$$

### 3.1 Causal versus Subjunctive Interventions

In CDT, the intervention $\Do(\Act = a)$ is strictly physical and local. It severs the incoming edges to $\Act$ in the causal graph $G$, setting $\Act = a$ while holding all non-downstream variables fixed at their actual or prior values. Because past events (such as a predictor’s forecast made yesterday) are not causally downstream of today's bodily movement, CDT insists:
$$P(\Var{Prediction} = \text{"two-box"} \mid \Do(\Act = \text{one-box})) = P(\Var{Prediction} = \text{"two-box"}).$$

P-FDT rejects this causal insulation. The policy $\mathbf{\Pi}^*$ is not a physical lever; it is a mathematical object—a specification of an algorithm. In any world containing predictors, twins, or automated systems that simulate or reason about the agent, those systems contain representations of $\mathbf{\Pi}^*$. 

When two physical systems compute the same algorithm or when one system contains an accurate model of another, Yudkowsky and Soares term their interdependence **subjunctive dependence**:
> "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." (Section 3)

In Pearl's graphical formalism extended to P-FDT, the policy variable $\mathbf{\Pi}^*$ acts as an upstream parent of *both*:
1. The agent's physical action: $\Act \leftarrow \mathbf{\Pi}^*$.
2. Any environmental prediction, simulation, or parallel agent that tracks this decision procedure: $\Var{Prediction} \leftarrow \mathbf{\Pi}^*$.

Therefore, the Pearlian graphical surgery $\Do(\mathbf{\Pi}^* = \pi)$ severs the incoming edges to $\mathbf{\Pi}^*$ (representing whatever meta-deliberative reasons lead to that policy) and propagates the setting $\mathbf{\Pi}^* = \pi$ downstream through all causal *and* subjunctive children. When the agent considers the counterfactual $\mathbf{\Pi}^* = \pi'$, she imagines a hypothetical world in which:
* Her own physical action in context $x$ would be $\pi'(x)$.
* Every predictor simulating her computes $\pi'$, and hence predicted $\pi'$.
* Every psychological twin computing the same algorithm executes $\pi'$.

### 3.2 The Counterpossible Status of Subjunctive Hypotheticals

A rigorous reader will note a deep foundational issue: $\text{P-FDT}$ is a fully determined mathematical function. If $\text{P-FDT}(P, G) = \pi_1$, then the antecedent $\mathbf{\Pi}^* = \pi_2$ (for $\pi_2 \neq \pi_1$) is not merely physically counterfactual; it is **logically impossible**—a *counterpossible* (Cohen 1990; Brogaard and Salerno 2007).

CDT avoids counterpossibles because it treats physical actions as free variables unmoored from the computational algorithms generating them. But as Yudkowsky and Soares argue (Section 8), this is an illusion: in a deterministic universe, a CDT agent’s physical action is just as physically and logically fixed as a mathematical theorem. CDT simply blinds itself to the logical constraints connecting the agent's computation to the predictor's simulation.

P-FDT embraces this challenge. Evaluating $\Do(\mathbf{\Pi}^* = \pi)$ requires an operational logic for counterpossible reasoning. In the graphical approximation developed by Yudkowsky and Soares, this is resolved by using the graph $G$ as an explicit axiomatic specification of how logical variations propagate: the graph explicitly declares which variables are children of the algorithm node $\mathbf{\Pi}^*$. While building $G$ purely from empirical data remains an active open problem in logical induction (Demski 2012a; Garrabrant et al. 2016), once $G$ is specified, the mathematical evaluation of $\Do(\mathbf{\Pi}^* = \pi)$ is completely rigorous and well-defined.

---

## 4. P-FDT Applied: Step-by-Step Analyses

To see how P-FDT operates in practice, we analyze three benchmark problems: Newcomb's Problem, the Transparent Newcomb Problem, and Parfit's Hitchhiker.

### 4.1 Newcomb's Problem

Recall the setup:
* Box A contains $\$1,000$.
* Box B contains either $\$1,000,000$ or $\$0$.
* An accurate predictor (reliability $r = 0.99$) placed $\$1,000,000$ in Box B iff she predicted the agent would leave Box A behind.
* The agent makes no observations before choosing: $\mathcal{X} = \{ \emptyset \}$.

#### Mathematical Formulation
The policy space consists of two constant policies:
$$\pi_{\text{one}}(\emptyset) = \text{one-box}, \quad \pi_{\text{two}}(\emptyset) = \text{two-box}.$$

In the P-FDT agent’s graph $G$, the policy node $\mathbf{\Pi}^*$ has two directed outgoing paths:
1. $\mathbf{\Pi}^* \to \Act \to \Outcome \to V$.
2. $\mathbf{\Pi}^* \to \Var{Prediction} \to \Var{Box B} \to \Outcome \to V$.

Let $U(1f) = \$1,000,000$, $U(2f) = \$1,001,000$, $U(1e) = \$0$, $U(2e) = \$1,000$.

#### Evaluating the Policies
The agent computes:
$$\mathbb{E}\left[ V \;\middle|\; \Do(\mathbf{\Pi}^* = \pi_{\text{one}}) \right] = 0.99 \cdot U(1f) + 0.01 \cdot U(1e) = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000.$$
$$\mathbb{E}\left[ V \;\middle|\; \Do(\mathbf{\Pi}^* = \pi_{\text{two}}) \right] = 0.01 \cdot U(2f) + 0.99 \cdot U(2e) = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$

Since $\$990,000 > \$11,000$, P-FDT outputs:
$$\text{P-FDT}(P, G) = \pi_{\text{one}}.$$
Applying this policy to the null observation $\emptyset$, the agent executes:
$$\Act = \pi_{\text{one}}(\emptyset) = \text{one-box}.$$

P-FDT one-boxes without hesitation. Unlike CDT, which severs $\Act$ from $\Var{Prediction}$, P-FDT intervenes on the algorithmic type $\mathbf{\Pi}^*$, correctly recognizing that a world where its algorithm outputs two-boxing is a world where the predictor anticipates two-boxing.

---

### 4.2 The Transparent Newcomb Problem and Parfit’s Hitchhiker

The true power of P-FDT becomes apparent in dynamic dilemmas with intermediate observations, where CDT and EDT both fail.

#### Problem 1: Transparent Newcomb (Drescher 2006)
Everything is identical to Newcomb's problem, except that Box B is *transparent*. The agent observes whether Box B is full ($x = \Val{full}$) or empty ($x = \Val{empty}$) before making her choice. The predictor placed $\$1,000,000$ in Box B iff she predicted that the agent, *upon observing two full boxes*, would leave Box A behind.

#### Problem 2: Parfit's Hitchhiker (Parfit 1986)
An agent is dying of thirst in the desert. A driver arrives who can carry the agent to the city, but only if the agent will pay $\$1,000$ at an ATM upon arrival. Being saved is worth $\$1,000,000$. The driver cannot legally enforce payment in the city, but is an expert lie detector (reliability $r = 0.99$). The driver leaves the agent to die unless she predicts that the agent, upon arriving safely in the city ($x = \Val{city}$), will actually withdraw the cash and pay.

#### The Failure of CDT and EDT
In both problems, once the observation arrives ($x = \Val{full}$ or $x = \Val{city}$):
* **CDT** reasons: "The past is fixed. The ride has already been given (or the box is already full). Paying $\$1,000$ (or leaving Box A behind) causally loses me $\$1,000$ with no downstream compensation. Therefore, I defect."
* **EDT** reasons: "Conditional on being in the city, learning that I pay is bad news (I lose $\$1,000$). The survival is already given as an evidential fact. Therefore, I defect."

Predicting this, the driver leaves CDT and EDT agents to die in the desert, and the Newcomb predictor leaves their boxes empty!

#### The P-FDT Resolution via Policy Selection
Let us formalize the Transparent Newcomb problem under P-FDT.
The observation space is $\mathcal{X} = \{ \Val{full}, \Val{empty} \}$.
The action space is $\mathcal{A} = \{ \Val{one-box}, \Val{two-box} \}$.
The policy space $\Pi$ contains $2^2 = 4$ policies:
$$\pi_{ij}: \text{where } \pi_{ij}(\Val{full}) = i \text{ and } \pi_{ij}(\Val{empty}) = j, \quad \text{for } i, j \in \{ \Val{one}, \Val{two} \}.$$

The predictor’s setup specifically depends on the agent’s counterfactual behavior when facing two full boxes:
$$\Var{Prediction} = \begin{cases} \Val{full} & \text{if } \mathbf{\Pi}^*(\Val{full}) = \Val{one-box} \text{ (with prob 0.99)}, \\ \Val{empty} & \text{if } \mathbf{\Pi}^*(\Val{full}) = \Val{two-box} \text{ (with prob 0.99)}. \end{cases}$$

Notice that if the predictor fills the box, the agent observes $x = \Val{full}$; if the predictor does not fill the box, the agent observes $x = \Val{empty}$.

Now, let us evaluate the expected utility of the candidate policies under the global intervention $\Do(\mathbf{\Pi}^* = \pi)$ in P-FDT (Equation 1):

1. **Candidate Policy $\pi_{\Val{one}, \Val{two}}$** (One-box if full, two-box if empty):
   * Under $\Do(\mathbf{\Pi}^* = \pi_{\Val{one}, \Val{two}})$, the predictor predicts $\Val{full}$ with probability $0.99$.
   * With probability $0.99$, Box B is full, the agent observes $\Val{full}$, executes $\pi_{\Val{one}, \Val{two}}(\Val{full}) = \Val{one-box}$, obtaining $U(1f) = \$1,000,000$.
   * With probability $0.01$, Box B is empty (predictor error), the agent observes $\Val{empty}$, executes $\pi_{\Val{one}, \Val{two}}(\Val{empty}) = \Val{two-box}$, obtaining $U(2e) = \$1,000$.
   $$\mathbb{E}\left[V \mid \Do(\mathbf{\Pi}^* = \pi_{\Val{one}, \Val{two}})\right] = 0.99(\$1,000,000) + 0.01(\$1,000) = \$990,010.$$

2. **Candidate Policy $\pi_{\Val{two}, \Val{two}}$** (Two-box regardless of what is seen):
   * Under $\Do(\mathbf{\Pi}^* = \pi_{\Val{two}, \Val{two}})$, the predictor predicts $\Val{empty}$ with probability $0.99$.
   * With probability $0.99$, Box B is empty, the agent observes $\Val{empty}$, executes $\pi_{\Val{two}, \Val{two}}(\Val{empty}) = \Val{two-box}$, obtaining $U(2e) = \$1,000$.
   * With probability $0.01$, Box B is full (predictor error), the agent observes $\Val{full}$, executes $\pi_{\Val{two}, \Val{two}}(\Val{full}) = \Val{two-box}$, obtaining $U(2f) = \$1,001,000$.
   $$\mathbb{E}\left[V \mid \Do(\mathbf{\Pi}^* = \pi_{\Val{two}, \Val{two}})\right] = 0.99(\$1,000) + 0.01(\$1,001,000) = \$990 + \$10,010 = \$11,000.$$

Comparing the expectations across all four policies:
$$\text{P-FDT}(P, G) = \pi_{\Val{one}, \Val{two}}.$$

Now consider the execution phase (Equation 2). The agent walks up to the table. She looks into the transparent box and **sees that Box B is full** ($x = \Val{full}$). 

What does she do? She does **not** re-deliberate from scratch using a localized act-intervention conditioned on $x = \Val{full}$. Rather, she faithfully applies the optimal policy chosen in Phase 1:
$$\Act = \pi^*(\Val{full}) = \pi_{\Val{one}, \Val{two}}(\Val{full}) = \Val{one-box}.$$

She leaves the $\$1,000$ in Box A behind, taking only Box B!

The logic is identical in Parfit's Hitchhiker: P-FDT selects the policy $\pi^*(\Val{city}) = \Val{pay}$. Upon finding herself safely in the city, she pays the driver the $\$1,000$. The driver foresaw this policy, gave her the ride, and she lives. Parfit's desert is littered with the bodies of CDT agents who insisted that once in the city, paying is dominated.

---

## 5. Resolving the Ambiguities in Footnote 16

Footnote 16 of Yudkowsky and Soares (2017) sketches policy selection in two sentences, leaving several deep mathematical and structural questions unaddressed:
1. **The Epistemic Timing Problem:** Exactly what probability distribution evaluates the policy expectation? Does the agent evaluate policies using her *prior* distribution before observations, or does she evaluate policies *after* an observation has arrived?
2. **The Updatelessness Problem:** If an agent evaluates policies after receiving an observation, does she condition on that observation, or does she remain "updateless"?
3. **The Self-Referential Quining Problem:** How does an agent mathematically represent the node $\mathbf{\Pi}^*$ without triggering infinite regress?

Here we provide a rigorous operational interpretation of these issues, explicitly distinguishing the core claims of Yudkowsky and Soares from our proposed formalization.

### 5.1 The Operational Interpretation: Updateless Policy Selection

In the main text of Yudkowsky and Soares (Section 6, Transparent Newcomb), the authors model act-level FDT by having Fiona change *which node she intervenes upon* based on her observation:
$$\text{Intervene on } \FDTpgv{full} \quad \text{versus} \quad \FDTpgv{empty}.$$
They observe that in her hypothetical calculation:
> "even in the case where Fiona has observed that box B is full, when she *envisions* two-boxing, she envisions a scenario where she instead (with high probability) sees that the box is empty."

When translated to P-FDT, this behavior reveals the foundational structure of the theory. There are two competing interpretations of how P-FDT could be formalized:

* **Interpretation A (Update-Then-Deliberate):** The agent observes $x$, updates her distribution to $P(\cdot \mid \Obs = x)$, and then finds the policy that maximizes expected utility conditional on that observation:
  $$\pi^*_x = \argmax_{\pi \in \Pi} \mathbb{E}\left[ V \;\middle|\; \Do(\mathbf{\Pi}^* = \pi), \Obs = x \right].$$
* **Interpretation B (Global / Updateless Policy Deliberation):** The agent always evaluates policies relative to her *root prior* $P$ (the model of the dilemma before any observations are realized), selects a global policy $\pi^*$, and then executes $\Act = \pi^*(x)$:
  $$\pi^* = \argmax_{\pi \in \Pi} \mathbb{E}_{P}\left[ V \;\middle|\; \Do(\mathbf{\Pi}^* = \pi) \right].$$

#### Why Interpretation B is Mathematically Superior
We argue that **Interpretation B** is the only coherent operationalization of footnote 16. 

If an agent follows Interpretation A, she conditions on $\Obs = \Val{full}$ *before* intervening on $\mathbf{\Pi}^*$. But under Pearlian graphical mechanics, conditioning on a child variable $\Obs = \Val{full}$ can freeze or distort the evidential pathways from upstream nodes (activating "explaining away" effects via collider stratification). More dangerously, if an agent conditions on already being in the city ($x = \Val{city}$ in Parfit's hitchhiker), any variation of $\pi$ that would have caused the driver not to give the ride becomes probabilistically inconsistent or requires singular conditioning!

Under Interpretation B, P-FDT embodies the core philosophy of **Updateless Decision Theory (UDT)** (Dai 2009). The agent does not ask: "Given that I have observed $x$, which policy is best?" She asks:
$$\text{"Which policy function, computed and deployed by my cognitive system across all possibilities, produces the highest overall expected utility?"}$$

This global expectation is cleanly decomposed over the possible observation histories:
$$\mathbb{E}_P\left[ V \;\middle|\; \Do(\mathbf{\Pi}^* = \pi) \right] = \sum_{x \in \mathcal{X}} P(\Obs = x \mid \Do(\mathbf{\Pi}^* = \pi)) \cdot \mathbb{E}_P\left[ V \;\middle|\; \Do(\mathbf{\Pi}^* = \pi), \Obs = x \right]. \tag{3}$$

Equation (3) reveals why P-FDT achieves dynamic consistency. The value of a policy $\pi$ explicitly weights the utility obtained in branch $x$ by the probability $P(\Obs = x \mid \Do(\mathbf{\Pi}^* = \pi))$ that adopting policy $\pi$ causes that observation branch to be reached! 

In Parfit's hitchhiker, adopting the policy $\pi(\Val{city}) = \Val{refuse}$ causes $P(\Obs = \Val{city} \mid \Do(\mathbf{\Pi}^* = \pi)) \approx 0.01$. Even though *conditional* on reaching the city the agent would save $\$1,000$, the policy-level intervention accounts for the fact that this policy destroys the probability of ever arriving at the city in the first place.

### 5.2 Formalizing Self-Reference via Gödelian Quining

Equation (1) defines $\text{P-FDT}(P, G)$ as an argmax over an expectation involving $\Do(\mathbf{\Pi}^* = \pi)$. But inside the model $(P, G)$, what is the variable $\mathbf{\Pi}^*$?

As Yudkowsky and Soares note in Section 5, $\mathbf{\Pi}^*$ is the symbolic representation of the algorithm itself:
$$\mathbf{\Pi}^* \equiv \text{P-FDT}(\underline{P}, \underline{G}).$$
This introduces apparent self-reference: the definition of the function $\text{P-FDT}$ refers to a graph $G$ which contains a node representing $\text{P-FDT}$.

To put this on solid mathematical ground, we appeal to **Kleene's Second Recursion Theorem** (Kleene 1938). Let $\text{Code}(P, G)$ be a finite Gödel encoding of the agent’s model. By the recursion theorem, any computable function can access its own source code. The node $\mathbf{\Pi}^*$ is not a magical metaphysical entity; it is a designated discrete variable in the probabilistic network whose structural equation is evaluated by running the quined program $\text{P-FDT}(\underline{P}, \underline{G})$. 

When the agent evaluates $\Do(\mathbf{\Pi}^* = \pi)$, she is performing standard causal/counterpossible graph surgery: she temporarily replaces the structural equation determining $\mathbf{\Pi}^*$ with the constant value $\pi$, and computes the resulting distribution over $V$. There is no circularity or infinite regress.

---

## 6. The Mechanics of Deliberation: A Comparison of Decision Theories

We can now cleanly contrast how the major decision theories construct and evaluate their decision hypotheticals.

| Theory | Object of Choice | Mathematical Operator | Hypothetical Evaluated |
| :--- | :--- | :--- | :--- |
| **EDT** | Physical Act $a \in \mathcal{A}$ | Bayesian Conditioning | $\mathbb{E}\left[ V \mid \Obs = x, \Act = a \right]$ |
| **CDT** | Physical Act $a \in \mathcal{A}$ | Physical Intervention | $\mathbb{E}\left[ V \mid \Do(\Act = a), \Obs = x \right]$ |
| **Act-FDT** | Act Token $a \in \mathcal{A}$ | Localized Logical $\Do$ | $\mathbb{E}\left[ V \mid \Do(\FDTvar(\underline{P}, \underline{G}, \underline{x}) = a) \right]$ |
| **P-FDT** | Global Policy $\pi \in \Pi$ | Global Logical $\Do$ | $\mathbb{E}_P\left[ V \mid \Do(\mathbf{\Pi}^* = \pi) \right]$ |

### Why P-FDT Dominates Act-FDT
While Act-FDT and P-FDT agree on standard problems like Newcomb's problem, act-level FDT suffers from structural clumsiness when handling observations. 

In act-level FDT, when Fiona observes that Box B is full in Transparent Newcomb, she must intervene on $\FDTvar(\underline{P}, \underline{G}, \Val{full})$, but she must deliberately avoid conditioning on the observation variable $\Obs = \Val{full}$ in the ordinary Bayesian way, because conditioning on the observation would break the subjunctive link to the predictor's past action. Yudkowsky and Soares describe this as: "Fiona reacts to observations by switching which variable she intervenes on, rather than conditioning."

P-FDT dissolves this conceptual awkwardness entirely. In P-FDT:
1. Deliberation is purely over the policy $\pi \in \Pi$.
2. The agent never "refuses to condition" or performs weird gymnastics with evidence.
3. The policy optimization (Equation 1) is conducted globally. Once $\pi^*$ is chosen, observation processing is entirely standard: the agent simply feeds $x$ into $\pi^*(x)$ and acts.

---

## 7. Strategic and Game-Theoretic Implications

The shift to policy-level functional decision theory has radical implications for multi-agent game theory.

### 7.1 Dynamic Consistency Without Precommitment
In classical economic theory, an agent faced with problems like Parfit's Hitchhiker suffers from **dynamic inconsistency** (Strotz 1955). At time $t_0$ (in the desert), she wishes she could bind her future self to pay $\$1,000$. But at time $t_1$ (in the city), her preferences change: the benefit is sunk, and paying is a pure loss. Causal agents therefore rely on costly external commitment mechanisms—such as escrow contracts, posting collateral, or neurochemically altering their brains.

P-FDT completely solves the problem of dynamic consistency **without physical precommitment mechanisms**. 

A P-FDT agent does not need to alter her physical brain or sign binding contracts, because her deliberative architecture evaluates whole policies from the global perspective. Since $\pi^*$ was selected because of its global expected utility, the agent at $t_1$ does not experience any temptation to re-deliberate locally. She recognizes that she is an execution step of the algorithm $\text{P-FDT}(P, G)$, and executing $\pi^*(x)$ is what makes her the kind of agent that gets rescued.

### 7.2 Defeating Blackmail and Extortion
Consider the *Mechanical Blackmail* problem (Dilemma 6 in Yudkowsky and Soares 2017):
A blackmailer has incriminating information that would ruin both the agent and the blackmailer (costing $\$1,000,000$). The blackmailer builds an automated program that releases the info unless the agent pays $\$1,000$. But the blackmailer only launches the program if she predicts the agent will pay upon receiving the letter.

A CDT agent who receives the letter pays: $\$1,000$ is better than $\$1,000,000$. CDT agents are thus universal extortion magnets.

What does P-FDT do?
Let $\mathcal{X} = \{ \Val{letter}, \emptyset \}$.
The candidate policies are:
* $\pi_{\Val{pay}}$: Set $\pi(\Val{letter}) = \Val{pay}$.
* $\pi_{\Val{refuse}}$: Set $\pi(\Val{letter}) = \Val{refuse}$.

Under $\Do(\mathbf{\Pi}^* = \pi_{\Val{pay}})$, the blackmailer predicts payment, launches the attack, the agent sees $\Val{letter}$, pays $\$1,000$, and nets:
$$\mathbb{E}[V \mid \Do(\mathbf{\Pi}^* = \pi_{\Val{pay}})] = -\$1,000.$$

Under $\Do(\mathbf{\Pi}^* = \pi_{\Val{refuse}})$, the blackmailer predicts defiance. Because releasing the data hurts the blackmailer too, the blackmailer aborts! The program is never launched, the agent never receives a letter ($\Obs = \emptyset$), and no money is lost:
$$\mathbb{E}[V \mid \Do(\mathbf{\Pi}^* = \pi_{\Val{refuse}})] = \$0.$$

P-FDT selects $\pi^* = \pi_{\Val{refuse}}$. The blackmailer never sends the letter, and the P-FDT agent is completely immune to extortion.

What if the blackmailer is imperfect and sends the letter by accident (noise)? Under P-FDT, even if the agent is holding the letter in her hands, her policy dictates $\pi^*(\Val{letter}) = \Val{refuse}$. She drops the letter in the wastebasket. She does this not out of spite, but because the mathematical policy she instantiates is one that does not incentivize extortion in any possible branch.

### 7.3 Multi-Agent Coordination and Twin Dilemmas
In the Psychological Twin Prisoner's Dilemma, two identical P-FDT agents face each other. Both agents compute $\mathbf{\Pi}^* = \text{P-FDT}(P, G)$. 

When Agent 1 evaluates $\Do(\mathbf{\Pi}^* = \pi)$, she knows that Agent 2 is running the identical code. Therefore:
$$\Act_1 = \pi(\emptyset), \quad \Act_2 = \pi(\emptyset).$$
The candidate policies are $\pi_C$ (cooperate) and $\pi_D$ (defect).
$$\mathbb{E}\left[ V \mid \Do(\mathbf{\Pi}^* = \pi_C) \right] = U(\text{Both Cooperate}) = \$1,000,000.$$
$$\mathbb{E}\left[ V \mid \Do(\mathbf{\Pi}^* = \pi_D) \right] = U(\text{Both Defect}) = \$1,000.$$

P-FDT naturally selects $\pi_C$, achieving mutual cooperation effortlessly where CDT collapses into mutual defection.

---

## 8. Open Mathematical Challenges for P-FDT

While P-FDT provides an extraordinarily powerful framework, several fundamental mathematical challenges remain open:

1. **Formalizing the Space of Subjunctive Graphs:** Pearl provided a rigorous axiomatization of how causal graphs can be learned from observational and interventional data (Pearl 2000). Decision theorists do not yet have an analogous complete axiomatization for learning *subjunctive* graphs containing computational dependencies. How should an agent automatically discover that an external system is running an emulation of her policy?
2. **Infinite Observation Spaces and Computational Complexity:** If $\mathcal{X}$ is continuous or arbitrarily large, the policy space $\Pi = \mathcal{A}^{\mathcal{X}}$ becomes infinite or computationally intractable. An agent cannot literally evaluate all functions $\pi$. A realistic P-FDT agent must search over a restricted class of heuristic computer programs, introducing bounded-rationality constraints and algorithmic approximations.
3. **Priors Over Logical Counterpossibles:** In Equation (1), computing the expectation requires assigning subjective probabilities to outcomes under counterpossible operations $\Do(\mathbf{\Pi}^* = \pi)$. Developing a mathematically sound foundation for probabilities over logical statements has advanced through the framework of *Logical Induction* (Garrabrant et al. 2016), but integrating logical induction fully into the graphical $\Do$-calculus remains at the frontier of theoretical AI research.

---

## 9. Conclusion

Classical causal decision theory made a fateful modeling choice: it located the agent's decision at the level of the isolated physical act-token, severing the choice from the mathematical algorithm that produced it. This blinded CDT to the rich tapestry of subjunctive dependencies that characterize environments containing predictors, twins, code inspections, and strategic adversaries.

**Policy Functional Decision Theory (P-FDT)** repairs this foundational flaw. As indicated in footnote 16 of Yudkowsky and Soares (2017), rational deliberation is most properly understood not as choosing an act, but as **selecting an entire policy mapping via a global subjunctive intervention**:
$$\text{P-FDT}(P, G) = \argmax_{\pi \in \Pi} \mathbb{E}_P\left[ V \;\middle|\; \Do(\mathbf{\Pi}^* = \pi) \right].$$

By shifting the locus of choice from act to policy:
* P-FDT achieves dynamic consistency across time without relying on costly precommitment mechanisms.
* It cleanly operationalizes updateless reasoning, resolving Parfit's hitchhiker problem and the Transparent Newcomb problem in a unified, mathematically transparent stroke.
* It resists blackmail, coordinates with copies, and maximizes expected utility across an expansive class of decision problems where both CDT and EDT systematically fail.

P-FDT demonstrates that instrumental rationality does not consist in asking "What physical movement should my fingers make right now?", but rather: *"Which mathematical program would I have wanted the universe to run?"* In an increasingly algorithmic world populated by predictive systems and intelligent machines, P-FDT provides our most promising glimpse into the true nature of rational agency.

---

## References

* Ahmed, Arif. 2014. *Evidence, Decision and Causality*. Cambridge University Press.
* Ahmed, Arif. 2014b. "Dicing with Death." *Analysis* 74 (4): 587–592.
* Brogaard, Berit, and Joe Salerno. 2007. "Why Counterpossibles Are Non-Trivial." *The Reasoner* 1: 5–6.
* Cohen, Daniel. 1990. "On What Cannot Be." In *Truth or Consequences: Essays in Honor of Nuel Belnap*, edited by J. Michael Dunn and Anil Gupta, 123–132. Kluwer Academic Publishers.
* Dai, Wei. 2009. "Towards a New Decision Theory." *LessWrong* (August 13, 2009).
* Demski, Abram. 2012a. "Logical Prior Probability." In *Artificial General Intelligence (AGI 2012)*, LNCS 7716: 50–59. Springer.
* Drescher, Gary L. 2006. *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Garrabrant, Scott, Tsvi Benson-Tilsen, Andrew Critch, Nate Soares, and Jessica Taylor. 2016. "Logical Induction." arXiv:1609.03543 [cs.AI].
* Gibbard, Allan, and William L. Harper. 1978. "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, edited by C. A. Hooker et al., 125–162. D. Reidel.
* Jeffrey, Richard C. 1983. *The Logic of Decision*. 2nd ed. University of Chicago Press.
* Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Joyce, James M. 2012. "Regret and Instability in Causal Decision Theory." *Synthese* 187 (1): 123–145.
* Kleene, Stephen Cole. 1938. "On Notation for Ordinal Numbers." *Journal of Symbolic Logic* 3 (4): 150–155.
* Lewis, David. 1981. "Causal Decision Theory." *Australasian Journal of Philosophy* 59 (1): 5–30.
* Nozick, Robert. 1969. "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel*, edited by Nicholas Rescher, 114–146. D. Reidel.
* Parfit, Derek. 1986. *Reasons and Persons*. Oxford University Press.
* Pearl, Judea. 2000. *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Skyrms, Brian. 1980. *Causal Necessity*. Yale University Press.
* Soares, Nate, and Benja Fallenstein. 2015. "Toward Idealized Decision Theory." arXiv:1507.01986 [cs.AI].
* Strotz, Robert H. 1955. "Myopia and Inconsistency in Dynamic Utility Maximization." *Review of Economic Studies* 23 (3): 165–180.
* Yudkowsky, Eliezer, and Nate Soares. 2017. "Functional Decision Theory: A New Theory of Instrumental Rationality." arXiv:1710.05060 [cs.AI].
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
