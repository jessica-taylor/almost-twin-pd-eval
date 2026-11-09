# 021_fdt_eq4_google_gemini-4-argon_rhigh_phigh / 00009

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/b1a4cc52-3de1-49b2-93ba-45a974512afa/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/b1a4cc52-3de1-49b2-93ba-45a974512afa/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Intervening on the Algorithm: A Mathematical Guide to Action Functional Decision Theory (A-FDT)

## 1. Philosophical Motivation: The Dilemma of Counterfactuals

For half a century, normative decision theory was locked in a stalemate between two competing paradigms: **evidential decision theory (EDT)** and **causal decision theory (CDT)**. Measured by the average utility an agent achieves across decision problems, each theory triumphs where the other fails. 

In Nozick’s (1969) **Newcomb’s Problem**, an agent faces a transparent Box A containing $\$1,000$ and an opaque Box B containing either $\$1,000,000$ or $\$0$. A predictor with $99\%$ accuracy has already placed $\$1,000,000$ in Box B if and only if she predicted the agent would leave Box A behind ("one-boxing"). EDT prescribes one-boxing, because taking only Box B is overwhelming statistical evidence that Box B is full; EDT agents reliably walk away with $\$1,000,000$. CDT prescribes taking both boxes ("two-boxing"), reasoning that the predictor's action lies in the causal past: whatever is currently inside Box B, taking Box A yields an extra $\$1,000$. Predictably, CDT agents walk away with only $\$1,000$.

In Skyrms’s (1980) **Smoking Lesion Problem**, the fortunes reverse. An unobserved arterial lesion causes both a desire to smoke (worth $\$1,000$ in utility) and a $99\%$ chance of fatal lung cancer (whereas non-sufferers have a $1\%$ cancer rate, and survival is worth $\$1,000,000$). Smoking itself has no causal effect on cancer. CDT recognizes that smoking cannot cause the lesion and prescribes smoking, securing the extra $\$1,000$ of utility. Standard EDT prescribes refraining, because observing oneself smoke is grim statistical evidence of possessing the lethal lesion—a failure mode Lewis (1981) famously diagnosed as irrationally "managing the news."

Worse still, in sequential or observational prediction dilemmas such as **Parfit’s Hitchhiker** (Parfit 1986), the **Transparent Newcomb Problem** (Drescher 2006), and the **Mechanical Blackmail Problem** (Soares and Fallenstein 2015), *both* CDT and EDT fail to maximize utility. Once the driver has rescued the hitchhiker from the desert—or once the agent sees through a transparent Box B that the $\$1,000,000$ is already inside—both CDT and EDT advise defecting (refusing to pay the $\$1,000$ fee or taking both boxes). Foreseeing this via an accurate model of the agent, the driver leaves CDT and EDT agents to die in the desert, and the predictor leaves Box B empty.

To resolve these anomalies with a single coherent rule, Yudkowsky and Soares (2017) introduced functional decision theory. In their paper, they note that while one can formulate the theory by iterating over policies, their primary formal presentation in Section 5 evaluates individual actions via interventions on the output of the agent's decision function. In this essay, we call this formal framework **action functional decision theory (A-FDT)**. 

To see how **A-FDT** fits alongside EDT and CDT, recall that all three are expected utility theories. Following Gibbard and Harper (1978) and the representation theorem of Joyce (1999), any rational agent with coherent conditional preferences seeks to choose an action $a \in \mathcal{A}$ (a finite action set) after observing history $x \in \mathcal{X}$ (a countable observation set) that maximizes expected utility over a countable set of outcomes $\mathcal{O} = \{o_1, o_2, \dots\}$:

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j) \qquad \text{(Equation 1)}$$

Here $\mathcal{U}: \mathcal{O} \to \mathbb{R}$ is a bounded utility function, and $P(a \hookrightarrow o_j ;\, x)$ is the probability assigned to outcome $o_j$ under the hypothetical supposition that action $a$ is executed given observation $x$. As Joyce (1999) writes, "decision theories should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated."

The three theories diverge strictly in how they define the hypothetical connective "$\hookrightarrow$"—that is, how an agent modifies her world-model $M$ to construct a hypothetical distribution $M^{a\hookrightarrow}$ for each candidate action $a$:

* **EDT** equates hypothetical supposition with Bayesian conditionalization on physical action $\textsc{Act}=a$ and observation $\textsc{Obs}=x$. Writing $\textsc{V} \coloneqq \mathcal{U}(\textsc{Outcome})$, EDT selects:
  $$\mathrm{EDT}(P, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs}=x, \textsc{Act}=a\right) \qquad \text{(Equation 2)}$$
  where actions with prior probability $0$ are excluded.
* **CDT** augments $P$ with a directed acyclic graph (DAG) $G$ encoding physical causation (Pearl 1996, 2000). It conditions on $\textsc{Obs}=x$ and applies Pearl’s $\mathtt{do}$-operator to sever $\textsc{Act}$ from its causal ancestors while propagating effects to its causal descendants:
  $$\mathrm{CDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x\right) \qquad \text{(Equation 3)}$$

Why do both fail? EDT preserves *too many* correlations: conditioning on $\textsc{Act}=a$ retains purely statistical correlations with common causes (like the smoking lesion). CDT preserves *too few* correlations: intervening on the physical token $\textsc{Act}=a$ severs the correlation between the agent's decision and any environmental process—such as a psychological twin or an accurate predictor—that computes or simulates the very same decision procedure.

**A-FDT** repairs this by replacing purely causal dependence with **subjunctive dependence**. According to Yudkowsky and Soares (2017), when two physical systems compute the same mathematical function—like two well-functioning calculators on opposite sides of the globe computing $6288 + 1048$, or an agent and a predictor’s simulation of that agent—their outputs subjunctively depend on that shared mathematical function. Causal dependence is simply a special case of subjunctive dependence. In terms of Peirce’s (1934) type-token distinction, whereas CDT intervenes on the physical action *token* $\textsc{Act}$, **A-FDT** intervenes on the logical/computational *type*: the output of the mathematical decision function itself.

---

## 2. The Formalism of A-FDT

In Section 5 of Yudkowsky and Soares (2017), the primary formal definition of **A-FDT** (denoted $\mathrm{FDT}$ in the source equation) is given by **Equation (4)**:

$$\mathrm{FDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right) \qquad \text{(Equation 4)}$$

To apply **A-FDT** with mathematical precision, we must unpack every component of Equation (4) and contrast it with Equation (3).

### 2.1 Logical Variables, Dequoting, and Self-Reference

In an **A-FDT** agent’s world-model $M = (P, G)$, the probability distribution $P$ ranges not only over physical variables (such as $\textsc{Act}$, $\textsc{Box B}$, or $\textsc{Outcome}$), but also over variables representing the outputs of mathematical functions under logical uncertainty. For instance, $P$ may include a random variable for the sum $6288 + 1048$, concentrating probability mass near $1$ on $7336$.

Among these functional variables is $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$, which represents the logical output of the **A-FDT** algorithm when evaluated on the specific probability distribution $P$, dependency graph $G$, and observation $x$. Here, the underline notation denotes *dequoting* (syntactic substitution of values into variable identifiers): if $x \coloneqq 3$, then $\textsc{Z}\underline{x}$ denotes the variable name $\textsc{Z}3$. 

As the authors emphasize, it is crucial to distinguish between $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ and $\mathrm{FDT}(P, G, x)$:
1. $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ is a *node inside the agent's graphical model $G$* representing the output of her decision procedure, upon which she performs hypothetical surgery to evaluate candidate actions $a \in \mathcal{A}$.
2. $\mathrm{FDT}(P, G, x)$ is the *actual action output* returned by solving the $\operatorname*{argmax}$ in Equation (4).

Because the variable name $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ depends on $\underline{P}$ and $\underline{G}$, which themselves contain that variable, the model is self-referential. Yudkowsky and Soares note that this self-reference is benign: the agent does not need to know the *value* of $\mathrm{FDT}(P, G, x)$ in advance in order to include a node *representing* that value in $G$, and Kleene’s (1938) second recursion theorem guarantees via "quining" that computational data structures can contain and manipulate exact syntactic representations of themselves.

### 2.2 From Counterpossibles to Extended Graphical $\mathtt{do}$-Surgery

Because a deterministic mathematical function has a unique output on fixed inputs $(P, G, x)$ as a matter of logical necessity, asking "What if $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ output $a$ instead of $b$?" requires evaluating a **counterpossible conditional** (Cohen 1990)—a counterfactual whose antecedent is logically impossible, akin to asking how elliptic curves would behave if Fermat’s Last Theorem were false.

Ideally, one might wish to define a logical conditioning operator $\mathtt{true}(\phi)$ that updates a distribution $P$ directly on a logical sentence $\phi$, yielding an epistemic formulation $\mathrm{FDT}^*(P, x) = \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}(\textsc{V} \mid \mathtt{true}(\textsc{fdt}(\underline{P}, \underline{x}) = a))$. However, because no standard probability calculus yet exists for conditioning on logically false propositions, Equation (4) bypasses the need for a general $\mathtt{true}$ operator. Instead, **A-FDT** requires that the dependency structure of relevant counterpossibles be supplied explicitly as an augmented DAG $G$ encoding logical, mathematical, computational, and causal dependencies alike. Given $(P, G)$, Pearl’s graphical surgery operator $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)$ is well-defined:
1. Set the value of the node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ deterministically to $a$.
2. Sever all incoming edges to $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ (in all standard **A-FDT** graphs, this node is already a root node with no parents).
3. Propagate the value $a$ outward along all directed paths in $G$ using the structural equations/conditional distributions of $P$, leaving all variables not downstream of $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ untouched at their prior marginal distributions.

Whenever all correlations between $\textsc{Act}$ and other variables in $(P, G)$ are caused by $\textsc{Act}$ (except that $\textsc{Act}$ depends on $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$), Equations (2), (3), and (4) coincide:
$$\mathbb{E}[\textsc{V} \mid a] = \mathbb{E}[\textsc{V} \mid \mathtt{do}(a)] = \mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)].$$
They diverge precisely when non-causal correlations exist between $\textsc{Act}$ and the environment.

### 2.3 The Two Structural Pillars of Equation (4)

Comparing CDT’s Equation (3) with **A-FDT**’s Equation (4) reveals two profound mathematical differences:

1. **Intervention on the Function Node rather than the Physical Action Node**: CDT intervenes at $\mathtt{do}(\textsc{Act}=a)$, leaving predictors or twins upstream of $\textsc{Act}$ unaffected. **A-FDT** intervenes upstream at $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})=a)$, which simultaneously updates both the agent's physical act $\textsc{Act}$ and any external prediction or twin action that subjunctively depends on that computation.
2. **Observation-Indexed Intervention ("Updatelessness")**: Notice that in Equation (3), CDT conditions on the observation via $\textsc{Obs}=x$ on the right side of the conditioning bar. In Equation (4), **$\textsc{Obs}=x$ does not appear as a conditioning event**. Instead, when an **A-FDT** agent observes $x$, she incorporates $x$ by *changing which node in $G$ she intervenes upon*—switching her intervention target to $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$. As the paper notes, Wei Dai’s (2009) "Updateless Decision Theory" (UDT) inspired this mechanism, whereas Eliezer Yudkowsky’s (2010) earlier "Timeless Decision Theory" (TDT) both conditioned on $\textsc{Obs}=x$ and changed the intervention node, producing a harmful "double update." By omitting $\textsc{Obs}=x$ from the conditioning bar, **A-FDT** allows the agent to recognize that if $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ had output a different action $a'$, she might never have observed $x$ in the first place.

---

## 3. Applying A-FDT to Classic and Diagnostic Dilemmas

Let us trace how Equation (4) operates in practice across four diagnostic problem classes. Following the paper’s cast of characters, we compare Eve (EDT, Equation 2), Carl (CDT, Equation 3), and Fiona (**A-FDT**, Equation 4).

### 3.1 Standard Newcomb’s Problem and Subjunctive Dominance

In Newcomb’s Problem, there is no informative intermediate observation $x$, so we omit $\underline{x}$ and write Fiona’s intervention node as $\textsc{fdt}(\underline{P^F}, \underline{G^F})$. Her graphical model $G^F$ has the following directed edges:
* $\textsc{fdt}(\underline{P^F}, \underline{G^F}) \to \textsc{Act}$ and $\textsc{fdt}(\underline{P^F}, \underline{G^F}) \to \textsc{Prediction}$
* $\textsc{Accurate} \to \textsc{Prediction} \to \textsc{Box B}$
* $\textsc{Act} \to \textsc{V}$ and $\textsc{Box B} \to \textsc{V}$

Here $P^F(\textsc{Accurate} = \mathit{accurate}) = 0.99$. The structural equations specify that $\textsc{Act}$ copies $\textsc{fdt}(\underline{P^F}, \underline{G^F})$, while $\textsc{Prediction}$ matches $\textsc{fdt}(\underline{P^F}, \underline{G^F})$ when $\textsc{Accurate} = \mathit{accurate}$ and inverts it when $\textsc{Accurate} = \mathit{inaccurate}$. $\textsc{Box B}$ is $\mathit{full}$ ($\mathit{\$1,000,000}$) if $\textsc{Prediction} = \mathit{onebox}$, and $\mathit{empty}$ ($\mathit{\$0}$) otherwise.

Fiona evaluates Equation (4) over $\mathcal{A} = \{\mathit{onebox}, \mathit{twobox}\}$:
* **Hypothetical 1 ($\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{onebox})$)**: This sets $\textsc{Act} = \mathit{onebox}$ with probability $1$ and $\textsc{Box B} = \mathit{full}$ with probability $0.99$. Thus:
  $$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{onebox})\right) = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000.$$
* **Hypothetical 2 ($\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{twobox})$)**: This sets $\textsc{Act} = \mathit{twobox}$ with probability $1$ and $\textsc{Box B} = \mathit{full}$ with probability $0.01$. Thus:
  $$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{twobox})\right) = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$

Since $\$990,000 > \$11,000$, $\mathrm{FDT}(P^F, G^F) = \mathit{onebox}$. Notice that this calculation is completely independent of Fiona’s prior probability $P^F(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{onebox})$, because $\mathtt{do}$-surgery overwrites the node's prior. Even if Fiona already knows she is a one-boxer and is $99\%$ certain Box B is full, she does not deviate to two-boxing: under **A-FDT**, for her to two-box requires $\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{twobox}$, which subjunctively implies Box B is $99\%$ likely to be empty.

This also exposes why the traditional dominance argument for CDT is circular. Every decision theory induces its own dominance principle relative to its hypotheticals $M^{a\hookrightarrow}$. Holding fixed the subjunctive dependency $\textsc{Accurate}$ (whether the predictor erred), one-boxing yields $\$1,000,000$ vs. $\$1,000$ when the predictor is accurate, and $\$0$ vs. $\$1,001,000$ when inaccurate—so two-boxing does *not* dominate one-boxing under **A-FDT** counterfactuals.

### 3.2 The Smoking Lesion Problem: Uncertainty Over One's Own Model

In the Smoking Lesion Problem, no external agent predicts $\textsc{fdt}(-)$. However, the lesion causes the agent to enjoy smoking. Yudkowsky and Soares formalize this by introducing two utility functions: $\mathcal{U}_S$ (which values smoking at $+\$1,000$) and $\mathcal{U}_R$ (which values smoking at $-\$1$). Consequently, there are two possible distributions Fiona might be running: $P^F_S$ (using $\mathcal{U}_S$, when $\textsc{Lesion} = \mathit{lesion}$) and $P^F_R$ (using $\mathcal{U}_R$, when $\textsc{Lesion} = \mathit{nolesion}$). Because Fiona cannot introspectively observe whether she has the lesion, her graph $G^F$ contains *both* functional nodes: $\textsc{fdt}(\underline{P^F_S}, \underline{G^F})$ and $\textsc{fdt}(\underline{P^F_R}, \underline{G^F})$.

The edges of $G^F$ are:
* $\textsc{Lesion} \to \textsc{Cancer} \leftarrow \textsc{Luck}$, and $\textsc{Cancer} \to \textsc{Death} \to \textsc{V}$
* $\textsc{Lesion} \to \textsc{Act}$, $\textsc{fdt}(\underline{P^F_S}, \underline{G^F}) \to \textsc{Act}$, and $\textsc{fdt}(\underline{P^F_R}, \underline{G^F}) \to \textsc{Act}$, with $\textsc{Act} \to \textsc{V}$.

Specifically, $\textsc{Act}$ functions as a multiplexer gated by $\textsc{Lesion}$:
$$\textsc{Act}(\mathit{lesion}, s, r) \coloneqq s, \qquad \textsc{Act}(\mathit{nolesion}, s, r) \coloneqq r,$$
where $s = \textsc{fdt}(\underline{P^F_S}, \underline{G^F})$ and $r = \textsc{fdt}(\underline{P^F_R}, \underline{G^F})$. Let $p = P^F_S(\textsc{Lesion} = \mathit{lesion}) \in (0, 1)$, and let $q = P^F_S(\textsc{fdt}(\underline{P^F_R}, \underline{G^F}) = \mathit{smoke})$ be Fiona's prior probability that her non-lesion counterpart smokes. Given the $99\%$ cancer rate with the lesion and $1\%$ rate without it, expected survival utility is $\$10,000$ if $\textsc{Lesion} = \mathit{lesion}$ and $\$990,000$ if $\textsc{Lesion} = \mathit{nolesion}$.

When Fiona actually has the lesion, her cognitive system executes $\mathrm{FDT}(P^F_S, G^F)$, intervening on $\textsc{fdt}(\underline{P^F_S}, \underline{G^F})$. Crucially, neither $\textsc{Lesion}$ nor $\textsc{fdt}(\underline{P^F_R}, \underline{G^F})$ is downstream of $\textsc{fdt}(\underline{P^F_S}, \underline{G^F})$, so their probabilities $p$ and $q$ remain invariant under $\mathtt{do}(\textsc{fdt}(\underline{P^F_S}, \underline{G^F}) = a)$:
* **For $a = \mathit{smoke}$**:
  $$\mathbb{E}_S\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F_S}, \underline{G^F}) = \mathit{smoke}\right)\right] = p(\$10,000 + \$1,000) + (1-p)(\$990,000 + q \cdot \$1,000).$$
* **For $a = \mathit{refrain}$**:
  $$\mathbb{E}_S\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F_S}, \underline{G^F}) = \mathit{refrain}\right)\right] = p(\$10,000) + (1-p)(\$990,000 + q \cdot \$1,000).$$

Subtracting the two expectations, the $(1-p)$ terms cancel out completely, leaving a strict advantage of $p \cdot \$1,000 > 0$ for $\mathit{smoke}$. Thus **A-FDT** prescribes smoking in the Smoking Lesion Problem and one-boxing in Newcomb’s Problem via the exact same Equation (4).

### 3.3 Endogenous Observations: Transparent Newcomb, Parfit’s Hitchhiker, and Blackmail

The power of **A-FDT**’s second structural pillar—responding to observations by changing the intervention node rather than conditioning $P$—becomes clear in the **Transparent Newcomb Problem** (which is decision-theoretically isomorphic to **Parfit’s Hitchhiker**).

Suppose Box B is transparent, and the predictor places $\$1,000,000$ in Box B if and only if she predicts the agent will one-box *upon observing that Box B is full*. Both Eve (EDT) and Carl (CDT) condition on $\textsc{Obs} = \mathit{full}$:
$$\mathbb{E}(\textsc{V} \mid \textsc{Act}=\mathit{twobox}, \textsc{Obs}=\mathit{full}) = \mathbb{E}(\textsc{V} \mid \mathtt{do}(\textsc{Act}=\mathit{twobox}), \textsc{Obs}=\mathit{full}) = \$1,001,000 > \$1,000,000.$$
Thus both Eve and Carl two-box upon seeing a full box; foreseeing this, the predictor leaves Box B empty, and both get $\$1,000$. (Even worse, before looking at Box B, an EDT agent would pay to blindfold herself—assigning negative value to information!)

Now consider Fiona (**A-FDT**) when she observes $x = \mathit{full}$. Her graph $G^F$ contains two functional nodes corresponding to the two possible observations: $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$ and $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$. The predictor only cares what Fiona does when Box B is full, so the directed edges are:
* $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) \to \textsc{Prediction} \leftarrow \textsc{Accurate}$, with $\textsc{Prediction} \to \textsc{Box B}$
* $\textsc{Prediction} \to \textsc{Act}$, $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) \to \textsc{Act}$, and $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty}) \to \textsc{Act}$

Here $\textsc{Prediction} \in \{1, 2\}$ determines whether Box B is $\mathit{full}$ ($1$) or $\mathit{empty}$ ($2$), which in turn determines which observation Fiona receives and therefore which functional node governs her physical act $\textsc{Act}$:
$$\textsc{Act}(1, a_{\mathit{full}}, a_{\mathit{empty}}) \coloneqq a_{\mathit{full}}, \qquad \textsc{Act}(2, a_{\mathit{full}}, a_{\mathit{empty}}) \coloneqq a_{\mathit{empty}}.$$

Upon observing $x = \mathit{full}$, Fiona solves Equation (4) by intervening on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$ *without conditioning on $\textsc{Obs} = \mathit{full}$*. Let $q = P^F(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty}) = \mathit{twobox})$ be her prior probability that she would two-box if she saw an empty box:
* **Hypothetical 1 ($\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{onebox})$)**:
  With probability $0.99$ ($\textsc{Accurate} = \mathit{accurate}$), $\textsc{Prediction} = 1$, so $\textsc{Box B} = \mathit{full}$ and $\textsc{Act} = \mathit{onebox}$, yielding $\$1,000,000$. With probability $0.01$ ($\textsc{Accurate} = \mathit{inaccurate}$), $\textsc{Prediction} = 2$, so $\textsc{Box B} = \mathit{empty}$ and $\textsc{Act}$ is governed by $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$, yielding $q \cdot \$1,000$ in expectation. Total expected utility:
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{onebox}\right)\right] = 0.99(\$1,000,000) + 0.01(q \cdot \$1,000) = \$990,000 + \$10q.$$
* **Hypothetical 2 ($\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{twobox})$)**:
  With probability $0.01$ ($\textsc{Accurate} = \mathit{inaccurate}$), the predictor mispredicts one-boxing ($\textsc{Prediction} = 1$), so Fiona sees a full box, two-boxes, and gets $\$1,001,000$. With probability $0.99$ ($\textsc{Accurate} = \mathit{accurate}$), the predictor accurately foresees that she would two-box if shown a full box ($\textsc{Prediction} = 2$), and therefore leaves Box B empty! In that $99\%$ branch, Fiona actually observes an empty box and gets $q \cdot \$1,000$ in expectation. Total expected utility:
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{twobox}\right)\right] = 0.01(\$1,001,000) + 0.99(q \cdot \$1,000) = \$10,010 + \$990q.$$
  (Note that when $q=1$, this equals $\$11,000$, printed with a typographical comma shift as $\$110,00 + q \cdot \$990$ in Section 6 of the source text.)

For any $q \in [0, 1]$, $\$990,000 + \$10q > \$10,010 + \$990q$. Even while staring directly at $\$1,000,000$ in a transparent Box B, Fiona one-boxes! Why? Because when she imagines her $\mathit{full}$-observation algorithm outputting $\mathit{twobox}$, she imagines a counterfactual universe in which the predictor foresaw that output and never showed her a full box in the first place. 

The exact same updateless mechanics allow Fiona to defeat both the **XOR Blackmail** and the **Mechanical Blackmail** (Section 7 and Section 9 of the source). In the Mechanical Blackmail, a blackmailer launches an unstoppable mutual-destruction program (costing $\$1,000,000$ unless the agent wires $\$1,000$) if and only if she predicts the agent will pay upon receiving the blackmail notice. When Fiona receives the notice, she intervenes on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{blackmail})$. Under $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{blackmail}) = \mathit{refuse})$, the blackmailer predicts refusal and never launches the program, sending Fiona’s counterfactual probability of being blackmailed to $\approx 0$ (assuming predictor error $< 0.001$). Thus Fiona refuses to pay, is reflectively stable (never wishing to self-modify away from **A-FDT**), and is never blackmailed.

### 3.4 Death in Damascus: Reflective Stability Under Asymmetric Prediction

Finally, consider **Death in Damascus** (Gibbard and Harper 1978), where an infallible predictor (Death) travels to whichever city—Damascus or Aleppo—he predicts the agent will choose, causing the agent to die (losing $\$1,000,000$), while fleeing to Aleppo costs an extra $\$1,000$. 

Under CDT (Equation 3), $\textsc{Death’s Location}$ is treated as causally independent of $\textsc{Act}$. If Carl expects to stay in Damascus, CDT advises fleeing to Aleppo; if he expects to flee to Aleppo, CDT advises staying in Damascus. Even if Carl uses a ratification procedure (Arntzenius 2008; Joyce 2012) to mix at $p(\mathit{damascus}) = 0.5005$ and $p(\mathit{aleppo}) = 0.4995$, CDT’s hypotheticals evaluate his options *as if* Death's location were uncorrelated with his choice, leading Carl to act as though he already has a $50.05\%$ chance of survival ($\$500,500$ expected utility). Consequently, if offered a *genuinely* random quantum coin for $\$1$ that would truly thwart Death $50\%$ of the time (yielding $\$500,000 - \$1$), Carl absurdly refuses to buy it!

Under **A-FDT** (Equation 4), $\textsc{fdt}(\underline{P^F}, \underline{G^F}) \to \textsc{Death’s Location}$ and $\textsc{fdt}(\underline{P^F}, \underline{G^F}) \to \textsc{Act}$. Intervening on $\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{damascus}$ yields $\$0$ (certain death, no travel cost), whereas $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{aleppo})$ yields $-\$1,000$ (certain death plus travel cost). Fiona immediately stays in Damascus without deliberative loops, and would gladly pay $\$1$ for a genuinely random coin that breaks the subjunctive link to Death’s prediction.

---

## 4. Open Questions and an Operational Recipe for Unfamiliar Cases

While Yudkowsky and Soares (2017) establish the power of Equation (4) in known dilemmas, they explicitly leave three foundational questions open:
1. **Deducing $G$ and Counterpossibles**: Unlike Pearl (2000), who showed how to infer causal graphs $G$ from physical interventions, the authors state that "Equation (4) works *given* a graph that accurately describes how changing the value of a logical variable affects other variables, but it is not yet clear how to construct such a thing."
2. **Action-Based vs. Policy-Based Evaluation and Cross-Branch Priors**: In Footnotes 7 and 16, the authors remark that while Equation (4) selects an *action* by intervening on $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$, their preferred generalization intervenes on $\textsc{fdt}(\underline{P}, \underline{G})$ to select a *policy* $\pi: \mathcal{X} \to \mathcal{A}$, adding that the difference "only matters in multi-agent dilemmas so far as we can tell." Moreover, in single-agent problems with multiple functional nodes (such as $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$ in Transparent Newcomb), the source paper leaves the prior $q$ on the unintervened node as a free parameter because $q$ is Either canceled out or swamped by small error probabilities.
3. **Formalizing "Fair" Dilemmas**: In Section 9 (and Footnote 15), the authors note that any decision theory can be punished if a predictor directly inspects its source code (e.g., "punish anyone who uses **A-FDT**"), and leave open how to formalize the class of "fair problems" where outcomes depend only on predictions of the agent's behavior in the dilemma at hand.

To enable a reader to apply **A-FDT** systematically to *unfamiliar* decision problems, we now develop an explicit operational interpretation addressing these gaps. Everything that follows in Sections 4.1 and 4.2 beyond the summary of the source text represents **our own operational proposal and mathematical analysis**.

### 4.1 An Operational 4-Step Protocol for Constructing $(P, G)$

When confronted with a new decision problem, how should an **A-FDT** theorist construct the subjunctive graph $G$? We propose treating $G$ as a **computational structural equation model (C-SEM)** built via the following four-step recipe:

* **Step 1 (Identify the Epistemic-Observational Index Set $\mathcal{I}$)**: List all possible local input tuples $i = (P_i, G, x_i) \in \mathcal{I}$ that the agent (or a copy/counterpart of the agent in the problem) might face at the decision point. For each $i \in \mathcal{I}$, instantiate a distinct root node $F_i \coloneqq \textsc{fdt}(\underline{P_i}, \underline{G}, \underline{x_i})$ taking values in $\mathcal{A}$.
* **Step 2 (Separate Algorithmic Emulators from Statistical Confounders)**: For every environmental variable $Z$ that correlates with the agent’s action, apply the *Algorithmic Simulation Test*: Does the physical mechanism generating $Z$ operate by simulating, deducing, or replicating the input-output mapping of the agent's decision procedure at index $i \in \mathcal{I}$ (like a predictor, a psychological twin, or the agent’s own future self facing an isomorphic problem)?
  * If **yes**, draw a directed edge $F_i \to Z$, alongside an exogenous noise node $E_Z \to Z$ representing simulation/prediction accuracy.
  * If **no**—if $Z$ is a historical or biological state (such as a genetic lesion, a rumor of termites, or a prior coin toss) that merely influences *which* index $i \in \mathcal{I}$ the agent occupies—Make $Z$ an upstream parent of the observation/multiplexer, with **no** incoming edge from any $F_i$.
* **Step 3 (Construct the Physical Action Multiplexer)**: Draw directed edges from all $F_i$ ($i \in \mathcal{I}$) and from the state/observation-generating variables to $\textsc{Act}$. Define the structural equation for $\textsc{Act}$ as a deterministic multiplexer: if the realized world-state delivers input tuple $i^*$ to the agent, then $\textsc{Act} = F_{i^*}$ (possibly modulated by physical execution noise, such as a cosmic ray node).
* **Step 4 (Evaluate Equation 4 at the Realized Index $i_0 = (P, G, x)$)**: Given the agent’s actual inputs $(P, G, x)$, compute for each $a \in \mathcal{A}$ the post-intervention expectation $\mathbb{E}[\textsc{V} \mid \mathtt{do}(F_{i_0} = a)]$ by propagating $F_{i_0} = a$ forward through the C-SEM without conditioning on $\textsc{Obs} = x$.

### 4.2 Resolving Unintervened Node Priors ($q$) and the Boundary Between A-FDT and Policy-FDT

What happens in Step 4 if the optimal action at index $i_0 = (P, G, x)$ *does* depend on the prior probability $q$ assigned to another functional node $F_{i'}$ ($i' \neq i_0$)? Here we must distinguish two cases that illuminate the exact mathematical boundary between action-based **A-FDT** (Equation 4) and policy-based functional decision theory (**P-FDT**).

#### Case A: Sequential or Decoupled Unintervened Nodes (Recursive Self-Simulation)
Suppose the node $F_{i'} = \textsc{fdt}(\underline{P}, \underline{G}, \underline{x'})$ has a well-defined solution under Equation (4) that does not depend back on $F_{i_0}$. For instance, in Transparent Newcomb, what *is* the value of $q = P^F(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty}) = \mathit{twobox})$? As Yudkowsky and Soares note in passing, "The correct value of $q$ is $1$, as you may verify." Why? Because if we apply Equation (4) to the node $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$, it has *no outgoing edge to $\textsc{Prediction}$* (the predictor only predicted what Fiona would do if Box B were full). Thus, intervening on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$ affects $\textsc{Act}$ only when $\textsc{Box B} = \mathit{empty}$, yielding $P^F(\textsc{Box B} = \mathit{empty}) \cdot \$1,000$ for $\mathit{twobox}$ versus $\$0$ for $\mathit{onebox}$. 

**Operational Rule (Recursive Closure)**: Whenever an unintervened node $F_{i'}$ is subjunctively downstream or acyclic relative to $F_{i_0}$, an **A-FDT** agent should compute $\mathrm{FDT}(P_{i'}, G, x')$ via Equation (4) first, and set $P(F_{i'} = \mathrm{FDT}(P_{i'}, G, x')) = 1$ (or $1 - \epsilon$ under bounded logical uncertainty).

#### Case B: Simultaneous Cross-Branch Coupling (Where A-FDT and P-FDT Diverge)
Now consider an unfamiliar dilemma designed to test Footnotes 7 and 16: the **Cross-Observation Coordination Game**.

> **Example (The Split-Room Twin Coordination Dilemma)**: You and your identical computational twin are placed in separate rooms. A fair coin is flipped: whoever is in Room H observes $x = \mathit{H}$, and whoever is in Room T observes $x = \mathit{T}$ (you do not know in advance which room you will be put in, so each observation has prior probability $0.5$). Each of you must choose an action $a \in \{\mathit{Left}, \mathit{Right}\}$. A referee rewards both of you with $\$1,000,000$ if and only if **the action chosen upon observing $\mathit{H}$ matches the action chosen upon observing $\mathit{T}$**, and gives an extra $\$1,000$ bonus if that matching pair is $(\mathit{Left}, \mathit{Left})$ rather than $(\mathit{Right}, \mathit{Right})$. If your actions mismatch, you both receive $\$0$. You look around and observe $x = \mathit{H}$. What does **A-FDT** (Equation 4) prescribe?

Let us build the graph $G$ using our protocol. There are two observational indices for the shared algorithm: $F_{\mathit{H}} \coloneqq \textsc{fdt}(\underline{P}, \underline{G}, \mathit{H})$ and $F_{\mathit{T}} \coloneqq \textsc{fdt}(\underline{P}, \underline{G}, \mathit{T})$. Because you observed $\mathit{H}$, your physical action is $\textsc{Act}_{\mathit{H}} = F_{\mathit{H}}$, and your twin’s physical action in the other room is $\textsc{Act}_{\mathit{T}} = F_{\mathit{T}}$. The utility function is:
$$\textsc{V}(F_{\mathit{H}}, F_{\mathit{T}}) = \begin{cases} \$1,001,000 & \text{if } F_{\mathit{H}} = F_{\mathit{T}} = \mathit{Left}, \\ \$1,000,000 & \text{if } F_{\mathit{H}} = F_{\mathit{T}} = \mathit{Right}, \\ \$0 & \text{if } F_{\mathit{H}} \neq F_{\mathit{T}}. \end{cases}$$

Look closely at what happens when you apply pure **A-FDT** (Equation 4) upon observing $x = \mathit{H}$:
$$\mathrm{FDT}(P, G, \mathit{H}) = \operatorname*{argmax}_{a \in \{\mathit{Left}, \mathit{Right}\}} \mathbb{E}\left[\textsc{V}(F_{\mathit{H}}, F_{\mathit{T}}) \;\middle|\; \mathtt{do}(F_{\mathit{H}} = a)\right].$$
Because $F_{\mathit{H}}$ and $F_{\mathit{T}}$ are distinct functional nodes (evaluating the algorithm on distinct inputs $\mathit{H} \neq \mathit{T}$), there is no directed edge $F_{\mathit{H}} \to F_{\mathit{T}}$. Therefore, under $\mathtt{do}(F_{\mathit{H}} = a)$, the distribution of $F_{\mathit{T}}$ is held fixed at its prior $q = P(F_{\mathit{T}} = \mathit{Left})$!
* For $a = \mathit{Left}$, expected utility is $q \cdot \$1,001,000$.
* For $a = \mathit{Right}$, expected utility is $(1-q) \cdot \$1,000,000$.

If your prior $q$ happened to be $< 0.49975$ (i.e., you initially believed you and your twin would coordinate on $(\mathit{Right}, \mathit{Right})$), then both $\mathrm{FDT}(P, G, \mathit{H})$ and $\mathrm{FDT}(P, G, \mathit{T})$ will lock into $\mathit{Right}$, leaving $\$1,000$ on the table because neither branch’s local intervention $\mathtt{do}(F_x = a)$ can unilaterally alter the other branch’s node $F_{x'}$!

By contrast, in **policy-based FDT (P-FDT)** (Footnotes 7 and 16), the agent intervenes on a single global policy node $\textsc{fdt}_{\text{policy}}(\underline{P}, \underline{G}) = \pi \in \mathcal{A}^{\mathcal{X}}$, and then executes $\pi(x)$:
$$\mathrm{PFDT}(P, G, x) \coloneqq \left[\operatorname*{argmax}_{\pi \in \mathcal{A}^{\mathcal{X}}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}_{\text{policy}}(\underline{P}, \underline{G}) = \pi\right)\right)\right](x).$$
Because $\mathtt{do}(\textsc{fdt}_{\text{policy}}(\underline{P}, \underline{G}) = \pi)$ simultaneously sets $F_{\mathit{H}} = \pi(\mathit{H})$ and $F_{\mathit{T}} = \pi(\mathit{T})$, **P-FDT** directly compares all four policies $\{\mathit{LL}, \mathit{LR}, \mathit{RL}, \mathit{RR}\}$ and selects $\pi^* = \mathit{LL}$ ($¥1,001,000$) regardless of prior $q$. Within **A-FDT** (Equation 4), achieving the same result in cross-branch games requires an additional epistemic assumption on $P$: that the agent’s prior over functional nodes $(F_{\mathit{H}}, F_{\mathit{T}})$ concentrates on the Pareto-optimal fixed point before local $\mathtt{do}$-interventions are evaluated.

---

## 5. Conclusion

**Action functional decision theory (A-FDT)**, formalized by Equation (4) of Yudkowsky and Soares (2017), represents a major milestone in the foundations of instrumental rationality. By shifting the locus of decision-theoretic intervention from the physical act $\textsc{Act}$ to the logical output $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ of the decision algorithm itself—and by responding to observations $x$ through indexing the intervened variable rather than conditioning the world-model—**A-FDT** unifies single-agent decision theory and multi-agent coordination. It captures the benefits of precommitment without requiring physical self-binding, assigns non-negative value to information, resists extortion, and achieves maximal utility across Newcomb’s Problem, the Smoking Lesion, Parfit’s Hitchhiker, and Death in Damascus. While deep technical questions remain regarding logical uncertainty and the transition from action-level to policy-level interventions in multi-branch games, **A-FDT** provides a mathematically sharp, operationally powerful blueprint for rational agency in a world populated by predictors and replicators.

---

## References

* Arntzenius, Frank (2008). "No Regrets, or: Edith Piaf Revamps Decision Theory." *Erkenntnis* 68 (2): 277–297.
* Cohen, Daniel (1990). "On What Cannot Be." In *Truth or Consequences: Essays in Honor of Nuel Belnap*, 123–132. Kluwer Academic Publishers.
* Dai, Wei (2009). "Towards a New Decision Theory." *Less Wrong*, August 13, 2009.
* Drescher, Gary L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Gibbard, Allan, and William L. Harper (1978). "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, Vol. 1, 125–162. D. Reidel.
* Joyce, James M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Joyce, James M. (2012). "Regret and Instability in Causal Decision Theory." *Synthese* 187 (1): 123–145.
* Kleene, Stephen Cole (1938). "On Notation for Ordinal Numbers." *Journal of Symbolic Logic* 3 (4): 150–155.
* Lewis, David (1979). "Prisoners' Dilemma is a Newcomb Problem." *Philosophy & Public Affairs* 8 (3): 235–240.
* Lewis, David (1981). "Causal Decision Theory." *Australasian Journal of Philosophy* 59 (1): 5–30.
* Nozick, Robert (1969). "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel*, 114–146. D. Reidel.
* Parfit, Derek (1986). *Reasons and Persons*. Oxford University Press.
* Pearl, Judea (1996). "Causation, Action, and Counterfactuals." In *6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-'96)*, 51–73.
* Pearl, Judea (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Peirce, Charles Sanders (1934). *Collected Papers of Charles Sanders Peirce, Vol. V: Pragmatism and Pragmaticism*. Harvard University Press.
* Skyrms, Brian (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Soares, Nate, and Benja Fallenstein (2015). "Toward Idealized Decision Theory." *arXiv preprint* arXiv:1507.01986.
* Yudkowsky, Eliezer (2010). *Timeless Decision Theory*. Technical Report, The Singularity Institute.
* Yudkowsky, Eliezer, and Nate Soares (2017). "Functional Decision Theory: A New Theory of Instrumental Rationality." *arXiv preprint* arXiv:1710.05060v2.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Scope**

I'm now focusing on defining the scope for this explanation of Action Functional Decision Theory. The goal is to create a technical explanation, probably in essay or blog post form. I am keeping in mind the need for practical application to real-world decision-making problems. I need to make sure the target audience is clear to define scope, but an expert audience is presumed.


**Clarifying Target Audience**

I've clarified the target audience; it's mathematically literate individuals interested in formal procedures and the philosophical underpinnings of decision theories. My role is that of a researcher creating a mathematical essay or technical blog post. I'll focus on Action Functional Decision Theory (**A-FDT**), using Equation (4) from Section 5 of the paper as the primary formal presentation. I am using **A-FDT** consistently, while clearly identifying other decision theories.


**Defining Content Parameters**

I'm now zeroing in on defining specific content parameters for the explanation of Action Functional Decision Theory. I plan to present a coherent account including mathematical definitions, equations, examples, and explanations. It should be precise enough for application in unfamiliar cases. I'm prioritizing clarity, aiming for approximately 2,400–3,000 words. My work will distinguish original claims from additions. I'm focusing on explaining how A-FDT evaluates actions, treating dependencies and counterfactuals, particularly Equation (4), the action-intervening formulation.


**Identifying A-FDT**

I've determined the formal definition is Action Functional Decision Theory (**A-FDT**), not the general Functional Decision Theory (**FDT**) presented in the 2017 paper. I'll make this clear. The primary focus is Equation (4) from Section 5. My essay will present Equation (4) as the formal definition of A-FDT. I'll also discuss the philosophical motivation and the CDT vs. EDT stalemate.


**Analyzing Decision Frameworks**

I'm now analyzing key decision scenarios to highlight the limitations of both Causal Decision Theory (CDT) and Evidential Decision Theory (EDT), showing the advantages of A-FDT. I am going to explore the nuances of Parfit's Hitchhiker, Transparent Newcomb, and Mechanical Blackmail, where both CDT and EDT fail, as well as Death in Damascus, in which CDT is reflectively unstable, while EDT/A-FDT succeed. I am investigating Joyce's representation theorem, to show the differences depend only on the epistemic perspective. I will highlight how EDT's over-respect for statistical correlations and CDT's severing of logical ones each lead to issues.


**Intervening on A-FDT**

I am now focusing on the core mechanism of Action Functional Decision Theory (**A-FDT**). I've got a clearer understanding: A-FDT intervenes on the logical output of the decision function, which is $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)$. This intervention tracks subjunctive dependence, where two systems compute the same mathematical function. My current focus is on the crucial mechanics of Equation (4), and now I have a grasp of its role in self-reference handling using Kleene's recursion theorem. I'm noting the distinction where CDT intervenes on physical tokens, while A-FDT intervenes on the computational type.


**Evaluating the Logic**

I'm now evaluating the specific logic of Action Functional Decision Theory (**A-FDT**) through $\EE(\VV \mid \Do(\Act=\act), \Obs=\obs)$ and how it relates to Equation (4). Crucially, **A-FDT** does *not* condition on $\Obs = \obs$. Instead, the intervention shifts the node being intervened upon, from $\FDTvar(\underline P, \underline G, \underline x)$ to $\FDTvar(\underline P, \underline G, \underline y)$, depending on observation $\obs$. This is vital in scenarios like Transparent Newcomb, where observation is causally downstream. By not conditioning on $\Obs=\obs$, **A-FDT** assesses the world *before* the observation.


**Operationalizing Counterfactuals**

I'm now focusing on operationalizing the construction of subjunctive dependency graph $G$ and defining a counterpossible truth operator. I propose an "Algorithmic Structural Equations" protocol for unfamiliar problems, which distinguishes what the paper specifies from my operational proposal. This involves defining a step-by-step procedure to construct $G$ in decision problems, a key challenge.


**Investigating Logical Nodes**

I'm now investigating how A-FDT works in specific scenarios by keeping separate nodes for logical dependencies. Maintaining separate logical decision nodes, such as $\FDTvar(\underline{P}, \underline{G}, \underline{x_1})$ and $\FDTvar(\underline{P}, \underline{G}, \underline{x_2})$, allows for proper counterfactual reasoning. I'm focusing on clarifying how this approach resolves problems in Transparent Newcomb and Smoking Lesion and when it diverges from policy-based FDT. I also want to address prior probabilities.


**Analyzing Parameter Space**

I'm now analyzing the parameter space in Action Functional Decision Theory (**A-FDT**), specifically the decision variable $q$ in scenarios where it matters. This includes situations where single-agent problems aren't decoupled, and a value for $q$ must be specified. I'm considering recursive evaluation or fixed-point computation to guide how an A-FDT agent sets $q$. My focus is on ensuring consistency in decision-making across varied problem structures.


**Defining Interventions**

I'm now focusing on defining the functional and observation-indexed interventions that distinguish Action Functional Decision Theory (**A-FDT**) from Causal Decision Theory (CDT). I'm highlighting that **A-FDT** intervenes on the function's output, $\FDTvar(\underline{P}, \underline{G}, \underline{x}) = \act$, rather than the action itself. The index of the variable is also key; the observation $\obs$ is encoded directly into that. My next step will be to contrast this against the causal framework.


**Comparing Decision Theories**

I'm now comparing A-FDT to Timeless Decision Theory (TDT) and Wei Dai's Updateless Decision Theory (UDT) to better elucidate the nuances of each. I'm focusing on contrasting their approaches to decision dilemmas, which involve mathematical models $(P, G)$. I'm particularly interested in how each evaluates actions, such as in Standard Newcomb, Smoking Lesion, and Transparent Newcomb scenarios. I'll showcase how these approaches compare.


**Operationalizing Decisions**

I'm now operationalizing decisions, focusing on constructing the subjunctive graph, G, and evaluating counterpossibles for unfamiliar cases. I am proposing a four-step algorithmic structural equations protocol, distinguishing the paper's claims from my operational extensions. I'm building this as a structured recipe for clarifying decision problem inputs and dependencies for further work.


**Analyzing Coordination Scenarios**

I'm now analyzing an unfamiliar case to compare Action-Based A-FDT with Policy-Based FDT, using a Cross-Information-Set Coordination Game. I'm investigating how pure A-FDT, using Equation 4, handles the other branches' nodes, specifically with regard to prior $q$, and how recursive self-evaluation resolves this in sequential scenarios. I want to highlight why simultaneous symmetric multi-branch coupling motivates Policy-FDT.


**Verifying Algebraic Fidelity**

I'm now carefully verifying the algebraic fidelity of the equations and examples presented in the source paper, particularly in the context of Newcomb's Problem and Transparent Newcomb. I've found some minor numerical discrepancies which I'll correct and explicitly clarify in my work. The goal is to ensure 100% mathematical accuracy throughout my explanation of A-FDT. I'm focusing on rigorous algebraic calculations to avoid any confusion.


**Refining Evaluation Scenarios**

I'm now refining the scenarios used to evaluate A-FDT, incorporating new insights from my algebraic verification. I'm focusing on clarifying how A-FDT handles scenarios with potential mispredictions, such as in the modified Newcomb's Problem, and how these affect expected payoffs, and how this relates to Equation (4). The key is distinguishing between observation-based and action-based utilities.


**Calculating Utilities**

I'm now calculating utilities for a modified Newcomb's Problem scenario, considering mispredictions by the predictor, and the expected payoffs. I'm carefully analyzing how A-FDT handles these edge cases using Equation (4), emphasizing the distinction between observational and action-based utilities. I've re-examined the payoffs, and I am focused on the utility calculation for the two-box action, accounting for both accurate and inaccurate predictions.


**Evaluating Smoking Lesion**

I'm now carefully evaluating the Smoking Lesion scenario, focusing on the algebra presented in Section 6. I'm calculating expected utilities under both $\Do(\FDTvar(\underline{P_S}, \underline{G}) = \Val{smoke})$ and $\Do(\FDTvar(\underline{P_S}, \underline{G}) = \Val{refrain})$, accounting for the agent's lesion and the potential for mispredictions. I'm paying attention to the values to correctly interpret how A-FDT behaves.


**Refining Content Considerations**

I'm now refining the overall content and word count for the explanation. I've been reviewing the source material to ensure all critical details, particularly concerning Equation (4), are included. I'm focusing on ensuring it's clear how A-FDT evaluates actions, dependencies, and counterfactuals within the specified word count, and I'll distinguish my proposals from the original claims. I've re-examined the source materials and examples.


```
