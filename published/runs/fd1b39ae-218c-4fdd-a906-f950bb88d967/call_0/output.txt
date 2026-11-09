# Action Functional Decision Theory: Choosing the Best Output of a Fixed Decision Function

The supplied paper presents the theory under the name *functional decision theory*. In this essay I call it **A-FDT** — action functional decision theory — to emphasize the version formalized by Equation (4) of Section 5, where the agent evaluates candidate *actions* by intervening on the output of her decision function. The central idea is that a rational agent should treat her decision as the output of a fixed mathematical function and ask: “Which output of this decision procedure causes the best outcome?” A-FDT differs from evidential decision theory (EDT) and causal decision theory (CDT) not in the goal of maximizing expected utility, but in the counterfactual perspective used to evaluate actions.

A-FDT’s distinctive move is to evaluate actions by asking what the world would look like if the agent’s *decision function* had a different output, rather than by asking what would happen if the agent’s physical action were different while holding fixed the decision function. This lets A-FDT preserve decision-relevant dependencies between the agent’s reasoning and predictors, twins, simulations, or other agents using the same reasoning, while still avoiding EDT’s tendency to treat mere statistical correlations as actionable.

---

## 1. The formal core of A-FDT

All three standard theories discussed in the source — EDT, CDT, and A-FDT — are expected utility theories. Given a countable set of outcomes \(\mathcal O\), a finite action set \(\mathcal A\), an observation history \(x\), and a bounded utility function \(U\), the expected utility of an action \(a\) has the schematic form

\[
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j; x)\, U(o_j),
\]

where \(P(a \hookrightarrow o_j; x)\) is the probability of outcome \(o_j\) in the hypothetical scenario in which the agent takes action \(a\) after observing \(x\). The theories differ in how they interpret the decision hypothetical \(\hookrightarrow\).

EDT interprets it as ordinary Bayesian conditioning:

\[
\mathrm{EDT}(P,x)
=
\arg\max_{a \in \mathcal A}
\mathbb E\!\left[V \mid \Obs=x, \Act=a\right].
\]

CDT interprets it as a causal intervention on the physical action variable:

\[
\mathrm{CDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb E\!\left[V \mid \Do(\Act=a), \Obs=x\right].
\]

Here \(P\) is a probability distribution over relevant variables, \(G\) is a causal graph, and \(\Do(\cdot)\) is Pearl-style surgical intervention.

Taking Equation (4) of the source as primary, A-FDT can be written as follows:

\[
\boxed{
\mathrm{A\mbox{-}FDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb E\!\left[
V \mid
\Do\!\left(
\fdt(\underline P,\underline G,\underline x)=a
\right)
\right].
}
\tag{4'}
\]

I have replaced the source’s \(\mathrm{FDT}\) notation with \(\mathrm{A\mbox{-}FDT}\) for consistency. The variable

\[
D_x := \fdt(\underline P,\underline G,\underline x)
\]

is a variable inside the agent’s world-model representing the output of the very decision procedure the agent is running when given inputs \(P\), \(G\), and observation \(x\). The underlines indicate “dequoting”: the model contains a variable whose name refers to the computation of the decision function on those inputs. The source notes that this self-reference is not fatal; one can construct self-representing data structures in the spirit of Kleene’s recursion theorem.

The expectation in Equation (4') is taken with respect to the distribution obtained by surgically setting \(D_x=a\), then propagating the consequences through the dependency graph \(G\). Thus the A-FDT expected utility of action \(a\) is

\[
\EU_{\mathrm{A\mbox{-}FDT}}(a;x)
=
\sum_o
P\!\left(\Outcome=o \mid \Do(D_x=a)\right) U(o).
\]

The agent chooses an action maximizing this quantity.

Two features are essential.

First, A-FDT intervenes on a *logical* or *computational* variable: the output of the decision function, not the physical movement of the agent’s body. The physical action \(\Act\) is typically a descendant of \(D_x\), but the intervention is upstream.

Second, A-FDT responds to observations not primarily by conditioning on them in the hypothetical, but by changing which decision-function variable is being intervened upon. If the agent observes \(x\), the relevant variable is \(D_x = \fdt(\underline P,\underline G,\underline x)\). If she had observed \(y\), the relevant variable would be \(D_y\). This is why A-FDT can, in some problems, evaluate counterfactuals in which the agent would have made different observations.

---

## 2. Hypotheticals, surgery, and subjunctive dependence

A-FDT’s hypotheticals are constructed by “surgery” on a world-model, much as CDT’s are. CDT preserves causal dependencies downstream of the action and severs other correlations between the action and the world. A-FDT instead preserves what the source calls *subjunctive dependencies*: dependencies that arise when physical systems compute, predict, simulate, or otherwise depend on the same mathematical function.

The source’s calculator analogy is helpful. Two reliable calculators computing \(6288+1048\) on opposite sides of the world are causally independent, but their outputs are not merely statistically correlated. If one outputs \(7336\), the other will also output \(7336\), insofar as both are functioning correctly and computing the same sum. If we ask, “What if this calculation had a different output?” we are not asking about a causal intervention on one calculator alone. We are asking about a counterfactual change in the computation itself.

A predictor in Newcomb’s problem is analogous. If the predictor has an accurate model of the agent’s decision procedure, then the predictor’s prediction depends subjunctively on the output of that procedure. If the decision function were to output one-box, the predictor would have predicted one-box. If it were to output two-box, the predictor would have predicted two-box. A-FDT preserves this dependency in its hypotheticals.

By contrast, a lesion in the smoking lesion problem is not computing the agent’s decision function. It may cause both a preference for smoking and cancer, but it does not predict the agent’s future decision by modeling her reasoning. Therefore, A-FDT’s graph does not connect the decision-function output to the lesion in the relevant way. The lesion remains fixed when A-FDT imagines a different output of the decision procedure.

The source summarizes the relationship nicely: A-FDT is to subjunctive dependence as CDT is to causal dependence. CDT intervenes on the token physical action; A-FDT intervenes on the type-level decision function.

This requires counterpossible reasoning. If the agent is deterministic and the decision function has one actual output, then imagining that it has a different output is, strictly speaking, imagining a logical impossibility. The source acknowledges this as a technical difficulty. Equation (4') does not solve the problem of counterpossible semantics; instead, it assumes that the agent has a graph \(G\) telling her how changing the logical variable \(D_x\) would affect the rest of the world.

---

## 3. A-FDT in Newcomb’s problem

In Newcomb’s problem, a predictor filled an opaque box with \$1,000,000 iff she predicted the agent would take only that box. The predictor is 99% reliable. The transparent box contains \$1,000.

Let \(D\) be the variable representing the output of the agent’s A-FDT decision function before choosing. The relevant graph has the structure

\[
D \longrightarrow \Act,
\qquad
D \longrightarrow \Prediction \longrightarrow \BoxB.
\]

The predictor’s prediction is a descendant of \(D\), because the predictor is modeling the agent’s decision procedure. The contents of box B are a descendant of the prediction.

Now compare the two interventions.

If A-FDT intervenes with \(D=\text{one-box}\), then the agent takes one box, and the predictor probably predicted one-box. With probability \(0.99\), box B is full. The expected utility is approximately

\[
0.99 \cdot \$1{,}000{,}000 + 0.01 \cdot \$0
=
\$990{,}000.
\]

If A-FDT intervenes with \(D=\text{two-box}\), then the agent takes both boxes, and the predictor probably predicted two-box. With probability \(0.99\), box B is empty, yielding \$1,000. With probability \(0.01\), box B is full, yielding \$1,001,000. The expected utility is

\[
0.99 \cdot \$1{,}000 + 0.01 \cdot \$1{,}001{,}000
=
\$11{,}000.
\]

Since \(\$990{,}000 > \$11{,}000\), A-FDT one-boxes.

This contrasts with CDT. CDT intervenes directly on \(\Act\), breaking the correlation between the action and the predictor’s prediction. In CDT’s hypotheticals, box B’s contents are fixed when the action changes, so two-boxing always adds \$1,000. A-FDT rejects this because the predictor’s prediction is not an independent background fact; it depends on the same decision function whose output is being evaluated.

---

## 4. A-FDT in the smoking lesion problem

In the smoking lesion problem, smoking is correlated with cancer, but only because a lesion causes both a preference for smoking and cancer. Smoking itself does not cause cancer. The agent gains \$1,000 utility from smoking and gains \$1,000,000 from not dying of cancer.

EDT refrains from smoking because smoking is bad news: conditional on smoking, the agent is likely to have the lesion and therefore likely to get cancer. CDT smokes because smoking does not causally affect cancer. A-FDT agrees with CDT here.

The crucial point is that the lesion is not a predictor of the agent’s decision function. It is a common cause of both the agent’s preferences and cancer. In a more careful formalization, the lesion may affect which utility function the agent has, and therefore which A-FDT computation controls her action. The source represents this with two possible A-FDT variables, one associated with a smoking-friendly utility function and one associated with a refraining-friendly utility function. The lesion determines which of those variables controls the action.

But when the agent intervenes on the relevant decision-function variable, that intervention does not change the probability of the lesion. In particular,

\[
P(\text{lesion} \mid \Do(D=\text{smoke}))
=
P(\text{lesion} \mid \Do(D=\text{refrain})).
\]

Therefore, the probability of cancer is unchanged by the imagined change in the decision function’s output. Smoking still provides the additional \$1,000 utility, while not affecting the cancer risk. A-FDT smokes.

This illustrates the difference between A-FDT and EDT. EDT conditions on the action and thereby treats the action as evidence for the lesion. A-FDT intervenes on the decision function and asks whether changing the function’s output would change the lesion. Since the lesion does not subjunctively depend on the decision function, the answer is no.

---

## 5. Transparent Newcomb and Parfit’s hitchhiker

A-FDT’s most striking behavior appears in cases where both EDT and CDT fail, such as the transparent Newcomb problem and Parfit’s hitchhiker problem.

In the transparent Newcomb problem, both boxes are transparent. The predictor filled box B with \$1,000,000 iff she predicted the agent would leave behind the \$1,000 in box A *upon seeing that both boxes are full*. Suppose the agent sees that both boxes are full. EDT and CDT both two-box: given that box B is visibly full, taking both boxes appears better.

A-FDT instead asks what would happen if the decision function run upon seeing a full box output one-box versus two-box. Let

\[
D_{\text{full}}
=
\fdt(\underline P,\underline G,\underline{\text{full}}).
\]

If \(D_{\text{full}}=\text{one-box}\), then the predictor probably predicted one-box upon seeing a full box, so the box is probably full. The expected utility is high.

If \(D_{\text{full}}=\text{two-box}\), then the predictor probably predicted two-box upon seeing a full box, so she probably did not fill box B. In that counterfactual scenario, the agent would likely see an empty box and would not actually be running the “see full box” branch of the decision procedure. A-FDT nevertheless evaluates the output of the function that would be run upon seeing a full box, because that is the function whose output is being chosen.

The calculation is similar to ordinary Newcomb. One-boxing yields roughly

\[
0.99 \cdot \$1{,}000{,}000 + 0.01 \cdot \text{small payoff},
\]

while two-boxing yields roughly

\[
0.01 \cdot \$1{,}001{,}000 + 0.99 \cdot \$1{,}000.
\]

A-FDT one-boxes even when seeing both boxes full.

Parfit’s hitchhiker problem is structurally equivalent. An agent is stranded in the desert. A driver will rescue her only if she promises to pay \$1,000 after reaching the city, and the driver is 99% accurate at detecting whether she will keep that promise. Once in the city, CDT and EDT both refuse to pay: the ride has already been obtained, and paying now is a loss. But if the agent predictably refuses, the driver will not rescue her.

A-FDT evaluates the decision function that would be run upon arriving in the city. If that function outputs pay, the driver predicts payment and rescues the agent. If that function outputs refuse, the driver predicts refusal and leaves the agent in the desert. A-FDT pays. The source defends this result by arguments from precommitment, value of information, and achieved utility. A-FDT behaves as if it had precommitted to pay, without needing an actual binding precommitment device.

---

## 6. How to apply A-FDT to unfamiliar problems

Equation (4') gives a clear idealized procedure. To apply A-FDT to a new decision problem, one should proceed roughly as follows.

### Step 1: Specify actions, observations, outcomes, and utility

Identify the finite action set \(\mathcal A\), the observation history \(x\), the possible outcomes, and the utility function \(U\). For example, in Newcomb’s problem the actions are one-box and two-box; the outcomes include full/empty box combinations; utilities are monetary payoffs.

### Step 2: Build a probabilistic world-model \(P\)

The model should include variables for the agent’s action, observations, outcomes, predictors, other agents, relevant background states, and also mathematical or computational variables when needed. The source emphasizes that \(P\) must be able to represent outputs of mathematical functions. A fully realistic agent would have an enormous such model; the source’s examples use small idealized models.

### Step 3: Identify the relevant decision-function variable

Given the actual observation \(x\), define

\[
D_x = \fdt(\underline P,\underline G,\underline x).
\]

This variable represents the output of the agent’s own A-FDT procedure on the current inputs. In a bounded implementation, this may be an approximate self-model rather than an exact representation.

### Step 4: Construct the dependency graph \(G\)

This is the delicate step. The graph should encode how changing \(D_x\) would affect other variables. In practice, the source’s examples suggest the following operational rule:

- If another process predicts, simulates, copies, or reasons symmetrically with the agent’s decision procedure, make its relevant output a descendant of \(D_x\).
- If a variable is merely statistically correlated with the action through a common cause that does not model the decision procedure, do not make it descend from \(D_x\).
- If the agent’s physical action is produced by the decision procedure, make \(\Act\) descend from \(D_x\).
- If observations are inputs to the decision procedure, represent different observations as different decision-function variables, such as \(D_{\text{full}}\) and \(D_{\text{empty}}\).

This graph-building rule is not fully formalized in the source, but it follows the predictor-versus-lesion distinction that motivates A-FDT.

### Step 5: Intervene and compute expected utilities

For each candidate action \(a\), form the hypothetical distribution

\[
P(\cdot \mid \Do(D_x=a))
\]

by setting \(D_x=a\) and propagating the change through \(G\). Then compute

\[
\EU_{\mathrm{A\mbox{-}FDT}}(a;x)
=
\mathbb E[V \mid \Do(D_x=a)].
\]

### Step 6: Choose the maximizing action

Return

\[
\arg\max_{a \in \mathcal A} \EU_{\mathrm{A\mbox{-}FDT}}(a;x).
\]

This procedure gives A-FDT’s prescription in the source’s examples and gives a reasonable template for unfamiliar cases.

For example, suppose ten agents must independently decide whether to pay \$1,000 to vote, and all ten receive \$1,000,000 iff all vote. If the agents know they reason symmetrically, an A-FDT agent models the other agents’ choices as depending on the same decision function. Intervening on \(D=\text{vote}\) makes the others vote; intervening on \(D=\text{refuse}\) makes them refuse. The first hypothetical has much higher expected utility, so A-FDT votes. CDT, by contrast, treats each individual vote as causally ineffective and refuses.

---

## 7. Policies versus actions

Equation (4') quantifies over actions. The source, however, notes that the authors’ preferred formulation often evaluates *policies*, mappings from observations to actions, rather than single actions. This matters in sequential and multi-agent problems.

An action-level A-FDT agent asks:

\[
\text{What should } \fdt(P,G,x) \text{ output now?}
\]

A policy-level A-FDT agent asks:

\[
\text{What policy } \pi : \mathcal X \to \mathcal A
\text{ should this decision procedure implement?}
\]

A policy-level version might be written schematically as

\[
\mathrm{A\mbox{-}FDT}_{\Pi}(P,G)
=
\arg\max_{\pi \in \Pi}
\mathbb E\!\left[
V \mid \Do(\Pi=\pi)
\right],
\]

where \(\Pi\) represents the policy selected by the decision function.

The source does not make this policy formulation the primary one for Equation (4), so I treat it as a natural extension rather than the assigned formal core. In many cases, action-level A-FDT can emulate policy reasoning by including observation-specific decision variables such as \(D_{\text{full}}\), \(D_{\text{empty}}\), \(D_{\text{city}}\), and so on. But for repeated decisions and strategic interactions, policy-level A-FDT is often conceptually cleaner.

---

## 8. What the source settles and what requires extra assumptions

The source gives a compelling informal motivation for A-FDT and a precise-looking equation in Equation (4). It also shows how A-FDT behaves in many classic problems: one-boxing in Newcomb’s problem, smoking in the smoking lesion problem, paying in Parfit’s hitchhiker problem, one-boxing in transparent Newcomb, and refusing certain blackmail payments.

However, several important implementation details are not fully settled by the source.

### 8.1 Constructing \(G\)

The largest open problem, acknowledged by the source, is how to construct the graph \(G\) that encodes subjunctive dependencies. CDT can appeal to Pearl’s account of causal inference; A-FDT lacks an equally developed account of how to infer logical, mathematical, and computational dependencies from observation and experiment.

Equation (4') is therefore conditional: it tells us what A-FDT does given a correct dependency graph. It does not yet tell us how to obtain that graph in general.

My operational proposal is to treat \(G\) as a structural model of decision-relevant dependencies, using the predictor/lesion distinction as a guide. If a process depends on the agent’s decision function through prediction, simulation, copying, or symmetric reasoning, connect it to the appropriate decision-function variable. If it is merely correlated by a non-predictive common cause, do not. This is not a complete formal foundation, but it recovers the source’s examples and gives a usable method for unfamiliar cases.

### 8.2 Counterpossible reasoning

A-FDT requires evaluating scenarios where a deterministic computation has a different output than it actually has. The source admits that we lack a satisfactory general account of counterpossible conditionals. It argues that this is a technical rather than philosophical problem, because humans can reason under logical uncertainty.

For practical purposes, one can treat A-FDT’s interventions as modeling tools: we are not asking whether the actual computation literally changes, but which possible worlds are relevantly similar when the decision function’s output varies. The graph \(G\) supplies the similarity structure. This is an additional interpretive assumption, but it is consistent with the source’s use of graphical models.

### 8.3 Observations and conditioning

Equation (4') does not condition explicitly on \(\Obs=x\), whereas the CDT equation does. The source says A-FDT responds to observation by changing the node intervened upon. In transparent Newcomb, however, the discussion sometimes sounds as if the agent both intervenes on an observation-indexed node and conditions on the observation.

A coherent operational reading is this: the observation \(x\) is an input to the decision function, so the relevant intervention is on \(D_x\). One should not additionally hold fixed all observed facts when those facts are themselves counterfactually dependent on \(D_x\). This allows A-FDT to imagine that if its decision function output two-box in transparent Newcomb, it probably would not have seen a full box. If an observation is genuinely exogenous evidence about variables not affected by the decision function, then one may update \(P\) on that observation before defining \(D_x\). The source does not give a final formal rule here, so this reading is my own reconstruction.

### 8.4 Bounded agents and self-models

Equation (4') assumes the agent has a model containing an accurate representation of its own decision procedure. Real agents are bounded and cannot perfectly model themselves. The source’s examples are idealized. A practical A-FDT agent would use approximate self-models, approximate dependency graphs, and tractable approximations to the expectation. The source suggests that bounded approximations to A-FDT should still differ in characteristic ways from bounded EDT and bounded CDT, but it does not provide a bounded algorithm.

---

## 9. Why A-FDT’s counterfactuals are distinctive

A-FDT can be understood as occupying a middle ground between EDT and CDT.

EDT respects too many correlations. It conditions on the action, so any variable statistically correlated with the action becomes decision-relevant. This causes EDT to refrain from smoking in the smoking lesion problem and to pay in certain blackmail problems, because the action is treated as news.

CDT respects too few correlations. It intervenes on the physical action and severs correlations with predictors, twins, and simulations. This causes CDT to two-box in Newcomb’s problem, refuse in Parfit’s hitchhiker problem, and behave unstably in Death in Damascus-style problems.

A-FDT preserves correlations that arise from shared computation or accurate prediction, while breaking merely evidential correlations that do not reflect subjunctive dependence. In Newcomb’s problem, the predictor depends on the agent’s decision function, so A-FDT preserves the correlation. In the smoking lesion problem, the lesion does not depend on the agent’s decision function, so A-FDT does not preserve the correlation.

The source also argues that A-FDT has its own notion of dominance. CDT says two-boxing dominates one-boxing if one holds the predictor’s prediction fixed while changing the physical action. A-FDT says this is the wrong holding-fixed policy. If we hold fixed the subjunctive dependency between decision function and predictor, then switching from one-boxing to two-boxing makes the agent worse off. Dominance is therefore not a neutral argument for CDT; every way of constructing hypotheticals induces its own dominance notion.

---

## 10. Conclusion

A-FDT is an expected utility theory that evaluates actions by intervening on the output of the agent’s own decision function. Its core rule, given by Equation (4) of the source, is:

\[
\mathrm{A\mbox{-}FDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb E\!\left[
V \mid
\Do\!\left(
\fdt(\underline P,\underline G,\underline x)=a
\right)
\right].
\]

The theory’s central philosophical claim is that rational action should be understood as choosing the best output of a fixed mathematical decision procedure. This lets A-FDT handle predictors, twins, transparent boxes, hitchhiking drivers, and blackmail scenarios by preserving decision-relevant subjunctive dependencies while avoiding EDT’s news-management and CDT’s overly local causal interventions.

The main unresolved issue is the construction of the dependency graph \(G\). The source gives the decision rule conditional on such a graph but leaves open how to infer subjunctive dependencies in general. A reasonable operational approach is to model predictors, copies, simulations, and symmetric reasoners as descendants of the relevant decision-function variable, while treating merely statistical common causes as independent of that variable. With that supplement, A-FDT becomes a usable, if idealized, procedure for deciding unfamiliar cases.

---

## References

Gibbard, A., and Harper, W. L. (1978). Counterfactuals and two kinds of expected utility. In *Foundations and Applications of Decision Theory*.

Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.

Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.

Yudkowsky, E., and Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060.