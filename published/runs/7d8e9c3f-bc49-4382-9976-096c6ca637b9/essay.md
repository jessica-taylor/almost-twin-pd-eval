# P-FDT: Choosing Policies in a World That Predicts You

A decision can matter through more than its immediate physical consequences. Someone may already have predicted it; another agent may be running the same computation; a prospective partner may cooperate only if they expect reciprocation. These dependencies challenge an account of rational choice that considers only what an isolated bodily action would cause.

**Policy functional decision theory (P-FDT)** evaluates a larger object: a policy mapping inputs to actions. Its central question is:

> Which policy would yield the best expected outcome, accounting for the processes that depend on which policy this very decision procedure selects?

The primary source for this formulation is footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality*. It describes their preferred formulation as intervening on the decision-function node to “choose not an action but a policy which maps inputs to actions,” after which the agent applies its inputs to that policy. Footnote 7 likewise identifies policies as mappings from observations to actions.

Most of the paper develops an **action-selection FDT** formulation instead. Its discussion of dependencies and counterfactuals supplies essential background, but its displayed action-selection equation is not itself a complete definition of P-FDT. The account below therefore separates the source’s central commitment—functional policy selection—from additional modeling assumptions needed to make it operational.

## 1. The object of choice

Begin with a finite, single-decision problem. Let:

- \(\mathcal X\) be the possible inputs or observations;
- \(\mathcal A\) be the available actions;
- \(\mathcal O\) be the outcomes;
- \(U:\mathcal O\to\mathbb R\) be the agent’s utility function.

A deterministic policy is a function
\[
\pi:\mathcal X\longrightarrow\mathcal A.
\]
Write \(\Pi\subseteq\mathcal A^{\mathcal X}\) for the admissible policies. In a sequential problem, inputs can instead be observation histories, so a policy specifies an action at every relevant history.

Choosing a policy is not merely choosing today’s action under another name. Two policies can agree at the actual observation while differing elsewhere. Those differences may affect a predictor’s decision, another agent’s response, or which observation the agent receives.

Let \(D\) denote the P-FDT policy selector, and let \(M\) be its evaluation model, including utilities and relevant dependencies. Its output is a policy:
\[
D(M)=\pi^*.
\]
Execution then takes the form
\[
a=\pi^*(x).
\]

The distinction between **selection** and **execution** is crucial. P-FDT does not generally maximize a fresh, ordinary conditional expectation separately at each observed \(x\). It evaluates alternative mappings, then uses the selected mapping to respond to \(x\).

Nor does policy selection require a physical commitment device. A predictor might model the selection computation before its policy is physically executed. P-FDT aims to account for that relationship without requiring a contract, brain modification, or binding promise.

## 2. A mathematical evaluation rule

P-FDT needs a model of what would happen under alternative outputs of its policy-selection computation.

Introduce a model variable \(\boldsymbol{\Pi}_M\) representing the mathematical output \(D(M)\). This variable is distinct from the policy actually returned. Let
\[
K_M(o,x;[\boldsymbol{\Pi}_M\leftarrow\pi])
\]
denote the hypothetical distribution over outcomes and observations obtained by setting that output to \(\pi\) and propagating the relevant dependencies.

An operational P-FDT rule is
\[
V_M(\pi)
=
\sum_{x\in\mathcal X}\sum_{o\in\mathcal O}
K_M(o,x;[\boldsymbol{\Pi}_M\leftarrow\pi])U(o),
\]
\[
\pi^*\in\operatorname*{arg\,max}_{\pi\in\Pi}V_M(\pi),
\qquad
a=\pi^*(x_{\mathrm{actual}}).
\tag{1}
\]
A fixed tie-breaking convention completes the selector.

Equation (1) is my reconstruction of the footnote’s proposal, not an equation explicitly supplied there. It exposes the required ingredients: candidate policies, utilities, an evaluation model, and a rule for constructing functional counterfactuals.

A useful special case employs background uncertainty \(W\sim\mu\). Suppose the hypothetical world is described by
\[
X=h(\pi,W),\qquad
A=\pi(X),\qquad
O=g(\pi,X,A,W).
\]
Then
\[
V_M(\pi)
=
\mathbb E_{W\sim\mu}
\left[
U\!\left(
g\bigl(\pi,h(\pi,W),\pi(h(\pi,W)),W\bigr)
\right)
\right].
\tag{2}
\]

The dependence of \(h\) and \(g\) on \(\pi\) can represent a predictor’s response or another implementation of the same computation. It must not be inserted merely because doing so favors a desired answer. These functions encode substantive claims about the problem.

This construction assumes a well-defined hypothetical outcome for each policy and background state. Sequential interactions, circular predictions, or multiple equilibria require additional semantics. The footnote does not provide them.

## 3. Which dependencies should change?

The paper’s key concept is **subjunctive dependence**: dependence that should persist when evaluating alternative outputs of a computation.

Three relationships must be distinguished.

**Causal dependence.** If an agent presses a switch, a lamp illuminates. Changing the policy can change the action and its downstream effects.

**Computational dependence.** If two systems implement the same policy-selection computation on the same selection inputs, their selected policies correspond. A sufficiently accurate predictor can exhibit a weaker version of this relationship.

**Merely evidential association.** An action may reveal something without changing it under the relevant counterfactual. A medical condition could influence both a preference and a health outcome without the health outcome depending on the conclusion of the agent’s deliberation.

P-FDT preserves the first two kinds of dependence where justified; it does not automatically preserve every correlation.

This distinguishes it from evidential decision theory (EDT), whose standard action evaluation uses
\[
\mathbb E[U(O)\mid X=x,A=a],
\]
and causal decision theory (CDT), whose standard evaluation uses
\[
\mathbb E[U(O)\mid X=x,\operatorname{do}(A=a)].
\]

P-FDT instead varies the output of the policy-selection computation. Consequently, the action, a prediction, another agent’s selected policy, and even the observation received may vary together.

None of this requires backward physical causation. Comparing a hypothetical in which a predictor previously anticipated a different policy does not mean believing that executing an action now sends a signal into the past.

There is nevertheless a foundational difficulty. A fixed mathematical procedure has a fixed output on fixed inputs. Alternative-output suppositions can therefore be **counterpossibilities**, not ordinary possible worlds. The paper openly acknowledges that a general account of these counterfactuals remains unfinished. A dependency model makes particular examples calculable; it does not solve that foundational problem.

## 4. Observations, policies, and the evaluation perspective

Suppose a driver rescues someone only if they predict that the passenger will pay afterward. Once the passenger reaches the city, paying has no remaining physical benefit. Why should a policy-based calculation still favor payment?

Because reaching the city is itself affected by the predicted policy.

The policy
\[
\pi_{\mathrm{pay}}(\text{city})=\text{pay}
\]
can produce rescue followed by payment. The policy
\[
\pi_{\mathrm{refuse}}(\text{city})=\text{refuse}
\]
can produce abandonment. Holding rescue fixed while comparing these policies removes the very dependency that makes payment valuable.

This suggests an operational interpretation: evaluate policies within a reference model that includes the process generating the observations, rather than automatically conditioning that process on the actual observation before every comparison.

That interpretation fits the source’s broader discussion, but footnote 16 leaves important choices unresolved:

- Which information belongs in the reference model?
- How broadly does the selected policy range?
- When should new evidence change the evaluation model itself?

I propose a **problem-relative evaluation frame**: include the uncertainties, observations, and dependencies belonging to the decision problem being analyzed. This is not necessarily a policy for the agent’s entire lifetime, nor a demand to retain a primordial prior forever.

The distinction is between *believing what has happened* and *choosing which counterfactual comparison evaluates a policy*. A passenger can be certain they are in the city while evaluating a refusal policy under which they would probably never have arrived.

But observations can also reveal model errors. A threatening letter might show that an alleged predictor is unreliable, or that an attack is unavoidable. P-FDT should not preserve a discredited model merely to sustain an earlier recommendation. Exactly how to distinguish observation-dependent execution from warranted revision of the evaluation frame remains an important open issue.

## 5. P-FDT in Newcomb’s problem

An opaque box contains \(m\) dollars if a predictor predicts one-boxing, and nothing otherwise. A transparent box contains \(b\) dollars.

For illustration, assume a symmetric functional prediction channel:
\[
P(\text{predict one}\mid[\pi_{\mathrm{one}}])=q,
\qquad
P(\text{predict one}\mid[\pi_{\mathrm{two}}])=1-q.
\]
This assumption is stronger than merely knowing the predictor’s historical average accuracy. It specifies how predictions vary across the policy counterfactuals.

The policy values are
\[
V(\pi_{\mathrm{one}})=qm,
\]
\[
V(\pi_{\mathrm{two}})=(1-q)m+b.
\]
Thus P-FDT selects one-boxing exactly when
\[
(2q-1)m>b.
\]

With \(q=0.99\), \(m=1{,}000{,}000\), and \(b=1{,}000\), the values are \(990{,}000\) and \(11{,}000\).

Contrast the paper’s imaginary smoking-lesion problem. Suppose smoking yields benefit \(s>0\), while cancer is entirely unaffected by smoking or by the policy-selection output. Holding the health distribution fixed gives
\[
V(\pi_{\mathrm{smoke}})
-
V(\pi_{\mathrm{refrain}})
=s.
\]
P-FDT selects smoking under those stipulated conditions. This is not a claim about real smoking, which causes serious disease.

The contrast illustrates the method: preserve the predictor’s response to the selected policy, but do not treat an ordinary medical common cause as though it were predicting that policy. The paper also acknowledges substantial complications in making the smoking-lesion story internally realistic.

## 6. P-FDT with transparent boxes and rescue

In transparent Newcomb, the predictor fills the large box if they predict that the agent would leave the small box behind **upon seeing the large box full**.

A policy must specify both branches:
\[
\pi(\text{full}),\qquad \pi(\text{empty}).
\]
Consider
\[
\pi_R(\text{full})=\text{one-box},
\qquad
\pi_R(\text{empty})=\text{two-box}.
\]
Under perfect prediction, this policy produces a full box and payoff \(m\). A policy that two-boxes upon seeing a full box instead produces an empty large box and, at best, payoff \(b\).

P-FDT therefore selects the former response to a full box when \(m>b\). Seeing the money does not initiate a separate policy evaluation that holds the money fixed while abandoning the predicted response.

Parfit’s hitchhiker has the same structure. Let rescue have utility \(r\), and payment cost \(c\), with \(r>c>0\). Under perfect prediction,
\[
V(\pi_{\mathrm{pay}})=r-c,
\qquad
V(\pi_{\mathrm{refuse}})=0,
\]
taking abandonment as the baseline.

The selected policy pays after rescue. Its justification is not that paying now physically causes an earlier rescue, but that the driver’s earlier decision depends on the predicted city-response component of the policy.

These recommendations are conditional on the dependency model. A driver who rescues indiscriminately supplies no prediction-based reason for payment, although contractual, moral, or reputational considerations may independently matter.

## 7. P-FDT and imperfect blackmail

Policy evaluation does not reduce to “always keep promises” or “always resist threats.” It depends on quantitative consequences.

Suppose a blackmailer attacks every agent predicted to pay. Payment costs \(c\); refusing an initiated attack causes loss \(L\). Assume:

- a paying policy is attacked with probability \(1\);
- a refusing policy is mistakenly attacked with probability \(\varepsilon\);
- otherwise, no attack occurs.

Then
\[
V(\pi_{\mathrm{pay}})=-c,
\qquad
V(\pi_{\mathrm{refuse}})=-\varepsilon L.
\]
P-FDT refuses precisely when
\[
\varepsilon L<c.
\]

For \(L=1{,}000{,}000\), \(c=1{,}000\), and \(\varepsilon=0.0009\), refusal loses \(900\) in expectation, less than payment’s \(1{,}000\).

An agent executing that policy may occasionally receive a letter and suffer the larger loss. The policy was selected for its expected consequences, not because every realized branch is favorable.

If attacks are independent of the policy, however, refusal supplies no deterrence. With an unavoidable attack and \(c<L\), this model favors payment. P-FDT’s recommendation changes when the dependency changes.

## 8. Why whole policies matter in multi-agent problems

Footnote 16 says that policy selection can matter in multi-agent dilemmas, without supplying a worked example. The following illustration is my own.

Two software agents share the same policy-selection computation and evaluation model. One receives input \(0\), the other input \(1\), with each assignment equally likely from either agent’s evaluation perspective. They cannot communicate after receiving their inputs.

Each receives \(10\) utility if their actions differ, and \(0\) otherwise. Taking action \(1\) additionally costs the actor \(1\).

A shared policy is represented by
\[
(\pi(0),\pi(1)).
\]
Because the agents’ selectors implement the same computation, varying its selected policy varies both agents’ policy implementations. The expected individual values are
\[
\begin{array}{c|c}
\text{Policy}&\text{Expected utility}\\ \hline
(0,0)&0\\
(1,1)&-1\\
(0,1)&9.5\\
(1,0)&9.5
\end{array}
\]
A shared tie-breaker can select \((0,1)\), giving complementary actions without communication.

The lesson is not that similar agents must take identical actions. Identical **policies** can prescribe different actions on different inputs. The dependency concerns the selected mapping; actual behavior depends on which input each implementation receives.

Conversely, merely knowing that another agent endorses P-FDT does not establish a shared policy output. Different models, utilities, roles, or tie-breakers can break the correspondence. Multi-agent analysis must identify the actual computational relationship rather than infer coordination from a theory’s name.

## 9. Applying P-FDT responsibly

For an unfamiliar problem, a practical analysis proceeds through five questions.

**First, what is the policy’s domain?** Include the observations or histories that predictors and other agents may distinguish. Specify admissible actions even at currently unobserved inputs.

**Second, what exactly is being predicted or replicated?** Distinguish another implementation of the same selection computation from an agent with merely similar behavior.

**Third, what changes under each policy counterfactual?** Propagate actions, predictions, observation-selection effects, and ordinary causal consequences. Keep unrelated background uncertainty fixed.

**Fourth, what is the evaluation frame?** State which information is incorporated into the model and which observations are generated within its policy comparisons. This choice can be decisive.

**Fifth, how robust is the answer?** Vary prediction accuracy, modeling assumptions, and policy scope. If plausible dependency models recommend different policies, the decision-theoretic label alone does not settle the case.

Several unresolved issues deserve emphasis.

A policy is extensionally a mapping, but predictors may inspect source code, proofs, or runtime behavior. Two programs implementing the same mapping need not be interchangeable in such environments. The model must say whether representations matter.

Randomization also requires specification. Selecting a distribution over actions differs from selecting a deterministic policy using a shared pseudorandom seed. Whether a predictor sees the seed can change the result.

Finally, useful consequences require qualifications. Additional information cannot lower the maximum policy value when the enlarged policy space permits ignoring it and the environment is otherwise unchanged. But this elementary policy-space argument does not establish unrestricted claims about information, self-modification, or reflective stability in every predictive environment.

The source presents broad motivations for such claims, while acknowledging unresolved counterfactual foundations and the absence of a general optimality theorem. Its informal distinction between “fair” and “unfair” problems is likewise not a completed universal performance criterion.

## Reference

Yudkowsky, Eliezer, and Nate Soares. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2. Primary passages: footnotes 7 and 16; supporting discussion in §§3, 5, and 9.

## Conclusion

P-FDT evaluates policies as outputs of a computation embedded in a world that may predict or replicate it. It compares entire observation-to-action mappings while preserving justified causal and computational dependencies—not every statistical association, and not merely the consequences of an isolated physical action.

Given a specified policy space, evaluation frame, and functional counterfactual model, its expected-utility calculation is straightforward. The difficult work lies in justifying those ingredients. P-FDT is therefore both a usable framework for carefully modeled problems and an unfinished account of how such models should be constructed.