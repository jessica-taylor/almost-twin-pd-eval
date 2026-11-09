# A-FDT: Choosing the Output of a Decision Procedure

An action can be connected to its consequences in more than one way. Pressing a switch may cause a light to turn on. But a predictor’s earlier decision can also depend on what the agent’s decision procedure outputs, even though the agent’s later bodily movement does not cause that prediction. Conversely, an action can correlate with an illness without either causing the illness or being predicted by it.

**Action functional decision theory (A-FDT)** distinguishes these relationships when constructing decision counterfactuals. Its central question is not merely what would happen if a physical action changed, nor what learning about that action would reveal. It asks what would happen if the particular computation producing the decision had a different output.

This essay takes Equation (4) of Yudkowsky and Soares’s paper as its definition of A-FDT. That qualification matters: the paper also discusses a policy-selecting formulation, which should not silently be substituted for the action-selecting rule examined here.

## 1. The formal rule

Let:

- \(\mathcal A\) be a finite action set;
- \(\mathcal O\) be a countable outcome set;
- \(x\) be the agent’s observation history;
- \(U:\mathcal O\to\mathbb R\) be a utility function with finite relevant expectations;
- \(V=U(O)\) be the resulting utility random variable;
- \(P\) be a probabilistic world-model;
- \(G\) describe the relevant dependencies among variables in that model.

A-FDT requires a variable representing its own output on specified inputs. Write this variable as
\[
D_{P,G,x}.
\]
Its intended referent is the value of the computation
\[
\operatorname{A\text{-}FDT}(P,G,x).
\]

The variable and its referent must be distinguished. \(D_{P,G,x}\) is an object inside the model, available for hypothetical manipulation. The actual computation’s output is the action eventually selected.

Rewriting the paper’s Equation (4) in this notation gives
\[
\boxed{
\operatorname{A\text{-}FDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E_P\!\left[
V\mid \operatorname{do}(D_{P,G,x}=a)
\right].
}
\tag{4}
\]
A fixed tie-breaking convention can make the rule single-valued.

The operator \(\operatorname{do}\) constructs an intervention hypothetical. It does **not** mean ordinary conditioning on the event \(D_{P,G,x}=a\). In particular, an alternative remains evaluable even if the agent is already certain that its procedure will not output it.

For comparison, evidential decision theory (EDT) evaluates
\[
\mathbb E_P[V\mid \mathrm{Obs}=x,\mathrm{Act}=a],
\]
whereas causal decision theory (CDT), in the paper’s graphical presentation, evaluates
\[
\mathbb E_P[V\mid
\operatorname{do}(\mathrm{Act}=a),\mathrm{Obs}=x].
\]

A-FDT differs in two places:

1. It intervenes on a **computational output**, rather than directly on a physical act.
2. Observation \(x\) selects the computational variable being intervened upon. Equation (4) does **not** additionally condition the expectation on \(\mathrm{Obs}=x\).

The second difference is essential. Adding that conditioning would change the assigned theory and eliminate some of its characteristic prescriptions.

## 2. What dependencies should survive an intervention?

The source calls the relevant relationship **subjunctive dependence**. Its clearest example is two systems implementing the same computation. If two accurate calculators evaluate the same expression, their answers are linked even without communication.

Similarly, an agent and a faithful simulation of its decision procedure depend on the same computational output. A predictor need not literally run identical code: a sufficiently accurate model can establish an imperfect version of the relationship.

A-FDT therefore preserves more than physical causal connections, but less than every statistical association.

Consider three patterns:

- **Causal consequence:** the decision output determines an action, which changes the environment.
- **Computational dependence:** another system computes or predicts the relevant output, and responds to it.
- **Common-cause correlation:** a background condition influences the action and another event, without that event depending on the decision computation.

The first two belong in A-FDT’s intervention structure. The third does not, merely by being correlated.

This is not a licence to make every similar agent change together. Two agents following the same named theory may have different inputs, utilities, information, or implementations. Even different outputs of one algorithm on different inputs need not vary together under a single intervention. The model must specify the particular dependence.

### A usable operational interpretation

The paper supplies Equation (4), but no general procedure for constructing its logical dependency graph. For finite examples, a reasonable additional assumption is to provide an explicit structural model:

\[
Y_i=f_i(\operatorname{Parents}_i,Z),
\]

where \(Z\) contains background uncertainty and the dependency graph is acyclic. To evaluate \(a\):

1. Replace the equation for \(D_{P,G,x}\) by \(D_{P,G,x}=a\).
2. Retain the other structural equations.
3. Recompute descendants of that node.
4. Average the resulting utility over the unchanged background distribution.

Equivalently,
\[
Q_x(a)=
\sum_z P_Z(z)\,
U\!\left(O^{\,\operatorname{do}(D_{P,G,x}=a)}(z)\right).
\]

This is an operational completion of the paper’s proposal, not its solution to logical counterfactuals in general. A graph alone may be insufficient: one also needs response equations, including responses to otherwise impossible inputs.

There is a genuine counterlogical element. A fixed mathematical function on fixed inputs has only one output. A-FDT nevertheless evaluates alternatives by locally replacing its represented output while retaining selected dependencies. These hypotheticals are decision-making instruments, not claims that arithmetic or the past can physically be altered.

## 3. Three basic applications of A-FDT

### A-FDT in Newcomb’s problem

An opaque box contains \(M=\$1{,}000{,}000\) if a predictor predicted one-boxing, and nothing otherwise. A transparent box contains \(c=\$1{,}000\). The agent may take only the opaque box or both.

Assume the predictor tracks the relevant decision output with symmetric accuracy \(r\). This is stronger than merely knowing its aggregate historical accuracy: it specifies how predictions respond under each intervention.

Let \(D\) be the current decision-output variable. The relevant structure is
\[
D\longrightarrow \mathrm{Act},
\qquad
D\longrightarrow \mathrm{Prediction}
\longrightarrow \mathrm{OpaqueBox}.
\]
These are subjunctive dependency arrows; they need not all describe physical causation.

A-FDT obtains
\[
Q(\mathrm{onebox})=rM,
\]
\[
Q(\mathrm{twobox})=(1-r)M+c.
\]
Thus it one-boxes exactly when
\[
(2r-1)M>c.
\]

For \(r=0.99\), the values are \(\$990{,}000\) and \(\$11{,}000\).

No backwards signal is involved. The agent believes the money is already placed. Its decision comparison concerns a different hypothetical: what the predictor would have predicted had this computation output differently.

CDT instead holds the opaque box’s contents fixed across its action interventions, making the extra \(\$1{,}000\) attractive in either case. The disagreement is therefore about which features remain fixed, not about addition.

### A-FDT in the smoking-lesion problem

In the imaginary smoking-lesion problem, a lesion produces both a propensity to smoke and cancer. Smoking itself does not cause cancer.

The dependency pattern is schematically
\[
\mathrm{Lesion}\longrightarrow \mathrm{Cancer},
\qquad
\mathrm{Lesion}\longrightarrow \mathrm{SmokingPropensity}.
\]
Changing the relevant decision output does not change the lesion.

Consequently, wherever the intervened output controls the action, smoking can add its stipulated enjoyment without changing cancer risk. In a simplified fixed-preference model,
\[
Q(\mathrm{smoke})-Q(\mathrm{refrain})=\$1{,}000.
\]

The paper’s fuller construction introduces uncertainty about preferences and about which computation controls the act. There the gain is weighted by the probability that the intervened computation controls behavior; the sign remains positive for the smoking-preferring computation.

The source itself regards the traditional dilemma as problematic, particularly as a criticism of sophisticated versions of EDT. Its useful lesson here is narrower: **intervening on a decision output does not reverse every correlation that helped generate that decision.**

### A-FDT against a computational twin

Suppose two prisoners implement the same relevant decision computation on matching inputs. Mutual cooperation gives each \(\$1{,}000{,}000\); mutual defection gives each \(\$1{,}000\). A unilateral defector would receive \(\$1{,}001{,}000\).

Under the stipulated computational dependence,
\[
Q(\mathrm{cooperate})=\$1{,}000{,}000,
\qquad
Q(\mathrm{defect})=\$1{,}000.
\]

A-FDT cooperates for self-interested reasons. It is not assuming that cooperation physically influences the other room. It evaluates both implementations as depending on the same output.

Against an unrelated opponent whose behavior does not depend on that output, this argument disappears. A-FDT is not unconditional cooperation.

## 4. A-FDT’s distinctive treatment of observations

Ordinary Newcomb’s problem does not expose the full significance of Equation (4). Transparent Newcomb’s problem does.

Both boxes are visible. The predictor fills the large box if it predicts that the agent would one-box **upon seeing it full**. The agent now sees two full boxes.

Introduce separate variables
\[
D_f=D_{P,G,\mathrm{full}},
\qquad
D_e=D_{P,G,\mathrm{empty}}.
\]
The predictor responds to \(D_f\). Its prediction determines the box contents and hence which observation occurs. The physical action is then selected by the appropriate branch:
\[
\mathrm{Act}=
\begin{cases}
D_f,&\mathrm{Box}=\mathrm{full},\\
D_e,&\mathrm{Box}=\mathrm{empty}.
\end{cases}
\]

A-FDT, having observed a full box, intervenes on \(D_f\). But the resulting hypothetical is allowed to contain an empty box. In that hypothetical, the actual action is controlled by \(D_e\), not by the variable being intervened upon.

Let \(q\) be the model’s probability that the empty-box computation two-boxes. Assume predictor error is independent of this residual uncertainty, and that intervening on \(D_f\) does not change \(D_e\). Then
\[
Q_f(\mathrm{onebox})
=rM+(1-r)qc,
\]
whereas
\[
Q_f(\mathrm{twobox})
=(1-r)(M+c)+rqc.
\]

For \(r=0.99\), one-boxing wins for every \(q\in[0,1]\). If \(q=1\), the respective values are
\[
\$990{,}010
\quad\text{and}\quad
\$11{,}000.
\]

These are not posterior estimates of the money physically present. The agent knows it sees a full box. They are values of intervention hypotheticals in which changing the predicted response also changes whether that observation occurs.

Parfit’s hitchhiker has the same architecture. A driver rescues someone only if the driver predicts payment after arrival. At the ATM, A-FDT intervenes on the output for the “safely in town” input. Refusal can change the earlier rescue decision in the hypothetical, leaving that computational branch unimplemented. A-FDT therefore pays when the value of obtaining rescue sufficiently exceeds the payment.

### What remains unspecified?

Equation (4) does not fully determine how to obtain the underlying \(P\) and \(G\) across successive observations.

My operational interpretation is to retain, for the modeled decision episode, a distribution covering all relevant observation branches, and let observations select intervention nodes. This reproduces the source’s examples. Evidence can still inform factual beliefs and improve the model; it must not automatically become an extra fixed condition in the decision objective.

The paper does not supply a universal boundary between evidence that should revise the episode model and evidence handled through branch selection. That boundary is an implementation problem, not something Equation (4) resolves by itself.

## 5. A-FDT and prediction-dependent blackmail

Suppose a blackmailer launches a damaging mechanism after predicting whether the agent would pay upon receiving a demand. Payment costs \(c\); refusing an executed threat costs \(L\).

Let
\[
\alpha=
P(\mathrm{launch}\mid\operatorname{do}(D_{\mathrm{demand}}=\mathrm{pay})),
\]
\[
\beta=
P(\mathrm{launch}\mid\operatorname{do}(D_{\mathrm{demand}}=\mathrm{refuse})).
\]

Assuming no loss without launch, and that payment stops the damage,
\[
Q(\mathrm{pay})=-\alpha c,
\qquad
Q(\mathrm{refuse})=-\beta L.
\]
A-FDT refuses when
\[
\beta L<\alpha c.
\]

With \(c=\$1{,}000\), \(L=\$1{,}000{,}000\), \(\alpha=1\), and \(\beta=0.0009\), refusal has expected loss \(\$900\), against payment’s \(\$1{,}000\).

This explains refusal even after a demand is received: the refusal hypothetical includes the reduced probability of receiving it. A fallible predictor makes such actual demands possible without contradicting the agent’s model.

But A-FDT does not imply “never pay blackmail.” If launch is independent of the agent’s predicted response, then \(\alpha=\beta>0\). With \(c<L\), payment wins. The decisive issue is the modeled dependence, not a slogan about resisting threats.

## 6. Applying A-FDT beyond the standard examples

A practical analysis should proceed in this order:

1. **Specify outcomes and utilities.** Include relevant costs, benefits, and consequences outside the presently observed branch.
2. **Identify the exact computation.** Determine which inputs distinguish it from other decision computations.
3. **Specify dependence mechanisms.** Explain why each predictor, copy, or environmental response should change under the intervention.
4. **Construct complete hypotheticals.** Allow observations and branch selection to change when they are downstream of the intervened output.
5. **Compare expected utilities.** Test whether the recommendation survives plausible changes in predictor reliability and model structure.

Prediction quality must be represented carefully. A predictor with excellent population-wide accuracy might perform poorly on this agent or this alternative output. Historical correlation alone does not identify the intervention probabilities A-FDT needs.

### Actions are not entire policies

A policy is a mapping
\[
\pi:\mathcal X\to\mathcal A.
\]
Equation (4) chooses an action by intervening on the output associated with one specified input. It does not directly optimize over all such mappings.

The paper’s policy-based functional decision theory instead selects a policy as the relevant computational output. The authors say that this distinction matters in some multi-agent problems. That is a reason to preserve the distinction, not erase it.

For A-FDT, an intervention on \(D_x\) changes other output variables only where the supplied dependence model says it does. A whole-policy intervention can change several observation-contingent outputs jointly.

One implication, beyond the paper’s worked examples, is that individual output optimization need not establish global policy optimality. Several outputs might jointly support a beneficial arrangement even though changing any one alone is unhelpful. Additional assumptions are therefore needed before transferring broad policy-level claims to A-FDT.

### The central unresolved problem

The source explicitly acknowledges that it lacks a general theory for discovering logical and computational dependencies. Its self-reference discussion explains how a program can represent its own computation without first knowing its output. That does not establish coherent counterfactual semantics for every self-referential model.

My finite structural interpretation makes particular examples calculable once their response equations are supplied. It does not determine which equations are correct, handle every cyclic interaction, or solve computational intractability.

Accordingly, the paper’s broader claims about precommitment, reflective stability, and the value of information should be read as motivations and proposed advantages, not as unrestricted theorems about every application of Equation (4). Likewise, its suggestion that the approach outperforms rivals in all “fair” problems remains dependent on an unfinished definition of fairness.

## References

- Yudkowsky, E., and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2, especially §§3–6 and notes 7, 9, and 16. https://arxiv.org/abs/1710.05060v2.
- Pearl, J. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000. Background for structural interventions; not a completed account of logical intervention.

## Conclusion

A-FDT evaluates actions by intervening on the represented output of the computation making the decision. It preserves causal and computational dependencies while breaking correlations that do not survive that intervention. Crucially, its hypotheticals may change which observations occur.

This yields concrete recommendations in predictor problems, cooperation, rescue, and blackmail. Its remaining difficulty is equally concrete: Equation (4) selects an action only after the relevant dependency structure has been supplied. Applying A-FDT responsibly therefore requires both expected-utility calculation and an explicit, defensible account of what would change together.