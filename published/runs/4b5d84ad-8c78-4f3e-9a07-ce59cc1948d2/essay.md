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