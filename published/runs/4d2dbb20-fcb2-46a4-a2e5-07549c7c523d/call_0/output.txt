# A-FDT: Choosing the Output of a Decision Procedure

Decision theories disagree not only about what outcomes are desirable, but also about which hypothetical outcomes should guide action. Suppose a reliable predictor has already rewarded or penalized you according to its prediction of your present choice. Should deliberation hold that prediction fixed, because it lies in the past? Or should alternative choices be evaluated alongside corresponding alternative predictions?

**Action functional decision theory (A-FDT)** takes the second approach when the prediction depends appropriately on the computation producing your choice. It evaluates an action by hypothetically changing the output of the agent’s decision procedure, propagating that change through the relevant dependencies, and calculating expected utility.

Here, A-FDT means specifically the action-valued rule presented in Section 5, Equation (4), of Yudkowsky and Soares’s paper [1]. This qualification matters: the paper also discusses selecting entire policies, but Equation (4) maximizes over actions. We should not silently replace its intervention on a particular computation with optimization over every aspect of an agent’s behavior.

A-FDT’s central proposal is clear once a suitable world-model is supplied. Its principal unresolved problem is how to construct that model—especially its representation of logical and computational dependence.

## 1. The formal rule

Let:

- \(\mathcal A\) be a finite set of available actions;
- \(\mathcal X\) be a set of observation histories;
- \(O\) be an outcome variable;
- \(U(O)\) be a utility function, with finite relevant expectations;
- \(P\) be a probabilistic world-model;
- \(G\) describe the dependencies used to construct decision hypotheticals.

Write \(V=U(O)\). Crucially, the model includes a variable representing what the decision procedure outputs on specified inputs. Denote this variable by
\[
D_{P,G,x}.
\]
It represents the mathematical value of \(\operatorname{A\!-\!FDT}(P,G,x)\), rather than merely the agent’s physical movement.

With this abbreviation, the paper’s Equation (4) becomes
\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
=
\operatorname*{arg\,max}_{a\in\mathcal A}
\mathbb E_P\!\left[
V\mid \operatorname{do}(D_{P,G,x}=a)
\right].
}
\tag{A}
\]
A fixed tie-breaking convention can make this a single-valued function.

The notation \(\operatorname{do}\) describes a modification of the model, not ordinary conditioning. A-FDT constructs a hypothetical in which the designated computation outputs \(a\), then updates whatever depends on that output according to \(G\).

Compare two distinct theories:
\[
\operatorname{EDT}(P,x)
=
\operatorname*{arg\,max}_a
\mathbb E_P[V\mid X=x,A=a],
\]
and
\[
\operatorname{CDT}(P,G_{\mathrm c},x)
=
\operatorname*{arg\,max}_a
\mathbb E_P[V\mid \operatorname{do}(A=a),X=x].
\]
Evidential decision theory (EDT) conditions on performing an action. Causal decision theory (CDT) intervenes on the physical action variable \(A\). A-FDT instead intervenes on the output of the computation producing the decision.

There is another important difference: Equation (A) contains **no additional conditioning on \(X=x\)**. Observation history selects the computational variable being intervened upon. This feature is essential, not a dispensable notational choice.

Thus A-FDT is not simply CDT with extra arrows from actions to past predictions. Its intervention target changes, and observations enter its decision rule differently.

## 2. What dependencies should survive?

The paper calls the relevant relationship *subjunctive dependence*. Its clearest examples involve multiple implementations or representations of the same computation.

Suppose two reliable calculators evaluate the same sum. Changing one calculator’s physical display need not change the other display. But a hypothetical change in the mathematical answer should be reflected in both calculations. Similarly, an agent and a sufficiently faithful simulation of that agent may implement corresponding computations even when they cannot communicate.

A-FDT evaluates alternatives at this computational level. Its hypothetical changes:

1. the designated decision output;
2. physical actions implementing that output;
3. predictions, copies, and other computations that depend appropriately on it;
4. subsequent consequences of those changes.

It does not preserve every observed correlation. A disease that independently produces both a preference and an illness need not depend on the output of the preference-sensitive decision procedure.

Nor does A-FDT claim retrocausation. A past prediction can vary across its hypotheticals without being physically changed by the present action. The intervention modifies a representation used for deliberation; it sends no signal into the past.

This distinction creates a philosophical difficulty. A fixed deterministic function on fixed inputs has only one output. If its output is actually \(a\), supposing that it outputs \(b\ne a\) is a **counterpossible**, not an ordinary physically unrealized possibility.

The paper acknowledges this explicitly. Its proposed response is to supply dependency structure sufficient for the particular counterpossible comparisons needed in decision-making. It does not provide a general semantics for reasoning under arbitrary false mathematical assumptions.

That limitation matters. Without disciplined counterpossible semantics, one could justify almost any choice by inventing convenient dependencies.

## 3. An operational interpretation

Equation (A) becomes executable once the model specifies how variables respond to interventions. The following is a useful operational completion, consistent with the paper’s examples but more explicit than its general specification.

Assume a finite acyclic structural model. Each endogenous variable \(Z_i\) has a mechanism
\[
Z_i=f_i(\operatorname{pa}_i,W),
\]
where \(\operatorname{pa}_i\) lists its parents and \(W\) collects exogenous uncertainty.

For candidate action \(a\):

1. Replace the mechanism for \(D_{P,G,x}\) by the constant \(a\).
2. Leave other mechanisms and the exogenous distribution unchanged.
3. Recompute downstream variables.
4. Evaluate expected utility.

Writing \(O_a(w)\) for the resulting outcome,
\[
Q_x(a)=\sum_w P(W=w)\,U(O_a(w)),
\qquad
a^*\in\operatorname*{arg\,max}_a Q_x(a).
\tag{B}
\]

This supplies concrete meaning to “preserve dependencies”: preserve the response mechanisms, rather than freezing their outputs.

Two qualifications are essential.

First, a bare graph is insufficient. One also needs response probabilities or structural equations, including responses to parent configurations never observed in the actual distribution. This is especially important when intervening on logically determined variables. Observational probabilities alone need not determine such off-support behavior.

Second, the computational equations are deliberately relaxed at the intervention point. We do not both impose \(D_{P,G,x}=a\) and demand that it retain its original value, then reason classically from the resulting contradiction. We replace one constraint and propagate a specified collection of others.

This interpretation makes simple cases tractable without solving counterpossible reasoning generally. It also reveals what the paper leaves open: discovering the right computational variables, response mechanisms, and dependency directions.

Self-reference adds another issue. The model represents the output of the very procedure consulting that model. The paper invokes self-representing programs to explain how such a variable can be named without already knowing its value. That addresses representation; it is not a general proof that every self-referential dependency model is coherent or efficiently solvable.

## 4. A-FDT in Newcomb’s problem and the smoking lesion

### Newcomb’s problem

Let \(M=\$1{,}000{,}000\) be placed in an opaque box if a predictor forecasts one-boxing. A transparent box contains \(s=\$1{,}000\), which the agent receives only by two-boxing.

Assume, as an additional explicit modeling assumption, a symmetric prediction mechanism with accuracy \(r\). Under the computational interventions,
\[
P(B=M\mid\operatorname{do}(D=\text{one-box}))=r,
\]
\[
P(B=M\mid\operatorname{do}(D=\text{two-box}))=1-r.
\]
Then
\[
Q(\text{one-box})=rM,
\qquad
Q(\text{two-box})=(1-r)M+s.
\]
A-FDT one-boxes precisely when
\[
(2r-1)M>s.
\]
At \(r=0.99\), the scores are \(\$990{,}000\) and \(\$11{,}000\).

The mechanism matters more than the accuracy statistic. Historical accuracy of \(99\%\), by itself, does not establish symmetric reliability under both interventions. More generally, if the interventional probabilities of a full box are \(p_1,p_2\), A-FDT one-boxes when
\[
M(p_1-p_2)>s.
\]
Those probabilities require a predictive-dependence model, not merely an observed correlation.

CDT instead holds the existing box contents fixed across its action interventions, making two-boxing better by \(s\). A-FDT rejects that comparison because it detaches the action from the computation the predictor was predicting.

### The smoking lesion

Now suppose a lesion causes both cancer and a tendency to enjoy smoking, but smoking itself does not cause cancer. For an agent who enjoys smoking, let
\[
V=H(C)+b\,\mathbf1_{\{A=\text{smoke}\}},
\qquad b>0,
\]
where \(C\) describes the health outcome.

If neither the lesion nor cancer depends on the intervened decision output, their distribution remains unchanged. When the designated computation controls the action,
\[
Q(\text{smoke})-Q(\text{refrain})=b.
\]
A-FDT therefore recommends smoking in this imaginary medical environment.

This conclusion is not an endorsement of smoking in reality, where smoking has causal health consequences.

The paper also complicates its own lesion example: the lesion changes preferences, potentially selecting between different preference-dependent computations. In its fuller model, intervening on one such computation changes behavior only when that computation controls the action. The expected benefit is correspondingly weighted by the probability of control.

The lesson survives: changing a computation’s output does not thereby remove a disease that influences which computation is implemented. The paper nevertheless regards the traditional lesion problem as contrived, not as an unqualified refutation of every sophisticated version of EDT.

## 5. Observations select the intervention: transparent Newcomb

Transparent Newcomb reveals A-FDT’s most distinctive feature.

The agent sees both boxes. The predictor fills the large box according to what the agent would do **upon seeing it full**. Define
\[
D_F=\operatorname{A\!-\!FDT}(P,G,\text{full}),
\qquad
D_E=\operatorname{A\!-\!FDT}(P,G,\text{empty}),
\]
where these expressions abbreviate corresponding model variables.

The predictor responds to \(D_F\). The physical action is selected by the observation:
\[
A=
\begin{cases}
D_F,&B=M,\\
D_E,&B=0.
\end{cases}
\]

Assume symmetric predictive accuracy \(r\), and suppose \(D_E\) outputs two-boxing. This latter choice is optimal in the simple model because changing \(D_E\) does not change whether the box is filled.

After observing a full box, A-FDT intervenes on \(D_F\). It does **not** additionally condition its evaluation on the box remaining full.

If \(D_F=\text{one-box}\), then with probability \(r\) the box is full and the agent receives \(M\). Otherwise it is empty, \(D_E\) controls the action, and the agent receives \(s\). Hence
\[
Q_F(\text{one-box})=rM+(1-r)s.
\]
If \(D_F=\text{two-box}\), then
\[
Q_F(\text{two-box})
=(1-r)(M+s)+rs
=(1-r)M+s.
\]
For \(r=0.99\), these scores are \(\$990{,}010\) and \(\$11{,}000\). A-FDT leaves the small box behind.

The striking point is that, in the second hypothetical, the agent probably sees an empty box and implements a *different* observation-indexed computation. The candidate output need not become the physical action in every branch.

This is not an epistemic claim that the visibly full box might actually be empty. It is a rule for constructing decision hypotheticals that can differ from the actual observation history.

Parfit’s hitchhiker has the same structure. The driver rescues the agent according to a prediction of payment after reaching safety. A-FDT evaluates the output of the “already rescued” computation while allowing that output to affect whether rescue occurs. It consequently pays under the paper’s assumptions, without a binding precommitment.

Simply replacing \(P\) by \(P(\cdot\mid X=x)\) before applying Equation (A) would generally destroy this behavior. Equation (4) therefore requires care about what information is incorporated into the model and what remains represented by observation-indexed branches. The paper illustrates this architecture but does not fully specify how an unrestricted learning agent should maintain it over time.

## 6. Twins, cooperation, and policies

In the paper’s psychological-twin prisoner’s dilemma, mutual cooperation gives each player \(\$1{,}000{,}000\), mutual defection gives each \(\$1{,}000\), and unilateral defection gives the defector \(\$1{,}001{,}000\).

If both choices implement the same relevant computation \(D\), then
\[
\operatorname{do}(D=\text{cooperate})
\Longrightarrow (A_1,A_2)=(C,C),
\]
\[
\operatorname{do}(D=\text{defect})
\Longrightarrow (A_1,A_2)=(D,D).
\]
A-FDT cooperates for self-interested reasons.

This does not imply cooperation with arbitrary strangers. Sharing a decision-theoretic label does not establish identical computations. Different evidence, utilities, or computational limitations can break the dependency. A-FDT requires a justified relationship, not a presumption that other people mirror one’s choice.

The example also clarifies the action–policy distinction. For fixed \(P,G\), the outputs
\[
\pi(x)=\operatorname{A\!-\!FDT}(P,G,x)
\]
form an observation-dependent policy. But Equation (A) evaluates a designated output \(D_{P,G,x}\); it does not directly optimize over all mappings \(\pi:\mathcal X\to\mathcal A\).

A whole-policy intervention could jointly change behavior at many distinct inputs. The paper’s footnotes prefer such a formulation and acknowledge possible differences in multi-agent problems. That is a further theory specification. Results requiring coordinated changes across different inputs cannot automatically be attributed to Equation (4).

## 7. Blackmail and imperfect prediction

A-FDT’s resistance to blackmail is conditional on the targeting mechanism.

Suppose a blackmailer initiates a threat whenever it predicts payment. Paying costs \(c\); refusing an initiated threat costs \(L\). Assume, for illustration, that payment is always predicted correctly, while refusal is mistakenly predicted as payment with probability \(\varepsilon\).

The computational-intervention scores are
\[
Q(\text{pay})=-c,
\qquad
Q(\text{refuse})=-\varepsilon L.
\]
Thus A-FDT refuses when
\[
\varepsilon L<c.
\]
For \(c=\$1{,}000\) and \(L=\$1{,}000{,}000\), refusal is favored when \(\varepsilon<0.001\).

This calculation explains why A-FDT can refuse even after receiving the threat: its refusal hypothetical includes the reduced probability of being targeted. But it also shows why “A-FDT never pays blackmail” is false. Sufficient targeting error can make payment preferable.

Likewise, if the threat was initiated independently of any prediction of this decision procedure, the targeting probability does not change under the intervention. Paying may then be best. One cannot obtain deterrence merely by imagining that a determined attacker would have behaved differently.

## 8. Applying A-FDT responsibly

For an unfamiliar case, the practical procedure is:

1. **Specify utilities and outcomes.** Include prediction errors, implementation failures, and outcomes outside the observed branch.
2. **Identify the intervention target.** Which computation, on which inputs, is currently being evaluated?
3. **Justify dependency mechanisms.** Separate causal consequences, computational copies, predictive models, common causes, and accidental correlations.
4. **Represent observation selection.** Determine whether changing the target output changes which observation or decision branch occurs.
5. **Compute and compare interventional expectations.** Test sensitivity to uncertain mechanisms rather than treating a predictor’s claimed accuracy as sufficient.

The mathematical maximization is usually easier than these modeling tasks.

The paper argues that its approach outperforms CDT and EDT in the examples considered. It does not prove universal superiority. Its proposed category of “fair” problems remains informal, and it explicitly acknowledges that no decision theory wins every adversarially constructed test.

Nor does an expected-utility representation theorem settle the controversy. Such a theorem can justify maximizing expected utility once the evaluation perspective is fixed; it does not establish that A-FDT’s counterpossibles are the correct ones.

### References

[1] Eliezer Yudkowsky and Nate Soares. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2. Especially §§3–6, 9 and footnotes 7, 16.

[2] Judea Pearl. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.

## Conclusion

A-FDT evaluates actions as alternative outputs of a particular decision computation. It preserves relevant predictive and computational dependencies while breaking correlations that do not survive that intervention. Its observation-indexed rule can therefore recommend cooperation, payment after rescue, and resistance to prediction-dependent threats.

Given suitable response mechanisms, the calculation is precise. What remains unsettled is how to identify those mechanisms and construct reliable counterpossible models. A-FDT is consequently both a usable framework for well-specified problems and an unfinished account of general rational deliberation.