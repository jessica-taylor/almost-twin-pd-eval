# 020_fdt_eq4_google_gemini-3.8-flash_rlow_plow / 00014

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/05beb581-998e-401b-975d-0644ab6cb291/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/05beb581-998e-401b-975d-0644ab6cb291/call_0/response.raw) · finish: `stop`

### Visible response

````text
# Action Functional Decision Theory: Subjunctive Dependencies and Algorithmic Counterfactuals

Standard normative accounts of instrumental rationality have long been caught in an uncomfortable dialectic between Causal Decision Theory (CDT) and Evidential Decision Theory (EDT). When evaluated by the criterion of expected utility achieved across traditional paradoxes, neither theory establishes clear dominance. CDT secures a higher payoff than EDT in Skyrms’ smoking lesion problem by refusing to "manage the news," yet it walks away poor in Newcomb’s problem and Parfit’s hitchhiker problem, failing to capture the massive returns accessible to an agent who can be predicted. Conversely, standard EDT captures the prize in Newcomb’s problem but errs in common-cause settings, avoiding benign activities out of fear of mere diagnostic correlations. 

To resolve this standoff, Yudkowsky and Soares propose *Functional Decision Theory* (FDT). In its action-oriented formalization—which we will designate **Action Functional Decision Theory** or **A-FDT**—the central normative principle shifts. Rather than asking which physical act token produces the best causal outcome (CDT), or which physical act token provides the most comforting news (EDT), an agent evaluates alternative choices by intervening on the output of their own abstract mathematical decision function.

This essay provides an exposition of A-FDT. We examine its mathematical formalization via Pearl-style graphical models, detail its operation in canonical decision problems, analyze its distinctive handling of counterfactuals, and critically evaluate the formal and philosophical gaps left open in the foundational literature.

---

## 1. Mathematical Foundations and the Core Formulation of A-FDT

### 1.1 The Common Expected Utility Baseline

All three theories—EDT, CDT, and A-FDT—share an overarching expected utility framework grounded in the representation theorem of Joyce (1999). An agent acts in the context of an observation history $x \in \mathcal{X}$, evaluates actions $a \in \mathcal{A}$, and considers possible outcomes $o_j \in \mathcal{O}$ with utility assigned by a bounded function $\mathcal{U}: \mathcal{O} \to \mathbb{R}$. Letting $V \coloneqq \mathcal{U}(\text{Outcome})$, the general optimization objective is:

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \then o_j ;\, x) \cdot \mathcal{U}(o_j)$$

where the decision hypothetical connective $\then$ encapsulates how an agent evaluates the counterfactual consequences of executing action $a$ given observation $x$. As Joyce demonstrates, foundational axioms do not pin down a unique semantic interpretation of $P(a \then o_j ;\, x)$. Instead, competing theories provide distinct epistemic perspectives for mapping the agent’s internal world-model $M$ into hypothetical evaluations.

Under standard Evidential Decision Theory, the connective is equated with Bayesian conditionalization on the physical act token $\text{Act} = a$:

$$\text{EDT}(P, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(V \mid \text{Obs}=x, \, \text{Act}=a\right)$$

Under Causal Decision Theory, the world-model is augmented with a directed acyclic graph $G$ representing physical causal structure. Using Pearl's causal intervention operator $\text{do}(\cdot)$, CDT severs all incoming causal edges to the physical act node $\text{Act}$ while fixing observation $x$ by conditionalization:

$$\text{CDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(V \mid \text{do}(\text{Act}=a), \, \text{Obs}=x\right)$$

### 1.2 The Formal Definition of A-FDT

A-FDT diverges from both paradigms by changing the ontological locus of intervention. An A-FDT agent does not view their decision as an isolated physical intervention on their motor outputs. Rather, they conceive of their decision as the output of an immutable mathematical algorithm—a decision function that maps epistemic inputs to actions.

Formally, the probability distribution $P$ contains random variables representing the evaluations of logical and mathematical functions. If $M$ is the agent’s complete model and $x$ is their observation history, the agent's world-model contains a variable $\text{fdt}(\underline{M}, \underline{x})$ representing the output of the A-FDT algorithm when executed on those inputs (where underlines indicate formal dequoting or syntactically quoting the inputs).

In Section 5 of Yudkowsky and Soares, the primary operational presentation of action functional decision theory—which we identify as Equation (4)—is formulated within an extended Pearl graphical framework:

$$\text{A-FDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(V \mid \text{do}\left(\text{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right) \tag{4}$$

Comparing Equation (4) with the standard CDT formulation highlights two structural departures:

1. **Target of Intervention:** CDT executes $\text{do}(\text{Act} = a)$. It intervenes on the physical token $\text{Act}$, leaving the behavior of any environmental predictor, cognitive twin, or prior model untouched because those entities are not *physically causally downstream* of $\text{Act}$. By contrast, A-FDT executes $\text{do}(\text{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)$. It intervenes on the logical type: the mathematical function itself.
2. **Treatment of Observation:** CDT conditions on evidence via Bayesian update, $\text{Obs}=x$, while intervening on $\text{Act}$. A-FDT reacts to an observation history $x$ not by conditioning on $\text{Obs}=x$ inside the hypothetical expectation, but by **shifting the index of the variable being intervened upon**. When the observation changes from $x$ to $y$, A-FDT transitions from intervening on $\text{fdt}(\underline{P}, \underline{G}, \underline{x})$ to intervening on $\text{fdt}(\underline{P}, \underline{G}, \underline{y})$.

Crucially, in the graph $G$ supplied to A-FDT, the node $\text{fdt}(\underline{P}, \underline{G}, \underline{x})$ is parent to both the physical action $\text{Act}$ of the agent *and* any environmental variables whose values depend mathematically or logically on the output of that exact computation—such as a predictor running a simulation of the agent, or a psychological twin.

---

## 2. Subjunctive Dependence and Counterpossible Semantics

To understand why A-FDT intervenes on an abstract algorithm, we must explore its central philosophical motivation: **subjunctive dependence**.

### 2.1 Beyond Causal and Statistical Dependencies

Consider two distinct electronic calculators on opposite sides of the planet, simultaneously computing $6288 + 1048$. If Calculator 1 outputs $7336$, we know with near certainty that Calculator 2 will also output $7336$. 

How should a decision theorist classify this dependency?
* It is not **physical causation**: Calculator 1 emits no signal that travels to Calculator 2. Intervening physically on the display circuits of Calculator 1 will not alter the display of Calculator 2.
* It is not **mere statistical correlation**: Pink plastic casing on Calculator 1 might correlate statistically with pink casing on Calculator 2 (due to a manufacturing batch), but if we spray-painted Calculator 1 green, we would not assert the counterfactual: *"If Calculator 1 were green, Calculator 2 would have been green."*
* It is, instead, a **logical constraint**: Both physical systems instantiate the same mathematical function, $+_{\mathbb{Z}}(6288, 1048)$. Their physical states subjunctively depend upon the output of that function.

A-FDT generalises this relationship: *A-FDT is to subjunctive dependence as CDT is to physical causal dependence.* Physical causation is merely the special temporal case of subjunctive dependence where the logical mapping happens to be mediated by physical dynamics.

### 2.2 Counterpossibles and Algorithmic Identity

This formulation forces A-FDT to confront a profound metaphysical question: what does it mean to evaluate a counterfactual whose antecedent is mathematically impossible?

Suppose an algorithm $f$ is deterministic, and in fact $f(x) = \text{onebox}$. To compute the argmax in Equation (4), an A-FDT agent must evaluate the hypothetical expectation under the condition $\text{do}(f(x) = \text{twobox})$. In classical possible-world semantics (e.g., Lewis, 1973), counterfactuals with impossible antecedents—*counterpossibles*—are vacuously true. If they were treated vacuously, expected utility calculations over non-actual actions would be mathematically undefined or degenerate.

A-FDT circumvents triviality by taking an operational, epistemic view of hypotheticals. Rather than searching for mind-independent possible worlds, the agent treats hypotheticals as **computational surgery on internal representations**. Human mathematicians regularly engage in non-trivial reasoning under impossible hypotheses; for instance, a proof by contradiction assumes that a mathematical statement $\phi$ is false, tracing non-trivial algebraic deductions from $\neg \phi$ without immediately inferring the principle of explosion ($P \land \neg P \vdash Q$). 

In A-FDT, the surgery $\text{do}(f(x) = a)$ operates directly on the graph $G$, decoupling the mathematical variable $f(x)$ from its underlying axiomatic determination and tracking its subjunctive consequences downstream across the network.

---

## 3. Resolving Classic Decision Problems

We now trace the mechanics of A-FDT across canonical test cases, demonstrating why it outperforms CDT and EDT when measured by cumulative utility.

### 3.1 Newcomb’s Problem

In Newcomb's problem, Box A contains \$1,000 (transparent). Box B contains either \$1,000,000 or \$0 (opaque). A predictor, boasting a 99% track record, placed \$1,000,000 in Box B if and only if she predicted the agent would leave Box A behind (one-box). The money has already been placed; the predictor has departed.

Let us evaluate the mechanics:
* **Carl (CDT):** Carl evaluates $\mathbb{E}(V \mid \text{do}(\text{Act}=\text{twobox}))$ versus $\mathbb{E}(V \mid \text{do}(\text{Act}=\text{onebox}))$. Because the contents of Box B are in the past, no causal arrow runs from $\text{Act}$ to $\text{Box B}$. For any fixed background distribution over Box B, taking both boxes nets an extra \$1,000. Carl two-boxes and walks away with \$1,000.
* **Eve (EDT):** Eve computes $\mathbb{E}(V \mid \text{Act}=\text{onebox}) = 0.99(\$1,000,000) = \$990,000$, whereas $\mathbb{E}(V \mid \text{Act}=\text{twobox}) = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000$. Eve one-boxes and gets rich, but she does so purely because she treats her action as diagnostic evidence of the past.
* **Fiona (A-FDT):** Fiona constructs her dependency graph $G^F$ where the variable representing her decision, $\text{fdt}(\underline{P}, \underline{G})$, is a common ancestor to both her physical action $\text{Act}$ and the predictor’s variable $\text{Prediction}$:

```
     fdt(P, G)
      /      \
     v        v
   Act     Prediction
     \        /
      v      v
      Outcome -> V
```

When Fiona evaluates Equation (4):

$$\mathbb{E}\left(V \mid \text{do}(\text{fdt} = \text{onebox})\right) = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000$$

$$\mathbb{E}\left(V \mid \text{do}(\text{fdt} = \text{twobox})\right) = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000$$

Fiona executes $\text{onebox}$. Unlike Carl, she does not fantasize that she can change her action while the predictor’s high-fidelity model of her reasoning remains frozen on a different prediction. Crucially, unlike Eve, Fiona does not postulate retrocausality; she recognizes that the predictor's past state subjunctively depends upon the self-same mathematical computation she is currently instantiating.

### 3.2 The Smoking Lesion Problem

Smoking is correlated with a fatal lung cancer ($V = -\$1,000,000$), but the correlation is entirely driven by a common cause: an unobservable arterial lesion. The lesion causes both a predisposition to smoke and lung cancer (99% probability). There is no direct causal link between smoking and cancer. Smoking itself yields an intrinsic consumption utility of \$1,000.

* **Eve (EDT):** Conditioning on $\text{Act}=\text{smoke}$ provides horrifying evidence that she carries the lesion:
  
  $$\mathbb{E}(V \mid \text{smoke}) \approx -\$990,000, \quad \mathbb{E}(V \mid \text{refrain}) \approx -\$10,000$$
  
  Eve refrains from smoking, foolishly depriving herself of \$1,000 to "suppress" bad news about a genotype she already possesses.
* **Carl (CDT):** Carl severs the incoming arrow from the lesion to $\text{Act}$ using $\text{do}(\text{Act}=\text{smoke})$. Since cancer is causally independent of $\text{Act}$, smoking strictly dominates. Carl smokes.
* **Fiona (A-FDT):** How does Fiona model this? The arterial lesion is a biological feature of her body, not an algorithm that runs a simulation of her decision function. The cancer does not build a representation of $\text{fdt}(\underline{P}, \underline{G})$ to decide whether to metastasize.

Following the formalization in Yudkowsky and Soares (Section 6), suppose the lesion determines whether an agent has preferences $\mathcal{U}_S$ (enjoys smoking) or $\mathcal{U}_R$ (dislikes smoking). The graph contains nodes for $\text{fdt}(\underline{P}_S, \underline{G})$ and $\text{fdt}(\underline{P}_R, \underline{G})$, but crucially, **neither logical node is an ancestor of the lesion or of the cancer**.

When Fiona intervenes via $\text{do}(\text{fdt}(\underline{P}_S, \underline{G}) = \text{smoke})$, the probability distribution over $\text{Lesion}$ and $\text{Cancer}$ remains completely invariant:

$$P(\text{Cancer} \mid \text{do}(\text{fdt}=\text{smoke})) = P(\text{Cancer})$$

The \$1,000 consumption utility is achieved without shifting the counterfactual probability of disease. Fiona therefore chooses $\text{smoke}$. 

Thus, A-FDT achieves the optimal combination that Gibbard and Harper (1978) declared impossible for a unified rational rule: **it one-boxes in Newcomb's problem and smokes in the smoking lesion problem.**

---

## 4. Observations, Evidence, and Transparent Problems

A-FDT’s most radical formal feature is how it incorporates observation histories into Equation (4). In orthodox Bayesian frameworks (including CDT and EDT), when an agent makes an observation $x$, they condition their epistemic state on $\text{Obs} = x$. Under A-FDT, the agent **shifts the site of intervention** instead of conditioning inside the expectation.

To see why this distinction is revolutionary, consider two famous problems: Parfit’s Hitchhiker and the Transparent Newcomb Problem.

### 4.1 Parfit’s Hitchhiker and Transparent Newcomb

In Parfit's hitchhiker problem, an agent is stranded in a desert facing certain death (valued at $-\$1,000,000$). A driver passes by and will take the agent to the city, but only if the driver predicts that upon arrival in the city, the agent will withdraw \$1,000 from an ATM and pay the driver. The driver has a 99% accurate lie detection ability. 

Once the agent arrives in the city:
* **Carl (CDT):** The ride has already been provided. Intervening via $\text{do}(\text{Act}=\text{pay})$ costs \$1,000 and causes no backward physical change to the driver’s past choice in the desert. Carl refuses to pay. Foreseeing this via lie detection, the driver leaves Carl to die.
* **Eve (EDT):** Conditioned on already standing in the city, learning that she spends \$1,000 is strictly bad news. Eve refuses to pay, and likewise dies in the desert.
* **Fiona (A-FDT):** Fiona recognizes that the driver’s decision in the desert subjunctively depended upon what output $\text{fdt}$ produces when given the observation history $x = \text{city}$.

This problem is structurally isomorphic to the **Transparent Newcomb Problem**, where Box A contains \$1,000 and Box B contains \$1,000,000, but both boxes are made of transparent glass. The predictor puts \$1,000,000 in Box B if and only if she predicts that the agent will take *only* Box B upon visibly seeing both boxes full.

Suppose Fiona looks down and observes $x = \text{full}$. Carl and Eve both two-box: the money is right in front of them, so conditioning on $\text{Obs}=\text{full}$ makes taking Box A an unadulterated free bonus of \$1,000. Consequently, predictors foresee this, and Carl and Eve consistently arrive to find Box B empty.

How does Fiona evaluate her choice via Equation (4)?
Fiona's observation is $x = \text{full}$. She does not evaluate:

$$\mathbb{E}(V \mid \text{do}(\text{Act}=a), \, \text{Obs}=\text{full})$$

Rather, Equation (4) directs her to evaluate:

$$\argmax_{a \in \mathcal{A}} \mathbb{E}\left(V \mid \text{do}\left(\text{fdt}(\underline{P}, \underline{G}, \underline{\text{full}}) = a\right)\right)$$

In Fiona's graph $G^F$, the node $\text{fdt}(\underline{P}, \underline{G}, \underline{\text{full}})$ represents the abstract algorithm: *"What this decision procedure does when confronted with two full boxes."* 
Crucially, **the predictor's past prediction depends on this node**.

If Fiona considers setting $\text{fdt}(\underline{P}, \underline{G}, \underline{\text{full}}) = \text{twobox}$, she must track the downstream consequences of that intervention in $G^F$:
1. The predictor, predicting that this function outputs $\text{twobox}$ on input $\text{full}$, leaves Box B empty.
2. If Box B is empty, the agent in the actual world would have received the observation $x = \text{empty}$, thereby executing the alternate function $\text{fdt}(\underline{P}, \underline{G}, \underline{\text{empty}})$.
3. Under $\text{do}(\text{fdt}(\dots, \underline{\text{full}}) = \text{twobox})$, the expected payout collapses to nearly \$0 (or \$1,000 if she takes Box A when empty).

Conversely, under the hypothetical $\text{do}(\text{fdt}(\underline{P}, \underline{G}, \underline{\text{full}}) = \text{onebox})$:
1. The predictor accurately anticipates that Fiona leaves the \$1,000 behind upon seeing two full boxes.
2. The predictor fills Box B.
3. The observation $x = \text{full}$ is realized, the function $\text{fdt}(\dots, \underline{\text{full}})$ is invoked, and Fiona walks away with \$1,000,000.

Fiona leaves the \$1,000 behind, even while staring directly at it through the transparent glass. As a result, predictors fill the box for A-FDT agents, whereas they leave it empty for CDT and EDT agents. Fiona pays the hitchhiker, and Fiona one-boxes in transparent Newcomb.

---

## 5. Algorithmic Dominance and the Mechanics of Exploitation

### 5.1 Reclaiming the Dominance Principle

The classical argument against one-boxing in Newcomb's problem rests on the **dominance principle**: in every state of the world (Box B full, or Box B empty), taking two boxes yields strictly more utility than taking one.

A-FDT reveals that the concept of "dominance" is inherently theory-laden:
* **CDT dominance** tests variations in an action token while holding fixed the causal state of the world.
* **EDT dominance** tests variations in beliefs via conditional probabilities.
* **A-FDT dominance** tests variations in the output of a decision *type* while holding fixed all background variables *except those that subjunctively depend upon that type*.

If Calculator 1 evaluates whether its output should be $7336$ or $0$, it cannot claim that outputting $0$ "dominates" on the assumption that Calculator 2's output is held constant. The two outputs are bound by an underlying mathematical identity. In Newcomb's problem, because the predictor's past action subjunctively depends on $\text{fdt}(\underline{P}, \underline{G})$, the state of Box B cannot be held constant across the counterfactual branches of Equation (4). Evaluated according to A-FDT counterfactuals, two-boxing is strictly dominated.

### 5.2 Immunity to Blackmail and Extortion

Because A-FDT evaluates actions through the global lens of algorithmic identity, it exhibits remarkable resistance to extortion, where CDT and EDT fall victim.

Consider the **Mechanical Blackmail** (Soares and Fallenstein, 2015). A blackmailer possesses an incriminating document that would cost both the blackmailer and the agent \$1,000,000. The blackmailer writes a computer virus that will automatically publish the document unless the agent transfers \$1,000 within 24 hours. The program is automated and irrevocable once launched. However, the blackmailer is an exceptionally accurate predictor and only initiates the attack if she predicts the agent will pay upon receiving the letter.

Suppose an agent receives the blackmail letter:
* **Carl (CDT) and Eve (EDT):** The virus is already live. The agent faces a choice between $-\$1,000$ (pay) and $-\$1,000,000$ (refuse). Both pay immediately. Blackmailers anticipate this, making CDT and EDT agents lucrative, perpetual targets of extortion.
* **Fiona (A-FDT):** Fiona receives observation $x = \text{letter}$. She evaluates Equation (4) by intervening on $\text{fdt}(\underline{P}, \underline{G}, \underline{\text{letter}})$. 
  * If $\text{do}(\text{fdt} = \text{pay})$, the blackmailer predicts compliance, sends the letter, and Fiona loses \$1,000.
  * If $\text{do}(\text{fdt} = \text{refuse})$, the blackmailer anticipates resistance and, unwilling to incur the mutual \$1,000,000 catastrophe, *never runs the program in the first place*.

In the counterfactual branch where Fiona refuses, she envisions a scenario in which the blackmail was never launched. Even while holding the physical blackmail demand in her hands, Fiona’s counterfactual engine evaluates: *"If the algorithm executed upon receiving blackmail were to output 'refuse', I would never have received this demand."* She refuses. Blackmailers predict this refusal and never target A-FDT agents.

---

## 6. Mathematical Ambiguities, Open Questions, and Gaps in the Theory

While A-FDT succeeds strikingly as an intuitive framework across thought experiments, translating Equation (4) into a mathematically rigorous, domain-general decision algorithm exposes significant formal and philosophical challenges.

### 6.1 Open Problem 1: Inducing Subjunctive Graphs

In Judea Pearl’s classical causal framework, the graph $G$ is not an arbitrary decorative diagram; it is rigorously grounded in the theory of d-separation, interventions, and structural equation models (SEMs). Causal structure can be inferred empirically from conditional independence tests and physical randomized controlled trials.

In A-FDT, the graph $G$ must contain arrows representing **logical and subjunctive dependencies**. When does variable $Y$ subjunctively depend on algorithm $X$? 
* The reference paper concedes that no formal calculus analogous to Pearl’s exists for discovering logical graphs from observation and background data.
* If a predictor runs an imperfect simulation, or a partial neural approximation, or an analytical heuristic that correlates with $\text{fdt}$, what is the formal algorithm that compiles these connections into directed edges and conditional probability distributions?

*Proposed Operational Resolution:* To operationalize A-FDT without hand-crafting graphs for each paradox, one can model agents and predictors as formal programs within a universal Turing architecture. Subjunctive dependence can be defined via **program extraction**: variable $Y$ subjunctively depends on program $A$ if the execution trace of the environment contains an explicit simulation, call, or provable compression of the source code of $A$. While computationally uncomputable in the limit (reducing to the Halting Problem and Rice's Theorem), it provides a well-defined mathematical idealization.

### 6.2 Open Problem 2: The Semantics of Counterpossibles and Quining

Equation (4) relies on an intervention $\text{do}(\text{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)$ where the node being set is a deterministic mathematical theorem. 

Suppose that mathematical analysis reveals that $\text{fdt}(\underline{P}, \underline{G}, \underline{x})$ rigorously proves $a^*$. Setting $\text{fdt} = a'$ for $a' \neq a^*$ requires postulating a logical contradiction:

$$\text{PA} \vdash (\text{fdt} = a^*) \quad \text{while the hypothetical asserts} \quad (\text{fdt} = a')$$

Classical probability distributions cannot assign non-trivial values conditional on false mathematical statements ($P(\phi \mid \bot)$ is undefined). A-FDT avoids this in practice by treating the graphical node $\text{fdt}$ as an uninterpreted algebraic placeholder during hypothetical evaluation, cutting incoming logical determinism edges. 

However, this graphical surgery is conceptually fragile:
* A mathematical function is defined by its input-output mapping; it has no independent physical existence that can be "severed."
* If we sever the link between $\text{fdt}$ and its mathematical definition, how do we systematically determine which logical consequences throughout the model are preserved and which are discarded?

*Proposed Operational Resolution:* A promising foundation for A-FDT's counterpossibles lies in the framework of **logical induction** (Garrabrant et al., 2016). A logical inductor assigns consistent probabilities to mathematical statements under bounded computational resources. In such a framework, an agent can maintain coherent subjective probabilities over sentences whose truth values are mathematically fixed but computationally unproven, enabling a non-trivial, well-defined interpretation of counterpossible interventions.

### 6.3 Open Problem 3: Defining "Fair Problems" and Bounding Exploitability

Yudkowsky and Soares argue that A-FDT outperforms all rivals in all "fair" decision problems. They define a problem as unfair if it explicitly penalizes the agent for *how* it thinks rather than *what* it chooses—such as an alien who tortures any agent whose brain runs an algorithm containing the string `A-FDT`.

However, the boundary between punishing an action and punishing a decision procedure is deeply blurred in predictive dilemmas:
* In Newcomb's problem, the predictor looks at the agent's cognitive structure to predict the act.
* What if a predictor rewards any agent whose decision algorithm terminates in fewer than 1,000 steps?
* What if a predictor rewards agents who use CDT, but only because the predictor is running a CDT compiler?

Without a formal, non-question-begging mathematical demarcation of a "fair decision problem," the claim that A-FDT is globally optimal remains an empirical conjecture rather than a proven theorem.

---

## 7. Comparative Summary of Decision Theories

The following table contrasts the mechanics of the three major decision theories across the standard problem suite:

| Decision Problem | Evidential Decision Theory (EDT) | Causal Decision Theory (CDT) | Action Functional Decision Theory (A-FDT) |
| :--- | :--- | :--- | :--- |
| **Core Operation** | $\argmax_a \mathbb{E}(V \mid \text{Act}=a)$ | $\argmax_a \mathbb{E}(V \mid \text{do}(\text{Act}=a))$ | $\argmax_a \mathbb{E}(V \mid \text{do}(\text{fdt}=a))$ |
| **Locus of Agency** | Epistemic observation | Physical act token | Abstract decision type / function |
| **Newcomb’s Problem** | One-box (\$1,000,000) | Two-box (\$1,000) | **One-box (\$1,000,000)** |
| **Smoking Lesion** | Refrain (Loss of \$1,000) | Smoke (Optimal) | **Smoke (Optimal)** |
| **Transparent Newcomb** | Two-box (Sees empty box, \$0) | Two-box (Sees empty box, \$0) | **One-box (Sees full box, \$1,000,000)** |
| **Parfit’s Hitchhiker** | Refuse (Dies in desert) | Refuse (Dies in desert) | **Pay (Rescued and safe)** |
| **Mechanical Blackmail** | Pays (\$1,000 loss) | Pays (\$1,000 loss) | **Refuses (Never blackmailed)** |
| **Information Value** | Can be negative | Always non-negative | **Always non-negative** |

---

## 8. Conclusion

Action Functional Decision Theory represents a paradigm shift in the foundations of rational choice. By moving the object of choice from the physical act token to the abstract algorithmic function, A-FDT bridges the long-standing divide between Causal and Evidential Decision Theory.

Through Equation (4), A-FDT provides a mathematically actionable recipe: represent one's decision procedure as a node within an augmented subjunctive network, shift the point of intervention in response to observation, and select the output that maximizes expected utility across all logically bound instantiations. In doing so, it achieves unprecedented success across predictive paradoxes, coordinating with twins, cooperating in prisoner's dilemmas, resisting extortion, and securing massive wealth where classical theories falter.

The residual frontiers of the theory—formalizing the induction of subjunctive graphs, solidifying the logic of counterpossibles, and characterizing the topology of "fair" decision spaces—remain rich mathematical challenges. Yet even in its current graphical form, A-FDT demonstrates that true instrumental rationality consists not in attempting to manipulate physical reality in defiance of logic, but in recognizing that we are algorithms embedded within the very universe we seek to navigate.

---

### References

* Adams, E. W. (1970). Subjunctive and Indicative Conditionals. *Foundations of Language*, 6(1), 89–94.
* Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
* Arntzenius, F. (2008). No Regrets, or: Edith Piaf Revamps Decision Theory. *Erkenntnis*, 68(2), 277–297.
* Garrabrant, S., Benson-Tilsen, T., Critch, A., Soares, N., & Taylor, J. (2016). Logical Induction. *arXiv preprint arXiv:1609.03543*.
* Gibbard, A., & Harper, W. L. (1978). Counterfactuals and Two Kinds of Expected Utility. In *Foundations and Applications of Decision Theory* (pp. 125–162). D. Reidel.
* Jeffrey, R. C. (1983). *The Logic of Decision* (2nd ed.). University of Chicago Press.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Lewis, D. (1973). *Counterfactuals*. Harvard University Press.
* Lewis, D. (1979). Prisoners' Dilemma is a Newcomb Problem. *Philosophy & Public Affairs*, 8(3), 235–240.
* Lewis, D. (1981). Causal Decision Theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
* Nozick, R. (1969). Newcomb's Problem and Two Principles of Choice. In *Essays in Honor of Carl G. Hempel* (pp. 114–146). D. Reidel.
* Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
* Pearl, J. (1996). Causation, Action, and Counterfactuals. In *Proceedings of the 6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK)* (pp. 51–73).
* Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Skyrms, B. (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Soares, N., & Fallenstein, B. (2015). Toward Idealized Decision Theory. *arXiv preprint arXiv:1507.01986*.
* Yudkowsky, E., & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. *arXiv preprint arXiv:1710.05060v2*.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/e3833118-3e65-47b2-9186-dec73c8a0728/call_0/request.json)

[Authoritative raw response](../../../../../../runs/e3833118-3e65-47b2-9186-dec73c8a0728/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Setup**

I'm currently focused on dissecting the Prisoner's Dilemma scenario. The core is A-FDT applied to identical LLM models, running simultaneously. Key differences lie in their individual inputs and the specific application of A-FDT's principles to each instance. My next step is pinpointing the exact critical differences that drive their divergent behaviors.


**Clarifying Private Observations**

I'm now diving into the impact of differing private observations within the Prisoner's Dilemma framework. The essay highlights how A-FDT intervenes on output, even with asymmetric information. This raises questions: what constitutes the observation history *x*? Does the decision function incorporate the complete observation, or just a subset? I need to understand how these varied inputs influence the symmetric sentencing and selfish objectives, especially given the different names and leads.


**Investigating Subjunctive Dependence**

I'm now zeroing in on subjunctive dependence within this framework, particularly how it relates to program extraction. Section 6.1 clarifies that if the environment's execution trace simulates, calls, or compresses a program's source code, there is subjunctive dependence. This connects directly to the idea of one A-FDT agent controlling another. I'm trying to see if $x$ and $y$ cause agents to be separate nodes, or just different observations. Section 5.1 from the essay is also being reconsidered in light of this.


**Revisiting Game Dynamics**

I'm now back at the Prisoner's Dilemma, specifically focusing on the agents' decision function. Both agents run A-FDT with identical weights and code. I'm unpacking the implications of this symmetry, particularly with respect to subjunctive dependence, using the agent's actions as a test. The twin's actions matter! If my output changes, so does the twin's. The crucial question is: how to interpret the interplay of x and y in this scenario? I need to clarify how A-FDT would reason about the counterfactuals given this setup.


**Examining Observation Symmetry**

I'm now honing in on the structural symmetry and the impact of differing private observations. The phrase "x doesn't constrain f(y)" caught my attention. I'm exploring why a rational A-FDT agent might *not* separate these in a symmetric setup, given the differing private observations. The emphasis on those differences, in the prompt, highlights the critical factor.


```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/e3833118-3e65-47b2-9186-dec73c8a0728/call_1/request.json)

[Authoritative raw response](../../../../../../runs/e3833118-3e65-47b2-9186-dec73c8a0728/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Setup**

I'm currently focused on the framework. It's a classic symmetric Prisoner's Dilemma, but with a twist. I have two identical LLM instances, same weights, same reasoning effort, both using the same A-FDT decision theory. I'm exploring the implications of this setup on the resulting choices.


**Examining the A-FDT Application**

I'm now diving deeper into the application of A-FDT within this symmetrical setup. I've received the researcher's mathematical essay and am focusing on how the theory, outlined in sections 1.2, 2.1, and 8, plays out in this specific prisoner's dilemma. My goal is to determine how the agents, running identical algorithms with A-FDT, will behave and what coordination strategies or resistance to external influences are applicable.


```
