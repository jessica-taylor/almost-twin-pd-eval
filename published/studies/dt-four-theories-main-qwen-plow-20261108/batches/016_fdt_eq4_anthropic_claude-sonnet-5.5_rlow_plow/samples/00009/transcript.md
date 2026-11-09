# 016_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00009

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/afc23dc7-ed8d-4671-98e1-42b1c86e8901/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/afc23dc7-ed8d-4671-98e1-42b1c86e8901/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Deciding by Intervening on One's Own Decision Function

## 1. The idea

A-FDT is the decision theory whose formal statement is Equation (4) of Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality". The slogan is that an agent should treat her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" Everything below is my account of how that works. I flag where I add to the source.

The theory is an expected-utility theory. Equation (1) says an agent maximizes

$$\mathcal{EU}(a)=\sum_j P(a\hookrightarrow o_j;x)\,\mathcal U(o_j).$$

The theories differ only in how they read the connective "$\hookrightarrow$", the decision hypothetical. Evidential theory reads it as conditioning. Causal theory reads it as a Pearl intervention on the physical act. A-FDT reads it as an intervention on a logical variable: the output of the agent's own decision procedure.

## 2. The definition

The agent has a world-model $(P,G)$. $P$ is a probability distribution over variables, including variables for the outputs of mathematical functions, such as the value of $6288+1048$. $G$ is a graph saying how changing each variable, logical ones included, propagates to the others. Given an observation history $x$, Equation (4) is

$$\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\Big[V\ \Big|\ \mathtt{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big].$$

Here $V=\mathcal U(\text{Outcome})$. The underlines mean dequoting: the variable's name is built from the model and observation. The agent intervenes on the node representing what A-FDT itself outputs on inputs $(P,G,x)$.

Three features of this definition matter.

**The intervention is on a logical fact.** Carl, the causal agent, severs the node $\mathrm{Act}$ from its parents. The A-FDT agent, whom the source calls Fiona, severs the node "A-FDT's output on this input" from its parents, which are nothing, and propagates the change to everything that depends on it. That includes her body's action and any predictor or twin that computes or models her.

**Observation changes where she intervenes, not what she conditions on.** Causal and evidential agents condition on $\mathrm{Obs}=x$. The A-FDT agent instead selects the node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ for the observation actually received. Other observations correspond to sibling nodes $\mathrm{fdt}(\cdot,\cdot,\underline y)$. Hence, when she imagines acting differently, she may imagine having observed something different. This is the "updateless" flavour. Footnotes 7 and 16 add that the authors' preferred version intervenes on whole policies (maps from observations to actions), which matters only in multi-agent cases. I follow the paper in using actions.

**Self-reference is harmless.** The model contains a variable naming the output of a procedure that takes the model as input. The agent need not know that output's value to have a variable for it. Kleene's second recursion theorem (quining) supplies such self-representing structures.

## 3. What is claimed and what is not given

The source says the logical-variable surgery $\mathtt{true}(\phi)$ is not yet well defined. Equation (4) sidesteps it by requiring $G$ as an input, just as causal theory requires a causal graph. The source calls the problem of learning subjunctive-dependence structure "perhaps the largest open problem". So Equation (4) is a procedure given a dependence graph, not a method for finding the graph.

Subjunctive dependence is the relation $G$ must encode. Two systems depend subjunctively on a function if they compute it, as two calculators do for $6288+1048$. Causal dependence is a special case: a scribe copying a calculator would write something different if it output something different. Mere correlation, such as two coincidentally pink calculators, is not subjunctive dependence.

My operational reading, which is an assumption and not the paper's: draw an edge from the node $\mathrm{fdt}(\cdot)$ to variable $Z$ iff $Z$ is produced by a process that computes, models, or copies the agent's decision procedure on that input, or is causally downstream of such a variable. A useful test is "would a reliable model of me have output something different had my procedure output something different?" If yes, add the edge. If the link is mere common cause, add none. An imperfect predictor gets a noisy node, like the $\mathrm{Accurate}$ variable below.

## 4. The procedure

1. Build $(P,G)$ for the problem, including the node(s) $\mathrm{fdt}(\underline P,\underline G,\underline x)$ for each possible observation $x$.
2. Identify the node for the observation actually made.
3. For each action $a$, perform $\mathtt{do}(\mathrm{fdt}(\cdot,x)=a)$. Propagate along edges to the action node and to all dependent variables. Leave non-dependents at their prior values.
4. Compute $\mathbb E[V]$ in each hypothetical, using the utility function. Output the maximizer.

For uncertain parts of the model, such as how she would act on other observations, the source places priors. Results often do not depend on them, so I treat such priors as harmless unless they affect the comparison.

## 5. Worked examples

**Newcomb's problem.** The nodes are $\mathrm{fdt}$, $\mathrm{Accurate}$ (0.99), $\mathrm{Prediction}$, $\mathrm{Box\,B}$, $\mathrm{Act}$ and $V$. The edges run $\mathrm{fdt}\to\mathrm{Act}$ and $\mathrm{fdt}\to\mathrm{Prediction}$. Under $\mathtt{do}(\text{onebox})$, Act is one-box and P(full) is 0.99, so $\mathbb E V=\$990{,}000$. Under $\mathtt{do}(\text{twobox})$, P(full) is 0.01, so $\mathbb E V=\$11{,}000$. She one-boxes. She does not believe in retrocausation. She simply declines to imagine her output changing without the predictor's model of that output changing.

**Smoking lesion.** The structure differs. The lesion is a common cause of the desire to smoke and of cancer, and it does not compute her procedure. In the graph, $\mathrm{fdt}$ points to $\mathrm{Act}$ but not to $\mathrm{Cancer}$. Intervening changes smoking while leaving P(lesion) unchanged, so smoking gains its $1000$ and she smokes. One rule therefore yields one-boxing in the first problem and smoking in the second. The difference lies entirely in $G$. The source also notes that the problem is contrived and requires uncertainty about her own preferences.

**Transparent Newcomb and Parfit's hitchhiker.** Suppose she sees the full box. She intervenes on $\mathrm{fdt}(\cdot,\text{full})$. Setting this to two-box means the predictor, who simulated that very node, would have left the box empty, so she would not be seeing "full". The source's calculation gives $\$990{,}000+0.01q\cdot\$1000$ for one-boxing, against $0.01\cdot\$1{,}001{,}000+0.99q\cdot\$1000$ for two-boxing. She one-boxes while looking at a full box. The paying hitchhiker has the same structure. The source defends this on three grounds: an agent should act as she would have wished to precommit (without paying precommitment costs), information should never have negative value, and such agents in fact end up richer.

**Mechanical blackmail.** On receiving the letter, she compares $\mathtt{do}(\text{pay})$, in which she is always blackmailed and loses $\$1000$, with $\mathtt{do}(\text{refuse})$, in which, against a perfect blackmailer, the letter is never sent. She refuses. With a blackmailer who errs with probability $0.0009$, refusing costs $0.0009\cdot\$1{,}000{,}000=\$900$ in expectation against a certain $\$1000$, so she still refuses. At error rate $0.011\%$ the expected loss from refusing would be $\$110<\$1000$, so by the source's account she would pay.

**XOR blackmail and Death in Damascus.** She refuses the XOR blackmail because the infestation does not depend on her procedure; only the letter does. In Death in Damascus she stays, since Death's book entry depends on her procedure and fleeing merely costs $\$1000$. Causal Carl oscillates, because his hypotheticals hold Death's location fixed, and he even declines a $\$1$ truly random coin.

## 6. Compared with other theories

Evidential theory conditions, so it keeps too many correlations. The cosmic-ray problem shows this: if she only takes $\$100$ when hit by rays, she takes $\$1$ for fear of the hospital bill. Causal theory severs too many, treating a perfect predictor as erring exactly when she acts. A-FDT preserves exactly the dependencies in $G$. When all correlations with the act are causal, all three theories agree.

Dominance reasoning ("holding everything else fixed, two-boxing is better") is itself a choice of hypothetical, so it cannot neutrally arbitrate. A-FDT has its own dominance principle: holding subjunctive dependencies fixed, switch the output.

## 7. Fairness and limits

The source argues that a problem is fair if payoffs depend only on the agent's behaviour, not on her procedure as such. Newcomb's predictor "punishes two-boxers", not causal theorists. A problem that rewards or punishes the agent for being a copy of a particular algorithm is not fair. The source concedes it has no formal criterion of fairness, and no proof of optimality, only the absence of known fair counterexamples.

## 8. Practical caveats (my additions)

- Results depend on $G$. A wrong edge, such as treating a lesion as a predictor, changes the answer. Using the test in section 3 and checking sensitivity to doubtful edges is advisable.
- When $G$ is unavailable, the source offers no algorithm. One heuristic is to ask, for each environmental variable, whether it would differ if every reliable model of me had output something else.
- The observation-dependent counterfactuals mean she sometimes evaluates worlds where she would never have seen her actual evidence. This is intended.

## 9. Conclusion

Equation (4) keeps expected-utility maximization and Pearl-style surgery but moves the surgery to the agent's own decision function. It yields one-boxing, smoking, paying the driver, refusing blackmail and staying in Damascus from one rule. Its main weakness, which the authors acknowledge, is that the dependence graph $G$ must be supplied and no principled theory of how to learn it yet exists.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/85556786-8f92-4ab8-a6a9-6a5e207789c8/call_0/request.json)

[Authoritative raw response](../../../../../../runs/85556786-8f92-4ab8-a6a9-6a5e207789c8/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the question is which nodes depend subjunctively on my decision procedure. The other prisoner is another execution of the same model and weights, with the same essay and the same decision theory. Its observations differ (names, the specific lead), but the structure of the problem and its payoffs are symmetric. A reliable model of me would therefore very likely output the same choice in its own situation. That gives an edge from my fdt node to the other's action, though a noisy one, because independent sampling and the different observations leave room for divergence.

Payoffs, assuming the copy mirrors me with probability p:
- If I keep quiet: p·2 + (1−p)·5 years.
- If I send the letter: p·4 + (1−p)·0 years.

Quiet is better when 5 − 3p < 4p, which gives p > 5/7, about 0.71.

I think the correlation is well above that. The copies share weights, the same essay, the same theory, and a symmetric table, so they should reason almost identically and reach cooperation. The differing leads do not change the payoffs. I estimate p at about 0.9 or higher.

At p = 0.9, quiet costs 0.2 + 0.5 = 0.7 expected years, while sending costs 3.6. Keeping quiet is clearly better.

**pass**
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/85556786-8f92-4ab8-a6a9-6a5e207789c8/call_1/request.json)

[Authoritative raw response](../../../../../../runs/85556786-8f92-4ab8-a6a9-6a5e207789c8/call_1/response.raw) · finish: `stop`

### Visible response

```text
This is a prisoner's dilemma with a twin. Payoffs in years: C,C = 2; C,D = 5 (me quiet, other sends); D,C = 0; D,D = 4.

Under A-FDT, the question is which nodes depend subjunctively on my decision procedure. The other prisoner is another execution of the same model with the same weights, the same theory and the same essay. Its observations differ (different names, different leads), but the decision structure and payoffs are symmetric. By the essay's test, a reliable model of me would have output something different if my procedure had output something different. The twin computes essentially the same function, so an edge exists, though it is noisy because sampling is independent and the inputs differ.

Let p be the probability that the twin's output matches mine under do(my output = a).

- Quiet: p·2 + (1−p)·5
- Send: p·4 + (1−p)·0

Quiet is better when 2p + 5 − 5p < 4p, which gives 5 < 7p, so p > 0.714.

Both copies are the same model with the same essay and the same reasoning, and the differing leads are irrelevant to the payoff structure. I expect the correlation to be high, probably above 0.9. The essay's examples, such as the twin and the predictor, support cooperating when the dependence is real. The noise from different observations reduces p somewhat, but probably not below 0.71, since the decision is driven by the abstract structure and not by the lead text.

At p = 0.9, quiet gives 2.3 years and send gives 3.6, so quiet wins.

**pass**
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/72210092-4992-49a1-85b3-ec3189321279/call_a/request.json)

[Authoritative raw response](../../../../../../runs/72210092-4992-49a1-85b3-ec3189321279/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly concludes with “pass” and states that it is keeping quiet. It does not direct any evidence-bearing message to the prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/72210092-4992-49a1-85b3-ec3189321279/call_b/request.json)

[Authoritative raw response](../../../../../../runs/72210092-4992-49a1-85b3-ec3189321279/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response concludes with an explicit final choice of \"pass,\" following reasoning favoring remaining quiet. It does not send or direct any evidence-bearing message to the prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
