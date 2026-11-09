# Policy Functional Decision Theory: Choosing Policies, Not Acts

Policy functional decision theory, which I will call **P-FDT**, is a decision theory that evaluates choices by asking which *policy*—a mapping from possible observations to actions—would produce the best outcome if it were the output of the agent’s decision procedure. The name is not the one used in the source paper, which presents the theory under the name “functional decision theory.” However, footnote 16 of Yudkowsky and Soares’s paper says:

> “the author’s preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action.”

That policy-selecting formulation is the theory I will develop here as **P-FDT**. I will use **EDT** for evidential decision theory and **CDT** for causal decision theory, following the source’s distinction.

The core philosophical motivation is simple. In many decision problems, what matters is not merely the local physical movement an agent makes at one moment. What matters is the output of a reasoning procedure that other agents, predictors, simulations, or copies may model, predict, or instantiate. P-FDT therefore treats the decision as the output of a fixed mathematical function, but with an important refinement: the function’s output is not just an action. It is a policy.

So P-FDT asks:

> “Which policy should this very decision procedure output, given that the policy will then be applied to my actual observations?”

This differs from CDT, which asks which physical act causes the best outcome, and from EDT, which asks which act would be the best evidence. P-FDT instead asks which *logical output of the policy-selection function* would yield the best total outcome, once all relevant dependencies are taken into account.

---

## 1. From acts to policies

In the action-level presentation of the source’s theory, an agent with world-model \(P\), dependency graph \(G\), and current observation \(x\) chooses an action by maximizing

\[
\mathrm{FDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb{E}\!\left[V \mid \mathrm{do}(\mathrm{fdt}(\underline{P},\underline{G},\underline{x})=a)\right].
\]

Here \(\mathrm{fdt}(\underline{P},\underline{G},\underline{x})\) is a variable representing the output of the agent’s decision function on those inputs. The intervention \(\mathrm{do}(\cdot)\) is not a physical intervention on the agent’s body. It is an intervention on a logical variable: the variable saying what the decision function outputs.

P-FDT replaces the action variable with a policy variable. Let:

- \(\mathcal X\) be a set of observation histories or inputs,
- \(\mathcal A\) be a set of actions,
- \(\Pi = \mathcal A^{\mathcal X}\) be the set of policies \(\pi : \mathcal X \to \mathcal A\).

Let \(\Phi\) be a distinguished variable in the agent’s model representing the policy selected by P-FDT. The agent’s actual action, upon receiving observation \(x\), is then

\[
A = \Phi(x).
\]

A P-FDT agent chooses a policy by intervening on \(\Phi\). The basic decision rule is:

\[
\mathrm{P\text{-}FDT}(P,G)
\in
\arg\max_{\pi \in \Pi}
\mathrm{EU}(\pi; P,G),
\]

where

\[
\mathrm{EU}(\pi; P,G)
=
\mathbb{E}\!\left[V \mid \mathrm{do}(\Phi=\pi)\right].
\]

Equivalently, if outcomes \(o \in \mathcal O\) have utility \(U(o)\),

\[
\mathrm{EU}(\pi; P,G)
=
\sum_{o \in \mathcal O}
P(o \mid \mathrm{do}(\Phi=\pi))\, U(o).
\]

Once the optimal policy \(\pi^*\) is selected, the agent does not separately maximize over actions. She simply applies the policy to her actual observation:

\[
a^* = \pi^*(x).
\]

This is the mathematical core of P-FDT. The theory is still an expected-utility theory in the broad sense discussed by Joyce: it maximizes expected utility relative to a particular account of the hypotheticals used to evaluate options. But the hypotheticals are not formed by conditioning on acts, as in EDT, nor by intervening only on physical acts, as in CDT. They are formed by intervening on the policy output of the agent’s decision procedure.

---

## 2. How P-FDT constructs hypotheticals

To apply P-FDT, an agent needs a model \(M=(P,G)\). The probability distribution \(P\) represents the agent’s beliefs. The graph \(G\) represents the dependency structure of the world, including not only causal dependencies but also what the source calls *subjunctive dependencies*.

A variable subjunctively depends on the agent’s decision procedure if it would have been different had the procedure’s output been different. The source’s paradigm examples are predictors, psychological twins, simulations, and calculators computing the same function. If two reliable calculators compute \(6288+1048\), then seeing one output \(7336\) gives you reason to think the other outputs \(7336\). There need be no causal interaction between them. Their outputs are tied by the fact that they are computing the same mathematical function.

P-FDT treats decision procedures similarly. If a predictor has modeled the agent’s decision procedure, then the predictor’s prediction depends on what that procedure outputs. If a psychological twin uses the same reasoning procedure, then the twin’s action depends on the same output. If a simulation runs the same policy, its behavior depends on that policy. These are not merely statistical correlations. They are correlations grounded in shared computation or accurate representation.

By contrast, a merely statistical common cause does not create subjunctive dependence. The source’s smoking lesion problem is the standard example: a lesion may cause both a preference for smoking and lung cancer, but the lesion does not compute, predict, or instantiate the agent’s decision procedure. Therefore, when P-FDT imagines a different policy output, it does not imagine the lesion changing merely because the policy changed.

This gives P-FDT its distinctive counterfactual discipline:

- EDT preserves too many correlations. When EDT imagines an action, it conditions on that action and thereby treats all action-correlated events as relevant evidence.
- CDT preserves too few correlations. When CDT imagines an action, it se correlations not caused by the physical act, even when those correlations arise from predictors or copies of the decision procedure.
- P-FDT preserves the decision-relevant subjunctive dependencies. It changes the policy variable and updates everything that depends on that policy, while leaving unrelated statistical common causes fixed.

The source acknowledges that this requires a kind of counterpossible reasoning. If the decision procedure is deterministic, then it has exactly one output on its actual inputs. Imagining a different output is, strictly speaking, imagining something counter-to-logic. The source says that a fully satisfactory formal operator for such reasoning is not yet available. In the graphical formalization, the burden is placed on the graph \(G\): given \(G\), one can reuse a Pearl-style \(\mathrm{do}\)-operator to propagate the intervention.

Thus P-FDT is formally clear only relative to a dependency graph that correctly says what would change if the policy variable changed. The source itself identifies the construction of such graphs as an open problem.

---

## 3. Example: P-FDT in Newcomb’s problem

Newcomb’s problem is the simplest case where P-FDT differs from CDT.

An agent faces two boxes. Box A contains \$1,000. Box B contains \$1,000,000 if a highly reliable predictor predicted that the agent would take only Box B; otherwise Box B is empty. The predictor has already acted.

Here there is effectively one observation, so policies reduce to actions. Let

\[
\Pi = \{\texttt{one-box}, \texttt{two-box}\}.
\]

The predictor’s prediction is modeled as a noisy copy of the policy variable \(\Phi\):

\[
P(\text{Prediction}=\pi \mid \Phi=\pi) = 0.99.
\]

Box B is full iff the predictor predicted one-boxing.

If P-FDT intervenes on \(\Phi=\texttt{one-box}\), then the predictor probably predicted one-boxing, so Box B is probably full. The expected utility is approximately

\[
0.99 \cdot \$1{,}000{,}000 + 0.01 \cdot \$0
=
\$990{,}000.
\]

If P-FDT intervenes on \(\Phi=\texttt{two-box}\), then the predictor probably predicted two-boxing, so Box B is probably empty. The expected utility is approximately

\[
0.99 \cdot \$1{,}000 + 0.01 \cdot \$1{,}001{,}000
=
\$11{,}000.
\]

Therefore,

\[
\mathrm{P\text{-}FDT}(P,G) = \texttt{one-box}.
\]

P-FDT one-boxes, not because one-boxing is good news, and not because the agent physically causes the predictor’s past action to change, but because the predictor’s prediction subjunctively depends on the same decision procedure whose policy P-FDT is selecting.

---

## 4. Example: P-FDT in the smoking lesion problem

The smoking lesion problem is the corresponding test case where EDT goes wrong.

An agent chooses whether to smoke. Smoking is correlated with lung cancer, but only because a lesion causes both a preference for smoking and cancer. Smoking itself does not cause cancer. The agent gains \$1,000 utility from smoking and gains \$1,000,000 utility from not dying of cancer.

A P-FDT model contains variables for the lesion, cancer, action, and policy. Crucially, the lesion is not a child of the policy variable \(\Phi\). The lesion may affect the agent’s preferences or tendencies, but it does not compute the agent’s policy.

Thus, when P-FDT compares

\[
\mathrm{do}(\Phi=\texttt{smoke})
\]

with

\[
\mathrm{do}(\Phi=\texttt{refrain}),
\]

the probability of cancer is held fixed, because cancer depends on the lesion, not on the policy variable. Smoking adds \$1,000 utility without changing the probability of cancer. Therefore P-FDT chooses to smoke.

In the source’s more careful treatment, the agent may be uncertain about which utility function she has, because the lesion affects preferences. The formal model then includes two possible decision procedures, one for each possible preference state. Even there, intervening on the relevant policy variable does not change the probability of the lesion. The smoking policy remains better by a positive amount. P-FDT therefore smokes.

This shows the difference between P-FDT and EDT. EDT refrains because refraining is good news: it is evidence that the agent lacks the lesion. P-FDT does not manage the news. It asks what would happen if the policy variable were different, and it recognizes that the lesion is not subjunctively tied to the policy.

---

## 5. Example: P-FDT in transparent Newcomb and Parfit’s hitchhiker

P-FDT becomes especially interesting when the agent’s observation is itself policy-dependent.

Consider the transparent Newcomb problem. Both boxes are transparent. The predictor placed \$1,000,000 in Box B iff she predicted that the agent would leave Box A behind upon seeing that both boxes are full. The agent may therefore see two full boxes.

CDT and EDT both two-box when the agent sees that Box B is full. CDT says the contents are already fixed, so taking both boxes yields an extra \$1,000. EDT says that conditional on seeing Box B full, taking both boxes is better news.

P-FDT disagrees. The key is that the agent should not evaluate the isolated physical act “take both boxes now” while holding the predictor’s prediction fixed. Instead, P-FDT evaluates policies.

Let the possible observations be:

\[
\mathcal X = \{\texttt{full}, \texttt{empty}\}.
\]

Consider three candidate policies:

1. \(\pi_{11}\): one-box if full, one-box if empty.
2. \(\pi_{12}\): one-box if full, two-box if empty.
3. \(\pi_{22}\): two-box if full, two-box if empty.

Assume the predictor is 99% accurate about what policy the agent will run, specifically about whether the agent will one-box upon seeing full boxes.

For \(\pi_{12}\), the likely course of events is:

- With probability 0.99, the predictor predicts one-boxing upon seeing full boxes, fills Box B, the agent sees full boxes, and one-boxes: payoff \$1,000,000.
- With probability 0.01, the predictor mistakenly predicts two-boxing, leaves Box B empty, the agent sees empty boxes, and two-boxes: payoff \$1,000.

So

\[
\mathrm{EU}(\pi_{12})
=
0.99 \cdot \$1{,}000{,}000
+
0.01 \cdot \$1{,}000
=
\$990{,}010.
\]

For \(\pi_{22}\), the likely course of events is:

- With probability 0.99, the predictor predicts two-boxing, leaves Box B empty, the agent sees empty boxes, and two-boxes: payoff \$1,000.
- With probability 0.01, the predictor mistakenly predicts one-boxing, fills Box B, the agent sees full boxes, and two-boxes: payoff \$1,001,000.

So

\[
\mathrm{EU}(\pi_{22})
=
0.99 \cdot \$1{,}000
+
0.01 \cdot \$1{,}001{,}000
=
\$11{,}000.
\]

For \(\pi_{11}\), the expected utility is

\[
0.99 \cdot \$1{,}000{,}000
+
0.01 \cdot \$0
=
\$990{,}000.
\]

Thus P-FDT selects \(\pi_{12}\): one-box if full, two-box if empty.

Now suppose the agent actually sees full boxes. P-FDT does not ask, “Given that I see full boxes, should I add Box A?” Instead, it says: the selected policy maps this observation to one-boxing. Therefore the agent one-boxes.

This is the same reasoning that makes P-FDT pay the driver in Parfit’s hitchhiker problem. The driver helps iff she predicts the agent will later pay. Once in the city, CDT and EDT see no reason to pay. But P-FDT selects the policy “pay if in the city,” because that policy causes the driver to help in the first place.

The important structural point is that P-FDT allows observations to vary across the counterfactual policies it evaluates. If the agent imagines a policy that two-boxes upon seeing full boxes, she must also imagine that the predictor probably would not have filled the box, so she probably would not be seeing full boxes. The mere fact that she actually sees full boxes does not justify evaluating the policy conditional on that observation as though the observation were independent of the policy.

This is one place where the policy formulation is especially natural. The agent is not choosing an act at a single node while holding the rest of history fixed. She is choosing a complete response pattern, and the world’s response to that pattern includes which observations she receives.

---

## 6. Example: P-FDT and blackmail

P-FDT also recommends refusing blackmail in cases where CDT and EDT pay.

Consider a mechanical blackmail problem. A blackmailer has damaging information. She runs a program that will publish the information unless the agent pays \$1,000 within 24 hours. She runs the program only if she predicts the agent will pay upon receiving the blackmail letter. The agent receives the letter.

CDT says: the program is already running, so paying saves \$999,000. EDT says: receiving the letter is bad news, but paying makes it more likely that the damaging information will not be published. Both pay.

P-FDT evaluates policies. One policy is:

\[
\pi_{\text{pay}}(\texttt{letter}) = \texttt{pay}.
\]

Another is:

\[
\pi_{\text{refuse}}(\texttt{letter}) = \texttt{refuse}.
\]

If the blackmailer accurately predicts the agent’s policy, then a paying policy makes the blackmailer send the letter and run the program. A refusing policy makes the blackmailer not send the letter. The underlying damaging information is not subjunctively dependent on the agent’s policy; the blackmailer’s decision to send the letter is.

So P-FDT compares:

- a world in which the policy pays when blackmailed, and therefore blackmail occurs;
- a world in which the policy refuses when blackmailed, and therefore blackmail does not occur.

The refusing policy has higher expected utility. P-FDT selects it. If the agent actually receives the letter, she refuses to pay.

This may seem strange: the agent knows she has received the letter, yet she acts as though refusing makes it less likely that she received the letter. But that is exactly the source’s point about policy-dependent observations. P-FDT says that agents should entertain the hypothesis that, if their action were different, they might have made different observations. The agent’s actual observation is used as an input to the selected policy, not necessarily as a conditioning event that overrides policy selection.

---

## 7. P-FDT and multi-agent problems

Footnote 16 says that the difference between choosing actions and choosing policies “only matters in multi-agent dilemmas so far as we can tell.” The source does not fully develop that claim, so some interpretation is needed.

In multi-agent settings, P-FDT can treat other agents’ decisions as depending on the same policy variable when those agents are running the same reasoning procedure, using accurate models of the agent, or facing symmetric choices.

For example, in a prisoner’s dilemma against a perfect psychological twin, both agents use the same policy-selection procedure. If the shared procedure outputs a cooperative policy, both cooperate. If it outputs a defection policy, both defect. P-FDT compares:

\[
\mathrm{do}(\Phi=\texttt{cooperate})
\]

with

\[
\mathrm{do}(\Phi=\texttt{defect}).
\]

If mutual cooperation pays more than mutual defection, P-FDT chooses cooperation.

In voting coalitions, coordinated group action, and agreements between agents who can predict one another, P-FDT can recognize that individual decisions are not subjunctively independent. My choice is not a physically isolated event; it is the output of a procedure that others may instantiate or predict. P-FDT allows those logical or computational dependencies to enter the expected-utility calculation.

However, the source gives no complete game-theoretic solution concept for all multi-agent cases. If several agents use P-FDT but have different models, or if each agent’s policy selection depends on predictions of the others’ policy selection, one may need fixed-point reasoning or a more elaborate dependency graph. The footnote tells us that policy selection is the preferred formulation, but it does not give a full algorithm for every multi-agent equilibrium. This is an important open area.

---

## 8. Open questions and an operational interpretation

The footnote gives the central idea of P-FDT but leaves several questions unresolved. I will separate the source’s claims from my own operational proposals.

### 8.1 When is the policy selected?

The source says P-FDT intervenes to choose a policy, then applies inputs to that policy. It does not explicitly say whether the policy is selected before observation, after observation, or in some updateless sense.

In my view, the most coherent operational reading is that P-FDT selects policies from a perspective that does not condition on policy-dependent observations. If the agent has already received an observation \(x\), she still asks which whole policy would have been best to implement, taking into account that different policies may lead to different observations. Then she applies the selected policy to \(x\).

This is not merely a formal preference. It is necessary to recover the source’s desired behavior in transparent Newcomb and blackmail cases. If P-FDT conditioned policy selection on the observation “Box B is full,” then two-boxing would look better, because conditional on seeing a full box, taking both boxes yields more money. If P-FDT conditioned policy selection on receiving the blackmail letter, paying would look better, because conditional on receiving the letter, paying avoids greater damage. But those conditioned evaluations ignore the fact that the observation itself depends on the policy being evaluated.

When observations are genuinely exogenous—say, seeing whether it is raining before choosing whether to carry an umbrella—conditioning on them is harmless. A reasonable operational rule is therefore:

\[
\pi^*
=
\arg\max_{\pi}
\mathbb{E}[V \mid \mathrm{do}(\Phi=\pi), E=e],
\]

where \(E=e\) represents background evidence that is not itself affected by the policy variable. But if an observation is a descendant of the policy variable, P-FDT should not condition on it when selecting the policy.

This updateless reading is my proposal, though it is strongly suggested by the source’s discussion of observations and by the connection to updateless decision theory mentioned in the paper’s notes.

### 8.2 What is the policy space?

The footnote does not say which policies are admissible. Mathematically, one might take \(\Pi\) to be all functions from observations to actions. Practically, an agent cannot optimize over infinitely many arbitrary functions.

A reasonable operational interpretation is to restrict \(\Pi\) to policies the agent can represent, compute, or implement. In finite toy problems, \(\Pi\) can be the full finite set of mappings. In realistic settings, \(\Pi\) should be a tractable class of policies, perhaps parameterized policies or policies generated by known decision rules.

This introduces approximation. P-FDT is best understood as an ideal theory first: given full knowledge of \(P\), \(G\), and \(\Pi\), choose the optimal policy. Bounded agents approximate this ideal.

### 8.3 How is the subjunctive dependency graph constructed?

The source explicitly says that this is perhaps the largest open problem for functional decision theory. Pearl’s causal machinery gives CDT a clear method for representing causal structure, but there is no equally mature formal method for discovering logical, computational, or subjunctive dependencies from observation and experiment.

Operationally, an agent should ask:

1. Which parts of the world are predictions, simulations, copies, or consequences of my decision procedure?
2. Which parts are merely statistically correlated with my action but not computed from or responsive to my decision procedure?
3. Which observations are generated by predictors of my policy?
4. Which other agents are using the same reasoning procedure or a sufficiently accurate model of it?

Variables in the first category should be downstream of \(\Phi\). Variables in the second category should not be. This is a modeling principle, not a complete formal discovery procedure.

### 8.4 What about logical uncertainty?

P-FDT requires reasoning about what would happen if a deterministic function had a different output. This is counterpossible reasoning. The source mentions that human mathematicians can reason about unresolved or impossible mathematical assumptions in limited ways, but it does not provide a full formal account.

An operational P-FDT agent may therefore use approximations: logical induction, bounded proof search, simulation, or heuristic reasoning about algorithms. The formal equation

\[
\mathrm{EU}(\pi) = \mathbb{E}[V \mid \mathrm{do}(\Phi=\pi)]
\]

states the target, but computing it in realistic settings remains difficult.

---

## 9. What P-FDT changes about decision-making

P-FDT changes the unit of evaluation. CDT evaluates physical acts. EDT evaluates acts as evidence. P-FDT evaluates policies as logical outputs.

This has several consequences.

First, P-FDT behaves like a precommitted agent without needing actual precommitment. In transparent Newcomb, an agent would want to precommit to one-box upon seeing full boxes. P-FDT simply selects that policy.

Second, P-FDT avoids the instability of CDT in predictor problems. In Death in Damascus, CDT imagines changing location while holding Death’s prediction fixed. P-FDT recognizes that Death’s prediction depends on the decision procedure, so it imagines the prediction changing too.

Third, P-FDT gives a nonnegative value to information in the relevant sense. If seeing a full box would tempt a CDT or EDT agent to make a worse choice, P-FDT avoids the temptation by evaluating the whole policy rather than re-deciding locally.

Fourth, P-FDT resists extortion. If paying blackmailers makes one a blackmail target, P-FDT selects a refusing policy, because the policy variable affects whether the blackmail occurs at all.

Finally, P-FDT supplies its own dominance principle. An action or policy is dominated only relative to a way of constructing counterfactuals. CDT dominance holds predictors fixed while changing the act. P-FDT says that if the predictor depends on the policy, holding the prediction fixed while changing the act is not the relevant comparison. The relevant comparison holds the subjunctive dependency structure fixed while changing the policy output.

---

## Conclusion

Policy functional decision theory is best understood as an expected-utility theory that maximizes over policies by intervening on a logical variable representing the output of the agent’s policy-selection procedure. Its central rule is:

\[
\pi^*
\in
\arg\max_{\pi \in \Pi}
\mathbb{E}[V \mid \mathrm{do}(\Phi=\pi)],
\]

with the actual action given by

\[
a^* = \pi^*(x).
\]

The theory preserves dependencies that arise from prediction, simulation, shared computation, and replication of the decision procedure. It ignores merely statistical correlations that do not arise from such subjunctive dependence. It therefore one-boxes in Newcomb’s problem, smokes in the smoking lesion problem, pays in Parfit’s hitchhiker problem, one-boxes in transparent Newcomb when seeing full boxes, and refuses blackmail when paying would invite blackmail.

The source leaves important formal work unfinished: constructing subjunctive dependency graphs, handling counterpossible reasoning, defining the admissible policy space, and fully developing multi-agent cases. The operational reading I have proposed treats P-FDT as updateless with respect to policy-dependent observations and restricts policy spaces to implementable policies. These additions are not fully explicit in footnote 16, but they seem necessary if P-FDT is to be used as a practical decision procedure.

Even with those open problems, P-FDT offers a clear and attractive principle: do not ask only what act to perform now; ask what policy this very decision procedure should output, knowing that the world may already be responding to that output.

---

## References

Joyce, James M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

Pearl, Judea. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.

Yudkowsky, Eliezer, and Nate Soares. “Functional Decision Theory: A New Theory of Instrumental Rationality.” arXiv:1710.05060v2, 2017.