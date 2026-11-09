# P-FDT: Choosing the Policy, Not Just the Present Act

## 1. The source and the central idea

A decision can be evaluated at several levels: as a bodily action, as the conclusion of a computation, or as one branch of a policy governing many possible situations. **Policy functional decision theory (P-FDT)** takes the third perspective while retaining the second perspective’s attention to computational dependencies.

The primary source for this account is footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality*. It describes their preferred formulation as intervening on a computational node

> “to choose not an action but a policy which maps inputs to actions”

and then applying that policy to the agent’s inputs. Footnote 7 likewise says that their preferred formulation evaluates policies rather than actions. Most of the paper instead develops an action-output formulation of functional decision theory, which I will distinguish from P-FDT.

This distinction matters. Choosing a policy means comparing entire contingent responses, including responses to observations not actually received. Moreover, because other systems may predict or implement that policy, evaluating an alternative policy can require changing those systems’ behavior in the hypothetical under consideration.

The footnote supplies an architecture, not a complete mathematical theory. It does not settle the policy’s domain, the evidential standpoint for evaluating policies, or the semantics of computational interventions. Below I develop an operational interpretation informed by the surrounding paper, marking the important additional assumptions.

## 2. A mathematical formulation of P-FDT

Consider a finite decision problem with:

- an input space \(\mathcal X\), usually observation histories;
- an action space \(\mathcal A\);
- an outcome space \(\mathcal O\);
- a utility function \(u:\mathcal O\to\mathbb R\).

A deterministic policy is a function
\[
\pi:\mathcal X\longrightarrow\mathcal A.
\]
Let \(\mathcal P\subseteq\mathcal A^{\mathcal X}\) be the admissible policy set. Policies must respect informational constraints: they cannot distinguish situations that supply the same input. In sequential problems, their inputs can be complete available histories.

Let \(M\) contain probabilistic beliefs and a representation of relevant causal and computational dependencies. Write \(S(M)\) for a policy-selection computation, and let \(D_M\) be a variable *inside the model* representing its policy-valued output.

The distinction between \(D_M\) and \(S(M)\) is crucial. The former is a representation manipulated during deliberation; the latter is the policy actually selected.

Introduce a hypothetical-outcome distribution
\[
K_M(o;\pi)
=
\Pr_M\!\left(
O=o\;\middle|\;
\operatorname{do}_{\mathrm{sub}}(D_M=\pi)
\right).
\]
The notation \(\operatorname{do}_{\mathrm{sub}}\) denotes a **subjunctive intervention**: set the represented policy output to \(\pi\), and propagate the change through all relevant dependencies.

My proposed P-FDT rule is
\[
\boxed{
\begin{aligned}
Q_M(\pi)&=\sum_{o\in\mathcal O}K_M(o;\pi)\,u(o),\\
\pi^*&\in\arg\max_{\pi\in\mathcal P}Q_M(\pi),\\
a^*&=\pi^*(x_{\mathrm{actual}}).
\end{aligned}}
\]

This directly implements footnote 16’s two-stage structure: select a policy, then apply the actual input. A fixed tie-breaking rule makes the procedure single-valued.

A useful structural version starts with exogenous uncertainty \(W\sim p_M\). For each hypothetical policy \(\pi\), calculate an outcome \(O_\pi(W)\), giving
\[
Q_M(\pi)=\mathbb E_{W\sim p_M}[u(O_\pi(W))].
\]

For example, a model might contain
\[
R=r(D_M,W),\qquad
X=g(R,W),\qquad
A=D_M(X),\qquad
O=h(R,X,A,W),
\]
where \(R\) represents a prediction or another agent’s response. To evaluate \(\pi\), substitute \(D_M=\pi\) throughout these equations. Importantly, calculate the hypothetical input \(X_\pi\) before evaluating
\[
A_\pi=\pi(X_\pi).
\]
One must not automatically substitute \(\pi(x_{\mathrm{actual}})\) when the hypothetical changes which input is received.

This formalization restricts policies to observation histories within a fixed problem. A broader interpretation could include world-models or preferences among the policy’s inputs. The footnote does not settle that scope.

## 3. What changes under a P-FDT counterfactual?

P-FDT’s distinctive ingredient is not expected utility maximization but the construction of \(K_M\).

For comparison, **evidential decision theory (EDT)** evaluates an action using a conditional such as
\[
\mathbb E[u(O)\mid X=x,A=a].
\]
**Causal decision theory (CDT)** instead evaluates a causal intervention:
\[
\mathbb E[u(O)\mid X=x,\operatorname{do}(A=a)].
\]

P-FDT intervenes on a represented *policy-valued computational output*. Its counterfactual dependencies therefore extend beyond the physical consequences of the present action.

The source calls the broader relation **subjunctive dependence**. Paradigmatic examples include:

1. **Implementation:** the agent acts according to its selected policy.
2. **Replication:** another system implements the same policy-selection computation.
3. **Prediction:** another system accurately models that computation or its resulting behavior.
4. **Ordinary causation:** actions subsequently affect outcomes.

By contrast, a correlation generated by an unrelated common cause need not survive a policy intervention.

Suppose an accurate simulator predicts whether an agent will pay a fee. In the hypothetical where the policy selector outputs a refusal policy, the simulator’s prediction should generally change. But suppose a disease both induces a preference and causes illness. Changing the policy selector’s output does not thereby remove the disease.

Neither statistical association alone nor physical separation settles the issue. The question is how the systems’ behavior depends on the computation being evaluated.

This does **not** mean imagining that the agent physically installs a new program at the present moment. Such installation might come too late to influence an earlier predictor. The hypothetical concerns what would follow if the very computation being represented had a different policy output.

For a deterministic selector with fixed inputs, that antecedent may be mathematically impossible. P-FDT thus inherits the source’s problem of **counterpossible reasoning**. An operational model must selectively override one represented computational fact without allowing logical contradiction to make every conclusion follow.

Structural substitution provides a usable local procedure once the dependencies are supplied. It does not establish that those dependencies are correct. As the paper acknowledges, constructing a satisfactory general theory of such dependencies remains open.

## 4. Observations and the standpoint of policy evaluation

The most consequential unresolved choice is whether to evaluate policies conditional on the actual input:
\[
Q_{M,x}(\pi)
=
\mathbb E[u(O)\mid X=x,\operatorname{do}_{\mathrm{sub}}(D_M=\pi)],
\]
or from a background standpoint that allows the intervention to change \(X\).

These need not agree.

My operational interpretation uses the second approach when \(X\) itself depends on the selected policy. It is motivated by the surrounding paper’s transparent-box and blackmail examples, where hypothetical alternatives can involve different observations.

Specifically:

- Fix background context \(M\).
- Evaluate complete policies across the input distribution generated under each policy.
- Apply the selected policy to the actual input.

The background context need not be ignorance. It may incorporate extensive information. But one must distinguish information fixing the decision problem from observations generated *within* the policy-dependent process being evaluated.

This is an additional modeling commitment, not something fully determined by footnote 16. The source does not specify a unique prior or evaluation boundary, and policy selection alone does not establish one.

Nor does this interpretation imply ignoring observations. In an ordinary problem where policy choice does not affect the input distribution and branches are independent,
\[
Q_M(\pi)
=
\sum_x p_M(x)\,V_M(x,\pi(x)),
\]
where \(V_M(x,a)\) is the appropriate causal value of acting after input \(x\). With unrestricted policies, optimization separates:
\[
\pi^*(x)\in\arg\max_a V_M(x,a)
\]
for every positive-probability input.

Thus P-FDT can use evidence exactly as ordinary conditional optimization does. The unusual prescriptions arise when policy outputs influence predictions, input occurrence, or behavior elsewhere.

## 5. P-FDT in prediction problems

### Opaque and transparent boxes

In Newcomb’s problem, an opaque box contains \(B=\$1{,}000{,}000\) if a predictor predicts one-boxing, and nothing otherwise. A second box contains \(k=\$1{,}000\).

Assume, as an explicit counterfactual model, that prediction accuracy is symmetrically \(q\) under either policy. Historical accuracy alone would not establish this.

For the two constant policies,
\[
Q(\pi_{\mathrm{one}})=qB,
\qquad
Q(\pi_{\mathrm{two}})=(1-q)B+k.
\]
P-FDT one-boxes when
\[
(2q-1)B>k.
\]
At \(q=0.99\), the values are \(\$990{,}000\) and \(\$11{,}000\).

The policy formulation becomes more revealing when both boxes are transparent. Suppose the predictor forecasts what the policy would do *upon seeing a full large box*, and fills it exactly when the forecast is one-boxing.

Consider
\[
\pi_{OT}(\mathrm{full})=\mathrm{one},
\qquad
\pi_{OT}(\mathrm{empty})=\mathrm{two}.
\]
Its value is
\[
Q(\pi_{OT})=qB+(1-q)k.
\]
The always-two-box policy has value
\[
Q(\pi_{TT})=(1-q)B+k.
\]
Hence
\[
Q(\pi_{OT})-Q(\pi_{TT})
=(2q-1)B-qk.
\]
At \(q=0.99\), their values are \(\$990{,}010\) and \(\$11{,}000\). The other two deterministic policies do no better: taking the small box when the large one is empty adds money without changing this predictor’s prediction.

P-FDT therefore selects \(\pi_{OT}\), including its one-boxing response to seeing a full box.

The agent need not believe that the visible money can physically disappear. Its belief about the actual box remains intact. Its *policy comparison* nevertheless includes alternatives under which the predictor would probably have left that box empty.

Parfit’s hitchhiker has the same structure: a driver rescues someone conditional on predicting payment afterward. A sufficiently reliable prediction can make “pay if rescued” the better policy, even though payment has no further rescue benefit once the city is reached.

### A common-cause contrast

In the hypothetical smoking-lesion problem, assume smoking provides utility \(s>0\), has no health consequences, and is correlated with cancer only through a lesion.

Under the stipulated dependency model,
\[
\Pr(C\mid\operatorname{do}_{\mathrm{sub}}(D_M=\pi_{\mathrm{smoke}}))
=
\Pr(C\mid\operatorname{do}_{\mathrm{sub}}(D_M=\pi_{\mathrm{refrain}})).
\]
The smoking policy is therefore better by \(s\).

This illustrates the distinction between prediction and common-cause correlation, not a real-world recommendation. The source itself eventually criticizes the smoking-lesion setup as contrived, especially concerning uncertainty about preferences and population-level correlations.

## 6. Why whole-policy selection can matter between agents

Footnote 16 says that the policy/action distinction matters in multi-agent dilemmas, but provides no worked example. The following is my illustration.

Two copies share a policy selector. Each independently receives a uniformly random label \(x\in\{0,1\}\), then chooses \(C\) or \(D\). Each agent’s utility is
\[
u_i=10\,\mathbf 1\{A_1=C,A_2=C\}
-6\,\mathbf 1\{A_i=C\}.
\]
Thus mutual cooperation yields \(4\), mutual defection yields \(0\), and unilateral cooperation yields \(-6\) to the cooperator.

Suppose both implementations subjunctively depend on the same selected policy \(\pi\). Let
\[
r=\Pr(\pi(X)=C).
\]
Because the labels are independent,
\[
Q(\pi)=10r^2-6r.
\]
For deterministic policies:

| Policy outputs on labels \(0,1\) | \(r\) | Expected utility |
|---|---:|---:|
| \(D,D\) | \(0\) | \(0\) |
| \(C,D\) or \(D,C\) | \(1/2\) | \(-1/2\) |
| \(C,C\) | \(1\) | \(4\) |

Whole-policy optimization selects cooperation on both inputs.

Now consider a hypothetical procedure that changes only one table entry while holding the other fixed. Starting from \(D,D\), either isolated change lowers value from \(0\) to \(-1/2\). Yet changing both entries improves value to \(4\).

This demonstrates a general distinction:
\[
\text{optimal complete policy}
\neq
\text{policy admitting no profitable single-entry change}.
\]

It is not a proof that the source’s action-output formulation must defect in this example: that answer also depends on its unspecified computational dependency model. The example instead shows why replacing policy optimization with local action optimization is not generally harmless.

Equally importantly, shared policy does not mean identical action. Different inputs can appropriately produce different outputs. P-FDT coordinates the relevant computation, not everyone’s bodily movements indiscriminately. Merely knowing that two agents endorse P-FDT does not prove that their policy selections are identical or tightly coupled.

## 7. P-FDT, blackmail, and sensitivity to errors

Consider a stylized mechanical blackmail problem. An attacker launches a damaging program when it predicts that the agent will pay \(k\). If attacked, payment prevents damage \(L\).

Assume:

- a paying policy is attacked with probability \(1\);
- a refusing policy is mistakenly attacked with probability \(\varepsilon\);
- otherwise no damage occurs.

Then
\[
Q(\pi_{\mathrm{pay}})=-k,
\qquad
Q(\pi_{\mathrm{refuse}})=-\varepsilon L.
\]
P-FDT selects refusal when
\[
\varepsilon L<k.
\]

With \(k=\$1{,}000\) and \(L=\$1{,}000{,}000\), the threshold is
\[
\varepsilon<0.001.
\]
At \(\varepsilon=0.0009\), refusal loses \(\$900\) in expectation, less than payment’s \(\$1{,}000\). At \(\varepsilon=0.0011\), payment is preferable under this model.

This captures the source’s motivation without making resistance unconditional. P-FDT does not prescribe stubbornness regardless of prediction quality.

On the policy-evaluation interpretation above, receiving a demand does not by itself justify conditioning away the policy’s influence on whether demands occur. Nevertheless, genuinely new evidence that the attacker is indiscriminate, or that the error model was wrong, raises another question: should the background model be revised? Footnote 16 does not resolve the boundary between appropriate learning and destructive branchwise reoptimization.

Consequently, these stylized results are not general advice about real extortion. Their conclusions depend on unusually strong knowledge of the attacker and the dependency structure.

## 8. Applying P-FDT to unfamiliar cases

A practical P-FDT analysis can proceed as follows:

1. **Specify the policy domain.** What inputs are available, and what actions are feasible at each input?
2. **Choose the evaluation context.** Which facts define the background model, and which observations arise within the policy-dependent process?
3. **Identify the computational target.** What policy-selection output is being varied?
4. **Map dependencies.** Which implementations, predictors, and consequences change with that output? Which common causes remain unchanged?
5. **Construct complete hypotheticals.** Recompute predictions, inputs, actions, and outcomes under each candidate policy.
6. **Compare expected utilities.** Test sensitivity to errors, uncertain dependencies, and policy restrictions.
7. **Execute the selected branch.** Apply the chosen policy to the actual input.

The difficult work usually lies in steps 2–4, not in taking an argmax.

Several attractive claims require qualification. Policy optimization gives information nonnegative value when the enlarged policy space contains an option that ignores it *and the surrounding dependency model remains otherwise unchanged*. It does not establish that every information-acquisition process is beneficial. Likewise, a precommitment-like prescription is not automatically a theorem of reflective stability.

Finally, neither the footnote nor the paper proves universal optimality. The authors acknowledge that arbitrary environments can reward or punish particular decision procedures, and that their proposed distinction between “fair” and “unfair” problems lacks a complete formal treatment.

### Reference

Yudkowsky, Eliezer, and Nate Soares. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2. Primary passages: footnotes 7 and 16; supporting discussion: §§3, 5–6, and 9. https://arxiv.org/abs/1710.05060v2

## Conclusion

P-FDT evaluates complete input-to-action policies by asking what would follow if the represented policy-selection computation output each alternative. It preserves relevant computational dependencies without preserving every statistical correlation.

That architecture supports useful, precise analyses of predictors, copies, contingent cooperation, and threats. Its unresolved core is equally clear: specifying the policy’s scope, its evidential standpoint, and the semantics of subjunctive intervention. A responsible application makes those choices explicit rather than treating a short policy-selection footnote as an already complete theory.