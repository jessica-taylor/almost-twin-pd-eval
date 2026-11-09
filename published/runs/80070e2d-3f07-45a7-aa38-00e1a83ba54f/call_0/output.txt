# P-FDT: Choosing the Policy That Makes the Best World

A decision can matter without physically causing everything that depends on it. A predictor may already have anticipated it; another computer may be running the same calculation; a negotiating partner may have decided whether to approach us by modeling our response. **Policy functional decision theory (P-FDT)** treats these dependencies as relevant to choice.

Its distinctive proposal is to evaluate complete policies, not merely individual physical actions. A policy specifies what to do under each possible input. P-FDT asks which policy-output of the agent’s decision procedure corresponds to the best expected outcome, accounting for systems that predict, reproduce, or otherwise depend on that output.

The primary source is footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality*. It describes intervening on the decision-procedure node

> “to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action.”

The paper does not call this formulation “P-FDT”; that is the name used here. Its main equations instead formalize **action-selection functional decision theory**, an important distinction because changing an entire policy can differ from changing its response to just one observation.

The footnote supplies an architecture, not a complete mathematical theory. The account below develops an operational interpretation, drawing on the surrounding paper while marking additional assumptions.

## 1. Policies as the objects of choice

Let \(\mathcal X\) be a finite set of possible inputs and \(\mathcal A\) a finite action set. A deterministic policy is a function

\[
\pi:\mathcal X\longrightarrow\mathcal A.
\]

Write \(\Pi\subseteq\mathcal A^{\mathcal X}\) for the admissible policies. Inputs might be observations, private information, or complete observation–action histories. In a sequential problem, a policy therefore specifies a contingent plan for the whole relevant interaction.

Let \(M\) be a reference world-model containing:

- uncertainty about the environment;
- a utility function \(U:\mathcal O\to\mathbb R\);
- representations of the agent and relevant predictors or copies;
- a specification of how hypothetical policy changes propagate.

Suppose a selector \(\mathsf S\), implementing P-FDT, returns a policy from this model. Introduce a model variable

\[
D_M=\text{“the policy output by }\mathsf S(M)\text{.”}
\]

This variable represents a mathematical output, not merely the agent’s bodily behavior.

A natural reconstruction of P-FDT is

\[
Q_M(\pi)
=
\mathbb E_M\!\left[
U(O)\mid
\operatorname{do}_{\mathrm{sub}}(D_M=\pi)
\right],
\]

\[
\pi_M^*
\in
\arg\max_{\pi\in\Pi}Q_M(\pi),
\qquad
a^*(x)=\pi_M^*(x).
\tag{1}
\]

Here \(\operatorname{do}_{\mathrm{sub}}\) denotes a **subjunctive intervention**: a hypothetical change to the selector’s output, propagated through the appropriate dependencies. It is not ordinary conditioning and need not be a physical intervention.

Equation (1) is my formal reconstruction, not an equation supplied by footnote 16. In particular, the footnote does not settle the reference model, policy domain, or intervention semantics.

The distinction between selector and policy matters. A candidate \(\pi\) is not necessarily a replacement decision algorithm installed in the agent’s head. Rather, P-FDT evaluates the supposition that **this selector outputs \(\pi\)**. Predictors of the selector must consequently respond to that supposition. Imagining a replacement policy while leaving all predictions of the actual selector unchanged would miss the central proposal.

For finite \(\Pi\), a maximum exists whenever all expectations are defined. A fixed tie-breaking convention makes the selector single-valued. Infinite policy spaces require additional existence or approximation assumptions.

## 2. What changes in a P-FDT hypothetical?

The surrounding paper calls the relevant relation **subjunctive dependence**. Two implementations of the same computation can have linked outputs even when neither physically causes the other. Likewise, a reliable prediction depends on what the predicted computation concludes.

P-FDT preserves such links while breaking correlations that are merely evidential.

For comparison, **evidential decision theory (EDT)** ordinarily evaluates

\[
\mathbb E[U(O)\mid X=x,A=a].
\]

It asks what taking an action would indicate. **Causal decision theory (CDT)** instead evaluates a causal intervention such as

\[
\mathbb E[U(O)\mid X=x,\operatorname{do}(A=a)].
\]

It changes the physical action while preserving causally upstream facts. P-FDT changes the represented policy-output and updates whatever appropriately depends on that output.

An operational model might contain equations

\[
W\sim\mu,\qquad
H=h(D_M,W),\qquad
X=g(H,W),
\]

\[
A=D_M(X),\qquad
O=o(W,H,X,A).
\tag{2}
\]

Here \(W\) contains background uncertainty and predictor errors; \(H\) represents a prediction or another dependent response. To evaluate \(\pi\), replace \(D_M\) by \(\pi\), retain the distribution of \(W\), and recompute the remaining variables.

The arrow implicit in \(H=h(D_M,W)\) need not represent a physical signal from the present to the past. It specifies how the prediction varies across decision hypotheticals.

This model is useful only if its dependencies are justified. A predictor might forecast one particular response, infer the whole policy, or imperfectly approximate the selector. These are different models. Similarly, two agents using similar language or sharing a decision-theory label need not have identical policies.

There is a foundational difficulty. A fixed mathematical selector has only one actual output on fixed inputs. Supposing another output may therefore be **counterpossible**, not merely counterfactual. The source acknowledges that it lacks a general satisfactory account of such reasoning.

The operational response is to manipulate a structured representation: replace the policy-output node rather than append a contradiction to ordinary mathematics. This permits useful calculations without claiming to resolve the underlying semantics.

## 3. P-FDT in Newcomb’s problem

In Newcomb’s problem, a predictor puts \(M=\$1{,}000{,}000\) in an opaque box if it predicts that the agent will take only that box. A transparent box contains \(k=\$1{,}000\), which the agent can additionally take.

With only one relevant input, policies reduce to two alternatives: always one-box or always two-box.

Assume a symmetric subjunctive prediction model:

\[
P(\text{predict one-box}\mid
\operatorname{do}_{\mathrm{sub}}(D_M=\pi_1))=p,
\]

\[
P(\text{predict one-box}\mid
\operatorname{do}_{\mathrm{sub}}(D_M=\pi_2))=1-p.
\]

Then

\[
Q_M(\pi_1)=pM,
\qquad
Q_M(\pi_2)=(1-p)M+k.
\]

P-FDT one-boxes exactly when

\[
(2p-1)M>k.
\]

For \(p=0.99\), the values are \(\$990{,}000\) and \(\$11{,}000\).

This is not an attempt to send money-producing influence backward in time. The two hypotheticals differ in both the policy-output and its predicted representation. CDT holds the already-filled box fixed when changing the physical action; P-FDT preserves the specified prediction relationship.

One qualification is essential: historical accuracy of \(99\%\) does not, by itself, determine these two subjunctive probabilities. Accuracy may vary by action, agent, or policy. The numerical example assumes more than aggregate predictive success.

### P-FDT and a merely evidential correlation

Contrast the paper’s fictional smoking-lesion problem. A lesion causes both a desire to smoke and cancer, while smoking itself causes no cancer.

If changing the policy-output does not change the lesion or cancer, then, for an agent who values smoking by \(b>0\),

\[
Q_M(\pi_{\mathrm{smoke}})
-
Q_M(\pi_{\mathrm{refrain}})
=b.
\]

P-FDT smokes in this stipulated world. It does not treat favorable evidence about health as an outcome it can purchase by abstaining.

The source itself cautions that fully specifying this example raises problems involving self-knowledge and preferences. The general lesson is narrower and sturdier: **correlation alone does not establish subjunctive dependence**.

## 4. Observations are inputs, not necessarily constraints on every hypothetical

A central question is whether P-FDT evaluates policies conditional on the observation currently received.

Footnote 16 does not explicitly answer this. The surrounding discussion, however, allows decision hypotheticals in which the agent would have received different observations. A natural policy-level interpretation therefore evaluates complete policies in a reference model, rather than conditioning every alternative on the actual observation.

Write \(P_M^\pi\) for the distribution produced by the intervention in (1). Then

\[
Q_M(\pi)
=
\sum_x
P_M^\pi(X=x)\,
\mathbb E_M^\pi[U(O)\mid X=x].
\tag{3}
\]

Both the probability of an input and the outcome following it may depend on the policy.

This is not a recommendation to ignore information. If \(X\) is policy-independent, and changing \(\pi(x)\) affects only outcomes on branch \(x\), then

\[
Q_M(\pi)=\sum_x P_M(X=x)\,v_x(\pi(x)).
\]

Optimization separates across inputs:

\[
\pi^*(x)\in\arg\max_a v_x(a)
\]

for every positive-probability input. Ordinary evidence-responsive behavior follows.

The interesting cases are those where the policy helps determine which input arrives, or where different policy entries have linked consequences.

### P-FDT in transparent Newcomb

Suppose both boxes are transparent. The predictor fills the large box according to its prediction of what the agent would do **upon seeing it full**.

A policy now has two entries:

\[
\pi(\mathrm{full}),\qquad \pi(\mathrm{empty}).
\]

Under a perfect predictor, a policy that one-boxes upon seeing a full box produces a full box and receives \(M\). A policy that two-boxes in that circumstance produces an empty box and receives at most \(k\). P-FDT therefore selects one-boxing on the full-box branch.

Seeing the full box does not trigger reoptimization with its fullness held fixed. It identifies which entry of the selected policy to execute.

Under perfect prediction, the empty-box response is off-path and may remain undetermined by expected utility. Giving the predictor a small positive error probability can make that entry consequential; in the usual model, taking both boxes when the large box is empty is then preferable.

This illustrates both the power and the incompleteness of policy optimization: it selects favorable dispositions, but zero-probability contingencies may require tie-breaking or a richer uncertainty model.

## 5. P-FDT in rescue and blackmail problems

In Parfit’s hitchhiker problem, a driver rescues an agent only if the driver predicts payment after arrival. Let rescue be worth \(V\), and payment cost \(c<V\).

Under perfect prediction, the policy “pay when rescued” yields \(V-c\); “refuse when rescued” yields no rescue. P-FDT selects payment. On reaching the city, it executes that policy rather than treating rescue as fixed across all alternatives.

Mechanical blackmail has the opposite structure. A blackmailer initiates a costly threat only when predicting payment. Let payment cost \(c\), and uncompensated damage cost \(L\).

With perfect prediction:

\[
Q_M(\pi_{\mathrm{pay}})=-c,
\qquad
Q_M(\pi_{\mathrm{refuse}})=0,
\]

because refusal deters initiation. Thus P-FDT refuses.

With imperfect prediction, suppose payment attracts blackmail with certainty, while a refusal policy attracts mistaken blackmail with probability \(\varepsilon\). Then

\[
Q_M(\pi_{\mathrm{refuse}})=-\varepsilon L,
\]

so refusal is preferred precisely when

\[
\varepsilon L<c.
\tag{4}
\]

For \(c=\$1{,}000\) and \(L=\$1{,}000{,}000\), the threshold is \(\varepsilon<0.001\). This calculation is an explicit illustrative model, not a universal blackmail prescription.

Under perfect prediction, receiving blackmail after selecting refusal is inconsistent with the model. Small prediction-error probabilities make the received-letter contingency meaningful. The demanding feature remains: P-FDT may execute refusal even in a rare case where payment would reduce the immediate loss.

Conversely, if the attack is independent of the policy, deterrence disappears from the calculation. P-FDT can then recommend payment. Its principle is not stubbornness but dependency-sensitive optimization.

## 6. Why whole-policy selection matters in multi-agent problems

Footnote 16 says the policy/action distinction matters in multi-agent dilemmas, without supplying a worked example. The following construction illustrates a possible reason.

Two copies of the same selector receive independent fair private bits \(X_1,X_2\in\{0,1\}\). Each chooses action \(0\) or \(1\). Player \(i\)’s utility is

\[
u_i(a_i,a_j)
=
10\,\mathbf 1\{a_i=a_j\}
+
\mathbf 1\{a_i=1\}.
\]

Assume both copies implement the same selected policy. A subjunctive change to that policy therefore changes both implementations, though their private inputs remain independent.

There are four deterministic policies:

| Policy \((\pi(0),\pi(1))\) | Expected utility per player |
|---|---:|
| \((0,0)\) | \(10\) |
| \((1,1)\) | \(11\) |
| \((0,1)\) | \(5.5\) |
| \((1,0)\) | \(5.5\) |

For either nonconstant policy, actions match with probability \(1/2\), and each player chooses action \(1\) with probability \(1/2\). Hence the value \(5+0.5\).

P-FDT selects the constant-\(1\) policy. Notice, however, that starting from constant \(0\), changing only one policy entry lowers expected utility from \(10\) to \(5.5\). Whole-policy optimization can escape a trap in coordinatewise improvement.

This does not prove that the paper’s action-selection formulation must select constant \(0\); its treatment of interacting decision nodes would need further specification. It demonstrates why evaluating complete policies is not generally equivalent to optimizing their entries separately.

The same distinction clarifies cooperation with psychological twins. The relevant claim is not that “rational agents always act alike.” It is that particular computations are linked. Identical policies can prescribe different actions on different inputs, and unrelated agents need not change their behavior when one’s policy-output is varied.

Nor does P-FDT introduce altruism. Each player can evaluate only personal utility. Cooperation arises when preserving computational dependencies makes mutually cooperative outcomes preferable.

## 7. Applying P-FDT beyond the examples

A practical analysis should proceed in four stages.

**First, define the policy problem.** Specify inputs, available actions, utility, and the interaction’s horizon. Include relevant contingencies rather than encoding only the action currently salient.

**Second, identify the policy-output node.** What computation is being evaluated? Which predictors or copies represent that computation? Merely sharing an objective or algorithm name is insufficient.

**Third, construct each policy hypothetical.** Change the selector’s represented output; propagate changes through justified predictive, computational, and causal dependencies; preserve unrelated background uncertainty.

**Fourth, compare complete expected outcomes.** Select a maximizing policy and apply the actual input to it. Where uncertain dependency models give different answers, report sensitivity rather than manufacturing a unique recommendation.

Several issues remain open.

The most consequential is the **reference perspective**. Which evidence belongs in \(M\), and which belongs among the policy’s inputs? The footnote does not specify a uniquely privileged prior or say that an agent must optimize from birth. My operational proposal is to use a reference model for the interaction under examination and include potentially policy-dependent observations as inputs. Choosing that boundary remains substantive, especially when later information revises the model itself.

A second issue is policy individuation. Are policies mathematical functions, programs, or computationally bounded procedures? Extensionally equivalent functions may be differently predictable. Representation and computational cost can therefore matter.

Third, policy spaces are enormous: even finite sets give

\[
|\mathcal A^{\mathcal X}|=|\mathcal A|^{|\mathcal X|}.
\]

Practical implementations require restricted policy classes, approximation, and uncertainty about dependencies. Self-representation alone does not solve these computational or reflective-consistency problems.

Finally, broad success claims need qualification. Access to information cannot hurt an optimizer when it can ignore that information while preserving the same policy possibilities and environmental response. But information acquisition can itself change predictions or incentives. Likewise, the source’s proposed superiority in “fair” problems is a research conjecture, not an established general theorem.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, [arXiv:1710.05060v2](https://arxiv.org/abs/1710.05060v2), especially footnotes 7 and 16 and §§3, 5, 9.

## Conclusion

P-FDT evaluates a complete policy as the output of a represented decision procedure, preserving relevant predictive and computational dependencies while rejecting merely evidential correlations. Its central question is not simply what a physical action causes, but which policy-output corresponds to the best expected world.

That provides a powerful framework for prediction, commitment, and coordination problems. Its unresolved work lies chiefly in specifying the reference perspective and the semantics of subjunctive intervention—precisely the choices that must be made explicit when applying it to unfamiliar cases.