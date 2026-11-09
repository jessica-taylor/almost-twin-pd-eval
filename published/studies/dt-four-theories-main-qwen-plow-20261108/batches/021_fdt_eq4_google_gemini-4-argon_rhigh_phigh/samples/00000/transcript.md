# 021_fdt_eq4_google_gemini-4-argon_rhigh_phigh / 00000

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/ec9d51df-b2a4-41e9-a614-1eb9f0f40545/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/ec9d51df-b2a4-41e9-a614-1eb9f0f40545/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Action Functional Decision Theory (A-FDT): Formal Mechanics, Subjunctive Dependence, and Operational Application

## 1. Introduction: The Instrumental Impasse and the Functional Turn

For half a century, normative decision theory has been divided between two competing accounts of instrumental rationality: **evidential decision theory (EDT)** and **causal decision theory (CDT)**. When an agent chooses an action $a$ from a finite set of available options $\mathcal{A}$, both theories agree that she should maximize expected utility, yet they disagree on how to construct the hypothetical scenarios under which candidate actions are evaluated. EDT evaluates an action as a piece of *evidence* about the state of the world, asking which physical act would be the best news to learn one had taken. CDT evaluates an action as a localized *physical intervention*, asking which physical act causes the best downstream outcomes while holding the causal past fixed.

Measured by average utility achieved across classic decision-theoretic dilemmas, neither theory is uniformly satisfactory. In Newcomb's problem (Nozick 1969) and the psychological twin prisoner's dilemma (Lewis 1979), EDT prescribes the utility-maximizing action (one-boxing; cooperating) while CDT prescribes the worse-off action (two-boxing; defecting). Conversely, in medical common-cause dilemmas such as the smoking lesion problem (Skyrms 1980) or the XOR blackmail problem (Soares and Fallenstein 2015), CDT makes the sensible choice (smoking; refusing to pay) while EDT is exploited by purely statistical or manufactured correlations into "managing the news." And in sequential predictive dilemmas where the agent's observation reveals the predictor's past move—such as Parfit's hitchhiker problem (Parfit 1986), the transparent Newcomb problem (Drescher 2006), and mechanical blackmail—*both* CDT and EDT fail to secure the high-utility outcome, leaving agents stranded in the desert or vulnerable to predictable extortion.

In *"Functional Decision Theory: A New Theory of Instrumental Rationality"* (2017), Eliezer Yudkowsky and Nate Soares propose a unified resolution to this impasse. The core philosophical thesis of their framework is that an agent should not treat her decision as an isolated physical token (the bodily movement $\textsc{Act} = a$), nor as an empirical datum to condition upon. Instead, she should treat her decision as the logical output of a *fixed mathematical decision function* that answers the question: *"Which output of this very function would yield the best outcome?"*

While Yudkowsky and Soares note in footnotes 7 and 16 of their paper that their preferred general formalization of functional decision theory optimizes over full *policies* (mappings from observations to actions), the primary formal rule they present and analyze throughout the body of their paper—**Equation (4) in Section 5**—evaluates and selects individual *actions* $a \in \mathcal{A}$ by intervening on the logical output of the decision function for the agent's current observation history. In this essay, we refer to the decision theory defined by Equation (4) as **action functional decision theory (A-FDT)**. 

Our goal is twofold: first, to provide a rigorous mathematical exposition of A-FDT, showing how its graphical intervention mechanics and "updateless" treatment of observations resolve classic dilemmas; and second, to examine the foundational questions that Yudkowsky and Soares leave open—such as how to construct graphs of subjunctive dependence and when action-level intervention diverges from policy-level optimization—and develop concrete operational rules for applying A-FDT to unfamiliar decision problems.

---

## 2. The Formal Machinery of A-FDT

### 2.1 The Expected Utility Framework

Following Gibbard and Harper (1978) and the representation theorem of Joyce (1999), EDT, CDT, and A-FDT share a common foundational skeleton. Let $\mathcal{A}$ be a finite set of actions, $\mathcal{X}$ a countable set of observation histories, $\mathcal{O} = \{o_1, o_2, \dots\}$ a countable set of outcomes, and $\mathcal{U}: \mathcal{O} \to \mathbb{R}$ a bounded utility function. An agent who has received observation history $x \in \mathcal{X}$ seeks to select an action $a \in \mathcal{A}$ that maximizes expected utility, defined in Equation (1) of Yudkowsky and Soares (2017) as:

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j), \tag{1}$$

where $P(a \hookrightarrow o_j ;\, x)$ denotes the subjective probability that outcome $o_j$ will obtain in the hypothetical scenario where action $a$ is taken after observing $x$. As Joyce (1999) observes, "decision theories should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated." That epistemic perspective is entirely encoded in the interpretation of the decision-hypothetical connective "$\hookrightarrow$".

Computationally, an agent maintains a world-model $M$ and, for each candidate action $a \in \mathcal{A}$, performs a formal operation on $M$ to construct a hypothetical world-model $M^{a\hookrightarrow}$ from which she computes the expected value of utility $\textsc{V} \coloneqq \mathcal{U}(\textsc{Outcome})$.

### 2.2 From EDT and CDT to Equation (4)

To see precisely how A-FDT modifies the epistemic perspective of decision-making, compare the three formal decision rules presented in Section 5 of Yudkowsky and Soares (2017).

**Evidential Decision Theory (EDT)** takes the world-model $M$ to be a standard Bayesian probability distribution $P$ over variables including $\textsc{Obs}$, $\textsc{Act}$, and $\textsc{V}$, and constructs the hypothetical $M^{a\hookrightarrow}$ via standard Bayesian conditionalization:

$$\mathrm{EDT}(P, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \mid \textsc{Obs}=x, \textsc{Act}=a\right), \tag{2}$$

where actions with prior probability zero are excluded. Because Equation (2) merely conditions on $\textsc{Act}=a$, any statistical correlation between $\textsc{Act}$ and past state variables is preserved intact.

**Causal Decision Theory (CDT)** augments the probability distribution $P$ with a causal graph $G$—formalized by Yudkowsky and Soares using Pearl's (1996, 2000) graphical causal models—so that $M = (P, G)$. Here, $G$ is a directed acyclic graph (DAG) whose edges encode direct causal dependencies, and $P$ factorizes according to $G$. CDT constructs its hypothetical via Pearl's surgical intervention operator $\mathtt{do}(\textsc{Act}=a)$, which deletes all incoming arrows into the physical action node $\textsc{Act}$, fixes $\textsc{Act}=a$, and propagates changes exclusively to nodes causally downstream of $\textsc{Act}$, while conditioning on the observation $\textsc{Obs}=x$:

$$\mathrm{CDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x\right). \tag{3}$$

**Action Functional Decision Theory (A-FDT)** retains the graphical surgery apparatus of $(P, G)$ and Pearl's $\mathtt{do}$-operator, but shifts *what* is represented in $G$, *where* the intervention occurs, and *how* observations enter the calculation. In Equation (4) of Section 5, Yudkowsky and Soares define the rule (written there as $\mathrm{FDT}$, which we designate here as **A-FDT**) by:

$$\mathrm{FDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right). \tag{4}$$

When writing this rule explicitly under our assigned terminology, we denote the algorithm and its corresponding model-level variable with $\mathrm{AFDT}$ and $\textsc{afdt}$, respectively, while noting that they are mathematically identical to $\mathrm{FDT}$ and $\textsc{fdt}$ in Equation (4). Let us unpack the three foundational components of Equation (4).

### 2.3 Deconstructing Equation (4)

#### 1. Logical Variables, Quining, and Type-Level Intervention
In A-FDT, the probability distribution $P$ and graph $G$ do not merely range over physical events; they also contain variables representing the outputs of mathematical functions and algorithms. Just as an agent lacking logical omniscience may maintain a random variable in $P$ for the value of $6288 + 1048$ (concentrating probability on $7336$), an A-FDT agent with world-model $M = (P, G)$ and observation $x$ maintains a variable $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ in $G$ that represents the output of the A-FDT decision algorithm itself when evaluated on inputs $(P, G, x)$.

The underlines in $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ denote *dequoting*: if $x = \mathit{full}$, then $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ syntactically names the specific variable $\textsc{fdt}(\underline{P}, \underline{G}, \mathit{full})$ inside the graph $G$. As the authors point out, constructing a data structure $(P, G)$ that contains an accurate syntactic representation of a variable indexed by $(P, G)$ itself is a standard application of Kleene's (1938) second recursion theorem ("quining"). Crucially, the agent does not need to know the *output value* $\mathrm{FDT}(P, G, x)$ in advance in order to include a *variable* $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ representing that output in her model and to intervene upon it.

In Peirce's (1934) terminology, whereas CDT intervenes on the physical *token* $\textsc{Act}$ ("my body performs $a$"), A-FDT intervenes on the logical *type* $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ ("this mathematical decision function outputs $a$ on input $(P, G, x)$").

#### 2. Subjunctive Dependence vs. Causal Dependence
Because $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ is a logical variable, the directed edges in $G$ do not represent merely physical causation; they represent *subjunctive dependence*. Two physical systems—such as the agent's brain and a psychological twin's brain, or the agent's decision module and a predictor's simulation of that module—subjunctively depend on the same function when both compute or instantiate that function. 

Ideally, as Yudkowsky and Soares note, one might wish to define a logical conditional operator $\mathtt{true}(\phi)$ that updates a probability distribution $P$ on the counterpossible supposition that the mathematical statement $\textsc{fdt}(\underline{P}, \underline{x}) = a$ is true, yielding $\mathrm{FDT}^*(P, x) = \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}(\textsc{V} \mid \mathtt{true}(\textsc{fdt}(\underline{P}, \underline{x}) = a))$. Because probability theory currently lacks a general formalization of $\mathtt{true}(\cdot)$ for counterpossibilities (antecedents that run counter to mathematical necessity), Equation (4) instead requires that the dependency structure be supplied explicitly by the augmented graph $G$. Given $G$, Pearl's $\mathtt{do}$-operator computes the interventional distribution:

$$P\left(v_1, \dots, v_m \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right) = \mathbb{I}\left(v_{\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})} = a\right) \prod_{V_i \neq \textsc{fdt}(\underline{P}, \underline{G}, \underline{x})} P\left(v_i \mid \mathrm{pa}_G(v_i)\right).$$

When $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ is a root node of $G$, $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)$ simply substitutes the value $a$ into the structural equations of all children of $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$—including both the agent's physical action $\textsc{Act}$ and any external predictor's simulation of $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$—while leaving all variables not downstream of $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ untouched.

#### 3. Updatelessness: Responding to Observations by Shifting the Locus of Intervention
Comparing Equation (3) and Equation (4) reveals a profound difference in how CDT and A-FDT process observations $x$. In CDT, when the agent observes $x$, she restricts her expectation to the slice of the probability space where $\textsc{Obs} = x$ via Bayesian conditioning. In A-FDT, **$\textsc{Obs} = x$ does not appear as a conditioning event on the right-hand side of Equation (4)**. Instead, receiving observation $x$ changes *which node* in $G$ the agent intervenes upon: she intervenes on $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ rather than $\textsc{fdt}(\underline{P}, \underline{G}, \underline{y})$, while evaluating the expectation of $\textsc{V}$ globally across the entire distribution $P$ (an approach inherited from Wei Dai's 2009 *Updateless Decision Theory*, avoiding the harmful "double update" of Yudkowsky's 2010 *Timeless Decision Theory*, which both conditioned on evidence and intervened on the logical node).

Why is this absence of Bayesian conditioning on $\textsc{Obs}=x$ essential? Because in dilemmas like the transparent Newcomb problem or mechanical blackmail, *which observation the agent receives is itself downstream of the predictor's prediction of $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$*. Conditioning on $\textsc{Obs} = x$ would artificially sever the subjunctive link between the output of $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ and the probability of observing $x$ in the first place.

---

## 3. Applying A-FDT: Subjunctive Graphs and Worked Examples

When do EDT, CDT, and A-FDT agree, and when do they diverge? As Yudkowsky and Soares note in Section 5, if the world-model $(P, G)$ is such that every correlation between $\textsc{Act}$ and other decision-relevant variables is caused downstream of $\textsc{Act}$ (except for $\textsc{Act}$'s own dependence on $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$), then:

$$\mathbb{E}[\textsc{V} \mid a] = \mathbb{E}[\textsc{V} \mid \mathtt{do}(a)] = \mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})=a\right)\right],$$

and all three theories prescribe the exact same action. They diverge when events correlate with $\textsc{Act}$ without being physically caused by $\textsc{Act}$. Let us trace how A-FDT evaluates actions across three canonical classes of such problems.

### 3.1 Predictor vs. Common Cause: Newcomb's Problem and the Smoking Lesion Problem

Consider an A-FDT agent (whom the source calls Fiona) facing **Newcomb's problem** (Dilemma 2). Box A is transparent and contains $\$1,000$; Box B is opaque and contains either $\$1,000,000$ ($\mathit{full}$) or $\$0$ ($\mathit{empty}$). A predictor with $99\%$ accuracy ($\textsc{Accurate} = \mathit{accurate}$ with probability $0.99$, $\mathit{inaccurate}$ with probability $0.01$) has filled Box B if and only if she predicted the agent would leave Box A behind ($\mathit{onebox}$). No observation is made during the problem ($\mathcal{X}$ is trivial, so we omit $x$).

In CDT's causal graph $G^C$, a background variable $\textsc{Predisposition}$ is a common cause of both $\textsc{Act}$ and $\textsc{Prediction}$:

$$\textsc{Act} \leftarrow \textsc{Predisposition} \rightarrow \textsc{Prediction} \rightarrow \textsc{Box B} \rightarrow \textsc{V} \leftarrow \textsc{Act}.$$

When CDT executes $\mathtt{do}(\textsc{Act}=a)$, it severs the arrow $\textsc{Predisposition} \to \textsc{Act}$, rendering $\textsc{Box B}$ independent of the intervention: $P^C(\textsc{Box B}=\mathit{full} \mid \mathtt{do}(\textsc{Act}=a)) = p$ for both $a \in \{\mathit{onebox}, \mathit{twobox}\}$. Two-boxing then yields $p(\$1,001,000) + (1-p)(\$1,000)$, exceeding one-boxing by $\$1,000$ regardless of $p$.

In A-FDT's graph $G^F$, by contrast, the agent recognizes that both her physical action $\textsc{Act}$ and the predictor's mental simulation $\textsc{Prediction}$ subjunctively depend on the output of her decision procedure $\textsc{fdt}(\underline{P^F}, \underline{G^F})$. The structural equations in $(P^F, G^F)$ are:
*   $\textsc{Act}\big(\textsc{fdt}(\underline{P^F}, \underline{G^F})\big) = \textsc{fdt}(\underline{P^F}, \underline{G^F})$,
*   $\textsc{Prediction}(a, \mathit{accurate}) = a$, and $\textsc{Prediction}(a, \mathit{inaccurate}) = \neg a$, where $\neg\mathit{onebox} = \mathit{twobox}$,
*   $\textsc{Box B}(\mathit{onebox}) = \mathit{full}$ and $\textsc{Box B}(\mathit{twobox}) = \mathit{empty}$,
*   $\textsc{V}(\textsc{Act}, \textsc{Box B}) = \$1,000 \cdot \mathbb{I}(\textsc{Act}=\mathit{twobox}) + \$1,000,000 \cdot \mathbb{I}(\textsc{Box B}=\mathit{full})$.

Applying Equation (4), A-FDT compares the two interventional expectations:

$$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{onebox}\right)\right] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000,$$

$$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{twobox}\right)\right] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$

Since $\$990,000 > \$11,000$, $\mathrm{FDT}(P^F, G^F) = \mathit{onebox}$. Notice that A-FDT also induces its own *subjunctive dominance principle*: holding fixed the structural mechanisms of $G^F$ (namely, whether $\textsc{Accurate}$ is $\mathit{accurate}$ or $\mathit{inaccurate}$), switching the logical output of $\textsc{fdt}(\underline{P^F}, \underline{G^F})$ from $\mathit{twobox}$ to $\mathit{onebox}$ yields higher expected utility without any appeal to retrocausality.

Now compare **the smoking lesion problem** (Dilemma 3). Here, an unobserved arterial lesion ($\textsc{Lesion} \in \{\mathit{lesion}, \mathit{nolesion}\}$, with prior probability $P^F_S(\mathit{lesion}) = p \in (0,1)$) causes lung cancer $99\%$ of the time (whereas $\mathit{nolesion}$ causes cancer $1\%$ of the time, controlled by an independent variable $\textsc{Luck}$) and simultaneously causes the agent to value smoking at $+\$1,000$ (utility function $\mathcal{U}_S$, corresponding to distribution $P^F_S$) rather than $-\$1$ (utility function $\mathcal{U}_R$, corresponding to distribution $P^F_R$). Avoiding fatal cancer is worth $\$1,000,000$.

Why does A-FDT smoke here instead of refraining like EDT? Because an arterial lesion is not a predictor: it does not simulate or depend upon $\textsc{fdt}(\underline{P^F_S}, \underline{G^F})$. Rather, $\textsc{Lesion}$ is a physical switch that determines *which* world-model ($P^F_S$ or $P^F_R$) the agent's body actually runs:

$$\textsc{Act}\big(\textsc{Lesion}, \textsc{fdt}(\underline{P^F_S}, \underline{G^F}), \textsc{fdt}(\underline{P^F_R}, \underline{G^F})\big) = \begin{cases} \textsc{fdt}(\underline{P^F_S}, \underline{G^F}) & \text{if } \textsc{Lesion} = \mathit{lesion}, \\ \textsc{fdt}(\underline{P^F_R}, \underline{G^F}) & \text{if } \textsc{Lesion} = \mathit{nolesion}. \end{cases}$$

In $G^F$, there is no directed path from $\textsc{fdt}(\underline{P^F_S}, \underline{G^F})$ to $\textsc{Lesion}$ or $\textsc{Cancer}$. Consequently, for an agent with preferences $\mathcal{U}_S$ (who is uncertain whether she has the lesion and assigns probability $q$ to $\textsc{fdt}(\underline{P^F_R}, \underline{G^F}) = \mathit{smoke}$), intervening on $\textsc{fdt}(\underline{P^F_S}, \underline{G^F})$ leaves the probability of $\textsc{Lesion}$ invariant:

$$P^F_S\left(\mathit{lesion} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F_S}, \underline{G^F}) = \mathit{smoke}\right)\right) = P^F_S\left(\mathit{lesion} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F_S}, \underline{G^F}) = \mathit{refrain}\right)\right) = p.$$

Evaluating Equation (4) under $P^F_S$:
*   For $a = \mathit{smoke}$: With probability $p$, $\textsc{Lesion} = \mathit{lesion}$, her action is governed by $\textsc{fdt}(\underline{P^F_S}, \underline{G^F}) = \mathit{smoke}$, and her expected survival utility is $0.01(\$1,000,000) = \$10,000$ plus $\$1,000$ from smoking. With probability $1-p$, $\textsc{Lesion} = \mathit{nolesion}$, her action is governed by $\textsc{fdt}(\underline{P^F_R}, \underline{G^F})$ (which smokes with probability $q$), and her expected survival utility is $0.99(\$1,000,000) = \$990,000$. Thus:

    $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F_S}, \underline{G^F}) = \mathit{smoke}\right)\right] = p(\$10,000 + \$1,000) + (1-p)(\$990,000 + q \cdot \$1,000).$$

*   For $a = \mathit{refrain}$: The $(1-p)$ branch is identical, while the $p$ branch loses the $\$1,000$ smoking payoff:

    $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F_S}, \underline{G^F}) = \mathit{refrain}\right)\right] = p(\$10,000) + (1-p)(\$990,000 + q \cdot \$1,000).$$

Smoking strictly outperforms refraining by $p \cdot \$1,000 > 0$, so $\mathrm{FDT}(P^F_S, G^F) = \mathit{smoke}$.

### 3.2 Observation-Dependent Prediction: Transparent Newcomb, Parfit's Hitchhiker, and Blackmail

The distinctive power of Equation (4) becomes clearest when the agent receives a non-trivial observation $x \in \mathcal{X}$ prior to acting. Consider **the transparent Newcomb problem** (Dilemma 5), which is decision-theoretically isomorphic to **Parfit's hitchhiker problem** (Dilemma 4) and structurally analogous to **the mechanical blackmail problem** (Dilemma 8).

In the transparent Newcomb problem, both Box A ($\$1,000$) and Box B ($\$1,000,000$ or $\$0$) are transparent, so the agent observes $\textsc{Obs} \in \{\mathit{full}, \mathit{empty}\}$ before choosing whether to $\mathit{onebox}$ or $\mathit{twobox}$. The predictor (with $99\%$ accuracy) places $\$1,000,000$ in Box B if and only if she predicts that the agent would $\mathit{onebox}$ *upon observing that Box B is $\mathit{full}$*.

Suppose the agent observes $x = \mathit{full}$. Both CDT and EDT prescribe two-boxing: once the distribution is conditioned on $\textsc{Obs} = \mathit{full}$, Box B is guaranteed to contain $\$1,000,000$, so two-boxing yields $\$1,001,000$ while one-boxing yields $\$1,000,000$. Predictors foresee this, leaving CDT and EDT agents with an empty Box B (and leaving CDT and EDT hitchhikers to die in Parfit's desert).

How does A-FDT evaluate the choice upon observing $x = \mathit{full}$? In the A-FDT graph $G^F$ (Figure 5b of the source), there are two logical decision nodes corresponding to the two possible observations: $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$ and $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$. Because the predictor specifically predicts what the agent will do *if she sees a full box*, the structural equations of $(P^F, G^F)$ are:
1.  **Prediction**: $\textsc{Prediction}$ depends on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$ and $\textsc{Accurate}$ ($\mathit{accurate}$ with probability $0.99$):
    *   $\textsc{Prediction}(\mathit{onebox}, \mathit{accurate}) = \textsc{Prediction}(\mathit{twobox}, \mathit{inaccurate}) = 1$ (which sets $\textsc{Box B} = \mathit{full}$),
    *   $\textsc{Prediction}(\mathit{twobox}, \mathit{accurate}) = \textsc{Prediction}(\mathit{onebox}, \mathit{inaccurate}) = 2$ (which sets $\textsc{Box B} = \mathit{empty}$).
2.  **Physical Action Multiplexing**: Which logical node controls the agent's physical action $\textsc{Act}$ depends on which box state the predictor creates:

    $$\textsc{Act}\big(\textsc{Prediction}, \textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}), \textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})\big) = \begin{cases} \textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) & \text{if } \textsc{Prediction} = 1, \\ \textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty}) & \text{if } \textsc{Prediction} = 2. \end{cases}$$

When the agent sees $x = \mathit{full}$, Equation (4) instructs her to find $a \in \{\mathit{onebox}, \mathit{twobox}\}$ maximizing:

$$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = a\right)\right].$$

*(Technical note on the source text: In Section 6 of Yudkowsky and Soares 2017, a typographical error in the unnumbered display equation for Transparent Newcomb prints $\mathbb{E}(\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})=a, \textsc{Obs}=\mathit{full})$. As Equation (4) in Section 5, the surrounding prose in Section 6, and the calculation immediately following that display equation confirm, A-FDT does **not** condition on $\textsc{Obs}=\mathit{full}$.)*

Let $q \coloneqq P^F\big(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty}) = \mathit{twobox}\big)$ be the agent's prior probability that she two-boxes upon seeing an empty box. We now compute the exact expectations under Equation (4):
*   **Case 1: $\mathtt{do}\big(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{onebox}\big)$**.
    *   With probability $0.99$ ($\textsc{Accurate} = \mathit{accurate}$), $\textsc{Prediction} = 1$, so $\textsc{Box B} = \mathit{full}$ and $\textsc{Act} = \textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{onebox}$, yielding $\textsc{V} = \$1,000,000$.
    *   With probability $0.01$ ($\textsc{Accurate} = \mathit{inaccurate}$), $\textsc{Prediction} = 2$, so $\textsc{Box B} = \mathit{empty}$ and $\textsc{Act} = \textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$, yielding expected utility $q \cdot \$1,000$.
    *   Total expected utility:

        $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{onebox}\right)\right] = 0.99(\$1,000,000) + 0.01(q \cdot \$1,000) = \$990,000 + \$10q.$$

*   **Case 2: $\mathtt{do}\big(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{twobox}\big)$**.
    *   With probability $0.01$ ($\textsc{Accurate} = \mathit{inaccurate}$), $\textsc{Prediction} = 1$, so $\textsc{Box B} = \mathit{full}$ and $\textsc{Act} = \textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{twobox}$, yielding $\textsc{V} = \$1,001,000$.
    *   With probability $0.99$ ($\textsc{Accurate} = \mathit{accurate}$), $\textsc{Prediction} = 2$, so $\textsc{Box B} = \mathit{empty}$ and $\textsc{Act} = \textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$, yielding expected utility $q \cdot \$1,000$.
    *   Total expected utility:

        $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{twobox}\right)\right] = 0.01(\$1,001,000) + 0.99(q \cdot \$1,000) = \$10,010 + \$990q.$$
        *(Note: The source text prints $0.01 \cdot \$1,001,000$ as "$\$110,00$" due to a decimal typo; the exact figure is $\$10,010$, which leaves the comparison completely unaffected.)*

For every $q \in [0, 1]$, $\$990,000 + \$10q > \$10,010 + \$990q$. Hence $\mathrm{FDT}(P^F, G^F, \mathit{full}) = \mathit{onebox}$. Even while staring directly at $\$1,000,000$ in Box B, the A-FDT agent leaves the $\$1,000$ behind—because in her hypothetical for $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{twobox}$, she imagines a universe in which the predictor foresaw that output, left Box B empty with $99\%$ probability, and caused her to observe $\mathit{empty}$ instead!

This exact mechanism explains why A-FDT agents:
*   **Pay the driver in Parfit's hitchhiker problem** upon reaching the city ($\mathrm{FDT}(P^F, G^F, \mathit{city}) = \mathit{pay}$), because counterfactually outputting $\mathit{refuse}$ on input $\mathit{city}$ implies a world where the lie-detecting driver left the agent in the desert;
*   **Refuse to pay in mechanical blackmail** upon receiving the blackmail note ($\mathrm{FDT}(P^F, G^F, \mathit{blackmail}) = \mathit{refuse}$), because counterfactually outputting $\mathit{refuse}$ on input $\mathit{blackmail}$ implies a world where the blackmailer predicted refusal and never launched the mutually destructive program;
*   **Refuse to pay in XOR blackmail** (Dilemma 6), because the termite infestation is a root node in $G^F$ unaffected by $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{letter})$, whereas EDT is tricked into paying by conditioning on both the letter and its action; and
*   **Stay in Damascus without oscillation in Death in Damascus** (Dilemma 7), because wherever $\textsc{fdt}(\underline{P^F}, \underline{G^F})$ sends the agent, Death's appointment book subjunctively sends Death to the same city, making it trivially optimal to save the $\$1,000$ travel cost—and immediately willing to pay $\$1$ for a genuinely random coin that breaks Death's predictive edge.

---

## 4. Open Questions and Operational Extensions for Unfamiliar Cases

While Yudkowsky and Soares (2017) demonstrate A-FDT's compelling performance across classic dilemmas, they explicitly leave two foundational questions open for practitioners wishing to apply Equation (4) to unfamiliar decision problems. In what follows, we carefully distinguish what follows directly from the source paper from our own operational proposals designed to make A-FDT a self-contained procedure for novel cases.

### 4.1 Open Question 1: How Do We Construct the Subjunctive Graph $G$?

#### What the Source Establishes
In Sections 3, 5, and 10, Yudkowsky and Soares emphasize that Equation (4) operates *given* a graph $G$ encoding subjunctive dependencies, and they identify the problem of deducing $G$ from observation and experiment—as well as formalizing counterpossible conditionals—as "perhaps the largest open problem in the study of functional decision theory." In CDT, Pearl (2000) grounds causal arrows in physical mechanisms and physical randomized interventions. In A-FDT, however, $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ is the output of a fixed mathematical function; if it outputs $a_1$, then $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a_2$ is logically impossible, so one cannot deduce its outgoing arrows by physically randomizing a mathematical truth while holding the rest of mathematics fixed.

#### Operational Proposal 1: Algorithmic Instantiation Factoring (Additional Proposal)
To apply A-FDT to unfamiliar cases without a full philosophical theory of counterpossibilities, we need a clear operational rule for deciding when an environmental variable $Y$ receives a directed edge from $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ in $G$. We propose a three-step **Algorithmic Instantiation Factoring** procedure that treats $(P, G)$ as a *structural causal-computational model*:

1.  **Start with the standard physical causal DAG $G_{\text{phys}}$**. Identify all physical variables in the environment (e.g., $\textsc{Act}$, $\textsc{Outcome}$, genetic lesions, weather, other agents' physical actions $Y_1, \dots, Y_k$) and draw their standard Pearlian causal arrows.
2.  **Identify computational trackers of the decision function**. For each decision-relevant mechanism $Y_i$ in the environment that is not causally downstream of $\textsc{Act}$, ask an operational question about its physical data-generating process: *Does the physical mechanism generating $Y_i$ compute, simulate, or estimate the output of the agent's decision rule applied to the epistemic context $(P, G, x)$?*
    *   If $Y_i$ is generated by a physical process whose output is invariant to replacing the agent's decision module for $(P, G, x)$ with a different lookup table (for instance, a pre-existing termite infestation or a congenital arterial lesion), then $Y_i$ is **computationally insensitive** to $\mathrm{FDT}(P, G, x)$ and receives *no* arrow from $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$.
    *   If $Y_i$ is generated by a predictor, a psychological twin, a game-theoretic opponent modeling the agent's best-response function, or the agent's own future self facing the same normalized decision problem $(P, G, x)$, then $Y_i$ is **computationally sensitive** to $\mathrm{FDT}(P, G, x)$.
3.  **Parametrize noisy trackers via independent accuracy variables**. Whenever a mechanism $Y_i$ tracks $\mathrm{FDT}(P, G, x)$ with estimated reliability $\eta_i \in [0, 1]$, introduce an exogenous accuracy/noise node $E_i \sim \mathrm{Bernoulli}(\eta_i)$ and draw directed edges $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) \to Y_i \leftarrow E_i$, with structural equation:

    $$Y_i = \begin{cases} \psi_i\big(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})\big) & \text{if } E_i = 1 \text{ (accurate tracking)}, \\ Y_i^{\text{fallback}} & \text{if } E_i = 0 \text{ (tracking failure)}, \end{cases}$$

    where $\psi_i(a)$ is the tracker's response to predicting action $a$ and $Y_i^{\text{fallback}}$ is its noisy or default behavior when its prediction fails.

This operational rule reduces the counterpossible question ("What if this mathematical function had a different output?") to a well-defined counterfactual over *computational circuits* ("If we treat the lookup register storing the return value of $\mathrm{FDT}(P, G, x)$ as an exogenous input pin shared by every physical circuit in the universe that computes or estimates $\mathrm{FDT}(P, G, x)$, how does toggling that pin propagate through $G_{\text{phys}}$?").

### 4.2 Open Question 2: Off-Observation Nodes and Action-Level vs. Policy-Level Intervention

#### What the Source Establishes
In footnotes 7 and 16, Yudkowsky and Soares state:
> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

Why does A-FDT—Equation (4)—not require specifying the exact value of the off-observation variable $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x'})$ (for $x' \neq x$) in the paper's examples? Look back at the transparent Newcomb problem in Section 3.2: when the agent observes $x = \mathit{full}$, she intervenes *only* on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$, while treating $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$ as an un-intervened background variable with prior probability $q$ of two-boxing. Because the predictor in Transparent Newcomb only cares about $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$, the parameter $q$ cancels out in the ordinal comparison for every $q \in [0, 1]$.

However, the source leaves open two crucial operational questions for unfamiliar problems:
1.  How should an A-FDT agent determine the distribution (the parameter $q$) of off-observation nodes $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x'})$ when applying Equation (4) if the comparison *does* depend on $q$?
2.  In what exact class of problems does A-FDT (Equation 4) diverge from **policy functional decision theory (P-FDT)**, which intervenes simultaneously on the entire policy $\pi: \mathcal{X} \to \mathcal{A}$ via $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}) = \pi)$ and executes $\pi(x)$?

#### Operational Proposal 2: Recursive Off-Branch Resolution and the Multi-Observation Divergence Test (Additional Proposal)
To make A-FDT fully operational on unfamiliar multi-observation dilemmas, we must specify how $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x'})$ is evaluated when $x' \neq x$, and identify where single-node action intervention hits its structural limit.

**Rule A (Recursive Self-Evaluation for Off-Observation Nodes)**: Suppose an A-FDT agent observes $x \in \mathcal{X}$ and applies Equation (4) by intervening on $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$. If the expectation $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)]$ depends on the value of another node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x'})$ whose outcome does *not* itself depend on $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$, the agent should not leave $q = P(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x'}) = a')$ as an arbitrary free parameter. Instead, she can compute $\mathrm{FDT}(P, G, x')$ directly by running Equation (4) on input $x'$! For instance, in the transparent Newcomb problem, if the agent runs Equation (4) on $x' = \mathit{empty}$, notice that $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$ has no arrow to $\textsc{Prediction}$ in $G^F$; it only controls $\textsc{Act}$ in the $1\%$ or $99\%$ event that $\textsc{Box B} = \mathit{empty}$, where $\mathit{twobox}$ yields $\$1,000$ and $\mathit{onebox}$ yields $\$0$. Thus, Equation (4) evaluated at $x' = \mathit{empty}$ deterministically yields $\mathrm{FDT}(P^F, G^F, \mathit{empty}) = \mathit{twobox}$, justifying $q = 1$ (as Yudkowsky and Soares parenthetically remark in Section 6).

**Rule B (Diagnosing Divergence Between A-FDT and P-FDT)**: What if a predictor's action or a twin's payoff depends *jointly and non-additively* on the outputs of the decision procedure across *multiple* distinct observations $x_1, x_2 \in \mathcal{X}$? Let us construct a concrete unfamiliar dilemma to see what happens.

> **Example (The Split-Observation Coordination Dilemma)**. An agent will observe a fair coin flip $\textsc{Obs} \in \{\mathit{heads}, \mathit{tails}\}$ ($P(\mathit{heads}) = P(\mathit{tails}) = 0.5$) and must choose an action $a \in \{\mathit{cooperate}, \mathit{defect}\}$. Paying $\mathit{cooperate}$ costs $\$1,000$ in effort regardless of the coin flip. However, an infallible predictor examines the agent's decision function *before* the coin is flipped and places $\$1,000,000$ in the agent's bank account if and only if the predictor predicts that the agent would choose $\mathit{cooperate}$ on $\mathit{heads}$ **and** choose $\mathit{cooperate}$ on $\mathit{tails}$ (i.e., both $\textsc{fdt}(\underline{P}, \underline{G}, \mathit{heads}) = \mathit{cooperate}$ and $\textsc{fdt}(\underline{P}, \underline{G}, \mathit{tails}) = \mathit{cooperate}$). Suppose the coin lands $\mathit{heads}$. What does A-FDT do?

Let us apply Equation (4) at $x = \mathit{heads}$. The graph $G$ contains two root decision nodes: $F_H \coloneqq \textsc{fdt}(\underline{P}, \underline{G}, \mathit{heads})$ and $F_T \coloneqq \textsc{fdt}(\underline{P}, \underline{G}, \mathit{tails})$. The predictor's deposit is $\textsc{Bank} = \$1,000,000 \cdot \mathbb{I}(F_H = \mathit{cooperate} \land F_T = \mathit{cooperate})$, and the effort cost is $\$1,000 \cdot \big(0.5\,\mathbb{I}(F_H = \mathit{cooperate}) + 0.5\,\mathbb{I}(F_T = \mathit{cooperate})\big)$.

Under Equation (4), when the agent observes $\mathit{heads}$, she intervenes *only* on $F_H$, holding the prior distribution of $F_T$ fixed at $q \coloneqq P(F_T = \mathit{cooperate})$:

$$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(F_H = \mathit{cooperate})\right] = q(\$1,000,000) - \$500 - \$500q = \$999,500q - \$500,$$

$$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(F_H = \mathit{defect})\right] = \$0 - \$0 - \$500q = -\$500q.$$

Here, A-FDT's prescription at $x = \mathit{heads}$ depends critically on $q$:
*   If $q > \frac{500}{1,000,000} = 0.0005$, then $\mathrm{FDT}(P, G, \mathit{heads}) = \mathit{cooperate}$ (and by symmetry, $\mathrm{FDT}(P, G, \mathit{tails}) = \mathit{cooperate}$, which self-consistently ratifies $q = 1$ and wins the $\$1,000,000$).
*   However, if the agent initially assigns $q = 0$ (believing her $\mathit{tails}$-branch will defect), then intervening solely on $F_H$ yields $-\$500$ for $\mathit{cooperate}$ versus $\$0$ for $\mathit{defect}$, creating a perverse Coordination Nash Equilibrium $(F_H, F_T) = (\mathit{defect}, \mathit{defect})$ between the agent's own observation branches!

More starkly, suppose the predictor rewards the agent with $\$1,000,000$ if and only if $F_H = F_T = \mathit{cooperate}$, **and** the two observations $\mathit{heads}$ and $\mathit{tails}$ are structurally asymmetric (so that $F_H$ and $F_T$ are distinct nodes in $G$), while the effort cost of cooperating on $\mathit{heads}$ alone is slightly subsidized if $F_T = \mathit{defect}$ in a way that creates a prisoner's dilemma between the $F_H$ and $F_T$ nodes. Because Equation (4) intervenes on $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ one observation $x$ at a time, it treats $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x'})$ for $x' \neq x$ as an independent variable unless $G$ encodes a subjunctive link between them.

This yields a clear operational diagnostic for any unfamiliar problem:
1.  **When Pure A-FDT (Equation 4) Suffices**: Whenever external predictors or twins either (a) predict only the single node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ corresponding to a single observation $x$ (as in Newcomb, Transparent Newcomb, Parfit's Hitchhiker, and Mechanical Blackmail), or (b) receive symmetric inputs so that all players/branches evaluate the *exact same* node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$, Equation (4) is completely sufficient and invariant to off-branch beliefs.
2.  **Bridging Asymmetric Observations within A-FDT**: If an unfamiliar problem involves a predictor or twin whose behavior depends jointly on multiple distinct observation nodes $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_1})$ and $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_2})$, an A-FDT practitioner has two operational choices: either (i) recognize that both branches are computed by the same overarching algorithm $\mathrm{FDT}(P, G, \cdot)$ and evaluate the policy node $\textsc{fdt}(\underline{P}, \underline{G}) = \pi$ directly (transitioning to P-FDT as endorsed in footnotes 7 and 16), or (ii) select the Pareto-dominant fixed point $(q_1, q_2)$ among self-consistent branch beliefs when parameterizing $P$.

---

## 5. Conclusion

Action functional decision theory (A-FDT), as formalized in Equation (4) of Yudkowsky and Soares (2017), represents a decisive advance in the mathematics of instrumental rationality. By shifting the locus of Pearlian intervention from the physical action token $\textsc{Act}$ to the logical function output $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$, and by using the observation $x$ to index the point of intervention rather than conditioning the probability distribution $P$ on $\textsc{Obs} = x$, A-FDT captures the best features of both causal and evidential decision theory while avoiding their signature pathologies. It one-boxes in Newcomb's problem without refraining in the smoking lesion problem; it pays the driver in Parfit's hitchhiker problem and resists extortion in both XOR and mechanical blackmail; and it remains reflectively stable in Death in Damascus while assigning non-negative expected value to information and eliminating the need for costly physical precommitments.

At the same time, viewing Equation (4) with mathematical precision clarifies where the theory relies on rich structural inputs: it requires a world-model $(P, G)$ that distinguishes computational trackers of the agent's decision function from merely statistical common causes, and its single-observation intervention structure highlights why multi-observation coordination ultimately motivates the generalization from action-level intervention to policy-level functional decision theory. For human game theorists and designers of autonomous artificial agents alike, A-FDT provides a rigorous, coherent, and practical blueprint for rational agency in a world populated by predictors and peers.

---

## References

*   Ahmed, Arif. 2014. *Evidence, Decision and Causality*. Cambridge: Cambridge University Press.
*   Dai, Wei. 2009. "Towards a New Decision Theory." *LessWrong*, August 13, 2009.
*   Drescher, Gary L. 2006. *Good and Real: Demystifying Paradoxes from Physics to Ethics*. Cambridge, MA: MIT Press.
*   Eells, Ellery. 1984. "Metatickles and the Dynamics of Deliberation." *Theory and Decision* 17 (1): 71–95.
*   Gibbard, Allan, and William L. Harper. 1978. "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, edited by C. A. Hooker, J. J. Leach, and E. F. McClennen, Vol. 1. Boston: D. Reidel.
*   Jeffrey, Richard C. 1983. *The Logic of Decision*. 2nd ed. Chicago: University of Chicago Press.
*   Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. New York: Cambridge University Press.
*   Joyce, James M. 2012. "Regret and Instability in Causal Decision Theory." *Synthese* 187 (1): 123–145.
*   Kleene, Stephen Cole. 1938. "On Notation for Ordinal Numbers." *Journal of Symbolic Logic* 3 (4): 150–155.
*   Lewis, David. 1979. "Prisoners' Dilemma is a Newcomb Problem." *Philosophy & Public Affairs* 8 (3): 235–240.
*   Lewis, David. 1981. "Causal Decision Theory." *Australasian Journal of Philosophy* 59 (1): 5–30.
*   Nozick, Robert. 1969. "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel*, edited by Nicholas Rescher, 114–146. Dordrecht: D. Reidel.
*   Parfit, Derek. 1986. *Reasons and Persons*. New York: Oxford University Press.
*   Pearl, Judea. 1996. "Causation, Action, and Counterfactuals." In *Proceedings of the 6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-'96)*, 51–73. San Francisco, CA: Morgan Kaufmann.
*   Pearl, Judea. 2000. *Causality: Models, Reasoning, and Inference*. New York: Cambridge University Press.
*   Peirce, Charles Sanders. 1934. *Collected Papers of Charles Sanders Peirce, Vol. V: Pragmatism and Pragmaticism*. Cambridge, MA: Harvard University Press.
*   Skyrms, Brian. 1980. *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. New Haven, CT: Yale University Press.
*   Soares, Nate, and Benja Fallenstein. 2015. "Toward Idealized Decision Theory." arXiv preprint arXiv:1507.01986.
*   Spohn, Wolfgang. 1977. "Where Luce and Krantz Do Really Generalize Savage's Decision Model." *Erkenntnis* 11 (1): 113–134.
*   Yudkowsky, Eliezer. 2010. *Timeless Decision Theory*. Technical Report, The Singularity Institute, San Francisco, CA.
*   Yudkowsky, Eliezer, and Nate Soares. 2017. "Functional Decision Theory: A New Theory of Instrumental Rationality." arXiv preprint arXiv:1710.05060v2.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Scope**

I'm now focusing on defining the scope for a mathematical essay or technical blog post about Action Functional Decision Theory (A-FDT). My aim is to explain the application of A-FDT to decision problems, referencing the supplied paper. I intend to build a thorough understanding of the core concepts, from the paper.


**Clarifying Constraints & Scope**

I've been drilling down on the constraints for the A-FDT essay. I'm prioritizing Equation (4) from Section 5 as the central formal presentation, ensuring consistent use of "A-FDT" and clearly differentiating other theories. I will adhere to source quotations faithfully, with careful attention to how the theory handles dependencies. I'm preparing to address open questions with operational interpretations, distinguishing source claims from my own additions. Finally, I'm aiming for a word count between 2400 and 3000 words.


**Refining Equation (4)**

I'm now zeroing in on Equation (4) from Section 5, as it defines A-FDT by maximizing actions, not policies. I've re-examined the source paper's discussion of policies versus actions in footnotes 7 and 16. I believe this distinction is crucial to clarify, particularly for multi-agent problems. I'll need to clearly present Equation (4) in my essay, and will now start to prepare for the essay appendices and conclusion.


**Clarifying Typo Discovery**

I've got a fresh point to integrate: the importance of A-FDT's action-based formulation, specifically contrasting it with the policy-based preference from the source. I'm focusing on incorporating the notation from Equation (4), and will consistently use A-FDT in my writing. There's a curious typo in Section 6, so I plan to account for this quirk while presenting the analysis of the Transparent Newcomb Problem.


**Addressing the Missing Parenthesis**

I've got a critical point about a missing parenthesis and an interesting calculation in the source material. It seems the source contains an error where the calculation *doesn't* condition on the stated observation. I think highlighting this discrepancy is perfect for demonstrating a deep reading of the source! It highlights the important distinction in the equation's application, and this clarity will be a strength of my presentation. I can also integrate this into a plan to deconstruct the paper's structure.


**Analyzing Decision Foundations**

I'm now focusing on A-FDT's core insight: viewing decisions as outputs of a fixed mathematical function. I'm making distinctions between actions as tokens and actions as logical outputs. I'm also preparing to clarify how A-FDT differentiates from policy-based FDT, Updateless Decision Theory (UDT), and Timeless Decision Theory (TDT), with attention to Expected Utility foundations and Joyce's representation theorem. The goal is to provide a complete view.


**Unpacking Mathematical Components**

I'm now diving into the mathematical components of Equation (4) more deeply. My focus is on the world-model, (P, G). I'm looking at how P handles probability distributions over both physical and logical variables. G's DAG encoding of subjunctive dependence seems crucial, and I'll generalize causal dependence to encompass logical/computational dependencies for full clarity.


**Elaborating Algorithm Properties**

I'm now clarifying the properties of the A-FDT algorithm. I'm focusing on how the function $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ identifies a node in $G$ corresponding to its output. I'm also distinguishing between the object-level function and the model-level random variable. Finally, I'm working to clarify structural shifts from CDT to A-FDT, especially the type vs. token intervention and updatelessness.

I'm starting to build a model $(P, G)$ and apply Equation (4) step by step.


**Comparing Dilemmas & Models**

I'm now comparing Standard Newcomb's Problem with the Smoking Lesion Problem to highlight structural differences in $G^F$. I'll calculate the expected utilities for Newcomb's (\$990,000 vs. \$11,000). For the Smoking Lesion problem, I'll demonstrate how uncertainty over preferences leads to two function nodes, each unaffected by $\textsc{Lesion}$ or $\textsc{Cancer}$. I'm also planning to derive the expectation algebra showing smoking yields a net advantage of $p \cdot \$1,000$. I'll also start analyzing observation-dependent dilemmas like the Transparent Newcomb problem.


**Calculating Transparent Newcomb**

I'm now calculating the Transparent Newcomb problem's expected value for both action options. My world model's full state, \underline{G^F}, determines the prediction. Then I'll work through the calculation for $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = a)]$ to determine the ideal action, noting a minor arithmetic error and typo in the source material. I will contrast this to other solutions.


**Addressing Open Questions**

I'm now zeroing in on open problems presented by the source. I'm focusing on the challenges of constructing the subjunctive dependency graph, *G*, and formalizing counterpossibilities within A-FDT. I need to figure out how the idealized logical conditional operator, $\mathtt{true}(\phi)$, from the source can be practically implemented and what assumptions need to be made to operationalize A-FDT in complex scenarios, like XOR Blackmail and Death in Damascus. I'm building a plan to address the challenges, noting where I will draw on my own ideas.


**Developing Operational Models**

I'm now focused on operationalizing A-FDT, especially building the subjunctive dependency graph, *G*. I'm developing a recipe for constructing *G* algorithmically. I will explore using computational and structural-equation techniques for an algorithmic "common-source factoring" to address multi-node and joint behavior predictions. My goal is to determine a practical approach that can be used in unfamiliar decision problems. This is an extension of the source ideas.


**Formalizing Dependency Resolution**

I'm now formalizing subjunctive dependence through algorithmic templates or structural causal-computational models (SCCMs). I'm treating any environmental mechanism computing the agent's decision output as a noisy channel, and incorporating the fidelity of this mechanism. Physical common causes that don't receive the representation of the decision output will not have an incoming edge. I'm also planning to resolve the value $P$ assigns to fdt when evaluating actions at observations other than x.


**Clarifying Dual Contingencies**

I'm now grappling with the implications of dual-contingent predictors in A-FDT. I'm focusing on scenarios where a predictor's actions depend on *multiple* observations, and examining the impact of independent interventions on each observation node in Equation (4). I'll work through concrete examples to demonstrate how an A-FDT agent solves for off-branch priors via recursive self-evaluation, and identify when a single-node intervention is sufficient compared to a coordinated approach.


**Summarizing Policy Results**

I'm now focusing on a summary of A-FDT's accomplishments. I aim to encapsulate its unification of causal intervention, logical self-reference, and updateless evaluation, highlighting its implications for game theory and artificial intelligence. I will also build a concise reference list of cited works. My goal is to ensure the tone remains rigorous, clear, and mathematically sophisticated. I'll also start checking that the word count and formatting are correct.


**Verifying Quotations**

I'm now methodically verifying all quotes and equations from the source paper, starting with the abstract. I'm paying careful attention to consistent usage of "A-FDT" and "FDT," and I'm also preparing that dedicated section distinguishing source claims from my own interpretations. I'm focusing on ensuring all equations, numbers, and quotes are verbatim.


**Analyzing Epistemic Perspectives**

I'm now integrating insights from several key passages. I'm focusing on the epistemic perspectives in decision theory. I'm especially focused on contrasting the evaluation of actions based on their consequences within a fixed universe versus the hypothetical consequences of alternate decisions. I'm also ready to analyze the application of policy vs. action iterations.


**Comparing Equation Types**

I'm now comparing EDT, CDT, and A-FDT formally, and will use all three key equations. I will contrast the different dependencies each equation captures in a clear way, to show the differences between A-FDT and the policy-based FDT. I'm focusing on the differences in evaluation, and how the distinction is captured by these different formulae.


**Refining Action Representation**

I'm now refining how the mathematical exposition defines the Pearlian do-operator in Section 2, to work mathematically with Structural Causal Models (SCM) or Graphical Models (P, G). I'm carefully presenting the formula for interventions, which includes how CDT applies do(Act = a) and conditions on Obs = x, and will then clarify the nuances. I'll maintain a strict word count to hit the sweet spot of ~2,700 words.


**Distinguishing Interventions**

I'm now clarifying A-FDT's unique intervention approach. I'm focusing on why it doesn't condition on observation *x*, unlike CDT, which conditions on *Obs = x*. I'm thinking through cases like Transparent Newcomb, where conditioning would cause a problematic "double update". Now, I'm working to explicitly distinguish source claims from my ideas in Section 4.


```
