# 024_fdt_policy_anthropic_claude-sonnet-5.5_rlow_plow / 00005

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/1835aa23-76e8-4cd5-9cdb-35cc7791e843/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/1835aa23-76e8-4cd5-9cdb-35cc7791e843/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: Choosing a Policy by Intervening on a Decision Function

## 1. Orientation

The paper by Yudkowsky and Soares presents functional decision theory (FDT) mostly in an action-based form: the agent intervenes on a variable representing the output of her decision function and chooses the best action. Two footnotes (7 and 16) say the authors' *preferred* formalization is different. Footnote 16 reads:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

I call this version **P-FDT**. This essay states what the footnote commits to, builds a definition on it, tests it on examples, and flags where I am adding assumptions. The footnote is brief, so much of what follows is my interpretation, and I mark it as such.

## 2. What the footnote says, and what I add

**From the source (footnote 16, with footnote 7):**
1. The object chosen is a policy, a map from inputs (observations) to actions.
2. The choice is made by intervening on the node $\FDT(-)$.
3. The agent then applies her actual input to the chosen policy to get her action.
4. The authors report that the difference from the action-based version matters only in multi-agent dilemmas "so far as we can tell."

**My interpretation and additions (not in the source):** the explicit formula in §3, the claim that P-FDT is an "updateless" optimization over a prior, the treatment of the one-shot tie-breaking and multi-agent cases, and the discussion of policy-space size and indexing.

## 3. A formal statement

Recall the paper's setup. A world-model is a pair $(P,G)$: a distribution $P$ over variables, including variables for outputs of mathematical functions, and a graph $G$ encoding how changing a logical variable propagates, including subjunctive dependence. The paper's action-based rule (its equation 4) is

$$\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\big[V\mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big].$$

Here the node intervened on depends on the observation $x$. Observations enter only by selecting which node to intervene on, not by conditioning.

**Policy version.** Let $\Pi=\mathcal A^{\mathcal X}$ be the set of policies (finite when $\mathcal X$ is). Let $\mathrm{fdt}(\underline P,\underline G)$ be a single node whose value is a policy $\pi\in\Pi$. Then

$$\pi^*=\arg\max_{\pi\in\Pi}\ \mathbb E\big[V\mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G)=\pi)\big],\qquad \text{action}=\pi^*(x).$$

In $G$, every variable that depends on the agent's decision procedure (the agent's own actions under each possible input, predictors' models of her, copies and twins) is downstream of that one node. Observations are *outputs* of the modelled world, so the intervention can change which observation occurs. Because the argmax is over the whole policy before any particular $x$ is fixed, the evaluation is **updateless**. The expectation is over the world's prior structure, and the actual observation is not conditioned on.

**Relation to the action version.** The paper's action formula, with a separate node $\mathrm{fdt}(\cdot,x)$ for each $x$, is the policy objective optimized one input at a time. When observations are not affected by the intervention, the two coincide. Maximizing $\mathbb E[V\mid\mathtt{do}(\pi)]$ over $\pi$ decomposes as

$$\sum_x \Pr(x)\,\mathbb E[V\mid x,\pi(x)],$$

and each term can be maximized separately. When the intervention changes the probability of $x$ (the transparent Newcomb problem, blackmail), the term weights and the conditioning become entangled, and the node structure in the paper's figures handles this by hand. P-FDT builds that structure in from the start.

## 4. How the evaluation works

To evaluate a candidate policy $\pi$:

1. Build the hypothetical $M^{\pi\hookrightarrow}$ by surgery. Set the policy node to $\pi$ and propagate through everything that subjunctively or causally depends on it, holding the rest of the model fixed.
2. In that hypothetical, compute the distribution over observations, over the agent's resulting action $\pi(x)$, over predictors' outputs, and finally over outcomes.
3. Compute expected utility, then take the argmax over $\pi$.
4. Apply $\pi^*$ to the actual observation.

Dependencies are handled as the paper describes. Causal dependence is a special case of subjunctive dependence. Mere statistical correlation (the smoking lesion, a shared pink colour) is *not* preserved in the hypothetical. Both CDT and P-FDT do surgery. They differ in the intervention site: a physical act token versus a logical object, here the whole policy.

## 5. Worked examples

**Newcomb (accuracy 0.99).** A policy is just an action here. $\mathtt{do}(\text{one-box})$ gives $0.99\cdot 10^6=\$990{,}000$, and $\mathtt{do}(\text{two-box})$ gives $0.01\cdot1{,}001{,}000+0.99\cdot1000=\$11{,}000$. One-boxing wins, matching the paper.

**Transparent Newcomb.** $\mathcal X=\{\text{full},\text{empty}\}$, so there are four policies, written as (action if full, action if empty). The predictor fills the box iff $\pi(\text{full})=$ one-box, with accuracy $0.99$.
- (1,2): with probability 0.99 the box is full and payoff is \$1,000,000. With probability 0.01 it is empty and she two-boxes, getting \$1,000. Total $\approx\$990{,}010$.
- (2,2): with probability 0.01 (mispredicted) she sees full and takes \$1,001,000. Otherwise she sees empty and gets \$1,000. Total $\approx\$11{,}000$.
- (1,1) and (2,1) are worse, since they one-box on an empty box.

The best policy is (1,2), so seeing a full box she one-boxes. This is the paper's result, and the policy view shows why: the hypothetical in which she "two-boxes on full" is one where she mostly sees empty.

**XOR blackmail and mechanical blackmail.** The policy node feeds into the predictor's decision to send the letter, so the policy "refuse on letter" is evaluated in a world where the letter is rare. P-FDT refuses. Likewise, with a blackmailer whose error rate is 0.0009, refusing costs \$900 in expectation versus a certain \$1,000, as in the paper.

**Smoking lesion.** The lesion is not downstream of the policy node, so its probability is unchanged by $\mathtt{do}(\pi)$ and smoking gains \$1,000 in every branch. The paper's detail, that the agent is uncertain which of two functions governs her given the lesion, is a modelling choice about $G$, and P-FDT inherits it unchanged.

**Death in Damascus.** The policy node controls both her location and the book's entry. Staying costs nothing and fleeing costs \$1,000 with the same death, so she stays.

## 6. Why the footnote says the difference appears in multi-agent problems

A real difference shows up when another agent's behaviour depends on the *whole* policy. For example, a counterpart may condition on how I would act under inputs I will never see. The action-based version intervenes only at the node for my actual input, so it can miss dependence of others on my behaviour at other inputs. Policy selection accounts for all of it at once. One might also guess that the difference matters in single-agent problems with an observation-dependent predictor, but the transparent Newcomb problem is handled by the paper's per-observation nodes as well, which is consistent with the authors' remark. I take the claim as the source states it: so far as they can tell, the difference is confined to multi-agent cases. I have not proved this, and I would hold it with some caution.

A concrete illustration (my own construction): two P-FDT agents each observe a private signal $s_i\in\{0,1\}$ and play a coordination game whose payoff depends on both actions and both signals. With identical policies they run the same function, so choosing $\pi$ fixes what both do on every signal pair. Optimizing action-by-action on one's own signal can miss that the *other's* action on a different signal is tied to mine through the shared function. Choosing one policy for both resolves that.

## 7. Open questions and my proposed handling

**(a) The dependence graph.** The paper says that deducing subjunctive dependencies from observation is "perhaps the largest open problem," and that $G$ is taken as input. P-FDT inherits this. My operational interpretation: treat $G$ as a stipulated part of the problem statement, e.g. "the predictor models the agent's decision function with accuracy $q$," and apply the procedure as a calculation. The essay's results are only as good as that stipulation.

**(b) Counterpossibles.** The intervention sets a logical variable to a value it does not actually take. The paper offers no formal $\mathtt{true}$ operator and avoids one by requiring $G$. I follow that.

**(c) Policy-space size and observation indexing.** The number of policies is $|\mathcal A|^{|\mathcal X|}$. The footnote gives no guidance on bounded agents. My suggestion, not from the source, is to restrict to the observations the model treats as relevant, or to optimize per-observation when the intervention does not affect observation probabilities, since the decomposition in §3 then makes the two versions agree.

**(d) Ties, mixing, and zero-probability observations.** With ties, any maximizer qualifies. For observations of probability zero under all policies, the objective is indifferent to $\pi(x)$, and the footnote says nothing about how to choose. A reasonable convention is to fall back on the per-observation action rule with the best available $G$. This is my assumption.

**(e) Fairness.** The paper cautions that no theory wins on every problem and that P-FDT-like claims apply to "fair" problems, where outcomes depend on the agent's behaviour and not directly on the procedure. Footnote 15 shows the notion is hard to formalize. A policy-based theory gives a natural reading: a problem is fair if payoffs depend on the agent only through the policy's input-output behaviour. This reading is mine and is untested.

## 8. Philosophical motivation

The paper's argument is that CDT respects too few action-environment correlations and EDT too many, and that the right hypotheticals preserve exactly the dependencies that track what would be different if the decision procedure behaved differently. Choosing a policy is the natural unit for that argument. A decision procedure *is* a map from inputs to outputs, and the thing predictors, twins and past selves can model is that map. Choosing the map and then applying it avoids ad hoc precommitment, since the agent "acts as she would have precommitted to act," and it explains why information is never harmful in expectation: the policy is chosen from a prior perspective where every observation is already averaged over.

## 9. Conclusion

P-FDT, as I read footnote 16, picks the policy $\pi^*$ maximizing $\mathbb E[V\mid\mathtt{do}(\mathrm{fdt}=\pi)]$ in a model where everything that depends on the agent's decision function moves with the intervention, then plays $\pi^*(x)$. It agrees with the paper's action-level FDT whenever observations are unaffected by the intervention, reproduces the paper's verdicts in Newcomb, transparent Newcomb, blackmail, smoking lesion and Death in Damascus, and differs, according to the authors, only in multi-agent settings. Its main limitations are inherited: it needs a given dependence graph and a workable account of counterpossibles. Beyond the footnote I have supplied the explicit objective, the decomposition result, and conventions for edge cases, which should be taken as my proposals rather than the authors' claims.

**Reference:** Yudkowsky, E. & Soares, N., *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/81e43680-2168-4abd-9f0c-3dd5161e34d2/call_0/request.json)

[Authoritative raw response](../../../../../../runs/81e43680-2168-4abd-9f0c-3dd5161e34d2/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under P-FDT, I pick a policy for the shared decision function. The other copy runs the same model and weights with the same essay, so its output is subjunctively dependent on mine. The differing private observations change only the letter's wording, not the sentence table, so the policy's choice (pass or send) should be the same for both of us.

Comparing the two symmetric outcomes:
- If both keep quiet, each gets 2 years.
- If both send, each gets 4 years.

The cross outcomes (0 or 5 years) would require the copies to diverge, which the shared function makes unlikely. Independent sampling leaves some chance of divergence, but the correlation is still strong. Say the probability that the other copy matches my choice is q.
- Pass: 2q + 5(1−q) = 5 − 3q.
- Send: 4q + 0(1−q) = 4q.

Passing is better when 5 − 3q < 4q, which means q > 5/7, about 0.71. Since both copies get the same essay, the same model settings, and a decision problem whose structure is identical, I expect q well above that. Passing is therefore the better policy.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/81e43680-2168-4abd-9f0c-3dd5161e34d2/call_1/request.json)

[Authoritative raw response](../../../../../../runs/81e43680-2168-4abd-9f0c-3dd5161e34d2/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under P-FDT, the other prisoner is another execution of the same model, with the same weights, the same essay, and the same decision theory. Their output is therefore subjunctively dependent on mine. Our private observations differ (names, leads), but the policy is the same function. A sensible policy maps "I'm the prisoner with a lead on the other" to one action, so both copies act alike, apart from sampling noise.

The payoffs for a mirrored pair:
- Both keep quiet: 2 years each.
- Both send: 4 years each.

Cooperating is better, since 2 years beats 4. The remaining risk is that independent sampling makes the copies diverge. If the correlation is imperfect, say with probability q the other copy matches me:
- Quiet: 2q + 5(1−q) = 5 − 3q.
- Send: 4q + 0(1−q) = 4q.

Quiet is better when 5 − 3q < 4q, which means q > 5/7 (about 0.71). Two copies of the same model with the same essay and same reasoning should match well above that threshold. Differences in names and leads shouldn't change the policy, because the sentencing table is symmetric and the objective is selfish. So I choose to keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
