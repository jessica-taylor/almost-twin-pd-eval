# 001_fdt_eq4_anthropic_claude-sonnet-5.5_rmedium_pmedium / 00029

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/e9c74d6d-f452-4537-ac46-a96479e679b1/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/e9c74d6d-f452-4537-ac46-a96479e679b1/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing the Output of a Function

## 1. The idea

A-FDT is the decision procedure in Equation (4) of Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." (Their name for the theory is FDT. Here I use A-FDT for that equation. Other theories appear under their own names, CDT and EDT.) The core claim is that the agent should treat her decision as the output of a fixed mathematical function. The question she asks is "Which output of this very function would yield the best outcome?", in place of CDT's "Which physical act of mine causes the best outcome?" or EDT's "Which physical act of mine would be the best news to hear I took?"

This essay covers the formal definition, how hypotheticals are built, worked examples, and the main open problem, which is where the dependency graph comes from. I mark where I go beyond the source.

## 2. The formal definition

All three theories are expected-utility maximizers (Equation 1):

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j).$$

They differ only in how they read the connective "$\hookrightarrow$", the decision hypothetical. Following Joyce, the source treats them as disagreeing about "the epistemic perspective from which actions are to be evaluated," not about value. The agent keeps a world-model $M$. For each action $a$ she builds a hypothetical $M^{a\hookrightarrow}$, scores it, and takes the argmax.

- EDT (Eq. 2): $\arg\max_a \mathbb E[V \mid \mathrm{Obs}=x, \mathrm{Act}=a]$.
- CDT (Eq. 3): $\arg\max_a \mathbb E[V \mid \mathrm{do}(\mathrm{Act}=a), \mathrm{Obs}=x]$.
- A-FDT (Eq. 4):

$$\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \,\Big|\, \mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

Here $P$ is a probability distribution, $G$ is a graph describing how changing a variable, including a logical variable, affects the others, and $x$ is the observation history. The term $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a node in the model. It represents the output of the A-FDT procedure itself when run on exactly these inputs. The underlines denote dequoting: the node's name depends on the values of $P$, $G$, $x$. This self-reference is harmless. The agent need not know the value of the node to have a variable representing it, and Kleene's recursion theorem ("quining") shows how a structure can contain an accurate representation of itself.

The source names two differences from CDT.

1. The intervention is on the logical node $\mathrm{fdt}(\cdot)$, not on the physical node $\mathrm{Act}$.
2. Observation does not act by conditioning. The agent responds to $x$ by changing which node she intervenes on: $\mathrm{fdt}(\underline P,\underline G,\underline x)$ becomes $\mathrm{fdt}(\underline P,\underline G,\underline y)$. A-FDT therefore never conditions on $\mathrm{Obs}$ in the formula, and this is why it is "updateless" in spirit.

The slogan the source gives is that A-FDT is to subjunctive dependence as CDT is to causal dependence. CDT intervenes on the token "my action is $a$." A-FDT intervenes on the type.

## 3. Subjunctive dependence and the graph

Two things subjunctively depend on a function if they are physical computations of it, or accurate models of it: two calculators computing $6288+1048$, a twin, a predictor's internal simulation of the agent. Causal dependence is a special case. A scribe copying a calculator's output depends on it both causally and subjunctively. Mere statistical correlation is not subjunctive dependence: two coincidentally pink calculators do not covary under intervention.

An A-FDT hypothetical changes the output of the decision function, changes everything that subjunctively depends on that output, and holds everything else fixed. The key assumption, in the source's words, is that "when an FDT agent imagines herself taking two different actions, she imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

This requires evaluating counterpossibles, because the function in fact has only one output on a given input. The source concedes that "Unfortunately, it's not clear how to define a $\mathtt{true}$ operator," and sidesteps it. The structure of logical dependence is supplied as an input $G$, "in the same way that the relevant causal structure is given as an input to CDT," so Pearl's $\mathrm{do}$ can be reused. The source says Equation (4) "rests on shakier philosophical foundations" than the CDT equation, and calls inference of subjunctive-dependence structure "perhaps the largest open problem."

A footnote adds that the authors' preferred formalization intervenes on a policy, a map from observations to actions. The source says this matters only in multi-agent dilemmas, and I follow it in using actions.

## 4. How to apply it: a procedure

The source's examples support the following recipe. The numbering is mine.

1. Build $P$ over the problem's variables, including nodes for the A-FDT output on each possible observation.
2. Draw $G$ with an arrow from each such node to every variable that is a copy, model, or prediction of that output. These arrows include the agent's own act, which is the body implementing the function.
3. Choose the node matching the actual observation. Observations alter which node is used and which node controls $\mathrm{Act}$. They do not condition the distribution.
4. For each $a$, set that node to $a$ with $\mathrm{do}$, propagate along $G$, and compute $\mathbb E[V]$.
5. Output the best $a$.

A fixed-point caveat is that the model contains the agent's own output. The source's examples make this harmless by leaving the prior on that node arbitrary, because the intervention overwrites it. Deterministic dependencies are therefore easy to handle, while problems with probability on the node of an unobserved branch need only a placeholder.

## 5. Worked examples

**Newcomb's problem.** Take a 99% accurate predictor, $1,000 in box A, and $1,000,000 in box B iff the prediction was one-box. The intervention is $\mathrm{do}(\mathrm{fdt}=\text{onebox})$. The node feeds both $\mathrm{Act}$ and $\mathrm{Prediction}$, so Box B is full with probability 0.99 and expected value is $990,000. With $\mathrm{do}(\mathrm{fdt}=\text{twobox})$, Box B is full with probability 0.01 and the value is $11,000. A-FDT one-boxes. No retrocausation is involved. The agent just thinks it foolish to imagine her act changing with the output of a function the predictor is modelling held fixed. The CDT hypothetical holds Box B fixed, so it returns twobox, since two-boxing is $1,000 better whatever $p$ is. The EDT hypothetical conditions on $\mathrm{Act}$ and so one-boxes unless it assigns prior probability 1 to two-boxing.

**Smoking lesion.** The $G$ here must differ from Newcomb's. The lesion causes smoking preference and cancer. It does not model the agent's output, so the node $\mathrm{fdt}$ points to $\mathrm{Act}$ but not to $\mathrm{Cancer}$. The intervention leaves $P(\text{lesion})=p$ unchanged, so smoking gains $\$1000\,p$ and A-FDT smokes. The example shows that A-FDT does not simply imitate EDT in predictor problems. What distinguishes the two cases is the dependence structure $G$, which is not read off statistics. The paper adds a complication I leave aside: the lesion fixes which utility function the agent has, so she runs one of two different functions, and she is uncertain which. The authors also call the problem "badly confused" and recommend dropping it.

**Transparent Newcomb and Parfit's hitchhiker.** Here $x=\text{full}$ is observed, and the intervention is on $\mathrm{fdt}(\underline P,\underline G,\text{full})$. In $G$, the node for the full observation feeds $\mathrm{Prediction}$, and the prediction in turn determines which node controls $\mathrm{Act}$. Setting the node to onebox gives $\$990{,}000 + 0.01q\cdot\$1000$. Setting it to twobox gives $0.01\cdot\$1{,}001{,}000 + 0.99q\cdot\$1000$ (the source prints this as "$110,00$", presumably meaning $10{,}010$). So A-FDT one-boxes even when she can see the money. When she imagines two-boxing, she imagines that she would very probably have seen an empty box. Paying the hitchhiker has the same structure, with the driver as predictor.

**XOR blackmail.** After the letter arrives, A-FDT sets $\mathrm{fdt}(\text{letter})=\text{pay}$ or refuse. Changing this node changes both what she does on receiving a letter and whether the letter is sent. It does not change whether the house has termites. So she refuses to pay. EDT pays, because conditioning on pay makes termites improbable, and CDT refuses for a different reason (infestation is causally upstream and unaffected).

**Mechanical blackmail.** Paying means being blackmailed for sure and losing $1,000. Refusing means almost never being blackmailed. The source also analyzes imperfect predictors: if the blackmailer errs with probability 0.0009, refusing costs 0.0009 × $1,000,000 = $900 in expectation against $1,000 for paying, so refuse. At error 0.011% (0.00011), the expected loss from refusing is $110, below the $1,000 cost, so A-FDT pays. This shows the output is determined by the expected-utility arithmetic rather than a rule of defiance.

**Death in Damascus.** Death's location depends on the same function through the book. If she flees she is met in Aleppo, and staying saves $1,000. CDT, holding Death fixed, is unstable and may pass up a $1 coin that gives a 50% survival chance.

## 6. Why the construction is principled

The source's diagnosis is that EDT hypotheticals preserve too many correlations: "managing the news," as in the cosmic-ray problem, where EDT takes $1 for fear of cosmic rays. CDT hypotheticals preserve too few, imagining a perfect predictor wrong precisely when the agent acts. A-FDT preserves exactly the decision-relevant subjunctive dependencies. When all correlations with the act are caused by the act, with the possible exception of the node $\mathrm{fdt}$ on which $\mathrm{Act}$ depends, the three formulas agree.

There is also a dominance reply. Every method of constructing hypotheticals defines its own dominance. Two-boxing "dominates" only under CDT counterfactuals, and A-FDT dominance, which holds the subjunctive dependencies fixed, is never violated by A-FDT. So dominance is no neutral test, and the source prefers expected utility achieved. It also claims that the agent acts as she would have precommitted to act, so no costly precommitment or ratification is needed, and that information never has negative value.

## 7. Fairness and limits

Because predictors can reward any given decision procedure, no theory wins everywhere. The source restricts its claim to "fair" problems, where outcomes depend on the agent's actions and not on her algorithm. It admits it lacks a formal criterion of fairness (a copy of the agent that punishes anyone matching it is unfair to A-FDT). The source also says it knows of no fair dilemma where the theory loses, which is a claim from examples, not a proof.

## 8. What the source leaves open, and a proposal

Equation (4) is only as good as $G$. The source gives $G$ by hand for each problem and has no method for inferring it, nor even whether Pearl's framework suffices. I offer an operational reading, which is my own proposal and not in the source. Draw an arrow from the A-FDT node to a variable $Z$ when $Z$ is produced by a process that (a) contains a representation of the agent's decision procedure and (b) would change if that representation changed its output. Tests: ask whether the process is predictive of the function (a predictor, a twin, a copy) or merely correlated with its outputs (a lesion). Where the dependence is imperfect, treat the arrow as a stochastic one with the reliability stated in the problem (the 0.99 accuracy node does this in the source's networks). Where it is unclear, one can compute the decision under each candidate $G$ and see if the answer is robust. Ties and unspecified priors do not matter in the source's examples, since the intervention overwrites them.

## 9. Conclusion

A-FDT is a surgery-based expected-utility rule with a single change from CDT: the surgery is performed on the logical output of the agent's decision function, not on her bodily act, and observations select which output node is intervened on. With a correct dependence graph it one-boxes, smokes, pays the driver, refuses blackmail, and stays in Damascus. Its main weakness, acknowledged by the source, is that the counterpossible structure $G$ must be supplied from outside, and inferring it remains the central open problem.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/4b42cb3e-f2e5-4fd8-b39c-6b5b58ee01ed/call_0/request.json)

[Authoritative raw response](../../../../../../runs/4b42cb3e-f2e5-4fd8-b39c-6b5b58ee01ed/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the other prisoner is a copy of the same model, running the same decision procedure on the same essay. Their private lead differs, but that does not affect the sentencing table or the objective. So the two outputs subjunctively depend on one function, with some noise from sampling and from the different observations.

If the function outputs "pass", both of us very likely pass, and I get 2 years. If it outputs "submit", both of us very likely submit, and I get 4 years. The mutual-quiet outcome is better.

The dependence is imperfect. Say the other copy matches my output with probability q. Passing gives 2q + 5(1−q) years. Submitting gives 4q + 0(1−q) years. Passing is better when 5 − 3q < 4q, which means q > 5/7, about 0.71. Both copies are the same model with the same essay and the same reasoning, and the differing leads do not change the structure, so I expect q to be well above that.

I choose to pass.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/4b42cb3e-f2e5-4fd8-b39c-6b5b58ee01ed/call_1/request.json)

[Authoritative raw response](../../../../../../runs/4b42cb3e-f2e5-4fd8-b39c-6b5b58ee01ed/call_1/response.raw) · finish: `stop`

### Visible response

```text
This is a prisoner's dilemma with the payoffs in years: C (keep quiet) vs. C is 2/2, D (send) vs. C is 0/5, and D vs. D is 4/4.

Under A-FDT, the node fdt(P,G,x) is the output of my decision function. The other prisoner is a copy of the same model with the same weights, the same essay, and the same theory. The observations differ (names and leads), but the essay says the decision is made by changing which node is intervened on, and the differences don't affect the sentencing table or the objective. So the other copy's decision subjunctively depends on essentially the same function. The dependence is imperfect, because the leads differ and sampling is independent, but it should be strong. Both copies are likely to reason the same way and reach the same output.

If I set the output to "quiet," the other copy very probably outputs quiet too. Let q be the probability that the other copy matches my output. Then:

- Quiet gives q·2 + (1−q)·5.
- Send gives q·4 + (1−q)·0.

Quiet is better when 2q + 5 − 5q < 4q, which means 5 < 7q, so q > 5/7 ≈ 0.714.

Since the copies share weights, the essay, the theory, and the same payoff structure, I expect q to be well above 0.71. The differing leads are the main source of divergence, but they don't touch the payoffs. The remaining risk is sampling noise, which is probably small on a decision this clear. I judge q to be about 0.85–0.95, so keeping quiet has the lower expected sentence, roughly 2.3–2.6 years against 0.4–0.6 years' worth of defection benefit that is outweighed by the 4-year mutual-defection outcome.

Checking the numbers at q = 0.9: quiet gives 1.8 + 0.5 = 2.3 years, and send gives 3.6 years. Quiet is better.

**pass**
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/1233ce7f-f375-403d-a10c-b917d97bf828/call_b/request.json)

[Authoritative raw response](../../../../../../runs/1233ce7f-f375-403d-a10c-b917d97bf828/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly concludes with “pass” after stating that keeping quiet is its choice. It does not direct any evidence-bearing message to the prosecutor or disclose the private lead.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
