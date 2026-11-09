# From Actions to Policies: A Mathematical Account of Policy Functional Decision Theory (P-FDT)

## 1. Introduction: From Physical Acts to Mathematical Policies

In classical decision theory, rational choice is framed as a problem of selecting a physical act at a particular moment in time. The two standard paradigms—evidential decision theory (EDT) and causal decision theory (CDT)—disagree not over the goal of maximizing expected utility, but over how an agent should evaluate the hypothetical consequences of an action. An EDT agent asks which physical act would provide the best news if she learned she had taken it, evaluating options via Bayesian conditionalization. A CDT agent asks which physical act would physically cause the best outcome, evaluating options via causal intervention while holding the causal past fixed.

As Eliezer Yudkowsky and Nate Soares demonstrate in *"Functional Decision Theory: A New Theory of Instrumental Rationality"* (2017), both EDT and CDT fail systematically in predictable classes of decision problems. CDT leaves money on the table in Newcomb's problem, defects against psychological twins in the Prisoner's Dilemma, and leaves agents to die in Parfit's hitchhiker problem; EDT is vulnerable to statistical confounding in the smoking lesion problem and to extortion in the XOR blackmail problem. Yudkowsky and Soares propose *functional decision theory* (FDT) to resolve these failures under a single principle: an agent should treat her decision as the output of a fixed mathematical function and ask, *"Which output of this very function would yield the best outcome?"*

Yet there is a crucial fork in the formalization of this principle. Throughout the main text of their paper, Yudkowsky and Soares present an action-selecting version of the theory—which we will call **Action-FDT**—to keep the exposition simple. However, in Footnotes 7 and 16, they reveal that their preferred formulation is actually a policy-selecting theory, which we will call **policy functional decision theory (P-FDT)**. In Footnote 7, they note:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

They elaborate on the operational mechanics of **P-FDT** in Footnote 16:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

Because the source paper sets **P-FDT** aside after these brief remarks, the formal structure of **P-FDT**, the exact mechanics of its counterfactual interventions, and the reasons it diverges from Action-FDT in multi-agent settings remain largely implicit. In this essay, we reconstruct **P-FDT** from first principles, contrast its mathematical machinery with EDT, CDT, and Action-FDT, demonstrate how to apply **P-FDT** to concrete decision problems, and resolve several foundational questions that the source text leaves open.

---

## 2. Mathematical Foundations: EDT, CDT, Action-FDT, and P-FDT

Following Gibbard and Harper (1978) and Joyce (1999), Yudkowsky and Soares situate EDT, CDT, and FDT within a common expected-utility framework. Let $\mathcal{O} = \{o_1, o_2, \dots\}$ be a countable set of possible outcomes, $\mathcal{A}$ a finite set of available actions, $\mathcal{X}$ a countable set of possible observation histories, and $\mathcal{U} : \mathcal{O} \to \mathbb{R}$ a bounded utility function. An expected-utility maximizer who has received observation $x \in \mathcal{X}$ selects an action $a \in \mathcal{A}$ that maximizes

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j), \tag{1}$$

where $P(a \hookrightarrow o_j ;\, x)$ denotes the probability that outcome $o_j$ would obtain in the hypothetical scenario where action $a$ is executed after observing $x$. As Joyce (1999) observes, *"decision theories should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated."* Differing decision theories supply different definitions of the decision-hypothetical connective $\hookrightarrow$.

Let $\textsc{Outcome}$, $\textsc{Obs}$, and $\textsc{Act}$ be random variables taking values in $\mathcal{O}$, $\mathcal{X}$, and $\mathcal{A}$, respectively, and define the utility random variable $\textsc{V} \coloneqq \mathcal{U}(\textsc{Outcome})$. Writing $\mathbb{E}$ for expectation with respect to the agent's subjective probability distribution $P$, the three theories formalized in Section 5 of Yudkowsky and Soares (2017) are defined as follows:

1. **Evidential Decision Theory (EDT)** equates hypotheticals with Bayesian conditional probabilities. Its world-model is simply $P$, and it prescribes:
   $$\mathrm{EDT}(P, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs} = x, \textsc{Act} = a\right). \tag{2}$$

2. **Causal Decision Theory (CDT)** augments $P$ with a directed acyclic graph (DAG) $G$ encoding physical causal dependencies (Pearl, 1996, 2000). Using Pearl's $\mathtt{do}(\cdot)$ operator—which severs incoming arrows to the intervened variable, sets its value, and propagates the change strictly to causally downstream variables—CDT prescribes:
   $$\mathrm{CDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{Act} = a), \textsc{Obs} = x\right). \tag{3}$$

3. **Action-FDT** (the main-text formulation in Yudkowsky and Soares, 2017) augments $P$ with a broader dependency graph $G$ that encodes not only physical causation, but also logical, mathematical, and computational dependencies—what the authors term *subjunctive dependence*. In Action-FDT, $G$ contains logical variables $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ representing the output of the $\mathrm{FDT}$ algorithm when evaluated on inputs $(P, G, x)$ (where underlines denote dequotation: if $x \coloneqq 3$, then $\textsc{Z}\underline{x}$ is the variable name $\textsc{Z}3$, constructed without circularity via Kleene's 1938 second recursion theorem). Action-FDT prescribes:
   $$\mathrm{FDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right). \tag{4}$$

### Formulating P-FDT

We now construct the formal equations for **P-FDT** based on Footnotes 7 and 16. Whereas Action-FDT defines a separate logical node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ in $G$ for each possible observation $x \in \mathcal{X}$ and intervenes only on the node matching the agent's current observation, **P-FDT** treats the decision algorithm as a function that outputs a *policy*—a complete contingency plan mapping observations (or inputs) to actions.

*(Note on interpretation: We first formalize the baseline case in which the agent's prior world-model $(P, G)$ is fixed and a policy maps observations $x \in \mathcal{X}$ to actions $a \in \mathcal{A}$, as stated in Footnote 7. In Section 4, we examine the broader formulation suggested by Footnote 16 where policies map arbitrary algorithm inputs to actions.)*

Let $\Pi \coloneqq \mathcal{A}^{\mathcal{X}} = \{\pi : \mathcal{X} \to \mathcal{A}\}$ denote the set of all policies mapping observations to actions. (When $\mathcal{X}$ is finite, $|\Pi| = |\mathcal{A}|^{|\mathcal{X}|}$; if $\mathcal{X}$ is countably infinite, we restrict $\Pi$ to a suitable set of computable or measurable functions.) In **P-FDT**, the dependency graph $G$ contains a single logical decision node $\textsc{pfdt}(\underline{P}, \underline{G})$ whose state space is $\Pi$, representing the policy output of the **P-FDT** procedure given world-model $(P, G)$.

How does the physical action node $\textsc{Act}$ depend on this logical node? As Footnote 16 specifies, the algorithm chooses a policy, *"to which the agent then applies her inputs in order to select an action."* Graphically, $\textsc{Act}$ has incoming arrows from both the policy node $\textsc{pfdt}(\underline{P}, \underline{G})$ and the observation node $\textsc{Obs}$ (or whatever environmental nodes generate $\textsc{Obs}$), governed by the evaluation mechanism:

$$\textsc{Act}(\pi, x) \coloneqq \pi(x) \quad \text{for all } \pi \in \Pi, \; x \in \mathcal{X}. \tag{5}$$

Similarly, any external predictor or twin in the environment that models the agent's decision procedure is represented in $G$ as subjunctively downstream of the policy node $\textsc{pfdt}(\underline{P}, \underline{G})$.

Given a world-model $(P, G)$ and an observation $x \in \mathcal{X}$, **P-FDT** operates in two distinct stages:

1. **Policy Selection (Global Subjunctive Optimization):** The agent identifies the optimal policy $\pi^* \in \Pi$ by intervening on the logical node $\textsc{pfdt}(\underline{P}, \underline{G})$:
   $$\mathrm{PFDT}_{\mathrm{pol}}(P, G) \coloneqq \argmax_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right). \tag{6}$$

2. **Policy Application (Action Execution):** The agent applies the selected policy $\pi^* = \mathrm{PFDT}_{\mathrm{pol}}(P, G)$ to her actual observation $x$:
   $$\mathrm{PFDT}(P, G, x) \coloneqq \left[\mathrm{PFDT}_{\mathrm{pol}}(P, G)\right](x) = \left[\argmax_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right)\right](x). \tag{7}$$

Equations (5)–(7) provide a complete mathematical specification of **P-FDT** under a fixed model $(P, G)$.

---

## 3. Subjunctive Dependence, Updatelessness, and Counterfactuals in P-FDT

To understand how **P-FDT** evaluates options in practice, we must examine two features of Equations (6) and (7): how **P-FDT** models *subjunctive dependence* via counterpossible interventions, and how it processes *observational evidence*.

### Subjunctive Dependence and Counterpossibilities

In Yudkowsky and Soares's framework, *"Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."* When two physical systems—such as two twin prisoners, or an agent and a predictor's simulation of that agent—compute the same mathematical function, their outputs subjunctively depend on that function's logical value.

Because a mathematical function has a determinate output on a given input as a matter of logical necessity, imagining that $\mathrm{PFDT}_{\mathrm{pol}}(P, G)$ outputs $\pi_1$ vs. $\pi_2$ requires evaluating *counterpossibilities*—counterfactuals with logically impossible antecedents, analogous to asking how two calculators would behave if $6288 + 1048$ summed to something other than $7336$. Rather than requiring a general-purpose logical conditionalization operator $\mathtt{true}(\phi)$, both Action-FDT and **P-FDT** encode subjunctive dependencies directly into the structure of the graph $G$. When the agent constructs the hypothetical $M^{\pi \hookrightarrow}$ via $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$, Pearl's graph surgery holds fixed all variables not downstream of $\textsc{pfdt}(\underline{P}, \underline{G})$ (such as past carcinogenic lesions or pre-existing termite infestations) while updating all variables subjunctively downstream of $\textsc{pfdt}(\underline{P}, \underline{G})$ (the agent's physical action, a twin's action, and any reliable predictions of the agent's policy).

### Radical Updatelessness in P-FDT

A striking feature of Action-FDT in Equation (4)—inspired by Wei Dai's (2009) "Updateless Decision Theory" (UDT) and contrasting with Eliezer Yudkowsky's (2010) "Timeless Decision Theory" (TDT), which conditioned on evidence in addition to intervening logically—is that the expectation $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)]$ is *not* conditioned on $\textsc{Obs} = x$. Instead, Action-FDT responds to observation $x$ by changing *which node* in $G$ it intervenes upon.

In **P-FDT**, this updatelessness is carried to its logical conclusion. Notice that in Equation (6), the observation $x$ does not appear inside the $\argmax$ or the $\mathtt{do}(\cdot)$ operator at all! Expanding the expectation in Equation (6) over the possible observations $x' \in \mathcal{X}$ makes the mechanics of **P-FDT** completely transparent:

$$\mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right) = \sum_{x' \in \mathcal{X}} P\left(\textsc{Obs} = x' \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right) \cdot \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs} = x', \, \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right). \tag{8}$$

Equation (8) reveals why **P-FDT** effortlessly solves dynamic dilemmas like Parfit's Hitchhiker, the Transparent Newcomb Problem, and the Mechanical Blackmail:
* First, the probability distribution over observations, $P(\textsc{Obs} = x' \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi))$, is itself a function of the policy $\pi$. When a **P-FDT** agent evaluates a policy $\pi$, she explicitly accounts for how adopting $\pi$ alters which observations she is likely to see in the first place.
* Second, the agent always acts as she would have precommitted to act *ex ante*, because Equation (6) is mathematically identical to an *ex ante* precommitment over the policy space $\Pi$.

### Worked Example 1: P-FDT in the Transparent Newcomb Problem

Let us verify how **P-FDT** operates in the **Transparent Newcomb Problem** (Dilemma 5 in Yudkowsky and Soares, 2017) and compare the calculation to Action-FDT.

In this dilemma, both Box A (\$1,000) and Box B (\$1,000,000 or \$0) are transparent. A predictor with $99\%$ accuracy ($\textsc{Accurate} = \mathit{accurate}$ with probability $0.99$, $\mathit{inaccurate}$ with probability $0.01$) places \$1,000,000 in Box B if and only if she predicts that the agent will leave Box A behind ($\mathit{onebox}$) upon observing that Box B is $\mathit{full}$. The observation space is $\mathcal{X} = \{\mathit{full}, \mathit{empty}\}$ and the action space is $\mathcal{A} = \{\mathit{onebox}, \mathit{twobox}\}$.

In Section 6 of the reference paper, when Fiona (following Action-FDT) observes $\textsc{Obs} = \mathit{full}$, her graph $G^F$ contains two separate logical nodes: $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$ and $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$. Because she observes $\mathit{full}$, she intervenes *only* on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$. Consequently, when calculating her expected utility in the $1\%$ branch where the predictor is inaccurate and shows her an empty box, Action-FDT must treat her own behavior at the other node, $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$, as an un-intervened random variable with some prior probability $q = P^F(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty}) = \mathit{twobox})$.

Now consider Fiona executing **P-FDT**. Her policy space $\Pi = \mathcal{A}^{\mathcal{X}}$ consists of four deterministic policies, which we write as $\pi_{ab}$ where $a = \pi(\mathit{full})$ and $b = \pi(\mathit{empty})$, with $1 \coloneqq \mathit{onebox}$ and $2 \coloneqq \mathit{twobox}$:

$$\Pi = \{\pi_{11},\, \pi_{12},\, \pi_{21},\, \pi_{22}\}.$$

In her **P-FDT** graph $G^F$, there is a single rectangular intervention node $\textsc{pfdt}(\underline{P^F}, \underline{G^F})$ with arrows pointing to $\textsc{Prediction}$ and $\textsc{Act}$:

```
                  [ pfdt(P^F, G^F) ]      ( Accurate )
                     /          \              /
                    /            v            v
                   |            ( Prediction )
                   |               /       \
                   v              /         v
                ( Act ) <--------+       ( Box B )
                   \                       /
                    \                     /
                     v                   v
                      <       V         >
```

The structural equations in $P^F$ are:
* $\textsc{Prediction}(\pi_{ab}, \mathit{accurate}) = 1$ if $a = 1$, and $2$ if $a = 2$ (since the predictor checks whether the policy one-boxes when seeing $\mathit{full}$, i.e., whether $\pi(\mathit{full}) = 1$); and the reverse when $\textsc{Accurate} = \mathit{inaccurate}$.
* $\textsc{Box B}(1) = \mathit{full}$ and $\textsc{Box B}(2) = \mathit{empty}$, with $\textsc{Obs} = \textsc{Box B}$.
* $\textsc{Act}(\pi_{ab}, \mathit{full}) = a$ and $\textsc{Act}(\pi_{ab}, \mathit{empty}) = b$.

Using Equation (6), Fiona evaluates $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt}(\underline{P^F}, \underline{G^F}) = \pi_{ab})]$ for all four policies in $\Pi$:

$$\begin{aligned}
\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\pi_{12})\right] &= 0.99 \cdot \mathcal{U}(\mathit{1f}) + 0.01 \cdot \mathcal{U}(\mathit{2e}) = 0.99(\$1,000,000) + 0.01(\$1,000) = \$990,010, \\
\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\pi_{11})\right] &= 0.99 \cdot \mathcal{U}(\mathit{1f}) + 0.01 \cdot \mathcal{U}(\mathit{1e}) = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000, \\
\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\pi_{22})\right] &= 0.01 \cdot \mathcal{U}(\mathit{2f}) + 0.99 \cdot \mathcal{U}(\mathit{2e}) = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000, \\
\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\pi_{21})\right] &= 0.01 \cdot \mathcal{U}(\mathit{2f}) + 0.99 \cdot \mathcal{U}(\mathit{1e}) = 0.01(\$1,001,000) + 0.99(\$0) = \$10,010.
\end{aligned}$$

The unique optimal policy is $\pi^* = \pi_{12}$, which prescribes one-boxing when Box B is full and two-boxing when Box B is empty. By Equation (7), upon observing $\textsc{Obs} = \mathit{full}$, Fiona executes $\mathrm{PFDT}(P^F, G^F, \mathit{full}) = \pi_{12}(\mathit{full}) = \mathit{onebox}$.

Notice that while **P-FDT** and Action-FDT prescribe the same action here, **P-FDT** is mathematically cleaner: the nuisance parameter $q$ representing Fiona's prior epistemic uncertainty about her own action in the counterfactual $\mathit{empty}$ branch vanishes entirely, because **P-FDT** jointly optimizes over both branches at once.

---

## 4. Unresolved Questions and Operational Extensions of P-FDT

Because Yudkowsky and Soares mention **P-FDT** only in Footnotes 7 and 16, they leave three important theoretical and operational questions unresolved:
1. Why and how does **P-FDT** diverge from Action-FDT in multi-agent dilemmas?
2. What is the precise domain of a policy $\pi$—does it map only *observations* $\mathcal{X}$ to actions (as Footnote 7 states), or all *inputs* $(P, G, x)$ to actions (as Footnote 16 suggests), particularly when an agent is uncertain about her own world-model or preferences?
3. How should **P-FDT** handle policy ties and computational scaling?

In what follows, we distinguish the claims of the source text from our own mathematical proposals and develop operational answers to each question.

### 4.1. How P-FDT Diverges from Action-FDT in Multi-Agent Dilemmas

The source text states that choosing a policy rather than an action *"makes a difference in certain multi-agent dilemmas"* (Footnote 7; cf. Footnote 16), without providing an example. Using our formalizations of Action-FDT in Equation (4) and **P-FDT** in Equations (6)–(7), we can pinpoint the exact structural reason they diverge and construct a multi-agent dilemma that separates them.

Why does Action-FDT ever fail where **P-FDT** succeeds? In Action-FDT, an agent who observes $x_1$ intervenes *only* on the node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_1})$, treating the node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_2})$ for any other observation $x_2 \neq x_1$ as a fixed background variable governed by her prior $P$. In a single-agent problem against a predictor who only predicts what the agent will do at $x_1$, this creates no trouble. However, in a multi-agent dilemma where a twin, copy, or coalition partner implements the *same* decision algorithm $(P, G)$ but receives a *different* observation $x_2 \neq x_1$, the twin's action is controlled by the node for $x_2$. Under Action-FDT, intervening on $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_1})$ **severs coordination** with the twin who observes $x_2$, because $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_2})$ is not downstream of $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x_1})$! Under **P-FDT**, by contrast, both twins' actions are downstream of the *same* global policy node $\textsc{pfdt}(\underline{P}, \underline{G})$.

Consider the following concrete dilemma (our own construction) to see this divergence in action:

> **Dilemma (Asymmetric-Observation Twin Stag Hunt).** An agent and her perfect psychological twin—known to run the exact same decision algorithm with the same initial world-model $(P, G)$—are placed in separate rooms. One room has a red light ($\textsc{Obs} = \mathit{red}$) and the other has a blue light ($\textsc{Obs} = \mathit{blue}$); each twin is equally likely ($50\% / 50\%$) to be placed in the red or blue room. Each twin must independently choose whether to $\mathit{work}$ (at a personal effort cost equivalent to $\$1,000$) or $\mathit{shirk}$ (cost $\$0$). If *both* the twin in the red room and the twin in the blue room choose $\mathit{work}$, a joint project succeeds and each twin receives $\$1,000,000$. If either twin chooses $\mathit{shirk}$, the project fails and neither gets the $\$1,000,000$. Suppose the agent enters her room and observes $\textsc{Obs} = \mathit{red}$. Should she $\mathit{work}$ or $\mathit{shirk}$?

Let us compare **Action-FDT** and **P-FDT** on this dilemma:

* **How Action-FDT behaves:** Suppose Fiona runs Action-FDT and observes $\textsc{Obs} = \mathit{red}$. In her dependency graph $G^F$, her own physical action $\textsc{Act}$ (since she is in the red room) is controlled by $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{red})$, while her twin's action $\textsc{TwinAct}$ (in the blue room) is controlled by the distinct node $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{blue})$. When Fiona evaluates Equation (4) for $x = \mathit{red}$, she intervenes on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{red})$. Because $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{blue})$ is a separate root node in $G^F$, her intervention does *not* change the probability that her twin in the blue room works! Let $q = P^F(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{blue}) = \mathit{work})$ be her prior probability that the algorithm outputs $\mathit{work}$ on input $\mathit{blue}$. Then her expected utilities under Action-FDT are:
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{red}) = \mathit{work}\right)\right] = q \cdot \$1,000,000 - \$1,000,$$
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{red}) = \mathit{shirk}\right)\right] = \$0.$$
  Notice the disaster: if Fiona initially believes that her blue-room counterpart will shirk ($q < 0.001$), then Action-FDT prescribes $\mathit{shirk}$ in the red room! By symmetry, if the twin in the blue room also assigns probability $q_{\mathit{red}} < 0.001$ to $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{red}) = \mathit{work}$, then Action-FDT prescribes $\mathit{shirk}$ in the blue room as well. And if both shirk, their pessimistic beliefs ($q = q_{\mathit{red}} = 0$) are completely accurate and reflectively consistent! Just like EDT with extreme priors or CDT in a Stag Hunt, Action-FDT can be trapped in a mutually destructive $( \mathit{shirk}, \mathit{shirk} )$ equilibrium because it cannot intervene on both observation branches simultaneously.

  *(A second, even starker failure of Action-FDT occurs in an **Altruistic/Cross-Payoff Twin Dilemma**: suppose the twin in the red room can pay $\$1,000$ to give the twin in the blue room $\$1,000,000$, and vice versa, where each twin only cares about her own payout. Under Action-FDT, once Fiona observes $\mathit{red}$, she knows she is in the red room; intervening on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{red}) = \mathit{pay}$ only costs her $\$1,000$ to benefit the other twin without affecting $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{blue})$! Thus Action-FDT defects with certainty regardless of priors $q$, whereas **P-FDT** evaluates the policy $\pi$ prior to conditioning on which room she is in, yielding $0.5(\$1,000,000 - \$1,000) + 0.5(\$1,000,000 - \$1,000) = \$999,000$ for $\pi_{\mathit{pay},\mathit{pay}}$ vs. $\$0$ for $\pi_{\mathit{refuse},\mathit{refuse}}$!)*

* **How P-FDT behaves:** Now suppose Fiona runs **P-FDT** in the Asymmetric-Observation Twin Stag Hunt. In her **P-FDT** graph, both her own action $\textsc{Act}(\pi, \textsc{Obs})$ and her twin's action $\textsc{TwinAct}(\pi, \textsc{TwinObs})$ are deterministic functions of the *single* policy node $\textsc{pfdt}(\underline{P^F}, \underline{G^F})$. There are four policies $\pi_{ab} \in \{\mathit{W}, \mathit{S}\}^{\{\mathit{red}, \mathit{blue}\}}$, where $a = \pi(\mathit{red})$ and $b = \pi(\mathit{blue})$. Evaluating Equation (6):
  $$\begin{aligned}
  \mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\pi_{\mathit{W}\mathit{W}})\right] &= \$1,000,000 - \$1,000 = \$999,000, \\
  \mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\pi_{\mathit{W}\mathit{S}})\right] &= 0.5(-\$1,000) + 0.5(\$0) = -\$500, \\
  \mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\pi_{\mathit{S}\mathit{W}})\right] &= 0.5(\$0) + 0.5(-\$1,000) = -\$500, \\
  \mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\pi_{\mathit{S}\mathit{S}})\right] &= \$0.
  \end{aligned}$$
  Regardless of any prior beliefs $q$, **P-FDT** uniquely selects $\pi^* = \pi_{\mathit{W}\mathit{W}}$, and upon observing $\mathit{red}$, Fiona executes $\pi_{\mathit{W}\mathit{W}}(\mathit{red}) = \mathit{work}$. Both twins work and walk away with $\$999,000$ net utility.

### 4.2. The Domain of a Policy: Observations ($\mathcal{X}$) vs. Full Inputs ($\mathcal{M} \times \mathcal{X}$)

A second question left open by the source text concerns a subtle discrepancy between Footnote 7 and Footnote 16:
* Footnote 7 defines policies as *"mappings from observations to actions"* ($\pi : \mathcal{X} \to \mathcal{A}$).
* Footnote 16 says that **P-FDT** *"intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action."*

In Equation (4) of the paper, the inputs to the $\mathrm{FDT}$ function are not merely the observation $x$, but the triple $(P, G, x)$—that is, the world-model $M = (P, G)$ together with $x$. Why does this distinction matter?

Recall how Yudkowsky and Soares formalize **The Smoking Lesion Problem** in Section 6 (Figure 4). Because the lesion causes the agent to love smoking, they model the lesion as determining the agent's utility function: an agent with the lesion has distribution $P_S^F$ (incorporating utility function $\mathcal{U}_S$, which values smoking at $+\$1,000$), while an agent without the lesion has distribution $P_R^F$ (incorporating $\mathcal{U}_R$, which values smoking at $-\$1$). Because Fiona does not have introspective access to whether she has the lesion, her graph $G^F$ in Figure 4 contains two distinct decision nodes corresponding to different model inputs: $\textsc{fdt}(\underline{P_S^F}, \underline{G^F})$ and $\textsc{fdt}(\underline{P_R^F}, \underline{G^F})$. When Fiona actually has the lesion, she intervenes on $\textsc{fdt}(\underline{P_S^F}, \underline{G^F})$ while treating $\textsc{fdt}(\underline{P_R^F}, \underline{G^F})$ as a background variable with prior probability $q$.

If we apply **P-FDT** to dilemmas where an agent (or her twin in a Bayesian game) may have different world-models $M \in \mathcal{M}$, which node does **P-FDT** intervene on? We propose that we must distinguish two operational interpretations of **P-FDT**:

1. **Model-Indexed P-FDT ($\pi : \mathcal{X} \to \mathcal{A}$):** Under this interpretation (matching Equations 6–7 above), the policy node is $\textsc{pfdt}(\underline{P}, \underline{G})$, indexed by the agent's world-model $(P, G)$ (including her utility function $\mathcal{U}$), and outputs a mapping $\pi : \mathcal{X} \to \mathcal{A}$. In the Smoking Lesion problem, $\textsc{pfdt}(\underline{P_S^F}, \underline{G^F})$ and $\textsc{pfdt}(\underline{P_R^F}, \underline{G^F})$ remain separate nodes in $G^F$.
2. **Universal-Input P-FDT ($\Pi_{\mathrm{univ}} = \{\Psi : \mathcal{M} \times \mathcal{X} \to \mathcal{A}\}$):** Under a literal reading of Footnote 16 (*"intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a policy which maps inputs to actions"*), $G^F$ contains a single unindexed node $\textsc{pfdt}$ representing the universal **P-FDT** algorithm itself, and the agent intervenes to set $\textsc{pfdt} = \Psi$, where $\Psi(P, G, x) \in \mathcal{A}$ specifies what the algorithm outputs for *every* possible world-model $(P, G)$ and observation $x$.

Which interpretation is normatively and operationally superior? Here we offer our own analysis and proposal:
* If two models $P_1, P_2 \in \mathcal{M}$ differ only in **epistemic beliefs or private information** while sharing the same fundamental utility function $\mathcal{U}$, those differences should be absorbed into the observation space $\mathcal{X}$ over a common prior $(P, G)$ (following Harsanyi's 1967 doctrine of common priors in Bayesian games). Then Model-Indexed **P-FDT** ($\pi : \mathcal{X} \to \mathcal{A}$) already coordinates across all epistemic states!
* Conversely, if two models $P_S^F$ and $P_R^F$ have **different utility functions** $\mathcal{U}_S \neq \mathcal{U}_R$ (as in the Smoking Lesion formalization), Universal-Input **P-FDT** exhibits a subtle pathology: when an agent with utility function $\mathcal{U}_S$ evaluates a universal meta-policy $\Psi$ using $\mathcal{U}_S$, she evaluates $\Psi(P_R^F, G^F)$ according to $\mathcal{U}_S$ rather than $\mathcal{U}_R$! In the Smoking Lesion problem, an agent with the lesion ($\mathcal{U}_S$) evaluating Universal-Input **P-FDT** would judge that the optimal meta-policy $\Psi^*$ should force her lesion-free counterfactual self ($P_R^F$) to smoke too, yielding expected utility $p(\$10,000 + \$1,000) + (1-p)(\$990,000 + \$1,000)$, even though her lesion-free self hates smoking! Worse, if a predictor rewarded agents only if their decision function respected $\mathcal{U}_R$ when given input $P_R^F$, Universal-Input **P-FDT** evaluated from the perspective of $\mathcal{U}_S$ would mispredict its own behavior on input $P_R^F$ (since an agent actually running Universal-Input **P-FDT** with $\mathcal{U}_R$ would select a *different* meta-policy $\Psi^*_R \neq \Psi^*_S$).

**Operational Proposal:** To prevent counterfactual preference-imposition across distinct utility functions while preserving full multi-agent coordination across observations and private signals, **P-FDT** should be formalized as in Equations (6)–(7): the logical node $\textsc{pfdt}(\underline{P}, \underline{G})$ is parameterized by the agent's prior $(P, G)$ and utility function $\mathcal{U}$, and outputs a policy $\pi : \mathcal{X} \to \mathcal{A}$ mapping all observational and informational inputs $x \in \mathcal{X}$ to actions.

### 4.3. Canonical Tie-Breaking and Computational Scaling

Two final operational considerations arise when applying **P-FDT** to unfamiliar cases:

1. **Coordination under Policy Ties:** In Equation (6), $\argmax_{\pi \in \Pi} \mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)]$ may return a set of multiple tied optimal policies $\Pi^* \subset \Pi$. For instance, in our Asymmetric-Observation Twin dilemma, suppose the twins receive $\$1,000,000$ if and only if they choose *opposite* actions—either $(\pi(\mathit{red}) = A, \pi(\mathit{blue}) = B)$ or $(\pi(\mathit{red}) = B, \pi(\mathit{blue}) = A)$. Both policies $\pi_{AB}$ and $\pi_{BA}$ achieve the maximum expected utility of $\$1,000,000$, whereas $\pi_{AA}$ and $\pi_{BB}$ yield $\$0$. If the red-room twin breaks the tie in favor of $\pi_{AB}$ while the blue-room twin breaks the tie in favor of $\pi_{BA}$, they will execute $(A, A)$ and get $\$0$! Because **P-FDT** treats $\mathrm{PFDT}_{\mathrm{pol}}(P, G)$ as a deterministic mathematical function, we must equip $\argmax_{\pi \in \Pi}$ with a fixed, canonical tie-breaking rule (e.g., selecting the lexicographically first policy in $\Pi^*$ under a fixed encoding of $\mathcal{X}$ and $\mathcal{A}$) so that all agents implementing **P-FDT** select the exact same policy $\pi^* \in \Pi^*$.
2. **Computational Complexity and Bounded Approximation:** Because $|\Pi| = |\mathcal{A}|^{|\mathcal{X}|}$ grows exponentially in the number of possible observations $|\mathcal{X}|$, exact enumeration of $\Pi$ in Equation (6) is intractable for large observation spaces. However, notice that in any problem where the observation $\textsc{Obs}$ does not subjunctively depend on off-observation branches of $\pi$ and no other agent's payoff-relevant action depends on those branches, Equation (8) decomposes additively across $x' \in \mathcal{X}$:
   $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)\right] = \sum_{x' \in \mathcal{X}} w(x', \pi(x')) \cdot v(x', \pi(x')).$$
   Whenever this decomposition holds, maximizing over $\pi \in \Pi$ reduces to optimizing $\pi(x)$ independently at the observed $x$, recovering Action-FDT as a fast, exact local reduction of **P-FDT**. Bounded **P-FDT** agents only need to optimize jointly over the subset of observations $\mathcal{X}_{\mathrm{coupled}} \subseteq \mathcal{X}$ that are subjunctively coupled through multi-agent interaction or cross-branch predictors.

---

## 5. Conclusion

**Policy functional decision theory (P-FDT)** represents the most general and mathematically cohesive formulation of the functionalist program in decision theory. By shifting the locus of counterfactual intervention from physical actions (CDT) and observation-specific logical outputs (Action-FDT) to a global policy node $\textsc{pfdt}(\underline{P}, \underline{G})$ mapping inputs to actions, **P-FDT** embodies Yudkowsky and Soares's "global perspective" in its purest form.

As we have seen, **P-FDT** retains every advantage of Action-FDT in classic single-agent dilemmas—one-boxing in standard and transparent Newcomb problems, smoking in the smoking lesion problem, paying the driver in Parfit's hitchhiker problem, and resisting extortion in both XOR and mechanical blackmail—while eliminating arbitrary prior parameters over unvisited observation branches. More importantly, in multi-agent dilemmas where copies, twins, or predictors depend on how the decision procedure behaves across distinct observations, **P-FDT** succeeds where Action-FDT falters, coordinating seamlessly across asymmetric information states. While foundational questions remain regarding how bounded agents learn subjunctive dependency graphs $G$ from experience, **P-FDT** provides a clear, rigorous, and operationally complete rule for instrumental rationality in a world populated by predictors and fellow reasoners.

---

## References

* Dai, W. (2009). Towards a New Decision Theory. *Less Wrong*. http://lesswrong.com/lw/15m/towards_a_new_decision_theory/
* Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. Cambridge, MA: MIT Press.
* Gibbard, A., & Harper, W. L. (1978). Counterfactuals and Two Kinds of Expected Utility. In C. A. Hooker, J. J. Leach, & E. F. McClennen (Eds.), *Foundations and Applications of Decision Theory* (Vol. 1). Boston: D. Reidel.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. New York: Cambridge University Press.
* Kleene, S. C. (1938). On Notation for Ordinal Numbers. *Journal of Symbolic Logic*, 3(4), 150–155.
* Lewis, D. (1979). Prisoners' Dilemma is a Newcomb Problem. *Philosophy & Public Affairs*, 8(3), 235–240.
* Lewis, D. (1981). Causal Decision Theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
* Nozick, R. (1969). Newcomb's Problem and Two Principles of Choice. In N. Rescher (Ed.), *Essays in Honor of Carl G. Hempel* (pp. 114–146). Dordrecht: D. Reidel.
* Parfit, D. (1986). *Reasons and Persons*. New York: Oxford University Press.
* Pearl, J. (1996). Causation, Action, and Counterfactuals. In *6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-'96)* (pp. 51–73). Morgan Kaufmann.
* Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. New York: Cambridge University Press.
* Skyrms, B. (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. New Haven, CT: Yale University Press.
* Soares, N., & Fallenstein, B. (2015). Toward Idealized Decision Theory. *arXiv preprint arXiv:1507.01986*.
* Yudkowsky, E. (2010). *Timeless Decision Theory*. The Singularity Institute, San Francisco, CA.
* Yudkowsky, E., & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. Machine Intelligence Research Institute, arXiv:1710.05060v2.