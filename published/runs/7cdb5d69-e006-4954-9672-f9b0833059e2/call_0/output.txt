# A-FDT: Choosing the Output of a Decision Computation

A decision is both a physical event and the result of a computation. Usually, these descriptions suggest the same practical advice. Sometimes, however, another system predicts, copies, or independently implements the relevant computation. Then changing the hypothetical output of that computation can have implications beyond the physical consequences of the agent’s present action.

**Action functional decision theory (A-FDT)** evaluates alternatives at this computational level. It asks which output of the agent’s actual decision procedure corresponds to the best expected outcome, preserving relevant dependencies between that output and other parts of the world.

Here, A-FDT means specifically the **action-output rule in Equation (4), Section 5**, of Yudkowsky and Soares’s paper [1]. The paper also discusses a policy-output formulation. That distinction matters: choosing one action-output is not automatically equivalent to optimizing an entire policy.

## 1. The A-FDT decision rule

Let:

- \(\mathcal A\) be a finite action set;
- \(\mathcal X\) be a countable set of observation histories;
- \(O\) be an outcome variable;
- \(U(O)\) be utility, with all relevant expectations finite;
- \(P\) be a probabilistic world-model;
- \(G\) describe relevant causal, computational, mathematical, and other dependencies.

Write \(V=U(O)\). For a particular input \((P,G,x)\), introduce a variable
\[
D_x
\]
representing the output of the A-FDT computation on exactly those inputs. Importantly, \(D_x\) is a **variable inside the model**, not the action already obtained by running the computation.

In this abbreviated notation, the paper’s Equation (4) becomes
\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E_P\!\left[V\mid\operatorname{do}(D_x=a)\right].
}
\tag{4}
\]

For each candidate action \(a\), construct a hypothetical model in which the represented computation outputs \(a\). Propagate the implications specified by \(G\), calculate expected utility, and select a maximizing action. A deterministic implementation also needs a fixed tie-breaking convention.

Two comparisons clarify the distinctive proposal. **Evidential decision theory (EDT)** evaluates
\[
Q_{\mathrm{EDT}}(a)
=
\mathbb E[V\mid X=x,A=a],
\]
where \(A\) is the physical action variable. **Causal decision theory (CDT)** instead evaluates, in the paper’s presentation,
\[
Q_{\mathrm{CDT}}(a)
=
\mathbb E[V\mid\operatorname{do}(A=a),X=x].
\]

A-FDT differs in both the **intervention target** and the **treatment of observations**:

1. It intervenes on \(D_x\), not directly on \(A\).
2. It uses \(x\) to identify the computation being evaluated, rather than additionally conditioning the expectation on \(X=x\).

The second difference is essential. Adding \(X=x\) to Equation (4) generally changes the theory.

The self-reference is deliberate: the algorithm evaluates hypothetical outputs of the very computation currently selecting an output. As the paper emphasizes, representing a computation does not require already knowing its result. Nevertheless, having a self-description does not by itself solve the harder problems of computing counterfactual values or constructing a consistent model.

## 2. Constructing A-FDT counterfactuals

The relevant relationship is called **subjunctive dependence** in the source. Two systems may be linked because they implement, represent, or reliably track the same computation, even when neither system’s present behavior physically causes the other’s.

Suppose two isolated machines execute the same deterministic program on the same input. A-FDT does not evaluate an alternative program output while arbitrarily holding one machine’s corresponding output fixed. Both implementations belong in the hypothetical.

This does **not** mean preserving every observed correlation. A common cause can correlate two events without either being an implementation or prediction of the other. A disease may influence both someone’s preferences and their health; changing the hypothetical output of their deliberation need not change the disease.

A useful operational interpretation is to supply a **modular structural model**. This develops the paper’s graphical proposal, rather than supplying its missing general theory of logical dependence. For a finite acyclic model, let variables satisfy equations
\[
Z_i=f_i(Z_{\operatorname{pa}(i)},\xi_i),
\]
with exogenous uncertainty represented by \(\xi\). Include \(D_x\), physical actions, predictions, observations, and utility among the variables.

To evaluate \(a\):

- replace the equation determining \(D_x\) by \(D_x:=a\);
- retain the remaining structural equations;
- recompute the resulting variables;
- average utility over the stipulated exogenous distribution.

Equivalently, for fully specified kernels \(K_i\), the modified distribution has the truncated factorization
\[
P_a(z)
=
\mathbf 1\{z_{D_x}=a\}
\prod_{i:Z_i\ne D_x}
K_i(z_i\mid z_{\operatorname{pa}(i)}).
\]

Here, arrows need not represent physical causation. An arrow from a logical-output variable to yesterday’s prediction represents a dependency between the prediction and the computation being predicted—not a signal traveling backward in time.

There is a substantial qualification. A deterministic mathematical function has only one output on a fixed input. Alternative assignments to \(D_x\) are therefore often **counterpossible**: contrary to mathematical fact, not merely contrary to actuality. Ordinary Bayesian conditioning cannot evaluate a logically impossible event of probability zero.

The structural interpretation handles this locally by replacing one represented equation while retaining others. It does not close the resulting hypothetical under every logical consequence, which would make an inconsistent antecedent useless.

This supplies calculations **given a model**. It does not tell us which model is correct. Moreover, a graph and an observational distribution may leave behavior on impossible or unobserved input combinations unspecified. Counterfactual use requires additional structural equations or kernels covering those combinations. The paper explicitly identifies the construction of adequate subjunctive-dependency models as a major open problem.

## 3. A-FDT in Newcomb’s problem and the lesion problem

### Newcomb’s problem

An opaque box contains \(M=\$1{,}000{,}000\) if a predictor predicts one-boxing, and nothing otherwise. A transparent box contains \(s=\$1{,}000\).

For a concrete model, suppose the prediction tracks \(D\), the relevant A-FDT output, with independent symmetric accuracy \(r\):
\[
\Pr(\widehat D=D\mid\operatorname{do}(D=a))=r
\]
for either action. This is a structural assumption; an aggregate historical accuracy figure alone would not establish both counterfactual probabilities.

The dependency pattern is
\[
D\longrightarrow A,\qquad
D\longrightarrow\widehat D\longrightarrow B,
\]
with \(A\) and box contents \(B\) determining utility.

A-FDT evaluates
\[
Q(\text{one})=rM,
\qquad
Q(\text{two})=(1-r)M+s.
\]
Thus one-boxing is preferred exactly when
\[
(2r-1)M>s.
\]

At \(r=0.99\),
\[
Q(\text{one})=\$990{,}000,\qquad
Q(\text{two})=\$11{,}000.
\]

A-FDT therefore one-boxes. It does not believe that reaching for one box physically changes its contents. Rather, its alternatives preserve the stipulated relationship between the computation and its predictor.

CDT holds the box-filling process fixed under a physical-action intervention, making the extra \(\$1{,}000\) attractive. Consequently, the familiar dominance argument for two-boxing already assumes a particular intervention target. It does not independently settle whether that target is appropriate.

### The fictional smoking lesion

Now suppose a lesion influences both smoking behavior and cancer, while smoking itself has no effect on cancer. Let smoking provide a positive utility increment \(c\).

If changing the relevant decision output changes smoking but leaves lesion and cancer variables unchanged, then
\[
Q(\text{smoke})-Q(\text{refrain})=c>0.
\]
A-FDT smokes in this fictional setting. The lesion is not predicting the deliberation’s conclusion.

The paper’s fuller treatment is more delicate: the lesion influences preferences, creating different preference-dependent decision computations. Intervening on one such computation changes behavior only in the branch where it controls action. The utility improvement is then \(c\) multiplied by that branch’s probability.

The authors themselves acknowledge difficulties in making the standard lesion story coherent. Its durable lesson is narrower: **statistical association alone is not a reason to propagate a change through an A-FDT hypothetical**.

## 4. A-FDT cooperation without magical coordination

Consider the paper’s prisoner’s dilemma against a perfect psychological twin. Each player receives:

- \(\$1{,}000{,}000\) for mutual cooperation;
- \(\$1{,}000\) for mutual defection;
- \(\$1{,}001{,}000\) for defecting against cooperation;
- nothing for cooperating against defection.

If both players implement the same relevant computation, up to the appropriate symmetry of their situations, then intervening on its output changes both decisions. A-FDT compares mutual cooperation with mutual defection and cooperates.

For imperfect dependence, define
\[
q_C=\Pr(A_{\mathrm{other}}=C\mid\operatorname{do}(D=C)),
\]
\[
q_D=\Pr(A_{\mathrm{other}}=C\mid\operatorname{do}(D=D)).
\]
Then
\[
Q(C)=1{,}000{,}000q_C,
\qquad
Q(D)=1{,}000+1{,}000{,}000q_D.
\]
Cooperation is preferred when
\[
q_C-q_D>0.001.
\]

This makes the operative issue precise: how much does the other player’s behavior vary across the computational hypotheticals?

Merely knowing that another player is intelligent, similar, or also follows A-FDT does not establish the required dependence. Different observations, utilities, or models can produce different computations. A-FDT is not a general instruction to cooperate.

## 5. Observations select the A-FDT intervention

The most surprising consequences of Equation (4) concern observations that themselves depend on the output under evaluation.

Define, for fixed \(P,G\), one output variable per history:
\[
D_x=\text{represented output on input }x.
\]
The physical action can be modeled by a selector,
\[
A=D_X.
\]

Although the actual history is \(x\), intervening on \(D_x\) may change \(X\). In the resulting hypothetical, the physical action may therefore be selected from a different node \(D_y\). Consequently,
\[
\operatorname{do}(D_x=a)
\]
does not always imply that the hypothetical physical action equals \(a\).

### A-FDT with transparent boxes

Suppose both Newcomb boxes are transparent. The predictor fills the large box precisely when it predicts that the agent would one-box **upon seeing it full**.

Introduce
\[
D_f=\text{output on seeing a full box},
\qquad
D_e=\text{output on seeing an empty box}.
\]
The predictor tracks \(D_f\), not necessarily the action eventually performed. Actual action is
\[
A=
\begin{cases}
D_f,&B\text{ is full},\\
D_e,&B\text{ is empty}.
\end{cases}
\]

In the paper’s model, \(D_e\) does not influence the prediction. It therefore outputs two-boxing: taking the small box adds money whenever the empty-box branch is implemented.

Assume independent symmetric prediction accuracy \(0.99\). To determine \(D_f\), A-FDT compares
\[
Q_f(\text{one})
=
0.99M+0.01s
=
\$990{,}010
\]
with
\[
Q_f(\text{two})
=
0.01(M+s)+0.99s
=
\$11{,}000.
\]
It one-boxes upon seeing the full box.

In the second hypothetical, the predictor usually leaves the large box empty, so the physical agent usually implements \(D_e\), not \(D_f\). Conditioning again on seeing a full box would remove precisely these branches and produce a different evaluation.

A-FDT does not deny the actual observation. It distinguishes **what is observed** from **what must remain fixed in the decision hypothetical**.

### A-FDT in Parfit’s hitchhiker

The same structure appears when a driver rescues an agent only if the driver predicts payment upon arrival.

Let \(D_{\mathrm{city}}\) represent the payment decision in the city. With perfect prediction, outputting “pay” corresponds to rescue followed by payment; outputting “refuse” corresponds to no rescue. If survival is worth \(L\) and payment costs \(c<L\), the relevant comparison is
\[
L-c\quad\text{versus}\quad 0.
\]

A-FDT pays after arriving. The explanation is instrumental rather than moral: the payment computation helps determine whether the city branch is reached.

This observation treatment should not be inflated into a prohibition on factual learning. Equation (4) specifies how the supplied \(P,G,x\) are used; the paper does not give a complete account of how an agent should acquire and revise its encompassing model throughout its life.

## 6. A-FDT and prediction-sensitive blackmail

Suppose an attacker launches a threat according to a prediction of the agent’s response. Payment costs \(c\); refusal after an attack causes loss \(L\).

Let
\[
p_P=\Pr(\text{attack}\mid\operatorname{do}(D_{\mathrm{letter}}=\text{pay})),
\]
\[
p_R=\Pr(\text{attack}\mid\operatorname{do}(D_{\mathrm{letter}}=\text{refuse})).
\]
Assuming no loss when no attack occurs,
\[
Q(\text{pay})=-p_Pc,\qquad
Q(\text{refuse})=-p_RL.
\]
A-FDT refuses when
\[
p_RL<p_Pc.
\]

For \(p_P=1\), \(c=\$1{,}000\), and \(L=\$1{,}000{,}000\), refusal is preferred if
\[
p_R<0.001.
\]

This can recommend refusal even when an erroneous attack actually occurs. The agent does not expect refusal physically to erase the threat; its criterion compares the encompassing computational hypotheticals.

The qualification is crucial. If the attacker launches regardless of the relevant computation, then \(p_P=p_R=1\), and payment is preferable when \(c<L\). A-FDT is not unconditional stubbornness. Its resistance depends on the threat being sufficiently sensitive to the predicted response. Real-world application therefore requires evidence for that structural relationship, not merely an attacker’s assertion.

## 7. Applying A-FDT beyond the examples

A practical analysis should make four stages explicit.

**First, identify the computation.** Specify its model, goals, observations, and output variable. Do not silently merge different histories or agents into one decision node.

**Second, specify dependencies.** Separate physical consequences, genuine implementations or predictions, and merely statistical associations. Give prediction-error mechanisms, including how they behave under alternative outputs.

**Third, propagate the intervention.** For each action, replace the represented output and follow the supplied structural relations. Permit observations and branch selection to change where the model requires it.

**Fourth, compare expected utilities and test robustness.** Vary uncertain dependency strengths and error rates. If the answer changes across plausible models, the conclusion is conditional, not determined by the slogan “use A-FDT.”

Structural uncertainty can itself be represented probabilistically—for example, by a latent variable indicating whether an opponent is simulating the agent or acting independently. That is a reasonable modeling extension, not a method supplied by the paper for discovering such uncertainty or assigning its probabilities.

Another boundary concerns policies. For fixed inputs \(P,G\), the family
\[
\pi(x)=D_x
\]
resembles an observation-to-action policy. But Equation (4) intervenes on **one component** \(D_x\). Other components change only through dependencies explicitly represented in \(G\). It does not automatically optimize the whole vector \((D_y)_y\) jointly.

The paper’s footnotes describe a preferred **policy-output functional decision theory**, which intervenes on a policy-producing computation. That is a distinct formulation. Its prescriptions cannot simply be imported into A-FDT, especially in multi-agent problems where coordinated changes across histories may matter.

Finally, the source’s broader claims require calibrated interpretation. Its examples motivate advantages concerning precommitment, information, and reflective stability. They do not constitute a general theorem that Equation (4), under arbitrary models, always achieves those advantages. Expected-utility representation results justify the form of maximization given a counterfactual perspective; they do not establish that perspective’s correctness. Nor does the paper prove universal superiority: it acknowledges both the difficulty of formalizing “fair” comparisons and the impossibility of winning every deliberately theory-targeted problem.

### References

[1] Eliezer Yudkowsky and Nate Soares. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2, especially §§3–6, 9, and notes 7 and 16.

[2] Judea Pearl. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.

[3] James M. Joyce. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

## Conclusion

A-FDT changes the object of decision-theoretic intervention: from a physical action to the output of the computation selecting it. This preserves prediction and replication dependencies without preserving every statistical correlation. Its treatment of observations is equally important: observations select a decision node, but need not remain fixed across its hypotheticals.

Given adequate structural assumptions, Equation (4) supplies a precise expected-utility calculation. The unresolved challenge is obtaining those assumptions reliably—especially for counterpossible computational alternatives. A-FDT is therefore both an actionable modeling framework and an unfinished theory of which counterfactual dependencies rational deliberation should respect.