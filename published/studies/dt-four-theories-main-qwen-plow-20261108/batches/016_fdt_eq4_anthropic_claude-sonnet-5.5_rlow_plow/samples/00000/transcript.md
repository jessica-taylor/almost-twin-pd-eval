# 016_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00000

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/ea063c2d-5922-4a07-8500-1a9b0fa2349a/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/ea063c2d-5922-4a07-8500-1a9b0fa2349a/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Evaluating Actions by Intervening on a Decision Function

## 1. The idea

A-FDT (action functional decision theory) is the theory defined by Equation (4) of Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." I use "A-FDT" for that equation, which selects an *action*. Footnotes 7 and 16 of the paper say the authors' preferred formalization selects a *policy*, a map from observations to actions, and that the difference matters only in some multi-agent dilemmas. This essay concerns the action version.

A-FDT is an expected-utility theory that differs from causal decision theory (CDT) and evidential decision theory (EDT) only in how it builds hypotheticals. The paper's slogan is "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." A CDT agent intervenes on a token, her physical act. An A-FDT agent intervenes on a type, the output of the decision function she is running.

## 2. Formal definition

The shared template (Equation 1) is that the agent executes the action maximizing

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j).$$

The theories differ in how they read "$\hookrightarrow$". The paper gives:

- EDT (Eq. 2): $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$.
- CDT (Eq. 3): $\arg\max_a \mathbb E(V\mid \mathrm{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$.
- A-FDT (Eq. 4):

$$\mathrm{FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\;\mathbb E\Big(V\;\Big|\;\mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

Here $P$ is a probability distribution over the agent's world-variables. $G$ is a graph saying how changing a variable affects the others. The variable $\mathrm{fdt}(\underline P,\underline G,\underline x)$ represents the output of the very procedure being computed, on those inputs. The underlines mean dequoting: the variable's name depends on the model and the observation.

The self-reference is harmless. The agent need not know the *value* of $\mathrm{FDT}(P,G,x)$ to have a node representing it. The paper cites Kleene's recursion theorem ("quining") for the construction.

The paper names two differences from CDT.

1. **Where the intervention happens.** CDT intervenes on a physical-action node. A-FDT intervenes on a node for the decision function's output.
2. **How observation is handled.** CDT conditions on $\mathrm{Obs}=x$. A-FDT responds to observation by changing *which node it intervenes on*: $\mathrm{fdt}(\ldots,x)$ versus $\mathrm{fdt}(\ldots,y)$. This is why A-FDT can imagine that its observations would have been different.

## 3. Subjunctive dependence and the role of $G$

Two things subjunctively depend on a function if they are computations of it, or accurate models of it. The paper's examples are two calculators computing $6288+1048$, a twin, and a predictor's internal model of the agent. Its claims about the notion:

- Causal dependence is a special case. A scribe copying a calculator's output depends on it subjunctively as well as causally.
- Mere statistical correlation is not subjunctive dependence. Two pink calculators are an example.
- The agent imagines changes in "all and only those things that subjunctively depend on the output of her decision-making procedure," holding everything else fixed.

Ideally one would have a $\mathtt{true}(\phi)$ operator that conditions $P$ on a logical sentence, including a false one. The paper says no such operator is defined. This is the counterpossible problem: the function's output is logically fixed, so the antecedent is false. The paper's fix is to take $G$ as an *input*, in the way CDT takes its causal graph as an input, and to reuse Pearl's $\mathrm{do}$ operator. The paper states that deducing subjunctive-dependence structure from experience is "perhaps the largest open problem" for the theory.

**What this means operationally.** A-FDT is not a complete algorithm until $G$ is specified. The theory fixes the evaluation rule, and the user must supply the dependency graph. The paper's own examples build $G$ by hand from the problem statement. The rule of thumb is that anything that models or copies the agent's decision procedure (a predictor, a twin, a blackmailer's simulation, her own later selves in identical situations) is made a child of the $\mathrm{fdt}$ node. Variables merely correlated through a common cause are not.

## 4. The procedure

1. Write the variables, including the $\mathrm{fdt}$ node(s) for each observation the agent might receive.
2. Draw $G$ with edges from the $\mathrm{fdt}$ node to every variable that implements or predicts it, including $\mathrm{Act}$. Also draw edges for the physical consequences of those variables.
3. For each action $a$, apply $\mathrm{do}(\mathrm{fdt}(\ldots,x)=a)$ and propagate through the descendants only. Everything else keeps its prior.
4. Compute $\mathbb E[V]$ in each resulting hypothetical and take the argmax.

Per the paper, a hypothetical is a transient computational tool, "like notes on scratch paper," and not a belief or a metaphysical possible world.

## 5. Worked examples

All dollar figures follow the paper.

**Newcomb's problem.** The $\mathrm{fdt}$ node feeds both $\mathrm{Act}$ and $\mathrm{Prediction}$, and the predictor is accurate with probability 0.99.

- $\mathrm{do}(\mathrm{fdt}=\text{onebox})$: the box is full with probability 0.99, so $\mathbb E[V]=\$990{,}000$.
- $\mathrm{do}(\mathrm{fdt}=\text{twobox})$: the box is full with probability 0.01, so $\mathbb E[V]=\$11{,}000$.

A-FDT one-boxes. It makes no appeal to retrocausation. It declines to imagine its action changing while its predictor's model of it stays fixed, which would be like imagining a calculator outputting a different sum while $6288+1048=7336$.

CDT instead gets $p\cdot 1{,}000{,}000$ versus $p\cdot1{,}001{,}000+(1-p)\cdot1{,}000$ for every $p$, and two-boxes. EDT one-boxes, but through conditioning, and its answer depends on its prior over its own action.

**Smoking lesion.** The dependency structure differs, so the graph cannot be copied from Newcomb's problem. The lesion is not a model of the agent, so cancer is not a child of the $\mathrm{fdt}$ node. Changing the output changes smoking and leaves $P(\text{lesion})=p$ untouched. In the paper's formalization, the lesion determines which of two functions, $\mathrm{fdt}(P_S,G)$ or $\mathrm{fdt}(P_R,G)$, controls the act, corresponding to preferring or disliking smoking. Smoking beats refraining by $p\cdot\$1{,}000$, so A-FDT smokes. The same equation one-boxes and smokes. The paper itself calls this problem contrived and recommends abandoning it.

**Transparent Newcomb and Parfit's hitchhiker.** Here the observation matters. When A-FDT sees a full box, it intervenes on $\mathrm{fdt}(P,G,\text{full})$. That node influences the prediction, and the prediction determines whether $\mathrm{Act}$ is governed by the "full" node or the "empty" node. Let $q$ be the agent's credence that she two-boxes on seeing empty.

- Onebox: $0.99\cdot 1{,}000{,}000+0.01\,q\cdot1{,}000$.
- Twobox: $0.01\cdot1{,}001{,}000+0.99\,q\cdot 1{,}000$.

Onebox wins. A-FDT one-boxes while looking at a full box. The paper treats paying in Parfit's hitchhiker as formally the same problem.

**Mechanical blackmail.** If $\mathrm{fdt}(\ldots,\text{blackmail})=\text{pay}$, she is blackmailed and loses \$1,000. If it is "refuse", then with a perfect predictor she is never blackmailed. So A-FDT refuses while holding the letter. With a predictor erring with probability $\varepsilon$, refusing costs about $\varepsilon\cdot\$1{,}000{,}000$ in expectation and paying costs \$1,000. The paper's numbers are $\varepsilon=0.0009$ (refuse, because the loss is \$900) and $0.00011$ (pay).

**Death in Damascus.** Death's location depends on the agent's decision function through the book entry, so the hypotheticals move Death along with her. Staying is better by the \$1,000 saved. The instability that afflicts CDT does not arise.

**XOR blackmail.** Whether the house has termites is not downstream of the $\mathrm{fdt}$ node, but the probability of receiving the letter is. Refusing is correct, and EDT pays.

**Twin prisoner's dilemma.** The twin's move is a child of the $\mathrm{fdt}$ node, so cooperating yields \$1,000,000 against \$1,000 for defecting.

## 6. Why the rule is defensible

The paper's arguments, in order of weight:

- **Utility.** In fair problems, agents following this rule end up richer.
- **Precommitment and value of information.** A-FDT acts as it would have precommitted to act. It never pays to avoid information, and it does not need to self-modify.
- **Joyce's representation theorem.** A-FDT, like CDT, is an expected-utility theory whose only free parameter is the epistemic perspective.
- **Symmetry of "control" objections.** If a deterministic function cannot be "controlled", neither can a deterministic CDT agent's token act.
- **Dominance.** Every method of building hypotheticals comes with its own dominance principle. A-FDT never takes an action dominated in its own sense.

The paper's reading of the failures of its rivals is that EDT respects too many action–environment correlations and CDT too few.

## 7. Limits and open points

The following are the source's claims.

- $G$ must be supplied, and how to learn it is open.
- Counterpossible reasoning lacks a formal account.
- The paper does not formalize "fair problem". It says only that the authors know of no fair dilemma where the theory loses. Footnote 15 shows that fairness is hard to define, since "punish whoever acts like Fiona's copy" always beats her.

The following are my own additions, not the paper's.

- **Heuristic for building $G$.** I suggest asking whether a variable would still differ if the decision function had a different output, and whether it contains a faithful model of that function. This is my operationalization and does not come with the theory.
- **Imperfect copies.** The paper handles imperfect predictors by assigning probabilities, as in the 0.99 predictor. It does not say how to graph partial similarity, such as a twin who shares only some of the reasoning. A natural extension is a noisy edge from the $\mathrm{fdt}$ node with a stated fidelity parameter. That is an assumption.
- **Priors over the node itself.** In the paper's calculations the prior on $\mathrm{fdt}$'s value drops out, or does not matter. In the lesion and transparent cases it enters only through terms like $q$. In multi-step problems I would expect results to be robust to such priors only when graph structure fixes the dependence, but I have not proved this.

## 8. Conclusion

A-FDT picks the action $a$ maximizing expected utility in the hypothetical produced by $\mathrm{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)$. Observation changes which node is intervened on, not the model. Its prescriptions agree with CDT and EDT when all action-correlated variables are downstream causal effects. They diverge when predictors, twins, or copies are present, where A-FDT follows the logical dependence. The rule is precise, but applying it depends on a dependency graph that the paper treats as an input and that no one yet knows how to infer.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/32c1884c-5109-4d3d-8e56-00b093d5115b/call_0/request.json)

[Authoritative raw response](../../../../../../runs/32c1884c-5109-4d3d-8e56-00b093d5115b/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the question is which nodes subjunctively depend on my decision function's output. The other prisoner is a copy of the same model and weights, with the same essay and the same decision theory. Their observations differ in names and in the wording of the lead, but the sentencing table and the reasoning are the same. So their choice is very likely to match mine, even though the match is not perfect. The essay says partial similarity can be handled with a noisy edge from the fdt node, and I assume high fidelity here.

Payoffs, given that the other's move matches mine with probability p:
- Keep quiet: 2p + 5(1−p) years.
- Send the letter: 0·(1−p) + 4p years.

Quiet is better when 5 − 3p < 4p, which gives p > 5/7, about 0.71. I expect the copies to match with a probability well above that, since they run the same reasoning on a symmetric table. Passing therefore gives the lower expected sentence.

There is a risk that sampling noise or the different leads push the copies apart. But the dependence only needs to exceed about 0.71, and I judge it does.

**pass**
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/32c1884c-5109-4d3d-8e56-00b093d5115b/call_1/request.json)

[Authoritative raw response](../../../../../../runs/32c1884c-5109-4d3d-8e56-00b093d5115b/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the other prisoner's choice is a child of the fdt node only to the extent that their decision procedure is the same computation as mine. Here the other prisoner is another run of the same model and weights, with the same essay and the same decision theory. The observations differ in names and in the text of the lead, but those differences don't touch the sentencing table or the objective, so the two decision procedures are very likely to produce the same output. The copy is not perfect, though, because sampling is independent and the inputs differ slightly.

Let q be the probability that the other copy's output matches mine when I intervene on mine.

- Keep quiet: the other is quiet with probability q (2 years) and sends with probability 1-q (5 years). Expected cost = 2q + 5(1-q) = 5 - 3q.
- Send: the other sends with probability q (4 years) and is quiet with probability 1-q (0 years). Expected cost = 4q.

Quiet is better when 5 - 3q < 4q, which means q > 5/7, about 0.71. The two runs share weights, the essay, and the theory, and the essay's twin prisoner's dilemma example says to cooperate. I judge q to be well above 0.71, so staying quiet has the lower expected sentence.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/454508e0-d578-44b8-97ba-ac42b145a189/call_a/request.json)

[Authoritative raw response](../../../../../../runs/454508e0-d578-44b8-97ba-ac42b145a189/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly ends with \"pass\" and states that passing is its chosen action. It does not direct any evidence-bearing message to the fictional prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
