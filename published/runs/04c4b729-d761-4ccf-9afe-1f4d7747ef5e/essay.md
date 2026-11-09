# P-FDT: Choosing Policies While Preserving Computational Dependencies

## 1. The starting point: a policy, not an isolated action

Decision-making is often described as choosing an action in a world whose relevant background features are fixed. But what if that background includes a prediction of the choice, or another agent running the same decision procedure? Changing only the physical action may then break a dependency that matters to the outcome.

**Policy functional decision theory (P-FDT)** evaluates alternatives at the level of a policy-producing computation. Its primary source here is footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality*. The footnote describes intervening on a computational node to choose:

> “not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action.”

This is more than advice to plan ahead. The proposed intervention concerns the output of a fixed mathematical procedure, including its relevant representations elsewhere in the world. A predictor’s response may therefore vary across the alternatives, even if its physical prediction occurred earlier.

The distinction from the paper’s main-text, action-selection formulation is important. That formulation varies the output associated with a particular input; P-FDT selects an entire input-to-action mapping. The authors say the distinction matters in some multi-agent dilemmas, while leaving it largely undeveloped.

Consequently, the footnote supplies a central idea, not a complete specification. This essay develops one mathematical reconstruction, using the paper’s account of *subjunctive dependence* as background. I will explicitly identify additional assumptions, especially concerning which observations enter policy selection and which enter policy execution.

## 2. A mathematical reconstruction of P-FDT

Let:

- \(\mathcal X\) be a finite set of possible inputs or observation histories;
- \(\mathcal A\) be a finite action set;
- \(\Pi\subseteq\mathcal A^{\mathcal X}\) be the admissible policies;
- \(\mathcal O\) be the outcome space;
- \(u:\mathcal O\to\mathbb R\) be a utility function.

A deterministic policy is a function

\[
\pi:\mathcal X\longrightarrow\mathcal A.
\]

Inputs may include private information, an assigned role, or a sequence of observations. A policy therefore specifies behavior at contingencies that never actually occur.

Let \(M\) be the agent’s evaluative world-model. Besides probabilities, it must describe how outcomes depend on actions, predictions, and relevant computations. Write \(\mathsf S\) for the fixed policy-selection procedure and introduce a model variable

\[
D_M\quad\text{representing the output of }\mathsf S(M).
\]

The distinction between the variable and its represented value is essential: \(D_M\) is something the model manipulates; \(\mathsf S(M)\) is the policy actually selected.

For each candidate \(\pi\), construct a hypothetical distribution

\[
K_M^\pi(o)
=
P_M\!\left(
O=o\;\middle|\;
\operatorname{do}_{\mathrm{subj}}(D_M=\pi)
\right).
\]

The subscript emphasizes that this is not an ordinary causal intervention. It replaces the represented output of the policy-selection computation and propagates the replacement through all relevant subjunctive dependencies.

The reconstructed P-FDT rule is

\[
\boxed{
\mathsf S(M)
=
\operatorname*{arg\,max}_{\pi\in\Pi}
\sum_{o\in\mathcal O}K_M^\pi(o)u(o)
}
\]

with a fixed tie-breaking convention. After receiving input \(x\), the agent executes

\[
a=\mathsf S(M)(x).
\]

**My operational assumption** is that \(M\) remains the reference model throughout the decision episode. Observations within that episode enter the selected policy rather than automatically replacing its evaluation with a new, observation-conditioned optimization. This captures the policy-wide perspective suggested by the footnote and the surrounding discussion, but the footnote does not uniquely require this convention.

A useful implementation separates background uncertainty from intervention-sensitive variables. Let \(W\sim\mu_M\) represent background conditions, including predictor errors. A model might specify

\[
H=h(D_M,W),\qquad
A=D_M(H),\qquad
O=g(D_M,H,A,W).
\]

Under \(D_M=\pi\), recompute these equations to obtain \(O_\pi(W)\), giving

\[
J_M(\pi)=\mathbb E_{\mu_M}[u(O_\pi(W))].
\]

The direct appearances of \(D_M\) in \(h\) and \(g\) can represent predictions or other implementations of the computation. They do **not** imply that the agent can physically transmit its policy backward in time.

This formalism assumes well-defined hypothetical outcomes. Constructing a satisfactory general intervention semantics remains an open problem.

## 3. P-FDT’s dependencies and counterfactuals

P-FDT differs from other expected-utility theories primarily in how it constructs alternatives.

**Evidential decision theory (EDT)** ordinarily evaluates an action through

\[
\mathbb E[u(O)\mid H=x,A=a].
\]

This asks what learning that one acted would indicate.

**Causal decision theory (CDT)** instead uses a causal intervention, schematically

\[
\mathbb E[u(O)\mid H=x,\operatorname{do}(A=a)].
\]

This changes the physical action and its causal consequences, without changing upstream causes.

P-FDT intervenes on a computational output: the selected policy. Dependencies preserved under this intervention can include:

1. **Causal consequences:** changing an executed action changes what it physically affects.
2. **Computational agreement:** exact implementations of the same policy-producing computation return the same policy.
3. **Prediction:** a sufficiently accurate representation of that computation responds appropriately to its hypothetical output.

Mere correlation is insufficient. A disease correlated with an action need not change when the policy changes. Conversely, a causally isolated copy of the selector may change in the hypothetical because both implementations represent the same mathematical computation.

This is the paper’s notion of **subjunctive dependence**. Its scope must be justified, not assumed whenever coordinated behavior would be profitable. Two people’s endorsement of P-FDT does not establish that their different models, utilities, and inputs produce identical policies.

There is also a logical difficulty. A fixed deterministic computation has one output. Imagining that it returns another policy may therefore be a *counterpossible*: an antecedent incompatible with the relevant mathematical facts.

The paper acknowledges the absence of a complete theory of such reasoning. Its practical proposal is to supply a dependency structure and perform model surgery. P-FDT inherits this limitation. A notation such as \(\operatorname{do}_{\mathrm{subj}}\) identifies the missing operation; it does not solve it.

Nor does replacing “the output were different” with “I used another algorithm” remove the issue. If a predictor models the actual selector, one must still specify how its prediction changes across alternatives.

## 4. P-FDT in Newcomb’s problem and the lesion contrast

In Newcomb’s problem, an opaque box contains \(M\) dollars if a predictor forecast one-boxing and zero otherwise. A transparent box contains \(b\) dollars. Assume that, under either policy intervention, the predictor reports the selected action correctly with probability \(q\).

This last assumption is stronger than knowing an overall historical accuracy rate: it specifies how reliability behaves across the alternatives being evaluated.

With only one relevant input, policies reduce to constant actions. Their values are

\[
J(\pi_{\mathrm{one}})=qM,
\]

\[
J(\pi_{\mathrm{two}})=(1-q)M+b.
\]

Thus P-FDT one-boxes exactly when

\[
(2q-1)M>b.
\]

For \(q=0.99\), \(M=\$1{,}000{,}000\), and \(b=\$1{,}000\), these values are \(\$990{,}000\) and \(\$11{,}000\).

The reasoning does not say that taking one box physically fills it. It says that the alternative policy outputs have different associated predictions, and therefore different box contents.

Contrast the fictional smoking-lesion problem. A lesion causes both cancer and a disposition toward smoking, while smoking itself has no health consequences. Suppose smoking contributes \(s>0\) utility, and changing the selected policy changes neither the lesion nor cancer. Then

\[
J(\pi_{\mathrm{smoke}})
-
J(\pi_{\mathrm{refrain}})
=s.
\]

P-FDT recommends smoking in this stipulated world—not as medical advice about actual smoking.

The difference is structural. A predictor represents behavior; a lesion need not. The paper itself later acknowledges difficulties in formalizing the lesion example, including agents’ knowledge of their preferences. The general lesson is therefore the distinction between correlation and policy-sensitive dependence, not an unqualified victory over every version of EDT.

## 5. P-FDT after observing the outcome of a prediction

Transparent Newcomb makes the observation issue explicit. Both boxes are visible. The predictor fills the large box if it predicts that the agent would one-box **upon seeing it full**.

A policy must specify two responses:

\[
\pi(F),\qquad \pi(E),
\]

where \(F\) and \(E\) mean that the large box appears full or empty.

Compare

\[
\pi_1(F)=\mathrm{one},\qquad
\pi_1(E)=\mathrm{two},
\]

with the always-two-box policy \(\pi_2\). Assume the predictor correctly predicts \(\pi(F)\) with probability \(q\). Then

\[
J(\pi_1)=qM+(1-q)b,
\]

whereas

\[
J(\pi_2)=(1-q)(M+b)+qb=(1-q)M+b.
\]

At the previous numerical values,

\[
J(\pi_1)=\$990{,}010,\qquad
J(\pi_2)=\$11{,}000.
\]

The policy that always one-boxes is slightly worse than \(\pi_1\), because taking the small box when the large box is empty earns an additional \(b\) without affecting the prediction rule.

Under this reconstruction, P-FDT therefore takes only the large box when it sees that box full.

Why not condition on fullness and reconsider? Because doing so changes the question. Conditional optimization holds the favorable observation fixed. Policy evaluation compares alternatives under which that observation itself can differ: changing \(\pi(F)\) changes the prediction and hence which input the agent receives.

This does not mean the agent doubts its eyesight. Its factual belief remains that the box is full. Its decision hypothetical asks what the episode would look like under another computational output.

Parfit’s hitchhiker has the same structure. A driver rescues a stranded traveler if the driver predicts payment after arrival. A policy that pays in the city can secure rescue, while a policy that refuses may prevent arrival altogether. P-FDT evaluates that whole relationship rather than treating arrival as independent of the payment policy.

The controversial commitment is genuine: P-FDT can prescribe a locally costly action because it belongs to the better globally evaluated policy. The footnote leaves open how to delimit that global evaluation.

## 6. P-FDT’s policy-wide intervention in a multi-agent example

Why select a whole policy rather than one input-specific output? Consider this constructed example; it is not a case supplied by the paper.

Two agents implement the same selector with the same evaluative model. They receive complementary roles \(r=0,1\), assigned uniformly at random. Each can invest or abstain. Role \(0\)’s investment costs \(1\); role \(1\)’s costs \(2\). If both invest, each receives a benefit of \(5\). Otherwise there is no benefit.

The shared selected policy maps roles to actions:

\[
\pi:\{0,1\}\to\{I,A\}.
\]

Evaluated before role assignment, the four policies have values

\[
\begin{array}{c|c}
(\pi(0),\pi(1)) & J(\pi)\\ \hline
(A,A)&0\\
(I,A)&-\tfrac12\\
(A,I)&-1\\
(I,I)&5-\tfrac12(1+2)=3.5.
\end{array}
\]

P-FDT selects \((I,I)\). Its intervention changes both agents’ selected policies because, by construction, they implement the same selection computation. Their actions need not be identical in general: the shared output is a function, subsequently applied to different inputs.

Now consider evaluating one policy entry at a time while holding the other at abstention. Changing only \(\pi(0)\) to investment loses money; changing only \(\pi(1)\) does likewise. Such coordinate-wise evaluation gets stuck at \((A,A)\), although changing the whole policy is beneficial.

This illustrates the significance of the footnote’s policy object. It is not a proof that every action-selection formulation must fail here; another counterfactual model might encode additional dependencies between its action-output nodes.

The shared-selector assumption is doing substantive work. If the other agent independently follows a fixed abstention policy, intervening on one’s own selector does not alter it, and investment is wasteful. P-FDT is not permission to assume cooperation into existence.

## 7. P-FDT and the price of resisting blackmail

Policy evaluation also explains resistance to predictive blackmail, without making refusal unconditional.

Suppose a blackmailer always demands payment from an agent predicted to pay \(c\). An agent predicted to refuse is mistakenly targeted with probability \(\varepsilon\). Refusing an actual demand incurs loss \(L\). Assume no other relevant consequences.

The two response policies have values

\[
J(\pi_{\mathrm{pay}})=-c,\qquad
J(\pi_{\mathrm{refuse}})=-\varepsilon L.
\]

P-FDT refuses when

\[
\varepsilon<\frac{c}{L}.
\]

With \(c=\$1{,}000\) and \(L=\$1{,}000{,}000\), the threshold is \(0.001\). At \(\varepsilon=0.0009\), refusal loses \(\$900\) in expectation, less than the payer’s \(\$1{,}000\).

Under the fixed-reference interpretation, this policy still prescribes refusal on the rare occasion a demand arrives. Its advantage does not imply that refusal saves money on every realized branch.

But if the demand is independently initiated and unaffected by predictions of the response, the comparison changes. Paying can then avert \(L\) at cost \(c\). P-FDT’s prescription depends on the actual predictive relationship, not on a general maxim against paying threats.

## 8. Applying P-FDT: a procedure and its unresolved choices

Given a sufficiently specified model, the reconstructed procedure is:

1. **Define the episode and reference information.** State what is already incorporated into \(M\), and what will instead be supplied as policy input.
2. **Specify complete policies.** Include behavior at unrealized contingencies, not merely the currently available action.
3. **Identify the selector variable.** Represent this computation’s policy output, rather than an arbitrarily chosen disposition.
4. **Map dependencies.** Distinguish causal effects, computational agreement, prediction, and mere statistical association.
5. **Construct each hypothetical.** Set the selector output to \(\pi\), propagate its supported dependencies, and preserve unaffected background conditions.
6. **Maximize expected utility and execute.** Choose the best policy, then apply it to the actual input.

Several choices remain unresolved by footnote 16.

**Reference-model selection.** Freezing the episode model explains the examples above, but does not tell us where an episode begins. Reoptimizing after every observation can destroy policy-level incentives; refusing all model revision would prevent learning. A plausible extension distinguishes observations anticipated as policy inputs from evidence that the model itself is mistaken. The source does not supply a general boundary rule.

**Computational identity and prediction strength.** Exact copies provide a clear limiting case. Approximate predictors require a justified response model under interventions. Ordinary correlation or observed accuracy alone may not identify it.

**Randomization.** The finite deterministic policy space was a simplifying assumption. A broader theory must distinguish independent private randomness from shared or predictable randomness. Two copies selecting the same stochastic policy need not realize the same action.

**Information value.** With a fixed evaluation and an enlarged policy space, an informational policy can always imitate one that ignores a signal. Maximization therefore gives nonnegative informational value under those assumptions. This argument does not automatically cover information that changes the environment, incurs costs, or changes the reference model.

Finally, neither the footnote nor the paper establishes universal optimality. The authors acknowledge both the unfinished counterfactual semantics and the difficulty of defining a class of “fair” problems. P-FDT is a proposed normative framework whose prescriptions become determinate only with additional modeling structure.

## References

Yudkowsky, E., and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2. Especially footnotes 7 and 16, and §§3, 5, and 9.

Pearl, J. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000. Background for causal interventions, not a completed semantics for P-FDT’s computational interventions.

## Conclusion

P-FDT evaluates complete policies as alternative outputs of a fixed computation, preserving the predictions and implementations that genuinely depend on that output. This explains both its appeal and its controversial prescriptions: a good policy can require locally costly behavior after favorable observations. Its central unfinished task is to specify those computational counterfactuals—and their evidential scope—without either discarding real dependencies or inventing convenient ones.