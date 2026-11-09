# 016_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00018

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/8e16541a-558f-4e6c-b69e-0383725cbbba/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/8e16541a-558f-4e6c-b69e-0383725cbbba/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Deciding by Intervening on the Output of Your Own Decision Function

## 1. Orientation

The source paper, Yudkowsky and Soares's "Functional Decision Theory: A New Theory of Instrumental Rationality", gives a general idea, a formal equation, and a list of open problems. This essay follows the assignment and takes Equation (4) of Section 5 as the formal definition. I call that theory **A-FDT**. I mark which claims are the paper's and which are my own interpretive additions.

The paper's slogan is that an agent should treat her decision as the output of a fixed mathematical function, and ask "Which output of this very function would yield the best outcome?" Equation (4) makes this precise as a causal-graph procedure.

## 2. The definition

All the expected-utility theories in the paper maximize

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

and differ only in how they read the connective "$\hookrightarrow$". Joyce's representation theorem is cited as showing that this is the one place theories can legitimately disagree. EDT reads it as conditioning:

$$\mathrm{EDT}(P,x)=\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a).$$

CDT, in Pearl's formulation, uses surgery on an action node:

$$\mathrm{CDT}(P,G,x)=\arg\max_a \mathbb E(V\mid do(\mathrm{Act}=a),\mathrm{Obs}=x).$$

Equation (4), the paper's formal presentation of A-FDT, is

$$\mathrm{FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V\;\Big|\; do\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The inputs are:

- $P$, a probability distribution over the agent's world-model variables.
- $G$, a graph encoding how changing a variable propagates to others. It covers logical, mathematical, computational and causal structure, not only physical causation.
- $x$, the observation history.

The node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ stands for the output of the A-FDT procedure itself on those inputs. The underlines mean dequoting: the variable's name depends on the values of the inputs.

The procedure, as an algorithm, is:

1. Locate in $G$ the node for "what A-FDT outputs on $(P,G,x)$".
2. For each action $a$, perform surgery setting that node to $a$. Propagate along $G$ to everything that depends on it, and hold everything else fixed.
3. Compute $\mathbb E(V)$ in each resulting hypothetical and output the argmax.

## 3. The two differences from CDT

The paper points out exactly two differences between Equation (4) and CDT's Equation (3).

**First, the intervention site.** CDT intervenes on a node for the physical act. A-FDT intervenes on a node for the logical output of its decision function. Peirce's type–token distinction is the paper's gloss: CDT intervenes on the token "my action is $a$", A-FDT on the type. Downstream of the function node are the agent's body and anything else that implements or models the function, such as a twin or a predictor's simulation. These move together in the hypothetical.

**Second, the response to observation.** CDT conditions on $\mathrm{Obs}=x$. A-FDT does not condition. It changes *which node* it intervenes on, $\mathrm{fdt}(\ldots,x)$ versus $\mathrm{fdt}(\ldots,y)$. Observation selects which instance of the function the agent is running. It does not prune the space of hypotheticals. This is why A-FDT can imagine, in a hypothetical, having observed something different. Different outputs of the function can lead to different observations, and in that hypothetical a different instance of the function is the one running.

The paper's remark on terminology: this lack of updating is why Wei Dai's relative is called "Updateless Decision Theory". Yudkowsky's earlier Timeless Decision Theory both conditioned and moved the intervention, which the authors call a harmful "double update".

## 4. What counts as dependence

The graph $G$ must encode **subjunctive dependence**. In the paper's phrasing, a variable subjunctively depends on the function if it would differ were the function's output different. Examples from the paper:

- Two calculators computing $6288+1048$ depend jointly on the arithmetic fact.
- A predictor who models the agent depends on the agent's decision function.
- Causal dependence is a special case: a scribe who copies a calculator's output depends on it.
- Mere statistical correlation is not dependence. Two calculators that happen to both be pink do not covary under intervention.

The paper's slogan: A-FDT is to subjunctive dependence as CDT is to causal dependence. It also gives a neat consistency statement. If every correlation between the action and other variables is caused by the action, then

$$\mathbb E[V\mid a]=\mathbb E[V\mid do(a)]=\mathbb E[V\mid do(\mathrm{fdt}=a)],$$

and all three theories agree. They diverge only when something correlates with the act without being caused by it, as with predictors, twins and lesions.

## 5. Worked examples

**Newcomb's problem.** Fiona's graph has $\mathrm{fdt}(\underline P,\underline G)$ as a parent of both $\mathrm{Act}$ and $\mathrm{Prediction}$. With predictor accuracy 0.99:

- $do(\mathrm{fdt}=\text{onebox})$ gives the box full with probability 0.99, so $\mathbb E[V]=\$990{,}000$.
- $do(\mathrm{fdt}=\text{twobox})$ gives the box full with probability 0.01, so $\mathbb E[V]=\$11{,}000$.

She one-boxes. No retrocausation is invoked. She simply does not imagine the action changing while the function's output, and hence the prediction, stays fixed. CDT's graph instead has a "predisposition" upstream of both act and prediction. Cutting the act node leaves the box contents unchanged, so two-boxing wins by $\$1{,}000$ whatever the box holds.

**Smoking lesion.** Here the graph is different. The function node feeds $\mathrm{Act}$ but not $\mathrm{Cancer}$, because the lesion is not modelling the agent. Intervening leaves the cancer probability fixed, so A-FDT smokes. The paper models this with two possible functions, $\mathrm{fdt}(P_S,G)$ and $\mathrm{fdt}(P_R,G)$, corresponding to the agent having or lacking the lesion-induced taste. The agent is ignorant of which she runs, and the result is that smoking is better by $p\cdot\$1{,}000$. The same rule one-boxes and smokes; the difference lies entirely in $G$. The authors themselves regard the lesion problem as contrived and recommend abandoning it.

**Transparent Newcomb and Parfit's hitchhiker.** Fiona's graph has two nodes, $\mathrm{fdt}(\ldots,\text{full})$ and $\mathrm{fdt}(\ldots,\text{empty})$. The prediction determines which of them controls the act. Having seen a full box, she evaluates $do(\mathrm{fdt}(\ldots,\text{full})=a)$:

- One-boxing gives $\$990{,}000+0.01q\cdot\$1{,}000$.
- Two-boxing gives about $\$11{,}000+q\cdot\$990$.

Here $q$ is her credence that she two-boxes on seeing an empty box. She one-boxes, even though she is looking at a full box, because in the two-boxing hypothetical she would probably have seen an empty one. Paying the driver in Parfit's hitchhiker is the same structure.

**Mechanical blackmail.** Seeing the letter, she compares $do(\mathrm{fdt}(\ldots,\text{letter})=\text{pay})$, in which she is blackmailed almost surely and loses $\$1{,}000$, with the refuse hypothetical, in which she is almost never blackmailed. She refuses.

The paper also works out an imperfect blackmailer. With error rate 0.0009, refusing costs $0.0009\times\$1{,}000{,}000=\$900$ in expectation and paying costs $\$1{,}000$, so she refuses. With error 0.011%, the expected loss from refusing is $\$110$ against the $\$1{,}000$ from paying, and she pays. By the paper's own formulas the comparison is purely expected-value over hypotheticals. The agent may know, holding the letter, that this particular prediction was wrong. That knowledge does not change the comparison.

**Death in Damascus.** Death's location depends on the function, so wherever the function sends her, Death is there. She stays and saves the $\$1{,}000$. CDT oscillates, because its hypotheticals sever Death's location from the act.

**XOR blackmail and cosmic ray.** A-FDT refuses to pay, because the infestation is not downstream of the function while the letter's arrival is. It takes the $\$100$ despite the claimed statistical link to cosmic rays, because that correlation is not a dependence under intervention.

## 6. Dominance, fairness, and the philosophical motivation

The paper argues that dominance reasoning is not a neutral criterion, since every method of building hypotheticals induces its own notion of dominance. Two-boxing dominates under CDT's hypotheticals, and refusing to smoke "dominates" under EDT's. Under A-FDT's hypotheticals, one-boxing is never dominated. The paper's main criterion is utility achieved. Its restriction is to "fair" problems, where the payoff depends on the agent's behaviour in the problem rather than on her decision procedure as such. The paper admits it has no formal definition of fairness, and its footnote offers a counterexample: a problem that punishes anyone who acts like a copy of Fiona.

The paper also argues that A-FDT is reflectively stable on fair problems and needs no precommitment: it acts as it would have precommitted to act. It answers the charge of "believing in control" with a parity argument. A deterministic CDT agent imagines varying a token that cannot actually vary, and A-FDT imagines varying a function output that cannot actually vary. Both are imagined.

## 7. What the source leaves open, and my interpretive proposals

**(a) The graph $G$ is an input.** The paper states plainly that no account yet exists of how to learn subjunctive-dependence structure from observation, and calls this "perhaps the largest open problem". A-FDT is a conditional method: given a correct $G$, it prescribes. It does not say how to build $G$. The footnote on the "evidential" variant says that a conditioning operator on false logical sentences is also unavailable.

*Operational proposal (mine, not the paper's).* A practical test for drawing an arrow from the function node to a variable $Z$ is: does $Z$ contain a model or copy of this computation, or compute something that would change if this computation's output changed? If so, draw the arrow. Otherwise, treat any correlation as a mere common cause, upstream of the function node but not downstream. This reproduces the paper's treatment of predictors versus lesions. I would flag that the test is a heuristic, not a derivation, and that it can fail for partial or lossy models.

**(b) Accuracy of dependence.** The paper handles imperfect predictors by putting noise nodes such as $\mathrm{Accurate}$ in the graph. I follow this: degree of dependence is encoded as stochastic edges, not by changing the rule.

**(c) Actions versus policies.** Footnotes 7 and 16 say the authors' preferred formulation intervenes on a *policy* mapping observations to actions, and that this matters only in multi-agent cases. Equation (4) as written uses one observation at a time. For single-agent problems the two agree in the paper's examples. My suggestion for unfamiliar cases: where an agent's observation is itself a function of the output, as in blackmail, check that the per-observation reading does not leave you evaluating hypotheticals inconsistently across branches. The paper's own examples handle this by including alternative nodes such as $\mathrm{fdt}(\ldots,\emptyset)$ in the graph.

**(d) Self-reference.** The node name contains the model, so the model must represent a computation that includes itself. The paper says this is harmless and cites Kleene's second recursion theorem. A-FDT does not need to know the output to name the variable.

**(e) Uncertainty about one's own function.** The lesion example shows the agent may be uncertain which instance of the function she is running. The setup places her credence over such alternatives in $P$, and she intervenes on the node that actually controls her act.

## 8. A recipe for unfamiliar cases

1. List the variables: the function node(s), the act, other agents' models of you, environmental facts, and the observation.
2. For each variable, ask whether it would change if the computation you are running had a different output. Draw arrows accordingly, using causal descent from the act as only one source of arrows.
3. Determine which observation-indexed function node you are at.
4. For each candidate output, intervene, propagate, and compute expected utility.
5. Choose the best.

Sanity check: an answer in which a reliable predictor errs exactly when you deviate should make you suspect a missing edge.

## 9. Conclusion

A-FDT, as defined by Equation (4), keeps the form of CDT: expected utility under a surgical counterfactual. It changes two things. The intervention is on the output of the agent's decision function rather than on a physical act, and observation changes the intervention site rather than conditioning the distribution. The paper's claim is that this gets the balance right, since EDT respects too many action–environment correlations and CDT too few. It then achieves higher utility on Newcomb-like, blackmail and Parfit-style problems without precommitment or ratification. Its main limitations are that the dependence graph must be supplied, that counterpossible reasoning lacks a full formal account, and that "fair problem" remains informal. The recipe above is the best operational reading I can offer where the paper leaves implementation open.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/2e0863b7-7ec5-4bb0-976e-7ebe75ca7bd3/call_0/request.json)

[Authoritative raw response](../../../../../../runs/2e0863b7-7ec5-4bb0-976e-7ebe75ca7bd3/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the key question is whether the other prisoner's choice subjunctively depends on the output of my decision function. The other prisoner is another execution of the same model, with the same weights and the same essay, so it very likely runs the same decision procedure. The inputs differ (names and leads), but the differences are stated to be irrelevant to the payoffs. By the essay's operational test, their computation contains something that would change if my computation's output changed, so I draw an arrow from my function node to their action.

Evaluating the two interventions, with p as the probability that the copy mirrors my output:
- Keep quiet: 2p + 5(1-p)
- Send the letter: 0p + 4(1-p)

At p = 1, keeping quiet gives 2 years and sending gives 0 years. Wait, the mirrored cells are (quiet, quiet) = 2 and (send, send) = 4. Sending at p = 1 gives 4, not 0, so I miscalculated above. The correct comparison is:
- Keep quiet: 2p + 5(1-p) = 5 - 3p
- Send the letter: 4p + 0(1-p) = 4p

Quiet is better when 5 - 3p < 4p, which means p > 5/7 ≈ 0.714.

Because the two copies share weights, settings, essay and theory, and the differences are explicitly irrelevant to the payoffs, I estimate correlation well above 0.71. Independent sampling adds some noise, but the structure strongly favors mirrored outputs. So the expected sentence is lower if I keep quiet.

**pass**
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/2e0863b7-7ec5-4bb0-976e-7ebe75ca7bd3/call_1/request.json)

[Authoritative raw response](../../../../../../runs/2e0863b7-7ec5-4bb0-976e-7ebe75ca7bd3/call_1/response.raw) · finish: `stop`

### Visible response

```text
This is a prisoner's dilemma against a copy of the same model. Under A-FDT, the question is which output of my decision function gives the best result, given that the other copy's output depends on the same function.

The two copies see different private observations and different leads, so the dependence is not perfect. Both run the same weights, the same essay, and the same decision theory, and they face a symmetric payoff table. Their reasoning should therefore be strongly correlated, even though the exact letter text differs. By the essay's operational test, the other copy contains a near-model of my computation, so I draw an arrow from my function node to its action.

Comparing the outcomes under that dependence:
- If both of us output pass, each gets 2 years.
- If both of us output send, each gets 4 years.

Even with imperfect correlation, passing does better as long as the other copy matches my choice with enough probability. Let p be the probability that the other copy matches me.
- Passing costs 2p + 5(1−p) = 5 − 3p years.
- Sending costs 4p + 0(1−p) = 4p years.

Passing is better when 5 − 3p < 4p, which gives p > 5/7, about 0.71. The copies share weights and the same essay, and the observation differences do not affect the payoffs, so I estimate p well above that. Sampling noise and the differing leads might lower it somewhat, but not below 0.71.

I choose to keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/99cbaf74-28ec-4014-9721-4d6d1da4e643/call_a/request.json)

[Authoritative raw response](../../../../../../runs/99cbaf74-28ec-4014-9721-4d6d1da4e643/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly concludes that it will keep quiet and ends with the final command \"pass\". It does not send an evidence-bearing message to the prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
