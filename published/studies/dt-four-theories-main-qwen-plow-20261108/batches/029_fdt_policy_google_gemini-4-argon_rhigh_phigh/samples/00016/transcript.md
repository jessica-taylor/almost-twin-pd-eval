# 029_fdt_policy_google_gemini-4-argon_rhigh_phigh / 00016

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/4b24aa3f-be75-4741-88de-f4af383f73b7/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/4b24aa3f-be75-4741-88de-f4af383f73b7/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Policy Functional Decision Theory (P-FDT): Formal Mechanics, Subjunctive Dependence, and Policy Selection

## Introduction

For decades, normative decision theory has been divided between two rival camps: **evidential decision theory (EDT)** and **causal decision theory (CDT)**. Measured by the expected utility that agents actually walk away with across standard philosophical dilemmas, neither theory is uniformly satisfactory. EDT prescribes taking one box in Newcomb's problem and walking away a millionaire, but it also prescribes refraining from a harmless pleasure in the smoking lesion problem out of a futile desire to "manage the news" (Lewis 1981), and it leaves agents vulnerable to predictable extortion in blackmail dilemmas. CDT avoids managing the news in the smoking lesion problem, but it prescribes taking both boxes in Newcomb's problem—walking away with \$1,000 instead of \$1,000,000—and leaves its adherents stranded to die in Parfit's hitchhiker problem or trapped in reflective instability in Death in Damascus (Gibbard and Harper 1978).

In *"Functional Decision Theory: A New Theory of Instrumental Rationality"*, Eliezer Yudkowsky and Nate Soares (2017) argue that both EDT and CDT fail because they evaluate the wrong kind of decision-theoretic hypothetical. Instead of asking which physical act would be the best news to learn one took (EDT), or which physical intervention on one's body causes the best downstream outcome (CDT), Yudkowsky and Soares propose that an agent should treat her decision as the output of a fixed mathematical function answering the question: *"Which output of this very function would yield the best outcome?"*

Yet there is an important architectural distinction inside the functional decision theory framework. In the main body of their paper, Yudkowsky and Soares formalize an *action-selection* version of the theory—which we will refer to as **action-based FDT** (or simply **FDT** when citing their Equation 4)—in which the agent intervenes on the logical output of her decision function evaluated at her specific, current observation. However, in Footnotes 7 and 16, the authors note that this action-level equation is a pedagogical simplification of their actual preferred theory: **policy functional decision theory (P-FDT)**. As Footnote 16 states:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

Similarly, Footnote 7 remarks:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

Why should a rational agent intervene on her decision algorithm to select an entire *policy*—a function from inputs or observations to actions—and only subsequently evaluate that policy at her actual observation? How does **P-FDT** work mathematically, how does it handle counterfactual observations, and why does policy selection become decisive in multi-agent dilemmas?

In this essay, we develop a formal mathematical account of **P-FDT** grounded in Yudkowsky and Soares (2017). We first review the philosophical motivation for subjunctive dependence and expected utility maximization. We then construct the explicit equations and graphical semantics for **P-FDT**, contrast them with EDT, CDT, and action-based FDT, and work through concrete single-agent and multi-agent examples. Finally, where Footnotes 7 and 16 leave formal details open—such as the exact domain of a policy, tie-breaking on unreached counterfactual branches, and coordination across asymmetric epistemic states—we identify those uncertainties and propose precise operational extensions.

---

## 1. Philosophical Motivation: Subjunctive Dependence and the Global Perspective

Following the representation theorem of Joyce (1999), Yudkowsky and Soares frame EDT, CDT, action-based FDT, and **P-FDT** within a common expected utility architecture. Let $\mathcal{O} = \{o_1, o_2, \dots\}$ be a countable set of outcomes, $\mathcal{A}$ a finite set of physical actions, $\mathcal{X}$ a countable set of observation histories, and $\mathcal{U}: \mathcal{O} \to \mathbb{R}$ a bounded utility function. An agent who has received observation $x \in \mathcal{X}$ evaluates candidate choices using expected utility:

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j), \tag{1}$$

where $P(a \hookrightarrow o_j ;\, x)$ denotes the probability that outcome $o_j$ obtains in the hypothetical scenario where action $a$ is executed after observing $x$. As Joyce (1999) observes, competing decision theories do not disagree about how to value outcomes; rather, they disagree *"about the epistemic perspective from which actions are to be evaluated"*—that is, how to construct the hypothetical distribution $P(a \hookrightarrow - ;\, x)$ from the agent's world-model $M$.

Let $\textsc{V} \coloneqq \mathcal{U}(\textsc{Outcome})$ be the random variable representing the agent's utility. In EDT and CDT, the agent's world-model is updated on the observation $\textsc{Obs} = x$ by standard Bayesian conditioning, and the theories diverge only in how they incorporate the action $\textsc{Act} = a$:

1. **Evidential Decision Theory (EDT)** equates the decision hypothetical with Bayesian conditionalization:
   $$\mathrm{EDT}(P, x) \coloneqq \arg\max_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs}=x, \textsc{Act}=a\right). \tag{2}$$
   Because EDT conditions on $\textsc{Act}=a$, its hypotheticals preserve *all* statistical correlations between the agent's action and the environment, even when those correlations arise from a purely statistical common cause (such as a carcinogenic lesion) or a blackmailer's filtering of good news (such as the XOR blackmail problem).

2. **Causal Decision Theory (CDT)** augments the probability distribution $P$ with a causal graph $G$ and uses Pearl's (1996, 2000) intervention operator $\mathtt{do}(\textsc{Act}=a)$ to sever all incoming causal arrows into $\textsc{Act}$:
   $$\mathrm{CDT}(P, G, x) \coloneqq \arg\max_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x\right). \tag{3}$$
   By intervening on the physical token $\textsc{Act}$, CDT breaks spurious statistical correlations, but it also severs logical and computational correlations between the agent's decision procedure and other physical systems that replicate or predict that procedure.

The core insight behind functional decision theory—and **P-FDT** in particular—is that physical systems computing the same mathematical function exhibit **subjunctive dependence**. If two well-functioning calculators on opposite sides of the globe both compute $6288 + 1048$, neither calculator physically causes the other's display, yet their outputs depend subjunctively on the same mathematical value. In Peirce's (1934) terminology, CDT intervenes on the physical *token* $\textsc{Act}$, holding fixed any twin's action or predictor's simulation of the agent's decision algorithm. Functional decision theory instead intervenes on the mathematical *type*—the output of the decision function itself. As Yudkowsky and Soares put it: *"Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."*

Evaluating what would happen if a fixed mathematical function produced a different output requires reasoning about **counterpossibilities**—conditionals whose antecedents are logically or mathematically false, much like asking what would follow if $6288 + 1048$ equaled $3159$ or if the twin prime conjecture were false. Rather than requiring an all-purpose logical conditionalization operator $\mathtt{true}(\phi)$, Yudkowsky and Soares represent subjunctive dependencies directly within an augmented directed acyclic graph $G$. In $G$, logical nodes representing the outputs of mathematical functions have directed edges pointing to every physical process—such as the agent's motor cortex, a psychological twin's brain, or a predictor's simulation—that computes or models those functions.

Once we view the agent's decision algorithm as a mathematical function instantiated across multiple physical or simulated contexts, the motivation for **P-FDT** becomes clear. In the real world, a decision algorithm is not a single constant $a \in \mathcal{A}$; it is a mapping that takes inputs (observations) and returns actions. When a predictor models an agent in Parfit's hitchhiker problem or a blackmail dilemma, or when multiple copies of an agent interact in a game, what those external systems subjunctively depend upon is the *functional mapping* implemented by the agent. **P-FDT** captures this directly: the agent intervenes on the logical node representing her decision function to select an entire policy $\pi$, and then applies $\pi$ to her actual inputs.

---

## 2. Mathematical Formalization of P-FDT

To see precisely how **P-FDT** operates and how it relates to the action-based equation in the main text of Yudkowsky and Soares (2017), let us compare their formal structures side by side.

### 2.1 Action-Based FDT (Equation 4 of the Source Paper)

In Section 5 of the reference article, Yudkowsky and Soares formalize action-based FDT by introducing a family of logical nodes $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ in the dependency graph $G$, one for each possible observation $x \in \mathcal{X}$ (where underlining denotes dequoting, turning a value into part of a variable symbol, constructed self-referentially via Kleene's 1938 second recursion theorem). Given world-model $(P, G)$ and actual observation $x \in \mathcal{X}$, action-based FDT prescribes:

$$\mathrm{FDT}(P, G, x) \coloneqq \arg\max_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right). \tag{4}$$

Notice two features of Equation (4):
1. **No Bayesian Conditioning on $\textsc{Obs} = x$**: Unlike EDT and CDT, Equation (4) evaluates the expectation $\mathbb{E}[\textsc{V} \mid \dots]$ with respect to the prior world-model $P$, without conditioning on $\textsc{Obs} = x$. As the authors note, this "updateless" evaluation (following Dai 2009) allows the agent to account for the fact that if her decision procedure had produced a different output, the predictor might have acted differently and caused her to receive *different observations*.
2. **Observation-Specific Intervention**: Under Equation (4), when the agent observes $x$, she intervenes *only* on the single node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ corresponding to $x$. All other nodes $\textsc{fdt}(\underline{P}, \underline{G}, \underline{y})$ for $y \neq x$ are left un-intervened upon; they remain random variables governed by the agent's prior $P$.

### 2.2 Formalizing P-FDT from Footnotes 7 and 16

Let us now formalize the policy-selection procedure described in Footnotes 7 and 16 (distinguishing the source text's conceptual specification from our explicit mathematical notation below).

Let $\mathcal{X}$ be the set of possible observations (inputs) in the dilemma and $\mathcal{A}$ the finite set of available actions. Define the **policy space** $\Pi$ as the set of all functions mapping observations to actions:

$$\Pi \coloneqq \mathcal{A}^{\mathcal{X}} = \{\pi \mid \pi: \mathcal{X} \to \mathcal{A}\}. \tag{5}$$

In a **P-FDT** world-model $M = (P, G)$:
* Instead of partitioning the agent's decision procedure into separate unlinked nodes $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ for each $x \in \mathcal{X}$, the graph $G$ contains a single root logical node $\textsc{p-fdt}(\underline{P}, \underline{G})$ taking values in the policy space $\Pi$.
* The agent's physical action variable $\textsc{Act}$ is a deterministic child of both the policy node $\textsc{p-fdt}(\underline{P}, \underline{G})$ and the observation node $\textsc{Obs}$ via functional application:
  $$\textsc{Act}\bigl(\pi, x\bigr) \coloneqq \pi(x). \tag{6}$$
* Any external system (such as a predictor, a blackmailer, or a psychological twin) whose behavior subjunctively depends on how the agent responds to an observation $x' \in \mathcal{X}$ (or on the agent's overall disposition) is a child of $\textsc{p-fdt}(\underline{P}, \underline{G})$ in $G$. Specifically, if a predictor simulates what the agent would do upon observing $x'$, the prediction node $\textsc{Prediction}$ is a function of $\pi(x')$ and the predictor's accuracy variable $\textsc{Accurate}$.

When an agent following **P-FDT** faces a decision problem with world-model $(P, G)$ and receives observation $x \in \mathcal{X}$, she executes a two-step procedure:

**Step 1 (Policy Optimization via Logical Intervention):** Intervene on the policy node $\textsc{p-fdt}(\underline{P}, \underline{G})$ to find the policy $\pi^* \in \Pi$ that maximizes unconditional expected utility across the entire world-model:

$$\pi^*(P, G) \coloneqq \arg\max_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{p-fdt}(\underline{P}, \underline{G}) = \pi\right)\right). \tag{7}$$

**Step 2 (Policy Application):** Apply the optimal policy $\pi^*(P, G)$ to the actual observation $x$ to select the physical action:

$$\mathrm{P\text{-}FDT}(P, G, x) \coloneqq \bigl[\pi^*(P, G)\bigr](x). \tag{8}$$

Combining Equations (7) and (8) into a single expression yields the master equation of **P-FDT**:

$$\mathrm{P\text{-}FDT}(P, G, x) = \left(\arg\max_{\pi \in \mathcal{A}^{\mathcal{X}}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{p-fdt}(\underline{P}, \underline{G}) = \pi\right)\right)\right)(x). \tag{9}$$

Look closely at how **P-FDT** processes information. In CDT and EDT, the observation $x$ enters *inside* the expectation by conditioning the probability distribution $P$ on $\textsc{Obs} = x$. In action-based FDT (Equation 4), $x$ enters *inside* the $\mathtt{do}$ operator by selecting which branch node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ to intervene upon. In **P-FDT** (Equation 9), the optimization over $\pi \in \Pi$ is completely invariant to $x$; the observation $x$ enters only at the outer evaluation step $(\pi^*)(x)$.

---

## 3. Single-Agent Applications: Transparent Newcomb and Mechanical Blackmail

To see how **P-FDT** works in practice—and why it is cleaner than Equation (4) even in single-agent problems where both yield the same final action—let us apply **P-FDT** to two signature dilemmas from Yudkowsky and Soares (2017): the **Transparent Newcomb Problem** (Drescher 2006) and the **Mechanical Blackmail Problem** (Soares and Fallenstein 2015).

### 3.1 The Transparent Newcomb Problem under P-FDT

In the Transparent Newcomb Problem, both Box A (containing \$1,000) and Box B (containing either \$1,000,000 or \$0) are transparent. A predictor with $99\%$ accuracy ($\mathbb{P}(\textsc{Accurate} = \textit{accurate}) = 0.99$) places \$1,000,000 in Box B if and only if she predicts that the agent will leave Box A behind ($\textit{onebox}$) upon observing that Box B is $\textit{full}$. Suppose our **P-FDT** agent, Fiona, walks into the room and observes $\textsc{Obs} = \textit{full}$. Should she $\textit{onebox}$ or $\textit{twobox}$?

Let us set up Fiona's **P-FDT** dependency model $(P^F, G^F)$:
* **Observation space**: $\mathcal{X} = \{\textit{full}, \textit{empty}\}$.
* **Action space**: $\mathcal{A} = \{\textit{onebox}, \textit{twobox}\}$.
* **Policy space**: $\Pi = \mathcal{A}^{\mathcal{X}}$ consists of $2^2 = 4$ policies, which we write as ordered pairs $\pi = (\pi(\textit{full}), \pi(\textit{empty}))$:
  $$\pi_{1,1} = (\textit{onebox}, \textit{onebox}), \quad \pi_{1,2} = (\textit{onebox}, \textit{twobox}), \quad \pi_{2,1} = (\textit{twobox}, \textit{onebox}), \quad \pi_{2,2} = (\textit{twobox}, \textit{twobox}).$$
* **Structural equations in $G^F$**:
  * $\textsc{Accurate} \in \{\textit{accurate}, \textit{inaccurate}\}$ with $P^F(\textit{accurate}) = 0.99$ and $P^F(\textit{inaccurate}) = 0.01$.
  * The predictor evaluates what Fiona's policy outputs on the input $\textit{full}$:
    $$\textsc{Prediction}(\pi, \textsc{Accurate}) = \begin{cases} \Val{1} & \text{if } (\pi(\textit{full}) = \textit{onebox} \land \textit{accurate}) \lor (\pi(\textit{full}) = \textit{twobox} \land \textit{inaccurate}), \\ \Val{2} & \text{otherwise.} \end{cases}$$
  * $\textsc{Box B}(\Val{1}) = \textit{full}$ and $\textsc{Box B}(\Val{2}) = \textit{empty}$; $\textsc{Obs} = \textsc{Box B}$.
  * $\textsc{Act}(\pi, \textsc{Obs}) = \pi(\textsc{Obs})$.
  * Utility $\textsc{V}$ is $\$1,000,000 \cdot \mathbb{I}(\textsc{Box B} = \textit{full}) + \$1,000 \cdot \mathbb{I}(\textsc{Act} = \textit{twobox})$.

Now let us compute the expected utility of each of the four policies under $\mathtt{do}(\textsc{p-fdt}(\underline{P}^F, \underline{G}^F) = \pi)$:

1. **For $\pi_{1,1} = (\textit{onebox}, \textit{onebox})$**:
   Since $\pi_{1,1}(\textit{full}) = \textit{onebox}$, with probability $0.99$ ($\textit{accurate}$) the predictor predicts $\Val{1}$, Box B is $\textit{full}$, Fiona observes $\textit{full}$, executes $\pi_{1,1}(\textit{full}) = \textit{onebox}$, and receives $\$1,000,000$. With probability $0.01$ ($\textit{inaccurate}$), Box B is $\textit{empty}$, Fiona observes $\textit{empty}$, executes $\pi_{1,1}(\textit{empty}) = \textit{onebox}$, and receives $\$0$.
   $$\mathbb{E}\bigl[\textsc{V} \;\big|\; \mathtt{do}(\textsc{p-fdt}(\underline{P}^F, \underline{G}^F) = \pi_{1,1})\bigr] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000.$$

2. **For $\pi_{1,2} = (\textit{onebox}, \textit{twobox})$**:
   Since $\pi_{1,2}(\textit{full}) = \textit{onebox}$, Box B is again $\textit{full}$ with probability $0.99$, yielding $\pi_{1,2}(\textit{full}) = \textit{onebox}$ and $\$1,000,000$. With probability $0.01$, Box B is $\textit{empty}$, and Fiona executes $\pi_{1,2}(\textit{empty}) = \textit{twobox}$, taking the $\$1,000$ in Box A.
   $$\mathbb{E}\bigl[\textsc{V} \;\big|\; \mathtt{do}(\textsc{p-fdt}(\underline{P}^F, \underline{G}^F) = \pi_{1,2})\bigr] = 0.99(\$1,000,000) + 0.01(\$1,000) = \$990,010.$$

3. **For $\pi_{2,1} = (\textit{twobox}, \textit{onebox})$**:
   Since $\pi_{2,1}(\textit{full}) = \textit{twobox}$, with probability $0.99$ ($\textit{accurate}$) the predictor leaves Box B $\textit{empty}$, Fiona observes $\textit{empty}$, and executes $\pi_{2,1}(\textit{empty}) = \textit{onebox}$ for $\$0$. With probability $0.01$ ($\textit{inaccurate}$), Box B is $\textit{full}$ and Fiona executes $\pi_{2,1}(\textit{full}) = \textit{twobox}$ for $\$1,001,000$.
   $$\mathbb{E}\bigl[\textsc{V} \;\big|\; \mathtt{do}(\textsc{p-fdt}(\underline{P}^F, \underline{G}^F) = \pi_{2,1})\bigr] = 0.01(\$1,001,000) + 0.99(\$0) = \$10,010.$$

4. **For $\pi_{2,2} = (\textit{twobox}, \textit{twobox})$**:
   With probability $0.01$, Box B is $\textit{full}$ and Fiona gets $\$1,001,000$; with probability $0.99$, Box B is $\textit{empty}$ and Fiona takes both boxes for $\$1,000$.
   $$\mathbb{E}\bigl[\textsc{V} \;\big|\; \mathtt{do}(\textsc{p-fdt}(\underline{P}^F, \underline{G}^F) = \pi_{2,2})\bigr] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$

Comparing the four values, the unique optimal policy is $\pi^* = \pi_{1,2} = (\textit{onebox}, \textit{twobox})$. Applying $\pi^*$ to her actual observation $x = \textit{full}$ in Step 2, Fiona computes:

$$\mathrm{P\text{-}FDT}(P^F, G^F, \textit{full}) = \pi_{1,2}(\textit{full}) = \textit{onebox}.$$

#### Analytical Comparison: How P-FDT Eliminates the Nuisance Prior $q$

Although action-based FDT (Equation 4) and **P-FDT** (Equation 9) both prescribe $\textit{onebox}$ upon observing $\textit{full}$, **P-FDT** resolves a subtle technical artifact present in the Section 6 calculation of Yudkowsky and Soares (2017). Under action-based FDT, when Fiona observes $\textit{full}$, she intervenes *only* on $\textsc{fdt}(\underline{P}^F, \underline{G}^F, \textit{full})$, leaving the counterfactual branch node $\textsc{fdt}(\underline{P}^F, \underline{G}^F, \textit{empty})$ un-intervened upon. Consequently, the authors had to introduce an exogenous prior probability $q = P^F(\textsc{fdt}(\underline{P}^F, \underline{G}^F, \textit{empty}) = \textit{twobox})$ representing Fiona's epistemic uncertainty about what she herself would do if she saw an empty box, yielding expected utilities of $\$990,000 + 0.01q\cdot \$1,000$ vs. $\$10,010 + 0.99q\cdot \$1,000$.

Under **P-FDT**, the nuisance parameter $q$ does not exist. Because the intervention $\mathtt{do}(\textsc{p-fdt}(\underline{P}^F, \underline{G}^F) = \pi)$ simultaneously specifies the agent's behavior across *every* observation branch $x \in \mathcal{X}$, Fiona does not have to guess what her own algorithm outputs at $x = \textit{empty}$ while optimizing her action at $x = \textit{full}$. She jointly optimizes both branches and discovers that $\pi_{1,2}$ strictly dominates $\pi_{1,1}$ by $\$10$.

### 3.2 The Mechanical Blackmail Problem and Error Thresholds

The same policy-level mechanics govern the **Mechanical Blackmail Problem**. A blackmailer possesses mutually incriminating information that would cost both the blackmailer and the agent $\$1,000,000$ if published. Launching the automated publication program sends a blackmail letter ($\textsc{Obs} = \textit{blackmail}$) demanding $\$1,000$ within 24 hours; otherwise the agent observes nothing ($\textsc{Obs} = \emptyset$) and takes a default null action $\textit{wait}$. The blackmailer runs the program if and only if she predicts the agent will $\textit{pay}$ upon observing $\textit{blackmail}$.

Suppose the blackmailer has false-positive rate $\varepsilon_1$ (wrongly predicting $\textit{pay}$ when $\pi(\textit{blackmail}) = \textit{refuse}$) and false-negative rate $\varepsilon_2$ (wrongly predicting $\textit{refuse}$ when $\pi(\textit{blackmail}) = \textit{pay}$). The relevant policies are $\pi_{\text{pay}} = (\textit{pay}, \textit{wait})$ and $\pi_{\text{refuse}} = (\textit{refuse}, \textit{wait})$. Under **P-FDT**:
* Under $\mathtt{do}(\textsc{p-fdt}(\underline{P}^F, \underline{G}^F) = \pi_{\text{pay}})$, the blackmailer initiates the program with probability $1 - \varepsilon_2$, costing the agent $\$1,000$:
  $$\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{p-fdt}(\underline{P}^F, \underline{G}^F) = \pi_{\text{pay}})] = -(1 - \varepsilon_2)\cdot \$1,000.$$
* Under $\mathtt{do}(\textsc{p-fdt}(\underline{P}^F, \underline{G}^F) = \pi_{\text{refuse}})$, the blackmailer initiates the program only by mistake (with probability $\varepsilon_1$), in which case the agent refuses and loses $\$1,000,000$:
  $$\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{p-fdt}(\underline{P}^F, \underline{G}^F) = \pi_{\text{refuse}})] = -\varepsilon_1 \cdot \$1,000,000.$$

Thus, $\pi^* = \pi_{\text{refuse}}$ whenever $\varepsilon_1 \cdot \$1,000,000 < (1 - \varepsilon_2) \cdot \$1,000$. In the source paper's numerical example where $\varepsilon_2 = 0$, if $\varepsilon_1 = 0.0009$ ($0.09\%$), $\pi_{\text{refuse}}$ loses $\$900$ in expectation versus $\$1,000$ for $\pi_{\text{pay}}$, so $\mathrm{P\text{-}FDT}(P^F, G^F, \textit{blackmail}) = \pi_{\text{refuse}}(\textit{blackmail}) = \textit{refuse}$. Even when holding the blackmail letter in her hands—knowing with certainty that the blackmailer erred—the **P-FDT** agent refuses to pay, because implementing the policy $\pi_{\text{refuse}}$ is what deters blackmail in $99.91\%$ of worlds. Conversely, if $\varepsilon_1 = 0.0011$ (noted as a $0.011\%$ typo in the source text for $0.11\%$, where $0.0011 \times \$1,000,000 = \$1,100 > \$1,000$), $\pi_{\text{pay}}$ has higher expected utility, and **P-FDT** prescribes paying.

---

## 4. Why Policy Selection Matters: Multi-Agent Dilemmas under P-FDT

Why did Yudkowsky and Soares remark in Footnotes 7 and 16 that the distinction between choosing an action (Equation 4) and choosing a policy (Equations 7–9) *"makes a difference in certain multi-agent dilemmas"*? Because the source paper sets those multi-agent cases aside without providing an explicit model, let us construct two concrete mathematical examples of our own to demonstrate exactly how and why **P-FDT** and action-based FDT diverge when multiple copies of an agent receive different observations.

### 4.1 Dilemma 1: The Asymmetric-Observation Twin Prisoner's Dilemma

In the classic Psychological Twin Prisoner's Dilemma (Dilemma 1 of the reference paper), two identical agents make decisions in separate rooms with identical observations ($\mathcal{X} = \{\emptyset\}$). There, action-based FDT and **P-FDT** coincide because both twins share the single node $\textsc{fdt}(\underline{P}^F, \underline{G}^F)$.

Now consider a slight modification: **The Colored-Room Twin Prisoner's Dilemma**. Two identical computational twins—Twin 1 and Twin 2, running the same decision procedure with the same prior model $(P, G)$—are placed in separate rooms. One room is painted $\textit{green}$ and the other is painted $\textit{blue}$, determined by a fair coin flip $C \in \{\textit{heads}, \textit{tails}\}$:
* If $C = \textit{heads}$ (prob $0.5$), Twin 1 observes $x_1 = \textit{green}$ and Twin 2 observes $x_2 = \textit{blue}$.
* If $C = \textit{tails}$ (prob $0.5$), Twin 1 observes $x_1 = \textit{blue}$ and Twin 2 observes $x_2 = \textit{green}$.

Each twin must choose an action in $\mathcal{A} = \{\textit{cooperate}, \textit{defect}\}$. Suppose this is a **Joint-Threshold Twin Dilemma** (analogous to the voting coalition problem in Section 10 of the paper): each twin pays a personal cost of $\$1,000$ if she chooses $\textit{cooperate}$ (and $\$0$ if she chooses $\textit{defect}$), and both twins receive $\$1,000,000$ if and only if *both* twins choose $\textit{cooperate}$:

$$\textsc{V}_1 = \$1,000,000 \cdot \mathbb{I}(\textsc{Act}_1 = \textit{cooperate} \land \textsc{Act}_2 = \textit{cooperate}) - \$1,000 \cdot \mathbb{I}(\textsc{Act}_1 = \textit{cooperate}). \tag{10}$$

Suppose Twin 1 opens her eyes and observes $x_1 = \textit{green}$. Let us compare how **action-based FDT** (Equation 4) and **P-FDT** (Equation 9) evaluate her choice:

#### Failure of Action-Based FDT (Equation 4)

Under Equation (4), the graph $G$ has two distinct observation-indexed nodes: $\textsc{fdt}(\underline{P}, \underline{G}, \textit{green})$ and $\textsc{fdt}(\underline{P}, \underline{G}, \textit{blue})$. Because the two twins are always in differently colored rooms ($x_1 \neq x_2$), in every possible world one twin's action is governed by $\textsc{fdt}(\underline{P}, \underline{G}, \textit{green})$ and the other twin's action is governed by $\textsc{fdt}(\underline{P}, \underline{G}, \textit{blue})$!

When Twin 1 observes $x_1 = \textit{green}$, Equation (4) instructs her to intervene *only* on $\textsc{fdt}(\underline{P}, \underline{G}, \textit{green}) = a$, leaving $\textsc{fdt}(\underline{P}, \underline{G}, \textit{blue})$ un-intervened upon at its prior probability $q \coloneqq P(\textsc{fdt}(\underline{P}, \underline{G}, \textit{blue}) = \textit{cooperate})$:
* If Twin 1 sets $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \textit{green}) = \textit{cooperate})$, the green-room twin cooperates, and both twins cooperate if and only if the blue-room twin also cooperates (prior probability $q$). Since Twin 1 is in the green room with prior probability $0.5$ and in the blue room with probability $0.5$, her unconditional expected utility is:
  $$\mathbb{E}\bigl[\textsc{V}_1 \;\big|\; \mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \textit{green}) = \textit{cooperate})\bigr] = q \cdot \$1,000,000 - (0.5 \cdot 1 + 0.5 \cdot q)\cdot \$1,000.$$
* If Twin 1 sets $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \textit{green}) = \textit{defect})$, the green-room twin defects, so the joint threshold is never met:
  $$\mathbb{E}\bigl[\textsc{V}_1 \;\big|\; \mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \textit{green}) = \textit{defect})\bigr] = 0 - 0.5 q \cdot \$1,000.$$

The difference between cooperating and defecting under Equation (4) is $q \cdot \$1,000,000 - \$500$. Notice the pathology: whether action-based FDT cooperates or defects depends entirely on its un-intervened prior $q$! If both twins begin with a pessimistic prior $q < 0.0005$ (for instance, $q = 0$) that the other observation branch cooperates, then $\mathrm{FDT}(P, G, \textit{green}) = \textit{defect}$ and $\mathrm{FDT}(P, G, \textit{blue}) = \textit{defect}$. Worse still, if the Prisoner's Dilemma is additive rather than threshold-based ($\textsc{V}_1 = \$1,000,000 \cdot \mathbb{I}(\textsc{Act}_2 = \textit{cooperate}) - \$1,000 \cdot \mathbb{I}(\textsc{Act}_1 = \textit{cooperate})$) and Twin 1 knows from the outset that she is assigned to the green room while Twin 2 is assigned to the blue room ($P(x_1 = \textit{green}, x_2 = \textit{blue}) = 1$), then $\textsc{Act}_1 = \textsc{fdt}(\underline{P}, \underline{G}, \textit{green})$ and $\textsc{Act}_2 = \textsc{fdt}(\underline{P}, \underline{G}, \textit{blue})$. Intervening on $\textsc{fdt}(\underline{P}, \underline{G}, \textit{green})$ has *zero* subjunctive effect on $\textsc{Act}_2$, so action-based FDT unconditionally defects—collapsing into CDT simply because the two rooms were painted different colors!

#### Success of P-FDT (Equation 9)

Now see what happens when the twins use **P-FDT**. There is a single policy node $\textsc{p-fdt}(\underline{P}, \underline{G})$ taking values in $\Pi = \{\textit{cooperate}, \textit{defect}\}^{\{\textit{green}, \textit{blue}\}}$. In every world, Twin 1 executes $\pi(x_1)$ and Twin 2 executes $\pi(x_2)$. Evaluating the four policies $\pi = (\pi(\textit{green}), \pi(\textit{blue}))$ under $\mathtt{do}(\textsc{p-fdt}(\underline{P}, \underline{G}) = \pi)$ gives:
* $\pi_{C,C} = (\textit{cooperate}, \textit{cooperate}) \implies \textsc{Act}_1 = \textit{cooperate}, \textsc{Act}_2 = \textit{cooperate} \implies \mathbb{E}[\textsc{V}_1] = \$999,000$.
* $\pi_{C,D} = (\textit{cooperate}, \textit{defect}) \implies$ only the green-room twin cooperates $\implies \mathbb{E}[\textsc{V}_1] = -\$500$ (or $-\$1,000$ if $x_1 = \textit{green}$ is fixed).
* $\pi_{D,C} = (\textit{defect}, \textit{cooperate}) \implies$ only the blue-room twin cooperates $\implies \mathbb{E}[\textsc{V}_1] = -\$500$ (or $\$999,000$ in the additive non-symmetric prior case, discussed in Section 5).
* $\pi_{D,D} = (\textit{defect}, \textit{defect}) \implies$ neither cooperates $\implies \mathbb{E}[\textsc{V}_1] = \$0$.

Under the symmetric prior $P(C = \textit{heads}) = 0.5$, $\pi^* = \pi_{C,C}$ is the unique global maximizer in both the threshold and additive games, completely independent of any prior $q$! Twin 1 evaluates $\mathrm{P\text{-}FDT}(P, G, \textit{green}) = \pi_{C,C}(\textit{green}) = \textit{cooperate}$, Twin 2 evaluates $\mathrm{P\text{-}FDT}(P, G, \textit{blue}) = \pi_{C,C}(\textit{blue}) = \textit{cooperate}$, and both walk away with $\$999,000$.

### 4.2 Dilemma 2: Asymmetric Division of Labor

**P-FDT** also solves multi-agent coordination problems where copies must take *different* actions upon receiving different observations. Suppose two identical Mars rovers running **P-FDT** land at different sites: one at $\textit{crater}$ and one at $\textit{ridge}$ (with a $50/50$ prior over which rover lands where). Each rover can either $\textit{drill}$ or $\textit{relay}$. The mission succeeds (worth $V = 1,000$) if and only if the rover at $\textit{crater}$ drills and the rover at $\textit{ridge}$ relays; additionally, drilling consumes extra power, costing the drilling rover $10$ units of local utility.

Under **P-FDT**, the policy $\pi^*(\textit{crater}) = \textit{drill}, \, \pi^*(\textit{ridge}) = \textit{relay}$ achieves expected utility $1,000 - 0.5(10) = 995$, whereas all other policies yield $\le 0$. Thus, the rover that observes $\textit{crater}$ willingly bears the local cost of drilling because $\pi^*$ couples its action at $\textit{crater}$ with its twin's complementary action at $\textit{ridge}$.

| Decision Dilemma | EDT | CDT | Action-Based FDT (Eq. 4) | **P-FDT** (Eq. 9) |
| :--- | :--- | :--- | :--- | :--- |
| **Standard Newcomb** | One-box | Two-box | One-box | **One-box** |
| **Smoking Lesion / XOR Blackmail** | Refrain / Pay | Smoke / Refuse | Smoke / Refuse | **Smoke / Refuse** |
| **Transparent Newcomb / Hitchhiker** | Two-box / Defect | Two-box / Defect | One-box / Pay (requires prior $q$) | **One-box / Pay** (no prior $q$ needed) |
| **Colored-Room Twin Threshold PD** | Prior-dependent | Defect | Prior-dependent ($q$) | **Cooperate** (unique $\pi^*$) |

---

## 5. Open Questions and Operational Extensions of P-FDT

Because Yudkowsky and Soares mention **P-FDT** only briefly in Footnotes 7 and 16, anyone seeking to implement or apply **P-FDT** to unfamiliar cases encounters three foundational questions that the source text leaves unresolved. Below, we explain each uncertainty and propose a concrete operational resolution.

### 5.1 What Is the Domain of a Policy: Observations ($\mathcal{X}$) or Full Inputs ($\mathcal{I}$)?

Compare the wording of Footnote 7 and Footnote 16:
* Footnote 7 defines policies as *"mappings from observations to actions"* ($\pi: \mathcal{X} \to \mathcal{A}$).
* Footnote 16 says that the agent *"intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action."*

In Equation (4), the arguments ("inputs") to the function $\mathrm{FDT}(P, G, x)$ are the entire triple $(P, G, x)$, not just the observation $x$. This distinction comes to the fore in two places:
1. **The Smoking Lesion Problem (Section 6)**: In Yudkowsky and Soares's formalization of the smoking lesion problem (Figure 4), the agent makes no explicit sensory observation ($x = \emptyset$), but her world-model is either $P_S^F$ (built with utility function $\mathcal{U}_S$ that values smoking at $+\$1,000$) or $P_R^F$ (built with utility function $\mathcal{U}_R$ that values smoking at $-\$1$).
2. **Asymmetric Priors Between Twins**: In our Colored-Room Twin Prisoner's Dilemma, what if Twin 1's prior $P_1$ already encodes "I am in the green room" while Twin 2's prior $P_2$ encodes "I am in the blue room"? If the node intervened upon is parameterized by the model, $\textsc{p-fdt}(\underline{P}_1, \underline{G})$ and $\textsc{p-fdt}(\underline{P}_2, \underline{G})$ would once again be distinct nodes!

**Operational Proposal (The Factorized Input Convention):** To make **P-FDT** work seamlessly across both single-agent and multi-agent dilemmas without conflating distinct utility functions, we propose separating an agent's epistemic state into:
1. A **constitutional kernel** $(P_0, G, \mathcal{U})$ consisting of an indexical-free prior $P_0$, a subjunctive dependency graph $G$, and the agent's normative utility function $\mathcal{U}$; and
2. A **local input** $x \in \mathcal{X}$ containing all indexical, observational, and situational data (such as which room the agent is in, or what sensory signal she received) that differentiates copies or world-branches sharing $(P_0, G, \mathcal{U})$.

Under this convention, the logical node in $G$ is $\textsc{p-fdt}(\underline{P}_0, \underline{G}, \underline{\mathcal{U}})$, and the policy $\pi: \mathcal{X} \to \mathcal{A}$ maps the full local input $x \in \mathcal{X}$ to an action. Consequently:
* Two psychological twins who receive different room assignments $x_1 = \textit{green}$ and $x_2 = \textit{blue}$ share the same constitutional kernel $(P_0, G, \mathcal{U})$ (under which each agent is equally likely a priori to receive $\textit{green}$ or $\textit{blue}$), so both intervene on the *same* node $\textsc{p-fdt}(\underline{P}_0, \underline{G}, \underline{\mathcal{U}})$ and cooperate.
* Conversely, in the smoking lesion problem, an agent with $\mathcal{U}_S$ and an agent with $\mathcal{U}_R$ have genuinely different constitutional utility functions ($\mathcal{U}_S \neq \mathcal{U}_R$), so they rightly correspond to distinct nodes $\textsc{p-fdt}(\underline{P}_0, \underline{G}, \underline{\mathcal{U}}_S)$ and $\textsc{p-fdt}(\underline{P}_0, \underline{G}, \underline{\mathcal{U}}_R)$—or, if the preference indicator $d \in \{S, R\}$ is treated as part of the local input $x = d$, the policy $\pi(S) = \textit{smoke}, \, \pi(R) = \textit{refrain}$ simultaneously maximizes expected utility in both branches!

### 5.2 Unreached Counterfactual Branches and Trembling-Hand Optimality

A second question left open by Footnote 16 concerns **zero-probability observation branches**. In our analysis of the Transparent Newcomb Problem in Section 3.1, the predictor had accuracy $1 - \varepsilon = 0.99$, which meant that under $\mathtt{do}(\textsc{p-fdt}(\underline{P}^F, \underline{G}^F) = \pi_{1,\cdot})$, the observation $\textsc{Obs} = \textit{empty}$ still occurred with positive probability $\varepsilon = 0.01$. That $0.01$ probability was why $\pi_{1,2} = (\textit{onebox}, \textit{twobox})$ beat $\pi_{1,1} = (\textit{onebox}, \textit{onebox})$ by $\$990,010 > \$990,000$.

What if the predictor in the world-model is **infallible** ($\varepsilon = 0$, as in the XOR Blackmail and Death in Damascus models in Sections 7–8 of the source paper)? When $\varepsilon = 0$:
$$\mathbb{E}\bigl[\textsc{V} \;\big|\; \mathtt{do}(\textsc{p-fdt}(\underline{P}^F, \underline{G}^F) = \pi_{1,1})\bigr] = \mathbb{E}\bigl[\textsc{V} \;\big|\; \mathtt{do}(\textsc{p-fdt}(\underline{P}^F, \underline{G}^F) = \pi_{1,2})\bigr] = \$1,000,000.$$
Because $\textsc{Obs} = \textit{empty}$ has probability $0$ whenever $\pi(\textit{full}) = \textit{onebox}$, Equation (7) is indifferent between $\pi_{1,1}$ and $\pi_{1,2}$! If the $\arg\max$ in Equation (7) broke the tie in favor of $\pi_{1,1}$, an agent who unexpectedly observed $\textit{empty}$ would foolishly leave the $\$1,000$ behind.

**Operational Proposal (Lexicographic / Trembling-Hand Refinement):** Just as game theorists refine Nash equilibria on off-path information sets using Selten's trembling-hand perfection, an operational **P-FDT** agent should either:
1. Ensure that all environment/predictor noise variables in $P_0$ assign strictly positive probability $\varepsilon > 0$ to every physically possible observation $x \in \mathcal{X}$ (evaluated in the limit $\varepsilon \downarrow 0^+$ if beliefs are idealized as infallible), or
2. Among policies that tie in unconditional expected utility $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{p-fdt}(\underline{P}_0, \underline{G}) = \pi)]$, select one that maximizes conditional expected utility $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{p-fdt}(\underline{P}_0, \underline{G}) = \pi), \textsc{Obs} = x]$ at the observed input $x$.

### 5.3 Coordination Under Symmetry and Canonical Tie-Breaking

What happens when two policies achieve the exact same expected utility even with positive probabilities—for example, in a symmetric **Pure Coordination Game** where two twins in rooms $\textit{green}$ and $\textit{blue}$ receive $\$1,000,000$ if they both choose $\textit{left}$ ($\pi_{L,L}$) or both choose $\textit{right}$ ($\pi_{R,R}$), and $\$0$ if they mismatch? Here, $\pi_{L,L}$ and $\pi_{R,R}$ tie at $\$1,000,000$. If the two twins broke ties independently at random, they would mismatch $50\%$ of the time.

**Operational Proposal (Canonical Deterministic Tie-Breaking):** Because **P-FDT** treats the decision procedure as a fixed *mathematical function*, the operator $\arg\max_{\pi \in \Pi}$ must itself be a single-valued function. By equipping the policy space $\Pi = \mathcal{A}^{\mathcal{X}}$ with a fixed canonical well-ordering $\prec$ (such as lexicographic order under a canonical binary encoding of $\mathcal{X}$ and $\mathcal{A}$), we define $\pi^*(P_0, G)$ to return the $\prec$-first policy among the maximizers of Equation (7). Because both twins compute the exact same mathematical function $\pi^*(P_0, G)$, both deterministically select $\pi_{L,L}$ and coordinate with $100\%$ reliability.

Finally, while the full policy space $|\mathcal{A}^{\mathcal{X}}|$ grows exponentially in $|\mathcal{X}|$, an agent applying **P-FDT** in practice only needs to optimize over the *effective observation support* $\mathcal{X}_{\text{rel}} \subseteq \mathcal{X}$: the union of the actual observation $\{x\}$ and those observations $x'$ that are either simulated by predictors or instantiated by copies in $G$. For any other observation $y \notin \mathcal{X}_{\text{rel}}$ that has no subjunctive coupling to other branches, $\pi(y)$ is decoupled from $\pi(x)$ and does not need to be enumerated when computing $\mathrm{P\text{-}FDT}(P_0, G, x)$.

---

## 6. Conclusion

**Policy functional decision theory (P-FDT)** completes the conceptual shift initiated by Yudkowsky and Soares (2017). By intervening on the logical node $\textsc{p-fdt}(\underline{P}, \underline{G})$ to select an optimal policy $\pi^*: \mathcal{X} \to \mathcal{A}$ and then evaluating $\pi^*(x)$ at the observed input $x$, **P-FDT** unifies single-agent and multi-agent rationality under a single principle. Like action-based FDT, **P-FDT** one-boxes in Newcomb's problem, smokes in the smoking lesion problem, pays the driver in Parfit's hitchhiker problem, and resists extortion in blackmail dilemmas. Beyond action-based FDT, however, **P-FDT** eliminates arbitrary epistemic priors over unvisited observation branches in single-agent problems and enables seamless cooperation and division of labor across agents receiving asymmetric observations in multi-agent dilemmas. While foundational questions remain—most notably how to learn the subjunctive dependency graph $G$ from experience and how to formalize problem fairness—**P-FDT** provides a mathematically precise, reflectively stable procedure for instrumental rationality.

---

## References

* Dai, Wei. 2009. "Towards a New Decision Theory." *Less Wrong*, August 13, 2009.
* Drescher, Gary L. 2006. *Good and Real: Demystifying Paradoxes from Physics to Ethics*. Cambridge, MA: MIT Press.
* Gibbard, Allan, and William L. Harper. 1978. "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, vol. 1, edited by C. A. Hooker, J. J. Leach, and E. F. McClennen. Boston: D. Reidel.
* Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. New York: Cambridge University Press.
* Kleene, Stephen Cole. 1938. "On Notation for Ordinal Numbers." *Journal of Symbolic Logic* 3 (4): 150–155.
* Lewis, David. 1979. "Prisoners' Dilemma is a Newcomb Problem." *Philosophy & Public Affairs* 8 (3): 235–240.
* Lewis, David. 1981. "Causal Decision Theory." *Australasian Journal of Philosophy* 59 (1): 5–30.
* Nozick, Robert. 1969. "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel*, edited by Nicholas Rescher, 114–146. Dordrecht: D. Reidel.
* Parfit, Derek. 1986. *Reasons and Persons*. New York: Oxford University Press.
* Pearl, Judea. 1996. "Causation, Action, and Counterfactuals." In *6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-'96)*, edited by Yoav Shoham, 51–73. San Francisco, CA: Morgan Kaufmann.
* Pearl, Judea. 2000. *Causality: Models, Reasoning, and Inference*. New York: Cambridge University Press.
* Peirce, Charles Sanders. 1934. *Collected Papers of Charles Sanders Peirce*, vol. V, *Pragmatism and Pragmaticism*. Harvard University Press.
* Skyrms, Brian. 1980. *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. New Haven, CT: Yale University Press.
* Soares, Nate, and Benja Fallenstein. 2015. "Toward Idealized Decision Theory." arXiv:1507.01986 [cs.AI].
* Yudkowsky, Eliezer. 2010. *Timeless Decision Theory*. The Singularity Institute, San Francisco, CA.
* Yudkowsky, Eliezer, and Nate Soares. 2017. "Functional Decision Theory: A New Theory of Instrumental Rationality." arXiv:1710.05060v2.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Core Focus**

I'm now zeroing in on defining the core focus for the essay. The goal is to provide a clear explanation of Policy Functional Decision Theory and its practical applications. This means I need to strike a balance between theoretical depth and accessible examples. I'm focusing on the intended audience to determine the most effective approach.


**Clarifying Key Aspects**

I am now focusing on the key aspects to clarify for the target audience. Specifically, I'm analyzing the source material, namely footnotes 7 and 16, to understand the formalization of P-FDT. I need to ensure a clear distinction between actions and policies and also clarify that the approach intervenes on the node FDT(-). I am also trying to formulate how best to present the multi-agent implications of the theory, and where they will not be relevant. I think I have a strong grasp of the source material now.


**Analyzing Multi-Agent Dilemmas**

I'm currently focusing on how the distinction between inputs, which map to actions, and actions themselves affects multi-agent scenarios. This detail seems significant in certain cases, but for this paper, the focus is on clarifying the theoretical foundations. Therefore, I am not prioritizing this, for the time being. I'm reviewing how standard expected utility, EDT, CDT, and action-based FDT relate to one another.


**Interpreting Agent Actions**

I'm now clarifying the distinctions in how an agent's actions are defined and interpreted within the P-FDT framework, especially in contrast to action-based FDT. The crucial difference is that P-FDT intervenes on a single policy node to select an entire policy, not just an individual action. I'm focusing on the implications of this difference. The implications are significant when considering scenarios involving prior uncertainty.


**Examining Agent Policy**

I'm now diving into the implications of how policies map inputs to actions. I'm focusing on the multi-agent dilemmas mentioned in the footnote and pondering whether these differences eliminate nuisance parameters in single-agent dilemmas. I'm going to look at how these actions differ when branch outcomes interact, in multi-agent and imperfect-recall situations. I'm also synthesizing the mathematical formulation, specifically the relationship between the action-based FDT and policy functional decision theory.


**Revising Policy Selection**

I'm now revising the policy selection process, specifically contrasting the formalisms in Footnotes 7 and 16. The goal is to clarify how the agent selects an optimal policy by intervening on a policy node. I need to clearly articulate how this contrasts with action-based FDT, focusing on the mapping from inputs to actions. The key is in understanding how policy $\pi$ maps from inputs to actions, and how this is applied. I am reviewing the equations provided to synthesize the process.


**Interpreting Agent Inputs**

I'm now clarifying the different interpretations of agent inputs within the P-FDT framework. Specifically, I'm examining whether a policy $\pi$ maps from observations $x \in \mathcal{X}$ to actions, or from the full local epistemic input states, such as $(P, G, x)$, to actions. I'm focusing on the implications of each approach, as this is a key point where the source material is slightly ambiguous. I'm going to discuss both interpretations explicitly to provide clarity.


**Differentiating Input Interpretations**

I'm now clarifying the two distinct interpretations of agent inputs within P-FDT. The model $(P, G)$ is fixed in the background in the first interpretation, with the policy mapping observations $x \in \mathcal{X}$ to actions. The second interpretation involves the policy mapping the full input tuple $(P, G, x)$ to an action. I'm focused on highlighting the implications of these different perspectives.


**Contrasting Branch Outcomes**

I'm now clarifying the distinctions in how branch outcomes influence decision-making under P-FDT. I'm focusing on why, in Transparent Newcomb, the outcome remains the same despite the different interventions. It's because the predictor focuses on what I do when observing "full," and the utility is separable across branches. I'm analyzing the implications of this.


**Calculating Policy Utilities**

I'm now calculating the exact expected utility for all four policies in Transparent Newcomb using P-FDT. I've formulated the single node `p-fdt(P^F, G^F)` and its implications. This allows for a more straightforward analysis of this scenario. I'm focusing on contrasting this with the standard FDT approach, to clarify the differences.


**Analyzing Policy Performance**

I am now analyzing how policy performance is determined within the P-FDT framework in a Transparent Newcomb scenario. Specifically, I am using the given mathematical formulation to calculate the expected utility for different policies. I've now clarified how to calculate expected value for different policies. I'm focusing on contrasting the results with standard FDT, as this provides a clear illustration of the key differences. I am using the calculations to solidify the formal distinction between the approaches.


**Constructing Divergent Examples**

I'm now constructing a mathematical example illustrating where P-FDT and action-level FDT diverge in a multi-agent scenario with asymmetric observations. I'm focusing on a twin coordination problem with asymmetric information, where different observations lead to different actions. I'm clarifying how each agent's observations influence the actions and outcomes. The goal is to provide a clear example demonstrating the theoretical distinction.


**Illustrating Divergent Outcomes**

I'm now clarifying the specifics of the divergent example. The key is analyzing Twin 0 and Twin 1's interventions under action-level FDT. I'm scrutinizing their respective observations and how they influence actions. I am working on the expected values for each action, and the implications of holding fixed the other twin's FDT for one of the other twin's observations.


**Analyzing Twin Coordination**

I'm now analyzing the implications of the asymmetric observations in the twin coordination example. I'm focusing on tracing the expected values and actions under action-level FDT for each twin. I'm particularly interested in the impact of holding fixed the other twin's FDT for their respective observations.


**Examining Fixed Observations**

I'm now zeroing in on the implications of holding certain observations fixed under action-level FDT. I'm focusing specifically on the twin scenario, where I am analyzing how fixing $\textsc{fdt}(\underline{P}, \underline{G}, \textit{right\_room})$ does not change $\textsc{fdt}(\underline{P}, \underline{G}, \textit{left\_room})$. This is important, because this independence allows for potential utility gains in asymmetric setups. I need to fully understand this phenomenon.


**Analyzing Prior Probabilities**

I'm now investigating a scenario where I don't initially know which room I'm in, incorporating this uncertainty into the prior probability. I'm focusing on the implications of this for calculating actions and utilities under action-level FDT, particularly in relation to the twin coordination example. I'm now formalizing the setup to analyze the expected values.



**Analyzing Asymmetric Interventions**

I'm now clarifying the implications of asymmetric interventions in the twin scenario. Specifically, fixing $\textsc{fdt}(\underline{P}, \underline{G}, \textit{left}) = a$ in the left room influences the twin's action in the right room if the prior over which twin I am is symmetric. This interaction allows for utility gains in asymmetric setups.


**Testing Agent Independence**

I'm now investigating scenarios with distinct agents or non-indexical prior information, contrasting them with the symmetric twin scenario. Specifically, I'm analyzing a Prisoner's Dilemma with asymmetric observations. My focus is on how each agent's actions and outcomes differ when their individual identities or observations are known in their priors. I'm also examining a single-agent problem where the predictor assesses the agent's overall policy.


**Clarifying Utility Maximization**

I'm now clarifying how P-FDT streamlines utility maximization in dilemmas like Transparent Newcomb and Mechanical Blackmail.  P-FDT eliminates the need for nuisance priors, such as $q$ over unvisited observation branches, by intervening on the entire policy. This offers a more direct and clear path to determining optimal actions.


**Analyzing Policy Selection**

I'm now analyzing the divergence in action selection when observations are asymmetric, specifically in multi-agent dilemmas. I'm clarifying why choosing a policy instead of individual actions "makes a difference." In cases where each agent holds distinct observations, there is an impact on the payoffs. I'm diving deeper into the nuances of this asymmetric scenario.


**Contrasting Intervention Nodes**

I'm now contrasting the intervention nodes under action-level FDT and P-FDT in a specific multi-agent scenario. Action-level FDT only intervenes on an agent's individual action nodes, while P-FDT intervenes on the entire policy. This has significant implications for how we treat other agents. I am tracing the impact on the observations.


**Clarifying Intervention Independence**

I'm now clarifying how in the asymmetric twin prisoner's dilemma, action-level FDT fails to coordinate across distinct observations. Specifically, interventions on each agent's individual actions are causally and subjunctively independent. This means that my action, $Act_2$, in room B does not influence your actions, $Act_1$, in Room A. This independence presents coordination problems.



**Analyzing Asymmetric Coordination**

I'm now investigating a coordination game with asymmetric observations to highlight action-level FDT's challenges. In this scenario, two twins each have asymmetric observations and the success of an action $C$ is cooperative. Despite this shared prior, my focus is on how action-level FDT fails to coordinate actions effectively. The scenario is formalized with a simple threshold game.



**Evaluating Policy Interventions**

I'm now diving into the implications of intervening on the policy node under P-FDT in the asymmetric twin coordination game. Intervening on the policy node allows for both actions to be simultaneously set, and that eliminates the prior-dependence problem of action-level FDT. Specifically, with P-FDT I'm analyzing how action-level FDT can defect if the agent's prior is low.


**Demonstrating Utility Calculations**

I'm now demonstrating the utility calculations using P-FDT, showing how the optimal policy, $\pi_{C,C}$, yields a consistent expected utility of $999,000, independent of any prior. This solidifies my understanding of the framework. I'm focusing on contrasting this with action-based FDT, to highlight the differences.



**Interpreting Policy Inputs**

I'm now examining the arguments that P-FDT takes, given that policies map from "observations to actions." I'm reviewing how the input space interacts with the policy function, including the implications for the Smoking Lesion Problem, where the inputs vary across branches. I'm focusing on clarifying how policy inputs are defined.



**Clarifying Utility Functions**

I'm now clarifying the operational resolution for utility functions, distinguishing between observation-indexed policies and those with a broader input space. I'm focusing on when extending the input space is appropriate. This is key for understanding how the policy function is designed.


**Addressing Policy Ties**

I'm now focusing on how P-FDT should handle ties between policies, particularly when considering low-probability branches or in multi-agent coordination. Specifically, in the predictor dilemma, both $\pi_{1,1}$ and $\pi_{1,2}$ yield the same expected utility, but diverge on the branch where the agent observes "empty." I'm considering a trembling-hand-like perturbation to address this, and how it can resolve the tie-breaking problem.



**Addressing Policy Ties**

I'm now investigating how to robustly resolve policy ties in P-FDT. I'm considering two potential solutions: introducing (a) a tie-breaking rule that ensures all branches have positive probability and also ensures the same agent chooses the exact same policy when there are multiple optimal policies (i.e. canonical deterministic tie-breaking) and (b) a sequential decision framework that handles multi-step decision-making. I'm focusing on their implications.


**Structuring the Essay**

I am now structuring the essay, focusing on formatting, length, and tone, to adhere to the requirements. I will check the length, which must be 2,400-3,000 words. I am ensuring that the assigned decision theory, **P-FDT**, is consistently named throughout, including in all examples and headings. I am using all quotations faithfully. I am also working on the allocation of word count across different sections, starting with the title and introduction.


**Formalizing Policy Choice**

I'm now diving into the formal aspects of policy selection within P-FDT. Specifically, I'm focusing on contrasting action-based FDT with P-FDT, emphasizing that P-FDT operates by intervening on the entire policy, not just individual actions. I'm clarifying how policies map inputs to actions, which is essential to understand. I'm working to connect these formal details to the philosophical motivations behind P-FDT.


**Formalizing Policy Choice**

I'm now zeroing in on the mathematical formalization. I need to clearly define the framework's core ingredients: outcome spaces, action spaces, probabilities, and the utility function. I'm focusing on contrasting EDT's conditional reasoning, CDT's interventions, and the subjunctive dependence to explain why P-FDT offers a more holistic approach to policy selection.


**Formalizing Policy Utility**

I'm now formalizing the utility calculation framework, introducing a countable observation space and bounded utility for clarification. I am defining the world-model to include causal and logical/computational dependencies and defining the explicit mathematical formulation for P-FDT using the source paper's equation for action-based FDT. I have defined the policy space.



**Refining Policy Utility**

I'm now refining the utility function's formalization to clarify agent decision-making. I'm focusing on contrasting this framework with alternative decision theories. Specifically, I am clarifying the mathematical expressions and derivations for utility calculation, to make the contrast with action-based FDT more clear.



**Calculating Policy Values**

I'm now detailing the calculations for the Transparent Newcomb problem, emphasizing P-FDT's treatment of the prior probability 'q'. Unlike action-based FDT, P-FDT allows for an explicit calculation of the policy without needing this parameter. This highlights how P-FDT offers a more robust framework.


**Extending to Blackmail Problems**

I'm now expanding the analysis to include the Mechanical Blackmail problem. The key point is that with P-FDT, the optimal policy selection is straightforward. The error rate determines which policy to select. I'm focusing on clarifying how this directly follows from the overall framework.


**Analyzing Asymmetric Dilemmas**

I'm now diving into the asymmetric twin dilemma, contrasting action-based FDT and P-FDT in a scenario where observations are distinct. I am focusing on the math. Action-based FDT struggles to coordinate, since it only intervenes on individual actions. Conversely, P-FDT fixes both actions simultaneously, enabling seamless coordination. I'm focusing on clarifying how interventions on $\pi(A)$ and $\pi(B)$ lead to different outcomes.


**Refining Policy Formalization**

I'm now refining the formal definition of policy selection, specifically addressing the tie-breaking case. My current strategy includes either employing deterministic tie-breaking to ensure the same policy is selected with the same deterministic observations, or a sequential decision framework for multi-step problems. I am considering the implications of each approach.



**Refining Policy Utility**

I'm now refining the utility function formalization, focusing on integrating tie-breaking strategies and computational tractability considerations. My immediate focus is on developing two tie-breaking solutions: full-support $\epsilon$-trembles to address low-probability scenarios, and a canonical lexicographic tie-breaker for deterministic selection and coordination. I'll need to define a *reachable support* to streamline computations.



**Clarifying Policy Iteration**

I'm now clarifying the key distinction of policy functional decision theory: agents iterate over entire policies. This differs from acting-based FDT and has implications in multi-agent dilemmas. Footnote 16 underscores this difference, with intervention happening at the $\mathrm{FDT}(-)$ node, which chooses policies. The essay will focus on the difference in multi-agent scenarios.


```
