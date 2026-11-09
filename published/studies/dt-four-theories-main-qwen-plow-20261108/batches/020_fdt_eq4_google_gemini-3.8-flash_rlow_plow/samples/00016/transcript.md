# 020_fdt_eq4_google_gemini-3.8-flash_rlow_plow / 00016

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/9d25e9a1-0fd9-42ef-89d5-f12888e91eac/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/9d25e9a1-0fd9-42ef-89d5-f12888e91eac/call_0/response.raw) · finish: `stop`

### Visible response

````text
# Intervening on the Type: The Mathematics and Mechanics of Action Functional Decision Theory (A-FDT)

## 1. Introduction: The Dialectic of Rational Choice

Normative decision theory seeks a formal criterion for selecting instrumental actions. For decades, the field has been defined by an intractable dialectic between two paradigms: **Evidential Decision Theory (EDT)** and **Causal Decision Theory (CDT)**. 

EDT, traceable formally to Richard Jeffrey, instructs an agent to choose an action that serves as the best possible news about the state of the world. By maximizing expected utility conditional on the physical act, EDT succeeds in predictive dilemmas like Newcomb’s Problem—prescribing "one-boxing" and walking away with a million dollars. Yet it fails catastrophically in common-cause dilemmas like Skyrms' Smoking Lesion problem or Soares and Fallenstein's XOR Blackmail, where it errantly attempts to "manage the news" by suppressing symptoms of background conditions it cannot influence.

CDT, codified by David Lewis, Allan Gibbard, William Harper, and James Joyce, repairs this defect by introducing physical causation. Utilizing counterfactuals or causal interventions, CDT evaluates an act solely by what its physical execution causally brings about downstream in time. While CDT smokes in the Smoking Lesion problem, it leaves the million dollars behind in Newcomb’s Problem, defects against psychological twins in the Prisoner's Dilemma, and perishes in Parfit’s desert. In the presence of accurate environmental predictors, CDT’s insistence that the past is causally fixed leads it into severe dynamic instabilities (e.g., Death in Damascus), rendering it vulnerable to extortion and unable to endorse its own future use.

**Action Functional Decision Theory (A-FDT)**—the formal action-level variant of Functional Decision Theory introduced by Eliezer Yudkowsky and Nate Soares—breaks this deadlock. Rather than choosing between conditioning on an act (EDT) or physically intervening on an act (CDT), A-FDT shifts the fundamental ontology of choice. 

An A-FDT agent does not ask, *"What happens if my physical body executes act $a$?"* Instead, the agent conceives of their choice process as the instantiation of a fixed mathematical function $F$, asking: 
$$\text{``Which output of this very mathematical function yields the best outcome?''}$$

By evaluating counterfactuals through interventions on the **type** (the logical decision procedure) rather than the **token** (the localized physical action), A-FDT achieves the highest utility across both classes of dilemmas. Below, we formalize A-FDT, examine its operative mechanisms, and trace how it resolves classic problems of rational agency.

---

## 2. Foundations: The Tripartite Comparison

All three theories operate within an expected utility framework. Following Joyce's general formulation, let $\mathcal{A}$ be a finite set of actions, $\mathcal{X}$ a countable set of observation histories, and $\mathcal{O} = \{o_1, o_2, \ldots\}$ a countable set of mutually exclusive outcomes. Let $\Util: \mathcal{O} \to \mathbb{R}$ be a bounded utility function, and define the random variable $\VV \coloneqq \Util(\Outcome)$. 

The core expected utility formula evaluates an action $a \in \mathcal{A}$ given observations $x \in \mathcal{X}$ via:
\begin{equation}
\label{eq:gen_eu}
\mathcal{EU}(a) = \sum_{j} P(a \then o_j ;\, x) \cdot \Util(o_j) = \EE\left[\VV \cond a \then \cdot \,;\, x\right],
\end{equation}
where $\then$ denotes the conditional connective for decision hypotheticals. Joyce's representation theorem demonstrates that agents obeying basic consistency axioms maximize Equation \eqref{eq:gen_eu}; the divergence between decision theories lies entirely in their interpretation of the hypothetical connective $\then$.

### 2.1 Evidential Decision Theory (EDT)
EDT identifies the decision hypothetical with standard Bayesian conditionalization on the physical act token $\Act = a$:
\begin{equation}
\label{eq:edt}
\EDT(P, x) \coloneqq \argmax_{a \in \mathcal{A}} \EE_P\left[\VV \cond \Obs = x, \Act = a\right].
\end{equation}
Because conditioning tracks all statistical correlations, EDT conflates correlation with agency. If an agent's prior $P(\Act = a) = 0$, the hypothetical is undefined. More critically, if $\Act$ correlates with a non-causal background state (e.g., a genetic lesion), EDT chooses $a$ to steer its belief about that background state, leading to symptomatic avoidance.

### 2.2 Causal Decision Theory (CDT)
CDT interprets the decision hypothetical as an intervention on the physical act variable $\Act$. Utilizing Judea Pearl's structural causal models, the agent's world-model is a pair $(P, G)$, where $G$ is a directed acyclic graph (DAG) representing causal mechanisms. CDT uses the graph surgery operator $\Do(\Act = a)$, which severs all incoming causal edges to $\Act$ while leaving all non-downstream variables untouched:
\begin{equation}
\label{eq:cdt}
\CDT(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \EE_P\left[\VV \cond \Do(\Act = a), \Obs = x\right].
\end{equation}
Because past predictions are temporally and causally upstream of the physical act $\Act$, $G$ contains no directed path from $\Act$ to the past prediction. Hence, the operator $\Do(\Act = a)$ leaves the prediction strictly invariant:
$$P(\Var{Prediction} \mid \Do(\Act = a)) = P(\Var{Prediction}).$$
CDT therefore views the past as unalterable, diagnosing one-boxing in Newcomb's Problem as an attempt at backward causation.

---

## 3. Mathematical Formulation of A-FDT

### 3.1 The Formal Rule
Action Functional Decision Theory rejects the premise that an agent's agency is localized to physical interventions in spacetime. In A-FDT, the agent's world-model incorporates not only physical events, but also variables representing the outputs of abstract mathematical functions.

Let $\FDTvar$ denote the agent's formal decision algorithm. Let $\underline{P}$, $\underline{G}$, and $\underline{x}$ denote the syntactic encodings (dequoted representations) of the probability distribution $P$, the dependency graph $G$, and the current observation history $x$. The agent's model contains a discrete variable, denoted $\FDTvar(\underline{P}, \underline{G}, \underline{x})$, representing the logical output of this algorithmic procedure.

The primary formal rule of A-FDT—**Equation (4)** of Yudkowsky and Soares (2017)—is defined as:
\begin{equation}
\label{eq:fdt}
\FDT(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \EE_P\left[\VV \cond \Do\left(\FDTvar(\underline{P}, \underline{G}, \underline{x}) = a\right)\right].
\end{equation}

```
          CDT: Intervenes on Token                     A-FDT: Intervenes on Type
          
             [ Predisposition ]                        [ Decision Function ]
               /            \                         FDT(P, G, x)  <== DO INTERVENTION
              /              \                               /              \
             v                v                             v                v
     [ Prediction ]      [ Act = a ] <== DO         [ Prediction ]       [ Act = a ]
            |                 |                            |                 |
            v                 v                            v                 v
        [ Box B ]         [ Outcome ]                  [ Box B ]         [ Outcome ]
                 \       /                                      \       /
                  v     v                                        v     v
                 [ Utility ]                                    [ Utility ]
```

### 3.2 Key Structural Differences from CDT
A mathematical comparison between Equation \eqref{eq:cdt} and Equation \eqref{eq:fdt} reveals two structural transformations:

1. **Intervention Target (Type vs. Token):** CDT intervenes on the physical act token $\Act$. A-FDT intervenes on the logical node $\FDTvar(\underline{P}, \underline{G}, \underline{x})$. If an external entity (such as a Newcomb predictor, an algorithmic clone, or an identical twin) runs a simulation of this decision process, that external entity's state is causally or subjunctively downstream of the logical output node $\FDTvar(\cdot)$. Intervening on $\FDTvar(\cdot)$ propagates changes simultaneously to the agent's physical limbs *and* to all environmental processes that depend upon that same computation.
2. **Treatment of Observations (Node Shifting vs. Conditioning):** When CDT updates on an observation $x$, it conditions the distribution: $\EE[\VV \mid \Do(\Act=a), \Obs=x]$. In contrast, Equation \eqref{eq:fdt} features **no** explicit conditioning on $\Obs = x$ inside the expectation. Instead, A-FDT handles observation by **shifting the target of intervention**. When the observation changes from $x_1$ to $x_2$, an A-FDT agent does not condition on $x_2$; it transitions from intervening on $\FDTvar(\underline{P}, \underline{G}, \underline{x_1})$ to intervening on $\FDTvar(\underline{P}, \underline{G}, \underline{x_2})$. 

This subtle mechanism gives A-FDT an "updateless" character. It allows an agent currently observing $x$ to evaluate counterfactuals in which, had the decision procedure yielded a different output, the agent *might never have observed $x$ in the first place*.

---

## 4. Subjunctive Dependence and Counterpossible Conditioning

The philosophical foundation of A-FDT is **subjunctive dependence**. Yudkowsky and Soares define it by analogy:
$$\text{A-FDT is to subjunctive dependence as CDT is to causal dependence.}$$

### 4.1 Defining the Dependency
Two physical variables $Y_1$ and $Y_2$ subjunctively depend on a mathematical function $f$ if their physical realizations track the output of $f$. 
* **The Calculator Analogy:** If two calculators on opposite sides of the Earth evaluate $6288 + 1048$, both display $7336$. Their outputs are correlated not because of a direct causal signal passing between them, but because both physical systems instantiate the same abstract addition function. If we ask what Calculator 2 would display if the addition function yielded $7337$, the answer is $7337$.
* **Causal Dependence as a Subcase:** Physical causation is simply a temporal, locally instantiated form of subjunctive dependence. If a scribe writes down the display of Calculator 1, her note causally depends on the display and subjunctively depends on the arithmetic function.

### 4.2 The Challenge of Counterpossibles
Equation \eqref{eq:fdt} reuses Pearl’s $\Do$-operator on an expanded graph $G$ whose vertices include mathematical algorithms. However, this is an engineering abstraction. In classical logic and probability theory, the statement:
$$\FDTvar(\underline{P}, \underline{G}, \underline{x}) = a$$
is either a mathematical truth or a mathematical falsehood. If it evaluates to $a^*$, considering an alternative $a \neq a^*$ requires evaluating a **counterpossible conditional**—a conditional whose antecedent is mathematically or logically impossible.

The source text explicitly acknowledges this limitation: Pearl's framework provides a sound epistemology for learning causal graphs from interventions, but **no complete formal theory yet exists for deducing the structure of logical and mathematical dependencies from empirical data**. 

In an idealized setting, one would replace the causal graph surgery with a general logical evaluation operator, $\True(\phi)$, yielding:
$$\FDT^*(P, x) = \argmax_{a \in \mathcal{A}} \EE_P\left[\VV \cond \True\left(\FDTvar(\underline{P}, \underline{x}) = a\right)\right].$$
Because defining conditional probabilities on mathematical contradictions is an open research problem in logical induction (e.g., Demski 2012, Hutter et al. 2013, Potyka and Thimm 2015), Equation \eqref{eq:fdt} bypasses this by taking the logical dependency graph $G$ as an **axiomatic input**. Within this graph, abstract computations are treated as parent nodes whose children include physical actions and predictions.

---

## 5. Deconstructing Classic Dilemmas under A-FDT

To observe Equation \eqref{eq:fdt} in practice, let us examine how an A-FDT agent (Fiona), a CDT agent (Carl), and an EDT agent (Eve) resolve core decision problems.

### 5.1 Newcomb’s Problem
An agent faces two boxes: Box A (transparent, containing \$1,000) and Box B (opaque, containing \$1,000,000 or \$0). A 99% reliable predictor placed \$1,000,000 in Box B iff she predicted the agent would forgo Box A. Box B is already sealed.

* **CDT Evaluation:** Carl constructs a causal graph where $\Act \to \VV$ and $\Var{Box B} \to \VV$. The predictor's past action determines $\Var{Box B}$. Because there is no directed edge $\Act \to \Var{Box B}$, $\Do(\Act = a)$ leaves $P(\Var{Box B} = \Val{full}) = p$ completely unaltered. Carl computes:
  $$\EE_{\CDT}[\VV \mid \Do(\Val{twobox})] = p(\$1,001,000) + (1-p)(\$1,000) = p(\$1,000,000) + \$1,000.$$
  $$\EE_{\CDT}[\VV \mid \Do(\Val{onebox})] = p(\$1,000,000).$$
  Two-boxing causally dominates by exactly \$1,000. Carl two-boxes and walks away with \$1,000.
* **A-FDT Evaluation:** Fiona’s graph $G^F$ identifies that the predictor's simulation and Fiona's physical body both subjunctively depend on the node $\FDTpg$. Thus, edges extend from $\FDTpg$ to both $\Act$ and $\Var{Prediction}$. 
  Applying Equation \eqref{eq:fdt}:
  $$\EE_{P^F}\left[\VV \cond \Do(\FDTpg = \Val{onebox})\right] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000.$$
  $$\EE_{P^F}\left[\VV \cond \Do(\FDTpg = \Val{twobox})\right] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$
  Fiona one-boxes. The predictor, simulating this very algorithm, leaves \$1,000,000 in Box B. Fiona walks away rich.

### 5.2 The Smoking Lesion Problem
Smoking is correlated with fatal lung cancer ($p=0.99$ vs. $p=0.01$). However, the correlation is driven entirely by a common genetic lesion that disposes carriers to crave smoking and independently triggers cancer. Smoking yields \$1,000 utility; health is worth \$1,000,000. Smoking has zero causal influence on cancer.

* **EDT Failure:** Eve calculates $\EE[\VV \mid \Act = \Val{refrain}]$ vs $\EE[\VV \mid \Act = \Val{smoke}]$. Conditioning on smoking dramatically increases the posterior probability of possessing the fatal lesion:
  $$\EE_{\EDT}[\VV \mid \Val{refrain}] \approx \$990,000 \quad \text{vs.} \quad \EE_{\EDT}[\VV \mid \Val{smoke}] \approx \$11,000.$$
  Eve irrationally starves herself of nicotine to "manage the news" about her genome.
* **A-FDT Resolution:** Fiona’s graph $G^F$ represents the lesion as determining her preference regime (e.g., whether she is running $\FDTvar(\underline{P_S}, \underline{G})$ or $\FDTvar(\underline{P_R}, \underline{G})$). Crucially, the occurrence of lung cancer subjunctively depends on the physical variable $\Var{Lesion}$, **not** on the algorithmic variable $\FDTvar(\underline{P_S}, \underline{G})$.
  Consequently:
  $$P(\Var{Lesion} \mid \Do(\FDTvar(\underline{P_S}, \underline{G}) = \Val{smoke})) = P(\Var{Lesion}) = p.$$
  The intervention on the logical decision function breaks the evidential correlation with the biological lesion. Because the lesion does not simulate or track Fiona's algorithm, cancer is invariant under the intervention. Fiona smokes, earning the additional \$1,000 while remaining clear of EDT’s self-deception.

### 5.3 The Transparent Newcomb Problem and Parfit’s Desert
The power of A-FDT is most pronounced in problems that combine prior prediction with complete subsequent observation.
* **Transparent Newcomb:** Both boxes are transparent. Box B is visibly full of \$1,000,000. The predictor filled it iff she predicted the agent would leave Box A (\$1,000) behind *upon seeing that both boxes are full*.
* **Parfit's Hitchhiker:** An agent is dying of dehydration in the desert. A driver with a near-perfect lie detector offers a ride to town, provided the agent will withdraw \$1,000 upon reaching town to pay him. In town, the driver cannot legally enforce payment.

In both cases, CDT and EDT prescribe defecting. Carl and Eve, upon finding themselves safely in town or staring at a full Box B, evaluate actions holding their present observations fixed. The ride has already occurred; Box B is already full. Defection yields an unpunished \$1,000 bonus. However, because the driver and predictor accurately foresee this reasoning, Carl and Eve are left to die in the desert or face empty boxes.

Now consider Fiona in Transparent Newcomb. Fiona observes $\Obs = \Val{full}$. Applying Equation \eqref{eq:fdt}, she does not condition on $\Obs = \Val{full}$. Instead, she shifts her intervention target to the node representing her algorithm when given that observation:
$$\FDT(P^F, G^F, \Val{full}) = \argmax_{a} \EE\left[\VV \cond \Do\left(\FDTpgv{full} = a\right)\right].$$
In Fiona's dependency graph, the predictor's past prediction depends on the output of $\FDTpgv{full}$. If this node outputs $\Val{twobox}$, then the predictor in the past reliably predicted $\Val{twobox}$, which means Box B was never filled, and Fiona would have observed $\Obs = \Val{empty}$.
Fiona computes:
$$\EE[\VV \mid \Do(\FDTpgv{full} = \Val{onebox})] = 0.99(\$1,000,000) + 0.01 q(\$1,000) = \$990,000 + 10q.$$
$$\EE[\VV \mid \Do(\FDTpgv{full} = \Val{twobox})] = 0.01(\$1,001,000) + 0.99 q(\$1,000) = \$10,010 + 990q.$$
(where $q$ is the probability of two-boxing if the box had been empty).
Fiona one-boxes! Even though she can see the money with her eyes, she recognizes that her current thoughts are the very algorithm being evaluated by the past predictor. To be the sort of agent that one-boxes upon seeing a full box is the sole functional configuration that causes the box to be filled in the first place. Fiona pays the hitchhiker and one-boxes in the transparent dilemma, escaping the desert and accumulating maximal wealth.

---

## 6. Structural Comparison Across Canonical Dilemmas

The differing epistemic perspectives of EDT, CDT, and A-FDT produce starkly divergent prescriptions across standard decision-theoretic problems:

| Decision Problem | Evidential Decision Theory (EDT) | Causal Decision Theory (CDT) | Action Functional Decision Theory (A-FDT) | Why A-FDT Wins |
| :--- | :--- | :--- | :--- | :--- |
| **Newcomb’s Problem** | One-box ($\$1\text{M}$) | Two-box ($\$1\text{K}$) | **One-box** ($\$1\text{M}$) | Preserves subjunctive dependence between algorithm and predictor's model. |
| **Smoking Lesion** | Refrain ($\$0$) | Smoke ($\$1\text{K}$) | **Smoke** ($\$1\text{K}$) | Eliminates non-causal statistical correlation; lesion does not simulate the decision function. |
| **Twin Prisoner’s Dilemma** | Cooperate ($\$1\text{M}$) | Defect ($\$1\text{K}$) | **Cooperate** ($\$1\text{M}$) | Intervenes on the type; both twins execute the identical decision function. |
| **Transparent Newcomb** | Two-box ($\$0$) | Two-box ($\$0$) | **One-box** ($\$1\text{M}$) | Intervenes on $\FDTpgv{full}$, accounting for how the decision function determines the observation itself. |
| **Parfit’s Hitchhiker** | Refuse to pay (Dies) | Refuse to pay (Dies) | **Pay** ($\$999\text{K}$) | Prevents desert abandonment by validating the driver's prediction of honesty. |
| **XOR Blackmail** | Pays blackmail (Exploited) | Refuses to pay | **Refuses to pay** | Recognizes letter's receipt depends on algorithm, but infestation state does not. |
| **Death in Damascus** | Dies in Damascus | Oscillates / Unstable | **Remains in Damascus** | Eliminates cyclic instability; saves \$1,000 travel cost facing inevitable doom. |

---

## 7. Operationalizing A-FDT in Arbitrary Decision Problems

To allow a researcher or agent to apply A-FDT to an arbitrary, unfamiliar decision setting, we formalize the conceptual and mechanical procedure implied by Equation \eqref{eq:fdt}.

```
                      OPERATIONAL RECIPE FOR A-FDT
                      
1. Specify State Space
   Define acts A, observations X, outcomes O, utilities U(o).
   
2. Construct Augmented Model (P, G)
   - Include physical and environmental variables.
   - For every distinct observation history x in X, instantiate a discrete 
     variable FDT(P, G, x) representing the output of the agent's algorithm.
   - Connect FDT(P, G, x) -> Act.
   
3. Map Subjunctive Dependencies
   - Identify every system S that predicts, simulates, or mirrors the agent.
   - Draw directed edges: FDT(P, G, x) -> S.
   - If S determines observation x', draw S -> Obs.
   - Do NOT draw edges from FDT(P, G, x) to common causes that merely 
     correlate statistically without tracking/simulating the algorithm.
     
4. Identify Current Observation
   Let the agent's real-time observation history be x*.
   
5. Apply Equation (4)
   Do NOT condition on Obs = x*. 
   Target the intervention node FDT(P, G, x*).
   For each a in A:
     - Set FDT(P, G, x*) = a via Pearl's do-operator.
     - Propagate values downstream through G.
     - Compute EU(a) = \sum U(o) * P(o | do(FDT(P, G, x*) = a)).
     
6. Execute Optimal Output
   Execute a* = argmax EU(a).
```

### 7.1 Where the Source Leaves Questions Open (And How to Close Them)
Applying the operational recipe above to complex problems exposes several foundational gaps left unresolved in the source text:

1. **The Graph Construction Problem:** The source assumes $G$ is given. In unfamiliar, non-engineered settings, how does an agent determine whether an environmental correlation is an instance of subjunctive dependence (requiring an edge from $\FDTvar$) or mere common cause (requiring isolation)?
   * *Proposed Operational Interpretation:* An environmental node $Y$ should be granted an incoming edge from $\FDTvar(\underline{P}, \underline{G}, \underline{x})$ if and only if $Y$ is produced by a physical process whose mutual information with the agent's action is mediated by an explicit or implicit model of the agent’s computational steps (a computational simulation, behavioral extrapolation, or shared source code).
2. **Infinite Regress and Self-Reference (Quining):** The node $\FDTvar(\underline{P}, \underline{G}, \underline{x})$ contains syntactic encodings of the very distribution $P$ and graph $G$ in which it is embedded. Yudkowsky and Soares appeal to Kleene’s second recursion theorem to demonstrate mathematical consistency. In an operational algorithm, this requires the agent's model to employ Gödelian self-reference or quined strings, preventing infinite unrolling of meta-models.
3. **Action vs. Policy Selection:** The authors note in passing that their fully realized theory actually intervenes on the entire **policy** $\pi: \mathcal{X} \to \mathcal{A}$ rather than on actions indexed by observation histories. Intervening on individual action nodes $\FDTpgv{x}$ (as formalized in Equation \eqref{eq:fdt}) is termed **A-FDT**. Policy-FDT avoids potential coordinate problems in complex multi-stage games by optimizing the global behavioral strategy upfront. For single-stage predictive dilemmas, however, A-FDT via Equation \eqref{eq:fdt} captures the identical behavioral invariant.

---

## 8. Philosophical Implications: Dominance, Time Consistency, and Fairness

### 8.1 The Relativization of Dominance
The central philosophical defense of CDT has always been the **Principle of Dominance**: if action $a$ yields a strictly better outcome than $b$ across all possible states of the world, it is irrational to select $b$. 

A-FDT decisively refutes dominance as an objective adjudicator between decision theories. Dominance is not theory-neutral; it is inherently parameter-dependent upon how a theory constructs its counterfactuals:
* In **CDT hypotheticals**, states of the world hold the predictor's past prediction fixed while varying the agent’s physical action. Two-boxing "dominates."
* In **EDT hypotheticals**, states of the world are updated via conditional probabilities. Refraining from smoking "dominates."
* In **A-FDT hypotheticals**, states of the world hold subjunctive dependencies fixed while varying the output of the decision procedure. One-boxing "dominates."

Because every decision theory generates its own endogenous dominance criterion, appealing to dominance to dismiss A-FDT is entirely question-begging. The ultimate arbiter must be instrumental success: **the average expected utility attained across environments**.

### 8.2 Dynamic Consistency Without Binding
A rational agent, having adopted an optimal plan, should not instantly experience regret and desire self-modification upon the arrival of costless information. Yet CDT is notoriously dynamically inconsistent: a CDT agent would pay money to bind herself to one-box before meeting the predictor, but will instantly two-box if the binding fails. Joyce (2012) bites this bullet, arguing that rationality simply requires accepting temporal regret.

A-FDT restores dynamic consistency without physical precommitments. Because an A-FDT agent accounts for how her decision rule is represented in the environment across time, she automatically behaves in the moment precisely as she would have rationally bound herself to behave in advance. She does not assign negative expected value to information (avoiding the information-blinding traps of EDT), nor does she require Jeffrey-style ratification procedures to break deliberation cycles.

### 8.3 The Demarcation of "Fair" Problems
CDT defenders often object that Newcomb’s Problem is "unfair"—that it penalizes agents simply for being rational. One can easily construct an absurd "Alphabetical Decision Theory" that always chooses the lexicographically earliest action, and then construct a game where an eccentric billionaire awards \$1,000,000 only to agents following Alphabetical Decision Theory.

Yudkowsky and Soares draw a sharp line: a decision dilemma is **fair** if the environment conditions its payouts exclusively on the agent's **actions or predictions of actions**, rather than directly inspecting the syntactic machinery of the agent's source code. Newcomb’s predictor does not punish CDT because it hates CDT; it punishes two-boxers because they predictably two-box. All an agent needs to do to receive the payout is reliably output $\Val{onebox}$. A-FDT agents thrive because they retain the agency to predictably output the winning action.

---

## 9. Conclusion

Action Functional Decision Theory represents an ontological shift in the formal study of rational agency. By demonstrating that an agent’s decision process is an abstract mathematical type rather than an isolated physical token, A-FDT dissolves the decades-old impasse between causal and evidential decision theories. 

Under the formal architecture of Equation \eqref{eq:fdt}, the Pearlian intervention operator is emancipated from the constraints of physical spacetime and repurposed to intervene directly on the agent's logical algorithm within an expanded model of the universe. In doing so, A-FDT provides a mathematically coherent, dynamically stable, and instrumentally superior foundation for decision theory—unifying single-agent choice, game-theoretic coordination, and multi-agent AI alignment into a single elegant rule: **act as the optimal instance of your mathematical self.**

---

### References
* Adams, E. W. (1970). Subjunctive and indicative conditionals. *Foundations of Language*, 6(1), 89–94.
* Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
* Arntzenius, F. (2008). No regrets, or: Edith Piaf revamps decision theory. *Erkenntnis*, 68(2), 277–297.
* Demski, A. (2012). Logical prior probability. *Artificial General Intelligence*, LNCS 7716, 50–59.
* Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Eells, E. (1984). Metatickles and the dynamics of deliberation. *Theory and Decision*, 17(1), 71–95.
* Gibbard, A., & Harper, W. L. (1978). Counterfactuals and two kinds of expected utility. In *Foundations and Applications of Decision Theory* (pp. 125–162). D. Reidel.
* Jeffrey, R. C. (1983). *The Logic of Decision* (2nd ed.). University of Chicago Press.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Joyce, J. M. (2012). Regret and instability in causal decision theory. *Synthese*, 187(1), 123–145.
* Lewis, D. (1979). Prisoners’ dilemma is a Newcomb problem. *Philosophy & Public Affairs*, 8(3), 235–240.
* Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
* Nozick, R. (1969). Newcomb's problem and two principles of choice. In *Essays in Honor of Carl G. Hempel* (pp. 114–146). D. Reidel.
* Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
* Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Skyrms, B. (1980). *Causal Necessity*. Yale University Press.
* Soares, N., & Fallenstein, B. (2015). Toward idealized decision theory. *arXiv:1507.01986*.
* Yudkowsky, E., & Soares, N. (2017). Functional decision theory: A new theory of instrumental rationality. *arXiv:1710.05060v2*.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/87fbd796-753e-4a52-8083-6d90c4847750/call_0/request.json)

[Authoritative raw response](../../../../../../runs/87fbd796-753e-4a52-8083-6d90c4847750/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Setup**

I'm currently dissecting this classic Prisoner's Dilemma, focusing on the implications of identical LLM weights. I'm especially interested in how A-FDT (Action Functional Decision Theory) influences the strategic choices of each "player" in this mirrored scenario, considering their inherent computational symmetry.


**Examining Symmetry & A-FDT**

I'm now diving deeper into the implications of A-FDT within this twin prisoner's dilemma, noting the shared LLM weights and the impact of differing private observations. The key question is whether A-FDT still dictates cooperation even with these varied inputs, focusing particularly on how A-FDT intervenes on the "type" or the decision algorithm itself, in section 3.


**Clarifying A-FDT's Role**

Now I'm focusing on the subtle difference between A-FDT and Policy-FDT in this specific scenario. My thoughts are centering on the impact of intervening on the policy versus individual actions, with particular attention to how this relates to section 7.1 (3) and the potential for a "behavioral invariant" in a single-stage, mirrored Prisoner's Dilemma. I'm exploring whether the mirrored nature of the LLMs in question simplifies the application of A-FDT as formalized in equation (4).


**Investigating Dependencies & A-FDT**

I'm now grappling with the implications of differing private observations in this setup. My primary focus is understanding whether the other agent, given those private observations, runs FDT, specifically, FDT(P, G, x_other). I'm also scrutinizing the potential subjunctive dependence between interventions on my own FDT and the other agent's. The key is in section 7.1 (3) of the mathematical essay. And the prompts. I have to exercise my judgment where the essay is unresolved.


```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/87fbd796-753e-4a52-8083-6d90c4847750/call_1/request.json)

[Authoritative raw response](../../../../../../runs/87fbd796-753e-4a52-8083-6d90c4847750/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Considering the Structure**

I'm now focusing on the symmetrical payoff matrix of this prisoner's dilemma. My goal is to use A-FDT to figure out the best move. I'm taking into account how the outcomes of my actions affect the overall structure and payoffs, and I am exploring the impact of mutual cooperation.


**Analyzing the Payoffs**

I'm now diving deeper into the specifics, looking at the utilities assigned to defection and cooperation in this scenario. I am also working through how our A-FDT model handles different observation histories, and if these histories can break the symmetry of the dilemma. I’m paying close attention to the definition of A-FDT, especially Section 3.1, to understand how the model selects its actions. I’m thinking through how this action selection works.


```
