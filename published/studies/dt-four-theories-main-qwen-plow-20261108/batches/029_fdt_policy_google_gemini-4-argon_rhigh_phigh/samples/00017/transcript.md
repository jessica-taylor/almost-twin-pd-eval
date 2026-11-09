# 029_fdt_policy_google_gemini-4-argon_rhigh_phigh / 00017

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/849023c7-2901-40c4-8470-77fd9d5d4b42/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/849023c7-2901-40c4-8470-77fd9d5d4b42/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Policy Functional Decision Theory (P-FDT): Formalizing Global Choice Over Policies

## 1. Introduction: From Physical Acts to Decision Policies

In classical decision theory, an agent stands at a fork in time and asks what physical action to execute. **Causal decision theory (CDT)** advises the agent to select the physical act that *causes* the best expected outcome, holding fixed the causal past. **Evidential decision theory (EDT)** advises the agent to select the physical act that provides the best *news*—the act upon which conditioning the agent's beliefs yields the highest expected utility. Yet as a long tradition of Newcomblike dilemmas demonstrates, neither theory reliably maximizes utility across environments. CDT is systematically impoverished in scenarios involving accurate predictors or symmetric co-players (such as Newcomb's problem, Parfit's hitchhiker, and the twin prisoner's dilemma), whereas EDT is vulnerable to "managing the news" in common-cause environments and extortionate signaling (such as the smoking lesion problem and the XOR blackmail problem).

In *"Functional Decision Theory: A New Theory of Instrumental Rationality"*, Eliezer Yudkowsky and Nate Soares propose **functional decision theory (FDT)** to resolve this impasse. The philosophical core of their proposal is a shift from Peirce's action *tokens* to computational *types*. Rather than treating a decision as an isolated physical intervention or a piece of statistical evidence, a functional decision theorist treats her decision as the logical output of a fixed mathematical function—her decision procedure itself. When evaluating options, she asks: *"Which output of this very decision procedure yields the best outcome?"* Because other physical systems in the environment—such as psychological twins, game-theoretic counterparts, or predictors running mental simulations—may compute or model this same mathematical function, their behaviors *subjunctively depend* on its output.

However, a careful reading of Yudkowsky and Soares reveals that their paper actually contains two distinct formalizations of this principle. In the main text (Section 5, Equation 4), for ease of exposition, the authors formalize what we may call **action-based functional decision theory (A-FDT)**: an algorithm that takes a world-model and a specific observation history as inputs, intervenes on the mathematical node representing the function's output *at that specific observation*, and directly outputs an action. Yet in Footnotes 7 and 16, the authors note that this action-by-action formulation is merely a pedagogical simplification. In Footnote 7, they write:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

And in Footnote 16, while discussing why functional decision theorists do not perform standard Bayesian updating on observations before intervening, they state the core mechanism of their preferred theory:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

In this essay, we develop a rigorous mathematical account of this policy-based formulation, which we call **policy functional decision theory (P-FDT)**. Because the reference paper sketches **P-FDT** only in these brief passages, our goal is twofold: first, to synthesize the formal machinery of the paper into a complete operational specification of **P-FDT**; and second, to investigate the exact mathematical questions left open by Footnotes 7 and 16—including why **P-FDT** diverges from **A-FDT** in multi-agent dilemmas, how "inputs" versus "observations" should be typed, and how **P-FDT** handles measure-zero counterfactual branches. Throughout, we explicitly distinguish the claims made in Yudkowsky and Soares's text from our own mathematical reconstructions and extensions.

---

## 2. Mathematical Foundations of P-FDT

### 2.1 The Expected Utility Framework and Competing Epistemic Perspectives

Following Yudkowsky and Soares (who build on Gibbard and Harper 1978 and Joyce 1999), expected utility theories share a common valuation structure. Let $\mathcal{O} = \{o_1, o_2, \dots\}$ be a countable set of outcomes, $\mathcal{A}$ be a finite set of physical actions, and $\mathcal{X}$ be a countable set of possible observation histories. Let $\mathcal{U} : \mathcal{O} \to \mathbb{R}$ be a bounded utility function, and define the utility random variable $V \coloneqq \mathcal{U}(\textsc{Outcome})$.

In general, an expected utility maximizer who has received observation $x \in \mathcal{X}$ evaluates an option $a \in \mathcal{A}$ via:

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j),$$

where $P(a \hookrightarrow o_j ;\, x)$ denotes the probability that outcome $o_j$ obtains in the decision-theoretic *hypothetical* $M^{a\hookrightarrow}$ constructed from the agent's world-model $M$ for option $a$ given observation $x$. As James Joyce (1999) proved in his representation theorem, competing decision theories do not disagree on the mechanics of expected value; rather, they supply different constraints on the hypothetical connective "$\hookrightarrow$"—different rules for how an agent should construct hypothetical scenarios $M^{a\hookrightarrow}$ from her world-model $M$.

In the paper's formalization:
1. **Evidential Decision Theory (EDT)** represents the world-model solely as a Bayesian probability distribution $P$ over variables $(\textsc{Obs}, \textsc{Act}, \textsc{Outcome}, V, \dots)$ and constructs hypotheticals via standard conditionalization:
   $$\mathrm{EDT}(P, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(V \;\middle|\; \textsc{Obs}=x, \textsc{Act}=a\right).$$

2. **Causal Decision Theory (CDT)** augments the probability distribution $P$ with a directed acyclic causal graph $G$ (following Pearl 1996, 2000). Upon observing $x$, a **CDT** agent conditions on $\textsc{Obs}=x$ and constructs hypotheticals using Pearl's graph-surgery operator $\mathtt{do}(\textsc{Act}=a)$, which severs incoming causal arrows into the physical action node $\textsc{Act}$, sets $\textsc{Act}=a$, and propagates the change strictly to variables causally downstream of $\textsc{Act}$:
   $$\mathrm{CDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(V \;\middle|\; \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x\right).$$

3. **Action-Based Functional Decision Theory (A-FDT)**—the simplified version presented in Equation (4) of Yudkowsky and Soares—augments $P$ with an extended dependency graph $G$ that encodes not only physical causation, but also logical, mathematical, and computational *subjunctive dependencies*. Rather than intervening on $\textsc{Act}$ and conditioning on $\textsc{Obs}=x$, **A-FDT** intervenes on a logical node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ representing the output of the decision algorithm on inputs $(P, G, x)$:
   $$\mathrm{A\text{-}FDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(V \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right).$$
   Here, underlines denote dequoting (so if $x = \textit{full}$, $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ names the specific variable $\textsc{fdt}(\underline{P}, \underline{G}, \textit{full})$ inside $G$). Self-reference is achieved without circularity via Kleene's (1938) second recursion theorem ("quining").

### 2.2 Formalizing P-FDT

While **A-FDT** treats each observation-indexed call $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ as a separate node in $G$, Footnotes 7 and 16 specify that the decision function should instead output a *policy*—a complete mapping from inputs to actions—and then apply that policy to the agent's actual inputs.

To make **P-FDT** mathematically precise, we now introduce explicit definitions that operationalize Footnotes 7 and 16. (While the two-stage policy-selection and input-application structure is directly stated in Footnote 16, the exact formal notation below is our reconstruction.)

**Definition 1 (Policy Space).** Let $\mathcal{X}$ be the set of possible observations in the decision problem, and $\mathcal{A}$ be the finite set of available actions. A *policy* is a function $\pi : \mathcal{X} \to \mathcal{A}$. Let $\Pi \subseteq \mathcal{A}^{\mathcal{X}}$ denote the space of admissible policies. (In idealized models where $\mathcal{X}$ is finite, $\Pi = \mathcal{A}^{\mathcal{X}}$ has cardinality $|\mathcal{A}|^{|\mathcal{X}|}$.)

**Definition 2 (P-FDT World-Model and Subjunctive Graph).** A **P-FDT** world-model is a pair $M = (P, G)$ where:
* $G$ is a directed acyclic graph containing a distinguished logical node $\textsc{pfdt}(\underline{P}, \underline{G})$ taking values in the policy space $\Pi$, alongside environmental variables, predictor variables, observation node(s) $\textsc{Obs} \in \mathcal{X}$, physical action node(s) $\textsc{Act} \in \mathcal{A}$, and utility node $V$.
* In the structural equations of $(P, G)$, whenever a physical system (such as the agent's body) executes **P-FDT** upon receiving observation $\textsc{Obs}$, its physical action is governed by the evaluation map:
  $$\textsc{Act}\big(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi,\, \textsc{Obs} = x\big) \coloneqq \pi(x).$$
* Similarly, any predictor or twin in the environment whose behavior subjunctively depends on the agent's decision procedure is structurally modeled as a child (or descendant) of the single policy node $\textsc{pfdt}(\underline{P}, \underline{G})$.

**Definition 3 (The P-FDT Decision Rule).** Given a world-model $(P, G)$ and an actual observation $x \in \mathcal{X}$, **P-FDT** selects an action in two steps:

1. **Global Policy Selection:** The agent identifies the optimal policy $\pi^* \in \Pi$ by intervening on the logical policy node $\textsc{pfdt}(\underline{P}, \underline{G})$ and maximizing prior (unconditioned) expected utility:
   $$\mathrm{PFDT}_{\mathrm{pol}}(P, G) \coloneqq \argmax_{\pi \in \Pi} \mathbb{E}\left(V \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right). \tag{P-FDT-1}$$

2. **Input Application:** The agent applies the selected policy $\pi^* = \mathrm{PFDT}_{\mathrm{pol}}(P, G)$ to her actual observation $x$ to output a physical action:
   $$\mathrm{PFDT}(P, G, x) \coloneqq \big[\mathrm{PFDT}_{\mathrm{pol}}(P, G)\big](x) = \pi^*(x). \tag{P-FDT-2}$$

Expanding the expectation in $(\text{P-FDT-1})$ by the law of total probability over possible observations $x' \in \mathcal{X}$ illuminates how **P-FDT** evaluates policies:

$$\mathbb{E}\left(V \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right) = \sum_{x' \in \mathcal{X}} P\left(\textsc{Obs} = x' \;\middle|\; \mathtt{do}(\textsc{pfdt} = \pi)\right) \cdot \mathbb{E}\left(V \;\middle|\; \textsc{Obs} = x',\, \mathtt{do}(\textsc{pfdt} = \pi)\right).$$

Notice two foundational features of this equation:
* **Endogenous Observation Probabilities ("Updatelessness"):** The probability of receiving observation $x'$, $P(\textsc{Obs} = x' \mid \mathtt{do}(\textsc{pfdt} = \pi))$, is *itself* a function of the policy $\pi$. As Yudkowsky and Soares note in Section 9, this reflects the core insight of Wei Dai's (2009) **Updateless Decision Theory (UDT)** (and avoids the harmful "double update" of Yudkowsky's 2010 **Timeless Decision Theory (TDT)**, which both conditioned on $\textsc{Obs}=x$ and intervened logically). Under **P-FDT**, the agent never conditions $P$ on $\textsc{Obs}=x$ during step $(\text{P-FDT-1})$. Instead, the observation $x$ enters only at step $(\text{P-FDT-2})$ when evaluating $\pi^*(x)$.
* **Simultaneous Cross-Branch Counterfactuals:** When **P-FDT** constructs the hypothetical $M^{\pi\hookrightarrow}$ via $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$, it simultaneously specifies how the agent acts under *every* possible observation $x' \in \mathcal{X}$.

---

## 3. How P-FDT Evaluates Single-Agent Dilemmas

To see how **P-FDT** operates in practice—and why it cleanly streamlines the calculations of **A-FDT**—let us apply Definitions 1–3 to the **Transparent Newcomb Problem** (Dilemma 5 in the source paper, mathematically isomorphic to Parfit's Hitchhiker and the Mechanical Blackmail problem).

### 3.1 Worked Example 1: The Transparent Newcomb Problem

In the **Transparent Newcomb Problem**, both box A (containing $\$1,000$) and box B (containing either $\$1,000,000$ or $\$0$) are transparent. A predictor with $99\%$ accuracy ($\textsc{Accurate} = \textit{accurate}$ with probability $0.99$, $\textit{inaccurate}$ with probability $0.01$) places $\$1,000,000$ in box B if and only if she predicts that the agent will leave box A behind ($\textit{onebox}$) upon observing that box B is $\textit{full}$. The agent arrives and observes $x = \textit{full}$. Should she $\textit{onebox}$ or $\textit{twobox}$?

Let us set up the **P-FDT** model $(P, G)$:
* **Observation space:** $\mathcal{X} = \{\textit{full}, \textit{empty}\}$.
* **Action space:** $\mathcal{A} = \{\textit{1} \text{ (onebox)}, \textit{2} \text{ (twobox)}\}$.
* **Policy space:** $\Pi = \mathcal{A}^{\mathcal{X}}$ consists of four deterministic policies, which we write as pairs $\pi = (\pi(\textit{full}), \pi(\textit{empty}))$:
  $$\pi_{11} = (\textit{1}, \textit{1}), \quad \pi_{12} = (\textit{1}, \textit{2}), \quad \pi_{21} = (\textit{2}, \textit{1}), \quad \pi_{22} = (\textit{2}, \textit{2}).$$
* **Structural Equations in $G$:**
  The node $\textsc{pfdt}(\underline{P}, \underline{G})$ has no parents. $\textsc{Accurate} \sim \text{Bernoulli}(0.99)$ is an exogenous noise node. The predictor simulates the agent's policy on the $\textit{full}$ input:
  $$\textsc{Prediction}(\pi, \textit{accurate}) = \pi(\textit{full}), \qquad \textsc{Prediction}(\pi, \textit{inaccurate}) = 3 - \pi(\textit{full}).$$
  Box B and the agent's observation are determined by the prediction:
  $$\textsc{Box B}(\textsc{Prediction}) = \textsc{Obs}(\textsc{Prediction}) = \begin{cases} \textit{full} & \text{if } \textsc{Prediction} = \textit{1}, \\ \textit{empty} & \text{if } \textsc{Prediction} = \textit{2}. \end{cases}$$
  The agent's physical action applies the policy to the observation:
  $$\textsc{Act}(\pi, \textsc{Obs}) = \pi(\textsc{Obs}).$$
  Finally, utility $V$ is $\$1,000,000 \cdot \mathbb{I}(\textsc{Box B} = \textit{full}) + \$1,000 \cdot \mathbb{I}(\textsc{Act} = \textit{2})$.

Now we execute **P-FDT**:

**Step 1 (Policy Evaluation):** For any policy $\pi \in \Pi$, intervening via $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$ yields:
* Under $\pi_{11} = (\textit{1}, \textit{1})$: Since $\pi_{11}(\textit{full}) = \textit{1}$, with probability $0.99$ ($\textit{accurate}$) the predictor predicts $\textit{1}$, so $\textsc{Obs} = \textit{full}$ and $\textsc{Act} = \pi_{11}(\textit{full}) = \textit{1}$, giving $\$1,000,000$. With probability $0.01$ ($\textit{inaccurate}$), $\textsc{Obs} = \textit{empty}$ and $\textsc{Act} = \pi_{11}(\textit{empty}) = \textit{1}$, giving $\$0$.
  $$\mathbb{E}[V \mid \mathtt{do}(\textsc{pfdt} = \pi_{11})] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000.$$
* Under $\pi_{12} = (\textit{1}, \textit{2})$: Since $\pi_{12}(\textit{full}) = \textit{1}$, with probability $0.99$ we have $\textsc{Obs} = \textit{full}$ and $\textsc{Act} = \pi_{12}(\textit{full}) = \textit{1}$ ($\$1,000,000$). With probability $0.01$, $\textsc{Obs} = \textit{empty}$ and $\textsc{Act} = \pi_{12}(\textit{empty}) = \textit{2}$ ($\$1,000$).
  $$\mathbb{E}[V \mid \mathtt{do}(\textsc{pfdt} = \pi_{12})] = 0.99(\$1,000,000) + 0.01(\$1,000) = \$990,010.$$
* Under $\pi_{21} = (\textit{2}, \textit{1})$: Since $\pi_{21}(\textit{full}) = \textit{2}$, with probability $0.01$ ($\textit{inaccurate}$) we have $\textsc{Obs} = \textit{full}$ and $\textsc{Act} = \textit{2}$ ($\$1,001,000$). With probability $0.99$ ($\textit{accurate}$), $\textsc{Obs} = \textit{empty}$ and $\textsc{Act} = \textit{1}$ ($\$0$).
  $$\mathbb{E}[V \mid \mathtt{do}(\textsc{pfdt} = \pi_{21})] = 0.01(\$1,001,000) + 0.99(\$0) = \$10,010.$$
* Under $\pi_{22} = (\textit{2}, \textit{2})$: With probability $0.01$, $\textsc{Obs} = \textit{full}$ and $\textsc{Act} = \textit{2}$ ($\$1,001,000$); with probability $0.99$, $\textsc{Obs} = \textit{empty}$ and $\textsc{Act} = \textit{2}$ ($\$1,000$).
  $$\mathbb{E}[V \mid \mathtt{do}(\textsc{pfdt} = \pi_{22})] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$

Comparing the four values, the unique optimal policy is:
$$\pi^* = \mathrm{PFDT}_{\mathrm{pol}}(P, G) = \pi_{12} = (\textit{1}, \textit{2}).$$

**Step 2 (Input Application):** Having actually observed $x = \textit{full}$, the agent computes:
$$\mathrm{PFDT}(P, G, \textit{full}) = \pi_{12}(\textit{full}) = \textit{1} \text{ (onebox)}.$$
(And had the predictor erred so that $x = \textit{empty}$, the agent would have computed $\pi_{12}(\textit{empty}) = \textit{2}$, taking the $\$1,000$ consolation prize.)

### 3.2 Subtle Improvement Over A-FDT in Single-Agent Models

Although **P-FDT** and **A-FDT** both prescribe one-boxing upon seeing $\textit{full}$, comparing our calculation above with Section 6 of Yudkowsky and Soares highlights a notable structural cleanup. In **A-FDT**, because Fiona's graph $G^F$ splits her algorithm into two separate nodes—$\textsc{fdt}(\underline{P}^F, \underline{G}^F, \textit{full})$ and $\textsc{fdt}(\underline{P}^F, \underline{G}^F, \textit{empty})$—intervening on $\textsc{fdt}(\underline{P}^F, \underline{G}^F, \textit{full})$ leaves $\textsc{fdt}(\underline{P}^F, \underline{G}^F, \textit{empty})$ as an un-intervened random variable. Consequently, the authors had to introduce an arbitrary prior probability $q = P^F(\textsc{fdt}(\underline{P}^F, \underline{G}^F, \textit{empty}) = \textit{twobox})$ representing Fiona's uncertainty about what she would do on the other observation branch, yielding expected utilities $\$990,000 + \$10q$ vs. $\$10,010 + \$990q$.

In **P-FDT**, this nuisance parameter $q$ vanishes completely. Because **P-FDT** intervenes on the unified policy node $\textsc{pfdt}(\underline{P}, \underline{G})$, the agent does not need to hold prior probabilistic beliefs about her own counterfactual behavior at unreached observations; she directly optimizes over her actions at all observations simultaneously.

---

## 4. Multi-Agent Dilemmas: Why P-FDT Diverges from A-FDT

Why do Yudkowsky and Soares remark in Footnotes 7 and 16 that choosing policies rather than actions *"makes a difference in certain multi-agent dilemmas"*? The reference paper does not provide an example or proof of this divergence. In this section, we construct the mathematical mechanism of this divergence and demonstrate it on concrete multi-agent dilemmas. (The theorems and dilemmas in this section are our own mathematical developments designed to explain and verify the authors' claim in Footnotes 7 and 16.)

### 4.1 The Structural Mechanism of Divergence

Consider why **A-FDT** and **P-FDT** agree in single-agent problems like Transparent Newcomb or XOR Blackmail. In a single-agent problem, nature realizes only *one* observation $x \in \mathcal{X}$ in any given world state. The different observation branches $x \in \mathcal{X}$ partition the probability space into mutually exclusive events $\{\textsc{Obs} = x\}$. Because expectation is linear across mutually exclusive events, as long as the predictor's behavior in a given world depends on at most one branch's output (or depends additively), maximizing over $\pi(x)$ branch-by-branch (**A-FDT**) yields the same action as maximizing over the entire function $\pi$ jointly (**P-FDT**).

In **multi-agent dilemmas**, however, two or more physical agents who share the same decision function—such as psychological twins or copies of an AI system—coexist in the *same* world and receive *different* observations $x_1 \neq x_2$ simultaneously. Consequently, the payoff in a single world state depends **non-additively** (jointly) on $\pi(x_1)$ and $\pi(x_2)$.

Under **A-FDT**, the agent observing $x_1$ intervenes *only* on the node $\textsc{fdt}(\underline{P}, \underline{G}, x_1)$, treating the node $\textsc{fdt}(\underline{P}, \underline{G}, x_2)$ that governs her twin in the other room as causally and subjunctively independent of her intervention! Under **P-FDT**, by contrast, both twins' actions are downstream of the *same* policy node $\textsc{pfdt}(\underline{P}, \underline{G})$. Intervening to set $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$ simultaneously determines $\pi(x_1)$ and $\pi(x_2)$.

This creates two major classes of multi-agent dilemmas where **P-FDT** strictly outperforms **A-FDT**:

### 4.2 Worked Example 2: The Asymmetric-Observation Twin Prisoner's Dilemma

Consider first a variant of Dilemma 1 (the Psychological Twin Prisoner's Dilemma) where the two twins receive distinct sensory inputs that identify their physical locations:

> **Dilemma A (Role-Identified Twin Prisoner's Dilemma).** Two psychological twins, running the exact same decision procedure, are placed in separate rooms: one is placed in the **North Room** and observes $x = N$, while the other is placed in the **South Room** and observes $x = S$. Each must choose to Cooperate ($C$) or Defect ($D$). Cooperation costs the actor $\$1,000$ and delivers $\$1,000,000$ to the twin in the other room. Each twin cares only about her own monetary payoff.

How this dilemma behaves depends critically on how the prior distribution $P$ models the agent's identity—and whether the agent uses **A-FDT** or **P-FDT**.

Suppose first that the agent's world-model $P$ encodes her physical identity directly (for instance, she is the physical copy designated "Player 1", who was deterministically routed to the North Room, so $V = V_{\text{North}}$, while her twin "Player 2" was routed to the South Room and receives $V_{\text{South}}$):
* **How A-FDT fails:** Player 1 observes $x = N$ and evaluates $\mathrm{A\text{-}FDT}(P, G, N)$. She intervenes on $\textsc{fdt}(\underline{P}, \underline{G}, N) = a_N$. Because Player 2 observed $S \neq N$, Player 2's action is governed by a *different* node, $\textsc{fdt}(\underline{P}, \underline{G}, S)$. In $G$, there is no directed path from $\textsc{fdt}(\underline{P}, \underline{G}, N)$ to $\textsc{fdt}(\underline{P}, \underline{G}, S)$. Thus, changing $\textsc{fdt}(\underline{P}, \underline{G}, N)$ from $C$ to $D$ saves Player 1 $\$1,000$ without altering Player 2's action at all! **A-FDT** prescribes **Defect** ($D$) for both twins, leaving each with $\$1,000$ instead of $\$1,000,000$—collapsing right back into the classic **CDT** failure whenever twins have distinguishable observations!

Now suppose instead that both twins share a symmetric prior $P$ formed *behind a veil of ignorance* regarding which room they occupy: in $P$, the agent has probability $0.5$ of being the North twin ($\textsc{Obs}=N, V = V_N$) and probability $0.5$ of being the South twin ($\textsc{Obs}=S, V = V_S$). In this additive Prisoner's Dilemma, because a single twin's cooperation adds $0.5(-\$1,000) + 0.5(\$1,000,000) = +\$499,500$ to the veil-of-ignorance expectation $\mathbb{E}[V]$, even **A-FDT** can cooperate under a veil-of-ignorance prior. **However**, as soon as the payoff structure is *synergistic* (non-additive) across the two rooms, **A-FDT** fails even under a veil of ignorance! Let us prove this with a second multi-agent dilemma.

### 4.3 Worked Example 3: The Multi-Agent Asymmetric Twin Stag Hunt (Cross-Branch Coordination)

> **Dilemma B (Asymmetric Twin Stag Hunt / Joint Vault Dilemma).** Two psychological twins (or two copies of an AI agent) are placed in separate rooms: one in Room $L$ (observing $x = L$) and one in Room $R$ (observing $x = R$). In the prior $P$, the agent has a $50\%$ chance of waking up in Room $L$ and a $50\%$ chance of waking up in Room $R$.
> 
> Room $L$ contains a heavy **Left Lever** ($a \in \{\textit{Pull}_L, \textit{Pass}_L\}$) and Room $R$ contains a heavy **Right Lever** ($a \in \{\textit{Pull}_R, \textit{Pass}_R\}$). Pulling a lever costs the twin who pulls it $\$1,000$ in effort. A central vault opens and awards $\$1,000,000$ to each twin **if and only if** the twin in Room $L$ pulls the Left Lever **and** the twin in Room $R$ pulls the Right Lever. If only one twin pulls, the vault remains locked: the puller gets $-\$1,000$ and the passer gets $\$0$.

Let us compare **A-FDT** and **P-FDT** on Dilemma B.

#### Analysis under A-FDT (Action-Based FDT)

In **A-FDT**, the graph $G$ contains two distinct logical nodes: $\textsc{fdt}_L \coloneqq \textsc{fdt}(\underline{P}, \underline{G}, L)$ and $\textsc{fdt}_R \coloneqq \textsc{fdt}(\underline{P}, \underline{G}, R)$.
Suppose the agent wakes up in Room $L$ ($x = L$). She computes:
$$\mathrm{A\text{-}FDT}(P, G, L) = \argmax_{a_L \in \{\textit{Pull}_L, \textit{Pass}_L\}} \mathbb{E}\left(V \;\middle|\; \mathtt{do}(\textsc{fdt}_L = a_L)\right).$$
Because $\textsc{fdt}_R$ is a separate node not downstream of $\textsc{fdt}_L$, its value under $\mathtt{do}(\textsc{fdt}_L = a_L)$ is governed solely by the agent's prior probability $q_R \coloneqq P(\textsc{fdt}_R = \textit{Pull}_R)$.
* If she intervenes with $\mathtt{do}(\textsc{fdt}_L = \textit{Pull}_L)$:
  With probability $0.5$ she is the twin in Room $L$ (who definitely pays $-\$1,000$), and with probability $0.5$ she is the twin in Room $R$ (who pays $-\$1,000$ with probability $q_R$). In either room, the vault opens iff $\textsc{fdt}_R = \textit{Pull}_R$ (probability $q_R$). Thus:
  $$\mathbb{E}\big[V \;\big|\; \mathtt{do}(\textsc{fdt}_L = \textit{Pull}_L)\big] = q_R \cdot \$1,000,000 - 0.5(\$1,000) - 0.5 q_R(\$1,000) = \$999,500 q_R - \$500.$$
* If she intervenes with $\mathtt{do}(\textsc{fdt}_L = \textit{Pass}_L)$:
  The vault never opens ($0$), and the Room $R$ twin pulls with probability $q_R$:
  $$\mathbb{E}\big[V \;\big|\; \mathtt{do}(\textsc{fdt}_L = \textit{Pass}_L)\big] = -\$500 q_R.$$

Comparing the two expressions, $\mathrm{A\text{-}FDT}(P, G, L)$ chooses $\textit{Pull}_L$ if and only if $\$1,000,000 q_R > \$500$, i.e., $q_R > 0.0005$.

Look closely at what happens if the twins initially have a low prior belief that the other branch will pull—say, $q_L = q_R = 0$:
* When the twin in Room $L$ runs **A-FDT**, because $q_R = 0$, she calculates that $\textit{Pull}_L$ yields $-\$500$ while $\textit{Pass}_L$ yields $\$0$. So $\mathrm{A\text{-}FDT}(P, G, L) = \textit{Pass}_L$.
* Symmetrically, when the twin in Room $R$ runs **A-FDT**, because $q_L = 0$, $\mathrm{A\text{-}FDT}(P, G, R) = \textit{Pass}_R$.
* Worse still, the prior beliefs $q_L = 0$ and $q_R = 0$ are **completely reflectively consistent**! Each twin accurately predicts that **A-FDT** outputs $\textit{Pass}$ on the other observation branch, and given that prediction, **A-FDT** indeed outputs $\textit{Pass}$ on her own branch!

Just as Yudkowsky and Soares criticize **EDT** in Section 6 (citing Spohn 1977) for being "at the mercy of her priors" when an extreme prior locks **EDT** into a suboptimal self-confirming equilibrium, **A-FDT** suffers from the exact same pathology across distinct observation branches in multi-agent games! Even more starkly, if the game is an **Asymmetric Anti-Coordination Game**—where both twins get $\$1,000,000$ if and only if they choose *opposite* actions from $\{\textit{Alpha}, \textit{Beta}\}$ ($a_L \neq a_R$) and $\$0$ if they choose the same action—and both twins start with a symmetric uniform prior $q_L = q_R = 0.5$, **A-FDT** evaluates $\textit{Alpha}$ and $\textit{Beta}$ as tied ($0.5 \times \$1,000,000$ each) at both $L$ and $R$, providing no mechanism to guarantee opposite actions.

#### Analysis under P-FDT (Policy Functional Decision Theory)

Now let us apply **P-FDT** to Dilemma B. The policy space is $\Pi = \{(\textit{Pull}_L, \textit{Pull}_R),\, (\textit{Pull}_L, \textit{Pass}_R),\, (\textit{Pass}_L, \textit{Pull}_R),\, (\textit{Pass}_L, \textit{Pass}_R)\}$. Both twins' actions are governed by the single policy node $\textsc{pfdt}(\underline{P}, \underline{G})$:
$$\textsc{Act}_L = \pi(L), \qquad \textsc{Act}_R = \pi(R).$$

In Step 1 ($\text{P-FDT-1}$), the agent intervenes on $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$ for each of the four policies:
1. $\mathtt{do}\big(\textsc{pfdt} = (\textit{Pull}_L, \textit{Pull}_R)\big)$: Both levers are pulled with probability $1$. Both twins receive $\$1,000,000 - \$1,000 = \$999,000$.
   $$\mathbb{E}\big[V \;\big|\; \mathtt{do}(\textsc{pfdt} = (\textit{Pull}_L, \textit{Pull}_R))\big] = \$999,000.$$
2. $\mathtt{do}\big(\textsc{pfdt} = (\textit{Pull}_L, \textit{Pass}_R)\big)$: Vault stays locked; Room $L$ twin loses $\$1,000$, Room $R$ twin gets $\$0$.
   $$\mathbb{E}\big[V \;\big|\; \mathtt{do}(\textsc{pfdt} = (\textit{Pull}_L, \textit{Pass}_R))\big] = 0.5(-\$1,000) + 0.5(\$0) = -\$500.$$
3. $\mathtt{do}\big(\textsc{pfdt} = (\textit{Pass}_L, \textit{Pull}_R)\big)$: Symmetrically yields $-\$500$.
4. $\mathtt{do}\big(\textsc{pfdt} = (\textit{Pass}_L, \textit{Pass}_R)\big)$: Neither pulls; vault stays locked.
   $$\mathbb{E}\big[V \;\big|\; \mathtt{do}(\textsc{pfdt} = (\textit{Pass}_L, \textit{Pass}_R))\big] = \$0.$$

Regardless of what prior probabilities $P$ initially assigned to $\textsc{pfdt}(\underline{P}, \underline{G})$, the $\mathtt{do}$ intervention wipes out those priors and directly identifies the globally optimal policy:
$$\pi^* = \mathrm{PFDT}_{\mathrm{pol}}(P, G) = (\textit{Pull}_L, \textit{Pull}_R).$$
In Step 2 ($\text{P-FDT-2}$), the twin in Room $L$ applies $\pi^*(L) = \textit{Pull}_L$, and the twin in Room $R$ applies $\pi^*(R) = \textit{Pull}_R$. Both walk away with $\$999,000$. (Likewise, in the Asymmetric Anti-Coordination game, **P-FDT** immediately eliminates the losing symmetric policies $(\textit{Alpha}, \textit{Alpha})$ and $(\textit{Beta}, \textit{Beta})$ and selects a coordinated asymmetric policy such as $(\textit{Alpha}, \textit{Beta})$ under a canonical tie-breaker.)

| Decision Theory | Node(s) Intervened Upon | Conditioning on $\textsc{Obs}=x$? | Vulnerable to Cross-Branch Prior Traps in Multi-Agent Games? | Prescription in Dilemma B (when prior $q=0$) |
| :--- | :--- | :--- | :--- | :--- |
| **EDT** | None (Bayesian conditioning on $\textsc{Act}$) | Yes | Yes (and single-agent prior traps) | $\textit{Pass}$ |
| **CDT** | Physical node $\textsc{Act}$ | Yes | Yes (ignores twin interdependence) | $\textit{Pass}$ |
| **A-FDT** | Point output $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ | No | **Yes** ($\textsc{fdt}(\cdot, L)$ and $\textsc{fdt}(\cdot, R)$ are separate nodes) | $\textit{Pass}$ |
| **P-FDT** | Full policy $\textsc{pfdt}(\underline{P}, \underline{G}) \in \mathcal{A}^{\mathcal{X}}$ | No (applies $\pi^*(x)$ ex post) | **No** (optimizes joint policy across all $x \in \mathcal{X}$) | $\textit{Pull}$ |

---

## 5. Unresolved Questions in the Source and Operational Proposals

Because Yudkowsky and Soares relegate **P-FDT** to Footnotes 7 and 16, several crucial mathematical questions regarding its full specification are left open. To enable a researcher to apply **P-FDT** unambiguously to unfamiliar cases, we now analyze three open questions in the source text and propose concrete operational resolutions.

### 5.1 Uncertainty 1: What Is the Domain of a Policy—Observations $\mathcal{X}$ or Full Inputs $\mathcal{I}$?

There is a subtle terminological shift between Footnote 7 and Footnote 16 in the source paper:
* **Footnote 7** defines policies as *"mappings from observations to actions"* ($\pi : \mathcal{X} \to \mathcal{A}$).
* **Footnote 16** says that the agent *"intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action."*

Why does the distinction between "observations" and "inputs" matter? Consider how Yudkowsky and Soares formalize the **Smoking Lesion Problem** in Section 6 (Figure 4). In that dilemma, Fiona receives no external sensory observation ($\textsc{Obs} = \emptyset$). However, the lesion causes its bearers to love smoking, which the authors formalize by saying that the lesion determines whether Fiona's world-model uses probability/utility distribution $P_S^F$ (built from $\mathcal{U}_S$, which values smoking at $\$1,000$) or $P_R^F$ (built from $\mathcal{U}_R$, which values smoking at $-\$1$). Because Fiona does not have introspective access to whether she has the lesion, her graph $G^F$ in Figure 4 contains two separate nodes: $\textsc{fdt}(\underline{P}_S^F, \underline{G}^F)$ and $\textsc{fdt}(\underline{P}_R^F, \underline{G}^F)$.

If a **P-FDT** policy only maps *external observations* $x \in \mathcal{X}$ to actions, then in the Smoking Lesion problem (where $\mathcal{X} = \{\emptyset\}$ is a singleton), **P-FDT** would still require two separate nodes $\textsc{pfdt}(\underline{P}_S^F, \underline{G}^F)$ and $\textsc{pfdt}(\underline{P}_R^F, \underline{G}^F)$, leaving the nuisance prior $q = P_S^F(\textsc{fdt}(\underline{P}_R^F, \underline{G}^F) = \textit{smoke})$ in the equations!

**Operational Proposal (Internalized Epistemic Inputs):** We propose resolving this tension in favor of Footnote 16's broader term *"inputs"* via a standard Harsanyi-style type consolidation. Whenever an agent faces uncertainty over her own local parameters (such as whether her local preference parameter is $\theta \in \Theta = \{S, R\}$ or which local epistemic state $x \in \mathcal{X}$ she occupies), we represent the background world-model $(P, G)$ as a single unified prior over $(\Theta, \mathcal{X}, \dots)$ and define the input space as $\mathcal{I} \coloneqq \Theta \times \mathcal{X}$. A policy is then a mapping $\pi : \mathcal{I} \to \mathcal{A}$.

Let us verify how cleanly this resolves the **Smoking Lesion Problem** under **P-FDT**:
* The input space is $\mathcal{I} = \{S, R\}$, representing the agent's local preference state induced by $\textsc{Lesion} \in \{\textit{lesion}, \textit{nolesion}\}$.
* The policy space $\Pi = \{\textit{smoke}, \textit{refrain}\}^{\{S, R\}}$ contains four policies $\pi = (\pi(S), \pi(R))$.
* With probability $p = P(\textsc{Lesion} = \textit{lesion})$, the agent receives input $S$ and her utility for smoking is $+\$1,000$; with probability $1-p$, she receives input $R$ and her utility for smoking is $-\$1$. Cancer occurs with probability $0.99$ given $\textit{lesion}$ and $0.01$ given $\textit{nolesion}$, causally and subjunctively independent of $\textsc{pfdt}(\underline{P}, \underline{G})$.
* Let $C_0 \coloneqq p(\$10,000) + (1-p)(\$990,000)$ be the baseline expected survival utility. Evaluating $(\text{P-FDT-1})$ across the four policies $\pi = (\pi(S), \pi(R))$:
  $$\begin{aligned}
  \mathbb{E}[V \mid \mathtt{do}(\textsc{pfdt} = (\textit{smoke}, \textit{refrain}))] &= C_0 + p(\$1,000) + (1-p)(\$0), \\
  \mathbb{E}[V \mid \mathtt{do}(\textsc{pfdt} = (\textit{smoke}, \textit{smoke}))] &= C_0 + p(\$1,000) + (1-p)(-\$1), \\
  \mathbb{E}[V \mid \mathtt{do}(\textsc{pfdt} = (\textit{refrain}, \textit{refrain}))] &= C_0, \\
  \mathbb{E}[V \mid \mathtt{do}(\textsc{pfdt} = (\textit{refrain}, \textit{smoke}))] &= C_0 + (1-p)(-\$1).
  \end{aligned}$$
* For any $p \in (0, 1)$, the unique optimal policy is $\pi^* = (\textit{smoke}, \textit{refrain})$, which smokes if and only if the agent enjoys smoking, without any dependence on the nuisance parameter $q$!

### 5.2 Uncertainty 2: Measure-Zero Observation Branches and Infallible Predictors

A second mathematical subtlety arises when a predictor is *infallible* ($\varepsilon = 0$ error rate rather than $0.01$, as Yudkowsky and Soares assume in the XOR Blackmail and Mechanical Blackmail dilemmas).

Consider the **Mechanical Blackmail Problem** (Dilemma 8) with a $100\%$ infallible predictor. The blackmailer launches a mutually destructive program (sending a blackmail letter $x = \textit{blackmail}$ rather than $x = \emptyset$) if and only if she predicts the agent will $\textit{pay}$ (losing $\$1,000$) rather than $\textit{refuse}$ (losing $\$1,000,000$) upon seeing $\textit{blackmail}$.

Suppose the only non-trivial action choice occurs when $x = \textit{blackmail}$ (at $x = \emptyset$, no action is required, or suppose the agent also has a side choice at $x = \emptyset$ whether to pick up a free $\$10$ bill on the street, $a_\emptyset \in \{\textit{take10}, \textit{leave10}\}$). Now, what if the agent considers a policy $\pi$ that *pays* the blackmailer ($\pi(\textit{blackmail}) = \textit{pay}$)? Under $\mathtt{do}(\textsc{pfdt} = \pi)$, because the blackmailer is $100\%$ infallible, $P(\textsc{Obs} = \textit{blackmail} \mid \mathtt{do}(\textsc{pfdt} = \pi)) = 1$ and $P(\textsc{Obs} = \emptyset \mid \mathtt{do}(\textsc{pfdt} = \pi)) = 0$. Conversely, in the **Transparent Newcomb Problem** with a $100\%$ infallible predictor, any policy $\pi$ with $\pi(\textit{full}) = \textit{1}$ (onebox) induces:
$$P\big(\textsc{Obs} = \textit{full} \;\big|\; \mathtt{do}(\textsc{pfdt} = \pi)\big) = 1, \qquad P\big(\textsc{Obs} = \textit{empty} \;\big|\; \mathtt{do}(\textsc{pfdt} = \pi)\big) = 0.$$
Consequently, under an infallible predictor in Transparent Newcomb, both $\pi_{11} = (\textit{1}, \textit{1})$ and $\pi_{12} = (\textit{1}, \textit{2})$ yield the exact same global expected utility ($\$1,000,000$), because the event $\textsc{Obs} = \textit{empty}$ has probability $0$ under both policies! If $\argmax_{\pi \in \Pi}$ breaks ties arbitrarily, **P-FDT** is indifferent between one-boxing and two-boxing in the measure-zero event that the agent unexpectedly sees an empty box.

**Operational Proposal (Trembling-Hand / Lexicographic Policy Optimality):** While Yudkowsky and Soares avoid this in Transparent Newcomb by setting predictor accuracy to $1 - \varepsilon = 0.99$, a general decision procedure should not prescribe throwing away $\$1,000$ on an unexpected observation branch merely because its prior probability was zero. We can operationalize this in two equivalent ways:
1. **Strict Positivity (Trembling-Hand Priors):** Require the world-model $(P, G)$ to assign a strictly positive error probability $\varepsilon > 0$ (however small, e.g., cosmic ray noise) to every logically possible observation $x \in \mathcal{X}$ that is not ruled out by the agent's own policy, and take the limit of $\mathrm{PFDT}_{\mathrm{pol}}(P_\varepsilon, G)$ as $\varepsilon \to 0^+$. As shown in Section 3.1, for every $\varepsilon \in (0, 0.99)$, $\pi_{12} = (\textit{1}, \textit{2})$ strictly dominates $\pi_{11} = (\textit{1}, \textit{1})$ by $\$1,000\varepsilon > 0$.
2. **Conditional Sub-Branch Tie-Breaking:** If a set of policies $\Pi^* \subseteq \Pi$ ties on global expected utility in $(\text{P-FDT-1})$, refine $\Pi^*$ by selecting $\pi^* \in \Pi^*$ that maximizes the conditional expected utility $\mathbb{E}[V \mid \textsc{Obs}=x, \mathtt{do}(\textsc{pfdt}=\pi)]$ on any measure-zero observation $x$ whose realization does not subjunctively depend on $\pi(x)$.

### 5.3 Uncertainty 3: Deducing Subjunctive Graphs and Bounding Policy Search

Finally, Yudkowsky and Soares explicitly highlight two foundational open problems in Sections 5, 6, and 10 that carry over directly to **P-FDT**:
* **The Subjunctive Structure Problem:** Equation $(\text{P-FDT-1})$ relies on Pearl's $\mathtt{do}$ operator applied to a graph $G$ that encodes logical and computational dependencies alongside causal ones. Ideally, one would define a logical counterpossible operator $\mathtt{true}(\phi)$ directly on a probability distribution $P$, yielding:
  $$\mathrm{PFDT}^*(P, x) = \left[\argmax_{\pi \in \Pi} \mathbb{E}\left(V \;\middle|\; \mathtt{true}\big(\textsc{pfdt}(\underline{P}) = \pi\big)\right)\right](x).$$
  Because no general formal theory of counterpossible conditioning (conditioning on logically false mathematical statements, such as $\textsc{pfdt}(\underline{P}) = \pi'$ when in fact $\textsc{pfdt}(\underline{P}) = \pi^*$) yet exists, **P-FDT** requires the dependency graph $G$ to be supplied as part of the agent's model. How an agent should systematically learn $G$ for abstract computations from observation and experiment remains a premier open problem.
* **Tractability of $\Pi$:** In **A-FDT**, the agent searches over $|\mathcal{A}|$ actions. In **P-FDT**, the policy space $\mathcal{A}^{\mathcal{X}}$ grows exponentially in $|\mathcal{X}|$. For real-world or bounded AI agents where $\mathcal{X}$ is vast, iterating over all functions $\pi : \mathcal{X} \to \mathcal{A}$ is computationally intractable. Operationalizing **P-FDT** for bounded agents requires either restricting $\Pi$ to a parameterized family of tractable policies $\Pi_\Theta$ (analogous to policy-gradient methods in reinforcement learning) or decomposing $(P, G)$ into independent sub-problems where observations that do not share common predictors or multi-agent links can be optimized locally.

---

## 6. Conclusion

**Policy functional decision theory (P-FDT)**—the formulation identified in Footnotes 7 and 16 of Yudkowsky and Soares's paper as the authors' preferred version of functional decision theory—completes the philosophical transition from local act evaluation to global algorithmic choice. By intervening on the single logical node $\textsc{pfdt}(\underline{P}, \underline{G})$ to select a complete policy $\pi^* : \mathcal{X} \to \mathcal{A}$ and then evaluating $\pi^*(x)$ on the observed input $x$, **P-FDT** retains every advantage of action-based **FDT** over **CDT** and **EDT**: it one-boxes in Newcomb's problem and the transparent Newcomb problem, smokes in the smoking lesion problem, resists extortion in the XOR and mechanical blackmail problems, and stays in Damascus without needing ad-hoc ratification or precommitments.

More importantly, as our formal analysis demonstrates, elevating the unit of subjunctive intervention from point-actions to policies is not merely an aesthetic preference. In single-agent sequential dilemmas, **P-FDT** eliminates nuisance priors over counterfactual observation branches. And in multi-agent dilemmas where copies or twins receive distinct observations, **P-FDT** overcomes the cross-branch coordination failures and prior traps that afflict action-based **FDT**, providing a unified mathematical foundation for rational choice across both decision theory and game theory.

---

## References

* Dai, Wei (2009). "Towards a New Decision Theory." *LessWrong*.
* Gibbard, Allan, and William L. Harper (1978). "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, Vol. 1, 125–162. D. Reidel.
* Joyce, James M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Kleene, Stephen Cole (1938). "On Notation for Ordinal Numbers." *Journal of Symbolic Logic* 3 (4): 150–155.
* Lewis, David (1979). "Prisoners' Dilemma is a Newcomb Problem." *Philosophy & Public Affairs* 8 (3): 235–240.
* Pearl, Judea (1996). "Causation, Action, and Counterfactuals." In *Proceedings of the 6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-'96)*, 51–73.
* Pearl, Judea (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Soares, Nate, and Benja Fallenstein (2015). "Toward Idealized Decision Theory." arXiv:1507.01986.
* Spohn, Wolfgang (1977). "Where Luce and Krantz Do Really Generalize Savage's Decision Model." *Erkenntnis* 11 (1): 113–134.
* Yudkowsky, Eliezer (2010). *Timeless Decision Theory*. The Singularity Institute.
* Yudkowsky, Eliezer, and Nate Soares (2017). "Functional Decision Theory: A New Theory of Instrumental Rationality." Machine Intelligence Research Institute, arXiv:1710.05060v2.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Core Focus**

I'm focusing on clarifying the user's ultimate goal: a comprehensive mathematical essay or technical blog post that explains **P-FDT (policy functional decision theory)** and how to practically use it in decision-making scenarios. I need to fully grasp the necessary depth and breadth of the explanation.


**Clarifying Target Audience**

I'm now zeroing in on the intended readership. They're mathematically capable and want the 'why' behind the 'how' of P-FDT. This means the essay must be rigorous, yet also address the underlying philosophical reasoning. The source text will be the Yudkowsky & Soares paper, with a strong emphasis on the policy-selection concept found in footnote 16 and related footnote 7.


**Refining Content and Structure**

I'm now establishing the content's requirements. It seems I need to construct a coherent account of P-FDT. This will include mathematical definitions, equations, examples, and detailed explanations. I'm aiming for a level of precision that would allow a reader to apply it to unfamiliar cases. I am also working on clearly explaining how P-FDT evaluates alternative actions/policies. Finally, I will consistently use the "P-FDT" terminology throughout the essay.


**Analyzing Dependencies and Scope**

I'm now zeroing in on the importance of relevant dependencies and counterfactuals, drawing a direct link to the need for graphical interventions. I plan to flesh out any gaps or ambiguities in the source material by developing reasonable operational interpretations, and by clearly distinguishing my proposals from the original claims. Also, I'll include multi-agent dilemmas for contrasting against action-based FDT, and use specific examples to make it clear.


**Defining FDT Equations**

I'm now detailing the core equations for Expected Utility (EU) maximization, Evidential Decision Theory (EDT), Causal Decision Theory (CDT), and Standard Functional Decision Theory (FDT). I'm focusing on their respective formulas, including the crucial $\mathtt{do}$ operator and Bayesian conditioning within each. I am giving special attention to how FDT intervenes on the logical output, rather than physical action.


**Elaborating Policy Implications**

I'm now diving into the implications of policy intervention within the FDT framework. I'm focusing on the distinction between action-based and policy-based interventions. The source material highlights the preference for intervening on policies rather than actions themselves, especially in multi-agent scenarios. I am exploring the impact of this approach on the equations, considering examples like the "two-boxing" scenarios to clarify the differences. I am using the observations $x$ from the source to make this more precise.


**Simplifying Scope and Focus**

I'm now narrowing the focus. I'm noting the source's observation that the distinction between action-based and policy-based intervention is only relevant in multi-agent dilemmas, and I have decided to set that aside for now to streamline the exposition. This means I can concentrate on clarifying the core mathematical formalism of P-FDT in a simplified setting. I'm working to define key sets and spaces, which will serve to formalize the equations going forward. Specifically, I'm defining observations and actions. Finally, I will now define a policy as a function from observations to actions, with the policies comprising a functional space.


**Formalizing PFDT Equation**

I'm now clarifying the formal equation for P-FDT policy selection and action execution. The focus is on correctly interpreting "inputs" within the context of the policy function. Does this mean observations $x$, or the tuple $(P, G, x)$? Does it also include world models? I need to precisely define how the agent uses the selected policy $\pi^*$ to derive an action, given the observation $x$.



**Interpreting Policy Inputs**

I'm now carefully analyzing the input ambiguity for the policy function in P-FDT. The source leaves this open! Does the policy function take observations $x$ as input, as in the footnote definition? Or does it take full epistemic inputs, like $(P, G, x)$? It is an opportunity to clarify, distinguish source claims, and add operational definitions. My intention is to focus on both readings and their implications!


**Clarifying Policy Input Ambiguity**

I'm working to reconcile differing interpretations of the policy function's inputs in P-FDT. The policy can accept local inputs or unify preference uncertainty as internal observations. This clarifies distinctions from action-based FDT, and addresses potential issues like the Smoking Lesion problem, potentially unifying the policy into a single node. I will examine how the policy performs in Transparent Newcomb.


**Analyzing Transparent Newcomb**

I'm now diving into the implications of Transparent Newcomb. Action-based FDT focuses on the "full" box observation. I'm exploring how Fiona's uncertainty about the predictor's behavior (represented by $q$) influences her decision, considering potential variations in her utility based on the predictor's choice and the separable nature of the payoffs. My goal is to use this example to solidify P-FDT's response.


**Examining Transparent Newcomb**

I'm now calculating Fiona's optimal policy within P-FDT for Transparent Newcomb. I'm focusing on how she'd evaluate policies, and on the key point: the chosen policy is optimal across all possible observations, avoiding the need for prior beliefs or arbitrary assumptions. I am thinking through the two-box vs. one-box choice for the transparent and opaque observations, respectively.



**Analyzing Twin Dilemma Scenarios**

I'm now crafting a multi-agent dilemma to highlight P-FDT's strengths. I'm developing a "Twin Prisoner's Dilemma with Asymmetric Observations," where each twin only sees their own room. Their actions jointly determine a payoff. I'm working to formalize the payoff matrix and demonstrate how P-FDT can coordinate optimal behavior despite limited information. The goal is to set the equations correctly.


**Formalizing Twin Dilemma**

I'm now formalizing the multi-agent twin prisoner's dilemma, focusing on an action-based FDT perspective with asymmetric observations. Specifically, I'm working to correctly apply the FDT intervention equation (Equation 4) within this setup, noting the distinct FDT nodes governing each twin's decision. I will clarify the implications of intervening on one twin's node without affecting the other's.


**Revising Utility Assumptions**

I'm now carefully re-evaluating the utility framework for the Twin Prisoner's Dilemma. I'm considering scenarios where the agent evaluates global ex-ante utility and the implications of her own utility versus a shared, or combined utility. This leads to the question of the optimal policy for each agent.


**Testing Synergistic Policies**

Now, I'm examining a multi-agent dilemma to highlight P-FDT's coordination ability. This scenario includes two agents, Alice and Bob, who share the same decision function. The payoff depends on their joint actions. They can both pull levers for a large reward, but only if both pull. If only one pulls, that agent loses. This tests how P-FDT enables synergistic behavior.


**Analyzing Coordination Failures**

I'm now focusing on how action-based FDT can fail to coordinate optimal behavior in scenarios like the lever-pulling dilemma. My analysis reveals a self-confirming equilibrium where both agents choose to "Wait," even though the optimal outcome requires both to "Pull." This stems from each agent's inability to influence the other's prior belief about the other agent's action. I will examine how the policy is a coordination trap.


**Clarifying P-FDT Coordination**

I'm now focusing on how P-FDT resolves coordination issues, particularly asymmetric dilemmas. I'm noting that in scenarios with multiple equilibria, P-FDT intervenes on the entire policy, not just individual actions or observations. This prevents prior sensitivity and coordination failures, directly comparing policies like "Pull-Pull" against other combinations, ensuring a guaranteed optimal outcome.



**Evaluating Asymmetric Observations**

I'm now carefully examining an asymmetric, multi-agent Prisoner's Dilemma, considering distinct observations and utilities. Under action-based FDT, an agent's focus on their payoff, given their distinct observation, hinders coordination. This lack of coordination leads to a suboptimal Nash Equilibrium.


**Differentiating Interventions**

I'm now clarifying how interventions on individual agents' policies, based on unique observations, do not affect others in the model. Agent 1's action is controlled by $\textsc{fdt}(\underline{P}, \underline{G}, \textit{North})$, while Agent 2's is based on $\textsc{fdt}(\underline{P}, \underline{G}, \textit{South})$. Therefore, intervening on Agent 1, to save \$1000, does not influence Agent 2.


**Comparing P-FDT Coordination**

I'm currently comparing the behavior of action-based FDT against P-FDT in the North/South Twin Dilemma. With asymmetric observations, action-based FDT still defects. However, P-FDT, given a symmetric prior, yields a mixed strategy with a 50% chance of being in each role, and hence **cooperates**, avoiding the suboptimal Nash equilibrium!


**Calculating Expected Rewards**

I'm now calculating the expected rewards under symmetric and asymmetric conditions in the Twin Stag Hunt. I'm focusing on scenarios where agents must coordinate to receive rewards, and how P-FDT guarantees a favorable outcome through policy evaluation. I'm carefully evaluating how these asymmetric observations impact rewards!



**Evaluating Stag Hunt Policy**

I'm now analyzing the Stag Hunt scenario to demonstrate how policy intervention improves outcomes. Action-based FDT is trapped when the prior belief is small, leading to the $(\textit{Hare}, \textit{Hare})$ equilibrium. However, P-FDT guarantees favorable outcomes through policy evaluation. I'm focusing on the Stag and Hare options.



**Defining Asymmetric Coordination**

I'm now investigating asymmetric coordination with P-FDT in scenarios like the Battle of the Sexes. Since both agents execute actions from the same policy node $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$, intervening to enforce a specific profile, such as $(\pi(\textit{North}), \pi(\textit{South}))$, is straightforward. I'm focusing on the implications of asymmetric coordination on each observation.


**Refining Utility Assumptions**

I'm now carefully re-evaluating the utility framework in complex dilemmas. Considering global, ex-ante utility and individual utility, I'm working through the implications.


**Formalizing P-FDT Equations**

I'm now writing out the core equations for Expected Utility (EU), Evidential Decision Theory (EDT), Causal Decision Theory (CDT), and Standard Functional Decision Theory (FDT). I'm carefully defining their formulas, including the crucial $\mathtt{do}$ operator and Bayesian conditioning within each. A key focus is on how P-FDT intervenes on the logical output, specifically the policy function.


**Defining PFDT Equations**

I'm now detailing formal equations for EU (Eq. 1), EDT (Eq. 2), CDT (Eq. 3), and A-FDT (Eq. 4) from the paper. I'm providing a clear two-stage definition of P-FDT. This will include defining the policy space and the policy node, then explicitly defining the policy optimization via global intervention, and finally, the action execution. I will ensure to explain the mechanics of subjunctive dependence, counterpossibilities, and quining.


**Elaborating Graph Construction**

I'm now detailing graph construction in P-FDT, demonstrating how the graph, $G$, encodes downstream effects from a policy node, affecting the agent's action and external predictor models. The focus is on the link between the selected policy $\pi$ and the eventual actions.



**Analyzing Single-Agent Advantages**

I'm now clarifying the superior single-agent behavior in P-FDT compared to action-based FDT, even when focusing on a single agent. The policy $\pi$ lets the agent optimize actions over all observations simultaneously, removing prior parameter $q$ and simplifying decisions. I'm focusing on Section 6.



**Developing Multi-Agent Dilemma**

I'm working on a formal multi-agent example to highlight P-FDT's advantages, specifically an Asymmetric Twin Stag Hunt. The core issue is the asymmetric information, leading to the risk of "cross-branch Spohn traps" where action-based FDT fails. My plan is to show how each twin's individual decision, based on a distinct observation, might lead to suboptimal outcomes if P-FDT isn't used.


**Clarifying Observation Domains**

I'm now carefully examining the domain ambiguity of policy functions. Does it map observations to actions, or accept a more complex input? Analyzing this clarifies distinctions from action-based FDT and will clarify operational definitions. I will focus on the Smoking Lesion Problem for illustration.


**Analyzing Policy Domains**

I'm now clarifying the domain extension of policy functions within P-FDT. I'm focusing on whether policies take observations or local epistemic inputs. By unifying preference uncertainty into the observation, I aim to create a single P-FDT node, thereby resolving issues like the Smoking Lesion problem. I will also examine measure-zero observation branches.


**Refining Optimization Algorithms**

I'm now focusing on the computational feasibility of P-FDT, especially the size of the policy space. I plan to restrict it for tractability, potentially using lexicographic or trembling-hand optimality. A formal theory of counterfactuals will be needed for the subjunctive structure.


**Refining Accuracy Checks**

I'm now meticulously cross-referencing all direct quotations against the original source to ensure precise accuracy. This includes verifying the wording of key footnotes regarding policy-based intervention, particularly footnotes 7 and 16. I am also working on correctly citing the Joyce quote on differing epistemic perspectives.


```
