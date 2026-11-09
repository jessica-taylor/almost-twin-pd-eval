# P-FDT: Choosing the Rule, Not Just the Move

Decision problems become unusual when the world responds not only to what an agent physically does, but also to predictions or other implementations of its reasoning. A predictor may already have rewarded an anticipated choice. A psychological twin may independently reach the same conclusion. A blackmailer may decide whether to issue a threat by forecasting the victim’s response.

**Policy functional decision theory (P-FDT)** evaluates decisions at the level of an entire input-to-action rule. Its central question is:

> Which policy would yield the best outcome, allowing predictions and other relevant implementations of that policy to vary with it?

The primary source for this account is footnote 16 of Eliezer Yudkowsky and Nate Soares’s *[Functional Decision Theory: A New Theory of Instrumental Rationality](https://arxiv.org/abs/1710.05060v2)*. That footnote describes their preferred formulation as choosing “a policy which maps inputs to actions,” then applying the agent’s inputs to obtain an action. Footnote 7 likewise identifies policies as mappings from observations to actions.

These passages specify the object of choice, but not a complete mathematical theory. The paper develops an action-selection formulation in detail while postponing the policy distinction, which the authors suggest matters in some multi-agent problems. Accordingly, the formalism below is an **operational reconstruction of P-FDT**, informed by the paper’s account of dependencies and counterfactuals—not a claim that the footnote settles every modeling choice.

## 1. The mathematical object of choice

Let \(\mathcal X\) be a finite set of possible inputs and \(\mathcal A\) a finite action set. A deterministic policy is a function

\[
\pi:\mathcal X\longrightarrow\mathcal A.
\]

Write \(\Pi\subseteq\mathcal A^{\mathcal X}\) for the admissible policies. After selecting \(\pi^*\), an agent receiving input \(x\) performs

\[
a^*=\pi^*(x).
\]

Inputs may include observations, private signals, remembered events, or other information relevant to action. In sequential settings, they can be complete observation–action histories. A policy then specifies behavior at every relevant history, including histories that do not occur under that policy.

The important distinction is between choosing:

* an action **at the currently observed input**; and
* a complete rule specifying actions **across possible inputs**.

Two policies can agree on what to do now while differing elsewhere. Those differences can matter if another agent predicts behavior at an unrealized input, or if another implementation receives a different input.

For a finite abstraction, suppose the agent has a background model \(M\), an outcome variable \(O\), and a bounded utility function \(u(O)\). Let \(K_M\) be a variable representing the policy selected by the P-FDT computation for that background model. Define a policy-value functional

\[
V_M(\pi)
=
\mathbb E_M\!\left[
u(O)\mid
\operatorname{do}_{\mathrm{subj}}(K_M=\pi)
\right].
\]

Then the reconstructed rule is

\[
\boxed{
\pi_M^*\in\arg\max_{\pi\in\Pi}V_M(\pi),
\qquad
a^*=\pi_M^*(x).
}
\tag{1}
\]

A fixed tie-breaking convention makes this single-valued.

The operator \(\operatorname{do}_{\mathrm{subj}}\) is not ordinary conditioning and need not be a physical intervention. It constructs a hypothetical in which the policy-selection computation returns \(\pi\), propagating that change through relevant **subjunctive dependencies**.

Equation (1) also exposes a major interpretive choice: which information belongs in the fixed background \(M\), and which belongs among the varying inputs \(x\)? For now, assume that \(M\) describes the interaction before the policy-dependent observations being modeled. We return to this boundary below.

## 2. What changes when a policy changes?

The paper’s motivating distinction is between three kinds of dependence.

**Causal dependence:** a motor command changes the motion of an arm.

**Statistical dependence:** smoking may provide evidence of an underlying condition without causing that condition.

**Subjunctive dependence:** two implementations of the same computation must correspond in their outputs, even when neither physically influences the other.

For P-FDT, predictions and copies belong in policy counterfactuals when their behavior depends on the selected policy. Mere correlations do not automatically belong there.

A useful operational model introduces exogenous uncertainty \(W\), distributed according to \(\mu_M\), and equations such as

\[
X=g(K_M,W),\qquad
A=K_M(X),\qquad
Y=h(K_M,W),\qquad
O=f(X,A,Y,W).
\]

Here \(Y\) might describe a predictor’s response or another implementation’s behavior. Under the policy hypothetical \(K_M=\pi\), recompute the dependent variables:

\[
X^\pi=g(\pi,W),\quad
A^\pi=\pi(X^\pi),\quad
Y^\pi=h(\pi,W).
\]

Thus,

\[
V_M(\pi)
=
\sum_w\mu_M(w)\,
u\!\left(f(X^\pi,A^\pi,Y^\pi,w)\right).
\tag{2}
\]

This is a proposed finite implementation of the source’s idea. The equations must already encode the appropriate dependencies; merely drawing arrows does not establish them.

An essential point is that **a common policy need not produce a common action**. If two copies receive \(x_1\) and \(x_2\), their actions are

\[
A_1=\pi(x_1),\qquad A_2=\pi(x_2),
\]

which may differ. P-FDT coordinates rules, not necessarily moves.

Nor does P-FDT hold that all intelligent agents share one policy-selection variable. Shared rationality, similar preferences, or agreement in past cases is insufficient. The dependency must be justified by the particular relationship: identical computation, accurate simulation, known prediction mechanisms, or some weaker probabilistic connection.

### Why these are counterfactuals, not evidence

Evidential decision theory evaluates actions using quantities such as

\[
\mathbb E[u(O)\mid X=x,A=a].
\]

Causal decision theory instead uses, schematically,

\[
\mathbb E[u(O)\mid X=x,\operatorname{do}(A=a)].
\]

P-FDT asks about changing the output of the policy-selection computation, rather than merely conditioning on an action or physically overriding it.

This introduces the paper’s hardest foundational problem. A fixed deterministic computation has only one output. Supposing that it returns another policy may therefore be a **counterpossible** supposition—contrary to a mathematical fact.

One cannot preserve every mathematical truth while changing that output. The intended operation locally overrides the selected output while retaining the dependency relations needed to evaluate its consequences. The paper acknowledges that a general account of such reasoning remains unavailable. P-FDT is therefore most operationally definite when the relevant counterfactual model is explicitly supplied.

## 3. P-FDT in prediction and common-cause problems

### Newcomb’s problem

An opaque box contains \(R=\$1{,}000{,}000\) if a predictor anticipated one-boxing, and nothing otherwise. A transparent box contains \(b=\$1{,}000\). Assume a symmetric prediction mechanism that matches either contemplated choice with probability \(q\).

With only one relevant input, policies reduce to the two constant choices. The P-FDT values are

\[
V(\pi_{\mathrm{one}})=qR,
\qquad
V(\pi_{\mathrm{two}})=(1-q)R+b.
\]

One-boxing is preferred exactly when

\[
(2q-1)R>b.
\]

For \(q=0.99\), the values are \(\$990{,}000\) and \(\$11{,}000\).

The qualification about the prediction mechanism matters. A historical statement that a predictor is “99% accurate” does not, by itself, specify accuracy under both policy counterfactuals. That requires further modeling.

P-FDT does not claim that taking one box sends a signal backward in time. It compares two hypothetical outputs of the computation that the predictor modeled. Different outputs correspond to different predictions and hence different box contents.

### The smoking lesion

Now suppose a lesion causes both a tendency to smoke and cancer, while smoking itself has no effect on cancer. In this fictional example, smoking adds utility \(c>0\).

If cancer does not subjunctively depend on the policy-selection output, then changing the smoking policy leaves its probability unchanged. Consequently,

\[
V(\pi_{\mathrm{smoke}})
-
V(\pi_{\mathrm{refrain}})
=c>0.
\]

P-FDT selects smoking without treating this as a means of altering—or receiving reassuring evidence about—the lesion.

The source itself cautions that the traditional smoking-lesion problem becomes contrived when preferences and self-knowledge are fully specified. Its useful lesson is structural: **a predictor’s response to a policy and a common cause of behavior are different dependencies**.

## 4. Observations belong inside the policy

P-FDT’s most distinctive recommendations arise when an observation depends on anticipated behavior. Conditioning on that observation before evaluating policies can eliminate precisely the dependency that policy selection was meant to retain.

### Transparent Newcomb

Suppose both boxes are transparent. The predictor fills the large box if it predicts that the agent would leave the small box behind **upon seeing the large box full**.

A policy now specifies two actions:

\[
\pi(\mathrm{full}),\qquad\pi(\mathrm{empty}).
\]

Consider

\[
\pi_C(\mathrm{full})=\mathrm{one},
\qquad
\pi_C(\mathrm{empty})=\mathrm{two}.
\]

Assume the predictor estimates \(\pi(\mathrm{full})\) with symmetric accuracy \(q\), and its decision determines which input the agent receives. Then

\[
V(\pi_C)=qR+(1-q)b.
\]

For the policy \(\pi_T\) that always takes both boxes,

\[
V(\pi_T)=(1-q)R+b.
\]

At \(q=0.99\), these are \(\$990{,}010\) and \(\$11{,}000\). The selected policy leaves the small box when the large box is full, but takes it when the large box is empty.

Even after observing fullness, the agent executes \(\pi_C(\mathrm{full})\). The policy comparison did not hold fullness fixed: a different policy would usually have produced a different observation.

This is not the belief that the observed box is secretly empty. Beliefs about actuality and instruments for evaluating alternatives play different roles.

Parfit’s hitchhiker has the same structure. A driver rescues the agent if the driver predicts payment after arrival. A policy of paying in the city can have greater value than a policy of keeping the money there, because rescue depends on the predicted response. Once rescued, P-FDT executes the selected policy rather than re-solving a problem that holds rescue fixed.

### Mechanical blackmail

Suppose a blackmailer launches a damaging program when it predicts payment. Payment costs \(c\); refusing after launch costs \(L\).

Under perfect prediction:

* a paying policy induces launch and loses \(c\);
* a refusing policy deters launch and loses nothing.

P-FDT selects refusal.

To see that this is not an unconditional rule against paying, assume instead that the blackmailer mistakenly launches against a refusing policy with probability \(\varepsilon\), while always launching against a paying policy. Then

\[
V(\pi_{\mathrm{pay}})=-c,\qquad
V(\pi_{\mathrm{refuse}})=-\varepsilon L.
\]

Refusal is preferred exactly when

\[
\varepsilon L<c.
\tag{3}
\]

A sufficiently unreliable deterrence mechanism can therefore make payment preferable.

These conclusions depend on the stipulated mechanism. If launch is independent of the agent’s policy, refusal offers no deterrence benefit. P-FDT does not turn every already-issued threat into an avoidable event.

## 5. Why whole policies can matter in multi-agent settings

Footnote 16 says the policy distinction matters in multi-agent dilemmas, but supplies no worked example. The following constructed example illustrates one reason it can matter; it is not attributed to the source.

Two agents implement the same policy-selection computation. Each receives a private bit, and their bits are always opposite. They choose actions \(0\) or \(1\). Each receives:

\[
u(0,0)=2,\qquad
u(1,1)=3,\qquad
u(0,1)=u(1,0)=0.
\]

There are four deterministic policies:

\[
(\pi(0),\pi(1))
\in\{(0,0),(0,1),(1,0),(1,1)\}.
\]

Because both agents use the selected policy, their common values are

\[
\begin{array}{c|cccc}
\pi &(0,0)&(0,1)&(1,0)&(1,1)\\ \hline
V(\pi)&2&0&0&3
\end{array}
\]

P-FDT chooses the constant-\(1\) policy.

Contrast this with a coordinate-wise procedure that changes only the output at one input while holding the output at the other input fixed. Starting from the constant-\(0\) rule, changing either coordinate alone creates disagreement and reduces utility from \(2\) to \(0\). Nevertheless, changing the complete policy raises utility to \(3\).

The distinction is between two optimization domains:

\[
\text{one input-specific output}
\quad\text{versus}\quad
\text{the whole input–output mapping}.
\]

This does not establish that every action-selection formulation must fail: its dependency model might link different input-specific outputs. It shows why replacing whole-policy optimization with independent local choices is not generally innocuous.

## 6. Applying P-FDT beyond familiar examples

A practical analysis can proceed in six steps.

1. **Specify outcomes and utility.** Include all relevant consequences, not merely immediate rewards.

2. **Define the inputs and policy domain.** List the observations or histories to which the policy must respond, including relevant unrealized branches.

3. **Identify the policy-selection computation.** Determine which physical implementations and predictors depend on it. Do not equate similarity with identity.

4. **Construct policy counterfactuals.** For each \(\pi\), recompute predictions, observations, actions, and outcomes that depend on that policy, leaving unrelated uncertainty unchanged.

5. **Calculate expected utility.** Evaluate \(V_M(\pi)\), including prediction errors and adverse branches.

6. **Select and execute.** Choose a maximizing policy and apply it to the actual input.

The difficult work lies in steps 2–4, not in the final maximization. Several unresolved choices deserve explicit treatment.

### The reference perspective

Footnote 16 does not specify a unique prior, an observation cutoff, or a rule for deciding which evidence may be conditioned upon before policy selection.

My operational proposal is to fix a reference model for the interaction and represent **policy-dependent observations inside that model**, rather than conditioning them away. Policy-independent background evidence can inform the model in the ordinary way.

This captures transparent Newcomb and blackmail while avoiding the claim that an agent must forever retain its earliest beliefs. But the boundary between learning the model and receiving a policy input is substantive. In unfamiliar cases, different boundaries can produce different recommendations. They should be stated and subjected to sensitivity analysis.

### Policy scope and feasibility

A policy could cover a single encounter, a repeated relationship, or a much larger range of circumstances. Footnote 16 does not settle its scope.

Policies should also be executable using the information available at each input. A purported policy that secretly depends on an unobserved state is not an available alternative.

For bounded agents, \(\Pi\) may need to be a restricted class of programs or heuristics, with computation costs included in utility. The result is then optimal only relative to that class and model.

### Randomization and copying

One may extend policies to \(\pi:\mathcal X\to\Delta(\mathcal A)\), but the source does not specify how randomization should work. Independent private random bits, shared random bits, and predictable pseudorandom bits produce different dependencies.

Two agents can share a randomized policy without sharing its realized action. A model that fails to distinguish these cases can assign spurious coordination benefits.

### What follows—and what does not

With a fixed reference model and counterfactual semantics, maximization ensures that no admissible policy has greater modeled expected utility. It does **not** prove that the model is correct or that P-FDT universally outperforms rival theories.

Likewise, free information has nonnegative policy value when the enlarged policy space includes an option to ignore it and that option preserves the old outcome distribution. If acquiring information changes others’ behavior, an additional argument is needed.

The paper motivates broader claims about reflective stability and performance in “fair” problems, but explicitly leaves a general optimality criterion unresolved. P-FDT’s examples are compelling tests of a perspective, not a completed universal theorem.

## Conclusion

P-FDT evaluates a complete rule for acting across inputs, preserving the dependencies between that rule, its implementations, and predictions of it. This can justify cooperation, honoring predicted agreements, and resisting extortion without confusing correlation with control.

Its central practical demand is precise modeling: specify the policy domain, the reference perspective, and what changes under each policy hypothetical. Footnote 16 provides the policy-selection idea; turning that idea into a general decision procedure still requires a defensible theory of those counterfactual dependencies.