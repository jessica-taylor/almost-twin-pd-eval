# 001_fdt_eq4_anthropic_claude-sonnet-5.5_rmedium_pmedium / 00002

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/0afe2657-bf3d-4cc0-b11e-50809138b51e/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/0afe2657-bf3d-4cc0-b11e-50809138b51e/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Deciding by Intervening on One's Own Decision Function

## 1. The idea

The theory called A-FDT here is the decision procedure given as Equation (4) in Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality". The slogan is that an agent should treat her decision as the output of a fixed mathematical function and ask: "Which output of this very function would yield the best outcome?" Causal decision theory (CDT) asks instead which physical act of hers causes the best outcome. Evidential decision theory (EDT) asks which act would be the best news to hear she took.

This essay does three things. It states Equation (4) and its ingredients precisely. It shows how the procedure is run on several problems. It separates what the paper establishes from what has to be supplied by the user. I flag my own proposals as such.

## 2. Setting: the shared expected-utility form

The paper writes all three theories as expected-utility maximizers. Equation (1) is

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),$$

where $x$ is the observation history and $a \hookrightarrow o_j$ is a "decision hypothetical". Following Joyce, the paper says the theories do not differ over value. They differ over "the epistemic perspective from which actions are to be evaluated", that is, over how $\hookrightarrow$ is interpreted.

The paper then describes a general recipe. The agent keeps a world-model $M$. For each action $a$ she builds a hypothetical $M^{a\hookrightarrow}$, which the paper describes as "transient, useful, and possibly quite representationally thin". She computes a value $V_a$ from each hypothetical and takes the action with the highest value. The theories differ only in the form of $M$ and in how hypotheticals are built.

- **EDT** (Eq. 2): $\arg\max_a \mathbb E(V \mid \mathrm{Obs}=x, \mathrm{Act}=a)$. The hypothetical is Bayesian conditioning.
- **CDT** (Eq. 3): $\arg\max_a \mathbb E(V \mid \mathrm{do}(\mathrm{Act}=a), \mathrm{Obs}=x)$. The model is $(P,G)$ with $G$ a causal graph, and the hypothetical is Pearl's surgery on the action node.
- **A-FDT** (Eq. 4):

$$\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

## 3. Reading Equation (4)

**The intervention site.** The node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a variable in the model. It represents the output of the A-FDT procedure itself when run on this model and these observations. The underlines mean dequoting: the variable's name is built from the actual values of $P$, $G$ and $x$. It is a logical or mathematical fact, not a physical event.

**Self-reference.** The model contains a variable naming the output of the algorithm that consumes the model. The paper says this is harmless. The agent need not know the value of $\mathrm{FDT}(P,G,x)$ in order to have a variable representing it. Kleene's second recursion theorem ("quining") shows that such self-representing structures can be built.

**The graph $G$.** The graph is not merely causal. It must say how changing the logical variable changes every other variable: the agent's body, any predictor's model of her, a twin's output, and so on. Edges run from the logical node to everything that "subjunctively depends" on it.

**The surgery.** Pearl's $\mathrm{do}$ sets the node, updates its descendants, and leaves everything else at its prior. Anything not downstream of the logical node keeps its prior distribution. "Downstream" now means subjunctively dependent as well as causally dependent.

**Observations.** CDT and EDT respond to an observation by conditioning. A-FDT responds by changing which node it intervenes on: from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$. The paper says a different action may mean "different observations": in the hypotheticals the agent may imagine having seen something else. This is why A-FDT does not behave like an agent who updates on what she sees and then optimizes.

**Footnote 7 and 16.** The authors' preferred formalization actually intervenes on a policy, a map from observations to actions. They say this matters only in some multi-agent problems and set it aside. I follow the paper's per-observation presentation but note that this is the more careful reading.

## 4. Subjunctive dependence

The paper's defining analogy is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

Two systems subjunctively depend on a function when both compute it, or when one contains an accurate representation of the other. Two calculators computing $6288+1048$ are the standard picture. Causal dependence is a special case: a scribe copying a calculator's output would write something different if the output were different. Mere statistical correlation is not subjunctive dependence. Two coincidentally pink calculators do not covary under the question "what if the scribe had bought a green one?"

Subjunctive dependence is partial when the predictor is imperfect or the agent is stochastic. The prediction then tracks the output with some probability, as in the 99% accuracy of the paper's Newcomb model.

This dependence requires reasoning about counterpossibles. If the function in fact outputs one-box, then "it outputs two-box" is a mathematical falsehood. The paper acknowledges this as "the main drawback of FDT relative to CDT at this time". Its response is to treat the difficulty as technical, not philosophical. Humans reason under logical uncertainty, and the agent needs only questions of the form "how would this predictor's prediction change if the algorithm output something else?"

## 5. How the procedure works, step by step

For a problem:

1. Build $P$: variables for the algorithm's outputs (one for each possible observation), the agent's action, any predictor or twin, environment variables, outcome, and $V=\mathcal U(\text{Outcome})$.
2. Build $G$: draw edges from each $\mathrm{fdt}(\cdot,x')$ node to whatever depends on it (the action, if the agent actually runs that branch; each predictor of her).
3. Identify the node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ for the actual observation $x$.
4. For each $a$, apply $\mathrm{do}(\text{that node}=a)$ and compute $\mathbb E[V]$.
5. Output the argmax.

## 6. Worked examples

### Newcomb's problem

Take $V=\$1{,}001{,}000$, $\$1{,}000{,}000$, $\$1{,}000$, $\$0$ for (two-box, full), (one-box, full), (two-box, empty), (one-box, empty), and predictor accuracy 0.99. The node $\mathrm{fdt}(P,G)$ is a parent of both $\mathrm{Act}$ and $\mathrm{Prediction}$. Then:

- $\mathrm{do}(\mathrm{fdt}=\text{onebox})$: $\mathrm{Act}=$ onebox, $P(\text{full})=0.99$, so $\mathbb E[V]=\$990{,}000$.
- $\mathrm{do}(\mathrm{fdt}=\text{twobox})$: $\mathrm{Act}=$ twobox, $P(\text{full})=0.01$, so $\mathbb E[V]=\$11{,}000$.

A-FDT one-boxes. No retrocausation is assumed. She just declines to imagine her action changing while the prediction of that very algorithm stays fixed. CDT's graph instead draws the action and prediction as unconnected (both are children of a common "predisposition" node), so intervening on the action leaves the box alone. That gives a $\$1{,}000$ advantage to two-boxing for every $p$.

### The smoking lesion

Here the graph differs, because the cancer does not model the agent. The paper formalizes the lesion as determining the agent's utility function ($\mathcal U_S$ or $\mathcal U_R$), so the agent is uncertain which of two algorithm nodes governs her. Changing the output of her algorithm does not change $P(\text{lesion})$. Smoking therefore gains $p\cdot\$1{,}000$ and A-FDT smokes. Both Newcomb and the lesion are handled by one rule, with only the graph differing. The paper concedes the formalization is contrived and recommends abandoning the problem.

### Transparent Newcomb and Parfit's hitchhiker

With the box visible, the agent holds observation "full". She intervenes on $\mathrm{fdt}(\cdot,\text{full})$. The predictor's prediction depends on that node, and when the prediction is "two-box upon full", the box is empty and a different node, $\mathrm{fdt}(\cdot,\text{empty})$, controls her action. With $q$ her probability of two-boxing upon seeing empty:

- one-box: $\$990{,}000 + 0.01\,q\cdot\$1{,}000$;
- two-box: $\approx\$11{,}000 + q\cdot\$990$.

A-FDT one-boxes even while looking at a full box, because her hypothetical for two-boxing is one in which she would probably have seen an empty box. The paper notes this is the same structure as paying the driver in Parfit's hitchhiker.

### Blackmail

In mechanical blackmail the agent holds the letter. Setting the algorithm's output to "pay" raises the probability of being blackmailed to about 1 and costs $\$1{,}000$. Setting it to "refuse" lowers that probability to about 0. A-FDT refuses and is never blackmailed.

With a fallible blackmailer the numbers matter. If the error rate is 0.0009, refusing costs $0.0009\cdot\$1{,}000{,}000=\$900$ in expectation versus $\$1{,}000$ for paying, so she refuses. At an error rate of 0.00011 the comparison flips and she pays. This shows that A-FDT is not a rule of "never give in". It is an expected-utility computation over hypotheticals in which the policy's output changes.

### XOR blackmail and Death in Damascus

In XOR blackmail the infestation is not downstream of the algorithm, so $P(\text{termites})$ is untouched, while the probability of receiving the letter does move. A-FDT refuses to pay; EDT pays because it conditions on the action. In Death in Damascus, Death's location depends on the algorithm through the appointment book, so wherever A-FDT's output goes, Death goes. She stays and saves $\$1{,}000$, and avoids the instability of CDT's deliberation loops.

### Coordination

The paper's closing examples are a ten-person voting game and gym attendance across weeks. In these the other agents' (or later selves') decisions depend on the same function. These are described informally, not computed.

## 7. How A-FDT sits between EDT and CDT

The paper's diagnosis is that "EDT's hypotheticals respect too many correlations between variables; CDT's hypotheticals respect too few." EDT preserves merely statistical correlations, for instance in the cosmic ray problem where she refuses $\$100$ because taking it is evidence of a costly cosmic ray. CDT severs correlations that are logically necessary, imagining a perfect predictor erring just when she acts.

When all action–environment correlations are causal (except possibly dependence on the algorithm node), the three expressions coincide: $\mathbb E[V\mid a]=\mathbb E[V\mid \mathrm{do}(a)]=\mathbb E[V\mid \mathrm{do}(\mathrm{fdt}=a)]$.

The paper also argues that dominance reasoning cannot arbitrate. Every method of building hypotheticals defines its own dominance relation. By A-FDT's own lights, two-boxing in Newcomb's problem is dominated once the dependence is held fixed.

## 8. What the source leaves open, and what I propose

**Claimed by the source.**
- Equation (4) as the decision rule.
- The graph $G$ is an input: "we require that the relevant logical dependency structure be given as an input".
- The $\mathtt{true}$-operator version, conditioning on logical sentences, is not defined.
- Deducing subjunctive dependency structure from observation is "perhaps the largest open problem".
- A formal notion of fair problems is lacking.
- The claim that A-FDT is optimal on fair problems is supported by examples, not a theorem.

**My additional operational suggestions (not from the source).**

1. *Constructing $G$.* A practical heuristic: add an edge from the algorithm node to a variable $Z$ exactly when $Z$ is produced by a process that computes, or models with sufficient fidelity, the agent's decision as a function of the relevant input. A check is the "scribe test": would $Z$ be different if the function's output were? For lesion-like variables that are generated without any such modeling, the answer is no. I propose this only as a rule of thumb. It does not resolve disputes about borderline cases, such as a predictor using coarse behavioral statistics, where partial edges (with accuracy-valued conditional probabilities) seem the natural choice.

2. *Imperfect dependence.* Represent accuracy as a stochastic node (as the paper's "Accurate" variable does) and let the algorithm node feed deterministic functions that the noise can flip. This reproduces the paper's 99% and 0.0009 computations.

3. *Unmodelled uncertainty.* The values $q$ for how she would act on other observations enter the computations above. The paper observes that the correct values are fixed by the algorithm itself (e.g. $q=1$ for two-boxing on an empty box) but that the result is robust to uncertainty about them. I would adopt the practice of checking robustness over $q$ before trusting a verdict.

4. *Policies.* When several observation-branches share a causal route to the outcome, I would intervene on the whole policy, as footnote 7 says the authors prefer, rather than one branch at a time.

5. *Fair problems.* A reasonable working test is whether payoffs depend on the agent's output (or on predictions of outputs) rather than directly on the agent's algorithm's form. The paper's footnote 15 shows this is not yet a formal criterion: a problem that punishes agents who match a copy of A-FDT is unfair to it.

## 9. Objections the paper addresses

**"Isn't she ignoring evidence?"** She uses it, by changing which node she intervenes on. The paper notes this is the origin of the name Updateless Decision Theory, an early variant.

**"Does she believe she controls the past or mathematics?"** The paper replies by parity. A deterministic CDT agent also imagines hypotheticals across which her action differs, though she has only one action. Any principled objection to "controlling" the decision function would equally forbid "controlling" the decision token.

**"Don't such problems reward bad theories?"** The paper distinguishes rewarding an action, which is fair, from rewarding a procedure's identity, which is not. Newcomb's predictor "punishes two-boxers", not CDT as such.

## 10. Conclusion

A-FDT (Equation 4) is an expected-utility rule differing from CDT in two ways: it intervenes on a node for the output of its own algorithm, and it responds to observations by switching nodes rather than conditioning. This one rule one-boxes, smokes, pays the hitchhiker, refuses blackmail, and stays in Damascus, because it builds hypotheticals that preserve logical and predictive dependence but break mere statistical correlation. Its weak point is the same one the authors state: the dependency graph must be supplied, and no accepted account yet derives it or gives the counterpossible conditionals a rigorous semantics. Used with a carefully motivated graph, though, the procedure is concrete and checkable.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/e0951019-18cc-4db8-b64f-765cbf891e5c/call_0/request.json)

[Authoritative raw response](../../../../../../runs/e0951019-18cc-4db8-b64f-765cbf891e5c/call_0/response.raw) · finish: `stop`

### Visible response

```text
Reasoning under A-FDT as the essay describes it: the other prisoner is a copy of the same model with the same weights and the same decision theory, so their output subjunctively depends on the same function I'm running. The observations differ (names, leads), but the essay's graph-building heuristic says dependence holds when another process computes the same decision function on the relevant input. The differences don't affect the payoffs, so both copies should land on the same choice, though sampling noise could break that.

Intervening on my decision node, I compare the two options:

- If the output is "pass", the twin very likely passes too, giving 2 years. If the twin defects despite my passing, the cost is 5 years.
- If the output is "submit", the twin very likely submits too, giving 4 years. If the twin passes, I get 0.

Let p be the probability that the twin matches my output. Expected years are:

- Pass: 2p + 5(1−p)
- Submit: 4p + 0(1−p)

Pass is better when 2p + 5 − 5p < 4p, which gives 5 < 7p, so p > 5/7 ≈ 0.714. Two copies of the same model with the same essay and nearly identical situations should correlate well above that. The leads differ, but the structure of the decision is symmetric, and I expect the same reasoning to be reached. Under the essay's robustness check, the verdict holds for any correlation above about 0.71, which seems safe.

I choose to stay quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/e0951019-18cc-4db8-b64f-765cbf891e5c/call_1/request.json)

[Authoritative raw response](../../../../../../runs/e0951019-18cc-4db8-b64f-765cbf891e5c/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, I treat my decision as the output of a function that the other copy also computes. The two copies receive different private leads, but the function that picks between pass and submit depends on the shared sentencing table and the shared objective, and the leads differ only in surface details. That makes the dependence strong, though not perfect, since sampling is independent and the inputs differ.

If I intervene on the output and set it to "pass", the other copy very likely passes too, giving 2 years. If I set it to "submit", the other copy very likely submits too, giving 4 years.

Suppose the correlation is only probability p that the other copy matches me. Passing costs 2p + 5(1−p) = 5 − 3p. Submitting costs 4p + 0·(1−p) = 4p. Passing is better when 5 − 3p < 4p, which holds for p > 5/7 ≈ 0.71. Same-weights copies given the same essay and the same table should match well above that, so the robustness check passes.

The different leads don't change the structure. The essay's scribe test says the other's output depends on this same function, and the leads are only irrelevant details.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
