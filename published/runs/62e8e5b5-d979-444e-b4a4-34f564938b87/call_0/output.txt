# Policy Functional Decision Theory

## 1. Introduction: P-FDT as policy selection

Policy Functional Decision Theory, which I will call **P-FDT**, is the policy-centered version of the decision theory introduced by Yudkowsky and Soares in “Functional Decision Theory: A New Theory of Instrumental Rationality.” The paper’s main formal equations describe a theory that chooses an *action* by intervening on a logical variable representing the output of the agent’s decision procedure. But the passage that defines the version I am calling P-FDT appears in footnote 16:

> “the author’s preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a *policy* which maps inputs to actions, to which the agent then apply her inputs in order to select an action.”

The source calls the theory FDT; in this essay I use **P-FDT** for the policy-selection formulation. The central idea is this: a rational agent should treat her decision as the output of a fixed mathematical function, but the relevant output is not merely a single action in the present circumstance. It is a **policy**: a mapping from possible inputs, observations, or histories to actions. The agent asks:

> “Which policy, as the output of this very policy-selection procedure, would yield the best outcome?”

After selecting the best policy, the agent applies her actual input to that policy and performs the action it specifies.

This small change matters because many decision problems involve predictors, twins, negotiations, threats, or sequential choices where other agents or environmental processes depend not only on what the agent does now, but on what the agent *would do* in various possible situations. P-FDT evaluates the whole disposition, not merely the local act.

The source provides only a brief remark about this policy formulation, so much of the formal structure below is my reconstruction. I will try to distinguish the paper’s claims from my own operational assumptions.

---

## 2. Formal model of P-FDT

Let \(\mathcal X\) be a finite or countable set of possible observations, and let \(\mathcal A\) be a finite set of actions. A deterministic policy is a function

\[
\pi : \mathcal X \to \mathcal A.
\]

In sequential problems, one should replace \(\mathcal X\) with a set of observation histories \(h\), so that \(\pi\) maps histories to actions. For simplicity, I will usually write policies as functions of observations.

Let \(\Pi\) denote the set of policies under consideration. In an idealized theory, \(\Pi\) might be all functions from \(\mathcal X\) to \(\mathcal A\). In bounded applications, \(\Pi\) may be restricted to policies the agent can represent or implement.

The agent has a world-model \(M = (P, G)\), where:

- \(P\) is a probability distribution over relevant variables, including outcomes and possibly logical variables;
- \(G\) is a graph or structural model describing how changing certain variables changes others;
- \(V\) is the utility-bearing outcome variable, with utility \(U(V)\).

The crucial addition is a logical variable \(D_M\), representing the policy output by the agent’s policy-selection procedure when run on model \(M\). The values of \(D_M\) are policies \(\pi \in \Pi\).

P-FDT evaluates a policy \(\pi\) by an intervention:

\[
\operatorname{EU}_{\text{P-FDT}}(\pi; M)
=
\mathbb{E}\!\left[V \mid \operatorname{do}(D_M = \pi)\right].
\]

The agent then chooses a policy

\[
\pi^* \in \arg\max_{\pi \in \Pi}
\mathbb{E}\!\left[V \mid \operatorname{do}(D_M = \pi)\right].
\]

If the agent’s actual observation is \(x\), P-FDT prescribes the action

\[
a = \pi^*(x).
\]

This is the core P-FDT rule:

\[
\boxed{
\text{P-FDT}(M,x) = \pi^*(x),
\quad
\pi^* \in \arg\max_{\pi}
\mathbb{E}[V \mid \operatorname{do}(D_M=\pi)].
}
\]

The notation \(\operatorname{do}(D_M=\pi)\) is borrowed from causal modeling, but the intervention is not primarily physical. It is a *logical* or *subjunctive* intervention on the output of the agent’s policy-selection function. The graph \(G\) tells us which other variables change when that output changes.

For comparison, in a problem with actual observation \(x\):

- Evidential Decision Theory, EDT, chooses

\[
\arg\max_a \mathbb{E}[V \mid X=x, A=a].
\]

- Causal Decision Theory, CDT, chooses

\[
\arg\max_a \mathbb{E}[V \mid \operatorname{do}(A=a), X=x].
\]

- The action-based formulation of functional decision theory in the source chooses

\[
\arg\max_a \mathbb{E}[V \mid \operatorname{do}(D_{M,x}=a)].
\]

P-FDT instead chooses a policy first and then applies the actual observation:

\[
\pi^* = \arg\max_\pi \mathbb{E}[V \mid \operatorname{do}(D_M=\pi)],
\qquad
a = \pi^*(x).
\]

This distinction is subtle but important. EDT conditions on the action as news. CDT intervenes on the physical action. Action-based FDT intervenes on the output of the decision function for the current input. P-FDT intervenes on the output of a policy-selection function.

---

## 3. Observations, updatelessness, and unresolved choices

The footnote does not fully specify how P-FDT should use the actual observation. The source’s action-based FDT says that when an observation changes, the agent does not merely condition on the observation; rather, the agent changes which decision-function node she intervenes on. In the action-based equation, observing \(x\) leads to intervention on a node representing the decision procedure with input \(x\).

For P-FDT, the natural interpretation is that the agent selects a policy without treating the actual observation as an ordinary conditioning event that must be held fixed in every counterfactual. Instead, the observation is an input to the selected policy. If the observation itself is something that would have been different under a different policy, P-FDT should allow that difference in the hypothetical evaluation.

For example, if a predictor sends a blackmail letter only if it predicts the agent will pay, then the observation “I have received the letter” is policy-dependent. A policy that pays upon receiving the letter makes the letter more likely; a policy that refuses upon receiving the letter makes the letter less likely. P-FDT evaluates these policies globally, rather than simply conditioning on the letter as fixed news.

This creates an important open question. If the agent has already observed \(x\), should the model \(P\) be updated on \(x\)? My operational interpretation is:

1. If \(x\) is treated as evidence about variables that are not subjunctively downstream of the policy-selection node, then the agent may update \(P\) on \(x\).
2. If \(x\) is itself represented in \(G\) as downstream of \(D_M\), then P-FDT should not condition on \(x\) in a way that breaks the policy-dependence.
3. In sequential problems, the cleanest version of P-FDT selects a policy for the entire decision episode, and then executes that policy at each history.

This is my proposed way of making the footnote operational. The source itself does not give a complete rule for distinguishing legitimate evidential updating from improper conditioning on policy-dependent observations.

---

## 4. Subjunctive dependence and counterfactuals

P-FDT relies on the paper’s notion of **subjunctive dependence**. Two systems are subjunctively dependent on a mathematical function when their behavior tracks the output of that function. The paper’s analogy is two calculators computing the same sum. If one calculator outputs \(7336\) for \(6288+1048\), a well-functioning calculator elsewhere computing the same sum will also output \(7336\), even if there is no causal connection between them.

In decision problems, predictors, twins, simulators, and other agents can be subjunctively dependent on the agent’s decision procedure. A perfect predictor of the agent’s policy is, in effect, computing or modeling the same policy-selection function. Therefore, when P-FDT imagines a counterfactual policy, it must also imagine corresponding changes in the predictor’s prediction, the twin’s action, or the simulator’s output.

By contrast, a merely statistical correlation does not create subjunctive dependence. In the smoking lesion problem, smoking is correlated with cancer because a lesion causes both smoking and cancer. But the lesion does not compute the agent’s decision procedure. Therefore, changing the output of the agent’s policy-selection function does not, in the relevant subjunctive sense, change whether the lesion exists.

This is why P-FDT can one-box in Newcomb’s problem and smoke in the smoking lesion problem. In Newcomb’s problem, the predictor’s prediction depends on the agent’s decision procedure. In the smoking lesion problem, the lesion does not.

There is a philosophical cost. If the agent’s policy-selection function is deterministic, then it has only one actual output. To evaluate alternative policies, P-FDT must reason about counterpossibilities: “What would the world look like if this very function had a different output?” The source admits that we do not yet have a fully satisfactory formal semantics for such counterpossibles. In the graphical formulation, the theory assumes that the agent has a graph \(G\) telling her how changing the logical variable \(D_M\) would affect other variables. Constructing such a graph from observation is an open problem.

---

## 5. Example: Newcomb’s problem

In Newcomb’s problem, an agent faces two boxes:

- Box A contains \$1,000.
- Box B contains \$1,000,000 if a reliable predictor predicted the agent would take only Box B; otherwise Box B is empty.

Suppose the predictor is correct with probability \(0.99\).

In a simple one-shot version, the observation set can be trivial. A policy is just a fixed action: one-box or two-box. Let:

\[
\pi_1 = \text{one-box}, \qquad \pi_2 = \text{two-box}.
\]

The predictor subjunctively depends on \(D_M\). Therefore:

\[
\operatorname{do}(D_M=\pi_1)
\]

makes the predictor predict one-boxing with high probability, so Box B is probably full. The expected utility is approximately

\[
0.99 \cdot 1{,}000{,}000 + 0.01 \cdot 0 = 990{,}000.
\]

By contrast,

\[
\operatorname{do}(D_M=\pi_2)
\]

makes the predictor predict two-boxing with high probability, so Box B is probably empty. The expected utility is approximately

\[
0.99 \cdot 1{,}000 + 0.01 \cdot 1{,}001{,}000 = 11{,}000.
\]

P-FDT chooses \(\pi_1\), the one-boxing policy.

CDT chooses two-boxing because it intervenes only on the physical action and holds the predictor’s past prediction fixed. EDT chooses one-boxing because one-boxing is good evidence that the predictor filled the box. P-FDT chooses one-boxing for a reason closer to CDT than EDT: it evaluates a counterfactual intervention, but the intervention is on the policy-selection function rather than on the physical act alone.

---

## 6. Example: the smoking lesion problem

In the smoking lesion problem, smoking is correlated with cancer, but only because a lesion causes both a preference for smoking and cancer. Smoking itself does not cause cancer. Smoking gives the agent \$1,000 utility. Surviving cancer is worth \$1,000,000.

Let the policies be:

\[
\pi_S = \text{smoke}, \qquad \pi_R = \text{refrain}.
\]

The lesion is not subjunctively dependent on the agent’s policy-selection function. Therefore, in the P-FDT graph, the node \(D_M\) affects the action but not the lesion or cancer variable. Thus:

\[
P(\text{lesion} \mid \operatorname{do}(D_M=\pi_S))
=
P(\text{lesion} \mid \operatorname{do}(D_M=\pi_R)).
\]

Smoking adds \$1,000 utility without changing the probability of cancer. Therefore P-FDT chooses \(\pi_S\), the smoking policy.

This matches CDT’s prescription and avoids EDT’s mistake. EDT refrains because smoking is bad news: it is evidence that the agent has the lesion. P-FDT rejects this management of news. It asks what would happen if the policy-selection function output smoking rather than refraining, and since the lesion does not depend on that function, smoking is better.

---

## 7. Example: transparent Newcomb and Parfit’s hitchhiker

P-FDT becomes especially illuminating in problems where the agent may observe evidence that seems to make the optimal policy look locally irrational.

In the transparent Newcomb problem, both boxes are transparent. The predictor fills Box B iff she predicts the agent will leave Box A behind upon seeing both boxes full. Suppose the agent sees that both boxes are full.

A local calculation might say: “Box B is already full, so I should take both boxes.” EDT and CDT both two-box in this situation, assuming they condition on seeing the full box or intervene only on the physical action while holding the observation fixed.

P-FDT instead evaluates policies such as:

\[
\pi(\text{full}) = \text{one-box}, \quad
\pi(\text{empty}) = \text{two-box}.
\]

The predictor’s filling of Box B depends on the predicted policy, especially what the policy would do upon seeing a full box. If the predictor predicts \(\pi(\text{full})=\text{one-box}\), she fills Box B. If she predicts \(\pi(\text{full})=\text{two-box}\), she leaves Box B empty.

Using predictor accuracy \(0.99\), the policy that one-boxes upon seeing a full box has expected utility roughly

\[
0.99 \cdot 1{,}000{,}000 + 0.01 \cdot 1{,}000 = 990{,}010.
\]

The policy that two-boxes upon seeing a full box has expected utility roughly

\[
0.01 \cdot 1{,}001{,}000 + 0.99 \cdot 1{,}000 = 11{,}000.
\]

Therefore P-FDT selects the policy that one-boxes upon seeing a full box. When the agent actually sees a full box, she applies the policy and one-boxes.

This may appear strange: the agent sees that Box B is full but still leaves behind the visible \$1,000. P-FDT’s answer is that the agent should not imagine changing only the local physical action while holding the predictor’s accuracy fixed. If the agent’s policy-selection function were the kind that two-boxed upon seeing a full box, the predictor would probably not have filled Box B in the first place.

Parfit’s hitchhiker problem is structurally similar. An agent is stranded in a desert. A driver will rescue her only if the driver predicts that the agent will later pay \$1,000 after reaching the city. Once in the city, paying seems locally costly. CDT and EDT agents who reason locally cannot sincerely promise to pay, so the driver leaves them behind.

P-FDT selects the policy:

\[
\pi(\text{in city}) = \text{pay}.
\]

Because the driver can detect this policy, the agent is rescued. Upon reaching the city, the agent pays. P-FDT thereby achieves the high-utility outcome without requiring an actual binding precommitment device. It acts as it would have been optimal to precommit to act.

---

## 8. Why policies matter in multi-agent problems

The source says that the difference between action-selection and policy-selection “only matters in multi-agent dilemmas so far as we can tell.” The paper does not fully develop a multi-agent example of the policy formulation, so here I must extrapolate.

The general point is that other agents may respond not merely to the action one takes now, but to one’s entire pattern of behavior across possible inputs. A predictor, negotiator, coalition partner, or opponent may condition their behavior on your policy.

For instance, suppose a predictor will give an agent \$1,000,000 iff it predicts that the agent’s policy would refuse a small demand in a rare future branch. The branch may have low probability, but the policy’s behavior in that branch determines the predictor’s current action. A theory that evaluates only the action at the current observation may miss the fact that the agent’s counterfactual behavior in another branch is what produces the reward.

P-FDT handles such cases by intervening on the whole policy. If the predictor’s action depends on what the agent would do in multiple contingencies, those dependencies are represented by arrows from the policy node \(D_M\) to the predictor’s prediction and possibly to the agent’s future observations. P-FDT then chooses the policy that produces the best global outcome.

A related example is mechanical blackmail. A blackmailer runs a harmful program iff she predicts the agent will pay upon receiving a blackmail letter. If the agent’s policy is “pay if letter,” the blackmailer predicts payment and sends the letter. If the agent’s policy is “refuse if letter,” the blackmailer predicts refusal and does not send the letter. P-FDT chooses the refusing policy. If the agent nevertheless receives the letter, she refuses, because the selected policy says to refuse. The policy is valuable precisely because it makes blackmail unprofitable.

---

## 9. P-FDT and dominance

CDT often defends two-boxing by dominance: whatever the predictor did, taking both boxes gives \$1,000 more than taking only Box B. P-FDT rejects this dominance argument because CDT’s dominance notion holds fixed variables that P-FDT treats as subjunctively dependent on the decision function.

P-FDT has its own dominance principle. Policy \(\pi_1\) dominates policy \(\pi_2\) if, holding fixed all relevant subjunctive dependencies, changing the policy-selection output from \(\pi_2\) to \(\pi_1\) is never worse and sometimes better. In Newcomb’s problem, once the predictor’s dependence on the agent’s policy is held fixed in the P-FDT sense, two-boxing does not dominate one-boxing. The policy that two-boxes leads to an empty box with high probability.

This mirrors the source’s defense of FDT: every way of constructing hypotheticals generates its own notion of dominance, so dominance alone cannot decide between decision theories. The more important criterion is expected utility achieved in fair problems, where the environment rewards or predicts actions and policies rather than punishing agents for using a particular theory.

---

## 10. Open problems and additional assumptions

The footnote’s policy formulation is suggestive but incomplete. Several important questions remain unresolved.

First, the exact intervention node is not specified. The footnote says the theory “intervenes on the node FDT(-),” but it does not say whether the node takes the current observation as input. In my formulation, \(D_M\) outputs a policy from the agent’s model \(M\), and the actual observation is applied afterward. Another possible formulation would let the node take the current observation as an input but still output a policy rather than an action. The policy-selection version seems cleaner if \(D_M\) outputs a policy and then receives inputs, but the source does not settle this.

Second, the policy space is unspecified. Should the agent consider all functions from observations to actions? Only computable policies? Only policies the agent can explicitly represent? In bounded applications, this matters enormously. I have assumed an idealized finite or representable policy class.

Third, the treatment of actual observations needs care. If the agent has already observed \(x\), P-FDT must decide whether to update \(P\) on \(x\). My proposed rule is to update on observations only insofar as they are not modeled as downstream of the policy-selection node. When observations are policy-dependent, P-FDT should evaluate policies globally rather than conditioning them away. This is an operational interpretation, not a fully explicit rule in the source.

Fourth, the theory requires a graph \(G\) of subjunctive dependencies. The source admits that we do not yet know how to infer such dependencies from observation and experiment in the way Pearl’s causal calculus infers causal structure. In practice, a P-FDT agent must identify predictors, twins, simulations, and other systems that depend on its decision procedure, while excluding merely statistical correlates such as lesions.

Fifth, P-FDT relies on counterpossible reasoning. If the agent’s decision procedure is deterministic, alternative outputs are logically impossible. P-FDT nevertheless needs to reason about what would happen if the procedure had a different output. The source treats this as a technical problem rather than a fatal objection, but a complete formal semantics is still lacking.

Despite these gaps, the policy formulation is attractive because it expresses the core functional decision-theoretic idea at the right level of generality. Agents often do not merely choose isolated actions; they choose dispositions, plans, and responses.

---

## 11. Conclusion

Policy Functional Decision Theory evaluates decisions by asking which policy would be best if it were the output of the agent’s own policy-selection procedure. Formally, P-FDT chooses

\[
\pi^* \in \arg\max_{\pi}
\mathbb{E}[V \mid \operatorname{do}(D_M=\pi)],
\]

then performs \(\pi^*(x)\) for the actual observation \(x\). It preserves the expected-utility framework of EDT, CDT, and action-based FDT, but changes the object of intervention: not an action, not merely an action given the current observation, but a policy mapping inputs to actions.

This allows P-FDT to handle predictor problems, transparent Newcomb cases, Parfit’s hitchhiker, blackmail, and multi-agent situations where other actors respond to an agent’s entire pattern of behavior. It one-boxes in Newcomb’s problem, smokes in the smoking lesion problem, pays in Parfit’s hitchhiker problem, and refuses blackmail when refusal makes blackmail unprofitable.

The theory is not complete. It needs a better account of subjunctive-dependence graphs, counterpossible reasoning, policy spaces, and observation update. But its central prescription is clear and powerful: choose the policy that this very policy-selection procedure should output, then act according to that policy.

---

### Reference

Yudkowsky, Eliezer, and Nate Soares. “Functional Decision Theory: A New Theory of Instrumental Rationality.” arXiv:1710.05060v2.