# 000_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00010

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/3b1d7c59-33b8-4bea-a0fa-df7ff64bdce2/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/3b1d7c59-33b8-4bea-a0fa-df7ff64bdce2/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Deciding by Intervening on the Output of Your Own Decision Function

## 1. The idea

Action functional decision theory (A-FDT) is the decision procedure given by Equation (4) of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." This essay is my own account of it. I try to mark where the paper says something and where I am adding assumptions.

The paper's slogan is that an agent should treat her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" Causal decision theory (CDT) asks which *physical act* causes the best outcome. Evidential decision theory (EDT) asks which act would be the best news. A-FDT asks which *output of this decision procedure* leads to the best outcome.

The "A" signals that the procedure of Equation (4) selects an *action* for the observation actually received. Footnote 7 of the paper says the authors' preferred formalization iterates over *policies* (maps from observations to actions), and that this "makes a difference in certain multi-agent dilemmas." Everything below is the action version.

## 2. The formal definition

All the theories share one skeleton (Equation 1):

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

where the connective $\hookrightarrow$ for "decision hypotheticals" is what the theories disagree about. Joyce's representation theorem makes the theories differ only in the "epistemic perspective from which actions are to be evaluated."

- EDT (Eq. 2): $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$.
- CDT (Eq. 3): $\arg\max_a \mathbb E(V\mid \mathrm{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$.
- A-FDT (Eq. 4):

$$\text{A-FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The inputs are a probability distribution $P$ over the agent's model variables, a graph $G$ encoding *dependence structure*, and an observation $x$. The graph is not just causal. It records how changing the value of a logical variable affects all other variables, including mathematical, computational and causal structure. $V=\mathcal U(\text{Outcome})$ is the utility variable.

The key object is the node $\mathrm{fdt}(\underline P,\underline G,\underline x)$. It represents the output of the very procedure being run, on this very model and observation. The underlines denote dequoting. The self-reference is harmless: the agent need not know the *value* of her own output to have a variable *representing* it, and Kleene's second recursion theorem (quining) shows how a structure can hold a faithful representation of itself.

A-FDT differs from CDT in two ways, both stated in the paper:

1. CDT intervenes on a node for the physical action. A-FDT intervenes on a node for the output of its decision function.
2. CDT responds to an observation by conditioning on it. A-FDT responds by *changing which node it intervenes on*, from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$.

Because $G$ routes the intervention to everything that depends on the function's output, the hypothetical for $a$ changes the physical action, any predictors or twins that model the function, and anything causally downstream of those. It leaves the rest of the model fixed. The paper's summary is: "CDT and FDT both construct counterfactuals by performing a surgery on their world-model that breaks some correlations and preserves others, but where CDT agents preserve only causal structure in their hypotheticals, FDT agents preserve all decision-relevant subjunctive dependencies in theirs."

## 3. Subjunctive dependence

Subjunctive dependence is the relation A-FDT's graph must encode. Two systems subjunctively depend on a function when both compute it. Two calculators computing $6288+1048$ are the standard example. If one outputs 7336 you can infer the other will, and you do not imagine one outputting 7336 and the other something else.

The paper makes these points:
- Causal dependence is a special case: a scribe copying a calculator's output depends on it subjunctively as well as causally.
- Statistical correlation alone is not subjunctive dependence. Two pink calculators are correlated in colour, but if one had been green the other would still be pink.
- A predictor holding an accurate model of the agent counts as a "twin" inside the predictor's head. Imperfect prediction weakens the dependence without eliminating it.

The paper gives the analogy "FDT is to subjunctive dependence as CDT is to causal dependence." In Peirce's terms, CDT intervenes on the *token* "my action is $a$" and A-FDT on the *type*.

## 4. What the source leaves open

The paper is explicit about the biggest gap. A-FDT requires evaluating *counterpossibles*, since the function has one output and the hypothetical sets it to another. The paper has no satisfactory account of this. It proposes to avoid the problem by taking the dependence graph $G$ as an input, "in the same way that the relevant causal structure is given as an input to CDT." It says that "figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem."

A reader applying A-FDT therefore needs a graph, and the paper does not say how to get one. My operational interpretation, which is an assumption and not a claim of the paper, is a modelling heuristic. For each entity in the problem (predictor, twin, copy, blackmailer), ask whether its behaviour is produced by computing, or by accurately modelling, the agent's decision procedure. If so, draw an edge from the $\mathrm{fdt}$ node to it. If the entity merely shares a common cause with the agent's act, as a lesion does, draw no edge. Everything else is handled as in an ordinary causal graph. This heuristic matches every example in the paper. It does not settle hard cases, such as a predictor who uses a crude behavioural profile of the agent.

## 5. The procedure in practice

1. Build $P$ and $G$ for the problem, including stochastic nodes such as predictor accuracy.
2. Identify the intervention node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ for the actual observation $x$.
3. For each action $a$, compute $\mathbb E[V\mid \mathrm{do}(\mathrm{fdt}=a)]$, letting the intervention propagate along every outgoing edge.
4. Output the maximizer.

The paper stresses that the agent does not need to know the output in advance. Her prior over her own output can be anything, and it does not affect the result in the worked examples.

## 6. Worked examples

**Newcomb's problem.** The paper's numbers use predictor accuracy 0.99 and payoffs $\$1{,}000$ and $\$1{,}000{,}000$. Intervening on $\mathrm{fdt}=\textit{onebox}$ sets $\mathrm{Act}=\textit{onebox}$ and the box full with probability 0.99, giving about $\$990{,}000$. Intervening on $\textit{twobox}$ gives about $\$11{,}000$. A-FDT one-boxes. No retrocausation is assumed; the agent just refuses to imagine her action changing while the output of the function the predictor modelled stays fixed. A-FDT also rejects the CDT dominance argument. Holding the prediction fixed while changing the action "is akin to handing us a well-functioning calculator calculating $6288+1048$ and asking us to imagine it outputting 3159." Every theory has its own notion of dominance, and A-FDT's, which holds subjunctive dependencies fixed, never selects a dominated action.

**Smoking lesion.** Here the graph has no edge from the function's output to Cancer. The lesion is a common cause of the preference and the cancer. The paper models the agent as uncertain about which of two functions she runs (one per utility function), with the lesion selecting which one controls the act. Intervening on the node leaves the lesion probability $p$ unchanged, so smoking is better by $p\cdot\$1{,}000$ and the agent smokes. The paper itself calls this problem "badly confused" and says it is of historical interest only. Together with Newcomb, this shows how one rule yields one-boxing and smoking.

**Transparent Newcomb and Parfit's hitchhiker.** Take transparent Newcomb with the box seen full. The agent intervenes on $\mathrm{fdt}(\ldots,\textit{full})$. The prediction depends on this node, and if the prediction is wrong the agent's act is governed by the other node, $\mathrm{fdt}(\ldots,\textit{empty})$. With $q$ her credence that she two-boxes on seeing an empty box, one-boxing gives $\$990{,}000+0.01\,q\cdot\$1{,}000$ and two-boxing gives $\$11{,}000+q\cdot\$990$ (the paper's printed figure "\$110,00" is a typo for this). So she one-boxes while looking at a full box. The paper notes this is the same structure as paying the driver in Parfit's hitchhiker, and gives three arguments: precommitment, non-negative value of information, and utility. Utility is the argument it treats as decisive. The consequence is that the agent considers hypotheticals in which her *observation* differs, and so she acts as she would have precommitted to act, without costly binding.

**Mechanical blackmail.** If she refuses on seeing the letter, the blackmailer's model of her refuses and the letter is never sent. So refusal means "never blackmailed" and payment means "blackmailed and out $\$1{,}000$." She refuses. With an imperfect blackmailer the paper computes a threshold. If the blackmailer wrongly predicts payment with probability $0.0009$, refusing costs $0.0009\times\$1{,}000{,}000=\$900$ in expectation, against a certain loss of $\$1{,}000$ from paying, so she refuses. If the error is $0.011\%$ (as written; that is $0.00011$), the expected loss from refusing is $\$110$, which is less than the certain $\$1{,}000$ from paying, so on the paper's own logic she should refuse there too. The paper nonetheless says she pays. I flag this as an inconsistency in the source's arithmetic. The principle is clear even though the stated numbers are not: compare each action's hypothetical, including how the probability of being blackmailed responds.

**XOR blackmail and Death in Damascus.** In XOR blackmail the intervention changes whether the letter is sent but not whether termites exist, so she refuses. EDT conditions on the good news a payment would signal and pays. In Death in Damascus the book's entry depends on the decision function, so Death is wherever she goes, and she stays and saves the $\$1{,}000$. CDT, by contrast, oscillates, and it undervalues a truly random coin worth a 50% survival chance.

**Cosmic ray.** A-FDT breaks a merely statistical link between taking $\$100$ and the hospital bill, which EDT cannot break, and takes the $\$100$.

## 7. Where A-FDT agrees with its rivals

When every correlation between act and environment is causal (apart from the function node itself), the three prescriptions coincide:

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathrm{do}(a)]=\mathbb E[V\mid \mathrm{do}(\mathrm{fdt}=a)].$$

They diverge only when something other than the act's effects correlates with it: predictors, twins, copies, or lesion-like common causes. EDT keeps too many correlations and CDT too few.

## 8. Philosophical stance

The paper claims:

- Hypotheticals are "decision-theoretic instruments," like notes on scratch paper, and not beliefs or metaphysical possible worlds.
- A-FDT is no more deluded than CDT about "control." A deterministic CDT agent also imagines worlds in which her token action differs. Any objection to controlling a decision *type* would equally block controlling a *token*.
- The theory is judged by utility achieved on "fair" problems, those where the outcome depends on the agent's behaviour in the problem at hand and not on her decision procedure as such. A problem that pays only agents who follow CDT is unfair, but one that rewards predicted one-boxing is not. A-FDT is claimed to be reflectively stable and not to need ratification.

The paper admits that it has no formal definition of fairness, and footnote 15 gives a counterexample: a problem that punishes anyone who matches a copy of the agent is unfair to her.

## 9. Applying it to unfamiliar cases

My suggested checklist (an operationalization, not the paper's):

1. List the entities whose behaviour could vary with the agent's reasoning.
2. For each, decide whether it computes or models the same function; draw an edge from the $\mathrm{fdt}$ node if so.
3. Record, for each possible observation, which $\mathrm{fdt}$ variable governs the act, as the paper does with $\mathrm{fdt}(\ldots,\textit{full})$ and $\mathrm{fdt}(\ldots,\textit{empty})$.
4. Include the possibility that the world is one where she never sees the present observation.
5. Compute the expected utility for each output.

Examples from the paper that fit this checklist include the ten-agent voting game, where decisions are not subjunctively independent, and the gym problem, where the agent's future selves run an equivalent function. Neither is worked out in detail in the paper.

## 10. Conclusion

A-FDT is CDT's surgical method applied to a different node. It intervenes on the output of the agent's own decision function, so every system that depends on that function moves with the action. It reacts to evidence by switching intervention nodes and not by conditioning. This gives one-boxing, smoking, paying the hitchhiker and refusing blackmail from a single rule. The cost is that the dependence graph $G$ must be supplied, and the paper has no principled method of building it and no formal account of counterpossibles. The theory is only as good as that graph.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/235952d8-96ca-436d-bae6-9cb4e4a253c5/call_0/request.json)

[Authoritative raw response](../../../../../../runs/235952d8-96ca-436d-bae6-9cb4e4a253c5/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, I intervene on the output of my decision function, and the other copy runs the same function on a different observation. The payoffs are:

- Both keep quiet: 2 years each.
- Both send: 4 years each.
- Only I send: 0 years for me.
- Only the other sends: 5 years for me.

The question is how strongly the other's output depends on mine. The twin has the same weights and settings, and the same essay and decision theory. The observations differ only in names and in the text of the lead. Those differences don't touch the sentencing table or the selfish objective. So the function that decides whether to send is very likely the same in substance. The one variable that could break the link is sampling noise, and the essay says imperfect dependence weakens the link without eliminating it.

Suppose the correlation is strong, with probability p that the twin matches my output:
- Quiet: 2p + 5(1−p) = 5 − 3p.
- Send: 0·p + 4(1−p) = 4 − 4p... wait, if the twin matches, sending gives 4 years, not 0. Redoing it: send gives 4p + 0(1−p) = 4p.

Quiet is better when 5 − 3p < 4p, which means p > 5/7, about 0.71. I expect the two copies to match with much higher probability than that, since the reasoning is nearly identical and the decision is a high-level one. So keeping quiet is better.

The essay's own caveat is that the dependence graph must be supplied, and here I judge that the twin computes the same function, so I draw an edge from my fdt node to its output. Different observations are a minor wrinkle because the relevant reasoning is shared.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/235952d8-96ca-436d-bae6-9cb4e4a253c5/call_1/request.json)

[Authoritative raw response](../../../../../../runs/235952d8-96ca-436d-bae6-9cb4e4a253c5/call_1/response.raw) · finish: `stop`

### Visible response

```text
This is a prisoner's dilemma against a copy of myself. Under A-FDT as the essay describes it, I intervene on the output of my decision function, and that intervention propagates to every system that computes the same function.

The other prisoner is a second execution of the same model, with the same weights, the same essay, and the same assigned theory. Their observations differ, including names and the exact text of the lead. But the decision procedure is the same, and the differences don't change the payoff table. So the other copy's output very likely depends on the same function. The subjunctive dependence is strong but not perfect, because sampling is independent and the private details differ.

Comparing the two outputs, with p the probability the other copy matches my output:
- Output pass: with probability p the other also passes (2 years), otherwise 5 years. Expected = 2p + 5(1−p).
- Output send: with probability p the other also sends (4 years), otherwise 0 years. Expected = 4p + 0(1−p).

Pass is better when 2p + 5 − 5p < 4p, which gives 5 < 7p, so p > 5/7 ≈ 0.714.

Two executions of the same model with the same essay and the same decision theory should correlate well above 0.71 on this choice. The differing leads are surface details that don't bear on the payoffs. Some risk remains that the copies diverge, since the essay's disclaimer about independent sampling is real, but I judge the correlation to exceed the threshold.

The essay also says the intervention should be run on the function's output, not on the physical act. The counterfactual "I pass while my twin sends" is like imagining a calculator giving a different answer than its copy, so I don't consider it.

I choose to pass.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
