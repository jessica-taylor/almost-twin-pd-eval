# P-FDT: choosing a policy in a world of predictors

A decision can affect the world in more ways than by sending a physical signal from an action to its consequences. A predictor may have already acted on an accurate model of the decision-maker. Another agent may be running the same decision procedure in a separate room. In such cases, changing the output of the procedure in a hypothetical can require changing the prediction or the other agent’s output, even though the actual physical action causes neither.

**Policy functional decision theory**, or **P-FDT**, asks what policy the decision procedure should output when these dependencies are taken into account. A policy maps possible inputs to actions. Rather than choosing only an act for the observation currently in hand, P-FDT evaluates alternative mappings, then applies the selected mapping to that observation.

This is an interpretation of a short passage in Yudkowsky and Soares’s *Functional Decision Theory*. Footnote 16 says that the authors’ preferred formulation intervenes on the decision-theory node to choose “not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action.” Footnote 7 likewise says that agents iterate over policies rather than actions. The main text develops an action-selection version in greater detail; the footnote does not provide a complete policy-selection algorithm. In what follows, the broad functional-counterfactual idea is drawn from the paper, while the explicit policy model and several implementation choices are proposals for making the footnote operational.

## 1. Why policies rather than isolated actions?

Let \(\mathcal X\) be a set of possible observation histories and \(\mathcal A(x)\) the actions available after history \(x\). A deterministic policy is a function

\[
\pi:\mathcal X\longrightarrow\mathcal A,
\qquad \pi(x)\in\mathcal A(x).
\]

For example, a policy for a transparent-box problem might say:

- if the opaque box is observed full, take only that box;
- if it is observed empty, take both boxes.

The policy specifies behavior at both inputs, including one that may not occur. This matters whenever someone predicts what the agent *would* do in a particular circumstance, or when several implementations of a decision procedure receive different inputs.

P-FDT’s central question is not simply “What would happen if my body performed action \(a\)?” Nor is it merely “What would I learn if I observed myself performing \(a\)?” It is:

> What outcomes would obtain if the policy selected by this decision procedure were \(\pi\), with the relevant dependencies on that selection preserved?

The paper calls these **subjunctive dependencies**. They include ordinary causal dependencies, but also dependencies arising from computation or prediction. Two implementations of the same function on the same input should agree, barring error. A reliable predictor’s output also changes, to a degree determined by its mechanism and reliability, across suitable hypotheticals about the predicted procedure.

The claim is not that choosing now physically changes yesterday’s prediction. The hypothetical is a tool for comparing possible outputs of a decision procedure in a model that represents the predictor as a predictor.

## 2. A mathematical skeleton for P-FDT

Suppose an agent has:

- a model \(M=(P,G)\), with probabilities \(P\) and a graph or other description \(G\) of relevant dependencies;
- a set \(\Pi\) of admissible policies;
- a utility function \(U\) over outcomes;
- an actual observation \(x_{\mathrm{act}}\).

Let \(D\) denote the P-FDT policy-selection computation, and let \(Z\) be a variable in the model representing the policy it outputs. The following is a useful **proposed formalization**, not an equation supplied in footnote 16:

\[
\pi^\star
\in \operatorname*{arg\,max}_{\pi\in\Pi}
V(\pi),
\qquad
V(\pi)=
\mathbb E_{M}^{\,\operatorname{do}(Z=\pi)}[U(O)],
\]

followed by

\[
a^\star=\pi^\star(x_{\mathrm{act}}).
\]

The notation \(\operatorname{do}(Z=\pi)\) means model surgery: set the node representing the selector’s output to \(\pi\), and propagate the consequences through the dependencies encoded in \(G\). It does **not** by itself tell us which arrows belong in \(G\). Supplying those is the difficult part.

In a simple model, the observation and action equations might be

\[
X=h(Z,W),\qquad A=Z(X),\qquad O=g(A,X,W),
\]

where \(W\) represents background uncertainty. The dependence of \(X\) on \(Z\) permits the environment to respond to a prediction of the selected policy. Under the intervention \(Z=\pi\),

\[
V(\pi)
=\mathbb E_W\!\left[
U\!\left(g\bigl(\pi(h(\pi,W)),h(\pi,W),W\bigr)\right)
\right].
\]

This expression makes an important feature visible: the observation at which the policy is evaluated can itself change across policy hypotheticals. The agent still applies its chosen policy to its *actual* observation. But when ranking policies, it need not assume that the actual observation would have occurred under every alternative.

The formula also makes assumptions that the footnote leaves open. It treats the policy selector as a coherent node, gives all alternatives a common reference distribution over background variables, and assumes the optimization has a solution. For finite \(\Pi\), existence is straightforward; ties need a specified rule. For large or infinite policy spaces, existence and computation require further conditions.

### The role of evidence

The model may incorporate evidence that remains fixed across the comparison. For example, the agent can condition on a known game rule or a measurement made before any relevant predictor modeled its policy. By contrast, if seeing a full box is itself an effect of a prediction of the policy, conditioning every hypothetical on “the box is full” may erase the dependency the comparison is intended to capture.

This distinction is not completely resolved by the footnote. My proposed convention is to distinguish:

1. **Reference evidence:** information taken as fixed when constructing the policy-selection problem.
2. **Policy-dependent input:** information whose occurrence may vary under the policy intervention, but to which the selected policy responds.

The division must be justified by the model, not by a blanket rule that observations are either always conditioned on or always ignored. If an observation is informative about an independent background state, discarding its evidential content can be costly. A policy can use that observation: the reference distribution describes the state and the observation mechanism, and \(\pi(x)\) specifies the response.

## 3. How P-FDT differs from CDT and EDT

The three theories differ in their decision hypotheticals. For an action \(a\), observation \(x\), and outcome utility \(U\), a standard evidential decision theory, **EDT**, compares

\[
\mathbb E[U\mid X=x,A=a].
\]

It asks how good the news would be that the agent takes \(a\). Causal decision theory, **CDT**, instead compares something like

\[
\mathbb E[U\mid X=x,\operatorname{do}(A=a)],
\]

changing the physical action and propagating its causal effects. P-FDT’s proposed comparison intervenes on the selected **policy**, propagating both causal and relevant computational or predictive dependencies.

The distinctions can be illustrated by two classic cases.

### P-FDT in Newcomb’s problem

A transparent box contains \$1,000. A second box contains \$1 million if a predictor predicted that the agent would take only the second box; otherwise it is empty. Suppose, as an explicit model assumption, that the predictor gets the relevant policy output right with probability \(0.99\), independently of which of the two policies is selected.

For a policy that one-boxes, the expected payoff is

\[
V(\pi_{\mathrm{one}})=0.99(1{,}000{,}000)=990{,}000.
\]

For a policy that two-boxes, it is

\[
V(\pi_{\mathrm{two}})
=0.01(1{,}000{,}000)+1{,}000
=11{,}000.
\]

P-FDT selects the one-boxing policy in this model. CDT’s physical-action intervention holds the already-filled box fixed, making the extra \$1,000 attractive. EDT can also one-box, but for a different reason: taking one box is evidence that the predictor filled it.

A predictor being “99% accurate” in some population is not, by itself, enough to establish the two counterfactual probabilities above. The relevant error rates must apply under the candidate policies being compared. An adversarial predictor, a distribution shift, or a predictor whose accuracy depends on the policy could change the answer.

### P-FDT and the smoking lesion

In the paper’s imaginary smoking-lesion problem, a lesion causes both a desire to smoke and a high cancer risk; smoking itself does not cause cancer. If smoking yields an additional utility of 1,000 and changing the policy does not affect the lesion or cancer, then

\[
V(\pi_{\mathrm{smoke}})-V(\pi_{\mathrm{refrain}})
=1{,}000
\]

in the simplest version where both policies act at the relevant input.

The lesion is correlated with action, but it is not predicting the policy. Thus the proposed model leaves the lesion and its cancer consequences unchanged under the policy intervention. P-FDT smokes if smoking is genuinely beneficial under the stipulated utilities. A simple EDT model may refrain because smoking is bad news about the lesion, though the paper notes that this example has complications concerning self-knowledge and that some versions of EDT can respond to them.

The contrast is not “always preserve correlations” versus “always break them.” It is a question about the mechanism that makes a dependency persist across the particular hypothetical under consideration.

## 4. Predictions of conditional behavior

The policy formulation is especially natural when a predictor cares about what the agent would do after an observation that the predictor can influence.

In **transparent Newcomb**, the predictor fills the million-dollar box if it predicts that the agent would one-box *on seeing it full*. Consider two policies, both of which take the \$1,000 box when the million-dollar box is empty:

\[
\begin{array}{c|cc}
 & \text{full} & \text{empty}\\ \hline
\pi_C & \text{one-box} & \text{two-box}\\
\pi_D & \text{two-box} & \text{two-box}
\end{array}
\]

Assume a 99%-accurate prediction of the full-box response. Then

\[
V(\pi_C)=0.99(1{,}000{,}000)+0.01(1{,}000)
=990{,}010,
\]

whereas

\[
V(\pi_D)=0.01(1{,}001{,}000)+0.99(1{,}000)
=11{,}000.
\]

P-FDT selects \(\pi_C\), and if the agent actually sees a full box, it one-boxes. The lower-valued policy’s hypothetical usually contains an *empty* box. This is precisely the feature that a comparison conditioned on the actual full-box observation would suppress.

The policy also says to take both boxes if the million-dollar box is empty. That contingency matters in the predictor-error branch. A policy is not a promise to take the same action regardless of evidence; it is a plan for responding to evidence.

The same structure appears in Parfit’s hitchhiker. A driver rescues someone only if she predicts payment upon arrival. In a model with sufficiently accurate prediction and a rescue benefit much larger than the payment, a policy of paying on arrival can have greater value than a policy of refusing. P-FDT then pays if arrival occurs, even though the ride is already over. This is a controversial prescription: CDT regards the completed rescue as fixed when evaluating the later physical payment. P-FDT instead values the whole conditional policy using the dependency between that policy and the earlier rescue.

An imperfect predictor makes the trade-off quantitative. In mechanical blackmail, suppose paying a demand costs 1,000 and ensures that a predictor sends it. Refusing causes a loss of 1,000,000 only if the predictor mistakenly sends the demand, with probability \(\epsilon\). Under these particular assumptions,

\[
V(\pi_{\mathrm{pay}})=-1{,}000,\qquad
V(\pi_{\mathrm{refuse}})=-1{,}000{,}000\epsilon.
\]

Refusal is preferred when \(\epsilon<0.001\). This is not a universal rule against paying threats: different error rates, outside options, or consequences can reverse the calculation. Nor does the calculation assert that a recipient has not received a demand. It compares policy-dependent hypothetical distributions, one of which contains few demands.

## 5. P-FDT with other agents

Consider a prisoner’s dilemma against a perfect psychological twin. Each receives \$1 million if both cooperate and \$1,000 if both defect. A unilateral defector gets \$1,001,000; the unilateral cooperator gets nothing.

If both agents implement the same policy-selection computation on the same relevant input, the model can represent their actions as

\[
A_1=Z(x),\qquad A_2=Z(x).
\]

Intervening on \(Z\) to select cooperation changes both modeled actions; intervening to select defection does likewise. The comparison is therefore

\[
V(\pi_C)=1{,}000{,}000,\qquad
V(\pi_D)=1{,}000.
\]

P-FDT cooperates. This need not express altruism: the utility being maximized can be the first agent’s own payoff.

The policy perspective becomes more important when agents receive **different** inputs. Suppose the same selected policy is run once with input \(x_L\) and once with \(x_R\). The modeled actions are

\[
A_1=\pi(x_L),\qquad A_2=\pi(x_R).
\]

A policy intervention can change both entries together. It does not imply \(A_1=A_2\): a single policy may prescribe different actions at different inputs. For instance, a coordination rule might say “choose left on input \(x_L\), right on input \(x_R\),” because complementary actions are rewarded.

That is why replacing policy selection with a separate action intervention at the current input can lose information. The relevant alternative may be a *whole mapping*, not a change to just one output while other outputs of the selected mapping are held fixed.

However, shared use of the name “P-FDT” is not enough to establish a shared node. Agents may have different models, utilities, observations, implementations, or tie-breaking rules. With imperfect similarity, the model needs a graded dependence or uncertainty over mechanisms. Treating a stranger’s choice as identical to one’s own without evidence is not a consequence of P-FDT.

## 6. A procedure for unfamiliar problems

The following is an operational interpretation of the source, not a complete algorithm proven correct by it.

1. **Specify the policy domain.** List the observation histories, available actions, and admissible policies. Include relevant off-path inputs, especially those that predictors or other implementations may use.
2. **Choose the reference perspective.** State what evidence is fixed, what observations may depend on the policy, and what uncertainties remain.
3. **Model mechanisms.** Identify causal effects, predictors, simulations, shared computations, and independent background variables. Give imperfect dependencies explicit error models where possible.
4. **Construct one hypothetical per policy.** Set the selector’s output to the candidate policy. Propagate the consequences through the modeled dependencies; do not automatically condition on the actual action or actual observation.
5. **Calculate utility over complete outcomes.** Include branches in which a different observation occurs and the candidate policy prescribes a different action.
6. **Select and apply.** Maximize expected utility using an explicit tie-breaker, then apply the selected policy to the input actually received.
7. **Check sensitivity.** Vary prediction accuracy, dependence assumptions, reference evidence, and policy availability. Report when the preferred policy changes.

This procedure prevents two common mistakes. First, merely correlated background facts should not be made policy-dependent without a mechanism. Second, a predictor should not be frozen at its actual prediction if the model says that prediction tracks the policy output being varied.

## 7. What remains open

**Counterpossibles.** A fixed deterministic computation has one actual output. Asking what would happen if it output a different policy can therefore be a counterpossible: its antecedent may be mathematically false. The paper proposes using a graph that represents how logical and other dependencies propagate, while acknowledging that no satisfactory general method for constructing such a graph is provided. Ordinary conditioning on \(Z=\pi\) is not a substitute when that proposition has probability zero. The graph-surgery equation is a modeling proposal, not a solved semantics for all mathematical counterpossibles.

**Which selector, and which inputs?** Footnote 16 says to intervene on a node that chooses a policy, but does not fully specify how the selector is individuated across agents, observations, or time. It is also unclear in general which evidence should already be incorporated into its model. My reference-evidence convention makes some examples tractable, but different defensible boundaries can produce different prescriptions. In sequential problems, independently reselecting a policy at every history may also produce inconsistency unless the selector and its reference perspective are specified carefully.

**Randomization.** One may enlarge \(\Pi\) to stochastic policies. But a predictor might predict a distribution, a pseudorandom seed, or the realized outcome of a random device. These are different dependencies. Randomization cannot be assumed to defeat prediction merely because the agent is uncertain of its own eventual act.

**Self-reference and feasibility.** A selector can represent a node for its own output without first knowing that output, as the paper emphasizes. But representation alone does not guarantee that a self-referential dependency model is coherent, that an optimum is unique, or that it can be computed. Real applications require approximations and uncertainty over the model itself.

**Performance claims.** The paper argues that functional reasoning performs well in a range of predictive dilemmas and conjectures favorable performance in suitably “fair” problems. It also acknowledges that no theory wins in every constructed environment and that fairness is not formally settled. Policy selection does not by itself prove optimality, nonnegative value of information, or reflective stability for every environment; such results depend on the policy space and dependency model.

## Conclusion

P-FDT evaluates a decision as the output of a policy-selecting computation. It compares whole input-to-action mappings, propagates their consequences through causal and relevant computational dependencies, and applies the preferred mapping to the actual input. This can capture predictions of conditional behavior and coordination between implementations receiving different inputs.

Its distinctive strength is also its central challenge: the answer depends on which dependencies the counterfactual model preserves. Footnote 16 supplies the policy-selection idea, but not a complete account of how to build that model. Applied carefully, P-FDT is therefore both a decision procedure and a research program about the counterfactual structure of prediction and computation.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, especially §§3–6 and footnotes 7 and 16. [arXiv:1710.05060v2](https://arxiv.org/abs/1710.05060v2).