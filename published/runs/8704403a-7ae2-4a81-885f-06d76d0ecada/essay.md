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