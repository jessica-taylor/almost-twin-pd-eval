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