# 029_fdt_policy_google_gemini-4-argon_rhigh_phigh / 00012

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/36241ab1-a63c-410a-9547-184fc3878a58/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/36241ab1-a63c-410a-9547-184fc3878a58/call_0/response.raw) · finish: `stop`

### Visible response

````text
# Policy Functional Decision Theory (P-FDT): Formal Foundations, Subjunctive Policies, and Decision Analysis

## 1. Introduction and Philosophical Motivation

In the foundations of rational choice, standard decision theories agree that an instrumentally rational agent ought to maximize expected utility, yet they fracture over a deceptively simple question: *how should an agent evaluate the hypothetical world in which she chooses a different option?*

Drawing on the representation theorem of Joyce (1999), Yudkowsky and Soares (2017) observe that expected utility maximization can be written in a unified form. Given a countable set of outcomes $\mathcal{O}$, a finite set of actions $\mathcal{A}$, a countable set of observation histories $\mathcal{X}$, and a bounded real-valued utility function $\mathcal{U}: \mathcal{O} \to \mathbb{R}$, an agent who has received observation history $x \in \mathcal{X}$ evaluates an action $a \in \mathcal{A}$ via

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j),$$

where $P(a \hookrightarrow o_j ;\, x)$ denotes the probability that outcome $o_j \in \mathcal{O}$ obtains in the hypothetical scenario where action $a$ is taken after observing $x$. As Joyce remarks, "decision theories should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated." That epistemic perspective is encoded entirely in the decision-hypothetical connective "$\hookrightarrow$".

The two classical contenders—Evidential Decision Theory (EDT) and Causal Decision Theory (CDT)—interpret "$\hookrightarrow$" in ways that fail systematically on well-known classes of decision problems:

* **Evidential Decision Theory (EDT)** equates decision hypotheticals with Bayesian conditionalization: $P(a \hookrightarrow o_j ;\, x) = P(\textsc{Outcome} = o_j \mid \textsc{Obs} = x, \textsc{Act} = a)$. Because conditioning preserves *all* statistical correlations between the agent's action and the state of the world, EDT prescribes one-boxing in Newcomb's problem, but it also prescribes irrationally "managing the news" when correlations arise from a common cause or a manipulative extortionist—such as refraining from smoking in the Smoking Lesion problem or paying up in the XOR Blackmail problem.
* **Causal Decision Theory (CDT)** equates decision hypotheticals with local causal interventions on the agent's physical action token: $P(a \hookrightarrow o_j ;\, x) = P(\textsc{Outcome} = o_j \mid \mathtt{do}(\textsc{Act} = a), \textsc{Obs} = x)$ in Pearl's (1996, 2000) graphical framework. Because the $\mathtt{do}(\textsc{Act} = a)$ operator severs all correlations with events not causally downstream of the physical act, CDT rightly ignores merely statistical correlations in the Smoking Lesion and XOR Blackmail problems. However, it also severs logically or computationally necessary correlations between the agent's decision process and accurate predictors or psychological twins—causing CDT agents to two-box (and walk away poor) in Newcomb's problem, defect in the Psychological Twin Prisoner's Dilemma, die in Parfit's Hitchhiker problem, and spiral into reflective instability in Death in Damascus.

To resolve this impasse, Yudkowsky and Soares (2017) introduce functional decision theory, which treats decision-making as selecting the output of a fixed mathematical function and evaluates hypotheticals by varying the logical output of that function across all physical systems—predictors, simulations, and psychological twins—that *subjunctively depend* upon it. 

Yet within Yudkowsky and Soares's paper, there is a crucial structural distinction between the simplified formalization presented in the main text and the deeper theory the authors actually endorse. In the main body of their paper, the authors formalize what we will call **Action-FDT** (or standard action-based FDT), in which the agent intervenes on a node representing the specific action output for her current observation history. However, in Footnotes 7 and 16, the authors note that their preferred formulation is **Policy Functional Decision Theory (P-FDT)**:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper." (Footnote 7)

And in Footnote 16, they describe the operational mechanics of **P-FDT**:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition." (Footnote 16)

In this essay, we develop a rigorous mathematical account of **P-FDT**. We will show how **P-FDT** is formalized using structural causal and subjunctive graphs, how it evaluates policies and counterfactual observations, why it eliminates arbitrary nuisance parameters that linger in Action-FDT, how it diverges sharply from Action-FDT in multi-agent dilemmas with asymmetric information, and how to resolve the open technical questions left unspecified by Footnote 16.

---

## 2. Formalizing P-FDT: From Action Nodes to Policy Spaces

To understand **P-FDT** precisely, let us first establish the formal machinery shared by EDT, CDT, and Action-FDT in Section 5 of Yudkowsky and Soares (2017), and then construct the policy-selection equations indicated by Footnotes 7 and 16.

Let $\mathcal{O}$ be a countable set of outcomes, $\mathcal{A}$ a finite set of physical actions, and $\mathcal{X}$ a countable (and in standard finite dilemmas, finite) set of possible observations or observation histories. Let $\textsc{Outcome}$, $\textsc{Act}$, and $\textsc{Obs}$ be random variables taking values in $\mathcal{O}$, $\mathcal{A}$, and $\mathcal{X}$ respectively, and define the utility random variable $\textsc{V} \coloneqq \mathcal{U}(\textsc{Outcome})$.

An agent maintains a world-model $M = (P, G)$, where:
1. $P$ is a subjective probability distribution over a collection of random variables describing both physical facts about the environment and logical/mathematical facts about the outputs of functions.
2. $G$ is a directed acyclic graph (DAG) over the variables in $P$ encoding both causal dependencies and *subjunctive dependencies*—structural relations describing how the behavior of physical systems (such as predictors, copies, or the agent's own body) depends on the outputs of mathematical decision algorithms.

In this graphical framework, the three action-level theories in the reference article are defined as follows:

$$\mathrm{EDT}(P, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs} = x, \textsc{Act} = a\right), \tag{1}$$

$$\mathrm{CDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{Act} = a), \textsc{Obs} = x\right), \tag{2}$$

$$\mathrm{FDT}_{\text{act}}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right). \tag{3}$$

Here, following the notation of the reference paper, underlines denote *dequoting*: if $x = \textit{full}$, then $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ is the syntactic variable name $\textsc{fdt}(\underline{P}, \underline{G}, \textit{full})$ inside $G$.

### The Mathematical Structure of P-FDT

Why move from Equation (3) to **P-FDT**? Notice what Equation (3) does when the observation space $\mathcal{X}$ contains more than one possible observation, say $\mathcal{X} = \{x_1, x_2, \dots, x_k\}$. Action-FDT must place $k$ separate logical nodes into the graph $G$:

$$\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_1}), \quad \textsc{fdt}(\underline{P}, \underline{G}, \underline{x_2}), \quad \dots, \quad \textsc{fdt}(\underline{P}, \underline{G}, \underline{x_k}).$$

When the agent observes $x_i$, Action-FDT intervenes *only* on the single node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_i})$, holding the remaining $k-1$ nodes fixed to whatever prior probability distribution $P$ assigns to them.

**P-FDT** replaces this fragmented node-by-node intervention with a unified functional intervention. Let us define the **policy space** $\Pi$ as the set of all mappings from observations to actions:

$$\Pi \coloneqq \mathcal{A}^{\mathcal{X}} = \{\pi \mid \pi: \mathcal{X} \to \mathcal{A}\}.$$

(When $\mathcal{X}$ and $\mathcal{A}$ are finite, $\Pi$ is a finite set of cardinality $|\mathcal{A}|^{|\mathcal{X}|}$.) 

In **P-FDT**, the world-model $(P, G)$ contains a single logical decision node $\textsc{pfdt}(\underline{P}, \underline{G})$ taking values in the policy space $\Pi$. This node represents the mathematical policy output of the **P-FDT** algorithm when given the world-model $(P, G)$. Following Footnote 16—which specifies that **P-FDT** "intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action"—we formalize **P-FDT** as a two-stage procedure:

**Stage 1 (Policy Selection via Subjunctive Intervention):**
The agent identifies the optimal policy $\pi^*_{(P,G)} \in \Pi$ by intervening on the logical policy node $\textsc{pfdt}(\underline{P}, \underline{G})$ in $(P, G)$ and maximizing unconditional expected utility:

$$\pi^*_{(P,G)} \coloneqq \operatorname*{argmax}_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right). \tag{4a}$$

**Stage 2 (Policy Application / Input Evaluation):**
Given the agent's actual observation $x \in \mathcal{X}$, the agent applies the selected policy $\pi^*_{(P,G)}$ to $x$ to output her concrete physical action:

$$\mathrm{PFDT}(P, G, x) \coloneqq \pi^*_{(P,G)}(x) = \left[\operatorname*{argmax}_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right)\right](x). \tag{4b}$$

### Structural Equations of a P-FDT Graph

To see how the $\mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)$ operator propagates through the graph $G$, consider how the node $\textsc{pfdt}(\underline{P}, \underline{G})$ connects to the rest of the world-model:

1. **The Agent's Physical Action ($\textsc{Act}$):** The agent's physical act depends on both her policy and the observation she actually receives. In $G$, $\textsc{Act}$ has incoming arrows from $\textsc{pfdt}(\underline{P}, \underline{G})$ and $\textsc{Obs}$, governed by the evaluation structural equation:
   $$\textsc{Act}(\pi, x) \coloneqq \pi(x).$$
2. **Predictors and Simulators ($\textsc{Prediction}$):** Any predictor in the environment who models how the agent will respond to a hypothetical observation $x' \in \mathcal{X}$ (or who models the agent's overall disposition across multiple contingencies) has an incoming arrow directly from $\textsc{pfdt}(\underline{P}, \underline{G})$. For instance, a predictor checking what the agent does upon observing $x'$ computes a noisy or exact function of $\pi(x')$.
3. **Other Copies or Psychological Twins ($\textsc{Act}_i$):** In a multi-agent setting where copy $i$ shares the decision algorithm and world-model $(P, G)$ but receives local observation $\textsc{Obs}_i$, copy $i$'s physical action is governed by the structural equation $\textsc{Act}_i(\pi, \textsc{Obs}_i) \coloneqq \pi(\textsc{Obs}_i)$, with an incoming arrow from the *same* logical node $\textsc{pfdt}(\underline{P}, \underline{G})$.

```
                  +----------------------+
                  |   pfdt(P, G) = pi    |  <-- Point of P-FDT Intervention
                  +----------------------+
                     /                \
                    /                  \ (Subjunctive dependence:
   (Policy evaluation:                  \ Predictor queries pi(x'))
    Act = pi(Obs))                       v
           |                    +------------------+      +------------+
           |                    |    Prediction    | <--- |  Accurate  |
           v                    +------------------+      +------------+
     +-----------+                   /        \
     |    Act    | <---- +---------+           \
     +-----------+       |   Obs   |            v
           \             +---------+      +-----------+
            \                             |   Box B   |
             \                           /+-----------+
              v                         v
             +---------------------------+
             |       V = U(Outcome)      |
             +---------------------------+
```

When the agent performs the Pearl surgery $\mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)$, she sets the logical variable $\textsc{pfdt}(\underline{P}, \underline{G})$ to the complete function $\pi: \mathcal{X} \to \mathcal{A}$ and propagates this assignment forward along all directed paths in $G$, holding fixed all variables not downstream of $\textsc{pfdt}(\underline{P}, \underline{G})$ (such as exogenous noise $\textsc{Accurate}$ or background states like $\textsc{Infestation}$).

---

## 3. Subjunctive Dependence, Counterpossibles, and "Updateless" Evaluation

A striking feature of **P-FDT** (shared with Action-FDT and Wei Dai's 2009 Updateless Decision Theory) is how it incorporates new evidence $x \in \mathcal{X}$. Look closely at Equations (4a) and (4b): in Stage 1, the expectation $\mathbb{E}\left[\textsc{V} \mid \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right]$ is computed with respect to the *prior* world-model $P$, **without** conditioning $P$ on $\textsc{Obs} = x$. Instead, the observation $x$ enters only in Stage 2, when the agent evaluates $\pi^*_{(P,G)}(x)$!

Why does **P-FDT** refuse to condition $P$ on $\textsc{Obs} = x$ before selecting $\pi^*$? Because in dilemmas containing predictors who anticipate how the agent reacts to observations, *which observation the agent receives depends subjunctively on the policy she adopts*. 

If an agent conditions $P$ on $\textsc{Obs} = x$ before evaluating her options—as CDT and EDT do, and as Yudkowsky's (2010) earlier Timeless Decision Theory (TDT) did in what the reference paper calls a harmful "double update"—she treats her observation $x$ as an immutable past fact that could not have been otherwise even if her decision rule had been different. By contrast, **P-FDT** recognizes that if her policy $\pi$ were different, a predictor anticipating $\pi$ might have acted differently, causing the agent to receive a completely different observation $x' \neq x$.

As Yudkowsky and Soares note in Section 3, this requires evaluating *counterpossible* conditionals: since $\textsc{pfdt}(P, G)$ is a fixed mathematical function, there is only one policy $\pi^*$ it outputs of logical necessity, just as $6288 + 1048 = 7336$ of necessity. Yet a bounded agent who does not know the output of her own computation in advance can represent $\textsc{pfdt}(\underline{P}, \underline{G})$ as a node in her graphical model $G$ (via Kleene's 1938 second recursion theorem) and compute what would follow under each candidate assignment $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$.

### Worked Example 1: P-FDT in the Transparent Newcomb Problem

To see how **P-FDT** operates in practice—and how it simplifies the calculations of Action-FDT in the reference paper—let us apply **P-FDT** to Drescher's (2006) **Transparent Newcomb Problem** (Dilemma 5 in Yudkowsky & Soares 2017).

* **Setup:** Both Box A (containing $\$1,000$) and Box B (containing either $\$1,000,000$ or $\$0$) are transparent. A predictor with $99\%$ accuracy ($\textsc{Accurate} = \textit{accurate}$ with probability $0.99$, $\textit{inaccurate}$ with probability $0.01$) placed $\$1,000,000$ in Box B if and only if she predicted that the agent would leave Box A behind ($\textit{onebox}$) upon seeing that Box B is $\textit{full}$. The agent walks into the room and observes $x = \textit{full}$. Should she one-box or two-box?

Let us first recall how Action-FDT handled this in Section 6 of the reference article. Because Action-FDT splits the decision function into two separate nodes—$\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full})$ and $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty})$—an Action-FDT agent who observes $\textit{full}$ intervenes *only* on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full})$. To compute expected utility in the $1\%$ error branch where Box B is empty, the authors had to introduce an extraneous parameter $q \in [0, 1]$ representing "Fiona's prior probability that she two-boxes upon seeing the box empty."

Now let us solve the exact same problem using **P-FDT**. Here:
* Observation space: $\mathcal{X} = \{\textit{full}, \textit{empty}\}$.
* Action space: $\mathcal{A} = \{\textit{onebox}, \textit{twobox}\}$.
* Policy space: $\Pi = \mathcal{A}^{\mathcal{X}}$ consists of $2^2 = 4$ policies. Let us denote a policy by $\pi_{a,b}$, where $a = \pi(\textit{full})$ is the action taken when Box B is observed full, and $b = \pi(\textit{empty})$ is the action taken when Box B is observed empty:
  1. $\pi_{1,1}$: $\pi(\textit{full}) = \textit{onebox}, \quad \pi(\textit{empty}) = \textit{onebox}$
  2. $\pi_{1,2}$: $\pi(\textit{full}) = \textit{onebox}, \quad \pi(\textit{empty}) = \textit{twobox}$
  3. $\pi_{2,1}$: $\pi(\textit{full}) = \textit{twobox}, \quad \pi(\textit{empty}) = \textit{onebox}$
  4. $\pi_{2,2}$: $\pi(\textit{full}) = \textit{twobox}, \quad \pi(\textit{empty}) = \textit{twobox}$

The structural equations in $G$ are:
* $\textsc{Prediction}(\pi, \textit{accurate}) = 1$ if $\pi(\textit{full}) = \textit{onebox}$, and $2$ if $\pi(\textit{full}) = \textit{twobox}$ (and reversed when $\textsc{Accurate} = \textit{inaccurate}$).
* $\textsc{Box B}(1) = \textit{full}$ and $\textsc{Box B}(2) = \textit{empty}$; $\textsc{Obs} = \textsc{Box B}$.
* $\textsc{Act}(\pi, \textsc{Obs}) = \pi(\textsc{Obs})$.

In **Stage 1**, the **P-FDT** agent evaluates $\mathbb{E}\left[\textsc{V} \mid \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right]$ across all four policies in $\Pi$:

1. **For $\pi_{1,1} = (\textit{onebox}, \textit{onebox})$:** Since $\pi_{1,1}(\textit{full}) = \textit{onebox}$, with probability $0.99$ the predictor predicts $1$, Box B is $\textit{full}$, and the agent plays $\pi_{1,1}(\textit{full}) = \textit{onebox}$, receiving $\$1,000,000$. With probability $0.01$ the predictor errs, Box B is $\textit{empty}$, and the agent plays $\pi_{1,1}(\textit{empty}) = \textit{onebox}$, receiving $\$0$.
   $$\mathbb{E}\left[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi_{1,1})\right] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000.$$

2. **For $\pi_{1,2} = (\textit{onebox}, \textit{twobox})$:** With probability $0.99$, Box B is $\textit{full}$ and the agent plays $\pi_{1,2}(\textit{full}) = \textit{onebox}$ ($\$1,000,000$). With probability $0.01$, Box B is $\textit{empty}$ and the agent plays $\pi_{1,2}(\textit{empty}) = \textit{twobox}$ ($\$1,000$).
   $$\mathbb{E}\left[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi_{1,2})\right] = 0.99(\$1,000,000) + 0.01(\$1,000) = \$990,010.$$

3. **For $\pi_{2,1} = (\textit{twobox}, \textit{onebox})$:** Since $\pi_{2,1}(\textit{full}) = \textit{twobox}$, with probability $0.01$ (when the predictor errs) Box B is $\textit{full}$ and the agent plays $\pi_{2,1}(\textit{full}) = \textit{twobox}$ ($\$1,001,000$). With probability $0.99$ (when the predictor is accurate) Box B is $\textit{empty}$ and the agent plays $\pi_{2,1}(\textit{empty}) = \textit{onebox}$ ($\$0$).
   $$\mathbb{E}\left[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi_{2,1})\right] = 0.01(\$1,001,000) + 0.99(\$0) = \$10,010.$$

4. **For $\pi_{2,2} = (\textit{twobox}, \textit{twobox})$:** With probability $0.01$, Box B is $\textit{full}$ and the agent plays $\pi_{2,2}(\textit{full}) = \textit{twobox}$ ($\$1,001,000$). With probability $0.99$, Box B is $\textit{empty}$ and the agent plays $\pi_{2,2}(\textit{empty}) = \textit{twobox}$ ($\$1,000$).
   $$\mathbb{E}\left[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi_{2,2})\right] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$

Comparing the four values, the unique optimal policy is $\pi^*_{(P,G)} = \pi_{1,2} = (\textit{onebox}, \textit{twobox})$, which achieves $\$990,010$ in expectation. 

In **Stage 2**, the agent plugs her actual observation $x = \textit{full}$ into $\pi^*_{(P,G)}$:

$$\mathrm{PFDT}(P, G, \textit{full}) = \pi_{1,2}(\textit{full}) = \textit{onebox}.$$

Notice an immediate mathematical benefit of **P-FDT** over Action-FDT that goes unremarked in the reference paper: **P-FDT** eliminates the arbitrary prior parameter $q$ over counterfactual observation nodes! Because the intervention $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$ simultaneously specifies the agent's behavior at *both* $\textit{full}$ and $\textit{empty}$, the agent does not need to maintain subjective probability estimates about what she would do at unvisited observation nodes; she optimizes over all observation branches jointly.

---

## 4. Why Policy Selection Matters: Multi-Agent Dilemmas and Action-FDT vs. P-FDT

Why do Yudkowsky and Soares remark in Footnotes 7 and 16 that iterating over policies rather than actions "makes a difference in certain multi-agent dilemmas"? The reference paper does not supply an explicit example of such a multi-agent dilemma. Let us construct two precise game-theoretic examples (our own mathematical constructions extending the source text) that reveal exactly why Action-FDT breaks down in multi-agent environments with asymmetric observations while **P-FDT** succeeds.

### Worked Example 2: The Distributed Twin Coordination Dilemma

Suppose two psychological twins, Agent 1 and Agent 2, implement the exact same decision algorithm with the same initial world-model $(P, G)$ in separate, causally isolated rooms. A referee flips a fair coin to assign one twin the observation $\textit{A}$ and the other twin the observation $\textit{B}$ (so in the prior $P$, each twin has a $50\%$ chance of observing $\textit{A}$ and a $50\%$ chance of observing $\textit{B}$, and knows the other twin observes the complementary symbol).

Each twin must choose an action from $\mathcal{A} = \{\textit{cooperate}, \textit{defect}\}$. Choosing $\textit{cooperate}$ incurs a personal effort cost of $\$1,000$. However, the two twins are working on two halves of a joint lock: **both twins receive a $\$1,000,000$ payout if and only if both the $\textit{A}$-observer and the $\textit{B}$-observer choose $\textit{cooperate}$**.

Let us compare how **Action-FDT** (Equation 3) and **P-FDT** (Equations 4a–4b) behave when a twin wakes up and observes $x = \textit{A}$:

#### Case A: Action-FDT's Vulnerability to Cross-Branch Priors
In Action-FDT, because the two twins receive different observations ($\textit{A}$ vs. $\textit{B}$), their actions are governed by **two distinct nodes** in $G$: $\textsc{fdt}(\underline{P}, \underline{G}, \textit{A})$ and $\textsc{fdt}(\underline{P}, \underline{G}, \textit{B})$.
When the twin who observes $\textit{A}$ runs Action-FDT, she intervenes *only* on $\textsc{fdt}(\underline{P}, \underline{G}, \textit{A}) = a$. Because $\textsc{fdt}(\underline{P}, \underline{G}, \textit{B})$ is a separate node in $G$ not downstream of $\textsc{fdt}(\underline{P}, \underline{G}, \textit{A})$, the intervention $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \textit{A}) = a)$ leaves the distribution of $\textsc{fdt}(\underline{P}, \underline{G}, \textit{B})$ untouched!

Let $q = P(\textsc{fdt}(\underline{P}, \underline{G}, \textit{B}) = \textit{cooperate})$ be the agent's prior probability in $P$ that the algorithm outputs $\textit{cooperate}$ on input $\textit{B}$. Under Action-FDT:
* If she sets $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \textit{A}) = \textit{cooperate})$: With probability $0.5$ she is the $\textit{A}$-observer (paying $\$1,000$), with probability $0.5$ she is the $\textit{B}$-observer (paying $\$1,000$ with probability $q$), and the $\$1,000,000$ lock opens only if the $\textit{B}$-observer also cooperates (probability $q$). Thus:
  $$\mathbb{E}\left[\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \textit{A}) = \textit{cooperate})\right] = q(\$1,000,000) - 0.5(\$1,000) - 0.5q(\$1,000).$$
* If she sets $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \textit{A}) = \textit{defect})$: The lock never opens ($0$), and she only pays $\$1,000$ if she is the $\textit{B}$-observer and $\textit{B}$ cooperates:
  $$\mathbb{E}\left[\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \textit{A}) = \textit{defect})\right] = -0.5q(\$1,000).$$

Comparing the two, Action-FDT cooperates if and only if $q(\$1,000,000) > \$500$, i.e., $q > 0.0005$. If both twins begin with a pessimistic prior $q < 0.0005$ about what their twin will do upon seeing the *other* observation—or if the game is an asymmetric coordination game (such as Distributed Battle of the Sexes where the $\textit{A}$-observer must play $f_1$ and the $\textit{B}$-observer must play $f_2$ to avoid interference)—Action-FDT cannot coordinate across the two observation branches! It falls prey to the exact prior-sensitivity and equilibrium-selection failures that plagued EDT and CDT.

#### Case B: P-FDT's Global Coordination
Now see how **P-FDT** solves the same dilemma. In **P-FDT**, both twins share the single policy node $\textsc{pfdt}(\underline{P}, \underline{G}) \in \Pi = \{\textit{cooperate}, \textit{defect}\}^{\{\textit{A}, \textit{B}\}}$. The $\textit{A}$-observer executes $\pi(\textit{A})$ and the $\textit{B}$-observer executes $\pi(\textit{B})$. In Stage 1, both twins evaluate all four policies $\pi = (\pi(\textit{A}), \pi(\textit{B}))$:

1. $\pi_{C,C} = (\textit{cooperate}, \textit{cooperate})$: Both twins cooperate, both pay $\$1,000$, and both get $\$1,000,000$.
   $$\mathbb{E}\left[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi_{C,C})\right] = \$1,000,000 - \$1,000 = \$999,000.$$
2. $\pi_{C,D} = (\textit{cooperate}, \textit{defect})$: The $\textit{A}$-twin pays $\$1,000$ (probability $0.5$), the lock stays shut.
   $$\mathbb{E}\left[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi_{C,D})\right] = -\$500.$$
3. $\pi_{D,C} = (\textit{defect}, \textit{cooperate})$: The $\textit{B}$-twin pays $\$1,000$ (probability $0.5$), the lock stays shut.
   $$\mathbb{E}\left[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi_{D,C})\right] = -\$500.$$
4. $\pi_{D,D} = (\textit{defect}, \textit{defect})$: Neither pays, the lock stays shut.
   $$\mathbb{E}\left[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi_{D,D})\right] = \$0.$$

Regardless of any prior beliefs $q$, $\pi^* = \pi_{C,C}$ uniquely maximizes expected utility at $\$999,000$. In Stage 2, the $\textit{A}$-twin computes $\pi_{C,C}(\textit{A}) = \textit{cooperate}$, and the $\textit{B}$-twin computes $\pi_{C,C}(\textit{B}) = \textit{cooperate}$.

### Worked Example 3: The Role-Asymmetric Twin Prisoner's Dilemma

Even more dramatically, consider a multi-agent dilemma where the two observation branches have **non-complementary (purely additive) payoffs**, so that even with perfect logical omniscience ($q=1$), Action-FDT fails if the agent knows her own role in $P$.

Suppose Alice and her psychological twin Bob share the same decision procedure and world-model $(P, G)$, where it is common knowledge from the outset that Alice will receive observation $x = \textit{room1}$ and Bob will receive observation $x = \textit{room2}$. Each must choose $\textit{cooperate}$ or $\textit{defect}$. 
* If the agent in $\textit{room1}$ chooses $\textit{cooperate}$, she pays $\$1,000$ and the agent in $\textit{room2}$ receives $\$1,000,000$.
* If the agent in $\textit{room2}$ chooses $\textit{cooperate}$, she pays $\$1,000$ and the agent in $\textit{room1}$ receives $\$1,000,000$.

Suppose first that $P$ encodes indexical symmetry before the observation $x$ is plugged in—meaning that in $P$, the random variable $\textsc{V}$ represents the utility of a randomly selected twin ($50\%$ $\textit{room1}$, $50\%$ $\textit{room2}$), and only the input $x \in \{\textit{room1}, \textit{room2}\}$ tells the agent which room she is in. Even then, look at what happens if only $\textit{room1}$ has the opportunity to sacrifice $\$1,000$ to give $\textit{room2}$ $\$1,000,000$ (a one-way **Twin Rescue Dilemma** where $\textit{room2}$ has no actions): under **P-FDT**, the policy $\pi(\textit{room1}) = \textit{cooperate}$ yields expected utility $0.5(-\$1,000) + 0.5(\$1,000,000) = \$499,500 > \$0$, so the $\textit{room1}$ twin rescues the $\textit{room2}$ twin!

What if Alice's world-model $P$ already identifies her as the occupant of $\textit{room1}$ (so $\textsc{V} = \textsc{V}_1$ is strictly Room 1's personal payoff), while Bob's world-model identifies him as the occupant of $\textit{room2}$ ($\textsc{V} = \textsc{V}_2$)? Under Action-FDT, when Alice intervenes on $\textsc{fdt}(\underline{P}, \underline{G}, \textit{room1})$, she controls *only* Room 1's action, which costs Room 1 $\$1,000$ and gives Room 1 $\$0$ (since Room 1's $\$1,000,000$ comes solely from $\textsc{fdt}(\underline{P}, \underline{G}, \textit{room2})$). Thus Action-FDT defects! Under **P-FDT**, if Alice and Bob share a role-indexed policy function $\pi$ mapping roles to actions under an ex-ante veil-of-ignorance prior $P$, intervening on $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$ couples their fates across roles and secures mutual cooperation.

---

## 5. Unresolved Questions in Footnote 16 and Operational Proposals

Because Yudkowsky and Soares (2017) mention **P-FDT** only briefly in Footnotes 7 and 16, several important mathematical and operational questions are left open by the source text. To apply **P-FDT** reliably to unfamiliar cases, a researcher must recognize these underspecified points and adopt coherent operational conventions. Below, we distinguish what the source text states from our own operational proposals.

### Open Question 1: What Counts as an "Input" to the Policy?

In Footnote 7, the authors write that policies are "mappings from observations to actions" ($\pi: \mathcal{X} \to \mathcal{A}$). In Footnote 16, however, they write that the agent intervenes on $\mathrm{FDT}(-)$ to choose a policy "which maps inputs to actions, to which the agent then applies her inputs in order to select an action." Meanwhile, in Equation (4) of the main text, the formal inputs to the algorithm $\mathrm{FDT}(P, G, x)$ are the triple $(P, G, x)$—or, in the Smoking Lesion problem (Section 6), a pair $(P^F_S, G^F)$ vs. $(P^F_R, G^F)$ where the agent's utility function $\mathcal{U}_S$ vs. $\mathcal{U}_R$ differs across branches!

This raises a crucial modeling question: **Does a policy $\pi$ map only observations $\mathcal{X} \to \mathcal{A}$ for a fixed $(P, G)$, or does it map full epistemic/preference states $(\mathcal{P} \times \mathcal{G} \times \mathcal{X}) \to \mathcal{A}$?**

* **Our Operational Proposal:** We propose treating $(P, G)$ as the fixed **prior architectural index** of the decision node $\textsc{pfdt}(\underline{P}, \underline{G})$, and encoding all contingent variations in observations, indexical roles, and disposition-induced preferences (such as the lesion in the Smoking Lesion problem) as components of the runtime input $x \in \mathcal{X}$. 

To see why this operationalization is vastly cleaner than the reference paper's treatment of the Smoking Lesion problem, recall Section 6 of Yudkowsky and Soares (2017). There, to model an agent whose lesion causes her to love smoking ($\mathcal{U}_S$ vs. $\mathcal{U}_R$), the authors had to posit *two separate probability distributions* $P^F_S$ and $P^F_R$ and two separate graph nodes $\textsc{fdt}(\underline{P^F_S}, \underline{G^F})$ and $\textsc{fdt}(\underline{P^F_R}, \underline{G^F})$, forcing the agent to compute her action "under ignorance about her own preferences" while introducing an extraneous prior probability $q = P^F_S(\textsc{fdt}(\underline{P^F_R}, \underline{G^F}) = \textit{smoke})$.

Under our operationalization of **P-FDT**, there is a single prior model $(P, G)$ and a single internal input $x \in \mathcal{X} = \{\textit{crave}, \textit{dislike}\}$ representing the agent's experienced gustatory preference for smoking (caused by $\textsc{Lesion}$). The agent selects a policy $\pi: \{\textit{crave}, \textit{dislike}\} \to \{\textit{smoke}, \textit{refrain}\}$ by intervening on $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$. Because $\textsc{Lesion}$ and $\textsc{Cancer}$ are upstream of $\textsc{Obs}$ and not downstream of $\textsc{pfdt}(\underline{P}, \underline{G})$, changing $\pi$ has zero effect on cancer in either branch; the policy $\pi^*(\textit{crave}) = \textit{smoke}, \pi^*(\textit{dislike}) = \textit{refrain}$ uniquely maximizes expected utility without any need for duplicate probability distributions $P^F_S, P^F_R$ or arbitrary beliefs $q$.

### Open Question 2: Zero-Probability Observations and Off-Path Indifference

In **P-FDT**, the agent chooses $\pi^*$ to maximize the unconditional expectation $\mathbb{E}\left[\textsc{V} \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)\right]$. What happens if, under two candidate policies $\pi_1$ and $\pi_2$, a particular observation $x_0 \in \mathcal{X}$ has **probability zero** of occurring *and* no predictor in $G$ queries $\pi(x_0)$?

First, note a subtle point that often confuses newcomers to **P-FDT**: in dilemmas with an *infallible* predictor—such as the **Mechanical Blackmail** problem (Dilemma 8) with a $100\%$ accurate blackmailer—if the agent adopts a policy $\pi$ with $\pi(\textit{blackmail}) = \textit{refuse}$, the blackmailer predicts refusal and *never sends the blackmail letter*. Thus, under $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$, the observation $x = \textit{blackmail}$ occurs with probability $0$! Does that make **P-FDT** indifferent between $\pi(\textit{blackmail}) = \textit{refuse}$ and $\pi(\textit{blackmail}) = \textit{pay}$? **No!** Even though $P(\textsc{Obs} = \textit{blackmail} \mid \mathtt{do}(\textsc{pfdt} = \pi)) = 0$ when $\pi(\textit{blackmail}) = \textit{refuse}$, the blackmailer's decision node $\textsc{Blackmailer}$ in $G$ is a direct function of $\pi(\textit{blackmail})$:
* If $\pi(\textit{blackmail}) = \textit{refuse}$, $\textsc{Blackmailer}$ does not run the program, and $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi)] = \$0$.
* If $\pi(\textit{blackmail}) = \textit{pay}$, $\textsc{Blackmailer}$ runs the program, the agent observes $\textit{blackmail}$ and pays, and $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi)] = -\$1,000$.
Thus, $\pi(\textit{blackmail}) = \textit{refuse}$ is strictly preferred even when $\textit{blackmail}$ has zero realized probability!

However, what if an observation $x_0 \in \mathcal{X}$ is genuinely unreachable and unqueried under $\pi^*$ (for example, theblackmailer has $0\%$ error when predicting refusal, and if she *didn't* send the blackmail, there is some unexpected sub-observation $x_0$ that happens with probability $0$)? Then $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi)]$ is invariant to $\pi(x_0)$, creating a tie in $\operatorname*{argmax}_{\pi \in \Pi}$.

* **Our Operational Proposal (Trembling-Hand Policy Regularization):** Whenever multiple policies $\Pi^* \subset \Pi$ tie in Stage 1 because an observation $x_0$ has zero probability and zero subjunctive influence along the optimal path, we propose breaking ties via an $\varepsilon$-trembling-hand perturbation $P_\varepsilon$ (where every observation $x \in \mathcal{X}$ has at least probability $\varepsilon > 0$ of being generated by exogenous noise, taking the limit $\varepsilon \to 0^+$), or equivalently by conditioning on $\textsc{Obs} = x_0$ as a secondary lexicographic tie-breaker among policies in $\Pi^*$. This guarantees that $\pi^*(x)$ is uniquely and sensibly defined for every $x \in \mathcal{X}$.

### Open Question 3: Computational Complexity and Deducing the Subjunctive Graph $G$

Two further challenges must be noted when scaling **P-FDT**:
1. **Exponential Policy Space ($|\mathcal{A}|^{|\mathcal{X}|}$):** While Action-FDT iterates over $|\mathcal{A}|$ actions at runtime, **P-FDT** iterates over $|\Pi| = |\mathcal{A}|^{|\mathcal{X}|}$ policies. When $|\mathcal{X}|$ is large, brute-force enumeration of $\Pi$ is intractable. However, whenever the graphical model $G$ exhibits conditional independence across disjoint observation subsets (for example, when observations $x_1$ and $x_2$ do not jointly feed into any common predictor or multi-agent payoff node), the objective function $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi)]$ decomposes additively across $x \in \mathcal{X}$, allowing dynamic programming or local optimization over independent sub-policies.
2. **Constructing the Subjunctive Graph $G$:** As Yudkowsky and Soares emphasize in Section 5, "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." **P-FDT** assumes $G$ is given as part of the world-model. In practical applications, constructing $G$ requires identifying every physical subsystem (twin, predictor, or future self) whose causal mechanism simulates, copies, or converges on the same normative decision rule as the agent, and drawing directed edges from $\textsc{pfdt}(\underline{P}, \underline{G})$ to those subsystems.

---

## 6. Step-by-Step Procedure for Applying P-FDT to Unfamiliar Problems

To decide any unfamiliar decision problem using **P-FDT**, apply the following five-step algorithm:

1. **Specify the Spaces ($\mathcal{X}, \mathcal{A}, \Pi, \mathcal{O}$):** List all possible observations $\mathcal{X}$ the agent (or her copies) might receive in the dilemma, all available actions $\mathcal{A}$, the policy space $\Pi = \mathcal{A}^{\mathcal{X}}$, and the utility function $\mathcal{U}: \mathcal{O} \to \mathbb{R}$.
2. **Construct the Subjunctive Graph $G$ and Prior $P$:** Include a single root policy node $\textsc{pfdt}(\underline{P}, \underline{G}) \in \Pi$. Draw directed edges from $\textsc{pfdt}(\underline{P}, \underline{G})$ to:
   * the agent's own physical action node $\textsc{Act}$ (alongside an incoming edge from $\textsc{Obs}$, with $\textsc{Act} = \pi(\textsc{Obs})$);
   * the action nodes $\textsc{Act}_i = \pi(\textsc{Obs}_i)$ of any identical copies or psychological twins sharing the algorithm; and
   * the prediction nodes $\textsc{Prediction}_j$ of any predictors who simulate or predict the agent's response to one or more observations.
   Do *not* draw edges from $\textsc{pfdt}(\underline{P}, \underline{G})$ to merely statistical common causes (like a genetic lesion or a pre-existing termite infestation).
3. **Evaluate Candidate Policies (Stage 1):** For each policy $\pi \in \Pi$, perform the graphical intervention $\mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)$ on the *unconditioned* prior model $(P, G)$, propagate the functional assignment $\pi$ through all downstream nodes, and compute $\mathbb{E}\left[\textsc{V} \mid \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right]$.
4. **Select the Optimal Policy $\pi^*$:** Choose $\pi^* \in \operatorname*{argmax}_{\pi \in \Pi} \mathbb{E}\left[\textsc{V} \mid \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right]$, using trembling-hand regularization ($\varepsilon \to 0^+$) to break any ties on zero-probability, unqueried observations.
5. **Apply the Actual Observation (Stage 2):** Given the observation $x \in \mathcal{X}$ actually received, execute the action $a^* = \pi^*(x)$.

| Dilemma | EDT Prescription | CDT Prescription | Action-FDT Prescription | P-FDT Prescription |
| :--- | :--- | :--- | :--- | :--- |
| **Newcomb's Problem** | One-box | Two-box | One-box | One-box |
| **Smoking Lesion** | Refrain | Smoke | Smoke (requires $q$ parameter) | Smoke (no $q$ parameter needed) |
| **Transparent Newcomb / Hitchhiker** | Two-box / Defect | Two-box / Defect | One-box / Pay (requires $q$ parameter) | One-box / Pay (no $q$ parameter needed) |
| **XOR Blackmail** | Pay | Refuse | Refuse | Refuse |
| **Mechanical Blackmail** | Pay | Pay | Refuse | Refuse |
| **Distributed Twin Coordination** | Fails under bad priors | Defects / Miscoordinates | Fails under bad cross-branch prior $q$ | **Succeeds (Global Policy Optimum)** |

---

## 7. Conclusion

By shifting the unit of subjunctive intervention from an isolated action token to a complete policy $\pi: \mathcal{X} \to \mathcal{A}$, **Policy Functional Decision Theory (P-FDT)** fulfills the philosophical vision of Yudkowsky and Soares (2017). Like Action-FDT, **P-FDT** one-boxes in Newcomb's problem, smokes in the Smoking Lesion problem, pays the driver in Parfit's Hitchhiker problem, and resists extortion in both XOR and Mechanical Blackmail—acting naturally as an agent would have ideally precommitted to act, without costly precommitment rituals or negative value of information. Yet by intervening on a single policy node $\textsc{pfdt}(\underline{P}, \underline{G})$ rather than separate observation-indexed action nodes, **P-FDT** eliminates arbitrary prior parameters over unvisited observation branches and enables identical agents with asymmetric observations to achieve optimal distributed coordination.

## References

* Dai, W. (2009). "Towards a New Decision Theory." *Less Wrong*.
* Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Gibbard, A., & Harper, W. L. (1978). "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, Vol. 1. D. Reidel.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Kleene, S. C. (1938). "On Notation for Ordinal Numbers." *Journal of Symbolic Logic*, 3(4), 150–155.
* Lewis, D. (1979). "Prisoners' Dilemma is a Newcomb Problem." *Philosophy & Public Affairs*, 8(3), 235–240.
* Pearl, J. (1996). "Causation, Action, and Counterfactuals." In *6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-'96)*, 51–73.
* Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Yudkowsky, E. (2010). *Timeless Decision Theory*. The Singularity Institute.
* Yudkowsky, E., & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. Machine Intelligence Research Institute (arXiv:1710.05060v2).
````

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Approach**

I'm focusing on defining the approach. Currently, my goal is to frame the essay or blog post from a researcher's viewpoint. I'm prioritizing clarity in explaining P-FDT and its application to decision problems, specifically targeting an expert audience familiar with the field. I intend to build the narrative around the provided paper as the core source material.


**Clarifying the Focus**

I'm now clarifying the focus on policy selection within P-FDT. I've pinpointed Footnote 16 and related Footnote 7 in the Yudkowsky and Soares paper as the jumping-off point. My intention is to analyze the implications of this policy-based approach. The target audience is experts familiar with formal procedures and philosophical motivations, and I'm treating this paper as the foundational source.


**Elaborating the Framework**

I'm now elaborating on the formal framework for Policy-based FDT. My current focus is including mathematical definitions and examples. I need to ensure a precise account so the reader can apply the content. I'm actively working on explaining how P-FDT evaluates actions, and the treatment of dependencies, including counterfactuals. Further, I'm working to make the distinctions between this and Action-FDT clear. I'm working on several uncertainties found in the original source, and making an operational interpretation.


**Refining the Structure**

I'm presently focused on structuring the essay for clarity and impact. I'm prioritizing consistent naming conventions, using "P-FDT" throughout while clearly differentiating it from other theories like EDT and CDT. I'm incorporating faithful quotations from the source to maintain accuracy. The planned format is a substantive, mathematically-grounded essay with headings and examples, avoiding lengthy bibliographies or appendices, and concluding briefly. I'm aiming for a word count between 2,400 and 3,000 words to ensure thoroughness within the scope. I am also planning on including the standard FDT equation from the paper.


**Analyzing the Formula**

I'm now analyzing the core FDT formula and how it handles observations, particularly in cases with multiple possible observations. I'm focusing on the change in the intervention node within the graph $G$ and how alternative observations are represented. For instance, I'm examining how we treat the value of $\textsc{fdt}(\underline{P}, \underline{G}, \textit{empty})$ as a separate random variable in $P$ within $\textsc{fdt}(\underline{P}, \underline{G}, \textit{full})$. I'm going to look closely at Footnotes 7 and 16 to clarify.


**Clarifying P-FDT Policies**

I am clarifying the implementation of policies within P-FDT. I've realized that the paper focuses on iterating policies (observation-to-action mappings) rather than individual actions, which is important in multi-agent dilemmas. My focus now is understanding how this affects the mathematical formulation of P-FDT, especially the selection of a policy $\pi \in \Pi$, where $\Pi = \mathcal{A}^{\mathcal{X}}$. I am working to define how full inputs (P,G,x) are mapped to A to achieve clean operationalization, as described in the paper.


**Differentiating P-FDT Actions**

I'm now differentiating between policy-based and action-based FDT implementations, as described in Footnote 16. I'm focusing on the two-step process to operationalize P-FDT. The core of my analysis is using the provided equations to specify this difference, including $\pi^* = \operatorname*{argmax}_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right)$ and  $\mathrm{PFDT}(P, G, x) \coloneqq \pi^*(x)$. This should clarify how policies are selected and applied relative to Action-FDT.


**Examining the Differences**

I'm now examining the critical differences in how P-FDT handles observations compared to standard FDT. I'm focusing on the implications of a single policy node, rather than individual action nodes. I'm also considering the multi-agent dilemma caveat, and checking how single-agent scenarios are effected by multiple observation nodes and uncertainty. I'm actively analyzing the impact of these distinctions in specific examples.


**Analyzing Newcomb Scenarios**

I'm now analyzing Transparent Newcomb scenarios. The focus is contrasting Action-FDT and P-FDT, especially with errors and payoff structures that couple observation branches. I'm focusing on how the predictor accuracy of 99% impacts the value calculation of *onebox* and *twobox*. I'm now looking at how this applies to multi-agent scenarios or the value of one agent observing in multiple information sets. I am looking at how to model a single-agent problem where reward is conditioned by the predictor.


**Investigating Joint Behaviors**

I am now investigating joint behavior in multi-agent dilemmas, particularly with psychological twins. Analyzing the implications of each agent only observing local input. Currently, I'm examining how Action-FDT might not vary the action of the other twin, leading to uncertainty if multiple equilibria exist, and how this impacts overall utility.


**Verifying Multi-Agent Behavior**

I'm verifying the claim that P-FDT's focus on policy iteration distinguishes it from Action-FDT in multi-agent dilemmas. I've realized that in asymmetric observation scenarios, Action-FDT's local optimization per observation leads to a Bayesian Nash Equilibrium, while P-FDT optimizes the joint policy across all observations. This is a mathematically precise way to explain Footnotes 7 and 16. I am now checking this with several more cases.


**Analyzing Twin Coordination**

I'm now analyzing twin coordination in multi-agent dilemmas. Action-FDT might not change the other twin's action due to independent observation nodes. This can lead to uncertainty in the existence of multiple equilibria, which can affect the overall utility in coordinated trade-off situations.


**Revisiting Sacrifice Scenarios**

I'm revisiting the asymmetric sacrifice scenario to clarify P-FDT's behavior. I am analyzing the implications when Action-FDT fails to coordinate, leading to uncertainty in equilibria, and how this affects utility. I am now exploring scenarios involving a red twin giving and a blue twin keeping, to clarify how P-FDT can solve this dilemma.


**Clarifying Room Observations**

I'm now clarifying how observations in distinct rooms affect action choices, focusing on the asymmetric twin prisoner's dilemma. In the room scenario, I am looking at the individual optimization of action FDT when viewing $x = \textit{room1}$. I'm focusing on the payoff structure that occurs in asymmetric versions of this dilemma, and how the twins have different views of the environment.


**Analyzing Room Dilemmas**

I'm now analyzing Action-FDT within the asymmetric twin prisoner's dilemma, specifically in the "room" scenario. I'm focusing on why Action-FDT evaluates the expected value using the unconditioned prior $P$ when calculating $\mathrm{FDT}(P, G, x)$. I'm considering why intervening on the action in Room 1 doesn't influence the twin's action in Room 2. This seems important to understanding the equilibria that arise in this situation.


**Revisiting Room Scenarios**

I'm revisiting the room scenarios, particularly the implications of indexical uncertainty and joint payoffs in the twin dilemma. I've realized that if there's no indexical uncertainty, or if payoffs depend on joint actions, the initial Action-FDT analysis might be insufficient. I'm tracing the cases of Alice and Bob twins, where each gets a million dollars *only* if Room 1 and Room 2 cooperate, and will re-check my calculations.


**Analyzing Twin Utility**

I'm now analyzing the utility outcomes in the twin scenario, focusing on Action-FDT where each twin's action depends on their local room observation. I see now that each twin's decision hinges on their prior belief, represented as `q`, over the other twin's action, leading to a negative expected utility in this version of the dilemma. This analysis should help clarify the divergence in outcome from P-FDT.


**Examining Indexical Uncertainty**

I'm now examining the impact of indexical uncertainty on utility outcomes in the twin scenario when using Action-FDT. A key insight is that separate observation branches lead to potential bad equilibria and coordination failures due to pessimistic priors. This extends to scenarios where cooperation from one agent exclusively benefits the other, highlighting the limitations of Action-FDT.


**Clarifying Branch Coordination**

I'm now clarifying branch coordination in multi-agent dilemmas, focusing on the treatment of external random variables, specifically the distinction in how P-FDT and Action-FDT evaluate payoffs across multiple observations. I'm focusing on the payoff being dependent on the joint action of both policies derived from $x_1$ and $x_2$. I'm exploring the implications for multi-agent games with joint payoffs.


**Analyzing Prior Sensitivities**

I'm now analyzing the impact of prior probabilities on action selection, particularly focusing on how these probabilities affect the decision-making process in multi-agent and joint-payoff scenarios. I'm exploring how Action-FDT, under specific conditions, introduces sensitivities to priors, potentially undermining the robust decision-making FDT aims for. This analysis is prompted by the original paper's analysis of scenarios where the dependence on `q` does NOT cancel out.


**Defining Joint Functionality**

I'm now defining joint functionality between policies, as described by the policy-based FDT. The function $\pi$ maps from observation to action, and the policy iterates over the total space of observations, so there is no local belief variable like `q`. This ensures the policy simultaneously addresses all possible observations. I am now working on clarifying this aspect.


**Defining Policy Operations**

I am now defining the policy operations in P-FDT. The policy $\pi$ maps from observation to action, while Action-FDT has a local belief variable, `q`. P-FDT considers the whole space of observations, so belief-updating is part of the policy selection. This guarantees that all potential observations are addressed simultaneously, and that there are no local beliefs.


**Comparing Decision Frameworks**

I'm now comparing EDT, CDT, Action-FDT, and P-FDT equations to clarify their differences. I'm focusing on how P-FDT's policy-based approach impacts the overall formulation and application. The key is in $\pi^*_{(P,G)}$, which optimizes over policies rather than single actions, as shown in the last two equations. This should highlight how P-FDT solves multi-agent dilemmas.


**Describing Policy Nodes**

I'm now describing the graphical architecture of P-FDT. Unlike Action-FDT, P-FDT uses a single policy node, pfdt(P, G), which outputs the policy $\pi$. Physical actions are determined by evaluating the policy at a realized observation: $\textsc{Act} = \mathrm{eval}(\textsc{pfdt}(\underline{P}, \underline{G}), \textsc{Obs}) = \pi(\textsc{Obs})$, while predictors query $\pi(x')$ directly from $\textsc{pfdt}(\underline{P}, \underline{G})$. I'm going to clarify the implications of using an updateless observation in P-FDT, to contrast it with Action-FDT.


**Evaluating Transparent Newcomb**

I'm now evaluating Transparent Newcomb scenarios, focusing on policy evaluation. I'm aiming to work through a step-by-step example using P-FDT to demonstrate agreement with Action-FDT. I am actively working on clarifying how P-FDT avoids the arbitrary logical prior $q$ by directly comparing policies, showcasing the precise expected utility calculations.


**Analyzing Twin Coordination**

I'm now analyzing the Asymmetric-Information Twin Coordination Game, demonstrating where Action-FDT and P-FDT diverge mathematically. Each twin observes a local variable $x_1$ or $x_2$, leading to potentially different action selections. I'm focusing on scenarios where joint outcomes depend on both twins' actions, and how Action-FDT can fail to coordinate effectively due to local optimization.


**Clarifying Twin Payoffs**

I'm now clarifying the implications for Action-FDT when observations and actions are divided across twins in a joint payoff scenario. With Action-FDT, intervening on $x=\textit{A}$ only affects $\textsc{fdt}(\underline{P}, \underline{G}, \textit{A})$, leaving $\textsc{fdt}(\underline{P}, \underline{G}, \textit{B})$ unchanged. This means Action-FDT might not achieve the maximum, due to pessimistic priors or asymmetric payoffs. Under P-FDT, both twins intervene on a single policy $\pi$, optimizing jointly. I am carefully distinguishing source claims from open questions, and clarifying the inputs to the policy.


**Operationalizing Policy Selection**

I'm now operationalizing policy selection to resolve a discrepancy in the paper. I'm focusing on defining the policy $\pi$ mapping observations $\mathcal{X}$ to actions $\mathcal{A}$ for a fixed $(P, G)$, addressing whether the mapping depends on $(P, G)$. I'm also ensuring that this operationalization simplifies the Smoking Lesion problem by treating $(P, G)$ as a fixed node index. I'm actively working to clarify this.


**Refining Observation Weights**

I'm now refining how P-FDT handles observations with zero probability or those not directly queried by predictors, particularly in scenarios such as mechanical blackmail. I'm focusing on why a policy's decision still matters even if its observation is never reached. My next step will be to formulate an $\varepsilon$-perturbation or tie-breaking rule to account for these situations, focusing on implications for policy stability.


**Operationalizing Policy Design**

I'm now operationalizing policy design within P-FDT to address the exponential growth in policy space with the size of observations, and also the difficulty of determining the dependency graph G. I'm focusing on incorporating structured policy spaces, potentially through modular graphical models, to operationalize P-FDT in practical applications. My final steps include a section synthesizing P-FDT's fulfillment of functional decision theory's philosophical and mathematical goals and checking the word count and tone. I'm also ensuring all calculations are correct.


**Evaluating Action-FDT Choices**

Now, I'm evaluating the Action-FDT choices in a Transparent Newcomb scenario. Specifically, I'm carefully checking the expected utility calculations for both "onebox" and "twobox" options, particularly when considering the predictor's accuracy and the outcomes from both full and empty boxes, correcting a typo in the provided source text. I'm focusing on the payoff structures.


**Revisiting Newcomb Scenarios**

I'm now revisiting Newcomb scenarios with transparent box contents. I am actively working on the math in the provided example and correcting errors, now focusing on the precise calculation of expected utilities for each policy in P-FDT. I'm verifying that P-FDT's policy-based approach ensures rational choices in these cases.


**Refining Newcomb Calculations**

I am now refining the Newcomb scenario calculations using the provided equations to clarify P-FDT's solution and correct source errors. I've re-calculated expected utility for all policies and verified that P-FDT uniquely maximizes the utility at $990,010, demonstrating the superior performance of P-FDT over Action-FDT.


**Analyzing Twin Cooperation**

Now I'm analyzing the implications of the twin scenario, specifically focusing on how Action-FDT evaluates the joint payoff structure where observations are divided across twins. I am working to define how intervening on action 'A' affects the action 'B', given the joint payoff structure. I see that each twin's decision making process is independent.


**Clarifying Joint Payoffs**

I'm now clarifying the implications of joint payoffs in Action-FDT within the twin scenario. The expected utility calculation shows that intervening on one twin's action, A, leaves the probability of the other twin's cooperation, $q$, unchanged. My focus is now on the agent's expected utility. I am currently recalculating these values.


**Calculating Twin Payoffs**

I'm now calculating Action-FDT payoffs in the asymmetric twin prisoner's dilemma, focusing on outcomes from the perspective of the donor. With a donation of \$1000 from the donor, and a million-dollar payoff to the recipient, the donor only values their own action, and may choose to defect if the belief on the other twin's action is sufficiently low. The value to the donor is thus $-1000$, and the value to the recipient is $1,000,000$.


**Calculating Twin Payoffs**

Now, I'm analyzing the asymmetric twin prisoner's dilemma, focusing on action costs. I'm clarifying how each twin's expected payoff is calculated. With Action-FDT and the twins separated by room, each calculates the outcome as $-1000$ or $+1,000,000$, and the belief on the other twin's action, $q$, is crucial.


**Refining Room Scenarios**

I'm now refining the room scenarios by clarifying the utility outcomes using Action-FDT, considering both non-indexical and indexical interpretations of the utility function. I'm calculating the payoff to Alice as -$1000, and $1000000 to Bob. I'm focusing on evaluating the utility to both players in the different rooms, using the updated payoff structures.


**Analyzing Coordination Games**

I'm now analyzing coordination games with multiple equilibria, specifically a distributed Battle of the Sexes scenario. My focus is on the impact of separate room observations with asymmetric payoffs. Action-FDT leads to local optimization, while P-FDT ensures coordinated policy selection. This will highlight potential inefficiencies with Action-FDT.


**Examining Twin Equilibria**

I'm now examining the impact of asymmetric payoffs in twin scenarios on equilibrium selection. In the asymmetric scenario, each twin independently values their local observation, which can lead to miscoordination or suboptimal equilibria. This approach highlights the transparency of global vs. local action selection.


```
