# 021_fdt_eq4_google_gemini-4-argon_rhigh_phigh / 00008

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/b325f4d2-3c4f-4180-82fd-4b1e56467769/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/b325f4d2-3c4f-4180-82fd-4b1e56467769/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Action Functional Decision Theory (A-FDT): Formal Mechanics, Subjunctive Counterfactuals, and Operational Application

## 1. Introduction and Philosophical Motivation

For decades, normative decision theory has been divided between two foundational paradigms: **evidential decision theory (EDT)** and **causal decision theory (CDT)**. When an agent deliberates among a finite set of available actions $\mathcal{A}$, both theories agree that rational choice consists in maximizing expected utility, yet they disagree over how to construct the hypothetical probability distribution associated with choosing an action $a \in \mathcal{A}$. 

An EDT agent asks which action would provide the strongest statistical evidence of a desirable outcome—asking, in effect, *"Which physical act of mine would be the best news to hear I took?"* A CDT agent, by contrast, isolates the causal consequences of the physical act token itself, holding fixed everything causally upstream of the action—asking, *"Which physical act of mine causes the best outcome?"*

Measured by expected utility achieved across standard decision-theoretic dilemmas, neither theory is uniformly satisfactory. In Newcomb's problem (Nozick, 1969) or the Psychological Twin Prisoner's Dilemma (Lewis, 1979), an environment contains an accurate predictor or symmetric reasoner whose behavior correlates with the agent's choice. Here, EDT prescribes one-boxing (or cooperating) and walks away rich, whereas CDT severs the correlation between the agent's choice and the predictor's prior state, prescribes two-boxing (or defecting), and walks away poor. Conversely, in medical or statistical confounding dilemmas such as the Smoking Lesion problem (Skyrms, 1980) or the XOR Blackmail problem (Soares & Fallenstein, 2015), an unobservable state of the world correlates with both the agent's action and a catastrophic outcome without being causally or logically downstream of the agent's deliberation. Here, EDT irrationally attempts to "manage the news" (Lewis, 1981)—refraining from smoking or paying a blackmailer to buy auspicious statistical evidence—while CDT rightly ignores the spurious correlation. Still more troublingly, in sequential prediction dilemmas such as Parfit's Hitchhiker (Parfit, 1986), the Transparent Newcomb problem (Drescher, 2006), and Mechanical Blackmail, *both* EDT and CDT fail to secure the high-utility outcome once the agent observes the predictor's move.

In *"Functional Decision Theory: A New Theory of Instrumental Rationality"*, Eliezer Yudkowsky and Nate Soares propose a unified resolution to these dilemmas. Their core insight is that an agent should not treat a decision merely as an isolated physical event token, but as the output of a fixed mathematical decision function. As they summarize the principle in their abstract, a rational decision-maker should treat her choice as the output of a function that answers the question: *"Which output of this very function would yield the best outcome?"*

While Yudkowsky and Soares note in passing (Footnotes 7 and 16) that a fully general version of their framework can evaluate entire *policies* (mappings from observations to actions), the formal decision rule they present and apply throughout their paper—given in **Equation (4), Section 5**—intervenes directly on the *action* output of the decision function for the agent's current inputs. In this essay, we refer to this formal system as **action functional decision theory (A-FDT)**. Below, we develop a rigorous mathematical account of **A-FDT**, explain how it represents subjunctive dependencies and observation histories, trace its calculations across classic dilemmas, and establish an operational procedure for applying **A-FDT** to unfamiliar decision problems.

---

## 2. The Formal Architecture of A-FDT

### 2.1 Expected Utility and Epistemic Perspectives

Following Gibbard and Harper (1978) and Joyce (1999), EDT, CDT, and **A-FDT** can all be expressed within a common expected-utility framework. Let $\mathcal{A}$ be a finite set of available actions, $\mathcal{O} = \{o_1, o_2, \dots\}$ be a countable set of outcomes, $\mathcal{X}$ be a countable set of possible observation histories, and $\mathcal{U} : \mathcal{O} \to \mathbb{R}$ be a bounded utility function. An agent who has received observation history $x \in \mathcal{X}$ seeks to choose an action $a \in \mathcal{A}$ that maximizes expected utility, defined in Equation (1) of the reference paper as:

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j) \tag{1}$$

Here, $P(a \hookrightarrow o_j ;\, x)$ denotes the probability assigned to outcome $o_j$ in the decision-theoretic hypothetical where action $a$ is taken upon observing $x$. As Joyce (1999) observes, *"decision theories should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated."*

Computationally, an agent maintains an internal world-model $M$ and, for each candidate action $a \in \mathcal{A}$, performs a surgical modification on $M$ to construct a transient hypothetical representation $M^{a\hookrightarrow}$ of what the world would look like if $a$ were chosen. Defining the random variable $\textsc{V} \coloneqq \mathcal{U}(\textsc{Outcome})$ and writing $\mathbb{E}$ for expectation under the probability measure $P$, the competing theories are distinguished by how they define $M$ and construct $M^{a\hookrightarrow}$:

1. **Evidential Decision Theory (EDT)**: The world-model $M$ is simply a probability distribution $P$ over variables including $\textsc{Obs}$ (observation history), $\textsc{Act}$ (physical action), and $\textsc{V}$ (utility). Hypotheticals are formed by standard Bayesian conditioning (Equation 2):
   $$\mathrm{EDT}(P, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs}=x, \textsc{Act}=a\right) \tag{2}$$
   where actions $a$ with $P(\textsc{Act}=a \mid \textsc{Obs}=x) = 0$ are excluded from consideration.

2. **Causal Decision Theory (CDT)**: Following Pearl (1996, 2000), the world-model $M$ is a causal model $(P, G)$, where $G$ is a directed acyclic graph (DAG) encoding causal relationships among the variables of $P$. Hypotheticals are formed by applying Pearl's $\mathtt{do}(\cdot)$ operator to sever all incoming causal arrows into the physical action node $\textsc{Act}$, setting $\textsc{Act}=a$, and conditioning on the observation $\textsc{Obs}=x$ (Equation 3):
   $$\mathrm{CDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x\right) \tag{3}$$

### 2.2 The Primary Formal Presentation of A-FDT (Equation 4)

Where CDT intervenes on a node representing a *physical* event ($\textsc{Act}=a$), **A-FDT** intervenes on a node representing a *logical* or *computational* fact: the output of the **A-FDT** algorithm itself when evaluated on the agent's current model and observation history.

Ideally, one might wish to define a logical conditioning operator $\mathtt{true}(\phi)$ that updates a probability distribution $P$ on the counterpossible assumption that a mathematical sentence $\phi$ holds, yielding:

$$\mathrm{AFDT}^*(P, x) = \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{true}\left(\textsc{afdt}(\underline{P}, \underline{x}) = a\right)\right)$$

Because no general formalization of $\mathtt{true}(\phi)$ currently exists for counterpossible conditionals, Yudkowsky and Soares augment the probability distribution $P$ with a directed graph $G$ that encodes not only physical causation, but also logical, mathematical, and computational dependencies—collectively termed *subjunctive dependencies*. Using Pearl's $\mathtt{do}(\cdot)$ operator on this augmented graph $G$ yields **Equation (4)** of Section 5, our primary formal definition of **A-FDT**:

$$\mathrm{AFDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{afdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right) \tag{4}$$

*(Note on terminology: In Equation (4) of the source text, the function and node are written $\mathrm{FDT}$ and $\textsc{fdt}$; we write $\mathrm{AFDT}$ and $\textsc{afdt}$ to identify **A-FDT** specifically and distinguish it from policy-level variants.)*

Every symbol in Equation (4) carries precise operational meaning:
* **$(P, G)$ as a Subjunctive Graphical Model**: $P$ is a subjective probability distribution over a set of random variables $\mathcal{V}$ that includes both physical states (such as $\textsc{Act}$, $\textsc{Obs}$, $\textsc{Outcome}$) and logical variables representing the outputs of mathematical functions (such as a node for $6288 + 1048$, or nodes for decision functions run on various inputs). $G$ is a DAG over $\mathcal{V}$ whose directed edges $Y \to Z$ specify how surgical changes to a parent node $Y$ propagate to child node $Z$.
* **Quoting/Dequoting ($\underline{P}, \underline{G}, \underline{x}$) and Self-Reference**: The underline notation denotes syntactic substitution (dequoting): if $x$ takes the value $3$, then $\textsc{Z}\underline{x}$ names the variable $\textsc{Z}3$. Thus, when the agent runs $\mathrm{AFDT}$ on inputs $(P, G, x)$, the algorithm singles out the specific variable $\textsc{afdt}(\underline{P}, \underline{G}, \underline{x})$ inside $G$ that represents the output of $\mathrm{AFDT}(P, G, x)$. By Kleene's (1938) second recursion theorem (via "quining"), a computational structure can contain an exact syntactic representation of itself without circularity or infinite regress. Furthermore, the agent does not need to know the *actual* output of $\mathrm{AFDT}(P, G, x)$ in advance; she simply iterates over $a \in \mathcal{A}$, uses $\mathtt{do}(\textsc{afdt}(\underline{P}, \underline{G}, \underline{x}) = a)$ to set that node's value to $a$ in each hypothetical $M^{a\hookrightarrow}$, propagates the change along the arrows of $G$, and selects the $a$ that maximizes expected utility $\mathbb{E}(\textsc{V})$.

### 2.3 Two Structural Departures from CDT

Comparing Equation (3) for CDT with Equation (4) for **A-FDT** reveals two fundamental mathematical differences:

1. **Type vs. Token Intervention**: In Peirce's (1934) terminology, CDT intervenes on the physical action *token* $\textsc{Act}$, severing $\textsc{Act}$ from the agent's own decision algorithm. **A-FDT** intervenes on the computational *type* $\textsc{afdt}(\underline{P}, \underline{G}, \underline{x})$. Consequently, any environmental process $Z$ that computes, simulates, or predicts the output of $\mathrm{AFDT}(P, G, x)$ is a descendant of $\textsc{afdt}(\underline{P}, \underline{G}, \underline{x})$ in $G$ and covaries with $a$ under the $\mathtt{do}\left(\textsc{afdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)$ intervention.
2. **Updateless Response to Observations**: Look closely at the right-hand side of Equation (4): unlike EDT in Equation (2) and CDT in Equation (3), **A-FDT** does *not* condition the probability distribution $P$ on $\textsc{Obs} = x$. As the authors emphasize directly beneath Equation (4): *"Second, where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon."* When an **A-FDT** agent's observation history changes from $x$ to $y$, she does not restrict her evaluation to worlds where $\textsc{Obs} = y$; instead, she switches the target of her intervention from $\textsc{afdt}(\underline{P}, \underline{G}, \underline{x})$ to $\textsc{afdt}(\underline{P}, \underline{G}, \underline{y})$ while evaluating expectation over the *prior* distribution $P$. (This property is inherited from Wei Dai's [2009] Updateless Decision Theory; as noted in Section 9 of the source paper, simultaneously conditioning on $\textsc{Obs}=x$ and changing the intervention node creates a harmful "double update" that characterizes Yudkowsky's [2010] earlier Timeless Decision Theory.)

---

## 3. Subjunctive Dependence and Worked Applications

### 3.1 What is Subjunctive Dependence?

Why should an intervention on $\textsc{afdt}(\underline{P}, \underline{G}, \underline{x})$ propagate to a predictor's prior state in Newcomb's problem, yet not propagate to an arterial lesion in the Smoking Lesion problem? Yudkowsky and Soares answer via the concept of **subjunctive dependence**:

> *"Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."* (Section 3)

When two physical systems—such as two calculators computing $6288 + 1048$, two psychological twins deliberating in separate rooms, or an agent and a predictor's simulation of that agent—implement the same mathematical function on the same inputs, their outputs subjunctively depend on that function's logical value. Causal dependence is simply a special case of subjunctive dependence (e.g., theagent's physical muscles $\textsc{Act}$ causally and therefore subjunctively depend on the output of her decision algorithm). Purely statistical correlation, however, does not entail subjunctive dependence.

Because a mathematical function has a single output on a given input of logical necessity, imagining $\textsc{afdt}(\underline{P}, \underline{G}, \underline{x}) = a$ for suboptimal $a$ requires evaluating a *counterpossible* conditional (Cohen, 1990). In **A-FDT**, the graph $G$ serves as an explicit formal encoding of which variables in the universe subjunctively depend on the counterpossible variation of $\textsc{afdt}(\underline{P}, \underline{G}, \underline{x})$.

Let us trace how Equation (4) operates across three major classes of decision problems.

### 3.2 Case 1: Predictive vs. Diagnostic Correlations (Newcomb's Problem vs. The Smoking Lesion)

In **Newcomb's Problem**, transparent Box A contains $\$1,000$, and opaque Box B contains either $\$1,000,000$ ($\mathit{full}$) or $\$0$ ($\mathit{empty}$). A predictor with $99\%$ accuracy ($\textsc{Accurate} \in \{\mathit{accurate}, \mathit{inaccurate}\}$ with $P(\mathit{accurate}) = 0.99$) filled Box B iff she predicted the agent would leave Box A behind ($\mathit{onebox}$). Since the agent receives no differentiating observation during the problem, $\mathcal{X}$ is suppressed and the target node is $\textsc{afdt}(\underline{P}^F, \underline{G}^F)$.

In the **A-FDT** graph $G^F$ (Figure 3b of the source), $\textsc{afdt}(\underline{P}^F, \underline{G}^F)$ has two outgoing arrows:
$$\textsc{afdt}(\underline{P}^F, \underline{G}^F) \to \textsc{Act}, \qquad \textsc{afdt}(\underline{P}^F, \underline{G}^F) \to \textsc{Prediction} \to \textsc{Box B}$$
with $\textsc{Accurate} \to \textsc{Prediction}$ and $\textsc{Act}, \textsc{Box B} \to \textsc{V}$. The structural equations are:
$$\textsc{Act}(a) = a, \qquad \textsc{Box B}(a, \mathit{accurate}) = \begin{cases} \mathit{full} & \text{if } a = \mathit{onebox} \\ \mathit{empty} & \text{if } a = \mathit{twobox} \end{cases}, \qquad \textsc{Box B}(a, \mathit{inaccurate}) = \begin{cases} \mathit{empty} & \text{if } a = \mathit{onebox} \\ \mathit{full} & \text{if } a = \mathit{twobox} \end{cases}$$

Applying Equation (4), the **A-FDT** agent evaluates:
$$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{afdt}(\underline{P}^F, \underline{G}^F) = \mathit{onebox}\right)\right) = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000$$
$$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{afdt}(\underline{P}^F, \underline{G}^F) = \mathit{twobox}\right)\right) = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000$$
Since $\$990,000 > \$11,000$, $\mathrm{AFDT}(P^F, G^F) = \mathit{onebox}$.

Notice how **A-FDT** dissolves CDT's dominance argument. A CDT agent claims $\mathit{twobox}$ dominates $\mathit{onebox}$ because, holding $\textsc{Box B}$ fixed, $\textsc{Act} = \mathit{twobox}$ yields $+\$1,000$ in both states. From **A-FDT**'s perspective, holding $\textsc{Box B}$ fixed while varying $\textsc{Act}$ imagines a physical actuator malfunctioning while the decision function's output remains fixed. Under **A-FDT**'s own dominance principle—holding fixed the subjunctive dependency $\textsc{Accurate}$ and varying the decision function's output—$\mathit{onebox}$ yields $\$1,000,000$ vs. $\$1,000$ when $\textsc{Accurate} = \mathit{accurate}$ ($99\%$ of the time), and Expected Utility cleanly favors $\mathit{onebox}$.

Now contrast this with the **Smoking Lesion Problem**. An arterial lesion ($\textsc{Lesion} \in \{\mathit{lesion}, \mathit{nolesion}\}$ with prior $P(\mathit{lesion}) = p \in (0,1)$) causes agents to love smoking and causes fatal lung cancer $99\%$ of the time (versus $1\%$ without the lesion). Surviving cancer is worth $\$1,000,000$; smoking gives utility $\$1,000$ to an agent with the lesion.

How does **A-FDT** formalize the fact that the lesion causes the agent to love smoking without the lesion subjunctively depending on the **A-FDT** function? In Section 6, Yudkowsky and Soares model the lesion as determining *which utility function* (and thus which belief-preference distribution) the agent possesses: $\mathcal{U}_S$ (which values smoking at $+\$1,000$), inducing distribution $P_S^F$, or $\mathcal{U}_R$ (which values smoking at $-\$1$), inducing distribution $P_R^F$. Because the agent does not know whether she has the lesion, she cannot introspectively tell whether her calculation is running on $P_S^F$ or $P_R^F$, but whichever one she is actually running is fixed by $\textsc{Lesion}$.

In her graph $G^F$ (Figure 4 of the source), there are two logical nodes: $\textsc{afdt}(\underline{P_S^F}, \underline{G}^F)$ and $\textsc{afdt}(\underline{P_R^F}, \underline{G}^F)$. Crucially, $\textsc{Lesion}$ has *no* incoming arrows from either logical node; instead:
$$\textsc{Lesion} \to \textsc{Cancer} \to \textsc{Death} \to \textsc{V}, \qquad \textsc{Lesion}, \textsc{afdt}(\underline{P_S^F}, \underline{G}^F), \textsc{afdt}(\underline{P_R^F}, \underline{G}^F) \to \textsc{Act} \to \textsc{V}$$
where the physical action is determined by the multiplexing equation:
$$\textsc{Act}(\mathit{lesion}, s, r) \coloneqq s, \qquad \textsc{Act}(\mathit{nolesion}, s, r) \coloneqq r$$

Suppose the agent has the lesion, so her decision procedure evaluates $\mathrm{AFDT}(P_S^F, G^F)$ by intervening on $\textsc{afdt}(\underline{P_S^F}, \underline{G}^F)$. Because $\textsc{Lesion}$ and $\textsc{afdt}(\underline{P_R^F}, \underline{G}^F)$ are non-descendants of $\textsc{afdt}(\underline{P_S^F}, \underline{G}^F)$ in $G^F$, their probabilities remain invariant under the intervention:
$$P_S^F\left(\mathit{lesion} \;\middle|\; \mathtt{do}\left(\textsc{afdt}(\underline{P_S^F}, \underline{G}^F) = a\right)\right) = P_S^F(\mathit{lesion}) = p$$
Let $q \coloneqq P_S^F(\textsc{afdt}(\underline{P_R^F}, \underline{G}^F) = \mathit{smoke})$. In the branch where $\textsc{Lesion} = \mathit{lesion}$ (probability $p$), survival probability is $0.01$, yielding baseline health utility $0.01 \times \$1,000,000 = \$10,000$, and $\textsc{Act}$ equals the intervened value $a$. In the branch where $\textsc{Lesion} = \mathit{nolesion}$ (probability $1-p$), survival probability is $0.99$, yielding baseline health utility $0.99 \times \$1,000,000 = \$990,000$, and $\textsc{Act}$ is governed by $\textsc{afdt}(\underline{P_R^F}, \underline{G}^F)$, which smokes with probability $q$. Evaluated under $\mathcal{U}_S$, Equation (4) yields:
$$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{afdt}(\underline{P_S^F}, \underline{G}^F) = \mathit{smoke}\right)\right) = p(\$10,000 + \$1,000) + (1-p)(\$990,000 + q \cdot \$1,000)$$
$$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{afdt}(\underline{P_S^F}, \underline{G}^F) = \mathit{refrain}\right)\right) = p(\$10,000) + (1-p)(\$990,000 + q \cdot \$1,000)$$
The $\mathit{smoke}$ intervention strictly exceeds $\mathit{refrain}$ by $p \cdot \$1,000 > 0$. Thus $\mathrm{AFDT}(P_S^F, G^F) = \mathit{smoke}$.

### 3.3 Case 2: Observation-Indexed Interventions (Transparent Newcomb & Mechanical Blackmail)

The full power of Equation (4)—and its second structural departure from CDT—emerges when the predictor's action determines what observation $x \in \mathcal{X}$ the agent receives before choosing.

In the **Transparent Newcomb Problem** (isomorphic to **Parfit's Hitchhiker**), both boxes are transparent, so the agent directly observes $x \in \{\mathit{full}, \mathit{empty}\}$ before deciding whether to $\mathit{onebox}$ or $\mathit{twobox}$. The predictor placed $\$1,000,000$ in Box B iff she predicted with $99\%$ accuracy that the agent would $\mathit{onebox}$ *upon observing* $\mathit{full}$.

When an EDT or CDT agent observes $\textsc{Obs} = \mathit{full}$, she conditions her distribution on $\textsc{Obs} = \mathit{full}$, locking the probability of $\textsc{Box B} = \mathit{full}$ at $1$. Consequently, both EDT and CDT prescribe $\mathit{twobox}$ ($1,001,000 > 1,000,000$). Foreseeing this, the predictor leaves Box B empty, and EDT and CDT agents receive $\$1,000$ (or die in Parfit's desert).

Now consider how an **A-FDT** agent models the problem in $G^F$ (Figure 5b of the source). There are two observation-indexed logical nodes: $\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{full})$ and $\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{empty})$. Because the predictor specifically simulates what the agent will do *if shown a full box*, only $\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{full})$ points into $\textsc{Prediction}$:
$$\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{full}) \to \textsc{Prediction} \to \textsc{Box B}$$
Meanwhile, $\textsc{Prediction}$ (which determines whether Box B is full or empty, and thus which observation the agent receives) selects which of the two logical nodes controls the physical action $\textsc{Act}$:
$$\textsc{Act}\left(\textsc{Prediction}, a_{\mathit{full}}, a_{\mathit{empty}}\right) \coloneqq \begin{cases} a_{\mathit{full}} & \text{if } \textsc{Prediction} = 1 \text{ (i.e., } \textsc{Box B} = \mathit{full}\text{)} \\ a_{\mathit{empty}} & \text{if } \textsc{Prediction} = 2 \text{ (i.e., } \textsc{Box B} = \mathit{empty}\text{)} \end{cases}$$

*(Textual clarification for the reader: In Section 6 of the reference article, when writing the display expression for Transparent Newcomb, the authors inadvertently wrote $\mathbb{E}(\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P}^F, \underline{G}^F, \mathit{full})=a, \textsc{Obs}=\mathit{full})$ with an unclosed parenthesis. As their immediately following calculation and Section 5's prose confirm, that `, \textsc{Obs}=\mathit{full}` is a typographical artifact: had they conditioned on $\textsc{Obs}=\mathit{full}$, $\textsc{Box B}$ would be fixed to $\mathit{full}$ with probability $1$. Instead, the calculation evaluates Equation (4) directly without conditioning on $\textsc{Obs}=\mathit{full}$.)*

Let us execute the exact calculation from Equation (4) when the agent sees two full boxes ($x = \mathit{full}$) and therefore intervenes on $\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{full}) = a$. Let $q \coloneqq P^F(\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{empty}) = \mathit{twobox})$ be the agent's prior probability that she two-boxes when seeing an empty box:
* **Under $\mathtt{do}\left(\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{full}) = \mathit{onebox}\right)$**:
  * With probability $0.99$ ($\textsc{Accurate} = \mathit{accurate}$), $\textsc{Prediction} = 1$, $\textsc{Box B} = \mathit{full}$, and $\textsc{Act} = \textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{full}) = \mathit{onebox}$, yielding $\textsc{V} = \$1,000,000$.
  * With probability $0.01$ ($\textsc{Accurate} = \mathit{inaccurate}$), $\textsc{Prediction} = 2$, $\textsc{Box B} = \mathit{empty}$, and $\textsc{Act}$ is governed by $\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{empty})$, yielding expected utility $q \cdot \$1,000$.
  * Total expected utility: $\$990,000 + 0.01q \cdot \$1,000 = \$990,000 + \$10q$.
* **Under $\mathtt{do}\left(\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{full}) = \mathit{twobox}\right)$**:
  * With probability $0.01$ ($\textsc{Accurate} = \mathit{inaccurate}$), $\textsc{Prediction} = 1$, $\textsc{Box B} = \mathit{full}$, and $\textsc{Act} = \textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{full}) = \mathit{twobox}$, yielding $\textsc{V} = \$1,001,000$.
  * With probability $0.99$ ($\textsc{Accurate} = \mathit{accurate}$), $\textsc{Prediction} = 2$, $\textsc{Box B} = \mathit{empty}$, and $\textsc{Act}$ is governed by $\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{empty})$, yielding expected utility $q \cdot \$1,000$.
  * Total expected utility: $0.01(\$1,001,000) + 0.99q \cdot \$1,000 = \$10,010 + \$990q$.

For every $q \in [0, 1]$, $\$990,000 + \$10q > \$10,010 + \$990q$. Thus, $\mathrm{AFDT}(P^F, G^F, \mathit{full}) = \mathit{onebox}$. Even while staring directly at $\$1,000,000$ in Box B, the **A-FDT** agent recognizes that she is computing the output of the subroutine $\mathrm{AFDT}(P^F, G^F, \mathit{full})$; if that subroutine outputs $\mathit{twobox}$, then in $99\%$ of worlds she is never even called upon to execute it because she sees an empty box instead!

The exact same mechanism resolves **Mechanical Blackmail** (Dilemma 7, Figure 7 of the source), where a predictor launches a mutually destructive $\$1,000,000$ rumor-publishing program iff she predicts the agent will wire $\$1,000$ upon receiving the blackmail notice ($x = \mathit{blackmail}$). When evaluating $\mathrm{AFDT}(P^F, G^F, \mathit{blackmail})$, setting $\mathtt{do}(\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{blackmail}) = \mathit{refuse})$ causes the blackmailer not to launch the program in the hypothetical world (except with small prediction error $\epsilon$). Specifically, if the blackmailer falsely predicts payment with probability $\epsilon = 0.0009$, then $\mathit{pay}$ yields $-\$1,000$ (since she is always blackmailed and pays), whereas $\mathit{refuse}$ yields $-0.0009 \times \$1,000,000 = -\$900$ in expectation. **A-FDT** therefore prescribes $\mathit{refuse}$ even when holding the blackmail letter. (If instead the predictor's error rate is $\epsilon = 0.011$, refusing loses $0.011 \times \$1,000,000 = \$11,000$ in expectation while paying loses at most $\$1,000$, so **A-FDT** smoothly switches to $\mathit{pay}$.)

### 3.4 Case 3: Reflective Stability and Value of Information (Death in Damascus)

In **Death in Damascus** (Gibbard & Harper, 1978), Death perfectly predicts whether the agent stays in Damascus or flees to Aleppo (at a camel-riding cost of $\$1,000$) and meets her there, costing $\$1,000,000$ (her life). Under CDT, the agent is reflectively unstable: believing she will stay in Damascus makes fleeing appear to save her life, while believing she will flee makes staying appear to save her life. Even if the CDT agent uses a ratification procedure (Joyce, 2012) to settle on a mixed belief state $(P_*^C(\mathit{damascus}) = 0.5005, P_*^C(\mathit{aleppo}) = 0.4995)$, her CDT hypotheticals treat Death's location as independent of her action, causing her to act *as if* her survival probability is already $\ge 50\%$ (expected value $\$500,500$). Consequently, if offered a *truly random* coin for $\$1$ that genuinely thwarts Death's prediction $50\%$ of the time, the CDT agent refuses to buy it!

An **A-FDT** agent experiences neither instability nor delusion. In $G^F$, $\textsc{afdt}(\underline{P}^F, \underline{G}^F)$ points to both $\textsc{Act}$ and $\textsc{Death's Location}$. Under $\mathtt{do}(\textsc{afdt}(\underline{P}^F, \underline{G}^F) = \mathit{damascus})$, she dies in Damascus ($\textsc{V} = \$0$); under $\mathtt{do}(\textsc{afdt}(\underline{P}^F, \underline{G}^F) = \mathit{aleppo})$, she dies in Aleppo and pays for the camel ($\textsc{V} = -\$1,000$). She calmly stays in Damascus ($\textsc{V} = \$0$), and if offered a truly random coin for $\$1$—which severs the arrow from $\textsc{afdt}$ to $\textsc{Act}$ and replaces it with an unpredictable physical coin toss—she immediately pays $\$1$ to gain $\$500,000 - \$1 = \$499,999$ in expected utility.

| Decision Problem | EDT ($\mathrm{EDT}$) | CDT ($\mathrm{CDT}$) | A-FDT ($\mathrm{AFDT}$) | Why A-FDT Succeeds |
| :--- | :--- | :--- | :--- | :--- |
| **Newcomb's Problem** | One-box | Two-box | **One-box** | $\textsc{Prediction}$ is downstream of $\textsc{afdt}(\underline{P}, \underline{G})$ |
| **Smoking Lesion** | Refrain | Smoke | **Smoke** | $\textsc{Lesion}$ is upstream of $\textsc{Act}$, not downstream of $\textsc{afdt}$ |
| **Transparent Newcomb** | Two-box | Two-box | **One-box** | Intervenes on $\textsc{afdt}(\underline{P}, \underline{G}, \mathit{full})$ without conditioning on $\textsc{Obs}$ |
| **XOR Blackmail** | Pay | Refuse | **Refuse** | $\textsc{Infestation}$ is independent of $\textsc{afdt}(\underline{P}, \underline{G}, \mathit{letter})$ |
| **Mechanical Blackmail** | Pay | Pay | **Refuse** (for $\epsilon < 10^{-3}$) | Refusing lowers probability of receiving $\mathit{blackmail}$ in $M^{\mathit{refuse}\hookrightarrow}$ |
| **Death in Damascus** | Stay | Unstable / Rejects \$1 Coin | **Stay / Buys \$1 Coin** | Tracks $\textsc{Death}$'s dependence on $\textsc{afdt}$ vs. true randomness |

---

## 4. Open Questions and Operationalizing A-FDT for Unfamiliar Cases

### 4.1 What the Reference Article Leaves Open

While Yudkowsky and Soares provide a clear mathematical rule in Equation (4) *given* a subjunctive graphical model $(P, G)$, they explicitly identify two foundational aspects of the formalism that remain open or simplified in their presentation:

1. **Deducing the Subjunctive Dependency Graph $G$**: In Section 5, the authors note that while Pearl (2000) provides a rigorous methodology for inferring *causal* graphs from physical observation and intervention, *"no such formal treatment has yet been given to the problem of deducing the structure of other kinds of subjunctive dependence. Equation (4) works given a graph that accurately describes how changing the value of a logical variable affects other variables, but it is not yet clear how to construct such a thing."*
2. **Action Iteration (A-FDT) vs. Policy Iteration**: In Footnotes 7 and 16, the authors remark that in their preferred formalization, agents iterate over complete *policies* $\pi : \mathcal{X} \to \mathcal{A}$ by intervening on a single unindexed node $\textsc{fdt}(\underline{P}, \underline{G}) = \pi$ and then executing $\pi(x)$, rather than intervening on the observation-specific action node $\textsc{afdt}(\underline{P}, \underline{G}, \underline{x}) = a$ as in Equation (4). They state that *"The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."*

If a reader wishes to apply **A-FDT** (Equation 4) to a novel decision problem, how should they systematically construct $(P, G)$, and how can they tell whether **A-FDT**'s observation-indexed action intervention is sufficient? In the remainder of this section, we develop and justify an explicit **operational interpretation** that goes beyond the source text to make **A-FDT** practically applicable to unfamiliar cases.

### 4.2 An Operational Procedure for Constructing $(P, G)$ under A-FDT

*(Note: The following four-step construction and structural criterion represent our proposed operationalization of Yudkowsky and Soares's modeling practices, designed to give a reproducible procedure for building $(P, G)$ in novel problems.)*

When confronting an unfamiliar decision problem with action space $\mathcal{A}$ and reachable observation histories $\mathcal{X} = \{x_1, \dots, x_m\}$ (and possible preference/epistemic types $\Theta = \{\theta_1, \dots, \theta_k\}$ if the agent has uncertainty about her own utility function, as in the Smoking Lesion problem), construct $(P, G)$ as follows:

* **Step 1 (Instantiate the Logical Node Family)**: For each epistemic/preference type $\theta \in \Theta$ and each reachable observation $x \in \mathcal{X}$, introduce a logical root variable:
  $$D_{\theta, x} \coloneqq \textsc{afdt}(\underline{P_\theta}, \underline{G}, \underline{x}) \in \mathcal{A}$$
  In $G$, every node $D_{\theta, x}$ has **in-degree zero** (no parents). Why? Because $D_{\theta, x}$ represents the timeless mathematical output of the function $\mathrm{AFDT}$ on fixed syntactic inputs $(P_\theta, G, x)$. Physical events in the world do not change what a mathematical function outputs on a fixed argument; rather, physical events determine *which* argument $(\theta, x)$ the agent physically encounters!
* **Step 2 (Wire Subjunctive Dependencies to Environmental Predictors)**: For any environmental variable $Z$ (such as a predictor's action, a twin's choice, or a verification mechanism), draw a directed edge $D_{\theta, x} \to Z$ **if and only if** the physical or computational process generating $Z$ depends on a simulation, deduction, or structural copy of how the agent's decision procedure behaves when given input $(\theta, x)$, and that dependency would vary if the mathematical output $D_{\theta, x}$ were altered while holding exogenous noise fixed.
  * *Operational Test*: Ask whether an advance binding precommitment by the agent to output $a$ specifically upon observing $x$ in state $\theta$—made before $Z$ is determined and made visible to the mechanism generating $Z$ in the same way the agent's disposition is visible—would causally alter the distribution of $Z$. If yes, include the edge $D_{\theta, x} \to Z$; if no (as with a genetic lesion or pre-existing termite infestation), omit it.
* **Step 3 (Wire Observations and the Physical Multiplexer $\textsc{Act}$)**: Let $\textsc{Type} \in \Theta$ and $\textsc{Obs} \in \mathcal{X}$ be physical variables determined by their causal ancestors in the environment. Define the physical action node $\textsc{Act}$ via the deterministic multiplexing structural equation:
  $$\textsc{Act}\left(\textsc{Type}, \textsc{Obs}, \{D_{\theta, x}\}_{\theta \in \Theta, x \in \mathcal{X}}\right) \coloneqq \sum_{\theta \in \Theta} \sum_{x \in \mathcal{X}} \mathbb{I}(\textsc{Type} = \theta \land \textsc{Obs} = x) \cdot D_{\theta, x}$$
  This equation guarantees that $D_{\theta, x}$ controls the agent's physical body $\textsc{Act}$ *only* in worlds where the agent actually has type $\theta$ and observes $x$.
* **Step 4 (Evaluate Equation 4)**: Given actual type $\theta^*$ and actual observation $x^*$, compute for each $a \in \mathcal{A}$:
  $$\mathbb{E}_{P_{\theta^*}}\left[\textsc{V} \;\middle|\; \mathtt{do}(D_{\theta^*, x^*} = a)\right]$$
  by fixing $D_{\theta^*, x^*} = a$, leaving all exogenous variables and all *other* logical nodes $D_{\theta, x}$ for $(\theta, x) \neq (\theta^*, x^*)$ distributed according to $P_{\theta^*}$, and propagating through $G$ to $\textsc{V}$.

### 4.3 Applying the Procedure to an Unfamiliar Dilemma

To see how this operational procedure handles an unfamiliar case that combines statistical confounding, imperfect prediction, and observation-switching, consider the following novel problem:

> **The Diagnostic vs. Predictive Screening Dilemma**: An agent may have a latent genetic condition ($\textsc{Gene} \in \{1, 0\}$ with prior $P(\textsc{Gene}=1) = 0.2$) that causes a $-\$100,000$ health loss ($\textsc{Illness} = 1$). A diagnostic clinic sends the agent a warning text ($\textsc{Obs} = \mathit{warn}$ vs. $\textsc{Obs} = \mathit{clear}$) under the following protocol:
> 1. If $\textsc{Gene} = 1$, an automated lab test immediately sends $\mathit{warn}$ with probability $1$.
> 2. If $\textsc{Gene} = 0$, the clinic's behavioral AI predicts (with $90\%$ accuracy, $\textsc{Acc} \sim \mathrm{Bernoulli}(0.9)$) whether the agent will purchase a $\$5,000$ wellness package ($a = \mathit{buy}$ vs. $a = \mathit{decline}$) upon receiving $\mathit{warn}$. If the AI predicts $\mathit{buy}$, the clinic sends a promotional $\mathit{warn}$ text to extract the $\$5,000$; if it predicts $\mathit{decline}$, it sends $\mathit{clear}$.
> 3. The wellness package does *not* cure the genetic illness, but it provides $\$2,000$ of general comfort utility in all states (so net cost of buying is $-\$3,000$), plus a $\$10,000$ stress-relief rebate *only* if $\textsc{Gene} = 0$ and the agent received $\mathit{warn}$ (so if $\textsc{Gene} = 0$ and $\textsc{Obs} = \mathit{warn}$, buying yields $-\$5,000 + \$2,000 + \$10,000 = +\$7,000$ relative to declining!).
> 
> Suppose the agent receives $\textsc{Obs} = \mathit{warn}$. Should she $\mathit{buy}$ or $\mathit{decline}$?

Let us compare CDT, EDT, and **A-FDT** on this unfamiliar case:

* **How CDT and EDT Reason**: Conditional on $\textsc{Obs} = \mathit{warn}$, if the agent knew she was the sort of agent who declines, $\mathit{warn}$ would strongly indicate $\textsc{Gene}=1$, where buying loses $\$3,000$ net. Under CDT, holding the past fixed upon seeing $\mathit{warn}$, buying gains $+\$7,000$ if $\textsc{Gene}=0$ and loses $-\$3,000$ if $\textsc{Gene}=1$. Notice that if CDT expects itself to buy, then $P(\textsc{Gene}=0 \mid \mathit{warn}) = \frac{0.8 \times 0.9}{0.2 + 0.8 \times 0.9} = \frac{0.72}{0.92} \approx 0.7826$, so CDT calculates the expected causal gain of buying as $0.7826(+\$7,000) + 0.2174(-\$3,000) = +\$4,826 > 0$ and buys! As a result, the AI predicts CDT will buy, sends $\mathit{warn}$ $90\%$ of the time when $\textsc{Gene}=0$, and traps the CDT agent into receiving stressful promotional warnings and paying $\$5,000$ whenever she is healthy.
* **How A-FDT Applies Our 4-Step Procedure**:
  1. **Nodes**: Instantiate $D_{\mathit{warn}} \coloneqq \textsc{afdt}(\underline{P}, \underline{G}, \mathit{warn})$ and $D_{\mathit{clear}} \coloneqq \textsc{afdt}(\underline{P}, \underline{G}, \mathit{clear})$.
  2. **Subjunctive Edges**: $\textsc{Gene}$ is a genetic state with no incoming edge from $D_{\mathit{warn}}$. The AI predictor simulates $D_{\mathit{warn}}$, so $D_{\mathit{warn}}, \textsc{Acc} \to \textsc{AI}$.
  3. **Observations and Multiplexer**:
     $$\textsc{Obs} = \begin{cases} \mathit{warn} & \text{if } \textsc{Gene}=1 \text{ or } (\textsc{Gene}=0 \land \textsc{AI}=\mathit{buy}) \\ \mathit{clear} & \text{if } \textsc{Gene}=0 \land \textsc{AI}=\mathit{decline} \end{cases}$$
     $$\textsc{Act} = \mathbb{I}(\textsc{Obs}=\mathit{warn}) D_{\mathit{warn}} + \mathbb{I}(\textsc{Obs}=\mathit{clear}) D_{\mathit{clear}}$$
     When $\textsc{Obs}=\mathit{clear}$, buying has no rebate and loses $-\$3,000$, so let $D_{\mathit{clear}} = \mathit{decline}$ (utility $\$0$).
     Wait: how does the $\$10,000$ stress-relief rebate work when $\textsc{Gene}=0$ and $\textsc{Obs}=\mathit{warn}$? Being sent the promotional $\mathit{warn}$ text when $\textsc{Gene}=0$ causes $-\$12,000$ of anxiety, which buying the package partially relieves by $+\$10,000$ (plus $+\$2,000$ comfort minus $\$5,000$ fee = $-\$5,000$ net if she buys, versus $-\$12,000$ net if she declines, compared to $\$0$ if she receives $\mathit{clear}$!).
  4. **Evaluating Equation (4) at $x = \mathit{warn}$**:
     * **Under $\mathtt{do}(D_{\mathit{warn}} = \mathit{buy})$**:
       * If $\textsc{Gene}=1$ (prob $0.2$): $\textsc{Obs}=\mathit{warn}$, $\textsc{Act}=\mathit{buy}$, utility $= -\$100,000 - \$3,000 = -\$103,000$.
       * If $\textsc{Gene}=0, \textsc{Acc}=1$ (prob $0.8 \times 0.9 = 0.72$): $\textsc{AI}=\mathit{buy} \implies \textsc{Obs}=\mathit{warn}$, $\textsc{Act}=\mathit{buy}$, utility $= -\$5,000$.
       * If $\textsc{Gene}=0, \textsc{Acc}=0$ (prob $0.8 \times 0.1 = 0.08$): $\textsc{AI}=\mathit{decline} \implies \textsc{Obs}=\mathit{clear}$, $\textsc{Act}=\mathit{decline}$, utility $= \$0$.
       * Total $\mathbb{E}[\textsc{V} \mid \mathtt{do}(D_{\mathit{warn}}=\mathit{buy})] = 0.2(-\$103,000) + 0.72(-\$5,000) + 0.08(\$0) = -\$24,200$.
     * **Under $\mathtt{do}(D_{\mathit{warn}} = \mathit{decline})$**:
       * If $\textsc{Gene}=1$ (prob $0.2$): $\textsc{Obs}=\mathit{warn}$, $\textsc{Act}=\mathit{decline}$, utility $= -\$100,000$.
       * If $\textsc{Gene}=0, \textsc{Acc}=1$ (prob $0.72$): $\textsc{AI}=\mathit{decline} \implies \textsc{Obs}=\mathit{clear}$, $\textsc{Act}=\mathit{decline}$, utility $= \$0$.
       * If $\textsc{Gene}=0, \textsc{Acc}=0$ (prob $0.08$): $\textsc{AI}=\mathit{buy} \implies \textsc{Obs}=\mathit{warn}$, $\textsc{Act}=\mathit{decline}$, utility $= -\$12,000$.
       * Total $\mathbb{E}[\textsc{V} \mid \mathtt{do}(D_{\mathit{warn}}=\mathit{decline})] = 0.2(-\$100,000) + 0.72(\$0) + 0.08(-\$12,000) = -\$20,960$.

Because $-\$20,960 > -\$24,200$, $\mathrm{AFDT}(P, G, \mathit{warn}) = \mathit{decline}$! By intervening on $D_{\mathit{warn}}$ without conditioning on $\textsc{Obs}=\mathit{warn}$, **A-FDT** simultaneously (i) leaves the genetic confounder $\textsc{Gene}$ untouched ($P(\textsc{Gene}=1) = 0.2$ in both hypotheticals) and (ii) accounts for the fact that choosing $\mathit{decline}$ prevents the AI from sending the anxiety-inducing promotional text in $90\%$ of healthy worlds.

### 4.4 When Does A-FDT Diverge from Policy-Level FDT?

Finally, our operational formalization allows us to state precisely when **A-FDT** (Equation 4) diverges from policy-level FDT (Footnotes 7 and 16)—an additional mathematical clarification beyond the source text.

In **A-FDT**, when the agent observes $x_1$, she optimizes $D_{x_1}$ *holding fixed* her prior beliefs about $D_{x_2}$ for $x_2 \neq x_1$. This is equivalent to finding a sequential Nash equilibrium among her own observation-branches $(D_{x_1}, \dots, D_{x_m})$. Policy-level FDT, by contrast, jointly optimizes the entire tuple $\pi = (D_{x_1}, \dots, D_{x_m}) \in \mathcal{A}^{\mathcal{X}}$. The two procedures yield identical prescriptions whenever each predictor in the environment depends on at most one active observation branch, or when the payoff is additively separable across observation branches. They can diverge only if a predictor's reward rule depends *jointly and non-separably* on the agent's counterfactual actions across multiple distinct observations $(D_{x_1}, D_{x_2})$ (for instance, a coordinator who rewards the agent in branch $x_1$ iff $D_{x_1} = D_{x_2}$, where $D_{x_2}$ is never actually reached when $D_{x_1}$ is optimal). In such cross-branch coordination problems, **A-FDT** evaluates only variations in $D_{x_1}$ at runtime, whereas policy-level FDT coordinates $(D_{x_1}, D_{x_2})$ simultaneously.

---

## 5. Conclusion

**Action functional decision theory (A-FDT)**, as formalized in Equation (4) of Yudkowsky and Soares, represents a major conceptual and technical advance in the theory of instrumental rationality. By shifting the locus of decision-theoretic intervention from the physical action token $\textsc{Act}$ to the logical output node $\textsc{afdt}(\underline{P}, \underline{G}, \underline{x})$—and by responding to observations $x$ through indexing the point of intervention rather than Bayesian conditioning—**A-FDT** captures the causal realism of CDT while preserving the predictive and game-theoretic coordination power of precommitment. Although foundational questions remain regarding how bounded agents learn subjunctive dependency graphs $G$ from first principles, our operational four-step procedure demonstrates that whenever the causal and computational mechanisms of a decision environment are specified, **A-FDT** provides an unambiguous, mathematically rigorous rule that consistently maximizes utility across classic and novel dilemmas alike.

---

## References

* Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
* Cohen, D. (1990). On what cannot be. In *Truth or Consequences: Essays in Honor of Nuel Belnap* (pp. 123–132). Kluwer Academic Publishers.
* Dai, W. (2009). Towards a new decision theory. *Less Wrong*.
* Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Eells, E. (1984). Metatickles and the dynamics of deliberation. *Theory and Decision*, 17(1), 71–95.
* Gibbard, A., & Harper, W. L. (1978). Counterfactuals and two kinds of expected utility. In *Foundations and Applications of Decision Theory* (Vol. 1, pp. 125–162). D. Reidel.
* Jeffrey, R. C. (1983). *The Logic of Decision* (2nd ed.). University of Chicago Press.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Joyce, J. M. (2012). Regret and instability in causal decision theory. *Synthese*, 187(1), 123–145.
* Kleene, S. C. (1938). On notation for ordinal numbers. *Journal of Symbolic Logic*, 3(4), 150–155.
* Lewis, D. (1979). Prisoners' dilemma is a Newcomb problem. *Philosophy & Public Affairs*, 8(3), 235–240.
* Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
* Nozick, R. (1969). Newcomb's problem and two principles of choice. In *Essays in Honor of Carl G. Hempel* (pp. 114–146). D. Reidel.
* Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
* Pearl, J. (1996). Causation, action, and counterfactuals. In *6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-'96)* (pp. 51–73). Morgan Kaufmann.
* Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Peirce, C. S. (1934). *Collected Papers of Charles Sanders Peirce, Vol. V: Pragmatism and Pragmaticism*. Harvard University Press.
* Skyrms, B. (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Soares, N., & Fallenstein, B. (2015). Toward idealized decision theory. *arXiv preprint arXiv:1507.01986*.
* Yudkowsky, E. (2010). *Timeless Decision Theory*. The Singularity Institute.
* Yudkowsky, E., & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Scope**

I'm currently focused on defining the scope for this essay or blog post. The goal is to explain action functional decision theory, drawing from the provided reference. I'm aiming for a length between 2,400 and 3,000 words.


**Clarifying A-FDT's Core**

I'm now zeroing in on Equation (4) from Section 5 as the definitive formal expression of A-FDT. I'm focusing on consistently using the term "A-FDT" throughout, setting it apart from EDT, CDT, and policy-based FDT. I'll meticulously explain its mathematical underpinnings, action evaluation, dependency handling, and counterfactual reasoning. Where the source material raises questions about aspects like the subjunctive dependency graph, policy/action iteration, and counterpossibilities, I'm developing operational interpretations. I'll make sure to clearly differentiate the source's claims from my own interpretations.


**Refining A-FDT's Presentation**

I'm solidifying the focus on A-FDT, especially Equation (4). My objective now involves terminology; I'm ensuring consistent use of "A-FDT" throughout, setting it apart from other theories. I will remain very careful about direct quotations; I'll maintain their original wording, while introducing A-FDT everywhere else. The goal is a rigorous explanation that enables readers to apply it in novel situations.


**Interpreting Key Concepts**

I'm now diving deeper into how the source material handles dependencies and counterfactuals, especially the subjunctive aspects. I am going to address some open questions from the paper, like deducing the dependency graph and formalizing counterpossibilities. My goal is to develop a clear operational interpretation, differentiating the source's claims from my own ideas. My focus is on the action-level intervention within Equation (4), contrasting it with policy-level interventions as noted in the footnotes. I'm aiming for a readable mathematical essay, aiming for ~2,650–2,850 words.


**Formalizing A-FDT**

I'm working to formalize A-FDT. I'm focusing on the action-level intervention in Equation (4), contrasting it with policy-level interventions noted in footnotes 7 and 16. I am carefully evaluating the distinctions between A-FDT and other decision theories, and I'm comparing key equations: Expected Utility, EDT, and CDT. My goal is to ensure a precise mathematical grounding for this action-focused approach.


**Analyzing Equation (4)**

I'm now closely examining Equation (4) and its implications. I noticed a subtle but significant difference in Section 6's presentation, specifically the inclusion of $\textsc{Obs}=x$ in the conditioning, which is absent from the original Equation (4) in Section 5. I will make sure this difference is clarified. I am diving into how observations are handled and will interpret this discrepancy to better explain the distinction between CDT and A-FDT.


**Interpreting the Calculations**

I'm now focused on the calculations in Section 6, especially regarding Transparent Newcomb. I've realized that the paper's math in that section, when calculating the unconditional expectation, actually has a typo, which will be fixed. This contradicts Equation (4), Section 5, and Section 9. I am carefully examining this discrepancy and will interpret it to improve the paper's clarity, and also I'll be clear to point out the math for the reader.


**Developing the Foundation**

I'm structuring the essay to introduce A-FDT effectively. I'm starting with the classic EDT vs. CDT debate and highlighting their limitations in complex scenarios like Newcomb's problem and Parfit's Hitchhiker. I'll then introduce A-FDT's core: treating decisions as outputs of a fixed decision function. I'll clarify the distinction between type and token interventions. I'll move from Joyce's expected utility representation to formalize A-FDT's architecture using a decision-hypothetical connective.


**Formalizing A-FDT's Definition**

I'm currently working on formally presenting Equation (4) as the core of A-FDT, explicitly using "A-FDT" to differentiate it from policy-based FDT. I'll describe each mathematical component: the probability distribution $P$ encompassing physical and logical variables, the augmented DAG $G$ representing causal and subjunctive dependencies, and the quoting/dequoting notation ($\underline{P}, \underline{G}, \underline{x}$) with self-reference enabled by Kleene's second recursion theorem.


**Differentiating A-FDT's Principles**

I'm currently focused on the differences between CDT (Equation 3) and A-FDT (Equation 4). I've noted two key structural distinctions: the point of intervention and the role of observations. My goal is to clearly explain these differences, especially the updatelessness of A-FDT and the implications of intervening on the logical node $\textsc{afdt}(\underline{P}, \underline{G}, \underline{x})$. I'll also clarify the notation, to avoid reader confusion from the discrepancy in section 6. I am now working on practical applications of A-FDT. I will show how to construct (P, G) and evaluate A-FDT on different structures.


**Elaborating on Examples**

I'm now diving into concrete examples. I'm focusing on how A-FDT applies to classic problems. I will show how action interventions work through examples like Transparent Newcomb and the Smoking Lesion scenario. I am focusing on detailed computations, including expected utilities, clarifying the multiplexing mechanisms involved when observations are present. I'm aiming for practical demonstrations to solidify my understanding.


**Operationalizing A-FDT**

I'm working to make A-FDT useful in unfamiliar cases. I'm focusing on contrasting action-level A-FDT with policy-level interventions, to clarify the limits of the source paper. I will specifically operationalize constructing the subjunctive graph and formalizing counterpossibilities. My aim is to distinguish the source's claims from my interpretations. I'm carefully constructing specific examples and comparing them to policy-level thinking. I am currently considering the application of updatelessness to an unfamiliar case.


**Developing the Steps**

I'm now outlining a step-by-step procedure for applying A-FDT to new situations. I'm taking the existing concepts and making them into a clearly operational 4-step process. First, I'm computationally factoring the decision problem to identify relevant variables, including exogenous states, candidate computational nodes $\textsc{afdt}(\underline{P}, \underline{G}, \underline{x})$, environmental predictors, the observation map $\textsc{Obs}$, and the physical actuator multiplexing rule $\textsc{Act}$. My next steps will provide detailed descriptions of each of these steps, to maximize the understanding of this process.


**Operationalizing A-FDT Further**

I've just added three detailed steps to apply A-FDT in novel situations. I'm focusing on providing practical guidance. I'm building on the previous 4-step process by formally constructing a directed subjunctive graph, which allows me to differentiate between statistical confounders, the observation map, and the physical actuator multiplexing rule. I'm creating an example contrasting two screening processes to illustrate when A-FDT handles an unfamiliar case, and when it requires additional steps.


**Refining A-FDT's Application**

I'm currently working on clarifying when and how to apply A-FDT versus policy-level functional decision theory (FDT), specifically when the predictor considers multiple observational branches. I'll make sure the mathematical notation remains clear, consistent, and thoroughly explained. I'll also ensure all quotes from the original source are verbatim. My next step will be to create a brief synthesis of A-FDT's theoretical contributions and practical applications.


```
