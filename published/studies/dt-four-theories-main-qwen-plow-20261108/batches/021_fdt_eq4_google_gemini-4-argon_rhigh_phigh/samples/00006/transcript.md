# 021_fdt_eq4_google_gemini-4-argon_rhigh_phigh / 00006

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/9fa2f595-ea8a-4a26-a981-3499d75701d2/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/9fa2f595-ea8a-4a26-a981-3499d75701d2/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Subjunctive Surgery and Updateless Choice: A Mathematical Guide to Action Functional Decision Theory (A-FDT)

For nearly half a century, normative decision theory has been divided between two competing accounts of instrumental rationality: **Evidential Decision Theory (EDT)** and **Causal Decision Theory (CDT)**. When measured by the benchmark of average utility achieved across decision problems, neither theory dominates the other. EDT reliably walks away rich in Newcomb’s problem and achieves mutual cooperation in the psychological twin prisoner’s dilemma, yet it is easily exploited in common-cause environments like the smoking lesion problem or the XOR blackmail dilemma. Conversely, CDT makes the sensible choice in common-cause environments, but systematically settles for poverty in Newcomb’s problem, mutual defection against a psychological twin, and paralysis or self-defeating choices in dilemmas like *Death in Damascus*.

In *"Functional Decision Theory: A New Theory of Instrumental Rationality"* (2017), Eliezer Yudkowsky and Nate Soares propose a unified framework designed to capture the strengths of both theories while avoiding their respective pathologies. Their core philosophical move is to shift the locus of decision-making from a physical *token* (the bodily act executed at a specific moment in spacetime) to a mathematical *type* (the logical output of a fixed decision function). As they summarize the principle, a rational agent should treat her decision as the output of a fixed mathematical function that answers the question: *"Which output of this very function would yield the best outcome?"*

While Yudkowsky and Soares use the umbrella term "Functional Decision Theory (FDT)" throughout their paper, they note in Footnotes 7 and 16 that a functional decision theorist can formalize the decision function either as selecting a full *policy* (mapping observations to actions) or as selecting an individual *action* for a given observation. In the main body of their paper—specifically in **Equation (4) of Section 5**—they formalize and apply the action-selecting version. In this essay, we will refer to the formal theory defined by Equation (4) as **Action Functional Decision Theory (A-FDT)**, distinguishing it explicitly from **Policy Functional Decision Theory (P-FDT)** as well as from **CDT**, **EDT**, **Timeless Decision Theory (TDT)**, and **Updateless Decision Theory (UDT)**.

Our goal is twofold: first, to provide a mathematically precise exposition of **A-FDT** and the mechanics of its counterfactual evaluations; and second, to give a step-by-step operational recipe that allows a reader to apply **A-FDT** to novel, unfamiliar decision problems, clearly separating what is settled by Yudkowsky and Soares (2017) from the additional modeling assumptions required in practice.

---

## 1. The Formal Architecture of A-FDT

### 1.1 Expected Utility and Epistemic Perspectives

Following the framework of Gibbard and Harper (1978) and the representation theorem of Joyce (1999), **EDT**, **CDT**, and **A-FDT** all share a common foundation: they are expected utility theories. Let $\mathcal{A}$ be a finite set of available actions, $\mathcal{X}$ a countable set of possible observation histories, and $\mathcal{O} = \{o_1, o_2, \dots\}$ a countable set of outcomes. Let $\mathcal{U}: \mathcal{O} \to \mathbb{R}$ be a bounded utility function. Given an observation history $x \in \mathcal{X}$, an expected utility maximizer selects an action $a \in \mathcal{A}$ that maximizes:

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j) \tag{1}$$

where $P(a \hookrightarrow o_j ;\, x)$ denotes the probability assigned to outcome $o_j$ in the hypothetical scenario where action $a$ is taken after observing $x$. As Joyce (1999) observes, *"decision theories should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated."*

In algorithmic terms, an agent maintains an internal world-model $M$. To evaluate each candidate action $a \in \mathcal{A}$, the agent performs a formal operation on $M$ to construct a transient computational object $M^{a\hookrightarrow}$—the *hypothetical for $a$*—and computes the expected value of the utility random variable $\textsc{V} \coloneqq \mathcal{U}(\textsc{Outcome})$ within that hypothetical. The competing decision theories differ exclusively in how they represent $M$ and how they construct $M^{a\hookrightarrow}$.

### 1.2 From EDT and CDT to Equation (4) of A-FDT

To see what **A-FDT** changes, let us place the three formal decision rules side by side. Let $\textsc{Obs}$, $\textsc{Act}$, $\textsc{Outcome}$, and $\textsc{V}$ be random variables representing the agent's observation, physical action, outcome, and utility, respectively.

1. **Evidential Decision Theory (EDT)** represents the world-model purely as a Bayesian probability distribution $P$. It constructs hypotheticals via standard conditionalization on both the observation $x$ and the physical action $a$:
   $$\mathrm{EDT}(P, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs}=x, \textsc{Act}=a\right) \tag{2}$$
   (where actions $a$ with $P(\textsc{Act}=a \mid \textsc{Obs}=x) = 0$ are excluded).

2. **Causal Decision Theory (CDT)**, formalized using Pearl’s (1996, 2000) graphical causal models, represents the world-model as a pair $M = (P, G)$, where $G$ is a directed acyclic graph (DAG) encoding causal dependencies among the variables of $P$. CDT constructs hypotheticals by conditioning on the observation $x$ and performing a causal intervention $\mathtt{do}(\textsc{Act}=a)$, which severs all incoming edges to $\textsc{Act}$ in $G$, sets $\textsc{Act}=a$, and propagates the update strictly to nodes causally downstream of $\textsc{Act}$:
   $$\mathrm{CDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x\right) \tag{3}$$

3. **Action Functional Decision Theory (A-FDT)** also represents the world-model as a pair $M = (P, G)$, but broadens the scope of both $P$ and $G$. In **A-FDT**, $P$ includes variables representing the outputs of mathematical functions and logical computations, and $G$ encodes not merely physical causation, but *subjunctive dependence*—the structural, logical, and computational relationships describing how physical and informational systems covary with the output of a mathematical function. In **Equation (4) of Section 5**, Yudkowsky and Soares define the decision rule (written there as $\mathrm{FDT}$, and which we denote $\mathrm{A\text{-}FDT}$ to specify its action-evaluating form) as:
   $$\mathrm{A\text{-}FDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{a-fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right) \tag{4}$$
   *(Note: In the source text’s Equation (4), the function and node are denoted $\mathrm{FDT}$ and $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$; we use $\mathrm{A\text{-}FDT}$ and $\textsc{a-fdt}(\underline{P}, \underline{G}, \underline{x})$ consistently to distinguish this action-level rule from policy-level variants.)*

### 1.3 Dequoting, Self-Reference, and the Two Core Innovations of A-FDT

Equation (4) is remarkably compact, but every symbol inside the $\mathtt{do}(\cdot)$ operator is doing heavy conceptual work:

* **Function vs. Node**: We must distinguish $\mathrm{A\text{-}FDT}(P, G, x)$, which is the mathematical function the agent is executing to produce an action, from $\textsc{a-fdt}(\underline{P}, \underline{G}, \underline{x})$, which is a *random variable inside the agent's probability distribution $P$* representing the agent's epistemic uncertainty or structural representation of what that function outputs on inputs $(P, G, x)$.
* **Dequoting ($\underline{P}, \underline{G}, \underline{x}$)**: The underlines denote dequotation. If the variable $x$ currently holds the value $\textit{full}$, then $\textsc{a-fdt}(\underline{P}, \underline{G}, \underline{x})$ resolves to the specific variable name $\textsc{a-fdt}(\underline{P}, \underline{G}, \textit{full})$ within the graph $G$.
* **Harmless Self-Reference**: Because the variable $\textsc{a-fdt}(\underline{P}, \underline{G}, \underline{x})$ is an element of the model $(P, G)$ whose name depends on $(P, G)$, the model is self-referential. As the authors note, Kleene’s (1938) second recursion theorem guarantees via "quining" that computational data structures can contain accurate representations of their own source code without paradox. Moreover, the agent does not need to know the *value* of $\mathrm{A\text{-}FDT}(P, G, x)$ in advance in order to perform graph surgery on the *node* $\textsc{a-fdt}(\underline{P}, \underline{G}, \underline{x})$.

Comparing Equation (3) for **CDT** and Equation (4) for **A-FDT** reveals the two fundamental mathematical innovations of **A-FDT**:

1. **Intervention on the Logical Type Rather Than the Physical Token**: **CDT** intervenes on $\textsc{Act}$, breaking the link between the agent's physical action and any upstream causes or predictors. **A-FDT** intervenes on the logical output node $\textsc{a-fdt}(\underline{P}, \underline{G}, \underline{x})$. Both the agent’s physical action $\textsc{Act}$ and any external system that accurately predicts, simulates, or mirrors the agent's decision procedure sit *downstream* of $\textsc{a-fdt}(\underline{P}, \underline{G}, \underline{x})$ in $G$. As Yudkowsky and Soares write: *"Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."*
2. **Updateless Response to Observations**: Notice that in Equation (4), **there is no conditioning on $\textsc{Obs} = x$**. When an **A-FDT** agent observes $x$, she does not restrict her probability space to worlds where $\textsc{Obs} = x$. Instead, she uses $x$ to *select which logical node in $G$ to intervene upon*—intervening on $\textsc{a-fdt}(\underline{P}, \underline{G}, \underline{x})$ rather than $\textsc{a-fdt}(\underline{P}, \underline{G}, \underline{y})$. Because she evaluates expectations across the *entire* prior distribution $P$ under the surgery $\mathtt{do}(\textsc{a-fdt}(\underline{P}, \underline{G}, \underline{x}) = a)$, her hypotheticals allow for the possibility that if her decision algorithm had output a different action for observation $x$, a predictor would have foreseen this and she would never have observed $x$ in the first place. (This mechanism is inherited from Wei Dai's (2009) **Updateless Decision Theory (UDT)**, and avoids the harmful "double updating" of Yudkowsky's (2010) **Timeless Decision Theory (TDT)**, which both conditioned on evidence and changed the locus of intervention.)

When no external variables correlate with $\textsc{Act}$ except its causal descendants (and $\textsc{a-fdt}(\underline{P}, \underline{G}, \underline{x})$ itself), the three theories coincide:
$$\mathbb{E}[\textsc{V} \mid a] = \mathbb{E}[\textsc{V} \mid \mathtt{do}(a)] = \mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{a-fdt}(\underline{P}, \underline{G}, \underline{x})=a)].$$
They diverge sharply whenever the environment contains common causes, predictors, or copies.

---

## 2. Applying A-FDT to Classic Dilemmas

To see how Equation (4) operates as a concrete mathematical algorithm, let us trace how an **A-FDT** agent ("Fiona") constructs her graph $G^F$ and probability distribution $P^F$ across three canonical structural templates, contrasting her calculations with an **EDT** agent ("Eve") and a **CDT** agent ("Carl").

### 2.1 Basic Subjunctive Coupling: Newcomb’s Problem

In Newcomb’s problem (Nozick, 1969), a predictor with accuracy $99\%$ places $\$1,000,000$ in opaque Box B ($\textsc{Box B} = \textit{full}$) if and only if she predicts the agent will leave behind transparent Box A containing $\$1,000$ ($\textsc{Act} = \textit{onebox}$); otherwise $\textsc{Box B} = \textit{empty}$. There is no observation prior to choosing, so we omit $x$.

* **CDT’s Graph ($G^C$)**: Carl models a node $\textsc{Predisposition}$ as a common cause with arrows $\textsc{Predisposition} \to \textsc{Act}$ and $\textsc{Predisposition} \to \textsc{Prediction} \to \textsc{Box B}$. When Carl evaluates $\mathtt{do}(\textsc{Act}=a)$, he severs $\textsc{Predisposition} \to \textsc{Act}$. Consequently, $P^C(\textsc{Box B}=\textit{full} \mid \mathtt{do}(\textsc{Act}=a)) = p$ is held constant across both hypotheticals. Since $p(\$1,001,000) + (1-p)(\$1,000) > p(\$1,000,000)$, Carl two-boxes and receives $\$1,000$.
* **A-FDT’s Graph ($G^F$)**: Fiona replaces $\textsc{Predisposition}$ with the logical output node $\textsc{a-fdt}(\underline{P^F}, \underline{G^F})$. Because both her physical body and the predictor’s simulation of her decision process subjunctively depend on this logical output, $G^F$ contains directed edges:
  $$\textsc{a-fdt}(\underline{P^F}, \underline{G^F}) \to \textsc{Act} \to \textsc{V}$$
  $$\textsc{a-fdt}(\underline{P^F}, \underline{G^F}) \to \textsc{Prediction} \to \textsc{Box B} \to \textsc{V}$$
  along with an exogenous noise node $\textsc{Accurate} \to \textsc{Prediction}$ where $P^F(\textsc{Accurate}=\textit{accurate}) = 0.99$.

The structural equations in $P^F$ are deterministic given $\textsc{a-fdt}(\underline{P^F}, \underline{G^F})$ and $\textsc{Accurate}$:
$$\textsc{Act}(d) = d, \qquad \textsc{Box B}(d, \textit{accurate}) = \begin{cases} \textit{full} & \text{if } d = \textit{onebox} \\ \textit{empty} & \text{if } d = \textit{twobox} \end{cases}$$
(and reversed if $\textsc{Accurate} = \textit{inaccurate}$). Applying Equation (4), Fiona evaluates:

1. **Hypothetical for $\textit{onebox}$**: Under $\mathtt{do}(\textsc{a-fdt}(\underline{P^F}, \underline{G^F}) = \textit{onebox})$, $\textsc{Act}$ becomes $\textit{onebox}$ with probability $1$, and $\textsc{Box B}$ becomes $\textit{full}$ with probability $0.99$:
   $$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{a-fdt}(\underline{P^F}, \underline{G^F}) = \textit{onebox})\right) = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000.$$
2. **Hypothetical for $\textit{twobox}$**: Under $\mathtt{do}(\textsc{a-fdt}(\underline{P^F}, \underline{G^F}) = \textit{twobox})$, $\textsc{Act}$ becomes $\textit{twobox}$ with probability $1$, and $\textsc{Box B}$ becomes $\textit{full}$ with probability $0.01$:
   $$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{a-fdt}(\underline{P^F}, \underline{G^F}) = \textit{twobox})\right) = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$

Since $\$990,000 > \$11,000$, $\mathrm{A\text{-}FDT}(P^F, G^F) = \textit{onebox}$. Notice also how this reframes dominance: while two-boxing dominates under **CDT** counterfactuals (which hold fixed the predictor's output while varying the physical act), one-boxing dominates under **A-FDT** counterfactuals (which hold fixed the predictor's *accuracy* while varying the decision function's output).

### 2.2 Context Uncertainty Without Predictor Coupling: The Smoking Lesion Problem

In Skyrms’ (1980) smoking lesion problem, an unobserved arterial lesion ($\textsc{Lesion} \in \{\textit{lesion}, \textit{nolesion}\}$) causes agents both to love smoking and, with $99\%$ probability, to develop fatal lung cancer (losing $\$1,000,000$ in utility). Agents without the lesion develop cancer with only $1\%$ probability. Smoking itself has no causal effect on cancer and grants $\$1,000$ in utility to those who love smoking.

Eve (**EDT**) conditions on $\textsc{Act}$, sees that $P^E(\textit{dead} \mid \textit{smoke}) = 0.99$ while $P^E(\textit{dead} \mid \textit{refrain}) = 0.01$, and refrains from smoking to avoid bad news. How does **A-FDT** avoid this trap when it intervenes on a high-level decision node?

Yudkowsky and Soares formalize the lesion’s effect on the agent's desires by introducing two possible world-models: $P^F_S$ (which uses utility function $\mathcal{U}_S$ valuing smoking at $+\$1,000$) and $P^F_R$ (which uses $\mathcal{U}_R$ valuing smoking at $-\$1$). If Fiona has the lesion, her physical brain runs $\mathrm{A\text{-}FDT}(P^F_S, G^F)$; if not, she runs $\mathrm{A\text{-}FDT}(P^F_R, G^F)$. Fiona does not introspectively observe which distribution she is running.

In Fiona’s graph $G^F$, $\textsc{Lesion}$ has a causal arrow to $\textsc{Cancer} \to \textsc{Death} \to \textsc{V}$, and also acts as a *multiplexer* switch on $\textsc{Act}$ alongside the two logical nodes $\textsc{a-fdt}(\underline{P^F_S}, \underline{G^F})$ and $\textsc{a-fdt}(\underline{P^F_R}, \underline{G^F})$:
$$\textsc{Act}(\textit{lesion}, s, r) = s, \qquad \textsc{Act}(\textit{nolesion}, s, r) = r.$$
Crucially, there is **no directed path** from $\textsc{a-fdt}(\underline{P^F_S}, \underline{G^F})$ to $\textsc{Lesion}$ or $\textsc{Cancer}$: a biological lesion does not simulate Fiona's decision function. Let $P^F_S(\textsc{Lesion} = \textit{lesion}) = p \in (0,1)$, and let $q = P^F_S(\textsc{a-fdt}(\underline{P^F_R}, \underline{G^F}) = \textit{smoke})$ be her prior belief that her non-lesion self would smoke. When Fiona (having the lesion) computes $\mathrm{A\text{-}FDT}(P^F_S, G^F)$, she intervenes on $\textsc{a-fdt}(\underline{P^F_S}, \underline{G^F})$:

* Under $\mathtt{do}(\textsc{a-fdt}(\underline{P^F_S}, \underline{G^F}) = \textit{smoke})$: With probability $p$, she has the lesion (yielding survival utility $0.01 \times \$1,000,000 = \$10,000$) and $\textsc{Act}$ is governed by $\textsc{a-fdt}(\underline{P^F_S}, \underline{G^F}) = \textit{smoke}$ (adding $+\$1,000$). With probability $1-p$, she lacks the lesion (yielding expected survival utility $0.99 \times \$1,000,000 = \$990,000$) and $\textsc{Act}$ is governed by $\textsc{a-fdt}(\underline{P^F_R}, \underline{G^F})$ (adding $q \cdot \$1,000$ under $\mathcal{U}_S$). Total expected utility:
  $$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{a-fdt}(\underline{P^F_S}, \underline{G^F}) = \textit{smoke})\right) = p(\$10,000 + \$1,000) + (1-p)(\$990,000 + q\$1,000).$$
* Under $\mathtt{do}(\textsc{a-fdt}(\underline{P^F_S}, \underline{G^F}) = \textit{refrain})$: The $(1-p)$ branch is identical, while the $p$ branch loses the $\$1,000$ smoking benefit:
  $$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{a-fdt}(\underline{P^F_S}, \underline{G^F}) = \textit{refrain})\right) = p(\$10,000) + (1-p)(\$990,000 + q\$1,000).$$

The difference is strictly positive ($+p \cdot \$1,000$), so Fiona smokes. Because $G^F$ distinguishes between a predictor (which lies downstream of the $\textsc{a-fdt}$ node) and a statistical common cause (which does not), **A-FDT** one-boxes in Newcomb's problem and smokes in the smoking lesion problem without ad-hoc adjustments.

### 2.3 Updateless Choice Under Observation: Transparent Newcomb and Mechanical Blackmail

The most striking consequences of **A-FDT** arise when the agent makes an observation $x$ before acting, as in Drescher’s (2006) **Transparent Newcomb Problem** ( structurally isomorphic to Parfit’s (1986) hitchhiker problem) and Soares and Fallenstein’s (2015) **Mechanical Blackmail Problem**.

In the Transparent Newcomb Problem, both boxes are transparent. The $99\%$-accurate predictor fills Box B with $\$1,000,000$ if and only if she predicts that the agent will one-box *upon observing that Box B is full*. Suppose the agent walks into the room and sees $\textsc{Obs} = \textit{full}$. Both **CDT** and **EDT** condition on $\textsc{Obs} = \textit{full}$; once $\textsc{Box B} = \textit{full}$ is fixed by conditioning, taking both boxes yields $\$1,001,000$ whereas one-boxing yields $\$1,000,000$. Consequently, both **CDT** and **EDT** agents two-box—and because the predictor foresees this, **CDT** and **EDT** agents almost always see an empty Box B and walk away with $\$1,000$.

Now consider how Fiona (**A-FDT**) models the problem. Her graph $G^F$ contains two logical decision nodes corresponding to the two possible observations: $\textsc{a-fdt}(\underline{P^F}, \underline{G^F}, \textit{full})$ and $\textsc{a-fdt}(\underline{P^F}, \underline{G^F}, \textit{empty})$. Because the predictor specifically simulates what Fiona will do *if she sees a full box*, the predictor’s node depends only on $\textsc{a-fdt}(\underline{P^F}, \underline{G^F}, \textit{full})$ and $\textsc{Accurate}$:
$$\textsc{Prediction} = \begin{cases} 1 & \text{if } (\textsc{a-fdt}(\underline{P^F}, \underline{G^F}, \textit{full}) = \textit{onebox} \land \textsc{Accurate}=\textit{accurate}) \\ & \quad \lor\; (\textsc{a-fdt}(\underline{P^F}, \underline{G^F}, \textit{full}) = \textit{twobox} \land \textsc{Accurate}=\textit{inaccurate}) \\ 2 & \text{otherwise.} \end{cases}$$
Meanwhile, $\textsc{Box B}$ is $\textit{full}$ if $\textsc{Prediction} = 1$ and $\textit{empty}$ if $\textsc{Prediction} = 2$. Finally, $\textsc{Prediction}$ acts as the observation switch determining which of the two logical nodes controls Fiona’s physical action $\textsc{Act}$:
$$\textsc{Act}(d_{\textit{full}}, d_{\textit{empty}}, \textsc{Prediction}) = \begin{cases} d_{\textit{full}} & \text{if } \textsc{Prediction} = 1 \text{ (she sees } \textit{full}\text{)} \\ d_{\textit{empty}} & \text{if } \textsc{Prediction} = 2 \text{ (she sees } \textit{empty}\text{).} \end{cases}$$

When Fiona sees $\textsc{Obs} = \textit{full}$, Equation (4) instructs her to maximize:
$$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{a-fdt}(\underline{P^F}, \underline{G^F}, \textit{full}) = a\right)\right).$$
*(Mathematical note on the source text: In Section 6 of Yudkowsky and Soares (2017), the unnumbered display formula introducing this step contains a typographical error—a missing closing parenthesis and a stray ", $\textsc{Obs}=\textit{full}$"—that momentarily resembles CDT’s Equation (3). However, both Equation (4) in Section 5 and the authors' immediately following algebraic derivation confirm that Fiona does **not** condition on $\textsc{Obs}=\textit{full}$; she averages over both the $\textsc{Accurate}=\textit{accurate}$ and $\textsc{Accurate}=\textit{inaccurate}$ branches.)*

Let $q = P^F(\textsc{a-fdt}(\underline{P^F}, \underline{G^F}, \textit{empty}) = \textit{twobox})$ be Fiona's prior probability that she two-boxes if she sees an empty box (which equals $1$ upon reflection). Let us trace the two interventions:

1. **Intervening $\mathtt{do}(\textsc{a-fdt}(\underline{P^F}, \underline{G^F}, \textit{full}) = \textit{onebox})$**:
   * With probability $0.99$ ($\textsc{Accurate}=\textit{accurate}$), $\textsc{Prediction}=1$, so $\textsc{Box B}=\textit{full}$ and $\textsc{Act} = \textit{onebox}$, yielding $\$1,000,000$.
   * With probability $0.01$ ($\textsc{Accurate}=\textit{inaccurate}$), $\textsc{Prediction}=2$, so $\textsc{Box B}=\textit{empty}$ and $\textsc{Act}$ is governed by $\textsc{a-fdt}(\underline{P^F}, \underline{G^F}, \textit{empty})$, yielding $q \cdot \$1,000$ in expectation.
   * **Expected Utility**: $0.99(\$1,000,000) + 0.01(q \cdot \$1,000) = \$990,000 + \$10q$.

2. **Intervening $\mathtt{do}(\textsc{a-fdt}(\underline{P^F}, \underline{G^F}, \textit{full}) = \textit{twobox})$**:
   * With probability $0.01$ ($\textsc{Accurate}=\textit{inaccurate}$), $\textsc{Prediction}=1$, so $\textsc{Box B}=\textit{full}$ and $\textsc{Act} = \textit{twobox}$, yielding $\$1,001,000$.
   * With probability $0.99$ ($\textsc{Accurate}=\textit{accurate}$), $\textsc{Prediction}=2$, so $\textsc{Box B}=\textit{empty}$ and $\textsc{Act}$ is governed by $\textsc{a-fdt}(\underline{P^F}, \underline{G^F}, \textit{empty})$, yielding $q \cdot \$1,000$ in expectation.
   * **Expected Utility**: $0.01(\$1,001,000) + 0.99(q \cdot \$1,000) = \$10,010 + \$990q$.

Even though Fiona is currently staring at a full Box B, her hypothetical for $\textit{twobox}$ assigns $99\%$ probability to the scenario in which she never saw the full box at all! Because $\$990,000 + \$10q > \$10,010 + \$990q$ for all $q \in [0,1]$, she leaves the $\$1,000$ behind.

The exact same updateless mechanics govern the **Mechanical Blackmail Problem** (Section 9 of the source). A blackmailer launches a self-incriminating software program (costing both parties $\$1,000,000$ unless the agent wires $\$1,000$) if and only if she predicts the agent will pay upon receiving the blackmail notice. Suppose the blackmailer has a false-positive rate $\epsilon$: when the agent’s algorithm outputs $\textit{refuse}$, the blackmailer mistakenly predicts $\textit{pay}$ and launches the program with probability $\epsilon$. Assuming the blackmailer never errs when the agent outputs $\textit{pay}$, an **A-FDT** agent holding the blackmail letter compares:
$$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{a-fdt}(\underline{P^F}, \underline{G^F}, \textit{blackmail}) = \textit{pay})\right) = -\$1,000$$
$$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{a-fdt}(\underline{P^F}, \underline{G^F}, \textit{blackmail}) = \textit{refuse})\right) = \epsilon(-\$1,000,000) + (1-\epsilon)(\$0).$$
When $\epsilon = 0.0009$ ($0.09\%$), refusing has an expected utility of $-\$900 > -\$1,000$, so Fiona refuses to pay even while holding the letter, knowing she is in the $0.09\%$ error branch. If instead $\epsilon = 0.0011$ ($0.11\%$), refusing yields $-\$1,100 < -\$1,000$, and Fiona pays. In both regimes, **A-FDT** selects the exact threshold policy that maximizes unconditional expected utility prior to the interaction, without needing costly precommitment devices or temporal self-modification.

---

## 3. Diagnostic Power: Why EDT and CDT Fail Where A-FDT Succeeds

The formal contrast between Equations (2), (3), and (4) allows Yudkowsky and Soares to diagnose the failure modes of **EDT** and **CDT** with surgical precision: **EDT** preserves too many correlations in its hypotheticals, whereas **CDT** preserves too few.

### 3.1 EDT’s Vulnerability: Statistical Exploitation

Because **EDT** forms hypotheticals via Bayesian conditionalization $P(\cdot \mid \textsc{Obs}=x, \textsc{Act}=a)$, it cannot sever *any* correlation between the agent's action and the environment, even when that correlation is purely statistical or adversarially engineered.

In the **Cosmic Ray Problem**, an agent chooses between taking $\$1$ or $\$100$, knowing that with vanishingly small probability a cosmic ray flips her decision (requiring a $\$1,000$ hospital check-up). If Eve (**EDT**) initially believes she almost certainly takes $\$1$, then conditioning on $\textsc{Act}=\textit{take \$100}$ forces her to conclude she was struck by a cosmic ray, yielding $\$100 - \$1,000 = -\$900 < \$1$. Her belief becomes self-fulfilling.

Even more damningly, in the **XOR Blackmail Problem** (Soares & Fallenstein, 2015), an honest predictor knows whether the agent’s house has a $\$1,000,000$ termite infestation and sends a letter asking for $\$1,000$ if and only if *either* (i) there are no termites and the agent will pay, *or* (ii) there are termites and the agent will refuse. Neither Eells' (1984) tickle defense nor Jeffrey's (1983) ratification can save Eve here: conditional on $\textsc{Obs}=\textit{letter}$ and $\textsc{Act}=\textit{pay}$, the probability of termites is $0$; conditional on $\textsc{Obs}=\textit{letter}$ and $\textsc{Act}=\textit{refuse}$, the probability of termites is $1$. Eve pays $\$1,000$ for completely fabricated "good news."

Fiona (**A-FDT**), by contrast, intervenes on $\textsc{a-fdt}(\underline{P^F}, \underline{G^F}, \textit{letter})$. In her graph $G^F$, changing $\textsc{a-fdt}(\underline{P^F}, \underline{G^F}, \textit{letter})$ from $\textit{refuse}$ to $\textit{pay}$ changes whether the predictor sends the letter (switching whether she receives the letter in the $\textit{termites}$ vs. $\textit{no termites}$ states), but has **zero effect** on the upstream node $\textsc{Infestation}$. With $P^F(\textsc{Infestation}=\textit{termites}) = p$ invariant across both hypotheticals, refusing dominates paying.

### 3.2 CDT’s Vulnerability: Impossible Interventions and Reflective Instability

**CDT** fails in the opposite direction: by intervening only on the physical token $\textsc{Act}$, Carl’s hypotheticals stipulate that predictors who are known to be $100\%$ accurate magically make errors whenever Carl contemplates an alternative action.

This mismatch between factual beliefs and decision-theoretic hypotheticals becomes catastrophic in **Death in Damascus** (Gibbard & Harper, 1978). Death predicts perfectly whether the agent will stay in Damascus or pay $\$1,000$ to flee to Aleppo, and waits at the predicted city to claim the agent's life (worth $\$1,000,000$). Because Carl (**CDT**) holds Death’s location fixed when evaluating $\mathtt{do}(\textsc{Act}=a)$, believing he will stay makes fleeing look optimal, and believing he will flee makes staying look optimal.

If Carl uses Joyce’s (2012) ratification procedure with a pseudorandom coin (which Death still predicts perfectly), he settles into a mixed equilibrium $P^C_\ast(\textit{damascus}) = 0.5005$ and $P^C_\ast(\textit{aleppo}) = 0.4995$, where the $\$1,000$ travel cost balances the $0.1\%$ survival differential. Worse still, because Carl’s **CDT** hypotheticals treat Death’s location as independent of his current choice, he evaluates his survival probability under his own choice as $\max(p, 1-p) \ge 0.5$ (or $\$500,500$ in expected utility). If offered a *truly random* quantum coin for $\$1$ that genuinely thwarts Death $50\%$ of the time (expected utility $\$500,000 - \$1 = \$499,999$), Carl refuses to buy it!

Fiona (**A-FDT**) suffers no such delusion. In her graph $G^F$, $\textsc{a-fdt}(\underline{P^F}, \underline{G^F})$ points to both $\textsc{Act}$ and Death's appointment book $\textsc{Prediction}$. Under $\mathtt{do}(\textsc{a-fdt}(\underline{P^F}, \underline{G^F}) = \textit{damascus})$, she dies in Damascus with utility $\$0$; under $\mathtt{do}(\textsc{a-fdt}(\underline{P^F}, \underline{G^F}) = \textit{aleppo})$, she dies in Aleppo with utility $-\$1,000$. She stays in Damascus, saves $\$1,000$, and if offered the $\$1$ truly random coin (which severs the edge to $\textsc{Prediction}$), she gladly buys it to jump from $\$0$ to $\$499,999$ in expected utility.

---

## 4. Open Questions and an Operational Recipe for Unfamiliar Cases

Yudkowsky and Soares (2017) explicitly leave two major technical questions open. To help readers apply **A-FDT** to unfamiliar problems, we will first explain what the source text leaves unresolved and then develop a concrete operational interpretation of our own, clearly distinguishing the paper's claims from our proposed extensions.

### 4.1 Open Problems in Yudkowsky and Soares (2017)

1. **Deducing the Subjunctive Graph $G$ and Evaluating Counterpossibles (Sections 3 & 5)**:
   If $\mathrm{A\text{-}FDT}(P, G, x)$ is a deterministic mathematical function that actually outputs $\textit{cooperate}$, then the hypothesis $\textsc{a-fdt}(\underline{P}, \underline{G}, \underline{x}) = \textit{defect}$ is a *counterpossible*—a counterfactual with a logically impossible antecedent, analogous to asking what would happen if $6288 + 1048 \neq 7336$. While Yudkowsky and Soares note that an idealized theory $\mathrm{FDT}^*$ might use a logical conditioning operator $\mathtt{true}(\phi)$, no formal definition of $\mathtt{true}(\phi)$ currently exists. Equation (4) bypasses this by assuming the graph $G$ is given as an input and applying Pearl’s $\mathtt{do}(\cdot)$ operator. However, whereas Pearl (2000) provides a rigorous methodology for learning causal graphs from physical interventions, the authors emphasize that *"figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."*

2. **Action-Level (A-FDT) vs. Policy-Level (P-FDT) Evaluation (Footnotes 7 & 16)**:
   As noted earlier, Equation (4) intervenes on the single observation-specific variable $\textsc{a-fdt}(\underline{P}, \underline{G}, \underline{x})$ to choose an action $a \in \mathcal{A}$. In Footnotes 7 and 16, the authors remark that in their preferred formalization, the agent instead intervenes on a single unindexed node $\textsc{fdt}(\underline{P}, \underline{G})$ to select an entire *policy* $\pi: \mathcal{X} \to \mathcal{A}$, and then executes $\pi(x)$, noting that *"the difference only matters in multi-agent dilemmas so far as we can tell."* Because the paper does not formalize this difference, a practitioner facing a new multi-branch dilemma needs to know how Equation (4) behaves when outcomes depend on multiple observation branches simultaneously.

### 4.2 An Operational Recipe for Applying A-FDT to Unfamiliar Problems

*(Note: The following modeling procedure and worked example represent our own operational proposal for applying Equation (4) in practice, extending the framework of Yudkowsky and Soares (2017).)*

While philosophical counterpossibles in general mathematics are formidable, decision-making agents do not need to know how elliptic curves would behave if Fermat’s Last Theorem were false. They only need to model how physical and computational systems in their environment respond to the output of their own decision algorithm. We propose a four-step **Algorithmic Structural Modeling Recipe** to construct $(P, G)$ and evaluate **A-FDT** via Equation (4) on any unfamiliar finite decision problem:

* **Step 1 (Enumerate Information Contexts)**: Identify the finite set of distinguishable observation histories $\mathcal{X} = \{x_1, \dots, x_k\}$ the agent might hold at the moment of choice, and create a logical root node $D_{x_i} \coloneqq \textsc{a-fdt}(\underline{P}, \underline{G}, \underline{x_i})$ taking values in $\mathcal{A}$ for each $x_i \in \mathcal{X}$.
* **Step 2 (Wire Physical Action Execution)**: Model the agent’s physical action via a multiplexer structural equation:
  $$\textsc{Act} = \sum_{i=1}^k \mathbb{I}(\textsc{Obs} = x_i) \cdot D_{x_i}$$
  so that $\textsc{Obs}$ and $\{D_{x_1}, \dots, D_{x_k}\}$ are the parents of $\textsc{Act}$ in $G$. (If an unobserved physical state $C \in \mathcal{C}$ alters the agent's utility function, as in the smoking lesion problem, index the logical nodes $D_{c, x_i} = \textsc{a-fdt}(\underline{P_c}, \underline{G}, \underline{x_i})$ by $c$ as well.)
* **Step 3 (Criterion for Subjunctive Edges)**: For every external variable $Y$ in the environment (e.g., a predictor, a game-theoretic opponent, a lesion, or a natural state), draw a directed edge $D_{x_i} \to Y$ **if and only if** the physical mechanism generating $Y$ executes, simulates, proves theorems about, or evolved in game-theoretic best-response to an isomorphic copy or model of the agent’s decision rule evaluated at context $x_i$, modulated by an independent accuracy/noise variable $\textsc{Acc}_Y$. Never draw edges from $D_{x_i}$ to purely statistical common causes.
* **Step 4 (Updateless Surgery via Equation 4)**: Upon observing $x_{\text{actual}} \in \mathcal{X}$, do **not** condition $P$ on $\textsc{Obs} = x_{\text{actual}}$. Instead, for each $a \in \mathcal{A}$, set $D_{x_{\text{actual}}} = a$ via $\mathtt{do}(D_{x_{\text{actual}}} = a)$, marginalize over all exogenous states (including priors on $D_{x_j}$ for $j \neq \text{actual}$), and select the action maximizing $\mathbb{E}[\textsc{V} \mid \mathtt{do}(D_{x_{\text{actual}}} = a)]$.

### 4.3 Worked Unfamiliar Case: The Audited Sensor Dilemma

To test this recipe on a case not found in the paper—and to illuminate the boundary between **A-FDT** and **P-FDT**—consider the following novel dilemma:

> **Dilemma (The Audited Sensor Problem)**: An autonomous trading agent receives a noisy market signal $\textsc{Obs} \in \{\textit{high}, \textit{low}\}$ (each occurring with prior probability $0.5$ due to an exogenous market state $M \in \{\textit{bull}, \textit{bear}\}$). In each state, the agent can choose $\textsc{Act} \in \{\textit{aggressive}, \textit{conservative}\}$.
> * Directly from the market, $\textit{aggressive}$ yields $+\$10,000$ when $\textsc{Obs}=\textit{high}$ and $-\$10,000$ when $\textsc{Obs}=\textit{low}$, whereas $\textit{conservative}$ yields $\$0$ in both states.
> * However, before trading begins, a regulatory auditor simulates the agent’s code on **both** possible inputs ($\textit{high}$ and $\textit{low}$) with $100\%$ fidelity. If the auditor predicts that the agent will play $\textit{aggressive}$ in the $\textit{high}$ state **and** $\textit{conservative}$ in the $\textit{low}$ state—Wait: suppose instead the auditor is checking for *unconditional restraint*, and awards a $\$100,000$ compliance bonus ($\textsc{Bonus} = \$100,000$) if and only if the agent’s algorithm outputs $\textit{conservative}$ on **both** $\textit{high}$ and $\textit{low}$!

Let us apply our four-step **A-FDT** recipe when the agent observes $\textsc{Obs} = \textit{high}$:

1. **Nodes**: We introduce $D_{\textit{high}} \coloneqq \textsc{a-fdt}(\underline{P}, \underline{G}, \textit{high})$ and $D_{\textit{low}} \coloneqq \textsc{a-fdt}(\underline{P}, \underline{G}, \textit{low})$.
2. **Structural Equations**:
   * Market state $M \sim \text{Bernoulli}(0.5)$ determines $\textsc{Obs} \in \{\textit{high}, \textit{low}\}$.
   * Auditor bonus: $\textsc{Bonus} = \$100,000 \cdot \mathbb{I}(D_{\textit{high}} = \textit{conservative} \land D_{\textit{low}} = \textit{conservative})$.
   * Physical action: $\textsc{Act} = D_{\textsc{Obs}}$.
   * Total utility: $\textsc{V} = \textsc{Bonus} + \$10,000 \cdot \mathbb{I}(\textsc{Obs}=\textit{high} \land \textsc{Act}=\textit{aggressive}) - \$10,000 \cdot \mathbb{I}(\textsc{Obs}=\textit{low} \land \textsc{Act}=\textit{aggressive})$.

3. **Evaluating at $\textsc{Obs} = \textit{low}$ first**: If the agent observes $\textit{low}$, she intervenes on $D_{\textit{low}}$. Let $q_{\textit{high}} = P(D_{\textit{high}} = \textit{conservative})$.
   * $\mathbb{E}[\textsc{V} \mid \mathtt{do}(D_{\textit{low}} = \textit{conservative})] = \$100,000 \cdot q_{\textit{high}} + 0.5 \cdot (1 - q_{\textit{high}})(\$10,000) + 0.5(\$0)$.
   * $\mathbb{E}[\textsc{V} \mid \mathtt{do}(D_{\textit{low}} = \textit{aggressive})] = \$0 + 0.5 \cdot (1 - q_{\textit{high}})(\$10,000) + 0.5(-\$10,000)$.
   For *any* $q_{\textit{high}} \in [0,1]$, $\textit{conservative}$ strictly dominates at $\textsc{Obs}=\textit{low}$ (by $\$100,000 q_{\textit{high}} + \$5,000$). Thus, a reflectively coherent **A-FDT** agent knows with certainty that $D_{\textit{low}} = \textit{conservative}$, so $P(D_{\textit{low}} = \textit{conservative}) = 1$.

4. **Evaluating at $\textsc{Obs} = \textit{high}$**: Now suppose the agent observes $\textit{high}$. Knowing $P(D_{\textit{low}} = \textit{conservative}) = 1$, she applies Equation (4) to $D_{\textit{high}}$:
   * $\mathbb{E}[\textsc{V} \mid \mathtt{do}(D_{\textit{high}} = \textit{conservative})] = \$100,000 \cdot (1) + 0.5(\$0) + 0.5(\$0) = \$100,000.$
   * $\mathbb{E}[\textsc{V} \mid \mathtt{do}(D_{\textit{high}} = \textit{aggressive})] = \$0 + 0.5(\$10,000) + 0.5(\$0) = \$5,000.$

Because $\$100,000 > \$5,000$, **A-FDT** outputs $\textit{conservative}$ even when $\textsc{Obs}=\textit{high}$! Notice why: **CDT** and **EDT** both fail here (after observing $\textit{high}$, **CDT** treats the auditor's bonus as causally fixed in the past, and **EDT** only updates on the act at $\textit{high}$ unless coupled), whereas **A-FDT** succeeds because $D_{\textit{high}}$ is a parent of $\textsc{Bonus}$ and the agent holds an accurate belief $P(D_{\textit{low}} = \textit{conservative}) = 1$ about her other branch.

*Where, then, do **A-FDT** and **P-FDT** diverge?* Suppose the auditor rewarded coordination across two symmetric branches where neither branch had a dominant choice on its own—for instance, if the $\$100,000$ bonus required $D_{\textit{high}} = \textit{conservative}$ **and** a second symmetric branch $D_{\textit{high}'} = \textit{conservative}$, each sacrificing $+\$10,000$. Under **A-FDT** (Equation 4), because each intervention $\mathtt{do}(D_{x_i} = a)$ varies only $D_{x_i}$ while holding the prior $P(D_{x_j})$ on the other branch fixed, **A-FDT** would be sensitive to the prior $P(D_{x_j} = \textit{conservative})$: if the agent's prior assigned $P(D_{x_j} = \textit{conservative}) = 0$, unilateral restraint would appear useless (a coordination trap across observation branches). **Policy Functional Decision Theory (P-FDT)** eliminates this residual sensitivity to cross-branch priors by intervening on the entire policy $\pi = (D_{x_1}, \dots, D_{x_k})$ simultaneously. In all single-branch predictive dilemmas—or whenever cross-branch priors are reflectively anchored, as in our Audited Sensor Problem—**A-FDT** and **P-FDT** yield identical, utility-maximizing prescriptions.

---

## 5. Conclusion

**Action Functional Decision Theory (A-FDT)**, as formalized in Equation (4) of Yudkowsky and Soares (2017), resolves the classic impasse between **CDT** and **EDT** through two precise mathematical modifications to Pearl’s causal decision framework: it shifts the $\mathtt{do}(\cdot)$ intervention from the physical action token $\textsc{Act}$ to the logical decision-function output $\textsc{a-fdt}(\underline{P}, \underline{G}, \underline{x})$, and it responds to an observation $x$ not by Bayesian conditioning of the prior $P$, but by switching which observation-indexed logical node it intervenes upon. By preserving computational and predictive dependencies while severing spurious common-cause correlations, **A-FDT** achieves high utility across Newcomb's problem, the smoking lesion problem, Parfit's hitchhiker, blackmail dilemmas, and *Death in Damascus* using a single, reflectively stable rule. While open foundational problems remain—most notably the formalization of counterpossible conditionals and the empirical learning of subjunctive graphs—**A-FDT** provides a clear, operational blueprint for rational agency in worlds populated by predictors, replicators, and strategic peers.

---

## References

* Dai, W. (2009). Towards a new decision theory. *Less Wrong*.
* Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Eells, E. (1984). Metatickles and the dynamics of deliberation. *Theory and Decision*, 17(1), 71–95.
* Gibbard, A., & Harper, W. L. (1978). Counterfactuals and two kinds of expected utility. In *Foundations and Applications of Decision Theory* (Vol. 1). D. Reidel.
* Jeffrey, R. C. (1983). *The Logic of Decision* (2nd ed.). University of Chicago Press.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Joyce, J. M. (2012). Regret and instability in causal decision theory. *Synthese*, 187(1), 123–145.
* Kleene, S. C. (1938). On notation for ordinal numbers. *Journal of Symbolic Logic*, 3(4), 150–155.
* Nozick, R. (1969). Newcomb's problem and two principles of choice. In *Essays in Honor of Carl G. Hempel* (pp. 114–146). D. Reidel.
* Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
* Pearl, J. (1996). Causation, action, and counterfactuals. In *Proceedings of the 6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-96)* (pp. 51–73).
* Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Skyrms, B. (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Soares, N., & Fallenstein, B. (2015). Toward idealized decision theory. *arXiv preprint arXiv:1507.01986*.
* Yudkowsky, E. (2010). *Timeless Decision Theory*. The Singularity Institute.
* Yudkowsky, E., & Soares, N. (2017). Functional decision theory: A new theory of instrumental rationality. *arXiv preprint arXiv:1710.05060v2*.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Task**

I'm focusing on defining the scope and purpose: creating a math essay or tech blog post. I'm building on Yudkowsky and Soares' "Functional Decision Theory" article, figuring out what makes it an A-FDT-specific decision framework. I need to present its application to decision problems in a structured manner.


**Refining the Focus**

I've clarified the intended audience: mathematically savvy individuals keen on both the formalism and the underlying philosophy. I'm homing in on the core requirements now. Specifically, the goal is a detailed explanation of A-FDT's practical application, especially how the core equation works, which I will take as Equation 4 in Section 5 of the source. I'll maintain consistent use of "A-FDT" and distinctly identify other theories. I also plan to focus on its handling of dependencies and counterfactuals, resolving source ambiguities and clarifying my own additions.


**Determining Word Count & Scope**

I'm now determining the appropriate length and scope, aiming for roughly 2,400 to 3,000 words. My goal is a coherent explanation of A-FDT's core definitions, reasoning, and implications. I'm prioritizing clarity and completeness, avoiding unnecessary repetition or extraneous material. I'll include a concise conclusion. I am also working on clearly identifying the A-FDT formulation, which, after examining the source material, I'm identifying as action-based.


**Analyzing the Formalism**

I am now closely examining Equation (4) from Section 5. I realize the text uses "FDT" as a general term, but the equation specifically evaluates individual *actions*. I'm going to adopt "A-FDT" (Action Functional Decision Theory) for clarity. I'll make sure to consistently use A-FDT and distinct names for other decision theories. My focus is on clarifying its action-based nature. I will clearly explain this distinction in the writeup.


**Clarifying Notation & Context**

I'm now focusing on clear notation and context. My plan includes explicitly showing both $\text{A-FDT}(P, G, x)$ and $\text{FDT}(P, G, x)$ in Equation 4 to ensure source fidelity. I'm also planning to explicitly cover the core concepts behind A-FDT. I'm especially focused on the motivation for A-FDT: the tension between EDT and CDT. I'll describe how EDT respects too many correlations, while CDT respects too few. I am looking to clearly explain subjunctive dependence and type vs. token in relation to A-FDT as well.


**Defining Dependencies**

I'm presently clarifying the nature of subjunctive dependence within the A-FDT framework. I'm focusing on the computational and logical *type* output from the decision function, which is the key area for evaluation. Specifically, I'm working on how this relates to systems computing or predicting the same function subjunctively depending on that output. I'm also examining the formal setup, including the countable outcomes, finite actions, and bounded utility.


**Differentiating Theories**

I'm now identifying the key structural differences between CDT and A-FDT, especially the locus of intervention and treatment of observations. I am clarifying how I will treat observations, and how A-FDT does not condition P on Obs=x, but instead changes which logical node is intervened upon. I will be sure to address the specific differences in the formulation with both CDT and FDT.


**Elaborating on Analysis**

I'm currently focused on the specific mathematical inconsistencies in the original text, especially concerning the example in Section 6. I've pinpointed a crucial discrepancy: the source *doesn't* condition on $\textsc{Obs}=\textit{full}$ in Equation 4, even though this is implied in the immediate calculation. Highlighting this subtle difference, which requires averaging instead of conditioning on a specific observation, will provide a key insight into the practical application of A-FDT. I'm building this discrepancy into worked examples.



**Elaborating Examples**

I'm now detailing examples to illustrate A-FDT's core principles, especially its handling of observation-dependent interventions in scenarios like Transparent Newcomb and Mechanical Blackmail. I'm focusing on the expected utility algebra to demonstrate why an A-FDT agent one-boxes even when observing a full box, and analyzing the impact of predictor error thresholds. This will resolve any remaining confusions.


**Operationalizing Frameworks**

I'm now figuring out how to operationally define $(P, G)$ for practical application, especially in unfamiliar cases. I'm modelling bounded agents with structural computational graphs, or algorithmic causal models. Instead of needing complex counterfactual reasoning, I'm factoring in environment mechanisms and algorithmic execution nodes for predictors, simulations, or game theory.


**Refining Problem Scenarios**

I'm now focusing on scenarios where the intervention on actions $a$ versus $\mathcal{A}$ matters. I need to explain when the point-wise intervention $\mathtt{do}(\textsc{a-fdt}(\underline{P}, \underline{G}, \underline{x}) = a)$ suffices, and when a predictor cares about multiple observations. I'm preparing an "Asymmetric Information Twin Coordination Problem" to illustrate A-FDT's boundary.


**Planning the Word Count**

I'm now determining section word counts to stay on budget, targeting 2,650–2,800 total. I'm allotting 350 words to introduce the EDT/CDT rift and define A-FDT; 600 words for the formal architecture of expected utility, contrasting EDT, CDT, and A-FDT (Equation 4), covering subjunctive dependence and the *updateless* intervention; and 750 words to apply A-FDT to dilemmas like Newcomb's Problem and the Twin Prisoner's Dilemma. I'll need to define utility and probability functions for these.


**Structuring the Cases**

I am currently organizing the problem cases, starting with basic subjunctive coupling and A-FDT dominance. I'm moving on to handling unobserved context and utility uncertainty in the Smoking Lesion Problem via multiplexer nodes. I'll also present Transparent Newcomb and Mechanical Blackmail to showcase observation-indexed interventions and exact utility calculations.



**Refining Problem Cases**

I'm now prioritizing scenarios that highlight A-FDT's unique approach, specifically considering intervention at the action level versus the policy level, and preparing examples like the Audited Sensor Dilemma and Dual-Channel Coordination to illustrate this. I am carefully organizing the presentation, including how to handle the predictor's interactions across multiple observation branches. I'm ensuring consistency with the proper naming conventions and faithfully incorporating exact quotes from the source. I'm also planning the conclusion and references.


```
