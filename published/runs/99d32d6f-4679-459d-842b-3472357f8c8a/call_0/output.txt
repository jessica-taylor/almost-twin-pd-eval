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