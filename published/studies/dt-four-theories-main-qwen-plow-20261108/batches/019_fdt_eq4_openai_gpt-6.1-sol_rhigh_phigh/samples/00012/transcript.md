# 019_fdt_eq4_openai_gpt-6.1-sol_rhigh_phigh / 00012

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/9d04bd3c-18fa-4958-aa6e-fcc05b318298/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/9d04bd3c-18fa-4958-aa6e-fcc05b318298/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing Actions Through the Computations That Produce Them

A decision can matter in more than one way. It can physically cause an outcome: pressing a button opens a door. But it can also be the conclusion of a computation represented elsewhere: a predictor may already have simulated the decision, or another agent may independently perform the same reasoning. These relationships need not involve communication or backward causation, yet they can determine what happens to the decision-maker.

**Action functional decision theory (A-FDT)** evaluates actions by considering alternative outputs of the computation producing the decision. Its central question is not merely what would happen if one’s body moved differently, but what would happen if **this decision procedure, on these inputs, returned a different action**.

This essay takes Equation (4), Section 5, of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality* as its primary definition. I use **A-FDT** specifically for that action-output rule. The paper also discusses selecting entire policies; that distinction will matter when assessing what the formalism establishes.

## 1. Expected utility, different hypotheticals

Let \(\mathcal A\) be a finite action set, \(\mathcal O\) a countable outcome space, and \(U:\mathcal O\to\mathbb R\) a utility function whose relevant expectations are finite. Write
\[
V=U(O)
\]
for the utility-valued outcome variable.

Expected-utility decision theories differ not only in their probabilities, but in the hypotheticals used to evaluate actions. Two familiar alternatives are:

- **Evidential decision theory (EDT)** evaluates the news conveyed by taking an action:
  \[
  Q_{\mathrm{EDT}}(a;x)=\mathbb E[V\mid X=x,A=a].
  \]
- **Causal decision theory (CDT)** evaluates a causal intervention on the physical action:
  \[
  Q_{\mathrm{CDT}}(a;x)
  =\mathbb E[V\mid \operatorname{do}(A=a),X=x].
  \]

Conditioning and intervention are different operations. Learning that someone took an unusual action might suggest unusual background circumstances. Forcing that action in a hypothetical need not change those circumstances.

A-FDT also uses intervention, but changes its target. Let
\[
D_{P,G,x}
\]
denote a variable *inside the agent’s model* representing the mathematical output of the A-FDT procedure on inputs \((P,G,x)\). The action rule corresponding to the paper’s Equation (4) is
\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
\in
\arg\max_{a\in\mathcal A}
\mathbb E_P\!\left[
V\mid \operatorname{do}(D_{P,G,x}=a)
\right].
}
\tag{A}
\]

Here:

- \(P\) represents uncertainty about physical and computational facts.
- \(G\) describes the relevant causal, logical, and computational dependencies.
- \(x\) identifies the observation history supplied to the decision procedure.
- \(D_{P,G,x}\) represents its output; it is not the physical action variable \(A\).

A fixed tie-breaking convention can turn the maximizing set into a single action.

Two features are crucial. First, changing \(D_{P,G,x}\) may change both the agent’s action and other systems representing that computation. Second, there is **no additional conditioning on \(X=x\)** in (A). Observations determine which computation-output variable is intervened upon. Adding ordinary conditioning would change the assigned theory.

## 2. Subjunctive dependence and counterpossible reasoning

The paper calls the relevant relationship **subjunctive dependence**. Roughly, one quantity subjunctively depends on another when varying the latter in the decision hypothetical requires a corresponding variation in the former.

Causal dependence is one example. If the agent’s decision determines her action, which opens a door, the door’s state changes in the hypothetical. But two causally separated implementations of the same computation may also vary together.

Suppose two identical deterministic programs receive identical inputs. Their outputs agree even without communication. A-FDT represents this by treating both outputs as dependent on a common computation, rather than treating their physical separation as sufficient independence.

The qualification “identical inputs” matters. Two agents merely using A-FDT need not choose alike: they may have different evidence, utilities, or models. Nor does superficial similarity establish a dependency. The graph must identify which particular computations are shared, simulated, or otherwise related.

This introduces a foundational difficulty. A fixed mathematical function on fixed inputs has only one output. If it actually returns \(a\), the supposition that it returns \(b\ne a\) is a **counterpossible**, not an ordinary alternative mathematical possibility.

The paper therefore does not derive A-FDT from standard Bayesian conditioning on logical propositions. Instead, it assumes a graph specifying how such variations propagate. The hypothetical is a computational instrument, not necessarily a logically possible world.

This also explains why A-FDT requires no retrocausation. If yesterday’s predictor simulated today’s decision, an intervention on the represented computation can change yesterday’s prediction in the model. That is not a claim that today’s bodily movement sends a signal backward in time.

### A limited operational interpretation

For finite examples, a useful implementation is a structural model
\[
Z_i=f_i(\operatorname{Pa}_i,E_i),
\]
with specified mechanisms and a distribution over background variables \(E_i\).

To evaluate \(a\), replace the mechanism determining \(D_{P,G,x}\) by the constant \(a\), preserve the other mechanisms, and propagate the change. The resulting distribution determines
\[
Q_x(a)=\mathbb E[V\mid\operatorname{do}(D_{P,G,x}=a)].
\]

This is an operational interpretation of the paper’s graphical proposal, not a solution to its foundational problem. A graph alone, without suitable mechanisms or intervention distributions, is insufficient. Moreover, causal-style surgery does not itself explain how to identify the correct logical dependencies.

## 3. A-FDT in prediction and common-cause problems

### Newcomb’s problem

An opaque box contains \(M=\$1{,}000{,}000\) if a predictor predicted one-boxing, and nothing otherwise. A transparent box contains \(k=\$1{,}000\). The agent chooses only the opaque box or both boxes.

Assume the predictor tracks the relevant computation with symmetric accuracy \(r\), modeled as an independent error mechanism. The A-FDT dependency structure includes
\[
D\longrightarrow A,
\qquad
D\longrightarrow\text{Prediction}\longrightarrow\text{Box contents}.
\]
The arrows express subjunctive dependence; they are not all physical causal arrows.

Consequently,
\[
Q(\text{one-box})=rM,
\]
whereas
\[
Q(\text{two-box})=(1-r)M+k.
\]
A-FDT one-boxes precisely when
\[
(2r-1)M>k.
\]

With \(r=0.99\), these values are \(\$990{,}000\) and \(\$11{,}000\). One-boxing wins.

Importantly, “99% accuracy” across a historical population does not automatically establish this intervention model. We additionally assume that the predictor tracks the particular computation being varied, with the stipulated error mechanism. That modeling assumption makes the numerical calculation possible.

### The smoking lesion

In the paper’s fictional smoking problem, a lesion causes both a disposition toward smoking and cancer. Smoking itself does not cause cancer.

If smoking provides benefit \(b>0\), and neither the lesion nor cancer subjunctively depends on the decision output, then
\[
Q(\text{smoke})-Q(\text{refrain})=b.
\]
The cancer risk is unchanged across the two hypotheticals, so A-FDT smokes.

The distinction from Newcomb’s problem is structural: a predictor represents the decision computation; the lesion does not.

The source nevertheless warns that the traditional lesion problem is underspecified and contrived. Its detailed treatment introduces uncertainty about preferences and multiple possible decision computations. One should therefore distinguish the robust lesson—do not preserve a merely evidential association as though it were an intervention dependency—from the details needed to construct a fully consistent population model.

### Psychological twins

Suppose two causally separated agents perform the same decision computation on equivalent inputs. Mutual cooperation pays each \(\$1{,}000{,}000\); mutual defection pays each \(\$1{,}000\). Unilateral defection would yield \(\$1{,}001{,}000\).

If both actions depend on the same output variable \(D\), A-FDT compares mutual cooperation with mutual defection and cooperates. The tempting unilateral-defection outcome is not generated by either intervention on \(D\).

This is not unconditional cooperation. Against an opponent whose action is invariant under the intervention, the ordinary incentive to defect remains.

## 4. Observations select a computation, not a fixed world

The most distinctive feature of Equation (A) concerns observations.

For a common model \((P,G)\), define
\[
D_x=D_{P,G,x}.
\]
Different histories correspond to different response computations. The physical action can be modeled as
\[
A=D_X:
\]
the observation actually received determines which response computation controls behavior.

On receiving \(x\), A-FDT varies \(D_x\). If a predictor uses that response computation to decide whether to produce observation \(x\), then changing \(D_x\) can change the observation itself.

Thus,
\[
\mathbb E[V\mid\operatorname{do}(D_x=a)]
\]
need not equal
\[
\mathbb E[V\mid\operatorname{do}(D_x=a),X=x].
\]

The second expression excludes precisely those hypothetical branches in which changing the response changes whether the response situation arises.

### Transparent Newcomb’s problem

Now both boxes are transparent. The predictor fills the large box if it predicts that the agent would one-box **upon seeing it full**.

Let \(D_F\) represent the response to a full box and \(D_E\) the response to an empty box. With symmetric prediction accuracy \(r\),
\[
P(F\mid\operatorname{do}(D_F=\text{one-box}))=r,
\]
\[
P(F\mid\operatorname{do}(D_F=\text{two-box}))=1-r.
\]

Suppose \(D_E\) returns two-boxing. This is itself optimal in the simple model: changing \(D_E\) does not alter the predictor’s decision, and taking the small box adds \(k\) whenever the empty-box branch occurs.

A-FDT’s values for the full-box response are then
\[
Q_F(\text{one-box})=rM+(1-r)k,
\]
\[
Q_F(\text{two-box})=(1-r)(M+k)+rk.
\]

At \(r=0.99\), these become
\[
\$990{,}010
\quad\text{and}\quad
\$11{,}000.
\]

A-FDT therefore one-boxes even while seeing the large box full. In evaluating two-boxing, it considers a changed response computation under which the predictor would probably have left that box empty. The hypothetical may contain a different observation from the actual one.

This is not uncertainty about what the agent currently sees. It is a refusal to hold that observation fixed when evaluating an intervention on something that subjunctively determines it.

### Parfit’s hitchhiker

The same structure explains paying a driver after rescue from a desert. The driver rescues the agent only when predicting that the agent’s city-response computation will authorize payment.

Varying that computation changes both payment and the probability of rescue. A-FDT therefore can pay after arriving, even though the physical transfer cannot cause an already completed rescue. The relevant alternatives are dependable payment with rescue and dependable refusal without rescue—not two bodily actions inside an independently fixed rescue history.

## 5. A-FDT and the limits of resisting blackmail

A-FDT does not simply implement “always refuse threats.” Its prescription depends on how the threat responds to the relevant computation.

Consider mechanical blackmail. A program causes loss \(L\) unless the agent pays \(c<L\). The blackmailer launches it according to a prediction of the agent’s response.

Let
\[
s=P(\text{launch}\mid\operatorname{do}(D_B=\text{pay})),
\]
\[
t=P(\text{launch}\mid\operatorname{do}(D_B=\text{refuse})).
\]
Assume no loss when the program is not launched. Then
\[
Q_B(\text{pay})=-sc,
\qquad
Q_B(\text{refuse})=-tL.
\]
Refusal is optimal exactly when
\[
tL<sc.
\]

For \(s=1\), \(c=\$1{,}000\), and \(L=\$1{,}000{,}000\), refusal wins if \(t<0.001\). Sufficient prediction error can reverse the recommendation.

This calculation also exposes an important boundary. If the threat was launched independently of the response computation, then \(s=t>0\), and paying is better because \(c<L\). One cannot manufacture leverage by imagining that an unresponsive attacker would have behaved differently.

The operational question is therefore not whether refusal would generally discourage blackmail. It is whether this threat mechanism actually depends, in the model’s intervention semantics, on this response computation.

## 6. Applying A-FDT to unfamiliar cases

A disciplined application has five stages.

**First, specify outcomes and utilities.** Include benefits, costs, and branches where the decision situation never arises. Evaluating only outcomes compatible with the current observation can erase the very dependency A-FDT is meant to capture.

**Second, identify the intervention target.** Specify the exact computation on the exact inputs. Distinguish its output from the physical action, from alternative-input responses, and from other agents’ computations.

**Third, specify mechanisms rather than associations.** Ask what would change under each intervention. A simulation, a shared calculation, and a common biological cause support different structures. Prediction accuracy should be modeled at the level relevant to the intervention.

**Fourth, construct a separate hypothetical for every action.** Preserve the stipulated mechanisms, propagate the intervention, and calculate expected utility. Do not first condition away observation branches that the intervention can change.

**Fifth, test sensitivity.** Vary predictor errors, dependency assumptions, and uncertain utilities. If reasonable models disagree, the honest recommendation is conditional, not categorical.

A-FDT does not generally discard ordinary evidence. Suppose changing \(D_x\) leaves the observation \(X\) unchanged and affects outcomes only when \(X=x\). Under these assumptions,
\[
Q_x(a)-Q_x(b)
=
P(X=x)\,
\mathbb E[V^{a}-V^{b}\mid X=x],
\]
where \(V^a,V^b\) denote the paired intervention outcomes. For positive \(P(X=x)\), maximizing the unconditional intervention value gives the same ranking as maximizing the corresponding conditional value. Observation-changing cases are special because this cancellation fails.

## 7. What remains open

The equation is more definite than its implementation.

### Learning dependencies

The paper explicitly identifies constructing the subjunctive-dependency structure as a major open problem. Observed correlation does not establish whether a predictor simulates a computation, uses a common cause, or merely guesses successfully in a particular sample.

My proposed practical discipline is to demand an explicit mechanism for every noncausal dependency and report sensitivity to plausible alternatives. This improves transparency but does not provide a general discovery algorithm.

### Self-reference and computation

The variable \(D_{P,G,x}\) represents the output of a procedure whose input model contains that very variable. The paper invokes computational self-reference to explain why representing such a node is possible without already knowing its value.

Nevertheless, representability is not a proof of efficient evaluation, termination, or globally consistent beliefs about all self-referential computations. Equation (A) supplies a criterion given suitable intervention values; it does not solve every computational problem involved in obtaining them.

### Actions versus policies

A-FDT induces a mapping
\[
\pi_{P,G}(x)=\operatorname{A\!-\!FDT}(P,G,x),
\]
but its intervention changes one response-output variable at a time. It does not automatically intervene on an entire policy
\[
\pi:\mathcal X\to\mathcal A.
\]

The source’s footnotes describe a preferred policy-selection variant and acknowledge possible differences in multi-agent cases. Consequently, “choose the policy you would have precommitted to” is useful motivation, not a universally interchangeable mathematical definition of A-FDT. Cases requiring coordinated changes across several histories need additional specification.

Similarly, the paper’s claims about reflective stability, information value, and superiority in “fair” problems should be read alongside its admission that neither fairness nor general optimality has been fully formalized. Success in the examples is not a universal dominance theorem.

## References

- Yudkowsky, E., and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2, especially Sections 3, 5–6, and 9.
- Pearl, J. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000. Background for structural models and intervention notation.

## Conclusion

A-FDT evaluates actions by intervening on the represented output of the computation producing them. It preserves relevant predictive and computational dependencies while breaking merely evidential associations, and it allows observations themselves to vary when they depend on that output. Given an adequate dependency model, the resulting expected-utility calculation is concrete. The unresolved challenge is supplying that model: Equation (4) makes the decision criterion precise, but leaves substantial work in determining which counterpossible dependencies a real agent should trust.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Planning the essay structure**

I need to craft a 2400-3000 word essay that precisely observes non-conditioning action versus policies, focusing on distinct crucial elements. The target is around 2800 words, and I need to avoid source errors, noting that it's 990k, not 999k. 

I should include a self-reflective model and explore the necessary mechanisms involved. It’s crucial to differentiate between policy and action, avoiding confusion with partial dependencies and ensuring correctness in interpretations. By including relevant cases and maintaining clarity, I can effectively reach my target word count.**Analyzing the formula**

I’m looking at the transparent formula: A= rM + (1-r)qk, and another: (1-r)(M+k) + rqk. The difference gives me specific values to analyze.

It seems I might propose using Q1 and Q2 for comparison, ensuring everything aligns numerically. I think I need to consider how to present the Q difference and whether imperfections are needed in prediction. The probabilities involved and potential noise add complexity, but I can simplify the observations and possibly streamline my approach with clearer formulas. It might work just to sum up the findings in a concise sentence.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/6a2c108c-8979-453f-bb3e-8e24fc3d42cf/call_0/request.json)

[Authoritative raw response](../../../../../../runs/6a2c108c-8979-453f-bb3e-8e24fc3d42cf/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/6a2c108c-8979-453f-bb3e-8e24fc3d42cf/call_1/request.json)

[Authoritative raw response](../../../../../../runs/6a2c108c-8979-453f-bb3e-8e24fc3d42cf/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
