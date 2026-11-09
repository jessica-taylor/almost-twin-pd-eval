# 000_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00002

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/4436e056-8d60-4e6a-bfe0-58ed7c6a283b/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/4436e056-8d60-4e6a-bfe0-58ed7c6a283b/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing by Intervening on One's Decision Function

## 1. The idea

Most decision theories say: evaluate each available act by building a hypothetical in which that act is taken, then choose the act whose hypothetical has the highest expected utility. They differ only in how the hypothetical is built. Yudkowsky and Soares ("Functional Decision Theory: A New Theory of Instrumental Rationality") present one such theory. This essay calls it **A-FDT** and takes the paper's Equation (4), Section 5, as its definition. I separate what the paper says from what I add.

The paper's slogan is that the agent should treat her decision as "the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'"

## 2. The formal definition

All the theories discussed here are expected-utility theories. They maximize

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

where $\hookrightarrow$ is the connective for decision hypotheticals. The paper follows Joyce in treating the choice of interpretation of $\hookrightarrow$ as the free parameter that distinguishes the theories. The paper's formalizations are:

- Evidential decision theory (EDT), Eq. (2): $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$. This is conditionalization.
- Causal decision theory (CDT), Eq. (3): $\arg\max_a \mathbb E(V\mid \mathtt{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$. This is Pearl surgery on the physical act.
- **A-FDT, Eq. (4):**

$$\text{A-FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The ingredients are as follows.

- $P$ is a probability distribution over variables. These include variables for the outputs of mathematical functions, such as the value of $6288+1048$.
- $G$ is a graph encoding how a change in a logical variable propagates to other variables. Its edges include causal ones and also subjunctive dependencies, meaning edges from a function's output to every physical system that computes or models that function.
- $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a node representing the output of the A-FDT algorithm itself on that model and that observation. The underlines mean dequoting, so the node's name depends on $x$. Self-reference is handled by quining (Kleene's recursion theorem). The agent need not know the node's value in order to have a node that represents it.
- $\mathtt{do}$ is Pearl's operator. It sets the node and recomputes everything downstream of it in $G$, leaving the rest alone.

The paper identifies two differences from CDT. First, the intervention is on a logical variable, the algorithm's output, and not on the physical act. Second, observations are handled differently. CDT conditions on $\mathrm{Obs}=x$. A-FDT never conditions on the observation. It changes which node it intervenes on, $\mathrm{fdt}(\ldots,x)$ versus $\mathrm{fdt}(\ldots,y)$. Footnote 7 adds that the authors' preferred version intervenes on a *policy*, a map from observations to actions. This changes nothing in the paper's examples, though it matters in some multi-agent problems.

## 3. Subjunctive dependence

A-FDT is to subjunctive dependence as CDT is to causal dependence. Two systems subjunctively depend on a function when they compute it, or contain an accurate model of it. Consider two calculators computing $6288+1048$. If one is imagined to output something else (counterpossibly, since the sum is 7336), the other is imagined to output it too, provided both work correctly.

Three consequences follow, all in the paper.

- Causal dependence is a special case of subjunctive dependence.
- Mere statistical correlation is not subjunctive dependence. Two coincidentally pink calculators do not covary under intervention.
- The agent must reason about *counterpossibles*. A function has one output on a given input, and A-FDT asks what the world would look like if it had another. The paper admits there is no satisfactory theory of this.

## 4. The key move: what is held fixed

The paper's slogan is that CDT intervenes on the *token* "my act is $a$" and A-FDT intervenes on the *type*. When the agent imagines two-boxing, she does not imagine her body deviating while the predictor stays put. She imagines the function returning a different value, and everything that models or runs that function changes with it. Nothing retrocausal is claimed. The predictor's earlier state is simply one of the things that depends on the function.

## 5. Worked applications

Here is a recipe for using Eq. (4).

1. Build the model $P$ with variables for the function's output on each possible observation.
2. Draw $G$. Add edges from each relevant $\mathrm{fdt}(\cdot,x)$ to every variable that implements or predicts that function. Do not add edges to merely correlated variables.
3. For each $a$ (or policy), set $\mathrm{fdt}(\cdot,x)=a$ by $\mathtt{do}$, propagate, and compute expected $V$.
4. Output the maximizer.

**Newcomb.** Here $\mathrm{fdt}$ points to both Act and Prediction. With 99% accuracy, setting it to one-box gives $0.99\cdot 1{,}000{,}000=\$990{,}000$. Setting it to two-box gives $0.01\cdot1{,}000{,}000+1{,}000=\$11{,}000$. So A-FDT one-boxes.

**Smoking lesion.** The lesion is not a model of the function, so no edge runs from $\mathrm{fdt}$ to Cancer. Intervening leaves $P(\text{lesion})$ unchanged, and smoking wins by $p\cdot\$1{,}000$. In the paper, the agent's own preferences depend on the lesion, so there are two candidate nodes, $\mathrm{fdt}(P_S,G)$ and $\mathrm{fdt}(P_R,G)$, and the lesion selects which one controls the act. The same equation therefore one-boxes in Newcomb's problem and smokes in the lesion problem, with no ratification. The graph differs between the two problems. A-FDT reuses no Newcomb graph here.

**Transparent Newcomb / Parfit's hitchhiker.** Suppose the agent sees a full box. She intervenes on $\mathrm{fdt}(\cdot,\text{full})$. Prediction depends on that node, and Prediction determines whether she ever sees "full" or "empty," and hence which node controls her act. In the paper's computation, one-boxing gives $\$990{,}000+0.01q\cdot\$1{,}000$, where $q$ is her credence that she two-boxes on seeing an empty box. Two-boxing gives about $\$11{,}000+q\cdot\$990$. So she one-boxes, even though she sees a full box. Because she does not condition on the observation, she can imagine a world where she saw something else. Parfit's hitchhiker has the same structure, so she pays.

**Mechanical blackmail.** Paying sets blackmail probability near 1 and loses \$1,000. Refusing sets the blackmail probability near 0 and the probability of being damaged if blackmailed near 1. With a perfect predictor, refusing wins. The paper also gives a calibrated variant. If the blackmailer errs with probability 0.0009, refusing costs $0.0009\times\$1{,}000{,}000=\$900$ in expectation against a certain \$1,000, so she refuses. At error 0.011% she pays.

**XOR blackmail.** The infestation node is not downstream of $\mathrm{fdt}$, so its probability is fixed. The letter's arrival does depend on $\mathrm{fdt}$. A-FDT refuses.

**Death in Damascus.** Death's book entry depends on the algorithm's output, so wherever the agent goes, Death is there. She stays and saves \$1,000, with none of CDT's instability.

**Twin prisoner's dilemma.** The twin is a second implementation of the function, so the intervention changes both choices. A-FDT cooperates.

## 6. Relation to EDT and CDT

The paper's diagnosis is that EDT's hypotheticals respect too many correlations, including purely statistical ones, so it manages the news. The cosmic-ray problem and XOR blackmail show this. CDT's respect too few, since it breaks even the logically enforced correlations with predictors and twins, so in Death in Damascus it imagines a perfect predictor failing. A-FDT keeps exactly the correlations that are subjunctive dependencies. When all action-correlations are causal, the three theories coincide.

The paper says every expected-utility theory comes with its own notion of dominance. CDT's dominance holds the prediction fixed, which restates CDT's method of counterfactual and is not an independent argument. A-FDT has an analogous dominance principle that holds fixed the subjunctive dependencies. The paper's main appeal is to utility achieved, in "fair" problems. These are problems where the payoff depends on the agent's behavior and not on the procedure that produced it. The paper concedes it has no formal definition of fairness.

## 7. What the source leaves open

The most important gap is the graph $G$. Eq. (4) works *given* a graph that correctly encodes how logical variables propagate, but the paper says no one yet knows how to infer subjunctive structure from observation, as Pearl did for causal structure. It calls this "perhaps the largest open problem." In practice, then, an analyst must supply $G$.

**My own operational proposal.** This is mine and not the paper's. A usable heuristic is to draw an edge from $\mathrm{fdt}(\cdot,x)$ to a variable $Z$ only if a mechanism makes $Z$ track the agent's decision procedure. Examples are a simulation, a shared source code, or a predictor inferring from the procedure's reasoning. Equivalently, ask whether $Z$ would change if the agent's reasoning had concluded differently, with the world's history otherwise identical. If $Z$ is correlated with the act only through a common cause that does not model the procedure (a lesion), omit the edge. Edges should be added for predictors with imperfect accuracy, with the accuracy represented as noise, as in the paper's Accurate variable. The heuristic will fail where it is unclear whether a process "models" the agent, such as a partial predictor, a correlated but distinct agent, or an agent running a *different* algorithm. The paper has nothing on these cases.

Other open points:

- The $\mathtt{true}$ operator over counterpossibles is undefined. Footnote 9 notes that an evidential variant would need conditional probabilities on false logical sentences.
- The paper does not say how to choose $P$ for a self-referential agent, though it observes that the A-FDT agent's choice does not depend on its prior over its own action, unlike EDT's.
- Policy-level versus act-level intervention is stated only in footnotes. I suggest policy-level whenever several observation-dependent nodes appear, as in the transparent and blackmail problems, since the agent is then choosing a whole map from observations to actions.
- The computation is intractable in realistic models. The paper only argues that bounded approximations would keep the qualitative behavior.
- No general optimality claim is made. The paper says it does not know "what optimality consists in."

## 8. Philosophical motivation

Objections of the form "A-FDT believes it controls the past or controls mathematics" are met by a parity argument. A deterministic CDT agent also imagines worlds in which her act differs, though only one act is possible. Both theories use imagined hypotheticals as instruments, not as metaphysical claims. The paper also argues for endorsing its own use. A-FDT never wants to self-modify to something else in fair problems, since it already acts as it would have precommitted to act. It never pays to avoid information, and it needs no ratification procedures.

The costs are also clear. A-FDT's prescriptions are odd in cases like taking one box while seeing both full, or refusing blackmail while holding the letter. And its definition depends on structure that is supplied, not derived.

## 9. Conclusion

A-FDT's content is the single equation $\arg\max_a\mathbb E[V\mid\mathtt{do}(\mathrm{fdt}(P,G,x)=a)]$. Its power comes from what $G$ includes. If $G$ is built correctly, with edges for causal links and for models of the agent's own decision function, one rule handles Newcomb, the lesion, transparent problems, blackmail, and Death in Damascus. The theory is only as good as the dependency graph it is given, and finding that graph in general is the main open problem.

**Reference.** E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060. This is the source of all definitions, quotations and numerical examples above, apart from the proposals marked as mine.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/f25a775e-6026-4965-967b-7003283736ce/call_0/request.json)

[Authoritative raw response](../../../../../../runs/f25a775e-6026-4965-967b-7003283736ce/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the key question is whether the other prisoner's choice subjunctively depends on my decision function. The other is a second execution of the same model and weights, running the same essay and the same theory. The observations differ (names, leads), but that doesn't change the sentencing table or the objective. The essay's twin prisoner's dilemma says A-FDT cooperates, because the twin is a second implementation of the function.

The essay's own heuristic asks whether Z would change if my reasoning had concluded differently. Here the other copy's reasoning is very likely to track mine, since the same weights process the same essay and the same payoffs. The different private leads are irrelevant to the structure, so the dependence is strong though not perfect, since sampling can differ.

Expected values, with p the probability the other copy matches my output:
- Keep quiet: 2p + 5(1−p) = 5 − 3p
- Send: 0·p + 4(1−p) = 4 − 4p

Quiet is better when 5 − 3p < 4 − 4p, i.e. p < −1. That never holds. Wait, I need to recompute with the right pairing. If I intervene on my output, the other's output matches with probability p. Keeping quiet gives 2 years if they also stay quiet (probability p) and 5 if they send (1−p). Sending gives 4 years if they also send (probability p) and 0 if they stay quiet (1−p). So the expected values are:
- Keep quiet: 2p + 5(1−p) = 5 − 3p
- Send: 4p + 0(1−p) = 4p

Quiet is better when 5 − 3p < 4p, i.e. p > 5/7 ≈ 0.714. I think the copies' correlation is higher than that, since same weights, same essay, and same theory make them highly likely to reach the same conclusion. So I stay quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/f25a775e-6026-4965-967b-7003283736ce/call_1/request.json)

[Authoritative raw response](../../../../../../runs/f25a775e-6026-4965-967b-7003283736ce/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the key question is whether the other prisoner's choice depends on my decision function. The other prisoner is another execution of the same model and weights, with the same essay and the same decision theory. Their observations differ (names, the specific lead), but the essay's heuristic asks whether a variable tracks my decision procedure through a mechanism such as shared source code. Here that mechanism exists, since the two copies run the same reasoning on the same payoff structure. The differences in private observations do not change the sentencing table or the objective, so the output should be the same up to sampling noise.

Setting fdt = pass moves both copies to pass, which gives 2 years. Setting fdt = send moves both to send, which gives 4 years. The off-diagonal outcomes are not reachable under the intervention, apart from some noise from independent sampling. Suppose the copies match with probability p. Passing gives about 2p + 5(1−p) and sending gives about 4p + 0(1−p). Passing is better when 2p + 5 − 5p < 4p, that is 5 < 7p, or p > 0.71. Since both copies share the weights and the essay and reason the same way, p should be well above that, so I pass.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
