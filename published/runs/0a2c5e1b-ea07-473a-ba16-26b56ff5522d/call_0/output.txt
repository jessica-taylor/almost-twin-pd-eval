# Policy Functional Decision Theory (P-FDT)

## Introduction

The reference article introduces *functional decision theory* (FDT) as an alternative to evidential decision theory (EDT) and causal decision theory (CDT). Its core idea is that a rational agent should treat her decision as the output of a fixed mathematical function and ask, “Which output of this very function would yield the best outcome?” The present essay focuses on the policy-selection version of that idea. The authors write in footnote 16:

> “the author’s preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action.”

They add:

> “The difference only matters in multi-agent dilemmas so far as we can tell.”

For this essay, I call the policy-selection theory **P-FDT** (policy functional decision theory). P-FDT is an expected-utility theory, but instead of evaluating isolated physical acts, it evaluates *policies*: functions from observations or histories to actions. The agent chooses the policy whose selection by her own policy-selection procedure would produce the best world, and then she applies that policy to her actual inputs.

This policy formulation matters because many decision problems involve predictors, copies, negotiations, commitments, and other agents whose behavior depends not merely on what the agent does now, but on what the agent’s decision procedure would do across possible circumstances. P-FDT handles such problems by intervening on the logical variable representing the output of the agent’s policy-selection computation.

---

## 1. The central normative idea

P-FDT’s normative principle can be stated as follows:

> Choose the policy such that, if this very policy-selection procedure selected that policy, the expected outcome would be best.

This differs from EDT, CDT, and even the simpler action-based formulation of FDT.

EDT asks:

> “Which action would be the best news to learn I had taken?”

CDT asks:

> “Which physical action would causally produce the best consequences?”

Action-based FDT asks:

> “Which output of my decision function, given my current inputs, would produce the best outcome?”

P-FDT asks the broader question:

> “Which policy should my policy-selection function output?”

A *policy* is a plan for mapping observations to actions. If \(\mathcal X\) is a set of possible observations and \(\mathcal A\) is a set of possible actions, then a deterministic policy is a function

\[
\pi : \mathcal X \to \mathcal A.
\]

In sequential settings, the input to a policy may be a full history rather than a single observation, but the basic idea remains the same.

P-FDT does not first ask, “What should I do given this observation?” Instead, it asks, “What should my standing rule be for turning observations into actions?” Once the best policy has been selected, the agent applies it to her actual observation:

\[
a^* = \pi^*(x).
\]

This is the policy-selection passage’s point: P-FDT intervenes on the node that selects a policy, not directly on the node that selects an action.

---

## 2. A formal reconstruction of P-FDT

The source paper formalizes action-based FDT using a probability distribution \(P\), a dependency graph \(G\), and an intervention operator \(\do(\cdot)\) borrowed from causal modeling. P-FDT can be reconstructed in the same spirit.

Let:

- \(\mathcal X\) be a set of possible observations or inputs.
- \(\mathcal A\) be a finite set of actions.
- \(\Pi = \mathcal A^{\mathcal X}\) be the set of deterministic policies.
- \(V\) be a utility-valued random variable.
- \(\Phi_{P,G}\) be a variable representing the output of the P-FDT policy-selection procedure when given model \((P,G)\).

The variable \(\Phi_{P,G}\) is not an ordinary physical variable. It is a *logical* or *computational* variable: it represents what policy the agent’s decision procedure selects. The model \(P\) contains variables for the outputs of mathematical functions, including the agent’s own policy-selection function. This self-reference is not fatal; the source notes that data structures can represent themselves, via ideas such as Kleene’s recursion theorem.

P-FDT evaluates a candidate policy \(\pi \in \Pi\) by intervening on \(\Phi_{P,G}\):

\[
\EU_{\text{P-FDT}}(\pi; P,G)
=
\mathbb{E}_P\!\left[ V \mid \do(\Phi_{P,G} = \pi) \right].
\]

Then P-FDT chooses

\[
\pi^*
\in
\argmax_{\pi \in \Pi}
\mathbb{E}_P\!\left[ V \mid \do(\Phi_{P,G} = \pi) \right].
\]

If the agent’s actual observation is \(x\), the prescribed action is

\[
a^* = \pi^*(x).
\]

This is the essential equation of P-FDT. The theory does not maximize expected utility conditional on the actual action, nor does it merely intervene on the physical action variable. It intervenes on the policy-selection variable.

In a sequential setting, one can replace the simple observation set \(\mathcal X\) with a set of histories \(\mathcal H\). A policy is then

\[
\pi : \mathcal H \to \mathcal A,
\]

and under intervention \(\do(\Phi_{P,G}=\pi)\), the agent’s action at each history \(h\) is given by

\[
A_h = \pi(h).
\]

The expected utility of \(\pi\) is the expectation of \(V\) in the world produced by that policy, including the responses of predictors and other agents whose behavior depends on the policy.

### Comparison with EDT, CDT, and action-based FDT

The contrast with other theories is illuminating.

EDT evaluates an action \(a\) after observation \(x\) by conditioning:

\[
\EDT(P,x)
=
\argmax_{a \in \mathcal A}
\mathbb{E}\!\left[ V \mid \Obs=x, \Act=a \right].
\]

CDT evaluates an action by a causal intervention on the physical action variable:

\[
\CDT(P,G,x)
=
\argmax_{a \in \mathcal A}
\mathbb{E}\!\left[ V \mid \do(\Act=a), \Obs=x \right].
\]

The action-based FDT equation in the source is:

\[
\FDT(P,G,x)
=
\argmax_{a \in \mathcal A}
\mathbb{E}\!\left[ V \mid \do(\FDTvar(\underline P,\underline G,\underline x)=a) \right].
\]

P-FDT replaces the action variable with a policy variable:

\[
\text{P-FDT}(P,G)
=
\argmax_{\pi \in \Pi}
\mathbb{E}\!\left[ V \mid \do(\Phi_{P,G}=\pi) \right].
\]

Then the actual action is obtained by applying the selected policy to the actual observation.

The difference is subtle but important. Action-based FDT asks what the decision function should output for the current input. P-FDT asks what entire input-to-action mapping the policy-selection function should output. In many one-shot problems, the two approaches give the same answer. They can diverge when other agents or predictors depend on the agent’s policy as a whole, rather than on the current action alone.

---

## 3. Subjunctive dependence and counterfactuals

The source’s philosophical core is the notion of *subjunctive dependence*. CDT is sensitive to causal dependence. EDT is sensitive to evidential dependence. P-FDT is sensitive to subjunctive dependence: the dependence that holds when physical systems are computing, predicting, or simulating the same mathematical function.

The source gives the example of two calculators computing the same arithmetic problem. If one calculator outputs \(7336\), we expect the other to output \(7336\) as well, even if they are causally independent. Their outputs are not merely statistically correlated; they are tied by the mathematical fact that they are computing the same function.

Similarly, if a predictor contains an accurate model of the agent’s decision procedure, then the predictor’s prediction is subjunctively dependent on the agent’s decision procedure. If the agent’s policy-selection function were to output a different policy, the predictor’s prediction would differ as well.

P-FDT’s counterfactuals respect this dependence. When P-FDT evaluates

\[
\do(\Phi_{P,G} = \pi),
\]

it does not hold fixed the predictions of predictors that depend on \(\Phi_{P,G}\). It changes those predictions accordingly. It also changes the behavior of twins, simulations, or other agents implementing the same policy-selection procedure. By contrast, it does not change variables that are merely statistically correlated with the agent’s action, such as a lesion that causes both a preference for smoking and lung cancer, unless that lesion somehow depends on the agent’s policy-selection computation.

This is why P-FDT can one-box in Newcomb’s problem while still smoking in the smoking lesion problem. The predictor depends on the agent’s decision procedure; the lesion does not.

There is a difficulty, emphasized by the source: these counterfactuals are often *counterpossible*. If the actual P-FDT procedure outputs \(\pi_1\), then in ordinary logic it cannot output \(\pi_2\) on the same input. Nevertheless, P-FDT must reason as if the same computation had a different output. The source admits that we lack a fully satisfactory formal account of such counterpossible reasoning. In the graphical reconstruction, we simply assume that the model supplies a graph \(G\) telling us how changing the policy variable would affect other variables. This is a significant open problem inherited by P-FDT.

---

## 4. How P-FDT evaluates policies

A useful operational procedure for applying P-FDT is the following.

1. **Identify the policy space.**  
   Determine the observations or histories the agent may face and the actions available at each. Let \(\Pi\) be the set of candidate policies.

2. **Build a probabilistic model \(P\).**  
   This model should include variables for observations, actions, outcomes, utility, predictors, other agents, and relevant background facts.

3. **Specify the subjunctive-dependency graph \(G\).**  
   The graph should encode which variables depend on the agent’s policy-selection computation. Predictors, accurate models, copies, and simulations of the agent should typically be downstream of the policy variable. Merely correlated background variables, such as lesions or coincidences, should not be downstream unless they genuinely depend on the policy.

4. **For each policy \(\pi\), perform the intervention \(\do(\Phi_{P,G}=\pi)\).**  
   Under this intervention, the agent acts according to \(\pi\). Predictors that depend on the policy predict \(\pi\). Other agents that model the policy respond to \(\pi\). Observations that are produced by predictors may also change.

5. **Compute expected utility.**  
   Evaluate

   \[
   \mathbb{E}[V \mid \do(\Phi_{P,G}=\pi)].
   \]

6. **Choose the maximizing policy and apply it.**  
   Select

   \[
   \pi^* \in \argmax_{\pi \in \Pi} \mathbb{E}[V \mid \do(\Phi_{P,G}=\pi)],
   \]

   then take action

   \[
   a^* = \pi^*(x),
   \]

   where \(x\) is the actual observation.

This procedure makes P-FDT sound highly demanding, and in full generality it is. The source’s formalism is idealized. Real agents will need approximations, restricted policy classes, and heuristic models of subjunctive dependence.

---

## 5. Examples

### P-FDT in Newcomb’s problem

In Newcomb’s problem, an agent can take both boxes or only box B. A reliable predictor has placed \$1,000,000 in box B iff she predicted the agent would take only B. The predictor is correct 99% of the time. Box A contains \$1,000.

In a simple P-FDT model, the policy space can be reduced to two constant policies:

\[
\pi_1 = \text{one-box}, \qquad \pi_2 = \text{two-box}.
\]

Let \(\Phi\) be the policy-selection variable. The predictor’s prediction depends on \(\Phi\). If the predictor is accurate, then under \(\do(\Phi=\pi_1)\), the predictor predicted one-boxing and box B is probably full. Under \(\do(\Phi=\pi_2)\), the predictor predicted two-boxing and box B is probably empty.

The expected utilities are approximately:

\[
\EU(\pi_1)
=
0.99 \cdot 1{,}000{,}000
+
0.01 \cdot 0
=
990{,}000,
\]

\[
\EU(\pi_2)
=
0.01 \cdot 1{,}001{,}000
+
0.99 \cdot 1{,}000
=
11{,}000.
\]

P-FDT selects \(\pi_1\), the one-boxing policy.

This result matches the source’s claim that FDT one-boxes in Newcomb’s problem. The P-FDT formulation makes the reasoning explicit: the agent is not merely choosing a physical hand movement. She is choosing what policy her decision procedure should output, knowing that the predictor’s behavior depends on that policy.

### P-FDT in the smoking lesion problem

In the smoking lesion problem, smoking is correlated with cancer, but only because a lesion causes both a desire to smoke and cancer. Smoking itself does not cause cancer. Smoking gives \$1,000 worth of utility. Surviving cancer is worth \$1,000,000.

Here the lesion is not subjunctively dependent on the agent’s policy-selection procedure. Whether the agent has the lesion does not change if we counterfactually suppose that her P-FDT procedure outputs a smoking policy rather than a refraining policy.

Thus, under either policy, the probability of having the lesion remains the same. Smoking adds \$1,000 utility without changing the cancer risk. Therefore P-FDT selects the smoking policy.

This illustrates the crucial distinction between predictor-like dependencies and lesion-like dependencies. P-FDT respects correlations that arise because the environment is tracking the agent’s policy, but it ignores correlations that are merely evidential.

### P-FDT in transparent Newcomb’s problem

In transparent Newcomb’s problem, both boxes are transparent. The predictor placed \$1,000,000 in box B iff she predicted the agent would leave box A behind upon seeing that both boxes are full. The agent sees that both boxes are full. EDT and CDT both two-box. P-FDT one-boxes.

A policy formulation is natural here. Consider two policies:

\[
\pi_1:
\begin{cases}
\text{one-box if box B is full},\\
\text{two-box if box B is empty},
\end{cases}
\]

\[
\pi_2:
\begin{cases}
\text{two-box if box B is full},\\
\text{two-box if box B is empty}.
\end{cases}
\]

The predictor predicts what policy the agent will use, especially what the agent will do if she sees a full box B.

Under \(\do(\Phi=\pi_1)\), the predictor usually predicts one-boxing upon seeing a full box, so she fills box B. With probability \(0.99\), the agent sees a full box and one-boxes, receiving \$1,000,000. With probability \(0.01\), the predictor is wrong, the box is empty, and the agent two-boxes, receiving about \$1,000.

So

\[
\EU(\pi_1)
\approx
0.99 \cdot 1{,}000{,}000
+
0.01 \cdot 1{,}000
=
990{,}010.
\]

Under \(\do(\Phi=\pi_2)\), the predictor usually predicts two-boxing, so box B is empty. With probability \(0.99\), the agent sees an empty box and takes whatever is available, receiving about \$1,000. With probability \(0.01\), the predictor is wrong, the box is full, and the agent two-boxes, receiving \$1,001,000.

So

\[
\EU(\pi_2)
\approx
0.99 \cdot 1{,}000
+
0.01 \cdot 1{,}001{,}000
=
11{,}000.
\]

P-FDT selects \(\pi_1\). If the agent actually sees a full box B, she applies the policy and one-boxes.

The important point is that P-FDT does not treat the observation “box B is full” as fixed evidence to be conditioned on. When P-FDT imagines selecting \(\pi_2\), it imagines a world in which the predictor would have predicted differently, and therefore the agent would probably be seeing an empty box. The observation itself is allowed to vary counterfactually because it depends on the predictor’s prediction of the policy.

### P-FDT in blackmail problems

The source discusses blackmail cases in which a predictor sends a blackmail letter iff she predicts the agent will pay. The rational policy is to refuse to pay. If the agent’s policy is to pay, the predictor sends the letter. If the agent’s policy is to refuse, the predictor does not send the letter.

P-FDT evaluates the policy “pay if letter” by setting \(\Phi\) to that policy. The predictor predicts payment, sends the letter, and the agent loses money. P-FDT evaluates the policy “refuse if letter” by setting \(\Phi\) to that policy. The predictor predicts refusal and usually does not send the letter. The expected outcome is better.

Thus P-FDT selects the refusing policy. If the agent nonetheless receives the letter, she refuses to pay. This may seem strange, because the agent is holding the letter. But P-FDT’s counterfactual says: if this very policy-selection procedure were the kind of procedure that paid, the blackmailer would have predicted that and the situation would have been different. The policy of refusing makes blackmail unprofitable.

This example shows why P-FDT should not simply update on the actual observation and then choose an action. The observation “I received the letter” is itself evidence about the policy the predictor expected. P-FDT handles this by evaluating policies under intervention, not by conditioning on the observation as though it were fixed.

---

## 6. What P-FDT holds fixed and what it changes

P-FDT’s counterfactuals are defined by the graph \(G\). The theory preserves all decision-relevant subjunctive dependencies encoded in \(G\), while breaking merely statistical correlations that are not tied to the policy-selection computation.

Under \(\do(\Phi=\pi)\):

- The agent’s physical action becomes whatever \(\pi\) prescribes for the relevant observation.
- Predictors that model \(\Phi\) update their predictions to \(\pi\).
- Other agents implementing the same policy-selection computation select the corresponding policies.
- Observations that depend on predictors’ predictions may change.
- Variables merely correlated with the agent’s action, but not dependent on the policy, are held fixed.

This is the P-FDT analogue of CDT’s surgical intervention. CDT intervenes on a physical action variable. P-FDT intervenes on a logical policy variable.

One can also formulate a P-FDT notion of dominance. Policy \(\pi_1\) dominates \(\pi_2\) if, holding fixed the relevant subjunctive-dependency structure, replacing \(\pi_2\) with \(\pi_1\) never lowers expected utility and sometimes raises it. But dominance is internal to the theory’s counterfactuals. The source correctly warns that dominance arguments do not provide a neutral adjudication between EDT, CDT, and FDT-style theories.

---

## 7. Open questions and my interpretive assumptions

The footnote is brief, and many details are not settled by the source. The reconstruction above is my best mathematical interpretation, not a direct extraction of a complete formal theory.

### The dependency graph \(G\)

The largest open problem is the construction of \(G\). CDT can appeal, at least in principle, to Pearl-style causal discovery. P-FDT needs a way to discover or justify logical, mathematical, and computational dependencies. The source says this is perhaps the largest open problem for FDT. P-FDT inherits it.

In practice, I have assumed that the analyst supplies a model in which predictors, copies, and simulations are represented as depending on the agent’s policy variable. This is reasonable in stylized problems, but it is not yet a general epistemology of subjunctive dependence.

### The policy space

The source does not specify how the set of policies is chosen. If \(\mathcal X\) and \(\mathcal A\) are finite, then \(\Pi\) is finite but potentially enormous. In sequential or continuous settings, the policy space may be infinite. A realistic P-FDT agent must restrict attention to computable or representable policies.

I have assumed deterministic policies for simplicity. Stochastic policies could be handled by letting policies output probability distributions over actions, or by treating random seeds as part of the model. But if predictors can predict the randomization device, then randomization may not break subjunctive dependence. The source does not fully address stochastic policy selection.

### Updating on observations

The most delicate interpretive question is how P-FDT uses actual observations. The source’s action-based FDT responds to observation by changing the node on which it intervenes, rather than by ordinary Bayesian conditioning. In the policy formulation, I have proposed the following rule:

> Use the actual observation as an input to the selected policy, but do not condition the policy’s expected utility on that observation if the observation may itself depend on the policy.

This is not explicitly formalized in the footnote, but it seems necessary to preserve P-FDT’s behavior in transparent Newcomb and blackmail cases. If the agent conditions on seeing a full box or receiving a blackmail letter, she may choose the locally tempting action and lose the benefits of policy selection.

When an observation is known to be exogenous — for example, a weather report that no predictor has used to predict the agent’s policy — conditioning on it is harmless and often appropriate. But P-FDT’s distinctive cases are precisely those in which observations are not exogenous.

### Multi-agent dependence

The source says the action/policy distinction “only matters in multi-agent dilemmas so far as we can tell.” That is a source claim. My reconstruction suggests that policy selection is also useful for understanding sequential commitment, extortion resistance, and problems where the agent’s current observation depends on predictions of her policy. These may be describable without full policy iteration, but the policy formulation gives a cleaner unified account.

---

## Conclusion

P-FDT is the policy-oriented version of functional decision theory. Instead of asking which physical act to perform, it asks which policy the agent’s own policy-selection procedure should output. Formally, it evaluates a policy \(\pi\) by intervening on a logical variable \(\Phi_{P,G}\) representing the output of the P-FDT policy-selection computation:

\[
\pi^*
\in
\argmax_{\pi \in \Pi}
\mathbb{E}\!\left[ V \mid \do(\Phi_{P,G}=\pi) \right],
\]

and then executes

\[
a^* = \pi^*(x).
\]

P-FDT preserves dependencies between the agent’s policy and predictors, copies, simulations, and other agents who model the policy. It ignores merely evidential correlations, such as lesions. It allows observations themselves to vary in counterfactual policy evaluations when those observations are produced by policy-dependent predictors.

The theory gives attractive verdicts in familiar problems: it one-boxes in Newcomb’s problem, smokes in the smoking lesion problem, one-boxes in transparent Newcomb’s problem, and refuses blackmail. Its main weakness is not in its basic decision rule but in the unfinished task of constructing the subjunctive-dependency graph \(G\) and handling logical uncertainty in a fully rigorous way. Still, as an idealized normative theory, P-FDT offers a clear and powerful principle: choose the policy that this very policy-selection procedure should output, and then act accordingly.

---

## References

Yudkowsky, E., and Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060.

Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.