# 029_fdt_policy_google_gemini-4-argon_rhigh_phigh / 00010

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/3eb4d9e9-7a84-448f-b4c1-d26f32ce04ef/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/3eb4d9e9-7a84-448f-b4c1-d26f32ce04ef/call_0/response.raw) · finish: `length`

### Visible response

````text
# From Actions to Policies: A Mathematical Account of Policy Functional Decision Theory (P-FDT)

## 1. Introduction: Why Decision Theory Needs Policies

Traditional normative decision theory is divided between two major paradigms: **evidential decision theory (EDT)** and **causal decision theory (CDT)**. When an agent chooses an action $a$ from a finite set of available actions $\mathcal{A}$ after recording an observation history $x \in \mathcal{X}$, both theories tell the agent to maximize expected utility, but they disagree on how to construct the hypothetical scenarios used to evaluate each option. EDT evaluates an action by Bayesian conditionalization, asking which action would be the best news to learn one had taken. CDT evaluates an action by causal intervention, asking which physical act causes the best downstream outcome while holding the past and all causal independencies fixed.

As Yudkowsky and Soares (2017) demonstrate in *"Functional Decision Theory: A New Theory of Instrumental Rationality"*, both EDT and CDT fail systematically in decision problems involving predictors, replicators, or psychological twins. CDT leaves money on the table in Newcomb's problem, defects against a psychological twin in the Prisoner's Dilemma, and dies in the desert in Parfit's hitchhiker problem because it treats accurate predictions of the agent's current decision as causally independent of that decision. EDT one-boxes in Newcomb's problem, but it irrationally forgoes smoking in the smoking lesion problem, pays extortionists in the XOR blackmail problem, and two-boxes once it sees the boxes in the transparent Newcomb problem because it conditions on its current observations and cannot break merely statistical correlations.

To resolve these failures with a single decision rule, Yudkowsky and Soares propose **functional decision theory (FDT)**. The philosophical core of FDT is that an agent should treat her decision as the output of a fixed mathematical function and ask: *"Which output of this very function would yield the best outcome?"* Instead of intervening on a physical action token $\textsc{Act}$, an FDT agent intervenes on the logical output of her decision algorithm, propagating changes along all relations of **subjunctive dependence**—the logical, mathematical, and computational correlations linking any physical systems (such as predictors or twins) that compute or model that same function.

However, a careful reading of Yudkowsky and Soares (2017) reveals that the paper actually contains two distinct formalizations of functional decision theory. In the main text, for pedagogical simplicity, the authors formalize what we will call **action functional decision theory (A-FDT)**: an algorithm that takes a world-model and an observation $x$ and intervenes on an observation-indexed node to select a single action $a \in \mathcal{A}$. Yet in two crucial remarks—Footnote 7 and Footnote 16—the authors state that their preferred formalization is actually a policy-selection theory, which we will call **policy functional decision theory (P-FDT)**. In Footnote 7, they write:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

And in Footnote 16, while discussing why functional decision theorists entertain hypotheticals in which they made different observations, they elaborate:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

Because Yudkowsky and Soares set this distinction aside in their main text, they never write down the formal equations for **P-FDT**, nor do they show explicitly how a P-FDT causal/subjunctive graph differs from an A-FDT graph, why P-FDT and A-FDT diverge in multi-agent dilemmas, or how to resolve the technical ambiguities left open by Footnote 16. 

In this essay, we develop a complete mathematical formulation of **P-FDT**. We will show how P-FDT evaluates alternative policies, how it handles counterfactuals and subjunctive dependencies, how to apply it to both single-agent Newcomblike problems and unfamiliar multi-agent dilemmas, and how to operationalize the open questions left unresolved by the source text. Throughout, we will explicitly distinguish the claims made by Yudkowsky and Soares (2017) from our own formal reconstructions and extensions.

---

## 2. The Formal Architecture of EDT, CDT, A-FDT, and P-FDT

Following Gibbard and Harper (1978) and Joyce (1999), Yudkowsky and Soares (2017) frame expected utility maximization around a countable set of outcomes $\mathcal{O} = \{o_1, o_2, \dots\}$, a finite set of actions $\mathcal{A}$, a countable set of observation histories $\mathcal{X}$, and a bounded real-valued utility function $\mathcal{U} : \mathcal{O} \to \mathbb{R}$. Let $\textsc{Outcome}$, $\textsc{Obs}$, and $\textsc{Act}$ be random variables taking values in $\mathcal{O}$, $\mathcal{X}$, and $\mathcal{A}$ respectively, and define the utility random variable $V \coloneqq \mathcal{U}(\textsc{Outcome})$. Every expected utility theory prescribes choosing an option that maximizes

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j), \tag{1}$$

where $P(a \hookrightarrow o_j ;\, x)$ is the probability assigned to outcome $o_j$ in the hypothetical scenario $\mathcal{M}^{a\hookrightarrow}$ constructed for action $a$ given observation $x$.

### 2.1 EDT, CDT, and A-FDT in the Source Text

As formalized in Section 5 of Yudkowsky and Soares (2017), the theories differ in how an agent represents her world-model $M$ and constructs hypotheticals from it:

1. **Evidential Decision Theory (EDT)** represents the world-model solely as a probability distribution $P$ and constructs hypotheticals by conditioning on both the observation $x$ and the action $a$ (restricting to actions with $P(\textsc{Act}=a \mid \textsc{Obs}=x) > 0$):
   $$\mathrm{EDT}(P, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(V \;\middle|\; \textsc{Obs}=x, \textsc{Act}=a\right). \tag{2}$$

2. **Causal Decision Theory (CDT)** augments $P$ with a directed acyclic causal graph $G$ following Pearl (1996, 2000). It conditions on the observation $\textsc{Obs}=x$, but uses Pearl's surgical intervention operator $\mathtt{do}(\textsc{Act}=a)$ to sever all incoming arrows into $\textsc{Act}$ while propagating causal effects downstream:
   $$\mathrm{CDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(V \;\middle|\; \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x\right). \tag{3}$$

3. **Action Functional Decision Theory (A-FDT)**—the formulation in Equation (4) of Yudkowsky and Soares (2017)—augments $P$ with an expanded dependency graph $G$ that encodes not only physical causation, but also *subjunctive dependence*: how physical variables (like a predictor's prediction or a twin's choice) depend on the outputs of mathematical functions. Using underline notation $\underline{z}$ for dequoting (embedding the value of $z$ into a variable's syntactic name via Kleene's second recursion theorem), A-FDT intervenes on the logical variable $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ representing the output of the A-FDT algorithm on inputs $(P, G, x)$:
   $$\mathrm{AFDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(V \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right). \tag{4}$$

Notice two vital features of Equation (4) highlighted by Yudkowsky and Soares. First, A-FDT intervenes on a *logical* node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ rather than the physical node $\textsc{Act}$. Second, A-FDT is *updateless* (in the sense of Dai, 2009): it does not condition $P$ on $\textsc{Obs}=x$ (unlike Yudkowsky's 2010 **timeless decision theory (TDT)**, which both conditioned on $\textsc{Obs}=x$ and intervened on the logical node, creating a harmful "double update"). Instead, when an A-FDT agent observes $x$, she responds to the observation solely by changing *which node* she intervenes upon—from $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ to $\textsc{fdt}(\underline{P}, \underline{G}, \underline{y})$ when her observation changes from $x$ to $y$. (As a minor textual note, in Section 6 of the source paper, an unnumbered formula for the transparent Newcomb problem contains a typographical error reading $\mathbb{E}(V \mid \mathtt{do}(\textsc{fdt}(\underline{P}^F, \underline{G}^F, \textit{full})=a, \textsc{Obs}=\textit{full})$, which drops a closing parenthesis and includes $\textsc{Obs}=\textit{full}$; however, the authors' prose immediately above it and their explicit numerical derivation immediately below it confirm that Equation (4)—without conditioning on $\textsc{Obs}=\textit{full}$—is what they actually evaluate.)

### 2.2 Formalizing P-FDT

We now construct the formal mathematical definition of **P-FDT** from Footnotes 7 and 16. (While the conceptual definition of P-FDT as intervening on $\mathrm{FDT}(-)$ to select a policy and then applying that policy to the agent's inputs comes directly from Yudkowsky and Soares, the explicit equations and graphical semantics below are our formal reconstruction.)

Let $\mathcal{X}$ be the set of possible observations (assuming $\mathcal{X}$ and $\mathcal{A}$ are finite so that the policy space is finite and well-behaved), and let

$$\Pi \coloneqq \mathcal{A}^{\mathcal{X}} = \{\pi : \mathcal{X} \to \mathcal{A}\}$$

be the set of all deterministic **policies** mapping observations to actions. 

In **P-FDT**, the dependency graph $G$ does not split the agent's decision procedure into separate root variables $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ for each possible observation $x \in \mathcal{X}$. Instead, $G$ contains a single policy-valued root node $\textsc{pfdt}(\underline{P}, \underline{G})$ taking values in $\Pi$, which represents the policy output by the P-FDT policy-selection function on world-model $(P, G)$. In $G$, the agent's physical action $\textsc{Act}$ is a deterministic function of both the policy node $\textsc{pfdt}(\underline{P}, \underline{G})$ and the observation node $\textsc{Obs}$ via functional application:

$$\textsc{Act}\big(\pi, x\big) \coloneqq \pi(x). \tag{5}$$

Similarly, any predictor or twin in the environment who models or implements the agent's decision procedure is represented in $G$ as subjunctively downstream of the policy node $\textsc{pfdt}(\underline{P}, \underline{G})$.

Given a world-model $(P, G)$ and a realized observation $x \in \mathcal{X}$, **P-FDT** operates in two stages:

1. **Policy Selection (Global Intervention Stage):** The agent iterates over all candidate policies $\pi \in \Pi$. For each $\pi$, she constructs the hypothetical model $M^{\pi\hookrightarrow}$ by applying Pearl's $\mathtt{do}$-operator to set $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$ in $(P, G)$, and selects the policy $\pi^*$ that maximizes expected utility across the entire prior distribution $P$:
   $$\Pi^*(P, G) \coloneqq \operatorname*{argmax}_{\pi \in \Pi} \mathbb{E}\left(V \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right). \tag{6}$$

2. **Policy Application (Execution Stage):** Choosing a canonical optimal policy $\pi^* \in \Pi^*(P, G)$, the agent feeds her actual observation $x$ as input to $\pi^*$ to output her physical action:
   $$\mathrm{PFDT}(P, G, x) \coloneqq \pi^*(x) = \left[\operatorname*{argmax}_{\pi \in \Pi} \mathbb{E}\left(V \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right)\right](x). \tag{7}$$

Compare Equations (4) and (7). In A-FDT, the observation $x$ enters *inside* the $\mathtt{do}$-operator, indexing which node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ is intervened upon while leaving all sibling nodes $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x'})$ ($x' \neq x$) untouched at their prior distributions in $P$. In **P-FDT**, the observation $x$ stands completely *outside* the $\operatorname{argmax}$ and the $\mathtt{do}$-operator! The intervention $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$ simultaneously specifies how the agent behaves at *every* observation $x' \in \mathcal{X}$. Once the globally optimal policy $\pi^*$ is determined from $(P, G)$, the agent simply evaluates $\pi^*(x)$.

---

## 3. Applying P-FDT to Single-Agent Dilemmas: The Transparent Newcomb Problem

To see how P-FDT works and why Yudkowsky and Soares note that it yields the same prescriptions as A-FDT in the single-agent dilemmas of their paper, let us work through the **Transparent Newcomb Problem** (Dilemma 5 in the source paper, due to Drescher, 2006).

Recall the setup: Box A is transparent and contains $\$1,000$. Box B is also transparent and contains either $\$1,000,000$ ($\textit{full}$) or $\$0$ ($\textit{empty}$). A predictor who is $99\%$ accurate ($\textsc{Accurate} = \textit{accurate}$ with probability $0.99$, $\textit{inaccurate}$ with probability $0.01$) places $\$1,000,000$ in Box B if and only if she predicts that the agent will one-box ($\textit{onebox}$) upon observing that Box B is $\textit{full}$. The agent looks at Box B, observes $\textsc{Obs} = \textit{full}$, and must choose $a \in \mathcal{A} = \{\textit{onebox}, \textit{twobox}\}$.

### 3.1 How A-FDT Analyzes the Problem

In Section 6 of Yudkowsky and Soares (2017), Fiona's A-FDT graph $G^F$ has two separate decision nodes: $\textsc{fdt}(\underline{P}^F, \underline{G}^F, \textit{full})$ and $\textsc{fdt}(\underline{P}^F, \underline{G}^F, \textit{empty})$. Because the predictor only cares about what Fiona does when she sees a full box, only $\textsc{fdt}(\underline{P}^F, \underline{G}^F, \textit{full})$ has an arrow to $\textsc{Prediction}$. When Fiona sees $\textsc{Obs} = \textit{full}$, A-FDT intervenes solely on $\textsc{fdt}(\underline{P}^F, \underline{G}^F, \textit{full}) = a$. 

What happens in the $1\%$ branch where the predictor makes an error and leaves Box B empty? In that branch, Fiona's action is controlled by the *un-intervened* node $\textsc{fdt}(\underline{P}^F, \underline{G}^F, \textit{empty})$. Consequently, to compute her expected utility in A-FDT, Fiona must assign a prior subjective probability $q = P^F(\textsc{fdt}(\underline{P}^F, \underline{G}^F, \textit{empty}) = \textit{twobox})$ to what she would do if she saw an empty box, yielding $\$990,000 + 0.01q \cdot \$1,000$ for $a = \textit{onebox}$ versus $\$10,010 + 0.99q \cdot \$1,000$ for $a = \textit{twobox}$.

### 3.2 How P-FDT Analyzes the Problem

Now let us set up the same dilemma in **P-FDT**. Here $\mathcal{X} = \{\textit{full}, \textit{empty}\}$ and $\mathcal{A} = \{\textit{onebox}, \textit{twobox}\}$. There are $2^2 = 4$ possible policies in $\Pi = \mathcal{A}^{\mathcal{X}}$, which we can write as ordered pairs $\pi = (\pi(\textit{full}), \pi(\textit{empty}))$:

$$\begin{aligned}
\pi_{11} &= (\textit{onebox}, \textit{onebox}), & \pi_{12} &= (\textit{onebox}, \textit{twobox}), \\
\pi_{21} &= (\textit{twobox}, \textit{onebox}), & \pi_{22} &= (\textit{twobox}, \textit{twobox}).
\end{aligned}$$

In the P-FDT dependency graph $G^{\text{PFDT}}$, there is a single rectangular intervention node $\textsc{pfdt}(\underline{P}, \underline{G})$ with arrows pointing to $\textsc{Prediction}$ and $\textsc{Act}$:

```
                  [ pfdt(P, G) ]        ( Accurate )
                    /        \               /
                   /          \             v
                  /         ( Prediction )
                 /               |      \
                v                v       v
             ( Act ) <------ ( Obs )  ( Box B )
                 \                       /
                  \-----> < V > <-------/
```

The structural equations of $G^{\text{PFDT}}$ and prior $P$ are:
* $P(\textsc{Accurate} = \textit{accurate}) = 0.99$ and $P(\textsc{Accurate} = \textit{inaccurate}) = 0.01$.
* The predictor predicts the policy's output on input $\textit{full}$:
  $$\textsc{Prediction}(\pi, \textit{accurate}) = \begin{cases} 1 & \text{if } \pi(\textit{full}) = \textit{onebox}, \\ 2 & \text{if } \pi(\textit{full}) = \textit{twobox}, \end{cases}$$
  and the reverse when $\textsc{Accurate} = \textit{inaccurate}$.
* $\textsc{Box B}(1) = \textit{full}$, $\textsc{Box B}(2) = \textit{empty}$, and $\textsc{Obs} = \textsc{Box B}$.
* $\textsc{Act}(\pi, \textsc{Obs}) = \pi(\textsc{Obs})$.
* $V(\textit{onebox}, \textit{full}) = \$1,000,000$, $V(\textit{twobox}, \textit{full}) = \$1,001,000$, $V(\textit{onebox}, \textit{empty}) = \$0$, and $V(\textit{twobox}, \textit{empty}) = \$1,000$.

Let us apply Equation (6) by computing $\mathbb{E}[V \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)]$ for each of the four policies:

1. **For $\pi_{11} = (\textit{onebox}, \textit{onebox})$:** Since $\pi_{11}(\textit{full}) = \textit{onebox}$, with probability $0.99$ the predictor predicts $1$, $\textsc{Box B} = \textit{full}$, the agent observes $\textit{full}$ and takes $\pi_{11}(\textit{full}) = \textit{onebox}$, receiving $\$1,000,000$. With probability $0.01$, $\textsc{Box B} = \textit{empty}$, and the agent takes $\pi_{11}(\textit{empty}) = \textit{onebox}$, receiving $\$0$.
   $$\mathbb{E}\left[V \;\middle|\; \mathtt{do}\big(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{11}\big)\right] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000.$$

2. **For $\pi_{12} = (\textit{onebox}, \textit{twobox})$:** With probability $0.99$, $\textsc{Box B} = \textit{full}$ and $\pi_{12}(\textit{full}) = \textit{onebox}$ yields $\$1,000,000$. With probability $0.01$, $\textsc{Box B} = \textit{empty}$ and $\pi_{12}(\textit{empty}) = \textit{twobox}$ yields $\$1,000$.
   $$\mathbb{E}\left[V \;\middle|\; \mathtt{do}\big(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{12}\big)\right] = 0.99(\$1,000,000) + 0.01(\$1,000) = \$990,010.$$

3. **For $\pi_{21} = (\textit{twobox}, \textit{onebox})$:** Since $\pi_{21}(\textit{full}) = \textit{twobox}$, with probability $0.99$ the predictor predicts $2$ ($\textsc{Box B} = \textit{empty}$) and only with probability $0.01$ is $\textsc{Box B} = \textit{full}$. Thus:
   $$\mathbb{E}\left[V \;\middle|\; \mathtt{do}\big(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{21}\big)\right] = 0.01(\$1,001,000) + 0.99(\$0) = \$10,010.$$

4. **For $\pi_{22} = (\textit{twobox}, \textit{twobox})$:** With probability $0.01$, $\textsc{Box B} = \textit{full}$ and two-boxing yields $\$1,001,000$; with probability $0.99$, $\textsc{Box B} = \textit{empty}$ and two-boxing yields $\$1,000$:
   $$\mathbb{E}\left[V \;\middle|\; \mathtt{do}\big(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{22}\big)\right] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$

Comparing the four values, $\pi^* = \pi_{12} = (\textit{onebox}, \textit{twobox})$ is the unique global maximizer, achieving $\$990,010$. Finally, applying Stage 2 (Equation 7) to the actual observation $x = \textit{full}$, the P-FDT agent executes:

$$\mathrm{PFDT}(P, G, \textit{full}) = \pi_{12}(\textit{full}) = \textit{onebox}.$$

Notice how clean this is compared to A-FDT. In P-FDT, the agent never needs a prior probability $q$ over what she would do at counterfactual observation nodes, because the policy intervention $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$ sets her actions across *all* observation branches simultaneously. Exactly the same policy-level reasoning applies to the **Mechanical Blackmail Problem** (Dilemma 8): P-FDT evaluates policies mapping $\{\textit{blackmail}, \emptyset\}$ to $\{\textit{pay}, \textit{refuse}, \textit{noop}\}$, finds that the policy of refusing upon observing $\textit{blackmail}$ maximizes expected utility by deterring the blackmailer from running the program, and applies that policy to output $\textit{refuse}$.

---

## 4. Where P-FDT Diverges from A-FDT: Multi-Agent Dilemmas with Asymmetric Observations

Why did Yudkowsky and Soares remark in Footnotes 7 and 16 that the distinction between iterating over policies (**P-FDT**) and iterating over actions (**A-FDT**) *"makes a difference in certain multi-agent dilemmas"*? (Note: the source paper states this claim without providing an example; the formal analysis and dilemma below are our own development to explain and prove their claim.)

In the **Psychological Twin Prisoner's Dilemma** (Dilemma 1 of the source paper), both twins receive the exact same observation (none, or $\emptyset$). Consequently, in A-FDT, both twins' actions depend on the *same* node $\textsc{fdt}(\underline{P}, \underline{G}, \emptyset)$, so A-FDT and P-FDT coincide.

Suppose, however, that two copies or psychological twins running the same decision algorithm wake up in **different** environments and therefore receive **different observations** $x_1 \neq x_2$ (for example, one wakes up in a Red room and the other wakes up in a Blue room, or each receives a different local sensor reading). 

Look at what happens to the causal/subjunctive graph in **A-FDT** versus **P-FDT**:
* In **A-FDT**, the agent who observes $\textit{red}$ intervenes *only* on the node $\textsc{fdt}(\underline{P}, \underline{G}, \textit{red})$. Her twin in the Blue room is governed by a *different* node, $\textsc{fdt}(\underline{P}, \underline{G}, \textit{blue})$. Because $\textsc{fdt}(\underline{P}, \underline{G}, \textit{blue})$ is not downstream of $\textsc{fdt}(\underline{P}, \underline{G}, \textit{red})$, the surgical intervention $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \textit{red}) = a)$ leaves $\textsc{fdt}(\underline{P}, \underline{G}, \textit{blue})$ untouched at whatever prior distribution $P$ assigns to it!
* In **P-FDT**, both twins' actions are governed by the *same* policy node $\textsc{pfdt}(\underline{P}, \underline{G})$: the Red-room twin executes $\pi(\textit{red})$ and the Blue-room twin executes $\pi(\textit{blue})$. Intervening on $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$ coordinates both twins across their distinct observations simultaneously.

As a result, A-FDT and P-FDT diverge sharply in multi-agent dilemmas with asymmetric observations whenever either (a) the payoff structure has cross-branch synergy (so that the optimal action at observation $x_1$ depends on the twin's action at observation $x_2$), or (b) the observations carry asymmetric probabilities or payoffs across agents. Let us demonstrate both mechanisms with concrete mathematical examples.

### 4.1 Example 1: The Two-Room Twin Vault Dilemma (Cross-Branch Synergy)

Consider the following multi-agent dilemma:

> **Dilemma (The Two-Room Twin Vault Dilemma).** An agent and her psychological twin are placed in separate rooms—one painted Red ($\textit{red}$) and one painted Blue ($\textit{blue}$)—with a $50/50$ prior chance of which twin is placed in which room. Each twin can either **Cooperate** ($C$) by paying $\$1,000$ to turn a heavy key in her room, or **Defect** ($D$) by keeping her $\$1,000$ and doing nothing. A central vault containing $\$1,000,000$ for *each* twin unlocks **if and only if both keys are turned** (i.e., both the twin in the Red room and the twin in the Blue room choose $C$). Adding $\$1,000$ as baseline endowment, a twin's personal utility $V$ as a function of $(\textsc{Act}_{\text{self}}, \textsc{Act}_{\text{twin}})$ is:
> * $V(C, C) = \$1,000,000$,
> * $V(C, D) = \$0$,
> * $V(D, C) = \$1,000$,
> * $V(D, D) = \$1,000$.
>
> You wake up, observe that your room is Red ($\textsc{Obs}_{\text{self}} = \textit{red}$, which implies $\textsc{Obs}_{\text{twin}} = \textit{blue}$), and must choose $C$ or $D$.

#### Evaluation under A-FDT: Vulnerability to Prior Paralysis
In A-FDT, there are two separate decision nodes: $a_{\textit{red}} \coloneqq \textsc{fdt}(\underline{P}, \underline{G}, \textit{red})$ and $a_{\textit{blue}} \coloneqq \textsc{fdt}(\underline{P}, \underline{G}, \textit{blue})$. In the prior $P$ (before knowing which room is which), with probability $0.5$ the deciding agent is in the Red room ($\textsc{Act}_{\text{self}} = a_{\textit{red}}, \textsc{Act}_{\text{twin}} = a_{\textit{blue}}$) and with probability $0.5$ she is in the Blue room ($\textsc{Act}_{\text{self}} = a_{\textit{blue}}, \textsc{Act}_{\text{twin}} = a_{\textit{red}}$).

When the agent in the Red room runs $\mathrm{AFDT}(P, G, \textit{red})$, she intervenes *only* on $a_{\textit{red}}$, holding $a_{\textit{blue}}$ at its prior probability $q \coloneqq P(a_{\textit{blue}} = C)$. Her expected utility under each intervention is:

$$\begin{aligned}
\mathbb{E}\left[V \;\middle|\; \mathtt{do}(a_{\textit{red}} = C)\right] &= q \cdot \$1,000,000 + (1-q) \left[\frac{1}{2}(\$0) + \frac{1}{2}(\$1,000)\right] = \$1,000,000q + \$500(1-q), \\
\mathbb{E}\left[V \;\middle|\; \mathtt{do}(a_{\textit{red}} = D)\right] &= q \left[\frac{1}{2}(\$1,000) + \frac{1}{2}(\$0)\right] + (1-q) \cdot \$1,000 = \$500q + \$1,000(1-q).
\end{aligned}$$

Notice that if $q < \frac{500}{1,000,000} = 0.0005$—in particular, if the agent has a skeptical prior $q = 0$ that the Blue-room decision node will output $C$—then

$$\mathbb{E}\left[V \;\middle|\; \mathtt{do}(a_{\textit{red}} = D)\right] = \$1,000 > \$500 = \mathbb{E}\left[V \;\middle|\; \mathtt{do}(a_{\textit{red}} = C)\right].$$

Thus $\mathrm{AFDT}(P, G, \textit{red}) = D$, and by identical reasoning $\mathrm{AFDT}(P, G, \textit{blue}) = D$. Worse still, $(a_{\textit{red}}, a_{\textit{blue}}) = (D, D)$ is *reflectively stable* under A-FDT: if both twins know that A-FDT outputs $D$ in both rooms, then $q = 0$ is true, which makes outputting $D$ strictly optimal under A-FDT's single-node intervention! A-FDT falls into the exact same prior-dependent trap that Yudkowsky and Soares criticize EDT for in Section 6.

#### Evaluation under P-FDT: Guaranteed Coordination
Now evaluate the same dilemma under **P-FDT**. Here $\mathcal{X} = \{\textit{red}, \textit{blue}\}$, $\mathcal{A} = \{C, D\}$, and $\Pi = \{\pi_{CC}, \pi_{CD}, \pi_{DC}, \pi_{DD}\}$, where $\pi_{ab}(\textit{red}) = a$ and $\pi_{ab}(\textit{blue}) = b$. Under $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{ab})$, the Red-room twin's action is set to $a$ and the Blue-room twin's action is *simultaneously* set to $b$. Regardless of any prior beliefs $P$ might hold about the decision node, Equation (6) yields:

$$\begin{aligned}
\mathbb{E}\left[V \;\middle|\; \mathtt{do}\big(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{CC}\big)\right] &= \$1,000,000, \\
\mathbb{E}\left[V \;\middle|\; \mathtt{do}\big(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{CD}\big)\right] &= \frac{1}{2}(\$0) + \frac{1}{2}(\$1,000) = \$500, \\
\mathbb{E}\left[V \;\middle|\; \mathtt{do}\big(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{DC}\big)\right] &= \frac{1}{2}(\$1,000) + \frac{1}{2}(\$0) = \$500, \\
\mathbb{E}\left[V \;\middle|\; \mathtt{do}\big(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{DD}\big)\right] &= \$1,000.
\end{aligned}$$

The policy $\pi^* = \pi_{CC}$ is the unique global maximizer independently of any prior $q$. Applying $\pi_{CC}$ to her observation $\textit{red}$, the P-FDT agent outputs $\pi_{CC}(\textit{red}) = C$, her twin outputs $\pi_{CC}(\textit{blue}) = C$, and both walk away with $\$1,000,000$.

### 4.2 Example 2: Asymmetric Division of Labor Between Twins

P-FDT also solves multi-agent dilemmas where two twins receiving different observations must take *complementary* actions, or where one observation branch must bear a cost to benefit the other. Suppose that in the Two-Room Twin Dilemma, the vault opens (paying $\$1,000,000$ to each twin) if and only if the twin in the **Red** room pulls the Left lever ($L$, which costs $\$5,000$ in radiation exposure in the Red room) and the twin in the **Blue** room pulls the Right lever ($R$, which costs $\$0$ in the Blue room), whereas pulling $R$ in the Red room costs $\$0$ and locks the vault.

Even if a single agent has a $50/50$ pre-observation prior over being assigned to the Red room or the Blue room, look at what happens if the two rooms have asymmetric observation spaces or if A-FDT evaluates an agent whose prior $P$ already assigns a high probability (say $0.999$) to her being the copy placed in the Red room (for instance, because she is the original earthly agent and her twin is a backup copy created on a space station only in $1\%$ of worlds, or because her model $P$ conditions on background indexical facts). If $P(\textsc{Obs}_{\text{self}} = \textit{red}) = 0.999$ and $P(\textsc{Obs}_{\text{twin}} = \textit{blue}) = 0.999$, then in A-FDT, intervening on $\textsc{fdt}(\underline{P}, \underline{G}, \textit{red})$ changes *only* the Red-room action without changing the Blue-room action. By contrast, in P-FDT under a shared pre-observation prior $P$, the policy $\pi^*(\textit{red}) = L, \pi^*(\textit{blue}) = R$ gives expected utility $\frac{1}{2}(\$995,000) + \frac{1}{2}(\$1,000,000) = \$997,500$, dominating all other policies and enabling seamless division of labor across states.

---

## 5. Open Questions in the Source and Operational Extensions for P-FDT

Because Yudkowsky and Soares (2017) relegate **P-FDT** to Footnotes 7 and 16, several important mathematical and philosophical questions are left unresolved by the source text. To make P-FDT fully operational for unfamiliar decision problems, we now identify three core uncertainties in the source and develop precise mathematical proposals to resolve them.

### 5.1 Uncertainty 1: What Is the Domain of a Policy—Observations $\mathcal{X}$ or Full Inputs $(\mathcal{M} \times \mathcal{X})$?

Compare the wording of the two footnotes in Yudkowsky and Soares (2017):
* **Footnote 7** defines policies as *"mappings from observations to actions"* ($\pi : \mathcal{X} \to \mathcal{A}$).
* **Footnote 16** states that the algorithm *"intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action."*

In Section 5 of the source paper, the inputs to the decision function $\mathrm{FDT}$ are not just the observation $x$, but the full triple $(P, G, x)$ (or $(M, x)$, where $M = (P, G)$ is the agent's world-model). Does a P-FDT policy map only observations $x \in \mathcal{X}$ to actions (as in Footnote 7 and our Section 2.2), or does it map the entire input tuple $(P, G, x)$ to actions (as suggested by Footnote 16's notation $\mathrm{FDT}(-)$)?

**Why this matters:** Consider the **Smoking Lesion Problem** as formalized in Section 6 of Yudkowsky and Soares (2017). There, the agent makes no runtime sensory observation ($\mathcal{X} = \{\emptyset\}$). Instead, the lesion alters the agent's preferences, determining whether her world-model is $(P_S^F, G^F)$ (which values smoking at $+\$1,000$ via $\mathcal{U}_S$) or $(P_R^F, G^F)$ (which values smoking at $-\$1$ via $\mathcal{U}_R$). Because Fiona does not have introspective access to which world-model she is running, her graph $G^F$ (Figure 4 in the source paper) contains two nodes: $\textsc{fdt}(\underline{P}_S^F, \underline{G}^F)$ and $\textsc{fdt}(\underline{P}_R^F, \underline{G}^F)$. If a policy only maps sensory observations $x \in \mathcal{X}$ to actions while the intervened node remains parameterized by $(\underline{P}, \underline{G})$, then $\textsc{pfdt}(\underline{P}_S^F, \underline{G}^F)$ and $\textsc{pfdt}(\underline{P}_R^F, \underline{G}^F)$ are still two separate nodes!

**Proposed Operational Resolution:** We propose distinguishing between *fixed-model problems* and *model-uncertainty problems*. Whenever the agent's world-model $(P, G)$ is common knowledge among all copies/predictors of the agent, taking $\Pi = \mathcal{A}^{\mathcal{X}}$ with intervention node $\textsc{pfdt}(\underline{P}, \underline{G})$ (Equations 6–7) is equivalent to the full-input formulation and avoids iterating over the intractably vast space of all functions on $\mathcal{M} \times \mathcal{X}$. When the agent faces uncertainty among a finite family of possible internal models or utility functions $\mathcal{M}_0 = \{M_1, \dots, M_k\}$ (as in the smoking lesion problem or Bayesian games with private preference types), we operationalize Footnote 16's $\mathrm{FDT}(-)$ by treating the agent's internal model index $m \in \{1, \dots, k\}$ as part of her effective input $(m, x) \in \{1, \dots, k\} \times \mathcal{X}$. Wait—there is a crucial catch! In the smoking lesion problem, if an agent with preference $\mathcal{U}_S$ chose the policy for *both* $M_S$ and $M_R$ using only $\mathcal{U}_S$, she would evaluate the $M_R$ branch using $\mathcal{U}_S$ (which likes smoking) rather than $\mathcal{U}_R$ (which dislikes smoking). Therefore, if $(P, G)$ is fixed as the parameter of $\textsc{pfdt}(\underline{P}, \underline{G})$ and policies map *observations* $\mathcal{X} \to \mathcal{A}$ (Footnote 7), each preference type $M_S$ and $M_R$ rightly optimizes its own policy node $\textsc{pfdt}(\underline{P}_S^F, \underline{G}^F)$ and $\textsc{pfdt}(\underline{P}_R^F, \underline{G}^F)$ according to its own utility function! For this reason, Footnote 7's definition ($\Pi = \mathcal{A}^{\mathcal{X}}$, intervening on $\textsc{pfdt}(\underline{P}, \underline{G})$) is actually more robust across preference-varying dilemmas than an unrestricted universal node $\mathrm{FDT}(-)$, unless utility is evaluated state-dependently via $\mathcal{U}_{\
````

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Project Scope**

I'm now zeroing in on the project's parameters. It's becoming clearer that the focus is on crafting a 2,400-3,000 word technical piece explaining Policy Functional Decision Theory from a researcher's perspective. The goal is to make it easy for the reader to apply the theory.


**Pinpointing Source Material**

I've homed in on the core source: Yudkowsky & Soares (2017). My immediate task involves thoroughly digesting footnote 16 (and its related footnote 7) within the paper, as that passage is the foundational element for P-FDT. I'm focusing on the mathematical formalization of policy iteration, and it seems this method is preferred over action iteration.


**Clarifying Theory Nomenclature**

Now I'm making sure to consistently label this specific policy selection theory as P-FDT. I need to be exact with names, clearly differentiating it from EDT, CDT, and other theories. This means incorporating mathematical definitions, equations, and specific examples. Also I need to explain how P-FDT works when evaluating actions and dependencies. The focus is to make it precise enough to apply to novel scenarios.


**Interpreting Source Material**

I'm now focusing on filling the gaps and clarifying ambiguities in the original footnote. I'm actively working to clearly differentiate the source's claims from my own interpretations. Maintaining verbatim quotations is paramount to ensure accuracy, and I'm sticking to the target word count. I'll omit unnecessary repetition, extensive bibliographies, and appendices to keep the piece concise, ending with a clear conclusion.


**Analyzing P-FDT Formula**

I'm currently dissecting the P-FDT formula and the implications of its structure. The key is in how observations, x, are handled within the policy. I noticed the lack of conditioning on observations, as well as the important nuance from Footnote 7 about iterating over policies. I need to make sure this is clearly communicated in the writing.


**Formalizing P-FDT**

I'm working to formalize P-FDT using mathematical notation. I'm focusing on defining the sets of observations, actions, and policies. I'm noting the crucial difference where P-FDT intervenes on a policy, rather than directly on an action. I'm also ensuring the notation clearly represents how policies map inputs to actions. I'm thinking how this relates to multi-agent dilemmas.


**Clarifying Agent Action**

I'm now zeroing in on defining the agent's action within P-FDT. I am working on how to precisely represent the policy output from the policy-selection function. My focus is understanding how the agent's action maps inputs to actions. I'm investigating the potential discrepancies in the source material related to inputs versus observations.


**Distinguishing Agent Actions**

I'm now diving into the precise definition of the agent's action, working through two possible interpretations of the policy's input. One sees the input as just the observation history, the other as the entire tuple including the model. I need to operationalize these ideas clearly, differentiating my explanations from the source material. I'll also check the mathematics to compare P-FDT with Action-FDT.


**Comparing FDT Paradigms**

I'm now carefully contrasting P-FDT and Action-FDT (A-FDT). I see that A-FDT intervenes on a single observation, while P-FDT fixes counterfactual behavior across all observations simultaneously. I need to figure out if P-FDT and A-FDT are equivalent in single-agent scenarios, specifically in situations where the predictor focuses on a single observation branch.


**Examining the Equivalence**

I'm now deeply examining the potential equivalence of P-FDT and A-FDT in single-agent scenarios, especially considering predictor dependencies. I'm focusing on the case with inaccurate priors, and it seems this may lead to divergent outcomes. This has me reconsidering whether the two are ever truly identical, and the implications of this.


**Investigating Asymmetric Dilemmas**

I'm now focusing on the implications of asymmetric observations in multi-agent dilemmas for P-FDT. Specifically, I'm analyzing a Twin Prisoner's Dilemma scenario where agents have different observations. The key is in why Yudkowsky & Soares highlighted this as important in footnotes 7 and 16. The policy optimization approach handles the differences.


**Analyzing Dilemma Outcomes**

I'm now analyzing a Twin Prisoner's Dilemma, focusing on how P-FDT and A-FDT handle differing observations. A-FDT's single-node intervention allows for defection, similar to CDT. However, with P-FDT, the policy-based intervention ensures cooperative outcomes, as it considers the policy's effects across all observations, including my twin's.


**Testing Dilemma Scenarios**

I'm now focusing on a Red/Blue Twin Prisoner's Dilemma, carefully testing how P-FDT evaluates policies, particularly from an *ex ante* perspective. My attention is on the implications where a fair coin determines the initial observation state. I'm exploring the implications of asymmetric observations, policy selection, and payoff structures for cooperative vs. defective outcomes.


**Evaluating Policy Effectiveness**

I'm now focusing on a Red/Blue Twin Prisoner's Dilemma, and have worked through how P-FDT evaluates policies from an *ex ante* perspective. I've considered the implications of asymmetric observations, policy selection, and payoffs. It's clear that policy optimization under P-FDT leads to a unique, cooperative outcome, even under asymmetric observations, in a way that differs from A-FDT.


**Analyzing Action Dynamics**

I'm now deep-diving into the mathematical implications of action within the Red/Blue Twin Prisoner's Dilemma. I'm focusing on two scenarios: 1) where I know I am Player 1, seeing red, and my twin is Player 2, seeing blue; and 2) where our shared P-FDT algorithm, or the observation, tells me which player I am. This analysis may yield deep insights.


**Tracing Observation Differences**

I'm now tracing the nuances of how P-FDT handles differing observations, focusing on Yudkowsky & Soares' (2017) framework. Specifically, I'm examining scenarios where the agent's prior world-model, *P*, is combined with the runtime observation, *x*. I'm thinking about cases where *P* distinguishes different observers via $\textsc{Obs}_1$ and $\textsc{Obs}_2$. For instance, I'm exploring an example where $\textsc{Obs}_1$ is $\textit{red}$, where I make my action $\textsc{Act}_1$ depend on an *fdt* calculation.



**Examining Twin Scenarios**

I'm now diving into the implications of using P-FDT in the same model where I am on Earth and my twin is on Mars. My utility hinges on the actions of both, even if my observations are limited. The challenge lies in how both of us compute the optimal policy. The crux is figuring out the impact of intervening on the policy.


**Clarifying Earth-Mars Scenario**

I'm now zeroing in on an Earth-Mars Twin Prisoner's Dilemma, aiming to clarify why a policy $\pi(\textit{earth}) = D, \pi(\textit{mars}) = C$ maximizes my value. The prior's structure determines this outcome: each twin runs the same decision function $\mathrm{PFDT}(P, G, x)$. I'm considering scenarios with a pre-observation prior or a symmetric prior over identity. I'm exploring the nuances when $P$ and $G$ are identical, but twins get different observations.


**Modeling Noisy Observations**

I'm now modeling a scenario with independent, noisy observations in a Twin Prisoner's Dilemma, focusing on Action-FDT (A-FDT). It involves two twins with identical priors but different, independent weather readings. I'm noting the probability that my twin's action, controlled by their individual A-FDT evaluation, is not set to the same state.

I am analyzing the scenario when the prior state is noisy as well.


**Calculating Expected Utility**

I'm now calculating the expected utility in the noisy observation A-FDT scenario. I'm focusing on the probability of matching observations. When observations don't match (probability $1 - \epsilon$), the action remains independent of $\textsc{fdt}(\underline{P}, \underline{G}, x)$.


**Analyzing Asymmetric Action**

I'm now analyzing an A-FDT Twin Prisoner's Dilemma with asymmetric observation probabilities, where my twin and I receive different weather readings. With different observation probabilities, the term for asymmetric payoffs becomes key: in asymmetric scenarios, my action affects only my payoff, while my twin's action affects the payoff of both twins! This raises new questions.


**Modeling Asymmetric Actions**

I'm now modeling a coordination/division-of-labor game where each twin observes either "left" or "right", needing to pull corresponding levers for the win. I'm calculating the P-FDT policy selection.


**Modeling Coordination Strategies**

I'm now carefully calculating P-FDT policy selection for a coordination game where twins observe "left" or "right" and must pull corresponding levers. The challenge is ensuring the actions satisfy cross-branch constraints for a win, like $\pi(\textit{left}) \neq \pi(\textit{right})$. I'm also modeling how A-FDT handles this.



**Modeling Coordination Challenges**

I'm now carefully calculating P-FDT policy selection for a coordination game where twins observe "left" or "right" and must pull corresponding levers. My focus is on how to satisfy constraints for a win, like $\pi(\textit{left}) \neq \pi(\textit{right})$. I'm also modeling how A-FDT handles this scenario.

I'm realizing that with A-FDT, even with uncertain priors in a Stag Hunt scenario, I'm held fixed at the prior distribution, causing the sub-optimal outcome.


**Revising Dilemma Logic**

I'm revisiting the Twin Prisoner's Dilemma logic under A-FDT with distinct observations, specifically rooms A and B. It now seems that Player 1, observing A, can only control their action based on their observation, and likewise Player 2, observing B, only controls their action. It appears that actions are not correlated.



**Refining Prisoner's Dilemma Analysis**

I'm now refining the Twin Prisoner's Dilemma analysis under Action-FDT (A-FDT) with distinct observations. The key is that Player 1, observing A, only controls their action based on that observation, while Player 2, observing B, only controls their action based on their own. This causes the actions to be uncorrelated.



**Modeling Stag Hunt Outcomes**

I'm now modeling a Stag Hunt scenario between two rooms, A and B, using Action-FDT (A-FDT). My focus is on the impact of my decision in one room on the outcome in the other. I've realized that in A-FDT, intervening on one room doesn't influence the outcome in the other, leading to suboptimal Stag Hunt outcomes. The two agents are independent from each other.



**Modeling Stag Hunt Differences**

I'm now carefully examining the Stag Hunt scenario using both Action-FDT (A-FDT) and Policy-FDT (P-FDT). My focus is on understanding how P-FDT resolves the Stag Hunt in a manner that contrasts with A-FDT. I'm exploring the implications for optimal outcomes. The differences are key to how the theory works.

I now understand how in P-FDT, the single intervention simultaneously sets the actions to always Stag or always Hare. If the prior probability of Stag is low, then the A-FDT agent, similar to EDT and CDT, can easily get trapped.


**Modeling Stag Hunt Differences**

I'm now carefully examining the Stag Hunt scenario using both A-FDT and P-FDT. I'm focusing on how P-FDT resolves the Stag Hunt in contrast to A-FDT. I've realized that the P-FDT single intervention allows simultaneous assignment of actions to always Stag or always Hare. In A-FDT, the agent can get trapped. This highlights how the theories differ.



**Examining Utility in Dilemmas**

I'm currently focused on evaluating agent utility within various dilemmas. In a scenario with shared $(P, G)$, but differing observations, the utility $V$ is evaluated from a specific perspective, but with shared utilities. I need to clarify how the agents compute the optimal policy within this framework.


**Clarifying Policy Computation**

I'm now clarifying how P-FDT policy computation works with shared priors but differing observations. I'm focusing on scenarios like the Twin Prisoner's Dilemma, examining how each agent's utility is determined, even with differing inputs. The goal is a precise model of optimal policy selection.

I'm analyzing the differences in action with A-FDT.


**Refining A-FDT Utility**

I'm now carefully analyzing agent utility within dilemmas under both A-FDT and P-FDT frameworks, given shared priors with differing observations. I'm clarifying how agents compute optimal policies and their differing action sets. Under A-FDT the actions are no longer correlated.


**Evaluating A-FDT Utility**

I'm now calculating the expected utility of intervening on a single node $\mathtt{do}(\textsc{fdt}(\underline{P}^F, \underline{G}^F, x) = a)$ in A-FDT. I'm focusing on a Prisoner's Dilemma, assigning costs and benefits to cooperation. I'm evaluating the outcomes when my and my twin's observations are independent and identically distributed.


**Revising A-FDT Utility**

I'm now revising my utility calculations for A-FDT in the Prisoner's Dilemma, focusing on scenarios where my observation probability, $P(\textsc{Obs}_{\text{me}} = x)$, differs from my twin's, $P(\textsc{Obs}_{\text{twin}} = x)$. This variance might stem from asymmetric roles or differing priors related to who is "me" in the utility calculation. I will investigate how this affects the expected values in this model.



**Revising A-FDT Utility**

I'm now diving into analyzing how utility is optimized in an asymmetric setting where room probabilities for agents vary: Agent 1 is in Room 1 with probability 0.99, and Agent 2 is in Room 2 with probability 0.99. Even small swaps, say 0.0001, in A-FDT causes Agent 1 to defect. But I need to revisit P-FDT to understand how Agent 1's $V_1$ computation of the optimal $\pi$ policy plays out in this case.


**Refining Asymmetric Dilemmas**

I'm now focusing on the implications of asymmetric observation probabilities on the optimal policy. The problem is if the priors differ, the utilities will differ too, and the P-FDT policy selection will be different. This makes me realize the importance of the initial prior structure and how to model asymmetric room probabilities to generate equivalent outcomes with differing $V$!



**Diverging Game Paradigms**

I'm now carefully exploring scenarios where A-FDT and P-FDT diverge in multi-agent dilemmas, focusing on symmetric priors and differing observations. I'm especially interested in games where my payoff in room A depends on my twin's action in room B. A Prisoner's Dilemma with additive payoffs becomes important in my exploration.


**Verifying Dilemma Dynamics**

I'm now diving into the implications of non-additive payoffs in multi-agent scenarios like the Joint Project/Threshold Prisoner's Dilemma. I'm focusing on the dependency between twin actions and how P-FDT policy choices are impacted. I'm verifying the claim that the optimal policy in room A depends on the policy in room B with mathematical analysis.


**Evaluating Dilemma Strategies**

I'm now carefully evaluating how A-FDT and P-FDT strategies play out in a Joint Project/Threshold Prisoner's Dilemma, and have a more nuanced view of payoffs. A-FDT intervenes solely on an observed node, while the P-FDT policy choices in each room are inter-related. I need to figure out why in A-FDT the cooperation strategy is suboptimal.


**Revising A-FDT Utility**

I'm now carefully revisiting the utility evaluations in the Joint Project/Threshold Prisoner's Dilemma under A-FDT. I've realized that the probability of the twin cooperating is key. Because the intervention on my action doesn't influence the twin's, and as the prior cooperative probability decreases, defection is the more rational choice. I'm clarifying why P-FDT provides a cooperative outcome, whereas A-FDT is always a trap.


**Clarifying Cooperation Paradigms**

I'm working to clarify the different outcomes in a joint protocol scenario. A-FDT agents are influenced by their priors, leading to potentially suboptimal outcomes, such as defection. In contrast, P-FDT offers a robust cooperative solution, which highlights the critical advantage of P-FDT in coordination dilemmas with asymmetric options.


**Constructing Key Examples**

I'm now crafting a game where A-FDT predictably fails, while P-FDT guarantees a good outcome, even with perfect self-knowledge. This focuses on the math of a Stag Hunt scenario where A-FDT struggles because it relies on the prior probabilities, leading to suboptimal outcomes, such as Hare. Meanwhile, P-FDT consistently delivers a cooperative equilibrium.


**Analyzing Coordinate Optimality**

I'm now zeroing in on why coordinate-wise maximization can lead to suboptimal outcomes in A-FDT. I am clarifying how strict local maxima, such as (Hare, Hare) in the Stag Hunt, become reflective fixed points within a single updateless agent. I'm focusing on the mathematical formalization of these limitations.


**Clarifying Dilemma Dynamics**

I'm now clarifying the nature of multi-agent dilemmas where agents have distinct utility functions but employ the same decision function. I'm focusing on scenarios with differing priors over being Agent 1 or 2, highlighting how Agent 1 maximizes their own $V_1$. It is this divergence which creates the unique properties in policy selection.


**Refining Cooperative Strategies**

I'm now carefully analyzing why cooperative strategies emerge in Dilemma 1. The key lies in understanding that Agent 1, with the goal of maximizing their own personal payout, and Agent 2, with the same objective, share the same model structure and receive identical observations. This convergence leads to cooperative outcomes. I need to examine what happens if the observations differ.


**Calculating Observation Scenarios**

I'm now calculating what happens if my twin and I have the same model, but receive distinct room observations, such as Red and Blue. I'm focusing on the implications of each agent's personal utility in this situation. It seems each agent's models are initially symmetric, reflecting an equal probability of either color.


**Calculating Asymmetric Observations**

I'm now investigating Action-FDT (A-FDT) dynamics with asymmetric observations. Specifically, I'm analyzing a scenario where observations are (red, blue) or (blue, red), each occurring with probability 0.5. I've noted that under A-FDT, the agent's action doesn't condition on their specific observation, but rather directly intervenes on the node, while holding the other fixed.


**Calculating Asymmetric Payoffs**

I'm now calculating the payoffs in a "Vault Twin Prisoner's Dilemma" with asymmetric scenarios where one action yields $\$2,000$ to the other twin. In this scenario, unlocking a vault (yielding $\$1,000,000$ to both) requires *both* twins to cooperate; defection costs zero effort. I'm noting the differing payoffs for each room in this case.



**Modeling Asymmetric Payoffs**

I'm now calculating the payoffs for a vault-unlocking Twin Prisoner's Dilemma, focusing on the scenario when the twins' actions depend on their observations. I'm noting the differing payoffs for each room in this case, specifically modeling the payoff matrix as a function of the actions of the two agents.


**Modeling Asymmetric Actions**

I'm now carefully examining the expected utilities in the "Vault Twin Prisoner's Dilemma". I am calculating the expected outcomes when one twin observes Red and the other Blue, and when their actions influence the $\$1,000,000$ payout for both or the personal $\$1,000$ for one. The P-FDT policy intervention yields cooperation, while A-FDT leads to defection.


**Refining Equilibrium Strategies**

I'm now zeroing in on a red/blue scenario where P-FDT yields a unique cooperative outcome, unlike A-FDT. I've realized that in A-FDT, even with a strong prior for cooperation, defection can be a self-consistent equilibrium. A-FDT action is independent of the other agent's. The key is to formulate payoffs in a way that A-FDT is trapped in (D, D), while P-FDT produces (C, C). I'm modeling $f(a_{\textit{red}}, a_{\textit{blue}})$ in the new model.


**Analyzing Equilibrium Criteria**

I'm now focusing on a key insight: coordinate-wise maximization can be suboptimal. I've realized that if both actions maximize the *same* function, then the global maximum is a Nash equilibrium. This implies that even if this does not result in the coordinate-wise maxima as a result, A-FDT can still be useful.



**Refining Policy Dynamics**

I'm now carefully examining the implications when a third party's actions depend on the algorithm $\pi$ or when dealing with sequential decisions across observations. Also I'm checking what happens in A-FDT when the agent is uncertain about algorithm output. The paper's Section 6 has a lot of relevant material.


**Examining Decision Independence**

I'm now carefully examining the Transparent Newcomb problem, specifically Section 6 of Yudkowsky & Soares (2017). I've noted that in the single-agent cases, the decision at the observed node doesn't depend on the prior probability *q* about actions at the unobserved node. This is a crucial distinction.


**Analyzing Multi-Agent Dilemmas**

I'm now zeroing in on multi-agent dilemmas where the observed branch's outcome depends on actions across all branches.  In A-FDT, Fiona's computation for $\textsc{fdt}(\underline{P}^F, \underline{G}^F, x)$ needs priors $q$ about other scenarios $x'$. With multiple fixed points, like in the Twin Stag Hunt, A-FDT requires external ratification and can fail to coordinate.


**Examining A-FDT Failures**

I'm now investigating scenarios where A-FDT fails, even when agents can compute fixed points. I'm focusing on multi-agent dilemmas where the predictor models a policy, or agents have asymmetric information/observations. I am checking if updating $P$ based on observations or using two P-FDT agents with differing observations can help. This extends to comparing outcomes in an Asymmetric-Information Twin Prisoner's Dilemma.


**Modeling Asymmetric Payoffs**

I'm now carefully modeling the Asymmetric-Cost Twin Prisoner's Dilemma as a Bayesian game. This requires establishing a payoff matrix that accurately reflects the scenarios: each twin's cost of cooperating is either low (small) or high (large), with independent probabilities, as each twin sees a distinct payoff structure. The critical task is evaluating the outcomes with different combinations of actions and costs.


**Refining Cost Strategies**

I'm now refining calculations for an asymmetric cost Prisoner's Dilemma, considering high/low cooperation costs. I've realized P-FDT yields the optimal policy: cooperate at low cost, defect at high. A key insight is a Volunteer's Dilemma, where the reward is dependent on cooperation from *at least one* twin. Under P-FDT, the best outcome has both twins doing $\pi^*(\textit{low}) = C$ and $\pi^*(\textit{high}) = D$.


**Analyzing Policy Formalization**

I'm now investigating Yudkowsky and Soares' (2017) preferred P-FDT formalization, focusing on policy iteration over individual action choices. I'm carefully reviewing the source text for mentions of policies, observations, and key footnotes. My goal is to extract every instance of this discussion.


**Formalizing Action Interventions**

I'm now diving into the implications of Equation (4) from Yudkowsky and Soares. I'm focusing on how FDT intervenes on decision outputs rather than the physical action itself. I'm noting the crucial difference in observation handling, where FDT changes intervention nodes. I'm working on how this distinction impacts policy selection and action dynamics.


**Refining Formula Implications**

I'm now carefully examining the implications of Section 9, Footnote 16, which explains how FDT selects *policies* rather than just actions. The difference is critical in multi-agent dilemmas. My focus is understanding how this policy-based intervention, compared to action intervention, alters action dynamics. I'm exploring observation handling in the policy, particularly the shift in the intervention nodes.


**Addressing Formula Nuances**

I'm now zeroing in on an anomaly in the provided formula, highlighting the missing parenthesis in the formalization and an extraneous observation term. The original authors use $\text{\$990,000} + 0.01q \cdot \text{\$1,000}$ without conditioning on the observation, which I will explicitly clarify. This demonstrates thorough understanding.


**Revising Formula Details**

I'm now revising my analysis, clarifying the domain of the policy function and the input variable. Specifically, I'm ensuring consistency in my terminology and how observations are handled in the formalization. I need to make clear the difference between inputs and observations when describing the functions.


**Clarifying Policy Inputs**

I'm now carefully differentiating between two key interpretations of the P-FDT policy function's input, clarifying how observations, priors, and world models shape the action output. The focus now is on understanding how we can operationalize both. I'm focusing on the mathematical formalization.



**Refining Policy Dynamics**

I'm now carefully examining the implications of symmetric-prior multi-agent dilemmas and differing observations. I'm focusing on the **Full-Input Policy Interpretation** of P-FDT where the policy maps the entire input $(P, G, x)$ to an action. This approach elegantly addresses uncertainties about my world-model and preferences, as exemplified by the Smoking Lesion Problem, unifying it even when there are multiple uncertain fixed points.


**Refining Observation Branches**

I'm now carefully examining the implications of a policy defining agent behavior for zero-probability observation branches. I'm especially focused on scenarios where policies dictate an agent's response to events that are counterfactual. I need to figure out what to do when those branches don't get reached, to ensure complete policy definitions.


**Addressing Policy Indeterminacy**

I'm now grappling with the implications of undefined policy actions on zero-probability observation branches. It looks like the expected utility remains unchanged when policies agree on reachable observations or have probability zero. My focus is on addressing this ambiguity, to resolve argmax ties in P-FDT. I'm exploring trembling-hand predictors for a more complete formalization.


**Refining Policy Refinement**

I'm now zeroing in on resolving ties in argmax by exploring trembling-hand predictors and refining policy actions on zero-probability observation branches. I'm focusing on ensuring action execution consistency across all observations, aligning the initial policy selection with its implementation. The focus is to make sure every outcome is specified.


**Refining Coordination Insights**

I'm now carefully examining the implications of a shared model $(P, G)$ within multi-agent scenarios, specifically when agents have differing observations. I'm focusing on why a *pre-observation* (or "indexically neutral") model is critical for coordination. I also need to ensure I don't go over the word limit.


**Defining Policy Functions**

I'm now focusing on clarifying how P-FDT centers around policy functions, using mathematical notation to define the key components: observations, actions, and policies. It's critical to show how P-FDT intervenes on policies, and not just actions, and how this relates to multi-agent dilemmas. I'm making sure to define sets and map these to actions.


**Formalizing P-FDT Details**

I'm now zeroing in on formalizing P-FDT with math notation, defining observation, action, and policy spaces. I'm focusing on the two-stage P-FDT procedure, specifically policy optimization via the $\mathtt{do}(\cdot)$ operator. I'm clarifying how P-FDT treats subjunctive dependencies and counterpossibilities within this formalization, and how it differs from EDT, CDT, and A-FDT.


**Analyzing Newcomb Scenarios**

I'm now analyzing the Transparent Newcomb Problem with P-FDT, showing its graph structure versus A-FDT. A-FDT requires separate nodes for full/empty boxes, needing priors about the empty branch. P-FDT simplifies with a single node representing policy choices, leading to utility maximization without external priors, and I've started the utilities calculation for all four policies.


**Formulating New Dilemma Insights**

I'm working on a formal mathematical model of asymmetric observations in multi-agent dilemmas. Focusing on the A-FDT Twin Dilemma, I'm analyzing the implications of fixed fixed-point behavior on different observation branches. I aim to mathematically show where A-FDT fails to guarantee cooperation or coordination due to external ratification.


**Clarifying Smoking Lesion Details**

I'm now making sure to clearly distinguish between Yudkowsky and Soares' statements and the open questions from footnotes. I'm focusing on defining the domain of the policy to resolve open questions. My goal is to carefully formulate the domain of the policy as *full input* versus *observations*, like in the Smoking Lesion Problem, to clarify agent behavior in scenarios with uncertainty.


**Refining Trembling Predictor Details**

I'm now carefully examining the epsilon-trembling predictor and lexicographic subjunctive dominance conditions. I'm clarifying how pre-observation priors, encoded in $(P, G)$, are essential for multi-agent games and indexical neutrality. The goal is to ensure multiple agents with different observations share the same P-FDT node, ensuring consistency.


**Refining Coordination Paradigms**

I'm working to expand upon the formalization, focusing on the implications of action independence in single-agent A-FDT and its implications for P-FDT in multi-agent scenarios. I am now evaluating the outcomes when interventions affect action choices, making sure my mathematics are sound.


```
