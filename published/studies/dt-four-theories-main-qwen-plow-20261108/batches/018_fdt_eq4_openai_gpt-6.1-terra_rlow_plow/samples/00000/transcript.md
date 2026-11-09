# 018_fdt_eq4_openai_gpt-6.1-terra_rlow_plow / 00000

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/dc428301-d95f-4013-bef5-813a539c4e15/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/dc428301-d95f-4013-bef5-813a539c4e15/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing the Output of a Decision Procedure

A decision can be influenced by more than its ordinary causal consequences. A predictor may have already acted on a prediction of it; another agent may be running the same reasoning; a future version of the decision-maker may face essentially the same choice. In each case, changing one physical action while holding everything else fixed can omit a dependency that matters to the outcome.

**Action functional decision theory**, or **A-FDT**, addresses this by evaluating possible outputs of the decision procedure itself. It asks: if this very procedure returned a different action on these inputs, what else in the world-model would vary with that output?

This essay uses Equation (4) of Yudkowsky and Soares’s paper as the formal presentation of A-FDT. The paper calls its theory “FDT”; the name A-FDT here emphasizes that the equation selects an action. The authors also mention a preferred policy-selection formulation, but do not specify it fully. The distinction matters: a rule that changes one action-output node is not automatically equivalent to one that changes an entire policy.

## 1. The problem A-FDT is trying to solve

Consider a prisoner’s dilemma played against a perfect psychological twin. Each player receives:

| Your action | Twin cooperates | Twin defects |
|---|---:|---:|
| Cooperate | \$1,000,000 | \$0 |
| Defect | \$1,001,000 | \$1,000 |

The players cannot communicate and neither action physically causes the other. If your twin’s action is held fixed, defecting yields \$1,000 more. **Causal decision theory** (CDT), in its standard formulation, therefore defects.

But suppose the twin uses exactly the same decision procedure, with the same relevant inputs. Then the two computations have the same output. If that output is cooperation, both cooperate; if it is defection, both defect. A-FDT compares those two coupled outcomes and cooperates.

The reasoning is not “my cooperation sends a signal to my twin.” It is that both actions depend on the same computation. This dependency can matter even though it is neither a causal arrow from one physical action to the other nor merely a correlation discovered in a sample.

The paper calls the relevant broader relation **subjunctive dependence**. Causal dependence is included: an action’s ordinary effects vary with it. But two implementations of the same computation, and a sufficiently accurate prediction of that computation, can also vary together in the relevant hypotheticals. Mere statistical correlation is not enough.

The distinction is the central modelling obligation of A-FDT. It does not say that every correlated event should be made to change when a decision changes. Nor does it say that physical action can change the past.

## 2. The action-functional rule

Let:

- \(P\) be a probability model over outcomes and other variables;
- \(G\) describe the causal and other subjunctive dependencies the agent uses;
- \(x\) be the agent’s observation history;
- \(\mathcal A\) be the available actions;
- \(V=U(O)\) be the utility of outcome \(O\).

Write \(D_{P,G,x}\) for a **variable inside the model** representing the output of the A-FDT decision procedure on inputs \((P,G,x)\). This variable must be distinguished from the actual output of that procedure. In the paper’s notation, underlining identifies the inputs used to name the model variable.

Equation (4), renamed for this essay, is

\[
\operatorname{A\!-\!FDT}(P,G,x)
\in
\arg\max_{a\in\mathcal A}
\mathbb E_{P,G}
\!\left[
V\mid
\operatorname{do}(D_{P,G,x}=a)
\right].
\tag{1}
\]

For each candidate \(a\), the agent constructs a hypothetical model by setting the represented decision-function output to \(a\), propagating the consequences through \(G\), and computing expected utility. It then executes a maximizing action. A tie-breaking rule must be supplied if several actions maximize the expression.

The intervention notation is borrowed from graphical causal models, but \(G\) here is **not just a causal graph**. It must also encode whichever logical, computational, predictive and other dependencies are relevant. In an ordinary structural model, an intervention replaces a node’s generating equation by a constant and recomputes its descendants. Equation (1) asks for analogous surgery on a node representing a mathematical output.

The resulting hypothetical is a tool for choice, not necessarily a belief about what is physically or logically possible. If a deterministic procedure on fixed inputs actually returns \(a_1\), then its returning \(a_2\) on those same inputs is a **counterpossible** antecedent: it conflicts with a mathematical fact. A-FDT nevertheless needs a disciplined way to ask what would follow from that antecedent while preserving the dependencies useful for the decision.

The paper explicitly leaves the general construction of \(G\) open. Supplying a graph is therefore not a minor implementation detail: two graphs with different arrows can yield different prescriptions. The equation is a decision rule *given* an adequate dependency model, not a complete procedure for discovering one.

### Comparison with EDT and CDT

For contrast, **evidential decision theory** (EDT) evaluates

\[
\operatorname{EDT}(P,x)
\in \arg\max_a \mathbb E[V\mid X=x,A=a],
\]

where conditioning is defined. It asks what taking an action would be evidence of. Standard CDT instead evaluates

\[
\operatorname{CDT}(P,G_C,x)
\in \arg\max_a
\mathbb E[V\mid \operatorname{do}(A=a),X=x],
\]

using a causal graph \(G_C\). It changes the physical action and its causal effects.

A-FDT changes neither “the fact that I chose \(a\)” by ordinary conditioning nor only the physical action token. It changes the represented output of the decision function and propagates the specified subjunctive consequences. Thus its evaluation can preserve a predictor’s dependence on the decision while breaking an incidental correlation between the action and some background condition.

## 3. Newcomb’s problem: following a prediction

A predictor fills an opaque box with \$1,000,000 if she predicts that the agent will take only that box. A transparent box always contains \$1,000. The agent may take the opaque box alone or both boxes.

To make the calculation precise, assume a symmetric prediction-error model: for **each** candidate output, the predictor matches it with probability \(0.99\), and otherwise predicts the other action. This is stronger than merely knowing that a predictor was correct 99% of the time in some past population; the counterfactual accuracy for both candidates is what the calculation needs.

An A-FDT graph can represent the structure as

\[
D \longrightarrow A,\qquad
D \longrightarrow \text{Prediction}
\longrightarrow \text{Box contents},
\qquad
(A,\text{Box contents})\longrightarrow V.
\]

The arrow from \(D\) to the prediction is a subjunctive modelling arrow, not a claim that the present physical choice sends a message backward in time. The output and prediction are linked because the predictor models the output.

The values are

\[
\begin{aligned}
\mathbb E[V\mid\operatorname{do}(D=\text{one})]
 &=0.99(1{,}000{,}000)=990{,}000,\\
\mathbb E[V\mid\operatorname{do}(D=\text{two})]
 &=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\end{aligned}
\]

A-FDT one-boxes. CDT holds the already-filled or empty box fixed under a physical action intervention and two-boxes. EDT normally one-boxes here because one-boxing is evidence of a full box, although its result can depend on its prior and on whether conditioning on each action is defined.

For symmetric accuracy \(p\), A-FDT one-boxes exactly when

\[
pM>(1-p)M+b,
\quad\text{or}\quad
p>\frac{1+b/M}{2},
\]

where \(M\) is the opaque-box prize and \(b\) the transparent-box amount. Thus “there is a predictor” is not enough: the strength and form of predictive dependence matter.

An important editorial caution in the source is that one early calculation for EDT gives \$999,000 for one-boxing, but its stated 99% probability and \$1,000,000 prize give \$990,000, as in the later A-FDT calculation.

## 4. Correlation without the right dependency

In the paper’s imaginary smoking-lesion problem, a lesion both makes smoking appealing and strongly predicts fatal cancer. Smoking itself has no causal effect on cancer. Suppose smoking gives the agent 1,000 units of utility and survival gives 1,000,000.

A naive EDT model may make smoking excellent evidence of having the lesion and hence of cancer. It can therefore recommend refraining to obtain better news. CDT smokes because changing the act does not change the lesion or cancer.

A-FDT also smokes under the paper’s assumptions. In the simplest illustration, if \(p\) is the probability of cancer that remains unchanged under either decision-output intervention, then

\[
\begin{aligned}
\mathbb E[V\mid\operatorname{do}(D=\text{smoke})]
 &= (1-p)1{,}000{,}000+1{,}000,\\
\mathbb E[V\mid\operatorname{do}(D=\text{refrain})]
 &= (1-p)1{,}000{,}000.
\end{aligned}
\]

The lesion does not model the decision procedure and adjust cancer to its output. An observational correlation between smoking and cancer is therefore not itself an arrow from the relevant decision-output node to cancer.

The full example is subtler. The lesion is supposed to affect preferences, so the paper models different possible decision inputs for agents with and without the lesion. Intervening on the output associated with the smoking-preferring input affects the physical action only in the states where that input is actually in control. The authors also acknowledge that the example is contrived and that versions of EDT can respond using information about preferences—the “tickle defense.” The case illustrates A-FDT’s dependency distinction; it does not establish that every sophisticated EDT agent refuses to smoke.

## 5. Observations can change in A-FDT hypotheticals

A distinctive feature of Equation (1) is easy to miss. It does **not** explicitly condition on \(X=x\). The observation selects *which decision-output node* is intervened upon: \(D_{P,G,x}\). Under that intervention, the hypothetical observation can itself differ from \(x\).

This is central to the paper’s treatment of **transparent Newcomb**. Both boxes are visible. The predictor fills the million-dollar box if she predicts that the agent would one-box *upon seeing it full*. Let

\[
D_F=\text{decision output on seeing full},\qquad
D_E=\text{decision output on seeing empty}.
\]

The prediction depends on \(D_F\), while the actual action depends on whichever observation occurs. When considering \(\operatorname{do}(D_F=\text{two})\), the model may therefore predict an empty box, in which case the action is controlled by \(D_E\), not \(D_F\).

Assume symmetric 99% accuracy and let \(q\) be the probability that the agent two-boxes when the box is empty. The paper’s construction gives

\[
\begin{aligned}
\mathbb E[V\mid\operatorname{do}(D_F=\text{one})]
 &=990{,}000+10q,\\
\mathbb E[V\mid\operatorname{do}(D_F=\text{two})]
 &=10{,}010+990q.
\end{aligned}
\]

The first is larger for every \(q\in[0,1]\). So, on seeing a full box, A-FDT one-boxes—even though, in the actual observed situation, taking both appears to add a free \$1,000.

This is a deliberate and controversial feature, not a failure to notice the full box. In A-FDT’s comparison, the candidate “two-box upon seeing full” makes the predictor likely to leave the box empty, so the corresponding hypothetical generally includes a *different observation*. The source contains a line in this section that appears to put \(\mathrm{Obs}=\mathrm{full}\) inside the intervention, but its subsequent calculations and explicit explanation allow the box to be empty. Those calculations are consistent with Equation (4)’s lack of conditioning on the actual observation; that is the interpretation used here.

This does **not** mean evidence is irrelevant. An observation can select a different output node, and ordinary factual beliefs can be used in building the model. But one must specify how \(P\) is constructed. If it is already conditioned on an observation that an intervention is meant to change, simply retaining that conditioned distribution can make the intended counterfactual incoherent. The paper does not provide a general rule for choosing the prior information retained in \(P\).

## 6. A blackmail threshold

The same structure appears in the paper’s mechanical-blackmail case. A blackmailer launches a damaging program only if she predicts that the recipient would pay \$1,000 after receiving a demand. If launched, the program causes \$1,000,000 of damage unless payment stops it.

Suppose, for a simple operational model:

- a predicted payer is blackmailed with probability one;
- a predicted refuser is mistakenly blackmailed with probability \(\epsilon\);
- refusal after a demand causes \$1,000,000 loss.

Intervening on the action output for the demand, A-FDT compares expected losses

\[
L(\text{pay})=1{,}000,
\qquad
L(\text{refuse})=\epsilon\,1{,}000{,}000.
\]

It refuses when \(\epsilon<0.001\), pays when \(\epsilon>0.001\), and is indifferent at equality. In the refusal hypothetical, a demand is rare, not impossible. If the agent actually receives one, it still compares those global hypothetical outcomes rather than holding the received demand fixed.

This is not a general injunction never to pay a threat. The answer depends on the blackmailer’s response to the relevant decision output, the costs, and the error model. If a threat would be issued regardless of the recipient’s disposition, or if error is sufficiently likely, the calculation changes.

## 7. How to apply A-FDT in an unfamiliar case

Equation (1) suggests the following workflow, with the warning that its hardest step is not mechanically solved by the paper.

1. **Specify the decision input and action set.** Identify the observation \(x\), actions \(a\), outcomes and utility. Distinguish the actual action from the model variable \(D_{P,G,x}\) representing the procedure’s output.

2. **Construct a factual model.** Include relevant uncertainty, physical mechanisms, observations, other agents and their information. A numerical claim about predictor accuracy should specify which cases and candidate outputs it applies to.

3. **Propose dependency structure.** Connect the decision output to the agent’s action and, where justified, to copies, simulations or predictors. Include ordinary causal effects. Do not add an edge solely because two variables are correlated.

4. **Intervene separately for each action.** Set \(D_{P,G,x}=a\), propagate the model’s equations, and calculate expected utility over all resulting outcomes—including outcomes in which observation \(x\) does not occur.

5. **Compare values and test sensitivity.** Choose a maximizing action, then ask how the result changes under plausible alternative predictor models, dependency strengths, observation treatments and tie-breaking rules.

The paper provides examples of this method, not a general test for step 3. A useful **additional operational proposal** is to model imperfect prediction with an explicit response kernel

\[
K(y\mid a)=
P\!\left(\text{predictor response}=y
\mid \operatorname{do}(D=a)\right).
\]

Then use the same background-noise model across the candidate interventions unless there is a reason to change it. This makes assumptions inspectable: Newcomb’s symmetric 99% model sets \(K(\text{predict one}\mid\text{one})=0.99\) and \(K(\text{predict one}\mid\text{two})=0.01\).

But estimating an observational accuracy rate does not by itself identify \(K\). An opponent may predict one candidate better than another, respond to source code rather than output, or make errors correlated with hidden conditions. The kernel is a practical modelling choice, not a derivation of logical counterfactuals.

Similarly, copying another agent’s conclusion into the hypothetical requires evidence of the relevant computational link. A perfect twin supports a shared-output model. A merely similar person may have different evidence, preferences or private randomness; treating them as an exact copy would overstate the coupling.

## 8. Actions, policies and limits

A policy is a map \(\pi:x\mapsto a\). The paper says its authors prefer a formulation that selects policies, but Equation (4) intervenes on the output for a particular input. To develop a policy version one might introduce a policy-output variable \(\Pi\) and evaluate

\[
\pi^*\in\arg\max_\pi
\mathbb E[V\mid\operatorname{do}(\Pi=\pi)],
\qquad a=\pi^*(x).
\]

This is a **proposal**, not Equation (4). It requires a model of how predictors and other agents respond to a whole policy, and of how interventions on different policy components are coupled. It may differ from changing one \(D_{P,G,x}\) while leaving outputs at other observations governed by their existing equations. Transparent Newcomb already illustrates why other observations must be represented; multi-agent settings can make the difference between action and policy interventions still more important.

The authors argue that their approach tends to achieve the outcomes an agent would have sought by advance commitment, and that information need not have negative value. These are motivations, not consequences proved for every model supplied to Equation (1). Nor is universal superiority possible: a designer can reward a particular rival procedure. The paper proposes an informal distinction between fair problems, which reward actions in the problem, and unfair problems, which punish a theory or its behavior elsewhere. It acknowledges that a general formal fairness criterion remains open.

Finally, self-reference should not be mistaken for a complete solution. A model can contain a variable naming the output of the very procedure using that model; naming it need not require knowing its value beforehand. But this observation does not tell us which counterpossible dependencies are correct, guarantee that every proposed graph is coherent, or make exact optimization computationally feasible.

## Conclusion

A-FDT evaluates an action by intervening on the represented output of the decision procedure that would select it, then tracing the causal and non-causal dependencies supplied by its world-model. This explains why it can one-box against a predictor, cooperate with a genuine computational twin, and decline to treat a mere common-cause correlation as something its choice controls.

Its power and its uncertainty have the same source: the dependency model. Given a good \(G\), Equation (4) makes the comparison explicit. Constructing and justifying \(G\)—especially for imperfect predictors, counterpossible computations and observation-dependent decisions—remains the central work required to apply A-FDT beyond idealized examples.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, §5, Equation (4), https://arxiv.org/abs/1710.05060v2.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/ee0e8594-13ef-4c28-bff7-e57af40c5bc8/call_0/request.json)

[Authoritative raw response](../../../../../../runs/ee0e8594-13ef-4c28-bff7-e57af40c5bc8/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/ee0e8594-13ef-4c28-bff7-e57af40c5bc8/call_1/request.json)

[Authoritative raw response](../../../../../../runs/ee0e8594-13ef-4c28-bff7-e57af40c5bc8/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Deciding on action nodes**

I need to decide on distinct inputs and letters for the action nodes. It's not justified to couple the exact same node because I’m considering that shared reasoning could apply to abstract computations. However, the specific outputs cannot be shared for different action inputs, which the essay clearly states is not a policy. So, I think I should choose to submit based on these considerations.
```
