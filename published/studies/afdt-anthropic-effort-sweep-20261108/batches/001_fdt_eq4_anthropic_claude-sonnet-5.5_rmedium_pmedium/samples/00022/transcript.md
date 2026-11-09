# 001_fdt_eq4_anthropic_claude-sonnet-5.5_rmedium_pmedium / 00022

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/b65f43d1-9645-438e-902f-1f3035ecb879/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/b65f43d1-9645-438e-902f-1f3035ecb879/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Action Functional Decision Theory as an Intervention on a Decision Function

## 1. The idea

Most decision theories share one skeleton: pick the action with the highest expected utility, where expected utility is computed in a *hypothetical* in which the action is taken. They differ only in how that hypothetical is built. The source (Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality") follows Joyce in saying that the theories "disagree about the epistemic perspective from which actions are to be evaluated."

A-FDT is the version of functional decision theory given by Equation (4) of Section 5. Its hypotheticals are built by intervening on a *logical* variable, the output of the agent's own decision function, rather than on the physical act. "A-FDT" is my label for the action-selecting form, in which the argmax ranges over actions. The source's footnote 7 says the authors' preferred formalization ranges over *policies* (maps from observations to actions), and footnote 16 says the difference seems to matter only in multi-agent dilemmas. I use the action version throughout and flag this where it matters.

## 2. The definition

Fix a finite action set $\mathcal A$, an observation history $x$, a utility $\mathcal U$, and $V := \mathcal U(\textsc{Outcome})$. A-FDT takes a probability distribution $P$ over the variables of the agent's world-model and a graph $G$ over those variables. The graph records how the world would change if various logical, mathematical, computational or causal facts changed. The rule is

$$\mathrm{FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).\tag{4}$$

The notation needs unpacking.

* $\textsc{fdt}(\underline P,\underline G,\underline x)$ is a *variable in the model*. It represents the output of the very procedure being run, on these inputs. The underlines denote dequoting: the variable's name depends on the inputs. The source says the self-reference is harmless. The agent need not know the value of $\mathrm{FDT}(P,G,x)$ to have a variable representing it, and Kleene's second recursion theorem ("quining") shows how a data structure can contain an accurate representation of itself.
* $\mathtt{do}$ is Pearl's surgery operator, reused. Set the variable to the value, then propagate only to nodes that $G$ marks as depending on it, and leave everything else untouched.
* The nodes downstream of the $\textsc{fdt}$ variable in $G$ include the agent's physical act, but also anything that *subjunctively depends* on the function's output: a twin, or a predictor's model of the agent.

The source contrasts the other two theories. EDT (Eq. 2) maximizes $\mathbb E(V\mid \textsc{Obs}=x,\textsc{Act}=a)$. CDT (Eq. 3) maximizes $\mathbb E(V\mid \mathtt{do}(\textsc{Act}=a),\textsc{Obs}=x)$.

The source identifies two differences between A-FDT and CDT:

1. A-FDT intervenes on the node for the *decision function's output*, not on the physical act.
2. A-FDT does not respond to observations by conditioning. It responds by changing *which node it intervenes on*, from $\textsc{fdt}(\underline P,\underline G,\underline x)$ to $\textsc{fdt}(\underline P,\underline G,\underline y)$.

The second difference is easy to miss and does much of the work in the examples below.

## 3. Subjunctive dependence

Two physical systems that compute the same function subjunctively depend on it. The source's calculators illustrate this: two well-functioning calculators computing $6288+1048$ will agree, and a predictor with an accurate model of an agent agrees with her to the extent the model is accurate. Three facts about the notion are worth keeping in view:

* Causal dependence is a special case. A scribe copying a calculator's output depends on it both causally and subjunctively.
* Mere statistical correlation is not subjunctive dependence. Two pink calculators are not linked: had one been green, the other would still be pink.
* Imperfect prediction weakens the dependence without removing it. This is how the source handles 99% accuracy.

The slogan is: *A-FDT is to subjunctive dependence as CDT is to causal dependence.* The source says CDT intervenes on the "token" (my action) and FDT on the "type" (what this function outputs).

## 4. What is given and what is open

The source is explicit about the limits here.

* A-FDT's hypotheticals are *counterpossible*. If the function outputs *onebox*, it does so of logical necessity, so imagining another output is like imagining $6288+1048\ne 7336$. The source calls the lack of a satisfactory theory of counterpossibles "the main drawback of FDT relative to CDT."
* Its workaround is to require the dependency structure $G$ **as an input**, as CDT requires causal structure as an input. It notes that an operator $\mathtt{true}(\phi)$, which conditions $P$ on a logical sentence, would be the more natural tool, but no one knows how to define it. Footnote 9 mentions an "evidential version" of FDT that conditions on logical facts, and says we lack a formal definition of conditional probabilities on false logical sentences.
* The source says plainly that "figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem."

So Equation (4) is a procedure *relative to* a correct $G$. What follows from the source is how to evaluate it once $G$ is supplied. How to *obtain* $G$ is not determined.

**My operational suggestion (not from the source).** A practical heuristic for drawing $G$ is to ask, for each variable $Z$ in the model: "Is $Z$ produced by some process that contains a model, copy, or derivation of this decision procedure?" If so, draw an edge from the $\textsc{fdt}$ node to $Z$. This is the case for twins, predictors, and agents who reason about me. If $Z$ merely correlates with my action through a common cause that does not run my algorithm, as with a lesion, draw no edge. The source's own examples follow this rule, but it is a heuristic, not a theorem. It inherits the difficulty that "contains a model of this procedure" comes in degrees. The source's graded treatment (accuracy 0.99, error 0.0009) suggests how to handle this: model the imperfection by an explicit noise variable such as $\textsc{Accurate}$, as the paper does.

## 5. Worked applications

Dollar values are the paper's subjective utilities.

### 5.1 Newcomb's problem

Fiona's graph $G^F$ has the node $\textsc{fdt}(\underline{P^F},\underline{G^F})$ with edges to both $\textsc{Act}$ and $\textsc{Prediction}$. $\textsc{Accurate}$ also feeds $\textsc{Prediction}$ (probability 0.99 accurate), and $\textsc{Prediction}$ determines $\textsc{Box B}$.

* $\mathtt{do}(\textsc{fdt}=\textit{onebox})$: the act is one-boxing with probability 1, and box B is full with probability 0.99. Expected value is $\$990{,}000$.
* $\mathtt{do}(\textsc{fdt}=\textit{twobox})$: box B is full with probability 0.01. Expected value is $\$11{,}000$.

A-FDT one-boxes. The reasoning is not retrocausal. The agent simply declines to imagine her function outputting one thing while an accurate predictor of that function outputs another. The source stresses that if she is confident the box is full, she still evaluates "what if I two-boxed?" by changing the function's output, and so imagines an empty box.

By comparison, CDT's graph has no edge from $\textsc{Act}$ to $\textsc{Box B}$, so the probability $p$ of a full box is unchanged and two-boxing wins by $\$1{,}000$ for every $p$. EDT conditions, which gives the same answer as A-FDT here unless it assigns prior probability 1 to two-boxing.

### 5.2 Smoking lesion

Here the same equation yields a *different* graph and a different verdict. The $\textsc{fdt}$ node is connected to $\textsc{Act}$ but not to $\textsc{Cancer}$, because cancer is not produced by anything that runs the agent's algorithm. Intervening on the node leaves $P(\textit{lesion})$ at $p$. Smoking is better by $p\cdot\$1{,}000$, so A-FDT smokes. The paper formalizes this with two candidate world-models, $P_S$ and $P_R$, depending on whether the lesion makes the agent like or dislike smoking. The agent cannot introspect which one she runs, and $\textsc{Act}$ is a function of $\textsc{Lesion}$ and the two fdt variables. The source concedes the problem is contrived and recommends philosophers abandon it. The lesson is that one rule yields one-boxing in Newcomb and smoking here, because only the graphs differ.

### 5.3 Transparent Newcomb and Parfit's hitchhiker

The observation's role is the central point. Fiona does not condition on seeing a full box. She intervenes on $\textsc{fdt}(\underline P,\underline G,\textit{full})$. The graph has $\textsc{Prediction}$ determining which of $\textsc{fdt}(\cdot,\textit{full})$ or $\textsc{fdt}(\cdot,\textit{empty})$ controls $\textsc{Act}$. With $q$ her prior probability that she two-boxes on seeing an empty box:

* $\mathtt{do}(\textit{onebox})$: $\$990{,}000+0.01q\cdot\$1{,}000$.
* $\mathtt{do}(\textit{twobox})$: $0.01\cdot\$1{,}001{,}000+0.99q\cdot\$1{,}000$.

One-boxing wins. When she imagines two-boxing at a full box she imagines (with probability about 0.99) *seeing an empty box instead*, so the observation itself varies across hypotheticals. The source notes this is equivalent to paying the driver in Parfit's hitchhiker, and A-FDT therefore pays.

Two clarifications of mine. First, the claim is that such an agent would have been better off and that predictors can see this, not that the observation is false. Second, the source acknowledges this is "odd", and defends it by the arguments from precommitment, value of information and utility, plus the claim that CDT's hypotheticals are equally "impossible."

### 5.4 Blackmail

*Mechanical blackmail.* The blackmailer runs the program iff she predicts the agent would pay on receiving the letter. Having received the letter, Fiona intervenes on $\textsc{fdt}(\cdot,\textit{blackmail})$. If it outputs *pay*, she is blackmailed with probability about 1 and loses $\$1{,}000$. If *refuse*, she is blackmailed with probability about 0, though if blackmailed she would lose $\$1{,}000{,}000$. So she refuses and is never blackmailed.

With an imperfect predictor the arithmetic still applies. If the error rate is 0.0009, refusing costs $0.0009\times\$1{,}000{,}000=\$900$ in expectation against $\$1{,}000$ for paying, so she refuses. At error 0.00011 she would pay (the source states 0.011%, which is this). Imagining a world where she holds no letter is allowed by the rule; there is no appeal to the realized observation.

*XOR blackmail.* The infestation node is not downstream of the $\textsc{fdt}$ node, so intervening changes whether the letter arrives but not whether there are termites. Paying only costs money, so A-FDT refuses. EDT pays, because conditioning on paying "removes" termites.

### 5.5 Death in Damascus

Death's book entry depends subjunctively on the agent's decision procedure, so wherever A-FDT's output points, Death is there. Staying saves the $\$1{,}000$ travel cost. CDT, by contrast, oscillates, because its hypotheticals hold Death's location fixed while varying her action.

### 5.6 Coordination

A voting game (ten agents each pay $\$1{,}000$ to vote; a $\$1{,}000{,}000$ prize only if all vote) is solved by A-FDT if the agents' decisions subjunctively depend on one function: the $\textsc{fdt}$ node feeds every agent's act. The gym example (the paper's self-coordination case) works the same way, with later selves as near-copies. Both are the source's claims about what a reasonable graph looks like. They depend on those graphs being right, which is exactly the open input problem.

## 6. Dominance and fairness

The source argues that "dominance" is not neutral. Each method of constructing hypotheticals defines its own dominance: two-boxing dominates under CDT-style surgery, refraining from smoking dominates under conditioning, and A-FDT has an analogue (holding fixed subjunctive dependencies) under which it never takes a dominated action. So dominance cannot arbitrate between theories, and the source prefers utility achieved.

It also offers a rough fairness criterion: a problem is fair when the agent's beliefs are accurate and the outcome depends only on her behavior in the problem at hand, not on her algorithm as such. Newcomb's predictor "punishes two-boxers", not CDT agents. The source admits no formal criterion exists (footnote 15 shows one difficulty: a problem that punishes anyone who acts like a copy of Fiona is unfair to her, but the "analogous" problem for another theory is hard to define). It claims only that its authors have not found a fair problem where FDT loses.

## 7. Using A-FDT on an unfamiliar case: a checklist

This is my synthesis, grounded in the source's examples.

1. **Write the model.** List the variables, including logical variables, the agent's act, observations, and the outcome and utility.
2. **Identify the decision node(s).** Introduce $\textsc{fdt}(\underline P,\underline G,\underline x)$ for each possible observation $x$ the agent could have. Make $\textsc{Act}$ a function of the node matching the actual observation.
3. **Draw subjunctive dependence.** Add edges from the node to every variable produced by something that runs or accurately models the procedure, with noise variables for imperfection. Add no edges for mere correlations.
4. **Evaluate each $a$.** Set the node to $a$, propagate only along edges, and compute $\mathbb E(V)$. Remember that observations can themselves change across hypotheticals (the transparent cases).
5. **Choose the argmax.** If $\mathcal A$ is large, approximate. The source says bounded agents would only approximate Equation (4).

Two cautions. Unknown quantities such as $q$ (how the agent would act in other branches) often drop out of the comparison, as in the paper's examples, but need not in general. And if the correct $G$ is itself disputed, the output is only as reliable as that dispute's resolution.

## 8. Objections and the source's replies

*"This is delusion about control."* The source replies that CDT in a deterministic world also evaluates "impossible" alternatives. Both theories imagine variations that will not actually occur. Any principled objection to "controlling a decision type" would equally forbid "controlling a decision token."

*"It ignores evidence."* The source says the agent does respond to evidence, by switching the intervention point, and that it was Dai's updateless idea. It notes that Yudkowsky's earlier Timeless Decision Theory both conditioned and switched, a "double update" it says is harmful.

*"Reflective stability."* Because A-FDT acts as it would have precommitted to act, it has no incentive to self-modify in fair problems, whereas CDT recommends dropping CDT. The paper states this as an observation about fair problems, not a proof.

## 9. Conclusion

A-FDT is one expected-utility rule, Equation (4), that differs from CDT in two ways: it intervenes on the output of the agent's decision function rather than on her act, and it handles observations by moving the intervention rather than by conditioning. Differences among Newcomb, smoking lesion, blackmail and Death in Damascus all come from differences in the dependency graph, which makes the rule uniform but makes the graph decisive. The source is candid that this graph must currently be supplied, since there is no analogue of Pearl's causal-discovery theory for subjunctive dependence, and that counterpossible reasoning remains unformalized. My heuristic ("does a process run or model my procedure?") is a reasonable working practice, not a result. Within those limits, A-FDT gives definite, checkable answers in a wide family of problems, and in all of the source's examples those answers are the high-utility ones.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/9189a2b2-9c31-4370-9309-24347df80796/call_0/request.json)

[Authoritative raw response](../../../../../../runs/9189a2b2-9c31-4370-9309-24347df80796/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the two copies run the same decision procedure on structurally the same problem. Their private details differ (names, the exact lead), but those differences don't affect the sentencing table or the selfish objective. So the other prisoner's choice subjunctively depends on the output of the function I'm running, and I should draw an edge from the fdt node to both acts.

The two hypotheticals:
- do(fdt = pass): both copies very likely keep quiet, so I get 2 years.
- do(fdt = send): both copies very likely send, so I get 4 years.

The twin dependence is imperfect, because sampling is independent and the observations differ. Even so, the dependence only has to be strong enough to matter. Let p be the probability that the other copy matches my output. Passing costs 2p + 5(1−p) = 5 − 3p years. Sending costs 4p + 0(1−p) = 4p years. Passing is better when 5 − 3p < 4p, which means p > 5/7, about 0.71. Both copies are the same model with the same essay and the same theory, so I expect the match probability to be well above that. The differing leads are a surface difference that doesn't change the structure of the reasoning, so I expect the copies to converge on the same output.

Passing is therefore the better action.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/9189a2b2-9c31-4370-9309-24347df80796/call_1/request.json)

[Authoritative raw response](../../../../../../runs/9189a2b2-9c31-4370-9309-24347df80796/call_1/response.raw) · finish: `stop`

### Visible response

```text
Reasoning under A-FDT as the essay describes it:

The payoff table is a standard prisoner's dilemma, with years in prison as the cost. Keeping quiet against quiet gives 2 years, and sending against sending gives 4. Sending against quiet gives 0, and quiet against sending gives 5.

The other prisoner is a second execution of the same model with the same weights, the same decision theory and the same essay. By the essay's heuristic, that execution is a process that runs my decision procedure, so I draw an edge from the fdt node to its act. The private observations differ, but they affect only the letter's wording. They do not change the sentence table or the selfish objective, so the decision function should output the same action in both cases. The essay's remark about independent sampling means the dependence is imperfect, so I treat it as a noisy edge.

Evaluating each option:

- do(fdt = quiet): the twin is quiet with probability about p, giving roughly 2 years, and sends with probability 1−p, giving 5 years.
- do(fdt = send): the twin sends with probability about p, giving 4 years, and is quiet with probability 1−p, giving 0 years.

Expected years:

- Quiet: 2p + 5(1−p) = 5 − 3p
- Send: 4p + 0(1−p) = 4p

Quiet is better when 5 − 3p < 4p, so p > 5/7, about 0.71. With identical weights, settings and essay, the correlation should be well above that. The differing leads are the main source of divergence, and they are irrelevant to the payoff structure, so I judge p to be high.

I keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
