# Action Functional Decision Theory: Choosing the Best Output of a Fixed Decision Function

The supplied reference calls the theory *functional decision theory* (FDT). In this essay I use the assigned name **action functional decision theory**, abbreviated **A-FDT**, while keeping the formal content tied to Equation (4) of Section 5 of the source paper.

A-FDT is a decision theory for agents who want to maximize expected utility in worlds that may contain predictors, copies, twins, simulations, blackmailers, and other systems whose behavior depends on what the agent’s decision procedure would output. Its guiding idea is that the agent should not ask primarily, “Which physical act of mine causes the best outcome?” or “Which act would be best news?” Instead, A-FDT asks:

> “Which output of this decision procedure causes the best outcome?”

The theory’s distinctive move is to treat the agent’s decision as the output of a fixed mathematical function and to evaluate candidate actions by considering counterfactual scenarios in which that very function has a different output.

---

## 1. Expected utility and decision hypotheticals

A-FDT, causal decision theory (CDT), and evidential decision theory (EDT) are all expected utility theories. They agree that an agent should choose an action that maximizes an expected utility expression of the form

\[
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j ; x)\, U(o_j),
\]

where \(a\) is an action, \(o_j\) are possible outcomes, \(x\) is the agent’s observation history, \(U\) is a utility function, and \(P(a \hookrightarrow o_j;x)\) is the probability assigned to outcome \(o_j\) in the hypothetical scenario where \(a\) is chosen after observing \(x\).

The disagreement concerns the meaning of the decision hypothetical \(\hookrightarrow\).

EDT interprets the hypothetical as ordinary Bayesian conditioning:

\[
\mathrm{EDT}(P,x)
=
\arg\max_{a \in \mathcal A}
\mathbb{E}\!\left[V \mid \Obs=x,\Act=a\right],
\]

where \(V\) is the utility variable. EDT asks what would be good news to learn about one’s own action.

CDT interprets the hypothetical as a causal intervention:

\[
\mathrm{CDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb{E}\!\left[V \mid \Do(\Act=a),\Obs=x\right].
\]

Here \(G\) is a causal graph, and \(\Do(\Act=a)\) means: set the physical action variable to \(a\), break its incoming causal arrows, and propagate the change forward through causal descendants.

A-FDT keeps the interventionist structure of CDT but changes the variable on which the agent intervenes. Instead of intervening on the physical action variable, the agent intervenes on a variable representing the output of the agent’s decision procedure given its inputs.

---

## 2. The primary formal definition of A-FDT

Following Equation (4) of the source, the central definition of A-FDT can be written as

\[
\boxed{
\mathrm{A\text{-}FDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb{E}\!\left[
V
\mid
\Do\!\left(
\operatorname{AFDTvar}(\underline{P},\underline{G},\underline{x}) = a
\right)
\right].
}
\]

The notation deserves careful attention.

- \(P\) is the agent’s probabilistic world-model. It includes not only ordinary empirical variables but also variables representing mathematical or computational facts, such as the output of a decision procedure.
- \(G\) is a dependency graph describing how changing one variable affects others. In CDT, \(G\) is purely causal. In A-FDT, \(G\) must also encode what the source calls *subjunctive dependencies*: logical, computational, predictive, or copy-like relationships.
- \(x\) is the observation history.
- \(\operatorname{AFDTvar}(\underline{P},\underline{G},\underline{x})\) is a variable inside the model whose value represents the output of the A-FDT decision procedure when run on inputs \(P\), \(G\), and \(x\).
- The underlines indicate “dequoting”: the model contains a name or representation of \(P\), \(G\), and \(x\), not the objects themselves in some external metalanguage.
- \(\Do(\cdot)\) is an intervention operator analogous to Pearl’s causal \(\Do\)-operator, but applied to a logical or computational variable rather than merely a physical action variable.

The self-reference is important but not fatal. The model contains a variable representing the output of the very procedure that is using the model. The source notes that this kind of self-reference can be handled using standard recursion-theoretic techniques, such as Kleene’s recursion theorem or “quining.”

There are two crucial differences between A-FDT and CDT.

First, CDT intervenes on the physical action variable \(\Act\). A-FDT intervenes on the decision-function output variable \(\operatorname{AFDTvar}(\underline{P},\underline{G},\underline{x})\).

Second, CDT responds to observations by conditioning on them. A-FDT responds to observations mainly by changing which decision-function variable it intervenes on. If the agent observes \(x\), it intervenes on \(\operatorname{AFDTvar}(\underline{P},\underline{G},\underline{x})\). If it had observed \(y\), it would intervene on \(\operatorname{AFDTvar}(\underline{P},\underline{G},\underline{y})\).

This second feature is central in problems such as transparent Newcomb and Parfit’s hitchhiker.

---

## 3. Subjunctive dependence

The philosophical motivation for A-FDT is the distinction between predictor-like dependencies and lesion-like correlations.

In Newcomb’s problem, a predictor has made a highly reliable prediction about the agent’s future action. The predictor’s prediction is not causally downstream from the agent’s later physical action, but it depends on the agent’s decision procedure in a stronger-than-merely-statistical way. If the decision procedure were to output a different action, a sufficiently accurate predictor would have predicted differently.

In the smoking lesion problem, by contrast, a lesion causes both a preference for smoking and a higher probability of cancer. Smoking is evidence of the lesion, but the lesion does not predict the agent’s decision procedure. The cancer risk does not depend on what the agent’s decision function outputs. It is merely correlated with smoking through a common cause.

The source summarizes the idea by saying that functional decision theory relates to subjunctive dependence as causal decision theory relates to causal dependence. In A-FDT terms:

- CDT holds fixed everything except the causal consequences of the physical action.
- EDT holds fixed nothing that is statistically correlated with the action.
- A-FDT holds fixed the relevant logical, mathematical, computational, and causal structure, while varying the output of the decision function.

Thus A-FDT’s counterfactuals are not ordinary causal counterfactuals. They are often counterpossible in the logical sense. If the agent knows with near certainty that its decision procedure will output \(a\), then to evaluate output \(b\) it must consider a scenario in which the same function, on the same inputs, outputs something other than what it in fact outputs. The source acknowledges that a fully satisfactory formal account of such counterpossibles is not yet available.

Nevertheless, the operational intent is clear: when imagining a different output of the decision function, the agent should also imagine corresponding changes in predictions, simulations, copies, and other processes that compute or depend on that same function.

---

## 4. How A-FDT evaluates alternative actions

A practical A-FDT evaluation can be described in five steps. Some of these steps are explicit in the source; others are my own operational interpretation where the source leaves details open.

### Step 1: Specify the decision situation

Identify:

- the action set \(\mathcal A\);
- the current observation history \(x\);
- the utility function \(U\);
- the relevant outcomes.

### Step 2: Build a probabilistic model \(P\)

The model should include variables for:

- exogenous facts;
- the agent’s physical action;
- predictions made by other agents or mechanisms;
- observations the agent might receive;
- outcomes;
- the output of the agent’s decision procedure for relevant inputs.

### Step 3: Build the dependency graph \(G\)

This is the delicate part. The source gives examples but does not provide a general method for constructing \(G\). A reasonable operational rule is:

Draw an arrow from the decision-function variable to a variable \(Z\) if \(Z\) is produced by a process that computes, predicts, simulates, copies, or otherwise depends on the output of the agent’s decision procedure.

For example:

- If a predictor simulates the agent’s reasoning, draw an arrow from the decision-function variable to the predictor’s prediction.
- If another agent runs the same decision procedure in symmetric circumstances, draw arrows from the shared decision-function output to both agents’ actions.
- If a lesion causes both a preference and a disease, do not draw an arrow from the decision-function variable to the disease.
- If the agent’s physical action is executed because the decision procedure outputs it, draw an arrow from the decision-function variable to the physical action.

This graph-construction step is not solved by the source. It is perhaps the main open problem for A-FDT.

### Step 4: Perform interventions on the decision-function variable

For each candidate action \(a\), form the hypothetical model

\[
P_a
=
P \mid \Do\!\left(
\operatorname{AFDTvar}(\underline{P},\underline{G},\underline{x}) = a
\right).
\]

This means: set the decision-function output to \(a\), break incoming arrows to that variable, and propagate the change through the graph \(G\).

### Step 5: Choose the action with highest expected utility

Compute

\[
\mathbb{E}_{P_a}[V]
\]

for each candidate action \(a\), and select an action maximizing this expectation.

---

## 5. A-FDT in Newcomb’s problem

Newcomb’s problem is the standard test case.

A predictor has placed \$1,000,000 in box B iff she predicted the agent would take only box B. Box A visibly contains \$1,000. The predictor is correct with probability \(0.99\).

Let \(D\) abbreviate

\[
D = \operatorname{AFDTvar}(\underline{P},\underline{G},\underline{x}).
\]

A simple A-FDT model may contain the following dependencies:

- \(D \in \{\text{one-box}, \text{two-box}\}\).
- The predictor’s prediction equals \(D\) with probability \(0.99\).
- Box B is full iff the predictor predicted one-boxing.
- The agent’s physical action equals \(D\).
- Utility is:
  - \$1,000,000 for one-boxing when box B is full;
  - \$0 for one-boxing when box B is empty;
  - \$1,001,000 for two-boxing when box B is full;
  - \$1,000 for two-boxing when box B is empty.

Now evaluate the two hypotheticals.

If A-FDT intervenes to set \(D = \text{one-box}\), then the predictor predicted one-boxing with probability \(0.99\). Therefore:

\[
\mathbb{E}[V \mid \Do(D=\text{one-box})]
=
0.99 \cdot 1{,}000{,}000
+
0.01 \cdot 0
=
990{,}000.
\]

If A-FDT intervenes to set \(D = \text{two-box}\), then the predictor predicted two-boxing with probability \(0.99\), so box B is probably empty:

\[
\mathbb{E}[V \mid \Do(D=\text{two-box})]
=
0.01 \cdot 1{,}001{,}000
+
0.99 \cdot 1{,}000
=
11{,}000.
\]

Since \(990{,}000 > 11{,}000\), A-FDT one-boxes.

CDT two-boxes because its intervention \(\Do(\Act=\text{two-box})\) holds the predictor’s prediction fixed. EDT one-boxes because conditioning on one-boxing is good evidence that the box is full. A-FDT one-boxes for a different reason: changing the output of the decision function changes what the predictor would have predicted.

---

## 6. A-FDT in the smoking lesion problem

In the smoking lesion problem, smoking is correlated with cancer, but only because a lesion causes both a liking for smoking and cancer. Smoking itself does not cause cancer.

A-FDT should not treat the lesion as though it were a predictor of the decision function. The lesion does not compute the agent’s decision procedure. It is a common cause of smoking and cancer, not a simulation or prediction of the agent’s reasoning.

So the A-FDT graph should contain arrows such as:

\[
\text{Lesion} \to \text{Smoking preference},
\]

\[
\text{Lesion} \to \text{Cancer},
\]

and

\[
D \to \Act,
\]

but not

\[
D \to \text{Cancer}.
\]

Therefore, when A-FDT intervenes on \(D\), the probability of cancer remains fixed. The only relevant difference between smoking and refraining is the direct utility of smoking. If smoking gives an extra \$1,000 of utility, A-FDT smokes.

This matches the intuitive distinction between Newcomb’s problem and the smoking lesion problem. Newcomb’s predictor is predictor-like: it depends on the agent’s decision function. The lesion is lesion-like: it merely produces a statistical correlation.

---

## 7. A-FDT in transparent Newcomb and Parfit’s hitchhiker

A more difficult case is transparent Newcomb. The agent sees both boxes. Box B is transparent and, in the case under consideration, full. The predictor filled box B iff she predicted the agent would one-box upon seeing two full boxes.

EDT and CDT both tend to two-box once the agent sees that box B is full. EDT conditions on the observation and says that, given a full box, taking both is better. CDT says that the box contents are already fixed, so taking the extra \$1,000 is better.

A-FDT gives a different answer. The agent has observed \(x = \text{full}\), so Equation (4) tells it to intervene on

\[
D_{\text{full}}
=
\operatorname{AFDTvar}(\underline{P},\underline{G},\underline{\text{full}}).
\]

The graph should represent that the predictor predicted what \(D_{\text{full}}\) would output. If \(D_{\text{full}} = \text{one-box}\), then the predictor probably filled box B, and the agent is likely to be in the branch where it sees a full box and receives \$1,000,000. If \(D_{\text{full}} = \text{two-box}\), then the predictor probably did not fill box B, and the agent is unlikely to be seeing a full box in the first place.

Thus, even after seeing a full box, A-FDT evaluates two-boxing by imagining a world in which the decision procedure that runs upon seeing a full box outputs two-boxing. In that world, the predictor would usually have left the box empty. The one-boxing hypothetical has higher expected utility, so A-FDT one-boxes.

This is equivalent to paying the driver in Parfit’s hitchhiker problem. The driver saves the agent only if she predicts the agent will pay later. Once in the city, CDT and EDT refuse to pay. A-FDT pays, because the decision procedure that pays upon reaching the city is the one that causes the driver to save the agent in the first place.

The source defends this behavior using arguments from precommitment, value of information, and achieved utility. A-FDT agents act as they would wish to have precommitted to act, without needing actual binding precommitments.

---

## 8. A-FDT and policies

Equation (4), as presented in the source, chooses an action after an observation. However, the source also notes in a footnote that the authors’ preferred formulation often evaluates policies rather than isolated actions. A policy is a function

\[
\pi : \mathcal X \to \mathcal A
\]

mapping observations to actions.

A policy-level version of A-FDT would introduce a variable \(\Pi\) representing the chosen policy and evaluate

\[
\Pi^*
=
\arg\max_{\pi}
\mathbb{E}
\left[
V
\mid
\Do(\Pi = \pi)
\right].
\]

The agent would then execute \(\Pi^*(x)\) upon observing \(x\).

This policy formulation is especially useful when the agent’s current observation is itself affected by predictions about its future behavior. It also clarifies why A-FDT resists blackmail. In XOR blackmail, for example, a predictor sends a letter iff exactly one of the following is true: the rumor about damage is false and the agent pays, or the rumor is true and the agent does not pay. If the agent pays upon receiving the letter, the letter becomes good news. If the agent refuses, the letter becomes bad news. But the letter does not affect whether the damage exists.

A-FDT refuses to pay because intervening on the decision procedure’s output changes whether the letter is sent, not whether the underlying damage exists. More generally, A-FDT avoids making itself a profitable target for predictors who condition their behavior on the agent’s anticipated compliance.

The source does not fully formalize the policy version in Equation (4), so I regard the policy equation above as a natural extension rather than the assigned core formula.

---

## 9. What A-FDT preserves and what it breaks

A useful way to understand A-FDT is by comparison with CDT and EDT.

EDT preserves too many correlations. If an action is statistically correlated with bad news, EDT may avoid the action even when the action has no causal or logical influence on the bad news. This is why EDT fails in the smoking lesion problem and pays in some blackmail problems.

CDT preserves too few correlations. It breaks correlations between the agent’s action and predictors, even when the predictor’s behavior is reliably computed from the agent’s decision procedure. This is why CDT two-boxes in Newcomb’s problem, defects in symmetric prisoner’s dilemmas, and behaves unstably in Death in Damascus-style problems.

A-FDT tries to preserve exactly the decision-relevant dependencies. It breaks merely evidential correlations that do not track the decision function, but it preserves dependencies arising from prediction, simulation, copying, or shared computation.

In cases where every correlation between the action and the environment is caused by the action itself, A-FDT, CDT, and EDT agree. Formally, if the model is such that

\[
\mathbb{E}[V \mid \Act=a]
=
\mathbb{E}[V \mid \Do(\Act=a)]
=
\mathbb{E}[V \mid \Do(D=a)],
\]

then all three theories prescribe the same action. They diverge precisely when predictors, twins, simulations, or other subjunctive dependencies are present.

---

## 10. Open problems and operational assumptions

The source is explicit that A-FDT’s formal presentation rests on assumptions that are not yet fully developed.

The largest open problem is the construction of \(G\). Pearl’s causal framework gives a developed account of how causal structure can be learned from observation and experiment. The source says there is not yet an analogous account for subjunctive dependencies. We do not have a fully general method for learning which variables depend on the output of a decision function.

A second open problem is the semantics of counterpossible conditionals. A-FDT must reason about what would happen if a mathematical function had a different output, even when the function in fact has a determinate output. The source treats this as a technical difficulty, not a fatal objection, but it remains unresolved.

A third issue is bounded rationality. Real agents cannot explicitly represent all mathematical dependencies or compute exact expected utilities over rich world-models. The source’s examples are idealized. A realistic A-FDT agent would need approximations, heuristics, and limited models.

Where the source leaves details open, the operational interpretation I have used is this: construct \(G\) by identifying variables that are computed from, predicted from, or logically tied to the agent’s decision procedure; then perform model surgery on the decision-function variable and propagate the intervention through those dependencies. This is not a complete formal solution, but it captures the examples and gives a usable method for unfamiliar cases.

---

## 11. Why A-FDT matters

A-FDT matters because many important strategic situations are not purely causal. Cooperation among similar agents, credible commitments, voting coalitions, blackmail, prediction markets, and interactions between artificial agents often depend on what other systems expect one’s decision procedure to do.

A-FDT gives a unified answer: choose the output of your decision procedure that leads to the best world when all relevant dependencies are respected. This lets A-FDT one-box in Newcomb’s problem, smoke in the smoking lesion problem, pay in Parfit’s hitchhiker problem, cooperate with psychological twins, and refuse exploitative blackmail.

The theory is demanding. It requires a model of logical and computational dependencies, not merely causal ones. But its central rule is simple and coherent: treat your decision as the output of a fixed function, and choose the output that, if produced by that function, yields the best outcome.

---

## Conclusion

Action functional decision theory evaluates actions by intervening on a variable representing the output of the agent’s own decision procedure. Equation (4) of the source paper gives the core formal rule:

\[
\mathrm{A\text{-}FDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb{E}\!\left[
V
\mid
\Do\!\left(
\operatorname{AFDTvar}(\underline{P},\underline{G},\underline{x}) = a
\right)
\right].
\]

The theory differs from CDT by intervening on a logical-computational variable rather than a physical action variable, and it differs from EDT by using structured counterfactual interventions rather than simple conditionalization. Its key conceptual tool is subjunctive dependence: predictor-like processes depend on the decision function, while lesion-like common causes do not.

The source provides a compelling set of examples but leaves major implementation questions open, especially the construction of the subjunctive-dependency graph \(G\) and the formal treatment of counterpossibles. Even so, A-FDT offers a clear normative picture: rational action is the selection of the best output of the very decision procedure one is running.

---

## References

Gibbard, A., and Harper, W. L. (1978). Counterfactuals and two kinds of expected utility. In *Foundations and Applications of Decision Theory*.

Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.

Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.

Yudkowsky, E., and Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2.