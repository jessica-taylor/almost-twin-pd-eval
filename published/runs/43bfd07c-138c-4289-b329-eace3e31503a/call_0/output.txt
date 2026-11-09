# P-FDT: choosing a policy as the output of a decision function

A decision can matter in two ways. It can physically change what happens next; and it can be the output of a procedure whose behavior has already been predicted, copied, or otherwise modeled. Policy functional decision theory, **P-FDT**, asks an agent to take both kinds of dependence into account.

The central object is not merely an action but a *policy*: a rule mapping possible inputs to actions. Roughly, P-FDT asks which policy would have the best consequences if it were the output of the very decision procedure now being used. The agent then applies that policy to its actual input.

This formulation comes from footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory*. The paper’s main text develops an action-selection formalization of functional decision theory, while the footnote says the preferred formulation instead intervenes on the decision function’s output to select a policy. It leaves important details unspecified: the policy space, the scope of the input, the construction of counterfactuals, and how policy selection behaves in multi-agent settings. The mathematical rule below is therefore an interpretation and operational proposal, not an equation explicitly supplied by the authors.

## 1. Why policies?

Let \(X\) be a set of possible decision inputs and \(A(x)\) the actions available at input \(x\). A deterministic policy is a function

\[
\pi:X\longrightarrow \bigcup_{x\in X} A(x),
\qquad
\pi(x)\in A(x).
\]

An input might include an observation history, a description of one’s role in a game, and other information available to the agent. For example, a policy for transparent Newcomb might say:

\[
\pi(\text{full})=\text{one-box},\qquad
\pi(\text{empty})=\text{two-box}.
\]

The distinction between a policy and an action is especially useful when others predict how the agent would act under an observation it may never receive. A blackmailer may ask, “Would this person pay *if* sent a threat?” A driver may ask, “Would the passenger pay *after* reaching town?” Such questions concern entries in a policy, including entries for circumstances that may not occur.

Footnote 16 states that the preferred formulation “intervenes on the node \(\mathrm{FDT}(-)\) to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action.” For this essay, P-FDT names that policy-selection formulation. The paper says the distinction matters in multi-agent dilemmas, as far as its authors can tell, but does not prove that it makes no difference elsewhere.

There are two functions to keep separate:

1. The **policy-selection procedure** \(D\), which outputs a policy.
2. The selected **policy** \(\pi\), which outputs an action when given an input.

The intervention is on a representation of the output of \(D\), not simply on the physical action taken by one body.

## 2. A working mathematical formulation

Suppose the agent has:

- a world-model \(M\), including probability assignments and a description of relevant causal and computational dependencies;
- a set \(\Pi\) of admissible policies;
- a utility function \(U\) over outcomes or complete histories;
- an actual input \(x\).

Let \(\mathbf D\) be a node in the model representing the policy output by the relevant instance of the policy-selection procedure. For each candidate \(\pi\), construct a hypothetical distribution

\[
Q_\pi(\,\cdot\,)
=
P_M\bigl(\,\cdot\mid \operatorname{do}(\mathbf D=\pi)\bigr).
\]

Here \(\operatorname{do}\) is a **modeling notation for a functional intervention**. It sets the policy-output node to \(\pi\) and propagates that change through the dependencies included in the model. It is not necessarily an ordinary physical intervention.

A natural P-FDT rule is then

\[
\pi^*\in\arg\max_{\pi\in\Pi} V(\pi),
\qquad
V(\pi)=\mathbb E_{Q_\pi}[U],
\qquad
a^*=\pi^*(x).
\tag{1}
\]

If several policies maximize value, a specified tie-breaking rule is needed. If actions vary by input, the policy space must ensure \(\pi(x)\) is admissible for every input on which it is defined.

Equation (1) is schematic. In particular, it does not tell us how to obtain \(Q_\pi\). Nor does it automatically settle which evidence is held fixed when computing \(V\). Those are central choices, not mere implementation details.

### An operational proposal about evidence

One interpretation, motivated by the paper’s transparent Newcomb and blackmail examples, is to evaluate policies from a **reference state before receiving observations that can themselves depend on the policy**. Evidence available at that reference state is incorporated into \(M\). Later observations are generated within each hypothetical and fed to the policy.

On this interpretation, the actual input \(x\) determines the action \(\pi^*(x)\), but it is not necessarily conditioned on in every policy hypothetical. A hypothetical policy can make \(x\) unlikely or prevent it from occurring altogether.

This is not the only possible interpretation of footnote 16. Choosing the reference state becomes difficult if an agent cannot reconstruct an earlier model, or if the evidence contains both policy-dependent and policy-independent components. The rule also needs a convention for re-selection over time. A useful proposal is that later agents implement the policy selected relative to a common reference model, rather than silently replace it with a newly optimized policy based on evidence the original policy was meant to govern. Whether a general P-FDT procedure can guarantee such consistency is open.

The distinction is not a refusal to learn. A policy can respond to information: “take an umbrella if it rains” is a policy. The issue is whether, when *comparing entire policies*, the agent should hold fixed evidence whose occurrence may depend on the policy being compared.

## 3. Three ways to evaluate alternatives

Evidential decision theory (**EDT**) evaluates an action by conditioning on the news that it is taken:

\[
V_{\mathrm{EDT}}(a)
=\mathbb E[U\mid A=a,\ X=x].
\]

Causal decision theory (**CDT**) evaluates an action by intervening on the physical action and propagating its causal effects:

\[
V_{\mathrm{CDT}}(a)
=\mathbb E[U\mid\operatorname{do}(A=a),\ X=x].
\]

P-FDT instead evaluates a policy-output intervention, including effects that depend on that output through prediction or shared computation as well as physical causation.

The paper calls the broader relationship **subjunctive dependence**. A predictor’s model and an agent can both depend on the output of the same decision procedure, just as two reliable calculators can depend on the answer to the same arithmetic problem. The connection need not be a signal sent backward in time. Conversely, correlation alone is insufficient: two things may be statistically associated because of a common cause, without either varying with the output of the decision procedure under consideration.

This matters for counterfactuals. If \(D\) is a fixed deterministic function, it has one actual output. To consider \(\mathbf D=\pi\) when \(D\) in fact outputs something else is to entertain a **counterpossible**: a hypothetical contrary to a logical fact. The paper acknowledges that there is no settled general method for constructing such hypotheticals. Its graphical approach assumes that a suitable dependency graph is supplied.

A practical model should therefore distinguish at least:

- the agent’s policy-output node;
- physical implementations of that policy;
- predictions or simulations responsive to the policy;
- ordinary causal consequences;
- background variables that do not depend on the policy;
- uncertainty about all of these relationships.

The graph is a substantive assumption. Drawing an arrow from one node to another does not establish a dependency.

## 4. P-FDT in Newcomb’s problem

An opaque box contains either \$1 million or nothing. A transparent box contains \$1,000. A predictor filled the opaque box if it predicted that the agent would take only that box. Suppose that, under the policy interventions being considered, the predictor is correct with probability \(0.99\), independently of the candidate policy.

With only one relevant input, a policy is effectively a choice between one-boxing and two-boxing. Under the stipulated counterfactual model,

\[
\begin{aligned}
V(\text{one-box})&=0.99(1{,}000{,}000)=990{,}000,\\
V(\text{two-box})&=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\end{aligned}
\]

P-FDT one-boxes. It does not claim the current act physically changes the already-filled box. Rather, the alternative policy hypotheticals change the predictor’s model of the agent and therefore its earlier prediction.

The accuracy assumption deserves care. A predictor’s observed success rate over a population does not by itself establish a \(99\%\) match rate under every hypothetical policy. It may be excellent at predicting familiar deterministic agents and poor at predicting randomized or unusual ones. For an unfamiliar case, one needs a model of the prediction mechanism, not just an aggregate correlation.

### Transparent boxes

Now suppose the opaque box is transparent, and the predictor fills it if it predicts the agent would one-box *upon seeing it full*. Consider two policies, both of which take both boxes when the million-dollar box is empty:

\[
\pi_1=(\text{one-box if full},\ \text{two-box if empty}),
\]
\[
\pi_2=(\text{two-box if full},\ \text{two-box if empty}).
\]

Under the same symmetric \(99\%\) prediction model,

\[
\begin{aligned}
V(\pi_1)&=0.99(1{,}000{,}000)+0.01(1{,}000)
=990{,}010,\\
V(\pi_2)&=0.01(1{,}001{,}000)+0.99(1{,}000)
=11{,}000.
\end{aligned}
\]

Thus the proposed policy rule chooses \(\pi_1\). If the actual box is full, the agent one-boxes.

The striking point is that the \(\pi_2\) hypothetical mostly contains an *empty* box, even if the agent actually sees a full one. Conditioning both policy evaluations on “full” would produce a different comparison: two-boxing would then yield an extra \$1,000. The paper’s action-selection treatment deliberately permits the observation to vary; the policy interpretation above extends that idea to whole policies.

## 5. P-FDT and the smoking lesion

Suppose a lesion both creates a desire to smoke and makes cancer likely. Smoking itself does not cause cancer, and, for this agent, smoking has an independent utility benefit of 1,000.

In a suitable P-FDT model, changing the policy’s smoking recommendation changes the action but not whether the lesion exists or whether cancer develops. If the expected survival utility is \(S\), then

\[
V(\text{smoke})=S+1{,}000,\qquad
V(\text{refrain})=S.
\]

P-FDT smokes.

A naive EDT calculation can instead treat smoking as bad news about the lesion and refrain. The source notes complications: if the agent knows enough about its desires or its own decision procedure, some EDT variants can avoid that conclusion. The example’s clean lesson is narrower: a policy intervention need not preserve every statistical correlation between action and background state. It preserves those dependencies the model says would persist under the relevant change.

## 6. Prediction of an off-path policy: mechanical blackmail

A blackmailer will run a damaging program only if she predicts the agent would pay \$1,000 upon receiving a threat. If the program runs and payment is refused, the agent loses \$1 million. If no program runs, the agent loses nothing.

Compare policies that pay or refuse upon receiving the letter. Suppose, as a specific model, that a paying policy causes blackmail with certainty, while a refusing policy is mistakenly blackmailed with probability \(\varepsilon\). Then

\[
V(\pi_{\rm pay})=-1{,}000,\qquad
V(\pi_{\rm refuse})=-1{,}000{,}000\varepsilon.
\]

Refusal is better precisely when

\[
\varepsilon<0.001.
\]

At \(\varepsilon=0.0009\), the expected loss of refusal is \$900, so the proposed P-FDT rule refuses even if a letter is actually received. At \(\varepsilon=0.0011\), expected loss is \$1,100, so it pays. These numbers depend on the stated error model; different false-positive or false-negative rates can change the result.

The refusal policy’s valuable feature is partly off-path: in most of its hypothetical histories, no letter arrives. Yet the policy must still specify what happens if one does. This is why “choose the best action given the letter” and “choose the best policy that includes a response to the letter” can differ.

A reader may object that, once the letter is in hand, refusing sacrifices \$1 million to maintain a policy that has already failed. That is the real normative dispute. P-FDT’s answer is not that the loss is illusory; it is that an agent predictably willing to make that sacrifice can make the threat rare enough to be better off across the policy’s relevant histories.

## 7. P-FDT in multi-agent problems

Consider the paper’s psychological-twin prisoner’s dilemma. Each player receives:

| | Twin cooperates | Twin defects |
|---|---:|---:|
| Cooperate | \$1,000,000 | \$0 |
| Defect | \$1,001,000 | \$1,000 |

If the twin implements the same relevant policy on the same input, a policy-output intervention changes both players’ actions. The comparison is therefore

\[
V(C)=1{,}000{,}000,\qquad V(D)=1{,}000,
\]

and P-FDT cooperates. No communication or altruism is required. An unrelated opponent whose action does not depend on the agent’s policy need not cooperate: P-FDT does not instruct agents to treat every opponent as a twin.

The policy formulation becomes more consequential when the agents receive *different* inputs. Imagine two copies of a policy, one told “row” and one told “column.” An intervention on the shared policy may alter both \(\pi(\text{row})\) and \(\pi(\text{column})\). This allows the agents to evaluate a coordinated contingent plan rather than assume that the other role’s output is fixed.

But the details matter. If each copy instead runs a different policy-selection procedure, or the opponent merely resembles the agent imperfectly, one should not automatically intervene on both outputs as identical. Nor does common use of the name “P-FDT” prove exact computational identity. A model must say which computations are shared, how inputs differ, and how another agent’s behavior responds to candidate policies.

There is also a preference issue. If the two roles have different utilities, one shared policy need not maximize both agents’ objectives. A joint optimization, bargaining rule, equilibrium, or separate policy selectors may be needed. Footnote 16 does not specify which. The policy formalization supplies a language for the question; it does not by itself solve every game.

## 8. How to apply P-FDT to an unfamiliar case

A practical analysis can proceed in five steps.

1. **Specify inputs and policies.** List observations and roles the policy may encounter, including relevant off-path inputs. Identify feasible actions and any resource or timing constraints.

2. **Specify the evaluation model.** Choose a reference state, a utility measure, and uncertainty about the environment. State which observations are generated inside each hypothetical rather than held fixed.

3. **Identify dependencies.** Model physical effects, predictors, copies, and simulations. Separately identify background factors correlated with behavior but not dependent on the policy output.

4. **Evaluate whole policies.** For each candidate \(\pi\), construct \(Q_\pi\), propagate the policy through all modeled dependencies, and compute \(\mathbb E_{Q_\pi}[U]\). Include histories where the actual observation does not occur.

5. **Apply the selected policy.** At the actual input \(x\), execute \(\pi^*(x)\). Check sensitivity to predictor accuracy, policy-space restrictions, tie-breaking, and alternative dependency models.

For stochastic policies, \(\pi(\cdot\mid x)\) gives a distribution over actions. One must additionally model whether random seeds are shared by copies and whether a predictor can forecast the realized draw or only its distribution. Randomization cannot simply be assumed to break prediction.

## 9. Limits and motivation

The philosophical attraction of P-FDT is that it evaluates a decision procedure as part of the world, rather than treating its present action as an isolated physical switch. A predictor can be relevant because it is responsive to the procedure; a lesion can be irrelevant because it is not. This can reproduce the advantages of advance commitment without requiring an actual external binding device.

But “act as one would have precommitted” is not a complete definition. A physical commitment changes the world through an ordinary causal mechanism; a P-FDT intervention changes the modeled output of a computation and its subjunctive dependants. They agree only under suitable assumptions.

Nor is superior performance universal. An environment can reward a particular decision procedure or punish a particular policy. The source conjectures that functional decision theory performs especially well in suitably “fair” problems, but explicitly leaves a precise fairness criterion and general optimality result open. The same caution applies to claims about reflective stability or nonnegative value of information: policy-level arguments support them under appropriate model and policy-space assumptions, but the footnote does not establish them for every formulation.

The largest technical gap remains the construction of functional counterfactuals. Self-reference can be represented—the decision procedure can have a node naming its own output—but representing a node does not determine how a predictor changes when that node is counterfactually set to another policy. That requires a defensible account of logical and computational dependence, particularly when predictors are imperfect or agents use different inputs.

## Conclusion

P-FDT selects an observation-contingent policy by comparing hypotheticals in which its own policy-selection procedure outputs different policies, then applies the chosen policy to the actual input. Its distinctive move is to propagate those hypotheticals through relevant predictions and shared computations, while not preserving mere statistical correlations indiscriminately.

The rule is usable when its policy space, reference model, and dependency assumptions are made explicit. Those assumptions also mark its unresolved frontier: footnote 16 gives the policy-selection idea, but not a complete general theory of counterpossible reasoning or multi-agent policy choice.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, especially §§3–6 and footnotes 7 and 16, [arXiv:1710.05060v2](https://arxiv.org/abs/1710.05060v2).