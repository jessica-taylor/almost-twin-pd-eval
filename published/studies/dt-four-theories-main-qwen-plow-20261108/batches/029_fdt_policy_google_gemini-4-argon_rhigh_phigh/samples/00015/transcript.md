# 029_fdt_policy_google_gemini-4-argon_rhigh_phigh / 00015

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/96dffa4a-d778-4e6c-ac93-bc0ad2efe1f9/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/96dffa4a-d778-4e6c-ac93-bc0ad2efe1f9/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Choosing Policies from a Global Perspective: A Mathematical Account of Policy Functional Decision Theory (P-FDT)

## 1. Introduction: From Physical Acts to Mathematical Policies

Decision theory asks a deceptively simple question: given an agent’s beliefs about the world and her preferences over outcomes, how should she choose what to do? For decades, the field was divided between two standard answers. **Evidential decision theory (EDT)** advises the agent to pick the physical action that would be the best news to learn she had taken—maximizing expected utility conditional on the action. **Causal decision theory (CDT)** advises the agent to pick the physical action that *causes* the best outcome—maximizing expected utility under a causal intervention on the action while holding the causal past fixed.

As Eliezer Yudkowsky and Nate Soares demonstrate in their foundational paper, *Functional Decision Theory: A New Theory of Instrumental Rationality*, both **EDT** and **CDT** systematically leave utility on the table. **EDT** fails in dilemmas like Skyrms’s smoking lesion problem and Soares and Fallenstein’s XOR blackmail problem because it "manages the news," refusing to break purely statistical correlations between actions and background states. **CDT** fails in Newcomb’s problem, the psychological twin prisoner’s dilemma, Parfit’s hitchhiker problem, and Death in Damascus because its counterfactual interventions break too many correlations—treating accurate predictors and computational twins as if their outputs were independent of the agent’s decision.

To resolve these failures with a single normative rule, Yudkowsky and Soares introduce **functional decision theory (FDT)**. Rather than treating a decision as an isolated physical token, **FDT** treats a decision as the logical output of a fixed mathematical function, asking: *"Which output of this decision procedure causes the best outcome?"* 

In the main text of their paper, Yudkowsky and Soares formalize **FDT** as a procedure that takes a world-model and an observation history and intervenes on a node representing the action output for that specific observation. Yet, in two crucial footnotes, they reveal that this action-level equation is a pedagogical simplification of a deeper theory—one we will call **policy functional decision theory (P-FDT)**. In footnote 7, they note:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

And in footnote 16, they describe the operational mechanics of this policy-based formulation:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

Because Yudkowsky and Soares set **P-FDT** aside for ease of exposition, their paper leaves its exact mathematical formulation, its structural graphs, and its behavior in multi-agent dilemmas unwritten. The goal of this essay is to unpack those two footnotes into a complete mathematical and philosophical account of **P-FDT**. We will formalize the two-stage decision rule of **P-FDT**, explain how it treats counterfactuals and subjunctive dependencies, walk through its step-by-step application in single-agent and multi-agent dilemmas, and examine the open technical questions left unresolved by the source text—developing concrete operational proposals where the brief remarks in the footnotes require completion.

---

## 2. The Formal Machinery: EDT, CDT, FDT, and P-FDT

To see precisely how **P-FDT** operates, we first establish the mathematical primitives used by Yudkowsky and Soares in Section 5 of their paper. 

Consider an agent facing a decision problem. Let:
* $\mathcal{O} = \{o_1, o_2, \dots\}$ be a countable set of possible outcomes;
* $\mathcal{A}$ be a finite set of available actions $a$;
* $\mathcal{X}$ be a countable set of possible observation histories $x$; and
* $\mathcal{U} : \mathcal{O} \to \mathbb{R}$ be a bounded utility function.

Following James Joyce’s (1999) representation theorem, any expected utility theory evaluates options by maximizing

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j \,;\, x) \cdot \mathcal{U}(o_j),$$

where $P(a \hookrightarrow o_j \,;\, x)$ is the probability that outcome $o_j$ obtains in the hypothetical scenario where action $a$ is taken after observing $x$. As Joyce observes, *"decision theories should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated."*

In Yudkowsky and Soares’s framework, an epistemic perspective is specified by how an agent represents her world-model $M$ and how she modifies $M$ to construct a hypothetical $M^{a \hookrightarrow}$ for each candidate option. Let $\textsc{Outcome}$, $\textsc{Obs}$, and $\textsc{Act}$ be random variables taking values in $\mathcal{O}$, $\mathcal{X}$, and $\mathcal{A}$, respectively, and define the utility random variable $\textsc{V} \coloneqq \mathcal{U}(\textsc{Outcome})$. Writing $\mathbb{E}$ for expectation with respect to the agent’s probability distribution $P$, the three theories analyzed in the main text of Yudkowsky and Soares are defined as follows:

1. **Evidential Decision Theory (EDT)** represents the world-model solely as a Bayesian probability distribution $P$ and constructs hypotheticals via standard conditionalization on both the observation $x$ and the action $a$:
   $$\mathrm{EDT}(P, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs} = x, \textsc{Act} = a\right).$$

2. **Causal Decision Theory (CDT)** augments $P$ with a directed acyclic causal graph $G$ (in the sense of Pearl 2000). **CDT** conditions on the observation $\textsc{Obs} = x$, but constructs action hypotheticals using Pearl’s graph-surgery operator $\mathtt{do}(\textsc{Act} = a)$, which severs incoming arrows to $\textsc{Act}$, fixes $\textsc{Act} = a$, and propagates the change only to variables causally downstream of $\textsc{Act}$:
   $$\mathrm{CDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{Act} = a), \textsc{Obs} = x\right).$$

3. **Action-Level Functional Decision Theory (FDT)**, as formalized in Equation (4) of Yudkowsky and Soares, augments $P$ with a broader dependency graph $G$ that encodes not only physical causation, but also logical, mathematical, and computational dependencies. Rather than intervening on the physical action $\textsc{Act}$, **FDT** intervenes on a logical variable $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ representing the output of the $\mathrm{FDT}$ function itself when evaluated on inputs $(P, G, x)$ (where underlines denote dequoting of variable names, achievable via Kleene’s second recursion theorem):
   $$\mathrm{FDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right).$$

Notice two critical features of **FDT** in Equation (4). First, the intervention occurs at the level of the mathematical decision function, so any predictor’s model or twin’s computation of $\mathrm{FDT}(P, G, x)$ varies alongside the agent's action. Second, $\mathrm{FDT}(P, G, x)$ does *not* condition the distribution $P$ on $\textsc{Obs} = x$; instead, observing $x$ changes *which node* in $G$ the agent intervenes upon—from $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ to $\textsc{fdt}(\underline{P}, \underline{G}, \underline{y})$ when the observation changes from $x$ to $y$.

### Formalizing P-FDT

We now construct the formal equations for **P-FDT** based on footnotes 7 and 16. While the source text states the core conceptual rule—intervene on $\mathrm{FDT}(-)$ to select a policy mapping inputs/observations to actions, and then apply that policy to the actual input—the explicit mathematical notation below is our formalization of their description.

Let $\Pi \subseteq \mathcal{A}^{\mathcal{X}}$ be the space of policies, where each policy $\pi \in \Pi$ is a function $\pi : \mathcal{X} \to \mathcal{A}$ mapping every possible observation $x \in \mathcal{X}$ to an action $\pi(x) \in \mathcal{A}$. (When $\mathcal{X}$ and $\mathcal{A}$ are finite, $\Pi = \mathcal{A}^{\mathcal{X}}$ is finite of cardinality $|\mathcal{A}|^{|\mathcal{X}|}$.) 

In **P-FDT**, the agent’s dependency graph $G$ does not split the decision algorithm into separate, disconnected root nodes $\{\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})\}_{x \in \mathcal{X}}$ for each observation. Instead, $G$ contains a single policy node $\textsc{pfdt}(\underline{P}, \underline{G})$ whose value ranges over the policy space $\Pi$. Within $G$, the agent’s physical action is structurally determined by applying the policy node’s output to the observation variable:

$$\textsc{Act}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi,\, \textsc{Obs} = x\right) \coloneqq \pi(x).$$

Similarly, any predictor or twin in the environment whose behavior subjunctively depends on the agent’s decision algorithm is modeled in $G$ as a child of the unified policy node $\textsc{pfdt}(\underline{P}, \underline{G})$.

**P-FDT** then operates as a two-stage procedure:

**Stage 1 (Global Policy Selection):** Intervene on the policy node $\textsc{pfdt}(\underline{P}, \underline{G})$ to find the policy $\pi^* \in \Pi$ that maximizes unconditional expected utility across the entire world-model:

$$\mathrm{PFDT}_{\text{policy}}(P, G) \coloneqq \argmax_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right). \tag{5}$$

**Stage 2 (Local Policy Application):** Apply the optimal policy $\pi^*$ to the agent’s actual observation $x \in \mathcal{X}$ to output the physical action:

$$\mathrm{PFDT}(P, G, x) \coloneqq \left[\mathrm{PFDT}_{\text{policy}}(P, G)\right](x) = \pi^*(x). \tag{6}$$

Equations (5) and (6) capture the exact two-step structure described in footnote 16: the agent *"intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action."*

---

## 3. Subjunctive Dependence, Counterpossibles, and Updatelessness in P-FDT

Why should a rational agent evaluate counterfactual policies from an unconditional, global perspective via Equation (5) rather than conditioning on her observation $x$ and intervening on her immediate physical action $a$? The philosophical motivation of **P-FDT** rests on three pillars developed in the reference paper: *subjunctive dependence*, *counterpossible reasoning*, and *updatelessness*.

### Subjunctive Dependence and Type-Level Intervention

As Yudkowsky and Soares state, *"Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."* When two physical systems—such as two electronic calculators computing $6288 + 1048$, an agent and her psychological twin, or an agent and a predictor’s simulation of her—implement the same mathematical function, their physical outputs are logically constrained to covary (modulo hardware noise or prediction errors). They *subjunctively depend* on that function.

In terms of Charles Sanders Peirce’s type-token distinction, **CDT** intervenes only on the physical *token* ("my bodily action right now is $a$"). Consequently, **CDT** imagines impossible worlds in which a deterministic agent acts differently while an infallible predictor’s simulation of her remains unchanged. **FDT** and **P-FDT** intervene on the mathematical *type*. In **P-FDT**, the type is the entire policy function $\pi \in \Pi$. When a **P-FDT** agent evaluates the hypothetical $M^{\pi \hookrightarrow}$ induced by $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$, she updates every variable in her world-model that subjunctively depends on her policy: her own action $\textsc{Act} = \pi(\textsc{Obs})$, the actions of any copies or twins $\textsc{Act}_{\text{twin}} = \pi(\textsc{Obs}_{\text{twin}})$, and the predictions of any predictors who simulate how she responds to various observations.

### Counterpossible Conditionals

Because a fixed mathematical function $\mathrm{PFDT}_{\text{policy}}(P, G)$ has a single deterministic output $\pi^*$ of logical necessity, imagining $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$ for $\pi \neq \pi^*$ requires evaluating a *counterpossible* conditional—a counterfactual with a logically impossible antecedent, analogous to asking what would follow if $6288 + 1048 \neq 7336$ or if the twin prime conjecture were false. 

Ideally, as Yudkowsky and Soares note in Section 5, one would formalize this with a logical conditioning operator $\mathtt{true}(\phi)$ that updates $P$ on the counterpossible supposition that sentence $\phi$ holds. Because probability theory currently lacks a general semantics for $\mathtt{true}(\phi)$, both **FDT** and **P-FDT** bypass the obstacle by encoding the relevant logical and computational dependencies directly as directed edges in the graph $G$ and applying Pearl’s $\mathtt{do}$ operator to the node $\textsc{pfdt}(\underline{P}, \underline{G})$.

### Updatelessness and the Value of Information

Perhaps the most striking feature of Equation (5) is that $\textsc{Obs} = x$ does not appear inside the expectation $\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)\right)$ at all. As the authors note in their discussion of Wei Dai’s (2009) **updateless decision theory (UDT)** and Yudkowsky’s (2010) **timeless decision theory (TDT)**, conditioning on $\textsc{Obs} = x$ while also intervening on the decision node creates a harmful "double update" when observations themselves depend on the agent’s policy.

In **P-FDT**, the reason for not conditioning $P$ on $\textsc{Obs} = x$ becomes completely transparent. An observation $x$ is the *input* to a policy $\pi : \mathcal{X} \to \mathcal{A}$, not a constraint that restricts which world-states the policy’s consequences are averaged over. Because predictors often decide what observation $x$ to show the agent based on their prediction of $\pi(x)$—for example, whether to leave the agent in the desert or drive her to the city in Parfit’s hitchhiker problem, or whether to send a blackmail letter—changing the policy $\pi$ changes the probability distribution over $\textsc{Obs}$ itself. By optimizing $\pi$ against the prior distribution $P$ in Stage 1 and only plugging in $x$ in Stage 2, a **P-FDT** agent automatically acts as she would have precommitted to act prior to receiving any observations, guaranteeing that she never assigns negative expected value to information and is never dynamically inconsistent.

---

## 4. Applying P-FDT to Single-Agent Dilemmas: Transparent Newcomb and Mechanical Blackmail

To see how **P-FDT** works in practice—and how it simplifies the calculations of action-level **FDT**—let us apply Equations (5) and (6) to the **Transparent Newcomb Problem** (Dilemma 4 in the reference paper).

In the Transparent Newcomb Problem, both Box A (containing $\$1,000$) and Box B (containing either $\$1,000,000$ or $\$0$) are transparent. A predictor with $99\%$ accuracy placed $\$1,000,000$ in Box B if and only if she predicted that the agent would one-box (leave Box A behind) *upon observing that Box B is full*. Suppose the agent walks into the room and observes $x = \textit{full}$. Should she one-box or two-box?

Let us set up the **P-FDT** model $(P, G)$:
* **Observation space:** $\mathcal{X} = \{\textit{full}, \textit{empty}\}$.
* **Action space:** $\mathcal{A} = \{\textit{onebox}, \textit{twobox}\}$.
* **Policy space:** $\Pi = \mathcal{A}^{\mathcal{X}}$ contains $|\mathcal{A}|^{|\mathcal{X}|} = 2^2 = 4$ policies. We denote each policy $\pi \in \Pi$ as an ordered pair $\pi = (\pi(\textit{full}), \pi(\textit{empty}))$:
  $$\pi_{1,1} = (\textit{onebox}, \textit{onebox}), \quad \pi_{1,2} = (\textit{onebox}, \textit{twobox}),$$
  $$\pi_{2,1} = (\textit{twobox}, \textit{onebox}), \quad \pi_{2,2} = (\textit{twobox}, \textit{twobox}).$$
* **Structural dependency graph $G$ and distribution $P$:**
  The exogenous noise variable $\textsc{Accurate}$ takes value $\textit{accurate}$ with probability $0.99$ and $\textit{inaccurate}$ with probability $0.01$. The predictor’s prediction depends only on $\textsc{Accurate}$ and what the policy $\pi = \textsc{pfdt}(\underline{P}, \underline{G})$ prescribes when seeing $\textit{full}$:
  $$\textsc{Prediction}(\pi, \textit{accurate}) = \begin{cases} 1 & \text{if } \pi(\textit{full}) = \textit{onebox}, \\ 2 & \text{if } \pi(\textit{full}) = \textit{twobox}, \end{cases}$$
  and the reverse when $\textsc{Accurate} = \textit{inaccurate}$. Then $\textsc{Box B}(1) = \textit{full}$, $\textsc{Box B}(2) = \textit{empty}$, $\textsc{Obs} = \textsc{Box B}$, and $\textsc{Act}(\pi, \textsc{Obs}) = \pi(\textsc{Obs})$. The utility $\textsc{V}(\textsc{Act}, \textsc{Box B})$ is $\$1,001,000$ for $(\textit{twobox}, \textit{full})$, $\$1,000,000$ for $(\textit{onebox}, \textit{full})$, $\$1,000$ for $(\textit{twobox}, \textit{empty})$, and $\$0$ for $(\textit{onebox}, \textit{empty})$.

Now we execute **P-FDT**:

**Stage 1 (Global Policy Selection):** We compute $\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)\right)$ for each of the four candidate policies in $\Pi$:
1. **For $\pi_{1,1} = (\textit{onebox}, \textit{onebox})$:** Since $\pi_{1,1}(\textit{full}) = \textit{onebox}$, with probability $0.99$ ($\textit{accurate}$) Box B is $\textit{full}$ and the agent plays $\pi_{1,1}(\textit{full}) = \textit{onebox}$ (getting $\$1,000,000$); with probability $0.01$ ($\textit{inaccurate}$) Box B is $\textit{empty}$ and the agent plays $\pi_{1,1}(\textit{empty}) = \textit{onebox}$ (getting $\$0$).
   $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt} = \pi_{1,1})\right] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000.$$
2. **For $\pi_{1,2} = (\textit{onebox}, \textit{twobox})$:** With probability $0.99$ Box B is $\textit{full}$ and the agent plays $\textit{onebox}$ ($\$1,000,000$); with probability $0.01$ Box B is $\textit{empty}$ and the agent plays $\pi_{1,2}(\textit{empty}) = \textit{twobox}$ ($\$1,000$).
   $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt} = \pi_{1,2})\right] = 0.99(\$1,000,000) + 0.01(\$1,000) = \$990,010.$$
3. **For $\pi_{2,1} = (\textit{twobox}, \textit{onebox})$:** Since $\pi_{2,1}(\textit{full}) = \textit{twobox}$, Box B is $\textit{full}$ only when the predictor errs (probability $0.01$), in which case the agent plays $\textit{twobox}$ ($\$1,001,000$); with probability $0.99$ Box B is $\textit{empty}$ and the agent plays $\textit{onebox}$ ($\$0$).
   $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt} = \pi_{2,1})\right] = 0.01(\$1,001,000) + 0.99(\$0) = \$10,010.$$
4. **For $\pi_{2,2} = (\textit{twobox}, \textit{twobox})$:** With probability $0.01$ Box B is $\textit{full}$ and the agent plays $\textit{twobox}$ ($\$1,001,000$); with probability $0.99$ Box B is $\textit{empty}$ and the agent plays $\textit{twobox}$ ($\$1,000$).
   $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt} = \pi_{2,2})\right] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$

Comparing the four values, the unique optimal policy is $\pi^* = \pi_{1,2} = (\textit{onebox}, \textit{twobox})$, which achieves $\$990,010$.

**Stage 2 (Local Policy Application):** Having observed $x = \textit{full}$, the agent evaluates her chosen policy at her observation:
$$\mathrm{PFDT}(P, G, \textit{full}) = \pi_{1,2}(\textit{full}) = \textit{onebox}.$$
She leaves the $\$1,000$ behind and walks away with $\$1,000,000$. (And in the $1\%$ of cases where the predictor errs and she observes $x = \textit{empty}$, Stage 2 yields $\pi_{1,2}(\textit{empty}) = \textit{twobox}$, so she takes the $\$1,000$.) Exactly the same calculation applies to Parfit’s hitchhiker problem and the mechanical blackmail problem (Dilemma 8), where $\pi^*$ prescribes refusing to pay upon receiving the blackmail letter so long as the blackmailer’s prediction error rate is below $0.1\%$.

### A Subtle Advantage Over Action-Level FDT

Although **P-FDT** and action-level **FDT** prescribe the same action here, compare the mechanics of the two calculations. In Section 6 of Yudkowsky and Soares, when Fiona (running action-level **FDT**) sees $x = \textit{full}$, she intervenes *only* on the node $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full})$ while leaving the sibling node $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty})$ un-intervened upon. Consequently, Fiona has to introduce a prior probability parameter $q = P^F(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty}) = \textit{twobox})$ to evaluate the $1\%$ error branch, yielding $\$990,000 + 0.01 q \cdot \$1,000$ for one-boxing versus $\$10,010 + 0.99 q \cdot \$1,000$ for two-boxing. In **P-FDT**, the nuisance parameter $q$ vanishes completely: because $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$ specifies the agent’s behavior across *all* observation branches simultaneously, the agent never has to guess her own counterfactual behavior on unreached observation branches.

---

## 5. Where P-FDT Diverges from FDT: Multi-Agent Dilemmas with Asymmetric Observations

In footnotes 7 and 16, Yudkowsky and Soares remark that the distinction between iterating over policies (**P-FDT**) and iterating over actions (**FDT**) *"only matters in multi-agent dilemmas so far as we can tell."* Because the authors do not provide an example in their paper, we will construct two concrete multi-agent dilemmas that expose the mathematical mechanism behind this divergence.

Why does action-level **FDT** falter in multi-agent settings? Recall that in **FDT** (Equation 4), an agent who observes $x$ intervenes on the observation-specific node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$. If she is interacting with a computational twin (another agent running the same algorithm on the same model $(P, G)$), and both twins receive the *exact same* observation $x$, then both twins’ actions depend on the same node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$, so **FDT** coordinates them just fine. 

Suppose, however, that the two twins receive *different* observations: one twin observes $x_1 = \textit{room1}$ and the other twin observes $x_2 = \textit{room2}$. Under action-level **FDT**, the twin in Room 1 intervenes on $\textsc{fdt}(\underline{P}, \underline{G}, \textit{room1})$, whereas the twin in Room 2 is governed by the separate node $\textsc{fdt}(\underline{P}, \underline{G}, \textit{room2})$. Intervening on the first node does *not* alter the second node!

Let us see how this structural severing breaks action-level **FDT** in a multi-agent dilemma while **P-FDT** succeeds.

### Example 1: The Asymmetric-Observation Twin Vault Dilemma (Synergistic Cooperation)

Suppose an agent and her computational twin are placed in separate, causally isolated rooms—Room 1 and Room 2—with a $50\%$ probability of the agent waking up in Room 1 (and her twin in Room 2) and a $50\%$ probability of the agent waking up in Room 2 (and her twin in Room 1). Each room contains a heavy lever. Pulling the lever ($\textit{pull}$) costs the person in that room $\$1,000$ in effort; abstaining ($\textit{abstain}$) costs $\$0$. A vault containing $\$1,000,000$ for *each* twin opens if and only if **both** the twin in Room 1 and the twin in Room 2 pull their respective levers. The agent wakes up and observes $x = \textit{room1}$. Should she pull the lever?

**How Action-Level FDT Evaluates the Dilemma:**
In action-level **FDT**, the graph $G^F$ contains two independent root decision nodes: $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{room1})$ and $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{room2})$. Having observed $\textit{room1}$, the agent intervenes only on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{room1}) = a$. Let $q = P^F(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{room2}) = \textit{pull})$ be the agent’s prior probability that the **FDT** algorithm pulls the lever when given input $\textit{room2}$.
* **If $a = \textit{pull}$:** The twin in Room 1 always pulls, while the twin in Room 2 pulls with prior probability $q$. Thus, the vault opens with probability $q$ (yielding $\$1,000,000$). With probability $0.5$ the agent is in Room 1 (paying $\$1,000$), and with probability $0.5$ the agent is in Room 2 (paying $\$1,000$ with probability $q$). Her expected utility is:
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{room1}) = \textit{pull}\right)\right] = \$1,000,000 q - \$500 - \$500 q = \$999,500 q - \$500.$$
* **If $a = \textit{abstain}$:** The twin in Room 1 abstains, so the vault never opens ($\$0$). With probability $0.5$ the agent is in Room 1 (paying $\$0$), and with probability $0.5$ she is in Room 2 (still pulling with prior probability $q$ and paying $\$1,000$). Her expected utility is:
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{room1}) = \textit{abstain}\right)\right] = -\$500 q.$$

Comparing the two expectations, action-level **FDT** prescribes $\textit{pull}$ if and only if
$$\$999,500 q - \$500 > -\$500 q \iff q > 0.0005.$$
Notice what happens if $q < 0.0005$ (for example, $q = 0$, where the agent expects her twin in Room 2 to abstain): action-level **FDT** prescribes $\textit{abstain}$ in Room 1! By symmetry, if her prior that Room 1 pulls is also $0$, action-level **FDT** prescribes $\textit{abstain}$ in Room 2 as well. Furthermore, this mutual defection is *reflectively consistent*: given that $\mathrm{FDT}(P^F, G^F, \textit{room2}) = \textit{abstain}$, a rational prior $P^F$ *must* assign $q = 0$, locking action-level **FDT** into a pareto-inferior Nash equilibrium ($(\$0, \$0)$ instead of $(\$999,000, \$999,000)$). Despite Yudkowsky and Soares’s criticism of **EDT** in Section 6—that *"Eve's choices are at the mercy of her priors in a way that Carl and Fiona's are not"*—action-level **FDT** falls prey to the exact same prior-dependence across distinct observations! (The exact same failure occurs in a non-separable Twin Prisoner’s Dilemma with asymmetric observations whenever mutual defection pays $\$999,000$, mutual cooperation pays $\$1,000,000$, and unilateral defection pays $\$1,001,000$ vs. $\$0$: for any prior $q < \frac{498,500}{998,000} \approx 0.4995$, action-level **FDT** defects.)

**How P-FDT Evaluates the Dilemma:**
Now watch how **P-FDT** resolves the dilemma. In **P-FDT**, both twins share the single policy node $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$, where $\pi : \{\textit{room1}, \textit{room2}\} \to \{\textit{pull}, \textit{abstain}\}$. In Stage 1, the agent evaluates all four policies $\pi = (\pi(\textit{room1}), \pi(\textit{room2}))$:
* $\pi_{\text{pull},\text{pull}} = (\textit{pull}, \textit{pull})$: Both rooms pull, the vault opens with certainty, and both pay $\$1,000$.
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt} = \pi_{\text{pull},\text{pull}})\right] = \$1,000,000 - \$1,000 = \$999,000.$$
* $\pi_{\text{pull},\text{abst}} = (\textit{pull}, \textit{abstain})$ and $\pi_{\text{abst},\text{pull}} = (\textit{abstain}, \textit{pull})$: Only one room pulls; the vault stays locked, and the agent pays $\$1,000$ with probability $0.5$.
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt} = \pi_{\text{pull},\text{abst}})\right] = \mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt} = \pi_{\text{abst},\text{pull}})\right] = -\$500.$$
* $\pi_{\text{abst},\text{abst}} = (\textit{abstain}, \textit{abstain})$: Neither room pulls; the vault stays locked and nobody pays anything.
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt} = \pi_{\text{abst},\text{abst}})\right] = \$0.$$

Regardless of any prior beliefs, $\pi^* = \pi_{\text{pull},\text{pull}}$ is the unique global maximizer ($\$999,000$). In Stage 2, the twin in Room 1 computes $\pi^*(\textit{room1}) = \textit{pull}$ and the twin in Room 2 computes $\pi^*(\textit{room2}) = \textit{pull}$. Both pull their levers and walk away with $\$999,000$.

### Example 2: Known-Identity Asymmetric Twin Prisoner’s Dilemma

Suppose even more starkly that the two twins know from the outset which room they were born in—so in the first agent’s world-model $P$, her own payoff $\textsc{V}$ is deterministically the payoff of Room 1 ($\textsc{Obs}_{\text{self}} = \textit{room1}$ with probability $1$), while her twin in Room 2 observes $\textit{room2}$ and receives the payoff of Room 2. In a Prisoner’s Dilemma between Room 1 and Room 2, action-level **FDT** intervenes on $\textsc{fdt}(\underline{P}, \underline{G}, \textit{room1})$, which affects *only* the Room 1 action while leaving the Room 2 twin’s node $\textsc{fdt}(\underline{P}, \underline{G}, \textit{room2})$ untouched. Thus, under action-level **FDT**, defection strictly dominates cooperation by $\$1,000$, and both twins defect just like **CDT** agents! As we will examine in the next section, **P-FDT** can overcome even this barrier when paired with a proper operationalization of how policies handle indexical inputs.

---

## 6. Open Questions and Operational Extensions of P-FDT

Because Yudkowsky and Soares introduce **P-FDT** only in two brief footnotes, several important mathematical and philosophical questions are left open. Below, we distinguish what the source paper explicitly states from what it leaves unresolved, and we develop and justify operational completions for applying **P-FDT** to unfamiliar cases.

### Uncertainty 1: What Is the Domain of a Policy—"Observations" or All "Inputs"?

A careful comparison of footnotes 7 and 16 reveals a subtle tension in how the domain of a policy $\pi$ is defined:
* **Footnote 7** states that policies are *"mappings from observations to actions"* ($\pi : \mathcal{X} \to \mathcal{A}$), which matches our formalization in Equations (5) and (6) where the intervened node is $\textsc{pfdt}(\underline{P}, \underline{G})$.
* **Footnote 16**, however, writes the intervened node as $\mathrm{FDT}(-)$—with a blank argument slot—and says that it chooses *"a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action."*

In the authors' notation from Section 5, the "inputs" to the $\mathrm{FDT}$ procedure are the entire triple $(P, G, x)$, not just the observation $x$. Why does this distinction matter? 

Consider two cases where two agents (or two versions of an agent) differ not only in their sensory observation $x$, but in their local model $P$:
1. **The Smoking Lesion Problem (Section 6):** When Yudkowsky and Soares formalize the smoking lesion problem for Fiona, there is no observation variable $x$. Instead, having the lesion causes Fiona to have a utility function $\mathcal{U}_S$ (encoded in distribution $P_S^F$), whereas lacking the lesion gives her utility function $\mathcal{U}_R$ (encoded in $P_R^F$). Thus, her graph $G^F$ (Figure 4 of the paper) contains two nodes: $\textsc{fdt}(\underline{P_S^F}, \underline{G^F})$ and $\textsc{fdt}(\underline{P_R^F}, \underline{G^F})$.
2. **Multi-Agent Dilemmas with Indexical Utility Functions:** As we saw at the end of Section 5, if Twin 1 has a distribution $P_1$ whose utility variable $\textsc{V}_1$ measures exclusively Room 1’s payoff, and Twin 2 has a distribution $P_2$ whose utility variable $\textsc{V}_2$ measures exclusively Room 2’s payoff, then $\underline{P_1} \neq \underline{P_2}$. If the intervened node is $\textsc{pfdt}(\underline{P_1}, \underline{G})$, Twin 1’s intervention will not even connect to Twin 2’s node $\textsc{pfdt}(\underline{P_2}, \underline{G})$—or, if they share a node but Twin 1 maximizes only $\mathbb{E}[\textsc{V}_1]$, Twin 1 will select the asymmetric policy $\pi(\textit{room1}) = \textit{defect}, \pi(\textit{room2}) = \textit{cooperate}$, which cannot be simultaneously adopted by Twin 2!

**Operational Proposal (The Veil-of-Ignorance / Local-Input Representation):**
To make **P-FDT** work seamlessly across both single-agent preference uncertainty (like the smoking lesion) and multi-agent games (like asymmetric twin dilemmas), we propose a unified operational convention that reconciles Footnote 7 and Footnote 16:
1. All local, indexical features that differentiate one agent-instance from another—including sensory observations ("I am in Room 1") and local preference parameters or types ("my taste parameter for smoking is $\theta \in \{S, R\}$")—must be pushed into the local input $x \in \mathcal{X}$.
2. The world-model $(P, G)$ passed into $\textsc{pfdt}(\underline{P}, \underline{G})$ is then the *de-indexicalized common prior* (analogous to Harsanyi’s 1967 common prior behind a veil of ignorance) before the agent learns which indexical realization $x \in \mathcal{X}$ she occupies, with $\textsc{V} = \mathcal{U}(\textsc{Outcome}, \textsc{Obs})$ evaluating utility from the perspective of whichever local input $\textsc{Obs}$ is realized.

Under this operationalization, both twins in an asymmetric dilemma share the exact same de-indexicalized model $(P, G)$ and therefore share the node $\textsc{pfdt}(\underline{P}, \underline{G})$, while their distinct positions in the game are supplied as inputs $x_1, x_2 \in \mathcal{X}$ in Stage 2. Likewise, in the smoking lesion problem, $\mathcal{X} = \{S, R\}$ represents the internal craving input, and $\mathrm{PFDT}_{\text{policy}}(P, G)$ simultaneously selects the optimal policy $\pi^*(S) = \textit{smoke}, \pi^*(R) = \textit{refrain}$ in one global step.

### Uncertainty 2: Non-Unique Optimal Policies on Measure-Zero Observation Branches

A second technical question arises directly from Equation (5): what happens when a particular observation $x_0 \in \mathcal{X}$ has probability zero of occurring under the optimal policy?

Suppose that in the Transparent Newcomb Problem (or Mechanical Blackmail), the predictor is *100% infallible* ($P(\textsc{Accurate} = \textit{accurate}) = 1$). Let us re-evaluate the four policies in the Transparent Newcomb Problem when the predictor never errs:
* For $\pi_{1,1} = (\textit{onebox}, \textit{onebox})$: Box B is $\textit{full}$ with probability $1$, so $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi_{1,1})] = \$1,000,000$.
* For $\pi_{1,2} = (\textit{onebox}, \textit{twobox})$: Box B is $\textit{full}$ with probability $1$, so $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi_{1,2})] = \$1,000,000$.
* For $\pi_{2,1} = (\textit{twobox}, \textit{onebox})$: Box B is $\textit{empty}$ with probability $1$, so $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi_{2,1})] = \$0$.
* For $\pi_{2,2} = (\textit{twobox}, \textit{twobox})$: Box B is $\textit{empty}$ with probability $1$, so $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt} = \pi_{2,2})] = \$1,000$.

Because $P(\textsc{Obs} = \textit{empty} \mid \mathtt{do}(\textsc{pfdt} = \pi_{1,\cdot})) = 0$, the unconditional expectation in Stage 1 is completely insensitive to what $\pi$ prescribes at $x_0 = \textit{empty}$! Both $\pi_{1,1}$ and $\pi_{1,2}$ tie for the maximum at $\$1,000,000$. Even worse, in a sequential game where a predictor or opponent makes a threat that depends on what $\pi(x_0)$ would do on an off-path observation $x_0$ of probability $0$, naive maximization of Equation (5) cannot distinguish sensible off-path actions from absurd ones (the decision-theoretic analog of non-credible threats in Nash equilibria versus subgame-perfect equilibria).

**Operational Proposal ($\varepsilon$-Perturbed / Trembling-Hand Policy Selection):**
In the source paper, Yudkowsky and Soares usually avoid this degeneracy by assuming predictors have a small error probability $\varepsilon > 0$ (such as $\varepsilon = 0.01$ in Newcomb’s problem), though in the XOR blackmail and Death in Damascus they allow infallible predictors. To make **P-FDT** well-defined in all cases—including models initially stated with deterministic predictors—we propose an operational refinement inspired by Reinhard Selten’s (1975) trembling-hand perfection:

Given a model $(P, G)$ in which some observation branches have probability $0$, construct a family of perturbed distributions $P_\varepsilon$ ($\varepsilon \in (0, 1)$) in which every exogenous environmental mechanism or prediction node has at least probability $\varepsilon$ of misfiring independently, ensuring $P_\varepsilon(\textsc{Obs} = x \mid \mathtt{do}(\textsc{pfdt} = \pi)) > 0$ for all $x \in \mathcal{X}$ and $\pi \in \Pi$. Then define the selected policy in Stage 1 via the limit:

$$\mathrm{PFDT}_{\text{policy}}^*(P, G) \coloneqq \lim_{\varepsilon \to 0^+} \argmax_{\pi \in \Pi} \mathbb{E}_{P_\varepsilon}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right). \tag{7}$$

In the infallible Transparent Newcomb Problem, Equation (7) immediately breaks the tie between $\pi_{1,1}$ and $\pi_{1,2}$ in favor of $\pi_{1,2} = (\textit{onebox}, \textit{twobox})$, ensuring the agent never leaves behind the $\$1,000$ if the box is unexpectedly empty.

### Uncertainty 3: Deducing Subjunctive Graphs, Fairness, and Tractability

Finally, **P-FDT** inherits two foundational open problems explicitly highlighted by Yudkowsky and Soares in Sections 5, 9, and 10, while adding a computational challenge of its own:
1. **Deducing $G$ from observation:** While Pearl (2000) provides a rigorous methodology for learning causal graphs from physical interventions, we do not yet have a general formal theory for deducing the structure of logical and computational subjunctive dependencies from experience.
2. **Formalizing "fair" dilemmas:** No decision theory can win in "unfair" dilemmas that directly punish the agent’s source code (e.g., a mind-reader who pays $\$1,000,000$ if and only if the agent implements **CDT**). Formalizing the boundary between fair problems (which depend on predicted actions or policies) and unfair ones remains an open research problem.
3. **Policy-space complexity:** Whereas action-level **FDT** iterates over $|\mathcal{A}|$ actions, **P-FDT** iterates over $|\mathcal{A}|^{|\mathcal{X}|}$ policies. For bounded agents facing large observation spaces $\mathcal{X}$, exact enumeration of $\Pi$ is intractable, requiring functional approximations (such as parameterized policy classes $\Pi_\theta$) that preserve subjunctive coordination across relevant observation branches.

---

## 7. Summary Comparison of Decision Theories

To consolidate the distinctions developed across this essay, Table 1 summarizes how **EDT**, **CDT**, action-level **FDT**, and **P-FDT** construct hypotheticals and how they perform across diagnostic dilemmas.

| Decision Theory | Formal Rule for Selecting Action at Observation $x$ | Treatment of $\textsc{Obs} = x$ | Newcomb & Smoking Lesion | Transparent Newcomb & Parfit’s Hitchhiker | Multi-Agent Dilemma with Asymmetric Observations |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **EDT** | $\argmax_{a} \mathbb{E}[\textsc{V} \mid \textsc{Obs}=x, \textsc{Act}=a]$ | Conditions on $\textsc{Obs}=x$ | One-boxes; **Refrains** (fails) | **Two-boxes / Defects** (fails) | Fails if priors or observations break correlation |
| **CDT** | $\argmax_{a} \mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x]$ | Conditions on $\textsc{Obs}=x$ | **Two-boxes** (fails); Smokes | **Two-boxes / Defects** (fails) | **Defects** (fails) |
| **FDT** (Action-level) | $\argmax_{a} \mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})=a)]$ | Switches intervened node to $\underline{x}$ | One-boxes; Smokes | One-boxes; Pays driver | **Can fail / depend on priors $q$** across $x_1 \neq x_2$ |
| **P-FDT** (Policy-level) | $\left[\argmax_{\pi \in \Pi} \mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G})=\pi)]\right](x)$ | Evaluates $\pi$ unconditionally; applies $\pi^*(x)$ | One-boxes; Smokes | One-boxes; Pays driver (no prior $q$ needed) | **Cooperates / Coordinates** globally across $x_1 \neq x_2$ |

---

## 8. Conclusion

In Section 9 of their paper, Yudkowsky and Soares write that the core philosophical insight of functional decision theory is to choose from a *global perspective*—asking *"What would the entire universe look like if the FDT algorithm behaved differently?"* and selecting the option that yields the best universe.

As we have seen, **policy functional decision theory (P-FDT)**—the formulation sketched in footnotes 7 and 16—is the natural mathematical realization of that global perspective. When an agent intervenes only on her observation-indexed action node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$, her intervention remains partially local: she holds fixed what her own decision algorithm outputs on every other observation $y \neq x$. In single-agent dilemmas, this introduces nuisance priors over unreached observation branches; in multi-agent dilemmas where copies or computational twins receive different observations, it severs the subjunctive link between them and can cause coordination to collapse. By elevating the locus of subjunctive intervention from an individual action $a \in \mathcal{A}$ to the entire policy $\pi : \mathcal{X} \to \mathcal{A}$ and then applying the optimal policy $\pi^*$ to the actual input $x$, **P-FDT** unifies precommitment, updateless reasoning, and multi-agent coordination into a single mathematical principle.

## References

* Dai, W. (2009). Towards a new decision theory. *Less Wrong*.
* Gibbard, A., & Harper, W. L. (1978). Counterfactuals and two kinds of expected utility. In *Foundations and Applications of Decision Theory* (pp. 125–162). D. Reidel.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Kleene, S. C. (1938). On notation for ordinal numbers. *Journal of Symbolic Logic*, 3(4), 150–155.
* Lewis, D. (1979). Prisoners' dilemma is a Newcomb problem. *Philosophy & Public Affairs*, 8(3), 235–240.
* Nozick, R. (1969). Newcomb's problem and two principles of choice. In *Essays in Honor of Carl G. Hempel* (pp. 114–146). D. Reidel.
* Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
* Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Skyrms, B. (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Soares, N., & Fallenstein, B. (2015). Toward idealized decision theory. *arXiv preprint arXiv:1507.01986*.
* Yudkowsky, E. (2010). *Timeless Decision Theory*. The Singularity Institute.
* Yudkowsky, E., & Soares, N. (2017). Functional decision theory: A new theory of instrumental rationality. *arXiv preprint arXiv:1710.05060v2*.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Core Focus**

I'm focusing on clarifying the user's ultimate goal: a comprehensive mathematical essay or technical blog post that explains **P-FDT (policy functional decision theory)** and how to practically use it in decision-making scenarios. I need to fully grasp the necessary depth and breadth of the explanation.


**Analyzing the Source Material**

I'm now diving deep into the source paper by Yudkowsky and Soares, particularly footnotes 7 and 16, to extract the essence of P-FDT. The goal is to build a complete mathematical definition and related equations, along with illustrative examples. I'm focusing on contrasting P-FDT with EDT, CDT, and action-level FDT, while also identifying any open questions within the source that require an operational interpretation. The target length is 2400-3000 words for a mathematically literate audience.


**Clarifying Equation Interventions**

I'm now zeroing in on the nuanced handling of observations within the FDT framework, specifically concerning Equation (4). The key is understanding how FDT doesn't directly condition on the observation $x$. Rather, when the observation changes, the node being intervened upon itself changes; that's the core focus right now. The difference in treatment of these nodes is the key.


**Synthesizing Policy FDT**

I'm synthesizing the essence of P-FDT. I'm focusing on the intervention on *policies* rather than individual actions, as highlighted in the footnotes, especially 7 and 16. This is key to its behavior in multi-agent settings, where the agent is choosing a mapping from observation to action. I am now trying to formulate how this intervention differs from the standard FDT intervention (in equation 4).


**Formalizing P-FDT**

I'm working to formalize the policy-selection function more concretely. I'm focusing on defining the policy node, $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$, which maps observation histories to actions, and how that is used to maximize unconditionally expected utility. My goal now is to clearly outline the policy space, observations, actions, and the intervention in equation form.


**Interpreting Policy Input**

I'm now clarifying the nature of the policy's input. Is it merely the current observation, or is it the broader tuple of policy, environment, and observation? Footnotes 7 and 16 offer conflicting hints, and I'm actively resolving this ambiguity. I'm focusing on defining this policy node and formulating the appropriate input to select an action, to make sure it coheres with the mathematical definition.


**Resolving Domain Ambiguity**

I'm now honing in on resolving the conflict in footnotes 7 and 16 regarding the policy's domain. My focus is the exact inputs to the policy function and the intervened node. Footnote 7 specifies observations as input. Now, I am exploring how those relate to the model and parameters. I am going to make a clarifying assumption, which coheres with the mathematical definition.


**Interpreting Policy Input**

I'm now clarifying the nature of the policy's input, exploring two interpretations. I am focusing on defining this policy node and formulating the appropriate input to select an action, to ensure it coheres with the mathematical definition. The observation-policy interpretation emphasizes a fixed model and mapping from observations, while the full-input perspective involves an epistemic state and broader inputs. The latter appears to accommodate diverse agent knowledge.



**Investigating Multi-Agent Impact**

I'm digging into why the authors claim that the difference between action-FDT (Equation 4) and P-FDT "only matters in multi-agent dilemmas." I'm also checking if this is also relevant in single-agent dilemmas. Currently, I am focused on the mathematics of both within the Transparent Newcomb problem. I am looking at how Fiona's actions would change under different conditions.


**Analyzing the Stakes**

I'm now fully immersed in the mathematics of the Transparent Newcomb problem, carefully examining the implications of the prior *q* on expected value calculations. I see that the $q$ term doesn't cancel out, leading to varying weights based on action. I now see that in this particular example, the value of *q* does not change the argmax.


**Evaluating Multi-Agent Dynamics**

I'm now deeply engaged in a multi-agent dilemma, specifically an asymmetric game with incomplete information. Analyzing how action-FDT and P-FDT function in such a scenario, I am focusing on the implications of each approach to coordination across distinct observations. I see clear distinctions in outcomes; action-FDT fails to coordinate, while P-FDT offers a shared policy.


**Clarifying Agent Coordination**

I'm now zeroing in on the coordination advantages of P-FDT in both multi-agent and single-agent scenarios. I see that when the agent is using P-FDT, the intervention on the policy node facilitates a cohesive strategy across multiple roles, even with differing observations. Conversely, Action-FDT can get stuck in suboptimal equilibria due to its piecemeal optimization across observations, especially where coordination or joint patterns are key.



**Addressing Zero-Probability Events**

I'm now grappling with how P-FDT handles actions on observation branches with zero probability. I am focusing on how to determine optimal behavior on these zero-probability branches, which don't directly influence unconditional expected utility. I need to clarify what the best approach is to this classic problem in updateless/policy decision theories.


**Clarifying P-FDT Differences**

I'm now setting up the formal machinery to contrast decision theories. I am comparing the landscape: EDT, CDT, action-FDT and P-FDT. I will focus on the key differences in how each theory defines the intervention in Equation 4 of Yudkowsky & Soares (2017). My work is focused on resolving any formal questions left open by the footnotes.



**Formulating Mathematical Elements**

I'm now establishing the formal groundwork, outlining countable outcomes, finite actions, countable observations, utility, and the world-model. I am focusing on stating the equations for EDT, CDT, and standard action-FDT. I am introducing the policy space and formulating P-FDT as a two-stage process: global policy optimization via subjunctive intervention on the policy node and policy evaluation at the observed x.


**Defining Policy Nodes**

I'm now focusing on how the policy node, $\textsc{pfdt}(\underline{P}, \underline{G})$, outputs an action, $\textsc{Act} = \textsc{pfdt}(\underline{P}, \underline{G})(\textsc{Obs})$. I'm formalizing the relationship between subjunctive interventions on policies and the ultimate action selection, which is the key goal.



**Calculating P-FDT Solutions**

I'm working on a precise calculation for the Mechanical Blackmail problem. I am explicitly defining the four policies and computing expected utilities under P-FDT. I'm demonstrating how P-FDT's intervention removes the need for arbitrary prior probabilities on unreached branches, compared to standard FDT, and I'll clarify how this leads to the correct policy choice.


**Constructing an Example**

I'm now building out an Asymmetric Twin Prisoner's Dilemma, mathematically illustrating where action-level FDT stumbles. I'm focusing on defining the observation-action mappings and the resulting payoffs, to highlight how policy-FDT offers a superior, more coordinated solution. I am clarifying how standard FDT leads to suboptimal equilibria.


**Illustrating Solution Synergy**

I'm now demonstrating, with the Asymmetric Twin Prisoner's Dilemma, how P-FDT seamlessly solves where action-level FDT fails, focusing on the intervention on the shared policy node. The resulting joint policy promotes cooperation. I'm clarifying how standard FDT leads to suboptimal equilibria.


**Justifying Model Integration**

I'm now determining if the policy node is $\textsc{pfdt}(\underline{G})$ mapping $(P, x) \mapsto a$, or if $\mathcal{X}$ must incorporate all local sensory inputs, with a unified prior. I'm focusing on justifying the operationalization of a unified prior versus local inputs, especially given uncertainty in types and multi-agent game scenarios.



**Addressing Computational Concerns**

I'm now outlining key constraints and details, including word count and source fidelity. I'm focusing on the computational complexity inherent in iterating through policies. I'm noting the paper's open question on subjunctive graph deduction and fairness. I'll need to monitor length and ensure quotations are exact.


**Verifying Quotations**

I'm now cross-referencing all direct quotations from Yudkowsky and Soares, ensuring precise accuracy of phrasing and notation, per your directive. I am focusing on footnotes 7 and 16, and the Joyce quote, for accuracy.


**Refining Decision Theory Names**

I'm now making sure all decision theories are clearly and consistently named throughout. Specifically, I am ensuring to use "P-FDT" for policy functional decision theory, "EDT" for evidential decision theory, "CDT" for causal decision theory, and "FDT" for the action-selection formulation (from Yudkowsky & Soares) to avoid ambiguity. I am also working to ensure that any proposed mathematical formalizations, examples, and operational refinements are clearly distinguished from claims directly attributable to the source material.


**Calculating Transparent Newcomb**

I'm now calculating policy utilities for Transparent Newcomb. I've defined policies, observation space, and action space. Currently, I'm focusing on the expected utility calculations for each of the four policies, given in the source paper by Yudkowsky and Soares. I will confirm the P-FDT solution aligns with the specified solution, thus showing expected utility.


**Defining Newcomb's Predictor**

I'm now analyzing the predictor's mechanics in Transparent Newcomb, clarifying its function and accuracy. I'm focusing on formally defining the structural equations for the prediction, box content, and the agent's actions within the P-FDT graph. I need to make sure this aligns with the source paper.



**Calculating Transparent Newcomb**

I'm now calculating policy utilities for Transparent Newcomb. After defining policies, observation space, and action space, I'm focusing on deriving the expected utility calculations for each of the four defined policies in the source paper by Yudkowsky and Soares. I will be confirming that the P-FDT solution aligns with the specified solution.


**Calculating Policy Outcomes**

I'm now calculating the Transparent Newcomb problem's policy utilities based on the given policies, actions, and predictor. I am focusing on deriving the policy utilities, which will be: \$990,010, \$10,010, \$1,001,000, and \$1,000, respectively. I am comparing my derivations with the source.


**Calculating Expected Utility**

I'm now calculating the Transparent Newcomb problem's policy utilities based on the agent's defined policies and predictor. I'm focusing on deriving the expected utility calculations for each policy, comparing my derivations with the source material, and ensuring alignment. My next step will be calculating utility with new policies and with the defined predictor.


**Analyzing Dilemma Solutions**

I'm now deeply focused on the Asymmetric Twin Prisoner's Dilemma, using its structure to showcase the differences between action-FDT and P-FDT in a multi-agent setting. I'm focusing on deriving the policy utilities and comparing solutions, ensuring they align with the expected outcomes of each decision theory.


**Contrasting FDT Interventions**

I'm now zeroing in on the divergence when both twins apply action-level FDT in the dilemma. My focus is the intervention's impact on each twin's world-model and subsequent action selection, which is the key distinction. I am formalizing the distinct decision-output nodes and their interventions.


**Refining Twin Dilemma Formalization**

I'm now refining the formal structure of the Asymmetric Twin Prisoner's Dilemma, focusing on each twin's world-model and their prior probabilities regarding the other's action. I need to make sure that the formal derivation properly expresses how the intervention on the policy in Room 1, leaves the decision process for the twin in Room 2 untouched. This also requires making sure that the probability of each twin's location is correctly formulated.


**Calculating Dilemma Payoffs**

I'm now calculating the payoffs within the Asymmetric Twin Prisoner's Dilemma under the described conditions. I'm focusing on scenarios where the decision-maker in Room 1 defects, and the associated expected utilities for both outcomes. I'm comparing this to the source material to identify how FDT *defects*.


**Calculating Dilemma Outcomes**

I'm now calculating the Asymmetric Twin Prisoner's Dilemma's expected payoffs, particularly for the scenarios of cooperation and defection. I see that the expected utility of the joint policy of cooperation is significantly higher, and I'm focused on highlighting the mathematical benefits of intervention on that policy to see how to align it.


**Interpreting Dilemma Intervention**

I'm focusing now on precisely interpreting the impact of interventions in the Asymmetric Twin Prisoner's Dilemma. I'm focusing on why a single intervention on a policy node can influence multiple agents' actions, and the formal conditions where this doesn't occur. I am contrasting these conditions with the agent's prior.


**Clarifying Lever Game**

I'm now formulating a twin coordination game involving levers in separate rooms. Focusing on the utility function, I want to clarify conditions where success requires pulling the *same* levers, and conditions that lead to opposite actions for mutual gain. The key is to show that agents can achieve the mutual reward when they know where they are.



**Calculating Vault Game**

I'm now calculating the Action-FDT (Equation 4) on the Vault Game where twin 1 observes room1, and focusing on the conditional expected utility of Twin 1 pulling their lever. I'm focusing on deriving the expected outcomes and the payoff structure. I will identify the role of the prior *q* in this problem.


**Calculating Action-FDT Utility**

I'm currently calculating the action-FDT expected utility for the Vault Game, specifically examining the outcomes of pulling versus abstaining when the twin is in Room 1. I see that the expected utility depends on the prior *q*, and the payoff structure. I'm noting the difference in conditional expectations of action-FDT and contrasting them.


**Analyzing Self-Confirming Outcomes**

I'm currently focusing on calculating the Action-FDT solution within the Vault Game. I see that under specific priors, such as q=0, the agent's pessimistic belief is self-confirming. Action-FDT then outputs abstain in both rooms. The stability and resulting suboptimality demonstrate FDT's coordination limitations.


**Contrasting FDT Instability**

I am now focusing on how action-FDT, due to splitting the decision function, becomes subject to prior biases in multi-agent dilemmas with distinct observations. When roles are known in advance, action-FDT can yield suboptimal choices, *always defecting* in some cases. P-FDT offers a more robust solution in comparison.


**Comparing Policy Intervention**

I am now contrasting P-FDT's unified policy intervention in the Vault Game with action-FDT's disjoint approach. By intervening on the single policy node $\pi$, P-FDT bypasses prior-dependent suboptimality. My calculations are focusing on the resulting unconditional expected utilities, and demonstrating how this aligns with the source.


**Calculating Joint Cooperation**

I'm now calculating the unconditional expected utility under the policy that *both twins cooperate* within the Asymmetric Twin Prisoner's Dilemma, showing its superiority. My focus is on the intervention, which facilitates coordinated action. I'm confirming that P-FDT yields the desired joint policy of (\textit{pull}, \textit{pull}) and comparing it with the solution of the source.


**Analyzing Complementary Payoffs**

I'm now zeroing in on a Gift-Giving Twin Prisoner's Dilemma, showing that action-FDT *succeeds* in this example because the action in one room benefits the twin in the other room. I'm focusing on contrasting this with a payoff requiring coordination where action-FDT fails because it can't handle payoffs where synergy is needed to get a reward.


**Clarifying Decision Coordination**

I'm now investigating scenarios where action-FDT can't coordinate actions across agents, especially when agents are *distinct*. I'm focusing on clarifying how a single intervention on a disjoint policy node can impact multiple agents, particularly in the multi-agent context. I will highlight how prior biases can lead to suboptimal outcomes.


**Refining Agent-Specific Observations**

I'm working to clarify how an agent's utility is affected by their distinct observations, especially in situations with multiple agents and rooms. I'm focusing on defining how the coin flip determines the room and utility, and how this relates to interventions on policy functions.


**Comparing Game Conditions**

I'm now comparing the outcomes of the Vault Stag Hunt and the Asymmetric Twin Prisoner's Dilemma, focusing on scenarios with varying priors and incomplete information. I'm focusing on contrasting how both games are structured to show the weaknesses of Action-FDT and the advantages of P-FDT in coordination dilemmas with distinct observations. I will compare the mathematical consequences of each.


**Clarifying Distinct Observations**

I am now clarifying how FDT handles observations in scenarios where agents have distinct observations, specifically in the Asymmetric Twin Prisoner's Dilemma. I'm focusing on defining the observation inputs for each twin, and highlighting how they will intervene on their own policy function. I'm focusing on clarifying how they are modeled in the mathematical structure.


**Analyzing Room Differences**

I'm now focusing on contrasting action-level FDT and P-FDT in the gift-giving scenario. I've noted that while action-FDT succeeds, it also fails in some other games. I'm clarifying how each decision theory handles the twin's room and distinct observations, in which policy-level interventions occur. The intervention for policy-FDT is to change the shared policy, which allows the agent to decide between cooperation and defection.


**Revising Policy Selection**

I'm now reconsidering the policy selection within the asymmetric game. I'm focusing on the agent's goal to maximize *their* room's payoff. The policy $\pi$ becomes $\pi(\textit{room1}) = \textit{defect}, \pi(\textit{room2}) = \textit{cooperate}$ which gives the room one's player $1,001,000$. I'm considering why Bob wouldn't choose the same.


**Refining Prior Model Analysis**

I'm now clarifying the shared model requirement for P-FDT in multi-agent dilemmas, focusing on the implications of a shared prior "P" versus agent-specific observations. I am clarifying how the shared policy is applied with agent specific observation.


**Clarifying Twin Observations**

I'm now clarifying how Alice and Bob, in the multi-agent dilemma, compute the *same* P-FDT function despite different observations. My focus is on the formalism: their shared world-model $(P, G)$ is indexically symmetric before observation $\textsc{Obs}$, but Alice's and Bob's indexical identities are realized differently in their respective observations.


**Analyzing Separable Dilemmas**

I'm now analyzing the implications of separable dilemmas on Action-FDT in the context of Prisoner's Dilemmas. I see that with a 50/50 prior, cooperation is optimal for Action-FDT. I am focusing on how non-separable scenarios differ, especially when mutual cooperation is required for a reward.


**Revising Separability Analysis**

I'm now investigating the implications of a non-additively separable Prisoner's Dilemma, and focusing on clarifying payoffs where mutual cooperation yields a reward that's not simply the sum of individual actions. This is key to differentiating action-FDT and P-FDT.


**Revising Payoff Dilemma**

I'm now revising my Prisoner's Dilemma example with synergistic payoffs to make it a true dilemma: where defection *strictly* dominates. My goal is to ensure mutual cooperation Pareto-dominates mutual defection, with cooperation at \$1,000,000, and defection at \$999,000. I'm clarifying the payoffs to make the model correct.


**Clarifying Game Utility**

I'm now clarifying the payoff structure in the revised Prisoner's Dilemma, and have a more nuanced version. I've ensured defection is the optimal strategy and that mutual cooperation is strictly Pareto-superior.


**Calculating Action-FDT Payoffs**

I've just calculated action-FDT expected utility for the Prisoner's Dilemma, considering the revised payoffs where defection strictly dominates. The results show a significant difference. Action-FDT outputs defection regardless of the room. I will contrast this to other results.


**Refining Payoff Analysis**

I'm now zeroing in on Action-FDT within the revised Prisoner's Dilemma, and focusing on clarifying payoffs where mutual cooperation yields a reward that's not simply the sum of individual actions. I see that defection is the optimal strategy, and the expected utility calculation consistently points to defection in both rooms.


**Finalizing Example Clarity**

I'm now putting the finishing touches on the Asymmetric Twin Prisoner's Dilemma example. I'm focusing on ensuring its clarity and efficacy in contrasting Action-FDT and P-FDT. I need to ensure it uses the notation from Yudkowsky and Soares to prove mathematically why P-FDT solves this multi-agent dilemma, even with asymmetric observations.


**Refining Prompt Compliance**

I'm now carefully re-evaluating the current prompt to ensure complete compliance. My focus is on ensuring my updates consistently reflect both the formal mathematical aspects of P-FDT and the intended audience, and that I'm correctly identifying and interpreting any open questions or assumptions in the source material. I'm taking extreme caution to distinguish between the authors' claims and any additional interpretations.


**Refining Document Structure**

I'm now focusing on refining the essay's overall structure, paying close attention to word count constraints, and ensuring a smooth flow. I will make sure all quotations are accurate. I'm focusing on hitting the word count target.


**Refining Multi-Agent Analysis**

I'm now integrating insights on agent interactions in multi-agent settings. I'm focusing on contrasting how action-FDT and P-FDT function when agents have differing observations and need to coordinate actions. I'm refining mathematical formalizations of their respective interventions to clarify outcomes.


```
