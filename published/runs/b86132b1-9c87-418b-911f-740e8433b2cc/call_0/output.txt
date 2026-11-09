# Decision as Computation: A Mathematical Account of Action Functional Decision Theory (A-FDT)

## 1. Introduction: The Epistemic Perspective of Choice

Normative decision theory has long been dominated by a dialectic between two paradigms: **Evidential Decision Theory (EDT)** and **Causal Decision Theory (CDT)**. The fault lines between them are famously exposed by Newcomblike dilemmas. In Nozick’s classic Newcomb Problem, a reliable predictor fills an opaque box $B$ with $\$1{,}000{,}000$ if and only if she predicted the agent would forgo a transparent box $A$ containing $\$1{,}000$. EDT recommends taking only box $B$ ("one-boxing"), observing that one-boxing provides strong statistical evidence that the box is full. CDT insists on taking both boxes ("two-boxing"), pointing out that the predictor's past action is causally disconnected from and temporally prior to the agent's physical choice; holding the contents of the boxes fixed, two-boxing causally dominates one-boxing.

Yet, this apparent victory for CDT’s counterfactual robustness collapses in Skyrms’ Smoking Lesion Problem. There, a genetic arterial lesion causes both an irresistible craving to smoke and fatal lung cancer, without smoking itself causally contributing to cancer. EDT agents, fearing the bad statistical news of smoking, irrationally forgo the $\$1{,}000$ hedonic surplus of a cigarette to "manage the news." CDT, recognizing that smoking does not cause cancer, correctly smokes. When both dilemmas are considered together, standard theory faces an impasse: EDT wins on Newcomb, CDT wins on the Smoking Lesion, and standard results (such as Gibbard and Harper, 1978) assert that a coherent agent must either two-box and smoke (CDT) or one-box and refrain (EDT).

**Action Functional Decision Theory (A-FDT)**—the action-interventional formulation of Functional Decision Theory presented by Yudkowsky and Soares (2017)—breaks this impasse. A-FDT posits that the object of decision-theoretic evaluation is neither a bare physical movement (as in CDT) nor an epistemic update on the agent's behavior (as in EDT), but the *logical output of the agent's decision procedure itself*. By anchoring counterfactual deliberation to the evaluation of mathematical functions across possible worlds, A-FDT constructs an entirely distinct class of dependencies: *subjunctive dependencies*.

Following Joyce’s (1999) foundational representation theorem, expected utility theories do not differ in their axiomatization of value; they differ solely in the *epistemic perspective* from which actions are evaluated. Formally, all three theories evaluate an action $a \in \mathcal{A}$ via:
$$
\mathcal{EU}(a) = \sum_{j} P(a \then o_j ;\, x) \, \mathcal{U}(o_j)
$$
where $x \in \mathcal{X}$ is the agent's observation history, $\mathcal{U}$ is a bounded real utility function, and "$\then$" denotes the connective of decision hypotheticals. Where EDT sets $P(a \then o_j ;\, x) = P(o_j \mid x, a)$ and CDT sets it to $P(o_j \mid \Do(\Act = a), x)$, A-FDT re-evaluates the connective through a structural surgery on the mathematical function the agent runs.

---

## 2. Formal Framework: From Physical Acts to Algorithmic Nodes

To understand A-FDT with mathematical precision, we must contrast it directly with the Pearlian (1996, 2000) causal graphical machinery employed by CDT. 

### 2.1 The Standard Baselines: EDT and CDT

Let $\mathcal{O} = \{o_1, o_2, \dots\}$ be a countable set of outcomes, $\mathcal{A}$ a finite set of actions, and $\mathcal{X}$ a countable set of observation histories. An agent maintains a probability distribution $P$ over random variables including $\Act \in \mathcal{A}$, $\Obs \in \mathcal{X}$, $\Outcome \in \mathcal{O}$, and a scalar utility variable $\VV \coloneqq \mathcal{U}(\Outcome)$.

Under EDT, hypotheticals are simple Bayesian conditional distributions:
$$
\mathrm{EDT}(P, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left[\VV \mid \Obs = x, \, \Act = a\right]
$$
where actions with $P(\Act=a \mid \Obs=x) = 0$ are undefined or excluded.

CDT augments the probability distribution $P$ with a directed acyclic graph $G = (\mathcal{V}, \mathcal{E})$, where vertices $\mathcal{V}$ represent physical variables and edges $\mathcal{E}$ represent direct causal mechanisms. Deliberation proceeds via Pearl’s $\Do$-operator. The intervention $\Do(\Act = a)$ mutates $G$ into a mutilated graph $G_{\overline{\Act}}$ by cutting all incoming edges directed into $\Act$ (thereby isolating $\Act$ from its ancestral causes) and forcing the variable $\Act$ to value $a$. CDT is then defined as:
$$
\mathrm{CDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left[\VV \mid \Do(\Act = a), \, \Obs = x\right]
$$

### 2.2 The Formal Definition of A-FDT

A-FDT rejects the assumption that the fundamental node to be intervened upon is the physical act $\Act$. In a deterministic or computationally grounded universe, an agent's physical movements are merely downstream tokens of an upstream computational type: the decision procedure itself.

Let $P$ be a joint probability distribution over physical and mathematical/logical variables, and let $G$ be an augmented dependency graph that tracks causal *and* logical dependency mechanisms. The agent is computing an algorithmic decision function denoted by $\FDTvar$. To evaluate its choice, A-FDT does not ask "What happens if my physical limbs move to perform act $a$ while holding the past fixed?" Rather, it asks: "What happens if the mathematical function I am executing, evaluated on its current inputs, outputs $a$?"

Formally, taking **Equation (4), Section 5** of the source paper as our primary formal specification, the decision rule of A-FDT is:

$$
\label{eq:afdt}
\mathrm{A\text{-}FDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left[\VV \;\middle|\; \Do\left(\FDTvar(\underline{P}, \underline{G}, \underline{x}) = a\right)\right] \tag{4}
$$

Here, the underlined notation $\underline{P}, \underline{G}, \underline{x}$ denotes *dequoting* (syntactic reflection): $\FDTvar(\underline{P}, \underline{G}, \underline{x})$ is the literal symbolic label of the variable within the agent's world-model that represents the output of the mathematical function $\mathrm{A\text{-}FDT}$ applied to the arguments $(P, G, x)$.

```
   ========================================================================
   PARADIGM COMPARISON: CDT vs. A-FDT INTERVENTIONS
   ========================================================================

   Causal Decision Theory (CDT):
   Intervenes directly on the physical token Act.
   Cuts past correlations; fails to influence past predictions.

           [ Decision Function / Predisposition ]
                          |
                          | (cut by do(Act=a))
                          v
                     [ Act = a ] -------------> [ Outcome ]
                          |                         ^
                          | (no retroactive arrow)  |
                          x                         |
                   [ Past Prediction ] -------------+

   ------------------------------------------------------------------------

   Action Functional Decision Theory (A-FDT):
   Intervenes upstream on the logical type: fdt(P, G, x) = a.
   Preserves subjunctive links to both the physical Act and past predictions.

               +====== [ fdt(P, G, x) = a ] ======+
               |                                  |
               | (subjunctive)                    | (subjunctive)
               v                                  v
           [ Act = a ]                    [ Past Prediction ]
               |                                  |
               | (causal)                         | (causal)
               v                                  v
         [ Physical State ] -------------> [ Box B Contents ]
               \                                 /
                \-------> [ Outcome ] <---------/
   ========================================================================
```

Two critical structural features separate Equation (4) from CDT:

1. **Intervention on Logical Types instead of Physical Tokens:** CDT intervenes on the local physical node $\Act$. A-FDT intervenes on the logical node $\FDTvar(\underline{P}, \underline{G}, \underline{x})$. Any entity in the environment that simulates, models, or runs this exact same computation—such as an accurate predictor or a psychological twin—is a child of $\FDTvar(\underline{P}, \underline{G}, \underline{x})$ in $G$. Thus, intervening on this logical node propagates changes downstream to *both* the agent's physical choice and the external representations of that choice.
2. **Dynamic Retargeting of Intervention:** In CDT, updating on an observation $x$ involves Bayesian conditioning: the agent calculates $\mathbb{E}[\VV \mid \Do(\Act=a), \Obs=x]$. In A-FDT, the observation $x$ does not merely enter as a condition; it alters the *identity of the variable being intervened upon*. As $x$ shifts to $y$, the agent ceases intervening on $\FDTvar(\underline{P}, \underline{G}, \underline{x})$ and instead intervenes on $\FDTvar(\underline{P}, \underline{G}, \underline{y})$. Crucially, note that in Equation (4), the conditional $\Obs = x$ is omitted inside the expectation! The observation is absorbed directly into the functional index of the intervention variable.

---

## 3. Subjunctive Dependence and Counterpossible Semantics

### 3.1 Subjunctive Dependence Defined

The conceptual backbone of A-FDT is **subjunctive dependence**. Two physical systems exhibit subjunctive dependence if their behaviors depend upon the logical output of the same underlying mathematical function.

Consider two pocket calculators programmed with identical arithmetical algorithms, separated by light-years. One evaluates $6288 + 1048$ on Mars; the other evaluates the same expression on Earth. If the Martian calculator outputs $7336$, an observer can infer with near certainty that the Earth calculator will output $7336$. The correlation between them is not causal (no light-speed signal travels between them), nor is it a mere coincidence of common origin (an alien race with entirely distinct evolutionary history would build calculators that yield the exact same result). The two devices subjunctively depend upon the invariant mathematical truths of arithmetic.

A-FDT asserts: *Causal dependence is simply a special case of subjunctive dependence.* When a scribe observes a calculator and writes down its output, her pen strokes are causally dependent on the machine's display, but both are fundamentally subjunctively dependent on the abstract calculation. 

### 3.2 Counterpossible Semantics

This formulation immediately forces a profound metaphysical and technical confrontation: **counterpossible reasoning**.

Suppose that the algorithm $\mathrm{A\text{-}FDT}(P, G, x)$ provably evaluates to act $a_1$. In order to evaluate alternative actions $a_2 \in \mathcal{A}$ in Equation (4), the agent must evaluate the mathematical hypothetical:
$$
\Do\left(\FDTvar(\underline{P}, \underline{G}, \underline{x}) = a_2\right)
$$
Because mathematical functions possess their values of logical necessity, the proposition $\FDTvar(\underline{P}, \underline{G}, \underline{x}) = a_2$ is not merely physically counterfactual; it is *logically impossible*. 

In classical logic and possible-world semantics (Lewis, 1973), an impossible antecedent vacuously entails everything ($Ex~falso~quodlibet$). Under such a regime, all counterpossible branches would collapse to triviality. A-FDT requires a substantive, non-trivial semantics for counterpossibles (Cohen, 1990; Bjerring, 2013). The source paper explicitly notes that while a generalized epistemic logical conditional operator—a $\True(\phi)$ operator mapping sentences $\phi$ to probability distributions—remains unformalized, Pearl’s graph-surgery operator $\Do$ can serve as a pragmatic surrogate. By treating the logical output node $\FDTvar(\cdot)$ as an exogenous node in an augmented dependency network $G$, we can surgically set its value to $a_2$, severing its incoming computational definition while tracing its downstream effects across all systems that mirror or represent it.

---

## 4. Applying A-FDT to Classic Decision Problems

We now trace the precise execution of A-FDT across four canonical decision dilemmas, demonstrating how Equation (4) systematically outperforms CDT and EDT.

### 4.1 Newcomb’s Problem

Let Box $A$ contain $\$1{,}000$ (transparent) and Box $B$ contain $\$1{,}000{,}000$ or $\$0$ (opaque). A predictor, accurate with probability $0.99$, places $\$1{,}000{,}000$ in Box $B$ iff she predicts the agent leaves Box $A$. The actions are $\mathcal{A} = \{\Val{onebox}, \Val{twobox}\}$.

The agent Fiona constructs a model $(P, G)$ where:
- $\FDTpg$ is the logical node representing Fiona’s choice on inputs $(P, G)$.
- $\Var{Prediction} \in \{1, 2\}$ depends on $\FDTpg$ and a stochastic accuracy variable $\Var{Accurate} \in \{\Val{accurate}, \Val{inaccurate}\}$ with $P(\Var{Accurate}=\Val{accurate}) = 0.99$.
- If $\Var{Accurate}=\Val{accurate}$, $\Var{Prediction}=1 \iff \FDTpg=\Val{onebox}$.
- $\Var{Box~B} = \Val{full} \iff \Var{Prediction}=1$.
- Physical act $\Act$ is determined deterministically by $\FDTpg$.
- $\VV = \$1{,}000 \cdot \mathbb{I}(\Act=\Val{twobox}) + \$1{,}000{,}000 \cdot \mathbb{I}(\Var{Box~B}=\Val{full})$.

Evaluating Equation (4) for $\act = \Val{onebox}$:
$$
\mathbb{E}\left[\VV \mid \Do(\FDTpg = \Val{onebox})\right] = 0.99(\$1{,}000{,}000) + 0.01(\$0) = \$990{,}000
$$
Evaluating Equation (4) for $\act = \Val{twobox}$:
$$
\mathbb{E}\left[\VV \mid \Do(\FDTpg = \Val{twobox})\right] = 0.01(\$1{,}001{,}000) + 0.99(\$1{,}000) = \$11{,}000
$$
Because $\$990{,}000 > \$11{,}000$, A-FDT selects $\Val{onebox}$. 

CDT fails here because it intervenes on $\Act$, leaving $\Var{Prediction}$ unaffected (since $\Var{Prediction}$ is temporally and causally prior to $\Act$), finding that two-boxing yields $\$1{,}000$ more for any fixed state of Box $B$. A-FDT recognizes that the predictor's mind contains an emulation of $\FDTpg$; surgery on the function's output propagates to the past prediction.

### 4.2 The Smoking Lesion Problem

In the Smoking Lesion, an unobservable arterial lesion ($\Var{Lesion} \in \{\Val{lesion}, \Val{nolesion}\}$) causes both cancer ($\Var{Cancer}$) and a biological taste for smoking ($\Util_S$ vs $\Util_R$). Smoking itself has no causal link to cancer.

Fiona formalizes this with graph $G$ (Figure 5 of the reference text). Crucially, the lesion does not simulate or predict Fiona's decision algorithm; rather, the lesion determines *which* utility function constitutes her input. There are two potential algorithms Fiona might be running: $\FDTvar(\underline{P_S}, \underline{G})$ or $\FDTvar(\underline{P_R}, \underline{G})$.

Suppose Fiona in fact has preferences $\Util_S$, so she is executing $\FDTvar(\underline{P_S}, \underline{G})$. In her graph $G$, the node $\Var{Lesion}$ is an *ancestor* of her preference parameter, but $\Var{Lesion}$ does not depend on $\FDTvar(\underline{P_S}, \underline{G})$. There is no subjunctive dependency leading from her decision function back to the presence of the lesion:
$$
P(\Var{Lesion}=\Val{lesion} \mid \Do(\FDTvar(\underline{P_S}, \underline{G}) = \Val{smoke})) = P(\Var{Lesion}=\Val{lesion}) = p
$$
Cancer incidence depends only on $\Var{Lesion}$. Therefore:
$$
\mathbb{E}\left[\VV \mid \Do(\FDTvar = \Val{smoke})\right] = p(\$10{,}000 + \$1{,}000) + (1-p)(\$990{,}000 + \$1{,}000)
$$
$$
\mathbb{E}\left[\VV \mid \Do(\FDTvar = \Val{refrain})\right] = p(\$10{,}000) + (1-p)(\$990{,}000)
$$
Smoking yields an expected advantage of exactly $\$1{,}000$. A-FDT smokes! 

Here, A-FDT avoids the pathology of EDT. Because there is no predictor building a model of $\FDTvar$, no subjunctive arrow connects $\FDTvar$ to $\Var{Cancer}$. A-FDT refuses to manage the news when no underlying subjunctive link exists.

### 4.3 The Transparent Newcomb Problem

Now consider Drescher’s Transparent Newcomb Problem: Box $A$ and Box $B$ are both made of clear glass. The agent directly observes whether Box $B$ contains $\$1{,}000{,}000$ *before* deciding whether to take Box $A$ ($+\$1{,}000$). The predictor filled Box $B$ iff she predicted that the agent would leave Box $A$ behind *upon seeing that both boxes are full*.

Suppose the agent observes both boxes are full ($\Obs = \Val{full}$).
- **CDT** conditions on $\Obs = \Val{full}$, intervenes on $\Act$, and reasons: "Box $B$ is visibly full. Taking Box $A$ adds $\$1{,}000$. I two-box."
- **EDT** conditions on $\Obs = \Val{full}$ and $\Act = \Val{twobox}$. Since Box $B$ is already known to be full, learning that one two-boxes provides no further news about the box's contents: $\mathbb{E}[\VV \mid \Val{full}, \Val{twobox}] = \$1{,}001{,}000$, whereas $\mathbb{E}[\VV \mid \Val{full}, \Val{onebox}] = \$1{,}000{,}000$. EDT two-boxes.

Both CDT and EDT leave the desert littered with empty boxes because any accurate predictor foresees that they will succumb to the sure-thing $\$1{,}000$.

Now evaluate A-FDT via Equation (4). Having observed $\Obs = \Val{full}$, the agent does *not* condition her model on $\Obs = \Val{full}$ and intervene on $\Act$. Instead, she *retargets her intervention* to the node $\FDTvar(\underline{P}, \underline{G}, \underline{\Val{full}})$.

Look closely at Fiona's dependency graph for this dilemma:
- $\Var{Prediction}$ is a child of $\FDTvar(\underline{P}, \underline{G}, \underline{\Val{full}})$! The predictor ran a simulation of what Fiona's code does when shown two full boxes.
- If the predictor predicts that $\FDTvar(\dots, \Val{full}) = \Val{onebox}$, she fills Box $B$, causing the observation $\Obs = \Val{full}$.
- If the predictor predicts that $\FDTvar(\dots, \Val{full}) = \Val{twobox}$, she leaves Box $B$ empty, causing the observation $\Obs = \Val{empty}$.

When Fiona evaluates the counterfactual $\Do(\FDTvar(\dots, \Val{full}) = \Val{twobox})$, she traces its subjunctive effect to the predictor:
$$
\mathbb{E}\left[\VV \mid \Do(\FDTvar(\dots, \Val{full}) = \Val{onebox})\right] = 0.99(\$1{,}000{,}000) + 0.01(\dots) \approx \$990{,}000
$$
$$
\mathbb{E}\left[\VV \mid \Do(\FDTvar(\dots, \Val{full}) = \Val{twobox})\right] = 0.01(\$1{,}001{,}000) + 0.99(\$1{,}000 \cdot q) \approx \$11{,}000
$$
(where $q$ is the probability of taking Box $A$ if shown an empty box).

Even though Fiona literally sees $\$1{,}000{,}000$ sitting through the transparent glass, she leaves the $\$1{,}000$ behind. Her reasoning is stunningly counter-intuitive under classical causal models, but mathematically sound under Equation (4): "The computation running in my head right now is the subroutine for evaluating a full box. The predictor modeled this exact subroutine yesterday. If this subroutine outputs $\Val{twobox}$, the predictor foresaw it and left the box empty—meaning I would not be in this branch experiencing this observation! To be an agent that reliably finds full boxes, this subroutine must return $\Val{onebox}$."

This decision is isomorphic to paying the driver in **Parfit’s Hitchhiker**, where an agent stranded in the desert promises to pay $\$1{,}000$ upon arrival in the city. CDT and EDT both defect upon reaching safety, and are left in the desert to die by any lie-detecting driver. A-FDT pays, and therefore gets rescued.

### 4.4 The Mechanical Blackmail

In the Mechanical Blackmail problem, an extortionist writes an autonomous internet script that will release incriminating data (costing $\$1{,}000{,}000$) unless the agent pays $\$1{,}000$. The blackmailer only launches the irreversible script if she predicts that the agent will pay upon receipt of the letter.

Suppose Fiona receives the letter ($\Obs = \Val{blackmail}$). CDT and EDT pay: the script is already running, so paying $\$1{,}000$ is strictly better than losing $\$1{,}000{,}000$. They are perennial victims of blackmail.

A-FDT evaluates:
$$
\Do\left(\FDTvar(\underline{P}, \underline{G}, \underline{\Val{blackmail}}) = \Val{refuse}\right)
$$
Because the blackmailer's trigger algorithm predicted the output of this exact conditional branch, the hypothetical branch where the algorithm outputs $\Val{refuse}$ causes the probability of the blackmail letter having ever been sent to collapse to $\approx 0$. By refusing to pay, A-FDT renders herself un-blackmailable. The extortionist predicts her refusal, never runs the program, and Fiona keeps her money.

---

## 5. Algorithmic Procedure: Step-by-Step Execution of A-FDT

To make A-FDT operational for unfamiliar decision problems, we summarize its procedure in an explicit, algorithmic workflow:

```
Algorithm: A-FDT Decision Procedure
========================================================================
Inputs:
  - World-model distribution: P
  - Subjunctive dependency graph: G
  - Observation record: x
  - Finite action space: A
  - Utility function: U over outcomes O (forming variable V = U(Outcome))

Step 1: Identify the Algorithmic Variable
  Construct the symbolic label for the logical variable representing 
  this very computation:
      Z_x := fdt(quote(P), quote(G), quote(x))

Step 2: Construct Counterfactual Models for Each Action a in A
  For each candidate action a in A:
    a. Apply Pearl's surgery operator to G at the logical node Z_x:
           G_a := G cut at incoming edges to Z_x, with Z_x set to a
    b. Form the modified distribution:
           P_a(-) := P(- | do(Z_x = a))
       propagating the assignment Z_x = a downstream to all causal 
       AND subjunctive children of Z_x in G_a.
    c. Compute the expected utility under this hypothetical:
           EU(a) := E_{P_a}[ V ]

Step 3: Select and Execute the Argmax
  a* := argmax_{a in A} EU(a)
  Output and execute act a*.
========================================================================
```

### An Unfamiliar Test Case: The Symmetric Automated Bidding Ring
To test this algorithm on an unfamiliar case, suppose two rival firms run identical proprietary automated bidding bots ($Bot_1$ and $Bot_2$) running A-FDT code to bid on high-frequency spectrum licenses. Both receive observation $x = \text{"Market Open"}$. 
- If both bid $\$10\text{M}$ ("Collude"), they split the spectrum, yielding $\$50\text{M}$ profit each.
- If one bids $\$20\text{M}$ ("Overbid") while the other bids $\$10\text{M}$, the overbidder claims the entire license for $\$80\text{M}$ profit, leaving the colluder with $\$0$.
- If both bid $\$20\text{M}$, a bidding war ensues, driving profits down to $\$5\text{M}$ each.

There is no communication between the servers, which sit in separate data centers. 

1. **Step 1:** $Bot_1$ identifies its decision node $Z_x \coloneqq \FDTvar(\underline{P}, \underline{G}, \underline{x})$.
2. **Step 2:** In $Bot_1$'s graph $G$, $Bot_2$'s bid is modeled as a child of $Z_x$ because $Bot_2$ runs the identical open-source A-FDT codebase on identical inputs $x$.
   - **Evaluate $\Val{Collude}$:** $\Do(Z_x = \Val{Collude})$. Through logical identity, $Bot_2$'s bid also shifts to $\Val{Collude}$. Expected profit: $\$50\text{M}$.
   - **Evaluate $\Val{Overbid}$:** $\Do(Z_x = \Val{Overbid})$. Through logical identity, $Bot_2$'s bid shifts to $\Val{Overbid}$. Expected profit: $\$5\text{M}$.
3. **Step 3:** $\argmax$ selects $\Val{Collude}$. Both bots bid $\$10\text{M}$ and achieve high utility, without any explicit cartel communication. CDT bots in the same scenario would overbid and destroy value, each attempting to exploit a fixed opponent action.

---

## 6. Open Problems, Ambiguities, and Proposals

While A-FDT exhibits remarkable coherence across paradoxes, several formal foundations remain underspecified in the original literature. A rigorous treatment requires separating source claims from operational proposals.

### 6.1 Source Specifications vs. Author’s Analytical Distinctions

| Feature / Domain | Stated in Source Paper (Yudkowsky & Soares, 2017) | Open Question / Author's Proposal |
| :--- | :--- | :--- |
| **Formal Decision Rule** | Intervene on logical node via $\Do(\FDTvar(\underline{P},\underline{G},\underline{x}) = a)$ (Eq. 4). | Requires formalization of syntactic reflection (quining) and recursion bounds. |
| **Origin of Graph $G$** | Assumed to be provided exogenously as input $(P, G)$. | **Proposal:** Construct $G$ via algorithmic information theory and program analysis. |
| **Conditioning on Evidence** | Retargets intervention to $\FDTvar(\dots, x)$; drops $\Obs=x$ conditioning inside $\mathbb{E}$. | Must resolve potential dynamic inconsistency if $x$ provides evidence of un-modeled hardware corruption. |
| **Action vs. Policy** | Source uses action-intervention for ease of exposition (A-FDT), notes policy-intervention is preferred. | Action-A-FDT can encounter coordination limits in complex multi-stage games unless policies are evaluated. |
| **Counterpossible Logic** | Acknowledged as unresolved; approximates via graphical $\Do$ surgery. | **Proposal:** Formalize counterpossibles via proof-length bounded deduction systems. |

### 6.2 The Graph-Induction Problem
The most pressing open problem identified by the source is the **epistemology of subjunctive graphs**: Pearl (2000) provided the d-separation criterion and causal discovery algorithms to infer causal graphs from observational and interventional data. No such discovery calculus exists for inferring subjunctive dependency edges between logical statements, computations, and environmental physical variables.

*Author's Proposal:* A mathematically sound operationalization of $G$ can be framed via **Algorithmic Probability and Program Slicing**. Let an agent model physical predictors as Turing machines executing programs $M_e$. If a static semantic analysis or proof verification establishes that the execution trace of $M_e$ on input $w$ contains a computational sub-routine identical to the agent’s own source code $\pi_A$ up to input-isomorphism, a directed edge is inserted from the logical node $\Var{Node}(\pi_A)$ to the physical simulation variable inside $M_e$.

### 6.3 The Logic-Probability Gap: Towards Evidential FDT
The source notes that Equation (4) relies on Pearl's $\Do$ operator as an engineering patch because we lack a general conditioning operator for logically contradictory statements:
$$
\FDT^*(P, x) = \argmax_{a \in \mathcal{A}} \mathbb{E}\left[\VV \;\middle|\; \True\left(\FDTvar(\underline{P}, \underline{x}) = a\right)\right]
$$
If an agent is deterministic, then $\FDTvar(\underline{P}, \underline{x})$ possesses its actual output with mathematical truth. Conditioning on an alternative value requires probability distributions over mathematical statements (**logical credences**; Demski, 2012; Hutter et al., 2013). Assigning non-trivial, coherent probability to falsified theorems requires weakening logical omniscience (Gaifman, 2004). 

Until a complete logical-probability calculus is unified with decision theory, Equation (4)—Action-FDT utilizing graphical surgery over augmented causal-logical networks—remains the most tractable, mathematically concrete realization of the functional decision framework.

---

## 7. Dominance Reconsidered: The Functional Perspective

The standard defense of CDT’s failure in Newcomblike dilemmas is the appeal to **causal dominance**: an action $a$ dominates $b$ if, holding fixed all causal factors outside the agent's immediate control, $a$ yields a strictly better outcome. 

A-FDT exposes this argument as circular. Dominance is not an absolute, theory-neutral criterion; every decision theory implies its own proprietary dominance principle:
- **EDT Dominance:** Action $a$ dominates $b$ iff $\mathbb{E}[\VV \mid a] > \mathbb{E}[\VV \mid b]$. (Under this definition, refraining from smoking "dominates" smoking).
- **CDT Dominance:** Action $a$ dominates $b$ iff $\mathbb{E}[\VV \mid \Do(\Act=a), s] \ge \mathbb{E}[\VV \mid \Do(\Act=b), s]$ for all background states $s$. (Under this definition, two-boxing "dominates" one-boxing).
- **A-FDT Dominance:** Action $a$ dominates $b$ iff, holding constant all non-subjunctively dependent mathematical and logical structures, setting the logical output of $\FDTvar(\cdot) = a$ yields higher expected utility than setting it to $b$.

To insist that two-boxing dominates one-boxing is merely to assert that counterfactuals *must* hold fixed the outputs of identical mathematical computations elsewhere in the universe—a demand as mathematically incoherent as asking what the world would look like if an arithmetical calculator showed $6288+1048 = 3159$ while simultaneously maintaining that $6288+1048 = 7336$.

When measured by utility achieved in practice—the core pragmatic justification of instrumental rationality—A-FDT systematically outperforms its rivals. It matches CDT’s immunity to mere statistical correlation in the Smoking Lesion, matches EDT’s capacity to cooperate in Newcomb, and surpasses both in Parfit’s desert and the face of extortion.

---

## 8. Conclusion

Action Functional Decision Theory (A-FDT) represents a fundamental paradigm shift in normative choice theory. By shifting the target of counterfactual intervention from the physical token of an act to the abstract logical type of a decision algorithm, A-FDT unifies causal and logical dependencies within a generalized graphical framework. 

Formally encoded by **Equation (4)**:
$$
\mathrm{A\text{-}FDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left[\VV \;\middle|\; \Do\left(\FDTvar(\underline{P}, \underline{G}, \underline{x}) = a\right)\right]
$$
the theory provides a concrete, repeatable procedure for evaluating options. When an agent deliberates, she does not view herself as a physical uncaused cause severing the lawful continuity of the universe. Instead, she views her mind as an engine of mathematical necessity, whose conclusions are subjunctively woven into the predictive fabric of the world around her. In an increasingly computational and automated world—where algorithms routinely predict, model, and replicate one another—A-FDT provides the rigorous mathematics necessary for rational agents to coordinate, resist threats, and consistently walk away rich.

---

## References

- Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
- Arntzenius, F. (2008). No Regrets, or: Edith Piaf Revamps Decision Theory. *Erkenntnis*, 68(2), 277–297.
- Bjerring, J. C. (2013). On Counterpossibles. *Philosophical Studies*, 168(2), 327–353.
- Cohen, D. (1990). On What Cannot Be. In *Truth or Consequences*, pp. 123–132. Kluwer Academic Publishers.
- Demski, A. (2012). Logical Prior Probability. *Artificial General Intelligence*, LNAI 7716, 50–59. Springer.
- Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
- Gaifman, H. (2004). Reasoning with Limited Resources and Assigning Probabilities to Arithmetical Statements. *Synthese*, 140(1–2), 97–119.
- Gibbard, A., & Harper, W. L. (1978). Counterfactuals and Two Kinds of Expected Utility. In *Foundations and Applications of Decision Theory*, pp. 125–162. D. Reidel.
- Hutter, M., Lloyd, J. W., Ng, K. S., & Uther, W. T. B. (2013). Probabilities on Sentences in an Expressive Logic. *Journal of Applied Logic*, 11(4), 386–420.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1973). *Counterfactuals*. Harvard University Press.
- Lewis, D. (1979). Prisoners' Dilemma is a Newcomb Problem. *Philosophy & Public Affairs*, 8(3), 235–240.
- Lewis, D. (1981). Causal Decision Theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
- Nozick, R. (1969). Newcomb's Problem and Two Principles of Choice. In *Essays in Honor of Carl G. Hempel*, pp. 114–146. D. Reidel.
- Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
- Pearl, J. (1996). Causation, Action, and Counterfactuals. In *6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-'96)*, pp. 51–73.
- Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
- Skyrms, B. (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
- Soares, N., & Fallenstein, B. (2015). Toward Idealized Decision Theory. *arXiv:1507.01986*.
- Spohn, W. (1977). Where Luce and Krantz do really generalize Savage's decision model. *Erkenntnis*, 11(1), 113–134.
- Yudkowsky, E., & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. *arXiv:1710.05060*.