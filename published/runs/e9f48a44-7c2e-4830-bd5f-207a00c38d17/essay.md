# A-FDT: Choosing Actions as Outputs of a Decision Function

A decision can matter without physically causing everything with which it is connected. A predictor may have anticipated it yesterday; another agent may be running the same computation elsewhere; a simulated copy may already have produced an equivalent answer. **Action functional decision theory (A-FDT)** proposes that these relationships belong inside deliberation.

Its central question is not simply, “What would happen if my body performed this action?” It is: “What would happen if this decision computation returned this action?” The difference concerns which dependencies survive when alternatives are evaluated.

Here A-FDT denotes specifically the action-selecting rule in Equation (4), Section 5, of Yudkowsky and Soares’s paper. The authors also discuss selecting whole policies, but that is a distinct extension, not something to substitute silently for the action rule.

A-FDT is precise about what to maximize once an appropriate dependency model is supplied. It is substantially less complete about how to obtain that model. Understanding both points is essential: otherwise the theory becomes either an ordinary causal calculation under a new name, or an unrestricted license to imagine favorable correlations.

## 1. The formal rule

Let:

- \(\mathcal A\) be a finite set of available actions;
- \(\mathcal X\) be a countable set of observation histories;
- \(O\) be an outcome variable;
- \(U(O)\) be utility, with finite relevant expectations;
- \(P\) describe uncertainty about the world;
- \(G\) describe its causal and other relevant *subjunctive dependencies*.

Write \(M=(P,G)\). For each observation history \(x\), introduce a model variable
\[
D_x:=\text{the output of A-FDT on inputs }(P,G,x).
\]
This notation abbreviates the paper’s variable whose name explicitly encodes \(P,G,x\). Crucially, \(D_x\) is a representation of a computation’s output, not the physical action variable \(A\).

Equation (4), with notation adapted, says
\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
\in
\arg\max_{a\in\mathcal A}
\mathbb E_{P,G}\!\left[
U(O)\mid\operatorname{do}(D_x=a)
\right].
}
\]
A fixed tie-breaking convention can make this single-valued.

Define
\[
Q_x(a)=
\sum_o
P_{G,\operatorname{do}(D_x=a)}(O=o)\,U(o).
\]
A-FDT selects an action maximizing \(Q_x\). Thus it remains an expected-utility theory; its novelty lies in the intervention that produces the hypothetical outcome distribution.

For comparison, **evidential decision theory (EDT)** evaluates
\[
\mathbb E[U(O)\mid X=x,A=a],
\]
whereas **causal decision theory (CDT)** evaluates, in the paper’s presentation,
\[
\mathbb E[U(O)\mid\operatorname{do}(A=a),X=x].
\]

These are three different operations:

- EDT treats taking an action as evidence.
- CDT intervenes on the physical action.
- A-FDT intervenes on the output of the decision computation.

There is also a second, easily missed distinction: **A-FDT’s displayed expectation does not additionally condition on \(X=x\).** Observation selects the node \(D_x\) on which to intervene. This will matter considerably.

The self-reference is intentional. The model represents the very algorithm using that model. As the authors emphasize, representing a computation does not require already knowing its answer. Nevertheless, representing oneself is not by itself a solution to every problem of logical uncertainty or reflective consistency.

## 2. What the intervention preserves

The paper calls a relationship *subjunctive dependence* when changing a computation’s output in a decision hypothetical calls for corresponding changes elsewhere. Its clearest examples are multiple implementations of the same computation and predictions based on accurate representations of that computation.

Suppose two reliable calculators evaluate the same expression. Their agreement is not merely an accidental correlation. Likewise, if an opponent implements the same decision computation on equivalent inputs, A-FDT does not evaluate cooperation while arbitrarily holding the opponent’s computationally identical response at defection.

This is not a claim that one calculator sends a signal to the other, or that present actions transmit information backward in time. The intervention changes a **model used for comparison**, not physical history.

A useful operational interpretation is to supply structural equations
\[
Z_i=f_i(\operatorname{pa}_i,E_i),
\]
together with a distribution over exogenous variables \(E_i\). To evaluate \(a\):

1. Replace the equation determining \(D_x\) by \(D_x=a\).
2. Preserve the other structural equations and exogenous distribution.
3. Recompute affected variables.
4. Average the resulting utility.

This makes the paper’s graphical proposal executable in finite, acyclic examples. But it is an implementation assumption, not a general solution supplied by the paper. A bare graph does not determine numerical responses, and observational probabilities may not determine responses to counterpossible interventions. Structural equations or equivalent intervention kernels must supply those details.

The intended balance is selective preservation. Causal consequences of the computation should change. Accurate representations of that computation should respond appropriately. An unrelated disease should not disappear merely because the chosen action was statistically associated with good health.

Consequently, predictor accuracy alone is not a complete model. A predictor who simulates the decision computation and one who merely observes a correlated medical condition need not respond identically under \(\operatorname{do}(D_x=a)\). That response requires an explicit assumption about the dependency.

## 3. A-FDT in Newcomb’s problem

An opaque box contains either \(B=\$1{,}000{,}000\) or nothing. A transparent box contains \(b=\$1{,}000\). A predictor filled the opaque box exactly when she predicted that the agent would take only it.

Assume, more specifically than an aggregate historical accuracy claim, that the predictor tracks the decision output with symmetric accuracy \(p\). Let \(D\) represent the current A-FDT computation. The proposed dependency structure is
\[
D\longrightarrow A,
\qquad
D\longrightarrow\text{Prediction}\longrightarrow\text{Box contents}.
\]
These arrows express subjunctive structure, not exclusively temporal causation.

The two values are
\[
Q(\text{one-box})=pB,
\]
\[
Q(\text{two-box})=(1-p)B+b.
\]
Therefore A-FDT one-boxes exactly when
\[
(2p-1)B>b.
\]
With \(p=0.99\), these values are \(\$990{,}000\) and \(\$11{,}000\), respectively.

The familiar CDT argument instead holds the opaque box’s contents fixed while changing the physical action. Taking the transparent box then adds \(b\) in every case. A-FDT rejects that comparison as the relevant decision hypothetical: its intervention changes the computation whose output the predictor was tracking.

This does not mean that money literally moves after the choice. The agent compares two computational suppositions, each including an appropriately corresponding prediction.

Nor is one-boxing unconditional. If prediction is sufficiently unreliable, the inequality reverses. A-FDT is a quantitative decision rule, not a slogan instructing agents always to cooperate with predictors.

## 4. A-FDT and merely evidential correlations

Consider the fictional smoking-lesion problem. A lesion causes both a desire to smoke and cancer; smoking itself does not cause cancer. Suppose smoking has positive utility \(b\).

In a simplified fixed-preference model, write
\[
U=b\,\mathbf 1_{\{A=\text{smoke}\}}
+V\,\mathbf 1_{\{\text{survival}\}}.
\]
If the lesion and cancer do not depend subjunctively on the decision output, then
\[
P(\text{cancer}\mid\operatorname{do}(D=\text{smoke}))
=
P(\text{cancer}\mid\operatorname{do}(D=\text{refrain})).
\]
Hence
\[
Q(\text{smoke})-Q(\text{refrain})=b>0.
\]

The contrast with Newcomb’s problem is structural. A predictor represents the decision computation; a lesion does not inspect its conclusion before deciding whether to cause cancer.

The paper’s fuller treatment is subtler than this simplified model. It lets the lesion select between preference-dependent decision calls. Intervening on one call changes actual behavior only when that call controls the agent. The gain from smoking is then weighted by the probability of that branch. The lesion’s probability still remains unchanged.

The authors also acknowledge that the traditional lesion problem has difficulties concerning introspection, preferences, and population statistics. Its strongest lesson is therefore methodological: **conditioning on an action can change beliefs about its causes, while intervening on the decision output need not change those causes.** The example concerns an imaginary causal structure, not actual smoking risks.

## 5. Observation selects a computation

A-FDT becomes most distinctive when observations themselves depend on predictions of the response to those observations.

Consider transparent Newcomb’s problem. Both boxes are visible. The predictor fills the large box if she predicts that the agent will one-box *upon seeing it full*.

Introduce two logical variables:
\[
D_F=\operatorname{A\!-\!FDT}(P,G,\text{full}),
\qquad
D_E=\operatorname{A\!-\!FDT}(P,G,\text{empty}).
\]
Actual behavior is selected by the observation:
\[
A=
\begin{cases}
D_F,&\text{if the large box is full},\\
D_E,&\text{if it is empty}.
\end{cases}
\]

The predictor tracks \(D_F\). Seeing a full box therefore leads A-FDT to intervene on \(D_F\), **without additionally conditioning its hypothetical distribution on fullness**.

Let the predictor’s symmetric accuracy be \(p\), and let \(q\) be the model’s probability that \(D_E\) takes both boxes. Then
\[
Q_F(\text{one-box})
=pB+(1-p)qb,
\]
while
\[
Q_F(\text{two-box})
=(1-p)(B+b)+pqb.
\]

With \(p=0.99\), one-boxing is preferable for every \(q\in[0,1]\).

Notice what the second hypothetical includes. If \(D_F\) returned two-boxing, the predictor would probably leave the box empty. The physical agent would then run the empty-observation computation \(D_E\), not \(D_F\). Thus intervening on a computation’s output need not make that output the physical action in every hypothetical branch.

This is not ordinary posterior expected-utility maximization after seeing a full box. A-FDT permits its decision hypothetical to contain different observations from those actually received.

Parfit’s hitchhiker has the same architecture. A driver rescues an agent only when predicting that the agent’s city-arrival computation will recommend paying. At the ATM, A-FDT evaluates that computation’s output together with its influence on rescue. Under the stipulated reliable dependence and sufficiently valuable rescue, it pays.

This feature also creates a modeling responsibility. The relevant \(P\) must retain the observation-generating process. Simply replacing it with a posterior already conditioned on the current observation can change the rule. The paper establishes this distinction but does not give a universal procedure for deciding which earlier information should already be incorporated into the supplied model.

## 6. A-FDT with copies—and the boundary with policies

In the psychological-twin prisoner’s dilemma, assume both agents implement the same relevant computation on equivalent inputs, allowing for player renaming. Let cooperation yield each agent \(\$1{,}000{,}000\), and mutual defection yield each \(\$1{,}000\).

A shared logical node \(D\) controls both actions:
\[
A_1=D,\qquad A_2=D.
\]
For an agent concerned only with her own payoff,
\[
Q(\text{cooperate})=1{,}000{,}000,
\qquad
Q(\text{defect})=1{,}000.
\]
A-FDT cooperates without appealing to altruism.

But the shared node does substantive work. Merely knowing that both players use A-FDT does not establish identical inputs or equivalent computations. Different observations, utilities, or models can produce different logical nodes. Similarity is evidence to investigate, not permission to identify decisions automatically.

This also clarifies the distinction between actions and policies. A policy is a mapping
\[
\pi:\mathcal X\to\mathcal A.
\]
The collection \((D_x)_{x\in\mathcal X}\) determines policy-like behavior, but Equation (4) evaluates changing one selected output \(D_x\). It does not automatically intervene on an entire mapping.

The paper’s footnotes explicitly prefer policy selection in a broader formulation and acknowledge possible differences in multi-agent cases. A-FDT should therefore not be described simply as “choose the globally best policy.” Such a prescription needs an additional intervention target and additional dependency assumptions.

For unfamiliar cases involving several observation-contingent decisions, one should specify whether alternatives change one output or several. Even where other outputs respond indirectly through supplied dependencies, joint policy optimization and single-output optimization are not generally interchangeable.

## 7. A-FDT and prediction-sensitive blackmail

Mechanical blackmail illustrates both A-FDT’s attraction and its sensitivity to modeling assumptions.

Suppose a blackmailer launches a damaging process only when predicting payment. Payment costs \(c\); refusing after launch incurs damage \(L\). Let \(D_L\) represent the agent’s response upon receiving a demand.

For a transparent numerical model, assume:

- if \(D_L=\text{pay}\), a demand is always launched;
- if \(D_L=\text{refuse}\), a prediction error nevertheless produces a demand with probability \(\varepsilon\);
- absent a demand, there is no loss.

Then
\[
Q_L(\text{pay})=-c,
\qquad
Q_L(\text{refuse})=-\varepsilon L.
\]
A-FDT refuses precisely when
\[
\varepsilon L<c.
\]

For \(c=\$1{,}000\), \(L=\$1{,}000{,}000\), and \(\varepsilon=0.0009\), refusal has expected loss \(\$900\), so A-FDT refuses—even while holding the demand.

Its rationale is not that refusal physically stops an already-running process. Rather, predictable refusal usually prevents the process from being launched. Equation (4) preserves that dependency in the hypothetical.

The uncomfortable implication deserves emphasis: in the exceptional branch where prediction failed, refusal really does incur the larger loss. A-FDT evaluates the response computation across the supplied model, rather than optimizing conditional solely on already having received the demand.

If demands instead arise independently of the response computation, these values do not apply. Likewise, different prediction-error rates can favor payment. The example supports resistance to a specified prediction-sensitive threat, not unconditional refusal of every threat.

## 8. Applying A-FDT responsibly

A practical analysis can proceed through five questions:

1. **What are the outcomes and utilities?** Include costs, uncertainty, and relevant observation branches.
2. **Which computation is under evaluation?** Specify its model and observation inputs.
3. **What depends on that computation’s output?** Distinguish physical consequences, simulations, imperfect predictions, and mere correlations.
4. **What survives intervention?** Preserve structural relationships and explicitly model errors; do not add observational conditioning absent from Equation (4).
5. **Which output has greatest expected utility?** Calculate, then test sensitivity to uncertain dependencies.

The fourth step often determines the answer. A-FDT does not license changing every inconvenient background fact. It requires changes justified by the supplied subjunctive structure.

Several limitations remain.

First, interventions on fixed mathematical outputs are *counterpossible*: a deterministic function cannot actually return a different value on the same input. The graph supplies a disciplined hypothetical calculation, but the paper does not derive a general semantics for such calculations.

Second, dependencies may be uncertain. One reasonable extension is to average values over candidate structural models,
\[
Q_x(a)=\sum_k w_k Q_x^{(k)}(a),
\]
using credences \(w_k\). This is a proposal for handling uncertainty, not an identification procedure provided by the source.

Third, the paper’s success claims exceed its formal results. Its examples motivate A-FDT, but do not prove universal superiority, guaranteed reflective stability, or nonnegative information value under every possible implementation. The authors themselves leave a general definition of “fair” decision problems open.

Finally, expected-utility representation theorems do not settle the dispute. They explain maximization given a perspective for evaluating alternatives; they do not establish that A-FDT’s counterfactual perspective is uniquely correct.

## References

- Yudkowsky, E., and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2, especially §§3, 5–6, 9 and footnotes 7, 16.
- Pearl, J. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.
- Joyce, J. M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

## Conclusion

A-FDT evaluates actions by intervening on the logical output of the current decision computation, preserving its modeled subjunctive dependencies. This explains its characteristic treatment of predictors, copies, observation selection, and merely evidential correlations. Given a suitable model, its calculation is straightforward. The unresolved challenge is supplying that model: determining which computational dependencies are real, how counterpossible interventions should propagate, and how confidently those assumptions should guide action.