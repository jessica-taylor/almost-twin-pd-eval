# Policy Functional Decision Theory: Choosing the Best Policy, Not Just the Best Act

Policy functional decision theory, which I will call **P-FDT**, is the policy-selection variant of the decision theory presented by Yudkowsky and Soares in *Functional Decision Theory: A New Theory of Instrumental Rationality*. The source paper mostly formalizes a theory that chooses an action by intervening on a variable representing the output of the agent’s decision procedure. But footnote 16 points toward a more fundamental formulation:

> “the author's preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition.”

This passage is brief, but it is enough to define a distinctive decision rule. On my reading, **P-FDT** says:

> Choose the policy that would produce the best expected outcome if it were the output of this very policy-selection procedure; then apply that policy to your actual input.

The essential shift is from “Which physical act should I perform?” to “Which input-output rule should this decision procedure implement?” P-FDT evaluates whole policies, not merely isolated actions, and it evaluates them by means of counterfactual interventions on a logical or computational variable: the variable representing the policy selected by the agent’s decision procedure.

Because the footnote does not give a complete formal system, the following essay develops an explicit mathematical reconstruction. I will distinguish claims made by the source from additional operational assumptions that I am adding to make P-FDT usable.

---

## 1. The basic objects of P-FDT

Let

- \(\mathcal X\) be a set of possible observations, inputs, or input histories;
- \(\mathcal A\) be a finite set of actions;
- \(\Pi = \mathcal A^{\mathcal X}\) be the set of deterministic policies, where a policy \(\pi \in \Pi\) maps each possible input \(x \in \mathcal X\) to an action \(\pi(x) \in \mathcal A\).

In sequential problems, \(\mathcal X\) should be understood as the set of decision-relevant histories, so that a policy tells the agent what to do at every possible decision point. Stochastic policies can also be allowed by letting \(\pi(x)\) be a distribution over \(\mathcal A\), but for simplicity I will use deterministic policies.

An agent using P-FDT has a world-model

\[
M = (P, G),
\]

where:

- \(P\) is a probability distribution over relevant variables;
- \(G\) is a dependency graph or structural model saying how those variables depend on one another.

The crucial variable in \(G\) is a logical or computational variable

\[
D \in \Pi,
\]

representing the policy output by the agent’s own policy-selection procedure. In the source’s notation, this is the variable `FDT(-)`; in this essay, I will call it the **P-FDT policy node**.

The model also contains variables such as:

- \(X\), the observation or input the agent receives;
- \(A\), the action taken;
- \(Y\), other relevant facts: predictions made by predictors, actions of other agents, contents of boxes, presence of lesions, and so on;
- \(V\), the utility or value of the resulting outcome.

Given a policy \(D = \pi\), the action variable is determined by the policy and the input:

\[
A = D(X) = \pi(X).
\]

The central P-FDT expected utility of a policy \(\pi\) is then

\[
\operatorname{EU}_{M}(\pi)
=
\mathbb{E}_{P}\!\left[ V \mid \operatorname{do}_{G}(D = \pi) \right],
\]

where \(\operatorname{do}_{G}(D=\pi)\) means: intervene on the policy node, setting it to \(\pi\), and propagate the consequences through the dependency graph \(G\).

The agent then selects a policy

\[
\pi^{*}
\in
\arg\max_{\pi \in \Pi}
\operatorname{EU}_{M}(\pi),
\]

and, upon receiving actual input \(x\), executes

\[
\text{P-FDT}(M,x) = \pi^{*}(x).
\]

This is the core decision rule.

---

## 2. How P-FDT differs from EDT and CDT

It is useful to compare P-FDT with evidential decision theory and causal decision theory.

**Evidential decision theory**, EDT, chooses an action by conditionalizing on the news that action provides:

\[
a_{\text{EDT}}
=
\arg\max_{a \in \mathcal A}
\mathbb{E}[V \mid X=x, A=a].
\]

EDT preserves all statistical correlations between the action and the world. This helps in some predictor problems but fails in smoking-lesion-style cases, where the action is merely evidence of a bad condition.

**Causal decision theory**, CDT, chooses an action by physically intervening on the action variable:

\[
a_{\text{CDT}}
=
\arg\max_{a \in \mathcal A}
\mathbb{E}[V \mid \operatorname{do}(A=a), X=x].
\]

CDT breaks correlations that are not caused by the action. This handles lesions but fails when predictors or copies depend on the agent’s decision procedure.

P-FDT instead intervenes on the policy-selection computation:

\[
\pi^{*}
=
\arg\max_{\pi \in \Pi}
\mathbb{E}[V \mid \operatorname{do}(D=\pi)].
\]

Then the actual act is \(\pi^{*}(x)\).

The difference is not merely notational. CDT asks, “What would happen if my body performed this action?” P-FDT asks, “What would happen if this very policy-selection procedure output this policy?” The latter preserves dependencies between the agent’s decision procedure and anything that predicts, simulates, copies, or otherwise logically depends on that procedure. It severs merely statistical correlations that do not arise from such dependence.

The source describes this distinction using the idea of **subjunctive dependence**. Two calculators computing the same arithmetic problem may be causally independent, but their outputs subjunctively depend on the same mathematical function. If one outputs \(7336\), the other will also output \(7336\), assuming both are working correctly. Similarly, if a reliable predictor models an agent’s decision procedure, the predictor’s prediction subjunctively depends on the output of that procedure. P-FDT treats such dependencies as decision-relevant.

---

## 3. P-FDT counterfactuals and dependency graphs

The formal heart of P-FDT is the intervention

\[
\operatorname{do}_{G}(D=\pi).
\]

This is analogous to Pearl’s causal \(\operatorname{do}\)-operator, but applied to a logical or computational variable. The graph \(G\) tells us which variables would change if the policy-selection procedure had a different output.

A variable \(Z\) should be treated as subjunctively dependent on \(D\) if, roughly, \(Z\) is produced by a process that computes, predicts, simulates, or otherwise tracks the output of the agent’s policy-selection procedure. Examples include:

- a predictor’s prediction of the agent’s policy;
- a psychological twin running the same reasoning procedure;
- a simulation of the agent used by another agent;
- a blackmailer’s decision to send a letter, where the blackmailer sends the letter only if she predicts the agent’s policy would pay;
- an observation that is itself produced by a predictor who responds to the agent’s expected policy.

By contrast, a variable should not be treated as subjunctively dependent on \(D\) if it is merely statistically correlated with the agent’s behavior through a common cause that does not compute or predict the policy. A lesion that causes both a taste for smoking and cancer is the canonical example. The lesion does not model the agent’s policy-selection procedure, so changing the policy node does not change whether the lesion exists.

This is the principle behind P-FDT’s treatment of counterfactuals:

> When imagining that her policy-selection procedure had a different output, the P-FDT agent changes all and only those things that subjunctively depend on that procedure.

This requires a kind of counterpossible reasoning. If the agent’s actual decision procedure deterministically outputs \(\pi^{*}\), then considering a different output \(\pi \neq \pi^{*}\) is, strictly speaking, counter-to-logic. The source acknowledges that we do not yet have a fully satisfactory formal account of such reasoning. P-FDT therefore assumes that the agent has some way of reasoning under logical uncertainty: she can coherently ask, “What would the world look like if this computation had a different output?”

My operational suggestion is this: in applied problems, construct \(G\) directly from the problem description. Draw an edge from \(D\) to \(Z\) exactly when the story says that \(Z\) is produced by prediction, simulation, copying, or logical dependence on the agent’s policy. If the story gives no such dependence, do not draw the edge. This is not a complete theory of how to learn subjunctive dependencies from data, but it is enough to solve many stylized decision problems.

---

## 4. P-FDT in Newcomb’s problem

Consider Newcomb’s problem. There is a transparent box A containing \$1,000 and an opaque box B containing either \$1,000,000 or \$0. A predictor who is correct with probability \(0.99\) filled box B iff she predicted the agent would take only box B.

The policy space is simple. The relevant input is “facing the boxes,” and the actions are:

\[
\mathcal A = \{\text{one-box}, \text{two-box}\}.
\]

Let \(\pi_1\) be the one-boxing policy and \(\pi_2\) the two-boxing policy.

In the P-FDT graph, the predictor’s prediction is a child of the policy node \(D\), because the predictor predicts the agent’s decision procedure. Box B’s contents depend on the prediction. The agent’s action depends on \(D\).

If \(D = \pi_1\), then with probability \(0.99\) the predictor predicted one-boxing and filled box B. With probability \(0.01\), she predicted two-boxing and left it empty. Thus

\[
\operatorname{EU}(\pi_1)
=
0.99 \cdot 1{,}000{,}000
+
0.01 \cdot 0
=
990{,}000.
\]

If \(D = \pi_2\), then with probability \(0.99\) the predictor predicted two-boxing and left box B empty, giving the agent \$1,000 from box A. With probability \(0.01\), she predicted one-boxing and filled box B, giving the agent \$1,001,000 by two-boxing. Thus

\[
\operatorname{EU}(\pi_2)
=
0.99 \cdot 1{,}000
+
0.01 \cdot 1{,}001{,}000
=
11{,}000.
\]

P-FDT selects \(\pi_1\), the one-boxing policy.

This matches the source’s broader argument: P-FDT one-boxes because the predictor’s behavior subjunctively depends on the same decision procedure that the agent is running.

---

## 5. P-FDT in the smoking lesion problem

Now consider the smoking lesion problem. Smoking is correlated with cancer, but only because a lesion causes both a desire to smoke and cancer. Smoking itself does not cause cancer. The agent gains \$1,000 in utility from smoking and gains \$1,000,000 from not dying of cancer.

Here the relevant policies are:

\[
\pi_S = \text{smoke}, \qquad \pi_R = \text{refrain}.
\]

The lesion affects cancer and may affect the agent’s preferences, but it does not compute or predict the agent’s policy-selection procedure. Therefore the P-FDT graph contains no edge from \(D\) to the lesion variable and no edge from \(D\) to cancer, except through the action itself. Since smoking does not cause cancer in the problem’s setup, changing \(D\) does not change the probability of cancer.

So the expected utility difference is just the direct utility of smoking:

\[
\operatorname{EU}(\pi_S)
=
\operatorname{EU}(\pi_R) + 1{,}000.
\]

P-FDT therefore chooses to smoke.

This is the desired result: P-FDT one-boxes in Newcomb’s problem and smokes in the smoking lesion problem. It does not treat all correlations alike. It respects predictor-like dependencies but ignores lesion-like correlations.

---

## 6. P-FDT in transparent Newcomb and Parfit’s hitchhiker

P-FDT becomes especially interesting in cases where the agent receives information that seems to make the optimal action obvious.

In the transparent Newcomb problem, both boxes are transparent. The predictor placed \$1,000,000 in box B iff she predicted that the agent would leave box A behind upon seeing that both boxes are full. Suppose the agent sees that box B is full.

EDT and CDT both two-box once the agent sees the full box. EDT says: given that box B is full, taking both boxes is better news. CDT says: given that box B is already full, taking box A causes an extra \$1,000 to be obtained.

P-FDT instead evaluates policies. A natural policy is:

\[
\pi_{\text{commit}}(x) =
\begin{cases}
\text{one-box}, & x = \text{see full},\\
\text{two-box}, & x = \text{see empty}.
\end{cases}
\]

Another policy is:

\[
\pi_{\text{defect}}(x) =
\begin{cases}
\text{two-box}, & x = \text{see full},\\
\text{two-box}, & x = \text{see empty}.
\end{cases}
\]

The predictor’s choice depends on the agent’s policy, not merely on the physical movement made after seeing the boxes. If the policy node is set to \(\pi_{\text{commit}}\), then with probability \(0.99\) the predictor filled box B, the agent sees it full, and one-boxes, receiving \$1,000,000. With probability \(0.01\), the predictor left it empty, the agent sees it empty, and two-boxes, receiving \$1,000. Thus

\[
\operatorname{EU}(\pi_{\text{commit}})
\approx
0.99 \cdot 1{,}000{,}000
+
0.01 \cdot 1{,}000
=
990{,}010.
\]

If the policy node is set to \(\pi_{\text{defect}}\), then with probability \(0.99\) the predictor left box B empty and the agent two-boxes for \$1,000. With probability \(0.01\), the predictor filled it, the agent sees it full, and two-boxes for \$1,001,000. Thus

\[
\operatorname{EU}(\pi_{\text{defect}})
=
0.99 \cdot 1{,}000
+
0.01 \cdot 1{,}001{,}000
=
11{,}000.
\]

P-FDT chooses \(\pi_{\text{commit}}\). Therefore, when the agent actually sees the full box, she one-boxes.

This is equivalent to paying the driver in Parfit’s hitchhiker problem. The driver helps iff she predicts the agent will pay after arriving in the city. A P-FDT agent adopts the policy of paying, because adopting that policy is what causes the driver to help. Upon arriving in the city, the agent pays.

The source defends this behavior through arguments from precommitment, value of information, and expected utility. P-FDT agents act as they would have wanted to precommit to act, without needing actual binding precommitments.

---

## 7. Why policy selection matters

The policy-selection passage in footnote 16 says the difference between choosing actions and choosing policies “only matters in multi-agent dilemmas so far as we can tell.” The source does not develop this fully, but the basic idea is clear: in some problems, the payoff depends not only on the action taken at the actual input, but on what the agent’s policy would do at other possible inputs.

Here is a simple example that illustrates the point.

### The off-path reward problem

An agent will receive one of two signals, \(0\) or \(1\), each with probability \(1/2\). Before the signal is issued, a predictor predicts the agent’s entire policy. If the predictor predicts that the agent’s policy would pay \$1,000 upon receiving signal \(1\), then the predictor gives the agent \$1,000,000 if signal \(0\) occurs. If the predictor predicts the agent would not pay upon signal \(1\), the predictor gives nothing.

If the agent receives signal \(1\), paying costs \$1,000 and has no further benefit. If the agent receives signal \(0\), the payoff depends on the predictor’s earlier prediction, while the agent’s current action is trivial.

The two relevant policies are:

\[
\pi_{\text{pay}}(1)=\text{pay}, \qquad
\pi_{\text{refuse}}(1)=\text{refuse}.
\]

If \(D = \pi_{\text{pay}}\), the predictor predicts payment in signal \(1\), so signal \(0\) yields \$1,000,000. Signal \(1\) yields \(-\$1,000\). Therefore

\[
\operatorname{EU}(\pi_{\text{pay}})
=
\frac12 \cdot 1{,}000{,}000
+
\frac12 \cdot (-1{,}000)
=
499{,}500.
\]

If \(D = \pi_{\text{refuse}}\), the predictor predicts refusal, so no reward is given. The expected utility is \(0\).

P-FDT chooses \(\pi_{\text{pay}}\). If the actual signal is \(0\), the agent receives the reward. If the actual signal is \(1\), the agent pays. The important point is that the payoff in signal \(0\) depends on the policy’s off-path behavior in signal \(1\).

An action-only theory that intervenes only on the act performed after the actual signal may miss this dependency unless it treats the whole policy as the relevant counterfactual variable. P-FDT treats the policy itself as the object of control.

---

## 8. P-FDT in multi-agent settings

In multi-agent problems, each agent may have her own policy-selection node. For agents \(i=1,\dots,n\), let

\[
D_i \in \Pi_i
\]

be the policy selected by agent \(i\)’s decision procedure.

Agent \(i\) using P-FDT evaluates

\[
\operatorname{EU}_i(\pi_i)
=
\mathbb{E}\!\left[ V_i \mid \operatorname{do}(D_i = \pi_i) \right],
\]

while the dependency graph \(G\) specifies how other agents’ predictions, policies, and actions respond to \(D_i\).

If the other agents are merely causally affected by agent \(i\)’s actions, then P-FDT resembles ordinary strategic reasoning. But if the other agents predict or simulate agent \(i\)’s policy, then \(G\) should contain edges from \(D_i\) to their predictions or actions.

Consider a psychological twin prisoner’s dilemma. Two agents use the same reasoning procedure. They cannot communicate. If both cooperate, each receives \$1,000,000. If both defect, each receives \$1,000. If one cooperates and the other defects, the defector receives \$1,001,000 and the cooperator receives \$0.

If the twin’s behavior is modeled as subjunctively dependent on the same policy-selection computation, then P-FDT does not evaluate a hypothetical in which I defect while my twin cooperates. That would be like imagining that the same arithmetic function gives different outputs on the same input. Instead:

- if \(D = \pi_{\text{cooperate}}\), both cooperate, yielding \$1,000,000;
- if \(D = \pi_{\text{defect}}\), both defect, yielding \$1,000.

P-FDT chooses cooperation.

The source notes that policy selection may matter most in multi-agent dilemmas, but it does not give a complete game-theoretic semantics. One unresolved question is how to handle cases where several agents are all using P-FDT and predicting one another. A natural approach is to introduce a policy node for each agent and then solve for a mutually consistent assignment of policies under the relevant subjunctive dependencies. In symmetric cases, one may impose that agents running the same P-FDT procedure select the same policy. In asymmetric cases, each agent’s policy node should be intervened on separately, with the graph determining which predictions co-vary.

This is an area where the source leaves significant work to be done. The core P-FDT rule remains clear, but its multi-agent implementation requires a precise account of logical dependencies between different agents’ decision procedures.

---

## 9. Observations: updateless or conditional?

A subtle issue is how P-FDT should treat actual observations.

In ordinary Bayesian reasoning, an agent updates on evidence. But in problems like transparent Newcomb or mechanical blackmail, the observation itself may be downstream of the agent’s policy. If the agent conditions too strongly on the observation, she may sever the very dependency that makes the problem interesting.

For example, in transparent Newcomb, seeing that box B is full is evidence that the predictor expected the agent to one-box. If the agent conditions on seeing the full box and then asks what action is best, she may conclude that two-boxing is better. But P-FDT says that the policy of two-boxing upon seeing a full box would have made it likely that the box was not full in the first place.

Thus P-FDT should not simply compute

\[
\mathbb{E}[V \mid X=x, \operatorname{do}(D=\pi)]
\]

when \(X\) is itself policy-dependent. Instead, it should evaluate the full policy over the observations that would occur under that policy:

\[
\operatorname{EU}(\pi)
=
\sum_{x \in \mathcal X}
P(X=x \mid \operatorname{do}(D=\pi))
\,
U(\pi(x), x).
\]

After selecting \(\pi^{*}\), the agent applies it to the actual input \(x\).

This is an interpretive proposal, not a fully explicit rule in the source. The footnote says the agent chooses a policy and then “applies her inputs” to it. I take this to mean that actual inputs determine which component of the policy is executed, but they should not be used in a way that destroys the subjunctive dependencies between the policy and predictor-controlled observations.

If an observation is genuinely exogenous—meaning it is not produced by prediction, simulation, or dependence on the agent’s policy—then ordinary conditioning is safe. If the observation is predictor-mediated, P-FDT should treat it as a variable that may counterfactually change when the policy changes.

---

## 10. Open questions and operational assumptions

Several important questions are left open by the source’s brief policy-selection passage.

### 1. What is the policy space?

The footnote says a policy “maps inputs to actions.” It does not specify whether inputs are raw observations, full histories, or something more abstract. In practice, I assume the policy space should be chosen to match the decision problem: one-shot problems use observation-to-action maps; sequential problems use history-to-action maps.

For bounded agents, the full space \(\Pi\) may be too large to search. A realistic P-FDT agent would maximize over feasible or representable policies. The normative ideal, however, is still maximization over the relevant policy class.

### 2. How is the subjunctive dependency graph constructed?

The source explicitly says that deducing subjunctive dependencies from observation and experiment is a major open problem. P-FDT needs a graph \(G\) that tells us how changing the policy node affects other variables.

My operational rule is:

- If a process computes, predicts, simulates, or copies the agent’s policy-selection procedure, connect it to \(D\).
- If a process is merely correlated with the agent’s behavior through a common cause that does not represent the procedure, do not connect it to \(D\).
- If a process is causally downstream of the action, connect it to \(A\), where \(A = D(X)\).

This is enough for many classic problems, but it is not a complete learning procedure.

### 3. How should P-FDT handle actual evidence?

As discussed above, I propose that P-FDT updates its model about exogenous facts but evaluates policies without conditioning away policy-dependent observations. This gives P-FDT an updateless flavor in cases where observations are themselves consequences of predictors’ responses to the agent’s policy.

This interpretation is consistent with the source’s treatment of transparent Newcomb, mechanical blackmail, and Parfit’s hitchhiker, but the footnote itself does not settle the issue.

### 4. How should multiple P-FDT agents reason?

The source says policy selection matters in multi-agent dilemmas but does not give a full game-theoretic account. A plausible extension is to give each agent a policy node and specify subjunctive dependencies among them. In symmetric cases, agents using the same P-FDT procedure may be treated as implementing the same policy function; in asymmetric cases, each agent’s policy should be evaluated separately under the appropriate graph.

This is perhaps the most important direction for future development.

### 5. What is the correct account of counterpossible reasoning?

P-FDT requires agents to reason about what would happen if a mathematical computation had a different output. This is counterpossible reasoning in the strict sense. The source acknowledges that no fully satisfactory account is currently available.

For human applications, we usually rely on informal modeling: we ask which facts would remain fixed and which would change if the decision procedure had a different output. P-FDT is usable insofar as those judgments are reliable.

---

## 11. Conclusion

Policy functional decision theory, P-FDT, is the policy-based version of the decision theory introduced by Yudkowsky and Soares. Its central idea is that rational choice is not primarily about selecting a physical act, but about selecting the output of a fixed mathematical policy-selection procedure. The agent asks:

> Which policy, if output by this very procedure, would yield the best expected outcome?

Formally, P-FDT chooses

\[
\pi^{*}
\in
\arg\max_{\pi \in \Pi}
\mathbb{E}[V \mid \operatorname{do}(D=\pi)]
\]

and then executes \(\pi^{*}(x)\), where \(x\) is the actual input.

This allows P-FDT to preserve decision-relevant subjunctive dependencies—predictors, copies, simulations, and other agents’ models of the agent’s reasoning—while ignoring merely evidential correlations such as smoking lesions. It one-boxes in Newcomb’s problem, smokes in the smoking lesion problem, pays in Parfit’s hitchhiker problem, one-boxes in transparent Newcomb, and can choose policies partly because of their off-path behavior.

The source’s footnote gives only a sketch. The mathematical reconstruction above fills in some gaps by introducing explicit policy spaces, dependency graphs, and an operational rule for handling observations. The largest unresolved problems remain the construction of subjunctive dependency graphs, the treatment of counterpossible reasoning, and the extension to multi-agent strategic equilibria. But even with these open questions, P-FDT gives a clear and powerful principle: choose the policy that would produce the best world if it were the output of your decision procedure, and then follow it.

---

### Reference

Yudkowsky, Eliezer, and Nate Soares. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2. The policy-selection passage used as the primary source for P-FDT appears in footnote 16.