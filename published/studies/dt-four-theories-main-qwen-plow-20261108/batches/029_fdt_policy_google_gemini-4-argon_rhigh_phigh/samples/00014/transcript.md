# 029_fdt_policy_google_gemini-4-argon_rhigh_phigh / 00014

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/9c93ea1d-c85d-447f-9a21-298b20d42259/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/9c93ea1d-c85d-447f-9a21-298b20d42259/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Policy Functional Decision Theory (P-FDT): Subjunctive Dependence, Policy Interventions, and Multi-Agent Coordination

## 1. Introduction: From Physical Acts to Mathematical Policies

For half a century, normative decision theory was divided between two rival interpretations of expected utility maximization: Evidential Decision Theory (EDT) and Causal Decision Theory (CDT). When evaluating an available action, an EDT agent asks what the world is likely to be like *conditional* on her taking that action—a rule that enables cooperation in Newcomb’s problem and the psychological twin prisoner’s dilemma, but infamously counsels agents to "manage the news" in medical and blackmail dilemmas where an action is merely a statistical symptom of an undesirable state (Gibbard and Harper 1978; Lewis 1981; Soares and Fallenstein 2015). A CDT agent instead asks what the world would be like if she *causally intervened* on her physical action while holding the past and all causally independent processes fixed—a rule that avoids managing the news in the smoking lesion problem, but leaves agents predictably impoverished in Newcomb’s problem, abandoned in Parfit’s hitchhiker problem, and vulnerable to reflective instability in Death in Damascus (Nozick 1969; Skyrms 1980; Parfit 1986; Joyce 2012).

In *"Functional Decision Theory: A New Theory of Instrumental Rationality"*, Eliezer Yudkowsky and Nate Soares (2017) propose a third paradigm: Functional Decision Theory (FDT). The core philosophical insight of FDT is that a decision-maker should not treat her choice purely as an isolated physical token in space-time, nor as a passive piece of statistical evidence. Instead, she should treat her decision as the logical output of a *fixed mathematical decision function*. When weighing options, the rational agent asks: *"Which output of this very mathematical function would yield the best outcome?"* Because predictors’ simulations of the agent and identical twins’ deliberations compute or represent this same mathematical function, they *subjunctively depend* on its output even when they are causally independent of the agent’s physical body.

Yet in the main text of Yudkowsky and Soares (2017), the formal equation for FDT—which we will refer to as **action-FDT** (or standard FDT) to keep our terminology exact—is presented in a simplified, action-by-action form. Under action-FDT, an agent who has received an observation $x$ intervenes on a mathematical variable representing the output of her decision procedure specifically at input $x$ to select an action $a$. In two crucial footnotes, however, the authors reveal that this action-level equation is merely an expositional simplification of their preferred theory, which we will call **Policy Functional Decision Theory (P-FDT)**. In footnote 7, they write:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

And in footnote 16, after explaining how functional decision theorists respond to observations in blackmail dilemmas, they elaborate:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

Why does intervening on a *policy* rather than an *action* matter, how is **P-FDT** mathematically defined, and how can we apply it to concrete decision problems? In this essay, we construct a rigorous formal account of **P-FDT** based on Yudkowsky and Soares’s framework, compare its mechanics to EDT, CDT, and action-FDT, demonstrate exactly how and why **P-FDT** diverges from action-FDT in multi-agent dilemmas with dispersed information, and resolve several foundational questions that footnote 16 leaves open.

---

## 2. Formalizing P-FDT and Its Rivals

### 2.1 The Expected Utility Scaffolding

Following Gibbard and Harper (1978) and Joyce (1999), EDT, CDT, action-FDT, and **P-FDT** all share a common expected utility scaffolding. Let $\mathcal{O} = \{o_1, o_2, \dots\}$ be a countable set of outcomes, $\mathcal{A}$ be a finite set of available physical actions, $\mathcal{X}$ be a countable set of possible observation histories, and $\mathcal{U}: \mathcal{O} \to \mathbb{R}$ be a bounded utility function. An expected utility maximizer who has observed $x \in \mathcal{X}$ seeks to maximize

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j), \tag{1}$$

where $P(a \hookrightarrow o_j ;\, x)$ denotes the probability assigned to outcome $o_j$ in the hypothetical scenario where action $a$ is taken given observation $x$. As Joyce (1999) observes, "decision theories should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated." Different decision theories correspond to different rules for representing the agent’s world-model $M$ and constructing hypotheticals $M^{a\hookrightarrow}$ from $M$.

Let $\textsc{Obs}$ be an $\mathcal{X}$-valued random variable representing the agent’s observation, $\textsc{Act}$ be an $\mathcal{A}$-valued random variable representing her physical action, $\textsc{Outcome}$ be an $\mathcal{O}$-valued random variable, and $\textsc{V} \coloneqq \mathcal{U}(\textsc{Outcome})$ be the resulting utility. Writing $\mathbb{E}$ for expectation with respect to the agent’s probability distribution $P$, the three baseline theories in Yudkowsky and Soares (2017) are formalized as follows:

1. **Evidential Decision Theory (EDT)**: The world-model is a probability distribution $P$, and hypotheticals are formed by standard Bayesian conditioning on both observation and action:
   $$\mathrm{EDT}(P, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs} = x, \textsc{Act} = a\right). \tag{2}$$

2. **Causal Decision Theory (CDT)**: The world-model is a Pearlian causal model $(P, G)$, where $G$ is a directed acyclic graph encoding causal dependencies among variables in $P$ (Pearl 1996, 2000). Hypotheticals are formed by conditioning on the observation $\textsc{Obs} = x$ and applying Pearl’s $\mathtt{do}$-operator to sever $\textsc{Act}$ from its causal ancestors:
   $$\mathrm{CDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{Act} = a), \textsc{Obs} = x\right). \tag{3}$$

3. **Action-Based Functional Decision Theory (action-FDT)**: The world-model $(P, G)$ is an extended dependency model in which $P$ includes variables for the outputs of mathematical functions and $G$ encodes both causal and *subjunctive* (logical/computational) dependencies. Rather than intervening on the physical node $\textsc{Act}$ or conditioning $P$ on $\textsc{Obs} = x$, action-FDT intervenes on the logical node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ representing the output of the $\mathrm{FDT}$ algorithm on inputs $(P, G, x)$ (where underlines denote dequoting the values of the arguments into the variable name):
   $$\mathrm{FDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right). \tag{4}$$

### 2.2 The Mathematical Definition of P-FDT

To move from action-FDT in Equation (4) to **P-FDT** as described in footnotes 7 and 16, we shift the target of the logical intervention from an individual action $a \in \mathcal{A}$ to an entire *policy* $\pi$.

*(Note on source vs. formal completion: Yudkowsky and Soares state the verbal procedure for **P-FDT** in footnotes 7 and 16, but omit its explicit algebraic and graphical equations. The formalization below is our mathematical operationalization of their description.)*

**Definition 1 (Policy Space).** Given a finite set of relevant observations $\mathcal{X}$ and a finite set of actions $\mathcal{A}$, a *policy* is a total function $\pi: \mathcal{X} \to \mathcal{A}$ mapping each possible observation $x \in \mathcal{X}$ to an action $\pi(x) \in \mathcal{A}$. The policy space is the function space $\Pi \coloneqq \mathcal{A}^{\mathcal{X}}$, which has cardinality $|\Pi| = |\mathcal{A}|^{|\mathcal{X}|}$.

**Definition 2 (P-FDT Dependency Model).** A **P-FDT** world-model is a pair $(P, G)$ where:
* $P$ is a probability distribution over a set of random variables that includes $\textsc{Obs} \in \mathcal{X}$, $\textsc{Act} \in \mathcal{A}$, $\textsc{V} \in \mathbb{R}$, environmental variables (such as predictors’ predictions or other agents’ actions), and a logical variable $\textsc{pfdt}(\underline{P}, \underline{G})$ taking values in the policy space $\Pi$.
* $G$ is a directed acyclic graph encoding all causal and subjunctive dependencies among these variables. Specifically:
  1. In $G$, the agent’s physical action node $\textsc{Act}$ has incoming arrows from both the policy node $\textsc{pfdt}(\underline{P}, \underline{G})$ and the observation node $\textsc{Obs}$. Provided the agent’s physical hardware executes her decision procedure without error, the structural equation for $\textsc{Act}$ is simply function evaluation:
     $$\textsc{Act}(\pi, x) \coloneqq \pi(x). \tag{5}$$
  2. Any external system (such as a predictor, blackmailer, or psychological twin) whose behavior subjunctively depends on the agent’s decision algorithm has a corresponding node in $G$ with an incoming arrow from $\textsc{pfdt}(\underline{P}, \underline{G})$.

**Definition 3 (The P-FDT Decision Rule).** When an agent with world-model $(P, G)$ observes $x \in \mathcal{X}$, **P-FDT** selects an action in two steps:
1. **Policy Selection (Global Intervention):** The agent identifies the optimal policy $\pi^* \in \Pi$ by intervening on the logical node $\textsc{pfdt}(\underline{P}, \underline{G})$ and maximizing unconditional expected utility:
   $$\Pi^*(P, G) \coloneqq \operatorname*{argmax}_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right). \tag{6}$$
2. **Policy Application (Local Evaluation):** The agent applies the selected policy $\pi^* = \Pi^*(P, G)$ to her actual observation $x$ to output her physical action:
   $$\mathrm{PFDT}(P, G, x) \coloneqq \Pi^*(P, G)(x) = \left[ \operatorname*{argmax}_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right) \right](x). \tag{7}$$

### 2.3 Subjunctive Dependencies, Counterpossibles, and "Updatelessness"

Three structural features of Equations (5)–(7) deserve immediate attention.

First, like action-FDT, **P-FDT** relies on *counterpossible* reasoning. Because $\Pi^*(P, G)$ is a deterministic mathematical function, there is only one policy $\pi^*$ that it outputs of logical necessity, just as $6288 + 1048 = 7336$ of necessity. When a **P-FDT** agent evaluates $\mathbb{E}(\textsc{V} \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi))$ for each candidate $\pi \in \Pi$, she uses the graph $G$ to propagate how the world—including any predictors or twins that compute or simulate $\Pi^*(P, G)$—would behave if, counterpossibly, her policy-selection function evaluated to $\pi$.

Second, **P-FDT** replaces a family of observation-indexed logical nodes with a *single* policy node. In action-FDT, if an agent can observe either $x_1$ or $x_2$, her graph $G^F$ must contain two separate logical nodes, $\textsc{fdt}(\underline{P}, \underline{G}, x_1)$ and $\textsc{fdt}(\underline{P}, \underline{G}, x_2)$, and upon observing $x_1$ she intervenes *only* on $\textsc{fdt}(\underline{P}, \underline{G}, x_1)$. In **P-FDT**, there is only one logical node $\textsc{pfdt}(\underline{P}, \underline{G})$ representing the entire mapping $\pi: \mathcal{X} \to \mathcal{A}$. Intervening on $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$ simultaneously fixes $\pi(x)$ for every $x \in \mathcal{X}$.

Third, notice how **P-FDT** handles observations. In Equation (6), the expectation $\mathbb{E}(\textsc{V} \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi))$ is computed with respect to the *prior* (unconditioned) distribution $P$, not the posterior distribution $P(- \mid \textsc{Obs} = x)$. Why? Because in dilemmas where a predictor’s action determines what the agent observes (such as the transparent Newcomb problem or mechanical blackmail), the observation $\textsc{Obs}$ is *subjunctively downstream* of the agent’s policy $\pi$. Conditioning on $\textsc{Obs} = x$ during policy evaluation would prevent the agent from recognizing that adopting a different policy $\pi'$ would have caused her to receive a different observation $x'$. As Yudkowsky and Soares note in Section 9, this refusal to condition on $\textsc{Obs}$ during policy evaluation originates in Wei Dai’s (2009) Updateless Decision Theory (UDT), whereas Eliezer Yudkowsky’s (2010) earlier Timeless Decision Theory (TDT) conditioned on $\textsc{Obs} = x$ while also intervening on the decision node, creating a harmful "double update." In **P-FDT**, the observation $x$ plays no role in constructing the hypothetical distributions; it enters solely in Equation (7), where the agent feeds $x$ into the globally optimal policy $\pi^*$ to determine $\pi^*(x)$.

*(Technical note on the source text: In Section 6 of Yudkowsky and Soares [2017], an inline formula for the transparent Newcomb problem contains a typographical artifact, $\mathbb{E}(\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = a, \textsc{Obs} = \mathit{full})$. However, the authors’ explicit definition in Equation (4), their prose in Section 5 and Section 9, and the numerical calculation immediately following that formula—which averages over the 99% full-box branch and the 1% empty-box branch—confirm that no conditioning or intervention on $\textsc{Obs} = \mathit{full}$ takes place.)*

---

## 3. Applying P-FDT to Single-Agent Dilemmas: Transparent Newcomb and Mechanical Blackmail

To see how **P-FDT** operates in practice—and why Yudkowsky and Soares remark that replacing action-FDT with **P-FDT** "will not make a difference in this paper"—let us apply **P-FDT** step by step to the **Transparent Newcomb Problem** (Drescher 2006; Section 4 and Section 6 of Yudkowsky and Soares 2017).

### 3.1 Problem Setup and P-FDT Graph

In the Transparent Newcomb Problem, both Box A (\$1,000) and Box B (\$1,000,000 or \$0) are transparent. A predictor with 99% accuracy ($\textsc{Accurate} = \mathit{accurate}$ with probability $0.99$, $\mathit{inaccurate}$ with probability $0.01$) places \$1,000,000 in Box B if and only if she predicts that the agent will leave Box A behind ($\mathit{onebox}$) upon observing that Box B is $\mathit{full}$. Suppose our **P-FDT** agent, Fiona, walks into the room and observes $\textsc{Obs} = \mathit{full}$. What does **P-FDT** prescribe?

Let the observation space be $\mathcal{X} = \{\mathit{full}, \mathit{empty}\}$ and the action space be $\mathcal{A} = \{\mathit{onebox}, \mathit{twobox}\}$ (abbreviated $1$ and $2$). There are $|\Pi| = 2^2 = 4$ possible policies, which we can write as ordered pairs $\pi = (\pi(\mathit{full}), \pi(\mathit{empty}))$:
$$\Pi = \{ (1, 1),\, (1, 2),\, (2, 1),\, (2, 2) \}.$$

In Fiona’s **P-FDT** dependency graph $G^F$, the variables and structural equations are:
* $\textsc{pfdt}(\underline{P^F}, \underline{G^F}) \in \Pi$: the logical node representing Fiona’s policy-selection function.
* $\textsc{Accurate} \in \{\mathit{accurate}, \mathit{inaccurate}\}$: an exogenous node with $P^F(\mathit{accurate}) = 0.99$ and $P^F(\mathit{inaccurate}) = 0.01$.
* $\textsc{Prediction} \in \{1, 2\}$: the predictor simulates Fiona’s response to seeing a full box, which depends on $\pi(\mathit{full})$:
  $$\textsc{Prediction}(\pi, \mathit{accurate}) = \pi(\mathit{full}), \qquad \textsc{Prediction}(\pi, \mathit{inaccurate}) = \neg \pi(\mathit{full}),$$
  where $\neg 1 = 2$ and $\neg 2 = 1$.
* $\textsc{Box B} \in \{\mathit{full}, \mathit{empty}\}$ and $\textsc{Obs} \in \{\mathit{full}, \mathit{empty}\}$: determined by $\textsc{Prediction}$, with $\textsc{Obs} = \textsc{Box B} = \mathit{full}$ if $\textsc{Prediction} = 1$, and $\mathit{empty}$ if $\textsc{Prediction} = 2$.
* $\textsc{Act} \in \{1, 2\}$: determined by evaluating the policy at the observation, $\textsc{Act}(\pi, \textsc{Obs}) = \pi(\textsc{Obs})$.
* $\textsc{V} \in \mathbb{R}$: yields $\$1,000,000 \cdot \mathbb{I}(\textsc{Box B} = \mathit{full}) + \$1,000 \cdot \mathbb{I}(\textsc{Act} = 2)$.

### 3.2 Evaluating the Policies

Following Equation (6), Fiona intervenes on $\textsc{pfdt}(\underline{P^F}, \underline{G^F}) = \pi$ for each of the four candidate policies in $\Pi$. For any policy $\pi = (\pi(\mathit{full}), \pi(\mathit{empty}))$, we can write the expected utility in closed form by summing over the two states of $\textsc{Accurate}$:

1. **If $\pi(\mathit{full}) = 1$ (policies $(1, 1)$ and $(1, 2)$)**:
   * With probability $0.99$ ($\mathit{accurate}$), $\textsc{Prediction} = 1$, so $\textsc{Box B} = \textsc{Obs} = \mathit{full}$. Fiona executes $\textsc{Act} = \pi(\mathit{full}) = 1$ and receives $\$1,000,000$.
   * With probability $0.01$ ($\mathit{inaccurate}$), $\textsc{Prediction} = 2$, so $\textsc{Box B} = \textsc{Obs} = \mathit{empty}$. Fiona executes $\textsc{Act} = \pi(\mathit{empty})$ and receives $\$1,000 \cdot \mathbb{I}(\pi(\mathit{empty}) = 2)$.
   * Thus:
     $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt} = (1, 1))\right] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000,$$
     $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt} = (1, 2))\right] = 0.99(\$1,000,000) + 0.01(\$1,000) = \$990,010.$$

2. **If $\pi(\mathit{full}) = 2$ (policies $(2, 1)$ and $(2, 2)$)**:
   * With probability $0.99$ ($\mathit{accurate}$), $\textsc{Prediction} = 2$, so $\textsc{Box B} = \textsc{Obs} = \mathit{empty}$. Fiona executes $\textsc{Act} = \pi(\mathit{empty})$ and receives $\$1,000 \cdot \mathbb{I}(\pi(\mathit{empty}) = 2)$.
   * With probability $0.01$ ($\mathit{inaccurate}$), $\textsc{Prediction} = 1$, so $\textsc{Box B} = \textsc{Obs} = \mathit{full}$. Fiona executes $\textsc{Act} = \pi(\mathit{full}) = 2$ and receives $\$1,001,000$.
   * Thus:
     $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt} = (2, 1))\right] = 0.01(\$1,001,000) + 0.99(\$0) = \$10,010,$$
     $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt} = (2, 2))\right] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$

Comparing all four policies, the unique global maximizer is $\pi^* = (1, 2)$—the policy that one-boxes when Box B is full and two-boxes when Box B is empty—achieving $\$990,010$ in expectation. Finally, by Equation (7), Fiona applies $\pi^*$ to her actual observation $x = \mathit{full}$:

$$\mathrm{PFDT}(P^F, G^F, \mathit{full}) = \pi^*(\mathit{full}) = 1 \text{ (one-box)}.$$

### 3.3 Why P-FDT Is Cleaner Than Action-FDT Even in Single-Agent Dilemmas

Compare this **P-FDT** derivation with the action-FDT derivation in Section 6 of Yudkowsky and Soares (2017). Under action-FDT, when Fiona sees $\mathit{full}$, she intervenes only on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$ and must treat her own behavior in the empty-box branch, $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$, as an unknown random variable with some prior probability $q = P^F(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty}) = 2)$. Her expected utilities under action-FDT are $\$990,000 + \$10q$ for one-boxing and $\$10,010 + \$990q$ for two-boxing.

In the Transparent Newcomb Problem (and likewise in Mechanical Blackmail), both theories prescribe the same action because for *every* $q \in [0, 1]$, $\$990,000 + \$10q > \$10,010 + \$990q$. Yet **P-FDT** eliminates the awkward epistemic parameter $q$ altogether. Instead of treating her own algorithm’s output at other observations as a random variable that she must guess via a prior $P^F$, a **P-FDT** agent directly optimizes her policy across all observations at once, immediately recovering $q = 1$ ($\pi^*(\mathit{empty}) = 2$) as part of the joint solution $\pi^* = (1, 2)$.

---

## 4. Where P-FDT Diverges from Action-FDT: Multi-Agent Dilemmas

Why do Yudkowsky and Soares state in footnotes 7 and 16 that choosing a policy rather than an action "makes a difference in certain multi-agent dilemmas"? We can now give a precise mathematical answer.

### 4.1 The Mathematical Condition for Divergence

Suppose an decision environment involves two possible observations, $\mathcal{X} = \{x_1, x_2\}$. Let $U(a_1, a_2)$ denote the agent’s unconditional expected utility when her algorithm outputs $a_1 \in \mathcal{A}$ upon observing $x_1$ and $a_2 \in \mathcal{A}$ upon observing $x_2$:

$$U(a_1, a_2) \coloneqq \mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = (a_1, a_2)\right)\right]. \tag{8}$$

* **Under P-FDT**, an agent observing $x_1$ solves the joint optimization problem
  $$(a_1^*, a_2^*) = \operatorname*{argmax}_{(a_1, a_2) \in \mathcal{A}^2} U(a_1, a_2)$$
  and executes $a_1^*$.
* **Under action-FDT**, an agent observing $x_1$ intervenes *only* on $F_1 \coloneqq \textsc{fdt}(\underline{P}, \underline{G}, x_1) = a_1$, leaving $F_2 \coloneqq \textsc{fdt}(\underline{P}, \underline{G}, x_2)$ distributed according to her prior $P(F_2 = a_2)$. She therefore solves the marginal problem:
  $$a_1^{\text{act}} = \operatorname*{argmax}_{a_1 \in \mathcal{A}} \sum_{a_2 \in \mathcal{A}} P(F_2 = a_2) \, U(a_1, a_2). \tag{9}$$

Whenever $U(a_1, a_2)$ is additively separable—i.e., $U(a_1, a_2) = u_1(a_1) + u_2(a_2)$—or whenever $a_1^*$ strictly dominates all other actions across every possible value of $a_2$ (as in Transparent Newcomb), Equations (8) and (9) are guaranteed to select the same action $a_1^*$ regardless of the prior $P(F_2)$.

However, in multi-agent dilemmas where two or more copies of an agent (or an agent and a symmetric partner) implement the same decision algorithm $(P, G)$ but receive *different observations* $x_1$ and $x_2$, the payoff $U(a_1, a_2)$ generically contains strong cross-terms between $a_1$ and $a_2$. In that regime, action-FDT treats the twin who observed $x_2$ in the exact way CDT treats a twin in the Prisoner's Dilemma: because $F_2 = \textsc{fdt}(\underline{P}, \underline{G}, x_2)$ is a *different node* from $F_1 = \textsc{fdt}(\underline{P}, \underline{G}, x_1)$, intervening on $F_1$ does not change $F_2$! Consequently, action-FDT re-introduces the very pathology for which Yudkowsky and Soares criticize EDT in Section 6 and Section 7 (such as the Cosmic Ray Problem): the agent’s decision becomes trapped by her prior beliefs $P(F_2)$ about what she will do at other observations. **P-FDT** cures this pathology by intervening on the shared policy $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$.

### 4.2 Worked Example 1: The Two-Room Twin Joint Project (Asymmetric Stag Hunt)

Consider the following multi-agent dilemma:

> **Dilemma 1 (The Two-Room Twin Joint Project).** An agent and her perfect psychological twin (who share the exact same world-model $(P, G)$ and decision algorithm) are placed in separate rooms: one is placed in Room A and observes $\textsc{Obs} = A$, while the other is placed in Room B and observes $\textsc{Obs} = B$ (each twin has a 50% prior probability of being the one in Room A vs. Room B). Each twin must independently choose whether to $\mathit{Work}$ on a joint scientific project (incurring a personal effort cost equivalent to $\$10,000$) or $\mathit{Shirk}$ (incurring $\$0$ cost). Room A and Room B control complementary halves of the experiment: the project succeeds, paying $\$1,000,000$ to *each* twin, **if and only if both the twin in Room A and the twin in Room B choose $\mathit{Work}$**. Suppose Fiona wakes up and observes that she is in Room A ($\textsc{Obs} = A$). Should she $\mathit{Work}$ or $\mathit{Shirk}$?

Let us compare the four decision theories on this dilemma:

* **CDT**: Carl reasons that his physical action in Room A has no causal effect on his twin’s action in Room B. Even if he were certain his twin in Room B would work, working would pay off; if he is sufficiently uncertain or has ratified a pessimistic belief that his twin will shirk, he shirks. Worse, if the effort cost is paid only when the other twin *doesn't* cover for him, or in a standard Prisoner's Dilemma payoff structure across rooms, CDT defects unconditionally.
* **Action-FDT**: Under action-FDT, Fiona’s graph contains two separate logical nodes: $F_A = \textsc{fdt}(\underline{P^F}, \underline{G^F}, A)$ (which controls whichever twin is in Room A) and $F_B = \textsc{fdt}(\underline{P^F}, \underline{G^F}, B)$ (which controls whichever twin is in Room B).
  When Fiona observes $\textsc{Obs} = A$, Equation (4) tells her to intervene *only* on $F_A$, holding her prior distribution over $F_B$ fixed. Let $q = P^F(F_B = \mathit{Work})$ be Fiona’s prior probability that her algorithm outputs $\mathit{Work}$ on input $B$.
  * Under $\mathtt{do}(F_A = \mathit{Work})$, the project succeeds if and only if $F_B = \mathit{Work}$ (probability $q$). Since Fiona has a 50% prior chance of being the twin in Room A (where she works for sure) and a 50% prior chance of being the twin in Room B (where she works with probability $q$), her expected utility is:
    $$\mathbb{E}[\textsc{V} \mid \mathtt{do}(F_A = \mathit{Work})] = q(\$1,000,000) - 0.5(\$10,000) - 0.5q(\$10,000) = \$995,000q - \$5,000.$$
  * Under $\mathtt{do}(F_A = \mathit{Shirk})$, the project never succeeds ($0$ probability), and Fiona only pays the effort cost if she is in Room B and $F_B = \mathit{Work}$:
    $$\mathbb{E}[\textsc{V} \mid \mathtt{do}(F_A = \mathit{Shirk})] = -\$5,000q.$$
  Notice that $\mathbb{E}[\textsc{V} \mid \mathtt{do}(F_A = \mathit{Work})] > \mathbb{E}[\textsc{V} \mid \mathtt{do}(F_A = \mathit{Shirk})]$ if and only if $\$1,000,000q > \$5,000$, i.e., $q > 0.005$.
  What if Fiona starts with a pessimistic prior $q < 0.005$ (for instance, $q = 0$, believing she is the sort of agent who shirks in Room B, just as Eve in Section 7 of Yudkowsky and Soares [2017] believes she is the sort of agent who takes \$1 in the Cosmic Ray Problem)? Then action-FDT outputs $\mathit{Shirk}$ in Room A! And by the exact same calculation, if she also assigns prior $< 0.005$ to working in Room A, action-FDT outputs $\mathit{Shirk}$ in Room B. Both twins shirk, their pessimistic priors are completely confirmed upon reflection, and they walk away with $\$0$.

* **P-FDT**: Now consider Fiona following **P-FDT**. Her graph $G^F$ has a *single* policy node $\textsc{pfdt}(\underline{P^F}, \underline{G^F}) \in \{\mathit{Work}, \mathit{Shirk}\}^{\{A, B\}}$, which controls *both* the twin in Room A (via $\pi(A)$) and the twin in Room B (via $\pi(B)$).
  Fiona evaluates all four policies $\pi = (\pi(A), \pi(B))$ via Equation (6):
  1. $\pi = (\mathit{Work}, \mathit{Work})$: Both twins work, the project succeeds with certainty, and Fiona pays the $\$10,000$ effort cost in whichever room she occupies:
     $$\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = (\mathit{Work}, \mathit{Work}))] = \$1,000,000 - \$10,000 = \$990,000.$$
  2. $\pi = (\mathit{Work}, \mathit{Shirk})$ or $(\mathit{Shirk}, \mathit{Work})$: Only one twin works (50% chance it is Fiona), so the project fails:
     $$\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = (\mathit{Work}, \mathit{Shirk}))] = \mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = (\mathit{Shirk}, \mathit{Work}))] = -\$5,000.$$
  3. $\pi = (\mathit{Shirk}, \mathit{Shirk})$: Neither twin works, and the project fails:
     $$\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = (\mathit{Shirk}, \mathit{Shirk}))] = \$0.$$
  Regardless of any prior beliefs about her own outputs, **P-FDT** uniquely selects the policy $\pi^* = (\mathit{Work}, \mathit{Work})$. Evaluating $\pi^*(A) = \mathit{Work}$ in Room A (and $\pi^*(B) = \mathit{Work}$ in Room B), both **P-FDT** twins work and walk away with $\$990,000$.

### 4.3 Worked Example 2: Multi-Option Coordination Under Uninformative Priors

The divergence between **P-FDT** and action-FDT is even starker when twins must coordinate on one of $K$ specialized tasks across rooms without a pre-ratified prior:

> **Dilemma 2 (Asymmetric Twin Division of Labor).** As in Dilemma 1, two identical twins are placed in Room A and Room B. To unlock the $\$1,000,000$ prize, the twin in Room A must select a radio frequency $k \in \{1, 2, \dots, 100\}$ *and* the twin in Room B must select the matching decryption key $k \in \{1, 2, \dots, 100\}$ (or alternatively, opting out for $\$0$, whereas attempting any frequency/key $k$ costs $\$20,000$). Frequency-key pair $k = 1$ has a slight bonus of $+\$100$ over $k \in \{2, \dots, 100\}$.

Suppose that before solving the decision problem, a twin has a symmetric, uninformative prior over what her algorithm outputs in the other room: $P(F_B = k) = 1/100$ for each $k \in \{1, \dots, 100\}$.
* Under **action-FDT**, when the twin in Room A intervenes on $F_A = k$, she treats $F_B$ as fixed to her prior $P(F_B)$. Thus, she calculates that choosing any frequency $k$ has only a $1/100$ chance of matching Room B, yielding an expected gross return of $\frac{1}{100}(\$1,000,100) \approx \$10,001$, which is less than the $\$20,000$ cost of attempting the transmission! Action-FDT therefore **opts out**, getting $\$0$.
* Under **P-FDT**, the agent intervenes on the joint policy $\pi = (\pi(A), \pi(B))$. For any matched policy $\pi_k = (k, k)$, the two twins match with probability $1$! Comparing all policies in $\Pi$, $\pi^* = (1, 1)$ achieves $\$1,000,100 - \$20,000 = \$980,100$, so both twins immediately coordinate on $k = 1$.

---

## 5. Open Questions and Operational Completions of P-FDT

Because Yudkowsky and Soares (2017) introduce **P-FDT** only briefly in footnotes 7 and 16, several crucial technical questions remain unresolved in the source text. To make **P-FDT** fully operational for unfamiliar cases, we must identify these ambiguities and formulate explicit mathematical resolutions. *(The analysis and proposals in this section go beyond the explicit claims of Yudkowsky and Soares [2017].)*

### 5.1 What Is the Domain of a Policy? Observations $\mathcal{X}$ vs. Full Inputs $(\mathcal{M} \times \mathcal{X})$

Look closely at the wording of the two footnotes in the source text:
* Footnote 7 defines policies as *"mappings from observations to actions"* ($\pi: \mathcal{X} \to \mathcal{A}$).
* Footnote 16 states that **P-FDT** chooses *"a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action."*

In Equation (4) of the paper, the inputs to the decision procedure are not just the observation $x \in \mathcal{X}$, but the full triple $(P, G, x)$—that is, the world-model $M = (P, G) \in \mathcal{M}$ together with the observation $x \in \mathcal{X}$. This raises a foundational question: does a **P-FDT** policy have domain $\mathcal{X}$ (with $(P, G)$ held fixed as parameters of the node $\textsc{pfdt}(\underline{P}, \underline{G})$), or does it have domain $\mathcal{M} \times \mathcal{X}$ (intervening on a single parameterless node $\textsc{pfdt}$ that maps $(P, G, x) \mapsto a$)?

**When the distinction matters:**
1. **Single-agent uncertainty about one’s own world-model/preferences:** Recall the **Smoking Lesion Problem** in Section 6 of Yudkowsky and Soares (2017). To formalize why the lesion causes the agent to love smoking, the authors introduce two distributions, $P_S^F$ (representing utility function $\mathcal{U}_S$) and $P_R^F$ (representing $\mathcal{U}_R$), and place two separate nodes in Fiona’s graph (Figure 4): $\textsc{fdt}(\underline{P_S^F}, \underline{G^F})$ and $\textsc{fdt}(\underline{P_R^F}, \underline{G^F})$. If **P-FDT** policies have domain $\mathcal{X}$, these two nodes remain separate because their model argument $\underline{P}$ differs, and a smoker-Fiona intervenes only on $\textsc{pfdt}(\underline{P_S^F}, \underline{G^F})$ while using a prior $q$ for $\textsc{pfdt}(\underline{P_R^F}, \underline{G^F})$. By contrast, if a policy is a meta-policy $\Psi: \mathcal{M} \times \mathcal{X} \to \mathcal{A}$, Fiona chooses how both $(P_S^F, G^F)$ and $(P_R^F, G^F)$ map to actions—evaluating the entire meta-policy $\Psi$ according to her actual utility function $\mathcal{U}_S$! (Notice a subtle pitfall here: if smoker-Fiona were to choose the branch for non-smoker-Fiona $\Psi(P_R^F, G^F)$ using $\mathcal{U}_S$, she would counterfactually want non-smoker-Fiona to smoke too, even though a real non-smoker-Fiona maximizes $\mathcal{U}_R$!)
2. **Multi-agent games with asymmetric priors/models:** If two agents run the same **P-FDT** source code $\mathrm{PFDT}$, but received slightly different prior training data so that Agent 1 has world-model $M_1$ and Agent 2 has world-model $M_2$, intervening on $\textsc{pfdt}(\underline{M_1})$ will not coordinate with $\textsc{pfdt}(\underline{M_2})$ unless the intervention occurs at the level of the shared source function $\textsc{pfdt}: \mathcal{M} \times \mathcal{X} \to \mathcal{A}$ (evaluated under a common veil-of-ignorance prior before $M_1$ and $M_2$ branched).

**Operational Proposal:** When applying **P-FDT** to standard decision problems where the agent’s world-model $(P, G)$ and utility function $\mathcal{U}$ are fixed and common knowledge among symmetric copies, **Definition 1 ($\pi: \mathcal{X} \to \mathcal{A}$ with node $\textsc{pfdt}(\underline{P}, \underline{G})$)** is the right operational default. It avoids cross-utility conflicts when preferences differ (as in the Smoking Lesion Problem) while capturing all multi-observation and multi-agent coordination for agents sharing $(P, G)$. When agents differ only in information acquired *after* a shared epistemic prior $P_0$, one should model all post-$P_0$ information—including which room or role an agent occupies—as part of the observation $x \in \mathcal{X}$ rather than baking it into distinct priors $P_1 \neq P_2$.

### 5.2 Zero-Probability Observations and Trembling-Hand Refinement

A second operational puzzle arises in sequential dilemmas with *infallible* predictors. Consider **The Mechanical Blackmail** (Section 9 of Yudkowsky and Soares 2017) or the **Transparent Newcomb Problem** when the predictor is 100% accurate ($P(\textsc{Accurate} = \mathit{accurate}) = 1$).

In Transparent Newcomb with a 100% accurate predictor, if Fiona chooses any policy $\pi$ with $\pi(\mathit{full}) = \mathit{onebox}$, then the predictor *always* fills Box B. Consequently, under $\mathtt{do}(\textsc{pfdt}(\underline{P^F}, \underline{G^F}) = \pi)$, the event $\textsc{Obs} = \mathit{empty}$ has probability **zero**! As a result, the two policies $\pi_1 = (\mathit{onebox}, \mathit{twobox})$ and $\pi_2 = (\mathit{onebox}, \mathit{onebox})$ yield the exact same unconditional expected utility:
$$\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = (1, 2))] = \mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = (1, 1))] = \$1,000,000.$$
If by some miracle Box B were empty, raw Equation (6) would be indifferent between one-boxing and two-boxing on the empty box! Even more acutely, in a game where an infallible predictor prevents observation $x_0$ from ever occurring under optimal play, how should **P-FDT** specify $\pi^*(x_0)$ if $x_0$ is unexpectedly observed?

**Operational Proposal (Trembling-Hand / $\varepsilon$-Perturbation):** Notice that in Sections 2, 4, 6, and 9, Yudkowsky and Soares consistently assign predictors an accuracy of $1 - \varepsilon = 0.99$ (or $1 - 0.0009$ in Section 9) rather than $1$. We can elevate this modeling choice into a formal refinement of **P-FDT** analogous to Reinhard Selten’s trembling-hand perfection in game theory:
* Whenever an observation $x \in \mathcal{X}$ has probability $0$ under $(P, G)$ for a candidate policy, evaluate policies in the limit as independent error/tremble probabilities $\varepsilon \to 0^+$ on all causal and predictive mechanisms in $G$:
  $$\Pi_{\text{perf}}^*(P, G) \coloneqq \lim_{\varepsilon \to 0^+} \operatorname*{argmax}_{\pi \in \Pi} \mathbb{E}_{P_\varepsilon}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right). \tag{10}$$
Because $P_\varepsilon(\textsc{Obs} = x \mid \mathtt{do}(\textsc{pfdt} = \pi)) > 0$ for every $x \in \mathcal{X}$ whenever $\varepsilon > 0$, Equation (10) uniquely selects $\pi^* = (\mathit{onebox}, \mathit{twobox})$ even in the infallible limit $\varepsilon \to 0^+$.

### 5.3 Deterministic Tie-Breaking and Graphical Construction

Finally, in symmetric coordination games—for instance, if two **P-FDT** twins in Room A and Room B must choose the same color from $\{\mathit{Red}, \mathit{Blue}\}$ where $(\mathit{Red}, \mathit{Red})$ and $(\mathit{Blue}, \mathit{Blue})$ both yield $\$1,000,000$—the $\operatorname*{argmax}_{\pi \in \Pi}$ in Equation (6) returns a set of two tied policies. If each twin broke ties using an independent physical randomizer after running $\Pi^*(P, G)$, they would fail to coordinate 50% of the time. To preserve subjunctive coordination across twins, $\operatorname*{argmax}_{\pi \in \Pi}$ in Equation (6) must be equipped with a *canonical lexicographic tie-breaking rule* over $\Pi$, so that $\Pi^*(P, G)$ is a single-valued mathematical function.

Of course, the deepest open problem identified by Yudkowsky and Soares in Section 5 and Section 10 remains just as pressing for **P-FDT**: whereas Pearl (2000) provides a rigorous methodology for learning causal graphs from empirical interventions, we do not yet have a general algorithmic theory for deducing the subjunctive dependency graph $G$—showing exactly which external systems depend on $\textsc{pfdt}(\underline{P}, \underline{G})$ and how—from raw observations.

---

## 6. Summary Recipe: How to Apply P-FDT to an Unfamiliar Case

To decide any unfamiliar decision problem using **P-FDT**, apply the following five-step procedure:

1. **Specify Spaces:** Identify the finite action space $\mathcal{A}$, the relevant observation space $\mathcal{X}$ (including any role or signal distinctions among symmetric agents), and the policy space $\Pi = \mathcal{A}^{\mathcal{X}}$.
2. **Construct the Dependency Graph $G$:** Introduce a single policy node $\textsc{pfdt}(\underline{P}, \underline{G}) \in \Pi$. Draw arrows from $\textsc{pfdt}(\underline{P}, \underline{G})$ and $\textsc{Obs}$ into $\textsc{Act}$ with $\textsc{Act}(\pi, x) = \pi(x)$. Draw arrows from $\textsc{pfdt}(\underline{P}, \underline{G})$ into the action or prediction nodes of all predictors, simulations, and identical twins that compute or model the agent’s decision algorithm. Do *not* draw arrows from $\textsc{pfdt}(\underline{P}, \underline{G})$ to merely statistically correlated background causes (such as a smoking lesion or termite infestation).
3. **Evaluate Each Policy Globally:** For each candidate policy $\pi \in \Pi$, compute the *unconditional* expected utility $\mathbb{E}_P[\textsc{V} \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)]$ across all possible observations and states of nature (using $\varepsilon \to 0^+$ trembles if needed to resolve zero-probability observations).
4. **Select the Optimal Policy $\pi^*$:** Choose the policy $\pi^* \in \Pi$ that maximizes this unconditional expectation (breaking exact ties lexicographically).
5. **Apply to Actual Observation $x$:** Output the physical action $a^* = \pi^*(x)$.

---

## 7. Conclusion

**Policy Functional Decision Theory (P-FDT)** represents the fullest expression of the "global perspective" advocated by Yudkowsky and Soares (2017). By elevating the point of intervention from an observation-specific action node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ to a unified policy node $\textsc{pfdt}(\underline{P}, \underline{G}): \mathcal{X} \to \mathcal{A}$, **P-FDT** retains all the triumphs of action-FDT in single-agent dilemmas—one-boxing in standard and transparent Newcomb problems, smoking in the smoking lesion problem, paying the driver in Parfit’s hitchhiker problem, and resisting extortion in XOR and mechanical blackmail—while eliminating the need for arbitrary epistemic priors over counterfactual observations. Most importantly, in multi-agent environments where identical agents or algorithms must coordinate across distinct local observations, **P-FDT** succeeds where action-FDT falters, providing a mathematically unified foundation for both individual rationality and game-theoretic coordination.

---

## References

* Dai, Wei. 2009. "Towards a New Decision Theory." *LessWrong*, August 13, 2009. http://lesswrong.com/lw/15m/towards_a_new_decision_theory/.
* Drescher, Gary L. 2006. *Good and Real: Demystifying Paradoxes from Physics to Ethics*. Cambridge, MA: MIT Press.
* Gibbard, Allan, and William L. Harper. 1978. "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, edited by C. A. Hooker, J. J. Leach, and E. F. McClennen, vol. 1. Boston: D. Reidel.
* Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. New York: Cambridge University Press.
* Joyce, James M. 2012. "Regret and Instability in Causal Decision Theory." *Synthese* 187 (1): 123–145.
* Lewis, David. 1979. "Prisoners' Dilemma Is a Newcomb Problem." *Philosophy & Public Affairs* 8 (3): 235–240.
* Lewis, David. 1981. "Causal Decision Theory." *Australasian Journal of Philosophy* 59 (1): 5–30.
* Nozick, Robert. 1969. "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel*, edited by Nicholas Rescher, 114–146. Dordrecht: D. Reidel.
* Parfit, Derek. 1986. *Reasons and Persons*. New York: Oxford University Press.
* Pearl, Judea. 1996. "Causation, Action, and Counterfactuals." In *Proceedings of the 6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-96)*, edited by Yoav Shoham, 51–73. San Francisco, CA: Morgan Kaufmann.
* Pearl, Judea. 2000. *Causality: Models, Reasoning, and Inference*. New York: Cambridge University Press.
* Skyrms, Brian. 1980. *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. New Haven, CT: Yale University Press.
* Soares, Nate, and Benja Fallenstein. 2015. "Toward Idealized Decision Theory." arXiv preprint arXiv:1507.01986.
* Yudkowsky, Eliezer. 2010. *Timeless Decision Theory*. San Francisco, CA: The Singularity Institute.
* Yudkowsky, Eliezer, and Nate Soares. 2017. "Functional Decision Theory: A New Theory of Instrumental Rationality." arXiv preprint arXiv:1710.05060v2.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Core Focus**

I'm focusing on clarifying the user's ultimate goal: a comprehensive mathematical essay or technical blog post that explains **P-FDT (policy functional decision theory)** and how to practically use it in decision-making scenarios. I need to fully grasp the necessary depth and breadth of the explanation.


**Pinpointing Target Audience**

I've homed in on the intended audience: mathematically savvy individuals keen on both formal methods and the underlying philosophy of the subject. My primary reference remains the paper's footnote 16 (and its link to footnote 7), focusing especially on the "policy-selection" aspects of P-FDT. I'm taking care to clarify the exact nature of the instructions and constraints. I am now working on understanding exactly what is expected in terms of mathematical rigor.


**Analyzing the Details**

I'm now diving into how P-FDT evaluates actions, especially how it handles dependencies and counterfactuals. I'm actively pinpointing open questions in the source material, and clarifying uncertainties to develop reasonable interpretations of operational implications. I'm carefully distinguishing between the source's claims and my own assumptions for clarity. I'm aiming for a readable mathematical essay of roughly 2400-3000 words.


**Clarifying FDT's Nuances**

I'm now focusing on the nuances between standard FDT and the author's preferred policy-based formulation as described in footnote 16. I am now aiming to clarify the key differences, especially in multi-agent scenarios, as the distinction affects how we implement and interpret Equation (4). I'm carefully comparing the agent's behavior under the two formulations, in the context of the Mechanical Blackmail/Updatelessness section, considering the implications of interventions on policies versus direct actions.


**Interpreting the Formalism**

I am now closely examining the implications of intervening on specific nodes within the decision graph, particularly in scenarios like Transparent Newcomb and Mechanical Blackmail. I'm focusing on how this intervention affects the evaluation of the FDT function and the treatment of other nodes as random variables governed by prior beliefs. I'm also considering how this relates to footnote 16 and the transition between intervening on the algorithm's output versus the policy itself. I want to build a better understanding of how the intervention affects decision outcomes.


**Clarifying Agent Actions**

I'm now zeroing in on the agent's actions in policy-based FDT. The agent doesn't directly pick an action $a$. Instead, she manipulates the policy-selecting function, choosing a policy $\pi$ (mapping observations to actions). Then, her input $x$ is fed into this selected policy to yield the actual action $\pi(x)$. Footnote 16 and Footnote 7 clarify this key point, though I'm noting a subtle ambiguity between them that needs resolution, as described above, to ensure a solid and complete interpretation.


**Interpreting Policy Inputs**

I'm now clarifying the nature of "inputs" within policy selection. I've identified an important ambiguity in how policies map to actions, which leads to two interpretations. Is a policy $\pi$ a map from the observation $x$ to an action $a$ (given a fixed world-model), or does it map from the full input $(P, G, x)$ to $a$? I am now exploring both interpretations, and their implications for the functional structure.


**Formalizing Decision Equations**

I'm now writing out the formal equations for P-FDT to ensure clarity, differentiating Yudkowsky & Soares (2017)'s core from any mathematical expansions. I need to make sure the equations are well-defined. I'm focusing on the agent choosing the input-output mapping. This is especially relevant when I am uncertain about the model/utility function, such as in the Smoking Lesion scenario.


**Formalizing Utility Calculations**

I'm now detailing how the agent computes expected utility, especially in scenarios involving model uncertainty. I'm carefully constructing the expected utility equations for both action-FDT and policy-FDT. I need to ensure a clear comparison between the direct intervention on action in action-FDT versus intervening on policy selection in policy-FDT. This is necessary to fully clarify the decision rules.


**Visualizing Model Components**

I'm now figuring out the graphical model's structure within P-FDT. Instead of separate nodes for each observation, I see a single policy node $\textsc{pfdt}(\underline{P}, \underline{G})$ taking values from the policy space. The physical action becomes a deterministic function of the policy and the observation, $\textsc{Act}(\pi, x) = \pi(x)$, and the prediction node depends on the policy too. Now I'm focused on the practical implications.


**Comparing Decision Dilemmas**

I'm now comparing single-agent, sequential dilemmas, such as Transparent Newcomb and Mechanical Blackmail, with multi-agent dilemmas, as highlighted in Footnotes 7 and 16. In the Transparent Newcomb scenario within Action-FDT, the intervention on the decision function when Fiona observes "full" only affects the observed case. The crucial thing is understanding the behavior under prediction error and its implications for subsequent actions.



**Analyzing Dilemma Solutions**

I'm now diving into the implications of P-FDT in sequential decision problems, particularly Transparent Newcomb and Mechanical Blackmail, in both single and multi-agent scenarios. The key lies in understanding how the agent's policy choices impact outcomes, and how prediction errors affect subsequent actions. I am considering the implications of Footnotes 7 and 16, and the agent's behavior under various interventions.



**Constructing Divergence Examples**

I'm now focusing on *when* policy-FDT truly diverges from action-FDT. I'm building multi-agent scenarios with asymmetric observations to demonstrate the divergence mathematically, specifically where iterating over policies makes a critical difference that action-FDT misses. The coordination across information sets is a key factor. I'm crafting specific examples to clearly illustrate why.


**Developing Divergence Scenario**

I'm now creating a multi-agent dilemma to illustrate policy-FDT's divergence from action-FDT. I'm focusing on "The Asymmetric Twin Coordination Game," where each twin must choose actions that complement each other. The payoff depends on their joint actions. I'm focusing on the mathematical formulation, where payoffs depend jointly on the twins' actions. I need to formulate the scenario with asymmetric information to highlight the divergence.


**Examining Equilibrium Selection**

I'm now clarifying how P-FDT handles equilibrium selection in the multi-agent Asymmetric Twin Coordination Game. I'm carefully contrasting it with Action-FDT. In Action-FDT, the twin in Room A intervenes only on her own decision, not the twin in Room B's. That means her prior influences the other twin's action, creating a potential failure mode, as noted above. I'm comparing how P-FDT can coordinate on selecting the best equilibria.


**Clarifying Action Failures**

I'm now zeroing in on Action-FDT failures within the twin coordination game. I'm focusing on scenarios where an agent's prior assigns a high probability to the other twin's action, leading to non-coordination and suboptimal outcomes, as detailed above. I'm building on the above to identify and mathematically prove this key point of divergence between policy and action-based formulations.



**Tracing Utility Maximization**

I'm now tracing through the math of Action-FDT versus Policy-FDT, especially the expected utility calculations with observations. I am clarifying how conditioning on the observations works in both frameworks for the Asymmetric Twin Game. I am checking the implications of both observations on the calculations.


**Interpreting the Global Expectation**

I'm now focusing on Equation (4), specifically the expectation calculation, $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)]$. I recognize that it is a *prior* expectation of $\textsc{V}$ over all states of the world, under the intervention. This is essential for the P-FDT formalism. I'm noting the implications.



**Clarifying Equilibrium Calculations**

I'm now carefully examining the divergence point: why Action-FDT fails in the multi-agent Asymmetric Twin Coordination Game. I'm focusing on why it may fail at equilibrium selection in comparison to P-FDT. I need to clarify the role of the unconditional expectation, and how it leads to miscalculations.

\n\nI'm now zeroing in on Action-FDT failures within the twin coordination game. My focus has shifted to the calculations, especially how the agent's prior on the other twin's actions impacts outcomes, as I detailed above. I'm actively working to mathematically prove the divergence between policy-based and action-based FDT formulations. I've re-examined the source's claims in Section 5 and 9 to clarify the computation, particularly focusing on the role of conditioning on the absence of observations.


**Analyzing Divergence Conditions**

I'm now carefully examining the conditions where action-FDT and policy-FDT diverge in the Asymmetric Twin Game. I'm rigorously exploring the role of priors on the other twin's actions and how they affect the expected utility calculations. I'm pinpointing the exact mathematical criteria that highlight the failure of Action-FDT and showing P-FDT's ability to coordinate and select appropriate equilibria.


**Revisiting Utility Calculations**

I'm now revising the utility calculations, particularly in cases of asymmetric actions, as detailed above. I'm building on prior findings, specifically where I am examining the expected utility function $U(a_1, a_2)$, with an emphasis on additively separable dilemmas. My objective is to formulate these equations with clarity and precision, to ensure clear understanding.


**Examining Utility Equations**

I'm now zeroing in on the payoff structure in Transparent Newcomb, described in Section 6. I've uncovered that the utility function $U(a_1, a_2)$ is not additively separable, specifically because the probability of $x_2$ depends on $a_1$. This interaction term results from $a_1$ changing the probability of observing $x_2$, which in turn multiplies the payoff of $a_2$. I'm now exploring the implications.


**Investigating Action Interactions**

I'm now diving into the interplay between actions, specifically when utility isn't additively separable, such as the Transparent Newcomb scenarios. The interaction terms arise from the dependency of one agent's action on another's, especially in multi-agent dilemmas. I'm focusing on the effect these dependencies have on the functional form of U.


**Tracing Action Outcomes**

I'm now tracing the outcomes of actions when utility isn't additively separable, such as in Transparent Newcomb scenarios. I'm focusing on non-separable utility functions $U(a_1, a_2)$, where actions are interdependent. The agent now considers what its policy would do in each possible observation $x_2$. I'm exploring the implications for Action-FDT in this specific context.


**Testing Twin Scenarios**

I'm now zeroing in on Action-FDT failures within a twin Prisoner's Dilemma with asymmetric observations. I've realized that even with ratified priors, Action-FDT can fail to reach an equilibrium, especially when priors are uncalibrated. This extends to a Twin Prisoner's Dilemma, and highlights critical limitations in multi-agent scenarios, as the agent is playing a non-cooperative game against her own prior beliefs, under specific observations.


**Tracing Twin Failures**

I'm now tracing action-FDT's failure in the asymmetric Prisoner's Dilemma, described above. Because of the differential observations, the twins each intervene on different instances of the action-FDT function, which leads to suboptimal outcomes. I'm focusing on contrasting this with policy-FDT, which may lead to coordination, due to the interventions on the same policy space.


**Calculating Global Expectation**

I'm now zeroing in on the global expectation $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \mathit{Red}) = a)]$. I am now using the asymmetric Prisoner's Dilemma to calculate this expectation to more precisely understand how interventions on $\textsc{fdt}(\underline{P}, \underline{G}, \mathit{Red})$ impact outcomes in multi-agent scenarios, specifically the two scenarios I described above.


**Analyzing Asymmetric Scenarios**

I'm now diving into asymmetric probabilities and known identities within the twin prisoner's dilemma. I'm focusing on how Action-FDT might yield suboptimal outcomes in scenarios with non-symmetric settings. The different probabilities and observation values for each twin now impact action selection, and I'm actively working to clarify these implications. The prior on observing Red versus Blue must now be included in the formal calculations to show the divergence.


**Examining Coordination Dilemmas**

I'm now zeroing in on Action-FDT failures within the twin Prisoner's Dilemma with asymmetric observations, described above. I'm focusing on the global expectation to clarify how interventions on $\textsc{fdt}(\underline{P}, \underline{G}, \mathit{Red})$ impact outcomes in multi-agent scenarios. I also have to consider cases where twins have symmetric priors and must coordinate or anti-coordinate across observations A and B. I am carefully clarifying the formal calculations.


**Calculating Divergence Examples**

I'm now detailing a Twin Stag Hunt, a two-room scenario where agents must coordinate to receive a reward. I'm building on prior findings, specifically asymmetric outcomes. I've designed the twin scenario to provide a clear demonstration of action-FDT failures. I am now formulating the expected utilities and equilibria under both Action and Policy-FDT in this scenario.


**Clarifying Divergence Scenarios**

I'm now detailing the utility calculations within the twin Stag Hunt dilemma and contrasting Action-FDT and Policy-FDT. I am formalizing the expected utilities and equilibria under each approach, highlighting how action-FDT fails to account for the impact of one twin's action on the other, unlike policy-FDT. This reinforces the core divergence in multi-agent dilemmas.


**Calculating Divergence Examples**

I'm now detailing a multi-project scenario to demonstrate action-FDT failures. I am computing the expected utility when one twin shirks. I'm focusing on the condition where the probability of success when shirk is $q=0$. This gives an expected utility of negative five thousand dollars. I'm actively working on demonstrating the conditions where a pessimistic prior leads to self-confirming shirking outcomes.


**Formulating Shirking Scenario**

I'm now detailing a scenario to highlight Action-FDT failures. If I, as the agent, have a prior uniform over 100 projects and there are high costs, then it becomes optimal to shirk. I've found an explicit multi-agent setup where Action-FDT gives up. The scenario and calculations should make it clear!


**Clarifying Shirking Outcomes**

I'm now detailing the conditions under which Action-FDT yields self-confirming shirking outcomes in the multi-agent project scenario, as I mentioned above. I'm formalizing the expected utility and clarifying the role of pessimistic priors in this scenario, where the probability of success when shirk is $q=0$. I'm also ensuring a clearer comparison between Action and Policy FDT in this case.


**Exploring Policy Interventions**

I'm now zeroing in on a multi-agent dilemma where policy-FDT might outperform action-FDT. I'm focusing on scenarios with asymmetric observations like Ultimatum or Asymmetric Twin Prisoner's Dilemma. I'm evaluating what happens when a predictor interacts with an agent's policy $\pi$ based on observations $x_1$ and $x_2$. I'm considering the effect of various interventions on fixed policies, and comparing it to what happens when we modify only actions directly.


**Analyzing Payoff Dependencies**

I'm now diving into scenarios where payoffs aren't additively separable, specifically the Stag Hunt and Joint Project scenarios that I mentioned above. I'm focusing on the effect of the dependency of one agent's action on another's outcomes, and how this impacts the behavior of the two formulations. My main goal is to examine how P-FDT can successfully coordinate when Action-FDT fails to do so.


**Clarifying Non-Separability Payoffs**

I'm now zeroing in on cases where payoffs aren't additively separable, specifically the multiplicative nature in scenarios like the Twin Prisoner's Dilemma. Here's a key observation: with Action-FDT, you need to begin with a prior that already favors cooperation for the scheme to function. But Policy-FDT can, by jointly optimizing $(\pi(\text{Red}), \pi(\text{Blue}))$, achieve cooperation directly. In an anti-coordination scenario, this provides the most value.


**Interpreting Policy Definitions**

I'm now carefully examining the definition of policy in the paper, especially distinguishing between mapping from observations to actions and mapping from full inputs to actions. I'm focusing on the mathematical implications of both interpretations, and how they change our understanding. Specifically, I am clarifying the differences between Footnote 7 and Footnote 16, and the impact this has on the model.


**Clarifying Domain Definitions**

I'm now carefully examining the definition of policy domains, considering cases with and without agent model uncertainty. I'm building on prior findings, distinguishing between mapping from observations to actions and mapping from full inputs to actions, and how this affects the intervention node. I'm focusing on scenarios with model uncertainty, like the Smoking Lesion Problem, or multi-agent games, and considering how interventions on the universal node, mapping $(\model, x) \mapsto a$, can improve decision outcomes.


**Interpreting Expectation Formalisms**

I'm now clarifying Equation (4)'s expectation calculation within P-FDT. The expectation $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\dots)]$ is with respect to the *unconditioned* distribution $P$, as described. I am working to demonstrate the potential for harmful "double update" scenarios, especially in sequential decisions. I am looking at Section 5 and 9 to clarify the computation.


**Clarifying Equation Interpretations**

I'm now clarifying the use of the unconditioned expectation in Equation (4) of P-FDT to prevent misapplication. I'm focusing on the *unconditional* expectation $\mathbb{E}_P[\textsc{V} \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)]$, as I found some confusion could arise from the inclusion of observation variables within the do-calculus. I'm considering scenarios with zero-probability observations like Mechanical Blackmail.


**Analyzing Infallible Scenarios**

I'm now zeroing in on scenarios with infallible predictors, particularly Mechanical Blackmail and Transparent Newcomb. My work centers on contrasting how P-FDT handles these cases, especially the unique selection of $\pi^*(\mathit{blackmail}) = \mathit{refuse}$ and the implications for zero-probability observations under different policies. I'm actively assessing how policies like $(\mathit{onebox}, \mathit{twobox})$ and $(\mathit{onebox}, \mathit{onebox})$ compare in the presence of an accurate predictor.


**Refining Policy Choices**

I'm now carefully examining the operational refinement for handling zero-probability observations under policy $\pi^*$, as I mentioned above, using an analogy to trembling-hand perfection. I'm focusing on defining a workable operational procedure, and considering the implications for computational complexity within the policy space $\Pi$. I need to ensure a clear demonstration.


**Refining Essay Outline**

I'm now refining the essay's structure, focusing on a clear presentation of P-FDT. I'll begin by contextualizing it within CDT and EDT. I will then explain action-FDT, and formally introduce P-FDT via key quotes from the source material. I will define a policy as a function that maps inputs to actions. I will then describe its role in evaluation, moving to formalizing the equations and outlining several example scenarios.


**Clarifying Expected Utilities**

I'm now detailing the calculations for action-FDT, contrasted with P-FDT, especially the expected utility framework and its equation (1), and the differences from CDT and EDT as they relate to Equation (4). I'm carefully formulating the expected value of utility, with and without observation variables. I am now formalizing the mathematical definitions.


**Clarifying Divergence Point**

I'm now zeroing in on the Transparent Newcomb problem to compare P-FDT and action-FDT calculations, as detailed above. I'm focusing on why these methods agree in single-agent dilemmas. I'm aiming to articulate the clean and unambiguous structure of P-FDT in handling policy choices. I'm comparing the epistemic prior and demonstrating that policy-FDT optimizes over observation branches simultaneously.


**Deriving Divergence Conditions**

I'm now deriving the exact mathematical conditions where action-FDT and policy-FDT diverge. My focus is non-separability (interaction terms) in expected utility across distinct observations in multi-agent dilemmas. I'm actively working through a concrete "Two-Room Twin Joint Project" example, to detail the failures of action-FDT and the successes of P-FDT.


**Clarifying Model Domains**

I'm now fully comparing the two policy interpretations: $\pi: \mathcal{X} \to \mathcal{A}$ versus $\pi: \mathcal{M} \times \mathcal{X} \to \mathcal{A}$, especially regarding model uncertainty. I'm focusing on their use in multi-agent scenarios, and in situations with zero probability observations, ensuring I have fully clarified the implications of these domain definitions.


**Refining P-FDT Framework**

I'm now detailing all acronyms and mathematical equations with clarity. I'm double-checking word count targets and quotation accuracy, especially from the sources. I'm ensuring consistent nomenclature for all decision theories. Finally, I will ensure that the notation is correct, and easy to follow.


```
