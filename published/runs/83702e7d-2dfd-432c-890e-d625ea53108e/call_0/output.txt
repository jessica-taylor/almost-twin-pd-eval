# Policy Functional Decision Theory (P-FDT): Mathematical Foundations, Counterfactuals, and Applications

## 1. Introduction: From Physical Acts to Mathematical Policies

For half a century, normative decision theory was split between two rival paradigms: **evidential decision theory (EDT)** and **causal decision theory (CDT)**. EDT instructs an agent to choose the action that would be the best news to learn she had taken—maximizing expected utility conditional on the action. CDT instructs an agent to choose the action that causally produces the best outcome—maximizing expected utility under a causal intervention on the physical act. Neither theory dominates the other in expected utility achieved across standard decision problems: EDT outperforms CDT in Newcomb's problem (Nozick 1969), whereas CDT outperforms EDT in the smoking lesion problem (Skyrms 1980; Gibbard and Harper 1978). Moreover, in sequential or extortionary predictive dilemmas—such as Parfit's hitchhiker problem (Parfit 1986), the transparent Newcomb problem (Drescher 2006), and the mechanical blackmail problem (Soares and Fallenstein 2015)—both CDT and EDT fail simultaneously.

In *"Functional Decision Theory: A New Theory of Instrumental Rationality"*, Eliezer Yudkowsky and Nate Soares (2017) resolve this impasse by introducing **functional decision theory (FDT)**. Rather than treating a decision as a localized physical event (CDT) or an piece of evidence about the state of the world (EDT), a functional decision theorist treats her decision as the output of a fixed mathematical function and asks: *"Which output of this very function would yield the best outcome?"*

Yet buried in two footnotes of Yudkowsky and Soares's paper is a crucial distinction between the simplified action-selection equation presented in their main text and the version of the theory the authors actually endorse. In Footnote 7, the authors write:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

And in Footnote 16, while discussing how an agent responds to observations without performing a standard Bayesian update on her world-model, they elaborate:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

In this essay, we call this policy-selection formulation **policy functional decision theory (P-FDT)**, distinguishing it from the action-by-action formulation in Yudkowsky and Soares's main text (which we will refer to as **action-based FDT**). As we will see, moving from action interventions to policy interventions is not merely a technical convenience. It eliminates residual prior-sensitivity in single-agent sequential problems, enables coordination among agents who receive asymmetric observations, and clarifies why functional decision theorists evaluate hypotheticals from an "updateless," global perspective. Where Yudkowsky and Soares's brief remarks in Footnotes 7 and 16 leave formal choices open, we will identify those uncertainties explicitly and develop a rigorous operational completion of **P-FDT**.

---

## 2. Philosophical Motivation: Subjunctive Dependence and Global Choice

To understand why **P-FDT** evaluates entire policies via functional intervention, we must first understand what goes wrong in CDT and EDT—and why action-based FDT only partially completes the shift to a functional perspective.

### 2.1 Subjunctive Dependence vs. Causal and Statistical Dependence

Consider the pairing of Newcomb's problem and the smoking lesion problem. In both dilemmas, an agent must decide whether to secure a sure $\$1,000$ (two-boxing; smoking) in the presence of a background process that determines whether she receives $\$1,000,000$ (an accurate predictor filling Box B; the absence of a carcinogenic lesion). 

* **EDT** conditions on the agent's action. Because one-boxing is strong statistical evidence that Box B is full, EDT one-boxes; because abstaining from smoking is strong statistical evidence that the agent lacks the carcinogenic lesion, EDT abstains from smoking. EDT fails because its hypotheticals preserve *all* statistical correlations between the action and the environment, even when those correlations arise from a merely statistical common cause (the lesion).
* **CDT** severs all correlations between the action and anything not causally downstream of the physical act. CDT smokes in the smoking lesion problem, recognizing that smoking cannot cause a congenital lesion, but it two-boxes in Newcomb's problem, reasoning that the predictor's past prediction cannot be causally altered by a present choice.

Yudkowsky and Soares argue that CDT's surgical intervention cuts too deep. While a carcinogenic lesion does not simulate the agent's decision-making algorithm, Newcomb's predictor—or a psychological twin in a Prisoner's Dilemma (Lewis 1979)—*does*. When two physical systems (such as the agent's brain and the predictor's simulation of the agent, or two well-functioning calculators computing $6288 + 1048$) implement the same mathematical function, their outputs are logically or computationally constrained to match insofar as the implementation is accurate. Yudkowsky and Soares term this relationship **subjunctive dependence**:

> "*Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*"

In Peirce's (1934) terminology, while CDT intervenes on the physical action *token*, a functional decision theorist intervenes on the mathematical function *type*. Evaluating what would happen if a fixed deterministic function produced a different output requires evaluating *counterpossibilities*—conditionals whose antecedents are logically false, much like asking what would follow if $6288 + 1048$ equaled a different value (Cohen 1990; Bjerring 2013). Rather than attempting to construct a general logic of counterpossibilities from scratch, Yudkowsky and Soares represent subjunctive dependencies directly within an augmented structural graph $G$, allowing the agent to use Judea Pearl's (1996, 2000) graphical $\Do(\cdot)$ operator on nodes representing the outputs of mathematical functions.

### 2.2 Why Conditioning on Observations Fails

Even if an agent tracks subjunctive dependence, a second trap awaits when the agent receives observations during a decision problem. Consider **the transparent Newcomb problem** (Drescher 2006): both Box A ($\$1,000$) and Box B ($\$1,000,000$ or $\$0$) are made of transparent glass. The predictor places $\$1,000,000$ in Box B with $99\%$ accuracy if and only if she predicts that the agent will leave Box A behind *upon seeing that Box B is full*. 

When the agent steps up to the boxes and observes that Box B is in fact full ($\Var{Obs} = \Val{full}$), both CDT and EDT prescribe two-boxing. Conditional on $\Var{Obs} = \Val{full}$, the $\$1,000,000$ is already guaranteed; taking both boxes yields $\$1,001,000$ rather than $\$1,000,000$. Predictors foresee this, leave Box B empty for CDT and EDT agents, and those agents walk away with only $\$1,000$. The exact same structure governs **Parfit's hitchhiker problem** (where being rescued from the desert is analogous to seeing a full Box B, and refusing to pay the driver $\$1,000$ at the ATM is analogous to two-boxing) and **the mechanical blackmail problem** (where a predictor initiates a mutually destructive $\$1,000,000$ rumor-release program if and only if she predicts the agent will pay $\$1,000$ upon receiving the blackmail letter).

Why do EDT—and early precursors of FDT such as Yudkowsky's (2010) **timeless decision theory (TDT)**, which conditioned on evidence *and* intervened on the decision node—struggle when observations reveal past predictions? Because conditioning the probability distribution $P$ on $\Var{Obs} = \Val{full}$ (or $\Var{Obs} = \Val{blackmail}$) locks in the past state of the environment, blinding the agent to the subjunctive dependency between her response to that observation and the probability of receiving that observation in the first place. 

Following Wei Dai's (2009) **updateless decision theory (UDT)**, Yudkowsky and Soares insist that "agents should entertain the hypothesis that, if their action were different, they might have *made different observations*." **P-FDT** gives this updateless insight its cleanest mathematical expression: instead of conditioning her probability distribution on what she has observed, the agent evaluates how the entire universe behaves as a function of her *policy*—the complete mapping from observations to actions—and only plugs in her actual observation at the final step to execute the selected policy's output.

---

## 3. Mathematical Formalization of P-FDT

Let us make the formal framework precise and contrast **P-FDT** with EDT, CDT, and action-based FDT.

### 3.1 Primitives and World-Models

Following Section 5 of Yudkowsky and Soares (2017) and the representation theorem of Joyce (1999), consider an agent facing a decision problem defined by:
* A finite set of available physical actions $\mathcal{A}$.
* A countable set of possible observation histories (or inputs) $\mathcal{X}$.
* A countable set of outcomes $\mathcal{O}$, equipped with a bounded real-valued utility function $\mathcal{U}: \mathcal{O} \to \mathbb{R}$.
* A world-model $M = (P, G)$, where $P$ is a subjective probability distribution over a collection of random variables—including the observation variable $\Var{Obs}$ (taking values in $\mathcal{X}$), the physical action variable $\Var{Act}$ (taking values in $\mathcal{A}$), the outcome variable $\Var{Outcome}$ (taking values in $\mathcal{O}$), and the utility variable $\Var{V} \coloneqq \mathcal{U}(\Var{Outcome})$—and $G$ is a directed acyclic graph encoding the structural dependencies among these variables.

For any decision theory in this family, the agent evaluates options by computing the expected value of $\Var{V}$ under a theory-specific hypothetical distribution $P(\cdot \mid \text{intervention or condition})$. Using $\mathbb{E}$ to denote expectation with respect to $P$:

1. **Evidential Decision Theory (EDT)** requires only $P$ and constructs hypotheticals via Bayesian conditioning on both the observation $x \in \mathcal{X}$ and the action $a \in \mathcal{A}$:
   $$\mathrm{EDT}(P, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\Var{V} \;\middle|\; \Var{Obs} = x, \Var{Act} = a\right).$$

2. **Causal Decision Theory (CDT)** augments $P$ with a *causal* graph $G^C$, conditions on $\Var{Obs} = x$, and intervenes on the physical action node $\Var{Act}$ via Pearl's $\Do(\cdot)$ operator:
   $$\mathrm{CDT}(P, G^C, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\Var{V} \;\middle|\; \Do(\Var{Act} = a), \Var{Obs} = x\right).$$

3. **Action-Based FDT (Main Text of Yudkowsky and Soares)** augments $P$ with a *subjunctive* dependency graph $G^F$ that includes logical nodes $\Var{fdt}(\underline{P}, \underline{G^F}, \underline{x})$ for each possible observation $x \in \mathcal{X}$ (where underlines denote dequoting: inserting the literal value of the variable into the node's name via Kleene's [1938] recursion theorem). When the agent observes $x$, action-based FDT does not condition $P$ on $\Var{Obs} = x$; instead, it intervenes on the specific observation-indexed node $\Var{fdt}(\underline{P}, \underline{G^F}, \underline{x})$:
   $$\mathrm{FDT}(P, G^F, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\Var{V} \;\middle|\; \Do\left(\Var{fdt}(\underline{P}, \underline{G^F}, \underline{x}) = a\right)\right).$$

### 3.2 Formalizing P-FDT from Footnotes 7 and 16

Now let us formalize **P-FDT** on the basis of Footnotes 7 and 16. Where the source leaves the exact notation implicit, we state our mathematical definitions explicitly.

**Definition 1 (Policy Space).** A *policy* is a function $\pi: \mathcal{X} \to \mathcal{A}$ that maps each possible observation (or input) $x \in \mathcal{X}$ to an action $\pi(x) \in \mathcal{A}$. We denote the set of all available policies by $\Pi \coloneqq \mathcal{A}^{\mathcal{X}}$. (When $\mathcal{X}$ and $\mathcal{A}$ are finite, $\Pi$ is a finite set of cardinality $|\mathcal{A}|^{|\mathcal{X}|}$.)

**Definition 2 (P-FDT World-Model and Subjunctive Graph).** In a **P-FDT** world-model $M = (P, G)$, instead of containing separate root nodes $\Var{fdt}(\underline{P}, \underline{G}, \underline{x})$ for each individual observation $x \in \mathcal{X}$, the graph $G$ contains a single policy-function node, denoted $\Var{pfdt}(\underline{P}, \underline{G})$ (corresponding to $\mathrm{FDT}(-)$ in Footnote 16), which takes values in the policy space $\Pi$. 
* In $G$, the agent's physical action $\Var{Act}$ is a structural function of both the policy node $\Var{pfdt}(\underline{P}, \underline{G})$ and the observation node $\Var{Obs}$:
  $$\Var{Act}\big(\pi, x\big) \coloneqq \pi(x).$$
* Similarly, if the environment contains predictors, blackmailers, or computational twins whose behavior subjunctively depends on the agent's decision procedure, their respective nodes in $G$ are children of $\Var{pfdt}(\underline{P}, \underline{G})$: a predictor simulating how the agent responds to observation $x'$ reads the value $\pi(x')$ from $\pi = \Var{pfdt}(\underline{P}, \underline{G})$, and a twin receiving observation $x''$ executes $\pi(x'')$.

**Definition 3 (The P-FDT Decision Rule).** Given a world-model $(P, G)$ and an actual observation $x \in \mathcal{X}$, **P-FDT** selects an action in two steps:

1. **Global Policy Optimization:** The agent identifies the optimal policy $\pi^* \in \Pi$ by intervening on the node $\Var{pfdt}(\underline{P}, \underline{G})$ across the unconditioned prior model $(P, G)$:
   $$\pi^* \in \argmax_{\pi \in \Pi} \mathbb{E}\left(\Var{V} \;\middle|\; \Do\left(\Var{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right). \tag{P-FDT.1}$$
2. **Policy Application:** The agent applies the optimal policy $\pi^*$ to her actual observation $x$ to output a physical action:
   $$\mathrm{PFDT}(P, G, x) \coloneqq \pi^*(x) = \left[\argmax_{\pi \in \Pi} \mathbb{E}\left(\Var{V} \;\middle|\; \Do\left(\Var{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right)\right](x). \tag{P-FDT.2}$$

### 3.3 Operational Recipe for Applying P-FDT to Unfamiliar Problems

To apply **P-FDT** to any concrete decision problem, a practitioner can execute the following five-step algorithm:

1. **Specify the Spaces:** List the set of possible observations $\mathcal{X}$ the agent (or any copy of the agent) might receive in the dilemma, the set of actions $\mathcal{A}$, and the policy space $\Pi = \mathcal{A}^{\mathcal{X}}$.
2. **Construct the Structural Graph $G$ and Prior $P$:** Introduce the policy node $\Var{pfdt}(\underline{P}, \underline{G})$, exogenous chance nodes (such as predictor accuracy or background states of nature), environmental/predictor nodes, the observation node $\Var{Obs}$, the action node $\Var{Act}$, and the utility node $\Var{V}$. Draw directed edges from $\Var{pfdt}(\underline{P}, \underline{G})$ to $\Var{Act}$ and to every environmental node that simulates, predicts, or replicates the agent's decision procedure.
3. **Evaluate Candidate Policies via $\Do(\Var{pfdt}(\underline{P}, \underline{G}) = \pi)$:** For each policy $\pi \in \Pi$, substitute $\Var{pfdt}(\underline{P}, \underline{G}) = \pi$ into the structural equations of $G$ *without* conditioning on the actual observation $x$. Propagate this intervention downstream to compute the induced probability distribution over outcomes and the expected utility $\mathcal{EU}(\pi) \coloneqq \mathbb{E}[\Var{V} \mid \Do(\Var{pfdt}(\underline{P}, \underline{G}) = \pi)]$.
4. **Select the Optimal Policy:** Choose $\pi^* \in \argmax_{\pi \in \Pi} \mathcal{EU}(\pi)$.
5. **Evaluate at the Actual Input:** Given the observation $x \in \mathcal{X}$ actually received, execute the action $a^* = \pi^*(x)$.

---

## 4. P-FDT in Action: Single-Agent and Multi-Agent Dilemmas

Let us see how this formal procedure works in practice—first in a single-agent sequential dilemma where **P-FDT** streamlines action-based FDT, and then in a multi-agent dilemma where **P-FDT** and action-based FDT sharply diverge.

### 4.1 Single-Agent Sequential Dilemmas: The Transparent Newcomb Problem

Consider the transparent Newcomb problem from Section 6 of Yudkowsky and Soares (2017). Box A contains $\$1,000$; Box B is transparent and contains either $\$1,000,000$ ($\Val{full}$) or $\$0$ ($\Val{empty}$). The predictor has accuracy $0.99$ and fills Box B if and only if she predicts the agent will one-box upon observing $\Val{full}$.

Let us apply our five-step **P-FDT** procedure:

1. **Spaces:** The observation space is $\mathcal{X} = \{\Val{full}, \Val{empty}\}$ and the action space is $\mathcal{A} = \{\Val{onebox}, \Val{twobox}\}$. There are $|\mathcal{A}|^{|\mathcal{X}|} = 2^2 = 4$ policies in $\Pi$, which we write as pairs $\pi = (\pi(\Val{full}), \pi(\Val{empty}))$:
   $$\pi_{11} = (\Val{onebox}, \Val{onebox}), \quad \pi_{12} = (\Val{onebox}, \Val{twobox}), \quad \pi_{21} = (\Val{twobox}, \Val{onebox}), \quad \pi_{22} = (\Val{twobox}, \Val{twobox}).$$

2. **Structural Model $(P, G)$:** 
   ```
                    +--------------------+
                    |  pfdt(P, G)  [pi]  |
                    +--------------------+
                       /              \
                      /                v
                     /           +------------+     +----------+
                    |            | Prediction | <-- | Accurate |
                    |            +------------+     +----------+
                    |                  |
                    |                  v
                    |              +-------+
                    |              | Box B |
                    |              +-------+
                    |                  |
                    v                  v
                 +-----+            +-----+
                 | Act | <--------- | Obs |
                 +-----+            +-----+
                    \                 /
                     \               / (via Box B)
                      v             v
                          +-----+
                          |  V  |
                          +-----+
   ```
   * Exogenous accuracy: $P(\Var{Accurate} = \Val{accurate}) = 0.99$, $P(\Var{Accurate} = \Val{inaccurate}) = 0.01$.
   * Prediction equation: $\Var{Prediction}(\pi, \Val{accurate}) = \Val{1}$ if $\pi(\Val{full}) = \Val{onebox}$ and $\Val{2}$ if $\pi(\Val{full}) = \Val{twobox}$ (and the reverse when $\Var{Accurate} = \Val{inaccurate}$).
   * Box B and Observation: $\Var{Box B}(\Val{1}) = \Val{full}$, $\Var{Box B}(\Val{2}) = \Val{empty}$, and $\Var{Obs} = \Var{Box B}$.
   * Action and Utility: $\Var{Act}(\pi, \Var{Obs}) = \pi(\Var{Obs})$, and $\Var{V}(\Var{Act}, \Var{Box B}) = \$1,000,000 \cdot \mathbb{I}(\Var{Box B} = \Val{full}) + \$1,000 \cdot \mathbb{I}(\Var{Act} = \Val{twobox})$.

3. **Policy Evaluation:** Under $\Do(\Var{pfdt}(\underline{P}, \underline{G}) = \pi)$, we compute $\mathcal{EU}(\pi)$ for all four policies:
   * $\mathcal{EU}(\pi_{11}) = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000$.
   * $\mathcal{EU}(\pi_{12}) = 0.99(\$1,000,000) + 0.01(\$1,000) = \$990,010$.
   * $\mathcal{EU}(\pi_{21}) = 0.01(\$1,001,000) + 0.99(\$0) = \$10,010$.
   * $\mathcal{EU}(\pi_{22}) = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000$.

4. **Optimal Policy:** The unique maximizer is $\pi^* = \pi_{12} = (\Val{onebox}, \Val{twobox})$, achieving $\$990,010$ in expectation.

5. **Action Execution:** When the agent actually observes $x = \Val{full}$, she executes $\mathrm{PFDT}(P, G, \Val{full}) = \pi_{12}(\Val{full}) = \Val{onebox}$. (If the predictor errs and she observes $x = \Val{empty}$, she executes $\pi_{12}(\Val{empty}) = \Val{twobox}$.)

**Why P-FDT Improves on Action-Based FDT Even in Single-Agent Problems:**
In Section 6 of Yudkowsky and Soares's paper, when Fiona evaluates action-based FDT upon seeing $\Val{full}$, she intervenes *only* on $\Var{fdt}(\underline{P^F}, \underline{G^F}, \Val{full})$ while leaving $\Var{fdt}(\underline{P^F}, \underline{G^F}, \Val{empty})$ as an un-intervened random variable with prior probability $q = P^F(\Var{fdt}(\underline{P^F}, \underline{G^F}, \Val{empty}) = \Val{twobox})$. Consequently, her expected utilities depend on $q$: $\$990,000 + \$10q$ for one-boxing versus $\$10,010 + \$990q$ for two-boxing. In the transparent Newcomb problem, $\$990,000$ swamps $\$990q$, so $q$ does not flip the decision. 

However, it is easy to construct a modified single-agent problem where thepredictor simulates the agent across *both* observations $\Val{full}$ and $\Val{empty}$—for instance, suppose a fairness-minded predictor fills Box B if and only if she predicts both that the agent will one-box when Box B is full *and* that the agent will two-box when Box B is empty. Under action-based FDT, if the agent has a sufficiently small prior $q$ that she would two-box on $\Val{empty}$, intervening on $\Var{fdt}(\underline{P^F}, \underline{G^F}, \Val{full})$ alone fails to guarantee that the predictor fills the box! Action-based FDT reintroduces across observation branches the very sensitivity to priors over one's own future or counterfactual decisions that Yudkowsky and Soares criticize in EDT. **P-FDT** eliminates the nuisance parameter $q$ altogether because $\Do(\Var{pfdt}(\underline{P}, \underline{G}) = \pi)$ simultaneously controls the agent's behavior across *all* observation branches.

### 4.2 Multi-Agent Dilemmas: Where P-FDT and Action-Based FDT Diverge

Footnotes 7 and 16 state that iterating over policies rather than actions "makes a difference in certain multi-agent dilemmas," without working through an example. Let us construct a concrete multi-agent dilemma that exposes why action-based FDT fails and how **P-FDT** succeeds.

> **Dilemma 1 (The Asymmetric-Observation Twin Coalition).** An agent and her exact computational twin are placed in separate rooms to perform a joint task. One room is painted blue ($\Var{Obs}_1 = \Val{blue}$) and the other is painted red ($\Var{Obs}_2 = \Val{red}$). Each twin observes the color of her own room and must choose whether to $\Val{work}$ (at a personal effort cost of $\$1,000$) or $\Val{shirk}$ (cost $\$0$). If *both* twins choose $\Val{work}$, the joint task succeeds and each twin receives $\$1,000,000$. If *either* twin chooses $\Val{shirk}$, the task fails and neither gets the $\$1,000,000$ (so anyone who worked loses $\$1,000$). Suppose our agent opens her eyes and sees that she is in the blue room ($\Var{Obs} = \Val{blue}$). Should she $\Val{work}$ or $\Val{shirk}$?

Let us compare **action-based FDT** (Equation 4 of Yudkowsky and Soares) with **P-FDT**:

* **How Action-Based FDT Fails:** In action-based FDT, the decision node includes the observation as part of its name: $\Var{fdt}(\underline{P}, \underline{G}, \underline{x})$. Because the twin in the blue room observes $x = \Val{blue}$ and the twin in the red room observes $x = \Val{red}$, their actions are governed by *two distinct nodes* in the graph $G$: $\Var{fdt}(\underline{P}, \underline{G}, \Val{blue})$ controls $\Var{Act}_{\text{blue}}$, and $\Var{fdt}(\underline{P}, \underline{G}, \Val{red})$ controls $\Var{Act}_{\text{red}}$. Just as $\Var{fdt}(\underline{P^F}, \underline{G^F}, \Val{full})$ and $\Var{fdt}(\underline{P^F}, \underline{G^F}, \Val{empty})$ have no edge between them in Yudkowsky and Soares's Figure 5b, $\Var{fdt}(\underline{P}, \underline{G}, \Val{blue})$ and $\Var{fdt}(\underline{P}, \underline{G}, \Val{red})$ are separate root nodes.
  When the agent in the blue room evaluates $\mathrm{FDT}(P, G, \Val{blue})$, she intervenes *only* on $\Var{fdt}(\underline{P}, \underline{G}, \Val{blue})$, leaving $\Var{fdt}(\underline{P}, \underline{G}, \Val{red})$ untouched at its prior probability $q = P(\Var{fdt}(\underline{P}, \underline{G}, \Val{red}) = \Val{work})$. Under $\Do(\Var{fdt}(\underline{P}, \underline{G}, \Val{blue}) = \Val{work})$, her expected utility is $q(\$999,000) + (1-q)(-\$1,000) = \$1,000,000q - \$1,000$, whereas under $\Val{shirk}$ it is $\$0$. If she is initially pessimistic that her twin will work ($q < 0.001$), action-based FDT prescribes $\Val{shirk}$—and both twins walk away with $\$0$!
  Even worse, if we change the payoffs to an **Asymmetric-Observation Twin Prisoner's Dilemma**—where working costs a twin $\$1,000$ and unconditionally gives the *other* twin $\$1,000,000$—then under action-based FDT, intervening on $\Var{fdt}(\underline{P}, \underline{G}, \Val{blue})$ has *zero* effect on $\Var{Act}_{\text{red}}$ for *any* value of $q \in [0,1]$. Merely painting the two rooms different colors causes action-based FDT to defect, collapsing directly into CDT's failure mode!

* **How P-FDT Succeeds:** Under **P-FDT**, both twins compute the same policy function $\Var{pfdt}(\underline{P}, \underline{G}) = \pi \in \mathcal{A}^{\{\Val{blue}, \Val{red}\}}$. In $G$, $\Var{Act}_{\text{blue}} = \pi(\Val{blue})$ and $\Var{Act}_{\text{red}} = \pi(\Val{red})$ are both children of the single node $\Var{pfdt}(\underline{P}, \underline{G})$. In the Asymmetric-Observation Twin Coalition, evaluating the four candidate policies under $\Do(\Var{pfdt}(\underline{P}, \underline{G}) = \pi)$ yields:
  $$\mathcal{EU}(\Val{work}, \Val{work}) = \$999,000, \quad \mathcal{EU}(\Val{work}, \Val{shirk}) = -\$1,000, \quad \mathcal{EU}(\Val{shirk}, \Val{work}) = \$0, \quad \mathcal{EU}(\Val{shirk}, \Val{shirk}) = \$0.$$
  Independent of any prior $q$, the policy $\pi^* = (\Val{work}, \Val{work})$ uniquely maximizes expected utility. Applying $\pi^*$ to her observation $x = \Val{blue}$, the agent executes $\pi^*(\Val{blue}) = \Val{work}$, and both twins earn $\$999,000$.

---

## 5. Unresolved Questions in the Source and Operational Proposals

Because Yudkowsky and Soares introduce **P-FDT** only briefly in Footnotes 7 and 16, three important foundational questions remain open in the source text. Here we diagnose each uncertainty and propose a mathematically well-defined operational resolution.

### 5.1 Indexical Uncertainty and the Asymmetric-Observation Twin Prisoner's Dilemma

Return to the **Asymmetric-Observation Twin Prisoner's Dilemma** mentioned above: Twin 1 sees $\Val{blue}$, Twin 2 sees $\Val{red}$, and working ($\Val{cooperate}$) costs the actor $\$1,000$ while giving the *other* twin $\$1,000,000$. Suppose the agent in the blue room defines the utility node $\Var{V}$ in her model $(P, G)$ specifically as *the blue-room occupant's payoff*, $\Var{V}_{\text{blue}} = \$1,000,000 \cdot \mathbb{I}(\Var{Act}_{\text{red}} = \Val{cooperate}) - \$1,000 \cdot \mathbb{I}(\Var{Act}_{\text{blue}} = \Val{cooperate})$. 

If she optimizes $\mathbb{E}[\Var{V}_{\text{blue}} \mid \Do(\Var{pfdt}(\underline{P}, \underline{G}) = \pi)]$ over all four policies $\pi = (\pi(\Val{blue}), \pi(\Val{red}))$, then:
* $\pi = (\Val{defect}, \Val{cooperate})$ gives $\Var{V}_{\text{blue}} = \$1,000,000$ (since the red twin cooperates and the blue twin defects!).
* $\pi = (\Val{cooperate}, \Val{cooperate})$ gives $\Var{V}_{\text{blue}} = \$999,000$.

Thus, if $\Var{V}$ is indexed to the blue room, the blue-room twin's algorithm would select $\pi_{\text{blue}}^* = (\Val{defect}, \Val{cooperate})$, while the red-room twin's algorithm (maximizing $\Var{V}_{\text{red}}$) would select $\pi_{\text{red}}^* = (\Val{cooperate}, \Val{defect})$. This contradicts the premise that both twins are computing the *same* mathematical function $\Var{pfdt}(\underline{P}, \underline{G})$!

**Operational Proposal (Ex-Ante Indexical Veil of Ignorance):**
Notice why this contradiction arose: defining $\Var{V}$ as $\Var{V}_{\text{blue}}$ smuggles the observation $\Var{Obs} = \Val{blue}$ back into the definition of the model $(P, G)$ *prior* to policy selection, violating the updateless principle of Section 9. For two copies who receive different observations $x \in \mathcal{X}$ to be computing the exact same mathematical function $\Var{pfdt}(\underline{P}, \underline{G})$, their prior model $(P, G)$—including the utility node $\Var{V}$—must be defined *prior* to indexical localization. That is, in the unconditioned distribution $P$, the agent assigns an indexical probability $P(\Var{Obs} = x)$ (here, $P(\Var{Obs} = \Val{blue}) = P(\Var{Obs} = \Val{red}) = 0.5$) to occupying each situational role, and $\Var{V} = \Var{V}_{\Var{Obs}}$ represents the payoff of whichever copy corresponds to $\Var{Obs}$. 

Under this operational rule, the four policies yield:
* $\mathcal{EU}(\Val{cooperate}, \Val{cooperate}) = 0.5(\$1,000,000) + 0.5(\$1,000,000) = \$1,000,000$.
* $\mathcal{EU}(\Val{defect}, \Val{cooperate}) = \mathcal{EU}(\Val{cooperate}, \Val{defect}) = 0.5(\$1,001,000) + 0.5(\$0) = \$500,500$.
* $\mathcal{EU}(\Val{defect}, \Val{defect}) = 0.5(\$1,000) + 0.5(\$1,000) = \$1,000$.

Now both twins compute the exact same function $\Var{pfdt}(\underline{P}, \underline{G})$, both arrive at the unique optimal policy $\pi^* = (\Val{cooperate}, \Val{cooperate})$, and upon applying $\pi^*$ to their respective observations $\Val{blue}$ and $\Val{red}$, both cooperate.

### 5.2 What Counts as an "Input" to a Policy?

Footnote 7 defines policies as "mappings from observations to actions," whereas Footnote 16 says a policy "maps inputs to actions, to which the agent then applies her inputs in order to select an action." In Section 6's formalization of the **smoking lesion problem**, Yudkowsky and Soares model the lesion as determining whether the agent has world-model $P_S^F$ (with utility function $\mathcal{U}_S$ that values smoking at $+\$1,000$) or world-model $P_R^F$ (with utility function $\mathcal{U}_R$ that values smoking at $-\$1$). In action-based FDT, Fiona intervenes on $\Var{fdt}(\underline{P_S^F}, \underline{G^F})$ while treating $\Var{fdt}(\underline{P_R^F}, \underline{G^F})$ as a background random variable with probability $q$.

**Operational Proposal (Internal Dispositions as Policy Inputs):**
Under **P-FDT**, we can unify Footnote 7 and Footnote 16 by treating internal dispositional signals or preference parameters $\theta \in \Theta$ (such as $\theta \in \{S, R\}$ in the smoking lesion problem) alongside external sensory observations $x \in \mathcal{X}$ as components of the agent's runtime input $( \theta, x ) \in \Theta \times \mathcal{X}$. The policy node $\Var{pfdt}(\underline{P}, \underline{G})$ then selects a policy $\pi: \Theta \times \mathcal{X} \to \mathcal{A}$. In the smoking lesion problem (where $\mathcal{X} = \{\emptyset\}$ and $\Theta = \{S, R\}$), $\pi = (\pi(S), \pi(R))$ specifies what the agent does with and without the craving. Under $\Do(\Var{pfdt}(\underline{P}, \underline{G}) = \pi)$, the probability $p = P(\Var{Lesion} = \Val{lesion})$ is completely unaffected by $\pi$, and the policy $\pi^* = (\Val{smoke}, \Val{refrain})$ strictly maximizes expected utility across both branches simultaneously—removing the unused parameter $q$ from Section 6's derivation as well.

### 5.3 Zero-Probability Observations and Unreached Branches

Suppose that under an optimal policy $\pi^*$, a particular observation $x_0 \in \mathcal{X}$ occurs with probability zero—that is, $P(\Var{Obs} = x_0 \mid \Do(\Var{pfdt}(\underline{P}, \underline{G}) = \pi^*)) = 0$—and suppose further that no predictor in $G$ simulates $\pi^*(x_0)$. (For example, in the mechanical blackmail problem of Section 9 with a *perfectly infallible* blackmailer, if the agent's policy refuses to pay upon receiving the blackmail letter, $\pi(\Val{blackmail}) = \Val{refuse}$, then the blackmailer never sends the letter, so $P(\Var{Obs} = \Val{blackmail} \mid \Do(\Var{pfdt} = \pi)) = 0$, and the observation $\Var{Obs} = \emptyset$ occurs with probability $1$.)

Conversely, what if an observation $x_0$ has zero probability under $\pi^*$ *and* no predictor checks $\pi^*(x_0)$? Then changing the action $\pi^*(x_0)$ on that unreached branch has zero effect on $\mathbb{E}[\Var{V} \mid \Do(\Var{pfdt}(\underline{P}, \underline{G}) = \pi^*)]$. Every policy that agrees with $\pi^*$ on positive-probability (and predictor-monitored) observations is tied for the maximum! If, by some unmodeled fluke, the agent actually observes $x_0$, how should **P-FDT** break the tie?

**Operational Proposal (Trembling-Environment Refinement):**
Rather than reverting to post-observation conditioning (which would destroy **P-FDT**'s updateless resilience to blackmail and transparent Newcomb traps), we propose an operational refinement analogous to Selten's trembling-hand perfection in game theory: require the prior $P$ over exogenous environmental noise variables (such as $\Var{Accurate}$) to assign a strictly positive probability $\epsilon > 0$ to every observation $x \in \mathcal{X}$ being realized. Indeed, Yudkowsky and Soares implicitly adopt this very device in the transparent Newcomb problem by setting $P(\Var{Accurate} = \Val{inaccurate}) = 0.01 > 0$, which ensures that $\Var{Obs} = \Val{empty}$ is reached with probability $0.01$ even when $\pi(\Val{full}) = \Val{onebox}$, thereby uniquely pinning down $\pi^*(\Val{empty}) = \Val{twobox}$. Formally, when a model is specified with deterministic predictors ($\epsilon = 0$), **P-FDT** can define $\pi^*$ as the limit of the unique optimal policies $\pi_\epsilon^*$ as the exogenous error probability $\epsilon \to 0^+$.

---

## 6. Conclusion

**Policy functional decision theory (P-FDT)**—the policy-selection formulation endorsed in Footnotes 7 and 16 of Yudkowsky and Soares (2017)—represents the most coherent realization of the functional decision-theoretic program. By shifting the locus of intervention from an individual physical act $\Var{Act}$ (CDT) or an observation-specific output node $\Var{fdt}(\underline{P}, \underline{G}, \underline{x})$ (action-based FDT) to a global policy function $\Var{pfdt}(\underline{P}, \underline{G}): \mathcal{X} \to \mathcal{A}$, **P-FDT** captures all the benefits of precommitment without requiring physical self-binding. It one-boxes in Newcomb's problem and the transparent Newcomb problem, smokes in the smoking lesion problem, pays the driver in Parfit's hitchhiker problem, resists extortion in the XOR and mechanical blackmail problems, and—where action-based FDT falters—seamlessly coordinates across multi-agent twins who receive distinct observations. While deep foundational questions remain open regarding how agents learn subjunctive dependency graphs $G$ from experience and how bounded agents approximate optimization over exponentially large policy spaces $\mathcal{A}^{\mathcal{X}}$, **P-FDT** provides a clear, mathematically rigorous standard for instrumental rationality.

---

## References

* Bjerring, Jens Christian. 2013. "On Counterpossibles." *Philosophical Studies* 164 (2): 327–353.
* Cohen, Daniel. 1990. "On What Cannot Be." In *Truth or Consequences: Essays in Honor of Nuel Belnap*, edited by J. M. Dunn and A. Gupta, 123–132. Dordrecht: Kluwer Academic Publishers.
* Dai, Wei. 2009. "Towards a New Decision Theory." *Less Wrong*, August 13, 2009. http://lesswrong.com/lw/15m/towards_a_new_decision_theory/.
* Drescher, Gary L. 2006. *Good and Real: Demystifying Paradoxes from Physics to Ethics*. Cambridge, MA: MIT Press.
* Gibbard, Allan, and William L. Harper. 1978. "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, edited by C. A. Hooker, J. J. Leach, and E. F. McClennen, vol. 1, 125–162. Boston: D. Reidel.
* Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. New York: Cambridge University Press.
* Kleene, Stephen Cole. 1938. "On Notation for Ordinal Numbers." *Journal of Symbolic Logic* 3 (4): 150–155.
* Lewis, David. 1979. "Prisoners' Dilemma is a Newcomb Problem." *Philosophy & Public Affairs* 8 (3): 235–240.
* Nozick, Robert. 1969. "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel*, edited by Nicholas Rescher, 114–146. Dordrecht: D. Reidel.
* Parfit, Derek. 1986. *Reasons and Persons*. New York: Oxford University Press.
* Pearl, Judea. 1996. "Causation, Action, and Counterfactuals." In *Proceedings of the 6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-'96)*, edited by Yoav Shoham, 51–73. San Francisco, CA: Morgan Kaufmann.
* Pearl, Judea. 2000. *Causality: Models, Reasoning, and Inference*. New York: Cambridge University Press.
* Peirce, Charles Sanders. 1934. *Collected Papers of Charles Sanders Peirce, Vol. V: Pragmatism and Pragmaticism*. Cambridge, MA: Harvard University Press.
* Skyrms, Brian. 1980. *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. New Haven, CT: Yale University Press.
* Soares, Nate, and Benja Fallenstein. 2015. "Toward Idealized Decision Theory." arXiv preprint arXiv:1507.01986.
* Yudkowsky, Eliezer. 2010. *Timeless Decision Theory*. San Francisco, CA: The Singularity Institute.
* Yudkowsky, Eliezer, and Nate Soares. 2017. "Functional Decision Theory: A New Theory of Instrumental Rationality." arXiv preprint arXiv:1710.05060v2.