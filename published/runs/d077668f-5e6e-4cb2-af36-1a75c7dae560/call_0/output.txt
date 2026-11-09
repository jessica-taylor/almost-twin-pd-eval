# P-FDT: choosing a policy as the output of a decision function

A decision can be physically isolated and still be connected to other events. A predictor may have acted yesterday on a model of what you would decide today. A copy of your program may be making a choice in another room. Neither need receive a signal from your present action for its behavior to be systematically related to yours.

**Policy functional decision theory (P-FDT)** takes such relationships seriously when evaluating decisions. Its central question is not merely “What happens if this physical action changes?” but approximately:

> What would follow if the decision procedure being implemented here selected a different policy?

A policy maps possible inputs—including observations—to actions. P-FDT evaluates candidate policies by changing the output of a represented decision function, propagating the consequences through relevant causal and computational dependencies, and selecting the policy with highest expected utility. It then applies that policy to the input actually received.

This account takes footnote 16 of Yudkowsky and Soares’ *Functional Decision Theory* as its primary source. The footnote says that their preferred formulation intervenes on a node representing the decision procedure to choose “not an action but a **policy** which maps inputs to actions,” then applies the input to that policy. The paper otherwise develops an action-selection formalization for simplicity. It does not give a complete policy-selection algorithm or settle how its counterfactuals should be constructed. The mathematical rule below is therefore an operational interpretation of P-FDT, not a theorem quoted from the paper.

## 1. Policies, inputs, and a decision node

Let \(\mathcal X\) be a set of possible inputs, and let \(\mathcal A(x)\) be the actions available at input \(x\). A deterministic policy is a function

\[
\pi:\mathcal X\longrightarrow \mathcal A,
\qquad \pi(x)\in\mathcal A(x).
\]

An input could describe the contents of a box, an opponent’s offer, or a history of observations and earlier actions. A policy must specify what to do at inputs that will not actually occur as well as at the input that does. Those unused entries can matter: a predictor may inspect what the agent *would* do after receiving a threat, even if it ultimately decides not to issue one.

Suppose an agent has a model \(M\) containing:

- a probability distribution over uncertain background circumstances;
- an outcome \(O\) and utility function \(U(O)\);
- a node \(D\) representing the policy output of the P-FDT decision procedure;
- relationships specifying how \(D\), observations, actions, predictions, and outcomes depend on one another.

Write \(M^{[D\leftarrow\pi]}\) for the hypothetical model obtained by setting the output of \(D\) to policy \(\pi\) and propagating the consequences along the dependencies that \(M\) treats as relevant. One natural policy-selection rule is

\[
\pi^*\in
\operatorname*{arg\,max}_{\pi\in\Pi}
\mathbb E_{M^{[D\leftarrow\pi]}}\!\left[U(O)\right],
\qquad
a^*=\pi^*(x_{\rm actual}),
\tag{1}
\]

where \(\Pi\) is the available policy class. Assume for simplicity that the maximum exists and a fixed tie-breaking rule chooses among maximizers.

Equation (1) should be read carefully. It does **not** say that the agent physically replaces itself with an arbitrary program and holds the rest of the world unchanged. The node \(D\) represents the output of the very procedure performing the evaluation. In a hypothetical where that output is \(\pi\), other systems sufficiently dependent on the same output may also behave differently.

Nor is \(M^{[D\leftarrow\pi]}\) simply the ordinary conditional distribution \(P(\,\cdot\mid D=\pi)\). It is a *constructed counterfactual model*. Some ordinary correlations will be broken; other, computational or predictive relationships will be preserved.

The paper uses a graph and a Pearl-style intervention as a convenient representation of such construction. But it explicitly acknowledges that the graph of logical and computational dependencies is not supplied by an established general procedure. Equation (1) inherits that limitation: its answer is only as good as the hypothetical models supplied to it.

### Which information enters the model?

A particularly important choice is the perspective from which policies are evaluated. My operational interpretation uses a **reference distribution** established before observations whose occurrence can itself depend on the policy. The policy may respond to those observations, but the evaluation does not automatically condition on their actual occurrence. Policy-independent background information can be incorporated into the reference model.

This is motivated by the paper’s treatment of transparent Newcomb and blackmail: its action-selection formalization can evaluate an alternative under which the observation currently being experienced would not have occurred. Footnote 16 does not itself specify a unique reference distribution or an exact rule for dividing background information from policy-dependent observations. Different choices can change the answer; they are substantive parts of an implementation, not mere notation.

## 2. Dependence is not just correlation

The source calls the relevant relationship **subjunctive dependence**. The term covers ordinary causal dependence but is broader. If a scribe copies a calculator’s display, her writing causally depends on it. If two reliable calculators independently compute the same sum, their matching answers depend on the same calculation, even without a causal connection between the machines.

Likewise, an accurate predictor may use a simulation of an agent’s decision procedure. In a P-FDT hypothetical where the represented output is different, the simulation’s result can change too. A perfect copy running the same procedure on the same input is an even clearer case: its output should track the intervened-on output.

By contrast, statistical association alone is not enough. In the imaginary smoking-lesion problem, a lesion causes both a desire to smoke and a high risk of cancer; smoking itself has no effect on cancer. If the agent values smoking at 1,000 utility, and the lesion and cancer mechanisms do not depend on the policy output, the two relevant P-FDT values differ by 1,000:

\[
V(\text{smoke})-V(\text{refrain})=1000.
\]

P-FDT therefore smokes under those assumptions. It does not infer that switching its policy changes the lesion merely because smokers are statistically more likely to have one. The source notes that a fully specified version of this example has complications concerning the agent’s knowledge of its own preferences; the lesson is the distinction between a common cause and a predictor-like dependence.

For comparison, **evidential decision theory (EDT)** evaluates an action using conditional expectations such as

\[
\mathbb E[U\mid X=x,A=a],
\]

whereas **causal decision theory (CDT)** evaluates it using a causal intervention on the physical action,

\[
\mathbb E[U\mid X=x,\operatorname{do}(A=a)].
\]

P-FDT instead intervenes on a policy-selection output and propagates the dependencies attributed to that output. CDT need not make yesterday’s predictor change when today’s action is intervened on; EDT may preserve correlations that are merely diagnostic. P-FDT aims to preserve neither too few nor too many relationships.

This is an ambition, not a mechanical test for every real-world case. Two agents using similar language, for instance, are not automatically linked like exact copies. One needs a model of how their reasoning actually relates to the policy-output counterfactual.

## 3. P-FDT in Newcomb’s problem

A predictor has filled an opaque box with \$1,000,000 if it predicts that the agent will take only that box. A transparent box contains \$1,000 and can be taken as well. Suppose the predictor is 99% accurate in each of the two relevant policy hypotheticals.

Let \(\pi_1\) take only the opaque box and \(\pi_2\) take both boxes. Under the stipulated prediction model,

\[
\begin{aligned}
V(\pi_1)&=0.99(1{,}000{,}000)=990{,}000,\\
V(\pi_2)&=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\end{aligned}
\]

P-FDT selects \(\pi_1\). This calculation does not say that leaving the transparent box behind *causes* the predictor’s earlier decision to change. It says that the hypothetical in which the relevant decision function selects the one-boxing policy also contains, with high probability, a predictor that predicted one-boxing.

The distinction matters when accuracy is imperfect. It is not enough to cite a predictor’s overall historical accuracy: the model needs appropriate probabilities for each candidate policy. An aggregate 99% accuracy rate could conceal very different error rates on different kinds of agents.

Now suppose both boxes are transparent, and the predictor fills the large box if it predicts that the agent will leave the \$1,000 behind **upon seeing the large box full**. A policy has at least two entries:

\[
\pi(\text{full}),\qquad \pi(\text{empty}).
\]

With a perfect predictor, a policy that takes only the large box when it is full produces \$1,000,000. A policy that takes both when it is full produces an empty large box, after which taking the small box yields \$1,000. Thus the better policy specifies one-boxing on seeing full and two-boxing on seeing empty.

The striking implication is that P-FDT applies the first instruction even when the agent actually sees a full box. The comparison is not “Given that the box is full, which physical act pays more?” It compares whole policies in a model where the contents can differ between policy hypotheticals. This is the source’s global-perspective motivation in policy form.

That conclusion is contentious. A CDT agent can reasonably reply that, once the full box is seen, taking the extra \$1,000 is causally dominant. P-FDT’s reply is that causal dominance holds the predictor’s earlier behavior fixed in precisely the comparison where its relationship to the policy is decision-relevant. Neither description alone settles the philosophical dispute; they use different counterfactuals.

## 4. Why P-FDT selects a whole policy

In a one-shot problem with only one relevant input, selecting an action and selecting a policy can appear equivalent. They need not be equivalent when the same policy is applied at several inputs.

Consider two exact copies running the same policy-selection procedure. One receives input \(L\), the other input \(R\). Each can choose \(C\) or \(D\), and both receive 10 utility exactly when the \(L\)-copy chooses \(C\) and the \(R\)-copy chooses \(D\); otherwise both receive 0. The policy

\[
\pi(L)=C,\qquad \pi(R)=D
\]

achieves 10 for each copy. Both can select the *same policy* and nevertheless take different actions.

An action-level shortcut that treats “the linked agents do the same action” as the dependency would miss this solution. The correct linkage in this example is equality of policy output, followed by application to different inputs—not equality of physical actions. Conversely, if two exact copies have the same input and use the same deterministic policy, their actions match.

This does not imply that all P-FDT agents share a policy output. Different models, objectives, available policies, or decision-procedure inputs can break the relevant identity. Footnote 16 says that the policy/action distinction matters in some multi-agent dilemmas, but it does not provide a general criterion for when distinct agents’ policy outputs are linked. The example illustrates one explicit assumption under which the distinction matters.

The familiar twin prisoner’s dilemma gives a simpler illustration. If identical agents with identical inputs obtain 1,000,000 each for mutual cooperation and 1,000 each for mutual defection, a shared-policy hypothetical compares those two outcomes. P-FDT cooperates. If the other player is an independent opponent with a fixed tendency to cooperate or defect, however, the same conclusion does not follow: the model must justify any dependence attributed to the opponent’s choice.

## 5. Threats, observations, and off-path instructions

Suppose a blackmailer runs a damaging program only if she predicts that the agent will pay \$1,000 after receiving a demand. If run and not stopped by payment, the program costs the agent \$1,000,000. A policy must specify its response to a demand even if no demand is received.

Assume, for an illustrative error model:

- a policy that pays when threatened is threatened with probability 1;
- a policy that refuses is mistakenly threatened with probability \(\epsilon\);
- there are no other relevant costs.

Then

\[
V(\pi_{\rm pay})=-1000,
\qquad
V(\pi_{\rm refuse})=-1{,}000{,}000\epsilon.
\]

Refusal is better if \(\epsilon<0.001\), or 0.1%. For example, at \(\epsilon=0.0009\), the expected loss from refusal is \$900. At \(\epsilon=0.0011\), it is \$1,100, so payment is better under these stipulated probabilities.

The paper’s later numerical sentence says that payment is preferred at an error chance of 0.011%. That appears inconsistent with its own preceding numbers: 0.011% is \(0.00011\), giving an expected refusal loss of \$110 rather than more than \$1,000. The policy calculation requires a specified error model and threshold; the qualitative lesson is not that P-FDT always refuses threats.

If the agent nevertheless receives a demand when following the refusal policy, applying that policy means refusing, even though payment would avert the imminent loss. The favorable policy value includes the much more common hypothetical in which the blackmailer does not issue the demand. This is an off-path instruction: it is essential to the policy’s effect on the predictor, despite rarely being executed.

An observed threat may also be evidence that the blackmailer is less accurate or operates differently than the model assumed. How P-FDT should revise its model after such surprising evidence, while retaining a coherent policy-selection perspective, is an important unresolved issue. One cannot simply assert the favorable threshold without specifying what is known, what is uncertain, and how that uncertainty enters the policy hypotheticals.

## 6. Counterpossibilities and implementation

There is a conceptual cost to intervening on a mathematical output. If a deterministic procedure on fixed inputs actually returns \(\pi^*\), then “it returns a different \(\pi\)” is not an ordinary possible state of the same computation. The paper calls such scenarios **counterpossibilities**: hypotheticals whose antecedents run against a logical fact.

The proposed intervention is a tool for evaluating these scenarios, not a claim that the agent can make arithmetic or the past physically change. In a model with equations such as

\[
\widehat A=f(D,E),\qquad
X=g(\widehat A),\qquad
A=D(X),\qquad
O=h(A,X,E),
\]

one can replace the represented policy output \(D\) with \(\pi\), retain the other specified mechanisms, and recompute. Here \(E\) represents prediction error or other background uncertainty. This graph is useful only if \(f\) really captures how the predictor tracks the decision procedure under the relevant counterpossibilities.

Several questions remain open:

1. **Identifying dependencies.** There is no general accepted algorithm for deciding which simulations, approximate reasoners, or proofs should track an intervention on \(D\), or by how much.
2. **Policy domain.** The footnote does not determine the input space, whether policies must be computable, or how to handle unavailable actions and unreachable histories.
3. **Randomization.** A policy may output a distribution over actions, but a predictor might know the distribution, the random seed, or neither. These are different models.
4. **Self-reference.** The decision procedure evaluates hypotheticals about its own output. A self-referential representation is possible in principle, but that does not establish that every proposed model has a unique, tractable solution.
5. **Updating and revision.** The reference perspective must be chosen without treating all evidence as either eternally fixed or automatically discarded. Footnote 16 does not resolve the general rule.

In practice, a P-FDT analysis should therefore expose its assumptions. Specify candidate policies and inputs; identify predictors, copies, and causal mechanisms; say which background uncertainties remain fixed or are resampled; compute the utility of each resulting hypothetical; and test whether the conclusion changes under plausible alternative dependency models.

## Conclusion

P-FDT extends functional decision-making from alternative actions to alternative **policies**. Its distinctive move is to evaluate the output of a decision procedure together with the predictors, copies, and downstream events that depend on that output, then apply the selected policy to the actual input.

The approach explains why predictable one-boxing, cooperation with an exact twin, or refusal of a sufficiently avoidable threat can be valuable without requiring backwards causation. Its central difficulty is equally clear: the source does not yet provide a general method for constructing the relevant logical counterfactuals or fixing the policy-selection perspective. P-FDT is therefore a powerful framework for posing decisions, but unfamiliar cases require explicit modeling rather than a stock list of prescribed actions.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, especially §§3–6, §9, and footnotes 7 and 16. [arXiv:1710.05060v2](https://arxiv.org/abs/1710.05060v2).