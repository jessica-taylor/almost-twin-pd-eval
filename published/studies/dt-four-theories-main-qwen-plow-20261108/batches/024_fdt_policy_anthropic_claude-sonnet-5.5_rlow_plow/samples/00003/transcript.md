# 024_fdt_policy_anthropic_claude-sonnet-5.5_rlow_plow / 00003

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/1d707e94-79ad-40d8-b2e7-b88d376dfe9f/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/1d707e94-79ad-40d8-b2e7-b88d376dfe9f/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: Choosing Policies by Intervening on a Decision Function

## 1. Orientation

The paper by Yudkowsky and Soares presents functional decision theory (FDT) mostly in an action-based form. Its footnotes say the authors' preferred formulation selects policies instead. The primary source for this essay is footnote 16:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

Footnote 7 says the same thing: "agents actually iterate over *policies* (mappings from observations to actions) rather than actions."

I call this policy-based formulation **P-FDT**. The footnote is brief, so I separate three things below: what the source says, what I infer from it, and what I add as my own proposal. Where I name the action-level theory, I call it "the paper's action-indexed FDT." I also mention CDT and EDT as the paper does.

## 2. The central definition

**Source claims.** The paper treats all its decision theories as maximizing expected utility $\sum_j P(a \hookrightarrow o_j;x)\,\mathcal U(o_j)$. They differ in how the hypothetical connective $\hookrightarrow$ is read. The action-indexed FDT is given as

$$\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\big[V\mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big].$$

The agent reacts to observation $x$ by changing which node she intervenes on, not by conditioning. Footnote 16 changes the intervention target. The node now outputs a whole policy.

**Formalization (my reconstruction).** Let $\mathcal X$ be the set of possible observations. A policy is a function $\pi:\mathcal X\to\mathcal A$. Let $\Pi=\mathcal A^{\mathcal X}$, which is finite if $\mathcal X$ is. Let $\mathrm{fdt}(\underline P,\underline G)$ be a node representing the output of the P-FDT procedure on the model alone. Its value is a policy. The model includes the dependence of the world on that node, and in particular the dependence of the observation $\mathrm{Obs}$ on the node. Then

$$\text{P-FDT}(P,G)\;:=\;\arg\max_{\pi\in\Pi}\ \mathbb E\big[V\mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G)=\pi)\big],$$

and the agent, having observed $x$, executes $\pi^*(x)$.

Three features of this definition matter.

1. **The intervention is made once, over the whole input-output map.** There is no longer a separate node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ for each $x$. The paper's transparent Newcomb graph had two such nodes, $\mathrm{fdt}(\cdot,\textit{full})$ and $\mathrm{fdt}(\cdot,\textit{empty})$, with the prediction selecting which one controls $\mathrm{Act}$. P-FDT merges them into one node whose value is the pair of responses.
2. **The agent does not condition on $x$ while evaluating.** Observation is used only at execution, as the argument to the chosen policy. This is why the paper says FDT "responds to observation by changing which node it intervenes upon" and why it describes Fiona's behaviour as not updating on the blackmail letter. In P-FDT the evaluation never depends on $x$.
3. **Expectations range over observations as well.** Under $\mathtt{do}(\pi)$, the distribution of $\mathrm{Obs}$ is whatever the model says it is when the decision function is $\pi$. In the paper's blackmail example, "changing $\mathrm{FDT}(P,G,\textit{letter})$ changes what Fiona would do if she received the letter, *and* changes the probability that she sees the letter in the first place."

Evaluating a policy therefore means computing

$$U(\pi)=\sum_{\omega} P(\omega\mid \mathtt{do}(\mathrm{fdt}=\pi))\;\mathcal U\big(\mathrm{outcome}(\omega;\pi)\big),$$

where the world $\omega$ includes the exogenous noise, the predictor's reading of $\pi$, the resulting observation, and the action $\pi(\text{observation})$.

## 3. The relevant dependencies

P-FDT keeps the paper's notion of *subjunctive dependence*. Variables that are outputs of computations implementing, or accurately modeling, the decision function move when the function's output changes. Merely correlated or causally upstream variables do not. The slogan is "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

For P-FDT the node's output is a policy, so every downstream variable can depend on any part of the policy. A predictor of "what the agent does on seeing a full box" depends on the value $\pi(\textit{full})$. A predictor who only checks the unconditional action depends on a different summary of $\pi$. Policies make this explicit because dependence is no longer confined to a single action coordinate.

The paper states that the dependence structure must be supplied: "we require that the relevant logical dependency structure be given as an input to FDT, in the same way that the relevant causal structure is given as an input to CDT." The source also says that learning this structure is "perhaps the largest open problem." P-FDT inherits that requirement unchanged. It also inherits the use of counterpossibles: the intervened value of the node typically differs from the one the agent's algorithm actually outputs.

## 4. Worked examples

I compute each example with the paper's numbers.

### 4.1 Newcomb (no observation)

Here $\mathcal X$ is a single point, so policies coincide with actions. P-FDT and the action-indexed FDT agree. The accuracy is $0.99$. Under $\mathtt{do}(\pi=\text{one-box})$ the box is full with probability $0.99$, giving $0.99\times 10^6=\$990{,}000$. Under two-boxing the box is full with probability $0.01$, giving $0.01\times 1{,}001{,}000+0.99\times 1{,}000=\$11{,}000$. P-FDT one-boxes.

### 4.2 Transparent Newcomb

Observations are $\mathcal X=\{\textit{full},\textit{empty}\}$. The four policies are written $(\pi(\textit{full}),\pi(\textit{empty}))$. The predictor fills box B iff it predicts $\pi(\textit{full})=\text{one-box}$. Let $\epsilon=0.01$ be the predictor's error rate. Write $q$ for the action taken upon seeing an empty box.

- If $\pi(\textit{full})$ = one-box, then with probability $0.99$ the box is full and she one-boxes, receiving \$1,000,000. With probability $0.01$ the box is empty, since the predictor errs. She then plays $\pi(\textit{empty})$, which earns \$0 if she one-boxes and \$1,000 if she two-boxes.
- If $\pi(\textit{full})$ = two-box, then with probability $0.01$ the box is full and she gets \$1,001,000. Otherwise it is empty and she gets \$0 or \$1,000 according to $\pi(\textit{empty})$.

The best policy is (one-box, two-box), worth $990{,}000+0.01\times 1{,}000=\$990{,}010$. The alternative (two-box, two-box) is worth $0.01\times1{,}001{,}000+0.99\times1{,}000=\$11{,}000$. The $\pi(\textit{empty})$ coordinate matters only slightly, and always favors two-boxing. This matches the paper's "correct value of $q$ is 1." Having seen a full box, the agent executes $\pi^*(\textit{full})$ = one-box. She never asks what she would gain by deviating after seeing the box.

### 4.3 Parfit's hitchhiker

This is the same structure. The policy "pay if in the city" gets the ride with probability about $0.99$. The policy "don't pay" gets the ride about 1% of the time. Paying costs \$1,000 and survival is worth \$1,000,000, so P-FDT pays.

### 4.4 Mechanical blackmail with an imperfect predictor

The source computes that with a blackmailer error rate of $0.0009$, refusing is better, and with an error rate of $0.00011$ she pays. The comparison of policies for $\pi(\textit{letter})$ is (for loss $L=\$10^6$, payment $c=\$1{,}000$, prediction error $e$ in the sense of wrongly predicting payment):

- "Pay on letter" is blackmailed always and loses $c$.
- "Refuse on letter" is blackmailed with probability $e$ and loses $eL$ in expectation, or $e\cdot L$ with $L=\$10^6$.

Refusing wins iff $e<c/L=0.001$. The paper's \$900 figure for $e=0.0009$ corresponds to this: $0.0009\times 10^6=\$900<\$1{,}000$. The comparison is made at the level of the policy, with no conditioning on the letter that she holds.

### 4.5 Where policies and actions differ

Footnote 16 says the difference "only matters in multi-agent dilemmas so far as we can tell." Here is my account of why, and where it could matter.

In single-agent problems with a single decision point, the P-FDT value of policy $\pi$ decomposes by observation. If a predictor or environment depends on $\pi$ only through the coordinate $\pi(x)$ for the actually-possible $x$, the best policy is the coordinatewise best. Then the action-indexed rule, which optimizes each coordinate by intervening on $\mathrm{fdt}(\cdot,x)$ separately, gives the same answer.

They can diverge when different coordinates interact through the world. The coordinates of one agent's policy are all outputs of one function, so they co-vary across copies and across times. Consider the policy-coupling of two agents. If a twin runs the same procedure on a different observation, choosing the coordinate $\pi(x_1)$ alone for me while the twin's behavior is governed by $\pi(x_2)$ misses the joint structure. The paper's voting and gym examples have this form: today's choice and next week's choice are two coordinates of the same function.

Here is a minimal example of my own. Two copies of an agent are given different private signals $x\in\{1,2\}$, one each, with probability $1/2$ for each assignment. They each choose $a\in\{A,B\}$ and are paid \$1 only if their actions differ. Under the policy $\pi$ "A on 1, B on 2" they always differ. Per-coordinate reasoning treats $\pi(1)$ and $\pi(2)$ as separate decisions, so each copy asks only what its own coordinate does. Choosing the full map makes the coordination explicit.

## 5. Open questions and my proposed interpretations

**1. Which policies are admissible?** The source does not say whether $\Pi$ includes all functions $\mathcal X\to\mathcal A$ or only computable or implementable ones. A natural proposal is that $\Pi$ is whatever the agent can actually run, namely maps she could compute. That keeps the decision function inside the model, but not inside $\Pi$ itself. This resembles the paper's treatment of FDT$'$, whose decision function $d\notin\mathcal F$.

**2. What is the observation space?** Since the intervention happens before any observation, the model must give a distribution over possible observations conditional on the policy. For the observation history $x$ to index the policy, it must be the full input to the decision function. I assume $x$ includes everything the agent will actually know, including memories of earlier decisions, but this is my own choice.

**3. Problem of self-reference.** The node $\mathrm{fdt}(\underline P,\underline G)$ is quined. The paper argues this is harmless, via Kleene's recursion theorem. P-FDT adds nothing new here.

**4. Tie-breaking.** Optimal policies may be non-unique. The source says nothing. A reasonable proposal is that any maximizer is acceptable, and that the agent should be indifferent only up to what the model captures. One might also prefer a fixed deterministic tie-break so that predictors can model the agent.

**5. Randomization.** The source does not discuss mixed policies. If the predictor reads only the policy, not the random draws, a mixed policy gets the average utility of the mixture, so pure policies suffice. If the environment responds to the realized random bit, randomization can matter. In the paper's Death in Damascus the agent does best without a coin, because Death predicts even pseudorandomness.

**6. Observations not generated by the policy.** If a problem's information is caused independently of the decision function, then policy evaluation weights the observations by their ordinary probabilities. This is the policy-level equivalent of "updating." P-FDT then reproduces ordinary expected utility maximization. The agent chooses $\pi^*(x)$ as the conditional best response whenever nothing correlates with $\pi$ other than the action itself. This agrees with the source's claim that all theories coincide when correlations with action are causal.

**7. Whether the equation is a "decision."** The source is explicit that the formulation of $\mathtt{do}$ on logical nodes rests on "shakier philosophical foundations" than CDT. P-FDT is exactly as shaky: it needs a graph $G$ of how a changed policy output alters the world, and the paper offers no method for deducing it.

## 6. Procedure summary

1. Build a world-model $(P,G)$ with a node $\mathrm{fdt}$ whose value is a policy, linking it to everything that computes, copies, or predicts that function.
2. Enumerate candidate policies $\pi:\mathcal X\to\mathcal A$.
3. For each, intervene $\mathrm{fdt}=\pi$, propagate through subjunctive and causal links including to the observation, and compute $U(\pi)$.
4. Select $\pi^*=\arg\max U$.
5. Observe $x$ and act $\pi^*(x)$.

## 7. Philosophical motivation

The source's argument is utility-based. The question is which agent does best. "Utility has primacy." Acting according to a utility-maximizing policy resembles what the paper calls acting "as they would have precommitted to act" without paying for precommitment. P-FDT makes this literal: the object evaluated is the thing one would precommit to. The value-of-information argument also comes out cleanly. Policy evaluation never penalizes seeing more, since the agent can ignore any observation by choosing a policy that does not depend on it.

The paper's fairness caveat applies fully. A problem is unfair if it rewards or punishes the agent for her algorithm rather than for what her policy does. Footnote 15's copy-punishing example shows that "fair" is not yet formalized. A predictor who tests only $\pi$'s input-output behavior is fair in the paper's sense.

## 8. Conclusion

P-FDT is the paper's footnote-16 formulation: intervene on the decision function's output node, where the output is a map from observations to actions, pick the policy with the greatest expected utility under that intervention, and apply it to what is actually observed. My reconstruction makes explicit that observation affects only execution, that the observation distribution itself shifts under the intervention, and that the single-node intervention captures interactions among copies of the same function. The source's own caveat, that the dependence structure and counterpossible reasoning remain unsolved, carries over unchanged. Everything beyond the equation above is my interpretation. In particular, the admissible-policy set, tie-breaking, and randomization are not settled by the source.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/3397e19b-46a2-465c-981f-b15ab5337b6c/call_0/request.json)

[Authoritative raw response](../../../../../../runs/3397e19b-46a2-465c-981f-b15ab5337b6c/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under P-FDT, I pick a policy for the whole decision function. The other prisoner is a copy of the same model running the same procedure, so our choices are subjunctively dependent even though our private observations differ. The observations differ only in names and in the text of each lead. Neither affects the sentence table or the objective, so the policy should treat them the same way.

If both copies run the same policy, only the diagonal outcomes can occur:
- Both keep quiet: 2 years each.
- Both send the letter: 4 years each.

Quiet gives 2 years and sending gives 4, so quiet is better on the diagonal.

Sampling noise and the differing observations might break the correlation. The essay's point is that the policy determines the output across copies. Still, the copies might not be perfectly correlated, so I check how much correlation is needed. Let p be the probability the other copy mirrors my action.
- Quiet: 2p + 5(1−p) = 5 − 3p.
- Send: 4p + 0(1−p) = 4p.

Quiet is better when 5 − 3p < 4p, which means p > 5/7, about 0.71. Two copies of the same model with the same essay and the same reasoning should match well above that, so I keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/3397e19b-46a2-465c-981f-b15ab5337b6c/call_1/request.json)

[Authoritative raw response](../../../../../../runs/3397e19b-46a2-465c-981f-b15ab5337b6c/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under P-FDT, I choose a policy for the whole function. The other prisoner is a copy of the same model running the same procedure, so our outputs are subjunctively dependent. The private observations differ (names and leads), but the decision structure is symmetric, so the policy should map each copy's situation to the same kind of action.

The outcomes by joint action:
- Both keep quiet: 2 years each.
- Both send: 4 years each.
- One sends and the other stays quiet: 0 years for the sender and 5 for the quiet one.

If the copies' policies are correlated, the realistic outcomes are (quiet, quiet) at 2 years or (send, send) at 4 years. Keeping quiet is better.

Independent sampling means the correlation is not perfect. Suppose the probability that the other copy matches my action is p. Quiet gives 2p + 5(1−p) = 5 − 3p. Sending gives 4p + 0(1−p) = 4p. Quiet is better when 5 − 3p < 4p, which means p > 5/7 ≈ 0.714. Two copies of the same model with the same essay and the same reasoning should match well above that, so quiet is the better policy.

The differing leads change only the text of the letter and not the sentence table, so they do not affect the policy.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
