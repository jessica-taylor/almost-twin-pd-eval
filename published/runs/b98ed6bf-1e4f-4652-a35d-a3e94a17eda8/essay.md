# A-FDT: Choosing the Output of a Decision Procedure

A decision can be considered both as a physical event and as the output of a computation. Usually this distinction makes no practical difference. When choosing between two ordinary purchases, we can compare their consequences without considering whether another system predicts or reproduces our reasoning. But predictions, simulations, and computational copies make the distinction important.

**Action functional decision theory (A-FDT)** evaluates actions by counterfactually varying the output of the decision procedure producing them. Its central question is not merely what would happen if one’s body acted differently, but what would happen if **this very decision procedure, on these inputs, returned a different action**.

This essay takes Equation (4), Section 5, of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality* as its primary definition. The designation A-FDT emphasizes that this equation selects an action. The paper also mentions a preferred policy-selecting formulation, but those remarks do not determine all the details of that different optimization problem.

A-FDT’s maximization rule is compact. The substantial work lies in specifying the counterfactual model over which it maximizes.

## 1. The formal rule

Let:

- \(\mathcal A\) be a finite action set;
- \(\mathcal X\) be a countable set of observation histories;
- \(O\) be an outcome variable;
- \(U(O)\) be real-valued utility, with finite relevant expectations;
- \(P\) be a probabilistic world-model;
- \(G\) describe the world’s relevant causal, computational, and logical dependencies.

For each input triple \((P,G,x)\), introduce a model variable
\[
D_x:=\text{the output of A-FDT on inputs }(P,G,x).
\]
This is a variable **representing** a computation’s output, not the output itself. The source uses underlining to construct the appropriate variable name from the inputs; the abbreviation \(D_x\) suppresses that notation.

Equation (4), relabeled for this essay, is
\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
\in
\arg\max_{a\in\mathcal A}
\mathbb E_{P,G}\!\left[U(O)\mid\operatorname{do}(D_x=a)\right].
}
\tag{A}
\]
A deterministic implementation additionally needs a tie-breaking convention.

The intervention changes the represented output of the decision computation. It then propagates that change through the dependencies specified by \(G\). These may include the physical action, another implementation of the same computation, or a predictor’s estimate of its result.

For comparison, evidential decision theory (EDT) evaluates
\[
Q_{\mathrm{EDT}}(a;x)
=\mathbb E[U(O)\mid X=x,A=a],
\]
whereas causal decision theory (CDT), in the paper’s graphical formulation, evaluates
\[
Q_{\mathrm{CDT}}(a;x)
=\mathbb E[U(O)\mid\operatorname{do}(A=a),X=x].
\]
EDT conditions on an action; CDT intervenes on a physical action; A-FDT intervenes on a computational output.

There is another crucial difference: **Equation (A) does not additionally condition on \(X=x\)**. Observation history determines which computation-variable is intervened upon. In appropriate counterfactuals, changing that variable can change which observations occur.

## 2. What should vary with the computation?

The paper calls the relevant relation **subjunctive dependence**. Two physical systems implementing the same mathematical function can have corresponding outputs without either physically influencing the other. Likewise, an accurate predictor’s estimate can depend on a computation it represents, even when its prediction occurs earlier.

Suppose two isolated machines evaluate the same deterministic function on identical inputs. A-FDT represents their shared answer by a common computational variable \(D\). Under the hypothetical \(D=a\), both implementations produce \(a\). This does not posit communication between the machines.

Conversely, correlation alone does not establish subjunctive dependence. A medical condition might cause both a desire and a disease. Changing what a decision procedure recommends need not change that condition.

Thus A-FDT preserves neither every correlation nor only forward causal influence. It preserves the dependencies appropriate to the intervention target.

This requires **counterpossible reasoning**. A fixed deterministic function has only one actual output on fixed inputs. If its output is \(a\), the supposition that it instead outputs \(b\) contradicts a mathematical fact. The paper treats such suppositions as decision-making instruments rather than descriptions of ordinary possible worlds.

The intended operation cannot be “assume the false equation and derive everything classically”: contradiction would make inference useless. Instead, the model must specify a controlled replacement of one computational output while retaining selected surrounding relationships.

That is also why A-FDT is not simply choosing a different algorithm. A predictor may be predicting the actual algorithm, including its deliberation. Replacing it with another algorithm does not automatically explain how predictions of the original algorithm should change.

## 3. An operational interpretation—and its limits

The source explicitly acknowledges that it does not supply a general method for discovering subjunctive dependencies, or establish that Pearl-style graphs can represent them satisfactorily in every case.

For finite examples, a useful operational completion is a structural model
\[
Z_i=g_i(\operatorname{Pa}_i,\eta_i),
\]
with jointly distributed background variables \(\eta\). Assume an acyclic dependency structure. To evaluate action \(a\):

1. replace the equation governing \(D_x\) with \(D_x:=a\);
2. retain the other structural equations;
3. propagate the replacement through descendants;
4. average the resulting utility over the unchanged background distribution.

Writing \(O^{(a)}(\eta)\) for the resulting outcome,
\[
Q_x(a)=
\mathbb E_\eta\!\left[U\!\left(O^{(a)}(\eta)\right)\right].
\]

This is an operational interpretation of the graphical proposal, not a solution to its foundational problems. The arrows need not represent temporal causation.

Importantly, **a graph alone is insufficient**. One needs quantitative response rules, including behavior at parent assignments that never actually occur. An observational distribution may fit many incompatible intervention models. Knowing that a predictor is usually correct, for example, does not by itself determine how its predictions respond to counterpossible changes in this particular computation.

Self-reference creates a separate issue. The computation represented by \(D_x\) evaluates interventions on \(D_x\). As the paper observes, representing a computation does not require already knowing its result; recursion-theoretic constructions can support self-description. But representability does not establish termination, tractability, or universally coherent counterfactual semantics.

## 4. A-FDT in opaque Newcomb’s problem

Let the opaque box contain either \(M=\$1{,}000{,}000\) or nothing, while a transparent box contains \(c=\$1{,}000\). The predictor fills the opaque box exactly when it predicts one-boxing.

Assume a **symmetric counterfactual prediction model**: under either intervention on the decision output, the predictor matches it with probability \(r\). This is stronger than merely knowing its historical accuracy.

The dependency structure is
\[
D\longrightarrow A,
\qquad
D\longrightarrow \widehat A\longrightarrow B,
\qquad
(A,B)\longrightarrow U.
\]
Here \(D\to\widehat A\) expresses computational dependence, not backward physical causation.

A-FDT assigns
\[
Q(\text{one})=rM,
\qquad
Q(\text{two})=(1-r)M+c.
\]
Hence it one-boxes exactly when
\[
(2r-1)M>c.
\]
For \(r=0.99\), these values are \(\$990{,}000\) and \(\$11{,}000\).

CDT instead holds the opaque box’s contents fixed across physical-action interventions, making two-boxing worth an additional \(c\). The disagreement concerns which relationship an alternative-action hypothetical should preserve.

A-FDT does not claim that reaching for a box changes the past. It compares outputs of a computation whose result was already represented by the predictor. A different output is evaluated together with the corresponding prediction.

The dependence assumption matters. If the alleged predictor merely guesses independently, there is no appropriate \(D\to\widehat A\) response, and A-FDT takes both boxes.

## 5. A-FDT with lesions and twins

### A-FDT and a common-cause correlation

In the fictional smoking-lesion problem, a lesion causes both smoking-related preferences and cancer; smoking itself does not cause cancer. Suppose smoking supplies utility \(s>0\), and let \(C\) indicate cancer:
\[
U=s\,\mathbf 1_{\{A=\text{smoke}\}}-LC.
\]

If intervening on the relevant decision output changes smoking but leaves the lesion and cancer mechanisms unchanged, then
\[
Q(\text{smoke})-Q(\text{refrain})=s>0.
\]
A-FDT smokes in this stipulated world. This conclusion has no application to actual smoking, where smoking causes substantial harm.

The source’s detailed treatment is more complicated because the lesion affects preferences and therefore which decision computation controls behavior. It also acknowledges problems with the example’s informational assumptions. The robust lesson is narrower: an upstream common cause should not change merely because its downstream action is statistically associated with it.

### A-FDT and a psychological twin

Now consider a prisoner’s dilemma against a perfect computational twin. Mutual cooperation pays each player \(\$1{,}000{,}000\); mutual defection pays \(\$1{,}000\). A unilateral defector receives \(\$1{,}001{,}000\), while the cooperator receives nothing.

If both agents implement the same relevant computation, then
\[
A_{\mathrm{self}}=D,\qquad A_{\mathrm{twin}}=D.
\]
Consequently,
\[
Q(\text{cooperate})=\$1{,}000{,}000,
\qquad
Q(\text{defect})=\$1{,}000.
\]
A-FDT cooperates for self-interested reasons.

This is not a general instruction to cooperate. Identical theory labels do not imply identical computations: inputs, utilities, information, and implementations matter. With an unrelated opponent whose response does not subjunctively depend on the selected computation, ordinary unilateral incentives remain.

## 6. Observations: the decisive feature of Equation (4)

Transparent Newcomb’s problem makes the absence of observational conditioning essential.

Both boxes are visible. The predictor fills the large box if it predicts that the agent would one-box **upon seeing it full**. Introduce two computational variables:
\[
D_F=\operatorname{A\!-\!FDT}(P,G,\text{full}),
\qquad
D_E=\operatorname{A\!-\!FDT}(P,G,\text{empty}).
\]
Physical action is selected by
\[
A=
\begin{cases}
D_F,&B=M,\\
D_E,&B=0.
\end{cases}
\]

The predictor targets \(D_F\), not the action eventually selected on every possible observation branch. Thus an intervention on \(D_F\) can change the prediction, box contents, observation, and which computational variable controls the action.

Assume symmetric prediction accuracy \(r\), and suppose the empty-box computation selects both boxes. This latter choice is optimal in the model because changing \(D_E\) does not affect the filling decision and earns \(c\) whenever implemented.

Then
\[
Q_F(\text{one})=rM+(1-r)c,
\]
whereas
\[
Q_F(\text{two})=(1-r)(M+c)+rc=(1-r)M+c.
\]
With \(r=0.99\), the values are \(\$990{,}010\) and \(\$11{,}000\).

A-FDT therefore one-boxes even after seeing the large box full. Its alternative hypothetical allows that it would instead have seen an empty box.

Adding conditioning on “full” would remove this comparison and would not implement Equation (4). The current input remains part of the **identity of the computation being evaluated**, even when that computation is not physically executed in some resulting hypotheticals.

This does not mean observations never guide A-FDT. In an ordinary case where changing \(D_x\) cannot affect whether history \(x\) occurs, utility differences often have the form
\[
Q_x(a)-Q_x(b)
=
P(X=x)\,\Delta_x(a,b).
\]
Outcomes on other observation branches cancel. Provided \(P(X=x)>0\), maximizing the unconditional expression gives the same ranking as maximizing the branch-specific difference \(\Delta_x\). This is a useful consequence under those structural assumptions, not a universal identity.

## 7. A-FDT, repayment, and resistance to threats

Parfit’s hitchhiker has the same structure as transparent Newcomb’s problem. A driver rescues a stranded agent only if she predicts repayment after arrival. Let survival be worth \(V\), repayment cost \(c\), and prediction accuracy be \(r\).

Intervening on the “in the city” computation gives
\[
Q_{\mathrm{city}}(\text{pay})=r(V-c),
\qquad
Q_{\mathrm{city}}(\text{refuse})=(1-r)V.
\]
A-FDT pays when
\[
(2r-1)V>rc.
\]
With the paper’s stakes, repayment wins overwhelmingly.

Once again, refusing is evaluated together with its effect on whether rescue occurs. The rationale requires neither gratitude nor an enforceable contract. Predictable repayment makes beneficial assistance available.

Mechanical blackmail reverses the incentive. A blackmailer initiates a damaging process when she predicts payment; payment then stops it. Let \(L\) be the damage and \(c\) the demand. Define
\[
t_P=P(\text{threat initiated}\mid\operatorname{do}(D_{\mathrm{letter}}=\text{pay})),
\]
\[
t_R=P(\text{threat initiated}\mid\operatorname{do}(D_{\mathrm{letter}}=\text{refuse})).
\]
Assuming payment reliably prevents damage,
\[
Q(\text{pay})=-t_Pc,\qquad
Q(\text{refuse})=-t_RL.
\]
A-FDT refuses when
\[
t_RL<t_Pc.
\]

For \(t_P=1\), \(t_R=0.0009\), \(L=\$1{,}000{,}000\), and \(c=\$1{,}000\), refusal loses \(\$900\) in expectation, versus \(\$1{,}000\) for payment. At \(t_R=0.0011\), payment instead wins.

The theory therefore does not categorically reject threats. If initiation is independent of the repayment computation, so \(t_R=t_P>0\), paying is preferable whenever \(c<L\). What matters is the modeled incentive dependence, not the word “blackmail.”

## 8. Applying A-FDT beyond the examples

A practical analysis should separate four tasks.

**First, identify the computation.** Specify its model, observation input, utility function, and action set. Similar-looking decisions need not share an output variable.

**Second, specify response mechanisms.** Which systems implement or predict this computation? Which correlations arise only from common causes? What errors, random seeds, or implementation failures remain unchanged under intervention?

**Third, construct each hypothetical.** Set \(D_x=a\), propagate through the specified mechanisms, and allow observations to change when they are downstream. Do not quietly replace this operation with conditioning on \(A=a\).

**Fourth, compare expected utilities and test sensitivity.** If several dependency models are plausible, calculate whether they agree. Averaging across uncertain graphs is a reasonable further proposal, but requires additional assumptions about how those graphs are represented and how interventions act within them.

There is also an unresolved modeling boundary: what information belongs in the fixed background model \(P\), and what information appears as the observation input \(x\)? Replacing \(P\) with an already-conditioned model can eliminate alternatives the original graph was meant to compare. The paper’s examples specify this boundary, but do not provide a universally applicable procedure for choosing it.

### Actions versus policies

A policy is a map
\[
\pi:\mathcal X\to\mathcal A.
\]
For fixed \((P,G)\), the family of outputs \(D_x\) describes such a map. Nevertheless, Equation (A) intervenes on **one observation-indexed output**, not jointly on an entire policy.

A simultaneous policy intervention could alter several branches and their predictions together. That need not agree with maximizing over one branch while leaving other output variables governed by the model.

The paper’s footnotes explicitly favor a policy-output formulation and acknowledge possible differences in multi-agent dilemmas. They do not license silently treating Equation (4) as unrestricted policy optimization. Applying A-FDT to a new multi-stage problem therefore requires specifying which output variables each intervention changes and how those changes interact.

## 9. Motivation without an optimality theorem

A-FDT’s philosophical attraction is that it treats prediction and replication as parts of the decision-relevant world. A computational output can matter beyond its immediate bodily implementation. Ignoring that structure can make cooperation, repayment, and resistance to exploitation systematically fail.

Its challenge to dominance arguments is correspondingly specific. Two-boxing dominates when box contents are held fixed. That does not settle whether fixed contents provide the appropriate comparison when the predictor represents the very computation being evaluated. The counterfactual framework helps determine what counts as dominance.

Still, success in these examples is not a universal optimality proof. The authors acknowledge that environments can arbitrarily reward or punish particular decision procedures. Their proposed restriction to “fair” problems—roughly, problems rewarding behavior rather than algorithm identity—remains incompletely formalized.

Likewise, the source’s broad claims about precommitment, information, and reflective stability should be distinguished from what Equation (4) alone establishes. Without a satisfactory general semantics for subjunctive dependence, those claims remain motivations and research conjectures rather than unrestricted guarantees.

## References

Yudkowsky, E., and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2, especially §§3–6 and 9, and notes 7 and 16.

Pearl, J. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.

## Conclusion

A-FDT selects actions by intervening on the represented output of the decision computation currently under consideration. It preserves the model’s relevant computational and causal dependencies while breaking correlations that should not survive that intervention. Crucially, its hypotheticals may change which observations occur.

Given an adequate dependency model, the rule is straightforward expected-utility maximization. Providing that model—especially for imperfect predictions, related computations, and multi-stage choices—is the central unfinished task. A-FDT offers a precise target for such modeling, not yet a complete general method for constructing it.