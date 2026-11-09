# 021_fdt_eq4_google_gemini-4-argon_rhigh_phigh / 00007

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/80712f80-57ad-4689-b031-4f8817e89833/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/80712f80-57ad-4689-b031-4f8817e89833/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Action Functional Decision Theory (A-FDT): Formal Mechanics, Subjunctive Counterfactuals, and Operational Application

## 1. Introduction: The Dilemma of Instrumental Rationality

For nearly half a century, normative decision theory has been divided between two competing accounts of instrumental rationality: **Evidential Decision Theory (EDT)** and **Causal Decision Theory (CDT)**. Both theories endorse the maximization of expected utility, yet they diverge sharply on how an agent should evaluate the hypothetical consequences of an action. EDT instructs an agent to choose the action that would be the best *news* to learn she had taken, evaluating options via standard Bayesian conditionalization. CDT instructs an agent to choose the action that *causes* the best outcome, evaluating options by holding fixed the causal past and propagating only the downstream physical effects of the act.

As Allan Gibbard and William Harper (1978) demonstrated, each theory triumphs where the other falters. In dilemmas involving predictors or symmetric co-reasoners—such as Newcomb's problem (Nozick 1969) or the Psychological Twin Prisoner's Dilemma (Lewis 1979)—EDT agents walk away rich while CDT agents defect against their twins and leave Newcomb's problem with a paltry $\$1,000$. Conversely, in dilemmas where an action is merely a statistical symptom of a prior physical state—such as Skyrms's (1980) smoking lesion problem or Soares and Fallenstein's (2015) XOR blackmail problem—EDT agents wastefully "manage the news" (Lewis 1981) and submit to extortion, whereas CDT agents recognize that their actions cannot alter the past and act optimally. Moreover, in sequential prediction dilemmas such as Derek Parfit's (1986) hitchhiker problem and Gary Drescher's (2006) transparent Newcomb problem, *both* EDT and CDT fail to secure the high-utility outcome, leaving rational agents to die in Parfit's desert unless they have paid in advance for a binding precommitment device.

In *"Functional Decision Theory: A New Theory of Instrumental Rationality"*, Eliezer Yudkowsky and Nate Soares (2017) propose a third paradigm designed to supersede both EDT and CDT without ad-hoc switching or costly precommitments. The core thesis of their framework is that a decision-maker should treat her choice not as an isolated physical act token, nor as an evidentiary update about her character, but as the output of a *fixed mathematical decision function*. An agent implementing this principle asks: *"Which output of this very function would yield the best outcome?"*

While Yudkowsky and Soares note that their overarching framework can be formulated to optimize over entire policies (Footnotes 7 and 16), the primary formalization they develop and apply throughout their paper—given in **Equation (4), Section 5**—operates directly on the *action* output of the decision procedure for a given input context. In this essay, we examine **Action Functional Decision Theory (A-FDT)** as defined by Equation (4). We unpack its mathematical machinery, trace how it evaluates dependencies and counterpossibilities across classic dilemmas, clarify subtle technical features of its "updateless" response to observations, and develop an explicit operational protocol for applying **A-FDT** to unfamiliar decision problems where the source paper leaves implementation questions open.

---

## 2. The Formal Architecture of A-FDT

### 2.1 Expected Utility and Epistemic Perspectives

Following Gibbard and Harper (1978) and James Joyce (1999), Yudkowsky and Soares situate EDT, CDT, and **A-FDT** within a common expected utility skeleton. An agent faces a finite set of available actions $\mathcal{A}$, a countable set of possible observation histories $\mathcal{X}$, and a countable set of outcomes $\mathcal{O} = \{o_1, o_2, \dots\}$ valued by a bounded utility function $\mathcal{U} : \mathcal{O} \to \mathbb{R}$. Upon receiving an observation $\obs \in \mathcal{X}$, an expected utility maximizer selects an action $\act \in \mathcal{A}$ maximizing Equation (1) of the paper:

$$\mathcal{EU}(\act) \coloneqq \sum_{j=1}^N P(\act \hookrightarrow o_j ;\, \obs) \cdot \mathcal{U}(o_j), \tag{1}$$

where $P(\act \hookrightarrow o_j ;\, \obs)$ denotes the probability assigned to outcome $o_j$ in the decision-theoretic *hypothetical* where action $\act$ is taken after observing $\obs$.

By Joyce's (1999) representation theorem, any coherent conditional preference ranking can be represented as maximizing Equation (1) relative to some constraint on the conditional likelihood connective "$\hookrightarrow$". As Joyce writes, "decision theories should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated." Computationally, the agent maintains a world-model $\model$ and, for each candidate action $\act \in \mathcal{A}$, applies a surgery or transformation to $\model$ to construct a hypothetical object $\model^{\act \hookrightarrow}$ ("the agent's hypothetical for $\act$"). Defining the random variable $\VV \coloneqq \mathcal{U}(\Outcome)$ and writing $\mathbb{E}$ for expectation with respect to the agent's probability distribution $P$, the three theories are distinguished by the data required in $\model$ and the operator used to construct $\model^{\act \hookrightarrow}$:

1. **Evidential Decision Theory (EDT)**: The world-model $\model$ is simply a probability distribution $P$ over the relevant random variables $(\Obs, \Act, \Outcome, \VV, \dots)$. The hypothetical for $\act$ is formed by standard Bayesian conditioning on both the observation $\Obs = \obs$ and the physical action $\Act = \act$ (Equation 2):
   $$\mathrm{EDT}(P, \obs) \coloneqq \operatorname*{argmax}_{\act \in \mathcal{A}} \mathbb{E}\left(\VV \;\middle|\; \Obs = \obs, \Act = \act\right). \tag{2}$$

2. **Causal Decision Theory (CDT)**: Following Judea Pearl's (1996, 2000) graphical formalism, the world-model $\model = (P, G)$ augments $P$ with a directed acyclic causal graph $G$. To evaluate action $\act$ upon observing $\obs$, the agent conditions on $\Obs = \obs$ and applies Pearl's $\mathtt{do}$-operator to the physical action variable $\Act$ (Equation 3):
   $$\mathrm{CDT}(P, G, \obs) \coloneqq \operatorname*{argmax}_{\act \in \mathcal{A}} \mathbb{E}\left(\VV \;\middle|\; \mathtt{do}(\Act = \act), \Obs = \obs\right). \tag{3}$$
   Graphically, $\mathtt{do}(\Act = \act)$ severs all incoming arrows into $\Act$ in $G$, fixes $\Act = \act$, and propagates this change strictly forward along causal arrows to variables downstream of $\Act$, leaving all causally upstream or parallel variables untouched.

### 2.2 Equation (4): The Formal Definition of A-FDT

Whereas CDT intervenes on the physical token $\Act$ ("how my body moves right now"), **A-FDT** intervenes on a *logical* variable representing the mathematical output of the agent's decision algorithm itself.

To formalize this in **A-FDT**, the probability distribution $P$ is expanded to include variables representing the outputs of mathematical functions and algorithms—despite those outputs being logically determinate. Just as an agent under bounded computational resources may maintain a random variable in $P$ for the sum $6288 + 1048$ or the truth value of the Twin Prime Conjecture, an **A-FDT** agent with world-model $(P, G)$ and observation $\obs$ includes in $P$ a random variable $\textsc{fdt}(\underline{P}, \underline{G}, \underline{\obs})$ representing the action output of the **A-FDT** algorithm when evaluated on inputs $(P, G, \obs)$.

Here, underlines denote *dequoting* (syntactic substitution of values into variable names): if $x \coloneqq 3$, then $\textsc{Z}\underline{x}$ names the variable $\textsc{Z}3$. Accordingly, $\textsc{fdt}(\underline{P}, \underline{G}, \underline{\obs})$ is a specific node in $G$ whose identifier encodes the description of $P$, $G$, and $\obs$. As Yudkowsky and Soares note, Kleene's (1938) second recursion theorem guarantees via "quining" that an algorithm and its world-model $(P, G)$ can contain an exact syntactic representation of their own specification without vicious circularity.

Ideally, evaluating counterfactual variations in a mathematical function would employ a logical conditioning operator $\mathtt{true}(\phi)$, yielding:

$$\mathrm{FDT}^*(P, \obs) = \operatorname*{argmax}_{\act \in \mathcal{A}} \mathbb{E}\left(\VV \;\middle|\; \mathtt{true}(\textsc{fdt}(\underline{P}, \underline{\obs}) = \act)\right).$$

However, because $\textsc{fdt}(\underline{P}, \underline{\obs})$ has a single true mathematical output, at least $|\mathcal{A}| - 1$ of the antecedents $\textsc{fdt}(\underline{P}, \underline{\obs}) = \act$ are logically false (*counterpossibles* in the sense of Cohen 1990), and no settled formal calculus for $\mathtt{true}(\phi)$ currently exists. **A-FDT** circumvents this obstacle by requiring that the dependency structure of logical, mathematical, computational, and causal facts be encoded directly into the augmented graph $G$. With $G$ supplied as an input, **A-FDT** re-uses Pearl's $\mathtt{do}$-operator to perform graph surgery on the logical node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{\obs})$. This yields **Equation (4), Section 5** of the paper—the primary formal definition of **A-FDT**:

$$\mathrm{FDT}(P, G, \obs) \coloneqq \operatorname*{argmax}_{\act \in \mathcal{A}} \mathbb{E}\left(\VV \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{\obs}) = \act\right)\right). \tag{4}$$

*(Throughout this essay, we refer to the theory and decision rule defined by Equation (4) as **A-FDT**, preserving the source paper's notation $\mathrm{FDT}$ and $\textsc{fdt}$ inside direct equations and quotations for fidelity.)*

### 2.3 Two Structural Departures from CDT

Comparing Equation (3) for CDT with Equation (4) for **A-FDT** reveals two profound mathematical differences:

1. **Locus of Intervention (Type vs. Token)**: CDT intervenes on the physical node $\Act$. **A-FDT** intervenes on the functional node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{\obs})$. In Charles Sanders Peirce's (1934) terminology, CDT intervenes on the physical action *token*, whereas **A-FDT** intervenes on the computational/mathematical *type*. Any physical system in the universe whose behavior is modeled in $G$ as depending on the output of $\mathrm{FDT}(P, G, \obs)$—including the agent's own body ($\Act$), an identical twin's body, or a predictor's simulation of the agent—lies downstream of $\textsc{fdt}(\underline{P}, \underline{G}, \underline{\obs})$ in $G$ and therefore covaries with $\act$ under the $\mathtt{do}$-intervention.
2. **Updateless Response to Observations**: Look closely at the conditioning bar in Equation (4). Unlike EDT in Equation (2) and CDT in Equation (3), **A-FDT** *does not condition the probability distribution $P$ on $\Obs = \obs$*. Instead, when the agent receives observation $\obs$, she incorporates $\obs$ solely by changing *which node she intervenes upon*—switching the target of $\mathtt{do}(\cdot)$ to the variable $\textsc{fdt}(\underline{P}, \underline{G}, \underline{\obs})$. Because $P$ is not updated by Bayesian conditioning on $\Obs = \obs$, the **A-FDT** agent evaluates expectations across her *prior* model $P$, allowing her hypotheticals to reflect how varying the output of $\textsc{fdt}(\underline{P}, \underline{G}, \underline{\obs})$ would have altered the probability of observing $\obs$ in the first place. (As noted in the paper's draft notes, this "updateless" mechanism derives from Wei Dai's [2009] **Updateless Decision Theory [UDT]** and avoids the "double update" pathology of Eliezer Yudkowsky's [2010] **Timeless Decision Theory [TDT]**, which both conditioned on $\Obs = \obs$ and intervened on the logical node.)

When all correlations between $\Act$ and other variables in $(P, G)$ are strictly downstream of $\Act$ (with $\Act$ depending on $\textsc{fdt}(\underline{P}, \underline{G}, \underline{\obs})$), Equations (2), (3), and (4) coincide:

$$\mathbb{E}[\VV \mid \act] = \mathbb{E}[\VV \mid \mathtt{do}(\act)] = \mathbb{E}[\VV \mid \mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}) = \act)].$$

The theories diverge precisely when non-causal correlations exist between $\Act$ and the environment.

---

## 3. Subjunctive Dependence and Worked Applications of A-FDT

### 3.1 Subjunctive Dependence

The philosophical backbone of **A-FDT** is *subjunctive dependence*: "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function" (Section 3).

Consider two intact pocket calculators on opposite sides of the globe both computing $6288 + 1048$. Their physical displays are causally independent, yet their outputs are logically constrained to agree insofar as neither calculator malfunctions. Causal dependence is a special case of subjunctive dependence (a scribe copying a calculator's output subjunctively depends on the calculation via a causal chain), whereas mere statistical coincidence (two calculators happening to be painted pink) entails no subjunctive dependence. Summarizing the structural parallel: *"Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."*

Let us see how Equation (4) operationalizes this principle across three diagnostic decision problems.

### 3.2 Newcomb's Problem and Decision-Theoretic Dominance

In Newcomb's problem, a transparent Box A contains $\$1,000$, and an opaque Box B contains either $\$1,000,000$ ($\mathit{full}$) or $\$0$ ($\mathit{empty}$). Yesterday, a predictor with $99\%$ accuracy ($\textsc{Accurate} = \mathit{accurate}$ with probability $0.99$, $\mathit{inaccurate}$ with probability $0.01$) predicted whether the agent would leave Box A behind ($\mathit{onebox}$) or take both boxes ($\mathit{twobox}$), filling Box B if and only if she predicted $\mathit{onebox}$.

In CDT's graph $G^C$, a background node $\textsc{Predisposition}$ is a common cause of both $\Act$ and $\textsc{Prediction}$ ($\textsc{Predisposition} \to \Act$ and $\textsc{Predisposition} \to \textsc{Prediction} \to \textsc{Box B} \to \VV$, along with $\Act \to \VV$). When the CDT agent evaluates $\mathtt{do}(\Act = \act)$, the incoming arrow $\textsc{Predisposition} \to \Act$ is severed. $\textsc{Box B}$ is unaffected by $\mathtt{do}(\Act = \act)$, retaining some fixed probability $p$ of being full. Comparing $p(\$1,000,000) + (1-p)(\$0)$ against $p(\$1,001,000) + (1-p)(\$1,000)$, CDT concludes that $\mathit{twobox}$ strictly dominates $\mathit{onebox}$ by $\$1,000$.

Now consider Fiona, an **A-FDT** agent with model $(P^F, G^F)$. Instead of an opaque physical $\textsc{Predisposition}$, the root node of $G^F$ is the logical variable $\textsc{fdt}(\underline{P^F}, \underline{G^F})$ representing the output of her decision algorithm. Because both Fiona's physical body and the predictor's predictive model compute $\mathrm{FDT}(P^F, G^F)$, the graph $G^F$ contains two directed paths out of $\textsc{fdt}(\underline{P^F}, \underline{G^F})$:

$$\textsc{fdt}(\underline{P^F}, \underline{G^F}) \to \Act \to \VV, \qquad \textsc{fdt}(\underline{P^F}, \underline{G^F}) \to \textsc{Prediction} \to \textsc{Box B} \to \VV,$$

where $\textsc{Prediction}$ also receives an incoming arrow from $\textsc{Accurate}$ ($\mathbb{P}(\mathit{accurate}) = 0.99$). Specifically:
- $\Act(z) = z$ for $z \in \{\mathit{onebox}, \mathit{twobox}\}$.
- $\textsc{Prediction}(\mathit{onebox}, \mathit{accurate}) = \mathit{1}$, $\textsc{Prediction}(\mathit{twobox}, \mathit{accurate}) = \mathit{2}$, and vice versa when $\mathit{inaccurate}$.
- $\textsc{Box B}(\mathit{1}) = \mathit{full}$ and $\textsc{Box B}(\mathit{2}) = \mathit{empty}$.

Applying Equation (4), Fiona evaluates two interventions on $\textsc{fdt}(\underline{P^F}, \underline{G^F})$:
1. Under $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{onebox})$, $\Act$ becomes $\mathit{onebox}$ with probability $1$, and $\textsc{Box B}$ becomes $\mathit{full}$ with probability $0.99$:
   $$\mathbb{E}\left[\VV \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{onebox}\right)\right] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000.$$
2. Under $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{twobox})$, $\Act$ becomes $\mathit{twobox}$ with probability $1$, and $\textsc{Box B}$ becomes $\mathit{full}$ with probability $0.01$:
   $$\mathbb{E}\left[\VV \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{twobox}\right)\right] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$

Since $\$990,000 > \$11,000$, Equation (4) yields $\mathrm{A\text{-}FDT}(P^F, G^F) = \mathit{onebox}$. Notice that this requires no belief in retrocausality: Fiona knows no physical signal travels backward in time from her choice to yesterday's prediction. Rather, she recognizes that holding the predictor's output fixed while varying the output of $\mathrm{FDT}(P^F, G^F)$ violates a structural constraint of the problem—analogous to imagining a working calculator outputting $3159$ while holding fixed $6288 + 1048 = 7336$. Relative to **A-FDT** counterfactuals (which hold fixed the predictor's accuracy rather than the predictor's specific historical guess), $\mathit{onebox}$ dominates $\mathit{twobox}$ when the predictor errs vs. succeeds in the relevant functional states. Every decision theory induces its own dominance principle via its counterfactual operator "$\hookrightarrow$"; hence, CDT dominance cannot serve as a neutral criterion against **A-FDT**.

### 3.3 The Smoking Lesion Problem: Separating Common Causes from Subjunctive Links

In the smoking lesion problem, an unobserved arterial lesion ($\textsc{Lesion} \in \{\mathit{lesion}, \mathit{nolesion}\}$) causes agents to love smoking and independently causes fatal lung cancer $99\%$ of the time ($\textsc{Luck} = \mathit{unlucky}$ with probability $0.99$), whereas agents without the lesion develop cancer only $1\%$ of the time. Surviving cancer is worth $\$1,000,000$, and smoking yields an additional $\$1,000$ to those who desire it.

For EDT and CDT, the probabilistic network for the smoking lesion problem is isomorphic to Newcomb's problem under a simple relabeling of variables ($\textsc{Predisposition} \mapsto \textsc{Lesion}$, $\textsc{Box B} \mapsto \textsc{Death}$, etc.). Consequently, EDT refrains from smoking (earning $\$990,000$ conditional expectation instead of $\$11,000$), while CDT smokes.

Why does **A-FDT** not fall into EDT's trap? Because the subjunctive dependency graph $G^F$ is *not* isomorphic to Newcomb's problem. A biological lesion does not simulate $\mathrm{FDT}$ to decide whether to metastasize. Instead, as Yudkowsky and Soares formalize the problem in Section 6, the lesion alters the agent's *preferences* (her utility function):
- If $\textsc{Lesion} = \mathit{lesion}$, the agent has utility function $\mathcal{U}_S$ (which values smoking at $+\$1,000$) and runs the model $P^F_S$, so her action is governed by the node $\textsc{fdt}(\underline{P^F_S}, \underline{G^F})$.
- If $\textsc{Lesion} = \mathit{nolesion}$, the agent has utility function $\mathcal{U}_R$ (which values smoking at $-\$1$) and runs the model $P^F_R$, so her action is governed by a *different* node, $\textsc{fdt}(\underline{P^F_R}, \underline{G^F})$.

In Fiona's graph $G^F$ (Figure 4 of the paper), $\textsc{Lesion}$ has a causal arrow to $\textsc{Cancer} \to \textsc{Death} \to \VV$ and an arrow to $\Act$. Crucially, $\Act$ is a multiplexer of three parents—$\textsc{Lesion}$, $\textsc{fdt}(\underline{P^F_S}, \underline{G^F})$, and $\textsc{fdt}(\underline{P^F_R}, \underline{G^F})$:

$$\Act(\mathit{lesion}, s, r) \coloneqq s, \qquad \Act(\mathit{nolesion}, s, r) \coloneqq r.$$

Neither $\textsc{fdt}(\underline{P^F_S}, \underline{G^F})$ nor $\textsc{fdt}(\underline{P^F_R}, \underline{G^F})$ has an arrow to $\textsc{Lesion}$ or $\textsc{Cancer}$.

Suppose Fiona in fact has the lesion (though she cannot introspectively observe $\textsc{Lesion}$ and assigns prior probability $P^F_S(\mathit{lesion}) = p \in (0,1)$ and $P^F_S(\textsc{fdt}(\underline{P^F_R}, \underline{G^F}) = \mathit{smoke}) = q$). Because her actual model is $(P^F_S, G^F)$, Equation (4) intervenes specifically on the node $\textsc{fdt}(\underline{P^F_S}, \underline{G^F})$:
- Since $\textsc{Lesion}$ is not downstream of $\textsc{fdt}(\underline{P^F_S}, \underline{G^F})$, its probability remains invariant under $\mathtt{do}$:
  $$P^F_S\left(\mathit{lesion} \;\middle|\; \mathtt{do}(\textsc{fdt}(\underline{P^F_S}, \underline{G^F}) = \mathit{smoke})\right) = P^F_S\left(\mathit{lesion} \;\middle|\; \mathtt{do}(\textsc{fdt}(\underline{P^F_S}, \underline{G^F}) = \mathit{refrain})\right) = p.$$
- Conditional on $\textsc{Lesion} = \mathit{lesion}$ (probability $p$), expected survival utility is $0.01(\$1,000,000) = \$10,000$, and $\Act$ equals the intervened value of $\textsc{fdt}(\underline{P^F_S}, \underline{G^F})$.
- Conditional on $\textsc{Lesion} = \mathit{nolesion}$ (probability $1-p$), expected survival utility is $0.99(\$1,000,000) = \$990,000$, and $\Act$ is determined by $\textsc{fdt}(\underline{P^F_R}, \underline{G^F})$, which equals $\mathit{smoke}$ with probability $q$.

Evaluating Equation (4) under $\mathcal{U}_S$ yields:

$$\mathbb{E}\left[\VV \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F_S}, \underline{G^F}) = \mathit{smoke}\right)\right] = p(\$10,000 + \$1,000) + (1-p)(\$990,000 + q \cdot \$1,000),$$

$$\mathbb{E}\left[\VV \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F_S}, \underline{G^F}) = \mathit{refrain}\right)\right] = p(\$10,000) + (1-p)(\$990,000 + q \cdot \$1,000).$$

The $(1-p)$ terms are identical in both hypotheticals and cancel out in the comparison. Smoking exceeds refraining by $p \cdot \$1,000 > 0$, so $\mathrm{A\text{-}FDT}(P^F_S, G^F) = \mathit{smoke}$. Thus, a single decision rule one-boxes in Newcomb's problem and smokes in the smoking lesion problem.

### 3.4 Updateless Evaluation: Transparent Newcomb, Parfit's Hitchhiker, and Blackmail

The most distinctive feature of **A-FDT** emerges when an agent makes an observation *after* a predictor has acted—as in the Transparent Newcomb Problem (where both boxes are transparent, and the predictor fills Box B iff she predicts the agent will one-box upon seeing Box B $\mathit{full}$), Parfit's Hitchhiker (where the driver rescues the agent from the desert iff she predicts the agent will pay $\$1,000$ upon observing $\Obs = \mathit{city}$), and the Mechanical Blackmail problem (where a blackmailer launches a mutually destructive $\$1,000,000$ rumor-publishing program iff she predicts the agent will wire $\$1,000$ upon observing $\Obs = \mathit{blackmail}$).

In all three problems, once the agent observes $\Obs = \mathit{full}$ (or $\mathit{city}$, or $\mathit{blackmail}$), both EDT and CDT condition their distributions on $\Obs = \mathit{full}$. Given that Box B is *already seen to be full*, $\mathbb{E}[\VV \mid \Act = \mathit{twobox}, \Obs = \mathit{full}] = \mathbb{E}[\VV \mid \mathtt{do}(\Act = \mathit{twobox}), \Obs = \mathit{full}] = \$1,001,000 > \$1,000,000$. Consequently, both EDT and CDT two-box (and refuse to pay the driver, and pay the blackmailer). Foreseeing this, the predictor leaves Box B empty, the driver leaves EDT and CDT agents to die in the desert, and the blackmailer extorts them.

How does **A-FDT** evaluate the Transparent Newcomb Problem when Fiona sees $\Obs = \mathit{full}$? In Fiona's graph $G^F$ (Figure 5b of the paper), there are two functional nodes corresponding to the two possible observations: $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$ and $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$. Because the predictor specifically simulates what Fiona will do *upon seeing a full box*, the node $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$ has an arrow to $\textsc{Prediction} \to \textsc{Box B}$ (and $\textsc{Prediction}$ determines which of the two $\textsc{fdt}$ nodes controls $\Act$):

$$\Act\left(\textsc{Prediction} = \mathit{1}, f_{\mathit{full}}, f_{\mathit{empty}}\right) = f_{\mathit{full}}, \qquad \Act\left(\textsc{Prediction} = \mathit{2}, f_{\mathit{full}}, f_{\mathit{empty}}\right) = f_{\mathit{empty}}.$$

> **Technical Clarification on Section 6 of the Source Paper:** In Section 6 ("Transparent Newcomb Problem"), Yudkowsky and Soares write an unnumbered display expression with a typographical error (including an unmatched parenthesis): $\mathbb{E}(\VV \mid \mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \act, \Obs = \mathit{full})$. However, as the authors explicitly state in the paragraph immediately preceding that formula ("Fiona does not react to observations by conditioning her distribution. Rather, she reacts to observations by switching which variable she intervenes on"), in Section 5's Equation (4), and in the actual numerical derivation that immediately follows, **A-FDT** *does not condition on $\Obs = \mathit{full}$*.

Let us verify the exact calculation from Equation (4) without conditioning on $\Obs = \mathit{full}$. Let $q \coloneqq P^F(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty}) = \mathit{twobox})$ be Fiona's prior probability that she two-boxes if she sees an empty box, and recall $\mathbb{P}(\textsc{Accurate} = \mathit{accurate}) = 0.99$:
1. **Intervention $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{onebox})$**:
   - With probability $0.99$ ($\mathit{accurate}$), the predictor predicts $\mathit{1}$, puts $\$1,000,000$ in Box B ($\mathit{full}$), and Fiona's action is governed by $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{onebox}$, yielding $\$1,000,000$.
   - With probability $0.01$ ($\mathit{inaccurate}$), the predictor predicts $\mathit{2}$, leaves Box B $\mathit{empty}$, and Fiona's action is governed by $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$, yielding $q \cdot \$1,000$ in expectation.
   - Total expected utility:
     $$\mathbb{E}\left[\VV \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{onebox}\right)\right] = \$990,000 + 0.01q \cdot \$1,000.$$
2. **Intervention $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{twobox})$**:
   - With probability $0.01$ ($\mathit{inaccurate}$), the predictor mistakenly predicts $\mathit{1}$, fills Box B ($\mathit{full}$), and Fiona's action is governed by $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{twobox}$, yielding $\$1,001,000$.
   - With probability $0.99$ ($\mathit{accurate}$), the predictor accurately predicts $\mathit{2}$, leaves Box B $\mathit{empty}$, and Fiona's action is governed by $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$, yielding $q \cdot \$1,000$ in expectation.
   - Total expected utility:
     $$\mathbb{E}\left[\VV \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{twobox}\right)\right] = 0.01(\$1,001,000) + 0.99q \cdot \$1,000 = \$10,010 + \$990q.$$
     *(Note: The source text prints $\$110,00 + q \cdot \$990$ due to a misplaced comma/digit, though the inequality is unaffected.)*

For any $q \in [0,1]$, $\$990,000 + \$10q > \$10,010 + \$990q$. Thus $\mathrm{A\text{-}FDT}(P^F, G^F, \mathit{full}) = \mathit{onebox}$. Even while staring directly at a full Box B, when Fiona imagines her algorithm $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$ outputting $\mathit{twobox}$, she imagines a counterfactual universe in which the predictor foresaw that output and $99\%$ likely left Box B empty—so that she would not have been observing $\mathit{full}$ at all! By the exact same updateless mechanics, **A-FDT** pays the driver upon reaching the city in Parfit's hitchhiker problem, refuses to pay the blackmailer in the Mechanical Blackmail problem (provided the blackmailer's false-positive prediction rate is sufficiently small, e.g., $0.0009$, where refusing loses $0.0009 \times \$1,000,000 = \$900 < \$1,000$), and stays put in Damascus in Gibbard and Harper's (1978) *Death in Damascus* without falling into CDT's infinite ratification loops or refusing a $\$1$ truly random coin.

---

## 4. Open Questions and Operational Extensions for Unfamiliar Problems

While Yudkowsky and Soares demonstrate how **A-FDT** resolves canonical dilemmas once the graph $G$ is given, a practitioner seeking to apply Equation (4) to *unfamiliar* cases immediately confronts three open questions left unresolved by the source paper. Below, we clearly distinguish what the source text states about these uncertainties from our own constructive operational proposals for resolving them.

### 4.1 Open Question 1: How to Construct the Subjunctive Graph $G$

**What the source states:** Yudkowsky and Soares explicitly acknowledge that Equation (4) "works *given* a graph that accurately describes how changing the value of a logical variable affects other variables, but it is not yet clear how to construct such a thing—nor even whether it can be done in a satisfactory manner within Pearl's framework. Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory" (Section 5).

**Operational Proposal (The Four-Step Subjunctive Modeling Protocol):** To apply **A-FDT** to a novel problem without an existing formal theory of counterpossibles, we can systematize the implicit modeling conventions of Section 6 into a four-step structural equation protocol:

1. **Step 1: Contextual Function-Node Indexing.** Identify the partition of possible epistemic/observational inputs the agent might receive in the dilemma. These include both explicit observations $\obs \in \mathcal{X}$ (e.g., $\{\mathit{full}, \mathit{empty}\}$ or $\{\mathit{letter}, \emptyset\}$) and any unobserved internal preference states $c \in \mathcal{C}$ that alter the agent's model $P_c$ (as in the smoking lesion's $\{P_S, P_R\}$). For each distinct tuple $(P_c, G, \obs)$, introduce a root logical variable $F_{c,\obs} \coloneqq \textsc{fdt}(\underline{P_c}, \underline{G}, \underline{\obs})$ taking values in $\mathcal{A}$.
2. **Step 2: Multiplexed Physical Action Specification.** Introduce the physical action node $\Act$ and a structural equation linking it to the family $\{F_{c,\obs}\}$, the variables determining the actual context $(C, \Obs)$, and any physical execution noise $U_{\text{act}}$ (such as the cosmic ray in Section 7's Cosmic Ray Problem):
   $$\Act = g_{\text{act}}\left(C, \Obs, \{F_{c,\obs}\}_{c \in \mathcal{C}, \obs \in \mathcal{X}}, U_{\text{act}}\right),$$
   where, in the absence of noise $U_{\text{act}}$, $g_{\text{act}}$ simply selects $F_{c,\obs}$ when $C = c$ and $\Obs = \obs$.
3. **Step 3: The Algorithmic Simulation Criterion for Outgoing Subjunctive Arrows.** For every environmental variable $Z$ (e.g., another agent's move, a predictor's setup, a blackmailer's decision), ask: *Does the physical mechanism generating $Z$ causally depend on running, simulating, proved-theorem-checking, or sharing the computational specification of the agent's decision procedure in context $(c, \obs)$?*
   - If **yes**, draw a directed arrow $F_{c,\obs} \to Z$, combined with an independent noise variable $U_Z$ representing prediction or replication error (e.g., $\textsc{Accurate}$).
   - If **no**—if $Z$ correlates with $\Act$ purely because a historical, biological, or environmental common cause $W$ influences both $Z$ and which context $(C, \Obs)$ the agent enters (or influences $U_{\text{act}}$)—draw arrows $W \to Z$ and $W \to C$ (or $W \to \Obs$), with *no* arrow from $F_{c,\obs}$ to $W$ or $Z$.
4. **Step 4: Causal Completion and Unconditional Intervention.** Add standard Pearl causal arrows from $\Act$ and environmental variables $Z$ to $\Obs$ and $\VV$. When the agent finds herself in context $(c^*, \obs^*)$, she computes Equation (4) by setting $\mathtt{do}(F_{c^*,\obs^*} = \act)$ for each $\act \in \mathcal{A}$ and taking the *unconditional* expectation of $\VV$ over all exogenous variables $(W, U_Z, U_{\text{act}})$ and non-intervened function nodes $\{F_{c,\obs}\}_{(c,\obs) \neq (c^*,\obs^*)}$.

### 4.2 Open Question 2: Cross-Context Coupling and Action-FDT vs. Policy-FDT

**What the source states:** In Footnotes 7 and 16, Yudkowsky and Soares remark that in their "preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions," adding that "[t]he difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

In the single-agent examples analyzed in Section 6 (Smoking Lesion and Transparent Newcomb), intervening on a single context node $F_{\obs^*}$ leaves the other context nodes $F_{\obs'}$ ($\obs' \neq \obs^*$) as random variables governed by a prior probability parameter $q$. In both of those examples, $q$ either canceled out completely (Smoking Lesion) or multiplied a tiny $0.01$ error term that could not reverse the preference ordering (Transparent Newcomb). However, the source paper does not explain how an **A-FDT** agent should determine $q$—or how Equation (4) behaves—when a single-agent problem *couples* the payoffs across different observation nodes!

**Operational Analysis and Proposal:** To see why this matters even in single-agent problems, consider an unfamiliar dilemma we may call **The Contingent Audit Problem**:

> **Dilemma (The Contingent Audit Problem):** A regulator uses a $50/50$ fair coin ($\textsc{Coin} \in \{\mathit{heads}, \mathit{tails}\}$) to send an agent either a **Green Notice** ($\Obs = \mathit{green}$) or a **Blue Notice** ($\Obs = \mathit{blue}$). At either notice, the agent must choose $\act \in \{\mathit{A}, \mathit{B}\}$, where choosing $\mathit{A}$ yields an immediate bonus of $\$1,000$ and choosing $\mathit{B}$ yields $\$0$. However, before sending the notice, an infallible predictor simulates the agent's decision function under *both* notices—predicting $F_{\mathit{green}} \coloneqq \textsc{fdt}(\underline{P}, \underline{G}, \mathit{green})$ and $F_{\mathit{blue}} \coloneqq \textsc{fdt}(\underline{P}, \underline{G}, \mathit{blue})$. The regulator awards a $\$1,000,000$ consistency grant iff the predictor predicts that the agent takes the *exact same action* across both notices ($F_{\mathit{green}} = F_{\mathit{blue}}$), and moreover only awards the grant if that common action is $\mathit{B}$ (i.e., $F_{\mathit{green}} = F_{\mathit{blue}} = \mathit{B}$). Suppose the agent receives $\Obs = \mathit{green}$. What does Equation (4) prescribe?

Let us apply **A-FDT** via Equation (4). In $G$, both $F_{\mathit{green}}$ and $F_{\mathit{blue}}$ have arrows into $\textsc{Grant} = \mathbb{I}(F_{\mathit{green}} = \mathit{B} \land F_{\mathit{blue}} = \mathit{B})$. When the agent observes $\Obs = \mathit{green}$, Equation (4) intervenes *only* on $F_{\mathit{green}}$, leaving $F_{\mathit{blue}}$ distributed according to the agent's prior $q \coloneqq P(F_{\mathit{blue}} = \mathit{B})$:
- Under $\mathtt{do}(F_{\mathit{green}} = \mathit{B})$, the grant is awarded iff $F_{\mathit{blue}} = \mathit{B}$ (probability $q$). On the $\mathit{heads}$ branch (probability $0.5$), the agent gets $\$0$ bonus; on the $\mathit{tails}$ branch (probability $0.5$), she gets $(1-q)\$1,000$ bonus. Thus:
  $$\mathbb{E}\left[\VV \;\middle|\; \mathtt{do}(F_{\mathit{green}} = \mathit{B})\right] = q(\$1,000,000) + 0.5(1-q)(\$1,000).$$
- Under $\mathtt{do}(F_{\mathit{green}} = \mathit{A})$, the grant condition $F_{\mathit{green}} = F_{\mathit{blue}} = \mathit{B}$ is false with probability $1$ ($\textsc{Grant} = \$0$), while the agent earns the $\$1,000$ bonus on the $\mathit{heads}$ branch:
  $$\mathbb{E}\left[\VV \;\middle|\; \mathtt{do}(F_{\mathit{green}} = \mathit{A})\right] = 0.5(\$1,000) + 0.5(1-q)(\$1,000).$$

Comparing the two expressions, **A-FDT** prefers $\mathit{B}$ over $\mathit{A}$ iff:

$$q \cdot \$1,000,000 > \$500 \iff q > 0.0005.$$

Notice the crucial operational dependence on $q$: if the agent's prior $P$ assigned $q = P(F_{\mathit{blue}} = \mathit{B}) = 0$ (for instance, if she pessimistically believed her counterfactual self at $\Obs = \mathit{blue}$ would grab the $\$1,000$), then at $\Obs = \mathit{green}$ **A-FDT** would output $\mathit{A}$ (and symmetrically at $\Obs = \mathit{blue}$ would output $\mathit{A}$), locking the agent into a bad coordination equilibrium across her own observation branches ($(\$1,000)$ instead of $\$1,000,000$)!

To make **A-FDT** fully operational in unfamiliar cross-coupled problems, we must distinguish two ways of completing the theory:
1. **Strict Action-Level Completion (Reflective Prior Constraint)**: If we strictly retain Equation (4)'s single-node intervention $\mathtt{do}(F_{\obs} = \act)$, we must supplement **A-FDT** with a *non-dogmatic self-simulation constraint* on $P$: for every $\obs' \neq \obs$, the prior $P(F_{\obs'} = \act')$ must be computed by recursively solving Equation (4) at $\obs'$ (or, where multiple fixed points exist, assigning non-extreme prior weight $q \in (\epsilon, 1-\epsilon)$ across Pareto-undominated fixed points). In the Contingent Audit Problem, any non-extreme uncertainty $q > 0.0005$ suffices for $\mathrm{A\text{-}FDT}$ to output $\mathit{B}$ at both notices, after which deductive reflection confirms $q = 1$.
2. **Policy Functional Decision Theory (P-FDT)**: Alternatively, as Yudkowsky and Soares suggest in Footnotes 7 and 16, one replaces Equation (4)'s single-node intervention with a simultaneous intervention on the entire policy vector $\pi = (\pi(\obs))_{\obs \in \mathcal{X}} \in \mathcal{A}^{\mathcal{X}}$, where a single root node $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$ determines $F_{\obs} = \pi(\obs)$ for *all* $\obs \in \mathcal{X}$ simultaneously, and the agent executes $\pi(\obs^*)$. Under **P-FDT**, the nuisance parameter $q$ disappears altogether because $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$ simultaneously fixes both $F_{\mathit{green}}$ and $F_{\mathit{blue}}$.

### 4.3 Open Question 3: Formalizing "Fair" Dilemmas

**What the source states:** In Section 9 and Footnote 15, Yudkowsky and Soares concede that no decision theory can win in dilemmas that directly punish agents for their internal source code (e.g., a mind-reader who pays $\$1,000,000$ iff the agent's brain implements CDT rather than **A-FDT**, or a game that punishes taking the same action as a copy of Fiona). They conjecture that **A-FDT** is optimal across all "fair problems"—informally defined as dilemmas where "the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the dilemma at hand"—while noting that formalizing fairness remains an open problem.

**Operational Proposal (Graph-Theoretic Extensionality):** Using our graphical framework $G$, we can formulate a clean operational test for whether an unfamiliar decision problem is *structurally fair* to **A-FDT**:

> **Definition (Extensional / Behavioral Fairness in $G$):** Let $\mathbf{F} = \{\textsc{fdt}(\underline{P}, \underline{G}, \underline{\obs})\}_{\obs \in \mathcal{X}}$ be the set of functional output nodes for the current dilemma, and let $\textsc{Code}$ be a random variable representing the syntactic implementation of the agent's decision algorithm $(P, G)$. A decision problem is *extensionally fair* if, in the true dependency graph $G$, $\textsc{Code}$ is $d$-separated from $\VV$ once we condition (or intervene) on the input-output nodes $\mathbf{F}$ and $\Act$—that is, every directed path from the agent's cognitive architecture to $\VV$ passes through the behavioral outputs $\mathbf{F}$ or $\Act$ in the dilemma at hand.

Whenever this extensionality condition holds, predictors in the environment respond exclusively to *what the decision function outputs* ($\mathbf{F}$), never to *how the function is syntactically written* independent of its output. In all such graphs, intervening on $\textsc{fdt}(\underline{P}, \underline{G}, \underline{\obs})$ captures $100\%$ of the decision-relevant dependencies between the agent's algorithm and her utility $\VV$.

---

## 5. Conclusion

**Action Functional Decision Theory (A-FDT)**, as formalized in Equation (4) of Yudkowsky and Soares (2017), resolves a decades-long impasse in instrumental rationality through a compact mathematical shift. By replacing CDT's intervention on the physical act token $\mathtt{do}(\Act = \act)$ and Bayesian conditioning on $\Obs = \obs$ with an updateless intervention on the logical output of the agent's decision function $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{\obs}) = \act)$, **A-FDT** preserves subjunctive dependencies with predictors, twins, and past observations while severing spurious statistical correlations with common physical causes. As a result, an **A-FDT** agent one-boxes in Newcomb's problem, smokes in the smoking lesion problem, pays the driver in Parfit's hitchhiker problem, resists extortion in both XOR and mechanical blackmail, and remains reflectively stable in *Death in Damascus*.

While deep foundational questions remain—most notably the development of a first-principles calculus for counterpossible conditionals ($\mathtt{true}(\phi)$) and the reconciliation of single-context action interventions (**A-FDT**) with global policy interventions (**P-FDT**) in cross-coupled environments—the structural modeling rules developed here allow practitioners to apply **A-FDT** rigorously to novel decision-theoretic and game-theoretic problems today.

---

## References

- Ahmed, Arif. 2014a. "Dicing With Death." *Analysis* 74 (4): 587–592.
- Ahmed, Arif. 2014b. *Evidence, Decision and Causality*. Cambridge University Press.
- Arntzenius, Frank. 2008. "No Regrets, or: Edith Piaf Revamps Decision Theory." *Erkenntnis* 68 (2): 277–297.
- Burgess, Simon. 2004. "The Newcomb Problem: An Unqualified Resolution." *Synthese* 138 (2): 261–287.
- Cohen, Daniel. 1990. "On What Cannot Be." In *Truth or Consequences: Essays in Honor of Nuel Belnap*, 123–132. Kluwer Academic Publishers.
- Dai, Wei. 2009. "Towards a New Decision Theory." *Less Wrong*, August 13, 2009.
- Drescher, Gary L. 2006. *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
- Eells, Ellery. 1984. "Metatickles and the Dynamics of Deliberation." *Theory and Decision* 17 (1): 71–95.
- Egan, Andy. 2007. "Some Counterexamples to Causal Decision Theory." *Philosophical Review* 116 (1): 93–114.
- Gibbard, Allan, and William L. Harper. 1978. "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, vol. 1, edited by C. A. Hooker, J. J. Leach, and E. F. McClennen. D. Reidel.
- Hintze, Daniel. 2014. "Problem Class Dominance in Predictive Dilemmas." PhD diss., Arizona State University.
- Jeffrey, Richard C. 1983. *The Logic of Decision*. 2nd ed. University of Chicago Press.
- Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Joyce, James M. 2007. "Are Newcomb Problems Really Decisions?" *Synthese* 156 (3): 537–562.
- Joyce, James M. 2012. "Regret and Instability in Causal Decision Theory." *Synthese* 187 (1): 123–145.
- Kleene, Stephen Cole. 1938. "On Notation for Ordinal Numbers." *Journal of Symbolic Logic* 3 (4): 150–155.
- Lewis, David. 1973. "Counterfactuals and Comparative Possibility." In *Ifs*, 57–85. Springer.
- Lewis, David. 1979. "Prisoners' Dilemma is a Newcomb Problem." *Philosophy & Public Affairs* 8 (3): 235–240.
- Lewis, David. 1981. "Causal Decision Theory." *Australasian Journal of Philosophy* 59 (1): 5–30.
- Nozick, Robert. 1969. "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel*, edited by Nicholas Rescher, 114–146. D. Reidel.
- Parfit, Derek. 1986. *Reasons and Persons*. Oxford University Press.
- Pearl, Judea. 1996. "Causation, Action, and Counterfactuals." In *6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-'96)*, 51–73. Morgan Kaufmann.
- Pearl, Judea. 2000. *Causality: Models, Reasoning, and Inference*. 1st ed. Cambridge University Press.
- Peirce, Charles Sanders. 1934. *Collected Papers of Charles Sanders Peirce, Vol. V: Pragmatism and Pragmaticism*. Harvard University Press.
- Skyrms, Brian. 1980. *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
- Skyrms, Brian. 1982. "Causal Decision Theory." *The Journal of Philosophy* 79 (11): 695–711.
- Soares, Nate, and Benja Fallenstein. 2015. "Toward Idealized Decision Theory." *arXiv preprint arXiv:1507.01986*.
- Spohn, Wolfgang. 1977. "Where Luce and Krantz Do Really Generalize Savage's Decision Model." *Erkenntnis* 11 (1): 113–134.
- Yudkowsky, Eliezer. 2010. *Timeless Decision Theory*. The Singularity Institute.
- Yudkowsky, Eliezer, and Nate Soares. 2017. "Functional Decision Theory: A New Theory of Instrumental Rationality." *arXiv preprint arXiv:1710.05060v2*.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Composing A-FDT Explanation**

I'm making progress on explaining Action Functional Decision Theory (A-FDT). My focus is on crafting a mathematical essay or technical blog post to help people understand how to use it in decision problems. The source text by Yudkowsky and Soares ("Functional Decision Theory: A New Theory of Instrumental Rationality") is my primary reference.


**Refining A-FDT Definition**

I've been working to refine the definition of Action Functional Decision Theory (A-FDT). My recent efforts center on ensuring the essay accurately explains A-FDT, especially Equation (4) from Section 5. The goal is to provide a clear and mathematically sound explanation for readers familiar with decision theory. I am aiming to ensure that the use of A-FDT is clearly and concisely presented.


**Defining Essay Scope**

I'm now focusing on defining the scope of this essay explaining A-FDT. I need to make sure I deliver a coherent, readable account with definitions, equations, examples, and explanations that will allow readers to decide unfamiliar cases using A-FDT. The core of my plan is to precisely explain the theory and distinguish source claims from my own. I'm aiming for a 2,400–3,000-word count.


**Prioritizing Clarity in A-FDT**

My current focus is prioritizing a clear explanation of A-FDT's core elements. I'm carefully reviewing the source text's structure, especially Section 5, and its mathematical details. I'm zeroing in on general expected utility maximization (Equation 1) and how A-FDT contrasts with EDT and CDT regarding decision hypotheticals. Specifically, the text presents Equation 1, then the differences in modeling $M^{a \hookrightarrow}$. My aim is a streamlined, understandable presentation of the central concepts.


**Clarifying A-FDT Formalism**

I'm now clarifying the formalism of Action Functional Decision Theory (A-FDT). My focus is specifically on Equation (4) from the source paper, which I plan to present clearly. I need to explain the rationale behind calling this A-FDT (action-intervening) to differentiate it from the policy-intervening variant discussed in footnotes 7 and 16. I'm exploring the implications of iterating over actions versus policies, and will incorporate the discussion into the mathematical explanation, drawing the reader's attention to the specific distinctions in the source text.


**Distinguishing A-FDT Formulation**

I'm now clarifying the key distinction between Action Functional Decision Theory (A-FDT) and the policy-based approach. The focus is on the difference between intervening on an action versus a policy. Equation (4) from the source paper is critical here. It clearly defines the action output, $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a$, which helps to underscore that A-FDT intervenes directly on the chosen action, not the policy itself. This nuance needs to be highlighted! I'm also ensuring the essay explains why A-FDT and the policy formulation diverge.


**Comparing A-FDT Variants**

I'm working to compare and contrast A-FDT with both CDT/EDT and Policy-FDT (TDT/UDT). My recent review of the source text now focuses on the Transparent Newcomb Problem discussed in Section 6. I'm checking a potential typo or quirk in that section, specifically regarding the absence of conditioning on $\textsc{Obs}=x$ in Equation (4), a point that the authors underscore. I'm focusing on how FDT responds to observation via changing the intervened-upon node.


**Analyzing Newcomb Problem**

I'm now analyzing the Transparent Newcomb Problem within the FDT framework. I've pinpointed a potential typo in Section 6, specifically within the inline display equation right below that paragraph. The equation doesn't align with the subsequent calculation, which actually doesn't condition on the observation, $\textsc{Obs}=\mathit{full}$. I'm working to clarify the implications of this discrepancy and how Fiona's strategy, switching intervened variables, impacts the solution compared to using expected utility. I will ensure this is properly explained in the mathematical essay, referencing how the display equation differs from the calculation.


**Clarifying A-FDT Updatelessness**

I'm focused on the updateless nature of A-FDT in the Transparent Newcomb problem. I've confirmed that Equation (4) in Section 6 is *not* conditional on the observation, $\textsc{Obs}=x$, despite a potentially misleading display equation. Highlighting this lack of update is crucial. I'm aiming to emphasize that A-FDT, even with observation, avoids conditioning for evaluation, aligning with the actual calculations and the "double update" discussion.


**Constructing FDT Procedures**

I'm now outlining a step-by-step operational procedure to build the Structural Causal/Subjunctive Model (SCM), which is needed to solve unfamiliar decision problems with Action Functional Decision Theory (A-FDT). My focus is on crafting a clear, constructive proposal to address the source text's open problem of constructing the structural graph G for A-FDT. I'll provide an operational procedure, distinguishing our approach from source claims. This process will include function-node partitioning as a critical step.


**Developing A-FDT Procedures**

I'm developing an operational procedure for using A-FDT, focusing on Structural Causal Models. I'm introducing function nodes $F_x$ for each context and modeling the agent's physical action as a multiplexer based on observation and function output. My key is to construct the model for determining when to connect $F_x$ to environmental variables, reflecting causal or simulated relationships. This framework provides concrete steps for applying A-FDT to practical decision problems.


**Investigating Stochasticity Effects**

I'm now investigating how stochastic observations impact A-FDT. I am focusing on what happens when the utility of an action under observation *x* actually depends on what the agent *would* do under a different observation *x'*, a situation where probabilities of the observations don't cancel out, as discussed in the Transparent Newcomb problem. The source text gives no explicit guidance on how to address this issue. I am exploring the implications of this stochasticity and considering how to integrate these nuances into the model.


**Planning FDT Formalization**

I'm now planning the formalization of "fair" versus "unfair" dilemmas in the A-FDT framework. I plan to define this boundary in terms of the structural graph, $G$, ensuring that environmental nodes depend on the function node, $F_x$, (or the agent's action, $\textsc{Act}$) rather than a meta-variable that represents the syntactic identity of the algorithm, $(P, G)$. I also plan to analyze cases where stochastic observations' value depends on actions under different observations.


**Refining Essay Outline**

I'm now refining the structure and word count of the essay. I'm aiming for a comfortable range of 2,650–2,850 words. The plan is to break the essay into sections. The introduction (~350 words) will cover the EDT/CDT tension and introduce A-FDT. The second section (~650 words) will present the A-FDT framework, including expected utility and the formal architecture. The remaining sections will break down A-FDT into specific components.


**Explaining A-FDT Equation**

I'm now focused on contrasting EDT (Equation 2) and Pearl-style CDT (Equation 3) with A-FDT (Equation 4). My main task is to explain each component of Equation (4), specifically addressing the probability distribution $P$ and dependency graph $G$. I'm highlighting dequoting notation, benign self-reference, and why the $\mathtt{do}$ operator is used. The two key departures from CDT (intervening on the logical function and updatelessness) are central.


**Detailing Function-Node Propagation**

I'm working on explaining subjunctive dependence, the difference between type-level and token-level interventions. My focus is crafting examples that highlight propagation through the function node and applying A-FDT to canonical decision problems. I'm aiming to apply the framework to Newcomb's Problem, the Smoking Lesion Problem, and one more example, with each case explained mathematically using A-FDT.


**Elaborating A-FDT Example**

I am now elaborating on an example to demonstrate A-FDT. I'm focusing on updateless evaluation in the Transparent Newcomb problem, detailing the exact expected utility calculation. I'm clarifying the mathematical treatment of observation and how the A-FDT agent accounts for changes to actions. I'll highlight the typographical discrepancy in the source paper and explore how this ties into A-FDT's treatment of observation.


**Operationalizing A-FDT Protocol**

I've been working on an operational protocol for applying A-FDT to new decision problems. My recent focus has been on two open problems. Firstly, I am proposing a 4-step protocol for constructing the subjunctive graph *G*. Secondly, I'm analyzing the implications of cross-context dependencies, where payoffs are coupled across observations, especially regarding the harmless nuisance parameter *q* and the distinctions between action vs. policy FDT in such scenarios.


**Formalizing Fair Prediction**

I'm now focusing on formalizing "fair" versus "unfair" behavioral prediction within the A-FDT framework, moving past merely syntactic discrimination. I plan to define "fairness" in terms of the structural graph, G, and identify graph-theoretic criteria. These criteria will ensure the agent's environmental nodes depend on a function node (or action) rather than on syntactic factors like the algorithm's identity. I also intend to incorporate discussion of the cases involving stochastic observations' value which depends on different observations.


```
