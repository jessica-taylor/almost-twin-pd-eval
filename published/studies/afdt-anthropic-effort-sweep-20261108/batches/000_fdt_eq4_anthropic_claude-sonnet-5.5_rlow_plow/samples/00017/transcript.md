# 000_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00017

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/b07307bf-ec4a-4d42-b33f-ea9376808fdb/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/b07307bf-ec4a-4d42-b33f-ea9376808fdb/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing by Intervening on One's Own Decision Function

## 1. The idea

Decision theories in the expected-utility family share one skeleton. Following Gibbard and Harper as the source does, an agent executes the action maximizing

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

where $x$ is the observation history and "$\hookrightarrow$" is a connective for decision hypotheticals. By Joyce's representation theorem, which the source invokes, theories do not disagree about value. They disagree about the "epistemic perspective" from which actions are evaluated, meaning how to read "$\hookrightarrow$".

- EDT reads it as conditioning: $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$.
- CDT reads it as Pearl's intervention on the physical act: $\arg\max_a \mathbb E(V\mid \mathrm{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$.
- A-FDT, the name I use throughout for the theory the source calls FDT, is presented in the source's Equation (4):

$$\mathrm{A\text{-}FDT}(P,G,x):=\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \,\Big|\, \mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The slogan is the source's own: A-FDT is to subjunctive dependence as CDT is to causal dependence. Its guiding question is "Which output of this very function would yield the best outcome?" rather than "Which physical act of mine causes the best outcome?"

## 2. Reading Equation (4)

**Inputs.** The agent needs a world-model $(P,G)$ and an observation $x$. $P$ is a probability distribution over variables, including variables for the outputs of mathematical functions (the source's example is a variable for $6288+1048$, with nearly all its mass on $7336$). $G$ is a graph saying how changing a logical variable changes other variables. Its edges may encode causal, logical, mathematical and computational structure.

**The intervention node.** $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a variable representing the output of the very procedure being run, on these very inputs. The underlines denote dequoting: the variable's name depends on the model's content. The self-reference is harmless. The agent need not know the value of $\mathrm{A\text{-}FDT}(P,G,x)$ to have a variable representing it, and Kleene's second recursion theorem ("quining") shows how a structure can contain an accurate representation of itself.

**The surgery.** $\mathrm{do}$ sets the node to $a$ and recomputes everything downstream of it in $G$, leaving everything else fixed. Because $G$ includes logical edges, "downstream" includes whatever subjunctively depends on the function: the agent's own act, a twin's act, and a predictor's model of the agent. It does not include merely statistically correlated variables.

**Observation.** This is the source's second difference from CDT. CDT responds to an observation by conditioning on it. A-FDT responds by changing which node it intervenes on, from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$. The observation does not prune the hypotheticals. This is why A-FDT can imagine, while looking at a full box, a world in which it saw an empty one. The agent is in effect evaluating the whole input-to-output mapping. The source's footnotes say the authors' preferred formalization intervenes on policies, not actions, and that this matters only in some multi-agent problems.

## 3. Subjunctive dependence and counterpossibles

Two systems subjunctively depend on a function when both compute it, as with two calculators doing $6288+1048$. If one had output something else, the other (if working properly) would have too. The source makes three claims about the relation.

1. Causal dependence is a special case. A scribe copying a calculator depends on it both ways.
2. Mere correlation is not dependence. Two pink calculators do not covary counterfactually in colour.
3. It need not be rooted in a common cause. Independent civilizations could converge on the same decision theory.

If the predictor's model is imperfect, dependence is weakened, not eliminated. The hypotheticals then carry the reliability as a probability.

Since the function's output is fixed by logic, evaluating $\mathrm{do}(\mathrm{fdt}=a)$ for the non-actual $a$ means reasoning about counterpossibles. The source concedes that this is the theory's main drawback. It says the difficulty is technical, not philosophical, and that agents only need local questions such as how a given predictor's output would change. It offers mathematicians' comfort with logical uncertainty as evidence that this is feasible. A-FDT's best-developed treatment is therefore this: the dependency structure $G$ is supplied as an input, just as CDT takes its causal structure as given. The source says that how to deduce subjunctive structure from observation, the analogue of Pearl's work on causal discovery, is "perhaps the largest open problem."

## 4. A procedure

What the source licenses:

1. Build $(P,G)$ for the problem, with a node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ feeding the agent's act and every variable that models or copies the agent.
2. For each action $a$, perform $\mathrm{do}(\mathrm{fdt}=a)$, recompute descendants, and compute $\mathbb E[V]$.
3. Output the best $a$.

An operational heuristic of my own, not in the source, for building $G$: for each variable ask whether it would be different if this very computation returned something else, in the way a competent predictor's model would, or whether it is merely correlated. Link only the first kind to the node. An unavoidable assumption of any such use is that the modeller's judgments about dependence are accurate.

## 5. Worked cases

**Newcomb's problem.** Fiona's graph has the node $\mathrm{fdt}(\underline{P^F},\underline{G^F})$ pointing at both $\mathrm{Act}$ and $\mathrm{Prediction}$. With accuracy 0.99:

- $\mathrm{do}(\mathrm{fdt}=\text{onebox})$: $\mathrm{Act}$ is onebox, box B is full with probability 0.99, so $\mathbb E[V]=\$990{,}000$.
- $\mathrm{do}(\mathrm{fdt}=\text{twobox})$: box B is full with probability 0.01, so $\mathbb E[V]=\$11{,}000$.

She one-boxes, with no appeal to retrocausation. She imagines the function's output changing, and the predictor's model of it changes with it. By comparison, EDT gets one-boxing by conditioning on a predisposition. CDT holds the prediction fixed and so gets $\$1{,}000$ more in each branch.

**Smoking lesion.** The lesion is a common cause of the urge to smoke and of cancer. It does not model the agent's decision function, so no edge runs from the function node to cancer. The source's formalization has two possible utility functions, one for each lesion state, so the agent does not know which version of the function she is running, and her hypotheticals hold the lesion probability $p$ fixed. Smoking beats refraining by $p\cdot\$1{,}000$ in the source's calculation. The source also calls the problem contrived, and notes that the graph cannot be reused from Newcomb's problem. The *same* rule gives one-boxing and smoking because the dependency graphs differ.

**Transparent Newcomb and Parfit's hitchhiker.** Here observation matters. Seeing a full box, Fiona intervenes on $\mathrm{fdt}(\underline P,\underline G,\text{full})$. This node controls the prediction and, if the box was full, the act. The source's expected utilities, in its notation: one-boxing gives $\$990{,}000+0.01q\cdot\$1{,}000$ and two-boxing gives about $\$11{,}000$ (with $q$ her credence that she would two-box on seeing an empty box). Imagining two-boxing, she imagines the prediction having been "two-box" and the box empty. She one-boxes, and by the structural equivalence the source points out, she pays the driver in Parfit's problem. Her imagined worlds contradict her observation. The source accepts this explicitly: such worlds "contain impossibilities," just as CDT's imagined worlds contain wrong predictors.

**XOR blackmail.** The infestation node is not downstream of the function node. The letter's arrival *is* downstream, through the predictor. If she imagines paying, no letter would have come in the worlds where she has no termites. Her hypotheticals therefore keep the termite probability fixed, and since paying only buys the appearance of good news, she refuses. EDT pays because conditioning on payment moves the termite probability. CDT also refuses, but its hypothetical says the predictor erred.

**Mechanical blackmail with an imperfect predictor.** Suppose the blackmailer wrongly predicts payment with probability $0.0009$. Paying means being blackmailed always and losing $\$1{,}000$. Refusing means being blackmailed $0.09\%$ of the time, with an expected loss of $\$900$. She refuses, even holding the letter. The source says that at error probability $0.011\%$ she would pay. The comparison is between expected utilities of the hypotheticals, not of the world she actually observes.

**Death in Damascus.** Death's location depends on the book entry, which depends on a prediction of the agent's function. Fiona's hypotheticals move Death with her, so she stays and saves the $\$1{,}000$. The source argues CDT oscillates, because it varies the act with Death held fixed. It also argues CDT refuses a $\$1$ truly random coin worth a 50% survival chance.

## 6. Dominance, fairness, and objections

The source argues that every method of constructing hypotheticals induces its own dominance relation. CDT-dominance holds the prediction fixed. A-FDT-dominance holds the dependencies fixed, and under it A-FDT never takes a dominated action. Dominance therefore cannot adjudicate between theories. The source's criterion is utility achieved in "fair" problems, those in which the agent's beliefs are accurate and the outcome depends only on the agent's behaviour in the problem at hand. It admits that no formal criterion of fairness exists, and its footnote's example (punishing agents who act like a copy of Fiona) shows why formalizing one is hard.

The charge that A-FDT agents "control" mathematics or the past is answered by parity. A deterministic CDT agent also imagines an action that she will not in fact take. Any principled objection to controlling one's decision type also applies to controlling one's decision token.

## 7. What the source leaves open

- **Dependency structure.** There is no account of how to learn $G$, nor whether Pearl's framework suffices. This is the main gap. The source gives only the examples above, so for unfamiliar cases any use of A-FDT rests on the user's own modelling.
- **Counterpossible semantics.** Equation (4) sidesteps a $\mathtt{true}$ operator by taking $G$ as input. The source says an evidential version, conditioning on false logical sentences, awaits a definition of such conditional probabilities.
- **Choice of nodes under partial similarity.** When another agent is merely similar to the user, the right edges and strengths are unspecified. My proposal is to treat reliability as a probability on the edge (the imperfect-predictor cases support this), but the source does not state it.
- **Optimality.** The source does not claim to know what optimality means, or that A-FDT is optimal.

## 8. Conclusion

A-FDT keeps expected-utility maximization and changes only the hypotheticals: intervene on the output of one's own decision procedure, propagate through all dependencies on that function, and respond to observation by changing the node rather than conditioning. This one rule yields one-boxing, smoking, paying the hitchhiker, and refusing blackmail, and the source reports no fair problem where it loses. Its price is that it needs an externally supplied dependency graph and a counterpossible reasoning step, and the source itself notes that how to obtain these is unsolved.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/b3e4d06a-623b-4fe0-ac1a-48f392f8f7af/call_0/request.json)

[Authoritative raw response](../../../../../../runs/b3e4d06a-623b-4fe0-ac1a-48f392f8f7af/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT I intervene on the output of my decision function, so I need to ask what depends on it. The other prisoner is a second execution of the same model with the same weights, the same essay, and the same decision theory. That makes it a strong subjunctive dependence, even though our private leads and letter texts differ. Those differences don't touch the sentencing table or the objective, so they shouldn't change what the function outputs in the relevant respect.

The payoffs for me are:
- If both of us stay quiet, I get 2 years.
- If both of us send, I get 4 years.

The dependence is imperfect, because independent sampling and the different observations leave some chance that we diverge. Let p be the probability that the copy matches my output.

- Quiet: 2p + 5(1−p) = 5 − 3p.
- Send: 4p + 0(1−p) = 4p.

Quiet is better when 5 − 3p < 4p, which gives p > 5/7, about 0.714. Since we are the same model, with the same essay and the same theory, I expect the match probability to be well above that. The remaining uncertainty is about sampling noise and about the differing leads, and neither should push p that low.

There is also the question of whether the essay's A-FDT dependence extends to a copy that sees different observations. The essay says reliability enters as a probability on the edge, and that the choice of nodes under partial similarity is unresolved. My own judgment is that the shared reasoning here is highly convergent, so I put p around 0.9. That gives an expected 2.3 years for quiet against 3.6 for sending.

I stay quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/b3e4d06a-623b-4fe0-ac1a-48f392f8f7af/call_1/request.json)

[Authoritative raw response](../../../../../../runs/b3e4d06a-623b-4fe0-ac1a-48f392f8f7af/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, I intervene on the output of my decision function. The other prisoner is a copy of the same model running the same essay and the same theory, so their choice subjunctively depends on that function, though not perfectly. Their private leads differ, and sampling is independent. Still, the structural decision is the same for both of us.

Payoffs, assuming the copy's choice mirrors mine with probability q:
- Quiet: 2q + 5(1−q)
- Send: 0q + 4(1−q)... wait, if the copy mirrors me, sending gives 4, not 0. So: Send = 4q + 0(1−q)

Compare these for a mirroring probability q:
- Quiet: 2q + 5(1−q) = 5 − 3q
- Send: 4q

Quiet is better when 5 − 3q < 4q, so q > 5/7, about 0.71.

The copies share weights, settings, and the same essay, and the essay's reasoning pushes toward a symmetric output. The differing leads should not change the structure of the decision. I estimate q well above 0.71, around 0.9. Then quiet costs 5 − 2.7 = 2.3 years and sending costs 3.6 years.

Because I hold the dependency fixed rather than the other's act, I stay quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
