# A-FDT: Choosing the Output of a Decision Computation

Decision theories differ not only over which outcomes are desirable, but over how to evaluate actions that an agent does not actually take. Suppose a reliable predictor has already rewarded or punished you according to its prediction of your decision. Should deliberation hold that prediction fixed, or allow it to vary with the decision being considered?

**Action functional decision theory (A-FDT)** takes the second approach when the predictor is tracking the computation that produces the decision. It evaluates alternative outputs of that computation, preserving dependencies between the computation and its implementations, predictions, and consequences.

This essay takes Equation (4) of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality* as its primary definition. Two qualifications matter. First, this is the paper’s **action-based presentation**, not its separately mentioned, preferred policy-based formulation. Second, the equation supplies a decision rule **given an appropriate model of dependencies**. The paper does not provide a general algorithm for constructing that model.

## 1. The formal rule

Let:

- \(\mathcal A\) be a finite action set;
- \(\mathcal X\) be a set of possible observation histories;
- \(O\) be an outcome variable;
- \(V=U(O)\) be utility, with expectations assumed finite;
- \(P\) describe the agent’s uncertainty;
- \(G\) describe relevant causal, computational, and logical dependencies.

For fixed inputs \(P,G,x\), write
\[
D_x:=\mathsf{Out}_{\mathrm{A\text{-}FDT}}(P,G,x).
\]
Here \(D_x\) is a **variable inside the model**, representing what A-FDT outputs on those inputs. It is not the output itself. Its full identity includes \(P\), \(G\), and \(x\).

In this notation, the source’s Equation (4) becomes
\[
\boxed{
\operatorname{A\text{-}FDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E_P\!\left[V\mid\operatorname{do}(D_x=a)\right].
}
\tag{4}
\]
A deterministic implementation also needs a tie-breaking convention; I assume a fixed one.

The intervention is a manipulation of a **representation used for deliberation**, not a physical operation on mathematics. To evaluate \(a\), the agent constructs a hypothetical in which its decision computation outputs \(a\), propagates the changes specified by \(G\), and calculates expected utility.

For comparison, the source presents evidential decision theory (EDT) as maximizing
\[
\mathbb E[V\mid X=x,A=a],
\]
and causal decision theory (CDT) as maximizing
\[
\mathbb E[V\mid \operatorname{do}(A=a),X=x].
\]

A-FDT differs in two important respects:

1. It intervenes on the **output of a computation**, rather than directly on physical action \(A\).
2. Observation \(x\) selects the intervention target \(D_x\); Equation (4) contains **no additional conditioning on \(X=x\)**.

The second feature is essential. Adding such conditioning changes the rule and can reverse its recommendations.

Self-reference enters because the computation being modeled is the very computation performing the evaluation. The source invokes computational self-reference techniques to explain how a program can represent itself without already knowing its output. This addresses representation, however, not the harder question of how to construct appropriate counterfactual dependencies.

## 2. Subjunctive dependence and model surgery

The paper calls the relevant relationship **subjunctive dependence**. Two systems can depend on the same computation even when neither physically causes the other’s output.

For example, two accurate calculators evaluating the same expression must agree. Similarly, an agent and an accurate simulation of that agent may produce matching decisions without communicating. A-FDT aims to preserve such relationships when evaluating alternatives.

This is stronger than causal dependence but narrower than statistical correlation. A disease might cause both a preference and an adverse medical outcome. Altering the output of a decision computation need not alter that disease. A predictor, by contrast, might explicitly calculate that output and act accordingly.

A useful operational interpretation—an implementation proposal rather than a general construction supplied by the paper—is to use a finite acyclic structural model. Let \(W\) contain background uncertainty, and give modeled variables response equations. For each candidate \(a\):

1. Replace the equation determining \(D_x\) by \(D_x=a\).
2. Retain other response equations.
3. Recompute descendants of \(D_x\).
4. Average the resulting utility over the unchanged distribution of \(W\).

If the resulting outcome is \(O_a(W)\), then
\[
Q_x(a)=\sum_w P(W=w)\,U(O_a(w)),
\qquad
a^*\in\arg\max_a Q_x(a).
\]

On this interpretation, \(G\) must come with enough information to determine responses, including responses under interventions that never occur ordinarily. A bare diagram of correlations is insufficient.

This construction makes the arithmetic concrete once the model is supplied. It does **not** solve the central modeling problem: which computational relationships should survive an intervention on a logically fixed output?

Indeed, a deterministic function has only one actual output on fixed inputs. Other outputs are counterpossible. A-FDT therefore needs selective hypothetical reasoning, not unrestricted classical deduction from an inconsistent premise. The source explicitly acknowledges the lack of a satisfactory general account.

## 3. A-FDT in Newcomb’s problem

An opaque box contains either \(M=\$1{,}000{,}000\) or nothing. A transparent box contains \(c=\$1{,}000\). A predictor filled the opaque box exactly when it predicted that the agent would take only that box.

Let \(D\) be the relevant A-FDT output and \(H\) the prediction. Consider the dependency structure
\[
D\longrightarrow A,
\qquad
D\longrightarrow H\longrightarrow B,
\qquad
(A,B)\longrightarrow V.
\]
The arrow \(D\to H\) represents computational dependence, not a signal traveling backward through time.

Assume an independent prediction-error channel with accuracy \(r\):
\[
P(H=\text{one-box}\mid\operatorname{do}(D=\text{one-box}))=r,
\]
\[
P(H=\text{one-box}\mid\operatorname{do}(D=\text{two-box}))=1-r.
\]
Then
\[
Q(\text{one-box})=rM,
\]
\[
Q(\text{two-box})=(1-r)M+c.
\]
A-FDT one-boxes exactly when
\[
(2r-1)M>c.
\]
At \(r=0.99\), the values are \(\$990{,}000\) and \(\$11{,}000\).

This is not an attempt to change the past physically. It is a comparison between two hypothetical outputs of a computation that the predictor was already trying to predict.

An important modeling qualification follows: a predictor’s historical accuracy alone does not identify these intervention probabilities. The independent symmetric-error model is an additional assumption. Other mechanisms—biased errors, selective prediction, or reliance on population statistics—require their own response models.

### Why the smoking lesion is different

In the source’s imaginary smoking example, a lesion causes both an inclination to smoke and cancer, while smoking itself does not cause cancer. A simplified dependency structure is
\[
L\longrightarrow C,
\qquad
L\longrightarrow\text{preferences},
\qquad
D_x\longrightarrow A.
\]

If smoking provides utility \(s>0\), independently of health, and changing \(D_x\) does not change cancer risk, then
\[
Q(\text{smoke})-Q(\text{refrain})=s.
\]
A-FDT smokes in this fictional setting.

The lesson is structural, not medical: an action’s being evidence of a condition does not establish that the condition should vary under intervention on the decision computation.

The source itself qualifies the example. Its detailed formalization uses uncertainty about the agent’s own preferences, and the authors acknowledge difficulties in maintaining the stipulated correlations. The example illustrates a distinction; it is not an uncontested demonstration against every formulation of EDT.

## 4. A-FDT and computational twins

Suppose two agents implement the same decision computation on equivalent inputs. Their prisoner’s-dilemma payoffs are:

\[
\begin{array}{c|cc}
 & \text{other cooperates} & \text{other defects}\\ \hline
\text{cooperate} & 1{,}000{,}000 & 0\\
\text{defect} & 1{,}001{,}000 & 1{,}000
\end{array}
\]

If both physical actions depend on the same output variable \(D\), then
\[
Q(\text{cooperate})=1{,}000{,}000,
\qquad
Q(\text{defect})=1{,}000.
\]
A-FDT cooperates for self-interested reasons: the alternatives being compared are mutual cooperation and mutual defection.

But “the other agent also uses A-FDT” is not sufficient. Different observations, utilities, or models generally correspond to different computation-output variables. Their relationship must be established, not assumed.

For imperfect similarity, let
\[
p_C=P(A_{\mathrm{other}}=C\mid\operatorname{do}(D_x=C)),
\]
\[
p_D=P(A_{\mathrm{other}}=C\mid\operatorname{do}(D_x=D)).
\]
The relevant comparison is
\[
Q(C)=p_C\,u(C,C)+(1-p_C)u(C,D),
\]
\[
Q(D)=p_D\,u(D,C)+(1-p_D)u(D,D).
\]
Exact twins are one limiting case. General cooperation depends on justified response probabilities, not resemblance alone.

## 5. Observation selects the question being answered

The most distinctive implications of Equation (4) concern observations that themselves depend on predictions of the agent’s response.

Consider transparent Newcomb’s problem. Both boxes are visible. The predictor fills the large box when it predicts that the agent would one-box **upon seeing it full**.

Introduce two variables:
\[
D_f=\text{A-FDT output on observing a full box},
\]
\[
D_e=\text{A-FDT output on observing an empty box}.
\]
The physical action is selected by the observation:
\[
A=
\begin{cases}
D_f,&B=\text{full},\\
D_e,&B=\text{empty}.
\end{cases}
\]
The predictor tracks \(D_f\), not whichever response happens to be physically executed.

After seeing a full box, A-FDT intervenes on \(D_f\). It does not additionally condition the resulting hypothetical on the box remaining full.

Assume the same independent symmetric prediction-error model, with accuracy \(r\), and let
\[
q=P(D_e=\text{two-box}),
\]
unchanged by intervention on \(D_f\). Then
\[
Q_f(\text{one-box})=rM+(1-r)qc.
\]
With probability \(r\), the large box is full and the agent executes \(D_f=\text{one-box}\). Otherwise it is empty, and \(D_e\) controls physical action.

Similarly,
\[
Q_f(\text{two-box})
=(1-r)(M+c)+rqc.
\]
At the usual values,
\[
Q_f(\text{one-box})=990{,}000+10q,
\]
\[
Q_f(\text{two-box})=10{,}010+990q.
\]
One-boxing wins for every \(q\in[0,1]\).

This calculation exposes an easily missed feature: setting \(D_f=a\) does not guarantee that physical action equals \(a\) throughout the hypothetical. The intervention can change the observation, causing another computation to control behavior.

A-FDT is not claiming that the agent is uncertain about what it presently sees. It distinguishes factual belief from the hypothetical used to evaluate an alternative computational output. Nevertheless, allowing a known observation to vary is a substantive and controversial normative commitment, not a consequence of ordinary Bayesian conditioning.

### A-FDT in Parfit’s hitchhiker

A driver rescues an agent only if she predicts that the agent will pay \(c\) after reaching town. Let rescue be worth \(L\), and let \(D_{\mathrm{city}}\) represent the payment decision upon arrival.

With perfect prediction,
\[
Q_{\mathrm{city}}(\text{pay})=L-c,
\qquad
Q_{\mathrm{city}}(\text{refuse})=0.
\]
A-FDT pays when \(L>c\), even after arrival.

Refusing corresponds to a hypothetical in which rescue would not have occurred. This resembles the result of advance commitment, but Equation (4) obtains it through intervention on the arrival-response computation, not through a binding contract.

## 6. A-FDT and blackmail: deterrence has a threshold

The same structure can support refusing extortion. Suppose a blackmailer launches a damaging program when it predicts payment. Paying costs \(c\); refusing after launch incurs loss \(L\).

Let
\[
b_P=P(\text{launch}\mid\operatorname{do}(D_{\mathrm{letter}}=\text{pay})),
\]
\[
b_R=P(\text{launch}\mid\operatorname{do}(D_{\mathrm{letter}}=\text{refuse})).
\]
Assume no loss without launch and no other consequences. Then
\[
Q(\text{pay})=-b_Pc,
\qquad
Q(\text{refuse})=-b_RL.
\]
Thus A-FDT refuses precisely when
\[
b_RL<b_Pc.
\]

Perfect prediction gives \(b_P=1,b_R=0\), making refusal preferable. With prediction errors, refusal need not remain optimal. For \(c=1{,}000\), \(L=1{,}000{,}000\), and \(b_P=1\), refusal wins only when
\[
b_R<0.001.
\]

This is not a categorical injunction against paying blackmail. If the threat is launched independently of the agent’s decision computation, then \(b_P=b_R\); with \(L>c\), payment wins in this simplified model. Real cases also require assessing credibility, repeated demands, enforcement, and other consequences.

The operative principle is dependence-sensitive evaluation, not toughness for its own sake.

## 7. Applying A-FDT beyond familiar examples

A practical analysis should separate the decision rule from the assumptions that make its inputs usable.

**First, identify the computation precisely.** Include relevant observations, preferences, and world-model inputs. Do not connect every instance of “rational reasoning” to one common output node.

**Second, identify mechanisms of dependence.** Copies, simulations, explicit predictions, and ordinary causal consequences provide candidate relationships. Correlation alone does not determine their direction or counterfactual persistence.

**Third, specify responses under alternatives.** Predictor accuracy, asymmetric errors, implementation failures, and observation-selection mechanisms belong in the model. Check that the model has determinate intervention outcomes.

**Fourth, apply Equation (4) without silently changing its treatment of observation.** Select \(D_x\), propagate the intervention, and evaluate utility across the resulting histories—including histories in which \(x\) is not observed.

**Finally, test sensitivity.** If plausible dependency models recommend different actions, A-FDT has not resolved the case without further information or modeling assumptions.

Several limitations remain especially important.

### Actions are not arbitrary policies

For fixed \(P,G\), the family of outputs defines an implicit policy
\[
\pi(x)=\operatorname{A\text{-}FDT}(P,G,x).
\]
But Equation (4) evaluates changes to one output \(D_x\), with other changes occurring only through specified dependencies. It does not automatically optimize over all mappings \(\pi:\mathcal X\to\mathcal A\).

The source’s footnotes discuss a preferred formulation that instead selects policies and acknowledge possible multi-agent differences. Consequently, globally optimal policy selection should not be attributed to A-FDT’s action rule without additional argument.

### Where does the background model begin?

Equation (4) specifies how \(x\) selects an intervention target, but does not fully determine how a bounded agent organizes all its background knowledge.

A reasonable operational proposal is to fix a model encompassing the relevant decision episode, including observation-selection processes influenced by predictions. Evidence genuinely external to that episode can inform its construction. However, selecting this boundary is additional modeling work. Replacing \(P\) by the current posterior \(P(\cdot\mid X=x)\) can erase exactly the alternatives that transparent Newcomb’s problem requires.

### Success is not a general optimality theorem

The source motivates A-FDT through utility obtained, agreement with useful precommitments, and resistance to exploitation. It also acknowledges that no decision theory wins in every conceivable environment. A rewarder can simply punish a particular procedure.

Its proposed restriction to “fair” problems—roughly, problems rewarding behavior rather than procedure identity—is not fully formalized. Nor does an expected-utility representation theorem determine which dependency model is correct.

The examples therefore support A-FDT’s central distinction, but do not establish universal optimality, unrestricted reflective stability, or every claimed information-value property for arbitrary implementations.

## References

- Yudkowsky, E., and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2. Especially §§3–6, §9, and notes 7 and 16.
- Pearl, J. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.
- Joyce, J. M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

## Conclusion

A-FDT evaluates actions by intervening on the output of the decision computation and preserving modeled subjunctive dependencies. This explains its treatment of predictors, twins, commitments, and observation-dependent opportunities. Its central practical challenge is constructing those dependencies without confusing them with mere correlation. Given such a model, Equation (4) yields a definite calculation; without it, A-FDT remains a framework for the unresolved counterfactual question, not a substitute for answering it.