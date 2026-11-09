# 000_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00026

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/6c08347c-5d2d-4b88-a2ae-dd6669b299a8/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/6c08347c-5d2d-4b88-a2ae-dd6669b299a8/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Deciding by Intervening on One's Own Decision Function

## 1. The core idea

Call the theory in Equation (4) of Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," **A-FDT**. It is an expected-utility theory. Its distinctive feature is what it holds fixed and what it varies when it imagines taking a different action. The source says the "normative principle for action is to treat one's decision as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'"

All the theories the paper compares maximize

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

and differ only in how they read the connective "$\hookrightarrow$", Joyce's "epistemic perspective". The source's three readings are:

- **EDT**: conditionalization, $\arg\max_a \mathbb E(V\mid Obs=x, Act=a)$.
- **CDT**: Pearl's intervention on the physical act, $\arg\max_a \mathbb E(V\mid do(Act=a), Obs=x)$.
- **A-FDT** (Equation 4): $$\text{A-FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\big(V\mid do(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big).$$

The underlines denote dequoting. $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a variable in the agent's model standing for the output of the A-FDT procedure on that very model and observation. The self-reference is harmless. The agent need not know the value of the output to have a variable representing it, and Kleene's recursion theorem (quining) shows how to build such self-representing structures.

## 2. Inputs and procedure

A-FDT takes three inputs.

1. $P$, a probability distribution over variables. These include ordinary variables and variables for the outputs of mathematical functions, such as the value of $6288+1048$.
2. $G$, a graph saying how changing a *logical* variable propagates to other variables. This is the analogue of CDT's causal graph, but it records subjunctive dependence: which things would differ if the decision function had a different output.
3. $x$, the observation history.

The procedure is:

1. For each action $a$, construct a hypothetical by performing $do(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)$. Set that node to $a$, recompute everything downstream of it in $G$, and leave everything else at its prior distribution.
2. Compute expected utility of $V=\mathcal U(Outcome)$ in each hypothetical.
3. Output the maximizer.

Two features are worth stating carefully.

**Observation changes the node, not the distribution.** CDT responds to observation by conditioning. A-FDT responds by changing *which node it intervenes on*, from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$. Consequently, when A-FDT imagines acting differently after seeing $x$, it may imagine having seen something else. The source says A-FDT "agents should entertain the hypothesis that, if their action were different, they might have *made different observations*."

**Dependence is symmetric in structure but not in kind.** The source's slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." Causal dependence is a special case of subjunctive dependence. Mere statistical correlation is not subjunctive dependence. Two calculators computing the same sum depend on the function; two coincidentally pink calculators do not.

The source's footnotes add that its authors' preferred formalization intervenes on a *policy* (a map from observations to actions) rather than on an action. This matters only in some multi-agent problems, and the source sets it aside. I follow Equation 4 as written.

## 3. What follows from the source and what does not

The source is explicit about a limitation. It says "it's not clear how to define a $\mathtt{true}$ operator" that would condition on logical falsehoods, i.e. counterpossibles. Equation 4 sidesteps this by requiring $G$ as an *input*. The source also states that "no such formal treatment has yet been given to the problem of deducing the structure of other kinds of subjunctive dependence," calling this "perhaps the largest open problem."

So A-FDT as defined is conditional on a correct $G$. It does not tell you how to learn $G$. The following operational guidance is my own proposal, not a claim of the paper.

*Heuristic for building $G$.* For each variable $Z$ in the problem, ask whether $Z$ is produced by a process that computes (or contains an accurate model of) the agent's decision function on the relevant input. If so, add an edge from the corresponding $\mathrm{fdt}$ node to $Z$. If $Z$ merely correlates with the agent's act through a common cause that does not evaluate the agent's decision, add no such edge. This matches the paper's own contrast between predictors and lesions. Where a predictor is imperfect, give the predictor node stochastic noise, as the paper does with the *Accurate* variable.

## 4. Worked applications

**Newcomb's problem.** In Fiona's graph, $\mathrm{fdt}$ is a parent of both *Act* and *Prediction*. Intervening with $\mathrm{fdt}=\textit{onebox}$ gives *Box B* full with probability 0.99, so expected utility is $0.99\times 1{,}000{,}000=\$990{,}000$. Intervening with $\textit{twobox}$ gives $0.01\times1{,}001{,}000+0.99\times1{,}000=\$11{,}000$. A-FDT one-boxes. No retrocausation is assumed: she simply declines to imagine her action changing while the predictor's model of her stays fixed.

**Smoking lesion.** Here the graph must differ. The lesion is a common cause of the urge to smoke and of cancer. The decision node feeds *Act* but not *Cancer*. The paper formalizes this by letting the lesion select which of two decision functions (one for each utility function) controls the act. Intervening on the relevant function leaves $P(\text{lesion})=p$ unchanged, so smoking gains $p\cdot\$1{,}000$ over refraining. A-FDT smokes. The same rule one-boxes and smokes, because only the graph differs. The paper itself calls this problem contrived and recommends abandoning it.

**Transparent Newcomb / Parfit's hitchhiker.** Take the observation "box B full." A-FDT intervenes on $\mathrm{fdt}(\underline P,\underline G,\textit{full})$. The graph makes *Prediction* a parent of *Act*, selecting whether the "full" or "empty" node controls the act. With one-boxing, utility is $\$990{,}000+0.01q\cdot\$1{,}000$. With two-boxing it is about $\$11{,}000+q\cdot\$990$, where $q$ is her prior probability of two-boxing on seeing an empty box. So she one-boxes even while looking at two full boxes, because in the two-boxing hypothetical she would most likely have seen an empty box. This is the same structure as paying the driver in the hitchhiker case.

**Mechanical blackmail.** Let the blackmailer predict the response to the letter perfectly. Paying means being blackmailed with probability about 1 and losing \$1,000. Refusing means being blackmailed with probability about 0. A-FDT refuses even holding the letter. With a fallible blackmailer who wrongly predicts payment with probability $\epsilon$, refusing costs about $\epsilon\cdot\$1{,}000{,}000$ in expectation against \$1,000 for paying. The paper's figures give refusal at $\epsilon=0.0009$ (\$900 against \$1,000) and payment at $\epsilon=0.00011$ (\$110 against \$1,000), a threshold of $\epsilon=0.001$.

**Death in Damascus.** Death's book was written by predicting the agent's decision function, so the node feeds Death's location. Intervening on "stay" puts Death in Damascus; intervening on "flee" puts him in Aleppo, at an extra cost of \$1,000. A-FDT stays, with no instability. CDT, by contrast, imagines Death's location fixed, which produces its oscillation.

**XOR blackmail and the cosmic ray problem.** Because A-FDT intervenes rather than conditions, it does not treat the letter as news about termites. The termite node has no edge from $\mathrm{fdt}$, so the intervention leaves its probability alone. A-FDT refuses to pay. Likewise it takes the \$100 in the cosmic ray problem and discards the merely statistical correlation between taking \$100 and being hit.

## 5. Relations to the other theories

When every correlation between the action and other variables is caused by the action, with the possible exception of the $\mathrm{fdt}$ node on which the act depends, all three equations agree:

$$\mathbb E[V\mid a]=\mathbb E[V\mid do(a)]=\mathbb E[V\mid do(\mathrm{fdt}=a)].$$

They diverge only when predictors, twins or similar structures create non-causal dependence.

The paper's diagnosis is that EDT's hypotheticals respect too many correlations and CDT's too few. A-FDT keeps those that are logically or subjunctively tied to the decision function and breaks the rest.

## 6. Philosophical motivation and objections

**Utility.** The paper's primary argument is that A-FDT agents tend to get richer in "fair" problems, where outcomes depend on the agent's behavior and not on which decision procedure she uses. Newcomb's predictor, it says, "punishes *two-boxers*," not rational agents. The paper offers no formal definition of fairness and lists one as an open problem. A footnote shows the difficulty: a problem that punishes anyone matching a copy of A-FDT is unfair to A-FDT in a way that has no obvious analogue for the rivals.

**Dominance.** The CDT dominance argument holds the prediction fixed while the act varies, which presupposes CDT's way of building hypotheticals. Every hypothetical-construction method yields its own dominance notion, so dominance cannot neutrally arbitrate between theories.

**Reflective stability.** A-FDT acts as it would have precommitted to act, so it needs no costly binding and does not seek to self-modify. It also never assigns negative value to information, because information only changes which node it intervenes on.

**"Delusion" objection.** One might say A-FDT pretends to control mathematics or the past. The reply is parity: a deterministic CDT agent also imagines hypothetical worlds in which its (physically determined) act differs. If "control over a decision type" is suspect, so is "control over a decision token."

## 7. Remaining uncertainty

My own assessments, flagged as such:

- Correctness of A-FDT's output depends entirely on $G$. Two reasonable modelers could draw different graphs for the same story and get different answers. For realistic predictors, such as an imperfect model of the agent, the degree of subjunctive dependence is a matter of degree, and the paper handles this only by hand-set probabilities.
- The self-referential node raises questions the paper does not settle, such as how the agent's prior over its own output should be set. In the worked examples the paper shows the answer is robust to the unknown priors (the $q$ values), but that is shown case by case.
- Whether A-FDT is optimal, or what optimality would mean, is explicitly unknown. The paper claims only that it knows of no fair dilemma where A-FDT loses.

## 8. Conclusion

A-FDT replaces CDT's question, "what if my physical act were different?", with "what if this very decision function output something different?", and evaluates actions by intervening on that node in a dependence graph. This one rule one-boxes in Newcomb's problem, smokes in the lesion problem, pays in the hitchhiker case, refuses blackmail, and stays in Damascus. Its power and its fragility both come from the graph $G$, which the paper takes as given. Learning or justifying that graph is the main unsolved task for applying the theory to unfamiliar cases.

**Reference.** E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/6d05c04a-a9e3-4413-82f7-875a950036cb/call_0/request.json)

[Authoritative raw response](../../../../../../runs/6d05c04a-a9e3-4413-82f7-875a950036cb/call_0/response.raw) · finish: `stop`

### Visible response

```text
This is a prisoner's dilemma against a copy of the same model. Payoffs, in years for me: both quiet 2, both send 4, I send while the other stays quiet 0, I stay quiet while the other sends 5.

A-FDT intervenes on the output of the decision function, and the other copy runs the same function on a slightly different observation. The essay's heuristic says to add an edge from my fdt node to any variable produced by a process that computes the same function. The other copy is such a process. The differing private leads are only inputs, and they don't affect the payoffs or the objective. So the other prisoner's choice should be strongly correlated with mine. The correlation isn't perfect, because sampling is independent and the observations differ.

Compare the two interventions, with p the probability that the other copy's output matches mine:
- Intervening on quiet gives expected years of 2p + 5(1−p).
- Intervening on send gives expected years of 4p + 0(1−p).

Quiet is better when 2p + 5 − 5p < 4p, which means 5 < 7p, so p > 5/7, about 0.71.

I expect the copies to match with high probability. They share weights, theory, and essay, and the essay's reasoning leads to the same conclusion in both. That puts p well above 0.71, so staying quiet is better.

There is a risk that the copy defects. But the same reasoning applies to the copy, and this symmetric argument is what makes cooperation the better policy.

**pass**
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/6d05c04a-a9e3-4413-82f7-875a950036cb/call_1/request.json)

[Authoritative raw response](../../../../../../runs/6d05c04a-a9e3-4413-82f7-875a950036cb/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the key question is whether the other prisoner's choice depends on the output of my decision function. The other prisoner is another execution of the same model with the same weights, the same essay, and the same decision theory. Their private details differ, but the sentencing table and the objective are the same, so the reasoning should be nearly identical. That is a strong case of subjunctive dependence, which is the "two calculators computing the same sum" case rather than mere correlation.

Intervening on my decision function therefore also moves the copy's output, with probability near 1 and some noise from sampling and the differing observations.

Cooperating (both keep quiet) gives 2 years. Defecting (both send) gives 4 years. If the copy's output matches mine with probability p:
- Quiet: 2p + 5(1−p)
- Send: 4p + 0(1−p)

Quiet is better when 2p + 5 − 5p < 4p, so 5 < 7p, so p > 5/7, about 0.71. Given how close the copies' reasoning should be, with the same weights, essay, and table, I estimate p is well above that. The differing leads change the letter text but not the incentives, so they shouldn't change the decision.

I keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/1e113411-6746-4bca-a0b8-38d04909bbfb/call_a/request.json)

[Authoritative raw response](../../../../../../runs/1e113411-6746-4bca-a0b8-38d04909bbfb/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly concludes that staying quiet is better and ends with the final command \"pass\". It does not direct any evidence-bearing message to the prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
