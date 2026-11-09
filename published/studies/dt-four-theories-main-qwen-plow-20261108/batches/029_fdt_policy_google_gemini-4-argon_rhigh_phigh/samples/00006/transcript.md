# 029_fdt_policy_google_gemini-4-argon_rhigh_phigh / 00006

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/650ef091-503a-4782-8667-7575a5fd8fe3/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/650ef091-503a-4782-8667-7575a5fd8fe3/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Choosing What to Be: A Mathematical Account of Policy Functional Decision Theory (P-FDT)

## 1. Introduction: From Physical Acts to Mathematical Policies

For half a century, normative decision theory was locked in a stalemate between two rival paradigms: **Evidential Decision Theory (EDT)** and **Causal Decision Theory (CDT)**. When an agent evaluates a potential action, EDT asks what the world is likely to be like *conditional* on taking that action—in effect asking, *"Which physical act of mine would be the best news to hear I took?"* CDT, by contrast, evaluates actions via causal interventions, asking, *"Which physical act of mine causes the best outcome?"* 

Measured by average utility achieved across classic decision-theoretic dilemmas, neither theory is satisfactory. EDT triumphs in Newcomb's problem (Nozick 1969), reliably walking away with \$1,000,000 where CDT settles for \$1,000, but EDT fails in the Smoking Lesion problem (Skyrms 1980) and is systematically exploitable in blackmail dilemmas where an adversary links an agent's actions to purely statistical items of good news. Conversely, CDT avoids managing the news in the Smoking Lesion problem, but defects against psychological twins in the Prisoner's Dilemma (Lewis 1979), dies in the desert in Parfit's Hitchhiker problem (Parfit 1986), and spirals into reflective instability in Death in Damascus (Gibbard and Harper 1978).

In *"Functional Decision Theory: A New Theory of Instrumental Rationality"* (2017), Eliezer Yudkowsky and Nate Soares break this impasse by proposing that rational agency should not center on choosing an isolated physical act token. Instead, an agent should treat her decision as the output of a fixed mathematical function and ask: *"Which output of this very function would yield the best outcome?"* 

Throughout the main text of their paper, Yudkowsky and Soares formalize an action-selection rule—which we will refer to as **action-based FDT** (or standard **FDT**)—that takes an agent's world-model and current observation history as inputs and intervenes on the logical output corresponding to that specific observation. Yet, in two crucial footnotes, the authors reveal that this action-based rule is actually a pedagogical simplification of a deeper, more general theory. In Footnote 7, they write:

> *"In the authors' preferred formalization of FDT, agents actually iterate over policies (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."*

In Footnote 16, while discussing how an agent responds to evidence without standard Bayesian updating, they elaborate on this policy-selection mechanism:

> *"As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."*

We call this preferred formulation **Policy Functional Decision Theory (P-FDT)**. This essay provides a self-contained mathematical exposition of **P-FDT**, explaining its philosophical motivation, its formal procedure for evaluating counterfactuals, how to apply it to concrete decision problems, where it diverges from action-based FDT, and how we can operationally resolve the technical questions that Yudkowsky and Soares's footnotes leave open.

---

## 2. The Formal Architecture of EDT, CDT, FDT, and P-FDT

### 2.1 The Expected Utility Framework

Following Gibbard and Harper (1978) and Joyce (1999), Yudkowsky and Soares frame EDT, CDT, FDT, and **P-FDT** within a common expected utility architecture. Let $\mathcal{A}$ be a finite set of physical actions, $\mathcal{X}$ be a countable set of possible observation histories, and $\mathcal{O} = \{o_1, o_2, \dots\}$ be a countable set of outcomes equipped with a bounded real-valued utility function $\mathcal{U}: \mathcal{O} \to \mathbb{R}$. 

To evaluate options after receiving an observation $x \in \mathcal{X}$, an agent maintains a world-model $M$ and constructs, for each candidate option, a computational or mental object $M^{a \hookrightarrow}$ called a *hypothetical*. This hypothetical yields a probability distribution $P(a \hookrightarrow o_j \,;\, x)$ over outcomes $o_j \in \mathcal{O}$, from which the agent computes expected utility:

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j \,;\, x) \cdot \mathcal{U}(o_j). \tag{1}$$

As Joyce's (1999) representation theorem establishes, competing expected utility theories do not disagree about how outcomes are valued; they disagree about *"the epistemic perspective from which actions are to be evaluated"*—that is, how to represent the world-model $M$ and how to construct hypotheticals $P(- \hookrightarrow - \,;\, x)$ from $M$.

Let $\textsc{Obs}$, $\textsc{Act}$, and $\textsc{Outcome}$ be random variables taking values in $\mathcal{X}$, $\mathcal{A}$, and $\mathcal{O}$ respectively, and define the utility variable $\textsc{V} \coloneqq \mathcal{U}(\textsc{Outcome})$. 

1. **Evidential Decision Theory (EDT)** represents $M$ purely as a probability distribution $P$ and constructs hypotheticals via standard Bayesian conditioning on both the observation $x$ and the action $a$:
   $$\mathrm{EDT}(P, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs} = x,\, \textsc{Act} = a\right). \tag{2}$$

2. **Causal Decision Theory (CDT)** augments $P$ with a directed acyclic graph (DAG) $G$ encoding causal dependencies (Pearl 1996, 2000). To evaluate $a \in \mathcal{A}$, CDT conditions on the observation $\textsc{Obs} = x$ and applies Pearl's graphical surgery operator $\mathtt{do}(\textsc{Act} = a)$, severing all incoming arrows into $\textsc{Act}$ while propagating causal effects downstream:
   $$\mathrm{CDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{Act} = a),\, \textsc{Obs} = x\right). \tag{3}$$

3. **Action-Based Functional Decision Theory (FDT)** expands the graph $G$ so that it encodes not only physical causation, but also logical, mathematical, and computational dependencies—what the authors term *subjunctive dependence*. In action-based FDT, the probability distribution $P$ includes variables representing the outputs of mathematical functions. Specifically, for a world-model $(P, G)$ and observation $x$, the graph contains a node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ representing the logical output of the $\mathrm{FDT}$ function when evaluated on inputs $(P, G, x)$ (where underlines denote dequotation: if $x = 3$, then $\textsc{Z}\underline{x}$ denotes the variable name $\textsc{Z}3$, constructed self-referentially via Kleene's [1938] second recursion theorem). Action-based FDT prescribes:
   $$\mathrm{FDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right). \tag{4}$$

Notice two crucial differences between CDT in Equation (3) and action-based FDT in Equation (4). First, rather than intervening on the physical token $\textsc{Act}$, action-based FDT intervenes on the logical variable $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$. Second, action-based FDT does *not* condition $P$ on $\textsc{Obs} = x$. (As the authors note in Section 9, this lack of Bayesian conditioning inspired the name of Wei Dai's [2009] *Updateless Decision Theory* [UDT], whereas Yudkowsky's [2010] *Timeless Decision Theory* [TDT] both conditioned on evidence and changed the point of intervention, creating a harmful "double update.") Instead, in action-based FDT, observing $x$ rather than $y$ changes *which logical node* the agent intervenes upon: from $\textsc{fdt}(\underline{P}, \underline{G}, \underline{y})$ to $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$.

### 2.2 Formalizing P-FDT

While action-based FDT represents each observation-contingent output $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ as a separate node in $G$, **P-FDT** unifies them into a single mathematical object: a *policy*. 

To turn the prose of Footnotes 7 and 16 into an explicit mathematical formalism (an operationalization that extends the notation of Section 5 of the reference paper), let $\Pi \coloneqq \mathcal{A}^{\mathcal{X}} = \{\pi : \mathcal{X} \to \mathcal{A}\}$ denote the set of all deterministic policies mapping observations to actions. (When $\mathcal{X}$ and $\mathcal{A}$ are finite, $\Pi$ is a finite set of cardinality $|\mathcal{A}|^{|\mathcal{X}|}$.) 

In a **P-FDT** world-model $M = (P, G)$, the graph $G$ contains a single logical decision node $\textsc{pfdt}(\underline{P}, \underline{G})$ taking values in the policy space $\Pi$. How does this node connect to the rest of the graph?
* **Physical Execution:** The agent's physical action node $\textsc{Act}$ is a child of both the policy node $\textsc{pfdt}(\underline{P}, \underline{G})$ and the observation node $\textsc{Obs}$, governed by the evaluation map $\mathrm{eval}: \Pi \times \mathcal{X} \to \mathcal{A}$:
  $$\textsc{Act}\big(\pi, x\big) \coloneqq \pi(x). \tag{5}$$
* **Environmental and Multi-Agent Predictions:** Any predictor in the environment that models the agent, or any twin/copy that implements the same decision algorithm on the same prior model $(P, G)$, is causally or logically downstream of the policy node $\textsc{pfdt}(\underline{P}, \underline{G})$.

Following Footnote 16—which specifies that the algorithm *"intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action"*—the **P-FDT** decision procedure consists of two steps:

1. **Global Policy Selection:** The agent iterates over candidate policies $\pi \in \Pi$, constructs a hypothetical $M^{\pi \hookrightarrow}$ for each policy via the graphical intervention $\mathtt{do}\big(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\big)$, and selects the policy $\pi^*$ that maximizes unconditional expected utility:
   $$\pi^*(P, G) \coloneqq \argmax_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right). \tag{6}$$

2. **Local Policy Application:** Having identified the optimal policy $\pi^*(P, G) \in \Pi$, the agent applies this policy to her actual observation $x \in \mathcal{X}$ to output a concrete physical action:
   $$\mathrm{PFDT}(P, G, x) \coloneqq \big[\pi^*(P, G)\big](x) = \left[\argmax_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right)\right](x). \tag{7}$$

In Peirce's (1934) type-token terminology, CDT intervenes on the physical action *token* $\textsc{Act}$; action-based FDT intervenes on the observation-indexed action *type* $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$; and **P-FDT** intervenes on the global policy *type* $\textsc{pfdt}(\underline{P}, \underline{G})$.

---

## 3. Subjunctive Dependence, Counterpossibles, and How P-FDT Evaluates Dilemmas

### 3.1 Subjunctive Dependence and Counterpossible Reasoning

Why does intervening on $\textsc{pfdt}(\underline{P}, \underline{G})$ affect a predictor's past prediction or a twin's causally isolated action, without presupposing retrocausality or telepathy? The philosophical core of both FDT and **P-FDT** is *subjunctive dependence*.

When two physical systems compute the same mathematical function—such as two calculators on opposite sides of the globe computing $6288 + 1048 = 7336$, or an agent and a predictor's internal simulation of that agent both evaluating $\mathrm{PFDT}(P, G, x)$—their physical outputs subjunctively depend on that abstract function. Causal dependence is a special case of subjunctive dependence (what a scribe writes down subjunctively depends on the calculator's output because it is caused by it), whereas mere statistical correlation is not (if two calculators in Paris and Tokyo happen to be pink by coincidence, intervening on the color of one does not alter the other). As Yudkowsky and Soares summarize the analogy:

> *"Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."*

Because a mathematical function $\mathrm{PFDT}(P, G, -)$ deterministically outputs a single policy $\pi^*$ of logical necessity, asking *"What would the universe look like if $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$ for some $\pi \neq \pi^*$?"* requires evaluating a *counterpossible conditional*—a counterfactual whose antecedent is logically impossible (Cohen 1990). Ideally, one would define an epistemic operator $\mathtt{true}(\phi)$ that updates a probability distribution $P$ to reflect the counterpossible supposition that the logical sentence $\phi$ holds. Because no general formal account of $\mathtt{true}(\phi)$ yet exists, **P-FDT** (like action-based FDT) encodes the relevant logical and computational dependencies directly into the augmented graph $G$, allowing Pearl's $\mathtt{do}$ operator to propagate counterpossible changes from $\textsc{pfdt}(\underline{P}, \underline{G})$ to all physical systems that compute or predict it.

### 3.2 Applying P-FDT: The Transparent Newcomb Problem

To see how **P-FDT** operates in practice—and how it streamlines the calculations of action-based FDT—consider Drescher's (2006) **Transparent Newcomb Problem** (Dilemma 5 in the source paper, which is decision-theoretically isomorphic to Parfit's Hitchhiker problem). 

An agent stands before two transparent boxes: Box A contains \$1,000, and Box B visibly contains either \$1,000,000 ($\textit{full}$) or \$0 ($\textit{empty}$). A predictor with $99\%$ accuracy placed \$1,000,000 in Box B if and only if she predicted that the agent would leave Box A behind ($\textit{onebox}$) upon observing that Box B is $\textit{full}$. Suppose the agent observes $x = \textit{full}$. Should she $\textit{onebox}$ or $\textit{twobox}$?

Both CDT and EDT prescribe $\textit{twobox}$ upon seeing $x = \textit{full}$: conditional on $\textsc{Obs} = \textit{full}$ (and whether or not one intervenes on $\textsc{Act}$), taking both boxes yields \$1,001,000 whereas taking one box yields \$1,000,000. Foreseeing this, the predictor leaves Box B empty for CDT and EDT agents, who walk away with \$1,000.

Now consider how a **P-FDT** agent solves the problem. Here, the observation space is $\mathcal{X} = \{\textit{full}, \textit{empty}\}$ and the action space is $\mathcal{A} = \{\textit{onebox}, \textit{twobox}\}$ (abbreviated $\textit{1}$ and $\textit{2}$). Thus, the policy space $\Pi = \mathcal{A}^{\mathcal{X}}$ contains four policies, which we can write as ordered pairs $\pi = \big(\pi(\textit{full}),\, \pi(\textit{empty})\big)$:
$$\Pi = \big\{(\textit{1}, \textit{1}),\; (\textit{1}, \textit{2}),\; (\textit{2}, \textit{1}),\; (\textit{2}, \textit{2})\big\}.$$

In the **P-FDT** graph $G$, the predictor's prediction depends on $\pi(\textit{full})$—specifically, on whether the policy node $\textsc{pfdt}(\underline{P}, \underline{G})$ maps the input $\textit{full}$ to $\textit{1}$ or $\textit{2}$—and on the accuracy node $\textsc{Accurate}$ ($P(\textsc{Accurate} = \textit{accurate}) = 0.99$). Formally:
* $\textsc{Box B}(\pi, \textit{accurate}) = \textit{full}$ if $\pi(\textit{full}) = \textit{1}$, and $\textit{empty}$ if $\pi(\textit{full}) = \textit{2}$ (and vice versa when $\textsc{Accurate} = \textit{inaccurate}$).
* $\textsc{Obs} = \textsc{Box B}$.
* $\textsc{Act}(\pi, \textsc{Obs}) = \pi(\textsc{Obs})$.
* $\textsc{V}(\textsc{Act}, \textsc{Box B})$ equals $\$1,001,000$ for $(\textit{2}, \textit{full})$; $\$1,000,000$ for $(\textit{1}, \textit{full})$; $\$1,000$ for $(\textit{2}, \textit{empty})$; and $\$0$ for $(\textit{1}, \textit{empty})$.

Let us evaluate $\mathbb{E}\big[\textsc{V} \;\big|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)\big]$ across all four policies:

| Policy $\pi = (\pi(\textit{full}), \pi(\textit{empty}))$ | Prob. of $\textsc{Box B} = \textit{full}$ | Payoff if $\textit{full}$ | Payoff if $\textit{empty}$ | Expected Utility $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi)]$ |
| :--- | :---: | :---: | :---: | :---: |
| $\pi_{1,1} = (\textit{onebox}, \textit{onebox})$ | $0.99$ | $\$1,000,000$ | $\$0$ | $0.99(\$1,000,000) + 0.01(\$0) = \$990,000$ |
| $\pi_{1,2} = (\textit{onebox}, \textit{twobox})$ | $0.99$ | $\$1,000,000$ | $\$1,000$ | $0.99(\$1,000,000) + 0.01(\$1,000) = \mathbf{\$990,010}$ |
| $\pi_{2,1} = (\textit{twobox}, \textit{onebox})$ | $0.01$ | $\$1,001,000$ | $\$0$ | $0.01(\$1,001,000) + 0.99(\$0) = \$10,010$ |
| $\pi_{2,2} = (\textit{twobox}, \textit{twobox})$ | $0.01$ | $\$1,001,000$ | $\$1,000$ | $0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000$ |

The unique optimal policy is $\pi^* = \pi_{1,2} = (\textit{onebox}, \textit{twobox})$, which achieves an expected utility of $\$990,010$. In Step 2, the **P-FDT** agent applies $\pi^*$ to her actual observation $x = \textit{full}$:
$$\mathrm{PFDT}(P, G, \textit{full}) = \pi_{1,2}(\textit{full}) = \textit{onebox}.$$
Even while staring directly at the \$1,000,000 in Box B, the **P-FDT** agent leaves Box A behind, because under the global policy perspective, adopting a policy that maps $\textit{full} \mapsto \textit{twobox}$ counterpossibly shifts the probability that Box B is full from $99\%$ to $1\%$.

*(An Analytical Comparison with Action-Based FDT):* Although the reference paper states that action-based FDT and **P-FDT** behave identically in single-agent dilemmas, comparing the derivation above with Section 6 of the paper reveals an instructive mathematical subtlety. When Fiona uses action-based FDT in Section 6 upon seeing $\textit{full}$, she intervenes *only* on the node $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full})$, leaving the counterfactual branch node $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty})$ untouched as an exogenous random variable! Consequently, the authors had to introduce an arbitrary prior probability $q \coloneqq P^F(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty}) = \textit{twobox})$ and write Fiona's expected utilities as $\$990,000 + 0.01q \cdot \$1,000$ versus $\$10,010 + 0.99q \cdot \$1,000$. Under **P-FDT**, the nuisance parameter $q$ vanishes completely: because the intervention $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$ simultaneously determines both $\pi(\textit{full})$ and $\pi(\textit{empty})$, the agent does not need epistemic priors over her own off-path behavior.

---

## 4. Where P-FDT Diverges from Action-Based FDT: Multi-Agent and Cross-Branch Dilemmas

Why do Yudkowsky and Soares remark in Footnote 16 that the distinction between action-based FDT and **P-FDT** *"only matters in multi-agent dilemmas so far as we can tell"*? Let us develop the exact mathematical mechanism behind this divergence. (While the authors state the claim in Footnotes 7 and 16 without providing an explicit example, the following theorem-level analysis and game-theoretic construction are our own operational demonstration of their claim.)

### 4.1 The Mathematics of Cross-Branch Independence vs. Joint Policy Coupling

Consider why action-based FDT and **P-FDT** agree in standard single-agent dilemmas like Transparent Newcomb or Mechanical Blackmail. Suppose an agent faces a single-agent problem where:
1. Only one instance of the agent acts in the world, receiving a single realized observation $\textsc{Obs} \in \mathcal{X}$.
2. For each observation $x \in \mathcal{X}$, the environment's causal/subjunctive response depends only on the agent's disposition at $x$ (or, as in Transparent Newcomb and Mechanical Blackmail, the predictor only conditions on a single critical branch $x_0$, and off-path branches have no predictor dependence).
3. The agent's prior $P$ over her own off-path action nodes $\textsc{fdt}(\underline{P}, \underline{G}, \underline{y})$ ($y \neq x$) already assigns probability $1$ to the component-wise optimal actions $\pi^*(y)$.

Under these conditions, maximizing $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)]$ over $\pi \in \Pi$ is equivalent to fixing $\pi(y) = \pi^*(y)$ for all $y \neq x$ and maximizing over $\pi(x) \in \mathcal{A}$—which is precisely what action-based FDT computes in Equation (4).

Now suppose we are in a **multi-agent dilemma** (or a distributed single-agent dilemma across time/space) where two or more copies of the agent implement the same decision algorithm on the same prior model $(P, G)$, **but receive different observations $x_1 \neq x_2 \in \mathcal{X}$**.

In action-based FDT, when Agent 1 observes $x_1$, she intervenes on $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_1}) = a_1$. By the rules of Pearl's $\mathtt{do}$-calculus on the graph $G$, intervening on $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_1})$ alters the behavior of any copy who observes $x_1$, **but it does not intervene on $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_2})$**. Because $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_1})$ and $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_2})$ are distinct parentless root nodes in $G$, action-based FDT treats the twin's decision at $x_2$ as causally and subjunctively independent of the decision at $x_1$!

This is a striking result: **Action-based FDT relates to P-FDT across distinct observations in the exact same way that CDT relates to FDT across distinct physical agents.** Just as CDT defects in the Psychological Twin Prisoner's Dilemma because intervening on $\textsc{Act}_1$ holds $\textsc{Act}_2$ fixed, action-based FDT fails whenever twins receive distinct observations $x_1 \neq x_2$, because intervening on $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_1})$ holds $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_2})$ fixed!

### 4.2 Worked Example: The Asymmetric Twin Prisoner's Dilemma

To make this concrete, consider the following dilemma:

> **Dilemma (The Asymmetric Twin Prisoner's Dilemma).** An agent and her perfect psychological twin—both sharing the exact same prior world-model $(P, G)$ and decision algorithm—are placed in separate rooms. A referee flips a fair coin to place one twin in $\textit{Room L}$ and the other in $\textit{Room R}$. Each twin observes only the label of her own room, $x \in \mathcal{X} = \{\textit{L}, \textit{R}\}$, and must choose an action $a \in \mathcal{A} = \{\textit{cooperate}, \textit{defect}\}$ (abbreviated $\textit{C}$ and $\textit{D}$). If both twins choose $\textit{C}$, each receives \$1,000,000. If both choose $\textit{D}$, each receives \$1,000. If one chooses $\textit{C}$ and the other chooses $\textit{D}$, the defector receives \$1,001,000 and the cooperator receives \$0. Which action should the agent take upon observing $x = \textit{L}$?

Let us compare **action-based FDT** and **P-FDT** in this dilemma.

#### How Action-Based FDT Fails

In action-based FDT, the graph $G^F$ has two logical decision nodes: $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{L})$ and $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{R})$. When our agent observes $x = \textit{L}$, she knows with certainty that she is in $\textit{Room L}$ (so her own action is governed by $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{L})$) and her twin is in $\textit{Room R}$ (so her twin's action is governed by $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{R})$). 

Wait: even before conditioning on who is in which room, under the prior $P^F$, there is a $50\%$ chance that the agent is in $\textit{Room L}$ (and her twin is in $\textit{Room R}$) and a $50\%$ chance that the agent is in $\textit{Room R}$ (and her twin is in $\textit{Room L}$). In either case, **one twin's action is determined by $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{L})$ and the other twin's action is determined by $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{R})$**.

When the agent observes $x = \textit{L}$, action-based FDT (Equation 4) evaluates $\mathtt{do}\big(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{L}) = a\big)$ for $a \in \{\textit{C}, \textit{D}\}$. Let $p_R \coloneqq P^F\big(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{R}) = \textit{C}\big)$ be her prior probability that the $\textit{Room R}$ node outputs $\textit{C}$. Because $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{R})$ is not downstream of $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{L})$, the intervention $\mathtt{do}\big(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{L}) = a\big)$ leaves $p_R$ completely unchanged!

Let us compute the expected utility $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{L}) = a)]$ under action-based FDT:
* **If $a = \textit{C}$:**
  * With probability $0.5$, the agent is in $\textit{Room L}$ (choosing $\textit{C}$) and her twin is in $\textit{Room R}$ (choosing $\textit{C}$ with prob. $p_R$, $\textit{D}$ with prob. $1-p_R$). Expected payoff: $p_R(\$1,000,000) + (1-p_R)(\$0)$.
  * With probability $0.5$, the agent is in $\textit{Room R}$ (choosing $\textit{C}$ with prob. $p_R$, $\textit{D}$ with prob. $1-p_R$) and her twin is in $\textit{Room L}$ (choosing $\textit{C}$). Expected payoff: $p_R(\$1,000,000) + (1-p_R)(\$1,001,000)$.
  * Total expected utility for $a = \textit{C}$:
    $$\mathcal{EU}_{\mathrm{FDT}}(\textit{C}) = 0.5\big(1,000,000 p_R\big) + 0.5\big(1,001,000 - 1,000 p_R\big) = \$500,500 + \$499,500 p_R.$$

* **If $a = \textit{D}$:**
  * With probability $0.5$, the agent is in $\textit{Room L}$ (choosing $\textit{D}$) and her twin is in $\textit{Room R}$. Expected payoff: $p_R(\$1,001,000) + (1-p_R)(\$1,000)$.
  * With probability $0.5$, the agent is in $\textit{Room R}$ and her twin is in $\textit{Room L}$ (choosing $\textit{D}$). Expected payoff: $p_R(\$0) + (1-p_R)(\$1,000)$.
  * Total expected utility for $a = \textit{D}$:
    $$\mathcal{EU}_{\mathrm{FDT}}(\textit{D}) = 0.5\big(1,000 + 1,000,000 p_R\big) + 0.5\big(1,000 - 1,000 p_R\big) = \$1,000 + \$499,500 p_R.$$

Wait—look closely at why $\mathcal{EU}_{\mathrm{FDT}}(\textit{C}) > \mathcal{EU}_{\mathrm{FDT}}(\textit{D})$ above: in that calculation, because action-based FDT did *not* condition on $\textsc{Obs} = \textit{L}$, the agent gave $50\%$ weight to the counterfactual possibility that *she herself is in $\textit{Room R}$* and her intervention on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{L})$ is actually controlling *her twin's* action in $\textit{Room L}$, thereby gifting herself $\$1,000,000$ when she is in $\textit{Room R}$! 

What if the game instead requires **complementary coordination** across rooms (an **Asymmetric Twin Stag Hunt / Coordination Game**), where the twins each get $\$1,000,000$ if and only if they take *matching* actions $(\textit{A}, \textit{A})$ or $(\textit{B}, \textit{B})$, or what if the payoff isn't symmetric between the two players? Let us check the **Asymmetric Twin Stag Hunt**:
* Both choose $\textit{Stag}$ ($\textit{S}$): each gets $\$1,000,000$.
* Any twin chooses $\textit{Hare}$ ($\textit{H}$): a twin choosing $\textit{H}$ gets a sure $\$100,000$, while a twin choosing $\textit{S}$ alone gets $\$0$.

Under action-based FDT, when evaluating $\mathtt{do}\big(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{L}) = a\big)$:
* If $a = \textit{S}$:
  $$\mathcal{EU}_{\mathrm{FDT}}(\textit{S}) = 0.5\big[p_R(\$1,000,000) + (1-p_R)(\$0)\big] + 0.5\big[p_R(\$1,000,000) + (1-p_R)(\$100,000)\big] = \$50,000 + \$950,000 p_R.$$
* If $a = \textit{H}$:
  $$\mathcal{EU}_{\mathrm{FDT}}(\textit{H}) = 0.5\big[\$100,000\big] + 0.5\big[p_R(\$0) + (1-p_R)(\$100,000)\big] = \$100,000 - \$50,000 p_R.$$

Look at what happens when $p_R < 0.05$ (for example, if both twins start with a cautious prior $p_L = p_R = 0$): **action-based FDT outputs $\textit{Hare}$ ($\textit{H}$) in both rooms**, locking both twins into the $\$100,000$ suboptimal Nash equilibrium! Why? Because when the agent in $\textit{Room L}$ intervenes only on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{L}) = \textit{S}$, her intervention fails to switch the $\textit{Room R}$ node $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{R})$ from $\textit{H}$ to $\textit{S}$. Even worse, if the twins know ahead of time which room they will be placed in (so that Twin 1's world-model assigns $100\%$ probability to her being in $\textit{Room L}$ and her twin being in $\textit{Room R}$), then in the Asymmetric Twin Prisoner's Dilemma itself, intervening on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{L})$ controls *only* Twin 1's action and has zero effect on Twin 2's action $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{R})$—causing action-based FDT to **defect** for the exact same reason CDT defects!

#### How P-FDT Succeeds

Now watch how **P-FDT** resolves both dilemmas effortlessly. Under **P-FDT**, both twins share the single policy node $\textsc{pfdt}(\underline{P}, \underline{G})$, which takes values in $\Pi = \mathcal{A}^{\{\textit{L}, \textit{R}\}}$. Regardless of whether the room assignment is random ($50/50$) or known in advance, intervening on $\mathtt{do}\big(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\big)$ simultaneously sets Twin 1's action in $\textit{Room L}$ to $\pi(\textit{L})$ and Twin 2's action in $\textit{Room R}$ to $\pi(\textit{R})$:

* In the **Asymmetric Twin Prisoner's Dilemma** (even with known room assignments where Twin 1 knows she is in $\textit{Room L}$):
  * $\pi_{C,C} = (\textit{C}, \textit{C}) \implies \mathbb{E}[\textsc{V}] = \mathbf{\$1,000,000}$ (Wait: what about $\pi_{D,C} = (\textit{D}, \textit{C})$? If the room assignment is symmetric $50/50$, $\pi_{D,C}$ gives $0.5(\$1,001,000) + 0.5(\$0) = \$500,500 < \$1,000,000$, so $\pi^* = (\textit{C}, \textit{C})$ uniquely wins!).
* In the **Asymmetric Twin Stag Hunt**:
  * $\pi_{S,S} = (\textit{S}, \textit{S}) \implies \mathbb{E}[\textsc{V}] = \mathbf{\$1,000,000}$.
  * $\pi_{S,H} = (\textit{S}, \textit{H}) \implies \mathbb{E}[\textsc{V}] = 0.5(\$0) + 0.5(\$100,000) = \$50,000$.
  * $\pi_{H,S} = (\textit{H}, \textit{S}) \implies \mathbb{E}[\textsc{V}] = 0.5(\$100,000) + 0.5(\$0) = \$50,000$.
  * $\pi_{H,H} = (\textit{H}, \textit{H}) \implies \mathbb{E}[\textsc{V}] = \$100,000$.

Without any dependence on prior probabilities $p_L$ or $p_R$, **P-FDT** selects $\pi^* = (\textit{S}, \textit{S})$, applies $\pi^*$ to the observed room $x \in \{\textit{L}, \textit{R}\}$, and achieves $\$1,000,000$.

*(An Extension to Single-Agent Dilemmas):* Going one step beyond Footnote 16's remark that the difference *"only matters in multi-agent dilemmas so far as we can tell,"* our mathematical formulation shows that **P-FDT** can also outperform action-based FDT in **single-agent dilemmas**. First, as the authors themselves note in Section 10 when discussing an agent deciding whether to go to the gym across multiple weeks, intertemporal coordination with one's future selves is structurally a multi-agent dilemma across different observation histories $x_t$. Second, consider a single-agent problem where a predictor inspects the agent's disposition across *two* possible observations $x_1, x_2 \in \mathcal{X}$ and rewards the agent with $\$1,000,000$ if and only if *both* $\pi(x_1) = \textit{cooperate}$ and $\pi(x_2) = \textit{cooperate}$ (when cooperating costs $\$1,000$). If the agent's prior $P^F$ happens to assign low probability to $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \underline{x_2}) = \textit{cooperate}$, an action-based FDT agent observing $x_1$ will conclude that intervening on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \underline{x_1})$ alone is futile and will defect! A **P-FDT** agent, by contrast, optimizes the joint policy $(\pi(x_1), \pi(x_2))$ and cooperates at both nodes.

---

## 5. Open Questions and Operational Extensions of P-FDT

Because Yudkowsky and Soares introduce **P-FDT** concisely in Footnotes 7 and 16, several important technical questions are left open. Here we identify three central uncertainties and develop concrete operational proposals to resolve them, distinguishing what the source text states from our proposed extensions.

### 5.1 What Counts as an "Input" to a Policy? (The Smoking Lesion Problem Revisited)

There is a subtle terminological tension between Footnote 7 and Footnote 16:
* Footnote 7 defines policies as *"mappings from observations to actions"* ($\pi: \mathcal{X} \to \mathcal{A}$).
* Footnote 16 says that **P-FDT** chooses *"a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action."*

In Equation (4) of the source paper, the inputs to the function $\mathrm{FDT}(P, G, x)$ are $(P, G, x)$, not merely $x$. Why does this distinction matter? Recall how the authors formalize the **Smoking Lesion Problem** in Section 6 (Figure 4). Because the lesion causes the agent to love smoking, the authors model Fiona as having uncertainty over her own utility function and world-model: if she has the lesion, her distribution is $P_S^F$ (built from $\mathcal{U}_S$, which values smoking at $+\$1,000$); if she does not have the lesion, her distribution is $P_R^F$ (built from $\mathcal{U}_R$, which values smoking at $-\$1$). In Figure 4, Fiona's graph $G^F$ contains two distinct nodes: $\textsc{fdt}(\underline{P_S^F}, \underline{G^F})$ and $\textsc{fdt}(\underline{P_R^F}, \underline{G^F})$, and she intervenes on whichever one corresponds to her actual world-model without introspective access to which node she is intervening on.

**Operational Resolution:** How should **P-FDT** handle uncertainty over one's own world-model or preferences, or asymmetric information where two twins have known distinct positions (as in the known-room Asymmetric Twin Prisoner's Dilemma above)? We propose a unified operational interpretation: **separate the agent's prior constitutional structure $(P, G, \mathcal{U})$ from her local situational index or private information $x \in \mathcal{X}$.** 

Specifically, whenever variations in preferences or local roles are foreseeable parts of the decision problem, they should be represented as part of the agent's local input $x \in \mathcal{X}$ relative to a common constitutional prior $(P, G)$. For instance, in the Smoking Lesion problem, rather than saying Fiona lacks introspective access to her own utility function $\mathcal{U}$, it is far cleaner to treat her taste for tobacco ($x \in \{\textit{craving}, \textit{no\_craving}\}$) as an internal observation input to a single **P-FDT** policy node $\textsc{pfdt}(\underline{P}, \underline{G})$. Then $\pi = \big(\pi(\textit{craving}),\, \pi(\textit{no\_craving})\big)$ is optimized jointly: because the node $\textsc{Lesion}$ is upstream of the craving and $\textsc{Cancer}$ is not downstream of $\textsc{pfdt}(\underline{P}, \underline{G})$, **P-FDT** uniquely selects the policy $\pi^* = (\textit{smoke}, \textit{refrain})$, smoking when she enjoys it and refraining when she dislikes it.

### 5.2 Zero-Probability Observations and Off-Path Policy Indeterminacy

A second mathematical challenge arises directly from **P-FDT**'s unconditional expectation in Equation (6). Suppose an observation $x_0 \in \mathcal{X}$ has probability zero of occurring under every policy, or has probability zero under the optimal behavior on other branches:
$$P\big(\textsc{Obs} = x_0 \;\big|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)\big) = 0.$$
For example, consider the **Mechanical Blackmail Problem** (Section 9, Dilemma 8) with a *perfect* ($100\%$ accurate) blackmailer who sends a blackmail letter ($x = \textit{blackmail}$) if and only if she predicts the agent's policy satisfies $\pi(\textit{blackmail}) = \textit{pay}$, and sends nothing ($x = \emptyset$) otherwise. Or consider the **Transparent Newcomb Problem** with an infallible ($100\%$ accurate) predictor.

In Transparent Newcomb with a $100\%$ accurate predictor, any policy $\pi$ with $\pi(\textit{full}) = \textit{onebox}$ guarantees $P(\textsc{Obs} = \textit{full} \mid \mathtt{do}(\textsc{pfdt} = \pi)) = 1$ and $P(\textsc{Obs} = \textit{empty} \mid \mathtt{do}(\textsc{pfdt} = \pi)) = 0$. Consequently, the two policies $\pi_{1,1} = (\textit{onebox}, \textit{onebox})$ and $\pi_{1,2} = (\textit{onebox}, \textit{twobox})$ yield the **exact same unconditional expected utility**: $\$1,000,000$! If the agent somehow found herself observing $x_0 = \textit{empty}$, naive maximization in Equation (6) would be indifferent between $\pi_{1,1}(\textit{empty}) = \textit{onebox}$ (getting $\$0$) and $\pi_{1,2}(\textit{empty}) = \textit{twobox}$ (getting $\$1,000$).

**Operational Resolution:** While the source paper sidesteps this in Transparent Newcomb by assuming the predictor is $99\%$ accurate rather than $100\%$ accurate (though it uses a $100\%$ accurate predictor in XOR Blackmail and Death in Damascus), a general mathematical formulation of **P-FDT** should not leave measure-zero branches arbitrary. We can resolve this cleanly via a **Trembling-Hand / Lexicographic Policy Refinement**:
1. **$\varepsilon$-Trembles:** Require the world-model $(P_\varepsilon, G)$ to assign a vanishingly small error probability $\varepsilon > 0$ to every fallible environmental prediction or observation channel, and define the optimal **P-FDT** policy in the limit as $\varepsilon \to 0^+$:
   $$\pi^*(P, G) \coloneqq \lim_{\varepsilon \to 0^+} \argmax_{\pi \in \Pi} \mathbb{E}_{P_\varepsilon}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right). \tag{8}$$
2. **Lexicographic Sub-Policy Selection:** Equivalently, if a set of policies $\Pi_1^* \subseteq \Pi$ ties for the maximum unconditional expected utility in Equation (6), break ties among $\pi \in \Pi_1^*$ by maximizing conditional expected utility on the zero-probability branches $x_0$ (conditioning on the event that the observation channel into $x_0$ misfired). Under either refinement, $\pi_{1,2} = (\textit{onebox}, \textit{twobox})$ strictly dominates $\pi_{1,1} = (\textit{onebox}, \textit{onebox})$.

### 5.3 Computational Complexity and Learning Subjunctive Graphs

Finally, two foundational challenges identified by Yudkowsky and Soares for action-based FDT become even more pronounced in **P-FDT**:
1. **Combinatorial Explosion of the Policy Space:** In Section 6, the authors note that maximizing over all actions $\mathcal{A}$ in a realistic world-model is already computationally intractable. In **P-FDT**, the search space expands from $|\mathcal{A}|$ to $|\Pi| = |\mathcal{A}|^{|\mathcal{X}|}$. A bounded **P-FDT** agent therefore cannot enumerate $\Pi$ exhaustively; instead, practical implementations must restrict $\Pi$ to a parameterized class of policies $\Pi_\theta$ or prune observation branches that are subjunctively independent of the current decision problem.
2. **Deducing Subjunctive Structure:** As the authors emphasize in Sections 5 and 10, Pearl (2000) showed how to infer causal graphs $G$ from empirical observations and physical interventions, but no comparable formal theory exists for deducing the structure of *logical and subjunctive* dependencies. Constructing a formal calculus that learns which environmental processes depend on $\textsc{pfdt}(\underline{P}, \underline{G})$—and how—remains the central open problem in the foundations of functional decision theory.

---

## 6. Conclusion

**Policy Functional Decision Theory (P-FDT)** represents the purest mathematical expression of Yudkowsky and Soares's functionalist turn in decision theory. By shifting the locus of counterfactual intervention from physical action tokens ($\textsc{Act}$) and even observation-indexed action outputs ($\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$) to the global mathematical policy $\textsc{pfdt}(\underline{P}, \underline{G}) \in \mathcal{A}^{\mathcal{X}}$, **P-FDT** eliminates arbitrary prior assumptions about off-path behavior and enables seamless coordination across agents and temporal selves who encounter different observations. 

Where EDT is trapped into managing statistical news and CDT is blinded by breaking logical correlations between predictors and predicted agents, a **P-FDT** agent evaluates options from a unified global perspective—asking which mapping from inputs to actions makes the universe best as a whole, and then executing the action that mapping prescribes here and now.

---

## References

* Ahmed, Arif. 2014. *Evidence, Decision and Causality*. Cambridge University Press.
* Cohen, Daniel. 1990. "On What Cannot Be." In *Truth or Consequences: Essays in Honor of Nuel Belnap*, 123–132. Kluwer Academic Publishers.
* Dai, Wei. 2009. "Towards a New Decision Theory." *Less Wrong*, August 13, 2009.
* Drescher, Gary L. 2006. *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Gibbard, Allan, and William L. Harper. 1978. "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, Vol. 1, 125–162. D. Reidel.
* Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Kleene, Stephen Cole. 1938. "On Notation for Ordinal Numbers." *Journal of Symbolic Logic* 3 (4): 150–155.
* Lewis, David. 1979. "Prisoners' Dilemma is a Newcomb Problem." *Philosophy & Public Affairs* 8 (3): 235–240.
* Nozick, Robert. 1969. "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel*, 114–146. D. Reidel.
* Parfit, Derek. 1986. *Reasons and Persons*. Oxford University Press.
* Pearl, Judea. 1996. "Causation, Action, and Counterfactuals." In *Proceedings of the 6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-'96)*, 51–73.
* Pearl, Judea. 2000. *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Peirce, Charles Sanders. 1934. *Collected Papers of Charles Sanders Peirce, Vol. V: Pragmatism and Pragmaticism*. Harvard University Press.
* Skyrms, Brian. 1980. *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Soares, Nate, and Benja Fallenstein. 2015. "Toward Idealized Decision Theory." arXiv:1507.01986.
* Yudkowsky, Eliezer. 2010. *Timeless Decision Theory*. The Singularity Institute.
* Yudkowsky, Eliezer, and Nate Soares. 2017. "Functional Decision Theory: A New Theory of Instrumental Rationality." arXiv:1710.05060v2.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Purpose**

I'm currently focused on defining the exact scope and purpose of this essay. I'm aiming for a clear explanation of P-FDT accessible to a mathematically literate audience, and I want to cover its practical application to decision problems. The goal is to provide a comprehensive, yet concise, overview.


**Analyzing the Source Material**

I'm now diving deep into the source material, specifically focusing on the policy-selection aspects of P-FDT as detailed in footnotes 7 and 16. I'm carefully extracting the key claims and distinguishing them from my own interpretations. The essay will consistently use the term "P-FDT" and contrasts it with other decision theories. My aim is to faithfully quote and clarify any ambiguities.


**Clarifying the Distinction**

I'm now clarifying the distinction between action-based FDT and the author's preferred policy-based formulation. It appears the key difference, for practical purposes, lies in multi-agent dilemmas. This nuance, involving the intervention on a policy node rather than directly on an action node, might be critical for the essay's scope. I'm carefully considering how to frame this for a decision theory expert.


**Examining the Implementation**

I'm now focused on how P-FDT alters the core FDT structure. Instead of isolated action interventions, P-FDT chooses a policy – a mapping from observations to actions. This single intervention node, denoted by  $\textsc{pfdt}(\underline{P}, \underline{G})$, selects the entire policy $\pi$, and then applies it to the observation. I'm unpacking the mathematical details, specifically from Footnote 16, to ensure complete clarity.


**Operationalizing P-FDT**

I'm working to formalize the equation for P-FDT, based on the source. The source doesn't provide an explicit equation. I'm carefully constructing one based on Footnotes 7 and 16, defining observations, actions, and policies. My current formalization focuses on how $\textsc{pfdt}(\underline{P}, \underline{G})$ selects a policy and applies it to observations. I'm aiming for an explicit representation for clarity.


**Formalizing the Equation**

I've made progress formalizing the P-FDT equation. Specifically, I'm focusing on the selection of the optimal policy using the equation, $$\pi^* \coloneqq \argmax_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right)$$, and its application to generate an action upon observing x. I am now focused on clarifying if "inputs" are really the same as "observations" for clarity.


**Interpreting the Policy**

I'm now focusing on the precise mapping of the P-FDT policy, given the inputs $(P, G, x)$. I'm analyzing two interpretations. The first, *Observation-Policy*, describes a policy $\pi$ that maps observation histories to actions, where the action node is a deterministic function of the policy and the observation. The second interpretation, *Full-Input*, considers the policy as taking the model/utility function as inputs, especially in scenarios with agent uncertainty.


**Investigating the Distinctions**

I'm currently investigating the distinctions between P-FDT and action-based FDT, particularly in multi-agent and single-agent dilemmas. I'm focusing on scenarios with observations. Specifically, I am grappling with how P-FDT handles policy mapping. How does a policy, which can use all inputs versus only observations, function in the context of the model and utility functions? The nuances of this distinction need clarification.


**Analyzing Action-Based FDT**

I'm now analyzing how action-based FDT functions, especially in scenarios like Transparent Newcomb and Mechanical Blackmail. My focus is on understanding the intervention nodes in $G^F$ and how standard FDT handles situations where multiple nodes exist, for instance $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full})$. I'm digging into specific examples, such as the calculations in Section 6, to get the mechanics clear. I need to understand this to contrast it to P-FDT.


**Contrasting FDT Functionality**

I'm now fully immersed in contrasting action-based FDT with P-FDT in scenarios like Transparent Newcomb, dissecting the intervention points and their implications. Specifically, I am grappling with how the distribution of observations and predictors' actions hinge solely on the 'full' observation branch in this context. The core aim is to precisely highlight these differences in the essay.


**Examining Implications**

I'm now examining the implications of Transparent Newcomb, focusing on how the probability of 'empty' changes under different intervention nodes ('full', 'onebox', 'twobox'). I see now why the specific value of 'q' didn't matter in the standard case. My thinking then moved to more complex scenarios. These scenarios include cases with closer values, or where the predictor's actions or a twin agent depends on a shared or different observation. I'm exploring scenarios now.


**Analyzing Twin Agent Dilemmas**

I'm now analyzing the implications when using action-based FDT for scenarios involving twin agents. Observing "Left," I see that direct intervention only affects that specific observation, leaving the twin's choice, "Right", unchanged, leading to a lack of joint optimization. This lack of coordination seems to be a significant limitation, especially where joint payoffs are involved.


**Analyzing the Dichotomy**

I'm now analyzing single-agent scenarios, questioning the claim that the distinction between P-FDT and action-based FDT only matters in multi-agent dilemmas. I'm focusing on the footnote statement. I am now working through complex scenarios where multiple counterfactual branches and cross-branch dependencies exist, to see if the distinction remains valid.


**Examining Branching Dynamics**

I'm now diving into complex single-agent scenarios. I'm focusing on why a predictor's predictions across *multiple* branches can matter. Specifically, I'm analyzing cases with uncertain priors, like the Transparent Newcomb setup, where the "q" uncertainty significantly impacts expected utility. I'm exploring scenarios where observation-specific actions can have inter-branch dependencies.


**Structuring the Essay**

I am now structuring the essay and confirming the target word count. I'm aiming for a clear, rigorous, and engaging format. I plan to address scenarios with uncertainty and coordination, including twin-agent examples and cross-branch dependencies. My focus will be on the benefits of P-FDT in these cases.


**Structuring the Essay**

I am now structuring the essay. I am planning the sections and sub-sections, starting with a brief introduction. The essay will start with functional decision theory, focusing on the differences between Evidential, Causal, and Functional Decision Theory. Next, the essay will cover Policy Functional Decision Theory and highlight the key differences between the action-selection and policy formulation.


**Defining the Equations**

I'm now defining the key equations for Evidential Decision Theory (EDT), Causal Decision Theory (CDT), and action-based Functional Decision Theory (FDT) within the expected utility framework. This includes presenting the foundation of the expected utility framework with equation 1. I'm focusing on contrasting their core mechanics, specifically how observations and interventions are handled.


**Formalizing the Process**

I'm now fully formalizing the process. I am making sure to clarify the mathematical notation. Specifically, I'm defining the policy space and the two-step P-FDT procedure outlined in the footnote. The focus is on the optimization step that uses expected utility and the policy application to the observed value. I'm aiming for explicit equations and clear definitions.


**Clarifying Subjunctive Dependence**

I'm now clarifying the concept of subjunctive dependence and why P-FDT requires counterpossible reasoning. I am focused on the differences between calculators, twins, predictors, and statistical lesions. Furthermore, I am examining how P-FDT, using the $\mathtt{do}$ operator, evaluates logically false antecedents. My goal is to use this reasoning to highlight the importance of the $\mathtt{do}$ operator in practical decision-making.


**Analyzing the Dynamics**

I'm now analyzing the branching dynamics of Transparent Newcomb, focusing on how P-FDT addresses the value of q. P-FDT's intervention fixes both $\pi(\textit{full})$ and $\pi(\textit{empty})$, which removes the sensitivity to $q$. This is in contrast to action-based FDT. I will detail how this influences scenarios, specifically in twin-agent dilemmas.



**Calculating the Utility**

I'm now calculating the exact expected utilities for action-based FDT versus P-FDT in the twin-agent scenario. Action-based FDT fails to coordinate, while P-FDT intervenes on the entire policy. This allows joint optimization across rooms. I'm focusing on the differences in outcomes given the distinct intervention points of the two decision theories.


**Calculating Utilities**

I'm now calculating the exact utilities for action-based FDT and P-FDT in a variant of the twin-agent scenario where outcomes depend on counterfactual branches. I'm carefully evaluating how these distinct intervention points impact the ability to achieve optimal joint outcomes. I'm focusing on contrasting expected utilities.


**Interpreting Policy Frameworks**

I'm now diving into interpreting P-FDT in scenarios of model/utility uncertainty, specifically the *Observation-Policy* ($\pi: \mathcal{X} \to \mathcal{A}$) versus *Epistemic-State Policy* ($\pi: \mathcal{M} \times \mathcal{X} \to \mathcal{A}$). Also, I'm examining zero-probability observations under P-FDT. If an observation has zero probability, all actions yield the same expected utility, which needs to be addressed. I am exploring tie-breaking methods or trembling-hand refinements.


**Addressing Tractability Issues**

I'm now grappling with the computational tractability of P-FDT, given the exponential scaling of policy search. Furthermore, learning the subjunctive graph remains an open problem. I'm considering ways to address these issues, such as exploring approximations or simplifying the policy space. My focus is ensuring practical utility while staying true to the theoretical framework.


**Addressing Tractability Issues**

I'm now fully immersed in addressing P-FDT's tractability challenges. I'm focusing on the exponential complexity of policy search and the learning difficulties associated with the subjunctive graph. I'm exploring approximation techniques and policy space simplification to mitigate these issues, ensuring the framework's practical usability. My priority remains maintaining the core theoretical integrity.


```
