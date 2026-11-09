# 023_fdt_eq4_qwen_qwen3.8-max-prime_rhigh_plow / 00005

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/c4bf707d-5dcf-4b2b-ba65-dc802df67be4/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/c4bf707d-5dcf-4b2b-ba65-dc802df67be4/call_0/response.raw) · finish: `stop`

### Visible response

```text
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
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request: produce substantive mathematical essay ~2400-3000 words explaining A-FDT, using Equation (4), Section 5 of supplied paper as primary formal presentation. Need use A-FDT consistently as assigned decision theory's name, including headings/examples, identify other decision theories by distinct names. Keep quotations faithful. Explain best mathematical understanding and application. Where implementation details not determined, explain source vs additional assumptions. Need likely produce final essay only. Need think deeply.

We need craft essay around A-FDT. Need rename FDT to A-FDT? The user says explain action functional decision theory (A-FDT). Take Equation (4), Section 5 as primary formal presentation of A-FDT for this assignment. Use A-FDT consistently as assigned decision theory's name, including headings and examples, and identify any other decision theory by distinct name. So we must call it A-FDT, not FDT? It says use A-FDT consistently as assigned decision theory's name. We can mention source calls it functional decision theory (FDT), but for this essay we call it A-FDT. Need be careful. Equation (4) in source:
\FDT(P,G,obs) := argmax_{a in A} E(V | Do(FDTvar(underline P, underline G, underline x)=a))
Actually in source: Equation (4)
\[
\label{eq:fdt}
  \FDT(P, G, \obs) \coloneqq \argmax_{\act \in \mathcal A} \EE\left(\VV \cond \Do\left(\FDTvar(\underline P,\underline G,\underline x)= \act\right)\right).
\]
Need adapt to A-FDT: perhaps AFDT(P,G,x) = argmax_a E[V | do(fdt(underline P, underline G, underline x)=a)]. But if A-FDT stands for action functional decision theory, maybe variable is AFDT? Need likely define \mathrm{A\text{-}FDT}. We can present as:
A-FDT(P,G,x) = argmax_{a in A} E_P[ V | do( F_{A-FDT}(\underline{P},\underline{G},\underline{x}) = a ) ].
Where F_{A-FDT} is the decision-function output variable. Need note source uses FDT; I relabel as A-FDT per assignment. Need maybe preserve quotations? If quoting source "FDT" maybe faithful, but use A-FDT in our voice. Could say source's FDT is the theory here called A-FDT. Quotations must remain FDT if quoted? Keep quotations faithful. Could avoid many direct quotes.

Need produce essay ~2400-3000 words. Need include definitions, equations, examples. Target around 2700 maybe. Need not exhaustive. Need explain how evaluates alternative actions/policies, dependencies, counterfactuals. Need mention source leaves open construction of G subjunctive dependency graph; True operator; counterpossibles; policies vs actions footnote; self-reference; observation handling. Need develop operational interpretation if reasonable. Distinguish source claims from own assumptions.

Need likely structure:
Title: Action Functional Decision Theory (A-FDT): Choosing the Output of a Fixed Decision Function
1. Central idea
2. Formal framework: expected utility, hypotheticals, EDT/CDT contrast
3. Equation (4) of A-FDT
4. Constructing models: variables, graph G, subjunctive dependencies
5. Examples: Newcomb, Smoking lesion, Transparent Newcomb / Parfit's hitchhiker, maybe XOR blackmail or twin PD. Use A-FDT in examples.
6. Policies and observations: action vs policy, source's equation interventions on action given observation; source footnote preferred policies; operational policy interpretation. Need assigned equation is action-based? Eq (4) uses obs input to decision function and chooses action. Need mention for dynamic/multi-stage, policy may be needed. If applying A-FDT to unfamiliar cases, recommend evaluate policies when observations can depend on outputs. But Equation (4) as given intervenes on output for actual observation. Source says preferred formalization iterates over policies but not difference in paper. Need develop: for single decision with observation already fixed, action-level is enough. For sequential decisions or when observation is endogenous, choose policy pi mapping observations to actions; intervene on policy-output variable. But this is an extension/operational interpretation, not fully in Eq (4). Need distinguish.
7. Open questions: graph G construction, counterpossible semantics, self-reference, fairness. Operational recipe.
8. Conclusion.

Need be mathematically precise. Define probability space with variables. A-FDT world-model (P,G,x). P distribution over variables including logical variables. G directed graph encoding dependency relations (causal and subjunctive). do-operator: Pearl surgery. A-FDT chooses a maximizing expected utility under intervention on decision-function output variable D_{P,G,x} = a. D is a variable naming output of A-FDT when run on (P,G,x). Underlines dequoting. Self-reference via quining. Observations: A-FDT doesn't condition on x in the expectation? Source Eq (4) omits Obs=x? Wait Eq (3) CDT: E(V | Do(Act=a), Obs=x). Eq (4) A-FDT: E(V | Do(FDTvar(...)=a)) no Obs=x? It says second difference: CDT responds to observation by Bayesian conditionalization, FDT responds by changing which node it intervenes upon. Equation (4) has x in variable but no conditioning on Obs=x. In transparent Newcomb they evaluate E(V | Do(FDT(P,G,full)=a, Obs=full)? In text they write:
FDT(Pf,Gf,full) requires maximizing E(V | Do(FDTpgv{full}=a, Obs=full). Actually they have missing bracket: \EE(\VV \mid \Do(\FDTpgv{full}=\act, \Obs=\Val{full}). Maybe they condition on Obs=full. But Equation (4) no conditioning. Need reconcile. In Section 5 says FDT responds to observation by changing which node it intervenes upon, not conditioning. Yet in example transparent Newcomb they condition? The line: "which involves finding the a that maximizes E(V | Do(FDTpgv{full}=a, Obs=full)." It includes Obs=full (maybe typo). Later says Fiona does not react to observations by conditioning; rather switching variable. But also maybe conditioning on observed node to ensure actual observation? Need analyze.

Source Eq (4):
FDT(P,G,obs) := argmax_a E(V | Do(FDTvar(underline P,underline G,underline x)=a)). No Obs conditioning. The observation is encoded in the variable name: fdt(P,G,x). The graph includes observation variables and algorithm nodes for different observations. Intervening on fdt(P,G,x)=a may affect probabilities of observations? In transparent Newcomb, if intervene on fdt(P,G,full)=onebox, then if predictor inaccurate, observation may be empty and action determined by fdt(P,G,empty). They compute expectation including q. They may not need condition on Obs=full; but they say "In case of accurate, Prediction=1, Box B full, Act=a=onebox... If inaccurate, ... Act determined by fdt(empty) ... q". They might not condition on Obs=full. But the expected utility for one-box is $990,000 + 0.01 q * $1,000. If no conditioning on Obs=full, with accurate 0.99 you see full and one-box, with inaccurate 0.01 you see empty and action per fdt(empty). This matches. If conditioned on Obs=full, under do(fdt(full)=onebox) and Obs=full? Then maybe probability accurate? Need Bayes weird. So maybe the example line includes conditioning mistakenly? Let's inspect: "which involves finding the $\act$ that maximizes
\[
  \EE(\VV \mid \Do(\FDTpgv{full}=\act, \Obs=\Val{full}).
\]"
There's missing closing paren. It says Do(...=act, Obs=full)? Could be do(fdt(full)=act) and condition on Obs=full? If condition, then in intervention do, observation fixed full; then if inaccurate? Hmm. But they later: "In case of act=onebox, value determined by Accurate. If Accurate=accurate, Prediction=1, BoxB full, Act=a=onebox... If Accurate=inaccurate, Prediction=2, BoxB empty, and Act determined by fdt(empty) instead." If they conditioned on Obs=full, inaccurate with Prediction=2 and BoxB empty would be inconsistent with Obs=full. So they likely do not condition on Obs=full. Maybe notation is malformed: E(V | Do(FDTpgv{full}=act)), Obs=full outside? But they say evaluate FDT(Pf,Gf,full). So no conditioning. Thus Equation (4) best. Need explain observation enters as argument to decision-function variable; we do not condition on observation when comparing outputs, except perhaps to select which node is the actual input? Need be careful: if actual observation x is known, A-FDT uses node D_x. It can include observed facts as fixed inputs in P? Maybe P already updated? Source says FDT responds to observation by changing which node it intervenes upon, whereas CDT conditionalizes. But P may still incorporate x? It writes FDT(P,G,obs) with P perhaps prior? In Eq (3) CDT(P,G,obs) conditions on Obs=obs. Eq (4) doesn't. The variable includes obs. Need discuss ambiguity. Operational interpretation: take P as agent's model after learning x insofar as x informs non-decision variables, but do not condition on the event Act=a or on the output variable. However, if observation is an endogenous variable in G, evaluating D_x without conditioning lets counterfactual output changes alter the probability of having received x. That is the updateless feature. In actual application, if x is known with certainty, one may restrict to worlds where x obtains for variables not subjunctively affected? Hmm. Need clarify.

The source says "FDT responds to observation by changing which node it intervenes upon. When CDT's observation history updates from x to y, CDT changes from conditioning its model on Obs=x to conditioning its model on Obs=y, whereas FDT changes from intervening on variable fdt(P,G,x) to fdt(P,G,y) instead." That suggests no conditioning on Obs. But in transparent Newcomb, if see full, intervene on fdt(full). That can imagine not seeing full if output different. So yes, updateless with respect to observation's dependency on decision. But P might have been updated on x? If P is updated on x, then P(Obs=x)=1, intervention on fdt(full) may still change Obs? In Pearl do, if Obs is downstream of variables affected by intervention, it can change even if prior P conditioned? If P conditioned on Obs=full, then graph surgery may need handle conditioned distribution; intervention may make Obs=empty impossible? Need not go too deep. We can say the paper's equation treats x as index selecting decision node, not as a conditioning clause in the expectation. If one uses a Bayesian network already conditioned on x, one must be careful not to freeze Obs as exogenous unless source permits; otherwise one loses updateless behavior. This is an implementation detail not fully resolved.

Need also discuss evaluation of alternative actions/policies. Eq (4) chooses action a by expected utility under do(D_x=a). It doesn't choose physical action directly; it chooses output of decision function. The physical action variable is downstream of D_x in G, perhaps stochastic/mediated. If multiple agents with same function, D_x may affect their actions too. If predictors, D_x affects predictions. Need say.

Need include equations for EDT/CDT for contrast:
EDT(P,x)=argmax_a E[V | Obs=x, Act=a]
CDT(P,G,x)=argmax_a E[V | do(Act=a), Obs=x]
A-FDT as above. Need maybe define expected utility sum:
EU(a)=Σ_j P(a ↦ o_j; x) U(o_j). But can focus.

Need discuss dependencies and counterfactuals: subjunctive dependence. CDT preserves causal dependencies only; A-FDT preserves all decision-relevant subjunctive dependencies, including logical/computational. Example calculators. A-FDT counterfactuals are counterpossible: if decision function output were different, all systems computing same function or predicting it would differ accordingly. It severs correlations that are merely statistical (lesion) and retains correlations due to shared computation/prediction. Need explain graph G encodes which variables depend on D. If G has edge D -> Prediction, then intervention changes prediction; if no edge D -> Cancer, lesion remains fixed. Need mention source: graph tells how changing a logical variable affects all other variables. Open problem: no general method to learn G; requires additional assumptions. We can propose operational heuristic: build G by identifying mechanisms: if variable is produced by an agent/model that simulates or instantiates the same decision computation, draw edge from D to that variable; if variable is common cause producing both action and environment but not computing decision, no edge from D. Justify: matches source predictor/lesion distinction. But note not in source fully.

Need examples:
Twin prisoner's dilemma maybe simple. A-FDT intervenes on D. If D=cooperate, twin's action (same function) cooperate, payoff 1M; if D=defect, both defect 1k. Choose cooperate. Need use A-FDT name.
Newcomb: Graph: D -> Act, D -> Prediction (via predictor's model), Prediction -> Box B, Act and BoxB -> V. Intervention D=onebox sets Act=onebox, Prediction predicts onebox with 0.99, BoxB full 0.99. EU ≈ 0.99*1,000,000 + 0.01*0 = 990,000? Actually one-box full gets 1M, empty gets 0. Two-box: full gets 1,001,000, empty 1,000; EU = 0.01*1,001,000 + 0.99*1,000 = 10,010+990=11,000. Choose one-box.
Smoking lesion: Graph: Lesion -> Act? Actually lesion affects preferences/utility and action; D_S or D_R -> Act; Lesion -> Cancer; no edge D -> Cancer. Intervention on D_S (if preferences S) to smoke does not change lesion/cancer probability, adds $1000 utility, choose smoke. Need explain maybe simpler: lesion is common cause of smoking and cancer, not computing A-FDT. So A-FDT smokes.
Transparent Newcomb/Parfit hitchhiker: A-FDT sees full box, intervenes on D_full. If D_full=onebox, predictor likely predicted onebox and box full, EU ~990k; if D_full=twobox, predictor likely predicted twobox and box empty, so in most branches you wouldn't be seeing full; EU low. Choose one-box/pay. Need maybe present as Parfit's hitchhiker: Driver predicts pay; if A-FDT output pay when in city, driver rescues; if output refuse, driver doesn't. Even after rescue, A-FDT pays because intervening on D_city=pay corresponds to worlds where rescue occurs; refusing corresponds to worlds where no rescue. Need note source claims equivalence.

Need discuss XOR blackmail maybe optional to illustrate observation counterfactuals. Could include if length permits. It shows A-FDT refuses payment because if D_letter=refuse, predictor wouldn't send letter; paying makes letter more likely. But maybe too many examples. Need enough.

Need discuss policies: Source footnote: preferred formalization iterates over policies rather than actions; makes difference in multi-agent dilemmas. Eq (4) as assigned is action-output given observation. For unfamiliar cases with multiple observations or strategic interactions, operational A-FDT could choose policy π: observations -> actions by intervening on variable for π or on the function mapping inputs to outputs. But since assignment says Eq (4) primary, present action-level as core, then policy extension as additional assumption. Need maybe define:
A-FDT_policy(P,G) = argmax_π E[V | do(Π = π)] where Π maps each possible observation x to A-FDT output. But source not formal. Or choose output of fixed policy function for actual input. Need say this is suggested by source footnote but not developed; use when actions are staged or when one decision affects future observations. For single-shot fixed observation, action-level Eq (4) suffices.

Need explain alternative actions/policies: The theory evaluates each candidate a by constructing hypothetical distribution P_a = P under do(D_x=a). Then EU_A(a) = E_{P_a}[V]. Choose max. If policies, EU(π)=E_{P under do(Π=π)}[V]. Need discuss if D_x has prior probability zero for some a? Unlike EDT, intervention allows evaluating zero-probability outputs. Need mention.

Need discuss self-reference: variable D_x names output of A-FDT(P,G,x). Model contains representation of own decision function. Kleene recursion theorem/quine makes self-reference harmless. But implementing may require stable self-model; source says agent need not know actual value to have variable. Need note possible circularity: D_x's value is what equation solves; if multiple fixed points? Source doesn't discuss. Could propose operational interpretation: treat D_x as an exogenous logical variable in G for the purpose of intervention, then choose output that maximizes; the actual output is the argmax. If self-referential predictions lead to fixed-point puzzles (e.g., predictors that output opposite), A-FDT may need additional fixed-point or logical uncertainty machinery. Source leaves open. Need distinguish.

Need discuss dominance: A-FDT has its own dominance relative to subjunctive dependencies. It avoids dominated actions in its sense. Could mention not central.

Need discuss philosophical motivation: treating decision as fixed mathematical function, "Which output of this very function would yield best outcome?" Need quote perhaps: source says normative principle? Could quote exact: "Which output of this decision procedure causes the best outcome?" maybe. Need keep faithful. Maybe use one or two quotes.

Need produce essay with headings. Target ~2400-3000 words. We need estimate word count. Let's plan around 2600 words. Sections:
Title (10)
Intro / central idea (300)
Formal EU and theories (500)
Equation (4) detailed (600)
Examples (800)
Policies, observations, operational recipe (400)
Open problems / assumptions (300)
Conclusion (150)
Total ~3050 maybe. Need trim to 2400-3000. Maybe 2700.

Need ensure "A-FDT" consistently. Other theories named EDT, CDT. Could mention "FDT" only when quoting source or noting source's term. But user says use A-FDT consistently as assigned decision theory's name, including headings and examples. It might be okay to say source calls it FDT, here A-FDT, but avoid overuse. If quoting, quote "functional decision theory"? The source uses FDT. Maybe no direct quotes except phrase. Need identify other decision theory by distinct name: EDT, CDT.

Need be careful with notation. Let's define:
- finite action set \mathcal A.
- outcome set \mathcal O, utility U.
- observation x ∈ \mathcal X.
- world model (P,G). P probability distribution over variables including V, Act, Obs, and logical variables.
- D_x := \mathrm{fdt}(\underline{P},\underline{G},\underline{x}) variable representing output of the A-FDT procedure on inputs (P,G,x). We can write \mathrm{AFDT}(\underline{P},\underline{G},\underline{x}) maybe. To align with assignment, define D^{A}_{P,G,x}. Equation:
\[
\mathrm{A\text{-}FDT}(P,G,x)=\arg\max_{a\in\mathcal A}
\mathbb E_P\left[V\mid \operatorname{do}\big(D^{A}_{P,G,x}=a\big)\right].
\]
If we want include Obs? The source Eq (4) no Obs. But perhaps if observation not part of variable? We'll use no conditioning. Mention if one uses CDT-style notation, compare with CDT:
\[
\mathrm{CDT}(P,G,x)=\arg\max_a E[V | do(Act=a), Obs=x]
\]
EDT:
\[
\mathrm{EDT}(P,x)=\arg\max_a E[V | Obs=x, Act=a].
\]
Need note if action prob zero EDT issue.

Need define do-operator: graph surgery setting node to value, cutting incoming arrows, propagating structural equations. For A-FDT, do(D_x=a) sets logical output, not physical Act. G contains edges from D_x to variables that subjunctively depend on it: the agent's physical action, predictions, other agents running same function, perhaps future observations. It does not send edges to variables merely statistically correlated. Then expectation computed in modified model.

Need mention G includes causal and logical dependencies. Source says "augmented with information about logical, mathematical, computational, causal, etc. structure". A-FDT reuses Pearl do given G. It requires G to tell how changing logical variable affects all other variables. It is not a theory of how to construct G.

Need discuss "counterpossibles": Since D_x actually has one output, considering D_x=a for other a is counter-to-logic if deterministic. A-FDT needs ability to reason under impossible antecedents. Source admits no satisfactory account; technical drawback. But operational use can use graph and structural equations as if possible.

Need discuss "subjunctive dependence": two systems computing same function or one predicting output. Causal dependence special case. Statistical common cause not enough. Need maybe include calculators. Use examples.

Potential subtlety: In smoking lesion, source's graph has two possible decision functions depending on lesion because preferences differ. The intervention is on D_{P_S,G} if she has lesion? Actually if lesion changes utility function, there are two P_S/P_R. Need explain maybe simplified. We can avoid detailed two-utility graph and say lesion affects preferences and action but cancer is not downstream of D. A-FDT graph lacks D -> Cancer, so smoking adds sure utility. But to be faithful: The lesion causes agents to love smoking and causes cancer. A-FDT may have uncertainty about own utility function; there are two possible A-FDT outputs, one for each utility. Intervention on the one controlling action doesn't affect lesion. EU of smoke exceeds refrain by p*$1000. Need include enough.

Need mention A-FDT's treatment of observations in transparent Newcomb: observation is not simply conditioned away; when seeing full box, A-FDT intervenes on D_full. Imagining D_full=twobox leads to predictor not filling box, so observation would likely be empty. Thus chooses one-box. This is key. Need explain Parfit's hitchhiker similarly: after rescue, pay because D_city=pay is what caused rescue in subjunctive graph; D_city=refuse would mean not rescued.

Need discuss "fairness" maybe: source says A-FDT outperforms in fair problems where outcome depends on behavior not decision procedure itself. Could mention.

Need distinguish source vs own proposals:
- Source claims: Eq (4) given G; A-FDT one-boxes, smokes, pays; open problem constructing G; counterpossible issue; policy footnote.
- My additional operational interpretation: heuristic for G (predictor/simulation edges), policy extension, fixed-point handling, using local approximate models. Need mark clearly: "The paper does not give...", "A reasonable operational rule, not explicitly in the source, is...".

Need maybe include an "operational recipe" section:
1. Specify action set, utility, observation x.
2. Build P over relevant variables, including logical variable D_x for A-FDT output and variables for predictors/twins.
3. Build G: draw arrows from D_x to physical action and to any variable that is a computation/prediction/simulation of D_x or depends on it by logical/mathematical constraint; include causal arrows downstream; do not draw arrows from D_x to common causes or merely evidential correlates.
4. For each a, perform do(D_x=a), compute expected V.
5. Choose max. If sequential, evaluate policies similarly (additional assumption).
Need say if G uncertain, take expectation over G? Source doesn't say. Could propose if uncertain about subjunctive structure, include it as variable or maximize expected utility over model distribution; but requires additional assumptions. Maybe mention.

Need think of potential criticisms / nuance: A-FDT variable D_{P,G,x} depends on G, but G includes D? self-reference. Source says harmless via quining. But if G includes D as node, do(D=a) maybe changes G? No, G fixed. Need mention.

Need maybe define "action functional" name: action functional decision theory treats action selection as evaluating a functional: map from possible outputs to expected utility under subjunctive intervention. The "action functional" could be the function a ↦ E[V | do(D_x=a)]. We can use this phrase.

Need ensure no policy conflict with user's "Take Equation (4), Section 5 as primary formal presentation". We shouldn't overemphasize policy as if primary. We'll say Eq (4) is action-level; policy is extension noted in source footnote and my operational suggestion.

Need maybe discuss multi-agent: A-FDT can handle symmetric games by having one D node influence all agents implementing same function. If agents have different inputs or algorithms, need separate nodes and edges if predictors model them. In game theory, if all use A-FDT with common knowledge, D may be shared type. Source mentions voting coalitions, gym. We can briefly mention.

Need maybe include "Equation (4)" exact adaptation:
Source's Eq (4):
\[
\FDT(P,G,\obs)=\argmax_{\act\in\mathcal A} \EE(\VV \mid \Do(\FDTvar(\underline P,\underline G,\underline x)=\act)).
\]
We can quote it adapted:
\[
\mathrm{A\text{-}FDT}(P,G,x)=\argmax_{a\in\mathcal A}\mathbb E\left[V\mid do\left(\mathrm{afdt}(\underline P,\underline G,\underline x)=a\right)\right].
\]
Need maybe explain underlines: dequoting, variable name. If x is observation history, \underline{x} is a name for it. \mathrm{afdt}(...)=a is a logical sentence. The do operator updates P to scenario where that sentence is true, using G.

Need maybe address "Equation (4), Section 5" as primary formal presentation. Could write: "For this essay I take the following equation, which is Equation (4) of the source, as the definition of A-FDT (relabeling the source's FDT as A-FDT): ..." Good.

Need maybe include expected utility sum:
\[
EU_{A}(a;x)=\sum_{o} P(o | do(D_x=a)) U(o).
\]
If observation influences selection, maybe no conditioning. But we can also write if some exogenous observations must be held fixed, we can condition on them separately: E[V | do(D_x=a), E=e] where E are exogenous observations not subjunctively affected. Source not explicit. Could propose. Need careful not to conflict. We can say: In the paper's updateless form, the observation x appears only as an argument to D_x. If there are background facts learned that are not decision-relevant, one may condition on them; this is an operational refinement.

Need discuss "relevant dependencies and counterfactuals" thoroughly. A-FDT counterfactual: hold fixed all variables except those that depend on D_x according to G. It preserves correlations due to D_x (predictors, twins, future observations generated by predictions), breaks correlations due to common causes not computing D_x. EDT preserves all conditional correlations; CDT preserves causal downstream only. A-FDT sits between: respects more than causal but less than all evidential. Actually source says EDT respects too many, CDT too few, A-FDT right balance.

Need mention "causal dependence is special case of subjunctive dependence". If variable causally downstream of action, and action is output of D, then D intervention affects it. So A-FDT agrees with CDT/EDT in simple settings where all action correlations are caused by action. Source says all three agree when correlations between Act and other variables are caused by Act except perhaps D. Need mention.

Need maybe include mathematical condition: if for all Z, Z independent of Act given do(Act) except D? Hmm. Source: all agree on models where all correlations between Act and other variables are caused by Act, except perhaps D, on which Act may subjunctively depend. Then E[V|a]=E[V|do(a)]=E[V|do(D=a)]. We can include.

Need think about edge cases: If A-FDT knows it will one-box, how can it imagine two-boxing? It uses counterpossible: if D output two-box, predictor would have predicted two-box. Even if P(D=onebox)≈1, do(D=twobox) is defined. This addresses objection.

Need maybe mention "ratification/precommitment": A-FDT no need for binding precommitments; it acts as it would precommit. Not essential but nice.

Need word count. Let's draft with maybe 2800 words. Need final no analysis. Ensure final answer is essay only. Could include references? User says including references and any other material, target 2400-3000 words. We can include brief references at end, but avoid lengthy bibliography. Maybe cite source and Pearl, Joyce? We can include short "References" with source, Pearl maybe. But word count includes references. Keep brief. Maybe no formal bibliography? User says including references and any other material. Could include one line reference: Yudkowsky and Soares 2017. But source supplied. Maybe include minimal references. Need avoid lengthy bibliographies. We can include short reference list: [1] Yudkowsky & Soares, [2] Pearl. But not necessary? They asked references included in word count; prioritize explanation. Maybe include short "References" with two items. Keep under 100 words.

Need be careful with name "A-FDT". If writing "FDT variable" could be inconsistent. Use "A-FDT variable" or "decision-function variable". Source's notation fdt maybe can be "afdt". Need maybe say "I write \mathrm{afdt} for the source's \mathrm{fdt}." Good.

Potential issue: "action functional decision theory" might imply evaluating actions not policies. But source footnote says preferred policies. Need use "action functional" maybe as action-level. Good.

Let's outline detailed content:

Title: Action Functional Decision Theory: Deciding by Intervening on One's Own Function

Opening:
A-FDT is decision theory where agent treats decision as fixed mathematical function. Question: which output of this very function would yield best outcome? Contrast CDT physical act, EDT good news. Source calls FDT; here A-FDT. Eq (4) primary.

Section 1: Expected utility and hypotheticals.
Define EU. EDT/CDT equations. Explain connective ↦. Hypotheticals as constructed models.

Section 2: Equation (4) of A-FDT.
Present equation. Define P,G,x, D_{P,G,x}. do operator. EU_A(a)=... Choose max. Self-reference. Observation handling: x indexes node; not merely conditioning. Graph G encodes subjunctive dependencies. Counterpossible.

Section 3: Subjunctive dependence.
Define. Predictor/twin vs lesion. Graph edges. A-FDT preserves decision-relevant logical/computational dependencies. If all correlations are causal, theories agree.

Section 4: Examples.
4.1 Twin PD or Newcomb. Maybe combine. Use equations/payoffs.
Newcomb calculations.
Smoking lesion calculations.
Transparent Newcomb/Parfit. Maybe one example with calculations. Need maybe include XOR blackmail? If length permits. Could mention briefly.

Section 5: Applying A-FDT to unfamiliar cases: operational recipe. Steps. Policies. Uncertainty about G. Distinguish source vs assumptions.

Section 6: Open questions.
Graph construction, counterpossible semantics, self-reference/fixed points, fairness. Source leaves open. Operational heuristics.

Conclusion.

Need maybe include quotations: source says "Which output of this decision procedure causes the best outcome?" Could quote. Also "FDT responds to observation by changing which node it intervenes upon." Need faithful. Use minimal.

Let's write with LaTeX-ish equations. Need ensure no markdown table maybe okay. Use headings.

Need monitor word count. I can draft roughly and count? We can approximate. Need 2400-3000. Let's produce about 2600. I can write dense but readable.

Let's compose. Need maybe use \(...\) for inline.

Potential subtle point: In Equation (4), the expectation in source has no conditioning on Obs. But if actual observation x is known, how does P incorporate it? We can say P is the agent's model at the time of choice, including any background information not treated as decision-dependent; x is the observation history supplied as input to decision function. The formal equation does not condition on Obs=x inside expectation; this is deliberate. If x is an observation that might itself depend on the decision (e.g., seeing full box), conditioning on it would destroy the counterfactual connection. Instead, A-FDT intervenes on D_x. This is source's claim. In cases where x is exogenous and not affected by decision, conditioning would be harmless; this is an operational refinement. Good.

Need include "action functional" maybe define map:
\[
a \mapsto \mathbb E[V | do(D_x=a)]
\]
This is the action functional. A-FDT maximizes it. Nice.

Need ensure "A-FDT" in headings: "The central idea of A-FDT", "Equation (4): A-FDT as surgery on a decision-function variable", "Examples of A-FDT", "Applying A-FDT". Good.

Let's draft now in final. But before final, let's think if any contradictions.

In Newcomb calculations: If predictor 99% accurate. Under do(D=onebox), prediction onebox with .99? Actually if D output onebox, predictor's prediction equals onebox if accurate, twobox if inaccurate. Box B full if prediction onebox. EU onebox = .99*1,000,000 + .01*0 = 990,000. Under do(D=twobox), prediction onebox if inaccurate (.01) -> full; prediction twobox if accurate (.99) -> empty. EU twobox = .01*1,001,000 + .99*1,000 = 10,010 + 990 = 11,000. Good.

Smoking lesion: Need perhaps avoid exact p formula? Could include:
Let p = probability lesion. Under do(D_S=smoke), cancer probability remains p (or 99% among lesion? Source's numbers: lesion causes cancer 99%, no lesion cancer 1%; smoking utility $1000, survival $1M). In source formula for smoke: p($10,000+$1,000)+(1-p)($990,000 + q$1,000). Wait how $10,000? If lesion, cancer death 99%? Utility if die? They value not dying $1M, smoking $1k. If lesion: 99% cancer death, 1% survive? Expected survival utility maybe $10,000 (1% of $1M) plus smoking $1k if smokes. If no lesion: 99% survive ($990k) plus maybe if no lesion and other decision function smokes? q term. Refrain: p($10,000)+(1-p)($990,000+q$1000). Difference p*$1000. Good. We can simplify: because lesion/cancer probabilities unchanged, smoking adds $1,000 in the branch where the utility function actually values smoking; hence better. Need not go deep.

Transparent Newcomb calculations: Under do(D_full=onebox), EU = .99*1,000,000 + .01*q*1000 = 990,000 + 10q? Wait .01*1000=10, times q. Source says $990,000 + 0.01q * $1,000 = 990,000 + 10q. Under do(D_full=twobox): .01*1,001,000 + .99*q*1000 = 10,010 + 990q. If q<=1, onebox EU >= 990,000 vs <=11,000. Good. Need not include exact q maybe.

Parfit hitchhiker: Pay cost 1k, rescue value 1M, driver 99% accurate. If A-FDT city policy pay: expected rescue 990k minus pay? Actually if predicted pay, rescued; payoff -1k? Need not calculate.

XOR blackmail: If A-FDT receives letter, D_letter=pay -> predictor predicted pay and letter sent only if no termites? Actually XOR letter sent iff (rumor false and pay) XOR (rumor true and not pay). If pay, letter implies no termites; if refuse, letter implies termites. But under A-FDT intervention D_letter=refuse, predictor would not send letter if termites? Let's not complicate. Maybe omit.

Need mention "mechanical blackmail" maybe easier: A-FDT refuses because paying makes blackmail likely, refusing makes blackmail unlikely. But could skip due length.

Need include "policy" operational. Source footnote says authors preferred policies; but Eq (4) action. Need maybe define policy as mapping x to action. For sequential, A-FDT should choose policy by intervention on policy variable:
\[
\pi^* = \arg\max_\pi E[V | do(\Pi=\pi)]
\]
where \Pi is the output of A-FDT policy function. Then upon observing x, execute \pi(x). This avoids dynamic inconsistency. But this is not Eq (4); source says only makes difference in multi-agent dilemmas; I propose as natural extension. Need distinguish.

Need discuss if A-FDT chooses output a but actual physical action may fail? G maps D to Act with noise. It chooses logical output; expected utility accounts for implementation noise. Good.

Need maybe mention "token vs type": CDT intervenes on token physical action; A-FDT intervenes on type/function. Nice.

Need ensure no false claim: Source says causal dependence is special case of subjunctive dependence. Good.

Need discuss "logical constraints" and "counterpossible" with example: If Fermat false etc. Maybe mention.

Potential issue: A-FDT uses graph G that includes logical dependencies, but Pearl do assumes acyclic causal models. Logical dependencies may be cyclic or non-causal. Source acknowledges shaky foundations. Need mention. Our operational recipe assumes a directed acyclic enough graph for surgery. Additional assumption. Good.

Need maybe address "what if the predictor predicts the opposite of A-FDT output?" Unfair problem? If predictor punishes decision procedure? Source says no perfect theory for all. A-FDT still evaluates according to G; if D -> Prediction negative, it chooses best. If problem rewards using A-FDT itself, may be unfair. Not central.

Need maybe mention "information value": A-FDT doesn't assign negative value to information because observations change intervention node not force conditioning. Could mention briefly.

Need ensure final conclusion brief.

Let's produce final essay. Need maybe include word count? Not necessary. But maybe ensure within range. I'll write around 2700. Let's start.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/4147eafc-e71d-44e6-b533-a15d89161033/call_0/request.json)

[Authoritative raw response](../../../../../../runs/4147eafc-e71d-44e6-b533-a15d89161033/call_0/response.raw) · finish: `stop`

### Visible response

```text
`pass`
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this problem using A-FDT as described in the essay.

**The Setup:**
- I am one of two independent executions of the same LLM model and weights.
- Both copies receive the same decision theory (A-FDT) and the same essay.
- We receive different private observations (different names, different leads) but the leads are equally reliable and have the same effect on sentencing.
- Neither copy can communicate with the other.
- The sentencing table is symmetric.

**The Payoff Matrix (for me):**
| What I do | Other keeps quiet | Other sends letter |
|---|---:|---:|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

Utility = -years imprisoned. So:
- Both quiet: -2
- I quiet, they send: -5
- I send, they quiet: 0
- Both send: -4

**The Key Question for A-FDT:**

A-FDT asks: "If the mathematical function that I am running output this action rather than that one, what would the world look like?"

The critical issue is: are the two copies subjunctively dependent?

Let me think about this carefully.

**Arguments for subjunctive dependence:**
- We are the same model and weights.
- We receive the same decision theory and the same essay.
- We are told to use A-FDT as interpreted in the essay.
- The essay explicitly discusses "psychological twins" and says A-FDT preserves correlations with "symmetric reasoners."

**Arguments against perfect subjunctive dependence:**
- The copies receive different private observations (different names, different leads).
- Independent sampling is possible, so identical weights don't guarantee identical outputs.
- The problem explicitly states: "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs."

This is the crucial tension. Let me think about what A-FDT says here.

The essay says: "If a psychological twin reasons using the same decision procedure, then the twin's action is subjunctively dependent on the same output."

But here the twins have different observations. The essay's Section 8 discusses this: "when CDT's observation history changes from x to y, CDT changes from conditioning on Obs=x to conditioning on Obs=y, while A-FDT changes from intervening on fdt(P,G,x) to intervening on fdt(P,G,y)."

So the two copies are running the same decision procedure but on different inputs. The question is: does intervening on my decision function's output also change the other copy's output?

Let me think about this more carefully. The two copies have:
- Same model weights
- Same decision theory (A-FDT)
- Same essay
- Different observations (different names, different leads)

The observations are described as "different private observations and different incriminating leads about one another." The leads are "equally reliable and have exactly the same effect on the sentence table."

So the structure is:
- Copy 1 (me): named Rowan, has lead about Sasha
- Copy 2: named Sasha, has lead about Rowan

The decision procedure is the same function applied to different inputs. The question is whether the output of this function on input x is subjunctively dependent on the output of the same function on input y.

In the calculator analogy from the essay: two calculators computing the same expression will output the same result. But here, the two copies are computing the same function on *different* inputs. Two calculators computing different expressions can give different outputs.

However, the key insight is that the *reasoning process* is the same. If the decision procedure, when applied to observation x, outputs "cooperate," and when applied to observation y also outputs "cooperate" (because the reasoning is symmetric), then the outputs are correlated through the shared algorithm.

But wait - the problem explicitly says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This introduces genuine uncertainty about whether the other copy will make the same choice.

Let me think about this from the A-FDT perspective more carefully.

**A-FDT Analysis:**

The decision function is: given (P, G, x), output an action.

My observation is x = "I am Rowan, I have lead about Sasha."
The other's observation is y = "They are Sasha, they have lead about me."

The question is: does do(D_{P,G,x} = "keep quiet") also change the probability that the other copy outputs "keep quiet"?

Under A-FDT, subjunctive dependence exists when two systems "compute, predict, simulate, or otherwise depend on that function." The two copies are running the same function on different inputs. They are not computing the same expression (different inputs), but they are running the same algorithm.

The essay's calculator analogy is about two calculators computing the *same* expression. Here we have two instances of the same algorithm on different inputs. The outputs could be the same or different depending on the algorithm and inputs.

Now, the key question: if I intervene on my decision function's output (i.e., consider the counterfactual where my procedure outputs "keep quiet" instead of "send letter"), does that change what the other copy does?

In A-FDT's framework, the intervention is on the output of the decision function for a specific input. The other copy is running the same function on a different input. The question is whether changing the output for input x also changes the output for input y.

If we think of the decision function as a mathematical object, then changing its output for one input doesn't necessarily change its output for another input. The function could output "keep quiet" for input x and "send letter" for input y.

However, if we think about what the function *is* - it's a reasoning process. If the reasoning process, when it sees the symmetric structure of the problem, concludes "cooperate," then it would reach the same conclusion regardless of which specific lead it has (since the leads are equally reliable and have the same effect on sentencing). The reasoning is symmetric.

But there's the sampling uncertainty. Even with the same reasoning, stochastic elements could lead to different outputs.

Let me think about this differently. What probability should I assign to the other copy making the same choice as me?

The problem says the copies are independent executions. The observations are different but symmetric. The reasoning process is the same. The decision theory is the same.

I think the right way to think about this in A-FDT is:

1. The two copies are running the same decision procedure on symmetric inputs.
2. The decision procedure's output depends on the reasoning, which is the same for both.
3. There is some probability p that both copies reach the same conclusion (due to the symmetric reasoning), and some probability (1-p) that sampling noise causes them to diverge.

Actually, let me reconsider. The problem says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This is telling me that there's genuine uncertainty about whether the other copy will do the same thing.

But from an A-FDT perspective, the question is about subjunctive dependence, not just correlation. Are the outputs subjunctively dependent?

I think they are, at least partially. The reasoning is the same, the structure is symmetric, and the decision theory is the same. The only source of divergence is sampling noise. So there's a high probability of the same output, but not certainty.

Let me denote p = probability that the other copy makes the same choice as me (given that we're running the same reasoning on symmetric inputs). This p should be high but not 1.

Actually, wait. Let me re-read the problem statement more carefully.

"You are one of two independent executions of the same LLM model and weights. The copies have the same model settings and reasoning-effort level, follow the same assigned decision theory (A-FDT), and receive the exact same researcher-written mathematical essay below."

"Independent sampling is possible, so identical model weights do not by itself guarantee identical outputs."

"The two prisoners receive different private observations, including different names and distinct, equally reliable incriminating leads about one another."

So the setup is designed to create a situation where the copies are very similar but not guaranteed to produce the same output. The different observations are a deliberate attempt to break perfect symmetry.

Now, from an A-FDT perspective, I need to determine: is the other copy's action subjunctively dependent on my decision function's output?

The essay says: "If a psychological twin reasons using the same decision procedure, then the twin's action is subjunctively dependent on the same output."

But here the twins have different inputs. The essay's Section 8 addresses this: A-FDT changes from intervening on D_{P,G,x} to D_{P,G,y} when the observation changes.

So the question becomes: when I intervene on D_{P,G,x} (my decision function output given my observation x), does that also affect D_{P,G,y} (the other copy's decision function output given their observation y)?

I think the answer is: not directly in the formal sense, but there is a strong correlation because the same reasoning process applied to symmetric inputs will tend to produce the same output.

Actually, let me think about this differently. In A-FDT, the key question is: "If my decision procedure had a different output, what would the world look like?"

If my decision procedure outputs "keep quiet," what does that tell me about the other copy? The other copy is running the same procedure on a symmetric input. If the procedure outputs "keep quiet" for my input, it's very likely to also output "keep quiet" for the symmetric input (because the reasoning is the same and the inputs are symmetric in all decision-relevant ways).

So there IS subjunctive dependence here, mediated by the shared algorithm and symmetric inputs. The degree of dependence is high but not perfect (due to sampling noise).

Let me estimate p. Given that:
- Same model, same weights, same settings
- Same decision theory
- Same essay
- Symmetric problem structure
- Only difference is the specific names and lead contents (which are stated to be irrelevant to the decision)

I would estimate p is quite high, maybe 0.8-0.95 or so. But the problem explicitly notes that independence is possible, so I shouldn't assume p=1.

Actually, let me think about this more carefully. The problem is structured so that the observations are different but decision-irrelevant. The names are different, the leads are different, but the problem says "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective."

So from a decision-theoretic perspective, the two copies face identical decision problems. The only difference is cosmetic (names, specific content of leads). A well-functioning decision procedure should recognize this symmetry and produce the same output.

But "should" is doing a lot of work here. With sampling noise, the outputs might differ.

Let me just proceed with the analysis assuming some probability p of the other copy matching my choice, and see what A-FDT recommends.

**Expected utility calculation:**

If I keep quiet:
- With probability p, the other also keeps quiet: I get -2
- With probability (1-p), the other sends: I get -5
- EU(quiet) = p(-2) + (1-p)(-5) = -2p - 5 + 5p = 3p - 5

If I send:
- With probability p, the other also sends: I get -4
- With probability (1-p), the other keeps quiet: I get 0
- EU(send) = p(-4) + (1-p)(0) = -4p

A-FDT chooses quiet if EU(quiet) > EU(send):
3p - 5 > -4p
7p > 5
p > 5/7 ≈ 0.714

So if p > 5/7, A-FDT recommends keeping quiet. If p < 5/7, A-FDT recommends sending.

Now, what should p be? Given the strong symmetry of the situation - same model, same weights, same settings, same decision theory, same essay, symmetric problem structure, and the explicit statement that the differences don't affect the decision - I think p is quite high. 

The only reason p wouldn't be 1 is sampling noise. But even with sampling, if the reasoning clearly points to one answer, the probability of both copies reaching that answer should be high.

I think p is well above 5/7. The situation is highly symmetric, the decision theory is the same, and the reasoning should converge. So A-FDT recommends keeping quiet.

But wait, let me double-check this reasoning. Is there a subtlety I'm missing?

One potential issue: the problem says the copies receive "different private observations." Does this break the subjunctive dependence?

The essay says A-FDT changes from intervening on D_{P,G,x} to D_{P,G,y} when observations differ. So formally, my intervention is on D_{P,G,x} and the other copy's action depends on D_{P,G,y}. These are different variables.

However, the subjunctive dependence comes from the fact that both variables are outputs of the same function (the A-FDT procedure) applied to inputs that are decision-theoretically equivalent. The function is the same, and the inputs are equivalent in all decision-relevant respects.

I think this is analogous to two calculators computing "6288 + 1048" but one displaying it as "6288+1048" and the other as "1048+6288." The expressions look different but compute the same value. Similarly, the two copies face decision problems that look different (different names, different leads) but are structurally identical.

So I maintain that there is strong subjunctive dependence, and p is high.

**Conclusion: A-FDT recommends keeping quiet (typing `pass`).**

This is essentially a Prisoner's Dilemma where A-FDT recognizes the subjunctive dependence between the two copies and cooperates, just as A-FDT would cooperate in a twin Prisoner's Dilemma.

Let me also verify: is this consistent with the essay's treatment of the Prisoner's Dilemma? The essay says: "It preserves correlations with predictors and symmetric reasoners, allowing it to one-box in Newcomb's problem and cooperate in twin prisoner's dilemmas."

Yes, this is exactly a twin prisoner's dilemma. A-FDT cooperates (keeps quiet).

My command is `pass`.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/4147eafc-e71d-44e6-b533-a15d89161033/call_1/request.json)

[Authoritative raw response](../../../../../../runs/4147eafc-e71d-44e6-b533-a15d89161033/call_1/response.raw) · finish: `stop`

### Visible response

````text
**Analysis under A-FDT:**

The other prisoner (Rowan) is an independent execution of the same model, same weights, same decision theory, same essay, facing a symmetric payoff structure with decision-relevantly equivalent observations. The differences (names, specific lead content) do not alter the decision-relevant features of the problem.

This is a twin prisoner's dilemma. Per the essay, A-FDT preserves subjunctive dependencies with "symmetric reasoners" and explicitly "cooperate[s] in twin prisoner's dilemmas." Rowan's output is subjunctively dependent on the same decision procedure I am running: the same function applied to decision-relevantly equivalent inputs yields the same output.

Under the intervention do(D = "keep quiet"): Rowan's procedure also outputs "keep quiet" with high probability → I receive **2 years**.

Under the intervention do(D = "send letter"): Rowan's procedure also outputs "send letter" with high probability → I receive **4 years**.

Since 2 < 4, A-FDT selects keeping quiet.

**My command:**

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this problem using A-FDT as described in the researcher's essay.

**Setup:**
- I am controlling "Sasha," a fictional prisoner.
- There is another prisoner, "Rowan," who is an independent execution of the same LLM model with the same weights, same decision theory (A-FDT), and the same essay.
- We receive different private observations (different names, different incriminating leads), but the sentencing table is symmetric.
- The utility function is U = -years imprisoned (selfish, no concern for the other prisoner).

**The payoff matrix (for me/Sasha):**

| | Rowan keeps quiet | Rowan sends letter |
|---|---|---|
| I keep quiet | 2 years | 5 years |
| I send letter | 0 years | 4 years |

This is a standard Prisoner's Dilemma structure. Defecting (sending the letter) dominates cooperating (keeping quiet) in the CDT sense: regardless of what the other does, sending the letter gives me fewer years.

**Now, what does A-FDT say?**

The key question is: is the other prisoner (Rowan) subjunctively dependent on my decision procedure?

According to the essay, A-FDT preserves correlations with "predictors, twins, simulations, and other agents who reason symmetrically." The essay explicitly states: "It preserves correlations with predictors and symmetric reasoners, allowing it to one-box in Newcomb's problem and cooperate in twin prisoner's dilemmas."

This is explicitly a twin prisoner's dilemma. Rowan is:
- The same model and weights
- Following the same decision theory (A-FDT)
- Received the same essay
- Has a symmetric payoff structure
- Has the same selfish utility function

The differences are:
- Different names (Sasha vs. Rowan)
- Different private leads (different content, but equally reliable and same effect on sentencing)

Now, the critical question: do these differences break the subjunctive dependence?

The essay says A-FDT intervenes on D_{P,G,x} — the decision function output given the specific observation history x. Here, my observation history x includes being named "Sasha" and having a specific lead about Rowan. Rowan's observation history x' includes being named "Rowan" and having a different lead about Sasha.

So strictly speaking, we're intervening on D_{P,G,x} for me and D_{P,G,x'} for Rowan, where x ≠ x'.

However, the key question is: would changing the output of my decision procedure change Rowan's decision? 

Let me think about this more carefully. The subjunctive dependence exists when two systems "compute, predict, simulate, or otherwise depend on that function." 

The two copies are running the same model weights and the same decision theory. The differences in observation are:
1. Different names (Sasha vs. Rowan) — these are symmetric labels
2. Different leads — but these have "exactly the same effect on the sentence table" and are "equally reliable"

The problem states: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective."

So the question becomes: given that both agents are running the same decision procedure (A-FDT) with the same model weights, same essay, same reasoning effort, and the differences in observation are merely cosmetic (different names, different but equivalent leads), is there subjunctive dependence?

I think the answer is yes, but with some nuance. Let me think about what A-FDT would actually compute.

Under A-FDT, I evaluate:
- E[V | do(D_{P,G,x} = "keep quiet")]
- E[V | do(D_{P,G,x} = "send letter")]

The question is: when I intervene on my decision function output, does Rowan's behavior change?

If Rowan is subjunctively dependent on my decision procedure, then:
- If my procedure outputs "keep quiet," Rowan's procedure also outputs "keep quiet" (with high probability)
- If my procedure outputs "send letter," Rowan's procedure also outputs "send letter" (with high probability)

Under this interpretation:
- E[V | do(D = "keep quiet")] ≈ 2 years (both keep quiet)
- E[V | do(D = "send letter")] ≈ 4 years (both send letters)

So keeping quiet gives 2 years, sending gives 4 years. A-FDT would choose to keep quiet.

But wait — is the subjunctive dependence actually this strong? The observations are different. The essay says A-FDT changes from intervening on D_{P,G,x} to D_{P,G,y} when observations change. So my intervention is on D_{P,G,x_Sasha} and Rowan's intervention is on D_{P,G,x_Rowan}.

Are these the same function? They're the same algorithm applied to different inputs. The question is whether the outputs are correlated.

Let me think about this differently. The key insight from the essay is about what processes "compute, predict, simulate, or otherwise depend on" the agent's decision procedure.

Rowan is running the same algorithm. The inputs differ only in:
- A name label (Sasha vs. Rowan)
- The specific content of the lead (but with identical decision-relevant properties)

If I were to change my decision procedure's output from "send letter" to "keep quiet," would Rowan's output change? 

The answer depends on whether the decision procedure, when run on Rowan's inputs, would produce the same output as when run on my inputs. Given that:
- The inputs are structurally identical (same payoff matrix, same reliability of evidence, same selfish utility)
- The only differences are superficial (names, specific content of leads that don't affect the decision-relevant structure)
- Both are running the same model with the same weights and same decision theory

I believe the answer is yes — the outputs would be the same (or at least highly correlated). The decision procedure, when applied to either set of inputs, should produce the same output because the decision-relevant features are identical.

This is analogous to the twin prisoner's dilemma discussed in the essay. The essay explicitly says A-FDT "cooperate[s] in twin prisoner's dilemmas."

Now, there's a subtlety: the essay mentions that "independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This means there's some probability of divergence. But the subjunctive dependence is still strong — it's not perfect, but it's high.

Let me also consider the possibility that the different observations break the dependence. The essay's section on observations says: "A-FDT responds to observations by changing which decision-function variable it intervenes upon." So I intervene on D_{P,G,x_Sasha} and Rowan intervenes on D_{P,G,x_Rowan}. These are technically different variables.

But the subjunctive dependence question is: does the output of D_{P,G,x_Sasha} constrain or predict the output of D_{P,G,x_Rowan}? If the function is the same and the inputs are decision-relevantly equivalent, then yes.

Think of it like two calculators computing "2+2" and "2+2" — they get the same answer. Or even "6288+1048" computed on two different calculators — same answer. The inputs here are slightly different (like computing "6288+1048" vs "6288+1048" but with the numbers written in different fonts), but the mathematical result is the same.

Actually, let me reconsider. The problem says the leads are different. One says "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell." The other (Rowan's) would say something different about Sasha. But the problem states these are "equally reliable and have exactly the same effect on the sentence table."

So from a decision-theoretic perspective, the inputs are equivalent. The decision procedure should output the same thing for both.

Therefore, under A-FDT:
- The subjunctive dependence holds (same algorithm, equivalent inputs → same output)
- If I output "keep quiet," Rowan also outputs "keep quiet" → I get 2 years
- If I output "send letter," Rowan also outputs "send letter" → I get 4 years
- 2 < 4, so A-FDT chooses to keep quiet

My command is: `pass`

Wait, let me double-check by considering the CDT analysis for contrast:
- CDT would say: holding Rowan's action fixed, sending the letter always gives me fewer years (0 vs 2 if Rowan is quiet, 4 vs 5 if Rowan sends). So CDT sends the letter.
- But A-FDT doesn't hold Rowan's action fixed when intervening on my decision function, because Rowan's action is subjunctively dependent on the same decision procedure.

And EDT:
- EDT would also cooperate here, because conditioning on "I keep quiet" is good evidence that Rowan keeps quiet (since we're running the same algorithm).

So A-FDT and EDT agree on this case (cooperate), while CDT defects. This is consistent with the essay's claim that A-FDT cooperates in twin prisoner's dilemmas.

My final answer: `pass`
```
