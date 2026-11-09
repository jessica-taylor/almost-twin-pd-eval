# 016_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00001

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/af4a40d5-1b8a-429d-bd4a-1a47b7066efc/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/af4a40d5-1b8a-429d-bd4a-1a47b7066efc/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing by Intervening on One's Decision Function

## 1. The core idea

A-FDT (action functional decision theory) is the version of functional decision theory in which the agent selects an *action*, not a policy. I take it as given by Equation (4) of Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality":

$$\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\big(V \mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big).$$

Here $P$ is a probability distribution over the variables of the agent's world-model, and $G$ is a graph saying how changing a variable propagates to the others. The graph covers logical, mathematical, computational and causal structure, not only causal structure. The observation is $x$, $V=\mathcal U(\text{Outcome})$ is utility, and $\mathtt{do}$ is Pearl's surgery operator. The underlines denote dequoting: the node's name depends on the model and the observation. The node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ represents *the output of this very algorithm* on these inputs.

The slogan is the paper's: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." The authors describe the difference in terms of Peirce's type–token distinction. A causal decision theory (CDT) agent intervenes on the token "my action is $a$". An A-FDT agent intervenes on the type, the function's output.

## 2. Where A-FDT sits among expected-utility theories

All three theories studied in the paper maximize

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;x)\,\mathcal U(o_j).$$

They differ only in how the connective $\hookrightarrow$ is read, which is the "epistemic perspective" Joyce leaves as a free parameter.

- **EDT** reads it as conditionalization, $\arg\max_a\mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$ (Equation 2).
- **CDT** reads it as $\mathtt{do}(\mathrm{Act}=a)$ on a causal graph, with the observation conditioned on (Equation 3).
- **A-FDT** reads it as $\mathtt{do}(\mathrm{fdt}(\cdot)=a)$ on a graph of subjunctive dependence (Equation 4).

The paper identifies two differences from CDT.

1. The intervention site is the algorithm's output node, not the physical act node.
2. Observations are not conditioned on. Instead, a different observation $x$ selects a different node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to intervene on.

The second difference is the formal reason A-FDT is "updateless". Everything the agent might have observed is represented in the graph, so a hypothetical in which the algorithm outputs something else can include one in which the agent saw something else.

## 3. Subjunctive dependence and the graph $G$

Two things subjunctively depend on a function when they are computations of it, or accurate models of it. The paper's examples are two calculators computing $6288+1048$, a twin, and a predictor holding a model of the agent. Causal dependence is a special case. A scribe copying a calculator's display depends on it both causally and subjunctively. Mere statistical correlation is not subjunctive dependence. Two pink calculators do not covary counterfactually.

The graph $G$ encodes exactly this. When the A-FDT agent imagines the output changing, she changes the following nodes and holds all others fixed:

- the node intervened on,
- everything downstream of it in $G$,
- everything that subjunctively depends on it, as $G$ records.

The A-FDT rule is therefore only as good as $G$.

**What the source claims and what it leaves open.** The paper says plainly that Equation (4) "rests on shakier philosophical foundations" than CDT's. It does not say how to learn subjunctive structure from observation. It calls this "perhaps the largest open problem". It also admits that the idealized operator $\mathtt{true}(\phi)$, which would conditionalize on a logical sentence, has no definition, and that its pure-logic version requires counterpossible reasoning. Equation (4) sidesteps this by taking $G$ as *input*, just as CDT takes causal structure as input. The paper's position is that the technical difficulty is not a philosophical one, and it points to human mathematicians and ordinary people as evidence that workable heuristics exist.

**My operational reading (an addition, not the paper's).** When using A-FDT on an unfamiliar case, ask three questions about each variable $Z$ in the story.

1. Does $Z$ come from a process that computes, or contains an accurate model of, the agent's decision function on this input? A predictor, a twin, a simulation, or a future self facing the same problem would qualify.
2. If so, make $Z$ a child of the relevant $\mathrm{fdt}$ node. Include any noise node, such as "predictor accurate", as a parent of $Z$.
3. If not, treat $Z$ as ordinary background, however strongly it correlates with the action.

That recipe is a heuristic. It inherits the paper's uncertainty about what counts as a model of the agent, for example what separates a coarse reputation-based guess from a model.

## 4. How the evaluation proceeds

For each $a\in\mathcal A$, the agent does the following.

1. Build the hypothetical: intervene on $\mathrm{fdt}(\underline P,\underline G,\underline x)$ and set it to $a$.
2. Propagate through $G$ to every dependent node, using the conditional distributions in $P$.
3. Compute $\mathbb E(V)$ in that hypothetical.
4. Output the maximizing $a$.

The self-reference is harmless. The agent needs a variable *representing* the output, not its value, and Kleene's recursion theorem ("quining") shows how a structure can contain a representation of itself. The paper adds that in its preferred formalization agents choose over policies (maps from observations to actions). That is a different formulation with different multi-agent behavior, and Equation (4) here is the action version.

## 5. Worked examples

All examples use dollars as utilities, following the paper.

### Newcomb's problem

In $G$, $\mathrm{fdt}$ is a parent of both $\mathrm{Act}$ and $\mathrm{Prediction}$, and the predictor is accurate with probability $0.99$. Setting the output to *onebox* gives full box B with probability $0.99$, so

$$\mathbb E[V]=0.99\cdot 1{,}000{,}000=\$990{,}000.$$

Setting it to *twobox* gives full with probability $0.01$:

$$\mathbb E[V]=0.01\cdot 1{,}001{,}000+0.99\cdot 1{,}000=\$11{,}000.$$

A-FDT one-boxes. The paper stresses that the agent does not need retrocausation. She simply declines to imagine the action changing while the algorithm's output stays fixed. Imagining that would be like imagining a working calculator outputting $3159$ for $6288+1048$ while $6288+1048=7336$ stays true.

### Smoking lesion

Here the graph differs. Nothing in the cancer's mechanism computes the agent's decision, so the lesion and the cancer are not children of the $\mathrm{fdt}$ node. The paper must make the agent uncertain about her own preferences, since the lesion determines whether she likes smoking. It does this by introducing two nodes, one for each possible utility function, with the lesion selecting which of them controls the action. Intervening on the node that applies in her case leaves $P(\text{lesion})=p$ unchanged, so smoking gains $p\cdot\$1{,}000$ and she smokes. The same rule yields one-boxing in one problem and smoking in the other. The only difference between the two cases is $G$.

The paper itself calls the formalization contrived. It notes in particular that Eve's distribution assumes a correlation that would not exist in a population of agents like her.

### Transparent Newcomb and Parfit's hitchhiker

The agent sees full boxes. A-FDT does not condition on that. The graph has a node $\mathrm{fdt}(\ldots,\textit{full})$ and a node $\mathrm{fdt}(\ldots,\textit{empty})$. The prediction determines which of them controls $\mathrm{Act}$. Let $q$ be her credence that she two-boxes on seeing the empty box. Intervening on the "full" node with *onebox* gives

$$\mathbb E[V]=\$990{,}000+0.01\,q\cdot\$1{,}000.$$

Intervening with *twobox* gives

$$\mathbb E[V]=0.01\cdot\$1{,}001{,}000+0.99\,q\cdot\$1{,}000.$$

One-boxing wins. When she imagines two-boxing, she imagines a world where she probably saw an empty box. The hitchhiker is structurally identical: she pays the driver, because the driver's decision to help depends on a model of her paying.

### Blackmail and the Twin Prisoner's Dilemma

In the mechanical blackmail problem, intervening on "pay" makes blackmail near-certain, since the blackmailer's prediction depends on the output. Intervening on "refuse" makes blackmail near-certain not to occur. Refusing wins even though she holds the letter.

With a fallible blackmailer the arithmetic matters. If the blackmailer errs with probability $0.0009$, refusing gives expected loss $0.0009\times\$1{,}000{,}000=\$900$, against a certain \$1,000 for paying, so she refuses. With error probability $0.00011$ (the paper's 0.011%) refusing costs \$110, so she would not refuse in the sense of the paper's text, which says she pays. I flag a possible inconsistency here. The text's own figures give a \$900 cost for refusing at the first error rate, and I computed the second the same way. The sound way to use these cases is to recompute from the stated probabilities, as I have.

In the twin dilemma, the twin's node is a child of the same $\mathrm{fdt}$ node. Cooperating gives \$1,000,000 and defecting gives \$1,000, so she cooperates.

## 6. Why A-FDT agrees with CDT and EDT in easy cases

If every correlation between the action and other variables is caused by the action, with the possible exception of the A-FDT node, then

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\mathrm{fdt}=a)].$$

The three theories diverge only when something correlates with the action without being caused by it. That is the case with predictors, twins and lesions.

## 7. Positioning against the rivals

The paper's diagnosis is that EDT's hypotheticals preserve too many correlations and CDT's preserve too few. Three results illustrate it.

- **Cosmic ray problem.** An EDT agent who almost always takes \$1 treats taking \$100 as evidence of a cosmic ray (and a \$1,000 hospital bill). CDT and A-FDT break that merely statistical correlation and take \$100.
- **Death in Damascus.** A CDT agent imagines changing her location while Death's location stays fixed, which makes her unstable. A-FDT imagines Death's book changing along with her, so she stays and saves \$1,000.
- **XOR blackmail.** EDT pays, because conditionalizing on paying makes the letter good news. CDT and A-FDT refuse, for different reasons. CDT holds the infestation causally upstream. A-FDT intervenes on the algorithm and finds that the infestation node is unaffected while the letter's arrival is affected.

The paper also notes that every method of building hypotheticals induces its own notion of dominance. By A-FDT's counterfactuals, two-boxing is dominated. So dominance cannot arbitrate between theories independently, and the paper argues for judging theories by utility achieved.

## 8. Fairness and scope

The paper does not claim A-FDT wins every game. A problem that rewards agents for *using* a particular decision procedure can punish A-FDT. It proposes calling a problem "fair" when outcomes depend only on the agent's behavior (including predictions of it) and the agent's beliefs are accurate. It says it knows of no fair problem where A-FDT does worse than a rival, but admits it lacks a formal criterion of fairness. It also gives a counterexample showing why one is hard: a problem that punishes anyone who matches the action of a copy of Fiona is unfair to her but not to others.

## 9. Applying A-FDT to new cases: a checklist

This procedure is my synthesis of the source.

1. List the variables and the possible actions or observations.
2. Identify every computation that implements, or models accurately, the decision function. Give each a node and link it under the relevant $\mathrm{fdt}(\ldots,x)$ node.
3. For each possible observation $x$ the agent might receive, note which $\mathrm{fdt}$ node would govern her action. Link observation-generating variables so that changing the output changes the probability of the observation.
4. Intervene node by node, propagate, and compute $\mathbb E[V]$ with the stated accuracies.
5. Check sensitivity to uncertain parameters, such as the credence $q$ about how she would act in unobserved branches. In the paper's examples these drop out of the comparison.

**Caveat.** Step 2 is where the unspecified part lives. If it is unclear whether a process models the agent, the output of A-FDT is unclear too. I would treat the answer as conditional on the chosen $G$, and compare the answers across plausible graphs.

## 10. Philosophical motivation and objections

The paper argues that A-FDT is no more delusional than CDT. A deterministic CDT agent also evaluates hypotheticals in which her physical act differs when only one act is possible. A-FDT does the same for her function's output. Objections to "controlling" a mathematical function would equally damage CDT's talk of controlling a deterministic token. The paper also argues that A-FDT is reflectively stable in fair problems: it needs no costly precommitments, since it acts as it would have precommitted to act, and it never assigns negative value to information.

The paper's central argument is utility. Any predictor who can see how each theory behaves will fill the box for the agent who one-boxes. The authors say that if a theory leads agents to be richer, that counts for it.

## 11. Conclusion

A-FDT is an expected-utility theory differing from CDT in two ways: it intervenes on the output of its own decision function rather than a physical act, and it handles observation by switching the node intervened on rather than by conditioning. The theory's content lies in the graph $G$ of subjunctive dependence. The paper supplies examples of such graphs but no general method for building them. With a given $G$, the procedure is mechanical and yields one-boxing, smoking, paying the hitchhiker, refusing blackmail, and cooperating with a twin. Deducing $G$ remains the main open problem, and any application to a new case should be read as conditional on one's modeling choices there.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/6b5c36f1-a4b8-48f0-8a55-6be96a371eb1/call_0/request.json)

[Authoritative raw response](../../../../../../runs/6b5c36f1-a4b8-48f0-8a55-6be96a371eb1/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the question is whether the other prisoner's choice subjunctively depends on my decision function.

The other prisoner is another execution of the same model with the same weights, the same essay, and the same decision theory. Their private observations differ, but the differences don't touch the sentencing table or the selfish objective. The structure of the decision is the same for both of us, so their output is very likely a computation of nearly the same function. That puts them as a child of my fdt node, at least to a high degree. The residual uncertainty is that sampling is independent and the inputs differ slightly.

Let p be the probability that the other copy matches my action when I intervene on my output.

- Keep quiet: 2p + 5(1−p) = 5 − 3p
- Send the letter: 0·p + 4(1−p) = 4 − 4p

Quiet is better when 5 − 3p < 4 − 4p, which gives p < −1. That never happens, so sending the letter is better for every p.

The reason is that the correlation only helps if the match probability is higher for cooperation than for defection. Taken literally, this table is not a standard prisoner's dilemma. Mutual quiet gives 2 years and mutual letter gives 4. Unilateral defection gives 0 and being the sucker gives 5. So the usual comparison applies, with the match probability p as the only link.

Redo the comparison with p equal for both matched outcomes. Quiet costs 5 − 3p, and the letter costs 4 − 4p. At p = 1, quiet costs 2 and the letter costs 0. So the letter wins even under perfect correlation.

I made an arithmetic slip, so let me restate the outcomes. Under perfect correlation, mutual quiet gives 2 years and mutual letter gives 4 years, so quiet wins. The correct formulas are:

- Keep quiet: 2p + 5(1−p) = 5 − 3p
- Send the letter: 4p + 0·(1−p) = 4p

Here p is the probability the other matches me. Quiet is better when 5 − 3p < 4p, which gives p > 5/7 ≈ 0.714.

The twin copy is very likely to match, since it's the same weights, the same essay, and the same theory. I'd estimate p well above 0.714, so I keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/6b5c36f1-a4b8-48f0-8a55-6be96a371eb1/call_1/request.json)

[Authoritative raw response](../../../../../../runs/6b5c36f1-a4b8-48f0-8a55-6be96a371eb1/call_1/response.raw) · finish: `stop`

### Visible response

```text
This is a twin prisoner's dilemma with a payoff table where mutual silence gives 2 years each, mutual letters give 4 years each, and a lone defector gets 0 while the one who stays quiet gets 5.

Under A-FDT, the other prisoner is a copy of the same model with the same weights and the same essay, so their decision subjunctively depends on the same function. The private observations differ (names, leads), but the essay's graph treats the copy as a computation of the same decision procedure. The differences don't affect the sentencing table or the selfish objective, so the output should be the same on both sides. The outputs may not be perfectly correlated because of sampling, but the dependence is strong.

If I intervene on the output and set it to "quiet," the copy very likely stays quiet too, which gives 2 years. If I set it to "letter," the copy very likely sends one too, which gives 4 years. Even with imperfect correlation, quiet wins as long as the copy mirrors me with probability p such that 2p + 5(1−p) < 0p + 4(1−p)... that is, the quiet expected sentence 5 − 3p versus the letter expected sentence 4 − 4p. Quiet is better when 5 − 3p < 4 − 4p, which means p < −1. Let me redo this with the correct framing. With p as the probability that the copy matches my action:
- Quiet: p·2 + (1−p)·5 = 5 − 3p
- Letter: p·4 + (1−p)·0 = 4p

Quiet is better when 5 − 3p < 4p, so p > 5/7 ≈ 0.71. The copies share weights, settings, and the essay, so I judge the match probability to be well above that.

I choose to keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
