# P-FDT: choosing a policy as the output of a decision function

A decision can matter in ways that do not look like ordinary causal consequences of the act. A predictor may already have formed an expectation of what you will do. Another agent may be running the same reasoning in a separate room. Your future behavior may be predictable from the rule you use now. In each case, changing the present physical act while holding everything else fixed may miss a dependency relevant to the outcome.

**Policy functional decision theory (P-FDT)** approaches such cases by evaluating alternative *outputs of a policy-selection procedure*. A policy maps inputs—such as observation histories—to actions. P-FDT asks which policy, considered as the output of its own decision procedure, has the best consequences once the relevant causal and computational dependencies are propagated. It then applies the selected policy to the input it has actually received.

The primary source for this account is footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory*. The paper’s main text gives an action-selection formalization; the footnote says the authors’ preferred formulation instead intervenes on the decision function “to choose not an action but a **policy** which maps inputs to actions, to which the agent then applies her inputs in order to select an action.” Footnote 7 likewise says that the preferred procedure iterates over policies.

That is a compact specification, not a complete mathematical theory. In particular, the paper does not fully define how a policy-level intervention changes other agents, how the policy’s domain is chosen, or how all observations enter evaluation. The formal rule developed below is an operational interpretation of the footnote, informed by the paper’s treatment of functional counterfactuals. Where it goes beyond the source, I will say so.

## From acts to policy outputs

Let \(X\) be a set of possible inputs, \(A\) a set of actions, and

\[
\Pi\subseteq \{\,\pi:X\to A\,\}
\]

a set of admissible policies. For sequential problems, an input can be an entire observation-and-action history; the policy then says what to do at each history. Let \(U\) assign a real-valued utility to outcomes.

Suppose a policy-selection computation \(S\), supplied with a model \(M\) and whatever other planning information its design requires, outputs a policy. Write \(D\) for the variable in \(M\) representing that output. The distinction is important: \(D\) is a *representation* of the computation’s result, which can be manipulated in a hypothetical model; the actual computation \(S\) produces the policy that the agent uses.

A schematic P-FDT rule is

\[
\pi^*\in\operatorname*{arg\,max}_{\pi\in\Pi}
\mathbb E_{M^{D\leftarrow\pi}}[U],
\qquad
a=\pi^*(x_{\mathrm{actual}}).
\tag{1}
\]

Here \(M^{D\leftarrow\pi}\) is a hypothetical model in which the policy-output node \(D\) is set to \(\pi\), with the consequences propagated through the model’s relevant dependencies. Equation (1) is a proposal for making the footnote operational, not an equation supplied by the paper.

The intervention is not merely a physical replacement of the agent’s action at the current moment. Nor is it necessarily the ordinary causal intervention of installing a different program in one body. It is a *functional* intervention: when other processes depend on the same computation or accurately model its output, their behavior may change in the hypothetical too.

The policy is then applied to the actual input. Thus a single candidate can say “one-box if I see a full box, two-box if I see an empty box.” Evaluating that candidate includes both branches, with probabilities determined by the hypothetical model. A policy is not just a promise about the branch currently visible.

This distinction is especially useful when observations and the opportunity to act depend on predictions about the policy. It can also matter in multi-agent settings: the paper says policy selection may differ from its action-selection formalization there, but does not supply a general theorem specifying when.

## What changes in a P-FDT hypothetical?

The source calls the relevant relation **subjunctive dependence**. It includes ordinary causal dependence: if an action triggers a machine, the machine’s response changes when the action changes. It also includes dependence arising from shared computations or accurate models: two correctly functioning calculators given the same sum give the same answer, even if neither causes the other’s output.

A useful way to construct a candidate hypothetical is:

1. Represent the policy-selector output \(D\), the agent’s inputs and actions, relevant predictors or other decision-makers, and utility.
2. Set \(D=\pi\) for one candidate policy.
3. Recompute processes represented as depending on \(D\), including physical downstream effects and appropriately linked predictions or copies.
4. Leave unrelated background processes governed by their original distributions.
5. Calculate expected utility over the resulting possible trajectories.
6. Compare policies and apply the selected policy to the actual input.

“Appropriately linked” does substantial work. A predictor might simulate the selector, infer its output imperfectly, inspect only one branch of the policy, or use evidence correlated with the agent without computing the selector at all. The model should represent the mechanism actually supposed by the problem. An observed correlation alone does not establish that a functional intervention should preserve it.

For comparison, **causal decision theory (CDT)** ordinarily evaluates an act by intervening on the physical action and propagating causal consequences. **Evidential decision theory (EDT)** evaluates an act by conditioning on having taken it. P-FDT instead evaluates an intervention on a policy-selection output. The three can agree in ordinary cases but disagree when predictions, shared computations, or merely statistical common causes are involved.

The source’s own graphical formalization uses a \(\operatorname{do}\)-like operation on a logical decision-function node. That notation should not conceal the difficulty: a deterministic computation on fixed inputs has one logically fixed output. Setting it to another value is a **counterpossible**—a hypothetical whose antecedent is contrary to a mathematical fact. The paper acknowledges that it lacks a general account of how to construct these counterpossibilities or discover all relevant subjunctive dependencies. Equation (1) inherits that limitation.

## Newcomb’s problem under P-FDT

In Newcomb’s problem, an opaque box contains \$1 million if a predictor predicted one-boxing, and nothing otherwise. A transparent box contains \$1,000. The agent may take the opaque box alone or both boxes. Suppose, as a modeling assumption, that the predictor matches the selected action with probability \(0.99\), under each of the two candidate policy interventions.

For this one-input version, the policies are simply \(\pi_1=\) one-box and \(\pi_2=\) two-box. P-FDT evaluates

\[
V(\pi_1)=0.99(1{,}000{,}000)=990{,}000,
\]

\[
V(\pi_2)=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\]

It therefore selects one-boxing. This calculation assumes more than the bare statement that a predictor has been right 99% of the time: it assumes the specified accuracy persists under *each policy counterfactual*. A predictor’s aggregate past accuracy might not warrant that assumption for every candidate policy.

P-FDT does not claim that leaving the transparent box behind physically sends a signal into the past. Rather, its hypothetical for two-boxing changes the modeled output of the selector and, because the predictor is modeled as tracking that output, changes the earlier prediction as well. By contrast, CDT holds the already-filled box fixed when intervening on the act, and so takes both boxes.

The policy distinction becomes clearer if the opaque box is transparent. Suppose the predictor fills it according to what the agent would do *on seeing it full*. A candidate policy has two entries:

\[
\pi(\text{full}),\qquad \pi(\text{empty}).
\]

Under a perfect predictor, the policy “one-box if full, two-box if empty” produces a full box and \$1 million. A policy that two-boxes when full produces an empty box; taking both then yields \$1,000. On this model P-FDT selects the former policy and, when it actually sees the full box, one-boxes.

The striking feature is that the hypothetical for a different full-box response may itself contain an empty box. P-FDT is not denying the observation. It uses the observation to determine which action of the chosen policy to execute, while policy evaluation can range over trajectories in which that observation differs.

## Common causes are not predictors

Now consider the imaginary smoking-lesion problem. A lesion causes both a desire to smoke and a high risk of cancer; smoking itself does not cause cancer. Suppose smoking has a positive utility of 1,000 and that, in the relevant model, changing the selected policy does not change the lesion or cancer process.

If \(p\) is the probability of cancer in the background distribution used for the comparison, then

\[
V(\text{smoke})=(1-p)1{,}000{,}000+1{,}000,
\]

\[
V(\text{refrain})=(1-p)1{,}000{,}000.
\]

P-FDT smokes. An action’s being evidence of a lesion in a population does not, by itself, make the lesion depend on the output of this policy selector.

This is an intentionally simplified version. The paper observes that a fully specified lesion example must handle the agent’s information about her own preferences and the consistency of the supposed action–lesion correlation. Some versions of EDT can also smoke using a “tickle” defense. The point is not that every smoker must ignore correlations; it is that a P-FDT model must distinguish *how* a correlation arises before deciding which dependencies survive a policy intervention.

## Policies, observation, and the hitchhiker

Suppose a driver will rescue a stranded traveler only if she predicts that the traveler will pay \$1,000 after reaching town. Death in the desert has disutility equivalent to \$1 million. A policy can specify what to do at the town input even in hypothetical trajectories where the traveler never reaches town.

With a perfect predictor:

- A policy that pays in town leads to rescue and a cost of \$1,000.
- A policy that refuses in town leads to no rescue and a loss of \$1 million.

P-FDT selects the paying policy. If the traveler actually arrives in town, she applies it and pays.

With errors, the decision depends on their rates. If the driver rescues a would-be refuser with probability \(\varepsilon\), and otherwise leaves her in the desert, while a payer is rescued for certain, then

\[
V(\text{pay})=-1{,}000,\qquad
V(\text{refuse})=-(1-\varepsilon)1{,}000{,}000.
\]

Paying is preferred when \(\varepsilon<0.999\). Different error models yield different thresholds. The calculation must specify what happens under each policy, including mistaken rescue and mistaken refusal of rescue; “the driver is reliable” alone is not enough.

There is an unresolved issue behind this example. Should the distribution used to evaluate policies incorporate the current observation that the traveler is in town? The paper’s main action-based formalization does not simply condition on every current observation; it uses the observation to select the decision-function node intervened upon. Footnote 16 says to select a policy and apply the input, but does not fully specify the corresponding policy-level treatment of evidence.

A reasonable operational proposal is to fix a **planning perspective**: condition on background information taken as given for the policy-selection problem, but allow observations generated by the modeled interaction to vary across policy hypotheticals. The policy then specifies responses to those observations. This reproduces the hitchhiker reasoning above. It is not a general theorem of footnote 16: where to draw the boundary around the planning perspective remains a substantive choice, especially when the agent learns that its model was wrong.

## Multi-agent P-FDT: same policy, different inputs

Consider the psychological-twin prisoner’s dilemma. Each player receives \$1 million if both cooperate and \$1,000 if both defect; unilateral defection gains the defector \$1,001,000 and leaves the cooperator with nothing. The players are in separate rooms but are assumed to implement the same selector on the same relevant input.

If the model links both players to the same policy output, then under the cooperation policy both cooperate, and under the defection policy both defect:

\[
V(\pi_C)=1{,}000{,}000,\qquad
V(\pi_D)=1{,}000.
\]

P-FDT cooperates. The reason is neither altruism nor a physical effect of one player’s move on the other’s. It is the stipulated computational dependence.

Policy selection makes a further distinction possible. Suppose two copies receive different inputs, \(x_L\) and \(x_R\), but both apply the same selected policy. Then one intervention \(D\leftarrow\pi\) can change both \(\pi(x_L)\) and \(\pi(x_R)\), even when those actions differ. For example, if the players must choose opposite sides, the policy

\[
\pi(x_L)=L,\qquad \pi(x_R)=R
\]

may coordinate them better than either constant policy. A single action-level intervention at \(x_L\), without a rule connecting it to \(x_R\), need not capture that coordination.

This is an illustration of a possible policy-level difference, not a result proved in the paper. Shared use of P-FDT does not automatically establish a shared policy-output node: agents may have different models, utilities, inputs to their selectors, or independently selected policies. If one player certainly defects regardless of the selector’s output, P-FDT should model that player as fixed; in the stated payoff table, defection is then better for the other player.

For imperfect similarity, one needs a graded dependency model. If cooperation by the agent is matched by the other with probability \(q_C\), while defection is matched by defection with probability \(q_D\), then, in thousands of dollars,

\[
V(C)=1000q_C,\qquad
V(D)=1q_D+1001(1-q_D).
\]

Cooperation is preferred exactly when

\[
1000q_C>q_D+1001(1-q_D).
\]

These probabilities must describe responses *under the two functional interventions*. Simply observing that the agents often agree does not determine them.

## Open choices in applying P-FDT

Several choices remain indispensable when using P-FDT on an unfamiliar case.

**Policy scope.** A policy might cover one decision, all histories in an episode, or a much broader class of situations. Too narrow a domain may omit dependencies with other inputs; too broad a domain may create an intractable optimization and force decisions about remote situations. Footnote 16 does not settle the scope. A practical proposal is to include histories that the model identifies as relevant to the present interaction, while making the boundary explicit.

**Identity and implementation.** A policy as an extensional map can be represented by different programs. If a predictor responds only to the map’s actions, extensional policies may suffice. If it inspects code, runtime, or proof structure, the representation of the policy or selector is itself outcome-relevant. The model must then say whether candidates are maps, implementations, or richer objects; these choices can change the answer.

**Randomization.** A randomized policy may map inputs to distributions over actions. But whether a predictor can predict the random seed, or whether two copies share randomness, matters. A policy that assigns probability \(1/2\) to each action is not automatically equivalent to a private, unpredictable coin flip. The source’s policy passage does not specify a general treatment of these cases.

**Self-reference and existence.** The selector evaluates counterfactual outputs of itself. The paper notes that self-representation is possible in principle, but that does not prove that every proposed self-referential model has a unique, computable optimum. Finite policy sets and a fixed tie-breaking rule make equation (1) easier to use; they do not solve the general construction of functional counterfactuals.

**Model uncertainty.** The graph or other dependency representation is an input to the calculation, not something supplied automatically by the name P-FDT. In practice an agent may need to average over plausible dependency models, test sensitivity to predictor error rates, or decline to infer a strong link from weak evidence.

These qualifications also limit broad claims of success. The paper argues that functional decision-making performs well in many “fair” problems—roughly, problems that reward behavior rather than membership in a named decision-theory class. It also concedes that no theory wins every deliberately constructed problem and that a satisfactory formal definition of fairness remains open. P-FDT’s attractive results in examples are reasons to investigate its rule, not a proof of universal optimality.

## Conclusion

P-FDT’s central move is to select a **policy** by evaluating hypothetical outputs of the policy-selection computation, then apply that policy to the actual input. Its counterfactuals propagate relevant causal and computational dependencies, rather than preserving every correlation or changing only the present physical act.

The footnote supplies the policy-selection idea; it does not settle the semantics needed for every case. With an explicit policy domain, planning perspective, dependency model, and treatment of prediction and randomness, P-FDT becomes a usable framework for analyzing unfamiliar problems. Its deepest open question is how to justify and construct those functional counterfactuals reliably.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, especially footnotes 7 and 16. https://arxiv.org/abs/1710.05060v2