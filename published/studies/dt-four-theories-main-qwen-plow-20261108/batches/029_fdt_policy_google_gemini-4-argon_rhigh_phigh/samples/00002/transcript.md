# 029_fdt_policy_google_gemini-4-argon_rhigh_phigh / 00002

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/aab64bf8-effe-485f-9445-53f9804eeb2a/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/aab64bf8-effe-485f-9445-53f9804eeb2a/call_0/response.raw) · finish: `stop`

### Visible response

````text
# Policy Functional Decision Theory (P-FDT): Formalism, Counterfactuals, and Applications

## 1. Introduction: From Physical Acts to Logical Policies

Normative decision theory turns on a deceptively simple question: when an agent evaluates candidate choices, which features of the world should she hold fixed, and which should she imagine varying with her choice? 

For decades, the debate was framed as a binary contest between **evidential decision theory (EDT)** and **causal decision theory (CDT)**. EDT evaluates an action $a$ by conditioning the agent's probability distribution on the event that she performs $a$, asking which action would provide the best news. CDT evaluates an action $a$ by performing a causal intervention on the physical act token, asking which action causally produces the best downstream outcomes. As Allan Gibbard and William Harper (1978) famously demonstrated, these two rules diverge whenever an action correlates with a state of the world without causing it: EDT outperforms CDT in Newcomb's problem, while CDT outperforms EDT in the smoking lesion problem.

In *"Functional Decision Theory: A New Theory of Instrumental Rationality"*, Eliezer Yudkowsky and Nate Soares propose a third paradigm. Rather than treating a decision as a purely physical event or an item of statistical evidence, **functional decision theory (FDT)** treats a decision as the logical output of a fixed mathematical function implemented by the agent—and potentially simulated by predictors or shared by psychological twins. In the main body of their paper, Yudkowsky and Soares formalize an action-based version of FDT (hereafter **action-based FDT**), in which the agent intervenes on a node representing the action output of her decision algorithm for her current observation. 

However, in two crucial footnotes, the authors reveal that this action-based equation is actually a pedagogical simplification of their preferred theory, which we will call **policy functional decision theory (P-FDT)**. In footnote 7, they note:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

And in footnote 16, they specify the mechanics of this policy-based intervention:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

This essay provides a self-contained mathematical exposition of **P-FDT** based on these passages and the surrounding framework of Yudkowsky and Soares. We will examine the philosophical motivation behind subjunctive dependence and updateless policy selection, develop the formal equations of P-FDT alongside EDT, CDT, and action-based FDT, and work through concrete decision problems—showing both why P-FDT agrees with action-based FDT in single-agent dilemmas (while simplifying the required epistemic priors) and why P-FDT strictly outperforms action-based FDT in multi-agent dilemmas with asymmetric observations. Finally, where the source text leaves formal choices open, we will identify those uncertainties and develop operational extensions to resolve them.

---

## 2. Philosophical Motivation: Subjunctive Dependence and the Global Perspective

All expected utility theories share a common mathematical skeleton. Drawing on Gibbard and Harper (1978) and the representation theorem of James Joyce (1999), an agent faces a finite set of actions $\mathcal{A}$, a countable set of observation histories $\mathcal{X}$, a countable set of outcomes $\mathcal{O}$, and a bounded utility function $\mathcal{U} : \mathcal{O} \to \mathbb{R}$. Under Joyce's framework, competing decision theories do not disagree about how to value outcomes; in Joyce's words, "decision theories should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated." Formally, they disagree on how to construct the hypothetical probability $P(a \hookrightarrow o_j ;\, x)$ that outcome $o_j \in \mathcal{O}$ obtains if action $a \in \mathcal{A}$ is taken after observing $x \in \mathcal{X}$:

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j).$$

Why do EDT and CDT fail to capture the right epistemic perspective? 
* **EDT** equates decision hypotheticals with Bayesian conditionalization: $P(a \hookrightarrow o_j ;\, x) = P(o_j \mid x, a)$. By preserving *all* statistical correlations between the agent's action and the environment, EDT cannot distinguish between a predictor who rewards one-boxing (Newcomb's problem) and a genetic lesion that causes both a love of smoking and fatal lung cancer (the smoking lesion problem). Worse, in problems like the *XOR Blackmail* (Soares and Fallenstein 2015), a predictor can extort an EDT agent simply by sending a blackmail letter that artificially correlates paying $\$1,000$ with the absence of a $\$1,000,000$ termite infestation. EDT "manages the news" rather than optimizing outcomes.
* **CDT** equates decision hypotheticals with physical causal interventions, formalized via Judea Pearl's (1996, 2000) $\mathtt{do}$-calculus: $P(a \hookrightarrow o_j ;\, x) = P(o_j \mid \mathtt{do}(\textsc{Act} = a), \textsc{Obs} = x)$. By severing all incoming arrows into the physical action node $\textsc{Act}$, CDT breaks spurious statistical correlations (correctly smoking in the lesion problem and refusing to pay in the XOR Blackmail). However, CDT breaks *too many* correlations. In Newcomb's problem or the *Psychological Twin Prisoner's Dilemma*, CDT holds the predictor's prediction or the twin's action fixed while varying $\textsc{Act}$. It asks what would happen if the agent's physical body acted differently while an accurate simulation of her decision process inexplicably failed to match. In asymmetric games against predictors like *Death in Damascus*, this blind spot makes CDT reflectively unstable and leads it to reject a $\$1$ truly random coin that would raise its survival probability from $0\%$ to $50\%$.

To get the balance right, Yudkowsky and Soares introduce **subjunctive dependence**. When two physical systems—such as two calculators computing $6288 + 1048 = 7336$, two psychological twins deliberating in separate rooms, or an agent and a predictor's simulation of that agent—implement the same mathematical function, their outputs subjunctively depend on that function's logical evaluation. Using Charles Sanders Peirce's (1934) type-token distinction, CDT intervenes only on the physical *token* $\textsc{Act}$, whereas functional decision theories intervene on the mathematical *type*: the decision function itself.

Crucially, intervening on the decision function requires adopting what Yudkowsky and Soares call a "global" or updateless perspective (building on Wei Dai's [2009] **updateless decision theory [UDT]**, and avoiding the "double update" of Yudkowsky's [2010] **timeless decision theory [TDT]**, which both conditioned on observations and changed the intervention locus). Consider the *Transparent Newcomb Problem* (Drescher 2006) or *Parfit's Hitchhiker* (Parfit 1986). In Transparent Newcomb, both boxes are transparent, and the predictor fills box B with $\$1,000,000$ if and only if she predicts that the agent will leave box A ($\$1,000$) behind *upon seeing that box B is full*. If the agent conditions her world-model on seeing a full box B ($\textsc{Obs} = \textit{full}$) before evaluating her decision, the past prediction is locked in; both CDT and EDT two-box, and the predictor leaves box B empty. 

A functional decision theorist recognizes that her observation $\textsc{Obs} = \textit{full}$ was itself generated by the predictor's simulation of how her algorithm responds to $\textit{full}$. If her algorithm were to output $\textit{twobox}$ on input $\textit{full}$, she would almost certainly have observed $\textit{empty}$ instead.

**P-FDT** carries this functional insight to its natural mathematical conclusion. An agent's decision procedure is not a disconnected collection of lookup-table entries evaluated in isolation for one observation $x$ at a time; it is a unified algorithm that selects a **policy** $\pi : \mathcal{X} \to \mathcal{A}$ mapping every possible observation to an action, and then applies that policy to the realized observation $x$ to produce $\pi(x)$. By intervening on the policy-selection node as a whole, P-FDT captures subjunctive dependencies not only between the agent and external predictors of her current observation, but also across distinct counterfactual observations and across multiple copies of the agent who observe different local inputs.

---

## 3. The Mathematical Formalism of P-FDT

To make the comparison precise, let $M = (P, G)$ be the agent's world-model, where $G$ is a directed acyclic graph (DAG) encoding both causal and logical/subjunctive dependencies among a collection of random variables, and $P$ is a probability distribution compatible with $G$. Let $\textsc{Obs}$ be an $\mathcal{X}$-valued variable representing the agent's observation, $\textsc{Act}$ be an $\mathcal{A}$-valued variable representing her physical action, $\textsc{Outcome}$ be an $\mathcal{O}$-valued variable representing the world outcome, and $\textsc{V} \coloneqq \mathcal{U}(\textsc{Outcome})$ be the resulting utility variable. Following the source's notation, an underline denotes dequoting: if $z$ has value $3$, then $\textsc{Node}(\underline{z})$ denotes the variable name $\textsc{Node}(3)$.

In the source paper, EDT, CDT, and action-based FDT are defined by Equations (2), (3), and (4):

$$\mathrm{EDT}(P, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs} = x, \textsc{Act} = a\right),$$

$$\mathrm{CDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{Act} = a), \textsc{Obs} = x\right),$$

$$\mathrm{FDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right).$$

Notice how action-based FDT handles an observation $x \in \mathcal{X}$. Rather than conditioning $P$ on $\textsc{Obs} = x$, it embeds a family of logical variables $\{\textsc{fdt}(\underline{P}, \underline{G}, \underline{x'})\}_{x' \in \mathcal{X}}$ inside $G$—one for each possible observation $x'$—and responds to observing $x$ by intervening solely on the node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$.

Now let us formalize **P-FDT** directly from footnotes 7 and 16. Let $\Pi \coloneqq \mathcal{A}^{\mathcal{X}} = \{\pi : \mathcal{X} \to \mathcal{A}\}$ denote the finite space of deterministic policies mapping observations to actions. (While footnotes 7 and 16 state the core mechanism conceptually, the explicit algebraic equations below are our formalization of their description.) Instead of indexing the logical node in $G$ by a specific observation $x$, the graph $G$ contains a single policy-valued logical node $\textsc{pfdt}(\underline{P}, \underline{G})$ with state space $\Pi$, representing the policy output of P-FDT's policy-selection subroutine when run on the world-model $(P, G)$.

P-FDT proceeds in two steps:
1. **Policy Selection (Intervention on the Policy Node):** The agent identifies the optimal policy $\Pi_{\mathrm{P\text{-}FDT}}(P, G) \in \Pi$ by intervening on $\textsc{pfdt}(\underline{P}, \underline{G})$ and maximizing unconditional expected utility:
   $$\Pi_{\mathrm{P\text{-}FDT}}(P, G) \coloneqq \argmax_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right).$$
2. **Policy Application (Evaluating at the Input Observation):** The agent applies the selected policy to her actual observation $x \in \mathcal{X}$ to output a physical action:
   $$\mathrm{P\text{-}FDT}(P, G, x) \coloneqq \left[\Pi_{\mathrm{P\text{-}FDT}}(P, G)\right](x) = \left[\argmax_{\pi \in \Pi} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi\right)\right)\right](x).$$

How does the graph $G$ wire $\textsc{pfdt}(\underline{P}, \underline{G})$ to the rest of the world? 
* First, the agent's physical action node $\textsc{Act}$ is governed by the structural equation
  $$\textsc{Act} = \textsc{pfdt}(\underline{P}, \underline{G})(\textsc{Obs}),$$
  meaning that $\textsc{Act}$ has incoming arrows from both $\textsc{pfdt}(\underline{P}, \underline{G})$ and $\textsc{Obs}$: once the policy $\pi$ and the observation $x$ are determined, the physical act is simply $\pi(x)$.
* Second, any environmental process that predicts the agent or implements the same decision algorithm (such as a Newcomb predictor, a blackmailer, or a psychological twin) also has an incoming arrow from $\textsc{pfdt}(\underline{P}, \underline{G})$. For instance, if a predictor simulates what the agent would do upon observing $x_0$, the predictor's action is a structural function of $\pi(x_0)$ (plus any simulation noise).

As in action-based FDT, the self-reference in $\textsc{pfdt}(\underline{P}, \underline{G})$ is benign: by Kleene's (1938) second recursion theorem ("quining"), a computational structure $(P, G)$ can contain a syntactic pointer to the variable representing its own evaluation without already knowing which policy $\pi \in \Pi$ maximizes the expression. And just like action-based FDT, evaluating $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$ for $\pi \neq \Pi_{\mathrm{P\text{-}FDT}}(P, G)$ involves evaluating a *counterpossible* conditional—imagining a world in which a deterministic mathematical function outputs a different policy than it actually does, while holding fixed the structural equations in $G$ that link predictors and physical actions to that output.

---

## 4. Applying P-FDT to Single-Agent Dilemmas

To see how to apply **P-FDT** in practice—and to understand why P-FDT produces the same actions as action-based FDT in single-agent problems while streamlining the calculation—let us work through the **Transparent Newcomb Problem** (Drescher 2006). (As Yudkowsky and Soares note in Section 4, this dilemma is decision-theoretically isomorphic to *Parfit's Hitchhiker* and structurally identical to the *Mechanical Blackmail* problem in Section 9.)

### Problem Setup and Graphical Structure
Box A is transparent and contains $\$1,000$. Box B is also transparent and contains either $\$1,000,000$ ($\textit{full}$) or $\$0$ ($\textit{empty}$). A predictor with accuracy $1 - \epsilon = 0.99$ predicted whether the agent would one-box ($\textit{1B}$, taking only box B) or two-box ($\textit{2B}$, taking both boxes) *upon observing that box B is full*. If she predicted $\textit{1B}$, she filled box B; if she predicted $\textit{2B}$, she left box B empty.

Under **P-FDT**, the observation space is $\mathcal{X} = \{\textit{full}, \textit{empty}\}$ and the action space is $\mathcal{A} = \{\textit{1B}, \textit{2B}\}$. The policy space $\Pi = \mathcal{A}^{\mathcal{X}}$ therefore consists of four policies, which we write as pairs $\pi = (\pi(\textit{full}), \pi(\textit{empty}))$:

$$\Pi = \left\{\pi_{1,1} = (\textit{1B}, \textit{1B}),\; \pi_{1,2} = (\textit{1B}, \textit{2B}),\; \pi_{2,1} = (\textit{2B}, \textit{1B}),\; \pi_{2,2} = (\textit{2B}, \textit{2B})\right\}.$$

The P-FDT graph $G$ and structural equations are specified as follows:
* **Exogenous accuracy node:** $\textsc{Accurate} \in \{\textit{accurate}, \textit{inaccurate}\}$ with $P(\textsc{Accurate} = \textit{accurate}) = 0.99$ and $P(\textsc{Accurate} = \textit{inaccurate}) = 0.01$.
* **Policy node (point of intervention):** $\textsc{pfdt}(\underline{P}, \underline{G}) \in \Pi$.
* **Prediction and Box B:** The predictor simulates the policy on the $\textit{full}$ input:
  $$\textsc{Box B}(\pi, \textit{accurate}) = \begin{cases} \textit{full} & \text{if } \pi(\textit{full}) = \textit{1B}, \\ \textit{empty} & \text{if } \pi(\textit{full}) = \textit{2B}, \end{cases} \qquad \textsc{Box B}(\pi, \textit{inaccurate}) = \begin{cases} \textit{empty} & \text{if } \pi(\textit{full}) = \textit{1B}, \\ \textit{full} & \text{if } \pi(\textit{full}) = \textit{2B}. \end{cases}$$
* **Observation and Action:** Since Box B is transparent, $\textsc{Obs} = \textsc{Box B}$. The agent's physical action is $\textsc{Act} = \pi(\textsc{Obs})$.
* **Utility $\textsc{V}$:**
  $$\textsc{V}(\textit{1B}, \textit{full}) = \$1,000,000, \quad \textsc{V}(\textit{2B}, \textit{full}) = \$1,001,000, \quad \textsc{V}(\textit{1B}, \textit{empty}) = \$0, \quad \textsc{V}(\textit{2B}, \textit{empty}) = \$1,000.$$

```
                [pfdt(P, G)]                [Accurate]
                 /        \                   /
                /          v                 v
               |          [Prediction / Box B]
               |               /         \
               |              v           |
               |            [Obs]         |
                \            /            |
                 v          v             |
                    [Act]                 |
                      \                  /
                       v                v
                              [V]
```

### Step-by-Step P-FDT Evaluation
Now suppose the P-FDT agent stands before the boxes and sees that Box B is full ($\textsc{Obs} = \textit{full}$). To compute $\mathrm{P\text{-}FDT}(P, G, \textit{full})$, she first computes $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)]$ for each of the four candidate policies $\pi \in \Pi$:

1. **Policy $\pi_{1,1} = (\textit{1B}, \textit{1B})$:** Since $\pi_{1,1}(\textit{full}) = \textit{1B}$, with probability $0.99$ ($\textit{accurate}$) Box B is $\textit{full}$ and she plays $\pi_{1,1}(\textit{full}) = \textit{1B}$ for $\$1,000,000$; with probability $0.01$ ($\textit{inaccurate}$) Box B is $\textit{empty}$ and she plays $\pi_{1,1}(\textit{empty}) = \textit{1B}$ for $\$0$.
   $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{1,1})\right] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000.$$

2. **Policy $\pi_{1,2} = (\textit{1B}, \textit{2B})$:** Since $\pi_{1,2}(\textit{full}) = \textit{1B}$, Box B is again $\textit{full}$ with probability $0.99$ (yielding $\pi_{1,2}(\textit{full}) = \textit{1B}$ and $\$1,000,000$), and $\textit{empty}$ with probability $0.01$ (yielding $\pi_{1,2}(\textit{empty}) = \textit{2B}$ and $\$1,000$).
   $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{1,2})\right] = 0.99(\$1,000,000) + 0.01(\$1,000) = \$990,010.$$

3. **Policy $\pi_{2,1} = (\textit{2B}, \textit{1B})$:** Since $\pi_{2,1}(\textit{full}) = \textit{2B}$, with probability $0.99$ ($\textit{accurate}$) the predictor leaves Box B $\textit{empty}$, so the agent observes $\textit{empty}$ and plays $\pi_{2,1}(\textit{empty}) = \textit{1B}$ for $\$0$; with probability $0.01$ ($\textit{inaccurate}$) Box B is $\textit{full}$ and she plays $\pi_{2,1}(\textit{full}) = \textit{2B}$ for $\$1,001,000$.
   $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{2,1})\right] = 0.01(\$1,001,000) + 0.99(\$0) = \$10,010.$$

4. **Policy $\pi_{2,2} = (\textit{2B}, \textit{2B})$:** Since $\pi_{2,2}(\textit{full}) = \textit{2B}$, with probability $0.99$ Box B is $\textit{empty}$ and she plays $\pi_{2,2}(\textit{empty}) = \textit{2B}$ for $\$1,000$; with probability $0.01$ Box B is $\textit{full}$ and she plays $\pi_{2,2}(\textit{full}) = \textit{2B}$ for $\$1,001,000$.
   $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{2,2})\right] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$

Comparing the four values, the unique optimal policy is $\Pi_{\mathrm{P\text{-}FDT}}(P, G) = \pi_{1,2} = (\textit{1B}, \textit{2B})$, which achieves $\$990,010$ in expectation. Finally, the agent applies $\pi_{1,2}$ to her actual observation $x = \textit{full}$:

$$\mathrm{P\text{-}FDT}(P, G, \textit{full}) = \pi_{1,2}(\textit{full}) = \textit{1B}.$$

Even while staring at a transparent box containing $\$1,000,000$, the P-FDT agent leaves the $\$1,000$ behind—and if the predictor ever erred and left Box B empty, the very same policy prescribes $\mathrm{P\text{-}FDT}(P, G, \textit{empty}) = \pi_{1,2}(\textit{empty}) = \textit{2B}$, taking the $\$1,000$.

### A Subtle Epistemic Advantage of P-FDT over Action-Based FDT
While Yudkowsky and Soares note that choosing policies rather than actions does not change the prescribed behavior in the single-agent dilemmas of their paper, comparing our P-FDT calculation above with the action-based FDT calculation in Section 6 of their paper highlights a clean mathematical simplification (an observation of our own that builds on their text). 

In Section 6, when Fiona evaluates action-based FDT upon seeing $\textit{full}$, she intervenes only on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full}) = a$, leaving the sibling node $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty})$ un-intervened. Because switching $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{full})$ to $\textit{2B}$ causes her observation to switch to $\textit{empty}$ $99\%$ of the time, her action in that counterfactual world is controlled by the un-intervened node $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty})$. Consequently, the authors must introduce a prior probability parameter $q \coloneqq P^F(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \textit{empty}) = \textit{2B})$ representing Fiona's subjective belief about what she would do if she saw an empty box, yielding expected utilities of $\$990,000 + 0.01q \cdot \$1,000$ for $\textit{1B}$ and $\$10,010 + 0.99q \cdot \$1,000$ for $\textit{2B}$.

Under **P-FDT**, the epistemic parameter $q$ vanishes completely. Because the intervention $\mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)$ simultaneously specifies $\pi(\textit{full})$ and $\pi(\textit{empty})$, the agent does not need to maintain prior beliefs about her own behavior at alternative observations; she directly optimizes across all contingencies at once.

---

## 5. Why Policies Matter: Applying P-FDT to Multi-Agent Dilemmas

Why do Yudkowsky and Soares emphasize in footnotes 7 and 16 that the distinction between action-based FDT and **P-FDT** "makes a difference in certain multi-agent dilemmas"? 

In the standard *Psychological Twin Prisoner's Dilemma* (Dilemma 1 of the paper), both twins receive the exact same null observation $x = \emptyset$. Consequently, in action-based FDT, both twins intervene on the exact same variable $\textsc{fdt}(\underline{P}, \underline{G}, \emptyset)$, and action-based FDT successfully cooperates. 

However, suppose the twins receive *different* observations before acting. In action-based FDT (Equation 4), an agent who observes $x$ intervenes *only* on the variable $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$. If her psychological twin observes $x' \neq x$, the twin's physical action is governed by a *different* variable in the graph, $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x'})$. Because Pearl's $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)$ operator only updates nodes downstream of $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ and leaves $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x'})$ untouched, **action-based FDT severs the subjunctive dependency between identical agents whenever they observe different inputs!**

To see this divergence starkly, consider the following concrete case (constructed here to illustrate the claim in footnote 16).

### Example: The Asymmetric Twin Prisoner's Dilemma
Two psychological twins—implementing the exact same decision procedure with the same prior world-model $(P, G)$—are placed in separate rooms, labeled Room $0$ and Room $1$, by a fair coin flip. Each twin observes her own room number $x \in \{0, 1\}$, knowing that her twin is in the other room observing $1 - x$. Each twin must choose an action $a \in \{\textit{C}, \textit{D}\}$ (Cooperate or Defect). Cooperating costs the cooperator $\$1,000$ and delivers $\$1,000,000$ to the *other* twin (in the opposite room). Thus, if the action chosen in Room $x$ is $A_x$ and the action chosen in Room $1-x$ is $A_{1-x}$, the utility of the twin in Room $x$ is:

$$\textsc{V}_x(A_x, A_{1-x}) = \$1,000,000 \cdot \mathbb{I}(A_{1-x} = \textit{C}) - \$1,000 \cdot \mathbb{I}(A_x = \textit{C}).$$

Let us compare how **action-based FDT** and **P-FDT** evaluate this dilemma when a twin observes $x = 0$:

#### 1. Action-Based FDT (Equation 4) Defects
In action-based FDT, the graph $G$ contains two separate logical decision nodes: $\textsc{fdt}(\underline{P}, \underline{G}, 0)$ (which controls the action $A_0$ of the twin in Room $0$) and $\textsc{fdt}(\underline{P}, \underline{G}, 1)$ (which controls the action $A_1$ of the twin in Room $1$). 

When the twin in Room $0$ observes $x = 0$, she computes $\mathrm{FDT}(P, G, 0)$ by intervening solely on $\textsc{fdt}(\underline{P}, \underline{G}, 0) = a_0$. Because $\textsc{fdt}(\underline{P}, \underline{G}, 1)$ is not downstream of $\textsc{fdt}(\underline{P}, \underline{G}, 0)$, the intervention $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, 0) = a_0)$ holds fixed her prior probability $q \coloneqq P(\textsc{fdt}(\underline{P}, \underline{G}, 1) = \textit{C})$ that her twin in Room $1$ cooperates:

$$\mathbb{E}\left[\textsc{V}_0 \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, 0) = \textit{C}\right)\right] = \$1,000,000 \cdot q - \$1,000,$$

$$\mathbb{E}\left[\textsc{V}_0 \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, 0) = \textit{D}\right)\right] = \$1,000,000 \cdot q.$$

Regardless of $q$, defecting yields $\$1,000$ more expected utility than cooperating! By symmetry, the twin in Room $1$ intervenes only on $\textsc{fdt}(\underline{P}, \underline{G}, 1)$ and likewise concludes that $\mathrm{FDT}(P, G, 1) = \textit{D}$. Action-based FDT collapses into CDT-style mutual defection, leaving both twins with $\$0$.

#### 2. P-FDT Cooperates
Under **P-FDT**, both twins share a *single* policy-selection node $\textsc{pfdt}(\underline{P}, \underline{G})$ in $G$. In the common prior $P$ (before conditioning on which room one wakes up in), the agent has probability $P(\textsc{Obs} = 0) = 0.5$ of being placed in Room $0$ and $P(\textsc{Obs} = 1) = 0.5$ of being placed in Room $1$. Both physical actions are downstream of the single policy node $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$:

$$A_0 = \pi(0), \qquad A_1 = \pi(1).$$

When the P-FDT agent in Room $0$ deliberates, she intervenes on $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$ across the four policies $\pi = (\pi(0), \pi(1)) \in \{\textit{C}, \textit{D}\}^{\{0, 1\}}$:

* **$\pi_{\textit{C},\textit{C}} = (\textit{C}, \textit{C})$:** In both rooms ($0.5$ chance of Room $0$, $0.5$ chance of Room $1$), the agent plays $\textit{C}$ and her twin plays $\textit{C}$:
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{\textit{C},\textit{C}})\right] = 0.5(\$999,000) + 0.5(\$999,000) = \$999,000.$$
* **$\pi_{\textit{C},\textit{D}} = (\textit{C}, \textit{D})$:** With probability $0.5$ the agent is in Room $0$ (plays $\textit{C}$ while twin plays $\textit{D}$, getting $-\$1,000$), and with probability $0.5$ she is in Room $1$ (plays $\textit{D}$ while twin plays $\textit{C}$, getting $\$1,000,000$):
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi_{\textit{C},\textit{D}})\right] = 0.5(-\$1,000) + 0.5(\$1,000,000) = \$499,500.$$
* **$\pi_{\textit{D},\textit{C}} = (\textit{D}, \textit{C})$:** By symmetry, $0.5(\$1,000,000) + 0.5(-\$1,000) = \$499,500$.
* **$\pi_{\textit{D},\textit{D}} = (\textit{D}, \textit{D})$:** In both rooms, both defect, yielding $\$0$.

Thus, $\Pi_{\mathrm{P\text{-}FDT}}(P, G) = \pi_{\textit{C},\textit{C}} = (\textit{C}, \textit{C})$. Applying this policy to her actual observation $x = 0$, the twin in Room $0$ outputs $\mathrm{P\text{-}FDT}(P, G, 0) = \pi_{\textit{C},\textit{C}}(0) = \textit{C}$, and the twin in Room $1$ outputs $\mathrm{P\text{-}FDT}(P, G, 1) = \pi_{\textit{C},\textit{C}}(1) = \textit{C}$. Both twins walk away with $\$999,000$.

| Decision Theory | Locus of Intervention | Updates on $\textsc{Obs} = x$ Inside $\mathbb{E}[\textsc{V}]$? | Newcomb / Lesion | Transparent Newcomb | Asymmetric Twin PD |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **EDT** | None (conditions on $\textsc{Act}=a$) | Yes (Bayesian conditioning) | $\textit{1B}$ / $\textit{Refrain}$ | $\textit{2B}$ ($\$1,000$) | $\textit{D}$ ($\$0$) |
| **CDT** | Physical act token $\textsc{Act}=a$ | Yes (Bayesian conditioning) | $\textit{2B}$ / $\textit{Smoke}$ | $\textit{2B}$ ($\$1,000$) | $\textit{D}$ ($\$0$) |
| **Action-Based FDT** | Single branch $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})=a$ | No (switches node to $\underline{x}$) | $\textit{1B}$ / $\textit{Smoke}$ | $\textit{1B}$ ($\$1,000,000$) | $\textit{D}$ ($\$0$) |
| **P-FDT** | Full policy $\textsc{pfdt}(\underline{P}, \underline{G})=\pi$ | No (applies $\pi$ to $x$ after $\argmax$) | $\textit{1B}$ / $\textit{Smoke}$ | $\textit{1B}$ ($\$1,000,000$) | $\textit{C}$ ($\$999,000$) |

*(Note: In Asymmetric Twin PD, an EDT agent whose prior treats her action in Room $0$ as statistically independent of her twin's action in Room $1$ defects; even if she posits a correlation, EDT lacks a mechanism to ground cross-observation policy optimization.)*

---

## 6. Unresolved Questions and Operational Extensions of P-FDT

Because Yudkowsky and Soares mention **P-FDT** only briefly in footnotes 7 and 16, several important technical questions are left open by the source text. To make P-FDT fully operational across arbitrary decision problems, we must identify these gaps and specify principled mathematical completions (clearly distinguishing our proposed operational assumptions from the claims explicitly stated by the authors).

### 1. What Are the "Inputs" to a Policy? (Observations vs. World-Models)
There is a subtle tension between footnote 7, which defines policies as "mappings from observations to actions" ($\pi : \mathcal{X} \to \mathcal{A}$), and footnote 16, which says that P-FDT selects "a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action." In Equation (4), the inputs to the decision algorithm are the triple $(P, G, x)$, not just $x$. 

Why does this matter? Recall how Yudkowsky and Soares formalize the *Smoking Lesion Problem* in Section 6 (Figure 5). Because the lesion causes agents to love smoking, Fiona does not know whether her internal world-model uses utility function $\mathcal{U}_S$ (distribution $P_S^F$) or $\mathcal{U}_R$ (distribution $P_R^F$). In action-based FDT, the authors create two distinct nodes in $G^F$: $\textsc{fdt}(\underline{P_S^F}, \underline{G^F})$ and $\textsc{fdt}(\underline{P_R^F}, \underline{G^F})$. Similarly, in multi-agent dilemmas, two copies of an agent might have slightly different local belief states or preferences.

**Operational Proposal (Harsanyi Type-Space Reduction):** Following John Harsanyi's standard technique in game theory, we can unify footnotes 7 and 16 by requiring that $(P, G)$ represent the agent's *prior* world-model and baseline utility function before receiving any local information—including introspective signals about her own preferences or dispositions. Any local variation in preference (such as loving vs. hating smoking in the lesion problem) or local epistemic state is encoded as part of the agent's local observation/type $x \in \mathcal{X}$, while the utility variable $\textsc{V} = \mathcal{U}(\textsc{Outcome}, \textsc{Obs})$ is allowed to depend on $x$. Under this operationalization, the node $\textsc{pfdt}(\underline{P}, \underline{G})$ depends solely on the shared prior structure $(P, G)$, and the policy $\pi : \mathcal{X} \to \mathcal{A}$ maps every local observation and internal type $x$ to an action. In the Smoking Lesion Problem, $\mathcal{X} = \{\textit{love\_smoking}, \textit{hate\_smoking}\}$: intervening on $\textsc{pfdt}(\underline{P}, \underline{G}) = \pi$ does not alter the upstream probability $p = P(\textsc{Lesion} = \textit{lesion})$, and the optimal policy is $\pi^*(\textit{love\_smoking}) = \textit{smoke}$ and $\pi^*(\textit{hate\_smoking}) = \textit{refrain}$.

### 2. Indexical Symmetry in Multi-Agent Models
In the Asymmetric Twin Prisoner's Dilemma above, we assumed that both twins share the exact same model $(P, G)$ and maximize an expected utility $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)]$ under a $50/50$ prior over being in Room $0$ or Room $1$. The source paper does not explicitly spell out how self-locating (indexical) beliefs should be represented in $P$ so that two distinct physical agents possess identical $(P, G)$ descriptions.

**Operational Proposal (Ex Ante Indexical Encoding):** In any multi-agent setting where $k$ physical instances implement P-FDT, the shared distribution $P$ should include an indexical variable $I \in \{1, \dots, k\}$ ("which physical copy am I?") assigned a uniform prior $P(I = i) = 1/k$ (or weighted by the agent's subjective measure over copies), with $\textsc{Obs} = \textsc{Obs}_I$, $\textsc{Act} = \textsc{Act}_I$, and $\textsc{V} = \textsc{V}_I$. Because P-FDT is updateless—selecting $\pi$ *before* plugging in the realized observation $x$—every physical copy $i \in \{1, \dots, k\}$ evaluates the exact same unconditional expectation over $I$, guaranteeing that all copies share the single node $\textsc{pfdt}(\underline{P}, \underline{G})$ and coordinate seamlessly across asymmetric roles.

### 3. Tie-Breaking on Zero-Measure Unpredicted Observations
What happens if a policy $\pi \in \Pi$ must specify an action $\pi(x_0)$ for an observation $x_0 \in \mathcal{X}$ that has strictly zero probability of occurring under $\pi$ *and* is never queried by any predictor? For example, in the *Mechanical Blackmail* problem (Dilemma 8) against a *strictly infallible* predictor ($\epsilon = 0$), if $\pi(\textit{blackmail}) = \textit{refuse}$, the blackmailer never sends the letter ($P(\textsc{Obs} = \textit{blackmail}) = 0$); conversely, if $\pi(\textit{blackmail}) = \textit{pay}$, the blackmailer *always* sends the letter ($P(\textsc{Obs} = \emptyset) = 0$) and the blackmailer's decision does not depend on $\pi(\emptyset)$. More generally, if changing $\pi(x_0)$ has zero effect on $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi)]$, the $\argmax_{\pi \in \Pi}$ operator returns a set of tied policies that disagree at $x_0$.

**Operational Proposal (Trembling-Hand Policy Refinement):** To ensure that $\Pi_{\mathrm{P\text{-}FDT}}(P, G)$ is uniquely well-defined at every observation $x \in \mathcal{X}$, an operational P-FDT agent should evaluate policies in the limit as environmental/predictor noise $\epsilon \to 0^+$ (analogous to Reinhard Selten's trembling-hand perfection), or equivalently apply a lexicographic tie-breaker that maximizes $\mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{pfdt}(\underline{P}, \underline{G}) = \pi), \textsc{Obs} = x_0]$ among policies that tie in unconditional expectation. As we saw in Section 4, any non-zero predictor error $\epsilon > 0$ (such as $\epsilon = 0.01$) automatically breaks the tie on the unpredicted branch, uniquely selecting $\pi_{1,2} = (\textit{1B}, \textit{2B})$.

### 4. Deducing Subjunctive Graphs and Computational Scaling
Finally, Yudkowsky and Soares candidly acknowledge two foundational challenges that apply equally to action-based FDT and P-FDT. First, while Pearl (2000) provides a rigorous methodology for learning causal graphs from physical interventions, we lack a general mathematical theory of counterpossibles (e.g., a formal $\mathtt{true}(\phi)$ operator) for deducing the subjunctive dependency graph $G$ from first principles. Second, moving from action-based FDT to P-FDT expands the optimization domain from $|\mathcal{A}|$ actions to $|\mathcal{A}|^{|\mathcal{X}|}$ policies. In practice, bounded P-FDT agents must restrict $\mathcal{X}$ to a coarse partition of decision-relevant observations or optimize over parameterized policy classes $\Pi_\theta \subset \mathcal{A}^{\mathcal{X}}$.

---

## 7. Conclusion

**Policy functional decision theory (P-FDT)** completes the conceptual shift initiated by functional decision theory. By intervening on the logical node $\textsc{pfdt}(\underline{P}, \underline{G})$ to select a complete policy $\pi : \mathcal{X} \to \mathcal{A}$ before evaluating $\pi(x)$ at the agent's realized observation $x$, P-FDT unifies precommitment, counterfactual reasoning, and multi-agent coordination into a single mathematical criterion. It retains all the triumphs of action-based FDT—one-boxing in Newcomb's problem and Transparent Newcomb, smoking in the lesion problem, paying the driver in Parfit's hitchhiker, and resisting extortion in blackmail dilemmas—while eliminating the need for ad-hoc priors over counterfactual observations and enabling agents to cooperate with copies and predictors even when they face asymmetric information.

## References

* Dai, Wei. 2009. "Towards a New Decision Theory." *Less Wrong*, August 13, 2009.
* Drescher, Gary L. 2006. *Good and Real: Demystifying Paradoxes from Physics to Ethics*. Cambridge, MA: MIT Press.
* Gibbard, Allan, and William L. Harper. 1978. "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, vol. 1, edited by C. A. Hooker, J. J. Leach, and E. F. McClennen. Boston: D. Reidel.
* Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. New York: Cambridge University Press.
* Kleene, Stephen Cole. 1938. "On Notation for Ordinal Numbers." *Journal of Symbolic Logic* 3 (4): 150–155.
* Parfit, Derek. 1986. *Reasons and Persons*. New York: Oxford University Press.
* Pearl, Judea. 1996. "Causation, Action, and Counterfactuals." In *6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-'96)*, 51–73.
* Pearl, Judea. 2000. *Causality: Models, Reasoning, and Inference*. New York: Cambridge University Press.
* Peirce, Charles Sanders. 1934. *Collected Papers of Charles Sanders Peirce*, vol. V. Cambridge, MA: Harvard University Press.
* Soares, Nate, and Benja Fallenstein. 2015. "Toward Idealized Decision Theory." arXiv:1507.01986 [cs.AI].
* Yudkowsky, Eliezer. 2010. *Timeless Decision Theory*. San Francisco, CA: The Singularity Institute.
* Yudkowsky, Eliezer, and Nate Soares. 2017. "Functional Decision Theory: A New Theory of Instrumental Rationality." arXiv:1710.05060v2.
````

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Core Focus**

I'm now zeroing in on defining the core focus for the essay. The goal is to provide a clear explanation of Policy Functional Decision Theory and its practical applications. This means I need to strike a balance between theoretical depth and accessible examples. I'm focusing on the intended audience to determine the most effective approach.


**Refining the Approach**

I'm now carefully examining the Yudkowsky and Soares paper, particularly the policy-selection passage and related footnotes. I am considering the essay's constraints and instructions, which are guiding how I present P-FDT (policy functional decision theory). The audience is mathematically literate but interested in philosophical motivation, so it will be important to balance theoretical depth with practical applications. I'm taking a methodological approach, aiming for clarity in definitions, examples, and explanations.


**Clarifying Scope & Constraints**

I'm now clarifying the scope, ensuring I distinguish the source's claims from my own additional assumptions. I aim for a mathematically-grounded but readable essay on P-FDT, using examples. The conclusion will be brief, avoiding repetition, lengthy bibliographies, and appendices. I will also be faithful to the provided paper's policy-selection passage and footnotes while using "P-FDT" consistently. I'm targeting between 2,600 and 2,800 words.


**Analyzing Policy Iteration**

I am now focusing on the implications of policy iteration within FDT, as described in footnotes 7 and 16. It looks like the distinction between iterating over actions versus policies, while significant in multi-agent contexts, doesn't impact the core arguments in the paper. I'm noting this distinction, as it is key to how the model works. I am analyzing how this works within the context of Section 5 and 9's standard FDT formulation, as this affects the agent's calculations.


**Examining Interventions**

I am now closely examining how FDT and P-FDT handle interventions, specifically the shift from node intervention to policy intervention. I'm focusing on scenarios like Transparent Newcomb and XOR Blackmail, which highlight the differences in action selection based on observations. The move to P-FDT, which intervenes on a policy instead of an action, is the crux of these considerations.


**Investigating Mathematical Structure**

I'm now diving into the formal aspects, specifically Footnotes 7 and 16. The policy mappings from observations to actions are clear, but I'm considering the arguments passed to the policy-selection function versus the policy itself. In standard FDT, inputs are taken as (P, G, x). The goal now is to analyze how the input $x$ is factored into $\pi$.


**Analyzing Policy Formulations**

Now I'm focusing on the mathematical formulation, specifically the role of the prior model (P, G). I'm carefully dissecting how the policy $\Pi^*$ is defined and how the action is eventually chosen given an actual observation $x$. I'm exploring the implications if the policy function $\pi$ maps either just $x$ to $a$, or $(P, G, x)$ to $a$. I should explicitly discuss these options, as this is something the original source leaves open.


**Exploring Parameterization Options**

I'm now investigating parameterization, considering two key possibilities for the policy function $\pi$: either $\pi$ maps the observation to the action, or it takes the world-model and observation as inputs. I'm focusing on the implications, particularly how the Smoking Lesion problem highlights the utility of the latter option for agents uncertain about their own models. I'm carefully analyzing how this impacts decision-making.



**Investigating Mathematical Divergence**

I'm now diving into the divergence between action-based FDT and P-FDT, especially within the single-agent context. I am analyzing how interventions affect the agent's calculations, especially in Transparent Newcomb. The focus is on the difference when Fiona intervenes only on the outcome when the box is full, leaving the other outcome to the agent's prior belief. The aim is to work out the exact mathematical mechanics.


**Decomposing the Utility**

I'm now carefully analyzing the decomposition of expected utility in Transparent Newcomb and whether the observation $\textsc{Obs}$ depends on the policy's action at $x = \textit{full}$. I've realized that when $\textsc{Accurate} = \textit{accurate}$, the box and thus $\textsc{Obs}$ *does* depend on the policy's action. This means the actual action taken at $x = \textit{empty}$ is affected by that original action at $x = \textit{full}$. I'm working through the implications for calculations within the action-based FDT framework, specifically in Section 6.


**Analyzing Prior Dependence**

I'm now carefully examining the Transparent Newcomb calculation, specifically Fiona's need for a prior, $q$, in action-based FDT. I've realized that her need for this un-intervened prior introduces a potential for inaccurate calculations and dependency issues. P-FDT avoids these problems. Now I'm carefully analyzing how the policy is affected by this.


**Constructing Multi-Agent Dilemmas**

I'm now working on crafting a concrete mathematical example to illustrate the divergence between action-based FDT and P-FDT in multi-agent dilemmas. I'm focusing on scenarios with asymmetric observations to explore coordination problems. Specifically, I'm constructing a case with two twins, each observing a different private signal, and will analyze how each decision theory handles their potential interactions. The goal is to highlight the benefits of P-FDT in such scenarios.


**Developing a Coordination Dilemma**

I'm now carefully developing the twin dilemma example. I have defined the nature's output, and the payoff structure for cooperation and defection. I'm focusing on the action-based FDT perspective with asymmetric information, which causes each twin to make decisions in isolation. I'm calculating the implications when each twin makes a decision, given different observed signals.


**Modeling the Asymmetric Dilemma**

I'm working on the asymmetric twin Prisoner's Dilemma, carefully detailing the payoff structure for each twin's choices based on their individual observations. I'm focusing on the action-based FDT perspective with asymmetric information, and I'm modeling how the action-based FDT agent in Room 0 intervenes on their own action, treating the twin's action in Room 1 as fixed. I'm now making it a true Prisoner's Dilemma across observations.


**Refining Utility Calculations**

I am now refining the payoff structure for each twin based on observations, ensuring the asymmetric Prisoner's Dilemma dynamics are correctly modeled under action-based FDT. The twins' actions are now defined by what is observed in each room. Each agent evaluates its utility by intervening on its own action, treating its twin's as fixed, and this is leading to the core divergence.



**Calculating Policy Payoffs**

I'm now carefully calculating the payoffs within the P-FDT framework for the asymmetric twin dilemma, ensuring policy selection aligns with cooperative outcomes. The twins' actions will be set through a shared policy. The goal is to highlight how P-FDT can achieve a better outcome.



**Revising Policy Outcomes**

I'm now meticulously reviewing the twin Prisoner's Dilemma calculations in the P-FDT framework. I've reevaluated the expected utilities of each policy for both twins, ensuring policy selection aligns with the desired cooperative outcome. The twins' actions will be fixed through a shared policy. The goal is to solidify this.



**Clarifying Multi-Agent Dynamics**

I'm revisiting the implications of policy iteration, especially concerning Footnotes 7 and 16. The key is now fully grasped: in multi-agent contexts, iterating over policies (mappings from observations to actions) instead of actions matters. In the symmetric twins problem, the identical observations ensure identical action selection. Now I'm considering the asymmetric information scenario.


**Analyzing Twin Divergence**

I'm now carefully analyzing the divergence in the twins' decision-making under different observations in the asymmetric dilemma. Specifically, action-based FDT with differing observations effectively severs the subjunctive link between what the twins do when they observe each possible signal. On the other hand, P-FDT intervenes on the policy *before* the twins make observations. This, therefore, will lead to different behavior.


**Evaluating Policy Predictions**

I am now assessing scenarios where P-FDT offers a unique advantage, especially in single-agent dilemmas. I'm focused on cases where a predictor evaluates the entire policy across multiple observations, like the coin-flip example, which is similar to Transparent Newcomb. The goal is to highlight instances where P-FDT's ability to intervene on the policy itself creates different predictions.


**Addressing Policy Input Choices**

I'm now carefully addressing open questions from Footnotes 7 and 16, particularly regarding the policy function $\pi$'s domain. While Footnote 7 states policies map observations to actions, Footnote 16 suggests additional inputs. I'm focusing on the mathematical inputs to the policy function itself. I'm determining which specific inputs are key to an agent's calculation.



**Formalizing Policy Inputs**

I'm now formalizing the two key approaches to the policy function's inputs. The first is an **Observation-Policy formulation**, where the policy maps only the observation, $x$, to the action, $a$, with node $\textsc{pfdt}(\underline{P}, \underline{G})$. However, I'm finding the second, the **Meta-Policy / Full-Input formulation**, where $\pi$ takes all decision problem inputs, like the world-model and utility function, is also important. This is critical for single-agent dilemmas.


**Formalizing the Meta-Model**

I'm now formalizing a meta-model for Harsanyi-type space reduction, where local beliefs and preferences are mapped into observations ($x$). This is clean and operational, and it's standard in game theory!

**Addressing Zero-Probability Observations**

I'm now grappling with how P-FDT handles actions based on observations that never occur, like in the Mechanical Blackmail example. I'm focusing on the implications of $\pi(x)$ when $x$ has zero probability, and how this affects the expected utility calculation. The challenge now is understanding how the model handles ties in action selection when a zero-probability observation causes a tie.


**Clarifying Updateless Properties**

Now, I'm clarifying that each agent in P-FDT maximizes their personal utility from an initial (updateless) perspective before considering their observation, $x$. For twins to share the same model, $V$ must be defined indexically. P-FDT's updateless nature ensures they have the same initial prior. I'm focusing on the link between updatelessness and the indexical definition of $V$.


**Calculating Complexity Increase**

I'm now carefully examining the computational complexity. The move from actions to policies introduces a significant increase in the search space.  My focus is on understanding the implications of the size of the subjunctive graph $G$, and how the move to P-FDT impacts it. The computational implications of moving from $|\mathcal{A}|$ to $|\mathcal{A}|^{|\mathcal{X}|}$ are quite important here.


**Refining Formal Structure**

I'm now refining the formal structure, starting from the source's goal to show the philosophical and counterfactual machinery of P-FDT. I'm focusing on the mathematical formulation and showing how to apply it to single- and multi-agent dilemmas. I'm resolving the formal questions that the source leaves open. I am emphasizing updatelessness as a key feature.


**Formalizing Decision Equations**

I'm now precisely formalizing the core decision equations to clearly contrast EDT, CDT, and action-based FDT. My focus is on defining the key components: outcome space, action space, observation space, utility, world-model, and the equations themselves. I'm prioritizing clarity.


**Formalizing Key Equations**

I'm now precisely formatting the core equations, highlighting that policy selection, $\Pi$, is crucial for understanding P-FDT. I'm focusing on defining the key components of the decision problem: outcome space, action space, observation space, utility, world-model, and the equation itself. I'm focusing on clarity and explicitness.


**Calculating Single-Agent Payoffs**

I'm now carefully calculating and organizing the expected utilities for each of the four policies in the Transparent Newcomb problem, ensuring the structural equations and policy selection are explicitly clear. I'm focusing on the mathematical formulation of the policies and associated payoffs for the one-box and two-box strategies. This helps solidify the single-agent P-FDT case, as I go.


**Refining P-FDT Benefits**

I'm now carefully examining the Transparent Newcomb problem to extract mathematical advantages of P-FDT in the single-agent case. I'm focusing on the exogenous prior in action-based FDT, and how P-FDT eliminates that free parameter via simultaneous policy intervention. This streamlines the model.


**Constructing Dilemma Solution**

I'm now building the asymmetric twin prisoner's dilemma, constructing an environment where action-based FDT fails to cooperate with asymmetric inputs while P-FDT can, demonstrating Footnote 16's claim. I am focusing on showing the divergences of the math when we have the twin's asymmetrical observations.



**Operationalizing Utility Uncertainty**

I'm now integrating local variations in beliefs and preferences into the observation variable ($x$), following Harsanyi's type-space approach. This allows policy functions to uniformly handle both environmental observations and preference uncertainty. I'm also ensuring identical agents share the same prior through indexical definitions.


**Refining Action Selection**

I'm now zeroing in on defining action selection in cases of underdetermination, especially where zero-probability observations are involved, like Mechanical Blackmail. My goal is to add a small trembling-hand refinement to achieve well-defined outcomes, even with no observations. It's a key part of the formal system.



```
