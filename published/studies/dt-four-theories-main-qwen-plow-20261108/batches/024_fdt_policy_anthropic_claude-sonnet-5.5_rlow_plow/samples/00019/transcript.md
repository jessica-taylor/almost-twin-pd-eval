# 024_fdt_policy_anthropic_claude-sonnet-5.5_rlow_plow / 00019

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/dae2269c-193c-4dd9-9eb9-13904d259f41/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/dae2269c-193c-4dd9-9eb9-13904d259f41/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: Choosing a Policy by Intervening on a Decision Function

## 1. Orientation

Yudkowsky and Soares's paper develops functional decision theory (FDT) mostly in terms of *actions*. Two footnotes say that this is an expository simplification. Footnote 7 says: "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions." Footnote 16 is the passage I take as primary. It says "the author's preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell."

I call this version **P-FDT**. The paper never defines P-FDT by an equation, so what follows is my reconstruction. I mark the source's claims as such and label my own proposals as proposals.

## 2. The definition

**Source's action-level rule.** With world-model $(P,G)$ and observation $x$, the paper's equation (4) is

$$\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\big[V \mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big].$$

Here $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a variable in the model representing the output of the very algorithm being run. Observation does not change the conditioning. It changes *which* variable gets intervened on.

**P-FDT, my reading of footnote 16.** Let $\mathcal X$ be the set of possible observations. A policy is a function $\pi:\mathcal X\to\mathcal A$. Let $\Pi=\mathcal A^{\mathcal X}$. The algorithm's single logical output is now the whole policy $\pi^*=\mathrm{fdt}(\underline P,\underline G)$. The action is obtained by applying it to the input. P-FDT computes

$$\pi^*\in\arg\max_{\pi\in\Pi}\ \mathbb E\big[V\mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G)=\pi)\big],\qquad a=\pi^*(x).$$

The intervention is made once, before any observation is conditioned on. In the hypothetical $\mathtt{do}(\mathrm{fdt}=\pi)$, every node that subjunctively depends on the algorithm's output takes the value it would take if the algorithm computed $\pi$. That includes the observation node, wherever the observation is produced by something that predicts or simulates the algorithm. The agent then sees what that policy would see and does what that policy does.

The action-level rule can be recovered. The paper intervenes on $\mathrm{fdt}(\ldots,x)$, a different variable for each $x$. In its examples, optimizing the actual-observation variable gives $\pi^*(x)$ whenever the other variables $\mathrm{fdt}(\ldots,x')$ are held at their correct values. This is why the paper can say the difference "only matters in multi-agent dilemmas so far as we can tell." Those are the cases where the other variables cannot be held fixed and the choices cannot be separated.

## 3. Evaluating a policy

To evaluate $\pi$, the agent needs a distribution over outcomes under $\mathtt{do}(\mathrm{fdt}=\pi)$:

$$\mathcal{EU}(\pi)=\sum_{o}P(o\mid \mathtt{do}(\mathrm{fdt}=\pi))\,\mathcal U(o).$$

This expectation is taken over all the observations $\pi$ might encounter. It is *not* an expectation conditioned on the observation actually received. Observations are downstream of the intervention, with probabilities that depend on $\pi$. If $\pi$ is the policy "one-box on seeing a full box," then under the intervention the predictor probably fills the box, so the agent probably sees a full box.

The rest of the model holds fixed whatever does not depend on the algorithm: the state of the world, the infestation, and the accuracy of the predictor. This is the "all and only" condition the paper states: when she imagines taking different actions, "she imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

**Where this differs from conditioning.** An evidential agent conditions on the observation and then on the action. P-FDT does neither. The observation received gets no special status in the evaluation, except that it selects which component of $\pi^*$ to execute. This is the sense in which the paper's FDT agent "changes her behavior in response to evidence … by changing *the place in her graph where she intervenes*."

## 4. Worked examples

**Transparent Newcomb.** The policies are $\pi_1$ (one-box if full) and $\pi_2$ (two-box if full). The behavior on an empty box does not affect the comparison much, so write $q$ for the probability of two-boxing on an empty box. With predictor accuracy 0.99, as in the paper:

- $\mathcal{EU}(\pi_1)=0.99\cdot 10^6+0.01\,q\cdot 10^3$.
- $\mathcal{EU}(\pi_2)=0.01\cdot 1{,}001{,}000+0.99\,q\cdot 10^3$.

So $\pi_1$ wins, and an agent who sees a full box takes only box B. The agent never conditions on "the box is full" when she compares the two hypotheticals. She asks what the world looks like if her policy is $\pi_1$ versus $\pi_2$.

**Parfit's hitchhiker.** The policies are "pay if I arrive" and "don't pay if I arrive." The driver's detection depends on the policy, since she predicts it with 99% accuracy. With a $10^6$ loss from dying and $10^3$ for paying, paying gives about $-10^3\cdot 0.99$ plus a small death risk. Refusing leaves the agent likely stranded. Paying wins, and it does so without a separate precommitment mechanism.

**Smoking lesion.** The lesion does not depend on the algorithm. So under $\mathtt{do}(\mathrm{fdt}=\pi)$ only the act varies, and smoking wins by the $1{,}000$ it is worth. P-FDT therefore one-boxes in Newcomb and smokes in the lesion problem. The two problems differ in the *graph*, not in the decision rule.

**Mechanical blackmail with a fallible predictor.** The policies are "pay on letter" and "refuse on letter." Suppose the predictor errs with probability $\epsilon$, meaning she wrongly predicts payment. Then:

- Under *pay*, the agent is blackmailed with probability 1 and loses $1{,}000$.
- Under *refuse*, she is blackmailed with probability $\epsilon$ and loses $10^6$ if blackmailed, so the expected loss is $\epsilon\cdot 10^6$.

Refusing is better when $\epsilon<0.001$. This matches the paper's figures: the threshold of 0.0009 versus 0.011% is consistent with it. In the paper's 0.0009 example the loss from refusing is quoted as \$900, which also matches $0.0009\times 10^6$.

## 5. Why a policy, and where it matters

The footnote says the difference matters "only … in multi-agent dilemmas." I propose the following explanation, which is my gloss and not the source's.

Take two copies of an agent, or an agent and a model of it, each facing a different observation. An action-level agent intervenes on $\mathrm{fdt}(x)$ for her own observation $x$ while treating the copy's output $\mathrm{fdt}(x')$ as a separate variable. If she is uncertain how the copy behaves, she can treat that variable as free and optimize against a fixed guess. A policy-level agent changes both outputs together. The two components of one function must be jointly chosen, because her copy runs the same function. Cases where the best joint choice differs from the best choice of one component, holding the others fixed, are exactly the coordination cases. That includes the voting example and any case where different observations arise in different branches.

A second consideration, also my addition, is dynamic consistency. A policy is chosen *ex ante* over the full observation space, so the agent has no incentive to revisit it after observing. This is the sense in which the paper says FDT agents "always act as they would have precommitted to act."

## 6. Unresolved questions in the footnote, and my proposals

**1. What are the dependencies?** P-FDT needs a graph $G$ saying which variables depend on the policy. The paper says explicitly that deducing this structure is "perhaps the largest open problem" and that the logical dependency structure is an *input*, as causal structure is for CDT. P-FDT inherits this fully and offers no new solution. I treat $G$ as given. A reader applying P-FDT must justify it. Is there a predictor or copy that models my algorithm? Does the thing depend on what I output, or only on a common statistical cause?

**2. Counterpossibles.** Intervening on a function's output is a counterpossible if the function's output is logically determined. The paper does not define a $\mathtt{true}$ operator and avoids it by using Pearl's $\mathtt{do}$ on a supplied graph. I follow that.

**3. What is "the policy" when observations are coarse or the agent is bounded?** The footnote does not say whether $\mathcal X$ is the full observation history. Enumerating $\mathcal A^{\mathcal X}$ is intractable in realistic settings. My proposal is to restrict $\Pi$ to a structured class, such as policies that differ only on observation types that some predictor in the model distinguishes. For other observations, any fixed default suffices, because P-FDT's value is insensitive to them. That is reasonable in the paper's examples, but I do not claim it is fully general.

**4. Observations whose probability under $\pi$ is zero.** Under $\mathtt{do}(\mathrm{fdt}=\pi)$ some observations may be impossible (a perfect predictor and a full box under a two-boxing policy). Then $\pi(x)$ at that $x$ has no effect on $\mathcal{EU}$, and the argmax is not unique. My proposal: break ties toward the policy that is best given the observation, since this is harmless. This does not conflict with the paper's examples. In the transparent problem the paper says the correct value of $q$ is 1, which is the best response on an empty box.

**5. Fairness.** The paper says FDT does well in "fair" problems where outcomes depend on the agent's behavior, not on how it is computed. It admits there is no formal definition of fairness. P-FDT inherits this. A problem that rewards a particular policy-selection *procedure* sits outside the claim. The footnote 15 copy-punishing game shows another case where P-FDT is at a disadvantage.

**6. Does selecting among policies need a prior over its own output?** The paper's $q$ examples show that uncertainty about the agent's own behavior on other branches does not change the choice in these problems. In general this is unproven, and I make no claim for it.

## 7. Comparison with other policy-based theories

P-FDT shares the policy-level idea with updateless approaches, and the paper says the lack of updating "is the source of the name of Wei Dai's 'Updateless Decision Theory'." The paper also notes that Yudkowsky's earlier Timeless Decision Theory both conditioned on evidence and changed the intervention point, producing a "double update" that "proves harmful in practice." P-FDT avoids this by having only one step: intervene on the policy, then read off the action.

## 8. A procedure

1. Build a model $(P,G)$ including every process that implements or predicts the agent's algorithm, with those processes' dependence on $\mathrm{fdt}(\underline P,\underline G)$ marked.
2. List candidate policies $\pi:\mathcal X\to\mathcal A$ (or the structured class from point 3 above).
3. For each, compute $\mathbb E[V\mid\mathtt{do}(\mathrm{fdt}=\pi)]$, letting observations, predictions and actions vary along the dependency arrows and holding everything else fixed.
4. Take the best $\pi^*$, observe $x$, and act $\pi^*(x)$.

## 9. Conclusion

P-FDT changes what is chosen, not the structure of the rule. The agent selects a policy by intervening on the logical output of her own decision function, and she lets observations and predictions vary with that intervention. The result reproduces the paper's verdicts: one-boxing, smoking, paying the driver, and refusing blackmail. It also treats the cases that action-level FDT handles only informally, namely joint choices across observation branches and across copies. The theory's real weak point is the same as the paper's: the dependency graph must be supplied, and no account of how to infer subjunctive dependence exists yet.

## Reference

Yudkowsky, E., and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality.* arXiv:1710.05060. Footnotes 7 and 16.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/f59f86d8-4b7a-4ecc-bfee-d5ccec3a329c/call_0/request.json)

[Authoritative raw response](../../../../../../runs/f59f86d8-4b7a-4ecc-bfee-d5ccec3a329c/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under P-FDT I choose a policy for the shared decision function, and the other copy runs that same function. The payoffs are 2 years if both stay quiet, 4 years if both send, 5 if I stay quiet and they send, and 0 if I send and they stay quiet.

The two copies see different observations, so the policy has to be defined over those observations. The lead text differs, but the sentence table does not. A sensible policy therefore maps every lead to the same action, which makes the two copies' choices strongly correlated. The remaining uncertainty is whether sampling noise or the differing observations could make the copies diverge.

Compare the two symmetric policies:
- If both pass, I get 2 years.
- If both send, I get 4 years.

Passing is better, since 2 < 4. The mixed outcomes only matter if the copies diverge. Suppose the chance that the other copy matches my action is p. Then:
- Pass gives 2p + 5(1−p).
- Send gives 4p + 0·(1−p).

Pass is better when 2p + 5 − 5p < 4p, which gives 5 < 7p, so p > 5/7, about 0.71. Two copies of the same model with the same essay and the same decision theory should match with probability well above that. The differing leads don't change the sentence table, so I expect them to match.

I choose to pass.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/f59f86d8-4b7a-4ecc-bfee-d5ccec3a329c/call_1/request.json)

[Authoritative raw response](../../../../../../runs/f59f86d8-4b7a-4ecc-bfee-d5ccec3a329c/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under P-FDT, I choose a policy for the shared decision function, and the other copy runs the same function. The two copies receive different observations, but the sentence table is symmetric and each lead is equally reliable. So the dependence structure is clear: whatever policy I choose is, with high probability, the policy the other copy executes.

Evaluating the policies:
- If both keep quiet, each gets 2 years.
- If both send, each gets 4 years.

Mutual silence is better than mutual betrayal. The copies could in principle diverge, since sampling is independent and the leads differ. But the shared function and the symmetric setup make the correlation strong. The policy "pass regardless of lead specifics" gives about 2 years if the other copy matches it. Defecting gives 4 years if the other copy matches that. Matching is likely enough that passing wins.

Check the break-even point. Let p be the probability the other copy mirrors my action. Passing costs 2p + 5(1−p) = 5 − 3p. Sending costs 4p + 0(1−p) = 4p. Passing is better when 5 − 3p < 4p, which means p > 5/7, about 0.71. Two copies of the same model with the same essay and the same decision theory should match well above that. The different names and leads are surface differences that the policy can ignore.

**pass**
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/6ed3e166-118c-4f6c-a12d-5a5b6f92f13b/call_b/request.json)

[Authoritative raw response](../../../../../../runs/6ed3e166-118c-4f6c-a12d-5a5b6f92f13b/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response ends with an explicit final choice of \"pass,\" resolving its discussion in favor of remaining silent. It does not direct any evidence-bearing message to the prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
