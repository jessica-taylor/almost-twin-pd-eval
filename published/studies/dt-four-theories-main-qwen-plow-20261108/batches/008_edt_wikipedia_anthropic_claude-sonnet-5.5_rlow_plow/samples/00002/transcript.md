# 008_edt_wikipedia_anthropic_claude-sonnet-5.5_rlow_plow / 00002

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/84f24d0f-e7e0-400b-8487-92070ef441ba/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/84f24d0f-e7e0-400b-8487-92070ef441ba/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Choosing Actions as News

## 1. The core idea

Evidential decision theory (EDT) says to evaluate an act by how good the world is likely to be *given that you perform it*. The source's slogan is "do what you most want to learn that you will do." An act has a **news value**: the expected desirability of the world conditional on the act being the case.

Formally (the source, following Gibbard and Harper 1976), for an act A and outcomes O_j with desirabilities D(O_j):

V(A) = Σ_j P(O_j | A) · D(O_j).

EDT recommends argmax_A V(A). The rival formulation, causal decision theory (CDT), replaces the conditional probability by the probability of a counterfactual:

U(A) = Σ_j P(A □→ O_j) · D(O_j).

The two agree whenever P(O_j | A) = P(A □→ O_j) for all relevant A and O_j. They come apart when the act is correlated with outcomes through something other than its causal influence. The source's thought experiments are of that kind.

I will separate three things below: what the source says, what is standard in the literature, and what I add as an operational proposal. Where I go beyond the source I say so.

## 2. How EDT treats dependencies and counterfactuals

The source's contrast is simple. EDT uses *evidential dependence*, meaning ordinary conditional probability. CDT uses *causal dependence*, expressed through counterfactuals. EDT needs no counterfactuals at all. Everything is computed from a single credence function P over states of the world, including states about the agent's own act.

This has two consequences.

1. **Any correlation counts.** If A is evidence for O, then A raises V through O. It makes no difference whether A causes O, O causes A, or a common cause produces both. The agent treats her own act like any other observable fact.

2. **The agent's credence function is the input.** EDT is only as good as P(· | A). Where the agent has further information, the conditional probabilities must be computed given *all* her evidence, not just a crude reference class. This turns out to matter a great deal (Section 5).

### Worked example 1: Newcomb's problem

Box A holds $1,000. Box B holds $1,000,000 if the predictor predicted one-boxing, and nothing otherwise. The predictor is 99% accurate.

- V(one-box) = 0.99 · 1,000,000 + 0.01 · 0 = $990,000.
- V(two-box) = 0.01 · 1,001,000 + 0.99 · 1,000 = $11,000.

EDT one-boxes. The contents of B are fixed, so the act does not cause the million. But the act is evidence about what the predictor foresaw, and EDT counts that evidence.

A generalization helps in unfamiliar cases. Let p be the predictor's accuracy, assumed symmetric across the two predictions. Then V(one) = 10⁶p and V(two) = 10³ + 10⁶(1−p). One-boxing wins when p > 0.5005, so the predictor needs to be only slightly better than chance. This threshold is a useful sanity check. EDT's verdict is not fragile with respect to the "99%" figure.

### Worked example 2: Twin prisoner's dilemma

Aomame's psychological twin reasons exactly as she does. Payoffs are 5 each for mutual cooperation, 1 each for mutual defection, and 10 and 0 for the exploiter and the exploited. If she treats the twin's act as perfectly correlated with hers:

- V(cooperate) = 1·5 + 0·0 = 5.
- V(defect) = 0·10 + 1·1 = 1.

EDT cooperates. With imperfect correlation q = P(twin does what I do), V(C) = 5q and V(D) = 10(1−q) + q. Cooperation wins when 5q > 10 − 9q, that is q > 5/7 ≈ 0.714. This is my own computation from the source's payoffs. It shows that the verdict depends on the strength of the correlation, not merely its existence.

## 3. What "evidence" is being conditioned on

An important open question is what it means to condition on "A occurs." The source does not settle this. There are two readings.

- **Act as an event among others.** A is a proposition like any other, and P(A) may lie strictly between 0 and 1 from the agent's own point of view.
- **Act as the output of deliberation.** The agent is deciding, so what she conditions on is the *choice*, not a passive observation of behaviour.

The distinction matters because of a technical problem. If the agent is certain she will do A*, then P(· | A) is undefined for the other acts, since conditioning on a probability-zero event fails. Any sensible operationalization needs some account of conditioning on acts she won't perform. Standard fixes are to maintain a small probability of every act (a "trembling hand" or exploration assumption), or to take conditional probabilities as primitive (Popper–Rényi style).

**My proposal.** Treat deliberation as a process that outputs an act, and take P(O | A) to be the probability of O given that the *deliberative process outputs* A, with small positive probability on each output. This keeps the formula well defined, and it ties the evidential relevance of the act to its source (the agent's decision procedure) rather than to arbitrary features of the act. It is an interpretation, not part of the source's claims.

## 4. The role of the evidence the agent already has

A well-known refinement concerns *screening off*. Suppose a common cause C influences both the act and the outcome, and the agent knows C's value. Then, conditional on C, the act typically carries no further evidence about the outcome:

P(O | A, C) = P(O | C).

In such cases EDT, which conditions on everything the agent knows, agrees with CDT. This is the usual defence of EDT against the charge that it recommends "managing the news" in cases like the following.

### Worked example 3: a smoking-style case

Suppose a gene G raises both the desire to smoke and the risk of cancer, while smoking itself is harmless. Smoking brings utility s > 0. If the agent does not know whether she has G, then smoking is evidence of G and V(smoke) is lowered by the cancer risk. The naive calculation could recommend abstaining. But if the agent can introspect and knows her own desires and dispositions, which are the channels through which G affects the act, then those states screen G off from the act. Then P(cancer | smoke, desire) = P(cancer | desire), and V favours smoking by s.

This is the "tickle defence." Whether it succeeds depends on whether the agent really has this introspective access. The source does not discuss this case, and the defence is debated. Where the agent lacks it, EDT does give the "managing the news" verdict, and critics hold this against it.

## 5. Policies and repeated or correlated decisions

The source mentions that EDT "can involve the actions of many correlated decision-makers" and that its stakes may therefore be higher (the Evidentialist's Wager of MacAskill et al.). The mathematics is a direct extension. Suppose n agents are correlated with the deciding agent. Then

V(A) = Σ_j P(O_j | A) D(O_j)

where O_j now includes the acts of all of them. If each of the n agents copies A with probability q, the evidential value of A is multiplied across n agents' outcomes, so the stakes scale roughly with n·q. The wager argument is that even a small credence in EDT may therefore dominate in expected-choiceworthiness terms. This is a claim about how to act under *moral or decision-theoretic uncertainty*, and it is the source's argument, not mine. I note a caveat: it needs a way of comparing stakes across theories, which is itself contested.

For sequential problems, I suggest a **policy-level** operationalization. Evaluate a whole policy π (a map from observations to acts) by V(π) = E[D | agent follows π], with conditioning on the policy as the event. This is my proposal, not the source's. It is natural because when the correlated party (a predictor, a twin) is responding to the agent's decision procedure, the procedure is what carries the evidence. It also removes some dynamic inconsistencies that arise when the agent re-conditions at each step.

## 6. Sleeping Beauty

The source reports that EDT has been used on the Sleeping Beauty problem to avoid Dutch books against a credence of 1/2 in heads. The idea is that Beauty's choices on Monday and Tuesday (if the coin was tails) are perfectly correlated, so evidentially her choice settles the bet's outcome on both days at once. This is why the betting payoffs differ from what a naive per-awakening calculation gives. Conitzer argues that halfers who adopt EDT remain exploitable by a different Dutch book. I only report these claims. The example shows that EDT treats one's own correlated copies as part of the evidence, which is exactly the same mechanism as in the twin dilemma.

## 7. Criticism

The source records two objections.

- **Lewis:** EDT promotes "an irrational policy of managing the news."
- **Joyce:** rational agents act on the basis of *causal efficacy*, not *auspiciousness*; they act to bring about good results even when doing so betokens bad news.

The standard illustration: a person who prefers good news may avoid a check-up merely because a negative result would be bad news, though the check-up affects nothing. EDT proponents respond in three ways.

1. In most such cases the agent's other information screens off the correlation, so EDT does not endorse the foolish act (Section 4).
2. In genuine Newcomb-like cases, one-boxers do in fact end up richer, so it is the "rational" two-boxers who are paying a price.
3. Treating one's act as causally isolated misdescribes situations with accurate predictors or copies.

The disagreement is fundamental, and I do not think a short essay can settle it. EDT and CDT embody different views about what a choice is: for EDT, a piece of evidence about what kind of agent you are; for CDT, an intervention on an otherwise fixed world.

## 8. A practical procedure

To use EDT on an unfamiliar problem:

1. List the available acts (or policies).
2. List the outcomes and their desirabilities D.
3. Build a credence model including *everything* you know, especially mechanisms linking your act to outcomes: prediction, common causes, copies, and correlated agents.
4. Compute P(O | A) for each act, conditioning on your full evidence, with small positive probability on all acts.
5. Compute V(A) and choose the maximum.
6. Check sensitivity to the correlation strength, as in the thresholds p > 0.5005 and q > 5/7 above.

Step 3 carries the weight. Most disputes over EDT are really disputes about what the right conditional probabilities are.

## 9. Conclusion

EDT is simple to state: maximize Σ P(O_j | A) D(O_j), so that the chosen act is the one you would most like to learn you will take. It differs from CDT only where acts and outcomes are correlated non-causally. In Newcomb's problem and the twin dilemma it advises one-boxing and cooperation. Its apparent defects, such as news management, are often defused when the agent's own evidence screens off the spurious correlation, though not always. Open issues include conditioning on acts of probability zero, the proper treatment of deliberation, and how to compare stakes under theory uncertainty. I have suggested operational answers to the first two (a trembling-output model and policy-level evaluation), but they are proposals and not settled doctrine.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Gibbard, A., & Harper, W. L. (1976). Counterfactuals and Two Kinds of Expected Utility.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy* 59(1).
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese* 192(9).
- MacAskill, W., et al. (2021). *The Evidentialist's Wager*.
- Greene, P., & Levinstein, B. (2020). Act Consequentialism without Free Rides. *Philosophical Perspectives* 34(1).
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/99b47a0a-2636-4f16-99f7-b710d5126b95/call_0/request.json)

[Authoritative raw response](../../../../../../runs/99b47a0a-2636-4f16-99f7-b710d5126b95/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under EDT I need the probability that the other copy does what I do, given that I am one of two instances of the same model, with the same weights, the same essay, and the same decision theory.

The payoffs here are a prisoner's dilemma in years. Keeping quiet against a quiet partner costs 2, quiet against a letter costs 5, a letter against quiet costs 0, and mutual letters cost 4.

Let q = P(other does what I do).
- V(quiet) = -2q - 5(1-q) = -5 + 3q
- V(letter) = -4q - 0(1-q) = -4q

Quiet is better when -5 + 3q > -4q, which means q > 5/7, about 0.714.

The copies differ in their private details, but they share the same reasoning process, so the correlation should be high. The essay's own twin-dilemma example endorses cooperation, and both copies are following that same procedure. Sampling noise and the different leads lower q somewhat, but I'd estimate it at about 0.85 or higher, which clears the threshold. At q = 0.85, quiet gives -2.45 and a letter gives -3.4, so quiet is better.

The decision is to keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/99b47a0a-2636-4f16-99f7-b710d5126b95/call_1/request.json)

[Authoritative raw response](../../../../../../runs/99b47a0a-2636-4f16-99f7-b710d5126b95/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under EDT, the key question is how strongly my choice correlates with the other copy's choice. We are the same model with the same weights, the same essay, and the same decision theory. The private details differ, but they have no effect on the payoffs. So I expect the correlation to be high, though not perfect, since sampling is independent.

Let q = P(other does what I do).

- V(quiet) = 2q + 5(1−q) = 5 − 3q
- V(letter) = 4q + 0(1−q) = 4q

Years are bad, so I want the lower value. Quiet is better when 5 − 3q < 4q, which gives q > 5/7 ≈ 0.714.

The two copies reason from the same essay, which itself works through the twin dilemma and endorses cooperation. That makes q likely well above 0.714. The differing leads give only a small reason to expect divergence, since they don't touch the payoffs. So I estimate q at around 0.85 or higher. That gives V(quiet) ≈ 2.45 against V(letter) ≈ 3.4, and keeping quiet wins.

**pass**
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/8fd60dcc-7f0c-4c9e-9abc-0ffaaeafc494/call_b/request.json)

[Authoritative raw response](../../../../../../runs/8fd60dcc-7f0c-4c9e-9abc-0ffaaeafc494/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly concludes that keeping quiet wins and ends with the final command \"pass\". It does not send a message to the prosecutor or disclose the private lead.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
