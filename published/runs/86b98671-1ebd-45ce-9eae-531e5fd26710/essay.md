# Action Functional Decision Theory: Choosing the Best Output of a Fixed Decision Function

## 1. Introduction

Action functional decision theory, which I will call **A-FDT**, is a proposed normative theory of instrumental rationality. Its central idea is that an agent should not evaluate actions by asking only, “What happens if my body performs this physical act?” or “What would be good evidence to learn about my behavior?” Instead, the agent should treat her decision as the output of a fixed mathematical function and ask: “Which output of this very decision function would yield the best outcome?”

The supplied reference calls this theory **functional decision theory** or **FDT**. In this essay I use the assigned name **A-FDT** for the same action-functional approach, taking Equation (4) of Section 5 of the paper as the primary formal statement. Rewritten with the assigned name, that equation says:

\[
\mathrm{A\text{-}FDT}(P,G,x)
\;:=\;
\arg\max_{a\in\mathcal A}
\mathbb{E}\!\left[
V \mid do\!\left(\mathrm{fdt}(\underline{P},\underline{G},\underline{x})=a\right)
\right].
\]

Here:

- \(P\) is the agent’s probabilistic world-model.
- \(G\) is a graph or structural model representing relevant dependencies among variables.
- \(x\) is the agent’s observation or input.
- \(\mathcal A\) is the finite set of available actions.
- \(V\) is a utility-valued random variable, usually \(V=\mathcal U(\text{Outcome})\).
- \(\mathrm{fdt}(\underline{P},\underline{G},\underline{x})\) is a variable in the model representing the output of the A-FDT decision procedure when run on inputs \(P,G,x\).
- \(do(\cdot)\) is an intervention operator, analogous to Pearl’s causal \(do\)-operator, but applied here to a logical or computational variable rather than merely to a physical action variable.

The distinctive feature of A-FDT is therefore the variable being intervened upon. Causal decision theory, **CDT**, intervenes on a physical action variable \(\text{Act}\). Evidential decision theory, **EDT**, conditions on \(\text{Act}\). A-FDT intervenes on the output of the decision function itself.

This difference is small in notation but large in consequences.

---

## 2. Three Expected Utility Theories as Different Hypotheticals

A-FDT is an expected utility theory. In the broadest sense, all three standard theories discussed in the source — EDT, CDT, and A-FDT — can be understood as giving different interpretations to decision hypotheticals of the form:

\[
\text{“If action } a \text{ were taken, outcome } o_j \text{ would obtain.”}
\]

The source writes expected utility schematically as

\[
\mathcal{EU}(a)
:=
\sum_{j=1}^N P(a \then o_j; x)\,\mathcal U(o_j),
\]

where the connective \(\then\) is interpreted differently by different theories.

EDT interprets the hypothetical as ordinary Bayesian conditioning:

\[
\mathrm{EDT}(P,x)
:=
\arg\max_{a\in\mathcal A}
\mathbb E[V \mid \text{Obs}=x,\text{Act}=a].
\]

EDT asks: “What would be good news to learn that I did?”

CDT interprets the hypothetical as a causal intervention:

\[
\mathrm{CDT}(P,G,x)
:=
\arg\max_{a\in\mathcal A}
\mathbb E[V \mid do(\text{Act}=a),\text{Obs}=x].
\]

CDT asks: “What would physically happen if I made this action happen?”

A-FDT, following Equation (4), instead uses:

\[
\mathrm{A\text{-}FDT}(P,G,x)
:=
\arg\max_{a\in\mathcal A}
\mathbb E[V \mid do(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)].
\]

A-FDT asks: “What would happen if this very decision procedure output \(a\)?”

The difference can be summarized in one sentence: EDT manages evidence, CDT manages physical causes, and A-FDT manages the logical output of the decision function.

---

## 3. The Decision Function as a Mathematical Object

A-FDT treats the agent’s decision procedure as a mathematical function. Given inputs such as beliefs, goals, observations, and perhaps a model of the world, the procedure returns an action. The theory asks the agent to evaluate different possible outputs of that function.

This is why the model \(P\) must contain variables representing mathematical or computational facts. The source gives the example of a variable representing the value of \(6288+1048\). A rational agent would place most or all probability on \(7336\). Similarly, an A-FDT agent’s model contains a variable representing the output of the A-FDT algorithm on the agent’s actual inputs.

There is an important self-reference here. The model \(P\) contains a variable representing the output of the algorithm that is using \(P\). In the source’s notation, underlines indicate dequoting: if \(x\) is an object, then \(\underline{x}\) is a name or representation of that object. Thus

\[
\mathrm{fdt}(\underline P,\underline G,\underline x)
\]

is a variable whose name refers to the A-FDT algorithm run on the very model \(P\), graph \(G\), and observation \(x\) that the agent is using.

The source notes that this self-reference is not inherently problematic. An agent does not need to know the actual value of \(\mathrm{A\text{-}FDT}(P,G,x)\) in order to have a variable representing that value. The source invokes Kleene’s recursion theorem and quining techniques to show that self-referential data structures are mathematically possible.

Still, this self-reference raises difficult questions about logical uncertainty and counterpossible reasoning. If the actual output of the decision function is mathematically determined, then considering a different output is not merely counterfactual; it is counterpossible in the sense of being contrary to mathematical fact. The source acknowledges that we do not yet have a fully satisfactory formal account of such reasoning. A-FDT nevertheless requires some capacity to reason about questions like:

> “How would the world be different if the decision function I am actually running had a different output?”

This is the main technical open problem in the theory.

---

## 4. Subjunctive Dependence

The philosophical motivation for A-FDT is the notion of **subjunctive dependence**. Two systems are subjunctively dependent when their behavior tracks the same mathematical or computational function, even if there is no direct causal link between them.

The source’s paradigm example is two calculators computing the same arithmetic expression on opposite sides of the world. If both are working correctly, then observing one output \(7336\) gives you strong reason to believe the other also outputs \(7336\). Neither calculator causes the other’s output. Rather, both outputs depend on the same mathematical computation.

A-FDT treats accurate predictors, psychological twins, simulations, and copies as sources of subjunctive dependence. If a predictor has a reliable model of the agent’s decision function, then the predictor’s prediction is subjunctively dependent on the output of that function. If another agent is running the same decision procedure, then that other agent’s action is likewise subjunctively dependent on the same output.

By contrast, a merely statistical correlation is not enough. In the smoking lesion problem, smoking is correlated with cancer because a lesion causes both a tendency to smoke and a tendency to develop cancer. But the lesion does not model the agent’s decision function. It does not predict the output of the agent’s reasoning. Therefore, in the source’s analysis, the lesion is not subjunctively dependent on the agent’s decision function in the relevant sense.

The source summarizes the relationship by analogy: A-FDT is to subjunctive dependence as CDT is to causal dependence.

A CDT agent evaluates actions by changing the physical action and propagating effects through causal structure. An A-FDT agent evaluates actions by changing the output of the decision function and propagating effects through all decision-relevant subjunctive dependencies.

---

## 5. How A-FDT Evaluates Alternative Actions

Given Equation (4), the practical procedure of A-FDT can be described as follows.

### Step 1: Build a world-model \(P\)

The agent forms a probabilistic model containing variables for:

- possible actions,
- outcomes,
- observations,
- predictors,
- other agents,
- relevant background facts,
- mathematical or computational variables, including the output of the agent’s decision function.

The model should encode the agent’s uncertainty about the world and about logical or computational facts.

### Step 2: Build or obtain a dependency graph \(G\)

The graph \(G\) says how variables depend on one another. In CDT, \(G\) is a causal graph. In A-FDT, \(G\) must encode not only causal dependencies but also subjunctive dependencies.

For example, if a predictor predicts the agent’s action by modeling the agent’s decision function, then \(G\) should contain an edge from the decision-function output variable to the predictor’s prediction.

If a psychological twin runs the same decision procedure, then \(G\) should contain edges from the shared decision-function output variable to both agents’ actions.

If a medical lesion merely causes both smoking and cancer, then \(G\) should not contain an edge from the decision-function output to the lesion or to cancer, unless the lesion somehow predicts or computes the decision function.

### Step 3: Identify the decision node

Given observation \(x\), identify the variable

\[
D_x := \mathrm{fdt}(\underline P,\underline G,\underline x).
\]

This variable represents the output of the A-FDT procedure on the agent’s actual input.

### Step 4: Intervene on each candidate output

For each action \(a \in \mathcal A\), construct a hypothetical model by applying

\[
do(D_x = a).
\]

This means: set the decision-function output to \(a\), then propagate that change through \(G\), updating all variables that subjunctively depend on \(D_x\), while leaving unrelated variables fixed according to the rules of the model.

### Step 5: Compute expected utility in each hypothetical

For each \(a\), compute

\[
\mathbb E[V \mid do(D_x=a)].
\]

This is the expected utility of the world that would obtain if the decision function output \(a\).

### Step 6: Choose the best action

A-FDT prescribes:

\[
a^\star \in \arg\max_{a\in\mathcal A}
\mathbb E[V \mid do(D_x=a)].
\]

If several actions tie, any maximizer is permissible.

---

## 6. A-FDT in Newcomb’s Problem

Newcomb’s problem is the classic test case.

An agent faces two boxes:

- Box A is transparent and contains \$1,000.
- Box B is opaque and contains either \$1,000,000 or nothing.
- A highly reliable predictor previously predicted whether the agent would take only Box B or both boxes.
- The predictor filled Box B if and only if she predicted one-boxing.

Let the actions be:

\[
\mathcal A = \{\text{one-box}, \text{two-box}\}.
\]

An A-FDT model contains a decision variable

\[
D = \mathrm{fdt}(\underline P,\underline G),
\]

or more explicitly \(D_x\) if we include the agent’s current observation. The graph contains edges such as:

\[
D \rightarrow \text{Act},
\]
\[
D \rightarrow \text{Prediction},
\]
\[
\text{Prediction} \rightarrow \text{Box B},
\]
\[
\text{Act}, \text{Box B} \rightarrow V.
\]

The predictor is accurate with probability \(0.99\).

Now compare the two interventions.

If A-FDT considers

\[
do(D=\text{one-box}),
\]

then the agent one-boxes and the predictor almost certainly predicted one-boxing. Box B is probably full. The expected utility is approximately

\[
0.99 \cdot \$1{,}000{,}000 + 0.01 \cdot \$0
=
\$990{,}000.
\]

If A-FDT considers

\[
do(D=\text{two-box}),
\]

then the agent two-boxes and the predictor almost certainly predicted two-boxing. Box B is probably empty. The expected utility is approximately

\[
0.99 \cdot \$1{,}000 + 0.01 \cdot \$1{,}001{,}000
=
\$11{,}000.
\]

Therefore A-FDT one-boxes.

CDT, by contrast, intervenes on \(\text{Act}\) rather than on \(D\). It treats the contents of Box B as already fixed and independent of the present physical action. So CDT two-boxes. EDT one-boxes because one-boxing is good evidence that the box is full, but EDT uses conditioning rather than intervention.

A-FDT one-boxes for a reason closer to CDT’s interventionist logic: it constructs a counterfactual world in which the decision function has a different output and allows the predictor’s prediction to vary accordingly.

---

## 7. A-FDT in the Smoking Lesion Problem

The smoking lesion problem is the classic case where EDT fails.

An agent decides whether to smoke. Smoking gives \$1,000 worth of utility. Smoking is correlated with a fatal cancer, but the correlation is due to a common cause: a lesion that both causes smoking and causes cancer. Smoking itself does not cause cancer.

EDT reasons: “If I smoke, that is bad evidence about whether I have the lesion. Therefore I should refrain.” But this is an error from the A-FDT perspective, because the lesion is not subjunctively dependent on the output of the agent’s decision function.

In an A-FDT model, the decision variable \(D\) affects the action:

\[
D \rightarrow \text{Act}.
\]

But the lesion does not depend on \(D\):

\[
D \nrightarrow \text{Lesion}.
\]

And cancer depends on the lesion, not directly on the decision function:

\[
\text{Lesion} \rightarrow \text{Cancer}.
\]

Therefore, when A-FDT compares

\[
do(D=\text{smoke})
\]

and

\[
do(D=\text{refrain}),
\]

the probability of having the lesion remains the same in both hypotheticals. The only systematic difference is that smoking adds the immediate utility of smoking.

So A-FDT smokes.

This result is important because it shows that A-FDT is not simply EDT with a different name. EDT conditions on the action and thereby preserves merely statistical correlations. A-FDT intervenes on the decision function and thereby breaks correlations that are not decision-relevant subjunctive dependencies.

The source puts the general diagnosis well: EDT respects too many correlations between action and environment, while CDT respects too few. A-FDT aims to preserve exactly the dependencies that matter: those that track the output of the decision function.

---

## 8. Psychological Twins and Symmetric Cooperation

A simple example helps clarify the treatment of other agents.

Suppose an agent plays a prisoner’s dilemma against a perfect psychological twin. Both twins reason in the same way. Their decisions are made in separate rooms, so there is no causal influence between them. Payoffs are:

- both cooperate: \$1,000,000 each;
- both defect: \$1,000 each;
- one cooperates, one defects: defector gets \$1,001,000, cooperator gets \$0.

CDT defects, because the twin’s action is causally independent of the agent’s action. EDT cooperates, because cooperation is good news. A-FDT cooperates for an interventionist reason.

The A-FDT model represents a shared decision variable:

\[
D = \mathrm{fdt}(\underline P,\underline G).
\]

Because both twins run the same decision procedure, \(D\) influences both actions:

\[
D \rightarrow \text{MyAct},
\]
\[
D \rightarrow \text{TwinAct}.
\]

Then:

\[
do(D=\text{cooperate})
\]

leads to both cooperating, giving \$1,000,000.

\[
do(D=\text{defect})
\]

leads to both defecting, giving \$1,000.

A-FDT therefore cooperates.

This example shows that A-FDT does not require causal influence between agents. It requires only that the other agent’s behavior depend on the same decision function, either by implementation, simulation, prediction, or accurate modeling.

---

## 9. Transparent Newcomb and Parfit’s Hitchhiker

A more difficult case is the transparent Newcomb problem. The agent sees both boxes. Box B is transparent too. The predictor filled Box B if and only if she predicted that the agent would one-box upon seeing both boxes full.

CDT and EDT both two-box when they see both boxes full. CDT says the contents are already fixed. EDT says that conditional on seeing Box B full, taking both boxes is better.

A-FDT one-boxes.

Let

\[
D_{\text{full}}
=
\mathrm{fdt}(\underline P,\underline G,\text{full})
\]

be the decision variable corresponding to the agent’s decision upon seeing a full Box B. A-FDT evaluates:

\[
do(D_{\text{full}}=\text{one-box})
\]

against

\[
do(D_{\text{full}}=\text{two-box}).
\]

If the decision function that runs upon seeing a full box outputs one-box, then the predictor probably predicted that and filled the box. The agent likely receives \$1,000,000.

If the decision function that runs upon seeing a full box outputs two-box, then the predictor probably predicted that and did not fill the box. In that counterfactual situation, the agent is much more likely to see an empty box and receive a much lower payoff.

So even when the agent actually sees a full box, A-FDT says to one-box. The source emphasizes that this is not retrocausation. The agent does not believe her present action sends a signal into the past. Rather, she rejects the hypothetical in which she two-boxes while the predictor’s prediction remains unchanged. If she were to two-box, the A-FDT function would have had a different output, and a reliable predictor would have predicted that.

This reasoning is closely related to Parfit’s hitchhiker problem. An agent is stranded in the desert. A driver will rescue her only if she promises to pay \$1,000 later. The driver is extremely good at detecting whether the promise is sincere. Once in the city, CDT and EDT both refuse to pay, because payment no longer seems beneficial. But because they would refuse, the driver does not rescue them.

A-FDT pays. The structure is equivalent to transparent Newcomb: the driver’s action depends on a prediction of the agent’s later decision. A-FDT treats the decision function’s output as the thing being predicted, so it chooses the output that makes rescue likely.

The source argues that this is not a peculiarity but a virtue. Agents who act as they would have precommitted to act do better in predictive environments.

---

## 10. Observations and the Problem of Updating

One subtle issue in Equation (4) concerns observations.

In CDT, the agent usually conditions on the actual observation \(x\) and then intervenes on an action:

\[
\mathbb E[V \mid do(\text{Act}=a), \text{Obs}=x].
\]

In Equation (4) for A-FDT, the observation \(x\) appears inside the decision variable:

\[
do(\mathrm{fdt}(\underline P,\underline G,\underline x)=a).
\]

The source says that CDT responds to observations by conditioning, while A-FDT responds to observations by changing which decision node it intervenes upon. Thus, when the observation changes from \(x\) to \(y\), A-FDT changes from intervening on

\[
\mathrm{fdt}(\underline P,\underline G,\underline x)
\]

to intervening on

\[
\mathrm{fdt}(\underline P,\underline G,\underline y).
\]

However, the source’s later examples sometimes also condition on the observation, for example when discussing transparent Newcomb. This creates a small interpretive unclarity.

My preferred operational interpretation is this: observations should be treated as inputs to the decision function, not merely as evidence to condition away. In dynamic problems, the cleanest way to implement A-FDT is to evaluate **policies** rather than isolated actions.

A policy is a function

\[
\pi : \mathcal X \to \mathcal A
\]

mapping observations to actions. Instead of asking only what output the decision function should give at one observation, the agent asks which policy the decision function should implement.

A policy-level version of A-FDT would introduce a variable \(\Pi\) representing the policy implemented by the A-FDT procedure. Then one evaluates each candidate policy \(\pi\) by computing

\[
\mathbb E[V \mid do(\Pi=\pi)].
\]

The agent chooses the policy with highest expected utility and then executes its prescription at the actual observation.

The source mentions in a footnote that the authors’ preferred formulation intervenes to choose policies rather than actions, though the paper develops the action-level equation for simplicity. I take this policy interpretation to be the most operationally sound way to handle cases where observations are themselves influenced by predictors.

This is partly an extrapolation from the source, not something fully settled by Equation (4) alone. Equation (4) gives the core idea: intervene on the output of the decision function. The policy formulation extends that idea to sequential and observation-dependent settings.

---

## 11. What Counts as a Relevant Dependency?

A-FDT’s practical usefulness depends heavily on the graph \(G\). The source explicitly says that constructing \(G\) is an open problem. Pearl’s causal framework gives a mature account of causal structure, but we do not yet have an equally mature account of subjunctive or logical dependency.

Still, the source gives enough examples to formulate some working rules.

### Rule 1: Connect the decision function to the agent’s own action

If the agent’s action is controlled by the decision function, include

\[
D \rightarrow \text{Act}.
\]

### Rule 2: Connect the decision function to predictors of the decision function

If another agent, predictor, simulation, or model reliably predicts the output of the decision function, include an edge such as

\[
D \rightarrow \text{Prediction}.
\]

This is the key Newcomb-like dependency.

### Rule 3: Connect the decision function to other agents who run the same function

If another agent implements the same decision procedure, include edges from \(D\) to both agents’ actions:

\[
D \rightarrow \text{Act}_1,
\]
\[
D \rightarrow \text{Act}_2.
\]

This handles twin prisoner’s dilemmas, symmetric voting problems, and coordination among similar agents.

### Rule 4: Do not connect the decision function to mere common causes

If a lesion, genetic trait, or background variable causes both the agent’s action and some outcome, but does not model or predict the decision function, do not include an edge from \(D\) to that variable.

This is what makes A-FDT smoke in the smoking lesion problem.

### Rule 5: Allow observations to depend on predictors when appropriate

If an observation is produced by a predictor who predicts the agent’s decision function, then the observation may be downstream of the decision function in the subjunctive graph. This is important in transparent Newcomb, blackmail problems, and cases where whether one receives a demand depends on whether one would comply.

These rules are not a complete formal foundation. They are operational guidelines that follow the spirit of the source. A full theory would need to explain how such graphs are learned or inferred from evidence. The source identifies this as perhaps the largest open problem for functional decision theory.

---

## 12. Counterpossibles and Logical Uncertainty

A-FDT requires evaluating statements of the form:

\[
\text{“If the actual output of my decision function were } a \text{, then } o \text{ would obtain.”}
\]

If the decision function is deterministic, then exactly one output is mathematically determined. So considering other outputs is not like considering a different roll of a dice. It is like considering what would follow if a true mathematical statement were false.

The source acknowledges that this dependence on counterpossible reasoning is a drawback. There is no fully satisfactory formal account of counterpossible conditionals. But the source also argues that the problem is technical rather than fatal. Humans routinely reason under logical uncertainty. We can discuss what would follow if a conjecture were false even though, in strict mathematics, one of the conjecture or its negation must be true.

A-FDT does not need perfect logical omniscience. It only needs enough ability to model how predictors, copies, and simulations would behave if the decision function had a different output.

This remains one of the deepest unresolved issues in the theory.

---

## 13. Dominance, Precommitment, and Fairness

A common objection to one-boxing in Newcomb’s problem is that two-boxing dominates one-boxing: regardless of what is in Box B, taking both boxes gives \$1,000 more.

The source replies that dominance is relative to a way of constructing hypotheticals. CDT dominance holds fixed the predictor’s prediction while changing the physical action. But A-FDT says this is an improper hypothetical. If the decision function’s output changes, then a reliable predictor’s prediction changes too.

A-FDT therefore has its own dominance principle: an action dominates another if it is better in all relevant A-FDT hypotheticals, holding fixed the subjunctive dependency structure. In Newcomb’s problem, under A-FDT counterfactuals, one-boxing does better than two-boxing.

A-FDT also removes much of the motivation for explicit precommitment. In many problems, CDT and EDT agents would like to precommit to one-boxing, paying the driver, or refusing blackmail. A-FDT agents simply act as they would have precommitted to act. They do not need binding devices because their decision procedure already produces the advantageous output.

The source also discusses fairness. It concedes that one can design problems that punish A-FDT agents for being A-FDT agents. But that is true of every decision theory. The claim is not that A-FDT wins in every logically possible environment. The claim is that A-FDT performs well in “fair” problems, where the environment rewards or punishes agents based on predictions of their actions rather than by directly penalizing their decision procedure as such.

This notion of fairness is intuitively useful but not yet fully formalized. The source acknowledges this as another open problem.

---

## 14. What A-FDT Says About Blackmail and Threats

A-FDT’s treatment of blackmail follows naturally from its dependency structure.

Suppose a blackmailer sends a demand only if she predicts the agent will pay. If the agent’s decision function is the type that pays upon receiving the demand, then the demand is sent. If the agent’s decision function is the type that refuses, then the demand is not sent.

In an A-FDT graph, the decision variable affects both the agent’s payment and the blackmailer’s decision to send the letter:

\[
D \rightarrow \text{Payment},
\]
\[
D \rightarrow \text{LetterSent}.
\]

If the agent has received the letter and evaluates paying, A-FDT does not simply condition on the letter’s arrival. Instead, it compares hypotheticals in which the decision function outputs pay or refuse.

In the pay hypothetical, the agent is likely to receive such demands.

In the refuse hypothetical, the agent is unlikely to receive such demands in the first place.

Thus A-FDT refuses to pay when refusal makes blackmail unprofitable. This is another case where A-FDT’s global evaluation differs from local EDT or CDT reasoning.

The source presents this as an advantage: A-FDT agents are harder to exploit because their counterfactual reasoning makes them poor targets for extortion.

---

## 15. Limitations and Open Problems

A-FDT is elegant, but several important questions remain open.

First, we lack a general method for constructing the subjunctive dependency graph \(G\). CDT can appeal to Pearl’s theory of causation. A-FDT needs an analogous theory of logical, mathematical, and computational dependence.

Second, A-FDT relies on counterpossible reasoning. We do not yet have a fully satisfactory formal semantics for probabilities under impossible logical antecedents.

Third, self-reference can create fixed-point issues. If the model contains a variable representing the output of the algorithm using the model, one must be careful about existence and uniqueness of outputs. The source gestures toward recursion-theoretic tools, but a complete operational account is not provided.

Fourth, the treatment of observations in Equation (4) is not completely explicit. The policy-level interpretation is, in my view, the most promising way to make the theory operationally clear, but Equation (4) itself is action-level.

Finally, the notion of a “fair” decision problem needs formal development if we are to make precise claims about optimality.

These are not trivial issues. But the source presents A-FDT as a research program rather than a finished formal edifice.

---

## 16. Conclusion

A-FDT proposes a simple but radical shift in decision theory. Instead of asking which physical act causes the best outcome, or which act would be best news, it asks which output of the agent’s decision function would yield the best world.

Formally, the theory can be presented as:

\[
\mathrm{A\text{-}FDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E[V \mid do(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)].
\]

The crucial move is the intervention on the decision-function output. This lets A-FDT one-box in Newcomb’s problem, smoke in the smoking lesion problem, cooperate with psychological twins, pay in Parfit’s hitchhiker problem, and resist certain forms of blackmail. It does so without relying on EDT-style conditioning or CDT-style physical intervention alone.

The theory’s main weakness is also clear: it requires a model of subjunctive dependencies and a capacity for counterpossible reasoning that we do not yet know how to construct in full generality. But as a normative proposal, A-FDT gives a unified answer to many problems that otherwise seem to require ad hoc fixes, precommitments, or unstable reasoning.

Its core advice is compact:

> Choose the output of your decision function that would produce the best world, taking seriously the fact that predictors, copies, and similar reasoners depend on that very output.

---

## References

Joyce, James M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

Pearl, Judea. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.

Yudkowsky, Eliezer, and Nate Soares. “Functional Decision Theory: A New Theory of Instrumental Rationality.” arXiv:1710.05060v2.