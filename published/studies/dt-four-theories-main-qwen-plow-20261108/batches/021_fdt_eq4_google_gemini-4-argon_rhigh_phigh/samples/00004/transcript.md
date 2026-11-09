# 021_fdt_eq4_google_gemini-4-argon_rhigh_phigh / 00004

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/0ffe0ad5-14d2-4edf-9084-9667cd58e3c8/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/0ffe0ad5-14d2-4edf-9084-9667cd58e3c8/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Action Functional Decision Theory (A-FDT): Formal Mechanics, Subjunctive Counterfactuals, and Operational Application

## 1. Introduction: The Instrumental Impasse

For half a century, normative decision theory has been divided between two competing accounts of instrumental rationality: *evidential decision theory* (EDT) and *causal decision theory* (CDT). Both theories accept the foundational premise of expected utility maximization—that a rational agent should select the option with the highest expected value across hypothetical outcomes—yet they disagree sharply on how to construct the hypothetical worlds used to evaluate an action.

An EDT agent evaluates an action $a$ by asking what that action implies as statistical evidence: *"Which physical act of mine would be the best news to hear I took?"* Formally, EDT equates decision-theoretic hypotheticals with standard Bayesian conditionalization. By contrast, a CDT agent evaluates an action by isolating its downstream physical effects: *"Which physical act of mine causes the best outcome?"* Formally, CDT constructs hypotheticals by performing a causal intervention on the agent's physical act while holding the causal past fixed.

Measured by average utility achieved across classic decision-theoretic dilemmas, neither theory is uniformly satisfactory (Gibbard and Harper 1978; Ahmed 2014). In Newcomb's problem (Nozick 1969) and the psychological twin prisoner's dilemma (Lewis 1979), EDT agents achieve high payoffs by one-boxing and cooperating, whereas CDT agents two-box and defect, walking away poor. Conversely, in medical common-cause dilemmas such as Skyrms's (1980) smoking lesion problem—or in adversarial information traps such as Soares and Fallenstein's (2015) XOR blackmail—CDT agents make the utility-maximizing choice, whereas EDT agents futilely sacrifice utility to "manage the news" (Lewis 1981). Worse still, in sequential predictive dilemmas such as Parfit's hitchhiker (Parfit 1986), the transparent Newcomb problem (Drescher 2006), and mechanical blackmail, *both* CDT and EDT fail, leaving their adherents stranded in the desert or exploited by extortionists.

In *"Functional Decision Theory: A New Theory of Instrumental Rationality,"* Eliezer Yudkowsky and Nate Soares (2017) propose a third paradigm designed to supersede both CDT and EDT with a single coherent rule. The core philosophical shift is to stop treating a decision as an isolated physical token in spacetime, and instead treat it as the logical output of a fixed mathematical decision function. 

While Yudkowsky and Soares note that their broader framework can be formulated over either policies or actions (Footnotes 7 and 16), the primary formal presentation they develop in Section 5, Equation (4) of their paper intervenes directly on the action output of the decision function for a given observation history. In this essay, we refer to this specific formal system as **action functional decision theory (A-FDT)**. We will examine the exact mathematical architecture of **A-FDT**, show how its treatment of subjunctive dependencies and observations resolves the classic paradoxes of decision theory, and develop an explicit operational protocol—distinguishing what follows directly from Yudkowsky and Soares (2017) from additional modeling assumptions—for applying **A-FDT** to unfamiliar decision problems.

---

## 2. The Formal Architecture of A-FDT

### 2.1 Expected Utility and Epistemic Perspectives

Following Gibbard and Harper (1978) and Joyce (1999), EDT, CDT, and **A-FDT** can all be expressed within a unified expected utility framework. Let $\mathcal{A}$ be a finite set of available actions, $\mathcal{X}$ a countable set of possible observation histories, and $\mathcal{O} = \{o_1, o_2, \dots\}$ a countable set of outcomes equipped with a real-valued utility function $\mathcal{U}: \mathcal{O} \to \mathbb{R}$ bounded so that expectations are always finite. Given an observation history $x \in \mathcal{X}$, expected utility maximization prescribes executing an action $a \in \mathcal{A}$ that maximizes Equation (1) of Yudkowsky and Soares (2017):

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j), \tag{1}$$

where $P(a \hookrightarrow o_j ;\, x)$ denotes the subjective probability assigned to outcome $o_j$ in the hypothetical scenario where action $a$ is taken after observing $x$. 

By Joyce's (1999) representation theorem, any agent whose conditional preferences and likelihoods satisfy standard coherence axioms will seek to maximize Equation (1). As Joyce observes, *"decision theories should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated."* That epistemic perspective is entirely encoded in the interpretation of the hypothetical connective "$\hookrightarrow$".

Computationally, we can view an agent as maintaining an internal world-model $M$. To evaluate candidate actions, the agent modifies $M$ for each $a \in \mathcal{A}$ to construct a transient computational object $M^{a\hookrightarrow}$—the *hypothetical for $a$*—and computes the expected value of the utility variable $\textsc{V} \coloneqq \mathcal{U}(\textsc{Outcome})$ within $M^{a\hookrightarrow}$.

### 2.2 From EDT and CDT to Equation (4)

The three theories diverge in what structural information they require inside the world-model $M$ and how they construct $M^{a\hookrightarrow}$:

1. **Evidential Decision Theory (EDT):** The world-model $M$ is simply a Bayesian probability distribution $P$ over random variables $\textsc{Obs}$ (taking values in $\mathcal{X}$), $\textsc{Act}$ (taking values in $\mathcal{A}$), and $\textsc{Outcome}$ (taking values in $\mathcal{O}$). The hypothetical $M^{a\hookrightarrow}$ is formed by standard Bayesian conditioning on both the observation and the action:
   $$\mathrm{EDT}(P, x) \coloneqq \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs}=x, \textsc{Act}=a\right), \tag{2}$$
   where actions $a$ with $P(\textsc{Act}=a \mid \textsc{Obs}=x) = 0$ are excluded from consideration.

2. **Causal Decision Theory (CDT):** Because conditioning preserves spurious common-cause correlations, CDT augments the distribution $P$ with a causal graph $G$—formalized by Yudkowsky and Soares using Judea Pearl's (1996, 2000) graphical causal models. In a Pearlian model $M = (P, G)$, $G$ is a directed acyclic graph (DAG) whose edges encode direct causal dependencies. To construct $M^{a\hookrightarrow}$, CDT conditions on the observation $\textsc{Obs}=x$ and applies Pearl's intervention operator $\mathtt{do}(\textsc{Act}=a)$, which severs all incoming causal arrows into $\textsc{Act}$, fixes $\textsc{Act}=a$, and propagates this change strictly forward along directed paths in $G$:
   $$\mathrm{CDT}(P, G, x) \coloneqq \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x\right). \tag{3}$$

3. **Action Functional Decision Theory (A-FDT):** Like CDT, **A-FDT** constructs hypotheticals via graphical surgery on an augmented world-model $M = (P, G)$. However, in **A-FDT**, the probability distribution $P$ and dependency graph $G$ include variables representing the outputs of mathematical functions and algorithms—including the agent's own decision algorithm. 

Taking Equation (4) of Section 5 in Yudkowsky and Soares (2017) as the defining formal prescription of **A-FDT** (writing $\mathrm{AFDT}$ and $\textsc{afdt}$ where the source writes $\mathrm{FDT}$ and $\textsc{fdt}$), the theory prescribes:

$$\mathrm{AFDT}(P, G, x) \coloneqq \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{afdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right). \tag{4}$$

### 2.3 Dequoting, Quining, and the Two Departures from CDT

To apply Equation (4) accurately, we must unpack both its notation and its operational semantics.

First, notice the underline notation in $\textsc{afdt}(\underline{P}, \underline{G}, \underline{x})$. In Yudkowsky and Soares's formalism, underlines denote *dequoting* (syntactic substitution of a value into a variable's identifier). For example, if $x \coloneqq 3$, then $\textsc{Z}\underline{x}$ denotes the variable name $\textsc{Z}3$. Thus, when an **A-FDT** agent has world-model $(P, G)$ and observes $x$, the expression $\textsc{afdt}(\underline{P}, \underline{G}, \underline{x})$ singles out a specific random variable inside $G$ that represents the logical output of the mathematical function $\mathrm{AFDT}$ when evaluated on the specific inputs $(P, G, x)$. 

Although this specification is self-referential—the variable name inside $G$ depends on $(P, G)$ itself—Yudkowsky and Soares point out that this self-reference is mathematically benign. The agent does not need to know the *output value* of $\mathrm{AFDT}(P, G, x)$ ahead of time in order to include a *variable node* representing that unknown output in her graph, and Kleene's (1938) second recursion theorem guarantees via "quining" that computational data structures can contain and manipulate exact representations of their own source code.

Second, comparing Equation (3) and Equation (4) reveals two profound structural differences between CDT and **A-FDT**:

1. **Logical Type vs. Physical Token Intervention:** CDT intervenes on $\textsc{Act}$, a variable representing the physical movement of the agent's body at a single point in space and time. **A-FDT** intervenes on $\textsc{afdt}(\underline{P}, \underline{G}, \underline{x})$, a logical variable representing the output of the decision function itself. Any physical system in the universe whose behavior is governed by, or accurately simulates, that decision function—including the agent's physical body ($\textsc{Act}$), an identical twin's body, or a predictor's simulation ($\textsc{Prediction}$)—is downstream of $\textsc{afdt}(\underline{P}, \underline{G}, \underline{x})$ in $G$.
2. **Updateless Handling of Observations:** Look closely at how observations enter Equation (4). In CDT, observing $x$ causes the agent to condition her probability distribution on the event $\textsc{Obs}=x$. In **A-FDT**, there is *no* conditioning on $\textsc{Obs}=x$ inside the expectation $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{afdt}(\underline{P}, \underline{G}, \underline{x}) = a)]$. Instead, when an **A-FDT** agent's observation history updates from $x$ to $y$, she responds to the evidence not by restricting her probability space to worlds where $\textsc{Obs}=y$, but by changing *which node in $G$ she intervenes upon*—switching from $\textsc{afdt}(\underline{P}, \underline{G}, \underline{x})$ to $\textsc{afdt}(\underline{P}, \underline{G}, \underline{y})$. 

This second property, inherited from Wei Dai's (2009) Updateless Decision Theory (UDT) and contrasting with the harmful "double update" of Yudkowsky's (2010) Timeless Decision Theory (TDT), allows an **A-FDT** agent to recognize that if her decision function had produced a different output on input $x$, she might never have observed $x$ in the first place.

Finally, Equation (2), Equation (3), and Equation (4) make it transparent when all three theories agree. In any simple decision problem $(P, G)$ where no external process predicts or correlates with $\textsc{Act}$ except via the causal consequences of $\textsc{Act}$ itself (and where $\textsc{Act}$ depends directly on $\textsc{afdt}(\underline{P}, \underline{G})$), we have:

$$\mathbb{E}[\textsc{V} \mid a] = \mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{Act}=a)] = \mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{afdt}(\underline{P}, \underline{G})=a)].$$

The theories diverge precisely when non-causal correlations exist between the agent's action and the environment.

---

## 3. Subjunctive Dependence, Counterpossibles, and Dominance

### 3.1 Subjunctive Dependence and the Calculator Analogy

Why should a predictor's yesterday forecast be modeled as downstream of the node $\textsc{afdt}(\underline{P}, \underline{G}, \underline{x})$, whereas a carcinogenic arterial lesion is not? Yudkowsky and Soares answer this by introducing *subjunctive dependence*. 

When two physical systems compute the same mathematical function on the same inputs, their behaviors subjunctively depend on that function. Suppose two well-functioning electronic calculators—one in Paris, one in Tokyo—are both tasked with computing $6288 + 1048$. Even if the calculators are causally isolated from one another, their outputs are logically constrained to agree ($7336$) insofar as neither suffers a hardware malfunction (such as a stray cosmic ray). Using Charles Sanders Peirce's (1934) type-token distinction, CDT intervenes solely on the physical *token* ("the Parisian calculator displays $a$"), leaving the Tokyo calculator's display untouched. **A-FDT** intervenes on the mathematical *type* ("the function $6288 + 1048$ evaluates to $a$"), which simultaneously updates every physical system that reliably computes or models that calculation.

Causal dependence is simply a special case of subjunctive dependence: if a scribe in Paris copies the calculator's display, her notes depend both causally and subjunctively on the calculation. Conversely, mere statistical coincidence or a non-computational common cause—such as both calculators happening to be painted pink, or an arterial lesion causing both a craving for tobacco and lung cancer—entails no subjunctive dependence between the decision function's output and the environmental state. Thus, as the authors summarize the core analogy: *"Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."*

### 3.2 The Problem of Counterpossibles

Because a mathematical function has its actual output of logical necessity, imagining that $\mathrm{AFDT}(P, G, x)$ outputs $\mathit{defect}$ when it in fact outputs $\mathit{cooperate}$ requires evaluating a *counterpossible conditional*—a counterfactual whose antecedent is logically impossible (Cohen 1990), analogous to asking what would follow if $6288 + 1048 \neq 7336$ or if the twin prime conjecture were false.

One might try to evade counterpossibles by defining a variant theory ($\mathrm{FDT}'$) that asks not *"What if my actual decision function $d$ had a different output?"* but *"What if I implemented a different decision function $f_n \in \mathcal{F}$?"* Yudkowsky and Soares demonstrate that this maneuver fails in Newcomb's problem: because the predictor simulates the agent's actual algorithm $d \notin \mathcal{F}$, merely imagining that the agent's body switches to $f_n$ would break the link with the predictor unless the agent also imagines that *all predictors of $d$ predict as if $d$ behaved like $f_n$*—which immediately reinstates the counterpossible.

Ideally, one might formalize functional counterfactuals via a logical conditioning operator $\mathtt{true}(\phi)$ that updates a distribution $P$ on a counterpossible sentence $\phi$, yielding an evidential-style variant:

$$\mathrm{FDT}^*(P, x) = \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{true}(\textsc{fdt}(\underline{P}, \underline{x}) = a)\right).$$

Because no general mathematical theory of $\mathtt{true}(\phi)$ currently exists, **A-FDT** in Equation (4) bypasses the problem by requiring that the dependency structure of the counterpossible be supplied explicitly via the graph $G$, allowing Pearl's standard $\mathtt{do}$ operator to perform the surgery.

### 3.3 Dominance and Reflective Stability

A frequent objection to one-boxing in Newcomb's problem is the causal dominance principle: regardless of whether Box B is full or empty, taking both boxes yields $\$1,000$ more than taking one box. However, Yudkowsky and Soares point out that dominance is not a theory-neutral criterion. Every interpretation of the hypothetical connective $\hookrightarrow$ induces its own dominance relation:

* Under CDT hypotheticals ($\mathtt{do}(\textsc{Act}=a)$), holding fixed the physical past, $\mathit{twobox}$ dominates $\mathit{onebox}$.
* Under EDT hypotheticals (conditioning on $\textsc{Act}=a$), $\mathit{refrain}$ "dominates" $\mathit{smoke}$ in the smoking lesion problem.
* Under **A-FDT** hypotheticals ($\mathtt{do}(\textsc{afdt}(\underline{P}, \underline{G}, \underline{x})=a)$), action $a$ dominates action $b$ iff, holding fixed all exogenous states and all subjunctive dependency laws in $G$, changing the output of $\mathrm{AFDT}$ from $b$ to $a$ is sometimes better and never worse. By this subjunctive dominance standard, **A-FDT** never selects a dominated option.

Furthermore, because CDT holds predictors' forecasts fixed when constructing hypotheticals, it suffers from severe reflective instability in anti-coordination dilemmas like Gibbard and Harper's (1978) *Death in Damascus*. Suppose Death perfectly predicts whether an agent will stay in Damascus or pay $\$1,000$ to flee by camel to Aleppo, and waits at the predicted city to claim the agent's life (worth $\$1,000,000$). Under CDT, believing one will stay in Damascus makes fleeing appear life-saving, while believing one will flee makes staying appear life-saving. Even if a CDT agent uses a ratification or pseudorandomization procedure (Arntzenius 2008; Joyce 2012) to settle on a mixed belief state $(p \approx 0.5005 \text{ for Damascus}, 1-p \approx 0.4995 \text{ for Aleppo})$, CDT's hypotheticals treat Death's location as independent of $\mathtt{do}(\textsc{Act}=a)$. Consequently, the CDT agent hallucinates an expected utility of $\$500,500$—and if offered a *genuinely* random quantum coin for $\$1$ that would actually defeat Death's prediction $50\%$ of the time (worth $\$500,000$), the CDT agent irrationally refuses to buy it! 

An **A-FDT** agent avoids this trap effortlessly. In her graph $G^F$, Death's appointment book is downstream of $\textsc{afdt}(\underline{P}^F, \underline{G}^F)$. Under $\mathtt{do}(\textsc{afdt}(\underline{P}^F, \underline{G}^F) = \mathit{damascus})$, she dies in Damascus with utility $\$0$; under $\mathtt{do}(\textsc{afdt}(\underline{P}^F, \underline{G}^F) = \mathit{aleppo})$, she dies in Aleppo with utility $-\$1,000$. She calmly stays in Damascus—and if offered the truly random coin for $\$1$, she immediately buys it because switching to the coin node breaks Death's predictive edge and raises her expected utility from $\$0$ to $\$499,999$.

---

## 4. Applying A-FDT to Canonical Decision Problems

To see how Equation (4) operates mechanically, let us trace the world-models $(P^F, G^F)$ and expected utility computations of an idealized **A-FDT** agent ("Fiona") across three representative dilemmas from Section 6 and Section 9 of Yudkowsky and Soares (2017), contrasting her with an EDT agent ("Eve") and a CDT agent ("Carl").

### 4.1 Case 1: Standard Newcomb's Problem (No Observation)

In Newcomb's problem, transparent Box A contains $\$1,000$, and opaque Box B contains $\$1,000,000$ ($\mathit{full}$) if a $99\%$-accurate predictor predicted the agent would $\mathit{onebox}$, and $\$0$ ($\mathit{empty}$) if the predictor predicted $\mathit{twobox}$. The agent makes no intermediate observation ($\mathcal{X} = \{\emptyset\}$, so we omit $x$).

In Fiona's graph $G^F$, the root intervention node is $\textsc{afdt}(\underline{P}^F, \underline{G}^F)$, alongside an exogenous stochastic node $\textsc{Accurate}$ with $P^F(\textsc{Accurate}=\mathit{accurate}) = 0.99$ and $P^F(\textsc{Accurate}=\mathit{inaccurate}) = 0.01$. The structural equations governing the downstream nodes are:

$$\textsc{Act}\big(\textsc{afdt}(\underline{P}^F, \underline{G}^F)\big) = \textsc{afdt}(\underline{P}^F, \underline{G}^F),$$

$$\textsc{Prediction}(a, \mathit{accurate}) = a, \qquad \textsc{Prediction}(a, \mathit{inaccurate}) \neq a,$$

$$\textsc{Box B}(\mathit{onebox}) = \mathit{full}, \qquad \textsc{Box B}(\mathit{twobox}) = \mathit{empty},$$

$$\textsc{V}(\mathit{onebox}, \mathit{full}) = \$1,000,000, \quad \textsc{V}(\mathit{twobox}, \mathit{full}) = \$1,001,000, \quad \textsc{V}(\mathit{onebox}, \mathit{empty}) = \$0, \quad \textsc{V}(\mathit{twobox}, \mathit{empty}) = \$1,000.$$

The dependency graph $G^F$ has directed edges:

$$\textsc{afdt}(\underline{P}^F, \underline{G}^F) \to \textsc{Act} \to \textsc{V}, \qquad \textsc{afdt}(\underline{P}^F, \underline{G}^F) \to \textsc{Prediction} \to \textsc{Box B} \to \textsc{V}, \qquad \textsc{Accurate} \to \textsc{Prediction}.$$

Applying Equation (4), Fiona evaluates her two candidate actions:

* **For $a = \mathit{onebox}$:** The intervention $\mathtt{do}\big(\textsc{afdt}(\underline{P}^F, \underline{G}^F) = \mathit{onebox}\big)$ sets $\textsc{Act} = \mathit{onebox}$ with probability $1$ and propagates through $\textsc{Prediction}$ to yield $P^F(\textsc{Box B}=\mathit{full} \mid \mathtt{do}(\dots)) = 0.99$. Thus:
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\big(\textsc{afdt}(\underline{P}^F, \underline{G}^F) = \mathit{onebox}\big)\right] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000.$$
* **For $a = \mathit{twobox}$:** The intervention $\mathtt{do}\big(\textsc{afdt}(\underline{P}^F, \underline{G}^F) = \mathit{twobox}\big)$ sets $\textsc{Act} = \mathit{twobox}$ with probability $1$ and yields $P^F(\textsc{Box B}=\mathit{full} \mid \mathtt{do}(\dots)) = 0.01$. Thus:
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\big(\textsc{afdt}(\underline{P}^F, \underline{G}^F) = \mathit{twobox}\big)\right] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$

Since $\$990,000 > \$11,000$, $\mathrm{AFDT}(P^F, G^F) = \mathit{onebox}$. Notice that unlike Eve (whose EDT calculation is undefined if her prior $P^E(\mathit{onebox})$ is $0$ or $1$), Fiona's $\mathtt{do}$ operator overrides any prior on $\textsc{afdt}(\underline{P}^F, \underline{G}^F)$. Even when Fiona knows with certainty that she will one-box and that Box B is therefore full, she does not defect to two-boxing, because her hypothetical for $\mathit{twobox}$ counterpossibly alters the output of $\mathrm{AFDT}(P^F, G^F)$ and hence alters the predictor's past forecast.

### 4.2 Case 2: The Smoking Lesion Problem (Preference Uncertainty)

In the smoking lesion problem, an unobserved arterial lesion ($\textsc{Lesion} \in \{\mathit{lesion}, \mathit{nolesion}\}$) causes agents to enjoy smoking and also causes fatal lung cancer $99\%$ of the time (whereas agents without the lesion develop cancer only $1\%$ of the time; $\textsc{Luck} \in \{\mathit{unlucky}, \mathit{lucky}\}$ with $P(\mathit{unlucky}) = 0.99$). Surviving cancer yields $\$1,000,000$; smoking yields $\$1,000$ to an agent with the lesion.

Yudkowsky and Soares formalize the lesion's effect on the agent's desires by introducing two utility functions: $\mathcal{U}_S$ (which values smoking at $+\$1,000$, inducing distribution $P_S^F$) and $\mathcal{U}_R$ (which values smoking at $-\$1$, inducing distribution $P_R^F$). Because Fiona's physical action depends on which preference state she has, her graph $G^F$ contains *two* logical decision nodes—$\textsc{afdt}(\underline{P_S^F}, \underline{G}^F)$ and $\textsc{afdt}(\underline{P_R^F}, \underline{G}^F)$—along with the exogenous nodes $\textsc{Lesion}$ and $\textsc{Luck}$:

$$\textsc{Act}(\mathit{lesion}, s, r) \coloneqq s, \qquad \textsc{Act}(\mathit{nolesion}, s, r) \coloneqq r.$$

Crucially, in $G^F$, there is **no directed path** from $\textsc{afdt}(\underline{P_S^F}, \underline{G}^F)$ to $\textsc{Lesion}$ or $\textsc{Cancer}$:

$$\textsc{Lesion} \to \textsc{Cancer} \to \textsc{Death} \to \textsc{V}, \qquad \textsc{Lesion} \to \textsc{Act} \to \textsc{V}, \qquad \textsc{afdt}(\underline{P_S^F}, \underline{G}^F) \to \textsc{Act}.$$

Let $P_S^F(\textsc{Lesion}=\mathit{lesion}) = p \in (0,1)$ and $P_S^F\big(\textsc{afdt}(\underline{P_R^F}, \underline{G}^F) = \mathit{smoke}\big) = q$. When Fiona has utility function $\mathcal{U}_S$, she evaluates $\mathrm{AFDT}(P_S^F, G^F)$ by intervening on $\textsc{afdt}(\underline{P_S^F}, \underline{G}^F)$. Because $\textsc{Lesion}$ is causally and subjunctively upstream of the intervention, its probability remains invariant:

$$P_S^F\big(\mathit{lesion} \;\big|\; \mathtt{do}(\textsc{afdt}(\underline{P_S^F}, \underline{G}^F) = \mathit{smoke})\big) = P_S^F\big(\mathit{lesion} \;\big|\; \mathtt{do}(\textsc{afdt}(\underline{P_S^F}, \underline{G}^F) = \mathit{refrain})\big) = p.$$

In the branch where $\textsc{Lesion}=\mathit{lesion}$ (probability $p$), her survival probability is $0.01$ (expected survival utility $\$10,000$), and $\textsc{Act}$ is governed by $\textsc{afdt}(\underline{P_S^F}, \underline{G}^F)$. In the branch where $\textsc{Lesion}=\mathit{nolesion}$ (probability $1-p$), her survival probability is $0.99$ (expected survival utility $\$990,000$), and $\textsc{Act}$ is governed by $\textsc{afdt}(\underline{P_R^F}, \underline{G}^F)$, which smokes with probability $q$. Thus, under $\mathcal{U}_S$:

$$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\big(\textsc{afdt}(\underline{P_S^F}, \underline{G}^F) = \mathit{smoke}\big)\right] = p(\$10,000 + \$1,000) + (1-p)(\$990,000 + q \cdot \$1,000),$$

$$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\big(\textsc{afdt}(\underline{P_S^F}, \underline{G}^F) = \mathit{refrain}\big)\right] = p(\$10,000) + (1-p)(\$990,000 + q \cdot \$1,000).$$

The $\mathit{smoke}$ hypothetical exceeds $\mathit{refrain}$ by exactly $p \cdot \$1,000 > 0$, so Fiona smokes.

*(Methodological note on the source text:* Yudkowsky and Soares remark in Section 6 that Fiona "does not have introspective access to the point of intervention, and computes her action under ignorance about her own preferences." Mathematically, Equation (4) requires dequoting the input distribution $\underline{P_S^F}$ to select the node $\textsc{afdt}(\underline{P_S^F}, \underline{G}^F)$, while simultaneously treating $P_S^F(\mathit{lesion}) = p < 1$ inside that distribution. In other words, the formal mechanism works because $P_S^F$ is an unconditioned prior over $\textsc{Lesion}$ paired with the valuation $\mathcal{U}_S$, rather than a posterior distribution conditioned on the agent discovering her own utility function. The authors rightly concur with Eells (1984) that this setup is artificial and point to the XOR blackmail problem as a cleaner test case where EDT fails even with full self-knowledge.)*

### 4.3 Case 3: Observation-Dependent Dilemmas (Transparent Newcomb & Blackmail)

Now consider dilemmas where the agent receives a non-trivial observation $x \in \mathcal{X}$ prior to acting. In the *transparent Newcomb problem* (isomorphic to *Parfit's hitchhiker*), both boxes are transparent, so the agent observes either $x = \mathit{full}$ or $x = \mathit{empty}$ before choosing $\mathit{onebox}$ or $\mathit{twobox}$. The predictor ($99\%$ accurate) places $\$1,000,000$ in Box B iff she predicts that the agent will $\mathit{onebox}$ *upon observing $\mathit{full}$*.

Both Carl (CDT) and Eve (EDT) condition on $\textsc{Obs} = \mathit{full}$, fixing Box B's contents at $\$1,000,000$, and therefore choose $\mathit{twobox}$ (getting $\$1,001,000 > \$1,000,000$ in their conditioned hypotheticals). Foreseeing this, the predictor leaves Box B empty.

How does **A-FDT** evaluate the problem when Fiona observes $x = \mathit{full}$? In Fiona's graph $G^F$, there are two logical decision nodes corresponding to the two possible observations: $\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{full})$ and $\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{empty})$. Because the predictor specifically simulates what Fiona will do if shown a full box, the predictor's forecast depends on $\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{full})$:

$$\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{full}) \to \textsc{Prediction} \to \textsc{Box B} \to \textsc{V}, \qquad \textsc{Accurate} \to \textsc{Prediction}.$$

Moreover, $\textsc{Prediction}$ determines which observation Fiona receives, and thus which of her two logical decision nodes actually controls her physical action $\textsc{Act}$:

$$\textsc{Act}\big(\textsc{Prediction}=\mathit{1}, a_{\mathit{full}}, a_{\mathit{empty}}\big) = a_{\mathit{full}}, \qquad \textsc{Act}\big(\textsc{Prediction}=\mathit{2}, a_{\mathit{full}}, a_{\mathit{empty}}\big) = a_{\mathit{empty}}.$$

When Fiona sees that Box B is full ($x = \mathit{full}$), Equation (4) instructs her to compute:

$$\mathrm{AFDT}(P^F, G^F, \mathit{full}) = \operatorname{argmax}_{a \in \{\mathit{onebox}, \mathit{twobox}\}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{full}) = a\right)\right).$$

*(Note: In Section 6 of the source paper, an inline display equation inadvertently writes $\textsc{Obs}=\mathit{full}$ inside the conditioning bar, but both Equation (4) and the authors' immediately following derivation make clear that **no** conditioning on $\textsc{Obs}=\mathit{full}$ occurs.)*

Let $q \coloneqq P^F\big(\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{empty}) = \mathit{twobox}\big)$ be Fiona's prior probability that she two-boxes if shown an empty box. Without conditioning on $\textsc{Obs}=\mathit{full}$, Fiona evaluates the global expectation under each intervention on $\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{full})$:

* **Under $\mathtt{do}\big(\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{full}) = \mathit{onebox}\big)$:**
  * With probability $0.99$ ($\textsc{Accurate}=\mathit{accurate}$), $\textsc{Prediction}=\mathit{1}$, $\textsc{Box B}=\mathit{full}$, and $\textsc{Act}$ follows $\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{full}) = \mathit{onebox}$, yielding $\$1,000,000$.
  * With probability $0.01$ ($\textsc{Accurate}=\mathit{inaccurate}$), $\textsc{Prediction}=\mathit{2}$, $\textsc{Box B}=\mathit{empty}$, and $\textsc{Act}$ is governed instead by $\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{empty})$, yielding $q \cdot \$1,000$ in expectation.
  * Total expected utility: $\$990,000 + 0.01q \cdot \$1,000$.
* **Under $\mathtt{do}\big(\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{full}) = \mathit{twobox}\big)$:**
  * With probability $0.01$ ($\textsc{Accurate}=\mathit{inaccurate}$), $\textsc{Prediction}=\mathit{1}$, $\textsc{Box B}=\mathit{full}$, and $\textsc{Act}$ follows $\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{full}) = \mathit{twobox}$, yielding $\$1,001,000$.
  * With probability $0.99$ ($\textsc{Accurate}=\mathit{accurate}$), $\textsc{Prediction}=\mathit{2}$, $\textsc{Box B}=\mathit{empty}$, and $\textsc{Act}$ is governed by $\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{empty})$, yielding $q \cdot \$1,000$ in expectation.
  * Total expected utility: $0.01(\$1,001,000) + 0.99q \cdot \$1,000 = \$10,010 + q \cdot \$990$ (printed in the source text with a minor typographical slip as $\$110,00 + q \cdot \$990$).

For any $q \in [0, 1]$, $\$990,000 + \$10q > \$10,010 + \$990q$. Thus, $\mathrm{AFDT}(P^F, G^F, \mathit{full}) = \mathit{onebox}$. Even while staring directly at $\$1,000,000$ in Box B, Fiona leaves Box A behind because her hypothetical for $\mathit{twobox}$ imagines a universe where $\mathrm{AFDT}(P^F, G^F, \mathit{full})$ outputs $\mathit{twobox}$—a universe in which she almost certainly never observes a full box at all.

Exactly the same updateless mechanics govern the two blackmail dilemmas:
* In **XOR Blackmail**, an honest predictor sends a letter ($x = \mathit{letter}$) iff either (i) the house has no termites ($\mathit{notermites}$) and the agent will $\mathit{pay}$ $\$1,000$, or (ii) the house has termites ($\mathit{termites}$, costing $\$1,000,000$) and the agent will $\mathit{refuse}$. Conditioning on $x = \mathit{letter}$ traps Eve (EDT) into paying, because $\textsc{Act}=\mathit{pay}$ implies $\mathit{notermites}$. Under **A-FDT**, however, $\textsc{Infestation}$ is an exogenous root node (prior probability $p$ of termites) with no incoming arrow from $\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{letter})$. Intervening on $\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{letter})$ changes whether the predictor sends the letter, but leaves $P^F(\textsc{Infestation}=\mathit{termites}) = p$ completely unchanged while costing $\$1,000$ whenever the letter is sent. Thus, Fiona refuses to pay.
* In **Mechanical Blackmail**, a predictor initiates a self-incriminating $\$1,000,000$ defamation program (sending observation $x = \mathit{blackmail}$) iff she predicts the agent will wire $\$1,000$ ($\mathit{pay}$) upon receiving the notice. If the predictor errs with probability $\varepsilon = 0.0009$, Fiona's intervention $\mathtt{do}\big(\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{blackmail}) = \mathit{pay}\big)$ yields expected utility $-\$1,000$ (she is blackmailed with probability $1-\varepsilon \approx 1$ and pays $\$1,000$), whereas $\mathtt{do}\big(\textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{blackmail}) = \mathit{refuse}\big)$ yields expected utility $-0.0009 \times \$1,000,000 = -\$900$ (she is only blackmailed when the predictor errs). Because $-\$900 > -\$1,000$, Fiona refuses to pay even when holding the blackmail letter in her hand!

---

## 5. Open Questions and an Operational Protocol for Unfamiliar Cases

While Yudkowsky and Soares (2017) establish the conceptual foundations of **A-FDT**, they explicitly leave two technical questions open: first, how to systematically construct the subjunctive dependency graph $G$ from a problem specification; and second, how the action-level formulation in Equation (4) relates to the policy-level formulation mentioned in Footnotes 7 and 16. In this section, we clearly separate what is stated in the reference paper from our own operational proposals for resolving these questions in unfamiliar cases.

### 5.1 An Operational Protocol for Constructing $(P, G)$

In Section 5, Yudkowsky and Soares note that while Pearl (2000) provides a rigorous methodology for inferring causal graphs from interventions, *"no such formal treatment has yet been given to the problem of deducing the structure of other kinds of subjunctive dependence."* 

To make **A-FDT** practically usable for a researcher facing a novel decision problem, we can synthesize the modeling patterns in Section 6 of the paper into an explicit four-step **Computational Structural Equation Protocol** (an operational systematization going beyond the text's informal remarks):

1. **Partition the Variable Space:** Divide the variables of the decision problem into three disjoint sets:
   * *Exogenous physical/stochastic variables* $\mathcal{E}$ (e.g., background states of nature, lesions, prediction noise $\textsc{Accurate}$), equipped with a prior distribution $P(\mathcal{E})$.
   * *Logical decision nodes* $\Lambda = \{\Lambda_{x, k} \coloneqq \textsc{afdt}(\underline{P_k}, \underline{G}, \underline{x}) : x \in \mathcal{X}, k \in \mathcal{K}\}$, indexed by every possible observation history $x \in \mathcal{X}$ (and, if the agent has uncertainty over her own epistemic/preference state $P_k$, indexed by $k \in \mathcal{K}$). Assign an arbitrary working prior $P(\Lambda)$ to these nodes for evaluating off-branch contingencies.
   * *Endogenous mechanism variables* $\mathcal{M}$, including predictors' actions ($\textsc{Prediction}$), the agent's observation ($\textsc{Obs}$), the physical action ($\textsc{Act}$), and utility ($\textsc{V}$).
2. **Assign Subjunctive Structural Equations for Predictors:** For every external agent or mechanism $Y \in \mathcal{M}$ in the environment, ask: *Does the physical process generating $Y$ simulate, deduce, or copy the output of the agent's decision procedure in contingency $(P_k, x)$?* 
   * If yes (e.g., a twin, a game-theoretic counterpart using symmetric reasoning, or a predictor simulating contingency $x$), add a directed edge $\Lambda_{x, k} \to Y$ and write the structural equation $Y = f_Y(\Lambda_{x, k}, \epsilon_Y)$, where $\epsilon_Y \in \mathcal{E}$ represents simulation error.
   * If no (e.g., a statistical correlate or prior common cause that does not compute $\mathrm{AFDT}$), add **no** edge from $\Lambda$ to $Y$.
3. **Wire the Observation-Gating Multiplexer for $\textsc{Act}$:** Because **A-FDT** does not condition on $\textsc{Obs} = x$, the physical action variable $\textsc{Act}$ must be modeled as a multiplexer (a conditional switch) gated by the endogenous observation $\textsc{Obs}$ (and preference state $k$):
   $$\textsc{Act}\big(\textsc{Obs}, k, \{\Lambda_{x', k'}\}\big) \coloneqq \Lambda_{\textsc{Obs}, k}.$$
   This equation is essential: it ensures that when we intervene on $\Lambda_{x, k}$ without conditioning on $\textsc{Obs}=x$, changing $\Lambda_{x, k}$ only alters $\textsc{Act}$ in those hypothetical worlds where the agent *actually observes $x$* (and is in state $k$).
4. **Execute Updateless Intervention:** Upon actually observing $x^*$ in preference state $k^*$, do not update $P(\mathcal{E})$. Instead, for each $a \in \mathcal{A}$, compute the expectation of $\textsc{V}$ under the Pearlian intervention $\mathtt{do}(\Lambda_{x^*, k^*} = a)$ using the structural equations from Steps 1–3, and output the action $a^*$ that maximizes this expectation.

### 5.2 Action-Level (A-FDT) vs. Policy-Level Intervention: An Unfamiliar Dilemma

In Footnotes 7 and 16, Yudkowsky and Soares remark that in their preferred formalization of FDT, agents iterate over *policies* (mappings $\pi: \mathcal{X} \to \mathcal{A}$) rather than actions, intervening on a single node $\textsc{fdt}(\underline{P}, \underline{G}) = \pi$ and then executing $\pi(x)$. They state that this distinction *"only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."*

Why—and exactly when—does the action-level rule of **A-FDT** in Equation (4) diverge from policy-level evaluation? Using the formal machinery above, we can construct an unfamiliar diagnostic case that makes the mathematical boundary between **A-FDT** and policy-based FDT crystal clear.

> **Dilemma (The Cross-Branch Audit):** An agent will observe a fair coin flip $x \in \{\mathit{heads}, \mathit{tails}\}$ ($P(\mathit{heads}) = 0.5$) and must then choose an action $a \in \{\mathit{safe}, \mathit{risky}\}$. Choosing $\mathit{risky}$ costs $\$1,000$ directly (regardless of the coin flip), while $\mathit{safe}$ costs $\$0$. Before the coin is flipped, an infallible auditor simulates how the agent will respond to *both* possible coin flips. The auditor places a $\$1,000,000$ bonus in the agent's bank account iff the auditor predicts that the agent will choose $\mathit{risky}$ on $\mathit{heads}$ **and** choose $\mathit{risky}$ on $\mathit{tails}$. Suppose the coin lands $x = \mathit{heads}$. What should the agent do?

Let us apply **A-FDT** (Equation 4) to this dilemma. Following our operational protocol, the graph $G^F$ has two logical decision nodes: $\Lambda_H \coloneqq \textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{heads})$ and $\Lambda_T \coloneqq \textsc{afdt}(\underline{P}^F, \underline{G}^F, \mathit{tails})$. The auditor's bonus variable $\textsc{Bonus} \in \{0, \$1,000,000\}$ depends on *both* nodes:

$$\textsc{Bonus}(\Lambda_H, \Lambda_T) = \begin{cases} \$1,000,000 & \text{if } \Lambda_H = \mathit{risky} \text{ and } \Lambda_T = \mathit{risky}, \\ \$0 & \text{otherwise.} \end{cases}$$

The physical action is gated by the coin flip $\textsc{Coin} \in \{\mathit{heads}, \mathit{tails}\}$: $\textsc{Act}(\mathit{heads}, \Lambda_H, \Lambda_T) = \Lambda_H$ and $\textsc{Act}(\mathit{tails}, \Lambda_H, \Lambda_T) = \Lambda_T$.

Now suppose the agent observes $x = \mathit{heads}$ and evaluates Equation (4) by intervening solely on $\Lambda_H$: $\mathtt{do}(\Lambda_H = a)$. Because $\Lambda_T$ is a separate node in $G^F$, what happens to $\Lambda_T$ when we intervene on $\Lambda_H$? 

Here we encounter an ambiguity left open by the source paper:

1. **Strict Independent-Node A-FDT:** If $\Lambda_H$ and $\Lambda_T$ have no directed edge between them in $G^F$, then $\mathtt{do}(\Lambda_H = a)$ leaves $\Lambda_T$ at its prior probability $q \coloneqq P^F(\Lambda_T = \mathit{risky})$. Then:
   $$\mathbb{E}[\textsc{V} \mid \mathtt{do}(\Lambda_H = \mathit{risky})] = q(\$1,000,000) - 0.5(\$1,000) - 0.5q(\$1,000),$$
   $$\mathbb{E}[\textsc{V} \mid \mathtt{do}(\Lambda_H = \mathit{safe})] = \$0 - 0.5q(\$1,000).$$
   Consequently, $\mathrm{AFDT}(P^F, G^F, \mathit{heads})$ chooses $\mathit{risky}$ iff $q > 0.0005$! If the agent starts with a pessimistic prior $q = 0$ about her own behavior on the $\mathit{tails}$ branch, each branch $\Lambda_H$ and $\Lambda_T$ will defect to $\mathit{safe}$ on the grounds that the other branch is defecting—a classic coordination failure across observation branches.
2. **Symmetry-Linked A-FDT or Policy-Level FDT:** Notice, however, that $\Lambda_H$ and $\Lambda_T$ are outputs of the *same* algorithm $\mathrm{AFDT}(P^F, G^F, \cdot)$ facing completely symmetric inputs. If the agent models this algorithmic symmetry as a subjunctive dependency between her own branches—or if, as Yudkowsky and Soares advocate in Footnotes 7 and 16, she intervenes on the function node $\textsc{pfdt}(\underline{P}^F, \underline{G}^F) = \pi$ over the four possible policies $\pi: \{\mathit{heads}, \mathit{tails}\} \to \{\mathit{safe}, \mathit{risky}\}$—then the policy $\pi^*(\mathit{heads}) = \pi^*(\mathit{tails}) = \mathit{risky}$ achieves $\$1,000,000 - \$1,000 = \$999,000$, decisively beating all other policies (which yield at most $\$0$).

This example illustrates why **A-FDT** (Equation 4) suffices for all single-contingency dilemmas in Yudkowsky and Soares (2017)—where the predictor only cares about the single node $\textsc{afdt}(\underline{P}^F, \underline{G}^F, x)$ corresponding to the observation $x$ the predictor induces—whereas problems with cross-branch predictive dependencies require either explicit subjunctive links between sibling nodes $\Lambda_{x_1}, \Lambda_{x_2}$ or a policy-level intervention.

### 5.3 The Open Problem of "Fair" Dilemmas

Finally, Yudkowsky and Soares emphasize in Section 9 that no decision theory can win in every conceivable environment. If an adversarial mind-reader rewards agents iff their source code literally implements CDT (or punishes agents who output the same action as a copy of Fiona), then **A-FDT** will lose. The authors define a dilemma as *informally fair* if the agent has accurate beliefs and the environment rewards or punishes the agent solely based on predictions of the agent's *behavior in the dilemma at hand*, rather than directly rewarding or punishing the syntax of the agent's decision procedure. Formalizing a general mathematical criterion for "fairness"—for instance, by systematically translating a game that penalizes copies of Fiona into an analogous game that penalizes copies of Carl (Footnote 15)—remains a major open research problem.

---

## 6. Conclusion

**Action functional decision theory (A-FDT)**, as formalized in Equation (4) of Yudkowsky and Soares (2017), achieves a synthesis long thought impossible in the philosophy of rational choice. By shifting the locus of intervention from the physical act token $\textsc{Act}$ to the logical output variable $\textsc{afdt}(\underline{P}, \underline{G}, \underline{x})$, and by responding to observations $x$ through target-node switching rather than Bayesian conditionalization, **A-FDT** preserves the genuine computational and predictive dependencies that CDT severs while discarding the spurious statistical correlations that paralyze EDT. Although foundational questions remain regarding the automated discovery of subjunctive graphs and the formal semantics of counterpossibles, **A-FDT** provides a mathematically precise, reflectively stable procedure that unifies single-agent decision theory and multi-agent coordination under a single principle of instrumental rationality.

---

## References

* Ahmed, Arif. 2014. *Evidence, Decision and Causality*. Cambridge University Press.
* Arntzenius, Frank. 2008. "No Regrets, or: Edith Piaf Revamps Decision Theory." *Erkenntnis* 68 (2): 277–297.
* Cohen, Daniel. 1990. "On What Cannot Be." In *Truth or Consequences: Essays in Honor of Nuel Belnap*, 123–132. Kluwer Academic Publishers.
* Dai, Wei. 2009. "Towards a New Decision Theory." *Less Wrong*, August 13, 2009.
* Drescher, Gary L. 2006. *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Eells, Ellery. 1984. "Metatickles and the Dynamics of Deliberation." *Theory and Decision* 17 (1): 71–95.
* Gibbard, Allan, and William L. Harper. 1978. "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, Vol. 1, 125–162. D. Reidel.
* Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Joyce, James M. 2012. "Regret and Instability in Causal Decision Theory." *Synthese* 187 (1): 123–145.
* Kleene, Stephen Cole. 1938. "On Notation for Ordinal Numbers." *Journal of Symbolic Logic* 3 (4): 150–155.
* Lewis, David. 1979. "Prisoners' Dilemma is a Newcomb Problem." *Philosophy & Public Affairs* 8 (3): 235–240.
* Lewis, David. 1981. "Causal Decision Theory." *Australasian Journal of Philosophy* 59 (1): 5–30.
* Nozick, Robert. 1969. "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel*, 114–146. D. Reidel.
* Parfit, Derek. 1986. *Reasons and Persons*. Oxford University Press.
* Pearl, Judea. 1996. "Causation, Action, and Counterfactuals." In *6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-'96)*, 51–73. Morgan Kaufmann.
* Pearl, Judea. 2000. *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Peirce, Charles Sanders. 1934. *Collected Papers of Charles Sanders Peirce*, Vol. V: *Pragmatism and Pragmaticism*. Harvard University Press.
* Skyrms, Brian. 1980. *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Soares, Nate, and Benja Fallenstein. 2015. "Toward Idealized Decision Theory." *arXiv preprint arXiv:1507.01986*.
* Yudkowsky, Eliezer. 2010. *Timeless Decision Theory*. The Singularity Institute.
* Yudkowsky, Eliezer, and Nate Soares. 2017. "Functional Decision Theory: A New Theory of Instrumental Rationality." *arXiv preprint arXiv:1710.05060v2*.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining A-FDT's Application**

I'm currently focused on structuring the essay to clearly explain Action Functional Decision Theory (A-FDT). My aim is to make its application to decision problems accessible. The main challenge lies in balancing technical rigor with clarity for a broader audience. I'm exploring different examples to illustrate A-FDT's core principles.


**Clarifying FDT's Formalism**

I'm now diving deep into Equation (4) from the paper, carefully analyzing its role as the central formal expression of A-FDT. I'm taking special note of the distinction between policy and action iterations within the formalism. The goal is to articulate this clearly for the audience, ensuring they grasp the nuances of the mathematical foundation.


**Refining A-FDT's Application**

I'm making sure to consistently use "A-FDT" throughout, especially in headings and examples, to avoid confusion. I'm also ensuring that all quotations are faithful to the original sources, even if it means clarifying the use of "FDT" in brackets. The aim is to create a clear and coherent account with mathematical definitions, examples, and explanations that allows readers to independently make decisions in unfamiliar cases. I'm focusing on how the theory evaluates actions and relevant dependencies.


**Elaborating Theoretical Nuances**

I'm digging deeper into counterfactuals, focusing on the $\mathtt{do}$ operator and its application to logical and computational nodes, along with the updatelessness principle. I'm exploring how observations are handled by surgical interventions rather than standard Bayesian conditioning. I plan to articulate uncertainties in the source material, providing justified operational interpretations where possible. I'm also preparing examples like Newcomb's Problem and others to demonstrate the theory's practical applications.


**Analyzing Word Count & Math**

I'm now focusing on the target word count and the mathematical foundations. I'm aiming for a word count between 2650 and 2850 words. Specifically, I'm carefully reviewing Equation (1), the expected utility maximization, from Gibbard & Harper (1978) and Joyce (1999). I'm carefully checking the details of the equation, including the parameters and their notations, along with Joyce's representation theorem.


**Comparing Decision Frameworks**

I'm now carefully comparing EDT, CDT, and A-FDT. I'm focusing on Equations 2, 3, and 4 from the source, specifically how each framework evaluates actions and makes decisions. I'm working to show how the world-model,  $M$ and the hypotheticals $M^{a\hookrightarrow}$, are used to compute the expected utility $V_a$, considering each framework's unique approach to handling observations and interventions. I'm clarifying how each framework uses causal models and the $\mathtt{do}$ operator, especially within A-FDT's self-referential structure.


**Correcting Mathematical Details**

I've pinpointed a typo in the inline formula for the Transparent Newcomb Problem, specifically the unnecessary conditioning on `Obs=full`. I am ensuring that the correct interpretation is emphasized: Fiona does *not* condition on `Obs=full`. I'm clarifying this crucial point and ensuring we faithfully represent Equation (4) using consistent A-FDT notation.


**Interpreting Equation 4's Structure**

I'm currently focused on the structural features of Equation (4) from Yudkowsky and Soares (2017). I'm carefully analyzing how A-FDT intervenes on the logical output of the decision procedure. I am working to clarify the use of Kleene's recursion theorem in handling self-reference, making the distinction between type and token clear in the intervention. I'm focusing on the dequoting process to ensure fidelity with the notation.


**Clarifying Updateless Observations**

I'm currently focusing on how A-FDT handles observations, contrasting it with EDT and CDT. Specifically, I'm analyzing the differences between Equation (4) and Equations (2) and (3). In A-FDT, observations solely influence which logical node is intervened upon within the causal graph. The agent *doesn't* condition on the observation as in EDT and CDT. This design is crucial for resolving dilemmas like the Transparent Newcomb Problem, where conditioning would lead to suboptimal choices.


**Analyzing Updatelessness Further**

I'm now further analyzing updatelessness. I'm carefully contrasting A-FDT's treatment of observations with the approaches of UDT and TDT. I understand the key difference, where A-FDT evaluates the universe after considering an observation, without updating beliefs. I'm focusing on the implications for decision-making in various scenarios, and working to clearly articulate this within the paper. I'm also examining the construction of the subjunctive dependency graph and counterpossible semantics, identifying areas where the original paper might be under-specified.


**Constructing FDT's DAG**

I'm now grappling with the practical application of A-FDT, especially the construction of the DAG G. Given that a formal theory of counterpossible conditionalization is currently unavailable, I'm focusing on defining an explicit operational protocol ("Computational Structural Equation Modeling") for building the DAG in unfamiliar decision problems. This involves identifying and distinguishing between exogenous variables, logical decision-output nodes, and the decision function itself.


**Defining Computational DAGs**

I'm now focusing on how A-FDT constructs the computational directed acyclic graph (DAG), especially in the Smoking Lesion scenario. I am also working to formalize how to deal with *introspective uncertainty*. The plan is to articulate the relationship between physical and predictive mechanisms that estimate the output of A-FDT. I'm carefully analyzing how Fiona's uncertainty about her own preferences impacts the DAG's structure.


**Resolving Internal Conflict**

I'm now clarifying a subtle tension in the Smoking Lesion scenario. While I understand that the algorithm *intervenes* on the logical output, my focus is on why the prose suggests no introspective access when dequoting her input $P_S^F$ and selecting the intervention node. This stems from Fiona's world model, where the prior probability of "Lesion" isn't fixed at 1, even though the decision procedure does use the utility function $\mathcal{U}_S$ in its evaluation. I'm carefully analyzing the nuances of this self-referential process to express this clearly.


**Differentiating A-FDT Formalisms**

I'm now clarifying the key distinction in Footnotes 7 and 16 regarding action-level versus policy-level interventions. My focus is on clearly articulating why our essay, which focuses on A-FDT, can set aside this nuance for simplicity. I'm focusing on how this distinction primarily affects multi-agent scenarios, remaining committed to an exposition that explains A-FDT's single-agent application concisely. This should enhance the reader's comprehension.


**Elaborating Multi-Observation Scenarios**

I'm now expanding the essay to explain how A-FDT handles multi-observation problems. I plan to construct a concrete example where the action-level evaluation diverges from the policy-level evaluation, especially when a predictor's actions depend on what the agent does across multiple observation branches. I'm focusing on showing how A-FDT evaluates actions node-by-node, highlighting this unique aspect.


**Structuring Essay Elements**

I'm now focusing on sectioning the essay to align with a natural, mathematically sound flow, and a word count of 2400-3000 words. The key will be highlighting the central clash in normative decision theory, followed by the formalization of A-FDT in Equation (4). The goal is a clear structure: an introduction to A-FDT, the formal architecture of the theory, a comparison of A-FDT to EDT and CDT, the application of A-FDT to decision problems, and then a conclusion.


**Analyzing A-FDT's Equation**

I'm now carefully dissecting Equation (4), contrasting how EDT, CDT, and A-FDT construct hypotheticals from the agent's world-model. I am focusing on the formal components: $P$, $G$, dequoting with Kleene's recursion theorem, intervening on the logical output, and updatelessness. I'm clarifying the mathematical distinctions between EDT, CDT, and A-FDT, especially regarding the do-operator and how it's used with observations.


**Clarifying Equivalence Conditions**

I'm now clarifying the circumstances under which EDT, CDT, and A-FDT yield identical results. I've pinpointed the key equivalence condition, emphasizing that when all non-causal correlations between Act and other variables vanish, each decision framework converges. This involves carefully analyzing the structural dependencies within the causal graph G and how each theory handles the evaluation of actions. I'm focusing on the implications of this condition for practical decision-making.


**Reframing Dominance in A-FDT**

My current focus is reframing the concept of dominance within A-FDT. I'm exploring how dominance is intrinsically tied to the chosen counterfactual connective. I'm articulating why A-FDT's subjunctive dominance principle resolves CDT's instability in dilemmas like *Death in Damascus*. I am working to clarify the utility calculations for several cases, including the canonical Newcomb's problem.


**Illustrating Decision Dynamics**

Now, I'm constructing a detailed walkthrough of multi-node graphs, specifically for Transparent Newcomb. I'm carefully calculating expected utilities under A-FDT, showing how updateless node-switching enables one-boxing, even with observations. The goal is to accurately represent the source's misprinted value and provide a mathematically sound explanation.


**Defining DAG Construction**

I'm now fully immersed in developing an operational protocol for constructing the subjunctive dependency graph, $G$, especially in unfamiliar decision problems, as the source is unspecified here. I'm focusing on a four-step process. First, I am clarifying how to identify exogenous variables. Second, I need to instantiate the observation-indexed logical nodes, $\Lambda_x$. Third, I must define computational/predictive dependencies via structural equations. Finally, I need to execute Pearl's $\mathtt{do}$ surgery without conditioning on $\textsc{Obs} = x$. I need to incorporate this into an example.


```
