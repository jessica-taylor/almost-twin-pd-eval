# P-FDT: Choosing a policy as the output of a decision function

A decision can be viewed at two levels. At the first, an agent chooses a physical act: take one box or two, pay a driver or walk away, cooperate or defect. At the second, the act is the output of a rule that also specifies what the agent would do under other observations.

**Policy functional decision theory**, or **P-FDT**, evaluates decisions at the second level. It asks which policy the agent’s decision procedure should output, taking into account not only the physical consequences of executing that policy but also other events that depend on what the procedure outputs. Those events can include the conclusions of predictors and the actions of sufficiently similar agents.

The primary source for this essay is footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory*. It says that their preferred formulation intervenes on the decision-function node to choose “not an action but a policy which maps inputs to actions,” and then applies the agent’s inputs to the chosen policy. The main text instead develops an action-selection formulation for simplicity.

That footnote gives P-FDT its central idea but not a complete algorithm. It does not specify, for example, the policy space, the treatment of information received before policy selection, or how to identify all relevant logical dependencies. I will distinguish the paper’s claims from one operational interpretation designed to make the policy formulation usable.

## 1. From acts to policies

Let \(X\) be a set of possible observation histories and \(A(x)\) the actions available after history \(x\). A deterministic policy is a function

\[
\pi:X\longrightarrow A,\qquad \pi(x)\in A(x).
\]

For example, a policy for transparent Newcomb’s problem might say:

\[
\pi(\text{box full})=\text{take only the opaque box},\qquad
\pi(\text{box empty})=\text{take both boxes}.
\]

A policy specifies actions even at histories that do not actually occur. Such off-path entries matter when a predictor asks what the agent *would* do under a particular observation, or when another agent’s behavior depends on a simulation of that response.

Let \(\mathcal P\) be a specified set of admissible policies. For a finite problem, it might contain every mapping from histories to available actions. In a larger problem it may instead contain policies expressible within some computational or institutional constraint. The choice of \(\mathcal P\) is substantive: optimizing over a restricted set need not give the result of optimizing over all possible policies.

The paper models decision-making using expected utility. Let \(O\) be the outcome and \(U(O)\) its utility. Write \(D(M)\) for the policy output of the P-FDT procedure when supplied with a decision model \(M\). The precise inputs to \(D\) are themselves an open design choice; \(M\) can include beliefs, available policies, utilities, and a representation of dependencies.

A schematic policy-selection rule is

\[
\pi^*
\in
\operatorname*{arg\,max}_{\pi\in\mathcal P}
\mathbb E_M\!\left[
U(O)\mid \operatorname{do}(D(M)=\pi)
\right],
\qquad
a=\pi^*(x).
\tag{1}
\]

Here \(\operatorname{do}\) is not an ordinary observation that the procedure outputs \(\pi\). It denotes a *hypothetical intervention* on a model variable representing that output. Once the policy is selected, the agent applies it to its actual input \(x\), as footnote 16 prescribes.

Equation (1) is an interpretation, not an equation supplied by the footnote. In particular, the expectation must be taken relative to a suitably chosen informational perspective. If \(x\) is itself affected by which policy is selected—for example, if a predictor fills a box according to the policy—then simply conditioning every candidate on the actual \(x\) can erase the dependence P-FDT is supposed to evaluate. I will return to this choice below.

The key distinction is between a **policy-output intervention** and a change of one physical action. Under the intervention \(D(M)=\pi\), every modeled consequence of that output is recomputed: which observation occurs, what action the policy specifies there, and what a predictor or linked agent does insofar as its behavior depends on that output.

## 2. What changes in a P-FDT hypothetical?

The source calls the relevant relationship **subjunctive dependence**. It includes familiar causal dependence, but also computational and logical relationships. If two devices correctly compute the same function on the same input, their outputs are connected even when neither device physically affects the other. Similarly, an accurate predictor of an agent’s decision can depend on that decision procedure without receiving a signal backward through time.

This produces three different ways to evaluate a candidate action or policy:

- **Evidential decision theory (EDT)** asks what outcomes are probable *conditional on* the agent taking the action.
- **Causal decision theory (CDT)** evaluates a physical intervention on the action and propagates causal effects.
- **P-FDT** evaluates an intervention on the decision procedure’s policy output and propagates the modeled causal and other subjunctive dependencies.

A useful schematic representation is

\[
D(M)\longrightarrow \pi
\longrightarrow
\begin{cases}
\text{agent's actions},\\
\text{predictor's model},\\
\text{outputs of linked implementations}
\end{cases}
\longrightarrow O.
\]

These arrows need not all be causal arrows in the ordinary physical sense. In the paper’s graphical formalization, such a graph is supplied as part of the model. The graph tells the agent which variables change when it imagines a different output of its decision function. The paper acknowledges that it does not provide a general method for discovering or constructing the correct graph.

This distinction also explains what P-FDT does **not** say. It does not claim that choosing an action today physically changes yesterday’s prediction. Rather, when evaluating a different output of the procedure, it considers a hypothetical in which a sufficiently accurate prediction of that output differs too. Nor does it preserve every correlation involving the agent’s action: a correlation due to an unrelated common cause need not survive the policy intervention.

### Counterpossibilities

A fixed deterministic mathematical procedure on fixed inputs has one output. If it actually outputs \(\pi_1\), the supposition \(D(M)=\pi_2\) is, strictly speaking, contrary to a mathematical fact. P-FDT therefore uses a *counterpossible*: a structured hypothetical whose antecedent may be logically impossible.

The paper treats hypotheticals as tools for deliberation, not as ordinary beliefs that the counterpossible world exists. A graph can provide a local answer—“change this node and propagate these dependencies”—without providing a complete semantics for all impossible propositions. That is useful, but it leaves a real gap: an incorrect dependency graph can generate confident, incorrect prescriptions.

Self-reference adds another challenge. The procedure evaluates hypotheticals about the output of that very procedure. Representing its own code or output node is possible in principle, as the paper observes, but self-reference alone does not prove that a practical procedure terminates, has a unique maximizing policy, or has correctly modeled its logical relationships.

## 3. A P-FDT operational interpretation

To apply the footnote’s idea, I propose the following idealized procedure. It is a reconstruction, not a complete theorem of the source.

1. **Specify the decision problem.** Identify the agent’s utility, feasible policies, observation histories, relevant uncertainty, and the point of view from which policies are to be evaluated.

2. **Represent the policy-output node.** Include a node for the policy selected by the P-FDT computation. The agent’s action at a history is the selected policy applied to that history.

3. **Model dependencies.** Include physical consequences, predictors’ use of the policy or its outputs, and other implementations of relevant computations. Do not add links merely because two variables are correlated.

4. **Intervene policy by policy.** For each candidate \(\pi\), set the policy-output node to \(\pi\), hold background uncertainties fixed as appropriate, and recompute the dependent variables. A different policy can produce a different observation history.

5. **Calculate expected utility and act.** Compare the resulting outcome distributions, select a maximizing policy using a specified tie-breaker, and execute its action at the actual history.

The most delicate step is choosing the informational perspective. One reasonable interpretation is to retain background information that would remain fixed across the policy alternatives, while representing policy-dependent observations inside the model rather than conditioning on their actual values in every hypothetical. The paper’s action-based formulation handles observations by changing the decision-function node on which it intervenes; it does not simply condition on an observation that the intervention itself may change.

For P-FDT, the analogous boundary is not fully determined by footnote 16. If a new observation is independent of all policy alternatives and merely describes an external state, conditioning on it may be appropriate. If it resulted from a prediction of the policy, holding it fixed can remove the very consequence being evaluated. A complete theory needs a principled rule for this boundary, especially when evidence is only partly policy-dependent.

## 4. Newcomb’s problem and the lesion

In Newcomb’s problem, an opaque box contains \(\$1{,}000{,}000\) if a predictor predicted that the agent would take only that box. A transparent box contains \(\$1{,}000\). Suppose the predictor matches the relevant choice with probability \(0.99\), symmetrically for either candidate policy.

For constant policies, the P-FDT values are

\[
\begin{aligned}
V(\text{one-box})&=0.99(1{,}000{,}000)=990{,}000,\\
V(\text{two-box})&=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\end{aligned}
\]

P-FDT therefore one-boxes. The calculation assumes not merely that the predictor was 99% accurate on some historical population, but that its modeled response has these probabilities under the candidate policy interventions. Accuracy measured on a different population does not by itself establish that counterfactual response.

CDT instead holds the already-filled box fixed under a physical action intervention and finds that taking the extra \(\$1{,}000\) is better. EDT can one-box because taking one box is evidence that the predictor filled it. P-FDT’s reason differs from EDT’s: it represents the predictor as responsive to the decision procedure, not as an arbitrary source of favorable news.

Contrast the imaginary smoking-lesion problem. A lesion causes both a desire to smoke and a high cancer risk, but smoking itself does not cause cancer. If smoking gives the agent 1,000 units of utility and the lesion’s cancer mechanism does not depend on the policy output, then, for otherwise identical policies,

\[
V(\text{smoke})-V(\text{refrain})=1{,}000.
\]

P-FDT smokes under those assumptions. It does not treat smoking as a way of changing the lesion merely because smokers are statistically more likely to have it. EDT may refrain when it treats the act as evidence of the lesion, although, as the source notes, versions of EDT with additional self-knowledge or other modifications can avoid that result.

The lesson is not a rule that “prediction matters but correlation never does.” Statistical evidence helps the agent learn which dependency model is plausible. But an association alone does not specify what happens when the policy-output node is varied.

## 5. Policy entries, observations, and predictors

The policy formulation is especially helpful when a predictor cares about what an agent would do at a particular observation.

In transparent Newcomb, suppose the predictor fills the large box if and only if it predicts that the agent’s policy says **one-box upon seeing it full**. Assume, for simplicity, a perfect predictor. Compare two policies that both take the small box when the large box is empty:

\[
\begin{array}{c|cc}
 & \text{full} & \text{empty}\\ \hline
\pi_1 & \text{one-box} & \text{two-box}\\
\pi_2 & \text{two-box} & \text{two-box}
\end{array}
\]

Under \(\pi_1\), the predictor fills the large box, the agent sees it full, and receives \(\$1{,}000{,}000\). Under \(\pi_2\), the predictor leaves it empty, and the agent receives \(\$1{,}000\). Thus \(\pi_1\) is preferable in this model.

The actual agent may see a full box before applying \(\pi_1\). P-FDT does not require it to doubt that observation. Rather, in the policy comparison, the alternative policy changes what the predictor would have done and hence what the agent would have observed. If one conditions both alternatives on “full box” after modeling the predictor, one has instead asked which action is best *given a full box regardless of how it came to be full*. That is a different counterfactual question and yields the CDT-style temptation to take both.

This makes off-path policy entries important. Under \(\pi_2\), the “full” entry is never executed with a perfect predictor, but it is precisely the entry the predictor inspects. The fact that a contingency is unrealized does not make it irrelevant to the outcome.

Parfit’s hitchhiker has the same structure. A driver rescues a stranded agent if she predicts that the agent will pay upon arrival. A policy that pays in town can lead to rescue; a policy that refuses can lead to abandonment. P-FDT can therefore select the former even though, after arrival, payment is costly and cannot physically cause the earlier rescue.

## 6. Linked agents and the scope of a policy intervention

The paper says the policy/action distinction can matter in multi-agent dilemmas, without specifying all such cases. A simple model shows why the distinction can matter.

Suppose two copies use the same policy-selection computation and face different inputs, \(x_L\) and \(x_R\). Each chooses \(C\) or \(D\). The first agent’s payoff is

\[
u(C,C)=3,\quad u(C,D)=0,\quad
u(D,C)=5,\quad u(D,D)=1.
\]

Assume both copies implement the very same policy output \(\pi\), and the first agent evaluates its own payoff. Then

\[
V(\pi)=u\bigl(\pi(x_L),\pi(x_R)\bigr).
\]

The four policy entries give values \(3,0,5,1\), respectively. P-FDT selects the asymmetric policy

\[
\pi(x_L)=D,\qquad \pi(x_R)=C,
\]

and the first agent defects. A local intervention that changed only the output at \(x_L\), while holding the copy’s action at \(x_R\) fixed, would not in general evaluate this same set of joint consequences.

This is not a general prediction that P-FDT agents exploit one another. The example stipulates a shared policy selector optimizing the first agent’s payoff. If the two agents have different utilities, different role information, or separate policy-selection computations, their outputs need not be linked in this way. If each independently optimizes its own payoff while recognizing the other’s reasoning, the model may require an equilibrium or fixed-point analysis; a single shared argmax is not automatically justified.

The example illustrates an important discipline: **same code is not enough to identify the intervention’s scope**. One must ask whether the relevant computations have the same inputs, whether they output the same policy, whether one predicts another, and how their utilities enter the calculation. Similarity can support a probabilistic dependency rather than an identity. When the link is uncertain, it should be represented with probabilities, not asserted as perfect coordination.

## 7. Imperfect prediction and blackmail

A policy’s desirability can change sharply with predictor reliability. Consider mechanical blackmail: if a blackmailer predicts payment upon receiving a demand, she starts a process that will cause a loss \(L\), unless the agent pays \(c\).

Assume, as a simplified model:

- a policy of paying always triggers the demand and costs \(c\);
- a policy of refusing triggers the demand by error with probability \(\varepsilon\);
- when triggered under refusal, the process causes loss \(L\).

Then

\[
V(\text{pay})=-c,\qquad
V(\text{refuse})=-\varepsilon L.
\]

P-FDT refuses precisely when

\[
\varepsilon L<c.
\]

For \(L=\$1{,}000{,}000\) and \(c=\$1{,}000\), refusal is preferred when \(\varepsilon<0.001\), or \(0.1\%\). At a \(0.09\%\) error rate its expected loss is \(\$900\). At \(0.011\%\), it is only \(\$110\), so refusal is still preferred under these assumptions. The supplied paper says payment at \(0.011\%\); that appears inconsistent with its own numbers, rather than a result to carry over.

The conditional sacrifice is substantial: if the demand actually arrives despite a refusal policy, refusing causes the large loss in that realized case. The proposed calculation compares policies over the model’s full distribution, including the possibility that the demand would not have arrived. Whether that is the correct perspective after receiving surprising evidence is a central philosophical dispute, not a mathematical consequence of expected utility alone.

## 8. What P-FDT promises—and what remains open

The source motivates functional decision-making partly by its resemblance to advantageous precommitment. Before a predictor acts, an agent might pay to bind itself to a policy that later looks locally costly. P-FDT seeks to select that policy directly, without a separate binding device. This is an illuminating analogy, but it is not an identity: a real precommitment is a physical intervention, whereas a P-FDT policy comparison is a hypothetical intervention on a decision-function output. They agree only when the relevant models make their consequences agree.

The paper also argues that a policy-based global perspective avoids giving information negative value. There is a limited mathematical basis for that claim. If obtaining a free signal leaves all old policies available, and the agent may ignore the signal, then

\[
\max_{\pi\text{ using or ignoring signal}} V(\pi)
\geq
\max_{\pi\text{ ignoring signal}} V(\pi).
\]

But the conclusion depends on those assumptions. Acquiring information may itself be costly, reveal something to a predictor, change the available policies, or alter which computation is implemented. Footnote 16 alone does not prove non-negative value of information in every model.

Likewise, the source suggests that functional decision theory performs particularly well in “fair” problems, while acknowledging that fairness has not been given a satisfactory general definition. No decision rule can outperform every rival in every artificially constructed environment: an environment can reward a specified rival or punish a specified procedure. Success in the examples supports the P-FDT perspective but does not establish universal optimality.

For unfamiliar cases, the greatest practical uncertainties are therefore:

- **Policy domain:** Which histories and actions must the policy cover? Are randomization or resource limits allowed?
- **Dependency scope:** Which predictors, copies, and computations respond to the policy output, and how reliably?
- **Evidence:** Which observations remain fixed in a hypothetical, and which are consequences of the candidate policy?
- **Counterpossibles:** What licenses a particular graph or response model for an output that the actual computation cannot have?
- **Multiple agents:** Are agents evaluating one shared computation or several interdependent computations with different goals?
- **Selection:** Do a maximizing policy and an adequate tie-breaking or fixed-point rule exist?

A useful answer to a P-FDT problem should expose these assumptions rather than hide them inside the phrase “the predictor knows.” In simple cases, the assumptions may be explicit enough to calculate a clear result. In realistic ones, sensitivity analysis over plausible dependency models can be more informative than pretending that one graph is known with certainty.

## Conclusion

P-FDT evaluates a decision by considering alternative **policy outputs** of the agent’s own decision procedure, propagating the relevant causal and subjunctive dependencies, and applying the preferred policy to the actual input. Its distinctive appeal is that it can account for predictors and linked agents without treating every correlation as something an action controls.

Footnote 16 supplies the policy-selection idea, not a finished semantics. The operational rule developed here is one way to make it precise in idealized models. Its success depends on choices about policy scope, information, and counterpossible dependence—choices that remain part of the research problem.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, version 2, especially footnotes 7 and 16 and sections 3–6. https://arxiv.org/abs/1710.05060v2