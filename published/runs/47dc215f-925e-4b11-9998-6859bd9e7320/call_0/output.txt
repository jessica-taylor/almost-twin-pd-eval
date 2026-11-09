# Policy Functional Decision Theory

## Introduction

Functional decision theory, as presented by Yudkowsky and Soares, is built around a simple normative idea: a rational agent should treat her decision as the output of a fixed mathematical function and ask, “Which output of this very function would yield the best outcome?” The paper’s official formalization usually applies this idea to actions: given an observation history \(x\), the agent intervenes on a variable representing the output of the decision function on that input and chooses the action with highest expected utility.

But footnote 16 of the paper points toward a more policy-oriented version:

> “the author’s preferred formulation of FDT actually intervenes on the node \(\mathrm{FDT}(-)\) to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action.”

I will call this policy-level theory **P-FDT**, for *policy functional decision theory*. The source generally calls the theory FDT, and it does not give a full formal equation for the policy version. Much of what follows is therefore a reconstruction: I will take the footnote’s policy-selection idea seriously, develop a workable mathematical formulation, and mark places where the source is silent and where I am adding operational assumptions.

The essential claim of P-FDT is this: the object of rational choice is not merely a physical action here and now, but a contingent plan—a mapping from possible observations or inputs to actions. The agent asks which output of her policy-selection function would produce the best world, once all relevant subjunctive dependencies are taken into account. She then applies the chosen policy to her actual input.

---

## 1. From actions to policies

Let \(\mathcal X\) be a set of observation histories or inputs, \(\mathcal A\) a finite set of actions, and \(\mathcal O\) a set of outcomes. A utility function \(\mathcal U:\mathcal O\to\mathbb R\) assigns value to outcomes. A deterministic policy is a function

\[
\pi:\mathcal X\to\mathcal A.
\]

Let \(\Pi\) be the set of policies under consideration. In the simplest case, \(\mathcal X\) has one element, so a policy is just an action. In richer cases, a policy specifies what the agent would do after each possible observation.

The agent maintains a world-model \(M=(P,G)\). Here \(P\) is a probability distribution over relevant variables, and \(G\) is a dependency structure describing how those variables would change under interventions. The source uses Pearl-style causal graphs for CDT and then generalizes the idea: for FDT, \(G\) must encode not only causal dependencies but also logical, computational, and predictive dependencies. I will call these **subjunctive dependencies**, following the source.

P-FDT adds a special variable to the model:

\[
\Phi_M = \text{“the policy selected by P-FDT given model }M\text{.”}
\]

This variable is self-referential: the model contains a representation of the agent’s own policy-selection function. The source notes that this kind of self-reference is not fatal; one can construct data structures that represent themselves, analogously to Kleene’s recursion theorem.

The central P-FDT rule, as I reconstruct it, is:

\[
\mathrm{P\text{-}FDT}(M)
=
\arg\max_{\pi\in\Pi}
\mathbb E_P\!\left[V \mid \operatorname{do}(\Phi_M=\pi)\right],
\]

where \(V=\mathcal U(\text{Outcome})\), and \(\operatorname{do}(\Phi_M=\pi)\) means: set the policy-selection node to output \(\pi\), then propagate that change through the dependency structure \(G\). The agent then receives or finds herself with some actual input \(x\in\mathcal X\), and executes

\[
a = \pi^*(x),
\]

where \(\pi^*\) is the maximizing policy.

If there is some background information \(h\) that is genuinely exogenous to the policy—meaning the policy cannot affect whether \(h\) obtains—then it is reasonable to condition on it:

\[
\mathrm{P\text{-}FDT}(M,h)
=
\arg\max_{\pi\in\Pi}
\mathbb E_P\!\left[V \mid \operatorname{do}(\Phi_M=\pi), H=h\right].
\]

But if an observation is itself endogenous—if predictors, blackmailers, or other agents decide whether the agent receives that observation on the basis of their predictions of her policy—then P-FDT should not condition that observation away when evaluating policies. Instead, the observation is a downstream variable in the graph, and its counterfactual value may change when the policy node changes.

This is one of the most important interpretive choices in P-FDT. The source does not fully settle it, but it is strongly suggested by the paper’s treatment of cases where agents “should entertain the hypothesis that, if their action were different, they might have made different observations.” My operational proposal is therefore:

1. Condition on facts that are fixed before and unaffected by the policy.
2. Do not condition on observations whose occurrence depends subjunctively on the policy.
3. After selecting the policy, apply it to the actual observation.

This gives P-FDT an updateless flavor: the policy is evaluated from a global perspective, not by first conditioning on every actual observation and then choosing locally.

---

## 2. How P-FDT differs from EDT, CDT, and action-based FDT

It is useful to compare P-FDT with the other theories discussed in the source.

Evidential decision theory, EDT, chooses an action by conditionalization:

\[
\mathrm{EDT}(P,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E[V\mid \Obs=x,\Act=a].
\]

It asks: “Which action would be the best news?”

Causal decision theory, CDT, intervenes on the physical action variable:

\[
\mathrm{CDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E[V\mid \operatorname{do}(\Act=a),\Obs=x].
\]

It asks: “Which physical act causes the best downstream consequences?”

The action-based FDT equation in the source intervenes on a logical variable representing the output of the FDT decision function given the current observation:

\[
\mathrm{FDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E[V\mid \operatorname{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)].
\]

P-FDT replaces the action variable with a policy variable:

\[
\mathrm{P\text{-}FDT}(P,G)
=
\arg\max_{\pi\in\Pi}
\mathbb E[V\mid \operatorname{do}(\Phi_{P,G}=\pi)].
\]

The agent then uses the actual observation \(x\) as input to the selected policy.

The difference is subtle but important. Action-based FDT asks what the decision function should output on a particular input. P-FDT asks what entire input-to-output mapping the policy-selection function should output. In many single-agent problems, this makes no practical difference. If there is only one relevant input, a policy is effectively an action. But in problems involving predictions, sequential structure, or other agents, the policy itself may be what other systems model, predict, or respond to.

---

## 3. Subjunctive dependence and counterfactuals

P-FDT depends on the notion of **subjunctive dependence** introduced in the source. Two systems are subjunctively dependent on a function when their behavior tracks the output of that function. Two calculators computing the same arithmetic expression are subjunctively dependent on the arithmetic function, even if causally independent. A predictor who accurately models an agent’s decision procedure is subjunctively dependent on that procedure. Causal dependence is a special case of subjunctive dependence, but mere statistical correlation is not.

This distinction is what separates Newcomb-like cases from the smoking lesion problem. In Newcomb’s problem, the predictor’s behavior depends on a representation of the agent’s decision function. In the smoking lesion problem, the lesion does not model the agent’s decision function; it merely causes both a preference for smoking and cancer. Therefore, a P-FDT agent’s policy node is connected to the predictor’s prediction in the Newcomb graph, but not connected to the cancer variable in the smoking lesion graph.

The intervention \(\operatorname{do}(\Phi_M=\pi)\) is not an ordinary physical intervention. If the agent’s policy-selection function deterministically outputs one policy, then imagining that it outputs another policy is a counterpossible: a counterfactual whose antecedent is logically impossible. The source acknowledges this difficulty. P-FDT inherits it. The theory does not require a complete metaphysics of counterpossibles; it requires only a working model \(G\) that says how the world would differ if the policy-selection function had a different output.

Operationally, one can think of \(G\) as encoding rules such as:

- If \(\Phi_M=\pi\), then the agent’s physical action at input \(x\) is \(\pi(x)\).
- If a predictor accurately models \(\Phi_M\), then the predictor’s prediction changes when \(\Phi_M\) changes.
- If another agent’s strategy depends on their prediction of \(\Phi_M\), then their action changes when \(\Phi_M\) changes.
- If a lesion or weather variable is merely statistically correlated with the agent’s behavior, it does not change when \(\Phi_M\) changes.

Thus P-FDT preserves correlations that arise from shared computation or accurate prediction, while breaking correlations that are merely evidential.

---

## 4. Examples

### 4.1 Newcomb’s problem

In standard Newcomb’s problem, the agent can take one box or two boxes. A predictor placed \$1,000,000 in the opaque box iff she predicted the agent would one-box. The predictor is correct 99% of the time.

Here there is only one relevant observation, so policies reduce to actions. Let \(\pi_1\) be the one-boxing policy and \(\pi_2\) the two-boxing policy. The P-FDT graph connects the policy node to both the agent’s action and the predictor’s earlier prediction.

If \(\Phi=\pi_1\), then with probability \(0.99\) the predictor predicted one-boxing and the big box is full; with probability \(0.01\) it is empty. Expected utility:

\[
\mathbb E[V\mid \operatorname{do}(\Phi=\pi_1)]
=
0.99(1{,}000{,}000)+0.01(0)
=
990{,}000.
\]

If \(\Phi=\pi_2\), then with probability \(0.99\) the predictor predicted two-boxing and the big box is empty; with probability \(0.01\) it is full. Expected utility:

\[
\mathbb E[V\mid \operatorname{do}(\Phi=\pi_2)]
=
0.99(1{,}000)+0.01(1{,}001{,}000)
=
11{,}000.
\]

P-FDT selects the one-boxing policy.

CDT two-boxes because it intervenes only on the physical action and holds the box contents fixed. EDT one-boxes because one-boxing is good news. P-FDT one-boxes for a different reason: the predictor’s behavior subjunctively depends on the same decision function whose output P-FDT is evaluating.

### 4.2 The smoking lesion problem

In the smoking lesion problem, smoking is correlated with cancer, but only because a lesion causes both a preference for smoking and cancer. Smoking itself does not cause cancer. The agent gains \$1,000 utility from smoking.

Here the P-FDT graph should not connect the policy node to the cancer variable. The lesion is not predicting the agent’s policy. It is a common cause of smoking preference and cancer, but it is not computing the agent’s decision function.

Therefore, when P-FDT evaluates the smoking policy versus the refraining policy, the probability of cancer remains fixed across the two hypothetical interventions. Smoking adds utility without changing the chance of cancer. P-FDT smokes.

This illustrates the asymmetry at the heart of the theory: predictor-like variables are counterfactually sensitive to the agent’s policy; lesion-like variables are not.

### 4.3 Transparent Newcomb and Parfit’s hitchhiker

The policy formulation becomes more illuminating in cases where the agent receives an observation that is itself produced by a predictor.

In the transparent Newcomb problem, both boxes are visible. The predictor placed \$1,000,000 in box B iff she predicted that the agent would one-box upon seeing that both boxes are full. The agent may therefore face the choice while seeing two full boxes.

Let the observation set be

\[
\mathcal X=\{\text{full},\text{empty}\},
\]

and the action set be

\[
\mathcal A=\{\text{one},\text{two}\}.
\]

Consider two policies:

\[
\pi_O(\text{full})=\text{one},\quad \pi_O(\text{empty})=\text{two},
\]

\[
\pi_T(\text{full})=\text{two},\quad \pi_T(\text{empty})=\text{two}.
\]

The predictor fills the box iff she predicts that the agent will one-box upon seeing a full box. Thus the policy node affects the predictor’s prediction, which affects whether the agent sees a full box, which affects which branch of the policy is executed.

If the predictor is 99% accurate, then under \(\pi_O\):

\[
\mathbb E[V\mid \operatorname{do}(\Phi=\pi_O)]
=
0.99(1{,}000{,}000)+0.01(1{,}000)
=
990{,}010.
\]

The small second term comes from the case where the predictor is wrong, the box is empty, the agent sees “empty,” and \(\pi_O\) takes both boxes for \$1,000.

Under \(\pi_T\):

\[
\mathbb E[V\mid \operatorname{do}(\Phi=\pi_T)]
=
0.01(1{,}001{,}000)+0.99(1{,}000)
=
11{,}000.
\]

P-FDT therefore selects \(\pi_O\). If the agent actually sees a full box, she one-boxes.

This is the policy-level analogue of the source’s claim that FDT one-boxes in the transparent Newcomb problem. It also matches Parfit’s hitchhiker problem. The driver helps the agent iff the driver predicts that the agent will pay after reaching the city. A P-FDT agent adopts the policy “pay if rescued,” because being the kind of agent who pays is what causes rescue. Upon reaching the city, the agent pays.

A purely local question—“Given that I am already in the city, should I pay?”—misrepresents the decision. The policy that gets you into the city is the same policy that requires paying once you are there. P-FDT evaluates the whole contingent plan.

### 4.4 Mechanical blackmail

Suppose a blackmailer runs a harmful program iff she predicts the agent will pay upon receiving a blackmail letter. If the agent receives the letter, paying stops the program at a small cost; refusing allows a large loss.

A local CDT or EDT calculation may say: given that the letter has arrived, paying avoids the larger loss. But P-FDT evaluates policies. The relevant policies include:

\[
\pi_{\text{pay}}(\text{letter})=\text{pay},
\]

\[
\pi_{\text{refuse}}(\text{letter})=\text{refuse}.
\]

If the blackmailer accurately predicts the agent’s policy, then a paying policy makes blackmail likely, while a refusing policy makes blackmail unlikely. The P-FDT graph connects the policy node to the blackmailer’s prediction and therefore to the probability of receiving the letter.

With a small error rate \(e\), the refusing policy may have expected loss approximately

\[
e\cdot 1{,}000{,}000,
\]

because the agent is blackmailed only when the blackmailer mistakenly predicts payment. The paying policy may have expected loss close to

\[
1{,}000,
\]

because the blackmailer predicts payment and sends the letter. If \(e\) is small enough, the refusing policy has lower expected loss. P-FDT then selects the refusing policy. If the agent actually receives the letter, she still refuses, because the selected policy maps “letter” to “refuse.”

This may seem harsh or strange. The source acknowledges the strangeness but defends it by the argument from utility: agents with the refusing policy are less often blackmailed. P-FDT does not ignore the letter; it treats the letter as an input to the selected policy. What it refuses to do is evaluate the policy by first conditioning on the letter as though the letter were independent of the policy.

---

## 5. Policy dependencies in multi-agent cases

Footnote 16 says that the policy formulation matters mainly in multi-agent dilemmas. The source does not develop a full multi-agent formalization, so this is an area where interpretation is required.

The natural idea is this: in multi-agent settings, other agents may not merely predict your current action. They may predict your entire strategy. Their actions may depend on what your policy would do in branches of the decision tree that are not currently actual. P-FDT is therefore well suited to cases where credibility, commitment, coordination, and reciprocal prediction matter.

For example, suppose another agent will cooperate with you only if they predict that your policy will cooperate in a future contingency. If your current action alone is evaluated, you might be tempted to defect in that future contingency. But if the other agent’s present behavior depends on their model of your full policy, then the policy-level intervention captures the fact that choosing a cooperative policy changes their behavior now.

This resembles game-theoretic strategy selection, but with a crucial difference: P-FDT does not merely choose a strategy as a physical commitment device. It treats the policy-selection function itself as a mathematical object whose output can be predicted, simulated, or instantiated by other agents. If another agent is running a sufficiently accurate model of your policy-selection function, then their behavior subjunctively depends on your policy output.

The source is cautious: it says the difference between action-based FDT and policy-based FDT only matters in multi-agent dilemmas “so far as we can tell.” That caution should be preserved. P-FDT is best understood as an extension of FDT’s core principle, not as a fully completed formal theory.

---

## 6. Open questions and operational assumptions

Because the policy-selection passage is brief, several important questions remain unresolved.

### 6.1 What policies are available?

The source does not specify the policy space \(\Pi\). In idealized theory, one might take \(\Pi=\mathcal A^{\mathcal X}\), the set of all functions from observations to actions. In practice, this is far too large. An operational P-FDT agent must restrict \(\Pi\) to computable, representable, or salient policies.

This restriction matters. If the optimal policy is not in \(\Pi\), P-FDT chooses the best available policy. That is not necessarily a defect; all real decision procedures face bounded policy spaces. But it means P-FDT’s prescription is relative to the agent’s modeling resources.

### 6.2 How is the subjunctive graph constructed?

The source identifies this as the largest open problem for FDT, and it remains open for P-FDT. CDT can appeal, at least in principle, to Pearl’s methods for learning causal structure. P-FDT needs a way to learn or infer logical and computational dependencies: which predictors, simulations, twins, or other agents depend on the agent’s policy-selection function?

A reasonable operational rule is:

- Add a dependency from \(\Phi_M\) to any variable whose generating process contains a sufficiently accurate representation of \(\Phi_M\) or of the agent’s relevant behavior.
- Do not add such a dependency for variables that are merely correlated with the agent’s action through non-representational common causes.
- Use predictor accuracy, simulation fidelity, and known copying relationships to assign probabilities.

This is a heuristic, not a full foundation.

### 6.3 Which observations may be conditioned on?

P-FDT must distinguish exogenous observations from endogenous observations. If an observation is known to be unaffected by the policy, conditioning on it is appropriate. If the observation is itself produced by a predictor or by a process that depends on the policy, conditioning on it can destroy the decision-relevant dependency.

The source’s discussion of transparent Newcomb and blackmail suggests that P-FDT should not treat endogenous observations as fixed when evaluating policies. My proposed interpretation is that P-FDT evaluates policies from the perspective of the decision problem as a whole, then applies the chosen policy to the actual observation.

### 6.4 Deterministic or stochastic policies?

The source’s examples are mostly deterministic. P-FDT can be extended to stochastic policies, where \(\pi(x)\) is a distribution over actions. Then \(\Phi_M\) selects a stochastic policy, and the expected utility calculation integrates over the resulting randomness. However, if predictors can predict the agent’s randomizing process, that too must be represented in \(G\). The source does not settle this point.

### 6.5 Counterpossible reasoning

P-FDT requires reasoning about counterpossibles: “What if this very policy-selection function had output a different policy?” The source admits that no fully satisfactory account of counterpossible reasoning is available. P-FDT does not solve that problem; it makes the problem more visible. In practice, human reasoners seem able to approximate such reasoning by asking how predictors, simulations, and similar agents would respond if the agent’s reasoning concluded differently.

---

## 7. Why P-FDT is attractive

P-FDT has several appealing features.

First, it unifies many cases. It one-boxes in Newcomb’s problem, smokes in the smoking lesion problem, pays in Parfit’s hitchhiker problem, one-boxes in transparent Newcomb when appropriate, and resists blackmail when resistance is predictably beneficial.

Second, it acts as if optimally precommitted. The agent does not need an actual binding device. She simply selects the policy whose adoption would produce the best expected world.

Third, it respects information. Because P-FDT evaluates policies globally, it need not fear endogenous information. Seeing a full box or receiving a blackmail letter may be bad news under some local conditional calculation, but P-FDT asks whether the policy that would take the locally attractive action is globally advantageous.

Fourth, it gives a clearer account of strategic commitment. In multi-agent settings, what matters is often not a single action but a whole pattern of behavior. P-FDT treats that pattern as the primary object of choice.

---

## Conclusion

Policy functional decision theory, P-FDT, is the policy-level version of functional decision theory suggested by the footnote in which the authors say their preferred formulation “intervenes on the node \(\mathrm{FDT}(-)\) to choose not an action but a policy which maps inputs to actions.” The core idea is that rational choice consists in selecting the output of a fixed policy-selection function: the agent imagines counterfactually that this function outputs different policies, propagates that change through all relevant subjunctive dependencies, and selects the policy that yields the best expected outcome. She then applies that policy to her actual observations.

The formal equation I have proposed is:

\[
\mathrm{P\text{-}FDT}(M)
=
\arg\max_{\pi\in\Pi}
\mathbb E[V\mid \operatorname{do}(\Phi_M=\pi)].
\]

This is a reconstruction rather than a direct quotation from the source, but it preserves the paper’s central commitments: expected utility maximization, intervention on a logical rather than merely physical variable, and sensitivity to predictor-like subjunctive dependencies rather than mere statistical correlations.

P-FDT leaves important problems open, especially the construction of subjunctive dependency graphs, the treatment of counterpossibles, and the precise handling of policy spaces in multi-agent games. But as a normative guide, it offers a clear rule: do not merely ask what action is best given the news, or what action causes the best local consequences. Ask which contingent policy, if it were the output of your decision procedure, would make the world go best—and then follow it.

---

### Reference

Yudkowsky, E., and Soares, N. “Functional Decision Theory: A New Theory of Instrumental Rationality.” arXiv:1710.05060.