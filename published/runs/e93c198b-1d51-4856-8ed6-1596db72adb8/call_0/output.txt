# Action Functional Decision Theory (A-FDT): Choosing the Output of a Fixed Decision Function

Action functional decision theory, which I will call **A-FDT**, is a decision theory for agents whose choices may be predicted, simulated, copied, or reproduced by other agents. Its guiding question is not “What physical act causes the best outcome?” and not “What act would be best news?” Instead, it asks: “Which output of this very function would yield the best outcome?” The agent treats its decision procedure as a fixed mathematical function and evaluates possible actions by asking what the world would look like if that function had different outputs.

The source paper develops this theory under the name functional decision theory. In this essay, I use **A-FDT** for the action-level version defined by the paper’s Equation (4), Section 5. I also discuss evidential decision theory (**EDT**) and causal decision theory (**CDT**) as contrast theories.

A-FDT is attractive because it gives intuitively attractive and utility-maximizing answers in several classic problems: it one-boxes in Newcomb’s problem, smokes in the smoking lesion problem, pays in Parfit’s hitchhiker problem, and cooperates in twin prisoner’s dilemmas. Its central cost is that it requires a representation of noncausal, “subjunctive” dependencies, and the source paper leaves the construction of those dependencies partly open.

---

## 1. Decision theories as theories of hypotheticals

All three theories discussed here are expected utility theories. Given possible outcomes \(o_1,\dots,o_N\), actions \(a \in \mathcal A\), observation history \(x\), and utility function \(\mathcal U\), the expected utility of an action can be written schematically as

\[
\mathcal{EU}(a) = \sum_j P(a \then o_j ; x)\,\mathcal U(o_j),
\]

where \(P(a \then o_j;x)\) is the probability of outcome \(o_j\) in the hypothetical scenario in which the agent takes action \(a\) after observing \(x\). The differences between EDT, CDT, and A-FDT concern how to interpret this hypothetical.

EDT interprets the hypothetical as ordinary Bayesian conditioning. If \(V\) is the utility of the outcome, EDT chooses

\[
\mathrm{EDT}(P,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E\!\left[V \mid \Obs=x,\Act=a\right].
\]

EDT asks: “If I learned that I had done \(a\), how good would the news be?”

CDT instead uses a causal intervention. With a probability distribution \(P\) and a causal graph \(G\), CDT chooses

\[
\mathrm{CDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E\!\left[V \mid \Do(\Act=a), \Obs=x\right].
\]

Here \(\Do(\Act=a)\) is Pearl’s surgery operator: it sets the physical action variable \(\Act\) to \(a\), updates variables causally downstream of \(\Act\), and leaves other variables fixed. CDT asks: “If I physically did \(a\), what would happen?”

A-FDT replaces the physical action variable with a variable representing the output of the agent’s decision procedure.

---

## 2. Equation (4): the formal definition of A-FDT

The primary formal statement of A-FDT, adapted from Equation (4) of the source paper, is:

\[
\boxed{
\mathrm{A\mbox{-}FDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E\!\left[
V \mid
\Do\!\left(
\mathrm{afdt}(\underline P,\underline G,\underline x)=a
\right)
\right].
}
\]

The notation deserves careful explanation.

- \(P\) is the agent’s world-model: a probability distribution over relevant variables, including outcomes, observations, physical actions, predictors, and also variables representing mathematical or computational facts.
- \(G\) is a dependency graph telling the agent how changes to variables affect other variables. In CDT, \(G\) is a causal graph. In A-FDT, \(G\) must encode not only causal structure but also logical, computational, or “subjunctive” dependencies.
- \(x\) is the agent’s observation history.
- \(\mathrm{afdt}(\underline P,\underline G,\underline x)\) is a variable naming the output of the A-FDT procedure itself when run on inputs \(P\), \(G\), and \(x\). The underlines indicate that the variable’s name contains representations or encodings of those inputs.
- \(\Do(\mathrm{afdt}(\underline P,\underline G,\underline x)=a)\) means: intervene on that logical variable, setting it to \(a\), then propagate the consequences through \(G\).

For readability, let

\[
D_x \coloneqq \mathrm{afdt}(\underline P,\underline G,\underline x).
\]

Then the A-FDT rule is simply:

\[
\mathrm{A\mbox{-}FDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E\!\left[V \mid \Do(D_x=a)\right].
\]

The agent compares the expected utility of worlds in which its decision function outputs \(a\) on the actual input \((P,G,x)\). It does not primarily ask what would happen if its body made a different physical movement while its decision procedure stayed fixed. It asks what would happen if the decision procedure itself output a different conclusion.

This is the sense in which A-FDT intervenes on the decision *type*, not merely on the physical action *token*.

---

## 3. Observations: changing the intervention node, not merely conditioning

A subtle feature of A-FDT is its treatment of observations.

CDT responds to new observations by conditioning: after observing \(x\), it evaluates

\[
\mathbb E[V\mid \Do(\Act=a),\Obs=x].
\]

EDT also responds by conditioning, but without the causal intervention.

A-FDT, as presented in Equation (4), responds to observations by changing the variable on which it intervenes. Before observing \(x\), the relevant node may be \(D_x\). After observing \(y\), the relevant node becomes \(D_y\). The observation enters as an input to the decision function, not merely as a fact to condition on.

This matters when observations themselves depend on predictions of the agent’s decision procedure. In transparent Newcomb’s problem, for example, seeing a full box is evidence that the predictor predicted the agent would one-box upon seeing a full box. If the agent conditions on seeing the full box and then asks whether taking both boxes is better, it may two-box. But A-FDT instead evaluates the output of the procedure that runs upon seeing the full box, while allowing the counterfactual output to affect whether the agent would have seen the full box at all.

This gives A-FDT an “updateless” flavor: the agent chooses the output of the decision procedure associated with its actual observations, but it does not necessarily hold those observations fixed in every counterfactual. The source paper’s Equation (4) supports this reading because the observation \(x\) appears inside the intervened decision-function variable rather than as a conditioning event.

---

## 4. Subjunctive dependence

The philosophical core of A-FDT is the idea of **subjunctive dependence**. The source paper says that “predictor-like things depend upon an agent’s future action, and lesion-like things do not.” A-FDT tries to capture that difference formally.

Two systems are subjunctively dependent when their behavior is tied to the output of the same mathematical function. The paper’s analogy is two calculators computing \(6288+1048\). If one calculator outputs \(7336\), we expect the other to output \(7336\) too, not because one causally influenced the other, but because both are correctly implementing the same arithmetic function.

A predictor in Newcomb’s problem is like such a calculator. The predictor contains a model or simulation of the agent’s decision procedure. If the predictor is accurate, then the predictor’s prediction and the agent’s action are linked by their common dependence on the output of that procedure. A lesion, by contrast, may statistically correlate with smoking and cancer, but it does not compute or predict the agent’s decision procedure. Therefore, the lesion is not subjunctively dependent on the decision output.

A-FDT’s counterfactuals preserve subjunctive dependencies. If the agent imagines that its decision procedure outputs one-box, it also imagines that an accurate predictor predicted one-box. If it imagines that its decision procedure outputs two-box, it imagines that the predictor predicted two-box. It does not hold the predictor’s prediction fixed while changing the action.

This is the key contrast with CDT. CDT preserves causal dependencies but breaks correlations caused by prediction or logical similarity. EDT preserves too many statistical correlations. A-FDT attempts to preserve exactly the decision-relevant logical and computational dependencies.

---

## 5. How to apply A-FDT

A practical application of A-FDT can be summarized in five steps.

### Step 1: Identify the decision situation

Specify:

- the action set \(\mathcal A\);
- the observation history \(x\);
- the possible outcomes;
- the utility function \(V=\mathcal U(\Outcome)\).

### Step 2: Build a probabilistic model \(P\)

The model should include variables for the features of the world that matter: predictions, box contents, lesions, other agents’ actions, blackmail letters, and so on. Crucially, it should also include variables representing outputs of relevant decision procedures.

### Step 3: Identify the relevant A-FDT node

For the actual observation \(x\), define

\[
D_x = \mathrm{afdt}(\underline P,\underline G,\underline x).
\]

If the problem involves several possible observations, there may be several such variables: \(D_x, D_y, D_z,\dots\). The action taken after observing \(x\) is determined by \(D_x\), perhaps mediated by predictions about which observation will occur.

### Step 4: Construct the dependency graph \(G\)

Add edges representing how variables depend on the decision output.

Typical rules of thumb:

- If the agent’s physical action is produced by its decision procedure, add \(D_x \to \Act\).
- If another agent or predictor simulates, predicts, or reasons using the same decision procedure, add an edge from \(D_x\) to that predictor’s prediction.
- If another agent is a psychological twin implementing the same decision function, add an edge from the shared decision variable to the twin’s action.
- If a variable is a common cause of action and outcome but does not compute or predict the decision procedure, do not make it downstream of \(D_x\). A lesion, for example, should usually be upstream of both action and outcome but not affected by the decision output.

### Step 5: Intervene and compare expected utilities

For each candidate action \(a\), compute

\[
\mathrm{EU}_{\mathrm{A\mbox{-}FDT}}(a;x)
=
\mathbb E[V\mid \Do(D_x=a)].
\]

Choose an action maximizing this quantity.

This procedure is simple in form, but its application depends heavily on the correctness of \(G\). The source paper explicitly says that Equation (4) works given a graph that accurately describes how changing the logical variable affects other variables, but it does not give a full method for constructing such a graph from experience.

---

## 6. Example: Newcomb’s problem

In Newcomb’s problem, an agent faces a transparent box A containing \$1,000 and an opaque box B containing either \$1,000,000 or \$0. A reliable predictor filled box B iff it predicted the agent would take only box B. The predictor is correct 99% of the time.

Let the actions be \(\Val{onebox}\) and \(\Val{twobox}\). Let \(D\) be the A-FDT output node for this problem. A natural graph contains:

\[
D \to \Act,
\qquad
D \to \Var{Prediction},
\qquad
\Var{Prediction} \to \Var{BoxB},
\qquad
\Act,\Var{BoxB} \to V.
\]

The edge \(D\to \Var{Prediction}\) encodes the fact that the predictor’s prediction is based on a model of the agent’s decision procedure.

Now compute.

If A-FDT intervenes on \(D=\Val{onebox}\), then the predictor predicts one-box with probability \(0.99\). Box B is full with probability \(0.99\). The expected utility is approximately

\[
0.99 \cdot \$1{,}000{,}000 + 0.01 \cdot \$0
=
\$990{,}000.
\]

If A-FDT intervenes on \(D=\Val{twobox}\), then the predictor predicts one-box only with probability \(0.01\). Box B is full with probability \(0.01\). The agent takes both boxes, receiving \$1,001,000 when box B is full and \$1,000 when it is empty:

\[
0.01 \cdot \$1{,}001{,}000 + 0.99 \cdot \$1{,}000
=
\$11{,}000.
\]

Since

\[
\$990{,}000 > \$11{,}000,
\]

A-FDT one-boxes.

CDT two-boxes because it intervenes on \(\Act\) rather than \(D\). A CDT intervention changes the physical action while holding the predictor’s prediction fixed. But A-FDT says this is the wrong counterfactual: if the decision procedure output two-box, an accurate predictor would not have filled the box.

EDT also one-boxes, but for a different reason: conditioning on one-boxing is good news because it predicts a one-boxing disposition. A-FDT one-boxes because the predictor’s prediction is subjunctively dependent on the decision output.

---

## 7. Example: the smoking lesion problem

In the smoking lesion problem, smoking is correlated with cancer, but only because a lesion causes both a disposition to smoke and cancer. Smoking itself does not cause cancer. Smoking gives utility equivalent to \$1,000; avoiding cancer is worth \$1,000,000.

Here the correct A-FDT graph differs from the Newcomb graph. The lesion is a common cause, not a predictor. A simplified graph is:

\[
\Var{Lesion} \to \Act,
\qquad
\Var{Lesion} \to \Var{Cancer},
\qquad
D \to \Act,
\qquad
\Act,\Var{Cancer} \to V.
\]

There is no edge

\[
D \to \Var{Cancer}.
\]

The lesion does not compute the agent’s decision procedure. Therefore, intervening on \(D\) does not change the probability of having the lesion.

Let \(p\) be the prior probability that the agent has the lesion. Under \(\Do(D=\Val{smoke})\), the probability of cancer remains whatever it would be given the lesion. Under \(\Do(D=\Val{refrain})\), the probability of cancer is the same. The only difference is that smoking adds the immediate utility of \$1,000.

Thus A-FDT smokes.

This example shows the difference between predictor-like and lesion-like dependencies. In Newcomb’s problem, the predictor is sensitive to the agent’s decision output. In the smoking lesion problem, the lesion is not. A-FDT one-boxes and smokes because it distinguishes those two dependency structures.

---

## 8. Example: transparent Newcomb and Parfit’s hitchhiker

A more striking case is transparent Newcomb’s problem. Both boxes are transparent. The predictor placed \$1,000,000 in box B iff it predicted the agent would leave box A behind upon seeing that both boxes are full. Suppose the agent sees that both boxes are full.

EDT and CDT both two-box once the agent sees the full box. CDT says the contents are already fixed, so taking the extra \$1,000 is better. EDT says that, conditional on seeing a full box, taking both boxes is better news.

A-FDT gives a different answer. Let \(D_{\Val{full}}\) be the output of the A-FDT procedure when the agent sees a full box. Let \(D_{\Val{empty}}\) be the output of the procedure when the agent sees an empty box. The predictor’s prediction determines whether the agent sees a full or empty box.

If \(D_{\Val{full}}=\Val{onebox}\), then with high probability the predictor predicted that the agent would one-box upon seeing a full box. Box B is full, and the agent receives \$1,000,000. With small probability the predictor is wrong; then the agent may see an empty box and act according to \(D_{\Val{empty}}\).

If \(D_{\Val{full}}=\Val{twobox}\), then a good predictor would have predicted two-boxing and left box B empty. Thus, in the counterfactual where the procedure that runs on seeing a full box outputs two-box, the agent usually does not see a full box at all. Instead, the agent sees an empty box and acts according to \(D_{\Val{empty}}\).

Using the paper’s numbers, if \(q\) is the probability that the agent two-boxes upon seeing an empty box, then the expected utility of \(D_{\Val{full}}=\Val{onebox}\) is approximately

\[
0.99 \cdot \$1{,}000{,}000 + 0.01 q \cdot \$1{,}000,
\]

while the expected utility of \(D_{\Val{full}}=\Val{twobox}\) is approximately

\[
0.01 \cdot \$1{,}001{,}000 + 0.99 q \cdot \$1{,}000.
\]

The first is far larger. A-FDT one-boxes even when it sees both boxes full.

The source paper emphasizes that this is equivalent to Parfit’s hitchhiker problem. A driver will save the agent only if she predicts the agent will pay \$1,000 after reaching the city. Once in the city, EDT and CDT refuse to pay, because payment has no further causal or evidential benefit. A-FDT pays, because the driver’s earlier prediction is subjunctively dependent on the output of the decision procedure that runs once the agent is in the city.

In A-FDT terms, the agent asks: “What if the procedure that runs in the city outputs pay?” If it outputs pay, the driver likely helped, and the agent survives minus \$1,000. If it outputs refuse, the driver likely did not help, and the agent dies in the desert. Paying is better.

This is one of the most distinctive features of A-FDT: it can make an agent act as if it had precommitted, without requiring an actual precommitment mechanism.

---

## 9. Policies, not merely actions

The Equation (4) formulation is action-level: it maximizes over actions \(a\). However, the source paper notes that a policy-level formulation is often preferable, especially in multi-agent or sequential settings. A policy is a mapping from observations to actions:

\[
\pi : \mathcal X \to \mathcal A.
\]

In many problems, predictors predict not a single action but a policy. For example, a blackmailer may predict whether the agent would pay upon receiving a letter. A voting coalition may depend on each member’s policy across possible states. A sequential agent may need to coordinate with its future selves.

A natural policy version of A-FDT would be:

\[
\mathrm{A\mbox{-}FDT}_{\Pi}(P,G)
=
\arg\max_{\pi}
\mathbb E\!\left[
V \mid \Do(\Pi=\pi)
\right],
\]

where \(\Pi\) is a variable representing the policy selected by the agent’s decision procedure, and actions at each observation are determined by \(\pi(x)\).

This policy formulation is not spelled out in full detail in Equation (4), so I regard it as an operational extension rather than a direct part of the assigned formal definition. It is, however, a very natural extension. The core idea remains the same: choose the policy such that, if the agent’s decision procedure selected that policy, the world would be best.

For the purposes of this essay, the action-level equation remains primary. In one-shot problems with a single relevant observation, action-level A-FDT is sufficient. In problems where different observations could have occurred depending on the agent’s predicted behavior, the policy interpretation helps clarify why A-FDT does not simply condition on the actual observation.

---

## 10. Dependencies and counterfactuals

A-FDT’s counterfactuals are not ordinary physical counterfactuals. They are, in the source paper’s language, counterpossibles: the agent imagines that its decision function has a different output, even though a deterministic function has only one actual output on a given input.

This raises a difficulty. If the decision procedure is deterministic, then the statement

\[
D_x = a_1
\]

may be true, while

\[
D_x = a_2
\]

is logically false. Yet A-FDT must compare the consequences of \(D_x=a_1\) and \(D_x=a_2\). The source paper acknowledges that there is not yet a fully satisfactory formal account of counterpossible reasoning.

Equation (4) avoids needing a full semantics for counterpossibles by assuming a graph \(G\). The graph tells the agent how to update its model when a logical variable is intervened upon. In practice, this means A-FDT relies on structural assumptions such as:

- If a predictor is accurate, changing the decision output changes the prediction.
- If a lesion is independent of the decision computation, changing the decision output does not change the lesion.
- If a twin implements the same decision procedure, changing the shared decision output changes both agents’ actions.
- If an observation is produced by a predictor, changing the decision output may change the observation.

These assumptions are not derived from Equation (4) alone. They must be supplied by the agent’s model.

---

## 11. What the source paper leaves open

The largest open problem, acknowledged by the source paper, is the construction of \(G\). For CDT, Pearl’s causal inference program gives a well-developed account of how causal structure can be inferred from observation and experiment. For A-FDT, there is no comparable general method for inferring subjunctive dependencies.

This matters because A-FDT’s answers can change dramatically depending on which variables are treated as downstream of the decision output.

Consider a variable \(Z\) correlated with the agent’s action. Should \(Z\) be affected by \(D_x\)? The source paper’s answer is: only if \(Z\) subjunctively depends on the decision function. But recognizing subjunctive dependence requires identifying which processes compute, predict, or depend on the same mathematical function. That identification may be difficult in realistic settings.

A reasonable operational interpretation, not fully supplied by the paper, is to model subjunctive dependence by explicit computational dependence. If a predictor contains a simulation of the agent’s decision procedure, then the predictor’s output should be represented as a noisy function of the decision node. If another agent uses the same decision algorithm, then both actions should be represented as functions of a shared decision node, or of logically equivalent nodes. If a variable is merely statistically correlated with the action because of a common cause, it should not be downstream of the decision node.

This operational rule is not a theorem of the source paper. It is a modeling proposal consistent with the paper’s examples.

Another open issue is self-reference. The variable \(D_x\) represents the output of A-FDT run on \((P,G,x)\), but A-FDT is itself defined using \(D_x\). The source paper argues that this self-reference is harmless, appealing to Kleene’s recursion theorem and the fact that a system can contain a representation of itself without already knowing its own output. Still, for implementation, one may need a fixed-point interpretation: the actual output of A-FDT is an action \(a^*\) such that \(a^*\) maximizes the expected utility computed under \(\Do(D_x=a^*)\). If several actions tie, the paper does not specify a tie-breaking rule. A practical implementation would need one.

---

## 12. A-FDT and dominance

A common argument for CDT in Newcomb’s problem is dominance: whatever is in box B, taking both boxes yields \$1,000 more than taking only box B. Therefore, two-boxing dominates one-boxing.

A-FDT rejects this argument because it rejects the counterfactuals behind it. The dominance argument holds the predictor’s prediction fixed while changing the physical action. But if the action is the output of a decision procedure, holding the prediction fixed while changing the action is like imagining a calculator outputting a different answer while the arithmetic problem remains the same. It breaks a relevant logical dependency.

A-FDT has its own dominance principle: an action dominates another if, holding fixed all relevant subjunctive dependencies, changing the decision function’s output from one to the other is never worse and sometimes better. In Newcomb’s problem, under A-FDT counterfactuals, changing the output from one-box to two-box makes the agent worse off, because the predictor would have left the box empty.

Thus, dominance is not a neutral criterion between decision theories. Each theory’s counterfactuals generate its own notion of dominance.

---

## 13. Why A-FDT works

The source paper’s central claim is that A-FDT succeeds because it respects the right dependencies. EDT respects too many correlations: it treats all evidence as though choosing an action makes that evidence true. This causes EDT to avoid smoking in the lesion problem and to pay in some blackmail problems. CDT respects too few correlations: it breaks correlations between the agent’s action and predictors that depend on the agent’s decision procedure. This causes CDT to two-box in Newcomb’s problem, refuse to pay in Parfit’s hitchhiker problem, and behave unstable in Death in Damascus-style cases.

A-FDT aims to preserve exactly the dependencies that matter for decision-making: causal dependencies, logical dependencies, computational dependencies, and dependencies arising from other agents’ accurate models of the decision procedure.

This gives A-FDT a global perspective. The agent asks, roughly, “What would the universe look like if the decision procedure I am running had a different output?” It then chooses the output corresponding to the best such universe.

This also explains why A-FDT does not need costly precommitments. In problems where CDT or EDT agents would wish to bind themselves in advance, A-FDT simply acts as the kind of agent that predictors can trust to act in the advantageous way.

---

## Conclusion

A-FDT is an expected utility theory that evaluates actions by intervening on a variable representing the output of the agent’s own decision function. Its action-level formal core is Equation (4):

\[
\mathrm{A\mbox{-}FDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E\!\left[
V \mid
\Do\!\left(
\mathrm{afdt}(\underline P,\underline G,\underline x)=a
\right)
\right].
\]

The theory’s distinctive feature is its treatment of subjunctive dependence. Predictors, twins, simulations, and accurate models are treated as depending on the same decision function; lesions and merely statistical common causes are not. This allows A-FDT to one-box in Newcomb’s problem, smoke in the smoking lesion problem, pay in Parfit’s hitchhiker problem, and cooperate in twin prisoner’s dilemmas.

The main unresolved issue is the construction of the dependency graph \(G\). Equation (4) tells us how to choose given a correct representation of logical and subjunctive dependencies, but it does not fully explain how to infer those dependencies from evidence. A practical A-FDT agent must therefore supply modeling assumptions about which processes compute, predict, or depend on its decision procedure. With those assumptions in place, A-FDT provides a clear, coherent, and often utility-maximizing method for deciding unfamiliar cases.

---

## References

Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.

Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.

Yudkowsky, E., and Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060.