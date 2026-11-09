# A-FDT: Choosing the Output of a Decision Procedure

A decision can be understood as a physical event: a hand reaches for a box, a payment is transmitted, or a prisoner announces cooperation. But it is also the output of a computation. That computation may be reproduced elsewhere—in another agent, a simulation, or a predictor’s reasoning.

**Action functional decision theory (A-FDT)** evaluates actions by intervening hypothetically on this computational output, rather than merely on the resulting physical act. Its central question is: which output of this very decision procedure corresponds to the best expected outcome, accounting for everything that depends on that output?

This essay takes Equation (4), Section 5, of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality* as its definition of A-FDT. The paper uses a broader name; here, **A-FDT specifically denotes its action-valued graphical rule**. That distinction matters because the paper also mentions a separate policy-output formulation.

## 1. The formal rule

Let:

- \(\mathcal A\) be a finite action set;
- \(X\) represent the agent’s observation history, with current value \(x\);
- \(O\) represent an outcome;
- \(V=U(O)\) be its utility, with finite expectations;
- \(P\) be the agent’s probabilistic world-model;
- \(G\) describe the relevant dependencies between variables in that model.

The distinctive ingredient is a model-variable \(D_{P,G,x}\), representing the output of the A-FDT procedure on inputs \((P,G,x)\). Abbreviate this variable as \(D_x\). Equation (4), with notation relabeled, becomes

\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
\in
\arg\max_{a\in\mathcal A}
\mathbb E_P\!\left[V\mid\operatorname{do}(D_x=a)\right].
}
\]

A fixed tie-breaking convention can make the rule single-valued; this is an implementation assumption rather than a substantive decision-theoretic principle.

Define the score

\[
Q_x(a)
=
\sum_o
P_G\!\left(O=o\mid\operatorname{do}(D_x=a)\right)U(o).
\]

A-FDT selects an action maximizing \(Q_x\). The difficult part is not maximizing expected utility, but constructing the interventional distribution.

For comparison, the paper presents **evidential decision theory (EDT)** as maximizing

\[
\mathbb E[V\mid X=x,A=a],
\]

where \(A\) is the physical action. It presents **causal decision theory (CDT)** as maximizing

\[
\mathbb E[V\mid\operatorname{do}(A=a),X=x].
\]

These three theories therefore differ in their decision hypotheticals:

- EDT conditions on taking an action.
- CDT intervenes on the physical action.
- A-FDT intervenes on the output of the computation producing the action.

A second difference is equally important. **A-FDT’s displayed rule does not additionally condition on \(X=x\).** Instead, \(x\) determines which computational-output variable is intervened upon. This allows an alternative output to change which observations occur in the hypothetical scenario.

Finally, \(D_x\) must not be confused with the actual value returned by the algorithm. One is a variable inside a model; the other is the result of evaluating that algorithm. The agent can represent its output before knowing it, just as a program can represent an expression before evaluating it. The paper invokes computational self-reference to explain how such representation is possible. This does not, by itself, establish that every proposed self-referential model is coherent or computationally tractable.

## 2. Subjunctive dependence and computational counterfactuals

The paper calls the relevant relationship **subjunctive dependence**. Two systems can depend on the same computation even when neither physically causes the other’s behavior.

Suppose two isolated machines execute the same deterministic program on identical inputs. Their outputs agree. If we hypothetically vary the output of that computation, we should vary both machines’ outputs together. By contrast, changing one machine’s casing from pink to green supplies no reason to change the other’s casing, even if their colors were previously correlated.

The intended distinction is therefore not simply between correlation and independence. It is between correlations supported by a dependency that should survive the decision hypothetical and correlations that should be broken.

The source treats ordinary causal dependence as included within subjunctive dependence. If a scribe copies a calculator’s display, her writing depends both causally and subjunctively on its output. A sufficiently accurate simulation may depend on the same computation without receiving a causal signal from the original machine.

Thus A-FDT’s graph is not necessarily a chronological causal graph. An arrow from \(D_x\) to yesterday’s prediction expresses computational dependence, not backward physical causation.

There is nevertheless a foundational difficulty. A fixed mathematical function has only one output on fixed inputs. If its output is \(a\), supposing that it instead outputs \(b\) can be logically impossible. A-FDT therefore needs **counterpossible** reasoning.

Ordinary Bayesian conditioning does not solve this problem: conditioning on a false mathematical statement may mean conditioning on an event of probability zero. Equation (4) instead uses graph surgery. The hypothetical is a modified computational model, not a claim that another output is genuinely mathematically possible.

This should not be interpreted as permission to change arbitrary facts. The intended intervention changes the selected output and its dependents while preserving the remaining mechanisms. Determining which mechanisms belong in that preserved structure is the theory’s principal unresolved problem.

## 3. A-FDT in opaque Newcomb problems and twin games

Consider Newcomb’s problem. An opaque box contains \(M\) dollars if a predictor predicted one-boxing, and nothing otherwise. A transparent box contains \(b\) dollars. The agent chooses the opaque box alone or both boxes.

In an A-FDT model, the structure includes

\[
D\longrightarrow A,
\qquad
D\longrightarrow\text{Prediction}
\longrightarrow\text{Opaque-box contents}.
\]

The two branches express that the agent implements the computation and the predictor models it.

Suppose the predictor tracks either hypothetical output with symmetric accuracy \(r\). Then

\[
Q(\text{one-box})=rM,
\]

whereas

\[
Q(\text{two-box})=(1-r)M+b.
\]

Consequently, A-FDT one-boxes exactly when

\[
(2r-1)M>b.
\]

For \(r=0.99\), \(M=1{,}000{,}000\), and \(b=1{,}000\), the scores are

\[
990{,}000
\quad\text{and}\quad
11{,}000.
\]

The agent is not trying to send a signal into the past. It compares a one-boxing computational output, usually predicted as such, with a two-boxing output, also usually predicted as such.

The accuracy assumption requires care. A historical success rate of \(99\%\) does not alone determine how a predictor responds under each computational intervention. More generally, write

\[
p_1=P(\text{full}\mid\operatorname{do}(D=\text{one-box})),
\]

\[
p_2=P(\text{full}\mid\operatorname{do}(D=\text{two-box})).
\]

A-FDT one-boxes when

\[
M(p_1-p_2)>b.
\]

The symmetric-error model supplies the additional assumptions \(p_1=r\) and \(p_2=1-r\). Counterfactual reliability, rather than aggregate accuracy alone, is what matters.

The same structure explains A-FDT’s cooperation with a perfect psychological twin. Using the paper’s payoffs, mutual cooperation gives each prisoner \(1{,}000{,}000\), mutual defection gives \(1{,}000\), and unilateral defection gives the defector \(1{,}001{,}000\).

If both prisoners implement the same computation on equivalent inputs, intervening on its output changes both choices:

\[
Q(\text{cooperate})=1{,}000{,}000,
\qquad
Q(\text{defect})=1{,}000.
\]

A-FDT cooperates for self-interested reasons.

This is not a prescription to cooperate with everyone described as rational or as following A-FDT. Different information, preferences, and computational inputs can produce different outputs. Without an appropriate dependency, the opponent’s action need not move with one’s own hypothetical output.

## 4. A-FDT and merely evidential correlations

The smoking-lesion problem supplies the contrasting case. In its fictional medical model, a lesion causes both a taste for smoking and cancer, but smoking itself does not cause cancer.

Let \(L\) denote the lesion and \(C\) cancer. The model contains a relationship \(L\to C\), but no dependency from the relevant decision output \(D\) to \(L\) or \(C\). Intervening on \(D\) therefore leaves disease risk unchanged.

In a streamlined version, suppose smoking supplies utility \(s>0\) and disease-free survival supplies utility \(H\). If

\[
q=P(C),
\]

then

\[
Q(\text{smoke})=H(1-q)+s,
\]

\[
Q(\text{refrain})=H(1-q).
\]

A-FDT smokes in this fictional model. The action can be evidence about the lesion without the lesion being a dependent of the action-producing computation.

The paper acknowledges that fully formalizing the traditional example is awkward. If the lesion changes preferences, it may also change which decision-output variable controls behavior. Its detailed treatment therefore distinguishes computations associated with different utility functions. The authors also discuss difficulties in making the stipulated action–lesion correlation accurate for a population of deliberating agents.

The robust lesson is narrower than a decisive refutation of every version of EDT: **A-FDT does not preserve a correlation merely because observing the action would convey information.** An environmental variable changes in the hypothetical only when the supplied dependency model says it should.

## 5. Observation selects the intervention, not a fixed hypothetical history

Transparent Newcomb’s problem reveals why the absence of \(X=x\) from Equation (4)’s conditioning matters.

Both boxes are visible. The predictor fills the large box if it predicts that the agent would one-box **upon seeing it full**. Let

\[
D_f=\text{the A-FDT output on observing “full”},
\]

\[
D_e=\text{the A-FDT output on observing “empty”}.
\]

The prediction depends on \(D_f\). Box contents determine the observation, which selects whether \(D_f\) or \(D_e\) controls the physical action.

Suppose the agent actually sees a full box. Equation (4) instructs it to compare

\[
\mathbb E[V\mid\operatorname{do}(D_f=\text{one-box})]
\]

with

\[
\mathbb E[V\mid\operatorname{do}(D_f=\text{two-box})].
\]

It does **not** instruct it to hold the observed fullness fixed in both hypotheticals.

Assume symmetric prediction accuracy \(r\), and let \(q\) be the modeled probability of two-boxing when the box is empty. Then

\[
Q_f(\text{one-box})
=
rM+(1-r)qb.
\]

The predictor usually predicts one-boxing, so the box is full and the selected computation controls the action. On the error branch, the box is empty and \(D_e\) controls behavior.

Similarly,

\[
Q_f(\text{two-box})
=
(1-r)(M+b)+rqb.
\]

Here the box is usually empty, so the computation currently being evaluated would usually not be physically implemented.

With \(r=0.99\), \(M=1{,}000{,}000\), \(b=1{,}000\), and \(q=1\), these scores are

\[
990{,}010
\quad\text{and}\quad
11{,}000.
\]

A-FDT therefore one-boxes despite seeing both boxes full.

The crucial separation is between factual belief and decision evaluation. The agent can correctly believe that the box is full. Its alternative-output hypothetical nevertheless contains a different observation because the observation depends on a prediction of that output.

Parfit’s hitchhiker has the same structure. A driver rescues the agent if she predicts payment after arrival. At the city, A-FDT intervenes on the payment-upon-arrival computation. A hypothetical refusal changes the prediction and can remove the rescue itself. Payment can therefore have the higher global score even though it has no remaining local benefit.

These cases motivate the source’s precommitment argument: an agent can obtain the benefits of a predictable commitment without installing an external enforcement mechanism. They do not, however, establish that action-output optimization always equals optimization over every possible contingent policy.

## 6. A-FDT and prediction-dependent threats

The same machinery can recommend resisting blackmail, but not unconditionally.

Suppose a blackmailer launches a damaging program only when predicting that the recipient will pay. Payment costs \(c\); publication causes loss \(H\). Let \(D_\ell\) represent the response upon receiving the letter.

Assume that a paying response is always targeted, while a refusing response is mistakenly targeted with probability \(\varepsilon\). With zero utility as the no-blackmail baseline,

\[
Q_\ell(\text{pay})=-c,
\]

\[
Q_\ell(\text{refuse})=-\varepsilon H.
\]

A-FDT refuses when

\[
\varepsilon H<c.
\]

For \(c=1{,}000\), \(H=1{,}000{,}000\), and \(\varepsilon=0.0009\), refusal scores \(-900\), better than payment’s \(-1{,}000\).

This can prescribe accepting a large loss on a rare realized branch—even while holding the letter. The justification concerns the overall consequences of a predictably refusing response, not a belief that refusal physically disables an already running program.

Conversely, if the threat is launched independently of the response, the deterrence dependency disappears. Refusal then offers no protection in the hypothetical model, and paying may maximize utility. A-FDT’s recommendation depends on the actual predictive mechanism, not on a blanket prohibition against paying threats.

## 7. Applying A-FDT when the graph is not given

Equation (4) is precise **conditional on a suitable model**. The paper explicitly acknowledges that it does not provide a general method for discovering the noncausal dependencies required by \(G\).

A useful operational interpretation is to instantiate the model with acyclic structural equations

\[
Z_i=h_i(\operatorname{Pa}_i,E_i),
\]

where the exogenous variables \(E_i\) represent background uncertainty. To evaluate \(a\), replace the equation for \(D_x\) by \(D_x=a\), preserve the background distribution, and recompute its descendants.

Writing \(O^{x\leftarrow a}(e)\) for the resulting outcome gives

\[
Q_x(a)
=
\mathbb E_{e\sim\mu}
\left[U\!\left(O^{x\leftarrow a}(e)\right)\right].
\]

This is an implementation proposal for finite toy models, not a solution to the paper’s graph-construction problem. The structural equations must already specify how predictors respond to hypothetical computational outputs.

A practical analysis should proceed through four questions.

**Which computation is being evaluated?** Identify its model, preferences, and observation input. Sharing an algorithm’s name does not establish that two agents evaluate the same function on the same inputs.

**What reproduces or predicts it?** Include simulations, equivalent computations, and their causal consequences. Preserve common-cause correlations only when the structural model warrants preserving them under intervention.

**Can the output change which observation occurs?** If so, retain those alternative branches. Replacing the entire model by a posterior conditioned on the current observation can erase precisely the dependency Equation (4) evaluates.

**How sensitive is the answer to uncertain dependencies?** Prediction errors, actuation failures, and imperfect computational similarity should be modeled explicitly. When plausible dependency models disagree, the action remains underdetermined by the available information.

The observation issue leaves an important boundary question. Equation (4) takes \(P\) as input but does not fully specify when background model revision should occur, or which information belongs in the observation input \(x\). For the examples above, a reasonable interpretation is to retain a model containing the predictor and all relevant observation branches. More general learning protocols require additional assumptions.

The action–policy distinction also limits what follows. A contingent policy is a map

\[
\pi:\mathcal X\to\mathcal A.
\]

A-FDT intervenes on the output associated with the current input \(x\). It does not automatically replace the entire map \(x\mapsto D_x\). Other outputs change only if the dependency model connects them to the selected intervention.

The paper’s footnotes mention a distinct **policy-output functional decision theory** that optimizes over such maps. Its prescriptions should not be silently attributed to A-FDT. Where outputs are otherwise independent, optimizing one policy coordinate need not find the jointly optimal policy.

Finally, the source offers examples and philosophical arguments, not a general optimality theorem. Its proposed class of “fair” problems remains incompletely formalized, and no decision theory wins in every environment deliberately constructed to reward a rival.

### References

Yudkowsky, Eliezer, and Nate Soares. *Functional Decision Theory: A New Theory of Instrumental Rationality*. [arXiv:1710.05060v2](https://arxiv.org/abs/1710.05060v2), especially Sections 3–6 and 9, and footnotes 7 and 16.

Pearl, Judea. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.

## Conclusion

A-FDT evaluates actions as alternative outputs of a fixed computation. Its hypotheticals preserve relevant computational and causal dependencies while breaking merely evidential correlations. Observations select the computation under evaluation; they need not remain fixed across its alternative-output scenarios.

Given an adequate dependency model, the procedure is straightforward expected-utility maximization. The unresolved challenge is constructing and justifying that model—especially when computations are only approximately shared, predictions are imperfect, or observations depend on the decision being evaluated.