# P-FDT: choosing the policy behind the action

Suppose a predictor has placed money in a box based on what it expects you to do. The box has already been filled or left empty. Your physical action cannot change the past, but the predictor’s earlier decision may nevertheless be systematically related to the reasoning you perform now.

**Policy functional decision theory (P-FDT)** takes that relationship seriously. Rather than evaluating an action only by its causal consequences, it evaluates alternative outputs of a decision procedure, allowing predictions, simulations, and other implementations of related reasoning to vary with that output. In the policy formulation, the output being varied is not merely an action but a rule mapping possible inputs to actions.

The primary source for this formulation is footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory*. The paper develops an action-level formalization in its main text. The footnote says that the authors’ preferred formulation instead intervenes on the decision-procedure node to choose “not an action but a *policy* which maps inputs to actions,” and then applies the agent’s inputs to that policy. The authors say that, as far as they can tell, the distinction matters only in multi-agent dilemmas, and set it aside in the paper.

That footnote gives the central architecture of P-FDT, but not a complete algorithm. In particular, it does not fully specify which inputs a policy covers, how observations affect policy evaluation, or how to construct logical counterfactuals. The account below distinguishes the paper’s principles from an operational interpretation that fills in some of those gaps.

## 1. From acts to policies

Let \(X\) be a set of possible information states and \(A(x)\) the actions available at \(x\). A deterministic policy is a function

\[
\pi:X\longrightarrow \bigcup_{x\in X} A(x),
\qquad \pi(x)\in A(x).
\]

For example, in transparent Newcomb’s problem, the agent observes whether the large box is full. A policy specifies both what to do when it is full and what to do when it is empty:

\[
\pi(\text{full})=\text{one-box},
\qquad
\pi(\text{empty})=\text{two-box}.
\]

A policy is therefore richer than the action it prescribes on the current input. Two policies can agree about what to do now while disagreeing about what to do in another state. That distinction matters when a predictor, a future self, or another agent reacts to the wider rule.

The intended sequence in footnote 16 is:

1. Evaluate candidate policies as alternative outputs of the decision procedure.
2. Select a policy according to its expected utility under the corresponding functional counterfactual.
3. Apply the selected policy to the agent’s input.

The second step is not simply “choose an action and write a policy around it.” The entire selected mapping can matter in the hypothetical. Nor does P-FDT merely ask which existing program should replace the agent. The source’s functional idea is to ask how *this decision procedure* should conclude: what if its output were a different policy?

This distinction is philosophical as well as technical. If a predictor has modeled the decision procedure, replacing the physical agent’s software while holding the predictor’s model fixed can destroy the very relationship under examination. A functional counterfactual instead tries to preserve the relevant relationship between the procedure and processes that model or implement it.

## 2. The counterfactual model

Let \(M\) represent an agent’s probabilistic model, augmented with information about relevant dependencies. Let \(D\) denote the policy-selection procedure, and let the model contain a node representing its output:

\[
\Pi_D=D(M).
\]

This is a schematic notation: the footnote does not specify exactly what arguments \(D\) receives. For each candidate policy \(\pi\), construct a hypothetical model by intervening on that output:

\[
M^\pi := M\bigl[\operatorname{do}(\Pi_D=\pi)\bigr].
\]

A natural policy-level analogue of the paper’s graphical rule is then

\[
\pi^* \in
\underset{\pi\in\mathcal P}{\operatorname{argmax}}\;
\mathbb E_{M^\pi}[U(O)],
\qquad
a=\pi^*(x),
\tag{1}
\]

where \(\mathcal P\) is the candidate policy class, \(O\) is the resulting outcome, \(U\) is utility, and \(x\) is the input presented to the selected policy.

Equation (1) is **an interpretation**, not an equation stated in footnote 16. It makes the footnote operational by extending the paper’s action-level graphical construction to policy outputs. It also leaves important work inside the notation: \(M^\pi\) must say what changes when the policy output is set to \(\pi\).

The source calls the relevant relation **subjunctive dependence**. It includes ordinary causal dependence but is broader. A predictor’s report can depend on a decision procedure even though the report was made before the agent acted. A duplicate running the same procedure can depend on it without either physical agent causing the other’s action. By contrast, a correlation caused by an unrelated common cause need not persist when the procedure’s output is varied.

A graphical model can represent this distinction. For example:

\[
\Pi_D \longrightarrow \text{prediction}
\longrightarrow \text{box contents},
\qquad
\Pi_D \longrightarrow A=\pi(X).
\]

Intervening on \(\Pi_D\) propagates through both paths. The arrow to the earlier prediction is not a claim that the present action sends a signal backward in time. It records a dependence in the hypothetical model: a predictor that accurately models the procedure would predict differently if that procedure had a different output.

The resulting hypothetical is a tool for evaluation, not necessarily a possible world in the ordinary logical sense. If the deterministic procedure actually outputs \(\pi^*\), then the assertion that it outputs a different \(\pi\) is false as a matter of computation. P-FDT therefore needs **counterpossible** reasoning: disciplined reasoning under a logically false antecedent. The paper explicitly acknowledges that there is no settled general account of how to construct such counterfactuals or infer all the relevant dependencies.

## 3. What changes—and what does not?

Three kinds of relationship should be kept separate.

**Causal effects.** If a policy tells an agent to press a button and pressing it opens a door, the door’s state changes in the policy hypothetical.

**Predictive or computational links.** If a reliable predictor determines its behavior by modeling the policy, its prediction changes according to that predictive mechanism. Perfect copies of the same policy-selection computation change together in the model.

**Mere correlations.** If an underlying condition makes both an action and an outcome more likely, changing the decision procedure’s output need not change that condition. The correlation may disappear in the hypothetical.

This gives a contrast with two familiar theories. **Evidential decision theory (EDT)** evaluates an action using a conditional expectation such as

\[
\mathbb E[U\mid X=x,A=a].
\]

That can treat an action as evidence about an external condition even when choosing the action would not change the condition. **Causal decision theory (CDT)** instead uses a causal intervention on the physical act, roughly

\[
\mathbb E[U\mid X=x,\operatorname{do}(A=a)].
\]

It preserves the act’s causal consequences but ordinarily holds an earlier prediction fixed. P-FDT intervenes on a policy-producing computation and propagates changes through the relevant functional as well as causal dependencies.

These are different ways to construct decision hypotheticals, not necessarily different beliefs about the actual world. A P-FDT agent can believe both that a box is already full and that its policy counterfactual for two-boxing usually has an empty box.

### A smoking-lesion illustration

In the paper’s imaginary smoking-lesion problem, smoking gives the agent positive utility and does not cause cancer. A lesion can cause both a desire to smoke and cancer. If the agent’s policy changes from smoking to refraining, the lesion does not thereby change, and neither does its effect on cancer. Under those assumptions, P-FDT smokes when smoking is valued.

A naive EDT calculation might instead regard smoking as bad news about the lesion and refrain. The paper notes that the example requires care: correlations between an agent’s own act and hidden preferences must be made consistent with the agent’s knowledge and decision procedure. It also notes EDT refinements that can address this particular case. The important P-FDT point is narrower: do not preserve a correlation merely because it appears in an observational distribution; identify the mechanism that would or would not transmit a policy intervention.

## 4. P-FDT in Newcomb’s problem

A transparent box contains \$1,000. An opaque box contains \$1,000,000 if a predictor predicted that you would take only the opaque box; otherwise it is empty. Assume that, under either candidate output, the predictor is accurate with probability \(q\).

For this one-observation problem, policies can be identified with their prescribed actions. If P-FDT one-boxes, the functional hypothetical gives expected utility

\[
V(\text{one-box})=q(1{,}000{,}000).
\]

If it two-boxes, the opaque box is full only when the predictor errs:

\[
V(\text{two-box})
=(1-q)(1{,}000{,}000)+1{,}000.
\]

At \(q=0.99\), these values are \$990,000 and \$11,000. P-FDT therefore one-boxes in this model. More generally it one-boxes when

\[
(2q-1)1{,}000{,}000>1{,}000.
\]

The threshold depends on the assumed counterfactual accuracy for *each* policy. A predictor’s reported historical success rate alone may not justify symmetric accuracy under every alternative. Applying P-FDT requires a model of how the predictor works, not just the assertion that “prediction” occurs.

CDT’s familiar objection is that, whatever is already in the opaque box, taking the extra \$1,000 is better. P-FDT does not deny that causal comparison. It denies that holding the prediction fixed is the appropriate comparison for choosing the output of a procedure that the predictor modeled. Conversely, the fact that P-FDT performs well here does not prove it universally optimal: a different environment could reward two-boxers or punish agents for their decision procedure.

## 5. Observations, policy selection, and transparent boxes

The policy formulation becomes especially interesting when observations themselves can depend on the selected policy. In transparent Newcomb, the predictor fills the large box if it predicts that the agent would one-box **upon seeing it full**. The agent then sees whether it is full.

Take two policies:

\[
\begin{array}{c|cc}
 & \text{full} & \text{empty}\\ \hline
\pi_1 & \text{one-box} & \text{two-box}\\
\pi_2 & \text{two-box} & \text{two-box}
\end{array}
\]

Suppose the predictor correctly predicts the full-box response with probability \(0.99\). Under \(\pi_1\), the box is usually full; if it is mistakenly empty, the agent takes the small box. Thus

\[
V(\pi_1)=0.99(1{,}000{,}000)+0.01(1{,}000)
=990{,}010.
\]

Under \(\pi_2\), the box is usually empty, although an erroneous prediction occasionally makes it full:

\[
V(\pi_2)=0.01(1{,}001{,}000)+0.99(1{,}000)
=11{,}000.
\]

On this model, P-FDT selects \(\pi_1\), and an agent seeing a full box one-boxes.

Here a choice left open by footnote 16 matters. Equation (1) evaluates whole policies against a distribution that allows the observation to vary with the policy. That resembles the source’s main-text treatment: its action-level functional counterfactuals can include different observations from the one actually received. If, instead, one conditions on “full” *after* each policy intervention, the comparison can discard the advantage of being predicted to one-box and favor taking both boxes.

My proposed operational interpretation is therefore to distinguish two sorts of information:

* **Background information** used to define the decision problem and its probability model may be incorporated before policy evaluation.
* **Inputs whose occurrence can depend on the policy** remain variables in the policy counterfactual; the selected policy specifies what to do for each such input.

This is a principled way to reproduce the source’s treatment of transparent Newcomb. It is not a complete solution to the observation problem. The footnote does not tell us exactly where to draw the boundary between background information and policy inputs, or whether the same policy selection should be recomputed at every information state. Different choices can give different answers. A careful application should state that boundary rather than silently treating all observed facts as either fixed or variable.

The same issue appears in Parfit’s hitchhiker. A driver rescues a stranded person only if she predicts payment after arrival. A policy that pays upon arrival can be preferable because it leads to rescue; a policy that refuses can lead to being left behind. Once safely in town, paying cannot physically cause the earlier rescue. P-FDT’s case for payment concerns the policy-dependent whole scenario, not retrocausation.

## 6. Why the whole policy can matter between agents

Consider two agents running the same policy-selection computation but receiving different role labels. Their common policy has two entries:

\[
\pi(L),\qquad \pi(R).
\]

Both receive 10 if the left-role agent chooses \(A\) and the right-role agent chooses \(B\); otherwise both receive 0. Each cares only about its own payoff. The policy

\[
\pi(L)=A,\qquad \pi(R)=B
\]

coordinates them, whereas the constant policies \(A,A\) and \(B,B\) do not.

Under an exact shared-output assumption, a P-FDT intervention on the common policy determines both agents’ actions on their respective inputs. It can select the role-sensitive policy and obtain 10 for each. This is not a claim that agents with different inputs must take identical actions. Sharing a policy can produce coordinated *different* actions.

It is also not a license to assume that any similarly described agents share a policy node. In a real interaction they may have different objectives, models, observations, code, or random seeds. Those differences may make their policy outputs only partially related or independent. A graph that links them without justification manufactures coordination.

For the paper’s psychological-twin prisoner’s dilemma, the idealization is stronger: each twin reasons in the same way on the same relevant input. If both cooperate each receives \$1,000,000; if both defect each receives \$1,000. Under exact functional linkage, P-FDT compares those two matched outcomes and cooperates. Against an independently deciding opponent whose action does not vary with the policy intervention, that argument does not apply.

Randomization requires similar care. A policy may output a distribution over actions, but the model must specify whether agents share a random seed, use predictable pseudorandomness, or draw independent random values. Equal mixed policies do not by themselves imply equal realized actions.

## 7. A practical procedure—and its limits

For an unfamiliar case, the following is a useful P-FDT workflow:

1. **Specify inputs and policies.** List the observations or roles the policy may receive, available actions, and feasible mappings. Include off-path inputs if predictions or other agents may depend on them.
2. **Specify utility and uncertainty.** Give payoffs and probabilities, including predictor errors and uncertainty about other agents.
3. **Identify the policy-output node.** State which implementations, simulations, or predictions are linked to it, and which are merely correlated.
4. **Construct each policy hypothetical.** Set the node to a candidate policy, propagate relevant functional and causal dependencies, and allow policy-dependent observations to vary.
5. **Compare expected utilities.** Select a maximizing policy, with an explicit tie-breaking rule, and apply it to the actual input.
6. **Test the model.** Check sensitivity to predictor accuracy, policy class, observation treatment, and assumptions about shared computation.

The most difficult step is usually the third. Graphs do not discover their own logical arrows. The source explicitly treats finding a satisfactory account of subjunctive dependence as a major open problem. Self-reference adds another complication: the procedure reasons about a node representing its own output. The paper observes that self-representing programs can be constructed; that does not by itself prove that every proposed counterfactual model has a unique, consistent solution.

Nor does a policy formulation automatically guarantee perfect commitment or positive value of information in every imaginable model. The source argues for reflective stability and useful information, but footnote 16 does not supply a general theorem covering all policy spaces and dependency structures. For example, if an agent reselects its policy after receiving information using a different model or selection criterion, the new selection may not preserve the earlier plan. Whether that is a defect or a permitted feature depends on a more complete specification of P-FDT.

Finally, the paper’s broader claim that functional agents outperform rivals in “fair” dilemmas is a conjectural motivation, not a proven dominance result. The authors acknowledge that no decision theory wins in every constructed environment and that a precise definition of fairness remains open.

## Conclusion

P-FDT’s central move is to evaluate a **policy output of the decision procedure**, then apply that policy to the agent’s input. Its counterfactuals preserve relevant predictive, computational, and causal dependencies while breaking merely statistical correlations that lack the right mechanism.

Footnote 16 supplies that architecture rather than a finished calculus. A workable interpretation can extend the paper’s intervention model to whole policies, but must make explicit how it treats observations, linked agents, predictor errors, and counterpossible dependence. Those choices are not peripheral: they determine whether P-FDT’s attractive precommitment-like reasoning applies in a new case.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, version 2, especially §§3–6 and footnotes 7 and 16. <https://arxiv.org/abs/1710.05060v2>