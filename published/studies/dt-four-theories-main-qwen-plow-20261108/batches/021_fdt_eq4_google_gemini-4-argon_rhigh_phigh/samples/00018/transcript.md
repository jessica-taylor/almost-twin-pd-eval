# 021_fdt_eq4_google_gemini-4-argon_rhigh_phigh / 00018

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/0c4878b4-8985-4616-afb3-b08a7f38a72c/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/0c4878b4-8985-4616-afb3-b08a7f38a72c/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Action Functional Decision Theory (A-FDT): Formal Mechanics, Subjunctive Counterfactuals, and Operational Application

## 1. Introduction: The Dilemma of Instrumental Rationality

For nearly half a century, normative decision theory has been divided between two competing accounts of instrumental rationality: **Evidential Decision Theory (EDT)** and **Causal Decision Theory (CDT)**. When evaluated by the average utility their practitioners achieve across decision problems, neither theory dominates the other. EDT outperforms CDT in dilemmas involving predictors and symmetrical agents—such as Newcomb's problem and the psychological twin prisoner's dilemma—where an agent's choice correlates with another actor's prior or causally independent decision (Nozick, 1969; Lewis, 1979; Ahmed, 2014). Conversely, CDT outperforms EDT in dilemmas where an agent's choice is merely a statistical symptom of a prior physical common cause—such as Skyrms's (1980) smoking lesion problem—where EDT irrationally prescribes "managing the news" (Gibbard & Harper, 1978; Lewis, 1981). Worse still, in sequential prediction dilemmas such as Parfit's (1986) hitchhiker problem and Drescher's (2006) transparent Newcomb problem, both CDT and EDT leave the agent impoverished or stranded.

In *Functional Decision Theory: A New Theory of Instrumental Rationality*, Eliezer Yudkowsky and Nate Soares propose a unified framework designed to resolve this impasse. Their central thesis is that rational agency should not be conceptualized as selecting a physical act token in isolation, nor as selecting the action that would be the most auspicious news to learn one took. Instead, rational decision-making treats one's choice as the output of a *fixed mathematical decision function* and asks: *"Which output of this very function would yield the best outcome?"*

While Yudkowsky and Soares note in passing (Footnotes 7 and 16) that their preferred multi-agent generalization optimizes over complete *policies* (mappings from observations to actions), the formal system developed and analyzed throughout their paper optimizes directly over *actions* by intervening on an observation-indexed logical node. In this essay, we examine this formal system—**Action Functional Decision Theory (A-FDT)**—as defined by **Equation (4) in Section 5** of Yudkowsky and Soares's paper. We will unpack its mathematical machinery, explain how it models counterfactuals via subjunctive dependence, demonstrate how to apply it step-by-step to classical and sequential dilemmas, and develop explicit operational proposals for the theoretical questions that the source paper leaves open.

---

## 2. The Formal Framework: From Expected Utility to Equation (4)

Following Gibbard and Harper (1978) and Joyce (1999), EDT, CDT, and A-FDT share a common foundation: all three are expected utility theories. Let $\mathcal{A}$ be a finite set of available actions, $\mathcal{O} = \{o_1, o_2, \dots\}$ be a countable set of outcomes, $\mathcal{X}$ be a countable set of observation histories, and $\mathcal{U}: \mathcal{O} \to \mathbb{R}$ be a bounded utility function. Given an observation history $x \in \mathcal{X}$, an expected utility maximizer selects an action $a \in \mathcal{A}$ that maximizes Equation (1) of the paper:

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j), \tag{1}$$

where $P(a \hookrightarrow o_j ;\, x)$ denotes the subjective probability that outcome $o_j$ will obtain in the hypothetical scenario where action $a$ is executed after observing $x$. As Joyce's (1999) representation theorem establishes, competing decision theories do not disagree about how outcomes are valued once a conditional likelihood function is fixed; rather, in Joyce's words, *"decision theories should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated."* Formally, each theory supplies a different mathematical rule for constructing a decision hypothetical $M^{a\hookrightarrow}$ from the agent's world-model $M$, thereby defining the decision-hypothetical connective "$\hookrightarrow$".

Let $\textsc{Outcome}$, $\textsc{Obs}$, and $\textsc{Act}$ be random variables taking values in $\mathcal{O}$, $\mathcal{X}$, and $\mathcal{A}$ respectively, and define the utility random variable $\textsc{V} \coloneqq \mathcal{U}(\textsc{Outcome})$. Writing $\mathbb{E}$ for expectation with respect to the agent's probability distribution $P$, the three theories diverge as follows.

### Evidential Decision Theory (EDT)
According to EDT, the world-model $M$ is simply a Bayesian probability distribution $P$, and the hypothetical $M^{a\hookrightarrow}$ is constructed by standard Bayesian conditionalization on both the observation history $\textsc{Obs} = x$ and the physical action $\textsc{Act} = a$ (provided $P(\textsc{Act} = a \mid \textsc{Obs} = x) > 0$). This yields Equation (2):

$$\mathrm{EDT}(P, x) \coloneqq \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs}=x, \textsc{Act}=a\right). \tag{2}$$

Because conditionalization preserves all statistical correlations encoded in $P$, an EDT agent evaluates $a$ by asking what $a$ constitutes *evidence* for, conflating indicative conditionals with counterfactuals.

### Causal Decision Theory (CDT)
CDT insists that decision hypotheticals must be genuinely counterfactual: they should track what an action *causes*, not what it indicates about the past. Using Pearl's (1996, 2000) graphical causal framework, CDT represents the agent's world-model as a causal theory $M = (P, G)$, where $G$ is a directed acyclic graph (DAG) encoding causal dependencies among the variables of $P$. To construct $M^{a\hookrightarrow}$, CDT conditions on the observation $\textsc{Obs} = x$ and applies Pearl's intervention operator $\mathtt{do}(\textsc{Act} = a)$, which severs all incoming arrows into $\textsc{Act}$ in $G$, fixes $\textsc{Act} = a$, and propagates this change strictly along directed causal paths downstream of $\textsc{Act}$. This yields Equation (3):

$$\mathrm{CDT}(P, G, x) \coloneqq \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x\right). \tag{3}$$

### Action Functional Decision Theory (A-FDT)
Like CDT, **A-FDT** constructs decision hypotheticals via surgery on a structured graphical model $M = (P, G)$. However, in A-FDT, the probability distribution $P$ and dependency graph $G$ are expanded to include variables representing the outputs of *mathematical functions*—for example, a variable for the sum $6288 + 1048$, and variables for the outputs of decision algorithms evaluated on specific inputs.

Specifically, an A-FDT agent's model $(P, G)$ contains a logical variable representing the output of the A-FDT decision procedure itself when run on inputs $(P, G, x)$. Adopting Yudkowsky and Soares's underline notation $\underline{z}$ to denote dequoting (so that if $x \coloneqq 3$, then $\textsc{Z}\underline{x}$ is the syntactic variable name $\textsc{Z}3$), let $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$—or equivalently $\textsc{afdt}(\underline{P}, \underline{G}, \underline{x})$—denote the variable in $G$ representing the output of the A-FDT algorithm on inputs $(P, G, x)$. As the authors note, this self-reference is mathematically benign: the agent need not know the *value* of the algorithm's output in order to include a syntactic node *representing* that output in $G$, and Kleene's (1938) second recursion theorem guarantees via "quining" that a computational procedure can construct and manipulate an exact syntactic representation of its own code and inputs.

Given a graph $G$ that encodes how changing the logical variable $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ propagates to all other variables in $P$, A-FDT is formally defined by **Equation (4)** of Section 5:

$$\mathrm{FDT}(P, G, x) \coloneqq \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P},\underline{G},\underline{x})= a\right)\right). \tag{4}$$

Comparing Equations (3) and (4) reveals two profound mathematical differences between CDT and A-FDT:

1. **Intervention on the Logical Type vs. the Physical Token**: CDT intervenes on the physical node $\textsc{Act}$, holding fixed all variables that are not causally downstream of the agent's bodily movement. A-FDT intervenes on the logical node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$, which represents the output of the mathematical function $\mathrm{FDT}$ on the input tuple $(P, G, x)$. Consequently, any physical system in the universe whose state depends on computing, simulating, or predicting $\mathrm{FDT}(P, G, x)$ lies downstream of $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ in $G$ and updates accordingly under the $\mathtt{do}$ operator.
2. **Observation Handling via Node-Switching ("Updatelessness")**: In Equation (3), CDT incorporates the observation $x$ by Bayesian conditionalization ($\textsc{Obs} = x$). In Equation (4), A-FDT *does not condition the distribution $P$ on $\textsc{Obs} = x$*. Instead, when the agent's observation history changes from $x$ to $y$, A-FDT responds by changing *which variable in $G$ it intervenes upon*—switching from $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ to $\textsc{fdt}(\underline{P}, \underline{G}, \underline{y})$. As Yudkowsky and Soares note, this feature is inherited from Wei Dai's (2009) Updateless Decision Theory (UDT), while avoiding the "double update" flaw of Yudkowsky's (2010) Timeless Decision Theory (TDT), which both conditioned on $\textsc{Obs} = x$ and shifted the intervention node.

When all correlations in $(P, G)$ between $\textsc{Act}$ and other decision-relevant variables are purely downstream causal effects of $\textsc{Act}$, the three theories coincide:

$$\mathbb{E}[\textsc{V} \mid a] = \mathbb{E}[\textsc{V} \mid \mathtt{do}(a)] = \mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})=a)].$$

They diverge precisely when non-causal correlations exist between the agent's action and the environment.

---

## 3. Subjunctive Dependence and Counterfactual Semantics

The philosophical core of A-FDT is captured by the authors' maxim: *"Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."*

What is **subjunctive dependence**? According to Yudkowsky and Soares, when two physical systems compute the same mathematical function, their behaviors subjunctively depend upon that function. Consider two well-functioning calculators in Paris and Tokyo, both computing $6288 + 1048$. Even if they share no recent causal link, their outputs are logically constrained to agree on $7336$ insofar as neither suffers a hardware malfunction (such as a stray cosmic ray). If a scribe in Paris writes down the Parisian calculator's output, her notes depend both *causally* and *subjunctively* on the calculation. Conversely, if both calculators happen by coincidence to be painted pink, that correlation is merely statistical; intervening on the Parisian calculator's color would not affect the Tokyo calculator's color.

In Peirce's (1934) terminology, CDT intervenes on the physical *token* ("my physical action right now is $a$"), whereas A-FDT intervenes on the mathematical *type* ("the output of the decision function $\mathrm{FDT}$ on input $(P, G, x)$ is $a$"). When an A-FDT agent faces a psychological twin in a Prisoner's Dilemma or an accurate predictor in Newcomb's problem, both the agent's physical body and the twin or predictor's simulation are physical instantiations ("calculators") evaluating the same logical function $\mathrm{FDT}(P, G, x)$.

### Why EDT and CDT Hypotheticals Fail
From the perspective of A-FDT, both EDT and CDT construct malformed hypotheticals:
* **EDT respects too many correlations.** Because EDT conditions on $\textsc{Act} = a$, it treats purely statistical correlations as invariant laws. In the *Cosmic Ray Problem* (Dilemma 5), an agent chooses between $\$1$ and $\$100$, knowing a rare cosmic ray occasionally flips her decision and requires a $\$1,000$ hospital check-up. If an EDT agent believes she almost always takes $\$1$, then conditional on taking $\$100$ she was almost certainly struck by a cosmic ray (netting $\$100 - \$1,000 = -\$900$), so she locks herself into taking $\$1$. Similarly, in *The XOR Blackmail* (Dilemma 6; Soares & Fallenstein, 2015), a predictor sends a letter iff *(i)* the agent has no termites (saving $\$1,000,000$) and will pay $\$1,000$, or *(ii)* the agent has termites and will refuse. Conditional on paying after seeing the letter, the probability of termites drops to $0$, so an EDT agent pays the extortionist even though the letter has zero causal or subjunctive effect on the termites.
* **CDT respects too few correlations.** Because CDT intervenes only on the physical token $\textsc{Act}$, it severs the link between the agent's decision and any predictor or twin that computed the same decision function. Consequently, CDT hypotheticals evaluate options in impossible worlds where known-to-be-reliable predictors inexplicably fail right when the agent acts. This produces severe pathology in *Death in Damascus* (Dilemma 7; Gibbard & Harper, 1978), where Death predicts whether the agent stays in Damascus or flees to Aleppo (at a $\$1,000$ travel cost) and meets her there. Holding Death's location fixed under $\mathtt{do}(\textsc{Act}=a)$, a CDT agent who expects to stay wants to flee, and one who expects to flee wants to stay. Even if the CDT agent uses a ratification procedure (Arntzenius, 2008; Joyce, 2012) to settle into a mixed state—assigning $50.05\%$ probability to staying in Damascus and $49.95\%$ to fleeing to Aleppo—she evaluates her options *as if* Death's location were independent of her choice, yielding a hallucinatory $\ge 50\%$ subjective survival rate ($$\$500,500$$ expected utility). If offered a genuinely unpredictable quantum coin for $\$1$ that actually gives a $50\%$ survival chance, the CDT agent refuses to buy it! An A-FDT agent recognizes that under $\mathtt{do}(\textsc{fdt}(\underline{P},\underline{G},\underline{x})=a)$, Death's appointment book changes with her output: survival is $0\%$ either way without the coin, so she stays in Damascus to save $\$1,000$—and would gladly pay $\$1$ for a truly random coin.

### Dominance Reconsidered
Causal decision theorists frequently defend two-boxing in Newcomb's problem by appealing to *dominance*: holding fixed the state of Box B, two-boxing yields $\$1,000$ more than one-boxing in every state. Yudkowsky and Soares point out that this argument is circular. Every rule for constructing hypotheticals $M^{a\hookrightarrow}$ induces its own dominance principle: action $a$ dominates $b$ relative to "$\hookrightarrow$" if switching from $b$ to $a$ is sometimes better and never worse across the worlds generated by "$\hookrightarrow$". Holding fixed the predictor's output while varying the agent's physical action is like asking what a reliable calculator would output if its screen displayed $3159$ while holding fixed that $6288 + 1048 = 7336$. Relative to A-FDT's subjunctive hypotheticals—where the accuracy of the predictor ($99\%$ or $1\%$) is held fixed while the logical output $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ varies—one-boxing strictly dominates two-boxing whenever the predictor is accurate, and overall in expectation.

---

## 4. Applying A-FDT: General Procedure and Canonical Cases

To make A-FDT operational so that a practitioner can apply Equation (4) to any decision problem, we can extract a four-step modeling and evaluation procedure from Sections 5 and 6 of the paper:

1. **Specify the Variable Space and Epistemic Inputs**: Identify the possible world-models/observation histories $(P', G, x')$ the agent might inhabit during the dilemma. For each such epistemic state, introduce a logical decision node $\textsc{fdt}(\underline{P'}, \underline{G}, \underline{x'})$ in $G$ taking values in $\mathcal{A}$. Include exogenous state variables (e.g., $\textsc{Accurate}$, $\textsc{Lesion}$, $\textsc{Infestation}$), predictor/twin variables, the physical action variable $\textsc{Act}$, and the utility variable $\textsc{V}$.
2. **Encode Subjunctive Dependencies and the $\textsc{Act}$ Multiplexer**:
   * Draw directed edges from $\textsc{fdt}(\underline{P'}, \underline{G}, \underline{x'})$ to any predictor or twin variable whose physical mechanism simulates or predicts how the agent decides when in state $(P', G, x')$.
   * Define $\textsc{Act}$ as a deterministic **multiplexer** (switching function) of the environmental state that determines which epistemic input the agent actually receives and the corresponding logical nodes $\textsc{fdt}(\underline{P'}, \underline{G}, \underline{x'})$.
3. **Intervene on the Active Logical Node**: Given the agent's actual model $P$, graph $G$, and observation $x$, do *not* condition $P$ on $\textsc{Obs} = x$. Instead, for each $a \in \mathcal{A}$, apply $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)$ to $P$.
4. **Propagate and Maximize**: Compute $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)]$ by propagating $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a$ along $G$'s structural equations, and output the maximizer $a^*$.

Let us see how this procedure works across three canonical structural templates.

### Template 1: Direct Predictive Coupling (Standard Newcomb's Problem)
In Newcomb's problem (Dilemma 2), Box A contains $\$1,000$, and Box B contains $\$1,000,000$ ($\mathit{full}$) if a $99\%$-accurate predictor predicted the agent would $\mathit{onebox}$, and $\$0$ ($\mathit{empty}$) if she predicted $\mathit{twobox}$. There are no intermediate observations ($x = \emptyset$).

For the A-FDT agent (Fiona), the graph $G^F$ (Figure 3b of the paper) has two exogenous root nodes: the logical variable $\textsc{fdt}(\underline{P^F}, \underline{G^F})$ and the predictor's accuracy variable $\textsc{Accurate}$ with $P^F(\textsc{Accurate} = \mathit{accurate}) = 0.99$ and $P^F(\textsc{Accurate} = \mathit{inaccurate}) = 0.01$. The structural equations downstream of $\textsc{fdt}(\underline{P^F}, \underline{G^F})$ are:
* $\textsc{Act} = \textsc{fdt}(\underline{P^F}, \underline{G^F})$.
* $\textsc{Prediction}(\textsc{fdt}(\underline{P^F}, \underline{G^F}), \textsc{Accurate})$ equals $1$ under $(\mathit{onebox}, \mathit{accurate})$ or $(\mathit{twobox}, \mathit{inaccurate})$, and $2$ under $(\mathit{twobox}, \mathit{accurate})$ or $(\mathit{onebox}, \mathit{inaccurate})$.
* $\textsc{Box B}(1) = \mathit{full}$ and $\textsc{Box B}(2) = \mathit{empty}$.
* $\textsc{V}(\textsc{Act}, \textsc{Box B})$ yields $\$1,000,000$ for $(\mathit{onebox}, \mathit{full})$, $\$1,001,000$ for $(\mathit{twobox}, \mathit{full})$, $\$0$ for $(\mathit{onebox}, \mathit{empty})$, and $\$1,000$ for $(\mathit{twobox}, \mathit{empty})$.

Applying Equation (4), we evaluate the two interventions:

$$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{onebox}\right)\right] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000,$$

$$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{twobox}\right)\right] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$

Because $\$990,000 > \$11,000$, $\mathrm{FDT}(P^F, G^F) = \mathit{onebox}$. Even if Fiona already knows before deciding that $\mathrm{FDT}(P^F, G^F) = \mathit{onebox}$ and hence is $99\%$ certain Box B is full, she does not switch to two-boxing: in her counterfactual semantics, for her to two-box, the logical value of $\textsc{fdt}(\underline{P^F}, \underline{G^F})$ would have to be $\mathit{twobox}$, in which case Box B would be $99\%$ likely to be empty.

### Template 2: Physical Common Cause and Model Uncertainty (The Smoking Lesion Problem)
In the Smoking Lesion Problem (Dilemma 3), an unobserved arterial lesion ($\textsc{Lesion} \in \{\mathit{lesion}, \mathit{nolesion}\}$) causes agents both to love smoking and ($99\%$ of the time, via $\textsc{Luck} = \mathit{unlucky}$) to develop fatal lung cancer ($\textsc{Death} = \mathit{dead}$, losing $\$1,000,000$); agents without the lesion die of cancer only $1\%$ of the time. Smoking yields an additional $\$1,000$ utility to those with the lesion.

Yudkowsky and Soares formalize this by noting that the lesion determines the agent's utility function: $\mathcal{U}_S$ (under which smoking is worth $+\$1,000$, inducing distribution $P_S^F$) if $\textsc{Lesion} = \mathit{lesion}$, or $\mathcal{U}_R$ (under which smoking is worth $-\$1$, inducing distribution $P_R^F$) if $\textsc{Lesion} = \mathit{nolesion}$. Fiona lacks introspective access to whether she has the lesion, so her graph $G^F$ (Figure 4 of the paper) contains *two* logical nodes, $\textsc{fdt}(\underline{P_S^F}, \underline{G^F})$ and $\textsc{fdt}(\underline{P_R^F}, \underline{G^F})$, and $\textsc{Act}$ acts as a multiplexer gated by $\textsc{Lesion}$:

$$\textsc{Act}(\mathit{lesion}, s, r) \coloneqq s, \qquad \textsc{Act}(\mathit{nolesion}, s, r) \coloneqq r,$$

where $s = \textsc{fdt}(\underline{P_S^F}, \underline{G^F})$ and $r = \textsc{fdt}(\underline{P_R^F}, \underline{G^F})$. Crucially, there is *no directed edge* from either logical node to $\textsc{Lesion}$ or $\textsc{Cancer}$: a biological lesion does not simulate the A-FDT algorithm.

Suppose Fiona actually has the lesion, so her decision procedure is $\mathrm{FDT}(P_S^F, G^F)$. Let $P_S^F(\mathit{lesion}) = p \in (0,1)$ and let $P_S^F(\textsc{fdt}(\underline{P_R^F}, \underline{G^F}) = \mathit{smoke}) = q \in [0,1]$. When Fiona intervenes on $\textsc{fdt}(\underline{P_S^F}, \underline{G^F})$, the probability of having the lesion is completely unaffected:

$$P_S^F\left(\mathit{lesion} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P_S^F}, \underline{G^F}) = \mathit{smoke}\right)\right) = P_S^F\left(\mathit{lesion} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P_S^F}, \underline{G^F}) = \mathit{refrain}\right)\right) = p.$$

With probability $p$, she has the lesion (receiving baseline survival expectation $0.01 \times \$1,000,000 = \$10,000$, plus $\$1,000$ iff $\textsc{fdt}(\underline{P_S^F}, \underline{G^F}) = \mathit{smoke}$). With probability $1-p$, she lacks the lesion (receiving baseline survival expectation $0.99 \times \$1,000,000 = \$990,000$, plus $q \cdot \$1,000$ as evaluated by $\mathcal{U}_S$ from the unactivated branch $\textsc{fdt}(\underline{P_R^F}, \underline{G^F})$). Thus:

$$\mathbb{E}_{P_S^F}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P_S^F}, \underline{G^F}) = \mathit{smoke}\right)\right] = p(\$10,000 + \$1,000) + (1-p)(\$990,000 + q \cdot \$1,000),$$

$$\mathbb{E}_{P_S^F}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P_S^F}, \underline{G^F}) = \mathit{refrain}\right)\right] = p(\$10,000) + (1-p)(\$990,000 + q \cdot \$1,000).$$

The difference is strictly positive ($p \cdot \$1,000 > 0$), so $\mathrm{FDT}(P_S^F, G^F) = \mathit{smoke}$. A-FDT thus one-boxes in Newcomb's problem and smokes in the Smoking Lesion Problem under a single rule.

### Template 3: Endogenous Observations (Transparent Newcomb, Parfit's Hitchhiker, and Mechanical Blackmail)
Now consider the **Transparent Newcomb Problem** (Dilemma 4), which is structurally isomorphic to **Parfit's Hitchhiker Problem** (Dilemma 3 in Section 4) and **The Mechanical Blackmail** (Dilemma 8). Here, both boxes are transparent, and the predictor (who is $99\%$ accurate) places $\$1,000,000$ in Box B iff she predicts the agent will $\mathit{onebox}$ *upon observing that Box B is full* ($\textsc{Obs} = \mathit{full}$).

When CDT and EDT agents observe $\textsc{Obs} = \mathit{full}$, both condition their probability distributions on $\textsc{Obs} = \mathit{full}$, locking the $\$1,000,000$ in place:

$$\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{Act}=\mathit{twobox}), \textsc{Obs}=\mathit{full}] = \mathbb{E}[\textsc{V} \mid \textsc{Act}=\mathit{twobox}, \textsc{Obs}=\mathit{full}] = \$1,001,000 > \$1,000,000.$$

Both therefore two-box upon seeing a full box; anticipating this, the predictor leaves Box B empty (and Parfit's driver leaves them in the desert to die).

How does A-FDT evaluate the situation when Fiona observes $x = \mathit{full}$? In Fiona's graph $G^F$ (Figure 5b of the paper), there are two observation-indexed logical nodes: $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$ and $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$. Because the predictor specifically predicts what Fiona will do *if shown a full box*, $\textsc{Prediction}$ has an incoming arrow from $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$ (and from $\textsc{Accurate}$), but *not* from $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$. Meanwhile, $\textsc{Prediction}$ determines $\textsc{Box B}$ (and hence which observation Fiona actually sees), so $\textsc{Act}$ is multiplexed by $\textsc{Prediction}$:

$$\textsc{Act}\left(\textsc{Prediction}, a_{\mathit{full}}, a_{\mathit{empty}}\right) = \begin{cases} a_{\mathit{full}} & \text{if } \textsc{Prediction} = 1 \text{ (Box B is }\mathit{full}\text{)}, \\ a_{\mathit{empty}} & \text{if } \textsc{Prediction} = 2 \text{ (Box B is }\mathit{empty}\text{)}. \end{cases}$$

When Fiona observes $\mathit{full}$, she applies Equation (4) by intervening on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = a$ *without conditioning $P^F$ on $\textsc{Obs} = \mathit{full}$*. (Note that in Section 6 of the source paper, the inline display formula on page 17 contains a typographical slip—writing $\mathbb{E}(\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})=a, \textsc{Obs}=\mathit{full})$ with an unclosed parenthesis—but the authors' immediately following derivation and text explicitly apply Equation (4) without conditioning on $\textsc{Obs} = \mathit{full}$.) Let $q = P^F(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty}) = \mathit{twobox})$. We compute:
* **Under $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{onebox})$**: With probability $0.99$ ($\textsc{Accurate} = \mathit{accurate}$), $\textsc{Prediction} = 1$, Box B is $\mathit{full}$, the multiplexer routes $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{onebox}$ to $\textsc{Act}$, and Fiona receives $\$1,000,000$. With probability $0.01$ ($\textsc{Accurate} = \mathit{inaccurate}$), $\textsc{Prediction} = 2$, Box B is $\mathit{empty}$, the multiplexer routes $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$ to $\textsc{Act}$, and Fiona receives $q \cdot \$1,000$ in expectation. Total expected utility:

  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{onebox}\right)\right] = \$990,000 + 0.01q \cdot \$1,000.$$

* **Under $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{twobox})$**: With probability $0.01$ ($\textsc{Accurate} = \mathit{inaccurate}$), $\textsc{Prediction} = 1$, Box B is $\mathit{full}$, the multiplexer routes $\mathit{twobox}$ to $\textsc{Act}$, and Fiona gets $\$1,001,000$. With probability $0.99$ ($\textsc{Accurate} = \mathit{accurate}$), $\textsc{Prediction} = 2$, Box B is $\mathit{empty}$, the multiplexer routes $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$ to $\textsc{Act}$, and Fiona gets $q \cdot \$1,000$. Total expected utility:

  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{twobox}\right)\right] = 0.01(\$1,001,000) + 0.99q \cdot \$1,000 = \$10,010 + q \cdot \$990.$$
  *(Note: the source paper prints $\$10,010$ with a minor typo as "$\$110,00$".)*

For any $q \in [0,1]$, $\$990,000 + \$10q > \$10,010 + \$990q$, so $\mathrm{FDT}(P^F, G^F, \mathit{full}) = \mathit{onebox}$. Even while staring directly at a full Box B, when Fiona imagines $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$ outputting $\mathit{twobox}$, she imagines a counterfactual world where the predictor foresaw this, left Box B empty with $99\%$ probability, and caused her to observe $\mathit{empty}$ instead!

The exact same updateless mechanics govern **The Mechanical Blackmail** (Dilemma 8, Figure 7 of the paper), where a blackmailer runs a self-incriminating program (causing $-\$1,000,000$ damage unless stopped by a $\$1,000$ wire transfer) iff she predicts the agent will $\mathit{pay}$ upon receiving the blackmail notice ($\textsc{Obs} = \mathit{blackmail}$). Suppose the blackmailer errs with probability $\varepsilon$ (falsely predicting the agent will pay when she will refuse). Upon holding the blackmail letter, Fiona intervenes on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{blackmail})$:
* Outputting $\mathit{pay}$ yields $-\$1,000$ (assuming accuracy $1-\varepsilon \approx 1$).
* Outputting $\mathit{refuse}$ means she is blackmailed only when the predictor errs (with probability $\varepsilon$), yielding expected utility $-\varepsilon \cdot \$1,000,000$.

Thus, if $\varepsilon = 0.0009$ ($0.09\%$), refusing yields $-\$900 > -\$1,000$, so Fiona refuses to pay even when holding the blackmail letter. If $\varepsilon = 0.0011$ ($0.11\%$), refusing yields $-\$1,100 < -\$1,000$, so she pays. In every case, A-FDT adopts the exact disposition that a rational agent would have paid to precommit to ex ante, without needing physical precommitment devices and without assigning negative value to information.

---

## 5. Open Questions and Operational Extensions for Unfamiliar Cases

While Yudkowsky and Soares provide a clear mathematical rule in Equation (4), they explicitly leave three foundational questions open. To help researchers apply A-FDT to novel problems, we carefully distinguish what the source paper establishes from additional operational assumptions we propose here.

### 5.1. Deducing the Subjunctive Graph $G$ Without a $\mathtt{true}$ Operator
**What the source states:** In Section 5, the authors note that an ideal formulation of functional decision theory ($\mathrm{FDT}^*$) would not require a graphical input $G$ at all; instead, it would use a logical counterpossibility operator $\mathtt{true}(\phi)$ that updates $P$ directly on the logical sentence $\textsc{fdt}(\underline{P}, \underline{x}) = a$ (or, as Footnote 9 notes, a logical conditional probability distribution over counterpossibles). Because logicians and computer scientists do not yet possess a general mathematical definition of $\mathtt{true}(\phi)$ for counter-to-logic antecedents (such as conditioning on $6288 + 1048 \neq 7336$), Equation (4) bypasses $\mathtt{true}$ by requiring the subjunctive dependency graph $G$ as an explicit input and applying Pearl's $\mathtt{do}$ operator. As the authors emphasize: *"Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."*

**Operational proposal (The Algorithmic Emulation Criterion):** How should a modeler construct $G$ in an unfamiliar problem? Extending the paper's calculator analogy, we propose a concrete structural rule: *In constructing $G$, a directed edge should be drawn from $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ to an environmental variable $Y$ if and only if the physical mechanism generating $Y$ is sensitive to an algorithmic emulation, formal proof, or behavioral copy of the agent's decision procedure evaluated on the specific epistemic input $(P, G, x)$.*

To apply this in practice, decompose any putative predictor $Y$ into two components: (i) the target mathematical function $\textsc{fdt}(\underline{P'}, \underline{G'}, \underline{x'})$ that $Y$'s physical mechanism attempts to evaluate, and (ii) an exogenous fidelity/noise variable $\textsc{Accurate}_Y$ capturing bounded computation, observation noise, or model misspecification.
* If a counterparty uses past statistical data about *other* humans to guess the agent's action without modeling the agent's actual decision function, $Y$ is merely a statistical correlate (like the smoking lesion): no edge from $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ to $Y$ is drawn.
* If a counterparty runs a noisy simulation of the agent's code on input $(P, G, x)$ with fidelity $1 - \varepsilon$, then $Y$ receives a directed edge from $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ and from $\textsc{Accurate}_Y$ (where $P(\textsc{Accurate}_Y = \mathit{accurate}) = 1 - \varepsilon$).

### 5.2. Unactivated Logical Nodes and the Boundary Between A-FDT and Policy FDT
**What the source states:** In Equation (4), A-FDT intervenes on the single node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ corresponding to the agent's actual observation $x$. However, as seen in the Smoking Lesion Problem and Transparent Newcomb Problem, the graph $G$ also contains *other* logical nodes $\textsc{fdt}(\underline{P'}, \underline{G}, \underline{x'})$ for unactivated epistemic inputs $(P', x') \neq (P, x)$. In Section 6, Yudkowsky and Soares treat the unactivated node as a random variable with prior probability $q$, remarking parenthetically that the "correct value" of $q$ can be verified (e.g., $q=0$ for smoking without the lesion; $q=1$ for two-boxing when Box B is seen to be empty), while noting that in those dilemmas the value of $q$ does not affect the optimal choice. Meanwhile, in Footnotes 7 and 16, the authors remark that in their preferred formulation of FDT, *"agents actually iterate over policies (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."*

**Operational analysis and an unfamiliar diagnostic case:** What happens in an unfamiliar dilemma where the value of the unactivated logical node *does* affect the decision, or where a predictor's behavior depends jointly on multiple observation branches? We can distinguish two cases and provide an explicit operational resolution:

* **Case A: Independent Unactivated Branches (Recursive Self-Evaluation).** Suppose that in the Transparent Newcomb Problem, an eccentric philanthropist adds a side-bet: if the predictor predicts $\mathit{twobox}$ (leaving Box B empty), the philanthropist awards the agent a bonus of $\$2,000,000$ iff the agent leaves Box A behind ($\mathit{onebox}$) upon seeing $\textsc{Obs} = \mathit{empty}$. Now the expectation on the $\mathit{empty}$ branch is no longer bounded by $\$1,000$: if Fiona believed $q = P^F(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty}) = \mathit{onebox}) = 1$, then under $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{twobox})$, she would expect to see an empty box $99\%$ of the time and win $0.99 \times \$2,000,000 = \$1,980,000 > \$990,000$!
  How does A-FDT avoid being misled by an arbitrary prior $q$? By **recursive self-evaluation**: because $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$ represents the output of the *same* deterministic algorithm $\mathrm{FDT}$ on input $(P^F, G^F, \mathit{empty})$, a logically coherent prior $P^F$ must concentrate its mass on the actual solution of Equation (4) for $x = \mathit{empty}$. Solving $\mathrm{FDT}(P^F, G^F, \mathit{empty})$ yields $\mathit{onebox}$ (because on that branch, $\mathit{onebox}$ nets $\$2,000,000$). Thus, recursive self-evaluation pins $q$ to its exact fixed point.

* **Case B: Jointly Predicted Branches (Where A-FDT and Policy FDT Diverge).** Consider an unfamiliar dilemma we call the **Twin-Branch Coordination Problem**. A predictor flips a fair coin $C \in \{\mathit{Heads}, \mathit{Tails}\}$ and shows the outcome to the agent ($\textsc{Obs} \in \{\mathit{Heads}, \mathit{Tails}\}$). The agent must choose $a \in \{\mathit{Red}, \mathit{Blue}\}$, paying a cost of $\$1,000$ if she chooses $\mathit{Red}$ and $\$0$ if she chooses $\mathit{Blue}$. Before flipping the coin, a perfect predictor simulates the agent under *both* possible observations and places $\$1,000,000$ in the agent's bank account iff *both* $\mathrm{FDT}(P, G, \mathit{Heads}) = \mathit{Red}$ *and* $\mathrm{FDT}(P, G, \mathit{Tails}) = \mathit{Red}$.
  Let us apply **A-FDT (Equation 4)** when the agent observes $x = \mathit{Heads}$. In $G$, the node $\textsc{Bank}$ is a conjunction of $\textsc{fdt}(\underline{P}, \underline{G}, \mathit{Heads}) = \mathit{Red}$ and $\textsc{fdt}(\underline{P}, \underline{G}, \mathit{Tails}) = \mathit{Red}$, while $\textsc{Act}$ is multiplexed by the coin $C$:
  $$\textsc{Act}(C, a_H, a_T) = \begin{cases} a_H & \text{if } C = \mathit{Heads}, \\ a_T & \text{if } C = \mathit{Tails}. \end{cases}$$
  Let $r = P(\textsc{fdt}(\underline{P}, \underline{G}, \mathit{Tails}) = \mathit{Red})$. Under Equation (4), intervening on $\textsc{fdt}(\underline{P}, \underline{G}, \mathit{Heads})$ alone while holding $\textsc{fdt}(\underline{P}, \underline{G}, \mathit{Tails})$ at its prior $r$ yields:

  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \mathit{Heads}) = \mathit{Red}\right)\right] = r \cdot \$1,000,000 - 0.5(\$1,000) - 0.5 r(\$1,000),$$

  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \mathit{Heads}) = \mathit{Blue}\right)\right] = 0 - 0.5(0) - 0.5 r(\$1,000).$$

  Notice that $\mathrm{FDT}(P, G, \mathit{Heads}) = \mathit{Red}$ iff $r \cdot \$1,000,000 > \$500$, i.e., $r > 0.0005$. Under strict A-FDT (Equation 4), the two observation branches $\textsc{fdt}(\underline{P}, \underline{G}, \mathit{Heads})$ and $\textsc{fdt}(\underline{P}, \underline{G}, \mathit{Tails})$ face a symmetric coordination game with each other: if the agent's prior sets $r = 0$, neither branch has a unilateral incentive under a single-node intervention to pay $\$500$ in expectation, trapping A-FDT in the $(\mathit{Blue}, \mathit{Blue})$ equilibrium ($0$ utility) unless a symmetry-breaking edge links the two nodes in $G$! By contrast, a *Policy FDT* agent (Footnotes 7 and 16) intervenes on a single function node $\textsc{fdt}(\underline{P}, \underline{G}) = \pi \in \mathcal{A}^{\mathcal{X}}$, directly comparing the policy $\pi_{RR}(\cdot) = \mathit{Red}$ (expected utility $\$999,000$) against $\pi_{BB}(\cdot) = \mathit{Blue}$ (expected utility $\$0$). Thus, within pure A-FDT, whenever a dilemma is symmetric across observation branches $x_1, x_2$, the modeler can recover the optimal outcome by explicitly encoding the symmetry constraint between $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_1})$ and $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_2})$ in $G$.

### 5.3. Formalizing "Fair" Dilemmas
**What the source states:** In Section 9 and Footnote 15, Yudkowsky and Soares acknowledge that no decision theory outperforms all rivals in *every* conceivable environment. For instance, an adversary who reads an agent's source code and rewards her iff she implements CDT (or iff she acts differently from a clone of Fiona) will punish A-FDT agents. The authors conjecture that A-FDT is optimal across all **"fair problems"**—informally defined as dilemmas where the agent's beliefs are accurate and outcomes depend only on predictions of the agent's *behavior in the dilemma at hand* ("Newcomb's predictor doesn't punish rational agents; she punishes *two-boxers*"). However, they note that formalizing fairness remains an open problem.

**Operational proposal (Extensional Action-Prediction Invariance):** Within the graphical formalism of $(P, G)$, we can formulate a precise structural criterion to test whether a dilemma is fair to A-FDT: *A decision model $(P, G)$ is **extensional-action fair** at input $(P, G, x)$ if every directed path in $G$ from $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ to the utility node $\textsc{V}$ either (i) passes directly through $\textsc{Act}$, or (ii) passes through predictor nodes $Y_i$ whose structural mechanisms depend only on the input-output mapping (the extension) of the agent's decision procedure in the current decision problem, rather than on syntactic properties of the algorithm or its outputs on unrelated decision problems.* Whenever this condition holds, any reward attainable by *some* predictable action in $\mathcal{A}$ is available to A-FDT via Equation (4).

---

## 6. Conclusion

Action Functional Decision Theory (**A-FDT**), as formalized in Equation (4) of Yudkowsky and Soares's paper, represents a major conceptual advance in the theory of rational choice. By shifting the point of causal surgery from the physical action token $\textsc{Act}$ to the logical output variable $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ and handling observations by switching the target of logical intervention rather than conditioning the prior distribution $P$, A-FDT unifies the strengths of CDT and EDT in a single mathematical rule. It cooperates with twins, one-boxes in standard and transparent Newcomb problems, smokes in the smoking lesion problem, resists extortion in both XOR and mechanical blackmail, and maintains reflective stability without requiring costly precommitments or ad-hoc ratification procedures. While foundational questions remain open—most notably deriving the subjunctive graph $G$ from a formal logic of counterpossibles and coordinating across multiple observation branches—A-FDT provides a rigorous, practical blueprint for rational agency in a world populated by predictors, replicators, and strategic counterparts.

---

## References

* Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
* Arntzenius, F. (2008). No regrets, or: Edith Piaf revamps decision theory. *Erkenntnis*, 68(2), 277–297.
* Dai, W. (2009). Towards a new decision theory. *Less Wrong*.
* Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Gibbard, A., & Harper, W. L. (1978). Counterfactuals and two kinds of expected utility. In *Foundations and Applications of Decision Theory* (Vol. 1). D. Reidel.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Joyce, J. M. (2012). Regret and instability in causal decision theory. *Synthese*, 187(1), 123–145.
* Kleene, S. C. (1938). On notation for ordinal numbers. *Journal of Symbolic Logic*, 3(4), 150–155.
* Lewis, D. (1979). Prisoners' dilemma is a Newcomb problem. *Philosophy & Public Affairs*, 8(3), 235–240.
* Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
* Nozick, R. (1969). Newcomb's problem and two principles of choice. In *Essays in Honor of Carl G. Hempel* (pp. 114–146). D. Reidel.
* Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
* Pearl, J. (1996). Causation, action, and counterfactuals. In *6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-'96)* (pp. 51–73).
* Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Peirce, C. S. (1934). *Collected Papers of Charles Sanders Peirce* (Vol. V). Harvard University Press.
* Skyrms, B. (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Soares, N., & Fallenstein, B. (2015). Toward idealized decision theory. *arXiv preprint arXiv:1507.01986*.
* Yudkowsky, E. (2010). *Timeless Decision Theory*. The Singularity Institute.
* Yudkowsky, E., & Soares, N. (2017). Functional decision theory: A new theory of instrumental rationality. *arXiv preprint arXiv:1710.05060v2*.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Composing A-FDT Explanation**

I'm making progress on explaining Action Functional Decision Theory (A-FDT). My focus is on synthesizing Yudkowsky and Soares' article into a clear, concise mathematical essay. I'm aiming for a technical blog post suitable for experts in the field. I'm working now to establish a basic outline of the essay, defining the key concepts in a precise manner.


**Defining A-FDT Formalism**

Now, I'm diving into the formal aspects of A-FDT, especially Equation (4) from the paper. I'm aiming to define the key components and how they fit together. My goal is to capture the essence of A-FDT in a way that is both mathematically precise and conceptually clear. I am also working to identify the key differences between this and other decision theories, such as EDT.


**Analyzing A-FDT Nuances**

I'm now focusing on how A-FDT tackles unfamiliar scenarios and evaluating alternative actions. I'm carefully analyzing how it handles dependencies and counterfactuals, and I will attempt to identify and interpret any gaps. I am carefully distinguishing the claims presented in the source text from any of my own additions. I'm aiming for a concise, readable mathematical essay, using examples for clarity and planning a solid conclusion.


**Contrasting Decision Theories**

I'm now deep-diving into the differences between Causal Decision Theory (CDT) and Evidential Decision Theory (EDT), outlining their core equations. EDT conditions on the action and struggles with the Smoking Lesion problem, whereas CDT intervenes on actions and faces issues like the Twin Prisoner's Dilemma. I'm carefully comparing their approaches to various problems to better grasp the nuances of each theory.


**Clarifying A-FDT's Formalism**

Now, I'm focusing on the core of A-FDT. I'm exploring how it relates to expected utility, framed by Joyce and Gibbard & Harper, where my goal is to explain the agent intervening on the action type, not the physical act. I'm carefully analyzing Equation (1) and considering how subjunctive dependence, crucial to A-FDT, is a generalization of causal dependence. My aim is to distinguish this from statistical correlation.


**Interpreting A-FDT Formalism**

Now, I'm carefully examining Equation (4) from the original paper, working on its interpretation. My focus is on unpacking the notation, particularly the "do" operator and the conditional expectation. I'm clarifying how this equation relates to the overall A-FDT framework. I will explicitly connect the paper's original notation with A-FDT in my writing. I am also currently working on a point-by-point comparison with CDT's core equation to highlight key mathematical differences.


**Differentiating A-FDT Formalisms**

I'm now zeroing in on the crucial distinctions between Causal Decision Theory (CDT) and Action Functional Decision Theory (A-FDT). My focus is now on the formal differences. CDT intervenes on the *physical* action, whereas A-FDT intervenes on the *logical* function representing the decision algorithm. A-FDT also does not condition on observations; instead, it shifts the intervention node based on new information.


**Clarifying A-FDT Notation**

Now, I'm identifying a typo in Section 6. I'll need to clarify the unnumbered equation regarding the Transparent Newcomb problem. It's crucial to explain how this aligns with Equation (4)'s intervention, differentiating from observation conditioning. I'll also look at Footnotes 7 and 16, and provide the reason for A-FDT vs Policy FDT, in my essay.


**Explaining A-FDT Iteration**

I'm now focusing on the distinction between A-FDT and Policy FDT, particularly as it relates to iterated policies. I'm exploring the implications of intervening on policy mappings, rather than individual actions, especially in multi-agent dilemmas, and how that influences my explanation of the underlying formalism. I'm reviewing Footnotes 7 and 16, and will be providing the reasoning for this distinction.


**Outlining A-FDT Process**

I'm now detailing a step-by-step operational procedure for applying A-FDT. I'm focusing on clarifying how to build the preference state $(P, G)$ and evaluate AFDT($P, G, x$). I'm working to specify the world-model variables, including exogenous variables, logical decision outputs, and predictor/twin variables, all with illustrative examples.


**Detailing A-FDT Mechanics**

I've outlined an A-FDT operational procedure, focusing on the agent's actual model and observation, $(P, G, x)$. I'm detailing the structural intervention $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)$ on the prior distribution $P$ for each action. I am also working to define the physical action and outcome nodes, clarifying their relation to the logical decision.


**Illustrating A-FDT Examples**

I'm now detailing clear, concrete examples to illustrate A-FDT. I'm focusing on Standard Newcomb's Problem and the Twin Prisoner's Dilemma, showing how intervening on the logical node impacts both the action and prediction. Also, I'm working to show how the Smoking Lesion Problem is handled. I am working to define all world-model variables, with the goals of showing the implications of structural interventions.


**Analyzing A-FDT Implementation**

I'm working on how A-FDT applies to unfamiliar scenarios, like asymmetric observations in multi-agent problems. I'm focusing on clarifying how it handles predictor errors and tunable prediction thresholds in the context of the Mechanical Blackmail problem. I'll highlight open questions from the source paper.


**Clarifying A-FDT Nuances**

I'm now zeroing in on an open question: deducing the subjunctive dependency graph *G* and its relation to counterfactual reasoning. I'm exploring the nuances of using Pearl's "do" operator, instead of a hypothetical "true" operator for logical conditioning, and the implications of this approach. I'm currently figuring out how A-FDT bypasses issues in counterpossible conditionalization.


**Proposing Dependency Solution**

I'm now focusing on a new problem: constructing the subjunctive dependency graph $G$. I'm proposing an algorithmic factorization based on computational common-source analysis to solve this, extending the calculator analogy. This involves identifying variables whose mechanisms simulate or copy the agent's decision, with an accuracy variable for hardware and modeling issues. Conversely, shared history correlations are treated as upstream causes.


**Addressing Unactivated Nodes**

I'm now investigating unactivated logical nodes within the A-FDT framework, especially their prior probabilities and how these impact decisions, focusing on their treatment in the paper. I'm exploring the implications of A-FDT's intervention on active observation nodes and how it considers unobserved, but related, scenarios. I'm currently working to resolve how a particular example works out.


**Operationalizing A-FDT**

I'm working on how A-FDT addresses scenarios where the payoff or predictor depends on the agent's actions across multiple observations, especially when the predictor is pivotal. I'm focusing on clarifying how the un-intervened nodes $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x'})$ are determined and handled for non-current observations, drawing on the recursive self-evaluation method. I'm currently using Footnotes 7 and 16 to distinguish A-FDT from policy-based FDT, particularly in multi-agent dilemmas.


**Formalizing Observation Dilemmas**

I'm now grappling with multi-observation scenarios where predictors depend on the agent's actions across multiple observations, creating a coordination bottleneck. I'm focusing on clarifying how intervening on a single observation branch while holding others fixed leads to issues. I am working towards a mathematical example that highlights this and explores recursive equilibrium and policy intervention as potential solutions.


**Formalizing Fairness Conditions**

I'm now formalizing the necessary conditions for "action-only fairness" from Section 9. I'm focusing on defining this within the $(P, G)$ framework using path constraints from the logical decision node to the utility node. Specifically, I'm working to describe how all paths in $G$ must pass through the action or an action-equivalent predictor.


**Planning Essay Structure**

I'm now mapping out the structure and estimating the word budget for my essay, aiming for around 2,750 words. I am planning on an introduction, formal framework, and several other sections. I am structuring the introduction, and formal framework of the essay right now, as a preliminary step.


**Differentiating A-FDT Mechanics**

I'm now contrasting Evidential Decision Theory (EDT) and Causal Decision Theory (CDT) equations, highlighting the critical distinctions. I'm introducing A-FDT via Equation (4) from Section 5, unpacking the structural innovations of type-level logical intervention and updateless observation handling. I'm focusing on the type-level logical intervention with the do operator. The structural innovations, including updateless observation handling, are now taking shape.


**Explaining Subjunctive Dependencies**

I'm now diving into subjunctive dependence, using the calculator analogy and contrasting it with predictor-based dependencies. I'm carefully contrasting how EDT, CDT, and A-FDT model hypothetical scenarios and how A-FDT redefines dominance. I'm focusing on why EDT "manages the news" too broadly and how CDT's approach is unstable, as illustrated by *Death in Damascus*. A-FDT's treatment with respect to subjunctive dependencies appears promising.


**Illustrating A-FDT Mechanics**

I'm now detailing clear examples to demonstrate A-FDT's core mechanisms. I'm carefully laying out two key templates: one on spurious physical correlation, using the Smoking Lesion Problem, and the other on endogenous observations using Transparent Newcomb, Parfit's Hitchhiker, and Mechanical Blackmail. I'm focusing on the calculations and multiplexing in each, and how the theory responds to the scenarios. I will also be noting the specific variables.


**Proposing Computational Analysis**

I'm now focusing on two key technical challenges. I plan to extend Equation (4) using a computational dependence criterion for constructing graph *G*, rather than the $\mathtt{true}$ operator, and I'll explore the implications of unactivated logical nodes, also revisiting Footnotes 7 and 16. I'm working to explicitly construct a novel example for an unfamiliar case, the Joint-Branch Predictor Dilemma, to expose any shortcomings.


**Operationalizing "Fair" Dilemmas**

I'm now detailing how A-FDT handles scenarios where payoffs or predictions are interdependent across multiple observations. My current focus is on clarifying why recursive self-evaluation works for independent branches, and why cross-branch coordination motivates policy extensions. I'm also discussing Section 9 and Footnote 15, and I am proposing an operational graphical criterion to test "fairness" by action predictions and extensional invariance. Finally, I'm verifying all quotations from the source text.


**Interpreting Key Concepts**

My focus is now on core concepts. I'm carefully analyzing how A-FDT aligns with the quoted phrases on subjunctive dependence, the epistemic perspective, and the open problem of deducing subjunctive dependency structures. I'm exploring the implications of iterating over *policies* (as mentioned in Footnote 7) and checking calculations from the original paper, using these notes.


```
