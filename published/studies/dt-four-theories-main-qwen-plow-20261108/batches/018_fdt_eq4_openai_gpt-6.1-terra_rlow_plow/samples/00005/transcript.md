# 018_fdt_eq4_openai_gpt-6.1-terra_rlow_plow / 00005

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/d2bda151-9d84-4312-8ee0-b95c82f40854/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/d2bda151-9d84-4312-8ee0-b95c82f40854/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Decisions as outputs of a function

A decision can influence more than its ordinary causal consequences. A predictor may have filled a box yesterday because it forecast what an agent would choose today. Another agent, reasoning independently in another room, may reach the same conclusion because it implements the same decision procedure. Neither case requires a signal travelling backwards in time or between the agents. Yet both can make the output of a decision procedure relevant to events that are not caused by the agent’s physical act.

**Action functional decision theory (A-FDT)** takes these dependencies as part of the decision problem. Its guiding question is not simply “What happens if this physical action is performed?” Nor is it “What would my action be evidence of?” Instead, it asks:

> What would the world be like if the decision function I am implementing returned this output?

The answer is a hypothetical model, not necessarily a possible world in which every logical truth remains intact. A-FDT compares the expected utilities of these hypotheticals and executes the action associated with the best one.

This essay takes Equation (4) of Yudkowsky and Soares’s paper as A-FDT’s primary formal rule. The paper calls its theory functional decision theory; it also mentions a preferred policy-based formulation in footnotes. The distinction matters: Equation (4) intervenes on a particular **action output**, while an intervention on an entire policy requires further specification. I will use A-FDT for the action-based rule and distinguish policy-based proposals from it.

## 1. Expected utility and three ways to evaluate an action

Let \(\mathcal A\) be a finite set of actions, \(O\) an outcome, and \(V=U(O)\) its utility. A decision theory associates each action \(a\) with a distribution over outcomes and chooses an action maximizing expected utility:

\[
a^* \in \arg\max_{a\in\mathcal A}
\sum_o P_a(O=o)\,U(o).
\]

The theories differ in how they construct \(P_a\).

**Evidential decision theory (EDT)** evaluates an action by conditioning on it:

\[
\operatorname{EDT}(P,x)
\in\arg\max_a \mathbb E[V\mid X=x,A=a].
\]

It asks what outcomes would be good news conditional on performing \(a\). As stated in the paper, this rule does not evaluate actions assigned probability zero.

**Causal decision theory (CDT)** instead intervenes on the physical action variable:

\[
\operatorname{CDT}(P,G,x)
\in\arg\max_a
\mathbb E[V\mid \operatorname{do}(A=a),X=x].
\]

Here \(G\) represents causal structure. The intervention replaces the ordinary mechanism determining \(A\), while propagating its consequences through causal descendants.

For **A-FDT**, let

\[
D_x
=
\operatorname{afdt}(\underline P,\underline G,\underline x)
\]

be a variable *in the model* representing the output of the A-FDT procedure on the specified inputs. The underlines indicate that the inputs identify the variable: \(D_x\) is a representation of the output, not the output itself. Equation (4), written with the assigned name, is

\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
\in\arg\max_{a\in\mathcal A}
\mathbb E\!\left[V\mid
\operatorname{do}(D_x=a)\right].
}
\tag{1}
\]

The graph \(G\) must now represent decision-relevant dependencies broader than physical causation. When \(D_x\) is set to \(a\), the model recomputes not only the physical action but also any prediction, simulation, or other variable represented as depending on that output.

The self-reference is deliberate: the procedure manipulates a variable naming its own output. The paper notes that a program can refer to a representation of itself without first knowing its output. This addresses the *representation* of self-reference; it does not by itself solve the harder problem of constructing a correct dependency graph or ensuring an efficient computation.

### The role of observation

Equation (1) does **not** simply add \(X=x\) as a conditioning event. The actual observation \(x\) selects the node \(D_x\) to intervene on. In an A-FDT hypothetical, changing that node may change what observation the agent would receive, and hence whether \(D_x\) would actually control its physical action.

This point is central to the paper’s transparent-box and blackmail examples. One displayed expression in its later transparent-box calculation includes \(\operatorname{do}(X=\text{full})\), but the accompanying graph and numerical calculation allow the box to become empty under the alternative intervention. I follow Equation (4) and that calculation’s substantive interpretation: \(x\) identifies the decision-function output under examination, rather than forcibly fixing the observed event in every hypothetical.

A model may still encode background information in \(P\). Exactly which information is held fixed, and which observation-generating mechanisms must remain variable, is an important modelling question—not something Equation (1) settles automatically.

## 2. Subjunctive dependence

The paper calls the relevant relationship **subjunctive dependence**. Causal dependence is one example: if a scribe copies a calculator’s display, what she writes depends on the display. But two calculators computing the same function also have related outputs, even if neither causally affects the other.

Likewise, if a predictor accurately simulates an agent’s decision procedure, its prediction can depend on the same computational fact as the agent’s action. A-FDT represents both as descendants of \(D_x\). This is not a claim that choosing now physically changes a prediction made yesterday. It is a rule for constructing alternative hypotheses about the output of the shared computation and the things represented as tracking it.

Mere correlation is not enough. An inherited condition might both make an agent inclined to smoke and increase its risk of illness. The illness does not thereby compute or predict the agent’s decision. An intervention on a decision-function output can break the action–illness correlation while leaving the condition and its effects intact.

For a deterministic procedure on fixed inputs, only one output is mathematically correct. Thus, at least some alternatives in Equation (1) are **counterpossible**: they suppose an output other than the actual logical result. A-FDT treats the resulting models as decision tools, not as ordinary beliefs. The source openly leaves a general account of such counterpossibilities unresolved. Supplying \(G\) is therefore substantive: ordinary causal graph surgery does not automatically tell us which logical relationships to preserve.

## 3. Newcomb’s problem

A predictor fills an opaque box with \$1 million if it predicts that the agent will take only that box. A transparent box contains \$1,000. The predictor has already acted.

Let \(D\in\{1,2\}\) denote the relevant A-FDT output, with \(1\) for one-boxing and \(2\) for two-boxing. Consider a model in which:

- the physical action equals \(D\);
- the predictor reports \(D\) correctly with probability \(r\);
- the opaque box is full exactly when the predictor reports \(1\).

The predictor’s error mechanism is assumed to have the same probability \(1-r\) under either intervention. Then

\[
\begin{aligned}
Q(1)
&=\mathbb E[V\mid\operatorname{do}(D=1)]
=r(1{,}000{,}000),\\
Q(2)
&=\mathbb E[V\mid\operatorname{do}(D=2)]
=(1-r)(1{,}000{,}000)+1{,}000.
\end{aligned}
\]

At \(r=0.99\), these values are \$990,000 and \$11,000, respectively. A-FDT one-boxes. More generally, in this symmetric-error model, it one-boxes when

\[
r>0.5005.
\]

That threshold depends on the assumed predictor model and payoffs. A predictor’s historical accuracy alone need not establish that the same accuracy holds under both decision-function interventions.

CDT two-boxes in the standard causal model: holding the already-filled box fixed, taking the extra \$1,000 is always better. EDT usually one-boxes when both actions have positive prior probability and the predictor is reliable: taking one box is evidence that it is full. A-FDT reaches the same action as EDT for a different reason. Its graph says the prediction tracks the decision-function output, not merely that the two are statistically correlated.

## 4. A contrasting dependency: the smoking lesion

Suppose smoking gives an agent 1,000 utility and has no causal effect on cancer. A lesion independently raises cancer risk and makes people more inclined to smoke. If smoking is evidence of the lesion, a simple EDT model can favour refraining: learning that one smoked is bad news about one’s health.

In a simplified A-FDT model, let \(p\) be the probability of cancer under either intervention on the relevant decision output. Then

\[
Q(\text{smoke})=1{,}000+1{,}000{,}000(1-p),
\qquad
Q(\text{refrain})=1{,}000{,}000(1-p).
\]

A-FDT smokes. The lesion and cancer risk do not change merely because the decision output is changed.

The paper’s fuller construction is more delicate. The lesion affects preferences, so it models different decision-function inputs for lesion and non-lesion agents. Intervening on the output for one input need not change the action under the other. In that construction, the advantage of the smoking output is \(1{,}000\) times the probability that this output controls the action, rather than necessarily the full \$1,000.

The authors also concede that the example is contrived: an accurate EDT agent may know enough about its own preferences or deliberation to remove the troubling correlation. The lesson is not that every smoking-lesion model defeats EDT. It is that A-FDT requires a distinction between a predictor tracking a computation and a common cause producing a correlation.

## 5. Observed outcomes and off-path actions

Consider **transparent Newcomb**. The agent sees whether the opaque box is full. The predictor fills it if it predicts that the agent would one-box *upon seeing it full*.

Let \(D_F\) be the output on observing a full box and \(D_E\) the output on observing an empty box. The prediction depends on \(D_F\); the action depends on whichever output corresponds to the observation actually received.

Assume a 99%-accurate predictor and let

\[
q=P(D_E=\text{two-box}).
\]

When evaluating \(D_F=\text{one-box}\), the box is full with probability \(0.99\). If the predictor errs, the box is empty and \(D_E\), not \(D_F\), controls the action. Thus

\[
Q(D_F=1)
=990{,}000+0.01q(1{,}000).
\]

When evaluating \(D_F=\text{two-box}\), the box is full only when the predictor errs:

\[
Q(D_F=2)
=0.01(1{,}001{,}000)+0.99q(1{,}000).
\]

The first value is greater for every \(q\in[0,1]\). Equation (1) therefore prescribes one-boxing after seeing both boxes full.

The striking feature is not that A-FDT denies what the agent sees. It is that, to evaluate an alternative output of the procedure used *when the box is full*, it includes hypothetical runs in which the box would be empty and that procedure would not control the physical act. Conditioning every hypothetical on a full box would discard the predictor-mediated consequence on which this result relies.

Parfit’s hitchhiker has the same structure. A driver rescues a stranded agent only if she predicts that the agent will pay \$1,000 on arrival. Under a reliable-prediction model, A-FDT pays in the city: the output “pay on arrival” is associated with rescue, while “refuse on arrival” is associated mostly with being left in the desert. This is a conditional prescription given the specified model, not a claim that paying physically causes the past rescue.

## 6. Coordination and imperfect links

In a prisoner’s dilemma against an exact psychological twin, both agents implement the same decision function on equivalent inputs. Suppose mutual cooperation pays each \$1 million, mutual defection \$1,000, and unilateral defection pays the defector \$1,001,000.

An A-FDT intervention on the shared output gives

\[
Q(C)=1{,}000{,}000,\qquad Q(D)=1{,}000.
\]

A-FDT cooperates. The other player’s action changes in the hypothetical because it is another implementation of the same output, not because the agents communicate.

The conclusion weakens when the link is imperfect. As an illustrative model, suppose that under either intervention the other player matches the chosen output with probability \(s\), and otherwise does the opposite. Then

\[
Q(C)=s(1{,}000{,}000),\qquad
Q(D)=s(1{,}000)+(1-s)(1{,}001{,}000).
\]

Cooperation is preferred when \(s>0.5005\). This calculation is a modelling proposal, not a universal measure of “similarity”: a real opponent may respond asymmetrically, use different inputs, or predict the agent by methods whose errors change across interventions.

The same caution applies to repeated actions by one person. Going to the gym today does not automatically make future decisions change with today’s output. There must be a represented dependency—perhaps the same algorithm on effectively identical inputs. Different dates, health states, incentives, and observations may make future outputs distinct nodes.

## 7. Applying A-FDT to unfamiliar problems

A practical application can proceed as follows.

1. **Define the target output.** Specify the decision procedure, its input \(x\), the candidate actions, and the model variable \(D_x\). Distinguish this variable from the physical act.

2. **Model the environment.** Include outcome and utility variables, relevant observations, predictions, other agents, and ordinary causal mechanisms.

3. **Mark dependencies.** For each predictor, copy, or downstream event, ask how its distribution would change under an intervention on \(D_x\). Do not infer this solely from temporal order or statistical correlation.

4. **Construct each hypothetical.** Replace the mechanism for \(D_x\) with \(D_x=a\), propagate changes through the stipulated graph, and retain the distributions of variables not affected by the intervention.

5. **Compute expected utility.** Compare the resulting values and choose a maximizing output, with a specified tie-breaking rule if needed.

6. **Test sensitivity.** Vary predictor accuracy, error structure, observation mechanisms, and uncertain dependencies. Report which assumptions change the recommendation.

A useful *operational proposal* is to represent an uncertain predictor with a stochastic response kernel

\[
K(b\mid a,z)
=
P(B=b\mid \operatorname{do}(D_x=a),Z=z),
\]

where \(B\) is its prediction and \(Z\) records relevant context. One can then propagate \(B\) through the rest of the model. This makes assumptions visible and permits sensitivity analysis. But \(K\) is not generally identifiable from ordinary correlations alone; defining or estimating it may require knowledge of the predictor’s code, simulations, structural assumptions, or a theory of logical counterfactuals.

Nor should every instance of the same named algorithm be tied together indiscriminately. Equation (1) identifies an output on specified inputs. Whether another computation depends on that output is a fact to be modelled, not a consequence of both computations carrying the label “A-FDT.”

## 8. Actions, policies, and open questions

A policy \(\pi:\mathcal X\to\mathcal A\) specifies actions for multiple observations. The paper notes that its authors prefer a policy-based formulation, but Equation (1) does not itself supply one. A natural extension would introduce a policy-output variable \(\Pi\) and compare

\[
\mathbb E[V\mid\operatorname{do}(\Pi=\pi)],
\]

then execute \(\pi(x)\). This is **not automatically equivalent** to A-FDT’s action-output intervention. Changing a whole policy can alter predictions and actions at several observations simultaneously; changing \(D_x\) changes one specified output. Whether policy coordinates are linked, and how an agent selects among policies, require additional assumptions. Such an extension may be valuable for multi-agent or sequential problems, but it should not be silently substituted for Equation (1).

The largest unresolved issue remains construction of \(G\). A graph can make the examples calculable once its dependencies are supplied, but the paper does not provide a general procedure for discovering them or prove that Pearl-style graphs can adequately represent every logical dependency. Imperfect predictions, randomized agents, logically equivalent computations with different descriptions, and self-referential predictors all pose further difficulties.

The philosophical case is correspondingly conditional. The paper argues that A-FDT tends to achieve more utility in its examples and that it behaves like an agent that had made useful advance commitments. It also proposes an informal distinction between “fair” problems that reward actions and problems designed to reward a particular decision theory. It does **not** establish a formal fairness criterion or prove A-FDT optimal across all fair problems. The paper’s claims about non-negative value of information and reflective stability likewise should not be read as general theorems following from Equation (1) without assumptions about information, models, and available strategies.

## Conclusion

A-FDT evaluates an action by intervening on the output of the decision function that would choose it, then calculating utility in a model that preserves the stipulated causal and computational dependencies. This explains both its one-boxing in Newcomb’s problem and its willingness to break merely evidential correlations in the smoking-lesion model.

The procedure is precise **given** an appropriate model; discovering and justifying that model is the central open problem. For unfamiliar cases, the disciplined question is therefore not merely “Who predicts me?” but “Which variables would change under this particular decision-output intervention, and why?”

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060v2, especially §§3–6. https://arxiv.org/abs/1710.05060v2
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/6ce6256e-739f-48c2-b3b3-33037e6b9996/call_0/request.json)

[Authoritative raw response](../../../../../../runs/6ce6256e-739f-48c2-b3b3-33037e6b9996/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/6ce6256e-739f-48c2-b3b3-33037e6b9996/call_1/request.json)

[Authoritative raw response](../../../../../../runs/6ce6256e-739f-48c2-b3b3-33037e6b9996/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
