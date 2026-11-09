# 021_fdt_eq4_google_gemini-4-argon_rhigh_phigh / 00001

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/392f952c-e364-4fc9-852a-7f738ede3a90/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/392f952c-e364-4fc9-852a-7f738ede3a90/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Action Functional Decision Theory (A-FDT): Formal Mechanics, Counterpossible Graph Surgery, and Practical Application

## 1. Introduction

For nearly half a century, normative decision theory has been divided between two foundational paradigms: *evidential decision theory* (EDT) and *causal decision theory* (CDT). Both frameworks endorse expected utility maximization, yet they disagree on how an agent should evaluate the hypothetical consequences of an action. Measured by average utility achieved across classic decision-theoretic dilemmas, neither theory is consistently dominant. EDT outperforms CDT in Newcomb’s problem and the psychological twin prisoner’s dilemma, whereas CDT outperforms EDT in Skyrms’s smoking lesion problem and simple extortion dilemmas (Gibbard and Harper 1978; Skyrms 1980; Ahmed 2014). An agent who judiciously alternated between CDT and EDT depending on the structure of the dilemma at hand would systematically outperform any purist adherent of either theory—an awkward state of affairs for any candidate theory of instrumental rationality.

In *"Functional Decision Theory: A New Theory of Instrumental Rationality"* (2017), Eliezer Yudkowsky and Nate Soares propose a unified alternative designed to capture the strengths of both theories without their respective pathologies. Their core philosophical move is to shift the unit of decision-making from a *physical action token* to the *logical output of a fixed mathematical decision function*. While the authors note in passing (Footnotes 7 and 16) that their most general formulation of the theory selects comprehensive *policies* mapping observations to actions, the formal procedure they present and analyze throughout the paper—given in **Equation (4), Section 5**—evaluates and selects individual *actions* by intervening on an observation-indexed functional variable.

In this essay, we examine **action functional decision theory (A-FDT)** as defined by Equation (4) of Yudkowsky and Soares (2017). We first lay out the philosophical motivation for **A-FDT** via the concept of *subjunctive dependence*. We then unpack the formal mathematical apparatus of **A-FDT**, contrasting its graphical interventions and "updateless" treatment of observations against EDT, CDT, and related variants. Next, we work through the exact mathematical mechanics of **A-FDT** across canonical decision problems. Finally, to equip readers to apply **A-FDT** to unfamiliar cases, we examine three areas where the source text leaves operational details open and develop explicit mathematical assumptions to bridge those gaps.

---

## 2. Philosophical Motivation: From Physical Acts to Subjunctive Dependence

To see why standard decision theories falter, compare two structurally parallel dilemmas from Yudkowsky and Soares (2017, Sec. 2):

1. **Newcomb’s Problem** (Nozick 1969): A predictor who is $99\%$ accurate has placed $\$1,000,000$ in an opaque box B if and only if she predicted the agent will leave behind a transparent box A containing $\$1,000$ (*one-boxing*), and $\$0$ in box B if she predicted the agent will take both boxes (*two-boxing*).
2. **The Smoking Lesion Problem** (Skyrms 1980): An agent gains utility equivalent to $\$1,000$ from smoking and $\$1,000,000$ from avoiding fatal lung cancer. Smoking does not cause cancer; rather, an unobserved arterial lesion causes afflicted agents both to love smoking and ($99\%$ of the time) to develop lung cancer, whereas those without the lesion develop cancer only $1\%$ of the time.

At the moment of choice, both dilemmas feature a state of the world (the contents of box B; the presence of the lesion) that is already fixed in the past and causally unaffected by the agent’s physical act, alongside a sure gain of $\$1,000$ for taking a specific physical action (two-boxing; smoking). Consequently, Gibbard and Harper (1978) argued that no single consistent principle of rationality can prescribe both one-boxing and smoking: an agent must either condition on the evidence her act provides about the past (as EDT does, one-boxing and refraining from smoking) or hold the past fixed when varying her physical act (as CDT does, two-boxing and smoking).

**A-FDT** rejects this equivalence by appealing to a precommitment test (Yudkowsky 2010; Burgess 2004). If a CDT agent were offered a binding precommitment to one-box *before* the predictor made her prediction, the CDT agent would gladly accept; if offered a binding precommitment to refrain from smoking *before* the cancer metastasized, the CDT agent would decline. The relevant asymmetry is mechanistic: Newcomb’s predictor constructs an accurate predictive model or simulation of the agent’s decision-making algorithm, whereas an arterial lesion does not simulate or evaluate how the agent reasons.

Yudkowsky and Soares formalize this asymmetry through **subjunctive dependence** (Sec. 3). When two physical systems compute the same mathematical function on the same inputs—such as two reliable calculators on opposite sides of the globe computing $6288 + 1048 = 7336$, or an agent and her psychological twin in a prisoner's dilemma executing the same decision algorithm, or an agent and a predictor’s mental simulation of that agent—their physical outputs are logically constrained to covary insofar as neither system malfunctions. Using Peirce’s (1934) type-token distinction, CDT intervenes only on the physical *token* ("my body executes action $a$ at time $t$"), holding all other physical instantiations of the same algorithm fixed. **A-FDT**, by contrast, intervenes on the mathematical *type* ("this decision function outputs $a$ on this input"). As the authors summarize the analogy:

> *"Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."* (Yudkowsky and Soares 2017, Sec. 3)

Physical causation is a special case of subjunctive dependence: if a scribe in Paris copies the output of a calculator, the scribe's notes depend both causally and subjunctively on the calculator's output. Conversely, mere statistical correlation or a non-computational common cause (such as two calculators coincidentally painted pink, or a carcinogenic lesion) entails no subjunctive dependence on the output of the decision function.

Because a mathematical function $f$ on a fixed input $z$ necessarily yields a single logical output, asking "What would happen if $f(z)$ output $a'$ instead of $a$?" requires evaluating a **counterpossible conditional**—a counterfactual whose antecedent is logically or mathematically impossible (Cohen 1990). Yudkowsky and Soares note that one cannot evade counterpossibilities by switching to a variant theory $\text{FDT}'$ that iterates over candidate functions $f_n \in \mathcal{F}$ and asks "What if I implemented $f_n$ instead of my actual decision function $d \notin \mathcal{F}$?" In Newcomb’s problem, the predictor predicts the actual procedure $d$, so $\text{FDT}'$ only gets the right answer if it imagines a world where predictors of $d$ predict *as if* $d$ behaved like $f_n$—which immediately reintroduces counterpossible reasoning about $d$. Rather than treating counterpossibilities as a philosophical barrier, **A-FDT** treats them as a technical modeling requirement: just as mathematicians routinely reason under uncertainty about logical propositions (e.g., what would follow if the twin prime conjecture were false), a rational decision-maker must track how physical systems that compute or simulate its decision algorithm would behave under alternative logical outputs of that algorithm.

---

## 3. The Formal Machinery of A-FDT

### 3.1 Expected Utility and Epistemic Perspectives

Following Gibbard and Harper (1978) and Joyce (1999), Yudkowsky and Soares cast EDT, CDT, and **A-FDT** within a common expected utility framework. Let $\mathcal{A}$ be a finite set of available actions, $\mathcal{O} = \{o_1, o_2, \dots\}$ be a countable set of outcomes, $\mathcal{X}$ be a countable set of observation histories, and $\mathcal{U}: \mathcal{O} \to \mathbb{R}$ be a bounded utility function. An expected utility maximizer who has received observation history $x \in \mathcal{X}$ selects an action $a \in \mathcal{A}$ that maximizes **Equation (1)**:

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j), \tag{1}$$

where $P(a \hookrightarrow o_j ;\, x)$ denotes the probability assigned to outcome $o_j$ in the **decision hypothetical** $M^{a\hookrightarrow}$ constructed from the agent’s world-model $M$ for action $a$ and observation $x$. Defining the random variable $\textsc{V} \coloneqq \mathcal{U}(\textsc{Outcome})$ and writing $\mathbb{E}$ for expectation with respect to the agent's probability distribution $P$, the competing decision theories differ solely in how they represent the world-model $M$ and how they construct the hypothetical distribution $P(- \hookrightarrow - ;\, x)$ from $M$:

- **Evidential Decision Theory (EDT)** represents the world-model simply as a Bayesian probability distribution $P$ and constructs hypotheticals via standard conditionalization (**Equation (2)**):
  $$\mathrm{EDT}(P, x) \coloneqq \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs} = x, \textsc{Act} = a\right). \tag{2}$$
- **Causal Decision Theory (CDT)**, formalized using Pearl’s (1996, 2000) graphical causal models, represents the world-model as a pair $(P, G)$, where $G$ is a directed graph encoding physical causal dependencies among the variables of $P$. CDT constructs hypotheticals by conditioning on the observation $\textsc{Obs} = x$ and applying Pearl’s $\mathtt{do}$-operator to the physical action variable $\textsc{Act}$ (**Equation (3)**):
  $$\mathrm{CDT}(P, G, x) \coloneqq \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{Act} = a), \textsc{Obs} = x\right). \tag{3}$$
  Here, $\mathtt{do}(\textsc{Act} = a)$ severs all incoming arrows into $\textsc{Act}$ in $G$, sets $\textsc{Act} = a$, and propagates the update strictly along outgoing causal paths downstream of $\textsc{Act}$, leaving all causally upstream or non-descendant variables untouched.

### 3.2 Equation (4): The Primary Formal Definition of A-FDT

In principle, if one possessed a formal counterpossible update operator $\mathtt{true}(\phi)$ capable of conditioning a probability distribution $P$ directly on a logical sentence $\phi$, one could define an idealized functional decision procedure $\mathrm{FDT}^*(P, x) = \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}(\textsc{V} \mid \mathtt{true}(\textsc{fdt}(\underline{P}, \underline{x}) = a))$. Because no general mathematical definition of $\mathtt{true}(\phi)$ currently exists for counterpossible antecedents, Yudkowsky and Soares instead augment the probability distribution $P$ with a dependency graph $G$ that encodes not only physical causation, but also logical, mathematical, and computational subjunctive dependencies. Applying Pearl’s $\mathtt{do}$-calculus to this augmented graph yields **Equation (4)** of Section 5, our primary formal definition of **A-FDT**:

$$\mathrm{FDT}(P, G, x) \coloneqq \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right). \tag{4}$$

In the terminology of this essay, Equation (4) defines the **A-FDT** decision rule, which we write equivalently as $\mathrm{A\text{-}FDT}(P, G, x)$. To apply Equation (4) accurately, four formal features require close attention:

1. **Logical Variables and Dequoting ($\underline{P}, \underline{G}, \underline{x}$):** In an **A-FDT** model $(P, G)$, the sample space of $P$ and vertex set of $G$ include variables representing the outputs of mathematical functions (for example, a variable for $6288 + 1048$). The underline notation denotes *dequoting* (syntactic substitution of values into variable identifiers): if $x \coloneqq 3$, then $\textsc{Z}\underline{x}$ denotes the variable name $\textsc{Z}3$. Thus, $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ is a specific node in $G$ representing the logical output of the **A-FDT** function when evaluated on the specific inputs $(P, G, x)$.
2. **Harmless Self-Reference via Quining:** Because the node name $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ inside $G$ refers to $P$ and $G$ themselves, the model is self-referential. As Yudkowsky and Soares point out, Kleene’s (1938) second recursion theorem guarantees that computational data structures can contain and manipulate exact representations of themselves via *quining*. Crucially, the agent does not need to know the *output value* $\mathrm{A\text{-}FDT}(P, G, x)$ in advance in order to include an uninstantiated *random variable* $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ in $(P, G)$ and perform graph surgery on it.
3. **Updateless Response to Observations ($x$):** Compare Equation (3) for CDT with Equation (4) for **A-FDT**. When a CDT agent observes $x$, she conditions her probability distribution on $\textsc{Obs} = x$. When an **A-FDT** agent observes $x$, **she does not condition $P$ on $\textsc{Obs} = x$**. Instead, she responds to changing her observation from $x$ to $y$ by *changing the node in $G$ upon which she intervenes*—switching from $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)$ to $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{y}) = a)$ while taking the expectation over the prior distribution $P$. (As the authors note in Section 9, this feature is inherited from Wei Dai’s 2009 *Updateless Decision Theory* [UDT], whereas Eliezer Yudkowsky’s 2010 *Timeless Decision Theory* [TDT] both conditioned on $\textsc{Obs} = x$ and intervened on the logical node, creating a harmful "double update.")
4. **Why Equation (4) Is Specifically *Action* FDT (A-FDT):** In Footnotes 7 and 16, the authors distinguish Equation (4) from what we may call *policy functional decision theory* (P-FDT). In P-FDT, the agent intervenes on an observation-independent node $\textsc{fdt}(\underline{P}, \underline{G}) = \pi$ to select an entire policy $\pi: \mathcal{X} \to \mathcal{A}$ and then executes $\pi(x)$. In **A-FDT** (Equation 4), by contrast, the agent maximizes directly over individual *actions* $a \in \mathcal{A}$ by intervening on the single observation-indexed node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ corresponding to her actual observation $x$, while leaving nodes $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x'})$ for counterfactual observations $x' \neq x$ untouched at their prior distributions in $P$.

When all correlations between $\textsc{Act}$ and other variables in $(P, G)$ are physically caused by $\textsc{Act}$ (except for $\textsc{Act}$'s own dependence on $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$), EDT, CDT, and **A-FDT** coincide:
$$\mathbb{E}[\textsc{V} \mid a] = \mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{Act}=a)] = \mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})=a)].$$
They diverge precisely when non-causal correlations exist between the agent's action and the environment.

---

## 4. Applying A-FDT: Worked Mathematical Examples

To see how **A-FDT** evaluates actions in practice, we follow Yudkowsky and Soares (Sec. 6–9) by constructing explicit graphical models $(P^F, G^F)$ for an **A-FDT** agent ("Fiona") and contrasting her calculations with an EDT agent ("Eve") and a CDT agent ("Carl").

### 4.1 Static Prediction and Dominance: Newcomb’s Problem and Death in Damascus

In Newcomb’s problem (where no mid-game observation $x$ occurs, so we write $\textsc{fdt}(\underline{P^F}, \underline{G^F})$), Fiona’s dependency graph $G^F$ has the following structure:
- Exogenous nodes: $\textsc{fdt}(\underline{P^F}, \underline{G^F}) \in \{\textit{onebox}, \textit{twobox}\}$ (intervention target) and $\textsc{Accurate} \in \{\textit{accurate}, \textit{inaccurate}\}$ with $P^F(\textsc{Accurate} = \textit{accurate}) = 0.99$.
- Structural equations:
  $$\textsc{Act} = \textsc{fdt}(\underline{P^F}, \underline{G^F}),$$
  $$\textsc{Prediction} = \begin{cases} \textsc{fdt}(\underline{P^F}, \underline{G^F}) & \text{if } \textsc{Accurate} = \textit{accurate}, \\ \neg\textsc{fdt}(\underline{P^F}, \underline{G^F}) & \text{if } \textsc{Accurate} = \textit{inaccurate}, \end{cases}$$
  $$\textsc{Box B} = \begin{cases} \textit{full} \;(\$1,000,000) & \text{if } \textsc{Prediction} = \textit{onebox}, \\ \textit{empty} \;(\$0) & \text{if } \textsc{Prediction} = \textit{twobox}, \end{cases}$$
  $$\textsc{V} = \textsc{Box B} + \mathbb{I}(\textsc{Act} = \textit{twobox}) \cdot \$1,000.$$

Notice how $G^F$ differs from Carl’s causal graph $G^C$. Both graphs look like a common-cause fork, where a top node points to both $\textsc{Act}$ and $\textsc{Prediction}$. However, Carl’s top node is a physical state $\textsc{Predisposition}$, and Carl intervenes downstream on $\textsc{Act}$ via $\mathtt{do}(\textsc{Act} = a)$, severing the link between $\textsc{Act}$ and $\textsc{Predisposition}$. Consequently, Carl holds $P^C(\textsc{Box B} = \textit{full}) = p$ constant across both hypotheticals, concluding that $\textit{twobox}$ yields $p(\$1,001,000) + (1-p)(\$1,000)$, which exceeds $\textit{onebox}$ by $\$1,000$ for every $p \in [0,1]$.

Fiona, applying **A-FDT** (Equation 4), intervenes at the root of the fork on $\textsc{fdt}(\underline{P^F}, \underline{G^F})$. Propagating $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \textit{onebox})$ down both branches yields $\textsc{Act} = \textit{onebox}$ with probability $1$ and $\textsc{Box B} = \textit{full}$ with probability $0.99$:
$$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \textit{onebox}\right)\right] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000.$$
Propagating $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \textit{twobox})$ down both branches yields $\textsc{Act} = \textit{twobox}$ with probability $1$ and $\textsc{Box B} = \textit{full}$ with probability $0.01$:
$$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \textit{twobox}\right)\right] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$
Since $\$990,000 > \$11,000$, $\mathrm{A\text{-}FDT}(P^F, G^F) = \textit{onebox}$. Notice that this calculation is entirely independent of Fiona’s prior $P^F(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \textit{onebox})$, because the $\mathtt{do}$-operator overrides the prior on the intervened node. Even once Fiona deduces that she will one-box and is $99\%$ certain box B is already full, she does not switch to two-boxing: under **A-FDT**, imagining two-boxing requires imagining the counterpossible world where $\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \textit{twobox}$, in which box B is $99\%$ likely to be empty.

This also shows why **A-FDT** rejects the traditional dominance argument for two-boxing (Sec. 6). Dominance is always relative to a choice of counterfactuals. Holding fixed the exogenous variable $\textsc{Accurate}$ rather than $\textsc{Box B}$, switching the functional output from $\textit{onebox}$ to $\textit{twobox}$ changes the agent's payoff from $\$1,000,000$ to $\$1,000$ when $\textsc{Accurate} = \textit{accurate}$ ($99\%$ of the time). Relative to subjunctive dependencies, **A-FDT** never takes a dominated action.

The payoff of preserving predictive dependencies becomes even starker in **Death in Damascus** (Gibbard and Harper 1978; Yudkowsky and Soares 2017, Sec. 8). Death perfectly predicts whether the agent will stay in $\textit{damascus}$ (cost $\$0$) or flee to $\textit{aleppo}$ (cost $\$1,000$), and waits at the predicted city to claim the agent's life (losing $\$1,000,000$). Under **A-FDT**, $\textsc{DeathLocation} = \textsc{fdt}(\underline{P^F}, \underline{G^F})$. Intervening on $\textsc{fdt}(\underline{P^F}, \underline{G^F})$ yields:
$$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \textit{damascus}\right)\right] = \$0, \qquad \mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \textit{aleppo}\right)\right] = -\$1,000.$$
Fiona immediately stays in Damascus. Furthermore, if offered a *truly random* physical coin for $\$1$ whose flip cannot be predicted by Death (giving a $50\%$ survival rate, worth $\$500,000 - \$1 = \$499,999$), Fiona immediately buys it. Carl, by contrast, treats $\textsc{DeathLocation}$ as causally independent of $\textsc{Act}$. If Carl believes he will stay in Damascus ($p > 0.5$), CDT tells him to flee to Aleppo; if he believes he will flee, CDT tells him to stay. Even if Carl adopts Joyce’s (2012) ratification procedure—settling into a mixed belief state $P^C(\textit{damascus}) = 0.5005$ and $P^C(\textit{aleppo}) = 0.4995$ where both CDT counterfactuals yield an imagined expected utility of $\$500,500$—Carl’s CDT hypotheticals delude him into evaluating his baseline survival odds at $50.05\%$, causing him to *reject* the $\$1$ truly random coin that would actually save his life $50\%$ of the time!

### 4.2 Non-Predictive Common Causes: The Smoking Lesion Problem

How does **A-FDT** avoid EDT’s mistake in the smoking lesion problem? Here, the lesion does not simulate the **A-FDT** algorithm; rather, it alters the agent’s physical preferences. Yudkowsky and Soares (Sec. 6) formalize this by introducing two utility functions: $\mathcal{U}_S$ (which values smoking at $+\$1,000$, held by agents with the lesion) and $\mathcal{U}_R$ (which values smoking at $-\$1$, held by agents without the lesion). Correspondingly, there are two possible probability distributions $P_S^F$ and $P_R^F$, and two distinct functional nodes in Fiona’s graph $G^F$: $\textsc{fdt}(\underline{P_S^F}, \underline{G^F})$ and $\textsc{fdt}(\underline{P_R^F}, \underline{G^F})$.

Because Fiona cannot directly observe whether she has the lesion, she lacks introspective access to which distribution she is running, though her actual evaluation when afflicted with the lesion uses $P_S^F$. In $G^F$, the exogenous node $\textsc{Lesion} \in \{\textit{lesion}, \textit{nolesion}\}$ (with prior $P_S^F(\textsc{Lesion} = \textit{lesion}) = p \in (0,1)$) and $\textsc{Luck} \in \{\textit{unlucky}, \textit{lucky}\}$ ($P_S^F(\textit{unlucky}) = 0.99$) govern cancer and physical action via:
$$\textsc{Act}\left(\textsc{Lesion}, s, r\right) = \begin{cases} s & \text{if } \textsc{Lesion} = \textit{lesion}, \\ r & \text{if } \textsc{Lesion} = \textit{nolesion}, \end{cases}$$
where $s = \textsc{fdt}(\underline{P_S^F}, \underline{G^F})$ and $r = \textsc{fdt}(\underline{P_R^F}, \underline{G^F})$. Crucially, there is **no arrow** from $\textsc{fdt}(\underline{P_S^F}, \underline{G^F})$ or $\textsc{fdt}(\underline{P_R^F}, \underline{G^F})$ to $\textsc{Lesion}$ or $\textsc{Cancer}$.

Let $q \coloneqq P_S^F(\textsc{fdt}(\underline{P_R^F}, \underline{G^F}) = \textit{smoke})$ denote Fiona’s prior probability that her non-lesion counterpart smokes. When Fiona (having the lesion, and thus running $\mathrm{A\text{-}FDT}(P_S^F, G^F)$) intervenes on $\textsc{fdt}(\underline{P_S^F}, \underline{G^F})$, the probability of $\textsc{Lesion} = \textit{lesion}$ remains invariant at $p$:
$$P_S^F(\textit{lesion}) = P_S^F\left(\textit{lesion} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P_S^F}, \underline{G^F}) = \textit{smoke}\right)\right) = P_S^F\left(\textit{lesion} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P_S^F}, \underline{G^F}) = \textit{refrain}\right)\right) = p.$$
If $\textsc{Lesion} = \textit{lesion}$ (probability $p$), her survival probability is $0.01$ (expected life utility $\$10,000$) and her action is controlled by the intervened variable $\textsc{fdt}(\underline{P_S^F}, \underline{G^F})$. If $\textsc{Lesion} = \textit{nolesion}$ (probability $1-p$), her survival probability is $0.99$ (expected life utility $\$990,000$) and her action is controlled by the untouched variable $\textsc{fdt}(\underline{P_R^F}, \underline{G^F})$, which yields expected smoking utility $q \cdot \$1,000$ under $\mathcal{U}_S$. Thus, under **A-FDT**:
$$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P_S^F}, \underline{G^F}) = \textit{smoke}\right)\right] = p(\$10,000 + \$1,000) + (1-p)(\$990,000 + q \cdot \$1,000),$$
$$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P_S^F}, \underline{G^F}) = \textit{refrain}\right)\right] = p(\$10,000) + (1-p)(\$990,000 + q \cdot \$1,000).$$
Subtracting the two expectations, the $(1-p)$ terms cancel identically, leaving a strict net advantage of $p \cdot \$1,000 > 0$ for $\textit{smoke}$. Thus $\mathrm{A\text{-}FDT}(P_S^F, G^F) = \textit{smoke}$.

### 4.3 Dynamic Observations and Extortion: Transparent Newcomb, Parfit’s Hitchhiker, and Blackmail

The most distinctive feature of **A-FDT** emerges when an agent makes an observation $x$ that was itself caused by a predictor’s prediction of how the agent would react to $x$. Consider the **Transparent Newcomb Problem** (Drescher 2006; Yudkowsky and Soares 2017, Sec. 4 & 6), which is decision-theoretically isomorphic to **Parfit’s Hitchhiker** (Parfit 1986) and **The Mechanical Blackmail** (Soares and Fallenstein 2015; Yudkowsky and Soares 2017, Sec. 9). Both boxes are transparent. The $99\%$-accurate predictor places $\$1,000,000$ in box B if and only if she predicts that *upon observing that box B is full* ($\textsc{Obs} = \textit{full}$), the agent will one-box.

Suppose the agent sees $\textsc{Obs} = \textit{full}$. Both CDT and EDT prescribe two-boxing: once $\textsc{Obs} = \textit{full}$ is conditioned upon, box B is guaranteed to contain $\$1,000,000$, so two-boxing yields $\$1,001,000$ whereas one-boxing yields $\$1,000,000$. Predictors foresee this and leave box B empty (or leave CDT and EDT hitchhikers to die in the desert).

How does **A-FDT** evaluate $\mathrm{A\text{-}FDT}(P^F, G^F, \textit{full})$? In Fiona’s graph $G^F$ (Fig. 5b of the source), there are two functional nodes corresponding to the two possible observations: $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full})$ and $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty})$. Because the predictor specifically predicts what Fiona will do *if she sees a full box*, $\textsc{Prediction}$ depends only on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full})$ and $\textsc{Accurate}$:
$$\textsc{Prediction} = \begin{cases} 1 \;(\text{fill Box B}) & \text{if } (\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full}) = \textit{onebox} \land \textsc{Accurate} = \textit{accurate}) \\ & \quad \lor (\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full}) = \textit{twobox} \land \textsc{Accurate} = \textit{inaccurate}), \\ 2 \;(\text{leave Box B empty}) & \text{otherwise.} \end{cases}$$
Meanwhile, Fiona’s physical action $\textsc{Act}$ is a multiplexer controlled by $\textsc{Prediction}$ (which determines whether she sees $\textit{full}$ or $\textit{empty}$):
$$\textsc{Act} = \begin{cases} \textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full}) & \text{if } \textsc{Prediction} = 1, \\ \textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty}) & \text{if } \textsc{Prediction} = 2. \end{cases}$$

When Fiona sees $\textsc{Obs} = \textit{full}$, **A-FDT** (Equation 4) instructs her to intervene on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full})$ **without conditioning on $\textsc{Obs} = \textit{full}$**. (Note: In Section 6 of the source paper, an unclosed display expression briefly writes $\mathbb{E}(\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full}) = a, \textsc{Obs} = \textit{full})$, which is a typographical slip in the source text; as Equations (4), Figure 5b, and the authors' immediately following arithmetic confirm, **A-FDT** does not condition on $\textsc{Obs} = \textit{full}$.)

Let $q \coloneqq P^F(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty}) = \textit{twobox})$ be Fiona’s prior probability that she two-boxes upon seeing an empty box.
- **Case 1: $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full}) = \textit{onebox})$.** With probability $0.99$ ($\textsc{Accurate} = \textit{accurate}$), $\textsc{Prediction} = 1$, so $\textsc{Box B} = \textit{full}$, Fiona sees $\textit{full}$, executes $\textsc{Act} = \textit{onebox}$, and receives $\$1,000,000$. With probability $0.01$ ($\textsc{Accurate} = \textit{inaccurate}$), $\textsc{Prediction} = 2$, so $\textsc{Box B} = \textit{empty}$, Fiona actually sees an *empty* box, executes $\textsc{Act} = \textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty})$, and receives $q \cdot \$1,000$ in expectation:
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full}) = \textit{onebox}\right)\right] = 0.99(\$1,000,000) + 0.01(q \cdot \$1,000) = \$990,000 + \$10q.$$
- **Case 2: $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full}) = \textit{twobox})$.** With probability $0.01$ ($\textsc{Accurate} = \textit{inaccurate}$), the predictor errs and fills box B anyway ($\textsc{Prediction} = 1$), so Fiona sees $\textit{full}$, executes $\textsc{Act} = \textit{twobox}$, and receives $\$1,001,000$. With probability $0.99$ ($\textsc{Accurate} = \textit{accurate}$), the predictor predicts her two-boxing and leaves box B empty ($\textsc{Prediction} = 2$), so in this hypothetical scenario Fiona does *not* see $\textit{full}$, executes $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty})$, and receives $q \cdot \$1,000$:
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full}) = \textit{twobox}\right)\right] = 0.01(\$1,001,000) + 0.99(q \cdot \$1,000) = \$10,010 + \$990q.$$

For every $q \in [0, 1]$, $\$990,000 + \$10q > \$10,010 + \$990q$. Thus $\mathrm{A\text{-}FDT}(P^F, G^F, \textit{full}) = \textit{onebox}$. Even while staring directly at a full box B (or holding a mechanical blackmail letter, or standing safely at an ATM in Parfit’s city), an **A-FDT** agent evaluates options from a **global perspective**: she asks what the whole universe would look like if her decision algorithm for the current observation output a different action, including the fact that she would almost certainly have received a *different observation*.

Crucially, this global perspective does *not* make **A-FDT** gullible to spurious correlations between observations and preexisting catastrophes. In **The XOR Blackmail** (Soares and Fallenstein 2015; Yudkowsky and Soares 2017, Sec. 7), an honest predictor knows whether the agent's house already has a $\$1,000,000$ termite infestation ($\textsc{Infestation}$) and sends a letter demanding $\$1,000$ if and only if $(\neg\textsc{Infestation} \land \textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{letter}) = \textit{pay}) \lor (\textsc{Infestation} \land \textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{letter}) = \textit{refuse})$. Eve (following EDT) conditions on $\textsc{Obs} = \textit{letter}$ and $\textsc{Act} = \textit{pay}$, which drives her conditional probability of termites to $0$, so she pays the blackmailer. Fiona (following **A-FDT**) intervenes on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{letter})$ in her graph $G^F$ (Fig. 6b of the source). Because $\textsc{Infestation}$ is causally and subjunctively upstream of both the predictor and $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{letter})$, varying $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{letter})$ changes whether the predictor *sends the letter*, but leaves $P^F(\textsc{Infestation} = \textit{termites})$ completely unchanged. Thus, Fiona refuses to pay.

---

## 5. Deciding Unfamiliar Cases: Open Questions and Operational Proposals

Suppose a researcher or engineer wants to apply **A-FDT** to a brand-new decision problem. What follows directly from Yudkowsky and Soares (2017), and where are additional operational assumptions required?

From the source text, the core **A-FDT** procedure for any decision problem with observation $x \in \mathcal{X}$ and action space $\mathcal{A}$ is:
1. Formulate a probability distribution $P$ and dependency graph $G$ containing nodes $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x'})$ for each relevant observation history $x' \in \mathcal{X}$.
2. Connect each $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x'})$ with directed edges to any physical variable (including the agent’s physical action $\textsc{Act}$ and any external predictor, twin, or simulator) whose behavior subjunctively depends on what the decision procedure outputs on input $(P, G, x')$.
3. Upon observing $x$, do *not* condition $P$ on $\textsc{Obs} = x$; instead, compute $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)]$ for each $a \in \mathcal{A}$ and execute the action $a^*$ that maximizes this expectation.

However, the source paper explicitly leaves three foundational and implementation questions open. Below, we explain each uncertainty in the source text and develop a concrete operational proposal of our own to make **A-FDT** fully executable on unfamiliar cases.

### 5.1 Open Question 1: Constructing the Subjunctive Graph $G$

**What the source states:** In Section 5, Yudkowsky and Soares emphasize that Equation (4) works *given* an accurate subjunctive dependency graph $G$, but note that while Pearl (2000) provides a rigorous methodology for deducing physical causal graphs from observation and physical interventions, *"no such formal treatment has yet been given to the problem of deducing the structure of other kinds of subjunctive dependence."* How, then, should a practitioner decide which edges to draw from $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ in a novel environment?

**Operational proposal (Mechanistic Simulation Factorization):** While a complete logic of counterpossibilities remains an open research problem, we can operationalize the construction of $G$ in decision-theoretic applications by starting with a standard physical causal DAG $G_{\text{phys}}$ and applying a structural factorization rule:
1. Identify every physical mechanism $M_k$ in $G_{\text{phys}}$ (e.g., the agent’s own brain/hardware, a twin’s brain, or a predictor’s simulation algorithm) that computes or estimates the output of the agent’s decision procedure under some modeled input state $(P, G, x')$.
2. Introduce the logical parent node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x'})$ and replace the deterministic or stochastic mapping inside $M_k$ with a noisy channel controlled by an exogenous fidelity variable $\textsc{Accurate}_k \in \{0, 1\}$ (with accuracy parameter $\alpha_k \in [0, 1]$) and an independent error distribution $E_k$:
   $$M_k = \textsc{Accurate}_k \cdot \textsc{fdt}(\underline{P}, \underline{G}, \underline{x'}) + (1 - \textsc{Accurate}_k) \cdot E_k.$$
3. Any physical variable $Z$ in $G_{\text{phys}}$ that does *not* execute, simulate, or causally descend from such a predictive mechanism $M_k$ (such as $\textsc{Lesion}$ or $\textsc{Infestation}$) receives no directed path from $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x'})$.

This operational rule reduces the philosophical question of subjunctive dependence to an empirical question about physical mechanisms: does system $M_k$ algorithmically simulate or replicate the agent's decision function on input $x'$ with fidelity $\alpha_k > 0$? If $\alpha_k = 0$ (pure statistical coincidence or a non-simulating common cause), the outgoing edge from $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x'})$ to $M_k$ vanishes.

### 5.2 Open Question 2: Unvisited Branch Priors ($q$) and Multi-Branch Predictors in A-FDT

**What the source states:** In Section 6, when analyzing the smoking lesion problem and the transparent Newcomb problem under **A-FDT**, the graph $G^F$ contains secondary functional nodes—such as $\textsc{fdt}(\underline{P_R^F}, \underline{G^F})$ or $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty})$—that are *not* intervened upon when the agent computes $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full}) = a)$. Yudkowsky and Soares assign a prior probability $q$ to these unvisited nodes and point out that in those two dilemmas, the exact value of $q$ does not affect the optimal action (while noting in parentheticals that the "correct" values are $q=0$ and $q=1$, respectively). Furthermore, in Footnotes 7 and 16, they remark without formal detail that iterating over *actions* (**A-FDT**, Equation 4) rather than *policies* (P-FDT) makes a difference in certain dilemmas.

**Mathematical analysis and operational proposal:** In unfamiliar dilemmas, two complications can arise for Equation (4) that do not arise in standard Newcomb:

First, **the value of the unvisited branch prior $q$ can change the optimal action at the visited branch $x$**. Suppose we modify the Transparent Newcomb problem into an **Insurance Dilemma**: if the predictor predicts the agent will choose action $a_1$ upon seeing $\textit{full}$, the predictor gives the agent $\$100$ and shows her $\textit{full}$ (where $a_1$ costs $\$0$ and $a_2$ pays $+\$10$). If the predictor predicts the agent will choose $a_2$ upon seeing $\textit{full}$, the predictor instead diverts the agent to observation $\textit{empty}$, where the agent faces a bomb: taking action $b_1$ at $\textit{empty}$ defuses the bomb for a payoff of $\$200$, whereas taking $b_2$ at $\textit{empty}$ detonates it for $-\$1,000$.
If the agent observes $\textit{full}$ and applies **A-FDT** (Equation 4) with a perfectly accurate predictor:
$$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \textit{full}) = a_1\right)\right] = \$100,$$
$$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \textit{full}) = a_2\right)\right] = q(\$200) + (1-q)(-\$1,000),$$
where $q = P(\textsc{fdt}(\underline{P}, \underline{G}, \textit{empty}) = b_1)$. Here, whether $a_1$ or $a_2$ is optimal at $\textit{full}$ depends entirely on $q$! If the agent left $q$ as an uncalibrated prior (say, $q = 0.5$, yielding $-\$400 < \$100$), she would choose $a_1$, even though if she actually reached $\textit{empty}$, **A-FDT** would obviously defuse the bomb ($\mathrm{A\text{-}FDT}(P, G, \textit{empty}) = b_1 \implies q = 1$, yielding $\$200 > \$100$).

To make **A-FDT** well-defined when unvisited branches affect the current expectation, we propose an explicit **Self-Consistent Branch Calibration Rule**: before evaluating Equation (4) at $x$, the prior distribution $P$ over any other functional node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x'})$ ($x' \neq x$) must be recursively calibrated (via backward induction or fixed-point iteration) so that $P(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x'}) = \mathrm{A\text{-}FDT}(P, G, x')) = 1$ (up to small logical uncertainty $\epsilon \to 0$).

Second, **what if a predictor’s action depends jointly on multiple observation branches?** This reveals the exact mathematical boundary between **A-FDT** (Equation 4) and policy-based P-FDT. Consider a **Cross-Branch Coordination Game**: nature flips a fair coin $C \in \{H, T\}$ and shows the outcome ($x \in \{H, T\}$) to the agent. Before the coin is flipped, a perfect predictor simulates what the agent would do on *both* branches—i.e., she inspects both $\textsc{fdt}(\underline{P}, \underline{G}, H)$ and $\textsc{fdt}(\underline{P}, \underline{G}, T)$—and deposits $\$1,000,000$ into the agent’s account if and only if *both* branches output action $\textit{C}$ (cooperate), whereas choosing $\textit{D}$ (defect) on the realized branch saves the agent $\$1,000$ in effort.
Suppose the agent observes $x = H$ and uses **A-FDT** (Equation 4). Because **A-FDT** intervenes *only* on the single node $\textsc{fdt}(\underline{P}, \underline{G}, H)$ while holding $\textsc{fdt}(\underline{P}, \underline{G}, T)$ fixed at its prior probability $q = P(\textsc{fdt}(\underline{P}, \underline{G}, T) = \textit{C})$, the **A-FDT** expectation is:
$$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, H) = \textit{C}\right)\right] = q \cdot \$1,000,000 + \frac{1}{2}(0) + \frac{1}{2}(1-q)(\$1,000),$$
$$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, H) = \textit{D}\right)\right] = \$0 + \frac{1}{2}(\$1,000) + \frac{1}{2}(1-q)(\$1,000).$$
Here, if $q = 0$ (i.e., the agent believes her $T$-branch self will defect), then under **A-FDT** the $H$-branch self *also* defects ($\textit{D}$ yields $\$1,000$ vs. $\$500$ for $\textit{C}$), so $(D, D)$ is a self-consistent trap for **A-FDT** unless $q > 0.0005$! By contrast, a policy-based P-FDT agent who intervenes simultaneously on the full policy $\pi = (\pi(H), \pi(T))$ directly compares $\pi = (C, C)$ (payoff $\$1,000,000$) against $(D, D)$ (payoff $\$1,000$) and uniquely selects $(C, C)$ regardless of priors. In an unfamiliar problem where a predictor conditions jointly on multiple observation branches, an **A-FDT** practitioner must either couple the branch nodes subjunctively or elevate the intervention to the policy level.

### 5.3 Open Question 3: Individuation of Functional Nodes Across Imperfect Twins and Time

**What the source states:** In Section 10, Yudkowsky and Soares apply their framework informally to two practical settings: (i) a voting coalition of ten agents who each pay $\$1,000$ to vote and win $\$1,000,000$ if all ten vote, and (ii) an agent deciding whether to go to the gym today (cost $\$1,000$) when getting fit (worth $\$1,000,000$) requires going to the gym dozens of times over future weeks. The authors state that "[i]f there are no relevant differences between her decision today versus tomorrow, then she should assume that she will continue going to the gym in the future if she goes today."

**Mathematical tension and operational proposal:** Look closely at the syntactic indexing in Equation (4): the intervened node is $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$. In the gym problem on Tuesday ($t=1$) versus Thursday ($t=2$), the agent’s total observation history $x_1$ is *not* bit-for-bit identical to $x_2$ (at minimum, she sees a different calendar date and remembers having gone to the gym on Tuesday). Likewise, ten voters in ten different rooms have distinct sensory histories $x^{(1)}, \dots, x^{(10)}$. If $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_1})$ and $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_2})$ are treated as independent nodes in $G$ whenever $x_1 \neq x_2$, then intervening on $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_1}) = \textit{gym})$ has *zero* effect on $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_2})$, reducing **A-FDT** to CDT’s failure!

To bridge Equation (4) with the authors' gym and coalition examples, we must introduce an explicit **Decision-Relevant Abstraction Mapping** $\tau(P, G, x)$ as an operational assumption:
1. Partition the agent’s full observation history $x = (x_{\text{rel}}, x_{\text{nuis}})$ into *decision-relevant features* $x_{\text{rel}} = \tau(x)$ (the payoff matrix and strategic structure of the dilemma) and *nuisance features* $x_{\text{nuis}}$ (the calendar date, room number, or player index).
2. Index the functional node in Equation (4) by the equivalence class $\textsc{fdt}(\underline{P}, \underline{G}, \underline{\tau(x)})$, or equivalently, connect $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_1})$ to the actions $A_2, \dots, A_K$ of future selves or coalition partners via structural equations of the form:
   $$P\left(A_k = a \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_1}) = a\right)\right) = \rho_k + (1 - \rho_k) P_0(A_k = a),$$
   where $\rho_k \in [0, 1]$ measures the **subjective algorithmic similarity** (the probability that agent/self $k$ shares the same abstracted decision function on the same equivalence class $\tau(x)$).

With this parameterization, the gym dilemma and $K$-player voting coalition become quantitatively solvable under **A-FDT**: if getting fit requires all $K$ temporal selves to attend the gym (worth $M = \$1,000,000$ at cost $c = \$1,000$ per visit) and each future self shares subjunctive correlation $\rho$ with today’s functional output (with baseline attendance probability $0$ otherwise), then intervening via $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{\tau(x)}) = \textit{gym})$ yields expected utility $\rho^{K-1} M - c$, compared to $\$0$ for skipping. Thus, **A-FDT** prescribes going to the gym (or voting) whenever $\rho > (c/M)^{1/(K-1)}$.

---

## 6. Conclusion

**Action functional decision theory (A-FDT)**, as formalized in Equation (4) of Yudkowsky and Soares (2017), resolves a foundational impasse in decision theory through a remarkably compact modification of Pearl’s causal decision calculus. By shifting the point of intervention from the physical act $\textsc{Act}$ to the logical output $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ of the agent’s decision algorithm, and by responding to observations $x$ through switching the target of intervention rather than conditioning away counterfactual branches, **A-FDT** captures the strategic benefits of precommitment without requiring physical self-binding. It cooperates with twins, one-boxes in both standard and transparent Newcomb problems, smokes in the smoking lesion problem, stays put in Damascus while appropriately valuing true randomness, and resists blackmail. While a fully general mathematical theory of counterpossible inference remains an open frontier, supplementing Equation (4) with explicit operational rules for mechanistic graph construction, branch calibration, and feature abstraction makes **A-FDT** a rigorous, practical tool for analyzing complex single- and multi-agent decisions.

---

## References

- Ahmed, Arif. 2014. *Evidence, Decision and Causality*. Cambridge University Press.
- Burgess, Simon. 2004. "The Newcomb Problem: An Unqualified Resolution." *Synthese* 138 (2): 261–287.
- Cohen, Daniel. 1990. "On What Cannot Be." In *Truth or Consequences: Essays in Honor of Nuel Belnap*, 123–132. Kluwer Academic Publishers.
- Dai, Wei. 2009. "Towards a New Decision Theory." *Less Wrong*, August 13, 2009.
- Drescher, Gary L. 2006. *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
- Gibbard, Allan, and William L. Harper. 1978. "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, vol. 1, edited by C. A. Hooker, J. J. Leach, and E. F. McClennen. D. Reidel.
- Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Joyce, James M. 2012. "Regret and Instability in Causal Decision Theory." *Synthese* 187 (1): 123–145.
- Kleene, Stephen Cole. 1938. "On Notation for Ordinal Numbers." *Journal of Symbolic Logic* 3 (4): 150–155.
- Nozick, Robert. 1969. "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel*, edited by Nicholas Rescher, 114–146. D. Reidel.
- Parfit, Derek. 1986. *Reasons and Persons*. Oxford University Press.
- Pearl, Judea. 1996. "Causation, Action, and Counterfactuals." In *6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-'96)*, 51–73. Morgan Kaufmann.
- Pearl, Judea. 2000. *Causality: Models, Reasoning, and Inference*. 1st ed. Cambridge University Press.
- Peirce, Charles Sanders. 1934. *Collected Papers of Charles Sanders Peirce*, vol. V: *Pragmatism and Pragmaticism*. Harvard University Press.
- Skyrms, Brian. 1980. *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
- Soares, Nate, and Benja Fallenstein. 2015. "Toward Idealized Decision Theory." arXiv:1507.01986 [cs.AI].
- Yudkowsky, Eliezer. 2010. *Timeless Decision Theory*. The Singularity Institute.
- Yudkowsky, Eliezer, and Nate Soares. 2017. "Functional Decision Theory: A New Theory of Instrumental Rationality." arXiv:1710.05060v2.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Composing A-FDT Explanation**

I'm now focusing on structuring the essay about Action Functional Decision Theory (A-FDT). I'm planning out the sections to ensure the explanation is clear and the math is accessible for a technical audience. The goal is a balance between explaining the core concepts and illustrating application with simple examples. I'm prioritizing clarity for your expert review.


**Refining A-FDT Definition**

I've been drilling down into the specifics, especially focusing on *Equation (4), Section 5* from Soares' paper. I'm unpacking the mathematical definitions to build a clear foundation for explaining A-FDT. The goal is to make sure it's not just a description, but a usable framework. The focus now is on translating the formal presentation into practical terms for the reader, ensuring the essay is both rigorous and accessible.


**Clarifying A-FDT vs. FDT**

I'm now focusing on a critical distinction: A-FDT iterates over actions ($a$), not policies. Equation (4) in the paper is action-based. This has led me to emphasize the naming, using A-FDT consistently in the essay and differentiating it from other decision theories. Where there are ambiguities, I will explain the uncertainty and provide an operational interpretation where possible.


**Analyzing A-FDT Source Details**

I'm now examining the original paper's mathematical specifics, especially Equation (4) and the examples presented. I'm focusing on the philosophical motivation and the concept of subjunctive dependence, specifically differentiating between Evidential and Causal Decision Theory. The plan is to unpack the source's claims from any additional assumptions. My word count target is between 2,400–3,000 words.


**Contrasting Decision Theories**

I'm now deeply contrasting A-FDT with Causal Decision Theory (CDT). I've unpacked why A-FDT excels in scenarios like Newcomb's and the Twin Prisoner's Dilemma but struggles with the Smoking Lesion, Cosmic Ray, and XOR Blackmail problems. Conversely, CDT shines in the latter but falls short in the former. The key seems to be CDT's intervention on the physical "Act" severing causal links and upstream links.


**Defining A-FDT Process**

I'm now focusing on A-FDT as the output of a fixed decision function, not physical actions. I'm unpacking subjunctive dependence: When an agent and a predictor both depend on the same function, their behaviors are subjunctively dependent. Causal dependence is a subset of this. I'm now looking into the formal framework, focusing on Equation 1.


**Formalizing A-FDT Framework**

I'm now examining the formal elements of A-FDT. I'm focusing on defining outcomes ($\mathcal{O}$), actions ($\mathcal{A}$), observation histories ($\mathcal{X}$), and the bounded utility function $\mathcal{U}$. The plan is to clarify the epistemic perspectives of different decision theories and how they construct "hypotheticals" ($M^{a\hookrightarrow}$) from the agent's world-model ($M$). I'm also now analyzing the potential use of an operator, $\mathtt{true}(\phi)$, for counterfactuals.


**Unpacking A-FDT Notation**

I'm now fully focused on unpacking the notation in Equation (4). I'm translating each component of the equation, ensuring a clear and concise explanation for the reader. My goal is to break down the formula and make each element understandable, including world-model *M* (with the DAG), observation history, and the dequoting notation.


**Defining A-FDT Node**

I'm currently focused on the implications of the variable name $\textsc{Z}3$, and how the model $M = (P, G)$ can contain a node like $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ that depends on $P$ and $G$ using the Kleene's second recursion theorem. I'm unpacking how the agent includes a variable representing that output in $G$ and $P$. Also, I am looking at how Equation (4) handles observations and actions.



**Clarifying A-FDT Observation**

I'm now clarifying how A-FDT handles observations. I've realized A-FDT doesn't update its beliefs about *P* or *G* given an observation *x*. Instead, A-FDT changes the target of its intervention. This is a crucial distinction and I'm updating the essay to highlight it with clear examples and the source of the subtle typo.


**Differentiating A-FDT Variants**

I'm now clarifying the distinctions between Action FDT (A-FDT) and Policy FDT (P-FDT), especially around Equation (4) and the agent's intervention point. I'm focusing on contrasting how each theory approaches the selection of actions, with A-FDT maximizing over actions directly, while P-FDT operates on policies. This ensures I address the core differences between the decision theoretic variants.


**Outlining A-FDT Application**

I'm now outlining a step-by-step application of A-FDT, intending to illustrate its use across varied decision scenarios. I'm focusing on providing a clear recipe for the reader, and breaking down example cases like Newcomb's Problem and the Smoking Lesion Problem, focusing on how to construct structural equations, graphs, and calculate expected utilities using A-FDT.


**Analyzing A-FDT Scenarios**

I'm now focusing on specific scenarios where A-FDT handles observations, especially Transparent Newcomb, Parfit's Hitchhiker, and Mechanical Blackmail. I am working on how A-FDT intervenes on `fdt(P, G, x)` when it observes 'full' and how that affects predictions. This includes how the `fdt` function impacts the prediction of actions, using the examples as practical demonstrations.



**Evaluating A-FDT Scenarios**

I'm now calculating utilities in scenarios like "full box" Newcomb's problem, comparing A-FDT, TDT, CDT, and EDT. I'm focusing on the math for each theory, showing how A-FDT's decision function leads to different expected values, especially in adversarial prediction. I'm also examining the implications of conditional updates and how A-FDT handles adversarial prediction.


**Identifying A-FDT Open Questions**

I'm now focusing on open questions in the A-FDT source, specifically, how to construct the subjunctive graph G, and how A-FDT handles adversarial prediction with observations. The goal is to list and analyze the uncertainties left by the source and clarify the implementation details. I also need to distinguish the source claims.



**Proposing Graph Construction Rules**

I'm now focused on the practical application and algorithmization of A-FDT, especially the construction of the subjunctive graph *G*. I'm proposing an "Algorithmic Reduction/Structural Factorization Rule" to guide practitioners. The idea is to begin with a causal DAG representing the physical environment, identifying the decision computations and factoring out the logical variable into a parent node. This strategy addresses the challenge of building the graph.



**Modeling A-FDT Scenarios**

I'm now focusing on modeling scenarios using the A-FDT framework, exploring the intricacies of "intervention only on a single node." I'm also examining the implications for the Smoking Lesion Problem and the role of unvisited nodes, particularly how assigning a prior probability (q) to these nodes affects the overall analysis.


**Analyzing A-FDT Interaction**

I'm now analyzing how A-FDT behaves in complex multi-agent situations, particularly where the prior probability, *q*, on unvisited nodes, *x'*, influences the outcome. I'm also exploring scenarios where a predictor's actions depend on *multiple* observations, and examining the mathematical implications of these complexities in relation to Equation 4, focusing on implementation details.



**Calibrating A-FDT Implementation**

I'm now implementing A-FDT operationally, especially where the prior probability, *q*, on unvisited branches impacts the outcome. I'm focusing on clarifying how Recursive/Fixed-Point Calibration influences *P*. I'm also examining the scenario when predictors condition on multiple observation branches, showing where policy-level intervention is crucial. This provides clarity for where A-FDT works and where it needs refinement, focusing on practical implementation of Equation (4).


**Defining A-FDT Indexing**

I'm now focusing on a practical issue: the exact indexing in Equation (4). The key is to address that bit-for-bit identical observation histories are unlikely between agents, or even temporal selves. Thus, my proposal is to introduce an Equivalence-Class / Feature-Abstraction Mapping $\phi(P, G, x)$ to relate decision-irrelevant differences, bridging the formal equation with informal examples.


**Refining A-FDT Indexing**

I'm now refining the Equivalence-Class / Feature-Abstraction Mapping $\phi(P, G, x)$, clarifying that irrelevant observations should map to the same functional node or induce high logical correlation in $G$. Also, I'm now working to stay within the word count range, targeting 2,500-2,900 words, by adjusting the structure of the essay. I'm introducing A-FDT and setting the stage to resolve the EDT vs. CDT conflict.


**Explaining A-FDT's Framework**

I'm currently working through the sections on A-FDT's formal framework. The essay is focusing on illustrating the epistemic perspective of different decision theories and how they construct hypotheticals. I'm focusing on contrasting EDT, and CDT (using their respective equations) and relating it back to Equation (1). I'm also now analyzing the use of an operator, $\mathtt{true}(\phi)$, for counterfactuals.


**Formalizing A-FDT Decisions**

I'm now fully focused on formally defining A-FDT, starting with its idealized form, $\mathrm{FDT}^*$. I'm highlighting the equation, carefully explaining the dequoting, the self-reference via Kleene's theorem, and contrasting with CDT. I'm unpacking two key structural differences: intervening on the logical output node and handling observations "updatelessly" by altering the node intervened upon. I am differentiating A-FDT from Policy-FDT, which acts on actions directly.


**Illustrating A-FDT Applications**

I'm now writing worked mathematical examples, starting with Newcomb's Problem, Death in Damascus, and Smoking Lesion. I'll show how A-FDT handles these scenarios by illustrating graph structures, structural equations, and utility calculations. I'm contrasting A-FDT's outcomes with CDT's for each problem, highlighting the philosophical implications, especially CDT's reflective instability, and why A-FDT stays grounded.


**Calculating A-FDT Utilities**

I'm working on calculating and contrasting expected utilities across scenarios. I'm focusing on scenarios with conditional updates and adversarial predictions to explain A-FDT's utility outcomes. I am working on the mathematics for each theory, demonstrating why A-FDT's decision function produces different expected values, especially in adversarial situations, as I refine my examples.


**Proposing A-FDT Operational Rules**

I am now focusing on translating the source's claims into operational rules for applying A-FDT. I've begun proposing a *Computational Factorization Rule* to guide the construction of the subjunctive graph $G$. I am also working on calibrating unvisited branches and addressing situations with multi-branch predictors. Finally, I'm proposing an explicit abstraction mapping for functional nodes.


```
