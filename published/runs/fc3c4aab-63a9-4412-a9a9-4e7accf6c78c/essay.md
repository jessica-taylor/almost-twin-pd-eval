# Policy Functional Decision Theory: Choosing the Best Output of a Policy-Selection Function

Policy functional decision theory, which I will call **P-FDT**, is the policy-selection version of the decision theory introduced by Yudkowsky and Soares as “functional decision theory” (FDT). In the main text of their paper, FDT is usually presented as choosing an *action* by intervening on a variable representing the output of the agent’s decision procedure given her current observations. But footnote 16 gives a more preferred formulation:

> “the author’s preferred formulation of FDT actually intervenes on the node \(\mathrm{FDT}(-)\) to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action.”

The footnote adds that this distinction “only matters in multi-agent dilemmas so far as we can tell.” That qualification is important. The source does not develop a full formal theory of this policy-selection variant. What follows is therefore an interpretation: I take the footnote as the defining clue, supply explicit mathematical machinery where the source is silent, and mark places where I am extending rather than merely reporting the source.

The central idea of P-FDT is this: a rational agent should treat her decision as the output of a fixed mathematical *policy-selection function*. Instead of asking, “What should I do now?” she asks:

> Which policy should this very policy-selection procedure output?

She then applies the chosen policy to her actual observations to obtain an action.

---

## 1. Actions, observations, and policies

Let \(\mathcal X\) be a finite or countable set of possible observation histories, and let \(\mathcal A\) be a finite set of actions. A **policy** is a function

\[
\pi : \mathcal X \to \mathcal A.
\]

Let \(\Pi = \mathcal A^{\mathcal X}\) be the set of available policies.

In an ordinary decision problem, the agent receives some observation \(x \in \mathcal X\) and then chooses an action \(a \in \mathcal A\). A policy-level theory does not directly compare actions. It compares policies. Once a policy \(\pi\) has been selected, the actual action is

\[
a = \pi(x).
\]

This is the structural difference between P-FDT and action-level theories.

For comparison:

- **Evidential decision theory (EDT)** asks which action would be best news:
  \[
  a_{\mathrm{EDT}} \in \arg\max_{a \in \mathcal A}
  \mathbb{E}[V \mid X=x, A=a].
  \]

- **Causal decision theory (CDT)** asks which action causally produces the best outcome:
  \[
  a_{\mathrm{CDT}} \in \arg\max_{a \in \mathcal A}
  \mathbb{E}[V \mid \operatorname{do}(A=a), X=x].
  \]

- The action-level version of **FDT** in the source asks which output of the decision procedure, given the current observation, yields the best outcome:
  \[
  a_{\mathrm{FDT}} \in \arg\max_{a \in \mathcal A}
  \mathbb{E}[V \mid \operatorname{do}(\mathrm{FDT}(M,x)=a)].
  \]

P-FDT replaces the action-output variable with a policy-output variable. If \(M\) is the agent’s model of the world and \(\mathrm{Pol}(M)\) is the variable representing the policy output by her decision procedure, then the core prescription is:

\[
\pi_{\mathrm{P-FDT}}
\in
\arg\max_{\pi \in \Pi}
\mathbb{E}[V \mid \operatorname{do}(\mathrm{Pol}(M)=\pi)].
\]

The agent then acts by evaluating the selected policy at her actual input:

\[
a_{\mathrm{P-FDT}} = \pi_{\mathrm{P-FDT}}(x).
\]

If the agent has some purely exogenous evidence \(e\) that is not itself downstream of her policy selection, one may condition on it:

\[
\pi_{\mathrm{P-FDT}}
\in
\arg\max_{\pi \in \Pi}
\mathbb{E}[V \mid \operatorname{do}(\mathrm{Pol}(M)=\pi), E=e].
\]

But if the current observation \(x\) is itself something that predictors might have caused based on their predictions of the agent’s policy, then P-FDT should not simply condition on \(x\). Instead, \(X\) should be represented inside the model as a variable that may change under the intervention \(\operatorname{do}(\mathrm{Pol}=\pi)\). This is an operational interpretation of the source’s claim that FDT agents “entertain the hypothesis that, if their action were different, they might have made different observations.”

---

## 2. Models, interventions, and subjunctive dependence

Like the source’s FDT, P-FDT requires a world-model \(M=(P,G)\):

- \(P\) is a probability distribution over relevant variables.
- \(G\) is a graph or dependency structure describing how changing one variable affects others.

The variables should include at least:

- \(\mathrm{Pol}\): the policy selected by the agent’s decision procedure;
- \(X\): the observation or input the agent receives;
- \(A\): the action performed;
- \(V\): utility.

A natural structural equation is

\[
A = \mathrm{Pol}(X).
\]

That is, once the policy variable is set, the action variable is determined by applying that policy to the observation variable.

The intervention \(\operatorname{do}(\mathrm{Pol}=\pi)\) sets the policy variable to \(\pi\). The expected utility of \(\pi\) is computed by propagating this intervention through the dependency graph \(G\). Variables that subjunctively depend on the policy are updated; variables that do not are held fixed.

The source’s key philosophical notion is **subjunctive dependence**. Two systems are subjunctively dependent when their behavior depends on the same mathematical function or computation. The classic example is two reliable calculators computing the same sum. Their outputs are not necessarily causally connected, but if one outputs \(7336\) for \(6288+1048\), the other will too, insofar as both are functioning correctly.

P-FDT treats predictors, psychological twins, simulations, and accurate models as subjunctively dependent on the agent’s decision procedure when appropriate. It does not treat merely statistical correlations as subjunctive dependencies. A lesion that causes both a desire to smoke and lung cancer is not computing the agent’s decision procedure. Therefore, intervening on the agent’s policy does not change the lesion.

This gives P-FDT its diagnostic slogan:

> EDT respects too many correlations; CDT respects too few; P-FDT respects the subjunctive correlations that matter.

More precisely:

- EDT conditions on the action and thereby preserves all correlations between action and environment.
- CDT intervenes on the physical action and thereby severs correlations not caused by that action.
- P-FDT intervenes on the policy-output variable and preserves correlations with anything that computes, predicts, simulates, or otherwise subjunctively depends on that policy.

The intervention is counterpossible in the same way the source describes for FDT. If the actual P-FDT procedure outputs one policy, evaluating another policy requires imagining that this very procedure had a different output. The source admits that we do not yet have a fully general formal account of such counterpossible reasoning. P-FDT inherits this open problem. Operationally, we must assume that the agent can supply, at least approximately, a graph \(G\) saying which facts would change if her policy-selection procedure had a different output.

---

## 3. P-FDT in Newcomb’s problem

In standard Newcomb’s problem, an agent faces box A containing \$1,000 and opaque box B containing either \$1,000,000 or nothing. A reliable predictor filled box B iff she predicted the agent would one-box.

Here the observation set can be a singleton, so policies and actions coincide. Let

\[
\pi_1 = \text{one-box}, \qquad \pi_2 = \text{two-box}.
\]

The predictor is correct with probability \(0.99\). Under the intervention \(\operatorname{do}(\mathrm{Pol}=\pi_1)\), the predictor almost certainly predicts one-boxing and fills the box. The expected utility is

\[
\mathbb{E}[V \mid \operatorname{do}(\mathrm{Pol}=\pi_1)]
=
0.99 \cdot 1{,}000{,}000
+
0.01 \cdot 0
=
990{,}000.
\]

Under \(\operatorname{do}(\mathrm{Pol}=\pi_2)\), the predictor almost certainly predicts two-boxing and leaves box B empty:

\[
\mathbb{E}[V \mid \operatorname{do}(\mathrm{Pol}=\pi_2)]
=
0.99 \cdot 1{,}000
+
0.01 \cdot 1{,}001{,}000
=
11{,}000.
\]

P-FDT therefore selects the one-boxing policy. The reasoning is not “I cause the past to change.” It is: “If this very policy-selection procedure outputs a one-boxing policy, then predictors of this procedure almost certainly filled the box. If it outputs a two-boxing policy, they almost certainly did not.”

This matches the source’s action-level FDT prescription, as expected in a one-observation problem.

---

## 4. P-FDT in the smoking lesion problem

In the smoking lesion problem, smoking is correlated with cancer only because a lesion causes both smoking and cancer. Smoking itself does not cause cancer. Smoking gives the agent \$1,000 of utility.

Let \(L\) be the lesion variable. The crucial modeling claim is that \(L\) is not downstream of the agent’s policy-selection variable. The lesion does not predict the agent’s policy; it merely causes a preference for smoking and, independently, cancer.

Thus, under either intervention,

\[
P(L \mid \operatorname{do}(\mathrm{Pol}=\pi_{\text{smoke}}))
=
P(L \mid \operatorname{do}(\mathrm{Pol}=\pi_{\text{refrain}}))
=
P(L).
\]

Smoking adds \$1,000 utility without changing the probability of cancer. Therefore,

\[
\mathbb{E}[V \mid \operatorname{do}(\mathrm{Pol}=\pi_{\text{smoke}})]
>
\mathbb{E}[V \mid \operatorname{do}(\mathrm{Pol}=\pi_{\text{refrain}})].
\]

P-FDT smokes.

This is the same broad result as the source’s FDT treatment. The source’s formal model introduces uncertainty about the agent’s utility function because the lesion causes the agent to like smoking. That complication does not change the essential point: P-FDT does not treat the lesion as something the agent’s policy can counterfactually control.

---

## 5. P-FDT in transparent Newcomb and Parfit’s hitchhiker

P-FDT becomes more interesting when observations matter. In the transparent Newcomb problem, the agent sees whether box B is full before choosing. The predictor filled box B iff she predicted the agent would one-box upon seeing that both boxes are full.

Let

\[
\mathcal X = \{\text{full}, \text{empty}\}.
\]

A natural candidate policy is

\[
\pi^*(\text{full}) = \text{one-box}, \qquad
\pi^*(\text{empty}) = \text{two-box}.
\]

The predictor fills the box iff she predicts \(\pi^*(\text{full})=\text{one-box}\).

If P-FDT intervenes to set \(\mathrm{Pol}=\pi^*\), then with probability \(0.99\) the predictor is accurate, the box is full, the agent observes “full,” and one-boxes, receiving \$1,000,000. With probability \(0.01\), the predictor is inaccurate, the box is empty, the agent observes “empty,” and two-boxes, receiving \$1,000. The expected utility is approximately

\[
0.99 \cdot 1{,}000{,}000
+
0.01 \cdot 1{,}000
=
990{,}010.
\]

If instead the policy two-boxes upon seeing a full box, the predictor almost certainly leaves the box empty. The expected utility is approximately

\[
0.99 \cdot 1{,}000
+
0.01 \cdot 1{,}001{,}000
=
11{,}000.
\]

So P-FDT selects the policy of one-boxing upon seeing a full box. When the agent actually sees a full box, she one-boxes.

This may seem strange: the agent sees that box B is full, yet she refuses the extra \$1,000. But P-FDT does not condition on the observation as if it were fixed independently of the policy. It treats the observation as something that would likely have been different if the selected policy had been different. If the policy two-boxed upon seeing full boxes, the predictor would probably not have filled the box, and the agent would probably not be seeing a full box.

This is precisely the reasoning that makes P-FDT pay in Parfit’s hitchhiker problem. The driver helps the agent iff she predicts the agent will pay after reaching the city. P-FDT selects the policy “pay if rescued.” When rescued, it pays. The payment is locally costly, but the policy as a whole is what secures rescue.

---

## 6. Why policy selection can matter

The source says the policy/action distinction “only matters in multi-agent dilemmas so far as we can tell.” It does not give a worked example. I therefore offer an illustrative case of my own, not a claim drawn directly from the source.

Suppose an agent faces a two-stage problem.

At time \(t_0\), a predictor predicts whether the agent’s P-FDT policy-selection node will output the policy

\[
\pi_{\text{pay}}(\text{asked}) = \text{pay } \$1{,}000.
\]

If the predictor predicts \(\pi_{\text{pay}}\), she gives the agent \$1,000,000. At time \(t_1\), the predictor asks for \$1,000. There is no further enforcement and no future prediction.

If the predictor is perfect, P-FDT compares:

- Policy \(\pi_{\text{pay}}\): receive \$1,000,000, then pay \$1,000. Utility: \$999,000.
- Policy \(\pi_{\text{refuse}}\): receive nothing and pay nothing. Utility: \$0.

P-FDT selects \(\pi_{\text{pay}}\). When asked, it pays.

A theory that re-optimizes only the local action at \(t_1\), while treating the earlier prediction as already fixed, may refuse to pay. P-FDT avoids this by selecting the policy at the point where the predictor depends on it.

In multi-agent settings, the same structure appears when another agent’s strategy depends not merely on what one does at one information set, but on one’s overall policy. For example, in cooperative games with several agents who use similar reasoning, an agent may need to select a policy that specifies behavior across several possible future observations. Other agents or predictors may depend on the entire policy. If each agent merely re-optimizes locally at each observation, the resulting behavior can fail to capture those policy-level dependencies.

The source does not spell this out in detail, so the above should be understood as an operational extension of the footnote.

---

## 7. How P-FDT treats dependencies and counterfactuals

P-FDT evaluates a policy by asking what the world would look like if the agent’s policy-selection procedure output that policy. This requires a counterfactual or counterpossible judgment.

The relevant counterfactual is not:

> What if I used a different decision algorithm?

Rather, it is:

> What if this very policy-selection algorithm had a different output?

This is why the source’s discussion of subjunctive dependence is essential. If a predictor contains an accurate model of the agent’s decision procedure, then the predictor’s behavior subjunctively depends on the policy output. If the policy output were different, the predictor’s prediction would be different. If a twin runs the same decision procedure, the twin’s behavior subjunctively depends on the same policy output. If a lesion merely causes preferences and disease, it does not subjunctively depend on the policy output.

Thus P-FDT’s counterfactuals preserve:

- logical entailments from the policy to its outputs;
- predictions of the policy by reliable predictors;
- behavior of copies, twins, or simulations running the same policy;
- causal consequences of the actions produced by the policy;
- observations that predictors may supply based on the policy.

They hold fixed:

- merely statistical common causes;
- lesions or predispositions that do not compute the policy;
- exogenous facts not downstream of the policy.

The hardest part is knowing which variables belong in which category. The source explicitly says that learning how to infer subjunctive dependency structure from observation is a major open problem for FDT. P-FDT inherits that problem. In practice, one must use modeling judgment. A reasonable rule is: if a variable is produced by predicting, simulating, or logically computing the agent’s policy, draw an arrow from the policy variable to that variable. If it is produced by an independent common cause, do not.

---

## 8. Open questions left by the footnote

The policy-selection passage is too brief to settle several questions.

### 8.1 Where is the policy selected?

P-FDT must decide at which point in a dynamic problem the policy node is located. My proposed operational rule is:

> Place the policy node at the earliest point where the agent’s decision procedure is subjunctively depended upon by predictors, other agents, or later versions of the agent whose behavior matters to the problem.

If no earlier predictor depends on the policy, one may select policies locally. But if an earlier predictor or another agent depends on the whole policy, P-FDT should choose the policy at that earlier point and then follow it.

### 8.2 What should be conditioned on?

The source’s FDT does not respond to observations by ordinary conditioning; it changes the intervention node. P-FDT is similar but needs a rule.

I propose:

- Condition on evidence that is genuinely exogenous relative to the policy variable.
- Do not condition away observations that are themselves downstream of the policy variable.
- Represent such observations as variables inside the model, allowing them to change under \(\operatorname{do}(\mathrm{Pol}=\pi)\).

This preserves P-FDT’s ability to say, “If this policy had been different, I might have seen different things.”

### 8.3 How do multiple agents share a policy variable?

If two agents run the same P-FDT procedure on symmetric inputs, one can model them as sharing a common policy variable. If their inputs differ, matters are more subtle. A policy can map different inputs to different actions. If each agent selects a policy after learning an asymmetrical role, they may not select the same policy unless the model represents policy selection as occurring before that role is known.

This is not resolved by the source. In symmetric problems, a shared policy variable is natural. In asymmetric problems, P-FDT’s prescription depends on how the model represents indexical information and logical dependence between agents.

### 8.4 How are policies compared when they differ only off-path?

Two policies may agree at the agent’s actual observation but differ elsewhere. If the elsewhere is not subjunctively relevant, P-FDT is indifferent. If predictors or other agents depend on the off-path behavior, P-FDT may prefer one policy over the other even though the actual action is the same. This is a feature, not a bug: it is how P-FDT captures dependencies on dispositions and commitments.

---

## 9. Conclusion

Policy functional decision theory, P-FDT, is the policy-level formulation of functional decision theory. Its normative principle is to choose the best output of a fixed policy-selection function. Formally, it intervenes on a variable representing the policy produced by the agent’s decision procedure, computes expected utility under that intervention, and then applies the selected policy to the actual observation.

In simple one-shot problems, P-FDT agrees with the source’s action-level FDT: it one-boxes in Newcomb’s problem and smokes in the smoking lesion problem. In observation-dependent problems such as transparent Newcomb and Parfit’s hitchhiker, it selects policies that perform well globally rather than optimizing myopically after each observation. In multi-agent or predictor-rich problems, the policy-level formulation is likely to matter most, because other agents may depend on the agent’s entire strategy rather than on a single isolated action.

The source leaves the formal details underdeveloped. It does not specify exactly how P-FDT should handle conditioning, dynamic policy selection, or asymmetric multi-agent information. The operational rules proposed here—select policies early where subjunctive dependencies arise, condition only on exogenous evidence, and represent policy-dependent observations as downstream variables—are an attempt to make the footnote usable.

P-FDT’s deepest difficulty is the same one facing the source’s FDT: we need a principled way to represent subjunctive dependence. Once such a representation is available, P-FDT gives a clear prescription: choose the policy that, if output by this very decision procedure, would yield the best expected world.

---

### References

Gibbard, A., and Harper, W. L. (1978). “Counterfactuals and Two Kinds of Expected Utility.” In *Foundations and Applications of Decision Theory*.

Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.

Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.

Yudkowsky, E., and Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060.