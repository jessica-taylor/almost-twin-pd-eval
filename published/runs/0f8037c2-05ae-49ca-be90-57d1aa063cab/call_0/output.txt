# Policy Functional Decision Theory: Choosing the Best Output of a Policy-Selection Function

Policy functional decision theory, which I will call **P-FDT**, is the policy-selection version of the decision theory presented by Yudkowsky and Soares in “Functional Decision Theory: A New Theory of Instrumental Rationality.” The paper’s main text usually describes an agent choosing an action by asking which output of her decision function would produce the best outcome. But the authors’ preferred formulation, given in footnote 16, says that the agent “intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action.” They add that “the difference only matters in multi-agent dilemmas so far as we can tell.”

That short passage is the primary source for P-FDT in this essay. The source does not give a full formal equation for the policy version, so part of what follows is reconstruction. I will try to separate what the source itself says from additional operational assumptions that seem needed to make P-FDT usable on unfamiliar problems.

The central idea is this: a P-FDT agent does not first ask, “Which physical act should I perform?” Instead, she asks, “Which policy should my decision procedure output?” A policy is a function from possible inputs—observations, information states, decision histories—to actions. Once the agent has selected the policy with the best counterfactual consequences, she applies her actual input to that policy and performs the resulting action.

## 1. P-FDT in relation to EDT, CDT, and action-level FDT

To locate P-FDT, it helps to compare it with three nearby rules.

Evidential decision theory, **EDT**, chooses an action by conditioning on it:

\[
\mathrm{EDT}(P,x)=\arg\max_{a\in\mathcal A}\mathbb E[V\mid X=x, A=a].
\]

Here \(P\) is the agent’s probability model, \(X\) is an observation history, \(A\) is the physical action, and \(V\) is utility. EDT asks which action would be the best news.

Causal decision theory, **CDT**, chooses by intervening on the physical action variable:

\[
\mathrm{CDT}(P,G,x)=\arg\max_{a\in\mathcal A}
\mathbb E[V\mid \operatorname{do}(A=a), X=x],
\]

where \(G\) encodes causal structure and \(\operatorname{do}\) is Pearl-style surgery. CDT asks which physical act causes the best downstream outcome.

The action-level formulation of functional decision theory, as in the main text of the source, intervenes not on the physical act but on a variable representing the output of the agent’s decision procedure:

\[
\mathrm{FDT}_{\text{action}}(P,G,x)=\arg\max_{a\in\mathcal A}
\mathbb E[V\mid \operatorname{do}(\mathrm{fdt}(P,G,x)=a)].
\]

The variable \(\mathrm{fdt}(P,G,x)\) represents what the agent’s decision function outputs when given model \(P\), dependency structure \(G\), and input \(x\).

**P-FDT** generalizes this by making the output of the decision function a policy rather than a single action. Let \(\Pi\) be a set of feasible policies, where each policy is a function

\[
\pi:\mathcal X\to\mathcal A.
\]

Let \(D_{P,G}\) be a variable representing the policy output by the P-FDT policy-selection function given the agent’s model. Then a natural P-FDT rule is:

\[
\pi^*\in\arg\max_{\pi\in\Pi}
\mathbb E[V\mid \operatorname{do}(D_{P,G}=\pi)],
\]

and the actual action given input \(x\) is

\[
\mathrm{P\text{-}FDT}(P,G,x)=\pi^*(x).
\]

This equation is not stated explicitly in the source. I take it to be the most direct mathematical elaboration of the footnote: intervene on the policy-output node, then apply the actual input.

The important difference from action-level FDT is that P-FDT evaluates whole input-output rules. Two policies may agree on the action taken at the actual observation but differ at other possible observations. P-FDT can still distinguish them, because predictors, other agents, or counterfactual observations may depend on the entire policy.

## 2. The model: policies, interventions, and subjunctive dependence

A P-FDT problem is represented by a pair \((P,G)\).

- \(P\) is a probability distribution over relevant variables: observations, predictions, actions, outcomes, utility, and logical/computational variables.
- \(G\) is a dependency graph telling us how those variables would change under interventions.
- \(D_{P,G}\) is a variable naming the policy selected by the agent’s P-FDT procedure.
- \(X\) is the observation or input history to which the policy is applied.
- \(A\) is the action, typically given by \(A=\pi(X)\) when \(D_{P,G}=\pi\).
- \(V\) is utility.

The graph \(G\) is not merely a causal graph in the ordinary sense. It must also represent what the source calls **subjunctive dependence**: dependence that arises when one system computes, predicts, simulates, or reliably models the output of another system. The source’s slogan is that functional decision theory relates to subjunctive dependence as CDT relates to causal dependence. For P-FDT, the slogan becomes: P-FDT intervenes on a policy variable and preserves all decision-relevant subjunctive dependencies of that policy variable.

Thus, when P-FDT compares policies \(\pi\) and \(\pi'\), it does not ask:

\[
P(V\mid \pi)
\]

as ordinary evidential conditioning. Nor does it ask what would happen if only the physical action changed while predictors remained fixed, as CDT does. It asks what the world would look like if the P-FDT procedure output \(\pi\) rather than \(\pi'\), holding fixed everything not subjunctively dependent on that procedure.

This requires counterpossible reasoning. If the agent is deterministic, then the P-FDT procedure has exactly one actual policy output. Imagining that it outputs a different policy is imaginingsomething counter-to-logic, like imagining that a correct calculation of \(6288+1048\) gives a different answer. The source acknowledges this as an open technical difficulty. For practical purposes, however, we can often represent the relevant counterpossibles structurally: we write down equations for predictors, observations, and outcomes as functions of the policy variable, then intervene on that variable.

A useful operational rule is:

1. Identify the agent’s P-FDT policy-selection computation.
2. Introduce a variable \(D_{P,G}\) for its policy output.
3. Draw arrows from \(D_{P,G}\) to anything that computes, predicts, or reliably depends on that output.
4. Draw arrows from those predictors to observations, payoffs, and other agents’ actions.
5. Do not draw arrows from \(D_{P,G}\) to variables that are merely statistically correlated with the agent’s behavior through a common cause.

Step 5 is what separates P-FDT from EDT. A lesion that causes both smoking and cancer is statistically associated with smoking, but it does not compute or predict the agent’s policy. Therefore, in P-FDT’s hypotheticals, changing the policy output does not change the lesion.

## 3. How P-FDT evaluates policies

The expected utility of a policy \(\pi\) is

\[
\mathrm{EU}(\pi;P,G)
=
\mathbb E[V\mid \operatorname{do}(D_{P,G}=\pi)].
\]

Equivalently, if outcomes \(o\in\mathcal O\) have utilities \(\mathcal U(o)\),

\[
\mathrm{EU}(\pi;P,G)
=
\sum_{o\in\mathcal O}
P(o\mid \operatorname{do}(D_{P,G}=\pi))\mathcal U(o).
\]

P-FDT then chooses a policy maximizing this quantity and executes its recommendation at the actual input:

\[
\pi^*\in\arg\max_{\pi}\mathrm{EU}(\pi;P,G),
\qquad
a^*=\pi^*(x).
\]

This means P-FDT does not evaluate isolated actions except as parts of policies. If someone asks, “Should I take both boxes now that I see both are full?” P-FDT does not evaluate the physical act of two-boxing while holding the observation fixed. It asks which policy—“one-box if full” or “two-box if full,” together with specified behavior in other possible inputs—has the best global consequences when predictors and observations are allowed to depend on that policy.

A subtle point concerns conditioning on the actual observation. If the observation is known to be exogenous—meaning it does not subjunctively depend on the policy—then one may safely condition on it:

\[
\mathrm{EU}(\pi;P,G,x)
=
\mathbb E[V\mid \operatorname{do}(D_{P,G}=\pi), X=x].
\]

But in Newcomblike problems, observations are often produced by predictors who predict the agent’s policy. In those cases, conditioning on the observation would break the very dependence P-FDT wants to preserve. The source’s discussion of “updateless” reasoning suggests that the agent should often evaluate policies from a perspective prior to treating the observation as fixed evidence, and then apply the chosen policy to the observation. This is one of the places where the footnote is underdeveloped; I will return to it in Section 7.

## 4. Example: Newcomb’s problem

In Newcomb’s problem, the agent may take only box B, or both boxes A and B. A predictor filled box B with \$1,000,000 iff she predicted the agent would one-box. Box A contains \$1,000. Suppose the predictor is 99% accurate.

There is only one relevant input, so policies reduce to actions. Let

\[
\pi_1(\varnothing)=\text{one-box},
\qquad
\pi_2(\varnothing)=\text{two-box}.
\]

The graph contains a policy node \(D\), a prediction node, a box-contents node, an action node, and a utility node. The predictor’s prediction subjunctively depends on \(D\). Therefore:

\[
P(\text{box full}\mid \operatorname{do}(D=\pi_1))=0.99,
\]

and

\[
P(\text{box full}\mid \operatorname{do}(D=\pi_2))=0.01.
\]

Expected utilities are approximately

\[
\mathrm{EU}(\pi_1)=0.99(1{,}000{,}000)+0.01(0)=990{,}000,
\]

and

\[
\mathrm{EU}(\pi_2)=0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000.
\]

P-FDT selects \(\pi_1\), so the agent one-boxes.

CDT two-boxes because it intervenes on the physical action and holds the box contents fixed. EDT one-boxes because conditioning on one-boxing is good news. P-FDT one-boxes for a reason closer in form to CDT’s: it uses an intervention, but the intervention target is the policy output of the decision procedure, not the physical movement of the agent’s hands.

## 5. Example: the smoking lesion problem

In the smoking lesion problem, smoking is correlated with cancer, but only because a lesion causes both a disposition to smoke and cancer. Smoking itself does not cause cancer. Smoking gives \$1,000 of utility; avoiding cancer is worth \$1,000,000.

EDT refrains from smoking because smoking is bad news: it evidences the lesion. CDT smokes because smoking does not causally affect cancer. P-FDT also smokes.

The crucial modeling claim is that the lesion is not subjunctively dependent on the output of the agent’s P-FDT policy-selection function. The lesion may influence the agent’s tastes, and perhaps which utility function the agent has, but it does not compute the P-FDT policy. Therefore, when P-FDT compares the policies

\[
\pi_S(x)=\text{smoke},
\qquad
\pi_R(x)=\text{refrain},
\]

the intervention \(\operatorname{do}(D=\pi_S)\) changes the probability of smoking but does not change the probability of having the lesion or cancer. Schematically,

\[
P(\text{cancer}\mid \operatorname{do}(D=\pi_S))
=
P(\text{cancer}\mid \operatorname{do}(D=\pi_R)).
\]

Since smoking adds utility without changing cancer risk, P-FDT chooses the smoking policy.

The source’s formal treatment of the lesion problem is more delicate because the lesion can affect the agent’s preferences, producing uncertainty about which decision function the agent is running. But the essential P-FDT conclusion is the same: the policy intervention preserves the decision-relevant structure and breaks merely evidential correlations. P-FDT neither “manages the news” nor ignores causal structure.

## 6. Example: transparent Newcomb and Parfit’s hitchhiker

P-FDT becomes especially illuminating in cases where the agent receives an observation that appears to make the optimal local action obvious.

In the transparent Newcomb problem, both boxes are transparent. The predictor filled box B iff she predicted the agent would one-box upon seeing two full boxes. If the agent sees that both boxes are full, should she take both?

EDT and CDT say yes: given that box B is full, taking both yields \$1,001,000 rather than \$1,000,000. But P-FDT says no.

Let the input \(x=\text{full}\) mean that the agent sees both boxes full. Consider two policies:

\[
\pi_O(\text{full})=\text{one-box},
\qquad
\pi_O(\text{empty})=\text{two-box},
\]

and

\[
\pi_T(\text{full})=\text{two-box},
\qquad
\pi_T(\text{empty})=\text{two-box}.
\]

The predictor’s prediction depends on the policy. If the agent follows \(\pi_O\), the predictor usually predicts one-boxing upon seeing full boxes and fills box B. If the agent follows \(\pi_T\), the predictor usually predicts two-boxing and leaves box B empty.

With 99% accuracy:

\[
\mathrm{EU}(\pi_O)
\approx
0.99(1{,}000{,}000)+0.01(1{,}000)
=
990{,}010,
\]

while

\[
\mathrm{EU}(\pi_T)
\approx
0.01(1{,}001{,}000)+0.99(1{,}000)
=
11{,}000.
\]

P-FDT therefore selects \(\pi_O\). When the agent actually sees two full boxes, she applies the policy and one-boxes.

This looks strange if one focuses only on the local branch: given full boxes, two-boxing seems to gain \$1,000. But P-FDT treats the observation “full boxes” as itself policy-dependent. If the P-FDT procedure output a two-boxing policy, the agent would probably not be seeing full boxes. The counterfactual is not causal retrocausation; it is a subjunctive dependence between the policy and the predictor’s earlier prediction.

Parfit’s hitchhiker problem has the same structure. An agent is stranded in a desert. A driver will rescue her only if she sincerely promises to pay \$1,000 later. The driver is 99% accurate at detecting lies. Once in the city, should the agent pay?

CDT says no: payment causes no further benefit. EDT, conditional on being in the city, also says no. But P-FDT selects the policy “pay if in the city.” That policy makes the driver predict payment and rescue the agent. When the agent reaches the city, she applies the policy and pays. The source argues that this is equivalent to one-boxing in transparent Newcomb, and P-FDT gives the same diagnosis.

## 7. Observations, updatelessness, and open questions

The footnote giving P-FDT’s policy-selection idea is brief, and several questions remain unresolved.

First, the source does not specify exactly how observations enter the expected-utility calculation. The phrase “to which the agent then applies her inputs” suggests that the policy is selected first, and the actual observation is used afterward as an input to that policy. In predictor problems, this leads to an updateless flavor: the agent evaluates policies without conditioning on the actual observation if that observation is itself downstream of the policy.

This is necessary to get the desired behavior in blackmail and transparent Newcomb cases. If the agent conditions on seeing a full box or receiving a blackmail letter before evaluating policies, she severs the counterfactual connection between her policy and the observation. But P-FDT’s whole point is to preserve such connections when they are subjunctive rather than merely statistical.

I therefore propose the following operational distinction:

- If an observation is exogenous and not subjunctively dependent on the policy, P-FDT may condition on it.
- If an observation is produced by a predictor, simulation, or other process that depends on the agent’s policy, P-FDT should not condition it away during policy evaluation. Instead, the observation should be treated as an input to the selected policy.

This distinction is not fully formalized in the source. It is my interpretation of how to make the policy-selection idea workable.

Second, the source does not say how to choose the policy space \(\Pi\). In finite toy problems, we can list the relevant policies explicitly. In realistic problems, the space of mappings from observation histories to actions may be enormous or uncomputable. A bounded P-FDT agent would presumably maximize over a tractable class of policies or use approximations. The ideal theory needs a principled specification of feasible policies; the source does not provide one.

Third, the source does not say whether policies may be stochastic. A natural extension allows

\[
\pi:\mathcal X\to\Delta(\mathcal A),
\]

where \(\Delta(\mathcal A)\) is a distribution over actions. Then the expected utility of a policy includes both environmental randomness and policy randomness. But if predictors can predict the agent’s random choices or the random seed, those dependencies must be represented in \(G\). If the randomness is genuinely unpredictable by the environment, stochastic policies may help. If predictors are perfect, deterministic policies are usually the relevant objects.

Fourth, the source says the difference between action selection and policy selection matters mainly in multi-agent dilemmas, but it does not give a detailed example. A plausible interpretation is that other agents often respond not to a single action but to an agent’s contingent plan. In strategic settings, opponents or partners may predict an entire response function. P-FDT is naturally suited to such cases because it selects the response function as a single logical output.

For example, suppose another agent will cooperate only if she predicts that your policy will cooperate after observing her cooperative move. If your decision procedure outputs a policy, her prediction can target that policy. P-FDT can then ask whether the world in which it outputs a cooperative policy is better than the world in which it outputs a noncooperative policy. In such cases, the policy-level formulation may be more than a notational convenience.

Fifth, and most importantly, the source leaves open how to learn or construct the dependency graph \(G\). CDT can appeal, at least in principle, to Pearl’s account of causal discovery. P-FDT needs an account of how to discover subjunctive dependencies: which predictors, simulations, copies, or mathematical structures depend on the agent’s decision procedure. The source identifies this as a major open problem. In this essay, I have assumed that the problem description gives enough information to write down a toy graph. For real applications, that assumption is rarely safe.

## 8. P-FDT and blackmail: choosing the kind of agent to be

The policy perspective is especially clear in blackmail problems. In the mechanical blackmail problem discussed by the source, a blackmailer runs a program that will publish damaging information unless the agent pays \$1,000. She runs the program iff she predicts the agent will pay upon receiving the blackmail letter.

Let \(\pi_P\) be the policy “pay if letter received,” and \(\pi_R\) the policy “refuse if letter received.” If the blackmailer is a perfect predictor, then:

\[
\mathrm{EU}(\pi_R)
\]

corresponds to a world where the blackmailer predicts refusal and does not send the letter, while

\[
\mathrm{EU}(\pi_P)
\]

corresponds to a world where the blackmailer predicts payment and sends the letter.

Thus P-FDT selects \(\pi_R\). If the agent actually receives the letter, she refuses to pay. Locally, this seems harsh: given that the letter has arrived, paying \$1,000 appears much better than suffering \$1,000,000 in damages. But P-FDT evaluates the policy globally. Being the kind of agent who pays makes blackmail profitable; being the kind of agent who refuses makes blackmail unprofitable. P-FDT chooses the latter policy.

This illustrates a general feature of P-FDT: it may recommend an action that is worse on the actual branch, provided that the policy producing that action has better expected utility across the counterfactual branches that predictors and observations depend on. The source explicitly accepts this feature. It is also one of the places where P-FDT departs most sharply from ordinary act-centered reasoning.

## 9. What P-FDT tells an agent to do

For an unfamiliar decision problem, a P-FDT analysis can be organized as follows.

1. **Identify the inputs.** What observations or information histories might the agent face? Call this set \(\mathcal X\).

2. **Identify the feasible policies.** Define a set \(\Pi\) of mappings from \(\mathcal X\) to available actions.

3. **Build the dependency model.** Introduce a variable \(D_{P,G}\) for the output of the agent’s P-FDT policy-selection function. Connect it to predictors, other agents, observations, actions, and payoffs according to subjunctive dependence.

4. **Evaluate each policy.** For each \(\pi\in\Pi\), compute or estimate

   \[
   \mathbb E[V\mid \operatorname{do}(D_{P,G}=\pi)].
   \]

5. **Choose the best policy.** Let

   \[
   \pi^*\in\arg\max_{\pi\in\Pi}\mathbb E[V\mid \operatorname{do}(D_{P,G}=\pi)].
   \]

6. **Apply the actual input.** Perform

   \[
   a^*=\pi^*(x).
   \]

This procedure makes P-FDT a policy-centered expected-utility theory. It is not EDT, because it does not treat the policy as ordinary evidence. It is not CDT, because it does not intervene on the physical action alone. It is also not merely action-level FDT, because its primary object of choice is a complete mapping from inputs to actions.

## 10. Conclusion

P-FDT develops the central insight of functional decision theory—that rational choice should treat the decision procedure itself as the object of intervention—and pushes it to the policy level suggested by the source’s preferred formulation. Instead of choosing an act directly, the agent chooses a policy: a function from possible inputs to actions. The right policy is the one whose counterfactual output by the agent’s decision procedure leads to the best world, given all causal, logical, computational, and predictor-like dependencies.

The theory handles the classic cases well. It one-boxes in Newcomb’s problem, smokes in the smoking lesion problem, one-boxes in transparent Newcomb, pays in Parfit’s hitchhiker, and refuses blackmail when refusal deters blackmail. Its distinctive move is to evaluate policies while preserving subjunctive dependencies that CDT discards and that EDT mistakes for mere evidence.

At the same time, P-FDT remains incomplete as a formal program. The source gives no full equation for policy selection, no general account of how to construct dependency graphs, no settled treatment of stochastic policies, and no detailed specification of the multi-agent cases where policy selection is supposed to matter. The operational interpretation offered here—intervene on a policy node, evaluate expected utility updatelessly when observations are policy-dependent, then apply the actual input—is an attempt to make the footnote precise enough for use. If that interpretation is correct, P-FDT is a coherent and powerful extension of functional decision theory: a theory that asks not merely “What should I do?” but “What plan should this very decision procedure output?”

## Reference

Yudkowsky, E., and Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality.* arXiv:1710.05060v2. Especially footnote 16.