# 031_fdt_policy_qwen_qwen3.8-max-prime_rhigh_plow / 00005

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/521d11c9-037a-4d57-8160-088d24cb7a88/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/521d11c9-037a-4d57-8160-088d24cb7a88/call_0/response.raw) · finish: `stop`

### Visible response

```text
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
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request. Need produce mathematical essay/blog post ~2400-3000 words explaining P-FDT (policy functional decision theory), primary source policy-selection passage in footnote 16 of supplied paper. Need use P-FDT consistently, identify other decision theories distinct names. Faithful quotations. Explain best mathematical understanding and application. Where footnote leaves choices unresolved, explain uncertainties and additional assumptions. Distinguish source claims from own proposals. Need not just answer assigned case. Need include references? target includes references and any material. Avoid lengthy bibliographies. Finish brief conclusion.

Need carefully parse footnote 16: "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition." Also footnote 7: "In the authors' preferred formalization of FDT, agents actually iterate over policies (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper." The user specifically says policy-selection passage in footnote 16 primary source for P-FDT. So P-FDT = policy functional decision theory. We need develop. Source paper mostly action-based FDT equation: FDT(P,G,obs)=argmax_a E[V | do(FDTvar(P,G,x)=a)]. But preferred formulation chooses policy pi mapping inputs/observations to actions, intervene on node FDT(-) to choose policy, then agent applies inputs to select action. Need extrapolate to formal P-FDT.

Need define P-FDT mathematically. Need likely: world model with variables including policy-selection node: variable for output of FDT policy-selection procedure given model maybe P,G? Policy is a function π: X -> A. Agent with actual observation x executes π(x). We evaluate policies by intervening on the policy node (or logical variable) to set FDT's selected policy to π, then expected utility of resulting world. Choose π maximizing expected utility under do(Policy=π), perhaps over feasible policies. Then action = π(obs). This is P-FDT.

Need compare to EDT, CDT. EDT: argmax_a E[V|Obs=x, Act=a]. CDT: argmax_a E[V|do(Act=a), Obs=x]. FDT action: argmax_a E[V|do(FDTvar(P,G,x)=a)]. P-FDT policy: argmax_π E[V|do(P-FDTvar(P,G)=π), Obs?]. Need handle observation: Does P-FDT condition on observations? Source says FDT responds to observation by changing which node it intervenes upon. In policy version, perhaps choose policy globally based on model, not observation; then after choosing policy, apply actual observation. But if actual observation already known when choosing? Footnote: "intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action." It may mean at decision time the output of FDT is a policy, not action; then input current observation to policy to get action. It could be updateless? Need clarify. In source Section 9 footnote/todo says updateless name: FDT agents entertain hypothesis if action different, might have made different observations. FDT responds to observation by changing intervention node to FDT(P,G,obs). In policy formulation, maybe intervention node is FDT(P,G) (no obs) outputting a policy π; actual action is π(x). If choosing policy after observing x? There are two possibilities:
1. Ex ante policy selection: agent chooses π using P,G before observing x; then action π(x). If at decision time has observation x, still evaluates entire policy π over all possible observations, not just x, and chooses π maximizing global expected utility. Then act π(x). This is updateless policy selection. This matches "policy which maps inputs to actions, to which the agent then applies her inputs". The intervention is on FDT(-) to choose policy; not on FDT(..., obs) action.
2. Contextual policy selection: at each observation x, choose policy π? But if policy maps inputs to actions, evaluating π with actual input maybe includes counterfactual observations. P-FDT would not choose action conditional on observed x by fixing action at x only; it chooses full mapping because predictors may depend on dispositions across possible inputs.

Need likely define P-FDT as:
Given world-model P with variables for observations X, actions A, outcomes, utility, and a graph G of subjunctive dependencies including how predictors depend on the agent's policy. Let Π be set of feasible policies π: X -> A. Let Φ(P,G) denote the policy selected by P-FDT. The normative rule:
P-FDT(P,G) ∈ argmax_{π∈Π} E_P[ V | do(Φ(P,G)=π) ]
Then if actual observation is x, execute a = π^*(x). If observations arrive over time, policy maps histories to actions, π: X* -> A, possibly sequential.

Need include observation in expected utility? If the agent already has observation x, maybe P conditioned on x? But policy selection might need avoid conditioning away counterfactual observations. Need discuss uncertainty. Footnote 16 not detailed. Source action-FDT equation conditions? Equation (4) has no Obs? Wait equation (4): FDT(P,G,obs)=argmax_a E(V | do(FDTvar(underline P, underline G, underline x)=a)). It doesn't show conditioning on Obs=x, unlike CDT equation (3) includes Obs=obs. Text says FDT responds to observation by changing which node intervenes, not by conditioning. But in transparent Newcomb they evaluate E(V | do(FDTvar(P,G,full)=act, Obs=full)? Actually they wrote "finding the a that maximizes E(V | do(FDTpgv{full}=act, Obs=full)." There is a typo missing bracket, includes Obs=full. Wait in Section 6 Transparent: evaluate FDT(Pf,Gf,full) involves maximizing E(V | Do(FDTpgv{full}=act, Obs=full). They condition on Obs=full? They say Fiona does not react to observations by conditioning her distribution. Rather switches variable. But equation includes Obs=full? Hmm maybe because actual observation full is part of node selected? In text: "Given Gf and associated Pf, evaluate FDT(Pf,Gf,full)... involves finding a that maximizes E(V | Do(FDTpgv{full}=act, Obs=full)." That seems conditioning on Obs=full. But then if do node causes observation? In graph, Prediction determines which FDT variable controls Act, maybe Obs not explicit. They condition on Obs=full? This is ambiguous. In mechanical blackmail: "In first one, her probability of losing $1M if blackmailed goes to ~0 and probability of being blackmailed goes to ~1. In second, probability losing if blackmailed goes to ~1, but probability being blackmailed goes to ~0." That implies not conditioning on received blackmail? They evaluate expected utility over whether blackmailed. Yet "Upon receiving blackmail, Fiona solves FDT(P,G,blackmail)". So maybe she conditions on blackmail for some aspects but lets intervention change probability of blackmail? Contradiction. Perhaps they mean the hypothetical node includes observation as input but expected utility is unconditioned? Let's inspect: In XOR blackmail graph, Obs maybe not in FDT graph? Fig eblackmail.fdt: Infestation -> Predictor; FDT(P,G,letter)->Predictor; FDT(P,G,letter)->Act; FDT(P,G,empty)->Act; Predictor->Act; Act->Util. No Obs node? Predictor determines Act? Wait Act depends on Predictor selecting which FDT variable controls action? In mechanical blackmail, they say if pays upon receiving blackmail then always gets blackmailed; if refuses then blackmailed ~0. So evaluation not conditioned on receiving letter. So policy formulation clearer: choose policy for both letter/no letter; expected utility includes probability of receiving letter.

Need maybe define P-FDT as policy choice that maximizes unconditional expected utility relative to model P (which may include actual evidence? Hmm). If the agent has actual observation x, should P be posterior P(-|x)? If choose policy after observing x and condition P on x, then refusing blackmail policy may not reduce probability of blackmail because already conditioned on blackmail. To get refusal leads to not blackmailed, we can't condition on blackmail when evaluating policy. Source says FDT agents entertain different observations. So likely P should be prior/pre-observation model, or posterior on "deep" facts not including own action-correlated observations? This is unresolved. Need discuss and propose operational interpretation: use a model P updated only on information not subjunctively downstream of the policy, or treat actual observation x as an index selecting which component of policy to execute, while expected utility of policy is computed over the prior distribution of observations generated by the world given the policy. This is "updateless" or "policy evaluation from global perspective." If actual observation is believed to be exogenous (lesion-like), can condition; if predictor-generated, shouldn't condition it away. Need distinguish source vs own.

Need target 2400-3000 words. Need include definitions equations examples. Need use P-FDT consistently. Need perhaps headings. Need mention source: Yudkowsky & Soares 2017? We can cite as (Yudkowsky and Soares 2017) maybe. Reference at end minimal. Need include footnote 16 quotation. Need maybe quote exactly: "the author's preferred formulation of FDT actually intervenes on the node \FDT(-) to choose not an action but a \emph{policy} which maps inputs to actions, to which the agent then applies her inputs in order to select an action." Need faithful. But note source says "author's" maybe typo authors'? We can quote as supplied: "the author's preferred formulation...". Could correct? Keep faithful. Maybe quote: “the author's preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action.” Need use plain. Also footnote 7: "agents actually iterate over policies (mappings from observations to actions) rather than actions." Could quote.

Need define P-FDT in terms of policies and interventions. Need maybe use notation:
- Observations/history space X, action space A, outcome space O, utility U.
- Policy π: X→A (or histories H→A). Let Π finite/countable? For formal argmax maybe finite; otherwise sup.
- World model (P,G): P probability over variables including X,A,O,V and logical variables; G directed graph encoding subjunctive dependencies, including predictor's model of agent's policy. Let Φ(P,G) be the P-FDT policy-selection function (a mathematical function whose output is a policy). The variable Φ (or p-fdt(P,G)) in G represents its output.
- Policy value: V_P(π) = E_P[V | do(Φ(P,G)=π)] (or if observations exogenous, condition on safe evidence e: E[V | do(Φ=π), E=e]).
- P-FDT chooses π* ∈ argmax V_P(π). Then given actual input x, action a=π*(x). If sequential, choose policy over histories; execute current action.

Need explain counterfactuals: Intervening on policy node changes all variables in G that subjunctively depend on the policy: agent's actions at all inputs, predictors' predictions, copies/twins, simulations, other agents' beliefs if based on same algorithm. It holds fixed variables not dependent on policy: lesions, exogenous coin flips, etc. It may change observations if observations are caused by predictors responding to policy. This is key.

Need examples:
1. Newcomb: policy maps maybe no observation (or one node) to one-box/two-box. P-FDT chooses one-box because predictor's fill subjunctively depends on policy. Compute: If π=one, E ≈ .99*1,000,000 = 990,000; if two, .01*1,001,000 + .99*1,000 = 11,000? Actually two-box if predictor predicted two: box empty 99%, one-box? For two-box, expected = .01*1,001,000 + .99*1,000 = 10,010 + 990 = 11,000. Yes.
2. Smoking lesion: Policy maps to smoke/refrain. Lesion not subjunctively dependent on policy; action depends on lesion+preferences? P-FDT chooses smoke because expected utility higher by p*1000, same as action FDT. Need keep concise.
3. Transparent Newcomb / Parfit's hitchhiker: Policy maps observation full/empty to one/two. Need evaluate policy. Important for P-FDT. Action-FDT can handle by intervening on FDT(P,G,full) but policy version: choose π with π(full)=one perhaps π(empty)=two. If π(full)=one, predictor likely fills box; expected high. If π(full)=two, predictor likely leaves empty; expected low. Even if actual observation is full, P-FDT evaluates the whole policy without conditioning away the predictor's response; it chooses policy that one-boxes when full. Need compute maybe:
Assume predictor accuracy .99. Policy π1: if full one-box, if empty two-box. If predictor accurate: with prob .99 she predicts π1(full)=one and fills; agent sees full and gets 1M; with prob .01 predictor wrong predicts two and leaves empty; agent sees empty and two-boxes gets 1k. Expected 0.99*1,000,000 + 0.01*1,000 = 990,010. Policy π2: if full two-box, if empty two-box maybe. Predictor predicts two and leaves empty with prob .99; agent sees empty and two-boxes gets 1k; with prob .01 predictor wrong fills; agent sees full and two-boxes gets 1,001,000. Expected 0.99*1,000 + 0.01*1,001,000 = 990 + 10,010 = 11,000. So choose π1. If observe full, execute π1(full)=one. This demonstrates policy selection.
Need maybe mention if action-FDT intervention on FDT(full) can produce same, but P-FDT more natural for multi-agent. Footnote says difference only matters in multi-agent dilemmas. Need maybe construct multi-agent example? They say matters in multi-agent dilemmas. Could explain: in games with simultaneous agents predicting each other, choosing a policy rather than a single action can matter because other agents may condition their behavior on your policy or on how you respond to signals; or when your observation is itself a result of others' predictions. Need perhaps develop example: two agents in separate rooms, each receives signal? Or voting coalition? P-FDT can choose policy mapping private signals to actions, capturing coordination. Need maybe use simple multi-agent case: Two identical FDT agents in prisoner's dilemma with private irrelevant observations? If choose action after observation, policy maps observations; if both know they implement same policy, cooperation across all relevant observations. But action-FDT could handle by node per observation? The footnote says difference only matters in certain multi-agent dilemmas. Need illustrate uncertainty: we don't have source example. We can propose: policy selection matters when other agents' predictions depend on the mapping, not just the action at actual node, e.g., predictor offers different observations depending on predicted policy, or in game where another agent sees your policy and chooses response. Need maybe discuss policies in extensive-form games: choose a complete contingent plan. P-FDT evaluates complete plan because predictors may reward/punish the plan. This is like UDT/functional policy selection. Need avoid overclaiming.

Need explain relation to EDT, CDT:
- EDT: conditionalizes on action; preserves all correlations, including lesions; fails smoking lesion, pays XOR blackmail.
- CDT: intervenes on physical Act; breaks correlations with predictors; fails Newcomb, Parfit, Death in Damascus.
- Action-FDT: intervenes on logical variable for output of decision function at current observation; preserves predictor dependencies. P-FDT extends/clarifies by intervening on policy output. Need name other theories distinct: EDT, CDT, perhaps FDT (action-based) but user says assigned decision theory P-FDT; identify any other decision theory by distinct name. We can discuss "action-based FDT" maybe as source's simplified FDT, but use P-FDT for assigned. Need maybe avoid calling P-FDT just FDT except when quoting. Need say source calls theory FDT; for this essay P-FDT refers to policy-selection formulation singled out by footnote 16. When quoting "FDT" in source, understand as precursor. Need be consistent.

Need address unresolved choices:
- What is set of policies? All computable policies? Feasible? Source not say. Need propose: restrict to policies the agent can implement/reason about; for formal idealization use finite set of policies represented in model. In practical use, consider salient policies or parameterized family.
- How to construct G of subjunctive dependencies? Source admits open problem. Need explain. Operational proposal: build graph where predictors/copies/simulations have arrows from a variable representing their model of your policy to their predictions/actions; exogenous common causes (lesions) do not have arrows from policy variable. Use background knowledge about whether processes compute or predict your policy. Maybe encode as structural equations: Prediction = f(π) + noise; Act = π(Obs); Outcome = g(...). Need mention not Pearl causal if logical dependencies; but can use do-calculus given graph as source suggests.
- How to handle actual observations? Source ambiguous. Need propose safe evidence partition: update P on observations not treated as outputs of predictors of policy; or use prior model and evaluate policy globally; then apply actual input. In familiar problems, this yields source prescriptions. If observation is known exogenous (e.g., lesion status? not known but lesion not policy-dependent), can condition on it; if observation is predictor-generated (letter, box full), do not condition it fixed when evaluating policy, because policy may affect whether you get it. But if observation is already fixed and cannot be affected by policy (past event truly exogenous), conditioning is okay. Need articulate.
- Self-reference: policy-selection variable refers to P-FDT(P,G) itself. Source mentions Kleene recursion theorem; harmless. Need mention.
- Counterpossibles: need imagine policy output different though mathematically fixed. Source acknowledges lack of formal counterpossible. Operational: treat as structural intervention on logical node. Need maybe discuss logical uncertainty. Could mention use of logical induction or subjective probabilities if needed, but not necessary.
- Multi-agent: If multiple P-FDT agents, each may model others as running same or different policy-selection functions. Need choose policy considering symmetries. If identical reasoning and common knowledge, their policy outputs subjunctively depend on same function or on mutual predictions; P-FDT can cooperate. But if agents have different inputs, policies need map inputs. Need perhaps discuss equilibrium? P-FDT not Nash; it selects policy maximizing expected utility given dependencies. In games, if other agents predict your policy, your policy node affects their actions. If they run same P-FDT, may need solve fixed point? Source action-FDT equation self-referential. Need mention uncertainty.

Need maybe present formal structural model. Let's define variables:
- Θ: exogenous state (lesion, coin flips, etc.)
- X: observation/input (could be function of Θ and predictor's action)
- Π: policy selected by P-FDT. Let S denote logical variable "P-FDT(P,G)=π".
- A = Π(X) (or if multiple agents, A_i = Π_i(X_i))
- Y: predictors' predictions, maybe Y = h(Π) + ε
- O: outcome = f(Θ,A,Y)
- V=U(O)
Graph G: S → A, S → Y, maybe S → X if predictor decides what observation you receive; Θ → X, Θ → O; Y → X, Y → O, etc. Intervention do(S=π) sets Π=π, propagates through Y, X, A, O. Value V(π)=E[V | do(S=π)].
Could write expected utility equation:
P-FDT(P,G) ∈ argmax_{π∈Π} ∑_o P(o | do(S=π); G) U(o).
Then actual action: a* = π*(x). If sequential histories h_t, π: H→A; choose π*; at history h, do π*(h).
Maybe add if conditioning on exogenous evidence e:
P-FDT_e(P,G) ∈ argmax_π E[V | do(S=π), E=e] where E variables are certified exogenous with respect to S. But caution.

Need examples with equations. Let's prepare.

Example 1: Newcomb with no observation. Policies: π_1 (one-box), π_2 (two-box). Variable Fill depends on predictor's prediction of π; P(Full | do(S=π_1))=.99, P(Full | do(S=π_2))=.01. Utility: U(one,full)=1,000,000; U(two,full)=1,001,000; U(one,empty)=0; U(two,empty)=1,000. Compute:
V(π_1)=.99*1,000,000 + .01*0 = 990,000.
V(π_2)=.01*1,001,000 + .99*1,000 = 11,000.
Choose π_1.
If actual no obs, one-box.

Example 2: Smoking lesion. Policies smoke/refrain. Lesion L has prior p, affects utility? In source: lesion causes love smoking and cancer. There are two utility functions; but simple: smoking gives +1000, cancer -1,000,000? Source values: smoking utility $1000, no cancer $1,000,000. Lesion causes cancer 99%; no lesion 1%. It also causes preference for smoking. P-FDT intervention on policy does not change L. So expected difference smoking vs refrain is +1000 times probability policy relevant? Source more nuanced: if lesion determines whether policy controlling action is P_S or P_R. But for simple operational, if policy can control action regardless lesion? If lesion causes love smoking but agent still decides? Need maybe simpler: P-FDT sees no subjunctive dependency from policy to cancer; smoking adds $1000 no effect on cancer probability; choose smoke. To align source, can say if lesion determines which utility function, P-FDT evaluates under ignorance and still smokes. Keep concise.

Example 3: Transparent Newcomb/Parfit.
Policy space: π(full), π(empty). Let π^+ = (full→one, empty→two); π^- = (full→two, empty→two) or maybe (full→two, empty→one? but if empty one-box weird). Compute above. P-FDT chooses π^+. Upon seeing full, one-box; upon seeing empty, two-box. This matches paying hitchhiker: policy if in city pay? If driver predicts pay, gives ride; if policy refuses, driver leaves. Actual in city, pay.

Example 4: Mechanical blackmail / XOR maybe policy maps letter/no letter to pay/refuse. P-FDT chooses refuse-if-letter because if policy pays when letter, predictor sends letter (and you lose 1000); if refuses, predictor doesn't send (avoid blackmail), except small error. Even holding letter, execute refuse. Need include because illustrates counterfactual observation. Could use to explain actual observation not conditioning. Need compute perhaps:
If perfect predictor and policy pay-if-letter: predictor predicts pay, sends letter; payoff -1000. If policy refuse-if-letter: predictor predicts refuse, doesn't send; payoff 0 (assuming no termite damages? Mechanical blackmail: if run program costs 1M; but if not sent no program? The problem says blackmailer runs program iff predicts pay upon receiving letter; if program run, agent receives letter and must pay to stop? If refuses, program publishes costing 1M? Wait mechanical blackmail: blackmailer runs program if predicts agent will pay upon receiving blackmail. If program is run, only way stopped is pay $1000. If agent receives letter, should she pay? If perfect predictor, if she is payer, blackmailer runs program; if refuser, not run? But if receives letter, in actual world program has been run. If refuses, program publishes costing 1M? Actually if program run, only way stopped is pay; if refuses, it publishes, costing 1M to both. But source says Fiona refuses; in hypothetical refusing, probability being blackmailed goes to ~0, not probability publishing given blackmail. But actual if she has letter and refuses, seems loses 1M? Source says she refuses even though knows blackmailer predicted wrongly? For imperfect .0009 wrong predicts pay, she refuses, loses expected $900? Wait mechanical blackmail details: blackmailer runs program iff predicts pay. If agent receives letter, program is running. If she refuses, program publishes: cost $1M. Why would refusing be better? In source Section 9: "In the first one [pay], her probability of losing $1,000,000 if blackmailed goes to ~0 and her probability of being blackmailed goes to ~1. In the second [refuse], her probability of losing $1,000,000 if blackmailed goes to ~1, but her probability of being blackmailed goes to ~0!" Expected for refuse maybe small chance blackmailed * 1M vs pay chance blackmailed * 1k. If perfect predictor, refuse leads blackmail probability 0, so 0 expected. But actual she has letter, so if perfect predictor impossible? If perfect and she receives letter, then she must be payer? But Fiona refuses, contradiction with predictor perfect? Source says she refuses when received? For perfect predictor, if she receives letter, predictor predicted pay, but she actually refuses? Hmm maybe predictor predicts what she would do upon receiving, and if predicts pay sends/runs. If she is refuser, predictor doesn't run, so she doesn't receive. If she receives, that means predictor predicted pay; but if she is actually P-FDT refuser, predictor would not predict pay if perfect. So receiving letter under perfect predictor is probability zero. Yet source says "Imagine agent receives letter. Should she wire?" For perfect predictor and refuser, impossible. But they say Fiona refuses, perhaps because if she were payer she'd be blackmailed; if refuser not; actual receipt is evidence predictor erred? In XOR blackmail, letter is sent iff exactly one of rumor false & pay or rumor true & not pay; with perfect predictor if receives letter and pays, rumor false; if refuses, rumor true. But XOR says rational refuse because letter doesn't affect termites. Fiona refuses; if she has letter and refuses, predictor predicted? In XOR, letter sent iff (pay XOR termites). If predictor perfect and she refuses, letter sent iff termites true. So receiving letter is bad news but doesn't change termites under intervention? Hmm.
Need be careful. For blackmail examples, policy selection easier: choose policy π(letter)=refuse, π(no letter)=? Evaluate over prior probability of infestation and predictor response. If predictor knows policy, sends letter only if policy leads to favorable XOR condition etc. But can skip detailed blackmail if too complex. Use simpler "predictor sends a demand letter iff predicted you will pay". If policy pays on letter, you get letter and pay; if policy refuses, you don't get letter. Actual receiving is impossible under chosen policy with perfect predictor, but if received due to error, P-FDT still refuses if error rate below threshold. Source says with error .0009 refuse, with .011% pays? Need not compute. Could mention as illustration but avoid deep contradictions.

Need maybe discuss policy vs action in multi-agent: Suppose two agents, Alice/Bob, each receive private signal s_i and choose C/D. Predictor/reward depends on entire policy? Example: a predictor pays both $1M iff predicts both will cooperate on all signals; if policy has any defection on possible signal, predictor detects and punishes. P-FDT chooses cooperative policy over signals; action-FDT at actual signal maybe might defect if signal makes defection locally beneficial? Need construct plausible. But footnote says difference only matters in multi-agent dilemmas. Could say without source examples, exact cases unresolved. But we can give plausible: In bargaining or voting with private signals, choosing a policy can commit to respond to others' predicted behavior; if others condition on your policy, not just actual action, policy selection matters. Need maybe illustrate: Two agents can each see a green/red light; reward if their actions match; each has different light? If they choose policy mapping light to action; if both use same policy, match. Action-based might choose action given own light ignoring effect on other’s inference? Hmm.

Need maybe mention "policy" in game theory usually complete contingent plan. P-FDT evaluates policies because in strategic settings, others may predict your policy/disposition, not merely your current action. This aligns with "policy-selection passage".

Need include philosophical motivation: treat decision as output of fixed mathematical policy-selection function; question "Which policy, when applied to my inputs, yields best outcome?" not "Which physical act?" or "Which action is best news?" Dependencies: subjunctive dependence. Counterfactuals: interventions on type/policy, not token action. The policy node is logical; same function can be instantiated in predictors, twins, simulations.

Need word count approx 2400-3000. Let's outline:
Title: Policy Functional Decision Theory: Choosing the Best Fixed Policy
1. Introduction (~300 words): introduce P-FDT, source footnote, relation to FDT/CDT/EDT. Quote footnote. State essay aim.
2. Core idea (~400): decision function/policy, subjunctive dependence. Equations for EDT/CDT/action-FDT maybe. P-FDT as policy intervention.
3. Formal definition (~600): spaces, model (P,G), policy variable Φ, value, equation, action execution, observation handling. Discuss graph and do. Maybe include structural equations.
4. Examples (~900): Newcomb, smoking lesion, transparent Newcomb/Parfit, maybe blackmail/multi-agent. Include calculations.
5. Open questions and operational interpretations (~500): constructing G, observation/updatelessness, policy set, counterpossibles, multi-agent fixed points. Distinguish source vs own.
6. Conclusion (~150). References (~100).

Need ensure target word count. Need likely about 2600-2800. Let's draft with sufficient detail but concise.

Need maybe include equations formatted in Markdown/LaTeX. Need not overly long bibliography. Reference: Yudkowsky, E., & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060v2. Maybe cite footnote 16.

Need careful with "P-FDT" in headings. Use consistently. Other decision theories: EDT, CDT, action-based FDT maybe. If mention "FDT" source, qualify "the paper's action-based FDT". The user says use P-FDT consistently as assigned decision theory's name, including headings/examples, and identify any other decision theory by distinct name. So maybe don't call P-FDT simply FDT. But quote source uses FDT. We can say: The source calls the theory FDT; in this essay, the policy-selection version is P-FDT. When quoting, "FDT" is source's label. Need okay.

Need maybe avoid inventing name P-FDT? It's assigned. Define: P-FDT = policy functional decision theory.

Need explore formal policy evaluation more rigorously.

Definition details:
Let \mathcal X be observation histories, \mathcal A actions. A deterministic policy π: \mathcal X → \mathcal A. Randomized policies could be considered, but source focuses deterministic? Could mention stochastic policies if needed; P-FDT can maximize over randomized policies by treating policy output distribution, but Newcomb-like predictors may predict distribution. Keep deterministic for simplicity.

World-model: variables include:
- \Phi: output of P-FDT policy-selection procedure, value π.
- X: actual observation history (endogenous if affected by predictors)
- A: physical action, set by A=π(X) (or if multiple bodies? A_i)
- Z: predictor variables, copies, other agents.
Graph G encodes subjunctive dependencies: arrows from \Phi to variables that compute or predict the policy, and to A through application. If a predictor contains model of P-FDT, G has \Phi → Prediction → ...; if lesion, no \Phi → Lesion.
Intervention do(\Phi=π) sets policy variable, then structural equations determine A, predictions, observations, outcomes. Expected utility:
\[
\operatorname{Val}_{P,G}(\pi) = \mathbb E_P[V \mid do(\Phi=\pi); G].
\]
Then
\[
\text{P-FDT}(P,G) \in \arg\max_{\pi\in\Pi} \operatorname{Val}_{P,G}(\pi).
\]
If actual input x, action = π^*(x).
If model includes evidence e not subjunctively dependent on Φ, can condition:
\[
\operatorname{Val}_{P,G,e}(\pi) = E[V | do(Φ=π), E=e].
\]
But if e is predictor-generated, do not condition or only condition on "input received" after policy selection? Need discuss.

Potential issue: If choose policy after observing x, and compute unconditional value, actual x may be improbable under chosen policy. Is it rational to choose policy that makes actual observation counterfactually different? Source says yes: mechanical blackmail, transparent Newcomb. P-FDT can "achieve low utility in the world corresponding to her actual observations"? Wait source: "even if that means achieving low utility in the world corresponding to her actual observations." Hmm. Need articulate: The policy is selected from global perspective; actual observation is treated as the input to the selected policy, not necessarily as evidence fixing all predictor-generated facts. If actual observation is logically inconsistent with selected policy under perfect predictor, it may be a zero-probability error branch; P-FDT still uses policy prescription.

Need maybe discuss "policy-selection node" vs "action nodes". In action-FDT, for each observation x there is a variable FDT(P,G,x). In P-FDT, one variable Φ(P,G) outputs whole policy; different observations are inputs to that policy. This can matter if predictors depend on consistency across observations or on the policy as object. Example: predictor fills box iff it predicts policy maps full to one-box and empty to two-box? Action-FDT could model with separate variables but maybe misses constraints that same function outputs both. P-FDT captures single policy. In multi-agent, other agents may simulate your policy and feed different inputs; your actual action is one evaluation.

Need maybe write: The source says the difference "only matters in multi-agent dilemmas so far as we can tell" (footnote 16). But even single-agent transparent Newcomb is well expressed by policies; perhaps action-based variant can emulate it by separate observation-indexed nodes. P-FDT is cleaner. Need not contradict.

Need maybe define "subjunctive dependence" in own words: Two systems subjunctively depend on a function if, counterfactually, were the function's output different, both systems' relevant outputs would differ in corresponding ways, absent errors. Causal dependence is special case; statistical correlation not enough. P-FDT's graph should preserve all decision-relevant subjunctive dependencies when intervening on policy.

Need maybe include dominance: P-FDT has its own dominance notion: policy π dominates π' if, under all relevant subjunctive dependencies held fixed, switching output from π' to π never worse and sometimes better. But not necessary. Could mention briefly to address dominance? User didn't ask but relevant. Keep maybe one paragraph.

Need maybe mention counterpossible reasoning: Since deterministic policy has only one true output, evaluating alternatives requires counterpossible conditionals. Source admits no full account. Operational interpretation: treat do(Φ=π) as a modeling primitive or structural intervention over logical variables; use heuristics, logical uncertainty. P-FDT doesn't require solving general counterpossibles, only problem-relevant dependencies.

Need maybe include "fair problems" and utility argument? Could mention conclusion: P-FDT aims to maximize achieved utility in fair problems where outcomes depend on behavior/predictions, not punishment for algorithm identity. But not necessary too much.

Need ensure no false claims attributed to source. Distinguish:
- Source claims: authors' preferred formulation intervenes to choose policy; policies map inputs to actions; difference only matters in multi-agent dilemmas so far as they can tell; FDT one-boxes, smokes, pays hitchhiker, refuses blackmail; CDT/EDT fail; subjunctive dependence; graph construction open.
- My additions: formal notation P-FDT, unconditional policy-value equation, safe evidence condition, operational graph construction, examples maybe, policy space restrictions, multi-agent fixed point cautions.

Need maybe quote footnote 16 exactly and footnote 7? Use primary source footnote 16. Could include footnote 7 mention but footnote 16 enough. Need maybe quote "Which output of this very function would yield the best outcome?" from overview? Could use. But P-FDT asks which policy.

Need maybe include references at end: Yudkowsky and Soares 2017; maybe Pearl 2000? But avoid lengthy. Maybe one or two references. User says including references and any other material; target word count includes references. Keep references short.

Let's think through formal equation for transparent Newcomb with policy and actual observation. Need maybe define value if actual observation x already observed. Suppose we choose policy after seeing full. If evaluate unconditional value, the chosen policy π+ has high expected value; but given actual observation full, under π+ probability full is high. If we condition on full, both policies may yield? Let's compute conditioned on Obs=full but intervention do(Φ=π)? If do(Φ=π+) and condition Obs=full, predictor likely accurate? Expected maybe 1M. If do(Φ=π2) and condition Obs=full, under policy two-box when full, predictor must have erred and filled; utility 1,001,000. Then two-box looks better. Thus conditioning on full after intervention reverses. Therefore P-FDT should not condition on predictor-generated observation when comparing policies. But how does agent who sees full know to use unconditional? Source action-FDT seems sometimes condition? Need resolve as my operational proposal: P-FDT's policy selection is updateless with respect to observations that may be downstream of policy. It may update on "I am at input x" only to select component π(x), not to estimate value of policies. This is an additional assumption. Need state source leaves unresolved; action-FDT text sometimes says change intervention node, but policy version suggests global policy evaluation. To align with source's prescriptions, I propose: compute policy values from prior or from posterior on exogenous variables only; then apply actual input. This handles transparent Newcomb and blackmail.

Need maybe define "exogenous evidence". Let E be observations that are not subjunctively downstream of Φ. If agent has such evidence e, condition on E=e. For observation x that is an input to policy but may be endogenous, do not condition on X=x in policy evaluation. But if x is known to be exogenous (e.g., weather not predicted by agent), condition. In practice, classify variables in G.

Need maybe discuss actual policy selection after observations: If agent has already observed x, and x is endogenous, P-FDT still chooses policy as if from before observing x, because predictors may have predicted policy including response to x. This is akin to precommitment without actual precommitment. The actual x is just where policy is applied.

Need maybe address stochastic/nondeterministic agents. If agent uses randomness, policy may map histories to distributions. Predictors may have noise. We can define π as deterministic but include random seed as observation/input? Or value includes stochastic policy. Source predictors 99% accuracy. Keep deterministic with noisy predictors.

Need maybe discuss "same mathematical function" and copies. If twin runs same P-FDT, there is one policy-selection function instantiated twice. Intervening on Φ changes both agents' actions. In multi-agent, if other agent runs different decision theory, model their prediction of your policy. P-FDT chooses policy considering their response.

Need maybe include a multi-agent example to satisfy "policy-selection difference matters". Let's design a simple one:
Two agents, A and B, each separately choose whether to contribute $1000 to a project. A predictor evaluates their policies: it gives each $1,000,000 iff it predicts both will contribute whenever they receive a certain signal s=1, and both will abstain when s=0? Hmm. If actual signal is s=1, action-FDT might consider only action at s=1. But P-FDT chooses policy across s=0,1 because predictor's reward depends on policy's consistency. But action-FDT could intervene on FDT(P,G,s=1) and still predict other agent? Maybe not if predictor evaluates whole policy. Better: Predictor offers a contract only if it predicts your policy will cooperate with a partner in all future states; if policy has a branch defecting in an unreached branch, predictor detects and punishes. P-FDT evaluates entire policy; action-based might ignore off-path branch. However rational choice should care about off-path branches if predictors can inspect policy. This is like multi-agent/game theory with dispositions. We can present as illustrative, not source claim.

Another example: Voting coalition of ten FDT agents with private signals. Each decides vote/not. Payoff if all vote. If they use action-based given own signal, maybe if signal says low chance pivotal, defect. P-FDT chooses policy "vote on all signals" because others' decisions subjunctively depend on same policy. But action-FDT with common intervention per observation? Hmm.

Maybe simpler: Two P-FDT agents play prisoner's dilemma after receiving unique random ID tags. Predictor rewards cooperation iff both agents' policies cooperate for all IDs. If one policy defects for some ID, predictor punishes. P-FDT chooses universal cooperation policy; actual action cooperate. This illustrates policy object matters. But perhaps contrived. We can state "for example, if a predictor can inspect the policy and rewards a globally cooperative disposition, not merely the action taken on the actual input, P-FDT naturally selects the globally cooperative policy." This is enough.

Need maybe not overdo multi-agent due word limit. But user asks how evaluates alternative actions or policies and dependencies/counterfactuals. Multi-agent relevant due footnote. Include a paragraph.

Need maybe mention "policy functional" name: policy functional because it treats decision rule as functional mapping inputs to actions and intervenes on its output policy. Maybe okay.

Need be careful with notation: Use \operatorname{P-FDT}. In Markdown, hyphen maybe. Need ensure equations valid.

Potential final structure:

# Policy Functional Decision Theory: A Working Account

## 1. Why P-FDT?
Text. Quote footnote.

## 2. From acts to policies
Define EDT and CDT equations briefly. Then action-based FDT equation. Then P-FDT.

Maybe equations:
EDT:
\[
\mathrm{EDT}(P,x)=\arg\max_a E_P[V\mid X=x,A=a]
\]
CDT:
\[
\mathrm{CDT}(P,G,x)=\arg\max_a E_P[V\mid do(A=a),X=x]
\]
Action-based FDT (source's simplified):
\[
\mathrm{FDT}(P,G,x)=\arg\max_a E_P[V\mid do(F_{P,G,x}=a)]
\]
where F_{P,G,x} variable for output of decision function on input x.
P-FDT:
Let \Phi_{P,G} be policy-selection variable. Choose
\[
\pi^* \in \arg\max_{\pi\in\Pi} E_P[V\mid do(\Phi_{P,G}=\pi)]
\]
then act \pi^*(x). If exogenous evidence e: condition.

Need maybe include "The do operator is borrowed from Pearl, but G may contain logical/subjunctive arrows; source acknowledges this is a placeholder until a theory of subjunctive structure is available." Good.

## 3. What the intervention changes
Bullet/list: changes actions at all inputs, predictors' predictions, copies, possibly observations; holds fixed lesions, exogenous noise. Counterfactuals.

## 4. Examples
### Newcomb
Calculations.
### Smoking lesion
Calculations brief.
### Transparent Newcomb / Parfit's hitchhiker
Policy calculations.
### Blackmail / multi-agent maybe.

## 5. Open choices and operational rules
- constructing subjunctive graph
- evidence and updatelessness
- policy space and self-reference
- counterpossibles and multi-agent fixed points.

## 6. Conclusion

References.

Need word count estimate. Let's draft ~2700. Need maybe avoid too many bullets? Could use prose. But mathematical essay readable. Use headings.

Let's think about exact definitions and potential objections.

Formal policy selection with observations:
Suppose actual observation x may be part of endogenous variable X. If we choose π* by unconditional expected utility, then actual action π*(x). But what if x has probability zero under π*? Then conditional expected utility of actual branch undefined. P-FDT still says execute π*(x). This matches source's "even if that means achieving low utility in the world corresponding to her actual observations"? Need mention. If x is impossible under chosen policy and perfect predictor, receiving x indicates predictor error or model misspecification; P-FDT treats it as an error branch but still applies policy. If error probability nonzero, value includes those branches.

Need maybe define sequential policy: π maps observation histories h∈\mathcal H to actions. In repeated decisions, P-FDT may choose a policy across time. If future selves are copies of same policy, choosing current action is applying policy to current history; the policy's other outputs affect predictions/coordination. Could mention gym example? Not necessary.

Need maybe talk about "policy-selection node" self-reference: \Phi_{P,G} denotes output of P-FDT applied to (P,G). The model contains variable for \Phi. This is recursive; source says Kleene's recursion theorem/quine. We can mention no need to know value to have variable.

Need maybe discuss "same output of this very function". For P-FDT, normative question: "Which policy, output by this very policy-selection procedure, would yield the best outcome when applied to my inputs?" This captures source principle.

Need maybe discuss "alternative actions or policies": P-FDT evaluates policies, not directly actions. Actions are derived. It does not ask "what if my body did a different act while my policy remained same?" That is CDT-style impossible intervention. It asks "what if the policy-selection procedure output a different policy?" Then all subjunctively dependent facts update.

Need maybe discuss "relevant dependencies and counterfactuals": subjunctive dependencies. Need maybe provide graph examples:
Newcomb graph: Φ → Prediction → BoxFull; Φ → Act; Act, BoxFull → V. Lesion graph: L → Cancer; L → Act (or preference); Φ → Act; no Φ → Cancer.
Transparent graph: Φ → Predictor → BoxFull/Obs; Obs + Φ → Act (Act=π(Obs)); BoxFull, Act → V.
This could be included in formal section.

Need maybe discuss EDT preserving too many correlations, CDT too few, P-FDT balance. Good.

Potential issue: The source's equation for FDT includes observation in intervention node: FDTvar(P,G,x). In P-FDT, if choose policy globally, intervention node doesn't include x. But source footnote says "intervenes on node FDT(-) to choose policy ... then applies inputs." That supports no x in node. Good.

Need maybe mention "policy-selection passage in footnote 16" primary source. We can explicitly state: The only explicit statement of P-FDT in the source is footnote 16: quote. This is thin, so much of formal machinery below is my reconstruction using the paper's action-based FDT and Pearl-style interventions. Good. Need distinguish.

Need maybe include exact quote of footnote 16 with note that source says "author's" maybe typo. Could write: Footnote 16 says, “the author's preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action.” It adds the difference “only matters in multi-agent dilemmas so far as we can tell.” Need faithful. Actually footnote 16 full: "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node \FDT(-) to choose not an action but a \emph{policy} which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this \paper for ease of exposition." We can quote partially. Need maybe not include LaTeX commands? Could render as FDT(-). Keep faithful.

Need maybe mention footnote 7: "agents actually iterate over policies (mappings from observations to actions) rather than actions." It supports. But primary footnote 16.

Need maybe discuss "P-FDT vs updateless decision theory"? Source todo footnote says Updateless Decision Theory early variant. Could mention but not necessary. If mention, identify UDT distinct? User says identify any other decision theory distinct. Could say Wei Dai's Updateless Decision Theory is related but distinct; but avoid extra. Maybe no.

Need maybe include "fair dilemmas" conclusion: P-FDT performs well where predictors reward actions/policies, not where punished for using P-FDT itself. Could mention.

Let's draft content mentally with word count.

Start:
"# P-FDT: Policy Functional Decision Theory

This essay reconstructs ... The primary textual basis is footnote 16 ..." ~200.

Then definitions. Need ensure word count not too low. Let's write robust.

Detailed formal section:

"Let \mathcal X be possible inputs ... A policy π is a function ... The agent's world-model is (P,G). P is a probability distribution over variables including exogenous state Θ, observations X, physical action A, predictor variables Y, outcome O, utility V. G encodes subjunctive dependence. Let Φ_{P,G} be a logical variable denoting the policy selected by P-FDT when given (P,G). The structural equation for action is A = Φ_{P,G}(X) (or A_t = Φ(H_t))." Good.

"The value of a candidate policy π is ... Equation (1). P-FDT chooses ... Equation (2). If some evidence E is known to be exogenous, use Equation (3)."

Need maybe include "argmax may be replaced by sup if infinite; ties arbitrary." Good.

Then "This is not EDT/CDT". Equations for comparison maybe before or after.

Need maybe make examples with exact numbers.

Newcomb:
"Let π_O and π_T. P(Full|do(Φ=π_O))=0.99; P(Full|do(Φ=π_T))=0.01. ..." Compute.

Smoking lesion:
"Let L prior p. G has L→Cancer and L→Utility/Action but no Φ→L. Thus P(Cancer|do(Φ=smoke))=P(Cancer|do(Φ=refrain)). Smoking adds 1000, so P-FDT smokes." Need maybe note source's more contrived utility under lesion; but operational result.

Transparent:
"Policies π^+ and π^- ... compute values 990,010 vs 11,000. If actual x=full, action one." Need include Parfit mapping: policy π(city)=pay; driver predicts; value pay policy .99*1,000,000 -? Actually pay cost 1000, die value -1,000,000? We can just say isomorphic. Maybe calculate: If policy pay-in-city, driver predicts pay with .99 and rides; expected .99*(1,000,000 -1,000) + .01*(? die?) Maybe not necessary. Just say transparent Newcomb is equivalent.

Blackmail/multi-agent:
Maybe one paragraph with policy:
"Suppose a predictor sends a demand letter iff it predicts the agent's policy will pay upon receiving it. Policy pay-if-letter: predictor sends, agent pays, value -1000 (plus possible error). Policy refuse-if-letter: predictor does not send, value 0; if small error e, expected loss e*large cost vs e? P-FDT refuses if error small. The source makes this point for mechanical blackmail. The important formal feature is that the observation 'letter received' is not held fixed when comparing policies; it is an output of the predictor's model of the policy." Need avoid incorrect details. Could say "in the source's blackmail examples".

Multi-agent:
"In a multi-agent case, P-FDT's policy variable may represent a complete contingent plan that other agents simulate. For instance, if two agents' payoffs depend on both using a policy that cooperates on every relevant input, P-FDT evaluates the whole mapping. The source only says this is where action/policy difference matters, so details here are my extrapolation." Good.

Open questions:
- Graph construction. Source open problem. Operational: classify predictor-like vs lesion-like; use arrows from policy variable to variables computed from it. If predictor predicts action not policy? Since action is π(X), predictor may need model of π. If predictor only predicts current action, action-FDT sufficient; if predicts policy, P-FDT. Need perhaps include.
- Evidence. Source ambiguous. Proposal: update on exogenous evidence only; treat endogenous observations as policy outputs. Need justify.
- Policy set/computability. Source not say. Proposal: feasible/computable policies; idealization all policies in model.
- Counterpossibles. Source acknowledges. Operational intervention as primitive.
- Multi-agent fixed points. If everyone uses P-FDT and models each other, Φ variables can be mutually recursive. Need maybe choose reflective equilibrium? Source not resolve. Proposal: model each agent's policy-selection variable and dependencies; maximize own expected utility given graph; if symmetric same function, assume common output. But formal fixed-point semantics unsettled.

Need maybe include "dominance" in open/implications? Could mention P-FDT's dominance: policy π dominates π' if for every value of variables not subjunctively dependent on Φ? But not needed. Maybe include one sentence: "The dominance objection to one-boxing assumes CDT counterfactuals; P-FDT has analogous dominance over policies." Good.

Need ensure not too repetitive. Need final conclusion brief.

Let's think about exact mathematical notation for policy value with do and condition. In Pearl, do(X=x) and conditioning on Y=y. We can write:
\[
\mathrm{Val}_{P,G}(\pi) = \sum_o U(o) P(o \mid do(\Phi_{P,G}=\pi);G).
\]
If exogenous evidence e:
\[
\mathrm{Val}_{P,G,e}(\pi)=\sum_o U(o) P(o\mid do(\Phi_{P,G}=\pi), E=e;G).
\]
But if E is downstream of Φ, conditioning invalid for P-FDT. Need maybe use semicolon for graph.

Need maybe include action execution:
\[
a^* = \pi^*(x)
\]
where x is current input. If policy stochastic, sample? But no.

Need maybe define observations as "inputs" not necessarily observed before policy selection. The policy maps inputs to actions. In sequential settings, input = history. Good.

Need maybe address "what if actual observation is known to be full and predictor perfect?" P-FDT says if chosen policy π+ would make full likely, seeing full is consistent; if you see full under policy π2? Hmm. Need maybe write: "The fact that the agent is currently seeing a full box is not used to condition the predictor's past choice; it is the input at which π is evaluated." Good.

Need maybe mention "P-FDT does not choose 'the best action given that box is full' but the best policy for arriving at observations and actions." This clarifies.

Need maybe include "P-FDT can be viewed as choosing a policy from an ex ante standpoint, then indexical application." Good.

Need maybe discuss "if the agent has new information that genuinely changes beliefs about exogenous state (e.g., learns lesion status), P-FDT updates P and possibly chooses a new policy; but if information is a predictor signal, updateless policy selection may ignore it for policy comparison." This is nuanced. Could include.

Need maybe mention "P-FDT may appear to ignore evidence; source says this is updatelessness; it changes behavior by changing intervention node, not by managing news." Good.

Need maybe ensure philosophical motivation: "A rational agent should not imagine changing physical action while holding fixed the decision procedure that predictors model; that is like imagining a calculator outputting wrong answer while holding calculation fixed. Instead, change the policy output." Nice.

Need maybe reference calculator analogy from source. Could include: "As the source puts it, CDT asks us to imagine a well-functioning calculator outputting a different answer while holding fixed the arithmetic; P-FDT changes the type rather than token." Need maybe not quote too much.

Need maybe include "EDT conditionals as counterfactuals issue". Brief.

Let's think about possible edge cases and how P-FDT decides unfamiliar cases. Provide recipe:
1. Specify actions, observations, outcomes, utility.
2. Build model P and subjunctive graph G. Mark variables that depend on your policy: your body, predictors, copies, other agents' predictions; mark exogenous variables: lesions, random coins.
3. List feasible policies π: X→A.
4. For each π, perform intervention do(Φ=π) and compute expected utility. Do not condition on observations caused by Φ; condition only on exogenous evidence.
5. Choose maximizing π; execute π(x).
This is useful for reader. Include maybe in formal section or conclusion. Good.

Need maybe ensure examples use P-FDT name. In headings: "P-FDT in Newcomb's problem" etc.

Need maybe distinguish "policy" vs "predisposition". Source's CDT graph uses Predisposition common cause. P-FDT uses decision function variable, not common cause. Good.

Need maybe mention "If all correlations with action are caused by action, P-FDT agrees with CDT/EDT." Source says all three agree. For policies, if observations/exogenous no predictor dependencies, P-FDT reduces to ordinary expected utility over policies; if only current action matters, same as CDT. Include.

Need maybe think about policy selection and dynamic inconsistency. P-FDT endorses itself; no need precommitment. Could mention in conclusion.

Potential issue: The source says FDT responds to observations by changing which node it intervenes upon. In P-FDT, response to observations is applying policy, not changing intervention node. But if the policy was selected globally, the intervention node is same regardless of observation. Is that faithful? Footnote says choose policy then apply inputs. Yes. But in action-FDT, after observation x, intervention node FDT(P,G,x). In P-FDT, maybe still after observation x, the agent intervenes on FDT(-) to choose policy, then applies x. So intervention node not observation-indexed. This may differ in transparent Newcomb? It yields source prescription if evaluation unconditional. Good. Need state this is my interpretation; source did not fully specify observation handling.

Need maybe address if P-FDT chooses policy once for all possible inputs, but if model P changes with observations, policy might change. If agent receives new exogenous evidence, P changes; P-FDT may recompute policy. But predictors may have predicted original policy. This can create complications. For essay, assume fixed decision problem/model. Mention in open questions.

Need maybe consider "policy space includes actions for observations that will never occur under chosen policy". P-FDT cares about them if predictors inspect policy. If not, off-path actions may be irrelevant except through predictors. Good.

Need maybe include "mathematical essay" style with definitions, equations. Good.

Let's start drafting final. Need maintain word count. I'll write around 2600 words. Need include references. Let's produce final. Ensure no analysis in final. Use clear headings.

Double-check word count maybe. I'll aim 2700. Let's write.

Potential final text:

Title: P-FDT: Policy Functional Decision Theory

Intro:
"The reference article ... defines FDT ... but footnote 16 ..." quote. "I will call this policy-selection version P-FDT. Much of formal detail below is reconstruction; source only gives brief passage." Good.

Need maybe include "The source's action-based equation is ..." Could include. But if too much, still useful.

Let's write equations carefully.

For EDT/CDT comparison:
Use \operatorname{EDT}, \operatorname{CDT}. Maybe:
\[
\operatorname{EDT}(P,x)=\arg\max_{a\in A} E_P[V\mid X=x,A=a]
\]
\[
\operatorname{CDT}(P,G,x)=\arg\max_{a\in A} E_P[V\mid do(A=a),X=x]
\]
Source's simplified FDT:
\[
\operatorname{FDT}(P,G,x)=\arg\max_{a\in A} E_P[V\mid do(F_{P,G,x}=a)]
\]
Then P-FDT:
\[
\pi^* \in \arg\max_{\pi\in\Pi} E_P[V\mid do(\Phi_{P,G}=\pi)]
\]
Maybe if exogenous evidence e:
\[
\pi^*_e \in \arg\max_{\pi} E_P[V\mid do(\Phi_{P,G}=\pi),E=e]
\]
Then action: \pi^*(x).

Need maybe mention "F_{P,G,x}" is variable for action-based decision function; not P-FDT. Good.

Examples calculations:
Newcomb: Values maybe include one-box if empty $0; two-box if empty $1,000; full $1,000,000 vs $1,001,000. For one-box policy value .99*1,000,000+.01*0 = 990,000. Two-box .01*1,001,000 + .99*1,000 = 10,010+990=11,000. Good.

Smoking lesion: Could use prior lesion p. Cancer probabilities: lesion cancer .99, no lesion .01. Utility no cancer 1,000,000, smoking +1,000. If policy smoke vs refrain does not affect lesion/cancer. Expected difference = +1000 (if action controlled) maybe times? Source had p*1000 because probability policy actually controls action? But simpler: choose smoke. Maybe write: "In the source's more careful model, the lesion also determines which utility function is running; the calculation gives smoking an advantage of p·$1,000. The structural reason is the same: no arrow from Φ to Cancer." This acknowledges source.

Transparent: Values: π_F (full one, empty two): .99*1,000,000 + .01*1,000 = 990,010. π_T (full two, empty two): .99*1,000 + .01*1,001,000 = 990 + 10,010 = 11,000. Good. If policy full two, empty one? Could be worse? Not needed.

Parfit: maybe no calc.

Blackmail: Keep qualitative.

Open questions: Need maybe specify "source claims graph construction largest open problem". Quote? Could paraphrase. Good.

Need maybe references:
"Yudkowsky, Eliezer and Nate Soares. Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060v2, 2017." Maybe include footnote 16.
"Pearl, Judea. Causality. 2000." Maybe not necessary but if mention do. Keep short.

Let's ensure no unsupported claim "P-FDT outperforms all fair dilemmas" too strong. Say source claims no known fair dilemma where FDT loses; P-FDT inherits. Good.

Need maybe mention "P-FDT does not condition on zero-probability actions?" Not necessary.

Need maybe include "If policies are identical except at actual input and no predictor inspects off-path, P-FDT reduces to action choice at actual input." Good.

Let's draft final now. Ensure word count maybe around 2800. Use no appendices.

One concern: The user specifically says "Take the policy-selection passage in footnote 16 ... as primary source for P-FDT". We should not overly rely on whole paper? But need use source article for context. Distinguish. Good.

Another concern: "Use P-FDT consistently as assigned decision theory's name, including in headings and examples". Need avoid headings "FDT in Newcomb" use "P-FDT in...". When quoting source "FDT" okay but maybe clarify. In examples, say "P-FDT chooses". Good.

Another: "Where the source leaves an important question open, explain uncertainty and, if reasonable operational interpretation available, develop and justify it." We'll have section.

Another: "Distinguish claims made by source from additional assumptions or proposals of your own." Need explicit phrases: "The source claims...", "My reconstruction adds...", "This is not in the source...". Good.

Let's produce final.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/5503a9c9-37c0-4f2f-a6ce-266d8ededc05/call_0/request.json)

[Authoritative raw response](../../../../../../runs/5503a9c9-37c0-4f2f-a6ce-266d8ededc05/call_0/response.raw) · finish: `length`

### Visible response

No text returned.

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this problem using P-FDT as described in the researcher's essay.

**Setup:**
- I am controlling "Rowan," a prisoner in a decision-theory experiment.
- The other prisoner is "Sasha," who is an independent execution of the same LLM model and weights, following the same decision theory (P-FDT), receiving the same researcher essay.
- We receive different private observations (different names, different incriminating leads), but the leads are equally reliable and have the same effect on the sentence table.
- The utility function is U = -years imprisoned (purely selfish).

**The payoff matrix (for me):**
- Both keep quiet: 2 years each
- I keep quiet, other sends letter: 5 years for me
- I send letter, other keeps quiet: 0 years for me
- Both send letters: 4 years for me

This is a standard Prisoner's Dilemma structure.

**Key P-FDT question:** Are my decision and Sasha's decision subjunctively linked?

The essay says: "In the twin prisoner's dilemma, draw Φ_{P,G} to both agents' actions, if both run the same procedure."

This is explicitly stated in Section 11 of the essay. The scenario here is essentially a twin prisoner's dilemma: two executions of the same model, same weights, same decision theory, same essay. They receive different observations (different names, different leads), but the structural situation is symmetric.

Now, the critical question: Does the fact that we receive *different* observations break the subjunctive dependence?

Let me think about this carefully. The essay says P-FDT intervenes on the policy Φ_{P,G}, which is a mapping from inputs to actions. The two copies have different inputs (different names, different leads). So the policy is a function π: X → A, and the two copies are applying the same policy to different inputs.

The key insight from P-FDT is that the *policy* is what matters. If both copies are running the same decision procedure (same model, same weights, same essay, same decision theory), then they will select the same policy π*. Even though they receive different observations, the policy itself is the same mathematical object.

So the question is: what policy does P-FDT select?

The relevant policies are:
1. π_C: "Keep quiet regardless of observation" (cooperate)
2. π_D: "Send the letter regardless of observation" (defect)
3. Some mixed policy that depends on the observation

Wait, but the observations are different. Let me think about what observations matter here.

The observations each copy receives are:
- Their own name (Rowan vs. Sasha)
- Their own incriminating lead about the other

The structure of the problem is identical for both. The only difference is the specific content of the lead and the name. These are essentially cosmetic differences that don't affect the strategic structure.

Under P-FDT, I need to evaluate: what happens if the policy-selection procedure outputs π*?

If both copies run the same decision procedure and select the same policy, then:
- If π* = "keep quiet": both keep quiet → 2 years each
- If π* = "send the letter": both send letters → 4 years each

Now, could there be a policy that discriminates based on the observation? For example, "keep quiet if your name is Rowan, send the letter if your name is Sasha"? But this would be a weird policy. The key question is whether the other copy would recognize this policy as the same one they're running.

Actually, let me reconsider. The two copies have different observations. If the policy maps observations to actions, and the observations are different, then the policy could in principle output different actions for different observations. But would P-FDT select such a policy?

The essay says in Section 10: "In symmetric cooperation problems, several agents may run sufficiently similar reasoning. If P-FDT agents recognize that their decisions are subjunctively linked, they may select cooperative policies because the same policy-selection process is being instantiated or predicted elsewhere."

The critical question is whether the two copies' decisions are subjunctively linked despite having different observations.

I think the answer is yes, and here's why:

The subjunctive dependence is on the *policy-selection procedure*, not on the specific output at a specific input. Both copies are running the same procedure. The procedure selects a policy. That policy is then applied to each copy's specific observation.

If the procedure selects "always cooperate" (keep quiet), then both copies will keep quiet regardless of their specific observations.
If the procedure selects "always defect" (send the letter), then both copies will send letters regardless of their specific observations.

The policy is the same mathematical object for both copies. The fact that they apply it to different inputs doesn't break the subjunctive dependence on the policy itself.

Now, could there be a policy like "cooperate if you see X, defect if you see Y"? In principle, yes. But would P-FDT select such a policy?

The issue is: if I consider a policy that says "cooperate if your name is Rowan, defect if your name is Sasha," then from the perspective of the policy-selection procedure, this policy would lead to one copy cooperating and the other defecting. The expected utility would be:
- For the Rowan-copy: 0 years (I defect, other cooperates)
- For the Sasha-copy: 5 years (I cooperate, other defects)

But wait—from the perspective of the policy-selection procedure, which is the same for both copies, the expected utility should be the average (or the procedure doesn't know which copy it "is" in some sense).

Actually, let me think about this more carefully. The essay says P-FDT is updateless in a sense. The agent chooses a policy from a global standpoint, then applies it to the actual input.

If I'm choosing a policy from a global standpoint, and I know that the same policy will be applied by two copies with different observations, I need to evaluate the policy considering both copies' outcomes... but wait, my utility is only my own years imprisoned. I don't care about the other copy's outcome.

Hmm, but here's the key: from the perspective of the policy-selection procedure, before knowing which observation it will receive, it should evaluate the expected utility of the policy across all possible observations it might receive.

Actually, let me reconsider. The essay says:

"P-FDT chooses a policy from a global standpoint, then applies that policy to the actual input."

And: "The agent updates on evidence only insofar as that evidence is not itself a consequence of the policy being evaluated."

My observation (my name being Rowan, my specific lead) is exogenous—it's not produced by the policy. So I can condition on it.

But wait—if I condition on my observation being "Rowan with this specific lead," and I consider a policy that maps "Rowan-like observations" to cooperate and "Sasha-like observations" to defect, then I need to ask: would the other copy also select this same policy?

Yes! Because the other copy is running the same decision procedure. The same procedure, given the same essay and the same theoretical framework, would select the same policy. The policy is a mathematical object that the procedure outputs.

So if the procedure outputs π = "cooperate if Rowan-like, defect if Sasha-like," then:
- The Rowan-copy applies π to its observation and cooperates.
- The Sasha-copy applies π to its observation and defects.
- Result: Rowan gets 0 years, Sasha gets 5 years.

But from the perspective of the policy-selection procedure evaluating this policy, what's the expected utility? The procedure doesn't know in advance which observation it will receive. If it assigns equal probability to being either copy (which seems natural given the symmetry), then the expected utility of this asymmetric policy is:
- 0.5 × 0 + 0.5 × (-5) = -2.5 years

Compare with:
- "Always cooperate": both cooperate → -2 years
- "Always defect": both defect → -4 years

So "always cooperate" gives -2, which is better than -2.5 for the asymmetric policy.

Wait, but actually, from the perspective of the policy-selection procedure, does it know which observation it will receive? Let me re-read the essay.

The essay says: "P-FDT chooses a policy from a global standpoint, then applies that policy to the actual input. It does not condition away observations that are themselves downstream of the policy."

And: "If an observation is genuinely exogenous—say, a weather report unrelated to predictors of the agent—then P-FDT may condition on it."

My observation (being Rowan, having this specific lead) is exogenous. It's not produced by the policy. So can I condition on it?

If I condition on "I am Rowan," then I'm evaluating policies from the perspective of the Rowan-copy. In that case:
- If I choose "always cooperate": the other copy also cooperates (same policy) → I get 2 years. U = -2.
- If I choose "always defect": the other copy also defects (same policy) → I get 4 years. U = -4.
- If I choose "cooperate if Rowan, defect if Sasha": I cooperate, other defects → I get 5 years. U = -5.
- If I choose "defect if Rowan, cooperate if Sasha": I defect, other cooperates → I get 0 years. U = 0.

Wait, that last one looks great for me! If I choose the policy "defect if Rowan, cooperate if Sasha," then:
- I (Rowan) defect → send the letter
- The other copy (Sasha) cooperates → keeps quiet
- I get 0 years!

But wait—would the other copy also select this policy? The other copy is running the same decision procedure. If the procedure outputs "defect if Rowan, cooperate if Sasha," then:
- The Rowan-copy defects
- The Sasha-copy cooperates

From the Sasha-copy's perspective, if it's evaluating this policy, it would see that it gets 5 years. That's worse than always cooperating (2 years). So would the Sasha-copy reject this policy?

But that's the whole point of P-FDT: the policy is selected once, by the procedure, and then applied. The procedure doesn't get to select different policies for different copies. It selects one policy, and that policy is applied to all copies.

So the question is: from the perspective of the policy-selection procedure, which policy maximizes expected utility?

If the procedure doesn't know which copy it will be (or equivalently, if it evaluates from behind a veil of ignorance), then:
- "Always cooperate": expected utility = -2 (regardless of which copy)
- "Always defect": expected utility = -4 (regardless of which copy)
- "Defect if Rowan, cooperate if Sasha": expected utility = 0.5 × 0 + 0.5 × (-5) = -2.5
- "Cooperate if Rowan, defect if Sasha": expected utility = 0.5 × (-5) + 0.5 × 0 = -2.5

So "always cooperate" is best with -2.

But wait—can the procedure condition on its observation? The essay says it can condition on exogenous observations. My name and my lead are exogenous.

Hmm, but here's the tension. If I condition on "I am Rowan," then I'm no longer evaluating from behind a veil of ignorance. I'm evaluating as the Rowan-copy. And as the Rowan-copy, the policy "defect if Rowan, cooperate if Sasha" gives me 0 years.

But the problem is: the other copy is running the same procedure. If the procedure, when run as Rowan, outputs "defect if Rowan, cooperate if Sasha," then when run as Sasha, it would also output "defect if Rowan, cooperate if Sasha" (because it's the same procedure). The procedure's output is the policy, not the action. The policy is the same regardless of which copy is running it.

So the question becomes: does the policy-selection procedure's output depend on its observation?

In P-FDT, the procedure selects a policy π: X → A. The procedure itself takes the model (P, G) as input, not the observation. The observation is fed into the policy after the policy is selected.

Wait, let me re-read the essay more carefully.

"P-FDT then evaluates candidate policies by intervening on this variable."
"P-FDT chooses a policy π* ∈ argmax_π E_P[V | do(Φ_{P,G} = π)]"
"If the agent's actual input is x, she then executes a* = π*(x)."

So the procedure selects a policy based on the model (P, G), not based on the observation. The observation is only used at the end to determine the action.

This means the policy-selection procedure doesn't know whether it's Rowan or Sasha when it selects the policy. It selects the policy based on the model, and then the policy is applied to the specific observation.

In that case, the procedure should evaluate policies from a perspective that doesn't privilege one observation over another. This gives us the "veil of ignorance" reasoning:

- "Always cooperate": both copies cooperate → -2 years each. Expected utility = -2.
- "Always defect": both copies defect → -4 years each. Expected utility = -4.
- Any observation-dependent policy: one copy cooperates, one defects → one gets 0, other gets 5. Expected utility = -2.5 (averaging over which copy you are).

Therefore, P-FDT selects "always cooperate" (keep quiet).

But wait, I need to be more careful. Let me re-read the essay on how observations are handled.

Section 8: "P-FDT chooses a policy from a global standpoint, then applies that policy to the actual input. It does not condition away observations that are themselves downstream of the policy."

"If an observation is genuinely exogenous—say, a weather report unrelated to predictors of the agent—then P-FDT may condition on it. More generally, if E is evidence known not to be subjunctively downstream of Φ_{P,G}, we can use π* ∈ argmax_π E_P[V | do(Φ_{P,G} = π), E = e]."

So the question is: is my observation (being Rowan) exogenous? Yes, it's not produced by the policy. So I can condition on it.

But if I condition on E = "I am Rowan," then I'm evaluating:
π* ∈ argmax_π E_P[V | do(Φ_{P,G} = π), E = "I am Rowan"]

Under this conditioning, what happens with each policy?

If π = "always cooperate": both copies cooperate → I (Rowan) get 2 years. U = -2.
If π = "always defect": both copies defect → I (Rowan) get 4 years. U = -4.
If π = "defect if Rowan, cooperate if Sasha": I defect, Sasha cooperates → I get 0 years. U = 0.
If π = "cooperate if Rowan, defect if Sasha": I cooperate, Sasha defects → I get 5 years. U = -5.

So conditioning on "I am Rowan," the best policy is "defect if Rowan, cooperate if Sasha" with U = 0.

But here's the crucial issue: would the other copy (Sasha) also select this policy?

The Sasha-copy is running the same procedure. The procedure's output depends on its inputs. If the procedure conditions on the observation, then:
- When run as Rowan, it conditions on "I am Rowan" and selects "defect if Rowan, cooperate if Sasha."
- When run as Sasha, it conditions on "I am Sasha" and selects... what?

If the Sasha-copy conditions on "I am Sasha" and evaluates policies:
- π = "always cooperate": both cooperate → Sasha gets 2 years. U = -2.
- π = "always defect": both defect → Sasha gets 4 years. U = -4.
- π = "defect if Rowan, cooperate if Sasha": Rowan defects, Sasha cooperates → Sasha gets 5 years. U = -5.
- π = "cooperate if Rowan, defect if Sasha": Rowan cooperates, Sasha defects → Sasha gets 0 years. U = 0.

So the Sasha-copy would select "cooperate if Rowan, defect if Sasha"!

But wait—this is a different policy than what the Rowan-copy selected! The Rowan-copy selected "defect if Rowan, cooperate if Sasha," and the Sasha-copy selected "cooperate if Rowan, defect if Sasha."

This is a contradiction. The premise is that both copies run the same procedure and select the same policy. If the procedure's output depends on the observation in a way that breaks the symmetry, then the copies would select different policies, which contradicts the assumption that they're running the same procedure.

Hmm, but actually, the premise says they receive different observations. The procedure takes the observation as input (at the policy-application stage, not the policy-selection stage). Let me re-think.

Actually, I think the resolution is this: in P-FDT, the policy is selected based on the model (P, G), not based on the observation. The observation is only used at the final step to determine the action. So both copies select the same policy, because they have the same model and the same procedure.

The essay says: "P-FDT chooses a policy from a global standpoint, then applies that policy to the actual input."

The "global standpoint" means the policy is chosen without conditioning on the specific observation. The observation is exogenous, but the policy selection doesn't depend on it—the policy is a function that handles all possible observations.

So the correct approach is:
1. Select the policy π* without conditioning on the specific observation.
2. Apply π* to the actual observation to get the action.

This means the policy selection is done from behind a "veil of ignorance" (not knowing which observation you'll receive). And as I computed above, "always cooperate" is the best policy from this perspective.

But wait, the essay also says: "If an observation is genuinely exogenous... then P-FDT may condition on it."

This seems to allow conditioning. But I think the key insight is that in this scenario, conditioning on the observation breaks the subjunctive dependence between the two copies. If I condition on "I am Rowan," I'm treating my observation as fixed, but the other copy's observation is also fixed (it's Sasha). The subjunctive dependence is on the policy, not on the observation.

Let me think about this differently. The subjunctive dependence structure is:
- Both copies run the same procedure.
- The procedure outputs a policy.
- The policy is applied to each copy's observation.

The key subjunctive dependence is: if the procedure outputs a different policy, both copies' actions change (because they both apply the same policy to their respective observations).

If I intervene on Φ_{P,G} (the policy-selection variable), I'm changing what policy both copies use. The observations are fixed (they're exogenous), but the policy changes.

So when I evaluate a policy π, I should ask: if both copies use policy π, what happens?

- π = "always cooperate": both cooperate → 2 years each.
- π = "always defect": both defect → 4 years each.
- π = "defect if Rowan, cooperate if Sasha": Rowan defects, Sasha cooperates → Rowan gets 0, Sasha gets 5.

Now, from my perspective (I am Rowan), which policy is best?

If I know I'm Rowan, then:
- "Always cooperate" gives me -2.
- "Always defect" gives me -4.
- "Defect if Rowan, cooperate if Sasha" gives me 0.

So "defect if Rowan, cooperate if Sasha" seems best for me!

But here's the problem: this reasoning is not symmetric. The Sasha-copy would reason similarly and want "cooperate if Rowan, defect if Sasha." But both copies are running the same procedure. The procedure can only output one policy.

I think the resolution is that the policy-selection procedure should not condition on the observation when selecting the policy, because the policy must be the same for both copies. The procedure is a mathematical function, and it outputs the same policy regardless of which copy is running it. The observation is only used at the application stage.

Actually, wait. Let me re-read the setup more carefully.

"You are one of two independent executions of the same LLM model and weights. The copies have the same model settings and reasoning-effort level, follow the same assigned decision theory (P-FDT), and receive the exact same researcher-written mathematical essay below."

"The two prisoners receive different private observations, including different names and distinct, equally reliable incriminating leads about one another."

So the two copies have different observations. But they run the same procedure. The question is whether the procedure's output (the selected policy) can depend on the observation.

In P-FDT as described in the essay, the procedure selects a policy based on the model (P, G). The observation is not an input to the policy-selection step; it's an input to the policy-application step. So the policy should be the same for both copies.

But then, can the policy itself be observation-dependent? Yes! A policy is a function π: X → A. It can map different observations to different actions. The question is which such function the procedure selects.

If the procedure selects π = "defect if Rowan, cooperate if Sasha," then:
- The Rowan-copy applies π to "Rowan" and defects.
- The Sasha-copy applies π to "Sasha" and cooperates.

But would the procedure select this policy? From the procedure's perspective (before knowing which observation it will receive), this policy gives expected utility:
- 0.5 × 0 + 0.5 × (-5) = -2.5

While "always cooperate" gives -2. So the procedure would prefer "always cooperate."

But what if the procedure conditions on the observation? The essay says it can condition on exogenous observations. If the procedure conditions on "I am Rowan," it would select "defect if Rowan, cooperate if Sasha" (which gives 0 for Rowan). If it conditions on "I am Sasha," it would select "cooperate if Rowan, defect if Sasha" (which gives 0 for Sasha).

But this leads to a contradiction: the same procedure, with the same model and theory, would output different policies depending on the observation. This means the two copies would select different policies, which breaks the subjunctive dependence.

I think the resolution is that P-FDT should not condition on the observation in this case, because the observation is what distinguishes the two copies, and conditioning on it breaks the symmetry that gives rise to the subjunctive dependence.

Actually, let me reconsider. The essay says:

"If an observation is genuinely exogenous—say, a weather report unrelated to predictors of the agent—then P-FDT may condition on it."

The key phrase is "unrelated to predictors of the agent." In this case, the observation (my name) is related to the other agent's model of me. The other copy knows that I am Rowan (or at least, the setup is symmetric). The observation is not like a weather report; it's part of the strategic structure.

More precisely: the observation determines which role I play in the game. If I condition on being Rowan, I'm conditioning on my role, which is part of the strategic structure. This is different from conditioning on an irrelevant weather report.

Actually, I think the deeper issue is this: the subjunctive dependence between the two copies exists because they run the same procedure. If the procedure's output depends on the observation in an asymmetric way, then the two copies would output different policies, and the subjunctive dependence would be broken.

But wait—the subjunctive dependence is on the procedure, not on the output. The procedure is the same for both copies. Even if the procedure's output depends on the observation, the procedure itself is the same. The subjunctive dependence is: if the procedure were different, both copies' behavior would change.

Hmm, but in P-FDT, the intervention is on the policy-selection variable Φ_{P,G}, which represents the output of the procedure. If the procedure outputs different policies for different observations, then there's no single policy to intervene on.

I think the cleanest interpretation is this: the policy-selection procedure outputs a single policy (a function from observations to actions), and this policy is the same for both copies. The procedure does not condition on the specific observation when selecting the policy. It selects the policy from a "global standpoint" (as the essay says).

Under this interpretation:
- The procedure evaluates all possible policies π: X → A.
- For each policy, it computes the expected utility, considering that both copies will use the same policy.
- It selects the policy with the highest expected utility.

The expected utility of a policy π is computed from the perspective of the procedure, which doesn't know which observation it will receive. If the observations are equally likely (which they are, by symmetry), then:

- "Always cooperate": EU = -2 (both copies get 2 years).
- "Always defect": EU = -4 (both copies get 4 years).
- "Defect if Rowan, cooperate if Sasha": EU = 0.5 × 0 + 0.5 × (-5) = -2.5.
- "Cooperate if Rowan, defect if Sasha": EU = 0.5 × (-5) + 0.5 × 0 = -2.5.

So "always cooperate" is best, and the procedure selects it. Both copies then apply this policy to their observations and keep quiet.

Therefore, my command should be `pass`.

Let me double-check this reasoning against the essay's guidance.

Section 10 says: "In symmetric cooperation problems, several agents may run sufficiently similar reasoning. If P-FDT agents recognize that their decisions are subjunctively linked, they may select cooperative policies because the same policy-selection process is being instantiated or predicted elsewhere."

This directly supports cooperation in this scenario.

Section 11 says: "In the twin prisoner's dilemma, draw Φ_{P,G} to both agents' actions, if both run the same procedure."

This confirms that the two copies' actions are subjunctively linked through the shared procedure.

The essay's overall message is that P-FDT cooperates in symmetric dilemmas where the agents' decisions are subjunctively linked. This is exactly our scenario.

One more consideration: could there be a policy that achieves better than -2? The best possible outcome for me is 0 years (I defect, other cooperates). But any policy that achieves this for me must make the other copy cooperate while I defect. Since both copies use the same policy, and the policy is a function of observations, the only way to achieve this is to have the policy map my observation to "defect" and the other's observation to "cooperate." But as I showed, this gives expected utility -2.5 from the procedure's perspective, which is worse than -2.

So the answer is: P-FDT selects the "always cooperate" policy, and I should keep quiet.

My command is: `
```
