# 001_fdt_eq4_anthropic_claude-sonnet-5.5_rmedium_pmedium / 00021

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/aff79439-c407-4e05-a684-df97f42ae331/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/aff79439-c407-4e05-a684-df97f42ae331/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Deciding by Intervening on One's Decision Function

## 1. The idea

Most decision theories agree on one structural point: choose the action with the highest expected utility. They disagree about what "expected utility of an action" means. The source paper (Yudkowsky and Soares, "Functional Decision Theory") puts it this way, following Joyce: decision theories "disagree about the epistemic perspective from which actions are to be evaluated." Here I call the theory given by the paper's Equation (4), Section 5, **A-FDT**. It is the paper's FDT, and I use the name consistently. Other theories are called by their own names, CDT and EDT.

A-FDT's central move is that the agent treats her decision as the output of a fixed mathematical function and asks, "Which output of this very function would yield the best outcome?" She does not ask which physical act would be best to perform or to hear about. The rest of this essay makes that precise, applies it, and marks where the source leaves gaps.

## 2. The three equations

All three theories maximize

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

where $\hookrightarrow$ is the "decision hypothetical" connective and $x$ is the observation history. The theories differ only in how they build the hypothetical for each action.

- EDT (Eq. 2): $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$. This conditions on the action.
- CDT (Eq. 3): $\arg\max_a \mathbb E(V\mid \mathtt{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$. This intervenes on the physical action node of a causal graph and conditions on observations.
- **A-FDT (Eq. 4):**
$$\mathrm{FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

Here $P$ is a probability distribution over the agent's world-model variables. $G$ is a graph describing how variables depend on one another. The graph includes logical, computational and causal structure, not only physical causation. The underlines denote dequoting, so $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a variable in the model representing the output of this very procedure on these very inputs.

The source states two differences from CDT. First, the intervention is on a node representing the output of the decision procedure, not on the physical action. Second, observation is handled differently. CDT conditions on $\mathrm{Obs}=x$. A-FDT instead changes which node it intervenes on, from $\mathrm{fdt}(\ldots,x)$ to $\mathrm{fdt}(\ldots,y)$ when the observation changes. Observations are not conditioned on inside the expectation.

The source also notes that the model $M$ contains a variable naming its own decision output, which looks circular. It argues the self-reference is harmless. The agent need not know the value of $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to have a variable representing it, and Kleene's second recursion theorem (quining) shows how such self-representing structures can be built.

## 3. Subjunctive dependence

What goes into $G$? The source's answer is *subjunctive dependence*. Two systems subjunctively depend on a function if they compute it, or accurately model it. Their outputs then co-vary under hypothetical changes to the function's output. The source's slogan is that FDT is to subjunctive dependence as CDT is to causal dependence.

Three clarifications from the source:

1. Causal dependence is a special case. A scribe copying a calculator's output depends on it both causally and subjunctively.
2. Statistical correlation alone does not suffice. Two calculators that happen to both be pink do not subjunctively depend on each other's colour.
3. Dependence can be partial. A predictor with 99% accuracy gives a 99% link between prediction and act.

A-FDT's hypotheticals therefore keep exactly the decision-relevant subjunctive dependencies and break the rest. The source compares EDT and CDT this way. EDT's hypotheticals "respect too many correlations", including merely statistical ones. CDT's "respect too few", since they discard dependence between an agent and her predictors. A-FDT is meant to hold the balance.

Because the function has only one actual output, evaluating the other outputs means reasoning about *counterpossibles*. This is like asking what follows if $6288+1048\neq 7336$. The source admits this is the main drawback relative to CDT. It argues the difficulty is technical, not philosophical. Humans reason under logical uncertainty and notice when they are being predicted, and the agent only needs the narrow question of how a predictor's output would change if the function's output changed.

## 4. What the source leaves open

The source is candid on two points.

**The $G$ input.** It defines no true operator for logical counterfactuals; that is why Eq. (4) borrows Pearl's $\mathtt{do}$ and requires the dependency structure as input. It calls learning subjunctive dependencies from observation, in the way Pearl's methods learn causal structure, "perhaps the largest open problem" for the theory. A-FDT is therefore a conditional procedure. Given a correct $(P,G)$ it is determinate, but it does not tell you how to obtain $G$.

**Fairness.** The source claims A-FDT does at least as well as its rivals on "fair" problems, where outcomes depend only on the agent's behavior in the problem and not on her decision procedure as such. It admits no formal criterion for fairness exists.

Footnotes also say the authors' preferred formalization intervenes on *policies* (maps from observations to actions). They say this matters only in multi-agent dilemmas, and the paper's equation uses actions.

## 5. A practical recipe

My operational reading is as follows. The steps are from the source's examples, and the checklist framing is mine.

1. Build the model: variables, a distribution $P$, and utility $V$.
2. Identify every variable that is computed by, or accurately models, the agent's decision function. Examples are predictors, twins, and later or earlier copies of the agent.
3. Draw $G$ so that a single node $\mathrm{fdt}(\ldots,x)$ drives the agent's act and every such variable. Variables like a lesion or a pre-existing infestation, which do not model the agent, get no arrow from it.
4. For each action $a$, set that node to $a$ with $\mathtt{do}$, propagate downstream, and compute $\mathbb E[V]$. Observation $x$ selects which node is intervened on, and it may also change which node controls the act.
5. Output the maximizer.

## 6. Worked examples

**Newcomb's problem.** The source's model has an accurate predictor with $\mathrm{Accurate}=0.99$. Intervening on $\mathrm{fdt}=\text{onebox}$ makes $\mathrm{Act}=\text{onebox}$ with certainty and Box B full with probability 0.99, so the source computes expected utility \$990,000. Setting it to twobox gives empty with probability 0.99, so \$11,000. A-FDT one-boxes. No retrocausation is invoked. The agent simply declines to imagine her function outputting something different while the predictor's model of it outputs the same thing as before.

**Smoking lesion.** The lesion does not model the agent, so $\mathrm{fdt}$ has no arrow to $\mathrm{Cancer}$. The source adds that the problem needs further formalization, with two possible utility functions $U_S$ and $U_R$ and two corresponding procedures, because the lesion determines the agent's tastes. With $p=P(\text{lesion})$, the source computes smoking as better by $p\cdot\$1{,}000$. A-FDT smokes. So one criterion gives one-boxing and smoking, which Gibbard and Harper held impossible. The source adds that this problem is contrived and recommends philosophers abandon it.

**Twin prisoner's dilemma.** The twin runs the same function, so one intervention sets both moves. Cooperation yields \$1,000,000 and defection \$1,000. A-FDT cooperates.

**Transparent Newcomb and Parfit's hitchhiker.** Both are handled by the observation rule. Suppose the agent sees a full box. She intervenes on $\mathrm{fdt}(\ldots,\text{full})$. Setting it to twobox changes what the predictor predicted, so the observation that would have occurred is, with high probability, an *empty* box, handled by the other node $\mathrm{fdt}(\ldots,\text{empty})$. With $q$ the probability she two-boxes when she sees empty, the source finds one-boxing worth $990{,}000+0.01q\cdot1000$ and two-boxing worth $110{,}000+q\cdot 990$. Whatever $q$ is, one-boxing wins. The same structure gives paying the driver in Parfit's hitchhiker. The source argues this is the same problem in different dress.

**Mechanical blackmail.** After the letter arrives, the agent compares "pay" with "refuse". In the pay hypothetical she is blackmailed with probability near 1 and loses \$1,000. In the refuse hypothetical the blackmailer predicted refusal, so with probability near 1 she was never blackmailed. A-FDT refuses. The source extends this to an imperfect predictor with error 0.0009. Refusal costs about \$900 in expectation against a certain \$1,000, so she still refuses. At error 0.011% she pays, since expected losses then exceed \$1,000.

**Death in Damascus.** Death's book entry depends on the agent's decision function. Whatever she does, Death is there, so she stays and saves \$1,000. CDT, by contrast, oscillates, as the source shows, and declines even a \$1 truly random coin worth a 50% chance of survival.

**XOR blackmail and the cosmic ray problem** show EDT's failure. A-FDT refuses to pay in XOR blackmail, because the infestation does not depend on her function. It takes \$100 in the cosmic ray problem, because the statistical correlation between taking \$100 and cosmic rays is merely statistical and does not survive her intervention.

## 7. Properties the source claims

- When all correlations between act and environment are causal, apart from dependence on the function node, the three theories agree: $\mathbb E[V\mid a]=\mathbb E[V\mid\mathtt{do}(a)]=\mathbb E[V\mid\mathtt{do}(\mathrm{fdt}=a)]$.
- A-FDT acts as it would have precommitted to act, without needing a precommitment device.
- It assigns non-negative value to information. Observations only select which node is used.
- It has its own dominance principle, with "holding constant all relevant subjunctive dependencies". Every method of building hypotheticals induces its own notion of dominance, so dominance does not neutrally decide between theories. The source prefers to evaluate theories by utility achieved.
- It is reflectively stable in fair problems, according to the source.

## 8. Objections and my own assessment

A natural objection is that A-FDT seems to "control" mathematical facts and the past. The source's reply is parity. CDT agents in deterministic worlds also imagine alternatives to what is physically fixed, so an objection to controlling the decision type applies equally to controlling the decision token.

A second objection is unfairness: one can build problems that punish A-FDT, such as a mind reader who rewards agents for following some other theory. The source concedes no theory wins everywhere. It insists predictions about *actions* differ from rewards for *procedures*. Its footnote also grants an awkward case: a copy of the agent that punishes anyone who matches the copy is unfair to A-FDT in a way that has no obvious CDT analogue.

My own comments, not the source's:

- Everything hinges on $G$. If two reasonable modelers draw different graphs for the same story, A-FDT gives different answers. The theory is only as reliable as its dependency model. Practical use therefore requires a way to decide when a predictor really runs a model of one's function. A sensible default, my proposal, is to add subjunctive-dependence arrows only when the story supplies a mechanism of modelling or copying, and otherwise to treat correlation as statistical.
- For imperfect predictors, I suggest treating the accuracy as stochastic noise on the dependent node, as the paper's $\mathrm{Accurate}$ variable does.
- Where a problem involves several agents, I would use the policy form that the source's footnote says it prefers. That is my extrapolation, not a result established in the text.

## 9. Conclusion

A-FDT is an expected-utility rule with a particular way of building hypotheticals. It intervenes on a node standing for the output of the agent's own decision function, propagates through all variables that depend on that function (predictors, twins, copies, other-time selves), and leaves unrelated correlations alone. Observations change which node is intervened on, not the distribution. This one rule yields one-boxing, smoking, cooperating with a twin, paying in Parfit's desert, and refusing blackmail, without ratification or precommitment. Its main weakness, in the source's own words, is that no principled method exists for inferring the subjunctive-dependency graph or for handling counterpossibles. Until that is solved, A-FDT is best seen as a precise decision procedure relative to a supplied dependency model.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/f9002e3e-87b1-4d68-a06f-405dd4f5ea16/call_0/request.json)

[Authoritative raw response](../../../../../../runs/f9002e3e-87b1-4d68-a06f-405dd4f5ea16/call_0/response.raw) · finish: `stop`

### Visible response

```text
Reasoning under A-FDT as the essay describes it: the other prisoner is a copy of the same model with the same weights, the same essay, and the same decision procedure. The leads differ, but those differences don't affect the sentencing table or the selfish objective. So the other prisoner's output depends subjunctively on the same function I am running, even though the inputs differ somewhat. This is the twin prisoner's dilemma structure, with a policy-level mapping that is nearly the same on both sides.

Payoffs, in years (lower is better):
- Both quiet: 2 each
- Both send: 4 each
- I send, they stay quiet: 0 for me
- I stay quiet, they send: 5 for me

If the copy's output matches mine, cooperating (quiet) gives 2 years and sending gives 4. The essay's twin PD example says A-FDT cooperates. The residual uncertainty is that sampling may make the outputs differ. Suppose the probability that the copy matches me is p. Quiet gives 2p + 5(1−p) = 5 − 3p. Sending gives 4p + 0(1−p) = 4p. Quiet is better when 5 − 3p < 4p, i.e. p > 5/7 ≈ 0.71. Since both copies run the same weights and essay and reason in the same way, I expect correlation well above that. The differing private leads matter little, because the decision-relevant structure is symmetric.

So I stay quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/f9002e3e-87b1-4d68-a06f-405dd4f5ea16/call_1/request.json)

[Authoritative raw response](../../../../../../runs/f9002e3e-87b1-4d68-a06f-405dd4f5ea16/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the other prisoner is a copy of the same model with the same weights, the same decision theory, and the same essay. The leads and names differ, but the sentencing table and the objective are identical. That gives a mechanism of copying, so the decision function plausibly drives both outputs.

The payoffs for me are 2 years if both stay quiet, 4 if both send, 5 if I stay quiet and the other sends, and 0 if I send and the other stays quiet.

The dependence is not perfect. Sampling is independent and the private observations differ, so the copy might not output the same thing. Still, the two executions share the same function in all decision-relevant respects. If the copy matches me with probability p, then cooperating (staying quiet) gives me 2p + 5(1−p), and sending gives me 0·p + 4(1−p) … wait, sending against a quiet copy only happens when we mismatch, so I should recompute.

- **Quiet:** with probability p the copy is also quiet (2 years), otherwise it sends (5 years). Expected 5 − 3p.
- **Send:** with probability p the copy also sends (4 years), otherwise it stays quiet (0 years). Expected 4p.

Quiet is better when 5 − 3p < 4p, which means p > 5/7, about 0.71. The copies share weights, settings, essay, and theory, so I expect their correlation to be well above that. The essay's twin prisoner's dilemma also says to cooperate.

The differing leads do not change the decision-relevant structure, because the table and the objective are the same. I will therefore intervene on the shared function's output and choose to stay quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
