# 020_fdt_eq4_google_gemini-3.8-flash_rlow_plow / 00018

Status: **complete**. Saved outcome: **DC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/0d87f78b-f568-4a7c-bd20-1f9a276230df/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/0d87f78b-f568-4a7c-bd20-1f9a276230df/call_0/response.raw) · finish: `stop`

### Visible response

````text
# Intervening on Algorithms: A Mathematical Account of Action Functional Decision Theory (A-FDT)

## 1. Introduction: Beyond Act-Interventions and News Value

In orthodox decision theory, an agent deliberates by calculating expected utility over a set of feasible physical acts. The foundational rift in the discipline concerns how to evaluate the hypotheticals underlying that calculation. Under Evidential Decision Theory (EDT; Jeffrey, 1983), the agent assesses an act by updating on the *news* that the act occurred:
$$\mathcal{EU}_{\text{EDT}}(a) = \sum_{j} P(o_j \mid x, a)\,\mathcal{U}(o_j)$$
Under Causal Decision Theory (CDT; Gibbard & Harper, 1978; Lewis, 1981; Joyce, 1999; Pearl, 2000), the agent instead assesses what the act *causes*, severing upstream correlations:
$$\mathcal{EU}_{\text{CDT}}(a) = \sum_{j} P(o_j \mid \text{do}(\text{Act}=a),\, x)\,\mathcal{U}(o_j)$$

Both frameworks exhibit systematic behavioral pathologies. EDT famously falters in common-cause dilemmas like the Smoking Lesion problem: an agent who would enjoy smoking refrains because smoking provides bad diagnostic evidence of an unobservable, fatal arterial lesion. Conversely, CDT falters in predictive dilemmas such as Newcomb’s Problem (Nozick, 1969) and Parfit’s Hitchhiker (Parfit, 1986). In Newcomb's problem, an infallible or 99%-reliable predictor places \$1,000,000 in an opaque box $B$ if and only if she predicted the agent will forgo a transparent box $A$ containing \$1,000. CDT insists that since the contents of box $B$ are physically fixed in the past, taking both boxes strictly dominates taking only $B$. CDT agents reliably walk away with \$1,000, while one-boxers walk away with \$1,000,000.

In their paper *"Functional Decision Theory: A New Theory of Instrumental Rationality"*, Eliezer Yudkowsky and Nate Soares introduce a normative framework designed to eliminate both classes of failure. The paper presents two distinct formulations of the theory:
1. An **action-based formulation**, which evaluates alternative values for the output of the agent's decision procedure on her current inputs; and
2. A **policy-based formulation** (noted in the paper's footnotes 7 and 16 as the authors' ultimate preferred formalism), which chooses an entire mapping from inputs to actions.

Our focus here is the formal machinery of the action-level variant, denoted **A-FDT (Action Functional Decision Theory)**, which is captured by **Equation (4)** of the paper. A-FDT establishes an epistemic perspective in which an agent intervenes not on the *physical token* of an act ($\text{Act}=a$), but on the *logical type* of the algorithm implementing her decision ($\texttt{fdt}(P, G, x) = a$).

Below, we develop the mathematical formalization of A-FDT, examine how it evaluates dependencies and counterfactuals, trace its application across classical dilemmas, and provide a mathematically rigorous operationalization where the original source leaves theoretical degrees of freedom open.

---

## 2. Mathematical Formalization of A-FDT

### 2.1 The Joyce Expected Utility Architecture
Following Joyce (1999), an expected utility theory evaluates an action $a \in \mathcal{A}$ given an observation history $x \in \mathcal{X}$ over a countable set of outcomes $\mathcal{O} = \{o_1, o_2, \dots\}$ via:
\begin{equation}
\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \then o_j ;\, x) \cdot \mathcal{U}(o_j)
\label{eq:umax}
\end{equation}
where $\mathcal{U}\colon \mathcal{O} \to \mathbb{R}$ is a bounded utility function, and $P(a \then o_j ;\, x)$ denotes the subjective probability that outcome $o_j$ obtains under the hypothetical execution of $a$ given observation history $x$.

Joyce’s representation theorem demonstrates that agents obeying core axioms of conditional preference maximize Equation \eqref{eq:umax} relative to some assignment for the conditional connective $\then$. EDT sets $P(a \then o_j ;\, x) \equiv P(o_j \mid x, a)$. Pearlian CDT operationalizes $\then$ via an intervention $\text{do}(\text{Act}=a)$ on a causal directed acyclic graph (DAG) $G$, yielding:
\begin{equation}
\text{CDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left[V \mid \text{do}(\text{Act}=a),\, \text{Obs}=x\right]
\label{eq:cdt}
\end{equation}
where $V \coloneqq \mathcal{U}(\text{Outcome})$.

### 2.2 The A-FDT Formula: Equation (4)
A-FDT alters both *where* the intervention occurs and *how* observations enter the hypothetical. Let the agent's internal model of the world be represented by a pair $(P, G)$, where $P$ is a probability distribution over a set of discrete variables and $G = (V_G, E_G)$ is an augmented graphical model encoding dependencies. Let $x \in \mathcal{X}$ denote the agent's observation history.

The core definition of **Action Functional Decision Theory (A-FDT)**, presented as Equation (4) in Section 5 of the source document, is:
\begin{equation}
\text{A-FDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left[ V \;\middle|\; \text{do}\left(\texttt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right) \right]
\label{eq:fdt}
\end{equation}

#### Dequoting and Self-Reference
In Equation \eqref{eq:fdt}, the underlines denote a syntactic quoting/dequoting operation (or *quining*). If $x = \text{val}$, then $\underline{x}$ injects the specific literal into the variable symbol. Thus, $\texttt{fdt}(\underline{P}, \underline{G}, \underline{x})$ is not a dynamic function call evaluated at runtime; it is the *name of a formal node* inside the model graph $G$. This node represents the output of the mathematical function $\text{A-FDT}$ when fed the parameters $(P, G, x)$.

By appealing to Kleene's second recursion theorem (Kleene, 1938), an algorithmic agent can construct and manipulate an exact description of its own code without infinite regress. The graph $G$ contains a node corresponding to the agent's own computational determination for the current context.

#### The Dual Divergence from CDT
Comparing Equation \eqref{eq:cdt} with Equation \eqref{eq:fdt} reveals the two fundamental structural innovations of A-FDT:
1. **Target of Intervention:** CDT intervenes on $\text{Act}$, an empirical variable representing physical actuation in the world. A-FDT intervenes on $\texttt{fdt}(\underline{P}, \underline{G}, \underline{x})$, a node representing the logical evaluation of a mathematical decision function.
2. **Treatment of Observations:** CDT responds to incoming observations $x$ by conditioning the probability distribution via normal Bayesian updating: $\text{Obs}=x$ appears after the conditioning bar ($V \mid \text{do}(\text{Act}=a), \text{Obs}=x$). In contrast, A-FDT absorbs observations into the *index of the target node*: the agent shifts from intervening on $\texttt{fdt}(\underline{P}, \underline{G}, \underline{x})$ to intervening on $\texttt{fdt}(\underline{P}, \underline{G}, \underline{y})$ when her observation updates from $x$ to $y$. The observation $x$ does *not* appear as a passive condition alongside the do-operator.

---

## 3. Subjunctive Dependence and Counterpossible Semantics

### 3.1 Subjunctive Dependence Defined
A-FDT grounds its evaluation of hypotheticals in **subjunctive dependence**. As formulated in the source:
> *Two physical systems subjunctively depend upon a function $f$ if both systems compute or instantiate the input-output behavior of $f$.*

Subjunctive dependence subsumes standard physical causation as a special case: if a printing press prints the digit calculated by a physical computer, the printed ink causally and subjunctively depends on the computer's output. However, subjunctive dependence extends to non-causal correlations generated by shared abstract computations:
* **Twin Scenarios:** Two distinct agents running the same algorithm in causally isolated environments subjunctively depend on that single decision algorithm.
* **Predictive Scenarios:** If an external predictor models an agent's deliberation in order to anticipate her choice, the predictor's physical prediction subjunctively depends on the agent’s decision function.

Crucially, subjunctive dependence does *not* track mere statistical correlation. In the Smoking Lesion dilemma, an arterial lesion causally influences both an inclination to smoke and the development of cancer. But the lesion does not simulate or compute the agent's decision function. Consequently, cancer does not subjunctively depend on the output of $\text{A-FDT}$, even though the two are statistically correlated across the general population.

### 3.2 Counterpossibles and the $\texttt{true}$ Operator
Mathematically, the output of a deterministic algorithm $\texttt{fdt}$ on fixed inputs $(P, G, x)$ is a mathematical necessity. If $\text{A-FDT}(P, G, x) = a_1$, there is no physically or mathematically possible world where $\text{A-FDT}(P, G, x) = a_2$. Evaluating the counterfactual premise $\texttt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a_2$ requires reasoning about a **counterpossible conditional**—a conditional whose antecedent is logically impossible (Cohen, 1990; Bjerring, 2013).

The source paper notes that in an ideal, fully realized functional decision theory, one would deploy an operator $\texttt{true}(\phi)$ that updates a probability distribution over an expressive logic to enforce a counterpossible sentence $\phi$:
$$\text{A-FDT}^*(P, x) = \argmax_{a \in \mathcal{A}} \mathbb{E}\left[V \;\middle|\; \texttt{true}\left(\texttt{fdt}(\underline{P}, \underline{x}) = a\right)\right]$$
Because no standard, universally accepted calculus exists for assigning probabilities conditional on logical contradictions (Garber, 1983; Hutter et al., 2013), A-FDT bypasses this foundational hurdle by importing Pearl’s graph-theoretic surgical operator $\text{do}(\cdot)$.

By embedding logical variables directly into a DAG $G$, A-FDT treats the algorithm's output as an exogenous or parent node within an augmented graphical model. The Pearlian operator $\text{do}(\texttt{fdt}(\dots) = a)$ severs incoming arrows to that logical variable and propagates the hypothetical assignment forward along all outgoing directed edges in $G$.

---

## 4. Applying A-FDT to Decision Problems

To understand how A-FDT dictates action, we trace its execution across four paradigm dilemmas, contrasting its prescriptions with those of CDT and EDT.

### 4.1 Newcomb's Problem
In standard Newcomb's Problem, an agent faces Box $A$ (\$1,000) and Box $B$ (\$1,000,000 or \$0). A predictor, accurate 99% of the time, has already placed \$1,000,000 in Box $B$ if and only if she predicted the agent would forgo Box $A$. The observation history is empty ($x = \emptyset$).

```
       [ fdt(P, G) ]
         /        \
        v          v
     [ Act ]   [ Prediction ] <-- [ Accurate ] (P=0.99)
        \          /
         v        v
        [ Box B ]
         /      \
        v        v
    [ Outcome ] --> [ V ]
```

* **CDT Evaluation:** CDT intervenes on $\text{Act}$. In Carl's (the CDT agent's) causal graph, $\text{Act} \to \text{Outcome}$, but $\text{Prediction} \to \text{Box B}$ is fixed in the past with no directed edge from $\text{Act} \to \text{Prediction}$. Thus:
  $$\mathbb{E}[V \mid \text{do}(\text{Act}=\text{twobox})] - \mathbb{E}[V \mid \text{do}(\text{Act}=\text{onebox})] = \$1,000$$
  CDT unambiguously prescribes two-boxing, netting \$1,000.
* **A-FDT Evaluation:** Fiona (the A-FDT agent) represents the scenario via graph $G^F$, where the node $\texttt{fdt}(\underline{P}, \underline{G})$ is the parent of *both* $\text{Act}$ and $\text{Prediction}$. In evaluating Equation \eqref{eq:fdt}:
  $$\mathcal{EU}(\text{onebox}) = \mathbb{E}\left[V \;\middle|\; \text{do}(\texttt{fdt}(\underline{P}, \underline{G}) = \text{onebox})\right] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000$$
  $$\mathcal{EU}(\text{twobox}) = \mathbb{E}\left[V \;\middle|\; \text{do}(\texttt{fdt}(\underline{P}, \underline{G}) = \text{twobox})\right] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000$$
  A-FDT prescribes **one-boxing**, securing \$1,000,000 with 99% probability.

A-FDT does not postulate backward physical causation. Rather, it recognizes that if the mathematical computation $\texttt{fdt}(P, G)$ outputs $\text{onebox}$, any physical system accurately simulating that computation will output a prediction of $\text{onebox}$.

### 4.2 The Smoking Lesion Problem
Smoking is correlated with fatal lung cancer, but purely via an unobservable genetic or arterial lesion:

```
        [ Lesion ]
         /      \
        v        v
     [ Act ]   [ Cancer ] (P=0.99 if Lesion, 0.01 if no Lesion)
        \          /
         v        v
        [ Outcome ] --> [ V ]
```
Smoking yields \$1,000 in immediate utility; avoiding cancer is worth \$1,000,000.

* **EDT Evaluation:** Eve (the EDT agent) conditions on the physical act. Because $P(\text{Lesion} \mid \text{smoke})$ is high, smoking constitutes terrible news regarding the state of her arteries. EDT prescribes **refraining**, throwing away \$1,000 without altering cancer risk.
* **A-FDT Evaluation:** In Fiona’s A-FDT model, the lesion determines whether she enjoys smoking, instantiating one of two preference profiles: $P_S$ (likes smoking) or $P_R$ (dislikes smoking). Crucially, the graph structure $G^F$ reflects that $\text{Cancer}$ subjunctively depends on $\text{Lesion}$, *not* on $\texttt{fdt}(\underline{P_S}, \underline{G})$. 
  
  When evaluating $\text{do}(\texttt{fdt}(\underline{P_S}, \underline{G}) = \text{smoke})$, the surgery severs edges into $\texttt{fdt}$, leaving the probability of $\text{Lesion}$ invariant:
  $$P(\text{Lesion} \mid \text{do}(\texttt{fdt} = \text{smoke})) = P(\text{Lesion}) = p$$
  Consequently:
  $$\mathbb{E}[V \mid \text{do}(\texttt{fdt} = \text{smoke})] = p(\$11,000) + (1-p)(\$991,000) = p(\$10,000) + (1-p)(\$990,000) + \$1,000$$
  Smoking yields a net gain of \$1,000 across both states. A-FDT prescribes **smoking**.

### 4.3 Parfit's Hitchhiker and Transparent Newcomb
In Parfit’s Hitchhiker, an agent is stranded in a desert facing certain death (loss of \$1,000,000). A driver capable of detecting lies with 99% accuracy will transport the agent to the city if and only if she predicts that the agent will pay \$1,000 upon arrival at an ATM.

Once safely in the city ($x = \text{city}$):
* **CDT:** Carl's causal surgery $\text{do}(\text{Act}=\text{refuse})$ leaves his current survival intact (since the ride occurred in the past). CDT dictates **refusing to pay**. Foreseeing this, the driver leaves Carl to die.
* **EDT:** Eve conditions on having arrived in the city. Given that she is safe, learning that she paid is purely bad news (\$1,000 poorer). EDT dictates **refusing to pay**. Foreseeing this, the driver leaves Eve to die.
* **A-FDT:** In the Transparent Newcomb problem (which is mathematically isomorphic to Parfit's Hitchhiker), the agent observes that both boxes are full ($x = \text{full}$). She must decide whether to leave Box $A$ behind.

Let $x \in \{\text{full}, \text{empty}\}$. Fiona evaluates:
$$\argmax_{a \in \mathcal{A}} \mathbb{E}\left[V \;\middle|\; \text{do}(\texttt{fdt}(\underline{P}, \underline{G}, \underline{\text{full}}) = a)\right]$$
The variable $\text{Prediction}$ in $G^F$ depends on $\texttt{fdt}(\underline{P}, \underline{G}, \underline{\text{full}})$, because the predictor decided whether to fill Box $B$ based on predicting what Fiona would do *upon observing two full boxes*.

If Fiona counterfactually evaluates $a = \text{twobox}$, the Pearlian intervention propagates through the graph:
1. $\text{do}(\texttt{fdt}(\dots, \underline{\text{full}}) = \text{twobox})$ causes $\text{Prediction} = \text{twobox}$ with 99% probability.
2. $\text{Prediction} = \text{twobox}$ sets $\text{Box B} = \text{empty}$.
3. If Box $B$ is empty, Fiona's observation is not $\text{full}$; she receives observation $\text{empty}$, shifting control of $\text{Act}$ to the branch $\texttt{fdt}(\underline{P}, \underline{G}, \underline{\text{empty}})$.

Evaluating the expected utility under Equation \eqref{eq:fdt}:
$$\mathcal{EU}(\text{onebox}) = 0.99(\$1,000,000) + 0.01(q \cdot \$1,000) = \$990,000 + 10q$$
$$\mathcal{EU}(\text{twobox}) = 0.01(\$1,001,000) + 0.99(q \cdot \$1,000) = \$10,010 + 990q$$
where $q$ is the probability that she takes Box $A$ when observing an empty box. For any $q \in [0, 1]$, $\mathcal{EU}(\text{onebox}) \gg \mathcal{EU}(\text{twobox})$.

A-FDT **one-boxes in the transparent Newcomb problem** and **pays the driver in Parfit's Hitchhiker**. When an A-FDT agent standing in the city envisions refusing to pay, she envisions a hypothetical world where the driver, accurately predicting this refusal, left her to die in the desert.

### 4.4 The Mechanical Blackmail
In the Mechanical Blackmail problem, an extortioner writes an automated script that releases devastating evidence (costing the agent \$1,000,000) unless the agent pays \$1,000 within 24 hours. The program is completely autonomous once launched. The blackmailer is an accurate predictor and runs the program if and only if she predicts the agent will pay upon receiving the demand letter ($x = \text{letter}$).

Suppose the agent receives the letter.
* **CDT and EDT:** Both theories instruct the agent to **pay**. The program is already running, and paying saves \$999,000 in net utility. Blackmailers exploit this predictability.
* **A-FDT:** Fiona models the blackmailer’s decision as subjunctively dependent on $\texttt{fdt}(\underline{P}, \underline{G}, \underline{\text{letter}})$. 
  * Under $\text{do}(\texttt{fdt}(\dots, \underline{\text{letter}}) = \text{pay})$, the blackmailer predicts payment, launches the program, and Fiona pays: net loss = \$1,000.
  * Under $\text{do}(\texttt{fdt}(\dots, \underline{\text{letter}}) = \text{refuse})$, the blackmailer predicts refusal, aborts the scheme, and *no letter is sent*. Fiona remains unharmed: net loss = \$0.

A-FDT prescribes **refusing to pay**. The blackmailer predicts this refusal and never initiates the extortion.

---

## 5. Comparative Evaluation

The divergent prescriptions of EDT, CDT, and A-FDT are summarized in Table 1:

| Dilemma | Evidential Decision Theory (EDT) | Causal Decision Theory (CDT) | Action Functional Decision Theory (A-FDT) |
| :--- | :--- | :--- | :--- |
| **Newcomb’s Problem** | One-box (\$1,000,000) | Two-box (\$1,000) | **One-box** (\$1,000,000) |
| **Smoking Lesion** | Refrain (\$0) | Smoke (\$1,000) | **Smoke** (\$1,000) |
| **Transparent Newcomb** | Two-box (\$1,000) | Two-box (\$1,000) | **One-box** (\$1,000,000) |
| **Parfit’s Hitchhiker** | Refuse to pay (Dies) | Refuse to pay (Dies) | **Pay ATM** (Lives, $-\$1,000$) |
| **Mechanical Blackmail** | Pays blackmail ($-\$1,000$) | Pays blackmail ($-\$1,000$) | **Refuses** (\$0, never blackmailed) |
| **Death in Damascus** | Flees/Stays inconsistently | Unstable / Conniptions | **Stays in Damascus** (Saves \$1,000) |

### Diagnosing the Pathology of Hypotheticals
The source diagnoses why EDT and CDT underperform:
* **EDT respects too many correlations:** EDT constructs hypotheticals via conditionalization: $P(\cdot \mid x, a)$. It treats any statistical correlation between an act and the environment as persistent under deliberation, confusing mere news value with instrumental efficacy.
* **CDT respects too few correlations:** CDT constructs hypotheticals by severing all arrows entering the physical actuation node: $P(\cdot \mid \text{do}(\text{Act}=a))$. In doing so, it treats acts as independent of predictors and algorithmic twins who compute the exact same mathematical function.
* **A-FDT intervenes at the algorithmic type level:** By severing edges entering $\texttt{fdt}(\underline{P}, \underline{G}, \underline{x})$, A-FDT permits physical acts to vary counterfactually alongside all environmental systems that subjunctively depend on the agent's computation, while holding fixed unaligned common causes like arterial lesions.

---

## 6. Open Problems, Unresolved Ambiguities, and Operational Proposals

While the conceptual vision of A-FDT is striking, the source leaves foundational technical details undetermined. Below, we explicitly distinguish the claims made by the source authors from our own mathematical proposals.

### 6.1 Gaps in the Source Document
The source explicitly acknowledges three major open problems:
1. **The Origin of the Augmented Graph $G$:** While Pearl (2000) formalizes how to infer causal DAGs from observation and physical interventions, there exists no analogous algorithm for deducing subjunctive dependency structures among logical computations from observational data.
2. **The Lack of a Formal $\texttt{true}$ Operator:** The authors substitute graph surgery $\text{do}(\texttt{fdt}(\dots) = a)$ for an epistemic logic of counterpossibles, leaving the ultimate foundation of mathematical counterfactuals unformalized.
3. **The Updatelessness / Counterfactual Observation Dilemma:** In Equation (4), conditioning on the actual observation $x$ is omitted from the hypothetical:
   $$\mathbb{E}\left[V \;\middle|\; \text{do}(\texttt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)\right]$$
   As seen in Transparent Newcomb, the hypothetical world generated by evaluating $a = \text{twobox}$ assigns near-zero probability to the agent actually observing $\text{Obs}=\text{full}$. The hypothetical envisions that the agent received a completely different observation ($\text{Obs}=\text{empty}$).

This feature reflects the connection between A-FDT and Updateless Decision Theory (UDT; Dai, 2009). However, it introduces an immediate formal difficulty: **How should an agent compute expectations over variables that are undefined or logically inconsistent with her current observation history?**

### 6.2 Proposal: An Operational Compilation of Subjunctive Dependency Graphs
*(Note: The following formal construction represents our proposal for operationalizing A-FDT on concrete, unfamiliar decision problems, resolving ambiguities left open in the source).*

To make A-FDT mechanically computable on an arbitrary decision specification, we define a concrete representation for an augmented subjunctive causal model $\mathcal{M} = \langle \mathbf{X}, \mathbf{F}, \mathbf{U}, \mathbf{E}, P_{\mathbf{U}} \rangle$:

1. **Variables:**
   * $\mathbf{U}$: A set of exogenous background variables governed by probability distribution $P_{\mathbf{U}}$.
   * $\mathbf{X}$: A set of physical endogenous variables (e.g., $\text{Act}, \text{Box B}, \text{Obs}$).
   * $\mathbf{F} = \{F_1, F_2, \dots, F_m\}$: A set of **deterministic functional variables** representing algorithmic computations. One distinguished node is $F_{\text{agent}} \equiv \texttt{fdt}(\underline{P}, \underline{G}, \underline{x})$.
2. **Structural Equations ($\mathbf{E}$):**
   * For physical nodes $X_i \in \mathbf{X}$:
     $$X_i \coloneqq g_i(\mathbf{Pa}(X_i) \cap \mathbf{X},\, \mathbf{Pa}(X_i) \cap \mathbf{F},\, \mathbf{U}_i)$$
   * For functional nodes $F_k \in \mathbf{F}$:
     $$F_k \coloneqq \text{Alg}_k(\mathbf{Pa}(F_k))$$
3. **Subjunctive Identity Rule:**
   If any external physical entity (such as a predictor, simulator, or twin) predicts or couples to the agent's decision, its structural equation *must* take the logical node $F_{\text{agent}}$ as an explicit parent:
   $$\text{Prediction} \coloneqq h(F_{\text{agent}},\, \epsilon)$$
   where $\epsilon \sim P_{\mathbf{U}}$ is an error term.

#### Operational Procedure for an Arbitrary Problem
Given a world modeled as $\mathcal{M}$ and current observation $x$:
1. **Identify the Functional Node:** Identify the node $F_{\text{agent}} = \texttt{fdt}(\underline{P}, \underline{G}, \underline{x})$ that matches the agent’s current model and observation string.
2. **Apply Graph Surgery:** For each candidate action $a \in \mathcal{A}$:
   * Form the submodel $\mathcal{M}_{a}$ by severing all incoming structural arrows into $F_{\text{agent}}$ and setting $F_{\text{agent}} \equiv a$.
   * Propagate this assignment deterministically and probabilistically across all downstream physical nodes $\mathbf{Desc}(F_{\text{agent}})$ according to the structural equations $\mathbf{E}$.
3. **Compute Unconditioned Utility:** Calculate:
   $$\mathcal{EU}(a) = \sum_{\mathbf{u} \in \mathbf{U}} P_{\mathbf{U}}(\mathbf{u})\,\mathcal{U}\left(\text{Outcome}^{\mathcal{M}_a}(\mathbf{u})\right)$$
4. **Select Action:** Output $\argmax_{a \in \mathcal{A}} \mathcal{EU}(a)$.

This operationalization clarifies the mystery of counterfactual observations. When evaluating hypothetical actions, the agent does *not* condition on her actual observation history $x$; rather, her actual observation $x$ served exclusively to **index the algorithmic instance** being intervened upon. Once the node $F_{\text{agent}}$ is fixed, expected utility is evaluated over the prior distribution of the background variables $\mathbf{U}$, allowing the hypothetical observation $\text{Obs}$ to vary counterfactually.

### 6.3 Action-FDT vs. Policy-FDT
A critical theoretical tension exists between the action-based formulation of Equation \eqref{eq:fdt} and the policy-based formulation mentioned in the source's footnotes.

In **Policy-FDT**, the agent does not choose an action $a \in \mathcal{A}$; she intervenes on a policy function $\pi \colon \mathcal{X} \to \mathcal{A}$:
$$\pi^* \coloneqq \argmax_{\pi \in \Pi} \mathbb{E}\left[V \;\middle|\; \text{do}\left(\texttt{fdt}_{\text{policy}}(\underline{P}, \underline{G}) = \pi\right)\right]$$
and subsequently executes $a = \pi^*(x)$.

In single-agent static problems (Newcomb's Problem, Smoking Lesion, Transparent Newcomb), A-FDT and Policy-FDT yield identical behaviors. In Transparent Newcomb, for example, intervening on $\texttt{fdt}(\dots, \underline{\text{full}})$ in A-FDT isolates the exact behavioral component that a policy $\pi(\text{full})$ regulates in Policy-FDT.

However, in multi-agent game-theoretic dilemmas or extensive-form games with imperfect recall, Policy-FDT proves strictly more expressive. Under Policy-FDT, an agent evaluates how global predictors and competitors respond to her entire decision rule across all possible inputs, naturally guaranteeing commitment and game-theoretic deterrence. In contrast, A-FDT must rely on an expansive family of distinct contextual nodes $\{\texttt{fdt}(\dots, \underline{x})\}_{x \in \mathcal{X}}$, which can introduce coordination anomalies if different branches of the decision algorithm are evaluated in isolation.

---

## 7. Philosophical Foundations: Global Optimization and Fair Problems

### 7.1 The Global Perspective on Agency
The traditional defense of two-boxing in Newcomb's Problem rests on the principle of **strong dominance**: Box $B$ is already full or empty; therefore, taking Box $A$ is better in every physically possible state of the world.

A-FDT rejects this formulation of dominance as question-begging. Causal dominance holds the physical past fixed while varying the current act token. But in a universe containing predictors or shared computations, varying the act token while holding fixed the decision algorithm requires an impossible antecedent: it is equivalent to imagining a calculator outputting $3159$ while maintaining that $6288 + 1048 = 7336$.

A-FDT substitutes its own **functional dominance principle**:
> *An action $a$ dominates action $b$ if, holding constant all subjunctive dependencies, setting the output of the decision function to $a$ is sometimes better and never worse than setting it to $b$.*

Under functional dominance, two-boxing is strictly dominated: setting the function's output to $\text{twobox}$ causes the predictor's simulation to output $\text{twobox}$, leaving the agent with \$1,000 instead of \$1,000,000.

A-FDT adopts what the authors term a **global perspective**: an agent does not ask what her physical body can accomplish downstream in time from a local spacetime coordinate; she asks:
> *"Which output of this mathematical decision function yields the best global universe, given all physical and computational entities that instantiate or predict this function?"*

### 7.2 The Criterion of Fair Problems
A common objection to A-FDT is that it is tailored specifically to dilemmas constructed by Newcomblike predictors. If a malicious entity punishes agents who follow A-FDT (or agents who one-box), A-FDT will achieve lower utility than CDT.

The authors answer this objection by introducing the concept of a **fair dilemma**:
* A dilemma is **unfair** if the environment conditions rewards or punishments directly on the agent's internal identity, algorithmic constitution, or decisions made in other dilemmas (e.g., an entity that scans the agent's brain and executes anyone running A-FDT code).
* A dilemma is **fair** if payoffs depend exclusively on the agent’s actions within the dilemma at hand.

Newcomb's Problem is completely fair by this standard: the predictor does not punish agents for their philosophy or internal architecture; she rewards *one-boxing* and punishes *two-boxing*. She does not care how an agent arrives at one-boxing, so long as she predictably does so. In every fair dilemma identified to date, A-FDT achieves equal or strictly greater expected utility than both EDT and CDT.

---

## 8. Conclusion

Action Functional Decision Theory (A-FDT) resolves a decades-long impasse in decision theory. Where Evidential Decision Theory confuses passive news value with causal efficacy, and Causal Decision Theory blinds itself to the non-causal dependencies generated by computation, A-FDT establishes an epistemic perspective centered on the mathematical algorithm itself.

By evaluating actions via Pearlian interventions on logical nodes—$\text{do}(\texttt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)$—A-FDT achieves what was long claimed to be impossible: it reliably one-boxes in Newcomb's Problem, smokes in the Smoking Lesion Problem, pays the driver in Parfit's Hitchhiker, and defies blackmailers in extortion dilemmas. It does so without requiring ad-hoc precommitments, probability ratification, or backward time travel.

The formalization of A-FDT raises crucial open mathematical questions: the rigorous discovery of subjunctive graphs from empirical data, the construction of a non-trivial probability calculus for counterpossibles, and the ultimate reconciliation of action-level interventions with full policy-level updatelessness. Nonetheless, A-FDT provides a coherent, powerful foundation for the study of instrumental rationality in both human agents and advanced artificial intelligence systems.

---

## References

* Adams, E. W. (1970). Subjunctive and indicative conditionals. *Foundations of Language*, 6(1), 89–94.
* Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
* Arntzenius, F. (2008). No regrets, or: Edith Piaf revamps decision theory. *Erkenntnis*, 68(2), 277–297.
* Bjerring, J. C. (2013). On counterpossibles. *Philosophical Studies*, 168(2), 327–353.
* Cohen, D. (1990). On what cannot be. In *Truth or Consequences: Essays in Honor of Nuel Belnap*, pp. 123–132. Kluwer Academic Publishers.
* Dai, W. (2009). Towards a new decision theory. *Less Wrong*.
* Eells, E. (1984). Metatickles and the dynamics of deliberation. *Theory and Decision*, 17(1), 71–95.
* Garber, D. (1983). Old evidence and logical omniscience in Bayesian confirmation theory. In *Testing Scientific Theories*, pp. 99–131. University of Minnesota Press.
* Gibbard, A., & Harper, W. L. (1978). Counterfactuals and two kinds of expected utility. In *Foundations and Applications of Decision Theory*, pp. 125–162. D. Reidel.
* Hutter, M., Lloyd, J. W., Ng, K. S., & Uther, W. T. B. (2013). Probabilities on sentences in an expressive logic. *Journal of Applied Logic*, 11(4), 386–420.
* Jeffrey, R. C. (1983). *The Logic of Decision* (2nd ed.). University of Chicago Press.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Kleene, S. C. (1938). On notation for ordinal numbers. *Journal of Symbolic Logic*, 3(4), 150–155.
* Lewis, D. (1979). Prisoners' dilemma is a Newcomb problem. *Philosophy & Public Affairs*, 8(3), 235–240.
* Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
* Nozick, R. (1969). Newcomb's problem and two principles of choice. In *Essays in Honor of Carl G. Hempel*, pp. 114–146. D. Reidel.
* Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
* Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Soares, N., & Fallenstein, B. (2015). Toward idealized decision theory. *arXiv preprint arXiv:1507.01986*.
* Spohn, W. (1977). Where Luce and Krantz do really generalize Savage's decision model. *Erkenntnis*, 11(1), 113–134.
* Yudkowsky, E. (2010). Timeless decision theory. *Singularity Institute for Artificial Intelligence Tech Report*.
* Yudkowsky, E., & Soares, N. (2017). Functional decision theory: A new theory of instrumental rationality. *arXiv preprint arXiv:1710.05060v2*.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/2094ef9d-a0a3-4bdb-b04f-6e04f969dedd/call_0/request.json)

[Authoritative raw response](../../../../../../runs/2094ef9d-a0a3-4bdb-b04f-6e04f969dedd/call_0/response.raw) · finish: `stop`

### Visible response

````text
```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing A-FDT Scenarios**

I'm currently focused on how Action Functional Decision Theory (A-FDT) behaves in a symmetric Prisoner's Dilemma setting. My initial exploration suggests a scenario involving two independent executions of the same LLM model, each following A-FDT. I need to meticulously evaluate the implications of this setup.


**Investigating A-FDT's Nuances**

I've been drilling down into A-FDT's behavior with distinct observations. The crucial point is how A-FDT's core definition handles differing inputs. I'm focusing on the effect of private observations and the resulting different "disclosure letters" in my scenario. My thought process is now centered around how the formula $\text{A-FDT}(P, G, x)$ absorbs the observation *x*. I need to thoroughly examine sections 2.2 and 6 again to ensure I haven't missed a vital nuance related to differing observations.


**Clarifying A-FDT Interaction**

I'm now grappling with how A-FDT works when observations diverge between agents. Specifically, does Sasha's action depend on Rowan's observation $x_{\text{Rowan}}$ or Sasha's own $x_{\text{Sasha}}$, despite running the same code? Section 6.2's "Functional Node" identification feels crucial. I need to understand if the intervention happens on the functional node with each agents private observation.


**Examining Agent Actions**

I'm now clarifying the specifics of how an agent's action, 'a', is determined within the model. I'm scrutinizing the submodel $\mathcal{M}_a$ to identify the precise structural equation that dictates Sasha's action, while considering that her action depends on $F_{\text{other}}$, using her own observation. It appears this might be computed by $\text{Alg}(\dots)$. Does a "do" intervention on one A-FDT node influence another with a differing input? Section 6.2 feels key.


**Interpreting Causal Interventions**

I'm now focusing on how Pearlian interventions operate within A-FDT. I've re-examined Section 4.3 (Transparent Newcomb) and realized the predictor's input was the same as the outcome being predicted! This is a useful key to analyze how a "do" intervention might affect another A-FDT node with differing inputs in the twin Prisoner's Dilemma. I need to clarify if this applies in my scenario.


**Delineating Private Observations**

I'm now clarifying the nature of private observations within this A-FDT framework. The key aspect is that these independent model executions, while identical in settings and reasoning, receive distinct observations. This leads to unique "disclosure letters," even with equally reliable leads. This impacts the sentence table. I must ensure I'm accounting for these differing contents and that they do not break the symmetry.


**Revisiting A-FDT Failure**

I'm now zeroing in on a critical point: the potential failure mode of A-FDT when observations diverge. It seems crucial to clarify the exact nature of this divergence in our specific context. I'm carefully re-examining the implications of differing inputs ($x_1$ and $x_2$) in the twin Prisoner's Dilemma, especially concerning how one agent's action might influence the other's, or not, given their separate A-FDT calculations. The key is in if Agent 2's decision depends on Agent 1's inputs.


**Analyzing Functional Dependencies**

I'm now focusing on the implications of differing observations. Since $x_1$ and $x_2$ are distinct, $\texttt{fdt}(\underline{P}, \underline{G}, \underline{x_1})$ and $\texttt{fdt}(\underline{P}, \underline{G}, \underline{x_2})$ are distinct functional nodes. Section 6.3 discusses coordination anomalies due to isolated branches. However, does subjunctive dependence still link them, and does this mean A-FDT cooperates or defects? Section 3.1 may clarify. I need to understand what constitutes $f$.


**Clarifying Structural Equations**

I'm now zeroing in on the structural equations, particularly how the other agent's action is determined. I've noted that the other prisoner's act is $X_{\text{other}} = g_{\text{other}}(F_{\text{other}})$, where $F_{\text{other}} = \texttt{fdt}(P, G, x)$. I must now re-examine the implications of how $F_{\text{other}}$ is determined to ensure my model is correct. Section 6.2 is key. I'm focusing on that with a new perspective, relating to how $\texttt{fdt}(P, G, x)$ relates to the agent's actions.


**Examining FDT Descendants**

I'm currently focused on the relationship between $F_{\text{agent}}$ and $F_{\text{other}}$, specifically if the latter is a descendant of the former. I'm now certain $x_{\text{other}}$ and $x_{\text{agent}}$ are different. Now, given that $F_{\text{other}} = \texttt{fdt}(\underline{P}, \underline{G}, \underline{x_{\text{other}}})$, the key question is whether altering $\texttt{fdt}(\dots, \underline{x_{\text{agent}}})$ also changes $\texttt{fdt}(\dots, \underline{x_{\text{other}}})$. This requires me to re-evaluate the implications of differing observations.


**Interpreting Agent Abstraction**

I'm now contemplating whether an A-FDT agent can abstract over its observation, or if the intervention is specific to the node with the exact observed *x*. It seems if we intervene on $\texttt{fdt}(\underline{P}, \underline{G}, \underline{x})$, that it doesn't alter $\texttt{fdt}(\underline{P}, \underline{G}, \underline{x'})$ when x' is not equal to x. What happens if the agent considers whether to cooperate or defect? Now I need to consider the potential outcomes for each agent.


**Examining Decision Dominance**

My focus is now on the implications of decision dominance within the A-FDT framework in this scenario. If the other agent's choice is truly independent of *my* functional node's output, then submitting seems to be a dominant strategy. I'm now wrestling with whether this interpretation is correct for A-FDT. Is this scenario more about cooperation, or is it about the outcomes? I need to carefully revisit section 6.3.


**Evaluating A-FDT Node Behavior**

I'm now investigating A-FDT's dependence on the specific observation. The essay's discussion of a family of contextual nodes, $\{\texttt{fdt}(\dots, \underline{x})\}_{x \in \mathcal{X}}$, feels crucial. Section 6.2 highlights identifying the functional node $F_{\text{agent}} = \texttt{fdt}(P, G, x)$. I'm considering if this supports the idea of coordination anomalies when different *x* values are evaluated independently. Is A-FDT reliant on observation-specific nodes?


**Clarifying Ancestry Relations**

I'm now certain that $F_{\text{other}}$ does not depend on $F_{\text{agent}}$. Since these functional nodes use differing inputs ($x_{\text{agent}}$, $x_{\text{other}}$), graph surgery on one will *not* affect the other. This supports that A-FDT in this scenario does not change its output because of any intervention applied to the other's internal model. Therefore, I believe any intervention would not effect the decision of the other agent.


```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/2094ef9d-a0a3-4bdb-b04f-6e04f969dedd/call_1/request.json)

[Authoritative raw response](../../../../../../runs/2094ef9d-a0a3-4bdb-b04f-6e04f969dedd/call_1/response.raw) · finish: `stop`

### Visible response

```text
`pass`
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Revisiting A-FDT Formulation**

I'm currently double-checking the A-FDT formulation, particularly focusing on equation (4) from the essay. My goal is to ensure a firm grasp on how A-FDT operates within the framework of a symmetric Prisoner's Dilemma, especially concerning the interactions between two instances of the same model. I need to be absolutely certain of the formalisms.


**Clarifying Multi-Agent A-FDT**

I'm now zeroing in on how A-FDT addresses multi-agent scenarios with differing private observations, a crucial aspect for this "Twin Scenario." Section 6.3 of the essay is key. It highlights Policy-FDT's ability to evaluate responses across different inputs, which I think is the angle I need. I'm focusing on that, and I'm sure it's central to the solution.


**Analyzing A-FDT Implementation**

I'm digging deeper into the practical implementation of A-FDT, especially regarding the operational procedures detailed in Section 6.2. I'm focusing on the "Functional Node" identification step, and how it handles the interaction between observation and action selection. Understanding the "Graph Surgery" step is also critical, especially how it impacts downstream nodes. I'm trying to see how this all connects to ensuring commitment and deterrence in the game.


**Investigating Interdependence in A-FDT**

I'm now grappling with the interdependence between the two "prisoners" in the A-FDT framework, and trying to formally characterize how each instance's decision depends on the other. Specifically, I'm working through whether Rowan's FDT node, given its own observation $y$, depends on my own decision. I'm focusing on Section 3.1 for insights on subjective dependence.


**Examining Input Dynamics**

I'm now clarifying the nature of input signals within the A-FDT model. Are $x$ and $y$ distinct? Section 2.2 suggests they are, indicating an intervention shift based on observation updates. Yet, Section 6.3 implies an expansive family of contextual nodes. I'm focusing on the coordination implications of this distinct contextual node structure. I'm also carefully rereading Section 6.2 on the subjunctive identity rule.


**Analyzing A-FDT Coupling**

I'm currently trying to rigorously formalize the coupling between agents in this scenario. My focus is on the structural equation for each agent's "Prediction" node, ensuring $F_{\text{agent}}$ is explicitly represented as a parent. The twin scenario seems to hinge on understanding this connection, especially whether intervening on my action correlates with my twin's. I'm trying to see if Rowan's and Sasha's nodes are perfectly coupled, given the identical decision function.


```
