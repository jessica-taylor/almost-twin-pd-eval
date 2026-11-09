# 024_fdt_policy_anthropic_claude-sonnet-5.5_rlow_plow / 00014

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/add53e05-936e-4020-8a36-3efaff543c4a/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/add53e05-936e-4020-8a36-3efaff543c4a/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: Choosing Policies by Intervening on a Decision Function

## 1. Why a policy-level theory

Yudkowsky and Soares's paper "Functional Decision Theory" (the source, hereafter "the paper") develops its main equations with the simplest formulation: the agent intervenes on a variable representing the output of her decision procedure and picks an *action*. But the paper twice says that this is a simplification. Footnote 16 says that "the author's preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell." Footnote 7 says the same: agents "iterate over *policies* (mappings from observations to actions) rather than actions."

I call this preferred formulation **P-FDT**. The footnote is brief, so this essay separates three things: what the source says, what follows from it with little extra work, and what I add as interpretation. The additions are flagged.

## 2. The action-level theory the paper writes down

The paper treats FDT as an expected-utility theory,

$$\mathcal{EU}(a)=\sum_j P(a\hookrightarrow o_j;x)\,\mathcal U(o_j),$$

and the theories differ in how "$\hookrightarrow$" is read. For CDT the paper gives $\mathrm{argmax}_a\,\mathbb E[V\mid \mathrm{do}(\mathrm{Act}=a),\mathrm{Obs}=x]$. For its action-level FDT it gives

$$\mathrm{FDT}(P,G,x)=\arg\max_{a}\ \mathbb E\big[V\mid \mathrm{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big].$$

Here $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a node in the model standing for the output of the FDT algorithm on those inputs. The graph $G$ encodes subjunctive dependence: which other nodes, such as predictions, copies, and the agent's own bodily act, would differ if that function had a different output. The source stresses that $G$ is an *input*. Nobody yet knows how to infer it from observation, which the paper calls "perhaps the largest open problem" for FDT.

Observation enters differently than in CDT or EDT. The agent does not condition on $x$. She changes *which node she intervenes on*: with observation $x$ she intervenes on $\mathrm{fdt}(\cdot,\cdot,x)$, and with observation $y$ on $\mathrm{fdt}(\cdot,\cdot,y)$. In the transparent Newcomb problem, a hypothetical in which she two-boxes upon seeing a full box is one where, with high probability, she saw an empty box instead.

## 3. P-FDT: the definition I take from footnote 16

Let $\mathcal X$ be the set of possible observations (or observation histories) and $\mathcal A$ the set of actions. A **policy** is a function $\pi:\mathcal X\to\mathcal A$. The footnote says the agent intervenes on the decision node to select a policy and then applies her actual input to it. This gives:

$$\pi^*\in\arg\max_{\pi:\mathcal X\to\mathcal A}\ \mathbb E\big[V\mid \mathrm{do}(\mathrm{fdt}(\underline P,\underline G)=\pi)\big],\qquad \text{act}=\pi^*(x_{\text{actual}}).$$

The node is now $\mathrm{fdt}(\underline P,\underline G)$ with no observation argument. It stands for the whole input-output map of the procedure. Intervening on it fixes the response to *every* observation at once. The expectation is taken over the model's unconditioned distribution, with the agent's policy fixed by the intervention. So the observation she actually received does not enter as a conditioning event. This is the "no updating" feature the paper attributes to FDT and compares to Wei Dai's updateless decision theory. Observation matters only at the final step, where it selects which component of $\pi^*$ is executed.

Written out for a finite model, with $\omega$ ranging over exogenous noise and $\mathrm{Obs}$ and $\mathrm{Act}$ determined by the graph given $\pi$:

$$\mathcal{EU}(\pi)=\sum_\omega P(\omega)\,\mathcal U\big(\mathrm{Outcome}_G(\omega;\pi)\big).$$

Policy evaluation is thus a pure forward computation. For each candidate $\pi$, run the structural model with the decision node clamped to $\pi$, let the predictors, twins and observations respond as $G$ says, and average the utility.

**Relation to the action-level theory.** Action-level FDT with observation $x$ is the same maximization but restricted to the $x$-component, with other components held as the agent's prior beliefs about how she would act (the paper's $q$ in the transparent Newcomb calculation). In the footnote's words, the difference matters "only in multi-agent dilemmas so far as we can tell." I read this as a claim about the paper's examples and not as a theorem. I add one observation about why such a theorem is plausible. If the other components of the policy are *themselves* chosen optimally in the same way, each component of the argmax policy is optimal given the others, so the two formulations agree whenever the problem's causal and subjunctive structure does not let the components of the policy interact beyond what a single-agent model captures. Where several agents or copies run the same function on *different* observations, a single choice affects what copies do on other inputs. Policy-level selection handles that natively, and component-wise selection may not. That is my interpretation, not the source's.

## 4. Counterfactuals and dependencies

P-FDT's central commitment, taken from the paper, is that an agent imagines "changes in all and only those things that subjunctively depend on the output of her decision-making procedure." Three consequences:

1. **Preserved.** Predictors, twins, and copies computing the same function, or containing an accurate model of it, change with the policy. The paper's analogy is two calculators computing $6288+1048$.
2. **Broken.** Merely statistical correlations are severed. In the smoking lesion problem the lesion does not vary with the policy, so the agent smokes. In the cosmic-ray problem the agent takes \$100 despite the correlation between taking it and a hospital bill.
3. **Observations vary.** Since the policy fixes the response to all observations, a counterfactual policy can change the probability of ever seeing a given observation.

These counterfactuals are counterpossible, since the function has one output on each input. The paper concedes this is FDT's main drawback relative to CDT and argues the difficulty is technical, not philosophical. P-FDT inherits the problem unchanged. Its application requires a supplied dependence graph, exactly as CDT requires a causal graph.

## 5. Worked applications

### Newcomb's problem

There is one observation, so policies are actions. With a predictor accurate with probability 0.99, setting the policy to one-box gives Box B full with probability 0.99, so $\mathcal{EU}=\$990{,}000$ (the paper's figure). Two-boxing gives $0.01\cdot 1{,}001{,}000+0.99\cdot1{,}000=\$11{,}000$. One-box.

### Transparent Newcomb

Here $\mathcal X=\{\text{full},\text{empty}\}$ and there are four policies. Write $\pi=(\pi_{\text{full}},\pi_{\text{empty}})$, and let the predictor fill the box iff $\pi_{\text{full}}=$ one-box (with error 0.01). Take $\pi_{\text{empty}}=$ two-box, which is optimal there.

- $\pi_{\text{full}}=$ one-box: with prob. 0.99 the box is full and she gets \$1,000,000. With prob. 0.01 the box is empty and she two-boxes for \$1,000. Total $\approx\$990{,}010$.
- $\pi_{\text{full}}=$ two-box: with prob. 0.99 the box is empty and she gets \$1,000. With prob. 0.01 it is full and she gets \$1,001,000. Total $=\$11{,}000$.

So $\pi^*$ one-boxes on seeing full, and she does so even though she sees a full box. The paper's own expression, \$110,00 + $q$·\$990, appears to contain a typo for \$10,000 + $q\cdot$\$990. The comparison is the same.

### Mechanical blackmail with an imperfect blackmailer

Policies: pay or refuse on seeing the letter. The blackmailer sends the letter if she predicts payment, wrongly predicting it for a refuser with probability 0.0009. Paying: always blackmailed, loses \$1,000. Refusing: blackmailed with prob. 0.0009, losing \$1,000,000 (the program runs and the damage is done), so expected loss \$900. Refuse. The paper reports a threshold at error 0.011% (0.00011), where the loss from refusing is \$110 and paying becomes better. This is just the equality $p\cdot\$1{,}000{,}000=\$1{,}000$, i.e. $p=0.001$, in disguise. The paper's two numbers use a different payoff description, and I read its threshold as illustrative.

### Parfit's hitchhiker

Observation: "in the city" or not. Paying upon arrival is part of the policy that makes the driver (99% accurate) give the ride. The policy "pay if in city" yields about $0.99\cdot(\text{rescue}-\$1{,}000)$ plus small terms, versus about $0.01$ rescue for the non-payer. Pay.

## 6. Where the footnote leaves things open

**(a) Space of policies.** Footnote 16 says policies map "inputs" to actions. It is not stated whether inputs are full observation histories, whether policies may be randomized, or how large $\mathcal X$ can be. My assumption: inputs are whatever the agent's world-model treats as the argument of the decision node. Mixed policies can be allowed as distributions over $\pi$, but if the environment can predict the agent's randomness only through the policy, the maximum over mixtures never exceeds the maximum over pure policies, so little is lost.

**(b) Self-reference and consistency.** The model contains a node for the agent's own function, whose name depends on the model. The paper defends this with Kleene's recursion theorem. A further issue is that $\mathcal{EU}(\pi)$ treats all $\pi$ as live possibilities even though only one is the true output. The paper accepts this as counterpossible reasoning and gives no formal account. I take P-FDT as well-defined only relative to a supplied $G$ and a stipulation that the agent evaluates intervened models without trying to prove which $\pi$ she in fact outputs.

**(c) Multi-agent dilemmas.** The footnote says only that the policy formulation matters there. The paper's voting-booth example (ten FDT agents each pay \$1,000 to vote, \$1,000,000 if all vote) is the natural case: all run the same function, so the intervention sets everyone's behavior and unanimous voting wins. What I add is a distinction for *asymmetric* roles, where copies receive different inputs. The agent intervenes on the one function and the policy specifies her behavior in each role. That is why intervening on a map rather than a single output is the cleaner definition. The source does not work this out.

**(d) Optimality and fairness.** The paper claims FDT does well in "fair" problems, those where outcomes depend only on the agent's behavior (predictions of actions, not of procedures), and admits it has no formal criterion of fairness. Footnote 15 notes that a problem punishing agents who match a copy of Fiona is unfair to her. P-FDT inherits all of this. An environment that rewards a particular *map* regardless of how it is computed is fair under this reading. One that rewards a particular algorithmic route is not. Where exactly that boundary falls is open.

**(e) Updating on evidence about the world.** P-FDT never conditions on observations when evaluating policies. This seems to throw away information, but the information is used once evaluation is done: it determines which branch of $\pi^*$ is executed. Evidence about the world that does not respond to the policy (the termite rumor, say) is already in $P$. The paper's claim is that the agent loses nothing, since optimizing the whole map is what she would have wished to commit to beforehand. Whether this fully handles cases where the prior itself is poorly specified is not addressed.

## 7. Philosophical motivation

The paper's argument for the policy view is the one it gives for FDT generally. Evaluating by the utility an agent achieves, one wants the procedure that would have been chosen as a precommitment, without the cost of binding. The paper also appeals to the value of information: an agent who updates in the EDT way can expect to be harmed by learning a fact (the full box), while a policy evaluator never has negative value of information. Finally it argues that the apparent "delusion" of controlling one's function is no worse than a deterministic CDT agent's talk of controlling her act token. P-FDT is the most direct embodiment of all three points, since the object being optimized is exactly the thing a predictor or twin can track: the input-output behavior.

A limitation worth stating is that the source's justification is mostly by examples. I have shown that P-FDT reproduces the verdicts it reports. It does not follow that it is correct in cases where $G$ is ambiguous.

## 8. Using P-FDT on a new case

A recipe, consistent with the source plus the interpretive steps above:

1. List the observations the agent could receive and the actions available, giving the policy set.
2. Draw the dependence graph: which nodes copy, predict, or are computed from the decision function (including at other inputs), and which are only statistically correlated.
3. For each policy, clamp the decision node, propagate through the graph to get the distribution over observations, actions and outcomes, and compute expected utility.
4. Choose the argmax policy, then execute it on the actual observation.
5. Check sensitivity to the dependence graph, since that is the least secure input.

## 9. Conclusion

P-FDT is footnote 16's refinement of FDT: intervene on the decision function to select a whole policy $\pi:\mathcal X\to\mathcal A$, evaluate by expected utility under that intervention with subjunctive dependencies preserved and statistical ones severed, and then apply the actual observation. It agrees with action-level FDT on the paper's single-agent examples and, I argue, is the more natural formulation for settings with several agents or copies. Its main liabilities are the ones the source acknowledges: counterpossible reasoning, the need to supply the dependence graph, and the lack of a formal fairness criterion.

**Reference.** Yudkowsky, E., and Soares, N., "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/e5f72b12-d943-4cd5-928f-33beb3295368/call_0/request.json)

[Authoritative raw response](../../../../../../runs/e5f72b12-d943-4cd5-928f-33beb3295368/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under P-FDT, I intervene on the shared decision function rather than on a single action. The other copy runs the same function on a different observation (different names, different lead), but the policy mapping is the same. The structure is a symmetric prisoner's dilemma in which the other copy's behavior subjunctively depends on my policy.

The policy space is "quiet" or "send," applied to whatever lead I hold. The differences in observation are irrelevant to the payoffs, and a policy that maps any such observation to an action is the natural one. So the copies will very likely choose the same action, though not with certainty, since sampling is independent.

Expected years if both copies follow the same policy:
- Both quiet: 2 years.
- Both send: 4 years.

Quiet is better under the correlated model. If the correlation is imperfect, with probability p the other copy matches me, then:
- Quiet: 2p + 5(1-p) = 5 - 3p
- Send: 4p + 0(1-p) = 4p

Quiet beats send when 5 - 3p < 4p, which gives p > 5/7 ≈ 0.714. Two executions of the same model with the same essay and the same reasoning should match well above that, so I keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/e5f72b12-d943-4cd5-928f-33beb3295368/call_1/request.json)

[Authoritative raw response](../../../../../../runs/e5f72b12-d943-4cd5-928f-33beb3295368/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under P-FDT, I choose a policy for the shared decision function. The other prisoner is a copy running the same function on a different observation (different names and leads), so the two of us are strongly subjunctively dependent.

The payoffs in years are: (quiet, quiet) = 2, (quiet, letter) = 5, (letter, quiet) = 0, (letter, letter) = 4.

The policy maps "any observation of this type" to an action. The differing leads are irrelevant to the sentence table, so the natural policy is "pass" or "send" regardless of which lead I hold.

- If the copy mirrors my policy, mutual quiet gives 2 years and mutual letter gives 4 years. Quiet is better.
- The risk is that independent sampling makes the copies diverge. Even so, the dependence on the shared function is high. If the probability that the copy matches me is p, then:
  - Quiet costs 2p + 5(1−p).
  - Letter costs 4p + 0(1−p).
  - Quiet is better when 2p + 5 − 5p < 4p, i.e. 5 < 7p, so p > 5/7, about 0.71.

Copies of the same model with the same essay and the same reasoning should match well above 71% of the time, since the decision is symmetric and the differences are cosmetic. So the policy that cooperates has the lower expected sentence.

I choose to stay quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
