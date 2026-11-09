# Action Functional Decision Theory: Choosing the Output of Your Own Function

## 1. Introduction

This essay explains **action functional decision theory**, which I will call **A-FDT** throughout. The theory is drawn from Yudkowsky and Soares’s “Functional Decision Theory: A New Theory of Instrumental Rationality.” The source calls the theory “functional decision theory”; here I use **A-FDT** to emphasize the action-level formalization given in Equation (4) of Section 5, which is the primary formal presentation for this essay.

The guiding idea is simple to state but radical in its implications. A rational agent should treat her decision as the output of a fixed mathematical function and ask:

> “Which output of this very function would yield the best outcome?”

This differs from the questions associated with the two standard theories:

- **Evidential decision theory**, or **EDT**, asks which action would be the best news to learn one had taken.
- **Causal decision theory**, or **CDT**, asks which physical intervention on one’s own action would cause the best outcome.
- **A-FDT** asks which output of the agent’s decision procedure, considered as a mathematical object, would produce the best world when all relevant dependencies are respected.

The source motivates A-FDT by its performance in predictive and game-theoretic dilemmas: it one-boxes in Newcomb’s problem, smokes in the smoking lesion problem, pays in Parfit’s hitchhiker problem, and resists certain forms of blackmail. My aim here is to explain the formal rule, how to apply it, what it says about counterfactuals, and where the source leaves important implementation questions open.

---

## 2. The formal core of A-FDT

All three theories discussed in the source are expected utility theories. Given a countable set of outcomes \(o_1,o_2,\ldots\), a finite action set \(\mathcal A\), an observation history \(x\), and a bounded utility function \(\mathcal U\), expected utility has the generic form

\[
\mathcal{EU}(a) = \sum_j P(a \then o_j; x)\,\mathcal U(o_j),
\]

where the theories disagree about the meaning of the decision hypothetical \(a \then o_j\).

EDT interprets this hypothetical as ordinary Bayesian conditioning:

\[
\mathrm{EDT}(P,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E\!\left[V \mid \Obs=x,\Act=a\right],
\]

where \(V\) is the utility-valued random variable \(\mathcal U(\Outcome)\).

CDT interprets the hypothetical as a causal intervention on the physical action:

\[
\mathrm{CDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E\!\left[V \mid \Do(\Act=a),\Obs=x\right].
\]

Here \(G\) is a causal graph, and \(\Do(\Act=a)\) is Pearl’s intervention operator: set \(\Act=a\), leave non-descendants fixed, and propagate the change through causal descendants.

Equation (4) of the source gives the corresponding rule for functional decision theory. Renaming the theory as **A-FDT**, while keeping the source’s internal notation for the decision-function variable, the rule is:

\[
\boxed{
\mathrm{A\text{-}FDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E\!\left[
V \mid
\Do\!\left(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\right)
\right].
}
\]

Let

\[
D_x := \mathrm{fdt}(\underline P,\underline G,\underline x)
\]

abbreviate the model variable representing the output of the agent’s own decision procedure when run on inputs \(P,G,x\). Then the rule is simply:

\[
\mathrm{A\text{-}FDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E\!\left[V \mid \Do(D_x=a)\right].
\]

The underlines in the source indicate “dequoting”: the variable’s name depends on the model and inputs. The agent does not need to know the actual value of \(D_x\) in order to have a variable representing it. The source mentions Kleene’s recursion theorem and quining as one way to make such self-reference harmless.

The essential difference from CDT is this:

- CDT intervenes on \(\Act\), a physical action variable.
- A-FDT intervenes on \(D_x\), a logical or computational variable representing the output of the agent’s decision function.

The graph \(G\) is not merely a causal graph. It must encode what the source calls **subjunctive dependencies**: facts about how changing the output of the decision function would change predictions, copies, twins, simulations, and other variables that depend on that function’s output. Given such a graph, A-FDT reuses Pearl-style intervention semantics, but applies them to a logical node rather than a purely physical one.

---

## 3. Subjunctive dependence and counterfactuals

A-FDT’s behavior depends on distinguishing three kinds of relationship between an agent’s action and the world.

### 3.1 Causal dependence

A variable \(Y\) causally depends on the agent’s action if changing the action changes \(Y\) through an ordinary causal pathway. If I push a cup off a table, the cup falls. CDT tracks these dependencies.

### 3.2 Statistical or evidential dependence

A variable \(Y\) may be statistically correlated with an action without being caused by it. The smoking lesion problem is the canonical example: a lesion causes both a preference for smoking and lung cancer, but smoking itself does not cause cancer in the imagined world. EDT treats this correlation as decision-relevant because conditioning on smoking is bad news about cancer. CDT and A-FDT both reject this as a reason to refrain.

### 3.3 Subjunctive dependence

The source introduces **subjunctive dependence** to describe the relationship between systems whose behavior depends on the same mathematical function. Two calculators computing \(6288+1048\) on opposite sides of the world are not causally connected, but their outputs are linked by the arithmetic function they both compute. If one outputs \(7336\), we should expect the other to output \(7336\) as well, assuming both are functioning correctly.

Similarly, if a predictor has an accurate model of an agent’s decision procedure, the predictor’s prediction is subjunctively dependent on the output of that decision procedure. The predictor is not necessarily computing the exact same algorithm, but it is tracking the output of the agent’s algorithm.

A-FDT treats subjunctive dependence as decision-relevant. The source summarizes the relation by saying that functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.

This means that A-FDT counterfactuals are not ordinary possible-world counterfactuals. If the agent’s decision function actually outputs \(a^\ast\), then the hypothesis \(D_x=a\) for \(a\neq a^\ast\) is, strictly speaking, a **counterpossible**: it runs contrary to mathematical fact. The source acknowledges that this is technically difficult but argues that humans already reason in this way when we ask how a predictor would have predicted if our algorithm had behaved differently.

For practical purposes, A-FDT assumes that the pair \((P,G)\) already supplies a way to evaluate such counterpossible hypotheticals.

---

## 4. How A-FDT evaluates an action

A reader who wants to apply A-FDT to a new problem can use the following procedure.

### Step 1: Build a probabilistic model \(P\)

Construct a probability distribution over relevant variables: states of the world, predictions, observations, actions, outcomes, and utility. The model should also include variables for logical or computational outputs, especially the output of the agent’s own decision procedure.

### Step 2: Build a dependency graph \(G\)

The graph says how variables change under intervention. It should include not only causal arrows but also arrows representing subjunctive dependence.

A natural heuristic, though not fully formalized in the source, is:

- Draw an arrow from \(D_x\) to the agent’s physical action, because the action is produced by the decision procedure.
- Draw arrows from \(D_x\) to predictors’ predictions when those predictors are modeling the agent’s decision procedure.
- Draw arrows from \(D_x\) to the behavior of twins, copies, simulations, or other agents using the same reasoning.
- Do **not** draw arrows from \(D_x\) to variables that are merely statistically correlated with the action, such as lesions, exogenous diseases, or unrelated states of nature.

The source explicitly says that constructing this graph from observation and experiment is the largest open problem for functional decision theory. Thus, the above heuristic should be understood as an operational gloss, not as a theorem of the paper.

### Step 3: Identify the current decision node

Given the actual observation history \(x\), identify the variable

\[
D_x = \mathrm{fdt}(\underline P,\underline G,\underline x).
\]

This is the node on which A-FDT intervenes.

### Step 4: Intervene on each possible output

For each candidate action \(a\in\mathcal A\), form the hypothetical distribution

\[
P_a(\cdot) = P(\cdot \mid \Do(D_x=a)).
\]

This means: set the output of the decision function to \(a\), then propagate that change through all variables that \(G\) says depend on it.

### Step 5: Compute expected utility and choose

Compute

\[
\mathrm{EU}_{\mathrm{A\text{-}FDT}}(a)
=
\mathbb E[V \mid \Do(D_x=a)].
\]

Choose an action maximizing this quantity.

This is the basic operational recipe.

---

## 5. Example: Newcomb’s problem

In Newcomb’s problem, a predictor has placed \$1,000,000 in box B iff she predicted the agent would one-box. Box A transparently contains \$1,000. The agent may take both boxes or only box B.

Let the actions be:

\[
\mathcal A = \{\text{one-box}, \text{two-box}\}.
\]

Let \(D\) represent the output of the agent’s decision procedure. The predictor is 99% accurate. The graph contains the following subjunctive dependencies:

\[
D \rightarrow \Act,
\]
\[
D \rightarrow \Var{Prediction},
\]
\[
\Var{Prediction} \rightarrow \Var{Box B}.
\]

Under the intervention \(\Do(D=\text{one-box})\), the agent one-boxes and the predictor almost certainly predicted one-boxing. Thus:

\[
P(\Var{Box B}=\text{full} \mid \Do(D=\text{one-box})) \approx 0.99.
\]

The expected utility is approximately:

\[
0.99 \times 1{,}000{,}000
+
0.01 \times 0
=
990{,}000.
\]

Under the intervention \(\Do(D=\text{two-box})\), the agent two-boxes and the predictor almost certainly predicted two-boxing. Thus:

\[
P(\Var{Box B}=\text{full} \mid \Do(D=\text{two-box})) \approx 0.01.
\]

The expected utility is approximately:

\[
0.01 \times 1{,}001{,}000
+
0.99 \times 1{,}000
=
11{,}000.
\]

Therefore A-FDT one-boxes.

CDT two-boxes because it intervenes directly on \(\Act\), holding the predictor’s prior prediction fixed. EDT also one-boxes, but for a different reason: it conditions on the action as evidence. A-FDT one-boxes because the predictor’s prediction is subjunctively dependent on the same decision function whose output is being evaluated.

---

## 6. Example: the smoking lesion problem

In the smoking lesion problem, a lesion causes both a desire to smoke and a high probability of lung cancer. Smoking does not causally affect cancer. Smoking gives \$1,000 worth of utility. Avoiding cancer is worth \$1,000,000.

The crucial modeling fact is that the lesion is not subjunctively dependent on the agent’s decision function. The lesion is a common cause of smoking and cancer, but it does not compute, predict, or simulate the agent’s decision procedure.

So the graph should include something like:

\[
\Var{Lesion} \rightarrow \Act,
\]
\[
\Var{Lesion} \rightarrow \Var{Cancer},
\]
\[
D_x \rightarrow \Act,
\]

but not:

\[
D_x \rightarrow \Var{Lesion},
\]
\[
D_x \rightarrow \Var{Cancer}.
\]

When A-FDT evaluates \(\Do(D_x=\text{smoke})\) versus \(\Do(D_x=\text{refrain})\), the probability of having the lesion remains fixed. Therefore the probability of cancer remains fixed across the two hypotheticals, except insofar as it is already determined by the lesion. Smoking simply adds the \$1,000 utility.

In a simplified model where the same decision procedure certainly controls the action, the expected utilities are:

\[
\mathrm{EU}(\text{smoke})
=
1000
+
\mathrm{EU}(\text{refrain}).
\]

So A-FDT smokes.

The source gives a more careful formalization because the lesion may also affect the agent’s preferences. It introduces two possible utility functions and therefore two possible decision-function variables, one for each preference state. Even in that more careful model, the intervention on the relevant decision-function variable does not change the probability of the lesion, and A-FDT still smokes.

This example shows why A-FDT is not simply EDT. A-FDT does not treat the action as evidence about the lesion in the decision hypothetical. It holds fixed variables that are not downstream of the decision function.

---

## 7. Example: transparent Newcomb and Parfit’s hitchhiker

The treatment of observation-dependent cases is one of the most interesting and subtle parts of A-FDT.

In the transparent Newcomb problem, both boxes are visible. The predictor filled box B iff she predicted that the agent would one-box upon seeing that both boxes are full. If the agent sees that box B is full, should she one-box or two-box?

CDT says two-box: given that box B is full, taking box A adds \$1,000.

EDT also says two-box: conditional on seeing box B full, taking both boxes is better news.

A-FDT says one-box.

The reason is that A-FDT does not respond to the observation by simply conditioning on it. Instead, it changes the node on which it intervenes. Upon seeing a full box, the relevant variable is not merely \(D\), but something like

\[
D_{\text{full}}
=
\mathrm{fdt}(\underline P,\underline G,\Val{full}),
\]

the output of the decision procedure when given the observation “full.”

The predictor’s earlier prediction determines whether the agent sees a full box or an empty box. In the hypothetical where \(D_{\text{full}}\) outputs “two-box,” the predictor would probably have predicted two-boxing, and box B would probably be empty. Thus, even though the agent actually sees a full box, A-FDT evaluates the two-boxing hypothetical as one in which the predictor likely did not fill the box.

Roughly:

\[
\mathbb E[V \mid \Do(D_{\text{full}}=\text{one-box})]
\approx
990{,}000,
\]

while

\[
\mathbb E[V \mid \Do(D_{\text{full}}=\text{two-box})]
\approx
11{,}000.
\]

So A-FDT one-boxes even when it sees that box B is full.

The source emphasizes that this is equivalent to Parfit’s hitchhiker problem. A driver will rescue you only if she predicts that you will pay \$1,000 after being rescued. Once in the city, CDT and EDT refuse to pay, because payment no longer causally or evidentially helps. A-FDT pays, because the driver’s earlier prediction is subjunctively dependent on the output of the decision procedure the agent will use upon arriving in the city.

In slogan form: A-FDT acts as it would have wanted to precommit to act, without needing an actual precommitment device.

---

## 8. Observation: what A-FDT does and does not condition on

Equation (4) has an important feature: the observation \(x\) appears as part of the decision-function variable \(D_x\), not as an explicit Bayesian condition inside the expectation:

\[
\mathbb E[V \mid \Do(D_x=a)].
\]

The source says that when CDT’s observation history changes from \(x\) to \(y\), CDT changes its conditioning from \(\Obs=x\) to \(\Obs=y\). A-FDT instead changes the intervention node from \(D_x\) to \(D_y\).

This is central to A-FDT’s behavior in transparent Newcomb and blackmail-style problems. If the agent conditioned on the observation while also intervening on the decision node, it could end up forcing an inconsistent or misleading hypothetical. For example, conditioning on “box B is full” while asking what would happen if the full-box decision procedure two-boxed would obscure the fact that a reliable predictor would not have filled the box if it had predicted two-boxing.

However, the source is not perfectly explicit about all implementation details. In some later discussions it appears to combine the intervention with an observation condition, and there is a tension between treating observations as fixed evidence and treating them as downstream of predictions. My preferred operational interpretation is this:

1. If an observation is genuinely exogenous—meaning it does not depend on the agent’s decision procedure or on predictors of it—then it may be treated as background evidence in \(P\), or as an input that simply selects the decision node.
2. If an observation is endogenous—meaning the agent receives it only because a predictor predicted some behavior—then A-FDT should not rigidly condition on it in a way that breaks the predictor-agent dependency. Instead, the observation should be represented in the graph as possibly affected by the policy or decision function being evaluated.

This distinction is not fully formalized in the source, but it follows naturally from the source’s treatment of transparent Newcomb and blackmail.

---

## 9. Actions versus policies

Equation (4) evaluates individual actions. The source notes, however, that the authors’ preferred formulation uses policies: mappings from observations to actions. This matters in multi-agent or sequential settings where one decision procedure must specify behavior at many possible observation histories.

A policy-level version of A-FDT can be written as:

\[
\mathrm{A\text{-}FDT}_{\Pi}(P,G)
=
\arg\max_{\pi\in\Pi}
\mathbb E[V \mid \Do(\Pi=\pi)],
\]

where \(\Pi\) is a variable representing the agent’s policy, and \(\pi\) maps observations to actions. The agent then executes \(\pi(x)\) at the actual observation \(x\).

This policy formulation is not the primary equation assigned here, but it is a natural extension of Equation (4). It clarifies cases where evaluating a single action at a single observation seems strange. For example, in mechanical blackmail, if an agent receives a blackmail letter, A-FDT may refuse to pay because the hypothetical in which the policy refuses is a hypothetical in which the blackmailer predicts refusal and does not send the letter. The actual observation of the letter may be the result of a rare predictor error, but A-FDT still chooses the policy that makes blackmail unprofitable in expectation.

I regard the policy formulation as the cleanest way to apply the spirit of A-FDT to unfamiliar sequential cases. But it should be distinguished from the strict action-level rule in Equation (4).

---

## 10. Blackmail and the value of being predictable

A-FDT’s treatment of blackmail follows the same logic. In XOR blackmail, a predictor sends a letter iff exactly one of two conditions holds: the agent will pay and there are no termites, or the agent will refuse and there are termites. Upon receiving the letter, EDT pays because paying is good news about the absence of termites. CDT refuses because termites are causally upstream. A-FDT also refuses, but for a different reason.

If the agent’s decision procedure, upon receiving the letter, pays, then the predictor predicted payment and sent the letter. If the agent’s procedure refuses, then the predictor predicted refusal and did not send the letter, assuming perfect prediction. The payment hypothetical is therefore a hypothetical in which one is blackmailed; the refusal hypothetical is one in which one is not blackmailed. Refusal has better global consequences.

This illustrates a general theme: A-FDT chooses the output that makes the agent the kind of agent whom it is not profitable to exploit. It does not need to bind itself in advance. Its decision rule already has the favorable disposition.

---

## 11. Dominance and the global perspective

CDT often appeals to dominance: two-boxing dominates one-boxing in Newcomb’s problem because, holding the box contents fixed, taking both boxes yields more money.

The source rejects this argument because it assumes CDT-style counterfactuals. If we hold fixed the predictor’s accuracy and the subjunctive dependence between decision function and prediction, then switching from one-boxing to two-boxing does not improve the outcome. Instead, it makes the predictor leave box B empty.

A-FDT therefore has its own dominance principle: an action dominates another if, holding fixed all relevant subjunctive dependencies, switching the output of the decision function from one to the other never worsens and sometimes improves the outcome. This is not a neutral criterion independent of counterfactual semantics, but neither is CDT’s dominance principle. The source argues that we should compare decision theories mainly by expected utility achieved, not by dominance relative to a contested notion of counterfactual.

This connects to the “global perspective” described in the source. A-FDT asks what the entire world would look like if the decision function had a different output. It does not restrict attention to the causal downstream effects of a physical movement. If that means imagining a world in which one sees different evidence or receives different messages, A-FDT accepts that consequence.

---

## 12. Open problems and interpretive uncertainties

The source is candid that A-FDT rests on unfinished foundations. The most important open problems are these.

### 12.1 Constructing \(G\)

Equation (4) assumes a graph \(G\) that tells us how changing a logical variable affects other variables. For CDT, Pearl’s causal inference program gives a developed account of how causal structure can be learned from observation and experiment. No comparable general account exists for subjunctive or logical dependence.

In practice, applying A-FDT requires modeling judgment. One must decide which predictors, copies, simulations, or other agents are tied to the agent’s decision procedure. The source’s examples make this intuitive, but a fully general method is missing.

### 12.2 Counterpossible probabilities

A-FDT must assign probabilities to scenarios in which a mathematical function has a different output than it actually has. This requires some account of reasoning under logical uncertainty. The source says this is a technical rather than philosophical problem and points to human mathematicians as proof that such reasoning is possible in rough form. Still, no complete formal account is supplied.

### 12.3 Observation handling

Equation (4) selects the intervention node using the observation \(x\), but it does not explicitly condition on \(x\). The source’s examples suggest that this is intentional, especially in endogenous-observation cases. Yet the exact boundary between exogenous observations that should be treated as fixed evidence and endogenous observations that should remain subject to counterfactual variation is not fully specified.

My proposed operational rule is to model endogenous observations as downstream of the policy or decision function wherever predictors control what the agent sees. For exogenous observations, one may condition in the background model. This is a reasonable extension, but it is not fully determined by Equation (4) alone.

### 12.4 Fairness

The source claims A-FDT performs best in “fair” dilemmas, where the environment rewards or punishes the agent based on predictions of her behavior rather than punishing her for using a particular decision procedure. It admits that no decision theory can win in every possible environment. One can always construct a problem that punishes A-FDT specifically. This limitation is not unique to A-FDT.

---

## 13. Conclusion

Action functional decision theory evaluates choices by intervening on a variable representing the output of the agent’s own decision function. Its central equation is:

\[
\mathrm{A\text{-}FDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E[V \mid \Do(D_x=a)].
\]

This simple change—intervening on the decision function rather than on the physical act—allows A-FDT to preserve dependencies that CDT discards and to discard correlations that EDT mistakenly preserves.

In Newcomb’s problem, A-FDT one-boxes because the predictor’s prediction depends on the same decision function. In the smoking lesion problem, it smokes because the lesion is merely a common cause, not a subjunctive dependent. In transparent Newcomb and Parfit’s hitchhiker, it chooses the action it would have wanted to precommit to, even when the favorable outcome has already been secured. In blackmail problems, it refuses payments that would make exploitation profitable.

The theory is elegant, but its implementation depends on difficult unresolved questions about logical dependence, counterpossible reasoning, and the construction of dependency graphs. The source provides powerful examples and a compelling normative picture, but not yet a complete formal foundation. Still, as a rule for deciding unfamiliar cases, A-FDT gives a clear directive: identify the decision procedure you are running, identify the variables whose behavior depends on its output, and choose the output that, when consistently imagined across all those dependencies, produces the best world.

---

## References

Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.

Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.

Yudkowsky, E., and Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060.