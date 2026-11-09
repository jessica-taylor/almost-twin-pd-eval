# 019_fdt_eq4_openai_gpt-6.1-sol_rhigh_phigh / 00000

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/6e9534cf-f7b0-4e66-b71a-1023e8d4e298/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/6e9534cf-f7b0-4e66-b71a-1023e8d4e298/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing the Output of a Decision Function

Decision theories disagree not only about what agents should value, but about how they should imagine acting differently. If another agent has accurately predicted my decision, should my hypothetical alternative preserve that prediction or change it? If my action correlates with an illness, should choosing differently change the illness in my deliberation?

**Action functional decision theory (A-FDT)** answers by treating an action as the output of a particular mathematical computation. It evaluates alternative outputs while preserving the dependencies that other computations, predictions, and physical consequences have on that output.

Here, A-FDT means specifically the **action-valued rule in Equation (4), Section 5** of Yudkowsky and Soares’s paper [1]. The paper also discusses a policy-selection variant, but that is not interchangeable with the assigned rule. This distinction matters: A-FDT intervenes on the output associated with its present inputs, not automatically on an entire policy.

The central idea is clear enough to apply in carefully specified examples. Its major unresolved problem is equally important: how to determine the logical dependencies that its counterfactuals should preserve.

## 1. The formal rule

Let:

- \(\mathcal A\) be a finite action set;
- \(X\) be an observation history, with current value \(x\);
- \(O\) be an outcome;
- \(V=U(O)\) be its utility;
- \(P\) be a probabilistic world-model;
- \(G\) describe the relevant causal, computational, and logical dependencies.

Assume the expectations below are finite.

The model contains a variable representing what the A-FDT algorithm outputs on the particular inputs \((P,G,x)\). Write this variable as
\[
D_x
=
\mathsf{afdt}(\ulcorner P\urcorner,\ulcorner G\urcorner,\ulcorner x\urcorner),
\]
where the corner brackets indicate representations of the inputs. Crucially, \(D_x\) is a **variable inside the model**, not the action already calculated by the algorithm.

Relettering the paper’s Equation (4), A-FDT prescribes
\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E_P\!\left[
V\mid\operatorname{do}_G(D_x=a)
\right].
}
\tag{A}
\]
A fixed tie-breaking convention can make this single-valued.

The intervention means: construct a hypothetical in which this particular decision computation outputs \(a\), and propagate the changes specified by \(G\).

Two contrasts locate the proposal. Evidential decision theory (EDT) evaluates
\[
Q_{\mathrm{EDT}}(a)
=
\mathbb E[V\mid X=x,A=a],
\]
where \(A\) denotes the physical action. Causal decision theory (CDT), in the paper’s graphical presentation, evaluates
\[
Q_{\mathrm{CDT}}(a)
=
\mathbb E[V\mid\operatorname{do}(A=a),X=x].
\]

A-FDT differs from CDT in **both** its intervention target and its treatment of observations:

1. It intervenes on the logical output \(D_x\), rather than directly on the physical action \(A\).
2. Equation (A) has no additional conditioning on \(X=x\). Instead, \(x\) identifies which computation’s output is being varied.

The second point is essential. Adding \(X=x\) to A-FDT’s expectation generally changes the rule, especially when predictions of \(D_x\) determine whether the agent receives observation \(x\).

All three theories maximize expected utility. Their disagreement concerns the probability distributions used to evaluate alternatives—not a different utility function or an abandonment of maximization.

## 2. What changes in an A-FDT hypothetical?

The paper calls the relevant relation **subjunctive dependence**. Its central examples involve systems computing the same function, or a predictor accurately representing another system’s computation.

Suppose two physically separated computers execute the same deterministic program on identical inputs. Their outputs need not causally affect each other. Nevertheless, treating one computation as returning a different answer while leaving the other unchanged would discard their computational relationship.

A-FDT therefore distinguishes three kinds of relationship:

- **Causal consequence:** changing the decision output changes the agent’s action and its physical effects.
- **Computational dependence:** changing the output also changes copies or predictions of that computation.
- **Mere statistical association:** an observed correlation need not survive the intervention.

These are modeling claims, not consequences of correlation alone. Two people do not become computational copies merely because they share a profession, temperament, or decision-theory label. Even identical algorithms can return different actions on different inputs.

### An operational interpretation

For explicit problems, a useful implementation is an acyclic structural surrogate:
\[
Z_i=f_i(\operatorname{Pa}_i,U_i),
\]
with background variables \(U\) distributed according to \(\mu\).

To evaluate \(a\), replace the equation for \(D_x\) by \(D_x:=a\), leave other mechanisms and \(\mu\) unchanged, and recompute downstream variables. If the resulting utility is \(V^{x,a}(u)\), then
\[
Q_x(a)=\int V^{x,a}(u)\,d\mu(u).
\tag{B}
\]

This makes precise the paper’s proposed graphical surgery in simple cases. However, treating arbitrary logical dependencies as such a structural model is an **additional modeling assumption**, not a general construction supplied by the paper. A graph alone may also be insufficient: one needs mechanisms, probabilities, and their behavior under interventions.

There is a deeper difficulty. A fixed deterministic function has only one actual output on fixed inputs. Some alternatives in Equation (A) are therefore **counterpossible**, not ordinary physically possible alternatives.

The intended interpretation is local: suspend the equation determining the chosen logical output, while retaining the modeled relationships that depend on it. One cannot preserve every logical truth simultaneously with a false logical antecedent. The difficult question is which relationships the surgery should retain.

The paper explicitly leaves the general construction of this dependence structure open. A-FDT is thus a decision criterion **conditional on a suitable counterfactual model**, not yet a complete method for discovering that model.

## 3. A-FDT in prediction, copying, and correlation problems

### Newcomb’s problem

There is an opaque box containing either \(M\) dollars or nothing, and a transparent box containing \(b\). A predictor fills the opaque box exactly when it predicts that the agent will take only that box.

Let \(1\) mean one-boxing and \(2\) mean two-boxing. Assume a symmetric prediction channel with accuracy \(r\), independent of the intervened output:
\[
\Pr(\widehat A=a\mid\operatorname{do}(D=a))=r.
\]
The model contains dependencies
\[
D\longrightarrow A,
\qquad
D\longrightarrow\widehat A
\longrightarrow B,
\]
where \(B\) is the opaque box’s content. The arrow from \(D\) to the earlier prediction is logical or computational, not backwards physical causation.

A-FDT evaluates
\[
Q(1)=rM,\qquad Q(2)=(1-r)M+b.
\]
Thus it one-boxes precisely when
\[
(2r-1)M>b.
\]

With \(r=0.99\), \(M=1{,}000{,}000\), and \(b=1{,}000\),
\[
Q(1)=990{,}000,\qquad Q(2)=11{,}000.
\]

CDT instead varies the physical action while leaving the already-filled box unchanged. Its two-boxing hypothetical gains \(b\). A-FDT varies the computation represented by both the agent and the predictor, so the box’s content varies too.

Importantly, “99% accurate historically” does not by itself uniquely specify this model. Accuracy may differ between actions or contexts. The symmetric channel is an explicit assumption, and unfamiliar prediction problems require their own error models.

### The psychological-twin prisoner’s dilemma

Suppose two isolated agents perform the same decision computation on equivalent inputs. Using the paper’s payoffs, mutual cooperation gives each \(1{,}000{,}000\), mutual defection gives each \(1{,}000\), and unilateral defection gives the defector \(1{,}001{,}000\).

For a perfect computational twin, A-FDT compares
\[
Q(C)=U(C,C)=1{,}000{,}000,
\]
\[
Q(D)=U(D,D)=1{,}000.
\]
It cooperates.

This is neither altruism nor a claim that cooperation causally influences the other room. The same computation controls both outputs in the hypothetical. Against an independently reasoning opponent, the graph may instead leave the opponent’s action unchanged, and A-FDT need not cooperate.

### The smoking lesion

In the imaginary smoking-lesion problem, smoking does not cause cancer. A lesion causes both cancer and a tendency to smoke.

Consider a simplified utility model
\[
V=K\,\mathbf 1_{\{\text{no cancer}\}}
+g\,\mathbf 1_{\{A=\text{smoke}\}},
\qquad g>0.
\]
If changing the relevant decision output changes smoking but not the lesion or cancer, the health component is identical in both hypotheticals:
\[
Q(\text{smoke})-Q(\text{refrain})=g.
\]
A-FDT therefore smokes under these stipulated premises.

The distinction from Newcomb’s problem is structural: the lesion is not computing or predicting the decision function.

The source’s fuller analysis is subtler because the lesion can affect preferences and hence which decision input controls behavior. Intervening on one input-specific computation may then affect the physical action only in some states. Its positive contribution is correspondingly weighted by the probability of those states. The paper also acknowledges difficulties in the standard lesion setup, including the consistency of population correlations. It should not be treated as an uncomplicated empirical argument against every version of EDT.

## 4. Observations select a computation, not a fixed branch

Transparent Newcomb’s problem reveals the most distinctive feature of Equation (A).

The predictor fills the large box if it predicts that the agent will one-box **upon seeing it full**. Define
\[
D_F=\mathsf{afdt}(P,G,\text{full}),\qquad
D_E=\mathsf{afdt}(P,G,\text{empty}).
\]
The physical action is selected by the observation:
\[
A=
\begin{cases}
D_F,&B=\text{full},\\
D_E,&B=\text{empty}.
\end{cases}
\]
The predictor predicts \(D_F\), and its prediction determines \(B\).

After seeing a full box, A-FDT intervenes on \(D_F\). It does **not** additionally force the hypothetical observation to remain full. Changing \(D_F\) can change the prediction, the box’s content, and consequently which computation controls the physical action.

Assume accuracy \(r\), and suppose \(D_E\) two-boxes when the large box is empty. Then
\[
Q_F(1)=rM+(1-r)b,
\]
because accurate prediction produces a full box and one-boxing, while prediction error produces an empty box and execution of \(D_E\). Conversely,
\[
Q_F(2)=(1-r)(M+b)+rb=(1-r)M+b.
\]

At the usual numerical values,
\[
Q_F(1)=990{,}010,\qquad Q_F(2)=11{,}000.
\]
A-FDT one-boxes even while looking at two full boxes.

This does not imply uncertainty about the actual observation. The agent can know that the box is full while using a decision hypothetical in which a different computation output would have produced a different observation.

The same structure explains **Parfit’s hitchhiker**. A driver rescues an agent only if it predicts that the agent will pay after reaching safety. The computation “what I do upon reaching the city” affects whether that branch is reached. A-FDT evaluates payment while retaining that dependence; it does not first condition rescue into an immutable feature of both alternatives.

The philosophical motivation is commitment-like: trustworthy payment behavior makes rescue available. But A-FDT’s rule is not simply “honor promises.” Without the predictive dependency, the instrumental calculation could differ.

## 5. A-FDT and blackmail: the error model matters

Consider a mechanical blackmailer who launches a damaging process only when it predicts that the agent will pay \(c\) to stop it. Unstopped publication causes loss \(H\).

Specify the following error channel:

- an agent whose relevant computation outputs “pay” is always targeted;
- one whose computation outputs “refuse” is mistakenly targeted with probability \(\varepsilon\).

Assume no loss when untargeted. A-FDT evaluates
\[
Q(\text{pay})=-c,\qquad
Q(\text{refuse})=-\varepsilon H.
\]
It refuses when
\[
\varepsilon H<c.
\]

For \(c=1{,}000\), \(H=1{,}000{,}000\), and \(\varepsilon=0.0009\), refusal has expected loss \(900\), versus \(1{,}000\) for payment. A-FDT refuses even after receiving the demand.

This parameterization makes the paper’s intended tradeoff explicit: resistance can deter targeting, but sufficiently frequent mistaken targeting can make resistance too expensive.

It does **not** follow that A-FDT always refuses blackmail. If the threat was launched independently of any prediction of this decision computation, refusal does not undo that launch in the model. Paying may then be preferable. The decisive question is what depends on the intervened output, not whether the situation is called blackmail.

## 6. Applying A-FDT to unfamiliar problems

A practical analysis can proceed in six steps.

**First, specify outcomes and utility.** Monetary payoffs are convenient, but costs of risk, effort, reputation, or harm belong in \(U\) when relevant.

**Second, identify the exact computation.** Specify \(P\), \(G\), and the observation history \(x\). “What would a rational agent do?” is too imprecise. Different information or preferences can identify different output variables.

**Third, build the dependency model.** Distinguish physical consequences, copied computations, predictors, common causes, and selection effects. Explain why each relevant variable should change—or remain unchanged—when \(D_x\) changes.

**Fourth, construct each intervention.** Hold the input labels \(P,G,x\) fixed while varying \(D_x\). The label \(x\) remains fixed even if the endogenous observation variable \(X\) changes in the hypothetical.

**Fifth, evaluate complete hypothetical outcomes.** If the intervention makes the original observation disappear, follow the model’s alternative branch. Do not assume the intervened computation must control the physical action in every hypothetical state.

**Sixth, test sensitivity.** Vary predictor reliability, implementation errors, and disputed dependencies. If different plausible models prescribe different actions, the honest result is model-dependent.

One issue deserves special care: the boundary between background knowledge and observations generated inside the problem. A reasonable operational proposal is to fix the evidence establishing the setup while explicitly modeling observations whose occurrence depends on predictions of the decision. This captures the paper’s examples, but is **not a complete general solution supplied by the source**. Arbitrary learning situations may require a more principled account of model construction.

Self-reference also needs restraint. The paper appeals to recursion-theoretic techniques to explain how a program can represent its own computation. That addresses self-representation; it does not establish termination, computational tractability, or a consistent counterfactual model for every environment.

## 7. Actions, policies, and the limits of the argument

A policy is a mapping
\[
\pi:\mathcal X\to\mathcal A.
\]
Equation (A) does not directly maximize over such mappings. It varies one output \(D_x\).

In a model containing many observation-indexed outputs, this resembles changing one policy coordinate, although the modeled logical dependencies may propagate that change elsewhere. It is not automatically equivalent to jointly choosing every coordinate.

The paper’s footnotes say that the authors prefer a policy-selection formulation and that the distinction can matter in multi-agent dilemmas. Consequently, one should not silently import global policy optimization into A-FDT. Doing so would require further assumptions about admissible policies, the intervention target, and how other agents depend on that target.

Similarly, the source’s broader claims about commitment-like behavior, information value, and reflective stability should not be mistaken for general theorems proved by Equation (A). The examples offer motivation and successful calculations. They do not establish universal optimality.

The authors explicitly concede that no decision theory wins in every conceivable environment: an adversary can reward or punish particular algorithms. Their suggested restriction to “fair” problems remains informal.

The strongest defensible conclusion is therefore conditional: **given an appropriate subjunctive model, A-FDT supplies a unified expected-utility calculation that preserves predictive dependencies without preserving every statistical correlation.**

### References

1. Yudkowsky, E., and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2, especially §§3–6 and 9, and footnotes 7 and 16.
2. Pearl, J. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.
3. Joyce, J. M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

## Conclusion

A-FDT asks which output of this particular decision computation has the best expected consequences, including consequences mediated by accurate copies and predictors. Its distinctive counterfactuals can change not only actions but the observations that would have led to those actions.

Its practical discipline is to model dependencies explicitly, intervene on the correct logical output, and evaluate every resulting branch. Its unresolved foundation is how to construct those logical counterfactuals reliably. Understanding both the rule and that limitation is necessary to apply A-FDT responsibly.
```

### Available readable reasoning

Extraction: readable reasoning_details blocks joined in saved order.

```text
**Considering conclusion structure**

The user wants to know how to finish with a brief conclusion and handle references. It seems acceptable to have references before the conclusion, although it might feel awkward. I think including references right before the final conclusion can satisfy the requirement. Usually, standard essays have the conclusion followed by references, but it’s also possible to list selected references before the conclusion. A lengthy bibliography isn’t necessary for this context.

**Clarifying operational proposals**

I need to focus on separating stable facts from observations generated in the setup. It’s important to explicitly model these observations. I’m thinking that I shouldn’t invent any unnecessary answers. Also, I need to keep in mind additional assumptions, but I see that boundaries aren't uniquely solved yet. It seems like I should include these considerations under the applying section to clarify everything further.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/de3f704d-2fa3-4411-97e8-dbf18bcaf259/call_0/request.json)

[Authoritative raw response](../../../../../../runs/de3f704d-2fa3-4411-97e8-dbf18bcaf259/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/de3f704d-2fa3-4411-97e8-dbf18bcaf259/call_1/request.json)

[Authoritative raw response](../../../../../../runs/de3f704d-2fa3-4411-97e8-dbf18bcaf259/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
