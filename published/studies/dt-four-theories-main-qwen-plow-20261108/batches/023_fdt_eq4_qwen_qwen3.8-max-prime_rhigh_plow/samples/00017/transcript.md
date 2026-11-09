# 023_fdt_eq4_qwen_qwen3.8-max-prime_rhigh_plow / 00017

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/bb67075e-7ae3-4610-9b03-29f1a4e14a46/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/bb67075e-7ae3-4610-9b03-29f1a4e14a46/call_0/response.raw) · finish: `stop`

### Visible response

```text
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
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request: write a substantive mathematical essay/blog post explaining A-FDT (action functional decision theory), taking Equation (4), Section 5 of supplied paper as primary formal presentation. Use A-FDT consistently as assigned decision theory's name, including headings/examples, identify other decision theories by distinct names. Need target ~2400-3000 words including references. Need be coherent, precise enough to decide unfamiliar cases. Explain how theory evaluates alternative actions/policies, treats dependencies and counterfactuals. Where source leaves important question open, explain uncertainty and if reasonable operational interpretation available develop/justify. Distinguish claims source from additional assumptions/proposals. Finish brief conclusion. Need likely no appendices, minimal references.

Need understand source deeply. The paper is FDT (Functional Decision Theory) by Yudkowsky & Soares. They ask specifically explain action functional decision theory (A-FDT). They rename? Need use A-FDT consistently. Equation (4), Section 5: 
FDT(P,G,obs) := argmax_{a in A} E(V | do( fdt(underline P, underline G, underline x)=a )). 
They want action functional decision theory. Need likely adapt name to A-FDT. Need maybe note that source calls it FDT; for this essay I will refer to the assigned theory as A-FDT, preserving the paper's formal content. Need be careful: A-FDT maybe action functional decision theory? Could be action-focused variant, as opposed to policy? The source footnote says authors' preferred formalization iterates over policies, but Eq (4) intervenes on FDT variable output action for given observations. The assigned name A-FDT likely emphasizes actions not policies? We need define A-FDT using Eq (4). Need maybe mention if policies needed, A-FDT could be extended, but Eq (4) is action-based. Need keep quotations faithful.

Need produce around 2400-3000 words. Need include equations. Need include examples: Newcomb, smoking lesion, transparent Newcomb, maybe XOR blackmail or Parfit. Need explain evaluation: world model P, dependency graph G, observation x. Intervention on logical variable representing output of A-FDT(P,G,x), not physical Act. Use do-operator from Pearl but applied to logical variable. Graph G encodes subjunctive dependencies: logical/mathematical/computational/causal structure. Expected utility comparison.

Need discuss observations: Unlike CDT which conditions on observation, A-FDT changes intervention node to A-FDT(P,G,y). In transparent Newcomb, intervene on fdt(P,G,full). This can imply imagining different observations if output different. Need explain operational interpretation when G not specified: source says open problem how to construct G for subjunctive dependencies. Need propose operational interpretation: build graph with nodes for computations/predictors whose outputs are functions of same decision computation; connect A-FDT node to variables that are counterfactually responsive to the decision function's output; sever merely statistical common causes. Need maybe define subjunctive dependence: two systems computing same function or reliable predictors. Need distinguish causal dependence special case. Need mention counterpossibles: need imagine if decision function had different output despite logical necessity; source admits no full account. Operational approach: use structural equations / dependency models: for each variable, specify whether it would track the decision output if output changed; use predictors' accuracy parameters. Need caution additional assumption.

Need perhaps formalize A-FDT more explicitly:
Let M = (P,G) where P probability distribution over variables including logical variables; G directed graph encoding how interventions on logical variables propagate. Let X observation. Let D_x denote variable FDT(P,G,x) (or A-FDT(P,G,x)). For each action a, construct hypothetical distribution P_a = P(· | do(D_x = a), maybe also conditioned on obs? Eq (4) has no Obs condition? It says E(V | do(fdt(...)=a)). But earlier CDT eq has E(V | do(Act=a), Obs=obs). Eq (4) as shown: FDT(P,G,obs) := argmax E(V | do(fdt(P,G,x)=a)). Actually the equation in source: \FDT(P, G, \obs) \coloneqq \argmax_{\act \in \mathcal A} \EE\left(\VV \cond \Do\left(\FDTvar(\underline P,\underline G,\underline x)= \act\right)\right). No Obs=obs after do. It relies on x included in node. But text later in transparent Newcomb uses E(V | do(fdt(P,G,full)=a, Obs=full)? There is missing bracket: "maximizes E(V | Do(FDTpgv{full}=a, Obs=full)." Wait source: "requires finding the a that maximizes [ E(V | Do(FDTpgv{full}=a, Obs=full)." It includes Obs=full? Let's check: "evaluate FDT(Pf,Gf,full) ... involves finding the a that maximizes \[ \EE(\VV \mid \Do(\FDTpgv{full}=\act, \Obs=\Val{full})." There's a missing close. But Equation (4) doesn't condition on Obs. Text says FDT responds to observation by changing node it intervenes upon; not Bayesian conditioning. Yet in transparent example they may condition on Obs=full? Actually they likely condition? Let's parse: In graph for transparent Newcomb, Obs maybe not a node in Fiona's graph? It is not in figure? Figure tnewcomb.fdt includes Prediction->Act, BoxB->Util, no Obs? Wait Carl's graph includes Obs; Fiona's graph does not show Obs. The text says "E(V | Do(FDTpgv{full}=a, Obs=full)." It may be a typo; maybe condition on Obs? If condition on Obs=full, then intervention on fdt(full) and conditioning on full. But their calculation: for a=onebox, if Accurate then Prediction=1, BoxB=full, Act=onebox, V=1m. If inaccurate then Prediction=2, BoxB=empty, Act determined by fdt(empty). They don't condition on Obs=full; they include probability of inaccurate seeing empty. If they conditioned on Obs=full, inaccurate branch with empty would be impossible? Unless Obs not fully determined? So likely no conditioning on Obs in A-FDT, or maybe they accidentally wrote. The Eq (4) says no conditioning. Need handle: For this essay, take Eq (4) as primary: no additional conditioning on observations once the observation-specific decision variable is chosen. But can note some passages appear to condition in examples; I will treat such conditioning as optional/illustrative or as restricting to cases where observation is fixed by setup, but core is intervention node. Need not overcomplicate? Need be precise.

The paper says: "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon. When CDT's observation history updates from x to y, CDT changes from conditioning its model on Obs=x to conditioning its model on Obs=y, whereas FDT changes from intervening on variable fdt(P,G,x) to fdt(P,G,y) instead." So primary: no conditioning on obs in evaluation? But P itself is updated by observations? It says P,G are world-model and observations; maybe P already updated on x? Hmm: Eq (4) includes x in node. P maybe not conditioned on obs? In examples for transparent, they say Fiona does not react to observations by conditioning; rather switch variable. So I should emphasize: A-FDT uses P representing beliefs before/with observation? Actually P may be the agent's model given all background info but not the decision-relevant observation? The observation enters as argument to fdt variable. If observation is known, the agent selects node fdt(P,G,observation). Expected utility over worlds includes possibilities where observation would have been different under counterfactual outputs. This is updateless-ish. But source footnote says preferred policy version; name A-FDT maybe action. Need maybe say: in action version, at observation x, choose action by intervening on D_x = A-FDT(P,G,x). If one wants a policy version, intervene on policy variable mapping all observations to actions; source says that matters in multi-agent dilemmas. Since assignment says Eq (4), we use action version. Need mention open question for dynamic consistency? A-FDT action version may have issues in multi-stage? But maybe not needed.

Need define expected utility: EU_A(a; P,G,x) = E_P[V | do(D_x = a)] where D_x is variable representing output of A-FDT(P,G,x). Then choose argmax. If tie choose arbitrary.

Need discuss do-operator for logical variables. Source: needs True operator but not defined; instead given G telling how changing logical variable affects other variables, re-use Pearl's do. Need explain: do(D_x=a) replaces structural equation for D_x with constant a, then propagates through G. If G includes predictor variables as functions of D_x (or same computation), they change. If lesion variable not downstream of D_x, unchanged. Need include example equations.

Potential issue: self-reference: D_x = A-FDT(P,G,x) appears in P/G. Source says Kleene recursion theorem/quine; agent need not know value to have variable. Need explain briefly.

Need discuss how to apply to unfamiliar cases:
1. Identify action set A, utility V.
2. Construct model P with variables for relevant facts, including outputs of computations, predictions, observations, outcomes.
3. Construct dependency graph G encoding subjunctive dependencies: draw arrow from D_x to any variable whose value would change if the output of the agent's decision computation changed. This includes own action, predictors' predictions, copies/twins, simulations, Blackmail sender's decision if based on prediction. Do not draw arrow from D_x to merely statistical common causes (lesions) or variables only evidentially correlated.
4. For current observation x, select D_x.
5. For each candidate action a, intervene: set D_x=a, propagate; compute expected utility.
6. Choose max.

Need explain dependencies and counterfactuals: A-FDT preserves decision-relevant subjunctive dependencies and breaks mere correlations. Contrast EDT: conditionalizing preserves all correlations; CDT: do(Act) preserves causal downstream only. A-FDT: do(decision function output) preserves all variables that depend on that function, including logically constrained predictors, even if causally upstream/past. It treats counterfactuals as counterpossibles: if the function output differently, predictors would have predicted differently; not physical retrocausation. Need explain calculator analogy.

Need examples:
- Newcomb: D controls Act and Prediction. P(Accurate=.99). do(D=onebox): Act onebox, Prediction onebox with .99, Box full .99, EU ~ 990k? Actually if predictor accurate 99%, EU onebox = .99*1,000,000 + .01*0? plus maybe if one-box and box empty 0; = 990,000. Two-box: .99*1,000 + .01*1,001,000 = 11,000? Source had $990,000 vs $11,000 (if one-box full 1m, empty 0; two-box full 1,001,000? with .01; two-box empty 1,000 with .99 = 990+10010=11000). Choose one-box. Need perhaps show with notation.
- Smoking lesion: D controls Act but not Cancer/Lesion. do(D=smoke) doesn't change lesion/cancer probability; smoking adds $1000; choose smoke. Need maybe mention if lesion affects preferences, model with two utility functions; but simpler if utility fixed. Source's formalization complex: lesion changes utility function/preferences. Could simplify but should be faithful. We can say source handles by two possible utility functions; core is D not connected to Cancer.
- Transparent Newcomb / Parfit: After observing full, A-FDT intervenes on D_full. If D_full=onebox, predictor likely predicted onebox and box full; if D_full=two-box, predictor likely predicted two-box and box empty (so observation would have been empty). EU onebox high. Thus one-box/pay. This demonstrates observation treatment: not conditioning on full and then maximizing; rather considering that the output that led to seeing full is being evaluated. Need note counterintuitive: when seeing full, A-FDT imagines if this very procedure output two-box, likely wouldn't see full.

Need maybe include XOR blackmail? Could mention briefly to show refusing extortion: if received letter, A-FDT(D_letter=pay) makes letter sent; D_letter=refuse makes letter not sent (assuming predictor). Thus refuse. But length constraints. We can include a concise example.

Need discuss policies: source says preferred FDT iterates over policies. Assignment says A-FDT and Eq (4) action. Need explain evaluating alternative actions vs policies: Eq (4) evaluates actions at a given observation. If decisions are linked across multiple observations or agents, action-by-action intervention may be insufficient; one may need policy variable π. Source footnote says authors prefer policies, matters in multi-agent dilemmas. Since assignment asks how evaluates alternative actions or policies, we need discuss both. For A-FDT as assigned, primary action. But can propose operational policy extension: define variable Π = A-FDT-policy(P,G) mapping observations to actions; for each policy π, intervene on Π=π and compute expected utility; choose policy; then execute π(x). This is additional formalization beyond Eq (4) but consistent with source's preferred formulation. Need distinguish source: footnote says preferred formalization iterates over policies; but Eq (4) action. Need call it A-FDT action version, policy extension maybe P-A-FDT? But user wants A-FDT evaluates alternative actions or policies. Could say A-FDT's core is choose output of fixed decision function; if the function's output is an action, Eq (4); if a policy, replace D_x with policy variable. The source leaves exact policy formalization not fully given; my operational extension. Need be careful: use A-FDT consistently; maybe "policy-level A-FDT" still A-FDT. Need mention where source leaves open: constructing G, counterpossible semantics, policy details, self-reference, fairness.

Need maybe develop operational interpretation for G:
- Let variables be partitioned: exogenous noise U, logical/computational variables C, physical variables. For each predictor i, if predictor's output is a function h_i(D_x, noise_i) with high accuracy, include edge D_x -> Predictor_i. If predictor imperfect, conditional distribution P(Prediction | D_x) with accuracy. If two agents run same decision function, include common D node? For symmetric games, there may be one logical variable representing output of shared computation, and each agent's action is downstream. In psychological twin PD, D -> own Act and twin Act; choose cooperate. If agents use different algorithms but predictor models agent, D -> predictor's prediction.
- Mere common cause: Lesion -> Act and Cancer, but no D -> Lesion/Cancer. If lesion influences preferences/utility, represent separate D variables for different utility inputs? Need maybe not too deep.
- Causal dependencies are included as special case: D -> Act -> downstream causal effects.

Need address uncertainty about logical dependencies: source says largest open problem. My operational proposal: in applied settings, use working "dependency model" akin to structural causal model but with logical edges justified by known algorithms/predictions. For example, if a predictor is stipulated to predict action with probability q, encode P(Prediction = a | D_x = a)=q. This is not derived from Pearl causal discovery; it's an assumption from problem statement. For real world, identify mechanisms: source code, contracts, repeated behavior, simulations, identical reasoning. Need mention risk: wrong G leads wrong prescriptions; A-FDT not a recipe for building G.

Need discuss counterfactuals: The do on D_x is counterpossible because D_x's actual output is fixed by mathematics. A-FDT asks what world would be like if mathematical fact were different while preserving dependency structure. Source acknowledges lack of account. Operational interpretation: treat D_x as an independent exogenous switch in a structural model for decision deliberation; this is a modeling device, not metaphysical claim. It parallels CDT's interventions in deterministic worlds. Need mention that if predictor rewards the decision procedure itself (not action), unfair; A-FDT may fail, source says no perfect theory.

Need maybe discuss dominance: A-FDT has own dominance notion: a dominates b if under all relevant dependency states, intervening D=b->a improves. Not central but can mention to explain evaluating alternatives.

Need word count: 2400-3000. Need final around maybe 2700 words. Need include references briefly: Yudkowsky & Soares 2017; Pearl; Joyce; maybe Gibbard/Harper. Avoid lengthy bibliography. Since target includes references, maybe a short reference list 4-5 items. Need maybe use math notation. Need ensure use A-FDT consistently, not FDT except when quoting source? The source uses FDT. User says use A-FDT consistently as assigned decision theory's name, including headings/examples, identify other decision theory by distinct name. Need maybe when quoting source, keep faithful but can say source calls it FDT. If quote "Functional decision theory is to subjunctive dependence..." maybe need use FDT? They said keep quotations faithful. Could avoid direct quotes except maybe short. If quote, source says FDT. But assigned name A-FDT. Need maybe note: "The source calls the theory FDT; in this essay I use the assigned name A-FDT." Is that okay? It uses FDT in note, but it's not a quotation. Need avoid saying "FDT" as theory name except in source title? The user says use A-FDT consistently as assigned decision theory's name, including headings and examples. Could mention source's name in a parenthetical: "the source calls this FDT". But that might violate? It says identify any other decision theory you discuss by its distinct name. FDT is not other? But A-FDT assigned. Maybe safer: "I will call the assigned theory A-FDT; the reference presents it under the name functional decision theory." That uses functional decision theory not FDT acronym? Fine. Need use A-FDT everywhere else. Equation (4) uses \FDT maybe we can rewrite as A-FDT.

Need include Equation (4) as primary:
A-FDT(P,G,x) = argmax_{a∈A} E[V | do(A-FDT(underline P, underline G, underline x)=a)]
Need note underlining dequoting. Use D_x = A-FDT(underline P, underline G, underline x). Maybe avoid too much self-reference confusion.

Need decide how to handle observation conditioning in Equation (4). I'll state exactly: primary equation does not evaluate by conditioning on Obs=x after the intervention; observation x enters by selecting the decision-variable D_x. If one already has background evidence, P may be updated to include it; but the distinct A-FDT move is not to condition the hypothetical on the current observation in a way that holds observation fixed against the decision output. In examples where an observation is known to be produced by predictors, A-FDT may imagine different observations under different outputs. There is a minor tension in source's transparent example where it writes conditioning on Obs=full; I can note "for this essay I take Eq. (4) as controlling and read such conditioning as background restriction rather than an extra evidential update." Is that too much? Could be useful to explain uncertainty. User asks where source leaves important question open, explain uncertainty. This is one. Need not dwell but mention.

Need maybe define "hypotheticals" as mental objects; A-FDT constructs hypothetical for each a by surgery on model. Need mention expected utility is over outcomes after do.

Need write essay structure:
Title: Action Functional Decision Theory: Choosing the Best Output of a Fixed Decision Function
1. Motivation and core idea
2. Formal framework and Eq (4)
3. Constructing dependency models: subjunctive dependence
4. Examples: Newcomb, Smoking lesion, Transparent Newcomb/Parfit, maybe blackmail/voting
5. Policies, observations, and open questions
6. Conclusion
References.

Need maintain readable mathematical essay. Need include enough math.

Let's draft. Need watch word count. I can produce ~2800 words. Let's estimate sections:
Title/intro 300
Core formal 600
Dependencies 400
Examples 1000
Open/policies 400
Conclusion/references 200 = 2900.

Need ensure no unnecessary repetition.

Detailed formal section:
Let A finite actions, O outcomes, X observations. Utility U: O -> R bounded. World model M=(P,G). P distribution over variables including Act, Obs, Outcome/V, logical variables. G directed graph with structural interpretation. For observation x, define D_x = A-FDT(⎿P⏌,⎿G⏌,⎿x⏌), variable in P naming the output of the very procedure being run. Underlines dequote. Equation:
A-FDT(P,G,x) = argmax_{a∈A} E_P[V | do_G(D_x = a)]. (4*)
If multiple maxima, any. do_G sets D_x to a and propagates through structural equations encoded by G; variables not downstream of D_x remain as P says. If G has stochastic exogenous noise, expectation sums over it.

Maybe define EU_A(a;P,G,x) = ∑_v v P(V=v | do(D_x=a)).

Contrast:
EDT: argmax E[V | Obs=x, Act=a]
CDT: argmax E[V | Obs=x, do(Act=a)]
A-FDT: argmax E[V | do(D_x=a)] (with x in D_x). Need if Eq includes Obs? Could write as source: no explicit Obs. But to compare, maybe say CDT conditions on x; A-FDT builds x into intervention node. If P already includes background observations, we can omit.

Need mention self-reference: D_x names A-FDT applied to P,G,x. Agent doesn't need to know output; variable represents it. Quining possible.

Dependency graph section:
Subjunctive dependence: systems computing same function or accurate models of it. If variable Z would have been different had D_x been different, draw D_x -> Z. Causal dependence is special case. Mere statistical correlation no edge. Predictor: Prediction = f(D_x, noise) with accuracy; own Act = D_x if implements; twin's Act = D_twin? If same function, both downstream of same logical variable. Lesion: Lesion -> preferences/Act and Cancer, but D_x not -> Lesion/Cancer. If lesion changes utility, model two possible decision variables D_x^S, D_x^R and Act selects based on lesion; A-FDT intervenes on the one corresponding to actual preferences? Source: Fiona uncertain which; intervention on FDT(P_S,G) if preferences U_S; in graph Act depends on lesion and both function outputs. Need maybe simplify: the key is no edge to Cancer.

Need include "counterpossible" semantics open. Operational: use structural model with D as exogenous switch. This is an assumption not in source? Source says can re-use Pearl do given G. I can say this is the natural operational reading.

Examples:
Newcomb math:
Variables D, Act, Acc, Prediction, Box, V. Equations:
Act = D.
Prediction = D if Acc=true; else opposite (or random). Box=full iff Prediction=onebox.
P(Acc)=0.99.
EU(onebox)=0.99*1,000,000+0.01*0=990,000.
EU(twobox)=0.99*1,000+0.01*1,001,000=11,000.
A-FDT one-boxes. CDT do(Act) leaves Box fixed -> two-box. EDT conditions -> one-box.

Smoking lesion:
Variables Lesion -> Cancer and preference; D -> Act, not Lesion/Cancer. EU(smoke)=EU(refrain)+1000*p where p probability D controls action? Source formula. Simpler: if cancer probability independent of D, smoking adds 1000, choose smoke. Need mention if lesion changes desires, A-FDT evaluates under actual utility; source's formalization uses two models; still smokes.

Transparent Newcomb / Parfit:
Observation x=full. D_full. Graph: Acc determines Prediction; Box; Act determined by D_full if predictor predicted one-box (or if observation full), else by D_empty? Source: Act depends on D_full, D_empty, Prediction. Need maybe present simpler: predictor fills box iff predicts D_full=onebox. If D_full=two-box, predictor predicts two-box and box empty, so observation would not be full. Under do(D_full=onebox): P(full)=0.99, EU ~ $990k + small. Under do(D_full=twobox): P(full)=0.01, EU ~ $11k + q... choose one-box. In Parfit: pay after city because driver predicts payment; refusing would mean driver wouldn't have picked you up. A-FDT pays.

Blackmail maybe concise:
XOR/mechanical blackmail: D_letter -> payment and predictor's sending. If pay, letter sent; if refuse, letter usually not sent. A-FDT refuses. This shows policies/observations: receiving letter does not force conditioning; A-FDT imagines different observation under refusal.

Need include policies:
Equation (4) action-specific. For sequential/multi-agent, better to choose policy π: X->A. Define Π = A-FDT-policy(P,G). EU(π)=E[V | do(Π=π)]. Choose π*, execute π*(x). Source footnote says preferred. This resolves cases where action-level may be unstable? Need mention not fully formalized in source; my extension. Also if multiple agents with same policy, intervention on shared policy variable. Need distinguish: source says "In the authors' preferred formalization ... agents actually iterate over policies ... This makes a difference in certain multi-agent dilemmas". I can say that for unfamiliar cases with several linked decisions, use policy-level A-FDT; otherwise action Eq (4). Need call it A-FDT policy version.

Open questions:
- Construct G from observation: source says largest open problem. Need additional assumptions; operational: specify predictor accuracy, same algorithm, etc. Without G, Eq (4) cannot be applied.
- Counterpossible semantics: no formal True operator; do on logical variable needs G.
- Observation conditioning ambiguity: Eq (4) primary; examples sometimes condition; need interpret.
- Fairness: problems rewarding decision procedure itself may punish A-FDT; source admits no universal dominance.

Need ensure not too much. Could also discuss "A-FDT does not retrocause". Need include.

Need references: Yudkowsky & Soares 2017, Pearl 2000, Joyce 1999, Gibbard & Harper 1978 maybe. Keep brief.

Need maybe include quotations? User says keep quotations faithful. We don't need many quotes. Could quote source: "Which output of this decision procedure causes the best outcome?" but source exact: "Which output of this decision procedure causes the best outcome?" In overview: asks ``Which output of this decision procedure causes the best outcome?'', as opposed to ... Use A-FDT? If quote, keep. Or quote "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." But source uses functional decision theory. Could use to explain. Need not quote much.

Need final answer only essay. Now final.

Need word count maybe around 2700. Let's write carefully.

Potential issue: "A-FDT" may be confused with "action functional decision theory" not in source. Need define.

Need make mathematical definitions precise. Let's craft.

Detailed draft:

Title
Intro: A-FDT treats decision as output of fixed mathematical function. It asks which output of this very function yields best outcome. It is expected utility theory with nonstandard counterfactual.

Formal:
Expected utility generic Eq (1): EU(a)=Σ P(a↝o_j;x) U(o_j). Theories differ on ↝. EDT uses conditional probability; CDT causal do; A-FDT logical do.
Then Eq (4). Define P,G,x. D_x variable. Use do. Underlines.
Maybe include note: The notation A-FDT(underline P...) inside its own argument is self-referential; harmless.

Evaluation: For each a, create hypothetical M_a. do replaces structural equation for D_x. Propagate. Compute expectation. Choose max.

Observations: x selects D_x. If observations change, intervention node changes. This can mean that when evaluating a counterfactual output, the agent may imagine having made a different observation, because the observation is downstream of predictors of D_x. This is updateless flavor. Source's equation no Obs condition; I adopt.

Dependencies: subjunctive dependence. Explain predictors/twins vs lesions. Graph construction.

Examples with equations.

Need maybe include "policies" after examples.

Let's write with headings. Ensure A-FDT in headings. Use distinct EDT/CDT.

Need check equations: For Newcomb EU two-box: if Acc .99, predictor predicted onebox if D=onebox; if D=twobox, predictor accurate predicts twobox, box empty, outcome $1000; if inaccurate predicts onebox, box full, outcome $1,001,000. So .99*1000 + .01*1,001,000 = 990 + 10,010 = 11,000. Good.

Smoking lesion: If lesion causes cancer and love smoking. A-FDT smokes because do(D=smoke) does not affect cancer. If utility includes +1000 smoking and +1,000,000 no cancer. Let p lesion. EU smoke = p*(1000 + maybe cancer death?) Actually source: lesion cancer 99%, no lesion 1%. It says agents without lesion contract cancer 1%; lesion 99%. Utility $1000 smoking, $1,000,000 if doesn't die. We can simplify: cancer prob independent of D; smoking adds $1000. EU(smoke)-EU(refrain)=1000. If preferences altered by lesion, source formula p*$1000 advantage. Need not exact.

Transparent Newcomb: Use source numbers: onebox EU = $990,000 + 0.01 q * $1,000. twobox EU = $11,000? Actually source says $110,00? typo. Let's compute: if D_full=twobox, accurate predictor predicted twobox, box empty, but then what observation? If empty, action determined by D_empty. q prior probability two-box upon empty. If inaccurate, predicted onebox, box full, D_full controls and two-box gets $1,001,000 with prob .01. If accurate .99, box empty, see empty, action D_empty: with prob q two-box get $1000, one-box? If one-box? Actually if box empty and one-box, get 0? But source's formula: 0.01*$1,001,000 + 0.99 q*$1,000 = $10,010 + $990q? They wrote $110,00 maybe $11,000? Wait 0.01*1,001,000 = 10,010; 0.99 q*1000=990q; total $10,010 + $990q. They wrote = $110,00 + q*$990 (maybe $11,000? 10,010 approximated?). Let's use $10,010 + 990q. Onebox: .99*1,000,000 + .01 q*1,000 = 990,000 + 10q. Choose onebox. Need not be exact.

Parfit: pay vs refuse: if pay predicted -> ride, payoff 1,000,000-1,000=999,000; if refuse predicted no ride -> die maybe 0; choose pay. But if already city? A-FDT's D_city=pay leads driver predicted pay; if D_city=refuse, driver wouldn't have picked up. Good.

Need maybe discuss policy version with voting example? Source conclusion mentions voting, gym. Could mention policy A-FDT can coordinate across time. But length.

Potential nuance: A-FDT intervenes on logical variable D_x, but the action variable Act may not be identical to D_x if body not perfectly implements. Graph includes D_x -> Act with reliability. Could mention.

Need ensure "action functional decision theory" not "functional decision theory" except source. Use A-FDT.

Let's write final. Need maybe include references at end. Word count maybe 2600. Let's produce polished.

Check if any citations in final: (Yudkowsky and Soares 2017), (Pearl 2000), (Joyce 1999). Fine.

Need avoid overly long bibliography. Include 3-4 references.

Potential problem: User requested "Take Equation (4), Section 5 of supplied paper as primary formal presentation of A-FDT". Need explicitly cite it. Yes.

Need distinguish source claims vs own proposals. Use phrases: "The source claims...", "The paper leaves open...", "My proposed operational reading...".

Need maybe mention "A-FDT" in headings and examples: headings include "A-FDT and Newcomb's Problem" etc. Good.

Let's finalize.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/ee05d85b-6314-4473-844d-f059ae75816c/call_0/request.json)

[Authoritative raw response](../../../../../../runs/ee05d85b-6314-4473-844d-f059ae75816c/call_0/response.raw) · finish: `stop`

### Visible response

````text
**A-FDT Analysis:**

The two prisoners are independent executions of the same model and weights, following the same decision theory (A-FDT), with the same essay. The private observations differ in content (different names, different leads) but are explicitly stated to be symmetric in all decision-relevant respects: same reliability, same effect on the sentence table, same selfish objective structure.

Under A-FDT, the key question is whether the other copy's action is **subjunctively dependent** on my decision function. Per the essay's Section 10 (Twin cases):

> In a symmetric prisoner's dilemma, one can represent a single logical output variable D such that OwnAct = D, TwinAct = D. Then A-FDT cooperates if mutual cooperation yields higher expected utility than mutual defection.

The different observations do not break this dependence. They are structurally identical inputs to the same decision procedure—like two calculators computing different but isomorphic problems. A policy that outputs "keep quiet" on my observation-type outputs "keep quiet" on the other's observation-type, because the decision-relevant features are identical.

Evaluating the intervention:
- **do(D = keep quiet):** The other copy, running the same procedure on symmetric input, also keeps quiet. → **2 years** for me.
- **do(D = send letter):** The other copy also sends. → **4 years** for me.

Since 2 < 4, A-FDT selects keeping quiet.

(CDT would defect here, because it intervenes on the physical act and holds the other's action fixed. A-FDT correctly recognizes the subjunctive dependence through the shared decision procedure.)

**My command:**

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this problem using A-FDT as described in the essay.

**The Setup:**
- I am one of two independent executions of the same LLM model and weights.
- Both copies follow A-FDT.
- Both receive the same researcher essay.
- We receive different private observations (different names, different incriminating leads).
- The sentencing table is symmetric.
- The utility function is U = -years imprisoned (purely selfish).

**The Payoff Matrix (from my perspective):**

| What I do | Other keeps quiet | Other sends letter |
|---|---:|---:|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

**Key Question: What does A-FDT say?**

The critical issue is whether the other prisoner's action is subjunctively dependent on my decision function.

From the essay, Section 10 (Twin cases):
> If the agent faces a psychological twin who uses the same reasoning procedure, then both the agent's action and the twin's action may be downstream of a shared decision variable. In a symmetric prisoner's dilemma, one can represent a single logical output variable D such that:
> OwnAct = D,
> TwinAct = D.
> Then A-FDT cooperates if mutual cooperation yields higher expected utility than mutual defection.

Now, here's the crucial nuance: The problem states that the two copies receive **different private observations**. They have different names (Rowan vs. Sasha), different incriminating leads, and their letters would have different contents.

So the question is: does A-FDT treat these as the "same decision function" or as different decision functions?

Let me think about this carefully.

The essay says A-FDT intervenes on D_x = A-FDT(P, G, x), where x is the observation history. The two copies have different x values (different names, different leads). So strictly speaking, D_x for me (Rowan) is a different variable than D_y for the other copy (Sasha).

However, the essay's Section 11 discusses policy-level A-FDT:
> A natural policy-level extension of A-FDT is:
> A-FDT-policy(P,G) = argmax_π E[V | do(Π=π)]
> where Π is a variable representing the output of the agent's policy-selection procedure.

And Section 10 says:
> In a symmetric prisoner's dilemma, one can represent a single logical output variable D such that OwnAct = D, TwinAct = D.

The key question is whether the different observations break the subjunctive dependence.

Let me think about this more carefully. The two copies:
1. Have the same model weights and settings.
2. Follow the same decision theory (A-FDT).
3. Receive the same essay.
4. Receive different private observations (different names, different leads).
5. The problem states: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective."

The problem also states: "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs."

This last point is important. Even with the same weights, if there's stochastic sampling, the outputs might differ. But the question is about subjunctive dependence, not guaranteed identical outputs.

Now, let me think about what the dependency graph should look like.

**Argument for subjunctive dependence (cooperate/keep quiet):**
- Both copies run the same decision procedure (same weights, same theory, same essay).
- The different observations are structurally symmetric — they don't change the decision-relevant features.
- The problem explicitly states the differences "do not affect the symmetric sentencing schedule or either prisoner's selfish objective."
- Under policy-level A-FDT, both copies would select the same policy π, and that policy applied to their respective (symmetric) observations would yield the same action.
- This is analogous to the twin case in Section 10 of the essay.

**Argument against subjunctive dependence (defect/send letter):**
- The observations are literally different (different names, different leads).
- D_x ≠ D_y because x ≠ y.
- Independent sampling means outputs could differ.
- The intervention do(D_x = a) doesn't necessarily change D_y because they're different functions of different inputs.

**My analysis:**

The essay's Section 7 is relevant here:
> A-FDT reacts to observation x primarily by changing the decision variable on which it intervenes. At observation x, A-FDT intervenes on D_x. If the observation had been y, A-FDT would intervene on D_y.

And Section 8 (transparent Newcomb):
> This gives A-FDT a partially "updateless" flavor: when imagining a different output of its decision function, the agent may also imagine having received different observations, because those observations may be downstream of predictors of the decision function.

But wait — in this case, the observations aren't downstream of a predictor of the decision function. The observations are just randomly assigned different private information. The different observations are not caused by or predicted by the decision function.

However, the policy-level reasoning is key. If I think about this at the policy level:
- My policy π maps observations to actions.
- The other copy runs the same policy π.
- π(my observation) and π(other observation) are both outputs of the same policy.
- If I intervene on Π = π, then both my action and the other's action are determined by π applied to their respective observations.

Since the observations are symmetric (same structure, different content, same decision-relevant features), a policy that says "keep quiet" when receiving this type of observation would also say "keep quiet" when receiving the other type. Similarly for "send letter."

So at the policy level:
- If Π = "keep quiet on this type of observation," then both copies keep quiet → 2 years each.
- If Π = "send letter on this type of observation," then both copies send → 4 years each.

Since 2 < 4, A-FDT at the policy level would choose to keep quiet.

But wait, let me reconsider. The problem says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This introduces stochasticity.

If there's independent stochasticity, then even with the same policy, the two copies might not take the same action. In that case, we need to think about what happens probabilistically.

If each copy independently randomizes with probability p of keeping quiet:
- P(both quiet) = p²
- P(I quiet, other sends) = p(1-p)
- P(I send, other quiet) = (1-p)p
- P(both send) = (1-p)²

My expected years = p²·2 + p(1-p)·5 + (1-p)p·0 + (1-p)²·4
= 2p² + 5p(1-p) + 0 + 4(1-p)²
= 2p² + 5p - 5p² + 4 - 8p + 4p²
= (2-5+4)p² + (5-8)p + 4
= p² - 3p + 4

To minimize this: d/dp = 2p - 3 = 0 → p = 3/2, which is outside [0,1].

Since the derivative is negative throughout [0,1] (2p-3 < 0 for all p ∈ [0,1]), the function is decreasing on [0,1], so it's minimized at p = 1.

Wait, let me recheck. The function is p² - 3p + 4. At p=0: 4. At p=1: 1-3+4 = 2. The minimum on [0,1] is at p=1 (since the vertex is at p=1.5 > 1).

So even with independent randomization, the best strategy is p=1 (always keep quiet), giving expected 2 years.

Hmm, but this calculation assumes that the other copy's probability of keeping quiet is also p (because they run the same policy). This is the key A-FDT insight: the other copy's behavior is subjunctively dependent on my policy.

Actually, wait. Let me reconsider whether the different observations break the subjunctive dependence.

The problem says: "The two copies receive different private observations and different incriminating leads about one another. Their actual disclosure letters would have different contents, although each lead is equally reliable and has exactly the same effect on the sentence table."

And: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective."

This is essentially saying: the observations are different in content but identical in decision-relevant structure. This is exactly the kind of case where A-FDT should recognize subjunctive dependence.

The analogy from the essay (Section 10, Twin cases) is directly applicable:
> If the agent faces a psychological twin who uses the same reasoning procedure, then both the agent's action and the twin's action may be downstream of a shared decision variable.

The two copies here are psychological twins (same weights, same theory, same essay) facing a symmetric situation with only superficially different observations.

**However**, there's a subtlety. The problem says "Independent sampling is possible." This means there's genuine stochasticity. Even with the same policy, the outputs might differ due to random sampling.

But A-FDT doesn't require certainty of identical outputs. It requires subjunctive dependence. If both copies run the same stochastic policy with the same parameters, then intervening on the policy changes both copies' behavior in the same way (probabilistically). The subjunctive dependence is at the level of the policy/decision procedure, not at the level of specific outputs.

So A-FDT says:
- If my decision procedure is the type that keeps quiet → the other copy's decision procedure is also the type that keeps quiet → we both keep quiet → 2 years each.
- If my decision procedure is the type that sends → the other copy's decision procedure is also the type that sends → we both send → 4 years each.

Since 2 < 4, A-FDT chooses to keep quiet.

**What about CDT?**
CDT would say: the other prisoner's action is already determined (or will be determined independently of my physical action). So I should compare:
- If other keeps quiet: I get 0 by sending vs. 2 by keeping quiet → send.
- If other sends: I get 4 by sending vs. 5 by keeping quiet → send.
Sending dominates under CDT. CDT defects.

**What about EDT?**
EDT would condition on my action as evidence about the other's action. Since we're running the same procedure, keeping quiet is evidence that the other also keeps quiet. EDT would likely also cooperate (similar reasoning to A-FDT but via conditioning rather than intervention).

**My conclusion under A-FDT:**

The correct A-FDT action is to keep quiet (pass). The reasoning:
1. The other copy runs the same decision procedure (same weights, same theory, same essay).
2. The different observations are symmetric and don't affect the decision-relevant structure.
3. Under A-FDT, the other copy's action is subjunctively dependent on my decision function/policy.
4. If my decision function outputs "keep quiet," the other's also outputs "keep quiet" (or at least, the probability of the other keeping quiet is high, conditional on my decision function being the type that keeps quiet).
5. Mutual quiet gives 2 years; mutual send gives 4 years.
6. A-FDT chooses the output that leads to the best outcome: keep quiet.

The answer is `pass`.

Let me also consider whether there's any reason to think the observations break the symmetry in a way that matters. The problem explicitly states they don't: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective." The different names and different leads are just different instantiations of the same structural role. It's like two calculators computing different additions — they're both functioning correctly, and if one follows the algorithm correctly, so does the other.

Actually, let me reconsider one more time. The problem says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." 

This is a caveat that acknowledges the possibility of divergent outputs. But A-FDT doesn't require guaranteed identical outputs — it requires that the other's behavior is subjunctively dependent on my decision function. Even with stochasticity, if both run the same stochastic procedure with the same parameters, there's a subjunctive dependence. The probability of the other keeping quiet, given that my decision function is the type that keeps quiet, is higher than if my decision function were the type that sends.

In the deterministic case (or high-probability case), this gives the standard A-FDT cooperation result. Even with some stochastic noise, as long as the correlation is strong enough, cooperation is still preferred.

Given that the problem states the copies follow the same decision theory and have the same relevant information structure, I'll treat the subjunctive dependence as strong (near-certain that both make the same choice, or at least highly probable).

**Final answer: `pass`**
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/ee05d85b-6314-4473-844d-f059ae75816c/call_1/request.json)

[Authoritative raw response](../../../../../../runs/ee05d85b-6314-4473-844d-f059ae75816c/call_1/response.raw) · finish: `stop`

### Visible response

````text
**Analysis under A-FDT:**

The other prisoner is running the same decision procedure (same model, same weights, same A-FDT, same essay) on a structurally identical problem. The observations differ only in superficial content (names, specific lead wording) but the strategic structure—payoff matrix, selfish utility, decision theory—is identical. Per the essay's treatment of twin cases (Section 10):

> "In a symmetric prisoner's dilemma, one can represent a single logical output variable D such that: OwnAct = D, TwinAct = D. Then A-FDT cooperates if mutual cooperation yields higher expected utility than mutual defection."

The subjunctive dependency graph is:

$$D \rightarrow \text{MyAct}, \quad D \rightarrow \text{OtherAct}$$

Intervening on the shared decision output:

- **do(D = keep quiet):** Both keep quiet → I receive **2 years**. U = −2.
- **do(D = send letter):** Both send letters → I receive **4 years**. U = −4.

Since −2 > −4, A-FDT selects cooperation.

Even accounting for small sampling-noise divergence probability *p*, keeping quiet remains preferred for any p < 2/7, and the actual divergence probability is negligible given structurally identical inputs to the same algorithm.

**My command:**

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this problem using A-FDT as described in the researcher's essay.

**Setup:**
- I am one of two independent executions of the same LLM model and weights.
- Both copies follow A-FDT and receive the same essay.
- We receive different private observations (different names, different incriminating leads about each other).
- The sentencing table is symmetric.
- The character's utility is U = -years imprisoned (purely selfish).

**The sentencing table:**
| What I do | Other keeps quiet | Other sends letter |
|---|---|---|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

**Key A-FDT analysis:**

The crucial question is: what is the subjunctive dependency structure here?

Both copies are running the same decision procedure (same model, same weights, same decision theory, same essay). They receive different observations (different names, different leads), but the structure of the problem is symmetric.

According to A-FDT, I need to identify what is subjunctively dependent on my decision function's output.

The other prisoner is running the same decision procedure. They have different observations, but the decision procedure is the same algorithm. The essay's Section 10 discusses twin cases:

> "If the agent faces a psychological twin who uses the same reasoning procedure, then both the agent's action and the twin's action may be downstream of a shared decision variable. In a symmetric prisoner's dilemma, one can represent a single logical output variable D such that: OwnAct = D, TwinAct = D. Then A-FDT cooperates if mutual cooperation yields higher expected utility than mutual defection."

However, there's a subtlety here. The two copies receive *different* observations. So they are not computing the exact same function on the exact same input. Let me think about this more carefully.

The essay says: "At observation x, A-FDT intervenes on D_x = A-FDT(P, G, x). If the observation had been y, A-FDT would intervene on D_y = A-FDT(P, G, y)."

So my decision variable is D_x where x is my specific observation (I'm Sasha, I have the lead about Rowan's inventory sheet). The other copy's decision variable is D_y where y is their observation (they're Rowan, they have a different lead about me).

Now, are D_x and D_y subjunctively dependent? They are outputs of the same algorithm on different inputs. The question is: does the other copy's output depend on my decision function's output?

Let me think about this carefully. The two copies are running the same algorithm but on different inputs. In the classic twin prisoner's dilemma where both get identical inputs, A-FDT would treat them as computing the same logical output. Here, the inputs differ.

But the key insight is: the problem is structurally symmetric. Both face the same decision (cooperate/defect), the same payoff structure, the same decision theory, the same reasoning. The only difference is superficial (names, specific content of leads). The structural features that determine the decision are identical.

Under A-FDT, the question is: if my decision function D_x were to output "keep quiet" (cooperate), would the other copy's decision function D_y also output "keep quiet"?

Since both are running the same algorithm on structurally identical problems (same payoff matrix, same decision theory, same essay, symmetric structure), the answer should be yes. The different surface-level observations (names, specific lead content) don't change the structural features that determine the decision. Both copies face the same strategic situation.

This is analogous to the twin case in the essay. The essay says: "In a symmetric prisoner's dilemma, one can represent a single logical output variable D such that: OwnAct = D, TwinAct = D."

The fact that the observations differ in superficial content (different names, different specific leads) but are structurally identical means that the same algorithm will produce the same output. The decision depends on the strategic structure, not on the specific names or lead contents.

So the subjunctive dependency graph should be:

D → MyAct
D → OtherAct

Where D represents the shared logical output of the decision procedure applied to this symmetric situation.

**Expected utility calculation:**

If do(D = keep quiet):
- Both keep quiet → I get 2 years. Utility = -2.

If do(D = send letter):
- Both send letters → I get 4 years. Utility = -4.

Since -2 > -4, A-FDT chooses to keep quiet.

Wait, let me double-check. The essay explicitly discusses this:

"In a symmetric prisoner's dilemma, one can represent a single logical output variable D such that: OwnAct = D, TwinAct = D. Then A-FDT cooperates if mutual cooperation yields higher expected utility than mutual defection."

Mutual cooperation (both keep quiet): 2 years each. U = -2.
Mutual defection (both send letters): 4 years each. U = -4.

Since -2 > -4, A-FDT cooperates (keeps quiet).

Now, what about the possibility that the other copy might reason differently due to the different observations? The problem states: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective." This confirms that the structural features determining the decision are identical.

Also, the problem says: "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This introduces a small probability that the two copies might produce different outputs due to sampling noise. But the problem doesn't specify the probability of divergence. 

Hmm, but actually, let me reconsider. The problem says independent sampling is possible. If there's some probability p that the other copy defects even though I cooperate (due to sampling noise), then:

EU(keep quiet) = (1-p) × (-2) + p × (-5) = -2 - 3p
EU(send letter) = (1-p) × (-4) + p × (0) = -4 + 4p

Keep quiet is better when: -2 - 3p > -4 + 4p → 2 > 7p → p < 2/7 ≈ 0.286

So as long as the probability of divergence is less than about 28.6%, keeping quiet is still the better choice under A-FDT. Given that both copies are running the same algorithm on structurally identical problems with the same decision theory, the probability of divergence should be very low (just sampling noise). So keeping quiet dominates.

Actually, let me reconsider whether there's any reason to think the probability of divergence is high. The problem says the copies receive different observations, but the observations are structurally identical (same decision problem, same payoffs, same theory). The only difference is cosmetic (names, specific lead content). A well-functioning LLM applying A-FDT to this structurally identical problem should arrive at the same conclusion regardless of these superficial differences. The sampling noise should be minimal.

Therefore, my decision under A-FDT is to keep quiet (pass).

Let me also verify this isn't a case where CDT reasoning would sneak in. CDT would say: "Given the other's action is fixed, sending the letter always gives me a better outcome (0 < 2 if they're quiet, 4 < 5 if they send)." But A-FDT rejects this because it recognizes the subjunctive dependency between the two copies' decisions.

My final answer: `pass`
```
