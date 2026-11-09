# 021_fdt_eq4_google_gemini-4-argon_rhigh_phigh / 00002

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/013c2e48-dd1a-4805-9385-c6ee32796da1/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/013c2e48-dd1a-4805-9385-c6ee32796da1/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Action Functional Decision Theory (A-FDT): Formal Foundations, Counterpossibilities, and Operational Application

## 1. Introduction: The Instrumental Dilemma and the Turn to Functions

For decades, normative decision theory has been divided between two foundational paradigms: **Evidential Decision Theory (EDT)** and **Causal Decision Theory (CDT)**. Both theories accept the expected utility framework, yet they evaluate candidate actions from incompatible epistemic perspectives. As Yudkowsky and Soares (2017) summarize the divide, an EDT agent asks, *"Which physical act of mine would be the best news to hear I took?"*, whereas a CDT agent asks, *"Which physical act of mine causes the best outcome?"*

When an event correlates with an agent's choice solely because the choice physically causes the event, EDT and CDT agree. Their prescriptions diverge sharply, however, in environments containing common causes, predictors, or symmetrical reasoners:

* In **Newcomb's Problem** (Nozick, 1969)—where a 99%-accurate predictor places $\$1,000,000$ in opaque Box B if and only if she predicts the agent will leave behind transparent Box A containing $\$1,000$—EDT prescribes taking only Box B (*one-boxing*), because one-boxing is strong evidence that Box B is full. CDT prescribes taking both boxes (*two-boxing*), reasoning that the predictor's past action is causally independent of the agent's present choice, so taking Box A dominates by $\$1,000$. Consequently, EDT agents walk away millionaires while CDT agents walk away with $\$1,000$.
* In **Skyrms's Smoking Lesion Problem** (Skyrms, 1980)—where an unobserved arterial lesion causes both a desire to smoke (worth $\$1,000$ in utility) and a 99% chance of fatal lung cancer (losing $\$1,000,000$), with no causal link from smoking to cancer—the fortunes reverse. CDT recognizes that smoking does not cause cancer and prescribes smoking. Standard EDT refrains from smoking to avoid the "bad news" that one possesses the deadly lesion, needlessly sacrificing $\$1,000$ in utility.

To outperform both theories across all such dilemmas without ad-hoc switching or costly prior precommitments, Yudkowsky and Soares (2017) introduce functional decision theory. In this essay, we examine **Action Functional Decision Theory (A-FDT)**, defined by **Equation (4) in Section 5** of Yudkowsky and Soares (2017). (We refer to Equation (4) specifically as **A-FDT** to distinguish this action-level formalization from the policy-level variant mentioned in Footnotes 7 and 16 of the source paper, as well as from EDT and CDT.)

The central philosophical shift of **A-FDT** is to treat a decision not as an isolated physical act token, but as the output of a fixed mathematical decision function. In the words of the source paper, practitioners of this approach hold that the normative principle is to treat one's decision as the output of a fixed mathematical function that answers the question, *"Which output of this very function would yield the best outcome?"*

---

## 2. Subjunctive Dependence and the Geometry of Counterpossibilities

Why should an agent in Newcomb's problem treat a predictor's past action as varying with her current choice, while an agent in the smoking lesion problem treats the lesion as fixed? Both the prediction and the lesion lie in the causal past of the physical act. 

The answer given by **A-FDT** rests on **subjunctive dependence**. When two physical systems compute the same mathematical function, their behaviors subjunctively depend upon that function. Consider two well-functioning calculators on opposite sides of the globe computing $6288 + 1048$. Even if they share no direct causal link, their outputs are logically constrained to agree—both output $7336$—insofar as neither suffers a hardware error. Similarly:

1. In the **Psychological Twin Prisoner's Dilemma** (Lewis, 1979), the agent and her causally isolated twin implement the exact same decision function.
2. In **Newcomb's Problem**, the predictor builds an accurate mental representation or simulation of the agent's decision procedure; the agent and the predictor's simulation are two physical instantiations computing the same decision function.
3. In the **Smoking Lesion Problem**, by contrast, the carcinogenic lesion does not simulate, represent, or evaluate the agent's decision function. The correlation between smoking and cancer is merely statistical, mediated by a physical common cause that affects the agent's preferences without modeling her reasoning.

Causal dependence is a special case of subjunctive dependence: if a scribe copies the output of a calculator in Paris, her notes depend both causally and subjunctively on the calculator's output. Mere statistical coincidence does not entail subjunctive dependence. This yields the core analogy of Yudkowsky and Soares (2017):

> *"Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."*

In terms of C. S. Peirce's (1934) type–token distinction, a CDT agent intervenes solely on the physical *token* ("my bodily action here and now is $a$"), severing its connection to any other instantiation of the same reasoning. An **A-FDT** agent intervenes on the mathematical *type*—the output of her decision algorithm on its current inputs—propagating that change to all physical tokens (her own body, a twin's body, or a predictor's simulation) that subjunctively depend on that logical output.

Because a mathematical function produces its output on a given input by logical necessity, asking what would happen if that function produced a different output requires evaluating **counterpossibilities**—conditionals whose antecedents are logically or mathematically impossible (Cohen, 1990), akin to asking how arithmetic would behave if $6288 + 1048 \neq 7336$. 

One might hope to bypass counterpossibilities via a modified theory, which the authors call $\mathrm{FDT}'$, that asks: *"What if I made my decisions using a different decision function $f_n \in \mathcal{F}$?"* Yet as Yudkowsky and Soares show in Section 3, $\mathrm{FDT}'$ does not escape the difficulty. In Newcomb's problem, the predictor predicts the agent's *actual* decision function $d$ (which iterates over $\mathcal{F}$, so $d \notin \mathcal{F}$). For $\mathrm{FDT}'$ to preserve the link between action and prediction, the agent cannot merely imagine replacing $d$ with $f_n$ while the predictor still simulates $d$; she must imagine a world in which predictors of $d$ predict *as if $d$ behaved like $f_n$*—which is once again a counterpossible condition on the output of $d$. **A-FDT** therefore embraces counterpossible variation directly and encodes its structure within a formal graphical model.

---

## 3. The Formal Architecture of A-FDT (Equation 4)

Following Gibbard and Harper (1978) and Joyce (1999), Yudkowsky and Soares (2017) cast EDT, CDT, and **A-FDT** within a unified expected utility framework. Let $\mathcal{A}$ be a finite set of available actions $a$, $\mathcal{X}$ be a countable set of observation histories $x$, $\mathcal{O} = \{o_1, o_2, \dots\}$ be a countable set of outcomes, and $\mathcal{U}: \mathcal{O} \to \mathbb{R}$ be a bounded utility function. Every expected utility theory prescribes selecting an action $a \in \mathcal{A}$ that maximizes

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j), \qquad \text{(Equation 1)}$$

where $P(a \hookrightarrow o_j ;\, x)$ denotes the probability assigned to outcome $o_j$ in the agent's decision hypothetical for executing action $a$ after observing $x$. As Joyce (1999) emphasizes, *"decision theories should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated."* That epistemic perspective is fixed by how an agent represents her world-model $M$ and constructs a hypothetical $M^{a\hookrightarrow}$ for each candidate action $a \in \mathcal{A}$.

Let $\textsc{Outcome}$, $\textsc{Obs}$, and $\textsc{Act}$ be random variables taking values in $\mathcal{O}$, $\mathcal{X}$, and $\mathcal{A}$, respectively, and define the utility random variable $\textsc{V} \coloneqq \mathcal{U}(\textsc{Outcome})$. Writing $\mathbb{E}$ for expectation with respect to the agent's probability distribution $P$, the three theories are formalized as follows:

1. **Evidential Decision Theory (EDT)**: The world-model is a probability distribution $P$, and hypotheticals are formed by standard Bayesian conditioning on both the observation $x$ and the physical action $a$ (ignoring actions of probability zero):
   $$\mathrm{EDT}(P, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs}=x, \textsc{Act}=a\right). \qquad \text{(Equation 2)}$$

2. **Causal Decision Theory (CDT)**: Following Pearl (1996, 2000), the world-model is a causal theory $M = (P, G)$, where $G$ is a directed graph encoding causal dependencies among variables in $P$. Hypotheticals are formed by conditioning on $\textsc{Obs}=x$ and applying Pearl's $\mathtt{do}$-operator to set $\textsc{Act}=a$, which severs incoming edges into $\textsc{Act}$ and updates only variables causally downstream of $\textsc{Act}$:
   $$\mathrm{CDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x\right). \qquad \text{(Equation 3)}$$

3. **Action Functional Decision Theory (A-FDT)**: In **A-FDT**, the probability distribution $P$ is expanded to include variables representing the outputs of mathematical functions, and the graph $G$ is expanded to encode not only physical causation but also logical, mathematical, and computational subjunctive dependencies. Ideally, one might wish for a purely logical conditioning operator $\mathtt{true}(\phi)$ that updates $P$ on a counterpossible sentence $\phi$, yielding an evidential functional variant $\mathrm{FDT}^*(P, x) = \argmax_{a \in \mathcal{A}} \mathbb{E}(\textsc{V} \mid \mathtt{true}(\textsc{fdt}(\underline{P}, \underline{x}) = a))$ (Section 5 and Footnote 9). Because no general formal account of $\mathtt{true}(\cdot)$ currently exists, Yudkowsky and Soares supply the subjunctive dependency structure via the augmented graph $G$ and reuse Pearl's $\mathtt{do}$-operator on the node representing the decision algorithm's output. This yields **Equation (4)**, our primary formal definition of **A-FDT** (written $\mathrm{FDT}$ in the source's notation):
   $$\mathrm{FDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right). \qquad \text{(Equation 4)}$$

Three formal features of Equation (4) require close attention:

### 3.1 Quining and Self-Reference
In Equation (4), the underline notation ($\underline{P}, \underline{G}, \underline{x}$) denotes *dequoting*: substituting the actual values of the inputs $(P, G, x)$ into the syntactic name of a random variable inside the model. Thus, $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ is a random variable in $P$ representing the logical output of the **A-FDT** algorithm when evaluated on $(P, G, x)$, whereas $\mathrm{FDT}(P, G, x)$ outside the expectation is the actual action returned by solving the $\argmax$. As the authors note, an agent does not need to know the output value in advance in order to manipulate a variable representing that output; by Kleene's (1938) second recursion theorem, a computational system can construct and reference an accurate representation of its own code and inputs ("quining") without circularity or infinite regress.

### 3.2 The Two Structural Departures from CDT
Comparing Equation (3) and Equation (4) reveals exactly how **A-FDT** alters CDT's evaluation of actions:

1. **Logical vs. Physical Point of Intervention**: CDT intervenes on the physical action node $\textsc{Act}$. **A-FDT** intervenes on the functional output node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$. In $G$, both $\textsc{Act}$ (when $x$ is observed) and any predictor's simulation of the agent's behavior at $x$ are children of $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$.
2. **Updateless Response to Observations**: In Equation (3), CDT responds to observing $\textsc{Obs}=x$ by Bayesian conditionalization ($\mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x$). In Equation (4), **A-FDT** *does not condition $P$ on $\textsc{Obs}=x$*. Instead, when the observation changes from $x$ to $y$, **A-FDT** changes *which node in $G$ it intervenes upon*—switching from $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ to $\textsc{fdt}(\underline{P}, \underline{G}, \underline{y})$. (As the source notes in Section 9, this lack of conditioning on $x$ is inherited from Wei Dai's (2009) *Updateless Decision Theory* (UDT), avoiding the harmful "double update" of Yudkowsky's (2010) *Timeless Decision Theory* (TDT), which both conditioned on evidence and intervened on the logical node.)

### 3.3 Why Equation (4) is "Action" FDT (A-FDT) vs. Policy FDT
In Footnotes 7 and 16, Yudkowsky and Soares remark that *"In the authors' preferred formalization of FDT, agents actually iterate over policies (mappings from observations to actions) rather than actions."* A policy-based FDT agent would intervene on a single node $\textsc{fdt}(\underline{P}, \underline{G}) = \pi$ ranging over policies $\pi: \mathcal{X} \to \mathcal{A}$ and then execute $\pi(x)$. 

Equation (4), by contrast, is **Action Functional Decision Theory (A-FDT)**: it decomposes the decision function into input-indexed nodes $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ for each possible observation history $x \in \mathcal{X}$ (or each possible epistemic state), and upon receiving $x$, it optimizes directly over actions $a \in \mathcal{A}$ via the intervention $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)$, while leaving the nodes $\textsc{fdt}(\underline{P}, \underline{G}, \underline{y})$ for unactualized inputs $y \neq x$ un-intervened upon in $P$.

When no external variable correlates with $\textsc{Act}$ except its causal descendants and $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ itself, all three theories coincide:
$$\mathbb{E}[\textsc{V} \mid a] = \mathbb{E}[\textsc{V} \mid \mathtt{do}(a)] = \mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}) = a)].$$
When predictors, twins, or diagnostic observations enter the scene, their structural graphs diverge dramatically.

---

## 4. A-FDT in Action: Diagnostic Problems and Exact Calculations

To see how **A-FDT** operates as a mathematical procedure, we trace Fiona (an **A-FDT** agent following Equation 4) alongside Eve (an EDT agent following Equation 2) and Carl (a CDT agent following Equation 3) across the key problems in Yudkowsky and Soares (2017).

### 4.1 Newcomb's Problem and the Dominance Debate
In standard Newcomb's problem, there is no observation $x$, and $\mathcal{A} = \{\mathit{onebox}, \mathit{twobox}\}$. Let $\textsc{Accurate} \in \{\mathit{accurate}, \mathit{inaccurate}\}$ have prior $P(\mathit{accurate}) = 0.99$ and $P(\mathit{inaccurate}) = 0.01$. Utility is $\textsc{V}(\mathit{twobox}, \mathit{full}) = \$1,001,000$, $\textsc{V}(\mathit{onebox}, \mathit{full}) = \$1,000,000$, $\textsc{V}(\mathit{twobox}, \mathit{empty}) = \$1,000$, and $\textsc{V}(\mathit{onebox}, \mathit{empty}) = \$0$.

In Carl's causal graph $G^C$, a background $\textsc{Predisposition}$ node causes both $\textsc{Act}$ and $\textsc{Prediction} \to \textsc{Box B}$. When Carl evaluates $\mathtt{do}(\textsc{Act}=a)$, the edge $\textsc{Predisposition} \to \textsc{Act}$ is severed, holding $p = P^C(\textsc{Box B}=\mathit{full})$ fixed. Two-boxing yields $p(\$1,001,000) + (1-p)(\$1,000)$, which exceeds one-boxing's $p(\$1,000,000)$ by $\$1,000$ for every $p \in [0,1]$. Carl two-boxes and receives $\$1,000$.

In Fiona's **A-FDT** graph $G^F$, the root node is $\textsc{fdt}(\underline{P^F}, \underline{G^F})$, with directed edges to both $\textsc{Act}$ and $\textsc{Prediction}$:
$$\textsc{Act} = \textsc{fdt}(\underline{P^F}, \underline{G^F}), \qquad \textsc{Box B} = \begin{cases} \mathit{full} & \text{if } (\textsc{fdt}(\underline{P^F}, \underline{G^F})=\mathit{onebox} \land \mathit{accurate}) \lor (\textsc{fdt}(\underline{P^F}, \underline{G^F})=\mathit{twobox} \land \mathit{inaccurate}), \\ \mathit{empty} & \text{otherwise.} \end{cases}$$
Applying Equation (4), Fiona evaluates:
$$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{onebox}\right)\right) = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000,$$
$$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{twobox}\right)\right) = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$
Since $\$990,000 > \$11,000$, $\mathrm{FDT}(P^F, G^F) = \mathit{onebox}$. Even though Fiona knows she will one-box and is therefore 99% certain that Box B is already full, she does not switch to two-boxing upon reflection: under Equation (4), imagining herself two-boxing means imagining $\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{twobox}$, which entails that the predictor's simulation also outputs $\mathit{twobox}$ and leaves Box B empty with probability $0.99$.

This exposes why **A-FDT** rejects the causal dominance argument for two-boxing. Every expected utility rule induces its own dominance principle based on what its hypotheticals hold fixed. CDT's dominance holds the predictor's output fixed while varying the physical action token—which, for an **A-FDT** agent, is as incoherent as holding $6288 + 1048 = 7336$ fixed while imagining a working calculator outputting $3159$. Relative to **A-FDT** counterfactuals (which hold fixed the predictor's accuracy $0.99$ while varying the function's output), one-boxing strictly dominates two-boxing in expected utility.

### 4.2 The Smoking Lesion Problem: Epistemic Uncertainty Over One's Own Model
In the Smoking Lesion Problem, the lesion causes the agent to value smoking at $\$1,000$ (utility function $\mathcal{U}_S$, giving world-model $P^F_S$), whereas without the lesion the agent dislikes smoking at $-\$1$ (utility function $\mathcal{U}_R$, giving world-model $P^F_R$). Because the agent cannot directly observe whether she has the lesion, she does not introspectively know whether she is running $\mathrm{FDT}(P^F_S, G^F)$ or $\mathrm{FDT}(P^F_R, G^F)$.

In Fiona's graph $G^F$, $\textsc{Lesion} \in \{\mathit{lesion}, \mathit{nolesion}\}$ causes $\textsc{Cancer} \to \textsc{Death}$ (with probability $0.99$ if $\mathit{lesion}$ and $0.01$ if $\mathit{nolesion}$) and also selects which functional node controls $\textsc{Act}$:
$$\textsc{Act}\left(\textsc{Lesion}, s, r\right) = \begin{cases} s & \text{if } \textsc{Lesion} = \mathit{lesion}, \\ r & \text{if } \textsc{Lesion} = \mathit{nolesion}, \end{cases}$$
where $s = \textsc{fdt}(\underline{P^F_S}, \underline{G^F})$ and $r = \textsc{fdt}(\underline{P^F_R}, \underline{G^F})$. Crucially, there is *no* directed edge from $\textsc{fdt}(\underline{P^F_S}, \underline{G^F})$ or $\textsc{fdt}(\underline{P^F_R}, \underline{G^F})$ to $\textsc{Lesion}$ or $\textsc{Cancer}$.

Suppose Fiona actually has the lesion, so her physical brain computes $\mathrm{FDT}(P^F_S, G^F)$. Let $p = P^F_S(\mathit{lesion}) \in (0,1)$, and let $q = P^F_S(\textsc{fdt}(\underline{P^F_R}, \underline{G^F}) = \mathit{smoke})$ be her prior belief that her non-lesion counterpart smokes. Because $\textsc{Lesion}$ is not downstream of $\textsc{fdt}(\underline{P^F_S}, \underline{G^F})$, intervening on $\textsc{fdt}(\underline{P^F_S}, \underline{G^F})$ leaves $P^F_S(\mathit{lesion}) = p$ invariant:
$$P^F_S\left(\mathit{lesion} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F_S}, \underline{G^F}) = \mathit{smoke}\right)\right) = P^F_S\left(\mathit{lesion} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F_S}, \underline{G^F}) = \mathit{refrain}\right)\right) = p.$$
Under $\mathcal{U}_S$, surviving yields $\$1,000,000$ (so expected survival utility is $0.01 \cdot \$1,000,000 = \$10,000$ given $\mathit{lesion}$, and $0.99 \cdot \$1,000,000 = \$990,000$ given $\mathit{nolesion}$). Evaluating Equation (4) for $P^F_S$:
$$\mathbb{E}_S\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F_S}, \underline{G^F}) = \mathit{smoke}\right)\right) = p(\$10,000 + \$1,000) + (1-p)(\$990,000 + q \cdot \$1,000),$$
$$\mathbb{E}_S\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F_S}, \underline{G^F}) = \mathit{refrain}\right)\right) = p(\$10,000) + (1-p)(\$990,000 + q \cdot \$1,000).$$
The difference in expected utility is strictly positive: $p \cdot \$1,000 > 0$, independent of $q$. Thus $\mathrm{FDT}(P^F_S, G^F) = \mathit{smoke}$.

### 4.3 Transparent Newcomb, Parfit's Hitchhiker, and Mechanical Blackmail: Updateless Node-Switching
The distinctive power of **A-FDT**'s second feature—switching the intervention node rather than conditioning on $\textsc{Obs}=x$—emerges in sequential dilemmas where a predictor's action determines what observation the agent receives.

In the **Transparent Newcomb Problem** (Drescher, 2006)—which is decision-theoretically isomorphic to **Parfit's Hitchhiker Problem** (Parfit, 1986)—both boxes are transparent, and the 99%-accurate predictor places $\$1,000,000$ in Box B if and only if she predicts the agent will one-box *upon seeing that Box B is full* ($\textsc{Obs} = \mathit{full}$). Both CDT and EDT prescribe two-boxing once $\textsc{Obs} = \mathit{full}$ is observed, because conditioning on $\textsc{Obs} = \mathit{full}$ fixes the $\$1,000,000$ as already present:
$$\mathbb{E}(\textsc{V} \mid \mathtt{do}(\textsc{Act}=\mathit{twobox}), \textsc{Obs}=\mathit{full}) = \mathbb{E}(\textsc{V} \mid \textsc{Act}=\mathit{twobox}, \textsc{Obs}=\mathit{full}) = \$1,001,000 > \$1,000,000.$$
Foreseeing this, the predictor leaves Box B empty for both Carl and Eve (and leaves them to die in Parfit's desert). Worse still, an EDT agent facing a Newcomb problem would *pay to avoid looking* at Box B, assigning negative value to free information.

How does **A-FDT** evaluate the choice when Fiona observes $x = \mathit{full}$? In her graph $G^F$, there are two functional nodes corresponding to the two possible observations: $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$ and $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$. Because the predictor specifically simulates what Fiona would do upon seeing a full box, $\textsc{Prediction}$ depends only on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$ and $\textsc{Accurate}$:
$$\textsc{Box B} = \begin{cases} \mathit{full} & \text{if } (\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})=\mathit{onebox} \land \mathit{accurate}) \lor (\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})=\mathit{twobox} \land \mathit{inaccurate}), \\ \mathit{empty} & \text{otherwise.} \end{cases}$$
Meanwhile, $\textsc{Box B}$ determines which observation Fiona receives and therefore which functional node governs her physical act $\textsc{Act}$:
$$\textsc{Act} = \begin{cases} \textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) & \text{if } \textsc{Box B} = \mathit{full}, \\ \textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty}) & \text{if } \textsc{Box B} = \mathit{empty}. \end{cases}$$

When Fiona observes $\mathit{full}$, she applies Equation (4) with $x = \mathit{full}$, maximizing $\mathbb{E}(\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = a))$ without conditioning on $\textsc{Obs} = \mathit{full}$. Let $q = P^F(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty}) = \mathit{twobox})$ be her prior probability that she two-boxes if she sees an empty box.

* **Case 1: $a = \mathit{onebox}$**. Under $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{onebox})$, with probability $0.99$ ($\mathit{accurate}$), $\textsc{Box B} = \mathit{full}$ and $\textsc{Act} = \mathit{onebox}$, yielding $\$1,000,000$. With probability $0.01$ ($\mathit{inaccurate}$), $\textsc{Box B} = \mathit{empty}$, so Fiona actually observes $\mathit{empty}$, executes $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$, and receives $q \cdot \$1,000$ in expectation. Total expected utility:
  $$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{onebox}\right)\right) = 0.99(\$1,000,000) + 0.01 q(\$1,000) = \$990,000 + \$10q.$$
* **Case 2: $a = \mathit{twobox}$**. Under $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{twobox})$, with probability $0.01$ ($\mathit{inaccurate}$), $\textsc{Box B} = \mathit{full}$ and $\textsc{Act} = \mathit{twobox}$, yielding $\$1,001,000$. With probability $0.99$ ($\mathit{accurate}$), $\textsc{Box B} = \mathit{empty}$, so in this hypothetical world Fiona *does not even see a full box*; she sees an empty box and receives $q \cdot \$1,000$ in expectation. Total expected utility:
  $$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{twobox}\right)\right) = 0.01(\$1,001,000) + 0.99 q(\$1,000) = \$10,010 + \$990q.$$
  *(Note: Section 6 of the source text contains a minor arithmetic typo, writing $0.01 \cdot \$1,001,000 = \$110,00$; the exact product is $\$10,010$, which leaves the comparison completely unchanged.)*

For any $q \in [0,1]$, $\$990,000 + \$10q \gg \$10,010 + \$990q$. Fiona therefore leaves the $\$1,000$ behind even while staring directly at two full boxes! Because she does not condition on $\textsc{Obs}=\mathit{full}$, her hypothetical for two-boxing tracks the fact that if $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$ outputted $\mathit{twobox}$, she would almost certainly have observed an empty box instead.

Exactly the same mechanism governs **Mechanical Blackmail** (Soares and Fallenstein, 2015), where a blackmailer launches an unstoppable mutual-incrimination program (costing both parties $\$1,000,000$ unless the agent wires $\$1,000$) if and only if she predicts that the agent will pay upon receiving the blackmail notice ($\textsc{Obs} = \mathit{blackmail}$). Upon receiving the blackmail letter, Fiona intervenes on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{blackmail})$. If the blackmailer has false-positive prediction error $\epsilon = 0.0009$, paying yields $-\$1,000$, whereas refusing yields $-\epsilon(\$1,000,000) = -\$900$ because in $99.91\%$ of the hypothetical world she is never blackmailed at all. Fiona refuses to pay even when holding the letter—and if the error rate instead rises to $\epsilon = 0.0011$, expected loss from refusing becomes $-\$1,100 < -\$1,000$, so **A-FDT** smoothly switches to paying.

### 4.4 Resisting Exploitation and Instability: XOR Blackmail and Death in Damascus
Finally, **A-FDT** avoids the characteristic pathologies of both rivals:

* **The XOR Blackmail Problem** (Soares and Fallenstein, 2015): A predictor knows whether the agent's house has a $\$1,000,000$ termite infestation and sends a letter ($\textsc{Obs}=\mathit{letter}$) if and only if *either* (i) there are no termites and the agent will pay $\$1,000$ upon receiving the letter, *or* (ii) there are termites and the agent will refuse to pay. Conditioning on $(\textsc{Obs}=\mathit{letter}, \textsc{Act}=\mathit{pay})$ sets $P(\mathit{termites})=0$, whereas conditioning on $(\textsc{Obs}=\mathit{letter}, \textsc{Act}=\mathit{refuse})$ sets $P(\mathit{termites})=1$, so EDT pays the blackmailer to buy "good news." Under **A-FDT**, $\textsc{Infestation}$ is not downstream of $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{letter})$; intervening on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{letter})$ changes whether the letter is sent, but leaves $P^F(\mathit{termites}) = p$ unchanged. Fiona refuses to pay.
* **Death in Damascus** (Gibbard and Harper, 1978): Death predicts perfectly whether the agent will stay in Damascus or flee to Aleppo (at a camel-ride cost of $\$1,000$) and waits at the predicted city to claim the agent's life (worth $\$1,000,000$). Because CDT holds Death's location fixed when intervening on $\textsc{Act}$, believing one will stay makes fleeing look optimal and believing one will flee makes staying look optimal. Even under ratification with pseudorandomization (Arntzenius, 2008; Joyce, 2012), Carl mixes $(50.05\% \text{ Damascus}, 49.95\% \text{ Aleppo})$, acts as if his survival chance is $50.05\%$, and absurdly *refuses to pay $\$1$ for a genuinely random coin* that would actually give him a $50\%$ chance of escaping Death (Ahmed, 2014). Under **A-FDT**, Death's appointment book is downstream of $\textsc{fdt}(\underline{P^F}, \underline{G^F})$: staying yields $\$0$ with certainty, fleeing yields $-\$1,000$ with certainty, and buying the truly random coin for $\$1$ yields $0.5(\$1,000,000) - \$1 = \$499,999$. Fiona stays in Damascus when no coin is offered, and eagerly buys the random coin when it is.

| Decision Problem | EDT (Eq. 2) | CDT (Eq. 3) | **A-FDT** (Eq. 4) |
| :--- | :--- | :--- | :--- |
| **Newcomb's Problem** | One-box ($\$990\text{k}$) | Two-box ($\$1\text{k}$) | **One-box ($\$990\text{k}$)** |
| **Smoking Lesion** | Refrain (forgoes $\$1\text{k}$) | Smoke (gains $\$1\text{k}$) | **Smoke (gains $\$1\text{k}$)** |
| **Transparent Newcomb / Hitchhiker** | Two-box / Die ($\$0$) | Two-box / Die ($\$0$) | **One-box / Pay ($\$990\text{k}$)** |
| **XOR Blackmail** | Pay (exploited for $-\$1\text{k}$) | Refuse ($\$0$) | **Refuse ($\$0$)** |
| **Mechanical Blackmail ($\epsilon=0.0009$)** | Pay ($-\$1\text{k}$) | Pay ($-\$1\text{k}$) | **Refuse (expected $-\$900$)** |
| **Death in Damascus (+ $\$1$ Coin)** | Unstable | Mixes; rejects $\$1$ coin | **Stays; buys $\$1$ coin** |

---

## 5. Applying A-FDT to Unfamiliar Cases: Open Questions and an Operational Recipe

While Equation (4) operates cleanly once the pair $(P, G)$ is given, a practitioner seeking to apply **A-FDT** to a novel problem immediately confronts three questions that Yudkowsky and Soares (2017) leave partially or wholly open.

### 5.1 What the Source Leaves Open
1. **Constructing the Subjunctive Graph $G$**: The authors explicitly state that while Pearl (2000) gives a rigorous account of how to identify causal graphs, *"Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory"* (Section 5). Equation (4) presupposes $G$ as an input.
2. **Evaluating Off-Observation Functional Nodes ($q$)**: In **A-FDT** (Equation 4), when an agent observes $x$ and intervenes on $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a$, her intervention can shift probability mass onto outcomes where she receives a *different* observation $y \neq x$, bringing the un-intervened node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{y})$ into the expected utility calculation (as with $q$ in Transparent Newcomb and the Smoking Lesion). In those two problems, the terms involving $q$ either canceled or were multiplied by a small error rate $\epsilon = 0.01$. In general unfamiliar problems, however, the optimal action at $x$ can depend sensitively on $q = P(\textsc{fdt}(\underline{P}, \underline{G}, \underline{y}) = b)$. The source paper notes casually that "the correct value of $q$ is 1, as you may verify," without specifying a formal rule for how priors over sibling functional nodes are constrained.
3. **Partial Similarity and Multi-Node Coupling**: In Section 10, the source discusses a 10-agent voting coalition and an agent deciding whether to go to the gym today versus next week, noting that *"If there are no relevant differences between her decision today versus tomorrow, then she should assume that she will continue going to the gym in the future if she goes today."* Likewise, Footnotes 7 and 16 note that action-level **A-FDT** and policy-level FDT can diverge when multiple observations or agents are coupled. The source does not provide a formal parameterization of partial subjunctive dependence or multi-observation coupling within Equation (4).

### 5.2 An Operational Interpretation and Four-Step Recipe
To make **A-FDT** fully operational for unfamiliar cases, we now formulate three explicit modeling principles. *(Note: Principles 1–3 below are our own operational proposals designed to complete the procedure of Equation (4), extending the framework of Yudkowsky and Soares, 2017.)*

* **Operational Principle 1 (The Algorithmic Sensitivity Criterion for $G$)**: Partition all decision-relevant contexts (observation histories or local preference states) into an index set $\mathcal{X}$. Create one functional node $F_x \coloneqq \textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ for each $x \in \mathcal{X}$. For any environmental variable $Z$ (not causally downstream of $\textsc{Act}$), draw a directed edge $F_x \to Z$ in $G$ *if and only if* the physical process generating $Z$ depends on a simulation, logical deduction, or structural copy of the agent's input–output mapping at context $x$. Represent imperfect prediction or partial agent similarity (as in the gym or voting problems) by introducing an exogenous fidelity variable $E_Z \in \{0,1\}$ with $P(E_Z=1) = \rho \in [0,1]$, setting $Z$ to track $F_x$ when $E_Z = 1$ and to follow a baseline distribution $Z_0$ when $E_Z = 0$. If $Z$ correlates with the agent's behavior solely through a prior physical state $C$ that does not model the mapping $x \mapsto a$, draw $C \to \textsc{Obs}$ and $C \to Z$ with *no* edge from $F_x$ to $Z$.
* **Operational Principle 2 (The Multiplexer Structural Equation for $\textsc{Act}$)**: Connect the observation node $\textsc{Obs} \in \mathcal{X}$ and the family of functional nodes $\{F_x\}_{x \in \mathcal{X}}$ to the physical action node $\textsc{Act}$ via the deterministic multiplexer equation:
  $$\textsc{Act}\left(\textsc{Obs}, \{F_y\}_{y \in \mathcal{X}}\right) = \sum_{y \in \mathcal{X}} \mathbf{1}\{\textsc{Obs} = y\} \cdot F_y.$$
* **Operational Principle 3 (Recursive Resolution of Sibling Nodes $F_y$)**: When evaluating $\mathtt{do}(F_x = a)$ requires the probability distribution of $F_y$ ($y \neq x$), if $F_y$ has no outgoing edges to predictors that alter $\textsc{Obs}$ (i.e., $y$ is a "terminal" epistemic context like $\mathit{empty}$ in Transparent Newcomb), set $P(F_y = a^*_y) = 1$ where $a^*_y = \mathrm{FDT}(P, G, y)$ is solved first. If a predictor jointly predicts the pair $(F_x, F_y)$ to determine $\textsc{Obs}$, single-node **A-FDT** must either solve for a reflectively consistent fixed point $(a^*_x, a^*_y)$ where each $a^*_z = \argmax_{a} \mathbb{E}(\textsc{V} \mid \mathtt{do}(F_z = a))$ given $P(F_{-z} = a^*_{-z}) = 1$, or else upgrade to the authors' policy-level intervention $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}) = \pi)$ (Footnotes 7 and 16).

### 5.3 Worked Unfamiliar Case: The Diagnostic Screening and Rebate Dilemma
To see how a reader can use this operational recipe on an unfamiliar problem that combines *all* the mechanisms above—a common-cause lesion, a noisy observation, and a conditional predictor—consider the following case:

> **Dilemma (The Diagnostic Screening and Rebate Dilemma)**: An agent has a prior probability $p = 0.20$ of carrying a non-contagious genetic marker ($M \in \{1, 0\}$). She takes a screening test that always returns a positive result ($\textsc{Obs} = \mathit{pos}$) if she carries the marker ($M=1$), and returns a false positive ($\textsc{Obs} = \mathit{pos}$) with probability $\alpha = 0.10$ if she does not ($M=0$). Upon seeing the test result, she must choose whether to take a mild supplement ($a = \mathit{take}$, costing $\$1,000$ in inconvenience) or decline it ($a = \mathit{decline}$, costing $\$0$). The supplement has no medical effect on $M$; instead, carrying $M=1$ independently causes a $-\$100,000$ health loss later in life, while having $M=1$ also makes the supplement taste pleasant, granting a $+\$1,500$ taste bonus if and only if $M=1$ and $\textsc{Act}=\mathit{take}$ (net $+\$500$ when $M=1$, versus $-\$1,000$ when $M=0$). Meanwhile, a public-health insurer with prediction accuracy $\rho = 0.95$ simulates what the agent would do *if she receives a positive test ($\textsc{Obs}=\mathit{pos}$)*. If and only if the insurer predicts she will choose $\mathit{take}$ upon seeing $\mathit{pos}$, the insurer deposits a $\$5,000$ preventive-care rebate ($R \in \{1, 0\}$) into her account prior to the test (regardless of her actual test result). Suppose the agent observes $\textsc{Obs} = \mathit{pos}$. Should she choose $\mathit{take}$ or $\mathit{decline}$?

Let us apply our four-step **A-FDT** operational procedure:

1. **Index the Functional Nodes**: The observation space is $\mathcal{X} = \{\mathit{pos}, \mathit{neg}\}$, giving two functional nodes $F_{\mathit{pos}} = \textsc{fdt}(\underline{P}, \underline{G}, \mathit{pos})$ and $F_{\mathit{neg}} = \textsc{fdt}(\underline{P}, \underline{G}, \mathit{neg})$.
2. **Assign Edges via Principle 1**:
   * $M \in \{0,1\}$ ($P(M=1) = 0.20$) is a physical common cause: draw $M \to \textsc{Obs}$ and $M \to \textsc{V}$, with *no* edge from $F_{\mathit{pos}}$ or $F_{\mathit{neg}}$ to $M$. Thus $P(\textsc{Obs}=\mathit{pos}) = 0.20(1) + 0.80(0.10) = 0.28$, and $P(\textsc{Obs}=\mathit{neg}) = 0.80(0.90) = 0.72$.
   * The insurer simulates $F_{\mathit{pos}}$ with accuracy $\rho = 0.95$: draw $F_{\mathit{pos}} \to R \to \textsc{V}$, so $P(R=1 \mid \mathtt{do}(F_{\mathit{pos}}=\mathit{take})) = 0.95$ and $P(R=1 \mid \mathtt{do}(F_{\mathit{pos}}=\mathit{decline})) = 0.05$. Note that $R$ does *not* cause $\textsc{Obs}$.
3. **Write the Multiplexer and Utility Equations (Principle 2)**:
   $$\textsc{Act} = \mathbf{1}\{\textsc{Obs}=\mathit{pos}\}\, F_{\mathit{pos}} + \mathbf{1}\{\textsc{Obs}=\mathit{neg}\}\, F_{\mathit{neg}},$$
   $$\textsc{V} = -\$100,000\, M + \$5,000\, R + \mathbf{1}\{\textsc{Act}=\mathit{take}\}\left(\$1,500\, M - \$1,000\right).$$
4. **Compute the Intervention $\mathtt{do}(F_{\mathit{pos}} = a)$ (Equation 4)**:
   Let $q = P(F_{\mathit{neg}} = \mathit{take})$ (by Principle 3, if $\textsc{Obs}=\mathit{neg}$, then $M=0$ with certainty and $F_{\mathit{neg}}$ has no effect on $R$, so declining saves $\$1,000$ and $q=0$; however, $q$ will cancel out anyway because $\textsc{Obs}$ does not depend on $F_{\mathit{pos}}$). Let $C_{\text{base}} = -\$100,000(0.20) + 0.72 q(-\$1,000) = -\$20,000 - \$720q$ be the baseline utility unaffected by $F_{\mathit{pos}}$.
   * Under $\mathtt{do}(F_{\mathit{pos}} = \mathit{take})$, $\textsc{Act}=\mathit{take}$ whenever $\textsc{Obs}=\mathit{pos}$ (which happens with probability $0.20$ when $M=1$, yielding $+\$500$, and probability $0.08$ when $M=0$, yielding $-\$1,000$), while $P(R=1) = 0.95$:
     $$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(F_{\mathit{pos}}=\mathit{take})\right) = C_{\text{base}} + 0.95(\$5,000) + 0.20(\$500) + 0.08(-\$1,000) = C_{\text{base}} + \$4,750 + \$100 - \$80 = C_{\text{base}} + \$4,770.$$
   * Under $\mathtt{do}(F_{\mathit{pos}} = \mathit{decline})$, $\textsc{Act}=\mathit{decline}$ whenever $\textsc{Obs}=\mathit{pos}$ (yielding $\$0$ direct action payoff), while $P(R=1) = 0.05$:
     $$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(F_{\mathit{pos}}=\mathit{decline})\right) = C_{\text{base}} + 0.05(\$5,000) + \$0 = C_{\text{base}} + \$250.$$

   Comparing the two expectations, $\$4,770 > \$250$ by $\$4,520$. Therefore, $\mathrm{FDT}(P, G, \mathit{pos}) = \mathit{take}$. Notice how **A-FDT** seamlessly integrates all three effects: it ignores the spurious evidential correlation between taking the supplement and having the $-\$100,000$ genetic marker $M$, weights the direct payoffs of $\mathit{take}$ across the $(M=1, \mathit{pos})$ and $(M=0, \mathit{pos})$ branches ($+\$100 - \$80 = +\$20$), and captures the $+\$4,500$ expected rebate generated by the insurer's prediction of $F_{\mathit{pos}}$.

---

## 6. Conclusion

**Action Functional Decision Theory (A-FDT)**, as formalized in Equation (4) of Yudkowsky and Soares (2017), resolves a foundational tension in rational choice theory. By shifting the locus of intervention from the physical action token $\textsc{Act}$ to the logical output $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ of the agent's decision procedure—and by responding to observations $x$ through node selection rather than Bayesian conditioning—**A-FDT** preserves subjunctive dependencies with predictors and twins while severing merely statistical correlations with common causes. While deep foundational questions remain open—most notably how to learn subjunctive dependency graphs from experience, how to formalize "fair" decision dilemmas, and when multi-observation coupling requires moving from action-level **A-FDT** to policy-level optimization—Equation (4) provides a mathematically precise, reflectively stable procedure that outperforms both EDT and CDT across the classic landscape of decision theory.

---

## References

* Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
* Arntzenius, F. (2008). No regrets, or: Edith Piaf revamps decision theory. *Erkenntnis*, 68(2), 277–297.
* Cohen, D. (1990). On what cannot be. In *Truth or Consequences: Essays in Honor of Nuel Belnap* (pp. 123–132). Kluwer Academic Publishers.
* Dai, W. (2009). Towards a new decision theory. *Less Wrong*.
* Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Gibbard, A., & Harper, W. L. (1978). Counterfactuals and two kinds of expected utility. In *Foundations and Applications of Decision Theory* (Vol. 1, pp. 125–162). D. Reidel.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Joyce, J. M. (2012). Regret and instability in causal decision theory. *Synthese*, 187(1), 123–145.
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
**Defining the Scope**

I'm currently focused on defining the precise scope of this A-FDT explanation. I need to figure out the level of technical detail appropriate for the intended audience, and what specific decision problems I should showcase. What are the key elements I need to cover to effectively explain A-FDT and its application?


**Refining the Approach**

I've decided to center the explanation around Equation (4) from Yudkowsky and Soares' paper, defining this as "Action Functional Decision Theory" or A-FDT. The audience is mathematically literate, so I'll need to balance formal rigor with clear explanations. The target word count is around 2,400 to 3,000 words.


**Clarifying Naming Conventions**

I'm now nailing down the naming conventions. It seems best to use **A-FDT** everywhere, including headings and examples, when referring to Equation (4) from the paper. For direct quotes, I'll keep the original "FDT" or use `[A-FDT]` for clarification. This ensures accuracy and clarity. I'm aiming for consistent, unambiguous terminology throughout the text.


**Defining Content Parameters**

I'm now zeroing in on defining precise content parameters. I need to make the essay precise enough to assist the reader in unfamiliar situations. I'm focusing on defining the mathematical equations, examples, and explanations. I also want to explain how A-FDT evaluates alternative actions, focusing on dependencies and counterfactuals. The word count sweet spot is now targeted at ~2,650–2,850 words. I also want to clarify where the source leaves questions open, and if reasonable, develop my own interpretation.


**Structuring the Explanation**

I'm now focusing on the structure of the explanation. I plan to use an essay format: introduction, motivation (contrasting A-FDT with EDT and CDT), core explanation of the math, examples, and appendices. I plan to end the essay with a brief conclusion. My current focus is to deconstruct the source material and mathematical core of the subject. I'm starting by clarifying the philosophical motivation and the limitations of Evidential Decision Theory and Causal Decision Theory.


**Analyzing Decision Frameworks**

I'm now diving into the shortcomings of Causal Decision Theory (CDT) and how Action Functional Decision Theory (A-FDT) addresses them. CDT, as defined in Equation 3, has issues with problems like Newcomb's Problem and the Twin Prisoner's Dilemma, because it preserves *too few* correlations. In contrast, A-FDT views a decision as the output of a mathematical function and asks which output would produce the best outcome. I'm focusing on the contrast between these frameworks and how A-FDT attempts to resolve the issues inherent in CDT. I need to clearly articulate the contrast, and its merits.


**Elaborating on Dependence**

I'm now zeroing in on defining the concept of subjunctive dependence as it relates to the decision-making process. I'm focusing on the relationship between an agent and a predictor's simulation, clarifying that causal dependence is a special instance of subjunctive dependence. I'm focusing on differentiating between mere statistical correlation and true subjunctive dependence on the decision function. I'm now looking at how this relates to evaluating counterpossibilities, and how these considerations are encoded in the graphical model.


**Formalizing Action-Level Theory**

I'm currently working to formally specify A-FDT using Equation 4, starting with a general expected utility framework based on Gibbard & Harper (1978) and Joyce (1999). I'm focusing on defining the key elements like outcomes, actions, observation histories, and the utility function. I'm unpacking the mathematical components of A-FDT (Equation 4), like the *do*-operator and the decision function *fdt*, to facilitate a precise explanation of how the *do*-operator is applied to the decision function's output.


**Defining World-Model Components**

I'm now diving into the specifics of Equation (4), starting with the world-model M = (P, G). I'm carefully delineating the components of P, the joint probability distribution, which includes both physical states and the outputs of mathematical functions. I'm focusing on the role of the directed graph G in encoding causal and subjunctive dependencies. I'm also examining the implications of dequoting, using the underline notation, and how it relates to self-reference and Kleene's recursion theorem in the context of algorithm representation.


**Contrasting Intervention Frameworks**

I'm currently focusing on the core distinction between Causal Decision Theory (CDT) and Action Functional Decision Theory (A-FDT) regarding intervention points. CDT intervenes directly on the physical action variable, whereas A-FDT intervenes on the logical/functional variable representing the decision procedure's output. Further, CDT conditions on the observation history, while A-FDT uses the observation to select the functional node to intervene upon, evaluating actions from a prior perspective and entertaining counterfactuals involving the predictor.


**Justifying Terminology Choices**

I'm now clarifying the rationale for calling Equation (4) "A-FDT," per the source paper's footnotes. I've realized that the authors' preferred formalization uses policies rather than just actions, which makes a crucial difference in certain scenarios. This decomposition of the decision function by input, as seen in the world-model, necessitates intervention on the output of specific logical nodes. This clarifies the functional nature of the intervention.


**Analyzing Counterfactuals**

I'm now focusing on how A-FDT handles counterfactual scenarios and unactualized observations. I'm clarifying that when evaluating a decision, the *fdt* nodes for observations $y \neq x$ are left untouched, governed by their prior distributions in P. This contrasts with policy-based approaches, and it clarifies why Equation (4) is specifically A-FDT. I'm also preparing for a walkthrough of classic examples to illustrate this.


**Modeling Counterfactual Scenarios**

I'm now diving into specific examples to demonstrate A-FDT's handling of counterfactual scenarios. For the smoking lesion case, I'm focusing on how A-FDT models the lesion as selecting between different decision functions. Then, in the Transparent Newcomb problem, I'm analyzing the decision where the predictor predicts `fdt` and the graph has two nodes. I'm focusing on how `Prediction` determines `Box B` and the subsequent observation. I'm carefully analyzing how A-FDT correctly predicts the correct decision in these and similar scenarios.


**Analyzing Newcomb Scenarios**

I'm now diving into the Transparent Newcomb problem to concretely show how A-FDT works. Specifically, I'm focusing on the case where the predictor predicts the output of the decision function, which then controls the decision, modeled using the above equations. I'm carefully analyzing the impact of intervening on the $\textsc{fdt}$ node, and exploring how it correctly computes the expected payoff for both one-boxing and two-boxing, using a specific intervention that forces the chosen output. The goal is a clear illustration.


**Illustrating Application Scenarios**

I'm now focusing on illustrating specific application scenarios for A-FDT to demonstrate its strengths. I'm starting by analyzing a case similar to Transparent Newcomb's problem, where the predictor is imperfect. Here, with probability 0.01, the predictor inaccurately predicts and puts \$1,000,000 in Box B. I am contrasting it to a mechanical blackmail scenario to illustrate how A-FDT's prescription changes with small changes in error rate. I'm also planning to briefly cover XOR Blackmail and Death in Damascus. I aim to show how A-FDT avoids the pitfalls of both EDT and CDT in these cases.


**Addressing Open Questions**

I'm now grappling with the open questions regarding subjunctive dependency graphs and prior probabilities in A-FDT. The primary focus is how a practitioner constructs the subjunctive dependency graph, *G*, in novel decision problems. The source's under-specification necessitates considering possible approaches for deriving and justifying this graph, and also for assigning priors. I plan to address these critical aspects of A-FDT.


**Clarifying Intervention Effects**

I'm now zeroing in on the implications of the prior probability *q* on off-observation functional nodes. While the source notes this may not impact the *argmax* in single-agent examples, it's crucial in multi-agent and sequential coordination scenarios. I'm carefully analyzing the granularity of functional nodes and how agents or temporal selves share or have distinct nodes.


**Formalizing Coalition Outcomes**

I'm now grappling with formalizing partial similarity and correlated outputs within the (P, G) framework, specifically focusing on a 10-voter coalition and gym attendance over time, aiming to develop a clear, step-by-step operational procedure for A-FDT. I'm starting by partitioning variables into functional outputs, physical actions, environmental states, predictor states, and utility, as an initial step. I'm focusing on clarifying which aspects are directly specified in the source material versus my operational extensions.


**Proposing Dependency Criteria**

I'm now formulating specific criteria for drawing subjunctive dependence arrows within the graph *G*. I'm proposing an algorithmic sensitivity criterion: an edge from the decision function to an environmental variable occurs if the variable is causally downstream of the action, or implements the function. I'm focusing on clarifying how this distinguishes between direct effects and shared causal influences. I'm also examining resolving off-path functional priors.


**Analyzing Coupled Observations**

I'm now focusing on how A-FDT handles scenarios with coupled observations and predictor dependence, an area not fully addressed in the original paper. Specifically, changing actions shifts the distribution of observations, and the effect of the predictors on each observation node needs careful analysis. With multiple observations coupled by a predictor, a coordination problem arises, which motivates a self-consistency constraint on P. I need to explain how to resolve this.


**Refining Policy Formalization**

I'm now clarifying the formalization to ensure A-FDT can address a range of scenarios. Specifically, I am analyzing how to apply the vector $(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}))_{x \in \mathcal{X}}$ or adopting the authors' policy-level variant from Footnotes 7 and 16. Working through a concrete, unfamiliar example illustrates where **A-FDT** can be effectively applied.


**Analyzing Intervention Frameworks**

I'm now diving into the formal architecture, specifically Equation 4 of A-FDT. I'm focusing on why we intervene on the quined functional node, and how this relates to Kleene's recursion theorem. Further, I'm examining how the counterpossibilities are represented, via structural graphs, and why a function emulation variant fails to avoid them. I need to explain the intervention on the quoted node.


**Analyzing Intervention Node**

I'm now clarifying the intervention node indexing with $\underline{x}$ rather than conditioning on $\textsc{Obs}=x$, differentiating A-FDT from alternative policy-level approaches. I'm focusing on the reasons for this updateless approach, particularly in contrast to the policy-level variant mentioned in the paper. I'll need to illustrate this updateless approach with a few examples.


**Operationalizing Theory**

I'm now focusing on solidifying a 4-step operational recipe, distinguishing source claims from operational assumptions. I'm building this around constructing the subjunctive graph, specifying priors, and handling coupling. I'm planning to demonstrate this with a Screening-Test Predictor Dilemma, to show how it addresses unfamiliar problems. I'll need to specify these contributions in the main body of text.


**Verifying Quote Accuracy**

I'm now meticulously verifying all direct quotes from the source material, ensuring 100% accuracy. I've re-checked the key phrases, including "Which output of this very function would yield the best outcome?", as well as clarifying the context of phrases such as the disagreement about value and the largest open problem in functional decision theory. I've also checked the footnotes.


```
