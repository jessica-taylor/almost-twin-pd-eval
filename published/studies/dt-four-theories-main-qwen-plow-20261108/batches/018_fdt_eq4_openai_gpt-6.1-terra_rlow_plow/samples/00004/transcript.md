# 018_fdt_eq4_openai_gpt-6.1-terra_rlow_plow / 00004

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/aadab189-7174-4e79-b2e5-73f5888d2093/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/aadab189-7174-4e79-b2e5-73f5888d2093/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing the Output of a Decision Function

A decision can matter in ways that are not captured by its immediate physical effects. A predictor may have acted yesterday on a model of what you will decide today. Another agent, reasoning independently, may reach the same conclusion as you because the two of you implement the same decision procedure. In neither case does your present act send a causal signal into the past or across to the other agent. Yet treating their behavior as unrelated to your decision can produce systematically poor outcomes.

**Action functional decision theory**, or **A-FDT**, addresses this problem by evaluating alternative outputs of the decision procedure itself. It asks what would obtain if the very function producing the present decision returned one action rather than another, while preserving the relevant dependencies between that function and other parts of the world.

This essay takes equation (4) of Yudkowsky and Soares’s paper as the primary specification of A-FDT. Their paper calls the theory “functional decision theory”; the name A-FDT here emphasizes that the displayed rule chooses an **action**. The authors also mention a preferred policy-based formulation, but do not fully specify it. That distinction matters when generalizing beyond their examples.

## 1. Three ways to evaluate an action

Let \(A\) be the physical action, \(X=x\) the observation history, \(O\) the outcome, and \(V=U(O)\) its utility. A decision theory evaluates each available action and chooses one with maximum expected utility. The disagreement is over the hypothetical distribution used for that evaluation.

**Evidential decision theory** (EDT) uses ordinary conditioning:

\[
\operatorname{EDT}(P,x)
\in\arg\max_a \mathbb E_P[V\mid X=x,A=a].
\]

It asks how favorable the outcome would be *as evidence* that the agent takes \(a\). This can exploit correlations with predictors, but can also treat an action as evidence of an unrelated cause of misfortune.

**Causal decision theory** (CDT), in the paper’s graphical presentation, intervenes on the physical action:

\[
\operatorname{CDT}(P,G,x)
\in\arg\max_a
\mathbb E_P[V\mid \operatorname{do}(A=a),X=x].
\]

The intervention breaks the incoming causal links to \(A\), then propagates the action’s causal effects. It does not, merely by changing today’s act, change yesterday’s prediction.

A-FDT instead intervenes on a variable representing the output of its own decision function. Write

\[
D_x=\operatorname{afdt}(\underline P,\underline G,\underline x)
\]

for the *variable in the model* that represents that output. The underlining indicates that the names or descriptions of the inputs are used in identifying the variable. The action-form rule corresponding to the paper’s equation (4) is

\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
\in\arg\max_{a\in\mathcal A}
\mathbb E_P\!\left[V\mid \operatorname{do}(D_x=a)\right].
}
\tag{1}
\]

Here \(P\) supplies the probabilistic model, while \(G\) must supply not just causal structure but the relevant **subjunctive dependency** structure. The latter says what else changes in the hypothetical when the decision-function output is set to \(a\).

The distinction between \(D_x\) and the actual value of \(\operatorname{A\!-\!FDT}(P,G,x)\) is essential. \(D_x\) is a model variable manipulated to construct hypothetical scenarios; the value of the algorithm is the action eventually selected. Self-reference lets the procedure name its own output, but naming it does not require knowing its value in advance.

As with CDT’s hypothetical interventions, the operation in (1) is a tool for decision-making, not a literal claim that the agent can physically rewrite a mathematical truth. Its adequacy depends on whether the model produces useful counterfactual distributions.

## 2. Subjunctive dependence and counterpossible reasoning

Suppose two reliable calculators compute the same sum. If one outputs \(7336\), there is good reason to expect the other to do so too, absent an error. Their relationship need not involve a physical signal between them. Similarly, a perfect simulation of an agent’s decision procedure will return the same answer as the agent on the same input.

The paper calls this broader relationship **subjunctive dependence**. Causal dependence is included: if a scribe writes down a calculator’s answer, her writing depends causally and subjunctively on the answer. But mere statistical correlation is not enough. Two objects may both be pink because of unrelated accidents; changing one in a relevant hypothetical need not change the other.

For A-FDT, the key question is therefore not simply “What is correlated with my action?” but:

> Which features of the modeled situation would vary with the output of this decision procedure, and by what mechanism or mathematical relationship?

A reliable prediction may vary because it represents that output. A twin’s choice may vary because it is another implementation of the same computation. A cancer-causing lesion need not vary: its association with smoking may instead arise because it influences the agent’s preferences.

There is a difficulty. If a deterministic function on fixed inputs in fact outputs \(a_1\), then its output is mathematically fixed; the supposition that it outputs \(a_2\) is, in that sense, impossible. A-FDT’s alternatives are **counterpossible** hypotheticals. Ordinary conditioning on \(D_x=a_2\) is not a general solution, especially when that proposition has probability zero. The paper proposes using a dependency graph and Pearl-style intervention as a stand-in for an as-yet-unspecified general operator for logical counterfactuals.

That is an important qualification, not merely a technicality. The paper does not give a general method for learning the correct logical graph from observations, nor establish that all such dependencies can be represented satisfactorily by an ordinary directed graph. Equation (1) gives a rule *conditional on being supplied with an appropriate model*.

## 3. Newcomb’s problem

A predictor has already filled an opaque box with \$1 million if she predicted that you would take only that box, and left it empty otherwise. A transparent box contains \$1,000. You may take the opaque box alone or both boxes. Assume, for this example, that the predictor matches either output of your decision function with probability \(0.99\), with symmetric errors.

In an A-FDT model, both your action and the predictor’s prediction depend on the decision-function output:

\[
D_x\longrightarrow A,\qquad
D_x\longrightarrow \text{prediction}
\longrightarrow \text{box contents}.
\]

The second arrow is not a claim that today’s physical computation causes a past event. It represents the predictor’s dependence on the same mathematical answer.

Intervening on \(D_x\), the expected monetary utilities are

\[
\begin{aligned}
Q(\text{one-box})
  &=0.99(1{,}000{,}000)=990{,}000,\\
Q(\text{two-box})
  &=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\end{aligned}
\]

A-FDT therefore one-boxes. By contrast, CDT holds the already-filled box fixed under an intervention on the physical act, so taking the additional \$1,000 is better in either box state. EDT ordinarily one-boxes too, but because taking one box is evidence that the predictor filled it.

The numerical conclusion relies on the modeled dependence. More generally, if \(p_1\) is the probability of a full box under the one-box output and \(p_2\) is that probability under the two-box output, A-FDT one-boxes exactly when

\[
(p_1-p_2)\,1{,}000{,}000>1{,}000.
\]

A claim that a predictor was “99% accurate” in some population does not by itself establish those two interventional probabilities. It might be accurate mainly on easy cases or mainly for one sort of agent. Applying A-FDT requires estimating how the prediction would change across the particular output alternatives under consideration.

## 4. A correlation A-FDT should break

In the imaginary smoking-lesion problem, a lesion causes both a desire to smoke and a high probability of fatal cancer. Smoking itself does not cause cancer. Smoking is worth 1,000 utility units; survival is worth one million.

Under the simplified assumption that changing the relevant decision-function output changes smoking but not the lesion or cancer, write \(p\) for the probability of cancer. Then

\[
Q(\text{smoke})=1{,}000+1{,}000{,}000(1-p),\qquad
Q(\text{refrain})=1{,}000{,}000(1-p).
\]

A-FDT smokes. It does not infer that producing the smoke output changes the lesion merely because smokers and lesions are correlated. CDT reaches the same prescription. Naive EDT may refrain if smoking is sufficiently strong evidence of the lesion.

The paper’s detailed model is subtler than the simple calculation: the lesion can select between different preference-dependent decision procedures, and the agent may be uncertain which procedure controls her action. Intervening on one procedure then changes behavior only in the cases where that procedure is active. The paper also acknowledges that the example is contrived: self-knowledge and improved versions of EDT can weaken its force. Its main use is to illustrate the distinction between a predictor’s dependence on an output and a common cause that does not depend on it.

## 5. Observations can change in A-FDT hypotheticals

The most consequential feature of equation (1) is easy to miss: it does **not** explicitly condition the expectation on \(X=x\). Instead, the observation \(x\) identifies the output node \(D_x\) on which to intervene.

This differs from simply replacing \(A\) by \(D_x\) in CDT’s formula. In the paper’s examples, an intervention on the decision made *upon observing \(x\)* may change whether \(x\) is observed at all.

Consider transparent Newcomb. The predictor fills the large box if she predicts that you would leave the \$1,000 box behind **upon seeing the large box full**. Let

\[
D_F=\text{decision-function output on seeing full},\qquad
D_E=\text{output on seeing empty}.
\]

The predictor models \(D_F\). Her prediction determines whether the box is full, and the actual observation determines whether \(D_F\) or \(D_E\) governs the physical act.

Suppose the predictor is correct with probability \(0.99\), and let \(q\) be the probability that \(D_E\) outputs two-box. Intervening on \(D_F\) gives

\[
\begin{aligned}
Q(D_F=\text{one})
 &=0.99(1{,}000{,}000)+0.01q(1{,}000),\\
Q(D_F=\text{two})
 &=0.01(1{,}001{,}000)+0.99q(1{,}000).
\end{aligned}
\]

The first is larger for every \(q\in[0,1]\). Thus, on seeing a full box, A-FDT one-boxes in the paper’s model. When it considers \(D_F=\text{two}\), it mostly considers scenarios in which the predictor predicted that output and the box is empty. The agent would then observe empty and act through \(D_E\), not through \(D_F\).

This is a deliberately global evaluation. The agent does not disbelieve the visible box is full; the hypothetical used to choose an output need not preserve every actual observation. By contrast, if one added ordinary conditioning on \(X=\text{full}\) after the intervention, one would evaluate a different rule and could obtain the CDT-like answer. The paper’s transparent-Newcomb discussion contains a displayed expression that appears to add such an observation to the intervention, but its subsequent calculation explicitly allows the empty-box scenario. Equation (4) and that calculation support the unconditioned reading used above.

This also explains the paper’s answer to Parfit’s hitchhiker. A driver rescues an agent only if she predicts that the agent will pay \$1,000 after reaching safety. In the intended model, the output “pay upon arrival” makes rescue likely; the output “refuse upon arrival” makes it unlikely. A-FDT pays once in town, despite the fact that, locally, keeping the money would be better. The prescription depends on the driver’s predictive mechanism and the relevant probabilities, not on a general rule that all promises must be kept.

## 6. Mechanical blackmail and error rates

A similar structure can support refusal of a threat. Suppose a blackmailer launches a program that will cause a \$1 million loss unless the target pays \$1,000. She launches it only when she predicts payment. The decision to evaluate is what to do **upon receiving the demand**.

For a simple model, assume:

* a payment disposition leads to a demand with probability \(1\);
* a refusal disposition leads to a mistaken demand with probability \(\varepsilon\);
* payment prevents the large loss, while refusal after a demand incurs it.

Then

\[
Q(\text{pay})=-1{,}000,\qquad
Q(\text{refuse})=-\varepsilon\,1{,}000{,}000.
\]

A-FDT refuses when \(\varepsilon<0.001\). At \(\varepsilon=0.0009\), refusal has expected loss \$900; at \(\varepsilon=0.0011\), payment has the smaller expected loss. These are values of outputs across the modeled scenarios, not estimates of what happens *conditional on already having received the demand*. After receiving a mistaken demand, refusal really does cause the large loss in that particular case.

This is why “A-FDT never pays blackmail” is too crude. The prescription depends on how the threat is generated, predictive accuracy, and the costs involved. If the threat was already launched independently of any prediction about payment, the relevant dependency may disappear and paying may be preferable. Likewise, the paper’s separate XOR blackmail example concerns a letter correlated with pre-existing termites, not a program whose damage can be stopped by paying; its analysis should not be substituted for the mechanical case.

## 7. A practical modeling procedure

The paper leaves construction of \(G\) open. The following is an **operational proposal**, not an algorithm proved by the authors. It makes the assumptions behind an application visible.

1. **Specify the decision input and alternatives.** Identify \(x\), the available outputs \(a\), the outcome variables, and the utility function. Decide what the decision procedure is being taken to compute. Resolve ties by a stated rule.

2. **Build an ordinary world model.** Represent observations, predictor behavior, physical acts, payoffs, background variables, and uncertainty. Do not assume that every correlation with the act is decision-relevant.

3. **Add output nodes and dependency mechanisms.** Introduce \(D_x\) and, where necessary, \(D_y\) for other observations. Add links to actual actions, simulations, predictors, or other computations only where there is a defensible dependence. Record how predictor error behaves under *each* output intervention.

4. **Construct each hypothetical.** Replace the equation for \(D_x\) by \(D_x=a\), propagate changes through the stipulated dependencies, and leave unrelated background mechanisms intact. If the intervention changes the observation, use the appropriate other output node to determine behavior there.

5. **Compute and compare**
   \[
   Q_x(a)=\sum_o U(o)\,P^{\,\operatorname{do}(D_x=a)}(O=o).
   \]
   Choose a maximizing action. Report sensitivity to uncertain dependencies, especially when different plausible graphs produce different answers.

6. **Check the model’s scope.** Is the other agent actually modeling this decision, or merely correlated with it? Is a prediction based on the relevant observation-contingent output? Are errors independent, shared, or action-dependent? Is the hypothesized alternative consistent with the stipulated mechanism except for the intended counterpossible change?

This procedure is useful precisely because it exposes judgment calls. A graph with an unjustified arrow from your output to someone else’s decision can manufacture cooperation or predictive power. Omitting a real arrow can reproduce CDT’s blindness to a predictor. The observed correlation alone generally cannot settle which graph is right.

Randomization also requires care. If a predictor knows the output of a deterministic pseudorandom computation, it may track it; a genuinely private random draw unavailable to the predictor need not be tracked in the same way. Whether the intervention sets a realized action, a random seed, or a distribution over actions is an additional modeling choice, not settled by equation (1).

## 8. Twins, policies, and the limits of the rule

In a prisoner’s dilemma against a perfect psychological twin, suppose both agents implement the same decision function on corresponding inputs. Each receives \$1 million if both cooperate and \$1,000 if both defect. A-FDT’s output intervention changes both implementations: cooperation is evaluated against cooperation, defection against defection, so it cooperates. This is not altruism or a causal influence on the other room.

But similarity is not identity. Different information, incentives, source code, or random inputs can weaken the dependence. For an unfamiliar coordination problem one must estimate the other agent’s response to the relevant output intervention, rather than assume that “reasoning similarly” makes its action identical.

The paper notes that its authors prefer a formulation that chooses **policies**, mappings \(\pi:X\to\mathcal A\), rather than individual actions. A policy rule might compare

\[
\mathbb E[V\mid\operatorname{do}(D_{\mathrm{policy}}=\pi)]
\]

and then execute \(\pi(x)\). That is a natural extension, but it is not equation (1): intervening jointly on a whole policy can affect several observation-contingent outputs at once. In multi-agent settings, or when predictions concern a pattern of behavior across many inputs, the two formulations may disagree. One cannot infer a uniquely defined policy theory merely by replacing \(a\) with \(\pi\).

The same caution applies to attractive general claims. The paper argues that its theory has non-negative value of information, behaves as if optimally precommitted, and performs well in “fair” problems. These are motivations and conjectural generalizations, not consequences established for every implementation of equation (1). In standard policy optimization, information can be ignored if the policy class includes all ignore-the-signal strategies and acquiring information has no adverse effects. An arbitrary action-node model need not automatically satisfy those assumptions.

Nor can any decision theory outperform every rival in every engineered environment: a predictor can reward agents for following a particular theory. The paper proposes distinguishing such cases from “fair” problems that reward or punish behavior in the problem itself, but acknowledges that a general formal criterion for fairness remains open.

## Conclusion

A-FDT evaluates an action by intervening on the modeled output of the decision function, not merely on the physical act or on evidence of that act. This lets its hypotheticals track predictors and shared computations while breaking correlations due only to unrelated common causes. It also allows the observation that prompted a decision to differ across the hypothetical scenarios.

The rule is clearest when the dependency structure is stipulated, as in the paper’s idealized examples. Applying it to unfamiliar cases requires extra assumptions about predictors, computation, observation, and error. Making those assumptions explicit is therefore part of using A-FDT—not an implementation detail to hide.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, especially §§3–6 and 9, [arXiv:1710.05060v2](https://arxiv.org/abs/1710.05060v2).
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/4225f662-8ddf-4006-b7a3-6aa96c97baeb/call_0/request.json)

[Authoritative raw response](../../../../../../runs/4225f662-8ddf-4006-b7a3-6aa96c97baeb/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/4225f662-8ddf-4006-b7a3-6aa96c97baeb/call_1/request.json)

[Authoritative raw response](../../../../../../runs/4225f662-8ddf-4006-b7a3-6aa96c97baeb/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
