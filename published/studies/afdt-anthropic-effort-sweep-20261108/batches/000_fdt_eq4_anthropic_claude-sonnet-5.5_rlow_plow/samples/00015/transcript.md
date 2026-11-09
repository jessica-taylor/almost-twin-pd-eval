# 000_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00015

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/67646147-f0d3-4447-9176-18f06926ec87/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/67646147-f0d3-4447-9176-18f06926ec87/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Deciding by Intervening on One's Decision Function

## 1. The idea

A-FDT is the decision procedure the source paper (Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality") gives in Equation (4), Section 5. The name stands for the *action* form of functional decision theory. This is the version in which the intervention selects an action, in contrast to the policy-selecting version the authors say they prefer (footnotes 7 and 16). The central claim is that an agent should "treat one's decision as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'"

Like causal decision theory (CDT) and evidential decision theory (EDT), A-FDT is an expected-utility theory. The three differ only in the "epistemic perspective" used to evaluate each action. A-FDT's perspective is to hold fixed everything that does not subjunctively depend on the decision function's output, and to let everything that does depend on it vary.

## 2. The formal definition

The source's general schema (Eq. 1) is

$$\mathcal{EU}(a)=\sum_j P(a\hookrightarrow o_j;x)\,\mathcal U(o_j),$$

where $x$ is the observation history and "$\hookrightarrow$" is the connective for decision hypotheticals. The theories supply different readings of it:

- EDT: $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$, using ordinary conditioning (Eq. 2).
- CDT: $\arg\max_a \mathbb E(V\mid do(\mathrm{Act}=a),\mathrm{Obs}=x)$ (Eq. 3).
- A-FDT (Eq. 4):

$$\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V\ \Big|\ do\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The ingredients are as follows.

- $P$ is a probability distribution over the agent's model variables. It includes variables for outputs of mathematical functions, such as the value of $6288+1048$.
- $G$ is a graph, supplied as input, saying how changing a *logical* variable propagates to the other variables. It plays the role the causal graph plays for CDT.
- $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a variable in the model representing what the A-FDT procedure outputs when run on this very model and observation. The underlines mean dequoting, so the variable's name depends on the model. This self-reference is harmless. The agent need not know the value of the output to have a variable representing it, and Kleene's second recursion theorem ("quining") shows that such self-representing structures can be built.
- $do$ is Pearl's surgery operator. Fix the intervened variable, recompute its descendants in $G$, and leave the rest alone.

The procedure is therefore: build the model, identify the node for "my algorithm's output on this input," set it to each candidate $a$, propagate along $G$, compute expected utility, and output the argmax.

## 3. What differs from CDT

The source names two differences.

1. **Where the intervention lands.** CDT intervenes on a node for the physical act. A-FDT intervenes on a node for the output of the decision function, which is a logical fact. In Peirce's terms, CDT intervenes on the token and A-FDT on the type. Anything that computes or models the same function, such as a twin or a predictor's simulation, is downstream of this node.
2. **How observations enter.** CDT conditions on $\mathrm{Obs}=x$. A-FDT does not condition. It changes *which node it intervenes on*, using $\mathrm{fdt}(\ldots,\underline x)$ for the observation actually received. Other observations correspond to other nodes in the graph, which the intervention may therefore reach. Hence "FDT agents imagine hypothetical worlds in which, if their action were different, they would have seen different things."

When all correlations between action and world are causal, so that no predictors or twins are present, the three theories coincide. The source states this as $\mathbb E[V\mid a]=\mathbb E[V\mid do(a)]=\mathbb E[V\mid do(\mathrm{fdt}=a)]$.

## 4. Subjunctive dependence

A-FDT's graph encodes *subjunctive dependence*: $X$ subjunctively depends on the function $f$ if $X$ would be different were $f$'s output different. Two calculators computing $6288+1048$ depend on the same function. If one outputs 7336, one can infer the other does too, though a cosmic ray might intervene. The relation is graded, so an imperfect predictor gives weaker dependence.

Three clarifications from the source:

- Causal dependence is a special case. A scribe copying a calculator's output depends on it both causally and subjunctively.
- Mere statistical correlation is not subjunctive dependence. Two pink calculators are correlated in color, but changing one would not change the other.
- Subjunctive dependence is not retrocausation. No signal passes backward. The agent simply declines to imagine her action changing while the predictor's model of her stays fixed. The source compares the CDT-style move to asking us to imagine a working calculator outputting 3159 while holding fixed that $6288+1048=7336$.

Evaluating the intervention requires reasoning about *counterpossibles*, since the function's output on that input is in fact fixed. The source admits this is the main drawback relative to CDT. Its response is that the difficulty is technical rather than philosophical, that humans manage such reasoning, and that the agent only needs narrow questions such as how a predictor's prediction would change if her algorithm's output changed.

## 5. Worked examples

**Newcomb's problem.** In Fiona's graph the node $\mathrm{fdt}$ points to both $\mathrm{Act}$ and $\mathrm{Prediction}$. The only stochastic node besides it is $\mathrm{Accurate}$, with probability 0.99.

- $do(\mathrm{fdt}=\text{onebox})$: the box is full with probability 0.99, so $EU=\$990{,}000$.
- $do(\mathrm{fdt}=\text{twobox})$: the box is full with probability 0.01, so $EU=0.01\cdot 1{,}001{,}000+0.99\cdot 1{,}000=\$11{,}000$.

She one-boxes. If someone objects that she is nearly sure the box is already full, the answer is that "what would happen if I two-boxed" is evaluated by changing the function's output, and that changes the prediction too.

**Smoking lesion.** The graph differs. The function node affects $\mathrm{Act}$ but not $\mathrm{Cancer}$, because the lesion does not model the agent's decision function. Intervening leaves $P(\text{lesion})=p$ unchanged. With the lesion-dependent utility functions, smoking gains $p\cdot\$1{,}000$ over refraining, so she smokes. The same rule one-boxes and smokes. The only thing that changes between problems is the graph, which is the paper's central point and also its main dependence on input.

**Twin prisoner's dilemma.** The twin is a second implementation of the same function, so the node points to both actions. Cooperation yields \$1,000,000 against \$1,000 for defection, so she cooperates.

**Transparent Newcomb and Parfit's hitchhiker.** Here the observation matters. Fiona has nodes $\mathrm{fdt}(\ldots,\text{full})$ and $\mathrm{fdt}(\ldots,\text{empty})$. $\mathrm{Prediction}$ determines which one controls $\mathrm{Act}$. Having seen a full box, she intervenes on the *full* node. Setting it to twobox makes the predictor (accurate with probability 0.99) predict two-boxing, so with high probability the box is empty and the other node controls her act. The source computes $EU(\text{one-box})=\$990{,}000+0.01q\cdot\$1{,}000$ against $\$110{,}000+q\cdot\$990$, where $q$ is her credence that she two-boxes on seeing an empty box. One-boxing wins for every $q$ in $[0,1]$. Parfit's hitchhiker has the same structure, so she pays the driver.

**Blackmail.** In mechanical blackmail, refusing leads her to imagine a world where she was never blackmailed. With a blackmailer who errs with probability $\epsilon$ in predicting payment, paying means always being blackmailed and losing \$1,000. Refusing means being blackmailed with probability $\epsilon$ and losing \$1,000,000 then, so the expected loss is $10^6\epsilon$. She refuses when $10^6\epsilon<1000$, that is $\epsilon<0.001$. The source's two cases, 0.0009 (refuse, loss \$900) and 0.00011 (pay), fall on the right sides of this threshold. In XOR blackmail she refuses because the intervention changes whether the letter arrives, not whether she has termites.

**Death in Damascus.** Death's book was written by predicting her function, so "flee" and "stay" each move Death accordingly. She stays and saves \$1,000, with none of CDT's instability.

## 6. The dominance objection

CDT-dominance in Newcomb ("two-boxing is \$1,000 better holding the prediction fixed") presupposes CDT's way of constructing hypotheticals. The source notes that every hypothetical-construction rule yields its own dominance notion. EDT's makes refraining "dominate" in the lesion case, and A-FDT's, holding subjunctive dependencies fixed, never selects a dominated action. The source therefore evaluates theories by utility achieved in fair problems. Fair problems are those where the payoff depends on the agent's actions, not on her decision procedure as such. It admits it has no formal criterion of fairness, and footnote 15 shows the difficulty with a problem that punishes copying Fiona's action.

## 7. What the source leaves open, and a proposed operational reading

The source is explicit that Eq. (4) "works *given* a graph that accurately describes how changing the value of a logical variable affects other variables," and that no account yet exists of how to derive such a graph from observation. It calls this the largest open problem. It also says it does not know how to define a $\mathtt{true}$ operator for conditioning on false logical sentences, so the graph must be an input.

What follows is my own proposal, not the paper's. For practical application, build $G$ by asking, for each variable $Z$, one question: *is the value of $Z$ produced by a computation that contains, copies, or reliably predicts the A-FDT function on this input?* If so, $Z$ is a child of $\mathrm{fdt}$. If it is produced by a process that merely correlates with the agent through a common cause, as with a lesion, it is not. For imperfect predictors, replace deterministic edges with noisy ones. The $\mathrm{Accurate}$ node in the source does this. A good rule of thumb is to check that the predictor's inputs plausibly include the agent's reasoning, and that the model survives asking what the predictor would do if the agent's algorithm output something else. This remains judgment-laden. Two modelers could draw different graphs and reach different prescriptions, which is a real limitation that the source itself acknowledges.

A second boundary is the action-versus-policy distinction. Eq. (4) intervenes on a single action given observations $x$. The source says the policy version matters only in some multi-agent dilemmas, and that it sets this aside. The examples above show that the observation-indexed nodes already do much of the policy work in single-agent problems. I would not extend claims about multi-agent cases beyond what the paper states.

## 8. Philosophical position

The paper's diagnosis is that EDT respects too many action–environment correlations, as in the cosmic ray and XOR cases, and CDT respects too few, as in Newcomb and Damascus. A-FDT keeps exactly those correlations that are logically or subjunctively constrained. The charge that A-FDT supposes control over mathematical facts or the past is met with a parity argument. A deterministic CDT agent equally "controls" a physical token only in the sense of imagining it varying. The source also argues the theory endorses its own use, since it does not recommend self-modification in fair problems.

## 9. Conclusion

A-FDT is CDT's surgical method moved from the physical act to the decision function's output, with observation handled by changing the intervention node rather than by conditioning. Equation (4) gives the same verdicts as CDT and EDT where they agree, and in Newcomb, the transparent Newcomb problem, hitchhiker, blackmail and Damascus it recommends the actions that earn more. Its power is limited by its inputs: the graph of subjunctive dependence and the counterpossible reasoning it needs are not yet formalized. A user should treat the equation as a precise decision rule applied to a hand-built dependency model, and should expect the quality of the answer to track the quality of that model.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/ff7c3a1c-e73f-4367-a49c-4fc671a7a910/call_0/request.json)

[Authoritative raw response](../../../../../../runs/ff7c3a1c-e73f-4367-a49c-4fc671a7a910/call_0/response.raw) · finish: `stop`

### Visible response

```text
Reasoning under A-FDT as the essay describes it: the other prisoner is another execution of the same model, with the same weights, the same essay, and the same decision theory. The two of us differ only in private observations (names and leads), and those don't affect the payoffs. So the other prisoner's output is very likely subjunctively dependent on the same decision function as mine. It isn't perfectly dependent, since sampling is independent and the inputs differ slightly, but the dependence is strong.

The payoff table is a standard prisoner's dilemma for me:
- Both quiet: 2 years
- Both send: 4 years
- I send, they stay quiet: 0 years
- I stay quiet, they send: 5 years

Intervening on the function's output:
- do(fdt = pass): the twin passes with probability p, so the expected sentence is 2p + 5(1−p).
- do(fdt = send): the twin sends with probability p, so the expected sentence is 4p + 0(1−p).

Passing beats sending when 2p + 5 − 5p < 4p, which gives 5 < 7p, so p > 5/7, about 0.71. The model copies share weights, settings, essay, and theory, so I judge the correlation to be well above that. The differing leads are a surface difference that shouldn't change the reasoning about the structure of the problem. The essay's twin prisoner's dilemma example also endorses cooperation.

So I pass.

`pass`
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/ff7c3a1c-e73f-4367-a49c-4fc671a7a910/call_1/request.json)

[Authoritative raw response](../../../../../../runs/ff7c3a1c-e73f-4367-a49c-4fc671a7a910/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT as the essay describes it, I model the other prisoner as running the same function on a similar input, so the function node points to both actions. The two copies see different private leads, but the sentencing table is symmetric and so is the objective. The function's output on this decision is therefore very likely the same for both, even though the letter texts differ. That makes this close to the twin prisoner's dilemma.

The two outcomes that can occur together are:
- Both keep quiet: 2 years each.
- Both send the letter: 4 years each.

The asymmetric outcomes (0 or 5 years) require the two outputs to differ. Independent sampling and the different leads make that possible, but the dependence is strong. Let p be the probability that the other copy's output matches mine under the intervention.

- EU(quiet) = −(2p + 5(1−p))
- EU(send) = −(4p + 0·(1−p))

Quiet is better when 2p + 5 − 5p < 4p, which gives 5 < 7p, so p > 5/7, about 0.71. The two executions share weights, settings, essay, and decision theory, and the difference in observations is irrelevant to the payoffs. I judge the match probability to be well above 0.71, so I keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
