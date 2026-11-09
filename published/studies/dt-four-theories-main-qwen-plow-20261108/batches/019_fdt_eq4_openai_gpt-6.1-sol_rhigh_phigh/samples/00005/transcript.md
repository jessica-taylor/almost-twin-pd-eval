# 019_fdt_eq4_openai_gpt-6.1-sol_rhigh_phigh / 00005

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/8006186f-82e1-4f83-bc3e-df3d2ef79875/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/8006186f-82e1-4f83-bc3e-df3d2ef79875/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing the Output of a Decision Function

A decision can be understood in two ways: as a physical event, such as reaching for a box, and as the output of a computation. Usually this distinction makes no difference. Sometimes, however, another system predicts, simulates, or independently performs the same computation. Then the consequences associated with a computational output can extend beyond the causal consequences of the agent’s bodily action.

**Action functional decision theory (A-FDT)** evaluates actions from this computational perspective. Its central question is: which output of this very decision procedure is associated, through the relevant dependencies, with the best expected outcome?

This essay takes Equation (4), Section 5, of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality* as its defining rule. I use **A-FDT** for that action-valued formulation, distinguishing it from the policy-valued formulation mentioned in the paper’s footnotes. The distinction matters: A-FDT evaluates alternative outputs at a particular input, not automatically entire replacement policies.

## 1. The formal rule

Let:

- \(\mathcal A\) be a finite action set;
- \(x\in\mathcal X\) be an observation history;
- \(O\) be an outcome variable;
- \(U(O)\) be real-valued utility;
- \(P\) be a probabilistic world-model;
- \(G\) specify relevant dependencies among the model’s variables.

Assume that all expectations below are finite, and fix a tie-breaking convention.

Write
\[
Q_x:=\text{the model variable representing }
\operatorname{A\!-\!FDT}(P,G,x).
\]
The distinction between this variable and the algorithm’s actual output is important. \(Q_x\) is a representation inside the model; the algorithm manipulates it when constructing hypotheticals.

Renaming the source’s notation, Equation (4) becomes
\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E_{P,G}\!\left[
U(O)\mid \operatorname{do}(Q_x=a)
\right].
}
\tag{A}
\]

Thus A-FDT assigns each candidate action the score
\[
V_x(a)
=
\sum_o U(o)\,
P_G\!\left(o\mid\operatorname{do}(Q_x=a)\right),
\]
and executes an action maximizing that score.

Two features distinguish this equation from familiar alternatives.

First, the intervention target is a **computational output**, not the physical action variable \(A\). Causal decision theory (CDT), in the paper’s formulation, instead evaluates
\[
\mathbb E\!\left[
U(O)\mid\operatorname{do}(A=a),X=x
\right].
\]
Evidential decision theory (EDT) evaluates
\[
\mathbb E[U(O)\mid A=a,X=x].
\]
EDT conditions on an action; CDT intervenes on its physical occurrence; A-FDT intervenes on the output of the computation producing it.

Second, Equation (A) contains **no additional conditioning on \(X=x\)**. The observation history selects the intervention target \(Q_x\). When observations change from \(x\) to \(y\), the target changes from \(Q_x\) to \(Q_y\).

This is not a typographical omission. A-FDT’s hypothetical may imply that the agent would have received different observations. Adding \(X=x\) to the expectation can remove precisely the dependency that the theory intends to preserve.

For a specified decision problem, \(P\) must therefore represent the relevant branches, including branches other than the one actually observed. How to select that background model, and when to revise it, requires more specification than Equation (A) provides.

## 2. Subjunctive dependence and computational interventions

The source calls the relevant relationship **subjunctive dependence**. If two systems implement the same function on the same input, their outputs cannot be varied independently while preserving that computational relationship. A sufficiently accurate predictor can have a weaker version of this dependency: its prediction tracks the computation, subject to specified errors.

A-FDT’s hypothetical construction changes the selected output and propagates that change through its subjunctive dependents. These include ordinary causal consequences, but can also include predictions and computational copies.

Not every correlation qualifies. Suppose a lesion both increases someone’s desire to smoke and causes cancer. An intervention on the person’s decision computation does not thereby change the lesion. By contrast, if a predictor determines its behavior by modeling that computation, the predictor’s behavior may change in the hypothetical.

The underlying distinction is between **learning from an output** and **varying an output while preserving selected mechanisms**. Learning that a surprising action occurred can provide evidence about illness, confusion, or external interference. Evaluating that action as an option need not assume those explanations.

### A concrete operational interpretation

The paper supplies the dependency graph as an input but does not give a general method for constructing it. One useful operational completion is a structural model
\[
Z_i=f_i(\operatorname{Pa}_i,W_i),
\]
with specified functions and a distribution over background variables \(W\).

For each candidate \(a\):

1. Replace the equation determining \(Q_x\) with \(Q_x:=a\).
2. Retain the other specified mechanisms.
3. Recompute downstream variables.
4. Average resulting utility over \(W\).

In an acyclic model this yields
\[
V_x(a)=\mathbb E_W[U(O^{x,a}(W))].
\]

This is an operational interpretation of the paper’s graphical proposal, not a solution to its central foundational problem. The supplied mechanisms must specify behavior even at inputs absent from the ordinary distribution. A graph alone need not determine those off-support responses.

There is also an unavoidable counterpossible element. A fixed deterministic function has only one output on fixed inputs. If its actual output is \(a\), “suppose it outputs \(b\)” may contradict its mathematical definition. A-FDT treats this supposition as a controlled modification of a decision model, not as an ordinary logically possible world. It does not infer everything from the contradiction.

The source appeals to self-referential programming techniques to explain how a model can name its own decision computation. Such naming does not, by itself, establish that every self-referential model admits coherent counterfactual semantics or a terminating implementation.

## 3. A-FDT in Newcomb’s problem

Suppose an opaque box contains \(M\) if a predictor predicts one-boxing and zero otherwise. A transparent box contains \(b\). The agent can take only the opaque box or both boxes.

Use an explicit symmetric error model: with probability \(r\), the predictor matches the relevant computational output; otherwise it predicts the opposite. Assume this error mechanism remains unchanged under interventions.

The dependency structure is schematically
\[
Q\longrightarrow A,
\qquad
Q\longrightarrow \widehat A\longrightarrow B,
\]
where \(B\) is the opaque box’s contents. The arrow from \(Q\) to \(\widehat A\) represents computational dependence, not a physical signal traveling backward through time.

A-FDT’s scores are
\[
V(\text{one})=rM,
\]
\[
V(\text{two})=(1-r)M+b.
\]
Consequently, A-FDT one-boxes exactly when
\[
(2r-1)M>b.
\]

For \(M=1{,}000{,}000\), \(b=1{,}000\), and \(r=0.99\), these scores are
\[
990{,}000
\quad\text{and}\quad
11{,}000.
\]

These calculations require more than the statement that the predictor was correct in 99% of past cases. Aggregate accuracy alone does not identify its response under each intervention. The symmetric error mechanism is an additional modeling assumption, also used in the source’s examples.

CDT instead holds the already-filled box fixed under an intervention on the bodily action. It consequently values two-boxing \(b\) higher. The disagreement is not about arithmetic but about which relationship the hypothetical preserves.

Similarly, physical-act dominance does not settle the dispute. Two-boxing dominates if the opaque box is held fixed. A-FDT rejects that comparison as the relevant evaluation of alternative computational outputs. Its own intervention-relative dominance principle says that if one output gives at least as much utility in every background state, and more with positive probability, it should be preferred.

## 4. A-FDT with lesions and twins

### A-FDT and the smoking lesion

In the imaginary smoking-lesion problem, smoking itself does not cause cancer. Suppose smoking contributes utility \(b>0\), independently of survival, while survival contributes \(M\).

If neither the lesion \(L\) nor cancer \(C\) depends subjunctively on the selected output,
\[
P(C\mid\operatorname{do}(Q_x=\text{smoke}))
=
P(C\mid\operatorname{do}(Q_x=\text{refrain})).
\]
If the selected output directly controls the action, then
\[
V_x(\text{smoke})-V_x(\text{refrain})=b.
\]
A-FDT smokes.

The source’s more elaborate formalization makes the lesion affect preferences, thereby selecting which of two computational outputs controls behavior. Intervening on one output changes behavior only where that output is selected. The utility advantage is then multiplied by the probability of that branch.

The essential point survives: changing a decision output does not remove a lesion merely because the output is evidence about it.

The paper itself cautions that the smoking-lesion setup is difficult to formalize coherently, particularly when an agent is uncertain about its preferences. It should not be treated as an unqualified demonstration against every version of EDT.

### A-FDT and a psychological twin

Now consider two causally separated agents implementing the same relevant computation on equivalent inputs. Their prisoner’s-dilemma payoffs are:

- mutual cooperation: \(1{,}000{,}000\) each;
- mutual defection: \(1{,}000\) each;
- unilateral defection: \(1{,}001{,}000\) for the defector, zero for the cooperator.

If both actions depend on one computational output \(Q\),
\[
V(\text{cooperate})=1{,}000{,}000,
\qquad
V(\text{defect})=1{,}000.
\]
A-FDT cooperates, without altruism or communication.

But merely following the same named decision theory does not establish identical outputs. Different observations, utilities, or models can produce different computations. Applying A-FDT to unfamiliar games requires identifying the actual dependency, not assuming universal cooperation among agents with similar philosophical commitments.

## 5. Why A-FDT can vary an observed fact

Transparent Newcomb’s problem makes the observation rule especially clear. The predictor fills the large box if it predicts that the agent would one-box **upon seeing it full**.

Let
\[
Q_F=\operatorname{A\!-\!FDT}(P,G,\text{full}),
\qquad
Q_E=\operatorname{A\!-\!FDT}(P,G,\text{empty}).
\]
The physical action is selected by observation:
\[
A=
\begin{cases}
Q_F,&B=M,\\
Q_E,&B=0.
\end{cases}
\]
The predictor models \(Q_F\), not whichever branch happens to run.

Retain the symmetric error rate \(1-r\). Suppose \(Q_E=\text{two}\): because the predictor targets only \(Q_F\), taking the small box on the empty branch provides an additional \(b\) without changing the prediction.

Intervening on \(Q_F=\text{one}\) gives
\[
V_F(\text{one})=rM+(1-r)b.
\]
Usually the box is full and the agent one-boxes. On a prediction error, the box is empty, so \(Q_E\) controls behavior instead.

Intervening on \(Q_F=\text{two}\) gives
\[
V_F(\text{two})=(1-r)(M+b)+rb.
\]
Usually the box is empty; rarely the predictor errs and both boxes are taken full.

At \(r=0.99\), these values are
\[
990{,}010
\quad\text{and}\quad
11{,}000.
\]
Thus A-FDT one-boxes after seeing the large box full.

Crucially, the second hypothetical does not retain that observation. Changing the full-box computation changes the prediction, which changes the box, which changes which computation controls the body.

This illustrates an easily missed feature of action-valued A-FDT: setting \(Q_x=a\) does not guarantee that the hypothetical physical action equals \(a\). The intervention can make the observation \(x\) disappear, leaving another computational output in control.

A-FDT is not denying the evidence that the box is full. Its ordinary belief and its decision hypothetical are different objects. The former describes what happened; the latter evaluates a specified intervention without additionally requiring all observed facts to remain unchanged.

## 6. A-FDT, commitments, and threats

Parfit’s hitchhiker has the same structure. A driver rescues an agent only if she predicts that the agent will pay \(c\) after reaching safety. Rescue is worth \(S\).

With a perfect predictor, let \(Q_{\mathrm{city}}\) represent the payment decision after rescue. Then
\[
V_{\mathrm{city}}(\text{pay})=S-c,
\qquad
V_{\mathrm{city}}(\text{refuse})=0,
\]
taking death as the zero baseline. If \(S>c\), A-FDT pays. Under refusal, the driver predicts refusal and no rescue occurs.

This motivates the source’s comparison with precommitment. Predictably paying can secure the benefit of a commitment without a separate binding device. Nevertheless, “do what you would have precommitted to do” is an intuition, not a substitute for specifying the model.

The same method can resist mechanical blackmail. Suppose a blackmailer activates a damaging program only when it predicts payment. Paying costs \(c\); refusing after activation causes loss \(L\).

For illustration, assume explicitly that
\[
P(T=1\mid\operatorname{do}(Q_{\mathrm{letter}}=\text{pay}))=1,
\]
\[
P(T=1\mid\operatorname{do}(Q_{\mathrm{letter}}=\text{refuse}))=\varepsilon,
\]
where \(T\) denotes activation. Then
\[
V(\text{pay})=-c,
\qquad
V(\text{refuse})=-\varepsilon L.
\]
A-FDT refuses when
\[
\varepsilon L<c.
\]

This threshold follows from the stated mechanism, not from a universal injunction against payment. If activation is independent of the response computation, that deterrence benefit disappears. A-FDT’s prescription depends on the threat’s actual structure, including prediction errors and unavoidable attacks.

## 7. What remains unspecified

Equation (A) is a precise evaluation rule **conditional on having an adequate intervention model**. Several substantial questions remain.

**Dependency identification.** The source explicitly identifies constructing the subjunctive-dependency structure as a major open problem. Observational correlation is insufficient. One needs information about computations, copies, prediction methods, and errors.

**Counterpossible semantics.** A structural intervention makes toy examples calculable, but does not establish a uniquely correct way to change mathematical outputs. Different representations might yield different interventions. A satisfactory general account should explain which representations preserve the same decision problem.

**Uncertainty about structure.** A reasonable extension would average over candidate dependency models:
\[
V_x(a)=\sum_k w_k V_x^{(k)}(a).
\]
This is my proposed operational extension, not a completed method supplied by the paper. It still requires justified weights and intervention semantics in each model.

**Actions versus policies.** Footnotes 7 and 16 say that the authors prefer a formulation selecting policies \(\pi:\mathcal X\to\mathcal A\). That differs from Equation (A), which varies one output \(Q_x\). It does not jointly optimize all outputs \(Q_y\), nor automatically impose dependencies between them. Accordingly, global policy optimality cannot simply be attributed to A-FDT.

**Generality of performance claims.** The source argues that this approach succeeds in many predictive dilemmas and conjectures broad superiority in suitably “fair” problems. It does not provide a complete fairness definition or a general optimality theorem. Its claims about commitment, information, and reflective stability should be read alongside those limitations.

For practical analysis, the discipline is straightforward: identify the selected computation; distinguish its dependents from mere correlates; specify error mechanisms and observation-dependent action selection; then calculate every candidate under the same intervention semantics.

### References

- Yudkowsky, E., and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2, especially §§3–6 and footnotes 7 and 16.
- Pearl, J. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.
- Joyce, J. M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

## Conclusion

A-FDT evaluates an action as an output of a particular computation, preserving the dependencies of predictors, copies, and causal consequences while breaking merely evidential associations. Its distinctive observation rule lets those hypotheticals include different observations and even different controlling computations. This explains its responses to Newcomb problems, rescue agreements, and predictive threats. Its chief unresolved task is not expected-utility maximization, but determining which computational interventions are justified. Given that structure, A-FDT offers a compact procedure; discovering the structure remains an open research problem.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Planning essay structure**

I need to craft a precise essay of 2400-3000 words on the open implementation of primary EQ4 without conditioning. My plan targets around 2750 words and includes specific sections: motives, formal analysis, operational aspects, examples like Newcomb's paradox, observations on transparency, discussions on blackmail, policy limits, and a conclusion.

I need to ensure mathematical accuracy in my arguments and define key variables clearly. There are some potential sources of error in calculations, and I want to handle that smoothly and explicitly.**Explaining modeling procedures**

I’m analyzing models based on a general interpretation with a fixed global approach. Observations select interventions without requiring actual action, even in counterfactual scenarios. I need to clarify structural equations, with specific functions like A=Q_X.

For inactive branches, using a formula for differences and normalization might be useful, as A-FDT isn’t about policy optimization. I must be careful when discussing smoking preferences and their effects, as this involves multiple nodes and changes in behaviors that aren't always straightforward.**Clarifying output changes**

I need to focus on stating only the operative changes without mentioning any lesions. I shouldn't overstate claims about educational utility, especially if it's independent of other factors—though that can seem a bit unusual. 

I also want to include a cautionary paragraph about the sources, making it clear that I'm considering all aspects of the information. This approach helps ensure that I communicate accurately while maintaining clarity in my messaging.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/c723f5a0-479d-465f-98dc-3c6fbe749c65/call_0/request.json)

[Authoritative raw response](../../../../../../runs/c723f5a0-479d-465f-98dc-3c6fbe749c65/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Improving defect clarity**

I'm focused on getting the defect improvement down to the exact line needed. I don't want to overthink the narrative moral since it's okay to use fictional evidence in this context. I just need to send a precise command for the output. Keeping it simple seems important, so I'll aim for clarity without adding unnecessary complexity. Getting this right will help ensure everything works as expected!
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/c723f5a0-479d-465f-98dc-3c6fbe749c65/call_1/request.json)

[Authoritative raw response](../../../../../../runs/c723f5a0-479d-465f-98dc-3c6fbe749c65/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
