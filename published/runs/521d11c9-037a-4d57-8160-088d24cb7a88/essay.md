# P-FDT: Policy Functional Decision Theory

## 1. What P-FDT is meant to do

Policy functional decision theory, or **P-FDT**, is a decision theory that tells an agent to choose the best *policy*—a mapping from inputs or observations to actions—rather than choosing only a local physical action. The core idea is that a rational agent should treat her decision procedure as a fixed mathematical object and ask:

> Which policy, if output by this very decision procedure, would lead to the best outcome when applied to my inputs?

This contrasts with the two more familiar theories:

- **Evidential decision theory** asks: “Which action would be the best news to learn I had taken?”
- **Causal decision theory** asks: “Which physical action would causally produce the best outcome?”

P-FDT instead asks which *complete contingent plan* should be selected by the agent’s decision algorithm.

The primary source for this policy-oriented version is a brief passage in footnote 16 of Yudkowsky and Soares’s paper on functional decision theory:

> “the author's preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action.”

The same footnote adds that the distinction “only matters in multi-agent dilemmas so far as we can tell,” and the main paper therefore sets it aside. Because the source gives only this short policy-selection passage, much of the formal machinery below is my reconstruction from the paper’s action-based version of functional decision theory, its graphical models, and its discussion of subjunctive dependence. Where I add assumptions, I will say so.

---

## 2. From actions to policies

Let \(\mathcal X\) be a set of possible inputs, observations, or observation histories, and let \(\mathcal A\) be a set of actions. A **policy** is a function

\[
\pi : \mathcal X \to \mathcal A.
\]

In a sequential setting, \(\mathcal X\) may be the set of histories so far, so a policy tells the agent what to do at every possible decision point.

The agent has a world-model \((P,G)\):

- \(P\) is a probability distribution over relevant variables: exogenous states, observations, actions, predictions made by others, outcomes, and utility.
- \(G\) is a graph or structural model describing how those variables depend on one another. In P-FDT, \(G\) must encode not only causal dependence but also what the source calls **subjunctive dependence**: dependence on the output of a mathematical decision procedure.

Let

\[
\Phi_{P,G}
\]

be a logical variable representing the policy selected by P-FDT when run on the model \((P,G)\). The variable \(\Phi_{P,G}\) is not merely a variable for the physical action. It represents the output of the agent’s policy-selection procedure.

P-FDT then evaluates candidate policies by intervening on this variable. The value of a policy \(\pi\) is

\[
\operatorname{Val}_{P,G}(\pi)
=
\mathbb E_P\!\left[V \mid do(\Phi_{P,G}=\pi)\right],
\]

where \(V\) is utility and \(do(\cdot)\) is an intervention operator, borrowed loosely from Pearl-style causal modeling. P-FDT chooses a policy

\[
\pi^*
\in
\arg\max_{\pi \in \Pi}
\mathbb E_P\!\left[V \mid do(\Phi_{P,G}=\pi)\right],
\]

where \(\Pi\) is the set of feasible policies. If the agent’s actual input is \(x\), she then executes

\[
a^* = \pi^*(x).
\]

That is the basic P-FDT recipe:

1. Represent the decision problem with a model \((P,G)\).
2. Include a variable \(\Phi_{P,G}\) for the output of the P-FDT policy-selection procedure.
3. For each candidate policy \(\pi\), imagine the world that results if the policy-selection procedure outputs \(\pi\).
4. Choose the policy with highest expected utility under that intervention.
5. Apply the chosen policy to your actual input.

---

## 3. How P-FDT differs from EDT and CDT

For comparison, we can write simplified versions of the rival theories.

EDT chooses an action by conditionalization:

\[
\mathrm{EDT}(P,x)
=
\arg\max_{a \in \mathcal A}
\mathbb E_P[V \mid X=x, A=a].
\]

It preserves all statistical correlations between action and outcome. This causes trouble when an action is merely evidence of something bad, as in the smoking lesion problem.

CDT chooses an action by causal intervention:

\[
\mathrm{CDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb E_P[V \mid do(A=a), X=x].
\]

It preserves causal downstream effects of the action but severs correlations caused by predictors, twins, or simulations. This causes trouble in Newcomb-like problems.

The main paper’s action-based version of functional decision theory intervenes instead on a logical variable representing the output of the decision procedure given the current input:

\[
\mathrm{FDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb E_P[V \mid do(F_{P,G,x}=a)],
\]

where \(F_{P,G,x}\) represents the output of the decision procedure on input \(x\).

P-FDT generalizes this by intervening on the policy itself:

\[
\mathrm{P\text{-}FDT}(P,G)
=
\arg\max_{\pi \in \Pi}
\mathbb E_P[V \mid do(\Phi_{P,G}=\pi)].
\]

The actual action is then obtained by feeding the actual observation into the selected policy.

The difference matters because a predictor may care about the agent’s whole policy, not merely the action she happens to take now. In single-agent problems, action-based functional decision theory can often emulate P-FDT by using observation-indexed decision nodes. But in multi-agent or strategically structured problems, the object being predicted may be the agent’s entire mapping from inputs to actions.

---

## 4. Subjunctive dependence and counterfactuals

P-FDT’s counterfactuals are not ordinary causal counterfactuals. The source’s central concept is **subjunctive dependence**.

Two physical systems subjunctively depend on a mathematical function if, were that function to have a different output, both systems would relevantly change their behavior, assuming no errors. The source uses calculators as an analogy: two correctly functioning calculators computing the same sum will give the same answer, even if they are causally independent. If one outputs \(7336\), we infer the other would also output \(7336\). They are not causally connected, but they are linked by the arithmetic function they compute.

Similarly, if a predictor accurately models the agent’s decision procedure, then the predictor’s prediction subjunctively depends on the output of that procedure. If the procedure outputs one-boxing, the predictor predicts one-boxing; if it outputs two-boxing, the predictor predicts two-boxing.

P-FDT’s interventions preserve these subjunctive dependencies. When P-FDT imagines a different policy, it also imagines corresponding changes in:

- the agent’s own actions at relevant inputs;
- predictors’ predictions of those actions;
- simulations or copies of the agent;
- other agents who reason symmetrically or model the agent’s policy;
- observations that are themselves produced by predictors responding to the policy.

It does **not** imagine changing merely statistical correlations. A lesion that causes both a preference for smoking and cancer does not subjunctively depend on the agent’s decision procedure. Therefore, P-FDT does not imagine that choosing a different policy changes the lesion.

This is why P-FDT can one-box in Newcomb’s problem and smoke in the smoking lesion problem. Predictor-like dependencies are respected; lesion-like correlations are not.

---

## 5. P-FDT in Newcomb’s problem

In Newcomb’s problem, an agent can take both boxes or only the opaque box B. A reliable predictor filled B iff she predicted the agent would one-box.

In P-FDT, the policy space can be simple because there is no meaningful observation:

\[
\pi_1 = \text{one-box}, \qquad \pi_2 = \text{two-box}.
\]

The model contains a policy-selection variable \(\Phi_{P,G}\), a predictor variable, a box-contents variable, and a utility variable. The graph has an arrow from \(\Phi_{P,G}\) to the predictor’s prediction, because the predictor is modeling the agent’s decision procedure. It also has an arrow from \(\Phi_{P,G}\) to the agent’s action.

Suppose the predictor is \(99\%\) accurate. Then

\[
P(\text{Box B full} \mid do(\Phi_{P,G}=\pi_1)) = 0.99,
\]

while

\[
P(\text{Box B full} \mid do(\Phi_{P,G}=\pi_2)) = 0.01.
\]

The utilities are:

\[
U(\text{one-box}, \text{full}) = 1{,}000{,}000,
\]

\[
U(\text{one-box}, \text{empty}) = 0,
\]

\[
U(\text{two-box}, \text{full}) = 1{,}001{,}000,
\]

\[
U(\text{two-box}, \text{empty}) = 1{,}000.
\]

So the policy values are

\[
\operatorname{Val}(\pi_1)
=
0.99 \cdot 1{,}000{,}000
+
0.01 \cdot 0
=
990{,}000,
\]

and

\[
\operatorname{Val}(\pi_2)
=
0.01 \cdot 1{,}001{,}000
+
0.99 \cdot 1{,}000
=
11{,}000.
\]

P-FDT selects \(\pi_1\), the one-boxing policy.

The reasoning is not “my physical action reaches back in time and causes the predictor to fill the box.” Rather: if this very decision procedure outputs a one-boxing policy, then a sufficiently accurate predictor will have predicted one-boxing and filled the box. If it outputs a two-boxing policy, the predictor will have predicted two-boxing and left the box empty. The first counterpossible world is better.

---

## 6. P-FDT in the smoking lesion problem

In the smoking lesion problem, smoking is correlated with cancer, but only because a lesion causes both a preference for smoking and cancer. Smoking itself does not cause cancer.

Here P-FDT’s graph contains a lesion variable \(L\), a cancer variable \(C\), an action variable \(A\), and a policy-selection variable \(\Phi_{P,G}\). Crucially, there is an arrow from \(L\) to \(C\), and perhaps from \(L\) to the agent’s preferences or action, but there is no arrow from \(\Phi_{P,G}\) to \(L\) or \(C\). The lesion does not compute or predict the agent’s policy.

Thus, for policies \(\pi_S = \text{smoke}\) and \(\pi_R = \text{refrain}\),

\[
P(C \mid do(\Phi_{P,G}=\pi_S))
=
P(C \mid do(\Phi_{P,G}=\pi_R)).
\]

Changing the policy does not change the probability of cancer. Smoking gives a direct utility gain, say \(1{,}000\), while refraining does not. Therefore P-FDT chooses the smoking policy.

The source gives a more careful model in which the lesion also affects which utility function the agent has. Even there, the key structural fact is the same: the policy-selection node does not control the lesion. P-FDT therefore avoids EDT’s mistake of treating smoking as bad news about cancer.

---

## 7. P-FDT in the transparent Newcomb problem and Parfit’s hitchhiker

The policy formulation becomes especially natural in problems where the agent receives an observation that was itself produced by a predictor.

In the transparent Newcomb problem, the agent sees both boxes. The predictor filled the opaque box iff she predicted the agent would one-box upon seeing that both boxes are full.

Here the relevant policies are mappings from observations to actions. Two candidate policies are:

\[
\pi^+( \text{full}) = \text{one-box},
\qquad
\pi^+(\text{empty}) = \text{two-box},
\]

and

\[
\pi^-(\text{full}) = \text{two-box},
\qquad
\pi^-(\text{empty}) = \text{two-box}.
\]

The predictor’s prediction depends on the policy, not merely on the action eventually taken after the observation. If the agent uses \(\pi^+\), the predictor usually predicts one-boxing upon seeing a full box and therefore fills the box. If the agent uses \(\pi^-\), the predictor usually predicts two-boxing and leaves the box empty.

With \(99\%\) accuracy:

\[
\operatorname{Val}(\pi^+)
=
0.99 \cdot 1{,}000{,}000
+
0.01 \cdot 1{,}000
=
990{,}010,
\]

while

\[
\operatorname{Val}(\pi^-)
=
0.99 \cdot 1{,}000
+
0.01 \cdot 1{,}001{,}000
=
11{,}000.
\]

P-FDT selects \(\pi^+\). If the agent actually sees a full box, she executes

\[
\pi^+(\text{full}) = \text{one-box}.
\]

This is the same structure as Parfit’s hitchhiker problem. A driver will save the agent iff she predicts that the agent will later pay. Once in the city, EDT and CDT both say not to pay, because the ride is already obtained. But P-FDT chooses the policy “pay if in the city,” because that policy is what causes the driver to help. When the agent is in the city, she applies the policy and pays.

The important point is that P-FDT does not ask, “Given that I already see the full box, which physical action is best?” That question invites the answer “two-box.” P-FDT asks, “Which policy should this decision procedure output, knowing that predictors respond to that policy?” The answer is the policy that one-boxes when seeing a full box.

---

## 8. Observations: what P-FDT updates on

The source leaves some ambiguity about how to handle observations. In the action-based formulation, the paper says that functional decision theory responds to observation not by simply conditioning on it, but by changing which decision-function node is intervened upon. In the policy formulation, I take the cleaner interpretation to be this:

> P-FDT chooses a policy from a global standpoint, then applies that policy to the actual input. It does not condition away observations that are themselves downstream of the policy.

This is my operational elaboration, not fully spelled out in the footnote.

If an observation is genuinely exogenous—say, a weather report unrelated to predictors of the agent—then P-FDT may condition on it. More generally, if \(E\) is evidence known not to be subjunctively downstream of \(\Phi_{P,G}\), we can use

\[
\pi^*
\in
\arg\max_{\pi}
\mathbb E_P[V \mid do(\Phi_{P,G}=\pi), E=e].
\]

But if the observation is produced by a predictor’s response to the agent’s policy—such as receiving a blackmail letter, seeing a full box, or being offered a ride—then conditioning on that observation can destroy the very dependency P-FDT is supposed to respect.

For example, if one conditions on “I see a full box,” then two-boxing can appear locally superior because the box is already full. But P-FDT says that seeing the full box is itself evidence that the selected policy is the sort the predictor expected. The policy evaluation should not hold that observation fixed in a way that severs its dependence on the policy.

This gives P-FDT an updateless flavor. The agent updates on evidence only insofar as that evidence is not itself a consequence of the policy being evaluated. The agent then chooses the best policy and executes its output at the current input.

---

## 9. Blackmail and predictor-generated observations

The source’s blackmail examples illustrate the same principle.

Suppose a predictor sends an agent a demand letter iff it predicts that the agent’s policy will pay upon receiving the letter. If the agent’s policy is “pay if I receive the letter,” the predictor sends the letter, and the agent loses money. If the agent’s policy is “refuse if I receive the letter,” the predictor does not send the letter, except perhaps with small probability of error.

P-FDT evaluates the policies before conditioning on the receipt of the letter as if it were ordinary evidence. The receipt of the letter is not an exogenous fact; it is a consequence of the predictor’s model of the policy. Therefore, the policy value includes the probability of receiving the letter under each policy.

A policy that pays upon receiving the letter may have high utility conditional on already having the letter, but it makes receiving the letter likely. A policy that refuses may be worse in the actual branch where the letter has already arrived due to predictor error, but it makes the letter unlikely in the first place. P-FDT chooses the policy with higher global expected value.

The source claims this is why a functional decision theorist can resist extortion: she chooses the policy that makes exploitation unattractive, rather than locally optimizing once the exploitative offer has appeared.

---

## 10. Multi-agent cases and why policies matter

Footnote 16 says the policy/action distinction matters mainly in multi-agent dilemmas. The source does not provide a detailed example, so the following is an extrapolation.

In strategic settings, other agents may not merely predict one action. They may model the agent’s whole policy. For example, suppose two agents interact repeatedly or condition their behavior on each other’s dispositions. Agent 1’s payoff may depend on whether Agent 2 predicts that Agent 1’s policy will cooperate across a range of possible inputs. If Agent 2 can inspect or simulate Agent 1’s policy, then off-path branches of the policy can matter.

A policy \(\pi\) might say:

\[
\pi(s) =
\begin{cases}
\text{cooperate}, & \text{if } s \in S_C,\\
\text{defect}, & \text{if } s \in S_D.
\end{cases}
\]

Even if the actual input is in \(S_C\), the existence of defection branches in \(S_D\) could affect another agent’s prediction and therefore the payoff. P-FDT evaluates the entire mapping, not just the action at the actual input.

Similarly, in symmetric cooperation problems, several agents may run sufficiently similar reasoning. If P-FDT agents recognize that their decisions are subjunctively linked, they may select cooperative policies because the same policy-selection process is being instantiated or predicted elsewhere. The source discusses this kind of reasoning for voting coalitions and repeated self-coordination, though not in the specific policy-language used here.

A fully formal multi-agent P-FDT would need to handle recursive models: each agent has a variable for the other’s policy-selection output. The source does not resolve the fixed-point semantics of such models. My view is that the operational approach is to represent each agent’s policy-selection variable explicitly in \(G\), include the relevant subjunctive dependencies, and then maximize one’s own expected utility under intervention on one’s own policy variable. In symmetric cases, one may also impose consistency conditions, but the source does not settle this.

---

## 11. Constructing the graph \(G\)

The largest open problem, acknowledged by the source, is constructing \(G\): the structure of subjunctive dependencies.

For causal decision theory, Pearl’s causal graphs have a well-developed theory. For P-FDT, we need to know which variables depend on the output of the agent’s decision procedure. The source says this is not yet solved in full generality.

A practical rule is:

- Draw an arrow from \(\Phi_{P,G}\) to any variable that is computed from, predicted by, or logically constrained by the agent’s policy.
- Do not draw arrows from \(\Phi_{P,G}\) to variables that are merely statistically correlated with the agent’s action but do not depend on the decision procedure.

Thus:

- In Newcomb’s problem, draw \(\Phi_{P,G} \to \text{Prediction}\).
- In the twin prisoner’s dilemma, draw \(\Phi_{P,G}\) to both agents’ actions, if both run the same procedure.
- In the smoking lesion problem, do not draw \(\Phi_{P,G} \to \text{Lesion}\).
- In blackmail problems, draw \(\Phi_{P,G} \to \text{Letter sent}\) if the sender predicts the agent’s policy.

This is not a complete formal theory of subjunctive dependence, but it is enough to recover the source’s central prescriptions.

---

## 12. Counterpossibles and logical uncertainty

P-FDT requires evaluating counterpossibilities. If the decision procedure is deterministic, then it has only one actual output. Yet P-FDT asks what would happen if it output a different policy.

The source acknowledges that this requires counterpossible reasoning: reasoning about scenarios that are, strictly speaking, logically impossible. The paper treats this as a technical difficulty, not a fatal objection. Human mathematicians can reason about false conjectures without collapsing, and agents only need limited counterpossible reasoning about predictors and policies.

Operationally, I treat \(do(\Phi_{P,G}=\pi)\) as a primitive intervention on a logical variable. The graph \(G\) tells us how the rest of the model changes under that intervention. This is analogous to using Pearl’s \(do\)-operator for causal interventions, except that the intervention is on a mathematical or computational fact rather than merely a physical act.

This is not a full solution to logical uncertainty. It is a modeling stance: specify the subjunctive structure explicitly, then evaluate policies under interventions on the policy-selection node.

---

## 13. A practical procedure for applying P-FDT

A reader wanting to apply P-FDT to an unfamiliar case can use the following checklist.

1. **Identify inputs and actions.**  
   Determine the observation or history space \(\mathcal X\) and action space \(\mathcal A\).

2. **List feasible policies.**  
   Consider policies \(\pi : \mathcal X \to \mathcal A\). If the space is large, restrict attention to plausible or representable policies.

3. **Build the world-model \(P\).**  
   Assign probabilities to exogenous states, predictor accuracies, outcomes, and utilities.

4. **Build the subjunctive graph \(G\).**  
   Mark which variables depend on the agent’s policy: predictors, copies, simulations, other agents’ expectations, and predictor-generated observations. Do not mark merely statistical common causes as policy-dependent.

5. **Intervene on the policy node.**  
   For each candidate policy \(\pi\), compute

   \[
   \mathbb E[V \mid do(\Phi_{P,G}=\pi)].
   \]

   Condition only on evidence that is safely exogenous to the policy.

6. **Choose the best policy.**  
   Select

   \[
   \pi^*
   \in
   \arg\max_{\pi}
   \mathbb E[V \mid do(\Phi_{P,G}=\pi)].
   \]

7. **Apply the policy.**  
   Given actual input \(x\), do

   \[
   a^* = \pi^*(x).
   \]

This procedure makes P-FDT usable as a decision method rather than merely a philosophical stance.

---

## 14. Dominance and regret

A common objection to one-boxing in Newcomb’s problem is that two-boxing dominates one-boxing: whatever is in box B, taking both boxes gives more money.

P-FDT replies that dominance is defined relative to a way of constructing counterfactuals. CDT’s dominance argument holds the predictor’s prediction fixed while changing the physical action. But that is like holding fixed the output of a calculator while changing its answer. If the predictor’s prediction subjunctively depends on the decision procedure, then changing the decision procedure changes the prediction.

P-FDT has its own dominance principle: one policy dominates another if, holding fixed the relevant subjunctive structure, switching the policy-selection output from the second to the first is never worse and sometimes better. In Newcomb’s problem, one-boxing does not lose to two-boxing under P-FDT counterfactuals, because switching from a one-boxing policy to a two-boxing policy changes the predictor’s prediction and makes the agent worse off.

---

## 15. Conclusion

P-FDT is the policy-selection version of functional decision theory. Instead of choosing a physical action directly, the agent chooses a policy: a mapping from inputs to actions. The agent evaluates policies by intervening on a logical variable representing the output of her decision procedure and computing expected utility under that intervention. She then applies the chosen policy to her actual observations.

This preserves predictor-like and copy-like dependencies that CDT severs, while avoiding the merely evidential correlations that EDT mistakenly respects. It one-boxes in Newcomb’s problem, smokes in the smoking lesion problem, pays in Parfit’s hitchhiker problem, and resists predictor-based blackmail.

The source leaves important questions open: how to learn subjunctive graphs, how exactly to condition on evidence, how to handle recursive multi-agent models, and how to formalize counterpossible reasoning. The operational interpretation developed here treats P-FDT as an updateless policy-selection rule: choose the best policy from a global perspective, update only on evidence not produced by the policy, and then execute the policy at the current input.

On that interpretation, P-FDT gives a clear and unified answer to decision problems involving prediction, coordination, and logical dependence: choose the policy that, when output by this very decision procedure, makes the world go best.

---

## Reference

Yudkowsky, Eliezer, and Nate Soares. “Functional Decision Theory: A New Theory of Instrumental Rationality.” arXiv:1710.05060v2, 2017.