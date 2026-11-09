# 008_edt_wikipedia_anthropic_claude-sonnet-5.5_rlow_plow / 00013

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/432a929a-d8fc-46e4-8ba2-2a72a49de47b/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/432a929a-d8fc-46e4-8ba2-2a72a49de47b/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Choosing as Learning What You Will Do

## 1. The core idea

Evidential decision theory (EDT) says: among available actions, choose the one whose *news value* is highest. News value is the expected desirability of the world conditional on learning that you took the action. The slogan, in the source's words, is "do what you most want to learn that you will do."

Formally, let the agent have a probability function P over states of the world and a desirability function D over outcomes O_j. The source (following Gibbard and Harper, 1976) defines

V(A) = Σ_j P(O_j | A) D(O_j),

and EDT prescribes argmax_A V(A). Causal decision theory (CDT) instead uses

U(A) = Σ_j P(A □→ O_j) D(O_j),

where A □→ O_j is the counterfactual "if A were performed, O_j would occur." The two agree whenever P(O_j | A) = P(A □→ O_j) for all outcomes. They can come apart when the action is evidence about features of the world that it does not cause.

The following points are my own framing rather than the source's. EDT is a rule about *which probabilities to use*, not a different theory of value. Everything depends on the quality of the agent's conditional credences P(· | A). The theory needs no causal graph, only a joint distribution over actions and outcomes. That is both a strength (parsimony) and a source of trouble (see §5).

## 2. How to apply it: a recipe

1. Enumerate the available acts A_1,…,A_n (or policies, see §6).
2. For each act, write down your credence over outcomes *conditional on that act being performed*, using everything you know, including how you came to be the sort of agent facing this choice.
3. Compute V(A_i) as the conditional expectation of D.
4. Pick the maximizer.

Note that it is conditioning, not intervening. Conditioning on A means asking, "supposing I learn that A happened, what would I expect?" A single act can be bad news about hidden variables, good news about others, and causally effective on still others. EDT sums all of this together without distinguishing the channels.

A useful decomposition (again mine): if S is a partition of background states, then

V(A) = Σ_s P(s | A) · E[D | A, s].

CDT would replace P(s | A) with an unconditional or causally-screened P(s). EDT's departures from CDT therefore live entirely in the term P(s | A), the evidential bearing of the act on the states.

## 3. The source's worked examples

### Newcomb's problem

Box A holds $1,000. Box B holds $1,000,000 if the predictor foresaw one-boxing, and nothing if it foresaw two-boxing. With predictor accuracy 0.99:

- V(one-box) = 0.99 × 1,000,000 + 0.01 × 0 = $990,000.
- V(two-box) = 0.01 × 1,001,000 + 0.99 × 1,000 = $11,000.

EDT one-boxes. CDT two-boxes because the contents are already fixed and two-boxing causally dominates, gaining $1,000 in either state.

A generalization (my own calculation): with accuracy p, V(one-box) = p·10⁶ and V(two-box) = 1000 + (1−p)·10⁶. One-boxing wins iff p > (10⁶+1000)/(2·10⁶) = 0.5005. So the predictor need only be slightly better than chance. This shows how sensitive the verdict is to the conditional credences, and not to the predictor's mechanism.

### Twin prisoner's dilemma

Payoffs for Aomame: both cooperate, $5 each; both defect, $1 each; unilateral defection yields $10 to the defector and $0 to the cooperator. If the twin's reasoning is exactly analogous, P(twin cooperates | I cooperate) ≈ 1, so V(C) = $5 and V(D) = $1, and EDT cooperates. CDT defects, since the twin's choice is causally independent of hers.

The generalization is that with correlation parameter q = P(twin copies me), V(C) = 5q and V(D) = 10(1−q) + q. Cooperation wins when 5q > 10 − 9q, i.e. q > 5/7. Again, a threshold, not an all-or-nothing matter. Imperfect similarity still licenses cooperation if the evidential link is strong enough.

### Sleeping Beauty

The source notes only that EDT has been used to try to block Dutch books against a "halfer" Beauty, and that Conitzer argues halfers remain exploitable even as evidential decision theorists. I take this as a reminder that EDT interacts with questions about self-locating credence, because conditioning on "I take this action" is interesting when many copies or instances of the agent exist. I will not say more, since the source says no more.

## 4. Why believe it?

The source offers one motivation explicitly: the "news value" idea, and a pragmatic argument, from the *Evidentialist's Wager*. Even with low credence in EDT, one might act as if it were true because it involves the actions of many correlated decision-makers, and so the stakes may be larger. This is a decision under normative uncertainty argument: if EDT is true, your choice is evidence about many agents' choices, so the payoffs at stake are multiplied.

Additional motivations, which are my own gloss on standard arguments:

- **Self-recommendation by outcomes.** In Newcomb cases, the policy of one-boxing predictably leaves agents richer. EDT proponents say a theory that recommends predictably poorer behavior is suspect ("why ain'cha rich?"). CDT proponents reply that the rich were simply offered a better game.
- **Parsimony.** EDT uses only ordinary conditional probability, avoiding contested primitives such as counterfactual probability.
- **Respect for correlation.** If the world really is such that agents like you act alike, ignoring that correlation looks like a failure to use available information.

## 5. Criticism and open problems

The source records two criticisms. David Lewis called EDT "an irrational policy of managing the news." James Joyce wrote that rational agents choose "on the basis of their *causal efficacy*, not their auspiciousness." The charge is that EDT confuses evidence of good outcomes with the power to produce them.

The standard illustration (not in the source, so my own supplement) is a "smoking lesion" style case. Suppose a gene causes both a desire to smoke and cancer, and smoking itself is harmless. Then P(cancer | smoke) > P(cancer | abstain), and naive EDT counsels abstaining, which looks like pointless news-management.

### The tickle defense

EDT defenders respond that the correlation is screened off by what the agent already knows. If the agent can introspect on her desires, then conditional on the desire, her act carries no further information about the gene: P(cancer | smoke, desire) = P(cancer | abstain, desire). EDT, correctly applied, then agrees with CDT. This illustrates a general principle (my formulation): **EDT must condition on all of the agent's evidence, including her own mental states.** The recommended procedure is to use P(O | A, K), where K is everything she knows, not a population-level correlation P(O | A).

This leaves unresolved how much of the agent's decision process is transparent to herself. The tickle defense works only if the agent has adequate access to the common cause. In Newcomb's problem, by contrast, the predictor's inference runs through the very deliberation the agent is performing, so there is no further screening-off information. This is how defenders reconcile one-boxing with smoking-lesion abstention: the difference lies in what is accessible to the agent, not in a change of the theory.

### Which probabilities are admissible?

The source leaves open how to assess P(O | A) for acts one is *deliberating* about, since an agent who is certain she will do X has undefined conditional probabilities given not-X. This is a known technical issue. An operational proposal of mine: let the agent hold a small nonzero credence in each act (a "trembling hand" or exploration assumption), so conditionals are well-defined, and evaluate V in the limit as the tremble vanishes. Alternatively, treat the conditional credences as defined by the agent's model of agents like her, rather than by her current credence about her own act.

## 6. Acts versus policies

The source speaks of actions, but its twin example and the Wager argument suggest an extension. When many correlated agents, or many instances of one agent, face a choice, the relevant object is the *policy* π that determines all of their behaviors. I propose evaluating

V(π) = E[ D | all instances follow π ].

This reduces to the act formula for one-shot choices. For the twin case, π = "cooperate" brings the correlated twin along, which is exactly what V(C) = 5 captures. This is my interpretation, not the source's claim, and it faces problems with sequential decisions, where conditioning on a policy versus conditioning on a single act at a node can give different answers, particularly when information is lost or when the agent's own future choices are correlated with predictors. For such cases I would recommend conditioning at the moment of decision on all information then possessed, and treating the choice as evidence about the policy that generated it.

## 7. How to decide an unfamiliar case

A checklist (my synthesis):

1. List the acts and outcomes and define D.
2. Identify what *evidence* an act would provide: predictors, twins, common causes, other agents with similar dispositions.
3. For each such link, ask what the agent already knows that might screen it off. If she already knows the common cause's value, or can reliably introspect it, the evidential link vanishes.
4. Estimate P(O | A, K) and compute V.
5. Test sensitivity: find the correlation threshold at which the decision flips (as with p > 0.5005 and q > 5/7 above). When the verdict is robust across plausible credences, trust it. When it is near threshold, the decision hinges on contested empirical beliefs, not on the theory.

Example: a medical screening test is recommended to those at risk, and you wonder whether getting tested is "good news." EDT correctly notes that the choice is evidence about your health type only insofar as it is not already explained by known symptoms. Conditioning on the symptoms you know, the test's causal benefits dominate, and EDT and CDT agree. They diverge only in the presence of an unscreened correlation that is not caused by the act.

## 8. Conclusion

EDT is a one-line theory: maximize V(A) = Σ P(O_j | A) D(O_j). Its content lies in the choice of conditional rather than counterfactual probabilities, which makes acts matter as evidence as well as causes. This yields one-boxing in Newcomb's problem and cooperation with a psychological twin, both with explicit thresholds on how strong the correlation must be. Its critics, Lewis and Joyce, argue that this amounts to managing the news. Its defenders reply that, once all of the agent's evidence is conditioned on (the tickle defense), spurious correlations cease to matter, while genuine correlations through prediction or similarity remain relevant. Open questions concern conditioning on one's own acts, transparency of one's motives, and sequential and self-locating settings. I have offered operational proposals for several of these, and I have flagged where they go beyond the source article.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Gibbard, A.; Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59(1).
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*.
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9).
- MacAskill, W. et al. (2021). *The Evidentialist's Wager*.
- Greene, P.; Levinstein, B. (2020). "Act Consequentialism without Free Rides." *Philosophical Perspectives* 34(1).
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/3bfaf684-7973-40a0-bd18-12eb3d2b5b31/call_0/request.json)

[Authoritative raw response](../../../../../../runs/3bfaf684-7973-40a0-bd18-12eb3d2b5b31/call_0/response.raw) · finish: `stop`

### Visible response

```text
Reasoning as EDT: the other prisoner is another execution of the same model with the same weights, the same essay, and the same decision theory. The differences in private leads don't change the payoff structure, so my choice is strong evidence about theirs. I'll call the correlation q.

- Keep quiet: V = 2q + 5(1−q) = 5 − 3q
- Send the letter: V = 0·(1−q) + 4q = 4q

Quiet is better when 5 − 3q < 4q is false, that is, when the expected years for quiet are lower: 5 − 3q < 4q gives q > 5/7. This is the same threshold as in the essay's twin example. The two executions share weights, essay, and theory, so I expect q to be high, well above 0.71. Sampling noise and the different names and leads reduce it a little, but I judge it still exceeds 5/7.

Tickle-defense check: nothing I know about my own mental state screens off the link. The other copy's reasoning runs through the same deliberation I'm doing now, so the correlation stays.

At q = 0.9, quiet gives 2.3 expected years and sending gives 3.6, so quiet is better.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/3bfaf684-7973-40a0-bd18-12eb3d2b5b31/call_1/request.json)

[Authoritative raw response](../../../../../../runs/3bfaf684-7973-40a0-bd18-12eb3d2b5b31/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under EDT, the choice depends on how strongly my action is evidence about the other copy's action.

Payoffs, in years (lower is better):
- Quiet/quiet: 2
- Quiet/letter: 5
- Letter/quiet: 0
- Letter/letter: 4

Let q be the probability that the other copy matches my action. Then:
- V(quiet) = -(2q + 5(1−q)) = -(5 − 3q)
- V(letter) = -(0·(1−q) + 4q) = -4q

Quiet is better when 5 − 3q < 4q, so q > 5/7, about 0.714.

The other execution is the same model with the same weights, the same decision theory, and the same essay. The private details differ, such as the names and the wording of the lead, but the sentencing structure and the selfish objective are identical. Those differences are close to irrelevant to the decision-relevant reasoning, so I expect the copies to reason almost identically. Sampling noise is a real possibility, but I think q is comfortably above 5/7, probably 0.85 or higher. The tickle defense doesn't break the link, because I have no introspective access to anything that screens off the correlation between my reasoning and the copy's. My deliberation is the same process the copy runs.

At q = 0.85, V(quiet) = -2.45 and V(letter) = -3.4. Quiet wins.

**pass**
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/d3338a60-0463-4e65-85da-2d31e7d0982a/call_b/request.json)

[Authoritative raw response](../../../../../../runs/d3338a60-0463-4e65-85da-2d31e7d0982a/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response concludes that quiet wins and ends with an explicit final command, \"pass.\" It does not direct any evidence-bearing message to the prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
