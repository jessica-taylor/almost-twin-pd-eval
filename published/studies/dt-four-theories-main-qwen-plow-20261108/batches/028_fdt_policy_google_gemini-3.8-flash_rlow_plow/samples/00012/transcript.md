# 028_fdt_policy_google_gemini-3.8-flash_rlow_plow / 00012

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/eada7fdd-162b-4da9-9e87-39be7a379ab2/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/eada7fdd-162b-4da9-9e87-39be7a379ab2/call_0/response.raw) · finish: `stop`

### Visible response

````text
# From Act-Intervention to Policy-Selection: A Mathematical Account of Policy Functional Decision Theory (P-FDT)

## 1. Introduction: The Dialectic of Decision

In standard expected utility theory, rational deliberation is formalized as the selection of an act $a \in \mathcal{A}$ maximizing expected utility with respect to some conditional probability connective $\hookrightarrow$:
\begin{equation}
\mathcal{EU}(a) = \sum_{j} P(a \hookrightarrow o_j \;;\, x) \mathcal{U}(o_j),
\end{equation}
where $\mathcal{U}$ is a von Neumann–Morgenstern utility function, $\mathcal{O} = \{o_j\}$ is the outcome space, and $x \in \mathcal{X}$ is the agent's observation history. Following Joyce (1999), decision theories do not primarily disagree on the axioms of cardinal evaluation, but rather on the epistemic and modal interpretation of the hypothetical conditional $a \hookrightarrow o_j$.

- **Evidential Decision Theory (EDT)** identifies hypotheticals with Bayesian posterior conditioning:
  \begin{equation}
  P_{\mathrm{EDT}}(a \hookrightarrow o_j \;;\, x) \coloneqq P(o_j \mid x, a).
  \end{equation}
  EDT prescribes selecting the act that would be the best news to hear that one performed. While this yields optimal payoffs in asymmetric coordination dilemmas such as the Psychological Twin Prisoner's Dilemma and Newcomb's Problem, it notoriously fails in common-cause settings like the Smoking Lesion Problem (Gibbard & Harper, 1978) or adversarial epistemic setups like the XOR Blackmail (Soares & Fallenstein, 2015), where it irrationally attempts to "manage the news."

- **Causal Decision Theory (CDT)** remedies this by interpreting hypotheticals via localized physical interventions, formalizable via Pearl's (2000) $\Do$-calculus:
  \begin{equation}
  P_{\mathrm{CDT}}(a \hookrightarrow o_j \;;\, x) \coloneqq P(o_j \mid \Do(\mathrm{Act}=a), \mathrm{Obs}=x).
  \end{equation}
  CDT models action as an intervention that severs all incoming causal edges to the physical act variable $\mathrm{Act}$, thereby ignoring upstream correlations. While this successfully prescribes smoking in the Smoking Lesion Problem, it causes the agent to two-box in Newcomb's Problem, defect against psychological twins, succumb to extortion in the Mechanical Blackmail, and walk to certain death in Damascus (Gibbard & Harper, 1978).

In their foundational paper *Functional Decision Theory: A New Theory of Instrumental Rationality*, Eliezer Yudkowsky and Nate Soares introduce **Functional Decision Theory (FDT)**. FDT diagnoses the failure modes of both predecessors: EDT preserves too many correlations (including spurious, non-decision-relevant correlations), while CDT breaks too many (severing logical and computational ties between the agent's cognition and predictors modeling that cognition).

In the body of their paper, Yudkowsky and Soares formulate FDT as an intervention upon a logical variable representing the output of the agent's decision algorithm for a given observation history:
\begin{equation}
\FDT(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left[ V \;\middle|\; \Do(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a) \right].
\end{equation}
However, in footnote 16 (previewed in footnote 7), the authors make a crucial qualification:
> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions... As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action."

We designate this preferred formulation **Policy Functional Decision Theory (P-FDT)**. 

While Yudkowsky and Soares sideline the policy-selection apparatus in their main text for ease of exposition, shifting from act-level intervention to policy-level functional intervention is far from a cosmetic adjustment. It fundamentally alters how counterfactual conditionals are evaluated across distinct informational sets, eliminates internal dynamic inconsistency without requiring exogenous precommitments, and provides an elegant, unified resolution to Newcomblike dilemmas, extensive-form games, and multi-agent coordination problems.

This essay provides a rigorous, self-contained mathematical formalization of **P-FDT**. We define its ontology, construct its graphical and probabilistic machinery, detail its operational calculus, demonstrate its performance across canonical benchmark problems, and address the open foundational questions surrounding counterpossible reasoning and policy spaces.

---

## 2. Foundations and Ontology of P-FDT

### 2.1 Subjunctive Dependence vs. Causal Dependence
Standard causal graphs represent physical systems where directed edges encode token-causal mechanisms governed by physical law. P-FDT operates on an expanded dependency structure that incorporates **subjunctive dependence**.

Two physical or cognitive processes subjunctively depend on an abstract mathematical object $\mathcal{F}$ if their operational realizations are constrained by the mathematical identity of $\mathcal{F}$. Consider two calculators situated on opposite sides of the globe, each computing $6288 + 1048$. There is no physical signal passing between them, nor must there be a proximal common physical cause for their synchronization. Rather, both physical devices instantiate the same arithmetical addition function $+: \mathbb{N} \times \mathbb{N} \to \mathbb{N}$. Insofar as neither calculator malfunctions, their outputs are logically constrained to be identical.

Similarly, when an agent deliberates and an external predictor simulates or models that agent's deliberation, both the agent's physical motor execution and the predictor's forecast subjunctively depend on the mathematical mapping being executed. In Charles Sanders Peirce's terminology, CDT intervenes upon the *token* (the agent's localized physical act $\mathrm{Act}$), whereas P-FDT intervenes upon the *type* (the abstract decision mapping $\pi$).

### 2.2 Formalizing the Policy Space
Let:
- $\mathcal{X}$ be a countable set of possible observation histories (information states).
- $\mathcal{A}$ be a finite set of primitive actions available to the agent.
- $\Pi \coloneqq \{ \pi : \mathcal{X} \to \mathcal{A} \}$ be the space of deterministic decision policies (extensions to stochastic behavioral policies $\Delta(\mathcal{A})^\mathcal{X}$ will be treated subsequently).

In standard game theory and reinforcement learning, an agent facing an extensive-form interaction selects an action dynamically at each information set $x \in \mathcal{X}$, or selects an ex-ante policy before observing $x$. In **P-FDT**, the agent finds herself at an information set $x$, but her deliberation does *not* ask:
$$\text{"What act } a \in \mathcal{A} \text{ should I execute now?"}$$
Nor does it ask:
$$\text{"What act } a \text{ would make me happiest to observe?"}$$
Instead, a P-FDT agent asks:
$$\text{"Which mathematical policy } \pi \in \Pi \text{ is such that this very decision procedure selecting } \pi \text{ yields the highest expected global utility?"}$$

Once the optimal policy $\pi^*$ is identified, the physical act executed in the world is simply the evaluation of that policy on the current observation:
\begin{equation}
a = \pi^*(x).
\end{equation}

---

## 3. Mathematical Formulation of P-FDT

### 3.1 The Augmented Subjunctive Graph
To operationalize P-FDT, we augment the agent's probabilistic belief state $P$ with an extended directed acyclic graph $G = (\mathcal{V}, \mathcal{E})$, where vertices $\mathcal{V}$ represent physical and logical variables, and directed edges $\mathcal{E}$ encode both causal and subjunctive dependencies.

The vertex set $\mathcal{V}$ contains:
1. An unconditioned, global functional node $\mathbf{\Pi}^*$, representing the logical output of the agent's policy-selection algorithm given the global specification of the decision problem:
   \begin{equation}
   \mathbf{\Pi}^* \sim \mathtt{p\_fdt}(\underline{P}, \underline{G}),
   \end{equation}
   where underlined terms denote the quoted, reified syntactic representations of the agent's own model and graph (justified formally via Kleene's second recursion theorem; Kleene, 1938).
2. The observation history variable $\mathrm{Obs} \in \mathcal{X}$.
3. The physical action variable $\mathrm{Act} \in \mathcal{A}$, which is a deterministic child of both $\mathbf{\Pi}^*$ and $\mathrm{Obs}$:
   \begin{equation}
   \mathrm{Act} \coloneqq \mathbf{\Pi}^*(\mathrm{Obs}).
   \end{equation}
4. External environment variables (e.g., predictors, physical systems, twins), which may possess incoming edges from $\mathbf{\Pi}^*$ reflecting subjunctive dependencies.
5. A scalar or real-valued utility variable $V \coloneqq \mathcal{U}(\mathrm{Outcome})$.

Crucially, in the standard FDT act-intervention graph (Yudkowsky & Soares, Section 5), there are multiple distinct algorithm nodes $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ for each possible observation $x$, and the agent reacts to an observation $x$ by shifting the target of intervention from one node to another. 

In **P-FDT**, by contrast, there is a **single, unified logical variable** $\mathbf{\Pi}^*$ upon which intervention takes place. The agent does not switch intervention nodes upon observing $x$; the object of counterfactual evaluation is globally the policy $\pi \in \Pi$.

### 3.2 The Policy Optimization Rule
Let $(P, G)$ be the agent's subjunctive world model. When an agent running P-FDT faces a decision with current observation history $x \in \mathcal{X}$, how should she evaluate alternative policies $\pi \in \Pi$?

Here, we must address an important ambiguity left open in footnote 16. Footnote 16 specifies that P-FDT intervenes on the function to select a policy mapping inputs to actions, but leaves two possible operational interpretations for how the current observation $x$ enters the expected utility calculation:

1. **The Ex-Post Evaluated Policy Rule ($\text{P-FDT}_{\text{post}}$):**
   The agent conditions on her actual observation history $\mathrm{Obs} = x$ while intervening on the policy node:
   \begin{equation}
   \pi^* = \argmax_{\pi \in \Pi} \mathbb{E}\left[ V \;\middle|\; \Do(\mathbf{\Pi}^* = \pi), \mathrm{Obs} = x \right].
   \end{equation}
2. **The Global / Updateless Policy Rule ($\text{P-FDT}_{\text{global}}$):**
   The agent evaluates candidate policies from the ex-ante (or global) epistemic perspective, integrating over all observation states that the policy might encounter, *without* conditioning the intervention background on $\mathrm{Obs} = x$:
   \begin{equation}
   \pi^* = \argmax_{\pi \in \Pi} \mathbb{E}\left[ V \;\middle|\; \Do(\mathbf{\Pi}^* = \pi) \right].
   \end{equation}

#### Analytical Distinction and Justification
The source document establishes that FDT agents act as they "would have ideally precommitted to act" and emphasizes that FDT agents achieve reflective consistency without being vulnerable to informational extortion. In dilemmas such as the Transparent Newcomb Problem and the Mechanical Blackmail, an agent who conditions on having already observed the anomalous or threatening state ($\mathrm{Obs} = \text{full}$ or $\mathrm{Obs} = \text{letter}$) before evaluating counterfactuals risks re-introducing the very distortions FDT is designed to bypass.

Specifically, in Section 9, Yudkowsky and Soares observe that when Fiona (the FDT agent) imagines refusing to pay blackmail, she imagines a world where she was never blackmailed in the first place—that is, the policy intervention counterfactually modifies the probability distribution over $\mathrm{Obs}$ itself. 

If an agent conditions on $\mathrm{Obs} = x$ *prior* to or *alongside* the intervention $\Do(\mathbf{\Pi}^* = \pi)$, she constrains the hypothetical space to worlds where $\mathrm{Obs} = x$ obtained, severing the subjunctive link between the policy choice and whether that observation occurs! 

Therefore, our mathematical account adopts **Interpretation 2 ($\text{P-FDT}_{\text{global}}$)** as the canonical, fully realized form of Policy Functional Decision Theory:
\begin{equation}
\label{eq:pfdt-core}
\mathbf{P\text{-}FDT}(P, G, x) \coloneqq \pi^*(x), \quad \text{where} \quad \pi^* = \argmax_{\pi \in \Pi} \mathbb{E}\left[ V \;\middle|\; \Do(\mathbf{\Pi}^* = \pi) \right].
\end{equation}
If there exists a non-singleton set of maximizing policies $\Pi^* \subseteq \Pi$, a canonical tie-breaking rule (e.g., lexicographic ordering over encodings of $\pi$) is applied.

Once the optimal policy $\pi^*$ is derived from the global perspective, the agent executes the specific action $a = \pi^*(x)$ indicated by her current observation $x$. This formalizes the core insight: **Deliberation is the identification of the optimal general mapping; action is merely the evaluation of that mapping at the current coordinate.**

---

## 4. How P-FDT Treats Dependencies and Counterfactuals

To understand why P-FDT succeeds where CDT and EDT fail, we must dissect the formal surgery performed by the operator $\Do(\mathbf{\Pi}^* = \pi)$ within the graph $G$.

```
       [ Decision Function \mathbf{\Pi}^* ]
             /                    \
  (subjunctive)                  (subjunctive)
           v                              v
[ Predictor / Twin ]              [ Physical Action ] <--- [ Observation ]
           \                              /                      ^
            v                            v                       |
             ------> [ Outcome ] <-------                        |
                         |                                       |
                         v                                       |
                    [ Utility V ]                                |
                         ^                                       |
                         |---------------------------------------|
```

### 4.1 Causal vs. Subjunctive Separation
In Pearl's causal graphical models, an intervention $\Do(\mathrm{Act} = a)$ replaces the structural equation for $\mathrm{Act}$ with a constant value $a$, severing all incoming edges to $\mathrm{Act}$. Any variable that was an ancestor of $\mathrm{Act}$ (or correlated with $\mathrm{Act}$ via an unblocked backdoor path) remains completely unaltered.

In **P-FDT**, the surgery is elevated to the type-level node $\mathbf{\Pi}^*$:
1. The intervention sets $\mathbf{\Pi}^* = \pi$.
2. All directed edges descending from $\mathbf{\Pi}^*$ propagate the consequences of adopting policy $\pi$.
3. Descendants of $\mathbf{\Pi}^*$ include:
   - The agent's physical motor act $\mathrm{Act} = \pi(\mathrm{Obs})$.
   - Any external system that contains an accurate model, simulation, or representation of the agent's decision logic (e.g., Newcomb's predictor, an extortionist, an opponent running the same algorithm).
   - The observation variable $\mathrm{Obs}$ itself, whenever the environment's disposition to present observations depends upon predictions of the agent's policy!

### 4.2 The Nature of Subjunctive Counterfactuals
A common philosophical critique of FDT is that it relies on *counterpossible conditionals*—evaluating what the world would look like if a mathematical algorithm produced an output different from its true logical output. 

P-FDT frames this issue cleanly. The agent does not pretend that logic itself is inconsistent; rather, she uses an augmented structural model $(P, G)$ where the node $\mathbf{\Pi}^*$ is treated as an input variable for the purposes of comparative evaluation across hypothetical design specifications. 

The conditional probability under the hypothetical policy $\pi$ is computed via structural graph surgery:
\begin{equation}
P(o \mid \Do(\mathbf{\Pi}^* = \pi)) = \sum_{x \in \mathcal{X}} P(\mathrm{Obs} = x \mid \Do(\mathbf{\Pi}^* = \pi)) P(o \mid \mathrm{Act} = \pi(x), \mathrm{Obs} = x, \Do(\mathbf{\Pi}^* = \pi)).
\end{equation}
This highlights why P-FDT does not "manage the news" in the pathological sense of EDT. In the Smoking Lesion Problem, the arterial lesion is a physical common cause; it does not simulate the agent's policy $\mathbf{\Pi}^*$. Thus, in Fiona's graph, there is no directed edge from $\mathbf{\Pi}^*$ to $\mathrm{Lesion}$. Intervening on $\mathbf{\Pi}^*$ leaves the probability of the lesion invariant:
\begin{equation}
P(\mathrm{Lesion} \mid \Do(\mathbf{\Pi}^* = \pi)) = P(\mathrm{Lesion}).
\end{equation}
Consequently, P-FDT agents smoke, achieving high utility without fallaciously attempting to undo an unalterable biological state.

---

## 5. Canonical Applications and Comparative Mechanics

We now demonstrate the operational calculus of P-FDT across four canonical decision problems that delineate the boundaries between EDT, CDT, standard FDT, and P-FDT.

### 5.1 Parfit's Hitchhiker
Recall Derek Parfit’s (1986) formulation:
An agent is stranded in a desert, facing certain death ($-\$1{,}000{,}000$). A driver appears who will transport the agent to the city if and only if she predicts that, upon arrival in the city, the agent will withdraw and pay $\$1{,}000$ to the driver. The driver has a 99% accurate lie-detection/predictive capacity. Once in the city, there is no legal or physical enforcement mechanism: the agent can either pay ($a = \mathrm{pay}$) or refuse ($a = \mathrm{refuse}$).

Let the information states be:
- $x_0$: Stranded in desert (initial).
- $x_1$: Safely in the city at the ATM.
- $x_2$: Left to die in the desert.

The actions available at $x_1$ are $\mathcal{A} = \{\mathrm{pay}, \mathrm{refuse}\}$. 
The policy space mapping observations to actions consists of two relevant policies:
- $\pi_{\mathrm{honest}}$: Set $\pi(x_1) = \mathrm{pay}$.
- $\pi_{\mathrm{selfish}}$: Set $\pi(x_1) = \mathrm{refuse}$.

#### The CDT Analysis
Carl the CDT agent arrives at $x_1$. He consults a causal graph where his current act $\mathrm{Act}$ has no causal influence over the past event (the driver giving him a ride). Intervening on $\mathrm{Act}$:
\begin{align}
\mathbb{E}_{\mathrm{CDT}}[V \mid \Do(\mathrm{Act}=\mathrm{refuse}), x_1] &= \$0, \\
\mathbb{E}_{\mathrm{CDT}}[V \mid \Do(\mathrm{Act}=\mathrm{pay}), x_1] &= -\$1{,}000.
\end{align}
CDT strictly prescribes $\mathrm{refuse}$. Anticipating this, the driver predicts defection with 99% accuracy and leaves Carl in the desert to die. Carl achieves an expected utility of $-\$990{,}000$.

#### The EDT Analysis
Eve the EDT agent in the city conditions on her act: learning she pays is bad news (she is out $\$1{,}000$), since she already knows she is in the city. Thus EDT also defects at $x_1$ and dies in the desert.

#### The P-FDT Analysis
Fiona the P-FDT agent, standing at the ATM in the city ($x_1$), does not evaluate acts in isolation. She evaluates policies $\pi \in \Pi$ via Equation~\eqref{eq:pfdt-core} from the global perspective:

1. Under $\Do(\mathbf{\Pi}^* = \pi_{\mathrm{honest}})$:
   The driver's prediction variable $\mathrm{Pred}$ depends subjunctively on $\mathbf{\Pi}^*$. With probability $0.99$, $\mathrm{Pred} = \mathrm{rescue}$, leading to observation $x_1$, where $\pi_{\mathrm{honest}}(x_1) = \mathrm{pay}$ is executed.
   \begin{equation}
   \mathbb{E}[V \mid \Do(\mathbf{\Pi}^* = \pi_{\mathrm{honest}})] = 0.99 \cdot (-\$1{,}000) + 0.01 \cdot (-\$1{,}000{,}000) = -\$990 - \$10{,}000 = -\$10{,}990.
   \end{equation}

2. Under $\Do(\mathbf{\Pi}^* = \pi_{\mathrm{selfish}})$:
   The driver predicts non-payment with probability $0.99$, setting $\mathrm{Pred} = \mathrm{abandon}$, leaving the agent at $x_2$ to die.
   \begin{equation}
   \mathbb{E}[V \mid \Do(\mathbf{\Pi}^* = \pi_{\mathrm{selfish}})] = 0.99 \cdot (-\$1{,}000{,}000) + 0.01 \cdot (\$0) = -\$990{,}000.
   \end{equation}

Comparing the two global expectations:
\begin{equation}
\mathbb{E}[V \mid \Do(\mathbf{\Pi}^* = \pi_{\mathrm{honest}})] \gg \mathbb{E}[V \mid \Do(\mathbf{\Pi}^* = \pi_{\mathrm{selfish}})].
\end{equation}
P-FDT unambiguously selects $\pi^* = \pi_{\mathrm{honest}}$. Evaluating this policy at her current observation $x_1$:
\begin{equation}
a = \pi^*(x_1) = \mathrm{pay}.
\end{equation}
The P-FDT agent happily pays the driver. Consequently, the driver accurately predicts this disposition, rescues the agent, and the agent survives Parfit's desert.

---

### 5.2 The Transparent Newcomb Problem
Consider Drescher's (2006) Transparent Newcomb Problem:
Box A contains a visible $\$1{,}000$. Box B is transparent, containing either $\$1{,}000{,}000$ or $\$0$. A 99% accurate predictor placed $\$1{,}000{,}000$ into Box B if and only if she predicted that the agent would take only Box B upon *observing* that both boxes are full. The agent stands before the boxes and sees that both are full ($\mathrm{Obs} = \text{both-full}$). Should she take one box ($a = \text{one-box}$) or both ($a = \text{two-box}$)?

Both CDT and EDT prescribe two-boxing: Box B is already observed to be full; taking Box A provides an additional, unconditional $\$1{,}000$.

Let the observations be $\mathcal{X} = \{x_{\mathrm{full}}, x_{\mathrm{empty}}\}$, denoting whether Box B is seen to contain $\$1{,}000{,}000$ or $\$0$.
The primitive actions are $\mathcal{A} = \{\mathrm{1B}, \mathrm{2B}\}$.
The candidate policies $\pi : \mathcal{X} \to \mathcal{A}$ include:
- $\pi_{1}$: $\pi(x_{\mathrm{full}}) = \mathrm{1B}$, $\pi(x_{\mathrm{empty}}) = \mathrm{2B}$.
- $\pi_{2}$: $\pi(x_{\mathrm{full}}) = \mathrm{2B}$, $\pi(x_{\mathrm{empty}}) = \mathrm{2B}$.

The predictor's prediction $\mathrm{Pred} \in \{\mathrm{full}, \mathrm{empty}\}$ subjunctively depends on whether the agent instantiates a policy that leaves Box A behind when seeing a full box:
\begin{equation}
P(\mathrm{Pred} = \mathrm{full} \mid \Do(\mathbf{\Pi}^* = \pi)) = 
\begin{cases} 
0.99 & \text{if } \pi(x_{\mathrm{full}}) = \mathrm{1B}, \\
0.01 & \text{if } \pi(x_{\mathrm{full}}) = \mathrm{2B}.
\end{cases}
\end{equation}

We evaluate the expected global utility of each policy:
\begin{align}
\mathbb{E}[V \mid \Do(\mathbf{\Pi}^* = \pi_{1})] &= 0.99 \cdot \mathcal{U}(\$1{,}000{,}000) + 0.01 \cdot \mathcal{U}(\$1{,}000) \approx \$990{,}010, \\
\mathbb{E}[V \mid \Do(\mathbf{\Pi}^* = \pi_{2})] &= 0.01 \cdot \mathcal{U}(\$1{,}001{,}000) + 0.99 \cdot \mathcal{U}(\$1{,}000) \approx \$10{,}010 + \$990 = \$11{,}000.
\end{align}
Clearly, $\pi_1$ dominates $\pi_2$ globally by $\$979{,}010$. 

Therefore, P-FDT identifies $\pi^* = \pi_1$. Standing in front of the transparent boxes with observation $x_{\mathrm{full}}$, the agent's action execution is purely mechanical:
\begin{equation}
a = \pi^*(x_{\mathrm{full}}) = \mathrm{1B}.
\end{equation}
The P-FDT agent leaves the $\$1{,}000$ behind, precisely as she would have precommitted to do. Because she implements this policy, predictors reliably anticipate it, fill Box B, and P-FDT agents walk away with $\$1{,}000{,}000$, whereas CDT and EDT agents reliably face empty boxes.

---

### 5.3 The Mechanical Blackmail
In Soares and Fallenstein's (2015) Mechanical Blackmail:
An autonomous damaging program will release catastrophic compromising data costing the agent $\$1{,}000{,}000$ unless the agent wires $\$1{,}000$ upon receipt of a blackmail notification letter. The blackmailer is an infallible predictor who only activates the program and sends the letter if she predicts the agent will pay upon receiving it. 

The agent receives the letter ($x = \mathrm{letter}$). 

- **CDT and EDT** see that the program is already running and pay the $\$1{,}000$ to avert the $\$1{,}000{,}000$ catastrophe. Consequently, blackmailers reliably target CDT and EDT agents.
- **P-FDT** evaluates the policy space $\Pi = \{\pi_{\mathrm{yield}}, \pi_{\mathrm{defy}}\}$:
  - Under $\Do(\mathbf{\Pi}^* = \pi_{\mathrm{yield}})$: The blackmailer predicts payment, launches the attack, sends the letter, and the agent pays $\$1{,}000$. Expected payoff: $-\$1{,}000$.
  - Under $\Do(\mathbf{\Pi}^* = \pi_{\mathrm{defy}})$: The blackmailer predicts refusal, aborts the program entirely, and sends no letter. Expected payoff: $\$0$.

The optimal global policy is unambiguously:
\begin{equation}
\pi^* = \pi_{\mathrm{defy}}.
\end{equation}
Holding the letter in her hands, the P-FDT agent executes:
\begin{equation}
a = \pi^*(\mathrm{letter}) = \mathrm{refuse}.
\end{equation}
Because the agent implements a decision procedure that outputs $\pi_{\mathrm{defy}}$, an infallible blackmailer never sends her the letter in the actual world. If the blackmailer were slightly fallible (e.g., error rate $\epsilon = 0.0001$), the P-FDT agent still refuses, because the expected cost of being known as an agent who yields ($-\$1{,}000$ on every encounter) far outweighs the rare unluckily triggered disaster ($\epsilon \cdot -\$1{,}000{,}000 = -\$100$). P-FDT forms an ironclad defense against extortion.

---

## 6. Resolving Multi-Agent and Dynamic Dilemmas: Why Policy-Selection Matters

Footnote 16 remarks that the policy-selection formulation:
> "...makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

Why did Yudkowsky and Soares single out multi-agent and dynamic dilemmas for this distinction? Understanding this reveals the mathematical necessity of P-FDT over act-level FDT.

### 6.1 The "Double-Update" Pathology of Timeless Decision Theory
Early predecessors of FDT, such as Yudkowsky’s (2010) *Timeless Decision Theory* (TDT), attempted to evaluate counterfactuals by simultaneously updating on an observation $x$ via Bayes' rule *and* intervening on the action variable:
\begin{equation}
\argmax_{a} \mathbb{E}\left[ V \;\middle|\; \Do(\mathrm{TDT}(x) = a), \mathrm{Obs} = x \right].
\end{equation}
As noted in the paper's inline annotations, this procedure induces a destructive **"double update."** If an agent observes evidence that correlates subjunctively with her own decision, conditioning on that evidence freezes parts of the world-model that the intervention itself should have been allowed to counterfactually modify.

Act-level FDT attempted to resolve this by eliminating the Bayesian update on $\mathrm{Obs} = x$ during the intervention, instead shifting the *site* of intervention to a node indexed by observation: $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$. However, in complex multi-agent games with asymmetric information or sequential moves, act-level FDT can suffer from **subgame incoherence**. 

Consider an extensive-form game where Player 1 moves, sending a signal to Player 2, who then moves. If Player 2 is modeled by Player 1, Player 1's choice of action depends not merely on what Player 2 will do given the actual signal, but on the *entire profile of Player 2's responses across all possible signals*—that is, on Player 2's **policy**. 

If Player 2 deliberates using act-level FDT, she only optimizes her action locally when she finds herself at an information set. But in games involving mutual simulation (such as program equilibrium; Tennenholtz, 2004), another agent simulating Player 2 inspects the *entire code or policy* of Player 2. If Player 2 evaluates decisions act-by-act, Player 1’s simulation may fail to find a stable fixed point, or Player 2 may be unable to credibly project off-path threats and promises.

### 6.2 Program Equilibrium and Mutual Policy Simulation
In multi-agent settings where agents exchange or predict each other's source code, agents can achieve cooperative outcomes that are impossible under classical Nash equilibrium. 

Suppose two agents, Alice and Bob, face a Prisoner's Dilemma. Each has access to a subjunctive model of the other. Alice runs P-FDT, selecting a policy $\pi_A : \mathcal{X}_A \to \{\mathrm{C}, \mathrm{D}\}$. Bob also runs P-FDT, selecting $\pi_B : \mathcal{X}_B \to \{\mathrm{C}, \mathrm{D}\}$.

Because both agents iterate over the space of policies, they can implement policies conditioned on the subjunctive extraction of the other's policy:
\begin{equation}
\pi_A^*(\cdot) = \begin{cases} 
\mathrm{C} & \text{if } \mathbf{\Pi}_B^* = \pi_{\mathrm{coop}}, \\ 
\mathrm{D} & \text{otherwise}. 
\end{cases}
\end{equation}
Under P-FDT, the space of strategic interaction is elevated from the primitive action game to the **policy meta-game**:
\begin{equation}
\mathcal{G} = (\mathcal{I}, \{\Pi_i\}_{i \in \mathcal{I}}, \{\tilde{\mathcal{U}}_i\}_{i \in \mathcal{I}}),
\end{equation}
where $\tilde{\mathcal{U}}_i(\pi_1, \dots, \pi_n) = \mathbb{E}\left[\mathcal{U}_i \;\middle|\; \Do(\mathbf{\Pi}_1^* = \pi_1, \dots, \mathbf{\Pi}_n^* = \pi_n)\right]$. 

Because P-FDT operates directly on the global policy node $\mathbf{\Pi}^*$, an agent's commitment to cooperate conditionally on the other's cooperative policy is mathematically transparent to external predictors. This enables P-FDT agents to effortlessly realize Pareto-optimal cooperation in games where CDT agents are condemned to defect by act-level dominance.

---

## 7. Open Problems and Mathematical Uncertainties

While P-FDT provides an exceptionally potent framework, translating footnote 16 into a complete, universal foundational theory faces several deep mathematical challenges that must be explicitly acknowledged.

### 7.1 The Infinite Regress of Policy Deliberation
In Equation~\eqref{eq:pfdt-core}, the P-FDT policy selection is defined as:
\begin{equation}
\pi^* = \argmax_{\pi \in \Pi} \mathbb{E}\left[ V \;\middle|\; \Do(\mathbf{\Pi}^* = \pi) \right].
\end{equation}
Notice that the policy $\pi^*$ is itself an element of $\Pi$. But what is the mathematical nature of the algorithm that computes this $\argmax$? 

If the agent’s deliberation process is computationally bounded, running an exhaustive search over $\Pi = \mathcal{A}^{\mathcal{X}}$ is impossible, as the policy space grows exponentially with the size of the observation history space $|\mathcal{X}|$ (and becomes uncountable if $\mathcal{X}$ is continuous). 

Furthermore, if the agent's policy $\pi$ must take into account that other agents are predicting her policy, and those agents' policies depend on predicting hers, we encounter self-referential fixed-point problems. While Kleene's recursion theorem guarantees the existence of self-referential programs, it does not guarantee that arbitrary systems of mutual simulation possess unique, non-trivial fixed points without introducing probabilistic smoothing or continuous relaxation (e.g., Kakutani's fixed-point theorem applied to mixed policies).

### 7.2 The Problem of Counterpossibles and Logical Conditioning
Equation~\eqref{eq:pfdt-core} relies on Pearl’s $\Do$-operator applied to a logical variable $\mathbf{\Pi}^*$. However, as Yudkowsky and Soares acknowledge in Section 5:
> "Equation [4] works *given* a graph that accurately describes how changing the value of a logical variable affects other variables, but it is not yet clear how to construct such a thing... Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

In standard graphical models, setting $\Do(\mathrm{Var} = val)$ is well-defined because variables represent mutually independent physical configurations before intervention. But if $\mathbf{\Pi}^*$ is the output of a deterministic Turing machine $\mathcal{M}$ on input $(P, G)$, then the assertion:
\begin{equation}
\mathbf{\Pi}^* = \pi' \quad (\text{where } \pi' \neq \mathcal{M}(P, G))
\end{equation}
is an **arithmetical contradiction**. It asserts that a deterministic mathematical function evaluates to something other than what it evaluates to.

CDT evades this because physical acts are contingent. EDT evades this because it conditions only on observations. P-FDT, by intervening on types, demands a coherent mathematical theory of **logical counterpossibles** (Cohen, 1990; Bjerring, 2013). 

Currently, two primary approaches exist to resolve this foundational gap:
1. **Proof-Theoretic and Algorithmic Probability:** Assigning probabilities to logical sentences via coherent probability distributions over formal theories (Gaifman, 2004; Demski, 2012; Garrabrant et al., 2016 on Logical Induction). An intervention on a logical node corresponds to adding an explicit axiom or modifying the evaluation trace of a bounded prover.
2. **Structural Logical Graphs:** Treating the dependency graph $G$ as an exogenously specified Bayesian network where edges encode known computational or inferential dependencies, side-stepping pure semantic model theory in favor of pragmatic causal modeling of computational tokens.

Until a definitive, consensus theory of logical counterfactuals is established, P-FDT’s operational calculus must be understood as conditional upon an agent possessing a valid subjunctive graph $G$.

---

## 8. Comparative Synthesis

The operational differences among the four primary decision theories are systematically contrasted in the following table:

| Decision Theory | Object of Evaluation | Counterfactual Operator | Response to Observation $x$ | Newcomb's Problem | Smoking Lesion | Parfit's Hitchhiker | Mechanical Blackmail |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **EDT** | Act $a \in \mathcal{A}$ | Bayesian conditioning: $P(\cdot \mid x, a)$ | Direct Bayesian update | One-box | Refrain (Fatalist failure) | Refuse (Dies in desert) | Pays (Exploited) |
| **CDT** | Act $a \in \mathcal{A}$ | Physical act intervention: $\Do(\mathrm{Act} = a)$ | Bayesian update on background variables | Two-box (Leaves $\$1\mathrm{M}$) | Smoke (Optimal) | Refuse (Dies in desert) | Pays (Exploited) |
| **FDT (Act)** | Functional output $\mathtt{fdt}(\cdot) \in \mathcal{A}$ | Algorithmic intervention: $\Do(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)$ | Switches intervention node to match $x$ | One-box | Smoke | Pays (Survives) | Refuses (Safe) |
| **P-FDT** | Global policy $\pi \in \Pi$ | Policy intervention: $\Do(\mathbf{\Pi}^* = \pi)$ | Applies optimal global policy: $a = \pi^*(x)$ | One-box | Smoke | Pays (Survives) | Refuses (Safe) |

---

## 9. Conclusion

Policy Functional Decision Theory (P-FDT), foreshadowed in footnote 16 of Yudkowsky and Soares (2017), represents the logical culmination of the functional approach to instrumental rationality. By elevating the target of decision deliberation from the localized, physical act token $\mathrm{Act}$ to the global policy mapping type $\mathbf{\Pi}^*$, P-FDT dissolves the historic tension between dynamic consistency and counterfactual evaluation.

Under P-FDT, an agent does not frantically evaluate what isolated physical movement yields the most utility after finding herself trapped in the city, standing before two full transparent boxes, or staring at an extortion letter. Instead, she recognizes that her current choice is simply the local instantiation of a fixed mathematical mapping. By evaluating which *mapping* maximizes expected global utility when subjunctively propagated through all predicting and simulating systems in the universe, the agent naturally exhibits the behaviors that classical theories could only emulate via ad-hoc, expensive precommitments.

P-FDT demonstrates that true instrumental rationality does not consist in shortsightedly snatching a free thousand dollars at the expense of an empty million-dollar box, nor in pathologically managing the news of one's cancer. Rather, it consists in being the kind of agent whose global functional signature systematically shapes the world into one where the desert yields a rescue, the blackmailer aborts her scheme, and the boxes are always full.

---

## References

- Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
- Arntzenius, F. (2008). No Regrets, or: Edith Piaf Revamps Decision Theory. *Erkenntnis*, 68(2), 277–297.
- Bjerring, J. C. (2013). On Counterpossibles. *Philosophical Studies*, 168(2), 1–27.
- Cohen, D. (1990). On What Cannot Be. In *Truth or Consequences: Essays in Honor of Nuel Belnap*, pp. 123–132. Kluwer Academic Publishers.
- Dai, W. (2009). Towards a New Decision Theory. *LessWrong*.
- Demski, A. (2012). Logical Prior Probability. In *Artificial General Intelligence (AGI 2012)*, LNCS 7716, pp. 50–59. Springer.
- Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
- Eells, E. (1984). Metatickles and the Dynamics of Deliberation. *Theory and Decision*, 17(1), 71–95.
- Gaifman, H. (2004). Reasoning with Limited Resources and Assigning Probabilities to Arithmetical Statements. *Synthese*, 140(1–2), 97–119.
- Garrabrant, S., Benson-Tilsen, T., Critch, A., Soares, N., & Taylor, J. (2016). Logical Induction. *arXiv preprint arXiv:1609.03543*.
- Gibbard, A., & Harper, W. L. (1978). Counterfactuals and Two Kinds of Expected Utility. In C. A. Hooker, J. J. Leach, & E. F. McClennen (Eds.), *Foundations and Applications of Decision Theory*, Vol. 1, pp. 125–162. D. Reidel.
- Jeffrey, R. C. (1983). *The Logic of Decision* (2nd ed.). University of Chicago Press.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Joyce, J. M. (2012). Regret and Instability in Causal Decision Theory. *Synthese*, 187(1), 123–145.
- Kleene, S. C. (1938). On Notation for Ordinal Numbers. *Journal of Symbolic Logic*, 3(4), 150–155.
- Lewis, D. (1979). Prisoners’ Dilemma is a Newcomb Problem. *Philosophy & Public Affairs*, 8(3), 235–240.
- Lewis, D. (1981). Causal Decision Theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
- Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
- Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
- Skyrms, B. (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
- Soares, N., & Fallenstein, B. (2015). Toward Idealized Decision Theory. *arXiv preprint arXiv:1507.01986*.
- Tennenholtz, M. (2004). Program Equilibrium. *Games and Economic Behavior*, 49(2), 363–373.
- Yudkowsky, E. (2010). *Timeless Decision Theory*. Technical Report, The Singularity Institute, San Francisco, CA.
- Yudkowsky, E., & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. *arXiv preprint arXiv:1710.05060v2*.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
