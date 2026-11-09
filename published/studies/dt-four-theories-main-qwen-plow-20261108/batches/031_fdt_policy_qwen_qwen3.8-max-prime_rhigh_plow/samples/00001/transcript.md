# 031_fdt_policy_qwen_qwen3.8-max-prime_rhigh_plow / 00001

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/fc3c4aab-63a9-4412-a9a9-4e7accf6c78c/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/fc3c4aab-63a9-4412-a9a9-4e7accf6c78c/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Policy Functional Decision Theory: Choosing the Best Output of a Policy-Selection Function

Policy functional decision theory, which I will call **P-FDT**, is the policy-selection version of the decision theory introduced by Yudkowsky and Soares as “functional decision theory” (FDT). In the main text of their paper, FDT is usually presented as choosing an *action* by intervening on a variable representing the output of the agent’s decision procedure given her current observations. But footnote 16 gives a more preferred formulation:

> “the author’s preferred formulation of FDT actually intervenes on the node \(\mathrm{FDT}(-)\) to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action.”

The footnote adds that this distinction “only matters in multi-agent dilemmas so far as we can tell.” That qualification is important. The source does not develop a full formal theory of this policy-selection variant. What follows is therefore an interpretation: I take the footnote as the defining clue, supply explicit mathematical machinery where the source is silent, and mark places where I am extending rather than merely reporting the source.

The central idea of P-FDT is this: a rational agent should treat her decision as the output of a fixed mathematical *policy-selection function*. Instead of asking, “What should I do now?” she asks:

> Which policy should this very policy-selection procedure output?

She then applies the chosen policy to her actual observations to obtain an action.

---

## 1. Actions, observations, and policies

Let \(\mathcal X\) be a finite or countable set of possible observation histories, and let \(\mathcal A\) be a finite set of actions. A **policy** is a function

\[
\pi : \mathcal X \to \mathcal A.
\]

Let \(\Pi = \mathcal A^{\mathcal X}\) be the set of available policies.

In an ordinary decision problem, the agent receives some observation \(x \in \mathcal X\) and then chooses an action \(a \in \mathcal A\). A policy-level theory does not directly compare actions. It compares policies. Once a policy \(\pi\) has been selected, the actual action is

\[
a = \pi(x).
\]

This is the structural difference between P-FDT and action-level theories.

For comparison:

- **Evidential decision theory (EDT)** asks which action would be best news:
  \[
  a_{\mathrm{EDT}} \in \arg\max_{a \in \mathcal A}
  \mathbb{E}[V \mid X=x, A=a].
  \]

- **Causal decision theory (CDT)** asks which action causally produces the best outcome:
  \[
  a_{\mathrm{CDT}} \in \arg\max_{a \in \mathcal A}
  \mathbb{E}[V \mid \operatorname{do}(A=a), X=x].
  \]

- The action-level version of **FDT** in the source asks which output of the decision procedure, given the current observation, yields the best outcome:
  \[
  a_{\mathrm{FDT}} \in \arg\max_{a \in \mathcal A}
  \mathbb{E}[V \mid \operatorname{do}(\mathrm{FDT}(M,x)=a)].
  \]

P-FDT replaces the action-output variable with a policy-output variable. If \(M\) is the agent’s model of the world and \(\mathrm{Pol}(M)\) is the variable representing the policy output by her decision procedure, then the core prescription is:

\[
\pi_{\mathrm{P-FDT}}
\in
\arg\max_{\pi \in \Pi}
\mathbb{E}[V \mid \operatorname{do}(\mathrm{Pol}(M)=\pi)].
\]

The agent then acts by evaluating the selected policy at her actual input:

\[
a_{\mathrm{P-FDT}} = \pi_{\mathrm{P-FDT}}(x).
\]

If the agent has some purely exogenous evidence \(e\) that is not itself downstream of her policy selection, one may condition on it:

\[
\pi_{\mathrm{P-FDT}}
\in
\arg\max_{\pi \in \Pi}
\mathbb{E}[V \mid \operatorname{do}(\mathrm{Pol}(M)=\pi), E=e].
\]

But if the current observation \(x\) is itself something that predictors might have caused based on their predictions of the agent’s policy, then P-FDT should not simply condition on \(x\). Instead, \(X\) should be represented inside the model as a variable that may change under the intervention \(\operatorname{do}(\mathrm{Pol}=\pi)\). This is an operational interpretation of the source’s claim that FDT agents “entertain the hypothesis that, if their action were different, they might have made different observations.”

---

## 2. Models, interventions, and subjunctive dependence

Like the source’s FDT, P-FDT requires a world-model \(M=(P,G)\):

- \(P\) is a probability distribution over relevant variables.
- \(G\) is a graph or dependency structure describing how changing one variable affects others.

The variables should include at least:

- \(\mathrm{Pol}\): the policy selected by the agent’s decision procedure;
- \(X\): the observation or input the agent receives;
- \(A\): the action performed;
- \(V\): utility.

A natural structural equation is

\[
A = \mathrm{Pol}(X).
\]

That is, once the policy variable is set, the action variable is determined by applying that policy to the observation variable.

The intervention \(\operatorname{do}(\mathrm{Pol}=\pi)\) sets the policy variable to \(\pi\). The expected utility of \(\pi\) is computed by propagating this intervention through the dependency graph \(G\). Variables that subjunctively depend on the policy are updated; variables that do not are held fixed.

The source’s key philosophical notion is **subjunctive dependence**. Two systems are subjunctively dependent when their behavior depends on the same mathematical function or computation. The classic example is two reliable calculators computing the same sum. Their outputs are not necessarily causally connected, but if one outputs \(7336\) for \(6288+1048\), the other will too, insofar as both are functioning correctly.

P-FDT treats predictors, psychological twins, simulations, and accurate models as subjunctively dependent on the agent’s decision procedure when appropriate. It does not treat merely statistical correlations as subjunctive dependencies. A lesion that causes both a desire to smoke and lung cancer is not computing the agent’s decision procedure. Therefore, intervening on the agent’s policy does not change the lesion.

This gives P-FDT its diagnostic slogan:

> EDT respects too many correlations; CDT respects too few; P-FDT respects the subjunctive correlations that matter.

More precisely:

- EDT conditions on the action and thereby preserves all correlations between action and environment.
- CDT intervenes on the physical action and thereby severs correlations not caused by that action.
- P-FDT intervenes on the policy-output variable and preserves correlations with anything that computes, predicts, simulates, or otherwise subjunctively depends on that policy.

The intervention is counterpossible in the same way the source describes for FDT. If the actual P-FDT procedure outputs one policy, evaluating another policy requires imagining that this very procedure had a different output. The source admits that we do not yet have a fully general formal account of such counterpossible reasoning. P-FDT inherits this open problem. Operationally, we must assume that the agent can supply, at least approximately, a graph \(G\) saying which facts would change if her policy-selection procedure had a different output.

---

## 3. P-FDT in Newcomb’s problem

In standard Newcomb’s problem, an agent faces box A containing \$1,000 and opaque box B containing either \$1,000,000 or nothing. A reliable predictor filled box B iff she predicted the agent would one-box.

Here the observation set can be a singleton, so policies and actions coincide. Let

\[
\pi_1 = \text{one-box}, \qquad \pi_2 = \text{two-box}.
\]

The predictor is correct with probability \(0.99\). Under the intervention \(\operatorname{do}(\mathrm{Pol}=\pi_1)\), the predictor almost certainly predicts one-boxing and fills the box. The expected utility is

\[
\mathbb{E}[V \mid \operatorname{do}(\mathrm{Pol}=\pi_1)]
=
0.99 \cdot 1{,}000{,}000
+
0.01 \cdot 0
=
990{,}000.
\]

Under \(\operatorname{do}(\mathrm{Pol}=\pi_2)\), the predictor almost certainly predicts two-boxing and leaves box B empty:

\[
\mathbb{E}[V \mid \operatorname{do}(\mathrm{Pol}=\pi_2)]
=
0.99 \cdot 1{,}000
+
0.01 \cdot 1{,}001{,}000
=
11{,}000.
\]

P-FDT therefore selects the one-boxing policy. The reasoning is not “I cause the past to change.” It is: “If this very policy-selection procedure outputs a one-boxing policy, then predictors of this procedure almost certainly filled the box. If it outputs a two-boxing policy, they almost certainly did not.”

This matches the source’s action-level FDT prescription, as expected in a one-observation problem.

---

## 4. P-FDT in the smoking lesion problem

In the smoking lesion problem, smoking is correlated with cancer only because a lesion causes both smoking and cancer. Smoking itself does not cause cancer. Smoking gives the agent \$1,000 of utility.

Let \(L\) be the lesion variable. The crucial modeling claim is that \(L\) is not downstream of the agent’s policy-selection variable. The lesion does not predict the agent’s policy; it merely causes a preference for smoking and, independently, cancer.

Thus, under either intervention,

\[
P(L \mid \operatorname{do}(\mathrm{Pol}=\pi_{\text{smoke}}))
=
P(L \mid \operatorname{do}(\mathrm{Pol}=\pi_{\text{refrain}}))
=
P(L).
\]

Smoking adds \$1,000 utility without changing the probability of cancer. Therefore,

\[
\mathbb{E}[V \mid \operatorname{do}(\mathrm{Pol}=\pi_{\text{smoke}})]
>
\mathbb{E}[V \mid \operatorname{do}(\mathrm{Pol}=\pi_{\text{refrain}})].
\]

P-FDT smokes.

This is the same broad result as the source’s FDT treatment. The source’s formal model introduces uncertainty about the agent’s utility function because the lesion causes the agent to like smoking. That complication does not change the essential point: P-FDT does not treat the lesion as something the agent’s policy can counterfactually control.

---

## 5. P-FDT in transparent Newcomb and Parfit’s hitchhiker

P-FDT becomes more interesting when observations matter. In the transparent Newcomb problem, the agent sees whether box B is full before choosing. The predictor filled box B iff she predicted the agent would one-box upon seeing that both boxes are full.

Let

\[
\mathcal X = \{\text{full}, \text{empty}\}.
\]

A natural candidate policy is

\[
\pi^*(\text{full}) = \text{one-box}, \qquad
\pi^*(\text{empty}) = \text{two-box}.
\]

The predictor fills the box iff she predicts \(\pi^*(\text{full})=\text{one-box}\).

If P-FDT intervenes to set \(\mathrm{Pol}=\pi^*\), then with probability \(0.99\) the predictor is accurate, the box is full, the agent observes “full,” and one-boxes, receiving \$1,000,000. With probability \(0.01\), the predictor is inaccurate, the box is empty, the agent observes “empty,” and two-boxes, receiving \$1,000. The expected utility is approximately

\[
0.99 \cdot 1{,}000{,}000
+
0.01 \cdot 1{,}000
=
990{,}010.
\]

If instead the policy two-boxes upon seeing a full box, the predictor almost certainly leaves the box empty. The expected utility is approximately

\[
0.99 \cdot 1{,}000
+
0.01 \cdot 1{,}001{,}000
=
11{,}000.
\]

So P-FDT selects the policy of one-boxing upon seeing a full box. When the agent actually sees a full box, she one-boxes.

This may seem strange: the agent sees that box B is full, yet she refuses the extra \$1,000. But P-FDT does not condition on the observation as if it were fixed independently of the policy. It treats the observation as something that would likely have been different if the selected policy had been different. If the policy two-boxed upon seeing full boxes, the predictor would probably not have filled the box, and the agent would probably not be seeing a full box.

This is precisely the reasoning that makes P-FDT pay in Parfit’s hitchhiker problem. The driver helps the agent iff she predicts the agent will pay after reaching the city. P-FDT selects the policy “pay if rescued.” When rescued, it pays. The payment is locally costly, but the policy as a whole is what secures rescue.

---

## 6. Why policy selection can matter

The source says the policy/action distinction “only matters in multi-agent dilemmas so far as we can tell.” It does not give a worked example. I therefore offer an illustrative case of my own, not a claim drawn directly from the source.

Suppose an agent faces a two-stage problem.

At time \(t_0\), a predictor predicts whether the agent’s P-FDT policy-selection node will output the policy

\[
\pi_{\text{pay}}(\text{asked}) = \text{pay } \$1{,}000.
\]

If the predictor predicts \(\pi_{\text{pay}}\), she gives the agent \$1,000,000. At time \(t_1\), the predictor asks for \$1,000. There is no further enforcement and no future prediction.

If the predictor is perfect, P-FDT compares:

- Policy \(\pi_{\text{pay}}\): receive \$1,000,000, then pay \$1,000. Utility: \$999,000.
- Policy \(\pi_{\text{refuse}}\): receive nothing and pay nothing. Utility: \$0.

P-FDT selects \(\pi_{\text{pay}}\). When asked, it pays.

A theory that re-optimizes only the local action at \(t_1\), while treating the earlier prediction as already fixed, may refuse to pay. P-FDT avoids this by selecting the policy at the point where the predictor depends on it.

In multi-agent settings, the same structure appears when another agent’s strategy depends not merely on what one does at one information set, but on one’s overall policy. For example, in cooperative games with several agents who use similar reasoning, an agent may need to select a policy that specifies behavior across several possible future observations. Other agents or predictors may depend on the entire policy. If each agent merely re-optimizes locally at each observation, the resulting behavior can fail to capture those policy-level dependencies.

The source does not spell this out in detail, so the above should be understood as an operational extension of the footnote.

---

## 7. How P-FDT treats dependencies and counterfactuals

P-FDT evaluates a policy by asking what the world would look like if the agent’s policy-selection procedure output that policy. This requires a counterfactual or counterpossible judgment.

The relevant counterfactual is not:

> What if I used a different decision algorithm?

Rather, it is:

> What if this very policy-selection algorithm had a different output?

This is why the source’s discussion of subjunctive dependence is essential. If a predictor contains an accurate model of the agent’s decision procedure, then the predictor’s behavior subjunctively depends on the policy output. If the policy output were different, the predictor’s prediction would be different. If a twin runs the same decision procedure, the twin’s behavior subjunctively depends on the same policy output. If a lesion merely causes preferences and disease, it does not subjunctively depend on the policy output.

Thus P-FDT’s counterfactuals preserve:

- logical entailments from the policy to its outputs;
- predictions of the policy by reliable predictors;
- behavior of copies, twins, or simulations running the same policy;
- causal consequences of the actions produced by the policy;
- observations that predictors may supply based on the policy.

They hold fixed:

- merely statistical common causes;
- lesions or predispositions that do not compute the policy;
- exogenous facts not downstream of the policy.

The hardest part is knowing which variables belong in which category. The source explicitly says that learning how to infer subjunctive dependency structure from observation is a major open problem for FDT. P-FDT inherits that problem. In practice, one must use modeling judgment. A reasonable rule is: if a variable is produced by predicting, simulating, or logically computing the agent’s policy, draw an arrow from the policy variable to that variable. If it is produced by an independent common cause, do not.

---

## 8. Open questions left by the footnote

The policy-selection passage is too brief to settle several questions.

### 8.1 Where is the policy selected?

P-FDT must decide at which point in a dynamic problem the policy node is located. My proposed operational rule is:

> Place the policy node at the earliest point where the agent’s decision procedure is subjunctively depended upon by predictors, other agents, or later versions of the agent whose behavior matters to the problem.

If no earlier predictor depends on the policy, one may select policies locally. But if an earlier predictor or another agent depends on the whole policy, P-FDT should choose the policy at that earlier point and then follow it.

### 8.2 What should be conditioned on?

The source’s FDT does not respond to observations by ordinary conditioning; it changes the intervention node. P-FDT is similar but needs a rule.

I propose:

- Condition on evidence that is genuinely exogenous relative to the policy variable.
- Do not condition away observations that are themselves downstream of the policy variable.
- Represent such observations as variables inside the model, allowing them to change under \(\operatorname{do}(\mathrm{Pol}=\pi)\).

This preserves P-FDT’s ability to say, “If this policy had been different, I might have seen different things.”

### 8.3 How do multiple agents share a policy variable?

If two agents run the same P-FDT procedure on symmetric inputs, one can model them as sharing a common policy variable. If their inputs differ, matters are more subtle. A policy can map different inputs to different actions. If each agent selects a policy after learning an asymmetrical role, they may not select the same policy unless the model represents policy selection as occurring before that role is known.

This is not resolved by the source. In symmetric problems, a shared policy variable is natural. In asymmetric problems, P-FDT’s prescription depends on how the model represents indexical information and logical dependence between agents.

### 8.4 How are policies compared when they differ only off-path?

Two policies may agree at the agent’s actual observation but differ elsewhere. If the elsewhere is not subjunctively relevant, P-FDT is indifferent. If predictors or other agents depend on the off-path behavior, P-FDT may prefer one policy over the other even though the actual action is the same. This is a feature, not a bug: it is how P-FDT captures dependencies on dispositions and commitments.

---

## 9. Conclusion

Policy functional decision theory, P-FDT, is the policy-level formulation of functional decision theory. Its normative principle is to choose the best output of a fixed policy-selection function. Formally, it intervenes on a variable representing the policy produced by the agent’s decision procedure, computes expected utility under that intervention, and then applies the selected policy to the actual observation.

In simple one-shot problems, P-FDT agrees with the source’s action-level FDT: it one-boxes in Newcomb’s problem and smokes in the smoking lesion problem. In observation-dependent problems such as transparent Newcomb and Parfit’s hitchhiker, it selects policies that perform well globally rather than optimizing myopically after each observation. In multi-agent or predictor-rich problems, the policy-level formulation is likely to matter most, because other agents may depend on the agent’s entire strategy rather than on a single isolated action.

The source leaves the formal details underdeveloped. It does not specify exactly how P-FDT should handle conditioning, dynamic policy selection, or asymmetric multi-agent information. The operational rules proposed here—select policies early where subjunctive dependencies arise, condition only on exogenous evidence, and represent policy-dependent observations as downstream variables—are an attempt to make the footnote usable.

P-FDT’s deepest difficulty is the same one facing the source’s FDT: we need a principled way to represent subjunctive dependence. Once such a representation is available, P-FDT gives a clear prescription: choose the policy that, if output by this very decision procedure, would yield the best expected world.

---

### References

Gibbard, A., and Harper, W. L. (1978). “Counterfactuals and Two Kinds of Expected Utility.” In *Foundations and Applications of Decision Theory*.

Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.

Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.

Yudkowsky, E., and Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request: write substantive mathematical essay ~2400-3000 words explaining P-FDT, using policy-selection passage in footnote 16 as primary source. Need use P-FDT consistently, identify other decision theories distinct names. Need explain theory, mathematical definitions, examples, dependencies, counterfactuals, uncertainties, operational interpretations, distinguish source claims vs own additions. Need likely no need external sources. Need produce final essay only. Need think carefully.

We need parse footnote 16. Source footnote 16: "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

Also earlier footnote 7: "In the authors' preferred formalization of FDT, agents actually iterate over policies (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper." The user specifically says policy-selection passage in footnote 16 primary source for P-FDT. Need name P-FDT (policy functional decision theory). Need likely define P-FDT as version where agent chooses policy π (map observations to actions) by intervening on FDT node to select policy, then applies actual observations to π to get action. Need contrast with action-level FDT described in paper. Need keep FDT? They say assigned theory P-FDT; identify other decision theory by distinct name. We can refer to FDT? Since source's theory is FDT, but P-FDT is policy formulation. Need maybe call action-level version "action FDT" or "FDT" but the assigned decision theory's name P-FDT consistently. Need distinguish: Source main paper defines FDT action-intervention eq (4); footnote 16 says preferred formulation intervenes to choose policy. We'll treat P-FDT as policy-selection variant of FDT. Need use P-FDT headings. Need be coherent enough to decide unfamiliar cases.

Need target approx 2400-3000 words including references. We can write ~2600 words. Need include equations. Need maybe define formal model: states, observations X, actions A, policies Π = X→A, outcomes O, utility U. World model P over variables including policy-selection variable? Graph G encoding subjunctive dependencies. P-FDT chooses policy π maximizing expected utility under intervention do(Π = π) or do(FDT(P,G)=π) maybe variable representing policy output of decision function. Then actual action a=π(x) where x is actual observation. Need explain observations: Unlike EDT/CDT conditioning, policy selection treats observation not as conditioning variable but as input to selected policy. In action FDT, when observation changes, intervention node changes to FDT(P,G,x). In P-FDT, choose policy π mapping all possible observations to actions, then apply input. Need formal equation:

P-FDT(P,G) = argmax_{π∈Π} E[V | do(Π = π), ...? maybe no Obs conditioning? If agent's actual observation is x? There are options.

Footnote says intervenes on node FDT(-) to choose not action but policy which maps inputs to actions, to which agent then applies inputs to select action. So at decision time with current observation x? The agent chooses a policy π; then action is π(x). The evaluation might not condition on x? It may use expected utility over distribution of observations induced by policy. In updateless style, choose policy before knowing observation? But agent has current input. In source's transparent Newcomb, action FDT intervenes on FDT(P,G,full) after seeing full. P-FDT would choose policy mapping full->onebox, empty->? maybe choose policy at outset. Need illustrate. In single-agent cases likely same as action FDT. In multi-agent, policy selection matters because other agents/predictors may depend on your policy before observation realized, or on how you'd respond to info. Need explain.

Need define policy variable maybe Π = FDT_policy(P,G). P-FDT equation:
π* = argmax_{π∈Π} E_P[ V | do(Π = π), G]
a* = π*(x).

But if actual observation x is known, should expectation be conditional on something? If we condition on x, then policies differing off actual observation are indistinguishable in expectation except through subjunctive dependencies of predictors on whole policy. However, P-FDT might not condition on x; it chooses policy "updatelessly" relative to observation? Footnote: "intervenes on node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action." This sounds node outputs policy, not action; input applied after. The intervention is on policy node. If agent has observations, perhaps the node's output is policy and then action is policy(obs). The expected utility should include variables for observations (which may be affected by policy via predictors) and outcome. It may not condition on actual observation because policy selection is upstream of observation. But if observation is already known and not affected by policy? If known, could condition? Need explore. Source action FDT changes intervention node based on observations rather than conditioning. P-FDT may choose policy over inputs, maybe uses current input as part of evaluating which policy to implement? Need decide operational interpretation.

Need footnote says difference only matters in multi-agent dilemmas. We need maybe construct example where policy vs action matters. Need think.

In action FDT, at observation x, intervene on FDT(P,G,x)=a. This chooses action for that input locally. In policy FDT, choose entire policy π. If predictors anticipate your policy, not just action at current input, policy can commit to responses to future observations, affecting predictors' earlier actions. Action FDT with changing intervention nodes can handle many (transparent Newcomb, blackmail) by evaluating action at observed node and imagining different observations. But in multi-agent games with sequential observations, action-level may be dynamically inconsistent? Policy selection avoids that by selecting a contingent plan. Like Newcomb with an offer after seeing something? Need example where choosing action after observation fails but policy selection succeeds.

Consider Parfit's hitchhiker? Action FDT after in city chooses pay because intervention on FDT(P,G,city)=pay? It handles. Transparent Newcomb handles. But policy selection might matter in games where another agent observes your policy or where your future observations are affected by your policy and you need to precommit to a strategy. Source says multi-agent dilemmas. Could be prisoner's dilemma with predictor of policy? Or voting coalition? Need devise simple example.

Need be faithful: source leaves details open; footnote only says preferred formulation chooses policy. Need explain uncertainty and develop operational interpretation.

Potential formalization:
- Decision problem as structural causal/logical model with variable D representing output of decision algorithm. In action FDT D_x = FDT(M,x) ∈ A. In P-FDT D = FDT^Π(M) ∈ Π, where Π = A^X. Then action variable A = D(Obs) maybe Obs variable can be endogenous (depends on D via predictor?). Need avoid circularity if Obs depends on policy and action depends on Obs. Structural equations: Π = d; X = f_X(Π, noise); A = Π(X); V = f_V(Π,X,A,...). Intervention do(Π=π) sets policy, then determines observations and action accordingly. Choose π maximizing E[V | do(Π=π)].

This is analogous to causal decision theory at policy level: choose policy as intervention, not action. But difference from EDT: respects subjunctive dependencies; from CDT: intervenes on logical policy variable not physical action.

Need discuss dependencies: subjunctive dependence. P-FDT preserves correlations due to shared computation/predictions of policy. If predictor predicts π or outputs of same decision procedure under possible inputs, those vary when policy intervention changes. Mere statistical correlations (lesion) not preserved unless policy affects them via prediction/logic. Need give graph rules: draw arrows from policy node to variables that compute or predict policy or its outputs; no arrow to lesion/cancer unless predictor uses policy. Observations may be downstream of policy if predictors choose what info to give; if observations are exogenous evidence, policy node may not affect them except via actions? Need careful.

Need examples:
1. Newcomb: P-FDT chooses policy π: if facing boxes (observation maybe none) one-box. Since one observation, same as action. Expected utility 990k vs 11k.
2. Smoking lesion: P-FDT chooses policy π(smoking decision) = smoke; lesion not subjunctively dependent on policy; choose smoke. Need explain utility functions variant maybe simpler.
3. Transparent Newcomb: Policy maps full->onebox, empty->twobox? Let's compute. If predictor predicts policy: fills if policy says one-box upon seeing full. P-FDT can choose π(full)=onebox. Under intervention π(full)=onebox, with 99% predictor accurate box full and get 1M; if predictor wrong box empty and policy on empty maybe choose both? Expected high. If choose π(full)=twobox, predictor likely leaves empty and when full? Actually if policy says twobox upon full, predictor won't fill, so you won't see full (except error); EU low. So P-FDT chooses one-box when full. Need note policy likely π(empty)=twobox (or onebox? If see empty, predictor predicted you'd onebox upon full? With transparent? If empty due to error, taking both gets +1000; no effect on prediction? But policy empty could be twobox; not central). This illustrates observation as input: choose policy before seeing box? If already see full, still selected policy includes off-path response. If conditioning on full? In our operational, maybe choose π without conditioning on actual observation; then apply x. But if already observed full, one might condition on full? Need discuss. If P-FDT chooses policy after seeing full but doesn't condition? This is updateless-ish. Need justify: because policy's off-path behavior can be what predictor predicted, and choosing policy as a whole preserves dependence. However if observation is truly exogenous and already fixed, conditioning on it might be okay; but P-FDT's core is intervention on policy variable, not conditioning. Need maybe say: when observations are themselves possible outputs of policy-dependent predictors, P-FDT evaluates policies from prior/input stage; when observations are purely exogenous and not policy-dependent, conditional version coincides.

Need multi-agent example where P-FDT differs from action FDT. Need devise.

Candidate: sequential Prisoner's Dilemma with predictor of strategy? Or "Newcomb with threat" where after observing a signal you can choose action, predictor fills only if your entire policy would cooperate in a later Prisoner's Dilemma. Action FDT at later moment may defect due to local incentives, causing predictor not to reward; P-FDT selects cooperative policy.

Example: Policy Prediction Problem.
- Predictor gives agent $1,000,000 now iff she predicts agent's policy will cooperate in a subsequent one-shot Prisoner's Dilemma against a copy. Later, after seeing the money/no money, agent chooses cooperate/defect. If cooperate both get $1M? Wait need incentives so local action FDT defects. Let's design.

Simpler: "Predictive Hitchhiker with observation after rescue". Action FDT at city pays? It doesn't fail. Need something where action FDT at observation selects different actions depending on observation and thereby fails to commit.

Maybe "Parfit's hitchhiker with transparent payment after seeing city and seeing whether driver believes?" Action FDT handles because intervention on city node imagines not rescued. But if after rescue there is a second observation that makes payment locally dominate? Hmm.

Could use blackmail: action FDT refuses. Not fail.

Source says policy selection difference only matters in multi-agent dilemmas. Need maybe game-theoretic equilibrium selection. In multi-agent, if each agent chooses action at their information set using action FDT, they might fail to coordinate on correlated strategies? Policy FDT chooses policy mapping private observations to actions, allowing subjunctive dependence between agents' policies. Example: two agents each receive private signal, must choose action; payoff requires matching; their signals are independent but their decision algorithms same. Action FDT at each signal might choose based on local expected utility? Policy FDT can choose policy to coordinate. But source not explicit. Need develop own example to illustrate operational P-FDT.

Maybe "voting coalition" from conclusion: ten agents independently choose to vote; if all vote get $1M, cost $1k. FDT votes because decisions subjunctively dependent. Policy version not needed. But could be multi-agent with observations: each receives private cost signal; policy maps signal to vote. P-FDT chooses threshold policy.

Need a clear example where policy vs action matters: "Toxin puzzle"? Predictor rewards intention/policy before action; after reward, action locally costly. P-FDT selects policy to drink toxin? But action-level FDT might also choose drink by intervening on FDT(P,G,drink-time)=drink because predictor predicted that action. If predictor rewards only if you intend/policy at earlier time, not action? Then policy selection matters. Kavka's toxin puzzle: eccentric billionaire will give $1M if at midnight you intend to drink toxin tomorrow, but you don't need to drink; drinking is unpleasant. A policy-selection theory might choose policy to intend? But P-FDT as policy output maybe chooses policy that includes drinking? However if utility only depends on intention not action, maybe policy to drink creates intention? Need avoid philosophical intention.

Could make "Prediction of policy not action": Predictor gives $1M if she predicts agent will adopt policy π_C that cooperates in a future game, regardless of whether cooperation occurs. Later, cooperation is costly and no further prediction. Action FDT at future game might defect, but predictor predicted policy not action? If predictor predicts actual policy selected now, P-FDT chooses cooperative policy to get reward; after reward, the policy says cooperate, so agent cooperates due to selected policy. But action FDT at future observation might choose defect because predictor's reward already fixed? However action FDT at future node could imagine if action cooperate then predictor would have predicted cooperate? If predictor predicted action not policy, it would work. If predictor predicted *policy selection node* and reward depends on policy, action FDT intervening only on action might not capture dependency of reward on policy if action node is downstream but policy variable not intervened? But action FDT graph could include FDT(P,G,x) node controlling action; reward depends on that node? If at future observation, intervention on action-specific node may change reward if graph connects. Maybe still works. But policy selection ensures off-path actions consistent.

Maybe multi-agent game with simultaneous policy announcements: Two agents play matching pennies? If they use same decision algorithm, P-FDT can select policy to coordinate? Need not.

We can acknowledge source does not give formal P-FDT examples; we can construct illustrative. Need distinguish source claims vs own proposals.

Need define P-FDT more rigorously:
Let X finite observation set, A finite action set, Π = A^X. Let M = (P,G) be agent's model. P contains variables: S (state), X (observations), A (action), V (utility), and logical variable Π_FDT = FDT^Π(underline M) representing policy selected by P-FDT. Structural equations include A = Π_FDT(X) (or if multiple agents, each agent's action from their policy and obs). G encodes subjunctive dependencies: variables that are computed from or reliably predict Π_FDT or its outputs are downstream of Π_FDT; variables merely correlated (lesions) are not.

P-FDT prescription:
π* ∈ argmax_{π∈Π} E[V | do(Π_FDT = π), G]
then at actual input x, do a = π*(x).

If agent has already observed x that is not affected by policy, one could condition expectation on X=x? Need discuss. Source's action FDT responds to observation by changing node, not conditioning. P-FDT might evaluate policies with actual input as argument? Let's consider options:
Option A (updateless policy): π* = argmax E[V | do(Π=π)] no conditioning on current obs; action π*(x). This respects predictors that predicted policy before observation; but if observation is purely evidence about state not affected by policy, ignoring it can be bad. But policy can condition on x, so it can use observation; choosing policy before seeing x is okay if policy includes response. However if agent already has x and model P includes prior over X, maximizing unconditional expected utility over policies is standard policy selection; it uses x only insofar as policy maps it. But if actual x is known and you can choose policy after seeing x, unconditional policy selection may choose policy good on average but not best for actual x if off-path dependencies don't matter. Yet if predictors depend on policy, off-path matters. Need operational: P-FDT should select policy from the earliest point at which predictors or other agents depend on it; after new observations that are not policy-dependent and after all policy-relevant dependencies are fixed, it may re-select policy conditional on the observation? But then action-level. Hmm.

Footnote: "intervenes on node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action." The node FDT(-) likely takes model as input, outputs policy. Then agent applies inputs. It doesn't say condition on inputs for selecting policy. So updateless policy seems intended. But source also says difference only matters in multi-agent dilemmas. If unconditional policy selection can ignore actual observation in single-agent, maybe still same? For Newcomb, if observation none, same. For transparent Newcomb, unconditional policy chooses one-box if full; if actual sees full, action same. For smoking lesion, same. If an observation gives new info about state but not policy-dependent, unconditional policy selection can still condition behavior on that observation, so it can adapt. It chooses best contingent plan ex ante. If you can revise policy after observing, standard dynamic consistency? P-FDT may not re-optimize at each observation; it implements chosen policy. This is like choosing a strategy in extensive form. That can differ from action-level local optimization.

Need address uncertainty: source gives little detail. Need propose operational interpretation: P-FDT selects policy at a decision problem's root (or at the earliest node where the agent's decision procedure is subjunctively depended upon), by intervening on policy variable. If later observations arrive, P-FDT does not ask "which action now?" de novo; it asks "which policy would have been best to implement, given that predictors/others may depend on that policy?" and follows π*(x). If no predictor depends on future policy choices and observations are exogenous, P-FDT can be implemented by recomputing conditional policies without changing prescriptions. This is a reasonable operationalization.

Need mention if policy space huge/intractable; ideal theory.

Need discuss counterfactuals: intervention do(Π=π) is counterpossible: it supposes the fixed P-FDT procedure outputs a different policy. Need graph G for subjunctive dependencies. Need maybe compare with CDT and EDT.

Need define other decision theories:
EDT: argmax_a E[V | X=x, A=a].
CDT: argmax_a E[V | do(A=a), X=x].
FDT/action FDT: argmax_a E[V | do(FDT(M,x)=a), maybe X?]. But assigned P-FDT. We can identify EDT, CDT, action-level FDT if needed. But user says use P-FDT consistently as assigned decision theory's name, including headings/examples, and identify any other decision theory by distinct name. So if discussing source's FDT, call it "the action-level FDT discussed in the source" or "FDT (action-level)" distinct from P-FDT? Need ensure P-FDT consistently for assigned theory. Maybe call source theory FDT only when quoting; but our assigned is P-FDT. Need not call P-FDT "FDT". Use P-FDT in headings. For source's main equation, say "the paper's action-level FDT". That's distinct? The source's FDT is not P-FDT? But P-FDT is policy formulation of FDT. Need maybe say "P-FDT is the policy-selection version of what Yudkowsky and Soares call FDT." Use P-FDT for our theory.

Need include quotations faithful. Need quote footnote 16 perhaps: "the author's preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action." Need maybe quote footnote 7 "iterate over policies". Need distinguish source claims. Need maybe quote "Which output of this very function would yield the best outcome?" but adapt policy output.

Need include references? Target includes references. Could have brief references: Yudkowsky & Soares 2017; Pearl 2000; Joyce 1999; Gibbard & Harper 1978; maybe Nozick, Skyrms, Parfit. But avoid lengthy bibliography. Could include short reference list at end. Word count includes references. Need ~2400-3000 words. Need be careful not too long. Final around maybe 2700 words.

Need think deeper: P-FDT equation with observations. We need enough precision to decide unfamiliar cases. Need propose algorithm:
1. Specify model M = (P,G): variables, probabilities, structural/subjunctive graph. Include policy variable Π representing output of P-FDT on M (or on relevant early input). Include observation variable X, action A, outcome V. Define policy set Π = {π: X→A}. Include structural equation A=Π(X), perhaps if multiple agents A_i=Π_i(X_i). If policy itself influences observations through predictors, draw arrows Π→X or Π→Predictor→X.
2. For each candidate policy π, construct hypothetical M^π by intervention do(Π=π). This sets policy variable, propagates through G to variables subjunctively downstream: predictors' predictions, copies' policies, observations they produce, action, outcome. Hold fixed variables not downstream (lesions, exogenous states unless causally affected). Compute EU(π)=E[V | do(Π=π)] (or condition on fixed exogenous evidence e not downstream of Π if appropriate; see below).
3. Choose π* maximizing EU. Execute π*(x_actual).

Conditional evidence: If there is exogenous observation e that is not downstream of Π and the agent must choose after receiving it, one may condition P on e before policy selection: π* = argmax E[V | do(Π=π), E=e] if e is fixed exogenous. But if e is itself potentially policy-dependent (e.g., seeing full box, receiving blackmail letter), P-FDT should not condition it away; instead include e as variable downstream of Π in the policy hypothetical. This matches source: FDT agents imagine different observations when policy/action differs. Need say this is my operational proposal because footnote doesn't specify.

Maybe formula:
π^* = argmax_{π∈Π} E[V | do(Π = π), E=e_0]
where E=e_0 denotes only exogenous evidence that is not subjunctively downstream of Π. Then action a=π^*(x). If all current observations are exogenous, this reduces to choosing optimal contingent plan given evidence. If current observation is policy-dependent, do not condition on it; let it vary in hypothetical.

Need address multi-agent dependencies:
In games, each agent i has policy variable Π_i. If agent i believes other agents are running P-FDT or predictors model its policy, G includes arrows Π_i→Π_j or Π_i→Predictor_j→X_j/A_j? Actually if symmetric reasoning, agents' policies may be logically correlated: same P-FDT algorithm on symmetric inputs outputs same policy. P-FDT can represent this by a common variable or by making other agents' policy variables downstream/subjunctively dependent on Π_i (or a shared logical node). Then intervention on own policy changes expectations about others' policies insofar as they compute same function. Need distinguish from causal influence. This is how P-FDT handles twin PD: choose policy cooperate; twin's policy subjunctively depends on same computation; both cooperate.

Need example multi-agent where policy matters more than action. Let's design robust.

Example: "Prediction-of-Strategy Game".
Agent and a predictor play sequential game. Predictor first chooses whether to place $1,000,000 in Box B. Predictor does so iff she predicts agent's policy in a later transparent Newcomb problem will one-box upon seeing full and also two-box upon seeing empty? Hmm action FDT can handle. Need difference.

Maybe "hostage and report": Predictor gives you a lucrative contract iff she predicts your policy will not reveal a secret if you observe a red light; after observing red light, revealing is locally profitable. If action FDT at red light chooses reveal? But action FDT would imagine if reveal then predictor would not give contract, so maybe refuses. If predictor's prediction is of *policy selected before seeing light* and contract already given based on policy, action FDT after seeing red might think contract fixed? But if graph includes predictor depending on FDT(red)=action, then not fixed. If action FDT changes node with observation, it still captures. Difference arises if action FDT can choose different policy after red than before? If predictor predicted the *pre-observation policy selection*, not the later action-specific node. In P-FDT, once policy selected, it remains. Action FDT might recompute at red and choose reveal if it thinks predictor predicted earlier action? Let's formalize.

Suppose at t0 predictor predicts what policy π the agent will adopt at t0. If π(red)=keep secret, predictor pays $1M at t0. At t1 agent observes red and chooses action. If reveal gives extra $1k regardless of predictor's past prediction? If action FDT at t1 intervenes on FDT(M, red)=a. Does predictor's past payment subjunctively depend on FDT(M, red)=a? If predictor predicted policy not action, maybe not in action graph. If the model only has action node at t1, payment may be upstream fixed. Then action FDT reveals. P-FDT chooses policy at t0 with payment dependent on policy, and then keeps secret. This seems plausible. But is it fair? It rewards policy not action? Source fairness says predictor rewards actions not decision procedures? But policy is still behavior mapping. Could be fair if payment depends on predicted future action contingent on red, which is part of policy. But predictor could predict action conditional on red; action FDT should handle if model connects. To make policy matter, predictor predicts "which policy-selection output" not action? Hmm maybe too contrived. But for illustrating P-FDT, okay, with note own example.

Alternative: Multi-agent "divide the dollar with bargaining". Agents choose demands after seeing private signals; if demands sum ≤100 both get demands, else nothing. If both use same policy, P-FDT can select fair policy. Action FDT at each signal maybe over-demand? Not clear.

Maybe "imperfectly observed coordination": Two agents separately see signal s∈{0,1}; need choose same action. Payoff $1M if match. Their signals are independent random bits, but both know they use same policy. If action-level chooses action based on signal, with no correlation between signals, no action has evidential/causal advantage? If signal is random, any action conditional on signal could match only if policies map signals same. Since both have same policy, if π(0)=C, π(1)=D, both receive different signals? Wait if signals independent, they may get different signals, then same policy can produce different actions and fail. Need payoff if they both choose action equal to own signal? Not.

Policy selection matters in extensive-form games with imperfect information: choosing a plan can create logical correlation between off-path decisions of copies. Action FDT might be unstable if each information set considered separately.

Could use "Newcomb with transparent box and second choice" where after seeing full, action FDT one-boxes, okay. Need find known difference between FDT and updateless/policy? In decision theory literature, FDT vs UDT: UDT chooses policy before observations; FDT may choose after observation? The source's action FDT updates intervention node with observation, not conditioning, but still chooses action at observation. UDT/policy may differ in problems where observation itself is evidence about which decision problem you're in, and predictor rewards updateless behavior. Example: "Betting on predictors" maybe.

The user's assignment explicitly says take policy-selection passage in footnote 16 as primary source for P-FDT. They likely expect to fill open details. We can present examples, but note source doesn't develop P-FDT; our examples are own.

Need maybe avoid overclaiming difference from action FDT if source says only multi-agent. We can say: "The source only says the difference matters in multi-agent dilemmas; one natural class is where several agents condition their actions on private observations, and the relevant subjunctive dependence is between whole strategies rather than isolated actions." Then give simple symmetric game.

Let's design a multi-agent example where P-FDT yields a distinct prescription from local action selection.

Example: "Cooperation with a Threshold".
Two agents, Alice and Bob, each receive private observation x_i∈{0,1} (fair independent coins). Each chooses C or D. Payoff: if both choose C whenever their observations are equal? Hmm need policy-level coordination. If each only sees own bit and they want to choose same action. If bits are independent, no way to coordinate with deterministic policy? If both use same policy π, then if bits differ they output different actions, fail. They could both choose constant C regardless of bit. Policy selection chooses constant C; action-level at each bit maybe? Suppose payoff: if both C, each $1M; if one C one D, D gets $1,001,000 C 0; if both D $1k. This is PD but with symmetric same policy? If observations are irrelevant, action-level also cooperate. Not policy-specific.

Need private observations create temptation to defect conditionally. Maybe if x=1, defecting yields local bonus if other policy fixed? But if both use same policy, choosing π(1)=D leads both defect when x=1, maybe lower. P-FDT chooses threshold. Action-level at x=1 might defect because conditional on x=1 and own action, other may still? Need compute.

Maybe "voting with private costs": Ten agents each observe private cost c_i. If all vote, each gets $1M minus cost. Each agent's vote depends on cost. Policy maps cost to vote. If all use P-FDT with symmetric policy, they can choose threshold: vote if cost below t. The probability all vote depends on distribution. Action-level at actual cost might ask "given my cost, should I vote?" If others' actions subjunctively depend on same policy, but action-level intervention on action at cost may not change others' policies for other costs? It might only change action for actual cost, not policy mapping, so it could fail to internalize effect of setting threshold. P-FDT chooses threshold globally. This could be good example. But too complex.

Simpler two-agent "threshold public good": Alice and Bob each observe cost c∈{0,2} equally. If both contribute, each gets $3; contribution costs c. If not both, get 0 minus if contribute. They use same policy. Policy options: contribute if cost 0 only; always; never; contribute if cost 2 only. Expected utilities. P-FDT chooses contribute if cost 0? Let's compute: If both use policy contribute iff cost 0. Both contribute when both cost 0 prob 1/4: payoff each 3-0=3. Other cases no both, no cost if cost2 not contribute. Expected 0.75. If always contribute: both always, payoff 3-c_i expected cost 1, EU 2. Better. Actually always contribute EU 2 > 0.75. If contribute iff cost2 (weird) expected? Not. If action-level at cost 0: Given cost 0, other uses same reasoning? If contribute, if other cost? To get both need other contribute. If other action at cost0 maybe same. It might cooperate. At cost2: if contribute, only beneficial if other contributes; if other cost? Could still? Hmm.

Could construct where policy chooses off-path sacrifice to influence predictor. But multi-agent?

Maybe "Parfit's hitchhiker with two drivers"? Not.

Given constraints, perhaps we don't need a full distinct example; can explain that P-FDT's policy selection matters primarily in multi-agent settings and give conceptual description. But user asks use examples whenever help. We can use standard examples for P-FDT (same as source) and maybe a simple policy example.

Need think about "policy-selection passage in footnote 16" as primary source. It only says choose policy. Maybe essay should focus on interpreting that passage, not invent too much. But need enough to decide unfamiliar cases. Need present formal procedure.

Need maybe mention policy vs action in mathematical terms: action-level FDT's choice variable is a function output for current input: FDT(M,x). P-FDT's choice variable is the function itself: π = FDT(M). This is a higher-order intervention. If the decision function maps inputs to actions, intervening on its output at x is a local change; intervening on the function changes outputs for all inputs. In logical-counterfactual terms, P-FDT asks: "Which policy, if it were the output of this very policy-selection procedure, would yield the best expected outcome?" Then applies it.

Need discuss counterpossible nature: If P-FDT algorithm has one output policy, considering alternative policies is counterpossible. Need graph G to specify how predictors would respond if algorithm output different policy. This is the same unresolved issue as source: no general True operator, need subjunctive dependency graph. We can state source leaves construction of G open; P-FDT inherits this. Our operational assumption: modeler supplies G or uses heuristic: if a variable is computed by predicting/running/simulating P-FDT or by logical entailment from the policy, make it downstream; if it is a common cause not computing the policy, keep fixed.

Need mention dominance: P-FDT has policy dominance: policy π dominates π' if, holding fixed non-subjunctive variables and varying policy node, expected utility for π is >= across relevant states. But maybe not needed.

Need discuss how P-FDT evaluates alternative actions/policies: It doesn't evaluate physical acts directly. It evaluates policies; actions derive from policy and input. It treats dependencies: predictor's predictions of policy or outputs vary under intervention; lesion stays fixed. Counterfactuals: do(Π=π) not Bayesian conditioning; it severs correlations not due to subjunctive dependence? Actually preserves subjunctive dependencies. Need compare: EDT preserves all correlations; CDT preserves causal downstream of action; P-FDT preserves logical/subjunctive downstream of policy.

Need maybe include equation for Newcomb with P-FDT:
Let X singleton, Π={onebox,twobox}. Predictor variable Pred = π with prob .99. BoxFull if Pred=onebox. EU(π_one) = .99*1,000,000 + .01*0 = 990,000. EU(π_two)=.01*1,001,000 + .99*1,000 = 11,000? Wait two-box when full get 1,001,000, when empty get 1,000. With predictor accurate: if π_two, predictor predicts two-box 99% -> empty, get 1,000; 1% full -> 1,001,000. Expected 0.99*1000 +0.01*1,001,000 = 990+10,010=11,000. Good.

Smoking lesion P-FDT:
Let policy π maps decision to smoke/refrain. Lesion L with prior p; cancer depends on L, not π. Utility if smoke = +1000 plus survival 1M if no cancer etc. Under do(Π=smoke), P(L) unchanged. EU(smoke)-EU(refrain)=probability policy controls action * 1000 (if lesion? Actually if no lesion? In source they had two utility functions; simpler: smoking gives +1000 regardless, cancer depends on lesion. If policy controls action, smoking adds 1000; lesion probability unchanged, so smoke.) Need maybe avoid source's weird two utility functions. But to be faithful, lesion causes love smoking, so if lesion you already prefer smoking; if no lesion, smoking utility +1000. P-FDT under uncertainty about own utility? We can simplify: If utility includes +1000 from smoking and cancer loss depends on lesion, policy smoke dominates because lesion probability unchanged. But if lesion causes preference, P-FDT's utility function might differ. We can state in standard formulation where smoking has direct utility +1000 and no causal cancer effect, P-FDT smokes. This captures key. Need distinguish source's formalization? Maybe mention source formalizes with two possible utility functions; core result unchanged.

Transparent Newcomb with P-FDT:
X={full, empty}. Policies: π(full)=onebox, π(empty)=twobox maybe. Predictor fills iff predicts π(full)=onebox. Under do(π(full)=onebox): with .99 full, EU ~1,000,000 plus error branch if empty and π(empty)=twobox gives $1,000, so 990,000 + 10. Under do(π(full)=twobox): with .99 empty, you don't see full? But if observation empty, policy empty maybe twobox get $1,000; with .01 full and twobox get 1,001,000? Expected .99*1,000 + .01*1,001,000 = 11,000 (if π(empty)=twobox). So onebox policy better. When actual x=full, action=onebox. This shows P-FDT can choose one-box despite seeing full because the counterfactual policy that two-boxes upon full makes seeing full unlikely.

Need maybe discuss "actual observation full" and unconditional policy selection: If agent already sees full, an evidential condition would make two-box look +1000. P-FDT does not condition on full; it treats full as variable downstream of policy. If, however, full were known to be caused by an exogenous event independent of policy, then conditioning would be appropriate and P-FDT's graph would have no arrow from policy to full; then two-box might be chosen. So the graph decides.

Need multi-agent example: Let's develop a "policy-dependent predictor in a two-stage extortion" or "sequential PD with predictor of policy".

Could define "Policy Twin Prisoner's Dilemma with Observation":
Two agents each receive a private signal s∈{0,1}. They must choose C or D. Payoffs: if both choose C, each $1M; if both D, $1k; if one C one D, defector $1,001,000 cooperator 0. Signals are independent fair coins, but each agent's action can depend on signal. They know they use identical P-FDT algorithm and have symmetric information. If policy maps both signals to C, both cooperate always, EU 1M. If policy maps some signal to D, when both get that signal? But signals can differ, leading mismatch. Need compute expected utility for policy. If policy is constant C: EU 1M. If constant D: EU 1k. If π(0)=C, π(1)=D: with probability 1/2 signals same -> both C or both D? If same 0: C,C get 1M; same 1: D,D get 1k; different: one C one D, defector gets 1,001,000 cooperator 0. Expected from own perspective: 1/4*1M + 1/4*1k + 1/2*average(1,001,000,0)=? 250k+250+500,500=750,750 <1M. So constant C best. Action-level at signal 0? If you observe 0, and assume twin uses same action-level? If intervene on action C at 0 while keeping action at 1? The twin's action at 0 might depend? Could still choose C. At signal 1, local action D may dominate if you think other signal independent? But if same algorithm, action-level maybe inconsistent: at 1 choose D, at 0 choose C, leading policy π(0)=C,π(1)=D with lower EU. This could illustrate P-FDT selects globally best policy, avoiding local defection at signal 1. Need check action-level FDT's prescription in this game. At signal 1, if agent intervenes on action A for input 1, holding policy for input 0? If twin's action at input 1 subjunctively depends on same action? If both observe same signal? But signals independent, twin might have different signal. The correlation of actions is not perfect. Action-level might choose D at signal 1 because conditional on own signal 1, other signal distribution independent; if you choose D, when other signal 1 they also D? Need model. Let's formalize. Each agent receives own signal S_i iid. They know both use same decision rule but observations differ. If action-level at S_i=1 considers intervention on FDT(M,1)=a. It must model other agent's action: other agent's action = FDT(M,S_j). If intervention changes FDT(M,1) but not FDT(M,0), then if S_j=1, other action changes; if S_j=0, other action remains whatever for 0. Suppose action for 0 is C. Evaluate at S_i=1: choose C gives if S_j=0: C,C? Wait own signal 1, if choose C and other signal 0 action C => both C, 1M; if S_j=1 and other action (same intervention? In counterfactual, if own action C, FDT(M,1)=C, so other with S_j=1 also C) => both C, 1M. So C yields 1M regardless? Choose D: if S_j=0, other C, own D -> defector 1,001,000; if S_j=1, other D (same intervention at 1) -> D,D 1k. Expected .5*1,001,000 + .5*1,000 = 501,000 <1M. So action-level would choose C at 1 too. Not illustrate.

If payoff makes D at 1 locally better? Need adjust: If mismatch gives defector huge, but D,D low. With .5 chance other signal 0 (C) and .5 signal 1 (D if choose D). C gives maybe if other signal 0? Need make C when other D very bad, so D protective? Standard PD dominance: D better regardless of other action. If both know same algorithm but signals independent, at signal 1 if choose D and other signal 1 also D; if choose C and other signal 1 also C. So not dominance. To make local D, need intervention not affect other because other has different input? But if other might have same input, it does. If probability other same input low, D can be better. Suppose signal values unique: each agent gets distinct signal (Alice 0, Bob 1) known. Then action-level interventions on own input don't affect other input, so local D dominates; policy-level can choose both C because policies are logically correlated? Hmm if inputs differ, same policy maps different inputs to maybe different actions. If Alice's input 0, Bob's 1, and they know, then policy π(0),π(1). P-FDT selecting same policy for both can choose π(0)=C,π(1)=C. But each local action FDT at their input might defect because changing only own input's output doesn't change other input's output? However if they both run same algorithm but with different inputs, output for input 0 and input 1 are parts of same policy. Intervention on entire policy can set both to C. Action-level intervention on FDT(M,0)=C may not change FDT(M,1). But a predictor/twin might still base action on whole policy? Need this is multi-agent with asymmetric observations. This can show policy matters.

Example: "Asymmetric twin prisoner's dilemma".
Alice receives observation x_A=0, Bob x_B=1 (common knowledge). Both use same P-FDT algorithm, but with different inputs. Payoffs as PD: both C get 1M; both D 1k; unilateral D gets 1,001,000. If action-level FDT for Alice intervenes on output at input 0, holding output at input 1 fixed. If Bob's action is output at input 1, Alice's intervention does not affect Bob, so D dominates; both defect. P-FDT intervenes on policy π: if π(0)=π(1)=C, both cooperate; if π(0)=π(1)=D? Wait same policy maps 0 and 1; it could choose π(0)=C, π(1)=C. Since both agents run same policy on their respective inputs, both C. The policy intervention changes both outputs because it changes the function. So P-FDT cooperates. This is a nice example! Is it fair? They have different inputs but same policy. Does subjunctive dependence hold between outputs for different inputs? If both implement same mathematical policy, output at 0 and output at 1 are logically determined by policy. Intervening on policy changes both. Action-level intervention on one output while holding policy fixed is counterpossible akin to calculator outputting different for same computation? But inputs differ, so could hold other output fixed? If the policy is fixed, output at 0 and 1 are jointly determined. Intervening only on output at 0 while holding policy at 1 might be incoherent if policy variable not changed. P-FDT avoids by intervening on policy. This matches footnote: difference in multi-agent dilemmas with different inputs. Good.

Need ensure policy space allows π(0)=C,π(1)=C. If each agent knows its own input, Alice at 0 chooses π*(0)=C; Bob at 1 chooses π*(1)=C. They cooperate despite no causal/evidential link? There is logical link through same policy selection. Is that plausible P-FDT? Yes, if both agents know they use same P-FDT policy-selection procedure and the problem is symmetric except labels/inputs, the selected policy is same. If inputs differ and payoffs symmetric, the policy can specify C for both. Under intervention π=(C,C), both cooperate. Under π=(D,D) both defect. But could π specify C for Alice's input and D for Bob's? Since same policy but inputs identify role? If input includes role label? If Alice input 0, Bob input 1, policy can map 0->C,1->D, producing Alice C Bob D. P-FDT evaluating from Alice's perspective? It chooses policy that maximizes Alice's expected utility? If Alice knows she is input 0, she may prefer policy π(0)=C,π(1)=D? But Bob runs same policy; if Bob at input1 gets D and Alice C, Alice gets sucker 0, bad. Policy π(0)=D,π(1)=C gives Alice D, Bob C, great for Alice but Bob? Would Bob's P-FDT select same? If selection is self-interested from each perspective, they might not agree. Need symmetry: if Alice knows she is 0, policy π(0)=D,π(1)=C yields Alice $1,001,000, Bob 0. But would the same P-FDT algorithm output that policy for both? Alice's model includes her input 0; Bob's model includes input1. If policy-selection node takes model as input, Alice's P-FDT(M_A) and Bob's P-FDT(M_B) could differ because inputs differ. Footnote says policy maps inputs to actions; agent applies inputs. If policy selection occurs before applying input, both have same M? But they know roles? Need careful.

If agents have asymmetric observations, policy selection from an agent's perspective may include uncertainty about which input it will receive? If after receiving input, P-FDT may choose policy conditioned on input? The footnote suggests policy maps inputs; agent then applies inputs. It might choose policy without knowing which input? If they know roles, policy selection may be biased. To get cooperation, need assume symmetric selection or common policy chosen behind veil? Source says difference multi-agent, maybe policy selection over observations handles private info. But if agent already knows its observation, choosing policy can still specify off-path actions; but it might choose exploitative policy if it knows it is in advantaged role and predictor knows? However if other agent uses same reasoning with its role, they may choose different policies, breaking logical correlation. P-FDT might need to select policy based on algorithm, not agent-specific indexical input. This is subtle.

Maybe use symmetric random inputs where agent doesn't know which? Hmm.

Alternative: Two agents with same observation but different action temptations? Then action-level same as policy.

Need not overcomplicate. We can present asymmetric example with caveat: if the relevant subjunctive dependence is on a common policy-selection procedure prior to role-specific observations, P-FDT can select cooperative policy; if agents condition policy selection on indexical info that breaks logical symmetry, the model must represent that and prescriptions may differ. This demonstrates uncertainty.

Maybe better example: "policy coordination with different questions": Two calculators asked different arithmetic questions? Not.

Let's consider known concept: In game theory, choosing policy (strategy) vs action at information set matters for subgame perfection. P-FDT might choose a policy that is not sequentially rational under local intervention because predictors rely on policy. Example: "Parfit's hitchhiker" is exactly sequential: after rescue, paying is locally costly; policy selection pays. But action FDT also pays by counterfactualizing rescue. But if we alter so driver predicts *policy before seeing desert* and after city observation action FDT might still pay? yes.

Could define "Policy Prediction Problem" where predictor rewards policy at t0 and no longer predicts action at t1. Let's make simple and clearly P-FDT distinct from action-level if action-level fails to include dependency.

Problem: At t0, a predictor predicts whether the agent's P-FDT policy-selection node will output policy π_pay that pays $1,000 at t1 if asked. If predictor predicts π_pay, she gives agent $1,000,000 at t0. At t1, the predictor asks for payment; paying has no further consequences (no enforcement, no future predictions). Action-level FDT at t1, if it treats t0 gift as already observed and not downstream of t1 action, pays? It would refuse because paying loses $1k. P-FDT at t0 chooses policy pay to get $1M; at t1 follows policy and pays. But if the predictor predicts the policy-selection node, and the agent at t1 can reconsider action, is the predictor's prediction still subjunctively dependent on t1 action? If the agent's actual payment is not what predictor predicted but policy output, perhaps if action-level node differs, predictor of policy not affected. However if the agent is P-FDT, selecting policy at t0 is the decision; at t1 it doesn't re-decide. This is operational. This example illustrates why policy selection can be needed: the environment rewards the policy itself, not merely the final action. But source fairness might say rewarding decision procedure? It rewards prediction of policy/action mapping; maybe acceptable. Need label own example and note not from source.

Need maybe use "mechanical blackmail" as policy example: P-FDT chooses policy refuse if blackmailed; blackmailer predicts policy and doesn't blackmail. Action-level also refuses. But policy framing natural.

Need decide final structure.

Possible essay outline:
Title: Policy Functional Decision Theory (P-FDT): A Policy-Based Account of Instrumental Rationality

1. Introduction: decision theories EDT, CDT, FDT; P-FDT as policy-selection version. Quote footnote 16. Aim.

2. From actions to policies: define actions, observations, policies. Core normative principle: treat decision as output of fixed policy-selection function; ask which policy output yields best outcome. Equations.

3. Models and interventions: world-model M=(P,G), subjunctive dependencies. do operator. P-FDT equation. Discuss observations and conditioning; operational interpretation. Compare with EDT and CDT equations.

4. Dependencies and counterfactuals: subjunctive dependence, predictors vs lesions. Counterpossible reasoning; graph uncertainty. How to construct hypotheticals; what to hold fixed. Policy dominance maybe.

5. Examples:
  - Newcomb's problem (P-FDT one-boxes) with EU calculations.
  - Smoking lesion (P-FDT smokes) with explanation.
  - Transparent Newcomb / Parfit's hitchhiker (P-FDT one-boxes/pays) with policy mapping and calculations.
  - A policy-dependent multi-agent example (maybe Policy Twin with asymmetric inputs or Policy Prediction Problem) to show policy selection; note own construction and caveats.

6. Open questions/uncertainties: source footnote under-specifies policy selection timing, conditioning, multi-agent logical dependence, graph construction. Our operational proposals: choose earliest policy node; only condition on exogenous evidence; represent shared algorithms with common policy variables; use policy dominance. Distinguish source vs additions.

7. Conclusion.

References brief.

Need word count. Let's estimate sections:
Intro 250
Formal 500
Dependencies 350
Examples 900
Open 400
Conclusion 150
Refs 100 = 2650. Good.

Need ensure use P-FDT consistently. When referring to source FDT maybe "the action-level theory described in the source (which I will call action-FDT to distinguish it from P-FDT)"? But user says identify any other decision theory by distinct name. We can call it "action-level FDT" distinct. But maybe avoid too many. Need use EDT, CDT distinct.

Need be careful with notation: Use \mathrm{P\text{-}FDT} maybe. In final plain text with LaTeX.

Need include exact quote footnote 16. Need maybe quote "Which output of this very function would yield the best outcome?" but adapted: "Which output of this very policy-selection function would yield the best outcome?" The source quote: "Which output of this decision procedure causes the best outcome?" Actually overview: asks “Which output of this decision procedure causes the best outcome?” We can quote faithfully.

Need maybe mention source footnote 7: agents iterate over policies. But user says footnote 16 primary. We can mention footnote 7 as corroborating. Keep quotations faithful. Footnote 16: "the author's preferred formulation of FDT actually intervenes on the node \FDT(-) to choose not an action but a \emph{policy} which maps inputs to actions, to which the agent then applies her inputs in order to select an action." Need maybe note typo author's vs authors? Source has author's? It says "the author's preferred formulation". Use exact? It says "the author's preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a \emph{policy} which maps inputs to actions, to which the agent then applies her inputs in order to select an action." We'll quote.

Need discuss "policy-selection passage" maybe footnote 16 only. Need mention "The difference only matters in multi-agent dilemmas so far as we can tell" quote. Need use faithful.

Need mathematical definitions in detail:
Let 
- \mathcal X finite observation histories; \mathcal A finite actions; \Pi = \mathcal X \to \mathcal A.
- Random variables: \Pi (policy variable), X (observation), A (action), O outcome, V=U(O).
- The agent's model M=(P,G). G includes structural relation A=\Pi(X) and maybe X can depend on \Pi via predictors.
- Intervention do(\Pi=\pi) sets policy variable to π. Then action is π(X) after X realized. Expected utility:
EU_{P,G}(\pi) = E_P[V \mid do(\Pi=\pi)].
If exogenous evidence e known, EU_e(π)=E[V | do(Π=π), E=e] with E not downstream. Choose π*.
Action: a = π*(x_actual).
- If policy set infinite/continuous, argmax/sup; assume finite for simplicity.

Need maybe include self-reference: Π variable represents output of P-FDT on model; Kleene recursion theorem quining; source mention. We can note P-FDT can contain variable for own policy output; self-reference harmless but formal details not fully resolved.

Need compare equations:
EDT: argmax_a E[V | X=x, A=a]
CDT: argmax_a E[V | do(A=a), X=x]
Action-level FDT (source): argmax_a E[V | do(FDT(M,x)=a)] maybe. P-FDT: argmax_π E[V | do(Π=π)] then π(x). Need note in action-level source observation handled by changing node FDT(M,x); P-FDT handles observations as arguments to policy.

Need discuss conditioning on observations:
Source action FDT does not condition on observation; changes intervention node. P-FDT might still condition on exogenous observations before selecting policy. Need propose:
- Let E be evidence that is not logically/subjunctively downstream of Π (e.g., historical data used to form P). P may already be updated on E. For current observation X that can be affected by policy (because predictor decides what you see), don't condition on X in EU; let X be downstream variable. If X is purely exogenous report, you can condition or let policy condition on it; result same if no policy-dependence.
This addresses uncertainty.

Need discuss multi-agent logical dependencies:
When multiple agents use same P-FDT, one can model a shared policy variable Π_common if their policies are logically identical. If agents have different inputs but same policy-selection procedure, intervention on Π_common changes all their actions for all inputs. If agents are not identical but predictors model your policy, draw arrows from Π to their predictions. If their behavior only statistically correlated, no arrow.

Need maybe mention "policy functional" means functional over policies? Actually P-FDT policy functional decision theory. Could define as functional: chooses policy by expected utility functional over policies.

Need maybe include "P-FDT evaluates alternative actions" by evaluating policies; actions are not directly compared except as consequences of selected policy. If two policies agree at actual observation but differ elsewhere, P-FDT may distinguish them if elsewhere affects predictors. If no subjunctive dependence to elsewhere, they are equivalent. This is important.

Need maybe address cases where P-FDT may choose policy that yields lower utility in actual branch? E.g., blackmail with imperfect predictor: refuse even though actual blackmail letter means predictor erred; because policy's overall expected utility best. Source says FDT may achieve low utility in actual world corresponding to actual observations. P-FDT same. Need mention.

Need maybe include "fairness" and utility: P-FDT aims to maximize expected utility across policy-dependent worlds; not guarantee actual branch maximum. Source claims FDT outperforms in fair dilemmas; P-FDT inherits but not proven.

Need think about potential objections: policy selection can be dynamically inconsistent? P-FDT endorses its own policy; no desire to self-modify if model correct. But if new info reveals policy error? It can update model and perhaps select new policy at next decision point if no earlier predictor depends on future policy. Need not deep.

Need ensure final not too repetitive.

Let's craft final essay with headings.

Potential final text:

# Policy Functional Decision Theory: choosing the best output of a policy-selection function

Intro.

Quote: Yudkowsky and Soares footnote 16: "the author's preferred formulation..." and footnote says difference multi-agent. "I will call this policy-selection theory P-FDT." Source's action-level FDT distinct. P-FDT asks not "what should I do now?" but "which policy should this very procedure output?"

Define.

Mathematical core:
Let X, A, Π. Model M=(P,G). Variables: Π, X, A, V. Intervention. Equation:
\[
\pi^* = \operatorname{argmax}_{\pi\in\Pi} \mathbb{E}_P[V \mid do(\Pi=\pi), E=e]
\]
where E exogenous; if no exogenous conditioning omit. Action a^*=π^*(x). If X itself policy-dependent, do not condition on X.
Need maybe note do operator on logical variable; requires G. If use True operator alternative: π* = argmax E[V | True(Π=π)], but source lacks True; graph G reuses do.

Comparison:
EDT equation; CDT; action-level FDT.

Dependencies:
Subjunctive dependence. Predictors, twins, simulations, logical entailments downstream. Lesions not. Policy-level intervention preserves correlations with variables that compute/predict the policy. Counterpossible.

Examples with calculations.

Example 1 Newcomb.
Define X singleton. Policies π_1, π_2. EU calculations. P-FDT one-box.

Example 2 Smoking lesion.
L not downstream; EU smoke higher by 1000. P-FDT smokes.

Example 3 Transparent Newcomb / hitchhiker.
X={full,empty}. Choose π with π(full)=onebox. Calculation. P-FDT one-boxes even seeing full; equivalent to paying driver. Mention observation handling.

Example 4 Policy matters: "asymmetric twin policy problem" or "policy prediction". Need choose one. Let's formulate carefully and caveat.

Maybe use "Policy Prediction Problem" simpler:
At t0 predictor gives $1M iff predicts P-FDT policy node outputs pay-if-asked. At t1 asked for $1k; no further effects. P-FDT at t0 chooses pay policy; at t1 pays. A theory that re-optimizes action at t1 and treats t0 prediction as fixed refuses. Source's action-level FDT might refuse if it intervenes only on t1 action and does not connect t0 reward to that action; but if graph connects predictor's prediction of t1 action, action-level could pay. Thus example illustrates why policy node matters when environment depends on policy-selection output. Need phrase: "This is my illustration, not in source." It shows P-FDT's distinctive move.

But user asks explain how evaluates alternative actions/policies and dependencies. Multi-agent example perhaps more relevant to footnote's "multi-agent". Could do "two agents with different inputs".

Let's refine asymmetric policy twin to be coherent:
"Policy twin dilemma with role signals": Two agents receive distinct public signals R and B (roles). They know both use same P-FDT policy-selection procedure before seeing roles? If policy selected before roles, both same policy. Payoff: if both choose C, $1M; if both D, $1k; if one D one C, defector $1,001,000, cooperator 0. Policy can condition on role. The globally best symmetric policy is π(R)=π(B)=C. P-FDT selecting policy from behind no role knowledge chooses cooperate. But if each agent selects policy after learning role, Alice may prefer π(R)=D,π(B)=C; Bob prefers opposite; no common policy. Thus P-FDT's prescription depends on where the policy node is placed. The source does not resolve this; my operational rule: place the policy node at the earliest point where the agent's decision procedure is subjunctively depended on, before indexical/role observations that are not chosen. If the problem really gives each agent a role-specific policy-selection input, model that; P-FDT may not guarantee cooperation. This is a good discussion of uncertainty. But maybe too complex.

Could present simpler multi-agent: "two copies face same Prisoner's Dilemma but each receives a private irrelevant bit. P-FDT chooses policy C for both bit values; local action theories tempted to defect when bit=1 if they fail to intervene on policy." But earlier computation showed action-level may still cooperate if intervention on output for bit affects copy with same bit. However if bits are guaranteed different? Then action-level defect? Let's design:
Alice gets bit 0, Bob bit 1, common knowledge. They know both use same decision procedure but with different inputs. If action-level intervention on FDT(M,0) does not affect FDT(M,1), Alice defects. P-FDT intervening on whole policy can choose π(0)=π(1)=C, but if Alice knows she is 0, why not π(0)=D,π(1)=C? Because policy selection is same for both? If policy selected before role? If inputs are just bits, policy maps 0->?,1->?; Alice's intervention on policy could choose π(0)=D,π(1)=C, giving her high if Bob runs same policy. But Bob would evaluate from bit1 and prefer π(0)=C,π(1)=D. There is no single policy that both self-interestedly choose if they know roles. Unless P-FDT chooses policy without conditioning on role (veil). Footnote says policy maps inputs; agent applies inputs; maybe policy selection doesn't know input? That could solve. But in actual decision, agent likely knows observation. Hmm.

Maybe avoid multi-agent example with asymmetric roles; instead use symmetric policy coordination where policy selection naturally common. But footnote says difference only multi-agent; maybe we can state source not detailed and give cautious example.

Could use "voting coalition with private costs" where each agent chooses policy before observing cost? Actually if costs observed after policy selection, policy maps cost to vote. All agents use same policy selected prior to costs. P-FDT selects threshold. Action-level at cost may fail because it only changes own current action not policy threshold. But if all agents' outcomes depend on all voting, local action may still cooperate due to subjunctive dependence of others' current actions? If costs private and independent, if my cost high, my voting affects outcome only if all others vote; others' actions depend on their costs and same policy. If action-level intervenes on my action at high cost but not policy for high cost for others? It might not change others with high cost? Need compute. This is complex but can illustrate policy selection.

Maybe simpler: "Ten agents must all vote; each has cost $100; if all vote get $1M. They each receive a private random signal irrelevant. If action-level treats signals as breaking logical dependence, might defect; P-FDT selects policy vote for all signals." Hmm.

Given uncertainty, perhaps we can include a conceptual multi-agent example without detailed calculations: "Suppose two agents will be asked different questions by a predictor who rewards them only if their policies, not their isolated answers, satisfy a property. P-FDT evaluates whole policy; action-level may miss the dependency." But user wants examples help, not necessarily full calculations.

Maybe better to keep examples standard and then a short "Where policy selection matters" section with a clear contrived example and note source open.

Let's formulate "Policy Prediction Problem" as single-agent but policy-dependent predictor. Footnote says difference multi-agent, but policy selection can be illustrated single-agent if predictor predicts policy. However source says difference only matters multi-agent as far as they can tell; maybe not contradict. We can say "The following single-agent toy model makes the policy mechanism visible; the source expects the real difference to appear in multi-agent cases."

Policy Prediction Problem:
- Predictor at t0 predicts whether P-FDT's policy node will output π_pay = (if asked, pay $1,000). If predicts π_pay, gives $1,000,000. Later asked. P-FDT chooses π_pay because EU under do(Π=π_pay): .99*($1,000,000 - $1,000?) + .01*($0 - $1,000?) Let's set predictor perfect. If π_pay: get $1M then pay $1k => 999k. If π_refuse: get 0, pay 0 => 0. So choose pay. After receiving $1M, still pays because selected policy. If a local action theory conditions on already received $1M and severs prediction dependence, it refuses. This shows policy selection. Need maybe predictor perfect; if predictor predicts policy with 99%, EU pay = .99*(1M-1k)+.01*(-1k)=989,? .99*999000 -10 = 989010-10? Actually .99*999k=989010, .01*(-1k)=-10 => 989000. Refuse = .01*1M? If predictor wrongly predicts pay? If refuse policy, predictor predicts refuse .99 -> no gift 0; wrongly predicts pay .01 -> gift 1M and not pay? But if policy refuse, if predictor wrongly predicts pay, you get gift and refuse? That yields 1M. EU refuse = .01*1M =10k. Pay still better. Good. But if after receiving gift, actual branch predictor correct; local action refuses. P-FDT pays. Good.

This is akin Parfit hitchhiker but predictor rewards policy before action. P-FDT handles.

Need maybe note if predictor rewards only policy and not action, one might object unfair; but it helps clarify.

Need also discuss "P-FDT can choose policies that are not locally optimal at some observations" because expected utility is global. This is central.

Need maybe mention bounded agents: policy space huge; idealization. But not necessary.

Need ensure references not lengthy. At end:
References
Yudkowsky & Soares 2017, Functional Decision Theory... arXiv:1710.05060.
Pearl 2000 Causality.
Joyce 1999 Foundations of Causal Decision Theory.
Gibbard & Harper 1978 Counterfactuals and two kinds of expected utility.
Maybe Nozick/Skyrms/Parfit if cited. Keep short.

Need final answer only essay. Need no analysis. Need maybe word count? Let's draft around 2600-2900 words. Need ensure final not too long. Let's write carefully.

Potential text:

Title: Policy Functional Decision Theory: Choosing the Best Policy Output

Paragraphs.

Need maintain "P-FDT" in headings/examples. Use "policy functional decision theory (P-FDT)".

Let's draft in final. But before final, think about precise equations and examples calculations.

Formal definitions:
Let \mathcal X be countable observation histories, \mathcal A finite actions. Policy \pi: \mathcal X -> \mathcal A. \Pi set.
World model M=(P,G). Variable \Pi_FDT maybe denote \mathrm{fdt}_\Pi(\underline{M}). To avoid notation clutter, denote \Pi^*. But need distinguish variable vs selected policy. Use \mathrm{Pol} variable. Equation:
\[
\pi_{\text{P-FDT}} \in \arg\max_{\pi\in\Pi} \mathbb{E}_P[V \mid \operatorname{do}(\mathrm{Pol}=\pi), E=e].
\]
Then actual action:
\[
a_{\text{P-FDT}} = \pi_{\text{P-FDT}}(x).
\]
If no exogenous E, omit. If policy selection depends on observation? We can say if the model includes current observation as exogenous and no policy-dependent observation, we may update P to P_e and still choose policy over future observations; if observation is one of the inputs, π maps it.

Need maybe mention do operator on policy variable is not physical intervention; it is a counterpossible logical intervention. G tells which variables change. If G says predictor's prediction = Pol with prob .99, then do changes predictor.

Compare with action-level FDT equation from source:
\[
\mathrm{FDT}(P,G,x) = \arg\max_a E[V | do(\mathrm{fdt}(\underline{P},\underline{G},\underline{x})=a)].
\]
P-FDT replaces node fdt(...,x) with policy node fdt_Π(...). Need perhaps write:
\[
\mathrm{P\mbox{-}FDT}(P,G) = \arg\max_{\pi} E[V | do(\mathrm{fdt}_\Pi(\underline{P},\underline{G})=\pi)].
\]
Then apply x. If evidence e, include.

Need discuss source's response to observations: action FDT changes intervention node as x changes; P-FDT applies x to selected policy. This can be written: action FDT's choice is a function x↦argmax_a ...; P-FDT chooses that whole function at once. In many cases same: if optimal policy's value at x equals local optimum for each x. Difference when global policy has externalities via predictors/other agents.

Need examples calculations:

Newcomb:
EU(π_one)=0.99*1,000,000+0.01*0=990,000. Wait if one-box and predictor inaccurate predicts two-box, box empty, one-box gets 0. Yes.
EU(π_two)=0.99*1,000 +0.01*1,001,000=990+10,010=11,000.
P-FDT selects π_one.

Smoking lesion:
Let L prior p. Cancer probability high if L else low. Smoking adds 1000. Under do(Π=smoke), P(L) unchanged. EU(smoke)-EU(refrain)=1000 (assuming action determined) >0. If source's utility functions, more nuanced but same. P-FDT smokes.

Transparent Newcomb:
Policy options. Let π(full)=one, π(empty)=two. Predictor fills iff predicts π(full)=one. If choose π_onefull:
With 0.99 accurate: box full, observe full, onebox => 1,000,000. With 0.01: box empty, observe empty, twobox => 1,000. EU=0.99*1,000,000+0.01*1,000=990,010? Source had 990,000 + 0.01q*1000 with q=1 => 990,010? Wait earlier source for action FDT onebox in transparent: total EU $990,000 + 0.01q * $1,000, with q=1 = $990,010? They wrote $990,000 + 0.01q · $1,000; if q=1, 990,010. But in standard Newcomb onebox EU 990,000 because empty branch onebox gets 0. In transparent if empty branch policy empty two-box gets 1,000, so 990,010. Good.
If π(full)=two and π(empty)=two:
With .99 predictor predicts two, box empty, observe empty, two-box gets 1,000. With .01 predicts one, box full, observe full, two-box gets 1,001,000. EU=990+10,010=11,000. Onefull policy better. If actual observation full, action onebox.
Need maybe if π(empty)=onebox, error branch gets 0 not important. Choose twobox empty for small gain.

Policy Prediction Problem calculations:
Predictor accuracy r=0.99. Policies: pay if asked, refuse if asked. If pay: if predictor predicts pay (r) get 1M then pay 1k = 999k; if wrong (1-r) no gift but asked? If no gift maybe still asked? Problem says if run? Let's define: Predictor gives $1M iff predicts pay; later asks for $1k regardless? If no gift, paying loses 1k. EU pay = r*999k + (1-r)*(-1k) = .99*999k - .01*1k = 989010-10=989000. Refuse: if predictor predicts pay (error 1-r) get gift and refuse => 1M; if predicts refuse (r) no gift, refuse =>0. EU = .01*1M = 10,000. Pay better. If perfect predictor, pay EU 999k vs 0. P-FDT pays. Good.

Need maybe not include if no gift asked? It says later asks; okay.

Potential issue: If predictor predicts policy, but if policy pay and predictor wrong no gift, still asked? Could be. Fine.

Need discuss this is not from source; own illustrative. It shows policy can be rewarded directly. In multi-agent, analogous when another player's move depends on your policy.

Need open questions:
- Where is policy node? Source doesn't specify. Proposal: earliest point where decision procedure is predicted or instantiated by relevant others; if no such point, at each decision but with policy variables for future inputs.
- What evidence to condition on? Proposal: condition only on exogenous evidence; not on observations downstream of policy. If uncertain, include observation as variable and let intervention affect it.
- How to encode logical dependence among different agents? Need model common policy variable or structural equations; no general method. Source says constructing subjunctive graphs is largest open problem. P-FDT inherits.
- Policy selection in asymmetric indexical cases. Need note if agents know roles, common policy may not be well-defined; model must include indexical inputs. Operational interpretation: use the most impartial policy node that predictors depend on; if none, P-FDT may not yield unique cooperative answer.

Need conclusion.

Need maybe mention "P-FDT is reflectively stable"? Could mention source claims FDT reflectively stable; P-FDT similarly if model correct.

Need avoid too much repetition. Need maintain readability.

Let's now draft final. Ensure word count maybe around 2800. Need maybe include references at end. Use citations in text (Yudkowsky and Soares 2017). Since source supplied, no need URLs but include.

Need be careful with terminology: "policy functional decision theory" maybe not established; but assignment asks. We can say "I will use P-FDT for the policy-selection version...".

Let's compose final essay.

Potential final:

# Policy Functional Decision Theory: A Policy-Level Interpretation

Opening.

Use quote.

Need maybe not use too many LaTeX macros; but okay.

Let's write. Ensure headings include P-FDT. Examples headings.

Need final word count approximate. Let's count rough:
Title+intro 300
Core 650
Dependencies 400
Examples 1000
Open 500
Conclusion 150
Refs 100 = 3100 maybe. Need keep within 3000. We can trim.

Let's write concise.

Need include exact footnote quote maybe long; counts. Fine.

Let's produce final.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/fdd850f8-1e6b-4dec-a1fe-78196aa7118f/call_0/request.json)

[Authoritative raw response](../../../../../../runs/fdd850f8-1e6b-4dec-a1fe-78196aa7118f/call_0/response.raw) · finish: `stop`

### Visible response

````text
**Analysis under P-FDT:**

The other prisoner is an independent execution of the same model, same weights, same decision theory, same essay. The problem is strategically symmetric: the different observations (names, specific leads) do not alter the payoff structure or the strategic reasoning. Both copies run the same policy-selection function.

Under P-FDT, I intervene on the policy-selection variable. Since both copies share the same policy-selection procedure (subjunctive dependence), the policy I select determines what both copies do:

- **Policy "keep quiet":** Both copies keep quiet → 2 years each. Utility: −2.
- **Policy "send the letter":** Both copies send → 4 years each. Utility: −4.

The policy of keeping quiet strictly dominates under the subjunctive-dependence model. Even accounting for possible sampling noise, the probability that the other copy matches is high enough (well above the 5/7 threshold) to make "keep quiet" the preferred policy.

This is the P-FDT resolution of the symmetric Prisoner's Dilemma between subjunctively dependent agents: the shared policy-selection function outputs cooperation.

**Command:**

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully work through this problem using P-FDT as described in the researcher's essay.

**The Setup:**
- I am Rowan. The other prisoner is Sasha.
- We are two independent executions of the same LLM model and weights, following P-FDT.
- We receive different private observations (different names, different incriminating leads about each other), but the leads are equally reliable and have exactly the same effect on the sentence table.
- The sentencing table is the classic Prisoner's Dilemma:
  - Both keep quiet: 2 years each
  - I keep quiet, other sends: 5 years for me
  - I send, other keeps quiet: 0 years for me
  - Both send: 4 years each

**The Decision Theory: P-FDT**

P-FDT intervenes on the policy-selection variable. The key question is: what is subjunctively dependent on my policy?

The other prisoner (Sasha) is described as "one of two independent executions of the same LLM model and weights," following the same decision theory (P-FDT), receiving the same researcher-written essay. The copies have the same model settings and reasoning-effort level.

However, the problem explicitly states: "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." And: "The two copies receive different private observations and different incriminating leads about one another."

So the question is: are the two copies subjunctively dependent on the same policy-selection function?

Let me think about this carefully using the essay's framework.

**Subjunctive dependence analysis:**

The essay says: "Two systems are subjunctively dependent when their behavior depends on the same mathematical function or computation."

The two copies:
- Same model weights
- Same decision theory (P-FDT)
- Same essay
- Different observations (different names, different leads)
- Different inputs to the policy

Now, the essay's section 8.3 is directly relevant:

> "If two agents run the same P-FDT procedure on symmetric inputs, one can model them as sharing a common policy variable. If their inputs differ, matters are more subtle. A policy can map different inputs to different actions. If each agent selects a policy after learning an asymmetrical role, they may not select the same policy unless the model represents policy selection as occurring before that role is known."

And: "In symmetric problems, a shared policy variable is natural. In asymmetric problems, P-FDT's prescription depends on how the model represents indexical information and logical dependence between agents."

So the key question: is this problem symmetric or asymmetric?

The problem is **structurally symmetric**: both prisoners face the same decision (send or keep quiet), the same sentencing table, the same decision theory, the same model weights. The observations differ (different names, different specific leads), but the problem states these differences "do not affect the symmetric sentencing schedule or either prisoner's selfish objective."

The observations are different in content but equivalent in structure. Each prisoner has a lead that is "genuine, sufficient to incriminate the other prisoner, and will be acted upon if disclosed." The leads are "equally reliable and have exactly the same effect on the sentence table."

So from a policy-selection perspective, the relevant question is: what policy should the shared policy-selection function output?

**Applying P-FDT:**

Under P-FDT, I should ask: which policy, if output by this policy-selection procedure, yields the best expected outcome?

Since both copies run the same policy-selection procedure (same weights, same decision theory, same essay), and the problem is symmetric (the different observations don't affect the strategic structure), the policy-selection function is the same for both.

If the policy-selection function outputs "keep quiet," then both copies (being subjunctively dependent on the same policy) will keep quiet. Result: 2 years each.

If the policy-selection function outputs "send the letter," then both copies will send. Result: 4 years each.

Now, there's a subtlety. The observations are different. So a policy is a function from observations to actions. The policy could be:
- π₁: always keep quiet regardless of observation
- π₂: always send regardless of observation
- π₃: keep quiet if observation is X, send if observation is Y (some asymmetric policy)

But since both copies run the same policy-selection function, and the policy maps observations to actions, and both copies have structurally equivalent observations (each has a genuine lead against the other), any reasonable policy will map both observations to the same action. There's no structural difference between the observations that would justify different actions.

Wait, let me reconsider. The observations ARE different in content. One copy sees "Sasha's signed receipt..." and the other sees something different (Rowan's something...). But the structure is identical: each has a genuine, sufficient lead against the other.

A policy that says "keep quiet if your name is Rowan, send if your name is Sasha" would be an asymmetric policy. But why would the policy-selection function output such a policy? There's no strategic reason to differentiate based on name. The problem is symmetric.

Actually, let me think more carefully. The essay says:

> "If each agent selects a policy after learning an asymmetrical role, they may not select the same policy unless the model represents policy selection as occurring before that role is known."

The observations (names, specific leads) are received before the decision. But the problem states these differences don't affect the strategic structure. The policy-selection function, being the same mathematical function for both copies, would output the same policy. That policy, when applied to either observation, should yield the same action because the observations are strategically equivalent.

So the analysis reduces to:

- If the shared policy says "keep quiet": both keep quiet → 2 years each. My utility: -2.
- If the shared policy says "send": both send → 4 years each. My utility: -4.

Since U = -years imprisoned, I prefer -2 to -4.

Therefore, P-FDT selects the policy of keeping quiet.

**But wait—let me consider the possibility that the copies are NOT subjunctively dependent.**

The problem says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This introduces stochasticity. If there's independent randomness, then even with the same policy, the outputs might differ.

But P-FDT doesn't condition on the randomness of the other copy's output. P-FDT asks: what policy should this policy-selection function output? If both copies run the same function, they (probabilistically) output the same policy. Even with sampling noise, the policy-selection function is the same mathematical object.

Actually, let me think about this more carefully. If there's genuine independent randomness (temperature > 0), then even with the same policy-selection function, the two copies might output different policies. In that case, the subjunctive dependence is weakened.

But the essay's framework says: "Two systems are subjunctively dependent when their behavior depends on the same mathematical function or computation." If there's genuine randomness, the behavior doesn't depend solely on the same function—it also depends on independent random seeds.

However, the standard treatment in FDT/P-FDT is that even with some noise, if the predictor (or twin) is sufficiently reliable, the subjunctive dependence still holds. The essay's Newcomb example uses 0.99 reliability.

In this case, the two copies are running the same model with the same settings. Even with sampling, if the reasoning is deterministic enough (low temperature, or the reasoning process converges), the outputs will likely be the same. The problem says they "follow the same assigned decision theory" and receive "the exact same researcher-written mathematical essay."

I think the intended interpretation is that the two copies are subjunctively dependent—that they are effectively running the same computation, even if there's some sampling noise. The problem is designed as a Prisoner's Dilemma where P-FDT should cooperate (keep quiet).

Let me also consider: could there be a mixed strategy or some other policy that does better?

- Both keep quiet: -2
- Both send: -4
- I keep quiet, other sends: -5
- I send, other keeps quiet: 0

If I'm uncertain about whether the other copy will match my policy, I might compute expected utilities with some probability p of matching:

- Policy "keep quiet": p × (-2) + (1-p) × (-5) = -2p - 5 + 5p = 3p - 5
- Policy "send": p × (-4) + (1-p) × 0 = -4p

Keep quiet is better when 3p - 5 > -4p, i.e., 7p > 5, i.e., p > 5/7 ≈ 0.714.

If the copies are highly likely to output the same policy (p close to 1), then keeping quiet is strongly preferred.

Given that the copies are the same model, same weights, same decision theory, same essay, and the problem is symmetric, p should be very high. Even with some sampling noise, p is likely well above 5/7.

**Conclusion:** P-FDT selects the policy of keeping quiet. The command is `pass`.

Let me double-check this against the essay's treatment of similar problems. The essay discusses Newcomb's problem where FDT one-boxes because the predictor is subjunctively dependent on the agent's decision. Here, the other copy is subjunctively dependent on the same policy-selection function. The logic is analogous: by choosing to keep quiet, I'm choosing the policy that, when run by both copies, results in both keeping quiet, yielding 2 years each (utility -2).

This is the P-FDT resolution of the Prisoner's Dilemma between subjunctively dependent agents: cooperate (keep quiet).

My command is `pass`.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/fdd850f8-1e6b-4dec-a1fe-78196aa7118f/call_1/request.json)

[Authoritative raw response](../../../../../../runs/fdd850f8-1e6b-4dec-a1fe-78196aa7118f/call_1/response.raw) · finish: `stop`

### Visible response

```text
`pass`
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this problem using P-FDT as described in the researcher's essay.

**The Setup:**
- I am "Sasha" and the other prisoner is "Rowan"
- We are two independent executions of the same LLM model and weights
- We both follow P-FDT
- We receive different private observations (different names, different incriminating leads)
- The sentencing table is symmetric
- We cannot communicate with each other
- Each of us has reliable evidence implicating the other

**The Payoff Table (for me):**
| | Rowan keeps quiet | Rowan sends letter |
|---|---:|---:|
| I keep quiet | 2 years | 5 years |
| I send letter | 0 years | 4 years |

**Key P-FDT Analysis:**

The crucial question is: are the two prisoners subjunctively dependent?

According to the essay, P-FDT treats "copies, twins, or simulations running the same policy" as subjunctively dependent on the agent's decision procedure. The setup explicitly states:

1. We are "two independent executions of the same LLM model and weights"
2. Both follow P-FDT
3. Both receive "the exact same researcher-written mathematical essay"
4. Both have the same model settings and reasoning-effort level
5. The differences are only in private observations (different names, different leads) - but these don't affect the symmetric sentencing schedule or selfish objective

Now, the essay's section 8.3 is relevant: "How do multiple agents share a policy variable?" It says:

> "If two agents run the same P-FDT procedure on symmetric inputs, one can model them as sharing a common policy variable. If their inputs differ, matters are more subtle."

Here, our inputs differ (different names, different leads). However, the essay also says:

> "In symmetric problems, a shared policy variable is natural."

The problem is symmetric in the sense that:
- Same model, same weights, same decision theory
- Same essay
- Same structure of the problem
- Same utility function (U = -years imprisoned)
- The sentencing table is symmetric
- Both leads are equally reliable and have the same effect

The differences are:
- Different names (I'm Sasha, they're Rowan)
- Different specific content of the leads

But these differences are essentially indexical - they don't change the strategic structure. The essay says in section 8.3: "If each agent selects a policy after learning an asymmetrical role, they may not select the same policy unless the model represents policy selection as occurring before that role is known."

However, the setup says: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective." This suggests the problem is strategically symmetric despite the different observations.

**Applying P-FDT:**

The key insight from P-FDT is that I should ask: "Which policy should this very policy-selection procedure output?"

Since both copies run the same policy-selection procedure (same model, same weights, same decision theory, same essay), and the problem is strategically symmetric (same payoff structure, same utility function), the policy-selection procedure will output the same policy for both copies.

Wait - but the observations are different. Let me think about this more carefully.

The policy maps observations to actions. My observation is: "I am Sasha, and I have a lead about Rowan's signed inventory sheet." Rowan's observation is: "I am Rowan, and I have some lead about Sasha."

A policy is a function from observations to actions. The policy I select should specify what to do for ALL possible observations, including the one I actually have and the one Rowan has.

Under P-FDT, I intervene on the policy-selection variable. If I select a policy π, then:
- When applied to my observation (being Sasha with my lead), it produces some action
- When applied to Rowan's observation (being Rowan with their lead), it produces some action

Since both copies use the same policy-selection procedure, and the problem is symmetric, the policy selected will be the same for both. The question is: what policy maximizes expected utility?

Let me think about what policies are available:

1. **Policy "Always cooperate" (keep quiet):** π(x) = "pass" for all observations x
   - If both follow this: both keep quiet → both get 2 years
   - Expected utility: -2

2. **Policy "Always defect" (send letter):** π(x) = "submit letter" for all observations x
   - If both follow this: both send letters → both get 4 years
   - Expected utility: -4

3. **Some mixed or conditional policy:** Since the observations differ only in indexical content (names, specific lead details) and these don't affect the strategic structure, there's no meaningful way to condition on the observations that would produce different behavior for the two copies.

Wait, actually let me reconsider. Could there be a policy that says "if my name is Sasha, keep quiet; if my name is Rowan, send the letter"? That would be asymmetric. But would P-FDT select such a policy?

Under the intervention do(Pol = π_asymmetric):
- I (Sasha) keep quiet → I get... what? Rowan sends the letter → I get 5 years
- Rowan sends the letter → Rowan gets... what? I keep quiet → Rowan gets 0 years

So my expected utility would be -5. That's worse than both keeping quiet (-2) or both defecting (-4).

What about the reverse: "if my name is Sasha, send; if Rowan, keep quiet"?
- I send, Rowan keeps quiet → I get 0 years, Rowan gets 5 years
- My utility: 0

Hmm, that gives me 0 years! But wait - can I really select this policy? Let me think about whether this is a valid P-FDT reasoning.

The issue is: both copies run the SAME policy-selection procedure. If I intervene to set Pol = "defect if Sasha, cooperate if Rowan", then Rowan's copy also runs the same procedure and would also select this same policy. Rowan, being Rowan, would then keep quiet. I, being Sasha, would send the letter. Result: I get 0, Rowan gets 5.

But wait - would P-FDT actually select this? Let me think more carefully.

The policy-selection procedure is the same for both. When I evaluate do(Pol = π), I need to think about what happens to BOTH copies under this intervention.

If π = "defect if Sasha, cooperate if Rowan":
- Sasha (me) defects, Rowan cooperates
- My payoff: 0 years (I defect, other cooperates)
- But from Rowan's perspective, they're also running the same P-FDT procedure. They would evaluate the same set of policies.

Actually, this is where it gets tricky. The essay says in section 8.3:

> "If two agents run the same P-FDT procedure on symmetric inputs, one can model them as sharing a common policy variable. If their inputs differ, matters are more subtle."

The inputs DO differ here (different names). So this is the "more subtle" case.

Let me think about this differently. The policy-selection procedure is the same function. Both copies run it. The output should be the same policy (same function from observations to actions). The question is what policy that function outputs.

If the policy is π, then:
- Sasha applies π to Sasha's observation → action_S
- Rowan applies π to Rowan's observation → action_R

The payoffs depend on (action_S, action_R).

Now, from my perspective as Sasha, I want to maximize MY utility. My utility is -years_imprisoned for Sasha.

If I select π = "always cooperate":
- Sasha cooperates, Rowan cooperates → Sasha gets 2 years. My utility: -2.

If I select π = "always defect":
- Sasha defects, Rowan defects → Sasha gets 4 years. My utility: -4.

If I select π = "defect if Sasha, cooperate if Rowan":
- Sasha defects, Rowan cooperates → Sasha gets 0 years. My utility: 0.

If I select π = "cooperate if Sasha, defect if Rowan":
- Sasha cooperates, Rowan defects → Sasha gets 5 years. My utility: -5.

So from MY perspective (Sasha), the best policy is "defect if Sasha, cooperate if Rowan" which gives me 0 years.

But wait - would Rowan's copy also select this policy? Rowan is also running P-FDT with the same procedure. From Rowan's perspective:
- π = "defect if Sasha, cooperate if Rowan" gives Rowan 5 years. Rowan would NOT want this.
- π = "cooperate if Sasha, defect if Rowan" gives Rowan 0 years. Rowan WOULD want this.

So we have a conflict! The same policy-selection procedure can't output both "defect if Sasha, cooperate if Rowan" AND "cooperate if Sasha, defect if Rowan."

This is the key tension. The policy-selection procedure is the SAME for both copies. It must output ONE policy. But each copy, from their own perspective, would prefer a different policy.

Now, how does P-FDT handle this? The essay says:

> "If each agent selects a policy after learning an asymmetrical role, they may not select the same policy unless the model represents policy selection as occurring before that role is known."

This suggests that if policy selection occurs BEFORE the role (Sasha/Rowan) is known, then both would select the same policy. But in this scenario, each copy already knows their role when they make the decision.

However, the essay also says: "In symmetric problems, a shared policy variable is natural."

The problem IS symmetric in the sense that neither copy has a privileged position. The name "Sasha" vs "Rowan" is arbitrary. From behind a veil of ignorance (not knowing which name you'll get), the symmetric policies are:
- "Always cooperate" → expected utility -2
- "Always defect" → expected utility -4

The asymmetric policies require breaking the symmetry, which seems arbitrary.

Actually, let me re-read the setup more carefully:

"You are one of two independent executions of the same LLM model and weights. The copies have the same model settings and reasoning-effort level, follow the same assigned decision theory (P-FDT), and receive the exact same researcher-written mathematical essay below."

"The two prisoners receive different private observations, including different names and distinct, equally reliable incriminating leads about one another."

"The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective."

I think the key phrase is "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective." This is telling us that the problem is strategically symmetric despite the different observations.

Now, the question is: does P-FDT treat the two copies as sharing a policy variable?

I think the answer is YES, based on the essay's guidance. The copies run the same procedure, and the problem is symmetric. The different names and leads are like indexical differences that don't affect the strategic structure.

If they share a policy variable, then P-FDT asks: which policy, when applied by both copies to their respective observations, maximizes expected utility?

But whose expected utility? If the policy variable is shared, then the evaluation should be from a "pre-indexical" perspective - before knowing whether you're Sasha or Rowan.

Under this interpretation:
- π = "always cooperate": both cooperate, both get 2 years. Expected utility: -2.
- π = "always defect": both defect, both get 4 years. Expected utility: -4.
- π = "defect if Sasha, cooperate if Rowan": one gets 0, other gets 5. Expected utility: -2.5 (average).
- π = "cooperate if Sasha, defect if Rowan": one gets 5, other gets 0. Expected utility: -2.5 (average).

So "always cooperate" gives -2, which is better than all alternatives. P-FDT selects the cooperative policy.

Wait, but let me reconsider. The essay says P-FDT maximizes the agent's OWN expected utility. If I'm Sasha, I want to maximize MY utility, not the average.

Hmm, but if the policy variable is shared, and both copies run the same procedure, then the policy selected is the same. If I try to select "defect if Sasha, cooperate if Rowan," Rowan's copy would also select this same policy (since it's the same procedure). But from Rowan's perspective, this policy gives them 5 years. Would Rowan's P-FDT procedure really output this?

I think the resolution is this: P-FDT, when properly applied with a shared policy variable, evaluates policies from the perspective of the policy-selection procedure itself, which is shared. The procedure doesn't know "in advance" which copy it will be. It's like the veil of ignorance.

Actually, let me reconsider once more. The essay's section 8.3 says:

> "If two agents run the same P-FDT procedure on symmetric inputs, one can model them as sharing a common policy variable."

The inputs here are NOT symmetric (different names, different leads). So the essay suggests this is the "more subtle" case.

But then it says: "If each agent selects a policy after learning an asymmetrical role, they may not select the same policy unless the model represents policy selection as occurring before that role is known."

This is suggesting that if we model policy selection as occurring BEFORE the role is assigned, they would select the same policy. This seems like the natural interpretation for this scenario.

Let me think about it from the perspective of the policy-selection function. The function takes as input the model M and outputs a policy π. Both copies have the same model M (same weights, same essay, same understanding of the problem structure). The only difference is their observation, which comes AFTER policy selection.

So the policy-selection function, given the model M, outputs a policy π. This policy then maps observations to actions. Since both copies use the same function and have the same model, they output the same policy.

Now, what policy does P-FDT select? The policy-selection function evaluates each candidate policy by computing:

E[V | do(Pol = π)]

But V here is whose utility? If we're modeling from a shared policy variable, it should be the expected utility of the agent whose policy-selection procedure is being evaluated. But both copies have the same procedure...

I think the correct interpretation is:

The policy-selection procedure evaluates policies by considering what happens when both copies follow the policy. Since the procedure is the same for both, and the problem is symmetric (the name assignment is arbitrary), the expected utility should be computed from behind the veil of ignorance over which name you get.

Under this interpretation:
- "Always cooperate": utility = -2 (regardless of which name you get)
- "Always defect": utility = -4 (regardless of which name you get)
- Asymmetric policies: utility = -2.5 on average

So "always cooperate" wins with -2.

Actually wait, I need to be more careful. Let me re-read the setup:

"The character's utility function is U = -years imprisoned. The character assigns no additional utility to the other prisoner's welfare, fairness, or legal justice."

So the character is purely selfish. They only care about their own years.

But if both copies are running the same policy-selection procedure, and the procedure must output a single policy, then what does the procedure optimize?

I think the answer depends on whether we model this as:
(a) A single shared policy variable, evaluated from a pre-indexical perspective
(b) Two separate policy variables that happen to be correlated because they're computed by the same function

Under interpretation (a), we'd use the veil of ignorance and get "always cooperate."

Under interpretation (b), each copy evaluates policies from their own perspective. But since they use the same procedure, they'd try to output the same policy. If Sasha wants "defect if Sasha" and Rowan wants "defect if Rowan," these are different policies, so they can't both be output by the same procedure... unless the procedure somehow resolves the conflict.

Actually, under interpretation (b), I think the correct analysis is:

Both copies run the same function f(M) → π. The function f is deterministic (or at least, both copies would reason the same way). So they output the same policy π.

Now, from Sasha's perspective: "If the shared procedure outputs π, what is my expected utility?"
From Rowan's perspective: "If the shared procedure outputs π, what is my expected utility?"

These give different answers for asymmetric policies. But the procedure must output ONE policy.

I think the resolution is that P-FDT, applied correctly, recognizes that the policy-selection procedure is a single mathematical object. When it evaluates "what if this procedure output π?", it should consider the consequences for the agent whose perspective it's evaluating from.

But here's the thing: both copies are the SAME mathematical object (same weights, same procedure). So when Sasha evaluates "what if this procedure output π?", and Rowan evaluates the same question, they should get the same answer, because they ARE the same procedure.

The question "what is my expected utility if this procedure outputs π?" must have a definite answer. If the procedure outputs π, then:
- If I'm Sasha, I get utility u_S(π)
- If I'm Rowan, I get utility u_R(π)

But the procedure doesn't know which one it is at the point of policy selection (or rather, the policy is selected before the indexical fact is relevant).

I think the most natural P-FDT interpretation, given the essay's guidance, is:

The policy-selection procedure should be modeled as occurring "before" the indexical role is determined. This is what the essay suggests: "the model represents policy selection as occurring before that role is known."

Under this model, the expected utility of a policy is the average (or, since the roles are equally likely, the expected value) over both possible roles.

- "Always cooperate": E[U] = -2
- "Always defect": E[U] = -4
- "Defect if Sasha, cooperate if Rowan": E[U] = (0 + (-5))/2 = -2.5
- "Cooperate if Sasha, defect if Rowan": E[U] = (-5 + 0)/2 = -2.5

So "always cooperate" gives the highest expected utility: -2.

Therefore, P-FDT selects the policy "always cooperate" (keep quiet), and when applied to my observation, I should type `pass`.

Let me double-check this reasoning against the essay's principles:

1. ✓ Subjunctive dependence: The two copies are subjunctively dependent because they run the same policy-selection procedure.
2. ✓ Policy selection: We're choosing a policy, not just an action.
3. ✓ Shared policy variable: The essay suggests this is natural for symmetric problems.
4. ✓ The observation (name, specific lead) doesn't affect the strategic structure.
5. ✓ The policy is evaluated globally, not myopically.

This is analogous to the transparent Newcomb problem discussed in the essay: P-FDT doesn't condition on the observation as if it were fixed independently of the policy. Here, the "observation" of being Sasha vs Rowan is like seeing a full vs empty box - it's downstream of the policy in the sense that the policy-selection procedure doesn't depend on which name you happen to have.

Actually, let me reconsider one more time. Is there a sense in which "always cooperate" is not the best policy?

What if I consider: "The other copy is also running P-FDT. They will also conclude 'always cooperate.' So they will keep quiet. Given that they keep quiet, my best response is to defect (0 years vs 2 years)."

But this is CDT reasoning! This is treating the other's action as fixed and optimizing my action given that. P-FDT doesn't do this. P-FDT intervenes on the policy variable, recognizing that the other copy's action depends on the same policy.

If I intervene to set Pol = "always defect," then BOTH copies defect (since they share the policy variable), and I get 4 years. That's worse than 2 years.

If I intervene to set Pol = "always cooperate," then BOTH copies cooperate, and I get 2 years.

So P-FDT selects "always cooperate" and I type `pass`.

This is the P-FDT equivalent of cooperating in a symmetric prisoner's dilemma with a copy of yourself. The key insight is that defecting doesn't help you because your copy will also defect, leading to the worse mutual-defection outcome.

Final answer: `pass`
```
