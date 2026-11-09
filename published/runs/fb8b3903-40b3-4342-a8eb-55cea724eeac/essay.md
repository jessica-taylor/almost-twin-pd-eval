# Policy Functional Decision Theory: Choosing a Policy as the Output of a Fixed Function

Policy functional decision theory, which I will call **P-FDT**, is the policy-selection version of the theory introduced by Yudkowsky and Soares in “Functional Decision Theory: A New Theory of Instrumental Rationality.” The source text develops most examples using an action-centered formulation of functional decision theory, but footnote 16 gives the version that I take as primary here:

> “As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition.”

I will use **P-FDT** for this policy-based theory, and I will refer to the source’s action-centered version as functional decision theory only when needed for contrast. The other standard theories discussed below are **evidential decision theory** (**EDT**) and **causal decision theory** (**CDT**).

The guiding idea of P-FDT is simple: a rational agent should treat her decision as the output of a fixed mathematical decision procedure, and she should choose not merely an action but a complete policy—a mapping from inputs, observations, or situations to actions. The normative question is therefore:

> Which policy, if implemented by this very decision procedure, would yield the best outcome?

P-FDT then applies the selected policy to the agent’s actual input to produce the action.

---

## 1. From action selection to policy selection

The source’s action-centered version of functional decision theory can be summarized schematically as follows. Given a probabilistic world-model \(P\), a dependency structure \(G\), and an observation \(x\), the agent chooses an action \(a\) by intervening on a variable representing the output of the decision function on that input:

\[
\mathrm{FDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb{E}\!\left[
V \mid \mathrm{do}\bigl(\mathrm{fdt}(\underline{P},\underline{G},\underline{x})=a\bigr)
\right].
\]

Here \(V\) is utility, \(\mathcal A\) is the action set, and \(\mathrm{do}(\cdot)\) is an intervention operator. The crucial feature is that the intervention is not on the physical action variable directly, as in CDT. It is on a logical variable: the output of the agent’s decision procedure when given the relevant inputs.

P-FDT generalizes this by letting the decision procedure output a **policy** rather than a single action. Let

\[
\mathcal X
\]

be the set of possible inputs, observations, or decision situations, and let

\[
\mathcal A
\]

be the set of actions. A policy is a function

\[
\pi : \mathcal X \to \mathcal A.
\]

In sequential settings, \(\mathcal X\) can be understood as the set of histories available to the agent, so that \(\pi\) is a complete strategy.

Let \(D\) be a distinguished variable in the agent’s model representing the output of the P-FDT policy-selection procedure. The domain of \(D\) is the set \(\Pi\) of available policies. The central rule of P-FDT is then:

\[
\pi^*
\in
\arg\max_{\pi \in \Pi}
\mathbb{E}\!\left[
V \mid \mathrm{do}(D=\pi)
\right].
\]

If the agent’s actual input is \(x\), the action taken is

\[
a^* = \pi^*(x).
\]

Equivalently, if the model contains separate variables \(D_x\) representing the decision procedure’s output on each possible input \(x\), then the intervention

\[
\mathrm{do}(D=\pi)
\]

can be understood as shorthand for the family of interventions

\[
\mathrm{do}\bigl(D_x = \pi(x)\bigr)
\quad\text{for all }x \in \mathcal X.
\]

This is my reconstruction of the footnote’s suggestion. The source gives the core idea—intervene on the node that chooses a policy—but does not provide a fully developed policy-level equation. The equations above should therefore be read as a natural formalization of the policy-selection passage, not as a direct quotation from the source.

The difference between P-FDT and action-centered functional decision theory is that P-FDT evaluates complete contingent plans. It does not ask only, “What should I do now?” It asks, “What should this decision procedure dispose me to do across the relevant inputs?” The agent then uses the actual input to index into that policy.

---

## 2. P-FDT compared with EDT and CDT

P-FDT is an expected-utility theory. It recommends maximizing expected utility, but it uses a distinctive kind of hypothetical.

EDT evaluates actions by conditionalization. Very roughly:

\[
\mathrm{EDT}(P,x)
=
\arg\max_{a \in \mathcal A}
\mathbb{E}[V \mid X=x, A=a].
\]

EDT asks: “Which action would be the best news to learn I had taken?”

CDT evaluates actions by causal intervention. In Pearl-style notation:

\[
\mathrm{CDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb{E}[V \mid \mathrm{do}(A=a), X=x].
\]

CDT asks: “Which physical action would cause the best outcome?”

P-FDT instead evaluates policies by intervening on the policy-selection variable:

\[
\pi^*
\in
\arg\max_{\pi \in \Pi}
\mathbb{E}[V \mid \mathrm{do}(D=\pi)].
\]

P-FDT asks: “Which output of this policy-selection procedure would yield the best world?”

The distinction matters because different theories preserve or break different correlations when they imagine alternatives. EDT preserves too many correlations: when it imagines an action, it also imagines all the evidence normally associated with that action, even when the action does not affect the relevant facts. CDT preserves too few correlations: when it imagines changing the physical action, it holds fixed the predictions of reliable predictors, the behavior of psychological twins, and other processes that depend on the agent’s decision procedure.

P-FDT tries to preserve exactly the decision-relevant **subjunctive dependencies**. If another system predicts the agent by modeling the agent’s decision procedure, then the predictor’s behavior subjunctively depends on the output of that procedure. If a lesion merely causes both a preference and a disease, but does not model the agent’s decision procedure, then the disease does not subjunctively depend on the agent’s decision output.

The source expresses this with the analogy of calculators. Two well-functioning calculators computing the same sum will output the same result even if they are causally isolated. Their outputs are not merely statistically correlated; they are constrained by the same mathematical function. Similarly, if a predictor accurately models an agent’s decision procedure, then the predictor’s prediction and the agent’s action are linked by the same computational structure. P-FDT respects that link in its hypotheticals.

---

## 3. Hypotheticals, interventions, and counterpossibles

A P-FDT agent needs a model of the world. For present purposes, we can represent this as a pair

\[
M = (P,G),
\]

where \(P\) is a probability distribution over relevant variables and \(G\) is a dependency structure describing how changes to logical or policy variables affect other variables.

The model should include variables such as:

- \(D\): the policy selected by P-FDT;
- \(X\): the agent’s input, observation, or situation;
- \(A\): the action, often determined by \(A = D(X)\);
- \(Y\): predictor variables, other agents’ actions, or environmental responses;
- \(O\): the outcome;
- \(V = U(O)\): utility.

Given a policy \(\pi\), the intervention \(\mathrm{do}(D=\pi)\) sets the policy variable to \(\pi\). The intervention then propagates through the model along the relevant dependency edges. If a predictor’s prediction depends on \(D\), the prediction changes. If another agent’s action depends on a prediction of \(D\), that action changes. If the agent’s observation depends on the predictor’s behavior, the observation distribution may also change.

For example, in a Newcomb-like problem, the predictor’s prediction is modeled as depending on the agent’s decision procedure. Thus, under P-FDT:

\[
\mathrm{do}(D=\text{one-boxing policy})
\]

makes the predictor predict one-boxing with high probability, which makes the opaque box full with high probability. By contrast,

\[
\mathrm{do}(D=\text{two-boxing policy})
\]

makes the predictor predict two-boxing, which makes the opaque box empty with high probability.

By contrast, in the smoking lesion problem, the lesion causes both a preference for smoking and a risk of cancer. But the lesion does not model the agent’s decision procedure. Therefore P-FDT’s graph should not contain an edge from the policy node to the lesion or to cancer. The intervention

\[
\mathrm{do}(D=\text{smoking policy})
\]

changes the action but does not change the probability of cancer, except insofar as smoking itself causally affects cancer, which by stipulation it does not.

The source emphasizes that this requires a kind of counterpossible reasoning. If the agent’s decision procedure is deterministic, then it cannot literally have a different output on the same input. Nevertheless, P-FDT must ask what the world would look like if this very procedure had a different output. The source acknowledges that we do not yet have a fully satisfactory formal account of such counterpossibles. In the graphical formulation, this difficulty is displaced into the need for a correct dependency structure \(G\). Given \(G\), P-FDT can reuse something like Pearl’s \(\mathrm{do}\)-operator. But the source admits that we lack a general method for learning or justifying \(G\) for subjunctive dependencies, analogous to Pearl’s treatment of causal dependencies.

This is one of the main open problems inherited by P-FDT.

---

## 4. P-FDT in Newcomb’s problem

Newcomb’s problem is the classic test case. An agent faces a transparent box \(A\) containing \$1,000 and an opaque box \(B\) containing either \$1,000,000 or \$0. A reliable predictor has filled box \(B\) iff she predicted the agent would leave box \(A\) behind.

In a simple P-FDT model, the policy set has two relevant elements:

\[
\pi_1 = \text{one-box}, \qquad \pi_2 = \text{two-box}.
\]

Let \(\text{Accurate}\) be the event that the predictor is accurate, with

\[
P(\text{Accurate}) = 0.99.
\]

The predictor’s prediction depends on the policy node \(D\). If \(D=\pi_1\), then with probability \(0.99\) the predictor predicts one-boxing and fills box \(B\). If \(D=\pi_2\), then with probability \(0.99\) the predictor predicts two-boxing and leaves box \(B\) empty.

The expected utilities are approximately:

\[
\mathbb{E}[V \mid \mathrm{do}(D=\pi_1)]
=
0.99 \cdot 1{,}000{,}000
+
0.01 \cdot 0
=
990{,}000.
\]

For two-boxing:

\[
\mathbb{E}[V \mid \mathrm{do}(D=\pi_2)]
=
0.99 \cdot 1{,}000
+
0.01 \cdot 1{,}001{,}000
=
11{,}000.
\]

P-FDT therefore selects the one-boxing policy.

CDT two-boxes because it intervenes on the physical action while holding the predictor’s prediction fixed. EDT one-boxes because one-boxing is good evidence that the predictor filled the box. P-FDT one-boxes for a reason closer in structure to CDT’s counterfactual reasoning: it intervenes, but it intervenes on the policy variable that the predictor tracks.

---

## 5. P-FDT in the smoking lesion problem

The smoking lesion problem is meant to show the failure of EDT. Smoking is correlated with a fatal cancer, but the correlation is due to a common cause: a lesion that both makes smoking enjoyable and causes cancer. Smoking itself does not cause cancer. The agent gains \$1,000 in utility from smoking.

EDT refrains from smoking, because being a smoker is bad news: it indicates a higher probability of having the lesion. CDT smokes, because smoking does not causally affect cancer. P-FDT also smokes.

In a P-FDT model, the policy node influences the action but not the lesion. The lesion is a common cause of preferences and cancer, but it is not a predictor of the policy node. Therefore:

\[
\mathrm{do}(D=\text{smoking policy})
\]

does not change the probability of the lesion or cancer. It only changes whether the agent smokes. Since smoking adds \$1,000 utility and does not change the cancer risk, P-FDT selects smoking.

The source gives a more careful formulation involving uncertainty about the agent’s own utility function, because the lesion may determine whether the agent enjoys smoking. But the essential point remains: P-FDT distinguishes predictor-like dependencies from lesion-like dependencies. It does not treat all statistical correlations as if they were controllable by the agent’s policy.

---

## 6. Transparent Newcomb and Parfit’s hitchhiker

The policy formulation becomes especially natural in problems where the agent’s action depends on an observation that is itself influenced by predictions of the agent’s policy.

In the transparent Newcomb problem, both boxes are transparent. The predictor filled box \(B\) iff she predicted that the agent would leave box \(A\) behind upon seeing that both boxes are full. The agent may therefore see two full boxes and must decide whether to one-box or two-box.

Here the input space contains at least two observations:

\[
\mathcal X = \{\text{full}, \text{empty}\}.
\]

A policy must specify what to do after each observation. One natural policy is:

\[
\pi^*(\text{full}) = \text{one-box}, \qquad
\pi^*(\text{empty}) = \text{two-box}.
\]

Another policy is:

\[
\pi'(\text{full}) = \text{two-box}, \qquad
\pi'(\text{empty}) = \text{two-box}.
\]

The predictor’s behavior depends on what the policy would do upon seeing a full box. If the predictor predicts that \(\pi(\text{full}) = \text{one-box}\), she fills the box. If she predicts that \(\pi(\text{full}) = \text{two-box}\), she leaves it empty.

Under the policy that one-boxes upon seeing a full box, the agent usually sees a full box and receives \$1,000,000. With small probability the predictor is wrong, the agent sees an empty box, and the policy can sensibly two-box, receiving \$1,000.

Under the policy that two-boxes upon seeing a full box, the predictor usually leaves the box empty. The agent usually sees an empty box and receives only \$1,000; only with small probability does she see a full box and receive \$1,001,000.

Thus P-FDT selects the policy that one-boxes when it sees a full box. When the agent actually sees a full box, she one-boxes.

This is the source’s striking conclusion: P-FDT one-boxes even when the agent knows that box \(B\) is full. The source connects this to Parfit’s hitchhiker problem, where a driver will rescue an agent from the desert only if she predicts that the agent will later pay \$1,000 after being rescued. Once rescued, CDT and EDT both refuse to pay, because payment no longer seems beneficial. P-FDT pays, because the selected policy is “pay if rescued.” The driver predicts this, and the agent is rescued.

In policy notation, the hitchhiker policy is:

\[
\pi(\text{city}) = \text{pay}, \qquad
\pi(\text{desert}) = \text{accept offer}.
\]

P-FDT chooses the policy that makes the driver’s favorable prediction true.

---

## 7. Observation, updating, and updateless policy choice

One of the hardest interpretive questions for P-FDT is how to treat observations that have already been made. In ordinary Bayesian reasoning, if an agent sees that box \(B\) is full, she conditions on that observation. But if P-FDT conditions on seeing a full box, then two-boxing looks better in transparent Newcomb. Similarly, if an agent has already received a blackmail letter, conditioning on the letter may make payment look rational.

The source’s examples suggest that P-FDT does not respond to such observations by simple Bayesian conditioning. Instead, it responds by changing which decision output is being evaluated. In the action-centered formulation, after observing \(x\), the agent intervenes on the variable representing the output of the decision procedure on input \(x\). In the policy formulation, the agent chooses a policy and then applies \(x\).

This is closely related to what the source calls “updateless” reasoning in a footnote: a P-FDT agent may entertain the hypothesis that if her action were different, she might have made different observations.

For P-FDT, I propose the following operational distinction.

An observation is **policy-endogenous** if the policy node has a subjunctive-dependence path to that observation. For example, seeing a full box in transparent Newcomb is policy-endogenous, because the predictor’s decision to fill the box depends on the agent’s policy. Receiving a blackmail letter in a blackmail problem is also policy-endogenous if the blackmailer sends the letter only upon predicting payment.

An observation is **policy-exogenous** if it is not influenced by the agent’s policy in the relevant way. For example, seeing that a coin has landed heads, when the coin is independent of the agent’s decision procedure, is policy-exogenous.

A reasonable operational rule is then:

1. Use ordinary Bayesian updating on policy-exogenous observations.
2. Do not condition away policy-endogenous observations when evaluating policies.
3. Treat policy-endogenous observations as inputs to the selected policy.

This rule is not explicitly formulated in the source, but it seems required to recover the source’s judgments in transparent Newcomb, Parfit’s hitchhiker, and blackmail cases. It also gives P-FDT a coherent operational reading: choose the policy that would have been best from the perspective of the agent’s model, then execute that policy at the actual input.

This is admittedly one of the least settled parts of the theory. The source itself says that the formal foundations are less secure than Pearl’s causal framework. Still, the policy formulation helps: the agent is not choosing an action after fixing the observation as an immutable fact. She is choosing a complete mapping from observations to actions, where some observations are themselves consequences of the policy she selects.

---

## 8. P-FDT and blackmail

Blackmail cases illustrate why policy selection matters.

Consider the mechanical blackmail problem from the source. A blackmailer has damaging information that would cost the agent \$1,000,000 if published. The blackmailer runs a program that publishes the information iff she predicts that the agent will pay \$1,000 upon receiving a blackmail letter. If the program is running, paying stops it.

If the agent’s policy is

\[
\pi(\text{letter}) = \text{pay},
\]

then the blackmailer predicts payment and sends the letter. The agent loses \$1,000.

If the agent’s policy is

\[
\pi(\text{letter}) = \text{refuse},
\]

then the blackmailer predicts nonpayment and does not send the letter. The agent loses nothing, except in rare cases where the predictor makes an error.

With a perfect predictor, P-FDT selects refusal. With an imperfect predictor, P-FDT compares the expected cost of rare false-positive blackmail against the cost of payment. If the predictor wrongly predicts payment with probability \(p\), then a refusing policy risks losing \$1,000,000 with probability \(p\), giving expected loss

\[
p \cdot 1{,}000{,}000.
\]

A paying policy risks losing \$1,000 with high probability. Thus refusal is favored when

\[
p \cdot 1{,}000{,}000 < 1{,}000,
\]

that is, when

\[
p < 0.001.
\]

The important point is not the exact threshold. The point is that P-FDT evaluates the entire policy, including how the policy affects the probability of being blackmailed in the first place.

If the agent has already received the letter, P-FDT may still refuse to pay, provided the selected policy refuses upon receiving the letter. This seems odd from an action-centered perspective, because the agent knows she has been blackmailed. But P-FDT reasons that being the kind of agent, or implementing the kind of policy, that pays blackmailers makes blackmail profitable. Being the kind of agent that refuses makes blackmail unprofitable. The policy-level viewpoint makes this especially clear: the blackmailer’s action depends on the agent’s policy, not merely on a local physical action.

---

## 9. Why policy selection matters in multi-agent problems

Footnote 16 says that the difference between action selection and policy selection “only matters in multi-agent dilemmas so far as we can tell.” The source does not fully develop such dilemmas, but the reason is not hard to see.

In single-agent predictor problems, it is often enough to choose the right action for the actual input, provided one correctly imagines the counterfactual dependence of the predictor on that action. But in multi-agent settings, other agents may base their behavior on predictions of the agent’s entire strategy. They may care not only about what the agent does now, but about what the agent would do in counterfactual situations.

For example, in cooperative game-theoretic settings, another agent may cooperate only if she predicts that the agent would cooperate in return under relevant conditions. In extortion settings, an extortionist may target an agent only if she predicts that the agent’s policy includes payment under threat. In voting coalitions, an agent’s willingness to vote may depend on expectations about what symmetric agents would do under the same circumstances. In all of these cases, a complete policy is the natural object of prediction.

P-FDT treats such problems by selecting a strategy rather than a sequence of isolated actions. If several agents use the same reasoning procedure, or have accurate models of one another’s reasoning, their policies may be subjunctively linked. P-FDT says that when evaluating one’s own policy, one should hold fixed the relevant dependency structure: if my policy changes, the predictions and policies of those who model me may change as well.

The source uses the psychological twin prisoner’s dilemma to illustrate functional decision theory’s basic idea. An agent and her twin reason identically. If the agent’s decision procedure concludes “cooperate,” then the twin’s procedure concludes “cooperate.” If it concludes “defect,” both defect. P-FDT gives the same answer, but frames it as policy selection: the agent chooses the policy that her shared reasoning procedure will implement. Since mutual cooperation yields a much better outcome, P-FDT selects cooperation.

In more complex multi-agent problems, the policy formulation may matter because the agent must specify what she would do at information sets that are not reached in the actual equilibrium. Other agents may respond to those off-path dispositions. P-FDT’s policy node makes those dispositions explicit.

---

## 10. Open questions and operational assumptions

P-FDT is attractive, but several important questions remain unresolved in the source. I will separate the source’s claims from my own reconstructive proposals.

First, the source claims that the preferred formulation chooses a policy rather than an action. It does not give a full formal equation for this policy version. The equation

\[
\pi^*
\in
\arg\max_{\pi \in \Pi}
\mathbb{E}[V \mid \mathrm{do}(D=\pi)]
\]

is my reconstruction. It seems faithful to the footnote, but it is not explicitly supplied by the source.

Second, the source does not specify the policy class \(\Pi\). In simple finite problems, it is natural to take \(\Pi\) to be all functions from \(\mathcal X\) to \(\mathcal A\). In sequential problems, \(\mathcal X\) should be the set of histories. In bounded settings, the policy class may need to be restricted to computable or tractable policies. Randomized policies could also be allowed by letting \(D\) range over stochastic policies, although the source’s emphasis on a single logical output suggests deterministic policies as the basic case.

Third, the source does not provide a general method for constructing the dependency structure \(G\). This is the deepest problem. To apply P-FDT, one must know which variables subjunctively depend on the agent’s policy. In practice, I propose the following modeling heuristics:

- If a predictor explicitly models the agent’s decision procedure, connect the predictor’s prediction to the policy node.
- If another agent uses the same decision algorithm, connect their policy node to the same abstract policy output, or represent their prediction as depending on your policy node.
- If a correlation is produced by a common cause that does not model the agent’s policy, do not connect it to the policy node.
- If an observation is produced by a predictor’s action, and that predictor’s action depends on the agent’s policy, treat the observation as policy-endogenous.

These heuristics are not in the source as formal rules, but they follow the spirit of the predictor/lesion distinction.

Fourth, the source does not fully explain how P-FDT should combine policy selection with ordinary Bayesian learning. My proposed distinction between policy-endogenous and policy-exogenous observations is one way to make the theory operational. Without such a distinction, P-FDT risks giving inconsistent advice when applied after observations have been received.

Fifth, the source relies on counterpossible reasoning. If the policy node represents the output of a deterministic function, then alternative outputs are logically impossible. The source acknowledges this and treats it as a technical difficulty rather than a fatal objection. Human reasoners can reason under uncertainty about mathematical facts, and P-FDT only needs limited counterpossible reasoning: how would predictors behave if this decision procedure had a different output? Still, a fully satisfactory formal semantics for such reasoning remains absent.

Finally, the source claims that functional decision theory outperforms CDT and EDT in “fair” problems, where agents are rewarded or punished based on predictions of their behavior rather than for using a particular decision theory by name. The notion of fairness is not formally defined. P-FDT inherits this open problem. It may be possible to formalize fairness by requiring that the environment respond only to the agent’s outputs, not to the syntactic identity of her algorithm, but the source leaves this unfinished.

---

## 11. Philosophical motivation

The philosophical appeal of P-FDT is that it unifies several desirable features.

First, it avoids EDT’s tendency to manage the news. EDT refrains from smoking because smoking is bad news. But bad news is not the same as bad consequences. P-FDT recognizes that a lesion can make smoking good evidence for cancer without making smoking causally or subjunctively relevant to cancer.

Second, it avoids CDT’s inability to take advantage of predictor-based opportunities. CDT two-boxes in Newcomb’s problem because it treats the predictor’s prediction as fixed when the physical action changes. But if the predictor is accurate because it models the agent’s decision procedure, then holding the prediction fixed while changing the action is an artificial hypothetical. P-FDT treats the predictor’s prediction as varying with the policy node.

Third, it gives a natural account of precommitment. In many problems, we intuit that it would be rational to precommit to paying the driver, one-boxing, or refusing blackmail. P-FDT agents do not need costly external precommitments. They simply implement the policy that they would have wanted to precommit to.

Fourth, it treats decisions globally. Instead of asking only what physical movement is locally optimal, P-FDT asks what the world would look like if the agent’s decision procedure had a different output. This is what the source calls the “global perspective.” The agent chooses the best policy from the standpoint of the entire dependency structure, not merely from the standpoint of the local causal consequences of a bodily movement.

---

## Conclusion

Policy functional decision theory, or P-FDT, is the policy-selection version of functional decision theory. Its core instruction is to treat one’s decision as the output of a fixed mathematical policy-selection function and to choose the policy that would yield the best outcome when that very function is intervened upon. Formally, one may write:

\[
\pi^*
\in
\arg\max_{\pi \in \Pi}
\mathbb{E}[V \mid \mathrm{do}(D=\pi)],
\]

and then act as

\[
a = \pi^*(x)
\]

for the actual input \(x\).

P-FDT differs from EDT by using counterfactual interventions rather than evidential conditioning. It differs from CDT by intervening on the policy output rather than on the physical action. It preserves predictor-like and logical dependencies while ignoring merely statistical correlations. This allows P-FDT to one-box in Newcomb’s problem, smoke in the smoking lesion problem, pay in Parfit’s hitchhiker problem, one-box in transparent Newcomb, and refuse profitable blackmail.

The theory remains incomplete. It needs a better account of subjunctive dependency structure, a clearer rule for updating on endogenous observations, and a more precise formalization of policy spaces and fairness. But the central idea is compelling: rational action may not be a matter of choosing the best local movement, but of choosing the best complete policy for this very decision procedure to implement.

---

### Reference

Yudkowsky, E., and Soares, N. “Functional Decision Theory: A New Theory of Instrumental Rationality.” arXiv:1710.05060v2. The policy-selection passage used here appears in footnote 16.