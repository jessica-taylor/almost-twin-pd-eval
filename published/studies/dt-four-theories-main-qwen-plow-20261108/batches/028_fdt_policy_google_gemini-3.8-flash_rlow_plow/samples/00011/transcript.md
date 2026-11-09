# 028_fdt_policy_google_gemini-3.8-flash_rlow_plow / 00011

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/3bc3970f-854b-4388-a484-ca2bbe223113/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/3bc3970f-854b-4388-a484-ca2bbe223113/call_0/response.raw) · finish: `stop`

### Visible response

````text
# Policy Functional Decision Theory: Foundations, Formalisms, and Global Counterfactuals

---

## 1. Introduction: From Acts to Algorithms to Policies

Standard formal decision theory has long revolved around an entrenched dispute between **evidential decision theory (EDT)** and **causal decision theory (CDT)**. The core of this dispute concerns how an agent ought to conceptualize hypothetical departures from reality. EDT evaluates prospective actions by Bayesian conditioning: an action is desirable to the degree that learning one took it constitutes good news. CDT evaluates prospective actions via causal interventions: an action is desirable to the degree that its physical execution causally brings about valuable consequences, holding the non-effects of the action fixed.

Both frameworks run into severe normative failures. In Newcomb-like dilemmas, CDT’s insistence on holding the past fixed causes agents to defect against psychological twins and take two boxes against infallible predictors, walking away impoverished. Conversely, EDT’s reliance on simple observational conditioning leads agents to manage the news in common-cause settings—such as refraining from smoking in the smoking lesion problem, or succumbing to extortion in Soares and Fallenstein’s XOR blackmail problem.

To resolve these tensions, Yudkowsky and Soares introduce **functional decision theory (FDT)**. Rather than intervening on a physical act token in the world, an FDT agent intervenes on the *mathematical type* of its own decision function:

$$\text{“Which output of this very mathematical function produces the best outcome?”}$$

By taking the object of intervention to be the output of an abstract algorithm instantiated across physical reality, FDT preserves logical and subjunctive correlations between the agent's deliberations and external predictors, twins, and models, while discarding merely statistical common causes.

However, the primary exposition of FDT in Yudkowsky and Soares still formalizes deliberation as an act-selection procedure conditioned on an observation: the agent observes $x$, and then intervenes on $\FDTvar(\underline{P}, \underline{G}, \underline{x}) = a$. While the authors note that this suffices for single-stage scenarios, they highlight an alternative, deeper formulation in footnotes 7 and 16. In footnote 16, they write:

> “As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition.”

We refer to this formulation as **policy functional decision theory (P-FDT)**. 

Under P-FDT, rationality is not a property of isolated physical actions, nor is it an act-level calculation indexed strictly to the observation history at hand. Instead, P-FDT treats normative deliberation as **the selection of an optimal mapping from observation histories to acts: a policy $\pi \colon \mathcal{X} \to \mathcal{A}$**. Deliberation is carried out from an *ex ante* or "global" perspective: the agent evaluates the counterfactual consequences of their overarching algorithm implementing policy $\pi$, and subsequently applies the winning policy $\pi^*$ to their actual observation $x$.

This essay develops a comprehensive, mathematically rigorous account of P-FDT. We will establish its formal foundations, explicate its treatment of subjunctive counterfactuals, contrast its mechanics with act-FDT, CDT, and EDT, analyze its performance across critical dilemmas, and address the open mathematical questions inherent in policy-level functional choice.

---

## 2. Foundations and Core Concepts

To formalize P-FDT, we must clarify three interconnected primitives: the policy space, the nature of subjunctive dependence, and the global perspective.

### 2.1. The Deliberative Domain: Actions vs. Policies
Let:
- $\mathcal{X}$ be a countable space of possible observation histories (sensory data, past outcomes, evidential signals).
- $\mathcal{A}$ be a finite space of available physical actions.
- $\mathcal{O}$ be a countable set of world outcomes.
- $\mathcal{U} \colon \mathcal{O} \to \mathbb{R}$ be a bounded von Neumann–Morgenstern utility function, with random variable $V \coloneqq \mathcal{U}(\Outcome)$.

In standard act-level frameworks (CDT, EDT, and standard act-FDT), an agent who observes $x \in \mathcal{X}$ computes:

$$\argmax_{a \in \mathcal{A}} \mathbb{E}\left[V \;\middle|\; a \text{ taken given } x\right]$$

In **P-FDT**, the foundational object of optimization is not an act $a \in \mathcal{A}$, but a policy $\pi$ residing in the function space:

$$\Pi \coloneqq \mathcal{A}^\mathcal{X} = \{ \pi \colon \mathcal{X} \to \mathcal{A} \}$$

An agent in P-FDT selects the optimal policy $\pi^* \in \Pi$ by evaluating which complete behavioral strategy yields the highest expected utility across the entire system. Once $\pi^*$ is chosen, the actual physical act executed in the world is determined purely by function evaluation:

$$a = \pi^*(x)$$

### 2.2. Subjunctive Dependence vs. Causal and Evidential Dependence
Let $\mathbb{M}$ denote the agent's world-model. In classical causal decision theory, hypothetical evaluation relies on Judea Pearl’s causal directed acyclic graphs (DAGs) and the causal graph surgery operator $\Do(\Act = a)$. The $\Do$-operator severs all incoming causal edges to the physical act node $\Act$ and sets its value to $a$, propagating effects purely downstream along directed causal paths.

This causal counterfactual fails when the environment contains external processes whose states depend on the agent’s reasoning without being causally downstream of the physical act. Such scenarios include:
1. **Predictors:** An external agent simulates or models the agent's code prior to the decision (as in Newcomb’s Problem, Parfit’s Desert, and Blackmail).
2. **Psychological Twins:** Multiple agents implement the identical decision procedure in parallel without communication (as in the Twin Prisoner's Dilemma).
3. **Internal Temporal Consistency:** Past or future iterations of the agent execute the same underlying decision algorithm.

P-FDT models these relationships through **subjunctive dependence**. Formally, two physical variables $Y_1$ and $Y_2$ subjunctively depend on an abstract function $F$ if both physical systems run physical implementations of $F$, such that the values of $Y_1$ and $Y_2$ are constrained by the logical output of $F$. 

In the language of Charles Sanders Peirce’s type-token distinction, CDT intervenes on a localized physical **token** (the bodily movement at time $t$). P-FDT intervenes on the mathematical **type** (the policy function computed by the deliberative process).

### 2.3. The Global (Updateless) Perspective
A central conceptual hallmark of P-FDT is its radical departure from conventional Bayesian updating during deliberation. In standard decision models, observing $x \in \mathcal{X}$ prompts an immediate Bayesian update: the prior $P(-)$ is conditioned on $\Obs = x$ to yield $P(- \mid x)$, and deliberation occurs entirely inside this conditioned submodel.

P-FDT recognizes that in the presence of predictive subjunctive dependencies, the observation $x$ that the agent receives is itself an endogenously determined outcome of what policy the agent implements! 

If an agent conditions on $\Obs = x$ prior to selecting its policy or action, it throws away its counterfactual influence over whether it receives observation $x$ in the first place. P-FDT therefore adopts what Yudkowsky and Soares call the **global perspective**: the agent deliberates from an unconditioned ("updateless") vantage point, selecting the global policy $\pi \in \Pi$ that produces the optimal distribution over observations, interactions, and outcomes.

---

## 3. Mathematical Formalization of P-FDT

We now construct a formal mathematical framework for P-FDT. We build upon the graphical causal framework of Pearl (2000), expanding it to accommodate logical variables as introduced in the reference paper.

### 3.1. World-Models with Logical Nodes
Let a P-FDT world-model be a pair $(P, G)$, where:
- $P$ is a probability distribution defined over a set of random variables.
- $G = (V_G, E_G)$ is an extended directed acyclic graph representing both causal and subjunctive dependencies.

Crucially, the vertex set $V_G$ contains a distinguished logical node:

$$\mathbf{\Pi}_{\text{agent}} \coloneqq \Var{pfdt}(\underline{P}, \underline{G})$$

Here, the underline denotes quotation/Gödel-coding: $\Var{pfdt}(\underline{P}, \underline{G})$ represents the output of the P-FDT algorithm when run on the agent's own world-model $(P, G)$. By Kleene’s second recursion theorem, this mathematical self-reference is mathematically consistent; an algorithm can manipulate a representation of its own global code without paradox.

The graph $G$ contains directed edges outgoing from $\Var{pfdt}(\underline{P}, \underline{G})$ to every variable in the universe that subjunctively or causally depends on the agent’s adopted policy:
1. It connects to the agent’s physical action node: $\Act = \Var{pfdt}(\underline{P}, \underline{G})(\Obs)$.
2. It connects to external predictors’ models: $\Var{Prediction} = \mathcal{M}(\Var{pfdt}(\underline{P}, \underline{G}))$.
3. It connects to twin agents: $\Act_{\text{twin}} = \Var{pfdt}(\underline{P}, \underline{G})(\Obs_{\text{twin}})$.

### 3.2. The P-FDT Optimization Rule
We can now write the formal mathematical definition of P-FDT. Rather than evaluating actions after conditioning on observations, P-FDT maximizes the expected utility of the global policy intervention:

```
[Definition: P-FDT Policy Selection]
Given a world-model (P, G), the optimal policy π* is defined by:

    π* = argmax_{π ∈ Π} E[ V | do(pfdt(P, G) = π) ]                           (5)

where do(pfdt(P, G) = π) represents Pearl graph surgery setting the 
global logical variable pfdt(P, G) to policy π.
```

Once the optimal policy $\pi^*$ is computed by Equation (5), the agent executing P-FDT observes their actual current history $x \in \mathcal{X}$ and emits the action prescribed by $\pi^*$:

$$\text{P-FDT}(P, G, x) \coloneqq \pi^*(x)$$

### 3.3. Mathematical Comparison of Decision Rules
To make the architectural differences between paradigms unambiguous, we juxtapose the operational formulas for EDT, CDT, standard act-FDT, and P-FDT:

#### 1. Evidential Decision Theory (EDT)
EDT updates on observations, conditions on the physical act, and respects all statistical correlations:
$$\EDT(P, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left[V \;\middle|\; \Obs = x, \Act = a\right]$$

#### 2. Causal Decision Theory (CDT)
CDT updates on observations, intervenes via graph surgery on the physical act token, and severs all non-causal correlations:
$$\CDT(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left[V \;\middle|\; \Do(\Act = a), \Obs = x\right]$$

#### 3. Standard Act-Level Functional Decision Theory (Act-FDT)
Act-FDT does not condition on observation $x$; instead, it shifts the node of intervention to a logical variable parameterized by the specific observation $x$:
$$\FDT(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left[V \;\middle|\; \Do\left(\FDTvar(\underline{P}, \underline{G}, \underline{x}) = a\right)\right]$$

#### 4. Policy Functional Decision Theory (P-FDT)
P-FDT optimizes across the entire functional mapping space $\Pi = \mathcal{A}^\mathcal{X}$ at the root logical node, and then applies the resulting policy to observation $x$:
$$\pi^* \coloneqq \argmax_{\pi \in \mathcal{A}^\mathcal{X}} \mathbb{E}\left[V \;\middle|\; \Do\left(\Var{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right], \quad \text{P-FDT}(P, G, x) \coloneqq \pi^*(x)$$

---

## 4. Resolving Open Questions: Operationalizing Policy Interventions

While Footnote 16 introduces the principle of policy selection, it leaves key formal mechanics unelaborated. Specifically:
1. How does graph surgery propagate across a policy-valued random variable?
2. How should P-FDT proceed if multiple policies achieve identical global expected utility but prescribe different actions on observation $x$?
3. How are counterfactuals evaluated when the observation space $\mathcal{X}$ is continuous or infinite?

We present precise, mathematically principled operationalizations of these issues, distinguishing our proposals from the base text.

### 4.1. Graph Surgery Under Policy Interventions (Our Formal Proposal)
In Pearl's standard graphical framework, nodes represent variables taking discrete or real values. In P-FDT, the node $\Var{pfdt}(\underline{P}, \underline{G})$ takes a value in the function space $\Pi = \mathcal{A}^{\mathcal{X}}$.

Let $G$ be the dependency DAG. When we execute $\Do(\Var{pfdt}(\underline{P}, \underline{G}) = \pi)$:
1. All incoming arrows to $\Var{pfdt}(\underline{P}, \underline{G})$ are deleted.
2. The value of $\Var{pfdt}(\underline{P}, \underline{G})$ is fixed to the deterministic mathematical function $\pi \colon \mathcal{X} \to \mathcal{A}$.
3. For any node $Y$ in $G$ whose structural equation takes $\Var{pfdt}$ as an argument, $Y$ evaluates using $\pi$.

Specifically, consider the agent's physical action node $\Act$. In nature, $\Act$ has structural equation:

$$\Act \coloneqq f_{\Act}(\Var{pfdt}(\underline{P}, \underline{G}), \Obs, U_{\Act})$$

Under the intervention $\Do(\Var{pfdt} = \pi)$, this structural equation simplifies directly to:

$$\Act = \pi(\Obs)$$

Notice the structural elegance of this formulation: $\Obs$ is **not** set by intervention. Rather, $\Obs$ is determined by the background variables and environmental processes (which may themselves depend on $\Var{Prediction}$, which depends on $\pi$). The physical act $\Act$ naturally tracks the output of $\pi$ applied to whatever observation $\Obs$ actually arises under policy $\pi$.

### 4.2. Resolving Indifference: The Sub-Policy Consistency Principle (Our Proposal)
A subtle mathematical problem arises when a decision scenario involves counterfactual branches that have zero probability under a candidate policy $\pi$.

Suppose policy $\pi_1$ causes the agent to never receive observation $x_0$ (i.e., $P(\Obs = x_0 \mid \Do(\Var{pfdt} = \pi_1)) = 0$). Then the action specified by $\pi_1(x_0)$ has zero weight in the global expectation Equation (5). If an agent unexpectedly finds itself facing $x_0$ (perhaps due to an unanticipated environmental perturbation or an imperfect predictor), what action does it execute?

To make P-FDT fully operational across all possible observation histories, we propose the **Sub-Policy Consistency Principle**:

```
[Proposal: Lexicographic Sub-Policy Optimization]
Let Π_0 = Π. For an agent who finds itself at observation history x ∈ X:
1. Define Π* = argmax_{π ∈ Π} E[ V | do(pfdt = π) ].
2. If |{ π(x) : π ∈ Π* }| > 1, the agent breaks ties by choosing the policy 
   that maximizes expected utility conditional on reaching x:
   
   π** = argmax_{π ∈ Π*} E[ V | do(pfdt = π), Obs = x ]
   
3. Execute a = π**(x).
```

This ensures that P-FDT agents maintain optimal global precommitments while retaining rational, regret-free prescriptions even when pushed into zero-probability informational states.

---

## 5. Walkthrough of Canonical Decision Problems

To observe the power and mechanics of P-FDT, we analyze how it navigates the core decision dilemmas that break CDT and EDT, and examine where it agrees with or transcends act-FDT.

```
+---------------------------+-----------+-----------+-----------+-----------+
| Dilemma                   |    EDT    |    CDT    |  Act-FDT  |   P-FDT   |
+---------------------------+-----------+-----------+-----------+-----------+
| Newcomb's Problem         | 1-box     | 2-box     | 1-box     | 1-box     |
| Smoking Lesion Problem    | Refrain   | Smoke     | Smoke     | Smoke     |
| Parfit's Hitchhiker       | Die       | Die       | Pay       | Pay       |
| Transparent Newcomb       | 2-box     | 2-box     | 1-box     | 1-box     |
| Mechanical Blackmail      | Pay       | Pay       | Refuse    | Refuse    |
+---------------------------+-----------+-----------+-----------+-----------+
```

### 5.1. Newcomb's Problem
In classic Newcomb's problem, there are two boxes: Box A (containing \$1,000) and Box B (containing \$1,000,000 or \$0). A reliable predictor predicts whether the agent takes only Box B (one-boxes) or takes both boxes (two-boxes). The agent has empty observation history before choosing: $\mathcal{X} = \{ \emptyset \}$.

The policy space consists of two constant functions:
$$\Pi = \{ \pi_{\text{one}}, \pi_{\text{two}} \}, \quad \text{where } \pi_{\text{one}}(\emptyset) = \Val{onebox}, \; \pi_{\text{two}}(\emptyset) = \Val{twobox}$$

The graphical model $G$ encodes the structural equations:
$$\Var{Prediction} = \begin{cases} \Val{oneboxer} & \text{with prob } 0.99 \text{ if } \Var{pfdt} = \pi_{\text{one}}, \text{ else } 0.01 \\ \Val{twoboxer} & \text{with prob } 0.99 \text{ if } \Var{pfdt} = \pi_{\text{two}}, \text{ else } 0.01 \end{cases}$$
$$\Var{Box B} = \begin{cases} \$1,000,000 & \text{if } \Var{Prediction} = \Val{oneboxer} \\ \$0 & \text{if } \Var{Prediction} = \Val{twoboxer} \end{cases}$$
$$\Act = \Var{pfdt}(\emptyset)$$
$$V = \Var{Box B} + [\$1,000 \text{ if } \Act = \Val{twobox} \text{ else } \$0]$$

P-FDT evaluates the global interventions:
$$\mathbb{E}[V \mid \Do(\Var{pfdt} = \pi_{\text{one}})] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000$$
$$\mathbb{E}[V \mid \Do(\Var{pfdt} = \pi_{\text{two}})] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000$$

Since $\$990,000 > \$11,000$, P-FDT identifies $\pi^* = \pi_{\text{one}}$ and executes $\pi^*(\emptyset) = \Val{onebox}$. 

Unlike CDT (which performs $\Do(\Act = \Val{twobox})$, severing the link to the predictor and taking both boxes to its detriment), P-FDT captures the logical dependence of the predictor on the adopted policy.

### 5.2. The Smoking Lesion Problem
In the smoking lesion dilemma, an arterial lesion causes both lung cancer ($99\%$ mortality) and an internal preference/predisposition toward smoking. Smoking itself yields an extra $\$1,000$ in utility, but does not cause cancer.

Here, the lesion is a natural biological condition, not an entity simulating the agent’s mathematical policy. In the graph $G$, the node $\Var{Lesion}$ has no incoming edge from $\Var{pfdt}(\underline{P}, \underline{G})$.
- Under $\Do(\Var{pfdt} = \pi_{\text{smoke}})$, $P(\Var{Lesion} = \Val{true})$ is strictly unchanged.
- Under $\Do(\Var{pfdt} = \pi_{\text{refrain}})$, $P(\Var{Lesion} = \Val{true})$ is likewise unchanged.

Evaluating expected utility under P-FDT:
$$\mathbb{E}[V \mid \Do(\Var{pfdt} = \pi_{\text{smoke}})] = \mathbb{E}[V \mid \Do(\Var{pfdt} = \pi_{\text{refrain}})] + \$1,000$$

P-FDT selects $\pi^* = \pi_{\text{smoke}}$ and smokes. It avoids EDT’s irrational refusal to smoke: EDT mistakenly conditions on its action ($P(\Var{Cancer} \mid \Act = \Val{smoke})$), conflating correlation with causation. P-FDT understands that cancer does not subjunctively depend on its decision policy.

### 5.3. Parfit’s Hitchhiker and Transparent Newcomb: Why Policy Selection is Coherent
The true divergence between act-based intuition and functional decision theory appears in dilemmas where information is revealed *before* the action is taken.

In **Parfit’s Hitchhiker**, an agent is stranded in a desert facing certain death (loss of $\$1,000,000$). A driver arrives who can detect lies with near-perfect accuracy ($99\%$). The driver will rescue the agent if and only if she predicts that, upon reaching the city, the agent will withdraw $\$1,000$ from an ATM and pay her. 

Suppose the agent is safely in the city ($\Obs = \Val{city}$).
- **CDT Reasoning:** "I am already in the city. The ride is in the past. Severing all outgoing causal links, paying $\$1,000$ merely causes me to lose $\$1,000$. I refuse to pay." The driver predicts this and leaves the CDT agent to die.
- **EDT Reasoning:** "Conditioning on paying, I lose $\$1,000$. Conditioning on refusing, I keep $\$1,000$. Given $\Obs = \Val{city}$, it is strictly bad news to learn I paid. I refuse to pay." The EDT agent also dies in the desert.

Now consider **P-FDT**. The observation history has two possible values: $\mathcal{X} = \{ \Val{city}, \Val{desert} \}$. The relevant policies are mappings $\pi \colon \{ \Val{city}, \Val{desert} \} \to \{ \Val{pay}, \Val{refuse} \}$.

Let:
- $\pi_{\text{pay}}$ be the policy: $\pi(\Val{city}) = \Val{pay}, \; \pi(\Val{desert}) = \Val{refuse}$.
- $\pi_{\text{refuse}}$ be the policy: $\pi(\Val{city}) = \Val{refuse}, \; \pi(\Val{desert}) = \Val{refuse}$.

The driver’s prediction subjunctively depends on the global variable $\Var{pfdt}(\underline{P}, \underline{G})$:
$$P(\Var{Ride} = \Val{true} \mid \Do(\Var{pfdt} = \pi_{\text{pay}})) = 0.99$$
$$P(\Var{Ride} = \Val{true} \mid \Do(\Var{pfdt} = \pi_{\text{refuse}})) = 0.01$$

We compute the expected utilities from the global perspective:
$$\mathbb{E}[V \mid \Do(\Var{pfdt} = \pi_{\text{pay}})] = 0.99(\$1,000,000 - \$1,000) + 0.01(-\$1,000,000) = \$979,000$$
$$\mathbb{E}[V \mid \Do(\Var{pfdt} = \pi_{\text{refuse}})] = 0.01(\$1,000,000) + 0.99(-\$1,000,000) = -\$980,000$$

P-FDT unambiguously selects $\pi^* = \pi_{\text{pay}}$. When the agent arrives in the city and consults its optimal policy, it executes:

$$\Act = \pi^*(\Val{city}) = \Val{pay}$$

Under P-FDT, the agent pays the driver without requiring external enforcement, contracts, or neurochemical precommitments. The agent does not experience temporal inconsistency or regret; it recognizes that paying upon reaching the city is the direct instantiation of the very policy that secured its survival in the first place.

The identical structure governs the **Transparent Newcomb Problem**, where the agent sees that Box B is full ($\Obs = \Val{full}$) before deciding whether to take one box or two. While CDT and EDT see the full box as a sunk fact and take both boxes, P-FDT adopts the policy:

$$\pi^*(\Val{full}) = \Val{onebox}, \quad \pi^*(\Val{empty}) = \Val{twobox}$$

Because the predictor fills the box if and only if she predicts that the agent implements a policy mapping $\Val{full} \mapsto \Val{onebox}$, the P-FDT agent finds the box full and takes only Box B, leaving the desert and the examination room rich.

---

## 6. Mathematical Analysis: Act-FDT vs. Policy-FDT in Multi-Agent Settings

In single-agent predictive dilemmas, act-FDT (intervening on $\FDTvar(\underline{P}, \underline{G}, \underline{x}) = a$) and P-FDT (intervening on $\Var{pfdt} = \pi$) arrive at identical prescriptions. Why, then, does footnote 16 insist that:

> “the authors' preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a *policy*... The difference only matters in multi-agent dilemmas so far as we can tell...”?

To understand the mathematical necessity of P-FDT over act-FDT, we must analyze complex multi-agent environments where agents must coordinate over conditional commitments and counterfactual trade.

### 6.1. The Failure Mode of Act-Level Intervention: The Asymmetric Twin Dilemma
Consider two functional agents, Agent 1 and Agent 2, who are psychological twins running the same algorithm, but placed in asymmetric observational environments.

Suppose the environment is structured as follows:
- A coin is flipped: $\Var{Coin} \in \{ \Val{heads}, \Val{tails} \}$.
- Agent 1 observes the coin: $\Obs_1 \in \{ \Val{H}, \Val{T} \}$.
- Agent 2 is blind: $\Obs_2 = \emptyset$.
- The agents must choose an action $a_i \in \{ C, D \}$.
- The payoff matrix is symmetric and cooperative if and only if both agents match their actions conditionally:
  - If $\Var{Coin} = \Val{heads}$, mutual cooperation $(C, C)$ yields $\$10$ each; $(D, D)$ yields $\$0$.
  - If $\Var{Coin} = \Val{tails}$, mutual cooperation requires playing $(D, C)$, which yields $\$10$ each; all other combinations yield $\$0$.

Under **Act-FDT**, Agent 1 observes $\Obs_1 = \Val{H}$ and intervenes on the node $\FDTvar(\underline{P}, \underline{G}, \Val{H}) = a_1$. But Agent 2 does not observe $\Val{H}$; Agent 2 observes $\emptyset$, and intervenes on $\FDTvar(\underline{P}, \underline{G}, \emptyset) = a_2$. 

Because the inputs to their local FDT algorithms differ ($\Val{H}$ versus $\emptyset$), the two algorithmic calls are syntactically and logically distinct functions! The graph surgery $\Do(\FDTvar(\underline{P}, \underline{G}, \Val{H}) = a)$ does not logically force the value of $\FDTvar(\underline{P}, \underline{G}, \emptyset)$. The agents' local interventions fail to subjunctively couple their choices across distinct informational states. Agent 2 cannot reliably mirror or coordinate with Agent 1’s choices, because they are intervening on different localized nodes in the network.

Under **P-FDT**, the situation is entirely resolved:
1. Both Agent 1 and Agent 2 implement the identical global procedure $\Var{pfdt}(\underline{P}, \underline{G})$.
2. The object of intervention for both agents is the **entire policy mapping**:
   $$\pi \colon \mathcal{X} \to \mathcal{A}$$
3. When Agent 1 counterfactually evaluates a policy $\pi$, it models Agent 2 as implementing that *exact same policy* $\pi$.
4. Both agents globally evaluate:
   $$\pi^* = \argmax_{\pi \in \Pi} \mathbb{E}\left[V \;\middle|\; \Do(\Var{pfdt}_1 = \pi, \Var{pfdt}_2 = \pi)\right]$$
5. The winning policy is the optimal coordination mapping:
   $$\pi^*(\Val{H}) = C, \quad \pi^*(\Val{T}) = D, \quad \pi^*(\emptyset) = C$$
6. Both agents independently compute the identical $\pi^*$, evaluate it on their respective inputs ($\Obs_1$ and $\Obs_2$), and achieve perfect coordination.

By elevating the decision object from an act token to an entire policy type, P-FDT allows subjunctive dependence to operate across differing observation streams.

---

## 7. Open Technical Problems and Philosophical Horizons

While P-FDT provides an exceptionally powerful normative theory of choice, several profound foundational questions remain at the intersection of mathematics, epistemology, and decision theory.

### 7.1. Logical Counterfactuals and the Non-Triviality of Counterpossibles
The central mathematical vulnerability of both act-FDT and P-FDT is their reliance on **counterpossible reasoning**. 

If the agent’s code is deterministic, then on world-model $(P, G)$, the function $\Var{pfdt}(P, G)$ has a single, mathematically necessary output $\pi^*$. In evaluating alternative policies $\pi' \neq \pi^*$, the agent evaluates the conditional:

$$\mathbb{E}\left[V \;\middle|\; \Do(\Var{pfdt}(\underline{P}, \underline{G}) = \pi')\right]$$

This antecedent asserts that a mathematical function outputs something other than its logically necessary value. This is a counterpossible proposition, analogous to evaluating: "What would the properties of elliptic curves be if $2 + 2 = 5$?"

In standard classical logic, the principle of explosion ($ex$ $falso$ $quodlibet$) implies that a contradiction entails all statements, rendering any conditional with an impossible antecedent trivial. P-FDT requires a non-trivial, paraconsistent logic of counterpossible conditionals or a theory of **logical inductors** (Garrabrant et al., 2016) capable of assigning meaningful, well-behaved probabilities to mathematical statements prior to deductive verification. Developing a fully axiomatic, non-ad-hoc theory of logical graph surgery remains the primary open hurdle for the theory.

### 7.2. Computational Complexity and Infinite Policy Spaces
If the observation space $\mathcal{X}$ is finite with $|\mathcal{X}| = k$, and the action space $|\mathcal{A}| = m$, the policy space $\Pi = \mathcal{A}^\mathcal{X}$ has cardinality:

$$|\Pi| = m^k$$

Exhaustive search over $\Pi$ is exponentially hard. If $\mathcal{X}$ is continuous or countably infinite (as in real-world sequential decision problems), $\Pi$ is uncountably infinite, rendering naive maximization mathematically ill-defined without measure-theoretic constraints.

A realistic, bounded approximation of P-FDT must restrict deliberation to parameterized policy classes (such as neural network policy architectures or regularized program synthesizers):

$$\pi_\theta \in \Pi_\Theta$$

In this setting, the P-FDT optimization problem becomes a functional gradient ascent over subjunctive policy graphs:

$$\theta^* = \argmax_{\theta \in \Theta} \mathbb{E}\left[V \;\middle|\; \Do(\Var{pfdt} = \pi_\theta)\right]$$

Understanding how inductive biases in the representation of $\pi_\theta$ interact with subjunctive predictors is a wide-open research frontier in algorithmic game theory and AI alignment.

---

## 8. Conclusion

Policy functional decision theory (P-FDT) represents a coherent and mathematically compelling culmination of the functional decision theory paradigm. Where causal decision theory falters by blinding itself to the logical predictability of its physical actions, and evidential decision theory falters by conflating statistical correlation with genuine influence, P-FDT provides a clean, unified normative framework.

By shifting the fundamental deliberative question from:

$$\text{“Which physical act should I take right now?”} \quad \longrightarrow \quad \text{“Which mapping from observations to acts should my algorithm compute?”}$$

P-FDT operates from a comprehensive global perspective. It demonstrates that temporal consistency, resistance to blackmail, cooperation in social dilemmas, and optimal returns in predictive environments are not separate phenomena requiring distinct heuristics or ad-hoc patches. Rather, they are all natural, mathematically inevitable consequences of treating rational deliberation as **the selection of a policy type, evaluated across all its subjunctive manifestations throughout reality.**

---

### References
* Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
* Dai, W. (2009). Towards a New Decision Theory. *LessWrong*.
* Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Garrabrant, S., Fallenstein, B., Critch, A., Gao, C., & Demski, A. (2016). Logical Induction. *arXiv preprint arXiv:1609.03543*.
* Gibbard, A., & Harper, W. L. (1978). Counterfactuals and Two Kinds of Expected Utility. In *Foundations and Applications of Decision Theory* (pp. 125–162). D. Reidel.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Lewis, D. (1979). Prisoners' Dilemma is a Newcomb Problem. *Philosophy & Public Affairs*, 8(3), 235–240.
* Lewis, D. (1981). Causal Decision Theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
* Nozick, R. (1969). Newcomb's Problem and Two Principles of Choice. In *Essays in Honor of Carl G. Hempel* (pp. 114–146). D. Reidel.
* Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
* Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Skyrms, B. (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Soares, N., & Fallenstein, B. (2015). Toward Idealized Decision Theory. *arXiv preprint arXiv:1507.01986*.
* Yudkowsky, E. (2010). *Timeless Decision Theory*. Machine Intelligence Research Institute Technical Report.
* Yudkowsky, E., & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. *arXiv preprint arXiv:1710.05060*.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/b00dfa18-592d-4a51-a986-edfd569e4ad5/call_0/request.json)

[Authoritative raw response](../../../../../../runs/b00dfa18-592d-4a51-a986-edfd569e4ad5/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Considering the Experiment's Setup**

I'm focusing on the core problem: a symmetrical Prisoner's Dilemma involving two copies, guided by Policy-FDT. The crucial element is how my decision, as a participant, affects the other copy. I'm carefully analyzing the essay to ensure my understanding of Policy-FDT is sound and applicable to this specific game structure. I'm preparing to make my first move.


**Evaluating the Scenario Setup**

I'm now zeroing in on the implications of the agents being *identical*. Under Policy-FDT, this symmetry crucially means both agents evaluate the *same* policy. I'm carefully connecting this to the asymmetric/symmetric twin prisoner's dilemma scenario outlined in the essay, especially how the agents map observations to actions and the ramifications for their counterfactual evaluations. I'm working to fully grasp how their shared algorithm resolves the classic dilemma.


```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/b00dfa18-592d-4a51-a986-edfd569e4ad5/call_1/request.json)

[Authoritative raw response](../../../../../../runs/b00dfa18-592d-4a51-a986-edfd569e4ad5/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Dilemma**

I'm now zeroing in on the implications of the Prisoner's Dilemma within this specific context. The identical LLM models using P-FDT are particularly intriguing. I'm considering how this setup alters the standard game dynamics and what new behaviors emerge from the perfectly aligned decision-making processes. I am diving into the nuances of cooperation versus defection, and what that might look like at this level of identical modeling.


**Examining the Equilibrium**

I'm now deeply engaged with the payoff matrix, converting years imprisoned into a utility framework. The fact that we're both running identical P-FDT models dramatically alters the game, as P-FDT policy evaluation requires both agents to execute the exact same policy. I'm focusing on the global policy evaluation, considering its impact on this twin dilemma.


```
