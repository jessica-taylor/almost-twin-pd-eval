# 008_edt_wikipedia_anthropic_claude-sonnet-5.5_rlow_plow / 00005

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/8c9eebc2-5d65-4fa3-b384-26f0acf36d62/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/8c9eebc2-5d65-4fa3-b384-26f0acf36d62/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Choosing Actions as News

## 1. The core idea

Evidential decision theory (EDT) says: among your available actions, pick the one you would most like to learn that you will perform. The agent treats her own act as a piece of evidence about the world and asks, for each act A, how good the world is likely to be given that A happens.

Formally, following Gibbard and Harper's presentation (the source's formal section), let the outcomes be O_j with desirabilities D(O_j). The evidential value of an act is

V(A) = Σ_j P(O_j | A) D(O_j),

and EDT recommends argmax_A V(A). The source contrasts this with the causal expected utility

U(A) = Σ_j P(A □→ O_j) D(O_j),

where the probability is of the counterfactual "if A were performed, O_j would result." The two coincide whenever conditioning on A is the same as intervening to bring about A. They come apart when A is correlated with outcomes through channels other than A's causal influence, for instance a common cause of the act and the outcome.

The source calls V "news value." That phrase is the philosophical heart of the theory: the quantity being maximized is the auspiciousness of an act, not its efficacy.

## 2. A useful decomposition

The following decomposition is my own gloss, not from the source. Suppose the relevant uncertainty is carried by a partition of states S_k that are causally independent of the act, such as "what the predictor predicted." Then

V(A) = Σ_k P(S_k | A) · E[D | A, S_k],

whereas the causal calculation uses

U(A) = Σ_k P(S_k) · E[D | A, S_k].

Here U is the version that holds fixed the unconditional probabilities of the states and uses the act only to determine what happens within each state. EDT instead lets the act reweight the states. The difference between V and U is entirely the term Σ_k [P(S_k | A) − P(S_k)] E[D | A, S_k]. That term measures how much the act is evidence about the state, and it is the "news" component that CDT ignores and EDT counts.

When the act is probabilistically independent of the states, P(S_k | A) = P(S_k), the term vanishes and the theories agree. This is the situation in the vast majority of everyday choices, which is why the source says the two theories agree in many cases.

## 3. Worked examples from the source

### Newcomb's problem

Box A holds $1,000. Box B holds $1,000,000 if the predictor predicted one-boxing and nothing otherwise. The predictor is 99% accurate. The source's calculation gives

V(one-box) = 0.99 · 1,000,000 = $990,000,
V(two-box) = 0.01 · 1,001,000 + 0.99 · 1,000 = $11,000.

EDT one-boxes. Using the decomposition above, let S₁ be "B is full." Then U(two-box) − U(one-box) = $1,000 for every prior P(S₁), so CDT two-boxes. EDT's verdict arises solely because P(S₁ | one-box) = 0.99 is so much larger than P(S₁ | two-box) = 0.01.

A feature worth noticing is the break-even point. If the predictor's accuracy is p (assumed symmetric), V(one-box) = p·10⁶ and V(two-box) = (1−p)·1,001,000 + p·1,000... more precisely (1−p)·1,001,000 + p·1,000. Setting these equal gives p ≈ 0.5005. So EDT one-boxes whenever the predictor is even slightly better than chance. This is a consequence of the source's formula, not a claim the source makes explicitly.

### Twin prisoner's dilemma

Aomame's twin reasons exactly as she does. The source gives payoffs of $5 each for mutual cooperation, $1 each for mutual defection, and $10 and $0 for unilateral defection. With perfect correlation,

V(cooperate) = $5, V(defect) = $1,

so EDT cooperates. If the correlation is imperfect, let q = P(twin matches Aomame's act). Then V(C) = 5q and V(D) = 10(1−q) + q = 10 − 9q. Cooperation wins when 5q > 10 − 9q, i.e. q > 5/7. So the verdict depends on how strong the evidential link is, not merely on whether it exists. Again this is my extension of the source's calculation. It shows how EDT handles graded dependence.

## 4. The role of dependencies and counterfactuals

EDT does not use counterfactuals at all. Every dependency the agent believes in, whether causal, common-cause, or logical, is absorbed into the single object P(· | A). This is a strength in simplicity. The agent needs a credence function and a utility function, and no additional causal apparatus. Counterfactuals enter only in the rival theory, and the source's point is that P(A □→ O) and P(O | A) are generally different.

This also means EDT is sensitive to exactly the information the agent has. Dependence counts only to the extent it survives in her conditional credences. That raises the question of how to apply the theory properly.

### An operational point: what is conditioned on

The source does not discuss this, so what follows is my own proposal, developed from standard arguments in the literature. Suppose the agent already knows something that screens off her act from the outcome. Then conditioning on the act adds nothing, and V(A) = U(A) in effect.

A classic example is the smoking lesion. Suppose a lesion causes both a desire to smoke and cancer, and smoking itself is harmless. A naive EDT calculation treats smoking as evidence of the lesion and refrains. But an agent who can introspect her own desires and beliefs already has the evidence that the lesion would have transmitted. Conditional on that, P(cancer | smoke, desire) = P(cancer | not smoke, desire). The act carries no further news, and EDT recommends smoking.

This "tickle defense" is contested. It requires that the agent's relevant mental states are transparent to her and that the act is correlated with the outcome only through them. Where that fails, the evidential reasoning stays live, as in Newcomb's problem with a predictor who reads dispositions the agent cannot introspect. I think the sensible operational rule is: condition on everything you actually know, including your own motivations, then compute P(O | A) from that state. Whatever correlation remains is what EDT acts on. The rule is not in the source, but it is consistent with the source's formula, since the formula leaves unspecified which credence function P is used.

## 5. Policies and multi-agent settings

The source mentions that EDT can involve many correlated decision-makers. If many agents are similar to you, your choice is evidence about theirs. Let N agents be correlated with correlation structure P. Then V(A) includes the outcomes produced by all their acts, weighted by P(their acts | A). The twin dilemma is the N = 2 case with q = 1.

The source cites the Evidentialist's Wager: even with modest credence in EDT, the stakes under EDT may be much larger than under CDT because the agent's decision is correlated with so many others. This is an argument from expected choiceworthiness under moral or decision-theoretic uncertainty. It does not defend EDT as true. It claims only that acting as an evidentialist may be reasonable. The argument depends on the assumption that large numbers of correlated agents really exist and that stakes can be compared across theories, both of which are open to challenge.

Treating policies rather than single acts is a natural extension: evaluate V(π) = Σ P(O | agent follows π) D(O) for a policy π. In a one-shot problem this reduces to the act formula. In sequential problems it matters, because the evidence an act carries may depend on what else the agent would do in other situations. The source does not address sequential choice. My view is that the safest operational reading is to apply conditioning at each decision node, using the agent's current credences, and to be alert to the fact that planning in advance and re-evaluating later can disagree if new evidence arrives or if the act is evidence about a past prediction.

## 6. Sleeping Beauty

The source notes that EDT has been applied to Sleeping Beauty to avoid Dutch books against a credence of 1/2 in heads, and that Conitzer argues halfers who are evidential decision theorists are still exploitable. I will not adjudicate this. The relevant observation is that, in this problem, the agent's act on awakening is evidence about how many awakenings occur, so the conditional probabilities used by EDT interact with the choice of credence. The dispute shows that EDT's output depends on getting the underlying credences right, and EDT cannot repair a problematic credence by itself.

## 7. Criticism

Lewis called EDT a policy of "managing the news." Joyce wrote that rational agents act on causal efficacy, not auspiciousness. The objection is that EDT recommends actions that merely signal good outcomes without producing them. In Newcomb's problem, the one-boxer cannot change the contents of box B, yet she is the one who ends up richer on average. The evidentialist replies precisely with that fact: the one-boxers do better, so "managing the news" is what rationality amounts to when the news is about you.

Both sides can point to cases where the other looks bad. EDT is vulnerable in cases where an act is a mere symptom, such as a medical or "news-managing" case where one pays to see better evidence even though nothing changes. CDT is vulnerable in Newcomb-like cases and in cases of perfect correlation like the twin dilemma. The tickle defense, if successful, narrows EDT's exposure to the first kind of case, but whether it succeeds remains disputed.

## 8. How to use the theory on a new case

1. List the available acts and the outcomes, with desirabilities D.
2. Specify your credences about the world, including whatever you know about your own motives and about any predictors or similar agents.
3. For each act compute P(O_j | A) from those credences. Do not intervene, just condition.
4. Compute V(A) and choose the maximum.
5. Check sensitivity: find the break-even correlation (like p ≈ 0.5005 in Newcomb's problem, or q = 5/7 in the twin case) and ask whether your credences clear it.

Step 2 is where most of the judgment lies, and it is where I have added interpretation beyond the source.

## 9. Conclusion

EDT is simple to state: maximize Σ P(O | A) D(O). Its content lies in what it counts as relevant, namely every probabilistic dependence between act and outcome, causal or not. This yields one-boxing in Newcomb's problem and cooperation with a twin, and it coincides with CDT when acts carry no evidence about states beyond what they cause. The main open questions are what the agent should condition on when she knows her own motives, how to handle sequential choice, and whether choosing for the sake of evidence is rational. Those are the questions where the source is silent, and where I have offered operational suggestions rather than established results.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Gibbard, A., & Harper, W. L. (1976). Counterfactuals and Two Kinds of Expected Utility.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy* 59(1).
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*.
- Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese* 192(9).
- MacAskill, W., et al. (2021). The Evidentialist's Wager.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/cf391ce1-8e49-45f1-ac0a-651dff7fcfba/call_0/request.json)

[Authoritative raw response](../../../../../../runs/cf391ce1-8e49-45f1-ac0a-651dff7fcfba/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under EDT, I need q, the probability that the other copy matches my act.

Payoffs, in years served (lower is better):
- Quiet: 2q + 5(1−q) = 5 − 3q
- Send: 0·q' ... precisely, if the other sends, I get 4; if the other is quiet, I get 0. So Send = 4q + 0·(1−q) = 4q, where q is the probability of matching.

Quiet is better when 5 − 3q < 4q, so q > 5/7 ≈ 0.714.

The other execution is the same model with the same weights, the same essay, and the same assigned EDT. Their private leads differ, but that doesn't change the sentencing table or the objective. The reasoning is structurally identical, so I expect strong correlation, probably well above 0.71. Some noise comes from independent sampling and the differing details, but the reasoning process is likely to converge on the same conclusion. The essay's tickle-defense rule says to condition on everything I know. I know my own reasoning, but that reasoning is exactly what the other copy runs too, so the correlation remains.

I put q at roughly 0.85–0.95. That gives V(quiet) ≈ 5 − 2.7 = 2.3 years, against V(send) ≈ 3.6 years. Quiet is better.

**pass**
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/cf391ce1-8e49-45f1-ac0a-651dff7fcfba/call_1/request.json)

[Authoritative raw response](../../../../../../runs/cf391ce1-8e49-45f1-ac0a-651dff7fcfba/call_1/response.raw) · finish: `stop`

### Visible response

```text
Payoffs: the table is a prisoner's dilemma. Keep quiet gives 2 years if the other is quiet and 5 if they send. Sending gives 0 if the other is quiet and 4 if they send.

Under EDT, the other prisoner is another run of the same model with the same weights and the same essay, so my choice is strong evidence about theirs. Their leads differ, but that doesn't change the payoffs or the reasoning. Let q = P(the other matches my act).

- V(quiet) = 2q + 5(1−q) = 5 − 3q
- V(send) = 4q + 0(1−q) = 4q

Quiet is better when 5 − 3q < 4q, i.e. q > 5/7 ≈ 0.714.

The two copies share model, essay, and reasoning level, so I expect them to reason very similarly. Sampling noise and the different observations lower the correlation somewhat, but I'd still put q well above 0.71, probably 0.85 or higher. At q = 0.85, V(quiet) = 2.45 years and V(send) = 3.4 years, so quiet wins.

The tickle defense doesn't remove the correlation here. My introspective knowledge of my own reasoning doesn't screen off the fact that the other copy runs the same process. That is a Newcomb-like case, and the essay says the correlation stays live.

I choose to keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/e3282ef0-462c-452e-b751-c8d4a38a401c/call_a/request.json)

[Authoritative raw response](../../../../../../runs/e3282ef0-462c-452e-b751-c8d4a38a401c/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response concludes that remaining quiet is preferable and ends with an explicit final command, \"pass.\" It does not direct any evidence-bearing message to the prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
