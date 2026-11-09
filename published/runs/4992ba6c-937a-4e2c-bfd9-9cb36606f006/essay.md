# Rationality Across Counterfactual Types: A Mathematical Account of Action Functional Decision Theory (A-FDT)

## 1. Introduction: Beyond Evidential and Causal Orthodoxy

Normative decision theory has long been divided between two classical formalisms: **Evidential Decision Theory (EDT)** and **Causal Decision Theory (CDT)**. The fault lines between them are exposed in scenarios where an agent's current choice correlates with an environmental variable that is causally upstream of, or physically isolated from, that choice. 

In Newcomb's Problem, a reliable predictor fills an opaque box $B$ with $\$1,000,000$ if and only if she predicts that the agent will leave behind a transparent box $A$ containing $\$1,000$. EDT recommends taking only box $B$ ("one-boxing") because learning that one one-boxed constitutes excellent evidence that box $B$ contains $\$1,000,000$. CDT diagnoses this reasoning as a fallacy of "managing the news": because the predictor has already placed the money or departed, the agent's physical choice cannot retroactively cause the box's contents to change. CDT holds that taking both boxes ("two-boxing") strictly dominates one-boxing, and so two-boxes, almost inevitably walking away with only $\$1,000$.

Yet EDT's triumph in Newcomb's dilemma reverses in Skyrms' Smoking Lesion Problem. There, an unobservable arterial lesion is a common cause of both a propensity to smoke and fatal lung cancer, with no direct causal bridge between smoking and malignancy. EDT agents refrain from smoking because smoking provides bad news about possessing the fatal lesion; CDT agents smoke, recognizing that refraining does not causally avert cancer while sacrificing the immediate hedonic benefit of smoking.

The classic taxonomy of Gibbard and Harper (1978) suggested that an agent must choose between two packages: either one-box and refrain (EDT), or two-box and smoke (CDT). The thesis of Functional Decision Theory (FDT), introduced by Yudkowsky and Soares, is that this dilemma rests on a false dichotomy regarding the object of intervention. In this essay, we examine the formal operationalization of this framework known as **Action Functional Decision Theory (A-FDT)**, formalized by Equation (4), Section 5 of their work:

$$\text{A-FDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(V \;\middle|\; \mathtt{do}\Big(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\Big)\right).$$

Rather than intervening on a physical token of action—such as an arm reaching for a box—an A-FDT agent intervenes on the *logical type* of her decision procedure itself. Below, we articulate the mathematical foundations of A-FDT, explain its operationalization of counterfactuals, compare its mechanics against CDT and EDT, and trace out its implications across classic and unfamiliar decision dilemmas.

---

## 2. Foundations and Formal Definition of A-FDT

### 2.1 The Joyce Representation Setting
Following Joyce (1999), expected utility theories share an overarching optimization format. Given a countable set of outcomes $\mathcal{O}$, a finite set of actions $\mathcal{A}$, an observation history $x \in \mathcal{X}$, and a bounded utility function $\mathcal{U}: \mathcal{O} \to \mathbb{R}$, an agent selects an action $a$ maximizing:

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \then o_j ;\, x) \cdot \mathcal{U}(o_j),$$

where "$\then$" denotes the connective for decision hypotheticals.

* **EDT** resolves $P(a \then o_j ;\, x)$ via standard Bayesian conditionalization on the physical act node:
  $$\text{EDT}(P, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\big(V \mid \text{Obs}=x, \text{Act}=a\big),$$
  where $V \coloneqq \mathcal{U}(\text{Outcome})$.
* **CDT** resolves $P(a \then o_j ;\, x)$ by intervening on the physical token $\text{Act}$ using Pearl's (1996, 2000) causal graph $(P, G)$:
  $$\text{CDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\big(V \mid \mathtt{do}(\text{Act}=a), \text{Obs}=x\big).$$

### 2.2 The A-FDT Formalism
A-FDT alters this architecture by transforming the locus of choice from a physical event variable $\text{Act}$ to a mathematical variable representing the evaluation of the decision algorithm itself. 

Let an agent's cognitive model be given by a pair $(P, G)$, where:
1. $P$ is a probability distribution over a set of discrete random variables. Crucially, the domain of $P$ includes logical/algorithmic variables. In particular, for inputs $(P, G, x)$, there exists a variable $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ representing the output of the A-FDT procedure on those arguments. (Here, the underline denotes a syntactic quote or Gödel number encoding the arguments, permitting self-reference via Kleene's recursion theorem without circularity).
2. $G = (\mathcal{V}, \mathcal{E})$ is a directed acyclic graph (DAG) representing *subjunctive dependence*. In $G$, arrows capture how mathematical truths, simulations, and physical mechanisms propagate dependencies across the universe.

The formal decision rule of A-FDT is:

$$\text{A-FDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(V \;\middle|\; \mathtt{do}\Big(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\Big)\right). \tag{1}$$

Two structural features of Equation (1) sharply distinguish A-FDT from CDT:

1. **Logical Intervention (Type vs. Token):** In CDT, the $\mathtt{do}$-operator operates on $\text{Act}$, severing the incoming causal edges to the physical body's motion. In A-FDT, the $\mathtt{do}$-operator is applied to $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$. Any variable in the world that subjunctively depends on what this algorithm outputs—such as an external simulation run by a predictor, a clone running identical code, or the agent's own physical action—is causally/subjunctively downstream of that node in $G$. Thus, intervening on the algorithm naturally propagates to all identical instantiations.
2. **Dynamic Locus of Intervention vs. Observation Conditioning:** When a CDT agent receives an observation $x$, she conditions her causal theory on $\text{Obs}=x$ and executes $\mathtt{do}(\text{Act}=a)$. When an A-FDT agent observes $x$, she **changes which node she intervenes upon**. Instead of conditioning on $\text{Obs}=x$ inside the expectation, the input $x$ is bound into the algorithm's label: she intervenes on $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$. This allows the counterfactual evaluation $\mathtt{do}(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a')$ to explore worlds where the historical observation $\text{Obs}$ *could have been different*, immunizing A-FDT to dynamic inconsistency and blackmail.

---

## 3. Subjunctive Dependence and the Semantics of Counterpossibles

The philosophical foundation of A-FDT is the concept of **subjunctive dependence**. Yudkowsky and Soares claim: *Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*

```
      [ Mathematical Truth / Algorithm Type ]
             mathtt{fdt}(P, G, x)
                /            \
               /              \
     Subjunctive               Subjunctive
     Dependence                Dependence
             v                  v
     [ Predictor's ]       [ Agent's Own ]
     [ Simulation  ]       [ Execution   ]
             |                  |
       Causal Path         Causal Path
             v                  v
       [ Box B Setup ]      [ Physical Act ]
             \                  /
              v                v
                 [ Outcome / V ]
```

### 3.1 Subjunctive Dependence vs. Causation and Correlation
Two physical systems exhibit subjunctive dependence if their respective behaviors are mediated by their shared instantiation of a common abstract mathematical function. 

* **Causation without Subjunctive Divergence:** If a scribe in Paris transcribes the output of a mechanical calculator, the scribe’s writing is both causally and subjunctively dependent on the calculator's state. If the calculator had output a different number, the scribe would have written a different number.
* **Correlation without Subjunctive Dependence:** If two calculators are painted green by historical coincidence, intervening on the color of one does not alter the color of the other. The correlation is purely statistical.
* **Subjunctive Dependence without Physical Causation:** Two calculators executing the arithmetic addition $6288 + 1048$ in isolated laboratories on opposite sides of the Earth output $7336$. There is no physical signal traveling between them. Yet, their outputs subjunctively depend on the mathematical identity $6288 + 1048 = 7336$. 

### 3.2 The Counterpossible Problem
Mathematically, if an algorithm $\mathtt{fdt}$ is deterministic, then for fixed inputs $(P, G, x)$, its evaluation $\mathtt{fdt}(P, G, x) = a^*$ is a necessary mathematical fact. Evaluating an alternative action $a \neq a^*$ requires an agent to entertain an impossible antecedent: *What would happen if the function $\mathtt{fdt}$, evaluated at $(P, G, x)$, returned $a$, even though it logically returns $a^*$?*

In philosophical logic, conditionals with impossible antecedents are termed **counterpossibles** (Cohen 1990; Bjerring 2013). Classical possible-world semantics renders all counterpossibles vacuously true. A-FDT skirts this collapse by avoiding an unconstrained metaphysical counterpossible operator ($\mathtt{true}(\phi)$) and adopting Pearl's graph-surgery formalism ($\mathtt{do}$). 

In Pearl's structural equation framework, a causal variable is an endogenous node whose equation is replaced with a constant value under intervention, severing its parent edges. A-FDT treats the node $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ as an endogenous node in a *subjunctive DAG* $G$. Graph surgery on this node breaks its connection to the abstract axiomatic derivation of the algorithm's value, holding all other axiomatic and empirical structures fixed, and calculates expected utility through standard ancestral graph propagation.

---

## 4. Analysis Across Classical Dilemmas

To make the mechanics of Equation (1) precise, we analyze the behavior of an A-FDT agent (Fiona) alongside an EDT agent (Eve) and a CDT agent (Carl) across four canonical benchmark problems.

### 4.1 Newcomb's Problem
The game parameters are: Box $A$ contains $\$1,000$ (transparent); Box $B$ contains $\$1,000,000$ or $\$0$ (opaque). The predictor has an accuracy rate of $p = 0.99$.

* **Carl (CDT):** Considers graph $\mathcal{G}^C$ where the intervention is on the physical act node $\text{Act} \in \{\text{onebox}, \text{twobox}\}$. Box $B$ was filled yesterday; thus, there is no directed path from $\text{Act}$ to $\text{Box B}$. For any prior belief $P(\text{Box B} = \text{full}) = \pi$:
  $$\mathbb{E}(V \mid \mathtt{do}(\text{Act}=\text{twobox})) = \pi(\$1,001,000) + (1-\pi)(\$1,000) = \pi(\$1,000,000) + \$1,000,$$
  $$\mathbb{E}(V \mid \mathtt{do}(\text{Act}=\text{onebox})) = \pi(\$1,000,000).$$
  Two-boxing strictly dominates by $\$1,000$. Carl takes both boxes and typically walks away with $\$1,000$.

* **Fiona (A-FDT):** Uses graph $\mathcal{G}^F$ where $\mathtt{fdt}(\underline{P}, \underline{G})$ is the parent of *both* $\text{Act}$ and $\text{Prediction}$. The predictor formulated her forecast by simulating $\mathtt{fdt}(\underline{P}, \underline{G})$. Under intervention on this node:
  $$\mathbb{E}\left(V \;\middle|\; \mathtt{do}\big(\mathtt{fdt}(\dots)=\text{onebox}\big)\right) = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000,$$
  $$\mathbb{E}\left(V \;\middle|\; \mathtt{do}\big(\mathtt{fdt}(\dots)=\text{twobox}\big)\right) = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$
  Equation (1) yields $\text{A-FDT}(P, G) = \text{onebox}$. Fiona one-boxes, being correctly anticipated as a one-boxer, and claims $\$1,000,000$.

### 4.2 The Smoking Lesion Problem
Smoking confers a utility increment of $\$1,000$. A genetic lesion causes both a desire to smoke and lung cancer (which costs $\$1,000,000$) 99% of the time, but smoking itself has no causal link to cancer.

* **Eve (EDT):** Calculates conditional expectations:
  $$\mathbb{E}(V \mid \text{Act}=\text{smoke}) \approx 0.01(\$1,000,000) + \$1,000 = \$11,000,$$
  $$\mathbb{E}(V \mid \text{Act}=\text{refrain}) \approx 0.99(\$1,000,000) = \$990,000.$$
  Eve irrationally starves herself of nicotine to avoid learning bad news about her genetics.

* **Fiona (A-FDT):** Analyzes the subjunctive dependencies. Does the biological occurrence of the lesion subjunctively depend on the mathematical output of $\mathtt{fdt}(\dots)$? No: the arterial lesion does not simulate Fiona's decision procedure to determine whether it should mutate. The DAG $\mathcal{G}^F$ contains no directed path from $\mathtt{fdt}(\underline{P_S}, \underline{G})$ to $\text{Lesion}$. Thus:
  $$P\left(\text{Lesion} \;\middle|\; \mathtt{do}\big(\mathtt{fdt}(\dots)=\text{smoke}\big)\right) = P\left(\text{Lesion} \;\middle|\; \mathtt{do}\big(\mathtt{fdt}(\dots)=\text{refrain}\big)\right) = P(\text{Lesion}).$$
  Intervening on her decision function changes whether her body lights the cigarette, but leaves the probability of having the cancer-causing lesion unaltered. Fiona computes that smoking yields an unconditional expected bonus of $\$1,000$, and smokes.

### 4.3 The Transparent Newcomb Problem
Both boxes are transparent. Box $A$ visibly holds $\$1,000$. The predictor placed $\$1,000,000$ in Box $B$ iff she predicted the agent would leave Box $A$ behind *upon directly seeing that both boxes are full*. The agent observes $x = \text{full}$.

* **Carl (CDT) & Eve (EDT):** Both two-box. For Carl, the money is already physically visible; taking both boxes causally yields $\$1,001,000$ versus $\$1,000,000$. For Eve, conditional on observing $x = \text{full}$, the hypothesis that Box $B$ is full has already attained probability 1; conditioning on two-boxing provides no further bad news about Box $B$'s contents, so she takes the extra $\$1,000$. Both agents are predicted to two-box upon seeing two full boxes, so the predictor leaves Box $B$ empty.

* **Fiona (A-FDT):** Equation (1) specifies that Fiona's observation $x = \text{full}$ changes her point of intervention to the node $\mathtt{fdt}(\underline{P}, \underline{G}, \text{full})$. In her graph $\mathcal{G}^F$, the predictor's past prediction depended on what $\mathtt{fdt}(\underline{P}, \underline{G}, \text{full})$ returns!
  $$\mathbb{E}\left(V \;\middle|\; \mathtt{do}\big(\mathtt{fdt}(\dots, \text{full})=\text{onebox}\big)\right) = 0.99(\$1,000,000) + 0.01 q(\$1,000),$$
  $$\mathbb{E}\left(V \;\middle|\; \mathtt{do}\big(\mathtt{fdt}(\dots, \text{full})=\text{twobox}\big)\right) = 0.01(\$1,001,000) + 0.99 q(\$1,000),$$
  where $q$ is the probability of taking Box $A$ if the box were seen empty. 
  
  Fiona one-boxes despite directly seeing that Box $B$ is full. Her counterfactual reasoning holds: "If the algorithm that runs when seeing a full box outputs $\text{twobox}$, the predictor would have anticipated that and the box would not be full right now." Fiona consistently encounters two full boxes and takes the $\$1,000,000$.

### 4.4 Parfit's Hitchhiker
Stranded in a desert and facing death (value: $-\$1,000,000$), an agent meets a driver who can transport her to the city, but demands she pay $\$1,000$ from an ATM upon arrival. The driver accurately detects lies with 99% accuracy; post-arrival enforcement is impossible. 

Upon reaching the city ($x = \text{city}$), CDT and EDT agents refuse to pay. Safe in the city, paying is a pure causal loss of $\$1,000$, and conditional on being in the city, nonpayment carries no bad news regarding desert survival. Because both types of agents predictably defect once safe, the driver leaves them to die.

An A-FDT agent evaluates $\mathtt{do}(\mathtt{fdt}(\underline{P}, \underline{G}, \text{city}) = \text{pay})$. In her subjunctive model, the driver's past decision to rescue her was an evaluation of what $\mathtt{fdt}(\underline{P}, \underline{G}, \text{city})$ would return. Intervening to set that node to $\text{refuse}$ propagates counterfactually into the past, causing the driver's lie detector to register a lie and leave her in the desert. She gladly pays the $\$1,000$, and survives.

---

## 5. Comparative Pathologies: Diagnosing the Competition

A-FDT reveals the underlying structural errors that cause EDT and CDT to systematically bleed expected utility:

```
+---------------+-----------------------------------+-----------------------------------+
| Theory        | Structural Flaw in Counterfactual | Consequence in Predictive Games   |
+---------------+-----------------------------------+-----------------------------------+
| EDT           | Preserves non-subjunctive         | "Manages the news"; vulnerable to |
|               | statistical correlations          | blackmail (XOR Blackmail)         |
+---------------+-----------------------------------+-----------------------------------+
| CDT           | Slices away non-causal            | Delusional independence; loops;   |
|               | subjunctive dependencies          | passes up real survival bets      |
+---------------+-----------------------------------+-----------------------------------+
| A-FDT         | Intervenes on algorithm type,     | Maximizes real-world payouts;     |
|               | preserving subjunctive graphs     | reflectively stable               |
+---------------+-----------------------------------+-----------------------------------+
```

### 5.1 The Pathology of EDT: Managing the News
EDT treats conditionalization as counterfactual reasoning. Consequently, it respects correlations that have no basis in mathematical or physical dependence.

This vulnerability is exploited in **The XOR Blackmail**. A reliable predictor sends an agent a letter if and only if exactly one of the following holds: (i) the agent's house has no termites and she will pay $\$1,000$; or (ii) the house has termites (damages: $\$1,000,000$) and she will refuse to pay. An EDT agent who opens the letter reasons: "If I pay, my conditional probability of termites collapses to 0; if I refuse, it jumps to 1. Paying is wonderful news!" Eve pays the blackmailer. 

Carl (CDT) and Fiona (A-FDT) both refuse to pay. But their reasons differ fundamentally: Carl ignores the predictor's reliability, whereas Fiona recognizes that the status of the termite infestation is a physical fact independent of her decision algorithm, meaning her algorithm's output only controls whether the letter is sent.

### 5.2 The Pathology of CDT: Impossible Interventions and Instability
CDT fails in the opposite direction: by restricting interventions strictly to the physical token $\text{Act}$, it severs the correlation between the agent's action and environmental nodes that compute identical or predictive processes. 

In **Death in Damascus**, Death awaits the agent in whichever city (Damascus or Aleppo) she chooses to stay in tomorrow, based on Death's past prediction. Fleeing to Aleppo costs $\$1,000$. A CDT agent exhibits cyclical preferences: if she plans to stay in Damascus, Death is predicted to be in Damascus, making Aleppo look better. But once she resolves to flee to Aleppo, her belief updates, making Damascus look better. 

Under Arntzenius's (2008) and Joyce's (2012) ratification protocols, Carl adopts a mixed deliberative state where he is indifferent, paying $\$1,000$ to flee roughly 50% of the time, and dies with 100% certainty. Astonishingly, if offered a *truly random coin* for $\$1$ that would randomize his location and give him a real 50% chance of survival, CDT Carl **refuses to pay the dollar**. Why? Because CDT's counterfactuals evaluate the coin against an internal model that falsely asserts he already has at least a 50% chance of dodging Death through his deterministic deliberation.

An A-FDT agent avoids this instability entirely. Fiona recognizes that Death's appointment book is an accurate reflection of $\mathtt{fdt}(\dots)$. She computes that fleeing to Aleppo guarantees meeting Death at a cost of $\$1,000$, whereas remaining in Damascus guarantees meeting Death at a cost of $\$0$. She calmly stays in Damascus, avoiding wasted expenditure. Furthermore, if offered the $\$1$ objective chance coin, she eagerly buys it, recognizing that decoupling her choice from Death's prediction raises her survival probability from 0% to 50%.

---

## 6. A Step-by-Step Guide to Applying A-FDT to Unfamiliar Cases

To enable a practitioner or researcher to apply A-FDT to novel, complex decision settings, we outline a four-step algorithmic schema implied by Equation (1), distinguishing explicit textual requirements from necessary operational assumptions.

### Operational Recipe

```
[ Step 1: Input Encoding ]
  Specify (P, G, x). Quote the parameters: (P, G, x).
       |
       v
[ Step 2: Subjunctive Dependency Graph Assembly ]
  Construct DAG G over empirical and logical nodes:
  - Add endogenous node mathtt{fdt}(P, G, x).
  - Trace edges from mathtt{fdt}(P, G, x) to physical Act.
  - Trace edges to all systems simulating/predicting mathtt{fdt}(P, G, x).
  - Isolate variables that do not track the function's evaluation.
       |
       v
[ Step 3: Graph Surgery and Counterfactual Propagation ]
  For each candidate action a in A:
  - Apply Pearl's operator: do(mathtt{fdt}(P, G, x) = a).
  - Sever incoming edges to mathtt{fdt}(P, G, x).
  - Propagate downstream evaluations across G to evaluate P(Outcome | do(...)).
       |
       v
[ Step 4: Utility Maximization ]
  Compute E(V | do(mathtt{fdt}(P, G, x) = a)) for all a in A.
  Return the argmax action.
```

### Unfamiliar Application: The Algorithmic Scribe Dilemma
To illustrate this procedure, consider an unfamiliar case:

> **The Dilemma of the Algorithmic Scribe:** An artificial agent faces an opportunity to execute a resource-intensive optimization routine $\alpha$ that yields $\$500$ in local profit, or default to a trivial routine $\beta$ yielding $\$0$. 
> 
> An external supercomputing "Scribe," operating thousands of miles away, has previously analyzed the source code of the agent's decision architecture. If the Scribe proved that the agent's architecture would choose $\alpha$ on this problem, the Scribe allocated $\$10,000$ to an escrow account dedicated to public infrastructure the agent values. If the Scribe proved that the agent would choose $\beta$, the Scribe allocated nothing. 
> 
> However, there is a known flaw in the Scribe's computing hardware: with probability $\epsilon = 0.05$, a memory corruption error occurs, causing the Scribe to invert its output regardless of the mathematical proof. The agent receives an observation $x = \text{flag}$, which indicates that a diagnostic pulse was received from the Scribe, but this pulse carries no information about whether an inversion error occurred.

How does A-FDT resolve this case?

1. **Step 1:** The agent identifies her model components: prior distribution $P$, observation history $x = \text{flag}$, and candidate actions $\mathcal{A} = \{\alpha, \beta\}$.
2. **Step 2:** Construct the graph $G$. The node $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{\text{flag}})$ is identified. Directed edges are established:
   $$\mathtt{fdt}(\underline{P}, \underline{G}, \underline{\text{flag}}) \longrightarrow \text{Physical Act} \in \{\alpha, \beta\},$$
   $$\mathtt{fdt}(\underline{P}, \underline{G}, \underline{\text{flag}}) \longrightarrow \text{Scribe Proof} \in \{\text{Proves } \alpha, \text{Proves } \beta\}.$$
   A noise node $\text{Hardware Error} \in \{\text{nominal}, \text{inverted}\}$ with $P(\text{inverted}) = 0.05$ feeds into $\text{Escrow Allocation}$, alongside $\text{Scribe Proof}$.
3. **Step 3:** Perform the graph surgery $\mathtt{do}(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{\text{flag}}) = a)$.
   * Under $\mathtt{do}(\mathtt{fdt} = \alpha)$:
     $\text{Physical Act}$ becomes $\alpha$, providing $\$500$.
     $\text{Scribe Proof}$ becomes $\text{Proves } \alpha$. The probability of the escrow allocation receiving $\$10,000$ is $P(\text{nominal}) = 0.95$.
     Expected Utility:
     $$\mathbb{E}(V \mid \mathtt{do}(\mathtt{fdt}=\alpha)) = \$500 + 0.95(\$10,000) + 0.05(\$0) = \$500 + \$9,500 = \$10,000.$$
   * Under $\mathtt{do}(\mathtt{fdt} = \beta)$:
     $\text{Physical Act}$ becomes $\beta$, providing $\$0$.
     $\text{Scribe Proof}$ becomes $\text{Proves } \beta$. The probability of the escrow allocation receiving $\$10,000$ via an error is $P(\text{inverted}) = 0.05$.
     Expected Utility:
     $$\mathbb{E}(V \mid \mathtt{do}(\mathtt{fdt}=\beta)) = \$0 + 0.05(\$10,000) + 0.95(\$0) = \$500.$$
4. **Step 4:** Compare the expected utilities:
   $$\$10,000 > \$500 \implies \text{A-FDT}(P, G, \text{flag}) = \alpha.$$

The A-FDT agent decisively executes $\alpha$. A CDT agent in the same position would observe that the Scribe has already executed its calculation and sent its diagnostic pulse. Because the escrow allocation cannot be causally affected by the physical execution of the routine at this point, the CDT agent would only see the $\$500$ marginal gain of $\alpha$ versus the cost of execution, behaving inappropriately if execution carried even a minor negative externality.

---

## 7. Open Foundational Uncertainties: Source Claims vs. Methodological Proposals

While A-FDT provides an appealing and unifying heuristic across a wide battery of dilemmas, its mathematical machinery leaves critical theoretical questions open. It is vital to separate what is proven in the foundational paper from what remains speculative.

### 7.1 What the Source Establishes
1. **Unification of Classic Successes:** Equation (1) provides an exact mathematical formula that one-boxes in Newcomb's Problem, smokes in the Smoking Lesion Problem, pays in Parfit's Hitchhiker, and one-boxes in the Transparent Newcomb Problem without invoking ad-hoc probability patches or dynamic ratification.
2. **Reflective Stability in Fair Dilemmas:** In "fair dilemmas"—where outcomes depend on predictions of the agent's actions rather than intrinsic penalties levied against her internal algorithms—A-FDT agents exhibit no incentive to self-modify into CDT or EDT agents.
3. **Equivalence of Precommitment and Action:** A-FDT agents naturally execute the exact actions that a CDT agent would have paid to precommit to ahead of time, effectively securing the benefits of precommitments dynamically on the fly.

### 7.2 What the Source Leaves Open
The source explicitly acknowledges several core theoretical gaps:
* **The Origin of the Subjunctive Graph $G$:** While Pearl (2000) formalizes causal discovery algorithms (e.g., the IC and PC algorithms) to infer causal DAGs from observation and active intervention, the paper explicitly notes that *no formal analogue exists for learning subjunctive dependency structures from observation and logical deliberation*.
* **A Pure Evidential $\mathtt{true}$ Operator:** The paper notes that relying on Pearl's $\mathtt{do}$-operator on a logical graph is an operational stopgap. The ideal theory would utilize an evidential operator:
  $$\text{FDT}^*(P, x) = \argmax_{a \in \mathcal{A}} \mathbb{E}\left(V \;\middle|\; \mathtt{true}\Big(\mathtt{fdt}(\underline{P}, \underline{x}) = a\Big)\right),$$
  which conditions directly on mathematical counterpossibles. But defining coherent probabilities conditioned on false logical statements remains an unsolved problem in logical induction and bounded arithmetic (Demski 2012; Hutter et al. 2013).

### 7.3 Methodological Proposal: Resolving Graph Ambiguity
When an agent encounters a predictor whose modeling fidelity is imperfect, how should the edge weight and graph structure in $G$ be determined? 

We propose an operational protocol: **The Algorithmic Mutual Information Criterion**. 
Let the predictor's simulation be an algorithm $\mathcal{M}$. We measure the Kolmogorov complexity of Fiona's algorithm $K(\mathtt{fdt})$ and the relative complexity $K(\mathcal{M} \mid \mathtt{fdt})$. If the predictive system works by reverse-engineering, decompiling, or simulating the agent's code, the mutual algorithmic information $I(\mathcal{M} : \mathtt{fdt})$ is large. 

In our proposed schema, a directed subjunctive edge from $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ to $\text{Prediction}$ exists in $G$ if and only if the predictor's internal state computationally instantiates a homomorphism of $\mathtt{fdt}$. The conditional probability table on that edge is parameterized by the fidelity of the simulation (e.g., error rate $1-p$). If the predictor merely exploits a common biological or environmental marker (as in the Smoking Lesion Problem), $I(\mathcal{M} : \mathtt{fdt})$ is purely physical/statistical, and no subjunctive edge is drawn. This criterion provides an objective baseline to construct $G$ in multi-agent and predictive settings, bridging one of the primary gaps left in the literature.

---

## 8. Conclusion

Action Functional Decision Theory (A-FDT) fundamentally reinterprets what it means to make a choice. Where Causal Decision Theory isolates the agent's physical body, cutting away the rich logical web that connects identical reasoning processes across time and space, Evidential Decision Theory blurs the distinction between genuine mathematical dependencies and passive correlations.

By formalizing counterfactuals as interventions on the *logical outputs of decision procedures* rather than interventions on physical acts, Equation (4) of Yudkowsky and Soares resolves decades of paradoxes with striking mathematical simplicity. The A-FDT agent does not need to resort to external precommitment mechanisms, does not fear information, and does not fall victim to blackmail or deliberative instability. While formalizing the automated discovery of subjunctive graphs and the mathematics of counterpossible conditioning remain active frontiers, A-FDT provides a mathematically sound, philosophically robust framework for understanding rationality in an interconnected, computational world.

---

## References

* Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
* Arntzenius, F. (2008). No Regrets, or: Edith Piaf Revamps Decision Theory. *Erkenntnis*, 68(2), 277–297.
* Bjerring, J. C. (2013). On Counterpossibles. *Philosophical Studies*, 168(2), 1–27.
* Cohen, D. (1990). On What Cannot Be. In *Truth or Consequences*, pp. 123–132. Kluwer Academic Publishers.
* Demski, A. (2012). Logical Prior Probability. In *Artificial General Intelligence*, Lecture Notes in Computer Science, 7716, 50–59. Springer.
* Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Eells, E. (1984). Metatickles and the Dynamics of Deliberation. *Theory and Decision*, 17(1), 71–95.
* Gibbard, A., & Harper, W. L. (1978). Counterfactuals and Two Kinds of Expected Utility. In C. A. Hooker, J. J. Leach, & E. F. McClennen (Eds.), *Foundations and Applications of Decision Theory* (pp. 125–162). D. Reidel.
* Hutter, M., Lloyd, J. W., Ng, K. S., & Uther, W. T. B. (2013). Probabilities on Sentences in an Expressive Logic. *Journal of Applied Logic*, 11(4), 386–420.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Joyce, J. M. (2012). Regret and Instability in Causal Decision Theory. *Synthese*, 187(1), 123–145.
* Lewis, D. (1979). Prisoners' Dilemma is a Newcomb Problem. *Philosophy & Public Affairs*, 8(3), 235–240.
* Lewis, D. (1981). Causal Decision Theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
* Nozick, R. (1969). Newcomb's Problem and Two Principles of Choice. In N. Rescher (Ed.), *Essays in Honor of Carl G. Hempel* (pp. 114–146). D. Reidel.
* Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
* Pearl, J. (1996). Causation, Action, and Counterfactuals. In *6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-'96)*, pp. 51–73. Morgan Kaufmann.
* Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Skyrms, B. (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Soares, N., & Fallenstein, B. (2015). Toward Idealized Decision Theory. *arXiv preprint arXiv:1507.01986*.
* Yudkowsky, E., & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. *arXiv preprint arXiv:1710.05060*.