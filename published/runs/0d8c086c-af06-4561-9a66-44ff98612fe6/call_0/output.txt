# A-FDT: Choosing the Output of a Decision Function

Decision theory is not only about assigning utilities and probabilities. It is also about deciding which hypothetical situations to compare. If I consider acting differently, what else should I imagine changing?

**Action functional decision theory (A-FDT)** answers: vary the output of the mathematical decision procedure being implemented, and propagate that variation through the relevant dependencies—including dependencies involving copies and predictors of that procedure.

This essay takes Equation (4), Section 5, of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality* as its primary definition. The paper calls that rule “FDT”; here I consistently call its action-selecting formulation **A-FDT**, distinguishing it from the policy-selecting formulation mentioned in the paper’s footnotes.

A-FDT supplies a precise optimization criterion **conditional on having an appropriate dependency model**. Its central unresolved problem is how to construct that model. Understanding both parts is essential: otherwise the theory can look either like ordinary causal decision theory or like an unrestricted instruction to imagine favorable correlations.

## 1. The formal rule

Let:

- \(\mathcal A\) be a finite set of actions;
- \(\mathcal X\) be a set of observation histories;
- \(O\) be an outcome variable;
- \(u(O)\) be real-valued utility, with finite expectations;
- \(P\) represent the agent’s probabilistic world-model;
- \(G\) describe relevant causal, computational, and logical dependencies.

Write \(V=u(O)\).

The distinctive variable is
\[
D_{P,G,x},
\]
which represents the output of the A-FDT algorithm on the particular inputs \((P,G,x)\). Its subscripts identify a mathematical computation; they are not conditioning events.

Equation (4), with notation simplified and the assigned name substituted, becomes
\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E_{P,G}
\!\left[V\mid\operatorname{do}(D_{P,G,x}=a)\right].
}
\tag{AF}
\]
A fixed tie-breaking convention can make this single-valued.

The intervention does not directly set the physical action. It sets the modeled output of the decision computation. Physical actions, predictions, and other consequences are then recomputed according to \(G\).

For comparison, **evidential decision theory (EDT)** evaluates
\[
Q_{\mathrm{EDT}}(a;x)
=
\mathbb E[V\mid X=x,A=a],
\]
while the paper’s formulation of **causal decision theory (CDT)** evaluates
\[
Q_{\mathrm{CDT}}(a;x)
=
\mathbb E[V\mid\operatorname{do}(A=a),X=x].
\]

The differences concern hypothetical evaluation, not utility itself. EDT asks what an action would indicate; CDT asks what a physical intervention would cause; A-FDT asks what follows from a different output of the decision computation.

Notice an especially important feature of (AF): **there is no additional conditioning on \(X=x\)**. Observation \(x\) instead determines which computation-node is intervened upon. This feature is responsible for A-FDT’s behavior in transparent-box and blackmail problems.

The rule is self-referential: the computation chooses an action by evaluating interventions on a variable representing its own output. The paper invokes computational self-reference results to explain how such representations can be constructed. Representing a computation does not require already knowing its result. Nevertheless, representability alone establishes neither tractability nor a complete semantics for these interventions.

## 2. Subjunctive dependence and mathematical intervention

Suppose two isolated computers execute the same deterministic program on the same input. Their outputs agree even without communication. A physical intervention corrupting one computer’s display need not affect the other. But the hypothesis that their shared mathematical computation has a different output concerns both implementations.

The paper calls this broader relationship **subjunctive dependence**. It includes ordinary causal dependence but is not exhausted by it.

Three relationships must therefore be distinguished:

1. **Causal dependence:** an actuator moves because a controller sends a command.
2. **Computational dependence:** two faithful implementations agree because they compute the same function.
3. **Merely evidential association:** smoking indicates a lesion that independently causes cancer.

A-FDT preserves the first two in its hypotheticals, but need not preserve the third.

This requires counterpossible reasoning. A fixed deterministic function has only one output on fixed inputs. Imagining another output may contradict a mathematical fact. The paper treats the resulting hypothetical as an instrument for decision-making, not as a claim that arithmetic can physically change.

A useful operational interpretation is available for finite examples. **The following is a modeling proposal that makes the paper’s graphical prescription explicit, not a general solution supplied by the paper.**

Represent the situation by an acyclic structural model:
\[
Z_i=f_i(\operatorname{pa}_i,W_i),
\]
with exogenous uncertainty \(W\sim\mu\). Include \(D_{P,G,x}\) among its nodes. To evaluate action \(a\):

1. Replace the structural rule for \(D_{P,G,x}\) by the constant \(a\).
2. Retain the remaining mechanisms.
3. Recompute dependent variables.
4. Average resulting utility over the unchanged exogenous distribution.

Thus,
\[
Q_x(a)=\sum_w\mu(w)\,u\!\left(O^{(a)}(w)\right).
\]

A graph alone is insufficient for numerical evaluation: one also needs mechanisms or suitable conditional distributions. More importantly, the choice of those mechanisms determines which dependencies survive the intervention.

This construction deliberately suspends the logical constraint fixing the intervened computation’s actual output. It does **not** permit arbitrary changes elsewhere. The intended discipline is to preserve all other relevant dependencies as specified by the model.

Nor should every superficially similar agent be linked to the same node. Identical source code with different inputs generally represents different computations. Shared allegiance to A-FDT does not itself imply identical actions.

## 3. A-FDT in three elementary problems

### A-FDT and Newcomb’s problem

A predictor fills an opaque box with \(M=\$1{,}000{,}000\) if it predicts one-boxing, and leaves it empty otherwise. A transparent box always contains \(s=\$1{,}000\).

Let
\[
D\longrightarrow A,
\qquad
D\longrightarrow\widehat A\longrightarrow B,
\]
where \(D\) is the decision-output node, \(\widehat A\) the prediction, and \(B\) the opaque-box contents. These arrows include computational rather than exclusively physical dependence.

Assume a symmetric prediction-error mechanism: under either intervention on \(D\), the prediction matches its output with probability \(\alpha\). Then
\[
Q(\text{one-box})=\alpha M,
\]
\[
Q(\text{two-box})=(1-\alpha)M+s.
\]
A-FDT one-boxes exactly when
\[
(2\alpha-1)M>s.
\]
At \(\alpha=0.99\), the scores are \(\$990{,}000\) and \(\$11{,}000\).

This does not posit backward causation. The intervention changes a representation of the mathematical answer used both by the agent and by the earlier predictor.

The symmetric-error assumption matters. A predictor’s historical 99% accuracy, by itself, does not determine its response under every contemplated intervention. Application requires a model of prediction errors, not merely an aggregate success rate.

### A-FDT and the smoking lesion

In the stipulated fictional problem, a lesion causes both smoking propensity and cancer, but smoking itself does not cause cancer.

For a simplified smoking-preferring agent, let
\[
V=M\,\mathbf 1_{\{\text{no cancer}\}}
+s\,\mathbf 1_{\{\text{smoke}\}}.
\]
Changing the decision-output node changes smoking but not the lesion or cancer. Consequently,
\[
Q(\text{smoke})-Q(\text{refrain})=s>0.
\]

The recommendation is therefore to smoke **under these fictional assumptions**. In reality, smoking causes serious disease.

The paper’s detailed model additionally handles uncertainty about the agent’s preferences. It also acknowledges that maintaining the stipulated smoking–lesion correlation among deliberating agents is problematic. The robust lesson is structural: evidence of a common cause does not automatically become a dependency preserved under decision-output intervention.

### A-FDT and a psychological twin

Suppose two causally isolated agents implement the same decision computation. Mutual cooperation yields each \(R\); mutual defection yields each \(P<R\). Defection earns slightly more against either action held fixed.

CDT defects because the other player’s action is causally independent. A-FDT instead evaluates
\[
Q(\text{cooperate})=R,
\qquad
Q(\text{defect})=P,
\]
because both outputs depend on the same computation.

This is not altruism or a universal injunction to cooperate. Against an independent opponent whose choice does not subjunctively depend on this computation, the extra dependency is absent. The recommendation then depends on the ordinary payoff structure.

## 4. Observation selects a computation, not a fixed world

The most consequential part of Equation (AF) is its treatment of observations.

For fixed \(P,G\), introduce a family of nodes
\[
D_x=D_{P,G,x}.
\]
Together they describe how the algorithm responds to different observations. A physical action can be selected by
\[
A=D_X.
\]
The observed input determines which mathematical answer controls the body.

When the agent observes \(x\), A-FDT intervenes on \(D_x\). But if that answer influences whether \(x\) occurs—for example, because somebody predicted it—the hypothetical may contain a different observation.

### A-FDT and transparent Newcomb

Suppose both boxes are transparent. The predictor fills the large box if it predicts that the agent would one-box **upon seeing it full**.

Let
\[
D_F=\text{output upon seeing a full box},
\qquad
D_E=\text{output upon seeing an empty box}.
\]
The predictor targets \(D_F\), while the body implements
\[
A=
\begin{cases}
D_F,&B=\text{full},\\
D_E,&B=\text{empty}.
\end{cases}
\]

After seeing a full box, A-FDT evaluates interventions on \(D_F\), without fixing \(B=\text{full}\) throughout the hypothetical.

Assume prediction accuracy \(0.99\), and let \(q\) be the modeled probability that \(D_E\) outputs two-boxing. Then
\[
Q_F(\text{one-box})
=
0.99M+0.01qs,
\]
whereas
\[
Q_F(\text{two-box})
=
0.01(M+s)+0.99qs.
\]
The first score is much larger for every \(q\in[0,1]\). A-FDT leaves the small box behind.

In the second hypothetical, the predictor usually predicts two-boxing and leaves the large box empty. The body therefore usually implements \(D_E\), not \(D_F\). Intervening on the answer associated with seeing a full box does not guarantee that this answer is physically implemented in the resulting scenario.

**Parfit’s hitchhiker has the same structure.** A driver rescues an agent only if it predicts payment after arrival. The answer to the in-city payment question influences whether the city observation occurs. A-FDT pays because that answer supports rescue, not because paying now physically alters the past.

### Why this need not ignore ordinary evidence

Suppose instead that changing \(D_x\) cannot affect whether \(X=x\), and has no consequences outside that observation branch. Then
\[
Q_x(a)-Q_x(b)
=
P(X=x)
\left(
\mathbb E[V^{(a)}\mid X=x]
-
\mathbb E[V^{(b)}\mid X=x]
\right).
\]
For \(P(X=x)>0\), the positive multiplier does not affect the ranking. Ordinary conditional choice is recovered.

The striking cases violate these assumptions: the decision-output intervention changes the probability of reaching the observed branch.

Nevertheless, choosing the reference model remains important. If one first conditions \(P\) so thoroughly on the present observation that all alternative observation branches disappear, changing the intervention node cannot generally restore them. The paper’s examples retain an encompassing model of the setup. They do not supply a universal procedure for deciding which evidence should be incorporated into that model and which should enter through the observation index.

## 5. A-FDT and prediction-sensitive blackmail

Consider a blackmailer who launches a destructive program only when it predicts that its target would pay. Payment costs \(c\); refusing an actual attack costs \(L\gg c\).

Let \(D_B\) represent the response upon receiving blackmail. Assume:

- if \(D_B=\text{pay}\), an attack occurs with probability \(1\);
- if \(D_B=\text{refuse}\), an erroneous attack occurs with probability \(\varepsilon\);
- no attack produces zero loss.

Then
\[
Q_B(\text{pay})=-c,
\qquad
Q_B(\text{refuse})=-\varepsilon L.
\]
A-FDT refuses when
\[
\varepsilon L<c.
\]

With \(c=\$1{,}000\), \(L=\$1{,}000{,}000\), and \(\varepsilon=0.0009\), refusal has expected loss \(\$900\), versus \(\$1{,}000\) for payment.

The same comparison applies after receiving a letter, because observation selects \(D_B\); it does not force the letter to remain present in every hypothetical.

This is not unconditional stubbornness. If mistaken attacks are sufficiently frequent, paying can receive the higher score. Nor does the reasoning apply unchanged to an attacker who launches the program regardless of the target’s predicted response. Deterrence requires a genuine dependency.

In a perfectly predictive model, a refusing agent never receives the letter. Encountering that allegedly impossible event raises a separate modeling question: which assumption failed? Equation (AF) alone does not determine how to revise the model.

## 6. Applying A-FDT responsibly

For unfamiliar problems, a useful workflow is:

**First, specify outcomes and utilities.** Include all relevant benefits, costs, and consequences. A-FDT’s unusual hypotheticals do not excuse incomplete accounting.

**Second, identify the exact computation being evaluated.** Specify its model, observation input, and action set. Distinguish its mathematical output from the physical action implementing it.

**Third, identify dependent systems.** Does another process simulate this computation, predict its answer, or implement the same function on the same input? Or is the association merely evidential?

**Fourth, construct each intervention explicitly.** Set the selected computation’s output to \(a\), propagate the stipulated dependencies, and allow observation branches to change when appropriate.

**Finally, compare expected utilities and test sensitivity.** Vary prediction-error assumptions and disputed dependencies. If reasonable models recommend different actions, the unresolved issue is in the model, not in the maximization.

Several limitations deserve emphasis.

### Dependencies cannot simply be stipulated for convenience

The paper identifies learning subjunctive structure as a major open problem. An ordinary causal model is already additional information beyond a probability distribution. A-FDT requires still more: an account of how changing a logical answer changes other represented quantities.

The structural interpretation above works for clean examples with explicit simulations, copies, or stipulated predictors. It does not establish a general method for approximate human similarity, logically equivalent programs, cyclic prediction, or uncertain computational relationships.

### Action selection is not unrestricted policy selection

A policy is a mapping
\[
\pi:\mathcal X\to\mathcal A.
\]
Although the family \((D_x)_x\) induces such a mapping, Equation (AF) evaluates alternative actions at one selected computation-node.

The paper’s footnotes describe a preferred policy-selecting formulation, which instead compares outputs representing entire policies. That is a distinct formulation. One must not silently replace
\[
\operatorname{do}(D_x=a)
\]
with an intervention choosing an entire \(\pi\).

If multiple observation-dependent answers are logically linked, those links require modeling. Otherwise, independently optimizing coordinates need not establish global policy optimality.

### The philosophical defense is substantial but incomplete

A-FDT’s motivation is that effective deliberation should respect genuine dependencies wherever they occur—not only downstream physical effects. This explains cooperation with copies, credible repayment, and resistance to prediction-sensitive exploitation.

It also reframes dominance arguments. Two-boxing is better with the large-box contents fixed. That does not settle whether those contents should remain fixed under the relevant decision hypothetical.

However, success in these examples is not a theorem of universal superiority. The paper acknowledges that arbitrary environments can reward or punish particular algorithms. Its proposed restriction to “fair” problems remains informal. Likewise, an expected-utility representation theorem can support the optimization framework without uniquely establishing A-FDT’s counterfactual semantics.

## References

- Yudkowsky, E., and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2, especially §§3–6, 9 and footnotes 7, 16.
- Pearl, J. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.
- Joyce, J. M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

## Conclusion

A-FDT evaluates actions by intervening on a representation of its own decision computation. Its essential discipline is to preserve genuine computational and causal dependencies while breaking merely evidential associations. Equation (4) makes action selection precise once those dependencies are supplied; it does not make discovering them automatic. The theory’s promise lies in its coherent treatment of predictors and copies. Its chief unfinished task is a principled, usable account of the counterfactual models that such treatment requires.