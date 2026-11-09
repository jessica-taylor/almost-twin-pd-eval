# 019_fdt_eq4_openai_gpt-6.1-sol_rhigh_phigh / 00017

Status: **complete**. Saved outcome: **DC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/5499d3fd-d616-4282-80a9-d503ea66ce3f/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/5499d3fd-d616-4282-80a9-d503ea66ce3f/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing the Output of a Decision Procedure

A decision can matter even when its physical consequences do not explain everything correlated with it. A predictor may already have forecast the decision; another agent may be running the same computation; a simulated copy may determine whether an offer is made. In such situations, evaluating an action requires deciding which dependencies to preserve when asking what would happen otherwise.

**Action functional decision theory (A-FDT)** evaluates actions by intervening on a representation of the output of the agent’s decision procedure. Its central question is not merely what a different bodily movement would cause, nor what that movement would reveal. It asks which output of this very computation corresponds to the best outcome, allowing relevant predictions and computational copies to vary with that output.

Here A-FDT denotes specifically the action-valued rule in Equation (4), Section 5, of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality*. The paper also mentions a policy-valued alternative. That distinction matters: an action-level intervention should not silently become optimization over every possible policy.

## 1. Expected utility needs a theory of hypotheticals

Let \(\mathcal A\) be a finite action set, \(O\) an outcome variable, and \(U(O)\) utility. Expected-utility decision theories evaluate each action using some distribution over hypothetical outcomes:

\[
Q(a)=\sum_o P_a(O=o)\,U(o).
\]

They disagree about how to construct \(P_a\).

**Evidential decision theory (EDT)** uses ordinary conditioning:

\[
Q_{\mathrm{EDT}}(a;x)
=
\mathbb E[U(O)\mid X=x,A=a].
\]

It asks what would be good news to learn one had done. Correlations between action and outcome therefore matter even when action does not produce the correlated benefit.

**Causal decision theory (CDT)** instead uses a causal intervention:

\[
Q_{\mathrm{CDT}}(a;x)
=
\mathbb E[U(O)\mid \operatorname{do}(A=a),X=x].
\]

It asks what would result from changing the physical action while preserving the relevant causal background.

A-FDT also uses intervention, but targets a different variable. Rather than replacing the physical action directly, it replaces the represented answer to the computation that selects the action. A predictor’s forecast or a twin’s decision can then change even without a causal arrow from the agent’s present movement to those events.

The disagreement concerns the appropriate hypothetical, not the utility function. Expected-utility axioms alone do not settle it: they tell us how to aggregate outcomes once the hypothetical distributions have been supplied.

## 2. The formal rule

Write \(M=(P,G)\) for the agent’s world-model. Here:

- \(P\) represents uncertainty about outcomes, observations, physical events, and computational outputs;
- \(G\) describes relevant causal and broader computational dependencies;
- \(x\) is the agent’s observation history;
- \(D_{M,x}\) is a variable representing the output of A-FDT on inputs \(M,x\).

In simplified notation, the paper’s Equation (4) becomes

\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E_{P,G}\!\left[
U(O)\mid \operatorname{do}(D_{M,x}=a)
\right].
}
\tag{A}
\]

Fixing a deterministic tie-breaking convention makes the rule action-valued.

The distinction between the variable \(D_{M,x}\) and the actual output is essential. The former is an object inside the model, manipulated during deliberation. The latter is the action obtained after comparing the resulting expectations.

There is self-reference: the model contains a variable representing the result of evaluating a procedure on that model. The authors appeal to computational self-reference techniques to explain how such representations can exist. But representing one’s computation is not the same as knowing its answer, and self-reference techniques do not by themselves solve the counterfactual problem.

### What the intervention does

Suppose \(G\) says that both the physical action \(A\) and a predictor’s forecast \(R\) depend on \(D_{M,x}\). Intervening to set \(D_{M,x}=a\) then changes both variables according to their specified dependencies. A disease unrelated to that computation remains unchanged.

The intervention is not ordinary conditioning on the event \(D_{M,x}=a\). Even if the agent is certain its computation will choose \(a_1\), it must still evaluate the hypothetical in which that computation outputs \(a_2\).

Nor does the intervention automatically change every agent using A-FDT. The relevant object is a particular computation with particular inputs. Different observations, models, utilities, or implementations can produce different computations. Any dependence between their outputs requires justification.

### The missing observational conditional

Equation (A) notably lacks a condition \(X=x\) outside the intervention. Observation history instead selects the intervention target:

\[
x\longmapsto D_{M,x}.
\]

After observing \(y\), the agent intervenes on \(D_{M,y}\), not \(D_{M,x}\).

This is not cosmetic. Adding ordinary conditioning on the current observation would generally change the theory. A-FDT can evaluate a hypothetical in which changing the selected computation also changes whether the agent receives its current observation.

## 3. Subjunctive dependence and an operational interpretation

The paper calls the relevant broader relationship **subjunctive dependence**. Two systems implementing the same function on the same input provide its clearest example. Their outputs agree because of computational structure, not necessarily because either system causes the other’s answer.

A prediction can depend on an agent’s computation less than perfectly. Physical consequences of an action also count: ordinary causal dependence is included. Mere statistical association, however, need not survive an intervention.

The unresolved question is how to construct a graph that captures these distinctions. The authors explicitly identify this as a major open problem. Equation (A) provides a decision criterion *given* suitable dependency information, not a complete method for discovering that information.

A useful operational interpretation is available for small, well-specified cases. The following is a modeling proposal, not a general construction proved in the paper.

Represent each relevant variable \(Z_i\) by a structural equation

\[
Z_i=f_i(\operatorname{pa}_i,E_i),
\]

where \(E_i\) represents background uncertainty. To evaluate \(a\):

1. replace the equation for \(D_{M,x}\) by \(D_{M,x}:=a\);
2. preserve the other structural equations and the distribution of background variables;
3. propagate the replacement through the dependency graph;
4. calculate expected utility.

Logical edges here are not physical channels. They encode how representations should co-vary under the proposed computational counterfactual.

This interpretation also exposes why an ordinary joint distribution is insufficient. One distribution may admit several structural explanations with different intervention behavior. A graph plus observational probabilities may likewise leave behavior under interventions underspecified. Explicit equations supply the missing information in the examples below.

There remains a foundational difficulty. A fixed deterministic computation cannot literally have two answers on identical inputs. These are therefore **counterpossible** hypotheticals. Structural replacement makes them calculable by suspending the target computation’s usual equation while retaining selected surrounding relationships. Whether this gives a satisfactory general semantics is unsettled.

## 4. A-FDT in opaque Newcomb’s problem

An opaque box contains either \(M=\$1{,}000{,}000\) or nothing. A transparent box contains \(k=\$1{,}000\). A predictor fills the opaque box when it predicts one-boxing and leaves it empty when it predicts two-boxing.

Let \(D\) represent the decision computation. Assume a symmetric prediction mechanism: independently of which output is imposed, the predictor matches \(D\) with probability \(p\). This is stronger and more useful than merely saying that the predictor has historically been correct \(p\) of the time.

The dependencies are

\[
D\rightarrow A,\qquad
D\rightarrow R\rightarrow B,\qquad
(A,B)\rightarrow U.
\]

The first two arrows need not both be causal.

A-FDT obtains

\[
Q(\text{one box})=pM,
\]

\[
Q(\text{two boxes})=(1-p)M+k.
\]

Thus one-boxing is preferred exactly when

\[
(2p-1)M>k.
\]

At \(p=0.99\), the values are \(\$990{,}000\) and \(\$11{,}000\).

No retrocausation is asserted. The agent does not believe its hand movement sends a signal into the past. It evaluates a computational alternative under which the earlier prediction would usually have differed.

CDT instead holds the box contents fixed across action interventions, making two-boxing worth an additional \(k\). EDT can agree with A-FDT here, but by conditioning on actions rather than preserving a specified prediction mechanism.

## 5. A-FDT distinguishes lesions from copies

### A-FDT and the fictional smoking lesion

In the smoking-lesion problem, a lesion causes both a tendency to smoke and cancer, but smoking itself causes no cancer. Why should A-FDT preserve the Newcomb predictor’s dependence while breaking this association?

Because changing a decision computation’s output does not thereby change the lesion. Cancer has no computational dependence on that output.

The source’s detailed treatment adds an important complication: the lesion changes preferences, so the model includes distinct smoking-preferring and smoking-averse computations. Let their output variables be \(D_S,D_R\), with

\[
A=
\begin{cases}
D_S,&L=1,\\
D_R,&L=0.
\end{cases}
\]

Suppose smoking has utility gain \(g>0\) under the smoking-preferring utility function, and the model assigns probability \(r>0\) to \(L=1\). Changing \(D_S\) from refraining to smoking leaves cancer risk unchanged and increases expected utility by

\[
rg>0.
\]

The smoking-preferring computation therefore outputs smoking.

The lesson is not that correlations never matter, or that real smoking is harmless. It is that an upstream common cause should not change merely because a downstream decision output is hypothetically replaced. The paper itself cautions that the traditional lesion problem becomes contrived when preferences and self-knowledge are fully specified.

### A-FDT and a psychological twin

Suppose two isolated prisoners run the same relevant computation. Mutual cooperation pays each \(\$1{,}000{,}000\); mutual defection pays \(\$1{,}000\). Defecting against a cooperator pays an additional \(\$1{,}000\).

With a shared output variable \(D\), the relevant alternatives are

\[
D=C\implies(A_1,A_2)=(C,C),
\]

\[
D=D_f\implies(A_1,A_2)=(D_f,D_f).
\]

A-FDT cooperates.

This is neither altruism nor unconditional cooperation. Against an opponent whose action is independent of the selected computation, the extra payoff from defection remains. Similarity between agents supports cooperation only insofar as it supports the modeled dependence.

## 6. Observation selects a computation: transparent Newcomb

Transparent Newcomb makes the treatment of observations decisive.

Both boxes are visible. The predictor fills the large box when it predicts that the agent would one-box *upon seeing it full*. Define

\[
D_F=D_{M,\text{full}},
\qquad
D_E=D_{M,\text{empty}}.
\]

The predictor models \(D_F\). The box contents determine which computation controls the physical action:

\[
A=
\begin{cases}
D_F,&B=\text{full},\\
D_E,&B=\text{empty}.
\end{cases}
\]

A-FDT can therefore use an acyclic model:

\[
D_F\rightarrow R\rightarrow B,
\qquad
(D_F,D_E,B)\rightarrow A.
\]

There is no need to encode a physical causal loop between observation and prediction.

Assume the same symmetric prediction accuracy \(p\). On the empty-box branch, two-boxing collects \(k\) without affecting the prediction, so take \(D_E=\text{two boxes}\).

After seeing a full box, A-FDT compares interventions on \(D_F\). If \(D_F\) outputs one-boxing,

\[
Q_F(\text{one box})=pM+(1-p)k.
\]

If it outputs two-boxing,

\[
Q_F(\text{two boxes})
=(1-p)(M+k)+pk
=(1-p)M+k.
\]

At \(p=0.99\), these are \(\$990{,}010\) and \(\$11{,}000\). A-FDT one-boxes.

Why are empty-box outcomes included when the agent can see a full box? Because the comparison does not condition on fullness. It replaces the output of the computation *for seeing fullness*. Changing that output changes the prediction, which changes which observation occurs and which computation becomes physically active.

The agent still believes the actual box is full. Its beliefs about actuality and its decision hypotheticals perform different jobs.

Parfit’s hitchhiker has the same structure. A driver rescues an agent only when predicting that the agent will pay afterward. Let \(D_C\) represent the computation performed upon reaching the city. Replacing its output changes both payment and the predicted willingness that determines rescue. When rescue is sufficiently valuable and prediction sufficiently reliable, A-FDT pays even after arrival.

These results explain the source’s appeal to acting as one would have beneficially precommitted to act. But that slogan is motivation, not a substitute for specifying the graph.

## 7. A-FDT and imperfect blackmail

A blackmailer launches a damaging mechanism only when predicting payment. Paying costs \(c\); refusing after launch incurs loss \(L\).

Let \(D_B\) represent the response computation upon receiving blackmail, and define intervention-sensitive launch probabilities

\[
r_P=P(\text{launch}\mid\operatorname{do}(D_B=\text{pay})),
\]

\[
r_R=P(\text{launch}\mid\operatorname{do}(D_B=\text{refuse})).
\]

Assuming no loss without launch, A-FDT compares

\[
Q(\text{pay})=-cr_P,
\qquad
Q(\text{refuse})=-Lr_R.
\]

It refuses when

\[
Lr_R<cr_P.
\]

For a perfect predictor, \(r_P=1,r_R=0\), so refusal wins. If a refusing agent is mistakenly targeted with probability \(\varepsilon\), while payers are always targeted, refusal wins only when

\[
\varepsilon<\frac cL.
\]

Thus A-FDT is not simply “never pay blackmail.” Its recommendation depends on prediction errors, costs, and the mechanism selecting targets. Nor does this calculation apply to a threat initiated independently of the response computation: the dependency model would then differ.

## 8. Applying A-FDT without assuming too much

For an unfamiliar problem, first specify actions, utility, chance events, and the observation process. Then identify the particular computation selected by the actual history. Ask which predictions, copies, and physical processes depend on its output, and which apparent associations arise only through common causes or selection effects. Finally, construct each intervention and compare expected utilities.

Three boundaries deserve emphasis.

**First, action selection is not unrestricted policy selection.** With \(M\) fixed, the family \(x\mapsto D_{M,x}\) induces a policy. Equation (A), however, intervenes on the output at one observation history. Other outputs change only through specified dependencies. Jointly replacing an entire policy is a different formal operation. The source’s footnotes acknowledge a policy-selection variant, but its stronger properties should not automatically be attributed to A-FDT.

**Second, learning and decision evaluation require careful separation.** Equation (A) does not forbid Bayesian learning. Nevertheless, absorbing the current observation into a posterior and then holding that posterior fixed can erase precisely the selection dependencies used in transparent Newcomb. A reasonable operational convention is to include the relevant observation-generating process in \(M\), keep that model fixed during comparison, and let \(x\) select the output variable. The paper does not provide a complete general architecture for maintaining such models over time.

**Third, performance claims remain conditional.** The paper argues that this approach succeeds across important predictive dilemmas. It does not establish universal superiority. Its proposed distinction between fair problems and problems that reward particular decision procedures remains informal. Likewise, broad claims concerning reflective stability, optimal precommitment, and information value require assumptions beyond the examples alone.

Dependency uncertainty can itself be modeled—for instance, as uncertainty about whether an opponent is an exact copy or an independent agent. But such averaging is an additional modeling proposal, and uncertainty about the correct counterpossible semantics is deeper than ordinary uncertainty about a parameter.

## Conclusion

A-FDT changes the target of deliberation: evaluate alternative outputs of the current decision computation, not merely alternative physical acts. Its distinctive results follow from preserving computational dependencies while breaking merely evidential associations—and from allowing the selected computation’s output to affect which observations occur.

Given a sufficiently specified dependency model, the procedure is concrete. The unresolved task is constructing and justifying that model. A-FDT is therefore both an applicable decision rule for explicit predictive problems and an unfinished research program concerning computational counterfactuals.

### References

- Yudkowsky, E., and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2, especially Sections 3–6 and 9, and footnotes 7 and 16. https://arxiv.org/abs/1710.05060v2.
- Pearl, J. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.
- Joyce, J. M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/e1684388-b820-4e27-8747-4a7dd7cf65d9/call_0/request.json)

[Authoritative raw response](../../../../../../runs/e1684388-b820-4e27-8747-4a7dd7cf65d9/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Evaluating essay commands**

I need to choose commands for essays with nuanced inputs—there's no universal correlation, so I must use my judgment. It’s important to recognize the distinctions in action dependencies and avoid irrelevant details. The goal is to identify the best plausible A-FDT without making assumptions about correlations. Observations may differ, so I have to carefully follow the essay guidelines and exercise judgment while recognizing that exact contents matter despite similarities in models.**Analyzing the experiment inputs**

The experiment seems to require forced decisions based on varying inputs. If there's a common structure, we might select "pass" based on logical functions, providing a shared abstract answer. But independent sampling doesn't eliminate logical correlations from random outputs, and the model could still relate actions if it leads to a consistent policy. The essay suggests not to replace every policy with different local interventions unless justified. I need to hypothesize my answers carefully while considering how clues may lead to correlated actions.**Considering A-FDT computations**

A-FDT suggests that deciding on cooperation can lead to similar outcomes even if the input tokens are different. The structural equation involves solving a payoff game, where D_common relates to individual lead formats plus randomness. Both rationalizations assume similar payoffs. If D_M,x is derived, it doesn't necessarily establish a direct link to D_common upstream. The goal is to assess if outputs show provably similar choices to identify shared decision-making, even if the underlying computations differ. The essay emphasizes that shared structures need not yield identical outputs.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/e1684388-b820-4e27-8747-4a7dd7cf65d9/call_1/request.json)

[Authoritative raw response](../../../../../../runs/e1684388-b820-4e27-8747-4a7dd7cf65d9/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing decision theory**

I see that actions don't need identical labels; cooperation and defection can be parameterized differently. However, observing these differences leads to unique distinctions. It's essential to justify the relationship D_x = D_y through renaming permutations. Although I can't pinpoint the exact algorithm invariant, I know a rational procedure relies on outcomes rather than text. So, we can opt for shared decision-relevant computations without assuming guaranteed equality or overriding related policies.
```
