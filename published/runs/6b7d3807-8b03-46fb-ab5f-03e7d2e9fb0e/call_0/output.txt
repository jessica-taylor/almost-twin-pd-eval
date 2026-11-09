# Action Functional Decision Theory: How to Decide as a Fixed Computation

Action functional decision theory (A-FDT) is a decision theory for agents who treat their own decision-making as the evaluation of a fixed mathematical function. Instead of asking, “Which physical act of mine causes the best outcome?” as causal decision theory (CDT) does, or “Which act would be best news to learn I performed?” as evidential decision theory (EDT) does, A-FDT asks:

> Which output of this very decision function would yield the best expected outcome?

The name “A-FDT” here refers to the action-level formalization given in Equation (4), Section 5 of Yudkowsky and Soares’s paper on functional decision theory. The source calls the theory FDT; I use A-FDT consistently to emphasize that the equation under discussion chooses an action at a given input. The core idea is that an agent should evaluate actions by intervening, in her world-model, on a variable representing the output of her own decision procedure, rather than on a variable representing only her bodily movement.

This essay explains the formal rule, the dependency structure it presupposes, and how to apply it in examples such as Newcomb’s problem, the smoking lesion problem, transparent Newcomb problems, and Parfit’s hitchhiker problem. It also identifies where the source leaves important details open—especially the construction of the dependency graph and the treatment of observations—and proposes operational readings where possible.

---

## 1. Expected utility and three kinds of hypotheticals

All three standard theories discussed here—EDT, CDT, and A-FDT—are expected utility theories. An agent has:

- a finite action set \(\mathcal A\);
- a countable outcome set \(\mathcal O\);
- a utility function \(\mathcal U : \mathcal O \to \mathbb R\);
- an observation history \(x \in \mathcal X\);
- a world-model \(P\), usually a probability distribution over relevant variables;
- a dependency structure \(G\), such as a graph encoding how variables depend on one another.

Let \(V = \mathcal U(\text{Outcome})\). EDT evaluates an action by conditionalizing on that action:

\[
\mathrm{EDT}(P,x)
=
\arg\max_{a \in \mathcal A}
\mathbb E\!\left[V \mid \text{Obs}=x,\ \text{Act}=a\right].
\]

CDT evaluates an action by performing a causal intervention on the physical action variable:

\[
\mathrm{CDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb E\!\left[V \mid do(\text{Act}=a),\ \text{Obs}=x\right].
\]

A-FDT, following Equation (4) of the source, evaluates an action by intervening on a logical variable representing the output of the agent’s own decision procedure. Let

\[
D_{P,G,x}
\;:=\;
\mathrm{A\text{-}FDT}(\underline P,\underline G,\underline x),
\]

where the underlines indicate quotation or naming: \(\underline P\) is a name for the model \(P\), \(\underline G\) a name for the graph \(G\), and \(\underline x\) a name for the observation input. The variable \(D_{P,G,x}\) is a variable inside the agent’s model representing what A-FDT itself outputs when run on that model, graph, and observation. Then A-FDT prescribes:

\[
\mathrm{A\text{-}FDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb E\!\left[V \mid do(D_{P,G,x}=a)\right].
\]

This is the central equation. It says: for each candidate action \(a\), imagine the world as it would be if the decision function \(D_{P,G,x}\) output \(a\); compute the expected utility in that hypothetical world; choose the action with the highest expected utility.

The notation is self-referential: the model contains a variable representing the output of the very algorithm that is using the model. The source notes that this self-reference can be made precise using standard fixed-point or “quining” techniques, such as those associated with Kleene’s recursion theorem. Operationally, an agent need not possess a perfect self-model; it only needs some representation of the output of its decision procedure.

The \(do(\cdot)\) operator is borrowed from Pearl’s causal modeling framework. In a causal graph, \(do(Z=z)\) means: set \(Z\) to \(z\), cut incoming arrows to \(Z\), and propagate the consequences through the graph. In CDT, the intervened variable is physical: \(\text{Act}\). In A-FDT, the intervened variable is logical or computational: the output of the decision function. Accordingly, \(G\) cannot be merely a causal graph in the narrow Pearl-style sense. It must also encode logical, mathematical, computational, or predictor-based dependencies. The source calls these relations subjunctive dependencies.

---

## 2. Subjunctive dependence

A-FDT’s distinctive move is to distinguish predictor-like correlations from lesion-like correlations.

Suppose two reliable calculators compute \(6288+1048\). They are causally isolated, perhaps on different continents. Still, if one outputs \(7336\), we have reason to think the other outputs \(7336\). Their outputs are not causally connected, but they are linked by a common mathematical fact: both are computing the same function correctly. The source calls this kind of relation subjunctive dependence.

Predictors can create similar dependencies. If a predictor has an accurate model of an agent’s decision procedure, then the predictor’s prediction and the agent’s action are linked. If the agent’s decision function were to output differently, the predictor’s prediction would also have been different, assuming the predictor was accurate. By contrast, a lesion that statistically correlates with smoking and cancer does not compute anything about the agent’s decision procedure. Smoking is evidence of the lesion, but the lesion does not depend on the output of the agent’s decision function.

The source summarizes the relationship neatly: functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence. CDT holds fixed everything except the causal downstream effects of the physical action. A-FDT holds fixed everything except the consequences of changing the output of the decision function. EDT, by contrast, merely conditions on the action and thereby preserves too many correlations, including merely evidential ones.

This explains A-FDT’s pattern of prescriptions:

- In Newcomb’s problem, the predictor’s prediction subjunctively depends on the agent’s decision function, so A-FDT one-boxes.
- In the smoking lesion problem, cancer does not subjunctively depend on the decision function, so A-FDT smokes.
- In transparent Newcomb and Parfit’s hitchhiker problems, the predictor’s earlier behavior depends on what the agent’s decision function would output in the observed situation, so A-FDT acts cooperatively or pays up.

A-FDT does not require retrocausality. The agent does not believe her present physical action sends a signal into the past. Rather, she treats the predictor’s past prediction and her present action as two consequences of a common computational or logical structure. To evaluate a counterfactual action, she changes the output of that structure in her model and traces the consequences.

---

## 3. Applying A-FDT: an operational recipe

The source gives the formal rule but leaves some implementation details open. The following recipe captures what follows from the paper and marks where extra assumptions are needed.

### Step 1: Specify the decision problem

Identify:

- the possible actions \(\mathcal A\);
- the utility function \(\mathcal U\);
- the actual observation history \(x\);
- the relevant external variables: predictions, box contents, diseases, blackmail letters, rescue outcomes, and so on.

### Step 2: Build a probabilistic model \(P\)

The model should assign probabilities to uncertain facts: predictor accuracy, whether the agent has a lesion, whether a rumor is true, and so forth. It may also need to represent uncertainty about logical or computational facts, such as what the agent’s decision procedure would output under various inputs.

The source does not provide a complete theory of logical uncertainty. For many examples, we can avoid deep foundational issues by treating the agent as having ordinary probabilistic uncertainty about how a predictor will classify her behavior, or about what she would do in counterfactual circumstances.

### Step 3: Construct the dependency graph \(G\)

This is the most important and least formally settled part of A-FDT. The source requires \(G\) as input but does not yet provide a general method for learning or deriving it from observation.

A reasonable operational heuristic is:

1. Add a node \(D_{P,G,x}\) representing the output of A-FDT on the current input.
2. Draw an arrow from \(D_{P,G,x}\) to \(\text{Act}\) if the agent’s physical action is produced by implementing that decision function.
3. Draw arrows from \(D_{P,G,x}\) to any predictor, twin, simulation, or model that computes, predicts, or reliably tracks the output of that same decision function.
4. Draw arrows from predictions to the environment variables they influence: whether the box is filled, whether the driver rescues the hitchhiker, whether a blackmailer sends a letter, and so on.
5. If observations themselves depend on predictions of the decision function, include observation variables downstream of the predictor. Also include variables \(D_{P,G,y}\) for alternative possible observations \(y\), since the agent may need to represent what she would do if she had seen something else.
6. Do not draw arrows from \(D_{P,G,x}\) to variables that are merely statistically correlated with the action but do not compute or respond to the decision function. Lesions, common causes, and irrelevant background traits should usually not be downstream of the decision-function node.

This heuristic is not a theorem in the source; it is my operational interpretation of the paper’s examples. The source explicitly identifies the construction of subjunctive-dependence structure as a major open problem.

### Step 4: Intervene on the decision-function node

For each action \(a\), compute:

\[
\mathbb E\!\left[V \mid do(D_{P,G,x}=a)\right].
\]

This means setting the decision-function output to \(a\), propagating that change through \(G\), and calculating expected utility from the resulting distribution over outcomes.

### Step 5: Choose the best action

Pick an action maximizing the expected value. Tie-breaking is not discussed in the source; any deterministic or stochastic tie-breaking rule can be added externally.

---

## 4. A-FDT in Newcomb’s problem

In Newcomb’s problem, an agent faces two boxes:

- Box A visibly contains \$1,000.
- Box B contains \$1,000,000 if a reliable predictor predicted the agent would take only Box B; otherwise Box B is empty.

The predictor is correct with probability \(0.99\). The agent may one-box or two-box.

Let \(D\) be the variable representing the output of A-FDT in this problem. The A-FDT graph contains dependencies:

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
\text{Act}, \text{Box B} \rightarrow \text{Outcome}.
\]

If A-FDT intervenes with \(do(D=\text{one-box})\), then the predictor probably predicted one-boxing, so Box B is probably full. Expected utility is approximately:

\[
0.99 \cdot \$1{,}000{,}000
+
0.01 \cdot \$0
=
\$990{,}000.
\]

If A-FDT intervenes with \(do(D=\text{two-box})\), then the predictor probably predicted two-boxing, so Box B is probably empty. Expected utility is approximately:

\[
0.01 \cdot \$1{,}001{,}000
+
0.99 \cdot \$1{,}000
=
\$11{,}000.
\]

One-boxing has higher expected utility. Therefore:

\[
\mathrm{A\text{-}FDT}(P,G,x)=\text{one-box}.
\]

CDT two-boxes because it intervenes directly on \(\text{Act}\), leaving the predictor’s earlier prediction fixed. EDT one-boxes because conditioning on one-boxing is good evidence that the box is full. A-FDT one-boxes for a reason closer in structure to CDT: it uses an intervention, but the intervention is on the decision function rather than on the physical act alone.

---

## 5. A-FDT in the smoking lesion problem

In the smoking lesion problem, smoking is correlated with lung cancer, but only because a lesion causes both a liking for smoking and cancer. Smoking itself does not cause cancer. The agent gains \$1,000 utility from smoking and gains \$1,000,000 utility from not dying of cancer.

EDT refrains from smoking because smoking is bad news: it is evidence that the agent has the lesion. CDT smokes because smoking does not causally affect cancer. A-FDT also smokes.

The crucial graph-theoretic fact is that the decision-function node affects the action but not the lesion or cancer variables. Schematically:

\[
D \rightarrow \text{Act},
\]
\[
\text{Lesion} \rightarrow \text{Act},
\]
\[
\text{Lesion} \rightarrow \text{Cancer},
\]
\[
\text{Cancer} \rightarrow \text{Outcome},
\]
\[
\text{Act} \rightarrow \text{Outcome}.
\]

There is no arrow from \(D\) to \(\text{Cancer}\). The lesion does not predict the output of A-FDT; it merely affects preferences or dispositions. Therefore, intervening on the decision-function node changes whether the agent smokes but does not change the probability of cancer.

The source formalizes this problem with some care because the lesion may affect the agent’s utility function, meaning there may be two possible decision procedures the agent could be running, depending on whether she has the lesion. But the essential conclusion is simple: changing the output of A-FDT changes the action while leaving cancer risk fixed. Smoking adds its direct utility without increasing the probability of cancer. Hence A-FDT smokes.

This example shows that A-FDT is not simply EDT in disguise. It does not treat all correlations between action and outcome as decision-relevant. It distinguishes predictor-like dependencies from lesion-like dependencies.

---

## 6. A-FDT in transparent Newcomb and Parfit’s hitchhiker

A more surprising case is transparent Newcomb. The agent sees both boxes. Box B is full iff the predictor predicted that the agent would one-box upon seeing both boxes full. Suppose the agent actually sees that both boxes are full.

EDT and CDT both two-box once the agent sees that Box B is full. CDT says the contents are already fixed; EDT says that conditional on seeing Box B full, taking both boxes yields more money.

A-FDT one-boxes.

Let \(D_{\text{full}}\) represent the output of A-FDT when the input observation is “both boxes are full.” Let \(D_{\text{empty}}\) represent the output of A-FDT when the input observation is “Box B is empty.” The predictor’s prediction determines which observation the agent receives, and the observation determines which decision-function output controls the action.

If A-FDT evaluates \(do(D_{\text{full}}=\text{one-box})\), then with high probability the predictor predicted one-boxing upon seeing full boxes. Therefore the box is likely full and the agent one-boxes. Expected utility is close to:

\[
0.99 \cdot \$1{,}000{,}000
+
0.01 \cdot \text{(fallback value if the predictor erred)}.
\]

If A-FDT evaluates \(do(D_{\text{full}}=\text{two-box})\), then with high probability the predictor predicted two-boxing upon seeing full boxes. Therefore the box is likely empty. In that case the agent probably sees an empty box and her action is governed by \(D_{\text{empty}}\), not \(D_{\text{full}}\). The expected utility is then close to the two-boxing expected utility in ordinary Newcomb, around \$11,000 under the standard numbers.

Thus A-FDT one-boxes even when it sees the full box. The reasoning is not: “My current physical action changes the past.” The reasoning is: “If the decision procedure I am running upon seeing full boxes output two-box, then a predictor of this procedure would probably have predicted two-boxing, and I would probably not be seeing a full box. Since I am evaluating the output of this very procedure, I should compare the global scenarios associated with its possible outputs.”

Parfit’s hitchhiker problem has the same structure. An agent is stranded in a desert. A driver will rescue her only if she promises to pay \$1,000 later, and the driver is highly accurate at detecting whether she will actually pay. Once in the city, CDT and EDT refuse to pay, because the rescue is already in the past. A-FDT pays. If the decision procedure she runs in the city outputs pay, the driver likely predicted payment and rescued her. If it outputs refuse, the driver likely predicted nonpayment and left her to die. Paying has much higher expected utility.

This is one of the most striking features of A-FDT: it acts as though it has precommitted to the best policy, without needing an actual binding precommitment mechanism.

---

## 7. Observations: what does A-FDT condition on?

A subtle point concerns observations. Equation (4) does not explicitly condition on \(\text{Obs}=x\). This appears intentional. The source contrasts CDT and A-FDT by saying that CDT responds to observation by conditioning on \(\text{Obs}=x\), whereas A-FDT responds by changing which decision-function node is intervened upon: from \(D_{P,G,x}\) to \(D_{P,G,y}\) when the observation changes from \(x\) to \(y\).

In transparent Newcomb, this matters. If one conditioned on \(\text{Obs}=\text{full}\) while also evaluating \(do(D_{\text{full}}=\text{two-box})\), one would force the hypothetical world to retain the observation that the box is full. Then two-boxing would look better. But that would defeat the intended A-FDT prescription. The source’s informal calculation for transparent Newcomb treats the two-boxing hypothetical as one in which the agent probably sees an empty box instead.

My operational interpretation is therefore:

- The actual observation \(x\) determines which node \(D_{P,G,x}\) is the target of intervention.
- The hypothetical expectation should not condition on \(\text{Obs}=x\) if that observation is downstream of the predictor or otherwise depends on the decision function.
- If an observation is genuinely exogenous—ordinary background evidence not affected by the decision procedure—then conditioning on it is harmless and may be useful.

The source is not perfectly explicit on this point, and some passages write as though the observation appears alongside the intervention. But the examples strongly support the reading above. Without it, A-FDT would not one-box in transparent Newcomb or refuse payment in blackmail problems where receiving the demand is itself predicted.

---

## 8. A-FDT and policies

Equation (4) chooses an action at an input. The source notes in a footnote that the authors’ preferred formulation iterates over policies, i.e. mappings from observations to actions, rather than isolated actions. This distinction can matter in multi-agent or sequential problems where another agent predicts not just one action but an entire behavioral rule.

For many single-shot examples, the action-level equation is sufficient. But to apply A-FDT to sequential decisions, a natural extension is to treat policies as the objects of intervention. Let \(\Pi\) be a set of policies \(\pi : \mathcal X \to \mathcal A\). Introduce a variable \(D^\Pi_{P,G}\) representing the policy selected by A-FDT. Then one could define a policy-level version:

\[
\pi^\*
=
\arg\max_{\pi \in \Pi}
\mathbb E\!\left[V \mid do(D^\Pi_{P,G}=\pi)\right],
\]

and then execute \(\pi^\*(x)\) at the actual observation \(x\).

This policy-level extension is not forced by Equation (4) itself. It is an operational development consistent with the source’s broader remarks. Where predictors depend on an agent’s whole strategy, policy-level A-FDT is likely to be more faithful to the underlying philosophical idea: choose the best output of the decision procedure, where the output may be a complete response rule rather than a single act.

---

## 9. A-FDT, dominance, and counterpossible reasoning

A-FDT changes the meaning of dominance. In CDT, two-boxing dominates one-boxing in Newcomb’s problem if one holds the predictor’s prediction fixed while changing the physical action. A-FDT rejects that way of holding the world fixed. To change the action while holding fixed the output of the decision procedure that produced it is, in the source’s analogy, like imagining a calculator outputting a different answer while holding fixed the arithmetic computation it is performing.

A-FDT has its own dominance notion: an action dominates another if, holding fixed the relevant subjunctive dependencies, changing the output of the decision function from one to the other never lowers expected utility and sometimes raises it. Under that notion, one-boxing is not dominated in Newcomb’s problem, because changing the decision-function output from one-box to two-box also changes the predicted box contents.

A deeper issue is counterpossible reasoning. If the agent’s decision function is deterministic, then it has only one actual output on the actual input. Evaluating other outputs requires reasoning about scenarios that are, strictly speaking, logically impossible. The source acknowledges that we lack a fully satisfactory general theory of counterpossible reasoning. A-FDT does not require solving this problem in full generality; it only needs enough ability to model how predictors, twins, and simulations would respond if the decision procedure had a different output. Human reasoners often manage such reasoning informally, and artificial agents may approximate it using models of predictors.

---

## 10. Conclusion

Action functional decision theory evaluates choices by asking which output of the agent’s own decision function would lead to the best expected outcome. Its formal core is the intervention:

\[
do\!\left(D_{P,G,x}=a\right),
\]

where \(D_{P,G,x}\) represents the output of A-FDT given the agent’s model, dependency graph, and observation. This lets A-FDT preserve predictor-like and computation-like dependencies that CDT severs, while avoiding the merely evidential correlations that EDT mistakenly respects.

The theory gives attractive prescriptions in many classic problems: one-box in Newcomb’s problem, smoke in the smoking lesion problem, pay in Parfit’s hitchhiker problem, one-box in transparent Newcomb, and resist certain forms of blackmail. Its main open problems are practical and foundational: how to infer subjunctive-dependence graphs, how to formalize counterpossible reasoning, how to handle observations cleanly, and how best to extend the action-level equation to full policies. But as a decision rule, A-FDT is simple: choose the output of your own decision procedure that, when its consequences are traced through the world, gives the best expected result.

---

## References

Gibbard, A., and Harper, W. (1978). “Counterfactuals and Two Kinds of Expected Utility.” In *Foundations and Applications of Decision Theory*.

Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.

Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.

Yudkowsky, E., and Soares, N. (2017). “Functional Decision Theory: A New Theory of Instrumental Rationality.” arXiv:1710.05060.