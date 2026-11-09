# Policy Functional Decision Theory: Choosing the Best Policy of a Fixed Decision Procedure

Policy functional decision theory, which I will call **P-FDT**, is a policy-selection variant of the decision theory introduced by Yudkowsky and Soares as functional decision theory. The core idea is this: when making a decision, do not ask merely, “Which physical act should I perform?” or “Which act would be best news?” Instead ask, “Which *policy* should be output by this very policy-selection procedure?” The agent then applies the selected policy to its actual input to produce an action.

The primary textual basis for P-FDT in this assignment is footnote 16 of the source paper:

> “the author’s preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then apply her inputs in order to select an action.”

The same paper also says in footnote 7 that in the preferred formalization, “agents actually iterate over policies (mappings from observations to actions) rather than actions.” The paper’s main equations, however, mostly formalize an action-output version of functional decision theory. P-FDT is therefore best understood as a natural extrapolation: replace the action-output node with a policy-output node.

I will use **P-FDT** for this policy-level theory. I will identify the other theories discussed here by their usual names: **evidential decision theory** (EDT), **causal decision theory** (CDT), and the paper’s action-level **FDT**.

---

## 1. The normative idea

P-FDT treats the agent as implementing a fixed mathematical procedure. That procedure takes the agent’s model of the world as input and outputs a *policy*, not a single action. A policy is a function from possible inputs—observations, evidence, histories—to actions.

The normative rule is:

> Choose the policy such that, if this very policy-selection procedure output that policy, the resulting world would be best.

This differs from EDT, which asks which action would be best evidence, and from CDT, which asks which physical intervention on the agent’s action variable would cause the best downstream consequences. P-FDT instead performs a counterfactual intervention on the output of the policy-selection procedure itself.

In simple one-shot problems with a single possible observation, a policy collapses to an action, so P-FDT agrees with action-level FDT. The distinctive character of P-FDT appears when the agent’s dispositions across possible inputs matter to predictors, other agents, or future versions of the agent.

---

## 2. A formal statement of P-FDT

Let:

- \(\mathcal X\) be a finite set of possible inputs or observations;
- \(\mathcal A\) be a finite set of actions;
- \(\Pi = \mathcal A^{\mathcal X}\) be the set of policies \(\pi : \mathcal X \to \mathcal A\);
- \(V\) be a real-valued utility variable;
- \(M = (P, G)\) be the agent’s world-model, where \(P\) is a probability distribution and \(G\) encodes the relevant dependency structure.

In CDT, \(G\) is usually a causal graph. In P-FDT, \(G\) must encode not only causal dependencies but also what the source calls *subjunctive* dependencies: dependencies of predictors, copies, simulations, and other systems whose behavior tracks the output of the agent’s decision procedure.

The model \(M\) contains a distinguished logical variable

\[
\Pi_M
\]

representing the policy output by P-FDT when run on \(M\). This is self-referential, but the source treats this as harmless: an agent can have a variable representing the output of its own decision procedure without already knowing that output.

P-FDT then selects a policy as follows:

\[
\pi^* \in \arg\max_{\pi \in \Pi}
\mathbb{E}_P\!\left[V \mid \operatorname{do}(\Pi_M = \pi)\right].
\]

Here \(\operatorname{do}(\Pi_M = \pi)\) is not merely Pearl’s causal intervention on a physical variable. It is a subjunctive intervention on a logical/policy variable. It sets the output of the agent’s policy-selection procedure to \(\pi\), then propagates the consequences through all variables that, according to \(G\), depend on that policy output.

Once \(\pi^*\) has been selected, the agent receives its actual input \(x \in \mathcal X\) and executes

\[
a^* = \pi^*(x).
\]

That is the whole procedure: choose the best policy, then apply the actual input.

For comparison, the paper’s three action-level theories can be summarized roughly as:

\[
\mathrm{EDT}(P,x)
=
\arg\max_{a \in \mathcal A}
\mathbb{E}[V \mid X=x, A=a],
\]

\[
\mathrm{CDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb{E}[V \mid \operatorname{do}(A=a), X=x],
\]

\[
\mathrm{FDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb{E}[V \mid \operatorname{do}(F_M(x)=a)],
\]

where \(F_M(x)\) is the output of the action-level decision procedure on model \(M\) and input \(x\).

P-FDT replaces the last kind of intervention with an intervention on a policy variable:

\[
\mathrm{P\text{-}FDT}(M)
=
\arg\max_{\pi \in \Pi}
\mathbb{E}[V \mid \operatorname{do}(\Pi_M=\pi)].
\]

The actual action is then \(\mathrm{P\text{-}FDT}(M)(x)\).

This formulation is not given explicitly in the source. The source gives the action-level equation and then says the preferred version chooses policies. The equation above is my reconstruction of that policy-level idea.

---

## 3. How P-FDT evaluates alternatives

P-FDT evaluates alternatives primarily as *policies*, not as isolated actions. If one wants to compare actions at a particular input \(x\), the natural derived comparison is:

\[
\mathrm{EU}(a;x)
=
\max_{\pi \in \Pi : \pi(x)=a}
\mathbb{E}[V \mid \operatorname{do}(\Pi_M=\pi)].
\]

Then P-FDT recommends the action \(a\) whose best compatible policy has highest expected utility. But the officially chosen object is still the whole policy \(\pi^*\), not the action considered in isolation.

This matters because the consequences of a policy may depend on what the agent would do in non-actual situations. A predictor may reward an agent for being the kind of agent who would refuse blackmail, pay a debt, or one-box upon seeing a full box. Those predictions concern the agent’s policy, not merely the physical movement that happens to occur at the actual moment.

P-FDT’s counterfactuals therefore have the form:

> “What would the world look like if this very policy-selection procedure output \(\pi\)?”

not merely:

> “What would the world look like if my body performed action \(a\)?”

The second question is CDT’s question. It severs correlations between the agent’s action and predictors of that action. P-FDT preserves those correlations when they are subjunctive rather than merely statistical.

---

## 4. Subjunctive dependence and counterpossibles

The source distinguishes three kinds of dependence:

1. **Causal dependence**: one event physically brings about another.
2. **Statistical/evidential dependence**: two events are correlated but neither tracks the other in the relevant way.
3. **Subjunctive dependence**: two systems depend on the same mathematical function, or one system accurately represents the output of the other.

The paper’s examples use calculators. Two reliable calculators computing \(6288+1048\) on opposite sides of the world are not causally connected, but their outputs are subjunctively linked: if one outputs \(7336\), the other will too, provided both are functioning correctly. Similarly, a good predictor of an agent’s decision is subjunctively linked to the agent’s decision procedure.

P-FDT uses this notion. When the agent imagines selecting a different policy, it also imagines corresponding changes in predictors, copies, twins, and other agents who model or share that policy-selection procedure. It does not imagine a perfect predictor mysteriously failing while the physical action changes. That is the mistake the source attributes to CDT.

However, P-FDT also requires *counterpossible* reasoning. If the agent’s policy-selection procedure is deterministic, then for a fixed input there is only one mathematically possible output. To ask, “What if it output a different policy?” is to ask something counter-to-logical-necessity. The source admits that this is technically difficult and that we lack a fully satisfactory formal account of counterpossible conditioning. In practice, P-FDT assumes that the agent has, or approximates, a graph \(G\) telling it how the world would change if the policy node had a different value.

This is one of the major open problems inherited by P-FDT: how do we learn or construct the dependency structure \(G\) for logical and computational dependencies in the way Pearl’s framework helps us learn causal dependencies?

---

## 5. Example: Newcomb’s problem

In Newcomb’s problem, an agent may take both boxes or only the opaque box B. A predictor placed \$1,000,000 in B iff she predicted the agent would one-box. The predictor is right 99% of the time.

Here \(\mathcal X\) has only one relevant input, so policies reduce to actions:

\[
\Pi = \{\text{one-box}, \text{two-box}\}.
\]

Let the utility values be:

- one-box, B full: \$1,000,000;
- two-box, B full: \$1,001,000;
- one-box, B empty: \$0;
- two-box, B empty: \$1,000.

In P-FDT, the policy node \(\Pi_M\) is connected to both the agent’s action and the predictor’s prediction. Therefore:

\[
\operatorname{do}(\Pi_M = \text{one-box})
\]

makes B full with probability approximately \(0.99\), while

\[
\operatorname{do}(\Pi_M = \text{two-box})
\]

makes B full with probability approximately \(0.01\).

So the expected utilities are approximately:

\[
\mathrm{EU}(\text{one-box})
=
0.99 \cdot 1{,}000{,}000
+
0.01 \cdot 0
=
990{,}000,
\]

\[
\mathrm{EU}(\text{two-box})
=
0.01 \cdot 1{,}001{,}000
+
0.99 \cdot 1{,}000
=
11{,}000.
\]

P-FDT selects the one-boxing policy. The agent one-boxes.

This matches the source’s action-level FDT prescription, because in a one-input problem the policy version collapses to the action version.

---

## 6. Example: the smoking lesion problem

In the smoking lesion problem, smoking is correlated with cancer, but only because a lesion causes both a love of smoking and cancer. Smoking itself does not cause cancer. The agent gains \$1,000 from smoking and gains \$1,000,000 if she does not die of cancer.

Here P-FDT’s graph differs from EDT’s evidential network. The policy node affects the action, but it does not affect the lesion. The lesion is not predicting the agent’s policy; it is merely a common cause of preferences and cancer.

Thus, under the intervention

\[
\operatorname{do}(\Pi_M = \text{smoke}),
\]

the probability of having the lesion remains the same as under

\[
\operatorname{do}(\Pi_M = \text{refrain}).
\]

Since smoking adds \$1,000 utility and does not change the probability of cancer, P-FDT chooses the smoking policy.

P-FDT therefore gets the desired pair of verdicts: one-box in Newcomb’s problem and smoke in the smoking lesion problem. It does so by preserving predictor-like dependencies while ignoring lesion-like correlations.

---

## 7. Example: transparent Newcomb and Parfit’s hitchhiker

The policy perspective becomes more interesting when the agent may receive different observations depending on the predictor’s earlier behavior.

In the transparent Newcomb problem, the agent can see whether box B is full. The predictor filled B iff she predicted the agent would one-box upon seeing B full.

Let the input set be

\[
\mathcal X = \{\text{full}, \text{empty}\}.
\]

A policy is a pair of responses:

\[
\pi = (\pi(\text{full}), \pi(\text{empty})).
\]

Suppose the predictor is 99% accurate about what the agent’s policy will do upon seeing a full box. Then:

- if \(\pi(\text{full}) = \text{one-box}\), B is probably full;
- if \(\pi(\text{full}) = \text{two-box}\), B is probably empty.

Consider two policies:

\[
\pi_1(\text{full}) = \text{one-box}, \quad
\pi_1(\text{empty}) = \text{two-box};
\]

\[
\pi_2(\text{full}) = \text{two-box}, \quad
\pi_2(\text{empty}) = \text{two-box}.
\]

Under \(\pi_1\), with probability \(0.99\) the agent sees a full box and one-boxes, receiving \$1,000,000; with probability \(0.01\) she sees an empty box and two-boxes, receiving \$1,000. So:

\[
\mathrm{EU}(\pi_1)
\approx
0.99 \cdot 1{,}000{,}000
+
0.01 \cdot 1{,}000
=
990{,}010.
\]

Under \(\pi_2\), with probability \(0.99\) B is empty and the agent two-boxes for \$1,000; with probability \(0.01\) B is full and she two-boxes for \$1,001,000. So:

\[
\mathrm{EU}(\pi_2)
\approx
0.99 \cdot 1{,}000
+
0.01 \cdot 1{,}001{,}000
=
11{,}000.
\]

P-FDT therefore chooses a policy that one-boxes upon seeing a full box. If the actual input is `full`, the agent one-boxes, even though she can see that B contains \$1,000,000.

This is the same structure as Parfit’s hitchhiker problem. A driver will save the agent iff the driver predicts the agent will later pay \$1,000 after being rescued. P-FDT chooses the policy “pay if rescued.” When the agent is rescued, that policy requires payment. The agent acts as if she had precommitted, without needing an actual binding precommitment.

A crucial interpretive point is that P-FDT should not simply condition on the actual observation `full` as if it were fixed independently of the policy. If it did, then upon seeing a full box it would calculate that two-boxing yields an extra \$1,000. Instead, P-FDT allows the counterfactual policy to change the probability of having seen `full` in the first place. The source expresses this idea when it says that FDT agents should entertain the hypothesis that, if their action were different, they might have made different observations.

This treatment of observations is not fully specified in the source, and I return to it below.

---

## 8. Example: mechanical blackmail

In the mechanical blackmail problem, a blackmailer runs a damaging program iff she predicts the agent will pay upon receiving the blackmail letter. If the agent receives the letter, paying costs \$1,000; refusing while the program runs costs \$1,000,000.

Let the inputs be:

\[
\mathcal X = \{\text{letter}, \text{no letter}\}.
\]

The relevant policies are roughly:

\[
\pi_{\text{pay}}(\text{letter}) = \text{pay},
\]

\[
\pi_{\text{refuse}}(\text{letter}) = \text{refuse}.
\]

If the blackmailer is a near-perfect predictor:

- under \(\pi_{\text{pay}}\), the blackmailer predicts payment, sends the letter, and the agent pays \$1,000;
- under \(\pi_{\text{refuse}}\), the blackmailer predicts refusal, does not send the letter, and the agent loses nothing.

So P-FDT chooses the refusing policy. If the agent nevertheless receives the letter because of predictor error, she still refuses. This may seem harsh, but it is precisely what makes her unattractive to blackmailers.

With an imperfect predictor, P-FDT compares expected losses. Suppose the blackmailer wrongly predicts payment with probability \(e\). If the policy is refuse, the expected loss is approximately

\[
e \cdot 1{,}000{,}000.
\]

If the policy is pay, the expected loss is approximately

\[
1{,}000.
\]

P-FDT refuses when

\[
e \cdot 1{,}000{,}000 < 1{,}000,
\]

that is, when \(e < 0.001\). It pays when the error probability is larger than that threshold. The source gives similar numerical illustrations.

The key point is that P-FDT does not ask, “Given that I already see the letter, should I pay?” in the ordinary evidential or causal sense. It asks, “Which policy should this decision procedure output, knowing that blackmailers predict this policy?” The actual input is then fed into the chosen policy.

---

## 9. Where policy selection may matter

The source says the difference between action-selection and policy-selection “only matters in multi-agent dilemmas so far as we can tell,” but it does not fully develop examples where the difference is decisive. This is one of the places where the source leaves P-FDT underdeveloped.

A reasonable way to see the difference is to imagine a predictor who rewards not a single action but an entire disposition. For example, suppose an agent may receive either red or green light. A predictor gives \$1,000,000 iff it predicts that the agent’s full policy satisfies:

\[
\pi(\text{red}) = C
\quad \text{and} \quad
\pi(\text{green}) = D.
\]

The agent actually sees red. An action-level theory that intervenes only on the action at red may fail to represent the fact that the reward depends on what the agent would do at green. P-FDT naturally represents this by evaluating whole policies. It chooses the policy with both required components and then executes \(C\) upon seeing red.

This example is my own, not taken from the source, but it illustrates the likely role of policy selection. In multi-agent settings, other agents often respond not merely to what you do now, but to what you would do in a range of circumstances: whether you can be trusted, bribed, blackmailed, or predicted. A policy node is a natural way to represent those dependencies.

---

## 10. Open questions and operational assumptions

P-FDT is elegant, but the source leaves several important questions open.

### 10.1 Constructing the dependency graph

The formal statement assumes a graph \(G\) saying how the world would change if the policy node were set to different policies. For CDT, Pearl’s causal framework gives a mature account of how causal structure can be learned from intervention and observation. For P-FDT, no comparable general account exists.

In practice, an agent must identify predictor-like dependencies. If another agent has modeled, simulated, or copied P-FDT, then the policy node should influence that other agent’s prediction. If a variable is merely statistically correlated, like the lesion, the policy node should not influence it.

This is a reasonable operational rule, but it is not yet a complete formal theory.

### 10.2 What to do with actual observations

The source’s action-level FDT responds to observations by changing which decision node is intervened upon, rather than by ordinary Bayesian conditioning. P-FDT responds by applying the chosen policy to the actual observation.

But this raises a delicate question: when evaluating policies, should the agent condition on the observation it actually has?

For predictor-dependent observations, I think the answer should usually be no. In transparent Newcomb, conditioning on seeing a full box would make two-boxing look locally better. P-FDT must instead allow the counterfactual policy to change the probability of having seen the full box. This gives P-FDT an updateless flavor: the policy is evaluated from a perspective that does not treat the actual observation as an immovable fixed fact when that observation is itself downstream of the policy.

For genuinely exogenous observations, conditioning may be harmless or necessary. If the agent learns a fact that affects payoffs but is not influenced by its policy, the model should incorporate that fact. The source does not draw this boundary precisely. My suggested operational interpretation is:

> Condition on observations only when they are known to be exogenous relative to the policy node; otherwise treat them as inputs to the policy and allow counterfactual policies to change their probabilities.

This is an additional assumption, not a theorem of the source.

### 10.3 Granularity of policies

The source does not specify how rich the input space \(\mathcal X\) should be. In sequential problems, inputs should probably be histories, not momentary observations. The policy space may then be enormous. Ideal P-FDT maximizes over all policies; bounded agents must approximate.

This is not unique to P-FDT. CDT and EDT also become intractable in large sequential environments. But P-FDT adds the further difficulty of modeling subjunctive dependencies across possible histories.

### 10.4 Counterpossible semantics

P-FDT requires evaluating scenarios in which a deterministic mathematical procedure has a different output than it actually has. The source acknowledges this as a drawback. Human reasoners can do something like this informally: we can ask what would follow if a conjecture were false, even if it is in fact true or false of logical necessity. But a full formal semantics for such counterpossibles remains unresolved.

---

## 11. Why P-FDT is attractive

Despite these open problems, P-FDT has considerable normative appeal.

First, it unifies several desirable behaviors. It one-boxes in Newcomb’s problem, smokes in the smoking lesion problem, pays in Parfit’s hitchhiker problem, one-boxes in transparent Newcomb when appropriate, and refuses blackmail when refusal makes blackmail unprofitable.

Second, it avoids the instability of CDT in predictor problems. CDT imagines changing the physical action while holding predictors fixed. That amounts to imagining perfect predictors making convenient errors. P-FDT instead imagines changing the policy and letting predictors change accordingly.

Third, it avoids EDT’s problem of managing the news. EDT conditions on actions and therefore treats every correlation as if it were something the action brings about evidentially. P-FDT breaks merely statistical correlations while preserving subjunctive ones.

Fourth, P-FDT acts as if it had made the best precommitment, without requiring actual precommitment mechanisms. It selects the best disposition on the fly.

Finally, P-FDT gives a unified account of single-agent and multi-agent reasoning. In games involving twins, predictors, voters, cooperators, blackmailers, or future selves, what matters is often not just the local act but the policy from which the act follows.

---

## Conclusion

P-FDT is the policy-selection version of functional decision theory suggested by Yudkowsky and Soares. Its central rule is to intervene on the output of one’s own policy-selection procedure, choose the policy whose subjunctive consequences are best, and then apply the actual input to that policy.

The theory can be summarized by the equation

\[
\pi^*
\in
\arg\max_{\pi \in \Pi}
\mathbb{E}[V \mid \operatorname{do}(\Pi_M=\pi)],
\]

with action

\[
a^* = \pi^*(x).
\]

Its distinctive feature is its treatment of dependencies. P-FDT preserves correlations that arise because predictors, copies, or other agents track the agent’s decision procedure. It discards merely evidential correlations, such as lesions or accidental statistical associations. In doing so, it aims to maximize actual utility in fair predictive and strategic environments.

The source leaves important matters unresolved, especially the construction of subjunctive dependency graphs, the treatment of actual observations, and the semantics of counterpossible interventions. Still, the policy-oriented reading gives a clear operational picture: rational choice is not merely the selection of an act, but the selection of the decision procedure—or policy—whose outputs one is willing to live with across all relevant possible inputs.

---

## Reference

Yudkowsky, E., and Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2. The policy-selection passage used as the primary source for P-FDT appears in footnote 16.