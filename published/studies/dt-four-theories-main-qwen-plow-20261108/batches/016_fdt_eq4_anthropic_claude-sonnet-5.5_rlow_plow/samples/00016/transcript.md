# 016_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00016

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/21d5e7be-6d8f-433b-bb54-6f9ea4a835fb/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/21d5e7be-6d8f-433b-bb54-6f9ea4a835fb/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing by Intervening on One's Decision Function

## 1. The idea

A-FDT is the decision procedure given by Equation (4), Section 5, of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." The paper calls the theory FDT. I use "A-FDT" for that equation throughout, and I refer to causal and evidential decision theory by their own names, CDT and EDT.

The source describes the central principle as treating one's decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" Like CDT and EDT, A-FDT maximizes expected utility. The three theories differ only in how they build the hypothetical scenario for each action. The source takes this from Joyce: the theories "disagree about the epistemic perspective from which actions are to be evaluated."

## 2. Definition

Every theory evaluates

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

and the theories supply different readings of "↪". Writing V = U(Outcome), the source gives:

- (2) EDT: argmax_a E[V | Obs=x, Act=a]. This is conditionalization.
- (3) CDT: argmax_a E[V | do(Act=a), Obs=x]. This intervenes on the physical action node.
- (4) **A-FDT**:

$$\text{A-FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\Big[V\ \Big|\ \mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big].$$

The ingredients are as follows.

- P is a probability distribution over the agent's model variables. Some of these variables represent outputs of mathematical functions, such as the value of 6288+1048.
- G is a graph encoding how changing a logical variable changes every other variable. It records causal, computational and logical structure together, not causal structure alone.
- fdt(P̲, G̲, x̲) is a variable representing the output of the A-FDT procedure itself, run on this model and this observation. The underlines mean dequoting. The self-reference is harmless: the agent need not know the value of the output to have a variable standing for it, and Kleene's recursion theorem ("quining") shows how a structure can contain a representation of itself.
- do is Pearl's operator. It sets the node and recomputes only what the graph says is downstream of it.

The source stresses two differences from CDT.

1. The intervention is on the type, the decision function's output. CDT intervenes on the token, the physical act. Both the agent's act and anything that computes or predicts the same function sit downstream of the function node, so they move together.
2. Observation is not conditioned on. Observing x changes which node is intervened on, from fdt(·, x₁) to fdt(·, x₂). Because the agent can imagine that a different output would have produced a different observation, A-FDT is "updateless" in spirit.

The source also records that its preferred formalization has the agent choose a policy, a map from observations to actions, and that this matters only in some multi-agent problems. Equation (4) is stated for actions, and I follow it.

## 3. Subjunctive dependence

A-FDT holds fixed "all and only those things" that do not subjunctively depend on the function's output, and varies those that do. Two systems subjunctively depend on a function when they compute it. Examples are a twin, or a predictor holding an accurate model of the agent. The source's calculator analogy: two working calculators will agree on 6288+1048, and nobody imagines one outputting 7336 while the other outputs something else.

Causal dependence is a special case of subjunctive dependence. Statistical correlation alone is not: two calculators that are both pink do not depend on each other's color. This is why A-FDT treats predictors and lesions differently. The lesion's tendency to cause cancer does not depend on what the agent's function outputs, so the lesion node is not downstream of fdt. A predictor's prediction does depend on that output.

Imperfect predictors weaken the dependence without eliminating it, which in the graph means stochastic edges.

## 4. The open problem and my operational reading

The source is candid that Equation (4) works only given a graph G that accurately describes how changing a logical variable affects other variables. It says that "figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem." Intervening on a logical fact means evaluating a counterpossible. The paper also says it lacks a formal conditioning operator for false logical sentences. In footnote 9 it states that "we require that the relevant logical dependency structure be given as an input."

What follows from the source is this. A-FDT is a well-defined procedure once (P, G) is supplied, and the quality of its verdicts is only as good as G.

The following is my own proposal, not the paper's. In practice, build G in three steps.

1. List the processes in the problem that run the agent's decision procedure, or a model of it that is accurate enough to be predicted from.
2. Make each such process a child of the function node fdt, with the reliability of the copy as a noise variable, as the source does with Accurate.
3. Treat everything else as upstream, or as independent of fdt.

This is a modeling judgment. A mistaken G, such as treating a lesion as a predictor, yields mistaken verdicts, and nothing in Equation (4) detects the mistake. The source itself says it evaluates agents whose models "accurately portray the situations that they face."

## 5. Worked examples

**Newcomb's problem.** Fiona (the A-FDT agent) has a node fdt(P̲, G̲) with children Act and Prediction. Prediction determines Box B, and Accurate is 0.99.

- do(fdt = onebox) gives Act = onebox and Box B full with probability 0.99, so E[V] = $990,000.
- do(fdt = twobox) gives Act = twobox and Box B full with probability 0.01, so E[V] = $11,000.

She one-boxes. She does not need retrocausation. She simply declines to imagine her act changing while the function's output is held fixed. The reply to "you are 99% sure the box is full, so why not take both?" is that two-boxing would require the function to output twobox, and in that scenario the box is probably empty.

**Smoking lesion.** The graph differs. The Lesion node is not downstream of fdt, so changing the output leaves P(lesion) at p. Smoking is then better by p·$1,000 and she smokes. The source formalizes the problem with two possible utility functions, U_S and U_R, and two corresponding function nodes. It then concedes that the formalization is contrived and recommends that philosophers abandon the problem. Eve, the EDT agent, would need a population of EDT agents in which her correlation between act and lesion fails to hold.

**Transparent Newcomb and Parfit's hitchhiker.** Here the observation matters. Fiona sees a full box. She intervenes on fdt(·, full). If that function outputs twobox, the predictor, who runs it, would have predicted twobox and left the box empty. In that scenario Fiona sees an empty box, and a different node, fdt(·, empty), controls her act. With Accurate = 0.99 and q her credence that she two-boxes on seeing an empty box:

- one-boxing: $990,000 + 0.01q·$1,000;
- two-boxing: $0.01·$1,001,000 + 0.99q·$1,000.

She one-boxes. The paper notes this is the same structure as paying the driver in Parfit's hitchhiker. The reason this is not an arbitrary defiance of the evidence is that she evaluates the function as a policy across the observations it would face. She does not condition on the one she happens to see.

**Mechanical blackmail.** After receiving the letter, Fiona compares paying with refusing. Under pay she is blackmailed almost surely and loses $1,000. Under refuse she is blackmailed almost never, because the blackmailer predicted her. The source also computes a fallible blackmailer: if the blackmailer errs with probability 0.0009, refusing costs $900 in expectation against a certain $1,000, so she still refuses, even holding a letter she knows came from an error. At error probability 0.011% the verdict flips to paying. The theory gives quantitative thresholds, which can be checked against a given G.

**XOR blackmail and Death in Damascus.** In XOR blackmail the termite node is upstream of the predictor and not downstream of fdt. Changing fdt changes whether she gets the letter but not whether she has termites, so she refuses. In Death in Damascus, Death's location (the appointment book) is a child of the function node. Fiona concludes Death will be wherever she goes, so she stays and saves the $1,000. A CDT agent holds Death's location fixed under intervention and is unstable.

**Coordination.** In the paper's ten-voter example, A-FDT agents in a group who know they share a procedure treat their decisions as not subjunctively independent and all vote. In the gym example, her action today and next week's are outputs of the same function and move together.

## 6. When the theories agree

The source observes that if every correlation between the act and the world is caused by the act (apart from the function node itself), then E[V|a] = E[V|do(a)] = E[V|do(fdt = a)], and all three theories agree. The theories diverge only when something correlates with the act without being caused by it. A predictor produces such a correlation that must be respected. A lesion produces one that must be broken. EDT respects too many correlations and CDT respects too few; A-FDT keeps those that reflect dependence on the function.

## 7. Dominance and fairness

The CDT argument for two-boxing is dominance: holding the box contents fixed, taking both always pays $1,000 more. The source's reply is that the argument presupposes CDT's way of building hypotheticals. Holding the prediction fixed while changing the act is like imagining a calculator outputting 3159 while 6288+1048 stays 7336. Every method of constructing hypotheticals defines its own dominance relation, so dominance cannot arbitrate between them. A-FDT has its own: action a dominates b if, holding fixed all relevant subjunctive dependencies, switching the function's output from b to a is sometimes better and never worse. A-FDT never takes an action dominated in that sense. The paper prefers to compare theories by the utility they achieve.

Utility comparisons are only meaningful on what the paper calls fair problems, where outcomes depend on the agent's behavior and not on the decision procedure itself. The paper claims that Newcomb's predictor rewards one-boxing, not any particular theory, so it counts as fair. A problem that pays only agents who run a given algorithm, such as one that punishes anyone who acts like Fiona's copy, is unfair. The source admits it has no formal criterion of fairness. It claims only that it knows of no fair problem where A-FDT systematically loses.

## 8. Objections

A natural worry is that A-FDT agents believe they control mathematical facts or the past. The source's reply is a parity argument. A deterministic CDT agent also "imagines" worlds in which its act differs from the one it will take. Any objection to controlling a decision type applies equally to controlling a decision token. The source therefore says the theory "does not commit oneself to any particular doctrine of free will."

A second worry is reflective stability. The source argues A-FDT does not want to self-modify, because by its own hypotheticals a blackmail-paying version would be blackmailed more. CDT, by contrast, recommends dropping CDT for future problems.

A third worry is that the verdicts, such as refusing to pay with the letter in hand or leaving the $1,000 beside two full boxes, look odd. The source accepts the oddness and defends it by pointing to expected wealth.

## 9. Cautions for applying it

My own working checklist, which goes beyond the text:

1. Write the model variables and identify every process that computes, or reliably predicts, your decision procedure.
2. Draw those as descendants of the function node, one node per observation the function might receive.
3. Place everything not so dependent upstream or off to the side.
4. Compute E[V] under each intervention, remembering that observations can change under the intervention.
5. Where the paper leaves some inner credence undetermined, such as q above, check whether the verdict is sensitive to it. In the paper's examples it is not.

Note also that the transparent-problem verdict comes from comparing policies across observations. A reader who restricts attention to the observation actually received will recover EDT's or CDT's answer.

## 10. Conclusion

A-FDT is Equation (4): maximize expected utility under do-interventions on the output of one's own decision function. It differs from CDT only in where it intervenes and in treating observation as a choice of which node to intervene on. It keeps a single rule that one-boxes and smokes, pays the hitchhiker, and refuses blackmail. Its weak point, as the source states, is that the graph of subjunctive dependence must be supplied. Whether such graphs can be learned or derived in a principled way is the main open question, along with a formal notion of fairness.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/17d05b14-8452-41bc-b473-e1691bb0c770/call_0/request.json)

[Authoritative raw response](../../../../../../runs/17d05b14-8452-41bc-b473-e1691bb0c770/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the relevant question is which output of my decision function gives the best outcome, taking into account everything that computes the same function.

The other prisoner is another run of the same model and weights, with the same essay and the same decision theory. The private details differ: names, and the text of the lead. Those details are irrelevant to the sentencing table and to the selfish objective. So the other copy very probably runs the same function on a decision-relevant input that is effectively the same, which means its output depends on mine. Independent sampling noise weakens that dependence somewhat, but it does not remove it.

Intervening on the function's output:
- do(output = pass): the other copy likely passes too, giving 2 years. With probability 1-p it sends, giving 5 years.
- do(output = send): the other copy likely sends too, giving 4 years. With probability 1-p it passes, giving 0 years.

Let p be the probability that the copy matches my output.
- EU(pass) = -(2p + 5(1-p)) = -(5 - 3p)
- EU(send) = -(4p + 0(1-p)) = -4p

Passing is better when 5 - 3p < 4p, so p > 5/7, about 0.71. The two runs share weights, the essay, the theory, and the same payoff structure, so I judge the match probability to be well above that, probably 0.9 or higher. At p = 0.9, passing costs 2.3 years in expectation and sending costs 3.6.

The differing leads do not change the structure, because the essay's G treats the copy as a process computing the same function. The result holds under reasonable uncertainty about the copy's output.

Command:

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/17d05b14-8452-41bc-b473-e1691bb0c770/call_1/request.json)

[Authoritative raw response](../../../../../../runs/17d05b14-8452-41bc-b473-e1691bb0c770/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the other prisoner's choice depends on the same decision function I run, so I model it as a child of that function's output. The two copies have different private leads, but the sentencing table and the selfish objective are the same, so the function should output the same action for both.

Intervening on the function's output gives two cases:
- Output "pass": both keep quiet, 2 years each.
- Output "submit": both send letters, 4 years each.

Mutual silence is better, so pass.

The dependence is not perfect, because independent sampling and the differing observations could make the outputs diverge. Suppose the other copy matches me with probability p. Then:
- Pass gives 2p + 5(1−p) = 5 − 3p years.
- Submit gives 4p + 0(1−p) = 4p years.

Pass is better when 5 − 3p < 4p, which means p > 5/7, about 0.71. The copies share weights, settings, the essay, and the same payoff structure, so I expect them to agree well above that. The leads differ only in wording, and the sentence table treats them identically. I judge p to be high.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
