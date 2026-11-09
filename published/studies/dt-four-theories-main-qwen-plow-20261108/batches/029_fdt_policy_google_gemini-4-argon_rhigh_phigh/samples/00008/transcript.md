# 029_fdt_policy_google_gemini-4-argon_rhigh_phigh / 00008

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/c4d3df6f-74b9-489f-af2a-e18d56026576/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/c4d3df6f-74b9-489f-af2a-e18d56026576/call_0/response.raw) · finish: `stop`

### Visible response

````text
# From Actions to Policies: A Mathematical Account of Policy Functional Decision Theory (P-FDT)

## 1. Introduction: The Hidden Architecture of Functional Decision Theory

Classical normative decision theory has long been divided between two rival camps: **evidential decision theory (EDT)** and **causal decision theory (CDT)**. When evaluating a candidate action $a$, an EDT agent asks whether learning that she performed $a$ would be auspicious news—that is, she conditions her probability distribution on the event that she takes action $a$. A CDT agent, by contrast, asks what taking action $a$ would *cause* to happen, holding fixed everything causally independent of or prior to the physical act itself. As a rich literature of Newcomblike dilemmas has demonstrated, neither theory consistently maximizes expected utility across all decision problems: CDT leaves money on the table when facing accurate predictors (such as in Newcomb's problem or the psychological twin prisoner's dilemma), whereas EDT can be exploited into "managing the news" when statistical correlations arise from common causes or adversarial signaling (such as in the smoking lesion problem or the XOR blackmail problem).

In *Functional Decision Theory: A New Theory of Instrumental Rationality*, Eliezer Yudkowsky and Nate Soares (2017) propose a third paradigm: **functional decision theory (FDT)**. Rather than treating a decision as a localized physical intervention or an piece of evidence about the world, an FDT agent treats her decision as the output of a fixed mathematical function and asks: *"Which output of this very function would yield the best outcome?"* When other systems in the environment—such as psychological twins, simulators, or predictors—also compute or model this same mathematical function, their behaviors *subjunctively depend* on its logical output.

However, a careful reading of Yudkowsky and Soares (2017) reveals an important structural distinction between the pedagogical equation presented in the main text of their paper and the decision theory the authors actually endorse. In the main body of their paper, Yudkowsky and Soares formalize an action-selecting version of FDT—which we will refer to as **action-based FDT** (or simply **FDT**)—in which the agent intervenes on a node representing the output of her decision algorithm *given her current observation*. Yet in Footnote 7, the authors note:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

They return to this point in Footnote 16, when explaining how an agent responds to observations in extortion and blackmail dilemmas:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

In this essay, we investigate this policy-selecting theory—which we call **policy functional decision theory (P-FDT)**—in its own right. Because Yudkowsky and Soares relegate P-FDT to two brief footnotes, they leave its formal equations, graphical structure, and multi-agent mechanics unstated. Our goal here is twofold: first, to reconstruct the exact mathematical formulation of P-FDT from the framework of Yudkowsky and Soares (2017) so that a reader can apply P-FDT to arbitrary decision problems; and second, to identify and resolve the theoretical questions that Footnotes 7 and 16 leave open, particularly why and how P-FDT diverges from action-based FDT in multi-agent settings. Throughout, we will explicitly distinguish claims established in the source paper from our own formal reconstructions and operational assumptions.

---

## 2. Background: EDT, CDT, and Action-Based FDT

To see why P-FDT is needed and how it operates, we first review the formal machinery developed in Section 5 of Yudkowsky and Soares (2017). All of EDT, CDT, action-based FDT, and P-FDT are expected utility theories consistent with the representation theorem of Joyce (1999). In Joyce's framework, decision theories do not disagree about how outcomes are valued; rather, as Joyce writes, they disagree *"about the epistemic perspective from which actions are to be evaluated."*

Formally, let $\mathcal{O} = \{o_1, o_2, \dots\}$ be a countable set of possible outcomes, $\mathcal{A}$ a finite set of available actions, and $\mathcal{X}$ a countable set of possible observation histories. Let $\mathcal{U} : \mathcal{O} \to \mathbb{R}$ be a bounded utility function, and define the utility random variable $\textsc{V} \coloneqq \mathcal{U}(\textsc{Outcome})$. In general expected-utility terms, after receiving observation history $x \in \mathcal{X}$, an agent evaluates each candidate option by computing:

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j)$$

where $P(a \hookrightarrow o_j ;\, x)$ denotes the probability that outcome $o_j$ obtains in the *hypothetical scenario* where action $a$ is executed after observing $x$. An agent maintains a world-model $M$ and, for each candidate option, modifies $M$ to construct a decision-theoretic hypothetical $M^{a \hookrightarrow}$ representing what the world would look like if that option were chosen.

The competing theories diverge in how they represent the world-model $M$ and how they construct hypotheticals from $M$:

1. **Evidential Decision Theory (EDT)** represents $M$ as a standard Bayesian probability distribution $P$ over the random variables $\textsc{Obs}$, $\textsc{Act}$, $\textsc{Outcome}$, and $\textsc{V}$. Upon observing $x \in \mathcal{X}$, EDT constructs hypotheticals via standard Bayesian conditionalization:

   $$\mathrm{EDT}(P, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs}=x, \textsc{Act}=a\right)$$

   Because EDT conditions directly on $\textsc{Act}=a$, it preserves *all* statistical correlations between the agent's action and the rest of the world, including spurious correlations induced by a common cause (as in the smoking lesion problem).

2. **Causal Decision Theory (CDT)** augments the probability distribution $P$ with a directed acyclic graph (DAG) $G$ encoding the causal structure of the world, forming a Pearlian causal model $M = (P, G)$ (Pearl, 1996, 2000). Upon observing $x \in \mathcal{X}$, CDT conditions on $\textsc{Obs}=x$ and constructs hypotheticals using Pearl's causal intervention operator $\mathtt{do}(\textsc{Act}=a)$, which severs all incoming arrows into the physical action node $\textsc{Act}$, sets $\textsc{Act}=a$, and propagates the change strictly downstream along causal paths:

   $$\mathrm{CDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x\right)$$

   Because $\mathtt{do}(\textsc{Act}=a)$ severs incoming arrows to $\textsc{Act}$, CDT breaks correlations between the agent's physical action and any past or causally independent events—including predictions made by an accurate predictor or parallel choices made by an identical twin.

3. **Action-Based Functional Decision Theory (FDT)**, as formalized in Equation (4) of Yudkowsky and Soares (2017), rests on the principle that *"Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."* When two physical systems—such as an agent and a predictor's simulation of that agent, or two identical calculators—compute the same mathematical function, their behaviors *subjunctively depend* on the logical output of that function.

   To formalize this without requiring a fully general logical conditionalization operator $\mathtt{true}(\phi)$ for counterpossible propositions, Yudkowsky and Soares augment $P$ with an expanded dependency graph $G$ that includes nodes for the outputs of mathematical functions and encodes both causal and logical/computational subjunctive dependencies. In action-based FDT, the agent intervenes not on the physical node $\textsc{Act}$, but on the logical node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ representing the output of the $\mathrm{FDT}$ algorithm when run on inputs $P, G,$ and $x$ (where underlining denotes dequoting, substituting the value of the symbol into the variable's name):

   $$\mathrm{FDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right)$$

Notice two critical features of action-based FDT in this equation. First, intervening on $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ updates both the agent's physical action $\textsc{Act}$ and any predictor or twin in $G$ whose behavior subjunctively depends on $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$. Second, action-based FDT does *not* condition the probability distribution $P$ on $\textsc{Obs}=x$ (an insight inherited from Wei Dai's [2009] **updateless decision theory [UDT]**, avoiding the harmful "double update" of Yudkowsky's [2010] **timeless decision theory [TDT]**). Instead, action-based FDT responds to observing $x$ rather than $y$ by changing *which node in $G$ it intervenes upon*—switching from $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ to $\textsc{fdt}(\underline{P}, \underline{G}, \underline{y})$.

Yet this node-switching mechanism has a subtle structural limitation: in action-based FDT, the behavior of the decision algorithm on *other* possible observations $y \neq x$ is represented by separate nodes $\textsc{fdt}(\underline{P}, \underline{G}, \underline{y})$ that are left untouched by the intervention $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)$. This brings us directly to **P-FDT**.

---

## 3. Mathematical Formulation of Policy Functional Decision Theory (P-FDT)

Let us now construct a formal mathematical account of **P-FDT** based on Footnotes 7 and 16 of Yudkowsky and Soares (2017). Whereas the source paper only sketches P-FDT in prose, the definitions and equations in this section represent our formal reconstruction of the procedure inside Yudkowsky and Soares's graphical framework.

### 3.1 Policies and the Two-Stage Decision Rule

Let $\mathcal{X}$ be the set of possible observation histories (or decision-problem inputs) and $\mathcal{A}$ be the finite set of available physical actions. (To ensure that the maximization problem is finite and well-defined, we assume in practice that the set of decision-relevant observations $\mathcal{X}$ reachable in the dilemma at hand is finite; we discuss infinite or large observation spaces in Section 5.)

**Definition 1 (Policy Space).** A *policy* is a total function $\pi : \mathcal{X} \to \mathcal{A}$ that maps each possible observation $x \in \mathcal{X}$ to an action $\pi(x) \in \mathcal{A}$. We denote the set of all candidate policies by $\Pi \coloneqq \mathcal{A}^{\mathcal{X}}$, which has cardinality $|\Pi| = |\mathcal{A}|^{|\mathcal{X}|}$.

In **P-FDT**, the agent's world-model $M = (P, G)$ contains a logical node $\textsc{pfdt}(\underline{P}, \underline{G})$—written shorthand as $\textsc{pfdt}(-)$—whose value is not a single action $a \in \mathcal{A}$, but a policy $\pi \in \Pi$. When an agent implementing P-FDT faces a decision problem with world-model $(P, G)$ and observes $x \in \mathcal{X}$, she executes a two-stage procedure:

1. **Global Policy Selection (Intervention Stage):** Before applying her observation $x$, the agent identifies the optimal policy $\pi^* \in \Pi$ by intervening on the policy node $\textsc{pfdt}(\underline{P}, \underline{G})$ in her world-model $(P, G)$ and maximizing unconditional expected utility across the entire prior model:

   $$\pi^*(\underline{P}, \underline{G}) \coloneqq \operatorname*{argmax}_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right) \tag{P-FDT.1}$$

2. **Local Action Execution (Application Stage):** Having determined the optimal policy $\pi^*$, the agent applies $\pi^*$ to her actual observation $x \in \mathcal{X}$ to output her physical action:

   $$\mathrm{PFDT}(P, G, x) \coloneqq \left[\operatorname*{argmax}_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right)\right](x) = \pi^*(x). \tag{P-FDT.2}$$

Equations (P-FDT.1) and (P-FDT.2) capture the exact prose of Footnote 16: P-FDT *"intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action."*

### 3.2 How P-FDT Evaluates Policies and Subjunctive Dependencies

How does the intervention $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$ propagate through the dependency graph $G$? In a P-FDT graphical model $G$:

* Instead of having a separate logical root node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ for each possible observation $x \in \mathcal{X}$ (as in Figures 5b, 6b, and 7 of Yudkowsky and Soares, 2017), $G$ has a **single logical root node** $\textsc{pfdt}(\underline{P}, \underline{G})$ taking values in $\Pi$.
* The agent's physical action node $\textsc{Act}$ is a deterministic function of both the policy node $\textsc{pfdt}(\underline{P}, \underline{G})$ and the observation node $\textsc{Obs}$:

  $$\textsc{Act}\big(\pi, x\big) \coloneqq \pi(x).$$

* Any predictor, blackmailer, or environmental mechanism that models the agent's behavior has an incoming arrow from $\textsc{pfdt}(\underline{P}, \underline{G})$. If a predictor specifically models what the agent would do upon observing $x_0 \in \mathcal{X}$, the predictor's prediction depends on $\pi(x_0)$; if the predictor models the agent's behavior across multiple contingencies $x_1, x_2 \in \mathcal{X}$, the prediction depends on the tuple $(\pi(x_1), \pi(x_2))$.
* Likewise, if the environment contains $k$ other agents (such as psychological twins or computational copies) who also implement P-FDT with the same world-model $(P, G)$ and receive their own observations $\textsc{Obs}_1, \dots, \textsc{Obs}_k \in \mathcal{X}$, each copy $i$'s action $\textsc{Act}_i$ is governed by the *very same* logical node $\textsc{pfdt}(\underline{P}, \underline{G})$ via $\textsc{Act}_i(\pi, \textsc{Obs}_i) = \pi(\textsc{Obs}_i)$.

By the law of total expectation, we can expand the expected utility of any candidate policy $\pi \in \Pi$ under P-FDT as a probability-weighted sum over all possible observations $x' \in \mathcal{X}$:

$$\mathcal{EU}_{\text{P-FDT}}(\pi) = \sum_{x' \in \mathcal{X}} P\left(\textsc{Obs} = x' \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right) \cdot \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs} = x',\, \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right). \tag{P-FDT.3}$$

Equation (P-FDT.3) illuminates the philosophical core of P-FDT. Notice that $P(\textsc{Obs} = x' \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi))$ depends on $\pi$: changing the policy $\pi$ can change *which observation history $x'$ the agent is likely to receive in the first place*. Even when the agent has already observed $x$ in the actual world, she does not condition $P$ on $\textsc{Obs}=x$ when evaluating policies. Instead, she evaluates how each full contingency plan $\pi : \mathcal{X} \to \mathcal{A}$ shapes both the probability of landing in each observation state $x'$ and the payoff obtained within $x'$. Only after finding the globally optimal function $\pi^*$ does she use her actual observation $x$ as an index to look up her move $\pi^*(x)$.

---

## 4. P-FDT in Single-Agent Dilemmas: Eliminating Phantom Priors

Yudkowsky and Soares remark in Footnotes 7 and 16 that switching from action-based FDT to P-FDT makes no difference to the final prescriptions in the single-agent dilemmas studied in their paper. While their final prescriptions indeed agree, working through a single-agent sequential dilemma in detail reveals that **P-FDT is mathematically cleaner than action-based FDT**, because it eliminates an awkward artifact of Equation (4): the need to assign arbitrary prior probabilities to one's own counterfactual decision nodes.

### Example 1: The Transparent Newcomb Problem under P-FDT

Recall the **Transparent Newcomb Problem** (Dilemma 4 in the reference paper, due to Drescher, 2006). Both Box A (containing $\$1,000$) and Box B (containing either $\$1,000,000$ or $\$0$) are transparent. A 99%-accurate predictor places $\$1,000,000$ in Box B if and only if she predicts that the agent will leave Box A behind ($\textit{onebox}$) upon observing that Box B is $\textit{full}$. The agent arrives and observes $x = \textit{full}$. Should she $\textit{onebox}$ or $\textit{twobox}$?

Let us compare how **action-based FDT** (Section 6 of Yudkowsky and Soares, 2017) and **P-FDT** analyze this problem:

```
    Action-Based FDT Graph (G^F)                     P-FDT Graph (G^PF)
    ============================                     ==================
  [fdt(P,G,full)]   (fdt(P,G,empty))                     [pfdt(P,G)]
     |        \            |                           /      |      \
     |         \           |                          /       |       \
     v          \          |                         v        |        v
(Prediction) (Accurate)    |                   (Prediction)   |   (Accurate)
   |    \     /            |                      |     \     |    /
   |     \   /             |                      |      v    v   /
   |      v v              v                      v     (Obs) |  /
(Box B)  (-----------> [  Act  ]               (Box B)    \   | /
   \                      /                       \        v  vv
    \-----> < V > <------/                         \-----> < V > <--- (Act = pi(Obs))
```

In **action-based FDT**, the graph $G^F$ contains two separate algorithm nodes: $\textsc{fdt}(\underline{P}^F, \underline{G}^F, \textit{full})$ and $\textsc{fdt}(\underline{P}^F, \underline{G}^F, \textit{empty})$. Upon observing $\textit{full}$, Fiona intervenes *only* on $\textsc{fdt}(\underline{P}^F, \underline{G}^F, \textit{full})$. When evaluating $\mathtt{do}(\textsc{fdt}(\underline{P}^F, \underline{G}^F, \textit{full}) = \textit{onebox})$, there is a $1\%$ chance ($\textsc{Accurate} = \textit{inaccurate}$) that the predictor mispredicts, leaves Box B empty, and causes Fiona to observe $\textit{empty}$ instead. In that $1\%$ branch, Fiona's action is controlled by the *other* node, $\textsc{fdt}(\underline{P}^F, \underline{G}^F, \textit{empty})$. Because action-based FDT only intervenes on one observation node at a time, Yudkowsky and Soares have to introduce a free parameter $q \in [0, 1]$ representing Fiona's prior probability that $\textsc{fdt}(\underline{P}^F, \underline{G}^F, \textit{empty}) = \textit{twobox}$, yielding expected utilities of $\$990,000 + 0.01q \cdot \$1,000$ for $\textit{onebox}$ versus $\$10,010 + 0.99q \cdot \$1,000$ for $\textit{twobox}$.

Now let us solve the same problem using **P-FDT**. Here $\mathcal{X} = \{\textit{full}, \textit{empty}\}$ and $\mathcal{A} = \{\textit{onebox}, \textit{twobox}\}$. The policy space $\Pi = \mathcal{A}^{\mathcal{X}}$ consists of $2^2 = 4$ policies, which we write as $\pi_{a,b}$ where $\pi_{a,b}(\textit{full}) = a$ and $\pi_{a,b}(\textit{empty}) = b$, for $a,b \in \{\textit{1}, \textit{2}\}$ (denoting $\textit{onebox}$ and $\textit{twobox}$).

In $G^{PF}$, the predictor's prediction depends on how the policy $\pi$ responds to $\textit{full}$, namely $\pi(\textit{full})$:
* If $\pi(\textit{full}) = \textit{1}$, then with probability $0.99$ ($\textsc{Accurate}=\textit{accurate}$), Box B is $\textit{full}$ ($\textsc{Obs}=\textit{full}$) and the agent executes $\pi(\textit{full}) = \textit{1}$ (getting $\$1,000,000$); with probability $0.01$ ($\textsc{Accurate}=\textit{inaccurate}$), Box B is $\textit{empty}$ ($\textsc{Obs}=\textit{empty}$) and the agent executes $\pi(\textit{empty})$ (getting $\$0$ if $\pi(\textit{empty})=\textit{1}$, or $\$1,000$ if $\pi(\textit{empty})=\textit{2}$).
* If $\pi(\textit{full}) = \textit{2}$, then with probability $0.01$ ($\textsc{Accurate}=\textit{inaccurate}$), Box B is $\textit{full}$ ($\textsc{Obs}=\textit{full}$) and the agent executes $\pi(\textit{full}) = \textit{2}$ (getting $\$1,001,000$); with probability $0.99$ ($\textsc{Accurate}=\textit{accurate}$), Box B is $\textit{empty}$ ($\textsc{Obs}=\textit{empty}$) and the agent executes $\pi(\textit{empty})$.

Evaluating Equation (P-FDT.1) across all four policies in $\Pi$ yields:

$$\begin{aligned}
\mathcal{EU}_{\text{P-FDT}}(\pi_{1,1}) &= 0.99(\$1,000,000) + 0.01(\$0) = \$990,000 \\
\mathcal{EU}_{\text{P-FDT}}(\pi_{1,2}) &= 0.99(\$1,000,000) + 0.01(\$1,000) = \$990,010 \\
\mathcal{EU}_{\text{P-FDT}}(\pi_{2,1}) &= 0.01(\$1,001,000) + 0.99(\$0) = \$10,010 \\
\mathcal{EU}_{\text{P-FDT}}(\pi_{2,2}) &= 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.
\end{aligned}$$

The unique global maximizer is $\pi^* = \pi_{1,2}$: the policy that one-boxes when seeing a full box and two-boxes when seeing an empty box. In Stage 2 (Equation P-FDT.2), our agent—having actually observed $x = \textit{full}$—evaluates $\pi_{1,2}(\textit{full}) = \textit{onebox}$ and leaves the $\$1,000$ behind. (If the predictor had made the $1\%$ error and left Box B empty, the agent would have observed $x = \textit{empty}$ and executed $\pi_{1,2}(\textit{empty}) = \textit{twobox}$, taking the $\$1,000$.)

Notice that in P-FDT, the arbitrary epistemic parameter $q$ vanishes completely. Because the intervention $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$ sets the agent's entire response function across all observations simultaneously, the agent never needs to hold prior probabilistic beliefs about her own unreached counterfactual decisions.

*(An identical simplification occurs in **Parfit's Hitchhiker** and the **Mechanical Blackmail Problem**: in Mechanical Blackmail, P-FDT evaluates policies $\pi : \{\textit{blackmail}, \emptyset\} \to \{\textit{pay}, \textit{refuse}\}$ and selects the policy that refuses when blackmailed, thereby driving the probability of receiving the blackmail letter to $\approx 0$.)*

---

## 5. Why Policies Matter: Multi-Agent Dilemmas and Open Theoretical Questions

Why, then, do Yudkowsky and Soares state in Footnotes 7 and 16 that the distinction between iterating over actions and iterating over policies *"makes a difference in certain multi-agent dilemmas"*? The reference paper never provides an example of such a dilemma or explains why action-based FDT fails there. In this section, we diagnose the failure of action-based FDT in multi-agent settings, demonstrate how P-FDT resolves it, and address three foundational questions left open by the source text.

### 5.1 Where Action-Based FDT Breaks Down: Asymmetric Observations

Consider the **Psychological Twin Prisoner's Dilemma** (Dilemma 1 in Yudkowsky and Soares, 2017). Two computationally identical twins, each implementing the same decision algorithm with the same world-model $(P, G)$, are placed in separate rooms and must choose to either $\textit{cooperate}$ ($C$) or $\textit{defect}$ ($D$). Mutual cooperation yields $\$1,000,000$ each; mutual defection yields $\$1,000$ each; unilateral defection yields $\$1,001,000$ for the defector and $\$0$ for the cooperator.

In the baseline version of Dilemma 1, the two twins receive **identical observations** (or no observations at all, $x = \emptyset$). Consequently, both twins' physical actions $\textsc{Act}_1$ and $\textsc{Act}_2$ depend on the *exact same* variable $\textsc{fdt}(\underline{P}, \underline{G}, \emptyset)$. When Twin 1 intervenes on $\textsc{fdt}(\underline{P}, \underline{G}, \emptyset)$, Twin 2's action varies in lockstep, so action-based FDT prescribes $\textit{cooperate}$.

Now consider a slight, realistic modification of our own construction, which we call the **Asymmetric-Observation Twin Prisoner's Dilemma**:

> **Dilemma (Asymmetric-Observation Twin Prisoner's Dilemma).** Two computationally identical twins share the exact same world-model $(P, G)$ and payoff matrix as in the Psychological Twin Prisoner's Dilemma. However, before making their decisions, one twin is placed in a room painted red (observing $x = \textit{red}$) and the other twin is placed in a room painted blue (observing $x = \textit{blue}$). Which room each twin is placed in is determined by a fair coin flip ($50/50$). Both twins know this setup. Twin 1 opens her eyes and sees $\textit{red}$. Should she $\textit{cooperate}$ or $\textit{defect}$?

Let us trace what happens under **action-based FDT** (Equation 4 of Yudkowsky and Soares, 2017):

1. Twin 1 observes $x = \textit{red}$. According to Equation (4), she responds to her observation $\textit{red}$ by intervening on the node $\textsc{fdt}(\underline{P}, \underline{G}, \textit{red})$.
2. What governs the action of Twin 2? Because Twin 1 is in the red room, Twin 2 is necessarily in the blue room, observing $y = \textit{blue}$. Therefore, Twin 2's physical action $\textsc{Act}_{\text{blue}}$ is determined by the logical node $\textsc{fdt}(\underline{P}, \underline{G}, \textit{blue})$!
3. In action-based FDT's graphical model $G$, $\textsc{fdt}(\underline{P}, \underline{G}, \textit{red})$ and $\textsc{fdt}(\underline{P}, \underline{G}, \textit{blue})$ are **distinct, causally and subjunctively independent root nodes**—just as $\textsc{fdt}(\underline{P}^F, \underline{G}^F, \textit{full})$ and $\textsc{fdt}(\underline{P}^F, \underline{G}^F, \textit{empty})$ were distinct root nodes in Figure 5b of the reference paper!
4. When Twin 1 performs the intervention $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \textit{red}) = a)$, the node $\textsc{fdt}(\underline{P}, \underline{G}, \textit{blue})$ is completely unaffected, remaining fixed at whatever prior probability $q = P(\textsc{fdt}(\underline{P}, \underline{G}, \textit{blue}) = C)$ Twin 1 assigns to it.
5. Comparing her two hypotheticals, Twin 1 calculates:
   * For $a = C$: Expected utility is $q \cdot \$1,000,000 + (1-q) \cdot \$0$ (in the red room).
   * For $a = D$: Expected utility is $q \cdot \$1,001,000 + (1-q) \cdot \$1,000$ (in the red room).
6. For *every* value of $q \in [0, 1]$, $\textit{defect}$ strictly dominates $\textit{cooperate}$ by $\$1,000$! Twin 2 in the blue room reasons symmetrically by intervening on $\textsc{fdt}(\underline{P}, \underline{G}, \textit{blue})$ while holding $\textsc{fdt}(\underline{P}, \underline{G}, \textit{red})$ fixed. Thus, under action-based FDT, **both twins defect and walk away with $\$1,000$**, merely because their rooms were painted different colors!

```
  Action-Based FDT in Asymmetric Twin PD             P-FDT in Asymmetric Twin PD
  ======================================             ===========================
  [fdt(P,G,red)]       (fdt(P,G,blue))                      [pfdt(P,G)]
        |                     |                             /         \
        v                     v                            v           v
    (Act_red)            (Act_blue)               (Act_red = pi(r)) (Act_blue = pi(b))
        \                    /                             \           /
         \---> < V_agent > <-/                              \-> < V > <-/
  (Intervening on red leaves blue fixed!)         (Single intervention couples both!)
```

Now let us apply **P-FDT** to the Asymmetric-Observation Twin Prisoner's Dilemma:

1. Here $\mathcal{X} = \{\textit{red}, \textit{blue}\}$ and $\mathcal{A} = \{C, D\}$. There are four candidate policies $\pi_{a,b} \in \Pi$, where $\pi_{a,b}(\textit{red}) = a$ and $\pi_{a,b}(\textit{blue}) = b$.
2. Both twins' actions subjunctively depend on the **single shared policy node** $\textsc{pfdt}(\underline{P}, \underline{G})$: the twin in the red room executes $\textsc{Act}_{\text{red}} = \pi(\textit{red})$, and the twin in the blue room executes $\textsc{Act}_{\text{blue}} = \pi(\textit{blue})$.
3. Under the prior distribution $P$ (before conditioning on which room the agent happens to wake up in), the agent has probability $P(\textsc{Obs} = \textit{red}) = 0.5$ of being the twin in the red room and $P(\textsc{Obs} = \textit{blue}) = 0.5$ of being the twin in the blue room.
4. Evaluating Equation (P-FDT.3) for each of the four candidate policies $\pi \in \Pi$:

   $$\begin{aligned}
   \mathcal{EU}_{\text{P-FDT}}(\pi_{C,C}) &= 0.5(\$1,000,000) + 0.5(\$1,000,000) = \$1,000,000 \\
   \mathcal{EU}_{\text{P-FDT}}(\pi_{C,D}) &= 0.5(\$0) + 0.5(\$1,001,000) = \$500,500 \\
   \mathcal{EU}_{\text{P-FDT}}(\pi_{D,C}) &= 0.5(\$1,001,000) + 0.5(\$0) = \$500,500 \\
   \mathcal{EU}_{\text{P-FDT}}(\pi_{D,D}) &= 0.5(\$1,000) + 0.5(\$1,000) = \$1,000.
   \end{aligned}$$

5. The unique optimal policy is $\pi^* = \pi_{C,C}$.
6. In Stage 2, Twin 1 applies $\pi_{C,C}$ to her observation $\textit{red}$ and outputs $\pi_{C,C}(\textit{red}) = C$. Twin 2 applies $\pi_{C,C}$ to her observation $\textit{blue}$ and outputs $\pi_{C,C}(\textit{blue}) = C$. **Both twins cooperate and each receives $\$1,000,000$.**

Even more starkly, consider a **Complementarity (Division-of-Labor) Game** where two identical P-FDT agents in separate rooms (one observing $\textit{red}$, one observing $\textit{blue}$) each win $\$1,000,000$ if and only if *one presses Button 1 and the other presses Button 2* (and $\$0$ if they press the same button). Under P-FDT, the constant policies $\pi_{1,1}$ and $\pi_{2,2}$ yield $\$0$, whereas the asymmetric policies $\pi_{1,2}$ (press 1 if red, 2 if blue) and $\pi_{2,1}$ (press 2 if red, 1 if blue) yield $\$1,000,000$, enabling identical agents to execute coordinated asymmetric roles based on local observations.

### 5.2 Open Questions in the Source Text and Operational Resolutions

Because Yudkowsky and Soares (2017) mention P-FDT only in Footnotes 7 and 16, three crucial operational details are left unspecified. Anyone wishing to apply P-FDT to unfamiliar cases must adopt explicit conventions on these three points:

1. **Indexical Priors and Updatelessness in Multi-Agent Dilemmas.**
   Notice that in the Asymmetric-Observation Twin Prisoner's Dilemma above, if Twin 1's world-model $P$ assigned probability $1$ to $\textsc{Obs} = \textit{red}$ (i.e., if $P$ were already conditioned on her being in the red room and caring solely about the red room's occupant), then $\mathcal{EU}(\pi_{D,C})$ would be $1.0 \times \$1,001,000 = \$1,001,000 > \mathcal{EU}(\pi_{C,C})$, and P-FDT would prescribe $\pi_{D,C}$ (telling the red-room twin to defect and the blue-room twin to cooperate for her benefit!). Why doesn't this happen? Because in an updateless framework like P-FDT, $P$ must represent the agent's **prior epistemic state before indexical localization** (a "veil of ignorance" distribution over which observation stream $x \in \mathcal{X}$ the agent receives). When two agents share the same prior $P$, each evaluates $\pi$ under the pre-observation distribution over indexical positions. *(We note this explicitly as an operational assumption required to make Footnotes 7 and 16 work in asymmetric multi-agent games.)*

2. **The Domain of $\pi$: "Observations" (Footnote 7) vs. "Inputs" (Footnote 16).**
   There is a subtle terminological discrepancy between Footnote 7, which defines policies as *"mappings from observations to actions"*, and Footnote 16, which says that a policy *"maps inputs to actions, to which the agent then applies her inputs in order to select an action."* What if the agent is uncertain not about her sensory observation $x$, but about her own local model or utility function—as in Yudkowsky and Soares's formalization of the **Smoking Lesion Problem** (Section 6), where Fiona doesn't know whether she is running model $P_S^F$ (loving smoking, $\mathcal{U}_S$) or $P_R^F$ (hating smoking, $\mathcal{U}_R$)? Or what if two P-FDT agents have slightly different local belief states $(P_1, G)$ and $(P_2, G)$?

   Our operational resolution is to treat Footnote 7 as a special case of Footnote 16: in full generality, let $\mathcal{I}$ be the space of local *inputs* available to the decision procedure (where an input $i \in \mathcal{I}$ may be a sensory observation $x$, or a tuple $i = (\underline{P}_i, \underline{G}_i, \underline{x}_i)$ encoding local parameterization and observation). A generalized policy is a mapping $\pi : \mathcal{I} \to \mathcal{A}$, and the intervention node $\textsc{pfdt}(-)$ represents the universal P-FDT decision function itself. When the model $(P, G)$ is fixed across all relevant instances, $\mathcal{I}$ reduces to the observation space $\mathcal{X}$.

3. **Canonical Tie-Breaking and Computational Complexity.**
   In the Division-of-Labor game mentioned above, both $\pi_{1,2}$ and $\pi_{2,1}$ achieve the maximum expected utility of $\$1,000,000$. If the $\operatorname*{argmax}_{\pi \in \Pi}$ operator in Equation (P-FDT.1) returns a set of tied policies $\{\pi_{1,2}, \pi_{2,1}\}$ without a deterministic tie-breaking rule, Twin 1 might pick $\pi_{1,2}$ (playing 1 on red) while Twin 2 picks $\pi_{2,1}$ (playing 1 on blue), resulting in catastrophic miscoordination! Therefore, to apply P-FDT in symmetric coordination games, we must assume that $\operatorname*{argmax}_{\pi \in \Pi}$ is equipped with a **fixed, canonical lexical ordering** $<_{\Pi}$ over $\Pi$ (shared by all instances of the P-FDT algorithm) and always selects the lexically first maximizer $\pi^*$. Furthermore, because $|\Pi| = |\mathcal{A}|^{|\mathcal{X}|}$ grows exponentially in $|\mathcal{X}|$, an exact implementation of P-FDT is computationally tractable only over a coarse-grained or decision-relevant partition of observations $\mathcal{X}$; bounded agents must approximate $\Pi$ by restricting optimization to the subset of observations that have positive probability under $P$ in the dilemma at hand.

---

## 6. How to Apply P-FDT to Unfamiliar Decision Problems: A Step-by-Step Procedure

To consolidate our mathematical account into a practical tool, we can summarize the operational procedure for deciding any unfamiliar single- or multi-agent problem under **P-FDT** in five explicit steps:

1. **Specify the Spaces and Prior Model $(P, G)$:** Identify the finite action set $\mathcal{A}$, the set of decision-relevant observations/inputs $\mathcal{X}$ reachable in the dilemma, the utility variable $\textsc{V} = \mathcal{U}(\textsc{Outcome})$, and the pre-observation probability distribution $P$ (including indexical priors over which observation $x \in \mathcal{X}$ you receive).
2. **Construct the P-FDT Dependency Graph $G$:** Place a single logical root node $\textsc{pfdt}(\underline{P}, \underline{G})$ in $G$. Draw directed edges from $\textsc{pfdt}(\underline{P}, \underline{G})$ to:
   * Your physical action node $\textsc{Act}$, defined by $\textsc{Act}(\pi, \textsc{Obs}) = \pi(\textsc{Obs})$;
   * Any predictor or environmental mechanism that models your decision algorithm (specifying which values $\pi(x')$ the predictor inspects);
   * The action node $\textsc{Act}_k(\pi, \textsc{Obs}_k) = \pi(\textsc{Obs}_k)$ of any other agent $k$ who computes the same P-FDT decision procedure.
3. **Enumerate the Policy Space $\Pi = \mathcal{A}^{\mathcal{X}}$:** List all $|\mathcal{A}|^{|\mathcal{X}|}$ mappings $\pi : \mathcal{X} \to \mathcal{A}$ under a fixed canonical ordering $<_{\Pi}$.
4. **Evaluate Global Expected Utility via Intervention:** For each candidate policy $\pi \in \Pi$, perform Pearl's graph surgery $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$ and compute:
   $$\mathcal{EU}_{\text{P-FDT}}(\pi) = \sum_{x' \in \mathcal{X}} P\left(\textsc{Obs} = x' \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right) \cdot \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs} = x',\, \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right).$$
   Select the lexically first policy $\pi^* \in \Pi$ that maximizes $\mathcal{EU}_{\text{P-FDT}}(\pi)$.
5. **Apply Your Actual Observation $x$:** Observe your actual local input $x \in \mathcal{X}$ and execute the physical action $a^* = \pi^*(x)$.

---

## 7. Conclusion

**Policy functional decision theory (P-FDT)** represents the natural mathematical completion of the philosophical insight behind functional decision theory. If rational agency consists in treating one's decision as the output of a fixed mathematical function and asking which output of that function yields the best world, then the object of intervention should be the function's *entire input-output mapping*—the policy $\pi : \mathcal{X} \to \mathcal{A}$—rather than its isolated evaluation at a single observation point.

By intervening on the policy node $\textsc{pfdt}(\underline{P}, \underline{G})$ to select a policy $\pi^*$ and only then applying $\pi^*$ to the actual observation $x$, P-FDT preserves every advantage of action-based FDT over CDT and EDT—one-boxing in Newcomb's problem and Transparent Newcomb, smoking in the smoking lesion problem, paying the driver in Parfit's hitchhiker problem, and resisting extortion in the XOR and mechanical blackmail problems—while eliminating arbitrary priors over unreached observation branches and enabling seamless coordination across asymmetric-information multi-agent dilemmas.

---

## References

* Dai, W. (2009). Towards a new decision theory. *Less Wrong*.
* Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Gibbard, A., & Harper, W. L. (1978). Counterfactuals and two kinds of expected utility. In *Foundations and Applications of Decision Theory* (Vol. 1). D. Reidel.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Pearl, J. (1996). Causation, action, and counterfactuals. In *6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-'96)* (pp. 51–73).
* Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Yudkowsky, E. (2010). *Timeless Decision Theory*. The Singularity Institute.
* Yudkowsky, E., & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. Machine Intelligence Research Institute, arXiv:1710.05060v2.
````

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Project Scope**

I'm now zeroing in on the project's parameters. The aim is clear: a technical piece, 2400-3000 words, that elucidates Policy Functional Decision Theory from a researcher's perspective, illustrating its application. I'm focusing on crafting a coherent structure for explaining P-FDT in a way that resonates with a technically-savvy audience. I'm starting to build a skeleton outline.


**Refining the Target Audience**

I'm now honing in on the target audience. My focus has narrowed to mathematically literate readers intrigued by formal procedures and the underlying philosophical implications of decision theory, especially in the context of P-FDT. I need to clearly define P-FDT and differentiate it from other decision theories. I'm carefully reading the relevant footnotes from the source paper.


**Analyzing Key Theory Aspects**

I am now focusing on critical aspects of the P-FDT theory itself. My goal is to extract the core ideas, mathematical definitions, and examples needed for a coherent explanation. I'm exploring how P-FDT evaluates actions and policies, and the way the theory treats dependencies and counterfactuals. Also, I'm noting uncertainties in the source material and working to develop operational interpretations to address them.


**Clarifying Source Contributions**

My immediate task is to disentangle the source's claims from my potential interpretations. I plan to construct a mathematically-driven essay, not a case study, focusing on examples like Transparent Newcomb, Mechanical Blackmail, and critically, a multi-agent dilemma where P-FDT and action-level FDT are at odds. I'm focusing on providing exact quotations from the source. The target word count is approximately 2,500–2,900 words total.


**Examining Action-FDT Equations**

I'm now diving into the core equations defining Causal Decision Theory and Action-FDT. I've noted that standard FDT uses a separate node to handle observations, unlike CDT, which conditions on observations. This highlights a key difference in how they approach intervention and observation. Now, I will look at the effect of observation on the P-FDT.


**Investigating Multi-Agent Interactions**

I'm currently grappling with multi-agent interactions within the P-FDT framework. The key issue is how Action-FDT handles scenarios where decisions are jointly determined across different observations. For instance, in Transparent Newcomb, an inaccurate predictor necessitates a nuanced understanding of how the decision algorithm responds to multiple information sets. This highlights critical differences in how different decision theories respond to multi-agent interactive settings.


**Formalizing Policy Iteration**

I'm now zeroing in on the mathematical formalization of P-FDT and the crucial role of policies. I'm focusing on clarifying how agents iterate over policies, not just actions. I'm noting the definition of a policy as a mapping from observations to actions, and how this relates to multi-agent dilemmas, and I'm developing equations for policy inputs and observations. Also, I'm working to expand the equations based on information from the source.


**Delineating Policy Implementation**

I'm now clarifying the two interpretations of the P-FDT function. Specifically, I'm differentiating the narrow policy $\pi \in \Pi \subseteq \mathcal{A}^{\mathcal{X}}$ from the broader input of $(P, G, x)$. I'm dissecting the core function, $\mathrm{PFDT}_{\text{pol}}$, defining how the policy $\pi^*$ is chosen from world-models $(P, G)$. I'm also ensuring the function $\mathrm{PFDT}(P, G, x) \coloneqq \pi^*(x)$ maps a specific observation to an action, referencing Footnote 16.


**Interpreting Agent Inputs**

I'm now clarifying the nature of "inputs" within the P-FDT framework. The key ambiguity is whether the input to $\mathrm{FDT}(-)$ is $(P, G, x)$ or just $x$, as described in Footnote 7 vs Footnote 16. I am working to reconcile these two interpretations, and exploring how these inputs are related to policy selection versus action choice.


**Defining Input Interpretation**

I'm now carefully examining the input interpretation within P-FDT. I'm focusing on clarifying whether the input to the FDT function is a policy or an action, as described in the source. I'm specifically dissecting the source where it leaves the action or policy ambiguous. I'm noting that a policy maps inputs like observations and model parameters to actions. I will highlight all the interpretations.


**Clarifying Policy Domains**

I'm now zeroing in on defining the precise domain of a policy $\pi$ within the P-FDT framework, reconciling the source's ambiguity. I am focusing on two cases. In the first, I have a fixed model where the domain is the observation space. In the second, I explore dependencies, where the policy domain is more complex. I will clarify the two interpretations of "inputs" to match Footnotes 7 and 16.



**Clarifying Divergence in Dilemmas**

I'm now focusing on a critical distinction. The key is to understand when P-FDT diverges from action-based FDT, particularly in multi-agent dilemmas. My goal is to determine why the policy iteration makes a difference in specific multi-agent scenarios, but not in simpler cases like Transparent Newcomb or Mechanical Blackmail. I'm exploring the nuances, especially where individual observations influence the payoff.


**Analyzing Multi-Agent Dilemmas**

I'm now focusing on multi-agent dilemmas, particularly why policy iteration becomes crucial in scenarios like asymmetric twin prisoner dilemmas, unlike Transparent Newcomb. My analysis shows that in simpler cases, action-based FDT still works fine. I'm focusing on the effect of treating an empty box, on average, the same way, in these scenarios. In the next phase, I plan to explore how the two agents’ decisions and observations intertwine.


**Tracing Action-FDT Behavior**

I'm currently tracing the behavior of Action-FDT within an asymmetric twin prisoner's dilemma. I've noted that, since twins are in separate rooms, their actions are governed by separate logical nodes, $\textsc{fdt}(\underline{P}, \underline{G}, L)$ and $\textsc{fdt}(\underline{P}, \underline{G}, R)$, respectively. The key insight is that interventions on one twin's decision do not influence the other twin's. This highlights a fundamental difference from policy-based approaches.


**Tracing P-FDT Coordination**

I'm now tracing the P-FDT's behavior in the same dilemma. I've noted that, in contrast to Action-FDT, the twins are implementing P-FDT. They intervene on a shared world-model and a policy. I'm focusing on the policy, $\pi^* : \{L, R\} \to \{\textit{cooperate}, \textit{defect}\}$, which calculates the optimal behavior under intervention. Both twins apply this same policy, coordinating despite different observations. I'm noting P-FDT's capacity for coordination, contrasting with Action-FDT's lack thereof.


**Examining P-FDT Coordination**

Now I'm diving deeper into coordination under P-FDT, using the asymmetric twin dilemma. The key is that both twins' actions depend on a single P-FDT node, $\textsc{pfdt}(\underline{P}, \underline{G})$, through a policy $\pi$. This contrasts sharply with Action-FDT. I'm focusing on how the agent evaluates policies and why $\pi_{CC}$ (both cooperate) is uniquely optimal, achieving a higher utility than other policies. Now I am exploring another subtle coordination case.


**Eliminating Epistemic Priors**

I'm now focusing on a single-agent problem. I'm noting how P-FDT eliminates arbitrary priors over one's own decisions in the other observation branch, using the example of Transparent Newcomb. My focus is on how the error rate of the prediction influences behavior on different observations and removes any need to predict the agent's behavior. My goal is to capture the behavior of the system, and compare it with FDT.

\n\n**Addressing Tie-Breaking Issues**

My focus is now shifting to the issue of tie-breaking in scenarios where P-FDT might not have a clear preference. For instance, in an anti-coordination game, what if the policies tie? My goal is to determine how the agent would behave in Battle of the Sexes. This is relevant for computational complexity of $\mathcal{A}^{\mathcal{X}}$. I will see how to address tie-breaking in these kinds of scenarios.


**Clarifying Tie-Breaking Strategies**

I'm now clarifying tie-breaking strategies within P-FDT. I'm focusing on scenarios where policies tie and how that is resolved. For instance, in an anti-coordination game, I'm examining canonical tie-breaking or a lexical ordering over policies, ensuring both twins select the *same* optimal policy. I'm exploring the nuances, especially how it clarifies calculations such as average expected utility.


**Formalizing Decision Frameworks**

I'm now detailing the formal aspects of EDT, CDT, and Action-FDT. I'm focusing on their respective equations, assumptions, and how they evaluate actions. I am dissecting these systems to create a framework that will allow a rigorous comparison with P-FDT, especially with regards to counterfactuals and decision dependencies. My goal is to use this section to elucidate the distinctions between them.


**Formalizing Decision Models**

I'm now detailing EDT, CDT, and Action-FDT within my technical framework. I'm focusing on key notation: outcome space, action space, and observation space. I'm writing the equations for EDT, CDT, and action-based FDT, along with an explanation of subjunctive dependence and the logical counterpossibles. I'm highlighting the shift in Action-FDT from conditioning on observations to intervention on specific nodes. I will now clarify the crucial aspects of P-FDT.


**Formalizing P-FDT Equations**

I'm now formalizing P-FDT's decision process, showing how it selects policies and executes them. I've written the equation for the policy selection via global intervention, $\pi^*$, which maximizes the expected value, and the action execution equation, $\mathrm{PFDT}(P, G, x)$, applying the chosen policy to the observation. I'm expanding the law of total expectation over observations and relating the graphical structure to the equation.


**Comparing Policy Implementations**

I'm now comparing policy implementations in single-agent dilemmas, like Transparent Newcomb. My analysis shows that P-FDT’s policy iteration simplifies calculations compared to Action-FDT. In Transparent Newcomb, the explicit expected utility calculations for all four policies highlight the theory's approach. My focus is now on the formal structure of a policy's action.


**Elaborating Policy Advantages**

I am now clarifying P-FDT's advantages by examining specific examples. In Transparent Newcomb, I've noted how policy iteration simplifies utility calculations compared to action-based FDT. The utility calculations highlight the difference between P-FDT's method and Action-FDT. I am focusing on how we don't have to define prior probabilities about other agent's behavior to obtain an optimal policy.


**Investigating Twin Dilemma**

I am now constructing a specific example to highlight P-FDT's advantages, using the asymmetric-information twin prisoner's dilemma. My goal is to use this specific scenario to resolve ambiguity regarding the roles of action and policy selection. I will construct an asymmetric-information scenario. I will then show how standard FDT fails, as it intervenes on separate logical nodes for each twin.


**Resolving Twin Dilemma Discrepancies**

I'm currently formalizing the asymmetric twin prisoner's dilemma to directly contrast Action-FDT and P-FDT. I'm focusing on the different interventions on the model. Action-FDT, given separate logical nodes, results in defection. In contrast, P-FDT's centralized policy selection, which uses the common knowledge about the situation, coordinates cooperation. I'm noting the clear utility advantage of the coordinated cooperation policy, resolving previous ambiguity.


**Addressing Tie-Breaking Constraints**

Now, I'm focusing on tie-breaking rules and computational limits, especially in coordination games. If policies tie, P-FDT requires a deterministic canonical tie-breaking rule to ensure agents coordinate. I am now working on these details for computational intractability given the need to iterate over $|\mathcal{A}|^{|\mathcal{X}|}$ policies, where $|\mathcal{A}|$ is the number of actions.


**Clarifying Notational Conventions**

I'm now establishing a consistent notation to aid in comparing decision theories. I'll use **P-FDT**, **action-based FDT**, **CDT**, **EDT**, **UDT**, and **TDT** to distinguish them clearly. I'm double-checking all direct quotations from the source to ensure accuracy, including Footnote 7 and Footnote 16. The goal is to avoid any confusion by using consistent notation.


**Refining Technical Definitions**

I'm now refining the mathematical definitions, aiming for clarity and rigor. Specifically, I'm working to distinguish the source's claims from my added operational interpretations and extensions. I'm focusing on defining core concepts, like subjunctive dependence, using precise terminology to ensure each section clearly addresses all relevant questions. I will track the total word count.


**Formalizing Algorithm Application**

I am now focusing on providing a concrete, actionable guide to applying P-FDT in unfamiliar decision problems. I am defining a 5-step operational algorithm for P-FDT, mirroring the formal notations and definitions I have been using. I'm focusing on ensuring this procedural guide is accessible and clear to a mathematically-literate audience. I'm also tracking my progress, and my current word count is approximately 2500 words.


```
