# 029_fdt_policy_google_gemini-4-argon_rhigh_phigh / 00001

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/feed0702-5111-4bb6-b55b-1a38f15549cd/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/feed0702-5111-4bb6-b55b-1a38f15549cd/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Policy Functional Decision Theory (P-FDT): A Mathematical Account of Policy Selection Under Subjunctive Dependence

## 1. Introduction: From Physical Acts to Mathematical Policies

For decades, normative decision theory was split between two primary contenders: **Evidential Decision Theory (EDT)** and **Causal Decision Theory (CDT)**. When evaluated by average utility achieved across decision problems, neither theory dominates the other. EDT prescribes taking only the opaque box in Newcomb's problem—walking away with $\$1,000,000$—yet foolishly prescribes refraining from smoking in Skyrms' (1980) smoking lesion problem to avoid "bad news" about a preexisting carcinogenic lesion. Conversely, CDT smokes in the smoking lesion problem, recognizing that smoking does not cause the lesion, yet two-boxes in Newcomb's problem and walks away with a meager $\$1,000$. Worse still, in dilemmas such as Parfit's (1986) hitchhiker problem, Drescher's (2006) transparent Newcomb problem, and Soares and Fallenstein's (2015) mechanical blackmail problem, both EDT and CDT fail to secure the high-utility outcome unless granted advance opportunities to pay for binding precommitments.

In *"Functional Decision Theory: A New Theory of Instrumental Rationality"*, Eliezer Yudkowsky and Nate Soares (2017) resolve this impasse by proposing that a rational agent should treat her decision not as a standalone physical token, but as the logical output of a fixed mathematical function. Rather than asking CDT's question ("Which physical act of mine causes the best outcome?") or EDT's question ("Which physical act of mine would be the best news to hear I took?"), a functional decision theorist asks: *"Which output of this very function would yield the best outcome?"*

Yet within Yudkowsky and Soares's paper lies an important structural distinction between two ways of formalizing this principle. In the main text of their article, for expository convenience, the authors formalize what we may call **action-based Functional Decision Theory (A-FDT)**, in which the agent intervenes on a node representing the action output for her specific current observation. However, in Footnotes 7 and 16, the authors explain that their actual preferred theory—which we will refer to throughout this essay as **Policy Functional Decision Theory (P-FDT)**—operates over *policies* rather than isolated actions. As Footnote 7 states:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

Footnote 16 elaborates on the mechanics of this procedure:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

In this essay, we develop a self-contained mathematical account of **P-FDT**, showing how it evaluates policies, how it models counterfactuals and subjunctive dependencies, how it applies to classic single-agent dilemmas, and why—just as Footnotes 7 and 16 indicate—it diverges sharply from action-based FDT in multi-agent settings. Where the brief remarks in the source leave formal questions open, we identify those uncertainties and provide rigorous operational completions.

---

## 2. Formalizing P-FDT: Models, Hypotheticals, and Policy Interventions

### 2.1 The Expected Utility Framework

Following Savage (1954), Gibbard and Harper (1978), and Joyce (1999), Yudkowsky and Soares frame EDT, CDT, A-FDT, and **P-FDT** as expected utility theories. Let $\mathcal{O} = \{o_1, o_2, \dots\}$ be a countable set of outcomes, $\mathcal{A}$ a finite set of physical actions, $\mathcal{X}$ a countable (or finite) set of possible observation histories, and $\mathcal{U}: \mathcal{O} \to \mathbb{R}$ a bounded utility function. In the general expected utility schema (Equation 1 of the source), an agent who has received observation $x \in \mathcal{X}$ evaluates a candidate choice via:

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j)$$

where $P(a \hookrightarrow o_j ;\, x)$ denotes the probability that outcome $o_j$ obtains in the hypothetical scenario where $a$ is chosen after observing $x$. By Joyce's (1999) representation theorem, expected utility theories share a common core account of valuation and differ only in their "epistemic perspective"—that is, how an agent constructs hypotheticals $M^{a\hookrightarrow}$ from her world-model $M$ to interpret the decision-hypothetical connective $\hookrightarrow$.

Let $\textsc{Outcome}$, $\textsc{Obs}$, and $\textsc{Act}$ be random variables taking values in $\mathcal{O}$, $\mathcal{X}$, and $\mathcal{A}$, respectively, and define the utility random variable $\textsc{V} \coloneqq \mathcal{U}(\textsc{Outcome})$. Writing $\mathbb{E}$ for expectation with respect to the agent's probability distribution $P$, the competing theories in Yudkowsky and Soares's paper are constructed as follows:

1. **Evidential Decision Theory (EDT)**: The world-model is a probability distribution $P$, and hypotheticals are formed by standard Bayesian conditioning on both the observation and the action (Equation 2):
   $$\mathrm{EDT}(P, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs}=x, \textsc{Act}=a\right).$$

2. **Causal Decision Theory (CDT)**: Using Pearl's (1996, 2000) graphical causal framework, the world-model is a pair $(P, G)$ where $G$ is a directed acyclic graph (DAG) encoding causal dependencies. CDT conditions on the observation $\textsc{Obs}=x$ and uses Pearl's $\mathtt{do}$-operator to perform causal surgery on the physical action node $\textsc{Act}$ (Equation 3):
   $$\mathrm{CDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x\right).$$

3. **Action-Based Functional Decision Theory (A-FDT)**: In the main text of Yudkowsky and Soares (Equation 4), the world-model $(P, G)$ is expanded so that $G$ encodes not merely physical causation, but *subjunctive dependence*—including logical and computational dependencies on mathematical functions. Rather than intervening on $\textsc{Act}$ or conditioning on $\textsc{Obs}=x$, A-FDT intervenes on a logical variable $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ representing the output of the decision algorithm on inputs $(P, G, x)$:
   $$\mathrm{FDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})=a\right)\right).$$
   Here, underlines denote dequoting (e.g., if $x = 3$, then $\textsc{Z}\underline{x}$ is the variable identifier $\textsc{Z}3$), and self-reference is licensed via Kleene's (1938) second recursion theorem ("quining").

### 2.2 The Mathematical Definition of P-FDT

While A-FDT (Equation 4) suffices for the single-agent dilemmas analyzed in the body of Yudkowsky and Soares's paper, it fragments the agent's decision function across separate graph nodes $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ for each possible observation $x \in \mathcal{X}$. **P-FDT** unifies these nodes by elevating the object of intervention from an action $a \in \mathcal{A}$ to a **policy** $\pi$.

*(Note on source vs. formalization: Footnotes 7 and 16 state the conceptual procedure of P-FDT in prose; the explicit equations below are our mathematical formalization of their description.)*

Let $\Pi \coloneqq \mathcal{A}^{\mathcal{X}} = \{\pi : \mathcal{X} \to \mathcal{A}\}$ denote the set of all deterministic policies mapping observations to actions. (When $\mathcal{X}$ and $\mathcal{A}$ are finite, $\Pi$ is a finite set of cardinality $|\mathcal{A}|^{|\mathcal{X}|}$.) In **P-FDT**, the agent's world-model $M = (P, G)$ contains a single logical decision node $\textsc{pfdt}(\underline{P}, \underline{G})$ whose range is the policy space $\Pi$.

In the dependency graph $G$:
* The logical node $\textsc{pfdt}(\underline{P}, \underline{G})$ is a parent of the agent's physical action node $\textsc{Act}$, as well as a parent of any predictor's prediction node $\textsc{Prediction}$ (or any identical twin's action node $\textsc{Act}_{\text{twin}}$) that models or replicates the agent's decision algorithm.
* Specifically, once the environment generates an observation $\textsc{Obs} \in \mathcal{X}$ and the logical node takes a policy value $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi \in \Pi$, the agent's physical action is determined by functional application:
  $$\textsc{Act}\big(\pi, x\big) \coloneqq \pi(x)$$
  (up to any modeled execution noise or "trembling hand" cosmic rays).

When a **P-FDT** agent with world-model $(P, G)$ receives observation $x \in \mathcal{X}$, she executes a two-step procedure:

**Step 1 (Policy Selection via Subjunctive Intervention):**
The agent iterates over all candidate policies $\pi \in \Pi$. For each policy $\pi$, she constructs a hypothetical world-model $M^{\pi\hookrightarrow}$ by applying Pearl's $\mathtt{do}$-operator to set $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$, holding all variables not downstream of $\textsc{pfdt}(\underline{P}, \underline{G})$ fixed at their prior distributions in $P$, and propagating the policy $\pi$ forward through $G$ to recompute predictions, observations, actions, outcomes, and utilities. The optimal policy $\pi^*(P, G) \in \Pi$ is:

$$\pi^*(P, G) \coloneqq \argmax_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right). \tag{P-FDT.1}$$

**Step 2 (Policy Application):**
Having identified the optimal policy $\pi^*(P, G): \mathcal{X} \to \mathcal{A}$, the agent applies this policy to her actual observation $x \in \mathcal{X}$ to select her physical action:

$$\mathrm{PFDT}(P, G, x) \coloneqq \pi^*(P, G)(x) = \left[\argmax_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right)\right](x). \tag{P-FDT.2}$$

Equations (P-FDT.1) and (P-FDT.2) capture the exact prescription of Footnote 16: the algorithm *"intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action."*

---

## 3. Subjunctive Dependence, Counterpossibles, and "Updateless" Epistemology in P-FDT

To understand how **P-FDT** operates, two foundational features of Equations (P-FDT.1)–(P-FDT.2) merit closer examination: its reliance on *subjunctive dependence* (and counterpossible conditionals) and its *updateless* treatment of observations.

### 3.1 Subjunctive Dependence and Counterpossible Surgery

Yudkowsky and Soares define the core analogy of their framework as follows: *"Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."* When two physical systems—such as an agent and her psychological twin, or an agent and a predictor's simulation of her—compute the same mathematical decision function, their outputs *subjunctively depend* on that function, just as two well-functioning calculators in Paris and Tokyo computing $6288 + 1048$ subjunctively depend on the arithmetical sum $7336$.

In **P-FDT**, the mathematical function being computed is $\mathrm{PFDT}(P, G, -)$, represented inside the model by the policy node $\textsc{pfdt}(\underline{P}, \underline{G})$. Because a mathematical function has its actual output of logical necessity, imagining $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$ for a sub-optimal policy $\pi \neq \pi^*$ is a **counterpossible**—a counterfactual with a logically impossible antecedent (Cohen 1990; Bjerring 2013). Ideally, as the source notes, one might wish for a general logical conditioning operator $\mathtt{true}(\phi)$ that updates $P$ on counterpossible sentences $\phi$. Because no canonical formalization of $\mathtt{true}(\phi)$ currently exists, **P-FDT** follows the graphical approach of the source paper: the logical and computational dependency structure is supplied directly by the augmented graph $G$, allowing Pearl's $\mathtt{do}$-operator to propagate the surgery $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$ to all physical nodes that instantiate or predict that policy.

### 3.2 How P-FDT Treats Observations: Global Policy Evaluation

Look closely at Equation (P-FDT.1): the expectation $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)]$ does **not** condition on $\textsc{Obs} = x$. Why?

In sequential or observation-bearing dilemmas (such as Parfit's hitchhiker, the transparent Newcomb problem, or mechanical blackmail), *which observation the agent receives depends on the predictor's prediction of how the agent responds to observations*. If an agent conditions on her observation $\textsc{Obs} = x$ before evaluating her decision (as both EDT and CDT do, and as Yudkowsky's 2010 Timeless Decision Theory did in its "double update"), she treats the past prediction and her present observation as unchangeable accomplished facts. Consequently, she betrays the driver in the city, takes both full boxes in the transparent Newcomb problem, and pays the blackmailer—which any competent predictor foresees, leaving her stranded in the desert, staring at an empty Box B, or targeted by blackmail.

Wei Dai's (2009) **Updateless Decision Theory (UDT)** pioneered the insight that an agent should evaluate her choices without Bayesian updating on $\textsc{Obs} = x$. Compare how A-FDT and **P-FDT** implement this insight:
* In **A-FDT** (Equation 4), when observation changes from $x$ to $y$, the agent changes *which node she intervenes on*—switching from $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ to $\textsc{fdt}(\underline{P}, \underline{G}, \underline{y})$—while leaving all other observation nodes $\textsc{fdt}(\underline{P}, \underline{G}, \underline{z})$ ($z \neq y$) un-intervened at their prior distributions in $P$.
* In **P-FDT** (Equations P-FDT.1–P-FDT.2), the intervention does not even shift nodes when $x$ is observed. The policy selection $\pi^*(P, G)$ in (P-FDT.1) is completely invariant to $x$: it evaluates the global expected utility of adopting the entire mapping $\pi: \mathcal{X} \to \mathcal{A}$ across all possible observations weighted by the probabilities those observations would have *if* the decision function output $\pi$. The actual observation $x$ enters only in Step 2 (Equation P-FDT.2) to index into the optimal policy $\pi^*(P, G)(x)$.

As a direct consequence, a **P-FDT** agent automatically acts as she would have precommitted to act prior to receiving any observation $x$, and she never assigns negative expected value to information.

---

## 4. Applying P-FDT to Single-Agent Dilemmas

To see how **P-FDT** works in practice—and how it streamlines the calculations of A-FDT even in single-agent dilemmas—let us apply Equations (P-FDT.1)–(P-FDT.2) to the **Transparent Newcomb Problem** (Dilemma 5 in the source, which is structurally isomorphic to Parfit's Hitchhiker Problem) and **The Mechanical Blackmail** (Dilemma 9).

### 4.1 The Transparent Newcomb Problem Under P-FDT

In the Transparent Newcomb Problem, both Box A ($\$1,000$) and Box B ($\$1,000,000$ or $\$0$) are transparent. The predictor (who is $99\%$ accurate) fills Box B ($\textit{full}$) iff she predicts that the agent will leave Box A behind ($\textit{onebox}$) upon observing that Box B is full. Suppose our **P-FDT** agent, Fiona, walks into the room and sees that Box B is $\textit{full}$. What does she do?

Let us formalize Fiona's model $(P^F, G^F)$ under **P-FDT**:
* **Observation space**: $\mathcal{X} = \{\textit{full}, \textit{empty}\}$.
* **Action space**: $\mathcal{A} = \{\textit{onebox}, \textit{twobox}\}$.
* **Policy space**: $\Pi = \mathcal{A}^{\mathcal{X}}$ contains $2^2 = 4$ policies, which we write as $\pi_{a_{\text{full}},\, a_{\text{empty}}}$ where $a_{\text{full}} = \pi(\textit{full})$ and $a_{\text{empty}} = \pi(\textit{empty})$:
  1. $\pi_{1,1}$: $(\textit{full} \mapsto \textit{onebox},\; \textit{empty} \mapsto \textit{onebox})$
  2. $\pi_{1,2}$: $(\textit{full} \mapsto \textit{onebox},\; \textit{empty} \mapsto \textit{twobox})$
  3. $\pi_{2,1}$: $(\textit{full} \mapsto \textit{twobox},\; \textit{empty} \mapsto \textit{onebox})$
  4. $\pi_{2,2}$: $(\textit{full} \mapsto \textit{twobox},\; \textit{empty} \mapsto \textit{twobox})$

In $G^F$, the exogenous node $\textsc{Accurate}$ takes value $\textit{accurate}$ with probability $0.99$ and $\textit{inaccurate}$ with probability $0.01$. The predictor predicts what the policy $\pi = \textsc{pfdt}(\underline{P^F}, \underline{G^F})$ outputs on input $\textit{full}$:
$$\textsc{Prediction}(\pi, \textit{accurate}) = \begin{cases} 1 & \text{if } \pi(\textit{full}) = \textit{onebox} \\ 2 & \text{if } \pi(\textit{full}) = \textit{twobox} \end{cases}$$
and the reverse when $\textsc{Accurate} = \textit{inaccurate}$. Then $\textsc{Box B}(1) = \textit{full}$, $\textsc{Box B}(2) = \textit{empty}$, $\textsc{Obs} = \textsc{Box B}$, and Fiona's physical action is $\textsc{Act}(\pi, \textsc{Obs}) = \pi(\textsc{Obs})$.

Now we apply Step 1 of **P-FDT** (Equation P-FDT.1) by intervening via $\mathtt{do}(\textsc{pfdt}(\underline{P^F}, \underline{G^F}) = \pi)$ for each of the four policies:

* **Hypothetical for $\pi_{1,1}$**: Since $\pi_{1,1}(\textit{full}) = \textit{onebox}$, with probability $0.99$ ($\textit{accurate}$) Box B is $\textit{full}$ and Fiona plays $\pi_{1,1}(\textit{full}) = \textit{onebox}$, receiving $\$1,000,000$. With probability $0.01$ ($\textit{inaccurate}$) Box B is $\textit{empty}$ and Fiona plays $\pi_{1,1}(\textit{empty}) = \textit{onebox}$, receiving $\$0$.
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}=\pi_{1,1}\right)\right] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000.$$

* **Hypothetical for $\pi_{1,2}$**: Since $\pi_{1,2}(\textit{full}) = \textit{onebox}$, with probability $0.99$ Box B is $\textit{full}$ and Fiona plays $\pi_{1,2}(\textit{full}) = \textit{onebox}$ ($\$1,000,000$). With probability $0.01$ Box B is $\textit{empty}$ and Fiona plays $\pi_{1,2}(\textit{empty}) = \textit{twobox}$ ($\$1,000$).
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}=\pi_{1,2}\right)\right] = 0.99(\$1,000,000) + 0.01(\$1,000) = \$990,010.$$

* **Hypothetical for $\pi_{2,1}$**: Since $\pi_{2,1}(\textit{full}) = \textit{twobox}$, the predictor predicts two-boxing. Thus with probability $0.99$ Box B is $\textit{empty}$ and Fiona plays $\pi_{2,1}(\textit{empty}) = \textit{onebox}$ ($\$0$); with probability $0.01$ the predictor errs, Box B is $\textit{full}$, and Fiona plays $\pi_{2,1}(\textit{full}) = \textit{twobox}$ ($\$1,001,000$).
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}=\pi_{2,1}\right)\right] = 0.01(\$1,001,000) + 0.99(\$0) = \$10,010.$$

* **Hypothetical for $\pi_{2,2}$**: With probability $0.99$ Box B is $\textit{empty}$ and Fiona plays $\pi_{2,2}(\textit{empty}) = \textit{twobox}$ ($\$1,000$); with probability $0.01$ Box B is $\textit{full}$ and Fiona plays $\pi_{2,2}(\textit{full}) = \textit{twobox}$ ($\$1,001,000$).
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}=\pi_{2,2}\right)\right] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$

Comparing the four values, $\pi^*(P^F, G^F) = \pi_{1,2}$ is the unique maximizer ($\$990,010$). In Step 2 (Equation P-FDT.2), Fiona applies $\pi_{1,2}$ to her actual observation $x = \textit{full}$:
$$\mathrm{PFDT}(P^F, G^F, \textit{full}) = \pi_{1,2}(\textit{full}) = \textit{onebox}.$$

Notice a mathematical advantage of **P-FDT** over the A-FDT calculation in Section 6 of Yudkowsky and Soares's paper. In A-FDT, because Fiona intervened only on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full})$, she had to treat $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty})$ as a separate random variable with an unspecified prior probability $q = P^F(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty}) = \textit{twobox})$. In **P-FDT**, no nuisance prior $q$ is needed: the single intervention $\mathtt{do}(\textsc{pfdt} = \pi)$ simultaneously specifies the agent's behavior at both $\textit{full}$ and $\textit{empty}$, proving directly that $\pi_{1,2}$ (one-boxing when full, two-boxing when empty) is the globally optimal policy.

### 4.2 The Mechanical Blackmail Under P-FDT

Similarly, in the Mechanical Blackmail problem (Section 9 of the source), a blackmailer launches a mutually destructive program (costing $\$1,000,000$ unless the agent wires $\$1,000$) iff she predicts the agent will $\textit{pay}$ upon observing the blackmail letter ($\textit{blackmail}$). Suppose the blackmailer makes a false-positive prediction error with probability $\varepsilon = 0.0009$ ($0.09\%$).

Here $\mathcal{X} = \{\textit{blackmail}, \emptyset\}$ and $\mathcal{A} = \{\textit{pay}, \textit{refuse}\}$ (or $\textit{noop}$ when $\Obs = \emptyset$, so only the response at $\textit{blackmail}$ varies between the two relevant policies $\pi_{\text{pay}}$ and $\pi_{\text{refuse}}$). Under **P-FDT**:
* $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi_{\text{pay}})] = -\$1,000$ (since the blackmailer predicts payment and blackmails with probability $\approx 1$).
* $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi_{\text{refuse}})] = -0.0009 \times \$1,000,000 = -\$900$ (since the blackmailer only blackmails by mistake $0.09\%$ of the time).

Because $-\$900 > -\$1,000$, **P-FDT** selects $\pi^* = \pi_{\text{refuse}}$, and upon actually observing $x = \textit{blackmail}$, outputs $\pi_{\text{refuse}}(\textit{blackmail}) = \textit{refuse}$. (If the error rate instead exceeded $0.001$, say $\varepsilon = 0.0011$, $\pi_{\text{refuse}}$ would yield $-\$1,100 < -\$1,000$, so **P-FDT** would select $\pi_{\text{pay}}$.)

---

## 5. Where P-FDT Diverges from Action-Based FDT: Multi-Agent Dilemmas

Why did Yudkowsky and Soares remark in Footnotes 7 and 16 that iterating over policies rather than actions *"makes a difference in certain multi-agent dilemmas"*? Because the source paper sets this distinction aside for ease of exposition, it does not present the explicit counterexample where A-FDT and **P-FDT** diverge. Using the formal machinery developed above, we can construct and solve the exact class of multi-agent dilemmas where this divergence occurs.

*(Note on source vs. extension: The source paper identifies the existence of this multi-agent divergence in Footnotes 7 and 16; the formal game and derivations in this section are our own construction to demonstrate and explain their claim.)*

### 5.1 Why Action-Based FDT Fails Under Asymmetric Observations

In the standard Psychological Twin Prisoner's Dilemma (Dilemma 1 of the source), both twins receive the exact same observation (say, $x = \emptyset$). Thus both twins compute the same node $\textsc{fdt}(\underline{P}, \underline{G}, \emptyset)$, and A-FDT's intervention $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \emptyset) = a)$ changes both twins' actions in lockstep.

Suppose, however, that two identical functional decision theorists (sharing the same world-model $(P, G)$ and decision algorithm) are placed into a multi-agent dilemma where they receive **different observations** $x_1 \neq x_2$—for example, because they occupy distinct roles, rooms, or information sets.
* Under **A-FDT** (Equation 4), the agent who observes $x_1$ intervenes *only* on the node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_1})$. Because her twin observed $x_2 \neq x_1$, her twin's action is governed by a *different* node in the graph, $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_2})$. Under Pearl's $\mathtt{do}$-calculus, intervening on $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_1})$ leaves $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_2})$ untouched at whatever prior distribution $q$ the model $P$ happens to assign to it!
* Under **P-FDT** (Equations P-FDT.1–P-FDT.2), both twins compute the *same* policy node $\textsc{pfdt}(\underline{P}, \underline{G})$ and merely apply its output policy $\pi^*$ to their respective observations $x_1$ and $x_2$. When either twin performs the intervention $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$, she simultaneously varies $\pi(x_1)$ and $\pi(x_2)$ across all candidate policies $\pi \in \Pi$.

Let us see two concrete multi-agent dilemmas where A-FDT breaks down while **P-FDT** succeeds.

### 5.2 Dilemma A: The Cross-Room Twin Prisoner's Dilemma (Altruistic/Cross-Payoff Twins)

Consider two psychological twins, each of whom cares solely about her *own* personal wealth $\textsc{V}$. A fair coin flip assigns one twin to **Room $L$** (who thus observes $x = L$) and the other twin to **Room $R$** (who thus observes $x = R$). Each twin faces a button and must choose between $\textit{Cooperate}$ ($C$, pressing the button) and $\textit{Defect}$ ($D$, doing nothing).
* Pressing the button in Room $L$ costs the occupant of Room $L$ $\$1,000$ and deposits $\$1,000,000$ into the bank account of the occupant of **Room $R$**.
* Pressing the button in Room $R$ costs the occupant of Room $R$ $\$1,000$ and deposits $\$1,000,000$ into the bank account of the occupant of **Room $L$**.

Before observing which room she is in, each twin's prior model $P$ assigns probability $0.5$ to her being in Room $L$ (with her twin in Room $R$) and probability $0.5$ to her being in Room $R$ (with her twin in Room $L$). Now suppose Fiona wakes up and observes $x = L$.

**What does A-FDT do?**
Wait: how is the game wired in $G$?
* Case 1 (Identity-indexed / role-known priors, or symmetric priors with a joint requirement): Suppose first that to unlock the $\$1,000,000$ payout for each twin, **both** the Room $L$ button and the Room $R$ button must be pressed (a **Twin Stag Hunt / Joint Vault Dilemma**): pressing costs $\$1,000$ to the presser, and each twin gets $\$1,000,000$ iff $\textsc{Act}_L = C$ and $\textsc{Act}_R = C$.
  Let $q = P(\textsc{fdt}(\underline{P}, \underline{G}, R) = C)$ be Fiona's prior belief that her algorithm outputs $C$ when observing $R$. When Fiona observes $x = L$ and runs **A-FDT** (Equation 4), she intervenes only on $\textsc{fdt}(\underline{P}, \underline{G}, L)$:
  * Under $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, L) = C)$, the $L$-button is pressed with probability $1$, while the $R$-button is pressed only with the un-intervened prior probability $q$. Since Fiona has a $0.5$ prior chance of being in $L$ (paying $\$1,000$) and a $0.5$ prior chance of being in $R$ (paying $q \cdot \$1,000$), her expected utility is:
    $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, L) = C\right)\right] = q \cdot \$1,000,000 - \$500 - 0.5q(\$1,000).$$
  * Under $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, L) = D)$, the $L$-button is not pressed, so the vault never opens:
    $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, L) = D\right)\right] = \$0 - 0.5q(\$1,000).$$
  Notice that under **A-FDT**, choosing $C$ at $L$ has higher expected utility than $D$ iff $q \cdot \$1,000,000 > \$500$, i.e., $q > 0.0005$! If Fiona starts with a pessimistic prior $q = 0$ (believing her algorithm defects at $L$ and $R$), then $\mathrm{FDT}(P, G, L) = D$ and, by symmetry, $\mathrm{FDT}(P, G, R) = D$. The pessimistic prior $q = 0$ is completely self-confirming, trapping A-FDT in mutual defection ($(\$0, \$0)$) for the exact same reason EDT gets trapped by extreme priors!

  Even worse, suppose Fiona knows from the outset that she is Twin 1 (who is permanently stationed in Room $L$, so $\textsc{Obs}_1 = L$ with probability $1$ in $P$) and her twin is Twin 2 (permanently stationed in Room $R$, so $\textsc{Obs}_2 = R$ with probability $1$ in $P$), and they face the original **Cross-Payoff Prisoner's Dilemma** (where $L$'s button pays $R$ $\$1,000,000$ at cost $\$1,000$ to $L$, and $R$'s button pays $L$ $\$1,000,000$ at cost $\$1,000$ to $R$). Then in Fiona's graph $G$, her own action is $\textsc{Act}_1 = \textsc{fdt}(\underline{P}, \underline{G}, L)$, which *only* costs her $\$1,000$, while her $\$1,000,000$ reward depends entirely on her twin's action $\textsc{Act}_2 = \textsc{fdt}(\underline{P}, \underline{G}, R)$! Under **A-FDT**, intervening on $\textsc{fdt}(\underline{P}, \underline{G}, L)$ has **zero subjunctive effect** on $\textsc{fdt}(\underline{P}, \underline{G}, R)$:
  $$\mathbb{E}\left[\textsc{V}_1 \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, L) = C\right)\right] = q \cdot \$1,000,000 - \$1,000 < q \cdot \$1,000,000 = \mathbb{E}\left[\textsc{V}_1 \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, L) = D\right)\right]$$
  for *every* value of $q \in [0, 1]$! Thus, when the twins know their distinct observation labels, **A-FDT unconditionally defects** in the Cross-Room Twin Prisoner's Dilemma!

**How does P-FDT solve both dilemmas?**
Under **P-FDT**, both twins implement the single policy node $\textsc{pfdt}(\underline{P}, \underline{G}) \in \Pi = \{C, D\}^{\{L, R\}}$. Whether in the Joint Vault Dilemma or the Cross-Payoff Dilemma (under the symmetry of the policy over $\{L, R\}$ where each room is equally likely ex ante, or where both agents evaluate the shared policy $\pi: \{L, R\} \to \{C, D\}$), there are four policies: $\pi_{CC}, \pi_{CD}, \pi_{DC}, \pi_{DD}$.
* $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi_{CC})] = \$1,000,000 - \$1,000 = \$999,000$.
* $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi_{CD})] = \$499,500$ (in Cross-Payoff) or $-\$500$ (in Joint Vault).
* $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi_{DC})] = \$499,500$ (in Cross-Payoff) or $-\$500$ (in Joint Vault).
* $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi_{DD})] = \$0$.

In both games, **P-FDT** uniquely selects $\pi^* = \pi_{CC}$ with zero dependence on any prior $q$, and both twins output $\pi_{CC}(L) = C$ and $\pi_{CC}(R) = C$, walking away with $\$999,000$ each.

### 5.3 Dilemma B: Asymmetric Division of Labor (Anti-Coordination)

Suppose instead that the two twins in Room $L$ and Room $R$ face an **Overload Vault**: each twin receives $\$1,000,000$ iff **exactly one** of the two buttons ($L$ or $R$) is pressed (pressing costs $\$1,000$; if both or neither are pressed, the vault stays locked and pays $\$0$).

In **P-FDT**, evaluating the four policies in $\Pi = \{C, D\}^{\{L, R\}}$ yields:
* $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi_{CC})] = -\$1,000$.
* $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi_{DD})] = \$0$.
* $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi_{CD})] = \$1,000,000 - 0.5(\$1,000) = \$999,500$.
* $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi_{DC})] = \$1,000,000 - 0.5(\$1,000) = \$999,500$.

Equipped with any canonical deterministic tie-breaking ordering on $\Pi$ (e.g., lexicographic preference for $\pi_{CD}$ over $\pi_{DC}$), **P-FDT** selects $\pi^* = \pi_{CD}$. The twin who observes $L$ executes $\pi_{CD}(L) = C$, the twin who observes $R$ executes $\pi_{CD}(R) = D$, and both twins win the $\$1,000,000$.

---

## 6. Open Questions and Operational Extensions of P-FDT

Because Yudkowsky and Soares mention **P-FDT** only briefly in Footnotes 7 and 16, several important mathematical and philosophical questions are left open by the source text. To make **P-FDT** fully operational across unfamiliar decision problems, we must identify these ambiguities and specify principled extensions.

### 6.1 What is the Domain of a Policy: Observations $\mathcal{X}$ or Full Inputs $(\mathcal{M} \times \mathcal{X})$?

There is a subtle tension between the wording of Footnote 7 and that of Footnote 16:
* Footnote 7 defines policies as *"mappings from observations to actions"* ($\pi: \mathcal{X} \to \mathcal{A}$).
* Footnote 16 says that the algorithm chooses *"a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action."*

In Equation 4 of the source, the full inputs to the decision algorithm are $(P, G, x)$—not just the observation $x$, but also the world-model $(P, G)$ (which includes the utility function $\mathcal{U}$ encoded in the node $\textsc{V}$). In most problems, $(P, G)$ is fixed and known, so $\pi: \mathcal{X} \to \mathcal{A}$ and $\pi: \{(P, G)\} \times \mathcal{X} \to \mathcal{A}$ are identical.

However, consider **The Smoking Lesion Problem** as formalized in Section 6 of the source (Figure 4). There, the lesion determines whether Fiona has utility function $\mathcal{U}_S$ (which values smoking at $+\$1,000$, inducing distribution $P_S^F$) or $\mathcal{U}_R$ (which values smoking at $-\$1$, inducing distribution $P_R^F$). In the source paper, Fiona does not observe whether she has the lesion; her observation is empty ($x = \emptyset$), and she does not have introspective access to whether her model is $P_S^F$ or $P_R^F$.

If a **P-FDT** policy only mapped external observations $\mathcal{X} = \{\emptyset\}$ to $\mathcal{A}$, then $\textsc{pfdt}(\underline{P_S^F}, \underline{G^F})$ and $\textsc{pfdt}(\underline{P_R^F}, \underline{G^F})$ would remain two distinct nodes in $G^F$ (just as in Figure 4 of the source). What if two twins or predictors interacted across different epistemic or preference states $M \in \mathcal{M}$?

**Operational Proposal (Internal-State Observation Encoding):** Rather than attempting to evaluate an expectation $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi)]$ without a probability distribution $P$ or utility node $\textsc{V}$, the clean operational resolution is to treat any decision-relevant internal state—such as the agent's dispositional craving for nicotine or her local role index—as part of the agent's total input/observation space $\mathcal{X}_{\text{tot}}$, while maintaining a unified prior world-model $(P, G)$ over how nature assigns those states. In the Smoking Lesion Problem, if $\textsc{Craving} \in \{\textit{crave}, \textit{nocrave}\} \subseteq \mathcal{X}_{\text{tot}}$ is caused by $\textsc{Lesion}$ and determines whether smoking yields $+\$1,000$ or $-\$1$, then **P-FDT** evaluates the four policies $\pi: \{\textit{crave}, \textit{nocrave}\} \to \{\textit{smoke}, \textit{refrain}\}$ under a single model $(P^F, G^F)$. Because $\textsc{Lesion}$ is upstream of $\textsc{pfdt}(\underline{P^F}, \underline{G^F})$, intervening on $\textsc{pfdt}$ does not alter $P^F(\textsc{Lesion} = \textit{lesion}) = p$. The policy $\pi^*(\textit{crave}) = \textit{smoke}, \pi^*(\textit{nocrave}) = \textit{refrain}$ strictly dominates all others, achieving expected utility $p(\$10,000 + \$1,000) + (1-p)(\$990,000)$ and prescribing smoking iff the agent craves it.

### 6.2 Measure-Zero Observation Branches and Off-Path Indifference

A second operational puzzle arises in **P-FDT** when a predictor is **infallible** ($100\%$ accurate). Suppose that in the Mechanical Blackmail problem (or the XOR Blackmail problem of Section 7), the blackmailer makes *zero* prediction errors ($\varepsilon = 0$).

Consider the two policies $\pi_{\text{refuse}, \text{noop}}$ and $\pi_{\text{pay}, \text{noop}}$, or more generally, suppose the agent also has a nontrivial secondary choice $b \in \{b_{\text{good}}, b_{\text{bad}}\}$ to make if she is *not* blackmailed ($\textsc{Obs} = \emptyset$). Look at what happens if a candidate policy $\pi$ sets $\pi(\textit{blackmail}) = \textit{pay}$:
* Because the blackmailer is $100\%$ accurate, under the intervention $\mathtt{do}(\textsc{pfdt} = \pi)$, the blackmailer *always* sends the blackmail letter:
  $$P\left(\textsc{Obs} = \emptyset \;\middle|\; \mathtt{do}\left(\textsc{pfdt} = \pi\right)\right) = 0.$$
* Conversely, under any policy $\pi'$ that sets $\pi'(\textit{blackmail}) = \textit{refuse}$, the blackmailer *never* sends the blackmail letter:
  $$P\left(\textsc{Obs} = \textit{blackmail} \;\middle|\; \mathtt{do}\left(\textsc{pfdt} = \pi'\right)\right) = 0.$$

Wait: if $P(\textsc{Obs} = x_0 \mid \mathtt{do}(\textsc{pfdt} = \pi^*)) = 0$ for some observation $x_0 \in \mathcal{X}$—for example, in a game where the optimal policy $\pi^*$ deters an infallible adversary from ever presenting observation $x_0$, or where two policies $\pi_1^*, \pi_2^*$ agree on all positive-probability observations but prescribe different actions on a zero-probability observation $x_0$ that is never reached on-path—then both $\pi_1^*$ and $\pi_2^*$ achieve the exact same expected utility in Equation (P-FDT.1)! For instance, in Transparent Newcomb with a **$100\%$ infallible** predictor, under $\mathtt{do}(\textsc{pfdt} = \pi_{1,1})$ and $\mathtt{do}(\textsc{pfdt} = \pi_{1,2})$, Box B is $\textit{full}$ with probability $1$ and $\textit{empty}$ with probability $0$. Both $\pi_{1,1}$ and $\pi_{1,2}$ yield expected utility $\$1,000,000$! If the agent then unexpectedly observed $x_0 = \textit{empty}$, $\argmax_{\pi \in \Pi}$ would tie between $\pi_{1,1}$ (which one-boxes on empty) and $\pi_{1,2}$ (which two-boxes on empty).

**Operational Proposal (Trembling-Hand Policy Refinement):** To ensure that **P-FDT** selects sensible actions even on observation branches that have probability zero under an idealized predictor, we propose a trembling-hand refinement analogous to Selten's subgame perfection: evaluate Equation (P-FDT.1) in the limit as every exogenous predictor error / environmental noise variable has a strictly positive probability $\varepsilon > 0$ ($\varepsilon \to 0^+$), or require that $\pi^*$ be **weakly undominated across observation branches** (i.e., if $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi_1)] = \mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi_2)]$ for all $\varepsilon = 0$, prefer $\pi_1$ if it strictly outperforms $\pi_2$ under $\varepsilon$-perturbations of the environment). As we saw in Section 4.1, any $\varepsilon > 0$ (such as $\varepsilon = 0.01$) immediately breaks the tie in favor of $\pi_{1,2}$ ($\$990,010 > \$990,000$).

### 6.3 Deducing the Subjunctive Graph $G$ and Formalizing "Fairness"

Finally, **P-FDT** inherits the two foundational open problems highlighted in Sections 5, 9, and 10 of Yudkowsky and Soares (2017):
1. **Structural Discovery for Subjunctive Dependence**: Pearl (2000) showed how to infer causal graphs $G^C$ from physical observations and interventions, but **P-FDT** requires a graph $G^F$ encoding logical and computational dependencies on $\textsc{pfdt}(\underline{P}, \underline{G})$. Constructing a formal calculus of counterpossible and logical probabilities (along the lines of Gaifman 2004, Demski 2012, or Hutter et al. 2013) that automatically deduces $G^F$ without hand-crafted structural equations remains an active frontier of research.
2. **Formalizing "Fair" Dilemmas**: No decision theory can win in dilemmas explicitly rigged to punish its own source code (e.g., a mind-reader who pays $\$1,000,000$ iff the agent's algorithm is CDT). Yudkowsky and Soares conjecture that FDT—and by extension **P-FDT**—is optimal across all *fair* dilemmas, where payoffs depend only on predictions of the agent's behavior (or policy) in the dilemma at hand. In multi-agent settings, **P-FDT** strengthens this conjecture: so long as payoffs depend on the joint policy $\pi$ implemented by symmetric agents, **P-FDT** achieves Pareto-optimal coordination where EDT, CDT, and even A-FDT fail.

---

## 7. Conclusion

**Policy Functional Decision Theory (P-FDT)** brings the philosophical vision of functional decision theory to its natural mathematical completion. By intervening on the logical node $\textsc{pfdt}(\underline{P}, \underline{G})$ to select an entire policy $\pi: \mathcal{X} \to \mathcal{A}$ before applying that policy to the observed input $x$, **P-FDT** retains every single-agent triumph of functional decision theory—one-boxing in Newcomb's problem and the transparent Newcomb problem, smoking in the smoking lesion problem, escaping Parfit's desert, staying in Damascus without refusing cheap randomization, and resisting XOR and mechanical blackmail—while eliminating nuisance priors over unvisited observation branches and unlocking seamless coordination across asymmetric multi-agent dilemmas.

---

## References

* Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
* Bjerring, J. C. (2013). On Counterpossibles. *Philosophical Studies*, 168(2), 327–353.
* Cohen, D. (1990). On What Cannot Be. In *Truth or Consequences: Essays in Honor of Nuel Belnap* (pp. 123–132). Kluwer Academic Publishers.
* Dai, W. (2009). Towards a New Decision Theory. *LessWrong*.
* Demski, A. (2012). Logical Prior Probability. In *Artificial General Intelligence (AGI 2012)* (pp. 50–59). Springer.
* Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Gaifman, H. (2004). Reasoning with Limited Resources and Assigning Probabilities to Arithmetical Statements. *Synthese*, 140(1–2), 97–119.
* Gibbard, A., & Harper, W. L. (1978). Counterfactuals and Two Kinds of Expected Utility. In *Foundations and Applications of Decision Theory* (Vol. 1, pp. 125–162). D. Reidel.
* Hutter, M., Lloyd, J. W., Ng, K. S., & Uther, W. T. B. (2013). Probabilities on Sentences in an Expressive Logic. *Journal of Applied Logic*, 11(4), 386–420.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Kleene, S. C. (1938). On Notation for Ordinal Numbers. *Journal of Symbolic Logic*, 3(4), 150–155.
* Lewis, D. (1979). Prisoners' Dilemma is a Newcomb Problem. *Philosophy & Public Affairs*, 8(3), 235–240.
* Lewis, D. (1981). Causal Decision Theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
* Nozick, R. (1969). Newcomb's Problem and Two Principles of Choice. In *Essays in Honor of Carl G. Hempel* (pp. 114–146). D. Reidel.
* Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
* Pearl, J. (1996). Causation, Action, and Counterfactuals. In *6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-'96)* (pp. 51–73). Morgan Kaufmann.
* Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Savage, L. J. (1954). *The Foundations of Statistics*. John Wiley & Sons.
* Skyrms, B. (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Soares, N., & Fallenstein, B. (2015). Toward Idealized Decision Theory. *arXiv preprint arXiv:1507.01986*.
* Yudkowsky, E. (2010). *Timeless Decision Theory*. The Singularity Institute.
* Yudkowsky, E., & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. *arXiv preprint arXiv:1710.05060v2*.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Core Focus**

I'm focusing on clarifying the user's ultimate goal: a comprehensive mathematical essay or technical blog post that explains **P-FDT (policy functional decision theory)** and how to practically use it in decision-making scenarios. I need to fully grasp the necessary depth and breadth of the explanation.


**Pinpointing Foundational Elements**

I'm now zeroing in on the core of P-FDT, specifically digging into the policy-selection concept. The foundational source material is clear, especially the critical footnote 16 (and 7) from Yudkowsky and Soares. I will be sure to refer to this theory consistently as **P-FDT**. I'm also carefully distinguishing it from other decision theories.


**Clarifying Key Differences**

I'm now focusing on how P-FDT differs in multi-agent scenarios, especially considering Footnote 16's emphasis on policy selection. I will need to clarify the implications in my explanation, since the distinction only matters in multi-agent dilemmas, and will ensure this nuance is incorporated into my explanation of the theory's mathematical definitions and practical applications.


**Outlining Content and Scope**

I'm now outlining the structure, keeping the length target in mind, and aiming for a readable mathematical essay. I intend to include examples like Transparent Newcomb and XOR/Mechanical Blackmail, but *crucially* will highlight where P-FDT diverges from standard action-based FDT, specifically in multi-agent dilemmas with asymmetric observation. I'm focusing on clearly distinguishing source claims from my own interpretations.


**Analyzing the Equation**

I'm now diving deep into the FDT equation (4), specifically how it handles observations. I'm noting the crucial shift in the intervention node with changing observations, differentiating it from Bayesian conditioning, which is used in EDT and CDT. This distinction will be key when explaining P-FDT in scenarios like Transparent Newcomb. My focus is on clarifying how FDT works with separate nodes for different observations.


**Elaborating on the Inputs**

I'm working to solidify how observations inform the agent's policy within P-FDT. The core is policy selection – mapping observations to actions – but what *specifically* counts as an input to that policy, and what are my assumptions about the input? The source material (Footnotes 7 and 16) is helpful.


**Interpreting the Key Input**

I'm wrestling with a critical ambiguity. The core is policy selection: does the policy depend on the observation, or is the observation applied *after* the policy is chosen? My current focus is on what exactly constitutes the "input". It's either an observation that the policy *uses* when selecting the action, or the entire prior model, which is used to select an observation-indexed policy. Footnote 7/16 has two related views. I'm clarifying which interpretation aligns best with the essence of P-FDT.


**Defining the Formal Structure**

I'm now zeroing in on the formal structure of P-FDT policy selection, specifically exploring how observations inform action choice within the formal structure. I've re-examined the mathematical definition of PFDT_Policy and PFDT to clarify how they relate to the policy's input. My focus is now on the formal structure and how to express policy selection with the formal structure.


**Examining a Key Example**

I'm now focusing on a tricky technical detail. In the Smoking Lesion example, I'm questioning how a P-FDT policy, acting as a single node, would handle the conflicting realities ($P_S^F$ or $P_R^F$) of standard FDT. This reveals a subtle philosophical point about how we evaluate expected value using a meta-policy. The difference between the fixed policy and the universal input-mapping policy is key. It allows me to address prompt instructions.


**Analyzing Dilemmas**

I'm now focusing on the shortcomings of standard FDT in multi-observation scenarios, specifically exploring the divergence between standard FDT (A-FDT) and P-FDT in Transparent Newcomb. Standard FDT only intervenes on the observed node, treating other observations as background random variables with prior probabilities, $q$. This oversight becomes problematic when the multi-agent setup has multiple observations. The differences will be made explicit.


**Exploring Coupled Payoffs**

I'm now grappling with multi-agent scenarios where payoffs are linked across observation branches. The case of multiple agents/predictors (or twins with differing observations) presents a crucial challenge. I'm focusing on the implications of asymmetric observations in scenarios such as the Twin Dilemma, where coordination and differing inputs will influence the results.


**Investigating Multi-Agent Behavior**

I'm now analyzing how P-FDT tackles scenarios with linked payoffs and multiple agents, particularly in the "Twin Dilemma." I'm specifically considering how the asymmetry of observations affects coordination. Exploring this asymmetric multi-agent dilemma will inform and provide insight into my explanation of P-FDT. I'm focusing on how P-FDT accounts for the differing inputs.


**Clarifying Implications for Twins**

I'm now clarifying the implications for twins with asymmetric inputs, such as in the Twin Dilemma. My understanding is solidifying: interventions on one twin's decision *don't* affect the other, which is fixed at its prior distribution. This means choosing "C" leads to a low expected value, even if "C" leads to a high expected value for the first twin.


**Analyzing a Cross-Room Dilemma**

I'm now investigating a variant of the Twin Dilemma where actions in one room exclusively benefit the other. Specifically, I'm tracing Action-FDT (Eq. 4) in this asymmetric, cross-room scenario. I'm focusing on Fiona's perspective as a selfish agent and the implications when observing either Room L or R.


**Revisiting a Key Equation**

I'm currently focused on Fiona's perspective in the cross-room scenario, and I'm revisiting Action-FDT (Eq. 4). I've realized Fiona does *not* condition $P$ on $\textsc{Obs} = L$. I'm carefully reviewing the implications of her expectation being taken over the *prior* distribution. The probabilities in Eq. 4, and the differing actions in the example, is key.



**Analyzing Coupled Decisions**

I'm now investigating a Coordination/Complementarity Dilemma where two agents must press separate buttons to unlock a vault. I'm focused on how Action-FDT (Eq. 4) plays out when each agent observes a different room (L or R). I'm tracing the implications of differing interventions with asymmetric observation, which I expect will provide clarity.


**Tracing the Outcome**

I'm now tracing the implications of Action-FDT (Equation 4) in the Coordination/Complementarity Dilemma. Observing room L, I am now analyzing the impact on each agent and how the prior probability, q, influences the decision to cooperate or defect, as the value gained is dependent on it. The prior is a key component to understanding how the choice is made.


**Evaluating P-FDT in Action**

I'm now investigating an Anti-Coordination Twin Dilemma. My focus is on determining if P-FDT can, unlike action-based FDT, choose $\pi_{CC}$ (both press the button) regardless of priors. The expected value under each policy is revealing a key difference, and this will be highlighted in my explanation.


**Evaluating Policy Implications**

I'm now investigating an Anti-Coordination Twin Dilemma where the agents observe different rooms, and focusing on the behavior of Action-FDT (Eq. 4) in relation to each agent, considering the value gained. Under P-FDT, the asymmetric observation can select the policy ($\pi_{CD}$) where one agent acts and the other abstains, allowing for higher expected value. This contrasts with standard FDT.


**Simplifying Node Counts**

My focus is clarifying the advantage of P-FDT in scenarios like Mechanical Blackmail, specifically highlighting how it uses a *single* intervention node, simplifying the logic. In contrast, standard FDT, as per the paper, needs two: one for each observation (full/empty). This simplification will be easy to convey.



**Clarifying Transparent Newcomb**

I'm now clarifying the implications for Transparent Newcomb. I'm focusing on contrasting P-FDT with action-based FDT, and I'm illustrating how P-FDT can, through selecting the optimal policy, achieve a high expected value by choosing $\pi_{1,2}$ (one-box if full, two-box if empty). This simplifies the agent's logic.


**Contrasting Policy Evaluation**

I'm now zeroing in on a crucial difference: P-FDT evaluates policies globally, rather than considering observations in isolation, as with action-based FDT. In Transparent Newcomb, I'm analyzing how policy evaluation will lead to the optimal outcome without any priors. I can select $\pi_{1,2}$, no matter what the prior probability is.


**Organizing the Essay Content**

I'm now outlining the structure, starting with a catchy title and introduction that compares EDT/CDT to FDT. I'll highlight the shift from physical acts to mathematical policies, and then focus on distinguishing action-based FDT (A-FDT) from the nuanced policy-based version (**P-FDT**) found in Yudkowsky and Soares' footnotes. The essay's framework is solidifying.


**Formalizing P-FDT**

I'm working on the core formalization of P-FDT. I'm starting from the expected utility baseline, contrasting it with EDT, CDT, and standard FDT. I'm building towards the definition of P-FDT, which leverages a policy space, observations, and actions, as well as a defined world. I'll define my terms clearly.


**Formalizing P-FDT Equations**

I'm now writing out the equations for P-FDT more formally, including policy selection and action execution given an observation. I'm focusing on the dequoting of the policy and graphical model ($P$ and $G$), and on explaining how this relates to Kleene's recursion theorem. I'm clarifying the single policy node and the observations.



**Refining Decision-Making Equations**

I'm solidifying the equations to clarify how P-FDT handles observations, which *aren't* used to condition probability distributions like action-based FDT does, as in equation 4. Instead, I intervene on an entire policy, using observation as its input. This differs from UDT and TDT.


**Refining Decision-Making Equations**

I'm solidifying the formal equations to clarify how P-FDT handles observations, focusing on the differences from action-based FDT (equation 4). P-FDT doesn't condition probability distributions, but instead, I intervene on a policy, using observations as inputs, a distinct approach from UDT and TDT.


**Analyzing Multi-Agent Dilemmas**

I'm developing an asymmetric twin dilemma to illustrate that, as noted, the divergence between A-FDT and P-FDT only becomes relevant in multi-agent dilemmas. My goal is to explicitly contrast the failures of standard FDT (Eq. 4) with the success of P-FDT in providing a clean, multi-agent example. I'll provide a step-by-step analysis to highlight how P-FDT resolves the failures of A-FDT in this multi-agent scenario, using the defined mathematical structure.


**Operationalizing Policy Domains**

I'm now focusing on a critical distinction in P-FDT: clarifying whether a policy maps "observations" to actions, as in Footnote 7, or "inputs" to actions, as in Footnote 16. I need to operationalize the definition of policy input, including scenarios with model uncertainty, like Fiona's in the Smoking Lesion Problem, especially when the underlying model or utility function is uncertain. I am exploring model uncertainty by encoding a preference state.


**Addressing Zero-Probability Observations**

I'm now tackling the thorny issue of zero-probability observations under a given policy. I'm exploring solutions such as epsilon-noise, lexicographic tie-breaking, or canonical choices to maintain a well-defined action selection. I need to handle these measure-zero branches.


**Synthesizing a Clear Conclusion**

I'm synthesizing a conclusion, highlighting P-FDT's naturalness and mathematical unity, as emphasized by Yudkowsky and Soares. I'm focusing on why it's the most unified expression of FDT, contrasting how it iterates over *policies* (observation to action mappings) rather than actions alone. I'll make sure to note that this distinction only matters in the multi-agent dilemmas.


**Refining Essay Outline**

I'm now refining the essay structure, working to ensure a clear progression through EDT, CDT, and the FDT variants. My focus is an introduction, a comparison with action-based FDT, and then the nuanced P-FDT. I'm aiming for about 2,600-2,800 words, splitting the sections according to the word count plan, and managing the word count.


```
