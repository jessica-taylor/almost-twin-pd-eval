# 028_fdt_policy_google_gemini-3.8-flash_rlow_plow / 00018

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/0e014b58-a6dd-4076-b766-c16112a6ac48/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/0e014b58-a6dd-4076-b766-c16112a6ac48/call_0/response.raw) · finish: `stop`

### Visible response

````text
# Policy Functional Decision Theory: Foundations, Formalisms, and Applications

## 1. Introduction: From Acts to Algorithms to Policies

Standard normative decision theory has long been divided between Causal Decision Theory (CDT) and Evidential Decision Theory (EDT). The standard debate typically revolves around Newcomblike dilemmas, where an agent’s physical choices correlate with background conditions or past predictions without directly causing them. In Newcomb's Problem, CDT takes two boxes because past predictions cannot be causally altered by present actions; EDT takes one box because taking one box provides good news about the contents of the opaque box. In the Smoking Lesion Problem, CDT smokes because the common cause (the lesion) is outside the agent's causal reach; EDT irrationally refrains from smoking in an attempt to "manage the news."

To reconcile these divergent failures, Yudkowsky and Soares (2017) introduce **Functional Decision Theory (FDT)**. FDT holds that rational choice centers on selecting the output of a *fixed mathematical decision function*, rather than choosing a physical act. When evaluating alternatives, an FDT agent does not ask what happens if their physical limbs move differently while holding the past fixed (CDT), nor what news is conveyed by their act (EDT). Instead, an FDT agent asks: *What would happen if this very mathematical decision procedure yielded a different output?*

In the main text of Yudkowsky and Soares (2017), FDT is predominantly formalized as choosing an *action* $a \in \mathcal{A}$ under a counterfactual intervention on the agent's decision algorithm for their specific, observed history $x$. However, in footnote 16 (and earlier in footnote 7), the authors introduce an alternative, strictly more general formulation:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions... As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action." (Yudkowsky & Soares 2017, Footnotes 7 & 16)

We designate this preferred formulation **Policy Functional Decision Theory (P-FDT)**. 

While Yudkowsky and Soares set P-FDT aside in their main text for ease of exposition—claiming that action-level FDT and P-FDT coincide in many single-agent problems—the distinction between selecting an action conditional on current observations and selecting an optimal global policy is of profound mathematical and conceptual importance. P-FDT unites the "updateless" perspective of Updateless Decision Theory (Dai 2009) with the structural calculus of Pearlian causal and logical networks.

This essay provides a rigorous mathematical exposition of P-FDT. We formalize the space of policies, define the evaluation of counterfactual dependencies via functional interventions, resolve the technical ambiguities left open in footnote 16, and demonstrate how P-FDT operates across standard, asymmetric, and multi-agent decision problems.

---

## 2. Theoretical Foundations: Subjunctive Dependence and Quining

Before formalizing the policy selection operator, we must understand the semantic framework underlying functional decision theories: **subjunctive dependence**.

### 2.1 Causal vs. Subjunctive Dependence

In standard causal graphical models (Pearl 2000), dependencies between random variables are parameterized by directed acyclic graphs (DAGs), where directed edges denote direct physical causation. An intervention $\Do(X = x)$ represents an idealized physical disruption: it severs all incoming arrows to $X$ in the graph while preserving all downstream functional relationships.

CDT restricts its counterfactual evaluations to physical interventions on the agent's token action node $\Act$:
$$\CDT(P, G, x) = \argmax_{a \in \mathcal{A}} \mathbb{E}_P\left[ \mathcal{V} \mid \Do(\Act = a), \Obs = x \right].$$
Consequently, CDT holds fixed all events that are not physically downstream of $\Act$. In Newcomb's Problem, because the predictor's past prediction $\Var{Prediction}$ is causally upstream of the present act $\Act$, the edge $\Var{Prediction} \to \Var{Box\ B}$ is unaffected by $\Do(\Act = a)$. Carl (the CDT agent) thus views the contents of Box B as invariant under his choice, deduces that two-boxing dominates one-boxing, and walks away poor.

FDT and P-FDT observe that physical causation is merely a special case of a broader class of dependencies: *subjunctive dependence*. Two physical systems subjunctively depend upon one another when their states are determined by the evaluation of the same mathematical function. If two calculators compute $6288 + 1048$, their outputs are identical not because a physical wire connects them across space, but because they instantiate the same arithmetic mapping. If a predictor constructs a high-fidelity simulation or psychological model of an agent, the predictor's forecast and the agent's eventual choice subjunctively depend on the *type* of the agent's decision algorithm.

### 2.2 Quining and Functional Nodes

To model subjunctive dependence within an extended graphical formalism, an agent’s internal world-model must incorporate random variables representing the outputs of mathematical algorithms. Let $\mathcal{L}$ denote a rich formal language capable of arithmetic and self-reference. By Kleene’s Second Recursion Theorem (Kleene 1938), an algorithm can manipulate a quote or blueprint of its own source code (a technique informally known as "quining").

In P-FDT, the world-model $M = (P, G)$ contains an explicit functional variable:
$$\Pi^* \equiv \Var{pfdt}(\underline{P}, \underline{G}),$$
where the underlined arguments indicate syntactic quotation (Gödel encoding) of the agent’s own belief distribution $P$ and subjunctive graph $G$. The variable $\Pi^*$ takes values in a set of candidate policies $\mathcal{F} = \{ \pi : \mathcal{X} \to \mathcal{A} \}$.

Subjunctive dependence is encoded directly into the extended graph $G$:
1. The agent's physical action node $\Act$ has incoming edges from the functional node $\Pi^*$ and the observation node $\Obs$, satisfying $\Act = \Pi^*(\Obs)$.
2. Any external process that simulates, predicts, or mirrors the agent’s decision process (e.g., Newcomb's predictor, psychological twins, blackmailers) also receives a directed edge from $\Pi^*$.

Intervening on $\Pi^*$ corresponds to asking: *What would happen if the mathematical algorithm implemented by my decision procedure were defined to return policy $\pi$?*

---

## 3. Mathematical Formalization of P-FDT

Footnote 16 defines P-FDT by stating that an agent intervenes on the function node to select a policy mapping inputs to actions, and subsequently applies the selected policy to her actual observations. Here, we make this procedure mathematically precise and address the foundational questions regarding priors, observations, and policy spaces that the source leaves open.

### 3.1 Formal Architecture

Let:
- $\mathcal{X}$ be a countable set of possible observation histories (information sets).
- $\mathcal{A}$ be a finite set of available base actions.
- $\mathcal{O}$ be a countable set of possible outcomes, equipped with a bounded utility function $\mathcal{U} : \mathcal{O} \to \mathbb{R}$. We denote the random variable $\mathcal{U}(\Outcome)$ by $\mathcal{V}$.
- $\mathcal{F} \subseteq \mathcal{A}^{\mathcal{X}}$ be the space of deterministic policies $\pi : \mathcal{X} \to \mathcal{A}$. (We address stochastic policies in Section 3.4.)
- $M = (P, G)$ be the agent's world-model, where $P$ is a joint probability distribution over the variables in $G$, and $G$ is a directed acyclic graph encoding causal and logical/subjunctive dependencies.

Within $G$, let $\Obs$ be the observation variable taking values in $\mathcal{X}$, and let $\Act$ be the physical action variable taking values in $\mathcal{A}$. The physical execution of an action is governed by the structural equation:
$$\Act = \Pi^*(\Obs).$$

Any predictor $\Var{Pred}$ that accurately models the agent does not merely predict the token action $\Act$; the predictor inspects or simulates the policy $\Pi^* = \Var{pfdt}(\underline{P}, \underline{G})$. Thus, in $G$, the node $\Pi^*$ has directed paths to $\Var{Pred}$ as well as to $\Act$.

### 3.2 The Policy Optimization Rule

How should an agent evaluate a policy $\pi \in \mathcal{F}$?

In standard (act-based) FDT, an agent receiving observation $x$ calculates:
$$\FDT(P, G, x) = \argmax_{a \in \mathcal{A}} \mathbb{E}_P \left[ \mathcal{V} \mid \Do\left(\FDTvar(\underline{P}, \underline{G}, \underline{x}) = a\right) \right].$$
As demonstrated in Section 6 of Yudkowsky and Soares (2017), when observations are received, act-based FDT responds by *shifting the node of intervention* to $\FDTvar(\dots, \underline{x})$ while refusing to condition on $\Obs = x$ inside the expectation. While this ad-hoc procedure prevents the agent from falling into the traps that plague CDT and EDT, it requires the graph to contain distinct nodes $\FDTvar(\dots, \underline{x})$ for every possible observation $x \in \mathcal{X}$, with the choice of intervention node controlled by an external meta-rule.

P-FDT resolves this inelegance by unifying evaluation into a single, global optimization over policies. We define the P-FDT decision procedure via a two-stage process:

#### Stage 1: Global Policy Selection
The agent identifies the optimal policy $\pi^* \in \mathcal{F}$ by evaluating the counterfactual consequences of setting the global decision function $\Pi^*$ to candidate policies $\pi$:

$$\pi^* = \PBDT(P, G) \coloneqq \argmax_{\pi \in \mathcal{F}} \mathbb{E}_P \left[ \mathcal{V} \mid \Do\left(\Pi^* = \pi\right) \right].$$

Here, the expectation is taken with respect to the agent’s *prior* or *subjunctive-base* distribution $P$, without conditioning on the realized observation $x$. The causal/logical intervention $\Do(\Pi^* = \pi)$ severs incoming arrows to $\Pi^*$ and propagates the assignment throughout $G$:
- The predictor $\Var{Pred}$ responds to the global policy $\pi$.
- The observation $\Obs$ is generated according to the environmental dynamics under $\pi$.
- The action $\Act$ evaluates to $\pi(\Obs)$.
- The outcome $\Outcome$ and utility $\mathcal{V}$ are computed from the resulting graph state.

#### Stage 2: Action Execution
Upon identifying the optimal policy $\pi^*$, the agent executes the action prescribed by $\pi^*$ for the observation $x$ actually encountered:
$$\PBDT_{\text{act}}(P, G, x) \coloneqq \pi^*(x).$$

```
        +------------------------------------------------+
        |                 P-FDT PIPELINE                 |
        +------------------------------------------------+
                               |
               [World Model: M = (P, G)]
                               |
                               v
            +------------------------------------+
            |      Stage 1: Policy Selection     |
            |                                    |
            |   Evaluate each policy π in F via: |
            |      E[ V | do(Π* = π) ]           |
            |                                    |
            |   Select:                          |
            |      π* = argmax E[ V | do(Π* = π) ]|
            +------------------------------------+
                               |
                               v
            +------------------------------------+
            |     Stage 2: Policy Execution      |
            |                                    |
            |   Observe actual history: Obs = x  |
            |   Execute action:                  |
            |      a* = π*(x)                    |
            +------------------------------------+
```

### 3.3 Resolving Footnote 16: Priors, Updatelessness, and the "Empty" History

Footnote 16 leaves several mathematical choices unresolved:
1. *From what epistemic state is the expectation evaluated?* Does the agent evaluate $\mathbb{E}[\mathcal{V} \mid \dots]$ using her prior distribution $P$ or a distribution conditioned on $x$?
2. *How are observations treated if the agent selects a policy before or after observing $x$?*
3. *What constitutes the space $\mathcal{F}$ when $\mathcal{X}$ is continuous or infinite?*

We provide the following interpretations and proposals to complete the theory:

#### Operational Proposal 1: The Principle of Radical Updatelessness
If the agent conditioned the expectation in Stage 1 on her current observation $x$—computing $\argmax_\pi \mathbb{E}[\mathcal{V} \mid \Do(\Pi^* = \pi), \Obs = x]$—she would re-introduce the exact pathologies P-FDT is designed to eliminate. If an agent has already conditioned on having received a blackmail letter, she can no longer incentivize the blackmailer not to send the letter in counterfactual branches where her policy rejects blackmail. 

Therefore, in P-FDT, **the policy evaluation must be updateless**: the expectation $\mathbb{E}_P[\mathcal{V} \mid \Do(\Pi^* = \pi)]$ is evaluated with respect to the agent’s *prior* (or root) distribution $P$, representing her beliefs before receiving the observation $x$ that triggered the choice. The observation history $x$ is not an epistemic constraint on the evaluation of $\Pi^*$; it is merely the input supplied to $\pi^*$ at the moment of execution.

#### Operational Proposal 2: The Counterfactual Information Graph
When $\Do(\Pi^* = \pi)$ is applied, the probability of encountering observation $x$ is endogenous to the policy:
$$P(\Obs = x \mid \Do(\Pi^* = \pi)).$$
Expanding the Stage 1 objective function makes this explicit:
$$\mathbb{E}_P \left[ \mathcal{V} \mid \Do(\Pi^* = \pi) \right] = \sum_{x \in \mathcal{X}} P(\Obs = x \mid \Do(\Pi^* = \pi)) \cdot \mathbb{E}_P \left[ \mathcal{V} \mid \Do(\Pi^* = \pi), \Obs = x \right].$$
This equation reveals the mathematical mechanics of P-FDT: a policy is rewarded not only for how it performs when an observation is realized, but for its capacity to *prevent* bad observations from occurring in the first place.

#### Operational Proposal 3: Deterministic vs. Stochastic Policies
If the environment or the predictor is sensitive to randomization, the policy space $\mathcal{F}$ can be generalized to Markov kernels $\pi : \mathcal{X} \to \Delta(\mathcal{A})$, where $\Delta(\mathcal{A})$ is the simplex of probability distributions over $\mathcal{A}$. An intervention $\Do(\Pi^* = \pi)$ sets the conditional probability distribution of $\Act$ given $\Obs$ to $\pi(a \mid x)$. In this essay, unless otherwise specified, we restrict our focus to pure policies $\mathcal{F} = \mathcal{A}^{\mathcal{X}}$.

---

## 4. Classic Decision Problems Revisited under P-FDT

To observe P-FDT in practice, we examine how it resolves classic decision-theoretic dilemmas, comparing its mechanics to CDT, EDT, and act-based FDT.

### 4.1 Newcomb's Problem

Recall the setup: Box A contains \$1,000; Box B contains \$1,000,000 or \$0. A 99% reliable predictor fills Box B iff she predicted the agent leaves Box A behind.

- $\mathcal{X} = \{ \emptyset \}$ (no informative observation prior to choice).
- $\mathcal{A} = \{ \Val{onebox}, \Val{twobox} \}$.
- Policies $\mathcal{F} = \{ \pi_1, \pi_2 \}$, where $\pi_1(\emptyset) = \Val{onebox}$ and $\pi_2(\emptyset) = \Val{twobox}$.

Because $\Pi^*$ has a directed edge to $\Var{Prediction}$ in $G$, the intervention $\Do(\Pi^* = \pi)$ alters the distribution of $\Var{Prediction}$:
- Under $\Do(\Pi^* = \pi_1)$: $P(\Var{Box\ B} = \Val{full} \mid \Do(\Pi^* = \pi_1)) = 0.99$.
  $$\mathbb{E}[\mathcal{V} \mid \Do(\Pi^* = \pi_1)] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000.$$
- Under $\Do(\Pi^* = \pi_2)$: $P(\Var{Box\ B} = \Val{full} \mid \Do(\Pi^* = \pi_2)) = 0.01$.
  $$\mathbb{E}[\mathcal{V} \mid \Do(\Pi^* = \pi_2)] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$

P-FDT selects $\pi_1$ and executes $\pi_1(\emptyset) = \Val{onebox}$. Here, P-FDT trivially reproduces the prescription of act-based FDT, because the observation space is trivial.

### 4.2 The Smoking Lesion Problem

In the Smoking Lesion Problem, an arterial lesion causes both a predisposition toward smoking and lung cancer (which costs \$1,000,000 in utility), but smoking itself yields an intrinsic utility of \$1,000 and has no direct causal link to cancer.

- $\mathcal{X} = \{ \emptyset \}$.
- $\mathcal{A} = \{ \Val{smoke}, \Val{refrain} \}$.
- Policies $\mathcal{F} = \{ \pi_S, \pi_R \}$, where $\pi_S(\emptyset) = \Val{smoke}$ and $\pi_R(\emptyset) = \Val{refrain}$.

In the graph $G$, $\Var{Lesion}$ is a biological condition determined prior to deliberation. Critically, **the lesion is not a predictor**. The lesion does not simulate or evaluate the mathematical function $\Pi^*$; it merely influences the emotional preferences of the agent. Thus, there is no directed arrow from $\Pi^*$ to $\Var{Lesion}$ in $G$.

When evaluating the policy intervention:
$$P(\Var{Lesion} = \Val{present} \mid \Do(\Pi^* = \pi_S)) = P(\Var{Lesion} = \Val{present}) = p.$$
The probability of cancer remains $p(0.99) + (1-p)(0.01)$, completely invariant under $\Do(\Pi^* = \pi)$. 
Evaluating expected utility:
$$\mathbb{E}[\mathcal{V} \mid \Do(\Pi^* = \pi_S)] = \mathbb{E}[\mathcal{V} \mid \Do(\Pi^* = \pi_R)] + \$1,000.$$
P-FDT identifies $\pi^* = \pi_S$ and smokes. P-FDT successfully avoids EDT's irrational self-denial because its intervention on $\Pi^*$ respects the absence of subjunctive dependence between the decision algorithm and non-predictive physical traits.

---

## 5. The True Test: Transparent Newcomb and Mechanical Blackmail

The distinct advantages of P-FDT become unmistakable when an agent receives informative observations that reveal information about past predictions.

### 5.1 The Transparent Newcomb Problem

In Drescher's Transparent Newcomb Problem, Box B is transparent: the agent can visually observe whether Box B is full or empty before deciding whether to take Box A. A 99% accurate predictor placed \$1,000,000 in Box B iff she predicted that the agent, *upon observing two full boxes*, would leave Box A behind.

- Observation space: $\mathcal{X} = \{ \Val{full}, \Val{empty} \}$.
- Action space: $\mathcal{A} = \{ \Val{onebox}, \Val{twobox} \}$.
- The policy space consists of four functions $\pi_{(a_f, a_e)}$ mapping $\Val{full} \mapsto a_f$ and $\Val{empty} \mapsto a_e$:
  $$\mathcal{F} = \{ \pi_{11}, \pi_{12}, \pi_{21}, \pi_{22} \},$$
  where $\pi_{12}$ denotes "one-box if full, two-box if empty."

#### CDT and EDT's Analysis
Suppose the agent observes $\Obs = \Val{full}$.
- **CDT**: Carl conditions on $\Obs = \Val{full}$. Intervening via $\Do(\Act = a)$, Box B is already full. Taking both boxes yields \$1,001,000, while taking Box B alone yields \$1,000,000. CDT takes two boxes. Because Carl is predictably a two-boxer, the predictor leaves Box B empty 99% of the time.
- **EDT**: Eve conditions on $\Obs = \Val{full}$. Since Box B is already known to contain \$1,000,000, conditioning on taking Box A gives no further news about Box B’s contents. Eve also takes two boxes!

#### P-FDT's Analysis
P-FDT does not evaluate an act after conditioning on $\Obs = \Val{full}$. Instead, P-FDT solves Stage 1 over the policy space $\mathcal{F}$ using the root distribution $P$:

$$\mathbb{E}[\mathcal{V} \mid \Do(\Pi^* = \pi)] = \sum_{x \in \{ \Val{full}, \Val{empty} \}} P(\Obs = x \mid \Do(\Pi^* = \pi)) \cdot \mathbb{E}[\mathcal{V} \mid \Do(\Pi^* = \pi), \Obs = x].$$

The predictor's model simulates the agent's policy $\Pi^*$. Specifically, the predictor evaluates what $\Pi^*$ outputs on input $\Val{full}$:
- If $\pi(\Val{full}) = \Val{onebox}$, the predictor sets Box B to full with 99% probability:
  $$P(\Obs = \Val{full} \mid \Do(\Pi^* = \pi)) = 0.99, \quad P(\Obs = \Val{empty} \mid \Do(\Pi^* = \pi)) = 0.01.$$
- If $\pi(\Val{full}) = \Val{twobox}$, the predictor sets Box B to full with only 1% probability:
  $$P(\Obs = \Val{full} \mid \Do(\Pi^* = \pi)) = 0.01, \quad P(\Obs = \Val{empty} \mid \Do(\Pi^* = \pi)) = 0.99.$$

Now we compare the candidate policies:

1. **Policy $\pi_{12}$ (One-box if full; Two-box if empty)**:
   $$\begin{aligned}
   \mathbb{E}[\mathcal{V} \mid \Do(\Pi^* = \pi_{12})] &= 0.99 \cdot \mathcal{U}(\Val{onebox}, \Val{full}) + 0.01 \cdot \mathcal{U}(\Val{twobox}, \Val{empty}) \\
   &= 0.99(\$1,000,000) + 0.01(\$1,000) \\
   &= \$990,000 + \$10 = \$990,010.
   \end{aligned}$$

2. **Policy $\pi_{22}$ (Two-box under all circumstances)**:
   $$\begin{aligned}
   \mathbb{E}[\mathcal{V} \mid \Do(\Pi^* = \pi_{22})] &= 0.01 \cdot \mathcal{U}(\Val{twobox}, \Val{full}) + 0.99 \cdot \mathcal{U}(\Val{twobox}, \Val{empty}) \\
   &= 0.01(\$1,001,000) + 0.99(\$1,000) \\
   &= \$10,010 + \$990 = \$11,000.
   \end{aligned}$$

Comparing all four policies, $\pi_{12}$ is uniquely optimal:
$$\pi^* = \argmax_{\pi \in \mathcal{F}} \mathbb{E}[\mathcal{V} \mid \Do(\Pi^* = \pi)] = \pi_{12}.$$

#### Execution (Stage 2)
The agent opens her eyes and observes $\Obs = \Val{full}$. She executes:
$$\Act = \pi^*(\Val{full}) = \Val{onebox}.$$
She leaves the \$1,000 behind.

Notice the conceptual elegance of P-FDT: There is no need for the convoluted retrocausal-sounding rationalizations that act-based FDT agents must construct (e.g., "If I two-boxed right now while seeing a full box, I would have to be in a world where the box was empty"). Under P-FDT, the agent's reasoning is straightforwardly forward-looking and counterfactually coherent: *I am executing policy $\pi_{12}$ because committing my algorithmic type to $\pi_{12}$ is what caused the box to be full with 99% probability in the first place.*

### 5.2 The Mechanical Blackmail

In the Mechanical Blackmail dilemma (Soares and Fallenstein 2015), an extortionist runs an automated, irreversible script that will publish damaging secrets costing the agent \$1,000,000 unless the agent pays \$1,000 within 24 hours. The blackmailer is an accurate predictor: she only launches the program and delivers the demand if she predicts the agent will pay upon receiving the letter.

- $\mathcal{X} = \{ \Val{letter}, \emptyset \}$.
- $\mathcal{A} = \{ \Val{pay}, \Val{refuse} \}$.
- Policies $\mathcal{F} = \{ \pi_{\Val{pay}}, \pi_{\Val{refuse}} \}$, where $\pi_{\Val{pay}}(\Val{letter}) = \Val{pay}$ and $\pi_{\Val{refuse}}(\Val{letter}) = \Val{refuse}$. (Assume both default to an inert action given $\emptyset$).

#### Evaluation under P-FDT
Let the blackmailer's prediction accuracy be $1 - \epsilon$. The blackmailer simulates the agent's policy $\Pi^*$:
- Under $\Do(\Pi^* = \pi_{\Val{pay}})$: The blackmailer predicts payment, launches the attack, and delivers the letter with probability $1 - \epsilon$. The agent pays \$1,000.
  $$\mathbb{E}[\mathcal{V} \mid \Do(\Pi^* = \pi_{\Val{pay}})] \approx (1 - \epsilon)(-\$1,000) + \epsilon(\$0) = -(1 - \epsilon)\$1,000.$$
- Under $\Do(\Pi^* = \pi_{\Val{refuse}})$: The blackmailer predicts defiance and does not launch the program with probability $1 - \epsilon$. With probability $\epsilon$ (an error), the program is launched anyway, the agent receives the letter, refuses, and suffers the \$1,000,000 catastrophe.
  $$\mathbb{E}[\mathcal{V} \mid \Do(\Pi^* = \pi_{\Val{refuse}})] = (1 - \epsilon)(\$0) + \epsilon(-\$1,000,000) = -\epsilon(\$1,000,000).$$

Comparing the two policies:
$$\mathbb{E}[\mathcal{V} \mid \Do(\Pi^* = \pi_{\Val{refuse}})] > \mathbb{E}[\mathcal{V} \mid \Do(\Pi^* = \pi_{\Val{pay}})] \iff \epsilon < \frac{\$1,000}{\$1,000,000} = 0.001.$$

If the blackmailer's error rate $\epsilon$ is less than $0.1\%$, P-FDT selects:
$$\pi^* = \pi_{\Val{refuse}}.$$

#### The Counterfactual Perspective
Now consider the agent holding the letter ($\Obs = \Val{letter}$). 
- Carl (CDT) reasons: "The program is already running! If I pay \$1,000, I lose \$1,000. If I refuse, I lose \$1,000,000. Paying is strictly dominant." Carl pays, making CDT agents perpetually vulnerable to blackmail.
- Fiona (P-FDT) reasons: "My current action is the output of $\pi^*(\Val{letter})$. I selected policy $\pi_{\Val{refuse}}$ because doing so ensures that across the probability distribution of reality, the blackmailer almost certainly never sends this letter. The fact that I am holding the letter means I am living in the rare $\epsilon$-probability branch where the blackmailer erred. My policy commands $\Val{refuse}$. If my policy wavered and paid in this branch, my algorithm would be known to be exploitable, and I would be blackmailed systematically."

Fiona refuses to pay, successfully immunizing P-FDT agents against extortion.

---

## 6. Where P-FDT and Act-FDT Diverge: Multi-Agent Coordination and Dynamic Games

In footnote 7 and footnote 16, Yudkowsky and Soares make a striking claim:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper." (Footnote 7)

Why does policy selection matter in multi-agent dilemmas, and how does P-FDT diverge from act-based FDT? The source leaves this as an open question. We provide a rigorous explanation and model below.

### 6.1 The Asymmetric Information Game

Consider a game involving two psychological twins or programmatic peers, Alice and Bob, who both run functional decision theory. They are placed in separate rooms and receive private signals about the state of the world before coordinating on an action.

```
                  +-----------------------------------+
                  |         NATURE / SOURCE           |
                  +-----------------------------------+
                       /                         \
         Signal X_A   /                           \   Signal X_B
                     v                             v
           +--------------------+        +--------------------+
           |       ALICE        |        |        BOB         |
           |  Runs: pfdt(M_A)   |        |  Runs: pfdt(M_B)   |
           |  Chooses: Act_A    |        |  Chooses: Act_B    |
           +--------------------+        +--------------------+
                     \                             /
                      \                           /
                       v                         v
                  +-----------------------------------+
                  |          PAYOFF / OUTCOME         |
                  +-----------------------------------+
```

#### The Dilemma: The Asymmetric Twin Coordination Problem
Nature draws a hidden state $\Theta \in \{ \theta_1, \theta_2 \}$ with equal probability $P(\theta_1) = P(\theta_2) = 0.5$.
- Alice observes a noisy signal $X_A \in \{ 1, 2 \}$ of $\Theta$.
- Bob observes *no* signal: $X_B = \emptyset$.
- Alice and Bob must each choose an action $a \in \{ \Val{Left}, \Val{Right} \}$ without communicating.
- Their utility depends on whether their actions match each other *and* match the hidden state:
  - If $a_{\text{Alice}} = a_{\text{Bob}} = \Val{Left}$ and $\Theta = \theta_1$: both receive \$1,000,000.
  - If $a_{\text{Alice}} = a_{\text{Bob}} = \Val{Right}$ and $\Theta = \theta_2$: both receive \$1,000,000.
  - If their actions fail to match each other, or match the wrong state: both receive \$0.
- Alice’s signal $X_A$ is 90% accurate: $P(X_A = 1 \mid \theta_1) = 0.9$ and $P(X_A = 2 \mid \theta_2) = 0.9$.
- Alice and Bob know that they are programmatic twins: Bob knows that Alice’s decision procedure is identical to his, except that Alice receives an observation history containing her signal $x$, whereas Bob’s history is empty ($\emptyset$).

### 6.2 The Failure of Act-FDT
Under act-based FDT (Equation 4 of the source), an agent evaluates an action by intervening on the function *specialized to their specific observation*:
$$\FDT(P, G, x) = \argmax_{a \in \mathcal{A}} \mathbb{E}_P \left[ \mathcal{V} \mid \Do\left(\FDTvar(\underline{P}, \underline{G}, \underline{x}) = a\right) \right].$$

Consider Bob's calculation. Bob observes $X_B = \emptyset$. He intervenes on $\FDTvar(\underline{P_B}, \underline{G_B}, \underline{\emptyset})$.
Does Alice’s choice depend on $\FDTvar(\underline{P_B}, \underline{G_B}, \underline{\emptyset})$? 
**No!** Alice’s action is determined by $\FDTvar(\underline{P_A}, \underline{G_A}, \underline{X_A})$, where $X_A \in \{ 1, 2 \}$. 

Because act-based FDT treats interventions on $\FDTvar(\dots, \underline{x_1})$ and $\FDTvar(\dots, \underline{x_2})$ as structurally distinct nodes in the causal/logical DAG, Bob’s intervention on his own choice node does not propagate to Alice's choice node! To Bob, Alice’s choice is governed by an algorithm evaluated on a completely different observation string. Bob views his own action as subjunctively isolated from Alice’s informed decision. Consequently, the coordination collapses: Bob cannot treat his action as logically bound to Alice's conditional actions.

### 6.3 The Success of P-FDT
Under P-FDT, the point of intervention is not the action conditioned on a specific input, but the **entire mapping** $\Pi^* : \mathcal{X} \to \mathcal{A}$.

Because Alice and Bob share the same core code, they share the same global policy variable $\Pi^*$. The policy space is:
$$\mathcal{F} = \{ \pi : \{ 1, 2, \emptyset \} \to \{ \Val{Left}, \Val{Right} \} \}.$$

Bob evaluates the global expected utility of setting $\Pi^* = \pi$:
$$\mathbb{E}[\mathcal{V} \mid \Do(\Pi^* = \pi)] = \sum_{\theta} P(\theta) \sum_{x_A} P(x_A \mid \theta) \cdot \mathcal{U}\left(\pi(x_A), \pi(\emptyset), \theta\right).$$

It is immediately obvious that the optimal policy $\pi^*$ must coordinate Bob’s unconditional choice $\pi(\emptyset)$ with Alice’s conditional choice $\pi(x_A)$. For instance, if Bob’s policy specifies $\pi(\emptyset) = \Val{Left}$, Alice cannot condition on her signal without miscoordinating with Bob. 

More importantly, P-FDT enables Alice and Bob to identify *correlated asymmetric policies* or randomized conventions. If the game permits Bob to coordinate with Alice's signal (e.g., if Bob can infer that Alice will follow a policy $\pi$ that maps signal $1 \mapsto \Val{Left}$ and signal $2 \mapsto \Val{Right}$), both agents optimize over the joint mapping simultaneously. 

By intervening on the global policy type $\Pi^*$ rather than the local token $\FDTvar(\dots, \underline{x})$, P-FDT ensures that subjunctive dependencies across agents with differing information sets remain intact. This justifies the authors' cryptic observation in Footnote 7: **P-FDT preserves logical coordination across agents in asymmetric information games where act-based FDT fragments into uncoordinated local interventions.**

---

## 7. Comparative Analysis: EDT, CDT, Act-FDT, and P-FDT

To synthesize the differences between these four decision theories, we compare their formal mechanics and operational characteristics in the table below.

| Decision Theory | Core Ontological Object | Interventional Target | Epistemic Stance on Evidence | Behavior in Transparent Newcomb | Behavior in Mechanical Blackmail |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **EDT** | Act tokens | None (Bayesian conditioning) | Fully conditioned on observation: $P(- \mid x, a)$ | Two-boxes (Box B already known to be full) | Pays blackmail (manages news of damages) |
| **CDT** | Act tokens | Physical action: $\Do(\Act = a)$ | Conditioned on observation: $P(- \mid \Do(a), x)$ | Two-boxes (cannot causally alter the past) | Pays blackmail (program is already running) |
| **Act-FDT** | Function evaluation tokens | Algorithm output for history $x$: $\Do(\FDTvar(\dots, \underline{x}) = a)$ | Shuts off conditioning; shifts interventional node | One-boxes (imagines empty box if two-boxing) | Refuses payment (imagines counterfactual history) |
| **P-FDT** | Global policy functions | Global policy mapping: $\Do(\Pi^* = \pi)$ | Updateless evaluation over prior; applies $\pi^*(x)$ | One-boxes (executes optimal policy $\pi_{12}$) | Refuses payment (executes optimal policy $\pi_{\Val{refuse}}$) |

### 7.1 The Nature of Dominance

Causal decision theorists have historically defended two-boxing by appealing to the Principle of Dominance: if state of the world $S$ is fixed, action $A_1$ yields higher utility than $A_2$ across all states $S$, then $A_1$ must be chosen.

As Yudkowsky and Soares argue in Section 6, every decision theory defines its own notion of dominance based on the hypotheticals it constructs:
- **CDT Dominance**: An action dominates if it yields higher utility holding fixed all non-causally downstream variables. Under this definition, two-boxing dominates.
- **P-FDT Dominance**: A policy $\pi_1$ dominates $\pi_2$ if, holding constant all *subjunctive dependencies* between $\Pi^*$ and the environment, $\pi_1$ yields at least as much utility as $\pi_2$ in all logically possible structures, and strictly more in at least one.

Under P-FDT dominance, **one-boxing dominates two-boxing in Transparent Newcomb**. Holding constant the predictor’s subjunctive dependence on $\Pi^*$, the policy $\pi_{12}$ yields \$990,010 in expectation, whereas $\pi_{22}$ yields \$11,000. Because P-FDT agents evaluate the holistic effects of their algorithmic type, they are never seduced by the illusion of local dominance.

---

## 8. Open Problems and Theoretical Challenges for P-FDT

While P-FDT resolves the operational and conceptual awkwardness of act-based FDT, it introduces deep theoretical challenges of its own.

### 8.1 The Computational Complexity of Policy Spaces

The most glaring practical challenge for P-FDT is the cardinality of the policy space. If an agent faces an observation history of length $T$ with observation alphabet $|\mathcal{X}|$ and action alphabet $|\mathcal{A}|$, the number of possible deterministic policies is:
$$|\mathcal{F}| = |\mathcal{A}|^{|\mathcal{X}|^T}.$$
Searching over this double-exponential space is intractable. In practice, a bounded P-FDT agent cannot evaluate all policies. Instead, bounded P-FDT must rely on programmatic heuristics:
- Searching over parameterized policy classes (e.g., neural networks or compact finite-state automata).
- Applying policy-gradient reinforcement learning or Monte Carlo tree search over subjunctive graphs.
- Formulating the optimization as a functional calculus over compact representations of logical dependency.

### 8.2 The Formal Structure of Logical Graphs

Both act-based FDT and P-FDT rely on Pearl’s $\Do$-operator applied to non-causal, logical variables. Pearl's do-calculus was explicitly developed for directed causal mechanisms verified by physical randomized experiments. What does it mean to "sever incoming arrows" to a mathematical function node $\Pi^*$?

As noted in Section 5 of the source document:
> "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." (Yudkowsky & Soares 2017)

In P-FDT, the graph $G$ must be supplied with structural equations asserting that external models correlate with $\Pi^*$. But if $\Pi^*$ is a deterministic algorithm, its true output is mathematically fixed by the axioms of arithmetic. Intervening to set $\Pi^* = \pi$ when the algorithm actually outputs $\pi'$ is a **counterpossible conditional**—reasoning about what would happen if a logical contradiction were true. Developing a mathematically sound foundation for counterpossible reasoning—perhaps via logical induction (Garrabrant et al. 2016) or proof-theoretic probability metrics—remains an active area of research.

### 8.3 The Selection of the Updateless Prior

P-FDT requires evaluating $\mathbb{E}_P[\mathcal{V} \mid \Do(\Pi^* = \pi)]$ relative to a root distribution $P$. But what is the agent’s "prior" if the agent is created midway through a dynamic environment? 

If an agent is initialized with an arbitrary prior, or if different representations of the prior lead to conflicting optimal policies, P-FDT risks arbitrariness. In artificial intelligence research, this is known as the *problem of the updateless prior*: defining a canonical, reflective prior distribution from which all counterfactual policy commitments can be stably derived.

---

## 9. Conclusion

Policy Functional Decision Theory (P-FDT) represents the natural culmination of the functional decision-theoretic program. By elevating the object of rational deliberation from token acts to global policies, P-FDT resolves the central tensions that have bedeviled normative decision theory for decades.

Where CDT fails by assuming present acts can be varied without changing past predictions that depend upon them, P-FDT recognizes the logical binding between an agent's code and its environmental simulations. Where EDT fails by managing news and attempting to influence biological common causes, P-FDT distinguishes between mere statistical correlations and genuine subjunctive dependencies. And where act-based FDT requires shifting intervention nodes and counterintuitive counterfactual explanations, P-FDT operates cleanly via a two-stage architecture: **globally optimize the policy, then locally execute the action**.

The result is a decision theory that does not merely theorize about rationality, but consistently secures high utility. P-FDT one-boxes in Newcomb's Problem, smokes in the Smoking Lesion Problem, pays the driver in Parfit's Hitchhiker, one-boxes in the Transparent Newcomb Problem, and defies the blackmailer in Mechanical Blackmail. By treating rationality as a global property of algorithms rather than an isolated property of physical acts, P-FDT provides a compelling foundation for the next generation of decision theory and artificial intelligence.

---

## References

- Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
- Arntzenius, F. (2008). "No Regrets, or: Edith Piaf Revamps Decision Theory." *Erkenntnis*, 68(2), 277–297.
- Dai, W. (2009). "Towards a New Decision Theory." *LessWrong*.
- Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
- Eells, E. (1984). "Metatickles and the Dynamics of Deliberation." *Theory and Decision*, 17(1), 71–95.
- Garrabrant, S., Fallenstein, B., Critch, A., Gao, C., & Demski, A. (2016). "Logical Induction." *arXiv preprint arXiv:1609.03543*.
- Gibbard, A., & Harper, W. L. (1978). "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory* (pp. 125–162). D. Reidel.
- Jeffrey, R. C. (1983). *The Logic of Decision* (2nd ed.). University of Chicago Press.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Kleene, S. C. (1938). "On Notation for Ordinal Numbers." *Journal of Symbolic Logic*, 3(4), 150–155.
- Lewis, D. (1979). "Prisoners' Dilemma is a Newcomb Problem." *Philosophy & Public Affairs*, 8(3), 235–240.
- Lewis, D. (1981). "Causal Decision Theory." *Australasian Journal of Philosophy*, 59(1), 5–30.
- Nozick, R. (1969). "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel* (pp. 114–146). D. Reidel.
- Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
- Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
- Skyrms, B. (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
- Soares, N., & Fallenstein, B. (2015). "Toward Idealized Decision Theory." *arXiv preprint arXiv:1507.01986*.
- Spohn, W. (1977). "Where Luce and Krantz do really generalize Savage's decision model." *Erkenntnis*, 11(1), 113–134.
- Yudkowsky, E. (2010). "Timeless Decision Theory." *The Singularity Institute*.
- Yudkowsky, E., & Soares, N. (2017). "Functional Decision Theory: A New Theory of Instrumental Rationality." *arXiv preprint arXiv:1710.05060v2*.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
