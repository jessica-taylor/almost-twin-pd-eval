# Action Functional Decision Theory: Choosing the Output of a Fixed Decision Function

This essay explains **action functional decision theory**, which I will call **A-FDT**, using Equation (4) of Section 5 of Yudkowsky and Soares’s paper “Functional Decision Theory: A New Theory of Instrumental Rationality” as the primary formal statement. The source calls the theory *functional decision theory*; I use **A-FDT** throughout to emphasize the action-level formulation assigned here.

A-FDT’s guiding idea is that a rational agent should treat her decision as the output of a fixed mathematical function. Rather than asking, “Which physical action of mine causes the best outcome?” as causal decision theory does, or “Which action would be best news?” as evidential decision theory does, A-FDT asks:

> “Which output of this decision procedure causes the best outcome?”

The theory is designed to handle problems involving predictors, copies, simulations, twins, blackmailers, and other agents whose behavior depends on what the agent’s decision procedure would output.

---

## 1. Expected Utility and the A-FDT Rule

A-FDT is an expected utility theory. Let:

- \(\mathcal A\) be a finite set of actions.
- \(\mathcal O\) be a set of possible outcomes.
- \(\mathcal U(o)\) be the utility of outcome \(o\).
- \(V = \mathcal U(\text{Outcome})\) be the utility random variable.
- \(P\) be the agent’s probabilistic world-model.
- \(G\) be a graph representing dependency structure.
- \(x\) be the agent’s current observation history.

The three theories discussed by the source differ in how they construct hypothetical scenarios. Evidential decision theory conditions on the action:

\[
\mathrm{EDT}(P,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E\left[V \mid \text{Obs}=x,\ \text{Act}=a\right].
\]

Causal decision theory intervenes on the physical action:

\[
\mathrm{CDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E\left[V \mid do(\text{Act}=a),\ \text{Obs}=x\right].
\]

A-FDT, adapting the source’s Equation (4), intervenes instead on a variable representing the output of the agent’s own decision procedure. Let

\[
D_x \;:=\; \operatorname{AFDT}(\underline P,\underline G,\underline x)
\]

denote a variable in the model whose value represents the output of the A-FDT algorithm when run on inputs \(P\), \(G\), and \(x\). The underlines indicate that \(P\), \(G\), and \(x\) are being used to name a variable; they are not ordinary mathematical arguments inside the probability distribution. Then the A-FDT decision rule is:

\[
\boxed{
\mathrm{A\text{-}FDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E\left[V \mid do(D_x=a)\right].
}
\]

This is the central formal principle of A-FDT.

The self-reference is intentional. The agent’s model \(P\) contains a variable \(D_x\) representing the output of the very decision procedure that is using \(P\). The source notes that this kind of self-reference can be made precise using techniques related to Kleene’s recursion theorem and “quining.” For practical purposes, the important point is that the agent can represent the output of her own reasoning as a variable in her model, even if she does not already know the value of that variable.

---

## 2. What Kind of Intervention Is A-FDT Performing?

In Pearl’s causal calculus, \(do(X=x)\) means: set \(X\) to \(x\), leave upstream variables unchanged, and propagate the change downstream according to the graph. CDT uses this operation on the physical action variable \(\text{Act}\). A-FDT uses a formally similar operation, but on a *logical* or *computational* variable: the output of the agent’s decision function.

This difference is crucial.

A CDT agent asks:

> “What would happen if my body performed action \(a\), holding fixed the past and all variables not causally downstream of my action?”

An A-FDT agent asks:

> “What would happen if the output of this very decision procedure were \(a\), holding fixed all variables that do not subjunctively depend on that output?”

The phrase “subjunctively depend” is the source’s term for the kind of dependence that predictors, simulations, copies, and psychologically identical twins have on an agent’s decision procedure. The source summarizes the idea with the slogan:

> “Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.”

Replacing the source’s name with the name used in this essay: A-FDT is to subjunctive dependence as CDT is to causal dependence.

A-FDT therefore evaluates actions by constructing hypothetical worlds in which the decision function’s output is different. If the decision function is deterministic, then strictly speaking there is no possible world in which it has a different output on the same input. A-FDT therefore requires reasoning about what philosophers call *counterpossibles*: conditionals whose antecedents are logically impossible. The source acknowledges that we do not yet have a fully satisfactory formal semantics for such counterpossibles. Equation (4) avoids needing a general theory by assuming that the agent already has a suitable graph \(G\) telling her how changing the logical variable \(D_x\) affects the rest of the model.

---

## 3. The Role of the Graph \(G\)

The graph \(G\) is the heart of an A-FDT model. It encodes which variables depend on the output of the agent’s decision procedure.

In an ordinary causal graph, arrows represent causal influence. In an A-FDT graph, arrows may represent causal influence, but they may also represent logical, computational, or predictive dependence. The source explicitly says that \(G\) may encode “the logical, mathematical, computational, causal, etc. structure of the world.”

A variable \(Y\) should be downstream of \(D_x\) if, in the agent’s model, \(Y\) depends on what the agent’s decision procedure would output. Examples include:

- A predictor’s prediction of the agent’s action.
- A simulation of the agent run by another party.
- The action of a psychological twin who uses the same reasoning procedure.
- The behavior of another agent who is known to implement the same decision algorithm.
- Whether a blackmailer sends a blackmail letter, if the blackmailer sends it only upon predicting that the agent will pay.
- Which observation the agent receives, if the observation is produced by a predictor anticipating the agent’s decision.

By contrast, a variable should not be downstream of \(D_x\) merely because it is statistically correlated with the agent’s action. If a lesion causes both a preference for smoking and cancer, but does not predict or compute the agent’s decision procedure, then the lesion is not subjunctively dependent on the output of the agent’s decision function.

This is how A-FDT distinguishes predictor-like dependencies from lesion-like dependencies.

---

## 4. A-FDT in Newcomb’s Problem

Newcomb’s problem is the standard test case.

A predictor has placed \$1,000,000 in opaque box B iff she predicted that the agent will take only box B. Box A visibly contains \$1,000. The predictor is correct 99% of the time. The agent may take both boxes, receiving the contents of both, or take only box B.

An A-FDT model contains variables such as:

- \(D\): the output of the agent’s A-FDT procedure.
- \(\text{Act}\): the physical action taken.
- \(\text{Prediction}\): the predictor’s prediction.
- \(\text{BoxB}\): whether box B is full or empty.
- \(V\): utility.

A plausible A-FDT graph includes arrows:

\[
D \rightarrow \text{Act},
\qquad
D \rightarrow \text{Prediction}
\rightarrow \text{BoxB},
\qquad
\text{Act}, \text{BoxB} \rightarrow V.
\]

The arrow \(D \rightarrow \text{Prediction}\) represents the fact that the predictor’s prediction is a reliable model of the agent’s decision procedure.

Now compare the two hypothetical interventions.

### One-boxing

If \(do(D=\text{one-box})\), then the agent takes only box B, and the predictor almost certainly predicted one-boxing. Thus box B is full with probability \(0.99\) and empty with probability \(0.01\). Expected utility is approximately:

\[
0.99 \cdot \$1{,}000{,}000 + 0.01 \cdot \$0
=
\$990{,}000.
\]

### Two-boxing

If \(do(D=\text{two-box})\), then the agent takes both boxes, and the predictor almost certainly predicted two-boxing. Thus box B is empty with probability \(0.99\) and full with probability \(0.01\). Expected utility is:

\[
0.99 \cdot \$1{,}000 + 0.01 \cdot \$1{,}001{,}000
=
\$11{,}000.
\]

Since

\[
\$990{,}000 > \$11{,}000,
\]

A-FDT one-boxes.

CDT, by contrast, intervenes on \(\text{Act}\) rather than on \(D\). It holds the contents of box B fixed and observes that taking both boxes always adds \$1,000. Therefore CDT two-boxes. EDT conditions on the action and one-boxes because one-boxing is good evidence that box B is full. A-FDT one-boxes not because one-boxing is good news, but because changing the output of the decision procedure changes the predictor’s prediction in the relevant hypothetical.

---

## 5. A-FDT and the Smoking Lesion Problem

The smoking lesion problem is meant to punish EDT-style reasoning.

In the problem, smoking is correlated with fatal lung cancer, but the correlation is due to a common cause: a lesion that both makes smoking pleasurable and causes cancer. Smoking itself does not cause cancer. Smoking gives \$1,000 worth of utility. Surviving cancer is worth \$1,000,000.

EDT refrains from smoking because smoking is bad news: it is evidence that the agent has the lesion. CDT smokes because smoking does not causally affect cancer. A-FDT also smokes.

The reason is that the lesion is not a predictor of the agent’s decision procedure. It is a common cause of both a preference for smoking and cancer, but it does not compute, simulate, or predict the output of the agent’s A-FDT algorithm.

A simplified A-FDT graph therefore contains:

\[
D \rightarrow \text{Act},
\qquad
\text{Lesion} \rightarrow \text{Cancer},
\]

but no arrow

\[
D \rightarrow \text{Cancer}.
\]

When the agent evaluates \(do(D=\text{smoke})\) and \(do(D=\text{refrain})\), the probability of cancer is unchanged. Smoking adds \$1,000 of utility. Therefore A-FDT smokes.

The source gives a more careful formalization because the lesion may also determine whether the agent has a utility function that enjoys smoking. In that version, there are two possible A-FDT nodes, one corresponding to the decision procedure with smoking-friendly preferences and one corresponding to the decision procedure with smoking-averse preferences. The lesion determines which procedure actually controls the action. Even then, intervening on the relevant A-FDT node does not change the probability of the lesion or cancer. The conclusion remains the same: smoking is better by the value of smoking itself.

The important structural lesson is that A-FDT does not preserve merely evidential correlations. It preserves dependencies that are relevantly tied to the decision procedure.

---

## 6. Observation and Updateless Reasoning

One of the most distinctive features of A-FDT is its treatment of observations.

CDT responds to an observation \(x\) by conditioning:

\[
\mathbb E[V \mid do(\text{Act}=a), \text{Obs}=x].
\]

EDT also conditions on the observation and the action.

A-FDT, according to Equation (4), responds to observation by changing which decision-function node is intervened upon. If the agent has observation \(x\), A-FDT intervenes on

\[
D_x = \operatorname{AFDT}(\underline P,\underline G,\underline x).
\]

It does not, in general, evaluate hypotheticals by additionally conditioning on \(\text{Obs}=x\). This is important in cases where the observation itself depends on the predictor’s model of the agent.

The source is explicit about this difference:

> “Where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon.”

This produces what is sometimes called updateless reasoning. The agent uses her observation to identify which decision problem she is in, but she does not necessarily hold that observation fixed inside every hypothetical. If changing the output of her decision procedure would have led her to receive a different observation, then the hypothetical should reflect that.

This point is central to the transparent Newcomb problem and to Parfit’s hitchhiker problem.

---

## 7. Transparent Newcomb and Parfit’s Hitchhiker

In the transparent Newcomb problem, both boxes are transparent. The predictor placed \$1,000,000 in box B iff she predicted that the agent would leave box A behind upon seeing that both boxes are full. Suppose the agent sees that both boxes are full.

CDT says: box B is already full, so take both boxes.

EDT says: conditional on seeing box B full, taking both boxes gives more money.

A-FDT says: one-box.

The A-FDT model must include at least two decision-function nodes:

\[
D_{\text{full}} = \operatorname{AFDT}(\underline P,\underline G,\underline{\text{full}}),
\]

\[
D_{\text{empty}} = \operatorname{AFDT}(\underline P,\underline G,\underline{\text{empty}}).
\]

The predictor predicts what \(D_{\text{full}}\) will output if the agent sees full boxes. If the predictor predicts one-boxing, she fills box B. If she predicts two-boxing, she leaves box B empty.

Now suppose the agent actually sees full boxes. A-FDT evaluates:

\[
\mathbb E[V \mid do(D_{\text{full}}=a)].
\]

If \(a=\text{one-box}\), then with high probability the predictor predicted one-boxing, box B is full, and the agent receives \$1,000,000. With small probability the predictor erred, the box is empty, and the agent receives whatever \(D_{\text{empty}}\) would lead her to do upon seeing empty boxes. The expected value is still close to \$990,000.

If \(a=\text{two-box}\), then with high probability the predictor predicted two-boxing, box B is empty, and the agent probably sees an empty box rather than a full one. In that branch, her actual action is governed by \(D_{\text{empty}}\), not \(D_{\text{full}}\). The expected value is low, roughly on the order of the value of taking the visible \$1,000.

Thus A-FDT one-boxes even when both boxes are seen to be full.

This is the same reasoning that makes A-FDT pay the driver in Parfit’s hitchhiker problem. In that problem, a driver will rescue the agent from the desert only if she predicts that the agent will later pay \$1,000 after reaching the city. Once in the city, CDT and EDT see no reason to pay. But A-FDT recognizes that the driver’s earlier prediction depended on the output of the agent’s decision procedure in the city. If the agent’s procedure outputs “pay,” the driver likely predicted payment and rescued her. If it outputs “refuse,” the driver likely predicted refusal and left her in the desert.

A-FDT therefore pays. The source emphasizes that one-boxing in transparent Newcomb and paying in Parfit’s hitchhiker are decision-theoretically analogous.

---

## 8. Policies Versus Actions

Equation (4), as assigned here, evaluates actions. The source notes in a footnote that the authors’ preferred formulation often evaluates policies—mappings from observations to actions—rather than single actions. This can matter in multi-agent or sequential problems.

For this essay, I take Equation (4) as primary and treat A-FDT as an action-level theory. However, it is useful to state how a policy version could be constructed.

Let \(\Pi\) be a set of policies \(\pi : \mathcal X \to \mathcal A\). Let \(D^\Pi\) be a variable representing the output of the agent’s policy-selection procedure. A natural policy-level analogue of A-FDT is:

\[
\mathrm{A\text{-}FDT}_{\Pi}(P,G)
=
\arg\max_{\pi\in\Pi}
\mathbb E\left[V \mid do(D^\Pi=\pi)\right].
\]

After selecting \(\pi\), the agent executes \(\pi(x)\) upon receiving observation \(x\).

This extension is not strictly forced by Equation (4), but it is a natural operational interpretation of the same principle: choose the output of the fixed decision procedure that yields the best world. If the relevant output is a policy rather than a single action, then A-FDT should intervene on the policy variable.

In many one-shot problems, action-level and policy-level formulations agree. In problems where observations are themselves influenced by predictors, the policy formulation can be cleaner, because it lets the agent evaluate the consequences of adopting a whole pattern of behavior rather than a single isolated act.

---

## 9. How to Apply A-FDT to a New Problem

The source does not give a complete algorithm for constructing \(P\) and \(G\). It assumes that the agent already has a model describing the relevant dependencies. This is the largest open problem in the theory.

Still, the examples support a practical recipe.

### Step 1: Identify the decision procedure

Ask: What is the algorithm whose output is being evaluated? In A-FDT, this is not “my body” or “my disposition” in a vague sense, but the particular computational procedure that maps beliefs, goals, and observations to an action.

### Step 2: Identify predictor-like dependencies

Ask: Which parts of the world depend on what this procedure outputs?

Include arrows from \(D_x\) to:

- Predictions of the agent’s action.
- Simulations of the agent.
- Copies of the agent.
- Other agents using the same algorithm in relevantly similar circumstances.
- Decisions by other agents to send letters, make threats, offer rewards, or enter contracts, when those decisions are based on predictions of the agent’s behavior.

### Step 3: Exclude merely statistical correlations

Ask: Is this variable correlated with my action only because of a common cause?

If a variable is a lesion, a genetic trait, a random environmental coincidence, or a historical fact that does not model the agent’s decision procedure, A-FDT should not treat it as downstream of \(D_x\).

### Step 4: Model observations carefully

If an observation is produced by a predictor, blackmailer, or environment that depends on the agent’s decision procedure, do not automatically condition it away. Use the observation to select the relevant decision node \(D_x\), but allow the hypothetical intervention on \(D_x\) to change the observation if the graph says the observation depends on the predictor’s prediction.

If an observation is genuinely exogenous—say, the weather on a day that has no connection to predictors of the agent—then conditioning on it may be harmless.

### Step 5: Intervene and compare expected utilities

For each candidate action \(a\), compute:

\[
\mathbb E[V \mid do(D_x=a)].
\]

Choose an action maximizing this expectation.

This recipe is not a complete formal solution to the problem of subjunctive dependence, but it captures the operational pattern of the source’s examples.

---

## 10. What Is Fixed by the Source and What Requires Extra Assumptions?

The source fixes several central claims:

1. A-FDT maximizes expected utility relative to interventionist hypotheticals.
2. The intervention is performed on a variable representing the output of the agent’s decision procedure.
3. Observations are handled by changing the intervention node, not merely by conditioning.
4. The graph \(G\) encodes logical, mathematical, computational, and causal dependencies.
5. CDT preserves too few correlations; EDT preserves too many; A-FDT aims to preserve the relevant subjunctive dependencies.

The source leaves several matters open.

First, it does not provide a general method for learning or constructing \(G\). It says that deducing subjunctive dependency structure from observation is perhaps the largest open problem for the theory.

Second, it does not provide a fully general semantics for counterpossible reasoning. The \(do\)-operator is borrowed from Pearl’s causal framework, but Pearl’s framework is designed for causal intervention, not for intervention on logical facts. The source acknowledges this and treats \(G\) as an input.

Third, the treatment of observation is slightly underdetermined. Equation (4) does not condition on \(\text{Obs}=x\), and the source says that A-FDT responds to observation by changing the intervention node. But some example calculations in the source appear to include observation conditions. The most coherent interpretation, and the one that yields the source’s endorsed answers in transparent Newcomb and blackmail problems, is that A-FDT does not hold decision-relevant observations fixed inside the hypothetical. It uses the actual observation to select the decision instance being evaluated.

Fourth, the action-versus-policy distinction is not fully settled by Equation (4). The source’s preferred formulation apparently uses policies, but Equation (4) is action-based. For this essay, I treat the action version as primary and the policy version as a natural extension.

My own operational proposal is that one should model A-FDT problems using structural equations or probabilistic programs, with explicit nodes for computations, predictors, and observations. Edges should represent the best available theory of which variables are computed from, predicted from, or logically constrained by the agent’s decision procedure. This goes beyond the source, but it seems necessary for applying A-FDT to unfamiliar cases.

---

## 11. Why A-FDT Differs from CDT and EDT

The source diagnoses EDT and CDT as follows:

> “EDT’s hypotheticals respect too many correlations between variables; CDT’s hypotheticals respect too few.”

A-FDT tries to preserve exactly the correlations that matter for decision-making.

EDT fails in the smoking lesion problem because it treats smoking as evidence of cancer, even though the agent cannot influence cancer by smoking. EDT “manages the news.”

CDT fails in Newcomb-like problems because it severs correlations between the agent’s action and accurate predictors of that action. CDT hypotheticals imagine the agent acting differently while predictors remain fixed, even when the predictors are known to be reliable.

A-FDT avoids both errors. In the smoking lesion problem, it recognizes that the lesion is not subjunctively dependent on the decision procedure. In Newcomb’s problem, it recognizes that the predictor is subjunctively dependent on the decision procedure.

The source also argues that A-FDT has its own version of dominance. CDT says two-boxing dominates one-boxing if one holds the predictor’s prediction fixed. But A-FDT says that holding the predictor fixed while changing the output of the decision procedure is an inappropriate hypothetical. In A-FDT-style counterfactuals, one-boxing does not become dominated, because changing the decision output also changes the prediction.

---

## 12. Conclusion

A-FDT is a decision theory that evaluates actions by asking what would happen if the output of the agent’s own decision function were different. Its formal core, taken from Equation (4) of the source, is:

\[
\mathrm{A\text{-}FDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E\left[V \mid do(D_x=a)\right],
\]

where \(D_x\) represents the output of the A-FDT procedure on inputs \(P\), \(G\), and \(x\).

The theory’s novelty is not expected utility maximization itself, but the choice of hypotheticals. A-FDT intervenes on a logical variable rather than a physical action variable. It preserves predictor-like and computation-like dependencies while ignoring merely statistical correlations. This lets it one-box in Newcomb’s problem, smoke in the smoking lesion problem, pay in Parfit’s hitchhiker problem, and resist certain kinds of blackmail.

The main unresolved issue is how to construct the graph \(G\) in a principled way. The source supplies examples and motivations, but not a complete account of how agents should learn subjunctive dependency structure. Until that problem is solved, applying A-FDT requires modeling judgment. Even so, the central rule is clear: choose the output of your decision procedure that would produce the best world, once all relevant logical and computational dependencies are taken into account.

---

## References

Pearl, Judea. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.

Yudkowsky, Eliezer, and Nate Soares. “Functional Decision Theory: A New Theory of Instrumental Rationality.” arXiv:1710.05060v2.