# Intervening on Algorithms: A Mathematical Account of Policy Functional Decision Theory (P-FDT)

## 1. Introduction: From Acts to Algorithms

Classical normative decision theories diverge sharply when an agent’s physical environment contains accurate predictors or cognitive replicas of the agent itself. Evidential Decision Theory ($\mathrm{EDT}$) prescribes acts that serve as the best subjective news:
$$\mathrm{EDT}(P, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left[\mathcal{V} \mid \mathrm{Obs}=x, \mathrm{Act}=a\right].$$
In doing so, $\mathrm{EDT}$ successfully navigates Newcomb's problem by one-boxing, but falls prey to mere statistical correlations in the Smoking Lesion problem and succumbs to extortion in scenarios like the XOR Blackmail. 

Causal Decision Theory ($\mathrm{CDT}$), formalised by Gibbard and Harper (1978), Lewis (1981), and Pearl (2000), corrects for spurious correlations by severing non-causal dependencies via the graph-theoretic intervention operator $\mathrm{do}(\mathrm{Act}=a)$:
$$\mathrm{CDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left[\mathcal{V} \mid \mathrm{do}(\mathrm{Act}=a), \mathrm{Obs}=x\right].$$
Yet by intervening strictly on the token physical act $\mathrm{Act}$, $\mathrm{CDT}$ severs the logical dependencies between an agent’s decision process and past predictions made about that process. Consequently, $\mathrm{CDT}$ two-boxes in Newcomb's problem, dies in the desert in Parfit’s Hitchhiker, and exhibits cycling instabilities in Death in Damascus.

To overcome these structural defects, Yudkowsky and Soares (2017) introduce *Functional Decision Theory* ($\mathrm{FDT}$). $\mathrm{FDT}$ replaces interventions on physical tokens with interventions on mathematical types: an agent evaluates counterfactual changes to the logical output of the very mathematical function she is computing.

In the primary text of Yudkowsky and Soares (2017), $\mathrm{FDT}$ is formalized as choosing an *act* by intervening on an observation-specific decision node:
$$\FDT(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left[\mathcal{V} \mid \mathrm{do}\left(\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right].$$
However, in Footnote 16 (and foreshadowed in Footnote 7), the authors acknowledge an important technical variant:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions... [T]he author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action."

We call this refined normative architecture **Policy Functional Decision Theory** ($\mathrm{P\text{-}FDT}$). While standard $\mathrm{FDT}$ intervenes on local execution branches, $\mathrm{P\text{-}FDT}$ elevates the unit of rational choice to the global decision rule itself. 

The purpose of this essay is to develop $\mathrm{P\text{-}FDT}$ into a fully explicit, self-contained mathematical framework. We will formalize its policy spaces, define its counterfactual evaluation mechanics, resolve theoretical ambiguities left open by Footnote 16, and demonstrate how it resolves classic single-agent and multi-agent dilemmas.

---

## 2. Foundations and Notation

### 2.1 Probability, Observation, and Outcome Spaces
Let $\mathcal{X}$ denote a countable set of possible observation histories, $\mathcal{A}$ a finite set of feasible physical actions, and $\mathcal{O}$ a countable set of world outcomes. The agent's subjective evaluations over outcomes are given by a bounded utility function $\mathcal{U}: \mathcal{O} \to \mathbb{R}$, yielding a real-valued random variable $\mathcal{V} \coloneqq \mathcal{U}(\mathrm{Outcome})$. 

In standard sequential choice, an agent receives an observation $x \in \mathcal{X}$ and selects an action $a \in \mathcal{A}$. A deterministic decision policy is a total function:
$$\pi: \mathcal{X} \to \mathcal{A}.$$
We denote the collection of all admissible policies by $\Pi \coloneqq \mathcal{A}^{\mathcal{X}}$. When randomized strategies are required, $\Pi$ may be generalized to the set of Markov kernels $\pi: \mathcal{X} \to \Delta(\mathcal{A})$.

### 2.2 Subjunctive Graphical Models
To model environments populated by cognitive models, clones, or algorithmic simulations, the agent equips a probability distribution $P$ with an augmented directed acyclic graph $G = (\mathbf{V}, \mathbf{E})$. 

The vertex set $\mathbf{V}$ includes standard empirical random variables (such as environmental states, sensory observations $\mathrm{Obs}$, and physical actions $\mathrm{Act}$) alongside *computational variables*. A computational variable represents the evaluated output of an algorithm or mathematical function. Specifically, $G$ contains a master policy variable, denoted $\mathbf{\Pi}^\star$, which represents the output of the agent's normative decision procedure.

Correlations between variables in $G$ are not restricted to physical mechanisms mediated by spacetime signals. Rather, $G$ encodes *subjunctive dependencies*—structural, nomic, or logical dependencies where multiple nodes vary systematically with the output of an algorithm:
- If a predictor constructs an internal simulation $\widehat{\pi}$ of the agent's code, the predictor's internal representation depends subjunctively on $\mathbf{\Pi}^\star$.
- If an agent possesses a psychological twin, both agents’ physical actions depend subjunctively on the identical mathematical procedure $\mathbf{\Pi}^\star$.

Following Pearl (2000), for any subset of variables $\mathbf{W} \subset \mathbf{V}$ and assigned values $\mathbf{w}$, the surgery operator $\mathrm{do}(\mathbf{W} = \mathbf{w})$ yields an interventional distribution $P(\cdot \mid \mathrm{do}(\mathbf{W} = \mathbf{w}))$. Under this operation, all incoming edges into $\mathbf{W}$ in $G$ are deleted, setting $\mathbf{W} \coloneqq \mathbf{w}$, while the conditional distributions of all non-descendants and remaining downstream nodes are preserved:
$$P(\mathbf{V} \setminus \mathbf{W} \mid \mathrm{do}(\mathbf{W} = \mathbf{w})) = \prod_{Y \in \mathbf{V} \setminus \mathbf{W}} P(Y \mid \mathrm{Parents}_G(Y))\Big|_{\mathbf{W}=\mathbf{w}}.$$
In $\mathrm{P\text{-}FDT}$, Pearl's $\mathrm{do}$-operator is applied directly to the master policy node $\mathbf{\Pi}^\star$.

---

## 3. Mathematical Formulation of P-FDT

### 3.1 The Algorithmic Operator
To establish the formal procedure for $\mathrm{P\text{-}FDT}$, we must address the self-referential property central to functional decision theories. The agent's world-model $M = (P, G)$ contains a variable designating the output of the agent's own decision procedure:
$$\mathbf{\Pi}^\star \equiv \operatorname{pfdt}(\underline{P}, \underline{G}),$$
where underlines indicate Gödel codes or syntactic encodings of the arguments. By Kleene's Second Recursion Theorem, an algorithm can manipulate and inspect an explicit blueprint of its own source code without circular paradox. 

$\mathrm{P\text{-}FDT}$ separates the agent's deliberation into two distinct mathematical phases:
1. **Policy Selection:** The agent determines the optimal global policy $\pi^\star \in \Pi$ by maximizing expected utility under counterfactual interventions on the policy variable $\mathbf{\Pi}^\star$.
2. **Policy Execution:** The agent evaluates the selected policy $\pi^\star$ on her actual observation history $x \in \mathcal{X}$ to output an action $a^\star = \pi^\star(x)$.

The formal specification of the $\mathrm{P\text{-}FDT}$ decision procedure is as follows:

```
Algorithm 1: Policy Functional Decision Theory (P-FDT)
Input : Probability distribution P, Subjunctive graph G, Observation history x
Output: Executable physical action a*

1. Identify candidate policy set: Π ⊆ A^X
2. For each policy π ∈ Π:
     Compute hypothetical expected utility:
       EU(π) = E_P [ V | do( pfdt(P, G) = π ) ]
3. Determine the optimal policy:
     π* = argmax_{π ∈ Π} EU(π)
4. Execute action:
     a* = π*(x)
5. Return a*
```

Formally, we write:
$$\operatorname{P\text{-}FDT}(P, G, x) \coloneqq \left[\operatorname*{argmax}_{\pi \in \Pi} \mathbb{E}_P\left[\mathcal{V} \;\middle|\; \mathrm{do}\left(\operatorname{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right]\right](x). \tag{1}$$

### 3.2 Act-FDT vs. Policy-FDT: The Fundamental Equation
To appreciate the divergence between the act-level formalization ($\mathrm{A\text{-}FDT}$) presented in Equation (4) of Yudkowsky and Soares (2017) and $\mathrm{P\text{-}FDT}$, let us inspect their interventional targets.

In $\mathrm{A\text{-}FDT}$, the graph $G$ maintains a family of nodes indexed by potential observations, $\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x})$. Upon observing $x$, $\mathrm{A\text{-}FDT}$ leaves past or alternate branches unconstrained and intervenes locally:
$$\mathrm{A\text{-}FDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}_P\left[\mathcal{V} \;\middle|\; \mathrm{do}\left(\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right]. \tag{2}$$

In $\mathrm{P\text{-}FDT}$, the agent does not intervene on a localized action variable. Instead, the agent intervenes on the entire mapping:
$$\mathrm{do}\left(\mathbf{\Pi}^\star = \pi\right).$$
In any subjunctive causal graph representing the agent’s situated execution, the token physical action $\mathrm{Act}$ is a child of both the observation history $\mathrm{Obs}$ and the policy node $\mathbf{\Pi}^\star$:
$$\mathrm{Act} = \mathbf{\Pi}^\star(\mathrm{Obs}).$$
Furthermore, if an external predictor or twin seeks to forecast the agent, that predictor models the mapping $\mathbf{\Pi}^\star$. 

Intervening on $\mathbf{\Pi}^\star$ propagates counterfactual updates simultaneously across all observation branches:
$$\mathbb{E}_P\left[\mathcal{V} \;\middle|\; \mathrm{do}(\mathbf{\Pi}^\star = \pi)\right] = \sum_{x' \in \mathcal{X}} P(\mathrm{Obs}=x' \mid \mathrm{do}(\mathbf{\Pi}^\star = \pi)) \sum_{o \in \mathcal{O}} P(o \mid \mathrm{do}(\mathbf{\Pi}^\star = \pi), \mathrm{Obs}=x') \mathcal{U}(o).$$
Because the policy $\pi$ affects which observations $x'$ are likely to be realized in the first place, $\mathrm{P\text{-}FDT}$ inherently captures *selection effects on information*.

---

## 4. Resolving Open Theoretical Questions in Footnote 16

Footnote 16 of Yudkowsky and Soares (2017) provides the conceptual seed of $\mathrm{P\text{-}FDT}$ but leaves three critical mathematical and operational problems unaddressed:
1. Does the policy selection step condition on the current observation $x$?
2. How is policy optimization constrained over infinite or intractable observation spaces?
3. What is the formal boundary between valid subjunctive dependence and illicit counterfactual magic?

Below, we identify the ambiguities inherent in the source text and propose concrete mathematical solutions.

### 4.1 Epistemic Status: Updatelessness vs. Conditional Deliberation
*Ambiguity in the Source:* When an agent executes $\operatorname{P\text{-}FDT}(P, G, x)$, she already possesses the observation history $\mathrm{Obs} = x$. Should the expectation in Equation (1) be evaluated relative to the unconditioned prior $P(\cdot)$ or the conditioned posterior $P(\cdot \mid \mathrm{Obs}=x)$?

*Analysis and Proposal:* If the agent conditions her world-model on $\mathrm{Obs}=x$ prior to evaluating the intervention $\mathrm{do}(\mathbf{\Pi}^\star = \pi)$, she re-introduces the vulnerabilities of update-splitting. Specifically, conditioning on an observation that was causally or subjunctively downstream of the predictor’s assessment of $\mathbf{\Pi}^\star$ can sever the agent’s ability to counterfactually alter whether that observation occurs.

Consider an agent who is blackmailed: the observation $x_{\mathrm{letter}}$ occurs only if the blackmailer predicted that the agent would submit to extortion. If the agent conditions on $x_{\mathrm{letter}}$ before optimizing her policy, she must evaluate what a policy does given that she is *already holding the letter*. Under a naive conditioning:
$$P(\mathrm{Blackmailer\ Sent\ Letter} \mid \mathrm{Obs}=x_{\mathrm{letter}}, \mathrm{do}(\mathbf{\Pi}^\star = \pi)) = 1.$$
Under such an evaluation, a policy refusing payment simply incurs the catastrophic punishment.

To maintain theoretical consistency with the foundational aims of $\mathrm{FDT}$, **$\mathrm{P\text{-}FDT}$ must be formulated as an updateless policy optimization**. The expectation must be computed with respect to the root distribution $P_0$ (the prior over initial problem states) prior to conditioning on the factual observation $x$:
$$\pi^\star = \operatorname*{argmax}_{\pi \in \Pi} \mathbb{E}_{P_0}\left[\mathcal{V} \;\middle|\; \mathrm{do}\left(\mathbf{\Pi}^\star = \pi\right)\right]. \tag{3}$$
The observation $x$ is not an input to the maximization operator; it serves solely as an evaluation argument during the physical execution step: $a^\star = \pi^\star(x)$. 

This establishes a clean conceptual separation:
- **Belief updating** via Bayesian conditionalization operates to maintain the agent's passive world model.
- **Counterfactual optimization** occurs globally over the unconditional policy space.

### 4.2 Computational Complexity and Bounded Policy Spaces
*Ambiguity in the Source:* The space of policies $\Pi = \mathcal{A}^\mathcal{X}$ scales as $|\mathcal{A}|^{|\mathcal{X}|}$. If $\mathcal{X}$ contains continuous signals or unbounded sequences of interaction, $\Pi$ is uncountably infinite, rendering naive maximization mathematically ill-defined or computationally impossible.

*Analysis and Proposal:* For mathematical rigor, an admissible policy must be computable. We formalize $\Pi$ not as the set of arbitrary extensional functions, but as the set of Turing machines $\mathcal{M}$ bounded by program length $K$ and computational time limit $T$:
$$\Pi_{K, T} \coloneqq \left\{ \mu \in \mathcal{M} \;\middle|\; \operatorname{len}(\mu) \le K, \; \forall x \in \mathcal{X}: \operatorname{Time}(\mu(x)) \le T \right\}.$$
In real-world or artificial intelligence implementations, $\Pi$ corresponds to a parameterized family of policy architectures (e.g., neural policy networks $\pi_\theta$). The argmax is computed via policy gradient optimization or symbolic algorithmic search over the interventional objective:
$$\theta^\star = \operatorname*{argmax}_{\theta} \mathbb{E}_{P_0}\left[\mathcal{V} \;\middle|\; \mathrm{do}\left(\mathbf{\Pi}^\star = \pi_\theta\right)\right].$$

### 4.3 The Semantics of Subjunctive Edges
*Ambiguity in the Source:* Yudkowsky and Soares state that an agent intervenes on a logical node, but note that a comprehensive calculus for generating subjunctive dependency graphs from raw observational data remains an open problem.

*Analysis and Proposal:* We propose the following formal criterion for establishing a subjunctive edge from $\mathbf{\Pi}^\star$ to an environmental node $Y$ in $G$. 

Let $\operatorname{Comp}(Y)$ denote the physical or biological system that determines the value of $Y$. A directed subjunctive edge $\mathbf{\Pi}^\star \to Y$ is valid if and only if:
1. $\operatorname{Comp}(Y)$ explicitly executes or simulates an algorithm $\widehat{\pi}$ whose input-output specification is provably identical to $\mathbf{\Pi}^\star$; or
2. $\operatorname{Comp}(Y)$ contains a statistical or deductive model whose parameter updates correlate with the input-output behavior of $\mathbf{\Pi}^\star$ across counterfactual perturbations.

Where the correlation between an agent’s choice and an environmental event is driven by an underlying physiological or physical third variable without any simulation of the decision process (as in the Smoking Lesion Problem), no edge from $\mathbf{\Pi}^\star$ exists.

---

## 5. Comparative Evaluation in Paradigmatic Dilemmas

We now apply $\mathrm{P\text{-}FDT}$ to the canonical decision problems treated by Yudkowsky and Soares (2017), contrasting its mechanics with $\mathrm{CDT}$, $\mathrm{EDT}$, and act-level $\mathrm{A\text{-}FDT}$.

### 5.1 Newcomb's Problem
In standard Newcomb's problem, Box A contains $\$1,000$ and Box B contains either $\$1,000,000$ or $\$0$. The observation history is trivial: $x = \emptyset$. The policy set reduces to constant functions:
$$\Pi = \{\pi_1, \pi_2\}, \quad \text{where } \pi_1(\emptyset) = \mathrm{one\text{-}box}, \; \pi_2(\emptyset) = \mathrm{two\text{-}box}.$$
The graph $G$ contains the master policy $\mathbf{\Pi}^\star = \operatorname{pfdt}(\underline{P}, \underline{G})$. Because the predictor’s forecast $\mathrm{Pred} \in \{1, 2\}$ is based on an accurate model of this procedure, $G$ contains the directed path:
$$\mathbf{\Pi}^\star \longrightarrow \mathrm{Pred} \longrightarrow \mathrm{Box\ B} \longrightarrow \mathrm{Outcome} \longrightarrow \mathcal{V}.$$
Simultaneously, the physical act node depends directly on the policy:
$$\mathbf{\Pi}^\star \longrightarrow \mathrm{Act} \longrightarrow \mathrm{Outcome}.$$

$\mathrm{P\text{-}FDT}$ computes:
$$\mathbb{E}\left[\mathcal{V} \mid \mathrm{do}(\mathbf{\Pi}^\star = \pi_1)\right] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000,$$
$$\mathbb{E}\left[\mathcal{V} \mid \mathrm{do}(\mathbf{\Pi}^\star = \pi_2)\right] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$
The policy $\pi_1$ uniquely maximizes expected utility. The agent executes $\pi_1(\emptyset) = \mathrm{one\text{-}box}$, walking away with $\$1,000,000$. 

$\mathrm{CDT}$ fails here because it intervenes on $\mathrm{Act}$, severing the dependence on $\mathrm{Pred}$, and concluding that two-boxing dominates.

### 5.2 The Transparent Newcomb Problem
In the Transparent Newcomb problem, both boxes are transparent. The agent directly observes whether Box B is full or empty prior to deciding:
$$\mathcal{X} = \{x_{\mathrm{full}}, x_{\mathrm{empty}}\}, \quad \mathcal{A} = \{\mathrm{one\text{-}box}, \mathrm{two\text{-}box}\}.$$
The policy space $\Pi = \mathcal{A}^\mathcal{X}$ contains four candidate policies:
- $\pi_{1,1}$: One-box if full, one-box if empty.
- $\pi_{1,2}$: One-box if full, two-box if empty.
- $\pi_{2,1}$: Two-box if full, one-box if empty.
- $\pi_{2,2}$: Two-box if full, two-box if empty.

The predictor fills Box B if and only if she predicts the agent will leave Box A behind upon seeing both boxes full. Thus, Box B's contents depend subjunctively on the policy's specific output on the branch $x_{\mathrm{full}}$:
$$P(\mathrm{Box\ B} = \mathrm{full} \mid \mathrm{do}(\mathbf{\Pi}^\star = \pi)) = 
\begin{cases} 
0.99 & \text{if } \pi(x_{\mathrm{full}}) = \mathrm{one\text{-}box}, \\
0.01 & \text{if } \pi(x_{\mathrm{full}}) = \mathrm{two\text{-}box}.
\end{cases}$$

Let us evaluate the expected utility of the policies under unconditioned policy optimization:
$$\begin{aligned}
\mathbb{E}\left[\mathcal{V} \mid \mathrm{do}(\mathbf{\Pi}^\star = \pi_{1,2})\right] &= P(\mathrm{full} \mid \mathrm{do}(\pi_{1,2})) \cdot \mathcal{U}(\mathrm{one\text{-}box}, \mathrm{full}) + P(\mathrm{empty} \mid \mathrm{do}(\pi_{1,2})) \cdot \mathcal{U}(\mathrm{two\text{-}box}, \mathrm{empty}) \\
&= 0.99 \times \$1,000,000 + 0.01 \times \$1,000 = \$990,010.
\end{aligned}$$
$$\begin{aligned}
\mathbb{E}\left[\mathcal{V} \mid \mathrm{do}(\mathbf{\Pi}^\star = \pi_{2,2})\right] &= P(\mathrm{full} \mid \mathrm{do}(\pi_{2,2})) \cdot \mathcal{U}(\mathrm{two\text{-}box}, \mathrm{full}) + P(\mathrm{empty} \mid \mathrm{do}(\pi_{2,2})) \cdot \mathcal{U}(\mathrm{two\text{-}box}, \mathrm{empty}) \\
&= 0.01 \times \$1,001,000 + 0.99 \times \$1,000 = \$11,000.
\end{aligned}$$

The optimal policy is unambiguously $\pi^\star = \pi_{1,2}$. 

Now suppose the agent enters the room and observes two full boxes ($x = x_{\mathrm{full}}$). $\mathrm{CDT}$ and $\mathrm{EDT}$ agents, conditioning on the factual state of the boxes, reason that the $\$1,000,000$ is already present and take both boxes. In contrast, the $\mathrm{P\text{-}FDT}$ agent simply evaluates her optimal policy on the factual input:
$$a^\star = \pi^\star(x_{\mathrm{full}}) = \mathrm{one\text{-}box}.$$
The $\mathrm{P\text{-}FDT}$ agent one-boxes without regret, because she understands that executing any policy that yields $\pi(x_{\mathrm{full}}) = \mathrm{two\text{-}box}$ would have subjunctively caused the predictor to leave Box B empty.

### 5.3 Parfit's Hitchhiker
In Parfit’s Hitchhiker, the agent is stranded in a desert. A driver with high predictive accuracy will rescue the agent if and only if she predicts that the agent will pay $\$1,000$ upon reaching the city. Dying in the desert costs $\$1,000,000$.

Let the observations be $\mathcal{X} = \{x_{\mathrm{city}}, x_{\mathrm{desert}}\}$ and actions $\mathcal{A} = \{\mathrm{pay}, \mathrm{refuse}\}$.
The policies are mappings $\pi: \{x_{\mathrm{city}}, x_{\mathrm{desert}}\} \to \{\mathrm{pay}, \mathrm{refuse}\}$. 
The driver's decision to offer a ride depends subjunctively on whether $\pi(x_{\mathrm{city}}) = \mathrm{pay}$.

Under $\mathrm{P\text{-}FDT}$:
$$\mathbb{E}\left[\mathcal{V} \mid \mathrm{do}(\mathbf{\Pi}^\star(x_{\mathrm{city}}) = \mathrm{pay})\right] \approx -\$1,000,$$
$$\mathbb{E}\left[\mathcal{V} \mid \mathrm{do}(\mathbf{\Pi}^\star(x_{\mathrm{city}}) = \mathrm{refuse})\right] \approx -\$1,000,000.$$
The optimal policy selects $\pi^\star(x_{\mathrm{city}}) = \mathrm{pay}$. Upon arrival in the safety of the city, the $\mathrm{P\text{-}FDT}$ agent does not attempt to "re-deliberate" or maximize utility locally; she executes $\pi^\star(x_{\mathrm{city}}) = \mathrm{pay}$. 

Where $\mathrm{CDT}$ and $\mathrm{EDT}$ agents defect once rescued and therefore die in the desert, $\mathrm{P\text{-}FDT}$ achieves the optimal payout by recognizing that rational action consists in executing the globally optimal algorithmic disposition.

### 5.4 The Smoking Lesion Problem
The Smoking Lesion problem illustrates how $\mathrm{P\text{-}FDT}$ avoids the news-managing pathology of $\mathrm{EDT}$. A genetic arterial lesion causes both a strong desire to smoke and lung cancer. Smoking provides $\$1,000$ of enjoyment; cancer imposes a $\$1,000,000$ penalty.

Let $\mathbf{\Pi}^\star$ denote the agent's policy procedure. Does the lesion subjunctively depend on $\mathbf{\Pi}^\star$?
Crucially, no. The lesion is a static biological condition. It does not model, predict, or simulate the mathematical output of $\mathbf{\Pi}^\star$. 

Therefore, in Fiona's graph $G$, the variable $\mathrm{Lesion}$ has no incoming edges from $\mathbf{\Pi}^\star$:
$$P(\mathrm{Lesion} \mid \mathrm{do}(\mathbf{\Pi}^\star = \pi_{\mathrm{smoke}})) = P(\mathrm{Lesion} \mid \mathrm{do}(\mathbf{\Pi}^\star = \pi_{\mathrm{refrain}})) = P(\mathrm{Lesion}).$$
Counterfactually altering the output of the policy does not alter the incidence of cancer:
$$\mathbb{E}\left[\mathcal{V} \mid \mathrm{do}(\mathbf{\Pi}^\star = \pi_{\mathrm{smoke}})\right] = \mathbb{E}\left[\mathcal{V} \mid \mathrm{do}(\mathbf{\Pi}^\star = \pi_{\mathrm{refrain}})\right] + \$1,000.$$
$\mathrm{P\text{-}FDT}$ selects $\pi^\star = \pi_{\mathrm{smoke}}$. The agent smokes, securing the $\$1,000$ surplus. Unlike $\mathrm{EDT}$, $\mathrm{P\text{-}FDT}$ distinguishes between an environmental variable that *predicts* an algorithm and one that merely shares a *common statistical origin* with an agent's preferences.

---

## 6. Where P-FDT Transcends Act-FDT: Multi-Agent and Dynamic Dilemmas

Footnote 16 notes that moving from act-level interventions to policy-level interventions "makes a difference in certain multi-agent dilemmas." Why should this be so? We examine two domains where $\mathrm{P\text{-}FDT}$ demonstrates decisive advantages over $\mathrm{A\text{-}FDT}$: game-theoretic coordination and sequential deterrence.

### 6.1 Multi-Agent Twin Dilemmas and Correlated Equilibria
Consider a symmetric coordination game played between two computational twins, Agent 1 and Agent 2, with actions $\mathcal{A} = \{C, D\}$. Both agents implement the identical normative theory. The payoff matrix is an asymmetric coordination problem:

| | $C$ | $D$ |
|---|:---:|:---:|
| **$C$** | $(5, 5)$ | $(0, 0)$ |
| **$D$** | $(0, 0)$ | $(1, 1)$ |

Now suppose the agents receive private correlated signals $x_1, x_2 \in \{0, 1\}$ from a shared external random event (e.g., parity of cosmic rays), which allows them to coordinate on alternating asymmetric payouts or randomized conventions.

Under act-level $\mathrm{A\text{-}FDT}$, Agent 1 intervenes on $\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x}_1)$ in isolation. If the two agents receive different observations ($x_1 \neq x_2$), their intervention nodes are formally distinct variables in the graph:
$$\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x}_1) \neq \mathrm{fdt}(\underline{P}, \underline{G}, \underline{x}_2).$$
As a consequence, $\mathrm{A\text{-}FDT}$ can lose the logical symmetry between the agents across heterogeneous observation branches. The agents may treat each other's decisions as decoupled whenever their local information differs, destroying their ability to coordinate.

In contrast, under $\mathrm{P\text{-}FDT}$, both agents recognize that they share the exact same decision architecture:
$$\mathbf{\Pi}_1^\star = \mathbf{\Pi}_2^\star = \mathbf{\Pi}^\star.$$
When Agent 1 evaluates an intervention on $\mathbf{\Pi}^\star$, she is evaluating the mapping across *all* observation states simultaneously:
$$\mathrm{do}(\mathbf{\Pi}^\star = \pi).$$
Because Agent 2 implements $\mathbf{\Pi}^\star$, Agent 1 knows with mathematical certainty that for any observation pair $(x_1, x_2)$, Agent 2 will execute $\pi(x_2)$ whenever Agent 1 executes $\pi(x_1)$. 

$\mathrm{P\text{-}FDT}$ agents optimize over the joint distribution of actions induced by the shared policy mapping:
$$\pi^\star = \operatorname*{argmax}_{\pi \in \Pi} \sum_{x_1, x_2} P(x_1, x_2) \, \mathcal{U}_1\left(\pi(x_1), \pi(x_2)\right).$$
This allows $\mathrm{P\text{-}FDT}$ agents to natively achieve correlated equilibria and cooperative conventions without physical communication, entirely through shared subjunctive reliance on a common policy function.

### 6.2 Counterfactual Blackmail and Threat Deterrence
The superiority of policy-level intervention becomes starkly apparent in dynamic extortion problems, such as the Mechanical Blackmail (Yudkowsky and Soares, 2017).

A blackmailer possesses compromising data that will destroy both the agent and the blackmailer (costing each $\$1,000,000$). The blackmailer writes an automated script that checks whether the agent would pay $\$1,000$ if blackmailed. If the script predicts payment, it runs an irreversible program that demands $\$1,000$ and notifies the agent via letter.

Let $\mathcal{X} = \{x_{\mathrm{letter}}, x_{\emptyset}\}$. The actions are $\mathcal{A} = \{\mathrm{pay}, \mathrm{refuse}\}$.
The policies are:
- $\pi_{\mathrm{complier}}$: $\pi(x_{\mathrm{letter}}) = \mathrm{pay}, \; \pi(x_{\emptyset}) = \mathrm{refuse}$.
- $\pi_{\mathrm{deterrent}}$: $\pi(x_{\mathrm{letter}}) = \mathrm{refuse}, \; \pi(x_{\emptyset}) = \mathrm{refuse}$.

The blackmailer's program runs if and only if it predicts $\mathbf{\Pi}^\star(x_{\mathrm{letter}}) = \mathrm{pay}$.

Under $\mathrm{P\text{-}FDT}$, the agent optimizes her policy from the root prior $P_0$:
$$\mathbb{E}\left[\mathcal{V} \mid \mathrm{do}(\mathbf{\Pi}^\star = \pi_{\mathrm{complier}})\right] = 1.0 \times (-\$1,000) = -\$1,000.$$
$$\mathbb{E}\left[\mathcal{V} \mid \mathrm{do}(\mathbf{\Pi}^\star = \pi_{\mathrm{deterrent}})\right] = 1.0 \times (\$0) = \$0.$$

$\mathrm{P\text{-}FDT}$ selects $\pi^\star = \pi_{\mathrm{deterrent}}$. Because the blackmailer accurately simulates this policy, the blackmailer aborts the scheme. The letter is never sent.

Now consider the counterfactual query: *What if the blackmailer makes a small prediction error $\epsilon > 0$, and the agent actually finds herself holding the blackmail letter ($x = x_{\mathrm{letter}}$)?*

Under act-level $\mathrm{A\text{-}FDT}$, the agent intervenes locally on $\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x}_{\mathrm{letter}})$. As discussed in Section 9 of the source paper, the agent must perform the strange mental gymnastics of imagining that switching her act to $\mathrm{refuse}$ causes her to enter a counterfactual world where the letter in her hands disappears.

$\mathrm{P\text{-}FDT}$ requires no such bizarre retroactive updating. Under $\mathrm{P\text{-}FDT}$, the agent’s deliberation was already concluded at the global policy level:
$$\pi^\star = \pi_{\mathrm{deterrent}}.$$
Upon seeing $x_{\mathrm{letter}}$, the agent does not attempt to reconstruct the universe or change the past. She simply evaluates the function:
$$a^\star = \pi^\star(x_{\mathrm{letter}}) = \mathrm{refuse}.$$
Even though the blackmailer erred, the agent refuses to pay because she is an execution trace of a policy designed to make extortion unprofitable. By committing to execute the policy faithfully even under observation error, $\mathrm{P\text{-}FDT}$ agents establish perfectly credible commitments without requiring external physical locking mechanisms.

---

## 7. Comparative Theoretical Synthesis

The operational differences between the major decision theories are summarized in the following table:

| Decision Theory | Mathematical Intervention Object | Deliberative Timing | Response to Predictors | Behavior in Newcomb | Behavior in Smoking Lesion | Stability in Death in Damascus |
|---|---|---|---|---|---|---|
| **EDT** | None (Bayesian conditioning) | Posterior: $\operatorname{argmax}_a \mathbb{E}[\mathcal{V} \mid x, a]$ | Respects all correlations | One-box | Refrains (suboptimal) | Flawed (manages news) |
| **CDT** | Token Physical Act: $\mathrm{do}(\mathrm{Act}=a)$ | Posterior: $\operatorname{argmax}_a \mathbb{E}[\mathcal{V} \mid \mathrm{do}(a), x]$ | Ignores logical dependencies | Two-box (poor) | Smokes (optimal) | Unstable (cyclic regret) |
| **A-FDT** | Local Algorithmic Node: $\mathrm{do}(\mathrm{fdt}(x)=a)$ | Branch-Specific: $\operatorname{argmax}_a \mathbb{E}[\mathcal{V} \mid \mathrm{do}(\mathrm{fdt}(x)=a)]$ | Tracks subjunctive dependencies | One-box (rich) | Smokes (optimal) | Stable (stays in Damascus) |
| **P-FDT** | Global Policy Mapping: $\mathrm{do}(\mathbf{\Pi}^\star=\pi)$ | Updateless Global Prior: $\pi^\star = \operatorname{argmax}_\pi \mathbb{E}[\mathcal{V} \mid \mathrm{do}(\pi)]$ | Optimizes across all branches simultaneously | One-box (rich) | Smokes (optimal) | Stable & Robust in Multi-Agent Games |

---

## 8. Philosophical Implications: Rationality and Reflective Stability

$\mathrm{P\text{-}FDT}$ challenges two entrenched tenets of contemporary decision theory: the principle of *act dominance* and the axiom of *subgame dynamic consistency*.

### 8.1 The Illusion of Act Dominance
Causal decision theorists have long defended two-boxing in Newcomb's problem by appealing to dominance: in every physical state of the world, Box B is already full or already empty; hence taking both boxes yields $\$1,000$ more than taking one.

$\mathrm{P\text{-}FDT}$ demonstrates that standard dominance arguments rely on an illicit counterfactual factorization. Holding the past fixed while varying the agent’s act assumes that an agent's physical choice can vary independently of the mathematical decision function it instantiates. This is logically equivalent to holding the sum $6288 + 1048$ fixed while asking what happens if an arithmetic calculator outputs $3159$. 

Dominance is only meaningful when defined across *subjunctively realizable states*. In a world where predictors model algorithms, the states of the environment are themselves functions of the policy:
$$\mathcal{S} = \mathcal{S}(\mathbf{\Pi}^\star).$$
When dominance is properly evaluated over policy mappings, $\pi_{\mathrm{one\text{-}box}}$ strictly dominates $\pi_{\mathrm{two\text{-}box}}$. $\mathrm{P\text{-}FDT}$ restores the alignment between expected utility maximization and structural dominance.

### 8.2 Reflective Stability Without Binding Precommitments
A chronic failing of $\mathrm{CDT}$ is its temporal and reflective instability. A $\mathrm{CDT}$ agent facing a Transparent Newcomb problem or Parfit’s Hitchhiker would gladly pay for an external physical mechanism (such as a tamper-proof contract or escrow service) to bind her future actions before meeting the predictor. Yet if she arrives in the city unbound, she immediately defects. $\mathrm{CDT}$ advises agents to modify their own code to stop using $\mathrm{CDT}$ in the future, yet demands defection in the present (Burgess, 2004; Soares and Fallenstein, 2015).

$\mathrm{P\text{-}FDT}$ dissolves this internal contradiction. A $\mathrm{P\text{-}FDT}$ agent has no need for physical self-binding, contracts, or memory erasing. Because she selects and executes actions strictly as evaluations of an optimal global policy, **she automatically behaves as she would have ideally precommitted to behave**. 

Consequently, $\mathrm{P\text{-}FDT}$ is inherently *reflectively stable*. If given the option to modify its own decision algorithm prior to facing any fair decision dilemma, an agent running Equation (3) will inspect candidate modifications and discover that no alternative architecture outperforms $\mathbf{\Pi}^\star$. It endorses its own code, unifying normative justification with empirical success.

---

## 9. Conclusion

Policy Functional Decision Theory ($\mathrm{P\text{-}FDT}$) represents the natural culmination of the functional decision-theoretic program initiated by Yudkowsky and Soares. By moving the locus of decision-theoretic intervention from the physical act token ($\mathrm{CDT}$), past the observation-conditioned algorithmic output ($\mathrm{A\text{-}FDT}$), and onto the **global policy function**, $\mathrm{P\text{-}FDT}$ provides an uncommonly unified account of instrumental rationality.

Under $\mathrm{P\text{-}FDT}$, rational agency is not conceived as a series of isolated physical impulses reacting to sensory inputs. Rather, rational agency is the execution of a mathematically coherent policy chosen from an updateless, global perspective. It respects nomic and physical causality without being blind to logical dependencies. It secures cooperation in twin prisoner’s dilemmas, fends off extortionists, takes the money in Newcomb’s problem, and escapes Parfit's desert—not by resorting to ad-hoc psychological constraints, but by adhering to a single, mathematically principled rule: **determine which global policy would cause the best universe if universally instantiated, and execute that policy.**

---

## References

- Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
- Arntzenius, F. (2008). No Regrets, or: Edith Piaf Revamps Decision Theory. *Erkenntnis*, 68(2), 277–297.
- Burgess, S. (2004). The Newcomb Problem: An Unqualified Resolution. *Synthese*, 138(2), 261–287.
- Dai, W. (2009). Towards a New Decision Theory. *LessWrong*.
- Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
- Eells, E. (1984). Metatickles and the Dynamics of Deliberation. *Theory and Decision*, 17(1), 71–95.
- Gibbard, A., & Harper, W. L. (1978). Counterfactuals and Two Kinds of Expected Utility. In C. A. Hooker, J. J. Leach, & E. F. McClennen (Eds.), *Foundations and Applications of Decision Theory* (Vol. 1, pp. 125–162). D. Reidel.
- Jeffrey, R. C. (1983). *The Logic of Decision* (2nd ed.). University of Chicago Press.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Joyce, J. M. (2012). Regret and Instability in Causal Decision Theory. *Synthese*, 187(1), 123–145.
- Kleene, S. C. (1938). On Notation for Ordinal Numbers. *Journal of Symbolic Logic*, 3(4), 150–155.
- Lewis, D. (1979). Prisoners' Dilemma is a Newcomb Problem. *Philosophy & Public Affairs*, 8(3), 235–240.
- Lewis, D. (1981). Causal Decision Theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
- Nozick, R. (1969). Newcomb's Problem and Two Principles of Choice. In N. Rescher (Ed.), *Essays in Honor of Carl G. Hempel* (pp. 114–146). D. Reidel.
- Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
- Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
- Skyrms, B. (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
- Soares, N., & Fallenstein, B. (2015). Toward Idealized Decision Theory. *arXiv preprint arXiv:1507.01986*.
- Spohn, W. (1977). Where Luce and Krantz do really generalize Savage's decision model. *Erkenntnis*, 11(1), 113–134.
- Yudkowsky, E. (2010). *Timeless Decision Theory*. Technical Report, The Singularity Institute, San Francisco, CA.
- Yudkowsky, E., & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. *arXiv preprint arXiv:1710.05060v2*.