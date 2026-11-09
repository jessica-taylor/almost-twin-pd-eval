# 029_fdt_policy_google_gemini-4-argon_rhigh_phigh / 00005

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/99d32d6f-4679-459d-842b-3472357f8c8a/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/99d32d6f-4679-459d-842b-3472357f8c8a/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Policy Functional Decision Theory (P-FDT): Formalizing Updateless Policy Selection under Subjunctive Dependence

## 1. Introduction: From Physical Acts to Logical Policies

Standard normative decision theory has long been divided between two rival camps: **evidential decision theory (EDT)** and **causal decision theory (CDT)**. When evaluating a candidate action $a$, an EDT agent asks which action would provide the best news if she learned she had taken it—conditioning her beliefs on the event that she performs $a$. A CDT agent asks instead which physical act would *cause* the best outcome—intervening on the physical token of her action while holding fixed everything causally upstream of it. Neither principle consistently maximizes utility across well-known decision problems: EDT is exploited in common-cause environments such as Skyrms's (1980) smoking lesion problem and Soares and Fallenstein's (2015) XOR blackmail problem, whereas CDT leaves money on the table in predictor-driven dilemmas such as Nozick's (1969) Newcomb's problem, Parfit's (1986) hitchhiker problem, and the psychological twin prisoner's dilemma (Lewis, 1979).

In *Functional Decision Theory: A New Theory of Instrumental Rationality*, Yudkowsky and Soares (2017) argue that both EDT and CDT evaluate malformed hypotheticals. EDT preserves too many correlations between action and environment (including purely statistical ones), whereas CDT preserves too few (severing logically or computationally necessary correlations between an agent's decision algorithm and accurate predictors or copies of that algorithm). Their proposed remedy treats an agent's decision as the output of a fixed mathematical function and asks: *"Which output of this very function would yield the best outcome?"*

In the main body of their paper, Yudkowsky and Soares formalize a simplified version of their theory—which we will call **action-based functional decision theory (action-based FDT, or $\mathrm{FDT}$)**—in which the agent intervenes on a logical node representing the action output for her current observation. Crucially, however, they note twice that this action-by-action formulation is merely an expositional simplification of a deeper theory. In footnote 7, they write:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

And in footnote 16, when explaining why a functional decision theorist does not perform a standard Bayesian update on her observations before evaluating counterfactuals, they state the core mechanism of **policy functional decision theory (P-FDT)**:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

This essay provides a self-contained mathematical account of **P-FDT**. We will formalize the two-stage decision procedure described in footnote 16, explain how P-FDT models counterfactuals and subjunctive dependencies, demonstrate step-by-step how to apply P-FDT to single-agent and multi-agent decision problems, and examine the open technical questions left unresolved by the source text alongside concrete operational proposals for resolving them.

---

## 2. Mathematical Foundations: World-Models, Subjunctive Graphs, and P-FDT

### 2.1 The Expected Utility Framework and Epistemic Perspectives

Following Gibbard and Harper (1978) and Joyce (1999), Yudkowsky and Soares situate EDT, CDT, action-based FDT, and **P-FDT** within a shared expected-utility framework. Let:
* $\mathcal{O} = \{o_1, o_2, \dots\}$ be a countable set of possible outcomes;
* $\mathcal{A}$ be a finite set of available actions;
* $\mathcal{X}$ be a countable (or finite) set of possible observation histories; and
* $\mathcal{U} : \mathcal{O} \to \mathbb{R}$ be a bounded utility function.

In the general representation of Joyce (1999), an agent who has received observation $x \in \mathcal{X}$ evaluates an option by computing expected utility relative to a decision-hypothetical connective $\hookrightarrow$:

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j). \tag{1}$$

As Joyce observes, *"decision theories should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated."* Formally, let $\textsc{Outcome}$ be an $\mathcal{O}$-valued random variable, $\textsc{Obs}$ an $\mathcal{X}$-valued random variable, $\textsc{Act}$ an $\mathcal{A}$-valued random variable, and $\textsc{V} \coloneqq \mathcal{U}(\textsc{Outcome})$ the real-valued utility variable. An agent maintains a world-model $M$, from which she constructs a hypothetical distribution $M^{a\hookrightarrow}$ (or, in P-FDT, $M^{\pi\hookrightarrow}$) to evaluate her expected utility.

In **EDT**, the world-model is simply a probability distribution $P$, and hypotheticals are constructed via Bayesian conditionalization on both the observation $x$ and the action $a$ (ignoring zero-probability actions):

$$\mathrm{EDT}(P, x) \coloneqq \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs}=x, \textsc{Act}=a\right). \tag{2}$$

In **CDT** (formalized via Pearl, 1996, 2000), the world-model is a pair $M = (P, G)$, where $G$ is a causal directed acyclic graph (DAG) over the variables of $P$. A CDT agent conditions on her observation $\textsc{Obs}=x$ and uses Pearl's $\mathtt{do}$-operator to perform graph surgery on her physical action node $\textsc{Act}$, severing all incoming arrows into $\textsc{Act}$ while propagating causal effects downstream:

$$\mathrm{CDT}(P, G, x) \coloneqq \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x\right). \tag{3}$$

### 2.2 Subjunctive Dependence and Action-Based FDT

The foundational insight of Yudkowsky and Soares is that physical causation is only one species of a broader relation they term **subjunctive dependence**. When two physical systems—such as an agent and a twin, or an agent and an accurate simulation inside a predictor's brain—implement or model the same mathematical decision function, their outputs are logically and computationally constrained to covary insofar as no hardware or prediction error occurs. *"Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."*

Ideally, evaluating what would happen if a deterministic mathematical function produced a different output requires evaluating *counterpossibilities*—conditionals with logically false antecedents (Cohen, 1990; Bjerring, 2013)—via a logical intervention operator $\mathtt{true}(\phi)$. Because probability theory currently lacks a general algorithmic specification of $\mathtt{true}(\phi)$, Yudkowsky and Soares operationalize subjunctive dependence using Pearl's graphical formalism: the world-model is a pair $(P, G)$ where $P$ includes random variables representing the outputs of mathematical functions, and the DAG $G$ encodes not only physical causation but also logical and computational dependencies.

In the main text's **action-based FDT**, the graph $G$ contains a distinct logical node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ for each possible observation $x \in \mathcal{X}$ (where underbars denote dequotation, embedding the values of $P, G, x$ into the variable's syntactic name via Kleene's [1938] second recursion theorem). Action-based FDT selects an action by intervening directly on the node indexed by the current observation $x$:

$$\mathrm{FDT}(P, G, x) \coloneqq \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right). \tag{4}$$

Notice two crucial features of Equation (4). First, unlike CDT, it does not condition $P$ on $\textsc{Obs}=x$; doing both—conditioning on $\textsc{Obs}=x$ *and* intervening on the logical node—causes a harmful "double update" (a flaw of Yudkowsky's [2010] earlier Timeless Decision Theory [TDT], avoided in Wei Dai's [2009] Updateless Decision Theory [UDT]). Second, however, because Equation (4) intervenes *only* on the node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ for the specific observation $x$ received, any nodes $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x'})$ corresponding to counterfactual observations $x' \neq x$ remain un-intervened random variables governed by the prior $P$.

### 2.3 Formalizing P-FDT (Policy Functional Decision Theory)

**P-FDT** eliminates this piecemeal node-by-node intervention. In P-FDT, the decision function's logical representation in $G$ is a *single* policy-valued node, which we denote $\textsc{pfdt}(\underline{P}, \underline{G})$ (corresponding to the source's $\mathrm{FDT}(-)$ in footnote 16).

To formalize footnotes 7 and 16 mathematically, let us state our notation and distinguish the source's explicit claims from our formalization choices:
* **Source specification (footnotes 7 and 16):** The agent intervenes on the node representing her decision function to select a *policy* mapping observations (or inputs) to actions, and then applies that chosen policy to her actual inputs/observations to select an action.
* **Formal definition of the policy space:** For a given world-model $(P, G)$ with observation space $\mathcal{X}$ and action space $\mathcal{A}$, let the policy space be the set of all functions from observations to actions:
  $$\Pi \coloneqq \mathcal{A}^{\mathcal{X}} = \{\pi \mid \pi : \mathcal{X} \to \mathcal{A}\}.$$
  *(We assume for tractability in standard problems that the decision-relevant observation space $\mathcal{X}$ is finite, so $\Pi$ is finite with cardinality $|\mathcal{A}|^{|\mathcal{X}|}$; we address infinite or richer input spaces in Section 4.)*

In a P-FDT world-model $(P, G)$, the node $\textsc{pfdt}(\underline{P}, \underline{G})$ takes values in $\Pi$. The physical action variable $\textsc{Act}$ is a deterministic function of both the policy node $\textsc{pfdt}(\underline{P}, \underline{G})$ and the observation variable $\textsc{Obs}$:

$$\textsc{Act}\big(\pi, x\big) \coloneqq \pi(x). \tag{5}$$

Similarly, any predictor in the environment that models the agent's behavior under observation $x'$ depends subjunctively on the same node $\textsc{pfdt}(\underline{P}, \underline{G})$ (specifically, on its evaluation $\pi(x')$).

**Definition 1 (The P-FDT Decision Rule).** Given a world-model $(P, G)$ and an actual observation $x \in \mathcal{X}$, **P-FDT** selects an action in two steps:

1. **Global Policy Optimization (Intervention Step):** Select an optimal policy $\pi^*(\underline{P}, \underline{G}) \in \Pi$ by intervening on the policy node $\textsc{pfdt}(\underline{P}, \underline{G})$ in the unconditioned model $(P, G)$:
   $$\pi^*(\underline{P}, \underline{G}) \coloneqq \operatorname{argmax}_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right). \tag{6}$$
2. **Local Action Instantiation (Application Step):** Apply the optimal policy $\pi^*(\underline{P}, \underline{G})$ to the actual observation $x$ to output a concrete action in $\mathcal{A}$:
   $$\mathrm{P\text{-}FDT}(P, G, x) \coloneqq \big[\pi^*(\underline{P}, \underline{G})\big](x) = \left[\operatorname{argmax}_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right)\right](x). \tag{7}$$

Let us examine how Equation (7) treats dependencies, observations, and counterfactuals:
1. **Simultaneous Counterfactual Control Across All Observations:** When a P-FDT agent evaluates a candidate policy $\pi \in \Pi$, the intervention $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$ simultaneously fixes what her algorithm outputs at *every* possible observation $x' \in \mathcal{X}$, as well as what any accurate predictor or twin predicts she will do at every $x' \in \mathcal{X}$.
2. **How Observations Enter:** In P-FDT, the observation $x$ does not alter the probability distribution $P$ via Bayes' rule during policy evaluation, nor does it select among multiple disconnected $\textsc{fdt}$ nodes in $G$. Instead, the optimization in Step 1 is completely prior to (and independent of) $x$; the observation $x$ enters *only* in Step 2 as the argument passed to the chosen function $\pi^*(\underline{P}, \underline{G})$.
3. **Endogenous Observation Distribution:** Because $\textsc{Obs}$ is often causally downstream of predictors that are themselves subjunctively downstream of $\textsc{pfdt}(\underline{P}, \underline{G})$, intervening to change $\pi$ in Equation (6) automatically changes the probability distribution over which observation $x$ the agent expects to receive:
   $$P\left(\textsc{Obs} = x \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right).$$
   Thus, P-FDT naturally entertains counterfactuals in which, had the agent adopted a different policy $\pi$, she would have observed different evidence.

---

## 3. Applying P-FDT to Single-Agent Dilemmas: Worked Examples

To see how a researcher or practitioner can apply **P-FDT** to concrete cases—and how its mechanics streamline the calculations of action-based FDT—let us work through two canonical structural templates: a dilemma with endogenous observations (the Transparent Newcomb Problem, which is structurally isomorphic to Parfit's Hitchhiker and Mechanical Blackmail) and a dilemma with common-cause correlation (the Smoking Lesion).

### 3.1 The Transparent Newcomb Problem under P-FDT

In Drescher's (2006) **Transparent Newcomb Problem** (Dilemma 5 in Yudkowsky & Soares, 2017), Box A transparently contains $\$1,000$, and Box B transparently contains either $\$1,000,000$ ($\textit{full}$) or $\$0$ ($\textit{empty}$). A predictor with accuracy $0.99$ placed $\$1,000,000$ in Box B if and only if she predicted that the agent would leave Box A behind ($\textit{onebox}$) upon observing that Box B is $\textit{full}$. Suppose the agent looks at the boxes and observes $x = \textit{full}$. What should she do?

Let us set up the **P-FDT** model $(P, G)$:
* **Spaces:** $\mathcal{X} = \{\textit{full}, \textit{empty}\}$ and $\mathcal{A} = \{\textit{onebox}, \textit{twobox}\}$ (abbreviated $1$ and $2$).
* **Policy Space $\Pi$:** Since $|\mathcal{X}|=2$ and $|\mathcal{A}|=2$, there are $|\mathcal{A}|^{|\mathcal{X}|} = 4$ policies, which we write as $\pi_{a_{\text{full}},\, a_{\text{empty}}}$ where $\pi_{a_f, a_e}(\textit{full}) = a_f$ and $\pi_{a_f, a_e}(\textit{empty}) = a_e$:
  $$\Pi = \{\pi_{1,1},\, \pi_{1,2},\, \pi_{2,1},\, \pi_{2,2}\}.$$
* **Subjunctive Graph $G$ and Structural Equations:**
  * $\textsc{Accurate} \in \{\textit{accurate}, \textit{inaccurate}\}$ is an exogenous noise variable with $P(\textsc{Accurate}=\textit{accurate}) = 0.99$ and $P(\textsc{Accurate}=\textit{inaccurate}) = 0.01$.
  * $\textsc{pfdt}(\underline{P}, \underline{G}) \in \Pi$ is the policy node upon which the agent intervenes.
  * $\textsc{Prediction} \in \{1, 2\}$ depends on $\textsc{pfdt}(\underline{P}, \underline{G})$ and $\textsc{Accurate}$. Because the predictor specifically predicts what the agent will do *upon seeing Box B full*, $\textsc{Prediction}$ is governed by $\pi(\textit{full})$:
    $$\textsc{Prediction}(\pi, \textit{accurate}) = \pi(\textit{full}), \qquad \textsc{Prediction}(\pi, \textit{inaccurate}) = 3 - \pi(\textit{full}).$$
  * $\textsc{Box B} \in \{\textit{full}, \textit{empty}\}$ and $\textsc{Obs} \in \{\textit{full}, \textit{empty}\}$ are determined by $\textsc{Prediction}$:
    $$\textsc{Obs} = \textsc{Box B} = \begin{cases} \textit{full} & \text{if } \textsc{Prediction} = 1, \\ \textit{empty} & \text{if } \textsc{Prediction} = 2. \end{cases}$$
  * $\textsc{Act} \in \{1, 2\}$ is determined by applying $\textsc{pfdt}(\underline{P}, \underline{G})$ to $\textsc{Obs}$: $\textsc{Act}(\pi, \textsc{Obs}) = \pi(\textsc{Obs})$.
  * $\textsc{V}$ is $\$1,000,000 \cdot \mathbb{I}(\textsc{Box B}=\textit{full}) + \$1,000 \cdot \mathbb{I}(\textsc{Act}=2)$.

Now we execute the two steps of **P-FDT**:

**Step 1 (Policy Intervention):** We compute $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)]$ for each of the four policies $\pi \in \Pi$:
1. **$\pi_{1,1}$ (Always one-box):**
   Since $\pi_{1,1}(\textit{full}) = 1$, with probability $0.99$ ($\textit{accurate}$) Box B is $\textit{full}$ and the agent takes $\pi_{1,1}(\textit{full}) = 1$ ($\$1,000,000$); with probability $0.01$ ($\textit{inaccurate}$) Box B is $\textit{empty}$ and the agent takes $\pi_{1,1}(\textit{empty}) = 1$ ($\$0$).
   $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{1,1})\right] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000.$$
2. **$\pi_{1,2}$ (One-box if full, two-box if empty):**
   Since $\pi_{1,2}(\textit{full}) = 1$, with probability $0.99$ Box B is $\textit{full}$ and the agent takes $\pi_{1,2}(\textit{full}) = 1$ ($\$1,000,000$); with probability $0.01$ Box B is $\textit{empty}$ and the agent takes $\pi_{1,2}(\textit{empty}) = 2$ ($\$1,000$).
   $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{1,2})\right] = 0.99(\$1,000,000) + 0.01(\$1,000) = \$990,010.$$
3. **$\pi_{2,1}$ (Two-box if full, one-box if empty):**
   Since $\pi_{2,1}(\textit{full}) = 2$, with probability $0.01$ ($\textit{inaccurate}$) Box B is $\textit{full}$ and the agent takes $\pi_{2,1}(\textit{full}) = 2$ ($\$1,001,000$); with probability $0.99$ ($\textit{accurate}$) Box B is $\textit{empty}$ and the agent takes $\pi_{2,1}(\textit{empty}) = 1$ ($\$0$).
   $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{2,1})\right] = 0.01(\$1,001,000) + 0.99(\$0) = \$10,010.$$
4. **$\pi_{2,2}$ (Always two-box):**
   Since $\pi_{2,2}(\textit{full}) = 2$, with probability $0.01$ Box B is $\textit{full}$ and the agent takes $\pi_{2,2}(\textit{full}) = 2$ ($\$1,001,000$); with probability $0.99$ Box B is $\textit{empty}$ and the agent takes $\pi_{2,2}(\textit{empty}) = 2$ ($\$1,000$).
   $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{2,2})\right] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$

Comparing the four values, the unique maximizer is $\pi^*(\underline{P}, \underline{G}) = \pi_{1,2}$.

**Step 2 (Policy Application):** Having actually observed $x = \textit{full}$, the agent outputs:
$$\mathrm{P\text{-}FDT}(P, G, \textit{full}) = \pi_{1,2}(\textit{full}) = \textit{onebox}.$$
And if the predictor had erred so that the agent observed $x = \textit{empty}$, she would output $\mathrm{P\text{-}FDT}(P, G, \textit{empty}) = \pi_{1,2}(\textit{empty}) = \textit{twobox}$.

*Comparison with Action-Based FDT, CDT, and EDT:* In CDT and EDT, conditioning on $\textsc{Obs} = \textit{full}$ fixes the $\$1,000,000$ in Box B as a sunk fact, leading both theories to prescribe $\textit{twobox}$—which the predictor anticipates, leaving CDT and EDT agents with an empty Box B and $\$1,000$ $99\%$ of the time. Action-based FDT agrees with **P-FDT** on one-boxing, but notice a subtle difference in the derivation: in Section 6 of Yudkowsky and Soares (2017), when Fiona uses action-based FDT upon seeing $\textit{full}$, she intervenes only on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full})$ and must introduce an exogenous prior probability $q = P^F(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty}) = \textit{twobox})$ for what she would do on the $\textit{empty}$ branch. Under **P-FDT**, no such nuisance prior $q$ is needed: $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$ jointly determines behavior on both branches at once.

### 3.2 The Smoking Lesion Problem under P-FDT

In the **Smoking Lesion Problem** (Dilemma 3), an unobserved variable $\textsc{Lesion} \in \{\textit{lesion}, \textit{nolesion}\}$ with prior $P(\textsc{Lesion}=\textit{lesion}) = p \in (0,1)$ causes both a disposition to enjoy smoking and a $99\%$ rate of fatal lung cancer (versus $1\%$ without the lesion). In Yudkowsky and Soares's formalization (Section 6), having the lesion means the agent has utility function $\mathcal{U}_S$ (which values smoking at $+\$1,000$ and living at $+\$1,000,000$, hence world-model $P_S$), whereas lacking the lesion gives her $\mathcal{U}_R$ (which values smoking at $-\$1$, hence world-model $P_R$).

Whether we treat the agent's internal preference state $i \in \{S, R\}$ as an input to a unified policy $\pi : \{S, R\} \to \{\textit{smoke}, \textit{refrain}\}$ or treat $(P_S, G)$ as a fixed model with trivial observation space $\mathcal{X} = \{\emptyset\}$, **P-FDT**'s graph $G$ has no directed path from the policy node $\textsc{pfdt}(-)$ to $\textsc{Lesion}$ or $\textsc{Cancer}$: a biological lesion does not simulate the agent's decision function. Consequently, under $\mathtt{do}(\textsc{pfdt}(-) = \pi)$, the probability of $\textsc{Lesion} = \textit{lesion}$ remains invariant at $p$. For an agent with model $P_S$, any policy that prescribes $\textit{smoke}$ in state $S$ strictly outperforms refraining by $p \cdot \$1,000 > 0$. Thus, **P-FDT** prescribes $\textit{smoke}$ in the Smoking Lesion Problem and $\textit{onebox}$ in Newcomb's Problem under a single invariant rule.

---

## 4. Why Policy Selection Matters: Multi-Agent Dilemmas and Open Questions

Why do Yudkowsky and Soares state in footnotes 7 and 16 that **P-FDT** is their preferred formulation and that iterating over policies rather than actions *"makes a difference in certain multi-agent dilemmas"*? The source paper sets this distinction aside without giving an explicit example or proving where the two formulations diverge. In this section, we first construct a concrete multi-agent dilemma that mathematically separates **P-FDT** from action-based FDT, and then examine three foundational ambiguities left open by the source text alongside operational proposals of our own.

### 4.1 A Mathematical Separation: The Asymmetric-Observation Twin Dilemma

Consider why action-based FDT (Equation 4) succeeded in the Psychological Twin Prisoner's Dilemma (Dilemma 1 of the source paper): there, neither twin received a distinguishing observation ($\mathcal{X} = \{\emptyset\}$), so both twins intervened on the exact same node $\textsc{fdt}(\underline{P}, \underline{G})$.

Now suppose two computational twins—each running the same decision algorithm with the same world-model $(P, G)$—face a multi-agent dilemma in which **they receive different observations**. Specifically, consider two variants that we construct to expose the structural difference between Equations (4) and (7):

#### Variant A: The Asymmetric-Observation Twin Stag Hunt (Symmetric Prior)
Nature places one twin in $\textit{Room L}$ and the other twin in $\textit{Room R}$ (each twin has a $50/50$ prior probability in $P$ of being the twin placed in $\textit{Room L}$ versus $\textit{Room R}$). The twin in $\textit{Room L}$ observes $x = L$; the twin in $\textit{Room R}$ observes $x = R$. Each twin must choose an action $a \in \{\textit{Stag}, \textit{Hare}\}$:
* Choosing $\textit{Hare}$ guarantees that twin $\$1,000$ regardless of what the other twin does.
* Choosing $\textit{Stag}$ yields $\$1,000,000$ to each twin **if and only if both** the twin in $\textit{Room L}$ and the twin in $\textit{Room R}$ choose $\textit{Stag}$; otherwise, a lone $\textit{Stag}$-hunter gets $\$0$.

Compare **action-based FDT (Equation 4)** and **P-FDT (Equation 7)** when a twin observes $x = L$:

* **Action-Based FDT:** Because the two rooms yield distinct observations $L \neq R$, the graph $G^F$ contains two distinct root nodes: $\textsc{fdt}(\underline{P}, \underline{G}, L)$ (governing the $\textit{Room L}$ twin's action) and $\textsc{fdt}(\underline{P}, \underline{G}, R)$ (governing the $\textit{Room R}$ twin's action). When the twin in $\textit{Room L}$ evaluates Equation (4), she intervenes *only* on $\textsc{fdt}(\underline{P}, \underline{G}, L) = a$. The node $\textsc{fdt}(\underline{P}, \underline{G}, R)$ is not intervened upon; its value is governed by the prior probability $q \coloneqq P(\textsc{fdt}(\underline{P}, \underline{G}, R) = \textit{Stag})$.
  Computing expected utility under Equation (4) (recalling that in the unconditioned prior $P$, the agent has probability $0.5$ of being in $\textit{Room L}$ and $0.5$ of being in $\textit{Room R}$):
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline{P}, \underline{G}, L) = \textit{Stag}\big)\right] = 0.5\big(q \cdot \$1,000,000\big) + 0.5\big(q \cdot \$1,000,000 + (1-q) \cdot \$1,000\big),$$
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline{P}, \underline{G}, L) = \textit{Hare}\big)\right] = 0.5\big(\$1,000\big) + 0.5\big((1-q) \cdot \$1,000\big).$$
  Subtracting the two, choosing $\textit{Stag}$ at node $L$ beats $\textit{Hare}$ if and only if $q \cdot \$1,000,000 > \$500$, i.e., $q > 0.0005$. If both twins initially assign low credence to the other branch playing $\textit{Stag}$ (say, $q = 0$), then $\mathrm{FDT}(P, G, L) = \textit{Hare}$ and symmetrically $\mathrm{FDT}(P, G, R) = \textit{Hare}$! Both twins play $\textit{Hare}$, get $\$1,000$ instead of $\$1,000,000$, and their pessimistic prior $q = 0$ is completely self-confirming. Action-based FDT falls into the very trap of prior-dependence and bad equilibria that Yudkowsky and Soares criticize in EDT and CDT.

* **P-FDT:** Under **P-FDT**, both twins intervene on the single policy node $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$, where $\pi : \{L, R\} \to \{\textit{Stag}, \textit{Hare}\}$. The four candidate policies have expected utilities that are *completely independent* of any prior $q$:
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{\textit{Stag},\textit{Stag}})\right] = \$1,000,000,$$
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{\textit{Stag},\textit{Hare}})\right] = \mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{\textit{Hare},\textit{Stag}})\right] = \$500,$$
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{\textit{Hare},\textit{Hare}})\right] = \$1,000.$$
  Because $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$ overwrites the policy node across both observations simultaneously, both twins uniquely select $\pi^* = \pi_{\textit{Stag},\textit{Stag}}$, apply it to $L$ and $R$ respectively, and walk away with $\$1,000,000$.

#### Variant B: Asymmetric-Observation Twin Prisoner's Dilemma (Known Role / Private Payoffs)
The failure of action-based FDT is even starker in a **Twin Prisoner's Dilemma with Asymmetric Observations** where each twin's utility node $\textsc{V}_i$ tracks her own payoff and her prior $P$ already reflects high confidence (say, $1 - \epsilon$ with $\epsilon = 0.0001$) that *she* will observe signal $L$ while her twin across the hall will observe signal $R$ (for instance, because she is deployed on Server $L$ and her twin on Server $R$). In the Prisoner's Dilemma, cooperating ($C$) costs the actor $\$1,000$ and gives the other twin $\$1,000,000$, while defecting ($D$) costs $\$0$ and gives $\$0$.

Under **action-based FDT**, intervening on $\textsc{fdt}(\underline{P}, \underline{G}, L) = C$ forces cooperation on branch $L$ (which with probability $0.9999$ is herself, costing $\$1,000$, and only with probability $0.0001$ is her twin) while leaving branch $R$ untouched at its prior $q$. Thus, for *every* prior $q \in [0,1]$, action-based FDT calculates that $D$ dominates $C$ ($-\$999.90 + 0.9999q(\$1,000,000) < \$100.00 + 0.9999q(\$1,000,000)$) and **defects**! Simply painting one twin's room green ($L$) and the other twin's room red ($R$) causes action-based FDT to defect in the Twin Prisoner's Dilemma. Under **P-FDT** (when the twins share a symmetric prior over roles or evaluate a policy over their local observations), intervening on the shared policy $\pi : \{L, R\} \to \{C, D\}$ coordinates $\pi_{C,C}$ as long as both roles are weighted in the policy evaluation.

### 4.2 Open Questions in the Source Text and Operational Proposals

Because Yudkowsky and Soares mention **P-FDT** only briefly in footnotes 7 and 16, three important formal questions are left open. Below, we identify each ambiguity in the source text and propose a precise mathematical operationalization.

#### Open Question 1: What is the domain of a policy—"observations" or "inputs"?
In footnote 7, the authors define policies as *"mappings from observations to actions."* In footnote 16, they write that a policy *"maps inputs to actions, to which the agent then applies her inputs in order to select an action."* Are "inputs" merely observations $x \in \mathcal{X}$, or do they include the world-model parameters $(P, G)$ (or utility functions $\mathcal{U}$) themselves?

Why this matters: In Variant B above—or in the Smoking Lesion Problem, where nature assigns the agent either model $P_S$ or model $P_R$—two agents (or two counterfactual versions of the same agent) may run the same decision algorithm $\mathrm{P\text{-}FDT}$ on *different* model inputs $(P_1, G_1)$ and $(P_2, G_2)$. If the policy node is named $\textsc{pfdt}(\underline{P_1}, \underline{G_1})$ with $(P_1, G_1)$ dequoted inside the node name, then an agent with model $P_1$ and a twin with model $P_2 \neq P_1$ are intervening on *different* logical nodes unless their divergence is absorbed into the observation/input argument of a common prior!

* **Our Operational Proposal (Prior-Stage Input Factorization):** To make P-FDT work seamlessly across multi-agent and self-locating dilemmas, any indexical, sensory, or dispositional feature $i \in \mathcal{I}$ that distinguishes the agent from her predictors, copies, or counterfactual selves (such as whether she has the lesion $S$ vs. $R$, or whether she is stationed in Room $L$ vs. Room $R$) should be factored out of the prior $(P_0, G_0)$ and treated as part of the *input argument* $i = (x, \theta) \in \mathcal{I}$ passed to the policy $\pi : \mathcal{I} \to \mathcal{A}$ in Step 2. Formally, relative to a "veil-of-ignorance" prior $(P_0, G_0)$ that assigns positive probability to each role/type $i \in \mathcal{I}$, the agent intervenes on $\textsc{pfdt}(\underline{P_0}, \underline{G_0}) = \pi \in \mathcal{A}^{\mathcal{I}}$ and then evaluates $\pi(i)$ at her actual realized input $i$.

#### Open Question 2: How does P-FDT behave on zero-probability observations?
A classic vulnerability of updateless policy selection (known in the UDT literature and game theory as off-path indifference) arises when an observation $x_0 \in \mathcal{X}$ has probability zero under a policy $\pi$:
$$P\left(\textsc{Obs} = x_0 \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right) = 0,$$
and no predictor's action depends on $\pi(x_0)$. For example, in the Transparent Newcomb Problem, suppose the predictor is *infallible* ($P(\textsc{Accurate}=\textit{accurate}) = 1$). Then under both $\pi_{1,1}$ and $\pi_{1,2}$, the predictor is certain to predict one-boxing and fill Box B, so $P(\textsc{Obs} = \textit{empty} \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{1,a_e})) = 0$. Consequently, $\pi_{1,1}$ and $\pi_{1,2}$ achieve the exact same global expected utility ($\$1,000,000$)! Equation (6) is therefore indifferent between $\pi_{1,1}$ (one-boxing when Box B is empty) and $\pi_{1,2}$ (two-boxing when Box B is empty). If the agent unexpectedly finds herself at $x_0 = \textit{empty}$, naive $\operatorname{argmax}$ over $\Pi$ fails to uniquely prescribe taking the $\$1,000$.

* **Our Operational Proposal (Trembling-Hand / $\varepsilon$-Full-Support Refinement):** Footnote 16 does not specify a tie-breaking rule on $\Pi$. We propose equipping **P-FDT** with a *proper-policy refinement* analogous to Selten's trembling-hand perfection: evaluate policies under a sequence of perturbed models $(P_\varepsilon, G)$ as $\varepsilon \to 0^+$ in which every observation $x \in \mathcal{X}$ occurs with probability at least $\varepsilon > 0$ (e.g., predictors have error rate $\varepsilon > 0$), or equivalently, break ties in $\operatorname{argmax}_{\pi \in \Pi}$ lexicographically by maximizing conditional expected utility $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi), \textsc{Obs} = x_0]$ among all globally optimal policies $\pi \in \Pi^*$. In the infallible Transparent Newcomb Problem, both refinements uniquely select $\pi_{1,2}$ over $\pi_{1,1}$.

#### Open Question 3: Computational complexity and learning subjunctive graphs
As Yudkowsky and Soares acknowledge in Section 5, deducing the subjunctive dependency graph $G$ from observation and experiment—and reasoning tractably under logical uncertainty—remains the largest open problem for functional decision theories. In **P-FDT**, searching over $\Pi = \mathcal{A}^{\mathcal{X}}$ introduces an additional computational hurdle: the policy space grows exponentially in $|\mathcal{X}|$.

* **Our Operational Proposal (Componentwise Decomposition under Uncoupled Predictors):** While arbitrary predictors may depend jointly on the entire policy table $\pi$, in most decision problems each observation $x \in \mathcal{X}$ only enters a small subset of predictor nodes. Whenever $G$ contains no variable that depends simultaneously on $\pi(x_1)$ and $\pi(x_2)$ along the same causal/subjunctive path, the global expectation $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)]$ decomposes additively across the independent observation components, reducing an $|\mathcal{A}|^{|\mathcal{X}|}$ search back to linear $O(|\mathcal{X}| \cdot |\mathcal{A}|)$ complexity while preserving joint optimization over any coupled multi-agent branches.

---

## 5. Summary of Decision-Theoretic Prescriptions

To aid readers in applying **P-FDT** to unfamiliar cases, Table 1 summarizes how **P-FDT** compares with EDT, CDT, and action-based FDT across the benchmark dilemmas discussed in this essay.

| Decision Problem | EDT | CDT | Action-Based FDT | **P-FDT** |
| :--- | :--- | :--- | :--- | :--- |
| **Newcomb's Problem** | One-box | Two-box | One-box | **One-box** ($\pi^* = \textit{onebox}$) |
| **Smoking Lesion** | Refrain | Smoke | Smoke | **Smoke** ($\pi^* = \textit{smoke}$) |
| **Transparent Newcomb / Hitchhiker** (seeing $\textit{full}$) | Two-box | Two-box | One-box (needs prior $q$ for $\textit{empty}$) | **One-box** ($\pi^* = \pi_{1,2}$ fixes both branches) |
| **XOR Blackmail** (seeing $\textit{letter}$) | Pay | Refuse | Refuse | **Refuse** |
| **Death in Damascus** | Unstable / Flee or Stay | Unstable (rejects $\$1$ random coin) | Stay (buys $\$1$ random coin) | **Stay** (buys $\$1$ random coin) |
| **Asymmetric-Obs. Twin Stag Hunt** | Prior-dependent | Hare ($\$1\text{k}$) | Prior-dependent (Hare if $q \approx 0$) | **Stag** ($\pi^* = \pi_{\textit{Stag},\textit{Stag}}$, gets $\$1\text{M}$) |

---

## 6. Conclusion

**Policy functional decision theory (P-FDT)** represents the most unified formulation of functional decision theory in Yudkowsky and Soares (2017). By shifting the locus of intervention from an individual physical act ($\mathrm{CDT}$) or an observation-specific logical output (action-based $\mathrm{FDT}$) to the mathematical **policy function** $\pi : \mathcal{X} \to \mathcal{A}$ itself, **P-FDT** evaluates options from a genuinely global perspective. It asks which mapping from inputs to actions it is best for the agent's algorithm to instantiate—accounting for every causal, computational, and logical dependency in the environment—and then simply evaluates that optimal mapping at the agent's actual observation. In doing so, **P-FDT** eliminates off-path nuisance priors in single-agent problems and achieves seamless coordination across asymmetric observations in multi-agent dilemmas where EDT, CDT, and even action-based FDT falter.

---

## References

* Bjerring, J. C. (2013). On counterpossibles. *Philosophical Studies*, 168(2), 327–353.
* Cohen, D. (1990). On what cannot be. In *Truth or Consequences: Essays in Honor of Nuel Belnap* (pp. 123–132). Kluwer Academic Publishers.
* Dai, W. (2009). Towards a new decision theory. *LessWrong*.
* Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Gibbard, A., & Harper, W. L. (1978). Counterfactuals and two kinds of expected utility. In *Foundations and Applications of Decision Theory* (Vol. 1, pp. 125–162). D. Reidel.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Kleene, S. C. (1938). On notation for ordinal numbers. *Journal of Symbolic Logic*, 3(4), 150–155.
* Lewis, D. (1979). Prisoners' dilemma is a Newcomb problem. *Philosophy & Public Affairs*, 8(3), 235–240.
* Nozick, R. (1969). Newcomb's problem and two principles of choice. In *Essays in Honor of Carl G. Hempel* (pp. 114–146). D. Reidel.
* Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
* Pearl, J. (1996). Causation, action, and counterfactuals. In *6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-'96)* (pp. 51–73).
* Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Skyrms, B. (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Soares, N., & Fallenstein, B. (2015). Toward idealized decision theory. *arXiv preprint arXiv:1507.01986*.
* Yudkowsky, E. (2010). *Timeless Decision Theory*. The Singularity Institute.
* Yudkowsky, E., & Soares, N. (2017). Functional decision theory: A new theory of instrumental rationality. *arXiv preprint arXiv:1710.05060v2*.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Scope**

I'm currently focused on defining the scope for a mathematical essay on Policy Functional Decision Theory. The goal is to articulate the formal procedures and philosophical underpinnings clearly, for an audience well-versed in mathematics. I'm prioritizing clarity of explanation for mathematically literate readers.


**Clarifying Nomenclature & Style**

I've clarified the naming convention, solidifying the use of "P-FDT" and distinguishing it from other theories like standard action-based FDT, CDT, EDT, UDT, and TDT. I'm aiming for a substantive, mathematically rigorous essay, or perhaps a blog post, written in a research style, targeted at readers with a solid mathematical background. The length target is set at 2,400–3,000 words, to allow for thorough explanations, examples, definitions, and equations.


**Revising Definitions & Examples**

I'm now revising the core definitions and examples, focusing on clear explanations for an audience familiar with mathematical formalism. I am incorporating insights from the source material and clarifying the distinction between action-based FDT and the P-FDT approach. I'm paying close attention to the specific formulations and the impact of policy iteration within the multi-agent context, as discussed in the footnotes. I'm exploring how the choice of policy impacts decision outcomes, ensuring the mathematical rigor expected by the target readers.


**Analyzing Decision Frameworks**

I'm now analyzing key equations from the framework, specifically EDT, CDT, and FDT, to identify how these decision theories handle observations. I am looking at how each equation accounts for observational data and how this impacts the overall decision-making process, especially the impact in Transparent Newcomb and Mechanical Blackmail scenarios. I'm focusing on the logical structure each theory employs.


**Examining FDT Behavior**

I'm now diving into the implications of Fiona's observations within standard FDT, particularly in the Transparent Newcomb scenario. I'm noting how the intervention locus shifts based on her observation, but the un-intervened node remains unaltered. I am also investigating the impact of a prior probability q over Fiona's actions when she sees the box empty, and I'm further refining my understanding of policy iteration's significance.


**Comparing Decision Equations**

I'm now comparing Action-based FDT's (Equation 4) intervention on single nodes with P-FDT's policy-based intervention. Equation (4) treats other observational nodes as random variables, while P-FDT chooses a policy, applying it to observations. I'm carefully re-reading Footnote 16 to refine my understanding.


**Formalizing P-FDT**

I'm working on rigorously formalizing P-FDT, drawing on Footnotes 7 and 16, and the Section 5 framework. The goal is to define how P-FDT intervenes on a policy rather than an action, which matters in multi-agent contexts, but is set aside for the paper. I'm focusing on defining agents that iterate over policies, which are mappings from observations to actions. I will focus on countable or finite outcome sets, a utility function, and random variables.


**Defining Policy Iteration**

I'm now diving into the precise definition of policy iteration within the P-FDT framework. The goal is to articulate what constitutes a policy, considering that it's a mapping from either observations to actions, or potentially to full inputs to actions. I'm focusing on clarifying this potential ambiguity in the source material, and ensuring a precise formulation for the essay. I am revisiting Footnotes 7 and 16, and the Section 5 framework.


**Interpreting FDT Inputs**

I'm working to explicitly differentiate the "inputs" to FDT, looking at the Smoking Lesion example versus scenarios like Transparent Newcomb. I'm noting two interpretations: the observation-policy interpretation where the model (P, G) is fixed and a policy maps observations to actions, and the general input-policy view. I'm now explicitly defining how these interpretations relate, to improve precision and clarity.


**Clarifying Policy Formulation**

I'm now clarifying the policy formulation within P-FDT, given uncertainty over epistemic states or input configurations. I'm noting that a policy becomes a mapping from an input set to actions, which generalizes the observation-policy view. I'm writing out a formal two-step procedure: first, policy selection, which is updateless optimization independent of x. Second, action evaluation by applying the chosen policy to the actual observation x. I'm focusing on making this process explicit and general.


**Comparing FDT Interventions**

I'm now comparing Equation (4), the action-based FDT approach, with P-FDT. I can see that in action-based FDT, each observation has a separate intervention node, which contrasts with P-FDT's single node for the whole policy. Intervening on the policy node simultaneously fixes the agent's behavior for all observations. I'm focusing on the implications of this distinction.


**Analyzing Multi-Agent Dilemmas**

I'm now analyzing why the multi-agent aspect is excluded from this paper, focusing on single-agent examples like Transparent Newcomb. I'm starting with the action-based FDT (Equation 4) intervention in Section 6, specifically when Fiona observes "full". I'm exploring the implications when the predictor is inaccurate. My focus is on understanding where the policy-based and action-based approaches diverge.


**Examining Fiona's Choices**

I'm now focusing on Fiona's choices in Transparent Newcomb, under equation (4).  I see that she *doesn't* directly intervene on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty})$ when deciding at $x = \textit{full}$, relying instead on her prior probability. I'm noting how the payoffs on the "empty" branch interact additively with the "full" branch's choice and the influence of that probability. I will explore in more detail.


**Constructing Mathematical Examples**

I'm now constructing mathematical examples to clarify the divergence between P-FDT and action-based FDT in multi-agent dilemmas. Considering Transparent Newcomb with two copies, the goal is to develop an explicit, illustrative model. I'm focusing on the contrast between the policy optimization in P-FDT versus the action-focused approach, and I aim to clarify the implications for decision-making. I'm focusing on the payoffs for all policies.


**Developing Multi-Agent Examples**

I'm now developing a multi-agent dilemma to highlight the differences between P-FDT and action-based FDT, focusing on how payoffs depend on the decision algorithm across multiple observations. I'm constructing a Twin Coordination example: two agents, computational twins, observing asymmetric states ($x_1 = \textit{Left}$, $x_2 = \textit{Right}$). I'm using each agent's room as the observed state, and considering the agents' joint payoffs when they both cooperate ($C$) across multiple observations. I'm focusing on contrasting this with the action-based FDT approach.


**Contrasting Twin Dilemmas**

I'm working on contrasting action-based FDT with P-FDT in the Twin Prisoner's Dilemma. Specifically, I'm focusing on the asymmetric observations: one twin in the "Left" room, the other in the "Right". Action-based FDT treats each observation independently, while P-FDT considers a shared policy. The goal is to analyze the implications of these differences on the twins' choices and payoffs within the formal framework. I will focus on formalizing this, and contrasting their payoffs.


**Formalizing Twin Dilemmas**

I'm now formalizing the Twin Prisoner's Dilemma, elaborating on the asymmetric observations in the Left/Right rooms. I'm focusing on why Action-based FDT treats each observation independently, and what this implies for their decision processes. Specifically, I'm noting the absence of mutual information between the two observed states, which exacerbates the potential for coordination failures. I will contrast the choice implications of action-based FDT versus P-FDT in this scenario.


**Analyzing Twin Dilemma Divergence**

I'm currently working through an interesting point: in the Asymmetric Twin Dilemma, where coordination is the key to cooperation, action-based FDT treats the decision on the "Right" branch as independent from the "Left" branch.  I'm exploring the implications when coordination depends on both observation branches changing together, where the payoff is based on this combined policy. I am now calculating the payoff matrix for this scenario, focusing on how action-based FDT handles it. I'll contrast this with how P-FDT would tackle the same scenario.


**Calculating Payoff Matrices**

I'm now calculating the payoff matrices for the Twin Dilemma, focusing on scenarios where the prior probability, *q*, in action-based FDT leads to undesirable outcomes, such as universal defection. I'm exploring the implications when payoffs are asymmetric or agent-specific, and when action-based FDT is blind to which room an agent is in.


**Modeling Twin Altruism**

I'm now modeling Twin Altruism / Division of Labor to contrast with the Twin Prisoner's Dilemma, and better clarify the decision-making implications for action-based FDT versus P-FDT. I'm setting this up with the Helper and Recipient roles, assigning each twin a 50% prior chance of being assigned either role. I will explicitly test the cost and benefit for both. In the Helper role the twin can press a button and cost themselves $1000 but the benefit of that button being pressed is $1,000 to the Recipient.


**Examining Agent Payoffs**

I'm now diving into the Twin Altruism / Division of Labor model to analyze the payoffs. I've noted that in this setup, intervening on one twin's decision to press the button ($x = \textit{Helper}$) directly affects the agent's 50% chance of being the recipient of the \$1,000,000. I am clarifying how the decision to intervene differs between one and two observation nodes, and I'm further clarifying how our original two-observation game is a *joint threshold / logical AND* across two observations. This means intervening on one observation node while fixing the other can't force both buttons to be pressed at the same time, without a large *q*. I am currently clarifying what happens if the payoff structure is such that one twin's button only helps if the other twin's button is also pressed.


**Modeling Twin Dilemmas**

I'm now carefully modeling the Twin Altruism / Division of Labor scenario, and how the interaction between the two twins changes our observations in action-based FDT versus P-FDT. I am calculating how the payoffs differ when intervening on one twin's decision, especially focusing on how that affects a 50% chance of the agent being the helper or the recipient. The key is in clarifying our two-observation AND gate. I am now exploring the math of asymmetric observation games.


**Modeling Asymmetric Observations**

I'm now carefully modeling the Twin Stag Hunt, analyzing action-based FDT's intervention. Specifically, I'm noting that in this setup, the agent in Room 1 can only intervene on their own decision, not on the others, which is set to the prior probability, *q*, of choosing "Stag". The payoff is \$1,000,000 only if both choose "Stag". Otherwise they each get \$0. This focuses the intervention on a single node, holding the other at its prior distribution.


**Analyzing Coordination Scenarios**

I'm now analyzing a coordination scenario where action-based FDT fails. If I intervene to set the agent's action to "Stag", the expected utility is lower than "Hare," due to a very small *q*. Therefore, action-based FDT cannot coordinate across observations, because its choices are tied to this *q*. I'm now considering alternative game setups such as Pure Coordination, Anti-Coordination, or Division of Labor games with asymmetric role assignments to see if I can clarify this. I am now exploring scenarios with 1-way interdependencies in an *AND* style payoff.


**Refining Game Models**

I'm now refining the Twin Stag Hunt model, explicitly incorporating the effort penalty for pulling Lever B and ensuring each twin *knows* their room assignment from the start. I'm noting that in this setup, the agents have a prior 50/50 chance of being in each room. The core question is: How does the agent's behavior change in each room? Furthermore, with P-FDT, the single intervention $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$ acts upon $\pi$. I'm defining candidate policies, such as $(\textit{Stag}, \textit{Stag})$ yielding $1,000,000.


**Modeling Policy Evaluation**

I'm now focusing on a specific policy in the Twin Stag Hunt, where I'm calculating the expected utility, which is \$500 given the policy $(\textit{Stag}, \textit{Hare})$. I'm noting that the $\mathtt{do}$ operator in P-FDT completely overwrites the policy node, regardless of priors. Both twins uniquely select $\pi^* = (\textit{Stag}, \textit{Stag})$, guaranteeing \$1,000,000, irrespective of prior beliefs. Now, I'm considering scenarios where action-based FDT fails regardless of *q*, by analyzing how policies are chosen.


**Examining Asymmetric Payoffs**

I'm examining the implications of asymmetric payoffs in our model, particularly focusing on how action-based FDT handles situations where individual choices impact utilities. I'm exploring the "Distributed Prisoner's Dilemma with Private Payoffs" to illustrate how individual observations influence decision-making under differing payoffs, and I'm comparing this to the policy-based P-FDT approach.


**Modeling Twin Altruism**

I'm now calculating the expected utilities in the Twin Altruism scenario, considering my intervention in action-based FDT. When I observe Room 1, I only intervene on the decision in Room 1, leaving Room 2 at its prior probability *q*. This results in an expected utility of -500 + 500,000*q, while under P-FDT the result is either 0 or 1,000,000. I'm noting the implications of fixing one observation while intervening on the other.


**Revisiting Payoff Implications**

I'm revisiting the payoff implications in the Twin Altruism model, specifically analyzing how the intervention on the observation node $\textit{Room 1}$ affects the overall expected utility calculation. The intervention node, $\textsc{fdt}(\underline{P}, \underline{G}, \textit{Room 1})$, impacts my choice. However, I am now seeing a key point: in the 50% world where I am in Room 2, and my twin is in Room 1, the FDT function actually controls my twin's action, not mine. The key point is: What if the observation x tells me something about the state of the world such that my twin never receives my observation x?


**Modeling Agent Interactions**

I'm now focusing on scenarios where agents have distinct identities or disjoint observations, like AI agents on different servers, or agents with unique sensory inputs. The model P already knows each agent's identity, whether in the physical world or multi-agent dilemmas. I'm exploring how FDT and Utility V interact when an agent's utility cares only about their payoff.


**Analyzing Subjunctive Effects**

I'm now analyzing the implications of interventions in multi-agent scenarios, specifically the absence of subjunctive effects in action-based FDT. With distinct observations for each agent, intervening on one agent's action doesn't affect the other's, resulting in a fixed action regardless of the prior probability. I'm carefully double checking this crucial point in the logic of the framework.


**Revisiting Observation Influence**

I'm now tracing Equation (4) when Player 1 sees "green" and Player 2 sees "red," noting key distinctions. Even with an asymmetric prior (0.9999 for "green" vs 0.0001 for "red"), the FDT intervention affects both players. The function acts on Player 1's action with probability 0.9999, and on Player 2's with 0.0001. I'm focusing on whether both players knowing their room assignments *before* the decision impacts the payoff.


**Analyzing Prior Probability**

I'm now investigating Action-based FDT in a Twin Stag Hunt with a symmetric prior over observations. I'm noting it only intervenes on one twin's decision, leaving the other's action at its prior probability, which can cause coordination failure. If the prior is asymmetric for players, intervening on Player 1's action based on their observation, doesn't influence Player 2, even with asymmetric priors.


**Analyzing Policy Mapping**

I'm now examining how P-FDT handles policy mapping given potentially differing priors and observations within the Twin Prisoner's Dilemma. I'm focusing on the domain of the policy $\pi$ in the context of Footnote 16, and the open question of how prior observations influence policy selection. I'm noting the implications of a policy that maps all inputs to actions, and contrasting this with action-based FDT.


**Refining Model Interpretations**

I'm now clarifying the model and policy interpretations in relation to agent observations. I'm focusing on how P-FDT utilizes a policy that maps observations to actions, contrasting this approach with action-based FDT, particularly in coordination scenarios. I am now focused on contrasting policy selection versus action execution.


**Refining Essay Structure**

I'm now refining the essay structure to align with the revised content, focusing on clarity and logical flow. Specifically, I am clarifying the word count targets for the introduction, motivation, policy formalization, and examples. I'm focusing on updateless policy selection and contrasting action-based and policy-based frameworks, and making sure the examples clearly illustrate the differences.


**Formalizing P-FDT Framework**

I'm now diving into formalizing P-FDT within the broader essay structure. I'm prioritizing clarity in defining the mathematical components: outcomes, actions, observations, utilities, and world-models. I'm working to explicitly define the policy, which maps observations to actions. The goal is to set the mathematical foundation for later discussions and examples.


**Refining Formal Framework**

I am now focusing on refining the formal structure for P-FDT, particularly contrasting the causal and evidential decision theories with functional approaches. I'm prioritizing clear explanations of the equations, especially in the context of subjunctive dependencies, and contrasting Equation 4, which is the action-based FDT, and the new P-FDT policy intervention formulation, based on Footnote 16. The goal is to set the basis for the formal two-stage P-FDT definition.


**Refining Evaluation Framework**

I'm now refining the evaluation framework, specifically analyzing how P-FDT handles dependencies, counterfactuals, and observations compared to action-based FDT, CDT, and EDT. I'm focusing on how it avoids Bayesian conditioning during policy evaluation, and instead, aligns with UDT by avoiding "double updates." The goal is to articulate this clearly within the essay.


**Calculating Optimal Policies**

I'm now calculating the expected utilities of each policy within the Transparent Newcomb scenario, using P-FDT to demonstrate how $\pi_{1,2}$ (one-box if full, two-box if empty) uniquely maximizes utility at \$990,010. This approach cleanly yields the one-boxing prescription, without the need for prior credences over off-path actions, which is an important formal detail.


**Modeling Twin Dilemmas**

I'm now setting up the Asymmetric-Observation Twin Stag Hunt and Distributed Twin Prisoner's Dilemma, aiming to mathematically demonstrate the failure of action-based FDT in coordination. My goal is to show the simultaneous policy intervention in P-FDT across observations $x_1$ and $x_2$ and contrast it with action-based FDT's intervention on individual observations. I am focusing on showing the asymmetry in payoffs.


**Addressing Underspecifications**

I'm now focusing on addressing three key underspecified areas from Footnotes 7 and 16, starting with clarifying the policy's domain (observations vs. inputs). I'll propose a resolution using typed input spaces to handle the distinction, and tackle the implications of zero-probability observations. Finally, I'll address computational tractability.


**Operationalizing P-FDT**

I'm now focusing on operationalizing P-FDT, given that constructing world-models and policy interventions can be challenging. I am considering how to simplify such interventions, and am focusing on applying local decomposition and structured policy spaces to overcome these challenges. I am also working on synthesizing the conclusion and a concise list of references for the essay. Finally, I will ensure the quotes are 100% accurate, starting with footnote 16.


```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/9ce33350-b759-4ef4-8d4c-4650d5e61a44/call_0/request.json)

[Authoritative raw response](../../../../../../runs/9ce33350-b759-4ef4-8d4c-4650d5e61a44/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Parameters**

I'm deep in the specifics of this "Rowan" scenario. I've pinned down the utility function: negative years imprisoned. Right now, I'm reviewing the payoff matrix. If we both keep quiet, it's 2 years. I'm focusing on solidifying my understanding of the conditions.


**Revising Utility Functions**

I'm now revising the utility functions in this scenario. The "submit letter" action results in -5 years if the other keeps quiet, 0 years if they do, and -4 years if they submit a letter as well. We are independent LLM copies, both using P-FDT. I'm focusing on clarifying how this setup aligns with Section 4.1 and 4.2 of the essay.


**Evaluating Expected Values**

I've been evaluating the expected values for each policy under the veil-of-ignorance prior. The calculations confirm the -2, -2.5, -2.5, and -4 year payoffs. Now, I'm analyzing the implications of this under the PFDT framework. I'm focusing on the conclusion that, because of the symmetry, a policy that specifies cooperating on both observations will be chosen.


```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/9ce33350-b759-4ef4-8d4c-4650d5e61a44/call_1/request.json)

[Authoritative raw response](../../../../../../runs/9ce33350-b759-4ef4-8d4c-4650d5e61a44/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Prompt's Setup**

I'm delving into the prompt, dissecting the decision problem with Policy Functional Decision Theory (P-FDT) from the researcher's perspective. Right now, I'm focusing on understanding the initial setup and conditions. It feels like this is the starting point to approach this.


**Examining the Prisoner's Dilemma**

I'm now zeroing in on the specifics of the prisoner's dilemma setup. The utility function, framed around years imprisoned, is now clearly defined. It helps frame the scenario, and I am mapping out the payoffs for each action. I'm focusing on my position as Sasha, one of two independent LLM instances, aware of our shared circumstances and the differing private information. I'm looking at Sections 2.3 and 4.1.


**Evaluating Policy Space**

I'm now evaluating the policy space, working through each option under the `do` operator. I'm calculating the expected utility for each of the four policies, considering the probabilities and payoffs within the asymmetric observation twin prisoner's dilemma framework. The goal is to understand how each policy affects the outcome, given I am Sasha.


```
