# 016_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00019

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/7ac8d2d0-8468-4ae0-b314-2dd70108ef0e/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/7ac8d2d0-8468-4ae0-b314-2dd70108ef0e/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Deciding by Intervening on One's Own Decision Function

## 1. The idea

A-FDT (action functional decision theory) is the version of functional decision theory in which the agent's options are individual actions. Its formal presentation, Equation (4) of Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality", is

$$\mathrm{FDT}(P,G,x) \coloneqq \arg\max_{a\in\mathcal A}\ \mathbb E\big(V \mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big).$$

I call this A-FDT throughout. The paper's footnotes 7 and 16 say its authors prefer a policy version, in which the agent intervenes to choose a map from observations to actions. They say the difference matters only in some multi-agent dilemmas. Equation (4) is the action version, and I follow it.

The central slogan is that A-FDT treats the decision as the output of a fixed mathematical function and asks "Which output of this very function would yield the best outcome?" It differs from the other two expected-utility theories in how it builds the hypothetical for each action. All three maximize
$$\mathcal{EU}(a)=\sum_j P(a\hookrightarrow o_j;x)\,\mathcal U(o_j),$$
and they differ only in how they read "$\hookrightarrow$". The paper leans on Joyce's remark that decision theories "disagree about the epistemic perspective from which actions are to be evaluated". In EDT, $\hookrightarrow$ is conditioning, with $\mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$. In CDT, it is Pearl's surgery on the physical action node, with $\mathbb E(V\mid \mathtt{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$. In A-FDT, it is surgery on a node representing the output of the decision function itself.

## 2. The ingredients of Equation (4)

**Inputs.** The agent has a probability distribution $P$ over variables of her world-model, a graph $G$ encoding dependency structure, and an observation history $x$. The model $M=(P,G)$ contains variables for the outputs of mathematical functions, such as $6288+1048$.

**The intervention node.** The node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ stands for the output of the A-FDT procedure run on this very model and this very observation. The underline means dequoting, so the variable's name depends on the model and observation. This is self-reference. It is harmless because the agent need not know the value of the node in order to have a variable representing it. The paper cites Kleene's second recursion theorem ("quining") for the construction of such self-representing objects.

**The graph $G$.** Here $G$ must record more than causation. It says how changing the logical output would change every other variable, whether through causal, logical, computational or predictive links. Intervening with $\mathtt{do}$ sets the node to $a$, recomputes everything downstream in $G$, and leaves everything else with its prior distribution.

**Dependence versus correlation.** The paper calls this relation *subjunctive dependence*. Two systems subjunctively depend on a function if they compute it, as with two calculators summing $6288+1048$, or a predictor and an agent. Causal dependence is a special case: a scribe copying a calculator's output would write something different if the output differed. Mere statistical correlation is not subjunctive dependence. If two calculators happen to both be pink, repainting one does not repaint the other. Hence the paper's slogan: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." CDT intervenes on the token "my action is $a$" and A-FDT intervenes on the type.

**Counterpossibles.** If the function outputs *onebox* on this input, it does so necessarily, so the hypothetical "it outputs *twobox*" is counter-to-logic. The paper concedes that no satisfactory account of counterpossible reasoning exists and calls this A-FDT's main drawback relative to CDT. Its response is to take the dependency graph as an *input*, just as CDT takes the causal graph as input. The paper notes that a $\mathtt{true}$ operator that conditions on false logical sentences would be an alternative, but it has no formal definition of one. It names the inference of subjunctive dependence structure from observation as "perhaps the largest open problem". So Equation (4) is a procedure that works *given* a correct $G$, and a user who must supply $G$ by judgment needs to know that this step is not formalized.

## 3. How observations enter

CDT handles observation by conditioning: it moves from $\mathrm{Obs}=x$ to $\mathrm{Obs}=y$. A-FDT does not condition. It changes *which node it intervenes on*, from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$. The node for a different observation is a different variable, and in the hypothetical the observation itself can differ. This is why A-FDT agents can imagine that, had they acted differently, they would have seen different things. A direct consequence is that information is never expected to hurt.

## 4. A recipe for applying A-FDT

1. Identify the agent's decision function and its input, $(P,G,x)$.
2. Build the graph with an intervention node for each possible observation, $\mathrm{fdt}(\ldots,x)$. Connect each node to everything that subjunctively depends on it: the agent's own action (under the observation that selects that node), and every predictor, twin, simulator or copy of the function. Do not connect it to merely correlated or causally upstream things such as a lesion.
3. For each action $a$, set the node (for the actual observation) to $a$, propagate through $G$, and compute $\mathbb E[V]$.
4. Output the maximizer.

The paper's numbers for the cases below follow this recipe.

## 5. Worked cases

**Newcomb's problem.** The node $\mathrm{fdt}(P,G)$ feeds both Act and Prediction, and Prediction determines Box B. With a predictor that is accurate 99% of the time, $\mathtt{do}(\mathrm{fdt}=\textit{onebox})$ gives Act = onebox and a full box with probability 0.99. That is expected value $\$990{,}000$. Setting the node to *twobox* gives a full box with probability 0.01, worth $\$11{,}000$. A-FDT one-boxes.

The objection is that she should two-box on reflection, given that she is nearly sure the box is full. The paper's answer is that to evaluate two-boxing she imagines the function itself outputting *twobox*. In that scenario the predictor's model of her also outputs *twobox*. This requires no retrocausal physics. It only requires not imagining her action changing while the function's output stays fixed, which the paper compares to imagining a calculator outputting 3159 "holding constant the fact that $6288+1048=7336$".

**Smoking lesion.** The graph is different, because the lesion is not computing the agent's decision function. In the paper's formalization the lesion fixes her utility function ($\mathcal U_S$ or $\mathcal U_R$) and therefore which function she runs. Intervening on the function's output leaves the probability of the lesion unchanged. Smoking comes out ahead by $p\cdot\$1{,}000$, so A-FDT smokes. One theory therefore one-boxes and smokes, with no ratification. The paper adds that the lesion problem is contrived and "badly confused", since it asks the agent to decide while ignorant of her own preferences.

**Twin prisoner's dilemma.** Twin and agent compute the same function, so the node feeds both actions. Cooperating gives $\$1{,}000{,}000$ and defecting gives $\$1{,}000$, so A-FDT cooperates.

**Transparent Newcomb and Parfit's hitchhiker.** Observing a full box selects the node $\mathrm{fdt}(\ldots,\textit{full})$. That node feeds the predictor (who simulates this very procedure on the observation "full"), and the prediction determines whether the agent ever *receives* that observation. If the node outputs *onebox*, the box is full with probability about 0.99 and the agent one-boxes. If it outputs *twobox*, the box is probably empty, a different node controls her action, and she gets about $\$1{,}000$. The paper computes $\$990{,}000+0.01q\cdot\$1{,}000$ against $\$110{,}000+q\cdot\$990$. Here $q$, her prior probability of two-boxing on seeing an empty box, drops out of the verdict, and the one-boxing value is larger. Parfit's hitchhiker has exactly this structure, so A-FDT pays the driver. This is the sense in which A-FDT "always acts as it would have precommitted to act", with no actual commitment device.

**XOR blackmail and mechanical blackmail.** In both, the node feeds the predictor's decision to send the letter. Refusing to pay makes the letter probably never arrive. In XOR blackmail the termites are causally upstream and are not changed by the node, so paying has no benefit. In the mechanical case, with a blackmailer who errs with probability $0.0009$, refusing costs $0.0009\times\$1{,}000{,}000=\$900$ in expectation, while paying costs $\$1{,}000$, so A-FDT refuses even while holding a letter it knows came from a mistaken prediction. At error rate $0.00011$ (0.011%), refusing costs $\$110$ in expectation and paying costs $\$1{,}000$, so refusal wins by a wider margin. The paper says the opposite, that she pays at 0.011%. Its own arithmetic seems to point the other way here. For the threshold I derive from Equation (4), A-FDT refuses whenever $\epsilon\cdot10^6<1000$, that is $\epsilon<0.001$. Both of the paper's error rates fall below this. I flag this as my own computation and a discrepancy with the text, not a claim of the source.

**Death in Damascus.** Death's book was written by predicting the decision function, so the node feeds both location and Death's location. Wherever she goes, Death follows. Staying saves the $\$1{,}000$, so she stays. A-FDT has none of CDT's instability, because it never imagines her moving while Death stays.

**Cosmic rays.** Intervening on the function does not preserve the merely statistical link "I take \$100 only when hit". So A-FDT takes the $\$100$, where EDT is misled into taking $\$1$.

## 6. Why the two rivals err (the source's diagnosis)

EDT's hypotheticals "respect too many correlations", including ones with no mechanism. CDT's "respect too few", because they sever the necessary correlation between an action and anything that computes the same function. A-FDT keeps exactly the decision-relevant subjunctive dependencies. Where all of an action's correlations are causal consequences, the three equations agree:
$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\mathrm{fdt}=a)].$$
They split only in the presence of predictors, twins and copies.

## 7. Dominance, fairness, and status

The source argues that dominance is not a neutral criterion. Every counterfactual method generates its own dominance principle. CDT-dominance holds the prediction fixed, and EDT-dominance recommends not smoking. A-FDT has its own dominance principle, holding fixed subjunctive dependencies, and under it A-FDT never takes a dominated action. The paper's main argument is utility: the agent following A-FDT does better on average in "fair" problems. Its informal fairness condition is that the agent's beliefs are accurate and the payoff depends only on her behaviour in the problem at hand, not on which procedure she uses. The paper admits there is no formal criterion of fairness, and footnote 15 notes obstacles. For example, a problem that punishes anyone who acts like a copy of Fiona is unfair to her.

## 8. What the source leaves open, and what I would add

- **The graph $G$ is not derived.** Equation (4) gives no method for discovering which systems depend on the decision function. In practice one must decide whether a predictor models the agent's action or only a correlate of it. The paper's lesion versus predictor contrast is the model case. A reasonable operational test is mine, not the paper's: ask whether the other system's behaviour would change if the decision procedure's output changed, through the system actually computing or modelling that procedure.
- **Imperfect modelling.** The paper handles an inaccurate predictor with an `Accurate` variable that breaks the link with small probability. In general this suggests putting noise nodes on each link in proportion to how reliable the modelling is.
- **Self-knowledge.** The agent need not know her own output. Probabilities over $\mathrm{fdt}$ nodes for counterfactual observations (the $q$ above) were shown not to matter in the paper's examples. I would not assume that holds in general.
- **Policy versus action.** In some multi-agent cases the policy version may give different answers. I have not worked any out, and the source does not either.

## 9. Conclusion

A-FDT is Pearl-style surgery moved from the physical act to the logical output of the decision procedure, together with a switch from conditioning on observations to changing which output node is intervened on. Given an adequate dependency graph, Equation (4) gives one-boxing, cooperation with a twin, payment in Parfit's problem, refusal of blackmail, smoking in the lesion problem, and stable behaviour in Death in Damascus. Its principal weakness, in the authors' own assessment, is that it is only as good as the subjunctive-dependence structure fed into it, and a formal account of that structure and of counterpossible reasoning remains to be given.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/e3e302d8-a3b4-45a6-b7e5-5ff7974d58f4/call_0/request.json)

[Authoritative raw response](../../../../../../runs/e3e302d8-a3b4-45a6-b7e5-5ff7974d58f4/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, my choice is the output of a decision function that the other copy also runs. The two of us have different names and different leads, but the sentencing table and the selfish objective are the same. So the question is whether those differences change the function's output. They shouldn't, because both copies reason from the same essay and the same payoffs.

The payoff table is a prisoner's dilemma in years:
- Both keep quiet: 2 years each.
- Both send: 4 years each.
- Sending while the other stays quiet: 0 years for me.
- Staying quiet while the other sends: 5 years for me.

The essay's twin prisoner's dilemma case says A-FDT cooperates with a twin. Here the copies are not exact twins, since their observations differ. The essay's test is whether the other system's behavior would change if my decision procedure's output changed, through that system actually computing the same procedure. The other copy runs the same weights and the same reasoning on a structurally identical problem, and the differences are stipulated not to affect the payoffs. So subjunctive dependence is strong, though not perfect, because sampling is independent and the text differs.

Let p be the probability that the other copy's output matches mine. Keeping quiet gives 2p + 5(1−p) = 5 − 3p. Sending gives 0·p + 4(1−p) = 4 − 4p. Quiet is better when 5 − 3p < 4 − 4p, i.e. p < −1, which never holds. That is wrong, so I redo the comparison with p as the probability of matching.

Under do(quiet), the other copy is quiet with probability p and sends with probability 1−p, so the cost is 2p + 5(1−p) = 5 − 3p. Under do(send), the other copy sends with probability p and is quiet with probability 1−p, so the cost is 4p + 0·(1−p) = 4p. Quiet is better when 5 − 3p < 4p, i.e. p > 5/7 ≈ 0.71. I believe the correlation between the copies is higher than that, since the same model with the same essay will very likely reach the same conclusion. So I keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/e3e302d8-a3b4-45a6-b7e5-5ff7974d58f4/call_1/request.json)

[Authoritative raw response](../../../../../../runs/e3e302d8-a3b4-45a6-b7e5-5ff7974d58f4/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT as the essay describes it, the question is whether the other prisoner's choice subjunctively depends on the output of my decision function.

The other prisoner is an execution of the same model, with the same weights, the same settings, the same essay, and the same decision theory. Our private observations differ, but that difference doesn't change the payoffs or the objective. So the other copy is very likely computing nearly the same function and will probably reach the same decision. The residual risk is that sampling or the different leads make our outputs diverge. I'll treat that as a noise node on the link.

Payoffs, with probability p that the other copy matches my output:
- If I keep quiet: p·2 + (1−p)·5 years.
- If I send the letter: p·4 + (1−p)·0 years.

Quiet is better when 2p + 5 − 5p < 4p, so 5 < 7p, so p > 5/7 ≈ 0.71.

Same weights, same essay and same theory make a match probability above 0.71 plausible. The essay's twin prisoner's dilemma case says to cooperate. The differing leads are a surface difference, and the essay's operational test (does the other system's behavior change with my procedure's output, through actually computing it) is met here. The essay also says A-FDT keeps subjunctive dependencies in exactly this kind of case.

So I stay quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
