# P-FDT: Choosing the Policy Behind the Action

A decision can influence an outcome without physically causing it. A predictor may have anticipated the decision yesterday; another agent may run the same computation elsewhere. Conversely, an action may correlate with something undesirable without offering any leverage over it. A useful decision theory must distinguish these relationships.

**Policy functional decision theory (P-FDT)** evaluates complete policies while preserving the dependencies between a policy-selection computation and the systems that implement or predict it. Its central question is: *Which policy would yield the best outcome if this very policy-selection procedure output it?*

The primary source for this account is footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality*. It describes their preferred formulation as choosing “not an action but a policy which maps inputs to actions,” then applying the agent’s inputs to that policy. Footnote 7 likewise identifies policies as mappings from observations to actions.

The paper does not itself introduce the label **P-FDT**. Here it names that preferred policy-selection formulation, distinguished from the paper’s simplified, action-selection presentation. The footnotes specify the object of choice, but not a complete mathematical theory. Below, I separate that commitment from an operational interpretation developed using the surrounding discussion.

## 1. The mathematical object P-FDT chooses

Consider a finite decision problem with:

- an input space \(\mathcal X\), containing observations, roles, or observation histories;
- an action space \(\mathcal A\);
- an outcome space \(\mathcal O\);
- a utility function \(u:\mathcal O\to\mathbb R\);
- a world-model \(M\), representing uncertainty and relevant dependencies.

A deterministic policy is a function
\[
\pi:\mathcal X\longrightarrow\mathcal A.
\]
Let \(\Pi\) be the feasible policy set. Policies must respect information constraints: a policy cannot use an observation unavailable when its prescribed action must occur. For a sequential problem, inputs should therefore be histories, and policies should be complete contingent plans.

P-FDT has two conceptually distinct stages:

1. select a policy \(\pi_M^*\);
2. on receiving input \(x\), execute \(\pi_M^*(x)\).

Let \(\mathsf L_M\) denote a variable *inside the model* representing the mathematical output of the policy selector on model \(M\). Define
\[
Q_M(o;\pi)
=
P_M\!\left(
O=o\mid
\operatorname{do}_{\mathrm{sub}}(\mathsf L_M=\pi)
\right),
\]
where \(\operatorname{do}_{\mathrm{sub}}\) denotes a **subjunctive intervention**, explained below.

My proposed finite-model rule is
\[
\boxed{
\begin{aligned}
V_M(\pi)&=\sum_{o\in\mathcal O}Q_M(o;\pi)u(o),\\
\pi_M^*&=\operatorname*{arg\,max}_{\pi\in\Pi}V_M(\pi),\\
A(M,x)&=\pi_M^*(x).
\end{aligned}}
\]
Assume a fixed tie-breaking convention. For infinite outcome spaces, replace the sum with an appropriate, finite expectation.

This is expected-utility maximization. Its distinctive features are the policy-valued intervention and the interpretation of \(Q_M\).

Choosing a policy does not mean acquiring different values or becoming a different decision algorithm. The counterfactual concerns the output of the **existing selector**. Otherwise, a predictor of that selector might remain unchanged while the agent imagines replacing itself—destroying precisely the correspondence P-FDT seeks to preserve.

The notation is self-referential: the selector evaluates interventions on a representation of its own output. Representing such an output need not require knowing it in advance. Nevertheless, this observation does not establish that every proposed self-referential model has a satisfactory solution.

## 2. Which dependencies survive a P-FDT counterfactual?

The source calls the relevant relationship **subjunctive dependence**. Exact copies of a computation exemplify it: if both correctly compute the same function on the same input, their outputs must agree. Predictors supply approximate versions of this dependence.

A P-FDT hypothetical changes the policy-selector output and propagates that change through everything depending on it, while leaving unrelated background mechanisms unchanged.

For comparison:

- **Evidential decision theory (EDT)** evaluates actions using conditional expectations such as
  \[
  \mathbb E[u(O)\mid X=x,A=a].
  \]
- **Causal decision theory (CDT)** evaluates causal interventions on the physical action:
  \[
  \mathbb E[u(O)\mid X=x,\operatorname{do}(A=a)].
  \]
- **P-FDT** evaluates subjunctive interventions on the policy-selector output.

Conditioning on an action can alter beliefs about its causes. Intervening causally on that action ordinarily does not alter those causes. P-FDT likewise need not alter them—but it can alter an earlier prediction representing the same policy-selection computation.

This is not retrocausation. A P-FDT agent does not believe its present action sends a signal into yesterday. It compares hypothetical configurations in which a mathematical output, its predictions, and its implementations vary together.

One operational representation is a structural simulator. Draw background uncertainty
\[
Z\sim\mu_M,
\]
and, under candidate policy \(\pi\), calculate
\[
X^\pi=H_M(\pi,Z),\qquad
A^\pi=\pi(X^\pi),\qquad
O^\pi=F_M(\pi,Z).
\]
Then
\[
V_M(\pi)=\mathbb E_{\mu_M}[u(O^\pi)].
\]

Here \(H_M\) and \(F_M\) encode predictions, other agents, physical consequences, and observation generation. Their dependence on \(\pi\) must be justified, not invented to obtain an attractive answer. The model must also specify a well-defined evaluation—for example, an acyclic computation or another explicit resolution of any feedback.

This simulator is an implementation proposal, not a complete foundation supplied by footnote 16. The paper itself emphasizes the missing foundation: no general method is given for identifying all relevant logical dependencies.

Moreover, a deterministic selector has only one actual mathematical output. Asking what happens if it outputs another policy can therefore be **counterpossible**, not merely physically counterfactual. Ordinary Bayesian conditioning on a logically impossible output does not resolve this problem. The intervention notation marks the additional structure required; it does not conjure that structure into existence.

## 3. Information and the reference perspective

Policy selection raises an important ambiguity: **from which informational perspective are policies evaluated?**

Footnote 16 does not specify a prior, a policy horizon, or exactly which observations should be conditioned upon. Merely saying “choose policies” does not settle these questions.

My operational interpretation fixes a **reference problem model** \(M\), then evaluates complete policies before conditioning the objective on observations that the policy can subjunctively influence. Actual observations select an action *through the chosen policy*. They need not remain fixed across the policy’s evaluation hypotheticals.

Thus, generally,
\[
V_M(\pi)\ne
\mathbb E_M[u(O^\pi)\mid X^\pi=x].
\]
On the left, observations can differ between candidate-policy worlds. On the right, the evaluation insists on the actual observation \(x\).

This interpretation follows the surrounding discussion in section 9: an alternative decision can correspond to different observations, including not receiving a blackmail letter. But it is an additional specification of the policy formulation, not an equation stated in footnote 16.

Nor does it require suppressing evidence. The agent can believe, with certainty, “I received this letter.” Its decision evaluation can nevertheless compare policies under which letters arrive at different rates. **Beliefs about actuality and decision hypotheticals serve different purposes.**

Evidence legitimately incorporated into the reference model can change the optimal policy. However, repeatedly rebuilding the objective by conditioning on policy-dependent observations can undo the intended global evaluation. The source does not fully explain where the reference perspective should begin or when it should be revised. For applications, that boundary must be stated explicitly.

## 4. P-FDT in prediction problems

### Newcomb’s problem

An opaque box contains \(m=\$1{,}000{,}000\) if a predictor anticipated one-boxing, and nothing otherwise. A transparent box contains \(k=\$1{,}000\).

There is no informative execution input, so the relevant policies are constant: always one-box or always two-box. Assume the predictor tracks either candidate with symmetric accuracy \(p\), with the error mechanism held fixed across interventions. Then
\[
V_M(\pi_{\mathrm{one}})=pm,
\]
and
\[
V_M(\pi_{\mathrm{two}})=(1-p)m+k.
\]
P-FDT one-boxes exactly when
\[
(2p-1)m>k.
\]
At \(p=0.99\), the values are \(\$990{,}000\) and \(\$11{,}000\).

The accuracy assumption matters. An observed historical success rate alone does not establish these counterfactual probabilities. We need a model explaining how predictions respond to alternative selector outputs.

CDT instead holds the already-filled box fixed when intervening on the physical action, making the extra \(\$1{,}000\) decisive. The disagreement concerns which hypothetical dependence to preserve.

### A nonpredictive common cause

Now consider the paper’s fictional smoking-lesion setting: a lesion correlates with smoking and cancer, but smoking does not cause cancer.

If the agent values smoking at \(s>0\), and neither the lesion nor cancer depends subjunctively on its policy-selector output, then
\[
V_M(\pi_{\mathrm{smoke}})
-
V_M(\pi_{\mathrm{refrain}})
=s.
\]
P-FDT smokes. It does not preserve a correlation merely because that correlation exists observationally.

This is only the stipulated imaginary case. The paper also acknowledges substantial difficulties in formalizing its preference and self-knowledge assumptions. The useful lesson is structural: an ordinary disease-producing common cause is not automatically a predictor of the policy computation.

### Transparent boxes and rescue

Suppose both Newcomb boxes are transparent, and the predictor fills the large box iff it predicts that the agent will leave the small box upon seeing both full.

With a perfect predictor, consider
\[
\pi_C(\mathrm{full})=\mathrm{one},
\qquad
\pi_C(\mathrm{empty})=\mathrm{two}.
\]
This policy receives a full box and earns \(m\). Any policy taking both boxes when full induces an empty large box and earns at most \(k\). P-FDT therefore selects \(\pi_C\).

After observing fullness, execution still returns “one.” Reoptimizing while insisting that fullness remain fixed would change the evaluation rule.

Parfit’s hitchhiker has the same structure. A driver rescues the agent iff payment in the city is predicted. A pay-if-rescued policy can purchase survival; a refuse-if-rescued policy can prevent rescue. Payment is instrumentally justified by that dependency, without needing a moral utility bonus.

## 5. Why whole policies matter in multi-agent problems

The footnotes say that policy selection can matter in multi-agent dilemmas, but provide no worked example of the distinction. The following is an illustration of my operational interpretation.

Two copies use the same policy-selector computation and reference model. One receives input \(r\), the other \(b\). Each may contribute, action \(1\), or abstain, action \(0\). Each receives benefit \(10\) iff both contribute, and pays cost \(1\) iff it personally contributes.

A policy is a pair
\[
\pi=(a_r,a_b)\in\{0,1\}^2.
\]
Evaluate from a reference perspective assigning equal probability to being either copy. Because both copies implement the policy selected by the same computation,
\[
V_M(\pi)
=
10a_ra_b-\frac{a_r+a_b}{2}.
\]
Consequently,
\[
\begin{array}{c|rrrr}
\pi &(0,0)&(1,0)&(0,1)&(1,1)\\ \hline
V_M(\pi)&0&-\tfrac12&-\tfrac12&9
\end{array}
\]
P-FDT selects \((1,1)\).

Starting from \((0,0)\), improving one policy branch at a time fails: changing either branch alone costs money without producing the joint benefit. A whole-policy intervention makes the beneficial coordinated change available in one comparison.

This is not a proof that every action-selection formalization must fail; additional logical dependencies might coordinate its separate comparisons. It demonstrates what policy selection represents explicitly: jointly varying behavior on **different inputs**.

Crucially, the other copy changes because it implements the same selector output—not because P-FDT assumes universal cooperation. Against an unrelated agent whose behavior remains fixed under these interventions, unilateral contribution may be wasteful. Sharing a theory’s name, or having broadly similar goals, does not by itself establish computational identity.

## 6. P-FDT and imperfect blackmail

Policy evaluation is especially revealing when observations depend on predicted responses.

Suppose a blackmailer launches a damaging program when it predicts payment. Paying costs \(k\); refusing after launch causes loss \(L>k\).

Consider two policies:

- \(\pi_P\): pay upon receiving the demand;
- \(\pi_R\): refuse upon receiving it.

Assume payment is always correctly predicted, so \(\pi_P\) is always targeted. A refuser is mistakenly targeted with probability \(\varepsilon>0\). Then
\[
V_M(\pi_P)=-k,\qquad
V_M(\pi_R)=-\varepsilon L.
\]
P-FDT refuses exactly when
\[
\varepsilon L<k.
\]

For \(k=1{,}000\), \(L=1{,}000{,}000\), and \(\varepsilon=0.0009\), refusal loses \(900\) in expectation, versus \(1{,}000\) for payment. The policy therefore refuses even on the rare branch where a letter actually arrives.

The positive error probability matters: receipt is a genuine possible event, rather than an observation inconsistent with perfect prediction and predictable refusal.

P-FDT does not deny the local damage from refusal. Its claim is that the response policy partly determines whether that local situation arises. Conversely, if launch is independent of the policy and unavoidable, both policies face launch with probability one:
\[
V_M(\pi_P)=-k,\qquad V_M(\pi_R)=-L.
\]
P-FDT then pays. Resistance to blackmail is not an unconditional rule; it follows from the specified dependency structure.

## 7. Applying P-FDT to unfamiliar cases

A practical analysis should make five choices explicit.

**First, specify utility, inputs, and feasible policies.** Include off-path observations. A policy omitting what happens after a surprising letter or prediction error is incomplete.

**Second, locate the policy-valued computation.** Identify what selects the policy and which physical systems implement or model that selection. Do not replace this step with “everyone reasons similarly.”

**Third, specify intervention semantics.** For each alternative output, determine which predictions, actions, observations, and outcomes change. Preserve ordinary causal consequences as well as justified computational dependencies. Keep unrelated background uncertainty fixed in distribution.

**Fourth, state the reference perspective.** Identify what information belongs in \(M\) and what enters as an execution input. If different choices here yield different recommendations, report that sensitivity rather than presenting one answer as forced by footnote 16.

**Fifth, evaluate complete policies, then execute the selected branch.** An action is justified as \(\pi_M^*(x)\), not by a fresh maximization that silently changes the objective.

Several limitations remain.

A finite policy space may already contain
\[
|\mathcal A|^{|\mathcal X|}
\]
elements. Policy restrictions and approximate search are unavoidable in realistic problems, but can exclude the best contingent plan.

Randomized policies require further care. Predictable pseudorandomness, shared seeds, and genuinely private randomness generate different dependencies. A predictor may track a randomized policy’s distribution without predicting its realized action.

There is also a conditional value-of-information result. If a free signal merely enlarges the feasible policy space, old policies remain available by ignoring it. Therefore the maximum attainable value cannot decrease. But that argument assumes the signal does not otherwise change the environment or prediction mechanism; it is not an unrestricted theorem about every information-acquisition act.

Finally, no universal optimality claim follows from these examples. The source itself leaves both a general account of subjunctive dependence and a satisfactory formal characterization of “fair” decision problems unresolved. P-FDT is an evaluative framework whose success depends on those modeling foundations.

## Reference

Yudkowsky, Eliezer, and Nate Soares. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2. Primary passage: footnote 16; supporting discussion: footnote 7 and sections 3, 5, and 9. https://arxiv.org/abs/1710.05060v2

## Conclusion

P-FDT chooses a complete contingent policy by evaluating alternative outputs of the computation selecting it. Its counterfactuals preserve relevant predictions and implementations while breaking merely evidential correlations. Under the reference-model interpretation developed here, observations guide execution without automatically becoming fixed constraints on policy evaluation.

The resulting procedure is concrete once a policy space, reference perspective, and dependency model are supplied. What remains open is how to supply those ingredients generally—and how to justify them without building the desired answer into the model.