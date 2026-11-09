# Policy Functional Decision Theory (P-FDT): Global Intervention, Functional Counterfactuals, and Optimal Rationality

---

### Abstract
In the foundational debate of formal decision theory, Evidential Decision Theory (EDT) and Causal Decision Theory (CDT) have long stood as the standard paradigms, each failing systematically in distinct classes of Newcomblike dilemmas. Yudkowsky and Soares introduce *Functional Decision Theory* (FDT), proposing that an agent ought to intervene on the output of a mathematical algorithm rather than on a physical action token. However, the core text of their presentation predominantly examines an *act-intervention* version of the theory. In footnote 16 (and footnote 7), the authors identify what they describe as their preferred formulation: an agent does not select an immediate physical act, but instead intervenes to select an entire **policy**—a mapping from observation histories to actions—and then executes the action dictated by that policy.

In this essay, we develop, formalize, and analyze this policy-based variant, designated **Policy Functional Decision Theory (P-FDT)**. We show how P-FDT evaluates policies globally via Pearlian-style interventions on logical types, how it computes counterfactuals across observation branches without falling into the pathologies of dynamic inconsistency or "double updating," and how it provides an elegant, unified resolution to Newcomb’s problem, Parfit’s hitchhiker, and predictive blackmail dilemmas. We also clarify open mathematical questions regarding counterpossible reasoning and the extraction of subjunctive dependence graphs.

---

## 1. Introduction: Beyond Act-Interventions and Mere Conditioning

Normative decision theory evaluates the expected consequence of choosing among alternative possibilities. Following Gibbard and Harper (1978) and Joyce (1999), expected utility can be expressed through a conditional prospect operator "$\then$":
\begin{equation}
\mathcal{EU}(a) = \sum_{j} P(a \then o_j ;\, x) \,\mathcal{U}(o_j),
\label{eq:eu_generic}
\end{equation}
where $x \in \mathcal{X}$ is the agent’s observation history, $a \in \mathcal{A}$ is an available option, $o_j \in \mathcal{O}$ are outcomes, and $\mathcal{U}: \mathcal{O} \to \mathbb{R}$ represents utility.

The fundamental cleavage in the literature concerns the semantics of the connective $a \then o$:
1. **Evidential Decision Theory (EDT)** interprets $a \then o$ via standard Bayesian conditionalization:
   \begin{equation}
   P(a \then o ;\, x) \coloneqq P(o \mid x, a).
   \end{equation}
   While EDT succeeds at securing $\$1{,}000{,}000$ in Newcomb's problem, it errs by managing symptoms rather than causes in dilemmas with confounding common causes, such as the classic Smoking Lesion Problem, and collapses entirely under extortionary structures like the XOR Blackmail (Soares and Fallenstein, 2015).
2. **Causal Decision Theory (CDT)** interprets $a \then o$ as a causal surgery on the physical act token, formalized by Pearl's (2000) $\Do$-operator:
   \begin{equation}
   P(a \then o ;\, x) \coloneqq P(o \mid \Do(\Act = a), x).
   \end{equation}
   CDT correctly identifies the lack of causal efficacy in the Smoking Lesion Problem, but fails in Newcomb's problem, the Twin Prisoner's Dilemma, and Parfit's Hitchhiker because it severs all upstream dependencies between the agent’s choice and prior predictions made by accurate external predictors.

To escape this dilemma, Yudkowsky and Soares formulate **Functional Decision Theory (FDT)**. Rather than intervening on a physical act token $\Act = a$, FDT posits that an agent is an execution instance of a fixed mathematical function. The agent's hypotheticals must respect *subjunctive dependencies*: when evaluating an alternative choice, the agent evaluates what the universe would look like if the *mathematical function itself* had evaluated to a different output.

Throughout the primary body of Yudkowsky and Soares's exposition, FDT is framed as an intervention on a function evaluated at the agent's *current observation history*:
\begin{equation}
\FDT(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left[\mathcal{V} \;\middle|\; \Do\left(\FDTvar(\underline{P}, \underline{G}, \underline{x}) = a\right)\right],
\label{eq:act_fdt}
\end{equation}
where $\mathcal{V} \coloneqq \mathcal{U}(\Outcome)$, and the underlines represent syntactic quotations of the agent’s internal model.

Yet, as the authors acknowledge in footnotes 7 and 16, this "act-intervention" formulation is a pedagogical simplification. Footnote 16 states:
> *"As mentioned earlier, the authors' preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."*

This preferred formulation is **Policy Functional Decision Theory (P-FDT)**. By lifting the intervention space from individual physical acts $\mathcal{A}$ to the space of entire decision policies $\Pi = \{ \pi : \mathcal{X} \to \mathcal{A} \}$, P-FDT provides an updateless, globally optimal foundation for instrumental rationality. 

In what follows, we develop the mathematical machinery of P-FDT, clarify how it navigates observational updating and counterfactual dependencies, work through critical applications, and systematically distinguish between the claims established in the source paper and our proposed operational completions.

---

## 2. Formalizing Policy Functional Decision Theory (P-FDT)

### 2.1 The Architecture of World-Models and Subjunctive Graphs
Let an agent be situated in an environment with:
- A countable set of observation histories $\mathcal{X}$.
- A finite set of atomic actions $\mathcal{A}$.
- A countable set of possible physical outcomes $\mathcal{O}$.
- A bounded utility function $\mathcal{U}: \mathcal{O} \to \mathbb{R}$.
- A policy space $\Pi \coloneqq \mathcal{A}^{\mathcal{X}}$, representing all deterministic mappings $\pi: \mathcal{X} \to \mathcal{A}$. (We address stochastic policies in Section 6).

An agent maintains an epistemic world-model $\mathcal{M} = (P, G)$:
- $P$ is a subjective joint probability distribution over a set of random variables. These include environmental states, past events, observations $\Obs \in \mathcal{X}$, physical acts $\Act \in \mathcal{A}$, outcomes $\Outcome \in \mathcal{O}$, and—crucially—variables representing mathematical computations.
- $G = (V, E)$ is a directed acyclic graph extending Pearl's causal Bayesian networks. Unlike classical causal graphs where edges represent physical, asymmetric transmission of energy or momentum, edges in $G$ represent **subjunctive dependence**. 

*Definition 1 (Subjunctive Dependence).* A variable $Y$ subjunctively depends on a variable $X$ if the value taken by $Y$ is determined by, or functionally constrained by, the value of $X$, such that in an evaluation of counterfactual alternatives where $X$ takes value $x'$, $Y$ varies accordingly. Causal dependence (physical causation) is a proper subset of subjunctive dependence. Mathematical and logical equivalence—such as two calculators running identical software or a predictor running an accurate simulation of an algorithm—constitute non-causal subjunctive dependencies.

In P-FDT, the core mathematical object evaluated by the universe is the agent's policy function node, denoted $\mathbf{\Pi}^*$.

### 2.2 Mathematical Definition of P-FDT
Under P-FDT, the agent does not ask: *"Given that I have observed $x$, which action $a \in \mathcal{A}$ should I execute?"* Instead, the agent asks: *"Which global policy $\pi \in \Pi$ should the decision algorithm output, such that executing $\pi(x)$ across all observation branches maximizes expected utility from the global perspective?"*

Formally, we define the P-FDT policy selection rule:

\begin{equation}
\pi^* \coloneqq \mathrm{P}\text{-}\mathrm{FDT}_{\mathrm{policy}}(P, G) \coloneqq \argmax_{\pi \in \Pi} \mathbb{E}\left[\mathcal{V} \;\middle|\; \Do\left(\mathbf{\Pi}^*(\underline{P}, \underline{G}) = \pi\right)\right],
\label{eq:pfdt_policy}
\end{equation}

where $\mathbf{\Pi}^*(\underline{P}, \underline{G})$ is the logical variable in the agent's network representing the output of her own policy-selection procedure when supplied with her model parameters.

Once the optimal policy $\pi^*$ is chosen, the agent’s executed action upon observing history $x$ is simply:
\begin{equation}
\mathrm{P}\text{-}\mathrm{FDT}(P, G, x) \coloneqq \pi^*(x).
\label{eq:pfdt_action}
\end{equation}

### 2.3 The Semantic Mechanism: Surgery on Policy Types
The operator $\Do(\mathbf{\Pi}^* = \pi)$ acts as a surgical intervention in the sense of Pearl (2000), but with two profound structural modifications:
1. **Intervention on Logical Types:** In CDT, $\Do(\Act = a)$ sets the physical variable $\Act$ to $a$ and clips all incoming edges to $\Act$. In P-FDT, the intervention targets $\mathbf{\Pi}^*$, the abstract *algorithm* or *policy type*. Any node in the universe that relies upon the calculation of this policy—whether it is the agent’s own physical motor cortex $\Act$, a predictor’s simulation running yesterday, or a psychological twin in a distant galaxy—has its value recomputed using the substituted policy $\pi$.
2. **Global Expectation (Updatelessness):** Notice that the expectation in \eqref{eq:pfdt_policy} is **not** conditioned on $\Obs = x$. The selection of $\pi^*$ is computed globally. The agent does not condition the distribution on her actual observation history before performing the policy evaluation. Rather, the observation history $x$ enters only at the terminal execution phase in \eqref{eq:pfdt_action}.

---

## 3. Comparing P-FDT with CDT, EDT, and Act-FDT

To appreciate how P-FDT functions, we must examine how it differs from rival formalisms in its treatment of information and counterfactuals.

| Decision Theory | Object of Optimization | Connective / Semantics ($a \then o$) | Treatment of Observation History $x$ |
| :--- | :--- | :--- | :--- |
| **EDT** | Act $a \in \mathcal{A}$ | Bayesian Conditioning: $P(o \mid x, a)$ | Updates beliefs via standard Bayes' Rule |
| **CDT** | Act $a \in \mathcal{A}$ | Causal Surgery: $P(o \mid \Do(\Act=a), x)$ | Updates beliefs on $x$, severs non-causal parents |
| **Act-FDT** (Eq. \ref{eq:act_fdt}) | Act $a \in \mathcal{A}$ | Functional Surgery: $P(o \mid \Do(\FDTvar(x)=a))$ | Changes the specific node of intervention to $\FDTvar(x)$ |
| **P-FDT** (Eq. \ref{eq:pfdt_policy}) | Policy $\pi \in \Pi$ | Global Policy Surgery: $P(o \mid \Do(\mathbf{\Pi}^*=\pi))$ | Updateless selection; $x$ evaluates policy at execution |

### 3.1 The Pathology of Act-Interventions in Multi-Stage Dilemmas
Why do Yudkowsky and Soares prefer P-FDT over Act-FDT? The answer lies in the problem of dynamic consistency and what footnote 16 calls the "double update" pathology of early Timeless Decision Theory (TDT; Yudkowsky, 2010).

In Act-FDT (\eqref{eq:act_fdt}), when an agent receives an observation $x$, she routes around Bayesian conditioning by shifting her point of intervention to a node specifically indexed by $x$: $\FDTvar(\underline{P}, \underline{G}, \underline{x})$. As shown in the source paper's analysis of the Transparent Newcomb Problem, when Fiona observes that Box B is full ($\Obs = \Val{full}$), she evaluates:
\begin{equation}
\argmax_{a} \mathbb{E}\left[\mathcal{V} \;\middle|\; \Do(\FDTvar(\underline{P}, \underline{G}, \Val{full}) = a), \Obs = \Val{full}\right].
\end{equation}
In doing so, Fiona must reason that if this node were to output $\Val{twobox}$, the predictor (who predicted what Fiona would do *upon seeing a full box*) would have foreseen this and therefore left Box B empty, meaning Fiona would *never have observed Box B full in the first place*. 

While this mathematically yields the correct choice in single-agent settings, it requires an unsettling conceptual gymnastics: the agent must entertain a counterfactual hypothetical where her actual observation history is contradicted by the intervention itself ("If I had two-boxed, I would not have observed what I am currently observing"). 

Under P-FDT, this tension dissolves entirely:
- The policy $\pi$ explicitly specifies what to do across *all* possible branches: $\pi(\Val{full})$ and $\pi(\Val{empty})$.
- When the agent performs $\Do(\mathbf{\Pi}^* = \pi)$, she computes the *ex-ante* or *global* expected value of adopting policy $\pi$.
- A policy that specifies $\pi(\Val{full}) = \Val{twobox}$ causes the predictor to set $\Var{Box B} = \Val{empty}$, ensuring that the $\Val{full}$ branch is never reached.
- The agent does not need to imagine "erasing" an observation she already conditioned on. The policy is selected unconditionally, and observations serve purely as computational inputs to execute the policy.

---

## 4. Applying P-FDT to Canonical Dilemmas

We now demonstrate the precision of P-FDT by applying it to the central dilemmas discussed in the source text.

### 4.1 Newcomb’s Problem
An agent faces two boxes: Box A containing $\$1{,}000$ and Box B containing either $\$1{,}000{,}000$ or $\$0$. A 99% reliable predictor fills Box B if and only if she predicted the agent leaves Box A behind.

Here, $\mathcal{X} = \{ x_0 \}$ (a trivial observation history), and $\mathcal{A} = \{ \Val{onebox}, \Val{twobox} \}$. The policy space $\Pi$ contains essentially two constant policies:
- $\pi_1(x_0) = \Val{onebox}$
- $\pi_2(x_0) = \Val{twobox}$

The graph $G$ contains the policy node $\mathbf{\Pi}^*$, which has two outgoing subjunctive edges:
1. $\mathbf{\Pi}^* \to \Act$, where $\Act = \mathbf{\Pi}^*(x_0)$.
2. $\mathbf{\Pi}^* \to \Var{Prediction}$, representing the predictor's simulation of the agent's policy algorithm.

P-FDT evaluates the two policies globally:
- **Evaluating $\pi_1$:**
  \begin{align}
  \mathbb{E}\left[\mathcal{V} \;\middle|\; \Do(\mathbf{\Pi}^* = \pi_1)\right] &= 0.99 \cdot \mathcal{U}(\$1{,}000{,}000) + 0.01 \cdot \mathcal{U}(\$0) \nonumber \\
  &= 0.99 \cdot 1{,}000{,}000 = \$990{,}000.
  \end{align}
- **Evaluating $\pi_2$:**
  \begin{align}
  \mathbb{E}\left[\mathcal{V} \;\middle|\; \Do(\mathbf{\Pi}^* = \pi_2)\right] &= 0.01 \cdot \mathcal{U}(\$1{,}001{,}000) + 0.99 \cdot \mathcal{U}(\$1{,}000) \nonumber \\
  &= 10{,}010 + 990 = \$11{,}000.
  \end{align}

P-FDT selects $\pi^* = \pi_1$, and therefore executes $\Act = \pi_1(x_0) = \Val{onebox}$. 

Unlike CDT, which severs the connection between $\Act$ and $\Var{Prediction}$ (and thus erroneously treats Box B's contents as independent of its choice), P-FDT intervenes on $\mathbf{\Pi}^*$, preserving the subjunctive link to the predictor's past prediction.

### 4.2 The Smoking Lesion Problem
Smoking is correlated with fatal lung cancer, but the correlation is driven entirely by a genetic lesion that predisposes individuals to enjoy smoking and independently causes cancer. There is no direct causal link between smoking and cancer.

In this problem, the agent's true utility function depends on whether she has the lesion: $\mathcal{U}_S$ (enjoys smoking, worth $+\$1{,}000$) or $\mathcal{U}_R$ (dislikes smoking, costing $-\$1{,}000$). Survival is worth $\$1{,}000{,}000$.

Let $\mathbf{\Pi}^*_S$ and $\mathbf{\Pi}^*_R$ denote the policy functions corresponding to these preference profiles. In the graph $G$, the lesion variable $\Var{Lesion}$ causally determines which utility function the agent possesses. Crucially, as highlighted in Figure 4 of the reference paper, **there is no directed subjunctive edge from $\mathbf{\Pi}^*$ to $\Var{Lesion}$ or $\Var{Cancer}$**. Cancer is caused biologically by the lesion, not by an algorithm running a model of the decision policy.

When P-FDT evaluates $\Do(\mathbf{\Pi}^*_S = \pi)$, the probability of the lesion remains invariant:
\begin{equation}
P(\Var{Lesion} \mid \Do(\mathbf{\Pi}^*_S = \pi_{\Val{smoke}})) = P(\Var{Lesion}) = p.
\end{equation}
Evaluating the policies under $\mathcal{U}_S$:
\begin{align}
\mathbb{E}[\mathcal{V} \mid \Do(\mathbf{\Pi}^*_S = \pi_{\Val{smoke}})] &= p(10{,}000 + 1{,}000) + (1-p)(990{,}000 + 1{,}000), \\
\mathbb{E}[\mathcal{V} \mid \Do(\mathbf{\Pi}^*_S = \pi_{\Val{refrain}})] &= p(10{,}000) + (1-p)(990{,}000).
\end{align}
The policy $\pi_{\Val{smoke}}$ dominates $\pi_{\Val{refrain}}$ by exactly $\$1{,}000$. P-FDT selects $\pi^* = \pi_{\Val{smoke}}$ and smokes.

Thus, P-FDT avoids EDT’s error of "managing the news." Because the lesion does not subjunctively depend on the algorithm $\mathbf{\Pi}^*$, intervening on $\mathbf{\Pi}^*$ does not alter the probability of cancer.

### 4.3 Parfit’s Hitchhiker and the Transparent Newcomb Problem
In Parfit’s Hitchhiker (Dilemma 4), an agent is stranded in a desert facing death (worth $-\$1{,}000{,}000$). A driver with a 99% reliable lie-detector will rescue the agent if and only if she predicts that the agent will pay her $\$1{,}000$ at an ATM upon reaching the city. Once in the city, the driver cannot enforce payment.

Let observation histories be:
- $x_{\Val{desert}}$: Being stranded in the desert.
- $x_{\Val{city}}$: Being safely in the city.

Actions at $x_{\Val{city}}$ are $\mathcal{A} = \{ \Val{pay}, \Val{refuse} \}$. Policies $\pi: \{ x_{\Val{city}} \} \to \mathcal{A}$ are:
- $\pi_{\Val{pay}}(x_{\Val{city}}) = \Val{pay}$
- $\pi_{\Val{refuse}}(x_{\Val{city}}) = \Val{refuse}$

The driver’s decision to rescue the agent subjunctively depends on a prediction of the agent’s global policy $\mathbf{\Pi}^*$.
- Under $\pi_{\Val{pay}}$, the driver predicts payment with 99% accuracy, rescues the agent, and the agent pays $\$1{,}000$:
  \begin{equation}
  \mathbb{E}[\mathcal{V} \mid \Do(\mathbf{\Pi}^* = \pi_{\Val{pay}})] = 0.99(-\$1{,}000) + 0.01(-\$1{,}000{,}000) = -\$10{,}990.
  \end{equation}
- Under $\pi_{\Val{refuse}}$, the driver predicts refusal with 99% accuracy and leaves the agent to die:
  \begin{equation}
  \mathbb{E}[\mathcal{V} \mid \Do(\mathbf{\Pi}^* = \pi_{\Val{refuse}})] = 0.01(\$0) + 0.99(-\$1{,}000{,}000) = -\$990{,}000.
  \end{equation}

P-FDT identifies $\pi^* = \pi_{\Val{pay}}$. Upon arriving in the city, the agent observes $x_{\Val{city}}$ and computes:
\begin{equation}
\Act = \pi^*(x_{\Val{city}}) = \Val{pay}.
\end{equation}

#### The Decisive Contrast with CDT and EDT
At $x_{\Val{city}}$, both CDT and EDT fail:
- **CDT** conditions on being in the city. Since the ride is already completed, paying $\$1{,}000$ has no causal power to alter whether the agent was saved. CDT refuses to pay, is predicted to refuse, and dies in the desert.
- **EDT** conditions on being in the city. Learning that one pays $\$1{,}000$ is purely bad news (a loss of $\$1{,}000$), because conditional on already being in the city, the survival news is already locked in. EDT refuses to pay and dies.

P-FDT succeeds because it is **fundamentally updateless**: the agent executes the policy that was optimal to commit to *ex-ante*. It does not re-evaluate its policy from an updated, myopic perspective that discards the subjunctive link between the driver's past behavior and the current policy.

The **Transparent Newcomb Problem** (Dilemma 5) is mathematically isomorphic:
- $\mathcal{X} = \{ \Val{full}, \Val{empty} \}$.
- The predictor fills Box B if and only if she predicts $\pi(\Val{full}) = \Val{onebox}$.
- P-FDT evaluates policies $\pi$. The policy satisfying $\pi(\Val{full}) = \Val{onebox}$ yields expected utility of $\approx \$1{,}000{,}000$. The policy satisfying $\pi(\Val{full}) = \Val{twobox}$ yields expected utility of $\approx \$1{,}000$.
- P-FDT selects the policy that one-boxes on $\Val{full}$. Upon seeing two full boxes, the agent executes $\pi^*(\Val{full}) = \Val{onebox}$.

### 4.4 The Mechanical Blackmail
In Dilemma 8, an infallible blackmailer runs an automated program that publicly leaks devastating information (costing $\$1{,}000{,}000$) unless the agent pays $\$1{,}000$ within 24 hours. Crucially, the blackmailer *only initiates the program* if she reliably predicts that the agent will pay upon receiving the letter. The agent receives the letter ($\Obs = \Val{letter}$). Should she pay?

Let the policies be:
- $\pi_{\Val{compliant}}(\Val{letter}) = \Val{pay}$
- $\pi_{\Val{resistant}}(\Val{letter}) = \Val{refuse}$

The blackmailer's program initiation node $\Var{Initiate}$ subjunctively depends on $\mathbf{\Pi}^*$:
\begin{equation}
\Var{Initiate} = 1 \iff \mathbf{\Pi}^*(\Val{letter}) = \Val{pay}.
\end{equation}
Evaluating under P-FDT:
- Under $\Do(\mathbf{\Pi}^* = \pi_{\Val{compliant}})$, the blackmailer initiates the program. The agent receives the letter and pays $\$1{,}000$:
  \begin{equation}
  \mathbb{E}[\mathcal{V} \mid \Do(\mathbf{\Pi}^* = \pi_{\Val{compliant}})] = -\$1{,}000.
  \end{equation}
- Under $\Do(\mathbf{\Pi}^* = \pi_{\Val{resistant}})$, the blackmailer predicts refusal, and therefore *never initiates the program*:
  \begin{equation}
  \mathbb{E}[\mathcal{V} \mid \Do(\mathbf{\Pi}^* = \pi_{\Val{resistant}})] = \$0.
  \end{equation}

P-FDT maximizes global utility by choosing $\pi^* = \pi_{\Val{resistant}}$. 

When the agent finds herself holding the letter, what does she do? She executes $\pi^*(\Val{letter}) = \Val{refuse}$. 
Because $\pi^*$ is known to be resistant, an accurate blackmailer never sends the letter in the first place! If an imperfect blackmailer sends the letter by error (with probability $\epsilon$), P-FDT continues to refuse as long as the ex-ante risk of being targeted by blackmailers outweighs the cost of swallowing the threat (as analyzed in Section 9 of the source paper).

---

## 5. Resolving Open Ambiguities: What Footnote 16 Leaves Unsaid

While Footnote 16 specifies that P-FDT intervenes to choose a policy rather than an action, it leaves several foundational mathematical details unspecified. We now formalize and propose explicit resolutions to these open questions, distinguishing between the source text's assertions and our operational developments.

### 5.1 The Logical Prior and Counterpossible Reasoning
A foundational critique of FDT is that it requires evaluating counterfactuals whose antecedents are mathematically impossible. If $\mathbf{\Pi}^*(\underline{P}, \underline{G}) = \pi^*$, then the antecedent $\mathbf{\Pi}^*(\underline{P}, \underline{G}) = \pi'$ for $\pi' \neq \pi^*$ is an arithmetical contradiction. In classical logic, a contradiction implies any proposition (principle of explosion), rendering probabilities conditioned on contradictions mathematically undefined.

#### The Source's Position
The source text acknowledges this challenge (Section 3 and Footnote 9). It proposes that the difficulty is technical rather than philosophical, pointing to human mathematical reasoning under logical uncertainty and citing work on logical probability (e.g., Gaifman, 2004; Demski, 2012; Garrabrant et al., 2016).

#### Our Operational Interpretation: The Structural Pearlian Extension
To make P-FDT mathematically rigorous without waiting for a completed theory of counterpossible conditionals, we interpret the subjunctive model $(P, G)$ as an **Abstract Functional Structural Causal Model (F-SCM)**.

*Definition 2 (Functional Structural Causal Model).* An F-SCM is a tuple $\mathcal{M} = (\mathbf{U}, \mathbf{V}, \mathbf{F}, P(\mathbf{U}))$, where:
- $\mathbf{U}$ is a set of exogenous variables distributed according to $P(\mathbf{U})$.
- $\mathbf{V}$ is a set of endogenous variables, containing physical states and a distinguished logical node $\mathbf{\Pi}^*$.
- $\mathbf{F} = \{ f_Y \mid Y \in \mathbf{V} \}$ is a set of deterministic structural equations:
  \begin{equation}
  Y \coloneqq f_Y(\mathbf{Pa}_Y, \mathbf{U}_Y),
  \end{equation}
  where $\mathbf{Pa}_Y \subseteq \mathbf{V} \setminus \{ Y \}$.
- For the distinguished policy node $\mathbf{\Pi}^*$, its natural structural equation is its algorithmic specification:
  \begin{equation}
  \mathbf{\Pi}^* \coloneqq \mathrm{SolvePolicy}(\underline{\mathcal{M}}).
  \end{equation}

In this framework, the intervention $\Do(\mathbf{\Pi}^* = \pi)$ is **not** a conditionalization on a logical contradiction. Rather, it is an algebraic substitution:
1. Replace the equation $\mathbf{\Pi}^* \coloneqq \mathrm{SolvePolicy}(\underline{\mathcal{M}})$ with the constant assignment $\mathbf{\Pi}^* \coloneqq \pi$.
2. For every child variable $Z \in \mathbf{Ch}(\mathbf{\Pi}^*)$, compute its value by propagating $\pi$ through the structural function $f_Z$.
3. Compute expected utility by integrating over the exogenous background distribution $P(\mathbf{U})$:
   \begin{equation}
   \mathbb{E}\left[\mathcal{V} \;\middle|\; \Do(\mathbf{\Pi}^* = \pi)\right] = \int_{\mathbf{U}} \mathcal{U}\left(\Outcome^{\mathbf{\Pi}^* \leftarrow \pi}(\mathbf{u})\right) dP(\mathbf{u}).
   \label{eq:fscm_integral}
   \end{equation}

By decoupling the *operational semantics of graph surgery* from the *proof-theoretic semantics of arithmetical truth*, the F-SCM framework renders P-FDT mathematically well-defined on any well-formed subjunctive graph.

### 5.2 The Problem of the Initial Epistemic Graph
Where does the subjunctive graph $G$ come from? In CDT, Pearl (2000) provides constraint-based and score-based algorithms for learning causal DAGs from observation and conditional independence tests (e.g., the PC algorithm). 

For P-FDT, the source text notes in Section 5:
> *"Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."*

#### Proposed Operational Graph Induction
We propose that subjunctive edges originating from an algorithmic node $\mathbf{\Pi}^*$ can be formally induced via **program analysis and informational compression**:
1. **Simulation Invariance:** A physical node $Y$ in the environment subjunctively depends on $\mathbf{\Pi}^*$ if the optimal algorithmic compression of the history leading to $Y$ contains an explicit simulation or model of $\mathbf{\Pi}^*$. 
2. **Algorithmic Mutual Information:** In the sense of Kolmogorov complexity, if $K(Y \mid \mathbf{\Pi}^*) \ll K(Y)$, and this Kolmogorov overlap cannot be accounted for by spatio-temporal causal paths from the agent's motor outputs, a subjunctive parent link $\mathbf{\Pi}^* \to Y$ is inscribed.

This distinguishes predictors from lesions: an accurate predictor's neural network contains mutual algorithmic information with the agent's code; a carcinogenic lesion does not compute or simulate the agent's decision code.

---

## 6. Mathematical Example: P-FDT Under Information Asymmetry

To illustrate the concrete application of P-FDT to an unfamiliar, complex problem involving multi-stage observations and counterfactual tradeoffs, consider the following original dilemma:

### The Asymmetric Oracle Dilemma
An agent faces two possible economic environments:
- **State $S_1$ (Boom):** Prior probability $P(S_1) = 0.8$.
- **State $S_2$ (Bust):** Prior probability $P(S_2) = 0.2$.

Before the agent acts, an accurate predictor (Oracle) inspects the agent’s code and issues an investment grant if and only if she predicts that the agent’s global policy $\pi$ satisfies:
\begin{equation}
\pi(x_2) = \Val{Cautious},
\end{equation}
where $x_2$ is the observation history corresponding to learning that the state is $S_2$. The Oracle's grant is worth $\$200{,}000$, awarded *prior* to the agent learning the state.

When the state is revealed, the agent observes $x \in \{ x_1, x_2 \}$ and must select an action:
- In state $S_1$ ($x_1$): 
  - $\Val{Invest}$: yields $\$100{,}000$.
  - $\Val{Cautious}$: yields $\$0$.
- In state $S_2$ ($x_2$):
  - $\Val{Invest}$: yields a loss of $-\$500{,}000$ (catastrophic failure).
  - $\Val{Cautious}$: yields $\$0$.

Now suppose an adversarial variation: the Oracle demands that in exchange for the $\$200{,}000$ upfront grant, the agent must commit to a policy that chooses $\Val{Invest}$ in state $S_2$ with probability 0.1, or choose a sub-optimal action in state $S_1$: $\pi(x_1) = \Val{Cautious}$.

Specifically, let the agent evaluate four deterministic policies $\Pi = \{ \pi_1, \pi_2, \pi_3, \pi_4 \}$:
- $\pi_1 = \{ x_1 \mapsto \Val{Invest}, \; x_2 \mapsto \Val{Cautious} \}$
- $\pi_2 = \{ x_1 \mapsto \Val{Invest}, \; x_2 \mapsto \Val{Invest} \}$
- $\pi_3 = \{ x_1 \mapsto \Val{Cautious}, \; x_2 \mapsto \Val{Cautious} \}$
- $\pi_4 = \{ x_1 \mapsto \Val{Cautious}, \; x_2 \mapsto \Val{Invest} \}$

The Oracle awards the $\$200{,}000$ grant if and only if $\mathbf{\Pi}^*(x_1) = \Val{Cautious}$ (demanding sub-optimality in the common state).

#### P-FDT Evaluation:
The agent evaluates the global expected utility of each policy via \eqref{eq:pfdt_policy}:
\begin{equation}
\mathbb{E}[\mathcal{V} \mid \Do(\mathbf{\Pi}^* = \pi)] = \mathbb{E}[\Var{Grant} \mid \Do(\mathbf{\Pi}^* = \pi)] + \sum_{i \in \{1, 2\}} P(S_i) \cdot \mathcal{U}(\Outcome(S_i, \pi(x_i))).
\end{equation}

1. **For $\pi_1$ (Standard rational choice on both branches):**
   - The Oracle sees $\pi_1(x_1) = \Val{Invest} \neq \Val{Cautious}$, so $\Var{Grant} = \$0$.
   - Yield:
     \begin{equation}
     \mathbb{E}[\mathcal{V} \mid \Do(\mathbf{\Pi}^* = \pi_1)] = \$0 + 0.8(\$100{,}000) + 0.2(\$0) = \$80{,}000.
     \end{equation}
2. **For $\pi_3$ (Complying with the Oracle’s demand):**
   - The Oracle sees $\pi_3(x_1) = \Val{Cautious}$, so $\Var{Grant} = \$200{,}000$.
   - Yield:
     \begin{equation}
     \mathbb{E}[\mathcal{V} \mid \Do(\mathbf{\Pi}^* = \pi_3)] = \$200{,}000 + 0.8(\$0) + 0.2(\$0) = \$200{,}000.
     \end{equation}
3. **For $\pi_2$ and $\pi_4$:** Both induce catastrophic risk in $S_2$ ($-\$500{,}000$) and are strictly dominated.

P-FDT selects policy $\pi^* = \pi_3$. 

#### Execution Behavior:
- When the state is revealed to be $S_1$, the agent observes $x_1$. 
- A myopic CDT or EDT agent at $x_1$ would argue: *"We are already in $S_1$! The Oracle has already paid the grant or not! Taking $\Val{Invest}$ gives a free extra $\$100{,}000$!"*
- A P-FDT agent does not perform this calculation. She looks up the executed policy:
  \begin{equation}
  \Act = \pi^*(x_1) = \Val{Cautious}.
  \end{equation}
She leaves the $\$100{,}000$ on the table. Why? Because the Oracle predicted that she is the *kind of agent whose global policy selects $\Val{Cautious}$ at $x_1$*, and that predictability earned her the $\$200{,}000$ upfront grant. On net, she walks away with $\$200{,}000$, whereas a CDT agent walks away with only $\$80{,}000$.

---

## 7. Philosophical Implications: Rationality and Reflective Stability

The architectural choice of P-FDT illuminates profound philosophical questions regarding the nature of agency and instrumental rationality.

### 7.1 The Global Perspective and Updatelessness
Standard decision theories are *update-centric*: an agent begins with a prior, conditions on sensory evidence, and then decides what physical act token to execute. P-FDT flips this priority: **the fundamental unit of rational agency is the global policy.** 

As Yudkowsky and Soares argue in Section 9, an agent should adopt a "global perspective":
> *"FDT’s prescription is that an agent should choose her action from a global perspective—asking herself 'What would the entire universe look like if the FDT algorithm behaved differently?' and choosing the action that corresponds to the best imagined universe."*

In P-FDT, this global perspective is instantiated literally by optimizing over the entire mapping $\pi \in \mathcal{A}^{\mathcal{X}}$. Observations do not serve to alter the agent's normative criteria mid-stream; observations are simply the physical switches that route the execution of the globally optimal program.

### 7.2 Reflective Stability and Precommitment
A decision theory is **reflectively stable** if an agent following that theory would not choose to self-modify into an agent following a different decision theory if given the opportunity (Arntzenius, 2008).
- **CDT is reflectively unstable:** A CDT agent in Newcomb's problem or Parfit's hitchhiker wishes she could bind herself beforehand to follow a different theory. If given access to a code-editor prior to the encounter, she would self-modify to become an FDT agent, but if handed the code-editor during the encounter, she would tear out the commitment.
- **P-FDT is reflectively stable:** Because P-FDT chooses the global policy $\pi^*$ that maximizes expected utility across all branches, there is no possible precommitment that achieves higher expected utility than $\pi^*$ itself. P-FDT agents naturally emulate the behavior of an ideally precommitted agent without requiring binding hardware, legal contracts, or neurological surgery.

---

## 8. Conclusion

Policy Functional Decision Theory (P-FDT) represents the complete, mature formalization of functional rationality prefigured in footnote 16 of Yudkowsky and Soares (2017). By transitioning from *act-interventions* to *policy-interventions*, P-FDT resolves the longstanding antinomies between Evidential and Causal Decision Theory.

Where EDT erroneously respects merely statistical correlations, P-FDT relies on surgical graph interventions that preserve only true subjunctive dependencies. Where CDT erroneously clips logical and computational dependencies between identical algorithms and predictors, P-FDT intervenes on the mathematical policy type itself. And where Act-FDT must resort to counter-observational gymnastics to evaluate choices after the fact, P-FDT selects the optimal global policy updatelessly, treating observations purely as inputs to execute a globally coherent strategy.

The result is a unified, reflectively stable, and mathematically formidable account of instrumental rationality—one capable of guiding both human philosophical inquiry and the algorithmic design of cooperative, unexploitable artificial intelligence.

---

## References

- Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
- Arntzenius, F. (2008). No Regrets, or: Edith Piaf Revamps Decision Theory. *Erkenntnis*, 68(2), 277–297.
- Demski, A. (2012). Logical Prior Probability. *Artificial General Intelligence (AGI 2012)*, LNCS 7716, 50–59. Springer.
- Gaifman, H. (2004). Reasoning with Limited Resources and Assigning Probabilities to Arithmetical Statements. *Synthese*, 140(1–2), 97–119.
- Garrabrant, S., Benson-Tilsen, T., Critch, A., Soares, N., & Taylor, J. (2016). Logical Induction. *arXiv preprint arXiv:1609.03543*.
- Gibbard, A., & Harper, W. L. (1978). Counterfactuals and Two Kinds of Expected Utility. In C. A. Hooker, J. J. Leach, & E. F. McClennen (Eds.), *Foundations and Applications of Decision Theory* (pp. 125–162). D. Reidel.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1979). Prisoners' Dilemma is a Newcomb Problem. *Philosophy & Public Affairs*, 8(3), 235–240.
- Lewis, D. (1981). Causal Decision Theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
- Nozick, R. (1969). Newcomb's Problem and Two Principles of Choice. In N. Rescher (Ed.), *Essays in Honor of Carl G. Hempel* (pp. 114–146). D. Reidel.
- Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
- Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
- Skyrms, B. (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
- Soares, N., & Fallenstein, B. (2015). Toward Idealized Decision Theory. *arXiv preprint arXiv:1507.01986*.
- Spohn, W. (1977). Where Luce and Krantz do really generalize Savage's decision model. *Erkenntnis*, 11(1), 113–134.
- Yudkowsky, E. (2010). *Timeless Decision Theory*. Machine Intelligence Research Institute Technical Report.
- Yudkowsky, E., & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. *arXiv preprint arXiv:1710.05060v2*.