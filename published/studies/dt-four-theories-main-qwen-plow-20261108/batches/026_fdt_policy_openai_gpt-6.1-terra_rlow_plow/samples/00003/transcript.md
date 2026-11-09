# 026_fdt_policy_openai_gpt-6.1-terra_rlow_plow / 00003

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/d4da7ac7-fe53-44b2-8c98-87d0f2a18c18/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/d4da7ac7-fe53-44b2-8c98-87d0f2a18c18/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: Choosing the policy a decision procedure outputs

Policy functional decision theory, **P-FDT**, asks an agent to evaluate not just isolated physical acts, but alternative outputs of its decision procedure. Its central thought is that an action may be linked to other events in ways that are not ordinary effects of performing that action. A predictor may have already forecast it; another agent may be running the same computation; or a future copy of the decision-maker may use the same rule.

The source paper presents functional decision theory chiefly through an action-selection formalism. But footnote 16 states that the authors’ preferred formulation intervenes on the decision procedure to choose a **policy**—a mapping from inputs to actions—and then applies that policy to the agent’s inputs. Footnote 7 likewise says that iterating over policies can matter in multi-agent dilemmas. The paper does not, however, supply a full policy-selection algorithm. The account below treats those passages as primary and develops one explicit interpretation, marking the extra assumptions where they matter.

The philosophical motivation is easiest to see in Newcomb’s problem. A predictor has already filled an opaque box with $1 million if she predicted that you would take it alone. A transparent box contains $1,000. If the predictor is reliable, the sort of agent who takes the opaque box alone usually gets $1 million; the sort who takes both usually gets $1,000. Yet, once the boxes have been filled, taking the extra $1,000 cannot physically change their contents.

P-FDT treats this as more than a choice between physical acts with the past fixed. It asks what the world would look like under alternative outputs of the decision procedure being predicted. That does **not** mean believing that a present action sends a signal backward in time. It means using counterfactual models that preserve the relevant relationship between a decision computation and an earlier prediction of it.

## 1. Actions, policies, and decision procedures

Let \(X\) be a set of possible inputs or observation histories, and let \(A(x)\) be the actions available on input \(x\). A deterministic policy is a function

\[
\pi:X\longrightarrow A,\qquad \pi(x)\in A(x).
\]

For example, in a transparent-box problem a policy can specify both what to do upon seeing a full box and what to do upon seeing an empty one. A policy is therefore more than an action at the observation actually encountered.

Write \(S\) for the P-FDT policy-selection computation and \(M\) for its model of the problem. Following footnote 16, we can schematically represent its output and the resulting act as

\[
\Pi=S(M),\qquad A=\Pi(X).
\]

The selector may have additional inputs, and the boundary between those inputs and the policy’s inputs is not settled by the footnote. For now, imagine that \(M\) describes a decision problem from a perspective broad enough to include the relevant possible observations. After selecting a policy, the agent applies it to the input \(x\) it actually receives.

A useful idealized rule is

\[
\pi^*\in\operatorname*{arg\,max}_{\pi\in\mathcal P}
  \mathbb E_{Q_\pi}[U(O)],
\qquad
a^*=\pi^*(x).
\tag{1}
\]

Here \(\mathcal P\) is a specified class of admissible policies, \(O\) is the outcome, and \(U\) is the agent’s utility function. The crucial term is \(Q_\pi\): the decision-theoretic distribution constructed for the hypothesis that **this policy selector outputs \(\pi\)**. It is not automatically the ordinary probability distribution conditional on the agent following \(\pi\), nor is it necessarily the distribution produced by physically installing \(\pi\) at the last moment.

Equation (1) is **my operational proposal**, not an equation given in footnote 16. It follows the footnote’s policy-selection architecture and the paper’s broader expected-utility and intervention-based treatment. To make it applicable, one must additionally specify a policy class, a tie-breaking rule, a utility function, a model, and a method for constructing each \(Q_\pi\).

A graphical implementation might use a node \(\Pi\) representing the selector’s output and write

\[
Q_\pi(O)=P\!\left(O\mid\operatorname{do}(\Pi=\pi)\right),
\tag{2}
\]

with a graph containing not only causal links but also the relevant computational and predictive dependencies. The notation is borrowed from interventionist causal modelling, but the operation is broader than a physical intervention: \(\Pi\) represents the output of a mathematical computation. The graph tells us which other representations change when that output is hypothetically changed.

This is a way to *encode* an answer to the dependency question, not a general solution to it. The source explicitly acknowledges that it lacks a satisfactory general method for discovering the structure of subjunctive dependencies or evaluating arbitrary logical counterpossibilities.

## 2. What changes in a P-FDT hypothetical?

The source calls the relevant relation **subjunctive dependence**. A causal effect is one example: if an agent presses a button, a connected lamp may illuminate. But two computations can also be related because they implement the same function. A predictor’s simulation and the agent’s actual computation may produce corresponding outputs even though the simulation happens earlier and is not physically caused by the later act.

When constructing \(Q_\pi\), the intended discipline is:

1. Set the represented output of the policy selector to \(\pi\).
2. Propagate that change through the model’s relevant computational, predictive, and causal links.
3. Keep unrelated background features governed by their specified distributions.
4. Calculate expected utility over the resulting outcomes.

“Keep unrelated features fixed” does not mean that every realized fact remains numerically unchanged. It means retaining the model’s background mechanisms and uncertainty while allowing variables downstream of the stipulated logical output to change.

This differs from two familiar theories. **Evidential decision theory** (EDT), in its simple form, evaluates an action by conditioning on taking it:

\[
V_{\rm EDT}(a)=\mathbb E[U(O)\mid X=x,A=a].
\]

**Causal decision theory** (CDT), in a graphical formulation, evaluates an intervention on the physical action:

\[
V_{\rm CDT}(a)=\mathbb E[U(O)\mid X=x,\operatorname{do}(A=a)].
\]

P-FDT instead evaluates a hypothesized output of the policy-selection computation. It preserves dependencies on that output even when they are not causal consequences of the eventual physical action. Conversely, it does not preserve every statistical correlation merely because it exists.

Consider the paper’s imaginary smoking-lesion case. A lesion makes an agent inclined to smoke and also causes cancer; smoking itself does not cause cancer. If smoking gives the agent positive utility, then changing the decision rule’s output from “refrain” to “smoke” need not change whether the lesion is present. In the stipulated model, P-FDT therefore chooses smoking. The apparent action–cancer correlation arises from a common cause, not from cancer tracking the decision computation.

There are modelling complications: the paper itself notes that making the lesion story internally consistent may require uncertainty about the agent’s preferences or decision process. The lesson is conditional on the model, not that every observed smoking–cancer correlation should be ignored.

## 3. Newcomb’s problem under P-FDT

Suppose the predictor is correct with probability \(p=0.99\), with the same error rate for either prediction. Let the policy have only one relevant input: choose one box or two. Under the stipulated predictor model,

\[
\begin{aligned}
V(\pi_{\rm one})
 &=0.99(1{,}000{,}000)=990{,}000,\\
V(\pi_{\rm two})
 &=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\end{aligned}
\]

P-FDT selects the one-boxing policy. The counterfactual difference is not that taking one box causally fills the opaque box. It is that, under the model, a predictor tracking the selector’s output is likely to fill it when that output prescribes one-boxing and likely to leave it empty when it prescribes two-boxing.

More generally, if the predictor has symmetric accuracy \(p\), the opaque-box prize is \(B\), and the transparent-box prize is \(b\), one-boxing is preferred when

\[
pB>(1-p)B+b,
\qquad\text{or}\qquad
(2p-1)B>b.
\]

Predictive dependence can therefore be too weak to justify giving up the smaller prize. Also, “99% accurate” as a historical aggregate is not by itself enough to establish symmetric accuracy under both policy interventions. The calculation needs the counterfactual response rates, which are assumptions about the predictor.

CDT reaches a different result in its standard model: holding the already-filled box fixed, two-boxing yields \(b\) more regardless of its contents. EDT may one-box because taking one box is evidence that the predictor filled it. P-FDT’s argument is distinct from both: it asks how the predictor responds to alternative outputs of the procedure it models.

## 4. Observation and the policy perspective

Policies matter most when different possible inputs lead to different actions. In transparent Newcomb, suppose the predictor fills the opaque box if she predicts that the agent would leave the transparent box behind **upon seeing the opaque box full**. A policy must specify

\[
\pi(\text{full})\quad\text{and}\quad\pi(\text{empty}).
\]

With a perfect predictor, compare these policies:

- \(\pi_1(\text{full})=\text{one-box}\), \(\pi_1(\text{empty})=\text{two-box}\);
- \(\pi_2(\text{full})=\text{two-box}\), \(\pi_2(\text{empty})=\text{two-box}\).

Under \(\pi_1\), the predictor fills the box and the agent receives \(1{,}000{,}000\). Under \(\pi_2\), the predictor leaves it empty and the agent receives \(1{,}000\). Thus the policy comparison favors \(\pi_1\); when the agent sees a full box, it applies \(\pi_1\) and takes only that box.

The policy’s empty-box action still matters: with predictor error, an empty box can occur under \(\pi_1\), and two-boxing then gains the transparent-box prize. Evaluating a whole policy makes such contingencies explicit.

There is a difficult question here: **which information is held fixed during policy selection?** The paper’s action-level formalism addresses observation by changing the decision-function node on which it intervenes, rather than simply conditioning every hypothetical on the current observation. Consequently, its transparent-Newcomb hypothetical can assign substantial probability to seeing an empty box even when the agent actually sees a full one.

My proposal for equation (1) is similar in spirit: evaluate policies using a model that includes the observation-generating process, and then apply the selected policy to the actual observation. Information already built into the model remains available; observations whose occurrence may depend on the policy are represented within the counterfactual rollout rather than automatically fixed across all policies. This is an **updateless-style** interpretation, not a fully specified consequence of footnote 16. Wei Dai’s **updateless decision theory** is a related but distinct theory.

The distinction matters. If one instead conditions every policy hypothetical on the opaque box actually being full, then both policies begin with the $1 million already present, and taking the additional $1,000 looks better. The choice between these constructions is part of the philosophical issue, not a notational detail.

Nor should P-FDT simply “ignore evidence.” A policy can react to evidence: it may prescribe different actions for a full and an empty box. The question is whether the *occurrence* of that evidence is itself allowed to vary while alternative policies are evaluated.

## 5. Prediction, threats, and error rates

The same structure appears in the paper’s mechanical-blackmail example. A blackmailer runs a damaging program only if she predicts that the agent would pay $1,000 on receiving a demand. If run, the program causes $1 million in damage unless the agent pays.

Assume, for a simple model, that a policy of paying is always predicted correctly, whereas a policy of refusing is mistakenly predicted to pay with probability \(\epsilon\). The expected losses are

\[
L(\pi_{\rm pay})=1{,}000,\qquad
L(\pi_{\rm refuse})=\epsilon\,1{,}000{,}000.
\]

The proposed P-FDT policy comparison favors refusal when

\[
\epsilon<0.001.
\]

If \(\epsilon=0.0009\), refusal has expected loss $900 and paying has expected loss $1,000. If \(\epsilon=0.0011\), refusal has expected loss $1,100, so paying is better in this model. The latter rate is **0.11%**, not 0.011%; the source’s nearby numerical statement appears to contain a typo.

The unusual implication is that a refusal policy can prescribe refusing *even after an erroneous demand has arrived*. In the policy comparison, that demand is rare under refusal but common under payment. Once it has arrived, paying would prevent the damage in the actual situation; P-FDT’s recommendation relies instead on the global policy-level comparison.

This conclusion is not unconditional advice to refuse threats. A blackmailer may issue demands independently of predicted compliance; error rates may differ; payment may have other consequences; and the decision-maker’s information may warrant a different model. The calculation illustrates how to use the proposed rule once those dependencies have been specified.

## 6. Shared policies and other agents

A policy intervention may also alter another agent’s behavior when that behavior depends on the same computation.

In the psychological-twin prisoner’s dilemma, two agents choose cooperate or defect. Each receives $1 million if both cooperate, $1,000 if both defect, and $1,001,000 if they defect while the other cooperates. Assume their inputs are the same and they implement the same relevant policy computation. The policy hypotheticals are then

\[
V(\pi_C)=1{,}000{,}000,\qquad
V(\pi_D)=1{,}000.
\]

P-FDT cooperates. CDT, holding the other agent’s choice causally fixed, defects because that earns an extra $1,000 against either fixed choice. EDT may also cooperate, but does so by treating cooperation as evidence of the twin’s cooperation.

The policy formulation becomes especially useful when inputs differ. Suppose two copies receive private signals \(x_1\) and \(x_2\) but share \(\pi\). Under an intervention on the shared policy, their actions are

\[
A_1=\pi(x_1),\qquad A_2=\pi(x_2).
\]

They need not take the same action: the same rule may respond differently to different inputs. Evaluating only a current action can miss how the proposed rule behaves at the other copy’s input. This is one reason the paper’s footnotes suggest that policy selection can matter in multi-agent cases.

The shared-policy link must be justified. Similar people do not automatically share an identical computation, and a policy change need not alter a dissimilar opponent. In an imperfect-copy model, one might assign a probability \(r\) that the other agent tracks the relevant policy output and otherwise model its behavior separately. The preferred policy then depends on \(r\), the payoff matrix, and the distribution of both agents’ inputs.

Randomized policies introduce another unresolved choice. A shared policy may output the same probability distribution for both agents without their random draws being identical. Shared random seeds, independent private randomness, and predictable pseudorandomness yield different joint-action distributions. Equation (1) can accommodate them only after the model specifies which randomness is shared and which is predictable.

## 7. Counterpossibilities and limits of the formalism

If a deterministic selector \(S(M)\) in fact outputs \(\pi_1\), then the proposition \(S(M)=\pi_2\) is mathematically false. P-FDT nevertheless asks for a useful hypothetical in which that output differs. Such a hypothetical is a **counterpossible**: its antecedent conflicts with a mathematical fact, not merely with an observed event.

Ordinary conditioning does not solve the problem if the antecedent has probability zero. Nor does merely imagining that a different program was installed: the source points out that a predictor of the *actual* selector may not track a last-minute substitute. P-FDT needs to represent what would follow if the selector being predicted had a different output.

A dependency graph is a practical idealization. For Newcomb, one can insert links from \(\Pi\) to the agent’s act and to the predictor’s prediction, plus an error variable. Intervening on \(\Pi\) then gives the desired comparison. But a graph does not prove that its links are correct, and different graphs can yield different decisions. Logical relationships can be cyclic, context-sensitive, or hard to infer from a predictor’s observed accuracy. The paper identifies finding a principled theory of these dependencies as a major open problem.

Several further choices remain open in policy P-FDT:

- **Policy scope.** How much of an agent’s life, or how many decision situations, does one policy cover? A narrow policy may miss a dependency; an excessively broad one may join unrelated decisions.
- **Input identity.** Which observations belong inside the policy, and which are inputs to the selector or fixed background information?
- **Selection and ties.** Different policies can agree at the actual input but differ elsewhere. Tie-breaking can affect what predictors or other copies do.
- **Self-reference.** The selector evaluates hypotheses about its own output. Self-referential representations can be constructed, but their existence alone does not guarantee a tractable, uniquely solved optimization.
- **Model uncertainty.** A practical agent may need to average over competing dependency models, including the possibility that a predictor is less responsive than advertised.

The paper argues that functional decision theory performs well in many “fair” problems—roughly, problems where rewards depend on behavior rather than a label attached to the decision theory. It also concedes that no theory wins every constructed problem and that a satisfactory general definition of fairness is missing. Neither the examples above nor equation (1) establishes universal optimality.

## Conclusion

P-FDT’s distinctive move is to compare alternative **policy outputs of the decision procedure**, carrying their consequences through causal, computational, and predictive dependencies, and then to apply the chosen policy to the actual input. This makes it possible to reason about predictors, copies, and contingent behavior within one expected-utility framework.

Footnote 16 provides that architecture, not a complete semantics. The operational rule developed here is one way to make it usable, but its answers depend on how policy scope, information, randomness, and subjunctive dependencies are modelled. Those choices are not secondary implementation details: they determine which counterfactuals P-FDT asks the agent to compare.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, especially §§3–6 and footnotes 7 and 16, [arXiv:1710.05060v2](https://arxiv.org/abs/1710.05060v2).
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/bee8ac2e-f708-495c-aa90-f75dd23f7d23/call_0/request.json)

[Authoritative raw response](../../../../../../runs/bee8ac2e-f708-495c-aa90-f75dd23f7d23/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/bee8ac2e-f708-495c-aa90-f75dd23f7d23/call_1/request.json)

[Authoritative raw response](../../../../../../runs/bee8ac2e-f708-495c-aa90-f75dd23f7d23/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
