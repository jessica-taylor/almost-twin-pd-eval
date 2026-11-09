# 021_fdt_eq4_google_gemini-4-argon_rhigh_phigh / 00005

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/7e23b669-0283-4957-b94c-f7ed189ec422/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/7e23b669-0283-4957-b94c-f7ed189ec422/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Action Functional Decision Theory (A-FDT): Formal Mechanics, Counterpossibles, and Decision Analysis

For half a century, normative decision theory has been divided between two competing accounts of instrumental rationality: **evidential decision theory (EDT)** and **causal decision theory (CDT)**. When evaluated by expected wealth accumulated across standard decision-theoretic dilemmas, neither theory is uniformly satisfactory. EDT achieves high utility in predictive dilemmas like Newcomb’s problem, where an environmental predictor rewards agents based on forecasts of their choices, but fails in common-cause dilemmas like Skyrms’s smoking lesion problem, where it sacrifices guaranteed utility to "manage the news" (Lewis 1981). Conversely, CDT makes the sensible choice in the smoking lesion problem by isolating the physical causal consequences of an action, yet systematically impoverishes itself in Newcomb’s problem, defects against psychological twins in the prisoner’s dilemma, and perishes in predictive extortion and commitment dilemmas such as Parfit’s hitchhiker and Death in Damascus.

In *"Functional Decision Theory: A New Theory of Instrumental Rationality"* (2017), Eliezer Yudkowsky and Nate Soares propose a framework designed to capture the strengths of both theories without the vulnerabilities of either. Their central thesis is that rational agency should not be framed as choosing an isolated physical movement, nor as selecting the most auspicious piece of evidence, but rather as determining the output of a *fixed mathematical decision function*. While Yudkowsky and Soares note that their broader research program includes policy-selecting variants (Footnotes 7 and 16), the primary formal rule developed and analyzed throughout their paper—Equation (4) in Section 5—intervenes directly on the action output of the decision function for the agent's current observation history. We refer to this theory and formal procedure as **action functional decision theory (A-FDT)**.

This essay provides a self-contained mathematical exposition of **A-FDT**. We examine its philosophical motivation, unpack the formal machinery of Equation (4), demonstrate how A-FDT evaluates canonical dilemmas, and develop concrete operational rules for applying A-FDT to unfamiliar decision problems where the source paper leaves implementation questions open.

---

## 1. Philosophical Motivation: From Action Tokens to Function Types

To see why CDT and EDT falter, consider the **Psychological Twin Prisoner’s Dilemma** (Dilemma 1 in Yudkowsky and Soares 2017). An agent and her psychological twin are placed in separate rooms without communication. Each must choose to $\Val{cooperate}$ or $\Val{defect}$. Mutual cooperation yields $\$1,000,000$ each; mutual defection yields $\$1,000$ each; unilateral defection pays $\$1,001,000$ to the defector and $\$0$ to the cooperator. Both know they execute the exact same reasoning process.

A CDT agent reasons that because the rooms are causally isolated, her physical choice cannot causally affect her twin’s choice. Holding the twin's action fixed, defection pays an extra $\$1,000$ in either state of the world. Both CDT twins therefore defect and walk away with $\$1,000$. By contrast, an **A-FDT** agent recognizes that she and her twin are physical instantiations of the same mathematical decision function. As Yudkowsky and Soares put it, the normative principle is to treat one’s decision as the output of a fixed mathematical function that answers the question: *"Which output of this very function would yield the best outcome?"* If that function outputs $\Val{cooperate}$, both twins cooperate and the agent receives $\$1,000,000$; if it outputs $\Val{defect}$, both defect and she receives $\$1,000$. The A-FDT agent therefore outputs $\Val{cooperate}$.

As Lewis (1979) proved, the twin prisoner's dilemma is decision-theoretically isomorphic to **Newcomb’s Problem** (Nozick 1969), in which an agent chooses between taking only an opaque Box B ($\Val{onebox}$) or taking both Box B and a transparent Box A containing $\$1,000$ ($\Val{twobox}$). Yesterday, a predictor with $99\%$ accuracy placed $\$1,000,000$ in Box B if and only if she predicted the agent would leave Box A behind. Under A-FDT, the predictor’s simulation of the agent is treated just like a psychological twin: both the predictor's model and the agent's brain are computing the output of the same decision function.

### Subjunctive Dependence and Counterpossibles

Why does A-FDT link the agent's choice to the predictor's forecast in Newcomb's problem, yet sever the link between smoking and lung cancer in the **Smoking Lesion Problem** (Skyrms 1980)? In the smoking lesion problem, an unobserved arterial lesion causes both a desire to smoke (worth $\$1,000$ in pleasure) and a $99\%$ chance of fatal lung cancer (whereas those without the lesion have only a $1\%$ chance of cancer; survival is worth $\$1,000,000$). Smoking does not cause cancer, nor does the lesion simulate the agent's decision algorithm.

Yudkowsky and Soares distinguish these structures via **subjunctive dependence**:

> *"When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function."* (Section 3)

Just as two well-functioning calculators in Paris and Tokyo computing $6288 + 1048$ have outputs that subjunctively depend on the mathematical value of that sum, the agent's physical act and the predictor's yesterday forecast both subjunctively depend on the output of the agent's decision algorithm. Causal dependence is a special case of subjunctive dependence (if a scribe writes down the Parisian calculator's output, her notes causally and subjunctively depend on the calculation), whereas bare statistical correlation (e.g., both calculators happening to be painted pink, or a lesion causing both a preference for smoking and lung cancer) is not. Using Peirce’s (1934) type-token distinction, CDT intervenes only on the physical *token* ("my action at this spacetime location is $a$"), whereas A-FDT intervenes on the mathematical *type* ("the output of my decision function on this input is $a$"). As the authors summarize the parallel:

> *"Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."* (Section 3)

Because a deterministic mathematical function $f$ applied to a fixed input $z$ takes on its actual value $f(z) = a^*$ of logical necessity, asking what would happen if $f(z) = a'$ (for $a' \neq a^*$) requires evaluating a **counterpossible**—a counterfactual conditional with a logically impossible antecedent (Cohen 1990). Yudkowsky and Soares note that attempting to dodge counterpossibles by asking *"What if I implemented a different function $f_n \in \mathcal{F}$?"* (which they call $\text{FDT}'$) fails in Newcomb’s problem: the predictor predicts the agent’s actual meta-procedure $d \notin \mathcal{F}$, so preserving the predictor’s accuracy still requires imagining that predictors of $d$ forecast as if $d$ behaved like $f_n$. A-FDT therefore embraces counterpossible variation of the function's output directly.

---

## 2. The Formal Architecture of A-FDT

Following Gibbard and Harper (1978) and Joyce (1999), EDT, CDT, and A-FDT all share a common expected-utility backbone. Let $\mathcal{A}$ be a finite set of available actions, $\mathcal{O} = \{o_1, o_2, \dots\}$ a countable set of outcomes, $\mathcal{X}$ a countable set of possible observation histories, and $\Util: \mathcal{O} \to \mathbb{R}$ a bounded utility function. Equation (1) of the paper defines the expected utility of an action $a \in \mathcal{A}$ after observing $x \in \mathcal{X}$ as:

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \then o_j ;\, \obs) \cdot \Util(o_j) \tag{1}$$

where $P(a \then o_j ;\, \obs)$ denotes the probability of outcome $o_j$ in the decision-theoretic hypothetical $\Cfor{a}$ constructed for action $a$ given observation history $\obs$. As Joyce (1999) observes, *"decision theories should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated."* That disagreement is encoded entirely in how each theory defines the hypothetical connective $\then$.

Let $\Outcome$, $\Obs$, and $\Act$ be random variables taking values in $\mathcal{O}$, $\mathcal{X}$, and $\mathcal{A}$ respectively, let $\VV \coloneqq \Util(\Outcome)$ denote the random variable for utility, and let $\EE$ denote expectation with respect to the agent's probability distribution $P$.

1. **Evidential Decision Theory (EDT)** (Equation 2) constructs hypotheticals via standard Bayesian conditioning on both the observation $\Obs = \obs$ and the physical act $\Act = \act$:
   $$\EDT(P, \obs) \coloneqq \argmax_{\act \in \mathcal A} \EE\left(\VV \mid \Obs=\obs, \Act=\act\right) \tag{2}$$

2. **Causal Decision Theory (CDT)** (Equation 3) augments $P$ with a directed acyclic causal graph $G$ (Pearl 1996, 2000). It conditions on $\Obs = \obs$, but evaluates the physical action via Pearl’s surgical intervention operator $\Do(\Act = \act)$, which severs incoming arrows into $\Act$, fixes $\Act = \act$, and propagates changes solely to nodes causally downstream of $\Act$:
   $$\CDT(P, G, \obs) \coloneqq \argmax_{\act \in \mathcal A} \EE\left(\VV \cond \Do(\Act=\act), \Obs=\obs\right) \tag{3}$$

3. **Action Functional Decision Theory (A-FDT)** (Equation 4) ideally seeks an operator $\True(\phi)$ capable of updating $P$ on counterpossible logical claims $\phi$, such as $\FDTvar(\underline{P}, \underline{x}) = \act$. Because no general mathematical theory of $\True(\phi)$ yet exists, Yudkowsky and Soares represent subjunctive dependencies—logical, mathematical, computational, and causal—within an extended dependency graph $G$. Applying Pearl’s $\Do$ operator to the node representing the output of the decision algorithm itself yields the primary formal definition of **A-FDT** (Equation 4 in Section 5 of the paper, where the procedure is denoted $\FDT$):

   $$\FDT(P, G, \obs) \coloneqq \argmax_{\act \in \mathcal A} \EE\left(\VV \cond \Do\left(\FDTvar(\underline P,\underline G,\underline x)= \act\right)\right) \tag{4}$$

### Unpacking Equation (4): Self-Reference, Dequoting, and Updatelessness

To apply Equation (4) accurately, three formal features require close attention:

* **Logical Variables and Dequoting ($\underline{P}, \underline{G}, \underline{x}$):** In an A-FDT world-model $(P, G)$, the sample space of $P$ and the node set of $G$ include variables representing the outputs of mathematical functions (for instance, a node for $6288+1048$). Underlines denote *dequoting*: if a variable $x$ has value $3$, then $\Var{Z}\underline{x}$ refers to the syntactically named variable $\Var{Z}3$. Thus, when the agent has world-model $(P, G)$ and observation history $x$, $\FDTvar(\underline{P}, \underline{G}, \underline{x})$ is the specific node in $G$ representing the logical output that the A-FDT algorithm returns when evaluated on inputs $(P, G, x)$.
* **Harmless Self-Reference via Quining:** Because $\FDTvar(\underline{P}, \underline{G}, \underline{x})$ is a node inside $G$, the graph $G$ appears to refer to its own syntactic description $\underline{G}$. Yudkowsky and Soares note that this self-reference is mathematically benign: the agent does not need to know the *output value* of $\FDT(P, G, x)$ in advance in order to include a *variable symbol* representing that output in $G$, and Kleene’s (1938) second recursion theorem guarantees via "quining" that formal data structures can contain and manipulate exact syntactic representations of themselves.
* **The Updateless Mechanism for Observations:** Comparing Equation (3) for CDT and Equation (4) for A-FDT reveals *two* structural differences, not just one:
  1. *Target of intervention:* CDT intervenes on the physical node $\Act$, whereas A-FDT intervenes on the logical node $\FDTvar(\underline{P}, \underline{G}, \underline{x})$.
  2. *Handling of observations $\obs$:* CDT conditions its probability distribution on $\Obs = \obs$. **A-FDT does not condition $P$ on $\Obs = \obs$ inside the expectation.** Instead, when an A-FDT agent observes $\obs$, she uses $\obs$ to select *which logical variable* $\FDTvar(\underline{P}, \underline{G}, \underline{x})$ to intervene upon, while taking the expectation over the prior distribution $P$ (an "updateless" evaluation borrowed from Dai 2009). Why? Because if an external predictor predicts what the agent will do *upon observing $\obs$*, the very fact that the agent observed $\obs$ rather than some $y \neq \obs$ may subjunctively depend on the output of $\FDTvar(\underline{P}, \underline{G}, \underline{x})$! Conditioning on $\Obs = \obs$ would freeze the past observation and blind the agent to how her conditional disposition determines whether she encounters $\obs$ in the first place. (As noted in the paper's draft comment in Section 9, Yudkowsky's 2010 "Timeless Decision Theory" both intervened on the logical node *and* conditioned on $\Obs = \obs$, producing a harmful "double update" that A-FDT avoids.)

Finally, Equation (4) immediately implies an equivalence theorem: whenever $(P, G)$ is a simple environment in which all correlations between $\Act$ and utility-relevant variables are causally downstream of $\Act$ (with $\Act$ depending on $\FDTvar(\underline{P}, \underline{G}, \underline{x})$), we have:
$$\EE[\VV \mid \act] = \EE[\VV \mid \Do(\Act=\act)] = \EE[\VV \mid \Do(\FDTvar(\underline{P}, \underline{G}, \underline{x})=\act)]$$
so EDT, CDT, and A-FDT prescribe the exact same action. They diverge precisely when $\Act$ correlates with non-downstream events.

---

## 3. Applying A-FDT to Canonical Decision Problems

Following Section 6 of Yudkowsky and Soares (2017), let us trace how three idealized agents—**Eve** (following EDT, Eq. 2), **Carl** (following CDT, Eq. 3), and **Fiona** (following **A-FDT**, Eq. 4)—evaluate three structural classes of dilemmas.

### Case 1: Unobserved Predictor (Standard Newcomb’s Problem)

In Newcomb’s problem ($\mathcal{X} = \{\emptyset\}$, so we omit $\obs$), Box A contains $\$1,000$ and Box B is either $\Val{full}$ ($\$1,000,000$) or $\Val{empty}$ ($\$0$). The predictor’s accuracy variable $\Var{Accurate}$ takes value $\Val{accurate}$ with probability $0.99$ and $\Val{inaccurate}$ with probability $0.01$.

In Fiona’s A-FDT model $(\Pf, \Gf)$, the root node of intervention is $\FDTpg$, which has directed arrows to both $\Act$ and $\Var{Prediction}$:
$$\Gf: \quad \FDTpg \longrightarrow \Act \longrightarrow \VV \longleftarrow \Var{Box B} \longleftarrow \Var{Prediction} \longleftarrow \FDTpg, \quad \Var{Accurate} \longrightarrow \Var{Prediction}$$
Specifically, $\Act = \FDTpg$, while $\Var{Box B} = \Val{full}$ if and only if $(\FDTpg = \Val{onebox} \land \Var{Accurate} = \Val{accurate})$ or $(\FDTpg = \Val{twobox} \land \Var{Accurate} = \Val{inaccurate})$.

Fiona applies Equation (4) by computing two interventional expectations:
* **Hypothetical 1 ($\Do(\FDTpg = \Val{onebox})$):** This sets $\Act = \Val{onebox}$ with probability $1$ and $\Var{Box B} = \Val{full}$ with probability $0.99$. Thus:
  $$\EE\left(\VV \cond \Do(\FDTpg = \Val{onebox})\right) = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000.$$
* **Hypothetical 2 ($\Do(\FDTpg = \Val{twobox})$):** This sets $\Act = \Val{twobox}$ with probability $1$ and $\Var{Box B} = \Val{full}$ with probability $0.01$. Thus:
  $$\EE\left(\VV \cond \Do(\FDTpg = \Val{twobox})\right) = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$

Since $\$990,000 > \$11,000$, Equation (4) yields $\FDT(\Pf, \Gf) = \Val{onebox}$. Unlike Eve (whose EDT prescription breaks down if her prior $\Pe(\Act=\Val{onebox})$ equals $0$ or $1$), Fiona’s A-FDT calculation is completely invariant to her prior probability $\Pf(\FDTpg = \Val{onebox})$. Even when Fiona reflects and becomes virtually certain that $\FDT(\Pf, \Gf) = \Val{onebox}$ and therefore that Box B is already full, she does not switch to two-boxing: under Equation (4), evaluating $\Val{twobox}$ requires intervening on $\FDTpg = \Val{twobox}$, which counterpossibly shifts $\Var{Prediction}$ and empties Box B in her hypothetical.

This also resolves the **dominance** debate. CDT claims two-boxing dominates one-boxing because CDT holds $\Var{Box B}$ fixed while varying $\Act$. As Yudkowsky and Soares point out, every decision theory defines its own dominance relation relative to the invariants of its hypotheticals. Under **A-FDT dominance**—which holds fixed the subjunctive relationship $\Var{Accurate}$ between the predictor and the function $\FDTpg$—one-boxing strictly dominates two-boxing in expectations across the relevant structural states.

### Case 2: Common Cause and Preference Uncertainty (The Smoking Lesion Problem)

In the smoking lesion problem, Gibbard and Harper (1978) observed that if one replaces $\Var{Predisposition}$ with $\Var{Lesion}$, $\Var{Accurate}$ with $\Var{Luck}$, and $\Var{Box B}$ with $\Var{Death}$ ($\Val{alive} = \$1,000,000$, $\Val{dead} = \$0$, $\Val{smoke} = +\$1,000$), the statistical distribution $P$ is identical to Newcomb’s problem. Consequently, Eve (EDT) refrains from smoking, whereas Carl (CDT) smokes.

How does Fiona (**A-FDT**) avoid Eve’s error? In the problem setup, the lesion causes the agent to enjoy smoking, whereas lacking the lesion makes smoking unpleasant. Yudkowsky and Soares formalize this by introducing two utility functions: $\Util_S$ (which values smoking at $+\$1,000$) and $\Util_R$ (which values smoking at $-\$1$), corresponding to two probability distributions $\Pf_S$ and $\Pf_R$. Because Fiona cannot directly introspect whether she has the lesion, she does not know whether she is physicalizing $\FDT(\Pf_S, \Gf)$ or $\FDT(\Pf_R, \Gf)$.

In her subjunctive graph $\Gf$ (Figure 4 in the paper), $\Var{Lesion}$ has an arrow to $\Var{Cancer} \to \Var{Death} \to \VV$, and $\Act$ is a deterministic multiplexer of $\Var{Lesion}$ and the two logical nodes $\FDTvar(\underline{\Pf_S}, \underline{\Gf})$ and $\FDTvar(\underline{\Pf_R}, \underline{\Gf})$:
$$\Act(\Val{lesion}, s, r) \coloneqq s, \qquad \Act(\Val{nolesion}, s, r) \coloneqq r.$$
Crucially, there is *no* arrow from $\FDTvar(\underline{\Pf_S}, \underline{\Gf})$ to $\Var{Lesion}$ or $\Var{Cancer}$: a biological lesion does not simulate A-FDT.

Suppose Fiona actually has the lesion, so her decision procedure is evaluating $\FDT(\Pf_S, \Gf)$. Let $\Pf_S(\Val{lesion}) = p \in (0, 1)$, and let $\Pf_S(\FDTvar(\underline{\Pf_R}, \underline{\Gf}) = \Val{smoke}) = q \in [0, 1]$. When she applies Equation (4), she intervenes on $\FDTvar(\underline{\Pf_S}, \underline{\Gf})$:
* Under $\Do(\FDTvar(\underline{\Pf_S}, \underline{\Gf}) = \Val{smoke})$, the probability of $\Val{lesion}$ remains $p$. If $\Var{Lesion} = \Val{lesion}$ (prob $p$), she smokes ($+\$1,000$) and survives with probability $0.01$ (expected survival value $\$10,000$). If $\Var{Lesion} = \Val{nolesion}$ (prob $1-p$), her action is controlled by $\FDTvar(\underline{\Pf_R}, \underline{\Gf})$ instead, yielding $\$990,000 + q(\$1,000)$. Thus:
  $$\EE\left(\VV \cond \Do(\FDTvar(\underline{\Pf_S}, \underline{\Gf}) = \Val{smoke})\right) = p(\$10,000 + \$1,000) + (1-p)(\$990,000 + q \cdot \$1,000).$$
* Under $\Do(\FDTvar(\underline{\Pf_S}, \underline{\Gf}) = \Val{refrain})$, the $(1-p)$ branch is completely unchanged, while the $p$ branch loses the $\$1,000$ smoking payoff:
  $$\EE\left(\VV \cond \Do(\FDTvar(\underline{\Pf_S}, \underline{\Gf}) = \Val{refrain})\right) = p(\$10,000) + (1-p)(\$990,000 + q \cdot \$1,000).$$

Subtracting the two expectations reveals that $\Val{smoke}$ exceeds $\Val{refrain}$ by exactly $p \cdot \$1,000 > 0$. Fiona smokes! (And in the **XOR Blackmail Problem**—Dilemma 6, where a predictor sends a letter iff [no termites $\land$ agent pays $\$1,000$] or [termites $\land$ agent refuses]—Fiona refuses to pay without needing preference uncertainty, because intervening on $\FDTvar(\underline{\Pf}, \underline{\Gf}, \Val{letter})$ alters whether the letter is sent but has no path to $\Var{Infestation}$.)

### Case 3: Endogenous Observations (Transparent Newcomb, Parfit’s Hitchhiker, and Mechanical Blackmail)

The full power of Equation (4)’s updateless observation mechanism emerges when the agent’s observation $\obs$ itself depends on the predictor’s forecast. Consider the **Transparent Newcomb Problem** (Drescher 2006; Dilemma 4 in the paper), which is structurally identical to **Parfit’s Hitchhiker Problem** (Dilemma 3) and the **Mechanical Blackmail Problem** (Dilemma 8). Both boxes are now transparent ($\Obs \in \{\Val{full}, \Val{empty}\}$). The predictor places $\$1,000,000$ in Box B (Accuracy $= 0.99$) if and only if she predicts that *upon observing $\Obs = \Val{full}$*, the agent will leave Box A behind ($\Val{onebox}$).

Suppose Eve, Carl, and Fiona walk into the room and observe $\Obs = \Val{full}$.
* Both **Carl (CDT)** and **Eve (EDT)** condition on $\Obs = \Val{full}$ in Equations (2) and (3). Once $\Obs = \Val{full}$ is conditioned upon, $\Var{Box B} = \Val{full}$ is locked at probability $1$. Both compute $\$1,001,000$ for $\Val{twobox}$ and $\$1,000,000$ for $\Val{onebox}$, so both two-box. Foreseeing this, the predictor leaves Box B empty for CDT and EDT agents (and in Parfit’s Hitchhiker, leaves them in the desert to die).
* **Fiona (A-FDT)** does not condition $\Pf$ on $\Obs = \Val{full}$. Instead, observing $\Obs = \Val{full}$ causes her to evaluate Equation (4) at the node $\FDTpgv{full}$. In her graph $\Gf$ (Figure 5b in the paper), $\Var{Prediction}$ depends on $\FDTpgv{full}$ and $\Var{Accurate}$, while $\Act$ depends on $\FDTpgv{full}$ (if $\Var{Box B} = \Val{full}$) and on the off-path node $\FDTpgv{empty}$ (if $\Var{Box B} = \Val{empty}$):
  $$\Act = \begin{cases} \FDTpgv{full} & \text{if } \Var{Box B} = \Val{full} \\ \FDTpgv{empty} & \text{if } \Var{Box B} = \Val{empty}. \end{cases}$$

*(Textual note on the source paper: In Section 6 of Yudkowsky and Soares 2017, an unnumbered display equation under "Transparent Newcomb Problem" contains a typographical slip, writing $\EE(\VV \mid \Do(\FDTpgv{full}=\act, \Obs=\Val{full})$. As confirmed by Equation (4), Footnote 16, Section 9, and the authors' immediately following arithmetic, $\Obs=\Val{full}$ is **not** conditioned upon; conditioning on it would force $\Prob(\Var{Box B}=\Val{full})=1$ and contradict their derived formula.)*

Let $q \coloneqq \Pf(\FDTpgv{empty} = \Val{twobox})$ be Fiona's prior probability that she two-boxes if she sees an empty box. Evaluating Equation (4) for $\obs = \Val{full}$:
* **If $\Do(\FDTpgv{full} = \Val{onebox})$:** With probability $0.99$ ($\Var{Accurate}=\Val{accurate}$), the predictor predicts $\Val{1}$, fills Box B, Fiona sees $\Val{full}$, executes $\Val{onebox}$, and gets $\$1,000,000$. With probability $0.01$ ($\Var{Accurate}=\Val{inaccurate}$), the predictor leaves Box B empty, Fiona sees $\Val{empty}$, and her action is governed by $\FDTpgv{empty}$, getting $q \cdot \$1,000$. Thus:
  $$\EE\left(\VV \cond \Do(\FDTpgv{full} = \Val{onebox})\right) = 0.99(\$1,000,000) + 0.01(q \cdot \$1,000) = \$990,000 + \$10q.$$
* **If $\Do(\FDTpgv{full} = \Val{twobox})$:** With probability $0.01$ ($\Var{Accurate}=\Val{inaccurate}$), the predictor mistakenly fills Box B, Fiona sees $\Val{full}$, executes $\Val{twobox}$, and gets $\$1,001,000$. With probability $0.99$ ($\Var{Accurate}=\Val{accurate}$), the predictor foresees her two-boxing, leaves Box B empty, Fiona sees $\Val{empty}$, and $\FDTpgv{empty}$ yields $q \cdot \$1,000$. Thus:
  $$\EE\left(\VV \cond \Do(\FDTpgv{full} = \Val{twobox})\right) = 0.01(\$1,001,000) + 0.99(q \cdot \$1,000) = \$10,010 + \$990q.$$
  *(Note: the source paper prints $\$110,00$ for $0.01 \times \$1,001,000$, a minor arithmetic typo for $\$10,010$; either way, the inequality is overwhelming.)*

For any $q \in [0, 1]$, $\$990,000 + \$10q > \$10,010 + \$990q$. Thus $\FDT(\Pf, \Gf, \Val{full}) = \Val{onebox}$. Even while staring directly at $\$1,000,000$ in a transparent Box B, Fiona leaves the $\$1,000$ behind—because in her A-FDT counterfactual, had $\FDTpgv{full}$ output $\Val{twobox}$, she would almost certainly be staring at an empty box instead.

---

## 4. Open Questions and Operationalizing A-FDT for Unfamiliar Cases

While Yudkowsky and Soares (2017) establish how Equation (4) operates once $(P, G)$ is given, they leave three foundational questions open:
1. **Constructing the Subjunctive Dependency Graph $G$:** Pearl (2000) provides an empirical calculus for discovering causal graphs, but as the authors admit in Section 5, *"no such formal treatment has yet been given to the problem of deducing the structure of other kinds of subjunctive dependence."*
2. **Specifying Off-Path Decision Variables:** In the Smoking Lesion and Transparent Newcomb calculations, Fiona’s equations contain a free parameter $q$ representing her prior belief about an unvisited decision node ($\FDTvar(\underline{\Pf_R}, \underline{\Gf})$ or $\FDTpgv{empty}$). In those two dilemmas, $q$ canceled out or was bounded too tightly to flip the inequality. What happens in an unfamiliar problem where the optimal choice at observation $\obs$ *does* depend on the exact value of $q$ at an off-path node $\obs'$?
3. **Action-Level (A-FDT) vs. Policy-Level Intervention:** In Footnotes 7 and 16, the authors remark that while Equation (4) intervenes on the action output $\FDTvar(\underline{P}, \underline{G}, \underline{x}) = \act$ for a single observation $\obs$, their preferred variant intervenes on a whole *policy* $\pi: \mathcal{X} \to \mathcal{A}$ at once, adding that *"The difference only matters in multi-agent dilemmas so far as we can tell."*

To enable a practitioner to apply **A-FDT** systematically to unfamiliar problems, we now distinguish what follows strictly from the source text from **our own operational proposals**, developing a concrete procedure that resolves these ambiguities.

### Proposal 1: A Four-Step Protocol for Constructing $G$ and Evaluating A-FDT

While a general philosophical theory of counterpossibles remains open, in applied decision theory and game theory we know the structural specification of the dilemma. We propose the following **Operational A-FDT Modeling Protocol** (an extension beyond the source text that systematizes the paper's examples):

1. **Index the Decision-Function Nodes by Epistemic State:** Identify every distinct epistemic/observational state $(P_k, x) \in \mathcal{M} \times \mathcal{X}$ the agent might occupy in the dilemma. For each such pair, instantiate a distinct logical root node $D_{k, x} \coloneqq \FDTvar(\underline{P_k}, \underline{G}, \underline{x})$ in $G$ with state space $\mathcal{A}$.
2. **Factor the Physical Action Node $\Act$ as a Multiplexer:** Set $\Act$ to be a deterministic function of the actual realized epistemic state $(K, \Obs)$ and the family of logical nodes $\{D_{k, x}\}$:
   $$\Act = \sum_{k, x} \mathbf{1}_{(K=k, \Obs=x)} \cdot D_{k, x}$$
   (plus any physical noise variable, such as a cosmic ray or trembling hand, if execution is non-deterministic).
3. **Draw Subjunctive Edges Only to Algorithmic Replicas and Simulators:** For each external entity or state variable $Y$ in the environment (lesions, weather, predictors, twins, blackmailers):
   * Draw a directed edge $D_{k, x} \to Y$ **if and only if** the mechanism generating $Y$ either (a) is causally downstream of $\Act$ (handled via $\Act \to Y$), or (b) explicitly computes, simulates, or replicates the output of the agent's decision procedure in state $(P_k, x)$.
   * If $Y$ merely correlates with the agent's preferences, hardware, or action via a prior physical cause $C$ without simulating the decision procedure $D_{k, x}$ (like the arterial lesion), draw $C \to K$ and $C \to Y$, leaving $D_{k, x}$ with **no outgoing edge** to $C$ or $Y$.
4. **Resolve Off-Path Priors $q$ via Recursive Self-Evaluation:** In the source paper, Yudkowsky and Soares treat the prior probability $q$ on an unvisited node $D_{k', x'}$ as an arbitrary parameter (merely parenthetically noting in Transparent Newcomb that *"The correct value of $q$ is 1, as you may verify"*). For unfamiliar problems where the optimal choice at $D_{k, x}$ depends on the value of $D_{k', x'}$, we propose **Recursive A-FDT Closure**: when $D_{k', x'}$ does not subjunctively affect the transition to $(k, x)$, the agent computes $a^*_{k', x'} = \FDT(P_{k'}, G, x')$ using Equation (4) and sets the point-mass distribution $P(D_{k', x'} = a^*_{k', x'}) = 1$. If $D_{k, x}$ and $D_{k', x'}$ are mutually interdependent, $(q_{k, x}, q_{k', x'})$ must be solved as a Nash/ratified fixed point of Equation (4) across the nodes, or else compared against policy-functional decision theory (P-FDT), as we now illustrate.

### Proposal 2: Testing the Boundary Between A-FDT and Policy-FDT in an Unfamiliar Case

Footnotes 7 and 16 state that A-FDT (Equation 4) and policy-based FDT (which we will call **P-FDT**, intervening on the entire policy $\pi: \mathcal{X} \to \mathcal{A}$ via $\Do(\Var{pfdt}(\underline{P}, \underline{G}) = \pi)$) only differ in certain multi-agent dilemmas. Using our operational framework, we can construct an unfamiliar *single-agent* predictive dilemma showing exactly when and why Equation (4)'s node-by-node intervention diverges from P-FDT.

> **Unfamiliar Case: The Dual-Scenario Predictor (An Operational Test Case).**
> Suppose a predictor is deciding whether to award an agent a $\$1,000,000$ grant. Before the grant is awarded, a fair coin $\Var{Coin} \in \{\Val{heads}, \Val{tails}\}$ is flipped and shown to the agent ($\Obs \in \{\Val{heads}, \Val{tails}\}$). In either observation state, the agent must choose whether to $\Val{work}$ (costing $-\$1,000$ in effort) or $\Val{shirk}$ ($\$0$). The predictor is an infallible simulator who awards the $\$1,000,000$ grant (regardless of the coin flip) **if and only if** she predicts that the agent would $\Val{work}$ upon observing $\Val{heads}$ **and** would also $\Val{work}$ upon observing $\Val{tails}$.

Let us apply **A-FDT (Equation 4)** when the agent observes $\Obs = \Val{heads}$.
By our operational protocol, the graph $G$ has two logical decision nodes: $D_H \coloneqq \FDTvar(\underline{P}, \underline{G}, \Val{heads})$ and $D_T \coloneqq \FDTvar(\underline{P}, \underline{G}, \Val{tails})$.
The predictor’s grant variable is $\Var{Grant} = \mathbf{1}_{(D_H = \Val{work} \,\land\, D_T = \Val{work})}$, worth $\$1,000,000$.
The agent's physical action is $\Act = D_H$ if $\Var{Coin} = \Val{heads}$ (prob $0.5$) and $\Act = D_T$ if $\Var{Coin} = \Val{tails}$ (prob $0.5$).

When the agent observes $\Obs = \Val{heads}$, A-FDT (Equation 4) intervenes **only** on $D_H$, holding the marginal distribution of the separate root node $D_T$ fixed at its prior probability $q \coloneqq P(D_T = \Val{work})$:
* **Under $\Do(D_H = \Val{work})$:** The grant is awarded iff $D_T = \Val{work}$ (prob $q$). The agent works on $\Val{heads}$ (prob $0.5$, cost $-\$1,000$) and works on $\Val{tails}$ with prob $0.5q$ (cost $-\$1,000$). Expected utility:
  $$\EE\left(\VV \cond \Do(D_H = \Val{work})\right) = q(\$1,000,000) - 0.5(\$1,000) - 0.5q(\$1,000) = \$999,500q - \$500.$$
* **Under $\Do(D_H = \Val{shirk})$:** Because $D_H = \Val{shirk}$, the conjunction $(D_H = \Val{work} \land D_T = \Val{work})$ is false, so $\Var{Grant} = 0$ with certainty. The agent shirks on $\Val{heads}$ (cost $\$0$) and works on $\Val{tails}$ with prob $0.5q$. Expected utility:
  $$\EE\left(\VV \cond \Do(D_H = \Val{shirk})\right) = 0 - 0 - 0.5q(\$1,000) = -\$500q.$$

Comparing the two under **A-FDT**:
$$\EE[\VV \mid \Do(D_H = \Val{work})] - \EE[\VV \mid \Do(D_H = \Val{shirk})] = \$1,000,000q - \$500.$$
Notice what this reveals about **A-FDT**:
1. If $q > 0.0005$, A-FDT uniquely prescribes $\Val{work}$ on $\Val{heads}$ (and by symmetry, $\Val{work}$ on $\Val{tails}$), achieving the $\$999,000$ net payoff.
2. However, because A-FDT treats $D_H$ and $D_T$ as separate root variables in $G$ (just as a multi-agent coordination game has separate players), if the agent initially believes $q = 0$ (she expects her $\Val{tails}$-self to shirk), then intervening solely on $D_H = \Val{work}$ yields $-\$500 < \$0$, trapping A-FDT in a mutual-shirking coordination failure across her own observation branches!
3. How can an A-FDT agent avoid this trap without switching to full **P-FDT**? If we supplement Equation (4) with an *algorithmic symmetry edge* in $G$ recognizing that $D_H$ and $D_T$ are symmetric calls to the same algorithm (just as A-FDT links two symmetric voters in the 10-voter coalition game in Section 10 of the paper), or if we move to **P-FDT** and intervene on the global policy $\pi = (a_H, a_T) \in \mathcal{A}^{\mathcal{X}}$, the agent evaluates $\Do(\pi = (\Val{work}, \Val{work}))$ ($+\$999,000$) directly against $\Do(\pi = (\Val{shirk}, \Val{shirk}))$ ($\$0$) and unconditionally works.

This analysis sharpens Footnotes 7 and 16 of Yudkowsky and Soares (2017): in **A-FDT**, because each observation history $\obs$ defines a distinct intervention node $\FDTvar(\underline{P}, \underline{G}, \underline{x})$, cross-observation coordination by a single agent is mathematically isomorphic to multi-agent coordination.

---

## 5. Conclusion

**Action functional decision theory (A-FDT)**, as formalized in Equation (4) of Yudkowsky and Soares (2017), achieves a remarkable synthesis in the foundations of rational choice. By shifting the locus of intervention from the physical action token $\Act$ to the logical function output $\FDTvar(\underline{P}, \underline{G}, \underline{x})$, and by responding to observations $\obs$ updatelessly—selecting which logical node to intervene upon rather than conditioning away the past—A-FDT one-boxes in Newcomb’s problem, smokes in the smoking lesion problem, cooperates with psychological twins, and resists blackmail and desert abandonment in Parfit’s hitchhiker. While deep philosophical questions remain regarding how to deduce subjunctive dependency graphs from first principles and how to formalize counterpossible conditionals, the operational framework developed here shows that A-FDT already provides a rigorous, mathematically transparent calculus for analyzing strategic interdependence.

---

## References

* Cohen, Daniel (1990). "On What Cannot Be." In *Truth or Consequences: Essays in Honor of Nuel Belnap*, 123–132. Kluwer Academic Publishers.
* Dai, Wei (2009). "Towards a New Decision Theory." *Less Wrong*.
* Drescher, Gary L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Gibbard, Allan, and William L. Harper (1978). "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, Vol. 1, 125–162. D. Reidel.
* Joyce, James M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Kleene, Stephen Cole (1938). "On Notation for Ordinal Numbers." *Journal of Symbolic Logic* 3(4): 150–155.
* Lewis, David (1979). "Prisoners' Dilemma is a Newcomb Problem." *Philosophy & Public Affairs* 8(3): 235–240.
* Lewis, David (1981). "Causal Decision Theory." *Australasian Journal of Philosophy* 59(1): 5–30.
* Nozick, Robert (1969). "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel*, 114–146. D. Reidel.
* Parfit, Derek (1986). *Reasons and Persons*. Oxford University Press.
* Pearl, Judea (1996). "Causation, Action, and Counterfactuals." In *Proceedings of the 6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-96)*, 51–73.
* Pearl, Judea (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Peirce, Charles Sanders (1934). *Collected Papers of Charles Sanders Peirce, Vol. V: Pragmatism and Pragmaticism*. Harvard University Press.
* Skyrms, Brian (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Yudkowsky, Eliezer (2010). *Timeless Decision Theory*. The Singularity Institute.
* Yudkowsky, Eliezer, and Nate Soares (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. Machine Intelligence Research Institute, arXiv:1710.05060v2.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Approach**

I'm now focusing on defining the approach. My aim is a mathematical essay or technical blog post about action functional decision theory (A-FDT). I'm drawing on the provided Yudkowsky and Soares reference to understand the core concepts. The main challenge is finding the right balance between mathematical rigor and accessibility for the intended audience. I'm exploring different organizational structures to ensure clarity.


**Clarifying Core Concepts**

I'm now zeroing in on the core concepts of A-FDT, intending to present it clearly for a mathematically-inclined audience. I'm focusing on Equation (4) from the paper as the central formal expression. A-FDT is the name I am using for the theory, and I will be precise in my use of terminology. The goal is a detailed account that's precise enough to aid in making unfamiliar decisions. I'm actively working on how A-FDT evaluates actions, dependencies, and counterfactuals.


**Formalizing Intervention Strategy**

I'm now diving into formalizing the intervention strategies, especially the action vs. policy intervention distinction, as flagged in the footnotes of the source. I'm focusing on the subjunctive dependency graphs, and the $\True$ operator. I'm working to formalize notions of "fairness" where operational interpretations exist. I am also working to ensure that any quotations will be faithful to the source and keeping the format and length constraints in mind. I aim for a concise, mathematically grounded exposition.


**Analyzing the Formalism**

I am now focusing on the formal components, specifically Equation (4) from the source. My presentation will define A-FDT precisely, carefully distinguishing it from the policy formulation. I will ensure faithful representation of the equation from the paper and will introduce my standardized notation alongside it, for clarity. I'm reviewing the key components and philosophical motivations to ensure a rigorous foundation.


**Contrasting Decision Frameworks**

I'm currently contrasting Causal Decision Theory (CDT) with Evidential Decision Theory (EDT). I see how they behave in problems like the Smoking Lesion scenario and Newcomb's problem. I'm focusing on why CDT and EDT produce different decisions in various scenarios, including the Psychological Twin Prisoner's Dilemma, and Parfit's Hitchhiker. I'm aiming to clarify the distinctions and limitations of each.


**Differentiating A-FDT**

I am now differentiating A-FDT from CDT and EDT using the formalism, especially Equations 1-4. I'm focusing on the crucial structural differences between CDT and A-FDT, particularly in how they handle counterfactuals and interventions. I'm working to highlight how the ability to vary its output requires evaluating counterpossibles. The goal is to articulate the key distinctions with mathematical precision.


**Distinguishing Logical Nodes**

I'm now focusing on distinguishing the physical intervention ($\Act$) from the logical node ($\FDTvar$). I'm using dequoting and Kleene's recursion theorem to handle self-reference. I'm noting the updateless nature of A-FDT regarding observations; it changes the logical node intervened upon without conditioning on the observation. I will be careful to identify the typo in the source on this distinction.


**Developing Worked Examples**

I'm now focusing on developing worked examples to illustrate A-FDT. I'm actively working on scenarios like the standard Newcomb's Problem, the Twin Prisoner's Dilemma, and the Smoking Lesion Problem, to make the formal concepts tangible. I'm carefully constructing these examples to demonstrate the theory's functionality. The plan is to clarify the subtle variations between CDT, EDT, and A-FDT.


**Operationalizing Graph Construction**

I'm now thinking about how to build the subjunctive dependency graph $G$ operationally, since there's no formal theory for deducing it. I'm focusing on creating an explicit operational procedure, perhaps using syntactic/algorithmic dependency factorization to separate variables. My goal is to outline how to construct the graph in practice for unfamiliar problems.


**Operationalizing Policy Evaluation**

Now, I'm analyzing the divergences of A-FDT from policy-based FDT. I'm focusing on cases requiring operational specifications, particularly scenarios where payoffs depend on off-path values. I'm considering scenarios where the predictor's actions depend jointly on multiple observation states. I'm exploring an operational implementation of A-FDT to handle these, considering recursive evaluation for off-path actions.


**Structuring the Discussion**

I'm now outlining the structure, targeting 2650-2800 words. My introduction will cover CDT, EDT, and A-FDT. I'll dedicate a section to philosophical motivation, discussing the type-token shift, and introducing subjunctive dependence. I'll be clear to keep the distinction between the original and my operational extensions. I'm carefully organizing sections and allocating word counts.


**Refining Logical Interventions**

I'm now zeroing in on the logical intervention aspect of A-FDT and the crucial distinction from physical interventions. I'm carefully unpacking Equation (4) and the symbols within it, including the world-model, observations, and operators. The plan is to clearly highlight A-FDT's updateless nature and how it uses logical interventions rather than Bayesian conditioning.


**Illustrating Practical Applications**

I am now focusing on providing detailed examples to show A-FDT's practical advantages. I'm actively constructing scenarios, including variations of Newcomb's Problem, the Smoking Lesion Problem, and others from the source. The objective is to make the differences between A-FDT and the other decision theories operationally clear with numerical examples. I will explain A-FDT's approach to each of these problems.


**Operationalizing Unfamiliar Cases**

I'm now zeroing in on open problems and operationalizing A-FDT for unfamiliar cases. I'm developing a four-step modeling protocol to construct the subjunctive graph $G$. My focus is on distinguishing the source claims from my operational proposals, particularly in resolving off-path probabilities in A-FDT. I am working on clarifying the implications of this for practical applications.


**Operationalizing Novel Examples**

I'm now expanding to encompass an *Observation-Bottleneck Coordination Game*, via recursive evaluation. I'm aiming to showcase action-level divergence within A-FDT compared to policy intervention, or P-FDT. I'll need to remember to check and note my use of A-FDT and quotes to ensure faithfulness.


**Reflecting on Subjunctive Dependence**

I'm reflecting on the implications of subjunctive dependence within FDT. The connection between FDT and subjunctive dependence resonates. I'm considering how this might change my entire decision process. It's like asking, "What if this had happened differently?" I'll ensure I address this perspective in the essay, including careful word count checks.


**Correcting Calculations and Notation**

I'm now focusing on correcting numerical errors from the source examples, especially in Newcomb's problem and the Smoking Lesion scenario. I aim to ensure accurate arithmetic and clear algebraic expressions. I'll maintain fidelity to the source, even while pointing out errors. I'll introduce my notation to maintain clarity and accuracy.


**Refining Smoking Lesion Examples**

I'm now refining the Smoking Lesion example, and double-checking calculations. It's becoming clearer how A-FDT's predictions differ from the CDT/EDT. I'm focusing on the probabilistic setup, ensuring it's mathematically sound. My goal is to use this numerical example to clarify the impact of A-FDT on the reader.


**Calculating Utility Divergences**

I'm now calculating utility divergences in a Newcomb-like scenario where the predictor is imperfect. I'm carefully evaluating A-FDT's behavior using specific probabilities and payoffs. My goal is to use this specific numerical example to clarify the divergence between the decision models. I'll need to remember to ensure fidelity to all the quotes.


```
