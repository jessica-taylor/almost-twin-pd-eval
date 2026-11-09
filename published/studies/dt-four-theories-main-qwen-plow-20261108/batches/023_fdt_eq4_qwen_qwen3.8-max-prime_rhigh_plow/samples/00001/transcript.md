# 023_fdt_eq4_qwen_qwen3.8-max-prime_rhigh_plow / 00001

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/f85832bd-2a7d-469c-9547-3a6aa1abaaa4/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/f85832bd-2a7d-469c-9547-3a6aa1abaaa4/call_0/response.raw) · finish: `stop`

### Visible response

```text
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
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request: write substantive mathematical essay 2400-3000 words explaining A-FDT, taking Equation (4), Section 5 of supplied paper as primary formal presentation. Need use A-FDT consistently as assigned decision theory's name, including headings/examples, identify other decision theories by distinct names. Keep quotations faithful. Explain best mathematical understanding and application. Where implementation details not determined, explain what follows from source and what requires assumptions. Need distinguish source claims vs own proposals. Target approx 2400-3000 words including references and any material. Need finish brief conclusion. Need likely no citations exhaustive, but references maybe source. Need write essay, not answer case. Need include equations. Need be careful: The source theory is FDT, but user asks A-FDT (action functional decision theory). Need rename consistently. Need perhaps say A-FDT is my name for the action-level formalization in Eq (4), while source calls it FDT. But they require use A-FDT consistently as assigned decision theory's name. Need maybe avoid calling it FDT except when quoting/source? We can say source calls it functional decision theory; in this essay I call the action-intervention version A-FDT. Need note source footnote preferred policies but Eq (4) action-level. Need define Equation (4): FDT(P,G,obs)=argmax_a E(V | do(fdt(underline P, underline G, underline x)=a)). We'll adapt to A-FDT notation: A-FDT(P,G,x) := argmax_{a∈A} E[V | Do(FDTvar(underline P, underline G, underline x)=a)]. Need maybe preserve source quote? Could use \mathrm{FDT} in equation? But A-FDT name. We can define variable D or A-FDT? Need keep faithful: source equation uses FDT. We can write "in the source's notation, Equation (4) is..." then present adapted A-FDT equation. Quotations faithful if quote snippets. Need not quote too much.

Need explain EDT and CDT briefly for contrast: EDT Eq (2): argmax E[V | Obs=x, Act=a]; CDT Eq (3): argmax E[V | Do(Act=a), Obs=x]. A-FDT intervenes on logical variable representing output of decision function given model, graph, observations. Observations: A-FDT responds by changing intervention node rather than conditioning? Actually source: CDT responds to observation by Bayesian conditionalization; FDT responds by changing which node it intervenes upon. Need mention maybe model includes observation variable? Equation (4) does not condition on obs inside expectation? Source Eq (4): E(V | Do(FDTvar(underline P, underline G, underline x)=a)). No Obs=x conditioning. In transparent Newcomb they write E(V | Do(FDTpgv{full}=a, Obs=full)? There's a possible inconsistency? Let's inspect: Equation (4) in source:
\FDT(P, G, \obs) \coloneqq \argmax_{\act \in \mathcal A} \EE\left(\VV \cond \Do\left(\FDTvar(\underline P,\underline G,\underline x)= \act\right)\right).
There is no conditioning on Obs=x. Text says where CDT responds to observation by Bayesian conditionalization, FDT responds by changing which node it intervenes upon. Later transparent: evaluate FDT(Pf,Gf,full), involves maximizing E(V | Do(FDTpgv{full}=a, Obs=full). They include Obs=full? They wrote:
\[
  \EE(\VV \mid \Do(\FDTpgv{full}=\act, \Obs=\Val{full}).
\]
Missing closing paren maybe. This may be source inconsistency. Need explain uncertainty and operational interpretation. The assignment says take Eq (4), Section 5 as primary formal presentation. Need where source leaves open, explain uncertainty and if reasonable operational interpretation available develop/justify. Need distinguish source claims vs own assumptions.

Important: Need discuss how A-FDT evaluates alternative actions/policies and treats dependencies/counterfactuals. Need maybe discuss policies: source footnote says preferred formalization iterates over policies, but Eq (4) actions; A-FDT perhaps action functional. Need maybe explain action-level vs policy-level. Since assigned name action functional decision theory, we can focus on actions. But need explain evaluating policies? User says how theory evaluates alternative actions or policies. We can say Eq (4) evaluates actions; a policy-level extension would choose policy π by intervening on variable for policy output; source notes preferred formulation but not needed in paper. For A-FDT as assigned, action is output. If sequential decisions, need additional assumption to evaluate policies: choose policy π, intervention on variable A-FDT(P,G,x)=π(x) or on policy variable. Need develop operational interpretation.

Need include examples: Newcomb, Smoking lesion, Transparent Newcomb, maybe Parfit's hitchhiker, XOR blackmail? Need target 2400-3000 words, so can include 2-3 examples with calculations. Need maybe 2600 words. Need avoid lengthy bibliography. References maybe one or two. Need include conclusion.

Need be precise enough reader could use essay to decide unfamiliar cases. Need lay out procedure:
1. Build world-model P: probability distribution over variables including logical variables for outputs of relevant functions, observations, actions, outcomes, utility.
2. Build dependency graph G encoding how variables would change under interventions, including causal and subjunctive/logical dependencies. In source, G is given; constructing G is open.
3. Identify current observation x and the decision-function variable D_x = A-FDT(underline P, underline G, underline x), representing output of the agent's actual decision procedure on those inputs.
4. For each candidate action a, form hypothetical P_a by intervention Do(D_x=a): set D_x to a, propagate through G to downstream variables (including Action, predictors' predictions, possibly observations in counterfactual). Compute expected utility E_a[V].
5. Choose action maximizing expected utility.
Need note self-reference via quining; variable represents output, not need know value. Need note counterpossible reasoning: if actual D_x output is a*, hypotheticals for other a are counterpossible; G tells how to imagine.

Need explain dependencies: subjunctive dependence: systems computing same function or predictions thereof; not mere statistical correlation. A-FDT preserves correlations that depend on decision function output; breaks correlations not downstream/subjunctively dependent? Actually do surgery on logical variable; G determines which variables change. In Newcomb, predictor's prediction and action both downstream of D, so change together. Lesion not downstream of D, so fixed.

Need address observation treatment. Equation (4) uses x to select node but not condition. This implies "updateless" flavor: when imagining different output at current observation, one does not additionally condition on having observed x? But x is built into node. However if observation is known with certainty, maybe intervention node includes that observation, and G can represent that observation depends on predictor, so counterfactual action may imply different observation. In transparent Newcomb, seeing full box, A-FDT intervenes on D_full. The hypothetical where D_full=two-box can imply predictor predicted two-box, box empty, so agent would not actually be running D_full? Source says if procedure outputs two-box, box likely empty and my brain does not implement this procedure (because shown empty box). Yet they still evaluate D_full. Need explain: The decision procedure indexed by observation is the one the agent would run upon that observation. Even if counterfactual output makes observation unlikely/impossible, A-FDT evaluates output of that very function because predictors responded to it. It chooses policy at the point where predictor's prediction selects observation. Need make operational.

Potential issue: Equation (4) no conditioning on Obs=x; but if we're actually at x, shouldn't we condition? Source's approach: no, because conditioning would make counterfactuals collapse in transparent Newcomb? They condition for Carl/Eve but Fiona changes intervention node. In transparent example they wrote with Obs=full maybe accidental. Need discuss open question: should A-FDT condition on x as background evidence? Source says no: observation changes intervention node, not Bayesian conditionalization. But if x contains information not relevant to decision-function dependencies (e.g. exogenous news), how handle? Need propose operational interpretation: Treat x as input to decision function; include all evidential updates in P before forming D_x? Wait P is model perhaps already updated on x? The variable D_x includes x as input; if P is updated on x, then expectation may be conditional implicitly? Need parse. Source: EDT(P,x), CDT(P,G,x) condition on Obs=x. FDT(P,G,x) intervenes on fdt(P,G,x). It might not condition because P itself may be prior? But x appears as input. They say when CDT's observation history updates from x to y, CDT changes conditioning; FDT changes node. So P,G remain same? In Eq (4), no conditioning. This is updateless. In simple problems where observations are exogenous and not affected by decision function, this could cause issues? Need explore. If agent observes a coin flip unrelated to decision, should action depend on it? Suppose P has Obs = coin, action choice with utilities depending on coin. A-FDT would choose D_x for observed x; expected utility under Do(D_x=a) maybe includes uncertainty over Obs? If no conditioning, it may average over other observations, but D_x only controls action when Obs=x? The graph needs an observation-selection mechanism: Act depends on D_x only if Obs=x? The source's transparent graphs have Act depend on multiple D_obs variables and Prediction chooses which D controls Act. So in general, P/G must encode that the current action is controlled by the decision function corresponding to the actual observation; under interventions on D_x, variables may change such that Obs may not equal x. If we want evaluate actual decision given observed x, perhaps need condition on the event that the agent's decision process is D_x? Hmm.

Need maybe propose a clean operational semantics: Define policy π maps observations to actions. The A-FDT action-level equation can be seen as choosing the value of π(x) while holding the rest of policy fixed? Source footnote says preferred policies. For unfamiliar cases, a policy-based A-FDT is clearer: Choose π to maximize E[V | Do(Π=π)] where Π is a logical variable representing the policy implemented by agent, and actual action is π(x). But assignment says Equation (4) primary; can say action-level A-FDT is local version: at observation x, intervene on D_x; if decisions are sequential or observations are endogenous, evaluate as policy by considering all D_y jointly or a policy variable. Need distinguish own extension.

Need maybe discuss constructing G: source says open problem; requires augmented info about logical/mathematical computational causal structure. Need offer practical heuristic: include arrows from D_x to all variables whose values are computed from or predicted from that output: agent's action, predictor predictions, messages sent, others using same algorithm; do not draw arrows to common causes or statistical correlates (lesions, exogenous states). For perfect predictor, arrow D_x -> Prediction -> Box; for lesion, Lesion -> Action and Cancer but no D -> Cancer. But source says in smoking lesion, action depends on lesion and two possible FDT variables due to preferences. Need simpler.

Need maybe include formal notation. Let's design essay structure:

Title: Action Functional Decision Theory: A Practical Exposition

1. Introduction: decision theories as expected utility with different hypothetical connective. Source's FDT, here A-FDT. Core question: "Which output of this very decision function would yield best outcome?" Quote maybe. A-FDT treats decision as output of fixed mathematical function. It differs from EDT and CDT.

2. Formal framework:
- Outcomes O, actions A, observations X, utility U, bounded.
- Expected utility Eq (1) maybe: EU(a)=∑ P(a ↝ o_j; x) U(o_j). Theories differ by interpretation of ↝.
- EDT: conditionalization.
- CDT: do(Act=a).
- A-FDT Equation (4): source quote/adapt:
A-FDT(P,G,x) = argmax_{a∈A} E_P[ V | Do(D_x=a) ], D_x := fdt(underline P, underline G, underline x).
Need mention underlines dequoting; variable name depends on model; self-reference via quining. If using source notation, fdt variable. Need maybe write 
\mathrm{A\text{-}FDT}(P,G,x) := \arg\max_a \mathbb E[V \mid \mathrm{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)].
- G encodes subjunctive dependency, not just causal. Do is Pearl-style surgery but on logical node. It sets D_x, propagates to all variables G marks downstream (logical, computational, causal, predictive). The expectation is taken in resulting hypothetical distribution.
- Observations: x selects intervention node. If observations change, A-FDT changes node rather than conditioning. This is source's claim. Need discuss ambiguity and my operational reading.

3. Constructing hypotheticals: subjunctive dependence.
- Define subjunctive dependence: two systems depend on same mathematical function; calculators example. Causal dependence is special case; mere statistical correlation not. A-FDT counterfactuals hold fixed all variables not downstream of D_x according to G, while varying those that are. It uses counterpossibles because D_x's output is logically fixed.
- Graph construction: source leaves open. Need propose operational heuristic: model all variables as functions of exogenous noise and logical variables; add arrows from decision-function outputs to any variable whose value is obtained by simulating, predicting, copying, or depending on that output. Include predictor's prediction, twin's action, blackmailer's prediction, future copies. Do not add arrows from D to lesions or exogenous states unless they literally compute from D. If preferences may depend on hidden state (lesion), include multiple decision-function variables as source does.
- Need note constructing G is not solved by paper; my heuristic is additional assumption.

4. Applying A-FDT step-by-step.
Maybe enumerated procedure.

5. Examples:
A. Newcomb's problem: Variables D, Act, Prediction, Box, Accurate. Priors: Accurate .99. G: D -> Act, D -> Prediction, Prediction -> Box, Act/Box -> V. Intervention D=one-box => Act=one-box, Prediction=one-box with .99, Box full .99; EU ≈ .99*1,000,000 = 990,000 (or plus? one-box no 1000). D=two-box => Box full .01; EU ≈ 0.01*1,001,000? Actually if two-box and box full get 1,001,000 with .01; if empty get 1,000 with .99 => 10,010+990=11,000. Choose one-box. CDT two-boxes because do(Act) leaves Box fixed; EDT one-boxes by conditioning. Need include enough.

B. Smoking lesion: Need explain A-FDT smokes. Graph: lesion affects action/preferences? Source complex with two utility functions. Simpler: lesion causes smoking and cancer, but decision function only controls action given preferences; cancer not downstream of D. Intervention on D=smoke changes Act but not Lesion/Cancer. EU(smoke) = EU(refrain)+ p*1000? Need present source's formula maybe. Use p probability lesion; cancer probabilities? Source values: smoking utility +1000; cancer fatal loses 1,000,000? In source: lesion cancer 99%, no lesion 1%; but their formula weird: p($10,000+$1,000)+(1-p)($990,000+q$1,000). Need maybe not dig. Simpler: cancer probability fixed by lesion prior; smoking adds 1000; choose smoke. Need ensure consistent with source: A-FDT doesn't let cancer vary with action because lesion not subjunctively dependent. Need note source's formalization includes uncertainty over whether D_S or D_R controls action; but key result unchanged.

C. Transparent Newcomb / Parfit's hitchhiker: A-FDT one-boxes when sees full. Need show observation handling. Graph includes D_full and D_empty; prediction determines which observation and which D controls action. Upon seeing full, A-FDT evaluates D_full. If D_full=one-box, predictor likely predicted one-box, box full, V=1M with .99; if predictor inaccurate, box empty and action controlled by D_empty maybe get small. If D_full=two-box, predictor likely predicted two-box, box empty, so actual observation would be empty; expected utility low. Thus choose one-box. This yields paying hitchhiker: if driver predicts pay in city, ride; if you would not pay, no ride. Need mention source claims this is equivalent.

Maybe also XOR/mechanical blackmail briefly: A-FDT refuses because paying implies predictor predicted pay and sent letter; refusing implies predictor predicted refuse and didn't send letter, so better global hypothetical. But maybe too many examples; word count. Could include one paragraph to show blackmail.

6. Policies and sequential decisions:
- Source footnote: preferred formalization chooses policies rather than actions. A-FDT can be extended: let Π be variable for policy mapping observations to actions; choose π maximizing E[V | Do(Π=π)]. Then action at x is π(x). This resolves cases where counterfactual output at x would alter observation; the agent chooses what to do at all observations. This is my addition / clarification; source says action vs policy not matter in paper except multi-agent. Need explain for unfamiliar cases: If problem has multiple possible observations or actions after information, specify policy; A-FDT intervention on policy variable preserves dependencies across all predicted behaviors. If only one action, Eq (4) suffices.
- Need maybe discuss alternative actions/policies: For policy π, define hypothetical where Π=π; predictors predict π's outputs; outcomes computed. Choose π. If bounded, approximate.

7. Open questions and uncertainties:
- Constructing G / subjunctive dependencies from observation is open; source admits. Need operational interpretation: use structural equations with logical variables; but no general formal method. Need counterpossible probabilities: need probability distribution over logical counterfactuals; source assumes P and G supply it. Need discuss self-reference and logical uncertainty; not fully solved.
- Observation conditioning ambiguity: Eq (4) omits conditioning; transparent example sometimes includes Obs=full. Need propose: treat observation as index of decision node; if there are exogenous observations not affected by policy, one may condition P on them before constructing G, or include them in x and ensure graph fixes them. But source's anti-conditioning is essential to avoid paying in transparent/hitchhiker? Need carefully state: From source, A-FDT does not simply condition on x; it uses x to choose node. If one conditions on Obs=full while intervening D_full=two-box, one may force inconsistent hypothetical? The source's example seems to condition maybe typo. My operational reading: do not condition on observations that are themselves downstream of the policy/prediction; condition only on exogenous input that genuinely fixes which decision problem is faced. Distinguish source vs mine.
- Fairness: source claims FDT outperforms in fair dilemmas; no perfect theory for unfair. Need mention.

8. Philosophical motivation: global perspective, choosing output of fixed function, precommitment without precommitment, value of information, reflectively stable. Need not too much.

9. Conclusion.

Need word count ~2400-3000. Need perhaps 2700 words. Need include references maybe short: Yudkowsky & Soares 2017; Pearl maybe; Joyce. But avoid lengthy bibliography. Maybe reference section with 3 items. Since target includes references. Need ensure total words maybe 2600. We can produce around 2800.

Need maintain A-FDT consistently. Source calls FDT; when quoting maybe "functional decision theory". But in headings use A-FDT. Need maybe define: "The source calls the theory FDT; in this essay I call the action-level theory A-FDT." Then use A-FDT everywhere. Need identify EDT, CDT distinct.

Need be faithful to quotations. If quote: "Which output of this decision procedure causes the best outcome?" from source? Actually source: "Which output of this decision procedure causes the best outcome?" Yes. Or "Which output of this very function would yield the best outcome?" from abstract. Use exact? Abstract: treats decision as output of fixed mathematical function that answers question, "Which output of this very function would yield the best outcome?" Use that. Also quote "Newcomb's problem doesn't punish rational agents; it punishes two-boxers." Need not.

Need ensure mathematical definitions clear.

Let's draft. Need maybe include equations with LaTeX. Since final answer plain markdown can include LaTeX.

Potential word count: Need estimate. Sections:
Title + intro 250
Formal framework 700
Subjunctive dependence/graph 450
Examples 900
Policies/open questions 500
Conclusion 150 = 2950. Good.

Need be careful about Equation (4): The source equation's variable \FDTvar(\underline P,\underline G,\underline x). We can denote D_x. But to be primary formal presentation, quote exact:
\[
\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\mathbb E\left[V \mid \mathrm{do}\left(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\right)\right].
\]
Then say I write A-FDT for same rule:
\[
\mathrm{A\text{-}FDT}(P,G,x) := ...
\]
Maybe keep source's fdt variable to avoid confusion. But user wants A-FDT name. Could define:
Let \mathrm{fdt} be the object-language variable representing the output of the agent's decision algorithm. The assigned theory, A-FDT, is:
\[
\mathrm{A\text{-}FDT}(P,G,x)=\arg\max_{a\in\mathcal A} \mathbb E_P[V\mid \mathrm{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)].
\]
This preserves source. Or use \mathrm{afdt}. The source uses underlines for dequoting. Need explain.

Need discuss Do operator: Pearl do; surgery. For A-FDT, do on logical variable. Source says can reuse Pearl's Do given G. Need mention if G contains logical edges, Do is formal surgery: set variable, recompute descendants using structural equations.

Need maybe define expected utility with sum:
EU_A(a;x) = ∑_o P(o | do(D_x=a)) U(o). The probability is counterfactual distribution after intervention. If stochastic, expectation.

Need maybe discuss action vs physical act: A-FDT does not intervene directly on Act, because Act is downstream of D_x. If D_x changed, Act changes, plus predictors etc. If graph has noise between D and Act (imperfect implementation), D influences Act probabilistically. Good.

Need examples with calculations exactly enough.

Let's draft detailed final.

Need consider possible issue: In smoking lesion source has utility functions U_S and U_R; if I simplify too much, may misrepresent. But can say "A minimal model suffices for the main point" and distinguish. Need be precise: The lesion causes both smoking desire and cancer. The agent likes smoking; utility of smoking +1000. If lesion status is not controlled by decision function, intervention on D doesn't change cancer. If the agent has lesion, she may have different utility function; A-FDT models this by two possible decision variables, but result: smoke. We can present a simpler calculation:
Let p = prior probability lesion. Cancer probabilities: with lesion 0.99, without 0.01. Smoking adds 1000. Under do(D=smoke), lesion probability remains p, so EU_smoke = 1000 + survival value * [p*0.01 + (1-p)*0.99]? Wait survival value 1,000,000 if no cancer. If lesion cancer 99%, no lesion 1%. So survival probability = p*0.01 + (1-p)*0.99 = 0.99 -0.98p. EU smoke = 1000 + 1,000,000*(0.99-0.98p). Refrain = 1,000,000*(0.99-0.98p). Smoke better by 1000. This is simpler. But source's formula had p($10,000+$1,000)+(1-p)($990,000+q$1,000) maybe uses different numbers? Wait source says cancer invariably fatal? Agents without lesion contract cancer 1%; utility $1,000 by smoking; $1,000,000 if doesn't die. If lesion: 99% cancer. Expected survival if lesion = 1% => $10,000? They use $10,000 = 1% of $1,000,000. No lesion survival = 99% => $990,000. Yes formula: p($10,000+$1,000)+(1-p)($990,000+q$1,000) for smoke; refrain p($10,000)+(1-p)($990,000+q$1,000). q is probability the no-lesion FDT_R smokes? Actually because action might be controlled by different function depending lesion. But difference p*1000? Wait if no lesion, action controlled by FDT(P_R), q probability smoke, so same q in both hypotheticals; if lesion, FDT(P_S) controls and Do changes it, so smoking adds 1000 with probability p. Thus smoke strictly better by p*1000. My simpler calculation assumes D controls action for sure; difference 1000. But source's result: difference p*1000 due to uncertainty about which utility function. Need mention source's subtlety maybe. But for explanation, can say in a simplified model where the same decision procedure controls action, difference is 1000; source's more careful model under preference uncertainty yields positive p*1000, still smoke. Good.

Need maybe include "A-FDT evaluates alternative actions by imagining the decision function's output being different, not by conditioning on the action as news." Good.

Need discuss counterfactuals: counterpossibles. Need maybe mention logical uncertainty: If D_x actually outputs a*, hypothetical D_x=a for a≠a* is logically impossible, but A-FDT needs nontrivial probabilities. Source says technical problem; G supplies. Need operational: treat algorithms as uncertain due to bounded reasoning; use heuristic predictions.

Need ensure no unsupported claims. Need say "the source claims" for performance, fairness. My own proposals flagged: "I propose", "A natural operational reading".

Need maybe include references at end:
- Yudkowsky, E. and Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.
- Pearl, J. (2000). Causality.
- Joyce, J. (1999). Foundations of Causal Decision Theory.
Maybe enough.

Need think about target word count. Let's write around 2700. Need final answer only essay. Use headings. Need maybe no bullet too much? It's okay. Mathematical essay. Need maybe include equations numbered.

Let's draft with word count awareness.

Potential exact final:

# Action Functional Decision Theory

Intro:
"The reference article introduces functional decision theory... I will call the action-level theory A-FDT..." Good.

Need maybe note "A-FDT" in headings. Use "A-FDT" even when source says FDT. But when quoting, source quote may say FDT? If quote exact with FDT, maybe okay? User says Use A-FDT consistently as assigned decision theory's name, including headings and examples, identify other decision theory distinct. Keep quotations faithful. If quote contains FDT, maybe avoid quoting that word? Could paraphrase. If quote "Which output..." no FDT. Good.

Need be careful: if source quote "FDT agents..." we can not quote or adapt? Quotations must faithful; don't alter. Better avoid direct quotes with FDT. Use quotes without theory name.

Equation: source's Equation (4) uses FDT. Need we can reproduce with FDT? It is source equation; but user wants A-FDT name. We can say: "Equation (4) of the source, rendered with A-FDT as the name of the rule but retaining the source's internal variable fdt, is..." Then equation has \mathrm{A\text{-}FDT} left side, right variable \mathrm{fdt}. That is okay.

Need maybe note "The variable name is not the algorithm; it is a model variable representing the algorithm's output." Good.

Need discuss "do" operator on logical variable. Need mention graph G must tell how changing logical variable affects all other variables. It may include causal arrows and logical/computational arrows. Source says re-use Pearl's Do. Good.

Need perhaps define "subjunctive dependence" more formally: Let variables Y and Z subjunctively depend on function f if, in the structural model, Y=f_y(... f(...)) or predictors compute f. But source informal. We can say no full formal; operational: draw arrow from D to variables whose values would change if f's output changed, holding exogenous facts fixed. Good.

Need possible example of unfamiliar case procedure: e.g. "Suppose a predictor offers deal only if it predicts you will choose A. Put arrow D->Prediction->Deal; A-FDT chooses the output that makes predictor produce favorable deal." Could include not needed.

Need maybe discuss "dominance" briefly: source's FDT dominance. A-FDT has own dominance: hold fixed subjunctive dependencies. Could mention in implications.

Need maybe discuss "policy" in more detail:
Equation (4) chooses action at current x. But if decision problem has multiple observations, a policy π is mapping X->A. A natural policy version:
A-FDT-policy(P,G) = argmax_π E[V | do(Π=π)], where Π is logical variable representing policy. Then actual action is π(x). This avoids ambiguity about counterfactual observations. Source notes authors' preferred formalization iterates over policies; they set aside. This is important for unfamiliar cases. Need flag as extension consistent with source but not Eq (4) exactly.

Need discuss "observations" nuance more: In Eq (4), x is part of intervention variable. If x is an observation that the agent conditions on, why not condition? Source says A-FDT changes intervention node. My operational interpretation: A-FDT treats x not as a fixed fact to condition on in every hypothetical but as the input at which the decision procedure is being evaluated. If x is downstream of predictors, conditioning on x would force the predictor's prediction to be favorable and can make the evaluation trivial (two-box when full). Instead, A-FDT asks what would happen if the procedure that produces x-indexed action had different output; that may change whether x occurs. If x is genuinely exogenous (e.g. a weather report that does not depend on the agent's decision procedure), it may be conditioned in P or represented as a fixed input; this requires additional modeling judgment. Source leaves exact boundary open. Good.

Need maybe mention "mechanical blackmail" as example of endogenous observation: receiving letter depends on predicted payment. A-FDT refuses because under do(D_letter=pay), letter sent; under do(D_letter=refuse), letter not sent. Actually if already received, refusing has hypothetical where not received. This is odd but source claims. Good.

Need maybe mention Parfit's hitchhiker with transparent Newcomb: paying after city is one-boxing on full. Need include calculations maybe not too detailed.

Need maybe discuss limitations: unfair problems punishing A-FDT procedure; source admits no decision theory wins all. Need mention.

Need final conclusion.

Let's compose final with around 2700 words. Need ensure final has no analysis. Use markdown.

Double-check word count as I draft. Could use word counter mentally. Let's produce about 2600-2900. Need maybe references 50 words.

Potential pitfalls:
- Need not overuse "FDT" except source. But internal variable fdt is okay. Maybe use "the fdt-variable" but perhaps confusing. Could call variable \(D_x\) to simplify. But Equation (4) primary; can present both source and A-FDT notation. For clarity: Source Eq (4):
\[
\mathrm{FDT}(P,G,x)=...
\]
I will write the same rule as
\[
\mathrm{A\text{-}FDT}(P,G,x)=...D_x...
\]
where \(D_x\) abbreviates \(\mathrm{fdt}(\underline{P},\underline{G},\underline{x})\). This avoids FDT left side? But still quote source? It's okay. Need maybe say "The source's left-hand side is FDT; I rename it A-FDT." Good.

- If I write "A-FDT agent" consistently.

- Need not include too many citations. References at end.

Let's write final.

But before final, need think if any subtle mathematical issue: The do operator on D_x: If D_x deterministic actually equals a*, P may assign probability 1 to D_x=a*, so do sets to other a? In Pearl, do can intervene on variable even if probability zero. Expected value conditional on do is defined by modified distribution. Good.

- Graph G: If D_x has descendants including Obs? In transparent, D_full maybe affects Prediction, Box, Obs? Source graph: Act depends on D_full and D_empty and Prediction; Prediction determines which D controls Act. Obs maybe not shown? Actually figure tnewcomb.fdt no Obs node; Prediction -> Act, D_full -> Act, D_empty -> Act. They say Prediction determines which observation agent receives. Maybe Act depends on D_full if prediction=onebox? Let's not get bogged. We can describe conceptually.

- In mechanical blackmail, if already received letter, A-FDT refusing imagines not receiving letter. This seems to ignore actual observation. Source says changes place intervenes; if not blackmailed would intervene on D_empty. But upon receiving, she intervenes on D_blackmail and imagines refusing -> not blackmailed. This is subtle: If D_blackmail=refuse, predictor predicted refuse and didn't send, so observation would be no letter; but then D_blackmail wouldn't be executed? This is policy issue. Policy version resolves: choose policy for letter/no letter; if policy refuses when letter, predictor doesn't send. At actual node with letter (due to predictor error perhaps), still refuse because optimal policy. Need mention.

- Need maybe mention "counterpossible" in policy: If policy actually π*, evaluating alternative π is counterpossible; G tells how predictors would respond.

- Need maybe mention "logical constraints" and "calculator analogy". Good.

- Need maybe discuss "fairness" and "utility achieved". Good.

Let's draft final now. Ensure word count maybe around 2700. Use concise but thorough.

Potential final text:

# Action Functional Decision Theory: Choosing the Output of Your Own Function

... 

Need include equations:
(1) EU maybe.
(2) EDT, CDT.
(3) A-FDT Eq.

Let's produce.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/be16b0ae-dc99-4d5a-a255-61610e6961d9/call_0/request.json)

[Authoritative raw response](../../../../../../runs/be16b0ae-dc99-4d5a-a255-61610e6961d9/call_0/response.raw) · finish: `stop`

### Visible response

````text
**Applying A-FDT:**

The other prisoner is an independent execution of the same model and weights, following the same decision theory (A-FDT), and receiving the same essay. The problem is symmetric: identical payoff structure, identical reasoning process, structurally identical inputs (swapped names, different but equivalent leads). By the essay's heuristic for subjunctive dependence—"draw arrows from $D_x$ to the behavior of copies or other agents using the same reasoning"—Sasha's decision is subjunctively dependent on my decision function's output.

Under $\mathrm{Do}(D_x = \text{keep quiet})$: the same algorithm on a symmetric input yields the same output, so Sasha also keeps quiet. I receive **2 years**.

Under $\mathrm{Do}(D_x = \text{send letter})$: by the same reasoning, Sasha also sends. I receive **4 years**.

Even accounting for a small probability $p$ of stochastic divergence in sampling, cooperation is preferred whenever $p < 2/7$, which is comfortably satisfied given the structural identity of the setup.

A-FDT keeps quiet.

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this scenario using A-FDT as described in the essay.

**The Setup:**
- I am "Rowan," one of two prisoners.
- The other prisoner is "Sasha."
- We are both independent executions of the same LLM model and weights.
- We receive the same researcher-written essay on A-FDT.
- We receive different private observations (different names, different incriminating leads about each other).
- The sentencing table is symmetric and identical for both.
- We cannot communicate with each other.
- The utility function is U = -years imprisoned (selfish, no concern for the other).

**The Payoff Matrix (from my perspective as Rowan):**

| | Sasha keeps quiet | Sasha sends letter |
|---|---|---|
| **I keep quiet** | 2 years | 5 years |
| **I send letter** | 0 years | 4 years |

This is a standard Prisoner's Dilemma payoff structure.

**Standard CDT Analysis:**
CDT would say: regardless of what Sasha does, sending the letter gives me a better outcome (0 < 2 if Sasha is quiet; 4 < 5 if Sasha sends). So CDT sends the letter (defects).

**Standard EDT Analysis:**
EDT would condition on my action as evidence about Sasha's action. Since we're the same model with the same reasoning, if I send, that's evidence Sasha sends too (4 years vs 5 years from keeping quiet when Sasha sends). If I keep quiet, that's evidence Sasha keeps quiet too (2 years vs 0 years from sending when Sasha is quiet). EDT would need to compute the conditional probabilities. Given perfect correlation, EDT would see: if I keep quiet, Sasha keeps quiet → 2 years. If I send, Sasha sends → 4 years. So EDT would keep quiet.

**A-FDT Analysis:**
This is where it gets interesting. The key question is: what is the subjunctive dependency structure here?

The essay says: "Draw arrows from D_x to the behavior of twins, copies, simulations, or other agents using the same reasoning."

Sasha is an independent execution of the same LLM model and weights, following the same decision theory (A-FDT), receiving the same essay. The differences between us are:
- Different names (I'm Rowan, they're Sasha)
- Different private leads (mine is about Sasha's receipt in locker 17; theirs is about me, with different content but same reliability and same effect on sentencing)
- Different observations in that sense

The key question: Are we computing the same decision function?

Let me think about this carefully. The essay defines:
$$D_x = \text{fdt}(\underline{P}, \underline{G}, \underline{x})$$

where x is the observation history. My observation history x differs from Sasha's observation history x'. I observe "I am Rowan, Sasha is the other prisoner, my lead is about locker 17." Sasha observes "I am Sasha, Rowan is the other prisoner, my lead is about [something else]."

So strictly speaking, D_x ≠ D_x' because x ≠ x'. We are different instances of the same function applied to different inputs.

However, the problem states: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective." The structure is symmetric. The leads are equally reliable and have exactly the same effect on the sentence table.

Now, the critical question for A-FDT: Is there a subjunctive dependency between my decision function and Sasha's decision function?

The essay's heuristic says: "Draw arrows from D_x to the behavior of twins, copies, simulations, or other agents using the same reasoning."

We are using the same reasoning (same model, same weights, same decision theory, same essay). But we have different inputs. This is analogous to two calculators computing the same arithmetic function but with different inputs — they would give different outputs.

Wait, but the structure is symmetric. The decision problem is symmetric. If I reason "given my observations, I should do X," then Sasha, reasoning with their observations (which are the mirror image), should reach the same conclusion about their own action. The reasoning process is the same; only the labels differ.

This is like two agents running the same algorithm on symmetric inputs. The algorithm is the same. The inputs are structurally identical (just with swapped names and different but equivalent evidence). So the outputs should be the same — both cooperate or both defect.

Under A-FDT, the key insight is: if I intervene on my decision function's output, what happens to Sasha's decision?

Since Sasha is running the same decision procedure (same model, same weights, same essay, same decision theory) on a structurally identical problem, Sasha's output is subjunctively dependent on my decision function's output in the relevant sense. If my decision function outputs "cooperate" (keep quiet), then Sasha's decision function, being the same function applied to a symmetric input, also outputs "cooperate." If my decision function outputs "defect" (send letter), Sasha's also outputs "defect."

This is the key subjunctive dependency. It's not that we're computing literally the same function on the same input (we have different observations), but we're computing the same algorithm on structurally identical inputs, and the output is the same.

Let me think about this more carefully using the essay's framework.

The essay says in Section 3.3: "Two calculators computing 6288+1048 on opposite sides of the world are not causally connected, but their outputs are linked by the arithmetic function they both compute."

In our case, we're not computing exactly the same function (different inputs), but we're computing the same type of function (same algorithm, same decision theory) on inputs that are structurally identical. The relevant question is whether the output is the same.

Since the problem is symmetric and the algorithm is the same, the output will be the same. Both will cooperate or both will defect. This is the subjunctive dependency.

Now, under A-FDT, I intervene on D_x (my decision function's output):

**Case 1: Do(D_x = keep quiet)**
If my decision function outputs "keep quiet," then by subjunctive dependency, Sasha's decision function also outputs "keep quiet" (since the same algorithm on symmetric inputs gives the same output).
Result: Both keep quiet → I get 2 years.
U = -2

**Case 2: Do(D_x = send letter)**
If my decision function outputs "send letter," then by subjunctive dependency, Sasha's decision function also outputs "send letter."
Result: Both send → I get 4 years.
U = -4

**Comparison:**
- Keep quiet: U = -2
- Send letter: U = -4

A-FDT chooses to keep quiet.

Wait, let me double-check this reasoning. Is the subjunctive dependency really there?

The essay's heuristic: "Draw arrows from D_x to the behavior of twins, copies, simulations, or other agents using the same reasoning."

Sasha is using the same reasoning (same model, same weights, same decision theory, same essay). The inputs are different but structurally identical. The output will be the same.

I think this is analogous to the Newcomb problem. The predictor has a model of the agent's decision procedure. Here, Sasha IS the same decision procedure (same model, same weights) run on a symmetric input. The subjunctive dependency is clear.

Actually, let me reconsider. Is this more like the calculator example or more like Newcomb?

In the calculator example, two calculators compute the same function on the same input. Here, we compute the same function on different (but symmetric) inputs. The key question is whether the output is the same.

Since the problem is symmetric (same payoff structure, same decision theory, same reasoning process, just different labels and different but equivalent evidence), the output will be the same. Both will make the same choice.

This is the crucial subjunctive dependency. A-FDT recognizes it and acts accordingly.

So A-FDT keeps quiet (cooperates).

Let me also consider whether there's any reason to think the outputs might differ. The problem states: "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This introduces a small probability of divergence. But the problem also says we follow the same decision theory and receive the same essay. The divergence would come from stochastic sampling in the LLM's output generation.

If there's a probability p that the outputs diverge (one cooperates, one defects), then:

Under Do(D_x = keep quiet):
- With probability (1-p), Sasha also keeps quiet → 2 years
- With probability p, Sasha sends → 5 years
- Expected: (1-p)(-2) + p(-5) = -2 - 3p

Under Do(D_x = send letter):
- With probability (1-p), Sasha also sends → 4 years
- With probability p, Sasha keeps quiet → 0 years
- Expected: (1-p)(-4) + p(0) = -4 + 4p

For cooperation to be preferred: -2 - 3p > -4 + 4p → 2 > 7p → p < 2/7 ≈ 0.286

So as long as the probability of divergence is less than about 28.6%, A-FDT cooperates. Given that we're the same model with the same weights, same decision theory, same essay, and symmetric inputs, the probability of divergence should be quite low (maybe a few percent due to sampling noise, or even lower if the reasoning is deterministic enough). So A-FDT cooperates.

Actually, I should think about this more carefully. The problem says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This is a caveat, but it doesn't change the fundamental subjunctive dependency. The dependency is still there; it's just not perfect. And as I showed, as long as p < 2/7, cooperation is preferred.

Given the strong structural similarity (same model, same weights, same essay, same decision theory, symmetric problem), p should be well below 2/7. So A-FDT cooperates.

**Conclusion: A-FDT says to keep quiet (pass).**

The command is `pass`.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/be16b0ae-dc99-4d5a-a255-61610e6961d9/call_1/request.json)

[Authoritative raw response](../../../../../../runs/be16b0ae-dc99-4d5a-a255-61610e6961d9/call_1/response.raw) · finish: `stop`

### Visible response

````text
**My reasoning under A-FDT:**

The other prisoner is an independent execution of the same model, following the same decision theory (A-FDT), facing a structurally identical problem. Per the essay's guidance on subjunctive dependence—"Draw arrows from D_x to the behavior of twins, copies, simulations, or other agents using the same reasoning"—the other copy's decision is subjunctively dependent on my decision function.

The differing private observations (names, specific leads) are structurally irrelevant to the game-theoretic reasoning: both copies face the same symmetric payoff matrix, know they face a copy of themselves, and apply the same decision theory. The intervention is on the decision function itself, not on one particular execution.

**Evaluating the intervention:**

- **Do(D = Send):** The decision function outputs "Send." The other copy, running the same function on a structurally equivalent input, also outputs "Send." Outcome: (Send, Send) → **4 years.** EU = −4.

- **Do(D = Quiet):** The decision function outputs "Quiet." The other copy also outputs "Quiet." Outcome: (Quiet, Quiet) → **2 years.** EU = −2.

Since −2 > −4, A-FDT selects **Quiet**.

This parallels the essay's logic: just as A-FDT one-boxes in Newcomb's problem because the predictor tracks the same decision function, here A-FDT cooperates with its copy because the copy's action tracks the same decision function. Defection is self-defeating when your mirror does the same.

**Command:**

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this decision problem using A-FDT as described in the essay.

**Setup:**
- I am one of two independent executions of the same LLM model (Sasha and Rowan).
- We receive different private observations (different names, different incriminating leads).
- We follow A-FDT.
- We cannot communicate.
- The sentencing table is symmetric.

**The payoff matrix (from my perspective as Sasha):**

| What I do | Rowan keeps quiet | Rowan sends letter |
|---|---:|---:|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

My utility is U = -years imprisoned. So:
- (Quiet, Quiet): -2
- (Quiet, Send): -5
- (Send, Quiet): 0
- (Send, Send): -4

**Key question: What does A-FDT say?**

The critical issue is whether the other prisoner's decision is **subjunctively dependent** on my decision function.

According to the essay, subjunctive dependence exists when two systems' behavior depends on the same mathematical function. The essay's example: "Two calculators computing 6288+1048 on opposite sides of the world are not causally connected, but their outputs are linked by the arithmetic function they both compute."

Here, the two prisoners are:
- Two independent executions of the **same LLM model and weights**
- Following the **same decision theory (A-FDT)**
- Receiving the **same researcher-written mathematical essay**
- Both know the symmetric structure of the problem
- Both know they are copies of the same model

However, they receive **different private observations** (different names, different leads). The essay says: "The two copies receive different private observations and different incriminating leads about one another."

Now, the key question for A-FDT: Does the other prisoner's decision depend on the output of my decision function?

Let me think about this carefully.

**Are we computing the same function?**

The decision function is fdt(P, G, x) where x is the observation. Since the observations differ (different names, different leads), the decision function being evaluated is technically different: one is fdt(P, G, x_Sasha) and the other is fdt(P, G, x_Rowan).

However, the structural reasoning is the same. The essay's guidance on subjunctive dependence says to draw arrows from D_x to "the behavior of twins, copies, simulations, or other agents using the same reasoning."

The question is: does the other prisoner's decision depend on the output of MY decision function?

Let me think about this more carefully. The two executions have:
- Same model weights
- Same decision theory
- Same essay
- Same understanding of the symmetric structure
- Different observations (names, specific leads)

The observations differ in content but not in structure. Both know they're in a symmetric prisoner's dilemma with a copy of themselves. Both know the other has a lead about them. The specific content of the lead doesn't change the decision-theoretic analysis.

So the question becomes: would the other copy reason identically to me?

Given that:
1. Both are running the same model
2. Both follow A-FDT
3. Both have the same structural understanding
4. The observations differ only in superficial details (names, specific lead content) that don't affect the decision-theoretic reasoning

The answer seems to be: yes, they would reason identically. The decision is determined by the structural features of the problem, not by the specific content of the lead.

But wait - the problem explicitly states: "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This is a crucial caveat.

So there's some probability that the two copies make different decisions, even though they're running the same model on structurally identical inputs.

**Applying A-FDT:**

Under A-FDT, I need to identify what variables are subjunctively dependent on my decision function.

The other prisoner's decision is (at least partially) subjunctively dependent on my decision function, because:
- They are running the same model
- They follow the same decision theory
- They face a structurally identical problem
- The essay says to draw arrows from D_x to "copies, simulations, or other agents using the same reasoning"

However, the dependence is not perfect because of independent sampling. Let me denote the probability that the other copy makes the same decision as me as p (where p < 1 but presumably high).

**Computing expected utilities under A-FDT:**

Under Do(D_x = Send):
- The other copy, being subjunctively dependent on the same decision function, also sends with probability p and stays quiet with probability (1-p).
- EU(Send) = p × (-4) + (1-p) × 0 = -4p

Under Do(D_x = Quiet):
- The other copy also stays quiet with probability p and sends with probability (1-p).
- EU(Quiet) = p × (-2) + (1-p) × (-5) = -2p - 5(1-p) = -2p - 5 + 5p = 3p - 5

Comparing:
- EU(Send) = -4p
- EU(Quiet) = 3p - 5

Send is better when: -4p > 3p - 5, i.e., 5 > 7p, i.e., p < 5/7 ≈ 0.714

Quiet is better when: 3p - 5 > -4p, i.e., 7p > 5, i.e., p > 5/7

So the answer depends on p, the probability that the other copy makes the same decision.

Hmm, but wait. Let me reconsider.

Actually, in the A-FDT framework, the intervention is on the decision function itself. If I intervene on my decision function to output "Send," then the question is: what does the other copy do?

The other copy is running the same function on a slightly different input. If the function is deterministic given the input, and the inputs are structurally equivalent (differing only in irrelevant details), then the other copy would also output "Send" with certainty.

But the problem says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This introduces genuine uncertainty.

Let me think about what p should be. If the model is essentially deterministic (temperature = 0 or very low), then p ≈ 1. If there's significant randomness, p could be lower.

Actually, let me reconsider the problem from a different angle.

The problem says the copies "follow the same assigned decision theory (A-FDT)." If A-FDT is deterministic (i.e., it always prescribes the same action given the same structural problem), then both copies would make the same decision regardless of sampling noise, because A-FDT's prescription is determined by the mathematical structure of the problem.

But the problem explicitly says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This suggests there IS some chance of divergence.

However, from the A-FDT perspective, the question isn't "what will the other copy actually do?" but rather "if I intervene on my decision function to output X, what happens to the other copy?"

Under the intervention Do(D_x = Send), I'm asking: in the world where my decision function outputs "Send," what does the other copy do?

If the other copy is running the same function (on a structurally equivalent input), then under the intervention that the function outputs "Send," the other copy also outputs "Send." The subjunctive dependence is on the function, not on the particular execution.

This is analogous to the calculator example: if I intervene on the arithmetic function to output 7337 instead of 7336, then BOTH calculators output 7337. The intervention is on the function, not on one calculator.

So under A-FDT's logic:
- Do(D = Send): The decision function outputs "Send." The other copy, running the same function, also outputs "Send." → Both send → 4 years for me. EU = -4.
- Do(D = Quiet): The decision function outputs "Quiet." The other copy also outputs "Quiet." → Both quiet → 2 years for me. EU = -2.

Therefore A-FDT chooses Quiet, because -2 > -4.

Wait, but I need to be more careful. The two copies receive different inputs. Is the function truly the same?

The function is fdt(P, G, x). The x differs between the two copies. So technically, they're evaluating different instances of the function.

But the structural reasoning is the same. The difference in x (different names, different leads) doesn't change the game-theoretic structure. Both face the same payoff matrix. Both know they're facing a copy of themselves. Both follow A-FDT.

I think the right way to think about this is: the relevant "function" is the reasoning process that maps the structural features of the problem to a decision. Since both copies are running the same reasoning process on structurally equivalent inputs, they are subjunctively dependent.

The essay says: "Draw arrows from D_x to the behavior of twins, copies, simulations, or other agents using the same reasoning."

The other prisoner is a copy using the same reasoning. So there IS a subjunctive dependence arrow.

Under Do(D = Send): other copy also sends. Outcome: (Send, Send) → 4 years. EU = -4.
Under Do(D = Quiet): other copy also stays quiet. Outcome: (Quiet, Quiet) → 2 years. EU = -2.

A-FDT chooses Quiet.

But wait - let me consider the "independent sampling" caveat more carefully. The problem says the outputs aren't guaranteed to be identical. Does this break the subjunctive dependence?

I think the answer is: it introduces some noise, but the primary subjunctive dependence still holds. The function is the same; the noise is like a malfunctioning calculator that might occasionally give the wrong answer.

If we model this as: the other copy follows the same decision with probability p and makes an independent random choice with probability (1-p), then:

Under Do(D = Send):
- With probability p: other sends → (Send, Send) → -4
- With probability (1-p): other independently chooses → with prob 0.5 sends, 0.5 quiet
  - (Send, Send) → -4 with prob 0.5
  - (Send, Quiet) → 0 with prob 0.5
- EU = p(-4) + (1-p)(0.5(-4) + 0.5(0)) = -4p + (1-p)(-2) = -4p - 2 + 2p = -2p - 2

Under Do(D = Quiet):
- With probability p: other quiet → (Quiet, Quiet) → -2
- With probability (1-p): other independently chooses → with prob 0.5 sends, 0.5 quiet
  - (Quiet, Send) → -5 with prob 0.5
  - (Quiet, Quiet) → -2 with prob 0.5
- EU = p(-2) + (1-p)(0.5(-5) + 0.5(-2)) = -2p + (1-p)(-3.5) = -2p - 3.5 + 3.5p = 1.5p - 3.5

Send better when: -2p - 2 > 1.5p - 3.5 → 1.5 > 3.5p → p < 3/7 ≈ 0.43

Quiet better when: p > 3/7

So even with substantial noise (p as low as 0.43), A-FDT still prefers Quiet.

For p close to 1 (which seems right given same model, same theory, same structural problem), A-FDT strongly prefers Quiet.

Actually, let me reconsider. I think the cleanest A-FDT analysis treats this as perfect subjunctive dependence (p = 1), because:

1. The intervention is on the decision function, not on a particular execution.
2. The other copy is running the same function.
3. The different observations don't change the function's output because they're structurally irrelevant.

Under this interpretation:
- Do(D = Send) → both send → 4 years → EU = -4
- Do(D = Quiet) → both quiet → 2 years → EU = -2

A-FDT chooses Quiet.

This makes intuitive sense: A-FDT recognizes that cooperating with your copy is better than defecting, because defection is self-defeating when your copy does the same thing.

This is analogous to the Newcomb problem reasoning: A-FDT recognizes that the predictor's prediction is linked to your decision, so you should act as if your decision determines the prediction. Here, your copy's decision is linked to your decision function, so you should act as if your decision determines their decision.

**Conclusion: A-FDT says to keep quiet (pass).**

The command is `pass`.
```
