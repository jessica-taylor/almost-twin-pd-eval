# A-FDT: Choosing Actions as Outputs of a Decision Function

An action can matter without physically causing everything that depends on it. A predictor may have simulated your reasoning yesterday; another agent may be running the same computation elsewhere. In such cases, changing only your bodily movement while holding the predictor or computational copy fixed may omit a decision-relevant dependency.

**Action functional decision theory (A-FDT)** evaluates alternatives by intervening on a representation of its own decision-function output. It asks which output of this particular computation corresponds to the best expected outcome, allowing both causal consequences and relevant computational dependencies to vary.

This essay takes Equation (4), Section 5 of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality* as its primary definition. That qualification matters. The paper also discusses choosing entire policies, but its displayed equation chooses actions. These formulations need not agree in every problem.

A-FDT supplies a precise maximization rule **given a suitable dependency model**. The principal unresolved difficulty is constructing that model. Understanding both parts—the rule and its missing foundations—is essential to applying the theory responsibly.

## 1. The defining equation

Let:

- \(\mathcal A\) be a finite action set;
- \(\mathcal X\) be a set of observation histories;
- \(O\) be an outcome variable;
- \(V=U(O)\) be utility, with finite relevant expectations;
- \(P\) be a probabilistic world-model;
- \(G\) describe causal, computational, and other relevant dependencies.

Write
\[
D_x:=\mathsf D_{\langle P,G,x\rangle}
\]
for a **variable inside the model** representing the output of A-FDT on inputs \((P,G,x)\). The brackets indicate an encoding of those inputs: \(D_x\) names a particular computation, not its already-known answer.

Renaming the paper’s notation, Equation (4) becomes
\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
\in
\arg\max_{a\in\mathcal A}
\mathbb E_{P,G}\!\left[V\mid\operatorname{do}(D_x=a)\right].
}
\tag{A}
\]
A fixed tie-breaking convention can make the output unique.

Define the action score
\[
Q_x(a)=\mathbb E[V\mid\operatorname{do}(D_x=a)].
\]
A-FDT constructs one hypothetical per action, computes these expectations, and outputs a maximizing action.

Two comparisons locate the novelty. Evidential decision theory evaluates
\[
Q_x^{\mathrm{EDT}}(a)=\mathbb E[V\mid X=x,A=a],
\]
where \(A\) represents physical action. Causal decision theory evaluates, in the paper’s graphical presentation,
\[
Q_x^{\mathrm{CDT}}(a)
=\mathbb E[V\mid\operatorname{do}(A=a),X=x].
\]

A-FDT differs in **both** its intervention target and its treatment of observations:

1. It intervenes on the logical decision-output variable \(D_x\), not directly on physical action \(A\).
2. Equation (A) contains no additional conditioning on \(X=x\). The observation history selects the node being intervened upon.

The second difference is easy to overlook and crucial in transparent Newcomb problems, rescue agreements, and predictive blackmail.

## 2. What should change in an A-FDT hypothetical?

The paper calls the relevant relationship **subjunctive dependence**. Its clearest examples are computational: two systems implementing the same function on the same input must agree, insofar as both implementations work correctly. An accurate predictor need not literally duplicate the computation, but its prediction tracks that computation’s output.

Causal dependence is included. If a decision output controls your hand, and your hand presses a switch, the resulting effects belong in the hypothetical. But ordinary statistical association is insufficient. A disease correlated with your action need not change when the represented decision output changes.

Thus A-FDT preserves neither every observed correlation nor only forward causal effects. It propagates the intervention through the dependencies represented in \(G\).

### An operational interpretation

For finite, acyclic examples, a useful implementation is an augmented structural model:
\[
Y_i=h_i(\operatorname{Pa}_i,W_i),
\]
where \(W\) contains exogenous uncertainty. Some arrows express physical causation; others express computational dependence.

To evaluate \(a\):

1. Replace the equation for \(D_x\) by \(D_x:=a\).
2. Keep the exogenous distribution and other structural equations unchanged.
3. Recompute descendants of \(D_x\).
4. Average the resulting utility:
   \[
   Q_x(a)=\mathbb E_W[U(O_a(W))].
   \]

This makes explicit the surgery described by the paper. It is an operational elaboration for manageable models, **not** a general solution to logical counterfactual reasoning.

In particular, a graph’s arrows alone are insufficient for numerical calculation. One also needs response functions or probability kernels, including behavior under interventions that may have zero probability in the original model. Those details must be supplied or inferred.

### Why the counterfactual can be logically impossible

A fixed mathematical function has only one output on fixed inputs. If A-FDT actually outputs \(a\), imagining the same computation outputting \(b\ne a\) is a *counterpossible*, not merely an unlikely physical event.

The paper treats hypotheticals as computational instruments constructed from beliefs, rather than ordinary possible worlds. Accordingly, surgery need not produce a globally consistent alternative mathematics. It provides a controlled representation in which one output is replaced and specified dependencies are propagated.

This interpretation also explains why A-FDT requires no backwards physical signal. Its hypothetical may contain a different past prediction, but the agent does not believe that moving her hand now transmits information yesterday.

## 3. A-FDT in Newcomb’s problem

There are two boxes. The transparent box contains \(k=\$1{,}000\). The opaque box contains \(M=\$1{,}000{,}000\) if a predictor predicted one-boxing, and nothing otherwise.

For a concrete model, assume an independent prediction-error mechanism with accuracy \(q\) under either candidate decision output. The dependency structure is
\[
D\longrightarrow A,
\qquad
D\longrightarrow \text{Prediction}
\longrightarrow B,
\]
where \(B\) indicates whether the opaque box is full.

Then
\[
Q(\text{one-box})=qM,
\]
and
\[
Q(\text{two-box})=(1-q)M+k.
\]
A-FDT one-boxes exactly when
\[
(2q-1)M>k.
\]
At \(q=.99\), the scores are
\[
\$990{,}000
\quad\text{and}\quad
\$11{,}000.
\]

These values follow from the stated symmetric error model. A historical record of “99% correct” does not, by itself, identify how prediction errors behave under each intervention. That is an additional modeling assumption, also implicit in the paper’s simple examples.

Causal decision theory holds the opaque box’s distribution fixed when intervening on physical action, so it assigns two-boxing an extra \(k\). A-FDT instead preserves the predictor’s responsiveness to the decision computation.

This also explains the disagreement about dominance. Two-boxing dominates when box contents are held fixed. But whether box contents should remain fixed is precisely the disputed counterfactual assumption. Dominance does not independently settle that dispute.

## 4. A-FDT separates prediction from mere correlation

### The smoking-lesion example

In the paper’s imaginary medical scenario, a lesion causes both a desire to smoke and cancer. Smoking itself has no harmful health effect. For an agent who enjoys smoking, let the benefit be \(b>0\).

If changing the relevant decision output does not change the lesion or cancer risk, both A-FDT hypotheticals retain the same health distribution. In a reduced model where this node directly controls smoking,
\[
Q(\text{smoke})-Q(\text{refrain})=b,
\]
so A-FDT smokes.

This is not a claim about real tobacco. It isolates a formal distinction: cancer is not predicting the decision function.

The paper’s fuller treatment is more intricate because the lesion changes preferences and hence which decision computation controls action. It introduces separate decision-output nodes for different utility inputs. Intervening on one node affects action only in branches where that computation is implemented; the utility advantage is correspondingly weighted by that branch’s probability.

The authors also acknowledge that the traditional lesion problem is contrived and problematic as a test of evidential decision theory. The durable lesson is narrower: **an association with action does not automatically establish dependence on the intervened computation**.

### The psychological-twin prisoner’s dilemma

Suppose two agents implement the same decision function on relevantly identical inputs. Mutual cooperation pays each \(\$1{,}000{,}000\); mutual defection pays \(\$1{,}000\). A unilateral defector receives \(\$1{,}001{,}000\), while the cooperator receives nothing.

Under the exact-copy assumption,
\[
A_1=D,\qquad A_2=D.
\]
A-FDT therefore compares
\[
Q(\text{cooperate})=\$1{,}000{,}000,
\qquad
Q(\text{defect})=\$1{,}000.
\]
It cooperates for self-interested reasons.

This does not imply cooperation with every similar-looking agent. Different information, preferences, algorithms, or prediction errors can weaken or remove the dependency. Merely labeling both participants “A-FDT agents” does not establish that their particular computations have identical outputs.

## 5. Observations select computations, not fixed hypothetical histories

The most distinctive feature of Equation (A) appears when the decision output influences which observation the agent receives.

Consider transparent Newcomb. The predictor fills the large box if it predicts that the agent would one-box **upon seeing it full**. Let
\[
D_f=\text{output on observing “full”},
\qquad
D_e=\text{output on observing “empty”}.
\]
The physical action is selected by the realized observation:
\[
A=
\begin{cases}
D_f,&B=\text{full},\\
D_e,&B=\text{empty}.
\end{cases}
\]

The predictor tracks \(D_f\), so intervening on \(D_f\) can change \(B\), thereby changing which computation controls the physical action.

Let prediction accuracy be \(q\), and let
\[
r=P(D_e=\text{two-box})
\]
in the retained model. Then
\[
Q_f(\text{one-box})
=qM+(1-q)rk,
\]
whereas
\[
Q_f(\text{two-box})
=(1-q)(M+k)+qrk.
\]

The first expression includes the possibility that a prediction error leaves the box empty, in which case \(D_e\), not \(D_f\), determines action. The second includes the possibility that changing \(D_f\) to two-box makes an empty box overwhelmingly likely.

For \(q=.99\),
\[
Q_f(\text{one-box})=990{,}000+10r,
\]
\[
Q_f(\text{two-box})=10{,}010+990r.
\]
Thus A-FDT one-boxes upon seeing a full box.

Its two-boxing hypothetical usually contains an empty box, although its actual observation is “full.” This is deliberate: the actual observation identifies \(D_f\); it is not imposed as an additional constraint on every hypothetical.

### Does A-FDT ignore evidence?

No—but one should not silently replace \(P\) by \(P(\,\cdot\mid X=x)\) and then claim to be applying Equation (A). That generally changes the theory.

A useful special case explains how ordinary evidence-sensitive choice can nevertheless emerge. Suppose an intervention on \(D_x\):

- cannot change whether \(X=x\);
- affects utility only in branches where \(X=x\).

Writing \(V_a\) for utility under the intervention gives
\[
Q_x(a)-Q_x(b)
=P(X=x)\,
\mathbb E[V_a-V_b\mid X=x].
\]
For positive \(P(X=x)\), the common factor does not affect the maximizing action. The unconditional score comparison therefore recovers the corresponding conditional comparison.

This derivation requires the stated locality assumptions. In transparent Newcomb they fail: changing \(D_f\) changes the probability of observing “full.”

### Parfit’s hitchhiker

The same structure explains paying a rescuer after reaching safety. A driver rescues someone only if she predicts that the person’s *safe-in-the-city computation* will output “pay.”

A-FDT intervenes on that computation. Changing its output can change whether rescue occurred and whether that computation ever controls the agent’s body. Paying is not justified by physically improving an already-completed rescue; it is justified through the predictive dependency.

## 6. A-FDT and predictive blackmail

A-FDT’s resistance to threats is conditional, not absolute.

Suppose a blackmailer attacks with probability \(s\) if the agent’s response computation outputs “pay,” and probability \(r\) if it outputs “refuse.” Payment costs \(c\); an attacked refuser suffers loss \(L\); no attack causes no loss.

Under this explicitly specified model,
\[
Q(\text{pay})=-sc,
\qquad
Q(\text{refuse})=-rL.
\]
A-FDT refuses when
\[
rL<sc.
\]

With perfect deterrence, \(r=0\), refusal wins. With sufficiently frequent mistaken attacks or sufficiently severe losses, paying can win.

Even after receiving the demand, Equation (A) uses the demand to identify the response node rather than conditioning all hypotheticals on an attack having occurred. This can prescribe accepting a severe loss on a rare mistaken-attack branch because the same response computation deters attacks elsewhere.

Conversely, if the attack is independent of any prediction of this computation, refusal has no deterrent advantage. A-FDT may then pay to avoid greater harm.

The practical question is therefore not “Does A-FDT refuse blackmail?” but “How does this attacker’s behavior depend on this response computation?” Without that dependency, importing the paper’s refusal result would be unjustified.

## 7. Actions, policies, and implementation limits

A policy is a mapping
\[
\pi:\mathcal X\to\mathcal A.
\]
The paper’s footnotes describe a preferred formulation that intervenes on a policy-valued output and then applies the policy to current observations. That is distinct from Equation (A), whose intervention changes one action-valued computation \(D_x\).

Although the family \(\{D_x\}\) induces policy-like behavior, changing one member is not generally equivalent to replacing the entire family. Simultaneous policy changes can couple observation branches differently, especially in multi-agent problems.

Accordingly, one should not silently reinterpret A-FDT as
\[
\arg\max_\pi\mathbb E[V\mid\operatorname{do}(\Pi=\pi)].
\]
That requires another formal specification: the policy variable, its dependencies, and its relation to the currently implemented computation.

Several further limits remain.

**Dependency discovery.** The paper explicitly leaves open how to infer general subjunctive dependencies. Observational agreement alone does not establish the appropriate intervention response. Mechanistic knowledge of predictors, simulations, and code is especially valuable.

**Self-reference.** The model must represent the computation using that very model. The paper appeals to self-representing programs and Kleene’s recursion theorem to explain how such naming can work. This does not establish that every self-referential decision problem has a tractable, uniquely coherent solution.

**Computational bounds.** Ideal expected-utility maximization may be intractable. The paper does not supply a general bounded approximation preserving all its desired properties.

**Comparative optimality.** Success on selected predictive dilemmas is not a theorem of universal superiority. The authors acknowledge that arbitrary environments can punish any named decision procedure, and their proposed restriction to “fair” problems remains incompletely formalized.

## 8. Applying A-FDT to an unfamiliar problem

A disciplined application should proceed in the following order.

First, specify outcomes, utilities, actions, and the exact computation being evaluated. Include its model and observation inputs; “my general disposition” is usually too vague.

Second, separate three relationships: physical causation, computational or predictive dependence, and mere statistical association. Ask what mechanism supports each proposed dependency.

Third, specify how interventions propagate. Predictor accuracy must mean something under each candidate output, not merely describe an aggregate historical correlation.

Fourth, represent observation-dependent control explicitly. A computation can be predicted without being physically executed in every hypothetical. Do not automatically hold its actual observation fixed.

Finally, calculate every action’s expected utility and test sensitivity to uncertain dependencies. As an additional modeling proposal—not a solution supplied by the paper—one can average over candidate augmented structural models or report which action wins across a plausible range. If reasonable models disagree, the honest result is conditional advice, not a categorical A-FDT verdict.

## References

- Yudkowsky, E., and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2, especially Sections 3–6 and 9, Equation (4), and footnotes 7 and 16.
- Pearl, J. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.
- Joyce, J. M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

## Conclusion

A-FDT evaluates actions by intervening on the represented output of a particular decision computation. Its hypotheticals preserve relevant causal and computational dependencies while breaking merely evidential associations. Observations select the computation under intervention rather than necessarily remaining fixed within every hypothetical.

This yields a coherent account of one-boxing, cooperation with exact computational twins, credible repayment, and predictive deterrence. Its central limitation is equally important: the maximization equation is only as determinate as the dependency model supplied to it.