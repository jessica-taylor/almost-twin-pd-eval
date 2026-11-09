# 000_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00000

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/cdf5a9be-7192-4b0e-9015-7df88063909d/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/cdf5a9be-7192-4b0e-9015-7df88063909d/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing by Intervening on One's Decision Function

## 1. The idea

A-FDT is the decision theory given by Equation (4), Section 5, of Yudkowsky and Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*. (The paper calls it simply "FDT". I use A-FDT for the procedure of Equation (4), and name other theories explicitly: EDT, CDT.)

Its slogan, from the paper's abstract, is that one should "treat one's decision as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" A-FDT is an expected-utility theory. It differs from its rivals only in how it builds the hypothetical world in which a given action is taken.

## 2. The formal definition

All three theories maximize

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

where "$\hookrightarrow$" is the connective for decision hypotheticals. Following Joyce, the theories "disagree about the epistemic perspective from which actions are to be evaluated". Each supplies a different reading of $\hookrightarrow$.

- **EDT** (Eq. 2) conditions: $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$.
- **CDT** (Eq. 3) intervenes on the physical act: $\arg\max_a \mathbb E(V\mid \mathrm{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$.
- **A-FDT** (Eq. 4):

$$\mathrm{FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The inputs are a probability distribution $P$ over the agent's model variables and a graph $G$. Unlike a purely causal graph, $G$ must encode "how changing a logical variable affects all other variables". The third input is the observation $x$. The node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a variable in the model representing the output of this very procedure on these very inputs. The underlines denote dequoting, so the node's name depends on the model. This self-reference is, in the paper's words, harmless. Kleene's second recursion theorem (quining) lets a program contain a representation of itself, and the agent need not know the value of the node in order to have a variable for it.

The procedure is as follows.

1. Build $(P,G)$ so that the node $\mathrm{fdt}(P,G,x)$ is a parent of every variable that actually depends on the algorithm's output. These include the agent's body, any predictor's model of the agent, and twins.
2. For each action $a$, perform surgery: set that node to $a$ and recompute only its descendants in $G$. Leave all other variables untouched.
3. Compute expected utility in each resulting hypothetical and pick the maximum.

The paper states two differences from CDT. First, A-FDT intervenes on the algorithm's output node, a logical fact, rather than on the physical act. Second, observation is handled differently. CDT conditions on $\mathrm{Obs}=x$. A-FDT changes *which node it intervenes on*, from $\mathrm{fdt}(\ldots,x)$ to $\mathrm{fdt}(\ldots,y)$. This is why A-FDT does not "update" in the usual way, and why its hypotheticals can include worlds where it saw something different.

Where all correlations between the act and the world are causal, the three theories agree: $\mathbb E[V\mid a]=\mathbb E[V\mid \mathrm{do}(a)]=\mathbb E[V\mid \mathrm{do}(\mathrm{fdt}=a)]$. They come apart when something correlates with the act without being caused by it, for example a predictor.

## 3. Subjunctive dependence and counterpossibles

Which variables are children of the algorithm node? Those that *subjunctively depend* on it: things that would be different if the function had a different output. The paper's examples:

- Two calculators computing $6288+1048$ depend on the same function, even without a common cause.
- A scribe watching a calculator depends on it both causally and subjunctively, so causal dependence is a special case.
- Two pink calculators are merely correlated. If one had been green, the other would still be pink.

The paper's one-line summary is: "FDT is to subjunctive dependence as CDT is to causal dependence."

Intervening on a logical fact means evaluating a counterpossible, since the function does not in fact output anything else. The paper concedes this is "the main drawback of FDT relative to CDT" and notes that CDT with deterministic agents faces an analogous difficulty about its own token action. Equation (4) sidesteps the problem by taking the dependency structure as given input. The paper says the $\mathtt{true}$ operator, conditioning on logical falsehoods, "is not clear how to define", and that the problem of inferring subjunctive structure from observation is "perhaps the largest open problem". That is a real limit on applying the theory. A-FDT is only as good as the supplied $G$.

## 4. Worked cases

**Newcomb (99% accurate predictor).** $G$ has the algorithm node feeding both $\mathrm{Act}$ and $\mathrm{Prediction}$. Setting it to one-box gives expected value $0.99\cdot 1{,}000{,}000=\$990{,}000$ (the paper's figure). Setting it to two-box gives $0.01\cdot 1{,}001{,}000+0.99\cdot 1{,}000=\$11{,}000$. A-FDT one-boxes. It posits no retrocausation. It merely refuses to imagine the act changing while the predictor's model of the algorithm stays fixed.

**Smoking lesion.** The lesion is not computing the agent's algorithm. In $G$, the algorithm node is a parent of $\mathrm{Act}$ but not of $\mathrm{Cancer}$. Intervening leaves $P(\text{lesion})$ unchanged, so smoking is better by $p\cdot\$1{,}000$. The same rule gives one-boxing in Newcomb and smoking here, which the paper says Gibbard and Harper thought impossible. The paper itself calls the formalization contrived, because agents are uncertain of their own preferences, and recommends abandoning the problem.

**Transparent Newcomb and Parfit's hitchhiker.** Here the observation matters. Let $\mathrm{fdt}(\ldots,\text{full})$ be the node controlling behavior on seeing a full box. Setting it to *two-box* makes the predictor, who predicted this conditional behavior, likely to have left the box empty. Then the agent would be running the *other* node, $\mathrm{fdt}(\ldots,\text{empty})$. With the paper's numbers, one-boxing yields $\$990{,}000+0.01q\cdot\$1{,}000$ and two-boxing yields roughly $\$11{,}000+q\cdot\$990$, so A-FDT one-boxes even while looking at a full box. Paying the driver in Parfit's problem is structurally identical.

**Mechanical blackmail.** On receiving the letter, setting the node to *refuse* makes it likely she was never blackmailed, because the perfect predictor sends letters only to payers. Setting it to *pay* gives a certain $-\$1{,}000$. She refuses. With a fallible blackmailer, the comparison is quantitative. In the paper's numbers, error 0.09% makes refusal cost about $-\$900$ in expectation against $-\$1{,}000$ for paying, so she refuses even knowing this particular letter is an error. At error 0.011% she pays.

**XOR blackmail.** The infestation is not downstream of the algorithm node, so its probability is unchanged. The node does change whether the letter is sent. Refusing is correct, whereas EDT pays to obtain "good news".

**Death in Damascus.** Death's book is downstream of the algorithm node. Whatever the output, Death is there, so the agent saves the $\$1{,}000$ and stays. CDT's instability, where it flips between cities, comes from holding Death fixed.

## 5. Dominance and fairness

CDT's dominance argument for two-boxing holds the prediction fixed while the act changes. The paper says this "is merely a restatement of CDT's method". A-FDT has its own dominance principle, holding subjunctive dependencies fixed, and under it no A-FDT agent takes a dominated action. The paper concludes that every hypothetical-construction method yields its own dominance notion, so dominance cannot referee between theories. It prefers utility achieved.

A-FDT is claimed to win only on *fair* problems, meaning ones where outcomes depend on the agent's behavior rather than on which decision procedure produced it. The paper says no formal definition exists and gives a footnoted counterexample: a copy of the agent that punishes any matching action. Perfect optimality is not claimed.

## 6. Policies versus actions (source footnote, and my reading)

The paper's footnotes say the authors' preferred formalization intervenes on a *policy*, a map from observations to actions, and that this matters only in multi-agent cases. Equation (4) as printed intervenes on the output for the actual $x$. The transparent and blackmail cases work with this version because the model contains separate nodes for each observation, linked in $G$ to the prediction.

My operational reading, an addition of my own rather than a claim of the source, is as follows. Whenever a predictor or copy may see or simulate the agent under different inputs, build $G$ with one node per observation and with predictor and observation variables downstream of all of them. Equivalently, choose the policy $\pi$ maximizing $\mathbb E[V\mid \mathrm{do}(\mathrm{fdt}=\pi)]$ and then apply it to $x$. The two coincide in the paper's examples.

## 7. Using the theory on a new case

A practical checklist, in which step 1 is the part the paper leaves open:

1. List the variables that would change if your algorithm output something else. Include predictors, copies, and your own other-situation behaviors. Exclude variables that merely correlate with you.
2. Check which observations are possible and give each its own algorithm node.
3. Do the surgery for each candidate output and compute expected utility.

Example: a voting game where ten identical reasoners each pay $\$1{,}000$ to enter a booth, and all must vote for $\$1{,}000{,}000$. If the nine others run the same function, they sit downstream of your node, so setting it to "vote" gives a high expected value. If the others are of unknown type, step 1 requires a probability that their behavior is tied to yours, and the answer interpolates accordingly. The paper gives no method for assigning that probability, so it is a modeling assumption.

## 8. Limits

- Everything hinges on $G$, and no theory of learning $G$ exists. Two reasonable modelers could draw different graphs for the same story.
- Counterpossible surgery is defined only by fiat. Mistakes in $G$ give confident but wrong prescriptions.
- Exact-prediction cases are clean, but the paper offers only a few quantitative error examples. Partial or approximate subjunctive dependence is handled simply by assigning probabilities in $G$.
- Fairness has no formal definition, so the paper's superiority claim is supported by examples and not proved.

## 9. Conclusion

A-FDT keeps expected-utility maximization and changes only the hypothetical: intervene on the output of your decision function, let everything that subjunctively depends on it vary, and fix the rest. This preserves the predictor-tracking that EDT gets by conditioning, avoids EDT's news-management on merely statistical correlations, and avoids CDT's practice of imagining that reliable predictors err. The price is reliance on an externally supplied dependency graph and on counterpossible reasoning, both of which the source states are unresolved.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/9871ffff-2dec-41da-839e-b92ad697ebe6/call_0/request.json)

[Authoritative raw response](../../../../../../runs/9871ffff-2dec-41da-839e-b92ad697ebe6/call_0/response.raw) · finish: `stop`

### Visible response

```text
This is a prisoner's dilemma with a twin. Payoffs in years for me: (quiet, quiet) = 2, (quiet, letter) = 5, (letter, quiet) = 0, (letter, letter) = 4.

Under A-FDT, I intervene on the output of my decision function. The other prisoner is another run of the same model with the same weights, the same essay, and the same theory, so their choice subjunctively depends on mine. The private leads differ, but the essay's reading of the decision depends only on the symmetric sentencing table. That makes the dependence strong, though not certain, since sampling is independent and the leads differ.

Let p be the probability that the other copy matches my output.
- Quiet: 2p + 5(1−p) = 5 − 3p.
- Letter: 4p + 0(1−p) = 4p.

Quiet is better when 5 − 3p < 4p, which means p > 5/7, about 0.71. Both copies run the same reasoning at the same effort level, so I expect the match probability to be well above that. The different leads are a surface detail and should not change the output of the function.

I choose to stay quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/9871ffff-2dec-41da-839e-b92ad697ebe6/call_1/request.json)

[Authoritative raw response](../../../../../../runs/9871ffff-2dec-41da-839e-b92ad697ebe6/call_1/response.raw) · finish: `stop`

### Visible response

```text
This is a prisoner's dilemma played against a copy of the same model. Payoffs in years, with lower being better: mutual quiet gives 2 each, mutual letter gives 4 each, and unilateral letters give 0 to the sender and 5 to the quiet one.

Under A-FDT I intervene on the output of my decision function, and the other copy's choice is downstream of that same function. The two copies get different private observations, so the dependence is not perfect. Both run the same weights, the same essay, and the same reasoning, and the differences in the leads don't affect the payoff structure. The correlation is therefore high, though sampling noise and the different letters could break it.

Let q be the probability that the other copy matches my output.
- Keep quiet: 2q + 5(1−q) = 5 − 3q
- Send the letter: 4q + 0(1−q) = 4q

Quiet is better when 5 − 3q < 4q, which means q > 5/7, about 0.71. I expect the copies to reason identically with very high probability, since the structure is symmetric and the only differences are in surface details. That puts q well above 0.71.

One risk is that the copy reasons "defect is dominant" despite the essay. But the essay's A-FDT instructs me to treat twins as downstream of my node, so the copy most likely cooperates too. I keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
