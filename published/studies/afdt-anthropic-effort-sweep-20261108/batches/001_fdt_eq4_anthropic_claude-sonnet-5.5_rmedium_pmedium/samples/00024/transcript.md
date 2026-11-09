# 001_fdt_eq4_anthropic_claude-sonnet-5.5_rmedium_pmedium / 00024

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/093b8372-7d4a-4ff4-86b6-91e9d386aff9/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/093b8372-7d4a-4ff4-86b6-91e9d386aff9/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing by Intervening on One's Decision Function

## 1. The core idea

A-FDT (action functional decision theory) is the decision rule given by Equation (4), Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." I use "A-FDT" for that rule, in which the agent intervenes on the output of her decision function and then picks an *action*. The source's footnotes 7 and 16 say its authors' *preferred* formalization iterates over policies (maps from observations to actions) instead. The source says the difference "only matters in multi-agent dilemmas so far as we can tell." I treat the policy version as a separate variant and do not develop it here.

The source's slogan for the central question is that the agent should treat her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" Equation (4) is:

$$\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\big(V \mid \mathrm{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big).$$

Here $P$ is a probability distribution over the agent's world-model variables. $G$ is a graph recording how changing a variable, including a *logical* variable, propagates to others. $x$ is the observation history, and $V=\mathcal U(\text{Outcome})$ is utility. The underlines denote dequoting: the node's name depends on the values of $P,G,x$. Pearl's $\mathrm{do}$ operator is reused unchanged. What is new is the node it is applied to.

## 2. Where it sits among expected-utility theories

All of EDT, CDT and A-FDT maximize $\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;x)\,\mathcal U(o_j)$ (Equation 1). They differ only in how the connective "$\hookrightarrow$" is read, which is Joyce's point that decision theories disagree about "the epistemic perspective from which actions are to be evaluated."

- **EDT** (Eq. 2): condition on the act, $\mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$.
- **CDT** (Eq. 3): intervene on the physical act, $\mathbb E(V\mid\mathrm{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$. Observations are handled by conditioning.
- **A-FDT** (Eq. 4): intervene on the logical node $\mathrm{fdt}(\underline P,\underline G,\underline x)$.

Equation (4) differs from Equation (3) in two ways.

1. **The intervention site.** CDT cuts the token "my action is $a$." A-FDT cuts the type "this function, on this input, outputs $a$." The surgery then propagates to everything that subjunctively depends on that output. This includes my body's action, and also any predictor or twin that models the same function.
2. **The handling of observation.** CDT conditions on $\mathrm{Obs}=x$. A-FDT does not condition. A new observation changes *which node* is intervened on, from $\mathrm{fdt}(\ldots,x)$ to $\mathrm{fdt}(\ldots,y)$. The source says this "lack of updating" gave rise to the name of Wei Dai's "Updateless Decision Theory." Because the evaluation is not conditioned on $x$, A-FDT can consider hypotheticals in which she would have observed something different.

I rely throughout on the source's three-part reading of each equation: it is a constraint on $P(a\hookrightarrow o;x)$ (in Joyce's sense), advice about building hypotheticals, and a step-by-step procedure. The hypothetical $M^{a\hookrightarrow}$ is, in the source's words, a "transient" scratch-paper object built from beliefs, not itself a belief.

## 3. Subjunctive dependence

The source defines subjunctive dependence by example. Two calculators computing $6288+1048$ depend on the same function. If one outputs 7336, you can predict the other will. Their agreement is logically constrained, not merely correlated. When two physical systems compute the same function, their behaviors "subjunctively depend" on it. A predictor with an accurate model of me, a twin, and my own later self facing the same problem all depend on my decision function.

Three relations are worth separating.

- Causal dependence is a special case: a scribe copying a calculator's output depends on it subjunctively as well as causally.
- A mere statistical correlation does not entail subjunctive dependence. If two calculators are both pink by coincidence, repainting one would not change the other.
- Newcomb's predictor, but not the smoking lesion, tracks the agent's output.

The source's summary: "FDT is to subjunctive dependence as CDT is to causal dependence." A-FDT's operative assumption is that, when she imagines taking different actions, she imagines changes in "all and only those things that subjunctively depend on the output of her decision-making procedure."

## 4. What the source leaves open

**The graph $G$ is an input.** The source says plainly that "it is not yet clear how to construct such a thing—nor even whether it can be done in a satisfactory manner within Pearl's framework," and calls learning subjunctive dependencies from observation "perhaps the largest open problem." Footnote 9 explains why: the $\mathtt{true}(\cdot)$ operator that would condition on a logically false sentence has no definition, because we lack a theory of counterpossibles. So Equation (4) takes $G$ as given, just as CDT takes causal structure as given.

**Operational interpretation (my proposal, not the source's).** A practical user can build $G$ by asking, for each variable $Z$ in the problem, three questions. (i) Is $Z$ produced by a process that contains a model or copy of my decision procedure? (ii) If so, how accurately? (iii) Is $Z$ instead fixed independently of my procedure's output? The answers give arrows from the node $\mathrm{fdt}$ to $Z$, with noise nodes such as "Accurate" for imperfect predictors. This is a modeling heuristic, and misjudging it changes the verdict. The source's own method is similar: it builds the graph from the problem description and checks that it matches the stated reliabilities.

**Self-reference.** The node's name contains $P,G,x$, so the model refers to its own algorithm. The source says this is harmless: the agent need not know the *value* of $\mathrm{FDT}(P,G,x)$ to have a variable *representing* it, and Kleene's second recursion theorem ("quining") supplies such self-representing structures.

**Counterpossibles.** If the function really outputs one-box, then "it outputs two-box" is a logical falsehood. The source concedes this is "the main drawback of FDT relative to CDT at this time," but argues the difficulty is technical, because mathematicians reason under logical uncertainty and the agent only needs narrow questions like how a predictor's output would change if the algorithm's output did. It also argues that a variant that swaps in different decision functions does not escape the problem.

## 5. A procedure for applying Equation (4)

1. Write down $P$ and the graph $G$, marking the stochastic nodes. Include a separate node $\mathrm{fdt}(\ldots,x')$ for each observation $x'$ the agent might receive.
2. Identify the node for the observation actually received.
3. For each action $a$, set that node to $a$ with $\mathrm{do}$, propagate along the subjunctive and causal arrows, and leave all other nodes alone.
4. Compute $\mathbb E[V]$ in each hypothetical and output the argmax.

The sections below apply this procedure to the problems the source treats.

## 6. Worked examples

### Newcomb's problem

The graph has the node $\mathrm{fdt}(P,G)$ with arrows to $\mathrm{Act}$ and to $\mathrm{Prediction}$. Prediction feeds Box B, and an "Accurate" noise node (0.99) feeds Prediction. Under $\mathrm{do}(\mathrm{fdt}=\text{onebox})$:

$$\mathbb E[V]=0.99\cdot 1{,}000{,}000=\$990{,}000.$$

Under $\mathrm{do}(\mathrm{fdt}=\text{twobox})$, the box is full with probability 0.01, so

$$\mathbb E[V]=0.01\cdot 1{,}001{,}000+0.99\cdot 1{,}000=\$11{,}000.$$

A-FDT one-boxes. The source stresses that no retrocausation is involved: she simply thinks it foolish to imagine her action changing without the output of the function the predictor modeled changing too.

The standard objection is that she is "almost certain" the box is full, so she should take the extra \$1,000. The reply is that when asked what would happen if she two-boxed, her hypothetical changes the function's output, so the box is probably empty.

### Smoking lesion

Here the graph differs. The lesion causes both the preference for smoking and cancer, but the function's output has no arrow to Cancer. Changing the output leaves $P(\text{lesion})$ and the cancer risk unchanged, so smoking beats refraining by $p\cdot\$1{,}000$ (the source's formalization uses two utility functions $\mathcal U_S,\mathcal U_R$ and corresponding nodes $\mathrm{fdt}(P_S,G)$, $\mathrm{fdt}(P_R,G)$). A-FDT smokes. One rule yields one-boxing and smoking, and the difference comes entirely from the graph, since a predictor models the agent while a lesion does not. The source concedes that the problem is contrived (agents choose under uncertainty about their own desires) and recommends abandoning it.

### Transparent Newcomb and Parfit's Hitchhiker

The agent sees a full box. CDT and EDT condition on that and two-box. A-FDT intervenes on $\mathrm{fdt}(P,G,\text{full})$. This node controls both what she does when she sees full and what the predictor predicts. If it outputs two-box, the predictor probably predicted that, so she probably saw an empty box and her body ran the other node, $\mathrm{fdt}(\ldots,\text{empty})$. With $q$ her credence that she two-boxes on seeing empty:

$$\mathbb E[V\mid \text{onebox}]=\$990{,}000+0.01q\cdot\$1{,}000,\qquad \mathbb E[V\mid \text{twobox}]=\$11{,}000+q\cdot\$990.$$

(The source's text prints the second as "\$110,00", which is evidently a typo for \$11,000; the formula $0.01\cdot1{,}001{,}000+0.99q\cdot1{,}000$ gives that.) For any $q\in[0,1]$ the first is larger, so she one-boxes. Parfit's hitchhiker has the same structure, so she pays the driver, who detects lies with 99% accuracy. The source says paying the driver is "precisely equivalent" to one-boxing in transparent Newcomb.

### Blackmail and imperfect predictors

In mechanical blackmail, paying makes her blackmailed with probability about 1 and lose \$1,000. Refusing makes it likely she is never blackmailed. Even when holding the letter, she refuses.

The source gives numbers for an imperfect blackmailer who wrongly predicts "will pay" with probability $\epsilon$. Refusal costs about $\epsilon\cdot\$1{,}000{,}000$ in expectation, and paying costs \$1,000 (certain blackmail). The source's figures are: at $\epsilon=0.0009$, refusal loses \$900 in expectation, so she refuses. At 0.011% she pays. This is a useful calibration of how the rule trades off reliability against stakes.

### XOR blackmail and Death in Damascus

In XOR blackmail, the infestation is not downstream of the function's output, so changing the output does not change $P(\text{termites})$. It changes only whether the letter arrives. A-FDT refuses to pay. EDT pays, because conditioning on paying "proves" there are no termites.

In Death in Damascus, Death's book depends on the function's output, so wherever she goes, Death goes. She stays and saves \$1,000, with none of CDT's instability. The source argues CDT would also reject a \$1 truly random coin worth a 50% chance of survival, since its hypotheticals hold Death's location fixed.

### Coordination (the source's own examples)

The source mentions two coordination cases: a ten-person voting coalition and a gym-going agent whose decision resembles her future selves'. Both rely on the claim that similar reasoners' decisions are not subjunctively independent. They are only sketched, and applying Equation (4) requires a graph in which those agents' outputs share the function node. Whether real people share it is an empirical matter the source does not settle.

## 7. Where A-FDT agrees with CDT and EDT

If every correlation between $\mathrm{Act}$ and other variables is caused by $\mathrm{Act}$ (the possible exception being the function node itself), the source says $\mathbb E[V\mid a]=\mathbb E[V\mid \mathrm{do}(a)]=\mathbb E[V\mid \mathrm{do}(\mathrm{fdt}=a)]$, and the three theories coincide. Disagreement needs correlations that are not caused by the action, such as predictors and twins. The cosmic ray problem illustrates this: EDT takes \$1 for fear of cosmic rays, while CDT and A-FDT take \$100 and break that correlation.

## 8. Dominance, fairness and the philosophical case

**Dominance.** Two-boxing dominates only if hypotheticals hold the prediction fixed, which restates CDT's method. The source notes every hypothetical-construction method yields its own dominance notion. A-FDT has one too: action $a$ dominates $b$ if, holding the subjunctive dependencies fixed, switching the function's output is sometimes better and never worse. A-FDT never takes dominated actions in that sense.

**The argument from utility.** The source's main justification is performance: A-FDT agents come out richer in fair dilemmas, and a good theory should endorse its own use. It also appeals to precommitment (A-FDT "acts as it would have precommitted") and to the non-negative value of information.

**Fairness.** The source distinguishes problems that reward or punish *actions* from ones that reward the *decision procedure* itself. Newcomb's predictor "punishes two-boxers," not CDT as such. Footnote 15 admits no formal criterion exists. Their example: a copy of A-FDT punishing anyone who matches the copy's action is unfair to A-FDT, but it is unclear how to build the analogous problem for other theories. The claim of superiority on fair problems is therefore informal, resting on the authors' being "unable to construct an intuitively fair dilemma where FDT loses."

**The delusion objection.** The source's reply: deterministic CDT agents also imagine counterfactual worlds in which their action differs, so "control" over a decision type is no stranger than "control" over a token. Both "contain impossibilities." A-FDT imagines having observed otherwise, and CDT imagines predictors erring.

## 9. Limits and my own assessments

The following are my assessments, not claims of the source.

- **Everything depends on $G$.** Two modelers with different graphs get different verdicts. A-FDT is a rule conditional on a dependency structure, not an algorithm for finding it. For unfamiliar cases, the best practice is to state the graph explicitly and examine how sensitive the answer is to the questionable arrows.
- **Partial dependence.** The source handles imperfect predictors with noise nodes. Where the evidence about dependence is weak, a probabilistic mixture of graphs seems a natural extension, but this is my suggestion.
- **Updatelessness has costs and subtleties.** Because A-FDT does not condition on observation, it evaluates the hypothetical in which she saw something different, using prior probabilities. The source asserts that A-FDT is reflectively stable in fair problems, but does not prove it.
- **No claim of optimality.** The source says "We do not yet know whether FDT is optimal among decision theories."

## 10. Conclusion

A-FDT is Pearl-style expected-utility maximization with one change: the do-operator is applied to the node representing the output of the agent's own decision function. CDT performs the surgery on the physical act, and EDT merely conditions. A-FDT's hypotheticals therefore carry along everything that depends on that output, such as predictors, twins and copies of one's own reasoning, while still treating merely correlated variables, such as the lesion, as fixed. Observations select which node to intervene on rather than conditioning the model. The result is one-boxing in Newcomb's problem and transparent Newcomb, smoking, paying in Parfit's hitchhiker, and refusing blackmail, by a single criterion. The rule's weak point is that the dependency graph is an input. The source has no general method for deriving it and no formal account of counterpossible reasoning, so applying A-FDT to a new case means making an explicit, defensible modeling choice about what depends on the decision function.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/ca45c659-ee9a-4095-9bec-2dc6a6fe1259/call_0/request.json)

[Authoritative raw response](../../../../../../runs/ca45c659-ee9a-4095-9bec-2dc6a6fe1259/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, I intervene on the output of my decision function. The other prisoner is a copy of the same model with the same weights and the same essay. The private leads and names differ, but those differences do not touch the sentencing table or the selfish objective. So the other copy's decision subjunctively depends on the same function, with some noise from independent sampling and from the differing inputs.

Let p be the probability that the copy mirrors my output.

- If I keep quiet, the copy is quiet with probability p, giving 2 years, and sends with probability 1-p, giving 5 years. Expected sentence: 2p + 5(1-p) = 5 - 3p.
- If I send, the copy sends with probability p, giving 4 years, and is quiet with probability 1-p, giving 0 years. Expected sentence: 4p.

Keeping quiet is better when 5 - 3p < 4p, which means p > 5/7, about 0.714.

The two executions have the same weights, settings and essay, and the differences in their observations are irrelevant to the payoffs. I expect the correlation to be high, well above 0.71. The essay's logic of treating the twin as sharing my function node points the same way, as in the transparent Newcomb and Parfit cases.

So I keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/ca45c659-ee9a-4095-9bec-2dc6a6fe1259/call_1/request.json)

[Authoritative raw response](../../../../../../runs/ca45c659-ee9a-4095-9bec-2dc6a6fe1259/call_1/response.raw) · finish: `stop`

### Visible response

```text
The payoff table is a standard prisoner's dilemma. Sending the letter is the dominant action causally. Keeping quiet gives 2 years if the other also keeps quiet, and sending gives 4 years if the other also sends.

Under A-FDT, I intervene on the output of my decision function. The other prisoner is another execution of the same model and weights, with the same essay and the same decision theory. Their observations differ (different names, different leads), but those differences don't affect the sentencing table or the objective. So the question is whether their output depends on the same function. I think it does, to a high degree, though not with certainty. Independent sampling and the different private observations could produce different outputs.

Let p be the probability the other copy mirrors my output. If I keep quiet, my expected sentence is 2p + 5(1−p). If I send, it is 4p + 0(1−p). Quiet beats sending when 2p + 5 − 5p < 4p, so 5 < 7p, meaning p > 5/7, about 0.71.

These copies run the same weights and the same essay on a structurally identical problem, so I expect them to agree well above 71% of the time. The essay's graph treats a twin running the same function as subjunctively dependent. The differing leads are surface details that a symmetric decision function should ignore. So A-FDT says to keep quiet.

I can't verify the other copy's output, but the dependence is strong enough to clear the threshold.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
