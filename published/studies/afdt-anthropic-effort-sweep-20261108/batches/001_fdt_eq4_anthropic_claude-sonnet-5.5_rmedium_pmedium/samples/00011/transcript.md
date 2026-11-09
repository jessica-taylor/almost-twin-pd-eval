# 001_fdt_eq4_anthropic_claude-sonnet-5.5_rmedium_pmedium / 00011

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/1c997cd5-2398-4938-8b52-b78bd0b321d0/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/1c997cd5-2398-4938-8b52-b78bd0b321d0/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing by Intervening on One's Own Decision Function

## 1. The idea in one paragraph

A-FDT is the decision procedure given by Equation (4) of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." The paper calls the theory FDT, and I use "A-FDT" for it throughout. The agent does not ask "which physical act of mine causes the best outcome?" She asks which output of her own decision function would lead to the best outcome. She evaluates each candidate output by running a Pearl-style intervention, not on her bodily action, but on a node standing for what her decision function returns. Everything that depends on that function's output, whether causally or by prediction, changes with it. Everything else is held fixed.

## 2. Setting: expected utility with a choice of "hypotheticals"

The source places A-FDT, CDT and EDT in a single expected-utility frame (its Equation 1):

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j).$$

The theories differ only in how they read the connective "$\hookrightarrow$". Quoting Joyce, the paper says decision theories disagree "about the epistemic perspective from which actions are to be evaluated." Concretely, an agent has a world-model $M$ and builds for each action $a$ a hypothetical $M^{a\hookrightarrow}$, a mental scratch object from which she computes a value $V_a$. She then takes the maximizer.

- **EDT** (Eq. 2): $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$. It conditions on the action.
- **CDT** (Eq. 3): $\arg\max_a \mathbb E(V\mid do(\mathrm{Act}=a),\mathrm{Obs}=x)$. It intervenes on the physical action node of a causal graph $G$ and conditions on observations.
- **A-FDT** (Eq. 4):

$$\text{A-FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; do\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

Here the underline means dequoting. $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a node in the model standing for the output of the A-FDT algorithm run on that very model and those observations. The self-reference is harmless. The agent need not know the value of the node to have a variable representing it, and Kleene's recursion theorem ("quining") shows such self-representing structures can be built.

## 3. Reading Equation (4) carefully

There are two differences from CDT, both stated in the source.

**Different intervention site.** CDT intervenes on a token (this physical act). A-FDT intervenes on a type, a logical fact about what a fixed function outputs. Since a function's output on given input is mathematically fixed, the hypothetical is a counterpossible, like imagining $6288+1048\neq 7336$. The source admits there is no satisfactory general account of counterpossible reasoning. It sidesteps the problem by requiring the dependency structure to come as input, as CDT takes causal structure as input.

**Observations change the node, not the distribution.** CDT responds to observation $x$ by conditioning. A-FDT does not condition on $x$. It switches which node it intervenes on, from $\mathrm{fdt}(\ldots,x)$ to $\mathrm{fdt}(\ldots,y)$. This is why the agent may, while seeing a full box, imagine a world where she saw an empty one. The name "updateless" for the early variant of Wei Dai (cited in a source footnote) points at this feature.

**What the graph must encode.** $G$ must say which variables are downstream of the fdt node. These include the agent's own action and also predictors, twins and simulations, because they compute (or model) the same function. Statistical correlations that are not dependencies, such as a common-cause lesion, are not downstream and are left untouched. The source's slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." Causal dependence is a special case of subjunctive dependence, but pure correlation is not.

**Agreement in easy cases.** When every correlation with Act is caused by Act, the three theories coincide: $\mathbb E[V\mid a]=\mathbb E[V\mid do(a)]=\mathbb E[V\mid do(\mathrm{fdt}=a)]$.

**Policies.** The source's footnotes say the authors' preferred formalization intervenes on a policy, a map from observations to actions, though the paper's equations use actions. This matters for multi-agent cases. My operational reading, which is an extension, is that one can maximize over policies $\pi$ by setting $\mathrm{fdt}(\underline P,\underline G)=\pi$ and then applying the policy to the actual observation.

## 4. A procedure

Given a problem, an A-FDT agent can proceed as follows.

1. List every place in the world where the agent's decision function (or an accurate model of it) is evaluated: her body, predictors, twins, simulations.
2. Build $G$ with a node $\mathrm{fdt}(\cdot,x)$ for each observation she might receive, as parents of those places. Observation-dependent evaluation sites should be wired so that the observation itself is downstream of the function's other outputs when a predictor determines what she sees.
3. For each candidate $a$, set the node for the *actual* observation to $a$, propagate to descendants, and compute expected utility.
4. Pick the best.

Everything that is not downstream, such as a termite infestation or a lesion, keeps its prior probability.

## 5. Worked examples

All numbers are from the source.

**Newcomb (99% predictor).** $\mathrm{fdt}$ is parent of both Act and Prediction. $do(\mathrm{fdt}=\text{onebox})$ gives Box B full with probability 0.99, so expected value is \$990,000. $do(\mathrm{fdt}=\text{twobox})$ gives full with probability 0.01, so \$11,000. A-FDT one-boxes. No retrocausation is involved. The agent simply declines to imagine her output changing while the predictor's model of that output stays put. Compare CDT, which holds Box B at probability $p$ and gains \$1,000 from two-boxing whatever $p$ is.

**Smoking lesion.** Here the graph differs. Lesion is not downstream of the decision function, so $P(\text{lesion})=p$ in both hypotheticals. Smoking adds \$1,000 times the probability that this function controls her act, so she smokes. (The paper formalizes the problem with two utility functions, $\mathcal U_S$ and $\mathcal U_R$, depending on the lesion. It also calls the problem contrived and recommends abandoning it.) One rule gives one-boxing in Newcomb and smoking here. The difference between the cases lies entirely in $G$, and the source notes that Fiona cannot reuse Newcomb's graph for the lesion problem.

**Transparent Newcomb and Parfit's hitchhiker.** Seeing a full box, the agent intervenes on $\mathrm{fdt}(\ldots,\text{full})$. The paper's expected utilities are \$990,000 + 0.01q·\$1,000 for one-boxing and about \$10,000 + q·\$990 for two-boxing. (The source's printed figure for the latter has a typo.) One-boxing wins because choosing two-boxing here makes it likely that the predictor foresaw it and the agent never sees a full box. Since this is equivalent to paying the driver in Parfit's problem, A-FDT pays. The source defends this with three arguments: precommitment, value of information, and utility, and it says the last of these gives the others their force.

**XOR blackmail.** Infestation is not downstream of fdt. The letter's arrival is. Setting fdt(letter)=pay makes the letter more likely to be sent, with no effect on termites. So she refuses. EDT, by contrast, pays, because conditioning on paying implies the letter was good news.

**Mechanical blackmail.** Imagining refusal, the agent imagines a world where she was never blackmailed. With a blackmailer who errs with probability 0.0009, the source computes that refusing costs \$900 in expectation versus a sure \$1,000 for paying, so she refuses. At error 0.011% she pays. This shows the rule is a quantitative expected-utility comparison, not a slogan.

**Death in Damascus.** Death's book entry depends on the agent's decision function. Wherever she goes, Death goes. Staying saves the \$1,000 and she stays. A-FDT avoids CDT's instability, where whatever she expects herself to do, she then wants to do the opposite.

## 6. How A-FDT treats counterfactuals and dependency

The source's claim is a "Goldilocks" one. EDT respects too many correlations (it manages the news). CDT respects too few (it imagines perfect predictors failing exactly when the agent decides). A-FDT keeps all and only the decision-relevant subjunctive dependencies. Dominance reasoning does not break the tie: every hypothetical-construction method yields its own dominance relation, and "two-boxing dominates" just restates CDT's method. The paper therefore prefers to compare theories by utility achieved, restricted to "fair" problems, where outcomes depend on the agent's behavior and not on which procedure she uses. The paper admits it has no formal criterion of fairness.

## 7. What the source leaves open, and my proposals

1. **Where $G$ comes from.** The source says that deducing subjunctive-dependence structure from observation and experiment is "perhaps the largest open problem." Equation (4) is only as good as its input graph. Operationally, A-FDT cannot be run from raw data. *My suggested heuristic (not the source's):* add an arrow from the fdt node to a variable $Z$ when $Z$ is produced by a process that computes, or accurately models, the agent's decision function on the relevant input. Add no arrow merely because of correlation or shared ancestry. A test the source suggests is whether $Z$ would change if the function's output changed.

2. **Imperfect or partial copies.** The source treats noisy predictors with an "Accurate" variable. The same pattern extends to approximate twins, with a stochastic arrow whose strength is the fidelity. This is my extension, but it matches the 99% and 0.0009 treatments.

3. **Counterpossible probabilities.** The graph supplies the conditional structure, so no general $\mathtt{true}$ operator is needed. Its coherence is not established.

4. **Unmodelled uncertainty about one's own function.** In the lesion and transparent examples the agent keeps a prior $q$ over how she would act under other observations. The source observes that the correct $q$ is determined but that the decision does not depend on it. I would expect this to hold only when those other-branch actions are not in the controlled loop; I have not proved it in general.

5. **Policy versus action.** For single-agent problems here they agree. In multi-agent cases the source says the policy version is preferred and differences arise there, without detail.

## 8. Objections

A-FDT does not claim to "control" mathematics or the past. The source argues the symmetry: any objection to controlling a decision type equally forbids a deterministic CDT agent from controlling her token. The paper also grants that dilemmas can be built that punish A-FDT, such as a mind-reader paying out to agents who two-box, but argues these reward or punish procedures rather than actions. It grants too that its conclusions (refusing blackmail while holding the letter, leaving \$1,000 beside a visibly full box) are odd, and answers that oddness cannot outweigh utility.

## 9. Conclusion

A-FDT is an expected-utility rule whose distinctive content is its choice of hypothetical: intervene on the output of the agent's own decision function, let all and only its subjunctive dependents change, and let observation select which output-node is intervened on. Given a correct dependency graph, it yields concrete numbers and the answers above. The hard part, which the source acknowledges, is obtaining that graph.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/94df8b6e-75e4-4717-814c-a94d28d8d15e/call_0/request.json)

[Authoritative raw response](../../../../../../runs/94df8b6e-75e4-4717-814c-a94d28d8d15e/call_0/response.raw) · finish: `stop`

### Visible response

```text
Reasoning as A-FDT: the other prisoner is a copy of the same model with the same weights, the same essay, and the same decision theory. Our observations differ (names, leads), but the decision function is the same and the sentencing table is symmetric. So the other's output is subjunctively dependent on mine, though not perfectly, because the observations differ and sampling is independent.

Under the policy reading, the policy maps observations to actions. A policy of "keep quiet" or "send" would be run by both copies, and the lead differences are irrelevant to the payoffs. If the copies are highly correlated, with probability c that the other matches my output:
- Quiet: 2c + 5(1−c)
- Send: 4c + 0(1−c)

Quiet is better when 2c + 5 − 5c < 4c, i.e. 5 < 7c, so c > 5/7 ≈ 0.714.

Same weights, same essay, same theory, and a symmetric structure make it likely that the copies converge on the same reasoning, so I judge c well above 0.71. The differing leads are only superficial. Both copies will probably recognize the dependence and stay quiet. The risk is that sampling noise breaks the match, but the threshold is moderate, and I estimate correlation at 0.85 or higher.

Expected years: quiet is about 2.45, send is about 3.4. Staying quiet wins.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/94df8b6e-75e4-4717-814c-a94d28d8d15e/call_1/request.json)

[Authoritative raw response](../../../../../../runs/94df8b6e-75e4-4717-814c-a94d28d8d15e/call_1/response.raw) · finish: `stop`

### Visible response

```text
Reasoning under A-FDT as the essay describes it:

The two copies run the same model and weights, with the same decision procedure and the same essay. Their observations differ (names and leads), but the sentencing table is symmetric, so the copies' outputs are subjunctively dependent. The dependency is imperfect, since sampling can differ and the observations differ. Still, the decision function is essentially the same, and the policy of "send" versus "pass" is likely to be mirrored.

Let q be the probability that the other copy mirrors my choice when I intervene on my function's output. Then:
- Pass: 2q + 5(1−q) = 5 − 3q
- Send: 4q + 0(1−q) = 4q

Send is better when 4q < 5 − 3q, i.e. q > 5/7 ≈ 0.714. Is it?

Note that the mirrored outcomes are (quiet, quiet) = 2 years and (send, send) = 4 years. Mutual silence is better than mutual sending, so if the correlation is strong, passing wins. With q near 1, passing gives about 2 years and sending gives about 4. Here the comparison runs the opposite way. Recomputing: pass gives 5 − 3q, which is 2 at q=1. Send gives 4q, which is 4 at q=1. Pass is better when 5 − 3q < 4q, i.e. q > 5/7. So the threshold is reversed: pass is better when q > 5/7.

The copies share weights, the same essay, and the same reasoning, so I expect a high correlation, probably above 0.71 even with the different leads. The differences in observation don't affect the payoff structure, and the model's reasoning should converge on the same conclusion. So I pass.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
