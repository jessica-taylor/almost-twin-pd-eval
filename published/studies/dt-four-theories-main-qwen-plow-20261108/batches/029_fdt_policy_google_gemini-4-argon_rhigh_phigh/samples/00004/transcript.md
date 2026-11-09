# 029_fdt_policy_google_gemini-4-argon_rhigh_phigh / 00004

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/7810e6a5-e8bb-4a92-a66a-eb1f474b7fe3/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/7810e6a5-e8bb-4a92-a66a-eb1f474b7fe3/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Policy Functional Decision Theory (P-FDT): Formalism, Subjunctive Counterfactuals, and Multi-Agent Coordination

## 1. Introduction: From Physical Acts to Mathematical Policies

Classical normative decision theory is divided between two standard accounts of instrumental rationality: **Evidential Decision Theory (EDT)** and **Causal Decision Theory (CDT)**. Both theories endorse expected utility maximization, yet they disagree on the epistemic perspective from which candidate actions should be evaluated. An EDT agent asks which action would provide the best news if she learned she had taken it, evaluating actions by standard Bayesian conditioning. A CDT agent asks which physical act would *cause* the best outcome, evaluating actions via causal interventions that hold the past and all causal independents fixed. 

As a result of this divergence, each theory fails systematically in well-known decision dilemmas. CDT two-boxes in Newcomb's problem and defects in the psychological twin prisoner's dilemma, walking away poor against reliable predictors and symmetric reasoners. EDT one-boxes in Newcomb's problem, but it also counterproductively "manages the news" in common-cause environments—refraining from smoking in Skyrms's smoking lesion problem and capitulating to extortion in the XOR blackmail problem.

In *Functional Decision Theory: A New Theory of Instrumental Rationality*, Eliezer Yudkowsky and Nate Soares (2017) introduce a third paradigm. Rather than treating a decision as an isolated physical event (CDT) or an piece of statistical evidence (EDT), functional decision theory treats a decision as the output of a *fixed mathematical function*. An agent implementing this algorithm evaluates her options by asking: *"Which output of this very function would yield the best outcome?"* Because predictors' simulations of the agent and computational twins of the agent compute this same mathematical function, their behaviors *subjunctively depend* on its output.

However, a careful reading of Yudkowsky and Soares (2017) reveals two distinct formalizations of this principle. Throughout the main body of their paper, for expository simplicity, the authors formalize what we will call **Action-FDT** (their Equation 4), in which the decision function intervenes on a node representing the *action* output for a specific observation. Yet in Footnotes 7 and 16, the authors explain that their preferred foundational theory actually selects a *policy* rather than an individual action:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper." (Footnote 7)

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition." (Footnote 16)

In this essay, we develop a formal mathematical account of **Policy Functional Decision Theory (P-FDT)** based on this policy-selection principle. We will establish the exact mathematical equations governing P-FDT, explain how it models subjunctive dependencies and counterfactual observations, show why P-FDT diverges from Action-FDT in multi-agent dilemmas (and certain single-agent predictive dilemmas), and provide an operational procedure for applying P-FDT to unfamiliar cases. Where the brief remarks in Footnotes 7 and 16 leave formal details open, we will highlight those uncertainties and formulate principled mathematical completions.

---

## 2. The Formal Architecture of P-FDT

### 2.1 Decision-Theoretic Primitives

Following Section 5 of Yudkowsky and Soares (2017) and the representation theorem of Joyce (1999), let us fix the mathematical primitives of a decision problem:

* $\mathcal{O} = \{o_1, o_2, \dots\}$ is a countable set of possible world outcomes.
* $\mathcal{U} : \mathcal{O} \to \mathbb{R}$ is a bounded utility function, and $\textsc{V} \coloneqq \mathcal{U}(\textsc{Outcome})$ is the random variable representing the utility of the realized outcome.
* $\mathcal{A}$ is a finite set of available physical actions $a$.
* $\mathcal{X}$ is a countable (and in typical finite dilemmas, finite) set of possible observations or observation histories $x$.

In general expected utility theory, an agent who has received observation $x \in \mathcal{X}$ evaluates a candidate choice by constructing a hypothetical probability distribution $P(a \hookrightarrow o_j ;\, x)$ and maximizing expected utility:
$$\mathcal{EU}(a) \coloneqq \sum_{j} P(a \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j).$$

In **EDT**, the agent's world-model is a prior probability distribution $P$, and the hypothetical connective $\hookrightarrow$ is interpreted as Bayesian conditioning on both the observation $\textsc{Obs} = x$ and the physical action $\textsc{Act} = a$:
$$\mathrm{EDT}(P, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs} = x,\, \textsc{Act} = a\right).$$

In **CDT**, using Pearl's (1996, 2000) graphical causal framework, the agent's world-model is a pair $M = (P, G)$, where $G$ is a directed acyclic graph (DAG) encoding causal relationships among the variables in $P$. A CDT agent conditions on her observation $\textsc{Obs} = x$ and performs a causal surgery $\mathtt{do}(\textsc{Act} = a)$ that severs all incoming arrows into the physical action node $\textsc{Act}$:
$$\mathrm{CDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{Act} = a),\, \textsc{Obs} = x\right).$$

In **Action-FDT** (the simplified version of functional decision theory presented in Equation 4 of Yudkowsky and Soares), the graph $G$ is expanded beyond physical causation to include *logical and computational dependencies*. Specifically, $G$ includes variables $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ representing the output of the Action-FDT algorithm when given inputs $(P, G, x)$ (where underlines denote dequoting: if $x = \textit{full}$, then $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ is the variable name $\textsc{fdt}(\underline{P}, \underline{G}, \textit{full})$). Action-FDT selects an action according to:
$$\mathrm{FDT}_{\text{act}}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right).$$

Notice that in Action-FDT, every distinct observation $x \in \mathcal{X}$ corresponds to a *separate* logical variable $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ in the graph $G$.

### 2.2 Defining Policies and the P-FDT Equations

**P-FDT** replaces action-level intervention with policy-level intervention. Let a **policy** be a function $\pi : \mathcal{X} \to \mathcal{A}$ that maps each possible observation $x \in \mathcal{X}$ to an action $\pi(x) \in \mathcal{A}$. Write $\Pi \coloneqq \mathcal{A}^{\mathcal{X}}$ for the space of all candidate policies (or a designated admissible subset thereof, a subtlety we examine in Section 5).

In a P-FDT world-model $M = (P, G)$, the agent does not maintain separate root nodes for each observation history. Instead, $G$ contains a single logical node $\textsc{pfdt}(\underline{P}, \underline{G})$ whose state space is the policy set $\Pi$. This node represents the mathematical policy output by the P-FDT decision function on the prior model $(P, G)$. (As noted by Yudkowsky and Soares, the self-reference of a model $(P, G)$ containing a node named $\textsc{pfdt}(\underline{P}, \underline{G})$ is formally benign and can be constructed via Kleene's (1938) second recursion theorem).

Within the graph $G$, the agent's physical action $\textsc{Act}$ is a deterministic child of *both* the policy node $\textsc{pfdt}(\underline{P}, \underline{G})$ and the observation node $\textsc{Obs}$, governed by the structural equation of function application:
$$\textsc{Act}\big(\pi, x\big) \coloneqq \pi(x).$$

Similarly, any external process in the environment that predicts or replicates the agent—such as Newcomb's predictor, a blackmailer, or a computational twin—is modeled in $G$ as a descendant of the policy node $\textsc{pfdt}(\underline{P}, \underline{G})$.

Following Footnote 16, P-FDT operates in two distinct stages:

1. **Global Policy Selection**: The agent intervenes on the logical node $\textsc{pfdt}(\underline{P}, \underline{G})$ to find the policy $\pi^* \in \Pi$ that maximizes unconditional expected utility across the entire world-model $(P, G)$:
   $$\pi^* = \mathrm{PFDT}_{\text{policy}}(P, G) \coloneqq \argmax_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right). \tag{P-FDT.1}$$

2. **Local Policy Application**: The agent applies the selected policy $\pi^*$ to her actual observation $x \in \mathcal{X}$ to output a concrete action in $\mathcal{A}$:
   $$\mathrm{PFDT}(P, G, x) \coloneqq \big[\mathrm{PFDT}_{\text{policy}}(P, G)\big](x) = \left[\argmax_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right)\right](x). \tag{P-FDT.2}$$

By the law of total expectation over the observation variable $\textsc{Obs}$, we can expand the objective function in Equation (P-FDT.1) explicitly as:
$$\mathcal{EU}_{\text{P-FDT}}(\pi) \coloneqq \sum_{x' \in \mathcal{X}} P\left(\textsc{Obs} = x' \;\middle|\; \mathtt{do}\big(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\big)\right) \cdot \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs} = x',\, \textsc{Act} = \pi(x'),\, \mathtt{do}\big(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\big)\right). \tag{P-FDT.3}$$

Equation (P-FDT.3) crystallizes the mathematical structure of P-FDT: a policy $\pi$ affects expected utility both by determining the conditional action $\pi(x')$ taken at each observation branch $x'$, *and* by subjunctively shifting the probability distribution $P(\textsc{Obs} = x' \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi))$ over which observations the agent is likely to encounter in the first place.

---

## 3. Subjunctive Dependence, Updatelessness, and Counterpossibles in P-FDT

### 3.1 Subjunctive Dependence and Counterpossible Reasoning

To understand how P-FDT evaluates hypotheticals, we must examine the philosophical motivation behind intervening on $\textsc{pfdt}(\underline{P}, \underline{G})$. Yudkowsky and Soares define *subjunctive dependence* as the logical or computational interdependence that holds between physical systems implementing or modeling the same mathematical function:

> "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function. ... *Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*" (Section 3)

In Peirce's (1934) terminology, CDT intervenes on the physical *token* $\textsc{Act}$ ("what if my body moved differently right now, holding the rest of the universe fixed?"), whereas P-FDT intervenes on the mathematical *type* $\textsc{pfdt}(\underline{P}, \underline{G})$ ("what if the P-FDT function itself evaluated to policy $\pi$ on inputs $(P, G)$?").

Because $\mathrm{PFDT}_{\text{policy}}(P, G)$ is a deterministic mathematical function, it has a unique true output $\pi^*$ of logical necessity. Consequently, for any alternative policy $\pi \neq \pi^*$, the antecedent $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$ is a *counterpossible*—a counterfactual whose antecedent is logically impossible, akin to asking what would follow if $6288 + 1048$ equaled $3159$ instead of $7336$. Ideally, as the source notes in Section 5, a complete theory of logical uncertainty would furnish an epistemic operator $\mathtt{true}(\phi)$ capable of conditioning a probability distribution directly on counterpossible logical claims. Because no general mathematical definition of $\mathtt{true}(\phi)$ currently exists, P-FDT (like Action-FDT) encodes subjunctive dependencies directly into the augmented graph $G$ and uses Pearl's $\mathtt{do}$ operator on the logical node $\textsc{pfdt}(\underline{P}, \underline{G})$.

### 3.2 Updatelessness and Counterfactual Observations

A striking feature of Equations (P-FDT.1) and (P-FDT.2) is *how* the agent uses her observation $x$. In both EDT and CDT, when the agent observes $\textsc{Obs} = x$, she immediately updates her probability distribution $P$ to $P(\cdot \mid \textsc{Obs} = x)$ before evaluating her options. Even early precursors to FDT, such as Yudkowsky's (2010) **Timeless Decision Theory (TDT)**, both conditioned on the observation $\textsc{Obs} = x$ *and* intervened on the logical decision node—a "double update" that fails in dilemmas where the predictor controls what observation the agent receives.

By contrast, P-FDT adopts the updateless architecture pioneered in Wei Dai's (2009) **Updateless Decision Theory (UDT)**. During the optimization step (P-FDT.1), the agent does *not* condition $P$ on $\textsc{Obs} = x$. Why? Because if the agent's policy $\pi$ were different, a predictor who anticipates $\pi$ might have caused the agent to receive a *different observation*. Updating on $\textsc{Obs} = x$ prior to policy selection would lock in the past observation as an immutable fact, blinding the agent to the ways her policy choice governs which observation branch she lands on.

### 3.3 Worked Single-Agent Example: P-FDT vs. Action-FDT in the Transparent Newcomb Problem

To see how P-FDT operates in practice—and how it cleans up a subtle formal artifact of Action-FDT—consider **The Transparent Newcomb Problem** (Drescher, 2006; Dilemma 5 in Yudkowsky and Soares, 2017):

* Box A is transparent and contains $\$1,000$. Box B is *also* transparent and contains either $\$1,000,000$ ($\textit{full}$) or $\$0$ ($\textit{empty}$).
* A predictor with $99\%$ accuracy ($\textsc{Accurate} = \textit{accurate}$ with probability $0.99$, and $\textit{inaccurate}$ with probability $0.01$) places $\$1,000,000$ in Box B if and only if she predicts that the agent would one-box ($\textit{1B}$) *upon observing that Box B is full*.
* The agent observes $\textsc{Obs} = \textit{full}$ and must choose between $\mathcal{A} = \{\textit{1B}, \textit{2B}\}$.

Both CDT and EDT prescribe two-boxing ($\textit{2B}$) upon seeing $\textsc{Obs} = \textit{full}$, since conditional on $\textsc{Obs} = \textit{full}$ the $\$1,000,000$ is already in Box B and taking both boxes yields $\$1,001,000 > \$1,000,000$. Foreseeing this, the predictor leaves Box B empty for CDT and EDT agents, who walk away with $\$1,000$.

Now compare how **Action-FDT** (Section 6 of the paper) and **P-FDT** analyze this problem:

In **Action-FDT**, the graph $G^F$ contains *two* separate decision nodes: $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full})$ and $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty})$. Upon observing $\textit{full}$, the Action-FDT agent intervenes *only* on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full}) = a$. Because there is a $1\%$ chance the predictor errs and leaves Box B empty, the Action-FDT agent must introduce an exogenous prior probability $q \coloneqq P^F(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty}) = \textit{2B})$ representing her uncertainty about what her own algorithm outputs when seeing an empty box! Her expected utilities under Action-FDT are:
$$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full}) = \textit{1B}\big)\right) = 0.99(\$1,000,000) + 0.01(q \cdot \$1,000) = \$990,000 + \$10q,$$
$$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full}) = \textit{2B}\big)\right) = 0.01(\$1,001,000) + 0.99(q \cdot \$1,000) = \$10,010 + \$990q.$$
Here Action-FDT prescribes $\textit{1B}$ regardless of $q \in [0,1]$, so the nuisance parameter $q$ happens to be harmless.

In **P-FDT**, no ungrounded parameter $q$ is needed. The observation space is $\mathcal{X} = \{\textit{full}, \textit{empty}\}$ and the action space is $\mathcal{A} = \{\textit{1B}, \textit{2B}\}$. There are $|\mathcal{A}|^{|\mathcal{X}|} = 2^2 = 4$ deterministic policies in $\Pi$, which we can write as pairs $\pi = (\pi(\textit{full}), \pi(\textit{empty}))$:
$$\Pi = \big\{(\textit{1B}, \textit{1B}),\; (\textit{1B}, \textit{2B}),\; (\textit{2B}, \textit{1B}),\; (\textit{2B}, \textit{2B})\big\}.$$
In the P-FDT graph $G$, the single node $\textsc{pfdt}(\underline{P}, \underline{G})$ determines both $\pi(\textit{full})$ (which the predictor evaluates to decide whether to fill Box B) and $\pi(\textit{empty})$. Using Equation (P-FDT.3), we compute the exact expected utility of each of the four policies under $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$:

| Policy $\pi = (\pi(\textit{full}), \pi(\textit{empty}))$ | $P(\textsc{Obs}=\textit{full} \mid \mathtt{do}(\pi))$ | Payoff if $\textit{full}$ | $P(\textsc{Obs}=\textit{empty} \mid \mathtt{do}(\pi))$ | Payoff if $\textit{empty}$ | Global Expected Utility $\mathcal{EU}_{\text{P-FDT}}(\pi)$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| $\pi_1 = (\textit{1B}, \textit{1B})$ | $0.99$ | $\$1,000,000$ | $0.01$ | $\$0$ | $\$990,000$ |
| $\pi_2 = (\textit{1B}, \textit{2B})$ | $0.99$ | $\$1,000,000$ | $0.01$ | $\$1,000$ | **$\$990,010$** |
| $\pi_3 = (\textit{2B}, \textit{1B})$ | $0.01$ | $\$1,001,000$ | $0.99$ | $\$0$ | $\$10,010$ |
| $\pi_4 = (\textit{2B}, \textit{2B})$ | $0.01$ | $\$1,001,000$ | $0.99$ | $\$1,000$ | $\$11,000$ |

By Equation (P-FDT.1), the unique optimal policy is $\pi^* = \pi_2 = (\textit{1B}, \textit{2B})$: one-box if Box B is full, and two-box if Box B is empty. Then, by Equation (P-FDT.2), upon actually observing $\textsc{Obs} = \textit{full}$, the P-FDT agent evaluates:
$$\mathrm{PFDT}(P, G, \textit{full}) = \pi^*(\textit{full}) = \textit{1B}.$$
And if the predictor ever made the $1\%$ error and the agent observed $\textsc{Obs} = \textit{empty}$, the agent would evaluate $\mathrm{PFDT}(P, G, \textit{empty}) = \pi^*(\textit{empty}) = \textit{2B}$, salvaging the $\$1,000$ in Box A.

---

## 4. Why Policies Matter: Multi-Agent Dilemmas with Asymmetric Observations

Why did Yudkowsky and Soares remark in Footnotes 7 and 16 that iterating over policies rather than actions *"makes a difference in certain multi-agent dilemmas"*? While the authors set this distinction aside in their paper without providing an explicit example, our formalization of P-FDT allows us to construct and prove the exact mechanism of this divergence.

### 4.1 The Asymmetric Twin Prisoner's Dilemma

In the standard **Psychological Twin Prisoner's Dilemma** (Dilemma 1 of the paper), two computational twins implementing the same decision algorithm with identical world-models $(P, G)$ are placed in separate rooms and face the exact same situation. Because they receive identical inputs, Action-FDT assigns both twins to the *same* logical variable $\textsc{fdt}(\underline{P}, \underline{G})$, so intervening on that variable changes both twins' actions together and secures mutual cooperation.

Now consider a slight variation—an **Asymmetric Twin Prisoner's Dilemma**—in which the two twins receive *different observations*:

> **Dilemma (Asymmetric Twin Prisoner's Dilemma).** Two computational twins, running the exact same decision algorithm with identical prior world-models $(P, G)$, are placed in separate rooms: one is placed in the **Red Room** (observing $x = \textit{Red}$) and the other is placed in the **Blue Room** (observing $x = \textit{Blue}$), determined by a fair coin flip so that the agent's prior probability of being the Red twin or the Blue twin is $1/2$ each. Each twin must independently choose whether to $\textit{Cooperate}$ ($\textit{C}$) or $\textit{Defect}$ ($\textit{D}$) with the other twin. Working in utilities (dollars), every $\textit{C}$ chosen by a twin bestows $\$1,000,000$ on the *other* twin at a personal cost of $\$1,000$ (so mutual cooperation yields $\$1,000,000$ each, mutual defection yields $\$1,000$ each, unilateral defection yields $\$1,001,000$, and unilateral cooperation yields $\$0$). You wake up and observe that you are in the Red Room ($\textsc{Obs} = \textit{Red}$). Should you cooperate or defect?

Let us compare how **Action-FDT** (Equation 4 of the paper) and **P-FDT** (Equations P-FDT.1–2) behave in this dilemma.

### 4.2 Why Action-FDT Fails and Collapses into Mutual Defection

Under **Action-FDT**, the decision function takes the observation $x \in \{\textit{Red}, \textit{Blue}\}$ as part of the variable name of the node being intervened upon. Thus, the graph $G$ contains two distinct logical nodes:
* $\textsc{fdt}(\underline{P}, \underline{G}, \textit{Red})$, which governs the action $\textsc{Act}_{\text{Red}}$ of the twin in the Red Room; and
* $\textsc{fdt}(\underline{P}, \underline{G}, \textit{Blue})$, which governs the action $\textsc{Act}_{\text{Blue}}$ of the twin in the Blue Room.

When the agent wakes up in the Red Room ($\textsc{Obs} = \textit{Red}$), Action-FDT instructs her to compute:
$$\mathrm{FDT}_{\text{act}}(P, G, \textit{Red}) = \argmax_{a \in \{\textit{C}, \textit{D}\}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \textit{Red}) = a\right)\right).$$

What happens when she performs the surgery $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \textit{Red}) = a)$? It sets the Red twin's action $\textsc{Act}_{\text{Red}} = a$, while leaving the *other* logical node $\textsc{fdt}(\underline{P}, \underline{G}, \textit{Blue})$ completely untouched! Let $q \coloneqq P(\textsc{fdt}(\underline{P}, \underline{G}, \textit{Blue}) = \textit{C})$ be her prior probability that the Blue twin cooperates. Because the agent has a $1/2$ prior probability of being the Red twin and a $1/2$ prior probability of being the Blue twin:
* If she is the Red twin (probability $1/2$), her own action is $a$ and her partner's action is $\textsc{Act}_{\text{Blue}}$ (which is $\textit{C}$ with probability $q$).
* If she is the Blue twin (probability $1/2$), her own action is $\textsc{Act}_{\text{Blue}}$ and her partner's action is $a$!

Wait—examine those two terms carefully! Under Action-FDT's updateless expectation over who she is:
* If she sets $\textsc{fdt}(\underline{P}, \underline{G}, \textit{Red}) = \textit{C}$, then:
  - In the $1/2$ world where she is Red, choosing $\textit{C}$ instead of $\textit{D}$ costs her $\$1,000$.
  - In the $1/2$ world where she is Blue, the Red twin's choice of $\textit{C}$ instead of $\textit{D}$ *gives* her $\$1,000,000$!
  Wait: what if the agent *already knows* from the outset (in her prior $P$) that she is Player 1 (and her twin is Player 2), and the asymmetric observation is simply an irrelevant piece of local background noise—for instance, Player 1 observes the local room temperature $x_1 = 20^\circ\text{C}$ and Player 2 observes $x_2 = 21^\circ\text{C}$, where Player 1 only cares about Player 1's utility $\textsc{V}_1$?

Let us calculate *that* case—where Twin 1 optimizes Twin 1's utility $\textsc{V}_1$, Twin 2 optimizes Twin 2's utility $\textsc{V}_2$, both use the same decision algorithm, and they receive distinct local observations $x_1 \neq x_2$ (for example, Twin 1 sees a green light $x_1 = \textit{green}$ and Twin 2 sees a yellow light $x_2 = \textit{yellow}$, or each twin observes their own distinct spatial coordinates):

In Action-FDT, Twin 1 observes $x_1$ and intervenes on $\textsc{fdt}(\underline{P}, \underline{G}, x_1) = a$. Because Twin 2 observed $x_2 \neq x_1$, Twin 2's action $\textsc{Act}_2$ is governed by $\textsc{fdt}(\underline{P}, \underline{G}, x_2)$. Consequently, in Twin 1's graph $G$, $\textsc{Act}_2$ is *not* downstream of $\textsc{fdt}(\underline{P}, \underline{G}, x_1)$! For any prior probability $q = P(\textsc{Act}_2 = \textit{C})$:
$$\mathbb{E}\left(\textsc{V}_1 \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline{P}, \underline{G}, x_1) = \textit{C}\big)\right) = \$1,000,000q,$$
$$\mathbb{E}\left(\textsc{V}_1 \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline{P}, \underline{G}, x_1) = \textit{D}\big)\right) = \$1,000,000q + \$1,000.$$
Thus, $\mathrm{FDT}_{\text{act}}(P, G, x_1) = \textit{D}$, and symmetrically $\mathrm{FDT}_{\text{act}}(P, G, x_2) = \textit{D}$. Whenever two Action-FDT twins receive distinct sensory inputs $x_1 \neq x_2$, Action-FDT severs the subjunctive link between them and collapses into CDT's mutual defection, earning $\$1,000$ instead of $\$1,000,000$!

### 4.3 How P-FDT Achieves Multi-Agent Cooperation Across Asymmetric Observations

Now let us apply **P-FDT** to the exact same scenario. Even when Twin 1 and Twin 2 have distinct local observations $x_1$ and $x_2$ (or when an agent is uncertain which observation $x \in \{x_1, x_2\}$ she and her twin will receive under an asymmetric division of labor), both twins share the same prior decision model $(P, G)$ and therefore compute the same policy node $\textsc{pfdt}(\underline{P}, \underline{G})$.

Specifically, suppose two identical P-FDT agents are randomly assigned to Role 1 (observing $x_1$) and Role 2 (observing $x_2$) with equal probability $1/2$, or suppose they face an **Asymmetric Division-of-Labor Game**:
* Twin A observes $x_1 = \textit{Lock\_Left}$ and Twin B observes $x_2 = \textit{Lock\_Right}$.
* To open a vault worth $\$1,000,000$ to each of them, the twin seeing $\textit{Lock\_Left}$ must turn her key *Left* ($\textit{L}$) at a personal effort cost of $\$1,000$, and the twin seeing $\textit{Lock\_Right}$ must turn her key *Right* ($\textit{R}$) at a personal effort cost of $\$1,000$, while doing *Nothing* ($\textit{N}$) costs $\$0$.

Under **P-FDT**, the policy space is $\Pi = \{\textit{L}, \textit{R}, \textit{N}\}^{\{\textit{Lock\_Left}, \textit{Lock\_Right}\}}$, containing $3^2 = 9$ policies $\pi = (\pi(\textit{Lock\_Left}), \pi(\textit{Lock\_Right}))$. In the P-FDT graph $G$:
* The single node $\textsc{pfdt}(\underline{P}, \underline{G})$ outputs $\pi \in \Pi$.
* The twin who observes $\textit{Lock\_Left}$ executes $\textsc{Act}_{\text{Left}} = \pi(\textit{Lock\_Left})$.
* The twin who observes $\textit{Lock\_Right}$ executes $\textsc{Act}_{\text{Right}} = \pi(\textit{Lock\_Right})$.

When either twin runs Equation (P-FDT.1), she intervenes on $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$, which simultaneously sets *both* $\textsc{Act}_{\text{Left}} = \pi(\textit{Lock\_Left})$ and $\textsc{Act}_{\text{Right}} = \pi(\textit{Lock\_Right})$:
* For $\pi^* = (\textit{L}, \textit{R})$, the vault opens and each twin incurs the $\$1,000$ effort cost, yielding $\mathcal{EU}_{\text{P-FDT}}(\pi^*) = \$1,000,000 - \$1,000 = \$999,000$.
* For $\pi_0 = (\textit{N}, \textit{N})$, the vault stays closed and neither twin expends effort, yielding $\mathcal{EU}_{\text{P-FDT}}(\pi_0) = \$0$.
* For any asymmetric shirking policy such as $(\textit{N}, \textit{R})$ or $(\textit{L}, \textit{N})$, the vault still stays closed and one twin wastes $\$1,000$, yielding $-\$500$ in expectation.

Therefore, Equation (P-FDT.1) uniquely selects the complementary policy $\pi^* = (\textit{L}, \textit{R})$. In Stage 2 (Equation P-FDT.2):
* The twin who observes $\textit{Lock\_Left}$ computes $\mathrm{PFDT}(P, G, \textit{Lock\_Left}) = \pi^*(\textit{Lock\_Left}) = \textit{L}$.
* The twin who observes $\textit{Lock\_Right}$ computes $\mathrm{PFDT}(P, G, \textit{Lock\_Right}) = \pi^*(\textit{Lock\_Right}) = \textit{R}$.

Both twins seamlessly coordinate on complementary actions despite receiving different observations and having no causal communication channel.

### 4.4 Beyond the Source: A Single-Agent Dilemma Where P-FDT Also Diverges from Action-FDT

In Footnote 16, Yudkowsky and Soares write that *"The difference only matters in multi-agent dilemmas so far as we can tell."* While that holds for all the single-agent dilemmas studied in their paper (where the predictor only cares about the agent's action at a single observation node, such as $\textit{full}$ in Transparent Newcomb or $\textit{blackmail}$ in Mechanical Blackmail), our mathematical analysis reveals a class of *single-agent* dilemmas where P-FDT also outperforms Action-FDT. (We note explicitly that this observation goes beyond the claims in the source text.)

Consider a **Holistic Predictor Dilemma**:
* A predictor flips a fair coin to show the agent either a **Green Box** ($x = \textit{G}$) or a **Blue Box** ($x = \textit{B}$), each containing a free $\$1,000$ that the agent can either *Take* ($\textit{T}$) or *Leave* ($\textit{L}$).
* The predictor wire-transfers $\$1,000,000$ to the agent's bank account if and only if she predicts that the agent's contingent plan is to *Leave* the $\$1,000$ when shown the Green Box **and** *Leave* the $\$1,000$ when shown the Blue Box—that is, $\pi(\textit{G}) = \textit{L}$ and $\pi(\textit{B}) = \textit{L}$.

Why does Action-FDT fail here? Suppose the coin lands Green, so the agent observes $x = \textit{G}$. An Action-FDT agent intervenes *only* on $\textsc{fdt}(\underline{P}, \underline{G}, \textit{G})$ while treating $\textsc{fdt}(\underline{P}, \underline{G}, \textit{B})$ as a fixed random variable with prior probability $q = P(\textsc{fdt}(\underline{P}, \underline{G}, \textit{B}) = \textit{L})$. If the Action-FDT agent happens to have low confidence $q < 0.001$ in what she would have done had she seen Blue, she will conclude that leaving the Green Box only has a $<0.1\%$ chance of triggering the $\$1,000,000$ payout, and will therefore *Take* the $\$1,000$! Worse, if both $\textsc{fdt}(\underline{P}, \underline{G}, \textit{G})$ and $\textsc{fdt}(\underline{P}, \underline{G}, \textit{B})$ expect each other to *Take*, Action-FDT gets trapped in a bad Nash equilibrium between its own observation branches: neither branch sacrifices $\$1,000$ because each branch treats the other branch's action as fixed at $\textit{T}$!

**P-FDT** completely avoids this intra-agent coordination failure. Because P-FDT intervenes on the entire policy $\pi = (\pi(\textit{G}), \pi(\textit{B})) \in \{\textit{T}, \textit{L}\}^2$ simultaneously:
* $\mathcal{EU}_{\text{P-FDT}}(\textit{L}, \textit{L}) = \$1,000,000$,
* $\mathcal{EU}_{\text{P-FDT}}(\textit{T}, \textit{T}) = \$1,000$,
* $\mathcal{EU}_{\text{P-FDT}}(\textit{L}, \textit{T}) = \mathcal{EU}_{\text{P-FDT}}(\textit{T}, \textit{L}) = \$500$.

Thus P-FDT immediately selects $\pi^* = (\textit{L}, \textit{L})$ without any dependence on off-path priors $q$ or intra-branch equilibrium traps.

---

## 5. Step-by-Step Procedure and Operational Resolutions of Open Questions

### 5.1 A General 5-Step Procedure for Applying P-FDT

To apply P-FDT to any unfamiliar decision problem, a researcher or automated reasoner can execute the following five-step procedure:

1. **Specify the Decision Spaces**: Identify the finite action space $\mathcal{A}$, the set of possible local observations $\mathcal{X}$, the outcome space $\mathcal{O}$, the utility function $\mathcal{U} : \mathcal{O} \to \mathbb{R}$ (with $\textsc{V} = \mathcal{U}(\textsc{Outcome})$), and the policy space $\Pi = \mathcal{A}^{\mathcal{X}}$.
2. **Construct the Subjunctive Graph $G$ and Prior $P$**: Introduce a single logical policy node $\textsc{pfdt}(\underline{P}, \underline{G})$ with state space $\Pi$. Draw directed edges from $\textsc{pfdt}(\underline{P}, \underline{G})$ to:
   * The agent's action node $\textsc{Act}$, governed by $\textsc{Act}(\pi, \textsc{Obs}) = \pi(\textsc{Obs})$;
   * Any predictor's prediction node that simulates or models the agent's decision procedure;
   * Any twin or symmetric agent's action node $\textsc{Act}_k = \pi(\textsc{Obs}_k)$ that implements the same decision procedure.
   Do *not* draw edges from $\textsc{pfdt}(\underline{P}, \underline{G})$ to purely statistical common causes (such as the arterial lesion in the Smoking Lesion problem or the termite infestation in the XOR Blackmail problem).
3. **Evaluate Candidate Policies via $\mathtt{do}$-Intervention**: For each policy $\pi \in \Pi$, compute the interventional distribution $P(\cdot \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi))$ by fixing the policy node to $\pi$ and propagating probabilities forward through $G$, *without* conditioning on the actual observation $x$.
4. **Select the Optimal Policy $\pi^*$**: Compute $\mathcal{EU}_{\text{P-FDT}}(\pi)$ via Equation (P-FDT.3) for each $\pi \in \Pi$, and select $\pi^* \in \argmax_{\pi \in \Pi} \mathcal{EU}_{\text{P-FDT}}(\pi)$.
5. **Apply $\pi^*$ to the Actual Observation**: Plug the agent's actual observation $x \in \mathcal{X}$ into $\pi^*$ to output the physical action $a^* = \pi^*(x)$.

### 5.2 Open Questions in the Source and Operational Proposals

Because Yudkowsky and Soares mention P-FDT only briefly in Footnotes 7 and 16, several crucial mathematical questions remain unresolved in the source text. Here we distinguish those open questions and propose concrete operational interpretations.

#### Open Question 1: What is the exact domain of a policy $\pi$ ("observations" vs. "inputs")?
In Footnote 7, the authors define policies as *"mappings from observations to actions"* ($\pi : \mathcal{X} \to \mathcal{A}$). In Footnote 16, they write that a policy *"maps inputs to actions, to which the agent then applies her inputs in order to select an action."* In Equation 4 of the paper, the inputs to the FDT algorithm are the full triple $(P, G, x)$—the world-model together with the observation.

If a policy mapped *all possible world-models and observations* $(\mathcal{P} \times \mathcal{G} \times \mathcal{X}) \to \mathcal{A}$, the policy space $\Pi$ would be uncountably infinite and computationally intractable. However, why might an agent ever want the domain of $\pi$ to be broader than $\mathcal{X}$? Consider the **Smoking Lesion Problem** (Section 6 of the paper), where the agent does not know whether her utility function is $\mathcal{U}_S$ (loves smoking, incorporated into $P_S$) or $\mathcal{U}_R$ (hates smoking, incorporated into $P_R$). Or consider a multi-agent dilemma where two agents share the same P-FDT algorithm, but have slightly different prior beliefs or utility functions.

**Operational Proposal**: In any problem where the agent's prior beliefs and utility function are known and shared with her subjunctive counterparts, the domain of $\pi$ should be taken simply as the observation history space $\mathcal{X}$, so $\Pi = \mathcal{A}^{\mathcal{X}}$. When an agent faces indexical or preference uncertainty across a finite family of possible internal epistemic states $\Theta$ (such as $\theta \in \{S, R\}$ in the Smoking Lesion problem, or role/type parameters in a Bayesian game), we can unify Footnotes 7 and 16 by defining the "input" space as $\mathcal{I} \coloneqq \Theta \times \mathcal{X}$, so that a policy $\pi : \Theta \times \mathcal{X} \to \mathcal{A}$ maps the agent's local type-and-observation pair $(\theta, x)$ to an action.

#### Open Question 2: How does P-FDT resolve ties on zero-probability observation branches?
Consider the **Mechanical Blackmail Problem** (Dilemma 8 in Section 9 of the paper) with an *infallible* blackmailer ($100\%$ accuracy). The observation space is $\mathcal{X} = \{\textit{blackmail}, \emptyset\}$ and the action space upon receiving the blackmail is $\mathcal{A} = \{\textit{pay}, \textit{refuse}\}$ (while at $\emptyset$ the only action is $\textit{nothing}$). Look at what happens when the predictor is $100\%$ accurate:
* Under $\pi_{\text{pay}} = (\textit{pay}, \textit{nothing})$, the blackmailer predicts $\textit{pay}$ and sends the blackmail ($P(\textsc{Obs} = \textit{blackmail} \mid \mathtt{do}(\pi_{\text{pay}})) = 1$), so the agent loses $\$1,000$.
* Under $\pi_{\text{refuse}} = (\textit{refuse}, \textit{nothing})$, the blackmailer predicts $\textit{refuse}$ and *never sends the blackmail* ($P(\textsc{Obs} = \textit{blackmail} \mid \mathtt{do}(\pi_{\text{refuse}})) = 0$), so the agent loses $\$0$.

Thus $\pi^* = \pi_{\text{refuse}}$ is uniquely optimal *even if* the observation $\textsc{Obs} = \textit{blackmail}$ has probability $0$ under $\pi_{\text{refuse}}$, because changing $\pi(\textit{blackmail})$ from $\textit{refuse}$ to $\textit{pay}$ changes the probability of $\textsc{Obs} = \textit{blackmail}$ from $0$ to $1$!

However, what if there is an observation $x_0 \in \mathcal{X}$ that has probability $0$ under *every* policy (or what if two policies $\pi_1, \pi_2$ yield identical global expected utility because $\pi_1(x_0)$ and $\pi_2(x_0)$ neither change $P(\textsc{Obs} = x_0)$ nor occur with positive probability)? Then $\argmax_{\pi \in \Pi} \mathcal{EU}_{\text{P-FDT}}(\pi)$ is not a singleton, and if the agent unexpectedly observes $x_0$, $\pi^*(x_0)$ is underdetermined.

**Operational Proposal**: We propose two complementary operational refinements for P-FDT:
1. **$\epsilon$-Full-Support Perturbation (Trembling-Hand Priors)**: Following Yudkowsky and Soares's modeling choice in the Transparent Newcomb and Mechanical Blackmail dilemmas (where predictors have accuracy $1 - \epsilon$ with $\epsilon = 0.01$ or $0.0009$), the prior $P$ should assign strictly positive "cosmic-ray" or "trembling-hand" probability $\epsilon > 0$ to every observation $x \in \mathcal{X}$. When $P(\textsc{Obs} = x \mid \mathtt{do}(\pi)) > 0$ for all $x$ and $\pi$, every branch $x \in \mathcal{X}$ contributes non-trivially to Equation (P-FDT.3), eliminating off-path indifference.
2. **Canonical Lexicographic Tie-Breaking**: In multi-agent coordination games with exact symmetry (e.g., two twins playing Pure Coordination where $(\textit{Left}, \textit{Left})$ and $(\textit{Right}, \textit{Right})$ both yield $\$1,000,000$), $\argmax_{\pi \in \Pi}$ returns a set of tied policies. For $\mathrm{PFDT}_{\text{policy}}(P, G)$ to be a well-defined mathematical function on which twins can coordinate without communication, the $\argmax$ operator must be equipped with a fixed canonical ordering $\prec$ over $\Pi$ (such as lexicographic order under a canonical binary encoding of $\mathcal{X}$ and $\mathcal{A}$) and select the $\prec$-first policy in the maximal set.

#### Open Question 3: Computational Complexity and Inferring the Subjunctive Graph $G$
As Yudkowsky and Soares acknowledge in Sections 5 and 6, solving the exact optimization in Equation (4) is computationally intractable in real-world environments, and deducing the structure of the subjunctive graph $G$ from observation and experiment remains *"perhaps the largest open problem in the study of functional decision theory."*

In P-FDT, the computational challenge is magnified: because $|\Pi| = |\mathcal{A}|^{|\mathcal{X}|}$, iterating naively over all policies in $\Pi$ scales exponentially in the number of possible observation histories $|\mathcal{X}|$. In practical AI or human decision-making, an operational P-FDT agent must restrict optimization to a parameterized or pruned policy class $\Pi_{\text{tractable}} \subset \mathcal{A}^{\mathcal{X}}$ (such as policies computable by circuits or neural networks of bounded size) and evaluate only the Equivalence Classes of observations that are decision-relevantly linked in $G$.

---

## 6. Conclusion

**Policy Functional Decision Theory (P-FDT)** completes the conceptual shift initiated by functional decision theory. By intervening on the logical node $\textsc{pfdt}(\underline{P}, \underline{G})$ to select an entire *policy* $\pi : \mathcal{X} \to \mathcal{A}$ before applying that policy to the observed input $x$, P-FDT unifies precommitment, updatelessness, and subjunctive reasoning into a single two-stage equation. It retains all the single-agent advantages of Action-FDT—one-boxing in Newcomb's and Transparent Newcomb's problems, smoking in the Smoking Lesion problem, staying put in Death in Damascus, and resisting extortion in XOR and Mechanical Blackmail—while eliminating ungrounded off-path priors and enabling symmetric agents to coordinate across asymmetric observations in multi-agent dilemmas.

## References

* Dai, W. (2009). Towards a new decision theory. *LessWrong*.
* Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Gibbard, A., & Harper, W. L. (1978). Counterfactuals and two kinds of expected utility. In *Foundations and Applications of Decision Theory* (pp. 125–162). D. Reidel.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Kleene, S. C. (1938). On notation for ordinal numbers. *Journal of Symbolic Logic*, 3(4), 150–155.
* Lewis, D. (1979). Prisoners' dilemma is a Newcomb problem. *Philosophy & Public Affairs*, 8(3), 235–240.
* Nozick, R. (1969). Newcomb's problem and two principles of choice. In *Essays in Honor of Carl G. Hempel* (pp. 114–146). D. Reidel.
* Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
* Pearl, J. (1996). Causation, action, and counterfactuals. In *Proceedings of the 6th Conference on Theoretical Aspects of Rationality and Knowledge* (pp. 51–73).
* Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Peirce, C. S. (1934). *Collected Papers of Charles Sanders Peirce, Vol. V: Pragmatism and Pragmaticism*. Harvard University Press.
* Skyrms, B. (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Soares, N., & Fallenstein, B. (2015). Toward idealized decision theory. *arXiv preprint arXiv:1507.01986*.
* Yudkowsky, E. (2010). *Timeless Decision Theory*. The Singularity Institute.
* Yudkowsky, E., & Soares, N. (2017). Functional decision theory: A new theory of instrumental rationality. *arXiv preprint arXiv:1710.05060v2*.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Purpose**

I'm currently focused on defining the precise parameters of this project. The goal is clear: a mathematical essay or technical blog post covering P-FDT and its application. I'm prioritizing clarity and accessibility for the intended audience, and ensuring the explanation is mathematically sound.


**Clarifying the Core Concept**

I've been drilling down into the core of P-FDT, using the provided paper as a foundation. My focus has narrowed to the policy-selection passage in footnote 16 and its connection to footnote 7, aiming for a precise understanding for a mathematically literate audience. The target word count is around 2,400 to 3,000 words, aiming for both technical clarity and philosophical context.


**Refining the Terminology**

I'm now zeroing in on the nuanced terminology. I'm prioritizing consistent use of "P-FDT" and distinguishing it from other theories. I'm focusing on crafting a coherent account of the theory with mathematical definitions, examples, and explanations. The essay will ensure mathematical precision and offer clarity on how P-FDT evaluates actions, dependencies, and counterfactuals, with sufficient detail for readers to use it to decide unfamiliar cases.


**Interpreting the Uncertainties**

I'm wrestling with an open and crucial question: how to operationalize the uncertainties inherent in P-FDT. I'm carefully distinguishing the claims made by the source material from my own interpretations and any additional assumptions I might bring to the table. Quotes remain verbatim. I plan to end with a concise conclusion, and eschew lengthy bibliographies or appendices. The word count range is still around 2,400–3,000 words.


**Analyzing the Core Equation**

I'm now deeply engaged with the core mathematical expression, specifically its implications for policy selection. I'm focusing on the intervention on the logical node and how it contrasts with intervening on a physical act. This involves understanding subjunctive dependence via the extended graph and the $\mathtt{do}$ operator, which represents a counterpossible. I am also working to grasp the updatelessness of observations. I'm aiming to capture this in a rigorous way for a mathematically sophisticated audience.


**Examining the Formalism**

I'm now zeroing in on the formal aspects, particularly how P-FDT handles observations and policies. I'm unpacking the distinction between intervening on an action versus a policy, which is more relevant in multi-agent systems. The latest focus is the differing nodes for observations and the role of the prior probability ($q$) of $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty})$. I'm aiming for mathematical precision and clarity on these points.


**Formalizing the Policies**

I'm now formalizing the concept of policies within the P-FDT framework. I'm focusing on defining observations ($\mathcal{X}$), actions ($\mathcal{A}$), and the policy space ($\Pi$). The key distinction I am grappling with is how inputs are processed to select actions, particularly in single-agent vs. multi-agent scenarios, and where those scenarios are most important. I'm noting the node in the graph $G$ is not indexed by observation $\underline{x}$. Instead, the node represents the policy that is output by the algorithm.


**Clarifying the Policy Definition**

I'm now clarifying the policy's function within P-FDT. Is it $\mathcal{X} \to \mathcal{A}$ or $(P, G, x) \to a$? In a fixed decision problem, my local input is the observation history, $x \in \mathcal{X}$. I am defining this precisely, referencing the two-stage procedure in Footnote 16: policy selection and action execution, providing the formulas for both.


**Defining Policy Inputs**

I'm now wrestling with the precise inputs a policy requires within the P-FDT framework, particularly the distinction between the mappings from observations to actions as a simpler, computationally feasible approach, versus considering all possible world-models as a vastly larger set. I'm clarifying how the graphical structure $G$ changes between Action-FDT and P-FDT.


**Distinguishing Node Interventions**

I'm now clarifying the distinctions in graphical interventions, particularly the implications of intervening on logical nodes. The focus is on how $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full})$ and $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty})$ behave as independent variables when one is intervened upon, contrasting this with P-FDT's single policy node and its implications for predictor-agent dependencies. I'm also exploring the "only matters in multi-agent dilemmas" statement.


**Interpreting Agent Planning**

I'm now considering the implications of an agent's prior uncertainty ($q$) about their own off-path behavior, particularly in scenarios where *q* flips the optimal action. I'm focusing on how P-FDT might resolve this through simultaneous optimization over a tuple representing the agent's entire contingent plan, rather than relying on an arbitrary prior. I'm also examining the relevance of this in multi-agent dilemmas with asymmetric observations.


**Analyzing Twin Scenarios**

I'm now analyzing twin scenarios, focusing on Action-FDT's degeneration to CDT-like behavior when observations differ, where interventions on one twin's observation do not affect the other. P-FDT, however, shares a single policy node, leading to the execution of policy inputs on both twins. This leads to non-independent nodes and distinct results.


**Elaborating on Policy Interdependence**

I've just had a breakthrough: the simultaneous variation of policy outputs on different observations in the twin scenarios is key! It's a mathematically rigorous explanation for why policy selection matters in multi-agent dilemmas, as described in footnotes. My next step involves addressing tie-breaking, stochastic policies, and sequential observations.


**Structuring the Content**

I'm now outlining the essay's structure to ensure depth and clarity within the word count. I'm starting with an introduction that covers EDT, CDT, and FDT, and introducing policy function focus. The goal is to set the stage, and then introduce Action-FDT, contrasted by P-FDT in footnote 16. I'll outline the twin scenarios, tie-breaking, and sequential observations to explore P-FDT's implications in multi-agent dilemmas.


**Formalizing the Architecture**

I'm now diving into the formal architecture, starting with mathematical primitives: $\mathcal{O}$, $\mathcal{U}$, $V$, $\mathcal{A}$, $\mathcal{X}$, and $M = (P, G)$. I'll contrast EDT, CDT, and Action-FDT. Then, I plan to formally present P-FDT, defining the policy space $\Pi$ and detailing the two-step procedure in Footnote 16, starting with the policy node intervention.


**Elaborating the Equation**

I'm now zeroing in on the core of the P-FDT formalism, specifically the equation and its implications. I'm focusing on the distinction between the policy evaluation in $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$ and local evaluation for the current observation $x \in \mathcal{X}$, and the function $\mathrm{PFDT}(P, G, x) \coloneqq \pi^*(x)$. I'm also planning an elaboration on the construction of the graphical model $G$.


**Illustrating the Problem**

I'm now crafting examples to illustrate P-FDT. I plan to use the Transparent Newcomb Problem and the Asymmetric Twin Prisoner's Dilemma. The Newcomb problem will highlight the elimination of the nuisance parameter $q$, while the dilemma will show policy importance in multi-agent scenarios. The explicit expected utility calculations are next.



**Demonstrating Scenario Failures**

I'm working on explaining Action-FDT's failure in the Twin Prisoner's Dilemma. I will show how P-FDT's single policy node enables cooperation, contrasting the step-by-step logic. I'm focusing on the effect of distinct observations, interventions on the $\textsc{fdt}$ function, and the distinction between single and multi-agent systems, with the formalization following the example.


**Interpreting P-FDT Scope**

I'm now focusing on clarifying the unresolved questions regarding P-FDT's scope, including the nature of policy inputs and tie-breaking for zero-probability observations, as mentioned in footnotes 7 and 16. I'm distinguishing between the observation space ($\mathcal{X}$) as local observation histories, or as parameters of some larger, higher-level model, and the issues of edge cases.


**Operationalizing the Policies**

I'm now operationalizing the policies, specifically addressing the tie-breaking question. I'm exploring the "trembling-hand" operationalization or lexicographic tie-breaking for zero-probability observations. I'm also planning to discuss computational intractability and bounded approximations for the policy space, including how subjunctive graphs can be inferred. The last step is to wrap up with a conclusion.


**Illustrating the Examples**

I'm now fully immersed in the examples, starting with explicit expected utility calculations for Transparent Newcomb. I'm focusing on why, in this case, P-FDT aligns with one-boxing, due to the single-policy node and the elimination of $q$, and why Action-FDT may two-box. I'm planning to work on the Twin Prisoner's Dilemma next.


**Managing the Word Count**

I'm now laser-focused on tone and style, ensuring a rigorous yet engaging mathematical flow. I'm carefully tracking the word count to stay within the target range, with a precise calculation for the Transparent Newcomb problem. I'm also ensuring the correct mathematical calculation for two-boxing is exact, to eliminate potential confusion. I'm ensuring consistent terminology, and distinct clarity of core concepts.


**Operationalizing the Process**

I'm now devising a clear 5-step operational procedure to apply P-FDT to any decision problem, emphasizing practicality. These steps include defining decision spaces, constructing the subjunctive world-model, determining the prior, computing expected utilities, and selecting the optimal action. I'm focusing on the clarity and completeness of each step for direct application.


**Defining the Equation**

I'm now clarifying the formal equation for Action Selection. I will provide a step-by-step description of how to operationalize the equation, breaking down each step to describe the evaluation mechanism $\textsc{Act} = \mathrm{Eval}(\Pi_{\text{node}}, \textsc{Obs}) = \Pi_{\text{node}}(\textsc{Obs})$. I'm going to carefully explain how to intervene on other agents' action nodes or predictors' prediction nodes.



```
