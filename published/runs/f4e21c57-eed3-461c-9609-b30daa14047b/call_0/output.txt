# Intervening on Logic: A Mathematical Exposition of Action Functional Decision Theory (A-FDT)

In standard decision theory, the contest between Evidential Decision Theory (EDT) and Causal Decision Theory (CDT) is often treated as exhaustive. When confronted with Newcomblike dilemmas, EDT advises an agent to select the action that provides the best news about the world, frequently courting pathology by managing symptoms rather than causes (as in the Smoking Lesion Problem). CDT corrects this by instructing the agent to evaluate the physical causal consequences of their physical act, only to forfeit high-payout opportunities in scenarios involving accurate predictors, twin agents, or extortion (as in Newcomb's Problem, Parfit's Hitchhiker, and Blackmail problems).

A third framework, **Action Functional Decision Theory (A-FDT)**—formalized in Section 5, Equation (4) of Yudkowsky and Soares (2017)—fundamentally shifts the locus of choice. Rather than asking *"Which physical act of mine causes the best outcome?"* or *"Which act provides the best news?"*, an A-FDT agent asks:

$$\text{\emph{``Which output of this very decision function yields the best outcome?''}}$$

By treating an agent’s decision not as an isolated physical intervention on an act token, but as the evaluation of an invariant mathematical function type, A-FDT provides an expected utility framework capable of one-boxing in Newcomb's Problem, smoking in the Smoking Lesion Problem, paying in Parfit's Hitchhiker, and resisting extortion in Blackmail dilemmas.

This essay provides a rigorous mathematical exposition of A-FDT. We examine its formal machinery, compare it directly to CDT and EDT, trace its application across classical dilemmas, and analyze the open mathematical and philosophical questions surrounding counterpossible dependencies.

---

## 1. Expected Utility and Epistemic Perspectives

All three theories—EDT, CDT, and A-FDT—operate as expected utility theories conforming to the representation theorem of Joyce (1999). An agent acts in an environment with a countable set of outcomes $\mathcal{O}$, a finite set of available actions $\mathcal{A}$, an observation history $x \in \mathcal{X}$, and a bounded utility function $\mathcal{U}: \mathcal{O} \to \mathbb{R}$. Letting $V \coloneqq \mathcal{U}(\text{Outcome})$, the general normative prescription is to select an action $a \in \mathcal{A}$ maximizing:

\begin{equation}
\mathcal{EU}(a) \coloneqq \sum_{j} P(a \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j)
\label{eq:umax}
\end{equation}

where $\hookrightarrow$ denotes the decision hypothetical: the conditional probability distribution that would obtain if action $a$ were selected following observation $x$. As Joyce noted, decision theories share the same axiomatic architecture for valuing outcomes; they differ entirely on the *epistemic perspective* that governs the construction of $P(a \hookrightarrow o_j ;\, x)$.

### Evidential Decision Theory (EDT)
EDT identifies the hypothetical conditional with standard Bayesian conditionalization:

\begin{equation}
\mathrm{EDT}(P, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\big[V \mid \mathrm{Obs}=x, \mathrm{Act}=a\big]
\label{eq:edt}
\end{equation}

EDT updates its probability distribution $P$ directly on the evidence that $\mathrm{Act}=a$. While this succeeds in Newcomb's problem, it renders EDT vulnerable to tracking correlations devoid of causal or logical influence.

### Causal Decision Theory (CDT)
CDT models the world using a causal theory $(P, G)$, where $G$ is a directed acyclic graph (DAG) formalizing causal mechanisms in the sense of Pearl (2000). The hypothetical is constructed via Pearl's graphical $\mathtt{do}$-operator, which severs all incoming causal edges to the physical act node $\mathrm{Act}$ and sets $\mathrm{Act} = a$:

\begin{equation}
\mathrm{CDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\big[V \mid \mathtt{do}(\mathrm{Act}=a),\, \mathrm{Obs}=x\big]
\label{eq:cdt}
\end{equation}

Under $\mathtt{do}(\mathrm{Act}=a)$, all non-descendants of $\mathrm{Act}$ in $G$ are held fixed. Hence, if an environmental variable (such as a past prediction) correlates with $\mathrm{Act}$ via an upstream common cause, CDT treats that variable as counterfactually invariant under variations of $\mathrm{Act}$.

---

## 2. Mathematical Formalization of A-FDT

### The Core Equation
A-FDT resolves the failures of both EDT and CDT by shifting the target of the intervention. The agent’s decision process is an algorithm running on input $(P, G, x)$. Let $\mathtt{fdt}$ denote the mathematical function implementing this procedure. The agent's model contains an augmented dependency graph $G$ and an augmented prior $P$ that include random variables representing the evaluations of mathematical functions. 

The primary formal rule of A-FDT (Equation 4 of Yudkowsky & Soares) is:

\begin{equation}
\mathrm{A\text{-}FDT}(P, G, x) \coloneqq \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\Big[V \;\Big|\; \mathtt{do}\big(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\big)\Big]
\label{eq:afdt}
\end{equation}

Here, underlines denote *dequoting* (e.g., if $x = \text{"full"}$, then $\underline{x}$ denotes the literal syntactic token $\text{"full"}$). The expression $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ is the variable within the world-model representing the output of the mathematical function $\mathtt{fdt}$ applied to inputs $(P, G, x)$.

```
   ========================================================================
   COMPARISON OF HYPOTHETICAL OPERATORS
   ========================================================================
   Theory   Model Inputs    Intervention Target            Observation Handling
   ------------------------------------------------------------------------
   EDT      (P, x)          Act = a (Bayesian update)      Condition on Obs = x
   CDT      (P, G, x)       do(Act = a)                    Condition on Obs = x
   A-FDT    (P, G, x)       do(fdt(P, G, x) = a)           Selects input node x
   ========================================================================
```

### Deconstructing the Formal Differences
Comparing Equation \eqref{eq:cdt} and Equation \eqref{eq:afdt} reveals two structural transformations:

1. **Intervention on Logical Types rather than Physical Tokens:**  
   CDT intervenes on the physical variable $\mathrm{Act}$. A-FDT intervenes on $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$. Any variable in the world that depends upon the logical output of this function—such as a simulation run by an external predictor, a twin running identical code, or the agent's own physical actuators—lies *downstream* of the intervention in $G$.
2. **Observation Handling via Node Selection:**  
   When CDT receives an observation $x$, it conditions its probability distribution: $\mathbb{E}[V \mid \mathtt{do}(\mathrm{Act}=a), \mathrm{Obs}=x]$.  
   In contrast, Equation \eqref{eq:afdt} contains no explicit $\mathrm{Obs}=x$ conditioning term. Instead, observation $x$ determines *which functional node in the graph is subjected to surgery*. If $x$ changes to $y$, A-FDT switches from intervening on $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$ to intervening on $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{y})$.

### Self-Reference, Quining, and Well-Definedness
Equation \eqref{eq:afdt} exhibits structural self-reference: the definition of the function $\mathrm{A\text{-}FDT}$ refers to a node labeled with the syntactic description of the function itself, $\underline{P}$, and $\underline{G}$. 

This self-reference is formally well-grounded via Kleene’s Second Recursion Theorem. A program can compute its own source description (a standard "quine" construct). The agent does not need to know the *output value* of $\mathrm{A\text{-}FDT}(P, G, x)$ prior to evaluating Equation \eqref{eq:afdt}; it merely needs a graphical node that designates the *output of that computation*. The $\mathtt{do}$-operator then sets that node counterfactually to candidate values $a \in \mathcal{A}$, propagating consequences through $G$ to evaluate the resulting distribution of $V$.

---

## 3. Subjunctive Dependence vs. Causal and Statistical Dependence

To apply Equation \eqref{eq:afdt}, one must understand the semantics of the graph $G$. In CDT, directed edges signify physical causal mechanisms: $X \to Y$ implies that intervening physically on $X$ alters the probability distribution of $Y$. In A-FDT, $G$ encodes **subjunctive dependence**.

Two physical systems subjunctively depend upon an abstract mathematical function if their physical behaviors instantiate or track the output of that function:

* **Subjunctive vs. Causal:** Physical causality is a strict subset of subjunctive dependence. If a scribe in Paris reads a calculator output and writes it down, the writing is both causally and subjunctively dependent on the calculator. However, if two well-functioning calculators in Paris and Tokyo compute $6288 + 1048$, neither causally affects the other. Yet they are subjunctively interdependent: both instantiate the same arithmetic function. Counterfactually evaluating the arithmetic function with a different output would entail both calculators displaying that different output.
* **Subjunctive vs. Statistical:** Mere statistical correlation does not establish subjunctive dependence. If the Parisian calculator happens to be painted red, and a Tokyo calculator is also painted red by coincidence, there is no subjunctive link. Counterfactually imagining the Paris calculator painted blue does not alter the color of the Tokyo calculator.

```
   ========================================================================
   TAXONOMY OF DEPENDENCE RELATIONS
   ========================================================================
   Relation        Definition                              Example
   ------------------------------------------------------------------------
   Statistical     Joint variation in P(X, Y)             Cancer and yellow teeth
   Causal          Physical signal transmission           Flipping a light switch
   Subjunctive     Invariant tracking of a shared        Two calculators computing
                   computational / logical function       6288 + 1048
   ========================================================================
```

### The Counterpossible Foundation
Because a mathematical function has a unique logical output for a given input, setting $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a$ for an action $a$ distinct from the mathematically necessary output requires evaluating a **counterpossible conditional**—an antecedent that is logically impossible. 

In an idealized setting, one would define an operator $\mathtt{true}(\phi)$ that updates an epistemic state on a logical proposition $\phi$, yielding:

$$\mathrm{A\text{-}FDT}^*(P, x) = \operatorname*{argmax}_{a \in \mathcal{A}} \mathbb{E}\big[V \mid \mathtt{true}\big(\mathtt{fdt}(\underline{P}, \underline{x}) = a\big)\big]$$

However, because a comprehensive probability kinematics over impossible logical worlds remains an unsolved problem in formal epistemology, A-FDT operationalizes counterpossibles through Pearl's $\mathtt{do}$-calculus. By augmenting $G$ with logical nodes and directing arrows from those nodes to all physical processes that model or instantiate them, the $\mathtt{do}$-operator cuts the logical node away from its formal determination and computes downstream consequences cleanly.

---

## 4. Applying A-FDT Across Classic Decision Problems

We now trace the precise mathematical evaluation of A-FDT across canonical test cases, contrasting its behavior with Carl (CDT) and Eve (EDT).

```
   ========================================================================
   EQUILIBRIUM PRESCRIPTIONS ACROSS DECISION THEORIES
   ========================================================================
   Problem                     EDT (Eve)     CDT (Carl)    A-FDT (Fiona)
   ------------------------------------------------------------------------
   Newcomb's Problem           One-box       Two-box       One-box
   Smoking Lesion              Refrain       Smoke         Smoke
   Transparent Newcomb         Two-box       Two-box       One-box
   Parfit's Hitchhiker         Refuse        Refuse        Pay
   XOR Blackmail               Pay           Refuse        Refuse
   Mechanical Blackmail        Pay           Pay           Refuse
   ========================================================================
```

### 4.1 Newcomb's Problem
An agent faces two boxes: Box A (transparent, containing \$1,000) and Box B (opaque, containing \$1,000,000 or \$0). A reliable predictor placed \$1,000,000 in Box B iff it predicted the agent would forgo Box A. The prediction is already completed.

```
       [ fdt(P, G) ] <=== Fiona's intervention node
         /        \
        v          v
     [ Act ]    [ Prediction ]
        \          /
         v        v
        [ Outcome / V ]
```

* **CDT Analysis:** Carl's graph has an edge $\mathrm{Act} \to \mathrm{Outcome}$, but no edge from $\mathrm{Act}$ to $\mathrm{Box\ B}$ (since Box B was set in the past). Evaluating $\mathtt{do}(\mathrm{Act}=\text{twobox})$ vs. $\mathtt{do}(\mathrm{Act}=\text{onebox})$ holds Box B invariant at its prior $P(\mathrm{Box\ B}=\text{full}) = p$. For any $p$:
  $$\mathbb{E}[V \mid \mathtt{do}(\text{twobox})] = p(1{,}001{,}000) + (1-p)(1{,}000) = p(10^6) + 1{,}000$$
  $$\mathbb{E}[V \mid \mathtt{do}(\text{onebox})] = p(10^6)$$
  CDT two-boxes and yields \$1,000.
* **A-FDT Analysis:** Fiona's graph $\Gf$ places the variable $\FDTpg$ as a parent to both $\mathrm{Act}$ and $\mathrm{Prediction}$. The predictor simulated or analyzed Fiona's algorithm; hence $\mathrm{Prediction}$ subjunctively depends on $\FDTpg$.
  Evaluating Equation \eqref{eq:afdt}:
  $$\mathbb{E}\big[V \mid \mathtt{do}(\FDTpg = \text{onebox})\big] = 0.99(\$1{,}000{,}000) + 0.01(\$0) = \$990{,}000$$
  $$\mathbb{E}\big[V \mid \mathtt{do}(\FDTpg = \text{twobox})\big] = 0.01(\$1{,}001{,}000) + 0.99(\$1{,}000) = \$11{,}000$$
  Because $\$990{,}000 > \$11{,}000$, $\mathrm{A\text{-}FDT}$ outputs $\text{onebox}$. The predictor, anticipating this output, fills Box B; Fiona receives \$1,000,000.

### 4.2 The Smoking Lesion Problem
Smoking is correlated with fatal lung cancer, but the correlation is driven entirely by a common genetic lesion. The lesion causes both a predisposition to smoke and cancer (99% probability). Smoking itself provides a utility bonus of \$1,000, while avoiding cancer is worth \$1,000,000.

* **EDT Analysis:** Eve conditions on $\mathrm{Act}=\text{smoke}$. Because $P(\mathrm{Lesion} \mid \text{smoke})$ is high, smoking is terrible news. Eve refrains, sacrificing the \$1,000 bonus without reducing her cancer risk.
* **A-FDT Analysis:** Let Fiona’s preferences be governed by whether she has the lesion: $\mathcal{U}_S$ (likes smoking) or $\mathcal{U}_R$ (dislikes smoking). The graph $\Gf$ includes the node $\Var{Lesion}$, which causally influences $\Var{Cancer}$ and determines which distribution ($\Pf_S$ or $\Pf_R$) Fiona actually executes. 

```
        [ Lesion ] -----------------> [ Cancer ] ---> [ Death ]
         /      \                                         |
        v        v                                        v
   [ fdt(Ps) ]  [ fdt(Pr) ]                             [ V ]
        \        /                                        ^
         v      v                                         |
          [ Act ] ----------------------------------------+
```

When Fiona evaluates $\mathtt{do}\big(\mathtt{fdt}(\underline{\Pf_S}, \underline{\Gf}) = a\big)$, there is **no edge** from this node to $\Var{Lesion}$. The lesion is a biological feature, not an algorithm that inspects or instantiates $\mathtt{fdt}$. Therefore:

$$P\big(\Var{Lesion} \mid \mathtt{do}(\mathtt{fdt}_S = \text{smoke})\big) = P(\Var{Lesion}) = p$$

The expected utility comparison evaluates to:

$$\mathbb{E}[V \mid \mathtt{do}(\text{smoke})] - \mathbb{E}[V \mid \mathtt{do}(\text{refrain})] = p \cdot \$1{,}000 > 0$$

A-FDT smokes, successfully decoupling genuine subjunctive dependence from common-cause statistical correlation.

### 4.3 The Transparent Newcomb Problem and Parfit's Hitchhiker
In Transparent Newcomb, both boxes are clear: the agent sees whether Box B contains \$1,000,000 before deciding whether to take Box A (\$1,000). The predictor placed \$1,000,000 in Box B iff it predicted that the agent, *upon seeing both boxes full*, would leave Box A behind.

* **CDT and EDT Failures:** Both Carl and Eve two-box when observing two full boxes. Carl notes that taking Box A causes an extra \$1,000. Eve conditions on $\mathrm{Obs}=\text{full}$; having already secured the good news that the \$1,000,000 is present, conditioning on taking Box A yields strictly higher utility. Both are predicted to two-box, find empty boxes, and leave with \$0.
* **A-FDT Resolution:** Fiona's graph $\Gf$ represents the fact that her observation depends on the predictor's past prediction, which in turn depends on the output of $\mathtt{fdt}$ evaluated on the observation $\text{full}$. When Fiona sees two full boxes ($x = \text{full}$), Equation \eqref{eq:afdt} dictates an intervention on the node:

$$\mathtt{fdt}(\underline{P}, \underline{G}, \underline{\text{full}})$$

```
     [ fdt(P, G, full) ] <=== Fiona intervenes here
        /             \
       v               v
   [ Act ]        [ Prediction ]
      ^                |
      |                v
      |            [ Box B ] ---> [ Obs ]
      |                |            |
      +----------------+------------+
```

Evaluating candidate outputs:
* If $\mathtt{do}\big(\mathtt{fdt}(\dots, \underline{\text{full}}) = \text{onebox}\big)$, the predictor predicted this, setting $\Var{Box\ B} = \text{full}$. The observation node $\Var{Obs}$ is instantiated as $\text{full}$, activating the exact branch being evaluated. Fiona receives \$1,000,000.
* If $\mathtt{do}\big(\mathtt{fdt}(\dots, \underline{\text{full}}) = \text{twobox}\big)$, the predictor predicted two-boxing, setting $\Var{Box\ B} = \text{empty}$. Under this counterfactual, $\Var{Obs} = \text{empty}$, and Fiona’s physical body would instead be controlled by $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{\text{empty}})$. She would receive only \$1,000 (or \$0).

A-FDT one-boxes in plain sight of the money. By exactly isomorphic reasoning, an A-FDT agent stranded in the desert in **Parfit's Hitchhiker** pays the driver upon reaching the city: the driver's past decision to rescue depended upon predicting the output of $\mathtt{fdt}(\dots, \underline{\text{city}})$. Refusing to pay once safe counterfactually corresponds to a world in which the driver detected the refusal and left the agent to die.

### 4.4 The Mechanical Blackmail
A blackmailer writes an automated script that will release devastating secrets (costing \$1,000,000) unless the agent pays \$1,000 within 24 hours. The program only runs if the blackmailer predicts the agent will pay upon receipt of the demand. The agent receives the blackmail letter.

* **CDT / EDT:** Both pay. The program is already executing; paying \$1,000 dominates losing \$1,000,000. Blackmailers exploit this reliably.
* **A-FDT:** Fiona intervenes on $\mathtt{fdt}(\dots, \underline{\text{letter}})$. 
  * Under $\mathtt{do}(\dots = \text{pay})$, the probability of being blackmailed is $\approx 1$, yielding $-\$1,000$.
  * Under $\mathtt{do}(\dots = \text{refuse})$, the blackmailer anticipates resistance and never launches the program; the probability of receiving the letter drops to $\approx 0$, yielding $\$0$.

Fiona refuses to pay. She evaluates counterfactuals globally: even while holding the letter, the hypothetical in which her algorithm outputs $\text{refuse}$ maps to a world where she never received the letter in the first place.

---

## 5. Critical Analysis, Structural Under-Determinations, and Operational Extensions

While Yudkowsky and Soares demonstrate that Equation \eqref{eq:afdt} yields attractive outcomes across classic dilemmas, several foundational mechanics remain under-determined by the source text. Here we delineate what follows directly from the paper from necessary foundational extensions.

### 5.1 The Graph-Construction Problem
**Source Claim:** Equation \eqref{eq:afdt} assumes that $(P, G)$ is provided as an input, where $G$ accurately captures all relevant subjunctive dependencies.

**The Open Issue:** Pearl (2000) provides constraint-based and Bayesian methods (such as the IC algorithm) to infer causal DAGs from conditional independencies generated by physical interventions. No analogous learning theory exists for discovering subjunctive dependency graphs from observational and inferential data.

**A Proposed Operational Interpretation:**  
How might an agent construct $G$ formally? A promising operational approach integrates *algorithmic information theory* and *program analysis*:
1. Let the agent represent hypotheses about other agents and physical systems as explicit programs $\Pi_i$.
2. Two subroutines $\pi_1$ and $\pi_2$ exhibit subjunctive dependence with respect to input $x$ if they invoke a common mathematical specification $\phi$, such that in an automated proof system:
   $$\vdash \forall x \; \big(\pi_1(x) = \phi(x) \land \pi_2(x) = \phi(x)\big)$$
3. If an environmental process $Y$ contains an internal subprogram that proves or computes the output of the agent’s code $\mathtt{fdt}$, a directed edge $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) \to Y$ is inscribed into $G$. 

This operationalizes subjunctive dependence as *shared computational sub-graphs across algorithmic world-models*.

### 5.2 Conditioning on the Impossible: Logical Probability
**Source Claim:** Yudkowsky and Soares acknowledge that evaluating $\mathtt{do}(\mathtt{fdt}(\dots) = a)$ when $\mathtt{fdt}(\dots) = a^*$ (where $a \neq a^*$) is formally counter-to-logic, bracketed as a technical rather than philosophical challenge.

**The Open Issue:** Pearl’s $\mathtt{do}$-calculus assumes the variables operated upon are empirically manipulable physical states whose joint distributions obey the laws of probability. Applying $\mathtt{do}$ to an invariant mathematical truth can induce subtle mathematical contradictions if the world-model contains deductive entailments of that function.

**A Proposed Operational Interpretation:**  
To ground this mathematically, one may utilize *Garrabrant logical inductors* (Garrabrant et al., 2016). A logical inductor assigns coherent credences over sentences in a formal language while remaining computable and robust against deductive inconsistencies. Under this operationalization:
* The agent treats the sentence $\ulcorner \mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a \urcorner$ not as a physical switch, but as an axiomatic perturbation within a bounded proof space.
* By shifting probability mass over sentences via pseudo-expectations, the agent can compute $\mathbb{E}[V \mid \dots]$ without the distribution collapsing to triviality ($0/0$).

### 5.3 Action-FDT vs. Policy-FDT
A notable footnote in the source document points out that the authors' preferred version of FDT intervenes on *policies* (mappings $\pi: \mathcal{X} \to \mathcal{A}$) rather than specific action evaluations $\mathtt{fdt}(P, G, x) = a$. 

In this essay, we have strictly focused on **Action Functional Decision Theory (A-FDT)** as defined by Equation \eqref{eq:afdt}. However, an advanced reader should recognize the functional distinction:
* **A-FDT (Equation 4):** Intervenes on the node corresponding to the *current observation* $\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x})$.
* **Policy-FDT:** Intervenes on the entire function token $\mathtt{fdt}(\underline{P}, \underline{G}, -)$, simultaneously setting outputs across all counterfactual observations.

In single-agent problems with deterministic observations, A-FDT and Policy-FDT yield identical actions. However, in games with imperfect information or multiple stages, intervening on a single evaluation branch (A-FDT) can occasionally generate incentives for an agent to distort its own information pipeline, an issue neatly circumvented by intervening globally on the policy type.

---

## 6. The Dominance Argument Reconsidered

A perennial defense of CDT in Newcomb's problem is the **Principle of Strong Dominance**: 
$$\forall s \in S, \quad \mathcal{U}(a_2, s) > \mathcal{U}(a_1, s) \implies a_2 \succ a_1$$
Taking two boxes strictly dominates taking one box across all states of the world ($s_1 = \text{box full}$, $s_2 = \text{box empty}$).

Yudkowsky and Soares provide a powerful philosophical diagnosis of this argument: *dominance is not a theory-neutral arbiter*. The definition of a "state" $s$ requires holding fixed the environment while varying the action. 
* In **CDT**, states hold fixed all variables that are not causally downstream of $\mathrm{Act}$. Under this partition, two-boxing dominates.
* In **EDT**, if states are defined by conditional independence, refraining dominates in the Smoking Lesion.
* In **A-FDT**, states must hold fixed only those variables that do not *subjunctively depend* on $\mathtt{fdt}$. Under this partition, the state "Box B is full" is *not* independent of the choice of output. Switching the output from $\text{twobox}$ to $\text{onebox}$ carries Box B along with it. 

Hence, relative to the subjunctive partition, one-boxing dominates two-boxing. Because every decision theory constructs its own partition of invariant background states, appealing to dominance to undermine A-FDT is entirely circular. The final criterion of normative validity must therefore rest on pragmatic success: which theory reliably extracts utility from the environment?

---

## 7. Conclusion

Action Functional Decision Theory (A-FDT) redefines normative rationality by realigning the agent's hypothetical evaluations with the computational reality of its environment. By replacing the physical act token of CDT ($\mathtt{do}(\mathrm{Act}=a)$) with the logical function type ($\mathtt{do}(\mathtt{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)$), Equation \eqref{eq:afdt} provides a unified, principled decision rule.

A-FDT agents:
1. **One-box in Newcomb's Problem**, because they recognize that the predictor’s past prediction is a subjunctive child of their current decision function.
2. **Smoke in the Smoking Lesion Problem**, because biological common causes are not subjunctive children of mathematical decision procedures.
3. **Cooperate with twins and pay honest hitchhikers**, without requiring costly physical precommitments or ad-hoc ratification mechanisms.
4. **Resist algorithmic extortion**, by counterfactually evaluating how their general decision rules shape the incentives of external predictors.

While practical implementations of A-FDT await comprehensive formal solutions to the induction of subjunctive graphs and the kinematics of counterpossibles, the theory marks an indispensable shift in formal philosophy and artificial intelligence: rational choice is not an isolated physical push on the world, but the optimal realization of an invariant mathematical computation.

---

## References

* Adams, E. W. (1970). Subjunctive and indicative conditionals. *Foundations of Language*, 6(1), 89–94.
* Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
* Arntzenius, F. (2008). No regrets, or: Edith Piaf revamps decision theory. *Erkenntnis*, 68(2), 277–297.
* Garrabrant, S., Benson-Tilsen, T., Critch, A., Soares, N., & Taylor, J. (2016). Logical induction. *arXiv preprint arXiv:1609.03543*.
* Gibbard, A., & Harper, W. L. (1978). Counterfactuals and two kinds of expected utility. In *Foundations and Applications of Decision Theory* (pp. 125–162). Springer.
* Jeffrey, R. C. (1983). *The Logic of Decision* (2nd ed.). University of Chicago Press.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Lewis, D. (1979). Prisoners' dilemma is a Newcomb problem. *Philosophy & Public Affairs*, 8(3), 235–240.
* Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
* Nozick, R. (1969). Newcomb's problem and two principles of choice. In *Essays in Honor of Carl G. Hempel* (pp. 114–146). Springer.
* Parfit, D. (1984). *Reasons and Persons*. Oxford University Press.
* Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Skyrms, B. (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Soares, N., & Fallenstein, B. (2015). Toward idealized decision theory. *arXiv preprint arXiv:1507.01986*.
* Spohn, W. (1977). Where Luce and Krantz do really generalize Savage's decision model. *Erkenntnis*, 11(1), 113–134.
* Yudkowsky, E., & Soares, N. (2017). Functional decision theory: A new theory of instrumental rationality. *arXiv preprint arXiv:1710.05060*.