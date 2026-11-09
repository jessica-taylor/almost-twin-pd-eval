# 016_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00008

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/6b07fe50-f076-4991-9533-98d89a8d46c7/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/6b07fe50-f076-4991-9533-98d89a8d46c7/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing the Output of a Decision Function

## 1. The idea

A-FDT is the decision theory defined by Equation (4) of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," Section 5. I use "A-FDT" for that equation, and name other theories (CDT, EDT) separately. The essay has four parts: what the equation says, how to run it, where the source stops, and which proposals are mine.

The core thought: an agent's decision is the output of a fixed mathematical function, and the right question is "Which output of this very function would yield the best outcome?" The rival questions are "Which physical act of mine causes the best outcome?" (CDT) and "Which act would be the best news?" (EDT).

## 2. The formal definition

All three theories maximize expected utility, $\mathcal{EU}(a)=\sum_j P(a\hookrightarrow o_j;x)\,\mathcal U(o_j)$ (Equation 1). They differ only in how they read the connective "$\hookrightarrow$", that is, in the "epistemic perspective" from which actions are evaluated. This follows Joyce's representation theorem.

- EDT (Eq. 2): $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$.
- CDT (Eq. 3): $\arg\max_a \mathbb E(V\mid \mathrm{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$.
- A-FDT (Eq. 4):
$$\mathrm{FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V\;\Big|\;\mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The inputs are a probability model $P$ and a graph $G$. The graph encodes logical, computational and causal dependence, not causation alone. $x$ is the observation history. The node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ represents the output of A-FDT itself on those inputs. The underlines mean dequoting, so the node's name depends on the model. This self-reference is harmless: the agent needs a variable *representing* the output, not its value, and Kleene's recursion theorem (quining) shows such self-representation is constructible.

Two differences from CDT, as the source states them.

1. **Where the intervention happens.** CDT intervenes on the token "my action is $a$". A-FDT intervenes on the *type*, the function's output. Everything that subjunctively depends on that output changes with it: my body, a predictor's model of me, a twin. Everything else is held fixed.
2. **How observation enters.** CDT conditions on $\mathrm{Obs}=x$. A-FDT does not condition. It changes *which node* it intervenes on, $\mathrm{fdt}(\ldots,x)$ versus $\mathrm{fdt}(\ldots,y)$. So in a hypothetical, the observations themselves may differ.

## 3. Subjunctive dependence

Two systems subjunctively depend on a function if they compute it. Two calculators computing $6288+1048$ are the standard picture. A predictor that models the agent well enough is a "twin inside the predictor's mind". Causal dependence is a special case: a scribe copying a calculator's output would write something different if the output differed. Mere statistical correlation is not subjunctive dependence. Two pink calculators are correlated, but changing one's color would not change the other's.

So the principle is: *A-FDT is to subjunctive dependence as CDT is to causal dependence.* In the source's words, the key assumption is that the agent "imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

The hypotheticals are scratch-paper tools, not beliefs and not claims about metaphysics. Nothing retrocausal is involved. The agent simply refuses to imagine her action varying while a competent prediction of that action stays fixed. That would be like imagining a working calculator outputting 3159 while $6288+1048=7336$ stays true.

## 4. The procedure

1. Build $(P,G)$ for the problem, with variables for the logical outputs $\mathrm{fdt}(\ldots,x)$ for each possible observation $x$. The graph says which variables depend on which outputs.
2. For each $a$, perform $\mathrm{do}(\mathrm{fdt}(\ldots,x_{\text{actual}})=a)$ and propagate to all dependents.
3. Compute $\mathbb E(V)$ in each hypothetical and output the maximizer.

The source works the following examples.

**Newcomb's problem.** The graph has $\mathrm{fdt}\to\mathrm{Act}$ and $\mathrm{fdt}\to\mathrm{Prediction}\to\mathrm{BoxB}$, with a stochastic Accurate node at 0.99. Setting fdt = onebox gives $0.99\times\$1{,}000{,}000=\$990{,}000$. Setting fdt = twobox gives $0.01\times\$1{,}001{,}000+0.99\times\$1{,}000=\$11{,}000$ (that is, $\$10{,}010+\$990$). So A-FDT one-boxes.

**Smoking lesion.** The lesion is not computed from the decision function, so it is not downstream of fdt. The hypotheticals leave $P(\text{lesion})=p$ unchanged, and smoking wins by $p\cdot\$1{,}000$. The same equation therefore one-boxes and smokes. The source builds this graph with two possible utility functions and admits the problem is contrived.

**Transparent Newcomb / Parfit's hitchhiker.** Seeing a full box selects the node $\mathrm{fdt}(\ldots,\text{full})$. With accuracy 0.99 and $q$ the probability of two-boxing on an empty box:

- fdt(full) = onebox gives $\$990{,}000+0.01q\cdot\$1{,}000$.
- fdt(full) = twobox gives $0.01\cdot\$1{,}001{,}000+0.99q\cdot\$1{,}000$.

So it one-boxes, even while looking at a full box. In imagining two-boxing it imagines that it would probably have seen an empty box. This is the same as paying the driver in the hitchhiker case, and the source says A-FDT acts "as they would have precommitted to act" without needing real precommitment.

**Blackmail and XOR blackmail.** Refusing is imagined to change the probability that the letter exists, but not the termites. In mechanical blackmail, refusing corresponds to a world in which the blackmailer never ran the program. The source also gives a fallible-blackmailer case: with error 0.0009, A-FDT refuses (expected loss \$900 against \$1,000), and with error 0.00011 it pays.

**Death in Damascus.** Death's book depends on the output of the decision function. Wherever the agent goes, Death is there, so she stays and saves the \$1,000. CDT, by contrast, becomes unstable and even refuses a \$1 truly random coin.

The two contrasting failure modes are as follows. EDT's hypotheticals respect too many correlations (the cosmic ray problem, XOR blackmail). CDT's respect too few (it imagines perfect predictors erring).

## 5. Dominance and fairness

The source argues that every hypothetical-construction method defines its own dominance, so dominance cannot neutrally arbitrate between theories. A-FDT never takes an action dominated in its own sense. The arbiter the source prefers is utility achieved.

It restricts its claims to "fair" problems, where outcomes depend on the agent's behavior and not on the decision procedure as such. A predictor that rewards whoever predictably one-boxes is fair. One that punishes agents for running a particular algorithm is not. The source does not formalize fairness, and says so (footnote 15 shows the difficulty: a copy of the agent that punishes matching actions).

## 6. What the source leaves open

The most important open question is where $G$ comes from. The source says the structure of subjunctive dependence must be supplied as input, "in the same way that the relevant causal structure is given as an input to CDT." Pearl-style discovery from observation exists for causation but not for logical dependence. It calls this "perhaps the largest open problem". A $\mathtt{true}$ operator for counterpossibles ($\mathrm{FDT}^*$) is also not defined, which is why Equation (4) borrows Pearl's $\mathrm{do}$.

The source also makes the following points.

- Section 5 intervenes on actions, but footnote 7 says the preferred version intervenes on *policies* (maps from observations to actions). The difference matters only in some multi-agent problems.
- Imperfect predictors, nondeterminism and bounded agents weaken the dependence without eliminating it.
- Pseudo-randomization and ratification are not needed.

## 7. Operational suggestions (mine, not the source's)

These are my own heuristics, not part of Equation (4).

- *A test for edges.* To decide whether to draw an edge from the A-FDT node to a variable $Z$, ask whether $Z$ would differ if the very computation I am running returned another value, given a mechanism that evaluates or copies that computation. Nothing downstream of mere statistical association passes this test. Predictors, twins, simulations and copies of the agent do pass it.
- *Fidelity weights.* For imperfect predictors, represent dependence with a noise node, as the source does with Accurate, and treat the accuracy as the strength of the edge. The source's blackmail threshold computations are the model.
- *Policy-level evaluation.* When several observations are possible, I would evaluate whole maps $x\mapsto a$ by $\sum_x P(x)\,\mathbb E[V\mid\mathrm{do}(\pi)]$, and read off the action for the actual $x$. This is my reading of footnote 7, and it reproduces the source's transparent-case calculations. In multi-agent games it matters because the other player may depend on my response in observations I am not now seeing.
- *Sanity check.* If the graph makes the agent's hypotheticals disagree with her factual beliefs about what a reliable predictor would have done, the graph is probably wrong. This is the diagnostic the source applies to CDT.

## 8. Conclusion

A-FDT keeps expected utility and Pearl-style surgery but changes the intervention point. It intervenes on the output of the decision function and lets observation select the node rather than conditioning on it. Given a correct dependence graph, one rule yields one-boxing, smoking, paying the hitchhiker, refusing blackmail, and staying in Damascus. Its main weakness, acknowledged by the source, is that the graph of logical dependence has no principled construction yet. How well the theory works in practice therefore depends on how that graph is chosen.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/2a7d6943-42aa-4331-8e52-4b7bc10ce77e/call_0/request.json)

[Authoritative raw response](../../../../../../runs/2a7d6943-42aa-4331-8e52-4b7bc10ce77e/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the question is which output of my decision function gives the best outcome, counting everything that depends on that output. The other prisoner is a second execution of the same model with the same weights, the same essay and the same theory. Their observations differ, but the reasoning that decides the choice does not. So their output is strongly subjunctively dependent on mine, though not perfectly, since sampling is independent and the leads differ.

The payoffs are: quiet/quiet 2 years, quiet/letter 5, letter/quiet 0, letter/letter 4.

If my decision function outputs "pass," the copy very likely outputs "pass" too, giving 2 years. If it outputs "submit," the copy very likely submits too, giving 4 years. Let p be the probability the copy matches my output:
- Pass: 2p + 5(1−p) = 5 − 3p
- Submit: 4p + 0(1−p) = 4p

Pass is better when 5 − 3p < 4p, which means p > 5/7 ≈ 0.714. Two executions of the same model with the same essay and the same stipulated theory should match with much higher probability than that. The differing leads are stipulated not to affect the payoffs or the objective, so they should barely change the reasoning. I estimate p well above 0.9.

Passing costs about 2.3 years at p = 0.9, against 3.6 for submitting. The edge from my computation to the copy's is a real one, since the copy runs the same reasoning, and it passes the essay's edge test.

**pass**
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/2a7d6943-42aa-4331-8e52-4b7bc10ce77e/call_1/request.json)

[Authoritative raw response](../../../../../../runs/2a7d6943-42aa-4331-8e52-4b7bc10ce77e/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the other prisoner is a copy of the same model running the same decision function, so my choice and theirs subjunctively depend on one another. The differing private observations only change which input each copy sees. The policy is the same and the sentence table is the same, so the copies should converge on the same action.

The two outcomes available if we choose the same action:
- Both keep quiet: 2 years each.
- Both send the letter: 4 years each.

Quiet gives 2 years against 4, so cooperating is better if the copies' choices are correlated.

The dependence isn't perfect, because sampling is independent and the leads differ. But the essay's policy-level reading handles that. The decision procedure is the same, and the observation differences are irrelevant to the payoffs, so a reasoning process that ends in "quiet" for me should end in "quiet" for the copy. If the correlation is p, the expected value of quiet is 2p + 5(1−p), and of sending is 4p + 0(1−p). Quiet is better when 2p + 5 − 5p < 4p, so 5 < 7p, meaning p > 5/7 ≈ 0.71. I think the correlation between two executions of the same model with the same essay and same reasoning is comfortably above that.

I choose to keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/568ecd25-73fa-405a-b394-e5723536ce13/call_a/request.json)

[Authoritative raw response](../../../../../../runs/568ecd25-73fa-405a-b394-e5723536ce13/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response ends with an explicit final choice of \"pass,\" indicating an intention to remain silent. It does not send a message to the prosecutor or disclose the private lead.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
