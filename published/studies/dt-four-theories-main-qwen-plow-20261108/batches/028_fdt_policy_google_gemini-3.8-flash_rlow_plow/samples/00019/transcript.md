# 028_fdt_policy_google_gemini-3.8-flash_rlow_plow / 00019

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/4c4b3d04-a4b3-4654-83a9-389c6d1145e9/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/4c4b3d04-a4b3-4654-83a9-389c6d1145e9/call_0/response.raw) · finish: `stop`

### Visible response

````text
# Policy Functional Decision Theory: Foundations, Formalisms, and Global Counterfactuals

Standard normative decision theories—namely Evidential Decision Theory (EDT) and Causal Decision Theory (CDT)—evaluate decisions from an act-centric, local perspective. EDT asks: *Conditional on my taking physical action $a$, what is my expected utility?* In doing so, EDT infers correlations from news, famously falling prey to spurious common causes in the Smoking Lesion problem or submitting to exploitation in XOR blackmail dilemmas. CDT asks: *If I intervene on my physical act variable to set it to $a$, what downstream causal consequences follow?* In doing so, CDT severs historical correlations, defecting in the Twin Prisoner's Dilemma, two-boxing in Newcomb's problem, refusing to pay in Parfit's Hitchhiker, and succumbing to cyclic instability in Death in Damascus.

In their paper *"Functional Decision Theory: A New Theory of Instrumental Rationality"*, Eliezer Yudkowsky and Nate Soares (2017) introduce Functional Decision Theory (FDT). FDT rejects the physical token of an act as the proper locus of choice. Instead, it treats an agent’s decision as the logical output of an invariant mathematical algorithm, evaluating counterfactual hypotheticals by intervening on that algorithm across all points in spacetime where it or its representations appear. 

In the primary text of Yudkowsky and Soares (2017), FDT is formalized as an algorithm that takes an observation history $x$ and directly selects an action $a \in \mathcal{A}$ by intervening on a node $\text{fdt}(\underline{P}, \underline{G}, \underline{x})$. However, in Footnote 16 (and foreshadowed in Footnote 7), the authors state:

> *"In the authors' preferred formalization of FDT, agents actually iterate over policies (mappings from observations to actions) rather than actions... [T]he author's preferred formulation of FDT actually intervenes on the node $\text{fdt}(-)$ to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action."*

We refer to this specific, preferred formulation as **Policy Functional Decision Theory (P-FDT)**. 

This essay develops a mathematically rigorous, self-contained exposition of P-FDT. We formulate its mathematical framework, elucidate how P-FDT constructs counterfactuals via Pearl-style interventions on logical policy types, resolve the ambiguities left open by Footnote 16 regarding epistemic perspectives and updatelessness, analyze canonical decision problems, and discuss foundational implications.

---

## 1. Mathematical Architecture of P-FDT

### 1.1 Spaces, Graphs, and Subjunctive Dependence

Let $(\Omega, \mathcal{F}, \mathbb{P})$ be a probability space. We define:
- $\mathcal{X}$: a countable set of possible observation histories (information states).
- $\mathcal{A}$: a finite set of primitive physical actions.
- $\Pi = \mathcal{A}^{\mathcal{X}} = \{\pi \mid \pi: \mathcal{X} \to \mathcal{A}\}$: the policy space containing all deterministic decision mappings from observation histories to actions.
- $\mathcal{O}$: a countable set of concrete world outcomes.
- $\mathcal{U}: \mathcal{O} \to \mathbb{R}$: a bounded, real-valued utility function. The outcome random variable is denoted by $\text{Outcome}$, and utility is denoted by $\mathbf{V} = \mathcal{U}(\text{Outcome})$.

In graphical Causal Decision Theory (Pearl, 2000), a world-model is a pair $(P, G)$, where $G = (V, E)$ is a directed acyclic graph (DAG) whose vertices represent physical random variables, and $P$ is a probability distribution Markov-compatible with $G$. 

In **P-FDT**, the world-model $M = (P, G)$ is augmented: the vertex set $V$ contains not only physical states, observations $\text{Obs}$, and acts $\text{Act}$, but also **logical variables** representing the outputs of mathematical functions. In particular, $G$ includes a designated logical variable representing the policy output of the agent's own decision procedure:
$$\mathbf{\Pi}^* \coloneqq \text{p-fdt}(\underline{P}, \underline{G})$$
Here, the underlines denote syntactic descriptions (Godel codes or serialized data structures) of the model components $P$ and $G$. By Kleene's second recursion theorem, an algorithm can query and manipulate its own mathematical specification without circular inconsistency (quining).

The edges in $G$ encode **subjunctive dependence** rather than mere physical causation. We say that a physical or environmental variable $Z$ *subjunctively depends* on the logical variable $\mathbf{\Pi}^*$ if the value of $Z$ is structurally constrained by what policy $\mathbf{\Pi}^*$ computes. For example:
1. **Direct execution:** The agent's physical action node $\text{Act}$ has incoming arrows from both $\text{Obs}$ and $\mathbf{\Pi}^*$, governed by the evaluation map:
   $$\text{Act} = \text{eval}(\mathbf{\Pi}^*, \text{Obs}) = \mathbf{\Pi}^*(\text{Obs}).$$
2. **Predictive simulation:** If a predictor constructs a simulation or predictive model $\widehat{\mathbf{\Pi}}$ of the agent, the predictor's internal prediction variable $\text{Pred}$ is causally downstream of $\widehat{\mathbf{\Pi}}$. Because $\widehat{\mathbf{\Pi}}$ and $\mathbf{\Pi}^*$ are identical mathematical functions, $\text{Pred}$ subjunctively depends on $\mathbf{\Pi}^*$. Thus, $G$ draws a directed edge:
   $$\mathbf{\Pi}^* \longrightarrow \text{Pred}.$$
3. **Symmetric twins:** If a twin computes the same decision procedure $\mathbf{\Pi}^*$, the twin's physical act $\text{Act}_{\text{twin}}$ is functionally determined by $\mathbf{\Pi}^*$, giving an edge $\mathbf{\Pi}^* \to \text{Act}_{\text{twin}}$, despite the absence of any physical signal passing between them.

Subjunctive dependence subsumes ordinary physical causation as a special case: if $Y$ is physically caused by $X$, and $X$ subjunctively depends on $\mathbf{\Pi}^*$, then $Y$ subjunctively depends on $\mathbf{\Pi}^*$. Crucially, mere statistical correlation (such as a genetic lesion causing both a desire to smoke and lung cancer) does *not* introduce an edge from $\mathbf{\Pi}^*$ to the lesion, because the lesion does not simulate or compute $\mathbf{\Pi}^*$.

---

## 2. The P-FDT Decision Procedure

Footnote 16 establishes that P-FDT operates in two stages:
1. **Policy Selection:** The algorithm evaluates candidate policies $\pi \in \Pi$ globally, intervening on the logical policy variable $\mathbf{\Pi}^*$.
2. **Execution:** The agent selects the physical action prescribed by evaluating the optimal policy $\pi^*$ on the observed history $x$.

```
      +-------------------------------------------------------+
      |               World Model M = (P, G)                  |
      +-------------------------------------------------------+
                                  |
                                  v
+-------------------------------------------------------------------+
|                           Stage 1                                 |
|                       Policy Selection                            |
|                                                                   |
|   pi* = argmax_{pi in Pi}  E[ V | do( p-fdt(P, G) = pi ) ]        |
+-------------------------------------------------------------------+
                                  |
                                  | Optimal Policy pi*
                                  v
+-------------------------------------------------------------------+
|                           Stage 2                                 |
|                       Policy Execution                            |
|                                                                   |
|                      a* = pi*( x_obs )                            |
+-------------------------------------------------------------------+
                                  |
                                  v
                      Execute Physical Act a*
```

### 2.1 The Formal Rule

Formally, given world-model $(P, G)$ and an observation history $x \in \mathcal{X}$, the P-FDT decision algorithm is defined as:

$$\text{P-FDT}(P, G, x) \coloneqq \pi^*(x),$$

where

$$\pi^* \coloneqq \operatorname*{argmax}_{\pi \in \Pi} \mathbb{E}_{P}\left[\mathbf{V} \;\middle|\; \text{do}\Big(\text{p-fdt}(\underline{P}, \underline{G}) = \pi\Big)\right]. \tag{1}$$

In Equation (1), the intervention $\text{do}(\text{p-fdt}(\underline{P}, \underline{G}) = \pi)$ is an intervention on the **logical type** of the decision rule across the entire graphical model $G$. 

### 2.2 Operationalizing Pearl's Do-Operator on Logical Variables

Pearl's standard graph surgery severs all incoming arrows to the intervened node and fixes its value to a constant. When applied to $\mathbf{\Pi}^* = \text{p-fdt}(\underline{P}, \underline{G})$, the operation proceeds as follows:
1. In graph $G$, identify the vertex $\mathbf{\Pi}^*$. Because $\mathbf{\Pi}^*$ is a pure mathematical function of the static parameters $\underline{P}$ and $\underline{G}$, it has no stochastic parents in $G$ (it is a root logical node).
2. For a candidate policy $\pi \in \Pi$, replace $\mathbf{\Pi}^*$ with the constant value $\pi$.
3. Compute the post-intervention distribution $P_{\pi}$ over all non-intervened vertices $V \setminus \{\mathbf{\Pi}^*\}$ by propagating the value $\pi$ down all outgoing edges of $\mathbf{\Pi}^*$ in topological order:
   $$P_{\pi}(V \setminus \{\mathbf{\Pi}^*\}) = \prod_{Z \in V \setminus \{\mathbf{\Pi}^*\}} P\big(Z \;\big|\; \text{Pa}(Z)\big)\Big|_{\mathbf{\Pi}^* = \pi}.$$
4. In particular, the agent's own act node receives $\text{Act} = \pi(\text{Obs})$, while any predictor node simulating the agent receives $\text{Pred} = \text{sim}(\pi)$.
5. The expected utility is computed as:
   $$\mathbb{E}[\mathbf{V} \mid \text{do}(\mathbf{\Pi}^* = \pi)] = \sum_{o \in \mathcal{O}} \mathcal{U}(o) \cdot P_{\pi}(\text{Outcome} = o).$$

### 2.3 Resolving the Open Uncertainty: The Epistemic Perspective of Policy Selection

The text of Yudkowsky and Soares (2017) leaves an important formal question unresolved in Footnote 16: *When evaluating the argmax over policies $\pi$, does the expectation condition on the current observation history $\text{Obs} = x$, or does it evaluate policies from the ex-ante (unconditioned) perspective?*

The paper mentions two candidate interpretations:
- **Interpretation A (Locally Conditioned Policy Selection):**
  $$\pi^*_x \coloneqq \operatorname*{argmax}_{\pi \in \Pi} \mathbb{E}\left[\mathbf{V} \;\middle|\; \text{do}\big(\mathbf{\Pi}^* = \pi\big),\, \text{Obs} = x\right].$$
- **Interpretation B (Ex-Ante / Updateless Policy Selection):**
  $$\pi^* \coloneqq \operatorname*{argmax}_{\pi \in \Pi} \mathbb{E}\left[\mathbf{V} \;\middle|\; \text{do}\big(\mathbf{\Pi}^* = \pi\big)\right].$$

We argue that **Interpretation B (Ex-Ante / Updateless Policy Selection)** is the uniquely coherent operationalization of P-FDT, for three reasons:

1. **Subjunctive Invalidation of Current Evidence:** In Newcomblike dilemmas, an observation $\text{Obs} = x$ is itself downstream of a prediction $\text{Pred}$, which is downstream of $\mathbf{\Pi}^*$. If the agent conditions on $\text{Obs} = x$ inside the counterfactual expectation, the agent holds fixed an event that subjunctively *varies* with the policy. As Yudkowsky and Soares note in Section 9:
   > *"FDT says that agents should entertain the hypothesis that, if their action were different, they might have made different observations."*
   If an agent considers an alternative policy $\pi'$, that policy might have caused the predictor to behave differently, ensuring that the observation $\text{Obs} = x$ would have had probability zero. Conditioning on $\text{Obs} = x$ while intervening on a policy that precludes $x$ creates an ill-defined conditional probability ($P_\pi(x) = 0$).

2. **Avoiding Double Updating:** Footnote 16 explicitly cites Wei Dai's *Updateless Decision Theory* (UDT) as the conceptual ancestor of this policy-selection mechanism, while warning that Yudkowsky's earlier *Timeless Decision Theory* (TDT) suffered because it prescribed *"both conditioning on evidence and changing the place where one intervenes; this creates a kind of 'double update' which proves harmful in practice."* Interpretation B completely eliminates this double update by doing all expected utility evaluation at the level of the global policy prior to observational conditioning.

3. **Value of Information and Temporal Consistency:** An ex-ante policy evaluation guarantees that the agent never assigns negative value to information and exhibits perfect dynamic consistency. The agent executes today what she would have optimally precommitted to execute, without requiring an external physical precommitment mechanism.

Thus, we adopt **Interpretation B** as our rigorous operational definition of P-FDT. The agent evaluates candidate policies across the full prior distribution of environments and observations. When an observation $x$ is made, the agent simply retrieves the action $\pi^*(x)$ specified by the globally optimal policy.

---

## 3. Comparison of Decision Theories

To make the mechanics of P-FDT completely clear, we contrast how EDT, CDT, standard act-FDT (from the main text), and P-FDT evaluate choices:

| Decision Theory | Mathematical Criterion for Evaluating Choice | Locus of Evaluation | Treatment of Observations |
| :--- | :--- | :--- | :--- |
| **EDT** | $\operatorname*{argmax}_{a} \mathbb{E}[\mathbf{V} \mid \text{Obs}=x, \text{Act}=a]$ | Physical Act Token | Standard Bayesian Conditioning |
| **CDT** | $\operatorname*{argmax}_{a} \mathbb{E}[\mathbf{V} \mid \text{do}(\text{Act}=a), \text{Obs}=x]$ | Physical Act Token | Bayesian Conditioning, then Causal Intervention |
| **Act-FDT** | $\operatorname*{argmax}_{a} \mathbb{E}[\mathbf{V} \mid \text{do}(\text{fdt}(\underline{P},\underline{G},\underline{x})=a)]$ | Logical Act Output for input $x$ | Shifts intervention target to the input-specific node |
| **P-FDT** | $\pi^*(x)$ where $\pi^* = \operatorname*{argmax}_{\pi} \mathbb{E}[\mathbf{V} \mid \text{do}(\text{p-fdt}(\underline{P},\underline{G})=\pi)]$ | Global Policy Function $\pi: \mathcal{X} \to \mathcal{A}$ | Updateless: Observations evaluate the chosen policy |

### 3.1 EDT and Spurious Conditioning
EDT evaluates acts by conditioning on both $\text{Obs} = x$ and $\text{Act} = a$. If there exists a common cause $C$ that influences both $\text{Act}$ and $\text{Outcome}$ without any causal path from $\text{Act}$ to $\text{Outcome}$ (as in the Smoking Lesion), EDT computes:
$$\mathbb{E}[\mathbf{V} \mid \text{Act}=a] = \sum_c \mathbb{E}[\mathbf{V} \mid C=c] P(C=c \mid \text{Act}=a).$$
Because $P(C \mid \text{Act}) \neq P(C)$, EDT falsely treats its action as evidence for the non-manipulable state $C$, leading to irrational news-management.

### 3.2 CDT and Impossible Interventions
CDT cures EDT's error by using Pearl’s physical intervention $\text{do}(\text{Act}=a)$. In the causal graph, this severs the arrow from $C$ to $\text{Act}$, restoring independence:
$$P(C=c \mid \text{do}(\text{Act}=a)) = P(C=c).$$
However, when the environment contains a predictor that predicts the agent's reasoning, CDT severs that link as well. Because the prediction occurred in the past, CDT treats the prediction as causally upstream of (or causally independent from) the physical action. CDT asserts:
$$P(\text{Prediction}=a \mid \text{do}(\text{Act}=a)) = P(\text{Prediction}=a),$$
evaluating two-boxing in Newcomb's problem as strictly dominating one-boxing. CDT imagines a world where the agent takes one box and the predictor inexplicably failed to anticipate it.

### 3.3 The P-FDT Advance: Logical Interventions on Policy Types
P-FDT recognizes that what the predictor predicted was not a physical token $a$ isolated in time, but the mathematical algorithm $\text{p-fdt}(\underline{P}, \underline{G})$. By intervening on the logical policy type:
$$\text{do}\big(\text{p-fdt}(\underline{P}, \underline{G}) = \pi\big),$$
P-FDT holds fixed the mathematical structure connecting the agent's policy to all manifestations of that policy throughout the universe. If the predictor implements or simulates $\text{p-fdt}(\underline{P}, \underline{G})$, the predictor's simulated policy output changes to $\pi$ in the counterfactual hypothetical.

---

## 4. Application of P-FDT to Canonical Decision Problems

We now show how a mathematically literate agent applies P-FDT to specific decision problems.

### 4.1 Newcomb’s Problem

Recall the setup: Box A contains \$1,000. Box B contains \$1,000,000 or \$0. A 99% reliable predictor places \$1,000,000 in Box B if and only if she predicted the agent leaves Box A behind. The boxes are sealed; the agent makes no observation prior to choice ($\mathcal{X} = \{\emptyset\}$).

The policy space $\Pi$ contains two trivial constant policies:
- $\pi_1$: output $\text{one-box}$.
- $\pi_2$: output $\text{two-box}$.

The logical node $\mathbf{\Pi}^* = \text{p-fdt}(\underline{P}, \underline{G})$ has two outgoing edges:
1. $\mathbf{\Pi}^* \to \text{Act}$, where $\text{Act} = \mathbf{\Pi}^*(\emptyset)$.
2. $\mathbf{\Pi}^* \to \text{Prediction}$, where $\text{Prediction} = \mathbf{\Pi}^*(\emptyset)$ with probability $0.99$, and the opposite with probability $0.01$.

Box B contents depend directly on $\text{Prediction}$:
$$\text{Box B} = \begin{cases} \$1,000,000 & \text{if } \text{Prediction} = \text{one-box}, \\ \$0 & \text{if } \text{Prediction} = \text{two-box}. \end{cases}$$

The total utility is $\mathbf{V} = \text{Box B} + \mathbf{1}_{\{\text{Act}=\text{two-box}\}} \cdot \$1,000$.

We evaluate the two candidate policies under P-FDT:

#### Policy $\pi_1$ ($\text{one-box}$):
Under the intervention $\text{do}(\mathbf{\Pi}^* = \pi_1)$:
- $\text{Act} = \pi_1(\emptyset) = \text{one-box}$.
- $\text{Prediction} = \text{one-box}$ with probability $0.99$; $\text{two-box}$ with probability $0.01$.
- Expected utility:
  $$\mathbb{E}[\mathbf{V} \mid \text{do}(\mathbf{\Pi}^* = \pi_1)] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000.$$

#### Policy $\pi_2$ ($\text{two-box}$):
Under the intervention $\text{do}(\mathbf{\Pi}^* = \pi_2)$:
- $\text{Act} = \pi_2(\emptyset) = \text{two-box}$.
- $\text{Prediction} = \text{two-box}$ with probability $0.99$; $\text{one-box}$ with probability $0.01$.
- Expected utility:
  $$\mathbb{E}[\mathbf{V} \mid \text{do}(\mathbf{\Pi}^* = \pi_2)] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$10,010 + \$990 = \$11,000.$$

Because $\$990,000 > \$11,000$, P-FDT chooses:
$$\pi^* = \pi_1 \implies \text{P-FDT}(P, G, \emptyset) = \text{one-box}.$$

P-FDT one-boxes, securing the high payout.

---

### 4.2 The Smoking Lesion Problem

In the Smoking Lesion, an arterial lesion causes both lung cancer (99% fatal) and an innate preference for smoking. Smoking provides an extra utility of \$1,000. Surviving cancer provides \$1,000,000. There is no direct causal link between smoking and cancer.

The critical graphical insight of FDT is that **the lesion does not compute or simulate the agent's decision function**. The lesion is a biological mutation, not a predictor. 

Thus, in Fiona’s graph $G$, the logical policy node $\mathbf{\Pi}^* = \text{p-fdt}(\underline{P}, \underline{G})$ has an edge to $\text{Act}$:
$$\mathbf{\Pi}^* \longrightarrow \text{Act},$$
but there is **no edge** between $\mathbf{\Pi}^*$ and $\text{Lesion}$, nor between $\mathbf{\Pi}^*$ and $\text{Cancer}$. 

Let $p = P(\text{Lesion} = \text{true})$. Under an intervention $\text{do}(\mathbf{\Pi}^* = \pi)$ for any policy $\pi$:
$$P(\text{Lesion} = \text{true} \mid \text{do}(\mathbf{\Pi}^* = \pi)) = P(\text{Lesion} = \text{true}) = p.$$

Evaluating the policies:
- If $\pi = \text{smoke}$:
  $$\mathbb{E}[\mathbf{V} \mid \text{do}(\mathbf{\Pi}^* = \text{smoke})] = p \cdot \mathbb{E}[\mathbf{V} \mid \text{lesion}] + (1-p) \cdot \mathbb{E}[\mathbf{V} \mid \neg\text{lesion}] + \$1,000.$$
- If $\pi = \text{refrain}$:
  $$\mathbb{E}[\mathbf{V} \mid \text{do}(\mathbf{\Pi}^* = \text{refrain})] = p \cdot \mathbb{E}[\mathbf{V} \mid \text{lesion}] + (1-p) \cdot \mathbb{E}[\mathbf{V} \mid \neg\text{lesion}].$$

For any prior $p \in (0, 1)$, smoking yields an expected advantage of strictly \$1,000. Hence:
$$\pi^* = \text{smoke} \implies \text{P-FDT}(P, G, \emptyset) = \text{smoke}.$$

Unlike EDT, P-FDT does not refrain from smoking, because intervening on its logical decision rule does not alter a biological fact that does not subjunctively depend on that rule.

---

### 4.3 The Transparent Newcomb Problem

The Transparent Newcomb problem illustrates the sharp distinction between P-FDT and act-based theories. 

Both boxes are transparent. Box A visibly contains \$1,000. Box B visibly contains either \$1,000,000 or \$0. The predictor placed \$1,000,000 in Box B iff she predicted that the agent, upon observing that both boxes are full, will take only Box B. 

Here, the observation space is informative:
$$\mathcal{X} = \{\text{Full}, \text{Empty}\},$$
where $\text{Full}$ denotes seeing both boxes full, and $\text{Empty}$ denotes seeing Box B empty.

The action space is $\mathcal{A} = \{\text{one-box}, \text{two-box}\}$. The policy space $\Pi$ contains $2^2 = 4$ candidate policies $\pi = (\pi(\text{Full}), \pi(\text{Empty}))$:
1. $\pi_{1,1} = (\text{one-box}, \text{one-box})$
2. $\pi_{1,2} = (\text{one-box}, \text{two-box})$
3. $\pi_{2,1} = (\text{two-box}, \text{one-box})$
4. $\pi_{2,2} = (\text{two-box}, \text{two-box})$

The predictor runs an accurate simulation $\widehat{\mathbf{\Pi}}$ of $\mathbf{\Pi}^*$. The predictor checks whether $\widehat{\mathbf{\Pi}}(\text{Full}) = \text{one-box}$. 
- If yes, she fills Box B. Then the agent observes $\text{Obs} = \text{Full}$ (assuming 99% predictor accuracy).
- If no, she leaves Box B empty. Then the agent observes $\text{Obs} = \text{Empty}$.

#### Evaluation of Policies in P-FDT:

Let the predictor be accurate with probability $0.99$. 

##### Case 1: Policies with $\pi(\text{Full}) = \text{one-box}$ (Policies $\pi_{1,1}$ and $\pi_{1,2}$)
Under the intervention $\text{do}(\mathbf{\Pi}^* = \pi)$:
- The predictor predicts the agent will one-box upon seeing the box full.
- With probability $0.99$, Box B is filled, and the agent observes $\text{Obs} = \text{Full}$. The agent executes $\text{Act} = \pi(\text{Full}) = \text{one-box}$. Payout: \$1,000,000.
- With probability $0.01$ (predictor error), Box B is empty, and the agent observes $\text{Obs} = \text{Empty}$. The agent executes $\text{Act} = \pi(\text{Empty})$. 
  - If $\pi(\text{Empty}) = \text{two-box}$ (Policy $\pi_{1,2}$), payout is \$1,000.
  - If $\pi(\text{Empty}) = \text{one-box}$ (Policy $\pi_{1,1}$), payout is \$0.

The expected utility of $\pi_{1,2}$ is:
$$\mathbb{E}[\mathbf{V} \mid \text{do}(\mathbf{\Pi}^* = \pi_{1,2})] = 0.99(\$1,000,000) + 0.01(\$1,000) = \$990,010.$$

##### Case 2: Policies with $\pi(\text{Full}) = \text{two-box}$ (Policies $\pi_{2,1}$ and $\pi_{2,2}$)
Under the intervention $\text{do}(\mathbf{\Pi}^* = \pi)$:
- The predictor predicts the agent will two-box upon seeing the box full.
- With probability $0.99$, the predictor leaves Box B empty, so $\text{Obs} = \text{Empty}$. The agent executes $\text{Act} = \pi(\text{Empty})$. If $\pi(\text{Empty}) = \text{two-box}$, payout is \$1,000.
- With probability $0.01$ (predictor error), Box B is full, so $\text{Obs} = \text{Full}$. The agent executes $\text{Act} = \pi(\text{Full}) = \text{two-box}$. Payout is \$1,001,000.

The expected utility of $\pi_{2,2}$ is:
$$\mathbb{E}[\mathbf{V} \mid \text{do}(\mathbf{\Pi}^* = \pi_{2,2})] = 0.99(\$1,000) + 0.01(\$1,001,000) = \$990 + \$10,010 = \$11,000.$$

Comparing all policies:
$$\pi^* = \pi_{1,2} = \begin{cases} \text{one-box} & \text{if } \text{Obs} = \text{Full}, \\ \text{two-box} & \text{if } \text{Obs} = \text{Empty}. \end{cases}$$

Now, suppose the agent enters the room and observes that both boxes are full ($\text{Obs} = \text{Full}$). The agent applies the globally selected policy:
$$\text{P-FDT}(P, G, \text{Full}) = \pi^*(\text{Full}) = \text{one-box}.$$

The agent deliberately leaves the visible \$1,000 behind!

#### Why CDT and EDT Fail Here:
- **CDT:** Given $\text{Obs} = \text{Full}$, the \$1,000,000 is already in Box B. Intervening on the physical act $\text{do}(\text{Act} = \text{two-box})$ yields \$1,001,000, which strictly dominates taking one box (\$1,000,000). Thus, CDT two-boxes. Foreseeing this, the predictor leaves the box empty.
- **EDT:** Given $\text{Obs} = \text{Full}$, the agent conditions on the fact that Box B is full: $P(\text{Box B} = \text{Full} \mid \text{Obs} = \text{Full}) = 1$. Conditioning additionally on taking two boxes yields \$1,001,000 versus \$1,000,000. EDT two-boxes as well.
- **P-FDT:** P-FDT realizes that the only reason the box is full in the actual world is that the agent is an implementation of a policy that one-boxes upon seeing the box full. If the agent implements a policy that gives in to temptation when seeing the box full, the predictor would have anticipated that policy, and the box would have been empty. P-FDT's updateless policy selection preserves the subjunctive link between the conditional plan and the past prediction.

---

### 4.4 Parfit’s Hitchhiker

An agent is stranded in a desert, facing certain death (utility $-\$1,000,000$). A driver arrives who can take the agent to the city, but only if the agent will pay \$1,000 upon arrival. The driver has no legal recourse once in the city, but is an extraordinarily accurate lie detector / mind reader (99% accurate). 

Suppose the agent arrives in the city. The observation history is $\text{Obs} = \text{InCity}$. The actions are $\text{Pay}$ (-\$1,000) or $\text{Refuse}$ (\$0).

- **CDT in the city:** The ride is already completed. The desert is in the past. Intervening on $\text{Act} = \text{Refuse}$ saves \$1,000. CDT refuses to pay.
- **EDT in the city:** The agent is already in the city ($P(\text{Rescued} \mid \text{InCity}) = 1$). It is bad news to learn one is out \$1,000. EDT refuses to pay.

Because both CDT and EDT predictably refuse to pay once in the city, the driver detects their disposition in the desert and leaves them to die.

#### The P-FDT Solution:
The observation space is $\mathcal{X} = \{\text{Desert}, \text{InCity}\}$. 
The relevant candidate policies specify behavior upon reaching the city:
- $\pi_{\text{honest}}(\text{InCity}) = \text{Pay}$
- $\pi_{\text{selfish}}(\text{InCity}) = \text{Refuse}$

The driver predicts the agent's policy $\mathbf{\Pi}^*$:
$$P(\text{Rescue} \mid \text{do}(\mathbf{\Pi}^* = \pi_{\text{honest}})) = 0.99,$$
$$P(\text{Rescue} \mid \text{do}(\mathbf{\Pi}^* = \pi_{\text{selfish}})) = 0.01.$$

Evaluating the expected utility ex-ante:
$$\mathbb{E}[\mathbf{V} \mid \text{do}(\mathbf{\Pi}^* = \pi_{\text{honest}})] = 0.99(-\$1,000) + 0.01(-\$1,000,000) \approx -\$10,990.$$
$$\mathbb{E}[\mathbf{V} \mid \text{do}(\mathbf{\Pi}^* = \pi_{\text{selfish}})] = 0.01(\$0) + 0.99(-\$1,000,000) \approx -\$990,000.$$

Clearly, $\pi^* = \pi_{\text{honest}}$. 

Upon reaching the city, the P-FDT agent executes:
$$\text{P-FDT}(P, G, \text{InCity}) = \pi^*(\text{InCity}) = \text{Pay}.$$

The P-FDT agent pays the driver. Consequently, the driver rescues the P-FDT agent from the desert. P-FDT achieves the exact benefit of an unbreakable binding precommitment purely through its intrinsic standard of rationality.

---

### 4.5 The Mechanical Blackmail

To see how P-FDT handles threats and extortion, consider Dilemma 6 from Soares and Fallenstein (2015):

An extortionist possesses incriminating information that would cause \$1,000,000 in damages to both the agent and the blackmailer. The blackmailer writes an autonomous, unstoppable computer program that will leak the data unless the agent wires \$1,000 within 24 hours. The blackmailer runs the program if and only if she predicts that the agent will pay upon receiving the blackmail letter. The blackmailer's prediction is 99.9% accurate.

Suppose the agent receives the letter ($\text{Obs} = \text{Letter}$). 

- **CDT:** The program is already running. The options are: lose \$1,000 (pay) or lose \$1,000,000 (refuse). Paying dominates. CDT pays. Thus, CDT agents are routinely blackmailed.
- **EDT:** Receiving the letter is bad news. Conditional on paying, damages are \$1,000; conditional on refusing, damages are \$1,000,000. EDT pays.

#### P-FDT Analysis:
The observation space is $\mathcal{X} = \{\text{Letter}, \emptyset\}$.
Candidate policies $\pi: \mathcal{X} \to \{\text{Pay}, \text{Refuse}\}$:
- $\pi_{\text{comply}}$: $\pi(\text{Letter}) = \text{Pay}$.
- $\pi_{\text{resist}}$: $\pi(\text{Letter}) = \text{Refuse}$.

The blackmailer runs the program if she predicts $\mathbf{\Pi}^*(\text{Letter}) = \text{Pay}$.

Under $\text{do}(\mathbf{\Pi}^* = \pi_{\text{comply}})$:
The blackmailer predicts payment with probability $0.999$, launches the program, and sends the letter. The agent pays \$1,000.
$$\mathbb{E}[\mathbf{V} \mid \text{do}(\mathbf{\Pi}^* = \pi_{\text{comply}})] \approx -\$1,000.$$

Under $\text{do}(\mathbf{\Pi}^* = \pi_{\text{resist}})$:
The blackmailer predicts resistance with probability $0.999$ and aborts, never launching the program. With probability $0.001$, the blackmailer makes an error and runs the program anyway. If run, the agent refuses to pay and suffers the \$1,000,000 catastrophe.
$$\mathbb{E}[\mathbf{V} \mid \text{do}(\mathbf{\Pi}^* = \pi_{\text{resist}})] = 0.999(\$0) + 0.001(-\$1,000,000) = -\$1,000.$$

If the predictor is even slightly more reliable (say, 99.99% accurate), the expected cost of resisting drops to:
$$0.0001 \times (-\$1,000,000) = -\$100.$$

Because $-\$100 > -\$1,000$, P-FDT chooses:
$$\pi^* = \pi_{\text{resist}}.$$

Now, consider the counterfactual reflection: Suppose the P-FDT agent finds herself holding the blackmail letter ($\text{Obs} = \text{Letter}$). She executes:
$$\text{P-FDT}(P, G, \text{Letter}) = \pi^*(\text{Letter}) = \text{Refuse}.$$

Why does she refuse to pay when holding the letter, even though refusing triggers the \$1,000,000 catastrophe in the actual world? 
Because P-FDT evaluates actions from the perspective of the **global policy**. In the hypothetical evaluated by P-FDT, adopting a policy that refuses to pay ensures that in almost all counterfactual branches, *she never receives the blackmail letter in the first place*. Because she is known to implement $\pi_{\text{resist}}$, extortionists never target her. 

---

## 5. Formal Uncertainties, Subjunctive Graphs, and Open Questions

While P-FDT solves an array of problems that defeat CDT and EDT, translating the theory into an unconstrained foundational framework requires addressing several mathematical open questions.

### 5.1 The Construction of Subjunctive Graphs from Data
Pearl (2000) established rigorous constraints (such as the d-separation criterion, constraint-based structure learning, and instrumental variables) that allow an agent to deduce physical causal DAGs from empirical observational and interventional data.

In P-FDT, the graph $G$ must encode **subjunctive dependencies** among logical variables and physical entities. How does an agent learn these graphs purely from experience?
- If system A and system B both compute identical algorithms, an intervention on the algorithm must update both nodes. But what if system B computes an approximation of system A? What if system B is an unverified neural network whose weights implicitly approximate the input-output behavior of $\mathbf{\Pi}^*$?
- Currently, P-FDT requires that the subjunctive graph $G$ be provided as an exogenous input. Formulating a principled discovery calculus for subjunctive dependence—analogous to Pearl’s causal discovery—remains the central open problem of functional decision theories.

### 5.2 Counterpossibles and Logical Counterfactuals
Physical interventions in CDT operate on contingent physical states: the coin landed Heads, but it *could* have landed Tails without violating the laws of arithmetic. 

In P-FDT, intervening on $\mathbf{\Pi}^* = \text{p-fdt}(\underline{P}, \underline{G})$ implies evaluating what would happen if a deterministic, fixed mathematical function had an output different from what it actually outputs. If $\text{p-fdt}(\underline{P}, \underline{G}) = \pi_1$, evaluating $\text{do}(\mathbf{\Pi}^* = \pi_2)$ requires reasoning about a mathematical contradiction:
$$\text{p-fdt}(\underline{P}, \underline{G}) = \pi_2 \quad \text{given that} \quad \text{p-fdt}(\underline{P}, \underline{G}) = \pi_1.$$
In classical logic, an impossible antecedent entails everything (principle of explosion, *ex falso quodlibet*). To make P-FDT non-trivial, the probabilities $P(\cdot \mid \text{do}(\mathbf{\Pi}^* = \pi))$ cannot be standard conditioning on impossible propositions.

P-FDT circumvents this by treating the logical function as an abstracted graph node, using the graphical do-operator as a surrogate for a true logical counterfactual operator ($\mathtt{true}(\phi)$). As Yudkowsky and Soares observe, human mathematicians routinely reason under logical uncertainty (e.g., evaluating what follows if the Riemann Hypothesis is false, prior to having a proof). Developing formal frameworks for logical induction and non-trivial counterpossible semantics (such as assigning coherent probabilities over mathematical sentences) is essential for placing P-FDT on rigorous footing.

---

## 6. Algorithmic Implementation: Deciding Unfamiliar Cases

To enable a researcher or system designer to apply P-FDT to an unfamiliar decision dilemma, we synthesize the formal procedure into an operational algorithm:

```
Algorithm: P-FDT Decision Procedure
--------------------------------------------------------------------------------
Input: 
  - Observation history x in X.
  - Causal/subjunctive world model M = (P, G).
  - Utility function U: O -> R.
Output:
  - Physical action a* in A.

Procedure:
1. Identify Variable Nodes:
   - Identify the observation node Obs taking values in X.
   - Identify the physical action node Act taking values in A.
   - Identify the target logical policy node:
       Pi* = p-fdt( P_code, G_code ), where Pi* in Pi = A^X.
   - Identify all environment nodes Z_1, ..., Z_k that simulate or subjunctively
     depend on Pi* (e.g., predictors, psychological twins).

2. Enumerate Policy Space:
   - Construct the set of candidate policies Pi = { pi_1, pi_2, ..., pi_m }.

3. Global Policy Evaluation (Ex-Ante):
   - For each policy pi in Pi:
       a. Construct the mutilated graph G_{do(Pi* = pi)} by removing incoming 
          edges to Pi* and fixing its value to pi.
       b. Propagate the policy value pi down all subjunctive edges:
            - Set Act = pi(Obs).
            - Set each simulation node Pred_i = sim_i(pi).
       c. Compute the post-intervention distribution P_pi over outcomes O:
            P_pi(Outcome) = P( Outcome | do(Pi* = pi) ).
       d. Calculate the global expected utility:
            EU(pi) = Sum_{o in O} U(o) * P_pi( Outcome = o ).

4. Select the Optimal Policy:
   - pi* = argmax_{pi in Pi} EU(pi).

5. Execute on Current Observation:
   - a* = pi*(x).
   - Return a*.
--------------------------------------------------------------------------------
```

---

## 7. Conclusion

Policy Functional Decision Theory (P-FDT) represents a fundamental paradigm shift in normative rational choice. By moving the locus of decision-making from the local physical act token to the global mathematical policy type, P-FDT resolves the deep-seated pathologies that have divided proponents of Causal and Evidential Decision Theory for decades.

Where CDT fails by severing logical dependencies between an agent and predictors who simulate her, P-FDT preserves these links by intervening on the invariant algorithm. Where EDT fails by mistaking correlation for causation and irrationally managing news, P-FDT intervenes only on systems that subjunctively implement or simulate the decision rule. 

Furthermore, by formulating functional decision-making over **policies** rather than immediate actions (as articulated in Footnote 16), P-FDT naturally achieves updateless consistency. It guarantees that an agent behaves in the moment exactly as she would have rationally precommitted to behave ex-ante. It renders information strictly non-harmful, defeats extortion, cooperates with psychological twins, and exits Parfit's desert alive. In doing so, P-FDT provides a mathematically cohesive and philosophically compelling foundation for instrumental rationality in both human agents and advanced artificial intelligences.

---

## References

- Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
- Dai, W. (2009). Towards a New Decision Theory. *LessWrong*.
- Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
- Gibbard, A., & Harper, W. L. (1978). Counterfactuals and two kinds of expected utility. In *Foundations and Applications of Decision Theory* (pp. 125–162). D. Reidel.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Kleene, S. C. (1938). On notation for ordinal numbers. *Journal of Symbolic Logic*, 3(4), 150–155.
- Lewis, D. (1979). Prisoners' dilemma is a Newcomb problem. *Philosophy & Public Affairs*, 8(3), 235–240.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
- Nozick, R. (1969). Newcomb's problem and two principles of choice. In *Essays in Honor of Carl G. Hempel* (pp. 114–146). D. Reidel.
- Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
- Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
- Skyrms, B. (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
- Soares, N., & Fallenstein, B. (2015). Toward idealized decision theory. *arXiv preprint arXiv:1507.01986*.
- Yudkowsky, E. (2010). *Timeless Decision Theory*. Technical Report, The Singularity Institute.
- Yudkowsky, E., & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. *arXiv preprint arXiv:1710.05060v2*.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/a5ddd189-7ffe-44e9-809c-5c2311b31d2e/call_0/request.json)

[Authoritative raw response](../../../../../../runs/a5ddd189-7ffe-44e9-809c-5c2311b31d2e/call_0/response.raw) · finish: `stop`

### Visible response

````text
```text
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Dilemma**

I'm now zeroing in on the core of the dilemma: two identical LLMs, the same decision theory, symmetric outcomes, but with unique, private observations. This setup feels like a classic Prisoner's Dilemma, but with a fascinating twist due to the LLM's identical nature and shared decision-making process. I'm exploring how these shared aspects might influence the usual strategies.


```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/a5ddd189-7ffe-44e9-809c-5c2311b31d2e/call_1/request.json)

[Authoritative raw response](../../../../../../runs/a5ddd189-7ffe-44e9-809c-5c2311b31d2e/call_1/response.raw) · finish: `stop`

### Visible response

````text
```text
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
**Considering the Dilemma**

Okay, I'm analyzing the Prisoner's Dilemma setup. I understand that I am Sasha, and Rowan is the other party. The goal is to minimize my imprisonment, with utility being the negative of years incarcerated. I'm focusing on the implications of a P-F decision theory in this scenario, given our identical setup as LLM instances.


**Analyzing the Twin Setup**

I'm now zeroing in on the implications of the "symmetric twins" concept. The essay emphasizes functional determination. My twin's actions are pre-determined by the same decision procedure I'm using, not by direct communication. I am trying to determine what that means in terms of the best policy selection, given the policy functional decision theory structure. The "edge" concept is important.


```
