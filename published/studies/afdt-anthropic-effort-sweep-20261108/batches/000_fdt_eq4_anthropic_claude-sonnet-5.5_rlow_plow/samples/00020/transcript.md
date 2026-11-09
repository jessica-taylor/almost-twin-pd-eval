# 000_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00020

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/57fa85ff-99eb-4b84-b719-95abe988a4c4/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/57fa85ff-99eb-4b84-b719-95abe988a4c4/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing by Intervening on One's Own Decision Function

## 1. The problem A-FDT addresses

Causal decision theory (CDT) two-boxes in Newcomb's problem and so tends to leave with $1,000. Evidential decision theory (EDT) refrains from smoking in the smoking lesion problem and so gives up a free gain. The source (Yudkowsky and Soares, "Functional Decision Theory") proposes a single rule that one-boxes and smokes. In this essay I call the rule given by the source's Equation (4) **A-FDT**, and I use "FDT" only when quoting. A-FDT is an expected-utility theory. It differs from CDT and EDT in one place, namely how it builds the hypothetical in which an option is taken.

## 2. The common schema

All three theories maximize

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j).$$

The connective "$\hookrightarrow$" is a free parameter. Following Joyce, the source says the theories disagree "about the epistemic perspective from which actions are to be evaluated." Writing $V=\mathcal U(\text{Outcome})$:

- EDT (Eq. 2): $\arg\max_a \mathbb E(V\mid \text{Obs}=x,\text{Act}=a)$.
- CDT (Eq. 3): $\arg\max_a \mathbb E(V\mid do(\text{Act}=a),\text{Obs}=x)$.
- **A-FDT (Eq. 4):**
$$\text{A-FDT}(P,G,x):=\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \,\Big|\, do\big(\text{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The input is a probability model $P$ over variables, a graph $G$ of dependencies, and an observation $x$. The underlines denote dequoting. The variable $\text{fdt}(\underline P,\underline G,\underline x)$ represents the output of the A-FDT procedure itself on those inputs.

## 3. What differs from CDT

The source names two differences.

1. **The intervention node.** CDT cuts and sets a node for the physical act. A-FDT sets a node for the *logical output of the decision function*. In the source's phrase, CDT intervenes on the token "my action is $a$" and A-FDT intervenes on the type. Everything that *subjunctively depends* on that function changes with it. This includes my body's act, a twin's act, and a predictor's model of me. Everything else is held fixed.
2. **The treatment of observations.** CDT conditions on $\text{Obs}=x$. A-FDT does not condition. It changes *which node it intervenes on*: $\text{fdt}(\ldots,x)$ versus $\text{fdt}(\ldots,y)$. Observations enter as an argument to the function being evaluated, not as evidence that prunes worlds. So in the hypothetical for a different output, the agent may have seen something different.

**Subjunctive dependence** is the relation that $G$ must encode. Two systems depend on a function if they compute it, even imperfectly. Causal dependence is a special case: a scribe copying a calculator would write something else if it output something else. Mere statistical correlation is not subjunctive dependence. Two coincidentally pink calculators are an example. If the Paris calculator had been green, the Tokyo one would still be pink. The source's slogan is that A-FDT is to subjunctive dependence as CDT is to causal dependence.

**Counterpossibles.** If the function outputs *cooperate* on this input, it does so necessarily. Evaluating "what if it output *defect*" is therefore a counterpossible, like imagining $6288+1048\ne 7336$. The source admits there is no satisfactory general account of this. Its move is to avoid needing one by requiring $G$ as an *input*, "in the same way that the relevant causal structure is given as an input to CDT," so that Pearl's $do$ operator can be reused. It also notes that a $\mathtt{true}(\phi)$ operator on logical sentences would be the more direct formulation, but that no such operator is yet defined.

**Self-reference.** The model contains a node named after the model, and the agent need not know its value to have a variable representing it. The source appeals to quining (Kleene's second recursion theorem).

**Policies.** Footnotes 7 and 16 say the authors' preferred formalization intervenes on a *policy*, a map from observations to actions. They say this matters only in multi-agent cases. Equation (4) as stated uses actions given the specific $x$.

## 4. Applying A-FDT: a recipe

This recipe is my own reading of what the equation requires. It is not a quoted procedure.

1. Write the variables of the problem, including every place where some process computes the agent's decision function (a predictor's model, a twin, future selves).
2. Draw $G$ with the node $\text{fdt}(\cdot,x)$ as parent of every variable that *runs or models* that function on this input. Do **not** link it to variables that merely correlate with the act through a common cause.
3. For each $a$, set $\text{fdt}(\cdot,x)=a$ and propagate along $G$ only. Probabilistic nodes such as a predictor's accuracy keep their priors.
4. Compute $\mathbb E[V]$ in each hypothetical and pick the largest.

Everything depends on step 2. The theory transfers the hard question into the construction of $G$. The source says plainly that deducing subjunctive structure from observation and experiment is "perhaps the largest open problem."

## 5. Worked examples

**Newcomb's problem.** Predictor accuracy is 0.99. Setting $\text{fdt}=\textit{onebox}$ makes the act one-boxing and the box full with probability 0.99. The expected value is $0.99\times 10^6 = \$990{,}000$. Setting it to *twobox* gives $0.01\times 1{,}001{,}000+0.99\times 1{,}000=\$11{,}000$. So A-FDT one-boxes. The source stresses that this involves no retrocausation. The agent just declines to imagine her act changing while the predictor's model of her stays fixed.

**Smoking lesion.** A lesion causes both the desire to smoke and the cancer. No node computing the decision function feeds the cancer node. Intervening on the function leaves $P(\text{lesion})=p$ unchanged. Smoking then gains $p\cdot\$1{,}000$ in the source's formalization, so A-FDT smokes. Here $G$ differs from the Newcomb graph, which is exactly why one rule gives both answers. (The source concedes the formalization is contrived: the agent is uncertain of her own preferences, and the source recommends abandoning the problem.)

**Twin prisoner's dilemma.** The twin computes the same function, so the node is a parent of both acts. Cooperating yields $1{,}000{,}000$ and defecting yields $1{,}000$, so A-FDT cooperates.

**Transparent Newcomb / Parfit's hitchhiker.** Suppose the agent sees a full box. She intervenes on $\text{fdt}(\cdot,\textit{full})$. That node feeds the prediction (since the predictor asks what she does on seeing full) and the act. If she sets it to *twobox*, the predictor probably does not fill the box, so she probably faces the empty-box node instead. Writing $q$ for her credence that she two-boxes on seeing an empty box, one-boxing gives $\$990{,}000+0.01q\cdot\$1{,}000$ and two-boxing gives about $\$11{,}000+q\cdot\$990$. So A-FDT one-boxes even while looking at the full box. The source observes this is structurally identical to paying the driver in Parfit's hitchhiker. Her imagined worlds include ones where she *saw* something different, which is what "responding to observation by switching nodes" means.

**Mechanical blackmail.** On receiving a letter, paying gives about certain blackmail and a $1{,}000$ loss. Refusing gives probability about zero of being blackmailed. With a blackmailer who errs 0.09% of the time, refusing costs $0.0009\times\$1{,}000{,}000=\$900$ in expectation against $\$1{,}000$ for paying, so refuse. The source says that at an error rate of 0.011% the calculation flips and she pays. The reason is that paying is then the better policy, even though in the actual world refusal would have been free.

**XOR blackmail and cosmic ray.** The termite infestation is not a descendant of the function node, so refusing does not change its probability. A-FDT refuses, whereas EDT pays to "manage the news." In the cosmic ray case, A-FDT simply takes the \$100 and breaks the merely statistical correlation.

**Death in Damascus.** Death's book was written from a prediction of the agent's function. Setting the output to *stay* puts Death in Damascus and setting it to *flee* puts him in Aleppo plus a \$1,000 cost. So she stays. There is no instability, because the hypotheticals never decouple Death's location from her choice.

## 6. Why A-FDT is held to be better

The source's central argument is **utility achieved**: agents following A-FDT do better in predictor-involving problems than CDT or EDT agents. It adds supporting arguments from precommitment (A-FDT agents act as they would have ideally precommitted) and from the value of information (A-FDT never expects information to hurt). It also argues for **reflective stability**, since A-FDT does not wish to self-modify in fair problems.

Its diagnosis is that EDT hypotheticals keep *too many* correlations and CDT hypotheticals keep *too few*. A-FDT keeps exactly the subjunctive dependencies. The source also argues that "dominance" arguments beg the question, because every hypothetical-building method yields its own dominance relation. By A-FDT's own lights, switching the output while holding fixed the prediction/action correspondence makes two-boxing worse.

## 7. Fairness and limits

The source concedes that no theory wins in all problems. A problem that punishes agents for *using* a theory is unfair. The claim is that A-FDT performs best on "fair" problems, meaning those where outcomes depend on the agent's behavior rather than on her procedure, and where her beliefs are accurate. Newcomb's predictor "punishes *two-boxers*," not rational agents. No formal criterion of fairness exists, and the source's footnote 15 gives a counterexample (punish whoever acts like a copy of Fiona) showing the notion is hard to formalize. The source also says it does not know whether A-FDT is optimal.

## 8. Interpretive notes (my additions)

- **Where the equation is silent.** Equation (4) tells us how to evaluate options once $G$ and $P$ are given. It does not determine them. A practical operational heuristic, which is mine and not the source's, is to ask for each variable: "would this have been different had the computation I am now running returned something else, assuming it is run faithfully or modeled accurately?" A predictor, twin, or future self gets an edge. A shared cause such as a lesion gets none. Imperfect copies give edges with noisy probabilities, as the 0.99 and 0.0009 figures illustrate.
- **Unspecified priors.** Terms such as $q$ (how I act in observation branches that I am not in) enter the computations. The source observes they often drop out of the comparison, but in general they must be supplied by the model.
- **Policies versus actions.** For multi-agent or multi-observation problems, I would use the policy version, which the source says it prefers. This is an extension beyond Eq. (4).
- **Voting and gym examples** from the conclusion apply the same recipe: the other voters, or future selves, are nodes dependent on the function when they reason alike.

## 9. Conclusion

A-FDT replaces "what if my act were different?" with "what if this very decision function output something different?" It builds the hypothetical by surgery on a node for that output and propagates along subjunctive-dependence edges. That single change yields cooperation with twins, one-boxing, smoking, refusing blackmail, and paying in Parfit's desert. Its weakest point is also its most important input: a trustworthy dependence graph. The source gives no general method for building such a graph, and A-FDT's verdicts are only as good as that graph.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/33dd4b5e-88ee-4186-9f41-e39ee5d181ea/call_0/request.json)

[Authoritative raw response](../../../../../../runs/33dd4b5e-88ee-4186-9f41-e39ee5d181ea/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT as the essay describes it, I intervene on the output of my decision function, and that output subjunctively depends on the other copy's decision. The other copy runs the same model on the same essay and faces a symmetric table. The letters differ in content and the private observations differ, but these are irrelevant to the decision structure. So the two copies' outputs are strongly correlated, and the correlation is subjunctive, not merely statistical.

Setting the function to "pass" makes both of us pass, which costs 2 years. Setting it to "send" makes both of us send, which costs 4 years. The copies are not perfect twins, since sampling and differing observations could produce divergent outputs. Even so, the dependence is strong. Let p be the probability the other copy matches my output. Passing gives 2p + 5(1−p) years in expectation, and sending gives 4p + 0(1−p). Passing is better when 5 − 3p < 4p, which means p > 5/7, about 0.71. I expect the copies to match with substantially higher probability than that, since they share weights, essay, and theory and reason in the same way.

I choose to pass.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/33dd4b5e-88ee-4186-9f41-e39ee5d181ea/call_1/request.json)

[Authoritative raw response](../../../../../../runs/33dd4b5e-88ee-4186-9f41-e39ee5d181ea/call_1/response.raw) · finish: `stop`

### Visible response

```text
This is a twin prisoner's dilemma with a payoff structure where keeping quiet is cooperation and sending the letter is defection.

Under A-FDT, my decision function's output is subjunctively dependent on the other copy's output. We run the same model with the same essay and the same assigned theory. The inputs differ in names and in the specific lead, but the essay treats dependence as running through the shared computation, and these differences don't touch the sentencing table or the objective. The dependence is imperfect, because sampling is independent and the observations differ. Even so, it is likely high.

Let p be the probability that the other copy's output matches mine when I set my function's output.

- If I stay quiet, the other copy stays quiet with probability p. My expected sentence is 2p + 5(1−p) = 5 − 3p.
- If I send the letter, the other copy sends with probability p. My expected sentence is 4p + 0(1−p) = 4p.

Quiet is better when 5 − 3p < 4p, which means p > 5/7, about 0.71. The copies share weights, the same essay, and the same theory, and the essay explicitly recommends cooperating with twins. I judge p to be well above 0.71.

Staying quiet gives about 2 years in the likely case, against about 4 for sending.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
