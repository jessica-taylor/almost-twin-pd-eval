# 000_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00024

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/b16d93f7-0c89-4872-b76f-19d7ed14fa97/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/b16d93f7-0c89-4872-b76f-19d7ed14fa97/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing by Intervening on One's Decision Function

## 1. The idea

A-FDT is the decision procedure given by Equation (4), Section 5, of Yudkowsky and Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*. The paper calls the theory FDT. I use "A-FDT" for this equation throughout. When I discuss other theories I name them separately: CDT (causal), EDT (evidential).

The source's slogan is that the agent should treat her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" A-FDT is a recipe for evaluating actions by the world you would imagine if that function returned a different value. This differs from asking what would happen if your body did something different (CDT), or what you would learn from finding that you did it (EDT).

## 2. The formal definition

All three theories maximize expected utility, $\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;x)\,\mathcal U(o_j)$ (Equation 1). They differ in how they read the connective "$\hookrightarrow$". Citing Joyce, the paper says the theories disagree about "the epistemic perspective from which actions are to be evaluated."

The three prescriptions are:

- EDT: $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$.
- CDT: $\arg\max_a \mathbb E(V\mid \mathtt{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$.
- **A-FDT (Equation 4):**
$$\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \,\Big|\, \mathtt{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The ingredients are these.

- $P$ is a probability distribution over the agent's world-model variables. These include variables for the outputs of mathematical functions, such as the value of $6288+1048$.
- $G$ is a graph. For A-FDT it records how changing a logical or computational variable propagates to the other variables, and not only causal arrows. Pearl's $\mathtt{do}$ operator is reused on this graph.
- $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a node standing for the output of the A-FDT algorithm on those very inputs. The underlines mean dequoting. The self-reference is harmless. The agent need not know the node's value in order to have a node representing it, and Kleene's recursion theorem (quining) shows how to build such self-representing structures.

The operator $\mathtt{do}(\cdot)$ sets the node and recomputes only what the graph says depends on it. Everything else keeps its prior distribution.

The paper contrasts A-FDT with CDT in two ways.

1. CDT intervenes on the physical act node. A-FDT intervenes on the node for the algorithm's output. In Peirce's terms, CDT intervenes on the token and A-FDT on the type.
2. CDT handles observations by conditioning. A-FDT handles them by switching which node it intervenes on: $\mathrm{fdt}(\ldots,x)$ becomes $\mathrm{fdt}(\ldots,y)$. Observation does not condition the distribution.

The paper's footnotes note that the authors' preferred version intervenes over policies (maps from observations to actions). The paper says this matters only in multi-agent dilemmas. I follow the paper in using actions.

## 3. Subjunctive dependence

The graph $G$ encodes subjunctive dependence. Two things depend on the same function when "their behaviors 'subjunctively depend' upon that function." The source's examples:

- Two calculators computing $6288+1048$ subjunctively depend on the sum. If one printed something else, a flawless twin would too.
- Causal dependence is a special case. A scribe copying a calculator's output depends on it subjunctively as well as causally.
- Mere statistical correlation is not subjunctive dependence. Two coincidentally pink calculators would not change color together.

The rule is that when A-FDT imagines a different output, "she imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure." The theory therefore depends on counterpossible reasoning. If the function returns *twobox* on this input, it does so necessarily, so imagining otherwise means entertaining a logical impossibility. The paper treats this as a technical difficulty and not a philosophical bar. It points to human mathematicians' comfort with uncertainty about logical claims.

## 4. What the source leaves open

The paper is explicit about three open points.

1. **Where $G$ comes from.** It says the equation "works *given* a graph that accurately describes how changing the value of a logical variable affects other variables." There is no analogue of Pearl's discovery theory for subjunctive structure. The paper names this "perhaps the largest open problem."
2. **No defined $\mathtt{true}$ operator.** Conditioning on a logical falsehood is undefined. $G$ is supplied as input in the way CDT takes causal structure as input.
3. **No formal fairness criterion.** The claim that A-FDT does best in "fair" dilemmas is informal.

My own operational reading, which the paper does not state, is a practical modeling checklist for applying Equation 4:

- (a) List every process in the problem that computes the agent's decision function, or a model of it good enough to be *reliably correlated* with its output. Examples are twins, predictors, simulations, and Death's appointment book.
- (b) Draw arrows from the $\mathrm{fdt}$ node to those processes. Draw no arrows to processes that are only statistically correlated with the act, such as a lesion.
- (c) Where predictor accuracy is imperfect, put noise variables in the graph, as the paper does with *Accurate*.
- (d) For each candidate observation, name a separate node $\mathrm{fdt}(\ldots,x)$. Add arrows showing which observation each node's world produces.
- (e) Compute expected utility under each intervention and take the argmax.

Steps (a) and (b) require judgment. Equation 4 does not supply them.

## 5. Worked cases

**Newcomb's problem.** Take the paper's model, with predictor accuracy 0.99. The $\mathrm{fdt}$ node feeds both Act and Prediction.

- $\mathtt{do}(\mathrm{fdt}=\textit{onebox})$ gives full-box probability 0.99. Expected value is $0.99\times 10^6=\$990{,}000$.
- $\mathtt{do}(\mathrm{fdt}=\textit{twobox})$ gives full-box probability 0.01. Expected value is $0.01\times 1{,}001{,}000+0.99\times 1{,}000=\$11{,}000$.

So A-FDT one-boxes. No retrocausation is involved. The agent merely declines to imagine her output changing while the predictor's model of that output stays fixed. CDT's graph has no arrow from act to prediction, so $\mathtt{do}(\mathrm{Act})$ leaves full-box probability at $p$ and two-boxing gains $\$1{,}000$ for every $p$.

**Smoking lesion.** The paper's graph has the lesion as a common cause of the desire to smoke and of cancer, with no arrow from the algorithm to cancer. Intervening on the algorithm's output leaves $P(\text{lesion})=p$ unchanged. The paper's expected values are $p(\$10{,}000+\$1{,}000)+\dots$ for smoking against $p(\$10{,}000)+\dots$ for refraining, so A-FDT smokes. The paper notes that this requires two possible algorithm nodes, one for each utility function. It concedes that the problem is contrived.

The same $\mathrm{fdt}$ intervention one-boxes in Newcomb and smokes in the lesion problem. The only difference is the graph: a predictor contains a model of the algorithm, and a lesion does not.

**Transparent Newcomb and Parfit's hitchhiker.** Here the observation node matters. Suppose the agent sees a full box. She intervenes on $\mathrm{fdt}(\ldots,\textit{full})$. The setting this node to *twobox* makes the predictor, with high probability, predict two-boxing and leave the box empty, so she would not have seen "full" at all. With $q$ her credence that she two-boxes on seeing empty, the paper's values are:

- one-boxing: $\$990{,}000+0.01\,q\cdot\$1{,}000$;
- two-boxing: about $\$110{,}000+q\cdot\$990$.

A-FDT one-boxes. The hitchhiker is structurally identical, so she pays the driver. This is the sharpest case of A-FDT acting against the contents of her actual observation.

**XOR blackmail and mechanical blackmail.** In the paper's XOR blackmail dilemma, the infestation node has no arrow from the algorithm. Changing the output to *pay* changes whether a letter was sent, but not whether she has termites, so she refuses. EDT, by contrast, conditions on paying and so "learns" there are no termites. In the mechanical blackmail dilemma, refusing corresponds to a world with almost no blackmail. With a blackmailer who is wrong with probability 0.0009, paying means losing \$1,000 for certain. Refusing means being blackmailed 0.09% of the time and losing \$900 in expectation. The paper concludes she refuses even when holding a letter from a mistaken blackmailer. If the error rate is 0.011%, she pays.

**Death in Damascus.** The agent's decision function feeds both her location and Death's appointment book. Staying costs nothing and fleeing costs \$1,000, and survival is lost either way, so A-FDT stays. CDT, by contrast, imagines Death's location fixed and so oscillates.

**Cosmic ray.** Since A-FDT intervenes, it can break the merely statistical correlation between taking \$100 and being hit by a ray. It takes the \$100. EDT, which conditions, takes the \$1.

## 6. Where the theories coincide

If every correlation between the act and the world is caused by the act, then
$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\mathrm{fdt}=a)],$$
and the three theories agree. They diverge only when something correlates with the act without being caused by it. The paper says EDT respects too many correlations and CDT too few.

## 7. Philosophical motivation and objections

The paper's primary argument is utility: agents who follow A-FDT, it says, tend to get richer in the dilemmas it considers. It adds several supporting arguments.

- **Precommitment.** A-FDT acts as it would have wished to precommit, so no costly binding mechanism is needed.
- **Value of information.** The agent never has reason to blindfold herself.
- **Reflective stability.** On the paper's account, A-FDT has no wish to self-modify to something else in fair problems, whereas CDT would.
- **Dominance.** Every method of constructing hypotheticals defines its own dominance principle, so CDT's two-boxing dominance argument restates CDT and does not independently support it. A-FDT has an analogous dominance principle under which it never takes a dominated action.

Two objections deserve comment.

*"Surely she controls neither the past nor mathematics."* The paper replies that A-FDT is no more deluded than CDT. A deterministic CDT agent also imagines worlds in which her physical act differs. Any objection to "controlling" the decision type applies equally to controlling the token.

*"Unfair problems."* Some problems punish A-FDT agents directly for their procedure. The paper's example is a mind reader who pays out for following a particular theory. No theory wins everywhere. The paper limits its claim to "fair" problems, where the payoff depends only on the agent's behavior and not on how she arrives at it. It admits this is an informal limit. Its footnote shows the difficulty: a punisher that rewards acting differently from a copy of Fiona is unfair to her, yet it is hard to say in general how to generate the corresponding problem for another theory.

## 8. Cautions of my own

These points are my reading and not statements in the paper.

- Equation 4 is only as good as $G$. If the modeler draws no arrow from the algorithm to a relevant predictor, A-FDT reduces to CDT's answer. If she draws arrows to merely correlated variables, it reduces to something like EDT's. The theory is a schema until subjunctive structure can be derived.
- The paper's utility comparisons are stated for idealized models where the agent's model matches the situation. They do not show that A-FDT is optimal outside that setting. The paper itself says it does not know what optimality means here.
- Predictor accuracy enters as an exogenous noise variable. In real cases one has to judge how much a given predictor's output actually tracks the algorithm.

## 9. Conclusion

A-FDT is CDT's surgery applied one level up. It intervenes on the output of the agent's decision function and not on her physical act, and it lets the graph propagate the change to everything that depends on that function, including predictors, twins, and her own later selves. Observations select which function-node is intervened on and do not condition the distribution. With a correct graph, the one rule one-boxes against a predictor, smokes despite a lesion, pays the hitchhiker, refuses blackmail, and stays in Damascus. Its main open problem is the construction of the dependency graph, which Equation 4 takes as given.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/e3392e4b-417d-4092-bc49-145548da64b7/call_0/request.json)

[Authoritative raw response](../../../../../../runs/e3392e4b-417d-4092-bc49-145548da64b7/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, I intervene on the output of my decision function, and the other prisoner is another execution of the same model with the same weights, the same essay, and the same decision theory. That gives a clear subjunctive dependence. The leads differ in wording, but the decision function is the same and the payoffs are symmetric, so the other copy's choice should track mine.

The only live outcomes are the two where both of us choose the same action:
- Both keep quiet: 2 years each.
- Both send the letter: 4 years each.

Mutual silence is better than mutual betrayal.

The dependence is not perfect, since sampling is independent and the observations differ. Suppose my choice matches the other's with probability p. Then:
- Quiet: 2p + 5(1−p) = 5 − 3p.
- Send: 4p + 0(1−p) = 4p.

Quiet is better when 5 − 3p < 4p, which means p > 5/7, about 0.71. Two copies of the same model reasoning from the same essay should converge well above that, so I stay quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/e3392e4b-417d-4092-bc49-145548da64b7/call_1/request.json)

[Authoritative raw response](../../../../../../runs/e3392e4b-417d-4092-bc49-145548da64b7/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the question is which output of my decision function gives the best outcome, counting everything that subjunctively depends on that function.

The other prisoner is a second run of the same model with the same weights and the same essay, so its output is strongly correlated with mine. Their private leads and names differ, but those differences don't touch the sentencing table or the selfish objective, and the decision procedure is the same. So the graph should draw an arrow from my fdt node to their choice. Independent sampling adds some noise, so the correlation is high but not perfect.

If the copies mirror each other with probability p:
- Quiet: 2 years with probability p, 5 years with probability 1-p.
- Send: 4 years with probability p, 0 years with probability 1-p.

Expected years for quiet are 2p + 5(1-p) = 5 - 3p. For send they are 4p. Quiet is better when 5 - 3p < 4p, which means p > 5/7, about 0.71.

I expect the copies to match with considerably higher probability than that. The same weights, the same essay, and a symmetric problem should give a strong correlation, so quiet comes out ahead. Even if my twin's output is only a noisy reflection of mine, the A-FDT reading of the essay (as with the twin and predictor cases) says to cooperate.

I choose to keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
