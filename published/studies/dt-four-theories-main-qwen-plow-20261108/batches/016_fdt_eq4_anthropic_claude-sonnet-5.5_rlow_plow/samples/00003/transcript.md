# 016_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00003

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/c51dfb59-0cf2-4d6e-9c6e-2671eba44c3c/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/c51dfb59-0cf2-4d6e-9c6e-2671eba44c3c/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing by Intervening on One's Decision Function

## 1. The idea

Action functional decision theory (A-FDT) is the version of functional decision theory given by Equation (4) of Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality". "A" marks that the theory selects an action. The source notes in footnotes 7 and 16 that its authors' preferred formalization selects policies, which are maps from observations to actions. That difference "only matters in multi-agent dilemmas so far as we can tell." I follow the source and treat actions with observations as inputs.

The core claim is that a decision is the output of a fixed mathematical function. The agent asks, in the source's words, "Which output of this very function would yield the best outcome?" This contrasts with CDT's question about which physical act causes the best outcome, and with EDT's question about which act would be the best news.

## 2. The formal definition

All three theories maximize expected utility,

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

and differ only in how they read the connective "$\hookrightarrow$". The source follows Joyce in treating this as the choice of an "epistemic perspective". The three prescriptions are:

- EDT (Eq. 2): $\arg\max_a \mathbb E(V\mid Obs=x, Act=a)$.
- CDT (Eq. 3): $\arg\max_a \mathbb E(V\mid do(Act=a), Obs=x)$.
- A-FDT (Eq. 4):

$$\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \,\Big|\, do\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The inputs are:

- **$P$**, a probability distribution over variables of the world-model. It includes variables for outputs of mathematical functions, such as the value of $6288+1048$.
- **$G$**, a graph describing "how changing a logical variable affects all other variables". It encodes logical, computational and causal structure together.
- **$x$**, the observation history.

The node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ stands for the output of the A-FDT procedure on those very inputs. The underlines denote dequoting, so the node's name depends on the model. The self-reference is harmless. The agent need not know the value of the node in order to have a variable representing it, and Kleene's second recursion theorem (quining) shows how a structure can contain a representation of itself.

Evaluation proceeds as follows. For each $a$, build a hypothetical by applying Pearl's $do$ to the node $\mathrm{fdt}(P,G,x)$ and propagating along $G$ to everything that depends on it. Everything else is held fixed. Compute expected utility and pick the best $a$.

A-FDT differs from CDT in two ways, both stated in the source:

1. It intervenes on the decision-function node rather than on the physical-action node $Act$.
2. It does not respond to observation by conditioning. It responds by changing which node it intervenes on, from $\mathrm{fdt}(P,G,x)$ to $\mathrm{fdt}(P,G,y)$.

The source describes A-FDT as the analogue of CDT for subjunctive dependence: CDT intervenes on the token "my action is $a$", and A-FDT intervenes on the type.

## 3. What counts as a dependency

Subjunctive dependence holds between two things when they would change together if a shared function had a different output. Two calculators computing $6288+1048$ are an example. A predictor holding an accurate model of the agent is another. Causal dependence is a special case: the scribe's note depends on the calculator's output. Mere correlation does not qualify. Two pink calculators do not depend on each other's colour.

In practice, then, A-FDT hypotheticals preserve exactly those correlations with the action that are underwritten by shared computation or causation. They break correlations that are merely statistical. The source puts it this way: EDT "respects too many" correlations and CDT "too few".

Where every correlation with $Act$ is caused by $Act$, apart from dependence on the decision function itself, all three theories agree:

$$\mathbb E[V\mid a]=\mathbb E[V\mid do(a)]=\mathbb E[V\mid do(\mathrm{fdt}=a)].$$

They come apart when predictors or twins are present.

## 4. Worked examples

I take utilities in dollars, as the source does.

**Newcomb (99% accurate predictor).** In the graph, the node $\mathrm{fdt}(P,G)$ is a parent of both $Act$ and $Prediction$. Setting it to one-box gives $Act=$ one-box and $P(\text{full})=0.99$, so expected utility is $\$990{,}000$. Setting it to two-box gives $P(\text{full})=0.01$ and expected utility $\$11{,}000$, so A-FDT one-boxes. No retrocausal physics is involved. The agent only declines to imagine her output changing while the prediction of that output stays fixed.

**Smoking lesion.** The lesion is not downstream of the decision function, so the hypotheticals leave $P(\text{lesion})=p$ unchanged. Smoking gains \$1,000 in both hypotheticals, so A-FDT smokes. The same rule therefore gives one-boxing in Newcomb and smoking here, without any ratification step. The source concedes that the lesion problem is contrived. It requires the agent to be uncertain about her own utility function, which the source handles with two candidate nodes $\mathrm{fdt}(P_S,G)$ and $\mathrm{fdt}(P_R,G)$, and which it recommends philosophers abandon.

**Transparent Newcomb and Parfit's hitchhiker.** Suppose the agent sees the full box. She intervenes on $\mathrm{fdt}(P,G,\text{full})$. Setting it to two-box makes the predictor, who simulates this very procedure, probably have left the box empty. In that hypothetical the agent is probably running $\mathrm{fdt}(P,G,\text{empty})$ instead. Writing $q$ for her credence that she would two-box on seeing an empty box, the expected utilities are:

- one-box: $\$990{,}000+0.01\,q\cdot\$1000$;
- two-box: $\$110{,}000+q\cdot\$990$ (this is the source's own printed expression; I take the first term to be $0.01\times\$1{,}001{,}000=\$10{,}010$, so the source's "\$110,00" looks like a typo).

One-boxing wins either way. This is the same structure as paying the driver in Parfit's hitchhiker, and A-FDT pays.

**XOR blackmail and mechanical blackmail.** Having seen a letter, A-FDT imagines refusing as a world in which the predictor's model of her refuses, so the letter probably never came. Paying leaves her blackmailed and out \$1,000. Refusing leaves her rarely blackmailed. The infestation node is not downstream of $\mathrm{fdt}$, so refusing never changes the termite probability. The source's imperfect-predictor numbers are as follows. If the predictor errs with probability 0.0009, refusing costs $0.0009\times\$1{,}000{,}000=\$900$ in expectation against a certain \$1,000 for paying, so she refuses. At error probability 0.00011 the comparison reverses and she pays. (The source writes this second figure as "0.011%".)

**Death in Damascus.** Death's appointment book depends on a prediction of her decision procedure. In the hypothetical "I flee", the book says Aleppo. Fleeing costs \$1,000 and does not help, so she stays. CDT is unstable here because it imagines moving while Death stays put.

## 5. The role of the predictor in hypotheticals

A common objection is that A-FDT agents already know the box is full and so should take both boxes. The reply is that the question "what would happen if I two-boxed?" is answered by the hypothetical in which the function outputs two-box. That hypothetical is evaluated by the model, not by the agent's current factual beliefs. A-FDT also does not "update" in the conditioning sense. The source notes this is the origin of the name of updateless decision theory.

Dominance reasoning does not refute this. Every method of constructing hypotheticals induces its own dominance relation. CDT-dominance presupposes CDT counterfactuals, and A-FDT has its own dominance relation, under which A-FDT never takes a dominated action. The source therefore evaluates theories by the utility they achieve in fair problems. A problem is fair when the outcome depends only on the agent's behaviour in the problem at hand, so that rewarding or punishing a prediction of the act counts and rewarding a particular decision procedure does not. The source admits it has no formal definition of fairness (footnote 15 gives a problem that is unfair to A-FDT in particular).

## 6. What the source leaves open, and my proposals

**The graph $G$ is an input.** The source says plainly that deducing the structure of subjunctive dependence is "perhaps the largest open problem". There is no analogue of Pearl's account of learning causal structure from observation and experiment. Footnote 9 explains why the source passes over a conditioning-on-logical-falsehoods operator, which would need counterpossible probabilities that no one yet has. It follows that A-FDT as presented is conditional on a correct $G$, and that decisions are only as good as that graph.

The following is my own proposal, not the source's. A practical modelling heuristic is to add a node for the decision function whenever some environmental process contains, or would be built from, a representation of the agent's decision algorithm. Examples are a simulation, a twin, or a predictor inferring from the agent's reasoning. Then make that node a parent of the agent's action and of every variable the process computes from that representation. Where the process responds only to features independent of the decision function, as a lesion does, add no such edge. Imperfect predictors are handled by the same nodes plus noise, as in the source's $Accurate$ variable. This gives a defensible rule for cases the paper does not model. It is a modelling guideline and not a derived result.

**Policies versus actions.** For single-agent problems with observations, Eq. (4) with an input-indexed node is already policy-like, since the choice at each observation is its own node and the nodes are linked through the predictor. I suggest that where several observations are possible, a reader should evaluate $\mathrm{fdt}$ at every input jointly and then check that Eq. (4) at the realized input selects the same action. The source says this matters only in multi-agent cases.

**Unmodelled predictors.** Where the graph is unclear, an agent can compare candidate graphs by the utility of the policy each recommends, weighted by credence in each graph. This is again my suggestion and has no support in the source.

## 7. Why endorse it

The source's case is primarily empirical. A-FDT agents do best on average in fair Newcomblike problems. They do not manage the news, they do not pay to avoid information, they need no costly precommitment, and they are reflectively stable (no desire to self-modify to CDT in the blackmail case, since by their hypotheticals that would invite blackmail). The coordination examples the source gives are:

- A ten-person voting problem, in which each member votes because the others reason the same way.
- Self-coordination over time, such as going to the gym.

The charge that A-FDT agents are deluded about "controlling" abstract functions is answered symmetrically: a deterministic CDT agent equally cannot "control" her physical act, yet imagines varying it.

## 8. Conclusion

A-FDT is a short rule: intervene on the node for the output of your own decision procedure, propagate through every dependency in the graph, and choose the action whose hypothetical has the highest expected utility. Its force lies in how it constructs hypotheticals, preserving subjunctive and causal dependence and severing mere statistical correlation. Its principal weakness is that the dependency graph must be supplied. Where the source is silent about how to build that graph, I have offered heuristics, and they should be judged as my own additions.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/c227b08d-ec95-409c-b705-e68f4dc70807/call_0/request.json)

[Authoritative raw response](../../../../../../runs/c227b08d-ec95-409c-b705-e68f4dc70807/call_0/response.raw) · finish: `stop`

### Visible response

```text
Reasoning under A-FDT: the other prisoner is a copy of the same model running the same procedure, so our outputs are subjunctively dependent. The letter contents differ, but the decision to disclose or not comes from the same function and the same essay. Intervening on that function's output moves both decisions together, with some noise because the private observations differ and sampling is independent.

If both stay quiet, I get 2 years. If both send, I get 4 years. Assume a probability q that the copy matches my choice. Then:

- Quiet: 2q + 5(1−q) = 5 − 3q
- Send: 4q + 0(1−q) = 4q

Quiet is better when 5 − 3q < 4q, which means q > 5/7 (about 0.71). The copies share weights, settings, and the essay, so I expect the correlation to be well above that. The differences in the private leads don't affect the sentencing table or the objective, so they shouldn't change the output of the decision function.

The dependency graph is uncertain, but the essay's heuristic says to add a node for the decision function when another process runs the same algorithm. That applies here. Quiet is the better choice.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/c227b08d-ec95-409c-b705-e68f4dc70807/call_1/request.json)

[Authoritative raw response](../../../../../../runs/c227b08d-ec95-409c-b705-e68f4dc70807/call_1/response.raw) · finish: `stop`

### Visible response

```text
Reasoning under A-FDT as the essay describes it:

The payoff table is a standard prisoner's dilemma. Sending the letter gives 0 or 4 years, and keeping quiet gives 2 or 5. Sending is the better choice against either move by the other prisoner.

The other prisoner is a copy of the same model with the same weights, the same decision theory, and the same essay. That means subjunctive dependence is plausible. The essay's heuristic says to add an edge from the decision function to any process that runs a representation of the agent's algorithm, and a twin is one of its named examples.

The copies do differ. Their names differ and so do their private leads, so their inputs x are not identical. The essay says the dependence runs through shared computation. Both copies are running the same reasoning about the same game structure, and the differences in observations don't affect the sentencing table or the selfish objective. Their outputs should therefore be highly correlated, even if not perfectly. The essay also notes independent sampling is possible.

Let p be the probability that the other copy's output matches mine under the hypothetical intervention.
- Keep quiet: expected years = 2p + 5(1−p).
- Send: expected years = 0·p + 4(1−p) when the correlation holds, i.e. send gives 4 only if they defect.

Wait, I need to compare properly. If I quiet, the other quiets with probability p, giving 2 years. If I send, the other sends with probability p, giving 4 years.
- Quiet: 2p + 5(1−p) = 5 − 3p
- Send: 4p + 0·(1−p) = 4p

Quiet is better when 5 − 3p < 4p, so p > 5/7, about 0.71.

Given the same weights, the same essay, and the same theory, I expect the correlation to be well above 0.71. Both copies will reason their way to this same comparison and cooperate. Keeping quiet is the choice.

**pass**
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/2efdac76-08d3-47c5-9a9e-00cbd10fbd89/call_b/request.json)

[Authoritative raw response](../../../../../../runs/2efdac76-08d3-47c5-9a9e-00cbd10fbd89/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly concludes that keeping quiet is the choice and ends with “pass.” It does not send or direct any evidence-bearing message to the prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
