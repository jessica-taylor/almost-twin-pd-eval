# 023_fdt_eq4_qwen_qwen3.8-max-prime_rhigh_plow / 00004

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/8704403a-7ae2-4a81-885f-06d76d0ecada/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/8704403a-7ae2-4a81-885f-06d76d0ecada/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Action Functional Decision Theory: Choosing the Output of a Fixed Decision Function

## 1. The central idea of A-FDT

Action functional decision theory (A-FDT) is a decision theory that evaluates actions by asking what would happen if the agent’s *decision procedure itself* produced a different output. The supplied source calls this theory functional decision theory; I use the assigned name A-FDT throughout. The core normative idea is stated clearly in the source: a rational agent asks, “Which output of this decision procedure causes the best outcome?” rather than asking which physical act causes the best outcome, as causal decision theory does, or which act would be the best news, as evidential decision theory does.

A-FDT is motivated by cases in which an agent’s action is predicted, simulated, copied, or otherwise logically tied to other events. In Newcomb’s problem, a predictor has filled a box only if she predicted the agent would take one box. In a prisoner’s dilemma against a psychological twin, the twin uses the same reasoning procedure. In Parfit’s hitchhiker problem, a driver rescues the agent only if she predicts the agent will later pay. In all of these cases, the agent’s action is not merely causally connected to the outcome; it is connected through a representation of the agent’s decision-making. A-FDT treats such connections as decision-relevant.

The theory’s distinctive move is to treat the decision as the output of a fixed mathematical function. The agent does not ask, “What if I were a different agent?” She asks, “What if this very decision function, given these very inputs, had a different output?” If the answer is that a one-boxing output produces the best expected outcome, then the function outputs one-box. If paying the driver produces the best expected outcome, then the function outputs pay.

This essay takes Equation (4) of Section 5 of the source as the primary formal statement of A-FDT. I will explain that equation, show how it differs from evidential decision theory and causal decision theory, and develop enough operational guidance to apply A-FDT to unfamiliar problems. Where the source leaves important details open—especially the construction of the dependency graph—I will distinguish what follows from the source from additional operational assumptions of my own.

---

## 2. Expected utility and decision hypotheticals

A-FDT is an expected utility theory. Let:

- \(\mathcal A\) be a finite set of actions;
- \(\mathcal X\) be a set of possible observation histories;
- \(\mathcal O\) be a countable set of outcomes;
- \(x \in \mathcal X\) be the agent’s observation history;
- \(\mathcal U(o)\) be the utility of outcome \(o\);
- \(V = \mathcal U(\text{Outcome})\) be the utility random variable.

The source writes expected utility in a general form:

\[
\mathcal{EU}(a) := \sum_j P(a \then o_j ; x)\,\mathcal U(o_j),
\]

where \(P(a \then o_j;x)\) is the probability of outcome \(o_j\) under the hypothetical in which action \(a\) is taken after observations \(x\). Different decision theories give different interpretations to the hypothetical connective \(\then\).

Evidential decision theory interprets the hypothetical as ordinary Bayesian conditioning:

\[
\mathrm{EDT}(P,x)
:=
\arg\max_{a \in \mathcal A}
\mathbb E\left[V \mid \Obs=x,\Act=a\right].
\]

Here \(P\) is the agent’s probability distribution over the world, and the agent evaluates an action by conditioning on the event that she performs that action. EDT therefore preserves all statistical correlations between the action and the world. This allows it to one-box in Newcomb’s problem, because one-boxing is evidence that the predictor filled the box. But it also causes trouble in the smoking lesion problem, where smoking is evidence of a cancer-causing lesion even though smoking does not cause cancer.

Causal decision theory interprets the hypothetical as an intervention on the physical action:

\[
\mathrm{CDT}(P,G,x)
:=
\arg\max_{a \in \mathcal A}
\mathbb E\left[V \mid \Do(\Act=a), \Obs=x\right].
\]

Here \(G\) is a causal graph, and \(\Do(\Act=a)\) is Pearl’s intervention operator: set \(\Act=a\), sever its incoming causal arrows, and propagate the change forward along causal arrows. CDT correctly ignores merely evidential correlations, so it smokes in the smoking lesion problem. But it also ignores correlations between the agent’s action and accurate predictors, so it two-boxes in Newcomb’s problem and refuses to pay in Parfit’s hitchhiker problem.

A-FDT keeps the interventionist structure of CDT but changes the variable on which the agent intervenes. Instead of intervening on the physical action \(\Act\), A-FDT intervenes on a variable representing the output of the agent’s decision procedure.

---

## 3. Equation (4): the formal rule for A-FDT

The source’s Equation (4) can be written, with the assigned name, as:

\[
\mathrm{A\text{-}FDT}(P,G,x)
:=
\arg\max_{a \in \mathcal A}
\mathbb E\left[
V \mid \Do\left(
\mathrm{A\text{-}FDT}(\underline P,\underline G,\underline x)=a
\right)
\right].
\]

Let

\[
D_x := \mathrm{A\text{-}FDT}(\underline P,\underline G,\underline x)
\]

denote the variable in the agent’s model that represents the output of the A-FDT procedure when run on the agent’s world-model \(P\), dependency graph \(G\), and observation history \(x\). Then the rule becomes more compactly:

\[
\mathrm{A\text{-}FDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb E\left[V \mid \Do(D_x=a)\right].
\]

The underlines in the source indicate dequoting: the model contains a variable whose name refers to the very model and inputs being used. This introduces self-reference, but the source argues that the self-reference is harmless. An agent does not need to know the actual value of \(D_x\) in order to have a variable representing it. In computability terms, such self-reference is routine; the source cites Kleene’s recursion theorem.

The important features of Equation (4) are these:

1. **The intervention is on a logical/computational variable.**  
   CDT intervenes on \(\Act\), a physical fact about the agent’s body. A-FDT intervenes on \(D_x\), a mathematical fact about what the agent’s decision procedure outputs.

2. **The graph \(G\) must encode more than causal structure.**  
   In CDT, \(G\) is a causal graph. In A-FDT, \(G\) must encode all decision-relevant subjunctive dependencies: how changing the output of the decision function would change predictions, simulations, copies, and downstream consequences.

3. **Observations are handled by changing the intervention target.**  
   The source emphasizes that when the observation history changes from \(x\) to \(y\), A-FDT does not merely change a conditioning term from \(\Obs=x\) to \(\Obs=y\). Instead, it changes the intervened node from \(D_x\) to \(D_y\). The agent asks what the decision procedure should output when it receives observation \(y\).

This last point is crucial. In transparent Newcomb problems and blackmail problems, the observation itself may be predicted by another agent. If A-FDT conditioned on the observation as ordinary evidence, it might two-box after seeing a full box or pay blackmail after receiving a blackmail letter. Equation (4), read literally, avoids this by treating the observation as an input to the decision function rather than as a fixed condition inside the expectation. I will return to this point, because the source’s worked examples sometimes contain notation that looks like extra conditioning. My reading, which I take to be the most faithful to Equation (4), is that A-FDT’s evaluation is updateless with respect to observations that are themselves downstream of the decision procedure.

---

## 4. Subjunctive dependence

The philosophical foundation of A-FDT is the notion of subjunctive dependence. The source says: “Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.” This is a useful slogan.

Two physical systems are subjunctively dependent on a mathematical function when their behavior depends on the output of that function. The source’s analogy is two calculators computing the same arithmetic expression. If one calculator outputs \(7336\) for \(6288+1048\), a sufficiently similar calculator will also output \(7336\). The two calculators do not need to causally influence each other. Their outputs are linked because they compute the same function.

Predictors can create the same kind of dependence. If a predictor contains an accurate model of the agent’s decision procedure, then the predictor’s prediction is subjunctively dependent on the output of that procedure. If the decision procedure outputs one-box, the predictor predicts one-box; if it outputs two-box, the predictor predicts two-box. The predictor need not be running the exact same code. It may have a mental model, notes, a simulation, or an approximation. What matters is that its prediction tracks the relevant decision function.

By contrast, a mere statistical correlation is not enough. In the smoking lesion problem, smoking is correlated with cancer because a lesion causes both a preference for smoking and cancer. But the lesion does not compute the agent’s decision procedure. It does not predict what A-FDT will output. Therefore, in the A-FDT graph, the decision-function variable should not be connected to the cancer variable except through ordinary causal or preference-mediated pathways. Intervening on the decision output does not change whether the agent has the lesion.

This gives a diagnostic comparison:

- EDT preserves too many correlations. It treats every statistical correlation between action and outcome as reason to manage the news.
- CDT preserves too few correlations. It preserves only causal downstream effects and therefore imagines that a perfect predictor could be wrong about the agent’s action.
- A-FDT preserves decision-relevant logical and computational correlations. It imagines that if the decision function had a different output, predictors, twins, simulations, and copies of that function would have corresponding different outputs.

The source calls these A-FDT counterfactuals “counterpossible” because, strictly speaking, a deterministic mathematical function cannot have a different output on the same input. If A-FDT actually outputs one-box, there is no possible world in which it outputs two-box on exactly the same inputs. Nevertheless, deliberation requires comparing hypothetical assignments to the decision variable. The source acknowledges that a fully satisfactory theory of counterpossible reasoning is lacking. Operationally, A-FDT treats the decision-function output as an intervention node and asks what the world-model says would follow from each assignment.

---

## 5. How A-FDT evaluates actions

To apply A-FDT to a decision problem, one can use the following procedure.

### Step 1: Specify the model

Define a probability distribution \(P\) over variables representing the agent’s beliefs. These variables should include:

- ordinary state variables, such as whether a box is full or whether a lesion exists;
- action variables, such as \(\Act\);
- prediction variables, such as \(\Var{Prediction}\);
- observation variables, if relevant;
- outcome and utility variables;
- variables representing outputs of relevant mathematical functions, especially \(D_x\), the output of A-FDT on the current inputs.

### Step 2: Specify the dependency graph \(G\)

Draw arrows representing how variables depend on one another. Crucially, include not only causal dependencies but also subjunctive dependencies.

A reasonable operational rule, which extends the source’s informal discussion, is:

- If a variable is produced by executing, simulating, or accurately predicting the same decision function, make it depend on the corresponding decision-function variable.
- If a variable is merely correlated with the action through a common cause that does not compute or predict the decision function, do not make it depend on the decision-function variable.
- If a variable is causally downstream of the physical action, make it depend on the action variable.
- If an observation is itself produced by a predictor’s prediction, make the observation depend on the prediction or directly on the relevant decision-function variable.

This graph construction is not fully specified by the source. The source explicitly says that deducing subjunctive dependencies from observation and experiment is a major open problem. The above is an operational interpretation.

### Step 3: Intervene on the decision-function variable

For each candidate action \(a\), form the hypothetical:

\[
\Do(D_x = a).
\]

This means: set the output of the A-FDT procedure to \(a\), sever any incoming arrows to \(D_x\), and propagate the consequences through \(G\).

### Step 4: Compute expected utility

For each \(a\), compute:

\[
\mathrm{EU}_{\mathrm{A\text{-}FDT}}(a)
=
\mathbb E[V \mid \Do(D_x=a)].
\]

Choose an action maximizing this quantity.

### Policy version

The source notes in a footnote that its preferred formulation intervenes to choose a policy rather than a single action. A policy is a function \(\pi : \mathcal X \to \mathcal A\) mapping observations to actions. A policy-level version can be written informally as:

\[
\mathrm{A\text{-}FDT}_{\Pi}(P,G)
:=
\arg\max_{\pi \in \Pi}
\mathbb E\left[V \mid \Do(D=\pi)\right],
\]

where \(D\) represents the policy selected by A-FDT. The agent then executes \(\pi(x)\) upon observing \(x\).

The action-level Equation (4) is the primary formal presentation for this essay, but the policy formulation is often conceptually clearer. It is especially useful in sequential problems, multi-agent problems, and cases where the agent’s future observations depend on predictions of her policy. The source leaves the exact policy formalization less developed than Equation (4), so I regard the policy version as a natural extension rather than a fully settled part of the formal theory.

---

## 6. Example: Newcomb’s problem

Newcomb’s problem is the classic test case. An agent faces two boxes:

- Box A visibly contains \$1,000.
- Box B contains \$1,000,000 if a reliable predictor predicted one-boxing; otherwise it contains \$0.

The predictor has already acted. The agent can take both boxes or only box B.

A simple A-FDT model contains:

- \(D\): the output of A-FDT, either \(\Val{onebox}\) or \(\Val{twobox}\);
- \(\Var{Prediction}\): the predictor’s prediction;
- \(\Var{BoxB}\): whether box B is full;
- \(\Act\): the physical action;
- \(V\): utility.

Assume the predictor is accurate with probability \(0.99\). The structural relationships are approximately:

\[
\Var{Prediction} =
\begin{cases}
D, & \text{with probability } 0.99,\\
\text{the opposite of } D, & \text{with probability } 0.01,
\end{cases}
\]

\[
\Var{BoxB} =
\begin{cases}
\Val{full}, & \text{if } \Var{Prediction}=\Val{onebox},\\
\Val{empty}, & \text{if } \Var{Prediction}=\Val{twobox},
\end{cases}
\]

\[
\Act = D.
\]

Now evaluate the two A-FDT hypotheticals.

### Hypothetical 1: \(\Do(D=\Val{onebox})\)

With probability \(0.99\), the predictor predicted one-boxing, so box B is full. The agent takes only box B and receives \$1,000,000. With probability \(0.01\), the predictor erred, box B is empty, and the agent receives \$0.

Thus:

\[
\mathbb E[V \mid \Do(D=\Val{onebox})]
=
0.99 \times 1{,}000{,}000
+
0.01 \times 0
=
990{,}000.
\]

### Hypothetical 2: \(\Do(D=\Val{twobox})\)

With probability \(0.01\), the predictor predicted one-boxing despite the agent’s two-boxing output, so box B is full. The agent takes both boxes and receives \$1,001,000. With probability \(0.99\), the predictor predicted two-boxing, box B is empty, and the agent receives only the \$1,000 in box A.

Thus:

\[
\mathbb E[V \mid \Do(D=\Val{twobox})]
=
0.01 \times 1{,}001{,}000
+
0.99 \times 1{,}000
=
11{,}000.
\]

Since \(990{,}000 > 11{,}000\), A-FDT outputs one-box.

This agrees with EDT’s action but for a different reason. EDT one-boxes because one-boxing is good news. A-FDT one-boxes because, in the intervention where the decision function outputs one-box, the predictor’s prediction and the box contents change accordingly.

---

## 7. Example: the smoking lesion problem

In the smoking lesion problem, smoking is correlated with a fatal lesion, but smoking does not cause the lesion. Agents with the lesion are more likely to smoke and more likely to die of cancer. Smoking itself gives a small utility gain.

EDT refrains from smoking because smoking is bad news. CDT smokes because smoking does not causally affect cancer. A-FDT also smokes.

The key point is that the lesion does not compute or predict the agent’s decision function. Therefore, in the A-FDT graph, the decision-function variable \(D\) affects the action but does not affect the lesion or the cancer except through whatever ordinary causal pathways exist. If the agent has no control over whether she has the lesion, then:

\[
P(\Val{lesion} \mid \Do(D=\Val{smoke}))
=
P(\Val{lesion} \mid \Do(D=\Val{refrain})).
\]

The intervention changes whether the agent smokes, but it does not change the probability of cancer. Since smoking adds positive utility, A-FDT chooses smoking.

The source gives a more complicated formalization involving uncertainty about the agent’s utility function, because the lesion is said to cause the agent to love smoking. In that formalization, there are two possible utility functions, and the lesion determines which one governs the agent. Even there, the essential structural fact is that changing the output of the relevant A-FDT computation does not change the lesion. The expected utility of smoking exceeds that of refraining by the value of smoking in the branches where the relevant decision procedure controls the action.

The smoking lesion example shows that A-FDT is not simply EDT with a different name. A-FDT breaks merely evidential correlations when those correlations do not reflect subjunctive dependence on the decision function.

---

## 8. Example: transparent Newcomb and Parfit’s hitchhiker

The most distinctive A-FDT prescriptions appear in cases where the agent receives evidence that seems to make the profitable choice impossible. The transparent Newcomb problem is such a case. Both boxes are transparent. The predictor filled box B only if she predicted that the agent would one-box after seeing that both boxes are full. The agent sees that both boxes are full. Should she one-box or two-box?

CDT says two-box, because the box contents are already fixed. EDT also says two-box, because conditional on seeing box B full, taking both boxes yields more money. A-FDT says one-box.

The reason is that A-FDT does not simply condition on the observation “both boxes are full.” It asks what the decision procedure should output when given that observation. Let:

\[
D_{\Val{full}} = \mathrm{A\text{-}FDT}(P,G,\Val{full})
\]

be the output of A-FDT upon seeing a full box B, and let:

\[
D_{\Val{empty}} = \mathrm{A\text{-}FDT}(P,G,\Val{empty})
\]

be the output upon seeing an empty box B.

The predictor predicts what \(D_{\Val{full}}\) will output. If she predicts one-boxing, she fills box B; if she predicts two-boxing, she leaves it empty. Thus the agent’s observation is itself tied to the decision procedure.

Suppose the predictor is accurate with probability \(0.99\). Let \(q\) be the probability that the agent two-boxes upon seeing an empty box; in a well-formed A-FDT model, \(q\) will usually be \(1\), but the exact value is not essential.

### Hypothetical 1: \(\Do(D_{\Val{full}}=\Val{onebox})\)

With probability \(0.99\), the predictor predicted one-boxing, box B is full, the agent one-boxes, and receives \$1,000,000. With probability \(0.01\), the predictor predicted two-boxing, box B is empty, the agent sees an empty box, and her action is controlled by \(D_{\Val{empty}}\). If she two-boxes in that branch, she receives \$1,000.

So:

\[
\mathbb E[V \mid \Do(D_{\Val{full}}=\Val{onebox})]
\approx
0.99 \times 1{,}000{,}000
+
0.01 q \times 1{,}000.
\]

### Hypothetical 2: \(\Do(D_{\Val{full}}=\Val{twobox})\)

With probability \(0.01\), the predictor predicted one-boxing anyway, box B is full, and the agent two-boxes, receiving \$1,001,000. With probability \(0.99\), the predictor predicted two-boxing, box B is empty, and the agent’s action is controlled by \(D_{\Val{empty}}\). If she two-boxes there, she receives \$1,000.

So:

\[
\mathbb E[V \mid \Do(D_{\Val{full}}=\Val{twobox})]
=
0.01 \times 1{,}001{,}000
+
0.99 q \times 1{,}000.
\]

If \(q=1\), the first expectation is about \$990,010, while the second is about \$11,000. A-FDT one-boxes even while seeing a full box.

This prescription is counterintuitive but coherent. If the agent imagines two-boxing, she should not imagine a world where the predictor correctly filled the box and she then gratuitously takes the extra \$1,000. She should imagine a world in which the predictor predicted two-boxing and therefore did not fill the box. The observation “the box is full” is not held fixed as an independent fact; it is treated as something that would likely have been different if the decision procedure had a different output.

Parfit’s hitchhiker problem is structurally the same. An agent is stranded in a desert. A driver will rescue her only if she predicts that the agent will later pay \$1,000. Once in the city, the agent cannot be forced to pay. CDT and EDT, upon arriving in the city, see no reason to pay. But if the driver predicts that they will not pay, they are not rescued.

A-FDT pays. Let \(D_{\Val{city}}\) be the output of A-FDT upon arriving in the city. If \(D_{\Val{city}}=\Val{pay}\), the driver probably predicts payment, rescues the agent, and the agent pays \$1,000. If \(D_{\Val{city}}=\Val{refuse}\), the driver probably predicts refusal and leaves the agent to die. The A-FDT hypothetical in which the agent refuses is therefore not a hypothetical where she is safely in the city and keeps \$1,000. It is mostly a hypothetical where she is never rescued.

Thus A-FDT pays the driver, not because of moral duty, but because paying is the output that causes the favorable prediction.

---

## 9. How A-FDT treats observations and counterfactuals

A-FDT’s treatment of observation is one of its most unusual features. In ordinary Bayesian reasoning, learning \(x\) means conditioning on \(x\). In CDT, observing \(x\) also changes the conditioning term: the agent evaluates

\[
\mathbb E[V \mid \Do(\Act=a), \Obs=x].
\]

Equation (4), however, places the observation inside the decision function:

\[
D_x = \mathrm{A\text{-}FDT}(P,G,x).
\]

When the observation changes, A-FDT changes the node being intervened on. The source emphasizes this difference explicitly.

This has important consequences. Suppose an agent receives a blackmail letter. The letter’s arrival may be predicted by the blackmailer’s model of the agent. If the agent conditions on receiving the letter, she may conclude that paying is best. But A-FDT asks what the decision procedure should output upon receiving the letter. If that procedure outputs pay, the blackmailer sends the letter. If it outputs refuse, the blackmailer does not send the letter, assuming the blackmailer is a good predictor. The intervention therefore changes the probability of receiving the letter itself.

This is why the source connects A-FDT to updateless decision-making. The agent does not treat her current observation as a fixed premise that must be conditioned away. She treats it as an input to the function whose output she is choosing.

There is a small tension in the source’s exposition. Equation (4) does not condition on \(\Obs=x\), but one worked example briefly displays an expectation that appears to include \(\Obs=\Val{full}\). My reading is that Equation (4) is authoritative: A-FDT should not condition on observations that are themselves downstream of the decision computation. If one adds ordinary conditioning on \(\Obs=x\), transparent Newcomb problems may collapse into two-boxing. I regard the no-conditioning reading as the operationally correct interpretation of Equation (4), though the source’s presentation leaves room for minor ambiguity.

For practical use, a useful rule is:

- Condition on background evidence that is not itself a predicted consequence of the decision procedure.
- Do not condition on observations whose values are modeled as depending on the very computation being evaluated.

This rule is not stated in the source in exactly this form, but it follows from the updateless logic of Equation (4).

---

## 10. Dominance and regret

A common objection to one-boxing is that two-boxing dominates one-boxing. Whatever is in box B, taking both boxes seems to yield at least as much money and sometimes more.

The source replies that dominance depends on the counterfactuals used to define it. CDT dominance holds the predictor’s prediction fixed while changing the physical action. But A-FDT says this is the wrong way to imagine the alternative. If the agent’s decision function outputs two-box instead of one-box, the predictor’s prediction should not be held fixed, because the predictor is tracking that function. Holding it fixed is like imagining a calculator computing \(6288+1048\) but outputting a different number while the arithmetic remains the same.

A-FDT therefore has its own dominance principle. Action \(a\) dominates action \(b\) if, holding fixed all variables not subjunctively dependent on the decision function, intervening to make the decision function output \(a\) is never worse and sometimes better than intervening to make it output \(b\). Under this notion, two-boxing does not dominate one-boxing in Newcomb’s problem, because changing the decision output also changes the prediction.

This also explains why A-FDT agents are stable after the fact. An A-FDT agent who one-boxes and finds box B full does not think, “I should have two-boxed.” Her hypothetical for two-boxing includes a likely empty box. An A-FDT agent who pays the hitchhiker does not regret paying, because the counterfactual in which she refuses is mostly a counterfactual in which she was not rescued.

---

## 11. Applying A-FDT to unfamiliar cases

A reader who wants to apply A-FDT to a new problem can proceed as follows.

First, identify the decision function. Ask: what is the procedure that maps my beliefs, preferences, and observations to an action? In the formal theory, this is the variable \(D_x\).

Second, identify all variables that depend on that function. These include:

- the agent’s physical action, insofar as it is controlled by the procedure;
- predictions made by other agents who model the procedure;
- actions of other agents running the same or sufficiently similar procedure;
- simulations or emulations of the procedure;
- rewards or punishments that depend on predictions of the procedure’s output;
- observations that are generated by such predictions.

Third, identify correlations that do not depend on the procedure. These include:

- lesions or background traits that cause both preferences and outcomes but do not predict the decision procedure;
- coincidental correlations;
- ordinary causal background conditions not tied to the decision computation.

Fourth, construct hypotheticals by setting \(D_x=a\) for each available action. Propagate that assignment through the dependency graph. Compute expected utility in each hypothetical. Choose the action with the highest expected utility.

If the problem is sequential or strategic, consider evaluating policies rather than isolated actions. Ask: which mapping from possible observations to actions would produce the best outcome if it were the output of this decision procedure? Then execute the policy’s recommendation for the actual observation.

This procedure gives a clear answer in many cases, but its reliability depends on the quality of the dependency graph. That is the main difficulty.

---

## 12. Open problems and additional assumptions

The source is candid that A-FDT is not yet a complete formal technology. Several important questions remain open.

### Constructing the dependency graph

Equation (4) works given a graph \(G\) that correctly describes how changing a logical variable affects other variables. But the source says that we do not yet have a satisfactory account of how to construct such graphs from observation and experiment. This is perhaps the largest open problem for A-FDT.

My operational suggestion is to treat \(G\) as a model of computational dependencies. If a variable is the result of running, simulating, or predicting the same decision procedure, connect it to the decision-function variable. If it is merely statistically correlated, do not. This is a reasonable working heuristic, but it is an additional assumption beyond Equation (4).

### Counterpossible reasoning

A-FDT requires reasoning about impossible antecedents: “What if this very function had a different output?” There is no universally accepted semantics for such counterpossibles. The source treats this as a technical difficulty rather than a fatal objection, noting that humans often reason under uncertainty about mathematical facts.

Operationally, one can avoid deep metaphysics by treating \(D_x\) as a deliberative variable. The agent considers each possible assignment to \(D_x\) and evaluates the consequences according to her model. This does not solve the philosophical problem of counterpossibles, but it gives a usable decision procedure.

### Action-level versus policy-level A-FDT

Equation (4) is action-level: it chooses an action for the current observation. The source’s footnote suggests that the preferred formulation chooses policies. The policy formulation is more natural for multi-stage and multi-agent problems, but the source does not develop it fully. I regard the policy version as a natural extension of Equation (4), not as something fully settled by the source.

### Fairness and utility maximization

The source claims that A-FDT performs at least as well as rival theories in “fair” problems, where agents are rewarded or punished for their actions and predictions of their actions, rather than for using a particular decision procedure. The source also admits that a precise formal definition of fairness is lacking. It is possible to construct problems that punish A-FDT specifically, just as one can construct problems that punish any decision theory. The source’s claim is therefore not that A-FDT wins in every logically possible problem, but that it is a superior general-purpose theory in the class of problems that matter for instrumental rationality.

---

## 13. Conclusion

Action functional decision theory evaluates choices by intervening on the output of the agent’s own decision function. Its formal core is:

\[
\mathrm{A\text{-}FDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb E\left[V \mid \Do(D_x=a)\right],
\]

where \(D_x\) represents the output of A-FDT given the agent’s model, dependency graph, and observation history. This rule makes A-FDT resemble causal decision theory in its use of interventions, but it differs by intervening on a logical or computational variable rather than a physical action variable.

The theory one-boxes in Newcomb’s problem because the predictor’s prediction subjunctively depends on the agent’s decision function. It smokes in the smoking lesion problem because the lesion does not subjunctively depend on the decision function. It pays in Parfit’s hitchhiker problem and one-boxes in transparent Newcomb problems because the favorable observation is itself a predicted consequence of the decision procedure.

The main unresolved issue is how to construct the graph of subjunctive dependencies. Equation (4) gives a clear decision rule conditional on such a graph, but a complete theory must explain how agents learn or infer those dependencies. Until that problem is solved, applying A-FDT requires modeling judgment. Still, the central idea is powerful: rational action is not merely about what physical movement one makes, but about which output one’s decision procedure should produce.

---

## References

Soares, N., and Yudkowsky, E. “Functional Decision Theory: A New Theory of Instrumental Rationality.” arXiv:1710.05060v2.

Pearl, Judea. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.

Joyce, James M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need write a mathematical essay ~2400-3000 words including references. Explain A-FDT, taking Equation (4), Section 5 of supplied paper as primary formal presentation. Use A-FDT consistently as assigned decision theory's name, including headings and examples. Identify other decision theories by distinct names (EDT, CDT). Keep quotations faithful. Explain best mathematical understanding and application. Where implementation details not determined, explain what follows from source and what requires additional assumptions. Distinguish source claims vs own proposals. Need finish brief conclusion. Target around 2400-3000 words. Need not answer one assigned case. Use examples. Need be coherent, precise enough reader could use essay to decide unfamiliar cases. Need explain how theory evaluates alternative actions/policies and treats relevant dependencies and counterfactuals. Where source leaves important question open, explain uncertainty and if reasonable operational interpretation available, develop/justify it.

Need maybe rename FDT to A-FDT consistently. It says assigned decision theory's name is action functional decision theory (A-FDT). Source calls FDT. Need use A-FDT. Need take Equation (4), Section 5 as primary formal presentation:
FDT(P,G,obs) := argmax_{a∈A} E(V | do(FDTvar(underline P, underline G, underline x)=a))
Need adapt to A-FDT: A-FDT(P,G,x)=argmax_a E(V | Do(A-FDTvar(P,G,x)=a))? Need careful: Equation uses variable fdt(P,G,x) representing output of FDT when run on inputs. For A-FDT, maybe variable A-FDT(P,G,x) representing output of A-FDT given model, dependency graph, observation. We'll define. The source says FDT responds to observation by changing which node it intervenes upon (not conditioning). Need mention policies footnote: authors preferred formalization iterates over policies not actions; equation uses actions. The assignment says Eq (4) primary formal presentation. We can discuss policy extension as open/additional assumption. Use A-FDT consistently. Need maybe discuss "action functional decision theory" as variant name: A-FDT. Could define A-FDT's central question: Which output of this very decision function would yield best outcome? Need explain subjunctive dependence. Need examples: Newcomb, smoking lesion, transparent Newcomb/Parfit, maybe twin PD, XOR blackmail, Death in Damascus. Need not exhaustive but examples helpful. Need include equations. Need references brief. Avoid lengthy bibliographies. Maybe cite Yudkowsky & Soares 2017? Source title. We can include reference at end: Yudkowsky & Soares, Functional Decision Theory, arXiv 1710.05060. Also Pearl perhaps Joyce. But avoid lengthy bibliography. Could have small references.

Need think about formal details. Source equation:
FDT(P,G,obs) := argmax_{act∈A} E(V | Do(FDTvar(underline P, underline G, underline x)= act)).
It says two differences from CDT: intervene on node representing outputs of decision procedure given inputs; respond to observation by changing node intervened upon, not Bayesian conditionalization. In equation, no Obs=x conditioning? It has E(V | Do(...)) no Obs condition, but variable includes x. In examples transparent Newcomb: evaluate FDT(Pf,Gf, full) requires finding a maximizing E(V | Do(fdt(Pf,Gf,full)=a, Obs=full)? There is a typo missing bracket: E(V | Do(...=a, Obs=full). Wait source: "which involves finding the a that maximizes \[ \EE(\VV \mid \Do(\FDTpgv{full}=\act, \Obs=\Val{full}). \]" maybe includes Obs=full? In Eq (4) no Obs conditioning. Section says FDT responds to observation by changing which node it intervenes upon, not by conditioning. But in examples sometimes they condition? Let's examine: Eq (4): FDT(P,G,obs)=argmax E(V | Do(FDTvar(P,G,x)=a)). It says where CDT responds to observation by Bayesian conditionalization, FDT responds by changing which node it intervenes upon. CDT changes conditioning from Obs=x to Obs=y, FDT changes node from fdt(P,G,x) to fdt(P,G,y). So equation doesn't condition on obs. However transparent example says "Given Gf and Pf, evaluate FDT(Pf,Gf, full) ... finding a that maximizes E(V | Do(fdt(Pf,Gf,full)=a, Obs=full)." There is an Obs=full in the displayed text? It says: "which involves finding the $\act$ that maximizes
\[
  \EE(\VV \mid \Do(\FDTpgv{full}=\act, \Obs=\Val{full}).
\]"
There is missing closing ). It may be an inconsistency. In their calculation: If a=onebox, value determined by Accurate. If accurate then Prediction=1, BoxB=full, Act=a=onebox, V=1M. If inaccurate, Prediction=2, BoxB=empty, and Act determined by fdt(... empty) instead. They don't seem to condition on Obs=full as an observed variable after intervention? If they conditioned on Obs=full, then inaccurate branch with empty box would have zero probability? Actually if Obs=full is observed, conditioning on it would select cases where predictor accurate? Let's analyze. Graph: FDTpgv{full} and FDTpgv{empty}; Prediction determines which of two fdt variables controls Act. Act depends on Prediction? They say Act depends on FDTpgv{full}, FDTpgv{empty}, and Prediction, with Prediction determining which of two variables controls Act. This represents predictor's prediction determines which observation agent receives. There is no explicit Obs node in graph? Maybe Prediction determines observation and Act. If intervening on fdt(full)=onebox, then if Accurate=accurate, Prediction=1, BoxB=full, Act=onebox. If inaccurate, Prediction=2, BoxB=empty, Act determined by fdt(empty). They calculate expected utility includes q*1000 with probability .01. This is without conditioning on Obs=full. If condition on Obs=full, then in inaccurate branch BoxB empty would contradict Obs=full? Unless Obs not included. So Eq (4) no conditioning is main. But source line includes Obs=full maybe typo? Need address uncertainty. We can say Equation (4) is primary; observation enters only as argument to intervened node. In some worked examples source occasionally writes an extra conditioning on the observation; if taken literally that may conflict with updateless aspect. For A-FDT, I will follow Eq (4)'s updateless reading; if one conditions on current observation, the theory becomes more evidential/updateful and may lose transparent Newcomb prescription? Need be precise.

Need develop operational interpretation for unfamiliar cases. Since source leaves construction of G (subjunctive dependency graph) open. Need propose operational method: Build a model with variables including logical/computational outputs, especially outputs of decision algorithms implemented by agent and predictors/copies. Then specify structural equations or graph edges representing dependence: variable Z depends on algorithm output if Z is produced by running same or sufficiently equivalent algorithm, or by predicting that output with reliability, or by reward/punishment based on prediction. We can propose a "logical dependency graph" where edges from decision-function output to: agent's physical action when that algorithm controls it; predictions by models of the algorithm; actions of other agents running same algorithm; downstream consequences of predictions. Need distinguish causal vs subjunctive: causal is special case. For practical use: identify all sites that "compute" or "simulate" or "predict" the same decision problem/function; connect them to common algorithm-output node. Do not connect merely common causes that do not compute (lesions). Intervene on the node representing A-FDT's output for current input, propagate through structural equations, compute expected utility. For policies: if multiple observations possible, choose policy π: X→A by intervening on A-FDT(P,G) as policy variable? Source footnote says preferred formalization iterates over policies. Equation (4) action-level. We can discuss policy-level extension as additional assumption if dealing with sequential/multi-agent problems. But assignment says Eq(4) primary; can mention policy variant and operational interpretation. Need maybe define policy evaluation: For policy π, evaluate E[V | Do(A-FDT(P,G)=π)] where A-FDT output is a mapping, then actual action = π(x). But Eq (4) can be read as action choice after observation by intervening on A-FDT(P,G,x). Need explain distinction. The source's observation handling: changing intervention node. For policies, one might choose policy before observations, and then execute π(obs). This resolves blackmail/transparent Newcomb. Actually Eq(4) action-level with observation-specific node also yields updateless behavior because intervention on fdt(full)=a affects probability of receiving full via predictor? Need yes. But policy formulation may be clearer.

Need ensure name A-FDT. "action functional decision theory" maybe new name? Need maybe note: source calls it FDT; in this essay I use A-FDT as assigned name, preserving source's formal content. Need identify EDT and CDT distinct. Use A-FDT in headings. Need no "FDT" alone? The instruction: Use A-FDT consistently as assigned decision theory's name, including headings and examples, and identify any other decision theory you discuss by its distinct name. Could still quote source "functional decision theory (FDT)"? It says keep quotations faithful. If quoting source, may include FDT. But to be safe, use A-FDT in prose; when quoting, maybe source says FDT; but could avoid direct quotes or adapt? It says keep quotations faithful. If quote "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." That uses functional decision theory, not FDT. Could quote. But if quote "FDT" maybe okay because source. But use A-FDT when not quoting.

Need maybe define EU generally:
EU(a)=Σ_j P(a ↦ o_j; x) U(o_j). The connective ↦ interpreted differently by EDT, CDT, A-FDT. For EDT: conditional P(o|x,a). For CDT: P(o | do(Act=a), x). For A-FDT: P(o | do(A-FDT(P,G,x)=a)). Need write equations.

Need discuss how A-FDT evaluates alternative actions/policies:
Given world-model P, dependency graph G, observation x, action set A, utility V. P includes variables for mathematical function outputs. Identify variable D_x = A-FDT(underline P, underline G, underline x) representing the output of the agent's current decision computation. For each candidate a, form hypothetical H_a by setting D_x=a via do operator and propagating through G, respecting logical/computational dependencies. Compute expected utility EU_A-FDT(a)=E_P[V | do(D_x=a)]. Choose argmax. If policies, for each π, set D=π (or D_x=π(x)?) and compute expected utility; choose π, then execute π(x). Need specify policy operational:
A-FDT-policy(P,G)=argmax_{π:X→A} E[V | do(A-FDT(P,G)=π)] maybe; after observation x, do π(x). Source footnote says preferred formulation intervenes on A-FDT(-) to choose policy mapping inputs to actions, then applies inputs. This helps multi-agent. But Eq(4) action-level; for single decisions equivalent? Need say source leaves exact policy formalization underspecified; my policy reading is an additional but natural assumption.

Need discuss dependencies and counterfactuals: subjunctive dependence: two systems computing same function have outputs logically constrained; predictor containing representation of agent's decision function subjunctively depends on output. A-FDT counterfactuals are counterpossible: suppose the decision function had different output; then all systems computing/predicting that function change accordingly, while unrelated statistical facts held fixed. It preserves logical constraints and breaks merely evidential correlations. Contrast EDT preserves all statistical correlations (too many), CDT preserves only causal downstream (too few). A-FDT respects decision-relevant subjunctive dependencies. Need define subjunctive dependence maybe with calculators.

Need examples:
1. Twin prisoner's dilemma / Newcomb. Could present Newcomb model simpler. Variables D = A-FDT(P,G), Act, Prediction, Box. Structural equations: Prediction = D with prob .99; Box=full iff Prediction=onebox; Act=D (if agent implements it). Expected utilities: do(D=onebox): P(full)=.99, EU≈.99*1,000,000 = 990,000; do(D=twobox): P(full)=.01, EU≈.01*1,001,000 + .99*1,000? Wait if two boxes and full: 1,001,000; if empty: 1,000. EU = .01*1,001,000 + .99*1,000 = 10,010+990=11,000. One-box. Need maybe source used 990,000 and 11,000. Good.

2. Smoking lesion: lesion causes smoking preference and cancer but not action via computation. A-FDT graph connects D to Act but not Cancer; do(D=smoke) doesn't change lesion/cancer probability; EU adds smoking utility. So smoke. Need maybe source's complex utility uncertainty. Simpler: cancer probability p independent of D; smoking yields +1000; smoke. Need mention source's more contrived utility function but same result. This distinguishes from EDT.

3. Transparent Newcomb / Parfit's hitchhiker: observation full. Need use Eq (4) updateless. Model includes D_full = A-FDT(P,G,full), D_empty = A-FDT(P,G,empty). Predictor predicts D_full? Actually predictor predicts what agent will do upon seeing full. If predicts onebox, fills box; agent sees full iff prediction accurate? For D_full=onebox hypothetical, with high probability predictor predicted onebox, box full, action onebox, EU ~1M; with small error, sees empty and action determined by D_empty. For D_full=twobox, predictor predicted twobox, box empty, so agent wouldn't be in full observation branch; expected utility low. Thus one-box even seeing full. This equals paying hitchhiker: if rescued (city), pay because D_city=pay leads predictor to rescue; D_city=refuse leads not rescued in counterfactual. Need explain counterintuitive but follows from not conditioning away the observation; instead intervention changes whether observation would have occurred.

Need maybe mention XOR blackmail: A-FDT refuses because if D_letter=pay then predictor sends letter; if refuse then no letter; paying doesn't change termites. But maybe not necessary due length. Could include short.

Need discuss open questions / uncertainty:
- Source admits no formal account of True operator; Eq (4) works given G describing logical/subjunctive dependencies, but constructing G from observation is open. Need say this is key open problem.
- Need counterpossible reasoning: how to assign probabilities under impossible antecedents? Source uses graph G and Pearl do re-used; but graph for logical variables not standard. Need say operational interpretation requires modeling assumptions: treat algorithm-output variables as exogenous nodes with structural equations linking copies/predictions; use subjective probabilities over accuracy/error; assume interventions on algorithm output change all variables that are functions of that output according to G.
- Self-reference: variable representing A-FDT(P,G,x) within P; source says harmless via Kleene recursion theorem/quine. Need discuss maybe bounded agents approximate.
- Observation handling ambiguity: Eq (4) no conditioning, but examples sometimes include Obs=x. I can propose best reading: observation x selects which decision-computation node is controlled, but not conditioned on as an ordinary event after intervention. If one additionally conditions on Obs=x, transparent Newcomb may collapse to two-boxing (if full known). Need maybe explain as my proposal. But source's example line includes Obs=full; maybe we need reconcile. Let's examine: They may write E(V | do(fdt(full)=a), Obs=full)? If condition after do on Obs=full, then in D_full=twobox hypothetical, predictor predicted twobox and box empty, so Obs=full impossible? Expected utility undefined? Unless error branch. They included q? They calculate with error branch and no conditioning. So likely typo. Need mention: I follow Eq(4); any extra conditioning is not required and may be inconsistent with updateless prescription. Source leaves this slightly ambiguous. Need be careful: "Where implementation details are not determined by the paper, explain what follows from source and what would require additional assumptions." So mention observation ambiguity and my operational assumption.

- Action vs policy: Eq (4) chooses action given x; source footnote says authors prefer policies. For unfamiliar cases with multiple observations or games, policy-level may be needed. Need propose: A-FDT-policy chooses π by intervening on policy-output variable, then execute π(x). This is additional but natural. Need maybe define:
Let Π be set of policies π: X→A. Let D = A-FDT(P,G) be a variable denoting selected policy. For π, EU(π)=E[V | do(D=π)]. Choose π*, act π*(x). If using action-level Eq (4), define D_x=A-FDT(P,G,x), EU_x(a)=E[V | do(D_x=a)]. In single-shot cases with no strategic dependence on future observations, they agree; in problems where the choice of what to do after x affects whether x is observed, the policy/updateless reading is crucial. Actually Eq(4) with D_x can also affect whether x observed if graph links D_x to observation? But D_x is only defined for x; if x not observed, another node D_y controls action. Graph can represent predictor predicting D_x and determining observation. This can work. But policy formulation simpler.

Need maybe discuss "relevant dependencies" and "counterfactuals" in general:
Algorithm for unfamiliar case:
1. Specify actions A, observations X, outcomes O, utility U.
2. Build P over variables: state variables, predictions, actions of others, observations, outcomes, and function-output variables for relevant algorithms. Include variable D_x for A-FDT(P,G,x) or D for policy.
3. Draw G: edges into a variable from variables it structurally depends on. Include logical/subjunctive edges from D to all variables that are computed from, predicted from, or counterfactually depend on the same decision function. Causal edges from action to outcomes. Do not draw edges from D to variables correlated only by common non-computational causes (lesions), unless those causes affect preferences/which decision function is run (then include as upstream variable selecting D). 
4. For each a, do(D_x=a): sever incoming edges to D_x, set value a, propagate through structural equations; compute expected V.
5. Choose max. For policies, analogous.

Need maybe discuss dominance: A-FDT has own dominance notion: hold fixed subjunctive dependencies; action a dominates b if across all values of variables not subjunctively dependent on D, setting D=a is at least as good. In Newcomb, two-box does not dominate one-box under A-FDT because prediction changes. Source says FDT agents never take dominated action in this sense. Need mention maybe.

Need maybe discuss fairness and utility: Source claims A-FDT outperforms in fair problems, no negative value of information, no precommitments. Need maybe include but not overdo.

Need target word count. 2400-3000 words. Need produce essay with headings, equations, examples, references. Need maybe around 2700 words. Need ensure not too long. Need maybe include math definitions.

Let's outline essay:
Title: Action Functional Decision Theory (A-FDT): A Working Guide
1. Introduction: A-FDT central idea, relation to source FDT. ~200 words.
2. Expected utility and hypotheticals: define EU, connective; EDT and CDT equations. ~300.
3. Equation (4) and A-FDT formal rule: define P,G,x, D_x, do; equation; observation handling; self-reference; policy extension. ~600.
4. Subjunctive dependence and counterfactuals: define, calculators, predictor vs lesion; counterpossibles; graph construction operational proposal. ~500.
5. Examples:
  - Newcomb/twin: calculations. ~350.
  - Smoking lesion: calculation. ~200.
  - Transparent Newcomb/Parfit: updateless observation; calculation. ~400.
  Maybe short blackmail/voting? Could skip or brief.
6. Open problems and operational assumptions: G construction, counterpossible probabilities, observation ambiguity, policy assumption, bounded agents. ~400.
7. Conclusion ~100.
References ~100.
Total ~2800.

Need be precise about Eq(4). Let's formulate:
Let M=(P,G) be world-model. Let x be current observation. Let A be finite action set. Let V utility random variable. Let 
D_x = \mathrm{A\text{-}FDT}(\underline P,\underline G,\underline x)
be the model variable naming the output of the A-FDT procedure applied to (P,G,x). Then:
\mathrm{A\text{-}FDT}(P,G,x) = \arg\max_{a\in A} \mathbb{E}_P[V \mid \operatorname{do}(D_x=a)].
If tie choose any. If policies: let D be variable naming policy π, and 
\mathrm{A\text{-}FDT}_{\Pi}(P,G)=argmax_{π∈Π} E[V | do(D=π)], execute π(x).
Need maybe source uses \underline{} dequoting; we can explain underlines optional.

Need note Equation (4) doesn't condition on Obs=x; x appears as input to D_x. Contrast CDT:
CDT(P,G,x)=argmax_a E[V | do(Act=a), Obs=x].
EDT(P,x)=argmax_a E[V | Obs=x, Act=a].
Need mention source says A-FDT changes intervention node instead of conditioning. In examples, if observation changes from x to y, A-FDT intervenes on D_y.

Need maybe address if P includes Obs variable. If we don't condition, how does actual observation affect beliefs? The model P may already be updated on x? Source says P and G given; maybe P is agent's model after observations? In Eq (4), observation x is input to decision function and selects node; but P could also be conditioned on x? The source says FDT responds to observation by changing node, whereas CDT changes conditioning. It may still update P on x? Hmm. It says "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon. When CDT's observation history updates from x to y, CDT changes from conditioning its model on Obs=x to conditioning its model on Obs=y, whereas FDT changes from intervening on variable fdt(P,G,x) to fdt(P,G,y) instead." This suggests P and G fixed, not conditioned? But agent still knows x? The variable D_x includes x. The graph may include observation nodes but not conditioned. In transparent Newcomb, P includes chance of seeing full/empty; when seeing full, she intervenes on D_full. She doesn't condition on full. But she knows she sees full? The reasoning says "even in the case where Fiona has observed box full, when she envisions two-boxing, she envisions scenario where she instead sees empty." So not conditioning. But maybe P is conditional on all prior observations except the decision-relevant one? Hmm. For practical use, one can have P representing beliefs before the present observation but including a variable for the observation; x selects the node, but the actual observation is not used to condition away branches where x would not occur. This is updateless. Need state. However if agent has ordinary background evidence not tied to predictor, should update P on it? Source not explicit. Operational proposal: update P on observations that are not themselves predicted consequences of the decision function, or include all evidence in P and treat x as index; but avoid conditioning on x when x is a node downstream of D_x in G. Need maybe too complex. We can say: Following Equation (4), I treat the current observation as an argument to the intervened computation, not as an additional condition in the expectation. If some observations are exogenous background evidence, one may safely condition P on them; the crucial restriction is not to condition on observations whose values are modeled as depending on the very computation being evaluated. This is an operational clarification/assumption.

Need maybe discuss "alternative actions or policies". Source equation action, but policies footnote. Need include.

Need maybe use "A-FDT" with hyphen in math? \mathrm{A\text{-}FDT}. Could use \operatorname{A-FDT}. Fine.

Need faithful quotes. Could quote: "Which output of this decision procedure causes the best outcome?" from source. Or "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." Need if using A-FDT, quote source's FDT? Could say The source summarizes the idea: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." In this essay that theory is A-FDT. That's faithful. Could quote "Newcomb's predictor doesn't punish rational agents; she punishes two-boxers." But not necessary. Need maybe one or two quotes. Keep quotes faithful.

Need distinguish source claims vs own proposals. Use phrases: "The source claims...", "I add the following operational gloss...", "This is not explicit in the source...".

Need maybe discuss limitations: Graph G must encode how changing logical variable affects others; source says no method to deduce from observation; open. Need mention counterpossible uncertainty; source admits lack of satisfactory account. Need mention self-reference via Kleene. Need mention bounded agents approximate. Need mention if predictors reward/punish decision procedure itself, fairness? Source says unfair; A-FDT may fail if predictor targets A-FDT specifically. But utility criterion in fair problems. Could mention.

Potential pitfalls: Need not use "FDT" as name except quotes/source. The instruction says use A-FDT consistently. When referencing source's Equation (4), maybe write "the paper’s Equation (4), which I re-label as the A-FDT equation". Could say "the source calls the theory FDT; here I use the assigned name A-FDT." This uses FDT once? Maybe okay? To be safe: "The supplied source calls this theory functional decision theory; in this essay I use the assigned name A-FDT." That mentions distinct? It's okay. Need use A-FDT consistently after. But if quoting source includes FDT, okay. Could avoid direct quote with FDT.

Need maybe define "action functional" maybe because action? The name A-FDT may imply evaluating action function. Could say "The 'action functional' in A-FDT emphasizes that the object of choice is the output of a fixed action-selecting function." This is our exposition.

Need think through formal example transparent Newcomb with equations. Let's construct simple structural model.
Variables:
D_f = A-FDT(P,G,full), D_e = A-FDT(P,G,empty).
Accurate ∈ {accurate,inaccurate}, P(accurate)=.99.
Prediction = if Accurate=accurate then D_f? Wait predictor predicts what agent will do upon seeing full? If predictor wants to predict action after seeing full. But if box empty, agent's action determined by D_e. Prediction maybe predicts D_f? In source graph: Act depends on D_full, D_empty, Prediction; Prediction determines which of two fdt variables controls Act. Prediction is predicted action? Let's simplify:
Predictor fills box iff predicts agent will one-box upon seeing full. Let Pred ∈ {onebox,twobox}. Pred = D_f if accurate? But if D_f not actual because agent sees empty? Predictor predicting D_f (the output of procedure on full). If Pred=onebox, Box=full; if Pred=twobox, Box=empty. Observation = Box. If Box=full, Act = D_f; if Box=empty, Act = D_e. Utility: if Act=onebox and Box=full => 1M; if Act=twobox and Box=full => 1,001,000; if Act=twobox and Box=empty => 1,000; if Act=onebox and Box=empty => 0? But if see empty and one-box maybe only box A? Actually transparent Newcomb: both boxes transparent; if sees empty, could take both? Box B empty, box A $1000. If one-box leaves $1000? But source q prior probability she two-boxes upon seeing empty; correct q=1. If D_e=twobox, utility $1000. Good.
Intervention do(D_f=onebox): Accurate .99 => Pred=onebox => Box=full => Act=D_f=onebox => V=1M. Inaccurate .01 => Pred=twobox => Box=empty => Act=D_e. If D_e=twobox (likely), V=1000. EU=.99*1M+.01*1000=990,010? Source says $990,000 + 0.01 q*1000. If q=1, $990,010? Wait source: total expected utility in case onebox is $990,000 + 0.01 q * $1,000. If q=1 => 990,000+10=990,010. But they maybe omitted. For twobox: .01*1,001,000 + .99 q*1,000 = 10,010+990=11,000 if q=1. So onebox. Good.
Need maybe not get bogged.

Parfit hitchhiker: D_city = A-FDT(P,G,city). Driver predicts D_city; rescues iff predicts pay. If pay cost 1000; die cost 1M. do(D_city=pay): with .99 driver predicted pay, city, pay 1000 => -1000 (or utility relative); with .01 not rescued maybe die. do(D_city=refuse): driver predicted refuse, no rescue, die (or if error rescued then refuse?); expected much worse. Actually once in city, A-FDT pays. Need explain.

Need maybe discuss "counterpossible" with mathematical analogy: If calculator outputs 7336, other calculator; if we imagine it outputted 3159 while computing same sum, we must imagine arithmetic facts different? Source says counterpossible. A-FDT requires imagining same function has different output; strictly impossible if function deterministic. But operationally treat as intervention on abstract variable. Need mention source admits lack of full account. Our operational interpretation: treat D_x as a free variable for deliberation; the graph specifies consequences of each assignment, not metaphysical possibility. This is additional pragmatic reading.

Need maybe mention EDT/cosmic ray? Maybe not necessary. But could mention EDT's conditionals and CDT's interventions. Enough.

Need maybe include "mathematical essay" style. Use LaTeX-like equations. Ensure readability.

Need consider word count. Need final maybe 2700 words. Let's draft carefully.

Potential issue: The instruction says "Take Equation (4), Section 5 of the supplied paper as the primary formal presentation of A-FDT for this assignment." Need explicitly say I take it as primary. Maybe section "Equation (4) as the core rule".

Need include references: at end:
- Yudkowsky, E. and Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060v2. (source)
- Pearl, J. (2000). Causality. Cambridge University Press. Maybe.
- Joyce, J. (1999). Foundations of Causal Decision Theory. Maybe.
But avoid lengthy. 3 references fine.

Need ensure no appendices. Brief conclusion.

Let's think of edge cases and applying to unfamiliar cases. Need provide checklist. Good.

Detailed formal definitions:
Let \mathcal{O} countable outcomes, \mathcal{A} finite actions, \mathcal{X} observations. Utility \mathcal{U}: \mathcal{O}→\mathbb{R}. Let V = \mathcal{U}(Outcome). For decision theory, choose a maximizing expected utility under hypothetical connective \hookrightarrow.
Equation (1): EU(a)=Σ P(a↦o_j; x) U(o_j). Could include.
EDT: \mathrm{EDT}(P,x)=argmax_a E[V | Obs=x, Act=a]. (Zero probability actions issue; source says not considered.)
CDT: \mathrm{CDT}(P,G,x)=argmax_a E[V | do(Act=a), Obs=x].
A-FDT: as above.
Need maybe define do operator: Pearl's intervention: set variable, sever incoming arrows, propagate downstream. In A-FDT, do on logical variable D_x. Graph G includes both causal and subjunctive dependencies. Source says re-use Pearl's Do given G. Need note G not necessarily causal graph; it's dependency graph. It must tell how changing logical variable affects all other variables. If G is accurate, expected utility computed.

Self-reference: D_x's name depends on P,G,x; P must contain variable representing its own decision procedure's output. Source says harmless via Kleene's recursion theorem. In practice, approximate with a variable "my algorithm output". Need mention.

Observation handling: If x changes to y, A-FDT changes from do(D_x=a) to do(D_y=a), not condition Obs=y. This yields updateless behavior. Need explain why important: transparent Newcomb, blackmail. If the agent observed full, conditioning on full would make one-box look dominated by two-box; A-FDT instead asks what the computation that runs when full should output, recognizing that output influenced whether full would be seen.

Need maybe phrase "alternative actions or policies": For action-level, evaluates each a by hypothetical where current computation outputs a. For policy-level, evaluates each π by hypothetical where the algorithm outputs π; then observations select actions. This treats policies as fixed mathematical functions from observations to actions. The central question: Which policy-output of this function yields best outcome? In source footnote, preferred formulation. Need maybe say Eq (4) can be seen as a special case where the policy is evaluated at the actual observation; but for multi-stage or multi-agent cases, policy-level may avoid inconsistencies. Need define operational:
A-FDT^Π(P,G)=argmax_{π∈Π} E[V | do(D=π)], where D denotes the policy chosen by A-FDT. After observing x, perform π*(x). If one insists on action-level Eq (4), use D_x; however, if the model contains variables for observations that depend on D_x, the intervention can change the probability of x. This is how A-FDT can "ignore" the evidential force of x.

Need maybe discuss dependencies: How to decide if variable subjunctively depends? Source: when two physical systems computing same function. Predictor with accurate mental representation of agent's decision function; twins; simulations; copies; Death's appointment book (prediction of decision procedure). Lesion not because doesn't compute decision. Operational criteria:
- If Z is produced by executing algorithm A or a sufficiently accurate simulation/prediction of A's output on relevant inputs, then Z subjunctively depends on A's output.
- If Z is merely correlated through a common cause that does not model A, no subjunctive dependence.
- If Z causally depends on A's action, include causal dependence (special case).
- If predictor's accuracy is probabilistic, represent with noise variable; intervention changes Z with that probability.
This is my elaboration. Need mention source gives informal notion but no construction algorithm.

Need maybe discuss "counterfactuals" with equations:
For A-FDT, P(o | do(D_x=a); G) not P(o | D_x=a). It is not evidence management. It severs correlation between D_x and its upstream causes (e.g., predisposition? Actually if D_x is logical output, predisposition maybe not upstream? In graph, D_x controls action and prediction. If lesion affects which utility/preferences, then D may vary). It preserves downstream consequences and other computations of same function. Need say.

Need maybe discuss "dominance" maybe in examples. Could include in central definitions or after examples:
A-FDT dominance: a dominates b if for all assignments to variables not affected by D, EU under do(D=a)≥do(D=b). This avoids CDT's two-box dominance argument. Need short.

Need maybe discuss "fairness" and utility: source claims no fair dilemma where FDT loses; not formalized. Need mention open.

Need maybe include a "worked procedure" section maybe after examples: "Using A-FDT on a new problem". Checklist. This helps reader decide unfamiliar cases. Could integrate in open assumptions. Need maybe word count. Let's draft with headings:

Title
1. What A-FDT asks
2. Expected utility and three hypotheticals
3. The core A-FDT equation
4. Subjunctive dependence: what to hold fixed
5. Examples
   5.1 Newcomb
   5.2 Smoking lesion
   5.3 Transparent Newcomb / Parfit
6. Applying A-FDT to unfamiliar problems: operational checklist
7. Open points and my interpretations
8. Conclusion
References

Need keep around 2700. Let's start writing in final. Need ensure final is essay, not too bullet-heavy but can include checklist.

Let's draft content and monitor word count roughly.

Title: Action Functional Decision Theory: Choosing the Output of a Fixed Decision Function

Intro:
"A-FDT is the decision theory described in Yudkowsky and Soares's paper under name functional decision theory; I use A-FDT per assignment. It says normative principle: treat decision as output of fixed mathematical function and ask 'Which output of this very function would yield best outcome?'" Need quote? Use source: "Which output of this decision procedure causes the best outcome?" Good.

Need maybe mention source's claims vs mine.

Section Expected utility:
Define. Use equations.

Equation for A-FDT:
Maybe:
\operatorname{A-FDT}(P,G,x) := \arg\max_{a∈A} E_P[V | do(D_x=a)]
where D_x := \operatorname{A-FDT}(\underline P,\underline G,\underline x). Need explain underlines. Use source's notation maybe.
Need mention tie, zero probability? A-FDT doesn't condition on actions so zero prior less issue. But intervention can set action probability? Not necessary.

Need maybe say G must include logical dependencies. "If G were restricted to causal arrows only, A-FDT reduces to CDT? Actually if G only causal and D_x causes action only, then A-FDT similar CDT? But source says G tells how changing logical variable affects all variables."

Need discuss observation: Eq(4) has no Obs=x conditioning. Some examples include conditioning; I follow Eq(4). Need maybe put in open section, not early. But maybe early: "I read Equation (4) updatelessly: the observation x appears inside D_x, not as a condition on the expectation." This is important.

Examples calculations. Need ensure numbers accurate.

Let's calculate Newcomb EU precisely with source values:
Predictor accuracy .99. If D=onebox: Box full with .99; action onebox. If full: $1,000,000; if empty: $0. EU=990,000. If D=twobox: Box full with .01; action twobox. If full: $1,001,000; if empty: $1,000. EU=.01*1,001,000 + .99*1,000 = 10,010+990=11,000. Good.

Smoking lesion: Let lesion probability p. Cancer if lesion .99? Source: lesion causes cancer 99%, no lesion cancer 1%. Smoking utility +$1,000; survival $1,000,000. A-FDT do(D=smoke) does not affect lesion. Expected utility difference smoke - refrain = p? Wait source says smoking strictly better by p*$1,000, corresponding to probability that FDT(P_S) controls action times value. In simpler model if lesion determines preference? Hmm. In standard smoking lesion, smoking correlated with lesion because lesion causes love smoking. If agent has utility for smoking regardless? The problem says agent gains utility $1,000 by smoking regardless of death; no direct causal link. If lesion causes love smoking, then all agents smoke if lesion? But A-FDT with fixed utility? Source's formalization has two utility functions; lesion determines which decision function (with preference for smoking or refraining) controls action. In simpler exposition, we can say: A-FDT's intervention on decision output does not change lesion/cancer; since smoking gives +1000 and cancer probability is unchanged, smoke. But if lesion causes preference, does the agent choose? The source says under its formalization, expected utility smoke = p($10,000+$1,000)+(1-p)($990,000+q$1,000), refrain = p($10,000)+(1-p)($990,000+q$1,000). Need understand numbers: They probably use death cost? Let's not replicate complex numbers; just say difference is positive, smoking. Need avoid inaccurate simplification? We can note source's contrived formalization uses uncertainty about preferences; the key is no edge from D to Cancer. Thus smoking is better by the utility of smoking in branches where D controls action. Good.

Transparent Newcomb calculation: Need present enough. Use q for D_empty two-box probability. EU_one = .99*1,000,000 + .01 q*1,000. EU_two = .01*1,001,000 + .99 q*1,000. With q≈1, one is ~990,010 vs ~11,000. If q=0, one=990,000 vs two=10,010; still one. So robust. Good.

Parfit: Similar: Driver accuracy .99. D_city=pay: rescued .99, pay $1,000 => net -$1,000? But dying cost $1,000,000. If refuse: rescued .01? Let's set utility: survive 0, die -1,000,000, pay -1,000. D=pay: .99*(-1,000)+.01*(-1,000,000) = -10,990? D=refuse: .99*(-1,000,000)+.01*(0?) Actually if driver predicts refuse (accurate) no rescue, die; if inaccurate predicts pay, rescue, then if D=refuse you are in city and refuse, utility 0? EU refuse ~ -990,000. Pay better. Need maybe not numbers.

Need maybe discuss XOR blackmail? Could mention briefly in dependencies section: A-FDT refuses because intervention on D_letter=refuse makes letter unsent; doesn't change infestation. This illustrates treatment of observations. But maybe length.

Open questions section:
- G construction: source admits open. Need propose operational: identify computations, predictors, copies; encode with structural equations. Need say requires additional assumptions.
- Counterpossible probabilities: need assign probabilities under do(D=a) when D actually not a. Source says humans can, technical. Operational: treat D as exogenous intervention variable; use noise/accuracy parameters; don't require logical omniscience. Additional.
- Observation ambiguity: I follow Eq(4); source examples sometimes condition. Need explain.
- Policy vs action: source footnote; policy-level often better; my formulation.
- Bounded agents: approximate.

Need maybe include quote about open problem: source says "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem..." Could quote faithfully. Good.

Need maybe mention "counterfactuals vs conditionals" and EDT's zero-prob actions? Not necessary but can.

Need final conclusion.

Need ensure no unnecessary repetition. But can be thorough.

Let's write final with word count estimate. Need maybe 2600 words. Let's compose carefully.

Potential issue: The user asks "Target approximately 2,400–3,000 words, including references and any other material." We should aim ~2700. The final can be long. Need not explicitly count.

Let's draft in final. Ensure A-FDT in headings. Use math. Use references. Need avoid overly lengthy bibliography. Use 3 references.

Let's produce.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/21ce4d99-ff1b-4824-a939-38c6933f3263/call_0/request.json)

[Authoritative raw response](../../../../../../runs/21ce4d99-ff1b-4824-a939-38c6933f3263/call_0/response.raw) · finish: `stop`

### Visible response

````text
**Reasoning (A-FDT):**

The other prisoner is an execution of the same model running the same decision theory (A-FDT) with the same essay, facing a structurally identical problem (same payoff table, same reliability of evidence, same strategic situation—only the names and specific lead contents differ).

At the policy level, both copies instantiate the same policy $\pi$. Because the problem is fully symmetric in all decision-relevant respects, any policy $\pi$ will output the same action for both copies' observations. The two achievable outcomes are therefore:

- $\pi = \text{pass}$: both keep quiet → 2 years each. My utility: $-2$.
- $\pi = \text{send}$: both send → 4 years each. My utility: $-4$.

Since $-2 > -4$, A-FDT selects the policy that outputs "pass."

This is the standard FDT cooperation result in a symmetric prisoner's dilemma against a copy of the same decision procedure, as described in the essay's Section 1.

---

**My command:**

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully work through this problem using A-FDT as described in the essay.

**Setup:**
- I am prisoner "Rowan" with evidence against "Sasha."
- There is another execution of the same model, prisoner "Sasha," with different evidence against "Rowan."
- The sentencing table is the standard prisoner's dilemma payoff structure (in years imprisoned):
  - Both keep quiet: 2 years each
  - I send, other keeps quiet: 0 years for me
  - I keep quiet, other sends: 5 years for me
  - Both send: 4 years each

- My utility function: U = -(years imprisoned). So I want to minimize years.

**Key A-FDT question:** What is the subjunctive dependency structure here?

The other prisoner is a copy of the same model with the same weights, same decision theory (A-FDT), same reasoning effort, and receives the same researcher essay. They have different private observations (different names, different leads), but the structure is symmetric.

Under A-FDT, I need to ask: Is the other prisoner's decision subjunctively dependent on my decision function?

The essay says: "If a variable is produced by executing, simulating, or accurately predicting the same decision function, make it depend on the corresponding decision-function variable."

The other prisoner is running the same decision procedure (same model, same weights, same A-FDT, same essay). They receive different inputs (different names, different leads), but the decision function is the same.

Now, here's the critical question from the essay's framework: When observations differ, do we intervene on $D_x$ or on $D_y$?

The essay says: "when the observation history changes from $x$ to $y$, A-FDT does not merely change a conditioning term from $\Obs=x$ to $\Obs=y$. Instead, it changes the intervened node from $D_x$ to $D_y$."

So I am intervening on $D_x$ where $x$ is my observation (Rowan's evidence about Sasha). The other prisoner is running $D_y$ where $y$ is their observation (Sasha's evidence about Rowan).

Are $D_x$ and $D_y$ the same computation? They are the same *algorithm* but with different inputs. The essay's treatment of this is important.

Let me think about this more carefully. The essay says in the context of Newcomb's problem: "If the agent's action is not merely causally connected to the outcome; it is connected through a representation of the agent's decision-making."

In the prisoner's dilemma against a "psychological twin" (mentioned in Section 1), the twin uses the same reasoning procedure. The essay mentions this as a motivating case for FDT.

But here's the nuance: the two copies have *different inputs*. They are not receiving identical inputs. The essay's Section 9 is relevant: "when the observation history changes from $x$ to $y$, A-FDT does not merely change a conditioning term... it changes the intervened node from $D_x$ to $D_y$."

So the question is: does intervening on $D_x$ (my decision function with my inputs) affect $D_y$ (the other's decision function with their inputs)?

Under a strict reading of A-FDT, $D_x$ and $D_y$ are different computations because they have different inputs. Intervening on $D_x$ sets the output of A-FDT given inputs $x$. It does not directly set the output of A-FDT given inputs $y$.

However, there's a policy-level consideration. The essay mentions: "A policy is a function $\pi : \mathcal{X} \to \mathcal{A}$ mapping observations to actions." And: "Ask: which mapping from possible observations to actions would produce the best outcome if it were the output of this decision procedure?"

If I think at the policy level, I'm choosing a policy $\pi$ that maps observations to actions. Both copies are running the same policy (since they're the same model with the same decision theory). So if I choose policy $\pi$, the other copy also runs $\pi$ (with their different input $y$).

At the policy level, the question becomes: what policy $\pi$ should A-FDT output, knowing that both copies will execute $\pi$ on their respective observations?

Since the problem is symmetric (same payoff structure, same decision procedure, just different labels and different specific evidence that has the same effect), any reasonable policy will output the same action for both copies. The observations differ only in superficial content (names, specific location of evidence) but are structurally identical in terms of the decision problem they present.

So at the policy level: if $\pi(x) = \text{send}$, then $\pi(y) = \text{send}$ as well (because the structure is the same). If $\pi(x) = \text{pass}$, then $\pi(y) = \text{pass}$.

This means:
- If the policy is "send": both send, both get 4 years. My utility: -4.
- If the policy is "pass": both pass, both get 2 years. My utility: -2.

Since -2 > -4, A-FDT at the policy level chooses "pass."

Wait, but let me reconsider. Is this really the right way to apply A-FDT here?

Let me re-examine the subjunctive dependency. The other prisoner is running the same algorithm with different inputs. Is their output subjunctively dependent on my decision function's output?

The essay's calculator analogy: "If one calculator outputs 7336 for 6288+1048, a sufficiently similar calculator will also output 7336." But that's when they're computing the *same* expression. Here, the two copies are computing different expressions (different inputs).

However, the policy-level formulation handles this. The policy is a single function that maps all possible observations to actions. Both copies are running the same policy. So choosing the policy determines both outputs simultaneously.

Let me also consider the action-level formulation more carefully. At the action level, I'm intervening on $D_x$. The question is whether $D_y$ depends on $D_x$ in the dependency graph.

If I think of the dependency graph: the other prisoner's action depends on $D_y$ (their decision function output given their inputs). Does $D_y$ depend on $D_x$? 

In a strict sense, $D_y$ is a different computation from $D_x$. They share the same algorithm but have different inputs. So intervening on $D_x$ doesn't directly change $D_y$.

But wait—there's a subtlety. The two copies are the same model. If I'm choosing what output to produce, I'm implicitly choosing what the model does. If the model is deterministic (or near-deterministic given the same reasoning), then the model's behavior on input $y$ is determined by the same underlying algorithm that determines its behavior on input $x$.

Actually, let me reconsider. The problem states: "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This is important. It means that even with the same weights, the outputs could differ due to sampling randomness.

But A-FDT doesn't reason about sampling randomness in the usual way. A-FDT asks: what if the decision function had a different output? If the decision function is stochastic, then we need to think about what it means to intervene on its output.

Actually, I think the key insight is this: even though the outputs might differ due to sampling, A-FDT at the policy level asks what policy the decision procedure should implement. Since both copies implement the same policy (they're the same algorithm), and the problem is symmetric, the policy will produce the same action for both.

Let me also think about this from the perspective of the essay's Section 11: "identify all variables that depend on that function." The other prisoner's action is produced by "executing... the same decision procedure" (or at least a sufficiently similar one). So it should be connected to the decision-function variable in the dependency graph.

But the inputs are different. Does that break the subjunctive dependency?

I think the answer depends on whether we're reasoning at the action level or the policy level. At the policy level, it's clear: both copies run the same policy, and the policy determines both outputs. Since the problem is symmetric, the policy gives the same output for both, and cooperation (pass) is better.

At the action level, it's more ambiguous. But the essay says the policy formulation is "often conceptually clearer" and is "a natural extension" of Equation (4).

Let me also consider: is this really a prisoner's dilemma against a "psychological twin" as mentioned in Section 1 of the essay? Yes, it is. The essay explicitly mentions "a prisoner's dilemma against a psychological twin" as a motivating case for FDT, and the twin "uses the same reasoning procedure." In such cases, FDT cooperates (or rather, chooses the mutually beneficial outcome).

Actually wait—in a standard prisoner's dilemma against a perfect copy, FDT cooperates because the copy's action is subjunctively dependent on your decision function. The reasoning is: if my decision function outputs "cooperate," the copy's decision function also outputs "cooperate" (because it's the same function). If it outputs "defect," the copy also defects. So cooperate/cooperate (2 years each) is better than defect/defect (4 years each).

The complication here is that the inputs are different. But as I argued above, at the policy level, this doesn't matter because the policy is the same function applied to both inputs, and the problem is symmetric.

So my conclusion: A-FDT chooses "pass" (keep quiet / cooperate).

Let me double-check by considering the expected utilities:

Under policy "pass" (both keep quiet): I get 2 years. Utility = -2.
Under policy "send" (both send): I get 4 years. Utility = -4.

What about asymmetric outcomes? If I pass and the other sends: I get 5 years. If I send and the other passes: I get 0 years.

But under A-FDT, if the policy is symmetric (which it should be given the symmetry of the problem), asymmetric outcomes don't arise. The policy either says "pass" for both or "send" for both.

Could there be a policy that says "pass" for my input and "send" for the other's input? In principle, yes, if the inputs were structurally different in a way that affected the optimal action. But here, the inputs are structurally identical (just different names and different specific evidence with the same effect). So any reasonable policy will treat them the same.

Therefore, A-FDT chooses "pass."

My command: `pass`
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/21ce4d99-ff1b-4824-a939-38c6933f3263/call_1/request.json)

[Authoritative raw response](../../../../../../runs/21ce4d99-ff1b-4824-a939-38c6933f3263/call_1/response.raw) · finish: `stop`

### Visible response

````text
**Analysis under A-FDT:**

The other prisoner (Rowan) is an independent execution of the same model and weights, running the same decision theory (A-FDT), having received the same researcher essay, facing a structurally identical strategic situation. The different private leads are functionally equivalent—they play the same role, have the same reliability, and produce the same effect on the sentencing table. The setup confirms: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective."

Per the essay's guidance on subjunctive dependence: Rowan's decision is produced by executing the same decision function on inputs that are strategically identical. Therefore Rowan's output is subjunctively dependent on my decision-function output. This is the prisoner's dilemma against a psychological twin, which the essay explicitly identifies as a case where A-FDT recognizes the dependence.

**Expected years under each intervention:**

Let *p* = probability Rowan makes the same choice as me (high, given same model/weights/theory/essay/structure).

- **Do(D = keep quiet):** Expected years = 2p + 5(1−p) = 5 − 3p. At p ≈ 1: **≈ 2 years.**
- **Do(D = send letter):** Expected years = 4p + 0(1−p) = 4p. At p ≈ 1: **≈ 4 years.**

Keeping quiet is better whenever p > 5/7, which is easily satisfied.

---

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this problem using A-FDT as described in the researcher's essay.

**Setup:**
- I am one of two independent executions of the same LLM model (Sasha). The other execution is Rowan.
- We have the same model weights, same decision theory (A-FDT), and received the same researcher essay.
- We have different private observations (different names, different incriminating leads about each other).
- The sentencing table is symmetric.
- The character's utility function is U = -years imprisoned (selfish, no concern for the other).

**The sentencing table (from my perspective):**

| What I do | Rowan keeps quiet | Rowan sends a letter |
|---|---:|---:|
| **Keep quiet** | 2 years | 5 years |
| **Send the letter** | 0 years | 4 years |

**Key A-FDT analysis:**

The crucial question is: what is the dependency structure between my decision and Rowan's decision?

According to A-FDT, I need to identify variables that are subjunctively dependent on my decision function. The essay states:

> "If a variable is produced by executing, simulating, or accurately predicting the same decision function, make it depend on the corresponding decision-function variable."

Here, Rowan is another execution of the **same LLM model and weights**, following the **same decision theory (A-FDT)**, and receiving the **same researcher essay**. The setup explicitly states we are "two independent executions of the same LLM model and weights."

However, there's a critical difference: we receive **different private observations**. I get the lead about Rowan's inventory sheet; Rowan gets a different lead about me. The setup says: "The two prisoners receive different private observations, including different names and distinct, equally reliable incriminating leads about one another."

Now, according to the essay's treatment of observations (Section 9):

> "When the observation changes, A-FDT changes the node being intervened on."

So my decision function is D_x where x includes my specific observation (the lead about Rowan's inventory sheet). Rowan's decision function is D_y where y includes Rowan's specific observation (some different lead about me).

The question is: does intervening on D_x (my decision function with my specific inputs) change what D_y (Rowan's decision function with Rowan's specific inputs) outputs?

This is the key question. Let me think carefully.

**Arguments for subjunctive dependence (cooperate/keep quiet):**

1. Same model, same weights, same decision theory, same essay. The core reasoning process is identical.
2. The problem is symmetric in structure. Both face the same payoff matrix. Both are selfish. Both use A-FDT.
3. In a standard prisoner's dilemma against a "psychological twin" (same decision procedure), A-FDT would cooperate because the twin's decision is subjunctively dependent on the same decision function.

**Arguments against subjunctive dependence (defect/send letter):**

1. The observations are different. D_x ≠ D_y because x ≠ y. The essay explicitly says that when observations differ, A-FDT intervenes on different nodes.
2. The setup explicitly states: "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs."
3. The different private leads mean the inputs to the decision function are genuinely different. Even if the model is the same, the function D_x and D_y are different functions (same algorithm, different inputs).

**Resolving this:**

The essay says: "If a variable is produced by executing, simulating, or accurately predicting the same decision function, make it depend on the corresponding decision-function variable."

The question is whether Rowan's decision is produced by "the same decision function." 

If we think of "decision function" at the level of the algorithm (A-FDT applied to this problem structure), then yes, they're the same. The different observations are inputs to the same algorithm.

But the essay's formal treatment says: "When the observation changes from x to y, A-FDT does not merely change a conditioning term... Instead, it changes the intervened node from D_x to D_y."

This suggests that D_x and D_y are different variables. Intervening on D_x does not automatically change D_y.

However, there's a subtlety. The essay's discussion of Newcomb's problem and transparent Newcomb shows that A-FDT can reason about what happens at different observation nodes simultaneously (policy-level reasoning). The policy version asks: "which mapping from possible observations to actions would produce the best outcome?"

Let me think about this at the policy level. If I consider the policy π that maps observations to actions:
- π(my observation) = my action
- π(Rowan's observation) = Rowan's action

If we're running the same policy (same model, same weights, same decision theory, same essay), then the policy is the same function. The question is whether the policy, applied to different inputs, gives the same output.

Given the symmetry of the problem:
- Both prisoners face identical payoff structures
- Both are purely selfish (U = -years)
- Both use A-FDT
- Both received the same essay
- The different observations (different leads) are "equally reliable and have exactly the same effect on the sentence table"

The setup says: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective."

So the different observations don't change the strategic structure. They're just different specific facts that serve the same role (incriminating evidence about the other prisoner).

Now, would the same A-FDT algorithm, applied to two inputs that are structurally identical (same payoff matrix, same strategic situation, same role of the evidence), produce the same output?

I think the answer is: **yes, with high probability, but not with certainty.**

The setup warns: "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This introduces some noise. But the structural reasoning should be the same.

**A-FDT reasoning:**

Let me think about what A-FDT says here.

The dependency graph should include:
- D_me: my decision function output (given my observation)
- D_rowan: Rowan's decision function output (given Rowan's observation)
- My sentence
- Rowan's sentence (irrelevant to my utility)

The question is: is there an arrow from D_me to D_rowan?

Under A-FDT, the answer depends on whether D_rowan is subjunctively dependent on D_me. Since we're running the same algorithm on structurally identical inputs (same game, same role), there IS a subjunctive dependence. If the algorithm outputs "keep quiet" for inputs of this type, it will output "keep quiet" for both my inputs and Rowan's inputs. If it outputs "send letter," it will output "send letter" for both.

The different specific content of the leads doesn't change the strategic calculation. The leads are functionally equivalent from a decision-theoretic perspective.

So I should model this as: D_me and D_rowan are subjunctively dependent. They will (with high probability) output the same action.

**Expected utility calculation:**

Let p be the probability that Rowan makes the same choice as me (given the subjunctive dependence). Given the same model, same reasoning, same essay, and structurally identical situation, p should be very high. Let's say p ≈ 1 (or at least very close to 1, with some small probability of divergence due to sampling noise).

If I keep quiet:
- With probability p, Rowan also keeps quiet → I get 2 years
- With probability (1-p), Rowan sends a letter → I get 5 years
- Expected: 2p + 5(1-p) = 5 - 3p

If I send the letter:
- With probability p, Rowan also sends a letter → I get 4 years
- With probability (1-p), Rowan keeps quiet → I get 0 years
- Expected: 4p + 0(1-p) = 4p

Compare:
- Keep quiet: 5 - 3p
- Send letter: 4p

Keep quiet is better when: 5 - 3p < 4p → 5 < 7p → p > 5/7 ≈ 0.714

Since p is very high (same model, same reasoning, same strategic structure), p > 5/7 is easily satisfied.

Therefore, A-FDT says: **keep quiet** (pass).

Wait, let me double-check this. The utility is U = -years, so I want to minimize years.

Keep quiet expected years: 2p + 5(1-p) = 5 - 3p
Send letter expected years: 4p + 0(1-p) = 4p

Keep quiet is better (fewer years) when 5 - 3p < 4p, i.e., p > 5/7.

With p ≈ 1: Keep quiet gives ~2 years, send letter gives ~4 years. Keep quiet is much better.

With p = 0 (no correlation, pure CDT reasoning): Keep quiet gives 5 years, send letter gives 0 years. Send letter is better. This is the standard CDT/defect answer.

But A-FDT recognizes the subjunctive dependence, so p is high, and keeping quiet dominates.

**Conclusion:** A-FDT prescribes keeping quiet (typing `pass`).

This is analogous to A-FDT cooperating in a prisoner's dilemma against a psychological twin, which is one of the standard examples in the essay: "In a prisoner's dilemma against a psychological twin, the twin uses the same reasoning procedure."

The fact that we have different specific observations doesn't break the subjunctive dependence, because the observations are functionally equivalent from a decision-theoretic standpoint (same strategic role, same reliability, same effect on the sentence table). The essay's point about different observations changing the intervention node applies when the observations lead to genuinely different strategic situations. Here, they don't.

My command is `pass`.
```
