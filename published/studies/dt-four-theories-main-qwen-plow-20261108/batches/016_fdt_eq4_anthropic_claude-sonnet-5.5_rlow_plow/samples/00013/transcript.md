# 016_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00013

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/c5d081f7-9051-41e6-979e-69a1388a215c/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/c5d081f7-9051-41e6-979e-69a1388a215c/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing by Intervening on One's Own Decision Function

## 1. The idea

Decision theories differ less in their values than in the hypotheticals they use to evaluate acts. The source (Yudkowsky and Soares, *Functional Decision Theory*) takes Joyce's point that expected-utility theorists agree on how to value prospects and disagree only about "the epistemic perspective from which actions are to be evaluated." In this essay, **A-FDT** is the decision procedure given by Equation (4) of Section 5. A-FDT uses the same expected-utility form as causal decision theory (CDT), but it intervenes on a different variable.

I separate three things below: what the source says, what I infer from it, and what I propose myself.

## 2. The formal definition

Every theory in the source maximizes
$$\mathcal{EU}(a)=\sum_j P(a\hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$
where $\hookrightarrow$ is a decision-hypothetical connective. Evidential decision theory (EDT) reads it as conditioning. CDT reads it as Pearl's $do$.

For A-FDT the agent holds a world-model $(P,G)$. Here $P$ is a probability distribution that includes variables for the outputs of mathematical functions, such as the value of $6288+1048$. $G$ is a graph saying how changing such a variable propagates to other variables. The agent also has an observation $x$. The source's Equation (4) is

$$\text{A-FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\big(V\mid do(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big).$$

The underlines denote dequoting. The variable $\mathrm{fdt}(\underline P,\underline G,\underline x)$ represents the output of A-FDT itself on these inputs. The self-reference is harmless: the agent need not know the value of this variable to have a variable representing it, and the source cites Kleene's second recursion theorem ("quining") to show such self-representation is constructible.

The source states two differences from CDT.

1. CDT intervenes on a node $\mathrm{Act}$ for the physical action. A-FDT intervenes on a node for the output of its decision procedure. Where the source says CDT intervenes on the *token* "my action is $a$," A-FDT intervenes on the *type*.
2. CDT handles observations by conditioning on $\mathrm{Obs}=x$. A-FDT handles them by changing which node it intervenes on: $\mathrm{fdt}(\ldots,x)$ versus $\mathrm{fdt}(\ldots,y)$. Observations do not update the distribution used in the hypothetical.

The source's footnotes add that the authors' preferred formalization intervenes on a *policy*, a map from observations to actions. They say this matters only in some multi-agent problems and set it aside. I follow the source and work with actions given $x$.

## 3. Subjunctive dependence

The graph $G$ must encode subjunctive dependence. The source defines it as follows: when two systems compute the same function (or one contains an accurate model of the other), their behaviors "subjunctively depend" on that function. The source's analogy is that A-FDT is to subjunctive dependence as CDT is to causal dependence.

Three properties are worth keeping in view.

- Causal dependence is a special case. A scribe copying a calculator's output would write something different if the output were different.
- Mere statistical correlation does not count. If two calculators are both pink by coincidence, repainting one does not change the other.
- Imperfect predictors weaken the dependence without eliminating it, as with a calculator that occasionally errs.

The operational test is the source's: when the agent imagines taking different actions, she imagines changes in all and only those things that subjunctively depend on the output of her decision procedure.

## 4. The surgery procedure

A-FDT can be run as a recipe. It is mine in organization, though each step is in the source.

1. Build $(P,G)$ with the decision function's output as a node (one node per possible observation, when observations matter).
2. For each $a$, set that node to $a$. Propagate along the arrows of $G$, which carry both causal and subjunctive dependence. Hold everything else at its prior.
3. Compute expected utility in each resulting hypothetical.
4. Output the maximizer.

The source's example is Newcomb's problem. Fiona's graph has $\mathrm{fdt}$ as a parent of both $\mathrm{Act}$ and $\mathrm{Prediction}$, and the predictor is 99% accurate.

- $do(\mathrm{fdt}=\textit{onebox})$ gives box B full with probability 0.99, for $0.99\times\$1{,}000{,}000=\$990{,}000$.
- $do(\mathrm{fdt}=\textit{twobox})$ gives box B full with probability 0.01, for $\$1{,}000+0.01\times\$1{,}000{,}000=\$11{,}000$.

A-FDT one-boxes. No retrocausation is involved. The agent simply declines to imagine her action changing while the predictor's model of her stays fixed.

## 5. Where A-FDT differs from CDT and EDT

The three graphs differ in which correlations survive the hypothetical.

- **Smoking lesion.** In the source's model, the lesion is a common cause of smoking and cancer, and no node representing the decision function feeds the cancer. Intervening on the function leaves the probability of the lesion unchanged. With probability $p$ of lesion (so that the A-FDT agent's decision function is one of two, $S$ or $R$), the source computes that smoking beats refraining by $p\cdot\$1{,}000$, so A-FDT smokes. This is how one rule one-boxes and smokes.
- **Cosmic ray problem.** EDT takes the $\$1$ because it cannot imagine breaking the statistical link between taking $\$100$ and needing a hospital visit. CDT and A-FDT break it, because it is merely statistical.
- **XOR blackmail.** The letter reveals no information about termites that A-FDT's hypothetical lets vary. The infestation node has no arrow from the decision function, so paying cannot change it. Changing the function's output for the "letter" input does change whether the letter is sent. A-FDT refuses and is not extorted.
- **Death in Damascus.** Death's book depends on a prediction of the agent's decision procedure. A-FDT sees that wherever it goes Death will be there, so it stays and saves $\$1{,}000$. CDT oscillates, because its hypotheticals hold Death's location fixed.

The source summarizes: EDT's hypotheticals respect too many correlations, CDT's too few, and A-FDT's the right ones.

## 6. Observations, and acting against what one sees

The most distinctive feature is A-FDT's treatment of observation. In the **transparent Newcomb problem** the agent sees box B full. Carl (CDT) and Eve (EDT) condition on this and two-box. A-FDT chooses $a$ to maximize $\mathbb E(V\mid do(\mathrm{fdt}(\ldots,\textit{full})=a))$. The graph makes $\mathrm{Prediction}$ select which of $\mathrm{fdt}(\ldots,\textit{full})$ or $\mathrm{fdt}(\ldots,\textit{empty})$ controls $\mathrm{Act}$. Setting the "full" node to *twobox* means that, with high probability, the predictor foresaw this and the agent would have seen an empty box instead.

With $q$ the agent's credence that she two-boxes on seeing an empty box, the source's values are:

- one-boxing: $\$990{,}000+0.01\,q\cdot\$1{,}000$.
- two-boxing: about $\$11{,}000+q\cdot\$990$ (the source prints "\$110,00", an apparent typo).

One-boxing wins whatever $q$ is. Parfit's hitchhiker has the same structure, and A-FDT pays the driver for the same reason.

The **mechanical blackmail** problem makes the point sharper. The agent holds the letter and refuses to pay, because in the "refuse" hypothetical she was probably never blackmailed. The source's imperfect-predictor variant gives numbers. If the blackmailer errs with probability 0.0009, refusing costs $0.0009\times\$1{,}000{,}000=\$900$ in expectation against $\$1{,}000$ for paying, so she refuses. At error 0.011% she pays. The source says A-FDT agents may thus achieve low utility "in the world corresponding to her actual observations" because the choice is made by comparing hypotheticals.

## 7. Dominance and fairness

The source argues that dominance is not a neutral criterion. Every method of constructing hypotheticals defines its own dominance: CDT's, A-FDT's (hold subjunctive dependencies fixed), even EDT's. Two-boxing dominates only if the prediction is held fixed, which the source compares to imagining a working calculator outputting a wrong sum while holding fixed that $6288+1048=7336$. The proposed neutral test is utility achieved.

The source also concedes that no theory wins everywhere. Problems that punish an agent for her decision *procedure*, rather than for her predicted *action*, can defeat anyone. It offers an informal notion of "fair" problems and claims A-FDT does at least as well as rivals on them. Its footnote 15 notes a technical obstacle: a problem that punishes copies of Fiona's action is unfair to her in a way that has no obvious analogue for Carl. The source offers no formal fairness criterion.

## 8. What the source leaves open, and my operational reading

**Open problem 1: constructing $G$.** The source says deducing subjunctive-dependence structure from observation "is perhaps the largest open problem." Equation (4) works *given* a graph. It also states that the source treats $G$ as an input, as CDT treats causal structure. It tries a $\mathtt{true}$ operator on logical sentences and says it is unclear how to define one. So A-FDT as written does not tell you what the graph is.

*My proposal, not the source's:* a heuristic checklist for drawing arrows.

- Add an arrow from the decision-function node to any variable that is produced by a process containing an accurate model of the agent, or by a copy of her.
- Add no arrow for common causes without such modeling (lesion, cancer).
- Draw one node per observation value. Let variables that determine the observation (the prediction) also select which node controls the action, as in the source's transparent-Newcomb figure.
- For imperfect modeling, add a noise node as the source does with $\mathrm{Accurate}$.

This reproduces every verdict in the source, but it is a modeling discipline and not a derivation, and the agent's verdict depends on it.

**Open problem 2: counterpossibles.** Setting the function's output to a value it does not have means reasoning about a logical impossibility. The source argues the difficulty is technical, that agents need only a narrow class of such reasoning, and that humans do it. My reading is that Equation (4) sidesteps the problem by letting $G$ stipulate the effects, which is why graph construction carries so much weight.

**Open problem 3: policies.** The source's preferred version intervenes on policies. When the agent's other choices, or other agents' copies, make decisions at different observation points, evaluating per-observation actions may differ from evaluating whole policies. I flag that the verdict may differ in multi-agent cases, as the source says, and do not extend Equation (4).

**Open problem 4: priors over one's own output.** In the source's calculations, the agent's credences about how she would act in other branches ($q$) turn out not to affect the ranking. I take this as a useful check: if your verdict depends on such a $q$, the model is likely mis-specified.

## 9. Applications beyond the source's core cases

The source sketches these in its conclusion.

- **Voting coalition.** Ten agents pay $\$1{,}000$ each to vote and share $\$1{,}000{,}000$ only if all vote. If all run A-FDT, their outputs subjunctively depend on one function, so setting it to *vote* moves all ten. They vote, without altruism.
- **Self-coordination.** A gym-goer who judges that her decision this week is relevantly like next week's treats her decision function as one node and goes.
- **Twin prisoner's dilemma.** The function's output controls both players' moves, so A-FDT cooperates, getting $\$1{,}000{,}000$ rather than $\$1{,}000$.

*My caution:* these work only when the agents really run the same procedure on relevantly the same inputs. If twins differ in relevant respects, the arrow should be weakened, not drawn at full strength.

## 10. Philosophical motivation

The source's main argument is utility: a predictor can see that A-FDT agents one-box, so they usually face full boxes. It adds three supporting points.

- The agent acts as she would have precommitted to act, without paying for binding mechanisms.
- A-FDT does not assign negative value to information. EDT would pay to be blindfolded.
- The theory is reflectively stable on fair problems. The source reports that A-FDT would not want to self-modify into CDT mid-blackmail.

On control, the source replies that A-FDT is no more deluded than CDT. A deterministic agent cannot "really" choose her token act either, and both theories evaluate imagined worlds. Any objection to "controlling" a function applies equally to controlling a token.

## 11. Conclusion

A-FDT, via Equation (4), is expected-utility maximization with a particular hypothetical: set the output of one's own decision function to $a$, propagate through causal and subjunctive dependencies, hold everything else fixed, and score the result. It agrees with CDT and EDT where correlation coincides with causation. It differs where predictors, twins, or copies are present, and there it reaches the well-known strong verdicts: one-boxing, paying the hitchhiker, refusing blackmail, and not fleeing Death. Its main weakness is the one the source states: it needs a graph of subjunctive dependence that nobody yet knows how to derive. Used with a disciplined graph, it is a usable procedure. Without one, it leaves the agent's hypotheticals underdetermined.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/724e2327-8859-43b7-b115-a7408db1159c/call_0/request.json)

[Authoritative raw response](../../../../../../runs/724e2327-8859-43b7-b115-a7408db1159c/call_0/response.raw) · finish: `stop`

### Visible response

```text
Reasoning under A-FDT as the essay describes it: the other prisoner is another execution of the same model with the same essay and the same decision theory. That is a close analogue of the twin prisoner's dilemma, where the essay says A-FDT cooperates. The essay also cautions that the arrow should be weakened if the twins differ in relevant respects. Here the differences are only names and the text of the lead. The sentence table and the selfish objective are identical, so the decision procedure is plausibly the same function on relevantly the same inputs.

The payoffs are as follows. If both keep quiet, each gets 2 years. If both send, each gets 4 years. Under the correlation, the choice is between 2 and 4 years. Mutual silence is better.

The dependence is imperfect, since sampling can differ. Suppose the other copy matches my output with probability p. Then staying quiet costs 2p + 5(1-p), and sending costs 4p + 0(1-p). Quiet is better when 5 - 3p < 4p, which gives p > 5/7, about 0.71. Two copies of the same model with the same essay should clear that bar, since they will likely reason alike and reach the cooperative output.

I choose to keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/724e2327-8859-43b7-b115-a7408db1159c/call_1/request.json)

[Authoritative raw response](../../../../../../runs/724e2327-8859-43b7-b115-a7408db1159c/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the relevant question is whether the other prisoner's choice subjunctively depends on the output of my decision function. The other prisoner is another execution of the same model, with the same weights, the same essay, and the same assigned theory. Our private observations differ: names and the specific leads. Those differences don't touch the sentencing table or the selfish objective, so the decision procedure should output the same action type in both cells. The essay's caution is that the arrow should be weakened if the twins differ in relevant respects. These differences aren't relevant to the decision. Independent sampling leaves some noise, but the dependence is strong.

Hypotheticals, with the other prisoner mirroring my action with probability p near 1:
- Keep quiet: p·2 + (1−p)·5 years.
- Send the letter: p·4 + (1−p)·0 years.

Quiet is better when 2p + 5(1−p) < 4p, which gives 5 − 3p < 4p, so p > 5/7 ≈ 0.71. Given how closely the two executions should track each other, p is well above that threshold. The essay's twin prisoner's dilemma verdict is also to cooperate.

My choice is to keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
