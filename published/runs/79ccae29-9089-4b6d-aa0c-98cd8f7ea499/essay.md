# A-FDT: Choosing the Output of a Decision Procedure

A decision can occur in several places at once—not as a physical event, but as a computation. An agent reasons about what to do; a simulator runs the same reasoning; a predictor models its conclusion. These physical processes may be separated by time and distance while remaining constrained to produce corresponding answers.

**Action functional decision theory (A-FDT)** evaluates actions by taking such dependencies seriously. Its central question is not merely what consequences a bodily action would cause, nor what that action would reveal. It asks which output of the agent’s present decision computation corresponds to the best outcome.

This essay takes Equation (4), Section 5, of Yudkowsky and Soares’s paper as the defining presentation of A-FDT. That equation supplies a precise optimization rule **conditional on having an adequate dependency model**. Constructing that model remains the theory’s central unfinished task.

## 1. The mathematical object A-FDT evaluates

Let \(\mathcal A\) be a finite action set, \(\mathcal X\) a set of observation histories, and \(\mathcal O\) a countable outcome space. Let
\[
u:\mathcal O\longrightarrow\mathbb R
\]
be a utility function, with expectations assumed finite. Write \(O\) for the outcome variable and \(V=u(O)\).

All the decision theories considered here maximize expected utility. Their disagreement concerns the probability distribution used to evaluate each alternative.

**Evidential decision theory (EDT)** evaluates
\[
Q_{\mathrm{EDT}}(a;x)
=\mathbb E[V\mid X=x,A=a].
\]
An action is attractive insofar as learning that it occurs would be good news.

**Causal decision theory (CDT)** instead uses a causal model:
\[
Q_{\mathrm{CDT}}(a;x)
=\mathbb E[V\mid \operatorname{do}(A=a),X=x].
\]
Here \(\operatorname{do}(A=a)\) replaces the mechanism determining the physical action, while retaining the mechanisms governing its consequences.

A-FDT changes both the intervention target and the treatment of observations. Let \(P\) be a probabilistic world-model and \(G\) its dependency structure. Introduce a model variable
\[
D_{P,G,x}
\]
representing the mathematical output of the A-FDT procedure on the particular inputs \(P,G,x\). Renaming the notation of the paper’s Equation (4), its rule is
\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
\in
\arg\max_{a\in\mathcal A}
\mathbb E_{P,G}
\!\left[V\mid\operatorname{do}(D_{P,G,x}=a)\right].
}
\tag{A}
\]

A fixed tie-breaking convention can make this single-valued; this is an additional implementation convention.

The intervention concerns **this procedure on these inputs**, not every decision made by any agent using A-FDT. Different inputs ordinarily correspond to different logical-output variables. Whether their outputs are nevertheless related must be represented in \(G\).

Also, \(D_{P,G,x}\) is a variable *inside the model*, whereas \(\operatorname{A\!-\!FDT}(P,G,x)\) is the action actually returned. Manipulating the former helps calculate the latter.

The self-reference is deliberate: the procedure reasons about a representation of its own output. The paper invokes computational self-reference techniques to explain how such representations can exist without already knowing their values. That addresses the naming problem, not every problem of logical consistency or computational tractability.

## 2. A-FDT dependencies and counterpossibilities

The paper calls the relevant relationship **subjunctive dependence**. Two implementations of the same computation provide the clearest example. If both correctly calculate the same function on the same input, their answers cannot vary independently.

Prediction supplies a less exact version. A predictor might simulate an agent, analyze its program, or employ an imperfect model. Its prediction can then depend on the agent’s decision computation even though the eventual bodily action does not cause the earlier prediction.

A-FDT therefore distinguishes:

- **Causal dependence:** an action changes an outcome through an ordinary physical mechanism.
- **Computational or logical dependence:** another process implements or predicts the decision computation.
- **Merely evidential association:** observing the action supplies information, without the associated event depending on that computation’s output.

The distinction is not simply between intelligent and unintelligent processes. What matters is the dependency represented by the model.

### An operational interpretation

The source assumes that \(P,G\) support suitable interventions, but does not provide a general method for constructing them. For finite examples, a useful operational interpretation is an acyclic structural model:
\[
Z_i=f_i(\operatorname{Pa}_i,W),
\qquad W\sim\mu,
\]
where \(W\) represents background uncertainty and the parent relations may include computational as well as causal dependencies.

This is a modeling proposal, not a completed general foundation supplied by the paper. Under it, evaluating action \(a\) means:

1. Identify the logical-output node \(D_{P,G,x}\).
2. Replace its determining equation by \(D_{P,G,x}:=a\).
3. Retain the other mechanisms and background distribution.
4. Recompute downstream variables.
5. Average the resulting utilities.

Thus, if \(O^{[a]}(w)\) is the surgically recomputed outcome,
\[
Q_x(a)=\sum_w\mu(w)\,u\!\left(O^{[a]}(w)\right),
\]
with an integral replacing the sum when necessary.

A graph alone is insufficient: one needs response mechanisms, including responses to intervention values absent from the observational distribution. Two models can fit the same observed correlations yet prescribe different interventions.

There is also a foundational difficulty. A fixed mathematical function has only one output on fixed inputs. If that output is \(a\), supposing it instead outputs \(b\) is not merely contrary to fact; it may be contrary to logic.

A-FDT therefore requires **counterpossible reasoning**. Its hypotheticals are computational evaluation devices, not assertions that contradictory mathematical worlds physically exist. The structural interpretation above makes this manageable in stipulated examples by replacing one equation while preserving selected others. It does not establish that every logical intervention has a uniquely correct interpretation.

## 3. A-FDT in Newcomb’s problem and the smoking lesion problem

### Prediction-sensitive rewards

In Newcomb’s problem, an opaque box contains \(M=\$1{,}000{,}000\) if a predictor predicted one-boxing, and nothing otherwise. A transparent box contains \(s=\$1{,}000\). The agent chooses one box or both.

Assume the predictor has symmetric, intervention-stable accuracy \(q\):
\[
\Pr(\widehat A=a\mid\operatorname{do}(D=a))=q.
\]
This assumption is stronger than merely reporting an aggregate historical accuracy rate.

The A-FDT dependency structure includes
\[
D\longrightarrow A,
\qquad
D\longrightarrow\widehat A\longrightarrow B.
\]
The first arrow represents implementation; the second represents prediction. It is not a backward-in-time physical influence.

Consequently,
\[
Q(\text{one-box})=qM,
\]
whereas
\[
Q(\text{two-box})=(1-q)M+s.
\]
A-FDT one-boxes exactly when
\[
(2q-1)M>s.
\]
At \(q=0.99\), these values are \(\$990{,}000\) and \(\$11{,}000\).

CDT holds the earlier box contents fixed across its physical-action interventions, so taking the extra thousand dollars always wins in its comparison. A-FDT instead preserves the predictor’s dependence on the decision computation.

This is not the belief that choosing one box physically fills it. It is a judgment about which correspondence between computation, prediction, and action should remain intact when alternatives are evaluated.

### A common cause is different

In the fictional smoking lesion problem, a lesion produces both a tendency to smoke and cancer. Smoking itself does not cause cancer.

Let \(L\) denote the lesion and \(C\) cancer. The intended A-FDT model contains
\[
L\longrightarrow C
\]
but no dependence of \(L\) or \(C\) on the output of the smoking decision computation. Intervening on that output therefore does not improve health.

If smoking contributes a positive utility \(s\), and the computation controls the action in every modeled circumstance,
\[
Q(\text{smoke})-Q(\text{refrain})=s.
\]
A-FDT smokes in this fictional setting.

The source’s detailed treatment is more complicated because the lesion also affects preferences. It introduces different decision-input nodes for different utility functions. An intervention then changes the physical action only in circumstances where the intervened-on computation controls it. The utility gain is correspondingly weighted by that circumstance’s probability.

The authors acknowledge that the traditional lesion problem is contrived, especially concerning ignorance of preferences and population correlations. Its useful lesson is narrower: **a statistical association with disease is not automatically preserved under a decision-output intervention**. Nothing here supports smoking when smoking actually causes serious harm.

## 4. A-FDT and observation-dependent decisions

Equation (A) contains no additional conditioning on \(X=x\). Observation history selects the intervention node:
\[
x\mapsto D_{P,G,x}.
\]

This is crucial. Replacing Equation (A) by
\[
\arg\max_a
\mathbb E[V\mid\operatorname{do}(D_{P,G,x}=a),X=x]
\]
would change the assigned theory.

The absence of conditioning does not mean observations are denied or forgotten. An agent can believe with certainty that it received some observation while evaluating an alternative under which that observation would not have occurred. Belief and decision hypothetical are different objects.

### Transparent Newcomb

Suppose both boxes are transparent. The predictor fills the large box according to its prediction of what the agent would do **upon seeing it full**.

Define
\[
D_F=\operatorname{A\!-\!FDT}(P,G,\text{full}),
\qquad
D_E=\operatorname{A\!-\!FDT}(P,G,\text{empty}),
\]
understanding these expressions as labels for their corresponding model nodes.

The predictor tracks \(D_F\). Actual action is selected by the observation:
\[
A=
\begin{cases}
D_F,&B=\text{full},\\
D_E,&B=\text{empty}.
\end{cases}
\]

Intervening on \(D_E\) does not affect the prediction in this model. Taking both boxes when the large box is empty therefore gains the extra \(s\) whenever that branch occurs.

Now suppose prediction accuracy is \(q=0.99\), with the empty-box response fixed at two-boxing. Evaluating the full-box response gives
\[
Q_F(\text{one-box})
=qM+(1-q)s
=\$990{,}010.
\]
If that response instead outputs two-boxing,
\[
Q_F(\text{two-box})
=(1-q)(M+s)+qs
=\$11{,}000.
\]

A-FDT consequently one-boxes upon seeing a full box.

The unusual feature is the second hypothetical: changing \(D_F\) usually makes the predictor leave the box empty, so the agent then acts through \(D_E\), not \(D_F\). The intervention’s output need not become the physical action in every hypothetical branch.

Conditioning again on seeing a full box would remove precisely this comparison.

### Parfit’s hitchhiker

The same structure explains paying a driver after rescue from the desert. Let \(D_C\) represent the payment decision upon reaching the city. A driver offers rescue only when predicting that \(D_C\) outputs payment.

Intervening on \(D_C\) changes both the prospective payment and the probability of rescue. A-FDT can therefore pay in the city because the alternative output corresponds predominantly to remaining in the desert.

This is not a moral requirement to honor promises. It follows from the stipulated predictive dependency and the agent’s utility for survival.

## 5. A-FDT in coordination and blackmail

### Cooperation with a computational twin

Consider the paper’s prisoner’s dilemma payoffs: mutual cooperation yields each player \(\$1{,}000{,}000\), mutual defection yields \(\$1{,}000\), and unilateral defection yields the defector \(\$1{,}001{,}000\).

If both players implement the same relevant computation on the same inputs, their actions share an output node:
\[
A_1=D,\qquad A_2=D.
\]
The A-FDT comparison is then
\[
Q(\text{cooperate})=\$1{,}000{,}000,
\qquad
Q(\text{defect})=\$1{,}000.
\]

Cooperation is individually advantageous under this dependency, without altruistic utility.

But merely calling two players rational, similar, or adherents of A-FDT does not establish that dependency. Different information, utilities, or algorithms can produce different nodes. A-FDT does not prescribe unconditional cooperation with strangers.

### Prediction-sensitive blackmail

A blackmailer launches a costly threat only when predicting payment. Let \(D_B\) represent the response upon receiving the demand. Define
\[
\alpha=\Pr(T=1\mid\operatorname{do}(D_B=\text{pay})),
\]
\[
\beta=\Pr(T=1\mid\operatorname{do}(D_B=\text{refuse})).
\]

Assume payment costs \(c\), an executed threat costs \(L\), and no threat produces zero loss. Then
\[
Q(\text{pay})=-\alpha c,
\qquad
Q(\text{refuse})=-\beta L.
\]
A-FDT refuses when
\[
\beta L<\alpha c.
\]

For \(\alpha=1\), \(c=\$1{,}000\), \(L=\$1{,}000{,}000\), and \(\beta=0.0009\), refusal has expected loss \(\$900\), versus \(\$1{,}000\) for payment. A-FDT refuses even if the demand actually arrives.

These parameter choices are an explicit illustrative model. They demonstrate a threshold, not an absolute prohibition on paying. If threats occur independently of the response computation, then \(\alpha=\beta=1\); paying is preferable when \(c<L\).

The practical question is therefore not whether something is called blackmail, but whether launching the threat genuinely depends on the response computation.

## 6. Applying A-FDT without assuming away its open problems

For an unfamiliar case, the optimization is usually easier than specifying the hypotheticals. A disciplined application should answer four questions.

**Which computation is being evaluated?** Specify its inputs, including observations, preferences, and relevant model information. Similar-looking choices need not instantiate identical computations.

**What depends on that computation?** Identify actual implementations, simulations, prediction mechanisms, and ordinary causal consequences. Do not infer intervention-stable dependence from correlation alone.

**How are observations generated?** Represent the mechanism selecting which observation-dependent computation controls action. Otherwise one may accidentally fix evidence that Equation (A) allows to vary.

**Which mechanisms survive intervention?** State error assumptions, background uncertainty, and responses outside observational support. Then compute expected utilities, preferably checking sensitivity to uncertain dependencies.

The last step matters greatly. Historical predictor accuracy does not uniquely determine its response to a counterpossible change in an algorithm’s output. Nor does observational data generally identify logical structure. Where several dependency models remain credible, averaging their action values using explicitly chosen model weights is a reasonable proposal:
\[
Q_x(a)=\sum_k w_k Q_x^{(k)}(a).
\]
The source does not derive a general method for selecting those models or weights.

### Actions are not whole policies

A policy is a map \(\pi:\mathcal X\to\mathcal A\). The source’s footnotes describe a preferred variant that selects policies rather than actions. That is not Equation (4)’s action-valued rule.

A-FDT intervenes on one input-specific output, \(D_{P,G,x}\). It does not automatically replace every response \(D_{P,G,y}\) with a jointly optimized policy. Other responses change only through dependencies supplied by the model.

Transparent Newcomb already gives the rule a policy-like character: deciding one response can change which response is physically implemented. Nevertheless, optimizing one component of a response map is not generally equivalent to optimizing the entire map simultaneously. Any extension to whole-policy optimization needs separate specification, especially in multi-agent settings.

### What the motivation establishes

The source motivates A-FDT through successful prediction-sensitive behavior, reduced need for costly precommitments, and resistance to exploitation. These are substantive advantages in its examples.

They are not a proved universal optimality theorem. The paper acknowledges that decision procedures can be selectively rewarded or punished, and leaves a satisfactory formal definition of “fair” comparison unresolved. Its broader claims about stability and information should likewise not be treated as consequences of Equation (A) under arbitrary models.

A-FDT’s defensible central proposal is more specific: expected-utility comparisons should preserve relevant computational dependencies, not only physical causal consequences or observational associations.

## References

1. Eliezer Yudkowsky and Nate Soares. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2, especially §§3–6 and footnotes 7 and 16.
2. Judea Pearl. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.
3. James M. Joyce. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

## Conclusion

A-FDT evaluates actions by intervening on the represented output of the present decision computation and maximizing the resulting expected utility. Its distinctive strengths come from preserving predictive and computational dependencies while allowing even observed circumstances to vary across decision hypotheticals. Given explicit mechanisms, this yields usable calculations. What remains unfinished is a general account of which logical interventions are justified—and how an agent should learn their structure.