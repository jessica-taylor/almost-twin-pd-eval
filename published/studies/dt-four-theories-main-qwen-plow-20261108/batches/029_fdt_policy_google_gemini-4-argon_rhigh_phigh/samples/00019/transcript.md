# 029_fdt_policy_google_gemini-4-argon_rhigh_phigh / 00019

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/93694eea-0f93-472a-8544-1d47ba8151ca/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/93694eea-0f93-472a-8544-1d47ba8151ca/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Policy Functional Decision Theory (P-FDT): Formalism, Counterfactuals, and Multi-Agent Coordination

## 1. Introduction and Philosophical Motivation

For decades, normative decision theory was locked in a stalemate between two rival paradigms: **evidential decision theory (EDT)** and **causal decision theory (CDT)**. Both theories endorse the maximization of expected utility, yet they disagree on how an agent should construct the hypothetical scenarios used to evaluate candidate choices. EDT evaluates an action by asking how good the news would be if the agent learned she had taken it—formally, conditioning her belief distribution on the action. CDT evaluates an action by asking what the action physically causes—formally, intervening on the physical action token while holding the causal past fixed.

Neither theory is universally satisfactory if we judge rationality by average utility achieved across decision problems. In Nozick’s (1969) Newcomb’s problem, where a reliable predictor places $\$1,000,000$ in an opaque box (Box B) if and only if she predicts the agent will leave behind a transparent box containing $\$1,000$ (Box A), CDT prescribes taking both boxes (“two-boxing”) because the prediction is already in the causal past; EDT prescribes taking only Box B (“one-boxing”) and walks away rich. Conversely, in Skyrms’ (1980) smoking lesion problem—where a congenital arterial lesion causes both a love of smoking and fatal lung cancer, with no causal link from smoking to cancer—EDT prescribes refraining from smoking to avoid “evidence” of the lesion, whereas CDT recognizes that smoking does not cause cancer and enjoys the cigar. And in sequential predictive dilemmas such as Parfit’s (1986) hitchhiker problem or Drescher’s (2006) transparent Newcomb problem, both CDT and EDT fail to secure the high-utility outcome without expensive prior precommitments.

In *Functional Decision Theory: A New Theory of Instrumental Rationality*, Eliezer Yudkowsky and Nate Soares propose a third paradigm that resolves these dilemmas under a single rule. The foundational premise of their framework is that an agent should treat her decision not merely as a physical bodily movement, but as the logical output of a fixed mathematical function—the decision algorithm itself—and ask: *“Which output of this very function would yield the best outcome?”* 

Yet within Yudkowsky and Soares’s presentation, there is a crucial distinction between the simplified **action-based functional decision theory (FDT)** analyzed in the main text of their paper and the fuller theory they actually endorse: **policy functional decision theory (P-FDT)**. In Footnote 7, the authors note:

> “In the authors’ preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper.”

They return to this formulation in Footnote 16 when discussing how agents respond to observations:

> “As mentioned earlier, the author’s preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition.”

This essay provides a self-contained mathematical and philosophical account of **P-FDT**. We will build the formal apparatus of P-FDT from the ground up, show how it evaluates counterfactual dependencies across observations, demonstrate why it matches action-based FDT in single-agent dilemmas while strictly outperforming it in multi-agent coordination problems, and develop operational answers to the formal questions left open by the source text.

---

## 2. From Action Hypotheticals to Policy Interventions: Formalizing P-FDT

To understand how **P-FDT** works, we first situate it within the general expected utility framework of Gibbard and Harper (1978) and Joyce (1999). Let $\mathcal{A}$ be a finite set of physical actions, $\mathcal{X}$ a countable set of possible observation histories, and $\mathcal{O} = \{o_1, o_2, \dots\}$ a countable set of outcomes. Let $\mathcal{U} : \mathcal{O} \to \mathbb{R}$ be a bounded utility function, and define the utility random variable $\textsc{V} \coloneqq \mathcal{U}(\textsc{Outcome})$.

In general expected utility theory, an agent who has received observation history $x \in \mathcal{X}$ evaluates a candidate choice $c$ by computing:

$$\mathcal{EU}(c) \coloneqq \sum_{j} P(c \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j),$$

where $P(c \hookrightarrow o_j ;\, x)$ is the subjective probability that outcome $o_j$ obtains in the hypothetical scenario where $c$ is chosen given observation $x$. As Joyce (1999) puts it, *“decision theories should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated.”* Each decision theory specifies what internal world-model $M$ the agent maintains and how she modifies $M$ to construct a hypothetical $M^{c\hookrightarrow}$ for each candidate option $c$.

### 2.1 EDT, CDT, and Action-Based FDT

In **EDT**, the world-model $M$ is simply a probability distribution $P$ over the relevant random variables ($\textsc{Obs}$, $\textsc{Act}$, $\textsc{Outcome}$, $\textsc{V}$, etc.). Upon observing $x \in \mathcal{X}$, EDT constructs hypotheticals via standard Bayesian conditioning on both the observation and the physical action:

$$\mathrm{EDT}(P, x) \coloneqq \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs}=x, \textsc{Act}=a\right).$$

In **CDT**, following Pearl’s (1996, 2000) graphical causal formalism, the world-model is a pair $M = (P, G)$, where $G$ is a directed acyclic graph (DAG) encoding causal dependencies among the variables of $P$. CDT constructs hypotheticals by conditioning on the observation $\textsc{Obs} = x$ and applying Pearl’s surgical intervention operator $\mathtt{do}(\textsc{Act}=a)$, which severs all incoming edges to the physical action node $\textsc{Act}$, fixes $\textsc{Act}=a$, and propagates the change only to variables causally downstream of $\textsc{Act}$:

$$\mathrm{CDT}(P, G, x) \coloneqq \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x\right).$$

Why do EDT and CDT fail in opposite ways? Because EDT’s conditioning preserves *all* statistical correlations between $\textsc{Act}$ and the rest of the world (including mere common-cause correlations like the smoking lesion), whereas CDT’s $\mathtt{do}(\textsc{Act}=a)$ severs *all* non-causal correlations (including the logical/computational correlation between an agent’s decision algorithm and an accurate predictor’s model of that algorithm).

Yudkowsky and Soares resolve this by introducing **subjunctive dependence**. When two physical systems—such as an agent’s brain and a predictor’s simulation, or two psychological twins—compute the same mathematical function, their outputs subjunctively depend on the abstract mathematical mapping that defines that function, just as two intact calculators computing $6288 + 1048$ subjunctively depend on the laws of arithmetic. Instead of intervening on the physical *token* $\textsc{Act}$, a functional decision theorist intervenes on the mathematical *type*: the logical output of her decision algorithm.

Because a deterministic mathematical function has a fixed output on a fixed input by logical necessity, asking “What if my decision function output $a_2$ instead of $a_1$?” is a *counterpossible* conditional. While a general logical conditionalization operator $\mathtt{true}(\phi)$ remains an open problem in philosophical logic, Yudkowsky and Soares observe that if the agent’s world-model $M = (P, G)$ augments $P$ with a dependency graph $G$ encoding both causal and computational/subjunctive dependencies, one can apply Pearl’s $\mathtt{do}$ operator directly to a node representing the algorithm’s output. By Kleene’s (1938) second recursion theorem (“quining”), a program can construct a representation of its own source code and inputs. Using underlines to denote dequoting (so that if $x = 3$, $\textsc{Z}\underline{x}$ denotes the variable name $\textsc{Z}3$), **action-based FDT** is defined in Equation (4) of the reference paper as:

$$\mathrm{FDT}(P, G, x) \coloneqq \operatorname{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right).$$

Notice two critical features of action-based FDT:
1. It intervenes on the logical variable $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$, which is upstream of both the agent’s physical action $\textsc{Act}$ and any predictor who simulates the agent’s behavior upon observing $x$.
2. It is *updateless* (following Dai’s 2009 Updateless Decision Theory, and avoiding the “double update” of Yudkowsky’s 2010 Timeless Decision Theory): it does not condition $P$ on $\textsc{Obs} = x$. Instead, when the observation changes from $x$ to $y$, action-based FDT changes *which node in the graph $G$ it intervenes upon*, switching from $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ to $\textsc{fdt}(\underline{P}, \underline{G}, \underline{y})$.

### 2.2 The Mathematical Definition of P-FDT

Why is action-based FDT merely an expository simplification of **P-FDT**? In action-based FDT, the agent’s graph $G$ breaks the decision function into a family of separate random variables $\{\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})\}_{x \in \mathcal{X}}$—one for each possible observation $x$. When the agent observes $x$, she intervenes *only* on the node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ corresponding to her actual observation, while treating her own counterfactual outputs at other observations $y \neq x$ as untouched background random variables.

**P-FDT** eliminates this fragmentation by recognizing that the decision algorithm defines a *global policy* across observations. Following Footnotes 7 and 16 of the source text, let us formalize this precisely. (Here we present our formal synthesis of those two passages; in Section 5 we examine alternative interpretations of their exact wording.)

**Definition 1 (Policy Space).** Given a finite action space $\mathcal{A}$ and a finite (or countable) observation space $\mathcal{X}$, the *policy space* $\Pi \subseteq \mathcal{A}^{\mathcal{X}}$ is the set of all mappings $\pi : \mathcal{X} \to \mathcal{A}$ from observations to actions. For any $\pi \in \Pi$ and $x \in \mathcal{X}$, $\pi(x) \in \mathcal{A}$ denotes the action prescribed by policy $\pi$ upon receiving observation $x$.

**Definition 2 (P-FDT World-Model and Subjunctive Graph).** A P-FDT world-model is a pair $M = (P, G)$, where $P$ is a subjective probability distribution and $G$ is a directed acyclic graph over the variables of $P$ encoding causal and subjunctive dependencies. Specifically:
* $G$ contains a single policy node $\textsc{pfdt}(\underline{P}, \underline{G})$ taking values in $\Pi$, which represents the policy output of the P-FDT policy-selection function when given inputs $P$ and $G$.
* For any physical instantiation $i$ of the agent in the world-model receiving observation variable $\textsc{Obs}_i$ and taking physical action $\textsc{Act}_i$, both $\textsc{pfdt}(\underline{P}, \underline{G})$ and $\textsc{Obs}_i$ are parents of $\textsc{Act}_i$ in $G$. In the deterministic case where the agent’s body reliably executes her decision algorithm, the structural equation for $\textsc{Act}_i$ is simply function evaluation:
  $$\textsc{Act}_i(\pi, x) \coloneqq \pi(x).$$
* Whenever an environmental entity (such as a predictor, blackmailer, or game-theoretic opponent) bases its behavior on a prediction or simulation of the agent’s decision procedure, $\textsc{pfdt}(\underline{P}, \underline{G})$ is a parent of that entity’s prediction node $\textsc{Prediction}$ in $G$.

**Definition 3 (The P-FDT Decision Rule).** An agent following **P-FDT** with world-model $(P, G)$ and current observation $x \in \mathcal{X}$ selects an action in two steps:

1. *Policy Selection (Global Counterfactual Optimization):* The agent identifies the optimal policy $\pi^* \in \Pi$ by intervening on the logical node $\textsc{pfdt}(\underline{P}, \underline{G})$ to set its output to each candidate policy $\pi \in \Pi$, evaluating expected utility under the prior $P$:
   $$\mathrm{PFDT}_{\mathrm{pol}}(P, G) \coloneqq \operatorname{argmax}_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right). \tag{1}$$

2. *Policy Application (Local Execution):* The agent applies the selected policy $\pi^* = \mathrm{PFDT}_{\mathrm{pol}}(P, G)$ to her actual observation $x \in \mathcal{X}$ to output a physical action:
   $$\mathrm{PFDT}(P, G, x) \coloneqq \left[\mathrm{PFDT}_{\mathrm{pol}}(P, G)\right](x) = \left[\operatorname{argmax}_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right)\right](x). \tag{2}$$

Look closely at Equations (1) and (2). In **P-FDT**, the observation $x$ does not appear inside the expectation or the $\mathtt{do}(\cdot)$ operator at all! Every hypothetical $M^{\pi\hookrightarrow}$ is constructed by intervening on the single node $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$ against the unconditioned prior $P$. The observation $x$ plays a role only *after* the optimal policy $\pi^*$ has been determined, serving as the argument fed into $\pi^*(\cdot)$.

---

## 3. Applying P-FDT to Classic Newcomblike Dilemmas

To see how **P-FDT** operates in practice—and why it agrees with action-based FDT in single-agent dilemmas—let us apply it to two diagnostic cases from Yudkowsky and Soares’s paper: the **Transparent Newcomb Problem** (which is structurally isomorphic to Parfit’s Hitchhiker and the Mechanical Blackmail problem) and the **XOR Blackmail Problem**.

### 3.1 P-FDT in the Transparent Newcomb Problem

In the **Transparent Newcomb Problem**, both Box A ($\$1,000$) and Box B ($\$1,000,000$ or $\$0$) are transparent. The predictor is $99\%$ accurate and places $\$1,000,000$ in Box B if and only if she predicts that the agent will one-box (leave Box A behind) *upon observing that Box B is full*. Suppose our P-FDT agent, whom we will call **Polly**, walks into the room and observes that Box B is full ($x = \textit{full}$). Should she one-box or two-box?

Both CDT and EDT prescribe two-boxing: conditional on $\textsc{Obs} = \textit{full}$, the $\$1,000,000$ is already visibly sitting in Box B, so taking both boxes yields $\$1,001,000$ whereas one-boxing yields $\$1,000,000$. Foreseeing this, the predictor leaves Box B empty for CDT and EDT agents, who end up with only $\$1,000$.

How does Polly decide using **P-FDT**? Let us specify her world-model $(P^F, G^F)$:
* **Observation space:** $\mathcal{X} = \{\textit{full}, \textit{empty}\}$.
* **Action space:** $\mathcal{A} = \{\textit{onebox}, \textit{twobox}\}$.
* **Policy space:** $\Pi = \mathcal{A}^{\mathcal{X}}$ contains $2^2 = 4$ policies, which we write as $\pi_{ab}$ where $a = \pi(\textit{full})$ and $b = \pi(\textit{empty})$:
  * $\pi_{11}$: $(\textit{full} \mapsto \textit{onebox},\; \textit{empty} \mapsto \textit{onebox})$
  * $\pi_{12}$: $(\textit{full} \mapsto \textit{onebox},\; \textit{empty} \mapsto \textit{twobox})$
  * $\pi_{21}$: $(\textit{full} \mapsto \textit{twobox},\; \textit{empty} \mapsto \textit{onebox})$
  * $\pi_{22}$: $(\textit{full} \mapsto \textit{twobox},\; \textit{empty} \mapsto \textit{twobox})$
* **Structural equations in $G^F$:**
  * $\textsc{Accurate} \in \{\textit{accurate}, \textit{inaccurate}\}$ is an exogenous noise node with $P^F(\textsc{Accurate} = \textit{accurate}) = 0.99$ and $P^F(\textsc{Accurate} = \textit{inaccurate}) = 0.01$.
  * The predictor checks what the policy $\pi = \textsc{pfdt}(\underline{P^F}, \underline{G^F})$ does when the box is full, i.e., $\pi(\textit{full})$:
    $$\textsc{Prediction}(\pi, \textit{accurate}) = \begin{cases} 1 & \text{if } \pi(\textit{full}) = \textit{onebox}, \\ 2 & \text{if } \pi(\textit{full}) = \textit{twobox}, \end{cases}$$
    and $\textsc{Prediction}(\pi, \textit{inaccurate})$ flips $1$ and $2$.
  * $\textsc{Box B}(1) = \textit{full}$ and $\textsc{Box B}(2) = \textit{empty}$.
  * $\textsc{Obs}(\textsc{Box B}) = \textsc{Box B}$ (since Box B is transparent).
  * $\textsc{Act}(\pi, \textsc{Obs}) = \pi(\textsc{Obs})$.
  * $\textsc{V}(\textsc{Act}, \textsc{Box B})$ equals $\$1,001,000$ for $(\textit{twobox}, \textit{full})$, $\$1,000,000$ for $(\textit{onebox}, \textit{full})$, $\$1,000$ for $(\textit{twobox}, \textit{empty})$, and $\$0$ for $(\textit{onebox}, \textit{empty})$.

Now Polly executes Step 1 of **P-FDT** (Equation 1), computing $\mathbb{E}(\textsc{V} \mid \mathtt{do}(\textsc{pfdt}(\underline{P^F}, \underline{G^F}) = \pi))$ for each of the four policies:

1. **For $\pi_{11}$** ($\textit{onebox}$ if full, $\textit{onebox}$ if empty): Since $\pi_{11}(\textit{full}) = \textit{onebox}$, with probability $0.99$ ($\textit{accurate}$) the predictor predicts $1$, $\textsc{Box B} = \textit{full}$, $\textsc{Obs} = \textit{full}$, and Polly plays $\pi_{11}(\textit{full}) = \textit{onebox}$, getting $\$1,000,000$. With probability $0.01$ ($\textit{inaccurate}$), $\textsc{Box B} = \textit{empty}$, $\textsc{Obs} = \textit{empty}$, and Polly plays $\pi_{11}(\textit{empty}) = \textit{onebox}$, getting $\$0$.
   $$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt} = \pi_{11})\right) = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000.$$

2. **For $\pi_{12}$** ($\textit{onebox}$ if full, $\textit{twobox}$ if empty): Again $\pi_{12}(\textit{full}) = \textit{onebox}$, so with probability $0.99$ Box B is full and Polly one-boxes ($\$1,000,000$). With probability $0.01$, Box B is empty and Polly plays $\pi_{12}(\textit{empty}) = \textit{twobox}$, taking the $\$1,000$ in Box A.
   $$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt} = \pi_{12})\right) = 0.99(\$1,000,000) + 0.01(\$1,000) = \$990,010.$$

3. **For $\pi_{21}$** ($\textit{twobox}$ if full, $\textit{onebox}$ if empty): Since $\pi_{21}(\textit{full}) = \textit{twobox}$, with probability $0.01$ ($\textit{inaccurate}$) the predictor mistakenly fills Box B and Polly plays $\pi_{21}(\textit{full}) = \textit{twobox}$, getting $\$1,001,000$. With probability $0.99$ ($\textit{accurate}$), Box B is empty and Polly plays $\pi_{21}(\textit{empty}) = \textit{onebox}$, getting $\$0$.
   $$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt} = \pi_{21})\right) = 0.01(\$1,001,000) + 0.99(\$0) = \$10,010.$$

4. **For $\pi_{22}$** ($\textit{twobox}$ if full, $\textit{twobox}$ if empty): With probability $0.01$, Box B is full and Polly two-boxes ($\$1,001,000$); with probability $0.99$, Box B is empty and Polly two-boxes ($\$1,000$).
   $$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt} = \pi_{22})\right) = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$

Comparing the four values, $\pi^* = \pi_{12}$ uniquely maximizes expected utility at $\$990,010$. In Step 2 (Equation 2), Polly applies $\pi_{12}$ to her actual observation $x = \textit{full}$:

$$\mathrm{PFDT}(P^F, G^F, \textit{full}) = \pi_{12}(\textit{full}) = \textit{onebox}.$$

Notice an immediate formal elegance of **P-FDT** over the action-based FDT calculation in Section 6 of the reference paper. When Yudkowsky and Soares evaluate action-based FDT at $x = \textit{full}$, Fiona intervenes only on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full})$, which forces the authors to introduce an arbitrary prior probability $q = P^F(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty}) = \textit{twobox})$ representing Fiona’s uncertainty about what she herself would do if the box were empty! Under **P-FDT**, no such nuisance parameter $q$ is needed: because Polly optimizes over the complete policy $\pi = (\pi(\textit{full}), \pi(\textit{empty}))$ simultaneously, she solves for her optimal behavior across both branches in a single pass.

### 3.2 P-FDT in the XOR Blackmail Problem

Consider next Soares and Fallenstein’s (2015) **XOR Blackmail Problem**. A rumor says Polly’s house has a termite infestation costing $\$1,000,000$ in damages; her prior probability of termites is $p \in (0,1)$. An infallible predictor learns whether she has termites and sends a blackmail letter demanding $\$1,000$ if and only if *either* (i) she does not have termites and will $\textit{pay}$ upon receiving the letter, *or* (ii) she has termites and will $\textit{refuse}$ upon receiving the letter. Suppose Polly receives the letter ($x = \textit{letter}$, as opposed to $x = \emptyset$ where no letter arrives and no payment action is available).

An EDT agent conditions on $\textsc{Obs} = \textit{letter}$ and $\textsc{Act} = \textit{pay}$, which logically entails no termites ($\$0$ damage, $-\$1,000$ payment), whereas conditioning on $\textsc{Obs} = \textit{letter}$ and $\textsc{Act} = \textit{refuse}$ entails termites ($-\$1,000,000$ damage). Thus EDT pays the blackmailer to “buy good news.”

In **P-FDT**, whether Polly has termites ($\textsc{Infestation} \in \{\textit{termites}, \textit{clean}\}$) is an exogenous node with prior $p$, causally and subjunctively independent of $\textsc{pfdt}(\underline{P^F}, \underline{G^F})$. The only nontrivial policy choice is what to do when $x = \textit{letter}$: let $\pi_{\mathrm{pay}}$ prescribe $\textit{pay}$ upon seeing $\textit{letter}$, and $\pi_{\mathrm{refuse}}$ prescribe $\textit{refuse}$ upon seeing $\textit{letter}$ (when $x = \emptyset$, the agent takes the default null action $\textit{nothing}$ at $\$0$ cost).
* Under $\mathtt{do}(\textsc{pfdt} = \pi_{\mathrm{pay}})$: With probability $p$ Polly has termites, the predictor does *not* send the letter ($x = \emptyset$), and Polly loses $\$1,000,000$. With probability $1-p$ Polly has no termites, the predictor *does* send the letter ($x = \textit{letter}$), and Polly pays $\$1,000$. Expected utility:
  $$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt} = \pi_{\mathrm{pay}})\right) = -p(\$1,000,000) - (1-p)(\$1,000).$$
* Under $\mathtt{do}(\textsc{pfdt} = \pi_{\mathrm{refuse}})$: With probability $p$ Polly has termites, the predictor sends the letter ($x = \textit{letter}$), Polly refuses to pay, and she loses $\$1,000,000$ from the termites. With probability $1-p$ she has no termites, no letter is sent, and she loses $\$0$. Expected utility:
  $$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt} = \pi_{\mathrm{refuse}})\right) = -p(\$1,000,000).$$

Since $-p(\$1,000,000) > -p(\$1,000,000) - (1-p)(\$1,000)$ for all $p < 1$, **P-FDT** selects $\pi^* = \pi_{\mathrm{refuse}}$. Applying $\pi_{\mathrm{refuse}}$ to $x = \textit{letter}$, Polly refuses to pay! Even though holding the letter and knowing she will refuse means she certainly has termites, in her counterfactual for $\pi_{\mathrm{pay}}$ she does not imagine the termites vanishing; she imagines a world where she still has termites with probability $p$, gets the letter only when she is termite-free, and wastes $\$1,000$ whenever she is lucky enough not to have termites.

---

## 4. Where P-FDT Diverges: Multi-Agent Dilemmas and Cross-Branch Coordination

Why did Yudkowsky and Soares remark in Footnotes 7 and 16 that the distinction between iterating over policies (**P-FDT**) and iterating over actions (action-based FDT) *“only matters in multi-agent dilemmas”*?

Let us state the precise mathematical reason (this formal characterization is our own analytical synthesis of the source’s remark). In a single-agent decision problem where the environment realizes at most one observation $x \in \mathcal{X}$ per play and predictors only care about the action $\pi(x)$ taken at the realized observation, the expected utility of a policy $\pi \in \Pi$ decomposes additively across observation branches, or decouples such that $\pi(x)$ and $\pi(y)$ ($y \neq x$) do not interact within the same state of the world. In such separable settings, maximizing jointly over the tuple $(\pi(x))_{x \in \mathcal{X}}$ (as **P-FDT** does) yields the exact same prescription at $x$ as maximizing coordinate-wise over $\pi(x)$ while holding $(\pi(y))_{y \neq x}$ fixed (as action-based FDT does).

However, in **multi-agent dilemmas** where multiple physical copies or psychological twins of the agent exist in the *same* world and receive *different* observations, the agents’ actions across different observations interact directly in the utility function! In that setting, action-based FDT’s coordinate-wise intervention fails dramatically, whereas **P-FDT** achieves optimal coordination.

### Example: The Asymmetric-Observation Twin Prisoner’s Dilemma

To see this divergence clearly, let us construct an explicit multi-agent dilemma (our own example designed to illustrate the claim in Footnotes 7 and 16).

> **Dilemma (Asymmetric-Observation Twin Prisoner’s Dilemma).** Polly and her perfect psychological twin—who implements the exact same decision algorithm with the same world-model $(P, G)$—are placed in separate, causally isolated rooms. A referee turns on a $\textit{red}$ light in one room and a $\textit{blue}$ light in the other room; Polly’s prior probability is $0.5$ that she is in the $\textit{red}$ room and $0.5$ that she is in the $\textit{blue}$ room. Each twin observes the light color in her own room ($x \in \{\textit{red}, \textit{blue}\}$) and must simultaneously choose $\textit{cooperate}$ ($C$) or $\textit{defect}$ ($D$). As in the standard Twin Prisoner’s Dilemma, mutual cooperation yields $\$1,000,000$ each; mutual defection yields $\$1,000$ each; and if one defects while the other cooperates, the defector gets $\$1,001,000$ and the cooperator gets $\$0$. Polly observes $x = \textit{red}$. Should she cooperate or defect?

Let us compare how **action-based FDT** (Equation 4 of the reference paper) and **P-FDT** (our Equations 1–2) analyze this dilemma.

#### How Action-Based FDT Fails

In action-based FDT, the graph $G$ contains two distinct logical nodes for the two possible observations: $\textsc{fdt}(\underline{P}, \underline{G}, \textit{red})$ and $\textsc{fdt}(\underline{P}, \underline{G}, \textit{blue})$. Whoever is in the red room executes $a_{\mathrm{red}} = \textsc{fdt}(\underline{P}, \underline{G}, \textit{red})$, and whoever is in the blue room executes $a_{\mathrm{blue}} = \textsc{fdt}(\underline{P}, \underline{G}, \textit{blue})$.

When the agent observes $x = \textit{red}$, action-based FDT evaluates:

$$\mathrm{FDT}(P, G, \textit{red}) = \operatorname{argmax}_{a \in \{C, D\}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \textit{red}) = a\right)\right).$$

Look at what happens under the surgical intervention $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \textit{red}) = a)$:
* It fixes the action of the twin in the $\textit{red}$ room to $a$.
* Because $\textsc{fdt}(\underline{P}, \underline{G}, \textit{blue})$ is a *separate root node* in $G$ not downstream of $\textsc{fdt}(\underline{P}, \underline{G}, \textit{red})$, the intervention leaves $\textsc{fdt}(\underline{P}, \underline{G}, \textit{blue})$ completely untouched!

Let $q = P(\textsc{fdt}(\underline{P}, \underline{G}, \textit{blue}) = C)$ be the agent’s prior probability that the blue-room node outputs $C$. Furthermore, recall that under $P$ (which is not conditioned on $\textsc{Obs} = \textit{red}$), the agent has a $0.5$ chance of being the red-room twin and a $0.5$ chance of being the blue-room twin:
* If she sets $\textsc{fdt}(\underline{P}, \underline{G}, \textit{red}) = C$:
  * With probability $0.5$ she is the red-room twin (playing $C$), earning $q(\$1,000,000) + (1-q)(\$0)$.
  * With probability $0.5$ she is the blue-room twin (playing $C$ with probability $q$ and $D$ with probability $1-q$ against the red-room twin’s $C$), earning $q(\$1,000,000) + (1-q)(\$1,001,000)$.
  * Total expected utility for $a = C$:
    $$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{fdt}(\dots, \textit{red}) = C)\right) = \$1,000,000 q + \$500,500(1-q).$$
* If she sets $\textsc{fdt}(\underline{P}, \underline{G}, \textit{red}) = D$:
  * With probability $0.5$ she is the red-room twin (playing $D$), earning $q(\$1,001,000) + (1-q)(\$1,000)$.
  * With probability $0.5$ she is the blue-room twin (playing against the red-room twin’s $D$), earning $q(\$0) + (1-q)(\$1,000)$.
  * Total expected utility for $a = D$:
    $$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{fdt}(\dots, \textit{red}) = D)\right) = \$500,500 q + \$1,000(1-q).$$

Wait—Look closely at those two expressions! In action-based FDT, because the agent does *not* update on $\textsc{Obs} = \textit{red}$ (she averages $50/50$ over being the red-room twin and the blue-room twin), when she intervenes on $\textsc{fdt}(\underline{P}, \underline{G}, \textit{red})$, she internalizes the externalities that the red-room twin’s action imposes on the blue-room twin! Specifically, for any $q \in [0,1]$, $\$1,000,000 q + \$500,500(1-q)$ is strictly greater than $\$500,500 q + \$1,000(1-q)$ (by $\$499,500$). So in this additive Prisoner’s Dilemma, even action-based FDT’s updatelessness saves cooperation!

*Why, then, does action-based FDT fail in multi-agent dilemmas?* Let us modify the payoff matrix slightly into a **Twin Coordination / Threshold Dilemma** (such as the voting coalition problem in Section 10 of the reference paper, or a noisy stag hunt):

> **Dilemma (Asymmetric-Observation Twin Stag Hunt / Coalition Dilemma).** The setup is identical—one twin sees $\textit{red}$, the other sees $\textit{blue}$—Wait: suppose each twin must decide whether to pay a cost of $\$10,000$ to $\textit{contribute}$ ($C$) to a joint venture or $\textit{shirk}$ ($S$, cost $\$0$). The venture succeeds, paying $\$1,000,000$ to each twin, **if and only if both twins contribute**. If either twin shirks, the venture fails and anyone who contributed loses their $\$10,000$.

Let us re-evaluate **action-based FDT** on this Asymmetric-Observation Twin Stag Hunt when the agent sees $\textit{red}$ and has a low prior $q = P(\textsc{fdt}(\underline{P}, \underline{G}, \textit{blue}) = C)$ (say, $q = 0$, because she expects the blue-room node to shirk):
* Under $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \textit{red}) = C)$: Since the blue-room node is held fixed at $S$ ($q = 0$), the joint venture is guaranteed to fail ($0\%$ chance of $\$1,000,000$), while the red-room twin wastes $\$10,000$ (which happens to the agent with probability $0.5$). Thus:
  $$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{fdt}(\dots, \textit{red}) = C)\right) = 0.5(-\$10,000) + 0.5(\$0) = -\$5,000.$$
* Under $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \textit{red}) = S)$: Neither twin contributes, so both get $\$0$:
  $$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{fdt}(\dots, \textit{red}) = S)\right) = \$0.$$

Because action-based FDT intervenes on only one observation node at a time, $\textsc{fdt}(\underline{P}, \underline{G}, \textit{red})$ and $\textsc{fdt}(\underline{P}, \underline{G}, \textit{blue})$ play a non-cooperative game against each other! If $q < 0.005$, action-based FDT gets trapped in the bad Nash equilibrium $(S, S)$, outputting $\textit{shirk}$ at both $\textit{red}$ and $\textit{blue}$ and walking away with $\$0$—Suffering from the exact same prior-sensitivity and equilibrium-selection pathology that Yudkowsky and Soares criticize in EDT and ratified CDT!

*(Even worse, suppose the two twins face a **Coordination Game with Asymmetric Roles**: to win $\$1,000,000$, the $\textit{red}$ twin and $\textit{blue}$ twin must play matching actions $(A, A)$ or $(B, B)$, where neither action has a prior advantage. Or suppose in our first Prisoner’s Dilemma the two agents are not symmetric under the prior—for example, Polly knows from the start that she is in the $\textit{red}$ room because $\textit{red}$ is encoded in her background model, while her twin’s observation $\textit{blue}$ is generated in the environment. Whenever the agent knows her own observation will be $\textit{red}$ with probability $1$ while a copy in the environment observes $\textit{blue}$, action-based FDT’s intervention on $\textit{red}$ cares $100\%$ about the $\textit{red}$ twin’s payoff and $0\%$ about the $\textit{blue}$ twin’s payoff, causing action-based FDT to **defect** in the Twin Prisoner’s Dilemma as well!)*

#### How P-FDT Succeeds

Now watch how **P-FDT** resolves both the Asymmetric-Observation Twin Stag Hunt and the known-observation Twin Prisoner’s Dilemma effortlessly.

In **P-FDT**, there are not two separate nodes for $\textit{red}$ and $\textit{blue}$; there is a single policy node $\textsc{pfdt}(\underline{P}, \underline{G})$ shared by both twins. The red-room twin executes $\pi(\textit{red})$ and the blue-room twin executes $\pi(\textit{blue})$. Polly evaluates the four policies $\pi \in \{\pi_{CC}, \pi_{CS}, \pi_{SC}, \pi_{SS}\}$ in the Twin Stag Hunt:

1. $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{CC})$: Both the red-room twin and the blue-room twin contribute. The venture succeeds with certainty, and each twin pays $\$10,000$ to receive $\$1,000,000$:
   $$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt} = \pi_{CC})\right) = \$1,000,000 - \$10,000 = \$990,000.$$
2. $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{CS})$ or $\pi_{SC}$: One twin contributes and loses $\$10,000$; the other shirks and gets $\$0$; the venture fails:
   $$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt} = \pi_{CS})\right) = 0.5(-\$10,000) + 0.5(\$0) = -\$5,000.$$
3. $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{SS})$: Both twins shirk:
   $$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt} = \pi_{SS})\right) = \$0.$$

Regardless of any prior beliefs $q$, **P-FDT** directly compares the global policies, sees that $\pi_{CC}$ yields $\$990,000$, selects $\pi^* = \pi_{CC}$, and applies $\pi_{CC}(\textit{red}) = C$. By intervening on the *policy* rather than the observation-indexed *action*, **P-FDT** transforms cross-branch coordination from an intra-agent Nash equilibrium problem into a single global optimization problem.

---

## 5. Open Questions and Operational Extensions in P-FDT

Because Yudkowsky and Soares relegate **P-FDT** to Footnotes 7 and 16 to keep their main exposition accessible, several important technical questions about how to operationalize P-FDT in full generality remain unresolved in the source text. Here we explicitly distinguish what the reference article states from our own proposed operational completions.

### 5.1 What Is the Domain of a Policy? ($\mathcal{X}$ vs. $\mathcal{M} \times \mathcal{X}$)

There is a subtle tension between the wording of Footnote 7 and Footnote 16 in the source paper:
* **Footnote 7** defines policies as *“mappings from observations to actions”* ($\pi : \mathcal{X} \to \mathcal{A}$).
* **Footnote 16** states that the agent *“intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action.”*

What are the “inputs” to the FDT algorithm? In Equation (4) of the paper, the inputs are the entire triple $(P, G, x)$—not just the observation $x$, but also the agent’s world-model $M = (P, G)$!

In most decision problems, $(P, G)$ is fixed and common between the agent and any predictors or twins, so $\pi : \mathcal{X} \to \mathcal{A}$ and $\pi : \mathcal{M} \times \mathcal{X} \to \mathcal{A}$ are equivalent. However, recall how Yudkowsky and Soares formalize the **Smoking Lesion Problem** in Section 6 of their paper: because the lesion causes the agent to love smoking, Fiona does not know whether her own world-model uses the smoking-loving distribution $P_S^F$ (with utility $\mathcal{U}_S$) or the smoking-disliking distribution $P_R^F$ (with utility $\mathcal{U}_R$). Consequently, in Figure 4 of the source paper, Fiona’s graph $G^F$ contains *two* model-indexed nodes: $\textsc{fdt}(\underline{P_S^F}, \underline{G^F})$ and $\textsc{fdt}(\underline{P_R^F}, \underline{G^F})$.

This raises an open question not settled by the paper: in **P-FDT**, should the node of intervention be parameterized by the model—$\textsc{pfdt}(\underline{P}, \underline{G})$, outputting $\pi : \mathcal{X} \to \mathcal{A}$—or should it be an unparameterized universal node $\textsc{pfdt}()$ outputting a *meta-policy* $\Pi_{\mathrm{meta}} \ni \mu : \mathcal{M} \times \mathcal{X} \to \mathcal{A}$ that maps world-models and observations to actions?

**Our Operational Proposal:** Both formulations are viable, and each serves a distinct purpose:
1. **Model-Parameterized P-FDT ($\pi : \mathcal{X} \to \mathcal{A}$, our Definition 3):** When the agent’s preferences and prior $(P, G)$ are fixed for a given agent type, intervening on $\textsc{pfdt}(\underline{P}, \underline{G})$ to select $\pi : \mathcal{X} \to \mathcal{A}$ is the cleanest operationalization. In the Smoking Lesion Problem, an agent with model $(P_S^F, G^F)$ intervenes on $\textsc{pfdt}(\underline{P_S^F}, \underline{G^F})$ (holding $\textsc{pfdt}(\underline{P_R^F}, \underline{G^F})$ fixed) and smokes, whileavoiding any forced utilitarian trade-offs between different utility functions $\mathcal{U}_S$ and $\mathcal{U}_R$.
2. **Universal Meta-Policy P-FDT ($\mu : \mathcal{M} \times \mathcal{X} \to \mathcal{A}$):** Suppose two agents in a multi-agent dilemma are *imperfect* twins who share the P-FDT algorithm and a common meta-prior $P_0$, but have acquired slightly different world-models $M_1, M_2 \in \mathcal{M}$ before the game begins. If they intervene on $\textsc{pfdt}(\underline{M_1})$ and $\textsc{pfdt}(\underline{M_2})$ separately, they cannot coordinate! By intervening on the universal node $\textsc{pfdt}$ to choose a meta-policy $\mu : \mathcal{M} \times \mathcal{X} \to \mathcal{A}$ that maximizes expected utility under a shared meta-prior $P_0$:
   $$\mathrm{PFDT}(M, x) \coloneqq \left[\operatorname{argmax}_{\mu \in \mathcal{A}^{\mathcal{M} \times \mathcal{X}}} \mathbb{E}_{P_0}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt} = \mu\right)\right)\right](M, x),$$
   agents with different models $M_1 \neq M_2$ can still achieve full functional coordination and Rawlsian bargaining behind a veil of ignorance.

### 5.2 Null-Probability Observations and Off-Path Indeterminacy

A second formal issue arises in **P-FDT** that does not arise in action-based FDT. Suppose that in the Transparent Newcomb Problem or the Mechanical Blackmail Problem, the predictor is **100% infallible** ($P(\textsc{Accurate} = \textit{accurate}) = 1$). 

Consider what happens when Polly evaluates the two one-boxing policies $\pi_{11}$ ($\textit{onebox}$ if full, $\textit{onebox}$ if empty) and $\pi_{12}$ ($\textit{onebox}$ if full, $\textit{twobox}$ if empty) against an infallible predictor. Because $\pi_{11}(\textit{full}) = \pi_{12}(\textit{full}) = \textit{onebox}$, an infallible predictor *always* fills Box B under both policies. Consequently, under both $\mathtt{do}(\textsc{pfdt} = \pi_{11})$ and $\mathtt{do}(\textsc{pfdt} = \pi_{12})$, the event $\textsc{Obs} = \textit{empty}$ has probability $0$! Both $\pi_{11}$ and $\pi_{12}$ yield an expected utility of exactly $\$1,000,000$. Thus, the $\operatorname{argmax}$ in Equation (1) is a tie between $\pi_{11}$ and $\pi_{12}$: if Polly actually were to observe $\textsc{Obs} = \textit{empty}$ (an unexpected off-path observation), pure maximization of Equation (1) would be indifferent between one-boxing and two-boxing on an empty box!

Even more starkly, in the Mechanical Blackmail Problem with an infallible blackmailer, under $\pi_{\mathrm{refuse}}$ the blackmailer *never* sends the blackmail letter ($P(\textsc{Obs} = \textit{blackmail} \mid \mathtt{do}(\textsc{pfdt} = \pi_{\mathrm{refuse}})) = 0$), whereas under $\pi_{\mathrm{pay}}$ the blackmailer *always* sends it ($P(\textsc{Obs} = \textit{blackmail} \mid \mathtt{do}(\textsc{pfdt} = \pi_{\mathrm{pay}})) = 1$). Here $\pi_{\mathrm{refuse}}$ strictly beats $\pi_{\mathrm{pay}}$ ($\$0 > -\$1,000$), so $\pi_{\mathrm{refuse}}$ is uniquely selected even when $\textsc{Obs} = \textit{blackmail}$ has zero probability under $\pi_{\mathrm{refuse}}$. Yet for any observation $x_0$ whose realization probability is $0$ across *all* optimal policies, $\pi^*(x_0)$ is unconstrained by Equation (1).

**Our Operational Proposal (Trembling-Hand Regularization):** Just as Selten (1975) resolved off-path indeterminacy in extensive-form games via “trembling-hand” perturbations—and just as Yudkowsky and Soares themselves model predictors with a $1 - \varepsilon = 0.99$ accuracy parameter in Newcomb’s problem—an operational **P-FDT** agent should require that her world-model $(P, G)$ assign strictly positive probability $\varepsilon > 0$ to environmental noise on all observation channels (so that $P(\textsc{Obs} = x \mid \mathtt{do}(\textsc{pfdt} = \pi)) > 0$ for all $x \in \mathcal{X}$ and $\pi \in \Pi$), or evaluate policies in the limit as $\varepsilon \to 0^+$. As we saw in Section 3.1, any $\varepsilon > 0$ immediately breaks the tie between $\pi_{12}$ and $\pi_{11}$ in favor of $\pi_{12}$ ($\$990,010 > \$990,000$).

### 5.3 Learning Subjunctive Graphs and Computational Complexity

Finally, **P-FDT** inherits the foundational open problems identified by Yudkowsky and Soares in Sections 3, 5, and 10 of their paper, plus a computational scaling challenge of its own:
1. *Deducing Subjunctive Structure:* While Pearl (2000) showed how to infer causal graphs $G^C$ from physical observations and interventions, we lack an analogous formal calculus for learning the subjunctive dependency graph $G^F$ and evaluating counterpossibles ($\mathtt{true}(\phi)$) from data.
2. *Exponential Policy Space:* Whereas action-based FDT iterates over $|\mathcal{A}|$ actions at decision time, **P-FDT** iterates over $|\Pi| = |\mathcal{A}|^{|\mathcal{X}|}$ policies. For real-world agents with large observation histories $\mathcal{X}$, exhaustive enumeration of $\mathcal{A}^{\mathcal{X}}$ is intractable. A practical P-FDT agent must therefore restrict policy search to a low-dimensional subspace of relevant observation equivalence classes—specifically, partitioning $\mathcal{X}$ into only those equivalence classes of observations that predictors or copies in the current dilemma actually distinguish.

---

## 6. Conclusion

**Policy functional decision theory (P-FDT)** represents the most unified and mathematically coherent formulation of functional decision-making. By shifting the locus of counterfactual intervention from physical actions ($\textsc{Act}$) or observation-specific algorithm outputs ($\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$) to the global policy mapping itself ($\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$), P-FDT captures the full normative force of Yudkowsky and Soares’s global perspective. It one-boxes in standard and transparent Newcomb problems, smokes in the smoking lesion problem, resists extortion in blackmail dilemmas, and—where even action-based FDT can falter—enables copies and multi-agent coalitions receiving different observations to coordinate seamlessly on globally optimal outcomes.

---

## References

* Dai, W. (2009). “Towards a New Decision Theory.” *LessWrong*.
* Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Gibbard, A., & Harper, W. L. (1978). “Counterfactuals and Two Kinds of Expected Utility.” In *Foundations and Applications of Decision Theory*, Vol. 1, D. Reidel.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Kleene, S. C. (1938). “On Notation for Ordinal Numbers.” *Journal of Symbolic Logic*, 3(4), 150–155.
* Nozick, R. (1969). “Newcomb’s Problem and Two Principles of Choice.” In *Essays in Honor of Carl G. Hempel*, D. Reidel, 114–146.
* Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
* Pearl, J. (1996). “Causation, Action, and Counterfactuals.” In *Proceedings of the 6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-96)*, 51–73.
* Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Skyrms, B. (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Soares, N., & Fallenstein, B. (2015). “Toward Idealized Decision Theory.” *arXiv:1507.01986*.
* Yudkowsky, E. (2010). *Timeless Decision Theory*. The Singularity Institute.
* Yudkowsky, E., & Soares, N. (2017). “Functional Decision Theory: A New Theory of Instrumental Rationality.” *arXiv:1710.05060v2*.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Framework**

I'm focusing on defining the scope and parameters for an essay explaining Policy Functional Decision Theory. The goal is to make it accessible yet mathematically sound, given the user is an expert. The provided paper is my main source for this undertaking, and is guiding my direction. I'm prioritizing accuracy and clarity.


**Refining the Focus**

I'm now zeroing in on the specifics from the provided paper, especially those key footnotes. I need to make sure the essay caters to mathematically savvy readers while ensuring clarity about both the formal procedures and the underlying philosophical concepts. The target word count remains, but the details are firming up.


**Clarifying the Core**

I'm now integrating the nuanced view of Policy FDT, or **P-FDT**, distinguishing it from other theories like CDT and EDT. I'm focusing on providing mathematical definitions, equations, and examples for clarity. I'm prioritizing explaining P-FDT's evaluation of actions and policies. I'm trying to ensure the explanation covers relevant dependencies and counterfactuals, even developing interpretations for open questions.


**Detailing the Approach**

I'm now carefully differentiating between the source's claims and my additional interpretations or proposals to ensure accuracy. I'm aiming for a substantive, mathematically rigorous essay, not a reaction to just one case. I'm using examples, including multi-agent dilemmas, to showcase where P-FDT diverges from standard FDT. Quotes will be faithful to the source, and I'm aiming for the 2400-3000 word count. The conclusion will be brief, avoiding repetition.


**Analyzing the Intervention**

I am now focusing on the nuances of the formal definition of FDT, especially the intervention process. I'm exploring the implications of treating the FDT function itself as a node in the causal graph, rather than conditioning on observations. I'm unpacking how this differs when evaluating various observational states, especially in scenarios like Transparent Newcomb, to clarify how the "do" operator functions within the algorithm. I'm aiming to articulate the difference between acting in response to an observation versus updating beliefs based on it.


**Defining Policy Actions**

I'm now clarifying the nature of "inputs" within P-FDT. I'm focusing on the contrast between standard FDT inputs $(P, G, x)$ and the policy's role as a mapping from inputs to actions. I'm considering treating the FDT function as a separate random variable with a prior probability, which will help distinguish actions from policies. I am paying close attention to the ambiguity between the footnotes in the paper. I'm aiming to formalize this for my expert audience.


**Formalizing the Policies**

I'm now detailing the policy's role, and distinguishing the policy-selection function $\mathrm{PFDT}_{\text{pol}}$ from the FDT algorithm. I'm exploring the implications of treating the policy selector itself as a mapping, considering its input and output. I'm carefully analyzing the differences between a policy that takes the entire world-model as input versus one that only takes the observation. I am including both as open questions in the source to maximize clarity. I'm developing a mathematical notation to represent policy selection, working through the relevant equations.


**Formalizing the Distinction**

I'm now detailing the implications of the P-FDT function's inputs. Specifically, I'm examining the function definition: `PFDT(P, G, x)`. I'm comparing the cases where the input is solely the observation $x$, versus the entire tuple of $(P, G, x)$. I'm also examining the implications of a policy $\pi : \mathcal{M} \times \mathcal{X} \to \mathcal{A}$ mapping the epistemic/evaluative state $M=(P,G)$ along with the observation $x$ to an action! I'm planning to highlight this distinction, and to address the uncertainties from the footnote in the source.


**Investigating the Dilemmas**

I'm now diving into the core difference in multi-agent dilemmas. Action-based FDT intervenes on `fdt(P, G, x)` while holding `fdt(P, G, y)` fixed, unlike Policy-FDT. In Transparent Newcomb, this holds true because Fiona's actions don't need to be coordinated. I'm exploring when a node is a policy.


**Exploring the Dilemma**

I'm now investigating a specific multi-agent dilemma where I can showcase the failure of action-based FDT compared to policy FDT. It involves asymmetric observations, where twins in separate rooms see different colored lights. Action-based FDT acts independently on each observation, whereas policy FDT takes a joint approach. This example should clarify the key distinctions.


**Clarifying the Application**

I am now focusing on how P-FDT handles the Twin Prisoner's Dilemma with asymmetric observations. Action-based FDT fails because one twin's action is independent of the other's observation. However, P-FDT implements a policy function that operates jointly, ensuring coordinated action, and thus cooperation. This highlights P-FDT's unique advantage.


**Illustrating the Impact**

I'm now detailing how Policy-FDT offers a solution in scenarios like the Twin Prisoner's Dilemma, using the observation of $\textit{red}$ as an example. Applying the policy $\pi$ to the world-model $P$ and the observation $\textit{red}$, yields a cooperative action that's preferable. The policy's potential payoff greatly exceeds that of asymmetric policies or a defection-defection outcome.


**Analyzing the Optimization**

I'm now investigating the conditions under which pointwise and joint optimization of the policy function align. I'm focusing on the separability of the objective function across observations. I'm considering scenarios, including single-agent settings, where a predictor anticipates outcomes across multiple observation branches and the implication for action-based FDT. Even in a single-agent problem, I'm finding that if a predictor forecasts both fdt outcomes, there's a need to consider a Nash equilibrium.


**Distinguishing the Dynamics**

I'm now detailing the implications of my findings on the differences between action-based and policy-based FDT. Specifically, in multi-agent dilemmas with copies of the agent, and asymmetric observations, the payoffs directly interact in the same world. Action-based finds local optima while P-FDT finds the team optimum!

\n\n


**Formalizing the Context**

I'm now detailing the implications of my findings, and I've integrated a framework focused on expected utility and the do-calculus. Specifically, I am describing the expected utility framework and the graphical do-calculus formulation of EDT, CDT, and standard action-based FDT. My current focus is to explain the use of Pearl's do operator on a logical variable representing the algorithm's output, contrasting how CDT, action-based FDT, and P-FDT handle observations x ∈ X. I'm aiming for clarity in these distinctions for my expert readers.


I'm now detailing the implications of my findings, and I've introduced policy optimization in P-FDT. I'm focusing on the contrast with action-based FDT, specifically, in how they handle the graphical structure G. I am elaborating on the two-stage evaluation procedure: policy optimization and policy application, within the framework. I am highlighting differences in the intervention nodes.


**Applying P-FDT Effectively**

I'm working on explaining P-FDT's practical application, especially in the Transparent Newcomb problem. I'm illustrating this with explicit policies and calculating expected utilities. My current focus is showing how P-FDT straightforwardly chooses the optimal policy, demonstrating its efficient single-pass optimization, a key advantage of the approach.


**Elaborating on Optimizations**

I am now clarifying why policy FDT is superior in multi-agent dilemmas. Action-based FDT, unlike policy FDT, requires $q$ to be used as a free parameter, while the expected utility decomposes additively. I am also discussing how the two converge in scenarios like transparent Newcomb.


**Refining the Example**

I'm now detailing an asymmetric Prisoner's Dilemma to show P-FDT's advantages, using a red/blue room scenario for clarity. I'm focusing on contrasting how action-based FDT fails because it can't coordinate, whereas policy FDT selects the cooperative policy, and thus the agents cooperate. I am aiming to illustrate policy selection for optimal team payoffs.


**Generalizing the Approach**

I'm now generalizing that, whenever the outcome relies on different evaluations, action-based FDT is an intra-algorithmic game, and P-FDT performs team optimization. I'm focusing on open questions, especially regarding policy domains; contrasting mappings from observations versus inputs, clarifying how P-FDT manages uncertainty in situations like Fiona's smoking lesion.


**Addressing Open Questions**

I'm now focusing on critical open questions. I'm starting with policy evaluation under an epistemic prior and utility tradeoffs, exploring questions around the implications of zero-probability observations. I'm also grappling with computational tractability and the implications on searching for optimal policies given the large policy domains involved. The goal is clarity and practical utility.


**Clarifying the Conclusion**

I'm now writing the conclusion, summarizing how Policy-FDT is the logical outcome of the functional perspective. I'll highlight key advantages like team optimization and policy learning, emphasizing its solutions to dilemmas. I'll also address the paper's open questions about computational tractability and counterfactuals, while reemphasizing clarity.


**Expanding the Distinction**

I'm now detailing the important differences between acting on *outcomes* versus acting on *policies*. This is a crucial clarification for multi-agent settings, aligning with Footnote 16. I am carefully re-reviewing calculations within the source paper and checking mathematical notation for consistency, precision, and clarity. I'm focusing especially on symbols like $\mathcal{A}, \mathcal{X}, \mathcal{O}, \mathcal{U}$ to ensure they're accurately applied.


```
