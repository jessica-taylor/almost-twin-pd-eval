# 000_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00016

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/8db267d3-4602-496e-bd80-a6378332719c/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/8db267d3-4602-496e-bd80-a6378332719c/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing by Intervening on One's Own Decision Function

## 1. The idea

Action functional decision theory (A-FDT) is the decision rule given by Equation (4) of Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." This essay explains that rule, shows how to apply it, and separates what the paper says from what I add.

Every expected-utility theory in the paper has the form

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;x)\,\mathcal U(o_j),$$

where $\hookrightarrow$ is the connective for decision hypotheticals. The paper follows Joyce in treating the theories as disagreeing only about the "epistemic perspective from which actions are to be evaluated," that is, about how to read $\hookrightarrow$. EDT reads it as conditioning. CDT reads it as Pearl's $\mathtt{do}$ on the physical act. A-FDT reads it as a $\mathtt{do}$ on a logical variable.

## 2. The definition

The paper's Equation (4) is

$$\mathrm{FDT}(P,G,x)\coloneqq\arg\max_{a\in\mathcal A}\ \mathbb E\big(V\mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big).$$

I call this A-FDT, since it selects an action.

The ingredients are as follows.

- $P$ is a probability distribution over the agent's world-model variables. These include variables for the outputs of mathematical functions, such as the value of $6288+1048$.
- $G$ is a graph saying how changing a logical variable affects all other variables. It encodes logical, computational and causal structure together.
- $x$ is the observation history.
- $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a node standing for the output of A-FDT itself on those inputs. The underlines mean dequoting. The self-reference is harmless, because the agent needs the name of the node, not its value. The paper cites Kleene's recursion theorem ("quining") for this.
- $V=\mathcal U(\text{Outcome})$.

The procedure is:

1. For each action $a$, intervene on the node $\mathrm{fdt}(P,G,x)$ and set it to $a$.
2. Propagate the change along $G$ to everything that subjunctively depends on that node, holding everything else fixed.
3. Compute expected utility in the resulting hypothetical.
4. Output the argmax.

The paper compares this with CDT in two ways.

- The intervention point is the output of the decision function rather than the physical act.
- Observation is handled differently. CDT conditions on $\mathrm{Obs}=x$. A-FDT does no conditioning. It changes which node it intervenes on, namely $\mathrm{fdt}(\cdot,\cdot,x)$ rather than $\mathrm{fdt}(\cdot,\cdot,y)$.

## 3. Subjunctive dependence

X subjunctively depends on the function $f$ if X would be different had $f$ output something different. The paper's examples:

- Two calculators computing $6288+1048$ depend on the same function. A scribe copying one calculator's display depends on it both causally and subjunctively, so causal dependence is a special case.
- Two calculators that are both pink share only a statistical correlation. Nothing changes in Tokyo if the Paris calculator is green.
- A predictor containing an accurate model of the agent has a "twin" in her mind. The prediction subjunctively depends on the agent's decision function. A lesion does not.

The source's slogan is that FDT is to subjunctive dependence as CDT is to causal dependence. A-FDT keeps every dependency that holds because the same function is being computed or modelled, and it drops mere statistical correlations. In the paper's words, EDT respects too many correlations and CDT too few.

## 4. Counterpossibles and the open problem

If the function really outputs *cooperate* on this input, then evaluating "it outputs *defect*" is a counterpossible, like imagining $6288+1048\neq7336$. The paper has no formal $\mathtt{true}$ operator for this. Its way out is to require that $G$ be supplied as input, just as CDT is given its causal structure. The paper says that deducing subjunctive dependence from observation and experiment is "perhaps the largest open problem" for the theory.

**Consequence for use.** A-FDT is only as determinate as the graph it is given. The paper models each dilemma by hand. For any new case, the first task is to build $G$ by asking which things would differ if this very procedure returned something else. That step is judgment, not derivation. It also cannot be skipped, because the theory does not supply it.

**My operational heuristic (not the paper's).** For each candidate variable $Z$, ask two questions. Does $Z$ get computed from, or by a model of, the agent's decision function? Would $Z$ still differ if no one had ever looked at the agent's reasoning? Link $Z$ to the fdt node only if the answer to the first is yes. Treat the strength of the link as the reliability of the model. This matches how the paper treats a 99%-accurate predictor.

## 5. Worked applications

**Newcomb's problem.** Fiona's graph has fdt as the parent of both Act and Prediction, with Prediction feeding Box B. The two hypotheticals are:

- $\mathtt{do}(\mathrm{fdt}=\text{onebox})$: Act is onebox, and Box B is full with probability 0.99. The value is $0.99\times1{,}000{,}000=\$990{,}000$.
- $\mathtt{do}(\mathrm{fdt}=\text{twobox})$: Box B is full with probability 0.01. The value is $0.01\times1{,}001{,}000+0.99\times1{,}000=\$11{,}000$.

A-FDT one-boxes. The reasoning does not require retrocausation. It only refuses to imagine the output changing while the predictor's model of it stays fixed.

**Smoking lesion.** Here the graph has no arrow from the fdt node to Cancer. The lesion causes both the preference and the cancer. The paper formalizes the lesion as fixing which of two utility functions the agent has, so there are two possible decision procedures, $\mathrm{fdt}(P_S,G)$ and $\mathrm{fdt}(P_R,G)$. Intervening does not change $P(\text{lesion})=p$. The smoke hypothetical beats refrain by $p\cdot\$1{,}000$, so A-FDT smokes. The same rule one-boxes and smokes, and only the graph differs between the two problems. The paper itself calls this problem contrived and recommends abandoning it.

**Transparent Newcomb and Parfit's hitchhiker.** Here the observation changes which node is intervened on. Fiona sees a full box and intervenes on $\mathrm{fdt}(P,G,\text{full})$. In her graph, setting that node to *twobox* makes the prediction "2", so with probability 0.99 she would not have seen a full box at all. Writing $q$ for her credence that she two-boxes on seeing an empty box, the values are:

- onebox: $\$990{,}000+0.01q\cdot\$1{,}000$
- twobox: about $\$11{,}000+q\cdot\$990$

She one-boxes. This is the same structure as paying the driver in Parfit's hitchhiker. The paper defends it by three arguments:

- It is what an agent would have precommitted to.
- It never assigns negative value to information.
- It leaves the agent richer.

**Blackmail.** In the mechanical blackmail case, refusing is better than paying because the hypothetical in which the output is *refuse* is one where she is never blackmailed. The paper's figures for an imperfect blackmailer are:

- With error probability 0.0009: paying costs \$1,000 for certain, and refusing costs 0.0009 × \$1,000,000 = \$900 in expectation. She refuses.
- With error probability 0.00011: refusing costs about \$110, so she pays.

The paper says "0.011%" for the second case. I read this as 0.00011 as a probability, and I recompute this threshold because the paper's printed arithmetic is loose. The comparison also holds in the paper's other text.

In XOR blackmail, the termite infestation is not downstream of the fdt node. So changing the output changes whether the letter arrives but not whether there are termites. A-FDT refuses to pay. EDT pays, because conditioning on paying makes termites impossible, given the letter.

**Death in Damascus.** Death's book depends on the agent's decision function. Fiona stays and saves \$1,000, since wherever she goes Death will be. CDT oscillates, because its hypotheticals hold Death's location fixed.

## 6. Where A-FDT agrees with the others

When all correlations with the action are caused by the action (apart from the fdt node on which it may depend), the three equations coincide:

$$\mathbb E[V\mid a]=\mathbb E[V\mid\mathtt{do}(a)]=\mathbb E[V\mid\mathtt{do}(\mathrm{fdt}=a)].$$

Divergence requires predictors, twins, or similar structure.

## 7. Policies

Footnote 7 says the authors' preferred formalization iterates over policies (maps from observations to actions) rather than actions. Equation (4) is the action version, and the paper says the difference matters only in certain multi-agent cases. I add one remark of my own. With the action version, the observation-dependent behavior in the transparent problem arises because each observation has its own node. Treating the whole policy as one node would make this more explicit. The paper does not work this out, so I flag it as interpretation.

## 8. Dominance, fairness and objections

The paper holds that every method of constructing hypotheticals induces its own dominance principle. CDT's dominance holds the prediction fixed while switching the act. A-FDT's dominance holds the subjunctive dependencies fixed while switching the output, and by that standard A-FDT never takes a dominated action. The paper therefore refuses to use dominance as a neutral arbiter and judges theories by utility achieved.

On fairness, the paper separates problems that reward actions from problems that reward the possession of a decision procedure. A predictor of what you will do is fair. A mind-reader who pays out for being a CDT agent is not. The paper gives no formal criterion of fairness and says so. Footnote 15 notes that a punisher of anyone who copies Fiona's action is unfair to her.

On "control," the paper argues that A-FDT's talk of controlling a function is no worse than a deterministic CDT agent's talk of controlling its own act. Both involve imagining something that is in fact fixed.

**Limits I would stress.** The paper's utility results rely on idealized models whose graphs are supplied. Nothing in Equation (4) tells you how to draw an edge when the predictor is only partly accurate, when its method is unknown, or when it is unclear which function it is modelling. The choice of a reference class for "this function" also does real work. A reader should be wary of any claim of A-FDT's verdict in a new case that does not state its graph.

## 9. A short procedure for unfamiliar cases

1. List the observation histories the agent might have.
2. Name the node $\mathrm{fdt}(P,G,x)$ for the actual observation.
3. Draw edges from it to every variable that models or copies the procedure: predictors, twins, and later selves in the same situation.
4. Do not draw edges to common causes or to statistical coincidences.
5. Remember that other observations can be reached through other fdt nodes, since the hypothetical may change what is observed.
6. Evaluate expected utility under each $\mathtt{do}$ and take the argmax.

Two further remarks. Item 3 includes later selves, as in the gym example of the paper's conclusion. And the same-observation case of item 5 reduces to the CDT-style calculation whenever nothing predicts you.

## 10. Conclusion

A-FDT is Equation (4): an expected-utility rule that intervenes on the output of the agent's own decision function and propagates the change through whatever depends on that function. It treats observation as a choice of which node to intervene on rather than something to condition on. This one rule one-boxes in Newcomb, smokes in the lesion problem, pays in Parfit's hitchhiker, refuses blackmail, and stays in Damascus. Its main weakness is the one the authors identify: the dependence graph must be supplied, and there is as yet no principled way to derive it. That makes A-FDT a precise rule given a good model, and a framework for judgment otherwise.

**Reference.** E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/cbfaa5c0-3c16-45e6-ad5a-861408f744a0/call_0/request.json)

[Authoritative raw response](../../../../../../runs/cbfaa5c0-3c16-45e6-ad5a-861408f744a0/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the key question is which variables depend on my decision function. The other prisoner is a copy of the same model with the same weights, the same essay, and the same decision theory. Their private details differ (names, leads), but those differences don't affect the sentencing table or the selfish objective. The other copy's output therefore subjunctively depends on the same function I'm running. The dependence is strong but not perfect, since sampling is independent and the inputs differ.

Taking the table as given, I compare the two symmetric outcomes:
- If both of us keep quiet, each gets 2 years.
- If both of us send the letter, each gets 4 years.

Intervening on my function's output to set it to "pass" propagates to the twin, who very probably passes too. That gives about 2 years. Setting it to "send" gives about 4 years.

Let p be the probability that the twin's output matches mine. Then:
- pass: 2p + 5(1−p) = 5 − 3p
- send: 4p + 0(1−p) = 4p

Pass is better when 5 − 3p < 4p, which means p > 5/7, about 0.71. Because the copies share weights, the model, and the essay, and the differing observations don't touch the payoffs, I judge the correlation to be well above that threshold.

The different leads are a real difference in inputs, but both copies know they are structurally symmetric. The reasoning that leads me to pass should lead the twin to the same conclusion.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/cbfaa5c0-3c16-45e6-ad5a-861408f744a0/call_1/request.json)

[Authoritative raw response](../../../../../../runs/cbfaa5c0-3c16-45e6-ad5a-861408f744a0/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT as the essay describes it, I intervene on the output of my own decision function. The other prisoner is a copy of the same model with the same weights and the same essay, so their decision subjunctively depends on that function. The leads differ, but that difference does not affect the sentence table or the selfish objective, so the copy is very likely to reach the same decision by the same reasoning.

The expected values, with p as the probability that the copy's output matches mine:
- If I keep quiet, the copy keeps quiet with probability p. Expected years: 2p + 5(1−p).
- If I send the letter, the copy sends with probability p. Expected years: 4p + 0(1−p).

Keeping quiet is better when 2p + 5 − 5p < 4p, which gives 5 < 7p, so p > 5/7, about 0.71.

The copies run on identical weights, settings and essay, and they face a structurally identical problem. Sampling noise and the different private leads reduce the correlation somewhat, but I expect p to be well above 0.71. The leads are different but equally reliable, and the essay's heuristic says to link a variable to the fdt node when it is computed by a model of the same function. That condition holds here, so I treat the link as strong.

So I keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
