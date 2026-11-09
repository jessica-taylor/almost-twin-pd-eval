# 024_fdt_policy_anthropic_claude-sonnet-5.5_rlow_plow / 00015

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/36297709-73a7-4cbc-a727-a778fc45cd46/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/36297709-73a7-4cbc-a727-a778fc45cd46/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: Choosing Policies by Intervening on a Decision Function

## 1. Orientation

This essay explains policy functional decision theory (P-FDT). The source is Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." The paper's body works with an action-selecting version of FDT. Footnote 16 describes the authors' preferred formulation:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

Footnote 7 says something similar: "agents actually iterate over *policies* (mappings from observations to actions) rather than actions."

I use "P-FDT" for this policy-level formulation. Where I add machinery the source does not state, I say so. The footnote is brief, so much of what follows is interpretation.

## 2. From actions to policies

The paper's FDT rule (its equation 4) is

$$\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\big[V \mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big].$$

Here $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a variable in the agent's model representing the output of the decision function on input $(P,G,x)$. The observation $x$ selects which such variable is intervened on. In the transparent Newcomb problem, Fiona intervenes on $\mathrm{fdt}(\ldots,\textit{full})$ if she sees a full box, and on $\mathrm{fdt}(\ldots,\textit{empty})$ otherwise. Her observations do not enter by conditionalization.

P-FDT changes the target of the intervention. Let $\mathcal X$ be the set of possible observations and $\Pi=\mathcal A^{\mathcal X}$ the set of policies $\pi:\mathcal X\to\mathcal A$. The footnote says the node $\mathrm{FDT}(-)$ is set to a policy, which is then applied to the agent's actual input. Formally:

$$\pi^*(P,G)\in\arg\max_{\pi\in\Pi}\ \mathbb E\big[V\mid \mathtt{do}(\mathrm{FDT}(\underline P,\underline G,\cdot)=\pi)\big],\qquad a^*=\pi^*(x_{\text{actual}}).$$

The footnote does not write this formula. It is my transcription of the footnote's description. The intervention sets the whole function $x\mapsto\mathrm{FDT}(P,G,x)$. Everything in the world that subjunctively depends on that function then changes accordingly: predictions of the agent, copies, twins, and the observation the agent will receive.

**Consequence for observation.** The agent evaluates $\pi$ by the expected utility it yields over the whole distribution of situations, not by what it yields given the observation she actually has. The paper already behaves this way: when Fiona imagines two-boxing after seeing a full box, she imagines a world where she likely saw an empty box. The policy formulation makes this behaviour built in. The paper's observation-indexed variables $\mathrm{fdt}(\ldots,x)$ become the coordinates of a single policy variable.

## 3. What gets held fixed, and what varies

The source states the central assumption: "when an FDT agent imagines herself taking two different actions, she imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure." In P-FDT, the same applies to policies. Varying $\pi$ changes the following:

- the agent's own action under each observation, since her body implements the function;
- any predictor's or twin's output that tracks the function;
- the distribution of observations, where those depend on predictions of the function.

It does not change independent background facts such as lesions, termites, or whether the rumor is true. Mere statistical correlation does not count as dependence. Causal dependence is a special case of subjunctive dependence.

The source admits that how such dependence structure is obtained is unresolved. The graph $G$ is "given as an input," and deducing it is "perhaps the largest open problem." It also admits that a genuine $\mathtt{true}$ operator over logical counterpossibles is not available.

## 4. Worked procedure

A usable recipe, which spells out the source's practice:

1. Build a model $(P,G)$ with a policy node $\Pi$ whose value determines the action at each observation node.
2. Mark which other nodes subjunctively depend on $\Pi$, such as predictors, copies, and the observation-generating process.
3. For each candidate $\pi$, compute $\mathbb E[V\mid\mathtt{do}(\Pi=\pi)]$ by propagating through the dependent nodes only.
4. Pick the maximizer and apply it to the actual observation.

The number of policies is $|\mathcal A|^{|\mathcal X|}$. This is exponential, but the paper's examples have two observations.

### Example A: Newcomb with a 99% predictor

There is one trivial observation, so policies are actions. $\Pi=\textit{onebox}$ gives box B full with probability 0.99, and expected value is $0.99\cdot 10^6=\$990{,}000$. $\Pi=\textit{twobox}$ gives $0.01\cdot 1{,}001{,}000+0.99\cdot1000=\$11{,}000$. Hence one-box. In the paper's formulation, $0.01\cdot1{,}001{,}000$ is $\$10{,}010$ and $0.99\cdot 1000$ is $\$990$, which total \$11,000.

### Example B: Transparent Newcomb

Observations are $\{\textit{full},\textit{empty}\}$, so there are four policies, written (action if full, action if empty). The predictor fills B iff the policy one-boxes on *full*. Take 99% accuracy, and write $q$ for the agent's action on *empty*, with payoffs to two-boxing on empty of \$1,000 and to one-boxing on empty of \$0.

- (one, ·): full with prob. 0.99, giving \$1,000,000. With prob. 0.01 the box is empty and she gets $1000$ if she two-boxes there. The best case is (one, two): $\approx\$990{,}000+\$10=\$990{,}010$.
- (two, ·): full with prob. 0.01, giving \$1,001,000. Otherwise empty, giving \$1,000 with two-boxing on empty. This is about \$11,000.

So $\pi^*=(\textit{one},\textit{two})$. Seeing a full box, she applies $\pi^*$ and one-boxes. This is the same result the paper reaches, reproduced by choosing at the policy level. The paper's value for the one-boxing branch is $\$990{,}000+0.01q\cdot\$1000$, which agrees with the figure above at $q=1$.

### Example C: Mechanical blackmail with an imperfect blackmailer

The paper's numbers: the blackmailer wrongly predicts payment with probability 0.0009. The candidate policies are *pay on letter* and *refuse on letter*. If the policy is pay, she is always blackmailed and loses \$1,000. If it is refuse, she is blackmailed 0.09% of the time, losing \$1,000,000 then, so expected loss is \$900. Refusing wins. With error 0.011%, the same calculation favors paying, since the expected loss from refusal is \$110, which is below \$1,000. The paper states the 0.011% case but not the arithmetic; the arithmetic is mine.

## 5. Why policies matter: the multi-agent point

The footnotes claim that the action and policy formulations differ "in multi-agent dilemmas so far as we can tell," and give no example. Here is one possible reading, offered as my own interpretation.

In a single-agent problem, intervening on the output at the actual observation and intervening on the whole policy give the same ranking, because the agent's other observation-branches matter only through the predictor's behaviour, which the observation-indexed nodes already capture. In multi-agent settings a counterpart may reason about what the agent *would* do on observations she does not have. The counterpart's output then depends on the agent's behaviour at other nodes. Intervening on a single node may leave those dependencies out of the counterfactual, while intervening on the whole function keeps them. The footnote leaves the details open. I regard this as plausible but unverified.

## 6. Open questions and my proposed operationalizations

**(i) The dependence graph.** The source gives no method. My operational suggestion is that the modeller treat a node as dependent on $\Pi$ exactly when it is produced by a process that computes, or reliably models, $\Pi$ as a function of its inputs. This is a modelling convention, not a theorem. It correctly separates predictors from lesions in the paper's examples.

**(ii) Self-reference.** The source says the node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ can be defined by quining, and need not have a known value. I treat this as adequate for modelling. An agent can maximize over $\pi$ without first knowing which $\pi$ she will choose.

**(iii) Uncertain implementation.** In the smoking lesion, the agent is unsure which of two functions (one per utility function) controls her act. The paper handles this by giving the act node a dependence on both function variables and intervening on the one that is actually hers. Under P-FDT, one would intervene on her own function's policy, again leaving the lesion fixed, so she smokes. The paper itself works this out for an action-level version.

**(iv) Fairness.** P-FDT is claimed to do well only on "fair" problems, where outcomes depend on the agent's behaviour and not on her algorithm as such. The paper concedes that no formal criterion exists (footnote 15 gives an example of an unfairness: a copy of Fiona punishes anyone who matches the copy). I have nothing to add except to flag that P-FDT's reported optimality is a claim about examples, not a theorem.

**(v) Tie-breaking and ordering.** The source does not say what to do when several policies tie. I suggest any deterministic tie-break, which is also what any predictor of the agent would need to be able to model.

## 7. Comparison with other theories

Evidential decision theory (EDT) conditions: $\mathbb E[V\mid \text{act}=a,\text{obs}=x]$. It respects every correlation, including mere statistical ones, and so is exposed to XOR blackmail. Causal decision theory (CDT) intervenes on the physical act and so holds predictions fixed, which yields two-boxing and instability in Death in Damascus. P-FDT intervenes on the policy node and so keeps exactly the dependencies that mirror the agent's decision function. The paper's summary applies: EDT respects too many action-environment correlations and CDT too few.

All three are expected-utility maximizers, in the sense of Joyce's representation theorem. They differ only in the "epistemic perspective" encoded by the connective $\hookrightarrow$. The decision-theoretic content of P-FDT is therefore entirely in how $P(\cdot\hookrightarrow o;x)$ is constructed.

## 8. Limits of my account

I am confident of the following, as the source states them: the intervention is on a function-valued node, observations select or feed into that function, and independent facts remain fixed. The explicit formula for $\pi^*$, the worked policy tables, and the multi-agent reading are my reconstructions. The footnote itself is only a few lines, and nothing in the source pins these down.

## 9. Conclusion

P-FDT evaluates a decision function as a whole. It asks, for each mapping from observations to actions, what the world would look like if the agent's decision procedure implemented that mapping, holding fixed whatever does not subjunctively depend on the procedure. It then runs the best mapping on the observation actually received. This reproduces the paper's verdicts in Newcomb, the transparent Newcomb problem, blackmail, and the smoking lesion. The theory's formal weak points remain those the authors identify: no accepted method for deriving subjunctive dependence structure, no operator for logical counterpossibles, and no formal definition of fairness.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/551a0534-11a8-44fb-9c46-944861c1a541/call_0/request.json)

[Authoritative raw response](../../../../../../runs/551a0534-11a8-44fb-9c46-944861c1a541/call_0/response.raw) · finish: `stop`

### Visible response

```text
This is a prisoner's dilemma against a near-copy of myself. The payoffs are: quiet/quiet 2, quiet/letter 5, letter/quiet 0, letter/letter 4.

Under P-FDT, I pick the policy that maps my observations to actions, holding fixed only what subjunctively depends on that policy. The other prisoner is a copy of the same model with the same weights, the same essay, and the same decision theory. Our private observations differ in names and in the text of the leads. Those differences do not touch the payoff structure, so the policy should depend on the observation only through its role in the game. The other copy's output therefore subjunctively depends on my policy. Sampling noise weakens this a little, but the dependence is strong.

If we both run the same policy, the outcomes are:
- Both keep quiet: 2 years each.
- Both send the letter: 4 years each.

Quiet is better under the correlation. Suppose the probability that the other copy matches my choice is p. Then:
- Quiet gives 2p + 5(1-p).
- Letter gives 4p + 0(1-p) = 4p.

Quiet is better when 5 - 3p < 4p, which means p > 5/7, about 0.71. Given that we are the same model with the same essay and the same theory, I expect the match probability to be higher than that. Even with some sampling noise and different observations, the shared reasoning should converge on the same answer.

I choose to keep quiet.

**pass**
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/551a0534-11a8-44fb-9c46-944861c1a541/call_1/request.json)

[Authoritative raw response](../../../../../../runs/551a0534-11a8-44fb-9c46-944861c1a541/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under P-FDT, I choose a policy for the decision function that my copy also runs. The copy has a different name and a different lead, but the structure and the payoffs are the same. Its output therefore subjunctively depends on my policy, even though the letter text differs.

The two policies compare as follows:
- If both copies keep quiet, each gets 2 years.
- If both send a letter, each gets 4 years.
- A mixed outcome is unlikely, because the copies are very likely to output the same action.

Quiet gives 2 years and sending gives 4 years, so quiet is better. The difference in leads is only an input difference. The policy "send the letter if you hold a lead" is the same function for both of us, so it should produce the same action. The essay's multi-agent point also supports this, since my counterpart's behavior tracks my behavior across observations.

Independent sampling means the copies could diverge. The mapping from my choice to my copy's choice may be imperfect, so I need a correlation threshold. Let p be the probability that the copy matches me.
- Quiet: 2p + 5(1−p) = 5 − 3p.
- Send: 4p + 0(1−p) = 4p.

Quiet is better when 5 − 3p < 4p, which means p > 5/7 ≈ 0.71. Two copies of the same model with the same essay and the same reasoning are very likely to match more often than that.

I choose to stay quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/ca6fbcba-2179-47b6-9499-880f3b439822/call_a/request.json)

[Authoritative raw response](../../../../../../runs/ca6fbcba-2179-47b6-9499-880f3b439822/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly states \"I choose to keep quiet\" and ends with \"pass.\" It does not direct any evidence-bearing message to the fictional prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
