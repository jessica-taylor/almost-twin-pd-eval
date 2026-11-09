# P-FDT: choosing a policy as the output of a decision function

A decision can affect more than the events physically downstream of an action. A predictor may have already acted on a model of what the decision-maker will do. Another agent may run the same decision procedure on a similar problem. In both cases, the agent’s action and a seemingly independent event are linked by a computation.

**Policy functional decision theory**, or **P-FDT**, asks an agent to take such links seriously when evaluating decisions. Its central question is not merely “What would happen if I performed this physical action?” but “What would the world look like if the decision procedure I implement selected this policy?”

The primary source for P-FDT here is footnote 16 of Yudkowsky and Soares’ *Functional Decision Theory*. The paper mostly presents an action-selection formulation of functional decision theory, but the footnote says that the authors’ preferred formulation intervenes on the decision function to select “not an action but a *policy* which maps inputs to actions,” and then applies the policy to the agent’s inputs. Footnote 7 similarly says that this distinction can matter in multi-agent dilemmas.

Those remarks establish the policy-selection idea, but they do not give a complete policy-level algorithm. In particular, they do not settle exactly which policies are candidates, what information is held fixed in their evaluation, or how broadly a policy intervention affects other agents. The formal procedure below is therefore an interpretation, not a theorem taken from the paper.

## 1. From actions to policies

Let \(\mathcal X\) be a set of possible inputs or observation histories, and let \(\mathcal A(x)\) be the actions available at input \(x\). A deterministic policy is a function

\[
\pi:\mathcal X\longrightarrow\mathcal A,
\qquad \pi(x)\in\mathcal A(x).
\]

For a simple single decision, \(x\) might describe whether a box is full. For a sequential problem, \(x\) may include everything the agent has observed and done up to a decision point. A policy can then prescribe different actions at different histories.

Write \(D\) for the policy-selection procedure and \(M\) for its model of the problem. In a schematic idealization,

\[
D(M)=\pi^*,
\qquad
A=\pi^*(X),
\]

where \(X\) is the input actually received. The source’s central proposal is that the agent evaluates candidate policies by imagining different outputs of \(D\), and then executes the selected policy at its actual input.

A compact expression is

\[
\pi^* \in \operatorname*{arg\,max}_{\pi\in\Pi}
\mathbb E_{Q_\pi}[U],
\qquad
a^*=\pi^*(x).
\tag{1}
\]

Here:

- \(\Pi\) is the candidate set of policies;
- \(U\) is utility over complete outcomes;
- \(Q_\pi\) is the hypothetical distribution used when the output of \(D\) is set to \(\pi\);
- \(x\) is the agent’s actual input when the policy is applied.

Equation (1) is a **proposed operational rendering** of footnote 16. Its important feature is that \(Q_\pi\) is not automatically the ordinary conditional distribution \(P(\,\cdot\mid D(M)=\pi)\), nor is it necessarily the result of physically replacing the agent’s program with \(\pi\). It is meant to represent a counterfactual change in the output of the very policy-selection computation being evaluated.

Why select a whole policy rather than just an action? A predictor may care about what the agent would do under an observation the agent never actually receives. Likewise, a second agent may apply the same selected policy to a *different* input. A policy-level hypothetical can represent both dependencies without pretending that all linked agents must perform the same physical action.

## 2. Subjunctive dependence and counterfactuals

The paper calls the relevant relationship **subjunctive dependence**. Physical causation is one instance: if an action changes, its causal consequences may change. But the source also includes computational and logical dependence. Two accurate implementations of the same calculation give corresponding outputs, even if they have no causal connection to each other.

For an idealized P-FDT model, introduce a variable \(S\) representing the policy output of \(D(M)\). A graphical approximation to (1) is

\[
Q_\pi(o)
=
P_G\!\left(O=o\mid\operatorname{do}(S=\pi)\right),
\tag{2}
\]

where \(G\) encodes the dependencies the model takes to be relevant. The graph might contain arrows

\[
S\longrightarrow A,\qquad
S\longrightarrow \text{prediction}
\longrightarrow \text{environment}
\longrightarrow O.
\]

The first arrow represents the application of the policy to an input. The second represents a predictor whose prediction depends on the policy. There may also be arrows from \(S\) to another implementation of the same decision procedure.

This resembles a causal intervention, but it is not an ordinary claim that an agent can physically change a mathematical fact. If \(D(M)\) is deterministic, it has one actual output. Asking what would happen if it had another is a **counterpossible**: its antecedent is incompatible with the actual computation. The graph is an instrument for constructing a useful hypothetical, not an assertion that the agent sends a signal backward in time.

The paper acknowledges that specifying such a graph is a major open problem. A graph supplied with the right dependency structure can yield an answer; it does not by itself tell us how to discover that structure. Nor does ordinary conditionalization solve the problem: if \(D(M)=\pi\) is known to be false, conditioning on it may be undefined or may reflect misleading selection effects.

This differentiates P-FDT from two familiar theories:

- **Evidential decision theory (EDT)** evaluates an action by conditioning on having taken it. It can treat an action as good news about an otherwise unchangeable state.
- **Causal decision theory (CDT)** evaluates an action by intervening on the physical action and propagating causal effects. It generally holds an earlier prediction fixed.

P-FDT instead evaluates the output of a policy-selection computation. It aims to preserve both causal consequences and relevant computational dependencies, while breaking correlations that have no such dependence.

## 3. Newcomb’s problem and the smoking lesion

In Newcomb’s problem, an opaque box contains \$1,000,000 if a predictor predicted that the agent would take it alone. A transparent box contains \$1,000. Assume a predictor who is accurate with probability \(r=0.99\), with symmetric errors under either candidate action.

For simplicity, let the relevant policies be constant: \(\pi_1\) takes one box and \(\pi_2\) takes both. Under the stipulated dependency model,

\[
Q_{\pi_1}(\text{opaque box full})=0.99,\qquad
Q_{\pi_2}(\text{opaque box full})=0.01.
\]

Taking money as utility,

\[
V(\pi_1)=0.99(1{,}000{,}000)=990{,}000,
\]
\[
V(\pi_2)=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\]

P-FDT selects \(\pi_1\). It does not claim that the physical act of leaving the transparent box behind changes the past. It claims that, in the policy-output hypothetical where the agent predictably two-boxes, the predictor’s earlier prediction will usually differ.

The conclusion depends on the predictive mechanism. With symmetric accuracy \(r\), one-boxing is preferred precisely when

\[
rB>(1-r)B+c,
\quad\text{or}\quad
(2r-1)B>c,
\]

where \(B\) is the opaque-box prize and \(c\) is the extra transparent-box payoff. A predictor’s accuracy in some unrelated population is not enough: what matters is how its predictions respond to the candidate policy outputs in this problem.

Contrast the imaginary **smoking lesion** case. A lesion causes both a desire to smoke and a high probability of cancer, but smoking itself has no effect on cancer. If smoking provides a benefit \(c>0\), and changing the decision procedure’s policy does not change whether the lesion exists or whether cancer develops, then

\[
V(\pi_{\text{smoke}})-V(\pi_{\text{refrain}})=c
\]

in the simple case where the intervention changes the action in the relevant circumstances. P-FDT smokes. It does not use the correlation between smoking and cancer as evidence that choosing to smoke makes the lesion more likely.

The source notes complications in making the smoking-lesion story epistemically consistent: if the agent knows its own preferences and decision procedure, the stipulated action–lesion correlation may disappear. The point for P-FDT is narrower and more general: **a correlation is not enough to establish a policy-level dependency**. The model must explain why changing the policy output would also change the correlated event.

## 4. Why the whole policy matters

Consider transparent Newcomb. The predictor fills the opaque box if it predicts that the agent would take only that box **upon seeing it full**. The agent can also see when the box is empty.

There are four deterministic policies, specified by their actions at full and empty observations. Suppose a correct prediction occurs with probability \(0.99\). The attractive policy is

\[
\pi(F)=\text{one-box},\qquad
\pi(E)=\text{two-box}.
\]

Its expected payoff is

\[
0.99(1{,}000{,}000)+0.01(1{,}000)=990{,}010.
\]

The best policy that two-boxes on seeing full gives

\[
0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000.
\]

Thus, in this model, P-FDT selects the first policy and applies it: if it actually sees a full box, it one-boxes.

This is a particularly revealing counterfactual. While evaluating a candidate policy at the full-box input, the model may assign substantial probability to the box being empty under that policy. The agent knows what it sees in the actual situation; it does not believe that the actual full box is empty. Rather, the alternative policy-output hypothetical allows the predictor, box contents, and observation to vary together.

The paper’s action-level treatment reaches a similar prescription by intervening on the output of the decision function at the full-box input. The policy-level treatment makes the alternative actions at *both* inputs explicit. That is useful even where, as here, both formulations can agree.

## 5. Linked agents with different inputs

Policy selection becomes especially important when the same procedure is implemented more than once. Consider two separate machines implementing the same P-FDT policy selector. Each receives a private role, \(L\) or \(R\), and then chooses one of two doors, \(0\) or \(1\). They both receive 10 if they choose different doors and 0 otherwise.

If the intervention sets the shared policy-selector output to \(\pi\), then each machine applies \(\pi\) to its own role. Compare

\[
\pi_{\text{same}}(L)=0,\quad \pi_{\text{same}}(R)=0
\]

with

\[
\pi_{\text{split}}(L)=0,\quad \pi_{\text{split}}(R)=1.
\]

Under a model in which the same policy output controls both machines,

\[
V(\pi_{\text{same}})=0,\qquad
V(\pi_{\text{split}})=10.
\]

The chosen policy coordinates them while prescribing *different actions*. An action-level shortcut that says “the other machine does whatever I do” would misrepresent the dependency.

This example requires a strong assumption: the two machines really do implement the relevant shared policy-selection computation, and the intervention reaches both implementations. Mere resemblance or agreement with P-FDT’s philosophical principles does not establish that. If their models, objectives, tie-breaking rules, or code differ, one needs a model of how their outputs vary together. The source says the policy/action distinction can matter in multi-agent dilemmas; it does not supply a universal rule that all P-FDT agents are linked.

The same caution applies to a psychological twin prisoner’s dilemma. If both agents are implementations of the same computation on the same input, their outputs coincide in the relevant hypothetical. With the source’s payoffs, mutual cooperation yields \$1,000,000 each and mutual defection \$1,000 each, so cooperation wins. But if the other player is an independent defector, P-FDT need not cooperate: its result follows from the modelled dependence, not from a blanket preference for cooperation.

## 6. Observation, blackmail, and the evaluation standpoint

The hardest unresolved choice in (1) is how to construct \(Q_\pi\) after the agent has observed something. The source’s action-level examples sometimes evaluate a decision using hypotheticals in which the agent would have received a different observation. Footnote 16 does not fully specify the policy-level analogue.

A reasonable interpretation is to choose an **evaluation standpoint** before the observations whose occurrence may depend on the policy. Facts already settled and not subjunctively dependent on the policy can be represented in the background distribution. The policy is then evaluated across the observations it would generate, and the selected policy is applied to the observation actually received.

This is an additional assumption. It preserves the paper’s motivation for predictor cases, but choosing the standpoint is not automatic. If one conditions on every current observation before evaluating policies, one can erase precisely the predictor dependence the source wants to preserve. If one conditions on too little, one can ignore genuinely relevant information. An operational model must say which evidence is background and which is generated within the policy hypothetical.

The mechanical-blackmail example illustrates the issue. A blackmailer starts a damaging program only if she predicts that the agent will pay \$1,000 to stop it. Otherwise she does not start it. If the agent refuses after being blackmailed, the loss is \$1,000,000.

Let \(\varepsilon\) be the probability that the blackmailer mistakenly starts the program against a refusing policy. Assume, for this calculation, that she always starts it against a paying policy. Then the expected losses are

\[
L(\pi_{\text{pay}})=1{,}000,\qquad
L(\pi_{\text{refuse}})=\varepsilon(1{,}000{,}000).
\]

Refusal is preferred if \(\varepsilon<0.001\). At \(\varepsilon=0.0009\), its expected loss is \$900, so P-FDT selects refusal. If a letter nevertheless arrives, this policy is applied and the agent refuses, even though paying would avert the immediate \$1,000,000 loss.

That result is stark. The justification is not that refusal can stop a program already running. It is that, under the stipulated model, a predictable refusal policy usually prevents the program from being started. If the blackmailer starts it regardless of prediction, the dependency disappears and paying can be optimal. More generally, asymmetric prediction errors or other costs change the threshold.

The supplied paper states that the agent pays when the error chance is **0.011%**. Under the numerical assumptions just given, that appears to be an error: \(0.011\%=0.00011\), giving an expected refusal loss of \$110, so refusal remains preferable. The threshold is **0.1%**.

## 7. A practical modelling procedure

For an unfamiliar case, the following is a useful P-FDT workflow, subject to the unresolved choices already noted.

1. **Specify inputs and policies.** List the observations relevant to later action, including observations that might not occur. Define feasible policies over them.
2. **Choose the evaluation standpoint.** Identify the background evidence and uncertainty used to evaluate policies. Explicitly mark observations whose occurrence may itself depend on the policy.
3. **Identify the policy-output node.** Say which computation’s output is being hypothetically set. Distinguish it from the actual physical action.
4. **Model dependencies.** For each candidate policy, propagate its consequences through actual implementations, predictors, simulations, other agents, and ordinary causal mechanisms—but only where a justified dependence exists.
5. **Calculate expected utility.** Include outcomes on every branch generated by the candidate policy, not just the branch matching the agent’s present observation.
6. **Select and apply.** Choose a maximizing policy, using a specified tie-breaker if needed, and apply it to the actual input.

Several technical qualifications matter. If policies can randomize, the model must distinguish a shared random seed from independent random draws. Identical probability distributions do not imply identical realized actions. In sequential cases, policy domains and histories must be rich enough to represent future choices without allowing actions unavailable at a given history. And selecting from only a restricted policy class can make a result depend on how the problem was encoded.

A policy intervention is also not simply a physical precommitment. A commitment device can be observable, costly, or introduced too late for a predictor to have acted on it. The paper uses ideal precommitment as motivation, but P-FDT’s hypothetical concerns the output of the decision computation itself. The two comparisons coincide only under additional assumptions.

Finally, self-reference is manageable in principle but not automatically solved in practice. A program can refer to a description of itself, but that does not guarantee that its optimization terminates, that its dependence model is correct, or that its counterfactual values are uniquely defined.

## 8. Motivation and limits

P-FDT’s philosophical appeal is that it treats an agent as part of a world containing models and copies of agents. If an earlier predictor tracks a policy, or another machine implements the same computation, disregarding that relationship can make the agent choose a worse pattern of behavior. The source argues that this perspective explains one-boxing, cooperation with a twin, paying Parfit’s driver, and resistance to predictive blackmail without invoking retrocausation.

That is not a proof that P-FDT maximizes utility in every problem. The paper itself acknowledges that any decision theory can be penalized by an environment designed to punish it. Its proposed distinction between “fair” and “unfair” tests remains informal. Nor does the ability to write (1) settle how to infer subjunctive dependencies, evaluate counterpossibles, or select the correct policy domain and evaluation standpoint.

The most defensible lesson is therefore conditional: **given** a sound model of how a policy output is linked to predictions, other implementations, observations, and outcomes, P-FDT selects the policy with the greatest expected utility in those policy-output hypotheticals. Establishing that the model is sound is part of the work, not something the name of the theory accomplishes.

## Conclusion

P-FDT moves the object of decision from an isolated act to a policy produced by a decision function. Its distinctive counterfactuals vary that output while preserving the causal and computational dependencies the model judges relevant. The policy is then applied to the agent’s actual input.

This provides a coherent way to analyze predictors and linked agents, including agents with different observations. Its central open problem is equally clear: a useful policy rule still needs a principled account of which dependencies to preserve and which information to hold fixed.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, especially footnotes 7 and 16, [arXiv:1710.05060v2](https://arxiv.org/abs/1710.05060v2).