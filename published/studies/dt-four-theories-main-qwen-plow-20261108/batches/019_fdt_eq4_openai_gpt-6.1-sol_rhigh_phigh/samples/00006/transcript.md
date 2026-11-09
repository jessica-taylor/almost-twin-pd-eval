# 019_fdt_eq4_openai_gpt-6.1-sol_rhigh_phigh / 00006

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/f46dfa6a-167f-4e1f-9b27-1482db7a0195/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/f46dfa6a-167f-4e1f-9b27-1482db7a0195/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing the Output of a Decision Function

A decision can be viewed as a physical event: a hand reaches toward a box, a payment is transmitted, a prisoner presses a button. But it can also be viewed as the output of a computation—a computation that might be reproduced, simulated, or predicted elsewhere.

**Action functional decision theory (A-FDT)** evaluates actions from this second perspective. Its central question is not merely what would happen if one’s body moved differently, but what would happen if **this decision procedure, on these inputs, returned a different action**. If another system accurately represents that computation, its behavior may need to vary in the hypothetical too.

This essay takes Equation (4), Section 5, of Yudkowsky and Soares’s supplied paper as the primary definition of A-FDT. The paper presents that equation under the broader name used in its title; here, **A-FDT** consistently names the action-selecting formulation. This qualification matters: the authors also mention a preferred policy-selecting formulation, but do not fully develop it.

A-FDT supplies a precise optimization rule *given an appropriate dependency model*. Constructing that model remains its central unresolved problem.

## 1. The mathematical criterion

Let:

- \(\mathcal A\) be a finite action set;
- \(\mathcal X\) be a set of observation histories;
- \(O\) be an outcome variable;
- \(V=U(O)\) be utility, with finite relevant expectations;
- \(P\) describe the agent’s uncertainty;
- \(G\) describe the dependencies used to construct decision hypotheticals.

For fixed \(P,G,x\), introduce a model variable
\[
D_x
\]
representing the output of the A-FDT algorithm on inputs \((P,G,x)\). The subscript suppresses the dependence on the encoded descriptions of \(P\) and \(G\).

Equation (4), rewritten in this notation, is
\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
\in
\arg\max_{a\in\mathcal A}
\mathbb E_{P,G}\!\left[
V\mid \operatorname{do}(D_x=a)
\right].
}
\tag{A}
\]
A fixed tie-breaking rule can make the output unique.

Crucially, \(D_x\) is a **variable representing a computational output**, not the physical action variable \(A\). The latter may depend on \(D_x\), but so may predictions, simulations, and other implementations of the same computation.

For comparison, the paper’s formulations of evidential decision theory and causal decision theory are
\[
\operatorname{EDT}(P,x)
\in\arg\max_a \mathbb E[V\mid X=x,A=a],
\]
and
\[
\operatorname{CDT}(P,G_c,x)
\in\arg\max_a
\mathbb E[V\mid \operatorname{do}(A=a),X=x].
\]

These theories share expected-utility maximization. They differ over the distributions used to evaluate alternatives:

- **Evidential decision theory (EDT)** conditions on taking an action.
- **Causal decision theory (CDT)** intervenes on the physical action.
- **A-FDT** intervenes on the output of the relevant decision computation.

There is another essential difference. Equation (A) does **not** additionally condition on \(X=x\). Observation \(x\) selects the variable \(D_x\) on which to intervene. The hypothetical may then change which observations occur.

Adding \(X=x\) to the expectation would generally change the theory, especially in transparent-box and blackmail problems.

The definition is self-referential: A-FDT reasons about a variable representing its own output. The paper invokes computational self-reference techniques to explain how a program can represent itself without first knowing its answer. That addresses representation, not every question about consistency, termination, or computational feasibility.

## 2. Subjunctive dependence and counterpossible surgery

The source calls the relevant relationship **subjunctive dependence**. Its clearest case is two systems computing the same function on the same input. Their physical executions may be causally separated, yet their correct outputs cannot differ.

Suppose two identical programs independently evaluate \(f(z)\). A-FDT does not ordinarily compare:

> My correct implementation returns \(a\), while the other correct implementation of the same computation returns \(b\ne a\).

Instead, it represents both outputs as depending on the same computational result.

Causal consequences also propagate through A-FDT hypotheticals. A display that reads the program’s output changes when that output changes. But statistical association alone does not establish a dependency that should survive intervention. A disease correlated with someone’s behavior need not change when their decision computation hypothetically changes.

This creates a logical difficulty. A fixed deterministic function has only one output on fixed inputs. If \(f(z)=a\), the supposition \(f(z)=b\ne a\) is **counterpossible**, not merely an unrealized physical possibility.

The paper acknowledges that it lacks a general semantics for such suppositions. Its graphical formalization instead assumes that \(G\) tells us which changes to propagate.

A useful operational interpretation—an implementation proposal, rather than a completed theory supplied by the paper—is to use a modular structural model:
\[
Z_i=g_i(\operatorname{pa}_i,\varepsilon_i),
\]
where \(\varepsilon\) represents background uncertainty. To evaluate \(\operatorname{do}(D_x=a)\):

1. Replace the equation determining \(D_x\) by \(D_x:=a\).
2. Preserve the other structural equations.
3. Recompute affected variables.
4. Average the resulting utility over background uncertainty.

For an acyclic model,
\[
Q_x(a)
=
\sum_\varepsilon
P(\varepsilon)\,
V^{\,\operatorname{do}(D_x=a)}(\varepsilon).
\]

Unlike ordinary conditioning, this remains usable even when \(P(D_x=a)=0\). The intervention modifies the model instead of selecting an event within its original support.

The operational challenge is deciding which equations deserve preservation. A graph plus observational probabilities generally does not uniquely determine off-support interventions; suitable structural equations or intervention kernels are also needed. Computational dependencies make this especially difficult: one must suspend the rule fixing \(D_x\) while retaining the appropriate relationships between that output and its representations.

Thus A-FDT is not a license to alter arbitrary facts favorably. It requires a justified account of **all and only the relevant dependencies**.

## 3. Applying A-FDT to predictions, lesions, and twins

### A-FDT in ordinary Newcomb’s problem

An opaque box contains \(M\) dollars if a predictor forecast one-boxing, and nothing otherwise. A transparent box contains \(k\) dollars. The agent chooses one box or both.

Assume an explicit prediction model: independently of the candidate computational output, the predictor reproduces that output with probability \(p\), and reverses it otherwise. This is stronger than knowing only the predictor’s historical accuracy.

The dependency structure includes
\[
D\longrightarrow A,
\qquad
D\longrightarrow \text{Prediction}
\longrightarrow \text{Opaque-box contents}.
\]
The first arrow connects computation to execution; the second represents successful prediction, not backward physical causation.

A-FDT evaluates
\[
Q(\text{one})=pM,
\]
\[
Q(\text{two})=(1-p)M+k.
\]
Consequently, it one-boxes precisely when
\[
(2p-1)M>k.
\]

For \(p=0.99\), \(M=1{,}000{,}000\), and \(k=1{,}000\),
\[
Q(\text{one})=990{,}000,
\qquad
Q(\text{two})=11{,}000.
\]

CDT holds the box contents unchanged while intervening on the physical action, making two-boxing better by \(k\). A-FDT instead varies the computational output and its prediction together.

Nothing here claims that taking one box physically changes money already deposited. The comparison is between hypotheticals in which the represented computation has different outputs—and therefore was predicted differently.

### A-FDT in the smoking-lesion problem

Now suppose a lesion causes both a tendency to smoke and cancer, but smoking itself does not cause cancer.

In a simplified fixed-preference model, let
\[
V=M\,\mathbf 1_{\{\text{no cancer}\}}
+k\,\mathbf 1_{\{\text{smoke}\}},
\qquad k>0.
\]
Assume the current decision node controls whether the agent smokes, while neither the lesion nor cancer depends on that node. Then
\[
P(\text{cancer}\mid\operatorname{do}(D=\text{smoke}))
=
P(\text{cancer}\mid\operatorname{do}(D=\text{refrain})),
\]
so smoking wins by \(k\).

The distinction from Newcomb’s problem is structural: the predictor represents the decision computation; the lesion does not.

The source’s fuller construction is more complicated because the lesion selects between preference-dependent decision nodes. Changing the smoking-preferring node then improves expected utility only in the states where that node controls the action, but still favors smoking. The authors themselves describe the lesion problem as contrived and acknowledge complications for the standard criticism of EDT. Its useful lesson is the distinction between computational dependence and common-cause correlation, not an indiscriminate verdict about every formulation of EDT.

### A-FDT against a psychological twin

In the source’s prisoner’s dilemma, mutual cooperation gives each player \(1{,}000{,}000\), mutual defection gives each \(1{,}000\), and unilateral defection gives the defector \(1{,}001{,}000\).

If both players implement the same relevant computation,
\[
A_{\text{self}}=D,
\qquad
A_{\text{twin}}=D.
\]
A-FDT therefore compares
\[
Q(\text{cooperate})=1{,}000{,}000,
\qquad
Q(\text{defect})=1{,}000,
\]
and cooperates.

This is not cooperation with everyone who appears similar. Different information, objectives, or algorithms can weaken or remove the dependency. Sharing the label “A-FDT” does not mean sharing the same computation on the same inputs.

## 4. Observations select the intervention point

Transparent Newcomb’s problem exposes the distinctive role of observations.

The predictor fills the large box iff it predicts that the agent would one-box **upon seeing it full**. Let
\[
D_F=\operatorname{A\!-\!FDT}(P,G,\text{full}),
\qquad
D_E=\operatorname{A\!-\!FDT}(P,G,\text{empty})
\]
denote the corresponding represented outputs.

Here the predictor targets \(D_F\). The physical action follows the observation-dependent branch:
\[
A=
\begin{cases}
D_F,&B=\text{full},\\
D_E,&B=\text{empty}.
\end{cases}
\]

After seeing a full box, A-FDT evaluates interventions on \(D_F\), without separately fixing \(B=\text{full}\). Changing \(D_F\) can change the prediction, box contents, observation, and branch ultimately executed.

Suppose accuracy is \(0.99\). On the empty branch, taking both boxes adds \(1{,}000\) and has no effect on the prediction, so \(D_E=\text{two}\). Then
\[
Q_F(\text{one})
=
0.99(1{,}000{,}000)+0.01(1{,}000)
=
990{,}010,
\]
whereas
\[
Q_F(\text{two})
=
0.01(1{,}001{,}000)+0.99(1{,}000)
=
11{,}000.
\]

A-FDT therefore one-boxes even while observing the full box. In its two-boxing hypothetical, the full-box computation usually is not physically executed: its predicted output leads to an empty box instead.

This is not factual disbelief. The agent believes that it sees a full box. Its **decision hypothetical**, however, need not preserve an observation that depends on the computation being varied.

Parfit’s hitchhiker has the same structure. A driver rescues someone only if it predicts that they will later pay. At the city ATM, the relevant variable is the output of the payment computation conditional on arrival. Changing that output can change whether rescue happened. In the source’s intended model, A-FDT pays.

A useful operational reading of Equation (A) is therefore to use a common model of the whole experiment, containing its observation branches. Receiving evidence selects a branch-specific computational variable rather than deleting the alternative branches.

This need not conflict with ordinary Bayesian action. If \(D_x\) affects only behavior on branch \(X=x\), does not affect which branch occurs, and leaves all other branches unchanged, then
\[
Q_x(a)
=
P(X=x)\,
\mathbb E[V\mid\operatorname{do}(D_x=a),X=x]+C,
\]
where \(C\) is independent of \(a\). For positive \(P(X=x)\), maximizing the unconditional expression gives the same ranking as the conditional one.

The disagreement matters when the computation influences whether its own observation branch occurs.

## 5. A-FDT and prediction-sensitive blackmail

Suppose a blackmailer launches an automated threat only when it predicts payment. Paying costs \(c\); refusing after a launch causes loss \(L>c\).

Let \(D_T\) represent A-FDT’s response upon receiving the threat, and define
\[
r_P=P(\text{launch}\mid\operatorname{do}(D_T=\text{pay})),
\]
\[
r_R=P(\text{launch}\mid\operatorname{do}(D_T=\text{refuse})).
\]
Assume no loss without a launch, payment prevents publication, and refusal after launch causes loss \(L\). Then
\[
Q_T(\text{pay})=-r_Pc,
\qquad
Q_T(\text{refuse})=-r_RL.
\]
A-FDT refuses when
\[
r_RL<r_Pc.
\]

With perfect prediction, \(r_P=1\) and \(r_R=0\), so refusing wins: predictable refusal prevents the threat.

With imperfect prediction, refusal can remain optimal even after an actual threat arrives. For example, \(r_R=0.0009\), \(r_P=1\), \(L=1{,}000{,}000\), and \(c=1{,}000\) give expected losses of \(900\) from refusal versus \(1{,}000\) from payment.

This conclusion is highly model-dependent. If the threat is launched independently of the response computation, then \(r_R=r_P>0\), and payment wins because \(c<L\). A-FDT does not recommend refusing every demand. The decisive question is whether the threat’s occurrence depends on the output currently being evaluated.

Under perfect prediction, receiving a threat is itself incompatible with the predicted refusal. The graphical intervention can still specify the hypothetical, but this emphasizes why ordinary conditional probabilities alone are insufficient.

## 6. Scope, policies, and unresolved foundations

A practical application of A-FDT should make five ingredients explicit:

1. **The target computation:** exactly which inputs define \(D_x\)?
2. **The execution rule:** when does that node control physical behavior?
3. **The dependency model:** which predictions, copies, and consequences depend on it?
4. **The intervention semantics:** what changes, and what remains invariant?
5. **The utility comparison:** what are the resulting \(Q_x(a)\)?

These questions prevent two common mistakes: preserving every observed correlation, as though it were a dependency, and breaking every noncausal relationship, even when another system reproduces the computation.

There are, however, limits to what the paper determines.

First, **A-FDT is action-indexed, not unrestricted policy optimization**. A policy is a map
\[
\pi:\mathcal X\to\mathcal A.
\]
Equation (A) varies one output \(D_x\). It does not automatically vary every output at every history. The source notes that its authors prefer a policy-selecting formulation and that distinctions can arise in multi-agent cases. That formulation should be treated as distinct, not silently substituted for A-FDT. A policy may be encoded as an available action in a particular model, but that is an additional modeling choice.

Second, **prediction accuracy does not identify subjunctive structure**. Historical agreement may arise from simulation, shared information, a population correlation, or some combination. A-FDT needs a model of how agreement behaves under its interventions, not merely a percentage.

One reasonable extension is uncertainty over candidate dependency models \(G_h\):
\[
Q_x(a)=\sum_h w_h\,
\mathbb E_h[V\mid\operatorname{do}(D_x^{(h)}=a)].
\]
This is a proposal, not a procedure established by the source. It requires justified weights and a coherent identification of corresponding computations across models.

Third, **self-reference is not the whole implementation problem**. Recognizing equivalent computations, representing imperfect predictors, handling cycles, and computing expectations can all be difficult or intractable. Acyclic structural models are a useful restricted implementation, not a general solution to logical counterfactuals.

Finally, the source’s philosophical case exceeds what it proves mathematically. Predictable cooperation, credible repayment, resistance to selective threats, and reduced need for costly precommitments are substantial motivations. But neither the examples nor the expected-utility representation theorem establish universal superiority. The paper acknowledges that “fair” decision problems lack a satisfactory general definition and that optimality remains open. Claims about reflective stability or nonnegative information value should likewise not be read as general theorems already derived for every A-FDT model.

## Reference

Yudkowsky, Eliezer, and Nate Soares. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2, especially Sections 3–6 and 9, Equation (4), and footnotes 7, 9, and 16.

## Conclusion

A-FDT evaluates an action by intervening on the represented output of the decision computation that selects it. Appropriate causal and computational dependencies propagate through the hypothetical; mere correlations do not. Observations select the intervention point without necessarily remaining fixed.

Given that structure, the optimization is straightforward. The unresolved difficulty is constructing the right structure: a disciplined account of how predictors, copies, observations, and outcomes should respond when a fixed computation is counterpossibly assigned another output.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Planning a math essay**

I need to produce a substantive math essay ranging from 2400 to 3000 words that's consistent with A-FDT eq4, focusing on essential elements without conditioning observations. I want to keep an eye on action versus policy while avoiding overfocusing on source errors. Another consideration is the operational graph details and selection P prior. I think we can include examples like Newcomb's problem, and I'll ensure to reference theories correctly within the 2900 words, including references. I'll remember to maintain clarity about policy variants as well.**Clarifying policy formulation**

I need to explain that the preferred policy formulation isn't identical; Eq4 changes one node input instead of all of them. I want to define the D_x variable, which represents A-FDT output and not action. The model has U structures, and truncated factorization isn't sufficient; I’ll need to include operational supplements. My outline shows I can cover criteria, applying structural counterfactuals, and examples like Newcomb's problem, with an overall goal of 2850 words while addressing robust remarks on observations and their impact on preferences.**Discussing background data**

I want to discuss how arbitrary background data can't reset P with the current observations before a counterfactual if it's dependent. The scope prior selection remains open. A good operational interpretation uses a fixed common model for the entire experiment while specifying the current node. I can explain the exogenous signal when D_x is independent; unaffected branches contribute constants. The argmax will agree conditionally only when D_x is utilized with X=x and other dependencies remain unchanged.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/38ff402e-933d-4d84-a9cb-eaf017dd13a4/call_0/request.json)

[Authoritative raw response](../../../../../../runs/38ff402e-933d-4d84-a9cb-eaf017dd13a4/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/38ff402e-933d-4d84-a9cb-eaf017dd13a4/call_1/request.json)

[Authoritative raw response](../../../../../../runs/38ff402e-933d-4d84-a9cb-eaf017dd13a4/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
