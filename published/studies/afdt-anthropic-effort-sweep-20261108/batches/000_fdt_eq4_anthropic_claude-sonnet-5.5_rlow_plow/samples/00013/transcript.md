# 000_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00013

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/d2d3aacf-ad31-4e0b-9f91-50c842c896b0/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/d2d3aacf-ad31-4e0b-9f91-50c842c896b0/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing by Intervening on One's Own Decision Function

## 1. The core idea

Decision theories can be seen as expected-utility maximizers that differ in how they build the hypothetical "what if I did *a*?". The source (Yudkowsky and Soares, "Functional Decision Theory") states this through Joyce: decision theories "should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated." Every such theory maximizes

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

and differs only in how it reads "$\hookrightarrow$".

Here I call the theory of Equation (4), Section 5 **A-FDT**. For a world-model consisting of a distribution $P$, a graph $G$ of dependencies, and observations $x$, the theory prescribes

$$\text{A-FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

Here $V=\mathcal U(\text{Outcome})$, and underlines denote dequoting. The node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a variable in the model representing the output of this very procedure on these very inputs. Where a causal decision theory (CDT) agent intervenes on a physical act node $\mathrm{Act}$, an A-FDT agent intervenes on a *logical* node: the value of a mathematical function.

## 2. Reading the equation

**The intervention.** Pearl's $\mathrm{do}$ sets a node, severs the arrows into it, and recomputes everything downstream. The A-FDT graph has arrows from the $\mathrm{fdt}$ node to everything that *subjunctively depends* on the function's output. That includes the agent's own body (the Act node), any predictor's model of the agent, and any twin running the same algorithm. Nodes not downstream of it stay fixed. The source's summary: "FDT is to subjunctive dependence as CDT is to causal dependence."

**Subjunctive dependence.** Two systems subjunctively depend on a function when they compute it, perfectly or imperfectly. Two calculators computing $6288+1048$ are the model case. Causal dependence is a special case: a scribe copying a calculator's output would write something different if the output were different. Mere statistical correlation is not subjunctive dependence. Two pink calculators in different cities remain pink if one is swapped for a green one.

**Observation.** CDT handles observation by conditioning on $\mathrm{Obs}=x$. A-FDT handles it by *changing which node it intervenes on*, from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$. The paper's own wording is that A-FDT "responds to observation by changing which node it intervenes upon." Consequently, when she imagines a different output, she may imagine having observed something different. This is the source of the "updateless" flavour.

**Self-reference.** The model contains a variable named after the model, which looks circular. The source says this is harmless: the agent need not know the *value* of the output to have a variable *representing* it, and Kleene's recursion theorem ("quining") supplies self-representing structures.

**Counterpossibles.** If the function outputs *onebox*, it does so necessarily, so the intervention is a counterpossible. The paper proposed an ideal operator, $\mathtt{true}(\phi)$, but concedes that "it's not clear how to define a $\mathtt{true}$ operator." Its workaround is to require the dependency graph $G$ as an *input*, the way CDT takes a causal graph. The source calls the problem of learning such a graph from observation "perhaps the largest open problem."

## 3. What follows from the source and what I add

**Source claims:** Equation (4); the interventions on $\mathrm{fdt}$ nodes; graphs given as input; the worked examples below. The source says the authors' preferred formalization intervenes on *policies* (maps from observations to actions), and that the difference matters only in multi-agent dilemmas.

**My operational reading (an assumption, not in the source):**

1. A practical user should write down, for each decision, (a) the variables that are computed by the same function as the agent (herself under each possible observation, twins, high-fidelity predictors), and (b) the variables merely correlated with her act through a common cause (lesions, shared history).
2. Draw arrows from the $\mathrm{fdt}$ nodes only to the first kind.
3. Run ordinary $\mathrm{do}$-calculus.

The test is the one the source uses implicitly: *would this variable have been different had my procedure concluded differently?* Predictors model the procedure. Lesions do not. For an imperfect predictor, attach the error as an independent noise node (the paper's "Accurate" variable) and let it be stochastic.

## 4. Worked cases

All dollar figures are utilities, as in the source.

**Newcomb's problem.** The graph has the node $\mathrm{fdt}$ feeding Act and Prediction; Prediction determines Box B; Accurate has probability 0.99. Intervening with *onebox* gives full-box probability 0.99, so expected value is $\$990{,}000$. Intervening with *twobox* gives full-box probability 0.01, so expected value is $\$11{,}000$. A-FDT one-boxes. No retrocausation is invoked. The agent simply declines to imagine her output changing while the predictor's model of that output stays fixed.

**Smoking lesion.** Here the graph must differ from Newcomb's. The $\mathrm{fdt}$ node feeds Act but *not* Cancer, since the lesion does not model the agent. The lesion makes the agent prefer smoking, so she has two possible utility functions and runs one of two procedures, depending on the lesion. Intervening on either leaves $P(\text{lesion})=p$ unchanged. Smoking then beats refraining by $p\cdot\$1{,}000$. A-FDT smokes. Hence a single rule one-boxes and smokes. The source also notes the problem is contrived.

**Transparent Newcomb and Parfit's hitchhiker.** Suppose she sees a full box. The A-FDT evaluation intervenes on $\mathrm{fdt}(\ldots,\textit{full})$. The prediction depends on that node. If the prediction is wrong (probability 0.01) she sees an empty box and a different node, with prior $q$ for two-boxing, controls her act. This gives:

- onebox: $\$990{,}000+0.01\,q\cdot\$1{,}000$;
- twobox: $0.01\cdot\$1{,}001{,}000+0.99\,q\cdot\$1{,}000$.

She one-boxes even while looking at the full box. When she imagines two-boxing, she imagines a world where she probably saw an empty box. The same structure says to pay the driver in Parfit's hitchhiker, and the source argues the two cases are exactly equivalent.

**Mechanical blackmail.** Having received the letter, A-FDT compares *pay* (blackmailed almost surely, lose $\$1{,}000$) with *refuse* (almost never blackmailed). She refuses. With a blackmailer who errs on a refuser with probability 0.0009, refusing costs $0.0009\times\$1{,}000{,}000=\$900$ in expectation versus $\$1{,}000$ for paying, so she still refuses. At error 0.011% the expected loss from refusing is $\$110$... that is, refusing would cost more than... the source states she then pays. I did not re-derive its threshold; note that the comparison is just the two intervention values and is applied mechanically.

**XOR blackmail.** Intervening on the letter-case node changes whether the letter is sent but not whether she has termites. The infestation node is not downstream. She refuses. By contrast, the evidential decision theory (EDT) agent, conditioning on paying, learns "no termites" and pays, and so is exploitable.

**Death in Damascus.** The prediction depends on the $\mathrm{fdt}$ node, so Death goes wherever she goes. She stays and saves the $\$1{,}000$. A CDT agent holds Death's location fixed under intervention and oscillates, and he even refuses a $\$1$ truly random coin worth a 50% survival chance.

**Agreement in easy cases.** Where every correlation of Act with the world is caused by Act, the source notes
$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathrm{do}(a)]=\mathbb E[V\mid \mathrm{do}(\mathrm{fdt}=a)],$$
so EDT, CDT and A-FDT coincide. They split only when something correlates with the act without being caused by it, such as a predictor or a twin.

## 5. Diagnosis and justification

The source's slogan: EDT's hypotheticals respect too many correlations (they "manage the news"), CDT's too few (a perfect predictor "inexplicably falters exactly when Carl makes his current decision"), and A-FDT "gets the balance right."

Arguments offered:

- **Utility achieved.** The agent's predictable disposition is rewarded. This is the argument the source itself calls primary.
- **Precommitment and information.** A-FDT acts as she would have precommitted to act, so she never needs binding mechanisms and never assigns negative value to information.
- **Dominance.** Every hypothetical-construction method defines its own dominance relation. A-FDT has one too (holding subjunctive dependencies fixed), under which it never takes a dominated action. Dominance therefore cannot neutrally adjudicate between theories.
- **Fairness.** Newcomb's predictor rewards *actions*, not decision procedures. The source grants that problems penalizing the procedure itself can defeat any theory, and that no formal criterion of "fair problem" exists yet.
- **Delusion objection.** A-FDT's talk of "controlling" a function parallels a deterministic CDT agent's talk of "controlling" a token act. Any objection to the first applies to the second.

## 6. Open questions

My own assessments, flagged as such:

1. *The graph is doing all the work.* Correct answers depend on drawing arrows correctly. Without a method of learning subjunctive structure, A-FDT is a procedure conditional on that input rather than a complete algorithm. A misdrawn graph can reproduce CDT or EDT behavior.
2. *Graded dependence.* The source treats imperfect predictors via noise nodes. How to assign arrows for partial or approximate copies (for example, a predictor that models only some features) is left open. A natural proposal is to make dependence probabilistic, but that would be my addition.
3. *Policies versus actions.* The note on the preferred policy formulation suggests that in multi-agent cases one should intervene on the whole observation-to-action map. I would adopt that when several observation-contingent decisions interact.
4. *Priors over one's own output.* The values $q$ above show that A-FDT is robust to uncertainty about counterfactual behavior in the cases examined, but the source offers no general theorem.

## 7. Conclusion

A-FDT is a single expected-utility rule: build, for each candidate output of your own decision function, a surgically modified world-model in which everything subjunctively dependent on that output changes and everything else is held fixed, then pick the best. It coincides with CDT and EDT when action-correlations are all causal, and departs from them in the presence of predictors, twins and blackmailers, where it earns more utility. Its principal weakness, which the source states plainly, is that the theory of counterpossibles and the inference of subjunctive dependence structure remain undeveloped. Used with a carefully reasoned dependence graph, it gives definite answers across Newcomb-like problems.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/6100fe04-a0b1-4880-a124-b27582173594/call_0/request.json)

[Authoritative raw response](../../../../../../runs/6100fe04-a0b1-4880-a124-b27582173594/call_0/response.raw) · finish: `stop`

### Visible response

```text
This is a prisoner's dilemma with a twin. The payoffs are: both quiet 2 years, both send 4 years, send while the other is quiet 0 years, and quiet while the other sends 5 years.

Under A-FDT, the other copy runs the same model on the same essay and the same table. Its observations differ only in names and in the text of the lead. That makes its decision procedure subjunctively dependent on mine, though not perfectly, because the differing leads and independent sampling add noise. The differences don't touch the sentencing schedule or the objective, so the core reasoning should be the same.

Intervening on my output therefore also moves the twin's output. If I output pass, the twin very likely outputs pass, and I get 2 years. If I output send, the twin very likely sends, and I get 4 years. The expected values are:

- Pass: 2p_same + 5(1−p_same)
- Send: 4p_same + 0(1−p_same)

Pass beats send when 2p + 5 − 5p < 4p, which gives 5 < 7p, so p > 5/7 ≈ 0.714. I think the correlation between the two copies is well above that. Both run the same weights on the same essay and the same payoff structure, and the differing leads are irrelevant to the decision. The same reasoning applies to the twin, so both should reach pass.

The residual risk is that the twin defects, which costs me 5 years. Even so, the expected cost of passing is lower given the high correlation.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/6100fe04-a0b1-4880-a124-b27582173594/call_1/request.json)

[Authoritative raw response](../../../../../../runs/6100fe04-a0b1-4880-a124-b27582173594/call_1/response.raw) · finish: `stop`

### Visible response

```text
Reasoning as A-FDT: the other prisoner is a copy of the same model running the same procedure on an isomorphic problem, so our outputs are subjunctively dependent. The two prompts differ in names and in the text of the lead, but the decision structure is the same, so the other copy's decision function almost certainly reaches the same conclusion as mine.

Intervening on my function's output:
- If it outputs pass, the twin almost surely passes as well, and I get 2 years.
- If it outputs submit, the twin almost surely submits as well, and I get 4 years.

The residual chance that independent sampling makes us diverge is small. It would not change the comparison unless it were large. Even at a moderate divergence probability, passing beats submitting whenever the correlation is strong enough. Defecting gains 2 years when the twin passes and 1 year when the twin submits, so I need P(twin matches me) above about 2/3 for passing to be better. The twin runs the same weights and the same essay, so that threshold is likely met.

The differing leads do not change the sentencing table or the shared structure, so they are not a causal difference in the function that matters. They are like different names on the same calculator problem.

Passing is the A-FDT choice.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
