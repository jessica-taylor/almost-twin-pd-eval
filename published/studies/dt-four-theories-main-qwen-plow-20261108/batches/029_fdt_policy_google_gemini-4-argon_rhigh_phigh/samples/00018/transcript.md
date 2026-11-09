# 029_fdt_policy_google_gemini-4-argon_rhigh_phigh / 00018

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/476a8da9-41e3-49e0-ae11-ed8b53578f07/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/476a8da9-41e3-49e0-ae11-ed8b53578f07/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Policy Functional Decision Theory (P-FDT): Mathematical Foundations, Subjunctive Policies, and Multi-Agent Coordination

## 1. Introduction: From Physical Acts to Mathematical Policies

Normative decision theory turns on a deceptively simple question: when an agent evaluates candidate courses of action, what should she hold fixed about the world, and what should she allow to vary? As James Joyce (1999) famously observed, expected utility theorists share a common account of valuation, because "decision theories should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated." 

For decades, this debate was framed as a binary choice between Evidential Decision Theory (EDT) and Causal Decision Theory (CDT). An EDT agent evaluates an action by Bayesian conditionalization, asking which physical act would provide the best news if she learned she had taken it. A CDT agent evaluates an action by local causal intervention, asking which physical act token would *cause* the best downstream outcome while holding the causal past fixed. Both frameworks suffer from well-known pathologies: EDT "manages the news" in common-cause environments like the Smoking Lesion problem and succumbs to extortion in the XOR Blackmail dilemma, whereas CDT leaves money on the table in Newcomb's problem, defects against psychological twins in the Prisoner's Dilemma, dies in Parfit's desert, and spirals into reflective instability in Death in Damascus.

In *Functional Decision Theory: A New Theory of Instrumental Rationality*, Eliezer Yudkowsky and Nate Soares (2017) propose Functional Decision Theory (FDT) to resolve this impasse. The central philosophical move of FDT is to treat a decision not as a localized physical act token, but as the logical output of a fixed mathematical function—the agent's decision procedure itself. As the authors summarize the principle, a rational agent treats her decision as the output of a fixed mathematical function that answers the question, "Which output of this very function would yield the best outcome?" When other physical systems in the environment—such as psychological twins, game-theoretic counterparts, or accurate predictors—compute or simulate that same decision function, their states *subjunctively depend* on the function's logical output even when they are causally independent of the agent's physical body.

In the main body of their paper, Yudkowsky and Soares formalize an action-selecting version of FDT (which we will refer to as *action-FDT* to keep our terminology exact). Under action-FDT, an agent who has received an observation $x$ intervenes on a logical node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ representing the action output by the algorithm on that specific observation. However, at two crucial points in the footnotes, the authors reveal that action-FDT is actually a pedagogical simplification of a deeper theory—**Policy Functional Decision Theory (P-FDT)**:

> **Footnote 7:** "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

> **Footnote 16:** "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

Because the source text leaves **P-FDT** in these two brief remarks, a reader who wants to apply **P-FDT** to novel problems must reconstruct its formal equations, verify why it agrees with action-FDT on the single-agent dilemmas studied in the paper, and identify why—and where—selecting policies rather than actions makes a decisive difference. In this essay, we develop a complete mathematical account of **P-FDT**, demonstrate its step-by-step application to decision problems, prove when it coincides with or diverges from action-FDT, and resolve the key theoretical ambiguities left open by Footnote 16.

---

## 2. The Formal Architecture of P-FDT

### 2.1 The Expected Utility Backbone and Competing Hypotheticals

Following Yudkowsky and Soares's adaptation of Gibbard and Harper (1978) and Joyce (1999), let $\mathcal{O} = \{o_1, o_2, \dots\}$ be a countable set of outcomes, $\mathcal{A}$ be a finite set of physical actions, and $\mathcal{X}$ be a countable set of possible observation histories (or sensory inputs). Let $\mathcal{U} : \mathcal{O} \to \mathbb{R}$ be a bounded utility function, and define the utility random variable $\textsc{V} \coloneqq \mathcal{U}(\textsc{Outcome})$.

In general expected utility theory, an agent who has observed $x \in \mathcal{X}$ evaluates options via a decision-hypothetical probability function $P(- \hookrightarrow - \,;\, x)$, seeking to maximize

$$\mathcal{EU}(a) \coloneqq \sum_{j} P(a \hookrightarrow o_j \,;\, x) \cdot \mathcal{U}(o_j).$$

Computationally, the agent maintains a world-model $M$ and constructs for each candidate choice a hypothetical object $M^{a \hookrightarrow}$ (or, in **P-FDT**, $M^{\pi \hookrightarrow}$) representing what the universe would look like if that option were chosen. The theories diverge in how $M$ is structured and how hypotheticals are constructed from $M$:

1. **Evidential Decision Theory (EDT):** The world-model is a probability distribution $P$, and hypotheticals are constructed by standard Bayesian conditioning on both the observation $\textsc{Obs} = x$ and the physical action $\textsc{Act} = a$:
   $$\mathrm{EDT}(P, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs} = x, \textsc{Act} = a\right).$$

2. **Causal Decision Theory (CDT):** The world-model is a Pearlian causal model $(P, G)$, where $G$ is a directed acyclic graph (DAG) encoding causal dependencies among variables in $P$. Hypotheticals are formed by conditioning on $\textsc{Obs} = x$ and applying Pearl's $\mathtt{do}$-operator to sever incoming arrows into the physical action node $\textsc{Act}$:
   $$\mathrm{CDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{Act} = a), \textsc{Obs} = x\right).$$

3. **Action-FDT (Standard FDT in Equation 4 of the source):** The world-model is an augmented pair $(P, G)$ where $G$ encodes not only physical causation, but also logical, mathematical, and computational *subjunctive dependencies*. Using Kleene's (1938) second recursion theorem ("quining"), the model contains variables $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ representing the output of the $\mathrm{FDT}$ function on inputs $(P, G, x)$ (where underlines denote dequoting the values of the parameters into the variable's syntactic name). Action-FDT prescribes:
   $$\mathrm{FDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right).$$

### 2.2 Formalizing P-FDT from Footnote 16

Notice a structural quirk in action-FDT's Equation (4). When the agent may receive one of several observations $x \in \mathcal{X}$—such as seeing Box B $\textit{full}$ versus $\textit{empty}$ in the Transparent Newcomb problem—action-FDT places a *separate* logical variable $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ in the graph $G$ for each possible $x \in \mathcal{X}$. When the agent observes $x$, she intervenes only on the node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$, while treating the nodes $\textsc{fdt}(\underline{P}, \underline{G}, \underline{y})$ for all other observations $y \neq x$ as un-intervened random variables governed by her prior distribution $P$.

**P-FDT** eliminates this fragmentation across observation nodes. Following Footnotes 7 and 16, let us define the **policy space** $\Pi$ as the set of all mappings from the observation space $\mathcal{X}$ to the action space $\mathcal{A}$:

$$\Pi \coloneqq \mathcal{A}^{\mathcal{X}} = \{\pi \mid \pi : \mathcal{X} \to \mathcal{A}\}.$$

(When $\mathcal{X}$ and $\mathcal{A}$ are finite, $\Pi$ is a finite set of cardinality $|\mathcal{A}|^{|\mathcal{X}|}$.) In **P-FDT**, the world-model $(P, G)$ contains a single logical root node $\textsc{pfdt}(\underline{P}, \underline{G})$ whose value ranges over policies $\pi \in \Pi$. This node represents the mathematical policy function output by the **P-FDT** algorithm when given the world-model $(P, G)$.

Inside the structural graph $G$, any physical system that implements or predicts the agent's decision procedure—including the agent's own physical action node $\textsc{Act}$ and any predictor's simulation node $\textsc{Prediction}$—is modeled as a structural child of $\textsc{pfdt}(\underline{P}, \underline{G})$:
* The agent's physical action is determined by applying the policy node's output $\pi$ to the realized observation node $\textsc{Obs}$:
  $$\textsc{Act}\big(\textsc{pfdt}(\underline{P}, \underline{G}), \textsc{Obs}\big) = \big[\textsc{pfdt}(\underline{P}, \underline{G})\big](\textsc{Obs}).$$
* A predictor who simulates how the agent responds to one or more candidate observations $x_1, \dots, x_k \in \mathcal{X}$ computes a structural function of $\big(\pi(x_1), \dots, \pi(x_k)\big)$ along with any predictor noise or environmental state variables.

Footnote 16 specifies a two-stage decision procedure for **P-FDT**: the algorithm first "intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions," and then "the agent then applies her inputs in order to select an action." Formally, we write the **P-FDT** policy selector $\mathrm{P\text{-}FDT}_{\Pi}$ and the resulting action prescription $\mathrm{P\text{-}FDT}(P, G, x)$ as follows:

$$\mathrm{P\text{-}FDT}_{\Pi}(P, G) \coloneqq \operatorname*{argmax}_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right), \tag{P-FDT-1}$$

$$\mathrm{P\text{-}FDT}(P, G, x) \coloneqq \big[\mathrm{P\text{-}FDT}_{\Pi}(P, G)\big](x) = \left[\operatorname*{argmax}_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right)\right](x). \tag{P-FDT-2}$$

### 2.3 Updatelessness, Subjunctive Dependence, and Counterpossibilities in P-FDT

Equations (P-FDT-1) and (P-FDT-2) illuminate how **P-FDT** handles dependencies, observations, and counterfactuals:

1. **Intervention on Policy Types vs. Action Tokens:** As Yudkowsky and Soares write, "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." In Peirce's type-token vocabulary, CDT intervenes on the physical token $\textsc{Act} = a$, whereas **P-FDT** intervenes on the mathematical policy type $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$. Because $\mathrm{P\text{-}FDT}_{\Pi}(P, G)$ is a deterministic mathematical function of $(P, G)$, there is only one policy $\pi^*$ it actually outputs in logical reality. Evaluating $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)]$ for $\pi \neq \pi^*$ therefore requires *counterpossible reasoning*—evaluating what the universe would look like if a fixed mathematical function took a different logical output. In Pearl's framework, this counterpossible evaluation is operationalized by graph surgery: setting $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$ and propagating $\pi$ forward along all arrows in $G$.
2. **Global Updatelessness:** Like Wei Dai's (2009) Updateless Decision Theory (UDT), **P-FDT** does *not* condition the prior probability distribution $P$ on $\textsc{Obs} = x$ when evaluating expected utility in (P-FDT-1). Why? Because in environments with predictors (such as the Transparent Newcomb or Mechanical Blackmail problems), *which observation $x$ the agent receives* subjunctively depends on the policy $\pi$ she adopts! If an agent conditioned on $\textsc{Obs} = x$ before choosing her policy, she would treat past predictions that caused her observation $x$ as unchangeable sunk facts, blinding herself to how her policy determines the probability distribution over $\textsc{Obs}$. Instead, **P-FDT** evaluates every policy $\pi$ from the global ex-ante perspective of $P$, and uses the realized observation $x$ solely in Stage 2 (Equation P-FDT-2) as the argument fed into the globally optimal policy $\pi^*$.

---

## 3. Applying P-FDT to Single-Agent Dilemmas

To see how **P-FDT** operates in practice—and why it simplifies and cleans up action-FDT even in single-agent problems—let us apply it step by step to the **Transparent Newcomb Problem** (Drescher 2006; Section 4 and Section 6 of Yudkowsky and Soares), which is decision-theoretically isomorphic to **Parfit's Hitchhiker** and **The Mechanical Blackmail**.

### 3.1 Worked Example: The Transparent Newcomb Problem

Recall the setup: Box A is transparent and contains $\$1{,}000$. Box B is also transparent and contains either $\$1{,}000{,}000$ ($\textit{full}$) or $\$0$ ($\textit{empty}$). A predictor with $99\%$ accuracy placed $\$1{,}000{,}000$ in Box B if and only if she predicted that the agent would leave Box A behind ($\textit{onebox}$) upon seeing Box B $\textit{full}$. The agent looks at Box B, observes $x = \textit{full}$, and must decide between $\textit{onebox}$ ($1\text{B}$) and $\textit{twobox}$ ($2\text{B}$).

To apply **P-FDT**, we specify the spaces, structural graph $G$, and probability distribution $P$:
* **Observation and Action Spaces:** $\mathcal{X} = \{\textit{full}, \textit{empty}\}$ and $\mathcal{A} = \{1\text{B}, 2\text{B}\}$.
* **Policy Space $\Pi$:** There are $|\mathcal{A}|^{|\mathcal{X}|} = 2^2 = 4$ possible policies, which we write as ordered pairs $\pi = (\pi(\textit{full}), \pi(\textit{empty}))$:
  $$\Pi = \big\{\pi_{1,1} = (1\text{B}, 1\text{B}),\; \pi_{1,2} = (1\text{B}, 2\text{B}),\; \pi_{2,1} = (2\text{B}, 1\text{B}),\; \pi_{2,2} = (2\text{B}, 2\text{B})\big\}.$$
* **Structural Graph $G$ and Distribution $P$:**
  * $\textsc{pfdt}(\underline{P}, \underline{G}) \in \Pi$: the logical intervention node.
  * $\textsc{Accurate} \in \{\textit{accurate}, \textit{inaccurate}\}$: an exogenous node with $P(\textsc{Accurate} = \textit{accurate}) = 0.99$ and $P(\textsc{Accurate} = \textit{inaccurate}) = 0.01$.
  * $\textsc{Prediction}(\pi, \textsc{Accurate})$: because the predictor specifically predicts what the agent will do upon seeing Box B $\textit{full}$, $\textsc{Prediction}$ depends on $\pi(\textit{full})$:
    $$\textsc{Prediction}(\pi, \textit{accurate}) = \begin{cases} 1 & \text{if } \pi(\textit{full}) = 1\text{B}, \\ 2 & \text{if } \pi(\textit{full}) = 2\text{B}, \end{cases} \qquad \textsc{Prediction}(\pi, \textit{inaccurate}) = \begin{cases} 2 & \text{if } \pi(\textit{full}) = 1\text{B}, \\ 1 & \text{if } \pi(\textit{full}) = 2\text{B}. \end{cases}$$
  * $\textsc{Box B}(\textsc{Prediction})$: equals $\textit{full}$ if $\textsc{Prediction} = 1$, and $\textit{empty}$ if $\textsc{Prediction} = 2$.
  * $\textsc{Obs}(\textsc{Box B}) = \textsc{Box B}$.
  * $\textsc{Act}(\pi, \textsc{Obs}) = \pi(\textsc{Obs})$.
  * $\textsc{V}(\textsc{Act}, \textsc{Box B}) = \$1{,}000{,}000 \cdot \mathbb{I}(\textsc{Box B} = \textit{full}) + \$1{,}000 \cdot \mathbb{I}(\textsc{Act} = 2\text{B})$.

Now we execute **Stage 1 (Equation P-FDT-1)** by intervening on $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$ for each of the four policies in $\Pi$:

1. **Policy $\pi_{1,2} = (1\text{B}, 2\text{B})$ (One-box if $\textit{full}$, two-box if $\textit{empty}$):**
   Since $\pi_{1,2}(\textit{full}) = 1\text{B}$, with probability $0.99$ ($\textsc{Accurate} = \textit{accurate}$) the predictor predicts $1$, sets $\textsc{Box B} = \textit{full}$, the agent observes $\textit{full}$ and plays $\pi_{1,2}(\textit{full}) = 1\text{B}$, receiving $\$1{,}000{,}000$. With probability $0.01$ ($\textsc{Accurate} = \textit{inaccurate}$), the predictor errs, sets $\textsc{Box B} = \textit{empty}$, and the agent observes $\textit{empty}$ and plays $\pi_{1,2}(\textit{empty}) = 2\text{B}$, receiving $\$1{,}000$. Thus:
   $$\mathbb{E}\big[\textsc{V} \;\big|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{1,2})\big] = 0.99(\$1{,}000{,}000) + 0.01(\$1{,}000) = \$990{,}010.$$

2. **Policy $\pi_{1,1} = (1\text{B}, 1\text{B})$ (Always one-box):**
   $$\mathbb{E}\big[\textsc{V} \;\big|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{1,1})\big] = 0.99(\$1{,}000{,}000) + 0.01(\$0) = \$990{,}000.$$

3. **Policy $\pi_{2,2} = (2\text{B}, 2\text{B})$ (Always two-box):**
   Since $\pi_{2,2}(\textit{full}) = 2\text{B}$, Box B is $\textit{full}$ only when the predictor errs (probability $0.01$), yielding $\$1{,}001{,}000$, and is $\textit{empty}$ with probability $0.99$, yielding $\$1{,}000$:
   $$\mathbb{E}\big[\textsc{V} \;\big|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{2,2})\big] = 0.01(\$1{,}001{,}000) + 0.99(\$1{,}000) = \$11{,}000.$$

4. **Policy $\pi_{2,1} = (2\text{B}, 1\text{B})$ (Two-box if $\textit{full}$, one-box if $\textit{empty}$):**
   $$\mathbb{E}\big[\textsc{V} \;\big|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{2,1})\big] = 0.01(\$1{,}001{,}000) + 0.99(\$0) = \$10{,}010.$$

Comparing the four values, the unique optimal policy is $\pi^* = \pi_{1,2} = (1\text{B}, 2\text{B})$. In **Stage 2 (Equation P-FDT-2)**, the agent applies $\pi^*$ to her actual observation $x = \textit{full}$:

$$\mathrm{P\text{-}FDT}(P, G, \textit{full}) = \pi_{1,2}(\textit{full}) = 1\text{B}.$$

Even while staring directly at $\$1{,}000{,}000$ in transparent Box B, the **P-FDT** agent leaves Box A's $\$1{,}000$ behind—and if the predictor ever makes the $1\%$ error of leaving Box B empty, $\mathrm{P\text{-}FDT}(P, G, \textit{empty}) = \pi_{1,2}(\textit{empty}) = 2\text{B}$ immediately prescribes taking the $\$1{,}000$.

### 3.2 Why Action-FDT and P-FDT Agree in Single-Agent Benchmark Problems

Compare our **P-FDT** calculation above with Yudkowsky and Soares's action-FDT calculation in Section 6 of the reference paper. In action-FDT, when Fiona observes $\textit{full}$, she intervenes only on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full})$, and must introduce an arbitrary prior probability $q = P^F(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty}) = 2\text{B})$ for what she would do if the box were empty, yielding $\$990{,}000 + 0.01q \cdot \$1{,}000$ for one-boxing versus $\$10{,}010 + 0.99q \cdot \$1{,}000$ for two-boxing.

Why didn't the nuisance parameter $q$ change Fiona's decision in action-FDT, and why does **P-FDT** yield the exact same prescription across every dilemma in the reference paper? We can state the exact mathematical condition as a proposition (our formalization of the equivalence noted in Footnotes 7 and 16):

> **Proposition 1 (Equivalence under Branch-Additive Separability).** *Suppose that in a decision problem $(P, G)$ with observation space $\mathcal{X}$, the expected utility under a policy intervention $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$ is additively separable across observations—that is, there exist functions $U_x : \mathcal{A} \to \mathbb{R}$ for each $x \in \mathcal{X}$ such that*
> $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right] = \sum_{x \in \mathcal{X}} U_x\big(\pi(x)\big).$$
> *Then joint optimization over policies $\pi \in \mathcal{A}^{\mathcal{X}}$ decomposes into independent pointwise optimizations over actions $\pi(x) \in \mathcal{A}$ for each $x \in \mathcal{X}$:*
> $$\max_{\pi \in \mathcal{A}^{\mathcal{X}}} \sum_{x \in \mathcal{X}} U_x\big(\pi(x)\big) = \sum_{x \in \mathcal{X}} \max_{a_x \in \mathcal{A}} U_x(a_x).$$
> *Consequently, $\mathrm{P\text{-}FDT}(P, G, x) = \mathrm{FDT}(P, G, x)$ for every $x \in \mathcal{X}$, provided only that in action-FDT's model, each node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ is wired to the events controlled by $\pi(x)$.*

In Transparent Newcomb, the expected utility of any policy $\pi$ is

$$\mathbb{E}\big[\textsc{V} \;\big|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)\big] = U_{\textit{full}}\big(\pi(\textit{full})\big) + U_{\textit{empty}}\big(\pi(\textit{empty})\big),$$

where $U_{\textit{full}}(1\text{B}) = \$990{,}000$, $U_{\textit{full}}(2\text{B}) = \$10{,}010$, $U_{\textit{empty}}(2\text{B}) = p_{\textit{empty}} \cdot \$1{,}000$, and $U_{\textit{empty}}(1\text{B}) = \$0$. Wait—notice that in Transparent Newcomb, the probability $p_{\textit{empty}}$ of seeing an empty box ($0.01$ vs. $0.99$) actually depends on $\pi(\textit{full})$! Even so, for *every* fixed choice of $\pi(\textit{full})$, $U_{\textit{empty}}(a)$ is monotonically maximized by $\pi(\textit{empty}) = 2\text{B}$, and in action-FDT, holding $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty})$ fixed at a prior $q \in [0, 1]$ merely replaces the second term with a constant expectation $p_{\textit{empty}}(\pi(\textit{full})) \cdot q \cdot \$1{,}000$ whose variation (at most $\$980$) is swamped by the $\$979{,}990$ gap in $U_{\textit{full}}$. **P-FDT** is cleaner than action-FDT here because it never needs to posit an unexamined prior $q$ over its own off-branch behavior; it optimizes $\pi(\textit{full}) = 1\text{B}$ and $\pi(\textit{empty}) = 2\text{B}$ simultaneously.

---

## 4. Where P-FDT Diverges from Action-FDT: Multi-Agent and Cross-Branch Dilemmas

Why, then, do Yudkowsky and Soares emphasize in Footnote 16 that choosing a policy rather than an action "matters in multi-agent dilemmas"?

The key lies in what happens when two or more copies of an agent (such as psychological twins, symmetric coalition members, or distributed AI instances sharing the same source code and prior model $(P, G)$) receive *different* observations $x_1 \neq x_2$ in the same strategic interaction. Under action-FDT (Equation 4), an agent who observes $x_1$ intervenes *only* on the node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_1})$, leaving the node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_2})$ untouched as an independent root variable in $G$. In effect, when two twins receive different observations $x_1 \neq x_2$, **action-FDT treats its own twin in the other observation branch the same way CDT treats a twin in another room**: as an exogenous process whose action is held fixed at a prior probability $q$ during the $\mathtt{do}$-intervention!

Let us demonstrate this divergence with two concrete mathematical examples—first in a multi-agent twin dilemma (confirming Footnote 16), and second in a single-agent dilemma with a cross-branch predictor (extending Footnote 16).

### 4.1 Multi-Agent Divergence: The Asymmetric-Observation Twin Prisoner's Dilemma and Stag Hunt

Consider an **Asymmetric-Observation Twin Prisoner's Dilemma**. An agent and her psychological twin share the exact same decision algorithm and prior world-model $(P, G)$. Nature flips a fair coin to place one twin in Room A (where the door sign reads $\textsc{Obs} = A$) and the other twin in Room B (where the door sign reads $\textsc{Obs} = B$). Thus, from the perspective of the prior $P$, the agent has probability $0.5$ of observing $x = A$ (with her twin observing $B$) and probability $0.5$ of observing $x = B$ (with her twin observing $A$).

Each twin must choose either $\textit{Cooperate}$ ($C$) or $\textit{Defect}$ ($D$). Consider a standard Prisoner's Dilemma payoff matrix $(T > R > P_0 > S)$ where mutual cooperation pays $R = \$1{,}000{,}000$, unilateral defection pays the defector $T = \$1{,}001{,}000$ and the cooperator $S = \$0$, and mutual defection pays each twin $P_0 = \$600{,}000$. Notice that $D$ strictly dominates $C$ causally ($T > R$ and $P_0 > S$), while mutual cooperation $(C, C)$ strictly Pareto-dominates mutual defection $(D, D)$ ($\$1{,}000{,}000 > \$600{,}000$). Moreover, because unilateral defection destroys the cooperative surplus ($T + S = \$1{,}001{,}000 < 2 P_0 = \$1{,}200{,}000$), the payoffs interact non-additively across the two rooms.

Now suppose our agent enters her room and observes $x = A$. How do **action-FDT** and **P-FDT** evaluate the decision?

#### Case 1: Action-FDT (Equation 4)
In action-FDT, the graph $G$ contains two distinct logical root nodes: $F_A = \textsc{fdt}(\underline{P}, \underline{G}, A)$ (governing whichever twin is in Room A) and $F_B = \textsc{fdt}(\underline{P}, \underline{G}, B)$ (governing whichever twin is in Room B). Having observed $x = A$, the agent intervenes *only* on $F_A$, holding fixed her prior probability $q \coloneqq P(F_B = C)$ that the Room B node outputs $C$:

* **If she intervenes with $\mathtt{do}(F_A = C)$:**
  With probability $0.5$ she is in Room A (playing $C$ against $F_B$), earning $q R + (1-q)S$. With probability $0.5$ she is in Room B (playing $F_B$ against her twin's $F_A = C$), earning $q R + (1-q)T$. Her expected utility is:
  $$\mathbb{E}\big[\textsc{V} \;\big|\; \mathtt{do}(F_A = C)\big] = q R + \frac{1-q}{2}(S + T) = \$1{,}000{,}000 q + \$500{,}500(1 - q) = \$500{,}500 + \$499{,}500 q.$$

* **If she intervenes with $\mathtt{do}(F_A = D)$:**
  With probability $0.5$ she is in Room A (playing $D$ against $F_B$), earning $q T + (1-q)P_0$. With probability $0.5$ she is in Room B (playing $F_B$ against her twin's $F_A = D$), earning $q S + (1-q)P_0$. Her expected utility is:
  $$\mathbb{E}\big[\textsc{V} \;\big|\; \mathtt{do}(F_A = D)\big] = \frac{q}{2}(T + S) + (1-q)P_0 = \$500{,}500 q + \$600{,}000(1 - q) = \$600{,}000 - \$99{,}500 q.$$

Compare the two expressions! Whenever $q < \frac{99{,}500}{599{,}000} \approx 0.166$, **action-FDT strictly prefers $\mathtt{do}(F_A = D)$**. Worse still, if both twins start with the pessimistic belief $q = 0$ (expecting the other room's node to defect), then $\mathrm{FDT}(P, G, A) = D$ and $\mathrm{FDT}(P, G, B) = D$. Mutual defection $(D, D)$ is completely self-confirming for action-FDT, trapping the twins at $\$600{,}000$ each! The exact same failure occurs in a **Two-Room Twin Stag Hunt** (or the 10-voter election coalition in Section 10 of the paper if each voter observes a distinct voter ID $x_i \in \{1, \dots, 10\}$): if paying $\$1{,}000$ to vote yields $\$1{,}000{,}000$ if and only if all 10 voters vote, an action-FDT agent who intervenes only on her own observation node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_i})$ while holding $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_j})$ fixed at $q = 0$ sees zero chance of swinging the election and stays home.

#### Case 2: P-FDT (Equations P-FDT-1 and P-FDT-2)
Now let us apply **P-FDT** to the exact same Asymmetric-Observation Twin Prisoner's Dilemma. Under **P-FDT**, there is only *one* logical intervention node in $G$, $\textsc{pfdt}(\underline{P}, \underline{G})$, which outputs a policy $\pi : \{A, B\} \to \{C, D\}$ shared by both twins. The agent iterates over all four policies in $\Pi = \{\pi_{CC}, \pi_{CD}, \pi_{DC}, \pi_{DD}\}$:

$$\mathbb{E}\big[\textsc{V} \;\big|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{CC})\big] = 0.5 R + 0.5 R = \$1{,}000{,}000,$$
$$\mathbb{E}\big[\textsc{V} \;\big|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{DD})\big] = 0.5 P_0 + 0.5 P_0 = \$600{,}000,$$
$$\mathbb{E}\big[\textsc{V} \;\big|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{CD})\big] = 0.5 S + 0.5 T = \$500{,}500,$$
$$\mathbb{E}\big[\textsc{V} \;\big|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{DC})\big] = 0.5 T + 0.5 S = \$500{,}500.$$

Regardless of any prior beliefs, $\mathrm{P\text{-}FDT}_{\Pi}(P, G)$ uniquely selects $\pi^* = \pi_{CC}$. Upon observing $x = A$, the agent executes $\pi^*(A) = C$; her twin in Room B executes $\pi^*(B) = C$; and both walk away with $\$1{,}000{,}000$. By intervening at the level of the *policy* mapping observations to actions, **P-FDT** preserves subjunctive coordination across distinct observation branches.

| Decision Theory | Intervention Target | Value of $\textsc{Obs} = B$ Behavior When $\textsc{Obs} = A$ | Prescription in Asymmetric Twin PD (with $q < 0.166$) | Outcome Achieved |
| :--- | :--- | :--- | :--- | :--- |
| **CDT** | Physical act $\textsc{Act} = a$ | Held fixed at conditional $P(\textsc{Act}_B \mid \textsc{Obs}=A)$ | Defect ($D$) | $\$600{,}000$ |
| **Action-FDT** | Action node $\textsc{fdt}(\underline{P}, \underline{G}, A) = a$ | Held fixed at prior $q = P(\textsc{fdt}(\underline{P}, \underline{G}, B) = C)$ | Defect ($D$) | $\$600{,}000$ |
| **P-FDT** | Policy node $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$ | Jointly optimized via $\pi = (\pi(A), \pi(B)) \in \Pi$ | Cooperate ($\pi_{CC}(A) = C$) | $\$1{,}000{,}000$ |

### 4.2 Extending Footnote 16: Single-Agent Dilemmas with Cross-Branch Predictors

Footnote 16 remarks that the difference between **P-FDT** and action-FDT "only matters in multi-agent dilemmas so far as we can tell." Armed with Proposition 1, however, we can see that this claim requires a slight mathematical refinement (an analytical finding of our own beyond the source text): **P-FDT** also outperforms action-FDT in *single-agent* dilemmas whenever a predictor simulates the agent across *multiple* possible observations before acting.

Suppose a single agent faces **The Consistency Predictor Dilemma**: a predictor flips a fair coin $C \in \{\textit{heads}, \textit{tails}\}$ to show the agent either a green lamp ($x = \textit{green}$) or a red lamp ($x = \textit{red}$). The agent can either press a button to take a free $\$1{,}000$ ($2\text{B}$) or refrain ($1\text{B}$). However, the predictor simulates the agent under *both* lamp colors before flipping the coin, and places $\$1{,}000{,}000$ in the agent's bank account if and only if she predicts that the agent will refrain under *both* observations ($\pi(\textit{green}) = 1\text{B} \land \pi(\textit{red}) = 1\text{B}$).

Here there is only one physical agent, yet the predictor's mental simulation couples the $\textit{green}$ and $\textit{red}$ observation branches:
* Under **action-FDT**, if the agent starts with prior $q = P(\textsc{fdt}(\underline{P}, \underline{G}, \textit{red}) = 1\text{B}) = 0$ and observes $x = \textit{green}$, intervening on $\textsc{fdt}(\underline{P}, \underline{G}, \textit{green}) = 1\text{B}$ yields $\$0$ (since the $\textit{red}$ node is held fixed at $2\text{B}$), whereas taking the $\$1{,}000$ ($2\text{B}$) yields $\$500$ in ex-ante expectation. Action-FDT two-boxes under both lamp colors and gets $\$1{,}000$.
* Under **P-FDT**, intervening on $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{1,1} = (1\text{B}, 1\text{B})$ simultaneously updates the predictor's simulation of both branches, yielding $\$1{,}000{,}000 - \$0 = \$1{,}000{,}000$ (compared to $\$1{,}000$ for $\pi_{2,2}$ and $\$500$ for $\pi_{1,2}$ or $\pi_{2,1}$). **P-FDT** selects $\pi_{1,1}$ and secures the $\$1{,}000{,}000$.

Thus, what truly separates **P-FDT** from action-FDT is whether the environment exhibits *cross-branch subjunctive coupling*—whether through multiple physical agents receiving different observations, or a single predictor inspecting multiple counterfactual branches of the agent's policy.

---

## 5. Unresolved Questions in Footnote 16 and Operational Proposals

Because Yudkowsky and Soares introduce **P-FDT** only in Footnotes 7 and 16, three important foundational questions remain open for anyone implementing the theory. Below, we identify these ambiguities and propose precise operational solutions.

### 5.1 What Counts as an "Input" to the Policy: Observations $\mathcal{X}$ or Full Models $(P, G, x)$?

Look closely at the wording of the two footnotes:
* Footnote 7 defines policies as "mappings from observations to actions" ($\pi : \mathcal{X} \to \mathcal{A}$).
* Footnote 16 says that **P-FDT** "intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action."

In Equation (4) of the source paper, the algorithm $\mathrm{FDT}(P, G, x)$ takes *three* inputs: the probability distribution $P$, the dependency graph $G$, and the observation $x$. Moreover, in the **Smoking Lesion Problem** (Section 6, Figure 4), Fiona makes no sensory observation $x$ at all. Instead, whether she has the lesion determines whether her preferences are governed by utility function $\mathcal{U}_S$ (yielding distribution $P_S^F$) or $\mathcal{U}_R$ (yielding distribution $P_R^F$). In the source paper, Fiona's graph $G^F$ contains two distinct nodes: $\textsc{fdt}(\underline{P_S^F}, \underline{G^F})$ and $\textsc{fdt}(\underline{P_R^F}, \underline{G^F})$.

This raises an immediate question: in **P-FDT**, should the policy $\pi$ map only sensory observations $x \in \mathcal{X}$ to actions (keeping $\underline{P}$ and $\underline{G}$ fixed inside the node name $\textsc{pfdt}(\underline{P}, \underline{G})$), or should $\pi$ map the entire input tuple $(P', G', x)$ to actions via a universal node $\textsc{pfdt}$?

**Operational Proposal:** We propose that the domain of $\pi$ must be restricted to **epistemic observations/signals $\mathcal{X}$ sharing a common ex-ante evaluative model $(P, G)$**, so that the intervention node is $\textsc{pfdt}(\underline{P}, \underline{G})$ and $\pi : \mathcal{X} \to \mathcal{A}$. Why? Suppose an agent in the Smoking Lesion problem intervened on a single universal node $\textsc{pfdt}$ to choose a mapping $\pi : \{P_S^F, P_R^F\} \to \{\textit{smoke}, \textit{refrain}\}$, and evaluated that mapping using her actual utility function $\mathcal{U}_S$ (which values smoking at $+\$1{,}000$ in *both* branches). Then under $\mathcal{U}_S$, she would choose the constant policy $\pi(P_S^F) = \textit{smoke}$ and $\pi(P_R^F) = \textit{smoke}$—incorrectly hallucinating that her non-lesion self ($P_R^F$, who actually dislikes smoking at $-\$1$) would also smoke! Keeping $(\underline{P}, \underline{G})$ fixed in the node identifier $\textsc{pfdt}(\underline{P}, \underline{G})$ while letting $\pi : \mathcal{X} \to \mathcal{A}$ range over sensory observations properly separates indexical information ($x \in \mathcal{X}$) from differences in terminal preferences ($\mathcal{U}_S$ vs. $\mathcal{U}_R$). (If two agents have different beliefs strictly because they observed different data streams $x_1, x_2 \in \mathcal{X}$ starting from a shared prior $P$, those differences belong in $\mathcal{X}$ so that $\textsc{pfdt}(\underline{P}, \underline{G})$ unifies them.)

### 5.2 Tie-Breaking on Zero-Probability Observation Branches

A second subtle issue arises when a predictor is **infallible** ($\textsc{Accurate} = \textit{accurate}$ with probability $1$), as Yudkowsky and Soares assume in their formalization of the **XOR Blackmail** problem (Section 7, Footnote 13).

Suppose we run **P-FDT** on the Transparent Newcomb problem with an *infallible* predictor ($P(\textsc{Accurate} = \textit{accurate}) = 1$). Re-evaluating our four policies from Section 3.1 with error probability $\varepsilon = 0$:
* $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{1,2})] = 1.0(\$1{,}000{,}000) + 0.0(\$1{,}000) = \$1{,}000{,}000$.
* $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{1,1})] = 1.0(\$1{,}000{,}000) + 0.0(\$0) = \$1{,}000{,}000$.
* $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{2,2})] = \$1{,}000$.
* $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{2,1})] = \$0$.

Notice that $\pi_{1,2}$ and $\pi_{1,1}$ **tie** at $\$1{,}000{,}000$! Because setting $\pi(\textit{full}) = 1\text{B}$ drives the probability of observing $\textsc{Obs} = \textit{empty}$ to $0$, the global expectation in (P-FDT-1) becomes completely insensitive to $\pi(\textit{empty})$. This is the decision-theoretic analogue of a Nash equilibrium failing to constrain behavior in unreached off-equilibrium subgames. What if, in a variant problem, the observation $x_0$ actually observed by the agent happens to lie on a zero-probability branch of an optimal policy?

**Operational Proposal (Trembling-Hand Policy Refinement):** To make **P-FDT** well-defined on every observation $x \in \mathcal{X}$ even when predictors are idealized as infallible, we can adopt a Selten-style *trembling-hand refinement* (or, equivalently, require non-dogmatic priors where environmental/prediction noise $\varepsilon > 0$ has full support over $\mathcal{X}$, and take the limit as $\varepsilon \downarrow 0^+$):

$$\mathrm{P\text{-}FDT}_{\Pi}^*(P, G) \coloneqq \lim_{\varepsilon \downarrow 0^+} \operatorname*{argmax}_{\pi \in \Pi} \mathbb{E}_{P_\varepsilon}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right),$$

where $P_\varepsilon$ perturbs deterministic observation gates with independent full-support noise of magnitude $\varepsilon$. As our $99\%$-accuracy calculation in Section 3.1 showed, any $\varepsilon > 0$ immediately breaks the tie in favor of $\pi_{1,2} = (1\text{B}, 2\text{B})$.

### 5.3 Computational Scaling and Subjunctive Graph Discovery

Finally, moving from action-FDT to **P-FDT** highlights two open problems noted by Yudkowsky and Soares:
1. **Combinatorial Complexity of Policy Iteration:** Whereas action-FDT maximizes over $|\mathcal{A}|$ actions for the single realized observation $x$, **P-FDT** maximizes over $|\mathcal{A}|^{|\mathcal{X}|}$ policies. For large observation spaces $\mathcal{X}$, exhaustive enumeration of $\Pi$ is intractable. However, Proposition 1 gives us an immediate algorithmic remedy: we can decompose $\mathcal{X}$ into connected components of *cross-branch subjunctive coupling* in $G$. For any subset of observations $\mathcal{X}_0 \subseteq \mathcal{X}$ whose downstream paths in $G$ do not jointly feed into any predictor or multi-agent payoff node, $\pi(x)$ can be optimized pointwise in $O(|\mathcal{A}|)$ time, reserving joint policy search for the small equivalence classes of observations that genuinely interact.
2. **Learning the Subjunctive Graph $G$:** Just as action-FDT assumes $G$ is given as input, **P-FDT** relies on $G$ to specify which environmental processes compute or simulate $\textsc{pfdt}(\underline{P}, \underline{G})$. Developing a formal theory of how bounded agents learn logical and computational dependency graphs from observation remains, as the authors note, the central open problem of functional decision theory.

---

## 6. Conclusion

**Policy Functional Decision Theory (P-FDT)** represents the most unified formulation of the functional decision-theoretic program. By intervening on a single logical node $\textsc{pfdt}(\underline{P}, \underline{G})$ to select a policy $\pi : \mathcal{X} \to \mathcal{A}$ and then evaluating $\pi(x)$ at the realized observation $x$, **P-FDT** retains every advantage of action-FDT on classic single-agent problems—one-boxing in Newcomb's and Transparent Newcomb's problems, smoking in the Smoking Lesion problem, paying the driver in Parfit's Hitchhiker, and resisting extortion in XOR and Mechanical Blackmail—while eliminating ungrounded prior parameters over off-branch actions. More importantly, when multiple agents or cross-branch predictors couple distinct observations together, **P-FDT** succeeds where action-FDT falters, enabling symmetric agents with heterogeneous observations to achieve optimal coordination without precommitment.

## References

* Dai, Wei. 2009. "Towards a New Decision Theory." *Less Wrong*, August 13, 2009.
* Drescher, Gary L. 2006. *Good and Real: Demystifying Paradoxes from Physics to Ethics*. Cambridge, MA: MIT Press.
* Gibbard, Allan, and William L. Harper. 1978. "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, vol. 1, edited by C. A. Hooker, J. J. Leach, and E. F. McClennen. Boston: D. Reidel.
* Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. New York: Cambridge University Press.
* Kleene, Stephen Cole. 1938. "On Notation for Ordinal Numbers." *Journal of Symbolic Logic* 3 (4): 150–155.
* Lewis, David. 1979. "Prisoners' Dilemma is a Newcomb Problem." *Philosophy & Public Affairs* 8 (3): 235–240.
* Nozick, Robert. 1969. "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel*, edited by Nicholas Rescher, 114–146. Dordrecht: D. Reidel.
* Parfit, Derek. 1986. *Reasons and Persons*. New York: Oxford University Press.
* Pearl, Judea. 2000. *Causality: Models, Reasoning, and Inference*. New York: Cambridge University Press.
* Skyrms, Brian. 1980. *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. New Haven, CT: Yale University Press.
* Soares, Nate, and Benja Fallenstein. 2015. "Toward Idealized Decision Theory." arXiv:1507.01986 [cs.AI].
* Yudkowsky, Eliezer. 2010. *Timeless Decision Theory*. The Singularity Institute, San Francisco, CA.
* Yudkowsky, Eliezer, and Nate Soares. 2017. "Functional Decision Theory: A New Theory of Instrumental Rationality." Machine Intelligence Research Institute, arXiv:1710.05060v2.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Narrative Voice**

I'm now focusing on defining the narrative voice for the essay. I want to convey my researcher perspective effectively and ensure the tone aligns with the target audience. Currently, I'm exploring different personas and considering the level of detail appropriate for an expert readership.


**Clarifying P-FDT Details**

I'm now diving deep into P-FDT, concentrating on the policy-selection passage within Yudkowsky and Soares's paper. My goal is to delineate it, clarify the mathematical procedure, and explain its motivations relative to EDT, CDT, and other forms of FDT. I'm focusing on its treatment of dependencies, counterfactuals, and any open questions left in the source document.


**Analyzing FDT Formalization**

I'm now zeroing in on the formalization of FDT, particularly as presented in the source material. I've taken note of updatelessness, which changes intervention targets. I'm also examining the iterative process over *policies* instead of actions as emphasized in the footnotes. I'm noting this distinction's impact in multi-agent dilemmas, and I want to better grasp the ramifications of the iterative nature.


**Simplifying FDT Exposition**

I'm now simplifying FDT's exposition, setting aside certain distinctions for clarity. Specifically, I'm noting how standard FDT handles observations via separate nodes in the graph, as seen in the Transparent Newcomb problem and XOR/Mechanical Blackmail. I'm focusing on the value of one branch being treated as a separate random variable in *P* with some prior probability *q*, which becomes problematic.


**Dissecting Policy-FDT Implications**

I'm now deeply engaged with P-FDT. I've realized $q$ drops out during action comparisons at the observed branch, revealing its implications. I'm focusing on the contrast with standard FDT in coupled-observation and multi-agent scenarios. The agent intervenes on a policy, simultaneously affecting counterfactual outcomes across all observations. This contrasts with action-FDT's treatment of its own behavior as fixed during optimization.


**Elaborating Policy Formalization**

I'm presently formalizing P-FDT further, based on the footnote's suggestion. I'm building on the idea that agents iterate over policies, not individual actions, which impacts certain multi-agent dilemmas. Currently, I'm examining how this policy-based intervention is formalized and its implications for the graphical structure.


**Formalizing P-FDT Structure**

I'm now focusing on how P-FDT functions, specifically examining its underlying structure. I've realized we can model this without needing separate intervention nodes for each potential observation. Instead, there's a single logical node that outputs the policy. I'm noting the policy selection rule and action execution, where the action is the result of the policy applied to the observed input.


**Evaluating P-FDT Cases**

I'm presently evaluating P-FDT in benchmark cases, specifically *Transparent Newcomb* and *Mechanical Blackmail*. I'm demonstrating how P-FDT evaluates policies, ensuring linear decomposition across observation branches. Optimizing jointly allows me to address the nuisance parameter, $q$, while yielding the same action at $x = \textit{full}$ as action-FDT. I'm focusing on the divergence from action-FDT and the implications of Footnote 16, particularly regarding what constitutes input vs. a fixed parameter.


**Clarifying Input Ambiguity**

I'm now grappling with the Smoking Lesion scenario and a significant ambiguity. Does the "input" to the P-FDT policy include just the observation $x$, or the agent's model itself, encompassing both probability $P$ and utility $G$? I can analyze both interpretations. I'm building a formal mathematical example to show how P-FDT diverges from action-FDT in multi-agent dilemmas.


**Analyzing Twin Coordination**

I'm now analyzing a multi-agent scenario with twin agents and asymmetric observations. Currently, I'm examining how standard action-FDT handles this. When one twin observes $x=\textit{left}$, the intervention targets $a$ while the prior is held fixed. This highlights a critical question: how do their non-additive, joint payoffs affect the decision?


**Verifying Action-FDT Behavior**

I'm now verifying the behavior of action-FDT in a twin scenario with asymmetric observations. It appears that when one twin observes "left", they view the other twin, who sees "right", as an independent causal node, similar to how a CDT agent would treat a twin in the Twin Prisoner's Dilemma. I'm confirming this by examining Equation (4) and the distinct root nodes in G^F, as illustrated in other examples.


**Modeling Exogenous Variables**

I'm now modeling exogenous variables in a twin prisoner's dilemma, focusing on an asymmetric observation scenario. Action-FDT, upon observing *x = 1*, seems to intervene solely on its own action, treating the other twin's observation as fixed. This leads me to question the implications of non-additive, joint payoffs. I'm noting the implications of a separate root node.


**Revising Utility Functions**

I'm now revising the utility functions in the Cross-Branch Twin PD. Focusing on how the payoff structure changes depending on the observation and actions, I'm examining how to calculate an agent's expected utility when they're uncertain about their initial room. This involves defining the utility $u(a_i, a_j)$ and the calculation of $V$ for each room. I'm carefully reviewing the payoffs in each state.


**Refining Agent Utility**

I'm now refining the agent's utility function within the Cross-Branch Twin PD framework. I'm focusing on why an agent's expected utility, in Equation (4), is not conditioned on her observation, given the model is supposed to be updateless. Further, I'm clarifying that the utility is strictly based on the agent's own money in a room, regardless of other agent's rooms, thus removing any cross-branch dependency from the state space.


**Examining FDT Paradoxes**

I'm currently examining a paradox within action-FDT involving twin agents and asymmetric observations. If I'm in room C=1, action-FDT seems to control both my action and my twin's action when C=2. This leads to unexpected utility calculations. I'm investigating why and how the causal structure is misapplied in this scenario, especially as applied to Equation (4).


**Modeling Coordination Payoffs**

I'm now modeling coordination payoffs in a symmetric twin setup to test action-FDT. I'm focusing on known, asymmetric roles and how joint payoff requirements influence the decision process. Specifically, I'm analyzing a "Two-Room Twin Stag Hunt" scenario to understand the payoff calculations.


**Comparing FDT Formalisms**

I'm now comparing action-FDT (Eq. 4) and P-FDT (Footnote 16) in a "Two-Room Twin Stag Hunt." Under action-FDT, observing $x=1$ leads to intervention on $F_1 = a_1$, fixing the prior belief *q*. Doing $F_1 = W$ yields a payoff dependent on $q$. However, I'm noting the project only succeeds when both choose *W*. The implications of updatelessness versus policy-based intervention are becoming clearer.


**Analyzing Action-FDT Behavior**

I'm currently focusing on a critical aspect of the Two-Room Twin Stag Hunt.  My analysis of action-FDT shows that a pessimistic belief ($q = 0$) results in an agent shirking, leading to a reflectively consistent Nash equilibrium. I'm noting this surprising outcome and its implications for multi-agent settings, especially when considering the interaction of payoffs across branches and the contrast with P-FDT.


**Clarifying P-FDT Success**

I've realized P-FDT's key advantage in the Two-Room Twin Stag Hunt. Intervention targets the policy itself, *simultaneously* setting both actions to $W$ regardless of prior beliefs or individual branches, yielding a clear payoff. This highlights P-FDT's ability to coordinate despite asymmetric observations. I'm focusing on why prior beliefs don't affect this outcome.


**Verifying P-FDT Benefits**

I'm now verifying P-FDT's advantages by analyzing an example of asymmetric twin coordination, that is mathematically similar to section 10 and 6/7. It's crystal clear that P-FDT overcomes prior belief dependencies. I'm carefully re-reading footnotes 7 and 16, to confirm.


**Evaluating Exposition Nuances**

I'm now clarifying the authors' statement, "The difference only matters in multi-agent dilemmas so far as we can tell." My current focus is how this relates to single-agent scenarios, specifically examining cases where a predictor *does* consider multiple observation branches, or perhaps considers them when there is no predictor at all. I am now exploring if the underlying single-agent problem, without a simulator, still allows the same solution when the predictor *does* depend on multiple observation branches.



**Proving Policy Separability**

I'm now focused on proving the additively separable nature of P-FDT across observation branches, a key equivalence with action-FDT when it holds. I'm formulating a mathematical proposition to demonstrate the conditions under which P-FDT can be decomposed into independent maximizations for each observation, ensuring P-FDT and action-FDT give identical results. This will help understand when action-FDT falls short in multi-agent settings with differing observations.


**Examining Predictor Dependence**

I'm now zeroing in on cases with single agents, examining the authors' statement in Footnote 16 more precisely. I'm noting how the predictor's action can rely on simulations of multiple observations, even in a single-agent scenario. I'm also finding this breaks the additive separability, challenging the prior belief about the importance of multi-agent settings.


**Defining Policy Domains**

I'm now examining the policy domain in P-FDT more closely, specifically the scope of "inputs" versus "observations." I'm reviewing Footnotes 7 and 16, and trying to reconcile their definitions. I'm noting the apparent ambiguity in the "Smoking Lesion" scenario where an agent faces uncertainty about their world-model without a direct observation. This ambiguity highlights the differing viewpoints on the intervention node's inputs.


**Interpreting Policy Node Inputs**

I'm currently trying to better interpret what the policy node *actually* takes as input, especially for P-FDT. I'm noting how the interpretation of "input" can vary. It can range from just an observation *x* to the entire world-model. I am focusing on reconciling these interpretations, particularly in the context of single-agent scenarios and how it influences the expectation calculation with the formalization and the Observation-Policy Interpretation.


**Interpreting Policy Node Inputs**

I'm working on a clearer understanding of what a policy node means. I'm focusing on the epistemic-state interpretation and figuring out how to operationalize it. I am also investigating the impact on null-branch scenarios, especially with infallible predictors, as in Mechanical Blackmail, Transparent Newcomb, or XOR Blackmail. I'm noting the zero-probability observations.


**Addressing Zero-Probability Branches**

I'm now grappling with zero-probability observation branches within P-FDT. I've realized that in scenarios like Transparent Newcomb, multiple policies, such as "onebox/twobox" and "onebox/onebox", yield identical expected utilities. I need to figure out how to handle the off-equilibrium behavior and what should happen if we can observe a null branch, especially in cases where the predictor *does* depend on this branch. I'm noting the analogy to equilibrium refinements in game theory to provide an answer.


**Clarifying Sequential Observations**

I'm now investigating sequential observation scenarios within P-FDT. I'm focusing on whether P-FDT remains dynamically consistent across time when applied to multi-stage decision problems, and whether the optimal policy $\pi^*$ is invariant across different observation histories, since the agent is updateless. I'm exploring the implications of this for practical applications.


**Confirming Dynamic Consistency**

I'm now investigating P-FDT's dynamic consistency across sequential observations. I'm focusing on whether this approach guarantees updatelessness across time. The analysis focuses on practical applications to multi-stage decision problems, and the impact the optimal policy is invariant to different observation histories. I'm focusing on how P-FDT can guarantee dynamic consistency.


**Formalizing P-FDT Procedure**

I'm now formalizing P-FDT's two-stage procedure. I'm starting by clarifying EDT, CDT, and action-FDT's hypothetical constructions and the explicit mathematical equations. I'll outline each component: state, observation, action, and policy spaces, with the logical policy variable using Kleene's recursion theorem. Finally, I'll formalize the intervention and evaluation steps.


**Clarifying P-FDT Interventions**

I'm now clarifying how P-FDT tackles subjunctive dependencies, counterpossibilities, and observations, especially in single-agent dilemmas. I'm focusing on why it differs from EDT/CDT's and action-FDT's approaches, using Transparent Newcomb and Mechanical Blackmail as examples. I'm working to formalize the structural equations and calculate the expected utility for each policy in these scenarios.


**Formalizing P-FDT Benefits**

I'm now formalizing the mechanics of the two-stage policy, by deriving the utility from both branches. I am now working on proving P-FDT's key advantage in the Two-Room Twin Stag Hunt. By intervening on the *policy* and setting actions, regardless of the prior beliefs or individual branches, it yields a clear payoff. This proves P-FDT's ability to coordinate, despite asymmetric observations, by selecting $\pi^* = \pi_{1,2}$.


**Formalizing P-FDT Scenarios**

I'm now formalizing multi-agent dilemmas, particularly the Observation Twin Prisoner's Dilemma and Stag Hunt. I'm focusing on why action-FDT treats the other room's node as exogenous. By contrast, P-FDT intervenes on a shared policy, simultaneously setting both actions, ensuring cooperation or coordination. I'm demonstrating single-agent settings where a predictor simulating across branches also breaks separability.


**Refining P-FDT Domain**

I'm now zeroing in on defining P-FDT's policy domain. I'm clarifying whether the domain is observations alone or encompasses general inputs, as the original text suggests. I'm exploring the nuances of the Smoking Lesion Problem, where there's no direct observation, to show when policies should map observations to actions vs. when epistemic parameters are fixed within the policy node's name.



**Refining P-FDT Scenarios**

I'm now zeroing in on handling zero-probability observation branches, like those in XOR Blackmail. I'm focusing on well-defined prescriptions on all branches. I am considering refining this with a full-support epsilon-tremble, to avoid undefined prescriptions. I'm focusing on defining an operational refinement.



**Refining References and Formatting**

I'm now refining the references section, ensuring I have enough and following formatting guidelines. I'm also reviewing the word count targets and naming conventions, which I will stick to during drafting. Finally, I will check all quotes to verify exact wording.


**Refining Definitions & Exposition**

I'm now zeroing in on defining the policy function, making the epistemic perspective clear, as I've been requested, and I'm integrating this with the formalization process. I'm taking notes from the references to improve the readability. I'm focusing on crafting a coherent exposition for mathematically literate readers, and on ensuring a clear and succinct presentation.


**Clarifying Example Nuances**

I'm now clarifying the nuances in the Transparent Newcomb problem example. Specifically, I'm ensuring we clearly distinguish between Yudkowsky and Soares's (2017) claims and our own formal extensions and operational proposals. I'm focusing on making that distinction explicit. I'm working on a clear mathematical presentation.


**Refining Formal Example**

I'm now zeroing in on a formal P-FDT example for Transparent Newcomb. My current task is formally representing Yudkowsky and Soares's (2017) definition of "full" and "empty" boxes, and how these affect the choice of policies. I am checking the formalization of the value for the agent as a function of the action and observations. I'm focusing on defining the expectation equation to map the actions to the observations and the overall value.


**Formalizing Newcomb Utility**

I'm now formalizing the utility calculation for the Transparent Newcomb problem with the two-stage policy. I've broken down the value of each policy based on the observation branches and their corresponding action choices, as demonstrated with a new, simplified, example calculation.


**Analyzing Twin Payoffs**

I'm now analyzing asymmetric twin coordination scenarios. I am reviewing the setup where agents have asymmetric observations and comparing the "Twin Stag Hunt" with the "Asymmetric-Role Twin Prisoner's Dilemma". I'm trying to see how to formalize the implications of joint payoffs in these scenarios. I'm focusing on the agent's expected utility and the impacts of room selection.


**Clarifying Shared World-Model**

I'm now focusing on a critical insight: P-FDT's shared node, $\textsc{pfdt}(\underline{P}, \underline{G})$, represents the twins' *shared prior* world-model before they observe their room. This explains why optimizing the utility, $\textsc{V}_1$, selects $\pi(A) = D, \pi(B) = C$, because their models $(P, G)$ are formulated prior to the individual observation. This contrasts directly with the asymmetric room observation and emphasizes the shared prior perspective.


**Contrasting FDT Implementations**

I'm now focusing on a critical distinction. Under action-FDT in the shared prior setup, with additively separable payoffs, both agents cooperate. However, with non-separable payoffs, which are the norm in multi-agent games, action-FDT's behavior diverges significantly. I'm exploring the implications of this divergence, contrasting with P-FDT.


**Revising Non-Additive Payoffs**

I'm now revising the non-additive payoffs in the Prisoner's Dilemma to ensure a dramatic divergence between action-FDT and P-FDT. I'm focusing on scenarios where the payoff for mutual cooperation creates a surplus that cannot be achieved by a single cooperator. I will examine why this scenario results in the divergence I was expecting.


**Refining Twin Divergence**

I'm now revising the non-additive twin payoffs to highlight action-FDT's divergence in the asymmetric Prisoner's Dilemma. I'm focusing on the selection of policy $D$. I'm verifying the choice of the dominated state of $(C,C)$, to confirm that it's possible for a twin to cooperate by selecting the dominated state $C$.



**Refining Payoff Analysis**

I'm now zeroing in on a formalization problem. My recent calculations show issues with non-additive payoffs in the asymmetric twin Prisoner's Dilemma. I need to make the payoff structure more dramatic to ensure the expected divergence. Specifically, I'm verifying the dominance of policy $C$, and checking the payoffs.



**Refining Dominance Example**

I'm now zeroing in on a formalization problem. My recent calculations show that the Prisoner's Dilemma payoffs need further refinement. I'm focusing on the non-additivity and ensuring that the payoff structure is dramatically non-separable to demonstrate a clear divergence. I will now examine why this example results in the divergence I expected.


**Verifying Divergence Calculations**

I'm now re-examining action-FDT calculations in the asymmetric twin Prisoner's Dilemma. I need to formally verify the divergence and confirm the dominance of defection, which I had previously calculated. I'm carefully reviewing the payoffs and ensuring the mathematical steps are correct. The goal is to accurately represent the counter-intuitive result.


**Verifying Twin Payoffs**

I'm now calculating the payoffs for both action-FDT and P-FDT in the asymmetric twin prisoner's dilemma, confirming action-FDT's defection. The aim is to verify that, under action-FDT, even with cooperative payoffs, pessimistic beliefs lead to defection in both cases. I will now prove that P-FDT achieves cooperation.


```
