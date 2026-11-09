# Action Functional Decision Theory (A-FDT): Choosing the Best Output of a Fixed Decision Function

The supplied paper introduces a decision theory it calls functional decision theory. In this essay I use the assigned name **A-FDT** for the theory, and I take **Equation (4) in Section 5** of the paper as the primary formal statement of A-FDT for present purposes. The core idea is that a rational agent should not ask merely, “Which physical act causes the best outcome?” or “Which act would be best news?” Instead, the agent should treat her decision as the output of a fixed mathematical function and ask: “Which output of this very function would yield the best outcome?”

A-FDT is an expected-utility theory. It agrees with causal decision theory (CDT) that decision-relevant hypotheticals should be counterfactual rather than merely evidential, but it differs from CDT about which counterfactuals are relevant. Where CDT intervenes on the agent’s physical action, A-FDT intervenes on a variable representing the output of the agent’s decision procedure. This small formal change lets A-FDT preserve decision-relevant dependencies on predictors, twins, simulations, and other agents who are reasoning in the same way, while still avoiding the distinctive errors of evidential decision theory (EDT).

---

## 1. The common expected-utility framework

A-FDT, CDT, and EDT all prescribe maximizing expected utility. Given a countable set of possible outcomes \(o_1,o_2,\dots\), a finite action set \(\mathcal A\), an observation history \(x\), and a utility function \(\mathcal U\), the paper writes expected utility schematically as

\[
\mathcal{EU}(a) \coloneqq \sum_j P(a \then o_j ; x)\,\mathcal U(o_j),
\]

where \(P(a \then o_j;x)\) is the probability of outcome \(o_j\) in the hypothetical scenario where action \(a\) is taken after observation \(x\). The theories differ in how they interpret the decision hypothetical \(\then\).

EDT interprets the hypothetical as ordinary Bayesian conditionalization. If \(P\) is the agent’s probability distribution and \(V\) is the utility variable, EDT chooses

\[
\mathrm{EDT}(P,x)
\coloneqq
\argmax_{a\in\mathcal A}
\mathbb E\!\left[V \mid \Obs=x, \Act=a\right].
\]

CDT instead uses a causal intervention. Using Pearl-style notation, CDT chooses

\[
\mathrm{CDT}(P,G,x)
\coloneqq
\argmax_{a\in\mathcal A}
\mathbb E\!\left[V \mid \Do(\Act=a), \Obs=x\right],
\]

where \(G\) is a causal graph and \(\Do(\Act=a)\) means: set the agent’s physical action to \(a\), then propagate consequences along causal arrows.

A-FDT keeps the interventionist structure of CDT but changes the variable on which the agent intervenes.

---

## 2. Equation (4): the formal statement of A-FDT

The paper’s Equation (4) can be written, using the assigned name, as

\[
\boxed{
\mathrm{A\text{-}FDT}(P,G,x)
\coloneqq
\argmax_{a\in\mathcal A}
\mathbb E\!\left[
V \mid
\Do\!\left(
\mathrm{A\text{-}FDT}_{\underline P,\underline G,\underline x}=a
\right)
\right].
}
\]

Here:

- \(P\) is the agent’s world-model, understood as a probability distribution over variables.
- \(G\) is a graph describing how changing certain variables changes others. For CDT, \(G\) is a causal graph. For A-FDT, \(G\) must encode not only causal structure but also relevant logical, mathematical, computational, and other “subjunctive” dependencies.
- \(x\) is the agent’s observation history or current input.
- \(\mathrm{A\text{-}FDT}_{\underline P,\underline G,\underline x}\) is a variable inside \(P\) representing the output of the A-FDT decision procedure when run on inputs \((P,G,x)\). The underlines indicate that \(P,G,x\) are being encoded as data inside the variable’s name.
- \(\Do(\cdot)\) is an intervention operator. It sets the indicated variable to a value and propagates the change through the dependencies encoded by \(G\).

The self-reference is deliberate: the model \(P\) contains a variable representing the output of the very decision procedure that is using \(P\). The paper notes that this is not a fatal problem; self-referential data structures can be constructed using standard recursion-theoretic techniques such as quining.

The essential contrast is this:

\[
\text{CDT intervenes on } \Act,
\qquad
\text{A-FDT intervenes on } \mathrm{A\text{-}FDT}_{\underline P,\underline G,\underline x}.
\]

CDT asks what would happen if the agent’s body performed action \(a\). A-FDT asks what would happen if the decision function that the agent is actually running, given her actual model and input, had output \(a\).

---

## 3. Subjunctive dependence and A-FDT counterfactuals

The paper motivates A-FDT with the notion of **subjunctive dependence**. Two physical systems can be relevantly linked not because one causes the other, but because both implement, predict, or accurately represent the same computation. The paper’s examples include:

- two agents using the same decision procedure;
- an agent and a predictor who has an accurate model of that agent;
- two calculators computing the same arithmetic expression;
- a predictor’s prediction and the action predicted.

The paper says that when two systems are computing the same function, their behaviors “subjunctively depend” upon that function. A-FDT is meant to stand to subjunctive dependence as CDT stands to causal dependence.

In an A-FDT hypothetical, the agent changes the output of her decision function and then changes all and only those things that depend on that output in the relevant subjunctive sense. This is different from EDT and CDT.

- EDT preserves too many correlations. If smoking is evidence of a lesion that causes cancer, EDT treats smoking as bad news and may refrain even when smoking cannot affect cancer.
- CDT preserves too few correlations. If a predictor has already predicted the agent’s action, CDT treats the predictor’s prediction as fixed when intervening on the physical action, thereby imagining scenarios in which a reliable predictor somehow fails exactly at the relevant moment.

The paper summarizes this diagnosis by saying that EDT respects too many action-environment correlations, while CDT respects too few. A-FDT attempts to preserve precisely the decision-relevant subjunctive dependencies.

Operationally, an A-FDT agent evaluates an action \(a\) by constructing a hypothetical distribution

\[
P^{a}_{\mathrm{A\text{-}FDT}}
=
P\bigl(\,\cdot \mid \Do(\mathrm{A\text{-}FDT}_{\underline P,\underline G,\underline x}=a)\bigr),
\]

then computing

\[
\mathbb E_{P^{a}_{\mathrm{A\text{-}FDT}}}[V].
\]

Variables that are descendants of the A-FDT output node in \(G\) are updated. Variables that are not descendants are held fixed. Thus, if a predictor’s prediction is modeled as depending on the output of the agent’s decision function, the predictor’s prediction changes when the A-FDT output is changed. If a lesion is modeled as a common cause of action and cancer but not as depending on the decision function, the lesion and cancer probabilities remain fixed.

---

## 4. How to apply A-FDT

A practical A-FDT analysis can be organized as follows.

### Step 1: Identify the decision problem

Specify:

- the action set \(\mathcal A\);
- the observation or input \(x\);
- the outcome variable \(\Outcome\);
- the utility variable \(V=\mathcal U(\Outcome)\).

### Step 2: Build a world-model \(P\)

The model should include variables for the relevant physical, informational, and computational facts. Crucially, it should include variables for logical or computational outputs, including the output of the agent’s own decision procedure:

\[
F_x \coloneqq \mathrm{A\text{-}FDT}_{\underline P,\underline G,\underline x}.
\]

It may also include variables for what the decision procedure would output under other observations:

\[
F_y \coloneqq \mathrm{A\text{-}FDT}_{\underline P,\underline G,\underline y}.
\]

This is important in problems where the observation itself depends on predictions of the agent’s behavior.

### Step 3: Build the dependency graph \(G\)

The graph \(G\) should encode how variables would change if the A-FDT output variable were changed. Draw an arrow from \(F_x\) to \(Z\) when \(Z\) is a prediction, simulation, copy, logical consequence, or downstream effect of the decision function’s output. Do not draw such an arrow when \(Z\) is merely statistically correlated with the action through a common cause that does not represent or compute the decision function.

For example:

- In Newcomb’s problem, the predictor’s prediction depends on the agent’s decision function, so \(F_x \to \Var{Prediction}\).
- In the smoking lesion problem, the lesion does not depend on the decision function, so there is no arrow \(F_x \to \Var{Lesion}\).
- In a twin prisoner’s dilemma, the twin’s action depends on the same decision function, so \(F_x \to \Var{TwinAction}\).

### Step 4: Intervene on the A-FDT output node

For each candidate action \(a\), form the hypothetical

\[
\Do(F_x=a).
\]

This means: set the output of the A-FDT procedure on the actual input to \(a\), then update all variables that depend on that output according to \(G\).

### Step 5: Compare expected utilities

Choose

\[
a^\ast
\in
\argmax_{a\in\mathcal A}
\mathbb E[V \mid \Do(F_x=a)].
\]

The A-FDT agent then executes \(a^\ast\).

---

## 5. A-FDT in Newcomb’s problem

Newcomb’s problem is the classic test case. A predictor has placed \$1,000,000 in box B iff she predicted that the agent would take only box B. Box A visibly contains \$1,000. The agent may take both boxes or only box B.

An A-FDT model contains variables such as:

- \(F = \mathrm{A\text{-}FDT}_{\underline P,\underline G,\emptyset}\), the output of A-FDT before the choice;
- \(\Var{Prediction}\), the predictor’s prediction;
- \(\Var{BoxB}\), whether box B is full or empty;
- \(\Act\), the physical action;
- \(V\), utility.

The graph includes:

\[
F \to \Act,
\qquad
F \to \Var{Prediction},
\qquad
\Var{Prediction} \to \Var{BoxB},
\qquad
\Act,\Var{BoxB} \to V.
\]

Suppose the predictor is 99% accurate. If A-FDT intervenes on \(F=\Val{onebox}\), then the agent one-boxes and the predictor almost certainly predicted one-boxing, so box B is almost certainly full. The expected utility is approximately

\[
0.99 \cdot \$1{,}000{,}000 + 0.01 \cdot \$0
=
\$990{,}000.
\]

If A-FDT intervenes on \(F=\Val{twobox}\), then the agent two-boxes and the predictor almost certainly predicted two-boxing, so box B is almost certainly empty. The expected utility is approximately

\[
0.01 \cdot \$1{,}001{,}000
+
0.99 \cdot \$1{,}000
=
\$11{,}000.
\]

Therefore,

\[
\mathrm{A\text{-}FDT}(P,G,\emptyset)=\Val{onebox}.
\]

CDT, by contrast, intervenes directly on \(\Act\). Since the predictor’s prediction is not causally downstream of the agent’s present physical action, CDT holds the contents of box B fixed and concludes that two-boxing always adds \$1,000. EDT also one-boxes, but for a different reason: it conditions on the action as evidence. A-FDT one-boxes because the predictor’s prediction is subjunctively dependent on the output of the agent’s decision function.

---

## 6. A-FDT in the smoking lesion problem

In the smoking lesion problem, smoking is correlated with cancer, but only because a lesion causes both a preference for smoking and cancer. Smoking itself does not cause cancer.

A-FDT’s graph must reflect the fact that the lesion is not a prediction, simulation, or logical consequence of the agent’s decision function. The lesion may affect the agent’s preferences or which utility function she has, but it is not downstream of the A-FDT output variable being intervened upon.

The paper formalizes this by allowing two possible utility functions: one that values smoking positively and one that does not. The lesion determines which utility function the agent has. Correspondingly, there are two possible A-FDT output variables, one for each possible utility function. But the key structural fact is that intervening on the relevant A-FDT output variable does not change the probability of having the lesion.

Thus, in the smoking hypothetical,

\[
P(\Val{lesion} \mid \Do(F=\Val{smoke}))
=
P(\Val{lesion} \mid \Do(F=\Val{refrain})).
\]

Cancer probabilities are therefore unchanged by the A-FDT intervention. Smoking adds utility without changing the chance of cancer. A-FDT smokes.

This is the important contrast with EDT. EDT conditions on smoking and thereby treats smoking as evidence of the lesion. A-FDT does not condition on the action; it intervenes on the decision function’s output. Since the lesion is not subjunctively downstream of that output, A-FDT correctly ignores the merely evidential correlation.

---

## 7. A-FDT in transparent Newcomb and Parfit’s hitchhiker

A more revealing case is the transparent Newcomb problem. The agent sees both boxes. The predictor filled box B iff she predicted that the agent would one-box upon seeing both boxes full. The question is whether the agent should one-box when she sees that box B is full.

CDT says two-box: box B is already full, so taking box A adds \$1,000. EDT also says two-box once it conditions on seeing box B full. A-FDT says one-box.

The formal reason is that A-FDT does not simply condition on the observation. It changes the node on which it intervenes. Let

\[
F_{\Val{full}}
=
\mathrm{A\text{-}FDT}_{\underline P,\underline G,\Val{full}}
\]

be the variable representing what A-FDT outputs when the agent sees a full box B. The graph also includes a variable

\[
F_{\Val{empty}}
=
\mathrm{A\text{-}FDT}_{\underline P,\underline G,\Val{empty}}
\]

for what A-FDT would output upon seeing an empty box B.

If \(F_{\Val{full}}=\Val{onebox}\), then a highly accurate predictor predicted one-boxing upon seeing full boxes, so box B is very likely full. The expected utility is approximately

\[
0.99 \cdot \$1{,}000{,}000
+
0.01 \cdot q \cdot \$1{,}000,
\]

where \(q\) is the probability that the agent two-boxes upon seeing an empty box. The exact value of \(q\) does not matter much; the first term dominates.

If \(F_{\Val{full}}=\Val{twobox}\), then an accurate predictor predicted two-boxing upon seeing full boxes, so box B is very likely empty. In that case the agent would usually not be in the “see full box” branch at all; she would instead see an empty box and act according to \(F_{\Val{empty}}\). The expected utility is approximately

\[
0.01 \cdot \$1{,}001{,}000
+
0.99 \cdot q \cdot \$1{,}000,
\]

which is far lower. Therefore A-FDT outputs \(\Val{onebox}\) upon seeing the full box.

This is the same structure as Parfit’s hitchhiker problem. A driver will save the agent only if she predicts that the agent will pay \$1,000 after reaching the city. Once in the city, CDT and EDT refuse to pay, because payment has no further causal benefit and is bad news conditional on already being safe. A-FDT pays, because the driver’s earlier prediction depends on the output of the agent’s decision procedure in the city. If A-FDT outputs \(\Val{pay}\), the driver predicts payment and saves the agent. If A-FDT outputs \(\Val{refuse}\), the driver predicts refusal and leaves the agent in the desert.

These cases are counterintuitive to many people, but they follow directly from Equation (4) once the observation-dependent nodes are represented correctly.

---

## 8. Policies, observations, and updateless reasoning

Equation (4) is an action-level formula: it chooses an action \(a\) for a given observation \(x\). However, the paper notes that the authors’ preferred formulation iterates over policies rather than isolated actions. A policy is a function

\[
\pi : \mathcal X \to \mathcal A
\]

mapping observations to actions.

A natural policy-level version of A-FDT, consistent with the spirit of the paper, would be

\[
\mathrm{A\text{-}FDT}_{\mathrm{policy}}(P,G)
\coloneqq
\argmax_{\pi}
\mathbb E\!\left[
V \mid \Do(\Pi_{P,G}=\pi)
\right],
\]

where \(\Pi_{P,G}\) is a variable representing the policy output by A-FDT given the agent’s model. The agent then executes \(\pi(x)\) upon receiving observation \(x\).

This policy interpretation helps clarify A-FDT’s treatment of observations. In ordinary Bayesian reasoning, an agent updates on \(x\) by conditioning. In A-FDT, especially in predictor problems, the observation \(x\) may itself be downstream of the agent’s decision function. If the agent conditions on \(x\) in the wrong way, she may destroy the counterfactual dependence that A-FDT is trying to preserve.

For example, in transparent Newcomb, if the agent sees a full box B and simply conditions on \(\Obs=\Val{full}\), she may conclude that two-boxing is better, because given that the box is full, taking both boxes adds \$1,000. But A-FDT’s prescription is not obtained by merely conditioning on the observation. Instead, the observation selects which decision-function output node is being evaluated: \(F_{\Val{full}}\) rather than \(F_{\Val{empty}}\). The hypotheticals then allow the possibility that if \(F_{\Val{full}}\) had a different output, the agent would have received a different observation.

This is why A-FDT has an updateless flavor in some cases. The paper connects this to earlier “updateless” ideas in decision theory. The agent chooses the output of the decision function for a given input by evaluating what kind of decision function performs well across the relevant possibility space, rather than by conditioning away the very observation that may depend on the decision function.

This point is not fully formalized in the source. Equation (4) places the observation \(x\) inside the intervened node, but it does not explicitly say whether the expectation should also condition on \(\Obs=x\). In the paper’s examples, the prescriptions that make A-FDT distinctive require not conditioning away observations that are themselves prediction-dependent. My operational interpretation is therefore:

- If an observation is exogenous and not subjunctively dependent on the decision function, it is safe to condition on it.
- If an observation is produced by predictors, simulations, or other processes that depend on the decision function, A-FDT should treat the observation as an input to the decision function and evaluate the output for that input without simply conditioning the observation away.

This interpretation reproduces the paper’s main examples and preserves the motivation behind Equation (4).

---

## 9. What remains open: constructing the graph \(G\)

The most important open problem is the construction of \(G\). CDT can appeal to Pearl’s mature theory of causal inference, where causal structure can sometimes be learned from observation and experiment. A-FDT requires a broader graph: one that encodes not only causal dependencies but also logical, mathematical, and computational dependencies.

The paper is explicit that Equation (4) works given a graph that accurately describes how changing the logical variable affects other variables, but it does not provide a full account of how to learn or construct such a graph. This is a serious gap. Without \(G\), A-FDT is not yet a complete algorithm for real-world agents.

Still, the source gives enough guidance to formulate a reasonable working heuristic. I propose the following operational rule, which is my own elaboration rather than a fully explicit theorem of the paper:

> Draw an arrow from the A-FDT output node \(F_x\) to a variable \(Z\) when \(Z\) is produced by a process that computes, predicts, simulates, copies, or logically depends on the output of the same decision function. Do not draw such an arrow when \(Z\) is merely correlated with the action through a common cause that does not represent the decision function.

This rule explains the central examples:

- A predictor who models the agent’s reasoning depends on the agent’s decision function, so \(F_x \to \Var{Prediction}\).
- A psychological twin using the same reasoning depends on the same decision function, so \(F_x \to \Var{TwinAction}\).
- A lesion that causes both smoking and cancer does not represent the agent’s decision function, so no arrow \(F_x \to \Var{Lesion}\).
- A blackmailer who sends a letter only if she predicts payment depends on the agent’s decision function, so \(F_x \to \Var{BlackmailerBehavior}\).

For imperfect predictors, the graph should include noise variables. For example, a variable \(\Var{Accurate}\) can determine whether the predictor’s prediction matches the agent’s decision-function output. The intervention on \(F_x\) then changes the predictor’s prediction with high probability but not certainty.

This heuristic is not a complete formal theory of subjunctive dependence, but it is often enough to recover the paper’s verdicts.

---

## 10. Counterpossibles and logical uncertainty

A-FDT also depends on counterpossible reasoning. If the agent is in fact running A-FDT and the actual output is \(a^\ast\), then the hypothetical “the A-FDT function outputs some different action \(a\)” is, strictly speaking, counter-to-logic. There is no possible world in which a deterministic function has a different output on the same input.

The paper acknowledges this issue. A fully satisfying account of counterpossible reasoning is not currently available. However, the paper argues that this is a technical difficulty rather than a fatal objection. Human mathematicians routinely reason under uncertainty about mathematical statements whose truth values are fixed. Similarly, an A-FDT agent does not need to reason about all logical counterpossibles in full generality; she only needs to reason about relatively specific questions such as: “How would the predictor’s prediction change if my decision procedure had a different output?”

In the graphical formulation, this burden is shifted into \(G\). The graph is supposed to tell the agent how the world would differ if the logical variable were changed. This is why the construction of \(G\) is so central.

---

## 11. Why A-FDT’s treatment of dependencies matters

A-FDT’s distinctive treatment of dependencies explains its success in the paper’s test cases.

In Newcomb’s problem, CDT fails because it treats the predictor’s prediction as fixed when intervening on the physical action. A-FDT succeeds because the predictor’s prediction is downstream of the decision-function output.

In the smoking lesion problem, EDT fails because it treats the lesion as evidentially connected to the action. A-FDT succeeds because the lesion is not downstream of the decision-function output.

In transparent Newcomb and Parfit’s hitchhiker, both CDT and EDT fail because they condition on the agent’s current favorable situation and ignore the fact that the agent reached that situation only because of a prediction of her future behavior. A-FDT succeeds because it evaluates the output of the decision function at the relevant observation while preserving the dependency between that output and the earlier prediction.

The same logic extends to blackmail, voting coalitions, and coordination over time. If other agents’ behavior depends on their predictions of one’s decision function, A-FDT represents those dependencies in \(G\). If a future self will face a structurally similar decision, A-FDT can treat future actions as depending on the same decision function or policy, allowing present choices to be made as though they were commitments.

The paper also argues that A-FDT has its own analogue of dominance. CDT’s dominance argument for two-boxing holds fixed the predictor’s prediction while changing the physical action. A-FDT says that this holds fixed something that should not be held fixed: the output of the decision function on which the prediction depends. Once subjunctive dependencies are preserved, one-boxing is not dominated in the relevant sense.

---

## 12. Conclusion

A-FDT is an expected-utility theory that chooses the action corresponding to the best counterfactual output of the agent’s own decision function. Its canonical formal statement, Equation (4), is

\[
\mathrm{A\text{-}FDT}(P,G,x)
=
\argmax_{a\in\mathcal A}
\mathbb E\!\left[
V \mid
\Do\!\left(
\mathrm{A\text{-}FDT}_{\underline P,\underline G,\underline x}=a
\right)
\right].
\]

The theory’s novelty is not that it maximizes expected utility—CDT and EDT do that too—but that it constructs decision hypotheticals by intervening on a logical or computational variable rather than on a physical action variable. This allows A-FDT to preserve dependencies on predictors, twins, simulations, and other agents who reason symmetrically, while avoiding EDT’s tendency to manage the news and CDT’s tendency to imagine impossible failures of reliable prediction.

The main unresolved issue is the construction of the dependency graph \(G\). Equation (4) gives a clean decision rule conditional on having a correct representation of subjunctive dependencies, but the paper does not yet provide a full account of how such representations are to be learned. A reasonable operational heuristic is to let \(G\) encode dependencies from the agent’s decision-function output to any variable that computes, predicts, copies, or otherwise logically depends on that output, while excluding merely statistical common-cause correlations. With that heuristic, A-FDT gives clear, utility-maximizing verdicts in Newcomb’s problem, the smoking lesion problem, transparent Newcomb, Parfit’s hitchhiker, and related predictor dilemmas.

---

## References

Gibbard, A., & Harper, W. L. (1978). Counterfactuals and two kinds of expected utility. In *Foundations and Applications of Decision Theory*.

Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.

Nozick, R. (1969). Newcomb’s problem and two principles of choice. In *Essays in Honor of Carl G. Hempel*.

Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.

Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.

Skyrms, B. (1980). *Causal Necessity*. Yale University Press.

Yudkowsky, E., & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2.