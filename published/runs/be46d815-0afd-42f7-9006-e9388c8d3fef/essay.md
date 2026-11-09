# Policy Functional Decision Theory: Choosing the Best Output of a Fixed Policy Function

Policy Functional Decision Theory, which I will call **P-FDT**, is a decision theory for agents who treat their decisions as the outputs of a fixed mathematical procedure. The version discussed here is the policy-selection formulation identified in footnote 16 of Yudkowsky and Soares’s paper on functional decision theory:

> “the author’s preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action.”

The paper’s main text mostly presents an action-level version of functional decision theory, where the agent asks what would happen if her decision procedure, given her current observations, output one action rather than another. P-FDT instead asks a broader question:

> Which policy, as the output of this very policy-selection procedure, would yield the best expected outcome?

The agent then applies the selected policy to her actual observations. This small shift matters when predictors, copies, or other agents depend not merely on the agent’s present action but on her general disposition to act across possible inputs.

I will use **P-FDT** for this policy-level theory. I will identify **evidential decision theory** as EDT and **causal decision theory** as CDT.

---

## 1. From actions to policies

Let:

- \(\mathcal X\) be a set of possible observation histories or inputs;
- \(\mathcal A\) be a finite set of actions;
- \(\Pi = \mathcal A^{\mathcal X}\) be the set of deterministic policies, where a policy \(\pi \in \Pi\) is a function \(\pi : \mathcal X \to \mathcal A\);
- \(\mathcal O\) be a set of outcomes;
- \(\mathcal U : \mathcal O \to \mathbb R\) be a bounded utility function.

A P-FDT agent does not first ask, “What action should I take now?” Instead, she asks, “Which policy should my policy-selection procedure output?” Once the policy \(\pi\) has been selected, the actual action is simply

\[
a = \pi(x),
\]

where \(x \in \mathcal X\) is the agent’s actual input or observation.

In simple one-shot problems with only one possible observation, policies collapse to actions. In such cases P-FDT gives the same prescriptions as the action-level functional decision theory described in the source. The distinctive behavior of P-FDT appears when the agent may receive different inputs, and when other processes depend on what the agent would do under those different inputs.

---

## 2. A formal model for P-FDT

Following the graphical treatment of decision theories in the source, suppose the agent has a world-model \((P, G)\):

- \(P\) is a subjective probability distribution over relevant variables;
- \(G\) is a graph or structural model describing how changes to some variables would affect others.

For CDT, \(G\) encodes causal structure. For P-FDT, \(G\) must encode a broader class of dependencies: causal dependencies, but also what the source calls **subjunctive dependencies**, such as the dependence of a reliable predictor’s prediction on the agent’s decision procedure.

Introduce a distinguished variable

\[
S \in \Pi,
\]

whose value is the policy output by the agent’s policy-selection procedure. In the source’s notation, this is roughly the node “FDT(-)”; in this essay, I write it as the P-FDT policy node.

A natural P-FDT decision rule is then:

\[
\pi^\* \in \argmax_{\pi \in \Pi}
\mathbb E_P\!\left[ V \mid \operatorname{do}_G(S = \pi),\ E = e \right],
\]

where:

- \(V = \mathcal U(\text{Outcome})\) is the utility variable;
- \(\operatorname{do}_G(S=\pi)\) is an intervention setting the policy-selection node to output \(\pi\);
- \(e\) is background evidence that the agent may condition on before choosing the policy.

After selecting \(\pi^\*\), the agent observes her actual input \(x\) and performs

\[
a = \pi^\*(x).
\]

This is my reconstruction of the policy-selection idea in footnote 16. The source does not give a full equation for P-FDT, so the exact treatment of evidence and observations requires interpretation. I return to that below.

For comparison:

**EDT** evaluates actions by conditioning:

\[
\operatorname{EDT}(P,x)
=
\argmax_{a \in \mathcal A}
\mathbb E[V \mid X=x,\ A=a].
\]

**CDT** evaluates actions by causal intervention on the physical action:

\[
\operatorname{CDT}(P,G,x)
=
\argmax_{a \in \mathcal A}
\mathbb E[V \mid X=x,\ \operatorname{do}(A=a)].
\]

The paper’s action-level **FDT** evaluates actions by intervening on a logical variable representing the output of the decision procedure given the current observation:

\[
\operatorname{FDT}(P,G,x)
=
\argmax_{a \in \mathcal A}
\mathbb E[V \mid \operatorname{do}(\operatorname{FDT}(P,G,x)=a)].
\]

P-FDT replaces the observation-indexed action node with a policy node:

\[
\operatorname{P\text{-}FDT}(P,G,e)
=
\argmax_{\pi \in \Pi}
\mathbb E[V \mid \operatorname{do}(S=\pi),\ E=e].
\]

The agent then applies the winning policy to her actual input.

---

## 3. What P-FDT holds fixed, and what it changes

The central normative idea is that P-FDT’s hypotheticals should preserve all decision-relevant dependencies on the agent’s policy-selection procedure, while breaking merely evidential correlations.

Suppose \(Z\) is some variable in the agent’s model. When P-FDT considers the hypothetical where \(S=\pi\) instead of \(S=\pi'\), it changes \(Z\) only if \(Z\) subjunctively depends on the policy-selection procedure.

### Predictor-like dependencies

If a predictor has modeled the agent’s policy and acts on that model, then the predictor’s behavior should be treated as dependent on \(S\). If \(S\) were counterfactually different, the predictor’s prediction would be different.

For example, if a driver will give a ride only if she predicts the agent will later pay, then the driver’s action depends on the agent’s policy. In P-FDT’s hypotheticals, changing the policy changes the driver’s prediction and therefore the driver’s action.

### Lesion-like dependencies

If a variable is merely statistically correlated with the agent’s behavior but does not represent, predict, or compute the agent’s policy, then P-FDT holds it fixed under intervention.

In the smoking lesion problem, the lesion causes both a preference for smoking and cancer, but it does not predict the agent’s decision procedure. Therefore, P-FDT’s hypotheticals leave the probability of the lesion unchanged when imagining a different policy output. P-FDT therefore smokes, just as action-level FDT does.

### Counterpossible reasoning

The source acknowledges a difficulty: if the agent’s policy-selection procedure is deterministic, then on a given input it has only one possible output. To compare hypothetical policies, P-FDT must reason about scenarios in which the very same mathematical function has a different output. These are counterpossibles.

The source’s response is that this is a technical problem, not a fatal philosophical objection. Human reasoners can entertain mathematical counterpossibles in limited ways. For P-FDT, the needed reasoning is often local: “If this policy-selection procedure had output \(\pi'\), how would predictors, copies, or other agents that depend on it behave?”

Still, the source does not provide a complete account of how to construct the graph \(G\) encoding these subjunctive dependencies. This is an open problem inherited by P-FDT.

---

## 4. Observations: condition or model as inputs?

A delicate issue is how P-FDT should handle the agent’s actual observation \(x\).

The source says that action-level FDT responds to observations not by simple Bayesian conditioning, but by changing which decision-function node it intervenes on. In the transparent Newcomb problem, for instance, an agent who sees a full box intervenes on the variable representing what FDT would output upon seeing a full box.

P-FDT handles this differently. The agent does not choose an action directly for each observation. She chooses a policy \(\pi\), and the observation becomes an input to that policy.

This raises an operational question: should the expected utility of \(\pi\) be conditioned on the actual observation \(x\)?

My operational interpretation is:

- If \(x\) is background evidence that is not counterfactually affected by the policy, then it may be included in \(e\) and conditioned on.
- If \(x\) is a decision-relevant input that could itself have been different under a different policy, then it should not be rigidly conditioned away. Instead, it should be represented in the graph as an input variable whose distribution may change under \(\operatorname{do}(S=\pi)\).

This distinction is essential in blackmail and predictor problems. If the agent has received a blackmail letter, and whether she receives the letter depends on the blackmailer’s prediction of her policy, then conditioning on “I received the letter” can make payment look attractive. But P-FDT should evaluate the whole policy: a policy of refusing payment may make it likely that the letter is never sent.

Thus, a reasonable P-FDT rule is:

\[
\pi^\*
=
\argmax_{\pi \in \Pi}
\mathbb E[V \mid \operatorname{do}(S=\pi),\ E=e],
\]

where \(e\) contains only evidence treated as upstream of or independent from the policy-selection node. The actual input \(x\) is then fed into \(\pi^\*\).

This is not spelled out fully in the source, but it seems to me the most faithful operational reading of the policy-selection passage.

---

## 5. Example: P-FDT in the transparent Newcomb problem

In the transparent Newcomb problem, the agent can see whether box B is full. The predictor filled box B iff she predicted that the agent would leave box A behind upon seeing two full boxes.

Let:

\[
\mathcal X = \{\text{full}, \text{empty}\},
\]

\[
\mathcal A = \{\text{one-box}, \text{two-box}\}.
\]

Consider two policies:

\[
\pi_1(\text{full}) = \text{one-box}, \quad
\pi_1(\text{empty}) = \text{two-box};
\]

\[
\pi_2(\text{full}) = \text{two-box}, \quad
\pi_2(\text{empty}) = \text{two-box}.
\]

Assume the predictor is correct with probability \(0.99\).

Under \(\operatorname{do}(S=\pi_1)\), the predictor usually predicts that the agent will one-box upon seeing a full box, so she fills box B. The agent sees a full box and one-boxes, receiving about \$1,000,000. With probability \(0.01\), the predictor errs, leaves the box empty, and the agent two-boxes, receiving about \$1,000. So:

\[
\mathbb E[V \mid \operatorname{do}(S=\pi_1)]
\approx
0.99 \cdot 1{,}000{,}000
+
0.01 \cdot 1{,}000
=
990{,}010.
\]

Under \(\operatorname{do}(S=\pi_2)\), the predictor usually predicts two-boxing upon seeing a full box, so she leaves box B empty. The agent usually sees an empty box and receives \$1,000. With probability \(0.01\), the predictor mistakenly fills the box, and the agent two-boxes, receiving \$1,001,000. So:

\[
\mathbb E[V \mid \operatorname{do}(S=\pi_2)]
\approx
0.99 \cdot 1{,}000
+
0.01 \cdot 1{,}001{,}000
=
11{,}000.
\]

P-FDT therefore selects \(\pi_1\). If the agent actually sees a full box, she one-boxes.

This is the policy-level analogue of the source’s claim that FDT one-boxes in the transparent Newcomb problem and pays the driver in Parfit’s hitchhiker problem. The agent behaves as she would have wanted to precommit to behave.

---

## 6. Example: P-FDT and blackmail

Consider the mechanical blackmail problem. A blackmailer has a program that will publish damaging information, costing the agent \$1,000,000, unless the agent pays \$1,000. The blackmailer runs the program only if she predicts that the agent will pay upon receiving the blackmail letter.

Let:

\[
\mathcal X = \{\text{letter}, \text{no letter}\},
\]

\[
\mathcal A = \{\text{pay}, \text{refuse}\}.
\]

Consider the policies:

\[
\pi_{\text{pay}}(\text{letter}) = \text{pay};
\]

\[
\pi_{\text{refuse}}(\text{letter}) = \text{refuse}.
\]

Under a policy of paying, the blackmailer predicts payment and sends the letter. The agent pays and loses \$1,000.

Under a policy of refusing, the blackmailer predicts refusal and does not send the letter. The agent loses nothing.

P-FDT therefore selects the refusing policy. If the agent nevertheless receives the letter, she refuses to pay.

This may seem odd: the agent is holding the letter, so surely the blackmailer predicted wrongly? P-FDT’s answer is that the evaluation of the policy should not be restricted to the branch where the letter is received. The hypothetical where the agent’s policy-selection procedure outputs a refusing policy is usually a hypothetical where the blackmailer never sends the letter.

This is one of the places where P-FDT, like the source’s action-level FDT, departs sharply from EDT. EDT conditions on receiving the letter and on paying, which makes paying look like good news. P-FDT intervenes on the policy and allows the probability of receiving the letter itself to vary.

---

## 7. Why policies matter in multi-agent cases

The source says that the policy-selection formulation matters mainly in multi-agent dilemmas. The reason is not hard to see. In multi-agent settings, other agents often do not merely predict your current action. They predict your strategy: what you would do under various possible observations.

For example, in an extensive-form game, another player may move before observing your action, but after forming beliefs about your policy. If you choose only your current action while leaving your counterfactual behavior unspecified, you may fail to control the part of the world that depends on your predicted strategy.

A stylized illustration: suppose a principal offers a valuable contract only if she predicts that the agent will perform a costly action in state \(S\) and a different action in state \(T\). The agent will learn which state occurs before acting. If the agent waits until the actual state and optimizes locally, she may choose the cheap action in \(S\), but the principal will predict this and not offer the contract. P-FDT instead chooses the whole policy: “perform the costly action in \(S\); perform the required action in \(T\).” If that policy maximizes expected utility under the principal’s prediction, P-FDT adopts it and thereby receives the contract.

This kind of case is not given explicitly in the source, but it illustrates why the authors say the policy/action distinction matters in multi-agent problems. The relevant object of prediction is often not a single action but an input-output disposition.

---

## 8. P-FDT compared with EDT and CDT

P-FDT can be understood by analogy:

> P-FDT is to subjunctive policy-dependence as CDT is to causal dependence.

CDT imagines changing the physical action while holding fixed all variables not caused by that action. This breaks correlations with predictors that are not downstream of the action, causing CDT to two-box in Newcomb’s problem and to act unstably in Death in Damascus.

EDT imagines receiving news that the agent took a certain action, preserving all statistical correlations. This causes EDT to refrain from smoking in the smoking lesion problem and to pay in certain blackmail problems.

P-FDT imagines changing the output of the agent’s policy-selection procedure. It preserves dependencies involving predictors, copies, simulations, and other agents modeling the agent’s policy. But it does not preserve merely evidential correlations, such as a lesion that causes both smoking and cancer without predicting the agent’s decision procedure.

Thus P-FDT aims to keep the useful part of EDT’s sensitivity to prediction while avoiding EDT’s news-management failures, and to keep CDT’s counterfactual interventionism while avoiding CDT’s neglect of logical and predictive dependencies.

---

## 9. Open questions and operational assumptions

The source’s footnote gives only the core idea of P-FDT. Several questions remain unresolved.

### What evidence should be conditioned on?

I have proposed that P-FDT should condition only on evidence not counterfactually affected by the policy-selection node. Inputs that can themselves vary with the policy should be represented inside the graphical model rather than conditioned away. This preserves the source’s treatment of blackmail and transparent Newcomb problems, but the source does not state the rule in precisely this form.

### How is the subjunctive graph constructed?

The source identifies this as a major open problem for FDT. CDT can appeal to Pearl-style causal discovery, at least in principle. P-FDT needs a graph encoding logical, computational, and predictive dependencies. We do not yet have a fully general method for learning or justifying such graphs from observation.

### Which policies are available?

Formally, \(\Pi\) could be all functions from observations to actions. In practice, bounded agents must restrict attention to computable, feasible, or representable policies. The idealized theory can maximize over all policies; applied versions need approximations.

### How does P-FDT handle logical uncertainty?

P-FDT must assign probabilities to claims about what its own policy-selection procedure would output. The source notes that self-reference is not fatal; Kleene-style recursion or quining can allow a system to represent itself. But a complete account of logical uncertainty remains unfinished.

### How does P-FDT behave in general games?

The source suggests that policy selection matters in multi-agent dilemmas, but does not develop a full game-theoretic account. In games with multiple reflective agents, one may need fixed-point reasoning: each agent’s policy depends on predictions of other agents’ policies. P-FDT likely needs additional machinery to handle such cases rigorously.

These are not merely technical details. They affect how P-FDT should be applied to unfamiliar cases. Still, the central prescription is clear enough for many problems: identify the policy-selection node, identify what subjunctively depends on it, evaluate candidate policies under interventions on that node, and then execute the best policy on the actual input.

---

## 10. Conclusion

Policy Functional Decision Theory treats the object of rational choice as a policy rather than an isolated action. The agent asks which mapping from inputs to actions would yield the best world if it were the output of her very policy-selection procedure. She then applies that policy to her actual observations.

This preserves the core insight of functional decision theory: decisions should be evaluated as outputs of a fixed mathematical procedure, not merely as physical movements. But it refines that insight by recognizing that predictors, other agents, and future choices often depend on the agent’s whole strategy, not only on her present action.

In simple cases, P-FDT agrees with action-level FDT. In transparent Newcomb problems, it one-boxes. In Parfit’s hitchhiker problem, it pays. In blackmail problems, it refuses payment. In lesion problems, it smokes. In multi-agent settings, it chooses policies that account for other agents’ predictions of its behavior across possible inputs.

The theory is elegant, but incomplete. Its main unresolved issue is the construction of the subjunctive dependency graph: how an agent should learn which facts depend on the output of its own policy-selection procedure. Until that problem is solved, P-FDT is best understood as an idealized normative criterion, plus a practical heuristic: when your dispositions are predictable, choose the policy whose predictable adoption would make the world best.

---

### References

Yudkowsky, E., and Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2.

Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.

Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.