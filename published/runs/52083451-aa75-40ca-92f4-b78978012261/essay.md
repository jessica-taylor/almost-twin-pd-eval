# Action Functional Decision Theory: A Working Mathematical Guide

This essay explains **action functional decision theory** (A-FDT), the decision theory presented in the supplied paper under the name *functional decision theory*. I will take **Equation (4), Section 5** of the paper as the primary formal statement of the theory, and I will write that equation using the name **A-FDT**. Where I discuss rival theories, I will identify them by their standard names: **evidential decision theory** (EDT) and **causal decision theory** (CDT).

The central idea is simple to state, though subtle to operationalize. A-FDT treats an agent’s decision as the output of a fixed mathematical decision function. The agent asks, in the source’s words, “Which output of this decision procedure causes the best outcome?” Rather than asking what would happen if the agent’s physical action were changed while holding fixed all predictors, copies, and models of the agent, A-FDT asks what would happen if the *output of the decision function itself* were different, and then propagates that change through all relevant dependencies.

This makes A-FDT especially useful in problems involving accurate predictors, psychological twins, simulations, contracts, blackmail, and other cases where the environment contains representations of the agent’s decision procedure.

---

## 1. The core intuition behind A-FDT

A-FDT distinguishes three kinds of dependence:

1. **Causal dependence**: one event physically brings about another.
2. **Evidential or statistical dependence**: one event is correlated with another, perhaps because of a common cause.
3. **Subjunctive dependence**: two systems depend on the same mathematical function or logical structure.

The paper’s slogan is: “Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.” In the terminology of this essay, **A-FDT is to subjunctive dependence as CDT is to causal dependence**.

A standard example is two calculators computing the same arithmetic expression. They may be causally independent, but if both are working correctly, their outputs are logically constrained to agree. If one outputs \(7336\) for \(6288+1048\), the other should also output \(7336\). Their outputs are not merely correlated by accident; they both depend on the same function.

A-FDT treats an agent’s decision similarly when predictors or copies are involved. If a reliable predictor has modeled the agent’s decision procedure, then the predictor’s prediction depends on the same mathematical function that the agent is running. Therefore, when the agent considers the hypothetical possibility that her decision function outputs one action, she should also imagine that the predictor’s prediction changes accordingly.

By contrast, a lesion that causes both a preference for smoking and lung cancer is not computing the agent’s decision function. Smoking may be evidence of the lesion, but the lesion does not depend on the output of the agent’s decision procedure. A-FDT therefore does not treat the lesion as something the agent’s decision output can change.

This distinction explains the classic pattern:

- In **Newcomb’s problem**, A-FDT one-boxes, because the predictor’s prediction subjunctively depends on the agent’s decision function.
- In the **smoking lesion problem**, A-FDT smokes, because the lesion and cancer do not subjunctively depend on the agent’s decision function.
- In **Parfit’s hitchhiker problem** and the **transparent Newcomb problem**, A-FDT pays or one-boxes even after the desirable condition has been observed, because the predictor’s earlier behavior depends on what the agent’s decision function would output in that very situation.

---

## 2. The formal statement of A-FDT

All three theories discussed in the paper are expected utility theories. They differ in how they interpret decision hypotheticals: what probability distribution over outcomes should be used when evaluating an action.

Let:

- \(\mathcal A\) be a finite set of actions.
- \(\mathcal X\) be a set of observation histories.
- \(\mathcal O\) be a set of outcomes.
- \(\mathcal U\) be a utility function on outcomes.
- \(V = \mathcal U(\text{Outcome})\) be the utility random variable.
- \(P\) be the agent’s probabilistic world-model.
- \(G\) be a graph describing dependency structure.
- \(x \in \mathcal X\) be the agent’s current observation or input.

EDT evaluates actions by conditional expectation:

\[
\mathrm{EDT}(P,x)
\coloneqq
\arg\max_{a \in \mathcal A}
\mathbb E\left[V \mid \text{Obs}=x, \text{Act}=a\right].
\]

CDT evaluates actions by causal intervention on the physical action variable:

\[
\mathrm{CDT}(P,G,x)
\coloneqq
\arg\max_{a \in \mathcal A}
\mathbb E\left[V \mid \operatorname{do}(\text{Act}=a), \text{Obs}=x\right].
\]

A-FDT, following Equation (4) of the source, intervenes not on the physical action variable but on a variable representing the output of the agent’s decision procedure. Let

\[
D_x
\]

denote the variable representing the output of A-FDT when run on inputs \((P,G,x)\). The source writes this kind of variable as something like \(\mathrm{fdt}(\underline P,\underline G,\underline x)\), where underlining indicates quotation or encoding. The self-reference is not meant to be paradoxical: an agent can have a variable representing the output of its own decision procedure without already knowing that output.

In this notation, the primary formal statement of A-FDT is:

\[
\boxed{
\mathrm{A\text{-}FDT}(P,G,x)
\coloneqq
\arg\max_{a \in \mathcal A}
\mathbb E\left[
V \mid \operatorname{do}(D_x = a)
\right].
}
\]

This is Equation (4) rewritten with the assigned name **A-FDT**.

The operator \(\operatorname{do}(D_x=a)\) is borrowed from Pearl-style causal modeling. It means: set the variable \(D_x\) to value \(a\), then propagate the consequences of that assignment through the graph \(G\), while holding fixed variables that are not affected by that intervention.

The crucial difference is that \(D_x\) is not merely a physical action variable. It is a *logical* or *computational* variable: the output of the agent’s decision function on its actual inputs.

---

## 3. What A-FDT counterfactuals preserve

A-FDT’s hypotheticals are constructed by surgery on a world-model, just as CDT’s are. The difference is what kind of surgery is performed.

CDT intervenes on the token physical act: “What if my body performed action \(a\)?” It preserves correlations that are caused by the action and breaks correlations that are merely evidential.

A-FDT intervenes on the type or function output: “What if this very decision procedure output \(a\)?” It preserves correlations with all variables that subjunctively depend on that function’s output.

Thus:

- If a predictor predicts the agent by modeling the agent’s decision procedure, A-FDT changes the predictor’s prediction when it changes the decision output.
- If another agent is running the same decision procedure, A-FDT changes that agent’s action too.
- If a blackmailer decides whether to send a letter based on a prediction of the agent’s response, A-FDT changes the probability of receiving the letter when it changes the response policy.
- If a lesion merely causes both a preference and a disease, A-FDT does not change the lesion or disease when it changes the decision output.

This gives A-FDT its own version of dominance. CDT says two-boxing dominates one-boxing in Newcomb’s problem if one holds the predictor’s prediction fixed. A-FDT replies that holding the predictor fixed while changing the decision output is the wrong counterfactual. If the predictor is reliable because it tracks the agent’s decision function, then changing the decision output changes the prediction. Under A-FDT-style counterfactuals, two-boxing does not dominate one-boxing.

---

## 4. A-FDT in Newcomb’s problem

Consider Newcomb’s problem. There is a transparent box A containing \$1,000 and an opaque box B containing either \$1,000,000 or \$0. A reliable predictor has placed \$1,000,000 in box B if and only if she predicted the agent would take only box B.

Let the action set be

\[
\mathcal A = \{\text{one-box}, \text{two-box}\}.
\]

Let \(D\) be the variable representing the output of the agent’s A-FDT procedure. The predictor’s prediction depends on \(D\). Suppose the predictor is accurate with probability \(0.99\).

A-FDT compares:

\[
\mathbb E[V \mid \operatorname{do}(D=\text{one-box})]
\]

and

\[
\mathbb E[V \mid \operatorname{do}(D=\text{two-box})].
\]

If \(D=\text{one-box}\), then the predictor probably predicted one-boxing, so box B is probably full. The expected utility is approximately:

\[
0.99 \cdot \$1{,}000{,}000 + 0.01 \cdot \$0
=
\$990{,}000.
\]

If \(D=\text{two-box}\), then the predictor probably predicted two-boxing, so box B is probably empty. The expected utility is approximately:

\[
0.01 \cdot \$1{,}001{,}000 + 0.99 \cdot \$1{,}000
=
\$11{,}000.
\]

Therefore A-FDT chooses:

\[
\mathrm{A\text{-}FDT}(P,G,x) = \text{one-box}.
\]

This reasoning does not require retrocausality. The agent does not believe her current action sends a physical signal into the past. Rather, she treats the predictor’s past prediction as counterfactually dependent on the same decision function she is now running.

---

## 5. A-FDT in the smoking lesion problem

In the smoking lesion problem, smoking is correlated with lung cancer, but the correlation is due to a common cause: a lesion that both makes smoking appealing and causes cancer. Smoking itself does not cause cancer.

EDT refrains from smoking because smoking is bad news: it is evidence that the agent has the lesion. CDT smokes because smoking has no causal effect on cancer.

A-FDT also smokes, but its reason is framed in terms of subjunctive dependence. The lesion is not a predictor-like process. It does not compute the agent’s decision function. Therefore, when A-FDT intervenes on the decision output variable \(D\), it does not change the probability of the lesion or the probability of cancer.

Schematically:

\[
P(\text{lesion} \mid \operatorname{do}(D=\text{smoke}))
=
P(\text{lesion} \mid \operatorname{do}(D=\text{refrain})).
\]

Since smoking gives a direct benefit of \$1,000 and does not change the cancer probability, A-FDT chooses to smoke.

The important point is that A-FDT does not treat every correlation as decision-relevant. It breaks merely evidential correlations, just as CDT does, but it preserves predictor-like and same-function correlations, which CDT breaks.

---

## 6. A-FDT in the transparent Newcomb problem and Parfit’s hitchhiker

The transparent Newcomb problem is especially revealing. Both boxes are transparent. The predictor placed \$1,000,000 in box B if and only if she predicted the agent would one-box upon seeing two full boxes. The agent now sees that both boxes are full.

EDT and CDT both two-box once the agent sees that box B is full. Given that the money is already visible, taking both boxes seems locally better.

A-FDT one-boxes.

To see why, distinguish two decision-function variables:

\[
D_{\text{full}}
\]

representing the output of A-FDT when the agent sees a full box B, and

\[
D_{\text{empty}}
\]

representing the output of A-FDT when the agent sees an empty box B.

The predictor’s prediction determines which observation the agent receives. If the predictor predicts one-boxing upon seeing a full box, she fills box B, and the agent sees a full box. If the predictor predicts two-boxing upon seeing a full box, she leaves box B empty, and the agent sees an empty box.

When the agent sees a full box, A-FDT intervenes on \(D_{\text{full}}\). It asks:

\[
\mathbb E[V \mid \operatorname{do}(D_{\text{full}}=\text{one-box})]
\]

versus

\[
\mathbb E[V \mid \operatorname{do}(D_{\text{full}}=\text{two-box})].
\]

If \(D_{\text{full}}=\text{one-box}\), then with high probability the predictor predicted one-boxing, box B is full, and the agent one-boxes, receiving about \$1,000,000.

If \(D_{\text{full}}=\text{two-box}\), then with high probability the predictor predicted two-boxing, box B is empty, and the agent is not even in the full-box branch. The agent instead ends up in the empty-box branch, where action is governed by \(D_{\text{empty}}\).

So A-FDT does not evaluate two-boxing by saying, “Given that I see a full box, I can take the extra \$1,000.” Instead, it says: if the decision procedure output two-boxing in the full-box case, the predictor would probably have predicted that, and I probably would not be seeing a full box at all.

This is precisely analogous to Parfit’s hitchhiker problem. A driver will rescue the agent only if she predicts the agent will later pay \$1,000 after being rescued. Once in the city, CDT and EDT refuse to pay. A-FDT pays, because the driver’s earlier decision depended on the output of the agent’s decision function in the city-arrival case.

A-FDT therefore acts as if it had made the optimal precommitment, without needing an actual precommitment device.

---

## 7. How A-FDT treats observations

One of the most important features of A-FDT is its treatment of observations.

CDT responds to an observation by conditioning:

\[
\text{CDT changes from } \text{Obs}=x \text{ to } \text{Obs}=y.
\]

A-FDT responds by changing the node on which it intervenes:

\[
\text{A-FDT changes from } D_x \text{ to } D_y.
\]

This is a major conceptual difference.

In Equation (4), the observation \(x\) appears as an input to the decision-function variable \(D_x\). The equation itself does not add an extra condition on \(\text{Obs}=x\). I take this seriously: A-FDT’s response to observation is primarily to select which decision instance is being evaluated, not to condition away counterfactual possibilities in which the agent would have observed something else.

This point is not entirely free of interpretive difficulty. In some examples, the paper appears to include observation variables in the graphical calculation. But the source’s explicit contrast between CDT and A-FDT is that CDT handles observation by Bayesian conditioning while A-FDT handles observation by changing the intervention target. The cleanest operational reading is therefore:

> Upon receiving observation \(x\), A-FDT intervenes on the variable representing the output of A-FDT given input \(x\), and evaluates the consequences of that output using the dependency graph \(G\).

This reading makes A-FDT partly “updateless” in flavor: it chooses the output of the decision procedure that would have done best across the relevant counterfactual structure, rather than choosing the locally best action conditional on the current evidence.

---

## 8. Evaluating policies rather than single actions

Equation (4) evaluates actions. However, the source notes that a policy-based formulation is often preferable, especially in sequential or multi-agent settings.

A policy is a function

\[
\pi : \mathcal X \to \mathcal A
\]

mapping observations to actions.

A policy-level version of A-FDT would introduce a variable \(D\) representing the policy selected by the agent’s decision procedure, and then choose:

\[
\mathrm{A\text{-}FDT}_{\Pi}(P,G)
\coloneqq
\arg\max_{\pi}
\mathbb E\left[
V \mid \operatorname{do}(D=\pi)
\right].
\]

The agent then executes \(\pi(x)\) upon observing \(x\).

This policy formulation is not the primary Equation (4), but it is a natural extension. It is especially helpful when the agent must coordinate across multiple observations, when other agents predict the agent’s policy, or when the agent’s current choice affects what future observations she will receive.

I regard the policy-level version as a reasonable development of the source’s approach, but not as something fully specified by Equation (4) itself.

---

## 9. Applying A-FDT to unfamiliar problems

To apply A-FDT to a new decision problem, one needs to build a suitable model \((P,G)\). The paper does not give a complete general algorithm for constructing \(G\). It says that this is a major open problem. Still, the examples support a practical heuristic.

A reasonable A-FDT workflow is:

1. **Identify the decision procedure.**  
   Determine the function whose output is being evaluated. This is the variable \(D_x\).

2. **Identify the action set and utility function.**  
   Specify \(\mathcal A\), outcomes, and utility \(V\).

3. **Identify predictor-like dependencies.**  
   Ask which parts of the environment depend on the agent’s decision function. These may include:
   - predictors,
   - simulations,
   - psychological twins,
   - other agents using the same decision theory,
   - contracts or mechanisms triggered by predicted behavior,
   - blackmailers deciding whether to make demands.

4. **Add subjunctive-dependence edges to \(G\).**  
   If a variable is computed from, predicted by, or reliably tracks the decision function’s output, make it depend on \(D_x\) in the graph.

5. **Do not connect the decision output to mere common causes.**  
   Lesions, genetic predispositions, background weather, and other common causes should not be descendants of \(D_x\) unless they genuinely depend on the decision function.

6. **Apply the intervention.**  
   For each candidate action \(a\), compute the expected utility under \(\operatorname{do}(D_x=a)\).

7. **Choose the maximizing action.**

This procedure is my operational reconstruction of the paper’s examples. The source supplies the formal rule, Equation (4), and the philosophical distinction between predictor-like and lesion-like dependencies. The detailed graph-building heuristics are an additional assumption needed to use the theory in practice.

---

## 10. What remains open in A-FDT

The most important open problem is the construction of \(G\). CDT can appeal to Pearl’s theory of causal inference to learn causal structure from observations and interventions. A-FDT needs a broader theory of subjunctive dependence: logical, mathematical, computational, and causal dependencies together.

The source is explicit that Equation (4) works only given a graph that accurately describes how changing a logical variable affects other variables. It is not yet clear how to infer such a graph from evidence in full generality.

A second open problem is counterpossible reasoning. If the actual output of the agent’s decision function is \(a^\ast\), then considering \(\operatorname{do}(D_x=a)\) for \(a \neq a^\ast\) means considering a scenario that is, strictly speaking, logically impossible. A-FDT does not require a fully general theory of impossible worlds, but it does require some way to reason about what would follow if a mathematical function had a different output.

A third issue is the exact treatment of observations. Equation (4) suggests that observations enter as inputs to the decision function rather than as conditioning events. This is the interpretation I have used here, because it best explains the transparent Newcomb and blackmail cases. But the paper’s graphical examples sometimes include observation variables in ways that leave room for interpretive refinement.

These open problems do not make A-FDT unusable. They do mean that A-FDT is best understood as a decision rule plus a modeling framework, rather than as a fully automated inference engine.

---

## 11. Why A-FDT is attractive

A-FDT has several appealing features.

First, it gives a unified treatment of single-agent and multi-agent problems. The same principle applies to Newcomb’s problem, twin prisoner’s dilemmas, blackmail, voting coalitions, and sequential self-control problems.

Second, it avoids EDT’s tendency to manage the news. EDT refrains from smoking because smoking is bad news. A-FDT can distinguish bad news from bad consequences.

Third, it avoids CDT’s inability to handle predictors. CDT two-boxes in Newcomb’s problem, refuses to pay in Parfit’s hitchhiker, and becomes unstable in Death in Damascus-style problems. A-FDT preserves the relevant predictor dependencies and therefore acts as a predictor-aware agent.

Fourth, A-FDT aligns with precommitment intuitions. If an agent would rationally precommit to a certain policy, A-FDT tends to act as if already precommitted. But it does not require actual costly precommitment devices.

Finally, A-FDT restores a straightforward utility-based comparison of theories. The paper’s central claim is not merely that A-FDT is conceptually elegant, but that A-FDT agents achieve more utility in the classic fair dilemmas.

---

## Conclusion

A-FDT can be summarized by one formal rule: choose the action that maximizes expected utility after intervening on the output of one’s own decision function. In the notation of this essay:

\[
\mathrm{A\text{-}FDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb E\left[
V \mid \operatorname{do}(D_x=a)
\right].
\]

The theory’s distinctive move is to replace CDT’s intervention on the physical action with an intervention on the logical output of the decision procedure. This allows A-FDT to preserve predictor-like and same-function dependencies while breaking merely evidential correlations.

The main unresolved issue is how to learn or construct the subjunctive-dependence graph \(G\). Until that is solved, A-FDT should be understood as a precise normative rule accompanied by a modeling framework. But within that framework, A-FDT gives clear, utility-maximizing answers in many problems where EDT and CDT famously fail.

---

**Reference**

Yudkowsky, E. and Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2.