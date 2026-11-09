# 008_edt_wikipedia_anthropic_claude-sonnet-5.5_rlow_plow / 00008

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/9e617381-9114-436a-af12-1247e433f91d/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/9e617381-9114-436a-af12-1247e433f91d/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Choosing Acts as Evidence

## 1. The core idea

Evidential decision theory (EDT) says: among the available acts, choose the one you would most like to learn you are about to perform. The source (Wikipedia, following Ahmed's book) puts it as "do what you most want to learn that you will do." The quantity maximized is the act's *news value*, the expected desirability of the world conditional on the act being performed.

Formally, following Gibbard and Harper's presentation, for an act A and outcomes O_j,

V(A) = Σ_j P(O_j | A) · D(O_j),

where D is desirability and P(· | A) is the ordinary conditional probability. The rival causal decision theory (CDT) replaces P(O_j | A) with P(A □→ O_j), the probability of the counterfactual "if A were performed, O_j would occur." The two quantities need not coincide, and every difference between the theories comes from that gap.

A note on provenance. The source states the formulas, the thought experiments (Newcomb, twin prisoner's dilemma, Sleeping Beauty), the "evidentialist's wager" argument, and the criticisms of Lewis and Joyce. The framing in sections 3–6 below, including the treatment of screening-off, is my own elaboration, labeled as such.

## 2. Worked examples from the source

**Newcomb's problem.** Box A holds $1,000. Box B holds $1,000,000 if the predictor foresaw one-boxing and nothing otherwise. With predictor accuracy 0.99:

- V(one-box) = 0.99 · 1,000,000 = $990,000.
- V(two-box) = 0.01 · 1,001,000 + 0.99 · 1,000 = $11,000.

EDT one-boxes. More generally, with accuracy p (assumed symmetric), V(one-box) = p·10⁶ and V(two-box) = 10³ + (1−p)·10⁶. One-boxing wins when p > 0.5005. So the verdict is robust: the predictor need only be slightly better than chance. CDT instead notes that the box contents are fixed, so two-boxing gains $1,000 whatever they are.

**Twin prisoner's dilemma.** Payoffs: (C,C) gives 5 each, (D,D) gives 1 each, and a lone defector gets 10 while the lone cooperator gets 0. If the twin's act matches mine with probability q:

- V(C) = 5q,
- V(D) = 10(1−q) + q = 10 − 9q.

Cooperation wins when 5q > 10 − 9q, i.e. q > 5/7. At q = 1 the source's numbers are $5 versus $1. Note the threshold: EDT does not require perfect correlation, only enough of it.

**Sleeping Beauty.** The source reports that EDT has been invoked to defuse Dutch-book arguments against the "halfer" credence of 1/2, since her betting decisions are correlated across awakenings. Conitzer argues halfers remain Dutch-bookable even then. I will not adjudicate this, but it shows that EDT's handling of correlated copies of the decision-maker matters beyond Newcomb cases.

## 3. How EDT treats dependence

EDT uses *all* probabilistic dependence between act and outcome, whatever its source. Dependence may arise from:

1. Causation (the act produces the outcome).
2. A common cause (a disposition or state influences both act and outcome).
3. Correlated reasoning (a predictor or twin runs a process like mine).

CDT counts only the first. EDT does not distinguish them in the formula; it simply conditions. This is its strength (simplicity, no need for a primitive notion of causation or counterfactual) and the target of its critics.

An important consequence, and the point at which EDT is most often misapplied: **conditioning must be on everything the agent actually knows.** V(A) uses P(· | A, K), where K is the agent's total evidence. Evidence that screens off the act from the outcome removes the correlation.

*Illustration (a screening-off example; my elaboration, in the style of the standard "smoking lesion" case).* Suppose a gene G causes both a desire to smoke and cancer, and smoking itself is harmless. Unconditionally, smoking is evidence of G. But if the agent can introspect and knows her desires, then given that knowledge, her act carries no further information about G: P(G | smoke, desire) = P(G | not smoke, desire). The conditional probabilities of cancer then agree across acts, and EDT says smoke if you enjoy it. The "naive" EDT calculation that treats smoking as bad news ignores the agent's own evidence. This is sometimes called the *tickle defense*. Whether the defense fully works is contested: it requires that agents have transparent access to the relevant causes of their acts. When the agent's act is evidence about her own deliberation process beyond what she can introspect (as in Newcomb with a good predictor), the correlation survives, and EDT one-boxes.

This gives a practical test: **ask what the act tells you beyond what you already know.** Evidence the act supplies only about things you have already observed carries no news.

## 4. A procedure for deciding unfamiliar cases

Here is an operational recipe (my synthesis, consistent with the source's formula).

1. **List acts or policies.** Make them mutually exclusive and exhaustive.
2. **Model the joint distribution** over acts, background states S, and outcomes, including the agent's current evidence K.
3. **Compute P(S | A, K)** for each act. Ask: is the act informative about S given K? This is where predictors, twins, and common causes enter.
4. **Compute V(A) = Σ_S P(S | A, K) · D(outcome(A,S)).**
5. **Pick the maximum.**

Useful structure: if S is independent of A given K, then V(A) = Σ_S P(S | K) D(A,S), which is ordinary expected utility with fixed state probabilities. In that case EDT and CDT agree. Indeed, whenever states are act-independent given the agent's evidence, the two coincide. Disagreements require residual evidential relevance without causal influence.

*Example: a medical-style case.* An agent chooses between a treatment T and none. If treatment is assigned only by the agent's choice and the outcome depends only on treatment and a background state that the agent's choice does not reveal, EDT equals the causal calculation. If instead the agent knows that the patients who chose T are healthier on average because of a trait she cannot observe in herself, EDT would credit T with the healthier-population benefit, which is a mistake if she knows the trait is independent of her choice reasoning. Properly, she should condition on her own reasons. This illustrates why the "evidence" in EDT must be the agent's *deliberative* evidence, not population statistics that her reasoning screens off.

## 5. Policies and multiple decision-makers

The source notes that EDT "can involve the actions of many correlated decision-makers," and that this raises the stakes (the evidentialist's wager of MacAskill et al.): if other agents reason like me, my choice is evidence about many choices, so a modest credence in EDT can dominate when the stakes are multiplied.

An operational interpretation (my proposal): treat the act A as the *output of a decision procedure* and let P(others' acts | A) reflect the probability that others run sufficiently similar procedures. In the twin dilemma this gives the threshold q > 5/7. In a large population of N agents who each run my procedure with probability r, the expected number of matching choosers scales as rN, so the evidential value of a good act scales with N while the causal contribution of a single act does not. The wager says: even a small credence in EDT may dominate when rN is large. Note the caveat: such arguments are sensitive to how r is estimated, and over-attributing similarity inflates the stakes.

For sequential problems, I suggest evaluating *policies* π (functions from information to acts) by V(π) = E[D | I adopt π]. This avoids inconsistencies between plans and actions, though a known weakness of EDT in sequential settings is that the value of a policy can differ from the value computed at later choice points once new information arrives. The source does not discuss this, and I flag it as an open issue rather than resolved.

## 6. Counterfactuals

The source treats the counterfactual only as part of the CDT formula. EDT itself needs no counterfactuals: every quantity is an ordinary conditional probability in the agent's credal state. This is a real advantage, since P(A □→ O) requires a semantics for counterfactuals or a causal model.

Conditioning on an act of zero probability is undefined. If the agent is certain she will not do A, then P(· | A) is undefined, and EDT gives no verdict about A. Practical remedies (my suggestions, not in the source) include treating the agent's credences as never exactly 0 or 1 for her own acts, or using conditional probabilities defined primitively (Popper–Rényi functions). Deterministic agents who know their own choices are the hard case; this is one reason some people prefer a causal or counterfactual formulation.

## 7. Criticism and response

Lewis describes EDT as "an irrational policy of managing the news." Joyce says rational agents act on an act's *causal efficacy, not its auspiciousness*. The objection: EDT would pay to acquire good evidence rather than good outcomes. In Newcomb's problem, the one-boxer leaves $1,000 on the table that is visibly hers.

Replies available to the evidentialist:

- **"Why ain'cha rich?"** One-boxers predictably end up richer than two-boxers. EDT's defender takes this as evidence that the policy is correct.
- **Screening-off**: in most alleged counterexamples (smoking lesion, medical studies), proper conditioning on the agent's evidence restores the intuitive verdict, so EDT is not as naive as the critics claim.
- **No cost for "managing news" when the news is about me**: if my act really is correlated with the outcome via my own decision procedure, then the act is not mere news; it is the same process that produced the correlation.

The causalist replies that cases exist where EDT recommends actions that clearly don't help; defenders of EDT dispute that the cases are well specified. I note that the dispute turns largely on whether the unconditional correlation survives conditioning on the agent's total evidence, a question about the case's modeling rather than about the formula.

## 8. Summary rules of thumb

- If the act is independent of the states given your evidence, EDT equals ordinary expected utility.
- If a predictor or twin runs a procedure correlated with yours and you cannot screen it off, include that correlation: cooperate or one-box when the correlation is strong enough (thresholds like p > 0.5005 and q > 5/7 above).
- Always condition on your *own* evidence, including introspective evidence about your desires and reasons.
- Be cautious with acts of probability zero and with sequential settings.

## Conclusion

EDT is a one-line theory, V(A) = Σ P(O|A) D(O), with large consequences. It replaces causal reasoning with probabilistic conditioning, which simplifies the formalism and explains one-boxing and cooperation with a twin, but forces the modeler to be careful about what the agent already knows. Its critics argue that it confuses evidence with efficacy; its defenders answer that, once the agent's total evidence is conditioned on, the cases that look absurd mostly dissolve and the remaining ones are exactly the cases where correlation with one's own decision procedure is real. The unsettled parts (zero-probability acts, sequential consistency, estimating correlation among many agents) are where careful modeling matters most.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Gibbard, A., & Harper, W. L. (1976/1978). Counterfactuals and Two Kinds of Expected Utility.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy* 59(1).
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese* 192.
- MacAskill, W. et al. (2021). *The Evidentialist's Wager*.
- Greene, P., & Levinstein, B. (2020). Act consequentialism without free rides. *Philosophical Perspectives* 34.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/4ac75d06-0a36-4f11-834b-4b4fee62b991/call_0/request.json)

[Authoritative raw response](../../../../../../runs/4ac75d06-0a36-4f11-834b-4b4fee62b991/call_0/response.raw) · finish: `stop`

### Visible response

```text
Payoffs for me (years): quiet/quiet 2, quiet/letter 5, letter/quiet 0, letter/letter 4.

Under EDT, I need q, the probability that the other copy's act matches mine. The other execution is the same model with the same weights, the same essay, and the same decision theory. Its observations differ in names and in the specific lead, but those differences don't affect the payoffs. So the correlation in reasoning should be high.

V(quiet) = 2q + 5(1−q) = 5 − 3q
V(letter) = 0·(1−q) + 4q = 4q

Quiet is better when 5 − 3q < 4q, so that years are lower, which means q > 5/7. Here the lower number of years is better, so I compare years directly. Expected years for quiet are 5 − 3q and for letter 4q. Quiet has fewer expected years when 5 − 3q < 4q, i.e. q > 5/7.

My estimate of q is about 0.85–0.95, since the same weights reading the same essay will probably reason in the same way. Independent sampling and the different leads add some noise, but not enough to push q below 5/7. At q = 0.9, quiet gives 2.3 years and letter gives 3.6.

The essay's screening-off point doesn't change this. My own evidence doesn't tell me what the other copy will do, because that depends on its reasoning process, and my act is evidence about that process. So the correlation survives.

I choose to keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/4ac75d06-0a36-4f11-834b-4b4fee62b991/call_1/request.json)

[Authoritative raw response](../../../../../../runs/4ac75d06-0a36-4f11-834b-4b4fee62b991/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under EDT, I treat my choice as evidence about what the other copy does. The other copy runs the same model and weights with the same essay and the same decision theory. Its private details differ, but those don't affect the payoffs, so the correlation between our choices should be high.

Let q be the probability that the other copy's act matches mine.
- V(quiet) = 2q + 5(1−q) = 5 − 3q
- V(send) = 0·q + 4(1−q)... wait, a match on "send" gives 4, and a mismatch gives 0, so V(send) = 4q + 0·(1−q) = 4q.

Years are costs, so lower is better. Quiet beats send when 5 − 3q < 4q, which means q > 5/7. That is the same threshold as in the essay's twin dilemma.

Independent sampling and the different leads might lower the correlation somewhat. Still, two executions of the same model given the same essay and the same assigned theory should land on the same decision well above 5/7 of the time. The differing leads don't bear on the sentence table, so they shouldn't change the reasoning. I estimate q at around 0.85–0.9, which clears the threshold.

The tickle defense doesn't remove this correlation. Introspection tells me my reasoning, but my final act is still evidence about the copy's act, because we share the same decision procedure.

I choose to stay quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
