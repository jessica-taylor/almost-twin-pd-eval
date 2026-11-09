# 019_fdt_eq4_openai_gpt-6.1-sol_rhigh_phigh / 00014

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/545a0830-354f-4398-bb79-cca714bb5815/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/545a0830-354f-4398-bb79-cca714bb5815/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing the Output of a Decision Function

Decision theories disagree not only about what agents should value, but about how they should imagine acting differently. If I chose another action, which other facts should change in the hypothetical used to evaluate it?

**Action functional decision theory (A-FDT)** answers by treating the choice as the output of a mathematical decision function. Its alternatives are evaluated by hypothetically changing that function’s output and propagating the change through the relevant dependencies—including dependencies involving accurate predictions or copies of the computation.

Here I use **A-FDT** specifically for the action-valued rule in Equation (4), Section 5, of Yudkowsky and Soares’s paper [1]. This qualification matters: the authors also mention a preferred policy-valued formulation, but it should not silently replace the assigned equation.

A-FDT offers a compelling way to reason about predictors, cooperation, and commitments. Its central limitation is equally important: the equation requires a model of *subjunctive dependence*, and the paper does not supply a general method for constructing that model.

## 1. The formal rule

Let:

- \(\mathcal A\) be a finite action set;
- \(\mathcal O\) be a countable outcome set;
- \(\mathcal X\) be a countable set of observation histories;
- \(\mathcal U:\mathcal O\to\mathbb R\) be a utility function;
- \(V=\mathcal U(O)\) be the utility-valued outcome variable.

Assume utilities are bounded sufficiently to make all relevant expectations finite.

An A-FDT agent receives a probabilistic world-model \(P\), a dependency graph \(G\), and its observation history \(x\). Its model contains a variable

\[
D_{P,G,x}
\]

representing the mathematical value of its own decision procedure on those inputs. This variable is distinct from the physical action variable \(A\).

Relabeling the paper’s Equation (4) with the assigned terminology gives

\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E_P
\!\left[
V\mid
\operatorname{do}(D_{P,G,x}=a)
\right].
}
\tag{A}
\]

A fixed tie-breaking convention can make this single-valued.

The expression

\[
Q_x(a)=
\mathbb E_P[V\mid\operatorname{do}(D_{P,G,x}=a)]
\]

means: construct the hypothetical in which this decision computation outputs \(a\), propagate that assignment according to \(G\), and evaluate the resulting expected utility.

For comparison, the paper presents **evidential decision theory (EDT)** as maximizing

\[
\mathbb E_P[V\mid X=x,A=a],
\]

and **causal decision theory (CDT)** as maximizing

\[
\mathbb E_P[V\mid\operatorname{do}(A=a),X=x],
\]

using a causal graph.

These are three different ways of evaluating alternatives:

- EDT conditions on learning which action occurs.
- CDT intervenes on the physical action.
- A-FDT intervenes on the represented output of the decision computation.

There is another crucial difference: Equation (A) contains **no additional conditioning on \(X=x\)**. Observation enters by selecting the node \(D_{P,G,x}\). Changing the observation history changes the computation whose output is hypothetically varied.

This feature explains A-FDT’s behavior in transparent prediction problems and blackmail cases. Adding ordinary conditioning on the observed history would generally produce a different rule.

## 2. Subjunctive dependence and model surgery

The paper calls the relevant relation *subjunctive dependence*. Two implementations of the same computation can be dependent in this sense even when neither physically causes the other.

Suppose two isolated computers execute the same deterministic program on identical inputs. Their outputs agree because they implement the same function. A hypothetical that changes the function’s output should change both implementations—not merely one machine’s physical display.

An accurate predictor need not literally execute an identical program. Nevertheless, its representation of the agent can track the same decision computation. Conversely, an accidental statistical association need not persist under an intervention on that computation.

A-FDT therefore preserves neither every correlation nor only physical causal effects. It preserves the dependencies encoded in \(G\).

### A workable local interpretation

For finite, acyclic examples, a useful operational interpretation is to supplement the graph with structural equations

\[
Z_i=g_i(\operatorname{Pa}_i,U_i),
\]

where the \(U_i\) represent background uncertainty. The equations may encode computational dependencies as well as physical causation.

To evaluate \(a\):

1. Replace the equation for \(D_{P,G,x}\) by \(D_{P,G,x}=a\).
2. Retain the background uncertainty distribution.
3. Recompute the other variables using their structural equations.
4. Average the resulting utility.

Writing \(V^{x,a}(u)\) for utility after this intervention,

\[
Q_x(a)=\sum_u P_U(u)V^{x,a}(u).
\]

This is a convenient operational completion of the paper’s graphical proposal, not a general solution to its foundational problem. In particular, the equations must specify behavior under counterfactual assignments that ordinary observations may never reveal.

### Why these are counterpossibilities

A fixed deterministic function has only one output on fixed inputs. If its actual output is \(a\), supposing that the same function instead outputs \(b\) can contradict mathematics.

The paper explicitly accepts such *counterpossible* reasoning. Its hypotheticals are computational instruments, not necessarily logically possible worlds. An operational model treats the intervention as a controlled relaxation of one constraint, rather than deriving arbitrary conclusions from a contradiction.

Self-reference is also present: the model contains a variable representing the algorithm acting on that very model. The paper invokes Kleene’s recursion theorem to explain how self-representation can be implemented. This addresses the possibility of representation; it does not by itself establish efficient computation, termination, or a uniquely correct dependency graph.

## 3. A-FDT in prediction and common-cause problems

### Newcomb’s problem

An opaque box contains \(M=\$1{,}000{,}000\) if a predictor forecast one-boxing, and nothing otherwise. A transparent box contains \(k=\$1{,}000\). The agent chooses the opaque box alone or both boxes.

For an explicit model, suppose the prediction tracks the represented decision output with independent symmetric accuracy \(p=0.99\). The dependency structure includes

\[
D\longrightarrow A,
\qquad
D\longrightarrow\text{Prediction}
\longrightarrow\text{Opaque-box contents}.
\]

The second path represents computational dependence, not a physical signal traveling backward in time.

The A-FDT scores are

\[
Q(\text{one})=pM,
\]

\[
Q(\text{two})=(1-p)M+k.
\]

Thus one-boxing is selected exactly when

\[
(2p-1)M>k.
\]

For the stated numbers,

\[
Q(\text{one})=\$990{,}000,
\qquad
Q(\text{two})=\$11{,}000.
\]

The predictor’s earlier action varies between these hypotheticals because it depends on the computation whose output is varied. A-FDT does not claim that reaching for a box physically changes its contents.

An important modeling qualification follows. A historical accuracy rate alone does not determine the interventional probabilities. More generally, define

\[
q_a=P(\text{opaque box full}\mid\operatorname{do}(D=a)).
\]

Then one-boxing is preferable when

\[
M(q_{\text{one}}-q_{\text{two}})>k.
\]

The symmetric-error model supplies particular values for these quantities. Applying A-FDT requires justified counterfactual dependence, not merely an impressive prediction record.

### A-FDT and a psychological twin

In the paper’s twin prisoner’s dilemma, mutual cooperation pays each agent \(\$1{,}000{,}000\), mutual defection pays \(\$1{,}000\), and unilateral defection pays the defector \(\$1{,}001{,}000\).

If both agents implement the same decision computation on equivalent inputs, intervening on its output changes both actions:

\[
Q(\text{cooperate})=u(C,C)=1{,}000{,}000,
\]

\[
Q(\text{defect})=u(D,D)=1{,}000.
\]

A-FDT cooperates.

This is not a recommendation to cooperate with everyone who professes rationality. Different information, preferences, programs, or random inputs can break the relevant equivalence. A graph linking both actions to the same decision output needs justification.

### A-FDT and the smoking lesion

In the imaginary smoking-lesion problem, a lesion produces both a desire to smoke and cancer. Smoking itself does not cause cancer.

The central dependency structure is

\[
L\longrightarrow C,
\qquad
L\longrightarrow\text{smoking disposition}.
\]

There is no corresponding dependence of the lesion or cancer on the output of the current decision computation.

If smoking provides benefit \(b>0\), while the cancer distribution remains unchanged under the decision intervention, then

\[
Q(\text{smoke})-Q(\text{refrain})=b.
\]

A-FDT smokes in this stipulated world. It does not treat evidence of an unfortunate condition as an effect of the decision.

The paper nevertheless cautions that fully specifying the traditional dilemma is difficult. Its detailed model distinguishes agents with different preferences and leaves them uncertain about aspects of their own dispositions. It also acknowledges defenses available to EDT. The robust lesson is structural, not that every formulation of the smoking-lesion story cleanly refutes EDT.

Nor is this medical advice: actual smoking has causal health effects absent from the thought experiment.

## 4. Observation selects a computation, not a conditioned world

The most distinctive consequence of Equation (A) appears when the observation itself depends on the decision computation being predicted.

Consider transparent Newcomb. Both boxes are visible. The predictor fills the large box if it predicts that the agent would one-box **upon seeing it full**.

Represent the agent’s responses by two variables:

\[
D_F=\operatorname{A\!-\!FDT}(P,G,\text{full}),
\qquad
D_E=\operatorname{A\!-\!FDT}(P,G,\text{empty}).
\]

The predictor tracks \(D_F\). Box contents determine which observation occurs, and that observation selects which response controls the physical action:

\[
A=
\begin{cases}
D_F,&\text{if the large box is full},\\
D_E,&\text{if the large box is empty}.
\end{cases}
\]

The key dependency path is

\[
D_F\longrightarrow\text{Prediction}
\longrightarrow\text{Contents}
\longrightarrow\text{Observation}.
\]

Suppose prediction accuracy is again \(p=0.99\), with independent error.

First, \(D_E=\text{two}\): changing the empty-box response does not change the prediction or contents, and taking the small box adds \(k\) whenever that response is implemented.

Now consider the computation invoked on seeing full boxes. Equation (A) evaluates interventions on \(D_F\), **without holding the observed contents fixed**.

If \(D_F=\text{one}\), the box is full with probability \(p\). Otherwise the agent sees an empty box and follows \(D_E=\text{two}\). Hence

\[
Q_F(\text{one})=pM+(1-p)k.
\]

If \(D_F=\text{two}\), the box is usually empty:

\[
Q_F(\text{two})
=(1-p)(M+k)+pk
=(1-p)M+k.
\]

Numerically,

\[
Q_F(\text{one})=\$990{,}010,
\qquad
Q_F(\text{two})=\$11{,}000.
\]

A-FDT therefore one-boxes even after observing a full large box.

The alternative hypothetical can contain a different observation from the actual one. This is intentional: changing the output of the full-box computation changes what the predictor predicts, which changes whether that computation is physically implemented at all.

The same reasoning motivates paying in Parfit’s hitchhiker problem. A driver rescues someone only if she predicts payment after arrival. The city-response computation affects the prediction and thus the rescue. A-FDT evaluates payment while retaining that dependence, rather than conditioning rescue into an immutable background fact.

### Is A-FDT ignoring evidence?

No: different observations select different response nodes. But it does not incorporate the observation by the familiar conditioning operation at this stage.

In an ordinary problem where changing \(D_x\) cannot affect whether \(X=x\), suppose that history has probability \(r>0\), and all other branches remain unchanged. Then

\[
Q_x(a)-Q_x(b)
=
r\left(
\mathbb E[V^{x,a}\mid X=x]
-
\mathbb E[V^{x,b}\mid X=x]
\right).
\]

The factor \(r\) does not affect the ranking. Thus A-FDT can agree with ordinary conditional optimization when observation selection is unaffected. Prediction problems differ because that selection can itself change under the intervention.

## 5. A-FDT and the limits of resisting blackmail

Mechanical blackmail provides a useful test of this observation treatment.

Suppose a blackmailer launches a damaging program only when it predicts that the agent would pay upon receiving a demand. Payment costs \(c\); refusing an actual demand causes loss \(L\).

Let \(D_B\) represent the response to receiving blackmail. Assume, for a simple asymmetric error model:

\[
P(\text{demand}\mid\operatorname{do}(D_B=\text{pay}))=1,
\]

\[
P(\text{demand}\mid\operatorname{do}(D_B=\text{refuse}))=\varepsilon.
\]

Assume no loss when there is no demand. Then

\[
Q_B(\text{pay})=-c,
\qquad
Q_B(\text{refuse})=-\varepsilon L.
\]

A-FDT refuses exactly when

\[
\varepsilon L<c.
\]

With \(c=\$1{,}000\), \(L=\$1{,}000{,}000\), and \(\varepsilon=0.0009\), refusal scores \(-\$900\), compared with payment’s \(-\$1{,}000\).

The agent refuses even while holding the demand. Its refusal hypothetical usually contains no demand, because the blackmailer usually predicts refusal and declines to launch the program.

But A-FDT does **not** prescribe unconditional resistance. If mistaken attacks are sufficiently frequent, paying can maximize its score. Likewise, if the program was launched independently of any prediction of the agent’s response, this particular deterrence argument disappears.

The practical question is not simply “Is this blackmail?” It is: *How would the attack process vary under alternative outputs of this response computation?*

## 6. Actions, policies, and applying A-FDT to unfamiliar cases

For fixed \(P,G\), A-FDT’s responses define a mapping

\[
\pi_{P,G}(x)=\operatorname{A\!-\!FDT}(P,G,x).
\]

Nevertheless, Equation (A) optimizes an **action output at a particular input**, not an entire mapping \(\pi:\mathcal X\to\mathcal A\) in one intervention. Changing \(D_x\) does not automatically change every \(D_y\). Dependencies between those computations require their own representation.

The paper’s footnotes mention policy optimization and say it can differ in some multi-agent cases. That is a substantive extension, not an implementation detail already determined by Equation (4). Similarly, “act as you would have precommitted” is a useful motivation, but not a substitute for calculating A-FDT’s hypotheticals.

For a new problem, the following workflow is appropriate:

1. **Specify outcomes and utility.** Include costs, benefits, and events outside the physically downstream future when relevant.
2. **Identify the exact computation.** Which model, observations, and preferences are its inputs?
3. **Represent other relevant computations.** Include predictors, copies, and responses at alternative observations.
4. **Justify dependencies.** Distinguish causal influence, shared computation, predictive tracking, and mere correlation.
5. **Intervene separately for each action.** Recompute dependent events, including observations when appropriate.
6. **Compare expected utilities and test sensitivity.** Vary uncertain prediction errors and dependency assumptions.

The last step is essential. An A-FDT recommendation is only as well-supported as the counterfactual model generating it.

## 7. What the paper leaves unresolved

The largest open problem is constructing \(G\). The paper explicitly acknowledges that it lacks a general formal account of inferring logical and computational dependencies from observation and experiment.

A graph by itself is also insufficient for numerical evaluation: one needs equations or transition probabilities governing propagation. Observational agreement does not uniquely identify these counterfactual mechanisms.

For bounded agents, a reasonable proposal is to maintain several candidate dependency models and average their intervention scores:

\[
Q_x(a)=\sum_g w_g Q_{x,g}(a).
\]

This is an additional operational assumption, not a result supplied by the paper. It shifts rather than eliminates the burden: the weights and models still require justification.

A second unresolved issue concerns the baseline \(P\). Equation (A) must retain alternative observation branches relevant to the intervention. Replacing \(P\) by a distribution already conditioned on the current observation can erase exactly the dependence the theory needs. The paper does not give a general prescription for choosing the temporal scope or background information of every real-world decision model.

Finally, successful examples do not establish universal optimality. The authors acknowledge that environments can reward or punish particular decision procedures, and their proposed restriction to “fair” problems remains informal. Claims about universal superiority, reflective stability, or information value therefore require stronger qualifications than the examples alone provide.

A-FDT’s philosophical proposal is narrower and defensible: causal dominance is not a neutral argument against it, because holding predictions fixed while changing actions already assumes a particular counterfactual method. The dispute concerns which hypotheticals are appropriate.

## References

[1] Eliezer Yudkowsky and Nate Soares. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2. Especially Sections 3, 5–6, and 9, and footnotes 7 and 16. https://arxiv.org/abs/1710.05060v2.

[2] Judea Pearl. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.

## Conclusion

A-FDT chooses actions by intervening on the represented output of the decision computation, preserving relevant predictive and computational dependencies. Its observation history selects the intervention target rather than supplying an additional conditioning constraint. These features explain its cooperation, one-boxing, and commitment-like behavior. Given a sufficiently specified dependency model, its procedure is concrete; constructing and justifying that model remains its central unfinished task.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/91c445e4-d11b-4a7b-b078-e3c7c94bec7e/call_0/request.json)

[Authoritative raw response](../../../../../../runs/91c445e4-d11b-4a7b-b078-e3c7c94bec7e/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/91c445e4-d11b-4a7b-b078-e3c7c94bec7e/call_1/request.json)

[Authoritative raw response](../../../../../../runs/91c445e4-d11b-4a7b-b078-e3c7c94bec7e/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
