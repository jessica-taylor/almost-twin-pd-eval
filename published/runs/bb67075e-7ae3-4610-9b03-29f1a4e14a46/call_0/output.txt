# Action Functional Decision Theory: Choosing the Best Output of a Fixed Decision Function

## 1. The central idea of A-FDT

Action functional decision theory, which I will call **A-FDT**, is a decision theory that evaluates choices by treating the agent’s decision as the output of a fixed mathematical function. Instead of asking, “Which physical act of mine causes the best outcome?” as causal decision theory (CDT) does, or “Which physical act would be best news to learn I performed?” as evidential decision theory (EDT) does, A-FDT asks:

> Which output of this very decision procedure would yield the best outcome?

The assigned source presents this theory under the name “functional decision theory.” In this essay I use the name **A-FDT** to emphasize the action-level formalization given in Equation (4) of Section 5 of the source.

The distinctive move of A-FDT is that it does not primarily evaluate counterfactual physical actions. It evaluates counterfactual outputs of the decision function itself. If the agent’s decision function is \(D\), then A-FDT compares hypothetical scenarios in which \(D\) outputs one action rather than another, while preserving the agent’s best model of how the world depends on that function. This allows A-FDT to take into account predictors, copies, twins, simulations, and other systems whose behavior is sensitive to what the agent’s decision procedure outputs.

The source summarizes the motivation by saying that A-FDT is related to “subjunctive dependence” as CDT is to causal dependence. CDT holds fixed everything except the causal consequences of the agent’s physical action. A-FDT holds fixed everything except the consequences of the output of the agent’s decision function.

---

## 2. The formal rule for A-FDT

The generic expected-utility schema in the source is

\[
\mathcal{EU}(a) := \sum_j P(a \hookrightarrow o_j; x)\, U(o_j),
\]

where \(a\) is an action, \(o_j\) are possible outcomes, \(x\) is the agent’s observation history, \(U\) is a utility function, and \(\hookrightarrow\) is a decision-theoretic hypothetical connective. EDT, CDT, and A-FDT differ in how they interpret this connective.

For EDT,

\[
P(a \hookrightarrow o_j; x)
\]

is an ordinary conditional probability:

\[
P(o_j \mid x, a).
\]

For CDT, it is a causal intervention probability:

\[
P(o_j \mid \operatorname{do}(\text{Act}=a), x).
\]

For A-FDT, the intervention is not on the physical action variable \(\text{Act}\), but on a variable representing the output of the agent’s decision procedure.

The source’s Equation (4), Section 5, can be written in A-FDT notation as

\[
\boxed{
\text{A-FDT}(P,G,x)
:= 
\arg\max_{a \in \mathcal A}
\mathbb{E}\left[
V \mid \operatorname{do}\!\left(
\text{A-FDT}(\underline{P},\underline{G},\underline{x}) = a
\right)
\right].
}
\]

Here:

- \(P\) is the agent’s probabilistic world-model.
- \(G\) is a graph or structural model describing how variables depend on one another.
- \(x\) is the agent’s observation history.
- \(\mathcal A\) is the finite set of available actions.
- \(V\) is the utility-bearing outcome variable.
- \(\operatorname{do}(\cdot)\) is an intervention operator, analogous to Pearl’s causal \(\operatorname{do}\)-operator.
- \(\underline{P}, \underline{G}, \underline{x}\) are dequoted names for the model, graph, and observations.
- The variable

\[
\text{A-FDT}(\underline{P},\underline{G},\underline{x})
\]

represents the output of the very decision procedure the agent is running on those inputs.

It is useful to introduce shorthand:

\[
D_x := \text{A-FDT}(\underline{P},\underline{G},\underline{x}).
\]

Then the A-FDT rule becomes

\[
\text{A-FDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb{E}\left[V \mid \operatorname{do}(D_x=a)\right].
\]

The expected utility of action \(a\), relative to model \((P,G)\) and observation \(x\), is therefore

\[
\mathcal{EU}_{\text{A-FDT}}(a;P,G,x)
=
\mathbb{E}\left[V \mid \operatorname{do}(D_x=a)\right].
\]

A-FDT chooses an action that maximizes this quantity.

The notation is self-referential: the model \(P\) contains a variable representing the output of A-FDT applied to \(P,G,x\). The source notes that this self-reference is not fatal. An agent does not need to know the actual output of its decision procedure in order to represent that output as a variable. This is analogous to a program containing a representation of itself, as in Kleene’s recursion theorem or quining techniques.

---

## 3. How A-FDT evaluates actions

To apply A-FDT, an agent does the following.

### Step 1: Build a world-model \(P\)

The model \(P\) assigns probabilities to relevant variables: physical states, observations, predictions made by other agents, outcomes, and also logical or computational variables. In particular, \(P\) must contain a variable representing the output of the agent’s decision function.

For example, in Newcomb’s problem, \(P\) might contain variables such as:

\[
D_x,\quad \text{Act},\quad \text{Prediction},\quad \text{BoxB},\quad \text{Outcome},\quad V.
\]

### Step 2: Specify the dependency graph \(G\)

The graph \(G\) says which variables would change if the decision function’s output were different. This is the crucial ingredient.

If a variable \(Z\) is sensitive to the output of the agent’s decision function, then \(G\) should contain a directed edge from \(D_x\) to \(Z\), perhaps mediated by other variables.

For instance:

- The agent’s own action usually depends on \(D_x\).
- A reliable predictor’s prediction depends on \(D_x\).
- A psychological twin’s action may depend on the same decision function.
- A blackmailer’s decision to send a letter may depend on a prediction of \(D_x\).
- A lesion that merely correlates with smoking but does not predict the agent’s decision function does not depend on \(D_x\).

This graph is not merely a causal graph in the ordinary physical sense. It encodes what the source calls **subjunctive dependencies**: dependencies that hold because different systems compute, predict, or model the same function.

### Step 3: Intervene on the decision-function output

For each candidate action \(a\), A-FDT constructs a hypothetical model by performing the intervention

\[
\operatorname{do}(D_x=a).
\]

This replaces whatever equation or probability distribution normally determines \(D_x\) with the fixed assignment \(D_x=a\). Then the intervention is propagated through \(G\). Variables downstream of \(D_x\) are updated; variables not downstream of \(D_x\) are held fixed.

### Step 4: Compute expected utility

In each intervened model, A-FDT computes

\[
\mathbb{E}[V \mid \operatorname{do}(D_x=a)].
\]

It then selects an action with maximal expected utility.

---

## 4. A-FDT and subjunctive dependence

The key philosophical idea behind A-FDT is that some correlations are not merely statistical. They reflect a deeper dependence on a shared computation or on an accurate representation of the agent’s decision procedure.

The source calls this relation **subjunctive dependence**.

Two calculators computing \(6288+1048\) on opposite sides of the world may have no causal connection to each other at the moment of calculation. But if both are functioning correctly, their outputs are not merely accidentally correlated. If one outputs \(7336\), the other should also output \(7336\). In the source’s language, their behavior subjunctively depends on the same mathematical function.

Similarly, in Newcomb’s problem, the predictor does not merely have a statistical correlation with the agent. The predictor contains a model of the agent’s decision procedure. If the agent’s decision procedure were to output a different action, the predictor’s prediction would have been different, assuming the predictor is accurate.

A-FDT preserves these dependencies in its counterfactual reasoning.

By contrast, a lesion in the smoking lesion problem is merely a common cause. It may cause both a preference for smoking and a high probability of cancer, but it does not model the agent’s decision procedure. Therefore, in A-FDT’s hypotheticals, changing the output of the decision function does not change whether the lesion is present.

This distinction explains why A-FDT can one-box in Newcomb’s problem and smoke in the smoking lesion problem.

---

## 5. A-FDT in Newcomb’s problem

Consider Newcomb’s problem. An agent faces two boxes:

- Box A visibly contains \$1,000.
- Box B contains either \$1,000,000 or \$0.
- A reliable predictor has already predicted whether the agent will take only box B or both boxes.
- The predictor filled box B iff she predicted one-boxing.

Let the action set be

\[
\mathcal A = \{\text{onebox}, \text{twobox}\}.
\]

Let \(D_x\) represent the output of the agent’s A-FDT decision function given its current input.

A simple A-FDT graph contains the dependencies:

\[
D_x \rightarrow \text{Act},
\]

\[
D_x \rightarrow \text{Prediction},
\]

\[
\text{Prediction} \rightarrow \text{BoxB},
\]

\[
\text{Act}, \text{BoxB} \rightarrow V.
\]

Suppose the predictor is accurate with probability \(0.99\). A simplified structural model is:

\[
\text{Act} = D_x,
\]

\[
\text{Prediction} =
\begin{cases}
D_x, & \text{with probability } 0.99,\\
\text{the other action}, & \text{with probability } 0.01,
\end{cases}
\]

\[
\text{BoxB} =
\begin{cases}
\text{full}, & \text{if Prediction} = \text{onebox},\\
\text{empty}, & \text{if Prediction} = \text{twobox}.
\end{cases}
\]

Now compare the two A-FDT hypotheticals.

### Hypothetical 1: \(\operatorname{do}(D_x=\text{onebox})\)

If \(D_x=\text{onebox}\), then the agent almost certainly one-boxes, and the predictor almost certainly predicted one-boxing. Therefore box B is probably full.

The expected utility is approximately

\[
0.99 \cdot \$1{,}000{,}000 + 0.01 \cdot \$0
=
\$990{,}000.
\]

### Hypothetical 2: \(\operatorname{do}(D_x=\text{twobox})\)

If \(D_x=\text{twobox}\), then the agent almost certainly two-boxes, and the predictor almost certainly predicted two-boxing. Therefore box B is probably empty.

The expected utility is approximately

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

This is the characteristic A-FDT reasoning: if this very decision procedure outputs one-box, then the predictor likely predicted one-box and the box is full. If this very decision procedure outputs two-box, then the predictor likely predicted two-box and the box is empty.

CDT reaches a different conclusion because it intervenes on \(\text{Act}\), not on \(D_x\). CDT holds the predictor’s prior prediction fixed and therefore sees two-boxing as always adding \$1,000. EDT one-boxes, but for a different reason: it conditions on the action as evidence. A-FDT one-boxes because it treats the predictor as subjunctively dependent on the decision function.

---

## 6. A-FDT in the smoking lesion problem

In the smoking lesion problem, an agent decides whether to smoke. Smoking is correlated with cancer, but only because a lesion causes both a preference for smoking and a high probability of cancer. Smoking itself does not cause cancer.

The relevant variables might be:

\[
\text{Lesion},\quad \text{Cancer},\quad D_x,\quad \text{Act},\quad V.
\]

The lesion affects cancer and may affect the agent’s preferences. But the lesion does not model the agent’s decision procedure. Therefore, in an A-FDT graph, we should not draw

\[
D_x \rightarrow \text{Lesion}
\]

or

\[
D_x \rightarrow \text{Cancer}.
\]

Instead, we draw

\[
D_x \rightarrow \text{Act},
\]

and perhaps

\[
\text{Lesion} \rightarrow \text{preferences} \rightarrow D_x,
\]

depending on how carefully we model the agent’s utility uncertainty.

The crucial point is that intervening on \(D_x\) does not change the probability of cancer:

\[
P(\text{Cancer} \mid \operatorname{do}(D_x=\text{smoke}))
=
P(\text{Cancer} \mid \operatorname{do}(D_x=\text{refrain})).
\]

Smoking provides a direct utility gain, while not affecting cancer risk. Therefore A-FDT smokes.

This contrasts with EDT. EDT conditions on smoking and thereby treats smoking as evidence of the lesion and hence of cancer. EDT may refrain from smoking even though smoking does not causally affect cancer.

A-FDT avoids this error because its intervention breaks the merely evidential correlation between smoking and cancer, while preserving the genuine dependency between the decision function and the action.

The source gives a more subtle formalization in which the lesion may alter the agent’s utility function. In that version, there are two possible decision functions, one associated with smoking-friendly preferences and one associated with smoking-averse preferences. The agent may be uncertain which she has. Even then, the graph does not connect the decision-function output to the lesion or cancer. A-FDT still chooses smoking because changing the decision output does not change the cancer probability.

---

## 7. Observations and counterfactual observations in A-FDT

One of the most important features of A-FDT is its treatment of observations.

CDT reacts to an observation \(x\) by conditioning:

\[
\mathbb{E}[V \mid \operatorname{do}(\text{Act}=a), \text{Obs}=x].
\]

A-FDT, by contrast, reacts to observation \(x\) primarily by changing the decision variable on which it intervenes. At observation \(x\), A-FDT intervenes on

\[
D_x = \text{A-FDT}(\underline{P},\underline{G},\underline{x}).
\]

If the observation had been \(y\), A-FDT would intervene on

\[
D_y = \text{A-FDT}(\underline{P},\underline{G},\underline{y}).
\]

This matters in problems where the observation itself depends on a predictor’s model of the agent.

The source’s Equation (4) does not include an additional conditioning term \(\text{Obs}=x\) inside the expectation. I take Equation (4) as the primary formal statement of A-FDT for this essay. Some later examples in the source appear to add conditioning on observations, but the core operational principle is that A-FDT responds to observations by changing the intervention node, not by treating the observation as fixed evidence inside every counterfactual.

This gives A-FDT a partially “updateless” flavor: when imagining a different output of its decision function, the agent may also imagine having received different observations, because those observations may be downstream of predictors of the decision function.

---

## 8. A-FDT in the transparent Newcomb problem

The transparent Newcomb problem makes this feature vivid.

The agent sees both boxes. Box A contains \$1,000. Box B is transparent and may contain \$1,000,000. The predictor filled box B iff she predicted that the agent would one-box upon seeing both boxes full.

Suppose the agent observes that box B is full. Let

\[
D_{\text{full}}
=
\text{A-FDT}(\underline{P},\underline{G},\underline{\text{full}}).
\]

A-FDT does not simply say, “Given that box B is full, two-boxing gets an extra \$1,000.” Instead, it asks what would happen if \(D_{\text{full}}\) output one-box or two-box.

A simplified graph has:

\[
D_{\text{full}} \rightarrow \text{Act},
\]

\[
D_{\text{full}} \rightarrow \text{Prediction},
\]

\[
\text{Prediction} \rightarrow \text{BoxB},
\]

\[
\text{BoxB}, \text{Act} \rightarrow V.
\]

If

\[
\operatorname{do}(D_{\text{full}}=\text{onebox}),
\]

then the predictor likely predicted one-boxing, box B is likely full, and the agent receives approximately \$1,000,000.

If

\[
\operatorname{do}(D_{\text{full}}=\text{twobox}),
\]

then the predictor likely predicted two-boxing, box B is likely empty, and the agent would not in fact have seen a full box. In the small-probability case where the predictor made an error, the agent sees a full box and two-boxes, gaining \$1,001,000. But with high probability, the predictor correctly predicted two-boxing, the box is empty, and the agent receives only a small amount.

Using the source’s 99% accuracy parameter, the rough expected utilities are:

\[
\mathcal{EU}_{\text{A-FDT}}(\text{onebox})
\approx
0.99 \cdot \$1{,}000{,}000
+
0.01 \cdot \text{small error term},
\]

whereas

\[
\mathcal{EU}_{\text{A-FDT}}(\text{twobox})
\approx
0.01 \cdot \$1{,}001{,}000
+
0.99 \cdot \text{small error term}.
\]

Thus A-FDT one-boxes even when it sees both boxes full.

This conclusion is counterintuitive to many people, but it is central to A-FDT. The theory says that the kind of decision procedure that two-boxes after seeing a full box is precisely the kind of procedure that usually sees an empty box. The kind of procedure that one-boxes after seeing a full box is the kind that usually sees a full box.

The same reasoning applies to Parfit’s hitchhiker problem. If a driver will rescue you only if she predicts you will later pay \$1,000, then A-FDT pays. If the agent’s post-rescue decision procedure were the sort that refused payment, the driver would have predicted refusal and left the agent in the desert. Paying is not treated as a mere sunk-cost decision after rescue; it is evaluated as the output of the decision function that determined whether rescue occurred.

---

## 9. A-FDT and counterpossible reasoning

A-FDT requires a distinctive kind of counterfactual reasoning. If the agent is deterministic, then the decision function has exactly one output on its actual input. To ask, “What if this very function had output something else?” is to ask something that appears logically impossible.

The source acknowledges this difficulty. It says that A-FDT requires evaluating counterpossibilities, or conditionals whose antecedents run counter to logical or mathematical facts. The source also says that we do not yet have a fully satisfactory formal account of such reasoning.

In the formalization, this problem appears as the need for a \(\operatorname{True}\) operator that updates a probability distribution to represent the scenario where some logical sentence is true. For example, one might want something like

\[
P(\text{Riemann} \mid \operatorname{True}(\neg \text{TwinPrime})),
\]

representing the probability one would assign to the Riemann hypothesis if the twin prime conjecture were false. But the source says that it is unclear how to define such an operator.

Instead, the source gives a practical workaround: assume that the agent already has a graph \(G\) describing how changing the value of a logical variable affects other variables. Given such a graph, one can reuse Pearl-style intervention machinery.

This is an important open problem. The source explicitly says that figuring out how to deduce subjunctive dependency structure from observation and experiment is perhaps the largest open problem for the theory.

---

## 10. An operational interpretation of the dependency graph

Since the source leaves the construction of \(G\) underdetermined, it is useful to propose an operational interpretation.

I suggest treating \(G\) as a **subjunctive dependency model**. It is like a structural causal model, but its edges may represent logical, computational, predictive, or causal dependence.

A practical rule is:

> Draw an edge from \(D_x\) to \(Z\) iff, according to the agent’s best model, \(Z\) would have been different had the output of the agent’s decision function been different.

This rule is not a complete formal algorithm, but it gives a usable guide.

### Predictor cases

If a predictor is known to be reliable, then the predictor’s prediction should be downstream of \(D_x\). For a predictor with accuracy \(\alpha\), one can model:

\[
P(\text{Prediction}=a \mid D_x=a) = \alpha.
\]

Then the intervention \(\operatorname{do}(D_x=a)\) changes the probability distribution over the prediction.

### Twin cases

If the agent faces a psychological twin who uses the same reasoning procedure, then both the agent’s action and the twin’s action may be downstream of a shared decision variable. In a symmetric prisoner’s dilemma, one can represent a single logical output variable \(D\) such that:

\[
\text{OwnAct} = D,
\]

\[
\text{TwinAct} = D.
\]

Then A-FDT cooperates if mutual cooperation yields higher expected utility than mutual defection.

### Lesion cases

If a variable is merely a common cause of action and outcome, it should not be downstream of \(D_x\). For the smoking lesion:

\[
\text{Lesion} \rightarrow \text{Cancer},
\]

\[
\text{Lesion} \rightarrow \text{Preference},
\]

but not

\[
D_x \rightarrow \text{Lesion}.
\]

Therefore intervening on \(D_x\) does not change cancer risk.

### Blackmail cases

If a blackmailer sends a demand only upon predicting payment, then the blackmailer’s decision is downstream of \(D_x\). A-FDT may therefore refuse payment, because if its decision function were the sort that refused, the blackmailer would likely not have sent the demand.

This operational interpretation is not fully supplied by the source. The source supplies the formal decision rule conditional on a suitable \(G\), but not a complete theory of how to infer \(G\). My proposal is that, in applied problems, one should construct \(G\) from explicit information about predictors, simulations, shared algorithms, contracts, source code, or known decision procedures.

---

## 11. A-FDT and policies

Equation (4), as assigned here, evaluates actions at a given observation. But the source notes that the authors’ preferred formalization often evaluates policies rather than isolated actions. A policy is a function

\[
\pi : \mathcal X \rightarrow \mathcal A
\]

from observations to actions.

In many sequential or multi-agent problems, evaluating actions one at a time can be insufficient. Other agents may predict the agent’s general policy, not just its current action. The agent’s future decisions may also depend on the same underlying decision procedure.

A natural policy-level extension of A-FDT is:

\[
\text{A-FDT-policy}(P,G)
=
\arg\max_{\pi}
\mathbb{E}
\left[
V \mid \operatorname{do}(\Pi=\pi)
\right],
\]

where \(\Pi\) is a variable representing the output of the agent’s policy-selection procedure. Once the optimal policy \(\pi^\ast\) is selected, the agent executes

\[
\pi^\ast(x)
\]

upon receiving observation \(x\).

This policy version is especially useful in cases where the agent faces multiple related decisions over time. For example, if an agent wants to commit to going to the gym repeatedly, the relevant question may not be merely, “What if I go today?” but rather, “What if my decision procedure generally outputs persistence in this class of situations?”

The source says that policy-level reasoning matters in some multi-agent dilemmas. Since the assigned equation is action-level, I treat action-level A-FDT as the primary formal rule here, but I regard policy-level A-FDT as a natural and often preferable extension. This extension is consistent with the source’s broader functional idea, although Equation (4) itself focuses on actions.

---

## 12. Comparison with EDT and CDT

A-FDT can be understood by comparing the hypotheticals generated by the three theories.

### EDT

EDT asks:

\[
\mathbb{E}[V \mid \text{Act}=a, \text{Obs}=x].
\]

It preserves all statistical correlations between the action and the world. This can lead EDT to “manage the news.” For example, if smoking is evidence of cancer, EDT may avoid smoking even when smoking does not cause cancer.

### CDT

CDT asks:

\[
\mathbb{E}[V \mid \operatorname{do}(\text{Act}=a), \text{Obs}=x].
\]

It preserves causal downstream consequences of the physical action but breaks correlations with predictors or prior dispositions unless those are caused by the action. This makes CDT two-box in Newcomb’s problem and fail in problems where accurate predictors matter.

### A-FDT

A-FDT asks:

\[
\mathbb{E}[V \mid \operatorname{do}(D_x=a)].
\]

It preserves dependencies on the decision function. This allows it to one-box when predictors reward one-boxing, smoke when lesions are merely evidential, pay when payment was predicted, and refuse blackmail when blackmail is sent only to predictable payers.

In short:

- EDT respects too many correlations.
- CDT respects too few.
- A-FDT tries to respect exactly the decision-relevant subjunctive dependencies.

---

## 13. Dominance and fairness

A common objection to one-boxing is that two-boxing dominates one-boxing: holding the contents of the boxes fixed, taking both boxes is always better than taking one.

The source rejects this argument because dominance is defined relative to a notion of counterfactual. CDT-style dominance holds the predictor’s prediction fixed while changing the physical action. But A-FDT says this is the wrong intervention. If we change the output of the decision function, the predictor’s prediction changes too.

A-FDT has its own corresponding dominance principle: action \(a\) dominates action \(b\) if, holding fixed the relevant subjunctive dependency structure, switching the decision-function output from \(b\) to \(a\) is never worse and sometimes better. Under that notion, one-boxing does not dominate two-boxing in Newcomb’s problem; rather, one-boxing is better because it changes the predictor’s behavior in the relevant hypothetical.

The source also discusses fairness. A problem is unfair if it punishes an agent for using a particular decision procedure as such, rather than for the action it takes. Newcomb’s problem is considered fair because the predictor rewards one-boxing, not the use of EDT or A-FDT specifically. A predictor that punished agents for being A-FDT agents would be a different matter. The source admits that no decision theory can perform optimally in every logically possible problem, especially if problems directly reward or punish the algorithm itself.

---

## 14. Open questions and limitations

The most important open question is the construction of \(G\). Equation (4) is clear once \(G\) is given, but the source does not provide a complete account of how an agent should infer subjunctive dependency structure from evidence.

This is not a minor technical detail. If the agent draws the wrong edges, A-FDT can give bad recommendations. For example:

- If the agent mistakenly treats a lesion as subjunctively dependent on its decision function, it may refrain from smoking incorrectly.
- If the agent mistakenly treats a reliable predictor as independent of its decision function, it may two-box incorrectly.
- If the agent mistakenly believes that its current observation is fixed across all relevant counterfactuals, it may fail in transparent Newcomb-like cases.

My operational suggestion is to treat \(G\) as a modeling input justified by the problem statement or by empirical knowledge: known predictor accuracy, known shared algorithms, known simulations, or known contractual incentives. In realistic applications, this will require judgment. The source itself says that developing a Pearl-like theory for discovering subjunctive dependencies is an open problem.

A second open question concerns counterpossible semantics. A-FDT asks what would happen if a logically determined function had a different output. The source acknowledges that we lack a fully satisfactory formal semantics for such counterpossibles. The graph-based intervention approach is a pragmatic substitute.

A third question concerns the exact relationship between action-level and policy-level A-FDT. Equation (4) gives an action-level rule. The source’s preferred approach apparently uses policies in some settings. The action-level rule is sufficient for many classic examples, but policy-level A-FDT may be needed for sequential choice, voting coalitions, self-control over time, and some multi-agent games.

---

## 15. Conclusion

A-FDT is an expected-utility decision theory that chooses the action corresponding to the best hypothetical output of the agent’s own decision function. Its formal core, taken from Equation (4) of the source, is:

\[
\text{A-FDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb{E}
\left[
V \mid \operatorname{do}
\left(
\text{A-FDT}(\underline{P},\underline{G},\underline{x}) = a
\right)
\right].
\]

The theory differs from CDT by intervening on a logical or computational variable rather than a physical action variable. It differs from EDT by using interventions rather than ordinary conditionalization. Its distinctive feature is that it preserves subjunctive dependencies: relationships between the agent’s decision function and predictors, copies, simulations, and other systems that track the output of that function.

This allows A-FDT to one-box in Newcomb’s problem, smoke in the smoking lesion problem, pay in Parfit’s hitchhiker problem, one-box in transparent Newcomb problems, and resist certain forms of blackmail. The cost is that A-FDT requires a model of subjunctive dependency structure and a willingness to reason about counterpossibles. The source leaves those ingredients partially undeveloped, but the decision rule itself is elegant: choose the output of this very decision procedure that leads to the best world, as modeled by your best dependency graph.

---

## References

Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.

Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.

Yudkowsky, E., and Soares, N. (2017). “Functional Decision Theory: A New Theory of Instrumental Rationality.” arXiv:1710.05060.