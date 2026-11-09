# Action Functional Decision Theory: Subjunctive Dependencies and Algorithmic Counterfactuals

Standard normative decision theory has long been divided into two competing paradigms: **evidential decision theory (EDT)** and **causal decision theory (CDT)**. EDT selects the action that constitutes the best news about the state of the world, formalizing deliberation through Bayesian conditionalization. CDT selects the action that causally brings about the best outcome, formalizing deliberation through physical interventions that hold the past fixed. 

Both paradigms exhibit well-documented pathologies:
* EDT falls prey to the *smoking lesion problem* and extortionate setups such as the *XOR blackmail*, where an agent irrationally acts to "manage the news" of bad latent states that are already fixed.
* CDT fails catastrophically in Newcomblike dilemmas, the *psychological twin prisoner's dilemma*, and *Parfit's hitchhiker*. In these environments, an external process predicts the agent's behavior or shares their underlying code, yet CDT treats the prediction as an independent background fact immune to the agent's current choice.

To resolve these tensions, Yudkowsky and Soares introduce **functional decision theory (FDT)**. In this essay, we focus on its formal action-selection formulation—which we term **action functional decision theory (A-FDT)**. A-FDT evaluates decisions not by intervening on a physical act token in spacetime, but by performing a hypothetical surgery on the *output of the agent's mathematical decision function itself*.

Below, we develop the formal architecture of A-FDT, trace its treatment of counterfactuals via Pearlian interventions on logical nodes, analyze how it decides core dilemmas, and inspect the foundational questions that remain open.

---

## 1. Decision Hypotheticals: From Tokens to Types

All three theories—EDT, CDT, and A-FDT—can be framed within Joyce’s general representation theorem for expected utility maximization (Joyce 1999). An agent with observation history $x \in \mathcal{X}$ chooses an action $a$ from a finite set $\mathcal{A}$ to maximize:

$$\mathcal{EU}(a) \coloneqq \sum_{j} P(a \then o_j ;\, x) \, \mathcal{U}(o_j)$$

where outcomes $o_j \in \mathcal{O}$ carry real-valued utilities $\mathcal{U}(o_j)$, and $a \then o$ denotes the decision hypothetical: *"what would obtain if the agent were to select $a$."* The fundamental dispute among decision theories concerns the semantics of this conditional connective "$\then$":

### Evidential Decision Theory (EDT)
EDT sets $P(a \then o;\, x) \coloneqq P(o \mid x, a)$. Letting $\mathbb{V} \coloneqq \mathcal{U}(\text{Outcome})$, EDT computes:
$$\text{EDT}(P, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\mathbb{V} \mid \text{Obs}=x, \, \text{Act}=a\right) \tag{1}$$
EDT conditions directly on its own physical behavior. When an action correlates with an exogenous variable, EDT treats the action as diagnostic of that variable, even when no causal or computational mechanism links them.

### Causal Decision Theory (CDT)
CDT augments the probability distribution $P$ with a directed acyclic graph (DAG) $G$, encoding physical causal pathways (Pearl 2000). The hypothetical is evaluated by Pearl's $\mathtt{do}$-operator, severing all incoming edges to the physical action node $\text{Act}$:
$$\text{CDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\mathbb{V} \;\middle|\; \mathtt{do}(\text{Act}=a), \, \text{Obs}=x\right) \tag{2}$$
In CDT, interventions act on the physical *token* ("my body performs action $a$ at time $t$"). Any event in the past or in causally disconnected regions of spacetime is held invariant. Consequently, CDT cannot internalize that an external predictor built a model of its reasoning: the prediction happened in the past, so $\mathtt{do}(\text{Act}=a)$ severs any link between the prediction and the choice.

### Action Functional Decision Theory (A-FDT)
A-FDT rejects the assumption that the fundamental locus of choice is a spatiotemporal act token. Rational deliberation is an execution of an abstract, invariant decision procedure: a mapping from an epistemic state and observation history to an action. An agent does not ask, *"What if my physical hands moved differently while holding my reasoning fixed?"* (which posits a physical miracle or a malfunctioning brain). Instead, the agent asks:
$$\text{\textit{What if this very mathematical decision function yielded a different logical output?}}$$

In Peirce’s terminology (Peirce 1934), CDT intervenes on the *token*, whereas A-FDT intervenes on the *type*. If the agent's decision function is instantiated in multiple places—such as inside an opponent's simulation, a twin's brain, or a past predictor's notebook—intervening on the logical output alters every manifestation that **subjunctively depends** on that function.

---

## 2. The Formal Specification of A-FDT

Section 5 of the source document introduces Equation (4) as the primary formal presentation of functional decision-making over actions. We designate this formulation **A-FDT**:

$$\text{A-FDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\mathbb{V} \;\middle|\; \mathtt{do}\left(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right) \tag{3}$$

Equation (3) encapsulates the mathematical mechanics of A-FDT. To apply it to unfamiliar problems, an analyst or automated agent must understand each of its components:

1. **Self-Referential Quining ($\underline{P}, \underline{G}, \underline{x}$):** The underlines denote literal syntactic representations (dequoting/Gödel codes). The agent’s world model $(P, G)$ contains random variables representing mathematical and algorithmic facts. Among these is a node $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$, which denotes the evaluation of the algorithm $\text{A-FDT}$ on the agent's current model inputs. By Kleene’s Second Recursion Theorem (Kleene 1938), a computer program can inspect its own code without infinite regress. The node represents the output of the function, but computing the argmax does not require knowing that output beforehand.
2. **The Extended Graph $G$:** Unlike standard causal graphs whose arrows strictly signify physical causal mechanisms propagating forward in time, the graph $G$ in A-FDT is an extended dependence structure. Directed arrows out of a logical node $\mathtt{fdt}(\cdot)$ represent **subjunctive dependencies**—informational, logical, simulation-based, or causal links.
3. **The Logical $\mathtt{do}$-Surgery:** The Pearlian operator $\mathtt{do}(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)$ mutates the joint distribution $P$ by:
   * Setting the value of the random variable $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ to $a$.
   * Severing all incoming arrows into $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ (rendering it independent of the agent's prior history or internal parameters).
   * Propagating this substitution forward through all directed descendants of $\mathtt{fdt}(\cdot)$ in $G$.
4. **The Treatment of Observations (The "Updateless" Shift):** Observe that Equation (3) conditions on $\mathtt{do}(\mathtt{fdt}(\dots)=a)$, but **not** on $\text{Obs}=x$! 
   * In CDT (Equation 2), an observation $x$ updates the background distribution via standard Bayesian conditioning: $\mathbb{E}(\dots \mid \mathtt{do}(\text{Act}=a), \text{Obs}=x)$.
   * In A-FDT (Equation 3), the observation $x$ enters as an argument *indexing the node to be intervened upon*. The hypothetical world being evaluated is allowed to retrodict or alter whether the observation $x$ would have been made in the first place, if the environment contains processes whose behavior depended on the prediction of $\text{A-FDT}(\dots, x)$.

---

## 3. Resolving the Dilemma Landscape

To make A-FDT operational, we trace its execution across canonical decision-theoretic problems, tracking how it escapes the traps of CDT and EDT.

### 3.1. Newcomb's Problem
*Setup:* Box A contains \$1,000 (transparent). Box B contains either \$1,000,000 or \$0 (opaque). A predictor, accurate 99% of the time, placed \$1,000,000 in Box B iff she predicted the agent would take only Box B. The prediction is already made.

```
       [ fdt(P, G) ]  (Intervention Point in A-FDT)
         /        \
        v          v
     [ Act ]    [ Prediction ] <-- [ Accurate (0.99) ]
        \          /
         v        v
        [ Box B / Outcome ]
                 |
                 v
                [ V ]
```

* **CDT Agent (Carl):** Intervenes on $\mathtt{do}(\text{Act}=a)$. Because $\text{Box B}$ is causally upstream or independent of $\text{Act}$ under a purely temporal causal graph, $P(\text{Box B}=\text{full} \mid \mathtt{do}(\text{Act}=\text{onebox})) = P(\text{Box B}=\text{full})$. Carl takes two boxes and walks away with \$1,000.
* **EDT Agent (Eve):** Conditions on $\text{Act}=\text{onebox}$. $P(\text{Box B}=\text{full} \mid \text{onebox}) = 0.99$. Eve takes one box and wins \$1,000,000, but does so by conflating evidence with control.
* **A-FDT Agent (Fiona):** Fiona consults graph $G^F$, where $\mathtt{fdt}(\underline{P}, \underline{G})$ is the common ancestor of both $\text{Act}$ and $\text{Prediction}$. She evaluates:
  $$\mathbb{E}\left(\mathbb{V} \;\middle|\; \mathtt{do}(\mathtt{fdt} = \text{onebox})\right) = 0.99(\$1{,}000{,}000) + 0.01(\$0) = \$990{,}000$$
  $$\mathbb{E}\left(\mathbb{V} \;\middle|\; \mathtt{do}(\mathtt{fdt} = \text{twobox})\right) = 0.01(\$1{,}001{,}000) + 0.99(\$1{,}000) = \$11{,}000$$
  A-FDT prescribes **one-boxing**. Fiona recognizes that the predictor's model subjunctively depends on her algorithm.

### 3.2. The Smoking Lesion Problem
*Setup:* A genetic lesion causes both a desire to smoke and lung cancer (fatal, utility loss \$1,000,000). Smoking provides an immediate sensory benefit of \$1,000. Smoking does not cause cancer; the correlation is driven entirely by the common cause.

Here, EDT notoriously fails: Eve refrains from smoking to deceive herself about her genetic status, sacrificing \$1,000 for zero actual health benefit.

In A-FDT, the agent constructs a graph where the lesion is a physical state of biology. The lesion fixes the agent's utility function ($\mathcal{U}_S$ for smoking-lovers, $\mathcal{U}_R$ for smoking-haters). However, does cancer *subjunctively depend* on the output of $\mathtt{fdt}(\dots)$? No. The cancer is a somatic pathology caused by the lesion, not by an algorithm simulation. 

As formalized in Section 6 of the source document:
$$P(\text{Lesion} \mid \mathtt{do}(\mathtt{fdt}_S = \text{smoke})) = P(\text{Lesion}) = p$$
The intervention on the decision function breaks the statistical correlation with the latent biological state because there is no computational or modeling link connecting $\mathtt{fdt}$ to the biological growth of cancer cells. The expected utility of smoking exceeds that of refraining by:
$$p \cdot \$1{,}000 > 0$$
A-FDT prescribes **smoking**. A-FDT thus breaks statistical correlations that lack subjunctive mechanisms, avoiding EDT’s fatal flaw.

### 3.3. Transparent Newcomb and Parfit's Hitchhiker
The decisive departure of A-FDT from both CDT and EDT occurs when the agent receives an observation that seems to make the past immutable.

In *Transparent Newcomb*, both boxes are transparent. Box B is seen to contain \$1,000,000. Box A contains \$1,000. The predictor filled Box B iff she predicted that the agent, *upon directly observing that Box B is full*, would leave Box A behind.

* **CDT:** The money is already in the box. Taking Box A yields an additional \$1,000. CDT takes both.
* **EDT:** Conditioned on $\text{Obs}=\text{full}$, the information is already revealed; news-management is moot. EDT takes both.
* **A-FDT:** Fiona has observed $x = \text{full}$. According to Equation (3), she intervenes on $\mathtt{do}(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{\text{full}}) = a)$. Notice that in $G^F$, the predictor's past prediction depended on the anticipated output of this exact branch: $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{\text{full}})$.

```
   [ fdt(P, G, full) ] (Intervened on!)      [ fdt(P, G, empty) ]
           \               \                     /
            \               v                   v
             \------> [ Prediction ] ------> [ Act ]
                           |
                           v
                        [ Obs ]
```

If Fiona sets this node to $\text{twobox}$, she considers a counterfactual world where the predictor anticipated this, classified her as a two-boxer upon seeing a full box, and therefore *never filled Box B in the first place*! In that hypothetical world, her observation would have been $\text{Obs}=\text{empty}$, and she would walk away with at most \$1,000.
$$\mathbb{E}(\mathbb{V} \mid \mathtt{do}(\mathtt{fdt}_{\text{full}} = \text{onebox})) = 0.99(\$1{,}000{,}000) + 0.01 q(\$1{,}000) \approx \$990{,}000$$
$$\mathbb{E}(\mathbb{V} \mid \mathtt{do}(\mathtt{fdt}_{\text{full}} = \text{twobox})) = 0.01(\$1{,}001{,}000) + 0.99 q(\$1{,}000) \approx \$11{,}000$$
A-FDT prescribes **one-boxing**, even when staring directly at the cash. Consequently, predictors fill the box for A-FDT agents, whereas CDT and EDT agents encounter empty boxes.

This behavior translates directly to *Parfit's Hitchhiker*. A driver rescues an agent from dying in the desert (worth \$1,000,000) iff she predicts the agent will pay \$1,000 upon reaching the safety of the city. Once in the city, CDT and EDT refuse to pay: the rescue has already happened. The driver anticipates their defection and leaves them to die. The A-FDT agent, reasoning in the city, considers the counterfactual: *"If $\mathtt{fdt}(\dots, \text{city})$ outputs $\text{refuse}$, the driver predicts this in the desert and leaves me to die."* A-FDT pays the driver, making the promise credible and securing the rescue.

---

## 4. The Taxonomy of Dependencies: When Does Subjunctive Dependence Hold?

To use A-FDT to resolve arbitrary, unfamiliar cases, one must formalize the demarcation between legitimate subjunctive dependencies and mere correlations. Why does Box B depend on $\mathtt{fdt}$, while the cancer lesion does not?

The source paper establishes three distinct categories of relational structures:

| Relation Type | Physical Causation Required? | Mechanism | Example | Respected by A-FDT? |
| :--- | :--- | :--- | :--- | :--- |
| **Purely Statistical Correlation** | No | Coincidental correlation or common physical cause without algorithm modeling | Two identically colored calculators; Smoking Lesion | **No** (Broken by $\mathtt{do}$) |
| **Physical Causal Dependence** | Yes | Energy/information transfer through physical spacetime | Hand moves, pushing a physical block | **Yes** (Standard causal arrows) |
| **Subjunctive / Logical Dependence** | No | Multiple physical systems running, simulating, or predicting the same formal function | Perfect Twin Prisoner's Dilemma; Newcomb Predictor | **Yes** (Preserved across all instances) |

### Algorithmic Twinhood and Simulations
Subjunctive dependence occurs when a physical system’s state is determined by the output of a computation that is logically constrained to match the agent’s decision algorithm. 
* If Agent 1 and Agent 2 run identical source code on identical inputs, their choices are mathematical copies: $\mathtt{fdt}_1(x) \equiv \mathtt{fdt}_2(x)$. Intervening on the mathematical function changes the output for both.
* If a predictor runs an internal simulation $\mathcal{S}$ of agent $A$, the state of $\mathcal{S}$ is an evaluation of $A$'s decision function. An intervention on $\mathtt{fdt}_A$ intervenes on the behavior of $\mathcal{S}$.

### The Dominance Principle Reconsidered
Causal decision theorists accuse A-FDT of violating the dominance principle in Newcomb's problem: holding the state of the world fixed (Box B is either empty or full), two-boxing strictly dominates one-boxing.

A-FDT replies that **every decision theory defines dominance relative to its own counterfactual hypotheticals**.
* **CDT Dominance:** Action $a$ dominates $b$ if, holding fixed everything outside the causal downstream of the *physical act*, $a$ yields higher utility.
* **A-FDT Dominance:** Action $a$ dominates $b$ if, holding fixed everything that does not *subjunctively depend* on the *decision function*, $a$ yields higher utility.

In Newcomb's problem, holding Box B fixed while varying the action requires positing a mathematical impossibility: that the function $\mathtt{fdt}(\underline{P}, \underline{G})$ evaluates to $\text{twobox}$ while a perfect evaluation of that exact same function by the predictor yielded $\text{onebox}$. A-FDT rejects this hypothetical as logically incoherent—analogous to asking what would happen if a calculator computed $2+2=5$ while holding constant that arithmetic is consistent.

---

## 5. Open Foundations: What the Source Establishes vs. What Remains Unsolved

While A-FDT provides an appealing set of prescriptions, its formalization in Equation (3) relies on several mathematical structures that are not fully closed in the source document. A rigorous evaluation requires clearly delineating established properties from open theoretical gaps.

```
       [ Well-Founded Base ]                          [ Open Foundational Problems ]
  +-------------------------------+             +-----------------------------------------+
  | Joyce's Representation Engine |             | Derivation of Extended Graph G          |
  | Pearl's Graphical do-Calculus | ----------> | (No logical analogue of d-separation)  |
  | Updateless Policy Invariance  |             | Semantics of Counterpossibles / True(.) |
  +-------------------------------+             +-----------------------------------------+
```

### 1. Where Does the Extended Graph $G$ Come From?
In CDT, Pearl’s causal discovery algorithms (Pearl 2000) show how causal graphs can be systematically inferred from observational data, conditional independence tests ($d$-separation), and physical randomized trials. 

**The Open Problem:** The source document explicitly concedes that *no formal methodology exists for deducing extended subjunctive graphs from observation and experiment*. The authors take $G$ as an exogenously provided primitive. 

**A Proposed Operational Construction:** To operationalize A-FDT without an oracle, we propose treating subjunctive dependence via *program analysis and Kolmogorov complexity*:
* An environmental variable $Y$ subjunctively depends on an agent's decision function $\mathtt{fdt}$ to the degree that any optimal compressive model of the environment computes an evaluation of the program code $\ulcorner \mathtt{fdt} \urcorner$ as an intermediate step to predicting $Y$. 
* If an environmental process contains a causal sub-graph isomorphic to the execution trace of the decision function (a simulation), an edge $\mathtt{fdt} \to Y$ is drawn. If $Y$'s correlation with the agent is purely mediated by a common historical node without programmatic emulation (as in the smoking lesion), no edge is drawn.

### 2. Counterpossible Conditionals and the $\mathtt{True}$ Operator
Equation (3) leverages Pearl's $\mathtt{do}$-operator on logical nodes as an engineering proxy for an ideal mathematical operator, $\mathtt{True}(\phi)$, which updates a probability distribution on a counterpossible sentence $\phi$ (e.g., conditioning on a false statement of arithmetic or logic). 

In standard probability theory, if $\mathtt{fdt}(P, G, x) = a_1$ is a deterministic theorem of mathematics, then the event $\mathtt{fdt}(P, G, x) = a_2$ has prior probability zero. Conditioning on it is undefined ($0/0$). 
Pearl's $\mathtt{do}$-operator evades this by graph surgery: it severs the deterministic incoming equations, treating the node as an unconstrained primitive. While computationally functional, this leaves deep semantic tensions: an agent is treating a fixed theorem of Peano arithmetic as though it were a free physical switch. Developing a consistent probability logic over non-omniscient mathematical sentences (logical uncertainty) remains an active research frontier (Gaifman 2004; Demski 2012).

### 3. Policy-Based vs. Action-Based Interventions
Footnote 7 and Footnote 16 of the source acknowledge that Yudkowsky and Soares prefer a formulation of FDT where agents intervene over **policies** (mappings $\pi: \mathcal{X} \to \mathcal{A}$) rather than actions. 

In our focus, **A-FDT**, the intervention is executed at the level of the specific action node $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$. The authors note that intervening on the action indexed by the observation history ($x$) achieves the updateless benefits of policy selection for all single-agent and predictive dilemmas evaluated in the text. However, in asymmetric multi-agent games with imperfect recall, intervening on an overarching policy $\pi$ can decouple an agent's commitments across different information sets more effectively than pointwise action interventions.

---

## 6. Algorithmic Recipe for Applying A-FDT

For a researcher analyzing an arbitrary decision dilemma under A-FDT, the procedure mandated by Equation (3) can be formalized into four sequential steps:

1. **Epistemic and Computational Graph Construction:**
   Construct a directed acyclic graph $G$ over random variables containing:
   * Observations $\text{Obs}$, physical actions $\text{Act}$, and outcomes/utilities $\mathbb{V}$.
   * Explicit logical nodes $\mathtt{fdt}(\underline{P}, \underline{G}, x')$ representing the evaluation of the decision algorithm for any reachable observation history $x'$.
   * Directed edges from $\mathtt{fdt}(\underline{P}, \underline{G}, x')$ to any physical process that runs an accurate model, simulation, or clone of this computation (e.g., predictors, twins, code verifiers).
   * Directed edges from $\mathtt{fdt}(\underline{P}, \underline{G}, x)$ to $\text{Act}$.
2. **Identification of the Intervention Node:**
   Given actual observation history $x$, identify the specific target node:
   $$\mathcal{N}^* \coloneqq \mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$$
3. **Graph Surgery and Counterfactual Propagation:**
   For each candidate action $a \in \mathcal{A}$:
   * Sever all incoming edges into $\mathcal{N}^*$.
   * Set $\mathcal{N}^* = a$.
   * Recompute the probabilities of all descendants of $\mathcal{N}^*$ in $G$ using structural equation propagation. Do **not** condition on $\text{Obs}=x$ after surgery; allow descendants of $\mathcal{N}^*$ (including past predictions) to adjust to $a$.
4. **Argmax Utility Selection:**
   Execute the physical action $a^*$ that maximizes expected utility under the surgically modified distribution:
   $$a^* = \argmax_{a \in \mathcal{A}} \mathbb{E}_{P \mid \mathtt{do}(\mathcal{N}^* = a)}[\mathbb{V}]$$

---

## 7. Conclusion

Action Functional Decision Theory (A-FDT) represents a fundamental shift in the ontology of rational choice. Where Evidential Decision Theory asks, *"What action would be the best news to observe?"*, and Causal Decision Theory asks, *"What physical movement of my body causally forces the best outcome?"*, A-FDT asks:

> *"Which output of this very mathematical decision function yields the best outcome, across all physical processes that subjunctively depend upon it?"*

By intervening on the mathematical *type* rather than the spatiotemporal *token*, A-FDT preserves the integrity of predictive relationships, simulations, and algorithmic symmetries without collapsing into the news-managing delusions of EDT. It one-boxes in Newcomb's problem, smokes in the smoking lesion problem, walks out of Parfit’s desert alive, and systematically resists extortion and blackmail. 

A-FDT reveals that an agent’s greatest asset in an interactive world is not physical force applied to the immediate environment, but the predictable, incorruptible character of the algorithm that selects its choices.

---

### References

* Ahmed, Arif. 2014. *Evidence, Decision and Causality*. Cambridge University Press.
* Arntzenius, Frank. 2008. "No Regrets, or: Edith Piaf Revamps Decision Theory." *Erkenntnis* 68 (2): 277–297.
* Demski, Abram. 2012. "Logical Prior Probability." In *Artificial General Intelligence (AGI 2012)*, LNCS 7716: 50–59. Springer.
* Gaifman, Haim. 2004. "Reasoning with Limited Resources and Assigning Probabilities to Arithmetical Statements." *Synthese* 140 (1–2): 97–119.
* Gibbard, Allan, and William L. Harper. 1978. "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, 125–162. Reidel.
* Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Kleene, Stephen Cole. 1938. "On Notation for Ordinal Numbers." *Journal of Symbolic Logic* 3 (4): 150–155.
* Lewis, David. 1979. "Prisoners' Dilemma is a Newcomb Problem." *Philosophy & Public Affairs* 8 (3): 235–240.
* Nozick, Robert. 1969. "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel*, 114–146. Reidel.
* Parfit, Derek. 1986. *Reasons and Persons*. Oxford University Press.
* Pearl, Judea. 2000. *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Peirce, Charles Sanders. 1934. *Collected Papers of Charles Sanders Peirce. Vol. V: Pragmatism and Pragmaticism*. Harvard University Press.
* Skyrms, Brian. 1980. *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Soares, Nate, and Benja Fallenstein. 2015. "Toward Idealized Decision Theory." *arXiv:1507.01986*.
* Yudkowsky, Eliezer, and Nate Soares. 2017. "Functional Decision Theory: A New Theory of Instrumental Rationality." *arXiv:1710.05060v2*.