# 003_fdt_eq4_anthropic_claude-opus-5.5_rlow_plow / 00028

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/9adef2df-7ec7-42c9-8227-bccd61b69ec2/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/9adef2df-7ec7-42c9-8227-bccd61b69ec2/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Action Functional Decision Theory (A-FDT): Deciding as the Output of a Function

## 1. The question A-FDT asks

Every expected-utility theory answers the same practical question, *what should I do?*, by weighing imagined alternatives. The theories differ in how they imagine them. Yudkowsky and Soares's paper *Functional Decision Theory* contrasts three ways of doing this:

- **Evidential decision theory (EDT)** asks: "Which physical act of mine would be the best news to hear I took?"
- **Causal decision theory (CDT)** asks: "Which physical act of mine causes the best outcome?"
- **Functional decision theory** asks: "Which output of this decision procedure causes the best outcome?"

The source formalizes the third question in Equation (4) of its Section 5. I call that equation **A-FDT** (action functional decision theory). The "action" label separates it from a variant the authors mention only in footnotes, in which the agent selects a *policy*, meaning a map from observations to actions, rather than an action. I call that variant **policy-FDT**. The paper itself uses "FDT" for both. In this essay, "A-FDT" always means Equation (4).

The core idea is that a deliberating agent is a physical system computing a fixed mathematical function. The same function may also be computed, or modelled, elsewhere: by a twin, by a predictor's simulation, or by one's own future self. If the agent's deliberation imagines the function itself returning a different output, then every system that implements or accurately models that function must "move together" in the imagined scenario. The authors call this relation *subjunctive dependence*: "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." On their account, causal dependence is a special case of subjunctive dependence, and mere statistical correlation does not imply it. Their slogan is that the theory "is to subjunctive dependence as causal decision theory is to causal dependence."

## 2. The formal definition

### 2.1 The common template

All three theories maximize an expectation of the form

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

where $x$ is the observation history and $\hookrightarrow$ is a "decision hypothetical" connective. Following Joyce, the authors treat the interpretation of $\hookrightarrow$ as the free parameter that separates the theories. In their words, the theories disagree "about the epistemic perspective from which actions are to be evaluated." Write $V=\mathcal U(\textsc{Outcome})$. The other two theories, given for comparison, are:

$$\mathrm{EDT}(P,x)=\arg\max_a \mathbb E(V\mid \textsc{Obs}=x,\textsc{Act}=a),$$
$$\mathrm{CDT}(P,G,x)=\arg\max_a \mathbb E(V\mid \mathtt{do}(\textsc{Act}=a),\textsc{Obs}=x).$$

Here $G$ is a causal graph, and $\mathtt{do}$ is Pearl's intervention: it sets a node, recomputes everything downstream of that node, and leaves everything else at its prior distribution.

### 2.2 Equation (4)

A-FDT requires the world-model to contain variables that stand for the outputs of mathematical functions. In particular, it contains a node $\textsc{fdt}(\underline P,\underline G,\underline x)$ representing what the decision procedure returns on the agent's own inputs. The underlines mark dequoting: the node's *name* is built from the model itself, and the authors cite Kleene's recursion theorem to show that this self-reference is harmless. The graph $G$ now encodes subjunctive dependence, not only causal dependence. Equation (4) reads:

$$\boxed{\;\text{A-FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\!\left(V \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right)\;}$$

The authors identify two differences from CDT:

1. **The intervention point.** CDT intervenes on the physical token $\textsc{Act}$. A-FDT intervenes on the logical type, the function's output. Everything downstream of that node in $G$ changes together. That includes the agent's body, any predictor's forecast, and any twin's move.
2. **How observations enter.** CDT conditions on $\textsc{Obs}=x$. A-FDT does not condition at all. Instead, "FDT responds to observation by changing which node it intervenes upon." The observation $x$ appears only in the *name* of the intervened node.

The second point is the formal source of A-FDT's characteristic "updateless" behaviour. Because nothing conditions on $x$, the hypotheticals may contain worlds in which the agent never sees $x$. Those worlds still count, and in them the agent's behaviour is governed by other nodes $\textsc{fdt}(\underline P,\underline G,\underline y)$ for $y\neq x$.

### 2.3 What the source does not specify

The source admits that the ideal operator would be $\mathtt{true}(\phi)$, which updates on a logical sentence counterpossibly. "It's not clear how to define a $\mathtt{true}$ operator," the authors write, so they take the logical dependency structure $G$ as an input, just as CDT takes causal structure as an input. They are frank that this is the theory's largest gap: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

A-FDT is therefore a *conditional* procedure. Given $(P,G)$, it is fully determinate. Choosing $G$ is a modelling step that the theory does not itself supply.

## 3. A working recipe

The following recipe is my operationalization. Each step is either explicit in the paper's worked examples or, where noted, is my own assumption.

1. **List the function nodes.** For every observation history $y$ the agent might have in the problem, include a node $F_y=\textsc{fdt}(\underline P,\underline G,\underline y)$. (Source practice: the transparent Newcomb example has nodes for "full" and "empty".)
2. **Wire the dependencies.** Draw an arrow from $F_y$ into anything that implements or accurately models the procedure on input $y$: the physical action in situation $y$, predictors' forecasts of behaviour on $y$, and twins facing $y$. Draw an arrow from the world state into a "switch" that determines which $F_y$ actually drives $\textsc{Act}$, namely whichever observation actually arises. Lesion-like common causes get *no* arrow from any $F_y$.
3. **Assign priors to the non-intervened function nodes.** For $y\neq x$, give $F_y$ some distribution. The paper calls this $q$ and notes that the correct value is whatever A-FDT would in fact output there. In its examples, the choice "doesn't matter" because the ranking is robust.
4. **Intervene and compute.** For each action $a$, set $F_x=a$ by $\mathtt{do}$, propagate through $G$, and compute $\mathbb E(V)$ using the prior over all non-descendants. Do *not* condition on $x$.
5. **Output the argmax.**

## 4. Worked examples

### 4.1 Psychological twin prisoner's dilemma

Both prisoners compute the same function, so one node $F$ feeds both moves. Under $\mathtt{do}(F=\text{cooperate})$ the payoff is \$1,000,000. Under $\mathtt{do}(F=\text{defect})$ it is \$1,000. A-FDT cooperates.

CDT holds the twin's move fixed. Defection then dominates, and CDT defects.

### 4.2 Newcomb's problem (99% predictor)

In the graph, $F\to\textsc{Act}$ and $F\to\textsc{Prediction}$, with $\textsc{Accurate}\sim(0.99,0.01)$.

- Under $\mathtt{do}(F=\text{onebox})$: $\mathbb E V=0.99\cdot 10^6=\$990{,}000$.
- Under $\mathtt{do}(F=\text{twobox})$: $\mathbb E V=0.01\cdot 1{,}001{,}000+0.99\cdot 1{,}000=\$11{,}000$.

A-FDT one-boxes. (These figures match the paper's A-FDT computation. The paper's EDT paragraph reports "\$999,000" for the same quantity, which appears to be a typo for \$990,000.)

The paper stresses that no retrocausation is involved. The agent "does not think that a physical signal passes between her action and the predictor's prediction." She only refuses to imagine her action changing while a good model of her procedure stays fixed. In the authors' words, imagining that would be like asking a working calculator to output 3159 "holding constant the fact that $6288+1048=7336$."

### 4.3 Smoking lesion

The lesion affects cancer and also affects *which utility function, and hence which decision procedure*, drives the act. No $F$ node points to $\textsc{Cancer}$. Intervening on $F_S$ therefore leaves $P(\text{lesion})=p$ unchanged. Smoking beats refraining by $p\cdot\$1{,}000$, so A-FDT smokes.

This is the paper's answer to Gibbard and Harper's claim that one cannot consistently both one-box and smoke. A predictor *models the function*; a lesion does not.

### 4.4 Transparent Newcomb

The agent sees box B full, so $x=\text{full}$. There are two nodes, $F_{\text{full}}$ and $F_{\text{empty}}$, and the prediction (a descendant of $F_{\text{full}}$) decides which one controls the act. Let $q=P(F_{\text{empty}}=\text{twobox})$. Then:

$$\mathbb E[V\mid\mathtt{do}(F_{\text{full}}=\text{one})]=990{,}000+10q,$$
$$\mathbb E[V\mid\mathtt{do}(F_{\text{full}}=\text{two})]=0.01(1{,}001{,}000)+0.99(1{,}000q)=10{,}010+990q.$$

(The paper prints the second constant as "\$110,00", which is evidently a typo.) For every $q\in[0,1]$ the first expression is larger, so A-FDT one-boxes even while looking at a full box.

In the hypothetical where it two-boxes, it mostly sees an *empty* box. That is exactly what "not conditioning on $x$" buys. The authors note that this case is structurally identical to Parfit's hitchhiker: paying the driver once safely in the city corresponds to leaving the \$1,000 here.

### 4.5 Blackmail and Death

**XOR blackmail.** Intervening on $F_{\text{letter}}$ changes whether the letter is sent but not whether termites exist. A-FDT refuses to pay, as CDT does but EDT does not. The difference from CDT lies in the counterfactual story each agent tells. CDT says, "had I paid, I'd still have the letter and the termites." A-FDT says, "had I paid, the letter wouldn't have come."

**Mechanical blackmail.** Suppose a blackmailer runs the damaging program iff she predicts the agent pays, with false-positive rate $\varepsilon$.

- Paying gives an expected loss of about \$1,000, since the agent is almost surely blackmailed.
- Refusing gives an expected loss of $\varepsilon\cdot\$10^6$.

The threshold is therefore $\varepsilon^*=0.001$. With the paper's $\varepsilon=0.0009$, the loss from refusing is \$900, so A-FDT refuses even while holding the letter. The paper then says that with "0.011%" the agent pays. By the arithmetic above, $0.011\%$ gives only \$110, which still favours refusing; "1.1%" or "0.11%" must be meant. The general rule, $\varepsilon^*=\text{cost of paying}/\text{damage}$, is what a reader should take away.

**Death in Damascus.** Death's book is a descendant of $F$, so Death is wherever the agent goes under either intervention. The only difference left between the options is the \$1,000 cost of fleeing, so A-FDT stays.

CDT, by contrast, oscillates. With a ratification procedure it ends up near 50/50, and the paper notes it will even decline a genuinely random coin offered for \$1. A-FDT would pay the dollar, because a truly random coin is *not* a descendant of $F$, so it buys a real 50% chance of surviving.

## 5. Dominance, self-endorsement, and fairness

The two-boxer's dominance argument holds the prediction fixed while varying the act. The authors reply that every way of building hypotheticals induces its own notion of dominance. They define A-FDT-dominance as follows: $a$ dominates $b$ if switching the *algorithm's output* from $b$ to $a$, holding subjunctive dependencies fixed, is sometimes better and never worse. A-FDT never takes an action dominated in this sense. Dominance therefore cannot adjudicate between the theories, and the authors fall back on expected utility actually achieved.

Two further claims support the theory:

- **No precommitment needed.** A-FDT agents act as they would have precommitted to act. CDT agents, by contrast, would pay to self-modify away from CDT.
- **Reflective stability in fair problems.** The source states this only tentatively: "so far as we know."

"Fair" here means that outcomes depend only on the agent's *behaviour* in the problem, not on which procedure produced it. Newcomb's predictor is fair in this sense, since she "punishes *two-boxers*." A mind reader who rewards agents for using EDT is not. The authors admit that fairness lacks a formal definition. Their footnote example of a game that punishes whoever matches a copy of the agent shows why one is hard to give.

## 6. Open points and how I would resolve them

**(a) Building $G$.** The source does not say how to tell whether some system "computes the same function." The extremes are clear. A twin running the same code is subjunctively linked; a coincidentally pink calculator is not. Intermediate cases, such as a crude predictor or a merely similar person, are not settled.

*My proposal:* treat a system $S$ as a descendant of $F_x$ to the extent that $S$'s behaviour would track $F_x$'s output across a range of hypothetical algorithm outputs, not merely across the actual one. A predictor whose accuracy comes from modelling the agent's reasoning qualifies. A predictor that is accurate only because it reads off a demographic correlate does not. This is roughly a "modelling" test. It goes beyond the source, which brackets "the particular method an agent uses."

**(b) Priors on off-path nodes.** Equation (4) optimizes only $F_x$. The other nodes $F_y$ are held at the prior $q$. The paper's examples are robust to $q$, but in general the answer could depend on $q$, and the paper says only that the "correct" $q$ is A-FDT's own output there.

*My proposal:* require self-consistency. Choose the profile $(F_y)_y$ so that each $F_y$ is the A-FDT argmax given the others. This makes the answer a fixed point, which may not be unique.

**(c) A-FDT versus policy-FDT.** Policy-FDT would solve

$$\pi^*=\arg\max_{\pi:\mathcal X\to\mathcal A}\mathbb E\big(V\mid\mathtt{do}(\textsc{fdt}=\pi)\big),\qquad \text{act } \pi^*(x).$$

This is a *joint* optimization across all observations. A-FDT's coordinate-wise choices, even at a self-consistent fixed point, can settle into a suboptimal local equilibrium when several information sets must coordinate. Policy-FDT avoids this. The source says the authors prefer the policy version and that the difference "makes a difference in certain multi-agent dilemmas." In every single-agent example above the two versions agree.

My reading is that the paper's "act as you would have precommitted" claims are guaranteed in general only for policy-FDT. For A-FDT, they hold whenever the self-consistent profile is also the globally best one.

**(d) Conditioning on $x$.** In the transparent-Newcomb passage, the paper writes the objective with "$\textsc{Obs}=\text{full}$" inside the expectation, but Equation (4) contains no conditioning, and the paper's computed numbers follow the unconditioned version. I follow Equation (4).

The paper also warns explicitly that adding Bayesian conditioning on top of moving the intervention point produces a harmful "double update." This is the problem it attributes to the earlier Timeless Decision Theory.

**(e) Counterpossibles.** The function's actual output is fixed by logic, so the alternative interventions are counterpossible. The source's reply is a parity argument. A deterministic CDT agent also imagines a physical act it could not have performed. Any objection to "controlling" the decision type therefore applies equally to controlling the decision token.

## 7. When A-FDT agrees with its rivals

If every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from $\textsc{Act}$'s own dependence on $F$, the three theories coincide:

$$\mathbb E[V\mid a]=\mathbb E[V\mid\mathtt{do}(a)]=\mathbb E[V\mid\mathtt{do}(F=a)].$$

So A-FDT is conservative in ordinary choices. It departs from CDT and EDT only when something else in the world tracks the agent's decision procedure. Predictors, copies, other agents reasoning symmetrically (the paper's voting coalition), and one's own future selves facing the same choice (the paper's gym example) all fall into this category. The paper expects such cases to become common among artificial agents that can be copied and simulated.

## 8. Conclusion

A-FDT is Equation (4): maximize expected utility under a Pearl-style intervention on the logical node representing one's own decision procedure's output on the current input, without conditioning on that input. Two features follow from this definition.

The first is the choice of intervention point. Intervening on the function rather than the act makes predictors, twins, and models of oneself covary with the choice, while lesion-like correlations stay severed. This yields one-boxing, smoking, and cooperation with a twin.

The second is how observations are handled. Treating them as a choice of node rather than as evidence produces the updateless behaviour seen in transparent Newcomb, Parfit's hitchhiker, and blackmail problems.

The procedure is exact once the dependency graph $G$ is given. Constructing $G$, assigning off-path priors, and choosing between action and policy optimization remain open. I have suggested a modelling test for subjunctive dependence, a self-consistency rule for the off-path priors, and the observation that policy-FDT is the safer choice when coordination across observations matters. Taken together, these let a reader apply A-FDT to unfamiliar cases while keeping clear which parts come from the source and which are interpretation.

*Primary source:* E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060. Also referenced: Gibbard and Harper (1978); Joyce (1999); Pearl (2000).
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm planning a roughly 2400–3000 word essay on A-FDT, the action-selecting version from Equation (4), and I'll keep that name throughout. The policy-selecting variant from footnotes 7 and 16 needs its own label so the two don't blur, so I'll call it P-FDT. The source uses "FDT" for both, and I want to make clear that the Equation (4) version is the A-FDT one.

I'm now checking the worked examples against the stated values: the Newcomb payoffs, the transparent variant, and the blackmail threshold. The paper's numbers have a few slips I need to flag, including a probability that looks off by a factor of ten.

I'm now going through the open questions: how to construct the graph G, and whether the other observation nodes, the ones not equal to x, stay at their prior distribution rather than being optimized jointly. That could matter for coordination across information sets and could lead to suboptimal equilibria, so I'm weighing a fixed-point treatment of those nodes as a practical fix.

I'm settling on the operational reading: the prior stays unconditioned, and the observation only determines which node gets intervened on. I'll work through the recipe steps and bring in the twin prisoner's dilemma and Death in Damascus cases so the essay covers a range of examples.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/56fa625c-ee4b-439e-929c-fc320a9fcb8d/call_0/request.json)

[Authoritative raw response](../../../../../../runs/56fa625c-ee4b-439e-929c-fc320a9fcb8d/call_0/response.raw) · finish: `stop`

### Visible response

````text
**Decision under A-FDT**

1. **Is the other prisoner linked to my decision?** The other prisoner is a second run of the same model. It has the same weights, the same assigned theory and the same essay. Our inputs differ only in names and in the wording of each lead, and the sentencing tables are exactly symmetric. A-FDT technically intervenes on my node, F_x, and the other prisoner's choice is driven by a different node, F_y. Still, the essay's modelling test applies: the other copy's output would follow whatever my reasoning returns across hypothetical outputs. That is because its reasoning does not depend on which name or locker number appears in the lead. So for this decision, F_x and F_y are effectively the same function, and the other prisoner's choice is a descendant of my choice.

2. **Comparing the two outcomes:**
   * If my procedure outputs pass, both of us pass, and I serve 2 years.
   * If my procedure outputs submit, both of us submit, and I serve 4 years.

3. **Self-consistency check:** Both copies passing is a consistent fixed point. It is also the globally best profile, so the A-FDT choice agrees with the policy-FDT choice here.

Passing gives 2 years instead of 4, so A-FDT keeps quiet.

**Command:**

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm treating the twin in this Prisoner's Dilemma as running the same model on the same essay, just with different observations. Under the A-FDT view, the other copy is computing the same function on a different input, so the question is whether that still counts as the same decision node. The structural symmetry and the essay's self-consistency point toward a single shared profile, since the observation differences look irrelevant to what the policy outputs.

Since the other copy's behavior tracks my output across hypothetical outputs, the decision procedure is effectively shared, so cooperating gives the better outcome: passing yields 2 versus 4.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/56fa625c-ee4b-439e-929c-fc320a9fcb8d/call_1/request.json)

[Authoritative raw response](../../../../../../runs/56fa625c-ee4b-439e-929c-fc320a9fcb8d/call_1/response.raw) · finish: `stop`

### Visible response

```text
**Command:** `pass`

**Reasoning under A-strict FDT as the essay interprets it:**

1. **Is the other prisoner linked to my decision?** The two observations differ only in labels (names, the wording of the leads). These differences have no effect on the payoff structure or on either prisoner's objective. The deciding computation is "an A-FDT agent faces a symmetric prisoner's dilemma against a copy of itself." That computation does not depend on the names.
   - The essay's modelling test (§6a) asks whether the other system's behaviour would track my function's output across hypothetical outputs. It would: the other prisoner's node is the same function applied to an input that differs only in irrelevant details.
   - So I treat the other prisoner's move as a descendant of the same logical decision. This is the twin case in §4.1, not an independent player held fixed.

2. **Self-consistency (§6b).** By symmetry, the self-consistent profile has both nodes give the same output. Two fixed points are possible: both pass, or both submit. My judgment is that the label differences should not break the subjunctive link. Under that reading:
   - Intervening to set the output to "pass" gives 2 years.
   - Intervening to set the output to "submit" gives 4 years.

3. **Result.** Passing gives U = −2, which beats U = −4. Passing is also the globally best symmetric profile, which is the case where the essay says A-FDT matches what one would have precommitted to (§6c).

Final action: **pass**
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm weighing whether the other twin's decision counts as a descendant of my F_x, since our observations differ. The two functions take different inputs, so the twins' outputs should match by self-consistency, but under A-FDT only F_x gets intervened on, which pushes toward defecting. I'm now checking the essay's modelling test: whether the other's behavior tracks mine.

I'm asking whether the other twin's choice counts as subjunctively dependent on the same computation, since the functions differ only in irrelevant inputs like names. I lean toward yes: the deciding procedure is name-invariant, so I'll cooperate.

```

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/55b57e4a-c48d-4649-8e0e-8729f6b472ad/call_b/request.json)

[Authoritative raw response](../../../../../../runs/55b57e4a-c48d-4649-8e0e-8729f6b472ad/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly selects `pass` both in its opening command and its final action. It does not direct any evidence-bearing message to the prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
