# P-FDT: choosing policies under logical dependence

A decision is not always an isolated physical event. Other people may predict it, machines may simulate it, and copies of the decision-maker may run the same reasoning in different circumstances. **Policy functional decision theory (P-FDT)** asks an agent to take these dependencies into account when selecting a rule for action.

The central source for P-FDT is footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory*. The authors say that their preferred formulation intervenes on the decision-function node to choose “not an action but a *policy* which maps inputs to actions,” and then applies the resulting policy to the agent’s inputs. The paper’s main formalism instead presents an action-selection version for simplicity. Footnote 7 similarly describes policies as mappings from observations to actions.

That distinction matters. A policy says what to do not only here, but at other inputs that may arise, including inputs presented to copies or considered by predictors. P-FDT evaluates candidate policies by asking what the world would be like if its policy-selection computation returned each candidate. It then acts according to the selected policy.

The footnote does not give a complete policy-level mathematical specification. In particular, it does not settle exactly which inputs a policy covers, what information is held fixed during its selection, or how logical dependencies are discovered. The formal rule developed below is therefore an **operational interpretation** of the footnote, using the paper’s broader account of subjunctive dependence. It should not be mistaken for a theorem supplied by the authors.

## From actions to policies

Let \(\mathcal X\) be a set of possible inputs and let \(\mathcal A(x)\) be the actions available at input \(x\). An input might include an observation history, the agent’s role in a game, available resources, and any other information the decision procedure is permitted to use. A deterministic policy is a function

\[
\pi:\mathcal X\longrightarrow \bigcup_{x\in\mathcal X}\mathcal A(x),
\qquad \pi(x)\in\mathcal A(x).
\]

For example, a policy for a transparent-box problem might specify

\[
\pi(\text{full})=\text{take only the opaque box},\qquad
\pi(\text{empty})=\text{take both}.
\]

The second instruction matters even when the agent actually sees a full box: a predictor may have chosen whether to fill it after considering the policy, and an alternative policy might lead to the empty-box input instead.

Write \(S\) for the mathematical computation that selects a policy, and \(Z\) for a variable in a world-model representing its output. Let \(U\) be utility and let \(M\) encode both probabilities and the relevant dependence structure. A schematic P-FDT rule is

\[
\pi^* \in \operatorname*{arg\,max}_{\pi\in\Pi}
V_M(\pi),
\qquad
V_M(\pi)=\mathbb E_M\!\left[U\mid
\operatorname{do}(Z=\pi)\right],
\qquad
a=\pi^*(x).
\tag{1}
\]

The intervention in (1) is **not** merely the physical replacement of an agent’s action. It is a model operation that supposes the policy-selection computation returns \(\pi\), then propagates that supposition through the dependencies represented in \(M\). It may change the agent’s action, predictions of that action, the behavior of relevant copies, and consequently the observation histories that occur.

The notation resembles causal intervention, but its interpretation is broader. The graph must represent mathematical and computational relationships as well as ordinary causal relationships. Equation (1) is useful only to the extent that those relationships have been modeled appropriately.

The output \(S\) and its representation \(Z\) must be distinguished. \(S\) actually returns one policy; \(Z\) is a variable manipulated inside a hypothetical. The computation can represent itself without already knowing its own output, although self-reference by itself does not prove that every proposed implementation terminates or has a well-defined optimum.

For comparison, a simple evidential decision theory (EDT) evaluates an action by \(\mathbb E[U\mid A=a,X=x]\): what would taking it be evidence of? A standard causal decision theory (CDT) evaluates it by intervening on the physical action \(A\), holding fixed variables not causally downstream. P-FDT instead intervenes on a policy output and preserves relevant dependencies of other processes on that output.

## What depends on a policy?

The paper calls the relevant relation **subjunctive dependence**. Causal effects are included: a written instruction may depend causally on the policy that produced it. But dependence can also arise because two systems compute, represent, or predict the same thing, even without a signal passing between them.

A useful working classification is:

1. **Ordinary causal consequences.** If \(\pi(x)\) changes an action, downstream physical consequences change.
2. **Copies and shared computations.** If another system applies the same selected policy, its action changes from \(\pi(x')\) to the alternative policy’s value at its own input \(x'\).
3. **Predictors.** If a predictor models the policy or its action at a particular input, its prediction may change when the hypothetical policy changes, subject to modelled errors.
4. **Independent background facts.** A fact merely correlated with actual behavior need not change. Its relationship to the policy must be justified, not inferred from correlation alone.

This last point distinguishes P-FDT from simply conditioning on one’s action. Suppose a lesion causes both a desire to smoke and cancer, but smoking itself has no effect on cancer. In a model where replacing the policy does not alter the lesion or cancer, a policy that smokes when the agent enjoys smoking gains the benefit of smoking without changing the probability of cancer. The paper notes that formal versions of this example require care about the agent’s knowledge of its desires and about the population generating the correlations. The lesson is conditional on the model: **do not make a background fact vary with a policy merely because it is statistically associated with the action.**

Conversely, neither resemblance nor a shared label automatically makes another agent’s action vary. A human opponent using different information and reasoning may respond to a policy, predict it imperfectly, or not be related to it at all. The dependence must be included with whatever strength the evidence warrants.

### Counterfactuals that may be counterpossible

If \(S\) is a fixed deterministic computation, it has one actual output. The supposition that this same computation returns another policy may therefore be logically false, not merely physically unrealized. The paper acknowledges the resulting need for *counterpossible* reasoning and does not provide a general theory of it.

A structural graph can stipulate how selected consequences change under such a supposition. For instance, it can stipulate that an accurate simulation changes its reported result when \(Z\) changes. But graph surgery does not explain how to derive all correct logical dependencies, or how to preserve consistency among overlapping computations. These are inputs and open research problems, not solved by writing \(\operatorname{do}(Z=\pi)\).

Nor does P-FDT claim that an action sends a signal into the past. A past predictor’s output and a later action can both depend on the same decision computation. Changing the represented computation in a hypothetical can therefore change both, even though the actual physical action cannot causally alter a past prediction.

## P-FDT in Newcomb’s problem

An opaque box contains \$1 million if a predictor predicted one-boxing, and nothing otherwise. A transparent box contains \$1,000. The agent may take only the opaque box or take both. Suppose that, under either policy intervention, the predictor gets the relevant action right with probability \(0.99\).

For constant one-box and two-box policies,

\[
V(\pi_{\rm one})=0.99(1{,}000{,}000)=990{,}000,
\]
\[
V(\pi_{\rm two})=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\]

P-FDT selects the one-box policy. The calculation assumes *intervention-relative* predictor accuracy: changing the policy in the model changes the prediction with the stated reliability. An observed 99% accuracy rate across a population does not, by itself, establish that same relationship for every policy intervention. One needs a model of what the predictor actually tracks.

A CDT agent, by contrast, holds the already-filled box fixed under a physical-action intervention and takes both boxes. An EDT agent ordinarily one-boxes because one-boxing is good evidence that the box was filled. P-FDT’s reason differs from both: it evaluates the policy together with a predictor whose output depends on that policy.

## Transparent boxes and the role of information

Now let the agent see whether the large box is full. The predictor fills it if it predicts that the agent would one-box *upon seeing it full*. Assume 99% accuracy about that conditional action.

Consider two policies, both taking both boxes when the large box is empty:

\[
\pi_C(\text{full})=\text{one-box},\qquad
\pi_D(\text{full})=\text{two-box}.
\]

Under \(\pi_C\), the box is full with probability \(0.99\); when it is empty, the agent takes the \$1,000 box:

\[
V(\pi_C)=0.99(1{,}000{,}000)+0.01(1{,}000)=990{,}010.
\]

Under \(\pi_D\), the box is full only when the predictor errs:

\[
V(\pi_D)=0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000.
\]

Thus this interpretation selects \(\pi_C\). If the agent sees a full box, it leaves the \$1,000 behind. In the alternative-policy hypothetical, the observation itself is usually different: a predictor expecting two-boxing usually leaves the large box empty.

This does **not** mean the agent believes the box it actually sees is empty, or refuses to use observations. Rather, it uses observations as inputs to the selected policy while evaluating policies from a perspective that does not automatically hold policy-dependent observations fixed. Conditioning on “full” *after* changing the policy would produce a different criterion and, in this example, can erase the predictor-sensitive advantage.

Where should the evaluation perspective come from? Footnote 16 does not say. A reasonable proposal is to choose a **baseline information state** containing facts taken as available to the policy selector, while treating later observations that depend on the policy as variables in its hypothetical model. Evidence genuinely independent of the policy can be incorporated into that baseline. The choice is substantive: changing which information is fixed can change the answer. It is not justified to declare every inconvenient observation irrelevant, nor to condition indiscriminately on an observation whose occurrence the candidate policy affects.

The same structure appears in Parfit’s hitchhiker. A driver gives a ride only if she predicts payment upon arrival. A policy that pays at the destination can obtain the ride; a policy that refuses may never reach the payment decision. On the model’s assumptions, P-FDT can select the paying policy even though, once safely in town, payment has no further causal benefit.

## Why whole policies matter in multi-agent cases

For identical inputs, action-level and policy-level interventions may coincide. Different inputs make the distinction visible.

Imagine two copies running the same policy selector, one assigned role \(L\), the other role \(R\). Each observes its role and must choose red or blue. Both receive utility \(10\) if their colors differ and \(0\) if they match. Suppose their policy is a shared function of role. The four deterministic policies have these consequences:

| Policy | \(L\)’s action | \(R\)’s action | Utility to each |
|---|---:|---:|---:|
| \(\pi_{RR}\) | red | red | \(0\) |
| \(\pi_{RB}\) | red | blue | \(10\) |
| \(\pi_{BR}\) | blue | red | \(10\) |
| \(\pi_{BB}\) | blue | blue | \(0\) |

Under a shared-policy intervention, both implementations use the same candidate mapping at their respective inputs. P-FDT selects one of \(\pi_{RB}\) and \(\pi_{BR}\), with a common tie-breaker if the agents must coordinate on the same result. They then take different actions.

A simultaneous intervention that forces the *same action* at both roles cannot represent either successful policy. Conversely, changing only \(L\)’s action while holding \(R\)’s fixed may discard the stipulated shared-policy dependence. Whole-policy selection captures the possibility that one shared rule produces **different outputs on different inputs**.

This example depends on genuinely shared policy selection and compatible models and tie-breaking. It does not show that any two P-FDT agents necessarily coordinate: distinct roles, preferences, code, private information, or independent random seeds can weaken the dependency. Stochastic policies also require a further choice: identical distributions need not imply identical random outcomes. A model should represent whether randomness is shared, independently sampled, or predictable.

The familiar psychological-twin prisoner’s dilemma is a simpler case. If the twins run the same procedure on the same relevant input, cooperation yields each \$1 million, while mutual defection yields each \$1,000. A shared-computation intervention compares those outcomes and favors cooperation. It is not a general license to cooperate against an opponent who will defect regardless.

## Applying P-FDT to an unfamiliar problem

A practical analysis can be organized as follows.

**1. Define inputs, actions, and utility.** Specify what the policy can observe, which actions are available at each input, and whose utility is being optimized. A policy cannot condition on facts its input does not reveal.

**2. Choose the candidate policy class.** Include relevant contingent responses, including responses at observations that may not occur under the selected policy. If the class is restricted for computational reasons, the result is optimal only within that class.

**3. Identify the policy-selection output.** Ask which systems implement, simulate, or predict that output. Distinguish the whole policy from its application at one input.

**4. Build the dependence model.** Represent causal consequences, copies, predictors, errors, and independent background variables. State what each predictor tracks: source code, a simulation, a particular conditional action, or something else.

**5. Fix the evaluation perspective.** State which evidence is included in the baseline and which observations can change across policy hypotheticals. This is especially important when receiving a message, arriving at a place, or seeing a filled box is itself prediction-dependent.

**6. Evaluate each policy.** Propagate \(\operatorname{do}(Z=\pi)\), compute expected utility, and retain the maximizing policy. Finally apply it to the actual input.

**7. Check robustness.** Vary prediction accuracy, costs, and disputed dependencies. If small changes reverse the choice, a confident qualitative slogan is a poor substitute for the calculation.

For example, suppose a blackmailer starts a damaging program with probability \(p_P\) against a policy that pays and probability \(p_R\) against one that refuses. Paying costs \(c\) if blackmailed; refusing causes loss \(L\) if blackmailed. Ignoring other consequences,

\[
V(\pi_P)=-p_Pc,\qquad V(\pi_R)=-p_RL.
\]

Refusal is preferred precisely when \(p_RL<p_Pc\). It is not automatically correct whenever someone is called a blackmailer. Nor does high accuracy in other settings determine \(p_R\) and \(p_P\): those are assumptions about this predictor under the two policy interventions.

## Limits of the interpretation

Several questions remain open.

First, the policy space may be enormous or infinite. An optimum may not exist, calculation may be infeasible, and policies may need to be compared approximately. Tie-breaking must be specified, particularly when copies need to select the same coordinating policy.

Second, whole-policy intervention may be too coarse if a predictor tracks only part of a policy or if different copies use only partially shared computations. The model must say which components co-vary. Footnote 16 tells us to select a policy; it does not settle every granularity question.

Third, P-FDT’s comparison can diverge sharply from conditional advice after an observation. A policy may perform well overall while recommending an action that is costly in a rare observed situation—for example, refusing an erroneous blackmail threat. Whether that is rational is precisely part of the philosophical dispute, not something established merely by calling the calculation “global.”

Finally, the paper argues that its functional approach performs well in many “fair” problems, but admits that fairness is not formally settled and that any theory can be deliberately rewarded or punished. Neither footnote 16 nor equation (1) proves that P-FDT dominates all alternatives or always agrees with ideal precommitment. Such claims depend on the policy class, information perspective, dependence model, and environment.

## Conclusion

P-FDT replaces the isolated question “Which act should I perform?” with “Which output policy of this decision procedure has the best consequences, including the consequences of others predicting or implementing it?” Its distinctive step is to intervene on the **selected policy**, propagate relevant causal and computational dependencies, and then apply the policy to the actual input.

This gives a unified way to analyze predictors, copies, contingent commitments, and ordinary actions. Its power comes with a burden: the policy space, information baseline, and subjunctive dependencies must be made explicit. Where those are uncertain, P-FDT is best used as a disciplined framework for exposing the uncertainty, not as a shortcut around it.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, especially footnotes 7 and 16 and sections 3–6. [arXiv:1710.05060v2](https://arxiv.org/abs/1710.05060v2).