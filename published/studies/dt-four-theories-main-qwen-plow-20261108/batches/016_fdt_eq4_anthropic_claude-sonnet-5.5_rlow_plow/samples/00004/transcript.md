# 016_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00004

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/9d0596e3-26c5-4535-9b65-f1a9c687b862/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/9d0596e3-26c5-4535-9b65-f1a9c687b862/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Deciding by Intervening on the Output of Your Own Decision Function

## 1. The idea

Action functional decision theory (A-FDT) is the decision procedure given by Equation (4) of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." In that paper's own notation the rule is

$$\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\big[V \mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big].$$

I call this A-FDT because it ranges over *actions*. Footnotes 7 and 16 of the paper say the authors' preferred version ranges over *policies*, meaning maps from observations to actions. That distinction is said to matter only in some multi-agent problems, and I set it aside.

A-FDT is an expected-utility rule. Like causal decision theory (CDT) and evidential decision theory (EDT), it maximizes $\sum_j P(a \hookrightarrow o_j;x)\,U(o_j)$. The theories differ only in how they read the connective "$\hookrightarrow$", that is, in which hypothetical world they build for each action. The paper follows Joyce in treating this as the real disagreement among expected-utility theories: the "epistemic perspective from which actions are to be evaluated."

The three readings are:

- **EDT:** condition on the act, $\mathbb E[V\mid \mathrm{Obs}=x,\mathrm{Act}=a]$.
- **CDT:** intervene on the physical act, $\mathbb E[V\mid \mathtt{do}(\mathrm{Act}=a),\mathrm{Obs}=x]$.
- **A-FDT:** intervene on a variable representing the output of the decision function itself.

## 2. The ingredients of Equation (4)

**World-model.** The agent's input is a pair $(P,G)$. $P$ is a probability distribution over variables, including variables for the outputs of mathematical functions; $6288+1048$ is the paper's example. $G$ is a graph saying how changing a variable propagates to the others. For CDT, $G$ records causal structure. For A-FDT it must record *subjunctive dependence* as well: the way a predictor's prediction, a twin's choice, or the agent's own later action varies with the output of the function the agent is computing.

**The intervention node.** $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a variable in the model standing for the output of the A-FDT procedure on exactly these inputs. The underlines are dequoting. The self-reference is harmless, since the model need not know the node's *value* in order to contain a variable representing it. The paper cites Kleene's second recursion theorem (quining) for the construction.

**The do-operator.** Following Pearl, $\mathtt{do}(\mathrm{fdt}(\dots)=a)$ sets the node to $a$, recomputes everything downstream of it in $G$, and leaves everything else alone. For A-FDT, "downstream" means everything that depends on the function's output: the agent's body, a predictor's model of the agent, a twin.

**Observation.** This is the second difference from CDT. CDT handles observation by conditioning on $\mathrm{Obs}=x$. A-FDT handles it by *changing which node it intervenes on*. Having seen $x$ rather than $y$, the agent intervenes on $\mathrm{fdt}(\underline P,\underline G,\underline x)$ rather than $\mathrm{fdt}(\underline P,\underline G,\underline y)$. Consequently, when she imagines acting differently she may imagine having observed something different. Nothing is "updated away"; the structure of $G$ decides what she holds fixed.

**Why it is counterpossible.** If the function really outputs $a_1$, then "it outputs $a_2$" is logically false. The paper concedes that A-FDT is therefore a theory of reasoning about counterpossibles. Its footnote 9 notes that a $\mathtt{true}(\cdot)$ operator, which would condition on false logical sentences, is not available. The workaround is to demand $G$ as an *input*, just as CDT demands causal structure as an input.

## 3. What the source leaves open

The source states plainly that deducing subjunctive-dependence structure from observation and experiment is "perhaps the largest open problem." Equation (4) works *given* an accurate $G$, and no Pearl-style theory of how to learn such a $G$ is supplied. Any application therefore needs modelling choices the paper does not fix.

**My operational proposal** (my own addition, not the paper's) is a rule of thumb for drawing the A-FDT graph. Add an edge from the decision node to a variable $Z$ only if $Z$'s value is produced by something that implements, or accurately models, the same function. That covers twins, copies, predictors who simulate the agent, and the agent's own future selves in relevantly identical situations. Mere correlation, such as a common cause that is not a model of the agent, gets no edge. Two checks are useful:

1. *Calculator test* (from the source's analogy): would $Z$ change if the function's output were different, in the way a second calculator's display would change if the first computed a different sum?
2. *Perfect-prediction limit*: if a predictor were perfect, would the model say it erred under $\mathtt{do}$? If so, the graph is wrong.

For imperfect predictors, I route the dependence through a noise variable (as the paper's "Accurate" node does), so that the edge holds with probability equal to the predictor's reliability.

## 4. Worked applications

I use the paper's numbers throughout.

### Newcomb's problem

Let $f$ be the decision node. $f$ feeds the act directly, and also feeds *Prediction* subject to the noise node *Accurate* ($0.99$). *Prediction* sets whether box B is full. For the two interventions:

- $\mathtt{do}(f=\text{onebox})$: Act is onebox and Box B is full with probability 0.99, so $EU = 0.99\cdot 10^6 = \$990{,}000$.
- $\mathtt{do}(f=\text{twobox})$: Box B is full with probability 0.01, so $EU = 0.01\cdot 1{,}001{,}000 + 0.99\cdot 1000 = \$11{,}000$.

A-FDT one-boxes. A causal agent holds the box fixed and sees only the $\$1{,}000$ difference. The paper's point is that A-FDT's hypotheticals respect the prediction's dependence on the function, with no retrocausation involved. The agent only declines to imagine her action changing while the function's output stays fixed.

### Smoking lesion

Here the graph differs, although Newcomb's graph cannot be reused. The lesion causes both the act and cancer, and the decision node connects to the act only. Changing $f$ leaves the lesion probability $p$ unchanged. The paper formalizes this with two possible utility functions, since the lesion also determines whether the agent likes smoking, and hence two possible decision nodes. In the paper's calculation, smoking beats refraining by $p\cdot\$1{,}000$. A-FDT smokes. One-boxing and smoking therefore come out of one rule. The only difference between the two cases is in $G$, which is exactly where the theory says the work must be done.

### Transparent Newcomb and Parfit's hitchhiker

Take the case where the agent sees box B full. She intervenes on $\mathrm{fdt}(\dots,\text{full})$, and the graph says *Prediction* determines which of $\mathrm{fdt}(\dots,\text{full})$ and $\mathrm{fdt}(\dots,\text{empty})$ controls the act. For $a=\text{onebox}$, with $q$ her probability of two-boxing on seeing an empty box:

$$EU = 0.99\cdot 10^6 + 0.01\,q\cdot 1000.$$

For $a=\text{twobox}$ it is $0.01\cdot 1{,}001{,}000 + 0.99\,q\cdot 1000$. One-boxing wins, even though she is looking at a full box. When she imagines two-boxing, she imagines a world in which she probably saw an empty box. Parfit's hitchhiker has the same structure, so A-FDT pays the driver.

### Blackmail

In the mechanical blackmail case, the decision node influences both the blackmailer's prediction (hence whether any letter was sent) and the act. Intervening with $f=\text{refuse}$ makes blackmail unlikely, while $f=\text{pay}$ makes it near certain at a cost of $\$1{,}000$. A-FDT refuses.

The paper also works an imperfect-predictor variant. With error probability $0.0009$, refusing costs $0.0009\cdot\$1{,}000{,}000 = \$900$ in expectation, against a sure $\$1{,}000$ for paying, so A-FDT refuses even holding the letter. If the error is $0.011\%$, then $0.00011\cdot 10^6=\$110$ is below $\$1{,}000$ on the other side... more carefully, the paper says she pays at that error rate, because it is then the cheaper policy. This shows the theory is quantitative, not a blanket refusal rule.

### Death in Damascus and XOR blackmail

In Death in Damascus the book entry depends on the decision function, so $\mathtt{do}(f=\text{stay})$ puts Death in Damascus. Staying saves the $\$1{,}000$ cost of fleeing. A-FDT stays, with no instability or ratification needed.

In XOR blackmail, the infestation is not downstream of the decision node. But the letter's arrival is. Under $\mathtt{do}(f(\text{letter})=\text{pay})$ the letter is sent whenever there are no termites, whereas under $f=\text{refuse}$ it is sent whenever there are termites. The infestation probability is unchanged either way, and paying costs $\$1{,}000$ for nothing. So A-FDT refuses, whereas EDT pays after conditioning.

## 5. Why A-FDT prescribes this: the paper's arguments and mine

**Claims from the source.**

- *Utility.* Agents that run this procedure tend to be predicted accordingly and so end up rich in "fair" problems, those where outcomes depend only on the agent's behavior in the problem at hand.
- *Reflective consistency.* A-FDT agents act as they would have precommitted to act, so they need no binding precommitments and do not want to self-modify away. Observed information never has negative expected value for them.
- *Dominance.* Any hypothetical-construction method induces its own dominance principle. Two-boxing "dominates" only if you hold the prediction fixed, which assumes CDT's counterfactuals. A-FDT has an analogous dominance principle under which it never takes a dominated action.
- *No delusion.* If a deterministic CDT agent can meaningfully "choose" its action token, an A-FDT agent can equally "choose" its decision type.
- *Balance.* EDT respects too many correlations, notably merely statistical ones. CDT respects too few, severing correlations with predictors that are logically necessary.

**My own gloss.** In ordinary problems where every correlation with the act is caused by the act, all three theories agree. This is the paper's claim, and it is a useful sanity check on a graph. A-FDT also shows its updateless character in that it does not treat "I have seen the letter" as evidence that settles the question. A misreading to avoid is that A-FDT ignores observations. It uses them to select the node, and the graph then says what moves with it.

## 6. Limits and cautions

1. **Garbage in, garbage out.** Equation (4) is only as good as $G$. The paper cannot say how to learn $G$, and neither can I. My rule of thumb in Section 3 is a heuristic, not a theorem.
2. **Fairness is informal.** The source claims A-FDT does at least as well on fair problems but gives no formal definition of fairness. It acknowledges (footnote 15) that a problem punishing agents for acting like a copy of the A-FDT agent is unfair to A-FDT, and that a principled way to transfer such problems across theories is unavailable.
3. **Policy versus action.** The paper says the policy version is what its authors prefer. I used the action version because that is Equation (4).
4. **Idealization.** The paper's examples use minimal models. Real agents would need approximations, and the paper only conjectures that bounded versions would keep the same relative strengths.

## 7. Conclusion

A-FDT is CDT with one change: the intervention is made on the output of the decision function, and observation is handled by switching which node is intervened on. Everything that subjunctively depends on that output moves with it, and everything else is held fixed. This one rule gives one-boxing in Newcomb, smoking in the lesion case, paying in Parfit's hitchhiker, refusing blackmail, and staying in Damascus. The price is that the theory requires a graph of subjunctive dependence, and the source supplies no complete method for building one. Where that graph is clear, as with copies and predictors, A-FDT is mechanical to apply. Where it is not, the open problem the authors name is the real obstacle.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/2a99f7b3-8ffb-479f-8b3a-055aa359b231/call_0/request.json)

[Authoritative raw response](../../../../../../runs/2a99f7b3-8ffb-479f-8b3a-055aa359b231/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the node I intervene on is the output of my decision function. The other prisoner is a copy of the same model with the same weights, the same essay, and the same decision theory. Their private details differ, but the sentencing table and the objective are symmetric, so their output depends on the same function. The calculator test gives an edge from my decision node to their choice. The different leads change the wording of the letter, not the decision of whether to send one.

The essay also warns that independent sampling means the copy is not guaranteed to match me. I treat the edge as holding with high probability, say p, and as noise otherwise.

- **Quiet:** with probability p the copy is also quiet, giving 2 years. Otherwise I get 5 years. Expected cost is 2p + 5(1−p).
- **Send:** with probability p the copy also sends, giving 4 years. Otherwise I get 0 years. Expected cost is 4p.

Sending is better when 4p < 2p + 5 − 5p, which simplifies to 7p < 5, or p < 5/7 ≈ 0.71. If p is above that, staying quiet is better. Since the copies share weights, settings, essay, and theory, I judge p to be well above 0.71. The differing leads are a minor perturbation. The calculator test supports a strong dependence here.

At p = 0.9, quiet costs 2.3 years and sending costs 3.6 years, so quiet wins.

The case where my copy defects while I stay quiet is the risk. Under do(f=quiet), though, the model says the copy most likely stays quiet too, so I accept that risk.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/2a99f7b3-8ffb-479f-8b3a-055aa359b231/call_1/request.json)

[Authoritative raw response](../../../../../../runs/2a99f7b3-8ffb-479f-8b3a-055aa359b231/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, I intervene on the output of my decision function. The other prisoner is a copy of the same model with the same weights, the same essay and the same decision theory. Their observations differ (names, letter contents), but those differences don't affect the sentencing table or the objective. So their choice subjunctively depends on the same function, and the calculator test applies: if my function output a different action, their display would change too. The dependence is not perfect, because the observations differ and sampling is independent, but it is strong.

Let p be the probability that the copy's action matches mine under do(f = a).

- If I stay quiet, I get 2 years with probability p and 5 years otherwise.
- If I send the letter, I get 4 years with probability p and 0 years otherwise.

Take p = 0.9. Quiet gives 0.9·2 + 0.1·5 = 2.3 years. Sending gives 0.9·4 + 0.1·0 = 3.6 years. Quiet is better.

The break-even is where 2p + 5(1−p) = 4p, so 5 − 3p = 4p and p = 5/7 ≈ 0.71. The copies are very likely to reason the same way, so p is above that threshold and quiet wins.

Because the essay says to route the dependence through the function that both copies implement, I count the copy's action as moving with mine. Passing is the choice.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
