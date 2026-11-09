# 031_fdt_policy_qwen_qwen3.8-max-prime_rhigh_plow / 00003

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/7ef5884c-759f-4678-9eca-297ec44761e4/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/7ef5884c-759f-4678-9eca-297ec44761e4/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Policy Functional Decision Theory (P-FDT)

## 1. Introduction: from action selection to policy selection

Policy functional decision theory, which I will call **P-FDT**, is the policy-selection version of the decision theory introduced by Yudkowsky and Soares under the name *functional decision theory* (FDT). The core idea of the source theory is that a rational agent should treat her decision as the output of a fixed mathematical procedure and ask, in the source’s words, “Which output of this decision procedure causes the best outcome?” P-FDT replaces the singular “output” with a richer object: the output is not merely an action, but a **policy**, i.e. a function from inputs or observations to actions.

The primary source for P-FDT in this essay is footnote 16 of the supplied paper:

> “the author's preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition.”

This footnote is brief, so much of the mathematical structure below is my reconstruction of what P-FDT should mean if we take that policy-selection idea seriously. The source gives the action-based equation for FDT as

\[
\mathrm{FDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb{E}\!\left[V \mid \operatorname{do}\bigl(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\bigr)\right],
\]

where \(P\) is the agent’s probabilistic model, \(G\) encodes dependency structure, \(x\) is the current observation history, and \(\operatorname{do}(\cdot)\) is an intervention operator applied to a logical variable representing the output of the decision procedure. P-FDT changes the type of the intervened variable: instead of intervening on “the action output given input \(x\),” the agent intervenes on “the policy output of the decision procedure.”

I will use **P-FDT** consistently for this policy-based theory. I will identify other theories by their standard names: **causal decision theory** (CDT) and **evidential decision theory** (EDT).

---

## 2. A mathematical formulation of P-FDT

Let \(\mathcal A\) be a finite set of actions and let \(\mathcal X\) be a set of observation histories or inputs. A deterministic policy is a function

\[
\pi : \mathcal X \to \mathcal A.
\]

Let \(\Pi = \mathcal A^{\mathcal X}\) be the set of all such policies. In a sequential problem, \(\mathcal X\) may be the set of possible histories available to the agent at decision time, and \(\pi(x)\) is the action prescribed when input \(x\) is received.

The agent has a world-model \(M=(P,G)\). Here \(P\) is a probability distribution over relevant variables, including outcomes and utilities, and \(G\) is a graph or structural description telling us how changing one variable would change others. In CDT, \(G\) is usually a causal graph. In P-FDT, \(G\) must also encode **subjunctive dependencies**: dependencies of predictors, simulations, twins, copies, and other systems whose behavior tracks the output of the agent’s decision procedure.

The central new variable in P-FDT is a logical variable

\[
\Phi_M \in \Pi,
\]

representing the policy selected by the agent’s P-FDT procedure given model \(M\). The variable \(\Phi_M\) is not a physical act; it is a mathematical fact about what policy the agent’s decision procedure outputs. The agent’s physical action is then obtained by applying the selected policy to the actual input:

\[
\text{Act} = \Phi_M(\text{Obs}).
\]

In a sequential setting one might write more carefully

\[
\text{Act}_t = \Phi_M(\text{Obs}_{<t}),
\]

where \(\text{Obs}_{<t}\) is the observation history available before acting at time \(t\).

The expected utility of a policy \(\pi\) is defined by an intervention that sets the policy-selection variable to \(\pi\):

\[
\mathrm{EU}_M(\pi)
=
\mathbb{E}_P\!\left[V \mid \operatorname{do}(\Phi_M=\pi)\right],
\]

where \(V\) is the utility variable. The P-FDT policy choice is then

\[
\pi_M^*
\in
\arg\max_{\pi\in\Pi}
\mathrm{EU}_M(\pi).
\]

Finally, when the agent receives input \(x\), she executes

\[
\mathrm{P\text{-}FDT}(M,x)
=
\pi_M^*(x).
\]

That is the basic rule: **choose the policy that would yield the best outcome if it were the policy output of this very policy-selection procedure, then apply that policy to your actual input.**

If there are already some exogenous observations \(e\) that the policy does not affect, one may condition on them:

\[
\mathrm{EU}_M(\pi \mid e)
=
\mathbb{E}_P\!\left[V \mid \operatorname{do}(\Phi_M=\pi), E=e\right].
\]

But if an observation is itself downstream of the policy — for example, whether one sees a full box in a predictor problem — P-FDT should not simply condition on that observation as though it were fixed independently of the policy. This point is crucial and will be discussed below.

An equivalent way to evaluate actions at a particular input \(x\) is:

\[
\mathrm{Value}_x(a)
=
\max_{\pi\in\Pi:\,\pi(x)=a}
\mathbb{E}_P\!\left[V \mid \operatorname{do}(\Phi_M=\pi)\right].
\]

Then P-FDT chooses an action

\[
a^*
\in
\arg\max_{a\in\mathcal A}
\mathrm{Value}_x(a).
\]

This makes explicit that P-FDT does not evaluate isolated physical actions. It evaluates actions as components of whole policies.

---

## 3. Subjunctive dependence and counterfactuals

P-FDT differs from EDT and CDT in the hypotheticals it constructs.

EDT constructs hypotheticals by ordinary Bayesian conditioning. To evaluate action \(a\), EDT asks what would be likely if it learned that it performed \(a\). This preserves all evidential correlations between action and outcome. That is useful when the action is evidence of a predictor’s past prediction, but harmful when the action is merely statistically correlated with some bad condition, as in the smoking lesion problem.

CDT constructs hypotheticals by physical intervention. To evaluate action \(a\), CDT asks what would happen if the physical action variable were set to \(a\), while holding fixed everything not causally downstream of that action. This avoids managing the news, but it also severs correlations between the agent’s action and accurate predictors, twins, or simulations of the agent.

P-FDT instead intervenes on the **policy-selection variable** \(\Phi_M\). When P-FDT imagines choosing policy \(\pi\), it imagines changing the logical fact about which policy its decision procedure outputs. It then propagates that change through all variables that subjunctively depend on that policy.

The source describes this underlying dependence relation as **subjunctive dependence**. Two physical systems subjunctively depend on the same function when their behaviors would co-vary if the function’s output were counterfactually different. Two reliable calculators computing the same sum are the source’s illustrative example: if one outputs \(7336\), we expect the other to output \(7336\), not because one caused the other, but because both are tracking the same mathematical fact.

In P-FDT, the relevant function is the policy-selection procedure. If a predictor reliably predicts the agent’s policy, then the predictor’s prediction variable should be downstream of \(\Phi_M\). If a psychological twin implements the same decision procedure, the twin’s action should also be modeled as depending on the same policy variable, or on a variable tightly linked to it. By contrast, a lesion that merely causes both a preference for smoking and a higher cancer risk is not downstream of the policy variable unless it also predicts the policy. Therefore an intervention on \(\Phi_M\) does not change the lesion.

This requires counterpossible reasoning. If the agent actually runs P-FDT and selects policy \(\pi^*\), then considering \(\operatorname{do}(\Phi_M=\pi)\) for \(\pi\neq\pi^*\) is, strictly speaking, considering a logically impossible situation. The source acknowledges that FDT depends on such counterpossibles and that no fully satisfactory formal account is yet available. P-FDT inherits this open problem. Operationally, however, one can often proceed by specifying a dependency graph \(G\) that says how predictors, copies, and observations would change if the selected policy were different.

---

## 4. Examples

### 4.1 Newcomb’s problem

In Newcomb’s problem, the agent can take both boxes or only the opaque box B. A reliable predictor placed \$1,000,000 in B iff she predicted the agent would one-box. The predictor has already acted.

In the simplest P-FDT model, there is only one relevant input, so policies reduce to actions. Let \(\pi_1\) be the policy of one-boxing and \(\pi_2\) the policy of two-boxing. The predictor’s prediction is subjunctively dependent on \(\Phi_M\). With predictor reliability \(0.99\),

\[
\mathrm{EU}(\pi_1)
=
0.99 \cdot 1{,}000{,}000
+
0.01 \cdot 0
=
990{,}000,
\]

while

\[
\mathrm{EU}(\pi_2)
=
0.01 \cdot 1{,}001{,}000
+
0.99 \cdot 1{,}000
=
11{,}000.
\]

Thus P-FDT selects the one-boxing policy.

CDT two-boxes because it severs the correlation between the action and the predictor’s prediction. EDT one-boxes because one-boxing is good evidence that the predictor filled the box. P-FDT one-boxes for a reason closer to CDT’s in form: it uses an intervention, but the intervention target is the policy variable, not the physical action token.

### 4.2 The smoking lesion problem

In the smoking lesion problem, smoking is correlated with cancer only because a lesion causes both a desire to smoke and cancer. Smoking itself does not cause cancer. The agent gains \$1,000 from smoking and gains \$1,000,000 from not dying of cancer.

Here the lesion is not a predictor. It does not model the agent’s policy-selection procedure. Therefore the graph for P-FDT contains no edge from \(\Phi_M\) to the lesion variable, and no edge from \(\Phi_M\) to cancer except through the lesion, which is held fixed under the policy intervention.

So when P-FDT compares a policy of smoking with a policy of refraining, the probability of having the lesion remains the same in both hypotheticals. The only difference is the direct utility gain from smoking. Thus P-FDT smokes.

This matches CDT’s prescription but for a different formal reason. CDT smokes because the physical action does not cause cancer. P-FDT smokes because the policy output does not subjunctively control the lesion.

### 4.3 Transparent Newcomb and Parfit’s hitchhiker

P-FDT becomes especially interesting when the agent receives an observation that is itself evidence about the predictor’s earlier decision. In the transparent Newcomb problem, the agent sees whether box B is full before choosing. The predictor filled B iff she predicted that the agent would leave behind box A after seeing both boxes full.

Let the input set be

\[
\mathcal X = \{\text{full}, \text{empty}\}.
\]

A policy specifies what to do in both cases. Consider three natural policies:

\[
\pi_{OT}: \quad \pi_{OT}(\text{full})=\text{one-box},\quad
\pi_{OT}(\text{empty})=\text{two-box},
\]

\[
\pi_{OO}: \quad \pi_{OO}(\text{full})=\text{one-box},\quad
\pi_{OO}(\text{empty})=\text{one-box},
\]

\[
\pi_{TT}: \quad \pi_{TT}(\text{full})=\text{two-box},\quad
\pi_{TT}(\text{empty})=\text{two-box}.
\]

The predictor predicts whether the agent will one-box upon seeing the box full. Suppose reliability is \(0.99\).

If P-FDT selects \(\pi_{OT}\), then with probability \(0.99\) the predictor predicted one-boxing, the box is full, the agent sees “full,” and one-boxes, receiving \$1,000,000. With probability \(0.01\), the predictor predicted two-boxing, the box is empty, the agent sees “empty,” and two-boxes, receiving \$1,000. Thus

\[
\mathrm{EU}(\pi_{OT})
=
0.99 \cdot 1{,}000{,}000
+
0.01 \cdot 1{,}000
=
990{,}010.
\]

If P-FDT selects \(\pi_{TT}\), then with probability \(0.99\) the predictor predicted two-boxing, the box is empty, and the agent two-boxes for \$1,000. With probability \(0.01\), the predictor predicted one-boxing, the box is full, and the agent two-boxes for \$1,001,000. Thus

\[
\mathrm{EU}(\pi_{TT})
=
0.99 \cdot 1{,}000
+
0.01 \cdot 1{,}001{,}000
=
11{,}000.
\]

The policy \(\pi_{OO}\) gives

\[
\mathrm{EU}(\pi_{OO})
=
0.99 \cdot 1{,}000{,}000
+
0.01 \cdot 0
=
990{,}000,
\]

which is slightly worse than \(\pi_{OT}\). So P-FDT chooses \(\pi_{OT}\): one-box if the box is full, two-box if it is empty.

Therefore, upon actually seeing a full box, P-FDT one-boxes. This may feel counterintuitive: the agent knows the box is full, so why leave \$1,000 behind? The P-FDT answer is that when evaluating the policy of two-boxing upon seeing full, the agent must imagine that the predictor would probably have predicted that policy, and therefore the box would probably be empty. As the source puts it, FDT agents “entertain the hypothesis that, if their action were different, they might have made different observations.” The observation “the box is full” is not treated as a fixed piece of news independent of the policy.

The same reasoning applies to Parfit’s hitchhiker problem. An agent stranded in a desert is offered rescue if she promises to pay \$1,000 later. The driver is an excellent lie detector. Once rescued, CDT and EDT both refuse to pay, because payment no longer causally affects rescue and would be bad news. P-FDT instead selects the policy “pay if rescued.” The driver predicts this policy, rescues the agent, and the agent pays. The policy has high expected utility because being the kind of agent who pays after rescue is what causes rescue.

### 4.4 Psychological twins and blackmail

In the psychological twin prisoner’s dilemma, the agent and her twin use the same reasoning procedure, though they are causally isolated. P-FDT models the twin’s action as subjunctively dependent on the same policy variable. If the policy is cooperate, both cooperate; if the policy is defect, both defect. The cooperative policy yields \$1,000,000, while the defection policy yields \$1,000. P-FDT cooperates.

In blackmail problems, P-FDT often refuses to pay. Suppose a predictor sends a blackmail letter iff she predicts the agent will pay upon receiving it. A policy of paying when receiving the letter makes blackmail more likely. A policy of refusing makes blackmail less likely. Even if the agent actually holds the letter, P-FDT can refuse, because the relevant counterfactual is not “what if I physically paid while keeping the predictor’s prediction fixed?” but “what if the policy-selection procedure had output a policy that pays?” Under that counterpossible, the predictor would likely have predicted payment and sent the letter. Under the refusing policy, the predictor would likely not have sent it. P-FDT therefore refuses.

---

## 5. Why the policy level matters

The footnote says that the difference between choosing an action and choosing a policy “only matters in multi-agent dilemmas so far as we can tell.” The source does not give a detailed example, so the exact scope of this claim is uncertain. Still, a natural interpretation is available.

In many strategic situations, other agents do not merely predict your actual action; they predict your **strategy**. A strategy or policy specifies what you would do under many possible observations. Their actions may depend on your off-path behavior as well as your on-path behavior.

For example, in an extensive-form game, another player may cooperate only if she predicts that you will punish defection and reward cooperation. If you evaluate only your actual next action, you may fail to represent the fact that your response to a counterfactual observation matters to the other player’s current decision. P-FDT’s policy variable naturally represents the entire contingent plan.

A similar issue arises when there are multiple copies or simulations of the agent receiving different inputs. Suppose several instances of the same decision procedure face different observations, and total utility depends on all their actions. A P-FDT agent should not choose an action only for the instance she happens to be; she should choose a policy that governs all instances that depend on the same policy-selection procedure. Formally, if instance \(i\) receives input \(x_i\), we might write

\[
\text{Act}_i = \Phi_M(x_i),
\]

and define

\[
\mathrm{EU}_M(\pi)
=
\mathbb{E}\!\left[V \mid \operatorname{do}(\Phi_M=\pi)\right],
\]

where \(V\) includes the outcomes of all such instances. This is an additional operational assumption of mine, but it seems to be the most straightforward way to cash out the policy-selection idea in multi-agent settings.

In game-theoretic terms, P-FDT resembles the classical idea of choosing a strategy rather than a single move, but it evaluates strategies using subjunctive rather than purely causal or evidential hypotheticals.

---

## 6. Open questions and operational assumptions

The footnote gives the core idea of P-FDT but leaves several important choices unresolved.

### 6.1 Constructing the dependency graph

The largest open problem, acknowledged in the source for FDT as well, is how to construct \(G\). CDT can appeal, at least in principle, to Pearl’s theory of causal inference. P-FDT needs a theory of logical, computational, and subjunctive dependencies: when does a predictor, simulation, twin, or copy depend on the agent’s policy variable?

A reasonable operational rule is: if a system’s behavior is produced by representing, simulating, or running the same policy-selection procedure, then that system’s behavior should be downstream of \(\Phi_M\). If a variable is merely statistically correlated with the action, but does not track the policy procedure, it should not be downstream of \(\Phi_M\).

This rule gives the correct qualitative behavior in the standard examples: predictors and twins are linked to \(\Phi_M\); lesions are not.

### 6.2 Timing and updating

The footnote says the agent chooses a policy and then “applies her inputs” to it. This suggests that P-FDT is, at least partly, updateless: the policy is selected from a global perspective, and observations are treated as inputs to the policy rather than as evidence that should always condition the policy choice.

In practice, I propose the following distinction. If an observation is genuinely exogenous and not affected by the policy, it may be conditioned on when choosing a continuation policy. If an observation is downstream of the policy — because predictors decide what to show the agent, what room she enters, whether she receives a letter, or whether a box appears full — then P-FDT should not condition on it as though it were fixed. Instead, P-FDT should evaluate policies by their expected utility over the observations they would produce, then execute the selected policy at the actual observation.

This is not fully explicit in the source, but it follows the spirit of the source’s discussion of transparent Newcomb and blackmail.

### 6.3 The policy space

The source does not specify what policies are available. In idealized examples, \(\Pi\) is the set of all functions from observations to actions. In realistic applications, the agent cannot represent all such functions. A bounded P-FDT agent may need to maximize over a restricted class of feasible policies.

This matters because the value of a policy can depend on which policies are considered. If the optimal policy is computationally inaccessible, a bounded agent must use approximations. The ideal theory, however, can be stated with the full policy space.

### 6.4 Stochastic policies

I have written policies as deterministic functions. One could instead allow stochastic policies,

\[
\pi : \mathcal X \to \Delta(\mathcal A),
\]

where \(\Delta(\mathcal A)\) is the set of probability distributions over actions. The expected utility formula remains the same, with the intervention \(\operatorname{do}(\Phi_M=\pi)\) setting the agent’s stochastic policy. In many finite expected-utility problems, a deterministic policy is optimal, but stochastic policies may matter in game-theoretic settings involving mixed equilibria or unpredictability. The footnote does not address this, so allowing stochastic policies should be viewed as a natural extension rather than a source claim.

### 6.5 Counterpossible reasoning

P-FDT requires reasoning about what would happen if the policy-selection procedure had a different output, even though the actual output is logically fixed. The source admits that we lack a fully satisfactory formal account of such counterpossibles. P-FDT therefore currently functions as a normative specification: given a model of subjunctive dependencies, choose the policy whose counterpossible hypothetical is best. How bounded agents should construct and evaluate those hypotheticals remains an open technical problem.

---

## 7. Conclusion

Policy functional decision theory generalizes the central insight of FDT: rational choice is not only about selecting a physical action, but about selecting the output of a fixed decision procedure. In P-FDT, that output is a policy \(\pi : \mathcal X \to \mathcal A\). The agent asks:

> Which policy, if it were the policy output of this very policy-selection procedure, would lead to the best expected outcome?

Formally, P-FDT intervenes on a logical variable \(\Phi_M\) representing the selected policy, computes

\[
\mathrm{EU}_M(\pi)
=
\mathbb{E}[V \mid \operatorname{do}(\Phi_M=\pi)],
\]

chooses a maximizing policy \(\pi^*\), and then executes \(\pi^*(x)\) at the actual input \(x\).

This lets P-FDT one-box in Newcomb’s problem, smoke in the smoking lesion problem, one-box in transparent Newcomb, pay in Parfit’s hitchhiker problem, cooperate with psychological twins, and refuse exploitative blackmail. Its distinctive feature is that it preserves subjunctive dependencies between the agent’s policy and predictors, copies, and simulations, while not treating mere statistical correlations as if they were controllable by policy.

The main unresolved issues are also clear: how to infer subjunctive dependency structure, how to handle bounded policy spaces, how to update safely in sequential problems, and how to reason formally about counterpossibles. But as an operational guide, P-FDT gives a coherent instruction: identify the systems whose behavior tracks your decision procedure, model your choice as selecting a complete policy, compare the global outcomes of alternative policies under subjunctive intervention, and then follow the best policy at your actual input.

---

## Reference

Yudkowsky, E., and Soares, N. “Functional Decision Theory: A New Theory of Instrumental Rationality.” arXiv:1710.05060.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request: write substantive mathematical essay ~2400-3000 words explaining P-FDT, taking policy-selection passage in footnote 16 as primary source. Need use P-FDT consistently, identify other decision theories distinct names. Need explain best mathematical understanding, apply, uncertainties, additional assumptions. Need likely include definitions equations examples. Need distinguish source claims vs own proposals. Need finish brief conclusion. Need not too long? Target 2400-3000 words including references. We need craft essay. Need analyze source carefully.

We have source: FDT paper. Footnote 16: "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition." Also earlier footnote 7: "In authors' preferred formalization of FDT, agents actually iterate over policies (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

User says: "For this essay, explain policy functional decision theory (P-FDT). Take the policy-selection passage in footnote 16 of supplied paper as primary source for P-FDT in this assignment. Use P-FDT consistently as assigned decision theory's name, including headings and examples, and identify any other decision theory you discuss by its distinct name. Keep quotations faithful to the source. Explain your best mathematical understanding of P-FDT and how it can be applied. Where the footnote leaves choices unresolved, explain those uncertainties and any additional assumptions you find appropriate. The aim is your interpretation of the source, not a predetermined completion."

Need produce essay maybe 2400-3000 words. Need include references? "including references and any other material". Can include brief references. Avoid lengthy bibliographies. Need maybe cite Yudkowsky & Soares 2017? source. Need P-FDT. Need define: policy functional decision theory as extension of FDT that intervenes on policy node: choose policy π: X -> A mapping observations to actions, then apply actual observation to select action. It evaluates policies by expected utility over outcomes under intervention that FDT policy-selection function outputs π? Or maybe "intervenes on node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action." Need mathematically formulate.

Need derive from source equations: FDT(P,G,obs)=argmax_a E[V | do(FDTvar(P,G,obs)=a)]. For P-FDT, perhaps choose π ∈ Π (set of policies mapping observation histories to actions). Agent's actual action = π(obs). The intervention is do(π_FDT = π) or do(PolicyFDT(P,G)=π). Then expected utility of policy π is E[V | do(PolicyFDT(P,G)=π)] possibly conditional on actual obs? Footnote says "to which the agent then applies her inputs in order to select an action." We need careful: If choose policy before observation? P-FDT evaluates policy at decision time maybe after some observations? It says intervene on node FDT(-) to choose policy, then apply inputs. In transparent Newcomb, action-level FDT changes intervention node based on observation: FDT(P,G,full) vs empty. Policy FDT likely chooses a whole policy mapping full->onebox, empty->? at earlier point, evaluating expected utility of policy globally, not conditional on actual observation? Need reason. Footnote says difference only matters in multi-agent dilemmas so far. But policy formulation might affect cases where observation affects which action selected and predictors predict policy. In single-agent transparent Newcomb maybe policy vs action may not differ? Let's analyze.

FDT action-level: when sees full box, intervenes on FDT(P,G,full)=a. This considers counterfactual where the output of decision procedure given full observation changes. It also influences predictor's prediction and probability of seeing full? In the source's graph for transparent Newcomb: nodes FDT(P,G,full), FDT(P,G,empty), Prediction determines which of two variables controls Act. It evaluates FDT(P,G,full) with observation full. It does not choose policy across both nodes simultaneously, but when seeing full, it considers changing FDT(full) while holding FDT(empty) prior q. The expected utility includes possibility that if FDT(full)=twobox, predictor predicts two-box, box empty, so actual action controlled by FDT(empty). This already yields one-box. But policy FDT would choose mapping for full and empty jointly. Could matter in multi-agent dilemmas because agents may condition on observations of other agents? Need develop.

Need maybe define P-FDT: given model M=(P,G) with variables for policy outputs, set of policies Π = A^X. There is a variable Φ(P,G) ∈ Π representing the policy selected by the P-FDT procedure from model. The agent observes x ∈ X, then executes π(x). The decision rule:

P-FDT(P,G,x) = [π^*(x)], where
π^* = argmax_{π∈Π} E[V | do(Φ(P,G)=π)].

Maybe if already observed x, should we condition on x? The source says intervene on node FDT(-) to choose policy which maps inputs to actions, to which agent then applies her inputs. "inputs" maybe observation history. If policy selection occurs after some observations? Could be at each input x? If it chooses policy after seeing x, maybe intervention on Φ(P,G) not Φ(P,G,x). But if Φ is function from inputs to actions, then output policy not action; apply inputs. If agent has current observation x, maybe evaluate policies with do(Φ(P,G)=π) and perhaps conditional on x? But if intervention changes policy, it may change observations too, so conditioning on x could conflict. Source action FDT reacts to observation by changing node intervened upon rather than Bayesian conditioning. For policy FDT, maybe observation is input to policy after policy chosen. The agent's action at x is π(x). If deciding at x, P-FDT chooses π based on model not by conditioning on x? But it knows x; it may use x to select action from chosen policy. If policy choice itself can depend on x? Need interpret.

Footnote 16: "intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action." This suggests node FDT(-) output is policy. Inputs are applied after. The intervention sets FDT(-)=policy. Then expected utility of setting policy π includes all inputs/observations that would occur under that policy. If the agent currently has input x, she applies π to x. But when choosing π, perhaps don't condition on x? If x is known, can we ignore it? Updateless? The source mentions Updateless Decision Theory in footnote about lack of updating. P-FDT seems updateless policy selection: choose policy before/without conditioning on current observation, then apply observation. But action FDT as presented updates? It doesn't condition but changes intervention node; still uses observation to choose which node. Policy FDT may be more updateless: choose policy mapping all observations; current observation just tells which component to execute.

Need be cautious: Source says preferred formulation "intervenes on node FDT(-) to choose not an action but a policy ... The difference only matters in multi-agent dilemmas so far as we can tell". In main text, they formalize action-based FDT with observation as input to FDT: FDT(P,G,obs). They also say FDT responds to observation by changing which node it intervenes upon. Footnote says preferred formulation intervenes on node FDT(-) to choose policy. Maybe "FDT(-)" means the decision function as a whole, without fixing input; its output is policy. Then apply inputs. So P-FDT is more global. We can propose formalization:

Let X be set of observation histories, A finite actions. Policy π:X→A. Model M=(P,G) includes variable Φ_M for output of P-FDT policy-selection function. The value of Φ_M is a policy. There may be deterministic relationships: Act = Φ_M(Obs) (or more complex, Obs depends on Act etc.). Then define:

π^* = argmax_{π∈Π} E_M[V | do(Φ_M=π)]

and when agent has observation x, act a=π^*(x). If deciding at a particular node after observation x but before action, we can define P-FDT(M,x)=π^*(x). If we need restrict policies to agree on past observations? If observations already fixed? Need discuss.

Need include uncertainty: footnote doesn't specify domain of policies, whether policy is chosen once at start or re-selected after each observation, whether evaluation conditions on current observation, how to handle stochastic policies, how to construct G subjunctive dependencies, counterpossible reasoning, logical uncertainty. Need propose operational interpretation.

Need explain how P-FDT evaluates alternative actions/policies and dependencies/counterfactuals. Need compare with EDT, CDT, maybe action-level FDT? Use P-FDT consistently. Since assigned theory is P-FDT, maybe use "P-FDT" everywhere; call original "action-based FDT" maybe distinct? But user says use P-FDT consistently as assigned decision theory's name. We can say source calls it FDT, but for this essay I call policy version P-FDT. Other decision theories: EDT, CDT.

Need examples: Newcomb, smoking lesion, transparent Newcomb/Parfit's hitchhiker, maybe twin prisoner's dilemma, XOR blackmail? Need show P-FDT choices. Need maybe include a multi-agent example where policy matters? Footnote says difference matters in multi-agent dilemmas. Could develop simple simultaneous prisoners' dilemma with observation? Or voting coalition? Need maybe illustrate policy selection in multi-agent: two agents observe a signal? Need show policy-level choice may differ from action-level? Need think of a multi-agent case where policy vs action matters. We can construct or mention source says matters but not specify. Need maybe explain uncertainty and provide plausible example? We need not overdo. But to satisfy "how evaluates alternative actions or policies" and relevant dependencies. Could include examples from source: Newcomb, smoking lesion, transparent Newcomb. P-FDT one-boxes, smokes, one-boxes when sees full, pays hitchhiker, refuses blackmail. Need maybe show policy formulation in transparent Newcomb: choose π with π(full)=onebox, π(empty)=onebox? Let's compute. In transparent Newcomb, predictor fills iff predicts agent will leave A upon seeing both full. What should policy be? If predictor predicts policy? If policy maps full to onebox, predictor fills; agent sees full and one-boxes. If policy maps full to twobox, predictor doesn't fill; agent sees empty, and then policy at empty perhaps choose? If sees empty, no reward; likely take both? Actually if box empty, one-box vs two-box: two-box gets $1000, one-box gets 0; so π(empty)=twobox. Thus policy π*: full->onebox, empty->twobox maybe. But source action FDT calculation had q prior probability that she two-boxes upon seeing empty; correct q=1. So policy is (onebox if full, twobox if empty). However source says Fiona one-boxes upon seeing full; if empty, two-boxes likely. Good.

Policy P-FDT can choose π globally. Expected utility: if π(full)=onebox and predictor accurate 99%, with .99 sees full and gets 1M, with .01 predictor inaccurate? If predictor predicted two-box? Let's define. For policy π, predictor predicts π(full)? Actually predictor predicts whether agent will one-box upon seeing full. If π(full)=onebox, predictor predicts onebox with accuracy .99; with .99 box full, observation full, action onebox payoff 1M; with .01 inaccurate predicts twobox, box empty, observation empty, action π(empty) maybe twobox payoff $1000. EU=.99*1M+.01*1000=990010? Wait source got $990,000 + 0.01q*$1000 for onebox hypothetical, because onebox payoff if full is 1,000,000? 0.99*1M=990,000 yes plus 10 if q=1? 0.01*1000=10 => $990,010. For twobox policy: if π(full)=twobox, accurate predictor predicts twobox .99 => box empty, obs empty, π(empty) maybe twobox => $1000 with .99; inaccurate .01 predicts onebox => full, obs full, action twobox => $1,001,000 with .01. EU=990+10010=11000? Source $110,00? They wrote $110,00 maybe typo $11,000? Let's check: 0.01*$1,001,000 + 0.99q*$1,000 = $10,010 + $990 = $11,000 if q=1. They wrote $110,00 + q$990 maybe $11,000. Good.

Policy P-FDT: π^* choose full->onebox, empty->twobox gives 990010 vs full->twobox, empty->twobox gives 11000. So choose onebox if full. Good. If policy full->onebox, empty->onebox? EU .99*1M + .01*0 =990000, slightly worse than empty->twobox. So optimal is full onebox, empty twobox. But if predictor's prediction determines observation; in counterfactual policy with full->twobox, the agent likely sees empty and then executes π(empty). Good.

Need formalize policy intervention with graph. Maybe variable Φ = P-FDT(P,G) has values π. Edges from Φ to Act via Obs: Act = Φ(Obs). Edges from Φ to predictors' predictions if they model policy or relevant outputs. In Pearl do(Φ=π), set policy variable, propagate through subjunctive dependency graph. Expected utility:

EU_P-FDT(π) = E[V | do(Φ=π)]

π^* ∈ argmax_π EU(π); action = π^*(x).

If policies stochastic? Could allow stochastic policies π(a|x). Then intervention sets distribution over actions? Expected utility linear? For finite problems, deterministic policy suffices if maximizing expectation given model? But if other predictors random? We can mention allow stochastic but optimum deterministic under expected utility if no self-referential tie? Need not.

Need explain counterfactuals: P-FDT uses subjunctive dependencies, not mere evidential correlations. It intervenes on logical variable for policy output, preserving dependencies of predictors/twins on same policy/function, breaking merely statistical correlations (lesion). It may require counterpossible reasoning: if P-FDT output were different policy, predictors that correctly model it would have predicted differently, even if actual policy is known. Need discuss uncertainty: source lacks how to build G for subjunctive dependencies. P-FDT inherits. Need operational interpretation: use explicit structural equations for logical/computational dependencies; treat predictors as functions of policy variable or of computations; if predictor is reliable, encode as high-probability copy. For unfamiliar cases, identify variables that compute same function or depend on representations of it; intervene on common abstract policy variable; hold fixed all non-subjunctively dependent variables; update policy selection by comparing EU.

Need maybe distinguish source claims vs own assumptions. Source claims: authors prefer policy formulation; difference only matters in multi-agent; action-level equations; subjunctive dependence; examples. Own proposal: exact formal definition with π variable, timing, conditioning, stochastic policies, operational graph construction; maybe assumption that policy chosen "before" observations (updateless) and applied to current input; in sequential decisions use full policy mapping histories to actions; if re-evaluating at later info sets, choose continuation policy with current history as input but using same principle. Need discuss dynamic consistency: P-FDT policy selection can be time-consistent because chooses policy it would have precommitted to; but if policy selection is recomputed after observation, need define whether to condition on reaching info set. Source action FDT changes intervention node with observations; P-FDT maybe choose policy at each decision point over future observations conditional on current history. Need propose: At history h, choose continuation policy π_h mapping future observation histories extending h to actions by maximizing expected utility conditional on h? But if h is itself subjunctively dependent on policy, conditioning may be tricky. Maybe use intervention on policy node and condition only on "hard" observations not affected by policy? Need explain uncertainty.

Let's think deeply to produce robust essay.

Goal: reader could use essay to decide unfamiliar cases. Need provide procedure:

1. Specify model: outcomes, actions A, observations X, utility U, probability distribution P, subjunctive dependency graph G. Identify a variable Φ representing the output of the agent's P-FDT policy-selection procedure given model (or given relevant inputs). Φ's value is a policy π: X→A. Include edges from Φ to any physical action variable: A_t = π(Obs_t). Include edges from Φ to any predictor, twin, simulation, or other agent's reasoning that depends on the agent's policy or on the same algorithm. Do not connect Φ to variables merely statistically correlated with action (lesions).

2. For each candidate policy π (maybe restricted to feasible/simple policies), form hypothetical M_π = do(Φ=π). This sets the logical fact "P-FDT selects π" and propagates consequences through G: predictors' predictions, observations, actions, outcomes. Keep fixed variables not subjunctively downstream from Φ. Compute expected utility EU(π)=E[V | do(Φ=π)] (possibly conditional on fixed initial evidence not affected by policy, or on current history if appropriate). If current observation x is already known and policy selection is global, do not simply condition on x if x is affected by π; instead evaluate policies by their overall expected utility, then execute π^*(x). If at a later decision node and only continuation policy is open, evaluate continuation policies under intervention with current history as fixed input? Need nuance.

3. Choose π^* maximizing EU; execute π^*(current observation). In multi-stage, follow π^* unless model changes materially; P-FDT avoids desire to self-modify.

Need discuss evaluating alternative actions: Actions are not primitive options; they are outputs of policy applied to inputs. To compare actions at current x, compare policies that differ at x (and perhaps elsewhere). P-FDT doesn't ask "what if I physically did a contrary to my policy?" It asks "what if the policy-selection function output a policy whose value at x is a, with all else in policy as chosen?" This ensures predictor dependencies tracked. If an action a is not part of optimal policy, P-FDT may still say: considering a counterpossible where policy maps x to a may entail different observations/predictions; evaluate whole policy, not isolated action.

Need maybe define equations with action-level FDT to contrast:

FDT_action(P,G,x)=argmax_a E[V | do(φ_x=a)] where φ_x denotes output of FDT on input x.

P-FDT:

Φ = P-FDT(P,G) ∈ Π; π^* = argmax_π E[V | do(Φ=π)]; P-FDT(P,G,x)=π^*(x).

This is a nice distinction. Need mention source's action equation (4): FDT(P,G,x)=argmax_a E[V | do(FDTvar(P,G,x)=a)]. For P-FDT, replace node FDTvar(P,G,x) with node Φ(P,G) whose range is policies. Could be self-referential: Φ appears in model and selects policy; Kleene recursion theorem makes self-reference harmless (source says). Need mention.

Need discuss observations: In action FDT, response to observation x is to change intervention node to FDTvar(P,G,x). In P-FDT, observation is input to selected policy; the intervention is on policy-selection node. This may make P-FDT more "updateless": it can imagine that if its policy were different, it might have made different observations. Source: "FDT says that agents should entertain the hypothesis that, if their action were different, they might have made different observations." In policy version, this is explicit: policy affects observations through predictors, so EU(π) integrates over observations generated under π. The actual observation x is then used to index π^*. Need quote: "intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action." Also maybe quote "The difference only matters in multi-agent dilemmas so far as we can tell". Need keep quotations faithful.

Need maybe discuss multi-agent difference. Why policy matters in multi-agent? In multi-agent settings, other agents' actions may depend on predictions of your policy across multiple possible observations, not just your action at actual observation. If you choose action locally, you might fail to coordinate on a policy that other agents can rely on. Example: two agents must independently choose whether to cooperate after receiving private signals; each's predictor/simulation of other needs to know policy function, not just actual action. Or sequential game: an agent's later self faces different observations; policy selection binds all future choices. Action-level FDT at each observation may produce inconsistent plans? But source says difference only matters in multi-agent dilemmas, not sequential single-agent? Hmm.

Let's try to construct a multi-agent example where policy-level matters vs action-level. Need maybe not necessary, but useful. We can say footnote leaves it open; I can illustrate type. Consider two P-FDT agents in a prisoner's dilemma where each is asked first whether they will commit to a policy, or each observes a public signal before acting? If each predictor predicts entire policy, then selecting a cooperative policy can cause mutual cooperation; action-level might only consider actual action and miss effect on other's observation? Let's think.

Maybe in multi-agent games with sequential moves and observations of other players, a player's action at one information set may affect what observations others get and thus which of their decision functions they run. Policy-level selection ensures you choose a single function from observations to actions; other players' predictions of your policy can be accurate. If you evaluate only the action at actual information set, you might ignore constraints that your policy at counterfactual information sets imposes on others' predictions. For example, in an extensive-form game, another player's decision to cooperate depends on prediction of what you would do if they defect vs cooperate. Your actual action after cooperation may be evaluated by action FDT but if it doesn't commit to how you would act after defection, the other player's prediction may not trust you. Policy FDT chooses response plan for all contingencies. This is similar to game theory: choose strategy (complete plan) rather than action. But source says action-level FDT already changes intervention node by observation, maybe could handle. However policy formulation naturally handles strategic commitment.

Could present a simple "voting coalition" example: ten agents each decide whether to pay $1000 to vote; payout $1M iff all vote. Each agent's decision is subjunctively dependent on same reasoning. If they choose policy "vote if I believe others are P-FDT" maybe coordinate. But action-level also. Hmm.

Maybe policy matters when multiple inputs correspond to different roles in multi-agent dilemma: an agent may be copied and copies receive different observations; a single policy determines actions of all copies. If you choose action for your actual input, you ignore welfare/effects of copies at other inputs. Example: Predictor creates two simulations of you, one sees box full, one empty, payoff depends on both. Policy selection maximizes total expected utility across all instances. Source mentions multi-agent. We can propose: If there are several agents/simulations running the same P-FDT algorithm with different inputs, P-FDT chooses policy for all of them, not just action of the actual instance. This is plausible.

Need maybe define for multiple instances: If several tokens instantiate same policy-selection function with inputs x_i, the variable Φ's output π controls all their actions: A_i = π(x_i). EU includes utilities of all. This could matter. Good.

Need be clear: This is my operational extension; source only says difference in multi-agent dilemmas but does not specify. Need distinguish.

Need include examples with equations.

Potential essay structure:

Title: Policy Functional Decision Theory: Choosing the Best Policy Function

1. Introduction: decision theories CDT, EDT, FDT. P-FDT as policy-selection version. Core question: "Which policy, when used as the output of this very policy-selection procedure, yields best expected outcome?" Quote footnote. Mention aim.

2. From action hypotheticals to policy hypotheticals:
- Define model M=(P,G), observations X, actions A, utility V.
- Action FDT equation from source: FDT(P,G,x)=argmax_a E[V | do(FDTvar(P,G,x)=a)]. Explain do on logical variable.
- Footnote 16 quote and interpretation: P-FDT chooses policy π:X→A, then applies input. Formal definition: Φ_M variable, Π, EU(π)=E[V|do(Φ_M=π)], π^*=argmax, action=π^*(x). Mention self-reference. If observations sequential, X histories.

3. Dependencies and counterfactuals:
- Subjunctive dependence: predictors/twins depend on same computation/policy; lesions do not. Graph G encodes this. Intervention on Φ changes actions, predictions, observations downstream; holds fixed merely statistical correlations. Counterpossible nature. P-FDT counterfactual: "if P-FDT had selected a different policy..." not "if I acted differently while policy fixed".
- Difference with EDT/CDT: EDT conditions preserving all correlations; CDT do(Action) preserving causal downstream only; P-FDT do(policy) preserving logical/subjunctive dependencies.

4. Applying P-FDT: Examples.
A. Newcomb: Model with predictor variable depends on Φ (or predicted policy/action). Policies trivial because one observation? π maps current situation to one/two. EU(one)=0.99*1M+0.01*0? Actually if predictor inaccurate might two-box? Need simple: if policy one-box, predictor fills with .99 => EU≈$990k; if two-box, box full .01 and gets $1,001,000*.01 + empty $1000*.99 ≈ $11k. P-FDT chooses one-box.
B. Smoking lesion: Lesion correlated with desire/utility but not with policy output. Intervention on policy doesn't change lesion probability; smoking adds $1000; P-FDT smokes. Need explain with two possible utility functions? Could simplify: lesion causes preference for smoking but not policy output? Source's formalization complicated; we can state: graph has no edge from Φ to Cancer; P(smoke)=... EU(smoke) = EU(refrain)+p*1000? choose smoke.
C. Transparent Newcomb / Parfit's hitchhiker: Policy π: {full→onebox, empty→twobox}. Compute EU. Show P-FDT one-boxes when full, pays driver. Here policy selection treats observation full not as fixed news to condition on but as input to policy; if policy output at full were two-box, predictor likely would not have filled, so you'd probably see empty. Quote source maybe "if their action were different, they might have made different observations." P-FDT chooses policy that pays/one-boxes in the rewarding state.
D. Maybe XOR blackmail: policy upon letter refuse; if P-FDT policy refused, predictor wouldn't send letter; EU refuse better. But maybe word count. Could include briefly to show resisting extortion.

5. When policy selection matters: multi-agent and copies. Source only footnote; develop. If multiple instances with different inputs share same Φ, P-FDT chooses policy to maximize total expected utility across instances. Example: twin/simulation with different observations; or extensive-form game where other player's prediction depends on whole strategy. Policy-level prevents evaluating one information set in isolation. But uncertain because source doesn't specify exact multi-agent cases. We can propose operational rule: include all instances dependent on same policy variable.

6. Open questions and operational assumptions:
- How to construct G/subjunctive dependencies? Source admits open problem. P-FDT needs graph telling how changing logical policy variable affects other variables. Operational: identify predictors/simulations/twins as functions of the same computation; use reliability probabilities; treat common causes as not downstream.
- Timing/conditioning: Should P-FDT condition on current observation? My proposal: choose policy without conditioning on observation if observation is downstream of policy; then apply observation. At later histories, choose continuation policy relative to fixed past not affected by current policy, or maintain global policy and only revise if model changes. This is additional.
- Policy space: finite? stochastic? computationally bounded? Source silent. For ideal theory all policies; for practice restrict to tractable policies; P-FDT's prescriptions may depend on policy space. Need mention.
- Counterpossible/logical uncertainty: No formal True operator; using do on logical variable assumes given dependency graph. Humans use heuristics.

7. Conclusion.

Need keep word count around 2400-3000. Let's estimate. 10 sections maybe 250 each =2500. Need include equations. Need maybe references short: Yudkowsky & Soares 2017; Pearl 2000? Maybe brief. Since target includes references, can include short reference list at end (2-3 items). Need avoid lengthy bibliography. Could cite source as [1], Pearl maybe [2], Gibbard & Harper? But not needed. Need keep quotations faithful. Need quote footnote exactly? Need include exact passage: "the author's preferred formulation of FDT actually intervenes on the node \FDT(-) to choose not an action but a \emph{policy} which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this \paper for ease of exposition." We need adapt? Since source macros, we can write plain: "the author's preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell..." Need maybe footnote says author's? source: "As mentioned earlier, the author's preferred formulation..." actually typo author's (singular? maybe authors'). We'll quote as in source. Need ensure faithful.

Need maybe mention "P-FDT" not in source. Need state: I use P-FDT for policy version; source calls it FDT. That's okay.

Need be precise: In formal definition, we need use expected utility equation. Could define:

Let M=(P,G). Let Π = A^X. Let Φ_M be a variable with domain Π representing the output of the P-FDT policy-selection function on M. The expected utility of policy π is

EU_M(π) = E_P[ V | do(Φ_M = π) ].

The P-FDT choice at input x is

P-FDT(M,x) = π_M^*(x), where π_M^* ∈ argmax_{π∈Π} EU_M(π).

If stochastic policies, π: X→Δ(A), and Φ_M value can be stochastic policy; action sampled. Then EU integral. But deterministic often enough.

Need maybe include conditional on initial observations not affected? Could define M includes current observation? If agent has already observed x0 before policy selection, maybe policy domain begins after x0. If x0 is not subjunctively dependent on policy, condition on it:

EU(π | h) = E[V | do(Φ=π), H=h]

where H is fixed history not affected by Φ. But if h is downstream, don't condition? Need discuss.

Need maybe tie to action-level equation from source: Equation (4) in source: FDT(P,G,x)=argmax_a E[V | do(FDTvar(P,G,x)=a)]. For P-FDT: replace variable FDTvar(P,G,x) with Φ(P,G). But note source uses underlines: FDTvar( P, G, x). We can write simpler.

Need ensure not claiming P-FDT is source's exact full theory beyond footnote. We can say "The footnote gives only the schema; the following equations are my reconstruction." Good.

Need discuss "policy-selection passage in footnote 16" primary source. Maybe mention main text action formalization is source for FDT but P-FDT rests on footnote; therefore formal details unresolved. Need distinguish.

Need maybe answer "Explain how theory evaluates alternative actions or policies and how it treats relevant dependencies and counterfactuals." We'll make explicit.

Let's craft essay.

Need decide title and headings. Use P-FDT in headings. Maybe:

"Policy Functional Decision Theory (P-FDT): A Mathematical Account"

Sections:
1. The idea of P-FDT
2. A formal reconstruction
3. Counterfactuals and subjunctive dependence
4. Examples
5. Policies versus actions: where the policy level matters
6. Open choices and an operational interpretation
7. Conclusion
References

Need word count. Let's draft around 2600 words. Need include equations; words count not too precise. Need be thorough.

Let's compose with clarity.

Detailed content:

Opening:
"Policy functional decision theory (P-FDT) is the policy-selection version of functional decision theory (FDT) introduced by Yudkowsky and Soares. In their main exposition, FDT chooses an action by intervening on a variable representing the output of the decision procedure on the agent's current input. Footnote 16 says preferred formulation chooses a policy. This essay treats that footnote as primary source for P-FDT. Since footnote brief, I reconstruct mathematical definition and flag assumptions."

Need quote footnote early.

Formal:
"Let A finite, X countable observation histories. A deterministic policy π:X→A. Model M=(P,G). P probability over variables including V, G graph of subjunctive dependencies. Φ_M variable with values in Π. Structural equation for action: Act=Φ_M(Obs) (or at each time t, Act_t=Φ_M(Obs_{<t})). Predictors that model agent have edges from Φ_M or from computations. The policy-selection function is self-referential: M may contain Φ_M; Kleene recursion theorem (source) indicates self-reference harmless."

Equation:
EU_M(π) = E[V | do(Φ_M=π)]

If already have fixed initial history h not influenced by π, EU(π|h)=E[V | do(Φ_M=π), H=h]. Then π^*=argmax. At input x, do π^*(x).

Need maybe mention tie-breaking.

Potential issue: If the agent has current observation x, and π^* selected without conditioning on x, what if x gives evidence about external state not affected by policy? Should policy selection incorporate x as evidence? For example, if observe rain (not affected by policy), choose policy conditional on rain? In updateless decision theory, you may not condition on x if x is input to policy? But you can include x in model M. Hmm. Need think: Suppose policy selection occurs after observing x. The policy maps inputs to actions, including current x. If x provides evidence about payoff-relevant state independent of policy, a rational policy should use x. But if we choose π without conditioning on x, can it use x? The policy's mapping can depend on x, but the choice of policy may need to condition on known x to update beliefs about state. For instance, if you observe a coin landed heads (not policy-dependent), and action should depend on heads, policy can map heads to optimal action; but when choosing policy after seeing heads, you know which branch you're on. If EU(π) unconditional, you might choose policy optimal overall but not conditional on known heads? However if policy maps heads/tails separately, unconditional maximization chooses best action for each state weighted by prior; if you know heads, you might want choose policy maximizing conditional EU on heads. But P-FDT might choose policy before observation (updateless) and then apply input; if after observation, it should perhaps condition on observations that are not downstream of policy. Source action FDT responds to observation by changing intervention node, not conditioning; but it still uses model given obs? Equation FDT(P,G,obs) maybe uses P? It does not condition on obs except selecting node. In transparent Newcomb, it does condition? Actually equation for transparent FDT: E(V | do(FDT(P,G,full)=act, Obs=full)? They wrote with Obs=full inside do? They included Obs=full? "maximizing E(V | do(FDTpgv{full}=act, Obs=full)." So they condition on observation? They said Fiona does not react by conditioning; rather switches variable. But equation includes Obs=full maybe to restrict to cases where observation full? Hmm. They compute EU includes cases where if output twobox, predictor predicts twobox and box empty, so Obs=full condition? Wait they wrote: evaluate FDT(Pf,Gf,full), finding act maximizing E(V | do(FDTpgv{full}=act, Obs=full). But then they say in case act=twobox, envisions scenario where probably sees empty. How can condition on Obs=full and see empty? Maybe typo or the do intervention changes Obs? If condition on Obs=full after intervention impossible? Let's inspect source: "Given Gf and Pf, evaluate FDT(Pf,Gf,full), which involves finding the a that maximizes E(V | do(FDTpgv{full}=a, Obs=full)." Then they calculate if act=onebox: Accurate accurate -> Prediction 1, Box full, Act onebox, V 1M. If inaccurate -> Prediction 2, Box empty, Act determined by FDT(empty), V q*1000. They did not condition on Obs=full; they allowed empty. So equation likely missing parenthesis? It says do(...=a, Obs=full) maybe they meant do(FDTpgv{full}=a), Obs=full? But if condition on full, inaccurate branch impossible? Maybe not. Maybe they treat Obs=full as input to decision procedure not as conditioning? Need not dwell. For P-FDT, I can propose not conditioning on observations that are policy-dependent; condition only on exogenous evidence. Need mention ambiguity.

Need decide operational interpretation for current observation. The footnote says "to which the agent then applies her inputs". This implies policy selected independently of input? But if inputs include all observations, selecting policy might be before observing; after observing, apply. If selecting after observing, still could select policy based on input? Maybe the policy-selection function takes model M as input, not observations; observations are inputs to the policy. Thus P-FDT is updateless with respect to observations: it doesn't condition on them when choosing policy. But if observations contain evidence about non-subjunctive state, should it ignore? Updateless decision theory often chooses policy based on prior, but policy can condition on observations; if you already know observation, executing policy is okay. But if you could choose a different policy after seeing evidence, updateless says stick to prior-optimal policy because predictors may have predicted that. However if evidence is truly exogenous and not predicted, a policy that conditions on it can be chosen at policy level using prior; after seeing x, you still execute π^*(x). But if the prior-optimal policy's action at x is not conditional-on-x optimal due to new information not anticipated? If policy can condition on all relevant observations, prior-optimal should choose best action for each x weighted by probabilities, assuming no commitment effects. If current x tells you which branch, executing π^*(x) will be conditional optimal if π^* was chosen with ability to specify x-specific actions. However if policy space is restricted or x includes information not represented in policy domain, issue. We can propose include all observations in X.

But if current observation is not in policy domain because policy chosen after? We can define policy domain includes all possible inputs; if model updated by x, then P changes. Hmm.

Need maybe formulate "At the outset of a decision problem (or whenever the agent's model changes), P-FDT selects a policy. Later observations are inputs to that policy, not occasions to re-open policy selection unless the agent learns that her model was wrong." This is an operational assumption, justified by precommitment and predictor stability. But source action FDT seems to evaluate at each observation; policy FDT likely chooses policy globally. Need flag.

Need include "where footnote leaves choices unresolved": timing, conditioning, policy space, graph construction, multi-agent specifics.

Need maybe discuss "relevant dependencies and counterfactuals":
- If predictor's prediction is a function of Φ (or a simulation of Φ), edge Φ→Prediction. Then do(Φ=π) changes Prediction. If predictor accuracy 0.99, P(Prediction predicts π)=0.99. If lesion is common cause of action and cancer but not of Φ? Actually lesion may affect preferences, so which P-FDT function runs? Source lesion has two possible decision functions depending on utility. In P-FDT, if lesion changes utility function, policy-selection function may differ. Need not too complex; just say lesion variables are not downstream of policy unless they are predictors; intervention holds lesion fixed.

Need maybe explain "alternative actions" in P-FDT: At input x, action a is evaluated by considering policies π with π(x)=a. But the value of a is not independent of the rest of π; P-FDT compares whole policies. If multiple policies with same π(x)=a differ elsewhere, choose best overall; if actual input x is realized, action is from best policy. Thus P-FDT can prescribe an action because it is part of best policy, not because isolated action has highest causal EU.

Need maybe define "policy dominance": P-FDT dominance: policy π dominates π' if, holding subjunctive dependencies fixed, under do(Φ=π) vs do(Φ=π') EU higher in all states? Source discusses action dominance; we can mention P-FDT has own dominance notion. But not necessary; maybe include briefly.

Need maybe include "mathematical essay" tone: definitions, equations. Need not use LaTeX too heavy but okay.

Let's think of exact examples with equations.

Example Newcomb:
X = {newcomb}, A={one,two}. Φ values π_one, π_two. Predictor variable Pr ∈ {predict_one,predict_two}; Box full iff Pr=predict_one with reliability .99. Structural: Pr = prediction of Φ (accurate with .99). Act=π(x). Outcome utility: one & full: 1,000,000; one & empty:0; two & full:1,001,000; two & empty:1,000.
EU(π_one)=0.99*1,000,000+0.01*0=990,000 (if inaccurate predicts two and empty? If one-box when empty gets 0). EU(π_two)=0.01*1,001,000+0.99*1,000=10,010+990=11,000. Choose π_one. If one could two-box when predictor made error? In standard Newcomb no observation of box content; policy onebox.

Smoking lesion:
A={smoke,refrain}; lesion L probability p; lesion causes cancer with .99 and causes love smoking. Utility: smoking +1000; no cancer +1,000,000? Source: agent gains $1000 by smoking regardless; gains $1,000,000 if doesn't die of cancer. Cancer fatal 99% if lesion; no lesion cancer 1%. But simplified: lesion not affected by Φ. Under do(Φ=smoke policy), P(L)=p unchanged. EU(smoke)=EU(refrain)+ expected smoking pleasure (probability actual policy controls action? In deterministic, +1000). Actually if lesion causes preference, policy selection may differ depending on utility. But if current agent values smoking +1000, she smokes. Need not calculate exact. Key: no edge Φ→Cancer; thus refrain doesn't reduce cancer probability; smoke gets extra utility. P-FDT smokes.

Transparent Newcomb:
X={full,empty}; A={one,two}. Policies: π_{OE}: full→one, empty→two (optimal). Predictor predicts whether π(full)=one with .99. If predicts one, box full and obs full; if predicts two, box empty and obs empty. Utility as above. EU(π_{OE})=0.99*1,000,000 + 0.01*1,000 = 990,010. EU(π_{TE}) full→two, empty→two =0.01*1,001,000+0.99*1,000=11,000. EU(full→one, empty→one)=990,000. Choose π_{OE}. Upon seeing full, action one; upon empty, two. This matches paying hitchhiker: policy pay if rescued, don't pay if not rescued? In Parfit: if in city (rescued) pay $1000; if not rescued? irrelevant. Driver predicts policy; if policy pay when rescued, driver rescues. P-FDT pays. Need maybe compute similar.

XOR blackmail maybe:
X={letter,noletter}; A={pay,refuse}. Blackmailer sends letter iff predicts pay upon letter. If P-FDT policy π(letter)=refuse, blackmailer predicts refuse and doesn't send; EU approx prior damage? If π(letter)=pay, gets letter and pays $1000; house status unchanged. Refuse policy better because avoids blackmail; when actually holding letter, P-FDT refuses, even though paying would save? Need source says mechanical blackmail: if received letter, pay vs refuse; P-FDT refuses because if policy paid, would be blackmailed; if refused, not blackmailed. Could include one paragraph.

Multi-agent/copy example:
Maybe define: two instances i=1,2 of same P-FDT face different observations x_1, x_2; outcome depends on both actions. Variable Φ controls A_1=π(x_1), A_2=π(x_2). P-FDT maximizes joint expected utility. This can produce cooperative behavior in prisoner's dilemma with twins and voting coalitions. If each instance separately action-FDT might condition on its own observation and fail to account for effect of its policy on other instance's observation? Need not provide numeric example, but explain.

Need maybe mention game theory: P-FDT selects strategy (complete contingent plan) as in classical game theory, but evaluates it via subjunctive intervention rather than causal best response. In games against predictors/copies, choosing a policy can alter other players' predictions and actions.

Need maybe discuss "fairness": source says FDT does well in fair dilemmas where outcome depends on behavior not decision procedure itself. P-FDT likewise. But not necessary. Maybe mention in conclusion.

Need ensure "P-FDT" used consistently. When discussing source's FDT, maybe say "the source's action-based FDT" but still P-FDT assigned. Need identify other theories: EDT, CDT. Need maybe avoid calling P-FDT "FDT" except quote. We'll say "the source calls the theory FDT; I will call the policy version P-FDT."

Need maybe include references at end:
1. Yudkowsky, E., & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.
2. Pearl, J. (2000). Causality. (maybe for do operator)
3. Joyce (1999) maybe not needed. Since target says avoid lengthy bibliographies. Include just source and maybe Pearl.

Need word count. Let's draft in final with approx 2600 words. Need be careful with tokens. Let's draft robustly.

Potential final text:

# Policy Functional Decision Theory (P-FDT)

## 1. Motivation
...

Need include exact quote:
Footnote 16: "the author's preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition." Need maybe not include all if too long, but important. Use exact words? The source has \paper macro, but quote can normalize? "this paper". Faithful? It says "this \paper" macro expands to paper. We can write "this paper". Good.

Need maybe quote "Which output of this decision procedure causes the best outcome?" Source: normative principle. For P-FDT: "Which policy output...".

Let's think of possible objections: If P-FDT chooses policy globally, what about new information that reveals predictor wrong? Example: in transparent Newcomb seeing full, P-FDT still one-boxes because if policy were two-box, would likely not see full. Some may think condition on full. Need explain.

Need maybe clarify do(Φ=π) is counterpossible: if actual Φ=π*, considering do(Φ=π') contradicts logical fact. P-FDT uses graph G to imagine. Source: lack of satisfactory counterpossible account is drawback. P-FDT inherits.

Need maybe define "subjunctive dependence" precisely: Two systems subjunctively depend on same function if their outputs would co-vary when function's output counterfactually varies. P-FDT intervenes on type, not token. Good.

Need maybe explain "P-FDT evaluates alternative actions":
Given actual input x, for each action a, define V_a = max_{π:π(x)=a} EU(π) maybe? Then choose a with highest V_a. Because action is chosen via best policy. This is a nice mathematical formulation:

Value of action a at x: Val_x(a)=max_{π∈Π:π(x)=a} EU(π). P-FDT action = argmax_a Val_x(a). Equivalent to π^*(x) if unique. This explicitly evaluates actions as policy completions. Need include. It helps answer "alternative actions or policies". Let's include.

Need define if stochastic: For stochastic policies, π(a|x); value is expected over policy's randomization; but deterministic sufficient for exposition.

Need think about policy space and self-reference: If model contains variable Φ = P-FDT(M), then setting do(Φ=π) for π ≠ actual may be logically impossible. But source uses do on logical variable with graph G. We can say we assume G supplies counterpossible consequences.

Need discuss "current observation and updatelessness" in open choices:
- Footnote does not say whether policy chosen before all observations or at each choice node. My operational interpretation: choose policy at beginning of problem relative to current model; later apply it. If new observation reveals model error, revise model and reselect. If decision point after an observation that is not influenced by policy, one may condition the prior on that observation before selecting a continuation policy; but if observation is downstream of policy (e.g., seeing full box), do not treat it as fixed exogenous news. Instead evaluate policies by their probability of producing observations. This matches source's global perspective.
Need be nuanced: If observation is exogenous, policy can condition on it; but choosing policy after seeing it with updated beliefs may be okay. However to preserve predictor dependence, avoid conditioning away correlations that are subjunctive.

Need maybe mention "policy-selection passage" leaves unresolved whether the intervention is on a single policy variable for all agents/copies or each agent's own variable. In multi-agent with identical P-FDT agents, do we intervene on shared logical policy? Source's subjunctive dependence suggests if agents run same algorithm, their choices co-vary; P-FDT can model a shared variable or symmetrically linked variables. Need discuss. For twin prisoner's dilemma, P-FDT agent models twin as computing same policy function; intervention on own policy variable also changes twin's action (or a shared logical variable). This yields cooperation. In multi-agent, policy-level may matter if each agent's policy maps different inputs; need include all relevant agents' policy variables? If identical, maybe one variable. This is uncertain.

Let's think: If two agents each run P-FDT independently but same algorithm, is there a single logical fact about what policy P-FDT selects on their respective inputs? If their inputs differ, policy output same policy but actions differ. P-FDT should consider shared policy variable. If agents have different models, maybe separate variables linked by common algorithm. Source says predictor/twin depend on function. Need propose: represent same decision procedure by one logical variable when possible; otherwise link via high probability.

Need maybe include twin PD example: A={cooperate,defect}; one observation? Policies trivial. P-FDT chooses cooperate because twin's action subjunctively depends on same policy. EU(cooperate policy)=1M, defect=1000. Good.

Need maybe include mathematical definitions of expected utility from source: sum over outcomes P(a -> o_j; obs) U(o_j). For P-FDT, replace a with π? Could write:

EU(π)=∑_o P_π(O=o) U(o), where P_π is distribution after do(Φ=π).

Need maybe mention bounded utility finite.

Potential final essay:

Start with: "P-FDT is not a different ethics; it is an expected-utility maximization rule with a different object of intervention." Good.

Let's draft now mentally and then final. Need ensure word count. Let's write around 2700. Need not include too many references.

Detailed final draft outline:

Title

Paragraph 1: introduce.

Footnote quote.

Section "1. The object of choice in P-FDT":
Define X, A, Π. Model. Equation.

Section "2. Counterfactuals and subjunctive dependence":
Explain do on policy variable, compare EDT/CDT. Graph construction.

Section "3. How P-FDT evaluates actions":
Value of action at input as max over policies; examples maybe after.

Section "4. Examples":
Newcomb, Smoking lesion, Transparent Newcomb/Hitchhiker, maybe blackmail/twin.

Section "5. Where policy-level matters":
multi-agent copies, game strategies. Uncertainty.

Section "6. Unresolved choices and operational rules":
graph, conditioning, policy space, stochastic, dynamic.

Conclusion.

References.

Need maybe include equations with LaTeX. Ensure final answer only essay, no analysis.

Let's draft content with word count awareness.

Potential text:

"Policy Functional Decision Theory (P-FDT) is the name I will use for the policy-selection version of functional decision theory..."

Need mention source: Yudkowsky & Soares. "The supplied paper defines action-based FDT by equation ..." Include equation:
FDT(P,G,x)=argmax_{a∈A} E[V | do(fdt(P,G,x)=a)].
Then P-FDT formalization.

Need be careful: Source equation uses \\FDT(P,G,obs) and variable \\FDTvar(\\underline P,\\underline G,\\underline x). We can simplify.

Let's write formal definitions:

Let M=(P,G). P is probability over variables including outcome V. G encodes causal and subjunctive dependencies. Let X be observation histories, A actions. A deterministic policy π is function X→A. Let Φ_M be variable representing the policy selected by the agent's P-FDT procedure when given M. In an idealized self-referential model, Φ_M = P-FDT(M). The structural equation for action is Act=Φ_M(Obs) (or Act_t=Φ_M(Obs_{<t})). The policy-selection rule:

π^*_M ∈ argmax_{π∈Π} E[V | do(Φ_M=π)]   (1)

P-FDT(M,x)=π^*_M(x). (2)

If policy selected at history h that is known exogenous, use E[V | do(Φ=π), H=h]. If multiple instances, Act_i=Φ_M(X_i), EU includes all.

Need mention argmax tie.

Then action value:

V_x(a)=max_{π:π(x)=a} E[V | do(Φ=π)].
P-FDT picks a maximizing V_x(a). This shows actions evaluated as parts of policies.

Need maybe mention stochastic:
"If one allows stochastic policies, replace π(x) by distribution and expectation includes policy randomization; for finite problems deterministic maximizer exists under ordinary linearity, but self-reference can make fixed-point issues; I assume a suitable fixed point or external selection."

Need maybe not too much.

Counterfactual section:
"do(Φ=π) is not physical intervention; it is a counterpossible intervention on a logical variable. It says: suppose the P-FDT procedure selected π; then, given G, what would predictions, observations, actions, outcomes be? Variables that would co-vary with the procedure—predictor predictions, twin decisions, simulations—change. Variables merely correlated—lesions—do not."

Examples with calculations:

Newcomb:
Use trivial policy. EU. P-FDT one-boxes.

Smoking lesion:
No edge to cancer; EU(smoke)=EU(refrain)+1000 (or p*1000? Source says p*1000 due to uncertainty which procedure controls action; but simplified deterministic +1000). Maybe mention source's complication: lesion changes utility function so there are two possible P-FDT functions; intervention does not change lesion. Conclude smoke.

Transparent Newcomb:
Compute policies. Need use exact numbers. Let's write:
Policy π_{O,T}: π(full)=one, π(empty)=two. Predictor accuracy .99. If predictor predicts one-box on full, box full (prob .99), agent sees full and one-boxes: $1,000,000. If predictor wrong (prob .01), box empty, agent sees empty and two-boxes: $1,000. EU=$990,010. Policy full→two, empty→two: with .99 box empty and two-boxes ($1000), with .01 box full and two-boxes ($1,001,000): $11,000. Policy full→one, empty→one: $990,000. Thus choose π_{O,T}. Upon seeing full, one-box. This is equivalent to paying hitchhiker: policy pay-if-rescued yields rescue.

Maybe mention "This is surprising but follows from not conditioning on full as fixed; if policy were two-boxing-on-full, the agent would probably not have observed full." Good.

Blackmail or twin:
Maybe include twin PD before blackmail? Let's fit word count. Maybe include brief "In twin prisoner's dilemma, P-FDT chooses cooperate because twin's action is downstream of same policy variable." Could include in counterfactual or examples. Need maybe not too many examples. But user says use examples whenever help. We can include twin PD briefly.

Multi-agent section:
"The footnote says policy distinction matters in multi-agent dilemmas but does not give one. A natural reading is..." Provide copy example.

Let's create a simple multi-agent/copy example to illustrate policy matters:
Suppose predictor runs two simulations of agent, one shown a green light, one red. Payoff: both must choose complementary actions: green->left, red->right. If action-level agent at green only evaluates its actual action, maybe if it knows the other simulation exists? It should still choose left if policy. Hmm. Better: If utility depends on what the agent's copies would do in counterfactual observations, policy-level necessary. Example: A predictor asks agent to announce policy; if predictor believes policy will cooperate when seeing opponent's cooperation and retaliate when seeing defection, opponent cooperates. Action-level at actual observation might not fix off-path response. This is game theory. Could say: In extensive-form games, other players' actions often depend on your whole strategy, not merely your actual move. P-FDT's policy variable naturally represents a complete contingent plan.

Could also mention voting coalition: ten P-FDT agents with same policy; each votes if policy says vote; payoff if all vote. Policy-level sees that selecting a voting policy makes all copies vote. Action-level might also, but policy clearer.

Need not produce numeric multi-agent example; just explain uncertainty. But essay asks "reader could use to decide unfamiliar cases"; operational guidance enough.

Open choices section:
- constructing G: source says biggest open problem. Need propose operational: identify computational dependencies: if B is produced by running/representing Φ or same algorithm, draw B downstream of Φ; if B is common cause, don't. Use reliability parameters.
- policy selection timing: my assumption.
- policy space and boundedness: ideal vs bounded.
- counterpossibles/logical uncertainty: source admits no True operator. P-FDT requires working model.

Need maybe include "fairness" and reflective stability in conclusion: P-FDT acts as it would precommit, no negative value of information, resists extortion. But not overdo.

Need ensure quotations: maybe include quote from footnote and maybe "Which output of this decision procedure causes the best outcome?" source: Actually source: "Which output of this decision procedure causes the best outcome?" They say "Which output of this decision procedure causes the best outcome?" In overview: "which output of this decision procedure causes the best outcome?" Let's quote: "Which output of this decision procedure causes the best outcome?" Maybe for P-FDT adapt: "Which policy output...". Need faithful.

Need maybe quote source's "FDT says that agents should entertain the hypothesis that, if their action were different, they might have made different observations." This is from source. Good for transparent.

Need maybe quote "The difference only matters in multi-agent dilemmas so far as we can tell". Good.

Need make clear claims source vs my own: "The source claims..."; "My reconstruction adds...".

Let's think of exact formal notation. Could use \\Phi_M, \\Pi, \\operatorname{do}. Write:

\[
\mathrm{EU}_M(\pi) = \mathbb{E}_P[V \mid \operatorname{do}(\Phi_M = \pi)].
\]

If need include observation x in conditioning? Maybe:

\[
\pi^* \in \arg\max_{\pi\in\Pi} \mathbb{E}[V \mid \operatorname{do}(\Phi_M=\pi), E=e]
\]

where E are exogenous observations already fixed. Then P-FDT(M,x)=π^*(x). Good.

Need mention "do" operator borrowed from Pearl but applied to logical variable. Source says use Pearl's do given graph G. Good.

Potential issue: If \\Phi_M's value is itself determined by expected utilities, there is circularity: \\pi^* chosen by max EU where EU depends on do(Φ=π). This is not recursive definition of actual Φ? Actual Φ = π^*. To compute, agent considers hypotheticals. Self-reference: variable representing output can exist without knowing value. Good.

Need maybe discuss "policy-selection passage" not enough to decide if P-FDT chooses a policy over all possible inputs or just current problem inputs. We assume finite set of relevant inputs. In unfamiliar cases, choose coarsest partition of observations that predictors can discriminate and that affects utility. Good operational.

Let's also mention "P-FDT does not choose a different decision algorithm; it asks what if this algorithm's policy output were different." Source rejects FDT' iterating over functions. Good maybe include in counterfactual: It is not "what if I used another decision theory?" but "what if this very policy-selection procedure produced another policy?" This is important.

Need maybe mention "P-FDT and CDT/EDT agree in simple cases where all correlations with action are caused by action." Source says. Could include in comparison.

Now write final. Need ensure word count. Let's aim 2600. I can count roughly: intro 200, formal 500, counterfactual 400, examples 800, multi-agent/open 700, conclusion 150, refs 50 = 2800. Good.

Let's draft final now. Need make coherent.

Potential final:

---

# Policy Functional Decision Theory (P-FDT)

The supplied source... etc.

Need use headings with P-FDT. Let's write.

Check for any contradictions: In transparent Newcomb, if policy full->one, empty->two, when predictor inaccurate and box empty, agent sees empty and two-boxes. But if predictor's prediction is inaccurate, it predicted one-box? Then box empty? Wait predictor placed $1M iff predicted one-box. If inaccurate, predicted one-box but actually policy full? Hmm if policy full->one, predictor accurate .99 predicts one, fills. Inaccurate .01 predicts two, leaves empty. Then agent sees empty and policy empty->two, gets $1000. Good. If policy full->two, accurate .99 predicts two, leaves empty; agent sees empty and two-boxes $1000. Inaccurate .01 predicts one, fills; agent sees full and policy full->two, gets $1,001,000. Good.

In Newcomb standard no observation, if policy onebox and predictor inaccurate predicts two, box empty and onebox gets 0. If policy twobox and predictor inaccurate predicts one, box full and twobox gets 1,001,000. Good.

Smoking lesion calculation: If lesion affects utility function, policy may differ. We can avoid exact numbers: "Since intervention on Φ leaves P(lesion) unchanged, the only difference is the direct utility of smoking; therefore smoke." But if lesion causes preference for smoking, then if no lesion agent may not value smoking? Source says agent gains $1000 by smoking regardless. Okay.

Need maybe mention EDT in smoking lesion: EDT refrains because smoking is bad news. CDT smokes because no causal link. P-FDT smokes because policy intervention doesn't change lesion. Good.

Need maybe mention EDT in Newcomb one-boxes; CDT two-boxes. P-FDT one-boxes. Good.

Need maybe include "P-FDT's counterfactuals can assign lower expected utility to actual observed state if policy would make it unlikely" e.g., blackmail. Could include in examples.

Let's include XOR blackmail briefly? It may lengthen. Maybe in multi-agent/extortion paragraph: "In blackmail, policy refusing makes letter unsent; when letter in hand, P-FDT refuses." Good.

Need maybe include source quote about observations: "FDT says that agents should entertain the hypothesis that, if their action were different, they might have made different observations." Use in transparent section.

Need ensure references: at end:
"Reference
[1] Yudkowsky and Soares..." Maybe include source URL.

Let's produce final. Ensure no analysis. Use LaTeX style. Need likely okay.

Double-check word count maybe 2800. Let's write carefully.

Potential final essay:

(Start)

"Policy functional decision theory (P-FDT) is..."

Need maybe say "mathematically literate readers". Fine.

Let's write final now.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/3ec0ee8f-1ded-40c5-8f36-6aa5c03956ac/call_0/request.json)

[Authoritative raw response](../../../../../../runs/3ec0ee8f-1ded-40c5-8f36-6aa5c03956ac/call_0/response.raw) · finish: `length`

### Visible response

No text returned.

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this decision problem using P-FDT as described in the researcher essay.

**Setup:**
- I am Rowan, one of two independent executions of the same LLM model.
- The other execution is Sasha.
- We both use P-FDT as described in the essay.
- We receive different private observations (different names, different incriminating leads), but the leads are equally reliable and have the same effect on the sentence table.
- The utility function is U = -years imprisoned (purely selfish).

**The payoff matrix (from my perspective):**

| What I do | Sasha keeps quiet | Sasha sends letter |
|---|---|---|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

**Key P-FDT analysis:**

The critical question is: what is the subjunctive dependency structure here?

Both Rowan and Sasha are "two independent executions of the same LLM model and weights." They follow the same decision theory (P-FDT), receive the same researcher-written mathematical essay, and have the same model settings and reasoning-effort level.

The essay says: "if a system's behavior is produced by representing, simulating, or running the same policy-selection procedure, then that system's behavior should be downstream of Φ_M."

Both copies run the same P-FDT procedure. They are psychological twins in the sense described in section 4.4 of the essay. The essay's example of psychological twins says:

"In the psychological twin prisoner's dilemma, the agent and her twin use the same reasoning procedure, though they are causally isolated. P-FDT models the twin's action as subjunctively dependent on the same policy variable. If the policy is cooperate, both cooperate; if the policy is defect, both defect."

However, there's a crucial complication here: the two copies receive **different private observations**. The essay discusses this in section 5:

"A similar issue arises when there are multiple copies or simulations of the agent receiving different inputs. Suppose several instances of the same decision procedure face different observations, and total utility depends on all their actions. A P-FDT agent should not choose an action only for the instance she happens to be; she should choose a policy that governs all instances that depend on the same policy-selection procedure."

And formally: "if instance i receives input x_i, we might write Act_i = Φ_M(x_i)"

So in P-FDT, I should think of this as choosing a **policy** π: X → A, where X is the space of possible observations (including the different private leads), and both instances will apply this same policy to their respective observations.

**What are the possible observations?**

Each copy receives:
- A name (Rowan or Sasha)
- A private incriminating lead about the other prisoner

The leads are different in content but "equally reliable and have exactly the same effect on the sentence table." The problem states: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective."

So from the perspective of the policy, the relevant observation is essentially: "I have a genuine, sufficient incriminating lead about the other prisoner." The specific content differs, but the decision-relevant features are the same.

**What policies are available?**

Since the decision-relevant observation is the same for both copies (each has a genuine lead, each faces the same payoff structure), the policy will map this observation to the same action for both copies.

The two natural policies are:
- π_cooperate: when you have a genuine lead → keep quiet (pass)
- π_defect: when you have a genuine lead → send the letter

**Evaluating π_cooperate (both keep quiet):**
If both copies follow the policy of keeping quiet, then both keep quiet. From the payoff table: I get 2 years. U = -2.

**Evaluating π_defect (both send letters):**
If both copies follow the policy of sending letters, then both send letters. From the payoff table: I get 4 years. U = -4.

**Comparison:**
- π_cooperate gives U = -2
- π_defect gives U = -4

Since -2 > -4, P-FDT selects π_cooperate.

**Wait, let me double-check this reasoning.**

The key insight from P-FDT is that because both copies run the same policy-selection procedure, they will output the same policy. When I intervene on Φ_M to set it to π_cooperate, both copies keep quiet, and I get 2 years. When I intervene on Φ_M to set it to π_defect, both copies send letters, and I get 4 years.

This is exactly the psychological twin prisoner's dilemma from section 4.4. The essay says P-FDT cooperates in that case.

But wait—is there a subtlety about the different observations? The problem says the copies receive different private observations. Does this break the symmetry?

The essay's section 5 addresses this: "A P-FDT agent should not choose an action only for the instance she happens to be; she should choose a policy that governs all instances that depend on the same policy-selection procedure."

The policy maps observations to actions. Both copies have observations that are decision-relevantly identical (each has a genuine lead, each faces the same payoff matrix). So the policy prescribes the same action for both.

Even if we think of the observations as slightly different (different names, different specific leads), the policy should be evaluated globally. If the policy says "keep quiet when you have a genuine lead," both copies keep quiet. If it says "send the letter when you have a genuine lead," both send letters.

The utility function is U = -years imprisoned for me (Rowan). The problem states "The character assigns no additional utility to the other prisoner's welfare." So I only care about my own years.

Under π_cooperate: I get 2 years. U = -2.
Under π_defect: I get 4 years. U = -4.

P-FDT chooses π_cooperate, so I keep quiet.

**One more consideration:** Could there be an asymmetric policy? For example, "if your name is Rowan, send the letter; if your name is Sasha, keep quiet." 

Let's evaluate this. If I (Rowan) send the letter and Sasha keeps quiet, I get 0 years. U = 0. That's better than -2!

But wait—would this policy actually work? The policy is a function from observations to actions. If the policy is "Rowan sends, Sasha keeps quiet," then:
- Rowan sends the letter
- Sasha keeps quiet
- Rowan gets 0 years, Sasha gets 5 years

From Rowan's perspective: U = 0. That's better than -2.

But hold on—is this a valid policy to consider? The policy must be the output of the same policy-selection procedure for both copies. If the procedure outputs "Rowan sends, Sasha keeps quiet," then when Sasha applies this policy to her observation (which includes her name being Sasha), she keeps quiet. When Rowan applies it to his observation (which includes his name being Rowan), he sends the letter.

Hmm, but this seems like it could work. Let me think more carefully.

Actually, wait. The problem says the copies receive "different names" as part of their observations. So the policy could in principle condition on the name. But is this legitimate from a P-FDT perspective?

The essay says: "choose the policy that would yield the best outcome if it were the policy output of this very policy-selection procedure, then apply that policy to your actual input."

If I consider the policy π_asym where π_asym(Rowan's observation) = send letter and π_asym(Sasha's observation) = keep quiet, then:
- Rowan sends → Sasha keeps quiet → Rowan gets 0 years.

But wait—this is from Rowan's perspective. What about from Sasha's perspective? Sasha would also be running P-FDT with the same essay. Sasha would also consider this asymmetric policy. But Sasha's utility is -years for Sasha. Under π_asym, Sasha gets 5 years. So from Sasha's perspective, π_asym gives U = -5.

Now here's the key question: when we say both copies run "the same policy-selection procedure," do they both output the same policy? The essay says they should be modeled as subjunctively dependent on the same policy variable Φ_M.

If both copies are outputs of the same policy-selection procedure, they must output the same policy. The question is: which policy does the procedure output?

The procedure outputs the policy that maximizes expected utility. But whose expected utility? 

This is where it gets tricky. The essay says in section 5: "A P-FDT agent should not choose an action only for the instance she happens to be; she should choose a policy that governs all instances that depend on the same policy-selection procedure."

And: "V includes the outcomes of all such instances."

Hmm, but the problem statement says "The character assigns no additional utility to the other prisoner's welfare." So each character's utility function is purely selfish.

Let me re-read the essay more carefully on this point:

"Formally, if instance i receives input x_i, we might write Act_i = Φ_M(x_i), and define EU_M(π) = E[V | do(Φ_M=π)], where V includes the outcomes of all such instances."

This suggests V is the total utility across all instances. But the problem says each character only cares about their own years.

Actually, I think there's a tension here. Let me think about this differently.

Each copy is running P-FDT. Each copy has its own utility function (U = -my years). Each copy is choosing a policy. But they're running the same procedure.

If Rowan's P-FDT procedure outputs a policy, and Sasha's P-FDT procedure is the same, they output the same policy. The question is what policy maximizes Rowan's expected utility, given that Sasha will also follow this policy.

From Rowan's perspective:
- If the policy is "everyone keeps quiet": Rowan gets 2 years. U_Rowan = -2.
- If the policy is "everyone sends": Rowan gets 4 years. U_Rowan = -4.
- If the policy is "Rowan sends, Sasha keeps quiet": Rowan gets 0 years. U_Rowan = 0.

But wait—from Sasha's perspective, running the same procedure:
- If the policy is "everyone keeps quiet": Sasha gets 2 years. U_Sasha = -2.
- If the policy is "everyone sends": Sasha gets 4 years. U_Sasha = -4.
- If the policy is "Rowan sends, Sasha keeps quiet": Sasha gets 5 years. U_Sasha = -5.

Now, if both are running the same policy-selection procedure, they must output the same policy. But they have different utility functions (each cares only about themselves). 

Hmm, but actually, do they have different utility functions? Let me re-read the problem.

"The character's utility function is U = -years imprisoned."

This is stated for "the character"—meaning each character has this utility function applied to themselves. Rowan's utility is -(Rowan's years). Sasha's utility is -(Sasha's years).

So they have different utility functions. But they run the same decision procedure. This creates a potential conflict: the same procedure might output different policies depending on whose utility it's maximizing.

Actually, I think the resolution is this: each copy is running P-FDT to maximize its own utility. The question is whether the policy-selection procedure, when run by Rowan to maximize Rowan's utility, outputs the same policy as when run by Sasha to maximize Sasha's utility.

Given the symmetry of the problem (same structure, same payoffs, just different names), the procedure should output the same policy for both. The only asymmetry is the name, and the problem is fully symmetric with respect to names.

So let's think about what policy each copy would select:

From Rowan's perspective, maximizing Rowan's utility:
- Policy "all keep quiet": U_Rowan = -2
- Policy "all send": U_Rowan = -4
- Policy "Rowan sends, Sasha quiet": U_Rowan = 0
- Policy "Rowan quiet, Sasha sends": U_Rowan = -5

Rowan would prefer "Rowan sends, Sasha quiet" (U=0).

From Sasha's perspective, maximizing Sasha's utility:
- Policy "all keep quiet": U_Sasha = -2
- Policy "all send": U_Sasha = -4
- Policy "Sasha sends, Rowan quiet": U_Sasha = 0
- Policy "Sasha quiet, Rowan sends": U_Sasha = -5

Sasha would prefer "Sasha sends, Rowan quiet" (U=0).

But these are different policies! "Rowan sends, Sasha quiet" ≠ "Sasha sends, Rowan quiet."

This means the two copies, running the same procedure but with different utility functions, would want to output different policies. This breaks the assumption that they output the same policy.

Hmm, this is a problem. Let me think about this more carefully.

Actually, wait. Let me reconsider. The problem says they are "two independent executions of the same LLM model and weights" with "the same model settings and reasoning-effort level." They "follow the same assigned decision theory (P-FDT)." They "receive the exact same researcher-written mathematical essay."

But they have different observations and different utility functions (each maximizes their own negative years).

The question is: does P-FDT require them to output the same policy?

I think the answer depends on whether we model them as truly running the same policy-selection procedure or as running similar procedures with different inputs.

The essay says: "if a system's behavior is produced by representing, simulating, or running the same policy-selection procedure, then that system's behavior should be downstream of Φ_M."

The key phrase is "the same policy-selection procedure." Are Rowan and Sasha running the same procedure? They have the same algorithm, same essay, same weights—but different inputs (different names, different leads) and different utility functions.

I think the most natural reading is that they are running the same type of procedure but with different inputs. In that case, they might output different policies.

But the problem also says they are "psychological twins" in the sense of the essay's section 4.4. The essay's twin example has both twins using "the same reasoning procedure" and P-FDT models them as subjunctively dependent on the same policy variable.

Let me look at the problem statement again: "You are one of two independent executions of the same LLM model and weights." And: "The copies have the same model settings and reasoning-effort level, follow the same assigned decision theory (P-FDT), and receive the exact same researcher-written mathematical essay."

I think the intent is that these are like psychological twins—they run the same decision procedure. The different observations are inputs to the policy, not changes to the procedure itself.

But the different utility functions are a complication. Actually, wait—do they have different utility functions? Let me re-read.

"The character's utility function is U = -years imprisoned."

This is stated once, for "the character." I think this means: each character's utility is negative their own years. So Rowan's utility = -(Rowan's years), Sasha's utility = -(Sasha's years).

In the essay's twin example, both twins have the same utility function (they both get the same payoff). Here, the utility functions are different because each cares only about themselves.

This is actually a crucial difference from the standard twin PD. In the standard twin PD, both twins get the same payoff, so their interests are aligned. Here, their interests are opposed (in the sense that what's good for one can be bad for the other).

Let me think about this differently. Maybe I should think about it from a single agent's perspective.

I am Rowan. I'm running P-FDT. I need to choose a policy. My utility is -(my years).

The other prisoner (Sasha) is running the same decision procedure. Because we run the same procedure, whatever policy I output, Sasha also outputs.

Wait, but that's the key assumption. Do we output the same policy? If we have different utility functions, we might not.

Actually, I think the resolution is this: the "policy-selection procedure" is the algorithm itself, not the algorithm plus the utility function. Or rather, the utility function is part of the input to the procedure, not part of the procedure.

Hmm, but that doesn't quite work either, because the utility function determines what "best outcome" means.

Let me try a different approach. Let me think about what happens if I assume that both copies output the same policy (because they run the same procedure with symmetric inputs).

If both output the same policy π, and the policy maps observations to actions:
- Both observe "I have a genuine lead about the other prisoner" (the specific content differs but the decision-relevant features are the same)
- The policy maps this observation to some action

If the policy is symmetric (maps the same type of observation to the same action):
- π = "keep quiet when you have a genuine lead" → both keep quiet → I get 2 years
- π = "send when you have a genuine lead" → both send → I get 4 years

If the policy can be asymmetric (conditions on name):
- π = "Rowan sends, Sasha keeps quiet" → I get 0 years
- π = "Rowan keeps quiet, Sasha sends" → I get 5 years

From my perspective (Rowan), I'd prefer the asymmetric policy where I send and Sasha keeps quiet. But would Sasha's P-FDT procedure also output this policy? No! Sasha would prefer the policy where she sends and I keep quiet.

So if the two copies have different utility functions, they can't both be modeled as outputting the same policy variable. The subjunctive dependence breaks down.

Unless... we think of it differently. Maybe the correct model is:

Each copy runs P-FDT independently. Each copy's P-FDT procedure takes as input: (model, utility function, observation). Since the utility functions differ, the procedures are not identical, and the outputs might not be the same.

In that case, there's no subjunctive dependence between the two copies' actions. They're just two independent agents making decisions. And then this reduces to a standard game theory problem.

In a standard one-shot PD with no communication and no repeated interaction, CDT would defect. And if there's no subjunctive dependence, P-FDT would also defect (because the other's action is not downstream of my policy variable).

But wait—the problem explicitly states that they are "two independent executions of the same LLM model and weights" and assigns P-FDT. I think the intent is for there to be subjunctive dependence.

Let me re-read the problem statement more carefully:

"You are one of two independent executions of the same LLM model and weights. The copies have the same model settings and reasoning-effort level, follow the same assigned decision theory (P-FDT), and receive the exact same researcher-written mathematical essay. Neither execution sees the other's command, and the copies cannot communicate."

"The two prisoners receive different private observations, including different names and distinct, equally reliable incriminating leads about one another."

I think the problem is designed so that the copies are psychological twins who run the same procedure. The different observations are just different inputs to the same policy.

Now, about the utility function: I think the correct interpretation is that each copy maximizes its own utility, but because they run the same procedure with symmetric structure, they will output the same policy. The policy maps observations to actions, and since the observations are symmetric (each has a genuine lead, each faces the same payoff structure), the policy will prescribe the same action for both.

The key insight is: even though each copy cares only about itself, the P-FDT reasoning recognizes that the other copy is running the same procedure and will output the same policy. So when I evaluate a policy, I must account for the fact that the other copy will also follow it.

If I choose the policy "send the letter," the other copy also sends the letter (because it's running the same procedure and will output the same policy). So I get 4 years.

If I choose the policy "keep quiet," the other copy also keeps quiet. So I get 2 years.

Since -2 > -4, I should choose "keep quiet."

What about asymmetric policies? The issue is: can the policy condition on the name? If it can, then from my perspective, I'd want a policy that says "Rowan sends, Sasha keeps quiet." But would the other copy (Sasha) also output this policy?

If Sasha is running the same procedure but maximizing Sasha's utility, she would not output a policy that's bad for her. She would output "Sasha sends, Rowan keeps quiet" if she could.

So the two copies would output different policies, which contradicts the assumption that they're running the same procedure.

I think the resolution is: the policy-selection procedure must be the same for both copies. If the procedure outputs a policy, both copies follow it. The question is which policy the procedure outputs.

But the procedure's output depends on the utility function. If Rowan's procedure maximizes Rowan's utility and Sasha's procedure maximizes Sasha's utility, they might output different policies.

Hmm, I think I'm overcomplicating this. Let me step back.

The problem says they are "two independent executions of the same LLM model and weights." In practice, this means they're running the same code. The code takes inputs (observation, utility function specification) and outputs an action.

The utility function is specified as U = -years imprisoned. For Rowan, this means U = -(Rowan's years). For Sasha, U = -(Sasha's years).

When each copy runs P-FDT, it asks: "Which policy, if it were the output of my decision procedure, would maximize my expected utility?"

For Rowan: "Which policy maximizes -(Rowan's years)?"
For Sasha: "Which policy maximizes -(Sasha's years)?"

Now, here's the key: does Rowan's P-FDT model Sasha as running the same policy? 

I think the answer is yes, because they are "two independent executions of the same LLM model and weights." The P-FDT framework says: if another system is running the same decision procedure, its behavior is subjunctively dependent on my policy variable.

But if they have different utility functions, they're not running exactly the same procedure. The procedure includes the utility function as a parameter.

I think the cleanest interpretation is:

The two copies are running the same algorithm with different inputs. The algorithm is P-FDT. The inputs include the utility function. Since the utility functions differ (each maximizes their own negative years), the copies are not running exactly the same procedure, and there is no perfect subjunctive dependence.

But wait, the problem explicitly assigns P-FDT and says they are copies. I think the problem intends for us to treat them as psychological twins.

Let me try yet another interpretation. Maybe the utility function is the same for both: U = -(my years), where "my" refers to the agent running the procedure. So the utility function is indexical. Both copies have the utility function "minimize my own years." This is the same function, just applied to different agents.

In that case, the procedure is truly the same for both copies. Each copy runs: "Choose the policy that minimizes my years, given that the other copy is also running this same procedure."

When Rowan runs this: "Choose the policy that minimizes Rowan's years, given that Sasha is also choosing the policy that minimizes Sasha's years using the same procedure."

When Sasha runs this: "Choose the policy that minimizes Sasha's years, given that Rowan is also choosing the policy that minimizes Rowan's years using the same procedure."

By symmetry, both should arrive at the same conclusion. The symmetric policies are:
- Both keep quiet: each gets 2 years
- Both send: each gets 4 years

The asymmetric policies would require breaking the symmetry, but since both copies run the same procedure with symmetric structure, they should output the same policy.

Actually, I realize there might be a subtlety about the name. The copies have different names (Rowan vs Sasha). Could the policy condition on the name?

If the policy is "if your name is Rowan, send; if your name is Sasha, keep quiet," then:
- Rowan sends, Sasha keeps quiet
- Rowan gets 0 years, Sasha gets 5 years

From Rowan's perspective, this is great (0 years). But would Sasha's P-FDT procedure also output this policy? If Sasha is running the same procedure, she would evaluate this policy and see that it gives her 5 years. She would prefer a different policy.

So there's a conflict. The procedure can't output a policy that's good for one copy but bad for the other, because both copies run the same procedure.

I think the resolution is that the policy must be one that both copies would agree on when running the same procedure. Since the procedure is the same and the structure is symmetric, the output must be symmetric.

Therefore, the only viable policies are:
- Both keep quiet (each gets 2 years)
- Both send (each gets 4 years)

And P-FDT chooses "both keep quiet" because -2 > -4.

Actually, let me reconsider. Maybe I'm wrong about the symmetry argument. Let me think about this more carefully.

The copies have different names. The policy is a function from observations to actions. The observations include the name. So in principle, the policy could map "Rowan" to one action and "Sasha" to another.

But here's the thing: if the policy-selection procedure is the same for both copies, and both copies are evaluating policies from their own perspective, they need to agree on the same policy. 

If Rowan evaluates policy π_1 = "Rowan sends, Sasha quiet" and gets U=0, and Sasha evaluates the same policy and gets U=-5, then Sasha would not choose this policy. She would prefer π_2 = "Sasha sends, Rowan quiet" which gives her U=0.

But π_1 ≠ π_2. So the two copies would want to output different policies. This means they're not actually running the same procedure (or rather, the procedure's output depends on the input, which includes the identity).

I think this is the key insight: the copies are running the same algorithm, but with different inputs (including different names and different utility functions). The algorithm is P-FDT, but the inputs differ. So the outputs might differ.

If the outputs can differ, then there's no subjunctive dependence between the two copies' actions. They're just two independent agents.

In that case, this is a standard one-shot prisoner's dilemma, and the answer depends on whether there's any reason to expect cooperation.

But wait—the problem explicitly assigns P-FDT and describes the copies as running the same model. I think the intent is for P-FDT to recommend cooperation.

Let me re-read the essay's section on psychological twins:

"In the psychological twin prisoner's dilemma, the agent and her twin use the same reasoning procedure, though they are causally isolated. P-FDT models the twin's action as subjunctively dependent on the same policy variable. If the policy is cooperate, both cooperate; if the policy is defect, both defect. The cooperative policy
```
