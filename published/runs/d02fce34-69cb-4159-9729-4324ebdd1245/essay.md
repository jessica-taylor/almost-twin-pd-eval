# Policy Functional Decision Theory: Choosing the Best Policy of a Fixed Decision Function

Policy functional decision theory, which I will call **P-FDT**, is a variant of functional decision theory in which the fundamental object of choice is not a single physical action but a *policy*: a function from possible inputs, observations, or decision situations to actions. The supplied source develops functional decision theory, or FDT, mostly by saying that an agent should treat her decision as the output of a fixed mathematical function and ask which output of that function would yield the best outcome. In a footnote, however, the source identifies a more basic formulation:

> “the author’s preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action.”  
> — footnote 16

Earlier, the source says similarly that in the preferred formalization, agents “iterate over *policies* (mappings from observations to actions) rather than actions.” The source adds that this difference “only matters in multi-agent dilemmas so far as we can tell,” and therefore sets it aside in the main text. My task here is to take that policy-selection passage as the primary source for **P-FDT**, develop its mathematics as clearly as I can, and explain how a mathematically literate reader could use it to decide unfamiliar cases.

Because the footnote is brief, some details are underdetermined. I will therefore distinguish between claims made by the source and my own reconstruction or operational assumptions.

---

## 1. The central idea of P-FDT

Standard expected utility theories compare possible actions. Evidential decision theory, **EDT**, asks which action would be the best news to learn one had taken. Causal decision theory, **CDT**, asks which action would causally produce the best outcome. Functional decision theories instead ask a different question: which output of one’s decision procedure should that procedure produce?

P-FDT sharpens this idea by making the output a *policy* rather than a single action. A policy is a function

\[
\pi : \mathcal X \to \mathcal A,
\]

where \(\mathcal X\) is a set of possible inputs or observation histories and \(\mathcal A\) is a set of actions. In a sequential problem, \(\mathcal X\) may be the set of histories available at a decision point; in a one-shot problem with no observations, \(\mathcal X\) may be a singleton and a policy collapses to an ordinary action.

The P-FDT agent does not first ask, “What should I do now, given that I have observed \(x\)?” Instead, she asks:

> Which policy should this very decision procedure output, given that predictors, copies, and other agents may depend on the policy this procedure outputs?

Having selected a policy \(\pi^*\), the agent then applies her actual input \(x\) and performs

\[
a = \pi^*(x).
\]

This distinction matters when the agent’s observation is itself correlated with the policy she follows. In transparent Newcomb problems, blackmail problems, and some multi-agent games, the best policy may make some observations likely or unlikely. If the agent conditioned only on the observation she actually receives, she might abandon the policy that made the favorable observation likely in the first place.

---

## 2. A formal model for P-FDT

The source gives an action-level equation for FDT using Pearl-style interventions:

\[
\mathrm{FDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E\!\left[V \mid \mathrm{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\right].
\]

Here \(P\) is the agent’s probabilistic world-model, \(G\) is a graph describing relevant dependency structure, \(x\) is the observation history, and \(\mathrm{fdt}(\underline P,\underline G,\underline x)\) is a variable representing the output of the agent’s decision function on those inputs.

For **P-FDT**, I propose the following policy-level analogue. Let

\[
\Pi = \{\pi : \mathcal X \to \mathcal A\}
\]

be the set of feasible policies. Let \(D\) be a distinguished variable in the agent’s model representing the policy selected by the agent’s decision procedure. In the source’s self-referential style, we may write

\[
D = \mathrm{P\text{-}FDT}(\underline P,\underline G).
\]

Then P-FDT evaluates each candidate policy \(\pi\) by performing an intervention that sets \(D=\pi\):

\[
\pi^*
\in
\arg\max_{\pi\in\Pi}
\mathbb E_P\!\left[U \mid \mathrm{do}(D=\pi)\right].
\]

Once \(\pi^*\) is chosen, the action at actual observation \(x\) is

\[
a^* = \pi^*(x).
\]

This is my reconstruction of the policy-selection idea in footnote 16. The source does not give a full equation for the policy version, so the exact formalization involves some interpretation.

For comparison, we can write EDT and CDT roughly as follows:

\[
\mathrm{EDT}(P,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E_P[U \mid X=x, A=a],
\]

\[
\mathrm{CDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E_P[U \mid \mathrm{do}(A=a), X=x].
\]

EDT conditions on the action. CDT intervenes on the physical action variable. P-FDT intervenes on the policy-output variable.

The graph \(G\) is crucial. It must encode not only causal structure but also what the source calls *subjunctive* dependencies: dependencies of predictors, simulations, copies, twins, and other systems whose behavior tracks the output of the agent’s decision procedure. If a predictor reliably predicts the agent’s policy, then the predictor’s behavior should be downstream of \(D\). If a lesion merely causes both a preference and a disease, but does not track the agent’s decision procedure, then it should not be downstream of \(D\).

A practical P-FDT recipe is therefore:

1. Identify the possible inputs \(\mathcal X\), actions \(\mathcal A\), and policies \(\Pi\).
2. Build a probabilistic model \(P\) over relevant variables: observations, actions, predictors, other agents, outcomes, and utility.
3. Specify a dependency graph \(G\) with a node \(D\) representing the output of the P-FDT policy-selection function.
4. For each candidate policy \(\pi\), perform the intervention \(\mathrm{do}(D=\pi)\).
5. Compute expected utility under that intervention.
6. Choose a policy maximizing expected utility.
7. Execute the chosen policy on the actual input.

This procedure is idealized. Real agents cannot enumerate all policies or perfectly model all subjunctive dependencies. But it gives the normative structure of P-FDT.

---

## 3. Observations, updatelessness, and counterfactuals

The most delicate question in P-FDT is how to treat the actual observation \(x\). Should the policy maximization be conditioned on \(x\)? For example, if the agent sees that the opaque box is full, should P-FDT choose the best policy conditional on seeing a full box?

The source’s examples suggest that the answer is usually **no**, at least when the observation is itself influenced by predictors of the agent’s decision procedure. In the transparent Newcomb problem, if the agent sees that both boxes are full, EDT and CDT both two-box because, conditional on seeing a full box, taking both boxes gives an extra \$1,000. But FDT one-boxes. The source explains that when the FDT agent imagines two-boxing, she imagines a world in which the predictor likely left the box empty. In other words, the counterfactual evaluation allows the observation itself to change.

The policy formulation makes this natural. P-FDT chooses a policy before, or as if before, the actual observation is known. It evaluates the policy’s expected consequences over the possible observations the agent might receive. Then it applies the actual observation to the selected policy.

Thus, my preferred operational interpretation is:

\[
\pi^*
\in
\arg\max_{\pi\in\Pi}
\mathbb E_P[U \mid \mathrm{do}(D=\pi)],
\]

without conditioning on the actual observation \(x\), when \(x\) is itself a variable that may be affected by the policy through predictors or other subjunctive dependencies.

If the agent receives genuinely exogenous evidence \(E=e\) that is not downstream of \(D\) and was not already represented in the policy space, then it may be appropriate to evaluate

\[
\pi^*_e
\in
\arg\max_{\pi\in\Pi}
\mathbb E_P[U \mid \mathrm{do}(D=\pi), E=e].
\]

But if the “evidence” is an observation whose probability depends on the policy, conditioning on it can destroy the very dependency that makes the good outcome possible. This is why P-FDT behaves in an updateless or quasi-updateless way in predictor problems.

This also clarifies P-FDT’s counterfactuals. To evaluate \(\pi\neq\pi^*\), P-FDT imagines a world in which the same decision function had output \(\pi\) instead of \(\pi^*\). If the actual decision procedure is deterministic, this is a counterpossible: strictly speaking, the function cannot have a different output on the same input. The source acknowledges that this is a technical difficulty for functional decision theory. P-FDT inherits it. The graph \(G\) is meant to tell us how the world would change if the logical output changed, even though such a change is not physically or logically ordinary.

---

## 4. Worked examples

### 4.1 Newcomb’s problem

In Newcomb’s problem, the agent chooses between one-boxing and two-boxing. A reliable predictor filled the opaque box iff she predicted the agent would one-box. The predictor is correct 99% of the time.

Here there is no meaningful observation before action, so policies reduce to actions. Let \(\pi_1\) be the one-boxing policy and \(\pi_2\) the two-boxing policy.

Under \(\mathrm{do}(D=\pi_1)\), the predictor probably predicted one-boxing, so the box is full with probability \(0.99\). Expected utility is approximately

\[
0.99 \cdot \$1{,}000{,}000 + 0.01 \cdot \$0
=
\$990{,}000.
\]

Under \(\mathrm{do}(D=\pi_2)\), the predictor probably predicted two-boxing, so the box is full with probability \(0.01\). Expected utility is

\[
0.01 \cdot \$1{,}001{,}000
+
0.99 \cdot \$1{,}000
=
\$11{,}000.
\]

P-FDT therefore chooses the one-boxing policy. This matches the source’s claim that FDT one-boxes in Newcomb’s problem.

### 4.2 The smoking lesion problem

In the smoking lesion problem, smoking is correlated with cancer only because a lesion causes both a fondness for smoking and cancer. Smoking does not cause cancer. The agent gains \$1,000 utility from smoking and \$1,000,000 from not dying of cancer.

Here the lesion is not subjunctively dependent on the agent’s decision procedure. The lesion does not predict the agent’s policy. It is a common cause of a preference and a disease, not a predictor. Therefore, in the P-FDT graph, the policy node \(D\) affects the action variable, but it does not affect the lesion or cancer variables.

Thus, under either policy,

\[
P(\text{lesion} \mid \mathrm{do}(D=\pi_{\text{smoke}}))
=
P(\text{lesion} \mid \mathrm{do}(D=\pi_{\text{refrain}})).
\]

Smoking adds \$1,000 utility and does not change the probability of cancer. P-FDT therefore smokes. This is the source’s desired result: FDT-like theories should one-box in Newcomb’s problem but smoke in the smoking lesion problem.

The difference is that the predictor in Newcomb’s problem is predictor-like: its behavior depends on the agent’s decision procedure. The lesion is lesion-like: it is statistically correlated with the agent’s action but does not track the output of the decision procedure.

### 4.3 Transparent Newcomb problem

In the transparent Newcomb problem, the agent can see both boxes. The predictor filled box B iff she predicted that the agent would leave box A behind upon seeing that both boxes are full.

Now the policy space is nontrivial. The agent may observe either `full` or `empty`. A policy has at least two components:

\[
\pi(\text{full}) \in \{\text{one-box}, \text{two-box}\},
\]
\[
\pi(\text{empty}) \in \{\text{one-box}, \text{two-box}\}.
\]

Consider the policy

\[
\pi^*(\text{full})=\text{one-box}, \qquad
\pi^*(\text{empty})=\text{two-box}.
\]

Under \(\mathrm{do}(D=\pi^*)\), a 99% accurate predictor predicts one-boxing upon seeing a full box, so box B is full with probability \(0.99\). The agent observes `full`, one-boxes, and receives \$1,000,000. With probability \(0.01\), the predictor is wrong, box B is empty, the agent observes `empty`, two-boxes, and receives \$1,000. Expected utility is therefore approximately

\[
0.99 \cdot \$1{,}000{,}000
+
0.01 \cdot \$1{,}000
=
\$990{,}010.
\]

Now consider the policy

\[
\pi'(\text{full})=\text{two-box}, \qquad
\pi'(\text{empty})=\text{two-box}.
\]

Under \(\mathrm{do}(D=\pi')\), the predictor predicts two-boxing upon seeing a full box, so box B is empty with probability \(0.99\). The agent usually observes `empty` and two-boxes for \$1,000. With probability \(0.01\), the predictor is wrong, the box is full, and the agent two-boxes for \$1,001,000. Expected utility is

\[
0.99 \cdot \$1{,}000
+
0.01 \cdot \$1{,}001{,}000
=
\$11{,}000.
\]

P-FDT chooses \(\pi^*\). If the agent actually sees a full box, she one-boxes. She does not condition on the observed full box and choose two-boxing, because doing so would ignore the fact that seeing a full box is itself evidence of a policy that one-boxes upon seeing a full box.

This example shows why policy selection is conceptually useful. The agent is not merely choosing an action at the observed node; she is choosing a way of responding to possible observations.

### 4.4 Mechanical blackmail

In the mechanical blackmail problem, a blackmailer runs a damaging program iff she predicts the agent will pay upon receiving the blackmail letter. If the program is run, the agent can stop it by paying \$1,000; otherwise the program causes \$1,000,000 in damages.

Let the policy space include at least:

\[
\pi_{\text{pay}}(\text{letter})=\text{pay},
\]
\[
\pi_{\text{refuse}}(\text{letter})=\text{refuse}.
\]

If P-FDT selects \(\pi_{\text{pay}}\), the blackmailer predicts payment, runs the program, and sends the letter. The agent pays and loses \$1,000.

If P-FDT selects \(\pi_{\text{refuse}}\), the blackmailer predicts refusal and does not run the program. The agent is not blackmailed and loses nothing, assuming a perfect predictor.

Thus P-FDT chooses the refusing policy. If the agent nevertheless receives the letter, P-FDT still refuses. This seems strange, but it follows from the policy logic: the agent chooses the policy that makes blackmail unattractive. In the perfect-predictor case, receiving the letter while following the refusing policy is an off-path or impossible observation. In the imperfect-predictor case, receiving the letter is evidence of predictor error. The source says that P-FDT-like agents may refuse even when they know the blackmailer predicted wrongly, because it is advantageous to be the kind of agent whose policy refuses.

This is one place where the source leaves room for interpretation. I am assuming that P-FDT evaluates policies from a prior or global perspective rather than conditioning away the observation that the letter has been received. That assumption is not explicit in footnote 16, but it coheres with the source’s discussion of updatelessness and with the claim that FDT agents “entertain the hypothesis that, if their action were different, they might have made different observations.”

---

## 5. Policies, games, and multi-agent dependence

The footnote says that the policy/action distinction “only matters in multi-agent dilemmas so far as we can tell.” The source does not fully develop such dilemmas, so this is an area where interpretation is required.

The natural idea is that in multi-agent settings, other agents may respond not merely to one isolated action but to an agent’s strategy. In an extensive-form game, for example, another player may trust an agent only if she predicts that the agent’s policy will repay trust. The relevant prediction is not merely “the agent will repay now,” but “the agent is following a policy that repays when trusted.” P-FDT represents this by making the other player’s action depend on the policy node \(D\), not merely on the local action variable.

Consider a simple trust game. Bob first decides whether to trust Alice. If Bob trusts Alice, Alice can either cooperate, giving both players a high payoff, or defect, giving Alice a slightly higher payoff and Bob a low payoff. Bob trusts only if he predicts that Alice’s policy will cooperate after being trusted.

If Alice evaluates only the local action after being trusted, defection may look attractive. But if Bob’s trust depends on Alice’s policy, then Alice should evaluate the policy as a whole. A policy that cooperates after trust may induce Bob to trust, producing a high expected payoff. A policy that defects after trust may cause Bob not to trust, producing a lower payoff. P-FDT captures this by comparing policies under interventions on \(D\).

This is closely related to the source’s arguments about precommitment. The source claims that FDT agents act as they would have precommitted to act, without needing actual binding precommitments. P-FDT makes that idea explicit: the agent chooses a policy, and the policy functions as a stable plan across possible inputs.

In symmetric multi-agent problems, such as prisoner’s dilemmas between psychological twins or voting coalitions among similar agents, P-FDT also treats other agents’ decisions as potentially subjunctively dependent on the same decision procedure. If two agents run the same policy-selection function on relevantly similar inputs, then changing the output of that function counterfactually changes both agents’ policies. P-FDT therefore may prescribe cooperation or collective action where CDT would defect.

The source does not give a full game-theoretic formalism for P-FDT, so this remains partly programmatic. But the core principle is clear: when other agents depend on your decision procedure, they often depend on your policy, not merely your present physical movement.

---

## 6. Open questions and my additional assumptions

The source is explicit that functional decision theory relies on a notion of subjunctive dependence that is not yet as well understood as causal dependence. CDT can use Pearl’s machinery for causal graphs. P-FDT can borrow the intervention notation, but it needs a graph that includes logical, mathematical, computational, and predictor-like dependencies. The source says that deducing this structure from observation is perhaps the largest open problem for FDT. P-FDT inherits that problem.

I have also added several operational assumptions:

1. **Policy evaluation is usually updateless.** When observations are affected by predictors of the agent’s policy, P-FDT should not condition the policy choice on the actual observation. Instead, it chooses a policy from the prior model and then applies the observation.

2. **Exogenous evidence may be conditioned on.** If new evidence is not downstream of the policy node and was not already represented in the problem, P-FDT may condition on it. The difficult task is distinguishing exogenous evidence from observation variables that are themselves policy-sensitive.

3. **Off-path observations should often not trigger policy revision.** If an agent following a good policy finds herself at an observation that the policy made improbable, she should often continue executing the policy. To abandon the policy whenever a bad observation appears may make one exploitable.

4. **The policy space may be restricted by feasibility.** Real agents cannot consider all functions from histories to actions. P-FDT as a normative theory can maximize over a feasible set \(\Pi\). The source’s idealized agents maximize over simple finite action sets; realistic P-FDT will require approximation.

5. **Stochastic policies can be included if needed.** The source does not say whether policies must be deterministic. In expected utility maximization, deterministic policies are often sufficient when no other agent needs to be randomized against, but in game-theoretic settings stochastic policies may be relevant. One can let \(\Pi\) include probability distributions over actions for each input.

These assumptions are not explicit in the footnote, but they seem necessary to make P-FDT usable.

---

## Conclusion

**P-FDT** is the policy-level version of functional decision theory. Its guiding question is not “Which physical act should I perform?” but “Which policy should this very decision procedure output?” The agent evaluates policies by intervening on a policy-output variable in a world-model that includes subjunctive dependencies: predictors, copies, simulations, and other agents whose behavior tracks the agent’s decision procedure. She then applies the chosen policy to her actual observations.

This approach preserves the attractive features attributed to FDT in the source: one-boxing in Newcomb’s problem, smoking in the smoking lesion problem, paying in Parfit’s hitchhiker-like cases, one-boxing in transparent Newcomb problems, and refusing blackmail when refusal makes blackmail unprofitable. The policy formulation makes especially clear why the agent should sometimes act as if she had precommitted to a plan: the plan itself is the object of evaluation.

The theory remains incomplete. It needs a satisfactory account of subjunctive dependence, counterpossible reasoning, and the construction of dependency graphs from evidence. But as a normative ideal, P-FDT offers a coherent and mathematically intelligible rule: choose the policy whose logical output would make the world best, then follow it.

---

## References

Soares, N., and Yudkowsky, E. “Functional Decision Theory: A New Theory of Instrumental Rationality.” arXiv:1710.05060v2. Primary source for FDT and footnote 16 policy formulation.

Pearl, J. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000. For causal intervention notation used by the source.

Joyce, J. M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999. For the expected-utility framework referenced by the source.