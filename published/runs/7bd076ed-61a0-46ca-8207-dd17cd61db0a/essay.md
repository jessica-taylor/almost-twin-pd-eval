# Action Functional Decision Theory: Choosing the Best Output of a Fixed Decision Function

This essay explains **action functional decision theory**, or **A-FDT**, the decision theory presented in Yudkowsky and Soares’s paper *Functional Decision Theory: A New Theory of Instrumental Rationality*. The source calls the theory “FDT”; here I use **A-FDT** consistently for the same assigned theory. The primary formal definition is the source’s Equation (4), Section 5.

A-FDT’s central idea is that a rational agent should not ask, “Which physical action of mine would cause the best outcome?” or “Which action would be best news?” Instead, she should ask, “Which output of this very decision procedure would yield the best outcome?” In other words, the agent treats her decision as the output of a fixed mathematical function and evaluates candidate outputs by imagining how the world would unfold if that function produced one output rather than another.

This produces a theory that behaves like causal decision theory in simple causal settings, but unlike causal decision theory in problems involving predictors, twins, simulations, blackmail, or strategic interaction. It also avoids evidential decision theory’s tendency to treat ordinary evidence about one’s action as something to be managed.

---

## 1. Expected utility and decision hypotheticals

A-FDT is an expected utility theory. Given possible outcomes \(o_1,\dots,o_N\), actions \(a \in \mathcal A\), observations \(x \in \mathcal X\), and utility function \(\mathcal U\), the generic expected utility of an action is

\[
\mathcal{EU}(a) \coloneqq \sum_j P(a \hookrightarrow o_j; x)\,\mathcal U(o_j),
\]

where \(a \hookrightarrow o_j\) is a decision hypothetical: the hypothetical scenario in which action \(a\) is taken and outcome \(o_j\) results. The major decision theories differ in how they interpret this hypothetical.

Evidential decision theory, EDT, interprets it as ordinary Bayesian conditioning:

\[
\mathrm{EDT}(P,x)
\coloneqq
\argmax_{a \in \mathcal A}
\mathbb E\!\left[V \mid \Obs=x, \Act=a\right],
\]

where \(V = \mathcal U(\Outcome)\). EDT asks what outcome is most strongly associated with each action.

Causal decision theory, CDT, uses Pearl-style causal intervention:

\[
\mathrm{CDT}(P,G,x)
\coloneqq
\argmax_{a \in \mathcal A}
\mathbb E\!\left[V \mid \Do(\Act=a), \Obs=x\right].
\]

Here \(P\) is a probability distribution, \(G\) is a causal graph, and \(\Do(\Act=a)\) means: set \(\Act=a\) and propagate this change only along causal arrows. CDT asks what outcome would be caused by the physical action.

A-FDT agrees with CDT that decision hypotheticals should be counterfactual rather than merely evidential, but it disagrees about what should be intervened upon.

---

## 2. The formal rule of A-FDT

The source’s Equation (4), rewritten with the name A-FDT, is:

\[
\boxed{
\mathrm{A\text{-}FDT}(P,G,x)
\coloneqq
\argmax_{a \in \mathcal A}
\mathbb E\!\left[
V \mid \Do\!\left(D_{P,G,x}=a\right)
\right]
}
\tag{4'}
\]

where

\[
D_{P,G,x}
\equiv
\Var{fdt}(\underline{P},\underline{G},\underline{x})
\]

is a variable in the agent’s world-model representing the output of the A-FDT procedure when run on inputs \(P\), \(G\), and \(x\). The underlines indicate dequoting: the variable name contains representations of the model, graph, and observation.

This self-reference is essential but not pathological. The agent does not need to know the value of \(D_{P,G,x}\) in order to include a variable representing that value. The source notes that Kleene’s recursion theorem shows how formal systems can contain representations of themselves.

The important contrast is this:

- CDT intervenes on \(\Act\), the physical action.
- A-FDT intervenes on \(D_{P,G,x}\), the logical output of the decision function that produces the action.

Thus A-FDT asks: what would happen if the output of this very decision procedure were \(a\)?

Observation enters differently than in CDT. CDT conditions on \(\Obs=x\). A-FDT, on the primary reading of Equation (4), responds to observation by changing which decision-function-output node is intervened upon. If the observation changes from \(x\) to \(y\), A-FDT changes from intervening on \(D_{P,G,x}\) to intervening on \(D_{P,G,y}\). This is one of the strangest but most important features of A-FDT.

---

## 3. Subjunctive dependence and the graph \(G\)

Equation (4') is only as definite as the graph \(G\). In CDT, \(G\) encodes causal structure. In A-FDT, \(G\) must encode a broader structure: logical, mathematical, computational, causal, and predictive dependencies. The source describes this as the structure of **subjunctive dependence**.

A variable subjunctively depends on the agent’s decision function when its value would change if the output of that function changed, even if there is no direct causal arrow from the agent’s present physical action to that variable. The paradigm examples are predictors, psychological twins, simulations, and copies. If a predictor reliably predicts the output of the agent’s decision procedure, then the predictor’s prediction is subjunctively dependent on that procedure.

The source’s analogy is useful. Two reliable calculators computing \(6288+1048\) may be causally disconnected, but if one outputs \(7336\), we expect the other to output \(7336\) as well, insofar as both are correctly computing the same function. Their outputs are not merely statistically correlated; they are logically constrained. A-FDT treats reliable predictors similarly.

By contrast, a lesion that causes both a preference for smoking and lung cancer is not subjunctively dependent on the agent’s decision function. The lesion may make smoking statistically correlated with cancer, but the lesion is not computing or predicting the agent’s decision. Therefore, A-FDT does not treat the cancer risk as something the decision function can alter by changing its output.

Operationally, \(G\) tells the agent which correlations to preserve when imagining counterfactual outputs of her decision procedure:

- Preserve correlations due to shared computation, reliable prediction, simulation, or logical equivalence.
- Break correlations that are merely statistical or due to common causes that do not compute the decision function.
- Preserve ordinary causal consequences of the action.

This is why A-FDT can one-box in Newcomb’s problem while smoking in the smoking lesion problem. It treats predictor-like dependencies differently from lesion-like dependencies.

The source is explicit that this is the major unresolved part of the theory. We do not yet have a Pearl-style account of how to learn the structure of subjunctive dependence from observation and experiment. Equation (4') is a decision rule given such a graph.

---

## 4. Worked examples

### 4.1 A-FDT in Newcomb’s problem

In Newcomb’s problem, an agent may take both boxes, receiving whatever is in box A and box B, or take only opaque box B. A reliable predictor has already predicted whether the agent will one-box. Box B contains \$1,000,000 if and only if the predictor predicted one-boxing.

Let \(D\) be the A-FDT output variable for the agent’s current input. The graph contains:

- \(D\), the output of the agent’s decision procedure;
- \(\Act\), the physical action, caused by \(D\);
- \(\Var{Prediction}\), caused by a predictor that models \(D\);
- \(\Var{BoxB}\), full iff the predictor predicted one-boxing;
- \(V\), utility determined by \(\Act\) and \(\Var{BoxB}\).

Assume the predictor is accurate with probability \(0.99\). Under the intervention \(\Do(D=\text{one-box})\):

\[
P(\Var{BoxB}=\text{full}) = 0.99.
\]

The expected utility is approximately

\[
0.99 \cdot \$1{,}000{,}000 + 0.01 \cdot \$0
= \$990{,}000.
\]

Under \(\Do(D=\text{two-box})\):

\[
P(\Var{BoxB}=\text{full}) = 0.01.
\]

The expected utility is approximately

\[
0.01 \cdot \$1{,}001{,}000
+
0.99 \cdot \$1{,}000
=
\$11{,}000.
\]

A-FDT therefore chooses one-boxing.

The reasoning is not retrocausal. A-FDT does not assume the agent’s present physical action sends a signal into the past. Rather, it assumes that the predictor’s past prediction is a reliable representation of the output of the same decision function the agent is now running. To imagine that the function outputs two-boxing is also to imagine that the predictor predicted two-boxing.

CDT, by intervening directly on \(\Act\), holds the predictor’s prediction fixed and therefore two-boxes. EDT one-boxes because one-boxing is good news. A-FDT one-boxes for a counterfactual reason closer in spirit to CDT: it evaluates what would follow if the decision function had a different output.

### 4.2 A-FDT in the smoking lesion problem

In the smoking lesion problem, smoking is correlated with cancer, but only because a lesion causes both a desire to smoke and cancer. Smoking itself does not cause cancer. The agent gains \$1,000 utility from smoking and strongly prefers avoiding cancer.

Here the lesion is not a predictor. It does not model the agent’s decision procedure. Therefore, in the A-FDT graph, the decision-function variable \(D\) affects the action but does not affect the lesion or cancer.

Under \(\Do(D=\text{smoke})\), the probability of cancer remains the same as under \(\Do(D=\text{refrain})\). The only difference is the direct utility gain from smoking. Therefore A-FDT smokes.

The source gives a more careful formalization because the lesion may also affect the agent’s preferences. There may be two possible decision procedures, one associated with smoking-friendly preferences and one associated with smoking-averse preferences. The agent may not know which she has. Even then, when A-FDT intervenes on the decision node corresponding to her actual preferences, that intervention does not change the lesion. Smoking remains better by the direct utility it provides.

This example shows that A-FDT does not simply preserve all correlations between action and outcome. EDT preserves too much: it treats smoking as evidence of cancer and refrains. A-FDT breaks the merely evidential connection while preserving the relevant decision-functional structure.

### 4.3 A-FDT in the transparent Newcomb problem and Parfit’s hitchhiker

The transparent Newcomb problem modifies Newcomb’s problem: both boxes are transparent, and the agent sees whether box B is full before choosing. The predictor filled box B iff she predicted that the agent would one-box after seeing both boxes full.

CDT and EDT both two-box once the agent sees box B full. CDT says the contents are already fixed; EDT says that, conditional on seeing box B full, taking both boxes is better news.

A-FDT instead one-boxes even after seeing box B full. Let \(D_{\text{full}}\) denote the output of the A-FDT procedure upon seeing a full box. The graph contains two relevant decision nodes:

- \(D_{\text{full}}\), used if the agent sees box B full;
- \(D_{\text{empty}}\), used if the agent sees box B empty.

The predictor predicts what \(D_{\text{full}}\) will output. If the predictor predicts one-boxing, she fills box B; otherwise she does not.

Now compare interventions.

Under \(\Do(D_{\text{full}}=\text{one-box})\), with high probability the predictor predicted one-boxing, box B is full, and the agent one-boxes. Expected utility is close to \$1,000,000.

Under \(\Do(D_{\text{full}}=\text{two-box})\), with high probability the predictor predicted two-boxing, box B is empty, and the agent never actually instantiates \(D_{\text{full}}\); instead she uses \(D_{\text{empty}}\). Only with small probability is the predictor wrong and the agent sees a full box while being the kind of decision procedure that two-boxes upon seeing it.

So A-FDT evaluates two-boxing after seeing a full box not as “I see the money, so I take the extra \$1,000,” but as: “If this very procedure for full-box observations two-boxed, predictors would usually have left the box empty, and I would usually not be in this observation branch.”

This is precisely the structure of Parfit’s hitchhiker problem. A driver will rescue the agent only if she predicts the agent will later pay \$1,000. Once rescued, CDT and EDT refuse to pay, because payment is costly and the rescue is already done. A-FDT pays, because being the kind of agent who pays after rescue is what causes the rescue to occur in the first place.

These cases are counterintuitive because they ask the agent to act against the apparent local dominance of an option. Given that the box is visibly full, two-boxing yields \$1,000 more in that branch. But A-FDT denies that this is the correct counterfactual comparison. The correct comparison is between worlds in which the decision function outputs one-boxing and worlds in which it outputs two-boxing, while preserving the predictor’s reliability.

---

## 5. Actions, policies, and observations

Equation (4') evaluates actions at a particular observation \(x\). But the source notes that a policy-based formulation may be preferable, especially in multi-agent or sequential problems. This is not fully formalized in Equation (4'), so I will state it as an operational extension.

A policy is a function

\[
\pi : \mathcal X \to \mathcal A
\]

mapping observations to actions. A policy-level A-FDT rule could be written as

\[
\pi^*
=
\argmax_{\pi}
\mathbb E\!\left[
V \mid \Do(\Pi = \pi)
\right],
\]

where \(\Pi\) is a variable representing the agent’s policy. Once \(\pi^*\) is selected, the agent executes

\[
a^* = \pi^*(x).
\]

This policy formulation makes explicit why A-FDT sometimes appears “updateless.” When evaluating a policy, the agent does not necessarily condition on her current observation as a fixed fact. Instead, she asks what would happen if her policy were such that it produced different actions in different observation branches. Predictors may respond to the policy as a whole, and observations themselves may depend on the policy.

For many single-shot problems, the action-level Equation (4') and the policy-level formulation give the same prescription if the graph is constructed appropriately. In cases where observations are themselves influenced by predictions of the agent’s behavior, the policy perspective clarifies what A-FDT is doing.

This is especially important in blackmail problems. Suppose a blackmailer sends a demand only if she predicts the agent will pay. A policy that pays upon receiving blackmail invites blackmail; a policy that refuses discourages it. A-FDT refuses, even after receiving the demand, because the counterfactual in which the agent’s policy refuses is usually a counterfactual in which the demand was never sent.

---

## 6. How A-FDT evaluates counterfactuals

A-FDT requires counterpossible reasoning. If the agent’s decision function in fact outputs \(a_1\), then the hypothetical “what if it output \(a_2\)?” is, strictly speaking, counter-to-logic. A deterministic mathematical function cannot have two outputs for the same input.

The source acknowledges that this is a technical difficulty. There is not yet a fully satisfactory formal semantics for such counterpossibles. A-FDT avoids needing a general theory by assuming that the agent has a graph \(G\) specifying how the world would change if the logical variable \(D_{P,G,x}\) were set to different values. The \(\Do\)-operator is then applied to that graph.

Operationally, this means the agent should ask:

> If the output of my decision procedure were different, which other variables would differ because they compute, predict, simulate, or depend on that procedure?

For a perfect predictor, the predictor’s prediction changes. For a perfect psychological twin, the twin’s action changes. For a lesion, the lesion does not change. For an ordinary causal consequence, the consequence changes as usual.

This also gives A-FDT its own notion of dominance. CDT says one action dominates another if, holding fixed non-causal background facts, changing the physical action improves utility. A-FDT says one action dominates another if, holding fixed the relevant subjunctive dependencies, changing the output of the decision function improves utility. In Newcomb’s problem, two-boxing dominates only if one wrongly holds the predictor’s prediction fixed while changing the action. A-FDT treats that as an inconsistent hypothetical, like imagining a correctly functioning calculator outputting the wrong sum.

---

## 7. Applying A-FDT to unfamiliar cases

To apply A-FDT to a new decision problem, one should proceed roughly as follows.

First, specify the action set \(\mathcal A\), observation set \(\mathcal X\), outcomes, and utility function.

Second, construct a probabilistic world-model \(P\). This model should include variables for the agent’s decision-function outputs, physical actions, predictions made by other agents or predictors, relevant background states, observations, and outcomes.

Third, construct a dependency graph \(G\). Draw arrows from the relevant decision-function variable \(D_{P,G,x}\) to:

- the agent’s own physical action;
- any predictor, simulation, copy, or twin that reliably computes the same or a sufficiently similar decision function;
- any downstream variables affected by those predictions or computations.

Do not draw arrows from \(D_{P,G,x}\) to variables that are merely statistically correlated with the action but do not compute or predict the decision function.

Fourth, identify the actual observation \(x\) and the corresponding node \(D_{P,G,x}\).

Fifth, for each candidate action \(a\), compute

\[
\mathbb E[V \mid \Do(D_{P,G,x}=a)].
\]

Choose the action with the largest value.

This procedure is clear in outline, but the hard work lies in constructing \(G\). The source does not provide a complete method for doing so.

A reasonable operational rule is this: treat a variable as subjunctively dependent on the agent’s decision function if the agent believes that variable is produced by a process that would, in relevant counterfactual circumstances, output a reliable function of the decision function’s output. If the variable is instead produced by a common cause that merely correlates with the action, do not treat it as subjunctively dependent.

For example:

- A predictor who has modeled the agent: include dependency.
- A psychological twin using the same reasoning: include dependency.
- A carcinogenic lesion causing both desire to smoke and cancer: exclude dependency.
- A random coin toss correlated with action only by accident: exclude dependency.

This is not a formal learning algorithm. It is an interpretive gloss on the source’s predictor-versus-lesion distinction.

---

## 8. Open questions and uncertainties

The largest open question is the construction of \(G\). The source states that Equation (4') works given a graph that accurately describes how changing the value of a logical variable affects other variables, but it is not clear how to deduce that graph from observation. CDT has Pearl’s causal calculus; A-FDT does not yet have an equally developed calculus for subjunctive dependence.

A second open question is the semantics of counterpossibles. A-FDT needs to reason about impossible suppositions, such as “this deterministic algorithm outputs something other than what it actually outputs.” The source treats this as a technical rather than philosophical obstacle, noting that humans can reason about unsettled mathematical claims. But a fully formal account is absent.

A third question concerns observation handling. Equation (4') does not condition on \(\Obs=x\); instead, observation \(x\) determines which decision node is intervened upon. This is essential for transparent Newcomb and blackmail cases. However, in some ordinary cases where observations are exogenous and not prediction-dependent, one might expect conditioning to be harmless. The source’s discussion leaves some ambiguity here. My operational interpretation is that A-FDT should not condition on observations that are themselves decision-relevant consequences of predictors or policies. When observations are purely exogenous information about payoff-relevant states, conditioning may be used without changing the theory’s spirit, provided the graph correctly represents that the observation is not subjunctively dependent on the decision function.

A fourth question is similarity. How similar must another agent or predictor be before its behavior subjunctively depends on one’s own decision function? The source’s examples use perfect twins and highly reliable predictors, but real cases involve imperfect similarity. The natural A-FDT response is to represent this with stochastic accuracy variables, as the source does in Newcomb’s problem. The stronger and more reliable the similarity, the stronger the subjunctive dependency.

These uncertainties mean that A-FDT is not yet a fully algorithmic decision procedure in the same sense that Pearl-style CDT can be once a causal graph is given. A-FDT is precise as a normative rule relative to a subjunctive-dependency model, but model construction remains the hard part.

---

## 9. Why A-FDT matters

A-FDT matters because it separates three ideas that are often conflated:

1. Acting causally.
2. Acting on good evidence.
3. Acting as the output of a predictable decision procedure.

CDT focuses on the first, EDT on the second, and A-FDT on the third. In many realistic strategic situations, outcomes depend not merely on what one physically does, but on what others predict one will do. Contracts, threats, blackmail, cooperation, voting, and coordination all involve predictors and replicas of one’s reasoning.

A-FDT’s prescription can be summarized globally: choose the output of your decision function that leads to the best world when all relevant logical, computational, causal, and predictive dependencies are preserved.

This explains its attractive features. A-FDT agents do not need costly precommitments, because they already act as they would have wanted to precommit to act. They do not pay to avoid information, because observations are handled by choosing the appropriate policy or decision node rather than by fragile conditionalization. They resist blackmail, because being predictably unwilling to pay makes blackmail unprofitable. They cooperate with sufficiently similar agents, because their actions are treated as outputs of a shared or mirrored computation.

The source claims that A-FDT outperforms EDT and CDT in all fair dilemmas, while admitting that “fairness” has not yet been formally defined. That claim should be understood as a normative conjecture supported by examples, not as a theorem. Still, the examples are powerful: A-FDT one-boxes in Newcomb’s problem, smokes in the smoking lesion problem, pays in Parfit’s hitchhiker problem, and refuses to pay in blackmail problems where paying would invite exploitation.

---

## Conclusion

Action functional decision theory evaluates choices by intervening on the output of the agent’s own decision function rather than on the physical action alone. Its core formal rule is

\[
\mathrm{A\text{-}FDT}(P,G,x)
=
\argmax_{a \in \mathcal A}
\mathbb E\!\left[
V \mid \Do(D_{P,G,x}=a)
\right],
\]

where \(D_{P,G,x}\) represents the output of the A-FDT procedure given the agent’s model, dependency graph, and observation.

The theory’s strength is that it preserves decision-relevant logical and predictive dependencies that CDT discards, while avoiding the purely evidential correlations that EDT mistakenly manages. Its main weakness is that it requires a graph of subjunctive dependencies, and we do not yet have a complete formal method for constructing such graphs.

Even so, A-FDT provides a unified and compelling picture of instrumental rationality: rational action is not merely physical intervention or news management, but selection of the best output of the very reasoning process one instantiates.

---

## References

Yudkowsky, E., and Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2.

Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.

Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.