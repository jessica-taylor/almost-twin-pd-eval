# Choosing the Program, Not Just the Move: A Mathematical Exposition of Policy Functional Decision Theory (P-FDT)

## 1. Introduction: The Dialectic of Rational Choice

Normative decision theory has long been caught in a deadlock between two dominant paradigms: Evidential Decision Theory (EDT) and Causal Decision Theory (CDT). Each theory encodes a distinct epistemic stance on how hypothetical deliberations connect to the external world. 

EDT evaluates an action $\act$ by conditioning its world-model directly on the observation that the agent has performed $\act$:
\[
\EDT(P, \obs) \coloneqq \argmax_{\act \in \mathcal{A}} \sum_{o \in \mathcal{O}} P(\Outcome = o \mid \Obs = \obs, \Act = \act) \, \Util(o).
\]
While EDT correctly reaps high rewards in predictive dilemmas such as Newcomb’s Problem by capturing the diagnostic link between choices and external predictions, it stumbles catastrophically into "news-managing." In problems like the Smoking Lesion or the XOR Blackmail, EDT treats non-causal statistical correlations as actionable levers, abstaining from harmless benefits or paying extortionists merely to suppress bad omens.

CDT repairs this pathology by replacing Bayesian conditioning with Pearlian causal surgery. Intervening directly on the physical realization of the act via the $\Do$-operator, CDT severs incoming causal arrows to the action node:
\[
\CDT(P, G, \obs) \coloneqq \argmax_{\act \in \mathcal{A}} \sum_{o \in \mathcal{O}} P(\Outcome = o \mid \Do(\Act = \act), \Obs = \obs) \, \Util(o).
\]
CDT refuses to manage the news: in the Smoking Lesion, it smokes, recognizing that the genetic lesion cannot be eradicated retroactively by physical restraint. Yet CDT's surgical knife cuts too deep. By holding fixed all facts that are not causally downstream of the physical action token, CDT imagines worlds where an accurate predictor's past forecast remains frozen even as the agent counterfactually alters her choice. This leads CDT to two-box in Newcomb’s Problem, defect against psychological twins in the Prisoner’s Dilemma, and die in the desert in Parfit’s Hitchhiker.

In *Functional Decision Theory: A New Theory of Instrumental Rationality*, Eliezer Yudkowsky and Nate Soares introduce Functional Decision Theory (FDT). FDT resolves the conflict by moving the target of counterfactual intervention from the *physical action token* ($\Act = \act$) to the *logical function type* that computes the action. Rather than asking, "What happens if my physical arm moves differently?", an FDT agent asks: "What happens if this very decision algorithm outputs a different result?"

The primary body of Yudkowsky and Soares (2017) formalizes an *act-intervening* version of this intuition: upon receiving an observation $\obs$, the agent intervenes on the specialized function variable instantiated on that specific observation:
\[
\FDT(P, G, \obs) \coloneqq \argmax_{\act \in \mathcal{A}} \EE\left( \VV \;\middle|\; \Do(\FDTvar(\underline{P}, \underline{G}, \underline{\obs}) = \act) \right).
\]
In **Footnote 16** (and the prefatory Footnote 7), however, the authors reveal an important qualification:
> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions... As mentioned earlier, the authors' preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action."

This essay is an investigation and rigorous mathematical construction of that preferred formulation: **Policy Functional Decision Theory (P-FDT)**. We will unpack why optimizing over complete mathematical policies, rather than local function outputs, constitutes the natural summit of the functional-decision-theoretic program; formalize P-FDT using augmented structural causal models over function spaces; analyze how P-FDT resolves classical dilemmas; and identify the open technical problems at the frontier of the theory.

---

## 2. Foundations: Subjunctive Dependence and Algorithmic Realization

The philosophical foundation of FDT—and by extension, P-FDT—rests on the concept of **subjunctive dependence**. 

### 2.1 Logical Identity Across Spacetime
Physical systems often implement the exact same abstract mathematical function. Two identical, well-functioning calculators calculating $6288 + 1048$ are physically distinct entities across space, yet their outputs are logically constrained to coincide:
\[
\text{Calc}_A = 7336 \iff \text{Calc}_B = 7336.
\]
This correspondence is neither a causal link (Calculator A does not send a signal to Calculator B) nor an accident of statistical coincidence. Rather, the states of both machines subjunctively depend upon a common mathematical reality: the value of the function $+_{\mathbb{N}}(6288, 1048)$.

In decision settings where other agents predict our choices—or where our psychological copies face symmetric games—those predictors must instantiate a computational representation of our deliberation. If a predictor simulates my decision logic to forecast my behavior, the predictor's forecast and my ultimate action are two downstream physical traces of the same logical type. 

### 2.2 Token vs. Type Interventions
CDT intervenes on the physical token: it sets $\Do(\Act = \act)$. Graphically, this clips the causal arrows entering $\Act$, rendering the action independent of the agent’s own prior computational state and independent of any predictor who simulated that state. CDT counterfactuals ask: "What if my physical limbs moved differently, while the predictor's completed simulation of me in the past remained identical?" As the source paper demonstrates, this hypothetical describes a physical impossibility: a broken prediction from an inerrant predictor.

FDT intervenes on the logical type. It asks: "What if the mathematical function that characterizes my mind had a different property?" When an FDT agent counterfactually alters the output of her algorithm, that modification propagates through all nodes in the structural network that depend upon that algorithm—including the historical predictions derived from running that code.

---

## 3. The Need for Policies: Motivating P-FDT

Why does Footnote 16 elevate policy selection over action selection? 

Consider an agent choosing an action $\act \in \mathcal{A}$ after conditioning on an observation history $\obs \in \mathcal{X}$. In the standard act-based FDT equation (Equation 4 of the source), the agent intervenes on the variable $\FDTvar(\underline{P}, \underline{G}, \underline{\obs})$. In problems like the Transparent Newcomb Problem or the Mechanical Blackmail, the author points out that Fiona (the FDT agent) handles this by refusing to condition her probability distribution on having seen the observation $\obs$. Instead, she *switches which node she intervenes upon*: she intervenes on $\FDTvar(\dots, \Val{full})$ or $\FDTvar(\dots, \Val{blackmail})$.

Yet this mechanism is conceptually fragile. When an agent receives an observation $\obs$, classical probability kinematics mandates that she condition her world-model: $\model \to \model \mid \Obs = \obs$. If she conditions on $\Obs = \Val{blackmail}$ before intervening, she immediately learns that the blackmailer has already sent the letter. In a causal graph where $\Obs$ is already fixed to $\Val{blackmail}$, intervening locally on what the function does *specifically at input $\Val{blackmail}$* requires delicate multi-node surgery to maintain that changing the function's evaluation at $\Val{blackmail}$ subjunctively retro-causes the blackmailer not to have sent the letter—a situation that generated the observation $\Val{blackmail}$ to begin with.

The source paper notes in passing:
> "Another early variant, the 'Timeless Decision Theory' of Yudkowsky (2010), prescribes both conditioning on evidence *and* changing the place where one intervenes; this creates a kind of 'double update' which proves harmful in practice."

**Policy Functional Decision Theory (P-FDT)** resolves this conceptual tension at the root. A policy is a complete mapping:
\[
\pi \colon \mathcal{X} \to \mathcal{A}.
\]
Under P-FDT, the fundamental object of rational evaluation is never an isolated action $\act$, nor even an observation-indexed function slice $f(\obs)$. The object of evaluation is the **entire policy $\pi$**. 

An agent does not deliberate by asking: "Given that I have observed $\obs$, which action shall I output?" Rather, the agent's cognitive architecture evaluates: "Which global mapping $\pi$ from observations to actions maximizes expected utility across all potential environments and encounters, when viewed from the foundational, global perspective?" Once the optimal policy $\pi^*$ is identified, the execution of an action at a particular instance $\obs_0$ is purely mechanical:
\[
\act = \pi^*(\obs_0).
\]
By moving the intervention to the policy level, P-FDT seamlessly integrates the "updateless" perspective (Dai 2009). The agent does not need to awkwardly "un-see" an observation or toggle intervention nodes on the fly. Counterfactually varying $\pi$ naturally alters which observations are received in the first place, because external predictors and simulators evaluate the agent's *entire code*, not merely the execution branch of the code that happens to be triggered on a single run.

---

## 4. Formalization of P-FDT

We now construct a rigorous mathematical model of P-FDT. We combine Judea Pearl’s structural causal framework with logical and functional variables, augmented to handle function-valued interventions.

### 4.1 Spaces and Primitives
Let the decision environment be formalized by the following spaces:
- $\mathcal{X}$: A countable set of possible observation histories.
- $\mathcal{A}$: A finite set of possible actions.
- $\Pi \coloneqq \mathcal{A}^{\mathcal{X}}$: The policy space consisting of all mappings $\pi \colon \mathcal{X} \to \mathcal{A}$.
- $\mathcal{O}$: A countable set of physical outcomes.
- $\Util \colon \mathcal{O} \to \mathbb{R}$: A bounded utility function. Let $\VV \coloneqq \Util(\Outcome)$.

### 4.2 The Structural World-Model
An agent maintains a world-model $\model = (P, G)$, where:
1. $G = (V, E)$ is a directed acyclic graph whose vertex set $V$ includes:
   - A distinguished functional variable $\mathbf{\Pi}_{\text{agent}}$, representing the logical policy implemented by the agent. $\mathbf{\Pi}_{\text{agent}}$ takes values in $\Pi$.
   - Observation variables $\Obs \in \mathcal{X}$.
   - Physical action variables $\Act \in \mathcal{A}$.
   - Environmental state, predictor, and noise variables ($S, \Var{Prediction}, \dots$).
   - An outcome variable $\Outcome \in \mathcal{O}$, which determines utility $\VV$.
2. $P$ is a probability distribution over the exogenous variables and background states, compatible with the Markov properties of $G$.

Critically, the graph $G$ is not merely a physical causal graph; it is a **subjunctive dependency graph**. Edges in $G$ represent both physical-causal mechanisms and logical-computational determinations.

Specifically, if a predictor in the environment inspects the agent's code or runs a simulation of the agent, there is a directed edge:
\[
\mathbf{\Pi}_{\text{agent}} \longrightarrow \Var{Prediction}.
\]
Furthermore, the agent's actual physical act $\Act$ is causally determined by applying the implemented policy to the realized observation:
\[
\Act = \mathbf{\Pi}_{\text{agent}}(\Obs).
\]
In structural equation terms, the node $\Act$ has parents $\mathbf{\Pi}_{\text{agent}}$ and $\Obs$, governed by the evaluation map:
\[
f_{\Act}(\pi, \obs) \coloneqq \pi(\obs).
\]

```
              ┌──────────────────────────┐
              │   Agent Policy Type      │
              │  Π_agent ∈ A^X           │
              └─────────────┬────────────┘
                            │
             Subjunctive    │         Subjunctive
             Dependence     │         Dependence
             ┌──────────────┴──────────────┐
             ▼                             ▼
   ┌───────────────────┐         ┌───────────────────┐
   │ Predictor's Model │         │ Physical Execution│
   │    of Agent       │         │    Mechanism      │
   └─────────┬─────────┘         └─────────┬─────────┘
             │ Causal                      │
             │ Path                        │ Causal Path
             ▼                             │
       ┌───────────┐                       │
       │Box B State│                       │
       └─────┬─────┘                       │
             │                             │
             │           ┌───────┐         │
             ├──────────►│  Obs  ├─────────┤
             │           └───┬───┘         │
             │ Causal        │ Causal      │
             │ Path          ▼ Path        ▼
             │         ┌─────────────────────┐
             └────────►│   Outcome / Util    │
                       └─────────────────────┘
```

### 4.3 The P-FDT Decision Rule
In P-FDT, the agent's fundamental decision is the selection of an optimal policy $\pi^* \in \Pi$. 

How does the agent evaluate a candidate policy $\pi$? She performs a Pearlean structural intervention setting the logical variable $\mathbf{\Pi}_{\text{agent}}$ to $\pi$:
\[
\Do(\mathbf{\Pi}_{\text{agent}} = \pi).
\]
This intervention severs any prior constraints on which policy the agent was "predisposed" to run, and propagates the consequence of adopting $\pi$ forward along all outgoing edges in the subjunctive dependency graph $G$. It affects what the predictor forecasts, what the environment prepares, what observations $\Obs$ are realized, and what physical action $\Act = \pi(\Obs)$ is executed.

Formally, the expected utility of a policy $\pi \in \Pi$ evaluated under world-model $(P, G)$ is:
\[
\mathcal{EU}_{\text{P-FDT}}(\pi) \coloneqq \EE\left( \VV \;\middle|\; \Do(\mathbf{\Pi}_{\text{agent}} = \pi) \right) = \sum_{o \in \mathcal{O}} \Util(o) \, P(o \mid \Do(\mathbf{\Pi}_{\text{agent}} = \pi)).
\]

The optimal policy $\pi^*$ prescribed by P-FDT is:
\[
\pi^* \coloneqq \argmax_{\pi \in \Pi} \mathcal{EU}_{\text{P-FDT}}(\pi).
\]
*(Tie-breaking: If multiple policies maximize expected utility, any canonical deterministic tie-breaking rule may be applied.)*

### 4.4 The Execution Phase: Acting on Evidence
Now suppose the agent is currently situated in time, possesses observation history $\obs_0 \in \mathcal{X}$, and must emit a physical action. What does P-FDT prescribe?

It prescribes the evaluation of the optimal policy on the actual observation:
\[
\text{P-FDT}(P, G, \obs_0) \coloneqq \pi^*(\obs_0) = \left[ \argmax_{\pi \in \Pi} \EE\left( \VV \;\middle|\; \Do(\mathbf{\Pi}_{\text{agent}} = \pi) \right) \right](\obs_0).
\]

Notice the profound structural contrast with both CDT and standard act-FDT:
1. **CDT:** Conditions on $\obs_0$, then intervenes on $\Act$: $\argmax_{\act} \EE(\VV \mid \Do(\Act = \act), \Obs = \obs_0)$.
2. **Standard Act-FDT:** Intervenes on the observation-specialized output function node: $\argmax_{\act} \EE(\VV \mid \Do(\FDTvar(\dots, \underline{\obs_0}) = \act))$.
3. **P-FDT:** Intervenes globally on the complete policy mapping $\mathbf{\Pi}_{\text{agent}}$, identifies the optimal mapping $\pi^*$, and evaluates $\pi^*(\obs_0)$.

In P-FDT, **no conditioning on $\Obs = \obs_0$ occurs during the counterfactual optimization step**. The observation $\obs_0$ is used exclusively as an input argument to the chosen policy during the execution step.

---

## 5. Resolving Dilemmas Under P-FDT

To observe P-FDT in action, we trace its execution through classical decision-theoretic test cases.

### 5.1 Newcomb's Problem
In classic Newcomb's Problem, the agent faces Box A containing \$1,000 and Box B containing either \$1,000,000 or \$0. A 99% reliable predictor places the \$1,000,000 in Box B if and only if she predicts the agent leaves Box A behind. The box contents are sealed before the agent acts. The observation space is uninformative: $\mathcal{X} = \{\emptyset\}$. The action space is $\mathcal{A} = \{\Val{onebox}, \Val{twobox}\}$.

A policy is simply a constant map:
- $\pi_1(\emptyset) = \Val{onebox}$
- $\pi_2(\emptyset) = \Val{twobox}$

The graph $G$ contains the edges:
\[
\mathbf{\Pi}_{\text{agent}} \longrightarrow \Var{Prediction} \longrightarrow \Var{Box B} \longrightarrow \Outcome \longrightarrow \VV,
\]
and
\[
\mathbf{\Pi}_{\text{agent}} \longrightarrow \Act \longrightarrow \Outcome \longrightarrow \VV.
\]
The agent computes:
\[
\mathcal{EU}_{\text{P-FDT}}(\pi_1) = \EE(\VV \mid \Do(\mathbf{\Pi}_{\text{agent}} = \pi_1)) = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000.
\]
\[
\mathcal{EU}_{\text{P-FDT}}(\pi_2) = \EE(\VV \mid \Do(\mathbf{\Pi}_{\text{agent}} = \pi_2)) = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.
\]
Since $\mathcal{EU}(\pi_1) > \mathcal{EU}(\pi_2)$, the agent selects $\pi^* = \pi_1$. At execution:
\[
\text{P-FDT}(P, G, \emptyset) = \pi_1(\emptyset) = \Val{onebox}.
\]
P-FDT effortlessly one-boxes, securing the \$1,000,000.

### 5.2 The Smoking Lesion Problem
In the Smoking Lesion, an underlying arterial lesion causes both lung cancer (99% probability) and a preference for smoking. Smoking grants \$1,000 of utility; surviving cancer grants \$1,000,000.

In the formalization established in Section 6 of Yudkowsky & Soares (2017), whether an agent has the lesion dictates her preference structure ($\Util_S$ vs $\Util_R$). As captured in Figure 5 of the source, there is **no arrow** from the agent's logical policy node to the presence of the lesion:
\[
\Var{Lesion} \longrightarrow \Var{Cancer} \longrightarrow \Outcome.
\]
The lesion is biologically determined; it does not read the agent's source code or predict the agent's policy. 

Under P-FDT, intervening on $\Do(\mathbf{\Pi}_{\text{agent}} = \pi)$ alters $\Act$, but leaves the distribution of $\Var{Lesion}$ strictly unchanged:
\[
P(\Var{Lesion} \mid \Do(\mathbf{\Pi}_{\text{agent}} = \pi_{\text{smoke}})) = P(\Var{Lesion} \mid \Do(\mathbf{\Pi}_{\text{agent}} = \pi_{\text{refrain}})) = P(\Var{Lesion}).
\]
Because smoking yields an unconditional $+\$1,000$ across both states of health without altering the probability of cancer, P-FDT chooses:
\[
\pi^*(\emptyset) = \Val{smoke}.
\]
Thus, P-FDT smokes in the Smoking Lesion while one-boxing in Newcomb's Problem, achieving the optimal payoff combination that Gibbard and Harper (1978) claimed was structurally impossible for a single unified expected utility theory.

### 5.3 The Transparent Newcomb Problem: The True Test of P-FDT
The Transparent Newcomb Problem (Drescher 2006) exposes the decisive mathematical advantage of P-FDT over both CDT and act-based FDT.

Recall the setup: Box B is transparent. The agent directly observes whether Box B is full or empty before choosing her action. 
- Observation set: $\mathcal{X} = \{\Val{full}, \Val{empty}\}$.
- Action set: $\mathcal{A} = \{\Val{onebox}, \Val{twobox}\}$.

The policy space $\Pi = \mathcal{A}^\mathcal{X}$ contains $2^2 = 4$ policies:
1. $\pi_{11}$: $\pi(\Val{full}) = \Val{onebox},\; \pi(\Val{empty}) = \Val{onebox}$
2. $\pi_{12}$: $\pi(\Val{full}) = \Val{onebox},\; \pi(\Val{empty}) = \Val{twobox}$
3. $\pi_{21}$: $\pi(\Val{full}) = \Val{twobox},\; \pi(\Val{empty}) = \Val{onebox}$
4. $\pi_{22}$: $\pi(\Val{full}) = \Val{twobox},\; \pi(\Val{empty}) = \Val{twobox}$

The predictor sets Box B to $\Val{full}$ if and only if she predicts that the agent will take one box upon seeing both boxes full—that is, if she predicts that the agent's policy satisfies:
\[
\pi(\Val{full}) = \Val{onebox}.
\]
Notice how the dependency runs: the predictor does not merely predict an act; she inspects the agent's code to determine what the agent **would do** if she observed $\Val{full}$. The predictor's prediction determines the contents of Box B, which in turn causes the observation $\Obs$:
\[
\mathbf{\Pi}_{\text{agent}} \longrightarrow \Var{Prediction} \longrightarrow \Var{Box B} \longrightarrow \Obs \longrightarrow \Act.
\]
Let the predictor's accuracy be $0.99$. We compute the expected utility of the four policies from the P-FDT perspective:

#### Evaluating $\pi_{12}$ (One-box if full, Two-box if empty):
- Under $\Do(\mathbf{\Pi}_{\text{agent}} = \pi_{12})$, the predictor sees that $\pi_{12}(\Val{full}) = \Val{onebox}$.
- With probability $0.99$, the predictor fills Box B. Box B is full, so the agent observes $\Obs = \Val{full}$. The agent executes $\Act = \pi_{12}(\Val{full}) = \Val{onebox}$. The payoff is \$1,000,000.
- With probability $0.01$, the predictor errs and leaves Box B empty. The agent observes $\Obs = \Val{empty}$. The agent executes $\Act = \pi_{12}(\Val{empty}) = \Val{twobox}$. The payoff is \$1,000.
- Expected utility:
  \[
  \mathcal{EU}(\pi_{12}) = 0.99(\$1,000,000) + 0.01(\$1,000) = \$990,010.
  \]

#### Evaluating $\pi_{22}$ (Two-box regardless):
- Under $\Do(\mathbf{\Pi}_{\text{agent}} = \pi_{22})$, the predictor sees that $\pi_{22}(\Val{full}) = \Val{twobox}$.
- With probability $0.99$, the predictor leaves Box B empty. The agent observes $\Obs = \Val{empty}$. The agent executes $\Act = \pi_{22}(\Val{empty}) = \Val{twobox}$. The payoff is \$1,000.
- With probability $0.01$, the predictor errs and fills Box B. The agent observes $\Obs = \Val{full}$. The agent executes $\Act = \pi_{22}(\Val{full}) = \Val{twobox}$. The payoff is \$1,001,000.
- Expected utility:
  \[
  \mathcal{EU}(\pi_{22}) = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.
  \]

Clearly, $\pi_{12}$ dominates $\pi_{22}$ (and likewise dominates $\pi_{11}$ and $\pi_{21}$). P-FDT unhesitatingly selects:
\[
\pi^* = \pi_{12}.
\]

Now, place the agent in the room. She looks at the table and observes:
\[
\obs_0 = \Val{full}.
\]
What does she do? She simply queries her optimal policy:
\[
\Act = \pi^*(\Val{full}) = \pi_{12}(\Val{full}) = \Val{onebox}.
\]
The P-FDT agent leaves the transparent \$1,000 sitting on the table and takes only Box B.

#### Comparison with CDT and Act-FDT
- **CDT's Failure:** CDT conditions on $\Obs = \Val{full}$. In its causal hypothetical, $\Do(\Act = \Val{twobox})$ holding Box B full yields \$1,001,000, while $\Do(\Act = \Val{onebox})$ yields \$1,000,000. CDT takes both boxes. Predictors foresee this, leave Box B empty, and CDT agents walk away with \$1,000.
- **Act-FDT's Complexity:** In the source paper, Fiona the act-FDT agent must intervene on the node $\FDTpgv{full}$ while entertaining hypotheticals where $\Var{Prediction} = \Val{empty}$ (and therefore where $\Obs$ counterfactually would have been $\Val{empty}$, even though she observed $\Val{full}$). As the paper notes in Section 6, this requires explaining why Fiona does not condition on $\Obs = \Val{full}$ in the standard Bayesian manner.
- **P-FDT's Elegance:** P-FDT requires no strange suspension of Bayesian updating. The agent's choice was the global policy $\pi$. She counterfactually varied policies *before* binding to an observation. When she observes $\Val{full}$, she does not deliberate about her policy anew; she executes the policy she already knows to be globally optimal. 

### 5.4 Parfit's Hitchhiker
Parfit's Hitchhiker is formally isomorphic to Transparent Newcomb. The driver rescues the agent from the desert only if the driver predicts the agent will pay \$1,000 upon reaching the city. Dying in the desert costs \$1,000,000.
- $\mathcal{X} = \{\Val{city}, \Val{desert}\}$.
- $\mathcal{A} = \{\Val{pay}, \Val{refuse}\}$.

A CDT agent in the city two-boxes: the ride is in the past, so she refuses to pay, saving \$1,000. Because the driver anticipates this, the CDT agent is left to die.

A P-FDT agent evaluates policies:
\[
\pi_{\text{honorable}}(\Val{city}) = \Val{pay}, \quad \pi_{\text{selfish}}(\Val{city}) = \Val{refuse}.
\]
Under $\Do(\mathbf{\Pi}_{\text{agent}} = \pi_{\text{honorable}})$, the driver predicts payment, rescues the agent, and the agent safely reaches the city and pays \$1,000 (net utility: $-\$1,000$). Under $\Do(\mathbf{\Pi}_{\text{agent}} = \pi_{\text{selfish}})$, the driver leaves the agent to die (net utility: $-\$1,000,000$). 

P-FDT selects $\pi_{\text{honorable}}$. Arriving in the city, the agent observes $\obs_0 = \Val{city}$ and executes $\pi_{\text{honorable}}(\Val{city}) = \Val{pay}$. P-FDT pays the driver, preserving reflective consistency and surviving the desert.

---

## 6. Mathematical Open Problems and Theoretical Interpretations

While P-FDT provides an exceptionally clean normative framework, formalizing it completely uncovers several subtle mathematical and philosophical questions. Where the source text leaves these unresolved, we must distinguish between the authors' published claims and our proposed formal completions.

### 6.1 The Policy Space Explosion and Bounded Reasoners
In any realistic scenario, the observation history $\obs \in \mathcal{X}$ is rich and continuous, rendering the policy space $\Pi = \mathcal{A}^\mathcal{X}$ uncountably infinite. A real agent cannot explicitly compute $\argmax_{\pi \in \Pi} \mathcal{EU}(\pi)$ over all possible functions.

*Author's Proposal for Operationalization:* In practice, an algorithmic approximation of P-FDT must restrict search to a parameterized family of tractable computational circuits (e.g., neural networks or compact heuristics):
\[
\pi_\theta \colon \mathcal{X} \to \mathcal{A}, \quad \theta \in \Theta.
\]
The optimization becomes:
\[
\theta^* = \argmax_{\theta \in \Theta} \EE\left( \VV \;\middle|\; \Do(\mathbf{\Pi}_{\text{agent}} = \pi_\theta) \right).
\]
This transforms P-FDT into a normative model for *program synthesis* and *meta-reinforcement learning*, where the objective is to compile an agent's code to be robust against adversaries who inspect or simulate the agent's weights.

### 6.2 Counterpossibles and Consistency in the Subjunctive Graph
The most acute open problem in FDT—acknowledged candidly in Section 3 and Footnote 9 of the source—is the reliance on **counterpossible conditionals**. 

If the agent's true code implements policy $\pi^*$, then the mathematical statement $\mathbf{\Pi}_{\text{agent}} = \pi'$ for $\pi' \neq \pi^*$ is a mathematical contradiction. In standard mathematical logic, a false antecedent implies everything (the principle of explosion). What does it mean to evaluate:
\[
P\left( \Outcome \;\middle|\; \Do(\mathbf{\Pi}_{\text{agent}} = \pi') \right)
\]
when $\mathbf{\Pi}_{\text{agent}} \neq \pi'$ is logically impossible?

The authors handle this by treating the graph $G$ as an exogenous primitive containing pre-specified subjunctive edges, using Pearl's graphical do-calculus purely as a formal machinery. But this leaves open how such graphs are constructed.

*A Reasonable Operational Interpretation:* We can interpret the subjunctive graph via **program equivalence and formal verification**. Suppose an environmental predictor tests whether the agent's source code $C_{\text{agent}}$ satisfies a specification $\Phi$:
\[
\text{Predictor}(C_{\text{agent}}) = 
\begin{cases}
1 & \text{if } \text{Proof}(C_{\text{agent}} \implies \text{cooperate}) \\
0 & \text{otherwise}.
\end{cases}
\]
Here, the dependency is not an arbitrary counterpossible; it is a well-defined question of proof theory and program semantics. Evaluating $\Do(\mathbf{\Pi}_{\text{agent}} = \pi)$ corresponds to substituting an alternate subprogram $C_\pi$ into the simulation harness and computing the logical consequences within a bounded formal system (such as Peano Arithmetic or a model of probabilistic computation). Recent work in logical inductors and algorithmic probability provides a concrete mathematical substrate for maintaining consistent probability distributions over mathematical statements, pointing toward a rigorous foundation for FDT’s counterpossible surgeries.

### 6.3 Multi-Agent Game-Theoretic Collusion: The True Divergence
Footnote 7 and Footnote 16 cryptically state that the distinction between act-FDT and P-FDT "makes a difference in certain multi-agent dilemmas." The source paper leaves this difference unelaborated. We can now explain precisely why this divergence occurs.

Consider an iterated or multi-stage game with incomplete information where two agents can inspect or predict each other's policies—for instance, an **Iterated Twin Prisoner's Dilemma** or a **Commitment Game with Mutual Verification**.

Under act-FDT, at stage $t$, the agent evaluates the counterfactual output of her decision at stage $t$, holding her future self's decision functions as separate variables:
\[
\FDTvar(\underline{M}, \underline{\obs_t}) = a_t.
\]
Because act-FDT intervenes slice-by-slice, it can fall victim to dynamic inconsistencies in multi-agent bargaining. An opponent might threaten: "If your policy at round 2 does not concede, I will punish you at round 1." An act-intervening agent who has already arrived at round 2 sees round 1 as fixed history; if she treats her stage-2 function as independent of her past policy commitment, she may concede.

P-FDT eliminates this vulnerability. In P-FDT, the entity that enters the game is the global policy $\pi$. If the opponent verifies that the agent's global policy contains a punishment trigger, the opponent is deterred *at round 0*. P-FDT acts as a built-in, unshakeable precommitment device. It achieves the optimal cooperative equilibria of program games (Tennenholtz 2004) without requiring external enforcement mechanisms.

---

## 7. Comparison Summary

The following table summarizes the conceptual and mathematical mechanics of the competing decision theories:

| Dimension | Evidential Decision Theory (EDT) | Causal Decision Theory (CDT) | Act Functional Decision Theory (Act-FDT) | Policy Functional Decision Theory (P-FDT) |
| :--- | :--- | :--- | :--- | :--- |
| **Deliberative Target** | Action token $\act \in \mathcal{A}$ | Physical action token $\Act = \act$ | Observation-indexed output $\FDTvar(\dots, \obs) = \act$ | Complete policy mapping $\pi \in \mathcal{A}^{\mathcal{X}}$ |
| **Formal Operation** | Conditioning: $P(- \mid \obs, \act)$ | Physical Intervention: $\Do(\Act = \act)$ | Logical Output Intervention: $\Do(\FDTvar(\dots, \obs) = \act)$ | Global Policy Intervention: $\Do(\mathbf{\Pi}_{\text{agent}} = \pi)$ |
| **Newcomb’s Problem** | One-boxes (\$1M) | Two-boxes (\$1K) | One-boxes (\$1M) | One-boxes (\$1M) |
| **Smoking Lesion** | Refrains (Poor) | Smokes (Optimal) | Smokes (Optimal) | Smokes (Optimal) |
| **Transparent Newcomb** | Two-boxes (\$1K) | Two-boxes (\$1K) | One-boxes (\$1M) | One-boxes (\$1M) |
| **Parfit’s Hitchhiker** | Refuses (Dies) | Refuses (Dies) | Pays (Survives) | Pays (Survives) |
| **XOR Blackmail** | Pays (Exploited) | Refuses (Safe) | Refuses (Safe) | Refuses (Safe) |
| **Handling of Evidence** | Bayesian conditioning | Bayesian conditioning | Node-switching / Un-updating | Observation passed as policy argument: $\Act = \pi^*(\obs)$ |

---

## 8. Conclusion

Policy Functional Decision Theory (P-FDT) represents the culmination of the functional approach to rational agency. Where Evidential Decision Theory confuses diagnostic signs for genuine influences, and Causal Decision Theory blinds itself to the shared logical fabric that connects computational agents to their predictors, Functional Decision Theory recognizes that we are programs embedded in a physical world.

By shifting the focal point of choice from the local action token to the global mathematical policy, P-FDT achieves three major theoretical advances:
1. It unifies one-boxing in predictive problems with smoking in non-predictive common-cause dilemmas under a single, non-circular decision rule.
2. It solves sequential, transparent, and extortionary dilemmas (Transparent Newcomb, Parfit's Hitchhiker, Mechanical Blackmail) without requiring agents to awkwardly ignore their own observations or invent ad-hoc precommitment rituals.
3. It resolves the problem of counterfactual evaluation into a clean two-step architecture: global policy optimization via subjunctive graph surgery, followed by mechanical policy execution on observed inputs.

While questions surrounding the proof-theoretic foundations of counterpossibles remain an active area of research, P-FDT provides a mathematically coherent blueprint for normative rationality. In a world increasingly shaped by algorithms that model, predict, and interact with other algorithms, P-FDT demonstrates that true instrumental efficacy lies not in asking what our physical bodies should do in the moment, but in choosing the very program we wish to be.

---

### References
- Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
- Dai, W. (2009). "Towards a New Decision Theory." *LessWrong*.
- Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
- Gibbard, A., & Harper, W. L. (1978). "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, Reidel, pp. 125–162.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1979). "Prisoners' Dilemma is a Newcomb Problem." *Philosophy & Public Affairs*, 8(3), 235–240.
- Parfit, D. (1984). *Reasons and Persons*. Oxford University Press.
- Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
- Soares, N., & Fallenstein, B. (2015). "Toward Idealized Decision Theory." *arXiv:1507.01986*.
- Tennenholtz, M. (2004). "Program Equilibrium." *Games and Economic Behavior*, 49(2), 363–373.
- Yudkowsky, E. (2010). "Timeless Decision Theory." *Machine Intelligence Research Institute Technical Report*.
- Yudkowsky, E., & Soares, N. (2017). "Functional Decision Theory: A New Theory of Instrumental Rationality." *arXiv:1710.05060v2*.