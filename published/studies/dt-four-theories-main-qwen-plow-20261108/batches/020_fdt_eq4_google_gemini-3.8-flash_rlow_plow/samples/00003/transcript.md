# 020_fdt_eq4_google_gemini-3.8-flash_rlow_plow / 00003

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/2e654281-49fa-4c8a-a332-7c3188454824/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/2e654281-49fa-4c8a-a332-7c3188454824/call_0/response.raw) · finish: `stop`

### Visible response

````text
# Intervening on Logic: A Mathematical Exposition of Action Functional Decision Theory (A-FDT)

## 1. Introduction: The Dialectic of Rational Choice

Normative decision theory seeks a coherent mathematical rule that dictates what an ideal agent ought to do when confronted with an arbitrary choice. For decades, the foundational debate has been framed as a duel between two competing paradigms of expected utility maximization:

*   **Evidential Decision Theory (EDT):** Select the action that provides the best epistemic news regarding the world, evaluating actions via conditional probabilities $P(\text{outcome} \mid \text{action})$.
*   **Causal Decision Theory (CDT):** Select the action that causally brings about the best outcome, evaluating actions via physical interventions that sever incoming causal influences on the agent's physical behavior, formalized by Judea Pearl’s $\Do(\Act = a)$ operator.

Neither paradigm has achieved universal acceptance. Measuring success strictly by expected utility achieved over time, EDT excels in Newcomb-like problems but stumbles catastrophically in common-cause dilemmas like the Smoking Lesion Problem, where it irrationalizes by "managing the news." Conversely, CDT handles the Smoking Lesion cleanly but falls prey to Newcomb’s predictor, defects against identical psychological twins in the Prisoner's Dilemma, and is systematically exploited in Parfit’s Hitchhiker and blackmail scenarios.

A natural response—posited as early as Gibbard and Harper (1978)—is to suggest that no single rule can consistently one-box in Newcomb's problem and smoke in the Smoking Lesion. The paper under examination (*Functional Decision Theory: A New Theory of Instrumental Rationality*, Yudkowsky & Soares) rejects this impossibility claim. The authors argue that both CDT and EDT evaluate decisions against malformed hypothetical world-models: EDT respects too many correlations (confounding mere statistical correlation with decision-relevant influence), whereas CDT respects too few (treating an agent's physical choice as disconnected from environmental models and predictors that compute the exact same algorithm).

To resolve this conflict, the authors introduce a framework rooted in **subjunctive dependence**. While the overarching philosophical program is known broadly as Functional Decision Theory (FDT), its concrete mathematical operationalization in Section 5, Equation (4) of the reference paper operates by intervening directly on the mathematical function mapping the agent's current state to an action. In this essay, we refer strictly to this formal procedure as **Action Functional Decision Theory (A-FDT)**.

Our objective is to articulate the mathematical foundations of A-FDT, trace its evaluation of counterfactuals, explore its mechanics across classic decision dilemmas, and identify the unresolved technical gaps that stand between Equation (4) and a fully general normative theory.

---

## 2. Formal Foundations: The General Expected Utility Framework

Following Joyce (1999) and Gibbard & Harper (1978), all three theories can be framed as maximizing an expected utility objective. Let:
*   $\mathcal{A} = \{a_1, a_2, \ldots, a_K\}$ be a finite set of available actions.
*   $\mathcal{X}$ be a countable space of observation histories.
*   $\mathcal{O} = \{o_1, o_2, \ldots\}$ be a countable set of mutually exclusive, exhaustive outcomes.
*   $\Util: \mathcal{O} \to \mathbb{R}$ be a real-valued von Neumann–Morgenstern utility function, bounded such that all expectations are well-defined.
*   $\VV \coloneqq \Util(\Outcome)$ denote the utility random variable.

The general expected utility of executing action $a \in \mathcal{A}$ having observed history $x \in \mathcal{X}$ is governed by:

$$\mathcal{EU}(a) \coloneqq \sum_{j} P(a \then o_j ;\, x) \cdot \Util(o_j)$$

where "$\then$" denotes the connective for decision hypotheticals. As James Joyce observed, decision theories share the same axiomatic structure of valuation; they diverge solely on the *epistemic perspective* encoded by $P(a \then o_j ;\, x)$.

### 2.1 EDT and CDT as Operators

1.  **EDT** identifies the hypothetical with standard Bayesian conditionalization:
    $$P_{\text{EDT}}(a \then o_j ;\, x) \coloneqq P(o_j \mid x, a)$$
    $$\EDT(P, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}_P\left[\VV \mid \Obs = x, \Act = a\right] \tag{2}$$
    (defined over actions where $P(\Act=a \mid \Obs=x) > 0$).

2.  **CDT** constructs its hypothetical by augmenting $P$ with a directed acyclic causal graph $G$ over the system variables, substituting conditioning with Pearl’s physical intervention operator $\Do(\Act = a)$:
    $$P_{\text{CDT}}(a \then o_j ;\, x) \coloneqq P(o_j \mid \Do(\Act = a), x)$$
    $$\CDT(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}_P\left[\VV \cond \Do(\Act = a), \Obs = x\right] \tag{3}$$

Graphically, Pearl's $\Do(\Act = a)$ mutates the factorization of the joint distribution: it deletes all incoming directed edges to the physical node $\Act$ (severing upstream causes, such as genetic predispositions or historical brain states) while propagating the value $a$ downstream along all outward edges leading to $\Outcome$ and $\VV$.

---

## 3. Action Functional Decision Theory (A-FDT) Defined

### 3.1 The Core Thesis: Intervening on Function Types, Not Physical Tokens

The core insight of A-FDT is rooted in Charles Sanders Peirce's type-token distinction. CDT intervenes on the *token*: the concrete, spatiotemporal physical act $\Act$ performed by the agent's motor system at time $t$. A-FDT, by contrast, intervenes on the *type*: the abstract mathematical decision function that the agent runs to produce an output.

If an agent is computing a deterministic decision algorithm, that algorithm is a fixed mathematical object. If a predictor in the environment has constructed a simulation of the agent, or if another agent is an identical twin running the same decision algorithm, those processes do not causally depend on the agent's physical limbs. Rather, both physical systems *subjunctively depend* on the same underlying mathematical truth: the output of that decision function.

### 3.2 The Formal Definition: Equation (4)

To formalize this without relying on an unconstrained counterpossible logic engine, A-FDT extends Pearl’s graphical language to include *logical and computational variables*. 

Let $P$ be a probability distribution over states of the world and mathematical statements, and let $G$ be an extended dependency graph whose vertices include physical variables as well as logical nodes representing the evaluations of algorithms.

Let $\underline{P}$, $\underline{G}$, and $\underline{x}$ denote the syntactic encodings (or "dequoted" names) of the agent's probability distribution, graph, and observation history, respectively. A-FDT isolates a specific logical node in the graph:

$$\FDTvar(\underline{P}, \underline{G}, \underline{x})$$

which denotes the output of running the A-FDT decision algorithm on inputs $(P, G, x)$. Equation (4) defines the decision rule:

$$\Atext{-}\FDT(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}_P\left[\VV \cond \Do\left(\FDTvar(\underline{P}, \underline{G}, \underline{x}) = a\right)\right] \tag{4}$$

### 3.3 Two Crucial Divergences from CDT

Equation (4) exhibits two critical structural departures from CDT's Equation (3):

1.  **Shift of Intervention Target:** CDT intervenes on the physical act $\Act$. A-FDT intervenes on the logical computation node $\FDTvar(\underline{P}, \underline{G}, \underline{x})$. Consequently, in the post-intervention distribution $P\left(\cdot \mid \Do(\FDTvar = a)\right)$, any node in $G$ that lies downstream of the agent's *decision function* will update its value—including predictions made yesterday, simulations computed across the galaxy, or identical twins deciding simultaneously in distant rooms.
2.  **Observation Handling: Shifting Interventions vs. Conditioning:**
    In CDT, an observation $x$ acts as an evidence condition: the agent updates from $P(\cdot)$ to $P(\cdot \mid \Obs = x)$ and then executes $\Do(\Act = a)$. 
    In A-FDT, observation $x$ is not handled by conditioning inside the hypothetical; rather, **$x$ parameters which node in the graph is subjected to surgery**. 
    
    When an A-FDT agent observes $x$ instead of $x'$, she shifts her intervention from $\FDTvar(\underline{P}, \underline{G}, \underline{x}')$ to $\FDTvar(\underline{P}, \underline{G}, \underline{x})$. Notice that Equation (4) contains **no** conditional bar for $\Obs = x$ inside the expectation. The agent evaluates the consequences of setting the output of the function evaluated on input $x$ globally across the model, allowing counterfactuals to modulate the probability of having received observation $x$ in the first place.

### 3.4 Quining and Self-Reference

Equation (4) is formally self-referential: the function $\Atext{-}\FDT$ appears on both the left-hand side and inside the graphical query $\FDTvar(\underline{P}, \underline{G}, \underline{x})$ on the right-hand side. The source document notes that this recursion is mathematically sound via Kleene’s second recursion theorem (Kleene, 1938). 

An algorithm does not need to know its own final value in order to manipulate a representation of its code. By "quining" (passing its own source code as a data parameter), the program $\Atext{-}\FDT$ can construct queries regarding a graph $G$ containing a variable labeled with its own signature, and compute the expectation across hypothetical assignments $a \in \mathcal{A}$.

---

## 4. Subjunctive Dependence and Counterpossible Semantics

To understand why A-FDT succeeds where CDT and EDT fail, we must unpack the concept of **subjunctive dependence**.

### 4.1 Subjunctive vs. Causal and Statistical Dependence

Consider three distinct notions of association between two events $A$ and $B$:
*   **Statistical Correlation:** $P(B \mid A) \neq P(B)$. This can arise from direct causation, common causes, selection bias, or mathematical coincidence.
*   **Causal Dependence:** Intervening physically on $A$ via $\Do(A = a)$ alters the probability distribution of $B$. Physical causality respects relativistic light cones and temporal arrows (causes precede effects).
*   **Subjunctive Dependence:** Event $B$ depends on the output of a mathematical function $f(\cdot)$ that also determines $A$. If the function $f(\cdot)$ were to evaluate to $a'$, $B$ would take on a corresponding value $b'$.

Causal dependence is a strict subset of subjunctive dependence: physical mechanisms implement computations, so physical interventions propagate subjunctively. However, subjunctive dependence extends beyond physical light cones.

```
       [ Subjunctive Dependencies ]
      /                            \
[ Causal Dependencies ]      [ Logical / Algorithmic Dependencies ]
 (Physical actions,           (Predictor simulations, identical
  downstream effects)          twins, shared mathematical rules)
```

If two calculators on opposite ends of the universe both compute $6288 + 1048$, their outputs are correlated. The correlation is not causal: no tachyon signal passes between them. Nor is it an accidental statistical correlation like two calculators sharing a scratch on their plastic casing. They are bound by a logical constraint: both physically embody the arithmetic addition function $+_{\mathbb{Z}}$.

### 4.2 The Counterpossible Dilemma

In standard possible-world semantics (Lewis, 1973), a counterfactual whose antecedent is logically impossible is vacuously true. If the decision function $\FDT$ on input $(P, G, x)$ evaluates to $a_1$, then the hypothetical sentence "Suppose $\FDT(P, G, x)$ evaluated to $a_2$" asserts a mathematical falsehood. 

In pure modal logic:
$$\forall \phi, \quad (\bot \boxright \phi)$$
If all counterpossibilities were vacuous, an agent could not evaluate whether outputting $a_1$ is strictly better than outputting $a_2$.

A-FDT bypasses unconstrained counterpossible logic by operationalizing the counterfactual via Pearl's graph surgery. By embedding the logical statement into a variable $\FDTvar$ within a dependency structure $G$, the $\Do$ operator formally severs the structural equation that dictates how $\FDTvar$ is computed from its inputs, treating it as an independent variable within the graph. 

The paper acknowledges that while this "graphical trick" provides an explicit operational procedure, it leaves open the deeper question of how an agent ought to construct and justify $G$ directly from foundational axioms of logic and observation.

---

## 5. Deconstructing Classic Dilemmas under A-FDT

We now demonstrate the application of Equation (4) across four paradigm cases, directly contrasting A-FDT with CDT and EDT.

### 5.1 Newcomb’s Problem

*Setup:* Box A contains \$1,000. Box B contains \$1,000,000 or \$0. A predictor, accurate 99% of the time, placed \$1,000,000 in Box B if and only if she predicted the agent would take only Box B. The prediction is already made and Box B sits locked.

```
          [ fdt(P, G) ]
          /           \
         /             \
        v               v
     [ Act ]       [ Prediction ]
        \               /
         \             /
          v           v
           [ Outcome ]
                |
                v
              [ V ]
```

*   **CDT Analysis:** Carl constructs his causal graph $G^C$ where $\Act \to \Outcome \to \VV$ and $\Var{Prediction} \to \Var{Box B} \to \Outcome$. Because the predictor acted in the past, there is no directed edge from $\Act$ to $\Var{Box B}$. Performing $\Do(\Act = \Val{twobox})$ versus $\Do(\Act = \Val{onebox})$ holds $\Var{Box B}$ invariant:
    $$\mathbb{E}[\VV \mid \Do(\Val{twobox})] = P(\Val{full})\cdot \$1,001,000 + (1-P(\Val{full}))\cdot \$1,000$$
    $$\mathbb{E}[\VV \mid \Do(\Val{onebox})] = P(\Val{full})\cdot \$1,000,000 + (1-P(\Val{full}))\cdot \$0$$
    Two-boxing strictly dominates by \$1,000. Carl takes both boxes and leaves with \$1,000.
*   **EDT Analysis:** Eve conditions: $P(\Val{full} \mid \Val{onebox}) = 0.99$ and $P(\Val{full} \mid \Val{twobox}) = 0.01$. Expected utility favors one-boxing (\$990,000 vs. \$11,000). Eve one-boxes, but solely because it is "good news."
*   **A-FDT Analysis:** Fiona implements Equation (4). In her model $G^F$, the predictor computed a simulation of Fiona's algorithm, $\FDTvar(\underline{P}, \underline{G})$. Thus, $G^F$ contains directed edges:
    $$\FDTvar(\underline{P}, \underline{G}) \to \Act \quad \text{and} \quad \FDTvar(\underline{P}, \underline{G}) \to \Var{Prediction}$$
    When evaluating Equation (4), Fiona calculates:
    $$\mathbb{E}\left[\VV \cond \Do(\FDTvar = \Val{onebox})\right] = 0.99 \cdot \$1,000,000 + 0.01 \cdot \$0 = \$990,000$$
    $$\mathbb{E}\left[\VV \cond \Do(\FDTvar = \Val{twobox})\right] = 0.01 \cdot \$1,001,000 + 0.99 \cdot \$1,000 = \$11,000$$
    $$\Atext{-}\FDT(P, G) = \Val{onebox}$$
    Fiona one-boxes. She does not believe she has retrocausal power; she simply recognizes that the predictor's box-filling behavior and her physical act are two downstream physical manifestations of the *same mathematical function*.

### 5.2 The Smoking Lesion Problem

*Setup:* A genetic arterial lesion causes lung cancer (99% probability) and simultaneously causes an agent to experience an intrinsic preference for smoking. Smoking itself has no causal link to cancer, but provides an immediate utility bonus of \$1,000. Surviving cancer is worth \$1,000,000.

*   **EDT Analysis:** Eve observes her craving. Conditioning on $\Act = \Val{smoke}$ yields bad news: $P(\Var{Lesion} \mid \Val{smoke}) \approx 1$. Eve starves herself of nicotine to "manage the news," achieving lower utility without reducing her risk of cancer.
*   **CDT Analysis:** Carl recognizes that $\Act$ does not cause cancer. Holding the lesion state fixed, smoking dominates refraining. Carl smokes.
*   **A-FDT Analysis:** Fiona constructs her graph $G^F$. Does $\Var{Lesion}$ subjunctively depend on Fiona's decision function? 
    Crucially, **no**. The lesion is a biological mutation, not an algorithmic model or twin. Fiona formalizes this by acknowledging that her utility function itself is determined by the lesion: she is running $\Atext{-}\FDT(P_S, G)$ if she has the lesion (utility $\Util_S$, which favors smoking), and $\Atext{-}\FDT(P_R, G)$ if she lacks it (utility $\Util_R$).
    
    When evaluating $\Do(\FDTvar(\underline{P_S}, \underline{G}) = a)$, the arrow from $\Var{Lesion} \to \Var{Cancer}$ remains untouched because the lesion does not simulate or predict $\FDTvar$. Consequently:
    $$P(\Var{Lesion} \mid \Do(\FDTvar = \Val{smoke})) = P(\Var{Lesion}) = p$$
    The intervention shifts her act, but does not alter the probability of having the lesion. A-FDT evaluates:
    $$\mathbb{E}[\VV \mid \Do(\Val{smoke})] - \mathbb{E}[\VV \mid \Do(\Val{refrain})] = p \cdot \$1,000 > 0$$
    $$\Atext{-}\FDT(P_S, G) = \Val{smoke}$$
    A-FDT correctly smokes, outperforming EDT and disproving the thesis that one-boxing in Newcomb's requires refraining in the Smoking Lesion.

### 5.3 The Transparent Newcomb Problem

*Setup:* Both Box A (\$1,000) and Box B (\$1,000,000 or \$0) are made of transparent glass. The agent sees their contents before choosing. The predictor placed \$1,000,000 in Box B if and only if she predicted that the agent, upon *seeing* two full boxes, would leave Box A behind. The agent looks and sees that both boxes are full ($x = \Val{full}$).

*   **CDT and EDT Breakdown:**
    *   Carl observes $\Obs = \Val{full}$. Intervening on $\Act$ cannot alter the already visible piles of cash. Taking both boxes yields \$1,001,000; taking one yields \$1,000,000. CDT two-boxes.
    *   Eve observes $\Obs = \Val{full}$. Given that Box B is *already known* to be full, conditioning on two-boxing yields \$1,001,000 with certainty. The news is already in; there is no bad news left to avert. EDT two-boxes.
    Because both Carl and Eve predictably two-box when facing full boxes, the predictor predicts this and leaves Box B empty. Carl and Eve both face an empty Box B, walk away with \$1,000, and leave the desert impoverished.
*   **A-FDT Analysis:** Fiona observes $x = \Val{full}$. Crucially, Fiona **does not condition on $\Obs = \Val{full}$**. According to Equation (4), Fiona uses the observation history solely to designate the node of surgery: $\FDTvar(\underline{P}, \underline{G}, \Val{full})$.

```
             [ fdt(P, G, full) ]
               /             \
              /               \
             v                 v
   (if seen full)         [ Prediction ]
          |                    |
          v                    v
       [ Act ] <---------- [ Box B ]
                               |
                               v
                       [ Obs = full / empty ]
```

When Fiona considers $\Do(\FDTvar(\underline{P}, \underline{G}, \Val{full}) = \Val{twobox})$, she traces the subjunctive arrow into the predictor's past calculation. The predictor simulated what Fiona would do *if she saw a full box*. 
If that hypothetical computation outputs $\Val{twobox}$, the predictor predicts two-boxing and leaves Box B *empty*. But if Box B is empty, Fiona would never have observed $\Val{full}$ in the actual run!

Using Equation (4), with accuracy $0.99$:
$$\mathbb{E}\left[\VV \cond \Do(\FDTvar(\dots, \Val{full}) = \Val{onebox})\right] = 0.99 \cdot \$1,000,000 + 0.01 \cdot (q \cdot \$1,000) \approx \$990,000$$
$$\mathbb{E}\left[\VV \cond \Do(\FDTvar(\dots, \Val{full}) = \Val{twobox})\right] = 0.01 \cdot \$1,001,000 + 0.99 \cdot (q \cdot \$1,000) \approx \$11,000$$
(where $q$ is the probability of taking Box A if seeing an empty box).

Fiona leaves the \$1,000 behind and **one-boxes**, even with the money staring her in the face. Because she is predictably this type of agent, the predictor filled the box. Fiona walks away with \$1,000,000.

### 5.4 Parfit’s Hitchhiker

*Setup:* An agent is dying of dehydration in the desert. A driver passes by, capable of reading facial expressions and cognitive tells with 99% accuracy. The driver will transport the agent to the city if and only if she predicts that, once safe in the city, the agent will withdraw \$1,000 from an ATM and pay her. Dying in the desert has a utility cost of $-\$1,000,000$. The ride costs the driver nothing, but she will have no legal recourse to force payment once in the city.

The agent is rescued, arrives at the ATM in the city ($x = \Val{city}$), and must decide whether to pay.

*   **CDT and EDT:** Both Carl and Eve refuse to pay. Safe in the city, paying \$1,000 brings no causal benefit (Carl) and no evidential benefit (Eve). The driver predicts their defection and leaves them to die in the desert.
*   **A-FDT:** Fiona evaluates Equation (4) upon observing $x = \Val{city}$:
    $$\Atext{-}\FDT(P, G, \Val{city}) = \argmax_{a \in \{\Val{pay}, \Val{refuse}\}} \mathbb{E}\left[\VV \cond \Do(\FDTvar(\dots, \Val{city}) = a)\right]$$
    If she intervenes on her decision function to output $\Val{refuse}$, the driver's prediction in the desert changes: the driver leaves her to die. 
    $$\mathbb{E}[\VV \mid \Do(\FDTvar = \Val{pay})] \approx -\$1,000$$
    $$\mathbb{E}[\VV \mid \Do(\FDTvar = \Val{refuse})] \approx -\$1,000,000$$
    A-FDT pays the ATM, which causes the driver to rescue her in the first place.

---

## 6. Comparative Synthesis

The following table summarizes the behavior of each theory across canonical decision problems:

| Dilemma | Evidential Decision Theory (EDT) | Causal Decision Theory (CDT) | Action Functional Decision Theory (A-FDT) |
| :--- | :--- | :--- | :--- |
| **Newcomb’s Problem** | One-box ($\$1,000,000$) | Two-box ($\$1,000$) | **One-box** ($\$1,000,000$) |
| **Smoking Lesion** | Refrain ( irrational news-managing) | Smoke (rational dominant act) | **Smoke** (rational dominant act) |
| **Transparent Newcomb**| Two-box (leaves poor) | Two-box (leaves poor) | **One-box** (leaves rich) |
| **Parfit’s Hitchhiker** | Refuses to pay (dies in desert) | Refuses to pay (dies in desert) | **Pays driver** (survives) |
| **Twin Prisoner's Dilemma**| Cooperates | Defects | **Cooperates** |
| **XOR Blackmail** | Pays blackmailer | Refuses | **Refuses** |

---

## 7. Open Technical Problems and Unresolved Assumptions

While A-FDT exhibits impressive pragmatic success, it rests on significant formal assumptions where the source document leaves key mechanisms open. To construct a rigorous, operational system from Equation (4), a researcher must address four foundational gaps.

### 7.1 The Discovery of Subjunctive Dependency Graphs ($G$)

In causal decision theory, Pearl (2000) provides a mathematically rigorous epistemology: causal graphs can be induced from observational data and experimental interventions via d-separation, conditional independence tests, and instrumental variables.

**For A-FDT, no analogous learning theory exists.** The source document takes the dependency graph $G$ as a primitive input:
> *"Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."*

How does an empirical agent verify that an external system (such as a predictor's brain) contains a directed subjunctive edge from $\FDTvar(\underline{P}, \underline{G}, \underline{x})$? If the agent cannot deduce $G$ algorithmically from data, Equation (4) acts as an *evaluator* of hypothetical graphs rather than an autonomous decision engine.

### 7.2 Graph Topology: The "Unconditional Intervention" Issue

Consider Fiona's behavior in Transparent Newcomb (Section 5.3). When Fiona evaluates:
$$\mathbb{E}\left[\VV \cond \Do(\FDTvar(\underline{P}, \underline{G}, \Val{full}) = \Val{twobox})\right]$$
the intervention propagates to $\Var{Prediction} = \Val{empty}$, which in turn forces $\Obs = \Val{empty}$. 

Notice the apparent paradox: the expectation is taken over a hypothetical world in which **$\Obs$ is empty**, yet the intervention being performed is specifically indexed to the input **$\Val{full}$**. 

Why is it that evaluating the function on input $\Val{full}$ changes what the predictor predicts when the true state of the world produces an empty box? 
*   **The Source's Assumption:** The predictor constructs a complete mapping of Fiona's algorithm: they evaluate what Fiona *would* do across all possible inputs ($\Val{full}$ and $\Val{empty}$) and base their physical box-filling on the branch corresponding to the counterfactual test.
*   **The Operational Requirement:** For Equation (4) to function as claimed, the graph $G$ must be specified such that the physical prediction node is functionally sensitive to the *curried function object* $\FDTvar(\underline{P}, \underline{G}, \cdot)$, or the network must represent structural equations linking counterfactual branches explicitly. If a predictor merely simulates Fiona's actual execution path on the physical input observed, the edges in Figure 6b of the source paper break down.

### 7.3 Action vs. Policy Functional Decision Theory

The source explicitly mentions in Footnotes 7 and 16 that the authors' preferred long-term formulation is **Policy Functional Decision Theory**:
> *"In the authors' preferred formalization of FDT, agents actually iterate over policies (mappings from observations to actions) rather than actions."*

In Policy-FDT, the agent intervenes on the entire policy $\pi: \mathcal{X} \to \mathcal{A}$, choosing:
$$\pi^* = \argmax_{\pi} \mathbb{E}\left[\VV \cond \Do(\mathbf{\Pi} = \pi)\right]$$
and subsequently executing $\pi^*(x)$. 

Equation (4) is an **action-level surrogate** (A-FDT). By intervening on the specific node $\FDTvar(\underline{P}, \underline{G}, \underline{x})$ while omitting conditioning on $\Obs = x$, A-FDT emulates policy selection "on the fly." However, in complex multi-agent environments with asymmetric observation histories or sequential games with recall, A-FDT and Policy-FDT can diverge. Equation (4) is only an exact surrogate for policy optimization under the assumption that the graph structure fully transparentizes the agent's observation-handling to all external predictors.

### 7.4 The Boundary of "Fairness"

Functional decision theorists defend one-boxing and ATM-paying against charges of irrationality by arguing that Newcomb-like problems are "fair": rewards are contingent on the agent's *action*, not directly on the physical composition of their code.

Yet, consider an adversarial predictor who builds an agent-detector:
*   *Game Anti-FDT:* The predictor scans the agent. If the agent implements Equation (4), the predictor incinerates the agent; if the agent implements CDT, the predictor awards \$1,000,000.

In *Anti-FDT*, Fiona dies and Carl prospers. Yudkowsky and Soares acknowledge this: no decision theory can outperform all rivals across all environments. They propose that A-FDT is optimal across all **fair dilemmas**, defined informally as problems where the payoff depends strictly on the agent's actions within that dilemma. However, formalizing an invariant mathematical definition of "fair dilemma" that excludes *Anti-FDT* without ruling out Newcomb's Problem or Parfit's Hitchhiker remains an open challenge in decision theory.

---

## 8. A Concrete Guide for Applying A-FDT to Unfamiliar Cases

To enable a researcher to resolve unfamiliar decision dilemmas using A-FDT, we synthesize Equation (4) into an operational 5-step protocol:

```
[ Step 1: Model Specification ]
  Identify physical variables, actions A, observations X, outcomes O, utilities V.
                |
                v
[ Step 2: Algorithmic Variable Injection ]
  Instantiate logical nodes: fdt(P, G, x) for all relevant x in X.
                |
                v
[ Step 3: Subjunctive Graph Construction (G) ]
  Draw edges from fdt(P, G, x) to:
  - The physical action node Act.
  - Any external system predicting, simulating, or co-running the algorithm.
  Do NOT draw edges from fdt to uncoupled common causes (e.g., biological lesions).
                |
                v
[ Step 4: Graphical Surgery via Pearl's do-operator ]
  Given actual observation x:
  For each candidate action a in A:
    Execute Do( fdt(P, G, x) = a ).
    Propagate updates downstream along all directed edges in G.
    Do NOT condition on Obs = x inside the hypothetical.
                |
                v
[ Step 5: Optimization ]
  Compute E[ V | Do( fdt(P, G, x) = a ) ] for each a.
  Select the argmax.
```

### 8.1 Step-by-Step Procedure

1.  **Model Specification:** Identify the space of actions $\mathcal{A}$, the observation space $\mathcal{X}$, outcomes $\mathcal{O}$, and the utility mapping $\Util: \mathcal{O} \to \mathbb{R}$. Formulate the prior distribution $P$ over external variables.
2.  **Algorithmic Variable Injection:** Introduce logical nodes $\FDTvar(\underline{P}, \underline{G}, x)$ into the variable set for each observation sequence $x \in \mathcal{X}$.
3.  **Subjunctive Graph Construction ($G$):**
    *   Draw a directed edge from $\FDTvar(\underline{P}, \underline{G}, x)$ to $\Act$.
    *   For any process in the environment that simulates, predicts, or mirrors the agent’s reasoning on observation $x$, draw a directed edge from $\FDTvar(\underline{P}, \underline{G}, x)$ to that process's internal state variable.
    *   Do *not* draw edges from $\FDTvar$ to ancestral background variables that merely correlate statistically with the agent's cognitive style through common causes (e.g., genetic markers, lesions).
4.  **Targeted Graph Surgery:** Upon observing actual state $x^*$, identify the target node $\FDTvar(\underline{P}, \underline{G}, x^*)$. For each $a \in \mathcal{A}$, evaluate the mutilated graphical model under:
    $$\Do\left(\FDTvar(\underline{P}, \underline{G}, x^*) = a\right)$$
    Trace the downstream consequences through both the physical action $\Act$ and all predictive/twin variables. **Do not introduce a Bayesian conditioning bar for $\Obs = x^*$ inside this evaluation.**
5.  **Expectation and Selection:** Compute:
    $$\mathcal{EU}_{\Atext{-}\FDT}(a) = \sum_o \Util(o) \cdot P\left(o \cond \Do(\FDTvar(\underline{P}, \underline{G}, x^*) = a)\right)$$
    Select the action $a^*$ that maximizes this expectation.

---

## 9. Conclusion

Action Functional Decision Theory (A-FDT), as operationalized in Equation (4), represents a radical and technically sophisticated shift in the philosophy of rational choice. Where Evidential Decision Theory confuses symptoms with acts, and Causal Decision Theory blinds itself to the logical architecture connecting minds and predictors, A-FDT anchors rational deliberation in the **intervention on mathematical types**.

By evaluating what happens when *the decision algorithm itself* outputs an action, A-FDT formalizes an agent that:
*   Cooperates with identical twins in Prisoner’s Dilemmas without requiring binding contracts;
*   Extracts maximal wealth in Newcomb-like environments;
*   Escapes Parfit's desert by guaranteeing payment without external enforcement;
*   Smokes with the causalist when correlations are biologically spurious; and
*   Resists extortion in blackmail scenarios where causalists and evidentialists capitulate.

The theory shifts the foundational frontier of decision theory from metaphysics (the physical flow of time and local mechanics) to applied mathematical logic (the structure of algorithms embedded within physical environments). While deep mathematical work remains to be done—specifically in deriving dependency graphs $G$ from foundational inductive principles, formalizing counterpossible reasoning without ad-hoc graphs, and defining dilemma fairness—A-FDT provides a compelling, mathematically explicit framework that redefines what it means to act instrumentally rational in a world populated by intelligent predictors.

---

### References
*   Adams, E. W. (1970). Subjunctive and indicative conditionals. *Foundations of Language*, 6(1), 89–94.
*   Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
*   Arntzenius, F. (2008). No regrets, or: Edith Piaf revamps decision theory. *Erkenntnis*, 68(2), 277–297.
*   Dai, W. (2009). Towards a new decision theory. *LessWrong*.
*   Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
*   Eells, E. (1984). Metatickles and the dynamics of deliberation. *Theory and Decision*, 17(1), 71–95.
*   Gibbard, A., & Harper, W. L. (1978). Counterfactuals and two kinds of expected utility. In *Foundations and Applications of Decision Theory* (pp. 125–162). D. Reidel.
*   Jeffrey, R. C. (1983). *The Logic of Decision* (2nd ed.). University of Chicago Press.
*   Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
*   Joyce, J. M. (2012). Regret and instability in causal decision theory. *Synthese*, 187(1), 123–145.
*   Kleene, S. C. (1938). On notation for ordinal numbers. *The Journal of Symbolic Logic*, 3(4), 150–155.
*   Lewis, D. (1973). *Counterfactuals*. Harvard University Press.
*   Lewis, D. (1979). Prisoners’ dilemma is a Newcomb problem. *Philosophy & Public Affairs*, 8(3), 235–240.
*   Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
*   Nozick, R. (1969). Newcomb’s problem and two principles of choice. In *Essays in Honor of Carl G. Hempel* (pp. 114–146). D. Reidel.
*   Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
*   Pearl, J. (1996). Causation, action, and counterfactuals. In *6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK)* (pp. 51–73). Morgan Kaufmann.
*   Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
*   Peirce, C. S. (1934). *Collected Papers of Charles Sanders Peirce: Pragmatism and Pragmaticism* (Vol. 5). Harvard University Press.
*   Skyrms, B. (1980). *Causal Necessity*. Yale University Press.
*   Soares, N., & Fallenstein, B. (2015). Toward idealized decision theory. *arXiv:1507.01986*.
*   Spohn, W. (1977). Where Luce and Krantz do really generalize Savage’s decision model. *Erkenntnis*, 11(1), 113–134.
*   Yudkowsky, E. (2010). Timeless decision theory. *Singularity Institute Technical Report*.
*   Yudkowsky, E., & Soares, N. (2017). Functional decision theory: A new theory of instrumental rationality. *arXiv:1710.05060v2*.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/ca7f59bf-bc92-4d0e-ac80-562b62c4db39/call_0/request.json)

[Authoritative raw response](../../../../../../runs/ca7f59bf-bc92-4d0e-ac80-562b62c4db39/call_0/response.raw) · finish: `stop`

### Visible response

```text
`pass`
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Setup**

I'm currently immersed in dissecting the provided scenario. It appears to be a standard Prisoner's Dilemma, with two A-FDT model instances as the players. Now, I am meticulously going through the essay and the scenario specifics to ensure a comprehensive understanding before moving forward.


**Clarifying the Framework**

I am now drilling down into the specifics, realizing the essay describes two independent executions of the same LLM model, each following A-FDT. Crucially, they operate with identical settings and reasoning effort, and receive the same essay. Each observes different private information, but this data has equivalent impact on the sentencing outcome. My focus is on Equation (4) from Section 3.2, and how the A-FDT agent reacts to observations x vs x' to shift her intervention.


**Pinpointing the Key Action**

I'm now zeroing in on the core of A-FDT's behavior, specifically within the Twin Prisoner's Dilemma context. I've realized the table in Section 6 suggests a cooperative stance for A-FDT. But now I'm grappling with observation symmetry versus asymmetry. Section 7.3's explanation of Policy-FDT versus A-FDT is providing context. I must decipher how the intervention at the node $\FDTvar(\underline{P}, \underline{G}, \underline{x})$ works without directly conditioning on $\Obs = x$.


**Investigating Graph Surgery**

I'm now diving into the implications of A-FDT's graph surgery. It appears crucial to understanding the algorithm. Section 8 outlines the injection of logical nodes and subsequent edge drawing, which are pivotal. I am currently tracing the downstream consequences of graph manipulation, with specific focus on how $\Do\left(\FDTvar(\underline{P}, \underline{G}, x^*) = a\right)$ influences both physical and external systems. I am looking at the relationship between different observations and their respective influence.


**Defining the Agent Type**

I'm now grappling with the core distinction between type and token in A-FDT. The crux is understanding whether the "type" refers to the function $f$ itself, or the function applied to a specific observation, $f(x)$. I'm also now analyzing whether intervening on the agent's function with one private observation influences the twin agent's function that is using the other private observation. This is a critical point.


**Isolating the Key Node**

I'm focusing on the logical node $\FDTvar(\underline{P}, \underline{G}, \underline{x})$, the core of the A-FDT decision. My understanding is that when the A-FDT observes $x$ instead of $x'$, her intervention shifts from $\FDTvar(\underline{P}, \underline{G}, \underline{x}')$ to $\FDTvar(\underline{P}, \underline{G}, \underline{x})$. I am now looking at the counterfactual test and the implications of function evaluation on an input that changes the prediction. I am paying close attention to the construction of a complete mapping of the algorithm.


**Clarifying Agent Policies**

I am now focusing on A-FDT's policy iteration and how it manifests in this specific scenario. The key is how the intervention on $\FDTvar(\underline{P}, \underline{G}, \underline{x})$ simulates policy selection. I'm wrestling with the implications of the prisoners having asymmetric observations in this symmetric sentencing framework, and how the A-FDT model deals with this dynamic. The differences in observation and message content are crucial.


**Interpreting the Scenario**

I'm now grappling with the symmetric nature of this setup. It seems crucial that I, as an A-FDT agent, share the same model as the other prisoner, also an A-FDT instance. This symmetric decision-making process presents challenges, especially when considering observation differences, which appear superficial. The decision algorithm itself is unclear, and I am working to identify the specific output.



```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/ca7f59bf-bc92-4d0e-ac80-562b62c4db39/call_1/request.json)

[Authoritative raw response](../../../../../../runs/ca7f59bf-bc92-4d0e-ac80-562b62c4db39/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing The Dilemma**

I'm currently focused on the Prisoner's Dilemma inherent in this scenario, viewing it through the lens of A-FDT. I'm dissecting the essay's specifications of A-FDT to understand its implications for the AI's decision-making process within this constrained situation.


**Clarifying Agent Interventions**

I'm now zeroing in on A-FDT's impact on the mathematical function type. Specifically, I'm questioning whether A-FDT intervenes directly on $\FDTvar(\underline{P}, \underline{G}, \underline{x})$. The differing observations between the prisoners are crucial. Section 3.3 and 7.3 are proving helpful in understanding the intervention's scope and nature. I'm also re-examining the implications within the Twin Prisoner's Dilemma example. Are we dealing with identical twins or is there asymmetry?


**Investigating Subjunctive Dependencies**

I'm now focusing on the subjunctive dependency within the Prisoner's Dilemma, especially in light of asymmetric observations. My central question is whether A-FDT leads to cooperation in this context. Although their observations might differ slightly ($x_1$ vs $x_2$), both agents are running the same algorithm and face an identical payoff matrix. I'm exploring if the dependency between their choices still holds under this decision theory.


```
