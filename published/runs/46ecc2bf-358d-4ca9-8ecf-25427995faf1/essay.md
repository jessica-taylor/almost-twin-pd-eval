# Action Functional Decision Theory: Choosing the Best Output of a Fixed Decision Function

This essay explains **action functional decision theory (A-FDT)**: a decision theory that evaluates actions by asking what would happen if the agent’s *decision procedure itself* produced different outputs. The reference article calls the theory “functional decision theory”; here I use the assigned name **A-FDT** and take **Equation (4) of Section 5** as the primary formal statement. I also emphasize the action-level version of the theory, while noting where a policy-level formulation may be needed.

A-FDT sits alongside two better-known theories:

- **Evidential decision theory (EDT)** asks: *Which action would be the best news to learn I had taken?*
- **Causal decision theory (CDT)** asks: *Which physical action causes the best outcome?*
- **A-FDT** asks: *Which output of this very decision procedure causes the best outcome?*

The distinctive claim of A-FDT is that rational agents should treat their decisions as outputs of a fixed mathematical function and should choose the output whose counterfactual consequences are best. In the source’s words, the agent asks, “Which output of this decision procedure causes the best outcome?”

---

## 1. The core idea of A-FDT

A-FDT is motivated by cases in which an agent’s action is correlated with something else—not because the action causes that thing, but because both depend on the same computation or on a reliable prediction of that computation.

Consider a prisoner’s dilemma between an agent and a perfect psychological twin who reasons exactly as the agent does. The choices are causally independent, but they are not independent as outputs of reasoning. If the shared reasoning procedure concludes “cooperate,” both cooperate; if it concludes “defect,” both defect. A-FDT says the agent should not ask only, “What does my local physical action cause?” Instead, she should ask what would happen if the shared reasoning procedure output one conclusion rather than another.

This leads to the central informal principle:

> An A-FDT agent chooses the output of her decision function that yields the best expected outcome, when the counterfactual variation is made to the output of the decision function rather than merely to the physical action.

The source summarizes this by saying that functional decision theory is to *subjunctive dependence* as causal decision theory is to causal dependence. The important notion is that some correlations are not merely statistical: they arise because two systems compute the same function, or because one system contains an accurate model of the other’s decision procedure. A-FDT tries to preserve exactly those dependencies in its counterfactuals.

---

## 2. Formal statement of A-FDT

Let:

- \(\mathcal A\) be a finite set of actions.
- \(\mathcal O\) be a countable set of outcomes.
- \(\mathcal X\) be a set of observation histories.
- \(U\) be a utility function on outcomes.
- \(V = U(\text{Outcome})\) be the utility random variable.
- \(P\) be the agent’s world-model, including probabilities over physical and logical variables.
- \(G\) be a graph or structural model describing how changes to variables propagate.

The generic expected-utility template is

\[
\mathcal{EU}(a;x)
=
\sum_j P(a \hookrightarrow o_j ; x)\,U(o_j),
\]

where \(x\) is the agent’s observation and \(\hookrightarrow\) is a decision-theoretic hypothetical. EDT, CDT, and A-FDT differ in how they interpret that hypothetical.

EDT uses ordinary conditional probability:

\[
\mathrm{EDT}(P,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E_P[V \mid \text{Obs}=x,\text{Act}=a].
\]

CDT uses a causal intervention on the physical action:

\[
\mathrm{CDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E_P[V \mid do(\text{Act}=a),\text{Obs}=x].
\]

Here \(do(\cdot)\) is Pearl-style surgical intervention: set the variable, propagate along causal arrows, and leave unaffected variables fixed.

Equation (4) of the source, rewritten with the assigned name, gives A-FDT:

\[
\boxed{
\mathrm{A\text{-}FDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E_P\!\left[
V
\mid
do\bigl(
\mathrm{afdt}(\underline{P},\underline{G},\underline{x}) = a
\bigr)
\right].
}
\]

The variable

\[
D_x := \mathrm{afdt}(\underline{P},\underline{G},\underline{x})
\]

represents the output of the A-FDT decision procedure when run on inputs \(P\), \(G\), and observation \(x\). The underlines indicate dequoting: they turn the values \(P\), \(G\), and \(x\) into names or descriptions of those objects inside the model. The model therefore contains a variable representing the output of the very algorithm being used. The source notes that this self-reference is harmless in principle; it is analogous to the self-representation made possible by Kleene’s recursion theorem.

The crucial difference from CDT is this:

- CDT intervenes on a physical action variable: \(do(\text{Act}=a)\).
- A-FDT intervenes on a logical/computational variable: \(do(D_x=a)\).

The difference from EDT is that A-FDT does not merely condition on the action. It performs an intervention, but the intervention is on the decision function’s output.

---

## 3. Observations in A-FDT

A subtle point is that Equation (4) does **not** evaluate

\[
\mathbb E[V \mid do(D_x=a), \text{Obs}=x]
\]

as its primary form. Instead, the observation \(x\) appears inside the name of the decision-function variable \(D_x\). The source says that whereas CDT responds to observation by Bayesian conditioning, A-FDT responds to observation by changing which node it intervenes upon.

This has an important consequence. In problems where the agent’s observation is itself correlated with predictions of the agent’s decision procedure, A-FDT does not simply condition on the observation and then choose the locally best physical act. Instead, it asks what would happen if the decision procedure, given that observation, output one action rather than another. This allows the agent’s counterfactual reasoning to change the probability of the observation itself, when that observation depends on predictors of the agent.

This is especially important in transparent Newcomb problems and blackmail problems. If the agent sees a full box or receives a blackmail letter, EDT and CDT tend to hold that observation fixed and ask what is best given it. A-FDT instead asks: *What if the decision procedure I am running on this observation had a different output?* In doing so, it may evaluate worlds in which the agent would have received a different observation.

In my own operational gloss, if an observation is genuinely exogenous—say, unrelated weather data that no predictor could have influenced—then conditioning on it is harmless. But if the observation is downstream of a predictor’s behavior, A-FDT should generally avoid conditioning it away. This is not fully formalized in the source, but it seems required to recover the source’s examples.

---

## 4. Subjunctive dependence and the graph \(G\)

The graph \(G\) is the heart of A-FDT. It tells the agent how changing the decision-function output would affect the rest of the world-model.

CDT’s graph encodes causal structure. If \(do(\text{Act}=a)\) is applied, only variables causally downstream of \(\text{Act}\) change. Variables that are merely correlated with \(\text{Act}\), but not caused by it, are held fixed.

A-FDT’s graph must encode a broader class of dependencies: causal, computational, logical, and predictive dependencies. The source calls these **subjunctive dependencies**. Two systems are subjunctively dependent when their behavior depends on the same mathematical function, or when one system contains a sufficiently accurate representation of the other’s decision procedure.

The source’s calculator analogy is helpful. Two well-functioning calculators computing \(6288+1048\) on opposite sides of the world do not causally influence each other, but their outputs are not merely accidentally correlated. If one outputs \(7336\), the other will too, assuming both are functioning correctly. Similarly, an agent and a reliable predictor may not causally influence each other at the moment of decision, but the predictor’s prediction depends on the agent’s decision procedure.

Thus, in an A-FDT graph:

- If a predictor reliably models the agent’s decision procedure, the predictor’s prediction should depend on the relevant \(D_x\).
- If a twin or copy runs the same decision procedure, the twin’s action should depend on the same logical output, or on a corresponding output variable.
- If a lesion or common cause correlates smoking with cancer, but does not represent the agent’s decision procedure, cancer should **not** depend on \(D_x\).

This is how A-FDT separates predictor-like dependencies from lesion-like dependencies.

---

## 5. Applying A-FDT: a practical procedure

An idealized A-FDT agent facing a decision can proceed as follows.

1. **Specify the decision problem.**  
   Identify the action set \(\mathcal A\), possible observations \(\mathcal X\), outcomes \(\mathcal O\), and utility function \(U\).

2. **Build a world-model \(P\).**  
   This model should include not only ordinary physical variables but also variables representing logical or computational facts, especially the outputs of relevant decision procedures and predictors.

3. **Build a dependency graph \(G\).**  
   Draw edges representing how changes to the decision-function output would propagate. Include edges to the agent’s action, to predictors who model the agent, to copies or twins, and to outcomes. Do not include edges from the decision-function output to variables that are merely statistically correlated with the action.

4. **Identify the actual observation \(x\).**  
   The actual observation determines which decision-function node \(D_x\) is relevant.

5. **For each candidate action \(a\), perform the intervention**
   \[
   do(D_x=a).
   \]

6. **Compute the expected utility of each intervened model.**

7. **Choose the action with the highest post-intervention expected utility.**

In real applications, the agent will usually be bounded and will not literally possess a complete graph of all logical dependencies. But the normative ideal is clear: A-FDT chooses by comparing counterfactual worlds generated by intervening on the decision function, not merely on the physical act.

---

## 6. Example: Newcomb’s problem

In Newcomb’s problem, an agent faces two boxes:

- Box A visibly contains \$1,000.
- Box B contains \$1,000,000 if a reliable predictor predicted the agent would one-box.
- Box B contains \$0 if the predictor predicted the agent would two-box.

The predictor is 99% accurate.

Let \(D\) be the variable representing the output of the A-FDT procedure in this situation. The relevant A-FDT graph contains dependencies such as:

\[
D \rightarrow \text{Act},
\]
\[
D \rightarrow \text{Prediction},
\]
\[
\text{Prediction} \rightarrow \text{Box B},
\]
\[
\text{Act}, \text{Box B} \rightarrow V.
\]

Now compare the two interventions.

If A-FDT intervenes on \(D=\text{one-box}\), then the predictor likely predicted one-boxing, so Box B is likely full:

\[
\mathbb E[V \mid do(D=\text{one-box})]
=
0.99(\$1{,}000{,}000) + 0.01(\$0)
=
\$990{,}000.
\]

If A-FDT intervenes on \(D=\text{two-box}\), then the predictor likely predicted two-boxing, so Box B is likely empty:

\[
\mathbb E[V \mid do(D=\text{two-box})]
=
0.01(\$1{,}001{,}000) + 0.99(\$1{,}000)
=
\$11{,}000.
\]

Therefore,

\[
\mathrm{A\text{-}FDT}(P,G) = \text{one-box}.
\]

CDT two-boxes because it intervenes directly on the physical action and holds the predictor’s prediction fixed. EDT one-boxes because conditioning on one-boxing is good news. A-FDT one-boxes for a structurally different reason: changing the output of the decision function changes what the predictor would have predicted.

---

## 7. Example: the smoking lesion problem

In the smoking lesion problem, smoking is correlated with lung cancer, but only because a lesion causes both a preference for smoking and cancer. Smoking itself does not cause cancer. Smoking gives \$1,000 of utility. Avoiding cancer is worth \$1,000,000.

EDT refrains from smoking because smoking is bad news: it is evidence of the lesion. CDT smokes because smoking does not cause cancer. A-FDT agrees with CDT here.

The reason is that the lesion does not subjunctively depend on the agent’s decision procedure. The lesion is not a predictor, not a copy, and not a simulation of the agent’s reasoning. It is a common cause of both smoking behavior and cancer.

In an A-FDT graph, the decision-function variable \(D\) affects the action:

\[
D \rightarrow \text{Act}.
\]

But it does not affect the lesion or cancer:

\[
D \nrightarrow \text{Lesion},
\]
\[
D \nrightarrow \text{Cancer}.
\]

Thus,

\[
P(\text{Lesion} \mid do(D=\text{smoke}))
=
P(\text{Lesion} \mid do(D=\text{refrain})).
\]

The probability of cancer remains unchanged by the intervention on \(D\). Smoking adds direct utility, while not changing the agent’s cancer risk. Therefore A-FDT chooses to smoke.

The source gives a more elaborate version in which the agent is uncertain about her own preferences, because the lesion may determine whether she likes smoking. Even there, the key point remains: intervening on the relevant decision-function output changes the action but does not change the lesion or cancer. A-FDT smokes.

This example shows that A-FDT is not simply EDT in disguise. It does not treat all correlations as decision-relevant. It preserves predictor-like dependencies but ignores lesion-like correlations.

---

## 8. Example: transparent Newcomb and Parfit’s hitchhiker

The transparent Newcomb problem is especially important for A-FDT. The agent sees both boxes. Box B is filled only if the predictor predicted that the agent would one-box *after seeing both boxes full*. If the agent sees two full boxes, should she one-box?

CDT says two-box, because the box is already full. EDT also says two-box, because conditional on seeing Box B full, taking both boxes yields more money. A-FDT says one-box.

Let

\[
D_{\text{full}} = \mathrm{afdt}(P,G,\text{full})
\]

be the output of the A-FDT procedure when the agent sees a full Box B, and let

\[
D_{\text{empty}} = \mathrm{afdt}(P,G,\text{empty})
\]

be the output when the agent sees an empty Box B.

The actual observation is \(x=\text{full}\), so A-FDT intervenes on \(D_{\text{full}}\). But the graph still allows the predictor’s earlier behavior to depend on \(D_{\text{full}}\). If \(D_{\text{full}}=\text{one-box}\), then the predictor probably predicted that the agent would one-box upon seeing a full box, and therefore filled it. If \(D_{\text{full}}=\text{two-box}\), then the predictor probably predicted two-boxing and left Box B empty.

Let \(q\) be the probability that the agent two-boxes upon seeing an empty box. Following the source’s calculation:

\[
\mathbb E[V \mid do(D_{\text{full}}=\text{one-box})]
=
0.99(\$1{,}000{,}000)
+
0.01(q \cdot \$1{,}000).
\]

This is approximately \$990,000 plus at most \$10.

By contrast,

\[
\mathbb E[V \mid do(D_{\text{full}}=\text{two-box})]
=
0.01(\$1{,}001{,}000)
+
0.99(q \cdot \$1{,}000).
\]

This is at most about \$11,000. Therefore A-FDT one-boxes even while seeing a full box.

This is the same structure as Parfit’s hitchhiker problem. A driver will save the agent only if she predicts the agent will later pay \$1,000 after being saved. Once saved, CDT and EDT see no reason to pay. A-FDT pays, because the earlier prediction depends on the output of the decision procedure the agent will run after being saved. A-FDT acts as though it has the optimal predisposition, without needing an explicit precommitment device.

This is one of the most striking features of A-FDT: it may prescribe an action that seems locally dominated, because the local dominance argument severs a subjunctive dependency that A-FDT treats as essential.

---

## 9. A-FDT and dominance

A common objection to one-boxing is that two-boxing dominates one-boxing: whatever is in Box B, taking both boxes gives an extra \$1,000.

A-FDT rejects the dominance argument as formulated by CDT. The CDT dominance argument holds the predictor’s prediction fixed while varying the physical action. But in cases with reliable predictors, that means varying the physical action while holding the decision function’s output fixed. The source argues that this is like imagining a correctly functioning calculator producing a different answer to the same arithmetic problem while holding the arithmetic fixed.

A-FDT has its own notion of dominance: one action dominates another if, holding fixed the relevant subjunctive dependencies, changing the decision function’s output from one to the other is never worse and sometimes better. In Newcomb’s problem, relative to A-FDT’s counterfactuals, two-boxing does not dominate one-boxing, because changing the decision function’s output to two-boxing also changes the predictor’s likely prediction.

This does not prove that A-FDT is correct, but it shows that the standard dominance objection is not neutral. Every theory of counterfactuals induces its own notion of dominance.

---

## 10. Policies versus actions

Equation (4) evaluates actions. The source notes, however, that the authors’ preferred formalization often evaluates **policies**, meaning mappings from observations to actions. This matters in sequential or multi-agent problems where predictors may predict the agent’s entire disposition, not just a single action.

For A-FDT as assigned here, the basic object is an action \(a\). But many problems are naturally modeled by multiple decision-function nodes, one for each possible observation:

\[
D_x = \mathrm{afdt}(P,G,x).
\]

In such cases, an A-FDT agent may need to evaluate a whole policy \(\pi : \mathcal X \to \mathcal A\). A natural policy-level extension would be:

\[
\mathrm{A\text{-}FDT}_{\text{policy}}(P,G)
=
\arg\max_{\pi}
\mathbb E_P
\left[
V
\mid
do\left(
\forall x:\ D_x = \pi(x)
\right)
\right].
\]

This is not literally Equation (4), but it is continuous with it. It says: choose the mapping from observations to actions such that, if the decision procedure implemented that mapping, expected utility would be highest.

In my view, policy-level reasoning is the safer operational interpretation for unfamiliar cases, especially when the agent expects future decisions, repeated interactions, or predictors of her entire strategy. Equation (4) remains the core action-level statement, but a full working implementation of A-FDT will often need to evaluate policies.

---

## 11. Open problem: constructing \(G\)

The most important unresolved issue is the construction of \(G\). CDT can appeal, at least formally, to causal graphs and interventionist accounts of causation. A-FDT needs a graph that tells it how changing a logical variable changes other variables. The source explicitly acknowledges that we do not yet have a satisfactory general method for inferring such subjunctive-dependence structure from observation and experiment.

The source therefore treats \(G\) as an input:

> Equation (4) works given a graph that accurately describes how changing the value of a logical variable affects other variables, but it is not yet clear how to construct such a thing.

This is a genuine limitation. A-FDT gives a decision rule conditional on a correct dependency model, but it does not fully solve the problem of building that model.

Still, a reasonable operational interpretation is possible. I propose the following heuristics, which are not fully formal but are suggested by the source’s examples.

### Heuristic 1: Connect predictors to the decision function

If another agent or mechanism contains a reliable model, simulation, or prediction of the agent’s decision procedure, then its behavior should depend on the relevant A-FDT output variable.

For example, in Newcomb’s problem:

\[
D \rightarrow \text{Prediction}.
\]

In blackmail problems, whether the blackmailer sends the letter may depend on her prediction of the agent’s response, so the sending event may depend on \(D\).

### Heuristic 2: Do not connect common causes to the decision function

If a variable correlates with the action only because it shares a common cause with the action, and does not represent the decision procedure, then it should not depend on \(D\).

For example, in the smoking lesion problem:

\[
\text{Lesion} \rightarrow \text{Act},
\]
\[
\text{Lesion} \rightarrow \text{Cancer},
\]
but not
\[
D \rightarrow \text{Lesion}.
\]

### Heuristic 3: Treat copies and twins as sharing the relevant computation

If another agent runs the same decision procedure, then their action should be linked to the same logical output, or to a corresponding output variable. This is why A-FDT cooperates in symmetric prisoner’s dilemmas against twins or sufficiently similar agents.

### Heuristic 4: Let observations vary when they are downstream of predictors

If the agent’s observation is produced by a predictor’s earlier choice, then counterfactual changes to \(D_x\) may change the probability of receiving \(x\). In such cases, A-FDT should not hold the observation fixed in a way that destroys the predictor correlation.

These heuristics are my operational proposal for applying A-FDT when the source leaves graph construction underdeveloped. They are justified by the fact that they reproduce the source’s desired prescriptions in the standard examples and by the general principle that A-FDT should preserve all decision-relevant subjunctive dependencies.

---

## 12. Counterpossible reasoning

Another difficulty is that A-FDT sometimes requires reasoning about counterpossibilities. If the agent’s decision procedure in fact outputs \(a\), then it is logically impossible for that very procedure to output \(b\) on the same input. Yet A-FDT asks what would happen if it did.

The source recognizes this. It notes that A-FDT would ideally use a “true” operator that updates a probability distribution to represent the scenario where some logical sentence is true. But no fully satisfactory definition of such an operator is currently available. Instead, Equation (4) uses a graph \(G\) and reuses the \(do\)-operator.

Operationally, this means A-FDT treats logical counterfactuals structurally. The agent does not need a complete metaphysics of impossible worlds. She needs only a model that says which variables would change if the decision function had a different output. Human reasoners seem capable of doing something like this in practice, even if the formal foundations remain incomplete.

This is perhaps the largest theoretical cost of A-FDT. It gains utility in predictive dilemmas, but it relies on a less mature account of logical counterfactuals than CDT’s account of causal counterfactuals.

---

## 13. What A-FDT gets right

The appeal of A-FDT is that it gives a unified treatment of several classic problems.

- In **Newcomb’s problem**, A-FDT one-boxes, because the predictor depends on the agent’s decision function.
- In the **smoking lesion problem**, A-FDT smokes, because the lesion is not a predictor and does not depend on the decision function.
- In **transparent Newcomb**, A-FDT one-boxes even when the box is seen to be full, because the predictor’s earlier choice depends on what the agent’s decision function would output upon seeing a full box.
- In **Parfit’s hitchhiker**, A-FDT pays after being rescued, because the driver’s prediction depends on the post-rescue decision procedure.
- In symmetric **prisoner’s dilemmas** with twins or copies, A-FDT cooperates, because the other agent’s choice depends on the same reasoning process.
- In many blackmail problems, A-FDT refuses to pay, because paying would make blackmail more likely in the counterfactuals that matter.

The common theme is that A-FDT tries to keep the right correlations intact. EDT keeps too many correlations, including merely evidential ones. CDT keeps too few, severing correlations with predictors and twins. A-FDT tries to keep precisely the subjunctive dependencies that matter for decision-making.

---

## Conclusion

Action functional decision theory evaluates actions by intervening on a variable representing the output of the agent’s own decision procedure. Its core rule, Equation (4), says to choose the action \(a\) that maximizes expected utility under the intervention

\[
do\bigl(\mathrm{afdt}(P,G,x)=a\bigr).
\]

This simple change—intervening on the decision function rather than on the physical act—allows A-FDT to handle predictor problems, twin problems, transparent Newcomb problems, and blackmail problems in a unified way.

The theory is elegant, but it is not yet complete. The hardest part is constructing the graph \(G\), which must encode not only causal dependencies but also logical, computational, and predictive dependencies. The source treats this as an open problem, and rightly so. Still, the examples support a workable operational interpretation: model predictors and copies as depending on the relevant decision-function output, model mere common causes as independent of that output, and evaluate policies when the problem involves multiple observations or future choices.

A-FDT’s central lesson is that rational choice may require thinking globally. The question is not merely “What does my physical act cause?” nor “What is the best news?” but rather: “What would the world look like if this very decision procedure produced this output instead of that one?” A-FDT chooses the output that makes that imagined world best.

---

## References

Yudkowsky, E., and Soares, N. “Functional Decision Theory: A New Theory of Instrumental Rationality.” arXiv:1710.05060v2.

Pearl, J. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.

Joyce, J. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

Gibbard, A., and Harper, W. “Counterfactuals and Two Kinds of Expected Utility.” In *Foundations and Applications of Decision Theory*, 1978.

Lewis, D. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59, no. 1, 1981.