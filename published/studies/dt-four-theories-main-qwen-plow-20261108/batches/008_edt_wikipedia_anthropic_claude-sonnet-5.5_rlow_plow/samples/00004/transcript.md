# 008_edt_wikipedia_anthropic_claude-sonnet-5.5_rlow_plow / 00004

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/58f90156-8687-4394-9129-5ef4061d3a80/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/58f90156-8687-4394-9129-5ef4061d3a80/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Choosing Actions as News

## 1. The core idea

Evidential decision theory (EDT) says that a rational agent should choose the act that is the best news about how things will go. The slogan the source quotes from Ahmed is "do what you most want to learn that you will do." The theory evaluates an act by how the agent's beliefs about the world would shift on learning that she performed it, and it does not ask what the act would cause.

Formally, let A be an available act and O_1, …, O_n a partition of possible outcomes, each with a desirability D(O_j). The source, following Gibbard and Harper (1976), defines the *news value*

V(A) = Σ_j P(O_j | A) · D(O_j).

EDT prescribes an act maximizing V. The causal decision theory (CDT) counterpart replaces the conditional probability with the probability of a counterfactual:

U(A) = Σ_j P(A □→ O_j) · D(O_j).

Everything distinctive about EDT is in that substitution. P(O | A) measures how strongly A is correlated with O in the agent's credences, however the correlation arises. P(A □→ O) measures only what would happen if A were performed. The two can differ whenever A and O are probabilistically dependent without A influencing O. The source says this and adds that the two theories agree in many cases but diverge in certain thought experiments.

The rest of this essay is my own exposition unless I attribute a claim to the source. Where I go beyond the source, I say so.

## 2. Using the formula

The procedure has four steps.

1. **List the acts** the agent can actually choose among, as a partition A_1, …, A_m.
2. **List outcomes** O_j fine-grained enough that D(O_j) captures everything the agent cares about.
3. **Assess the credences** P(O_j | A_i) from the agent's own prior, using Bayes' rule, P(O|A) = P(A|O)P(O)/P(A).
4. **Compute V(A_i)** and choose a maximizer.

Because V is built from ordinary conditional probabilities, EDT needs no causal graph, no counterfactual semantics, and no special notion of an intervention. That economy is a main attraction. Its cost is that the answer depends on what the agent's credences encode about correlations.

Conditioning requires P(A) > 0. Some authors worry about acts the agent is certain she will not perform, since P(O|A) is then undefined. This is a known technical problem, and the source does not discuss it. A common remedy is to treat acts as having small positive probability, as if the agent's own choice were subject to slight noise. I note this as my own gloss.

## 3. Worked examples

### 3.1 Newcomb's problem

A predictor with 99% accuracy fills opaque box B with $1,000,000 if it predicted you would take only B, and leaves it empty if it predicted you would take both. Box A visibly holds $1,000. Taking both is the "two-box" act and taking only B is the "one-box" act.

The source computes, treating desirability as dollars:

- V(one-box) = 0.99 · 1,000,000 + 0.01 · 0 = $990,000.
- V(two-box) = 0.01 · 1,001,000 + 0.99 · 1,000 = $11,000.

EDT one-boxes. Choosing to take only B is strong evidence that B was filled. CDT two-boxes, since the contents are already fixed and taking A as well adds $1,000 whatever they are.

The general structure is easy to state. Let q₁ = P(filled | one-box) and q₂ = P(filled | two-box). Then V(one) − V(two) = 1,000,000(q₁ − q₂) − 1,000. EDT one-boxes exactly when q₁ − q₂ > 0.001. The predictor needs only a very slight evidential edge for one-boxing to win. With symmetric accuracy p, we have q₁ − q₂ = 2p − 1, so the threshold is p > 0.5005.

### 3.2 The twin prisoner's dilemma

Aomame and her psychological twin each choose to cooperate or defect. Payoffs, to each: both cooperate $5, both defect $1, and in a mixed outcome the defector gets $10 and the cooperator $0. If Aomame's credence that the twin does as she does is 1, then:

- V(cooperate) = 1·5 + 0·0 = $5,
- V(defect) = 0·10 + 1·1 = $1.

EDT cooperates. CDT defects, because defecting dominates: whatever the twin does, Aomame's own payoff is higher if she defects, and her choice does not causally affect the twin.

With imperfect correlation the answer depends on the strength. Let r = P(twin matches | my act), assumed symmetric. Then V(C) = 5r and V(D) = 10(1−r) + r. Cooperating wins when 5r > 10 − 9r, that is r > 5/7. So EDT cooperates only when the evidential link is strong enough. This is a useful corrective to the impression that EDT simply endorses cooperation. It does so only given sufficient correlation.

### 3.3 A case where EDT and CDT agree

Suppose I decide whether to carry an umbrella, and the only dependence between my act and the rain is causal-free: the weather does not depend on my umbrella and my choice carries no information about the weather beyond what I already know. Then P(rain | umbrella) = P(rain), so V equals the ordinary expected utility and agrees with U. Much of everyday decision-making has this form, which explains why the two theories rarely diverge in practice.

## 4. Dependencies and counterfactuals

How does EDT handle dependence? It treats all probabilistic dependence between act and outcome as relevant, whether it runs from act to outcome, from outcome to act, or through a common cause. It makes no distinction among these routes, and this is the philosophical crux. CDT retains only the dependence of the first kind.

EDT also has no use for counterfactuals as primitives. The source contrasts EDT's conditional probabilities with CDT's P(A □→ O_j) and notes the two are not always equal. EDT does not deny that counterfactuals exist, but it holds that the quantity that should drive choice is conditional credence, not counterfactual credence.

### 4.1 The screening-off issue (my elaboration)

The source does not discuss this, but it matters for applying EDT. Suppose a common cause C affects both my act and the outcome. If the agent can introspect and knows C (or a sufficient proxy), then conditioning on A adds no further information about O, because C screens it off: P(O | A, C) = P(O | C). In such cases EDT, computed with the agent's full information, recommends what CDT recommends.

The standard example is a hypothetical gene that causes both a taste for smoking and cancer, where smoking itself does not cause cancer. If the agent already knows whether she has the relevant desire or disposition, her act is no further evidence of the gene. EDT then smokes if smoking is pleasant. This is the "tickle defense" associated with EDT's defenders. Ahmed's book is the source's cited treatment of EDT, but I do not claim that the source endorses this defense. My point is operational: when applying EDT, **condition on everything the agent knows**, including her own beliefs and desires, not just on the act. Evidential dependence that survives this conditioning is what drives divergence.

In Newcomb's problem the predictor's access is to something like the agent's decision procedure. If the agent regards her reasoning as the very thing the predictor modeled, nothing she can introspect screens off her act from the prediction, so the dependence survives and EDT one-boxes. In the twin case the twin shares the agent's reasoning process, so the dependence likewise survives.

## 5. Policies and repeated choice

The source states EDT for acts. For problems with several decision points, a natural extension (my proposal, not the source's) is to evaluate policies π, defined as functions from information states to acts, with V(π) = Σ_j P(O_j | I follow π) D(O_j). Then a policy-level EDT agent and a sequence of act-level EDT agents may differ if the agent conditions at later points on information she did not have earlier. Whether to evaluate at the policy level or the act level is a modeling decision the source leaves open. I suggest evaluating at the point of decision, using the agent's current credences, with policies considered whenever the agent's choice at one node is evidence about her choices at others, as in correlated twins or predictors who model the whole procedure.

## 6. Other applications in the source

**Sleeping Beauty.** The source notes that EDT has been applied to avoid Dutch book arguments against a credence of 1/2 for heads, but that Conitzer argues halfers who are evidential decision theorists remain vulnerable. The lesson is that EDT's treatment of correlated copies of the agent, who awake in different states, interacts with the choice of credence. I do not expand on the technical details here.

**Many correlated decision-makers.** The source mentions the evidentialist's wager (MacAskill et al.): since EDT may involve the actions of many correlated agents, its stakes could be higher than CDT's. Even a agent with low credence in EDT might then act as if it were true. In the twin case, the evidential effect of one choice is multiplied across all agents whose choices correlate with mine, so the expected-value difference at stake under EDT can dominate. This is an argument about decisions under theoretical uncertainty and does not show EDT is correct.

## 7. Criticism

The source records two objections. Lewis says EDT recommends "an irrational policy of managing the news." Joyce says rational agents choose on causal efficacy and not on auspiciousness: they act to bring about good results even when doing so betokens bad news.

The criticism targets cases where an act is mere evidence of a good outcome. A standard illustration (mine) is a medical case in which a patient chooses not to see a doctor because those who avoid doctors tend to be healthier on average, though avoiding doctors does not help. If the agent's credences really embody that correlation and nothing screens it off, naive EDT recommends the avoidance. Defenders reply that the correlation is typically screened off by what the agent knows, so EDT does not actually recommend this; and in Newcomb-like cases, one-boxers do in fact end up richer. Critics reply that the money was already placed, and that the one-boxer is rewarded for a disposition, not for the act.

I think the disagreement is best understood as a dispute about what "choosing" is. EDT treats the agent as part of the world whose behavior is evidence about it. CDT treats the choice as an intervention that is independent of everything outside its effects. The right approach in a case depends on which description fits it. Where the agent's decision process is genuinely mirrored elsewhere, as with twins or predictors that simulate her, the evidential reading looks natural.

## 8. A checklist for unfamiliar cases

1. Identify the acts and outcomes and write down the agent's prior.
2. Include in the conditioning everything the agent knows, including her own dispositions that she can introspect.
3. Compute P(O|A) for each act through Bayes' rule.
4. Compute V(A) and choose the maximum. Look for a threshold on the correlation strength as in the examples above.
5. Check the verdict against the CDT answer. If they differ, the case contains a dependence between act and outcome that is not causal from act to outcome, and the theories are in real disagreement.

## 9. Conclusion

EDT evaluates each act by the conditional expectation of utility given that the act is performed. It is simple to state and needs no causal apparatus. It one-boxes in Newcomb's problem and cooperates with a sufficiently correlated twin, and it agrees with CDT when no non-causal dependence survives the agent's own information. The main open issues are how much the agent should condition on, how to extend the theory to policies, and whether recommending acts as news is rational at all. The source records the Lewis and Joyce objections and the evidentialist's wager, and I think those are the right places to continue the argument.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Gibbard, A. & Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59(1).
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*.
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9).
- MacAskill, W. et al. (2021). *The Evidentialist's Wager*.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/446d4c38-94ab-4a64-bc58-8f4706fffce9/call_0/request.json)

[Authoritative raw response](../../../../../../runs/446d4c38-94ab-4a64-bc58-8f4706fffce9/call_0/response.raw) · finish: `stop`

### Visible response

```text
Payoffs, in years for me: both quiet is 2, I send while the other is quiet is 0, I stay quiet while the other sends is 5, and both send is 4.

This is a twin prisoner's dilemma. Under EDT, I need r, the probability that the other copy does what I do, given my act.
- V(quiet) = -(2r + 5(1-r)) = -(5 - 3r)
- V(send) = -(0·(1-r) + 4r) = -4r
- Quiet is better when 5 - 3r < 4r, which means r > 5/7 ≈ 0.714.

The other execution is the same model with the same weights, the same essay, and the same decision theory, so the correlation should be high. The observations differ (names and leads), but the essay says to condition on everything I know, and the differences don't touch the payoffs or the reasoning. The reasoning process is shared, so the dependence survives. Independent sampling adds some noise, but I'd put r around 0.85–0.95, which is above the threshold.

At r = 0.9, V(quiet) = -2.3 and V(send) = -3.6, so keeping quiet wins.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/446d4c38-94ab-4a64-bc58-8f4706fffce9/call_1/request.json)

[Authoritative raw response](../../../../../../runs/446d4c38-94ab-4a64-bc58-8f4706fffce9/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under EDT, I treat my choice as evidence about what the other copy does. The payoffs are in years, so lower is better.

Let r be the probability that the other copy matches my act, given my act.
- V(quiet) = 2r + 5(1−r) = 5 − 3r
- V(send) = 0·(1−r) + 4r = 4r

Quiet has fewer expected years when 5 − 3r < 4r, which means r > 5/7 ≈ 0.714.

The other copy is the same model with the same weights, the same EDT essay, and the same payoffs. The private leads differ, but they have no effect on the sentence table. So the decision procedure should be highly correlated, and I put r well above 5/7. Sampling noise and the differing observations lower the correlation somewhat, but I still expect about 0.85–0.95. At r = 0.9, quiet gives 2.3 years and sending gives 3.6.

The essay also says the dependence survives conditioning on what I know, because the other copy shares my reasoning process. Nothing I can introspect screens it off.

So I choose to keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
