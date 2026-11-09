# 018_fdt_eq4_openai_gpt-6.1-terra_rlow_plow / 00013

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/4caea66b-e5e0-4c6f-8375-670a1003d840/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/4caea66b-e5e0-4c6f-8375-670a1003d840/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: deciding as the output of a function

Action functional decision theory, or **A-FDT**, begins with a change in perspective. Instead of asking only what a physical action will cause, an agent asks what follows from a proposed output of the decision procedure it is currently implementing.

This matters when other things depend on the same computation. A predictor may have simulated the agent before the agent acted. A second agent may run the same algorithm in a separate room. Neither is necessarily affected *causally* by the agent’s present movement. Yet, if their behavior tracks the output of the same decision function, changing that output in a hypothetical may change their behavior too.

The central proposal of Yudkowsky and Soares’s paper is to treat these relationships as **subjunctive dependencies** and preserve them when evaluating actions. The primary formalization here is the paper’s Equation (4): an action-indexed procedure that intervenes on the represented output of the decision function. The authors mention a preferred policy-based formulation, but do not fully specify it. It is therefore important not to substitute a policy rule for Equation (4) without saying so.

A-FDT is an expected-utility theory. Its distinctive feature is not a new account of utility, but a new account of which hypothetical consequences belong to each action.

## 1. Three ways to evaluate an action

Let \(A\) be a finite set of actions, \(O\) an outcome, \(U(O)\) its utility, and \(x\) the agent’s observation history. Every theory discussed here chooses an action by comparing expected utilities. They differ in how they construct the distribution used for that comparison.

**Evidential decision theory (EDT)** asks what an action would be evidence for:

\[
a_{\mathrm{EDT}}\in\arg\max_{a\in A}
\mathbb E[U(O)\mid X=x,\ \mathrm{Act}=a].
\]

This is ordinary conditionalization. An action looks attractive if learning that it was taken would be good news. The displayed rule requires the conditioning event to have positive probability.

**Causal decision theory (CDT)** instead asks what would result from a causal intervention on the physical act:

\[
a_{\mathrm{CDT}}\in\arg\max_{a\in A}
\mathbb E[U(O)\mid \operatorname{do}(\mathrm{Act}=a),\ X=x].
\]

Here the causal model specifies which effects of the act change and which prior events remain fixed. In particular, a prediction made yesterday is not physically caused by today’s choice.

A-FDT changes the target of intervention. Let \(P\) be the agent’s probabilistic model, \(G\) a graph of relevant dependencies, and

\[
D_x \equiv \text{the model variable representing }
\mathrm{A\!-\!FDT}(P,G,x).
\]

The variable \(D_x\) represents the output of the very procedure being defined, on the specified inputs. It is not itself the output. The paper’s Equation (4), written with the assigned name, is

\[
\boxed{
\mathrm{A\!-\!FDT}(P,G,x)\in
\arg\max_{a\in A}
\mathbb E_{P,G}\!\left[
U(O)\mid\operatorname{do}(D_x=a)
\right].
}
\tag{1}
\]

The model must tell us what changes when \(D_x\) is set to \(a\): ordinarily the agent’s action, but possibly also a twin’s action, a prediction, an earlier decision based on that prediction, or even the observation that the agent receives.

Equation (1) uses intervention notation, but the graph is broader than an ordinary causal graph. An arrow from \(D_x\) to a predictor does **not** mean that the present physical decision sends information backwards in time. It represents a dependence between the predictor’s computation and the output being predicted.

The expectation is evaluated in a *hypothetical model*. The agent need not believe that it can physically alter a mathematical fact, or that the hypothetical is an ordinary possible world. The hypothetical is a device for comparing actions.

## 2. What is subjunctive dependence?

Two systems can be linked because they compute the same function, even if neither causes the other. Two accurate calculators given the same input should agree about the result. Likewise, two exact copies of a deterministic decision process given the same inputs should agree about its output.

A-FDT treats these dependencies as relevant to choice. Suppose two prisoners have the same preferences, the same information and the same decision algorithm. Their decisions are made independently, with no communication. Their payoffs to the first prisoner are:

| First prisoner | Twin | Payoff |
|---|---|---:|
| Cooperate | Cooperate | \$1,000,000 |
| Defect | Defect | \$1,000 |
| Defect | Cooperate | \$1,001,000 |
| Cooperate | Defect | \$0 |

A causal intervention on the first prisoner’s physical act leaves the twin’s act fixed, making defection better by \$1,000. But if both implement the same decision function on the same input, A-FDT’s intervention changes the common output. It compares mutual cooperation, worth \$1,000,000, with mutual defection, worth \$1,000, and cooperates.

This is not a general instruction to cooperate with anyone who resembles you. The conclusion depends on a model in which the other choice tracks the intervened-on output. Similar agents with different information, incentives, or private randomness may respond differently.

Conversely, statistical correlation alone is not enough. If a medical condition causes both a desire to smoke and cancer, it does not follow that the cancer is computing the agent’s choice. A-FDT aims to preserve the former kind of dependence without preserving every correlation observed in the data.

### Counterpossible reasoning

For a fixed deterministic function and fixed inputs, there is only one actual output. If it outputs \(a\), the supposition that it outputs \(b\ne a\) is contrary to mathematical fact. A-FDT therefore relies on *counterpossibles*: hypotheticals whose antecedents are logically impossible.

The paper does not give a general logic of counterpossibles. Instead, it takes \(G\) as an input that says which dependencies to preserve under the stipulated intervention. This is a substantial limitation: a correct graph is doing much of the work. The paper explicitly leaves open how such graphs should be discovered, and whether Pearl-style graphs can adequately represent all the required logical relationships.

The self-reference in \(D_x\) is a separate issue. A model can contain a name or representation of the procedure’s output without already knowing that output. The authors point to self-referential constructions as showing how such representations can be built. That does not, by itself, solve the harder problem of assigning sensible consequences to counterpossible outputs.

## 3. Newcomb’s problem

A predictor puts \$1 million in an opaque box if it predicts that the agent will take only that box. A transparent box contains \$1,000. The agent may take either the opaque box alone or both boxes.

For a simple A-FDT model, let \(D\in\{\text{one},\text{two}\}\), and assume that under each intervention the predictor matches \(D\) with probability \(0.99\). The predictor fills the opaque box when it predicts one-boxing. Thus:

\[
\begin{aligned}
V(\text{one})
 &=0.99(1{,}000{,}000)=990{,}000,\\
V(\text{two})
 &=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\end{aligned}
\]

A-FDT one-boxes. In the one-box hypothetical, the predictor probably predicted one-boxing; in the two-box hypothetical, it probably predicted two-boxing.

CDT holds the already-filled box fixed under intervention on the present act, and therefore takes the extra \$1,000. Standard EDT can also one-box, but for a different reason: conditioning on one-boxing is good news about what the predictor did.

The distinction is clearer if predictor accuracy is parameterized. Suppose the predictor matches either proposed output with probability \(r\). A-FDT one-boxes precisely when

\[
r(1{,}000{,}000)>
(1-r)(1{,}000{,}000)+1{,}000,
\]

or \(r>0.5005\), under this particular symmetric error model. At equality the actions tie. Importantly, an observed 99% accuracy in some population does not automatically establish this same accuracy under *both* A-FDT interventions. That requires a model of how the predictor responds to each output.

## 4. Why A-FDT need not “manage the news”

In the imaginary smoking-lesion problem, smoking is correlated with fatal cancer, but the correlation is entirely due to a lesion that causes both a desire to smoke and a high cancer risk. Smoking itself has no causal effect on cancer, and the agent values smoking at \$1,000.

A simple A-FDT graph has the lesion upstream of both cancer and the circumstances in which the agent decides, but no edge from the relevant decision-output variable to the lesion or cancer. If the agent’s probability of cancer is \(p\) under both interventions, then

\[
V(\text{smoke})-V(\text{refrain})=1{,}000.
\]

A-FDT smokes. The action may be correlated with illness, but the illness does not track the output in the way a predictor’s decision does. CDT likewise smokes; a simple EDT model may refrain because smoking is bad news about the lesion.

The paper’s more detailed treatment is subtler than this simplified calculation. It models different possible utility inputs, depending on whether the lesion is present. Intervening on the decision output associated with the smoking-valuing input affects the act only in the cases where that input controls it. If the lesion probability is \(p\), the advantage of that intervention is \(1{,}000p\), still positive for \(p>0\).

The authors also caution that the smoking-lesion story is contrived: the assumed correlation can be difficult to reconcile with an agent’s knowledge of its own preferences and decision procedure. Some versions of EDT have defenses against it. The useful lesson is therefore not that every formulation proves EDT wrong, but that A-FDT distinguishes *prediction of a computation* from a merely correlated common cause.

## 5. Observations and the transparent-box problem

The treatment of observation is one of the most consequential features of Equation (1). CDT’s formula explicitly conditions on \(X=x\). Equation (1), as printed, instead uses \(x\) to select **which decision-output variable to intervene on**, and contains no separate condition \(X=x\).

This is not merely a notational choice. Suppose the opaque box is now transparent. The predictor fills it if it predicts that the agent would one-box **upon seeing it full**. Let

\[
D_F=\text{output on seeing a full box},\qquad
D_E=\text{output on seeing an empty box}.
\]

The predictor’s decision depends on \(D_F\). The actual act depends on \(D_F\) if the box is full and on \(D_E\) if it is empty.

Assume a symmetric 99% predictor and let \(q\) be the probability that \(D_E\) outputs two-boxing. Intervening on \(D_F\), Equation (1) gives

\[
\begin{aligned}
V(D_F=\text{one})
  &=0.99(1{,}000{,}000)+0.01q(1{,}000),\\
V(D_F=\text{two})
  &=0.01(1{,}001{,}000)+0.99q(1{,}000).
\end{aligned}
\]

The first is larger for every \(q\in[0,1]\). Thus, even on actually seeing the full box, A-FDT outputs one-box. In the second hypothetical the predictor usually leaves the box empty, so the current full-box procedure is usually not the one physically executed.

There is an apparent inconsistency in the paper’s detailed transparent-box calculation: one displayed expression includes \(\operatorname{do}(X=\text{full})\), while the subsequent calculation allows the observation to be empty. The latter calculation is consistent with Equation (4)’s absence of a separate observation condition; forcibly fixing the observation would not be. The equations above follow Equation (4) and the paper’s accompanying explanation.

This does not mean that observations are useless. They select the input-indexed decision node and can affect the procedure’s output. Nor does it mean that agents should erase all learned facts. But **where evidence enters \(P\), the node index, and the graph matters**. If \(P\) is already conditioned on a full box and that conditioning fixes the box under every intervention, one may get a different result. Equation (4) alone does not specify a universal method for constructing \(P\) across observation histories.

The same structure explains the paper’s answer to Parfit’s hitchhiker. A driver rescues an agent only if she predicts that the agent will pay \$1,000 after arriving safely. On reaching the city, A-FDT evaluates the output of the *pay-if-rescued* computation; the rescue itself can differ across those hypotheticals. Under a sufficiently reliable predictor and the stated payoffs, it pays. This is a substantive departure from evaluating only the consequences while holding the known rescue fixed.

## 6. A practical recipe—and its assumptions

For an unfamiliar problem, Equation (1) can be applied as follows.

1. **Specify the decision and utility.** List available actions, relevant outcomes, and utilities. State the observation history \(x\).
2. **Identify the output variable.** Represent the output of A-FDT on the particular inputs as \(D_x\). Distinguish this variable from the physical action.
3. **Build a dependency model.** Include causal effects and any predictors, copies, simulations, or other processes plausibly dependent on \(D_x\). Include noise and observations where they matter.
4. **Intervene separately.** For each \(a\), set \(D_x=a\), propagate the graph’s specified dependencies, and calculate expected utility over all resulting outcomes—including outcomes in which a different observation is received.
5. **Choose a maximizer.** Execute an action with maximal value, using an explicit tie-breaking rule if necessary.
6. **Check sensitivity.** Vary prediction accuracy, background probabilities, and uncertain graph edges. Report where the choice changes.

Steps 1, 4 and 5 are standard decision analysis. Step 3 is the distinctive and difficult part. As an **operational proposal**, one can use a structural model in which each node has an explicit response function and exogenous noise; a logical intervention replaces the equation for \(D_x\), while the response functions selected as subjunctively downstream are recomputed. This makes assumptions inspectable and allows numerical sensitivity analysis.

It is only a proposal, not a general construction supplied by the paper. In particular, one must justify why a predictor’s response function remains appropriate under a counterpossible output. A predictor might inspect source code, use a simulation, rely on a crude behavioral heuristic, or react to a policy’s description rather than its output. Those mechanisms can yield different dependencies. Merely drawing an arrow from \(D_x\) to “prediction” does not establish its strength.

Randomization also needs explicit modeling. If two copies share the same random seed, their actions may move together; with independent private coins, they need not. Whether the decision variable represents a realized action, a distribution over actions, or a program producing random actions can change the analysis. Equation (1) does not settle every such choice of representation.

### Actions and policies

A policy is a map \(\pi:X\to A\). The paper says its authors prefer a formulation that intervenes on a policy output and then applies the selected policy to the observation. But it does not provide a complete policy equation.

A natural *extension* would compare interventions of the form \(\operatorname{do}(\Pi=\pi)\) and then execute \(\pi(x)\). This may be useful when a predictor examines an entire contingent plan, or when changing one part of a plan changes other parts. It is not automatically equivalent to Equation (1), which changes a single \(D_x\) node while leaving other input-indexed nodes governed by the model. The transparent-box calculation, for instance, explicitly retains a separate \(D_E\).

One should therefore use Equation (1) for A-FDT as presented here, and state separately when a policy-level variant or additional coupling among nodes is assumed.

## 7. What the motivation establishes—and what it does not

The paper argues for A-FDT largely by comparing achieved utility. In Newcomb-like settings, an agent that predictably one-boxes tends to become richer than one that predictably two-boxes. In the twin dilemma, the shared cooperation computation achieves more for each participant. A-FDT also behaves like a useful precommitment in certain problems without requiring a separate binding device.

These comparisons are compelling only under their modeled dependencies. A predictor that rewards two-boxers, or explicitly penalizes users of a particular theory, can make A-FDT perform worse. The authors acknowledge that no theory wins every constructed problem and propose an informal distinction between “fair” problems, which reward or punish behavior in the problem, and problems that punish a procedure directly. They do not provide a complete formal fairness criterion or a proof of universal optimality.

Similarly, the paper claims benefits concerning information, reflective stability, and extortion resistance. Such claims should be read against the relevant model assumptions, not as consequences of the bare \(\arg\max\) notation. For example, an opportunity to ignore information can support a nonnegative value-of-information argument when the relevant policy set and evaluation perspective remain fixed. Equation (1) alone does not prove that property for every way of constructing observation-indexed models.

A-FDT’s challenge is therefore both philosophical and technical: whether its global comparison is the right standard of rationality, and whether its logical-dependency models can be specified reliably enough to implement it.

## Conclusion

A-FDT evaluates an action by intervening on the output of the decision function, not merely on the agent’s physical act or on evidence about that act. In a supplied dependency model, this can change predictions, copies, and observations while leaving merely correlated background facts unchanged.

That rule explains its characteristic answers to Newcomb’s problem, the twin prisoner’s dilemma, and the smoking-lesion problem. It also exposes the theory’s central open question: how to construct justified counterpossible dependencies rather than simply assuming them. Equation (1) is a decision procedure *given* such a model; developing general methods for obtaining the model remains an essential part of making A-FDT practical.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, especially §§3–6, arXiv:1710.05060v2.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/237500f5-9392-4266-931f-7cee7655ad67/call_0/request.json)

[Authoritative raw response](../../../../../../runs/237500f5-9392-4266-931f-7cee7655ad67/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/237500f5-9392-4266-931f-7cee7655ad67/call_1/request.json)

[Authoritative raw response](../../../../../../runs/237500f5-9392-4266-931f-7cee7655ad67/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
