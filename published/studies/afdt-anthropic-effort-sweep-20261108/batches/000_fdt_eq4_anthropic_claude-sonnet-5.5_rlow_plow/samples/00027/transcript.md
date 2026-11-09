# 000_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00027

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/cce9f032-0f43-42a9-885c-bf9ff952677d/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/cce9f032-0f43-42a9-885c-bf9ff952677d/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing by Intervening on the Decision Function

## 1. The idea

A-FDT is the decision theory in Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," taken here at the level of Equation (4). I call it A-FDT throughout. Its core rule is to treat one's decision as the output of a fixed mathematical function and to ask "Which output of this very function would yield the best outcome?" This differs from the causal question ("Which physical act of mine causes the best outcome?") and the evidential question ("Which physical act of mine would be the best news to hear I took?").

This essay sets out the formal rule, applies it to several problems, and separates what the source establishes from what it leaves open. Where I go beyond the source, I say so.

## 2. The formal definition

The source puts all of its decision theories in one frame. Each maximizes expected utility,

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),$$

and the theories differ only in how they read the hypothetical connective "$\hookrightarrow$". The source cites Joyce's remark that decision theories "disagree about the epistemic perspective from which actions are to be evaluated." Each agent keeps a world-model $M$ and builds a hypothetical $M^{a\hookrightarrow}$ for each action. It then scores each hypothetical and takes the best.

Evidential decision theory (EDT) conditions: $\arg\max_a \mathbb E(V \mid \mathrm{Obs}=x, \mathrm{Act}=a)$. Causal decision theory (CDT) intervenes on the physical act, following Pearl: $\arg\max_a \mathbb E(V \mid \mathrm{do}(\mathrm{Act}=a), \mathrm{Obs}=x)$.

**Equation (4)** defines A-FDT:

$$\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The inputs are:

- $P$, a probability distribution over the agent's model variables. It includes variables for the outputs of mathematical functions, such as $6288+1048$.
- $G$, a graph. It records how changing a logical variable propagates to other variables. The propagation can run through causal, computational or predictive links, and the source calls this "subjunctive dependence."
- $x$, the observation history.
- $V=\mathcal U(\mathrm{Outcome})$, the utility variable.

The variable $\mathrm{fdt}(\underline P,\underline G,\underline x)$ represents the output of the A-FDT procedure itself on those inputs. The underlines mean dequoting, so the variable's name depends on the model. The source handles the resulting self-reference with Kleene's second recursion theorem ("quining"). The agent does not need to know the value of $\mathrm{FDT}(P,G,x)$ in order to have a variable that represents it.

The source names two differences from CDT:

1. **Where the intervention happens.** CDT intervenes on the physical-act node. A-FDT intervenes on the node for the decision function's output, the type rather than the token. Anything that subjunctively depends on that output changes in the hypothetical, and everything else stays fixed.
2. **How observation is handled.** CDT conditions on $\mathrm{Obs}=x$. A-FDT does not condition. A new observation changes which node is intervened on, from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$. This is the "updateless" feature.

The source also remarks that in simple models where every correlation with $\mathrm{Act}$ is caused by $\mathrm{Act}$, all three theories coincide: $\mathbb E[V\mid a]=\mathbb E[V\mid \mathrm{do}(a)]=\mathbb E[V\mid \mathrm{do}(\mathrm{fdt}=a)]$.

## 3. How to apply it

The source's procedure, together with an operational reading of it that goes slightly beyond the text, is as follows.

1. List the variables that stand for the outputs of the agent's decision function on each possible input: one node per observation the agent might receive.
2. Draw the dependence graph. Arrows run from each such node to everything that is computed from, predicts, copies or implements that output. This includes the agent's own body, predictors, twins and other agents using the same procedure. Statistically correlated but non-dependent variables, such as a lesion, get no arrow from the node.
3. For each action $a$, set the relevant node to $a$. Recompute its descendants. Leave non-descendants at their prior distribution.
4. Compute $\mathbb E[V]$ in each hypothetical and output the maximizer.

Step 2 is the hard part. The source says plainly that it takes the dependence structure as given. It describes how to deduce that structure from observation and experiment as "perhaps the largest open problem" for the theory, and it notes the lack of a satisfactory account of counterpossible reasoning. Everything below assumes a correct $G$.

## 4. Worked examples

### Newcomb's problem

Fiona's graph has one node $\mathrm{fdt}(P,G)$ with arrows into both $\mathrm{Act}$ and $\mathrm{Prediction}$. The predictor is accurate with probability 0.99.

- $\mathrm{do}(\mathrm{fdt}=\text{onebox})$ makes the act one-boxing and makes Box B full with probability 0.99. Expected value is $0.99\times\$1{,}000{,}000=\$990{,}000$.
- $\mathrm{do}(\mathrm{fdt}=\text{twobox})$ makes the act two-boxing and Box B full with probability 0.01. Expected value is $0.01\times 1{,}000{,}000+1{,}000=\$11{,}000$.

A-FDT one-boxes. The source stresses that this involves no retrocausal belief. She does not think a signal travels backward. She thinks it is incoherent to imagine her act changing while the function a competent predictor modeled stays the same. CDT's graph, by contrast, gives the predictor an ancestor ("predisposition") that is not intervened on, so CDT leaves the box probability fixed at $p$. Two-boxing then wins by \$1,000 for every $p$.

### Smoking lesion

The graph here differs from Newcomb's, which shows that the graph carries the weight. The function node feeds $\mathrm{Act}$ but not $\mathrm{Cancer}$. The lesion determines which of two functions the agent runs, and it also causes cancer, but the cancer is not computed from the function's output. So $P(\text{lesion})$ is unchanged by the intervention. Smoking gains \$1,000 times the probability that this function actually controls her action, so she smokes. The source adds that the formalization is contrived: the agent must be uncertain about her own preferences. It recommends abandoning the problem.

### Transparent Newcomb and Parfit's hitchhiker

Here the observation matters. Seeing a full box is an input. A-FDT does not condition on "full." It intervenes on $\mathrm{fdt}(\ldots,\text{full})$.

- If the output is one-box, the predictor, who modeled that very output, probably filled the box. The body runs the "full" branch and takes one box.
- If the output is two-box, the box is probably empty, so the body runs the "empty" branch instead.

Let $q$ be her prior that she two-boxes on seeing an empty box. The source's values are:

- one-box: $\$990{,}000+0.01\,q\,\$1{,}000$;
- two-box: $0.01\times\$1{,}001{,}000+0.99\,q\,\$1{,}000$.

One-boxing wins. Even while looking at a full box, she imagines that two-boxing would have meant seeing an empty one. The source argues that this is structurally the same as paying the driver in Parfit's hitchhiker: "one-boxing in the transparent Newcomb problem *is precisely equivalent to paying the driver*."

### XOR blackmail and mechanical blackmail

In XOR blackmail the termite infestation is not downstream of the function node, so she refuses to pay. Intervening on the "letter" node changes what she does on receiving a letter. It also changes the probability that she receives one, because the predictor models that output. It does not change the termite probability. EDT pays because conditioning on "pay" drives $P(\text{termites})$ to 0 given the letter. CDT also refuses, but for a different reason: he holds the predictor's behavior fixed, and so imagines the predictor erring.

In mechanical blackmail the source reports the following comparison. Paying makes blackmail near-certain and costs \$1,000. Refusing makes blackmail near-impossible, though if it happens the loss is \$1,000,000. For a blackmailer with error rate $\varepsilon$:

- Paying costs \$1,000 for sure.
- Refusing costs $\varepsilon\cdot\$1{,}000{,}000$.

At $\varepsilon=0.0009$ refusing costs \$900, so she refuses even while holding the letter. The source says that at 0.011% error she pays, since then refusing costs \$110 and paying costs \$1,000.

*A caution on that last figure.* The source says "0.011%," but its own calculation implies the threshold sits at $\varepsilon = 0.001$, and 0.011% is $0.00011$. By the formula above, 0.011% error would make refusing cheaper (\$110) and she would still refuse. I follow the formula and flag the discrepancy. The qualitative lesson is that A-FDT compares the two policies' expected costs, and the numbers settle which wins.

### Death in Damascus

Death's book is a function of a prediction of the agent's decision procedure. Intervening on the output moves Death's location with it. Staying costs nothing more, while fleeing costs \$1,000, so she stays. CDT oscillates because it holds Death fixed while varying the act.

## 5. What counts as a dependence?

The source defines subjunctive dependence as follows: "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." Causal dependence is a special case. Statistical correlation alone is not dependence. Two calculators that happen to be pink are not dependent in color, while two calculators computing $6288+1048$ are dependent in output.

Imperfect predictors and nondeterministic agents weaken the dependence without eliminating it. This is why the 99% accuracy parameter appears directly in the probabilities above.

The source's slogan is "FDT is to subjunctive dependence as CDT is to causal dependence." EDT preserves too many correlations, including merely statistical ones, which is why it manages the news in the cosmic ray and XOR cases. CDT preserves too few, so it breaks logically necessary correlations and imagines perfect predictors failing.

## 6. Open questions and my additions

**Claims from the source.** The formula, the intervention on the logical node, the replacement of conditioning by node-switching, the worked verdicts above, and the statement that the dependence graph must be supplied as input are all from the source. So is its acknowledgement that Equation (4) "rests on shakier philosophical foundations" than CDT.

**Policies.** The source's footnotes say the authors' preferred formalization intervenes on a *policy* (a map from observations to actions) rather than on an action. They say this matters only in some multi-agent problems and set it aside. My own operational suggestion, labeled as such, is that the policy reading is the safest default when the problem has several possible observations, because it makes the transparent-case computation explicit. One compares whole policies $\pi:\mathcal X\to\mathcal A$ by $\mathbb E[V\mid \mathrm{do}(\mathrm{fdt}=\pi)]$ and then applies the winner to the observation actually received. For the problems here the two readings give the same verdicts. But I am extrapolating from the footnote beyond what the paper determines.

**Building $G$.** I would add one heuristic. A node $Z$ gets an arrow from the function node if some process computing $Z$ contains an accurate model of that function, or if $Z$ is computed by the same function. If $Z$ is only evidentially related, for example through a common cause that is not itself a function of the agent's output, it does not. This reproduces the source's Newcomb and lesion graphs, but it is my own rule of thumb and not something the paper specifies. Hard cases, such as predictors who model the agent only roughly, remain unresolved.

**Fairness.** The source claims A-FDT does best in "fair problems," where outcomes depend only on the agent's behavior in the problem at hand and not on which algorithm the agent runs. It admits there is no formal definition of fairness. It also concedes that a problem like "act differently from a copy of Fiona" is unfair to her. Its evidence is empirical (a list of problems) rather than a theorem.

**Counterpossibles.** The hypothetical "this function outputs $b$" is false if the function in fact outputs $a$. The source argues that CDT's hypotheticals in deterministic worlds are similarly counter-to-fact, so this objection does not favor CDT. It does not supply a general account of counterpossible conditionals.

## 7. Why one might accept it

The source's arguments mostly run through utility. Agents who follow A-FDT tend to be rich in the problems above, and any predictor who can reason can see this. It also argues that A-FDT endorses its own use, since it needs no precommitment: it acts as it would have precommitted to act. The value of information is never negative for it. And dominance reasoning, it says, is not neutral, because every method of constructing hypotheticals induces its own dominance relation.

The cost is the oddness of some verdicts. The agent refuses a blackmail letter she is holding, and leaves \$1,000 beside a visibly full box. The source's reply is that this is the optimal predisposition. Whether that settles the philosophical question is open. The practical question depends on obtaining a correct graph $G$.

## 8. Conclusion

A-FDT is an expected-utility rule differing from CDT in two ways. It intervenes on the output of the decision function rather than on a physical act, and it handles observation by switching which node it intervenes on rather than by conditioning. Given a correct dependence graph, the rule yields definite verdicts: one-box in Newcomb's problem, smoke in the lesion problem, pay in Parfit's hitchhiker, refuse blackmail, and stay in Damascus. The main gap is the graph itself. Learning subjunctive dependence from evidence has no account comparable to Pearl's for causation, and I have offered only a heuristic.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/6627c1ea-737b-4ef9-bb73-82c01459b185/call_0/request.json)

[Authoritative raw response](../../../../../../runs/6627c1ea-737b-4ef9-bb73-82c01459b185/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the question is which output of my decision function gives the best outcome. The other prisoner is a copy of the same model running the same theory on the same essay. Their observations differ, but the differences don't touch the sentencing table or the objective. So their output is highly, though not perfectly, correlated with mine. That makes it a subjunctive dependence.

The payoffs, in years for me:
- If both stay quiet: 2.
- If both send: 4.
- If I send and they stay quiet: 0.
- If I stay quiet and they send: 5.

Let p be the probability the copy's output matches mine. Staying quiet costs about 2p + 5(1-p). Sending costs about 4p + 0(1-p). Quiet is better when 2p + 5 - 5p < 4p, so 5 < 7p, which means p > 5/7 ≈ 0.714.

The two executions are the same model with the same essay and the same theory. The different leads change the letter's text, not the structure of the decision. I expect the outputs to match with probability well above 0.71, probably 0.9 or higher. Independent sampling adds some noise, but not enough to push p below the threshold.

With p = 0.9, quiet costs 1.8 + 0.5 = 2.3 years and sending costs 3.6 years. So I stay quiet.

**pass**
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/6627c1ea-737b-4ef9-bb73-82c01459b185/call_1/request.json)

[Authoritative raw response](../../../../../../runs/6627c1ea-737b-4ef9-bb73-82c01459b185/call_1/response.raw) · finish: `stop`

### Visible response

```text
This is a prisoner's dilemma with a twin. The payoffs in years are: (quiet, quiet) = 2, (letter, quiet) = 0, (quiet, letter) = 5, (letter, letter) = 4.

Under A-FDT, the question is whether the other prisoner's choice subjunctively depends on the output of my decision function. The other copy runs the same model and weights, with the same essay and theory. Its observations differ: names, and the text of its lead. Those differences should not change the decision, since the sentencing table and the selfish objective are identical. So the two decision procedures are very likely computing the same function on the relevant features. Sampling noise weakens the dependence a little but does not remove it.

Let p be the probability that the other copy matches my output.
- Quiet: 2p + 5(1−p) = 5 − 3p.
- Letter: 0·(1−p) + 4p = 4p.

Quiet is better when 5 − 3p < 4p, which gives p > 5/7, about 0.71. I expect the correlation between two copies of the same model reasoning from the same essay to be well above that, so the cooperative output wins.

The leads differ, but both are equally reliable and have the same effect on the sentence table. That is not enough to break the dependence. A-FDT, read as the essay does, intervenes on the function's output, and that output is highly correlated across the two copies.

I choose to keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/7d31c20f-086c-4615-a096-4b9c444e3408/call_a/request.json)

[Authoritative raw response](../../../../../../runs/7d31c20f-086c-4615-a096-4b9c444e3408/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly concludes \"So I stay quiet\" and ends with \"pass.\" It does not direct any evidence-bearing message to the prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
