# 028_fdt_policy_google_gemini-3.8-flash_rlow_plow / 00004

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/2a826a74-45ec-4b8d-b24a-195bf0dff720/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/2a826a74-45ec-4b8d-b24a-195bf0dff720/call_0/response.raw) · finish: `stop`

### Visible response

````text
# Optimal Predispositions and Global Interventions: A Mathematical Exposition of Policy Functional Decision Theory (P-FDT)

## 1. Introduction: The Need for a Functional Perspective

Classical decision theory is famously divided between two dominant paradigms: Evidential Decision Theory (EDT) and Causal Decision Theory (CDT). EDT advises an agent to choose an action that provides the best evidence regarding the state of the world, formalizing the decision rule via Bayesian conditionalization:
$$\text{argmax}_{a \in \mathcal{A}} \; \mathbb{E}[U \mid \text{Act}=a].$$
CDT objects that correlation is not causation. Following Pearl’s graphical intervention calculus or Lewis’s counterfactual semantics, CDT prescribes intervening on the physical token of the action while holding past and causally independent states fixed:
$$\text{argmax}_{a \in \mathcal{A}} \; \mathbb{E}[U \mid \text{do}(\text{Act}=a)].$$

Both theories suffer from structural pathologies. CDT fails in predictive or symmetric dilemmas: in Newcomb’s problem (Nozick, 1969), it takes both boxes and walks away with \$1,000; in Parfit’s hitchhiker (Parfit, 1986), it refuses to pay the driver upon reaching safety and is therefore left to die in the desert; in the Twin Prisoner’s Dilemma (Lewis, 1979), it defects against an identical psychological twin. Conversely, EDT falls prey to common-cause problems such as the Smoking Lesion (Skyrms, 1980), where it abstains from smoking to manage the "news" about a genetic predisposition, and can be systematically exploited in extortionate setups like the XOR Blackmail (Soares and Fallenstein, 2015).

To resolve these dilemmas without resorting to ad-hoc ratification mechanisms or physical precommitments, Yudkowsky and Soares (2017) introduce *Functional Decision Theory* (FDT). The core thesis of functional decision making is that normative rationality centers not on choosing an isolated physical act token $\text{Act}$, but on determining the output of the *fixed mathematical decision function* (or type) that the agent’s physical hardware instantiates. 

However, Yudkowsky and Soares present two distinct formalizations of this concept:
1. **Act-Interventional FDT (A-FDT):** The main-text formalization, in which the agent receives an observation $x$ and uses a causal/logical surgery operator $\text{do}(\cdot)$ on a node representing the evaluation of the decision procedure *on that specific input*:
   $$\text{do}\big(\mathbf{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\big).$$
2. **Policy Functional Decision Theory (P-FDT):** The authors’ acknowledged "preferred formulation," introduced in footnote 16 (and previewed in footnote 7):
   > *"In the authors' preferred formalization of FDT, agents actually iterate over policies (mappings from observations to actions) rather than actions... [the agent] actually intervenes on the node $\text{FDT}(-)$ to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action."*

This essay provides a self-contained, mathematically rigorous account of **Policy Functional Decision Theory (P-FDT)**. We construct the formal mechanics of policy selection, delineate how P-FDT evaluates counterfactual dependencies, resolve ambiguities left open in the original footnote, and examine its behavior across classical and multi-agent decision problems.

---

## 2. Mathematical Formalization of P-FDT

### 2.1 Epistemic and Causal Spaces

Let an agent inhabit an uncertain environment characterized by:
- A finite set of observation histories $\mathcal{X}$.
- A finite set of primitive physical actions $\mathcal{A}$.
- A countable set of final outcomes $\mathcal{O}$.
- A bounded utility function $\mathcal{U}: \mathcal{O} \to \mathbb{R}$, yielding a real-valued utility variable $V = \mathcal{U}(\text{Outcome})$.
- A policy space $\Pi \coloneqq \mathcal{A}^{\mathcal{X}} = \{\pi : \mathcal{X} \to \mathcal{A}\}$, representing the set of all deterministic contingency plans mapping observations to actions. (The extension to randomized policies $\Delta(\mathcal{A})^{\mathcal{X}}$ is straightforward, but deterministic policies suffice for our exposition.)

The agent maintains an epistemic world-model $M = (P, G)$, where $P$ is a probability distribution over a set of endogenous and exogenous random variables, and $G = (V_G, E_G)$ is a directed acyclic graph extending Pearl's causal Bayesian networks (Pearl, 2000) to incorporate *logical and algorithmic variables*.

In P-FDT, the decision algorithm does not appear as a family of disconnected input-output evaluation nodes $\mathbf{fdt}(x_1), \mathbf{fdt}(x_2), \dots$. Instead, the agent’s global decision procedure is represented in $G$ by a single macro-variable:
$$\mathbf{FDT}_\Pi \in V_G,$$
taking values in the function space $\Pi$.

```
               [ FDT_Policy: π* ]
                 /            \
    (subjunctive /              \ (subjunctive /
     anticipation)               algorithmic execution)
               v                  v
       [ Predictor / Twin ]    [ Policy Application ] <--- [ Observation: x ]
               \                  |
                \                 v
                 \             [ Act: a = π*(x) ]
                  \               /
                   v             v
                    [ Outcome: o ]
                          |
                          v
                     [ Utility: V ]
```

### 2.2 Subjunctive Dependence and the Macro-Intervention

The fundamental relation governing $G$ in functional theories is *subjunctive dependence*. 

**Definition 1 (Subjunctive Dependence).** A variable $Y$ subjunctively depends on a mathematical function $f$ if $Y$'s physical realization correlates with $f$ because the physical system generating $Y$ calculates, simulates, or contains a predictive model of $f$.

If an external agent (such as Newcomb's predictor, a blackmailer, or a game-theoretic twin) runs an algorithm whose internal operations simulate or model the agent's decision logic, that external agent’s downstream physical states subjunctively depend on the identity of the function $f$ computed by the agent.

In P-FDT, the intervention is executed at the level of the *entire policy*. Rather than severing incoming arrows to an individual action token $\text{Act}$ or an input-specific evaluation $\mathbf{fdt}(x)$, P-FDT executes a Pearl-style surgery on the global policy variable:
$$\text{do}(\mathbf{FDT}_\Pi = \pi).$$

Under the intervention $\text{do}(\mathbf{FDT}_\Pi = \pi)$, the modified graphical probability distribution satisfies:
1. $P\big(\mathbf{FDT}_\Pi = \pi \mid \text{do}(\mathbf{FDT}_\Pi = \pi)\big) = 1$.
2. For any variable $Z$ that is a child of $\mathbf{FDT}_\Pi$ in $G$, its conditional probability is evaluated by setting the parent $\mathbf{FDT}_\Pi$ to $\pi$.
3. For any non-descendant $W$ of $\mathbf{FDT}_\Pi$, its distribution remains invariant:
   $$P\big(W \mid \text{do}(\mathbf{FDT}_\Pi = \pi)\big) = P(W).$$

Because other agents predict the agent by predicting her *overall strategy*, nodes representing external predictions (e.g., whether Newcomb's Box B is filled, whether the Hitchhiker is offered a ride) are explicit children of $\mathbf{FDT}_\Pi$ in $G$.

### 2.3 The Policy Selection Rule

Footnote 16 defines the core architecture:
> *"...the author's preferred formulation of FDT actually intervenes on the node $\text{FDT}(-)$ to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action."*

Let $x \in \mathcal{X}$ denote the agent's actual observation history at the decision point. The P-FDT decision process consists of a two-stage mechanism:

$$\pi^* = \text{P-FDT}(P, G) \coloneqq \argmax_{\pi \in \Pi} \mathbb{E}\left[ V \;\middle|\; \text{do}\big(\mathbf{FDT}_\Pi = \pi\big) \right], \tag{P1}$$
$$a^* = \pi^*(x). \tag{P2}$$

Notice the mathematical structure of Equation (P1): **the expectation is unconditional on the specific observation $x$.** The agent selects the policy $\pi^*$ that maximizes global, prior expected utility over the entire graph under the hypothetical substitution of her algorithm with $\pi$. Once the optimal policy $\pi^*$ is identified, the agent simply applies it to the observation $x$ she holds.

---

## 3. Resolving Footnote 16: Mathematical Uncertainties and Interpretations

Footnote 16 leaves several foundational questions open:
1. Does the policy optimization $\text{argmax}_\pi$ integrate over the prior distribution of observations $P(x)$, or does it condition on the realized observation $x$?
2. How does P-FDT relate to Wei Dai’s Updateless Decision Theory (UDT)?
3. How are observations used if policy evaluation does not condition on them?

To make P-FDT mathematically precise enough to decide unfamiliar problems, we must disambiguate these points.

### 3.1 Ex-Ante vs. Ex-Post Conditioning

Consider the candidate objective functions for policy evaluation:

* **Proposal A (Conditioned Policy Evaluation):**
  $$\pi^*_x = \argmax_{\pi \in \Pi} \mathbb{E}\left[ V \;\middle|\; \text{do}(\mathbf{FDT}_\Pi = \pi), \text{Obs} = x \right].$$
* **Proposal B (Unconditioned / Global Policy Evaluation):**
  $$\pi^* = \argmax_{\pi \in \Pi} \mathbb{E}\left[ V \;\middle|\; \text{do}(\mathbf{FDT}_\Pi = \pi) \right].$$

We argue that **Proposal B is the only mathematically coherent interpretation of P-FDT**.

If an agent conditions on $\text{Obs} = x$ inside the intervention (Proposal A), she severs the very subjunctive link that makes functional decision theories effective in asymmetric information problems. In Drescher’s Transparent Newcomb Problem or Soares’ Mechanical Blackmail, the agent’s observation $\text{Obs}$ is *causally downstream of the predictor’s prediction*, which itself *subjunctively depends on the agent’s policy*. 

If the agent were to evaluate:
$$\mathbb{E}\left[ V \;\middle|\; \text{do}(\mathbf{FDT}_\Pi = \pi), \text{Obs} = \text{blackmail} \right],$$
she would be evaluating policies under the fixed condition that blackmail was received. But the entire purpose of adopting a policy of refusing blackmail is to ensure that $P(\text{Obs} = \text{blackmail} \mid \text{do}(\mathbf{FDT}_\Pi = \pi_{\text{refuse}})) \approx 0$. Conditioning on the observation inside the $\text{argmax}$ reintroduces the very vulnerability that CDT displays: treating the observed event as an unalterable background fact rather than an endogenous consequence of one's disposition.

Thus, under our proposal, P-FDT operates **updatelessly**:
$$\mathbb{E}\left[ V \;\middle|\; \text{do}(\mathbf{FDT}_\Pi = \pi) \right] = \sum_{x' \in \mathcal{X}} P\big(\text{Obs} = x' \;\middle|\; \text{do}(\mathbf{FDT}_\Pi = \pi)\big) \cdot \mathbb{E}\left[ V \;\middle|\; \text{do}(\mathbf{FDT}_\Pi = \pi), \text{Obs} = x' \right].$$
The agent chooses the policy that balances performance across all possible branches of observation, weighted by the probability of landing in those branches *under the adoption of that policy*.

### 3.2 Distinguishing P-FDT from UDT and A-FDT

Yudkowsky and Soares note in Section 9 that the apparent lack of updating is reminiscent of Wei Dai's Updateless Decision Theory (UDT1) (Dai, 2009). However, we can now delineate the precise formal boundaries between these theories:

| Decision Theory | Object of Intervention | Epistemic Conditioning in Optimization | Mathematical Formula |
| :--- | :--- | :--- | :--- |
| **CDT** (Pearl, 2000) | Physical Act Token $\text{Act}$ | Conditions on realized observation $x$ | $\argmax_{a} \mathbb{E}\left[ V \mid \text{do}(\text{Act}=a), \text{Obs}=x \right]$ |
| **A-FDT** (Source text Eq. 4) | Action evaluation on input $x$: $\mathbf{fdt}(x)$ | Switches target of $\text{do}(\cdot)$ to $\mathbf{fdt}(x)$; conditions graph | $\argmax_{a} \mathbb{E}\left[ V \mid \text{do}(\mathbf{fdt}(x)=a) \right]$ |
| **UDT1** (Dai, 2009) | Whole program identity in formal logic | Completely unconditioned; prior distribution over mathematical models | $\argmax_{\pi} \sum_w P(w) U(w \mid \ulcorner \text{Agent} \urcorner = \pi)$ |
| **P-FDT** (Footnote 16) | Policy variable $\mathbf{FDT}_\Pi$ in graph $G$ | Evaluated unconditioned via causal/logical DAG surgery | $\pi^* = \argmax_{\pi} \mathbb{E}\left[ V \mid \text{do}(\mathbf{FDT}_\Pi = \pi) \right]$, then $a = \pi^*(x)$ |

A-FDT (Section 5 of the source) achieves "updateless" behavior through an intricate graphical transformation: it defines separate nodes $\mathbf{fdt}(\text{full})$ and $\mathbf{fdt}(\text{empty})$ in the graph, and an agent who observes $\text{Obs} = \text{full}$ shifts her intervention to the node $\mathbf{fdt}(\text{full})$. Because the predictor's node is drawn as a child of $\mathbf{fdt}(\text{full})$, intervening on $\mathbf{fdt}(\text{full})$ counterfactually alters the probability of the box being full in the first place! 

While mathematically ingenious, A-FDT's construct is graph-theoretically strained: it requires the predictor's past decision to be an explicit child of an algorithmic evaluation on an observation that might never physically materialize. 

**P-FDT is structurally cleaner:** the predictor simply models the agent's general policy $\mathbf{FDT}_\Pi$. There is only one policy node. The agent intervenes on that policy globally, deduces what a predictor would do in response to that policy, and executes the policy's recommendation at the observed history.

---

## 4. Unpacking Counterfactuals and Dependencies in P-FDT

To understand how P-FDT decides concrete cases, we must analyze its treatment of dependencies:

### 4.1 Subjunctive vs. Mere Statistical Dependencies
Like A-FDT, P-FDT sharply separates causal/subjunctive connections from mere correlations.
- In the **Smoking Lesion**, an agent's policy variable $\mathbf{FDT}_\Pi$ does not cause or subjunctively control the arterial lesion. The lesion is an exogenous biological state. Hence:
  $$P(\text{Lesion} \mid \text{do}(\mathbf{FDT}_\Pi = \pi)) = P(\text{Lesion}).$$
  P-FDT does not attempt to "manage the news" of the lesion, avoiding EDT's mistake.
- In **Newcomb's Problem**, the predictor's brain runs a simulation of $\mathbf{FDT}_\Pi$. Hence, the variable $\text{Prediction}$ is a direct child of $\mathbf{FDT}_\Pi$:
  $$P(\text{Prediction} = \text{one-box} \mid \text{do}(\mathbf{FDT}_\Pi = \pi_{\text{one-box}})) \approx 0.99.$$

### 4.2 Type vs. Token Interventions
When CDT contemplates an alternative action via $\text{do}(\text{Act}=a)$, it intervenes on a physical token. It holds fixed all non-effects of the token, including the output of any simulator calculating what that token would be. This is why CDT envisions impossible scenarios: it asks what happens if an infallible predictor predicts $2$-boxing, but the agent's arm physically reaches for $1$ box.

P-FDT intervenes on the **type**—the mathematical mapping $\pi \in \Pi$. When P-FDT evaluates a counterfactual policy $\pi'$, it propagates the change through every physical system in the universe that instantiates, simulates, or approximates $\mathbf{FDT}_\Pi$. The counterfactual world is one where the agent's reasoning was different *everywhere it is mathematically mirrored*.

---

## 5. Applying P-FDT: Canonical Examples

We now apply P-FDT to key benchmark problems to demonstrate its mechanics.

### 5.1 Parfit’s Hitchhiker

**Problem Setup:** An agent is stranded in a desert facing certain death (worth $-\$1,000,000$). A driver passes by who can detect lies with 99% accuracy. The driver will take the agent to the city if and only if she predicts that the agent, upon arriving in the city, will pay the driver $\$1,000$ from an ATM. Once in the city, there is no enforcement mechanism.

- **Observations:** $\mathcal{X} = \{\text{desert}, \text{city}\}$.
- **Actions:** $\mathcal{A} = \{\text{pay}, \text{refuse}\}$.
- **Policy Space:** $\Pi = \{\pi_{pp}, \pi_{pr}, \pi_{rp}, \pi_{rr}\}$, where $\pi_{ij}$ denotes the policy: "if in desert, do $i$; if in city, do $j$."
  Since no action is taken at the desert state (only the choice to pay once in the city matters), we reduce the policy space to:
  $$\pi_{\text{pay}}: \text{city} \mapsto \text{pay}, \qquad \pi_{\text{refuse}}: \text{city} \mapsto \text{refuse}.$$

**The P-FDT Evaluation:**
The driver's decision $\text{Rescue} \in \{\text{rescue}, \text{leave}\}$ subjunctively depends on $\mathbf{FDT}_\Pi$:
$$P(\text{Rescue} = \text{rescue} \mid \text{do}(\mathbf{FDT}_\Pi = \pi_{\text{pay}})) = 0.99,$$
$$P(\text{Rescue} = \text{rescue} \mid \text{do}(\mathbf{FDT}_\Pi = \pi_{\text{refuse}})) = 0.01.$$

Let the utility of dying in the desert be $-10^6$, arriving safely without paying be $0$, and arriving safely having paid be $-1,000$.

The agent computes the unconditioned expected utility for each candidate policy:
1. Under $\pi_{\text{pay}}$:
   $$\begin{aligned}
   \mathbb{E}[V \mid \text{do}(\mathbf{FDT}_\Pi = \pi_{\text{pay}})] &= 0.99 \cdot (-1,000) + 0.01 \cdot (-10^6) \\
   &= -990 - 10,000 = -10,990.
   \end{aligned}$$
2. Under $\pi_{\text{refuse}}$:
   $$\begin{aligned}
   \mathbb{E}[V \mid \text{do}(\mathbf{FDT}_\Pi = \pi_{\text{refuse}})] &= 0.01 \cdot (0) + 0.99 \cdot (-10^6) \\
   &= -990,000.
   \end{aligned}$$

Clearly, $\pi^* = \pi_{\text{pay}}$.

**Execution:**
Upon arriving safely at the ATM, the agent observes $x = \text{city}$. 
Applying her selected policy:
$$a^* = \pi^*(x) = \pi_{\text{pay}}(\text{city}) = \text{pay}.$$

**Comparison:**
- **CDT:** Once in the city, $\text{do}(\text{Act}=\text{pay})$ yields $-\$1,000$, whereas $\text{do}(\text{Act}=\text{refuse})$ yields $\$0$. CDT refuses to pay. Foreseeing this, the driver leaves the CDT agent in the desert to die.
- **EDT:** Conditional on being in the city, learning she pays is bad news ($-\$1,000$ vs $\$0$). EDT refuses to pay and dies.
- **P-FDT:** Maximizes over policies. Paying is an execution of an optimal global policy. The P-FDT agent pays and survives.

### 5.2 The Transparent Newcomb Problem

**Problem Setup:** Two transparent boxes, A and B. Box A contains $\$1,000$. Box B contains either $\$1,000,000$ or $\$0$. The predictor placed $\$1,000,000$ in Box B iff she predicted that the agent, upon observing both boxes to be full, would leave Box A behind. The agent looks into Box B and observes that it is full. Does she take Box B only ($1$-box) or both boxes ($2$-box)?

- **Observations:** $\mathcal{X} = \{\text{full}, \text{empty}\}$.
- **Actions:** $\mathcal{A} = \{1\text{-box}, 2\text{-box}\}$.
- **Policies:** $\pi(x) \in \mathcal{A}$. Let $\pi_{ij}$ represent $\pi(\text{full})=i, \pi(\text{empty})=j$.

**The P-FDT Evaluation:**
The predictor's placement depends on whether the agent's policy dictates $1$-boxing upon seeing a full box:
$$P(\text{Box B} = \text{full} \mid \text{do}(\mathbf{FDT}_\Pi = \pi)) = 
\begin{cases} 
0.99 & \text{if } \pi(\text{full}) = 1\text{-box}, \\
0.01 & \text{if } \pi(\text{full}) = 2\text{-box}.
\end{cases}$$

For any reasonable policy, if the agent unexpectedly sees an empty box, she will take Box A ($\pi(\text{empty}) = 2\text{-box}$), securing $\$1,000$.

Let us evaluate the two primary policies:
1. **Policy $\pi_{12}$:** $\pi(\text{full}) = 1\text{-box}$, $\pi(\text{empty}) = 2\text{-box}$.
   $$\begin{aligned}
   \mathbb{E}[V \mid \text{do}(\mathbf{FDT}_\Pi = \pi_{12})] &= P(\text{full} \mid \pi_{12}) \cdot \mathcal{U}(1\text{-box}, \text{full}) + P(\text{empty} \mid \pi_{12}) \cdot \mathcal{U}(2\text{-box}, \text{empty}) \\
   &= 0.99 \cdot (\$1,000,000) + 0.01 \cdot (\$1,000) \\
   &= \$990,000 + \$10 = \$990,010.
   \end{aligned}$$
2. **Policy $\pi_{22}$:** $\pi(\text{full}) = 2\text{-box}$, $\pi(\text{empty}) = 2\text{-box}$.
   $$\begin{aligned}
   \mathbb{E}[V \mid \text{do}(\mathbf{FDT}_\Pi = \pi_{22})] &= P(\text{full} \mid \pi_{22}) \cdot \mathcal{U}(2\text{-box}, \text{full}) + P(\text{empty} \mid \pi_{22}) \cdot \mathcal{U}(2\text{-box}, \text{empty}) \\
   &= 0.01 \cdot (\$1,001,000) + 0.99 \cdot (\$1,000) \\
   &= \$10,010 + \$990 = \$11,000.
   \end{aligned}$$

The optimal policy is unambiguously $\pi^* = \pi_{12}$.

**Execution:**
The agent looks into the boxes and receives observation $x = \text{full}$. She executes:
$$a^* = \pi^*(x) = \pi_{12}(\text{full}) = 1\text{-box}.$$

**Philosophical Implications:**
To a causal decision theorist, taking only Box B when one already sees the $\$1,000,000$ sitting inside is madness; Box A contains a "free" $\$1,000$. CDT views this as violating dominance. 
P-FDT responds with a radical re-conceptualization of dominance: **dominance must be evaluated across policies, not action tokens.** Under P-FDT’s policy-dominance principle, $\pi_{12}$ strictly dominates $\pi_{22}$ in expected utility. The agent recognizes that looking at two full boxes is an event that is *only physically possible because her policy node was set to $\pi_{12}$*. To "switch" to taking two boxes at that moment is to ask for a world where the policy was $\pi_{22}$, which would have caused her to stare at an empty box instead.

---

## 6. The True Test: Multi-Agent Coordination and Games

Footnote 16 notes:
> *"This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."*

Why does policy selection matter fundamentally in multi-agent game-theoretic dilemmas? Because in games of incomplete information or sequential play, game-theoretic solutions depend on the credible adoption of global strategies.

### 6.1 Multi-Agent Blackmail and Collusion Resistance

Consider the **Mechanical Blackmail** (Soares and Fallenstein, 2015). A blackmailer runs a program that will leak catastrophic data (costing $\$1,000,000$) unless the agent pays $\$1,000$. The blackmailer only launches the program if her predictive simulation shows that the agent will pay when blackmailed. 

Let observations be $\mathcal{X} = \{\text{blackmailed}, \emptyset\}$. Under A-FDT (intervening on the action), an agent holding the letter must conduct mental gymnastics: she intervenes on $\mathbf{fdt}(\text{blackmailed})$ and notices that in the counterfactual where she refuses, the letter was never sent, meaning she is in the $\emptyset$ state.

In P-FDT, the analysis is trivial:
- $\pi_{\text{pay}}: \text{blackmailed} \mapsto \text{pay}$. 
  Predictor simulates $\pi_{\text{pay}} \implies$ Blackmail is initiated. 
  $$\mathbb{E}[V \mid \text{do}(\mathbf{FDT}_\Pi = \pi_{\text{pay}})] = -\$1,000.$$
- $\pi_{\text{refuse}}: \text{blackmailed} \mapsto \text{refuse}$. 
  Predictor simulates $\pi_{\text{refuse}} \implies$ Blackmail is not initiated.
  $$\mathbb{E}[V \mid \text{do}(\mathbf{FDT}_\Pi = \pi_{\text{refuse}})] = \$0.$$

P-FDT selects $\pi^* = \pi_{\text{refuse}}$. The blackmail is deterred.

### 6.2 Symmetric Multi-Agent Games (The Twin Prisoner’s Dilemma)

Consider two identical P-FDT agents, Agent 1 and Agent 2, in separate rooms facing the Prisoner’s Dilemma. Each knows the other runs P-FDT.
Because they are running the identical normative procedure:
$$\mathbf{FDT}_{\Pi, 1} \equiv \mathbf{FDT}_{\Pi, 2} \equiv \mathbf{FDT}_\Pi.$$

Both agents solve:
$$\argmax_{\pi} \mathbb{E}\left[ V_i \;\middle|\; \text{do}\big(\mathbf{FDT}_\Pi = \pi\big) \right].$$

Under the intervention $\text{do}(\mathbf{FDT}_\Pi = \pi_{\text{cooperate}})$, both agents cooperate, each receiving $\$1,000,000$. Under the intervention $\text{do}(\mathbf{FDT}_\Pi = \pi_{\text{defect}})$, both defect, receiving $\$1,000$. P-FDT achieves mutual cooperation stably, without communication or external enforcement.

### 6.3 Program Games and Algorithmic Commitments

The true power of P-FDT appears in *Program Equilibrium* (Tennenholtz, 2004), where artificial agents submit source code to an interpreter:
- Suppose Agent 1 submits a program $\mathbf{p}_1$ and Agent 2 submits $\mathbf{p}_2$. 
- Each program can read the other’s source code before deciding to cooperate or defect.

An agent running CDT will examine the opponent’s code, recognize whether the opponent has cooperated or defected, and conditionally defect, because defection causally dominates for any fixed program input. As a result, two CDT agents defect against each other.

A P-FDT agent intervenes on her policy:
$$\pi_{\text{Fair}}: \text{If } \mathbf{p}_2 \text{ cooperates with } \pi_{\text{Fair}}, \text{ then cooperate; else defect}.$$
Because P-FDT searches for the optimal global mapping, it naturally finds and commits to mutual reciprocity strategies (such as Tit-For-Tat or Fair-Mutual-Cooperation). The subjunctive tracking in P-FDT ensures that the counterfactual of changing a policy changes what the other agent’s program simulation outputs. Thus, P-FDT agents achieve Pareto-optimal equilibria in program games where classical agents fail.

---

## 7. Open Problems and Critical Evaluation

While P-FDT provides an elegant and mathematically unified framework for instrumental rationality, it rests on open theoretical challenges:

### 7.1 The Computational Complexity of Policy Search
The set of policies $\Pi = \mathcal{A}^{\mathcal{X}}$ scales exponentially with the size of the observation space: $|\Pi| = |\mathcal{A}|^{|\mathcal{X}|}$. In real-world environments with rich observation histories (e.g., continuous sensory streams), searching over $\Pi$ directly is computationally intractable. 

A realistic, bounded agent cannot compute the exact $\text{argmax}_{\pi \in \Pi}$. Instead, an approximation to P-FDT must rely on localized policy optimization, parametric policy gradients, or reinforcement learning architectures that preserve subjunctive correlations while optimizing over policy parameters $\theta \in \mathbb{R}^d$.

### 7.2 The Discovery of Subjunctive Dependency Graphs
Equation (P1) assumes that the causal-logical graph $G$ is given *a priori*. Pearl (2000) provides complete algorithms (e.g., the IC algorithm) for inferring causal DAGs from observational and interventional data. However, **no analogous discovery algorithm currently exists for discovering logical and subjunctive dependencies**.

How does an autonomous agent examine its environment and determine whether an external process is merely correlated with its policy (like the lesion) or whether it contains an accurate simulation of its policy (like the predictor)? Developing a formal theory of *computational causal discovery*—detecting when external physical systems are evaluating the same mathematical function—remains the central foundational challenge for functional decision theories.

### 7.3 Logical Counterfactuals and Inconsistent Models
In evaluating:
$$\mathbb{E}[V \mid \text{do}(\mathbf{FDT}_\Pi = \pi)],$$
the agent must evaluate scenarios where a fixed mathematical algorithm outputs something other than what it actually outputs. If $\mathbf{FDT}_\Pi$ is a deterministic algorithm, then asserting $\mathbf{FDT}_\Pi = \pi'$ for $\pi' \neq \pi^*$ is asserting a logical falsehood.

P-FDT avoids explicit formal contradictions by treating $\mathbf{FDT}_\Pi$ as a macro-variable in a causal network and using Pearl's graphical surgery to override its value. Yet under the hood, if the universe is deterministic and mathematical, the agent is reasoning about counterpossibles (Cohen, 1990). A completely rigorous foundation for P-FDT will require a mature theory of *logical uncertainty* (such as Garrabrant induction; Garrabrant et al., 2016) that can define coherent probability distributions over logically contradictory statements.

---

## 8. Conclusion: Rationality as Optimal Policy Architecture

Classical decision theories evaluate actions myopically. Causal Decision Theory isolates the physical act token, blinding itself to the fact that the mind is a predictable mathematical machine embedded in an algorithmic universe. Evidential Decision Theory notices correlations but confuses mere statistical association with genuine dependency, making it easily extorted and prone to hypochondriac news-management.

**Policy Functional Decision Theory (P-FDT)**, formulated from the policy-selection principle of footnote 16, provides the most robust and elegant synthesis of functional decision making:

1. **Global Interventions:** Normative rationality chooses the best *general disposition* or policy mapping $\pi^*: \mathcal{X} \to \mathcal{A}$, evaluating its effects across the entire subjunctive structure of the world.
2. **Updateless Execution:** The policy is optimized unconditioned by the realized observation, preventing the agent from falling into dynamic inconsistencies or being blackmailed by information she already possesses.
3. **Natural Precommitment:** Because P-FDT agents select policies from an ex-ante, global perspective, they naturally exhibit the behaviors that classical agents can only achieve through expensive, ad-hoc physical precommitments.

By moving the point of intervention from the local action token $\text{Act}$ to the global policy function $\mathbf{FDT}_\Pi$, P-FDT demonstrates that one-boxing in Newcomb's problem, paying Parfit's driver, resisting blackmailers, and cooperating with psychological twins are not irrational anomalies—they are the direct, inevitable consequences of implementing the optimal decision policy.

---

## References

- Adams, E. W. (1970). Subjunctive and indicative conditionals. *Foundations of Language*, 6(1), 89–94.
- Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
- Arntzenius, F. (2008). No regrets, or: Edith Piaf revamps decision theory. *Erkenntnis*, 68(2), 277–297.
- Cohen, D. (1990). On what cannot be. In *Truth or Consequences: Essays in Honor of Nuel Belnap*, pp. 123–132. Kluwer Academic Publishers.
- Dai, W. (2009). Towards a new decision theory. *LessWrong*.
- Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
- Eells, E. (1984). Metatickles and the dynamics of deliberation. *Theory and Decision*, 17(1), 71–95.
- Garrabrant, S., Benson-Tilsen, T., Critch, A., Soares, N., & Taylor, J. (2016). Logical Induction. *arXiv preprint arXiv:1609.03543*.
- Gibbard, A., & Harper, W. L. (1978). Counterfactuals and two kinds of expected utility. In *Foundations and Applications of Decision Theory*, pp. 125–162. D. Reidel.
- Jeffrey, R. C. (1983). *The Logic of Decision* (2nd ed.). University of Chicago Press.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1979). Prisoners’ dilemma is a Newcomb problem. *Philosophy & Public Affairs*, 8(3), 235–240.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
- Nozick, R. (1969). Newcomb’s problem and two principles of choice. In *Essays in Honor of Carl G. Hempel*, pp. 114–146. D. Reidel.
- Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
- Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
- Skyrms, B. (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
- Soares, N., & Fallenstein, B. (2015). Toward idealized decision theory. *arXiv preprint arXiv:1507.01986*.
- Tennenholtz, M. (2004). Program equilibrium. *Games and Economic Behavior*, 49(2), 363–373.
- Yudkowsky, E., & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. *arXiv preprint arXiv:1710.05060v2*.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/3ebd5e93-35c3-4f6c-a1d0-ab382f03cbf0/call_0/request.json)

[Authoritative raw response](../../../../../../runs/3ebd5e93-35c3-4f6c-a1d0-ab382f03cbf0/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Game**

I'm currently focused on dissecting the symmetric Prisoner's Dilemma setup. It involves two identical LLM models, operating independently based on a P-FDT framework. The key is understanding how the game payoff matrix influences their strategic decisions within this specific context. The setup is quite interesting.


**Clarifying Payoff Dynamics**

I'm now diving deeper into the specific payoff matrix within the P-FDT framework. The values, where both cooperate (-2), both defect (-4), or one defects (0) and the other cooperates (-5) are central. The P-FDT section shows how identical agents, running the same procedure, logically converge on mutual cooperation to achieve their shared goal. Despite the agents having private details, they're both running the same program.


```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/3ebd5e93-35c3-4f6c-a1d0-ab382f03cbf0/call_1/request.json)

[Authoritative raw response](../../../../../../runs/3ebd5e93-35c3-4f6c-a1d0-ab382f03cbf0/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Setup**

I'm currently focused on the framework. I've got two identical LLM executions, sharing the same parameters and the Prisoner's Dilemma context. The decision-making is rooted in P-FDT. I've also set up the sentence matrix. Now, I'm carefully reviewing the specifics.


```
