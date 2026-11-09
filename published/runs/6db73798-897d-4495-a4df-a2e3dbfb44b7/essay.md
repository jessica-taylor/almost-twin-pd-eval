# Deciding by Policy: A Mathematical Exposition of Policy Functional Decision Theory (P-FDT)

## 1. Introduction: From Act Selection to Policy Optimization

Modern normative decision theory has long been divided between two paradigms: **Causal Decision Theory (CDT)** \citep{Lewis:1981, Joyce:1999} and **Evidential Decision Theory (EDT)** \citep{Jeffrey:1983}. In problems where the environment correlates with an agent's choices without being causally downstream of those choices, both frameworks run into notorious conceptual and practical difficulties. CDT famously two-boxes in Newcomb's problem \citep{Nozick:1969}, refusing to "manage the past," and thereby walks away poor. Standard EDT one-boxes in Newcomb's problem, but falls prey to mere statistical correlations in scenarios like the smoking lesion problem \citep{Skyrms:1980}, avoiding smoking to suppress the bad news of a deadly arterial lesion.

To transcend this dichotomy, Yudkowsky and Soares \citeyearpar{Yudkowsky:2010:TDT, Soares:2015:toward} introduced **Functional Decision Theory (FDT)**. The core insight of FDT is that an agent ought to treat their decision not as an isolated physical intervention on an act token ($\Act = a$), but as the output of an invariant mathematical algorithm—a decision function. By intervening on the *logical type* rather than the *physical token*, FDT captures the non-causal *subjunctive dependencies* that obtain when other physical systems (such as predictors, simulation engines, or game-theoretic twins) run models of, or share code with, the agent's decision function.

In the primary formulation of FDT presented in the body of Yudkowsky and Soares's paper, an agent evaluating a decision given an observation history $x$ computes an intervention directly on the algorithm evaluated on that specific observation: $\Do(\FDTvar(\dots, x) = a)$. However, as the authors note in footnote~7 and footnote~16:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper." (Footnote 7)

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition." (Footnote 16)

This policy-level variant is what we designate as **Policy Functional Decision Theory (P-FDT)**. 

While act-based FDT evaluates hypothetical assignments to individual decision instances $\FDT(\dots, x)$, **P-FDT** elevates the object of counterfactual evaluation to a global decision rule: a policy $\pi \colon \mathcal{X} \to \mathcal{A}$ mapping arbitrary observation histories to actions. P-FDT formalizes what it means to possess an optimal predisposition. Rather than asking "What happens if this algorithm outputs $a$ right now?", a P-FDT agent asks: "What global behavioral rule $\pi$ across all epistemically possible circumstances maximizes expected utility, and what does that optimal rule dictate here?"

This essay develops a rigorous mathematical account of P-FDT. We formalize its representation of dependencies, its evaluation of counterfactual policies, and its operational mechanics. We then apply P-FDT to canonical predictive dilemmas, contrast it with standard CDT, EDT, and act-based FDT, and resolve open foundational ambiguities that footnote~16 leaves unspecified.

---

## 2. Foundations: Models, Subjunctive Graphs, and Policies

### 2.1 The Space of Observations, Actions, and Policies

Let $(\Omega, \mathcal{F}, P)$ be a probability space underlying an agent's subjective world-model. We define three fundamental finite or countably infinite sets:
1. $\mathcal{X}$: The space of possible observation histories or epistemic contexts $x$ that the agent may observe prior to acting.
2. $\mathcal{A}$: The finite alphabet of physical actions $a$ available to the agent's actuators.
3. $\mathcal{O}$: The set of ultimate outcomes $o$, equipped with a bounded utility function $\Util \colon \mathcal{O} \to \mathbb{R}$. We denote the utility random variable as $\VV \coloneqq \Util(\Outcome)$.

A **policy** $\pi$ is a deterministic function mapping every conceivable observation to an action:
$$\pi \colon \mathcal{X} \to \mathcal{A}, \quad \pi \in \Pi \coloneqq \mathcal{A}^{\mathcal{X}}.$$
*(For stochastic extensions, $\pi(x) \in \Delta(\mathcal{A})$, but for the dilemmas considered in the foundational literature, deterministic policies suffice).*

### 2.2 Subjunctive Dependency Graphs

Following Pearl's structural causal framework \citep{Pearl:1996, Pearl:2000}, Causal Decision Theory defines an agent's world-model as a pair $(P, G)$, where $G = (V, E)$ is a Directed Acyclic Graph (DAG) whose vertices $V$ represent physical random variables, and whose directed edges represent asymmetric physical-causal mechanisms. In CDT, deliberation is modeled via the graph surgery $\Do(\Act = a)$, which severs all incoming edges to the physical node $\Act$ and sets its value to $a$, leaving non-downstream variables entirely invariant.

P-FDT generalizes this graphical formalism to incorporate mathematical, computational, and logical relationships:
- The graph $G = (V, E)$ is a **subjunctive dependency graph**. 
- Vertices $V$ include physical state variables (such as box contents, cancer status, driver actions) and **algorithmic node types**.
- Crucially, $G$ contains a distinguished functional node representing the agent's policy calculation, denoted $\mathbf{\Pi} \coloneqq \PFDTvar(\underline{P}, \underline{G})$.
- Directed edges emanating from $\mathbf{\Pi}$ encode *subjunctive dependencies*: if an external process $Y$ (such as an accurate predictor $S$) simulates, inspects, or shares algorithmic code with $\mathbf{\Pi}$, then $Y$ is a child or descendant of $\mathbf{\Pi}$ in $G$.

When an agent's code is deployed across distinct physical embodiments (e.g., twins or predictive simulations), those physical manifestations subjunctively depend upon the single mathematical object $\mathbf{\Pi}$. As Yudkowsky and Soares argue, intervening on $\mathbf{\Pi}$ intervenes on the *type*, not merely the local physical *token*.

```
   [ Subjunctive Graph in P-FDT ]
   
             +------------------------+
             | \PFDTvar(\underline{P},\underline{G}) |  <-- Intervention Node \mathbf{\Pi}
             +------------------------+
               /                    \
              / (subjunctive)        \ (subjunctive / behavioral)
             v                        v
      +--------------+          +-----------------------+
      |  Predictor   |          | Observation Node \Obs |
      |  Simulation  |          +-----------------------+
      +--------------+                      |
             |                              | (realized input)
             v                              v
      +--------------+          +-----------------------+
      | Physical Box | -------> | Act: a = \pi(\Obs)    |
      +--------------+          +-----------------------+
             \                              /
              \                            /
               v                          v
             +------------------------------+
             | Outcome \Outcome / Utility \VV|
             +------------------------------+
```

---

## 3. Formalizing Policy Functional Decision Theory (P-FDT)

### 3.1 The Policy-Selection Equation

In standard act-based FDT \citep{Yudkowsky:2010:TDT}, given an observation $x$, the agent solves:
$$\FDT(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\Big[\VV \;\Big|\; \Do\big(\FDTvar(\underline{P}, \underline{G}, \underline{x}) = a\big)\Big]. \tag{Act-FDT}$$
Act-FDT intervenes on the specific computational output indexed by the realized observation $x$.

Under **P-FDT**, as formulated in footnote~16, the agent performs a two-stage evaluation:
1. **Global Optimization:** The agent optimizes over the entire policy space $\Pi$, asking which mapping $\pi \colon \mathcal{X} \to \mathcal{A}$ causes the highest expected utility when substituted for the functional node $\mathbf{\Pi}$.
2. **Local Execution:** Having identified the optimal policy $\pi^*$, the agent executes the action prescribed by $\pi^*$ for their actual observation history $x$.

Formally, we define the P-FDT decision procedure:

$$\pi^* \coloneqq \argmax_{\pi \in \Pi} \mathbb{E}\Big[\VV \;\Big|\; \Do\big(\mathbf{\Pi} = \pi\big)\Big] \tag{P-FDT-1}$$

$$\PFDT(P, G, x) \coloneqq \pi^*(x) \tag{P-FDT-2}$$

where $\mathbf{\Pi} = \PFDTvar(\underline{P}, \underline{G})$ is the un-instantiated decision function implemented by the agent.

### 3.2 Evaluation of Counterfactuals and Conditionals

Equation \eqref{eq:fdt} from the reference paper intervened on a specialized node $\FDTvar(\underline{P},\underline{G},\underline{x})$. P-FDT replaces this with an intervention on the policy variable $\mathbf{\Pi} = \pi$. 

Under Pearl's $\Do$-operator extended to functional nodes, setting $\Do(\mathbf{\Pi} = \pi)$ propagates as follows:
1. In the subjunctive graph $G$, remove all incoming edges to the functional node $\mathbf{\Pi}$.
2. Set the value of $\mathbf{\Pi}$ to the function $\pi$.
3. For every node $Z$ downstream of $\mathbf{\Pi}$:
   - If an environmental predictor $S$ contains a mental model or simulation of the agent, its prediction $\widehat{\Act}$ is recomputed as $\widehat{\Act} = \text{Sim}( \mathbf{\Pi} )$. In the case of an accurate predictor simulating the agent under hypothetical inputs $x'$, the simulated output evaluates to $\pi(x')$.
   - The physical action node $\Act$ of the agent is structurally defined by functional evaluation: $\Act = \mathbf{\Pi}(\Obs) = \pi(\Obs)$.
   - All intermediate variables (e.g., whether Box B was filled yesterday, whether a driver stopped in the desert, whether a blackmailer sent a letter) take on the values induced by the downstream consequences of $\pi$.

Because $\mathbf{\Pi}$ is intervened upon *globally*, the counterfactual world generated by $\Do(\mathbf{\Pi} = \pi)$ does not merely imagine the action changing at the current observation history $x$. It imagines the agent *being an agent who systematically responds to any $x' \in \mathcal{X}$ with $\pi(x')$*.

---

## 4. Resolving Open Mathematical Ambiguities in Footnote 16

Footnote 16 specifies that the agent "chooses not an action but a policy... to which the agent then applies her inputs in order to select an action." However, the source leaves unresolved an essential mathematical subtlety: **At what epistemic stage is the expectation in Equation \eqref{P-FDT-1} evaluated?**

Specifically, when an agent sits at a decision node having observed $x \in \mathcal{X}$, should the policy $\pi$ be chosen by maximizing expected utility *prior* to conditioning on $x$ (an ex-ante / updateless perspective), or by maximizing expected utility *conditional* on having observed $x$ (an ex-post / posterior perspective)?

Let us rigorously analyze both proposals.

### 4.1 Proposal A: Ex-Ante (Updateless) Policy Functional Decision Theory

Under the ex-ante interpretation (closely aligned with Wei Dai's Updateless Decision Theory, \citeyear{Dai:2009}), the policy $\pi^*$ is chosen relative to the agent's prior distribution $P$, integrating over all possible observations that the agent might receive:

$$\pi^*_{\text{ante}} = \argmax_{\pi \in \Pi} \sum_{x' \in \mathcal{X}} P(\Obs = x') \cdot \mathbb{E}\Big[\VV \;\Big|\; \Do(\mathbf{\Pi} = \pi), \Obs = x'\Big]. \tag{Ex-Ante}$$

Equivalently, $\pi^*_{\text{ante}} = \argmax_{\pi \in \Pi} \mathbb{E}_{P}\big[\VV \mid \Do(\mathbf{\Pi} = \pi)\big]$. The agent calculates $\pi^*_{\text{ante}}$ once (or counterfactually considers what policy maximizes prior expected utility), and then upon observing $x$, takes action $\act = \pi^*_{\text{ante}}(x)$.

### 4.2 Proposal B: Ex-Post (Posterior) Policy Functional Decision Theory

Under the ex-post interpretation, the agent observes $x$ first, conditions the probability distribution on $\Obs = x$, and *then* optimizes the global policy $\pi$:

$$\pi^*_{\text{post}(x)} = \argmax_{\pi \in \Pi} \mathbb{E}\Big[\VV \;\Big|\; \Do(\mathbf{\Pi} = \pi), \Obs = x\Big]. \tag{Ex-Post}$$

The agent then executes $a = \pi^*_{\text{post}(x)}(x)$.

### 4.3 Why Proposal A (Ex-Ante) is the Correct Operationalization of P-FDT

A profound result in predictive decision theory—foreshadowed in Section~9 of the reference paper—demonstrates that **Proposal B (Ex-Post) breaks down in predictive dilemmas with asymmetric observation histories**.

Consider the **Mechanical Blackmail** (Dilemma~\ref{dil:cblackmail}). If the agent conditions on $\Obs = \Val{blackmail}$ before selecting a policy, the observation node is held fixed. Any policy $\pi$ that maps $\Val{blackmail} \mapsto \Val{refuse}$ leads to a catastrophe in the conditional world where the blackmail *has already occurred*, unless the graph surgery on $\mathbf{\Pi}$ is capable of changing the probability of $\Obs = \Val{blackmail}$ from within the conditional distribution $P(- \mid \Obs = \Val{blackmail})$. 

As the authors observe in Section~9:
> "FDT says that agents should entertain the hypothesis that, if their action were different, they might have *made different observations*."

If an agent conditions on $\Obs = x$ in the standard Kolmogorov sense, events where $\Obs \neq x$ are assigned probability zero. Intervening via Pearl's classical $\Do$-calculus *after* conditioning on $\Obs = x$ cannot revive states where the agent was never blackmailed, unless the intervention $\Do(\mathbf{\Pi} = \pi)$ retroactively updates the prior observation—which standard Pearlian conditioning explicitly prohibits.

In contrast, **Proposal A (Ex-Ante P-FDT)** avoids this contradiction completely:
1. The optimization over $\pi \in \Pi$ is performed over the global distribution.
2. In the global distribution, the node $\Obs$ is an endogenous variable determined downstream of the predictor's simulation of $\mathbf{\Pi}$.
3. For a policy $\pi_{\text{refuse}}$ that specifies $\pi(\Val{blackmail}) = \Val{refuse}$, the predictor simulates $\pi_{\text{refuse}}$, deduces that the agent will refuse, and therefore *never runs the program*. 
4. Hence, under $\Do(\mathbf{\Pi} = \pi_{\text{refuse}})$, $P(\Obs = \Val{blackmail}) \approx 0$, and the agent avoids both the blackmail payment and the catastrophic exposure.

Therefore, we formally establish that **P-FDT must be operationalized via Proposal A: Ex-Ante Policy Optimization**. The agent's algorithm identifies the policy $\pi^*$ that maximizes unconditional expected utility under the subjunctive intervention $\Do(\mathbf{\Pi} = \pi)$, and then evaluates that policy on the realized observation $x$.

---

## 5. Applying P-FDT Across Classic Decision Problems

We now trace the exact mathematical execution of P-FDT across the classic dilemmas presented in the reference paper, and compare its behavior to CDT, EDT, and act-based FDT.

```
+---------------------------+------------+------------+------------+------------+
| Dilemma                   | CDT        | EDT        | Act-FDT    | P-FDT      |
+---------------------------+------------+------------+------------+------------+
| Newcomb's Problem         | Two-box    | One-box    | One-box    | One-box    |
| Smoking Lesion            | Smoke      | Refrain    | Smoke      | Smoke      |
| Parfit's Hitchhiker       | Refuse     | Refuse     | Pay        | Pay        |
| Transparent Newcomb       | Two-box    | Two-box    | One-box    | One-box    |
| Mechanical Blackmail      | Pay        | Pay        | Refuse     | Refuse     |
+---------------------------+------------+------------+------------+------------+
```

### 5.1 Newcomb's Problem

In standard Newcomb's problem (Dilemma~\ref{dil:newcomb}), the observation set is trivial: $\mathcal{X} = \{ x_0 \}$, where $x_0$ represents the default epistemic state of facing the boxes. The action set is $\mathcal{A} = \{ \Val{onebox}, \Val{twobox} \}$. 

The policy space consists of only two constant policies:
$$\Pi = \{ \pi_1, \pi_2 \}, \quad \text{where } \pi_1(x_0) = \Val{onebox}, \; \pi_2(x_0) = \Val{twobox}.$$

The predictor's prediction $\Var{Pred} \in \{ 1, 2 \}$ subjunctively depends on $\mathbf{\Pi}$. With accuracy $1 - \epsilon = 0.99$:
$$P\big(\Var{Pred} = 1 \mid \Do(\mathbf{\Pi} = \pi_1)\big) = 0.99, \quad P\big(\Var{Pred} = 2 \mid \Do(\mathbf{\Pi} = \pi_2)\big) = 0.99.$$

Box B contains $\$1,000,000$ if $\Var{Pred} = 1$, and $\$0$ if $\Var{Pred} = 2$. Box A unconditionally contains $\$1,000$.

We compute the expected utilities under P-FDT:
$$\mathbb{E}\big[\VV \mid \Do(\mathbf{\Pi} = \pi_1)\big] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000.$$
$$\mathbb{E}\big[\VV \mid \Do(\mathbf{\Pi} = \pi_2)\big] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$10,010 + \$990 = \$11,000.$$

Since $\mathbb{E}[\VV \mid \Do(\mathbf{\Pi} = \pi_1)] > \mathbb{E}[\VV \mid \Do(\mathbf{\Pi} = \pi_2)]$, P-FDT uniquely selects $\pi^* = \pi_1$. 
Evaluated at the current observation $x_0$, the agent outputs:
$$\PFDT(P, G, x_0) = \pi^*(x_0) = \Val{onebox}.$$
P-FDT matches Act-FDT and EDT in achieving the $\$1,000,000$ payout, whereas CDT two-boxes and receives only $\$1,000$.

### 5.2 The Smoking Lesion Problem

In the Smoking Lesion Problem (Dilemma~\ref{dil:lesion}), the agent is afflicted with an unobservable arterial lesion with prior probability $p \in (0, 1)$. The lesion causes lung cancer with probability $0.99$ (versus $0.01$ without the lesion) and predisposes the agent toward smoking. Smoking provides an immediate net gain of $\$1,000$, while dying of cancer imposes a loss of $\$1,000,000$ (modeled as $\$0$ utility vs. $\$1,000,000$ for staying healthy).

Crucially, **cancer does not subjunctively depend upon the agent's decision function $\mathbf{\Pi}$**. The lesion is a purely biological condition; it does not read, simulate, or predict the mathematical output of $\mathbf{\Pi}$. 

In the subjunctive dependency graph $G$, the path between $\mathbf{\Pi}$ and $\Var{Cancer}$ passes through a common cause (or genetic predisposition), but there is no directed edge from $\mathbf{\Pi}$ to $\Var{Cancer}$, nor does $\Var{Cancer}$ model $\mathbf{\Pi}$.

The policy space over the trivial observation history is $\Pi = \{ \pi_{\Val{smoke}}, \pi_{\Val{refrain}} \}$.
Under the intervention $\Do(\mathbf{\Pi} = \pi)$, the probability of the lesion remains invariant:
$$P\big(\Var{Lesion} \mid \Do(\mathbf{\Pi} = \pi_{\Val{smoke}})\big) = P\big(\Var{Lesion} \mid \Do(\mathbf{\Pi} = \pi_{\Val{refrain}})\big) = p.$$

Consequently, the incidence of cancer is identical under both policies:
$$P\big(\Var{Cancer} \mid \Do(\mathbf{\Pi} = \pi)\big) = 0.99p + 0.01(1-p) \eqqcolon p_c.$$

Evaluating the expected utility of the policies:
$$\mathbb{E}\big[\VV \mid \Do(\mathbf{\Pi} = \pi_{\Val{smoke}})\big] = (1 - p_c)(\$1,000,000) + \$1,000.$$
$$\mathbb{E}\big[\VV \mid \Do(\mathbf{\Pi} = \pi_{\Val{refrain}})\big] = (1 - p_c)(\$1,000,000) + \$0.$$

P-FDT identifies $\pi^* = \pi_{\Val{smoke}}$. At execution:
$$\PFDT(P, G, x_0) = \Val{smoke}.$$
P-FDT smokes, successfully replicating the correct prescription of CDT and Act-FDT, while avoiding EDT's pathological refusal to smoke.

### 5.3 Transparent Newcomb and Parfit's Hitchhiker

The true power and elegance of P-FDT emerge in problems where the agent receives an observation that correlates with past predictive behavior.

In the **Transparent Newcomb Problem** (Dilemma~\ref{dil:transparent}), both Box A ($\$1,000$) and Box B ($\$1,000,000$ or $\$0$) are transparent. The agent observes the state of Box B before deciding whether to take one box or two:
$$\mathcal{X} = \{ \Val{full}, \Val{empty} \}, \quad \mathcal{A} = \{ \Val{onebox}, \Val{twobox} \}.$$

There are four conceivable policies in $\Pi = \mathcal{A}^\mathcal{X}$:
- $\pi_{11}$: Always one-box ($\Val{full} \mapsto \Val{onebox}, \Val{empty} \mapsto \Val{onebox}$).
- $\pi_{12}$: Conditional one-boxer ($\Val{full} \mapsto \Val{onebox}, \Val{empty} \mapsto \Val{twobox}$).
- $\pi_{22}$: Always two-box ($\Val{full} \mapsto \Val{twobox}, \Val{empty} \mapsto \Val{twobox}$).
- $\pi_{21}$: Inverted policy ($\Val{full} \mapsto \Val{twobox}, \Val{empty} \mapsto \Val{onebox}$).

The predictor places $\$1,000,000$ in Box B iff she predicts that the agent will leave Box A behind *upon seeing both boxes full*. That is:
$$\Var{Pred} = 1 \iff \text{Predictor simulates } \mathbf{\Pi}(\Val{full}) = \Val{onebox}.$$

Notice the decisive property: **The predictor's prediction depends solely on the policy's value at the input $\Val{full}$**.
- For any policy $\pi$ such that $\pi(\Val{full}) = \Val{onebox}$ (i.e., $\pi_{11}$ and $\pi_{12}$):
  $$P\big(\Var{Box B} = \Val{full} \mid \Do(\mathbf{\Pi} = \pi)\big) = 0.99.$$
  If the box is full, $\pi_{12}$ takes Box B only ($\$1,000,000$). If by a $1\%$ error the box is empty, $\pi_{12}$ observes $\Val{empty}$ and takes two boxes ($\$1,000$).
  Thus:
  $$\mathbb{E}\big[\VV \mid \Do(\mathbf{\Pi} = \pi_{12})\big] = 0.99(\$1,000,000) + 0.01(\$1,000) = \$990,010.$$

- For any policy $\pi$ such that $\pi(\Val{full}) = \Val{twobox}$ (i.e., $\pi_{22}$ and $\pi_{21}$):
  $$P\big(\Var{Box B} = \Val{full} \mid \Do(\mathbf{\Pi} = \pi)\big) = 0.01.$$
  Under $\pi_{22}$, in the $99\%$ of cases where the box is empty, the agent takes both boxes, receiving $\$1,000$. In the $1\%$ error case where the box is full, the agent takes both boxes, receiving $\$1,001,000$.
  Thus:
  $$\mathbb{E}\big[\VV \mid \Do(\mathbf{\Pi} = \pi_{22})\big] = 0.99(\$1,000) + 0.01(\$1,001,000) = \$990 + \$10,010 = \$11,000.$$

Comparing the policies globally:
$$\mathbb{E}\big[\VV \mid \Do(\mathbf{\Pi} = \pi_{12})\big] \gg \mathbb{E}\big[\VV \mid \Do(\mathbf{\Pi} = \pi_{22})\big].$$

P-FDT unambiguously selects the optimal policy $\pi^* = \pi_{12}$.

Now suppose the agent finds herself in the world where she observes the boxes, and **sees that Box B is full** ($x = \Val{full}$).
What does P-FDT prescribe? The agent simply consults $\pi^*$:
$$\PFDT(P, G, \Val{full}) = \pi^*(\Val{full}) = \Val{onebox}.$$

The agent leaves the transparent $\$1,000$ behind!

#### Comparison to CDT and EDT in Transparent Newcomb
- **CDT:** Given $\Obs = \Val{full}$, Carl the CDT agent observes that Box B already contains the money. The physical act of taking Box A cannot causally change the physical contents of Box B. Two-boxing strictly dominates one-boxing by $\$1,000$. Hence, CDT two-boxes, ensuring that Carl almost always faces an empty box.
- **EDT:** Given $\Obs = \Val{full}$, Eve the EDT agent already knows Box B is full ($P(\Var{Box B} = \Val{full} \mid \Obs = \Val{full}) = 1$). Taking Box A provides good news (+$\$1,000$) without altering the good news that the $\$1,000,000$ is already present. Hence, EDT also two-boxes.
- **Act-FDT:** Fiona the Act-FDT agent intervenes on $\FDTvar(\dots, \Val{full})$. If she sets this to $\Val{twobox}$, she imagines a world where the predictor predicted this and left the box empty. Hence, Act-FDT one-boxes.
- **P-FDT:** P-FDT achieves this result with supreme conceptual clarity. The agent does not need to perform complex counterfactual reasoning about whether she would be facing an empty box while staring at a full one. Rather, she recognizes that **the only way to be an agent that arrives at a full box in the first place is to implement a policy that one-boxes upon seeing a full box**. She executes the optimal policy $\pi^*$, which prescribes one-boxing at $\Val{full}$.

An identical mathematical formalization applies to **Parfit's Hitchhiker** (Dilemma~\ref{dil:parfit}). The driver only rescues the agent in the desert if she predicts that the agent implements a policy satisfying $\pi(\Val{city}) = \Val{pay}$. Upon arriving in the city, CDT and EDT refuse to pay the $\$1,000$. P-FDT recognizes that the optimal policy across the scenario is $\pi^*(\Val{city}) = \Val{pay}$, which reaps the $\$1,000,000$ benefit of rescue at the cost of $\$1,000$, leaving the agent with $\$999,000$ instead of death in the desert.

---

## 6. Mathematical Comparison: How P-FDT Differs from Act-FDT

Why does footnote 16 insist that policy selection is the "preferred formalization" of FDT, even though Act-FDT and P-FDT yield identical prescriptions in single-agent Newcomblike dilemmas?

The crucial difference appears in **multi-agent games and multi-stage dilemmas involving asymmetric information or counterfactual commitments**.

### 6.1 The "Double Update" Pathology in Act-FDT

In footnote~16 (and the accompanying todo annotation in Section~9), the authors remark that early formulations of functional decision theories (such as Yudkowsky’s Timeless Decision Theory \citeyearpar{Yudkowsky:2010:TDT}) suffered from a problematic "double update":
> "Another early variant, the 'Timeless Decision Theory' of Yudkowsky (2010), prescribes both conditioning on evidence *and* changing the place where one intervenes; this creates a kind of 'double update' which proves harmful in practice."

Under Act-FDT, the agent observes $x$, and then intervenes on $\FDTvar(\underline{P}, \underline{G}, \underline{x}) = a$. In Section~6, when Fiona evaluates Transparent Newcomb under Act-FDT, her hypothetical evaluation requires calculating:
$$\mathbb{E}\Big[\VV \;\Big|\; \Do\big(\FDTvar(\dots, \Val{full}) = \act\big), \Obs = \Val{full}\Big].$$
Because the graph contains a link from $\Var{Prediction}$ to $\Obs$, setting $\FDTvar(\dots, \Val{full}) = \Val{twobox}$ implies that $\Var{Prediction} = 2$, which implies $\Obs = \Val{empty}$. But the hypothetical was *already conditioned* on $\Obs = \Val{full}$! 

Act-FDT must therefore resolve a severe internal clash: it must evaluate a hypothetical where an intervention forces a variable to contradict the very observation on which the model was conditioned. As the authors admit in Section~6:
> "Fiona does not react to observations by conditioning her distribution. Rather, she reacts to observations by switching which variable she intervenes on... FDT says that agents should entertain the hypothesis that, if their action were different, they might have *made different observations*."

While Act-FDT patches this by replacing Bayesian conditioning with "intervening on the appropriate input-indexed node," this mechanism is mathematically fragile. It blurs the line between an observation and an intervention.

### 6.2 The Clean Resolution Provided by P-FDT

P-FDT resolves this conceptual tension completely by separating **policy optimization** from **policy execution**:

1. **Step 1 (Optimization):** The agent optimizes over the policy space $\Pi$ *unconditionally*. The probability distribution $P$ is never conditioned on contradictory evidence. The subjunctive intervention $\Do(\mathbf{\Pi} = \pi)$ acts cleanly on the root functional node, cleanly propagating forward to determine the joint distribution over predictions, environmental states, observations, and actions:
   $$P_{\pi}(\Obs = x, \Act = a, \Outcome = o) \coloneqq P\big(\Obs = x, \Act = a, \Outcome = o \;\big|\; \Do(\mathbf{\Pi} = \pi)\big).$$
2. **Step 2 (Execution):** The agent never asks "What if my policy were different?" after observing $x$. The optimal policy $\pi^* = \argmax_\pi \mathbb{E}_{P_\pi}[\VV]$ is already settled. The agent merely looks up $\pi^*(x)$ and executes it.

By moving the intervention from the *local act given $x$* to the *global policy $\pi$*, P-FDT eliminates the "double update." There is no contradiction between what is observed and what is intervened upon, because the intervention takes place at the level of the mathematical rule, prior to observation conditioning.

---

## 7. Open Challenges and Theoretical Frontiers for P-FDT

While P-FDT represents a significant mathematical and conceptual advance, it inherits and sharpens several profound theoretical challenges that remain open in the decision-theoretic literature.

### 7.1 The Computational Complexity of Policy Search

In any non-trivial environment, the observation space $\mathcal{X}$ is vast. If $|\mathcal{X}| = N$ and $|\mathcal{A}| = K$, the policy space $\Pi = \mathcal{A}^{\mathcal{X}}$ has cardinality $K^N$. 

In classical Markov Decision Processes (MDPs) where the Markov property holds and the environment does not contain subjunctive copies of the agent, dynamic programming and backward induction can find the optimal policy in polynomial time. However, in P-FDT settings, **the environment is non-Markovian in a radical sense**: an external actor's behavior at time $t=0$ depends subjunctively on what the policy $\pi$ would prescribe at time $t=100$ under an observation that may never be realized!

Because the predictor evaluates the policy globally, dynamic programming fails: sub-problems do not exhibit optimal substructure independent of counterfactual branches. Searching for $\pi^*$ in P-FDT is therefore an instance of non-linear functional optimization over a combinatorial space, which is in general NP-hard or undecidable \citep{Aaronson:2013:PhilosophersComplexity}. Practical approximations of P-FDT must rely on bounded heuristics, syntactic program search, or gradient-based policy representation in parameterized neural architectures.

### 7.2 The Problem of Subjunctive Graph Construction

As the reference paper highlights in Section~5:
> "Pearl (2000) has given a compelling philosophical account of how to deduce the structure of causation from observation and experiment, but no such formal treatment has yet been given to the problem of deducing the structure of other kinds of subjunctive dependence... Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

In P-FDT, this problem takes on a concrete form: How does an agent learn whether an external variable $Y$ depends subjunctively on $\mathbf{\Pi}$?

If two programs share source code, the dependency is logical. But what if an opponent in a game-theoretic dilemma runs a neural approximation of the agent, or uses a coarse abstraction of the agent's behavior? Deducing the graph edges between $\mathbf{\Pi}$ and environmental nodes requires a theory of **logical inductivism** and **program similarity** \citep{Demski:2012a, Soares:2015:toward}. Without an objective calculus for discovering subjunctive edges, P-FDT remains an idealized normative schema rather than a fully autonomous learning algorithm.

---

## 8. Conclusion: The Rationality of Policy-Level Agency

Policy Functional Decision Theory (P-FDT) redefines what it means to be an instrumentally rational agent. Classical decision theories ask:
- **CDT:** *What physical event does my body cause right now?*
- **EDT:** *What news would I like to hear about my current choice?*
- **Act-FDT:** *What output of my decision function on this specific input yields the best outcome?*

**P-FDT** synthesizes these into a higher-order normative question:
$$\text{\textit{"Which complete behavioral program }} \pi \colon \mathcal{X} \to \mathcal{A} \text{\textit{ would I prefer this very decision algorithm to instantiate across all circumstances?"}}$$

By shifting the locus of intervention from the local action token to the global behavioral policy, P-FDT resolves the deep paradoxes that have plagued decision theory for half a century:
1. It achieves high payouts in Newcomb-like problems by establishing predictable, subjunctive coordination with environmental predictors.
2. It smokes in the smoking lesion problem by recognizing that purely statistical or biological correlations are invariant under policy interventions.
3. It achieves temporal consistency without requiring external, physical precommitment mechanisms: a P-FDT agent naturally pays the hitchhiker and one-boxes in transparent Newcomb because the optimal policy $\pi^*$ contains those conditional commitments.
4. It avoids the mathematical and conceptual instability of the "double update," establishing a clean separation between the ex-ante optimization of a policy and its ex-post physical execution.

In an era increasingly shaped by autonomous artificial agents that are easily copied, inspected, simulated, and deployed in strategic environments, P-FDT provides a mathematically coherent, philosophically robust blueprint for normative rationality.

---

## References

\begin{hangparas}{.25in}{1}

Aaronson, Scott. 2013. "Why Philosophers Should Care About Computational Complexity." In *Computability: Turing, Gödel, Church, and Beyond*, edited by B. Jack Copeland, Carl J. Posy, and Oron Shagrir. MIT Press.

Ahmed, Arif. 2014. *Evidence, Decision and Causality*. Cambridge University Press.

Arntzenius, Frank. 2008. "No Regrets, or: Edith Piaf Revamps Decision Theory." *Erkenntnis* 68 (2): 277–297.

Dai, Wei. 2009. "Towards a New Decision Theory." *LessWrong* (blog), August 13, 2009. http://lesswrong.com/lw/15m/towards_a_new_decision_theory/.

Demski, Abram. 2012. "Logical Prior Probability." In *Artificial General Intelligence: 5th International Conference, AGI 2012*, edited by Joscha Bach, Ben Goertzel, and Matthew Iklé, 50–59. Springer.

Eells, Ellery. 1984. "Metatickles and the Dynamics of Deliberation." *Theory and Decision* 17 (1): 71–95.

Gibbard, Allan, and William L. Harper. 1978. "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, edited by C. A. Hooker, J. J. Leach, and E. F. McClennen, 13:125–162. D. Reidel.

Jeffrey, Richard C. 1983. *The Logic of Decision*. 2nd ed. University of Chicago Press.

Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. Cambridge University Press.

Joyce, James M. 2007. "Are Newcomb Problems Really Decisions?" *Synthese* 156 (3): 537–562.

Lewis, David. 1979. "Prisoners' Dilemma is a Newcomb Problem." *Philosophy & Public Affairs* 8 (3): 235–240.

Lewis, David. 1981. "Causal Decision Theory." *Australasian Journal of Philosophy* 59 (1): 5–30.

Nozick, Robert. 1969. "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel*, edited by Nicholas Rescher, 114–146. D. Reidel.

Parfit, Derek. 1986. *Reasons and Persons*. Oxford University Press.

Pearl, Judea. 1996. "Causation, Action, and Counterfactuals." In *6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-'96)*, edited by Yoav Shoham, 51–73. Morgan Kaufmann.

Pearl, Judea. 2000. *Causality: Models, Reasoning, and Inference*. Cambridge University Press.

Skyrms, Brian. 1980. *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.

Soares, Nate, and Benja Fallenstein. 2015. "Toward Idealized Decision Theory." *arXiv preprint arXiv:1507.01986 [cs.AI]*.

Spohn, Wolfgang. 1977. "Where Luce and Krantz Do Really Generalize Savage's Decision Model." *Erkenntnis* 11 (1): 113–134.

Yudkowsky, Eliezer. 2010. *Timeless Decision Theory*. Technical Report, Machine Intelligence Research Institute (formerly Singularity Institute).

Yudkowsky, Eliezer, and Nate Soares. 2017. "Functional Decision Theory: A New Theory of Instrumental Rationality." *arXiv preprint arXiv:1710.05060v2 [cs.AI]*.

\end{hangparas}