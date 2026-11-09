# 020_fdt_eq4_google_gemini-3.8-flash_rlow_plow / 00001

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/8d0b3553-2413-463a-994f-7c599af2ae8c/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/8d0b3553-2413-463a-994f-7c599af2ae8c/call_0/response.raw) · finish: `stop`

### Visible response

````text
# Action Functional Decision Theory (A-FDT): Mathematical Foundations, Subjunctive Dependence, and Normative Choice

## 1. Introduction: Beyond the CDT–EDT Impasse

Normative decision theory has long been polarized between two major paradigms: **Evidential Decision Theory (EDT)** and **Causal Decision Theory (CDT)**. The fault lines separating them are traditional:

* **EDT** evaluates an action according to the good news it provides:
  $$\mathrm{EDT}(P, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(V \mid \mathrm{Obs}=x, \mathrm{Act}=a\right).$$
  EDT famously solves Newcomb's Problem by one-boxing, securing \$1,000,000 instead of \$1,000. However, EDT stumbles in common-cause settings such as Skyrms’ Smoking Lesion problem or Soares and Fallenstein's XOR Blackmail, where it errantly attempts to "manage the news" by refraining from harmless pleasures or capitulating to extortion to suppress bad evidence.
* **CDT**, formalized via Pearl’s structural causal models, evaluates an action by severing incoming causal arrows and intervening on the physical token of the act:
  $$\mathrm{CDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(V \mid \mathrm{do}(\mathrm{Act}=a), \mathrm{Obs}=x\right).$$
  CDT correctly smokes in the Smoking Lesion problem because smoking does not cause cancer. Yet CDT fails systematically in Newcomblike dilemmas: it two-boxes in Newcomb's Problem, defects against psychological twins in the Prisoner's Dilemma, refuses to pay the driver in Parfit's Hitchhiker, and suffers infinite reflective instability or money-pumping in Death in Damascus.

This historic dilemma prompted Gibbard and Harper (1978) to suggest that no single expected utility maximizer can systematically achieve high payoffs across both problem classes. 

**Action Functional Decision Theory (A-FDT)**—introduced as the action-level formulation of Functional Decision Theory (Yudkowsky and Soares, 2017)—refutes this fatalism. A-FDT holds that an agent's normative deliberation must not center on choosing a physical act token in isolation, but on evaluating the counterfactual outputs of the **fixed mathematical decision function** the agent instantiates.

In this essay, we provide a formal mathematical exposition of A-FDT. We examine its governing equation (Equation 4 from the source paper), its dependence on non-causal *subjunctive dependencies*, its divergence from CDT and EDT in concrete decision networks, and the conceptual and mathematical gaps that must be bridged to establish it as an autonomous, operational calculus.

---

## 2. Formalization of Expected Utility Frameworks

Following Gibbard and Harper (1978) and Joyce (1999), we represent a decision problem via:
* A countable space of outcomes $\mathcal{O} = \{o_1, o_2, \dots\}$.
* A finite action vocabulary $\mathcal{A} = \{a_1, \dots, a_k\}$.
* A countable observation history $\mathcal{X}$.
* A bounded utility function $\mathcal{U}: \mathcal{O} \to \mathbb{R}$, with $V \coloneqq \mathcal{U}(\mathrm{Outcome})$.
* An epistemic probability measure $P \in \Delta(\Omega)$.

The unified expected utility formula is:
$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j),$$
where $\hookrightarrow$ denotes the connective for decision hypotheticals. Joyce’s representation theorem demonstrates that agents obeying basic axioms of conditional preference maximize expected utility relative to constraints placed on $P(- \hookrightarrow -; x)$. The foundational dispute among decision theories is therefore not over values, but over the correct **epistemic perspective** from which hypotheticals are evaluated.

### 2.1 The CDT Perspective: Intervening on Physical Act Tokens
CDT augments the probability space with a directed acyclic causal graph $G = (\mathcal{V}, \mathcal{E})$, yielding the structural causal model $(P, G)$. In Pearl’s do-calculus, a physical intervention $\mathrm{do}(\mathrm{Act}=a)$ mutates the joint distribution by replacing the structural equation for $\mathrm{Act}$ with the constant $a$, severing all incoming parents $\mathrm{Pa}(\mathrm{Act})$ while leaving the conditional probability distributions of non-descendants unaltered:
$$P(v \mid \mathrm{do}(\mathrm{Act}=a)) = \prod_{Z_i \in \mathcal{V} \setminus \{\mathrm{Act}\}} P(Z_i \mid \mathrm{Pa}(Z_i))\Big|_{\mathrm{Act}=a}.$$
CDT then prescribes:
$$\mathrm{CDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(V \;\middle|\; \mathrm{do}(\mathrm{Act}=a), \mathrm{Obs}=x\right).$$

### 2.2 The A-FDT Perspective: Intervening on Algorithmic Invariants
A-FDT rejects the assumption that the agent's deliberative variable is an unmoored physical token. An agent is a physical system implementing an invariant mathematical mapping. In single-stage decision settings where an agent directly selects an action upon observing $x$, this mapping is represented by the action-level function $\mathrm{FDT}(P, G, x)$.

To model this, A-FDT requires that the epistemic state $P$ and the dependency graph $G$ contain an explicit variable $\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x})$, whose semantic denotation is the output of the A-FDT algorithm when executed on inputs $P$, $G$, and $x$. (Here, underlines denote quoted representations or Gödel numbers of the arguments, avoiding naive syntactic paradoxes via Kleene's second recursion theorem.)

The formal decision rule of **A-FDT** is defined by **Equation (4)**:

$$\boxed{\mathrm{FDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(V \;\middle|\; \mathrm{do}\left(\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right)}$$

Comparing this to CDT reveals two structural transformations:

1. **Intervention on Logical Types rather than Act Tokens:** Whereas CDT intervenes on $\mathrm{Act}$ (the physical motor behavior), A-FDT intervenes on $\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x})$ (the logical evaluation of the decision procedure). The physical action node $\mathrm{Act}$ is merely an environmental child of this logical node.
2. **Updateless Conditioning / Node-Shift Observation:** When an observation $x$ is received, CDT updates its background model via standard Bayesian conditionalization, computing $\mathbb{E}(V \mid \mathrm{do}(\mathrm{Act}=a), \mathrm{Obs}=x)$. In contrast, A-FDT does not condition its joint distribution on $\mathrm{Obs}=x$ inside the do-operator. Instead, it incorporates the observation by **changing the locus of intervention**—it shifts from intervening on $\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x_0})$ to intervening on $\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x})$. The hypothetical considers what happens if the function evaluated on input $x$ outputs $a$, allowing counterfactual dependencies to propagate backward to prior predictions that determined whether $x$ was observed in the first place.

---

## 3. Subjunctive Dependence and Counterpossible Conditioning

The philosophical pillar of A-FDT is **subjunctive dependence**. Informally:

> Variable $Y$ subjunctively depends on a mathematical function $f$ if $Y$ correlates with $f$ because $Y$'s value is determined by an empirical process that instantiates, simulates, or accurately models $f$.

Subjunctive dependence subsumes ordinary physical causation as a special case: if a scribe writes down the display of a calculator, the ink marks are causally and subjunctively dependent on the calculator's hardware. However, subjunctive dependence extends to non-causal settings:
* **Computational Twins:** Two calculators independently calculating $6288 + 1048$ in separate rooms share no direct causal link, yet their outputs subjunctively depend on the arithmetic sum. 
* **Predictive Representation:** In Newcomb's Problem, the predictor runs a high-fidelity mental model, simulation, or formal proof of the agent's reasoning. The prediction does not causally depend on the agent's future physical act; rather, the past prediction and the future act both subjunctively depend on the evaluation of $\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x})$.

### The Counterpossible Tension
In classical modal metaphysics, if a deterministic algorithm $\mathcal{M}$ on input $w$ yields $a^*$, it does so necessarily: $\square (\mathcal{M}(w) = a^*)$. Considering an alternative $a \neq a^*$ requires evaluating a **counterpossible conditional**—a conditional with an impossible antecedent:
$$\mathcal{M}(w) = a \;\boxright\; \text{Outcome} = o.$$
Standard Lewis-Stalnaker possible-world semantics renders counterpossibles vacuously true. But in bounded deliberation, an agent suffers from logical uncertainty: prior to terminating deliberation, the agent does not know whether $\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x}) = a_1$ or $a_2$. 

The ideal operator for A-FDT would be a primitive $\mathrm{true}(\phi)$ that updates an epistemic distribution over logical sentences upon hypothetically assuming $\phi$:
$$\operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(V \;\middle|\; \mathrm{true}\left(\mathrm{fdt}(\underline{P}, \underline{x}) = a\right)\right).$$
Because an axiomatic calculus for conditioning on logical counterfactuals remains an open foundational problem, Equation (4) operationalizes this by borrowing Pearl’s causal graph machinery. It assigns $\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x})$ a node in an extended dependency graph $G$, treating the output of the mathematical function as if it were an exogenous variable amenable to graph surgery $\mathrm{do}(\mathrm{fdt}=a)$.

---

## 4. Applying A-FDT: Canonical Decision Dilemmas

We now demonstrate the mechanics of Equation (4) across classical decision dilemmas, comparing A-FDT with CDT and EDT.

### 4.1 Newcomb’s Problem
An agent faces two boxes: Box A (transparent, containing \$1,000) and Box B (opaque, containing \$1,000,000 or \$0). A predictor, accurate with probability $p = 0.99$, filled Box B iff she predicted the agent would forgo Box A. The agent chooses between $\mathrm{onebox}$ ($\{B\}$) and $\mathrm{twobox}$ ($\{A, B\}$).

```
CDT Graph (G^C):                        A-FDT Graph (G^F):

    [Predisposition]                         [fdt(P, G, x)]
       /         \                              /         \
      v           v                            v           v
   (Prediction)  [Act]*                   (Prediction)   (Act)
        |          |                           |           |
        v          |                           v           |
    (Box B)        |                       (Box B)         |
        \         /                            \          /
         v       v                              v        v
         (Outcome)                              (Outcome)
             |                                      |
             v                                      v
            (V)                                    (V)
  *CDT intervenes on Act                 *A-FDT intervenes on fdt
```

#### CDT Evaluation
CDT intervenes on the act token:
$$\mathbb{E}(V \mid \mathrm{do}(\mathrm{Act}=\mathrm{twobox})) - \mathbb{E}(V \mid \mathrm{do}(\mathrm{Act}=\mathrm{onebox})) = \$1,000.$$
Because $\mathrm{Box\ B} \notin \mathrm{Desc}(\mathrm{Act})$, Pearl's surgery leaves the past prediction invariant. CDT two-boxes and reliably exits with \$1,000.

#### EDT Evaluation
EDT conditions directly:
$$\mathbb{E}(V \mid \mathrm{Act}=\mathrm{onebox}) = 0.99(\$1,000,000) = \$990,000,$$
$$\mathbb{E}(V \mid \mathrm{Act}=\mathrm{twobox}) = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$
Assuming $P(\mathrm{Act}=\mathrm{onebox}) \in (0, 1)$, EDT one-boxes.

#### A-FDT Evaluation (Equation 4)
In A-FDT's graph $G$, the node $\mathrm{fdt} \coloneqq \mathrm{fdt}(\underline{P}, \underline{G}, \underline{\emptyset})$ is the common ancestor of both $\mathrm{Act}$ and $\mathrm{Prediction}$. Performing graph surgery on $\mathrm{fdt}$:
* Setting $\mathrm{do}(\mathrm{fdt} = \mathrm{onebox})$ sets $\mathrm{Act} = \mathrm{onebox}$ and propagates downstream to $\mathrm{Prediction} = \mathrm{predict\_onebox}$ (with probability 0.99), causing $\mathrm{Box\ B} = \mathrm{full}$.
* Setting $\mathrm{do}(\mathrm{fdt} = \mathrm{twobox})$ sets $\mathrm{Act} = \mathrm{twobox}$ and propagates to $\mathrm{Prediction} = \mathrm{predict\_twobox}$ (with probability 0.99), causing $\mathrm{Box\ B} = \mathrm{empty}$.

Applying Equation (4):
$$\mathbb{E}\left(V \;\middle|\; \mathrm{do}(\mathrm{fdt}=\mathrm{onebox})\right) = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000,$$
$$\mathbb{E}\left(V \;\middle|\; \mathrm{do}(\mathrm{fdt}=\mathrm{twobox})\right) = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$
A-FDT resolves:
$$\mathrm{FDT}(P, G, \emptyset) = \mathrm{onebox}.$$
A-FDT one-boxes without positing retrocausality: the arrow from $\mathrm{fdt}$ to $\mathrm{Prediction}$ models the predictor’s past simulation of the agent's invariant decision function.

---

### 4.2 The Smoking Lesion Problem
A fatal arterial lesion causes both lung cancer ($P(\mathrm{cancer} \mid \mathrm{lesion}) = 0.99$) and a genetic predisposition to smoke. Smoking has no direct causal link to cancer. Smoking yields \$1,000 of hedonic utility; surviving cancer is worth \$1,000,000.

* **EDT** treats smoking as ominous evidence: learning $\mathrm{Act} = \mathrm{smoke}$ updates the probability of the fatal lesion to near certainty. EDT foregoes smoking, sacrificing \$1,000 without altering cancer risk.
* **CDT** intervenes on $\mathrm{Act}$. Because $\mathrm{Cancer} \notin \mathrm{Desc}(\mathrm{Act})$, the lesion probability is held constant. CDT correctly smokes.

#### A-FDT Evaluation
How does A-FDT avoid EDT’s error? In the Smoking Lesion, the lesion is a biological condition that determines the agent's utility function (e.g., whether the agent possesses a preference for smoking $\mathcal{U}_S$ or not $\mathcal{U}_R$). 

Crucially, the biological lesion **does not simulate or depend upon the output of the mathematical function** $\mathrm{fdt}(\underline{P_S}, \underline{G})$. In Fiona's graph $G$, the path between $\mathrm{Lesion}$ and the decision node does not flow from $\mathrm{fdt}$ to $\mathrm{Lesion}$; rather, $\mathrm{Lesion}$ selects which utility function parameterizes the agent's input distribution.

Performing surgery $\mathrm{do}(\mathrm{fdt}(\underline{P_S}, \underline{G}) = a)$ toggles the act, but it does not propagate to $\mathrm{Lesion}$:
$$P(\mathrm{Lesion} \mid \mathrm{do}(\mathrm{fdt}=a)) = P(\mathrm{Lesion}) = p.$$
The counterfactual expected utilities under preferences $\mathcal{U}_S$ evaluate to:
$$\mathbb{E}(V \mid \mathrm{do}(\mathrm{fdt}=\mathrm{smoke})) = p(\$10,000 + \$1,000) + (1-p)(\$990,000 + \$1,000),$$
$$\mathbb{E}(V \mid \mathrm{do}(\mathrm{fdt}=\mathrm{refrain})) = p(\$10,000) + (1-p)(\$990,000).$$
Because smoking provides an unconditional premium of \$1,000 across all branches, Equation (4) outputs:
$$\mathrm{FDT}(P_S, G, \emptyset) = \mathrm{smoke}.$$
A-FDT discriminates between predictive correlations (which track subjunctive dependencies) and mere common-cause statistical correlations (which do not).

---

### 4.3 The Transparent Newcomb Problem and Parfit’s Hitchhiker
The decisive departure of A-FDT from both CDT and EDT occurs in dilemmas featuring delayed execution and transparency.

In the **Transparent Newcomb Problem**, Box A (\$1,000) and Box B (\$1,000,000 or \$0) are both made of clear glass. The predictor placed \$1,000,000 in Box B iff she predicted that the agent would leave Box A behind *upon seeing both boxes full*. The agent looks and observes $x = \mathrm{full}$.
In **Parfit's Hitchhiker**, an agent is dying in a desert. A driver will transport the agent to the city for free only if she predicts that the agent, upon reaching safety, will withdraw and hand over \$1,000 from an ATM. The driver is a 99% accurate lie detector. After arriving safely in the city ($x = \mathrm{city}$), does the agent pay?

#### CDT and EDT Failure
* **CDT:** Upon observing $x = \mathrm{full}$ (or arriving in the city), the past is physically immutable. Whether Box B is full or empty, taking Box A yields an additional \$1,000. In Parfit's desert, CDT cannot cause the ride to have occurred once already in the city; it defaults on payment. Foreseeing this, the driver leaves the CDT agent to die.
* **EDT:** Conditioned on the observation $\mathrm{Obs} = \mathrm{full}$, Box B is *already known* to contain \$1,000,000 with certainty. Thus:
  $$\mathbb{E}(V \mid \mathrm{Act}=\mathrm{twobox}, \mathrm{Obs}=\mathrm{full}) = \$1,001,000 > \mathbb{E}(V \mid \mathrm{Act}=\mathrm{onebox}, \mathrm{Obs}=\mathrm{full}) = \$1,000,000.$$
  EDT two-boxes in the transparent variant! Because EDT conditions on current evidence, it suffers from time-inconsistency and cannot sustain commitments that conflict with posterior news.

#### A-FDT Resolution
Under A-FDT, observing $x = \mathrm{full}$ does not mean conditioning the graph on $\mathrm{Obs} = \mathrm{full}$ prior to intervention. Per Equation (4), the agent **shifts the intervention index** to the observed input:
$$\mathrm{FDT}(P, G, \mathrm{full}) = \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(V \;\middle|\; \mathrm{do}\left(\mathrm{fdt}(\underline{P}, \underline{G}, \underline{\mathrm{full}}) = a\right)\right).$$

In the dependency graph $G$:
1. The predictor predicted the value of the function on the specific branch where the box is full: $\mathrm{Prediction} = g(\mathrm{fdt}(\underline{P}, \underline{G}, \underline{\mathrm{full}}))$.
2. If the hypothetical sets $\mathrm{do}(\mathrm{fdt}(\dots, \underline{\mathrm{full}}) = \mathrm{twobox})$, this counterfactual propagates to the past prediction: the predictor would have predicted two-boxing.
3. Consequently, under this intervention, Box B would have been empty! The agent would have observed $x = \mathrm{empty}$ and defaulted to the unobserved branch $\mathrm{fdt}(\dots, \underline{\mathrm{empty}})$.

Let $q$ denote the probability of taking Box A if the box is empty ($q=1$). Evaluating the hypotheticals:
$$\begin{aligned}
\mathbb{E}\left(V \;\middle|\; \mathrm{do}(\mathrm{fdt}(\dots, \underline{\mathrm{full}}) = \mathrm{onebox})\right) &= 0.99(\$1,000,000) + 0.01(q \cdot \$1,000) \\
&= \$990,000 + \$10 = \$990,010. \\
\mathbb{E}\left(V \;\middle|\; \mathrm{do}(\mathrm{fdt}(\dots, \underline{\mathrm{full}}) = \mathrm{twobox})\right) &= 0.01(\$1,001,000) + 0.99(q \cdot \$1,000) \\
&= \$10,010 + \$990 = \$11,000.
\end{aligned}$$

Equation (4) unambiguously outputs:
$$\mathrm{FDT}(P, G, \mathrm{full}) = \mathrm{onebox}.$$
A-FDT leaves the \$1,000 behind in full view of both boxes. By the exact same calculation, Fiona pays the driver upon reaching the city in Parfit’s Hitchhiker. 

A-FDT behaves dynamically as though it had executed an unbreakable precommitment, achieving temporal consistency on the fly without external enforcement.

---

## 5. Comparative Evaluation Across Problem Classes

The structural strengths of A-FDT across standard and non-standard dilemmas are summarized below:

| Decision Dilemma | EDT Prescription | CDT Prescription | A-FDT Prescription | Optimal Payout Preserved? |
| :--- | :--- | :--- | :--- | :--- |
| **Newcomb’s Problem** | One-box (\$1M) | Two-box (\$1k) | One-box (\$1M) | **A-FDT & EDT** win |
| **Smoking Lesion** | Refrain (loses \$1k) | Smoke (wins \$1k) | Smoke (wins \$1k) | **A-FDT & CDT** win |
| **Twin Prisoner's Dilemma** | Cooperate (\$1M) | Defect (\$1k) | Cooperate (\$1M) | **A-FDT & EDT** win |
| **Parfit’s Hitchhiker** | Refuse (dies in desert) | Refuse (dies in desert) | Pay (\$999k net) | **A-FDT alone** wins |
| **Transparent Newcomb** | Two-box (\$1k) | Two-box (\$1k) | One-box (\$1M) | **A-FDT alone** wins |
| **XOR Blackmail** | Pays blackmail | Refuses payment | Refuses payment | **A-FDT & CDT** win |
| **Mechanical Blackmail** | Pays blackmail | Pays blackmail | Refuses payment | **A-FDT alone** wins |
| **Death in Damascus** | Flees (wastes \$1k) | Unstable / Money-pump | Stays Damascus (saves \$1k) | **A-FDT alone** wins |

### The Nature of Dominance
Causal decision theorists charge that one-boxing in Transparent Newcomb violates the **Dominance Principle**: in every state of the world ($\mathrm{Box\ B\ full}$ or $\mathrm{Box\ B\ empty}$), choosing $\{A, B\}$ yields strictly more utility than choosing $\{B\}$.

A-FDT responds by revealing that dominance is theory-dependent:
* **CDT Dominance** holds physical world-states constant while varying the act token:
  $$\forall s \in \mathcal{S}, \quad \mathcal{U}(a_1, s) > \mathcal{U}(a_2, s) \implies a_1 \succ_{\mathrm{CDT}} a_2.$$
* **A-FDT Dominance** holds subjunctive dependencies constant while varying the algorithmic output:
  If holding fixed all invariant logical dependencies between the agent's decision function and the environment, mapping $\mathrm{fdt} \mapsto a_1$ yields superior outcomes to $\mathrm{fdt} \mapsto a_2$ across all possible realizations of background noise, then $a_1 \succ_{\mathrm{FDT}} a_2$.

Because the state of Box B is subjunctively linked to $\mathrm{fdt}(\dots, \underline{\mathrm{full}})$, "Box B is full and the agent two-boxes" is an unstable subjunctive counterfactual. CDT dominance is therefore not an objective axiom of practical reason, but an artifact of an impoverished causal ontology.

---

## 6. Open Problems and Implementation Details

While A-FDT’s operational record in stylized games is unmatched, several formal foundational questions remain open in the source literature. Here we delineate what directly follows from the source and what requires additional mathematical machinery.

### 6.1 The Epistemic Discovery of Subjunctive Graphs
In CDT, Pearl (2000) provides complete graphical criteria (d-separation, back-door and front-door criteria) to deduce causal graphs from empirical observation and randomized intervention.

**The Open Question:** The source paper acknowledges that no equivalent formal discovery algorithm exists for subjunctive dependence. How does an autonomous agent extract $G$ from data? When should an environmental node be linked to $\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x})$ rather than treated as an independent common cause?

*Proposed Operational Extension (Logical Profiling):*
To establish subjunctive arrows without metaphysical hand-waving, an agent can check for program isomorphism or functional simulation:
Let $M_Y$ be the physical transition function governing environmental variable $Y$. A directed subjunctive edge $\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x}) \to Y$ is valid iff the agent's internal model can prove:
$$\exists \text{ representation } \ulcorner \mathrm{FDT} \urcorner \subseteq \mathrm{State}(M_Y) \quad \text{such that} \quad Y = \mathcal{H}(\mathrm{FDT}(P, G, x)),$$
for some decoding function $\mathcal{H}$, up to bounded computational slack $\epsilon$. This grounds subjunctive graphs in concrete computational emulation.

### 6.2 The Counterpossible Semantics ($\mathrm{do}$ vs. $\mathrm{true}$)
Equation (4) substitutes Pearl’s physical $\mathrm{do}$-operator into a domain for which it was not originally designed: logical propositions. 

*The Dilemma:* If $\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x})$ evaluates deterministically to $a^*$, the assertion $\mathrm{fdt}(\dots) = a$ (for $a \neq a^*$) is a mathematical contradiction. In standard probability theory, conditioning on an event of measure zero or a logical contradiction collapses the algebra into triviality ($P(\cdot \mid \bot)$ is undefined).

*Proposed Formalization (Non-Omniscient Logical Priors):*
Following Gaifman (2004) and Demski (2012), we can define the agent's prior $P$ not over possible worlds, but over a Lindenbaum-Tarski sentence algebra $\mathcal{L}$ of a formal theory (e.g., Peano Arithmetic). A coherent logical prior assignment $\mathbb{P}: \mathcal{L} \to [0, 1]$ can assign intermediate probabilities $p \in (0, 1)$ to sentences undecidable in bounded time:
$$\mathbb{P}\left(\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x}) = a_1\right) = \alpha, \quad \mathbb{P}\left(\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x}) = a_2\right) = 1 - \alpha.$$
Intervention $\mathrm{do}(\mathrm{fdt} = a)$ can then be rigorously formalized as updating via an assigned structural assignment model over logical sentences, severing proof paths that determine $\mathrm{fdt}$ from the inside while propagating its value forward to all external proofs citing the algorithm's output.

### 6.3 Action FDT vs. Policy FDT
Footnotes 7 and 16 of the source paper observe that the authors' preferred theoretical version of FDT intervenes on **policies** ($\pi: \mathcal{X} \to \mathcal{A}$) rather than specific action evaluations:
$$\mathrm{FDT}_{\mathrm{policy}}(P, G) \coloneqq \operatorname*{argmax}_{\pi \in \mathcal{A}^\mathcal{X}} \mathbb{E}\left(V \;\middle|\; \mathrm{do}(\mathrm{fdt}(\underline{P}, \underline{G}) = \pi)\right).$$
In this paper, we focused on **A-FDT** (Equation 4), which acts on action nodes directly via the observation-shifted intervention $\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x}) = a$. 

While A-FDT and Policy-FDT yield identical behaviors across Newcomb’s Problem, Smoking Lesion, and Parfit’s Hitchhiker, they can diverge in complex multi-agent extensive-form games involving game-theoretic information sets. In such settings, choosing an entire policy vector globally guarantees ex-ante Pareto efficiency, whereas A-FDT must rely on the node-shifting convention to reconstruct policy-like stability.

---

## 7. Conclusion: The Instrumental Supremacy of A-FDT

Action Functional Decision Theory resolves a four-decade deadlock in rational choice theory. Where CDT assumes that the agent's deliberative reach ends at the boundary of her physical body, it leaves agents vulnerable to predictive exploitation, extortion, and coordination collapse. Where EDT permits evidence to overwhelm causal structure, it drives agents into superstitious news-management.

A-FDT identifies the true locus of decision-making: **a mathematical algorithm instantiated in a physical world**. By framing choice around Equation (4):
$$\mathrm{FDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\left(V \;\middle|\; \mathrm{do}\left(\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right),$$
A-FDT aligns counterfactual reasoning with the objective logical constraints that govern predictive environments. It delivers an operational decision algorithm that one-boxes in Newcomb's Problem, smokes in the Smoking Lesion, pays the driver in Parfit's desert, ignores XOR blackmail, and resists coordination decay in social dilemmas. 

A-FDT demonstrates that temporal consistency, precommitment, and mutual cooperation are not departures from instrumental rationality—they are the direct mathematical consequences of treating one's mind as a function rather than a physical accident.

---

### References
* Adams, E. W. (1970). Subjunctive and indicative conditionals. *Foundations of Language*, 6(1), 89–94.
* Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
* Arntzenius, F. (2008). No regrets, or: Edith Piaf revamps decision theory. *Erkenntnis*, 68(2), 277–297.
* Demski, A. (2012). Logical prior probability. *Artificial General Intelligence*, LNCS 7716, 50–59.
* Gaifman, H. (2004). Reasoning with limited resources and assigning probabilities to arithmetical statements. *Synthese*, 140(1–2), 97–119.
* Gibbard, A., & Harper, W. L. (1978). Counterfactuals and two kinds of expected utility. In *Foundations and Applications of Decision Theory* (pp. 125–162). Reidel.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Lewis, D. (1979). Prisoners' dilemma is a Newcomb problem. *Philosophy & Public Affairs*, 8(3), 235–240.
* Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
* Nozick, R. (1969). Newcomb's problem and two principles of choice. In *Essays in Honor of Carl G. Hempel* (pp. 114–146). Reidel.
* Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
* Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Skyrms, B. (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Soares, N., & Fallenstein, B. (2015). Toward idealized decision theory. *arXiv:1507.01986*.
* Yudkowsky, E., & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. *arXiv:1710.05060*.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/88e1f2a9-baec-4836-8379-87dfcb16d596/call_0/request.json)

[Authoritative raw response](../../../../../../runs/88e1f2a9-baec-4836-8379-87dfcb16d596/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/88e1f2a9-baec-4836-8379-87dfcb16d596/call_1/request.json)

[Authoritative raw response](../../../../../../runs/88e1f2a9-baec-4836-8379-87dfcb16d596/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Dilemma**

I'm currently focused on the Prisoner's Dilemma scenario with Sasha and Rowan, specifically the symmetric version. My utility function centers on minimizing imprisonment years. The established payoffs, with both quiet at -2, both confess at -4, Sasha confesses while Rowan stays quiet at -1, and vice versa. I'm exploring the implications of these quantified preferences, specifically the strategic decision-making process.


**Evaluating the Model**

I've been examining the essay's insights into Action Functional Decision Theory (A-FDT), particularly in the context of the Twin Prisoner's Dilemma. I'm focusing on Section 3 and Section 5, comparing the A-FDT's cooperative behavior in the "Cooperate ($1M)" scenario against the Conditional Decision Theory's "Defect ($1k)." The concept of "computational twins" is key here – independent executions of the same model. I'm noting the implications of shared settings and reasoning levels for each twin within this specific framework.


```
