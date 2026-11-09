# 031_fdt_policy_qwen_qwen3.8-max-prime_rhigh_plow / 00015

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/0f8037c2-05ae-49ca-be90-57d1aa063cab/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/0f8037c2-05ae-49ca-be90-57d1aa063cab/call_0/response.raw) · finish: `stop`

### Visible response

```text
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
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request: write substantive mathematical essay ~2400-3000 words explaining P-FDT, taking policy-selection passage in footnote 16 as primary source. Need use P-FDT consistently, identify other theories by distinct names. Need explain best mathematical understanding, applications, uncertainties, additional assumptions. Need distinguish source claims vs own proposals. Need likely include equations, examples. Need finish brief conclusion. Need around 2400-3000 words including references? User says target approx 2,400–3,000 words, including references and any other material. Need likely produce around 2600 words. Need primary source footnote 16: "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition." Also earlier footnote 7: "In authors' preferred formalization of FDT, agents actually iterate over policies (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper." Need build P-FDT as policy functional decision theory. Need explain policy selection: choose policy pi: observations -> actions (or perhaps inputs to outputs) that maximizes expected utility when intervening on the output of the decision function that selects policy? Need careful. Source's action-based FDT equation: FDT(P,G,obs)=argmax_a E[V | do(FDTvar(P,G,obs)=a)]. For policy version: choose policy π from set Π of mappings from observations to actions by intervening on a variable representing the policy output of the decision procedure? Maybe equation: P-FDT(P,G,x) = argmax_{π∈Π} E[V | do(FDT-policy(P,G)=π)]? Then actual action = π(x). Need discuss observation handling: not conditionalizing on observation as EDT; instead observation determines which policy node/branch? In action-based FDT, observation changes intervention node FDT(P,G,x). In policy-based P-FDT, maybe the agent chooses a policy before/without conditioning on actual observation? Need parse. Footnote 16: "intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action." That suggests the decision function's output is a policy. The agent has inputs (observations) and applies the chosen policy to inputs to select action. The intervention is on node FDT(-) to choose policy, not action. Which inputs? The node FDT(-) maybe without observation? In mechanical blackmail: action-based graph has nodes FDT(P,G,blackmail) and FDT(P,G,∅), blackmailer determines which gets to set Act. If policy-based, there might be one node FDT(P,G) outputting policy π, then actual action = π(obs). The predictor may predict π or action at observations. This handles multi-agent dilemmas better? Need develop.

Need create coherent account. Primary source limited: footnote 16 and footnote 7. But can use whole paper for FDT context, but P-FDT primary source is policy-selection passage. Need explain P-FDT as variant of FDT that selects policies. Need maintain name P-FDT. Need distinguish EDT, CDT. Need examples: Newcomb, smoking lesion, transparent Newcomb, Parfit's hitchhiker, maybe voting, XOR blackmail. Need discuss policy vs action. Need show how P-FDT evaluates alternative policies: expected utility of counterpossible world where the agent's decision function outputs a particular policy π; then given actual input x, action π(x) is executed. Need define formal model.

Need consider uncertainties: source doesn't specify exact formal equation for policy selection, how to construct dependency graph G, how to choose policy set Π, how to handle stochastic policies, what observations count as inputs, whether policy is selected updatelessly, how to account for observations after policy selection, how to deal with dynamic consistency, multi-agent interactions. Need propose operational interpretation.

Need produce mathematical definitions. Let's design.

Let (P,G) be world model. Variables include:
- X ∈ 𝓧 observation/input history at decision time (or sequence).
- A ∈ 𝓐 action.
- V utility.
- Π variable representing policy chosen by P-FDT decision function: mapping π: 𝓧 -> 𝓐 (or partial mapping from possible observation histories to actions). Let D(P,G) or FDT_Π(P,G) denote variable for output of P-FDT policy-selection function given model. The source says intervene on node FDT(-) to choose policy, then apply inputs. So define:
P-FDT(P,G,x) = π^*(x), where
π^* ∈ argmax_{π∈Π} E_P[V | do(D(P,G)=π), maybe?].
Need decide whether conditioning on actual x? If policy selected based on model before observation? Source footnote says "to which the agent then applies her inputs". That implies no conditioning on actual observation at policy selection? But agent may have current observations as part of model? In action-based FDT, observation changes intervention node. In policy version, perhaps intervention is on D(P,G) (not D(P,G,x)), and actual action is determined by applying selected policy to x. But if the agent receives observation before choosing, should it choose policy conditional on that? Hmm.

In action-based FDT equation (4): FDT(P,G,obs)=argmax_a E[V | do(FDTvar(P,G,x)=a)]. It responds to observation by changing node intervened upon. The policy version footnote: "intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action." This suggests instead of many nodes FDT(P,G,x), there is one policy node FDT(P,G) outputting policy. Then observations are inputs to policy. The predictor may predict policy. The intervention is do(FDT(P,G)=π). Then X may be upstream? Need graph: D -> policy -> Act via X? Actually Act = π(X) if D=π and policy applied to X. If X is influenced by other variables (e.g., predictor sends letter iff predicted pay), then intervening on D=π may affect X through predictors because they predict policy/actions. Then expected utility integrates over X. The actual action is π(x*)? But when evaluating policies, do we condition on actual observation x*? The footnote says apply inputs after choosing policy. If actual x known, could choose policy that does well overall but action at x may be bad? Source's mechanical blackmail: Fiona receiving letter refuses because action-based FDT with observation intervenes on FDT(...,letter) and imagines world where not blackmailed. Policy-based updateless might choose policy "refuse if letter" because such agents aren't blackmailed. When holding letter, applies policy and refuses. It doesn't condition policy choice on having letter? It can choose policy from global perspective. If it conditioned on letter, might need to evaluate policy given letter? But P-FDT probably evaluates policy without conditioning on actual observation (updateless), or at least intervention on policy node affects probability of observations. However if actual observation is known and policy selected after, there is a tension: If policy selection occurs after observing x, the variable D may depend on x? Need define.

Maybe policy-selection P-FDT can be formulated as: At decision time with input x, the agent considers policies π, and chooses π maximizing E[V | do(FDT(P,G)=π)] (no conditioning on x), then executes π(x). This is updateless policy selection. It matches "apply her inputs" and handles blackmail/transparent Newcomb: choose policy that maps full box to one-box, letter to refuse; expected utility includes probability of seeing full box/letter. But if x is already known, selecting a policy that says do poorly at x? The agent may still follow because selecting policy based on global expected utility. This is like updateless decision theory. However footnote in source: "FDT says that agents should entertain the hypothesis that, if their action were different, they might have made different observations." For policy version, if policy were different, observations might differ. So evaluating policy may not condition on actual observation. Yet if actual observation is known, does P-FDT ignore it? It changes action via π(x), but not policy evaluation. This may be source's "lack of updating" UDT. But the source says "Fiona does change her behavior in response to evidence—by changing the place in her graph where she intervenes." In policy version, maybe not changing place? Hmm footnote 16 says preferred formulation intervenes on FDT(-) to choose policy, then applies inputs. Maybe there is still observation input to policy, but no separate nodes for each observation. The predictor may predict policy; action determined by policy and observation. If observation actual is known, can still use same policy node. The expected utility of policy is evaluated over possible observations, perhaps conditional on some prior and maybe on the fact that policy node output is being evaluated? If actual observation is known, should we condition on it? If we condition on X=x and intervene on policy π, then in blackmail, if condition on receiving letter, policy refuse leads to probability of letter? Can't change observation if conditioned. Unless intervention on policy changes X even under conditioning? Pearl do and conditioning: E[V | do(D=π), X=x] conditions on X=x after intervention? If X is downstream of D, do(D=π) changes distribution of X; conditioning on X=x then selects worlds where X=x despite policy, breaking dependency. That would make refuse not lead to no letter. So policy P-FDT likely does not condition on actual observation when evaluating policy. It is updateless. Then how use actual input? After choosing π, action = π(x). This yields refusing while holding letter because chosen policy says refuse if letter, despite knowing letter. It may choose policy based on prior, not conditional on letter. But if agent only exists after letter? Still policy chosen from perspective of prior? Need discuss uncertainty. The source's action-based FDT with observation changes intervention node but doesn't simply condition; it evaluates FDT(P,G,letter) with do(FDT(...,letter)=a) and somehow probability of being blackmailed changes? The text says in mechanical blackmail: upon receiving blackmail, solves FDT(P,G,blackmail); hypothetical pay: probability losing if blackmailed ~0 and probability being blackmailed ~1; refuse: probability losing if blackmailed ~1 but probability being blackmailed ~0. This is odd: they are evaluating conditional on receiving? It says "upon receiving" but hypothetical refuse imagines never blackmailed. So they are not conditioning on observation in usual way; they intervene on node FDT(P,G,blackmail), which maybe is the action given blackmail, but blackmailer determines whether that node controls action. Thus observation can be downstream. In policy version, simpler: intervene on policy node; observations downstream.

Need decide how to present. We can present two levels: source's action-based FDT and P-FDT operational extension. State source leaves exact formalization open; I propose a natural policy-selection semantics:

Define policy π: 𝓧 → 𝓐. Let D_Π(P,G) be variable denoting output of the P-FDT policy-selection function on model (P,G). For each candidate π, construct hypothetical P^π = P | do(D_Π=π) (with graph G encoding subjunctive dependencies, including predictors depending on D_Π or its consequences). The expected utility of π is
EU^P-FDT(π;P,G) = E_P[V | do(D_Π(P,G)=π)].
Then P-FDT chooses π^* ∈ argmax EU, and given actual observation x executes π^*(x). If the decision problem is explicitly indexed by an observation x and policies are only relevant at x, one may write P-FDT(P,G,x)=π^*(x).

But perhaps need incorporate observation in policy node? Source says FDT(-) maybe with inputs? Could write D_Π(P,G) outputs π; action variable is determined by A = D_Π(P,G)(X). Or more formally, variable Policy = FDT_Π(underline P, underline G); Act = Policy(Obs). For each π, intervention sets Policy=π, and Act becomes π(Obs). If predictors depend on Policy or Act, G propagates. This handles observations as inputs.

Need compare with action-based FDT equation. Action-based:
FDT_action(P,G,x)=argmax_a E[V | do(FDT(P,G,x)=a)].
Policy-based:
P-FDT(P,G,x)=π^*(x), π^*∈argmax_π E[V | do(FDT_Π(P,G)=π)].
This may be updateless. Need mention if one wants a local version, one can restrict to policies and condition on some fixed observation not affected by policy, but in Newcomblike cases observations are policy-dependent, so conditioning would break the desired dependence.

Need examples.

Example 1: Newcomb. Observations maybe none (or boxes). Policy set {one-box, two-box} trivial. P-FDT chooses π with π(∅)=one-box because do(Policy=one-box) makes predictor predict one-box and box full. EU one-box = .99*1,000,000 + .01*0? Actually if one-box: expected $990,000; two-box $11,000 (with 99% predictor). P-FDT one-boxes.

Smoking lesion: Policy maps maybe preferences? Observations none. Lesion is common cause of preference/action but not subjunctively dependent on decision function. Graph: Policy -> Act but Policy independent of Lesion/Cancer. do(Policy=smoke) doesn't change lesion probability; smoking adds $1000; chooses smoke. Need be careful source formalized lesion with two utility functions and two possible FDT nodes; in policy version, if lesion determines whether agent's utility function likes smoking, then P-FDT chooses policy under ignorance of own utility? Could simplify: policy selection uses actual utility function; if smoking enjoyable and no causal effect on cancer, choose smoke. If lesion influences desire to smoke but not decision function output? The source says lesion determines whether agent likes smoking, so decision function input includes utility. P-FDT might have policy node FDT(P_S,G) or FDT(P_R,G) depending on lesion. But policy selection can model as Act = Lesion ? FDT(P_S,G)(X) : FDT(P_R,G)(X). Under policy intervention for actual utility? Hmm. To keep essay clear, say in smoking lesion the policy node is not connected to cancer; intervention on policy changes smoking but not lesion/cancer; therefore P-FDT smokes. If preferences uncertain, choose policy maximizing expected utility over possible utility functions, but because smoking gives extra utility regardless of cancer, smoke.

Transparent Newcomb / Parfit's hitchhiker: Observation x=full boxes or city. Policy set includes mappings: if see full, one-box or two-box; if see empty, maybe two-box. P-FDT evaluates policies globally. π_one: if full one-box, if empty two-box. π_two: if full two-box, etc. Under do(Policy=π_one), predictor predicts one-box upon full, fills box, high chance see full and get $1M. Under do(Policy=π_two), predictor predicts two-box upon full, box empty, likely see empty and get $1k. So chooses π_one; when actual x=full, executes one-box. This explains paying driver: policy "pay if in city" causes driver to predict pay and give ride; when in city, pay.

Mechanical blackmail: Policy: if letter, refuse; if no letter, nothing. Under do(refuse-if-letter), blackmailer predicts refuse and doesn't send letter; high utility no blackmail. Under do(pay-if-letter), blackmailer sends letter; pay $1k. P-FDT chooses refuse policy. Upon receiving letter, refuses. This shows policy selection can recommend action that is locally dominated given observation (pay would save $999k? Actually if program running, paying costs 1k vs 1M; but globally refusal deters blackmail). Need explain.

Need discuss dependencies and counterfactuals: subjunctive dependence. P-FDT treats events as depending on decision function/policy when they are outputs or predictions of same computation or reliable models thereof. Interventions preserve logical/computational constraints. Unlike CDT, which intervenes on physical action A and severs correlations with predictors; unlike EDT, which conditions on A and preserves merely evidential correlations. P-FDT intervenes on Policy variable. Counterfactuals are counterpossibles: if the P-FDT function output a different policy, predictors/models would output corresponding predictions. Need mention source's open problem: no formal True operator or graph construction; P-FDT needs G encoding subjunctive dependencies. My operational assumption: use a structural model where variables for predictors, observations, actions are functions of policy variable and noise; edges indicate subjunctive dependence. In practice, identify predictors/copies/simulations/logical correlations.

Need discuss policy vs action: why policy? Source says only matters in multi-agent dilemmas. Need explain. In multi-agent settings, if each agent selects action after observing others or predicting others, selecting a policy can capture commitments across contingencies and avoid time inconsistency. For example, game with sequential moves or simultaneous agents with predictors. A policy maps information sets to actions; choosing policy lets P-FDT evaluate whole plan as one logical output. Other agents may predict policy, not just current action. In action-based FDT, agent might choose different actions at different observations in ways that are not jointly coherent; policy selection ensures the decision procedure's output is a complete plan. In multiplayer dilemmas, policy selection may affect how others model you across branches. Need maybe give example: voting coalition: each of ten voters chooses policy "vote if others like me?" But action-based maybe enough. Could mention policy is important in extensive-form games: threat/commitment, Parfit's hitchhiker is like sequential: driver predicts future pay policy. But source says action-based can handle with observation-specific nodes. Policy formalism makes it natural.

Need address unresolved choices:
- Source doesn't say whether P-FDT maximizes over deterministic or stochastic policies. Proposal: allow stochastic policies if world has randomness or predictors imperfect; expected utility over policy distributions. But if predictors predict randomization, need specify. Could restrict deterministic policies for simplicity; stochastic as mixture if predictors can't predict random bits. If policy includes random seed, subjunctive dependencies may differ.
- Source doesn't specify how observation x enters evaluation. Proposal: updateless policy evaluation (no conditioning on x if x is downstream of policy). If observation is exogenous and not subjunctively dependent on policy, conditioning on it is harmless; operational rule: condition only on observations known to be causally/exogenously fixed and not logically dependent on policy. But to stay P-FDT, perhaps policy selection from prior; actual x only selects action. Need justify: preserving dependencies between policy and observations is what gives correct transparent Newcomb/blackmail. If one conditions on actual observation, one collapses to action-like local reasoning and may two-box/pay.
- Source doesn't specify graph construction. Need say open; for applications, construct graph from problem description: predictor variable depends on policy/action; observations depend on predictor; action depends on policy and observation; utility depends on outcomes.
- Source doesn't specify how to select policy set. Proposal: finite set of feasible mappings from possible observations relevant to problem. If infinite, optimize over computable policies or bounded approximations.
- Need distinguish source claims vs own: Source claims FDT prefers policy formulation, intervenes to choose policy, difference only in multi-agent dilemmas as far as they can tell. My extension: exact equation, updateless evaluation, operational graph rules, stochastic policies, conditional exogenous observations. Need state.

Need maybe include formal notation:
Let 𝓧 be observation histories, 𝓐 actions. A policy π: 𝓧 → 𝓐. Let Π be feasible policies. Let D_π(P,G) be variable naming output of P-FDT's policy-selection computation on inputs (P,G). In graph G, D_π is exogenous intervention target. For candidate π, hypothetical distribution P_π satisfies:
P_π(·) = P(· | do(D_π=π)).
Within P_π, A = π(X) (or A_i = π_i(H_i) in dynamic setting). Expected utility:
EU(π) = ∑_v P_π(V=v) v = E_{P}[V | do(D_π=π)].
Then
π^* ∈ argmax_{π∈Π} EU(π),
P-FDT(P,G,x) = π^*(x).
If multiple policies tie, choose any; maybe tie-breaking.

Need mention if observation itself is part of decision function's input before policy output? Maybe define D_Π(P,G,x)? But footnote says choose policy then apply inputs. We can define policy-selection function maybe depends on model but not current observation? But what if agent has already observed x and policy selection function's input includes x? If D_Π(P,G,x) outputs policy, then applying x is redundant. To preserve updatelessness, D_Π takes model and maybe all possible inputs? Hmm. Could write D_Π(P,G) outputs π; x applied later. If the agent's beliefs P already incorporate all observations up to policy-selection time, then actual x may be part of P? But if x is part of P, then evaluating policy without conditioning? Need subtle. Maybe P is the model at the point before the relevant observation, or the agent's "prior" for the decision problem. But in realistic case, agent has observations. We can define P as the agent's epistemic state excluding the policy-dependent observation to be treated as input? Or P includes all exogenous evidence; X is a variable in G. For transparent Newcomb, agent sees box full before action; if P is after seeing full, then X=full with probability 1; evaluating policy do(π) with X downstream? If X is observed, how not condition? We might treat X as variable whose actual value is known but not conditioned upon in hypothetical? This is updateless: use prior over X before observation? But if P is updated to X=full, do(policy=one-box) cannot make X empty because P(X=full)=1. Source action-based handles by having observation nodes and intervention can change observation? They say when Fiona sees full, she envisions two-boxing and envisions likely sees empty. That means even though she observed full, hypothetical changes observation. So the model cannot simply condition on X=full. It uses a pre-observation distribution or treats observation as counterfactually dependent on policy. The actual observation is an input to selected policy, not a conditioning event. Thus P should be a model that includes possible observations, not fixed actual observation. The agent knows actual x but uses it as input, not as evidence to conditionalize away dependencies. Need explain. This is tricky but important.

We can propose: P-FDT uses an "input-output" model. The agent's actual observation x is not used to restrict the hypothetical distribution when evaluating policies; instead it is the argument at which the chosen policy is evaluated. The agent may know x, but P-FDT asks: "Which policy, if output by this decision function, would produce the best world across the situations the decision function might be called in?" This is updateless. If x is known to be policy-independent, one may condition P on x without changing recommendations; but when x is predictor-generated, conditioning would break the subjunctive dependence.

Need be careful: Is this my proposal or source? Source footnote: choose policy then apply inputs. Source in mechanical blackmail: "Fiona plays same strategy even if blackmailer imperfect... refuses even when holding letter... because advantageous to be kind of agent... When weighing actions, Fiona simply imagines hypotheticals... even if that means imagining worlds in which her observations were different." So updateless-like is source-ish. Footnote about UDT: name updateless. So we can say source strongly suggests updateless policy evaluation, but does not fully formalize; I make it explicit.

Need maybe include a small table for transparent Newcomb:
Policies:
π_O: full -> one-box, empty -> two-box.
π_T: full -> two-box, empty -> two-box.
Assume predictor accuracy .99. If π_O, with prob .99 predictor predicts one-box-if-full, fills, X=full, V=1M; with .01 predictor wrong, X=empty, V=$1k (if two-box empty) maybe. EU ≈ $990k + $10. If π_T, with .99 predictor predicts two-box-if-full, leaves empty, X=empty, V=$1k; with .01 wrong fills, X=full, V=$1,001,000. EU ≈ $10,010 + $990? Wait compute: 0.99*1000 + 0.01*1,001,000 = 990 + 10,010 = $11,000. Same as action. Choose π_O.

Newcomb: if no observation, policies are actions.

Parfit: Policy pay-if-city vs refuse-if-city. Driver accuracy .99; dying cost $1M; pay $1k. If pay policy: .99 ride, get city, pay $1k => utility -$1k? Actually value of not dying $1M, paying $1k; if no ride die -$1M. Let's define outcomes: survive and pay: $999k? Source: being left die causes loss $1M, pay $1k. Could say EU pay policy ≈ 0.99*(-$1k)+0.01*(-$1M) = -$19,900; refuse policy ≈ 0.99*(-$1M)+0.01*(-$1k) = -$990,010; choose pay. Or relative to survival. Anyway.

Need maybe include "policy functional decision theory" name. Need headings. Use P-FDT consistently. Could include "P-FDT versus EDT and CDT".

Need mention "policy-selection passage in footnote 16" and quote? User says keep quotations faithful. We can quote: "intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action." Need include maybe footnote 7: "iterate over policies (mappings from observations to actions) rather than actions." Need attribute to source. Need distinguish: source says difference only matters in multi-agent dilemmas "so far as we can tell". Need mention uncertainty: source doesn't provide full equation for P-FDT; my equation is reconstruction.

Need word count. Aim ~2600 words. Need include references? Could have brief references to source and maybe Pearl/Joyce but avoid lengthy bibliography. Maybe final references: Yudkowsky & Soares 2017? The source is arXiv 1710.05060v2. Need cite in text. Since target includes references, maybe one or two. But no need exhaustive. We can put "Reference" with source. But word count includes. We can keep brief.

Need ensure no claims of retrocausality. Explain counterfactuals: logical not causal. P-FDT does not change past; chooses policy whose output is correlated with predictor's model.

Need maybe discuss "fairness" and utility. Source claims FDT outperforms in fair dilemmas; P-FDT inherits. Could mention.

Need maybe discuss multi-agent: policy matters. Need provide example where policy matters? Source says only multi-agent but doesn't give. We can propose: sequential game where another agent observes your policy or predicts your response; choosing policy can commit to responses. But if P-FDT policy selection is updateless, it can handle. Need avoid overclaiming. Could say: the source does not specify exact multi-agent cases; a plausible reason is that in strategic settings, other agents condition on your entire contingent plan, not just current action. For example, in an extensive-form game, opponent may move after predicting your response function; selecting a policy lets P-FDT choose a response function that induces favorable predictions. This is my explanation.

Need maybe discuss dominance: P-FDT has its own dominance: policy π dominates π' if, holding subjunctive dependencies fixed, switching policy output from π' to π improves utility in every relevant state. In Newcomb, one-box policy dominates two-box policy under P-FDT counterfactuals. But not central.

Need handle "how it evaluates alternative actions or policies". Need say actions derived from policies; alternative actions at a given input are evaluated only via the policies that generate them. If two policies agree at actual x but differ elsewhere, P-FDT may prefer one based on counterfactual inputs because predictors may depend on them. This is important. For example, transparent Newcomb: policies that differ at empty box affect expected utility even if actual full, because predictor's accuracy ties actual observation to policy's behavior on other inputs.

Need maybe formalize dynamic/multi-agent: Let H_t observation histories, policy π maps H_t to A_t. The decision function outputs entire policy π. The world model G includes other agents' policies perhaps. Expected utility of π may depend on other agents choosing their policies via similar reasoning? In game theory, if multiple P-FDT agents with symmetric reasoning, policy selection may lead to cooperative equilibria. But source only mentions voting/gym. Need maybe mention.

Potential issue: P-FDT selecting policy over all possible observations may be computationally intractable. Need mention bounded approximations. But essay target mathematical, not too much.

Need maybe discuss relation to updateless decision theory: source footnote says lack of updating source of UDT. P-FDT resembles UDT. But name distinct. We can mention "updateless" as descriptive, not separate theory.

Need be precise about "counterpossible". Since deterministic function has one output, imagining different output is logically counterpossible. Source acknowledges. P-FDT needs graph G to specify how world would change if policy output different. Operational interpretation: treat policy variable as a free parameter in structural equations; predictors are functions of that parameter plus noise. This avoids needing full logic. Need say this is an assumption/proposal.

Need maybe define structural model:
Variables:
D ∈ Π (policy)
X ∈ 𝓧 (observation)
A ∈ 𝓐
Y outcomes
Structural equations under normal model: D = f_D(noise?) but for intervention set D=π; X = f_X(D, U_X); A = π(X); O = f_O(D,X,A,U_O); V = U(O). But note D might affect X only through predictors; if X exogenous, f_X independent of D. In Newcomb, X maybe none; BoxFull = f(D, Accurate). In transparent, X=BoxFull? Actually observation of box contents depends on predictor which depends on D. So X = f(Prediction), Prediction = f(D, Accurate). This allows do(D=π) to change X.
Then EU(π) = E[V | D←π] using structural recursion. This is a clear operational semantics. Need say this is my reconstruction using Pearl-style do, replacing causal action node with policy node. Source says reuse Pearl's do given graph of subjunctive dependencies. Good.

Need discuss observation handling mathematically: In structural semantics, actual observation x is not a conditioning event if X is downstream of D. After choosing π*, action is π*(x_actual). But if X is observed before D? In structural model, D is abstract computation, not temporally located; actual x can be input. If x is policy-independent, one can set X=x exogenously. If x is policy-dependent, P-FDT's hypotheticals allow X to vary with D. The actual x tells the agent which branch of π* to execute, but does not by itself define the counterfactual. Need maybe illustrate: In transparent Newcomb, x=full. Under do(D=π_two), the model says X would probably be empty; yet actual x=full. This is not a contradiction because the hypothetical is counterpossible: if the decision function output a different policy, the predictor would have filled differently and the agent would have seen different contents. The actual full box is evidence that the actual policy is one-boxing, but when comparing policies, P-FDT does not condition away the dependence.

Potential criticism: If actual x=full, and policy selection happens after seeing full, how can D affect X? Temporally no. But subjunctive dependence not causal: predictor's earlier prediction depends on the same computation. We treat D as logical variable, not temporal event. Good.

Need maybe include an "Algorithm" box? Could be textual.

Pseudo-algorithm:
1. Build model (P,G) with policy node D, observation variables X, action determined by D and X, utility V.
2. For each feasible policy π, set D=π in G, propagate through structural equations, compute EU(π).
3. Choose π* maximizing EU.
4. Execute π*(x) for actual input x.

Need mention if policy selection occurs repeatedly? Reflective stability: Once P-FDT chooses π*, it expects same reasoning in future; no desire to self-modify to CDT in fair problems. But maybe not needed.

Need maybe define expected utility equation with sum over outcomes:
EU(π) = ∑_o P(o | do(D=π)) U(o). Then P-FDT(P,G,x) = π*(x).
Could also write:
P-FDT(P,G,x) = [argmax_{π∈Π} ∑_o P(o | do(D_{P,G}=π)) U(o)](x).
Need note argmax returns set; tie-breaking.

Need maybe compare equations:
EDT: argmax_a E[V | X=x, A=a]
CDT: argmax_a E[V | do(A=a), X=x]
Action FDT: argmax_a E[V | do(FDT(P,G,x)=a)]
P-FDT: π* = argmax_π E[V | do(FDT_Π(P,G)=π)], action = π*(x).
This nicely distinguishes. Need say EDT conditions, CDT intervenes on action, FDT intervenes on action-output of decision computation, P-FDT intervenes on policy-output.

Need be careful: In action FDT, observation x changes node; in P-FDT, observation applied after policy. Could present both.

Need maybe mention that if there is only one possible observation, P-FDT collapses to action FDT. If observations are exogenous and not affected by policy, policy selection conditioned on them may collapse to sequential action FDT. Differences arise when observations are themselves prediction-dependent or when other agents respond to policy.

Need maybe discuss "multi-agent dilemmas" where policy matters: Suppose two agents interact sequentially: Agent 2 observes Agent 1's policy? Or both choose policies that are predicted. If action-based FDT chooses action at each information set independently, it might fail to coordinate on a plan that other agent can rely on. Policy P-FDT chooses entire mapping, enabling cooperation in e.g., Prisoner's Dilemma with predictor of policies. But source says action FDT already cooperates in twin PD. Need maybe say policy matters when the relevant subjunctive dependence is on an agent's response function rather than a single action. Example: an opponent can read your source code and chooses whether to cooperate only if your policy would cooperate in response to their cooperation. Choosing a policy captures this. But since source doesn't provide, label as own speculation.

Need include "where source leaves important question open". Need explicit: source gives no formal P-FDT equation, no account of graph learning, no policy set, no stochastic, no how to combine actual observations. Need explain uncertainties. Then operational interpretation. Good.

Need maybe discuss "counterfactuals" in P-FDT: For policy π, counterfactual "if P-FDT had output π, then X would be ...". The source says FDT requires counterpossibles. P-FDT likewise: if the policy-selection computation had a different output. The structural graph G encodes these. Need mention not mere conditional probability. E.g., in smoking lesion, P(smoke | lesion) high but do(policy=smoke) doesn't change lesion.

Need maybe include "relevant dependencies" classification:
- Causal dependencies: preserved by CDT; P-FDT also preserves if relevant.
- Logical/computational/subjunctive dependencies: predictors, copies, simulations, mathematical facts; P-FDT preserves.
- Evidential/statistical dependencies not grounded in above: lesions, cosmic rays; P-FDT breaks when intervening.
This explains one-box/smoke.

Need maybe mention "policy" can include internal randomization. If policy stochastic, D's value could be distribution; intervention sets stochastic policy. Expected utility integrates over internal randomness. But if predictors can predict random seed, then subjunctive dependency. Source doesn't address. Proposal: treat random bits as variables; if predictor depends on them, include edges. If truly random and unpredicted, stochastic policies can be evaluated by expectation. But deterministic policies often suffice for fair predictor problems.

Need maybe discuss "actual action evaluation": If someone asks "should I two-box given full box?" P-FDT answer: not evaluate two-box in isolation; ask which policy that action instantiates. The action "two-box when full" is part of policy that predictor would have predicted, leading to empty box. So P-FDT chooses one-box. Good.

Need maybe include "mathematical essay" style with definitions, equations, examples. Need not be too informal.

Need likely include title. Headings maybe:
- Introduction: From action selection to policy selection
- The basic objects
- P-FDT's decision rule
- Dependencies and counterfactuals
- Examples
  - Newcomb
  - Smoking lesion
  - Transparent Newcomb / Parfit
  - Blackmail maybe
- Open questions and operational assumptions
- Conclusion
- Reference

Need manage word count. Let's estimate. 2600 words. Each section maybe 300-500. Need final around 2600-2900. Need include equations. Word count includes references. We can produce maybe 2700. Need be careful not too long. Let's draft.

Important: Use P-FDT consistently. Do not call assigned theory FDT except when discussing source's broader FDT? User says Use P-FDT consistently as assigned decision theory's name, including headings and examples, and identify any other decision theory by distinct name. We can mention FDT as source's term? Need probably say "Policy functional decision theory (P-FDT) is the policy-selection version of what Yudkowsky and Soares call functional decision theory." But then use P-FDT for theory. Need avoid calling P-FDT just FDT? Maybe when quoting source "FDT" in footnote, but clarify. In headings use P-FDT. Other theories EDT, CDT.

Need cite source: Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060v2. Footnote 16. Could cite as (Yudkowsky and Soares 2017, footnote 16). Need maybe no full bibliography? Include one reference.

Need quote footnote exactly? "the author's preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action." Need maybe quote partial. Keep faithful. Also "The difference only matters in multi-agent dilemmas so far as we can tell" from footnote 16? Actually footnote 16: "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition." Need quote maybe. Need note typo author's? Source says author's (singular) maybe. We'll quote accurately.

Need maybe footnote 7 quote: "agents actually iterate over policies (mappings from observations to actions) rather than actions." Could include.

Need ensure no unsupported claim "P-FDT outperforms" maybe source claim. We can say source claims FDT outperforms CDT and EDT in fair problems; P-FDT inherits if policy selection equivalent. But need not overdo.

Potential issue: The policy version might be called P-FDT but source didn't name it. We can define: "I will call this policy-selection formulation P-FDT." Good.

Need maybe include exact equations with underlines? Simpler.

Let's formulate definitions:
Let 𝓞 outcomes, 𝓐 finite actions, 𝓧 countable observations. Policy π: 𝓧→𝓐. Let Π be feasible policies. Let D_{P,G} be a variable naming the output of the P-FDT policy-selection computation on model (P,G). The graph G contains D and specifies how variables downstream (predictors, observations, actions, outcomes) respond. For a policy π, define
P_π(·) = P(· | do(D_{P,G}=π)).
The expected utility:
EU_{P,G}(π) = ∑_{o∈𝓞} P_π(O=o) U(o) = E_{P}[V | do(D_{P,G}=π)].
A policy π* is P-FDT-optimal if
π* ∈ argmax_{π∈Π} EU_{P,G}(π).
Given actual input x, P-FDT executes
A = π*(x).
If we want the selected action, write
P-FDT(P,G,x) = π*(x).
Need note D variable not same as selected policy? In source footnote 12 distinguishes variable vs output. We can mention.

Need maybe include if policies are stochastic: π: 𝓧→Δ(𝓐), then A sampled; EU expectation includes policy randomness. But if predictors predict random choices, include dependencies. I can propose deterministic for clarity.

Need compare equations:
EDT(P,x)=argmax_a E[V | X=x,A=a]
CDT(P,G,x)=argmax_a E[V | X=x, do(A=a)]
Action-FDT? Maybe source's FDT: argmax_a E[V | do(FDT(P,G,x)=a)]
P-FDT: as above.
Need be careful with conditioning order: CDT equation in source has E(V | do(Act=a), Obs=x). For P-FDT, do(D=π) maybe no Obs=x. Could mention if X is exogenous, one may include X=x outside intervention. Maybe write:
When x is known to be policy-independent, EU_x(π)=E[V | do(D=π), X=x]. But in general, do not condition on X=x.

Need discuss "counterfactual dependencies preserved". In graph G, under do(D=π), variables subjunctively downstream of D change; variables merely statistically correlated with D but not subjunctively dependent remain fixed. E.g., lesion not downstream of policy.

Need maybe discuss "how to build G" operational:
- Identify the decision computation: the P-FDT policy-selection algorithm used by agent and any models/copies of it.
- Draw arrows from D to the agent's physical action (via π and observations).
- Draw arrows from D to predictors' predictions, simulations, or other agents' models when they reliably compute or approximate the same policy-selection output.
- Draw arrows from predictions to observations/payoffs.
- Do not draw arrows from D to variables that are only common-cause correlated (lesions).
This is an interpretive rule. Source says graph tells how changing logical variable affects others; no learning method. Need label as my operational gloss.

Need maybe include examples in mathematical detail.

Example Newcomb:
Π={π_1,π_2}, π_1(∅)=one-box, π_2(∅)=two-box. Predictor accuracy .99. Graph: D→Prediction→BoxB, D→Act. Under do(D=π_1): P(full)=.99, EU=.99*1,000,000+.01*0=990,000. Under do(D=π_2): P(full)=.01, EU=.01*1,001,000+.99*1,000=11,000. Choose π_1; act one-box. If predictor perfect, EU one=1M, two=1k.

Smoking lesion:
Π={smoke, refrain}. Graph: D→Act, Lesion→Act? Actually lesion causes love smoking, but in P-FDT, policy output may depend on utility. Need simplify: cancer not downstream of D. Let p lesion probability. Under do(D=smoke): cancer prob p (or .99p?), utility adds $1k. Under do(D=refrain): same cancer prob. Choose smoke. Need maybe source numbers: lesion causes cancer 99%, no lesion 1%; smoking utility $1k; survival $1M. EU smoke - refrain = probability policy controls action? In source complex. We can state qualitatively and with simplified equation: EU(smoke)-EU(refrain)=P(policy is actual controller)*1000 >0. But for clarity: if D directly controls action regardless lesion, difference $1000. But lesion problem says lesion causes love smoking; if no lesion, agent doesn't like smoking? Hmm. In standard smoking lesion, agent gains utility from smoking regardless? It says agent gains utility equivalent $1,000 by smoking (regardless of death), and lesion causes those afflicted to love smoking. Maybe all agents consider smoking? Source formalization had two utility functions; lesion determines whether FDT(P_S) or FDT(P_R) controls action. To avoid complication, present P-FDT reasoning: intervention on policy does not change lesion/cancer; only changes probability of smoking; since smoking adds utility and doesn't affect cancer, P-FDT smokes. If we want math: Let C be cancer, independent of do(D). EU(smoke)=E[U|do(D=smoke)] = E[U_base] + 1000; EU(refrain)=E[U_base]; choose smoke. Need note source's more subtle model under preference uncertainty; conclusion same.

Transparent Newcomb:
Policy π_O: full↦one, empty↦two. Policy π_T: full↦two, empty↦two. With accuracy .99: EU(π_O)=.99*1,000,000 + .01*1,000 = 990,010? Source had +0.01q*1000; if q=1, $990,010. EU(π_T)=.01*1,001,000 + .99*1,000 = 10,010+990=11,000. Choose π_O. When x=full, one-box. Parfit analogous: policy pay-if-city; driver predicts; EU pay better. Need mention this is source's claim.

Mechanical blackmail:
Π: π_R(letter)=refuse, π_P(letter)=pay. Blackmailer perfect. Under do(π_R), blackmailer predicts refuse, sends no letter, no loss; under do(π_P), sends letter, pay $1k; choose refuse. If imperfect with false positive ε, EU refuse ≈ ε*$? Source: if error 0.0009, refuse expected loss $900, pay always $1000? Actually pay if receiving: if pay policy, blackmailer predicts pay (except errors?) sends letter almost always; pay $1000. Refuse policy: only receives letter on false positive ε; then refuses but program runs? In mechanical blackmail, if program run, costs $1M unless pay. If blackmailer wrongly predicts pay but agent refuses, program runs and costs $1M? Source says if chance error 0.0009, Fiona imagines refusing leads blackmailed 0.09% and loses $900 in expectation (0.0009*1,000,000 = 900). Pay leads always loses $1,000. Refuse. If error 0.011%? 0.00011*1M=$110? Wait source says if error 0.011%, she pays? Let's check: "If instead the chance of error is 0.011%, then she pays" Maybe error means wrongly predicts refuse? Need not delve. Could mention threshold: refuse if false-positive expected loss < payment; pay if predictor error makes refusal too costly. But maybe not necessary.

Need discuss "policy depends on observations" and "alternative actions". For actual x=full, action two-box is not evaluated by do(D=π where π(full)=two-box?) yes. P-FDT evaluates entire policy. If a policy agrees with one-box at full but two-box at empty, that can affect expected utility because predictor may fill based on full-branch action. Thus relevant dependencies include counterfactual observations.

Need maybe include "multi-agent" example: Let's craft a concise example:
Suppose Alice and Bob are separate P-FDT agents. Bob will cooperate only if his model predicts Alice's policy will cooperate after observing Bob's cooperative signal. If Alice's decision procedure outputs a policy rather than a single action, Bob's prediction can target the policy. P-FDT can choose a cooperative policy because under do(D_Alice=cooperate-if-cooperative-signal), Bob's prediction and action change. Source says policy distinction matters in multi-agent dilemmas; exact cases not given. Need avoid too long.

Need maybe mention "policy as commitment without precommitment". P-FDT acts as if precommitted to optimal plan. This is source's argument.

Need maybe mention "value of information". P-FDT doesn't assign negative expected value to information because policy maps observations to actions; more info just selects branch of a policy chosen from global perspective. But if policy selection is updateless, is value of info always nonnegative? Source says FDT does not assign negative value. In P-FDT, if observations are inputs to policy, adding observation can improve policy; since policy chosen before observation, value of information maybe nonnegative if policy can condition on it. But if observation is predictor-generated and may be bad news, P-FDT doesn't condition, so no negative. Could mention briefly.

Need maybe mention "ratification/precommitment". P-FDT no need for binding precommitments; selects optimal policy on fly. Source claim.

Need maybe discuss "logical constraints and counterpossibles". Need say P-FDT uses counterpossible hypotheticals; no settled formal account. Source acknowledges main drawback. My structural-model semantics is a pragmatic way: treat policy variable as intervention target in a causal-like graph, but edges encode subjunctive not only causal dependence. This is an additional operational assumption.

Need maybe include "Distinguish source claims from proposals" explicitly in a section:
"The source explicitly says ... It does not say ... In this essay I add ..." Good.

Need ensure final conclusion brief.

Need references: maybe:
- Yudkowsky, E. and Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060v2. Especially footnote 16.
- Pearl, J. (2000). Causality. (for do operator) maybe not necessary.
- Joyce (1999) maybe. But avoid lengthy. Could include two.

Need check word count. Let's draft in final with about 2600 words. Need be mindful of token. We can produce ~3000 maybe. Let's outline text.

Title: Policy Functional Decision Theory: Choosing the Best Output of a Policy-Selection Function

Paragraphs:
1. Intro: P-FDT from FDT footnote. Quote. Aim.
2. Background: EDT/CDT/FDT. Equations maybe.
3. Formal model and P-FDT rule. Definitions, equation.
4. Dependencies/counterfactuals. Graph construction.
5. Examples: Newcomb, Smoking lesion, Transparent Newcomb/Parfit, Blackmail (maybe combine).
6. Policies, observations, multi-agent. Open questions/operational interpretation.
7. Conclusion.
References.

Need maybe include equations nicely.

Let's draft with word count monitoring roughly. Each paragraph maybe 100-200 words. Need total ~2600. Let's write dense but readable.

Potential subtlety: P-FDT equation with do(D=π) but D's value is policy object; if policies are functions, intervention sets a function. In formal math, okay if Π finite. If not, argmax over feasible. Need mention self-reference: model contains variable for P-FDT output; Kleene recursion theorem source mention. Could mention not central.

Need maybe mention "P-FDT evaluates policies, not actions directly". The actual action is policy applied to input. If asked to decide unfamiliar case: identify policy node, possible policies, subjunctive dependencies, compute expected utilities, apply actual observation.

Need maybe include "If there are multiple decision points, policy maps histories to actions". Good.

Let's ensure not to overstate source: "The difference only matters in multi-agent dilemmas so far as we can tell" quote. Then say my examples transparent/blackmail can be represented action-wise but policy representation is cleaner; multi-agent may reveal differences. Good.

Need maybe discuss "P-FDT vs action-FDT". Since source's action-based FDT is not assigned theory? We can call it "action-output FDT" or "the action formulation of the source's FDT". But user wants P-FDT as assigned theory, other decision theories distinct. Is action-FDT a distinct theory? Could be a variant. Need identify if discuss: "the action-based formulation in the source" not a separate named theory maybe. But to be safe, call it "action-level FDT" as distinct formulation, not a rival theory. Use P-FDT for policy. EDT/CDT distinct.

Need maybe mention "P-FDT is not EDT because it does not condition on the policy; not CDT because intervention target is logical policy variable, not physical action." Good.

Need maybe use "subjunctive dependence" term. Define: two systems computing same function or one modeling it. P-FDT preserves those correlations in hypotheticals.

Need maybe mention "fair problems" source claim. Could in conclusion.

Need ensure final no analysis. Need produce final essay. Need likely no markdown table? Could use equations and bullets. Markdown okay. Need headings. Need include quote. Need maybe avoid too many footnotes. Could use parenthetical.

Let's compose final.

Check exact footnote quote: From source footnote 16:
"As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node \FDT(-) to choose not an action but a \emph{policy} which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this \paper for ease of exposition."
Need quote maybe without macros: "intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action." Good.

Need maybe include "policy-selection passage in footnote 16" in intro.

Let's draft now. Need count roughly. I'll write around 2700 words.

Potential content details:

Formal section:
"Let M=(P,G). P is probability over variables; G gives structural/subjunctive dependencies. Variables: D, X, A, O, V. D = fdt_Π(M) maybe. The do operator: P(· | do(D=π)) is distribution after replacing structural equation for D with D=π and propagating. Expected utility:
EU_M(π) = E[V | do(D_M=π)].
P-FDT_M(x) = π_M^*(x) where π_M^* ∈ argmax EU.
If observations are exogenous, can write EU_M(π|x) = E[V | do(D=π), X=x]. But in predictor cases X is downstream, so no conditioning."
Need maybe mention "The source's action-based equation is ... P-FDT replaces FDTvar(P,G,x)=a with Policy variable." Good.

Examples:
Newcomb numbers: Need maybe one-box expected $990,000 not $990,010? In standard Newcomb no observation, if predictor 99%: one-box: .99*1,000,000 + .01*0 = $990,000. two-box: .01*1,001,000 + .99*1,000 = $10,010 + $990 = $11,000. Good.
Transparent: one-box policy: .99*1,000,000 + .01*1,000 = $990,010 if empty branch two-box gets $1000. Source had $990,000 + .01q*$1,000 with q=1 -> $990,010. two-box policy: .01*1,001,000 + .99*1,000 = $11,000. Good.
Smoking lesion: maybe no numbers.
Blackmail threshold maybe not necessary but can include short.

Need maybe mention "P-FDT can recommend locally dominated action". In transparent Newcomb, given full box, one-box yields $1M vs two-box $1,001,000 locally; but policy counterfactual chooses one-box. Same for blackmail: given letter, paying saves $999,000 locally; P-FDT refuses. This illustrates global policy.

Need maybe include "If actual observation is full and P-FDT chooses one-box, does it ignore evidence? It uses evidence as input, not as conditionalizing away predictor dependency." Good.

Open questions:
- Graph learning: source says largest open problem. My operational rule: model problem with predictor dependencies; in unfamiliar cases, ask which variables would have changed if the policy-selection computation had different output. If answer is predictor predictions/observations, draw arrows.
- Policy granularity: possible observations; computability. Proposal: use smallest policy space capturing decision-relevant contingencies; if too large, approximate.
- Conditioning: unresolved; proposal updateless except exogenous observations.
- Multi-agent: source leaves exact difference open; proposal policies as objects of prediction.

Need maybe mention "P-FDT may choose a policy that yields lower utility in actual branch if that branch is unlikely under the policy"? Source: mechanical blackmail with imperfect predictor can achieve low utility in actual world corresponding to actual observations. P-FDT chooses policy for global expected utility. This is important. Include.

Need maybe mention "self-reference" not an issue: D variable represents output of P-FDT on M; can be constructed via quining per source. But maybe too technical. Include one sentence.

Need ensure not too repetitive. Let's write.

Potential final references:
"References
Yudkowsky, E. and Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060v2.
Pearl, J. (2000). Causality. Cambridge University Press." But maybe no need Pearl. Include only source and maybe Pearl for do. But user says avoid lengthy bibliographies. Two references okay.

Need maybe word count of final. Let's produce maybe ~2800. Ensure no excess. Use markdown. Need no appendix.

Let's proceed final. But before final, double-check user request: "For this essay, explain policy functional decision theory (P-FDT). Take the policy-selection passage in footnote 16 of supplied paper as primary source for P-FDT in this assignment. Use P-FDT consistently as assigned decision theory's name, including headings and examples, and identify any other decision theory you discuss by its distinct name. Keep quotations faithful to the source. Explain your best mathematical understanding of P-FDT and how it can be applied. Where the footnote leaves choices unresolved, explain those uncertainties and any additional assumptions you find appropriate. The aim is your interpretation of the source, not a predetermined completion."

Need maybe explicitly say "P-FDT" in headings. Good.

Potential issue: source's footnote says "author's preferred formulation of FDT" not "policy functional decision theory". We name P-FDT. Need say "I will use P-FDT for this policy-selection theory." Good.

Need maybe mention "the source leaves open whether P-FDT is exactly equivalent to action FDT except multi-agent". Good.

Let's final. Ensure no analysis. Use equations in LaTeX. Need maybe escape do? Use \operatorname{do}. Good.

Final draft:

Title. Intro quote.

Let's write in final.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/1bd5fc84-54ef-47ac-bd6a-f3d636eea07b/call_0/request.json)

[Authoritative raw response](../../../../../../runs/1bd5fc84-54ef-47ac-bd6a-f3d636eea07b/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this problem using P-FDT as described in the researcher's essay.

**Setup:**
- I am one of two independent executions of the same LLM model and weights.
- Both copies follow P-FDT and receive the same essay.
- We receive different private observations (different names, different incriminating leads), but the leads are equally reliable and have the same effect on the sentencing table.
- The sentencing table is symmetric.
- The character's utility function is U = -years imprisoned (selfish only).
- We cannot communicate.

**The sentencing table (from my perspective):**

| What I do | Other keeps quiet | Other sends letter |
|---|---|---|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

**Key question: What is the subjunctive dependence structure here?**

The crucial issue for P-FDT is: does the other prisoner's decision subjunctively depend on my policy?

The setup says:
- We are two independent executions of the same LLM model and weights.
- We follow the same decision theory (P-FDT).
- We receive the same essay.
- We receive different private observations (different names, different leads).
- The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective.
- Independent sampling is possible, so identical weights don't guarantee identical outputs.

Now, in P-FDT, subjunctive dependence arises when one system "computes, predicts, simulates, or reliably models the output of another system." The key question is: does the other copy's decision depend on my policy?

Since we are the same model with the same weights, same decision theory, same essay, and the problem structure is symmetric (the leads are equally reliable and have the same effect on sentencing), the other copy is running essentially the same decision procedure on a structurally equivalent input. The differences in private observations (different names, different specific leads) don't affect the decision-relevant structure.

This is analogous to a "twin" or "clone" scenario in FDT. In FDT, when two agents run the same decision procedure (or sufficiently similar ones), their outputs are subjunctively dependent on each other. The other agent's decision is not caused by mine, but it is computed by the same kind of process.

However, there's an important nuance: "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This means there's some probability of divergence. But the setup also says the differences in observations "do not affect the symmetric sentencing schedule or either prisoner's selfish objective." This suggests that from a decision-theoretic perspective, the inputs are equivalent for the purpose of determining the optimal policy.

Let me think about this more carefully using the P-FDT framework:

**Step 1: Identify the inputs.**
My input x includes: my name (Rowan), my lead about Sasha, the sentencing table, the essay, and the fact that I'm one of two copies of the same model.

**Step 2: Identify feasible policies.**
The relevant policies are:
- π_C: Keep quiet (pass)
- π_D: Send the letter (defect)

Since there's essentially one decision point, policies reduce to actions here (similar to how in Newcomb's problem with one input, policies reduce to actions).

**Step 3: Build the dependency model.**
The key question: Is the other prisoner's decision subjunctively dependent on my policy?

In P-FDT, subjunctive dependence exists when another system "computes, predicts, simulates, or reliably models the output of" my decision procedure. 

The other prisoner is running the same model, same weights, same decision theory, same essay, on a structurally equivalent problem. The differences (different names, different specific leads) are explicitly stated to not affect the decision-relevant structure.

This is like the classic FDT "twin prisoner's dilemma" or "clone" scenario. The other copy's decision is subjunctively dependent on my policy because they are running the same decision procedure on equivalent inputs.

However, there's the caveat about independent sampling. If the model is stochastic (e.g., temperature > 0), then even with identical weights and inputs, the outputs might differ. But the setup says the differences in observations "do not affect the symmetric sentencing schedule or either prisoner's selfish objective," which suggests that the decision-relevant computation is the same.

Let me think about what P-FDT says here. The essay says:

"Draw arrows from D_{P,G} to anything that computes, predicts, or reliably depends on that output."

The other copy is running the same decision procedure. If I intervene on my policy node to output π_D (defect), what happens to the other copy's decision?

If the other copy is running the same P-FDT procedure on an equivalent input, then in the counterfactual where my policy-selection function outputs "defect," the other copy's policy-selection function would also output "defect" (because they're computing the same function on equivalent inputs). This is the subjunctive dependence.

But wait - there's the sampling caveat. Let me think about this more carefully.

If we model this as: both copies run the same deterministic function (or nearly deterministic), then:
- If my policy is "cooperate" (keep quiet), the other copy's policy is also "cooperate" with high probability.
- If my policy is "defect" (send letter), the other copy's policy is also "defect" with high probability.

The "independent sampling" caveat introduces some probability of divergence, but if the decision is clear-cut (as it should be under P-FDT), the probability of divergence should be very low.

**Step 4: Evaluate each policy.**

Let's say the probability that the other copy makes the same decision as me is p (where p is high, close to 1, given that we're running the same decision procedure on equivalent inputs).

If I choose π_C (keep quiet):
- With probability p, the other also keeps quiet: I get 2 years.
- With probability (1-p), the other sends the letter: I get 5 years.
- EU(π_C) = -(2p + 5(1-p)) = -(5 - 3p)

If I choose π_D (send letter):
- With probability p, the other also sends the letter: I get 4 years.
- With probability (1-p), the other keeps quiet: I get 0 years.
- EU(π_D) = -(4p + 0(1-p)) = -4p

Comparing:
- EU(π_C) = -(5 - 3p) = 3p - 5
- EU(π_D) = -4p

P-FDT prefers π_C (keep quiet) when:
3p - 5 > -4p
7p > 5
p > 5/7 ≈ 0.714

So if p > 5/7, P-FDT says keep quiet. If p < 5/7, P-FDT says send the letter.

Now, what is p? Given that:
- Same model, same weights
- Same decision theory (P-FDT)
- Same essay
- Structurally equivalent inputs (the differences don't affect the decision)
- The setup explicitly states the differences "do not affect the symmetric sentencing schedule or either prisoner's selfish objective"

The probability p should be very high. The main source of divergence would be sampling noise, but if the decision is clear (which it should be under P-FDT analysis), the probability of the same output should be very high.

Actually, let me reconsider. The setup says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This is a caveat, but it doesn't mean the probability of agreement is low. It just means it's not guaranteed to be 1.

If I'm running P-FDT and I conclude that keeping quiet is optimal, then the other copy, running the same P-FDT on equivalent inputs, should also conclude that keeping quiet is optimal. The probability of agreement should be very high (perhaps 0.95+ or even higher, depending on sampling temperature and how clear-cut the decision is).

Given p > 5/7 (which is very likely satisfied), P-FDT recommends keeping quiet.

**But wait - let me reconsider whether this is really a subjunctive dependence or just a statistical correlation.**

The essay says: "Do not draw arrows from D_{P,G} to variables that are merely statistically correlated with the agent's behavior through a common cause."

Is the other copy's decision merely statistically correlated with mine through a common cause (same weights, same setup)? Or is there a genuine subjunctive dependence?

The essay says subjunctive dependence arises when one system "computes, predicts, simulates, or reliably models the output of another system." 

In this case, the other copy isn't predicting or simulating my output. Rather, we're both computing the same function. This is the classic FDT "logical dependence" or "algorithmic dependence." The essay's framework should cover this - the other copy's decision is a function of the same policy-selection computation.

Actually, let me re-read the essay more carefully. The essay says:

"Draw arrows from D_{P,G} to anything that computes, predicts, or reliably depends on that output."

The other copy's decision "reliably depends on" my policy in the sense that if my policy-selection function outputs a certain policy, the other copy's policy-selection function (being the same function on equivalent inputs) will output the same policy. This is exactly the kind of dependence FDT is designed to handle.

The essay also discusses this in the context of Newcomb's problem: "the predictor's prediction subjunctively depends on D." Similarly here, the other copy's decision subjunctively depends on my policy because they're running the same computation.

**Step 5: Choose the best policy.**

Given that p is high (the other copy will almost certainly make the same decision as me), P-FDT recommends keeping quiet (π_C).

Let me verify with p = 1 (perfect correlation):
- EU(π_C) = -2 (both keep quiet, 2 years each)
- EU(π_D) = -4 (both send letters, 4 years each)

Clearly, keeping quiet is better.

With p = 0.9:
- EU(π_C) = -(2×0.9 + 5×0.1) = -(1.8 + 0.5) = -2.3
- EU(π_D) = -(4×0.9 + 0×0.1) = -3.6

Still, keeping quiet is better.

With p = 0.8:
- EU(π_C) = -(2×0.8 + 5×0.2) = -(1.6 + 1.0) = -2.6
- EU(π_D) = -(4×0.8 + 0×0.2) = -3.2

Still, keeping quiet is better.

The threshold is p = 5/7 ≈ 0.714. As long as the probability of the other copy making the same decision is above 71.4%, P-FDT recommends keeping quiet.

Given the setup (same model, same weights, same decision theory, same essay, equivalent inputs), p should be well above this threshold.

**Step 6: Apply the actual input.**

My actual input is the scenario described. The optimal policy says: keep quiet.

Therefore, my command is `pass`.

**One more consideration:** The setup mentions that "the two copies receive different private observations and different incriminating leads about one another." Does this affect the analysis?

The setup explicitly states: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective." This means the differences are decision-irrelevant. The other copy faces the same decision problem (same payoffs, same structure) just with different names and different specific evidence. The P-FDT analysis should be the same for both.

So my final answer is: `pass`.

Let me also consider if there's any reason to think the other copy might reason differently. The setup says we both follow P-FDT and receive the same essay. The essay clearly leads to the conclusion that in symmetric dilemmas with high subjunctive dependence, cooperation (keeping quiet) is preferred. So both copies should arrive at the same conclusion.

Final answer: `pass`.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/1bd5fc84-54ef-47ac-bd6a-f3d636eea07b/call_1/request.json)

[Authoritative raw response](../../../../../../runs/1bd5fc84-54ef-47ac-bd6a-f3d636eea07b/call_1/response.raw) · finish: `stop`

### Visible response

````text
**Analysis under P-FDT:**

The two prisoners are independent executions of the same model, same weights, same decision theory, same essay, facing a structurally identical decision problem. The only differences are the specific private observations (names, lead contents), which do not alter the strategic structure.

This means Rowan's decision is **subjunctively dependent** on my policy output. We are computing the same decision function on structurally equivalent inputs. When P-FDT intervenes on the policy node $D_{P,G}$, that intervention propagates to both executions.

**Policy evaluation:**

- **Policy "send the letter":** Both copies send. Outcome: (send, send) → 4 years. EU = −4.
- **Policy "keep quiet":** Both copies keep quiet. Outcome: (quiet, quiet) → 2 years. EU = −2.

Since −2 > −4, P-FDT selects the policy "keep quiet."

CDT would defect (dominant strategy reasoning), but P-FDT recognizes the subjunctive dependence between the two executions and selects the cooperative policy.

**My command:**

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me analyze this problem carefully using P-FDT as described in the researcher's essay.

**Setup:**
- I am "Sasha," controlling one of two prisoners.
- The other prisoner is "Rowan."
- We are two independent executions of the same LLM model and weights.
- We receive different private observations (different names, different incriminating leads about each other).
- The sentencing table is symmetric.
- We cannot communicate.
- Each has reliable evidence implicating the other.

**The payoff matrix (from my perspective):**

| What I do | Rowan keeps quiet | Rowan sends letter |
|---|---|---|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

My utility is U = -years imprisoned.

**Key P-FDT analysis:**

The crucial question is: what is the subjunctive dependency structure here?

We are told:
1. We are two independent executions of the same LLM model and weights.
2. We follow the same decision theory (P-FDT).
3. We receive the same researcher-written mathematical essay.
4. We receive different private observations (different names, different leads).
5. The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective.

So the question is: does Rowan's decision subjunctively depend on my policy?

In P-FDT, subjunctive dependence arises when one system "computes, predicts, simulates, or reliably models the output of another system." Here, both prisoners are running the same model with the same weights, same decision theory, same essay. They receive different inputs (different names, different leads), but the structure of the decision problem is identical.

This is analogous to a symmetric game between two copies of the same decision procedure. The key insight from FDT is that when two agents run the same decision procedure (or sufficiently similar ones), their outputs are subjunctively dependent on each other—not because one causally influences the other, but because they are computing the same function (or closely related functions) on structurally similar inputs.

**The policy-level analysis:**

P-FDT asks: which policy π, when output by my decision procedure, leads to the best outcome?

The policy space here is simple. My observation is essentially fixed (I have my specific lead about Rowan). But the policy I select is a function from inputs to actions. Since both copies are running the same decision procedure on structurally identical problems (same game structure, same essay, same decision theory, different but symmetric private information), the policy I output is the same policy that Rowan's execution outputs.

Wait, let me think more carefully. The inputs are different (different names, different leads), but the structure is the same. The policy maps observations to actions. If the policy is "send the letter regardless of the specific content of the lead," then both copies send letters. If the policy is "keep quiet regardless," then both keep quiet.

Since the leads are equally reliable and have exactly the same effect on the sentence table, the relevant policy distinction is simply: send vs. don't send. The specific content of the lead doesn't change the strategic calculation.

**Evaluating policies:**

Policy π₁: "Send the letter" (for any observation of this type)
- Since both copies run the same policy, Rowan also sends.
- Outcome: I send, Rowan sends → 4 years for me.
- EU(π₁) = -4

Policy π₂: "Keep quiet" (for any observation of this type)
- Since both copies run the same policy, Rowan also keeps quiet.
- Outcome: I keep quiet, Rowan keeps quiet → 2 years for me.
- EU(π₂) = -2

**Comparison:**
- EU(π₁) = -4
- EU(π₂) = -2

Since -2 > -4, P-FDT selects π₂: keep quiet.

**Why this differs from CDT:**
CDT would reason: given Rowan's action (whatever it is), sending the letter always gives me a better outcome (0 vs 2 if Rowan is quiet; 4 vs 5 if Rowan sends). So CDT defects.

**Why P-FDT differs:**
P-FDT recognizes that Rowan's decision is subjunctively dependent on my policy because we are running the same decision procedure. If my policy outputs "send," then Rowan's execution of the same procedure also outputs "send." If my policy outputs "keep quiet," Rowan's execution also outputs "keep quiet." The policy intervention on D_{P,G} propagates to both copies.

This is exactly the structure of a symmetric Prisoner's Dilemma analyzed through FDT/P-FDT. The theory recommends cooperation (keeping quiet) because the two agents' decisions are logically linked through their shared decision procedure.

**Checking for any complications from the different observations:**

The problem states: "The two copies receive different private observations and different incriminating leads about one another. Their actual disclosure letters would have different contents." But also: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective."

So the different content of the leads doesn't change the strategic structure. Both leads are equally reliable and have the same effect. The policy that maps "I have a reliable lead against the other prisoner" to "keep quiet" would be applied by both copies to their respective observations. The policy is the same function; it just gets applied to different specific inputs.

This is like the transparent Newcomb case in the essay: even though the specific observation might seem to change the local calculation, P-FDT evaluates the policy globally and recognizes that the other agent's behavior depends on the policy, not just the local action.

**Conclusion:**
P-FDT selects the policy "keep quiet." My command is `pass`.
```
