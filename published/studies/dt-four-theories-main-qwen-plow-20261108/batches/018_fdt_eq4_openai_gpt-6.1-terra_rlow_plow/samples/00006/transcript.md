# 018_fdt_eq4_openai_gpt-6.1-terra_rlow_plow / 00006

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/60a79ab9-52c3-4c81-adeb-e525e908143b/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/60a79ab9-52c3-4c81-adeb-e525e908143b/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing the Output of a Decision Function

Suppose you and an exact psychological twin play a prisoner’s dilemma in separate rooms. Each chooses cooperate or defect. Mutual cooperation pays each of you $1,000,000; mutual defection pays $1,000 each. A lone defector receives $1,001,000, while the cooperator receives nothing.

Your physical choice cannot send a signal to your twin. Nevertheless, you know that she is reasoning in exactly the same way as you, with the same information. If your shared reasoning concludes “cooperate,” both of you cooperate; if it concludes “defect,” both defect. Is the right comparison therefore $1,000,000 versus $1,000—or should you hold your twin’s choice fixed and take the extra $1,000 by defecting?

**Action functional decision theory (A-FDT)** takes the first comparison seriously. It evaluates an action by considering what would follow if the *decision function* currently being evaluated had that output, including consequences for other systems that depend on the same computation. This is not a claim that a present action physically causes a distant twin’s action. It is a claim about which dependencies should be represented in a decision hypothetical.

The reference paper presents a broader theory under the name functional decision theory. Here “A-FDT” denotes its action-based formulation, specifically Equation (4) of Section 5. The paper notes that its authors prefer a formulation that selects policies rather than individual actions; that distinction matters when applying the theory beyond the examples in the paper.

## 1. Decision hypotheticals

Let \(\mathcal A\) be a finite action set, \(O\) an outcome, and \(V=U(O)\) its utility. An expected-utility decision rule assigns each candidate action a hypothetical distribution over outcomes and chooses a maximizer:

\[
a^*\in\arg\max_{a\in\mathcal A}
\sum_o P_a(O=o)\,U(o).
\]

The important question is how to construct \(P_a\). A hypothetical is a tool for choosing, not necessarily a belief that the imagined scenario is physically or logically possible.

Two familiar answers are:

- **Evidential decision theory (EDT):** evaluate \(a\) by conditioning on the proposition that the agent takes it:
  \[
  \mathbb E[V\mid X=x,A=a].
  \]
- **Causal decision theory (CDT):** intervene on the physical action \(A\), allowing its causal effects to change while holding causally upstream facts fixed:
  \[
  \mathbb E[V\mid \operatorname{do}(A=a),X=x].
  \]

A-FDT instead intervenes on a representation of the output of the agent’s decision computation. Thus it can preserve a connection between its action and a predictor’s earlier model of that action, without preserving every statistical correlation between action and environment.

## 2. The A-FDT equation

Let \(P\) be a probabilistic world-model, \(G\) a graph describing decision-relevant dependencies, and \(x\) the agent’s observation history. Write

\[
D_x=\mathsf{afd}(\underline P,\underline G,\underline x)
\]

for a **variable in the model** representing the output of the A-FDT procedure on those inputs. The underlining indicates that the inputs identify the variable; \(D_x\) is not itself the action returned by the algorithm.

The paper’s Equation (4), in this notation, is

\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
\in\arg\max_{a\in\mathcal A}
\mathbb E_{P,G}\!\left[
V\mid\operatorname{do}(D_x=a)
\right].
}
\tag{A-FDT}
\]

The intervention replaces the rule determining \(D_x\) with the constant \(a\). Variables downstream in \(G\) are then recomputed, while variables not affected by that intervention retain their modeled distributions. In a simple application, \(D_x\) affects the physical action; it may also affect a predictor, a copy of the agent, or a later action.

This is graph surgery resembling Pearl’s causal intervention, but \(G\) is **not merely a causal graph**. It is supposed to encode logical, computational, and other relevant *subjunctive dependencies*, as well as causal ones. An arrow from \(D_x\) to a predictor’s earlier prediction is not an arrow for a backwards-in-time physical signal.

The self-reference is deliberate. The procedure evaluates a variable representing its own output. Naming that variable does not require knowing its value in advance; the paper invokes self-referential constructions such as quining to illustrate the point. But being able to name the variable does not solve the harder question of how to construct the correct dependency graph.

Notice also what is **not** in Equation (A-FDT): an explicit condition \(X=x\). Observation selects the decision-output node \(D_x\). The reference paper emphasizes this contrast with CDT’s conditioning on the observation. In particular, the hypothetical under an intervention on \(D_x\) can assign probability to worlds in which observation \(x\) does not occur. This feature is central to the paper’s treatment of transparent Newcomb and blackmail.

## 3. Subjunctive dependence, not correlation alone

The paper calls a relationship *subjunctive dependence* when changing a decision-function output in the relevant hypothetical calls for a corresponding change elsewhere. Causal dependence is included: if an action causes a lamp to turn on, the lamp changes when the action changes. But the relation can also connect implementations of the same computation, or a computation and an accurate prediction of it.

Two reliable calculators evaluating the same expression need not communicate. Still, a model of their outputs should reflect the common calculation. Likewise, a predictor who accurately models an agent may produce a different prediction in the hypothetical where the modeled decision computation outputs a different action.

By contrast, correlation alone is insufficient. In the imaginary smoking-lesion problem, a lesion produces both a desire to smoke and a high risk of cancer; smoking itself has no causal effect on cancer. The lesion does not predict or implement the agent’s decision computation. In the paper’s A-FDT graph, intervening on that computation does not change whether the lesion exists. If smoking gives the agent $1,000 in utility and has no other effects, smoking is better by $1,000 in a simple model where the intervened-on computation controls the action.

The paper’s more detailed lesion model makes a subtler point. If the lesion determines which of two decision computations is actually implemented, intervening on only one computation changes the action only in the corresponding cases. With lesion probability \(p\), its calculated advantage for smoking is \(p\cdot \$1{,}000\), rather than $1,000. The paper also concedes that the classic lesion case is contrived: an accurate model of the agent’s preferences and deliberation can weaken the correlation on which the standard EDT diagnosis relies.

The practical distinction is therefore not “predictors matter, correlations do not” as a slogan. The task is to model **which features would change under an intervention on this particular computation**, and which would not.

## 4. A-FDT on opaque Newcomb

In Newcomb’s problem, box A contains $1,000. Opaque box B contains $1,000,000 if a predictor predicted that the agent would take only B, and nothing otherwise. The prediction was made before the agent chooses.

Consider the following explicit model:

\[
A=D,\qquad
Y=
\begin{cases}
D,&E=1,\\
\text{the other action},&E=0,
\end{cases}
\qquad
B=\mathbf 1\{Y=\text{one-box}\},
\]

where \(D\) is the modeled decision output and \(P(E=1)=0.99\). The outcome pays \(1{,}000{,}000B\), plus $1,000 if the agent takes both boxes.

Under A-FDT’s two interventions,

\[
\begin{aligned}
\mathbb E[V\mid\operatorname{do}(D=\text{one})]
  &=0.99(1{,}000{,}000)=990{,}000,\\
\mathbb E[V\mid\operatorname{do}(D=\text{two})]
  &=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\end{aligned}
\]

A-FDT one-boxes. CDT instead holds the already-filled box fixed under an intervention on the physical act and two-boxes. Standard EDT also one-boxes under suitable nonzero priors, but does so by conditioning on the action rather than by intervening on its computation.

The numerical conclusion requires more than an aggregate claim that the predictor is right 99% of the time in some population. The model assumes the stated accuracy relationship holds **under both decision-function interventions**. If the predictor’s counterfactual accuracy differs between one-boxers and two-boxers, let the relevant probabilities that B is full be \(p_1\) and \(p_2\). A-FDT one-boxes exactly when

\[
1{,}000{,}000p_1
>
1{,}000{,}000p_2+1{,}000.
\]

Estimating \(p_1-p_2\) is therefore part of the problem, not a consequence of the equation alone.

## 5. Observation-dependent decisions

The most surprising application is transparent Newcomb. The agent sees whether B is full. The predictor fills B if it predicts that the agent would one-box *upon seeing B full*.

Define two output variables:

\[
D_F=\mathsf{afd}(P,G,\text{full}),\qquad
D_E=\mathsf{afd}(P,G,\text{empty}).
\]

The predictor models \(D_F\), and the actual action is \(D_F\) if the box is full and \(D_E\) if it is empty. Suppose the predictor gets \(D_F\) right with probability \(0.99\), and let \(q\) be the probability that \(D_E\) outputs two-box.

When the agent actually sees a full box, Equation (A-FDT) selects \(D_F\) as the intervention target. Its hypothetical values are

\[
\begin{aligned}
V_F(\text{one})
&=0.99(1{,}000{,}000)+0.01q(1{,}000),\\
V_F(\text{two})
&=0.01(1{,}001{,}000)+0.99q(1{,}000).
\end{aligned}
\]

The one-box value is larger for every \(q\in[0,1]\). Thus A-FDT one-boxes even after seeing B full. In the second hypothetical, the intervention makes it likely that the predictor predicted two-boxing, so B is likely empty and the *other* output variable \(D_E\) determines the action. The hypothetical need not preserve the observation that selected \(D_F\).

There is a notational inconsistency in the paper’s Section 6: its displayed expression for this example includes an observation intervention, while its accompanying calculation allows the observation to vary. The calculation and the paper’s explicit explanation match Equation (4)’s absence of a fixed-observation condition. That is the interpretation used here.

The same structure explains Parfit’s hitchhiker. A driver rescues an agent only if she predicts the agent will pay $1,000 after reaching town. If the modeled dependence is sufficiently accurate, A-FDT evaluates the town-payment output partly through its effect on whether the ride occurs, and pays upon arrival. This is not because payment now changes the past; it is because the compared computations are associated with different past predictions.

## 6. Blackmail and the cost of being predictable

Consider mechanical blackmail: a predictor runs a damaging program only if it predicts the recipient will pay $1,000 to stop it. If run and not stopped, the program causes $1,000,000 in damage.

Assume, for illustration, that a predicted payer is always blackmailed, while a predicted refuser is blackmailed by mistake with probability \(\varepsilon\). Intervening on the output for *receiving the letter* gives

\[
\begin{aligned}
\text{expected loss if that output is pay}&=1{,}000,\\
\text{expected loss if that output is refuse}&=\varepsilon(1{,}000{,}000).
\end{aligned}
\]

A-FDT refuses when \(\varepsilon<0.001\), is indifferent at equality, and pays when \(\varepsilon>0.001\), under these assumptions. At \(\varepsilon=0.0009\), refusal has an expected loss of $900, despite being disastrous in the rare actual case where the letter arrives.

This example shows both A-FDT’s motivation and its controversy. It seeks the better *global pattern* of outcomes, even when the actual recipient knows the threat is already underway. The answer also depends on the blackmailer’s response function: a blackmailer who runs the program regardless of prediction does not create the same reason to refuse.

## 7. Applying A-FDT to an unfamiliar problem

Equation (A-FDT) is a decision rule conditional on a model, not a complete method for discovering the model. A disciplined application can proceed as follows.

1. **Specify outcomes and utility.** Include costs of actions, mistakes, observations and other agents’ responses. Utilities need not be monetary.
2. **Identify the output being evaluated.** What observation history \(x\) indexes \(D_x\)? Which physical acts implement that output, and in which contingencies might another output \(D_y\) control behavior?
3. **Model dependencies.** Represent actual causal effects, predictors, copies and their imperfections. Do not add a logical connection merely because two actions are correlated.
4. **Construct one intervention per candidate action.** Set \(D_x=a\), propagate the graph, and calculate expected utility across all resulting contingencies—including contingencies where \(x\) does not occur, if the model makes it downstream of the intervention.
5. **Compare, check sensitivity, and choose.** Vary uncertain predictor responses and dependency assumptions. If the ranking changes under plausible models, report that the prescription is model-dependent.

A reasonable **additional operational proposal** is to retain genuinely exogenous background evidence when building \(P\), while representing evidence that a decision output might affect as a variable inside \(G\). This helps separate an independent test result from the observation of a box whose contents are determined by a prediction. But the paper does not supply a general rule deciding which evidence belongs in each category. Preconditioning on an observation that the intervention should alter could erase precisely the dependency A-FDT is meant to preserve.

Imperfect similarity needs comparable care. A twin who shares code and input supports a strong dependency; a stranger who merely shares a goal may not. For imperfect prediction, the relevant inputs are conditional response functions under interventions, not just observed correlations or average accuracy. Randomization also requires a model: a predictor may know the distribution of a private random choice without knowing its realization, or may be able to predict a pseudorandom seed.

## 8. Actions, policies, and open problems

A policy is a map \(\pi:\mathcal X\to\mathcal A\). One might propose evaluating policies by intervening on a policy-output variable \(\Pi\) and selecting

\[
\pi^*\in\arg\max_{\pi}
\mathbb E[V\mid\operatorname{do}(\Pi=\pi)],
\qquad a=\pi^*(x).
\]

This is a useful way to reason about coordinated behavior across observations, but it is an **extension**, not Equation (A-FDT). The paper explicitly notes its authors’ preference for policy selection and says the distinction can matter in multi-agent problems. Policy search can coordinate changes at several inputs; the action equation intervenes on the output indexed by one input. Their answers need not coincide unless further relationships are specified.

There is also a deeper counterfactual difficulty. If a deterministic decision function in fact outputs \(a\), its output on the same inputs is fixed as a matter of mathematics. Asking what follows if it outputs \(b\ne a\) is therefore a *counterpossible*: its antecedent is logically false. Ordinary conditioning on that antecedent may be undefined. The graph is meant to provide a useful local surgery without requiring a general logic of counterpossibles, but the paper acknowledges that it does not show how to infer the appropriate graph, or whether Pearl-style graphs can adequately represent all such dependencies.

Finally, favorable examples do not prove universal optimality. The paper argues that Newcomb-like problems are fair tests because predictors reward actions rather than a theory’s name, and claims that A-FDT performs well in such cases. It also recognizes that any theory can be targeted by an adversarial problem and leaves a precise definition of “fair” open. Similarly, its claims about positive value of information, precommitment and reflective stability are motivations, not general theorems supplied by Equation (4). They depend on modeling choices and on what alternative policies are available.

## Conclusion

A-FDT’s central move is to evaluate an action as the output of a decision computation, then propagate the modeled consequences of that output—not merely the physical consequences of a bodily act or the evidential consequences of learning which act occurred. This explains its characteristic choices in Newcomb, twin cooperation and prediction-based threats.

The equation is precise once a suitable model and dependency graph are supplied. Constructing and justifying that graph, particularly for imperfect predictors and observation-dependent counterpossibles, remains the central unfinished part of the theory.

**Reference:** Eliezer Yudkowsky and Nate Soares, [*Functional Decision Theory: A New Theory of Instrumental Rationality*](https://arxiv.org/abs/1710.05060v2), especially Sections 3–6.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Planning lengthy submission**

I'm looking to deliver around 2400 words for this task. I need to address a couple of things, like an inconsistency equation in section 6 that has a typo, plus there’s that arithmetic value of 0.011 I need to clarify. I also want to focus on transparent calculations and make sure to include operational observations while noting any conditioning caveats. So I really need to write through this carefully to get everything right!
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/779df01a-7315-4057-a76b-9b6b7941ce97/call_0/request.json)

[Authoritative raw response](../../../../../../runs/779df01a-7315-4057-a76b-9b6b7941ce97/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing input-output relationships**

I’m thinking about how different inputs lead to distinct output actions without an apparent reason for each. It’s interesting that even though shared reasoning is involved, each input is unique, and it feels like there should be a model to capture that. However, intervention for specific output isn't a common policy, and without explicit grounds for dependency, I notice potential defects in this setup. It’s all quite intriguing to consider!
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/779df01a-7315-4057-a76b-9b6b7941ce97/call_1/request.json)

[Authoritative raw response](../../../../../../runs/779df01a-7315-4057-a76b-9b6b7941ce97/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Evaluating dependencies in outputs**

I need to figure out how differing x values impact distinct D_x; there's no specific dependence laid out. The same code might be structured symmetrically and still rely on abstract decisions, even if the outputs differ. Intervening in the exact output linked to a specific letter won't affect other functions. I realize that shared reasoning can involve common subcomputations, but changing D_x outputs doesn’t influence common upstream calculations. So, I guess I’ll submit what I've concluded!
```
