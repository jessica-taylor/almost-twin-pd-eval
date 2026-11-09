# Policy Functional Decision Theory (P-FDT): Choosing Policies by Subjunctive Intervention

Policy functional decision theory, which I will call **P-FDT**, is a decision theory that evaluates *policies* rather than isolated physical actions. The starting point for this essay is the policy-selection passage in footnote 16 of Yudkowsky and Soares’s paper on functional decision theory:

> “As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition.”

That footnote is brief, so much of the mathematical structure below is my reconstruction of what P-FDT must mean if it is to inherit the spirit of the source’s functional decision theory while making policy selection explicit. I will distinguish claims taken from the source from additional operational assumptions of my own.

The central idea is this: a rational agent should not merely ask, “Which physical act should I perform?” or “Which act would be best news?” or even “Which output should my decision procedure give on this exact input?” Instead, the agent should ask:

> Which policy should this very decision procedure output, given that the policy will then be applied to my actual inputs?

P-FDT therefore treats the agent’s decision as the selection of a mapping from observations, inputs, or decision contexts to actions. The agent chooses the best policy by imagining that the output of her decision procedure is that policy, evaluates the consequences under an appropriate notion of counterfactual intervention, and then executes whatever action the selected policy prescribes for her current input.

---

## 1. From action choice to policy choice

The source paper develops an action-level version of functional decision theory. In that version, the agent has a world-model \(P\), a graph \(G\) encoding dependency structure, and an observation history \(x\). The action-level theory chooses

\[
\mathrm{FDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb{E}\!\left[V \mid \mathrm{do}\bigl(\mathrm{fdt}(\underline{P},\underline{G},\underline{x})=a\bigr)\right],
\]

where \(\mathrm{fdt}(\underline{P},\underline{G},\underline{x})\) is a variable representing the output of the agent’s decision procedure on input \(x\), and \(\mathrm{do}(\cdot)\) is an intervention operator. The source contrasts this with evidential decision theory, which conditions on actions, and causal decision theory, which intervenes on physical action variables.

P-FDT modifies the object of intervention. Instead of intervening on a variable representing “the action taken on this input,” P-FDT intervenes on a variable representing “the policy selected by this decision procedure.” A policy is a function

\[
\pi : \mathcal X \to \mathcal A,
\]

where \(\mathcal X\) is a set of possible inputs or observation histories and \(\mathcal A\) is a set of actions. The agent does not first choose an action for the current input. She chooses a whole policy \(\pi\), and then the action actually taken is

\[
a = \pi(x),
\]

where \(x\) is her actual input.

This distinction matters when predictors, copies, twin agents, blackmailers, or other decision-dependent processes respond not merely to the agent’s present bodily movement, but to the agent’s broader decision behavior. A predictor may care what the agent would do if she saw a full box, received a blackmail letter, or arrived safely in the city. Those are policy-relevant facts.

---

## 2. A formal model for P-FDT

Let us build a simple formal framework.

Let:

- \(\mathcal X\) be the set of possible inputs, observations, or decision contexts.
- \(\mathcal A\) be the set of possible actions.
- \(\Pi\) be the set of candidate policies, where each \(\pi \in \Pi\) is a function \(\pi : \mathcal X \to \mathcal A\).
- \(V\) be a real-valued utility variable.
- \((P,G)\) be the agent’s world-model, where \(P\) is a probability distribution over relevant variables and \(G\) is a graph representing how variables depend on one another.

In P-FDT, the graph \(G\) must contain a variable representing the agent’s selected policy. I will call this variable \(\mathrm{Pol}\). Its possible values are policies \(\pi \in \Pi\). The actual action variable is downstream from \(\mathrm{Pol}\) and the input variable \(X\):

\[
A = \mathrm{Pol}(X).
\]

Other variables, such as predictors’ predictions, the contents of boxes, the behavior of other agents, or the presence of blackmail letters, may also depend on \(\mathrm{Pol}\), either directly or through predicted outputs of the policy.

P-FDT uses an intervention operator \(\mathrm{do}_G(\mathrm{Pol}=\pi)\). This operator replaces the normal determination of the policy variable with the fixed assignment \(\mathrm{Pol}=\pi\), then propagates the consequences through the graph \(G\). The expected utility of policy \(\pi\) is

\[
\mathrm{EU}_{\text{P-FDT}}(\pi;P,G)
=
\mathbb{E}_P\!\left[V \mid \mathrm{do}_G(\mathrm{Pol}=\pi)\right].
\]

The selected policy is

\[
\pi^*
\in
\arg\max_{\pi \in \Pi}
\mathrm{EU}_{\text{P-FDT}}(\pi;P,G).
\]

Given actual input \(x\), P-FDT performs the action

\[
\mathrm{P\text{-}FDT}(P,G,x)
=
\pi^*(x).
\]

This is the core mathematical proposal. The agent does not ask which action maximizes expected utility after fixing the current observation as an ordinary piece of evidence. She asks which policy would produce the best world if that policy were the output of her decision procedure, and then she applies that policy to her actual situation.

A practical recipe for applying P-FDT is:

1. Identify the relevant inputs \(\mathcal X\) and actions \(\mathcal A\).
2. Identify candidate policies \(\pi : \mathcal X \to \mathcal A\).
3. Construct a graph \(G\) encoding which variables subjunctively depend on the agent’s policy.
4. For each policy \(\pi\), evaluate \(\mathbb{E}[V \mid \mathrm{do}(\mathrm{Pol}=\pi)]\).
5. Choose a policy \(\pi^*\) with maximal expected utility.
6. Execute \(\pi^*(x)\), where \(x\) is the actual input.

There is a mild self-referential element: the model contains a variable representing the policy selected by P-FDT itself. The source notes that this kind of self-reference can be handled using standard recursion-theoretic techniques, and in practice one need not fully solve the self-reference in order to reason informally about the policy.

For comparison:

- **Evidential decision theory** chooses an action by conditioning:
  \[
  a^* = \arg\max_a \mathbb{E}[V \mid A=a].
  \]

- **Causal decision theory** chooses an action by physical intervention:
  \[
  a^* = \arg\max_a \mathbb{E}[V \mid \mathrm{do}(A=a)].
  \]

- **Action-level FDT**, as presented in the source, chooses an action by intervening on the output of the decision procedure for the current input:
  \[
  a^* = \arg\max_a \mathbb{E}[V \mid \mathrm{do}(\mathrm{fdt}(P,G,x)=a)].
  \]

- **P-FDT** chooses a policy:
  \[
  \pi^* = \arg\max_\pi \mathbb{E}[V \mid \mathrm{do}(\mathrm{Pol}=\pi)],
  \]
  then acts by applying \(\pi^*\) to the current input.

The move from action-level FDT to P-FDT is therefore a move from choosing an output-on-this-input to choosing a rule that maps many possible inputs to outputs.

---

## 3. Subjunctive dependence and counterfactuals

P-FDT inherits the source’s notion of **subjunctive dependence**. Two systems are subjunctively dependent on a computation when their behavior tracks what that computation outputs. The source’s favorite analogy is two calculators computing the same arithmetic problem. They are causally separated, but if one outputs \(7336\), the other will also output \(7336\), provided both are functioning correctly. Their outputs depend on the same mathematical fact.

In decision problems, predictors, psychological twins, simulations, copies, and some game-theoretic opponents can be subjunctively dependent on the agent’s decision procedure. If the agent’s policy is one that pays the driver after being rescued, a good predictor will predict that. If the agent’s policy is one that two-boxes on seeing a full box, a good predictor will predict that too.

P-FDT’s counterfactuals are therefore not merely causal counterfactuals. They are policy counterfactuals:

> What would the world look like if this very decision procedure selected policy \(\pi\) instead of policy \(\pi'\)?

This requires a kind of counterpossible reasoning. If the agent actually selects \(\pi^*\), then, given the same inputs, she cannot literally select \(\pi'\). Nevertheless, P-FDT asks what would follow if the decision procedure had a different output. The source acknowledges that this is technically difficult: we lack a fully satisfactory general account of counterpossible conditionals. In the graphical formulation, the difficulty is pushed into the graph \(G\): once \(G\) tells us how changing the policy variable affects other variables, we can use an intervention-like calculation.

The important normative point is that P-FDT preserves dependencies that causal decision theory wrongly severs, while breaking dependencies that evidential decision theory wrongly preserves.

- A predictor’s prediction may depend on the agent’s policy. P-FDT preserves this dependency.
- A carcinogenic lesion may statistically correlate with smoking, but it does not depend on the agent’s policy. P-FDT does not treat it as policy-dependent.
- A blackmailer’s decision to send a letter may depend on the agent’s policy. P-FDT can preserve this dependency.
- The weather, unless somehow prediction-dependent, is normally not policy-dependent.

Thus P-FDT is not simply “manage the news,” as EDT can be, nor simply “maximize downstream causal consequences,” as CDT does. It chooses the policy whose global implementation would produce the best world, given the agent’s model of logical, computational, predictive, and causal dependencies.

---

## 4. Examples

### 4.1 Newcomb’s problem

In Newcomb’s problem, the agent may take both boxes or only the opaque box. A predictor placed \$1,000,000 in the opaque box if and only if she predicted that the agent would one-box. The predictor is correct 99% of the time.

Here there is no important observation before the choice, so a policy reduces to an action. Let

\[
\Pi = \{\pi_{\text{one}}, \pi_{\text{two}}\}.
\]

Under \(\mathrm{do}(\mathrm{Pol}=\pi_{\text{one}})\), the predictor probably predicted one-boxing, so the opaque box is probably full:

\[
\mathrm{EU}_{\text{P-FDT}}(\pi_{\text{one}})
\approx
0.99 \cdot \$1{,}000{,}000
+
0.01 \cdot \$0
=
\$990{,}000.
\]

Under \(\mathrm{do}(\mathrm{Pol}=\pi_{\text{two}})\), the predictor probably predicted two-boxing, so the opaque box is probably empty:

\[
\mathrm{EU}_{\text{P-FDT}}(\pi_{\text{two}})
\approx
0.99 \cdot \$1{,}000
+
0.01 \cdot \$1{,}001{,}000
=
\$11{,}000.
\]

P-FDT selects \(\pi_{\text{one}}\). The agent one-boxes.

Causal decision theory two-boxes because it intervenes on the physical action while holding the predictor’s earlier prediction fixed. Evidential decision theory one-boxes because one-boxing is good evidence that the box is full. P-FDT one-boxes for a different reason: the predictor’s behavior subjunctively depends on the agent’s decision procedure, so the correct counterfactual changes the prediction when the policy changes.

### 4.2 The smoking lesion problem

In the smoking lesion problem, smoking is correlated with cancer only because a lesion causes both a preference for smoking and cancer. Smoking itself does not cause cancer. The agent gains \$1,000 worth of utility from smoking.

A simple P-FDT graph contains variables for the lesion, smoking, cancer, and utility. The lesion affects both the agent’s inclination to smoke and the probability of cancer. But the lesion does not depend on the agent’s policy. Thus:

\[
\mathrm{Pol} \not\to \mathrm{Lesion},
\]

and

\[
\mathrm{Pol} \not\to \mathrm{Cancer},
\]

except through the action of smoking, which by assumption has no causal effect on cancer.

Therefore,

\[
\mathrm{EU}_{\text{P-FDT}}(\pi_{\text{smoke}})
=
\mathrm{EU}_{\text{P-FDT}}(\pi_{\text{refrain}})
+
\$1{,}000.
\]

P-FDT recommends smoking.

This matches the source’s claim that functional decision theory should one-box in Newcomb’s problem and smoke in the smoking lesion problem. The key difference is that the predictor in Newcomb’s problem represents the agent’s decision procedure, while the lesion does not.

The source’s own treatment of the lesion problem is slightly more complicated because the lesion changes the agent’s preferences, so there are two possible utility functions and two possible decision-procedure outputs. For present purposes, the simpler graph captures the crucial point: P-FDT does not treat merely statistical common-cause correlations as policy-dependencies.

### 4.3 The twin prisoner’s dilemma

An agent plays a prisoner’s dilemma against a perfect psychological twin in a separate room. Both use the same decision procedure. The payoffs are:

- Both cooperate: \$1,000,000 each.
- Both defect: \$1,000 each.
- One cooperates, one defects: defector gets \$1,001,000, cooperator gets \$0.

If the agents’ decisions are computed by the same policy, then a P-FDT graph may represent both actions as downstream from the same policy variable:

\[
\mathrm{Pol} \to A_{\text{self}},
\qquad
\mathrm{Pol} \to A_{\text{twin}}.
\]

Then:

\[
\mathrm{EU}_{\text{P-FDT}}(\pi_{\text{cooperate}})
=
\$1{,}000{,}000,
\]

while

\[
\mathrm{EU}_{\text{P-FDT}}(\pi_{\text{defect}})
=
\$1{,}000.
\]

P-FDT selects cooperation.

This example illustrates the “global” character of P-FDT. The agent does not ask, “Given my twin’s fixed behavior, should I cooperate?” She asks, “What happens if this very reasoning procedure concludes cooperate, and what happens if it concludes defect?” Since the twin uses the same procedure, the two agents’ actions move together in the relevant counterfactuals.

### 4.4 Transparent Newcomb and Parfit’s hitchhiker

The policy structure becomes most important in cases where the agent receives an observation before acting.

In the transparent Newcomb problem, the agent sees the contents of both boxes. The predictor placed \$1,000,000 in box B if and only if she predicted that the agent would leave behind box A upon seeing that both boxes are full. Suppose the predictor is 99% accurate.

Let the relevant inputs be:

\[
\mathcal X = \{\text{full}, \text{empty}\}.
\]

A policy specifies what to do after seeing each possible state. Consider two policies:

\[
\pi_O(\text{full}) = \text{one-box},
\qquad
\pi_O(\text{empty}) = \text{two-box},
\]

and

\[
\pi_T(\text{full}) = \text{two-box},
\qquad
\pi_T(\text{empty}) = \text{two-box}.
\]

The predictor’s filling decision depends on what the policy would do upon seeing a full box.

If P-FDT intervenes on \(\mathrm{Pol}=\pi_O\), then with high probability the predictor predicted one-boxing-on-full and filled the box. The agent sees a full box and one-boxes:

\[
\mathrm{EU}_{\text{P-FDT}}(\pi_O)
\approx
0.99 \cdot \$1{,}000{,}000
+
0.01 \cdot \$1{,}000
=
\$990{,}010.
\]

If P-FDT intervenes on \(\mathrm{Pol}=\pi_T\), then with high probability the predictor predicted two-boxing-on-full and left box B empty. The agent sees an empty box and two-boxes:

\[
\mathrm{EU}_{\text{P-FDT}}(\pi_T)
\approx
0.99 \cdot \$1{,}000
+
0.01 \cdot \$1{,}001{,}000
=
\$11{,}000.
\]

P-FDT selects \(\pi_O\). When the agent actually sees both boxes full, she executes

\[
\pi_O(\text{full}) = \text{one-box}.
\]

This is the striking feature: after seeing that box B is full, P-FDT still one-boxes. It does not condition on the observation as though the observation were independent of the policy. Instead, it treats “seeing a full box” as one of the inputs to which the selected policy responds.

Parfit’s hitchhiker problem is structurally similar. An agent is stranded in a desert. A driver will rescue her only if the driver predicts that she will pay \$1,000 after arriving in the city. The driver is 99% accurate at detecting whether the agent would pay.

The relevant policy is:

\[
\pi_{\text{pay}}(\text{city}) = \text{pay}.
\]

The alternative is:

\[
\pi_{\text{refuse}}(\text{city}) = \text{refuse}.
\]

If the driver predicts payment, the agent is rescued and later pays. If the driver predicts refusal, the agent is left in the desert. P-FDT selects the payment policy, because the driver’s rescue decision subjunctively depends on the agent’s policy. Upon arriving in the city, the P-FDT agent pays.

Causal decision theory and evidential decision theory, once the agent is safely in the city, both see no reason to pay. P-FDT avoids that failure by choosing the policy before applying the input “I am now in the city.”

---

## 5. How P-FDT evaluates alternatives

P-FDT evaluates alternatives by comparing entire policy-implementations, not by comparing isolated actions while holding the rest of the world fixed in a purely causal way.

Suppose two policies \(\pi\) and \(\pi'\) agree on the actual input \(x\), but differ on some other input \(y\). A purely local action theory might treat them as equivalent. P-FDT need not. If predictors or other agents respond to what the agent would do at \(y\), then the difference between \(\pi(y)\) and \(\pi'(y)\) can affect the actual world.

This is exactly what happens in transparent Newcomb. The agent’s policy for seeing an empty box may affect the predictor’s prediction, even if the agent actually sees a full box. More generally, P-FDT allows unactualized branches of a policy to matter when the environment predicts or simulates the policy.

P-FDT also has its own version of dominance. A policy \(\pi\) dominates \(\pi'\) if, holding fixed the relevant subjunctive dependency structure, switching from \(\pi'\) to \(\pi\) is never worse and sometimes better. In Newcomb’s problem, two-boxing does not dominate one-boxing in this P-FDT sense, because changing the policy from one-boxing to two-boxing also changes the predictor’s likely behavior.

---

## 6. Open questions and operational interpretations

Footnote 16 gives the central idea but not a complete formal theory. Several choices remain unresolved.

### 6.1 What is the set of policies?

The footnote says that P-FDT chooses a policy mapping inputs to actions, but it does not say which policies are available. In finite toy problems, we can simply list the relevant policies. In realistic settings, the set may be huge or infinite.

A natural assumption is that the agent considers a tractable class of computable policies, perhaps restricted by the agent’s computational limits. For the examples above, the relevant policy class is small and explicit. I will assume that \(\Pi\) is supplied by the decision context or by the agent’s feasible planning vocabulary. This is an additional operational assumption, not a claim found explicitly in the footnote.

### 6.2 How should observations be handled?

The most delicate question is how P-FDT should treat an observation that has already been received.

In my preferred operational interpretation, P-FDT selects a policy by evaluating

\[
\mathbb{E}[V \mid \mathrm{do}(\mathrm{Pol}=\pi)]
\]

relative to the agent’s model, and then applies that policy to the actual input. If the observation is itself policy-dependent — for example, “I see a full box,” “I received the blackmail letter,” or “I am in the city” — P-FDT does not condition the policy evaluation on that observation as though it were exogenous. Instead, the observation is treated as an input to the policy.

If an observation is genuinely exogenous relative to the policy — for example, ordinary evidence about weather, payoffs, or other facts not influenced by the agent’s policy — then the agent may update \(P\) before selecting the policy. More generally, one could write

\[
\pi^*
\in
\arg\max_{\pi}
\mathbb{E}[V \mid \mathrm{do}(\mathrm{Pol}=\pi), E=e],
\]

where \(E\) represents exogenous evidence. The graph \(G\) determines which observations count as exogenous and which are downstream of the policy.

This distinction is my proposal for making P-FDT operational. The source does not fully specify how policy selection interacts with already-received observations. But this interpretation preserves the central policy idea: the agent should not let policy-dependent observations become reasons to abandon the policy that made those observations favorable in the first place.

### 6.3 How is the subjunctive dependency graph constructed?

The source admits that the biggest open problem for functional decision theory is determining the structure of subjunctive dependencies from observation and experiment. P-FDT inherits this problem.

In examples, we can construct \(G\) by asking: does this variable track the output of the agent’s decision procedure?

For predictors, the answer is usually yes. For lesions, the answer is usually no. For copies or twins using the same reasoning procedure, the answer is yes. For ordinary common causes that do not represent the agent’s decision, the answer is no.

But this is a heuristic. A fully general method for learning or justifying \(G\) is not supplied by the source.

### 6.4 Why multi-agent dilemmas?

The footnote says the difference between action-selection and policy-selection “only matters in multi-agent dilemmas so far as we can tell.” This claim is also left underdeveloped.

The likely reason is that single-agent predictor problems can often be represented either by action-level nodes for each possible observation or by a single policy node. Once multiple agents are involved, however, other agents may respond not just to the agent’s current action but to her whole pattern of behavior: her willingness to pay, retaliate, cooperate, vote, honor agreements, or resist extortion. In such cases, selecting a policy can change the strategic environment in ways that a one-shot action intervention may not capture.

For example, in voting coalitions, an agent’s decision may depend on whether she expects others to reason similarly. In blackmail, the blackmailer’s choice to send a threat depends on the agent’s predicted response policy. In bargaining, credibility depends on what policy the agent would carry out in future contingencies. P-FDT is naturally suited to these cases because it evaluates the agent as a fixed policy-source, not as a sequence of disconnected local optimizers.

Still, the source does not give a detailed multi-agent formalization. The policy equation above should therefore be understood as an interpretive development of the footnote, not as an explicit formula from the source.

---

## Conclusion

Policy functional decision theory, P-FDT, treats rational choice as the selection of a policy by a fixed decision procedure. Instead of asking which physical act causes the best outcome, or which act would be best news, P-FDT asks which policy, if output by this very decision procedure, would yield the best world. The agent then applies that policy to her actual input.

Mathematically, P-FDT can be expressed as maximizing expected utility under an intervention on a policy variable:

\[
\pi^*
\in
\arg\max_{\pi}
\mathbb{E}[V \mid \mathrm{do}(\mathrm{Pol}=\pi)],
\]

with the actual action given by \(\pi^*(x)\). The graph used in the intervention must encode subjunctive dependencies: predictors, twins, copies, simulations, and other processes that depend on the agent’s decision procedure. Mere statistical correlations, such as the smoking lesion, are not treated as policy-dependent unless the graph says they are.

P-FDT one-boxes in Newcomb’s problem, smokes in the smoking lesion problem, cooperates with psychological twins, pays the driver in Parfit’s hitchhiker problem, and one-boxes in transparent Newcomb. Its most distinctive feature is that it evaluates the whole policy, including what the agent would do in other possible inputs, because the world may respond to the agent’s policy rather than merely to her present bodily movement.

The theory is powerful, but incomplete. It requires a subjunctive dependency graph, a policy space, and an account of counterpossible reasoning. The source identifies these as open problems. Even so, P-FDT gives a clear operational principle: choose the policy whose implementation would produce the best global outcome, then act accordingly.

---

## Reference

Yudkowsky, E., and Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv source supplied for this assignment, especially footnote 16. Available at: https://arxiv.org/src/1710.05060v2