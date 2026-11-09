# 026_fdt_policy_openai_gpt-6.1-terra_rlow_plow / 00009

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/e8b812ca-ae04-46a3-9a3b-ce4e3162f902/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/e8b812ca-ae04-46a3-9a3b-ce4e3162f902/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: choosing a policy as the output of a decision function

A decision can be viewed in two ways. One can ask which physical action will have the best consequences, holding the rest of the world fixed except for that action’s causal effects. Or one can ask which conclusion a decision procedure should reach, taking into account that other processes may predict, simulate, or share that procedure.

**Policy functional decision theory (P-FDT)** develops the second perspective at the level of policies. Instead of directly choosing an action, it evaluates possible mappings from inputs to actions, selects a policy, and applies that policy to the input actually received. Its motivation is that a policy’s consequences can include not only what its user physically does, but also what predictors and other implementations of related computations do.

The primary source here is footnote 16 of Yudkowsky and Soares’ *Functional Decision Theory*. It says that their preferred formulation intervenes on the decision-function node to choose “not an action but a *policy* which maps inputs to actions,” which is then applied to the agent’s inputs. The paper’s main text instead develops a simpler action-selection formulation. Footnote 7 likewise mentions policies and says the distinction can matter in multi-agent dilemmas.

Those passages state the central idea, but they do not give a complete policy-level algorithm. In particular, they leave open how policy selection is anchored in the agent’s information, which other computations change under a policy intervention, and how ties and repeated selection are handled. The mathematical procedure below is therefore an **operational interpretation**, not a formula asserted by the paper. Its aim is to make the footnote usable while preserving the paper’s treatment of functional counterfactuals.

## 1. Policies and functional counterfactuals

Let \(\mathcal X\) be a set of possible inputs and \(\mathcal A\) a set of actions. A deterministic policy is a function

\[
\pi:\mathcal X\longrightarrow\mathcal A.
\]

An input might include an observation history, a role in a game, available actions, and other information the agent can use. A policy says what to do at *each* input in its domain, including inputs that will not in fact be encountered.

Suppose a policy-selection computation \(D\) takes a specification \(s\)—including a world-model, utility function, and description of candidate policies—and returns a policy:

\[
D(s)=\pi^*.
\]

On receiving input \(x\), the agent acts by computing \(\pi^*(x)\). The crucial P-FDT question is:

> What would the modeled consequences be if this very policy-selection computation returned \(\pi\)?

The emphasis on *this very computation* matters. The paper’s functional perspective does not merely ask what would happen if the agent physically replaced its software with some other policy. It asks how the world would differ under a hypothetical change in the output of the decision computation, while preserving relevant dependencies on that output.

Such a hypothetical can be **counterpossible**. If \(D\) is deterministic and \(s\) is fixed, there is one actual mathematical value of \(D(s)\). For an alternative \(\pi\ne D(s)\), the supposition \(D(s)=\pi\) contradicts that mathematical fact. Nevertheless, the paper treats these suppositions as decision-making tools: imagined models need not be beliefs that the impossible antecedent is actually true.

The source proposes using a graph augmented with logical, computational, and causal dependencies. Its action-level model intervenes on a variable representing a decision function’s output and propagates consequences through that graph. The unresolved problem is how to construct such a graph, especially for imperfect predictors and approximate computations. A policy-level account inherits that problem.

## 2. An operational P-FDT rule

Choose a **planning anchor** \(k\): the information taken as fixed when comparing candidate policies. Let \(M_k\) be the world-model at that anchor, \(\Pi\) the candidate policy class, and \(U\) the agent’s utility over outcomes. Introduce a model variable \(Q\) representing the output of the policy selector \(D(s_k)\).

For each candidate \(\pi\), construct a hypothetical distribution

\[
\mathsf H_\pi
\;=\;
\mathsf H\!\left(M_k;\operatorname{set}(Q=\pi)\right).
\]

Here \(\operatorname{set}\) denotes **functional intervention**: replace the modeled output of the selector with \(\pi\), then propagate the effects through dependencies represented in the model. It is not automatically ordinary conditioning on \(Q=\pi\), nor merely a causal intervention on one physical action.

The proposed rule is

\[
V_k(\pi)=\mathbb E_{\mathsf H_\pi}[U],
\qquad
\pi^*\in\operatorname*{arg\,max}_{\pi\in\Pi}V_k(\pi),
\qquad
a=\pi^*(x_{\rm actual}).
\]

A fixed tie-breaking rule makes the selection determinate when several policies have equal value. For a finite model, the first equation can be written

\[
V_k(\pi)=\sum_o \mathsf H_\pi(o)\,U(o).
\]

This is expected-utility maximization, but with a distinctive account of the hypothetical distribution. The source’s main text makes the analogous claim for its action-level formulation: decision theories can agree that utility should be maximized while disagreeing about the perspective from which alternatives are evaluated.

### What changes in \(\mathsf H_\pi\)?

A useful model may contain the following relationships:

\[
Q\longrightarrow \text{agent's action},\qquad
Q\longrightarrow \text{predictor's prediction},\qquad
Q\longrightarrow \text{another implementation}.
\]

The first arrow represents application of the policy. The second represents a predictor whose output depends on what the policy would do. The third represents a copy or another system whose behavior is linked to the same computation. Ordinary causal effects then propagate from actions and predictions to outcomes.

These arrows are not all causal arrows in the ordinary physical sense. In particular, a decision today does not send a signal into the past. A predictor’s earlier output can nevertheless vary across functional hypotheticals because the predictor modeled the decision procedure whose output is being varied.

Conversely, a correlation is not enough to justify an arrow. If a lesion makes smoking attractive and independently causes cancer, changing the policy’s smoking output need not change whether the lesion exists. The hypothetical should preserve the lesion’s causal effects without treating cancer as a computation of the policy.

### The role of the planning anchor

The anchor \(k\) is an important additional choice. One reasonable interpretation is to condition \(M_k\) on background evidence available **before** the policy-dependent observations the policy is meant to handle. The policy can then prescribe different actions for those later observations.

For example, a policy may say what to do upon receiving a blackmail letter and what to do if no letter arrives. If receiving the letter depends on a predictor’s assessment of that policy, the letter’s presence may vary across policy hypotheticals. The agent still uses the actual letter as input when executing the selected policy; it need not hold the letter fixed in every hypothetical used to value that policy.

This resembles the source’s action-level treatment of blackmail and transparent Newcomb. It is not a requirement explicitly spelled out in footnote 16. A different choice of anchor—especially conditioning on a policy-dependent observation after it occurs—can give a different answer. P-FDT’s footnote alone does not settle every such case.

## 3. Three kinds of dependence

It helps to contrast P-FDT with two other theories discussed in the paper.

**Evidential decision theory (EDT)** evaluates an action by conditioning on it. In a simple formulation, it maximizes

\[
\mathbb E[U\mid X=x,A=a].
\]

That asks what taking the action would be evidence about. Correlations between action and outcome can therefore affect the comparison even when the action does not influence the correlated outcome.

**Causal decision theory (CDT)** instead evaluates a physical intervention, schematically

\[
\mathbb E[U\mid X=x,\operatorname{do}(A=a)].
\]

It propagates the effects of changing the action along causal pathways, but ordinarily holds an earlier prediction fixed.

P-FDT’s policy intervention differs from both. It breaks correlations that arise only from background circumstances, as CDT does; but it also preserves modeled dependencies between the policy-selection output and accurate predictions or implementations of it. The paper calls the broader relation **subjunctive dependence**.

Consider the imaginary smoking-lesion problem. Smoking gives the agent \(1{,}000\) utility, has no causal effect on cancer, and is correlated with cancer only because a lesion independently causes both a desire to smoke and cancer. If the agent values smoking and the lesion is unaffected by the policy intervention, then

\[
V(\pi_{\rm smoke})-V(\pi_{\rm refrain})=1{,}000.
\]

Under these assumptions P-FDT smokes. A simple EDT model may refrain because smoking is bad news about the lesion. The paper also notes that more elaborate EDT treatments can avoid that result and that the smoking-lesion setup requires care about the agent’s knowledge of its own preferences.

Now contrast a predictor. If the predictor fills a box because its model predicts one-boxing, changing the policy output in a functional hypothetical changes what that model predicts. The lesion does not perform an analogous computation. This distinction—not a blanket preference for either correlation or causation—is the operative idea.

## 4. P-FDT in Newcomb’s problem

An opaque box contains either \(\$1{,}000{,}000\) or nothing; a transparent box contains \(\$1{,}000\). A predictor has filled the opaque box if it predicted that the agent would take only that box. Suppose it predicts correctly with probability \(0.99\), symmetrically for either policy.

Let \(\pi_1\) take only the opaque box and \(\pi_2\) take both. Under the assumed functional model,

\[
\begin{aligned}
V(\pi_1)&=0.99(1{,}000{,}000)=990{,}000,\\
V(\pi_2)&=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\end{aligned}
\]

P-FDT selects \(\pi_1\). The point is not that choosing one box physically changes money already placed in it. Rather, the hypothetical in which the selector outputs \(\pi_1\) is also one in which the predictor probably predicts \(\pi_1\).

The result depends on the prediction model. More generally, if the probability of a full box under \(\pi_1\) is \(p_1\), and under \(\pi_2\) is \(p_2\), one-boxing is favored exactly when

\[
(p_1-p_2)\,1{,}000{,}000>1{,}000.
\]

A reported overall accuracy rate does not by itself determine \(p_1-p_2\) for these interventions. To use P-FDT in an unfamiliar case, one needs a model of how the predictor responds to each candidate—not merely a correlation observed in some population.

## 5. Observations inside a policy: transparent Newcomb

Now let both boxes be transparent. The predictor fills the million-dollar box if it predicts that the agent would leave the \(\$1{,}000\) box behind **when the large box is full**.

A policy has at least two components:

\[
\pi=(\pi(\text{full}),\pi(\text{empty})).
\]

Assume the best empty-box action is to take both boxes. With \(99\%\) accurate prediction of the full-box component, compare:

\[
\begin{array}{c|cc|c}
\text{Policy} & \pi(\text{full}) & \pi(\text{empty}) & V(\pi)\\ \hline
\pi_C & \text{one box} & \text{two boxes}
&0.99(1{,}000{,}000)+0.01(1{,}000)=990{,}010\\
\pi_D & \text{two boxes} & \text{two boxes}
&0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000.
\end{array}
\]

Thus, with the earlier planning anchor, P-FDT selects \(\pi_C\). If the agent actually sees a full box, it applies that policy and takes one box.

The unsettling feature is deliberate: the \(\pi_D\) hypothetical usually contains an **empty** box, although the actual input may be “full.” The policy comparison is not a prediction that the observed box is now empty. It is an assessment of policies across modeled situations in which the observation itself depends on what the predictor expects the policy to do.

CDT, by contrast, holds the already full box fixed when intervening on the physical action and takes both. EDT conditioned on seeing the full box also normally takes both. The paper defends the functional verdict by comparing it with the policy an agent would have wanted to commit to before prediction. That argument is motivation, not a proof that the policy-level rule always matches ideal precommitment.

## 6. Why policy selection matters in multi-agent cases

Policies can link decisions made at different inputs. Consider two players in separate rooms, each running the **same policy selector with the same selector input**, but receiving different role labels \(L\) and \(R\) as inputs to the selected policy. Each chooses Cooperate (\(C\)) or Defect (\(D\)). For the left player, payoffs are:

\[
\begin{array}{c|cc}
 & R:C & R:D\\ \hline
L:C & 1{,}000{,}000 & 0\\
L:D & 1{,}001{,}000 & 1{,}000
\end{array}
\]

Suppose the right player has the symmetric payoff table. The possible deterministic policies include

\[
\pi_{CC}=(C,C),\quad
\pi_{CD}=(C,D),\quad
\pi_{DC}=(D,C),\quad
\pi_{DD}=(D,D),
\]

where the components are actions at inputs \(L\) and \(R\). A policy-output intervention changes both implementations because, by assumption, both use the same selector output. Their physical actions need not be identical: \(\pi_{CD}\), for instance, makes the left player cooperate and the right player defect.

For the left player, the values in this perfect-link model are

\[
V_L(\pi_{CC})=1{,}000{,}000,\quad
V_L(\pi_{CD})=0,\quad
V_L(\pi_{DC})=1{,}001{,}000,\quad
V_L(\pi_{DD})=1{,}000.
\]

If the common selector maximizes **left-player utility**, it selects \(\pi_{DC}\): the left player defects and the right player cooperates. If instead it maximizes right-player utility, it selects \(\pi_{CD}\). If its common objective is the sum of both players’ payoffs, it selects \(\pi_{CC}\).

This example exposes a genuine modeling issue rather than a universal prescription. Shared policy output alone does not imply cooperation: the objective encoded in the selector and the permitted role-dependent policies matter. Nor can two players with different selfish utility functions simply be assumed to have identical selector inputs. If each runs a distinct selector, one must model which computations are linked and how each responds to the other. Footnote 16 does not specify a general multi-agent equilibrium rule.

The example also shows why policy-level reasoning can differ from changing just the action at the current role. An intervention on an entire selected mapping can affect its outputs at both \(L\) and \(R\). Whether that is appropriate depends on whether the other player actually implements, predicts, or otherwise depends on the relevant mapping.

## 7. Blackmail and imperfect prediction

Suppose a blackmailer starts a damaging program only if she predicts that the agent would pay \(\$1{,}000\) upon receiving a demand. If the program runs and the agent refuses, the damage is \(\$1{,}000{,}000\). Assume the blackmailer always targets a payer, but mistakenly targets a refuser with probability \(\varepsilon\).

Using a planning anchor before the targeting decision, compare policies that pay or refuse upon receiving a demand:

\[
V(\pi_{\rm pay})=-1{,}000,\qquad
V(\pi_{\rm refuse})=-\varepsilon\,1{,}000{,}000.
\]

Refusal is preferred if

\[
\varepsilon<0.001.
\]

At \(\varepsilon=0.0009\), the expected loss from refusal is \(\$900\), so the policy refuses even on the rare occasion when a demand actually arrives. At \(\varepsilon=0.0011\), its expected loss is \(\$1{,}100\), so paying is favored under this particular model.

The comparison is sensitive to both error rates. If a payer is targeted with probability \(r\) rather than certainty, its expected cost is \(1{,}000r\), and refusal is favored when \(1{,}000{,}000\varepsilon<1{,}000r\). Additional costs, other threats, or predictors that inspect different aspects of the policy must likewise be modeled explicitly.

## 8. How to apply P-FDT, and what remains open

For a new problem, the following procedure makes the substantive assumptions visible:

1. **Specify the policy domain and objective.** Identify possible inputs, available actions, utility, and the candidate policy class. Include relevant off-path inputs, such as receiving a demand that the selected policy makes unlikely.
2. **Choose the planning anchor.** State which background evidence is fixed and which later observations may vary with the policy. Do not silently condition on an observation that the model says depends on the policy.
3. **Identify the selector and its implementations.** Ask what computation selects the policy, where its output is used, and whether predictors simulate that computation, its action at a particular input, or something only approximately related.
4. **Build and test the intervention model.** For each candidate policy, propagate its effects through the specified logical, predictive, and causal links. Leave unrelated background causes alone. For imperfect links, use candidate-sensitive probabilities.
5. **Compute expected utility and apply the winner.** Compare whole-policy values, break ties consistently, and execute the selected policy at the actual input. Check sensitivity to the anchor, prediction assumptions, and policy class.

Several limitations remain. The most basic is **logical counterfactual construction**: the paper supplies no general method for discovering all and only the relevant subjunctive dependencies. A graph that gives the desired Newcomb answer is not, by itself, an independently validated theory of predictors.

Second, **policy identity and scope** matter. Is an intervention on an entire function, one implementation’s selected policy, or a policy shared by several agents? Extensional equality of two mappings does not automatically establish that their selectors are the same computation. Conversely, two physically different machines may implement the same computation.

Third, **dynamic consistency** needs specification. A policy chosen at one anchor may later be reconsidered after new information. If the later selector conditions differently or changes its policy class, it need not reproduce the earlier policy. One operational solution is to retain the same anchor and selector while treating new observations as inputs to its policy; but footnote 16 does not prove this is always correct or feasible.

Finally, stochastic policies require a distinction between a distribution over actions and its realized random draw. A predictor might know the distribution without knowing an independent draw, or it might predict a pseudorandom seed. These are different dependency models and can yield different values.

The paper argues that functional reasoning performs well in “fair” problems whose outcomes depend on behavior rather than on the name of a decision theory. It also acknowledges that fairness is not formally settled and that no theory wins every constructed problem. Those qualifications apply with particular force to the policy-level interpretation: its attractive examples do not establish universal optimality.

## Conclusion

P-FDT evaluates a policy by imagining the policy-selection computation outputting that mapping, propagating the change through modeled dependencies, and maximizing expected utility over the resulting hypotheticals. The selected policy is then applied to the actual input.

This makes predictors, copies, and contingent observations part of the decision problem without treating every correlation as control. But its conclusions depend on choices that the source’s policy footnote leaves open—especially the planning anchor and the structure of functional dependence. Used carefully, P-FDT is therefore both a decision rule and a demand for an explicit model of what would change under its counterfactuals.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, especially footnotes 7 and 16 and sections 3–6. [arXiv:1710.05060v2](https://arxiv.org/abs/1710.05060v2).
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Explaining policy selection**

I need to deliver around 2400 words on policy selection inputs and possible re-evaluation of selections. I’m thinking about a multi-agent example with distinct inputs and a single shared mapping, highlighting asymmetric roles. I’ll compare two policies with deviations and how they relate to utilities. It could involve a numerical matrix with labeled separate utilities, showing how the shared algorithm works under the assumption that the same policy carries over when the same selector input is used. Sounds good!
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/f6a0a6e3-4bba-4681-af41-bc0154f0faad/call_0/request.json)

[Authoritative raw response](../../../../../../runs/f6a0a6e3-4bba-4681-af41-bc0154f0faad/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/f6a0a6e3-4bba-4681-af41-bc0154f0faad/call_1/request.json)

[Authoritative raw response](../../../../../../runs/f6a0a6e3-4bba-4681-af41-bc0154f0faad/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
