# Policy Functional Decision Theory: Choosing the Best Output of a Fixed Policy

The policy-selection passage in footnote 16 of “Functional Decision Theory: A New Theory of Instrumental Rationality” says:

> “the author’s preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a *policy* which maps inputs to actions, to which the agent then apply her inputs in order to select an action.”

I will call the theory described by that passage **policy functional decision theory**, or **P-FDT**. The source’s body mostly presents an action-level version of functional decision theory, where an agent intervenes on a variable representing “the output of this decision procedure on this observation.” The footnote indicates that the authors’ preferred formulation instead selects a whole policy: a function from possible inputs or observations to actions. The agent then applies the selected policy to her actual input.

This essay develops that policy-level idea. P-FDT’s central normative question is not:

> “Which physical act should I perform?”

or

> “Which act would be best news?”

but rather:

> “Which output of this very policy-selection procedure would produce the best world?”

P-FDT therefore chooses a policy as the output of a fixed mathematical procedure. An action is then the result of applying that policy to the agent’s actual observations.

---

## 1. The basic objects

Let:

- \(\mathcal X\) be the set of possible observation histories or inputs,
- \(\mathcal A\) be the set of possible actions,
- \(\mathcal O\) be the set of possible outcomes,
- \(\mathcal U : \mathcal O \to \mathbb R\) be a bounded utility function.

A **policy** is a function

\[
\pi : \mathcal X \to \mathcal A.
\]

Let \(\Pi\) be the set of policies under consideration. In finite problems, \(\Pi = \mathcal A^{\mathcal X}\). In realistic bounded settings, \(\Pi\) may be a smaller feasible set.

The agent has a world-model \(M = (P, G)\):

- \(P\) is a probability distribution over relevant variables, including observations, actions, predictions, outcomes, and logical or computational variables.
- \(G\) is a dependency graph saying how those variables would change under interventions. It includes causal dependencies and also what the source calls **subjunctive dependencies**: dependencies that arise when some part of the world computes, predicts, simulates, or otherwise depends on the output of the agent’s decision procedure.

The crucial variable for P-FDT is a logical variable

\[
S_M = \mathrm{P\mbox{-}FDT}(M),
\]

representing the policy output by the agent’s own policy-selection procedure when run on model \(M\). This variable is self-referential: the model contains a representation of the very procedure that is using the model. The source notes that this kind of self-reference can be handled by standard recursion-theoretic techniques, and it is not by itself a fatal problem.

P-FDT evaluates each candidate policy \(\pi \in \Pi\) by a subjunctive intervention on \(S_M\):

\[
\mathrm{EU}_{M}^{\mathrm{P-FDT}}(\pi)
=
\mathbb E_P\!\left[V \mid \operatorname{do}(S_M = \pi)\right],
\]

where \(V = \mathcal U(\text{Outcome})\). The agent then selects

\[
\pi_M^* \in \arg\max_{\pi \in \Pi}
\mathbb E_P\!\left[V \mid \operatorname{do}(S_M = \pi)\right].
\]

Given actual observation \(x \in \mathcal X\), the prescribed action is

\[
\mathrm{P\mbox{-}FDT}(M,x) = \pi_M^*(x).
\]

That is the core of P-FDT: intervene on the policy node, choose the best policy, then apply it to the actual input.

---

## 2. Relation to EDT, CDT, and action-level FDT

It helps to compare P-FDT with the other theories discussed in the source.

Evidential decision theory, or EDT, evaluates acts by conditional probability:

\[
\mathrm{EDT}(P,x)
=
\arg\max_{a \in \mathcal A}
\mathbb E[V \mid X=x, A=a].
\]

EDT asks which action would be best news. It preserves all statistical correlations between the action and the world, even when those correlations are not decision-relevant in the right way.

Causal decision theory, or CDT, evaluates acts by causal intervention:

\[
\mathrm{CDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb E[V \mid \operatorname{do}(A=a), X=x].
\]

CDT asks which physical act causally produces the best outcome. It severs correlations unless they are mediated by causal descent from the act.

The action-level functional decision theory presented in the body of the source intervenes on a logical variable representing the output of the decision procedure on the current observation:

\[
\mathrm{FDT}_{\text{action}}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb E[V \mid \operatorname{do}(\mathrm{FDT}(P,G,x)=a)].
\]

P-FDT replaces the action variable with a policy variable:

\[
\pi_M^*
=
\arg\max_{\pi \in \Pi}
\mathbb E[V \mid \operatorname{do}(S_M=\pi)].
\]

The action is then \(\pi_M^*(x)\).

This difference matters because many environments do not merely predict a single action; they predict the agent’s strategy. A predictor may ask, “What will this agent do if she sees a full box?” or “Will this agent pay if she reaches the city?” Those questions are naturally modeled as questions about policies, not isolated acts.

---

## 3. Subjunctive dependence and counterfactuals

P-FDT’s interventions are not ordinary physical interventions. They are interventions on a mathematical or logical variable: the output of the agent’s policy-selection procedure.

The source distinguishes three kinds of dependence:

1. **Statistical dependence**: two variables are correlated, but neither computes the other.  
   Example: a lesion causes both a preference for smoking and cancer.

2. **Causal dependence**: one variable physically brings about another.  
   Example: taking a drug causes recovery.

3. **Subjunctive dependence**: two physical systems depend on the same abstract computation, or one system accurately predicts the output of the other’s decision procedure.  
   Example: two identical calculators computing the same sum, or a predictor simulating an agent’s decision procedure.

P-FDT’s graph \(G\) must encode these subjunctive dependencies. If a predictor’s prediction depends on the output of the agent’s P-FDT procedure, then \(G\) should contain a path

\[
S_M \to \text{Prediction}.
\]

If the predictor’s prediction then determines whether a box is full, whether a blackmailer sends a letter, or whether a driver helps, the graph contains further downstream edges.

By contrast, a lesion may cause both smoking and cancer, but it does not compute the agent’s policy-selection procedure. So the graph should contain

\[
\text{Lesion} \to \text{Smoking}, \qquad
\text{Lesion} \to \text{Cancer},
\]

but not

\[
S_M \to \text{Cancer}.
\]

Thus P-FDT’s counterfactuals preserve predictor-like dependencies while ignoring lesion-like correlations.

The source is explicit that this requires counterpossible reasoning. If the agent is deterministic, then the actual output of her policy-selection procedure is fixed. To ask, “What if P-FDT had selected a different policy?” is to ask a question whose antecedent is counter-to-logic. P-FDT nevertheless needs such counterpossibles. The source does not give a complete semantics for them; it instead assumes that the agent has a graph \(G\) telling her how the world would change if the logical variable were different. I follow that assumption here.

---

## 4. Example: Newcomb’s problem

In Newcomb’s problem, an agent faces two boxes:

- Box A visibly contains \$1,000.
- Box B contains \$1,000,000 if a reliable predictor predicted one-boxing.
- Box B contains \$0 if the predictor predicted two-boxing.

The predictor has already made her prediction. The agent chooses whether to take both boxes or only box B.

Let there be one relevant observation \(x\), so policies reduce to actions. Consider two policies:

\[
\pi_1(x) = \text{one-box},
\]
\[
\pi_2(x) = \text{two-box}.
\]

Assume the predictor is accurate with probability \(0.99\). The graph contains:

\[
S_M \to \text{Prediction} \to \text{Box B} \to V.
\]

Under \(\operatorname{do}(S_M=\pi_1)\), the predictor almost certainly predicted one-boxing, so box B is almost certainly full:

\[
\mathrm{EU}(\pi_1)
=
0.99 \cdot 1{,}000{,}000
+
0.01 \cdot 0
=
990{,}000.
\]

Under \(\operatorname{do}(S_M=\pi_2)\), the predictor almost certainly predicted two-boxing, so box B is almost certainly empty:

\[
\mathrm{EU}(\pi_2)
=
0.01 \cdot 1{,}001{,}000
+
0.99 \cdot 1{,}000
=
11{,}000.
\]

P-FDT selects \(\pi_1\). The agent one-boxes.

CDT two-boxes because it intervenes on the physical act and holds the box contents fixed. EDT one-boxes because one-boxing is good evidence that the box is full. P-FDT one-boxes for a different reason: the predictor’s prediction subjunctively depends on the output of the same policy-selection procedure.

---

## 5. Example: the smoking lesion

In the smoking lesion problem, smoking is correlated with cancer, but only because a lesion causes both a preference for smoking and cancer. Smoking itself does not cause cancer. The agent gains \$1,000 utility from smoking and strongly prefers avoiding cancer.

Here the correct P-FDT graph has:

\[
\text{Lesion} \to \text{Smoking}, \qquad
\text{Lesion} \to \text{Cancer},
\]

but no edge

\[
S_M \to \text{Cancer}.
\]

The policy node affects the action, but not the lesion and not the cancer. Thus, for policies \(\pi_S\) and \(\pi_R\):

\[
\pi_S(x)=\text{smoke},
\]
\[
\pi_R(x)=\text{refrain},
\]

the probability of cancer is the same under both interventions:

\[
P(\text{Cancer} \mid \operatorname{do}(S_M=\pi_S))
=
P(\text{Cancer} \mid \operatorname{do}(S_M=\pi_R)).
\]

Smoking adds \$1,000 utility without changing cancer risk. P-FDT therefore chooses the smoking policy.

This shows the difference between P-FDT and EDT. EDT refrains because smoking is bad news. P-FDT smokes because the lesion is not a predictor of the agent’s policy. It is merely a common cause.

---

## 6. Example: transparent Newcomb and Parfit’s hitchhiker

P-FDT’s policy character becomes especially clear in cases where the agent receives an observation before acting.

In the transparent Newcomb problem, both boxes are transparent. The predictor filled box B if and only if she predicted that the agent would one-box upon seeing that both boxes are full. Suppose the agent sees that both boxes are full. Should she one-box or two-box?

EDT and CDT two-box once the agent sees that box B is full. CDT says taking box A adds \$1,000 causally. EDT says that given box B is full, taking box A is better news.

P-FDT instead chooses a policy before applying the actual observation. Let the observation set include:

\[
\text{full} = \text{“both boxes are full,”}
\]
\[
\text{empty} = \text{“box B is empty.”}
\]

Consider two policies:

\[
\pi_{\text{one}}(\text{full}) = \text{one-box},
\]
\[
\pi_{\text{two}}(\text{full}) = \text{two-box}.
\]

Assume, for simplicity, that both policies two-box when the box is empty. The predictor predicts which policy the agent will run. If P-FDT selects \(\pi_{\text{one}}\), the predictor fills box B, the agent sees “full,” and one-boxes. If P-FDT selects \(\pi_{\text{two}}\), the predictor leaves box B empty, the agent sees “empty,” and two-boxes.

With predictor accuracy \(0.99\), the policy of one-boxing upon seeing a full box has expected utility near

\[
0.99 \cdot 1{,}000{,}000,
\]

while the policy of two-boxing upon seeing a full box leads mostly to seeing an empty box and receiving about \$1,000.

P-FDT therefore selects the policy:

\[
\pi^*(\text{full}) = \text{one-box}.
\]

When the agent actually sees that both boxes are full, she applies \(\pi^*\) and one-boxes.

The same structure appears in Parfit’s hitchhiker problem. A driver will rescue the agent only if she predicts the agent will pay \$1,000 after reaching the city. Once in the city, paying is costly and cannot be enforced. EDT and CDT both refuse to pay once in the city, so the driver predicts refusal and leaves them behind.

P-FDT selects the policy:

\[
\pi^*(\text{city}) = \text{pay}.
\]

The driver predicts this policy, rescues the agent, and the agent pays. P-FDT acts as though it had precommitted, without needing an actual precommitment device.

This is one of the main advantages of policy selection. The agent does not ask, “Given that I am already in the city, should I pay?” Instead, P-FDT asks, “Which policy should this procedure output: pay-if-in-city, or refuse-if-in-city?” Because the driver’s behavior depends on the policy, P-FDT chooses the policy that makes rescue likely.

---

## 7. Example: blackmail and observation-dependent counterfactuals

The policy formulation is also useful in blackmail problems.

Suppose a predictor sends a blackmail letter only if she predicts the agent will pay upon receiving it. If the agent receives the letter, paying makes the threat go away, but refusing would have made the predictor not send the letter in the first place.

A policy-level model contains:

\[
S_M \to \text{Predictor sends letter} \to \text{Observation of letter}.
\]

Consider two policies:

\[
\pi_{\text{pay}}(\text{letter}) = \text{pay},
\]
\[
\pi_{\text{refuse}}(\text{letter}) = \text{refuse}.
\]

Under \(\operatorname{do}(S_M=\pi_{\text{pay}})\), the predictor sends the letter and the agent pays. Under \(\operatorname{do}(S_M=\pi_{\text{refuse}})\), the predictor usually does not send the letter at all. If the predictor is highly accurate, the expected loss from the refusing policy is much smaller than the expected loss from the paying policy.

P-FDT therefore selects the refusing policy. If, nevertheless, the agent actually receives the letter, P-FDT applies the selected policy and refuses to pay.

This illustrates an important feature of P-FDT counterfactuals: when imagining a different policy, P-FDT may imagine having made different observations. The agent does not condition on the actual observation in a way that holds it fixed across all counterfactual policies. If she did, she would lose the connection between her policy and the predictor’s decision to send the letter.

---

## 8. How P-FDT evaluates actions

Strictly speaking, P-FDT does not first evaluate actions. It evaluates policies. But we can derive an action recommendation from the selected policy.

Given actual observation \(x\), compare actions \(a\) and \(b\) by comparing policies that prescribe those actions at \(x\). If every optimal policy prescribes \(a\) at \(x\), then P-FDT performs \(a\). If several optimal policies prescribe different actions at \(x\), P-FDT is indifferent among them, or needs a tie-breaking rule.

Sometimes two policies agree at the actual observation but differ elsewhere. P-FDT may still prefer one over the other because predictors or observations depend on the whole policy. This is a distinctively policy-level effect.

For example, an agent might currently face a situation where both policies prescribe the same act, but one policy would have behaved differently in a counterfactual branch that a predictor simulated. If the predictor’s behavior depends on the entire policy, P-FDT can favor the policy with better global behavior even though the immediate act is unchanged.

---

## 9. Updating and the role of actual observations

The footnote’s policy-selection idea leaves an important question unresolved: when the agent has already made an observation, should P-FDT evaluate policies using a prior model, a posterior model, or something in between?

The source’s action-level discussion suggests that functional decision theory does not respond to observations simply by conditioning on them. Instead, the observation changes which decision-function output is being considered. In the policy formulation, I think the cleanest operational rule is this:

> P-FDT selects a policy using a model that represents the agent’s knowledge of exogenous facts, but it does not condition the policy comparison on observations that may themselves be downstream of the policy node.

In other words, if an observation could have been affected by the agent’s policy—because a predictor decides whether to show it, a blackmailer decides whether to send it, or a box’s transparency reveals a predicted action—then P-FDT should not treat that observation as fixed evidence when comparing policies. The observation is part of the world generated by the policy.

If an observation is known to be exogenous to the policy node, then conditionalizing on it is safe and usually appropriate. For example, if the agent observes a weather report that no predictor can use or affect, P-FDT can update its model of the weather while still evaluating policies as whole mappings from observations to actions.

This is my own operational elaboration; the footnote does not settle it. But it seems necessary if P-FDT is to handle transparent Newcomb, Parfit’s hitchhiker, and blackmail cases correctly. In those cases, the counterfactual policy changes what the agent would have observed. Conditioning on the actual observation would destroy precisely the dependency P-FDT is meant to respect.

---

## 10. The problem of constructing the dependency graph

The source is candid that a major open problem is constructing the graph \(G\). CDT can appeal, at least in principle, to Pearl-style causal discovery. P-FDT needs a broader account of subjunctive dependence: logical, computational, predictive, and causal dependencies.

For idealized examples, we simply stipulate the graph:

- In Newcomb’s problem, the predictor depends on the agent’s decision procedure.
- In the smoking lesion problem, the lesion does not depend on the agent’s decision procedure.
- In twin prisoner’s dilemma, the twin implements the same decision procedure.
- In blackmail problems, the blackmailer predicts the agent’s policy.

But in unfamiliar cases, how should an agent decide which variables are subjunctively dependent on \(S_M\)?

A reasonable heuristic is:

> Include an edge from \(S_M\) to \(Y\) if a competent model of the world says that, were the P-FDT policy-selection procedure to output a different policy, \(Y\) would change accordingly.

This is not a complete formal theory. It is a guide for constructing the graph. It handles predictors, simulations, copies, and twins. It excludes lesions, random coincidences, and common causes that do not compute or predict the agent’s policy.

The source admits that this is perhaps the largest open problem for functional decision theory. P-FDT inherits that open problem.

---

## 11. Logical uncertainty and counterpossibles

P-FDT also requires reasoning about logical uncertainty. The variable \(S_M\) represents the output of a computation. If the computation is deterministic, then its output is mathematically fixed. Yet P-FDT must compare hypothetical worlds where \(S_M\) has different values.

This is counterpossible reasoning. The source acknowledges that we lack a fully satisfactory account of counterpossibles. It argues that the difficulty is technical rather than fatal: humans can reason about false mathematical assumptions, and agents only need limited counterpossible reasoning about predictors and decision procedures.

In the formalism above, I have treated \(G\) as supplying the needed counterpossible semantics. This is an idealization. A bounded P-FDT agent would likely use approximations: simulations, proofs, statistical predictors, or heuristic models of how other agents predict it.

This is an additional assumption of mine, not a fully developed part of the source. The source gives the skeleton—intervene on a logical variable—but not the full semantics of the intervention.

---

## 12. Multi-agent cases

The footnote says the difference between action selection and policy selection “only matters in multi-agent dilemmas so far as we can tell.” That suggests the authors expected policy selection to be especially important when several agents reason about one another.

In a multi-agent setting, each agent may have a policy node:

\[
S_1 = \mathrm{P\mbox{-}FDT}(M_1),
\]
\[
S_2 = \mathrm{P\mbox{-}FDT}(M_2).
\]

If agent 1’s predictor models agent 2’s policy, then \(M_1\) contains a variable representing \(S_2\). If the agents are psychological twins running the same P-FDT procedure on symmetric inputs, there may be a single abstract policy output instantiated in both agents. In that case, intervening on the shared policy variable changes both agents’ actions.

This gives P-FDT its cooperative behavior in twin prisoner’s dilemma. If both agents use the same policy-selection procedure, then the question is how that procedure should conclude. If it concludes “cooperate,” both cooperate. If it concludes “defect,” both defect. P-FDT chooses cooperate.

But one must be careful. Not every correlation between agents is subjunctive dependence. Two agents may have similar behavior because of common training, common culture, or common environment, without one predicting the other or both instantiating the same relevant computation. P-FDT should not treat all correlations as decision-relevant. The graph must distinguish shared computation from mere statistical similarity.

The source does not fully develop this multi-agent policy formalism. The footnote points toward it, but the details remain open.

---

## 13. Stochastic policies and bounded agents

The discussion above assumes deterministic policies. The source also mostly assumes deterministic decision functions, though it allows imperfect predictors and noisy execution.

P-FDT can be extended to stochastic policies:

\[
\pi : \mathcal X \to \Delta(\mathcal A),
\]

where \(\Delta(\mathcal A)\) is the set of probability distributions over actions. The intervention \(\operatorname{do}(S_M=\pi)\) then sets the agent’s action distribution at each observation. Expected utility is taken over both environmental uncertainty and policy randomness.

However, perfect predictors create subtleties for randomization. If a predictor can predict the agent’s random seed, then the random choice is not independent of the predictor. P-FDT must represent that dependency in \(G\). If the randomness is genuinely unpredictable by the environment, then it may be treated as exogenous.

For bounded agents, the set \(\Pi\) cannot be all mathematical functions from observations to actions. A realistic P-FDT agent would maximize over a tractable class of policies, perhaps using approximate expected utility estimates. The normative ideal remains the same: choose the policy whose subjunctive intervention yields the best expected world.

---

## 14. What P-FDT gets right

P-FDT preserves the attractive features of functional decision theory while making the policy structure explicit.

First, P-FDT one-boxes in Newcomb’s problem because the predictor depends on the agent’s decision procedure.

Second, P-FDT smokes in the smoking lesion problem because the lesion is not a predictor of the agent’s policy.

Third, P-FDT pays in Parfit’s hitchhiker and one-boxes in transparent Newcomb because the relevant prediction is about what the agent’s policy will do after receiving an observation.

Fourth, P-FDT resists blackmail because a policy of refusing makes blackmail unprofitable, and the counterfactual policy comparison allows the agent to imagine not receiving the blackmail letter.

Fifth, P-FDT acts as though it had precommitted. It does not need binding commitments because it selects the policy that would have been best to commit to.

The unifying idea is that the agent’s decision procedure is a natural object in the world. Other agents, predictors, and simulations may depend on it. A good decision theory should not sever those dependencies when evaluating options. P-FDT treats the choice of policy as the primary object of decision.

---

## 15. Remaining uncertainties

Several important questions remain unresolved by the source.

First, the footnote does not say exactly how P-FDT updates on observations. I have proposed that P-FDT should not condition on observations that are themselves downstream of the policy node, but this needs a more precise general account.

Second, the source does not explain how to learn or infer subjunctive dependency graphs. It assumes \(G\) is given. In real applications, constructing \(G\) may be the hardest part.

Third, the semantics of counterpossible interventions on logical variables remain informal. The graph-based treatment is useful but not foundational.

Fourth, the multi-agent policy version is only mentioned. A full game-theoretic treatment would need to say how multiple P-FDT agents model one another’s policy nodes and what happens when their models are imperfect or asymmetric.

Fifth, the source says the policy/action distinction “only matters in multi-agent dilemmas so far as we can tell.” That is an empirical or conjectural claim, not a theorem. It may be that policy selection matters in some single-agent sequential problems as well, especially where an agent’s later observations depend on her earlier policy.

These uncertainties do not make P-FDT unusable. They mean that P-FDT is best understood as an idealized normative framework, plus a set of modeling assumptions, rather than a fully algorithmic procedure for every real-world case.

---

## Conclusion

Policy functional decision theory, or P-FDT, is the policy-level version of the functional decision theory described in the source. Its central rule is to choose a policy by intervening on the output of the agent’s own policy-selection procedure, then apply that policy to the actual input.

Formally, if \(S_M\) is the variable representing the policy chosen by \(\mathrm{P\mbox{-}FDT}(M)\), P-FDT selects

\[
\pi_M^*
\in
\arg\max_{\pi \in \Pi}
\mathbb E[V \mid \operatorname{do}(S_M=\pi)]
\]

and acts by computing \(\pi_M^*(x)\).

P-FDT differs from EDT because it uses subjunctive interventions rather than evidential conditioning. It differs from CDT because it intervenes on a policy-level logical variable rather than a physical act. And it differs from the action-level formulation in the source because it treats whole policies, not isolated actions, as the objects of choice.

The result is a theory that one-boxes in Newcomb’s problem, smokes in the smoking lesion problem, pays the driver in Parfit’s hitchhiker, one-boxes in transparent Newcomb, and refuses blackmail when refusal is the policy that makes blackmail unprofitable. Its main open problems are the construction of subjunctive dependency graphs, the semantics of counterpossible interventions, and the precise treatment of updating in policy selection.

---

## References

Yudkowsky, E., and Soares, N. “Functional Decision Theory: A New Theory of Instrumental Rationality.” arXiv:1710.05060v2.

Joyce, J. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

Pearl, J. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.