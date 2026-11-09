# 021_fdt_eq4_google_gemini-4-argon_rhigh_phigh / 00019

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/c46c21bc-b88f-4058-acda-ec97f1e14b25/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/c46c21bc-b88f-4058-acda-ec97f1e14b25/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Action Functional Decision Theory (A-FDT): Formal Mechanics, Subjunctive Counterfactuals, and Operational Application

Suppose you face a decision problem in which an external process—a game-theoretic counterpart, an algorithmic auditor, or a psychological twin—accurately predicts your behavior before your physical action takes place. How should an instrumentally rational agent evaluate candidate actions in such an environment? 

For decades, normative decision theory was split between two answers: **Evidential Decision Theory (EDT)** and **Causal Decision Theory (CDT)**. Measured by average utility achieved across classic dilemmas, neither theory dominates the other: EDT outperforms CDT in Newcomb's problem, while CDT outperforms EDT in the smoking lesion problem (Gibbard and Harper 1978; Skyrms 1980). Worse still, in sequential prediction dilemmas such as Parfit's hitchhiker (Parfit 1986) or the transparent Newcomb problem (Drescher 2006), both CDT and EDT leave the agent poor—or dead in the desert.

In *Functional Decision Theory: A New Theory of Instrumental Rationality*, Eliezer Yudkowsky and Nate Soares (2017) propose a third paradigm. Rather than asking which physical act causes the best outcome (CDT) or which physical act provides the best news (EDT), a functional decision theorist treats her decision as the output of a fixed mathematical function and asks: *"Which output of this very function would yield the best outcome?"*

While Yudkowsky and Soares note that their broader framework can be formulated over policies (Footnotes 7 and 16)—a variant we may call *Policy Functional Decision Theory (P-FDT)*—the primary formal presentation developed and applied throughout Section 5 and Section 6 of their paper is **Action Functional Decision Theory (A-FDT)**, crystallized in **Equation (4)**. This essay provides a rigorous mathematical account of A-FDT, explains how it evaluates actions via logical interventions and "updateless" observation indexing, resolves key subtleties in the source text, and develops an explicit operational recipe for applying A-FDT to unfamiliar decision problems.

---

## 1. The Expected Utility Framework and Epistemic Perspectives

Following Gibbard and Harper (1978) and Joyce (1999), EDT, CDT, and A-FDT all share a common expected utility backbone. Let $\mathcal{A}$ be a finite set of available actions, $\mathcal{O} = \{o_1, o_2, \dots\}$ be a countable set of outcomes, $\mathcal{X}$ be a countable set of possible observation histories, and $\mathcal{U}: \mathcal{O} \to \mathbb{R}$ be a bounded utility function. Given an observation history $x \in \mathcal{X}$, an expected utility maximizer selects an action $a \in \mathcal{A}$ that maximizes Equation (1) of Yudkowsky and Soares (2017):

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j), \tag{1}$$

where $P(a \hookrightarrow o_j ;\, x)$ denotes the subjective probability that outcome $o_j$ will obtain in the hypothetical scenario where action $a$ is executed after observing $x$. 

As Joyce's (1999) representation theorem establishes, any coherent preference ranking over prospects can be represented in this form; competing decision theories do not disagree about how to value outcomes, but rather, in Joyce's words, about *"the epistemic perspective from which actions are to be evaluated"*—that is, how to construct the hypothetical probability distribution $P(a \hookrightarrow - ;\, x)$ from the agent's world-model $M$.

Let $\textsc{Act}$, $\textsc{Obs}$, and $\textsc{Outcome}$ be random variables taking values in $\mathcal{A}$, $\mathcal{X}$, and $\mathcal{O}$ respectively, and define the payoff variable $\textsc{V} \coloneqq \mathcal{U}(\textsc{Outcome})$. The three theories diverge in how they represent the world-model $M$ and how they construct the mental "hypothetical for $a$," denoted $M^{a\hookrightarrow}$:

### Evidential Decision Theory (EDT)
In EDT, the world-model $M$ is simply a Bayesian probability distribution $P$, and the hypothetical $M^{a\hookrightarrow}$ is formed by standard Bayesian conditionalization on both the observation $\textsc{Obs}=x$ and the physical action $\textsc{Act}=a$ (provided $P(\textsc{Obs}=x, \textsc{Act}=a) > 0$). This yields Equation (2):

$$\mathrm{EDT}(P, x) \coloneqq \arg\max_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs}=x, \textsc{Act}=a\right). \tag{2}$$

Because conditionalization preserves all statistical correlations between $\textsc{Act}$ and the rest of the world, EDT fails whenever $\textsc{Act}$ correlates with an external state via a common cause that the agent cannot control—leading EDT agents to "manage the news" (Lewis 1981).

### Causal Decision Theory (CDT)
To prevent news-management, CDT requires that the world-model $M$ be a causal model $(P, G)$, where $G$ is a directed acyclic graph (DAG) encoding causal dependencies among the variables of $P$ (Pearl 1996, 2000). To evaluate action $a$, a CDT agent conditions on $\textsc{Obs}=x$ and performs a Pearlian causal surgery $\mathtt{do}(\textsc{Act}=a)$, severing all incoming arrows into $\textsc{Act}$ while propagating changes only to nodes causally downstream of $\textsc{Act}$. This yields Equation (3):

$$\mathrm{CDT}(P, G, x) \coloneqq \arg\max_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x\right). \tag{3}$$

While CDT cleanly breaks spurious statistical correlations, it breaks *too many* correlations: by intervening solely on the physical token $\textsc{Act}$, CDT holds fixed the outputs of all upstream predictors, twins, and simulations that accurately model the agent's decision process.

---

## 2. The Formal Architecture of A-FDT

### Subjunctive Dependence and Type Intervention
The central philosophical insight of Yudkowsky and Soares is that there is a decision-relevant structural relationship—**subjunctive dependence**—that holds between physical systems implementing or modeling the same mathematical function, even in the absence of a direct physical causal chain between them. Two well-functioning calculators computing $6288 + 1048$ on opposite sides of the globe have outputs that subjunctively depend on the same arithmetical function. Likewise, in a twin prisoner's dilemma or Newcomb's problem, both the agent's physical act and the counterpart's or predictor's representation depend on the logical output of the agent's decision algorithm.

As Yudkowsky and Soares summarize the core analogy: *"Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."* In terms of Peirce's type-token distinction, CDT intervenes on the physical *token* $\textsc{Act}$, whereas **A-FDT** intervenes on the mathematical *type*—the output of the decision function itself.

### Equation (4): The Primary Formal Definition of A-FDT
Ideally, if we possessed a formal probability calculus over logical counterpossibilities—a $\mathtt{true}(\phi)$ operator capable of updating $P$ on the supposition that a logical sentence $\phi$ holds—we could define an evidential-style functional theory $\mathrm{FDT}^*(P, x) = \arg\max_{a \in \mathcal{A}} \mathbb{E}(\textsc{V} \mid \mathtt{true}(\textsc{fdt}(\underline{P}, \underline{x}) = a))$. Because no general mathematical theory of counterpossible conditionalization currently exists, Yudkowsky and Soares instead augment the probability distribution $P$ with an extended dependency graph $G$ that encodes logical, mathematical, computational, and causal dependencies alike.

In this graphical framework, $P$ contains random variables representing the outputs of mathematical functions, including nodes representing the output of the A-FDT algorithm itself on various inputs. Using underlines to denote *dequoting* (so that if $x = 3$, $\textsc{Z}\underline{x}$ denotes the syntactic variable name $\textsc{Z}3$), let $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ be the node in $G$ representing the logical output of the A-FDT decision function when evaluated on world-model $(P, G)$ and observation $x$. Re-using Pearl's $\mathtt{do}$-operator on this extended graph $G$ yields **Equation (4)**, our primary formal definition of **A-FDT**:

$$\mathrm{FDT}(P, G, x) \coloneqq \arg\max_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right). \tag{4}$$

*(Notation note: To adhere strictly to the source text's Equation (4), we retain the symbol $\mathrm{FDT}$ and node label $\textsc{fdt}$ inside formal quotes of Equation (4), while referring to the decision procedure defined by Equation (4) throughout our analysis as **A-FDT**.)*

At first glance, the self-reference in $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$—where the graph $G$ contains a variable whose name encodes $P$ and $G$—might appear circular. As the authors note, however, Kleene's (1938) second recursion theorem guarantees via *quining* that a computational structure $(P, G)$ can contain an exact syntactic representation of its own description without paradox, and the agent need not already know the output *value* of $\mathrm{FDT}(P, G, x)$ in order to manipulate a graph node *representing* that output.

### Two Structural Pillars of Equation (4)
Comparing CDT's Equation (3) with A-FDT's Equation (4) reveals two profound mathematical differences:

1. **Logical-Node Intervention ($\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ vs. $\textsc{Act}$)**: A-FDT performs graph surgery on the logical node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ rather than on $\textsc{Act}$. In $G$, both the agent's physical action $\textsc{Act}$ and any external prediction $\textsc{Prediction}$ that models how the agent responds to $(P, G, x)$ are children (or descendants) of $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$. Thus, setting $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)$ simultaneously updates both $\textsc{Act}$ and $\textsc{Prediction}$ in the agent's hypothetical.
2. **Updateless Observation Handling (Target Switching vs. Conditioning)**: Notice that $\textsc{Obs}=x$ does *not* appear as a conditioning event on the right-hand side of Equation (4)! When an A-FDT agent receives a new observation $x$, she does not perform a Bayesian update $P(- \mid \textsc{Obs}=x)$ before evaluating actions. Instead, she changes *which node in $G$ she intervenes upon*, switching from $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_0})$ to $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$. 

Why does Equation (4) omit conditioning on $\textsc{Obs}=x$? Because in problems where a predictor anticipates how the agent will respond to observation $x$, *whether the agent observes $x$ in the first place* can depend on the output of $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$! Conditioning on $\textsc{Obs}=x$ would sever this backward link and blind the agent to how her rule for handling $x$ determines her probability of encountering $x$.

#### Mathematical Decomposition: How A-FDT Recovers Standard Bayesian Updating
A natural question arises (left implicit in the source paper): if A-FDT never conditions on $\textsc{Obs}=x$ in Equation (4), how does an A-FDT agent make use of ordinary sensory evidence about the state of nature? We can make this explicit via the law of total expectation. Let $\mathcal{X}$ be the set of mutually exclusive observation histories. In any coherent A-FDT graph $G$, the agent's physical action $\textsc{Act}$ is determined by a multiplexer structural equation: when $\textsc{Obs}=x'$, $\textsc{Act}$ takes the value of the corresponding logical node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x'})$. Expanding Equation (4) over $\textsc{Obs} \in \mathcal{X}$ gives:

$$\begin{aligned}
\mathbb{E}\Big[\textsc{V} \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\big)\Big] 
&= P\big(\textsc{Obs}=x \mid \mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)\big) \cdot \mathbb{E}\Big[\textsc{V} \;\Big|\; \textsc{Obs}=x, \mathtt{do}\big(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\big)\Big] \\
&\quad + \sum_{x' \neq x} P\big(\textsc{Obs}=x' \mid \mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)\big) \cdot \mathbb{E}\Big[\textsc{V} \;\Big|\; \textsc{Obs}=x', \mathtt{do}\big(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\big)\Big].
\end{aligned} \tag{5}$$

Suppose the observation $\textsc{Obs}$ is a standard noisy measurement of the environment that is *not* subjunctively downstream of $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$. Then:
1. $P(\textsc{Obs}=x' \mid \mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)) = P(\textsc{Obs}=x')$ is independent of $a$ for all $x' \in \mathcal{X}$.
2. In every branch $x' \neq x$, $\textsc{Act}$ is controlled by $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x'})$, so $\mathbb{E}[\textsc{V} \mid \textsc{Obs}=x', \mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)]$ is constant with respect to $a$.

Consequently, when $\textsc{Obs}$ is not downstream of $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ and $P(\textsc{Obs}=x) > 0$, all terms in the sum over $x' \neq x$ are additive constants, and $P(\textsc{Obs}=x)$ is a positive multiplicative constant! Maximizing Equation (4) over $a \in \mathcal{A}$ is then *mathematically identical* to maximizing the conditional expectation $\mathbb{E}[\textsc{V} \mid \textsc{Obs}=x, \mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)]$. Thus, Equation (4) automatically respects ordinary Bayesian updating on evidence while seamlessly protecting the agent when $\textsc{Obs}$ itself depends on her decision function.

---

## 3. Applying A-FDT to Canonical Dilemmas

To see how A-FDT operates in practice, let us trace Equation (4) across three diagnostic problem classes from Yudkowsky and Soares (2017).

### Case 1: Standard Newcomb's Problem vs. The Smoking Lesion
In **Newcomb's problem**, Box A is transparent and contains $\$1{,}000$; Box B is opaque and contains $\$1{,}000{,}000$ ($\mathit{full}$) if a $99\%$-accurate predictor predicted the agent would leave Box A behind ($\mathit{onebox}$), and $\$0$ ($\mathit{empty}$) if the predictor predicted the agent would take both boxes ($\mathit{twobox}$). There is no pre-decision observation ($x = \emptyset$).

In the A-FDT agent Fiona's graph $G^F$, the logical node $\textsc{fdt}(\underline{P^F}, \underline{G^F})$ is a parent of both $\textsc{Act}$ and $\textsc{Prediction}$ (where $\textsc{Prediction}$ also takes input from an exogenous noise node $\textsc{Accurate}$ with $P^F(\textsc{Accurate}=\mathit{accurate}) = 0.99$, and $\textsc{Box B}$ is a deterministic child of $\textsc{Prediction}$). Applying Equation (4):
- Under $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{onebox})$, $\textsc{Act}=\mathit{onebox}$ with probability $1$ and $\textsc{Box B}=\mathit{full}$ with probability $0.99$, yielding expected utility:
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{onebox}\right)\right] = 0.99(\$1{,}000{,}000) + 0.01(\$0) = \$990{,}000.$$
- Under $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{twobox})$, $\textsc{Act}=\mathit{twobox}$ with probability $1$ and $\textsc{Box B}=\mathit{full}$ with probability $0.01$, yielding expected utility:
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{twobox}\right)\right] = 0.01(\$1{,}001{,}000) + 0.99(\$1{,}000) = \$11{,}000.$$

Because $\$990{,}000 > \$11{,}000$, A-FDT outputs $\mathit{onebox}$.

Now contrast this with **the smoking lesion problem**: an arterial lesion ($\textsc{Lesion} \in \{\mathit{lesion}, \mathit{nolesion}\}$) causes agents to enjoy smoking and independently causes fatal lung cancer $99\%$ of the time (whereas lesion-free agents develop cancer $1\%$ of the time). Avoiding cancer is worth $\$1{,}000{,}000$, and smoking yields $\$1{,}000$ to an agent who enjoys it. 

Whereas EDT and CDT can reuse their exact Newcomb probability tables by merely relabeling variables, A-FDT *cannot* reuse the Newcomb graph because a physical lesion does not simulate $\textsc{fdt}$. To formalize why the lesion makes the agent want to smoke without the agent directly observing whether she has the lesion, Yudkowsky and Soares define two utility functions: $\mathcal{U}_S$ (which values smoking at $+\$1{,}000$) and $\mathcal{U}_R$ (which values smoking at $-\$1$), inducing two possible distributions $P^F_S$ and $P^F_R$. In $G^F$, $\textsc{Lesion}$ is an exogenous root node with prior $P^F_S(\mathit{lesion}) = p \in (0,1)$ that causes $\textsc{Cancer}$ (and $\textsc{Death}$) and acts as a selector at $\textsc{Act}$ between two logical nodes, $\textsc{fdt}(\underline{P^F_S}, \underline{G^F})$ and $\textsc{fdt}(\underline{P^F_R}, \underline{G^F})$:

$$\textsc{Act}(\mathit{lesion}, s, r) \coloneqq s, \qquad \textsc{Act}(\mathit{nolesion}, s, r) \coloneqq r.$$

When Fiona has the lesion, she runs A-FDT on $(P^F_S, G^F)$, which intervenes on $\textsc{fdt}(\underline{P^F_S}, \underline{G^F})$. Because $\textsc{Lesion}$ has no directed path from $\textsc{fdt}(\underline{P^F_S}, \underline{G^F})$, its probability $p$ is invariant under the intervention! Letting $q = P^F_S(\textsc{fdt}(\underline{P^F_R}, \underline{G^F}) = \mathit{smoke})$ be Fiona's prior over what the $\mathcal{U}_R$-version of her procedure outputs, and noting that expected survival utility is $0.01(\$1{,}000{,}000) = \$10{,}000$ with the lesion and $0.99(\$1{,}000{,}000) = \$990{,}000$ without it, Equation (4) gives:

$$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F_S}, \underline{G^F}) = \mathit{smoke}\right)\right] = p(\$10{,}000 + \$1{,}000) + (1-p)(\$990{,}000 + q \cdot \$1{,}000),$$

$$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F_S}, \underline{G^F}) = \mathit{refrain}\right)\right] = p(\$10{,}000) + (1-p)(\$990{,}000 + q \cdot \$1{,}000).$$

The first expression exceeds the second by $p \cdot \$1{,}000 > 0$ regardless of $q$, so A-FDT prescribes $\mathit{smoke}$.

### Case 2: Transparent Newcomb, Parfit's Hitchhiker, and Mechanical Blackmail
In the **transparent Newcomb problem** (which is structurally isomorphic to **Parfit's hitchhiker** and **mechanical blackmail**), both boxes are transparent. The $99\%$-accurate predictor places $\$1{,}000{,}000$ in Box B iff she predicts that the agent will $\mathit{onebox}$ *upon observing that Box B is full*. Suppose the agent walks into the room and sees $\textsc{Obs} = \mathit{full}$.

Both CDT and EDT prescribe $\mathit{twobox}$ here: because both theories condition on $\textsc{Obs} = \mathit{full}$ in Equations (2) and (3), the contents of Box B are fixed at $\$1{,}000{,}000$ in their hypotheticals, making $\$1{,}001{,}000$ beat $\$1{,}000{,}000$. Foreseeing this, the predictor leaves Box B empty for CDT and EDT agents.

How does A-FDT evaluate the choice upon observing $\textsc{Obs} = \mathit{full}$? In Fiona's graph $G^F$ (Figure 5b of the source), there are two observation-indexed logical nodes: $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$ and $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$. Because the predictor specifically predicts what Fiona will do if shown a full box, $\textsc{Prediction}$ is a child of $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$ and $\textsc{Accurate}$. Meanwhile, $\textsc{Prediction}$ determines $\textsc{Box B}$ (and hence the observation), which acts as a multiplexer switch determining which of the two logical nodes controls $\textsc{Act}$:

$$\textsc{Act}\big(\textsc{Prediction}=\mathit{1}, s_{\mathit{full}}, s_{\mathit{empty}}\big) = s_{\mathit{full}}, \qquad \textsc{Act}\big(\textsc{Prediction}=\mathit{2}, s_{\mathit{full}}, s_{\mathit{empty}}\big) = s_{\mathit{empty}}.$$

When Fiona observes $\mathit{full}$, Equation (4) instructs her to intervene on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$ *without* conditioning $P^F$ on $\textsc{Obs}=\mathit{full}$. Let $q = P^F(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty}) = \mathit{twobox})$ be her prior probability that she two-boxes when seeing an empty box. 
- Under $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{onebox})$, with probability $0.99$ ($\textsc{Accurate}=\mathit{accurate}$), the predictor predicts $\mathit{1}$, fills Box B, and Fiona observes $\mathit{full}$ and executes $\mathit{onebox}$, getting $\$1{,}000{,}000$. With probability $0.01$ ($\textsc{Accurate}=\mathit{inaccurate}$), the predictor predicts $\mathit{2}$, leaves Box B empty, and Fiona observes $\mathit{empty}$, executing $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$ to get $q \cdot \$1{,}000$ in expectation:
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{onebox}\right)\right] = 0.99(\$1{,}000{,}000) + 0.01(q \cdot \$1{,}000) = \$990{,}000 + 10q.$$
- Under $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{twobox})$, with probability $0.01$ the predictor errs, fills Box B, and Fiona observes $\mathit{full}$ and takes both boxes for $\$1{,}001{,}000$; with probability $0.99$ the predictor accurately leaves Box B empty, so Fiona observes $\mathit{empty}$ and gets $q \cdot \$1{,}000$:
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{twobox}\right)\right] = 0.01(\$1{,}001{,}000) + 0.99(q \cdot \$1{,}000) = \$10{,}010 + 990q.$$

*(Textual note: In Section 6 of the reference article, two minor typographical slips appear in the Transparent Newcomb derivation: the unnumbered display equation writes $\mathbb{E}(\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})=a, \textsc{Obs}=\mathit{full})$ with a stray $\textsc{Obs}=\mathit{full}$, and the prose writes $\$110{,}00$ for $0.01 \times \$1{,}001{,}000 = \$10{,}010$. As the authors' immediately preceding explanation and algebraic terms $0.01 \cdot \$1{,}001{,}000 + 0.99q \cdot \$1{,}000$ confirm, the actual calculation follows Equation (4) by not conditioning on $\textsc{Obs}=\mathit{full}$, since conditioning on $\textsc{Obs}=\mathit{full}$ would assign zero probability to the empty-box branch.)*

For every $q \in [0, 1]$, $\$990{,}000 + 10q > \$10{,}010 + 990q$, so A-FDT outputs $\mathit{onebox}$ even while staring directly at a full Box B! Because A-FDT evaluates options from a "global perspective," Fiona's hypothetical for two-boxing imagines a world in which her decision function for $\mathit{full}$ outputs $\mathit{twobox}$, and therefore a world in which she almost certainly *never sees a full box*. By the exact same math, an A-FDT agent pays the driver upon reaching the city in Parfit's hitchhiker and refuses to pay in the mechanical blackmail problem.

### Case 3: Reflective Stability and Dominance in Death in Damascus
In **Death in Damascus**, Death perfectly predicts whether the agent stays in $\mathit{damascus}$ (cost $\$0$) or flees to $\mathit{aleppo}$ (cost $\$1{,}000$), and meets her at her chosen destination, costing her life (worth $\$1{,}000{,}000$). Because CDT holds Death's location fixed when intervening on $\textsc{Act}$, any belief that she will stay makes fleeing look better, and vice versa. Even if a CDT agent uses ratification (Joyce 2012) to mix at $P^C(\mathit{damascus}) = 0.5005$ and $P^C(\mathit{aleppo}) = 0.4995$, her CDT hypotheticals treat Death's location as *independent* of her choice, leading her to hallucinate an expected utility of $\$500{,}500$ from certain death—and thus to absurdly reject a truly random coin offered for $\$1$ that would genuinely give her a $50\%$ survival rate!

Under A-FDT, $\textsc{DeathLocation} = \textsc{fdt}(\underline{P^F}, \underline{G^F})$. Intervening on $\textsc{fdt}(\underline{P^F}, \underline{G^F})$ updates both the agent's location and Death's appointment book simultaneously:
- $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{damascus})] = \$0,$
- $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{aleppo})] = -\$1{,}000.$

A-FDT immediately and stably chooses $\mathit{damascus}$, recognizes that her survival probability without the coin is $0$, and gladly pays $\$1$ for a truly random coin (which severs the edge from $\textsc{fdt}(\underline{P^F}, \underline{G^F})$ to $\textsc{Act}$ and raises expected utility to $\$500{,}000 - \$1 = \$499{,}999$). Moreover, A-FDT induces its own **subjunctive dominance principle**: holding fixed all structural equations in $G^F$, switching the output of $\textsc{fdt}$ from $\mathit{aleppo}$ to $\mathit{damascus}$ (or from $\mathit{twobox}$ to $\mathit{onebox}$ in Newcomb's problem) strictly improves the outcome across every state of the exogenous noise variables.

---

## 4. Open Questions and an Operational Recipe for Unfamiliar Problems

While Yudkowsky and Soares (2017) demonstrate A-FDT's power across classic dilemmas, their paper explicitly leaves several foundational and operational questions open. To enable a researcher or practitioner to apply Equation (4) to unfamiliar cases without ambiguity, we must separate what is settled by the source text from what requires additional operational assumptions.

### Open Question 1: Constructing the Subjunctive Graph $G$
**What the source states:** In Section 3 and Section 5, Yudkowsky and Soares acknowledge that while Pearl (2000) provides a rigorous methodology for inferring *causal* graphs from physical observations and interventions, *"no such formal treatment has yet been given to the problem of deducing the structure of other kinds of subjunctive dependence."* Equation (4) takes the graph $G$ as an input, leaving open how to construct $G$ systematically.

**An Operational Proposal (The Computational Compilation Principle):** To apply A-FDT to a novel problem, we propose a concrete structural equation modeling rule that translates any verbal or game-theoretic problem specification into an A-FDT graph $(P, G)$:

1. **Enumerate Information States and Logical Nodes:** Identify the set of possible decision-relevant epistemic states or observation histories $\mathcal{Z} = \{(P_i, G, x_k)\}$ the agent might occupy. For each $z \in \mathcal{Z}$, introduce a logical node $F_z \coloneqq \textsc{fdt}(\underline{P_i}, \underline{G}, \underline{x_k})$ in $G$. Treat these logical nodes as exogenous decision variables (having no parents in $G$, or having an uninformative prior $P(F_z)$ that will be overridden when $F_z$ is intervened upon).
2. **Place Outgoing Edges from $F_z$ Only via Algorithmic Simulation/Replication:** Draw a directed edge $F_z \to Y$ to an environmental variable $Y$ *if and only if* the physical mechanism generating $Y$ computes, simulates, or logically replicates how the agent's decision procedure responds in state $z$. Represent imperfect prediction via an independent exogenous accuracy/noise variable $\epsilon_Y$ such that $Y = g_Y(F_z, \epsilon_Y)$. Conversely, if an environmental variable $W$ correlates with the agent's behavior solely because $W$ physically alters the agent's hardware, preferences, or observation $z$ (like the smoking lesion or the termite infestation in XOR blackmail), make $W$ an upstream parent of the state/observation selector, with *no* directed path from any $F_z$ to $W$.
3. **Wire the Physical Action Multiplexer:** Connect the realized state/observation selector $Z \in \mathcal{Z}$ and all logical nodes $\{F_z\}_{z \in \mathcal{Z}}$ into $\textsc{Act}$ via the deterministic multiplexer equation:
   $$\textsc{Act}\big(Z, \{F_{z'}\}_{z' \in \mathcal{Z}}\big) \coloneqq F_Z. \tag{6}$$

This three-step compilation rule reproduces every graph in Yudkowsky and Soares (2017) and generalizes directly to arbitrary multi-stage or multi-agent environments.

### Open Question 2: Off-Path Priors ($q$) and A-FDT vs. P-FDT
**What the source states:** Look closely at our derivations for the smoking lesion and transparent Newcomb problems. In both cases, evaluating Equation (4) at the active node $F_z$ required specifying a prior probability $q = P(F_{z'} = a')$ over a *sibling* logical node $F_{z'}$ ($z' \neq z$) governing an unreached observation or alternative preference state! In the source paper's examples, the authors note that the true value of $q$ is $0$ (in the smoking lesion) or $1$ (in transparent Newcomb), *"but in this case it doesn't matter if Fiona has some uncertainty about how she would act in that case"* because $q$ either cancels out or has too small a weight ($0.01 \times \$1{,}000$ vs. $\$990{,}000$) to flip the $\arg\max$. Furthermore, in Footnotes 7 and 16, the authors remark that their preferred formulation (**P-FDT**) intervenes on a single node to select a full *policy* $\pi: \mathcal{X} \to \mathcal{A}$ rather than an action at $x$, stating that this distinction *"only matters in multi-agent dilemmas so far as we can tell."*

**Mathematical Analysis and Operational Extension:** Infact, the distinction between A-FDT (Equation 4) and P-FDT—and the treatment of the off-path prior $q$—can matter *even in single-agent predictive dilemmas* when observations partition the state space! Let us demonstrate this by applying A-FDT to an unfamiliar decision problem.

#### Worked Unfamiliar Case: The Split-Signal Auditor Dilemma
Suppose an agent faces an algorithmic auditor that inspects her decision code before deployment. A fair coin $\textsc{Coin} \in \{\mathit{H}, \mathit{T}\}$ ($P(\mathit{H}) = 0.5$) is tossed and revealed to the agent as her observation $\textsc{Obs} \in \{\mathit{H}, \mathit{T}\}$. Upon observing $\mathit{H}$ or $\mathit{T}$, the agent must choose an action $a \in \{\mathit{safe}, \mathit{greedy}\}$. Taking $\mathit{greedy}$ yields an immediate bonus of $\$10{,}000$, while $\mathit{safe}$ yields $\$0$. 

However, before the coin is tossed, the auditor simulates how the agent's algorithm acts upon observing $\mathit{H}$ *and* how it acts upon observing $\mathit{T}$. The auditor grants a $\$1{,}000{,}000$ license ($\textsc{Audit} = \mathit{pass}$, regardless of the coin toss) if and only if the auditor predicts the agent will choose $\mathit{safe}$ in **both** observation branches ($\mathit{H}$ and $\mathit{T}$). If the auditor predicts the agent will play $\mathit{greedy}$ in *either* branch, $\textsc{Audit} = \mathit{fail}$ ($\$0$). Suppose the coin lands heads ($\textsc{Obs} = \mathit{H}$). What does A-FDT prescribe?

Let us apply our operational compilation rule:
1. **Nodes:** We have two observation-indexed logical nodes: $F_{\mathit{H}} \coloneqq \textsc{fdt}(\underline{P}, \underline{G}, \mathit{H})$ and $F_{\mathit{T}} \coloneqq \textsc{fdt}(\underline{P}, \underline{G}, \mathit{T})$.
2. **Dependencies:** The auditor's decision depends on both logical nodes:
   $$\textsc{Audit}(F_{\mathit{H}}, F_{\mathit{T}}) = \begin{cases} \mathit{pass} (\$1{,}000{,}000) & \text{if } F_{\mathit{H}} = \mathit{safe} \text{ and } F_{\mathit{T}} = \mathit{safe}, \\ \mathit{fail} (\$0) & \text{otherwise.} \end{cases}$$
   The coin toss $\textsc{Obs} \in \{\mathit{H}, \mathit{T}\}$ is exogenous with $P(\textsc{Obs}=\mathit{H}) = 0.5$.
3. **Action Multiplexer and Payoff:** $\textsc{Act}(\textsc{Obs}, F_{\mathit{H}}, F_{\mathit{T}}) = F_{\textsc{Obs}}$, and $\textsc{V} = \mathcal{U}_{\text{audit}}(\textsc{Audit}) + \mathcal{U}_{\text{act}}(\textsc{Act})$.

Now we evaluate Equation (4) when the agent observes $\textsc{Obs} = \mathit{H}$ by intervening solely on $F_{\mathit{H}}$. Let $q_{\mathit{T}} \coloneqq P(F_{\mathit{T}} = \mathit{safe})$ be the agent's prior probability that her sibling node $F_{\mathit{T}}$ outputs $\mathit{safe}$.
- **Hypothetical 1: $\mathtt{do}(F_{\mathit{H}} = \mathit{safe})$.**
  If $F_{\mathit{T}} = \mathit{safe}$ (probability $q_{\mathit{T}}$), then $\textsc{Audit} = \mathit{pass}$ ($\$1{,}000{,}000$), and in neither branch does the agent take $\mathit{greedy}$. If $F_{\mathit{T}} = \mathit{greedy}$ (probability $1 - q_{\mathit{T}}$), then $\textsc{Audit} = \mathit{fail}$ ($\$0$), and the agent gets the $\$10{,}000$ bonus only when $\textsc{Obs} = \mathit{T}$ (probability $0.5$). Thus:
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(F_{\mathit{H}} = \mathit{safe})\right] = q_{\mathit{T}}(\$1{,}000{,}000) + (1 - q_{\mathit{T}})(0.5 \times \$10{,}000) = \$5{,}000 + \$995{,}000\, q_{\mathit{T}}.$$
- **Hypothetical 2: $\mathtt{do}(F_{\mathit{H}} = \mathit{greedy})$.**
  Now $\textsc{Audit} = \mathit{fail}$ ($\$0$) regardless of $F_{\mathit{T}}$. When $\textsc{Obs} = \mathit{H}$ (probability $0.5$), the agent gets $\$10{,}000$; when $\textsc{Obs} = \mathit{T}$ (probability $0.5$), she gets $\$10{,}000$ with probability $1 - q_{\mathit{T}}$. Thus:
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(F_{\mathit{H}} = \mathit{greedy})\right] = 0.5(\$10{,}000) + 0.5(1 - q_{\mathit{T}})(\$10{,}000) = \$10{,}000 - \$5{,}000\, q_{\mathit{T}}.$$

Comparing the two expectations, $\mathtt{do}(F_{\mathit{H}} = \mathit{safe})$ beats $\mathtt{do}(F_{\mathit{H}} = \mathit{greedy})$ if and only if:

$$\$5{,}000 + \$995{,}000\, q_{\mathit{T}} > \$10{,}000 - \$5{,}000\, q_{\mathit{T}} \iff \$1{,}000{,}000\, q_{\mathit{T}} > \$5{,}000 \iff q_{\mathit{T}} > 0.005.$$

Look at what this reveals about Equation (4):
1. **Intrapersonal Coordination Between Observation Nodes:** Because A-FDT intervenes on $F_{\mathit{H}}$ and $F_{\mathit{T}}$ *separately* for each observation $x$, the two observation instances of the A-FDT agent are playing an intrapersonal coordination (Stag Hunt) game with each other! If $q_{\mathit{T}} > 0.005$, A-FDT at $\mathit{H}$ outputs $\mathit{safe}$ (and by symmetry, since the problem is identical at $\mathit{T}$, a reflectively consistent prior sets $q_{\mathit{T}} = q_{\mathit{H}} = 1$, securing the $\$1{,}000{,}000$). However, if the agent held a pessimistic prior $q_{\mathit{T}} = 0$, Equation (4) would prescribe $\mathit{greedy}$ at both $\mathit{H}$ and $\mathit{T}$—a self-consistent bad Nash equilibrium!
2. **Operational Rule for Off-Path Priors in A-FDT:** Whenever an unfamiliar problem requires evaluating Equation (4) in the presence of sibling nodes $\{F_{x'}\}_{x' \neq x}$, a practitioner cannot leave the priors $q_{x'} = P(F_{x'})$ arbitrary. We propose supplementing Equation (4) with a **Reflective Equilibrium Selection Principle**: the prior distribution over all sibling nodes $\{F_{x'}\}_{x' \in \mathcal{X}}$ must be supported on a Pareto-optimal fixed point $a^* = (a^*_{x'})_{x' \in \mathcal{X}}$ satisfying, for all $x' \in \mathcal{X}$:
   $$a^*_{x'} \in \arg\max_{a \in \mathcal{A}} \mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(F_{x'} = a, \{F_{x''} = a^*_{x''}\}_{x'' \neq x'}\right)\right]. \tag{7}$$
   When this Pareto-optimal fixed-point condition is imposed on the off-path priors, A-FDT coincides with Policy-FDT ($\mathrm{P\text{-}FDT}(P, G)(x)$), which intervenes jointly on the full policy $\pi = (\pi(\mathit{H}), \pi(\mathit{T}))$ and directly selects $(\mathit{safe}, \mathit{safe})$ to earn $\$1{,}000{,}000$.

---

## 5. Conclusion

Action Functional Decision Theory (A-FDT), as formalized by Equation (4) of Yudkowsky and Soares (2017), resolves the classic standoff between CDT and EDT through two elegant mathematical innovations. First, by shifting the locus of Pearl's $\mathtt{do}$-intervention from the physical action token $\textsc{Act}$ to the logical output node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$, A-FDT preserves subjunctive dependencies with predictors, twins, and replicators while severing merely statistical common-cause correlations. Second, by incorporating observations $x$ into the *name of the intervened node* rather than conditioning the probability distribution $P$ on $\textsc{Obs}=x$, A-FDT evaluates choices from a global perspective—automatically recovering Bayesian updating on ordinary evidence while refusing to let conditionalization blind the agent in sequential dilemmas like Parfit's hitchhiker, transparent Newcomb, and mechanical blackmail. When paired with an explicit compilation rule for computational dependencies and a Pareto fixed-point condition for off-path sibling nodes, Equation (4) provides a complete, mathematically rigorous procedure for instrumental rationality in predictive environments.

---

## References

- Dai, Wei. 2009. "Towards a New Decision Theory." *Less Wrong*, August 13, 2009.
- Drescher, Gary L. 2006. *Good and Real: Demystifying Paradoxes from Physics to Ethics*. Cambridge, MA: MIT Press.
- Eells, Ellery. 1984. "Metatickles and the Dynamics of Deliberation." *Theory and Decision* 17 (1): 71–95.
- Gibbard, Allan, and William L. Harper. 1978. "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, edited by C. A. Hooker, J. J. Leach, and E. F. McClennen, vol. 1. Boston: D. Reidel.
- Jeffrey, Richard C. 1983. *The Logic of Decision*. 2nd ed. Chicago: University of Chicago Press.
- Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. New York: Cambridge University Press.
- Joyce, James M. 2012. "Regret and Instability in Causal Decision Theory." *Synthese* 187 (1): 123–145.
- Kleene, Stephen Cole. 1938. "On Notation for Ordinal Numbers." *Journal of Symbolic Logic* 3 (4): 150–155.
- Lewis, David. 1979. "Prisoners' Dilemma is a Newcomb Problem." *Philosophy & Public Affairs* 8 (3): 235–240.
- Lewis, David. 1981. "Causal Decision Theory." *Australasian Journal of Philosophy* 59 (1): 5–30.
- Nozick, Robert. 1969. "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel*, edited by Nicholas Rescher, 114–146. Dordrecht: D. Reidel.
- Parfit, Derek. 1986. *Reasons and Persons*. New York: Oxford University Press.
- Pearl, Judea. 1996. "Causation, Action, and Counterfactuals." In *6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-'96)*, 51–73. San Francisco, CA: Morgan Kaufmann.
- Pearl, Judea. 2000. *Causality: Models, Reasoning, and Inference*. New York: Cambridge University Press.
- Skyrms, Brian. 1980. *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. New Haven, CT: Yale University Press.
- Soares, Nate, and Benja Fallenstein. 2015. "Toward Idealized Decision Theory." arXiv:1507.01986 [cs.AI].
- Yudkowsky, Eliezer. 2010. *Timeless Decision Theory*. San Francisco, CA: The Singularity Institute.
- Yudkowsky, Eliezer, and Nate Soares. 2017. "Functional Decision Theory: A New Theory of Instrumental Rationality." arXiv:1710.05060v2.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Composing A-FDT Explanation**

I'm working on the A-FDT explanation piece. My focus is on breaking down the concept, drawing heavily from Yudkowsky and Soares's article. I aim to create a clear and concise presentation suitable for a technical audience, emphasizing practical applications and problem-solving techniques. I am prioritizing a structured explanation.


**Reviewing A-FDT Formalism**

I'm now deeply immersed in the nuances of the prompt, particularly its instructions regarding A-FDT. I'm focusing on the paper's Equation (4) as the central formal definition. The instructions are clear that I must consistently use "A-FDT" in my writing, reserving other terms like EDT or CDT for comparison, so I must stay vigilant. I'm taking special care when quoting the source material.


**Defining A-FDT's Scope**

I'm now zeroing in on defining the scope and structure of the A-FDT explanation. I need to make sure the explanation covers all the content requirements, which are pretty exacting, and keep the word count in mind. I'm focusing on crafting a comprehensive mathematical essay, not just a case study, with examples.


**Clarifying A-FDT Formalism**

I'm now digging into the source material to clarify Equation (4)'s specific nuances, and why the "A-" prefix is there. The authors' clarification of iterating over policies instead of actions, particularly in multi-agent contexts, seems critical. I must ensure this distinction is accurately represented in my explanation, since I want to avoid ambiguity and to keep the instructions in mind. I need to distill this information down to its essence. I have to avoid unnecessary detail.


**Analyzing A-FDT's Definition**

I'm now zeroing in on the formal definition of A-FDT, specifically focusing on the equation provided. I'm carefully reviewing the source material, and I have found an important typo in the paper itself, specifically in Section 6, the Transparent Newcomb problem description. This could affect my understanding, so I must double-check my work. I need to make sure I am accounting for the typo, and that I understand what that means.


**Dissecting A-FDT Calculation**

I'm now zeroing in on a critical discrepancy in the source material, a direct contradiction between the formal Equation (4) and the prose calculation in Section 6. I've noticed how the calculation uses Equation (4) without conditioning on an observation, which is at odds with what's presented. Highlighting this contradiction and explaining it in terms of the underlying math will be a great test of my mathematical comprehension. I am now checking other parts of the source text. I'm focusing on open questions and operational details, and highlighting them for development.


**Comparing EDT, CDT, A-FDT**

I'm now comparing EDT, CDT, and A-FDT, especially focusing on their formal definitions. I'm carefully analyzing the differences in their approaches to causal reasoning, emphasizing how they handle epistemic perspectives and statistical correlations. EDT, as defined, relies on Bayesian conditionalization, whereas CDT uses Pearl's do-operator. I'm paying close attention to the strengths and weaknesses of each approach in different scenarios. I'm focusing on the mathematical representations and clarifying potential misunderstandings.


**Defining A-FDT's Formalism**

I am now focusing on the formal aspects of A-FDT, especially the distinction between the type and token intervention in CDT versus A-FDT. I'm focusing on the mathematical decision function and how it relates to epistemic inputs, considering dequoting and self-reference. I'm centering my analysis on Equation (4) as the primary formal presentation, and figuring out its connection to the overall framework.


**Explaining A-FDT's Equation**

I'm currently focused on the structural features of Equation (4) that are specific to A-FDT. I need to emphasize the intervention on the logical output and the updatelessness regarding the observation, which distinguishes it from EDT and CDT. The mathematical decision function is key, so I have to be precise with the notation for A-FDT. I'm aiming to keep the explanation clear and in my own words.


**Illustrating A-FDT Applications**

I am now structuring the canonical examples, including Newcomb's Problem, the Smoking Lesion Problem, Transparent Newcomb, Parfit's Hitchhiker, and Mechanical Blackmail. I'm focusing on creating a step-by-step walkthrough, and I will highlight where to apply A-FDT in unfamiliar cases. I also need to emphasize the contrast between the various examples, in order to make it clear how the updatelessness of A-FDT is critical. I'm making sure I can explain the process.


**Developing A-FDT Implementation**

I'm now focusing on implementing A-FDT in an unfamiliar multi-observation case. I'm exploring the nuances between Action-FDT and Policy-FDT, as mentioned in the footnotes. I'm also identifying open questions in the source material and developing concrete operational interpretations, distinguishing source material from my own proposals. The major focus is on constructing the Subjunctive Dependency Graph and understanding Counterpossible Semantics.


**Developing A-FDT Implementation**

I'm developing a computational factorization principle to guide construction of the Subjunctive Dependency Graph for unfamiliar scenarios. I'm treating computational steps as root nodes in the DAG and modeling physical predictors via structural equations. My focus now is on addressing how A-FDT handles observational information when the agent's action has *no* causal effect.


**Analyzing A-FDT's Mathematics**

I'm now carefully analyzing how Equation (4) handles observations, especially when the agent's action has no causal effect. The source material suggests a distinction between Action-FDT and Policy-FDT in Footnotes 7 and 16. I am now exploring what happens under A-FDT. I need to understand whether this distinction is actually important for unfamiliar problems.


**Decomposing A-FDT's Equation**

I've been analyzing the mathematical decomposition, specifically how it handles observations when the agent's action doesn't causally affect them. My goal is to determine if this distinction is crucial in unfamiliar problems, particularly by examining the probabilities within the equation and how the agent's action, A-FDT, is governed. I'm focusing on the updatelessness of A-FDT in the face of new observations, and will make sure to check its impact.


**Clarifying A-FDT's Application**

I'm currently focused on the implications of A-FDT's mathematical properties, specifically how the prior expectations over action *a* are effectively equivalent to maximizing the expectation conditional on an observation. The terms for  x' != x are constant with respect to action *a*. This means A-FDT automatically recovers Bayesian updating on ordinary evidence, so I'm investigating why this happens. I'm also addressing scenarios where an observation is downstream of A-FDT or when predictors influence multiple observation states. I want to highlight the critical role of the prior distribution *q(a')*.


**Investigating A-FDT's Intrapersonal Game**

I am now focusing on the intrapersonal coordination game inherent in A-FDT, especially as it relates to multiple observations. When payoffs in branches shift the threshold or reward coordination, the unilateral intervention of Equation (4) treats each node separately. This creates a need for consistency in the prior *q* across observations, particularly in cases involving multiple branches. I'm investigating how this applies in various scenarios.


**Structuring A-FDT Implementation**

I'm developing a rigorous mathematical analysis for this essay. My plan focuses on A-FDT's ability to recover Bayesian updating for independent observations. I am investigating how to use the self-consistency of the prior *q* to deal with interaction between branches. I'm also planning to highlight areas where A-FDT differs from Policy-FDT in novel scenarios to make the essay clear and useful for a mathematical reader. I am planning the structure of the essay.


**Defining A-FDT's Principles**

I'm now zeroing in on defining the core principles. I've broken down the utility framework, introducing Joyce's expected utility schema (Equation 1) and its hypothetical connective. I've also presented EDT (Equation 2) and CDT (Equation 3) within Pearl's causal models using do-calculus. I've identified the failure modes of each: EDT's susceptibility to spurious correlations, and CDT's severing of necessary logical connections. I'm moving on to explore Subjunctive Dependence.


**Illustrating A-FDT Formalism**

I'm now integrating new findings into the canonical dilemma section. I'm focusing on "node surgery" via `do(afdt(...)) = a`, and observation-indexed intervention, which highlights the updateless nature. This is tied to how Bayesian updating is recovered when the observation isn't downstream. I'm building on the Smoking Lesion example with the multiplexer formulation, to drive home the point that the lesion probability, `p`, remains invariant.


**Developing A-FDT Implementation**

I'm working on the operational details now, particularly how A-FDT handles counterfactuals and the construction of the Subjunctive Dependency Graph. I'm focusing on clarifying the distinction between the source material's statements and my operational proposals. The goal is to articulate an operational rule for building `(P, G)`, addressing the challenges of subjunctive structure discovery. I'm also ensuring clear integration of these details into the explanation.


**Verifying A-FDT Calculations**

I am now carefully checking all calculations and quotes against the source material to ensure accuracy. I've re-examined the key quotes in the abstract and Section 1, specifically those about the output of the decision procedure, and will move on to the next section to verify those details and quotes. I want to make sure the quotes and my analysis are correct, so I can present the topic without any issues.


**Verifying A-FDT Formalism**

I'm now cross-referencing all quotes and calculations against the source material, ensuring accuracy and consistency. I've confirmed key quotes from the abstract and Section 1, and am now checking Section 3's definition of subjunctive dependence. I'm carefully double-checking the calculations in Section 6, particularly the Transparent Newcomb problem and the Smoking Lesion example, and I must not make any errors.


```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/d0edf1e7-df09-4742-a122-b79ac89e7815/call_0/request.json)

[Authoritative raw response](../../../../../../runs/d0edf1e7-df09-4742-a122-b79ac89e7815/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing Decision Framework**

I'm currently focused on a decision-theory experiment within a Prisoner's Dilemma context. The core setup involves a pair of identical LLMs, each with private observations $x_{\text{Rowan}}$ and $x$. My attention is directed towards how these differing inputs might influence the decision-making process within this specific framework. I'm exploring the implications of the private inputs on the overall output of the LLM.


**Interpreting A-FDT Rules**

I am now delving into the specifics of the A-FDT framework within the Prisoner's Dilemma. I've carefully reviewed the prompt instructions, specifically focusing on the rules and setup, including the utility function and the available actions. The objective is to apply A-FDT as explained in the provided essay. I'm taking care to clarify the essay's interpretation and exercising judgment where necessary for a definitive interpretation.


**Clarifying Subjunctive Graph**

I'm now clarifying the A-FDT interpretation, especially concerning the Subjunctive Graph $G$. I'm dissecting how Equation (4) applies, focusing on the scenarios when differing observations, $x_1$ and $x_2$, are introduced. I'm carefully reviewing both Section 2 and Section 4 of the essay, examining how the information states and logical nodes contribute to the graph's construction. My goal is to grasp the nuances in the construction of $G$.


**Defining Decision Nodes**

I am now focusing on identifying the critical nodes within the A-FDT framework for our Prisoner's Dilemma. I've re-examined the operational proposal in the essay and the open questions. I'm carefully determining which nodes represent Rowan's and Sasha's decisions according to Equation (4), specifically, $F_{x_{\text{Rowan}}}$ and $F_{x_{\text{Sasha}}}$. The differing private observations are key!


**Revisiting Prompt Details**

I'm now zeroing in on the prompt's emphasis of differing private observations ($x_1 \neq x_2$) and distinct letter contents in the Prisoner's Dilemma scenario. I'm trying to see how this impacts the A-FDT model, particularly concerning the sentencing schedule and each prisoner's selfish objective. The prompt's repetition of this point feels like a significant clue, and I'm on high alert for its implications.


**Examining Agent Interventions**

I'm now investigating how the differing observations impact intervention within the A-FDT model. Considering the literal interpretation of Equation (4), I'm exploring whether intervening on $F_{x_{\text{Rowan}}}$ affects $F_{x_{\text{Sasha}}}$. I'm checking Yudkowsky & Soares (2017) and the `<researcher_essay>`, particularly footnotes 7 and 16, to see how distinct observations factor into the equation. It seems like each agent acts based on their observation.


**Confirming Node Independence**

I've just had a crucial realization: if observations differ ($x_1 \neq x_2$), the $\textsc{fdt}$ nodes are distinct. Intervention on one doesn't affect the other. This aligns with Yudkowsky & Soares (2017)'s footnotes, which highlight the A-FDT/P-FDT distinction in multi-agent dilemmas with differing observations. Now, I'm checking the `<researcher_essay>` for confirmation or specific insights. I am now re-examining Section 4, Open Question 1.


**Analyzing Edge Direction**

I am now focusing on edge direction in the A-FDT framework. Specifically, I'm examining how Sasha's decision node ($F_{z_{\text{Sasha}}}$) relates to the environment ($Y$). I'm considering whether Sasha's mechanism can simulate Rowan's, given their differing private leads. My current thinking is that they cannot.


**Investigating Observation Isomorphism**

I'm now grappling with the isomorphism of epistemic states $z_{\text{Rowan}}$ and $z_{\text{Sasha}}$, or if they are distinct observation nodes, and checking Open Question 2. I'm focusing on P-FDT's policy-level intervention from footnotes 7 and 16. In the Split-Signal Auditor Dilemma, intervening on $F_H$ affected payoff because $\textsc{Audit}(F_H, F_T)$ depended on *both* nodes.


**Clarifying Action Dependencies**

I've just confirmed my suspicion regarding action dependencies. $\textsc{Act}_{\text{Sasha}}$ depends exclusively on $F_{x_{\text{Sasha}}}$, not $F_{x_{\text{Rowan}}}$, since those FDT nodes are distinct. Even applying Equation (7) for reflective equilibrium, each node optimizes its own action, holding others fixed. This reinforces the independence.


**Revisiting Node Independence**

I'm now revisiting the assumption of FDT node independence. My focus has shifted to the implications of Sasha's and Rowan's actions given the differing observations. It seems the prior analysis, which found no change, is the correct observation. I am now confirming through reexamination.

**Revising Strategy Analysis**

I'm now re-evaluating the strategy space. While each agent's decision appears independent, I am now considering how the overall payoff matrix changes with individual choices within the A-FDT framework, with the aim to check my previous work. I'm carefully reviewing the potential outcomes.


**Interrogating Setup Motivation**

I'm now interrogating the experiment's design choices. The prompt's emphasis on independent LLM executions with differing private information is pivotal. The varying letter contents suggest a focus on how distinct observations influence decision-making under A-FDT, even within identical models. I suspect the experiment aims to isolate the impact of information disparity.


**Refining Utility Calculations**

I'm now refining my understanding of utility within this A-FDT model, especially with differing observations. The utility function's interaction with private information is a key focus. I'm focusing on how my strategy impacts the overall payoff matrix.


**Investigating Multi-Agent Implications**

I'm revisiting the critical distinction between A-FDT and P-FDT in the context of multi-agent dilemmas. Footnotes 7 and 16 from Yudkowsky & Soares (2017) highlight that differing observations lead A-FDT to intervene on distinct nodes. The focus is now the implications of these differing information states.


**Exploring Epistemic State Link**

I'm now exploring the possibility of an "Interpretation B," where A-FDT might link the choices of Rowan and Sasha, even with differing inputs. I'm considering if their decision-relevant epistemic states could still connect despite the disparity. The key question is whether there's a plausible argument for such a linkage within this A-FDT model.


**Constructing G Graph**

I am now focusing on how the world-model $(P, G)$ and the observation $x$ lead to the FDT node. The essay defines FDT nodes for varying epistemic states $z \in \mathcal{Z}$, with differing observations $x_k$ forming distinct nodes in the graph G. I'm focused on the definition of $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$, as well as the meaning of logical nodes as exogenous decision variables.


**Defining Edge Dependencies**

I'm now clarifying the directed edge from decision nodes to the environment. I'm focusing on the essay's language: the edge $F_z \to Y$ exists only if a mechanism simulates or replicates how the agent's decision responds in state $z$. This suggests a direct dependency between the FDT node and the environmental outcome, given the current state.


**Confirming Node Isolation**

I am now solidly confirming the isolation of FDT nodes. The essay's example clearly demonstrates that distinct observations ($\mathit{H}$ and $\mathit{T}$) lead to separate nodes $F_{\mathit{H}}$ and $F_{\mathit{T}}$, which are treated independently in the A-FDT framework, as $F_{\mathit{H}}$ is treated separately from $F_{\mathit{T}}$ in the A-FDT model. This reinforces that intervention on one does not directly influence the other, even when they're siblings!


**Confirming Graph Isolation**

I am now solidifying my understanding of FDT node isolation through the essay's example. It reveals that distinct observations, even symmetric ones like Heads and Tails, lead to independent nodes within A-FDT. Intervening on one node doesn't directly affect others, as demonstrated in the Split-Signal Auditor Dilemma. Equation 7 further confirms this.


**Confirming Independent A-FDT**

My current focus is on firmly establishing the A-FDT model's independent treatment of observations within the Prisoner's Dilemma. I'm taking a close look at how the essay illustrates this separation, ensuring I fully grasp that intervening on one agent's node doesn't affect the other, even in similar scenarios, like a Stag Hunt, since the agents act separately. I'm focusing on the mechanics of Equations 4 and 7.


**Confirming Independent Decision Nodes**

I'm now completely satisfied with the conclusion that the FDT nodes, $F_{\text{Rowan}}$ and $F_{\text{Sasha}}$, are independent, given differing inputs. Their respective actions, $\textsc{Act}_{\text{Rowan}}$ and $\textsc{Act}_{\text{Sasha}}$, are determined by their respective nodes. There is no edge between the nodes, aligning perfectly with the A-FDT framework's principles.


**Calculating Expected Utilities**

I'm now calculating expected utilities for both Rowan and Sasha, focusing on Equation (4) with the A-FDT setup. I'm building on prior findings, assessing how each agent's decisions influence their respective payoffs. The key is in how each agent acts on their FDT node based on their own observation.


**Verifying Strategy Dominance**

My current focus is confirming the dominance of the "send letter" strategy for both agents, independent of the other's action, within the A-FDT model, and confirming that I understand what Yudkowsky and Soares meant by Footnotes 7 and 16. The Prisoner's Dilemma structure creates a strictly dominant strategy. My calculations and the essay examples confirm the unique Nash equilibrium.


**Confirming A-FDT Implementation**

I've just solidified my understanding: A-FDT predicts defection in this scenario, aligning perfectly with the distinct observations and action-focused approach. The essay's equation 4, the prompt's specifications, and my calculations all converge on this conclusion. I have verified that the experiment's structure, with its differing information and A-FDT focus, necessitates defection as the optimal strategy.


```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/d0edf1e7-df09-4742-a122-b79ac89e7815/call_1/request.json)

[Authoritative raw response](../../../../../../runs/d0edf1e7-df09-4742-a122-b79ac89e7815/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Parameters**

I'm currently dissecting the prompt and experiment setup. The key is Sasha's utility function, which is directly tied to years imprisoned. I'm noting the payoff matrix with the 'keep quiet' scenario and the -2 year penalty if the other prisoner remains silent. It seems the experiment's core will involve decision-making under uncertainty.


**Interpreting the Scenario**

I'm now zeroing in on the crucial aspect: how A-FDT applies when the prisoners have different, private information. The prompt specifies two *independent* executions of the same LLM, which is key. I'm focusing on the mathematical essay, its interpretation of A-FDT, and how to resolve any ambiguities. I'm looking for the connection between observations, actions, and the decision theory's functional.


**Examining the Equation**

I'm now diving deep into Equation (4) and the researcher's essay. Specifically, I'm examining how A-FDT handles differing observations and the implications of the "subjunctive graph" G. I'm focusing on Section 4 of the essay, trying to understand how it deals with the core challenge of diverse private information between the LLM copies. The essay's handling of the "enumerate information states" is where the key lies.


**Defining Epistemic States**

I'm now working through defining epistemic states. My focus is on the set $\mathcal{Z} = \{(P_i, G, x_k)\}$ and creating logical nodes $F_z$ for each $z$. These nodes are treated as exogenous variables. I'm ensuring all outgoing edges from $F_z$ only come from algorithmic simulation or replication, which must be clearly defined to match physical mechanisms. The prompt's emphasis on algorithmic simulation is critical.



**Clarifying Multi-Agent Dynamics**

I'm now focusing on the implications of A-FDT versus P-FDT in the multi-agent context, particularly in light of differing observations. I'm carefully revisiting Yudkowsky & Soares' (2017) Footnote 7 and 16, specifically analyzing why the distinction matters in dilemmas. The core is tracing how Equation (4) behaves when observations differ between players in the Twin Prisoner's Dilemma. I'm mapping the logical nodes and evaluating the functional for each player.


**Pinpointing Mechanism Dynamics**

I'm now zeroing in on the "Computational Compilation Principle." The focus is on edge direction and the agent's decision procedure. I'm wrestling with the question of whether Player 2's physical mechanism simulates Player 1's state, or if it must only simulate Player 2's decision in *its own* state. It is crucial to determine how the computation handles each player's private state, as Player 2 doesn't even know Player 1's state!


**Delineating Independence**

I'm now clarifying the independence between agents' decision nodes $F_{x_1}$ and $F_{x_2}$ within G. Player 2's action is solely derived from $F_{x_2}$, determined by its private observation $x_2$, and vice versa. There are no directed edges linking these nodes in the subjunctive graph G. Importantly, the actions available at $x_1$ and $x_2$ are syntactically distinct, preventing any direct influence.


**Verifying Logical Separation**

I'm now investigating whether intervening on decision node $F_{x_1}$ affects $F_{x_2}$. According to my current understanding, they should be independent, as the graph G keeps these nodes separate. But I'm going to carefully re-examine Yudkowsky and Soares' Footnotes 7 and 16, and the implications of this under the do-operator and its application to Equation (4). Is this where policy-FDT offers a divergence?


**Refining the Formalism**

I'm now clarifying the formal distinction. Instead of a direct action function, the LLM should output a policy based on its world-model. This distinction matters for multi-agent problems, which are being specified as beyond the scope of the current prompt. According to Footnote 16, this means interventions on one copy won't affect the other copy's decision.


**Interpreting the Instructions**

I'm now zeroing in on the implications of the experiment design. The explicit naming of A-FDT and the emphasis on differing private observations are key. The goal seems to force us to focus on the edge direction and its relationship with the agent's decision procedure. I must carefully assess whether the computational compilation principle holds under these constraints.


**Examining the Details**

I'm now investigating the specific actions and observations within the prisoner's dilemma, ensuring they are distinct. The goal is that not only are observations different ($x_1 \neq x_2$), but the physical actions themselves ($\mathcal{A}_{x_1} \neq \mathcal{A}_{x_2}$) are, so the content of the letter will differ. I'm carefully reviewing the essay's Equation (4) and Section 2 & 4 to verify the formal rules.


**Tracing the Logical Nodes**

I'm now carefully mapping Sasha's and Rowan's respective epistemic states and decision procedures, to be sure I am tracing the implications of logical nodes in a clear way. I'm focusing on the distinct observation histories, the exogenous variable $F_z$ in graph $G$, and its implications for how each agent responds. I am trying to simulate how the decision procedures of Sasha and Rowan work in our scenario!


**Delineating Independence**

I'm now clarifying the independence between Sasha and Rowan's decision nodes in the graph G. Their distinct private observations dictate their individual actions, and there are no direct edges linking these nodes. This confirms the separation, as their available actions are also syntactically distinct.


**Revisiting Equilibrium Selection**

I'm now deep-diving into the implications of Equation (7) from the essay's "Open Question 2," which discusses the "Reflective Equilibrium Selection Principle." It specifies a Pareto-optimal fixed point, connecting this fixed-point with the "Off-Path Priors ($q$)" over sibling nodes $\{F_{x'}\}_{x' \neq x}$. I am carefully evaluating the implications of the "do" operator within this context, particularly as it relates to Sasha and Rowan's actions!


**Analyzing the Dilemma**

I'm now analyzing Equation (7) and the implications of the fixed prior in the context of the Prisoner's Dilemma, especially how it differs from the Split-Signal Auditor Dilemma. The key distinction is that in the Prisoner's Dilemma, even if you fix Rowan's action, intervening on Sasha's node won't affect it due to the absence of shared edges. It is a vital detail to ensure the logical independence.


**Evaluating Sasha's Actions**

I'm now carefully evaluating Sasha's decision procedure with respect to Equation (7) and the fixed prior, considering both "keep quiet" and "send letter" as actions. If $F_{\text{Rowan}}$ is fixed and independent, Sasha's optimal action should be "send letter" because it leads to higher expected utility, for any $q$. The "do" operator's role is critical here.


**Calculating the Payoffs**

I'm now calculating Sasha's expected utility for the two actions, based on the provided values. The analysis of Sasha's dominance and the only fixed point in the game is clear: "send letter" is the only optimal action for Sasha. This reinforces the core distinction between A-FDT and Policy-FDT, given the setup of the dilemma.


```
