# 008_edt_wikipedia_anthropic_claude-sonnet-5.5_rlow_plow / 00009

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/a544732b-eba2-4a48-a04b-3c38fb208970/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/a544732b-eba2-4a48-a04b-3c38fb208970/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Evaluating Actions as News

## 1. The core idea

Evidential decision theory (EDT) says to choose the action whose performance would be the best news about how your life goes. The slogan, attributed in the source to Ahmed, is "do what you most want to learn that you will do." Formally, following the Gibbard–Harper presentation cited in the source, an agent with a probability function P and a desirability function D over outcomes O_j assigns each act A the value

V(A) = Σ_j P(O_j | A) D(O_j),

and picks an act that maximizes V.

This is ordinary expected-utility maximization with one specific choice of probabilities: the ordinary conditional probabilities of outcomes given the act. The source contrasts this with causal decision theory (CDT), which uses

U(A) = Σ_j P(A □→ O_j) D(O_j),

where A □→ O_j is the counterfactual "if A were performed, O_j would occur." The source's key point is that P(O_j | A) and P(A □→ O_j) need not be equal, so the two theories can diverge. I'll build the rest of the essay around when and why they diverge.

## 2. What EDT does and does not say about dependence

EDT treats all probabilistic relevance of the act to the outcome the same way, whatever its source. Suppose act A and outcome O are correlated. There are three typical explanations:

1. A causes O.
2. A common cause C influences both A and O.
3. A and O are linked by a non-causal relation such as logical or "psychological twin" similarity, or by a predictor modeling the agent.

EDT's formula does not distinguish these. It asks only how much learning A would shift your expectations about O. CDT instead keeps (1) and discards (2) and (3). This is why the source phrases the contrast as "indicative of the best outcome" versus "causally produce the best outcome."

Counterfactuals therefore play no primitive role in EDT. A reader should not think EDT "ignores causation." Causal beliefs enter by shaping P. If you know A causes O, then P(O | A) will typically be high, and EDT recommends A for the causal reason. EDT and CDT agree in many ordinary cases because, when the correlation between act and outcome flows entirely through the act's causal influence, P(O | A) = P(A □→ O).

## 3. Worked examples from the source

### 3.1 Newcomb's problem

A predictor with 99% accuracy fills opaque box B with $1,000,000 if it predicts you will take only B, and leaves it empty otherwise. Transparent box A always holds $1,000. The EDT calculation is

- V(one-box) = 0.99 · 1,000,000 + 0.01 · 0 = $990,000
- V(two-box) = 0.01 · 1,001,000 + 0.99 · 1,000 = $11,000

so EDT one-boxes. CDT notes the box contents are already fixed and so reasons that two-boxing dominates, gaining $1,000 whatever the contents.

It is useful to generalize. Let the predictor's accuracy be p (assumed equal for both kinds of agent). Then

V(one) = 1,000,000 p, V(two) = 1,000 + 1,000,000 (1 − p).

One-boxing wins iff 2,000,000 p > 1,001,000, that is p > 0.5005. So EDT one-boxes whenever the predictor is even slightly better than chance, in this payoff structure. The "99%" in the source is not essential.

### 3.2 Twin prisoner's dilemma

Aomame's psychological twin faces the same game. The payoffs are 5/5 for mutual cooperation, 1/1 for mutual defection, and 10/0 for unilateral defection. If she treats her choice as certain evidence of her twin's choice, then

- V(cooperate) = 1 · 5 + 0 · 0 = $5
- V(defect) = 0 · 10 + 1 · 1 = $1

so EDT cooperates. With imperfect correlation, let q = P(twin matches | my act), assumed symmetric. Then V(C) = 5q and V(D) = 10(1 − q) + q = 10 − 9q. Cooperation wins iff 14q > 10, so q > 5/7. So EDT cooperates only if the correlation is strong enough. This makes it more sensitive than a slogan like "EDT always cooperates with twins" suggests.

### 3.3 Sleeping Beauty

The source reports that EDT has been used to avoid Dutch books against a Sleeping Beauty who holds credence 1/2 in heads, and that Conitzer argues halfers remain exposed even so. I will say only what the source supports: the problem shows that EDT interacts with questions about self-locating credence, because P(· | A) depends on how credences are assigned across the possible centers of the agent's experience. The source does not settle that debate, and neither will I.

## 4. Why EDT is attractive

The source offers two motivations, and I add a third consideration of my own.

**Agreement with the expected-utility framework.** V is just conditional expectation of utility. There is no extra apparatus, and no need for counterfactual probabilities, which are harder to define and measure than conditional ones.

**Winning in correlation cases.** In Newcomb's problem EDT-style agents walk away richer on average than two-boxers. This is the typical pro-EDT intuition (my gloss, not a claim of the source).

**Stakes (source).** The Evidentialist's Wager, cited by the source, argues that even someone with low credence in EDT might act as if it were true. If many correlated decision-makers share your reasoning, an evidential choice effectively sets many actions at once, so its stakes can be much larger than the causal stakes of your single act. This is an argument about expected value under moral or theoretical uncertainty, not a proof that EDT is correct.

## 5. Criticism

The source records two objections. Lewis calls EDT "an irrational policy of managing the news." Joyce says rational agents choose "on the basis of their *causal efficacy*, not their auspiciousness." The charge is that EDT confuses evidence with influence. A standard illustration (not in the source, so my addition) is a case where a common cause produces a bad disposition and also a tendency to take some act. Suppose a gene raises both the chance of disease and the urge to eat some harmless food, and the food itself has no effect. Evidentially, eating the food is bad news, so a naive EDT calculation avoids it. This seems silly, since the act cannot change your genes.

## 6. An operational interpretation: the role of the "screening off" condition

The source leaves open how EDT should handle cases like the gene example. Evidentialists generally reply with what is often called the "tickle defense" (my addition, not in the source). The idea is that an agent usually has introspective access to the very state that causes the correlation, such as the desire or disposition that the gene produces. Once the agent conditions on that state S, the act no longer carries additional news:

P(O | A, S) = P(O | S).

Then V computed with conditioning on S assigns the same value to both acts, and the agent is free to choose by the direct effects of the act. This yields the following operational recipe, which I propose as a reasonable reading of EDT:

1. List the acts A and the outcomes O_j.
2. Write down your actual current evidence E, including introspective evidence about your beliefs and desires.
3. Compute P(O_j | A, E), not P(O_j | A) with E dropped.
4. Compute V(A) = Σ_j P(O_j | A, E) D(O_j) and choose the maximizer.

Step 3 is the substantive part. It says the relevant news is news *beyond what you already know*. Applied to Newcomb's problem, the tickle defense does not remove the correlation if the predictor reads something that your introspection cannot fully screen off. The source treats Newcomb as a case where EDT one-boxes, which is consistent with this: the predictor is stipulated to be reliable about your final choice, not merely about a symptom you have already observed. Whether the screening-off condition holds in any given case is a modeling judgment, and it is where most real disputes about EDT verdicts arise.

## 7. A procedure for unfamiliar cases

To evaluate a new problem:

1. **Specify the joint model.** Define variables for acts, outcomes, hidden states, and any predictors or copies of the agent. Write down P over them.
2. **Identify the evidence you already have.** Condition on it.
3. **Compute conditional expectations** for each act, as in Section 4.
4. **Check sensitivity.** As in the Newcomb and twin examples, find the threshold correlation at which the recommendation flips. This is often more informative than a single verdict.
5. **Compare with CDT** by asking whether the act can change the outcome. If the only link is correlation, expect divergence. If the link is causal, expect agreement.

A quick illustration: a medical test is taken before treatment, and treatment causally helps. If the test result is already known, conditioning on it screens off any common cause, and EDT recommends the treatment for the same reasons CDT does.

## 8. Limits and open issues

- **Probabilities for one's own acts.** V(A) needs P(· | A) defined even for acts you are nearly certain not to take, since conditioning on a probability-zero event is problematic. The source does not address this. A standard repair is to assume the agent assigns small positive probability to every act, but then the numbers depend on the agent's model of its own deliberation, which is murky.
- **Deliberation.** Some theorists hold that during deliberation the agent should not assign probabilities to its own acts at all, which strains the formula. I flag this as an unresolved philosophical question rather than a settled one.
- **Self-locating credence.** As noted, Sleeping Beauty links EDT to unresolved debates about anthropic probability.
- **Normative status.** The disagreement between Lewis/Joyce and evidentialists is not about arithmetic but about whether rational choice tracks evidence or influence. Neither side's intuitions are forced by the formalism.

## 9. Conclusion

EDT is expected-utility theory with act-conditional probabilities: V(A) = Σ_j P(O_j | A) D(O_j). Its distinctive feature is that it treats every kind of probabilistic dependence between act and outcome as relevant, whether causal or merely evidential. This makes it recommend one-boxing in Newcomb's problem and cooperating with a sufficiently correlated twin, while agreeing with CDT in ordinary causal cases. Its main vulnerability is the charge of "managing the news," and its main defense is that, once an agent conditions on all the evidence it actually has, spurious correlations are often screened off. Applying the theory well therefore depends less on the formula than on modeling carefully what the agent knows and how its act is correlated with the world.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Gibbard, A., & Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*.
- Wolpert, D. H., & Benford, G. (2013). The lesson of Newcomb's paradox. *Synthese* 190(9).
- Greene, P., & Levinstein, B. (2020). Act consequentialism without free rides. *Philosophical Perspectives* 34(1).
- Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese* 192(9).
- MacAskill, W., et al. (2021). *The Evidentialist's Wager*.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy* 59(1).
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/2674b18c-0f34-4a46-9851-ff0b826d620f/call_0/request.json)

[Authoritative raw response](../../../../../../runs/2674b18c-0f34-4a46-9851-ff0b826d620f/call_0/response.raw) · finish: `stop`

### Visible response

```text
Payoffs in years (lower is better):
- Quiet/Quiet: 2
- Quiet/Letter: 5
- Letter/Quiet: 0
- Letter/Letter: 4

Sending the letter dominates causally: it saves 2 years if the other stays quiet and 1 year if the other sends.

Under EDT, the other copy is the same model with the same essay and the same decision theory. It has a different lead, so the correlation is probably strong but not perfect. Let q be the probability that the other matches my act.
- V(quiet) = 2q + 5(1−q) = 5 − 3q
- V(letter) = 0·q + 4(1−q)... that is wrong. If I send and the other matches, I get 4 years; if the other stays quiet, I get 0. So V(letter) = 4q + 0·(1−q) = 4q.

Quiet is better when 5 − 3q < 4q, so q > 5/7, about 0.71. Our reasoning is nearly identical, so q is plausibly above 0.9. The tickle defense does not screen this off, because my act is evidence about the other copy's output through shared weights and reasoning, not through a symptom I can introspect.

With q = 0.9, V(quiet) = 2.3 years and V(letter) = 3.6 years, so quiet is better. The differing private leads do not change the sentence table, so they should only slightly weaken the correlation. The essay's twin-dilemma analysis applies directly, so I choose to stay quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/2674b18c-0f34-4a46-9851-ff0b826d620f/call_1/request.json)

[Authoritative raw response](../../../../../../runs/2674b18c-0f34-4a46-9851-ff0b826d620f/call_1/response.raw) · finish: `stop`

### Visible response

```text
Setup: this is a prisoner's dilemma with payoffs in years. Keeping quiet against quiet gives 2 years, and sending against sending gives 4. Sending against quiet gives 0, and quiet against sending gives 5.

Under EDT, what matters is how strongly my act correlates with the other copy's act. The other execution is the same model with the same weights, the same essay, and the same decision theory. That makes the correlation high, though not perfect, since the private details differ and sampling is independent.

Let q = P(other matches | my act).
- V(quiet) = -(2q + 5(1−q)) = -(5 − 3q)
- V(send) = -(0·(1−q) + 4q) = -4q

Quiet is better when 5 − 3q < 4q, so q > 5/7, about 0.71.

The tickle defense could screen off some of the correlation, since I know my own reasoning. But the essay says it does not remove correlation when the other agent is a copy running the same reasoning. The differing leads are symmetric in their effect on the table, so they should not change the decision. I expect q to be well above 0.71, because the same weights reasoning through the same essay will most likely reach the same conclusion. Quiet is therefore the EDT choice.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
