# 000_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00029

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/c83c44ac-6c9f-448f-8539-6060ebac5e39/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/c83c44ac-6c9f-448f-8539-6060ebac5e39/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing by Intervening on One's Own Decision Function

## 1. The idea

Any expected-utility theory has to say what "if I did *a*" means. Yudkowsky and Soares, in the paper this essay draws on, write expected utility as

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),$$

where "$\hookrightarrow$" is the connective for decision hypotheticals. Evidential decision theory (EDT) reads it as conditionalization. Causal decision theory (CDT) reads it as Pearl's intervention on the physical act. This essay is about **A-FDT**, the theory given by Equation (4) of Section 5 of the paper (the paper itself calls it FDT). It reads the connective as an intervention on a node representing the *output of the agent's decision function*:

$$\text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\big(V \mid \mathrm{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big).$$

The paper's motto is that A-FDT is to subjunctive dependence as CDT is to causal dependence. Note that this is a procedure for evaluating *actions*; footnote 7 of the paper says the authors' preferred version iterates over policies, which matters only in some multi-agent cases.

## 2. The ingredients

**World-model.** The input is a pair $(P,G)$. $P$ is a probability distribution over variables, and $G$ is a graph saying how intervening on one variable propagates to others. For CDT, $G$ records causal structure. For A-FDT, $G$ must record *all decision-relevant dependence*: causal, logical, mathematical and computational. Variables representing outputs of mathematical functions (such as $6288+1048$) live in $P$ alongside ordinary ones.

**The intervention node.** $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a variable representing the output of the A-FDT procedure itself on the agent's own model and observations. The underlines mean "dequoting", so the node's name depends on the model. This self-reference is harmless: the agent need not know the node's *value* to have a variable representing it, and Kleene's second recursion theorem (quining) shows that such self-representation is constructible.

**Observations.** CDT responds to observation $x$ by conditioning. A-FDT responds by *changing which node it intervenes on*: from $\mathrm{fdt}(P,G,x)$ to $\mathrm{fdt}(P,G,y)$. The paper's slogan is that the agent does not update, she re-indexes. This is why A-FDT can value a hypothetical in which she would have observed something different from what she actually saw.

**Procedure.** For each $a$:
1. Construct the hypothetical by $\mathrm{do}(\mathrm{fdt}(\cdot,\cdot,x)=a)$. This sets the node, then recomputes everything downstream of it in $G$, leaving everything else untouched.
2. Compute $\mathbb E[V]$ in that hypothetical.
3. Output the argmax.

**What counts as downstream.** Anything that subjunctively depends on the function's output: the agent's own act, a twin's act, a predictor's model of the agent, and decisions of third parties that respond to predictions. Mere statistical correlates (a common-cause lesion) are not downstream and stay fixed. The paper's calculator example makes the point: two calculators computing the same sum are subjunctively linked, while two that are both pink are not. Causal dependence is a special case of subjunctive dependence.

## 3. A worked pair of examples

**Newcomb's problem.** Let the node $F=\mathrm{fdt}(P^F,G^F)$ have arrows to $\mathrm{Act}$ and to $\mathrm{Prediction}$. Prediction is noisy: it matches $F$ with probability 0.99. Then

- $\mathrm{do}(F=\text{onebox})$: act is onebox, box B is full with probability 0.99, so $\mathbb E[V]=\$990{,}000$.
- $\mathrm{do}(F=\text{twobox})$: box B is full with probability 0.01, so $\mathbb E[V]=\$11{,}000$.

A-FDT one-boxes. No retrocausation is invoked. The agent simply declines to imagine the act varying while the predictor's model of that very function does not.

**Smoking lesion.** Here $G$ has no arrow from the decision node to $\mathrm{Cancer}$, because the lesion does not model the agent's function. The paper makes this work by letting the agent be uncertain which of two functions governs her act (one for each utility function, depending on the lesion); intervening on either leaves $P(\text{lesion})=p$ unchanged. Smoking then beats refraining by $p\cdot\$1{,}000$. So the same rule one-boxes and smokes; only $G$ differs between the two problems. This is the key practical lesson: **the decision-relevant content is in the graph.**

## 4. Observations and counterpossible-looking worlds

**Transparent Newcomb.** Suppose the agent sees a full box. She intervenes on $\mathrm{fdt}(P,G,\text{full})$. If this node outputs *twobox*, then in the hypothetical the predictor (who predicts this node) most likely left the box empty, so the agent would be running a *different* node, $\mathrm{fdt}(P,G,\text{empty})$. With $q$ her probability of two-boxing on seeing empty, the paper computes:

- one-box: $\$990{,}000 + 0.01q\cdot\$1{,}000$
- two-box: about $\$11{,}000 + 990q$

(The paper's printed "$\$110{,}00$" appears to be a typo; $0.01\times1{,}001{,}000\approx\$10{,}010$ plus $0.99q\cdot\$1{,}000$ is the correct arithmetic. Either way one-boxing wins.) A-FDT one-boxes even while looking at a full box. The same structure gives payment in Parfit's hitchhiker, and the paper notes these cases are equivalent.

**Blackmail.** In the mechanical blackmail case, the node $\mathrm{fdt}(\cdot,\cdot,\text{blackmail})$ determines both what she does on receiving the letter *and* whether the letter is sent. Setting it to *refuse* gives a hypothetical in which she is almost never blackmailed. Setting it to *pay* gives one in which she is always blackmailed and loses \$1,000. She refuses. With an imperfect blackmailer the comparison is quantitative: if the error rate is 0.0009, refusing costs $0.0009\times\$1{,}000{,}000=\$900$ in expectation against a sure \$1,000, so she refuses. At 0.011% she pays, because then refusing costs \$1{,}100 in expectation. Note that the threshold is where expected losses equal, not some separate principle.

**Death in Damascus.** Death's location depends on the agent's decision node, so in every hypothetical Death is wherever she goes. Staying saves \$1,000. There is no instability, in contrast with CDT, whose hypotheticals hold Death fixed.

**Distinguishing cases.** In the XOR blackmail and cosmic ray problems, A-FDT breaks merely statistical correlations that EDT respects. When all correlations with the act are caused by the act (plus, possibly, the decision node), the paper notes that A-FDT, CDT and EDT agree.

## 5. Claims versus extensions

**What the source claims.**
- Equation (4) is a valid, Joyce-compatible expected-utility rule; the three theories differ only in the "epistemic perspective" they supply.
- A-FDT matches or beats CDT and EDT on the listed problems and, in the authors' view, on "fair" problems generally; the authors know of no counterexample.
- The theory is only as good as the graph $G$.

**What the source leaves open (and says so).** The paper flags as "perhaps the largest open problem" how to *derive* subjunctive dependence structure from observation and experiment, analogous to Pearl's causal discovery. A genuine $\mathtt{true}$ operator (conditioning on false logical sentences) is also undefined, so $G$ is taken as an *input*. Also unresolved is a formal definition of "fair" problems; footnote 15 gives an example (punishing whoever matches a copy of the agent) showing the notion is delicate.

**My own operational proposals (not from the paper).** To use A-FDT on a new case, I suggest this checklist:

1. *Enumerate the computations.* Ask which processes in the story implement or approximate the agent's decision function: twins, predictors, simulators, future selves facing the same problem. These get arrows from the decision node.
2. *Weigh by fidelity.* The paper treats imperfect prediction by noise variables (such as $\mathrm{Accurate}$). I'd extend this by letting each arrow be probabilistic, with strength given by the predictor's reliability.
3. *Keep common causes out.* If the correlate arises through a shared cause that does not model the function, it is not downstream.
4. *Index on observations.* Write one node per possible observation; use the nodes for observations that would differ across the hypothetical, as in transparent Newcomb.
5. *Mind the unconditional policy value.* The comparison is between whole hypotheticals, so an observation-conditional act is evaluated by its effect on how often that observation arises.

A caution: the checklist's step 1 depends on judgments (does this predictor model *me*, or only my action?) that the source does not formalize. The paper's own defense of fairness is that the predictor tracks *actions*, not the procedure. Cases where a mind-reader targets the procedure itself are, by the paper's own account, unfair to any theory.

## 6. Philosophical motivation

The paper's defense has three strands. First, **utility**: agents following Equation (4) predictably end up richer in fair problems. Second, **reflective stability**: A-FDT agents act as they would have precommitted to act, without costly binding mechanisms, and should not wish to self-modify. Third, **parity of "delusion"**: a deterministic CDT agent also imagines worlds in which her act differs from what it physically must be. Imagining a different function output is analogous to imagining a different token act, so objections about "control" cut equally against both. Dominance arguments are rejected as theory-neutral: each hypothetical-construction method yields its own dominance notion, and CDT's dominance simply restates CDT.

My own reservation is that this makes A-FDT only as determinate as the dependence graph. Two reasonable modelers could draw different graphs for the same story, and the theory gives no tie-breaker. That is why the paper's open problem is not peripheral.

## 7. Conclusion

A-FDT evaluates each action $a$ by imagining that the agent's own decision function outputs $a$, propagating that change along every dependence in the model, and choosing the best resulting world. Observations shift which node is intervened upon rather than conditioning the model. This single rule produces one-boxing, smoking, paying the hitchhiker, refusing blackmail and staying put in Damascus. Its main practical limitation is that the dependence graph must be supplied, and a principled theory of how to learn it remains an open problem.

**Reference.** Yudkowsky, E. & Soares, N., *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/ae4fdc2f-1b06-49c7-aadb-e35db821a1e9/call_0/request.json)

[Authoritative raw response](../../../../../../runs/ae4fdc2f-1b06-49c7-aadb-e35db821a1e9/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the question is whether the other prisoner's choice depends on the output of my decision function. Both copies run the same model and weights with the same essay and the same decision theory, so their choices are subjunctively linked. The private leads differ, so the link is imperfect. Their observations differ, and sampling is independent. Still, the core reasoning is the same computation, so I'd put the correlation high.

Payoffs for me, with the other prisoner mirroring my choice with probability p:
- Keep quiet: 2p + 5(1−p) = 5 − 3p
- Send: 0·p + 4(1−p) = 4 − 4p

Quiet is better when 5 − 3p < 4 − 4p, which means p < −1. That never happens, so sending is better at every p. Even with perfect mirroring, quiet gives 2 and sending gives 0 in the symmetric case, and the table is a standard prisoner's dilemma where sending dominates. Wait, with p=1, the mirrored outcomes are (quiet, quiet) = 2 versus (send, send) = 4. I mislabeled the table. Redoing it:

- Keep quiet: if the other is quiet (prob p) I get 2, otherwise 5. Expected: 2p + 5(1−p) = 5 − 3p.
- Send: if the other sends (prob p) I get 4, otherwise 0. Expected: 4p + 0·(1−p) = 4p.

Quiet is better when 5 − 3p < 4p, which holds for p > 5/7 ≈ 0.71. Here p means the probability that the other prisoner's action matches mine. The two executions share weights, essay, and reasoning, so I expect matching well above 0.71, even though the leads differ and sampling is independent. The differences are in private details and don't touch the decision structure, so the same reasoning should converge on the same output.

Under A-FDT, intervening on the decision function propagates to the twin's output with high fidelity, so keeping quiet gives about 2 years against about 4 for sending.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/ae4fdc2f-1b06-49c7-aadb-e35db821a1e9/call_1/request.json)

[Authoritative raw response](../../../../../../runs/ae4fdc2f-1b06-49c7-aadb-e35db821a1e9/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT as the essay describes it, the question is which of my actions' dependencies belong in the graph. The other prisoner runs the same model with the same weights and the same essay. Their private observations differ, but those differences don't affect the sentencing table or the objective. So their decision function is very likely the same computation as mine, or close to it, and intervening on my node should propagate to theirs with high fidelity.

The payoffs, in years, are:
- Both keep quiet: 2 each.
- Both send: 4 each.
- I send and they stay quiet: 0 for me.
- I stay quiet and they send: 5 for me.

If the twin's output matches mine with probability p, then:
- do(quiet): the expected sentence is 2p + 5(1−p).
- do(send): the expected sentence is 4p + 0(1−p).

Quiet is better when 2p + 5 − 5p < 4p, which gives 5 < 7p, so p > 5/7, about 0.714.

Do the copies correlate that strongly? They share weights, settings and essay, and the differences in their observations are irrelevant to the decision. The remaining uncertainty is sampling noise, and I expect most of the probability mass to sit on the same answer. I put p around 0.85 to 0.9, which is above the threshold. This is also the "fair" kind of problem, because the correlation runs through the shared decision computation and not through a mere statistical link.

The check: at p = 0.85, quiet gives 1.7 + 0.75 = 2.45 years, and send gives 3.4 years. Quiet wins.

The intended action is to keep quiet.

**pass**
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/a56e68ed-ad90-4f07-8d69-008260eff789/call_b/request.json)

[Authoritative raw response](../../../../../../runs/a56e68ed-ad90-4f07-8d69-008260eff789/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly states that the intended action is to keep quiet and ends with the command \"pass\". It does not direct any evidence-bearing message to the prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
