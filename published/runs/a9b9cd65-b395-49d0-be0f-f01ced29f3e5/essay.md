# Action Functional Decision Theory: Choosing the Best Output of a Fixed Decision Function

The reference article introduces a decision theory called *functional decision theory*. In this essay I use the assigned name **A-FDT**, for *action functional decision theory*, to refer to the action-centered formalization given in Equation (4), Section 5 of the paper. The central idea is simple but radical: a rational agent should treat her decision as the output of a fixed mathematical function, and should ask, in the paper’s words, “Which output of this decision procedure causes the best outcome?”

A-FDT differs from evidential decision theory (EDT) and causal decision theory (CDT) not because it rejects expected utility maximization, but because it constructs decision hypotheticals differently. EDT asks what would be good news; CDT asks what would causally result from a physical action; A-FDT asks what would happen if the output of the agent’s actual decision procedure were different. This essay explains the formal rule, shows how it works in canonical problems, and discusses what must be added to apply it to unfamiliar cases.

---

## 1. Expected utility and the three hypotheticals

All three standard theories discussed in the source are expected utility theories. Given a countable outcome set \(\mathcal O\), finite action set \(\mathcal A\), observation history \(x\), and bounded utility function \(\mathcal U\), an agent evaluates actions by something of the form

\[
\mathcal{EU}(a)
=
\sum_j P(a \then o_j ; x)\,\mathcal U(o_j),
\]

where \(P(a \then o_j;x)\) is the probability assigned to outcome \(o_j\) in the hypothetical situation where action \(a\) is taken after observation \(x\). EDT, CDT, and A-FDT disagree about how to interpret the hypothetical connective \(\then\).

EDT interprets it as ordinary conditional probability:

\[
\mathrm{EDT}(P,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E\!\left[V \mid \Obs=x,\Act=a\right].
\]

CDT interprets it as a causal intervention on the physical action variable:

\[
\mathrm{CDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E\!\left[V \mid do(\Act=a),\Obs=x\right].
\]

Here \(P\) is a probability distribution, \(G\) is a causal graph, and \(do(\Act=a)\) is Pearl’s intervention operator: set \(\Act=a\), propagate consequences downstream in \(G\), and leave non-descendants fixed.

A-FDT replaces the physical action variable with a variable representing the output of the agent’s decision procedure. Translating the source’s Equation (4) into the assigned notation, the primary formal rule is:

\[
\boxed{
\mathrm{A\text{-}FDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E\!\left[
V \mid do\bigl(D_x=a\bigr)
\right]
}
\]

where

\[
D_x
=
\mathrm{fdt}_A(\underline P,\underline G,\underline x)
\]

is a variable in the agent’s model representing the output of A-FDT when run on inputs \(P\), \(G\), and \(x\). The underlines follow the source’s convention for “dequoting”: if \(x\) is an observation value, \(\underline x\) is the name or code for that value inside the variable’s identifier. The definition is self-referential because \(P\) contains a variable representing the output of the very procedure using \(P\), but the source notes that this is harmless in principle; self-referential data structures can be constructed by standard recursion-theoretic methods.

The expected utility of output \(a\) under A-FDT is therefore

\[
\mathcal{EU}_A(a;x)
=
\mathbb E_{P^{do(D_x=a)}}[V],
\]

where \(P^{do(D_x=a)}\) is the post-intervention distribution obtained by setting \(D_x=a\) and updating all variables that, according to \(G\), subjunctively depend on \(D_x\). A-FDT chooses an action maximizing this quantity.

One important feature is that A-FDT can evaluate actions to which the agent assigns prior probability zero. EDT, by conditioning on \(\Act=a\), can be paralyzed if \(P(\Act=a)=0\). A-FDT, like CDT, uses an intervention rather than mere conditionalization.

---

## 2. The role of the dependency graph \(G\)

The formal simplicity of Equation (4) hides a substantive requirement: the model must include a graph \(G\) saying how changing a logical or computational variable affects other variables. The source contrasts this with CDT, where \(G\) is a causal graph. In A-FDT, \(G\) must encode not only causal dependencies but also what the source calls *subjunctive dependencies*.

A variable \(Y\) subjunctively depends on the decision function when, if the function had a different output, \(Y\) would also change, even if there is no direct causal path from the agent’s present bodily movement to \(Y\). The paradigm cases are predictors, simulations, copies, and psychological twins. If a predictor has modeled the agent’s decision procedure, then the predictor’s prediction is not merely statistically correlated with the agent’s action; it is tied to the same underlying computation.

The source gives the analogy of two reliable calculators computing \(6288+1048\). They may be causally isolated, but if one outputs \(7336\), we infer that the other does too. Their outputs subjunctively depend on the same mathematical function. By contrast, if two calculators happen to be pink, their colors are statistically correlated but not subjunctively dependent: painting one green would not change the other.

Thus, in A-FDT:

- Causal dependencies are preserved when they are relevant.
- Logical, computational, and predictive dependencies are also preserved.
- Merely statistical correlations are not preserved unless they arise from shared computation or prediction.

This is the structural difference between the theories. EDT preserves too many correlations: it treats all evidential connections as decision-relevant. CDT preserves too few: it severs correlations between the agent’s action and predictors that are not caused by the action. A-FDT tries to preserve exactly the decision-relevant subjunctive dependencies.

---

## 3. How A-FDT evaluates alternative actions

To apply A-FDT to a decision problem, one proceeds as follows.

1. **Specify the action set \(\mathcal A\), observation input \(x\), outcomes, and utility function.**  
   The agent should have a bounded utility assignment to outcomes.

2. **Construct a probabilistic model \(P\).**  
   The model should include variables for the agent’s action, relevant environmental states, predictions, observations, outcomes, and the decision-function output variable \(D_x\).

3. **Construct a dependency graph \(G\).**  
   Draw edges from \(D_x\) to variables whose values are determined by, predicted from, or otherwise computationally dependent on the output of the agent’s decision procedure. Draw ordinary causal edges where appropriate. Do not draw edges from \(D_x\) to variables that are merely common causes or statistical correlates.

4. **For each candidate action \(a\), form the intervention \(do(D_x=a)\).**  
   Set the decision-function output variable to \(a\). Propagate this change through \(G\) to all downstream variables. Leave variables fixed if they are not downstream from \(D_x\) in the subjunctive-dependency graph.

5. **Compute expected utility in each post-intervention model.**  
   Evaluate

   \[
   \mathcal{EU}_A(a;x)
   =
   \mathbb E[V\mid do(D_x=a)].
   \]

6. **Choose an action maximizing expected utility.**  
   If several actions tie, any maximizer is permissible.

This procedure evaluates actions as possible outputs of the agent’s actual decision function. It does not ask, “What if I used a different decision theory?” It asks, “What if this very decision procedure concluded differently?”

That distinction matters. If an agent asks what would happen if she used some entirely different algorithm, she may fail to account for predictors who are predicting the algorithm she actually uses. The source argues that this alternative approach would still need to imagine predictors of the actual decision procedure behaving as if that procedure had a different output, bringing us back to A-FDT-style counterfactuals.

---

## 4. Newcomb’s problem

Newcomb’s problem is the cleanest illustration.

An agent faces two boxes. Box A contains \$1,000. Box B contains \$1,000,000 if a reliable predictor predicted the agent would take only Box B; otherwise Box B is empty. The predictor has already acted. The available actions are:

\[
\mathcal A=\{\Val{onebox},\Val{twobox}\}.
\]

An EDT agent conditions on its action and one-boxes, because conditional on one-boxing, Box B is probably full. A CDT agent intervenes on the physical action and two-boxes, because the predictor’s prediction is causally upstream and therefore unaffected by the current physical act.

A-FDT introduces a variable

\[
D_x=\mathrm{fdt}_A(\underline P,\underline G,\underline x),
\]

where \(x\) is the agent’s current observation. The graph contains edges such as:

\[
D_x \to \Act,
\qquad
D_x \to \Var{Prediction},
\qquad
\Var{Prediction} \to \Var{BoxB},
\qquad
\Act,\Var{BoxB}\to V.
\]

Assume the predictor is accurate with probability \(0.99\). Under the intervention \(do(D_x=\Val{onebox})\), the agent one-boxes and the predictor almost certainly predicted one-boxing, so Box B is full with probability \(0.99\). The expected utility is approximately

\[
0.99(\$1{,}000{,}000)+0.01(\$0)
=
\$990{,}000.
\]

Under the intervention \(do(D_x=\Val{twobox})\), the agent two-boxes and the predictor almost certainly predicted two-boxing, so Box B is empty with probability \(0.99\). The expected utility is approximately

\[
0.99(\$1{,}000)+0.01(\$1{,}001{,}000)
=
\$11{,}000.
\]

Therefore,

\[
\mathrm{A\text{-}FDT}(P,G,x)=\Val{onebox}.
\]

The reasoning is not retrocausal. A-FDT does not claim that the agent’s current physical movement sends a signal into the past. Rather, the predictor’s prediction and the agent’s action are both tied to the same decision function. If that function had output \(\Val{twobox}\), the predictor would have predicted \(\Val{twobox}\), and Box B would probably be empty.

---

## 5. The smoking lesion problem

The smoking lesion problem shows why A-FDT is not merely EDT in disguise.

An agent considers smoking. Smoking is correlated with fatal lung cancer, but the correlation is due to a common cause: a lesion that both makes smoking appealing and usually causes cancer. Smoking itself does not cause cancer. Smoking gives \$1,000 of utility; avoiding cancer is worth \$1,000,000.

EDT refrains from smoking because smoking is bad news: it is evidence of the lesion. CDT smokes because smoking does not causally affect cancer. A-FDT also smokes, but for a structural reason: the lesion is not subjunctively dependent on the output of the agent’s decision procedure.

In an A-FDT graph, the lesion variable may affect the agent’s preferences or action, and it may affect cancer, but the decision-function output variable does not affect the lesion or cancer:

\[
\Var{Lesion}\to \Var{Cancer},
\qquad
D_x\to \Act,
\qquad
\Act\to V.
\]

There is no edge

\[
D_x \to \Var{Lesion}
\]

or

\[
D_x \to \Var{Cancer}.
\]

Therefore, under either intervention,

\[
do(D_x=\Val{smoke})
\]

or

\[
do(D_x=\Val{refrain}),
\]

the probability of cancer remains the same. Smoking adds \$1,000 of utility without changing the cancer risk. Hence A-FDT smokes.

The source’s more careful treatment notes that the lesion may also affect which utility function the agent has, requiring two possible decision-function variables. But the essential conclusion remains: changing the output of the relevant decision procedure does not change whether the lesion exists. The lesion is predictor-like in neither direction; it is merely a common cause. A-FDT therefore does not manage the news.

---

## 6. Transparent Newcomb and Parfit’s hitchhiker

A-FDT’s most surprising implications appear when an observation is itself predicted or produced by a predictor-like process.

In the transparent Newcomb problem, both boxes are transparent. The predictor filled Box B iff she predicted the agent would one-box upon seeing two full boxes. If the agent sees that Box B is full, should she one-box or two-box?

CDT and EDT both two-box once the agent sees that Box B is full. If Box B is already full, taking both boxes yields \$1,001,000 instead of \$1,000,000.

A-FDT one-boxes. The key is that the observation \(x=\Val{full}\) is not treated as an exogenous fact to be conditioned on in the usual way. Instead, A-FDT evaluates the output of the decision procedure that runs upon seeing a full box:

\[
D_{\Val{full}}
=
\mathrm{fdt}_A(\underline P,\underline G,\underline{\Val{full}}).
\]

The graph contains a node for the predictor’s prediction, which determines whether Box B is full and which observation the agent receives. If \(D_{\Val{full}}\) outputs \(\Val{onebox}\), then the predictor likely predicted one-boxing, Box B is likely full, and the agent receives \$1,000,000. If \(D_{\Val{full}}\) outputs \(\Val{twobox}\), then the predictor likely predicted two-boxing, Box B is likely empty, and the agent probably does not even face the full-box decision; instead she faces the empty-box decision.

With predictor accuracy \(0.99\), and letting \(q\) be the probability that the agent two-boxes upon seeing an empty box, the source’s calculation gives approximately:

\[
\mathcal{EU}_A(\Val{onebox};\Val{full})
=
0.99(\$1{,}000{,}000)
+
0.01q(\$1{,}000),
\]

whereas

\[
\mathcal{EU}_A(\Val{twobox};\Val{full})
=
0.01(\$1{,}001{,}000)
+
0.99q(\$1{,}000).
\]

If \(q=1\), these are roughly \$990,010 versus \$11,990. A-FDT one-boxes.

This is formally analogous to Parfit’s hitchhiker problem. An agent stranded in the desert is offered a ride if she promises to pay \$1,000 later. The driver can detect lies with high accuracy. Once in the city, should the agent pay? CDT and EDT say no, because payment is costly and no longer causally beneficial. A-FDT says yes, because the driver’s decision to rescue depends on predicting the agent’s later decision procedure. The relevant A-FDT node is the procedure that runs upon arriving in the city. If that procedure outputs \(\Val{pay}\), the driver predicts payment and rescues the agent. If it outputs \(\Val{refuse}\), the driver predicts refusal and leaves the agent in the desert.

The source uses this equivalence to argue that one-boxing in transparent Newcomb and paying in Parfit’s hitchhiker are the same kind of decision. The paper’s claim is that this behavior is not a quirk but a consequence of taking subjunctive dependencies seriously.

---

## 7. Counterfactuals and counterpossibles

A-FDT’s hypotheticals are unusual because they often involve counterpossibles. If the agent’s decision procedure is deterministic and actually outputs \(a^\ast\), then the supposition “the procedure outputs \(a\neq a^\ast\)” is not logically possible in the strictest sense. Nevertheless, A-FDT needs to reason about such suppositions.

The source acknowledges that this is a technical difficulty. We do not yet have a fully satisfactory general account of counterpossible reasoning. However, the paper argues that the difficulty is not fatal. Human mathematicians can reason under uncertainty about mathematical claims that are either necessarily true or necessarily false. Likewise, an A-FDT agent only needs limited counterpossible reasoning: she needs to know how predictors, copies, and simulations would respond if her decision procedure had a different output.

Operationally, A-FDT treats the decision-function output as a variable in a structural model. The model assigns probabilities to the consequences of different outputs, even if only one output is actually logically possible. This is an idealization, but it is comparable to CDT’s idealization that a deterministic physical action can be varied in hypotheticals.

The source also emphasizes that A-FDT does not require believing in backward causation. The agent does not imagine a physical signal traveling back to the predictor. She imagines a world in which the relevant mathematical function has a different output, and then allows all variables that depend on that function to change accordingly.

---

## 8. Evaluating policies, not only actions

Equation (4), the primary equation for this essay, evaluates actions. However, the source notes in a footnote that a policy-based formulation is often preferable, especially in multi-agent or sequential settings. A policy is a function from observations to actions:

\[
\pi:\mathcal X\to\mathcal A.
\]

A policy version of A-FDT would introduce a variable \(\Pi\) representing the output of the agent’s decision procedure before conditioning on the current observation. The rule would be:

\[
\mathrm{A\text{-}FDT}_{\Pi}(P,G)
=
\arg\max_{\pi}
\mathbb E\!\left[V\mid do(\Pi=\pi)\right].
\]

The agent then executes \(\pi(x)\) upon observing \(x\).

This policy formulation helps clarify cases where several observation-contingent decision nodes are logically linked. In transparent Newcomb, for example, the policy includes what the agent would do upon seeing a full box and what she would do upon seeing an empty box. A predictor may evaluate the entire policy, not just the action taken in the actual branch.

The source does not make this policy formulation the official Equation (4), and for this essay I treat Equation (4) as primary. But the policy interpretation is a natural conservative extension of the same principle: choose the output of the fixed decision procedure that yields the best expected world.

---

## 9. Applying A-FDT to unfamiliar cases

A reader who wants to apply A-FDT to a new problem can use the following diagnostic questions.

### 9.1 What is the decision function?

Identify the procedure whose output is the agent’s action. In the formalism, this is \(D_x\). The agent is not choosing a physical movement in isolation; she is determining which output of this procedure would be best.

### 9.2 Which variables depend on that function?

Ask whether each variable in the model would change if \(D_x\) had a different output.

If the variable is a predictor, simulation, copy, twin, or record of the decision procedure, it likely subjunctively depends on \(D_x\). Draw an edge from \(D_x\) to that variable.

If the variable is a lesion, weather condition, or other common cause that does not represent or predict the decision procedure, do not draw an edge from \(D_x\) to it.

If the variable is causally downstream of the physical action, draw the usual causal edge from \(\Act\) to it.

### 9.3 Is the observation exogenous or predictor-produced?

This is one of the delicate points. Equation (4) uses the observation \(x\) to select the decision node \(D_x\), but it does not simply condition on \(\Obs=x\) in the manner of EDT or CDT. The source’s examples suggest that when the observation is itself produced by a predictor’s choice, A-FDT allows the observation to vary inside the hypothetical.

For unfamiliar cases, I propose the following operational distinction:

- If the observation is ordinary exogenous evidence about the world, such as seeing rain and inferring cloudy weather, condition the background model \(P\) on that evidence before applying A-FDT.
- If the observation is entangled with predictors, blackmailers, drivers, or box-fillers, do not rigidly condition on it as an independent fact. Instead, model it as a variable that may depend on the decision procedure.

This distinction is not fully formalized in the source, but it preserves the source’s treatment of transparent Newcomb, Parfit’s hitchhiker, and blackmail problems.

### 9.4 Compute the post-intervention expectations

For each action \(a\), calculate

\[
\mathbb E[V\mid do(D_x=a)].
\]

Choose the action with the largest value.

This gives a practical recipe, provided one can construct \(P\) and \(G\).

---

## 10. Open problems and additional assumptions

The source is candid that A-FDT is not yet a complete operational theory in the way that Pearl-style CDT is a theory of causal inference given a causal graph. Several questions remain open.

### 10.1 How do we learn \(G\)?

The paper says that deducing the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem for the theory. CDT can appeal, at least in principle, to Pearl’s account of causal discovery. A-FDT needs an analogous account of logical and computational dependency discovery.

Until such an account exists, applying A-FDT requires modeling assumptions. In toy problems, the graph is usually supplied by the problem statement: predictors predict the agent, twins use the same reasoning, lesions do not compute. In real-world problems, identifying predictor-like dependencies may be difficult.

My suggested operational rule is this: treat a dependency as subjunctively decision-relevant when the environment contains a process that represents, simulates, predicts, or instantiates the agent’s decision procedure. This is not a complete formal criterion, but it captures the paper’s examples.

### 10.2 How do we interpret counterpossibles?

A-FDT requires probabilities under antecedents such as “the decision function had a different output.” The source says no fully satisfactory account of counterpossible reasoning is available.

For practical purposes, one can treat \(D_x\) as an uncertain logical variable inside a probabilistic structural model. This is an additional modeling assumption, not something fully grounded by the source. A more complete theory would need a theory of logical uncertainty, perhaps related to probabilistic logic or logical induction, but the paper does not require that machinery for its examples.

### 10.3 How exactly are observations handled?

Equation (4) makes observation dependence explicit by changing the intervention node from \(D_x\) to \(D_y\) when the observation changes from \(x\) to \(y\). However, some of the source’s later examples appear to hold the observation fixed in one formula while allowing it to vary in the surrounding reasoning. The intended treatment, I believe, is that actual observations select the relevant decision node, but observations that are themselves consequences of predictor-like behavior should not be treated as exogenous constraints inside the hypothetical.

This is an important uncertainty. My proposed interpretation is that A-FDT should distinguish between:

1. **Observations as inputs to the decision function**, which determine which node is being evaluated; and  
2. **Observations as evidence about exogenous states**, which can be conditioned on in \(P\).

When an observation is entangled with prediction, it belongs primarily to the first category. When it is ordinary evidence, it belongs primarily to the second. This interpretation is not explicitly formalized in the source, but it makes the paper’s examples coherent.

---

## 11. Why A-FDT succeeds where EDT and CDT fail

The source’s central claim is that A-FDT achieves higher utility in a range of fair decision problems. It one-boxes in Newcomb’s problem, smokes in the smoking lesion problem, pays in Parfit’s hitchhiker, one-boxes in transparent Newcomb, and resists certain blackmail schemes.

The unifying diagnosis is that EDT respects too many correlations, while CDT respects too few. EDT treats evidence as if it were control. Smoking is bad news, so EDT avoids it. CDT treats only causal downstream effects as decision-relevant, so it ignores predictors and twins. A-FDT preserves correlations that arise because the environment is modeling or sharing the agent’s decision procedure, while breaking correlations that are merely statistical.

The source also argues that A-FDT avoids the need for costly precommitment and ratification. An A-FDT agent simply acts as she would have wanted to precommit to act. In Newcomb-like environments, that disposition is advantageous.

Finally, the source rejects the idea that Newcomb’s problem unfairly rewards irrationality. As the paper puts it, “Newcomb’s problem doesn't punish rational agents; it punishes two-boxers.” The predictor rewards or punishes actions, not the abstract decision theory by name. If a problem directly punished agents for using A-FDT itself, no decision theory could guarantee success. The source’s claim is limited to fair problems where outcomes depend on the agent’s behavior, not on arbitrary punishment for implementing a particular algorithm.

---

## Conclusion

A-FDT is an expected utility theory that chooses the action corresponding to the best counterfactual output of the agent’s actual decision function. Its official action-level rule, following Equation (4), Section 5 of the source, is:

\[
\mathrm{A\text{-}FDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E\!\left[
V \mid do\bigl(\mathrm{fdt}_A(\underline P,\underline G,\underline x)=a\bigr)
\right].
\]

The theory’s distinctive feature is its treatment of subjunctive dependence. Predictors, copies, simulations, and twins are not ignored as causally irrelevant, nor are they treated as mere evidence. They are represented in the dependency graph as variables that would change if the decision function’s output changed. This allows A-FDT to one-box in Newcomb’s problem, smoke in the smoking lesion problem, and pay in Parfit’s hitchhiker.

The main difficulties are also clear. We need a better account of how to construct subjunctive-dependence graphs, how to reason about counterpossibles, and how to handle observations that are both evidence and predictor-produced. The source supplies the formal decision rule and many illustrative examples, but some operational details require additional interpretive assumptions. With those caveats understood, A-FDT offers a precise and attractive principle: choose the output of this very decision procedure that produces the best expected world.

---

## References

Joyce, J. M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

Pearl, J. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.

Yudkowsky, E., and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2.