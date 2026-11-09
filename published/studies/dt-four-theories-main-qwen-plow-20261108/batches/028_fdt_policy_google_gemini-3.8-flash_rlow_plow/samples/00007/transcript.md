# 028_fdt_policy_google_gemini-3.8-flash_rlow_plow / 00007

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/e7f4e038-8fd7-48ed-a4a7-8669cdcad848/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/e7f4e038-8fd7-48ed-a4a7-8669cdcad848/call_0/response.raw) · finish: `stop`

### Visible response

````text
# Choosing the Decision Rule: A Mathematical Account of Policy Functional Decision Theory (P-FDT)

## 1. Introduction: From Act Selection to Policy Selection

Standard foundational debates in normative decision theory have long been organized around the clash between Evidential Decision Theory (EDT) and Causal Decision Theory (CDT). As formalized by authors such as Gibbard and Harper (1978), Skyrms (1980), and Joyce (1999), these frameworks disagree about how to evaluate counterfactual or conditional prospects: EDT evaluates an act based on the news value of having performed it, conditioning directly on the physical act, whereas CDT evaluates an act by holding fixed causal history and intervening via an operator like Pearl’s $\Do(\Act = a)$. 

In their paper *Functional Decision Theory: A New Theory of Instrumental Rationality*, Eliezer Yudkowsky and Nate Soares introduce Functional Decision Theory (FDT). FDT rejects the physical act token as the primitive locus of choice. Instead, FDT treats an agent’s decision as the output of an invariant mathematical function, intervening upon that function type across the entire world-model. 

However, the primary exposition of FDT in the Yudkowsky and Soares text focuses on an agent intervening on the specific execution of their decision function for a concrete observation history:
$$\FDT(P, G, x) = \argmax_{a \in \mathcal{A}} \mathbb{E}\left(V \;\middle|\; \Do(\FDTvar(\underline{P}, \underline{G}, \underline{x}) = a)\right)$$
While this act-level functional intervention handles classic puzzles like the standard Newcomb problem, the Psychological Twin Prisoner's Dilemma, and the Smoking Lesion Problem, the authors reveal in footnotes 7 and 16 that this is not their ultimate specification of the theory. In footnote 16, they state:

> "[T]he author's preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

We will refer to this policy-selection formulation of Functional Decision Theory as **P-FDT** (**Policy Functional Decision Theory**). 

The goal of this essay is to develop an explicit, mathematically rigorous account of P-FDT. We will formalize P-FDT’s policy optimization procedure, explain its conceptual departure from standard FDT, and detail how it manages subjunctive dependencies and counterfactuals without suffering from time inconsistency or epistemic distortion. Furthermore, we will show how P-FDT resolves dilemmas—such as Parfit’s Hitchhiker, the Transparent Newcomb Problem, and Mechanical Blackmail—by naturally integrating the global advantages of precommitment directly into the agent’s current, uncommitted decision rule.

---

## 2. Formal Framework: From Graphs to Subjunctive Dependencies

To formalize P-FDT, we must first establish the epistemic and graphical structures within which a functional agent operates.

### 2.1 Spaces and Variables
Let an environment be characterized by:
- A countable set of possible observation histories $\mathcal{X}$.
- A finite set of available physical actions $\mathcal{A}$.
- A countable set of physical outcomes $\mathcal{O}$.
- A bounded utility function $\mathcal{U}: \mathcal{O} \to \mathbb{R}$, yielding a real-valued utility variable $V \coloneqq \mathcal{U}(\Outcome)$.
- A policy space $\Pi \coloneqq \{ \pi : \mathcal{X} \to \mathcal{A} \}$, consisting of all deterministic mappings from observations to actions. (We discuss randomized policies in Section 5).

An agent maintains an epistemic world-model $M = (P, G)$. In the spirit of Pearl (2000), $P$ is a joint subjective probability distribution over a set of discrete or continuous random variables, and $G$ is a directed acyclic graph whose vertices represent variables and whose directed edges encode direct structural dependencies.

In CDT, $G$ is strictly causal: an edge $Y \to Z$ signifies that intervening on physical variable $Y$ physically brings about changes in $Z$. In FDT and P-FDT, $G$ is generalized to include **subjunctive dependencies** (as defined by Yudkowsky and Soares). Subjunctive dependencies subsume causal dependencies as a special case, but crucially track logical and computational constraints. If a physical process in the environment (such as a predictor's simulation, a biological twin's brain, or an automated program) computes or relies upon the output of the agent's mathematical decision routine, the corresponding node in $G$ is placed causally or logically downstream of the agent's functional code.

### 2.2 The Quined Functional Variable
A central technical insight of functional decision theories is that an agent running an algorithm $\mathcal{D}$ within a model $M = (P, G)$ must be able to reason about the output of $\mathcal{D}(P, G)$ without running into vicious infinite regress. As Yudkowsky and Soares observe, Kleene’s second recursion theorem guarantees that an algorithm can obtain its own mathematical description (its Gödel number or source code) via "quining."

In standard act-level FDT, the model contains an ensemble of parameterized nodes $\FDTvar(\underline{P}, \underline{G}, \underline{x})$ representing the output of the algorithm for each possible observation $x$. In **P-FDT**, the foundational object of intervention is not the localized evaluation at a specific $x$, but the **entire mapping** itself. 

Let $\mathbf{\Pi}^*$ denote the node in the subjunctive graph $G$ representing the agent’s global decision policy:
$$\mathbf{\Pi}^* \coloneqq \text{P-FDT}(\underline{P}, \underline{G})$$
Here, underlined terms represent dequoted constants: the agent feeds the static specification of its own Bayesian prior $P$ and graph $G$ into the formal variable representing its algorithm. The realization of $\mathbf{\Pi}^*$ is an element $\pi \in \Pi$.

---

## 3. Defining P-FDT: The Policy Selection Rule

We are now equipped to mathematically state the core operational rule of P-FDT, resolving the brief sketch provided in footnote 16 into a concrete optimization problem.

### 3.1 The P-FDT Optimization Criterion
An agent facing an environment with model $(P, G)$ and having observed an observation history $x \in \mathcal{X}$ does not optimize over acts $a \in \mathcal{A}$. Instead, the agent determines the optimal global policy $\pi^* \in \Pi$ by evaluating which policy yields the highest expected utility when imposed globally on the graph $G$ via Pearl's intervention operator $\Do$. Once the optimal policy $\pi^*$ is identified, the agent's concrete physical act is simply the evaluation of that policy on the current observation $x$.

Formally, we define the two-stage execution of P-FDT:

#### Definition 1 (Optimal Policy Selection)
The optimal policy $\pi^* \in \Pi$ for an agent with model $(P, G)$ is given by:
$$\pi^* = \text{P-FDT}_{\text{policy}}(P, G) \coloneqq \argmax_{\pi \in \Pi} \mathbb{E}\left(V \;\middle|\; \Do\left(\mathbf{\Pi}^* = \pi\right)\right) \tag{1}$$
where $\mathbb{E}\left(V \;\middle|\; \Do(\mathbf{\Pi}^* = \pi)\right)$ represents the expected value of utility $V$ computed over the interventional distribution:
$$P\left(\cdot \;\middle|\; \Do\left(\mathbf{\Pi}^* = \pi\right)\right)$$

#### Definition 2 (Action Execution)
Given an observed history $x \in \mathcal{X}$, the physical action executed by the P-FDT agent is:
$$\text{P-FDT}(P, G, x) \coloneqq \pi^*(x) \tag{2}$$
where $\pi^*$ is the policy selected by Equation (1).

### 3.2 Unpacking the Interventional Distribution
To compute Equation (1), we evaluate how the surgery $\Do(\mathbf{\Pi}^* = \pi)$ propagates through the subjunctive network $G$. 

In Pearl's structural causal semantics, setting a variable via $\Do(Y = y)$ replaces the structural equation determining $Y$ with the constant assignment $Y \leftarrow y$, severing incoming parental edges to $Y$ while propagating the assignment downstream along all directed paths emanating from $Y$.

In P-FDT, the graph $G$ contains directed paths from $\mathbf{\Pi}^*$ to:
1. The agent’s own physical action node $\Act$, mediated by the observation node $\Obs$:
   $$\Act = \mathbf{\Pi}^*(\Obs)$$
2. All environmental systems that model, simulate, or subjunctively depend on the agent’s decision process. For example, if a predictor predicts the agent’s policy or predicts the agent's action based on an observation the predictor expects the agent to make, that prediction node $\Var{Pred}$ is a descendant of $\mathbf{\Pi}^*$.

Crucially, the expectation in Equation (1) is **not conditioned on the agent’s actual observation $x$**:
$$\mathbb{E}\left(V \;\middle|\; \Do(\mathbf{\Pi}^* = \pi)\right) = \sum_{x' \in \mathcal{X}} \sum_{o \in \mathcal{O}} \mathcal{U}(o) \, P\left(\Obs = x', \Outcome = o \;\middle|\; \Do(\mathbf{\Pi}^* = \pi)\right)$$
The optimization is conducted from an **updateless prior perspective** over the policy space. 

This mathematical feature is the operational realization of the authors' remark in Section 9:
> "At first glance, it may seem like Fiona is ignoring information---shouldn't she update on the fact that she has seen the blackmail? ... Fiona does change her behavior in response to evidence, though---by changing *the place in her graph where she intervenes*."

In standard FDT, the agent conditions on $\Obs = x$ by intervening on the specific variable $\FDTvar(\underline{P}, \underline{G}, \underline{x})$. In P-FDT, the agent avoids intervening on a local, observation-conditioned node altogether; the agent intervenes on the function mapping $\mathbf{\Pi}^*$, evaluates its global consequence across all possible observations $x'$, and lets the current observation $x$ serve exclusively as the computational input to the selected policy $\pi^*$.

---

## 4. Comparing the Decision Criteria: EDT, CDT, FDT, and P-FDT

To appreciate the theoretical mechanics of P-FDT, it is instructive to compare how EDT, CDT, standard FDT, and P-FDT evaluate choices.

```
+---------------+------------------------+------------------------------------+-------------------------------------------+
| Theory        | Locus of Choice        | Hypothetical Operator              | Conditioning on Evidence Obs = x?         |
+---------------+------------------------+------------------------------------+-------------------------------------------+
| EDT           | Physical Act a in A    | P(- | Act = a, Obs = x)            | Yes (Bayesian conditionalization)         |
| CDT           | Physical Act a in A    | P(- | Do(Act = a), Obs = x)        | Yes (Intervene on Act, condition on Obs)  |
| Standard FDT  | Functional Act a in A  | P(- | Do(fdt(M, x) = a))          | Implicit (Intervention point tracks Obs)  |
| P-FDT         | Global Policy pi in Pi | P(- | Do(Pi* = pi))                | No in policy selection; applied at act    |
+---------------+------------------------+------------------------------------+-------------------------------------------+
```

### 4.1 Evidential Decision Theory (EDT)
EDT selects an act based on Bayesian conditionalization:
$$\EDT(P, x) = \argmax_{a \in \mathcal{A}} \mathbb{E}\left(V \;\middle|\; \Obs = x, \Act = a\right)$$
Because EDT does not alter the graph structure, it conditions across non-causal and non-subjunctive correlations. As seen in the Smoking Lesion Problem and the Cosmic Ray Problem, EDT conflates correlation with causation, attempting to "manage the news" even when the correlation stems from an uncontrollable common cause (e.g., an arterial lesion).

### 4.2 Causal Decision Theory (CDT)
CDT severs non-causal correlations by intervening physically:
$$\CDT(P, G, x) = \argmax_{a \in \mathcal{A}} \mathbb{E}\left(V \;\middle|\; \Obs = x, \Do(\Act = a)\right)$$
While CDT resolves the Smoking Lesion Problem by holding the lesion fixed under $\Do(\Act = a)$, its surgery is physically local. In Newcomb's Problem, CDT holds the contents of Box B fixed because Box B is in the past and causally upstream of $\Act$. CDT cannot recognize that the predictor's past prediction is subjunctively linked to the agent's reasoning, causing Carl the CDT agent to two-box and walk away with only \$1,000.

### 4.3 Standard FDT vs. P-FDT
Standard FDT intervenes on the logical type of the agent's act under observation $x$:
$$\FDT(P, G, x) = \argmax_{a \in \mathcal{A}} \mathbb{E}\left(V \;\middle|\; \Do(\FDTvar(\underline{P}, \underline{G}, \underline{x}) = a)\right)$$
Standard FDT correctly recognizes that Newcomb's predictor simulates $\FDTvar(\underline{P}, \underline{G}, \underline{x})$, so intervening on this variable updates the prediction in the agent's hypothetical.

However, consider what happens in sequential or multi-stage problems where the agent's observation history $x$ is itself causally or subjunctively downstream of the predictor's simulation of the agent. In standard FDT, the agent's graph must bifurcate the decision algorithm into separate nodes for each possible observation (e.g., $\FDTpgv{full}$ and $\FDTpgv{empty}$, as in Figure 5(b) of the paper). 

While this mathematically yields the correct choice in single-agent problems, it introduces an interpretative tension: why should an agent treat its decisions under different sensory inputs as distinct mathematical functions? A computer program is a single entity $\pi: \mathcal{X} \to \mathcal{A}$.

**P-FDT** rectifies this tension. By framing the decision problem as Equation (1), P-FDT models the agent as choosing which complete program $\pi$ to compile and execute.

---

## 5. Formal Derivations in Classic Dilemmas

To make the mechanics of P-FDT concrete, we now step through its explicit mathematical derivations in three canonical problems: Newcomb's Problem, Parfit's Hitchhiker / Transparent Newcomb, and Mechanical Blackmail.

### 5.1 Newcomb's Problem
In standard Newcomb's Problem:
- Observations: $\mathcal{X} = \{ \emptyset \}$ (no informative prior observation).
- Actions: $\mathcal{A} = \{ \Val{onebox}, \Val{twobox} \}$.
- Policies: Since $|\mathcal{X}| = 1$, the policy space $\Pi$ is isomorphic to $\mathcal{A}$:
  $$\pi_1(\emptyset) = \Val{onebox}, \quad \pi_2(\emptyset) = \Val{twobox}$$

The graph $G$ contains the policy node $\mathbf{\Pi}^* \in \{ \pi_1, \pi_2 \}$. The predictor sets $\Var{Prediction} \in \{ \Val{1}, \Val{2} \}$ according to an accurate simulation of $\mathbf{\Pi}^*$:
$$P(\Var{Prediction} = \Val{1} \mid \Do(\mathbf{\Pi}^* = \pi_1)) = 0.99$$
$$P(\Var{Prediction} = \Val{2} \mid \Do(\mathbf{\Pi}^* = \pi_2)) = 0.99$$
Box B contains \$1,000,000 if $\Var{Prediction} = \Val{1}$, and \$0 if $\Var{Prediction} = \Val{2}$. Box A contains \$1,000 unconditionally.

The P-FDT agent evaluates the expected utility of the two policies:
$$\begin{aligned}
\mathbb{E}\left(V \;\middle|\; \Do(\mathbf{\Pi}^* = \pi_1)\right) &= 0.99(\$1,000,000) + 0.01(\$0) = \$990,000 \\
\mathbb{E}\left(V \;\middle|\; \Do(\mathbf{\Pi}^* = \pi_2)\right) &= 0.99(\$1,001,000) + 0.01(\$1,000) = \$11,000
\end{aligned}$$
Since $\$990,000 > \$11,000$, P-FDT selects policy $\pi^* = \pi_1$. 
Applying Equation (2), the physical action executed is:
$$\Act = \pi^*(\emptyset) = \Val{onebox}$$
P-FDT one-boxes, precisely matching the intuitive functional verdict while operating strictly over policy space.

---

### 5.2 Parfit's Hitchhiker and Transparent Newcomb
The power of P-FDT is most evident in problems where an agent's current state is contingent on a past prediction of how the agent would react upon reaching that state.

Consider **Parfit's Hitchhiker**:
- An agent is stranded in the desert ($\Var{State} = \Val{desert}$). If left behind, $V = -\$1,000,000$.
- A driver can transport the agent to the city ($\Var{State} = \Val{city}$).
- The driver detects honesty with $99\%$ accuracy. She gives the agent a ride if and only if she predicts that the agent, upon arriving in the city, will pay \$1,000.
- Observations at decision time: $\mathcal{X} = \{ \Val{city} \}$. (If left in the desert, the agent dies and makes no ATM decision).
- Actions: $\mathcal{A} = \{ \Val{pay}, \Val{refuse} \}$.

#### The Failure of CDT and EDT
A CDT agent who has arrived in the city conditions on $\Obs = \Val{city}$ and evaluates:
$$\mathbb{E}\left(V \;\middle|\; \Obs = \Val{city}, \Do(\Act = \Val{refuse})\right) = \$0$$
$$\mathbb{E}\left(V \;\middle|\; \Obs = \Val{city}, \Do(\Act = \Val{pay})\right) = -\$1,000$$
CDT chooses $\Val{refuse}$. The driver anticipates this and leaves the CDT agent to die. EDT reasons identically once in the city: learning that one paid is bad news regarding one's wealth, so EDT also refuses.

#### The P-FDT Solution
In P-FDT, the agent in the city does not maximize over the localized act space $\{ \Val{pay}, \Val{refuse} \}$. Instead, the agent maximizes over the policy space $\Pi = \{ \pi_{\Val{pay}}, \pi_{\Val{refuse}} \}$, where:
$$\pi_{\Val{pay}}(\Val{city}) = \Val{pay}, \quad \pi_{\Val{refuse}}(\Val{city}) = \Val{refuse}$$
The subjunctive graph $G$ models the driver’s past choice $\Var{Ride} \in \{ \Val{rescue}, \Val{abandon} \}$ as dependent on the driver’s simulation of the policy $\mathbf{\Pi}^*$:
$$P\left(\Var{Ride} = \Val{rescue} \;\middle|\; \Do(\mathbf{\Pi}^* = \pi_{\Val{pay}})\right) = 0.99$$
$$P\left(\Var{Ride} = \Val{rescue} \;\middle|\; \Do(\mathbf{\Pi}^* = \pi_{\Val{refuse}})\right) = 0.01$$
Now, P-FDT evaluates the expected global utility under each policy via Equation (1):

Under $\Do(\mathbf{\Pi}^* = \pi_{\Val{pay}})$:
$$\begin{aligned}
\mathbb{E}\left(V \;\middle|\; \Do(\mathbf{\Pi}^* = \pi_{\Val{pay}})\right) &= P(\Val{rescue}) \cdot \mathcal{U}(\Val{rescued} \land \Val{pay}) + P(\Val{abandon}) \cdot \mathcal{U}(\Val{abandoned}) \\
&= 0.99(-\$1,000) + 0.01(-\$1,000,000) \\
&= -\$990 - \$10,000 = -\$10,990
\end{aligned}$$

Under $\Do(\mathbf{\Pi}^* = \pi_{\Val{refuse}})$:
$$\begin{aligned}
\mathbb{E}\left(V \;\middle|\; \Do(\mathbf{\Pi}^* = \pi_{\Val{refuse}})\right) &= P(\Val{rescue}) \cdot \mathcal{U}(\Val{rescued} \land \Val{refuse}) + P(\Val{abandon}) \cdot \mathcal{U}(\Val{abandoned}) \\
&= 0.01(\$0) + 0.99(-\$1,000,000) \\
&= -\$990,000
\end{aligned}$$

Comparing the two global expectations:
$$-\$10,990 \gg -\$990,000$$
Therefore, P-FDT selects:
$$\pi^* = \pi_{\Val{pay}}$$
Having selected $\pi_{\Val{pay}}$, the agent in the city evaluates $\pi^*(\Val{city}) = \Val{pay}$. The agent withdraws the \$1,000 and hands it to the driver.

Notice the conceptual elegance of this mechanism: **the agent does not require an external, physical precommitment device**. P-FDT behaves *as if* it had precommitted, because it evaluates its decisions at the level of the mathematical rule that governs its behavior.

---

### 5.3 The Transparent Newcomb Problem
The Transparent Newcomb Problem (Dilemma 5 in the paper) is structurally isomorphic to Parfit's Hitchhiker. Both boxes are transparent: the agent directly observes whether Box B is full or empty before deciding whether to take one box or two.

- Observations: $\mathcal{X} = \{ \Val{full}, \Val{empty} \}$.
- Actions: $\mathcal{A} = \{ \Val{onebox}, \Val{twobox} \}$.
- The policy space consists of four functions:
  $$\Pi = \{ \pi_{11}, \pi_{12}, \pi_{21}, \pi_{22} \}$$
  where $\pi_{ij}(\Val{full}) = i$ and $\pi_{ij}(\Val{empty}) = j$.

The predictor fills Box B (\$1,000,000) iff she predicts that the agent adheres to a policy that leaves Box A (\$1,000) behind upon seeing that Box B is full. That is, the predictor tests whether the agent's policy satisfies:
$$\pi(\Val{full}) = \Val{onebox}$$
If the predictor's accuracy is $99\%$:
- For any policy $\pi$ with $\pi(\Val{full}) = \Val{onebox}$, Box B is filled with probability $0.99$.
- For any policy $\pi$ with $\pi(\Val{full}) = \Val{twobox}$, Box B is filled with probability $0.01$.

Furthermore, if Box B is empty, taking two boxes strictly dominates taking one box, so any optimal policy will set $\pi(\Val{empty}) = \Val{twobox}$. This leaves two serious candidate policies:
1. $\pi_{\text{coop}}$: $\pi(\Val{full}) = \Val{onebox}, \pi(\Val{empty}) = \Val{twobox}$.
2. $\pi_{\text{defect}}$: $\pi(\Val{full}) = \Val{twobox}, \pi(\Val{empty}) = \Val{twobox}$.

Let us calculate the P-FDT expected utility for each policy prior to observation:

For $\pi_{\text{coop}}$:
$$\begin{aligned}
\mathbb{E}\left(V \;\middle|\; \Do(\mathbf{\Pi}^* = \pi_{\text{coop}})\right) &= 0.99 \cdot \mathcal{U}(\Val{full}, \Val{onebox}) + 0.01 \cdot \mathcal{U}(\Val{empty}, \Val{twobox}) \\
&= 0.99(\$1,000,000) + 0.01(\$1,000) \\
&= \$990,000 + \$10 = \$990,010
\end{aligned}$$

For $\pi_{\text{defect}}$:
$$\begin{aligned}
\mathbb{E}\left(V \;\middle|\; \Do(\mathbf{\Pi}^* = \pi_{\text{defect}})\right) &= 0.01 \cdot \mathcal{U}(\Val{full}, \Val{twobox}) + 0.99 \cdot \mathcal{U}(\Val{empty}, \Val{twobox}) \\
&= 0.01(\$1,001,000) + 0.99(\$1,000) \\
&= \$10,010 + \$990 = \$11,000
\end{aligned}$$

P-FDT unambiguously selects $\pi^* = \pi_{\text{coop}}$. 

Now suppose the agent stands before the transparent boxes and observes $\Obs = \Val{full}$. What does the agent do? The agent applies the globally chosen policy to the current observation:
$$\Act = \pi^*(\Val{full}) = \Val{onebox}$$
The agent leaves the \$1,000 behind, despite seeing it through the transparent acrylic. 

Standard CDT decries this as irrational: "Box B is already full! Taking Box A cannot cause Box B to become empty!" But as Yudkowsky and Soares emphasize, CDT agents who reason this way find themselves standing in front of *empty* boxes 99% of the time. The P-FDT agent achieves \$990,010 in expectation because their decision rule is transparently predictable to the predictor.

---

### 5.4 Mechanical Blackmail
In the Mechanical Blackmail problem (Dilemma 8):
- An autonomous program runs if and only if a perfect predictor predicts that the agent would pay \$1,000 upon receiving a blackmail letter.
- If the program runs, it demands \$1,000; if unpaid within 24 hours, it releases damaging information costing the agent \$1,000,000.
- Observations: $\mathcal{X} = \{ \Val{letter}, \emptyset \}$.
- Actions: $\mathcal{A} = \{ \Val{pay}, \Val{refuse} \}$.

The policy space $\Pi$ includes:
- $\pi_{\Val{pay}}$: $\pi(\Val{letter}) = \Val{pay}$.
- $\pi_{\Val{refuse}}$: $\pi(\Val{letter}) = \Val{refuse}$.

Under P-FDT:
$$\begin{aligned}
\mathbb{E}\left(V \;\middle|\; \Do(\mathbf{\Pi}^* = \pi_{\Val{pay}})\right) &= -\$1,000 \\
\mathbb{E}\left(V \;\middle|\; \Do(\mathbf{\Pi}^* = \pi_{\Val{refuse}})\right) &= 0 \cdot (-\$1,000,000) + 1.0 \cdot (\$0) = \$0
\end{aligned}$$
P-FDT selects $\pi^* = \pi_{\Val{refuse}}$. 

Consequently, the blackmailer predicts the refusal, does not launch the program, and no letter is ever sent. If, due to an infinitesimal perturbation or error, a P-FDT agent does receive the letter ($\Obs = \Val{letter}$), the policy dictates:
$$\Act = \pi^*(\Val{letter}) = \Val{refuse}$$
The agent refuses to pay. By refusing on the counterfactual branch, P-FDT secures immunity in the actual world.

---

## 6. Open Problems, Ambiguities, and Operational Proposals

While the policy-selection model of P-FDT resolves the multi-node fragmentation of standard FDT, footnote 16 and the surrounding text leave several deep mathematical and philosophical questions open. Here we isolate these open problems, distinguish the source’s explicit claims from our own extensions, and offer concrete operational proposals.

### 6.1 What Is the Epistemic Status of Counter-to-Logic Counterfactuals?
A foundational problem raised by Yudkowsky and Soares in Section 3 is that evaluating $\Do(\mathbf{\Pi}^* = \pi)$ requires reasoning about **counterpossibles**—evaluating what the world would look like if a fixed mathematical algorithm had an output other than its true logical output. If $\text{P-FDT}(P, G) = \pi_1$, then $\mathbf{\Pi}^* = \pi_2$ is a logical contradiction. Standard probability theory conditioned on a contradiction collapses via the principle of explosion.

#### Operational Interpretation (Logical Inductors)
In our view, the most rigorous modern framework for formalizing this aspect of P-FDT (developed after the cited paper's precursors) is the **Logical Induction Criterion** of Garrabrant et al. (2016). A logical inductor assigns coherent, non-extreme subjective probabilities to mathematical sentences before their truth values are settled by deduction. 

In this framing, an agent represents its decision function as an unproven logical formula in a formal language (such as Peano Arithmetic). Prior to halting its deliberation, the agent assigns open probabilities $P(\mathbf{\Pi}^* = \pi) \in (0, 1)$ to each policy. Counterfactual evaluation under $\Do(\mathbf{\Pi}^* = \pi)$ is operationalized as surgery on the agent's logical network: we sever the formal derivation of $\mathbf{\Pi}^*$ from its axioms and set the sentence $\mathbf{\Pi}^* = \pi$ as an empirical premise, tracing downstream effects through statistical correlations that have been learned between algorithmic outputs and physical events.

### 6.2 The Specification of the Prior: When Is the Policy Evaluated?
Equation (1) optimizes the policy from an "updateless" perspective:
$$\argmax_{\pi \in \Pi} \sum_{x' \in \mathcal{X}} P(\Obs = x' \mid \Do(\mathbf{\Pi}^* = \pi)) \, \mathbb{E}\left(V \;\middle|\; \Do(\mathbf{\Pi}^* = \pi), \Obs = x'\right)$$
This raises a vital ambiguity: **which prior $P$ should be used?**

If the agent has lived for many years and accumulated an extensive observation history $e_{\text{past}}$ before facing Newcomb's problem, does the agent evaluate policy expected utility with respect to $P(\cdot)$ (the blank, initial prior at the beginning of time), or $P(\cdot \mid e_{\text{past}})$?

#### The Proposed Resolution (Counterfactual Updating)
We propose that P-FDT must employ **Counterfactual Updatelessness**:
1. All environmental evidence that is **subjunctively independent** of the policy $\mathbf{\Pi}^*$ (such as physical constants, historical facts occurring before the agent's creation that no predictor could have conditioned on, and background laws of nature) should be conditioned on via standard Bayesian updating:
   $$P_{\text{base}}(\cdot) = P(\cdot \mid e_{\text{independent}})$$
2. All observations that are **subjunctively dependent** on $\mathbf{\Pi}^*$ (such as whether a letter was received, whether Box B is full, or whether a twin cooperated) must **not** be conditioned on prior to the maximization in Equation (1). They must remain stochastic variables inside the interventional expectation.

This ensures that the agent utilizes all genuine, immutable empirical knowledge about the laws of the universe while preserving the subjunctive flexibility that allows FDT agents to coordinate with predictors and twins.

### 6.3 Randomized Policies and Mixed Strategies
In games of conflict (such as the Death in Damascus dilemma in Section 8), a deterministic policy $\pi: \mathcal{X} \to \mathcal{A}$ may permit an adversary or predictor to anticipate and thwart the agent completely.

While the source document briefly notes that Carl the CDT agent fails when using pseudorandomness because he treats it as uncorrelated with Death's prediction, it does not explicitly define stochastic policies for P-FDT.

#### Extension to Stochastic P-FDT
We can cleanly extend P-FDT to stochastic policies by expanding the policy space to the simplex of conditional probability distributions:
$$\Pi_{\Delta} \coloneqq \{ \pi : \mathcal{X} \to \Delta(\mathcal{A}) \}$$
where $\pi(a \mid x)$ represents the probability of executing action $a$ given observation $x$. 

In this case, the subjunctive dependency between $\mathbf{\Pi}^*$ and a predictor operates at the level of the distribution $\pi$. When Death reads the appointment book in Damascus, Death can predict the exact probability distribution $\pi \in \Pi_{\Delta}$ that the agent implements. If the agent's policy is to randomize 50/50 between Damascus and Aleppo using an internal quantum device or cryptographically secure pseudorandom generator that Death cannot physically predict prior to execution, the agent's policy optimization will account for Death setting his prediction based on $\pi$. 

As shown by Yudkowsky and Soares, when Carl is offered a truly random coin in Death in Damascus, Carl values it at \$0 because his CDT hypotheticals treat Death's location as independent of his choice. In contrast, a P-FDT agent optimizing over $\Pi_{\Delta}$ immediately recognizes that choosing a policy that randomizes with a genuinely unpredictable device secures a $50\%$ chance of survival (\$500,000 in expectation), and will readily pay \$1 to acquire it.

---

## 7. Operationalizing P-FDT: An Algorithmic Recipe for Unfamiliar Cases

To enable a mathematically literate reader to apply P-FDT to any unfamiliar decision problem, we synthesize the framework into an explicit, step-by-step decision procedure:

```
Algorithm: P-FDT Decision Procedure
Input: Epistemic distribution P, Subjunctive Graph G, Current Observation x_actual
Output: Physical Action a_star

1. Identify Variables:
   - Identify the observation space X and action space A.
   - Form the policy space Pi = { pi : X -> A }.
   - Identify the utility variable V = U(Outcome).

2. Map Subjunctive Dependencies:
   - Construct graph G by adding directed edges from the global policy node Pi* 
     to any node representing:
       a) Physical Act: Act = Pi*(Obs)
       b) Predictors / Models: Any environmental variable that simulates, 
          predicts, or mirrors the agent's reasoning.
       c) Twins / Copies: Any other agent running the same decision procedure.

3. Interventional Counterfactual Evaluation:
   - For each policy pi in Pi:
       a) Apply the graph surgery Do(Pi* = pi).
       b) Compute the interventional joint distribution:
          P(Obs = x, Outcome = o | Do(Pi* = pi))
       c) Calculate the global expected utility:
          EU(pi) = \sum_{x in X} \sum_{o in O} U(o) * P(Obs = x, Outcome = o | Do(Pi* = pi))

4. Policy Selection:
   - Select the optimal global policy:
     pi_star = argmax_{pi in Pi} EU(pi)

5. Execution:
   - Evaluate pi_star on the actual current observation:
     a_star = pi_star(x_actual)
   - Return a_star.
```

---

## 8. Conclusion

Policy Functional Decision Theory (P-FDT) represents the natural conceptual culmination of the functional approach to rationality envisioned by Yudkowsky and Soares. Standard decision theories fail because they misidentify the locus of choice: CDT intervenes on the physical act token, severing logical invariants and falling prey to predictors; EDT conditions on the act token, confusing mere correlation with agency and falling prey to news-management and blackmail.

Standard FDT corrects this by intervening on the mathematical function representing the agent's choice, but when applied purely at the level of observation-conditioned acts, it leaves the agent conceptually fragmented across multiple observation nodes. 

As hinted in footnote 16 and fully developed here, **P-FDT elevates the intervention to the global policy itself**. By evaluating policies from an updateless, subjunctive perspective, P-FDT harmonizes the benefits of precommitment, optimal information valuation, and game-theoretic deterrence into a single, time-consistent normative criterion. An agent following P-FDT does not need to bind her hands, blind her eyes, or regret her rationality: she simply identifies the decision rule that it would be best for an agent of her kind to embody, and executes it.

---

## References

- Adams, Ernest W. 1970. "Subjunctive and Indicative Conditionals." *Foundations of Language* 6 (1): 89–94.
- Ahmed, Arif. 2014. *Evidence, Decision and Causality*. Cambridge University Press.
- Arntzenius, Frank. 2008. "No Regrets, or: Edith Piaf Revamps Decision Theory." *Erkenntnis* 68 (2): 277–297.
- Dai, Wei. 2009. "Towards a New Decision Theory." *LessWrong*.
- Drescher, Gary L. 2006. *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
- Eells, Ellery. 1984. "Metatickles and the Dynamics of Deliberation." *Theory and Decision* 17 (1): 71–95.
- Garrabrant, Scott, Tsvi Benson-Tilsen, Andrew Critch, Nate Soares, and Jessica Taylor. 2016. "Logical Induction." *arXiv preprint arXiv:1609.03543*.
- Gauthier, David. 1994. "Assure and Threaten." *Ethics* 104 (4): 690–721.
- Gibbard, Allan, and William L. Harper. 1978. "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, edited by C. A. Hooker, J. J. Leach, and E. F. McClennen, 13:125–164. Reidel.
- Jeffrey, Richard C. 1983. *The Logic of Decision*. 2nd ed. University of Chicago Press.
- Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Joyce, James M. 2012. "Regret and Instability in Causal Decision Theory." *Synthese* 187 (1): 123–145.
- Kleene, Stephen Cole. 1938. "On Notation for Ordinal Numbers." *Journal of Symbolic Logic* 3 (4): 150–155.
- Lewis, David. 1979. "Prisoners' Dilemma is a Newcomb Problem." *Philosophy & Public Affairs* 8 (3): 235–240.
- Lewis, David. 1981. "Causal Decision Theory." *Australasian Journal of Philosophy* 59 (1): 5–30.
- Nozick, Robert. 1969. "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel*, edited by Nicholas Rescher, 114–146. Reidel.
- Parfit, Derek. 1986. *Reasons and Persons*. Oxford University Press.
- Pearl, Judea. 2000. *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
- Skyrms, Brian. 1980. *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
- Soares, Nate, and Benja Fallenstein. 2015. "Toward Idealized Decision Theory." *arXiv preprint arXiv:1507.01986*.
- Spohn, Wolfgang. 2012. "Reversing 30 Years of Discussion: Why Causal Decision Theorists Should One-Box." *Synthese* 187 (1): 95–122.
- Yudkowsky, Eliezer. 2010. "Timeless Decision Theory." *Machine Intelligence Research Institute Technical Report*.
- Yudkowsky, Eliezer, and Nate Soares. 2017. "Functional Decision Theory: A New Theory of Instrumental Rationality." *arXiv preprint arXiv:1710.05060v2*.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/a13e203f-4b99-40f8-8d1e-19404a2c195a/call_0/request.json)

[Authoritative raw response](../../../../../../runs/a13e203f-4b99-40f8-8d1e-19404a2c195a/call_0/response.raw) · finish: `stop`

### Visible response

````text
```text
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Setup**

I'm currently focused on dissecting the Prisoner's Dilemma scenario involving two instances of the same LLM running P-FDT. I'm reviewing the setup, specifically the independence of the two LLM executions and their identical nature. I need to fully grasp the nuances of this shared computational architecture.


**Clarifying the Framework**

I am now clarifying the Prisoner's Dilemma payoff structure within the P-FDT context. I've defined actions (pass or submit), and outcomes for the specific symmetric game. Understanding the private observations and how they affect the shared utility of years imprisoned, which is the negative of the years. I'm focusing on how P-FDT evaluates policies, particularly the intervention on the global policy node, and confirming the other prisoner's independent, identical LLM execution.


```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/a13e203f-4b99-40f8-8d1e-19404a2c195a/call_1/request.json)

[Authoritative raw response](../../../../../../runs/a13e203f-4b99-40f8-8d1e-19404a2c195a/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Dilemma**

I'm now contemplating a Prisoner's Dilemma scenario involving two LLMs. Each model shares identical characteristics: same weights, settings, decision theory (P-FDT), and initial essay. The core of my analysis focuses on the interplay and potential outcomes of this setup. I'm exploring how these shared attributes affect the strategic choices the models might make.


**Examining the Symmetry**

I'm now zeroing in on the implications of the agents receiving differing, yet structurally equivalent, private observations. This is critical. Both models, even with distinct "names" and "leads," face identical decision algorithms and symmetric payoff tables. My focus is on how this symmetry, coupled with P-FDT, influences their strategic choices - particularly around cooperation versus defection. I'm exploring the mapping of observations to actions within this framework.


```
