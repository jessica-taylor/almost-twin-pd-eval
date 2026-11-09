# Action Functional Decision Theory: Choosing the Output of a Fixed Decision Function

Action functional decision theory, which I will call **A-FDT**, is a decision theory whose central move is to evaluate actions not by asking what would happen if a particular physical movement occurred, but by asking what would happen if the agent’s own decision procedure had a different output. The source article calls this theory functional decision theory, or FDT; in this essay I use the name **A-FDT** throughout. The theory can be summarized by the question: “Which output of this very decision procedure would yield the best outcome?”

A-FDT is intended to be a rival to both evidential decision theory, **EDT**, and causal decision theory, **CDT**. EDT asks, roughly, “Which action would be the best news to learn that I performed?” CDT asks, “Which physical action would cause the best downstream consequences?” A-FDT instead asks, “If the mathematical function that I am running output this action rather than that one, what would the world look like?” This shift lets A-FDT preserve useful correlations with predictors, twins, simulations, and other agents who reason symmetrically, while still ignoring merely statistical correlations of the sort that mislead EDT.

The primary formal definition used here is Equation (4), Section 5 of the reference paper, adapted to the name A-FDT:

\[
\mathrm{A\text{-}FDT}(P,G,x)
\coloneqq
\argmax_{a\in\mathcal A}
\mathbb E\!\left[
V \mid \operatorname{do}\!\left(
\mathrm{afdt}(\underline P,\underline G,\underline x)=a
\right)
\right].
\]

Here \(P\) is the agent’s probabilistic world-model, \(G\) is a graph describing the relevant dependency structure of the world, \(x\) is the agent’s observation history, \(\mathcal A\) is the finite set of available actions, and \(V\) is the utility-bearing outcome variable. The expression \(\mathrm{afdt}(\underline P,\underline G,\underline x)\) denotes a variable in the model representing the output of the A-FDT decision procedure itself when run on those inputs. The underlines indicate that we are referring to names or descriptions of objects, not the objects themselves: the model contains a representation of the agent’s own decision function.

This essay explains what that equation means, how A-FDT evaluates alternative actions, how it treats dependencies and counterfactuals, and how one might apply it in practice. I will also indicate where the source leaves matters open and where additional assumptions are needed.

---

## 1. Expected utility and the three hypotheticals

A-FDT, EDT, and CDT are all expected utility theories. They agree that an agent should choose an action that maximizes expected utility, but they disagree about the hypothetical probabilities used in the calculation. A generic expected-utility expression is

\[
\mathcal{EU}(a)
=
\sum_j P(a \then o_j; x)\,U(o_j),
\]

where \(o_j\) are possible outcomes, \(U\) is a utility function, \(x\) is the agent’s observation history, and \(P(a \then o_j;x)\) is the probability assigned to outcome \(o_j\) in the hypothetical situation where action \(a\) is taken after observing \(x\). The theories differ in how they interpret \(\then\).

EDT interprets the decision hypothetical as ordinary Bayesian conditioning:

\[
\mathrm{EDT}(P,x)
=
\argmax_{a\in\mathcal A}
\mathbb E\!\left[V \mid \Obs=x,\Act=a\right].
\]

Thus EDT evaluates an action by asking what the world is probably like conditional on the agent performing that action. This works well when actions are good evidence for desirable states, but it fails when an action is merely evidence of a bad background condition. In the smoking lesion problem, smoking is evidence of a lesion that causes cancer, even though smoking does not cause cancer. EDT then avoids smoking, thereby forgoing a sure benefit.

CDT interprets the decision hypothetical as a causal intervention. Using Pearl-style notation,

\[
\mathrm{CDT}(P,G,x)
=
\argmax_{a\in\mathcal A}
\mathbb E\!\left[
V \mid \operatorname{do}(\Act=a),\Obs=x
\right].
\]

The \(\operatorname{do}\)-operator modifies the model by setting the physical action variable \(\Act\) to \(a\), then propagating the effects only along causal arrows. CDT therefore ignores correlations between the action and variables that are not causally downstream of the action. This correctly handles the smoking lesion problem, because the lesion is not causally downstream of smoking. But CDT fails in Newcomb-style problems, because the predictor’s earlier action is causally upstream of the agent’s present physical act, even though it depends on a prediction of that act.

A-FDT accepts the CDT-style idea of graph surgery but changes the variable on which the surgery is performed. Instead of intervening on the physical action variable \(\Act\), A-FDT intervenes on a variable representing the output of the agent’s decision function.

---

## 2. Equation (4): A-FDT as surgery on a decision-function variable

The formal core of A-FDT is the following rule:

\[
\boxed{
\mathrm{A\text{-}FDT}(P,G,x)
=
\argmax_{a\in\mathcal A}
\mathbb E\!\left[
V \mid \operatorname{do}\!\left(
D_{P,G,x}=a
\right)
\right]
}
\]

where I write

\[
D_{P,G,x}
=
\mathrm{afdt}(\underline P,\underline G,\underline x)
\]

for the variable representing the output of the A-FDT procedure applied to the agent’s current model \(P\), dependency graph \(G\), and observation history \(x\).

For each candidate action \(a\), A-FDT constructs a hypothetical model

\[
P_a
=
P \mid \operatorname{do}(D_{P,G,x}=a),
\]

and computes the expected utility of \(V\) in that model. It then chooses the action whose corresponding hypothetical has highest expected utility.

This is an intervention on a logical or computational variable, not directly on a physical variable. The physical action \(\Act\) may be downstream of \(D_{P,G,x}\) in the graph, but it need not be the sole downstream variable. A predictor’s prediction, a psychological twin’s choice, a simulation’s output, or even the observation the agent expects to receive may also depend on \(D_{P,G,x}\). The graph \(G\) specifies which variables change when the decision-function output changes.

The source emphasizes two differences between A-FDT and CDT. First, CDT intervenes on a physical action variable; A-FDT intervenes on a variable representing the output of a decision procedure. Second, CDT responds to observations by conditioning on them, whereas A-FDT responds to observations by changing which decision-function variable it intervenes upon. In the source’s words, when CDT’s observation history changes from \(x\) to \(y\), CDT changes from conditioning on \(\Obs=x\) to conditioning on \(\Obs=y\), while A-FDT changes from intervening on \(\mathrm{fdt}(\underline P,\underline G,\underline x)\) to intervening on \(\mathrm{fdt}(\underline P,\underline G,\underline y)\). Relabelled in our notation, A-FDT changes from intervening on \(D_{P,G,x}\) to \(D_{P,G,y}\).

This second point is especially important in problems where the observation itself is decision-relevant. In the transparent Newcomb problem, for example, seeing a full box is itself evidence that the predictor predicted one-boxing. A-FDT does not simply condition on seeing the full box and then choose the locally best physical action. Instead, it asks what would happen if the decision procedure run upon seeing a full box output one-box versus two-box.

---

## 3. Subjunctive dependence

The philosophical motivation for A-FDT is the notion of **subjunctive dependence**. Two physical systems are subjunctively dependent on the same function when their behavior is constrained to correspond because they compute, predict, simulate, or otherwise depend on that function.

The source gives the image of two calculators computing the same arithmetic expression. If one calculator outputs \(7336\) for \(6288+1048\), then, assuming both are working correctly, the other calculator will also output \(7336\). The calculators need not causally influence one another. Their outputs are not correlated merely by accident; they are correlated because they are tracking the same mathematical function.

A-FDT treats predictors and twins in a similar way. If a reliable predictor has modeled the agent’s decision procedure, then the predictor’s prediction is subjunctively dependent on the output of that procedure. If a psychological twin reasons using the same decision procedure, then the twin’s action is subjunctively dependent on the same output. In both cases, A-FDT’s counterfactuals preserve the correlation between the agent’s action and the predictor’s prediction or twin’s action.

By contrast, a lesion that causes both a desire to smoke and a tendency to develop cancer is not subjunctively dependent on the agent’s decision procedure. The lesion may make smoking statistically correlated with cancer, but the lesion is not computing the agent’s decision function, nor is it predicting the output of that function. Therefore A-FDT does not allow an intervention on the decision-function output to change the lesion or the cancer rate, except through ordinary causal pathways.

The source puts the contrast succinctly: EDT respects too many correlations, CDT respects too few, and A-FDT tries to respect the right ones. EDT preserves all evidential correlations, including merely statistical ones. CDT preserves only causal downstream dependencies. A-FDT preserves causal dependencies and also decision-relevant logical, mathematical, computational, and predictive dependencies.

The graph \(G\) is the formal object encoding this information. In a CDT graph, arrows represent causal influence. In an A-FDT graph, arrows represent the broader dependency structure relevant to counterfactual changes in logical variables. If changing the output of the A-FDT function would change a predictor’s prediction, then \(G\) should contain a path from \(D_{P,G,x}\) to the prediction variable. If changing the output of the A-FDT function would not change whether the agent has a lesion, then \(G\) should not contain such a path to the lesion variable.

This is the main open problem in the theory. The source supplies Equation (4) as a decision rule given a suitable graph \(G\), but it does not provide a general method for constructing \(G\) from observation and experiment. Pearl’s causal calculus has a well-developed account of how causal structure can be learned or represented; A-FDT requires an analogous account of subjunctive or logical dependency, and the source explicitly identifies this as a major unresolved issue.

---

## 4. A-FDT in Newcomb’s problem

Newcomb’s problem is the classic test case. An agent faces a transparent box A containing \$1,000 and an opaque box B containing either \$1,000,000 or nothing. A reliable predictor has already predicted whether the agent will take only box B or both boxes. Box B is full iff the predictor predicted one-boxing.

Let the action set be

\[
\mathcal A=\{\textit{one-box},\textit{two-box}\}.
\]

Let \(D\) abbreviate \(D_{P,G,x}\), the variable representing the output of A-FDT in this situation. The A-FDT graph contains, at minimum, the following dependencies:

\[
D \rightarrow \Act,
\]
\[
D \rightarrow \Var{Prediction},
\]
\[
\Var{Prediction} \rightarrow \Var{BoxB},
\]
\[
\Act,\Var{BoxB} \rightarrow V.
\]

The predictor is 99% accurate. Thus, under the intervention \(\operatorname{do}(D=\textit{one-box})\), the predictor predicts one-boxing with probability \(0.99\), box B is full with probability \(0.99\), and the expected utility is approximately

\[
0.99 \cdot \$1{,}000{,}000
+
0.01 \cdot \$0
=
\$990{,}000.
\]

Under the intervention \(\operatorname{do}(D=\textit{two-box})\), the predictor predicts two-boxing with probability \(0.99\), box B is empty with probability \(0.99\), and the expected utility is approximately

\[
0.01 \cdot \$1{,}001{,}000
+
0.99 \cdot \$1{,}000
=
\$11{,}000.
\]

A-FDT therefore chooses one-boxing:

\[
\mathrm{A\text{-}FDT}(P,G,x)=\textit{one-box}.
\]

CDT chooses two-boxing because it intervenes on \(\Act\) and holds the contents of box B fixed. EDT also one-boxes, but for a different reason: it conditions on the action and treats one-boxing as good evidence that the box is full. A-FDT one-boxes without treating the action as mere evidence. It one-boxes because, in its hypotheticals, changing the output of the decision procedure changes the predictor’s prediction.

This distinction matters when we compare Newcomb’s problem with the smoking lesion problem.

---

## 5. A-FDT in the smoking lesion problem

In the smoking lesion problem, smoking is correlated with cancer, but only because a lesion causes both a preference for smoking and a high probability of cancer. Smoking itself does not cause cancer. The agent gains \$1,000 utility from smoking and gains \$1,000,000 utility from not dying of cancer.

EDT refrains from smoking because smoking is bad news: it is evidence of the lesion. CDT smokes because smoking does not causally affect cancer. A-FDT agrees with CDT here.

The crucial graphical point is that the A-FDT decision-function variable affects the action but does not affect the lesion or the cancer variable. A simplified dependency structure is:

\[
\Var{Lesion} \rightarrow \Var{Cancer},
\]
\[
\Var{Lesion} \rightarrow \text{preferences or utility function},
\]
\[
D \rightarrow \Act,
\]
\[
\Act \rightarrow V.
\]

There is no arrow

\[
D \rightarrow \Var{Lesion}
\]

and no arrow

\[
D \rightarrow \Var{Cancer}
\]

except insofar as cancer is causally downstream of the lesion, not of the decision function.

The source formalizes the problem by allowing two possible utility functions, depending on whether the agent has the lesion. If the agent has the lesion, she has preferences \(\Util_S\); if not, she has preferences \(\Util_R\). Correspondingly, there are two possible A-FDT outputs, one for each possible preference state. The actual action is determined by whichever A-FDT instance is operative. But intervening on the relevant A-FDT output does not change the probability of the lesion.

Thus, when A-FDT compares

\[
\operatorname{do}(D=\textit{smoke})
\]

with

\[
\operatorname{do}(D=\textit{refrain}),
\]

the probability of cancer remains the same in both hypotheticals. The only difference is the direct utility of smoking. Smoking is better by the value of smoking in the branches where the agent’s actual preferences give smoking positive value. Therefore A-FDT smokes.

This illustrates the intended balance of A-FDT. It one-boxes in Newcomb’s problem because the predictor is subjunctively dependent on the decision procedure. It smokes in the lesion problem because the lesion is not subjunctively dependent on the decision procedure.

---

## 6. Transparent Newcomb and Parfit’s hitchhiker

A-FDT’s distinctive character is clearest in cases where both EDT and CDT fail. The transparent Newcomb problem is one such case. Both boxes are transparent. The predictor filled box B iff she predicted that the agent would one-box after seeing that both boxes are full. The agent now sees that both boxes are full.

CDT two-boxes: given that box B is full, taking both boxes yields an extra \$1,000. EDT also two-boxes: conditional on seeing box B full, taking both boxes is better news than leaving money behind. A-FDT, however, one-boxes.

Let \(D_{\textit{full}}\) be the A-FDT output variable for the procedure run after observing that box B is full. A-FDT evaluates

\[
\mathbb E[V \mid \operatorname{do}(D_{\textit{full}}=\textit{one-box})]
\]

against

\[
\mathbb E[V \mid \operatorname{do}(D_{\textit{full}}=\textit{two-box})].
\]

If \(D_{\textit{full}}=\textit{one-box}\), then, with high probability, the predictor predicted one-boxing and filled the box. The agent sees the full box and leaves behind \$1,000, winning approximately \$1,000,000.

If \(D_{\textit{full}}=\textit{two-box}\), then, with high probability, the predictor predicted two-boxing and left box B empty. In that case the agent would not normally be in the branch where she sees a full box. The hypothetical in which the procedure outputs two-box is mostly a hypothetical in which the agent sees an empty box and receives a much lower payoff.

Thus A-FDT one-boxes even when it sees both boxes full. The source argues that this is equivalent to paying the driver in Parfit’s hitchhiker problem. In that problem, a driver rescues an agent from the desert only if she predicts that the agent will later pay \$1,000. Once in the city, CDT and EDT both refuse to pay, because the rescue has already occurred. But because they would refuse, a reliable predictor detects this and leaves them to die. A-FDT pays. It treats the decision “pay after being rescued” as the very output on which the driver’s prediction depended. If that output is pay, the agent is rescued; if it is refuse, the agent is not rescued.

These cases can feel counterintuitive. After all, once the agent sees both boxes full or has already arrived in the city, the locally dominant physical action appears to be two-boxing or refusing to pay. A-FDT rejects the local framing. It evaluates the output of the decision procedure across the whole dependency structure, including the processes that produced the agent’s current observation.

---

## 7. How A-FDT evaluates alternative actions

The operational logic of A-FDT can be summarized in a sequence of steps.

First, specify the action set \(\mathcal A\), the observation history \(x\), the utility function \(U\), and the outcome variable \(V\).

Second, construct a probabilistic model \(P\) containing variables for the relevant facts: the agent’s action, the state of the environment, predictions, other agents’ decisions, observations, and the output of the A-FDT procedure itself.

Third, construct or assume a dependency graph \(G\). The graph should indicate which variables would change if the output of the A-FDT procedure changed. In particular, draw arrows from the A-FDT output variable to:

1. the agent’s physical action;
2. other agents or systems implementing the same decision procedure;
3. predictors or simulations that model the output of the procedure;
4. observations whose occurrence depends on such predictions or simulations;
5. ordinary causal consequences of the action.

Do not draw arrows from the A-FDT output variable to variables that are merely statistically correlated with the action, such as common causes that do not compute or predict the decision procedure.

Fourth, for each action \(a\), perform the intervention

\[
\operatorname{do}(D_{P,G,x}=a).
\]

This means: set the decision-function output variable to \(a\), cut its incoming dependencies for the purposes of the intervention, and propagate the consequences through \(G\).

Fifth, compute

\[
\mathbb E[V \mid \operatorname{do}(D_{P,G,x}=a)].
\]

Sixth, choose an action maximizing this quantity.

This procedure makes A-FDT a kind of functional maximization. The agent is not merely comparing physical acts; she is comparing possible outputs of a fixed function. The “action functional” is the map

\[
a
\mapsto
\mathbb E[V \mid \operatorname{do}(D_{P,G,x}=a)].
\]

A-FDT selects the argument that maximizes this functional.

---

## 8. Actions, policies, and observations

Equation (4) as presented in the source intervenes on the output of the decision procedure for a given observation history \(x\). This is sufficient for many single-shot problems. However, the source also notes that the authors’ preferred formulation iterates over policies rather than isolated actions. A policy is a function

\[
\pi : \mathcal X \rightarrow \mathcal A
\]

mapping possible observations to actions.

This policy formulation matters in sequential or multi-agent settings where one decision affects later observations or where the agent must coordinate across multiple input conditions. In such cases, a natural policy-level version of A-FDT would be

\[
\pi^*
=
\argmax_{\pi}
\mathbb E\!\left[
V \mid \operatorname{do}(\Pi=\pi)
\right],
\]

where \(\Pi\) is a variable representing the output of the agent’s policy-selection procedure. The agent then executes \(\pi^*(x)\) upon observing \(x\).

This policy version is not fully formalized in the supplied source, and Equation (4) itself remains the assigned primary presentation. Still, the policy interpretation is a reasonable operational extension. It preserves the core A-FDT idea: intervene not on the local physical act alone, but on the output of the agent’s decision function, understood as a function from inputs to behavior.

Observations require special care. In CDT, after observing \(x\), the agent conditions on \(\Obs=x\). In A-FDT, observation \(x\) enters primarily as an input to the decision-function variable \(D_{P,G,x}\). This allows A-FDT to consider counterfactual scenarios in which a different output would have led to different observations. In transparent Newcomb, for example, imagining that the full-box procedure outputs two-box leads A-FDT to imagine that the box would probably have been empty.

This feature is sometimes described as “updateless” in spirit: A-FDT does not always treat the current observation as an immutable condition when evaluating outputs. Instead, it asks what the world would look like if the decision procedure that produced the observation-related behavior had had a different output. The source associates this idea with earlier updateless or timeless decision theories.

There is an ambiguity here. If some observed facts are genuinely exogenous and not decision-relevant, conditioning on them seems harmless. But if the observation is itself downstream of predictions about the agent’s decision procedure, conditioning on it can break the subjunctive dependencies that A-FDT wants to preserve. The source does not give a fully general rule for separating decision-relevant observations from exogenous background facts. A practical interpretation is to condition only on facts that the agent is confident are not subjunctively dependent on the output being evaluated. This is an operational refinement, not a fully explicit part of the source’s formalism.

---

## 9. Counterpossibles and logical uncertainty

A-FDT’s hypotheticals are often counterpossible. If the agent’s decision procedure is deterministic, then for a given input it has exactly one output. To evaluate an alternative action \(a\), A-FDT must nevertheless consider the scenario in which the same function outputs \(a\) instead. In a strict logical sense, if the actual output is \(a_1\), then the statement “the output is \(a_2\)” is false and perhaps impossible.

The source acknowledges this difficulty. A-FDT requires some capacity for counterpossible reasoning: reasoning about what would follow if a mathematical or logical fact were different. The source notes that this is a technical drawback relative to CDT, because we lack a fully satisfactory general account of counterpossible conditionals.

Nevertheless, the source argues that the problem is not fatal. Human mathematicians often reason under uncertainty about logical claims whose truth is fixed. We can discuss what would follow if the twin prime conjecture were false, even if one of the conjecture or its negation is in fact logically impossible relative to the axioms. Similarly, an A-FDT agent need only reason about limited counterpossibles such as: “How would this predictor’s prediction change if my decision algorithm output one-box instead of two-box?”

In the graphical formalization, this counterpossible reasoning is outsourced to \(G\). Given \(G\), the agent can use a Pearl-style \(\operatorname{do}\)-operator to compute the consequences of changing the decision-function variable. The source does not define a primitive \(\operatorname{true}\) operator that updates a probability distribution on the basis of arbitrary logical sentences. Instead, it reuses \(\operatorname{do}\) once the relevant dependency graph is supplied.

This is elegant but incomplete. A full implementation of A-FDT would need a way to represent logical uncertainty, self-reference, and subjunctive dependencies among computations. The source mentions Kleene’s recursion theorem and quining as reasons to think self-reference is manageable: a model can contain a representation of the agent’s own decision procedure without the agent already knowing the procedure’s output. But the deeper problem of learning or inferring the graph of logical dependencies remains open.

---

## 10. Dominance and fair problems

CDT often appeals to dominance. In Newcomb’s problem, two-boxing dominates one-boxing in the CDT sense: holding the box contents fixed, taking both boxes yields more money than taking only one. A-FDT rejects this dominance argument because it rejects the underlying counterfactuals. To hold the box contents fixed while changing the agent’s action is, in A-FDT’s view, to hold fixed the output of the predictor while changing the output of a decision procedure that the predictor reliably tracks. That is like imagining a calculator outputting the wrong answer while holding fixed the arithmetic expression it is computing.

A-FDT has its own dominance notion: an action \(a\) dominates \(b\) if, after holding fixed all relevant subjunctive dependencies and changing only the output of the decision procedure from \(b\) to \(a\), \(a\) is never worse and sometimes better. In Newcomb’s problem, under A-FDT-style counterfactuals, two-boxing does not dominate one-boxing, because changing the decision-function output from one-box to two-box also changes the predictor’s prediction and makes the agent worse off.

The source also discusses fairness. A-FDT is not claimed to dominate every possible rival in every logically possible environment. One can construct problems that punish an agent for using A-FDT itself, or that reward agents for following some arbitrary rule. The source’s claim is narrower: in “fair” problems, where the environment rewards or punishes the agent’s behavior rather than the mere identity of her decision procedure, A-FDT appears to perform at least as well as EDT and CDT and often better.

This fairness notion is intuitive but not fully formalized. The source acknowledges that giving a precise criterion for fairness is difficult. Still, the informal idea is important: A-FDT is designed for environments containing predictors, copies, simulations, and strategic agents, not merely for environments where all action-correlations are simple causal effects.

---

## 11. What follows from the source, and what requires extra assumptions

The source supplies several central claims:

1. A-FDT chooses the output of the agent’s decision function that maximizes expected utility under an intervention on that output.
2. The formal rule is Equation (4), which reuses Pearl-style \(\operatorname{do}\)-surgery given a graph \(G\).
3. A-FDT one-boxes in Newcomb’s problem, smokes in the smoking lesion problem, one-boxes in transparent Newcomb, and pays in Parfit’s hitchhiker problem.
4. A-FDT’s hypotheticals preserve subjunctive dependencies, including predictive and computational dependencies.
5. The theory depends on counterpossible reasoning and lacks a complete account of how to learn subjunctive dependency graphs.

Beyond these source claims, several operational assumptions are needed if one wants to apply A-FDT to unfamiliar cases.

First, one needs a method for constructing \(G\). The source does not provide one. A reasonable heuristic is to identify which parts of the environment compute, predict, simulate, or depend on the agent’s decision procedure. If a variable is produced by a process that models the agent’s reasoning, draw a dependency from the A-FDT output variable to that variable. If a variable is merely a common cause of the action and some outcome, and does not track the decision procedure, do not draw such a dependency.

Second, one needs a way to handle uncertainty about \(G\). In real applications, the agent may not know whether a predictor is reliable, whether another agent is using the same algorithm, or whether a correlation is predictive or merely statistical. A natural extension is to place a probability distribution over possible graphs or dependency structures and maximize expected utility relative to that distribution. This is not explicitly developed in the source.

Third, one needs a policy-level formulation for sequential decisions. The source mentions that the authors prefer policies, but Equation (4) primarily presents action-level choices. The policy extension is natural but requires additional formal care.

Fourth, one needs a treatment of self-reference and fixed points. The model contains a variable representing the output of the agent’s own decision procedure. In ordinary cases this is harmless, but in adversarial or highly self-referential environments it may create fixed-point puzzles. The source gestures at quining and recursion theory but does not give a full resolution.

These gaps do not make A-FDT unusable, but they mean that Equation (4) should be understood as a decision rule relative to a structured model, not as a complete epistemology of subjunctive dependence.

---

## 12. Conclusion

Action functional decision theory evaluates choices by asking which output of the agent’s own decision function would lead to the best world. Its formal core is an expected-utility maximization over interventions on a variable representing the output of the A-FDT procedure:

\[
\mathrm{A\text{-}FDT}(P,G,x)
=
\argmax_{a}
\mathbb E[V \mid \operatorname{do}(D_{P,G,x}=a)].
\]

This simple change of intervention target gives A-FDT its distinctive advantages. It preserves correlations with predictors and symmetric reasoners, allowing it to one-box in Newcomb’s problem and cooperate in twin prisoner’s dilemmas. It severs merely statistical correlations, allowing it to smoke in the smoking lesion problem. It handles transparent Newcomb and Parfit’s hitchhiker by treating observations and rescue conditions as themselves dependent on the decision function’s output.

The theory’s main weakness is also clear: it requires a graph of subjunctive dependencies, and we do not yet have a general method for constructing such graphs. A-FDT also relies on counterpossible reasoning about mathematical functions. These are serious open problems. But as a normative rule for agents who face predictors, copies, simulations, and strategic interactions, A-FDT provides a unified and powerful principle: choose the output of this very decision function that yields the best expected world.

---

## References

Yudkowsky, E. and Soares, N., *Functional Decision Theory: A New Theory of Instrumental Rationality*, Machine Intelligence Research Institute, arXiv:1710.05060v2.

Pearl, J., *Causality*, Cambridge University Press, 2000.