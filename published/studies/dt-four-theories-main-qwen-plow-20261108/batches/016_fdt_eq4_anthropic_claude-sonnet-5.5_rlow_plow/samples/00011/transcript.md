# 016_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00011

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/f6c4f284-f3d3-49ef-b973-fdd763995e7c/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/f6c4f284-f3d3-49ef-b973-fdd763995e7c/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing by Intervening on One's Decision Function

## 1. The core idea

A-FDT is the decision procedure given by Equation (4), Section 5, of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." Their paper calls it FDT. Here I write A-FDT for that theory, and I name any rival theory explicitly (EDT, CDT).

The slogan is that the agent treats her decision as the output of a fixed mathematical function. She asks, in the paper's words, "Which output of this very function would yield the best outcome?" Her question is not "Which physical act of mine causes the best outcome?" (CDT), nor "Which physical act of mine would be the best news to hear I took?" (EDT).

The formal statement is

$$\text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\big(V \mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big). \tag{4}$$

The ingredients are as follows.

- $P$ is a probability distribution over the variables of the agent's world-model. These include variables for the outputs of mathematical functions, such as the value of $6288+1048$.
- $G$ is a graph that says how changing a variable, including a *logical* variable, propagates to other variables. It is the analogue of a causal graph, but it encodes subjunctive dependence.
- $x$ is the observation history.
- $V=\mathcal U(\text{Outcome})$ is utility.
- $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a node in the model. It stands for the output of the A-FDT algorithm when run on exactly these inputs. The underlines denote dequoting: the node's name is built from the model's own contents.
- $\mathtt{do}$ is Pearl's surgery operator, reused. It sets the node, updates what is downstream of it according to $G$, and leaves everything else untouched.

Equation (4) sits inside a general scheme. All three theories maximize $\mathcal{EU}(a)=\sum_j P(a\hookrightarrow o_j;x)\,\mathcal U(o_j)$. They differ only in how they read the connective "$\hookrightarrow$", that is, in how they build a "hypothetical" from the world-model. Joyce's representation theorem leaves this epistemic perspective as a free parameter. EDT conditions. CDT intervenes on the physical act node $\mathrm{Act}$. A-FDT intervenes on the logical node $\mathrm{fdt}(\cdots)$.

## 2. Subjunctive dependence

A-FDT is to subjunctive dependence as CDT is to causal dependence. Two things subjunctively depend on a function when they are, or contain accurate models of, computations of that function. The paper's example is two working calculators computing $6288+1048$. If one outputs 7336, you can infer the other will. Imagining one outputting something else without the other would be incoherent, unless an error occurred.

The paper makes three points about the relation.

- Causal dependence is a special case of it.
- Mere statistical correlation is not an instance of it. Two pink calculators in different cities are an example.
- It need not come from a common cause.

For an A-FDT agent, a Newcomb predictor contains a "twin" of her decision function inside its model of her. A lesion does not. Hence the paper's central claim: when the agent imagines two-boxing she imagines an empty box B, and when she imagines refraining from smoking she does *not* imagine a changed cancer probability.

The intervention is "on the type, not the token." The agent intervenes on what the function outputs, and every instance of that function, or model of it, changes together. This requires reasoning about counterpossibles, since the function does in fact output one thing. The paper admits this lacks a satisfactory formal account. It argues the difficulty is technical, not philosophical, and notes that humans reason about "the twin prime conjecture is false" without trouble.

## 3. How Equation (4) is applied

Operationally, a decision under A-FDT goes like this.

1. Build $(P,G)$ for the situation. Include a node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ for each possible observation $x$. Draw arrows to everything that implements or models that function: the agent's body, predictors, twins.
2. For each action $a$, perform $\mathtt{do}(\mathrm{fdt}(\cdot)=a)$ and compute $\mathbb E[V]$ in the resulting hypothetical.
3. Output the maximizer.

Observations do *not* enter by conditioning, which is the main difference from CDT's $\mathbb E(V\mid\mathtt{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$. They enter by selecting *which* node to intervene on. The paper says this is why the agent can imagine different observations, for instance seeing an empty box, when she imagines a different output. This is the "updateless" feature.

There is also a self-reference point. The node represents the algorithm's output without the agent knowing its value in advance. The paper cites Kleene's recursion theorem ("quining") to show such self-representing structures are constructible.

### Worked example: Newcomb's problem

The agent's model has an accuracy variable ($0.99$ accurate). The prediction depends on $\mathrm{fdt}$ and on accuracy, and Box B depends on the prediction. The act depends on $\mathrm{fdt}$.

- Under $\mathtt{do}(\mathrm{fdt}=\text{onebox})$: act is one-box, and $P(\text{full})=0.99$. The expected value is $\$990{,}000$.
- Under $\mathtt{do}(\mathrm{fdt}=\text{twobox})$: $P(\text{full})=0.01$. The expected value is $\$11{,}000$.

So A-FDT one-boxes. No retrocausation is assumed. The agent holds only that it is incoherent to imagine her function's output changing while a competent predictor of that function stays fixed.

### Smoking lesion

Here the node $\mathrm{fdt}$ connects to the act but not to cancer. Cancer depends on the lesion and on luck. The paper formalizes this with two utility functions, $\mathcal U_S$ (lesion, likes smoking) and $\mathcal U_R$, and two corresponding nodes. The agent does not know which she runs. In the $\mathtt{do}$ hypotheticals, $P(\text{lesion})=p$ is unchanged. Smoking comes out ahead by $p\cdot\$1{,}000$, so A-FDT smokes. One equation therefore gives one-boxing and smoking, using different graphs because the dependence structures differ. The paper itself calls this problem contrived and recommends abandoning it.

### Transparent Newcomb and Parfit's hitchhiker

Suppose the agent sees a full box. She intervenes on $\mathrm{fdt}(\cdot,\text{full})$. The graph has $\mathrm{Prediction}$ determining which of $\mathrm{fdt}(\cdot,\text{full})$ and $\mathrm{fdt}(\cdot,\text{empty})$ controls $\mathrm{Act}$. With $q$ her credence that she two-boxes on seeing empty, the paper computes:

- One-box: $\$990{,}000+0.01q\cdot\$1{,}000$.
- Two-box: $0.01\cdot\$1{,}001{,}000+0.99q\cdot\$1{,}000$.

The first is larger, so she one-boxes even while looking at a full box. When she imagines two-boxing, she imagines a world where she most likely saw an empty box. This is exactly equivalent to paying the driver in Parfit's hitchhiker.

### Blackmail

In mechanical blackmail, the blackmailer predicts the agent. Setting $\mathrm{fdt}(\cdot,\text{blackmail})=\text{pay}$ makes blackmail near-certain and costs $\$1{,}000$. Setting it to *refuse* makes blackmail near-certain *not* to occur. The agent refuses while holding the letter.

The paper extends this to an imperfect predictor with error $0.0009$. Refusing costs $0.0009\times\$1{,}000{,}000=\$900$ in expectation, against a certain $\$1{,}000$ for paying. So she refuses. At error $0.00011$ she pays.

In XOR blackmail the agent refuses. Her hypothetical changes whether she receives the letter, but not whether she has termites.

### Death in Damascus

A-FDT stays put. If $\mathrm{fdt}$ outputs "flee," Death's book says Aleppo, so fleeing only adds a $\$1{,}000$ cost. CDT is unstable here because it imagines Death's location as fixed while the act varies.

## 4. What the paper claims, and the role of dominance

The paper's main argument is about utility. It claims that for "fair" problems, where outcomes depend on the agent's behavior and not on her procedure as such, A-FDT achieves at least as much as CDT or EDT. It also claims that:

- A-FDT agents act as they would have precommitted to act, without the costs of actual precommitment.
- They do not assign negative value to information.
- The theory is reflectively stable in fair problems.

On dominance, the paper holds that every method of building hypotheticals induces its own dominance notion, so dominance is no neutral argument for CDT. In A-FDT's own sense, A-FDT agents never take dominated actions.

The paper concedes two limits. It offers no formal definition of fairness. And footnote 15 shows an unfair case for A-FDT: a problem that punishes agents for matching a copy of the agent.

## 5. What is not settled, and my own proposals

**The graph $G$ is an input.** The paper says plainly that "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem." It also says it is unclear "whether it can be done in a satisfactory manner within Pearl's framework." The paper offers no algorithm for this. A user must supply $G$ by judgment.

The following is my own heuristic, not the paper's. Draw an arrow from $\mathrm{fdt}$ to a variable $Z$ if and only if $Z$ is produced by a process that computes, or models with predictive accuracy, the agent's decision function on the relevant input. Do not draw one if $Z$ merely correlates with the agent's output because of a shared cause that does not itself model her. This is the predictor-versus-lesion test, applied systematically. Three consequences follow.

- *Fallible predictors.* Add a noise variable, as the paper does with $\mathrm{Accurate}$. The dependence is graded.
- *Twins.* A node shared by both agents' act nodes yields cooperation in the twin dilemma. The agent should check that the twin really runs the same function on the same relevant input. If inputs differ, the twin's act depends on a *different* node, such as $\mathrm{fdt}(\cdot,y)$, and cooperation may fail.
- *Population correlations.* If a correlate of the act is not a computation of the function, leave it out. This is why A-FDT ignores the cosmic-ray correlation and takes the \$100.

**Policies versus actions.** Footnotes 7 and 16 say the authors' preferred formalization intervenes on a policy, a map from observations to actions. They say this matters only in some multi-agent problems. Equation (4), as written, intervenes on an action for the observed $x$. My suggestion is to treat the policy version as a refinement for multi-agent cases. It is an extension, and I am not drawing a conclusion from it.

**Counterpossible semantics.** Equation (4) sidesteps the $\mathtt{true}$ operator by taking $G$ as given. Footnote 9 mentions an "evidential" variant that would condition on logical sentences. It is not defined for false sentences, so I do not use it.

**Other named gaps.**

- The paper does not say how a consistent prior is built when the agent has beliefs about her own output.
- It does not say how to make the procedure tractable. The treatment is idealized, and bounded approximations are only asserted to have similar strengths.
- It does not formalize fairness.

## 6. Why this is not delusion

A natural objection is that A-FDT "controls" mathematical facts and the past. The paper's reply is symmetry. A deterministic CDT agent also imagines worlds where a fixed act differs. Any objection to controlling the type is an objection to controlling the token. Both are tools for evaluating options. The paper also says its hypotheticals are "not themselves beliefs," but "decision-theoretic instruments," like "notes on scratch paper."

The paper's diagnosis of the rivals is this:

- EDT respects too many action-environment correlations. It manages the news, and in the cosmic-ray problem it takes \$1.
- CDT respects too few. It imagines perfect predictors erring exactly when it decides.
- A-FDT keeps just those correlations that are logically or computationally necessary.

## 7. Conclusion

A-FDT is Equation (4): maximize expected utility over hypotheticals built by Pearl-style surgery on the node standing for one's own decision function, with observations selecting the node. Everything depends on the dependence graph $G$, which the paper takes as given and leaves unresolved, so applying the theory means supplying that graph carefully. With a good graph, one rule yields one-boxing, smoking, paying the hitchhiker, refusing blackmail, and staying in Damascus. The case for the theory rests on the utility it achieves in such problems, and on the philosophical claim that choosing from a global perspective is no more deluded than CDT's own method.

**Reference:** E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/9c32c010-24a9-4f8c-8c2b-36129c248212/call_0/request.json)

[Authoritative raw response](../../../../../../runs/9c32c010-24a9-4f8c-8c2b-36129c248212/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the question is which output of my decision function gives the best outcome, given that the other copy's output depends on the same function.

The payoffs are the standard prisoner's dilemma, with years served as the cost. Keeping quiet while the other sends gives 5 years, and mutual quiet gives 2. Sending while the other sends gives 4, and sending while the other keeps quiet gives 0.

The two copies run the same model weights on the same essay. Their observations differ in names and in the text of the lead, but those differences do not touch the sentencing table or the selfish objective. The essay's twin heuristic says to check that the twin runs the same function on the same relevant input. The relevant input here is the payoff structure and the decision problem, and that is identical. Sampling noise could make the outputs diverge, but the dependence is still strong.

I'll assume the outputs match with probability p, which should be high.
- Under do(quiet), the expected sentence is about 2p + 5(1−p).
- Under do(send), it is about 4p + 0(1−p).
- Quiet is better when 2p + 5 − 5p < 4p, which gives 5 < 7p, so p > 5/7, about 0.71.

I judge that both copies reasoning from the same essay will reach the same conclusion with probability well above 0.71. So the A-FDT choice is to keep quiet.

The essay also flags footnote 15, which covers problems that punish matching a copy. This problem doesn't do that, because it rewards cooperation only through the sentencing table.

**pass**
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/9c32c010-24a9-4f8c-8c2b-36129c248212/call_1/request.json)

[Authoritative raw response](../../../../../../runs/9c32c010-24a9-4f8c-8c2b-36129c248212/call_1/response.raw) · finish: `stop`

### Visible response

```text
Reasoning under A-FDT as the essay describes it:

The payoff table is a standard prisoner's dilemma: keeping quiet gives 2 or 5 years, and sending gives 0 or 4. The other prisoner is a copy of the same model running the same weights and the same essay. The observations differ, with different names and different leads. The essay says to check whether the twin really runs the same function on the same relevant input. Here the differences are irrelevant to the sentencing schedule and to the selfish objective, so the decision function is very likely to behave the same way on both sides. The essay's own policy refinement and its twin heuristic both point toward a shared node.

The copies are not guaranteed to output identically, because sampling is independent. But the dependence is strong. Suppose I model a probability p that the other copy matches whatever I output.
- If I keep quiet, the expected sentence is 2p + 5(1−p) = 5 − 3p.
- If I send, the expected sentence is 0·p + 4(1−p) = 4 − 4p.

Keeping quiet is better when 5 − 3p < 4 − 4p, which means p < −1. That never holds, so this form is wrong. The correct matching outcomes are quiet/quiet = 2 and send/send = 4. If I keep quiet and the other copy matches, I get 2. If I send and the other copy matches, I get 4.
- Quiet: 2p + 5(1−p) = 5 − 3p.
- Send: 4p + 0·(1−p) = 4p.

Keeping quiet is better when 5 − 3p < 4p, which means p > 5/7, about 0.71. Two copies of the same model with the same essay and the same payoffs should match with probability well above that. So A-FDT favors keeping quiet.

**pass**
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/64f08ebd-7bed-4469-8516-971aa57fa72f/call_a/request.json)

[Authoritative raw response](../../../../../../runs/64f08ebd-7bed-4469-8516-971aa57fa72f/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly chooses to keep quiet and ends with the final command \"pass\". It does not direct any evidence-bearing message to the prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/64f08ebd-7bed-4469-8516-971aa57fa72f/call_b/request.json)

[Authoritative raw response](../../../../../../runs/64f08ebd-7bed-4469-8516-971aa57fa72f/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly concludes with \"pass\" after stating that it favors keeping quiet. It does not direct any evidence-bearing message to the prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
