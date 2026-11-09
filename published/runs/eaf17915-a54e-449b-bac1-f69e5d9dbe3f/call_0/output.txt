# Policy Functional Decision Theory (P-FDT)

Policy functional decision theory (P-FDT) is the policy-selecting version of the decision theory presented by Yudkowsky and Soares in “Functional Decision Theory: A New Theory of Instrumental Rationality.” The paper’s main formal equation often intervenes on an observation-indexed decision variable, but the policy-selection passage in footnote 16 says that the authors’ preferred formulation is different: “the author's preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action.” The footnote adds that this distinction “only matters in multi-agent dilemmas so far as we can tell.”

This essay reconstructs P-FDT from that passage. I will treat P-FDT as a theory that chooses an entire input-to-action policy by performing a counterfactual intervention on the output of the agent’s policy-selection procedure, and then executes the policy at the actual input. The footnote is brief, so several details below are my own operational elaborations. Where I add assumptions, I will say so.

---

## 1. The central idea of P-FDT

P-FDT accepts the core functional-decision-theoretic principle: a rational agent should treat her decision as the output of a fixed mathematical procedure. But instead of asking, “Which physical act should I perform?” P-FDT asks:

> Which output of this very policy-selection procedure would produce the best outcome?

An output is not a single act, but a policy: a rule mapping observations, inputs, or histories to actions. Once the best policy is selected, the agent feeds her actual observations into it and performs whatever action it returns.

This differs from the two classical theories:

- **Evidential decision theory (EDT)** asks which action would be the best news to learn one had taken.
- **Causal decision theory (CDT)** asks which physical action causally produces the best consequences.
- **P-FDT** asks which policy, understood as the output of a fixed computational procedure, yields the best world when all relevant subjunctive dependencies are respected.

The key move is that P-FDT does not intervene directly on the physical action variable. It intervenes on a logical variable representing the agent’s policy. The action is then determined by the policy together with the agent’s inputs.

---

## 2. A formal reconstruction of P-FDT

The source gives a Pearl-style formulation for action-level FDT:

\[
\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}
\mathbb{E}\left[V \mid \operatorname{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\right],
\]

where \(P\) is a probabilistic model, \(G\) encodes dependency structure, \(x\) is an observation history, and the intervention is on the output of the decision function given that input.

P-FDT replaces the observation-indexed action output with a policy output. I will write \(D\) for the logical variable representing the output of the agent’s P-FDT policy-selection procedure. This notation is my own; the source speaks of intervening on the node `FDT(-)`.

Let:

- \(\mathcal X\) be a set of observations or observation histories;
- \(\mathcal A\) be a set of actions;
- \(\Pi\) be the set of policies, where a deterministic policy is a function  
  \[
  \pi:\mathcal X\to\mathcal A;
  \]
- \(V\) be the utility-bearing outcome variable;
- \(D\) be the variable representing the selected policy.

A P-FDT agent has a world-model \((P,G)\). The distribution \(P\) assigns probabilities to variables including observations, actions, predictions made by other agents or predictors, background states, outcomes, and the logical variable \(D\). The graph \(G\) encodes how those variables depend on one another. Crucially, \(G\) may contain arrows from \(D\) to predictors, copies of the agent, or other agents’ expectations, when those things depend on the agent’s policy. It should not contain arrows from \(D\) to merely statistically correlated background variables, such as lesions, unless the agent’s policy genuinely depends on them.

For each policy \(\pi\in\Pi\), define the P-FDT expected utility by

\[
\mathrm{EU}_{\mathrm{P\text{-}FDT}}(\pi;P,G)
=
\mathbb{E}_P\left[V \mid \operatorname{do}(D=\pi);\,G\right].
\]

Then P-FDT selects a policy

\[
\pi^* \in \arg\max_{\pi\in\Pi} \mathrm{EU}_{\mathrm{P\text{-}FDT}}(\pi;P,G).
\]

If the agent’s actual input is \(x\), the action taken is

\[
a^* = \pi^*(x).
\]

Equivalently, in outcome-sum form,

\[
\mathrm{EU}_{\mathrm{P\text{-}FDT}}(\pi)
=
\sum_o P\bigl(O=o \mid \operatorname{do}(D=\pi)\bigr)\,\mathcal U(o),
\]

where \(O\) is an outcome variable and \(\mathcal U\) is the utility function.

For dynamic problems, \(\mathcal X\) can be the set of observation histories, and a policy maps each history at which the agent must act to an action. For stochastic policies, one can let \(\pi(x)\) be a distribution over actions; the intervention \(D=\pi\) then sets the agent’s randomization rule. The source’s footnote speaks of policies mapping inputs to actions, so I will mostly assume deterministic policies for simplicity.

### Comparison with EDT, CDT, and action-level FDT

The contrast can be summarized schematically. EDT, after observing \(x\), chooses

\[
a_{\mathrm{EDT}}(x)
=
\arg\max_a \mathbb{E}[V\mid X=x, A=a].
\]

CDT chooses

\[
a_{\mathrm{CDT}}(x)
=
\arg\max_a \mathbb{E}[V\mid \operatorname{do}(A=a), X=x].
\]

The paper’s simplified action-level FDT chooses

\[
a_{\mathrm{action\text{-}FDT}}(x)
=
\arg\max_a \mathbb{E}[V\mid \operatorname{do}(D_x=a)],
\]

where \(D_x\) is the output of the decision procedure on input \(x\).

P-FDT instead chooses

\[
\pi^*
=
\arg\max_\pi \mathbb{E}[V\mid \operatorname{do}(D=\pi)],
\]

and then executes \(\pi^*(x)\).

The difference is subtle but important. Action-level FDT intervenes on “what the decision procedure outputs given this input.” P-FDT intervenes on “what policy the procedure selects,” and then lets the actual input be processed by that policy. In many one-shot cases, the recommendations coincide. The footnote says the distinction matters primarily in multi-agent dilemmas, though I think it also helps clarify sequential and precommitment-like problems.

---

## 3. Subjunctive dependence and P-FDT counterfactuals

The source’s central philosophical notion is **subjunctive dependence**. Predictor-like things depend on the agent’s decision procedure in a way that lesion-like things do not. A reliable predictor’s prediction is linked to the agent’s future action because the predictor models the agent’s decision procedure. A carcinogenic lesion may correlate with smoking, but it does not model the agent’s decision procedure.

The source says that functional decision theory is related to subjunctive dependence as causal decision theory is related to causal dependence. P-FDT inherits this idea at the policy level:

- CDT intervenes on a physical action variable \(A\), preserving causal downstream consequences while severing non-causal correlations.
- P-FDT intervenes on a policy-selection variable \(D\), preserving the consequences of changing the policy while holding fixed variables that do not subjunctively depend on that policy.

In graph terms, if a predictor’s prediction variable \(R\) is connected to \(D\) because the predictor simulates or reasons about the agent’s policy, then \(D\to R\) belongs in \(G\). Under \(\operatorname{do}(D=\pi)\), the predictor’s predicted policy changes accordingly. If a background variable \(L\), such as a lesion, is merely a common cause of preferences and cancer, then there is no arrow \(D\to L\). Under \(\operatorname{do}(D=\pi)\), \(L\) stays fixed.

This is how P-FDT distinguishes Newcomb-like cases from smoking-lesion-like cases. In Newcomb’s problem, the predictor’s behavior subjunctively depends on the agent’s decision procedure. In the smoking lesion problem, the lesion does not.

The source acknowledges a difficulty: if the decision procedure is a fixed mathematical function, then saying “this function outputs a different policy” is, strictly speaking, counterpossible. If the actual output is \(\pi^*\), there is no possible world in which the same function on the same inputs outputs \(\pi\neq\pi^*\). Nevertheless, the source argues that agents must reason about such counterpossibles, much as mathematicians reason under uncertainty about unresolved or logically fixed claims. I agree that this is the main formal gap in the theory. Operationally, I interpret P-FDT counterfactuals as modeling an agent’s uncertainty about what would follow if the relevant computation had a different output, without requiring a complete metaphysics of impossible worlds.

---

## 4. P-FDT applied to standard problems

### 4.1 P-FDT in the psychological twin prisoner’s dilemma

An agent and a perfect psychological twin independently choose cooperate or defect. The payoffs are:

- both cooperate: \$1,000,000 each;
- both defect: \$1,000 each;
- one cooperates, one defects: defector gets \$1,001,000, cooperator gets \$0.

A CDT agent defects, because the twin’s action is causally independent. EDT cooperates, because cooperation is good news. P-FDT cooperates for a different reason.

Here there is essentially one decision input, so policies reduce to actions: cooperate or defect. The agent’s model should include the fact that the twin runs the same policy-selection procedure, or at least a sufficiently accurate model of it. Thus the graph contains a subjunctive dependence between the agent’s policy variable \(D\) and the twin’s action.

If \(D=\text{cooperate}\), the twin cooperates, and the agent receives \$1,000,000. If \(D=\text{defect}\), the twin defects, and the agent receives \$1,000. Therefore,

\[
\mathrm{EU}(\text{cooperate}) = 1{,}000{,}000,
\qquad
\mathrm{EU}(\text{defect}) = 1{,}000.
\]

P-FDT selects the cooperate policy.

### 4.2 P-FDT in Newcomb’s problem

In Newcomb’s problem, a predictor places \$1,000,000 in box B iff she predicts the agent will take only box B. Box A visibly contains \$1,000. The predictor is correct 99% of the time.

A CDT agent two-boxes because the predictor’s choice is already in the causal past. EDT one-boxes because one-boxing is evidence that the box is full. P-FDT one-boxes because the predictor’s prediction subjunctively depends on the agent’s policy-selection procedure.

Let the relevant policies be:

- \(\pi_1\): take only box B;
- \(\pi_2\): take both boxes.

Under \(\operatorname{do}(D=\pi_1)\), the predictor probably predicted one-boxing, so box B is probably full. The expected payoff is approximately

\[
0.99 \cdot 1{,}000{,}000 + 0.01 \cdot 0 = 990{,}000.
\]

Under \(\operatorname{do}(D=\pi_2)\), the predictor probably predicted two-boxing, so box B is probably empty. The expected payoff is approximately

\[
0.01 \cdot 1{,}001{,}000 + 0.99 \cdot 1{,}000 = 11{,}000.
\]

Thus P-FDT selects \(\pi_1\), the one-boxing policy.

This follows directly from the policy-intervention rule. P-FDT does not ask, “Given that the boxes are already arranged, which physical act causes more money?” It asks, “Which policy output from this decision procedure leads to the better world, given that reliable predictors depend on that procedure?”

### 4.3 P-FDT in the smoking lesion problem

In the smoking lesion problem, smoking is correlated with cancer, but only because a lesion causes both a love of smoking and cancer. Smoking itself does not cause cancer. Smoking gives \$1,000 of utility. Avoiding cancer is worth \$1,000,000.

EDT refrains from smoking, because smoking is bad news. CDT smokes, because smoking does not causally affect cancer. P-FDT also smokes.

The lesion variable \(L\) should not be downstream of the policy-selection variable \(D\). The lesion may influence whether the agent enjoys smoking, and it may influence cancer, but it does not depend on the output of the agent’s P-FDT procedure. Therefore, under \(\operatorname{do}(D=\pi)\), the probability of cancer is unchanged.

If \(\pi_{\text{smoke}}\) adds \$1,000 of utility and does not change the cancer probability, then

\[
\mathrm{EU}(\pi_{\text{smoke}})
=
\mathrm{EU}(\pi_{\text{refrain}})
+
1{,}000.
\]

So P-FDT selects the smoking policy.

The source gives a more careful model in which the lesion may determine which utility function governs the agent, creating uncertainty about the agent’s own preferences. Even there, the policy-selection node is not connected to the lesion node in the relevant way, and the smoking policy remains preferable. The essential point is unchanged: P-FDT preserves predictor-like dependencies but breaks merely evidential lesion-like correlations.

### 4.4 P-FDT in transparent Newcomb and Parfit’s hitchhiker

The transparent Newcomb problem is like ordinary Newcomb’s problem, except both boxes are transparent. The predictor filled box B iff she predicted that the agent would one-box upon seeing that both boxes are full. If the agent sees that both boxes are full, should she leave box A behind?

CDT says take both boxes. EDT, conditioning on seeing box B full, also says take both boxes. P-FDT says one-box.

At the policy level, the agent chooses a rule for possible observations. A natural policy is:

\[
\pi^*(x)=
\begin{cases}
\text{one-box}, & \text{if } x=\text{full},\\
\text{two-box}, & \text{if } x=\text{empty}.
\end{cases}
\]

Under this policy, a highly accurate predictor predicts one-boxing upon seeing a full box, so the agent usually sees a full box and one-boxes. The expected payoff is roughly

\[
0.99 \cdot 1{,}000{,}000 + 0.01 \cdot 1{,}000 = 990{,}010.
\]

If instead the policy says “two-box when full,” the predictor predicts that, so the agent usually sees an empty box. The expected payoff is roughly

\[
0.01 \cdot 1{,}001{,}000 + 0.99 \cdot 1{,}000 = 11{,}000.
\]

So P-FDT selects the policy of one-boxing upon seeing a full box. When the agent actually sees a full box, she one-boxes, not because she can change the past, but because the policy whose output would have led to the best world is the policy that one-boxes in that situation.

Parfit’s hitchhiker is structurally similar. A driver will save an agent from dying in the desert iff she predicts the agent will later pay \$1,000. Once in the city, CDT and EDT do not pay, because payment has no further causal or evidential benefit. P-FDT selects the policy “pay if in the city.” The driver predicts this, saves the agent, and the agent pays. P-FDT thereby gains the large benefit of being saved, less the payment.

The source emphasizes that one-boxing in transparent Newcomb is equivalent to paying in Parfit’s hitchhiker. P-FDT makes this equivalence transparent: both cases involve choosing a policy that predictors can rely upon, even when the local physical action appears dominated by taking the extra money.

### 4.5 P-FDT and blackmail

Consider a blackmail problem where a predictor sends a blackmail letter only if she predicts the agent will pay. If the agent pays, she loses a small amount. If she refuses, she may suffer a large loss if the program was actually run, but a reliable predictor will not run the program against an agent predicted to refuse.

A policy of paying upon receiving the blackmail letter makes the agent a profitable blackmail target. Under \(\operatorname{do}(D=\pi_{\text{pay}})\), predictors predict payment and send the letter. A policy of refusing makes the agent unattractive to blackmail. Under \(\operatorname{do}(D=\pi_{\text{refuse}})\), predictors predict refusal and usually do not send the letter.

P-FDT therefore selects the refuse policy. If the agent actually receives a letter, she still refuses, because she is executing the policy whose global expected utility was best. This is one of the stranger implications of the theory, but the source accepts it. The agent is allowed to imagine, while holding the letter, that if her policy were different she would probably have had different observations.

This illustrates a distinctive feature of P-FDT: policy evaluation can change the probability of receiving observations. P-FDT does not simply condition on all actual observations as fixed. It conditions on observations only insofar as they are not themselves subjunctively downstream of the policy-selection procedure. This is my operational gloss; the source does not fully formalize the boundary between evidence to be conditioned on and observations to be treated as policy-dependent.

---

## 5. Open questions and an operational interpretation

Because footnote 16 is short, P-FDT requires interpretation beyond the source. The most important open questions concern the policy space, the subjunctive-dependence graph, observations, and multi-agent interaction.

### 5.1 What counts as a P-FDT policy?

The footnote says a policy maps inputs to actions. I have assumed that inputs are observation histories available to the agent. In a sequential problem, a policy should specify an action at every decision point, given the agent’s information at that point. This is standard in decision theory and game theory, and it seems the natural reading of “inputs.”

The source does not say how fine-grained inputs should be. If two observations are decision-theoretically indistinguishable, they should probably belong to the same information state. If a predictor can distinguish them, however, the policy may need to distinguish them too. A practical rule is to use the agent’s actual information partitions: policies map the agent’s possible epistemic situations to actions.

### 5.2 How does P-FDT obtain the graph \(G\)?

The source explicitly says that it does not have a full account of how to deduce subjunctive-dependence structure from observation. This is perhaps the largest open problem for functional decision theory generally. P-FDT inherits the problem.

Operationally, I think a P-FDT agent should construct \(G\) by asking which processes in the environment are sensitive to the agent’s decision procedure. Predictors, simulations, copies, and agents using the same reasoning create arrows from \(D\) to their behavior. Common causes that do not model the agent, such as lesions or unrelated statistical factors, do not.

If the agent is uncertain about \(G\), a natural extension is to maximize expected utility averaged over possible graphs:

\[
\pi^*
\in
\arg\max_\pi
\sum_G P(G)\,
\mathbb{E}[V\mid \operatorname{do}(D=\pi),G].
\]

This is not stated in the source, but it is a conservative operationalization when subjunctive structure is unknown.

### 5.3 How should P-FDT treat actual observations?

P-FDT’s global policy evaluation can appear to ignore evidence. If an agent holds a blackmail letter, why not condition on that fact? The source’s answer, in effect, is that the agent’s observation may itself depend on the policy being evaluated. P-FDT responds to observations by applying the selected policy to them, not by re-optimizing the local action after conditioning them away.

My operational interpretation is this: condition on observations that are exogenous relative to the policy-selection variable; do not condition away observations that are modeled as downstream of \(D\). The graph \(G\) determines which case obtains. If the observation is genuinely fixed and not predictor-dependent, P-FDT can condition on it. If the observation is part of a predictor-mediated process, P-FDT evaluates policies globally and then executes the selected policy at the observed input.

This is not fully formalized in the source, but it preserves the theory’s characteristic behavior in transparent Newcomb, Parfit’s hitchhiker, and blackmail cases.

### 5.4 P-FDT in multi-agent dilemmas

The footnote says the policy/action distinction matters mainly in multi-agent dilemmas. This is plausible. In strategic settings, other agents may predict not merely the agent’s current action but her entire contingent policy. Off-path behavior can affect what other agents do, even if the off-path branch is not reached.

The source does not provide a full multi-agent solution concept. A natural P-FDT approach is to include other agents’ policy-selection variables in the graph. If other agents are known to use P-FDT and share relevant inputs, the graph may encode logical correlation between their policy outputs. In a symmetric prisoner’s dilemma, this yields cooperation. In asymmetric games, the agent may need to choose a best policy given her model of others’ policies.

A further proposal, not in the source, is to seek a reflective policy equilibrium: a profile of policies such that each agent’s policy is P-FDT-optimal given a graph that correctly represents the others’ policy-selection procedures. This resembles a fixed-point condition over policy-selection functions. Whether this is the right multi-agent completion remains open.

---

## Conclusion

Policy functional decision theory (P-FDT) chooses policies rather than isolated physical actions. Its core rule is to intervene on the output of the agent’s policy-selection procedure and choose the policy that yields the highest expected utility when all relevant subjunctive dependencies are respected. Predictor-like dependencies are preserved; lesion-like statistical correlations are not.

This yields the characteristic functional-decision-theoretic prescriptions: cooperate with a perfect twin, one-box in Newcomb’s problem, smoke in the smoking lesion problem, one-box in transparent Newcomb, pay in Parfit’s hitchhiker, and refuse extortion in blackmail problems where payment makes one a target. The theory’s main unresolved issues are formal: counterpossible reasoning, construction of subjunctive-dependence graphs, treatment of observations, and multi-agent equilibrium. But as an operational decision procedure, P-FDT offers a clear rule: choose the policy that would produce the best world if this very policy-selection procedure output it, then act accordingly.

---

## References

Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.

Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.

Yudkowsky, E., and Soares, N. (2017). “Functional Decision Theory: A New Theory of Instrumental Rationality.” arXiv:1710.05060.