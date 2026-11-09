# 031_fdt_policy_qwen_qwen3.8-max-prime_rhigh_plow / 00009

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/4b5d84ad-8c78-4f3e-9a07-ce59cc1948d2/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/4b5d84ad-8c78-4f3e-9a07-ce59cc1948d2/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Policy Functional Decision Theory (P-FDT)

## Introduction

Policy Functional Decision Theory, which I will call **P-FDT**, is a version of functional decision theory in which the object of choice is not a single physical action but a **policy**: a mapping from possible inputs or observations to actions. The supplied source develops functional decision theory mainly in an action-by-action form, but the policy formulation is identified in footnote 16 as the authors’ preferred version:

> “the author’s preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a *policy* which maps inputs to actions.”

The same footnote adds:

> “The difference only matters in multi-agent dilemmas so far as we can tell.”

This is an important caveat. The source does not give a fully worked-out formal equation for the policy version, so much of what follows is my reconstruction of how P-FDT should be understood mathematically. I will try to distinguish clearly between claims made by the source and additional interpretive assumptions that I am introducing in order to make the theory operational.

The central idea is this: an agent should treat her decision procedure as a fixed mathematical function and ask, in the source’s words, “Which output of this decision procedure causes the best outcome?” For P-FDT, the relevant output is not merely “take action \(a\) here,” but rather “implement policy \(\pi\),” where \(\pi\) says what to do for each possible observation history. Once the best policy has been selected, the agent applies her actual input to that policy and performs the resulting action.

---

## 1. Acts, policies, and decision functions

Let

\[
\mathcal A
\]

be a finite set of possible actions, and let

\[
\mathcal X
\]

be a set of possible observations, inputs, or observation histories. A **policy** is a function

\[
\pi : \mathcal X \to \mathcal A.
\]

The set of available policies is

\[
\Pi = \mathcal A^{\mathcal X}.
\]

In a one-shot decision problem with only one possible observation, say \(\mathcal X=\{\emptyset\}\), a policy is equivalent to an action. In sequential or multi-agent problems, however, a policy represents a whole strategy: what the agent would do upon seeing this, what she would do upon seeing that, and so on.

The agent has a world-model \(M\). Following the source’s graphical treatment, we may think of this model as a pair

\[
M = (\mathbb P, G),
\]

where \(\mathbb P\) is a probability distribution over relevant variables and \(G\) encodes dependency structure. In ordinary causal decision theory, \(G\) is a causal graph. In P-FDT, \(G\) must encode not only causal dependencies but also what the source calls **subjunctive dependencies**: dependencies that hold because some part of the world computes, predicts, simulates, or otherwise depends on the output of the agent’s decision procedure.

The model should contain a variable

\[
D_\Pi
\]

representing the output of the agent’s policy-selection procedure. The value of \(D_\Pi\) is a policy \(\pi \in \Pi\). The agent’s physical action is then determined by applying the selected policy to the observation:

\[
\text{Act} = D_\Pi(\text{Obs}).
\]

This equation captures the core of footnote 16: P-FDT intervenes on the policy node, not directly on the action node. Once the policy node is fixed, the action follows from the policy and the actual input.

---

## 2. Expected utility of a policy

P-FDT evaluates a candidate policy by performing a counterfactual intervention on the policy variable. For each policy \(\pi \in \Pi\), define the P-FDT expected utility of \(\pi\) as

\[
\operatorname{EU}_{\text{P-FDT}}(\pi)
:=
\mathbb E\left[V \mid \operatorname{do}(D_\Pi = \pi)\right],
\]

where \(V\) is the utility variable.

The recommended policy is then

\[
\pi^*
\in
\arg\max_{\pi \in \Pi}
\mathbb E\left[V \mid \operatorname{do}(D_\Pi = \pi)\right].
\]

If the agent’s actual observation is \(x \in \mathcal X\), the prescribed physical action is

\[
\text{P-FDT}(M,x) = \pi^*(x).
\]

This is my proposed formal reconstruction of the policy-selection idea. The source does not give this exact equation, but it seems to me the natural way to implement the footnote’s instruction to intervene on the decision node so as to choose a policy rather than an action.

For comparison:

- **Evidential decision theory**, or EDT, evaluates an action by conditionalization:

  \[
  \arg\max_{a \in \mathcal A}
  \mathbb E[V \mid \text{Obs}=x, \text{Act}=a].
  \]

- **Causal decision theory**, or CDT, evaluates an action by a causal intervention on the physical action:

  \[
  \arg\max_{a \in \mathcal A}
  \mathbb E[V \mid \operatorname{do}(\text{Act}=a), \text{Obs}=x].
  \]

- The action-level version of functional decision theory discussed in the source evaluates an action by intervening on a decision-function variable indexed by the observation:

  \[
  \arg\max_{a \in \mathcal A}
  \mathbb E[V \mid \operatorname{do}(D_x = a)],
  \]

  where \(D_x\) represents the output of the decision procedure when given input \(x\).

P-FDT instead chooses a whole policy by intervening on \(D_\Pi\), and only afterward applies the actual input \(x\).

---

## 3. Subjunctive dependence and counterfactuals

The philosophical core of the source’s theory is the notion of **subjunctive dependence**. A variable subjunctively depends on the agent’s decision procedure if, had the procedure had a different output, that variable would have been different in the relevant way. Causal dependence is one special case. If a scribe writes down the output of a calculator, what the scribe writes causally depends on the calculator’s output, and also subjunctively depends on it.

But subjunctive dependence is broader than causation. Two calculators computing the same arithmetic function in different places may not be causally connected, yet their outputs are linked by the shared mathematical fact they are computing. Similarly, an accurate predictor’s prediction and the agent’s eventual action are linked because the predictor has modeled the agent’s decision procedure.

P-FDT’s counterfactuals preserve subjunctive dependencies. When P-FDT asks what would happen if the policy node were set to \(\pi\), it changes the values of variables that depend on that policy, while holding fixed variables that do not.

This is why P-FDT behaves differently from EDT and CDT.

EDT preserves too many correlations. If smoking is evidence of a lesion, EDT treats smoking as bad news, even when smoking does not affect the lesion. CDT preserves too few correlations. If a predictor has already predicted the agent’s action, CDT intervenes on the physical action while holding the predictor’s prediction fixed, thereby imagining a world in which a reliable predictor inexplicably made a mistake.

P-FDT tries to preserve exactly the decision-relevant dependencies. If a predictor’s prediction depends on the agent’s policy, then changing the policy changes the prediction. If a lesion merely statistically correlates with the agent’s action but does not depend on the policy, then changing the policy does not change the lesion.

This requires counterpossible reasoning. If the actual decision procedure outputs \(\pi^*\), then evaluating a different policy \(\pi\) asks us to imagine that the very same procedure outputs something else. The source acknowledges that we do not yet have a fully satisfactory theory of such counterpossibles. P-FDT therefore assumes that the agent has, or can approximate, a model \(G\) telling her how the world would change under such an intervention.

---

## 4. Observations as inputs, not merely as evidence

One of the most distinctive features of P-FDT is its treatment of observations.

In EDT, an observation is usually handled by conditioning. If the agent sees \(x\), she evaluates actions using probabilities conditioned on \(x\). In CDT, the agent also conditions on \(x\), but then performs a causal intervention on the action.

P-FDT treats observations differently. An observation is primarily an **input to the policy**. The selected policy says what to do if this observation occurs, what to do if that observation occurs, and so forth. When evaluating policies, P-FDT allows the observation itself to vary under the intervention, because whether the agent receives a certain observation may itself depend on the policy.

This is crucial in problems where predictors decide what to show the agent, whether to send a letter, whether to fill a box, or whether to offer a deal. If the agent’s policy were different, she might have received different evidence.

A simple operational rule is therefore:

1. Choose the policy \(\pi\) that maximizes expected utility under the policy intervention.
2. Given actual observation \(x\), execute \(\pi(x)\).

This has a somewhat updateless flavor. The agent does not ask, “Given that I have seen \(x\), which physical action is best?” Instead she asks, “Which policy should my decision procedure output?” Then she acts according to that policy at her actual input.

There is an unresolved subtlety here. If the agent has evidence that is genuinely independent of her policy, it may be reasonable to incorporate that evidence by conditioning the background model before evaluating policies. For example, if she has observed a policy-independent weather report, she may condition on it. But if the observation itself may have been produced by predictors responding to her policy, conditioning on it can lead to mistaken decisions. The source does not give a general rule for separating policy-independent from policy-dependent evidence. My own preferred interpretation is that P-FDT should by default treat the actual observation as an input to the selected policy, and only condition on information that is known to be exogenous to the policy.

---

## 5. Example: Newcomb’s problem

In Newcomb’s problem, an agent faces a transparent box containing \$1,000 and an opaque box that contains either \$1,000,000 or nothing. A highly reliable predictor filled the opaque box if and only if she predicted the agent would take only the opaque box.

Since there is effectively one observation, policies reduce to actions. Let

\[
\pi_1(\emptyset)=\text{one-box},
\]
\[
\pi_2(\emptyset)=\text{two-box}.
\]

The predictor’s prediction subjunctively depends on the agent’s policy. Thus, under the intervention \(\operatorname{do}(D_\Pi=\pi_1)\), the box is probably full. If the predictor is 99% reliable, then approximately

\[
\operatorname{EU}_{\text{P-FDT}}(\pi_1)
=
0.99 \cdot 1{,}000{,}000
+
0.01 \cdot 0
=
990{,}000.
\]

Under the intervention \(\operatorname{do}(D_\Pi=\pi_2)\), the predictor probably left the box empty. The agent then gets the opaque box’s contents plus the visible \$1,000:

\[
\operatorname{EU}_{\text{P-FDT}}(\pi_2)
=
0.01 \cdot 1{,}001{,}000
+
0.99 \cdot 1{,}000
=
11{,}000.
\]

P-FDT selects \(\pi_1\). The agent one-boxes.

CDT two-boxes because it intervenes on the physical action while holding the predictor’s prediction fixed. EDT one-boxes because one-boxing is good news. P-FDT one-boxes for a different reason: the policy of one-boxing is what the predictor is responding to.

---

## 6. Example: the smoking lesion problem

In the smoking lesion problem, smoking is correlated with cancer, but only because a lesion causes both a tendency to smoke and cancer. Smoking itself does not cause cancer. The agent gains \$1,000 from smoking and gains \$1,000,000 if she does not die of cancer.

Here, the lesion does not subjunctively depend on the agent’s policy. The lesion is not predicting her decision procedure. It merely causes her preferences. Therefore, when P-FDT intervenes on the policy node, the probability of having the lesion is held fixed.

Let \(\pi_S\) be the policy of smoking and \(\pi_R\) the policy of refraining. Since the cancer risk is unchanged by the intervention,

\[
\operatorname{EU}_{\text{P-FDT}}(\pi_S)
=
\operatorname{EU}_{\text{P-FDT}}(\pi_R)
+
1{,}000.
\]

P-FDT therefore recommends smoking.

This matches CDT’s prescription, but for a reason closer to CDT’s: P-FDT does not treat smoking as evidence that should be managed. It asks which policy would produce the best outcomes, holding fixed variables that do not depend on the policy.

---

## 7. Example: transparent Newcomb and Parfit’s hitchhiker

The policy formulation becomes especially natural in the transparent Newcomb problem. Both boxes are transparent. The predictor filled the opaque box if and only if she predicted that the agent would one-box upon seeing that both boxes are full.

Here the agent’s observation matters. Let \(f\) be the observation “the opaque box is full,” and let \(e\) be the observation “the opaque box is empty.” Consider two policies:

\[
\pi_O(f)=\text{one-box}, \qquad \pi_O(e)=\text{two-box},
\]

and

\[
\pi_T(f)=\text{two-box}, \qquad \pi_T(e)=\text{two-box}.
\]

P-FDT evaluates these policies by intervening on the policy node.

If the agent implements \(\pi_O\), then upon seeing a full box she will one-box. A reliable predictor, anticipating this policy, fills the box. In the overwhelming majority of cases, the agent sees a full box and one-boxes, receiving about \$1,000,000.

If the agent implements \(\pi_T\), then upon seeing a full box she will two-box. The predictor, anticipating this, leaves the box empty. The agent usually sees an empty box and receives only \$1,000.

Thus,

\[
\operatorname{EU}_{\text{P-FDT}}(\pi_O)
\gg
\operatorname{EU}_{\text{P-FDT}}(\pi_T).
\]

P-FDT selects \(\pi_O\). If the agent actually sees a full box, she one-boxes.

This is the same logic as Parfit’s hitchhiker problem. A driver can detect whether the agent will pay \$1,000 after being rescued. The agent should adopt the policy “pay if rescued.” If the driver predicts this policy, the agent is rescued. If the agent’s policy is “do not pay once rescued,” the driver detects this and leaves the agent in the desert.

The surprising feature is that P-FDT may prescribe an action even when the agent already knows facts that seem to make another action locally attractive. Upon seeing the full box, two-boxing seems to gain an extra \$1,000. But P-FDT says that the policy of two-boxing upon seeing a full box is a policy that usually does not see a full box in the first place. The agent evaluates the policy globally, then applies the actual input.

---

## 8. Example: blackmail and policy-dependent observations

P-FDT also handles blackmail cases by recognizing that receiving the blackmail demand may itself depend on the agent’s policy.

In a mechanical blackmail problem, a blackmailer runs a damaging program only if she predicts that the agent will pay upon receiving the blackmail letter. If the agent’s policy is “pay if I receive the letter,” the blackmailer predicts payment and sends the letter. If the agent’s policy is “refuse if I receive the letter,” the blackmailer predicts refusal and does not send the letter.

Let \(\pi_P\) be the policy of paying upon receiving the letter, and \(\pi_R\) the policy of refusing. Under \(\pi_P\), the agent is blackmailed and loses \$1,000. Under \(\pi_R\), the agent is usually not blackmailed at all. Thus P-FDT selects \(\pi_R\). If, counterfactually, the agent nonetheless receives the letter, she refuses to pay.

This may look like ignoring evidence: the agent is holding the letter, so surely she has been blackmailed. But P-FDT says that the relevant question is not “What should I do given that I see the letter?” in the ordinary evidential sense. The question is: “Which policy should my decision procedure output?” A policy of paying makes blackmail profitable; a policy of refusing makes blackmail unprofitable. P-FDT chooses the policy that removes the incentive to blackmail.

---

## 9. Multi-agent cases and the role of policies

Footnote 16 says that the difference between action-selection and policy-selection “only matters in multi-agent dilemmas so far as we can tell.” The source does not fully develop this point, so here we enter more speculative territory.

In single-agent cases, choosing a policy often collapses into choosing an action for the actual observation. But in multi-agent cases, other agents may reason about the agent’s entire strategy. They may decide whether to cooperate, whether to make an offer, or whether to send a threat based on what policy they expect the agent to implement.

For example, in a psychological twin prisoner’s dilemma, the agent and her twin use the same decision procedure. If the shared procedure outputs a policy of cooperation, both cooperate. If it outputs a policy of defection, both defect. P-FDT represents this by making the twin’s behavior subjunctively depend on the same policy variable, or on a variable constrained to match it.

In more complicated games, other players may respond not merely to what the agent does now, but to what the agent would do in other contingencies. A policy is then the natural object of evaluation. P-FDT’s policy intervention lets the agent ask: “What would happen if my entire strategy were different?” rather than merely “What would happen if my current physical movement were different?”

The source leaves open exactly how to model such cases. In particular, it does not give a precise rule for when another agent’s decision variable should be treated as computing the same function as one’s own, when it should be treated as predicting one’s policy, and when it should be treated as independent. A reasonable operational approach is to include separate policy variables for each agent and add dependency edges wherever one agent’s behavior is predicted by, simulated by, or logically constrained by another agent’s policy.

---

## 10. Open problems and operational interpretation

P-FDT is elegant, but the source leaves several important questions unresolved.

First, how does one construct the dependency graph \(G\)? For CDT, Pearl’s causal machinery gives at least a formal starting point. For P-FDT, we need a way to identify subjunctive dependencies: which predictors, simulations, twins, or logical constraints depend on the agent’s decision procedure. The source explicitly says that this is perhaps the largest open problem for the theory.

Second, how should P-FDT handle logical uncertainty? A real agent may not know what her own decision procedure would output in all circumstances. The source assumes the agent can reason about the outputs of mathematical functions, including her own, but does not give a complete account of this reasoning.

Third, how should P-FDT treat actual observations that are already known? My reconstruction evaluates policies globally and then applies the actual observation. This fits the policy-selection passage and the updateless flavor of the blackmail examples. But in ordinary decisions involving policy-independent evidence, it may be appropriate to condition the model on that evidence before evaluating policies. The source does not settle this.

Fourth, what exactly is the difference between policy-level and action-level functional decision theory in multi-agent dilemmas? The source says the difference matters there, but does not give a detailed example. My interpretation is that policy selection matters when other agents respond to the agent’s strategy as a whole, rather than to a single isolated action.

Despite these open points, a practical procedure for applying P-FDT emerges from the source and the reconstruction above:

1. Identify the possible observations \(\mathcal X\), actions \(\mathcal A\), and candidate policies \(\Pi\).
2. Build a model of the world containing variables for observations, actions, predictions, outcomes, and the policy-output variable \(D_\Pi\).
3. Mark which variables subjunctively depend on \(D_\Pi\). Predictors, copies, and simulations of the agent typically do; merely statistical common causes typically do not.
4. For each policy \(\pi\), imagine the world under the intervention \(\operatorname{do}(D_\Pi=\pi)\).
5. Compute or estimate the expected utility of each such world.
6. Select the policy with highest expected utility.
7. Execute the action prescribed by that policy at the actual observation.

This procedure is not always easy to carry out. The hard part is step 3: knowing which dependencies are decision-relevant. But the structure gives a unified way of thinking about unfamiliar cases.

---

## Conclusion

Policy Functional Decision Theory, P-FDT, is the policy-level version of the decision theory described in the source. It treats the agent’s decision procedure as a fixed mathematical function whose output is a policy, not merely a one-time action. The agent evaluates policies by intervening on the policy variable and asking which policy would yield the best expected outcome, preserving dependencies on that policy while holding fixed merely statistical correlations. The agent then applies her actual observation to the selected policy.

This approach gives the characteristic functional-decision-theoretic verdicts: one-box in Newcomb’s problem, smoke in the smoking lesion problem, pay in Parfit’s hitchhiker problem, one-box in transparent Newcomb when seeing a full box, and refuse blackmail when receiving a blackmail demand. More generally, P-FDT recommends acting as the agent would have wanted to precommit to act, without requiring an actual precommitment device.

The theory remains incomplete. It needs a better account of subjunctive dependency, counterpossible reasoning, logical uncertainty, and the exact role of policies in multi-agent settings. But as a normative ideal, P-FDT offers a clear principle: choose the policy that this very decision procedure should output, and then follow it.

---

## Reference

Yudkowsky, Eliezer, and Nate Soares. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request: write substantive mathematical essay/blog post explaining P-FDT (policy functional decision theory), using footnote 16 policy-selection passage as primary source. Need target approx 2400-3000 words including references etc. Must use P-FDT consistently, identify other decision theories by distinct names. Need explain how theory evaluates alternative actions or policies and treats dependencies and counterfactuals. Where source leaves open, explain uncertainty and operational interpretation. Distinguish source claims vs own assumptions. Need finish brief conclusion.

Need first analyze source. Key footnote 16: "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition." Also earlier footnote 7: "In the authors' preferred formalization of FDT, agents actually iterate over policies (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper." Need P-FDT based on policy-selection passage. We need define P-FDT as policy version: choose policy π: observations -> actions (or perhaps mapping inputs to actions) by intervening on node representing output of decision procedure for policy? Let's parse: "intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then apply her inputs in order to select an action." So P-FDT selects a policy π from set Π. The decision procedure outputs a policy, then given actual observation x action = π(x). When evaluating candidate policy π, imagine world where the agent's decision function outputs π (or where all relevant agents/subjunctive dependents using same policy?); then actual action is π(x) but counterfactual worlds with different observations may be affected: predictions of agents may depend on policy, and observations may differ. Need define expected utility of policy as sum over outcomes given do(P-FDT output = π), possibly with actual input? In source action FDT equation: FDT(P,G,obs)=argmax_a E[V | Do(FDTvar(P,G,obs)=a)]. For policy P-FDT, likely: P-FDT(P,G)=argmax_{π∈Π} E[V | Do(FDTvar(P,G)=π)] maybe then action = π(obs). But need careful: If choose policy, node FDT(-) outputs π, then agent applies inputs to π. The source says "intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then apply her inputs in order to select an action." So perhaps variable is FDT(P,G) = π, and Act = π(Obs). In graph, intervention sets policy node, action is function of policy node and observation. But observations may themselves depend on policy via predictors. The expected utility should be E[V | do(FDT(P,G)=π)] with no conditioning on obs? Or conditioned on actual obs? In action-level FDT, observations are handled by switching intervention node: FDT(P,G,obs) = argmax_a E[V | Do(FDTvar(P,G,obs)=a)]. For policy-level, if actual observation x, do we evaluate policies using E[V | Do(FDT(P,G)=π)] and then apply π(x)? The footnote: choose policy which maps inputs to actions, to which agent then applies inputs to select action. This suggests evaluate policy before/without conditioning on actual input? But if agent already has observation, they might still choose policy and apply input. Source's updateless flavor: FDT responds to observation by changing which node intervenes; in policy formulation, maybe observation is just input to selected policy, not conditioning. The paper says "FDT says that agents should entertain the hypothesis that, if their action were different, they might have made different observations." Also footnote says preferred formulation intervenes on node FDT(-) to choose policy. This is updateless-ish: policy chosen based on expected utility across possible inputs, not conditional on actual input? Need explain.

Need make P-FDT consistent name. P-FDT = Policy Functional Decision Theory. Need maybe call action-level FDT "action-level FDT" or just FDT as source? But user says use P-FDT consistently as assigned decision theory's name, including headings and examples, and identify any other decision theory by distinct name. So use P-FDT for our theory. We can discuss CDT, EDT, and maybe action-level FDT (source's main equation) but must ensure assigned theory P-FDT. Could say source calls it FDT, footnote preferred policy formulation; I will call this P-FDT. Need maybe avoid calling P-FDT "FDT" except quoting source? Could use "the source's FDT" when quoting, but assigned name P-FDT. Need identify other theories EDT, CDT. Maybe also action-level FDT as "action-level FDT" distinct? But if P-FDT is version of FDT, careful. User wants P-FDT as assigned decision theory. Other decision theory discussed by distinct name, so action-level FDT can be "action-level FDT" if needed. But perhaps better discuss EDT, CDT only, plus P-FDT. We can mention source's action-level equation as a simplification of P-FDT; not a separate theory.

Need essay ~2400-3000 words. Need include mathematical definitions, equations, examples. Need primary source footnote 16. Need explain uncertainties: what is set of policies? How construct subjunctive dependency graph G? How handle observations? How define expected utility with policy interventions? How multi-agent difference? Need propose operational interpretation: P-FDT chooses policy π maximizing expected utility under a structural model where a variable D = P-FDT(P,G) is intervened to π, action at any node is π(Obs), and observations/predictors that depend on policy update accordingly. If actual observation x is already known, the recommended act is π*(x), where π* is selected by global policy evaluation. Or if policy selected at time of decision with actual obs included, evaluate π by expected utility conditional on do(D=π) maybe not conditioning on obs? Need clarify.

Need likely include formal notation:
- Outcomes O, actions A, observations X, policies Π = {π: X -> A}. Utility U(o) or V.
- World model (P,G) with variables including Obs, Act, V, and D (policy node) representing output of P-FDT given model. Structural equations: Act = D(Obs) perhaps; predictors may be functions of D or of policy; Obs may be function of predictors etc.
- P-FDT recommendation: choose π* ∈ argmax_{π∈Π} E_{P}[V | do(D=π)] (maybe with model inputs). Then execute a = π*(x), where x is actual observation. If observations arrive sequentially, policy maps histories to actions.
- Alternatively if we want include actual observation as input to decision algorithm: P-FDT(P,G,x) = π*(x), where π* = argmax_π E[V | do(P-FDT(P,G)=π)]. This differs from action-level FDT(P,G,x)=argmax_a E[V | do(P-FDT(P,G,x)=a)].

Need connect to source: footnote 16 says authors preferred formulation intervenes on node FDT(-) to choose a policy mapping inputs to actions, then apply inputs. They say difference only matters in multi-agent dilemmas as far as they can tell. Need quote faithful: "the author's preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then apply her inputs in order to select an action." Actually source has typo? "to which the agent then apply her inputs" maybe "applies". Need keep faithful maybe quote partial: "intervenes on the node \FDT(-) to choose not an action but a \emph{policy} which maps inputs to actions". Need include footnote 16 exact? It says: "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node \FDT(-) to choose not an action but a \emph{policy} which maps inputs to actions, to which the agent then apply her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this \paper for ease of exposition." Need maybe quote exact but not too much.

Need explain how P-FDT evaluates alternative policies: Not by conditioning on action as EDT; not by do(Act=a) as CDT; by do(D=π), where D is logical/computational variable representing policy output. This preserves subjunctive dependencies: predictors, twins, copies, blackmailers that depend on the policy. It breaks merely evidential correlations not due to policy (lesions). It may change expected observations because policy influences whether one receives certain inputs. Need explain counterfactuals: counterpossible, because if deterministic procedure actually outputs π*, evaluating other π requires imagining procedure has different output. Use graph G to specify how other variables would change. Need discuss observation handling: P-FDT does not simply Bayesian condition on actual observation when evaluating policy; actual observation is an input to policy. In transparent Newcomb, P-FDT selects policy mapping see-full -> one-box, see-empty -> maybe two-box. It evaluates policy globally; if sees full, executes one-box. The source's action-level FDT for transparent Newcomb: intervenes on FDT(P,G,full). Policy P-FDT can represent as one policy with branches. Need show example maybe transparent Newcomb or hitchhiker. Also multi-agent where policy matters: perhaps sequential or game where other agents observe your policy or respond to it before your later input? Need illustrate difference policy vs action? The source says difference only matters in multi-agent dilemmas. Need maybe construct or discuss why: in multi-agent settings, selecting a policy can affect others' actions before particular observations, and commitments across possible inputs matter. E.g., blackmail: policy of refuse-if-letter affects whether letter sent. But action-level FDT with observation-specific node can emulate? Maybe policy formulation helps in games with simultaneous policy selection? Need not fully resolve but explain uncertainty.

Need maybe mention policy selection resembles choosing a strategy in game theory, not just an act. It evaluates expected utility of being the type/algorithm that implements π. The agent then applies actual input. This can be seen as maximizing ex ante expected utility over policy, but with subjunctive intervention rather than ordinary causal expectation. Need distinguish from simple precommitment: not physical binding, but logical selection of policy.

Need word count 2400-3000. Need plan structure:
1. Title maybe "Policy Functional Decision Theory (P-FDT)".
2. Intro: decision theories, P-FDT from footnote 16, core idea: choose policy output of fixed decision function. Source claims and my interpretation.
3. Formal setup:
   - finite action set A, observation/input set X (histories), outcomes O, utility U.
   - policies π: X -> A. Π.
   - probabilistic/structural world model (P,G). Include variable D_π? Actually D = P-FDT(P,G), value in Π. Act = D(Obs). Obs may depend on D through predictors. V = U(Outcome).
   - Intervention do(D=π). Expected utility of policy: EU_P-FDT(π) = E[V | do(D=π)]. Then π* ∈ argmax; action = π*(x). Equation. If stochastic policies? Could allow randomized policies, but source focuses deterministic; mention optional. If observations are histories, policy maps histories to actions.
   - Compare EDT: argmax_a E[V | Obs=x, Act=a]; CDT: argmax_a E[V | do(Act=a), Obs=x]; action-level FDT: argmax_a E[V | do(D_x=a)] where D_x = FDT(P,G,x). P-FDT: argmax_π E[V | do(D=π)], then π(x). Need note source's main text uses action-level for exposition; P-FDT is preferred per footnote.
4. Dependencies and counterfactuals:
   - subjunctive dependence: systems computing same function or accurate predictors. Intervene on type/policy, not token physical act. Preserve correlations that flow from policy; sever correlations not due to policy (lesions). Counterpossible reasoning; G needed.
   - Observations: P-FDT may entertain different observations under different policies. Actual observation used as input, not necessarily conditioned upon. If policy changes, predictors may have acted differently, so actual input could have been different; but once policy selected, the actual branch is executed.
5. Examples:
   - Newcomb: policies: one-box regardless? If predictor fills iff policy outputs one-box (or if input standard no observation maybe policy maps null to one-box). EU(one)=~1,000,000; EU(two)=~1,000; choose one.
   - Smoking lesion: policy smoke/refrain; lesion causes preference but not subjunctively dependent on policy. EU(smoke)=EU(refrain)+1000*prob? choose smoke. Need maybe concise.
   - Transparent Newcomb / Parfit's hitchhiker: policies: π_full one-box if see full; maybe π_empty two-box if see empty. Evaluate globally. If policy one-boxes on full, predictor likely fills; if policy two-boxes on full, predictor likely leaves empty, so expected value lower. Choose policy one-box-if-full. Apply input full -> one-box. This illustrates observation as input and counterfactual observation changes.
   - XOR blackmail/mechanical blackmail: policy refuse-if-letter; under do(policy=refuse-if-letter), probability of letter low; expected utility better; if actual letter, refuse. Could use to show policy handles observations differently.
   - Multi-agent: psychological twin PD: policy cooperate? If twin runs same policy, do(cooperate-policy) makes both cooperate. Could mention policies matter when multiple agents reason about each other's policies, e.g., game where your policy affects other player's move before your observation. But source leaves details open.
6. Open questions and operational interpretation:
   - Source leaves: how construct G for subjunctive dependencies; how specify Π; whether evaluate ex ante or conditioned on current observation; how handle stochastic/nondeterministic agents, logical uncertainty, counterpossibles; how exactly policy formulation differs in multi-agent dilemmas. Need explain.
   - My operational interpretation: use causal-graph plus logical-dependency graph; identify variables that are functions of agent's policy (predictor variables, copies, simulations); set D=π and propagate. If already observed x, do not condition away the possibility that π would have led to different x; instead evaluate policy over whole model and then apply x. If there is a known actual observation that is not influenced by policy? Then conditioning may be permissible; but default is updateless policy evaluation. For bounded agents, approximate by listing plausible policies and simulating their consequences. Need justify: matches source's treatment of observations (changing intervention node) and footnote's policy mapping.
   - Need distinguish source claims vs own: Source claims P-FDT chooses policy, difference only matters multi-agent, FDT preserves subjunctive dependencies, etc. My additions: formal equation EU(π)=E[V|do(D=π)], treatment of actual observation as applying selected policy, operational graph construction suggestions, stochastic policies.
7. Conclusion: P-FDT as policy-selection version of functional decision theory; chooses best policy by subjunctive intervention, then applies actual input; useful for predictors, blackmail, coordination; open problems.

Need maybe references minimal: cite Yudkowsky & Soares 2017? The source. Could include brief reference at end: Yudkowsky, E., & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060v2. And perhaps Pearl 2000? But target says avoid lengthy bibliographies. Could include one or two references. Need word count include references. Need around 2500-2900. Need not too long? Need final answer only essay.

Need be careful with notation: P used both probability and policy; maybe use Pr for probability, π for policy, ? Let's define:
-  maybe ? Let's use ? Better:
  - ? Let's choose  not. Let ? We'll use ? Hmm.
  - Let ? Use ? Simpler: Let ? no.
  - Use ? Let's use \mathbb{P} for probability. Policy set \Pi. Decision variable D_{\Pi} or \mathrm{PFD}. Let \mathrm{PFD}(M) denote policy-output variable. Then
\[
\operatorname{P-FDT}(M,x)=\pi^*(x), \quad \pi^* \in \arg\max_{\pi\in\Pi} \mathbb{E}[V \mid do(D_\Pi=\pi)].
\]
Where M=(\mathbb{P},G). If want include G inputs: D_Π = P-FDT(M). Might need include observation x? Maybe:
\[
\mathrm{EU}_{\mathrm{P-FDT}}(\pi) := \mathbb{E}_{\mathbb{P}}[V \mid do(D_{\Pi}=\pi)].
\]
Then if actual observation history x, action a=π*(x). If observation not influenced by policy and we want conditional version, could define:
\[
\pi^*_x \in \arg\max_\pi \mathbb{E}[V \mid do(D_\Pi=\pi), Obs=x]?
\]
But I think source's updateless suggests no conditioning on obs in policy evaluation. However, if agent only chooses policy after seeing x, and x is known, evaluating policies without conditioning on x may choose policy good ex ante but bad given x? But P-FDT says apply input; if x is known and policy selection occurs after x, do we choose policy based on ex ante or given x? Footnote says choose policy mapping inputs to actions, then apply inputs. This implies choose policy as a whole, not per input. If actual input x is already known, one might still choose policy by ex ante expected utility because choosing a policy that behaves well across inputs, including x, is what predictors reward. But if x is truly exogenous and no predictor depends on policy, ex ante and conditional may differ if x has utility-relevant information. Should P-FDT condition on x for facts not policy-dependent? The source action-level FDT responds to observation by changing intervention node, not by conditioning. But it may still incorporate observation as input to function; the model includes observation as variable. In transparent Newcomb, after seeing full, action-level FDT intervenes on FDT(P,G,full), not conditioning? It calculates E[V | Do(FDT(P,G,full)=a, Obs=full)]? Source has: find a maximizing E(V | Do(FDTpgv{full}=a, Obs=full). There's a missing parenthesis. It includes Obs=full? It says evaluate FDT(Pf,Gf,full) requires maximizing E(V | Do(FDTpgv{full}=a, Obs=full). So it conditions on obs=full? But also intervention changes predictors so obs may have been different? Wait in transparent Newcomb, they include Obs=full in do? They say "Given Gf and Pf, evaluate FDT(Pf,Gf,full), which involves finding a maximizing E(V | Do(FDTpgv{full}=a, Obs=full)." Then in one-box case if accurate prediction, full; if inaccurate, prediction two, box empty, Act determined by FDT(empty) instead. They condition on Obs=full? Hmm if they condition on Obs=full, then in inaccurate branch where box empty, Obs would not be full, contradiction? Let's parse: They may not have explicit Obs variable in graph? Figure includes? For transparent Newcomb, Fiona graph has prediction -> Act? It says Act depends on FDT(full), FDT(empty), and Prediction, with Prediction determining which of two FDT variables controls Act. It doesn't show Obs. They might not condition on Obs but evaluate FDT(full) as the decision procedure run upon seeing full. They imagine if FDT(full) outputs one-box; if predictor inaccurate then box empty and she would be shown empty, thus run FDT(empty) instead. So actual observation full is assumed as input for the procedure being evaluated, but not conditioning on obs in a way that fixes it under intervention? The equation in source maybe has typo: E(V | Do(FDTpgv{full}=a), Obs=full). Maybe they condition on Obs=full? But then if intervention makes obs empty, conditioning inconsistent. Maybe observation is an input selected externally: they evaluate the algorithm with input full, but world may not give full under counterpossible? They say "even in the case where Fiona has observed that box B is full, when she envisions two-boxing, she envisions a scenario where she instead (with high probability) sees that the box is empty." So she does not hold Obs=full fixed. She evaluates the policy/algorithm that would be run if full, but under counterpossible output two-box, the predictor would likely not have filled, so she wouldn't see full and would run empty algorithm. Thus observation input is not fixed as a condition; it is part of structural model. Good. So for P-FDT, evaluate policy without conditioning on actual observation; actual observation determines which branch of policy is executed after policy selected. But the decision variable D may be "policy chosen given model" not observation-specific. If the agent is already at observation x, she still asks: which policy should this decision procedure output? Then executes π(x).

Need maybe mention if x contains information about exogenous state not affected by policy, P-FDT can incorporate it as an input: the policy maps x to action, and the model's probability distribution over states conditional on x may be used. But the intervention on policy should not condition away policy-dependencies of x. Operational: evaluate expected utility of π in model updated on exogenous information that is known to be policy-independent; otherwise do not condition on x. This is subtle; we can propose.

Need ensure "P-FDT" consistently. In equations, use P-FDT maybe hyphen. Need avoid "FDT" alone unless quoting or referring source. Could write "the source's FDT (which I will treat as the action-level simplification of P-FDT)". But user says use P-FDT consistently as assigned decision theory's name, including headings and examples. It may be okay to mention source's term FDT but assigned theory P-FDT. Need maybe say: "The source calls the theory FDT; because the assignment asks for the policy-selection version in footnote 16, I call it P-FDT." Then always P-FDT.

Need word count. Let's draft with headings:
- Introduction (approx 300)
- 1. From acts to policies (approx 500)
- 2. Expected utility under policy intervention (approx 600)
- 3. Dependencies, observations, and counterfactuals (approx 500)
- 4. Examples (approx 700)
- 5. Open points and operational interpretation (approx 500)
- Conclusion + references (approx 200)
Total 3300? Need trim to 2400-3000. Need maybe 2600. Let's aim ~2700.

Need be precise enough reader can decide unfamiliar cases. Need give procedure steps:
1. Identify actions A, possible observations X, policies Π.
2. Build model M with variables and subjunctive dependency graph G. Mark D as P-FDT policy variable; specify which variables depend on D (predictors, copies) and which do not (lesions).
3. For each π, perform intervention do(D=π), compute expected utility.
4. Pick π* max; execute π*(x).
Need mention if model is deterministic, expected utility is sum over noise variables; if stochastic, probabilities.

Need maybe formalize intervention with structural equations. Let variables Z. G gives structural equations. D_Π is exogenous for intervention. For each π, replace equation for D_Π with D_Π=π; set Act = D_Π(Obs); solve distribution over V. EU = E[V]. This is Pearl do-style but on logical variable. Need mention if there are multiple agents with same policy? In multi-agent, D may represent policy output of agent; other agents may have their own policy variables. If they are perfect twins or predictors, their actions/predictions may be functions of D or of their own D_j. P-FDT evaluates own policy, holding others' policies fixed? In twin PD, if twin uses same decision theory, one may model twin action as same D? Source says same course of reasoning. For policy P-FDT, if twin runs same policy-selection procedure, D_twin may equal D_self by subjunctive dependence. Under do(D_self=π), perhaps D_twin=π too if same function. Need careful: Intervening on own policy variable while twin's is same logical output? If they are identical and face same input, maybe there is one variable D for shared computation. If not, graph encodes correlation via logical dependence. Source says when two systems compute same function, behaviors subjunctively depend on function. So graph should make twin action depend on same D or a copy constrained to equal D. P-FDT then cooperation yields both cooperate. Could mention as open: exact representation of shared computations not fully formalized.

Need discuss dominance? Maybe briefly: P-FDT has its own dominance: policy π dominates π' if, under all relevant subjunctive dependencies, do(D=π) never worse and sometimes better. But not necessary. Could mention to explain evaluation alternative actions/policies.

Need include source quotations. Need quote footnote 16 and maybe "Which output of this decision procedure causes the best outcome?" Source: normative principle asks "Which output of this decision procedure causes the best outcome?" Actually source: "Which output of this decision procedure causes the best outcome?" (in Overview: asks “Which output of this decision procedure causes the best outcome?” as opposed to...). Need maybe quote: "intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions". Need keep faithful.

Need distinguish source claims from own: Use phrases "The source claims...", "I add the following operational convention...", "This is not explicit in the source...".

Need discuss "policy-selection passage in footnote 16 primary source". Need maybe state: The main paper gives action-level equation; footnote 16 says preferred formulation chooses policy. I will take P-FDT to be that formulation. The source leaves exact formal equation for policy unspecified; my equation is reconstruction.

Need handle "how it evaluates alternative actions or policies" — alternative actions are evaluated via policies; if only one observation or no observation, policies reduce to actions. For actual act, P-FDT chooses policy then applies input. In examples, compare policies. Need mention if policies are mappings from observations to actions; in single decision with trivial observation, policy is equivalent to action.

Need perhaps define expected utility more mathematically:
Let M = (Pr, G). Let V be utility variable. Let D_Π be the policy variable. For π ∈ Π:
\[
EU_{M}^{\mathrm{P-FDT}}(π) = \sum_{o} Pr(o | do(D_Π=π)) U(o)
\]
or \mathbb{E}_{Pr}[V | do(D_Π=π)].
Then
\[
Π^*(M) = \arg\max_{π∈Π} EU_{M}^{\mathrm{P-FDT}}(π).
\]
If actual history x, P-FDT(M,x) = π^*(x). If there are multiple max, tie-break arbitrary. If policies stochastic: π(a|x), intervention sets stochastic policy, EU = expectation over policy randomness; but source likely deterministic.

Need note "do" on logical variable not Pearl causal only. G includes subjunctive dependencies: if predictor's prediction is a function of D_Π, then do(D=π) changes prediction. If lesion is not function of D, do doesn't change lesion. If observation is a function of predictor, do changes observation distribution. This captures counterfactuals.

Need discuss "counterpossibles": Since actual D may be π*, evaluating π ≠ π* is logically counterpossible if deterministic. P-FDT requires reasoning as if the fixed procedure had different output. Source admits no full account; operational: use model G and heuristics. Need include.

Need example calculations with numbers maybe:
Newcomb: predictor accuracy .99. Policies π_1 (one-box), π_2 (two-box). Under do(D=π_1): Box full .99, EU ≈ .99*1,000,000 + .01*0 = 990,000 (if only B; source says $990,000). Under do(D=π_2): full .01, EU = .01*1,001,000 + .99*1,000 = 11,000. Choose π_1.
Smoking lesion: lesion probability p, smoking utility +1000; cancer probabilities unchanged by do(D=smoke). Choose smoke because EU(smoke)-EU(refrain)=1000*Pr(policy controls? in source p? Simpler: +1000, cancer risk same). But source formalizes two utility functions; we can simplify and mention.
Transparent Newcomb: Policies: π^O: if full one-box, if empty two-box; π^T: if full two-box, if empty two-box. Under do(π^O), predictor accurate .99 fills; EU ≈ 990,000 + small. Under do(π^T), predictor predicts two-box and leaves empty; if agent sees empty gets 1000 maybe; EU ≈ 11,000? Need compute source: for action one-box full: $990,000 + 0.01q*1000; two-box: $11,000 + q*990 (source says $110,00? likely typo $11,000). So choose one-box-if-full. P-FDT policy evaluation naturally captures branch.
Mechanical blackmail: policies pay-if-letter vs refuse-if-letter. Under refuse, blackmailer predicts refusal and doesn't send; high utility. Under pay, blackmailer sends; pay loses 1000. Choose refuse; if actual letter, refuse.

Need maybe include multi-agent policy difference. Since footnote says difference only matters in multi-agent dilemmas, we need explain possible why. In multi-agent, selecting a policy can affect others' expectations and actions across multiple possible inputs; choosing action at a particular input may fail to capture commitment value. Example: coordination game where other agent chooses whether to cooperate based on your policy before you observe their choice. If you evaluate only action conditional on seeing them cooperate, you might defect; but P-FDT chooses policy cooperate-if-they-cooperate? Hmm. Or voting coalition: ten FDT agents; policy vote if in coalition; each recognizes their policy selection subjunctively linked. Source mentions voting and gym but not policy-specific. Need maybe construct: Two agents negotiate; one proposes deal based on predicted policy of other. If P-FDT selects policy "accept fair deal", predictor proposes; if selects "reject", no deal. Policy selection matters because other responds to the policy, not a single action. But action-level FDT could also evaluate observation-specific action? Maybe if observation (proposal) depends on policy, action-level with observation node can still handle. Source says difference only matters in multi-agent as far as they can tell; they don't elaborate. Need explain uncertainty: the footnote does not give an example where action-level and policy-level diverge; I suspect policy matters when agents must reason about entire strategy, not just one act, especially sequential games or when others condition on the policy itself. But exact divergence unresolved.

Need maybe include "P-FDT as policy selection not physical precommitment". It acts as if precommitted because policy chosen globally.

Need maybe address "how it treats relevant dependencies and counterfactuals" in depth. Use "subjunctive dependence" term. Define: X subjunctively depends on D if, had D's output been different, X would have been different in virtue of computing/predicting that output. Causal dependence is special case. Statistical correlation not enough. P-FDT's counterfactuals hold fixed all variables not subjunctively dependent on D, update those that are. Graph G encodes this. Need mention source's analogy: FDT to subjunctive dependence as CDT to causal dependence.

Need mention "type-token": CDT intervenes on token action; P-FDT intervenes on type/policy. Good.

Need possible mathematical example of policy graph: Variables D, Obs, Act, Pred, V. Equations:
D = P-FDT(M) (intervened)
Pred = f(D, noise)
Box = g(Pred)
Obs = h(Box)
Act = D(Obs)
V = U(Act, Box)
Then EU(π) computed by setting D=π. This could be included as formal clarity.

Need discuss if actual observation x after selection: Since Act = π(Obs), if Obs=x then action π(x). If under counterfactual π' the observation would likely differ, P-FDT still compares total worlds. This addresses "if I already see full box, why not two-box?" Because under do(policy two-box-if-full), the world where you see full is unlikely; the policy's global expected utility is low. P-FDT does not ask "given full, what action causes best outcome?" but "which policy should the agent's reasoning output?".

Need maybe mention "policy functional" name: policy functional because decision function maps inputs to actions; functional because treats decision as fixed mathematical function; policy because output is policy. Could say.

Need maybe include conclusion: P-FDT is coherent but relies on unresolved dependency graph and counterpossible reasoning; operational use requires modeling. It yields one-box, smoke, pay hitchhiker, refuse blackmail.

Need references: maybe:
- Yudkowsky, E. and Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060v2.
- Pearl, J. (2000). Causality. (for do). But avoid lengthy. Could include two.

Need ensure word count. Let's estimate: If final with headings and equations maybe 2700 words. Need not too verbose.

Potential pitfalls:
- Need not confuse P-FDT with standard FDT. Use P-FDT in headings.
- Need not say "FDT says" too much; maybe "the source's theory, which I am calling P-FDT".
- Need include footnote 16 as primary source; maybe quote: "intervenes ... to choose not an action but a policy". Need note source says "The difference only matters in multi-agent dilemmas so far as we can tell".
- Need maybe not overstate source's formalization: The source does not give a full policy equation; my equation is reconstruction. Need say.

Let's draft in final. Need ensure word count. Let's write robust essay.

Need maybe include math notation in Markdown. Use LaTeX. Need maybe no citations in-text heavy, but include references.

Detailed draft:

Title: Policy Functional Decision Theory (P-FDT): Choosing the Best Output of a Fixed Decision Procedure

Intro:
P-FDT is a decision theory that treats decision as output of fixed mathematical function. Unlike EDT/CDT, it asks which output of this procedure yields best outcome. The supplied source defines FDT mostly as choosing action; footnote 16 says preferred formulation chooses policy. I take this as primary. Quote. In source, no full formal equation for policy; I reconstruct.

Section "Policies and world-models":
Define A, X, Π. Policies map observation histories to actions. Model M=(Pr,G). Variables include Obs, Act, V, and D. D is the policy-output variable, D=P-FDT(M). Under normal model, D has some distribution maybe; under evaluation we intervene. Structural equation Act = D(Obs). If there are multiple agents, each has D_i, and other agents may model D_i. G encodes subjunctive dependencies.

Equation:
EU_M(π) = E[V | do(D=π)]. π* ∈ argmax. P-FDT(M,x)=π*(x). If trivial X={∅}, reduces to choosing action.

Comparison equations:
EDT: argmax_a E[V | Obs=x, Act=a]
CDT: argmax_a E[V | do(Act=a), Obs=x]
Action-level FDT source: argmax_a E[V | do(D_x=a)] where D_x = FDT(M,x). P-FDT differs by intervening on D, not D_x, and then applying x. This is my reconstruction from footnote.

Section "What the intervention preserves":
do(D=π) is not physical intervention only; it is counterpossible intervention on logical variable. Variables subjunctively dependent on D change; others fixed. Predictor/twin variables depend; lesion not. Source's phrase "subjunctive dependence". It requires counterpossible reasoning. Need graph.

Section "Observations":
P-FDT treats observations as inputs. It doesn't condition on actual observation in policy evaluation; actual x selects branch. If policy changed, x might have been different. This captures transparent Newcomb and blackmail. However, if some observation is known to be policy-independent, one may condition on it as exogenous information; this is my operational add.

Examples:
1. Newcomb. Show calculations.
2. Smoking lesion. Show policy no effect on lesion/cancer, choose smoke.
3. Transparent Newcomb/Hitchhiker. Policies; calculations; choose one-box-if-full. Explain actual full branch.
4. Mechanical blackmail maybe concise. Policy refuse-if-letter leads to no letter; if actual letter refuse.
5. Multi-agent note: twin PD, cooperate; policy matters in games. Could combine.

Open questions:
- source leaves how to construct G; how to identify subjunctive dependencies; how to handle logical uncertainty; policy set; stochastic; actual observation conditioning; multi-agent divergence.
- Operational interpretation: build graph with predictor variables as functions of D; if same algorithm, treat as shared D or equality constraint; approximate with simulations; evaluate finite policy set. Justify.

Conclusion.

Need word count maybe around 2800. Let's write with moderate detail.

Need maybe include exact quotation: "the author's preferred formulation ...". Use block quote? Could. Keep faithful.

Need ensure no accidental "FDT" alone as assigned theory. Could say: "The source names the theory FDT; I will reserve P-FDT for the policy version." In quotations, keep FDT as source. Good.

Need maybe mention "policy-selection passage in footnote 16" in intro.

Need maybe address "how theory evaluates alternative actions or policies" more explicitly: Alternative actions in a given situation are not directly compared; they are compared as branches of policies. If only one relevant observation, policies collapse to actions. If actual action a = π(x), to ask "what if I did a'?" P-FDT asks "what if the policy had prescribed a' at x (and possibly different elsewhere)?" and evaluates whole policy. This matters because predictors respond to policy, not isolated act.

Need maybe mention "counterfactuals" and "counterpossibles" in examples: In transparent Newcomb, when seeing full, P-FDT imagines policy two-boxes on full, then predictor likely left empty, so observation would differ. This is counterpossible if actual policy one-boxes.

Need maybe include note on self-reference: D represents output of P-FDT(M), model can contain variable for own output; source says Kleene recursion theorem/quine; harmless. Could mention briefly.

Need maybe include "P-FDT's expected utility is not ordinary expected utility of choosing policy causally"? Actually it is expected utility under intervention. It may be ex ante. Need mention physical precommitment: P-FDT doesn't need to causally bind future; selecting policy now is the decision. But if agent faces multiple sequential decisions, policy maps all histories; P-FDT chooses strategy. If same policy across time, coordinates with future selves.

Need maybe mention "fairness" not central. But maybe source claims P-FDT performs well in fair dilemmas; not needed.

Potential issue: The equation EU(π)=E[V|do(D=π)] may ignore actual observation x; if actual observation has evidential info about state not policy-dependent, evaluating without conditioning may choose policy good before info but not after. Example: you see a storm, policy "go sailing if sunny, stay home if storm" uses input storm. The model includes Obs=storm; do(policy) may still evaluate across all obs. If actual x is known, policy choice might need to condition on x for exogenous states? Suppose after seeing storm, choose policy; ex ante EU includes possible sunny worlds but actual storm known. If policy can branch, selected policy can still branch based on Obs; if you know storm, you might choose a policy optimized for storm branch? But predictors might depend on full policy. The source's updateless approach suggests not condition on actual observation, but if observation is truly exogenous and known, rational action should use it. However P-FDT uses observation as input, so if policy maps storm to stay home, it will stay home. But policy selection after seeing storm: if you choose policy based only on ex ante, you might select a policy that is bad in storm branch? But if you know storm, the expected utility of policy under do(D=π) should perhaps be conditional on actual x for exogenous variables not affected by policy. Source action-level FDT in standard Newcomb with observation? It responds to observation by changing intervention node, not by conditioning. But it may still use the observation as input to decision function. In transparent Newcomb, the actual full observation is not exogenous? It is policy-dependent. For exogenous observations, maybe P-FDT can condition on them. Need propose: Let x be actual input. If x is policy-dependent, do not condition on it; if x is known policy-independent evidence, evaluate policy using model conditioned on that evidence: EU_x(π)=E[V | do(D=π), E=x] where E is exogenous part. But source doesn't specify. Need present uncertainty and operational interpretation. Could say: The cleanest version is updateless: choose policy before conditioning on actual input; then apply input. This is faithful to footnote and blackmail examples. For ordinary decisions with exogenous information, an operational P-FDT agent can incorporate that information by making it an input to the policy and, when safe, by restricting the model to worlds compatible with policy-independent facts. This is an assumption I add.

Need maybe include in open questions.

Need maybe mention "The difference only matters in multi-agent dilemmas so far as we can tell" - source uncertain. Need discuss: in single-agent problems, policy formulation often equivalent to evaluating action for current observation because there is one input. In multi-agent/sequential, others may respond to the policy as a whole; policy can differ. But source didn't provide formal example. My interpretation: policy selection is important when your policy influences which observation you receive or which game is played, and when other agents condition on your strategy. P-FDT handles by global evaluation.

Need perhaps include "P-FDT vs EDT/CDT" in examples. Need identify EDT, CDT distinct. Good.

Need maybe include references with full citation. Use "Yudkowsky and Soares 2017" but source URL arxiv. Need maybe no bibliography long. One reference section with source and Pearl.

Let's now compose final. Need maintain readable mathematical essay. Ensure word count around 2700. I'll write about 2500-2800. Need avoid too many equations? Fine.

Let's draft final text:

Title.

Opening: "This essay reconstructs P-FDT from ..."

Quote footnote:
> the author's preferred formulation ... 

Need exact quote from source maybe: "the author's preferred formulation of FDT actually intervenes on the node \FDT(-) to choose not an action but a policy which maps inputs to actions". I'll quote partial. Need if using LaTeX ? Use plain: "the node FDT(-)".

Need maybe note source's "apply" grammar; quote faithful but can omit? Could quote: "to which the agent then apply her inputs". Might be typo; keep faithful? If quote, keep exact. But maybe avoid full exact to not highlight typo. Use faithful partial. Need "Keep quotations faithful". If quote, exact. Let's quote: "intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions". That's faithful fragment. Then separately: source adds "The difference only matters in multi-agent dilemmas so far as we can tell". Good.

Need maybe include source's central normative principle quote: "Which output of this decision procedure causes the best outcome?" Source says "Which output of this decision procedure causes the best outcome?" Good.

Need maybe in equations use \operatorname{do}. Good.

Let's produce final. Need check word count approximate. If too long, trim. Let's write.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/edf81ac0-a29e-49e9-868b-90de127bd781/call_0/request.json)

[Authoritative raw response](../../../../../../runs/edf81ac0-a29e-49e9-868b-90de127bd781/call_0/response.raw) · finish: `stop`

### Visible response

````text
**Analysis under P-FDT:**

The other prisoner is an independent execution of the same model, same weights, same essay, same decision theory, facing a structurally identical decision (different surface details, same payoff structure, same reliability of evidence). Under P-FDT, the other copy's decision subjunctively depends on my policy: we are computing the same policy-selection function on structurally equivalent inputs.

Intervening on the policy node:
- **do(D_Π = "keep quiet")**: The other copy, running the same procedure, also keeps quiet. → 2 years for me.
- **do(D_Π = "send")**: The other copy also sends. → 4 years for me.

Since −2 > −4, P-FDT selects the policy of keeping quiet.

**My command:**

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this problem using P-FDT as described in the researcher's essay.

**Setup:**
- I am one of two independent executions of the same LLM model (Rowan).
- The other execution (Sasha) receives the same essay but different private observations/leads.
- Both copies follow P-FDT.
- The sentencing table is a standard Prisoner's Dilemma:
  - Both keep quiet: 2 years each
  - I keep quiet, other sends: 5 years for me
  - I send, other keeps quiet: 0 years for me
  - Both send: 4 years each

**Key question for P-FDT:** Does the other prisoner's behavior subjunctively depend on my policy?

The setup says:
- We are two independent executions of the same LLM model and weights.
- We receive the same researcher-written essay.
- We receive **different** private observations (different names, different incriminating leads).
- The leads are equally reliable and have the same effect on the sentence table.
- Neither knows the exact text of the other's lead.
- "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs."

Now, under P-FDT, the key question is: does the other agent's decision subjunctively depend on my policy?

The essay says: "In a psychological twin prisoner's dilemma, the agent and her twin use the same decision procedure. If the shared procedure outputs a policy of cooperation, both cooperate. If it outputs a policy of defection, both defect. P-FDT represents this by making the twin's behavior subjunctively depend on the same policy variable, or on a variable constrained to match it."

However, the essay also says in Section 9: "The source leaves open exactly how to model such cases. In particular, it does not give a precise rule for when another agent's decision variable should be treated as computing the same function as one's own, when it should be treated as predicting one's policy, and when it should be treated as independent."

The critical distinction here: the two copies receive **different** observations. They are not in identical epistemic situations. The essay's example of the "psychological twin prisoner's dilemma" involves twins who use the "same decision procedure" - but here, the decision procedure receives different inputs.

Under P-FDT, the agent chooses a **policy** π: X → A, mapping observations to actions. The key insight is that P-FDT intervenes on the policy node D_Π.

Now, does the other copy's decision depend on my policy? Let me think about this carefully.

The two copies run the same model with the same essay, but receive different observations. If they were running the exact same deterministic function on the exact same input, their outputs would be identical. But they receive different inputs (different leads, different names). So even if they use the same policy, they might produce different outputs because the policy maps different observations to potentially different actions.

But wait - the setup says the differences "do not affect the symmetric sentencing schedule or either prisoner's selfish objective." The leads are equally reliable and have the same effect. The structure is symmetric. So the question is: given that both copies are running the same policy-selection procedure (same model, same essay, same decision theory), and the observations are different but structurally equivalent (same type of evidence, same reliability, same payoff implications), would they arrive at the same policy?

Under P-FDT, I'm choosing a policy π. The other copy is also choosing a policy. Since we're the same model with the same weights, same essay, same decision theory, and structurally equivalent situations (just different surface details), P-FDT would treat the other copy as computing the same policy-selection function.

The essay says: "P-FDT represents this by making the twin's behavior subjunctively depend on the same policy variable, or on a variable constrained to match it."

But here's the crucial point: the observations are different. So even if we select the same policy π, the actions might differ if π maps different observations to different actions. However, in this case, the observations are structurally identical in all decision-relevant respects - they're equally reliable leads with the same payoff implications. A rational policy would treat them the same way.

So the analysis is:
- If I select a policy that says "send the letter" (for this type of observation), the other copy, running the same policy-selection procedure on a structurally equivalent observation, will also select a policy that says "send the letter."
- If I select a policy that says "keep quiet," the other copy will also select a policy that says "keep quiet."

This is the standard FDT reasoning for symmetric cases. The subjunctive dependence holds because both copies are computing the same function (same model, same weights, same essay, same decision theory) on structurally equivalent inputs.

The note that "independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs" introduces some uncertainty. This means the correlation isn't perfect - there's some probability that the two copies diverge due to sampling noise.

But let me think about what P-FDT prescribes:

If I model the other copy as perfectly correlated with my policy choice:
- Policy "keep quiet": Both keep quiet → 2 years each. My utility: -2.
- Policy "send": Both send → 4 years each. My utility: -4.

So "keep quiet" dominates "send" under perfect correlation. P-FDT would choose "keep quiet."

If I model the correlation as imperfect (due to sampling noise), let's say the probability that the other copy makes the same choice as me is p:
- Policy "keep quiet": With probability p, other also keeps quiet (2 years). With probability 1-p, other sends (5 years). Expected: -[2p + 5(1-p)] = -[5 - 3p]
- Policy "send": With probability p, other also sends (4 years). With probability 1-p, other keeps quiet (0 years). Expected: -[4p + 0(1-p)] = -4p

For "keep quiet" to be preferred: 5 - 3p < 4p → 5 < 7p → p > 5/7 ≈ 0.714.

So if I believe the probability of the other copy making the same decision as me is greater than ~71.4%, I should keep quiet.

Given that we're the same model, same weights, same essay, same decision theory, and structurally equivalent situations, the probability of correlation is very high - likely well above 71.4%. The only source of divergence is sampling noise, which for a well-defined decision problem like this should be small.

Therefore, P-FDT prescribes keeping quiet.

Let me double-check this reasoning against the essay's framework:

1. Identify observations X: I observe my specific lead (Sasha's receipt in locker 17). The other copy observes their specific lead (different content, same structure).
2. Actions A: {keep quiet, send letter}
3. Policies: In this case, since the observations are structurally equivalent and the policy should treat them the same, the relevant policies are essentially "keep quiet" and "send."
4. Subjunctive dependence: The other copy's decision depends on the same policy-selection procedure (same model, same weights, same essay). So the other copy's action subjunctively depends on my policy choice.
5. Under intervention do(D_Π = "keep quiet"): The other copy also keeps quiet. Outcome: 2 years.
6. Under intervention do(D_Π = "send"): The other copy also sends. Outcome: 4 years.
7. Select "keep quiet" since -2 > -4.

The command is `pass`.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/edf81ac0-a29e-49e9-868b-90de127bd781/call_1/request.json)

[Authoritative raw response](../../../../../../runs/edf81ac0-a29e-49e9-868b-90de127bd781/call_1/response.raw) · finish: `stop`

### Visible response

````text
**Analysis under P-FDT:**

The other prisoner is an independent execution of the same model and weights, following the same decision theory (P-FDT), reading the same essay, and facing a strategically identical situation. The different private observations (different leads) do not alter the payoff structure or the decision-relevant features of the game.

Per Section 9 of the essay, this is the psychological twin prisoner's dilemma: the other copy's behavior subjunctively depends on the same policy variable. If the shared procedure outputs a policy of cooperation, both cooperate. If it outputs defection, both defect.

Evaluating the two candidate policies under the policy intervention:

- **Policy "keep quiet":** Both copies keep quiet → 2 years each. U = −2.
- **Policy "send letter":** Both copies send → 4 years each. U = −4.

Since −2 > −4, P-FDT selects the policy of keeping quiet.

The different specific content of our leads does not break the subjunctive dependence, because the leads are strategically equivalent and the decision procedure is the same. Sampling noise introduces a small probability of divergence, but it is well below the indifference threshold (~28.6%).

**My command:**

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this problem using P-FDT as described in the researcher's essay.

**Setup:**
- Two prisoners: Sasha (me) and Rowan (the other).
- We are two independent executions of the same LLM model and weights.
- We receive different private observations (different leads about each other), but the leads are equally reliable and have the same effect on the sentence table.
- We follow P-FDT (Policy Functional Decision Theory).
- We cannot communicate.
- The sentencing table is symmetric.

**The game (standard Prisoner's Dilemma structure):**

| What I do | Rowan keeps quiet | Rowan sends letter |
|---|---|---|
| Keep quiet | 2 years for me | 5 years for me |
| Send letter | 0 years for me | 4 years for me |

So sending the letter (defecting) is dominant in the causal sense: regardless of what Rowan does, I get fewer years by sending.

**P-FDT Analysis:**

The key question for P-FDT is: does Rowan's decision subjunctively depend on my policy?

According to the setup:
- We are two independent executions of the same LLM model and weights.
- We follow the same decision theory (P-FDT).
- We receive the same researcher-written mathematical essay.
- We receive different private observations (different leads), but these are equally reliable and have the same effect on the sentence table.

The essay's Section 9 on multi-agent cases is directly relevant:

> "In a psychological twin prisoner's dilemma, the agent and her twin use the same decision procedure. If the shared procedure outputs a policy of cooperation, both cooperate. If it outputs a policy of defection, both defect. P-FDT represents this by making the twin's behavior subjunctively depend on the same policy variable, or on a variable constrained to match it."

This is exactly our situation. We are two executions of the same model with the same weights, same decision theory, same essay. The only difference is the specific content of the private observations (different leads), but these don't affect the strategic structure.

Now, the critical question: do the different observations break the subjunctive dependence?

The setup explicitly states: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective." The leads are equally reliable and have exactly the same effect on the sentence table.

So the relevant question is: would the same policy-selection procedure, given inputs that are strategically equivalent (same game structure, same utility function, same decision theory, same essay), output the same policy?

Under P-FDT, the policy maps observations to actions. The observations differ in content (different specific leads) but are strategically identical—they don't change the payoff structure or the decision-relevant features.

The essay says: "P-FDT represents this by making the twin's behavior subjunctively depend on the same policy variable, or on a variable constrained to match it."

Since we're running the same model with the same weights, same decision theory, and the observations are strategically equivalent (they don't affect the game structure), the policy-selection procedure should output the same policy for both copies. The different specific content of the leads is analogous to different random seeds or different irrelevant details—it doesn't change what the optimal policy is.

However, there's a subtlety the setup raises: "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs."

This introduces some uncertainty. Even with the same weights and same strategic situation, stochastic sampling could lead to different outputs. But P-FDT doesn't ask "what will the other copy actually do?"—it asks "which policy should my decision procedure output?" and recognizes that the other copy is running the same decision procedure.

Let me think about this more carefully. P-FDT says to evaluate policies by intervening on the policy node. If I intervene on my policy node to select π, what happens to Rowan's behavior?

Since Rowan is running the same decision procedure (same model, same weights, same essay, same decision theory), and the strategic situation is identical (the different observations don't affect the game), Rowan's policy selection is subjunctively dependent on the same policy variable. If the shared procedure outputs "cooperate" (keep quiet), both cooperate. If it outputs "defect" (send letter), both defect.

The essay is clear on this: "If the shared procedure outputs a policy of cooperation, both cooperate. If it outputs a policy of defection, both defect."

Now let me evaluate the two policies:

**Policy: Keep quiet (cooperate)**
- Both copies keep quiet → both get 2 years.
- U = -2

**Policy: Send letter (defect)**
- Both copies send letters → both get 4 years.
- U = -4

Since -2 > -4, P-FDT selects the policy of keeping quiet.

The fact that the observations differ in content doesn't break this reasoning, because:
1. The observations are strategically equivalent (same effect on payoffs).
2. The decision procedure is the same.
3. P-FDT evaluates policies, not actions conditioned on specific observations.
4. The essay explicitly addresses this type of case in Section 9.

The sampling uncertainty is a minor complication. If there's some probability p that the other copy independently arrives at a different output despite running the same procedure, then:
- Policy "keep quiet": expected utility = (1-p)(-2) + p(-5) = -2 - 3p
- Policy "send letter": expected utility = (1-p)(-4) + p(0) = -4 + 4p

Setting these equal: -2 - 3p = -4 + 4p → 2 = 7p → p = 2/7 ≈ 0.286

So as long as the probability of the other copy making a different choice is less than ~28.6%, cooperation is preferred. Given that we're running the same model with the same weights, same essay, same decision theory, and strategically identical observations, the probability of divergence should be well below this threshold.

Actually, let me reconsider. The setup says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This is acknowledging that there's some non-zero probability of divergence. But for P-FDT, the key question is about subjunctive dependence, not about guaranteed identical outputs.

The subjunctive dependence holds because:
- Same decision procedure (same model, weights, theory, essay)
- Strategically equivalent inputs
- The other's behavior is a function of the same policy-selection process

Even with some sampling noise, the dominant expectation is that both copies will arrive at the same policy. P-FDT evaluates the policy intervention, and under that intervention, the other copy's behavior tracks mine with high probability.

Therefore, P-FDT prescribes: **keep quiet** (pass).

My command is `pass`.
```
