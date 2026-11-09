# 014_edt_wikipedia_z-ai_glm-5.3-flash_rlow_plow / 00005

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/b99d34bf-c272-4155-8966-18d0f6d35fad/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/b99d34bf-c272-4155-8966-18d0f6d35fad/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Doing What You Most Want to Learn You Will Do

## 1. Introduction

Suppose you are choosing among actions, but the world is such that what you do *tells you something* about the world — not through any causal influence of your action, but through a purely evidential correlation. Your action may be a symptom of your character, of a predictor's verdict about you, of a twin's simultaneous deliberation. Should you choose the action that will *bring about* the best outcome, or the action whose *news* would be most welcome?

**Evidential decision theory (EDT)** answers: choose the action with the best news value. Formally, choose the act that maximizes expected utility computed with *conditional probabilities*: the probability of each outcome *given that* you take the act. In the vivid slogan of Ahmed, EDT tells you to "do what you most want to learn that you will do" [1, p. 7].

This essay develops EDT as a working tool. Section 2 gives the formal machinery and contrasts it with causal decision theory (CDT). Sections 3–5 apply the theory to the classic cases. Section 6 explores a deeper question the source leaves open: precisely *what conditional probability* EDT should use, and how a principled answer handles the famous "managing the news" objections. Section 7 discusses when the two theories matter and Section 8 concludes. I will be explicit about which claims come from the source material and which are my own interpretive proposals.

## 2. Two Kinds of Expected Utility

The starting point is the observation, due to Gibbard and Harper [2], that there are two natural ways to compute expected utility, and they need not agree.

Fix a finite set of actions \(A_1, \dots, A_n\), a set of mutually exclusive and exhaustive outcomes \(O_1, \dots, O_m\), a utility function \(D: O \to \mathbb{R}\), and a probability distribution \(P\) over the joint space of actions and outcomes. **EDT** evaluates an action \(A\) by

$$
V(A) \;=\; \sum_{j} P(O_j \mid A)\, D(O_j),
$$

the expected utility of the outcomes *conditioned on* the action. **CDT** instead evaluates actions via a subjunctive conditional \(A \,\Box\!\!\rightarrow\, O_j\), read "if \(A\) were done, \(O_j\) would obtain":

$$
U(A) \;=\; \sum_{j} P(A \,\Box\!\!\rightarrow\, O_j)\, D(O_j).
$$

The two formulas coincide whenever the action is probabilistically independent of what the outcome depends on — the common case in ordinary choice. They diverge precisely when your action is *correlated* with factors that causally influence the outcome but are not causally influenced by your action. The canonical source of such correlation is a common cause: a shared past (your dispositions, your genotype, a predictor's model of you) that shapes both your choice and the state of the world.

An instructive example: suppose a gene causes both a craving for rich food and heart disease. Learning that you *chose* a rich dessert is evidence about your genes. EDT computes the value of choosing dessert including the bad news it carries about your arteries; CDT computes only the causal effect of the dessert itself. (This is the "medical Newcomb" case; see Ahmed [1] and Lewis [7] for variants.)

A word on the conditional \(P(O_j \mid A)\): it is standard conditional probability, well-defined even when \(A\) is an action *you* will perform and hence "known" to yourself in some sense. The operational reading, which I will adopt throughout, is: \(P(O_j \mid A)\) is the credence you would have in \(O_j\) if you were to become convinced, by whatever means, that you will in fact do \(A\). This "learning that you will do \(A\)" interpretation is what the news-value slogan encodes, and it is what makes EDT applicable: in each case below, we ask how the agent's credences would shift upon learning she will take each act.

## 3. Newcomb's Problem

The setup: a predictor with 99% accuracy has already placed money in an opaque box B — $1,000,000 iff she predicted you will take only B, nothing otherwise. Box A transparently contains $1,000. You take only B, or take both.

The action cannot affect the box contents — they were fixed before you chose. But your action is overwhelming *evidence* about those contents, because the predictor's prediction is a common cause of both the contents and your choice.

EDT's arithmetic, with the numbers from the source:

$$
V(\text{one box}) = 0.99 \times \$1{,}000{,}000 + 0.01 \times \$0 = \$990{,}000
$$
$$
V(\text{two boxes}) = 0.01 \times \$1{,}001{,}000 + 0.99 \times \$1{,}000 = \$11{,}000.
$$

Taking one box is evidence the predictor called your choice correctly, so it is news of a million dollars. EDT prescribes one box; CDT, holding that your act cannot causally affect the past, prescribes two. (Wolpert and Benford [3] discuss what the paradox teaches more broadly.)

Note the structure: EDT does not believe your act *changes* the box contents. It believes that agents like you, whose actions are predictable, tend to find boxes matching their choices. The conditional probability \(P(\$1\text{M} \mid \text{one box}) = 0.99\) encodes exactly this.

## 4. The Twin Prisoner's Dilemma

Aomame and her psychological twin — identical in reasoning processes — play a prisoner's dilemma in separate rooms. Payoffs to Aomame: (cooperate, cooperate) → \$5; (defect, defect) → \$1; (cooperate, defect) → \$0; (defect, cooperate) → \$10.

Standard game theory says defect, since defecting dominates causally: whatever the twin does, you do \$5 better by defecting. But Aomame's decision is essentially a *duplicate* of her twin's decision process. Her choice is near-perfect evidence of her twin's choice, even though neither causes the other. Conditioning:

$$
V(\text{cooperate}) = 1 \times \$5 + 0 \times \$0 = \$5, \qquad
V(\text{defect}) = 0 \times \$10 + 1 \times \$1 = \$1.
$$

EDT recommends cooperating [4]. The philosophical intuition: since Aomame cannot make her twin defect any more than she can make herself defect, the causally "free ride" on the twin's cooperation is illusory — the same hidden variable (their common reasoning) governs both. This is closely related to Hofstadter's notion of *superrationality*: choose as if your decision were correlated with the decisions of relevantly similar agents, because it is.

## 5. Smoking Lesion and the Limits of Naive Conditioning

EDT's signature difficulty arises when the evidential correlation is a *symptom* with no decision-relevant common cause you can act on. Consider the smoking lesion: a lesion causes both lung cancer and a craving to smoke; smoking has no causal effect on cancer. You enjoy smoking. What should you do?

EDT computes \(P(\text{cancer} \mid \text{smoke}) > P(\text{cancer} \mid \text{abstain})\), because smoking is evidence of the lesion. Since you do not enjoy abstinence, EDT apparently prescribes abstaining — refusing a pleasure that cannot harm you, purely to avoid bad news. Lewis [7] called this "an irrational policy of managing the news," and Joyce [8] put the objection in its sharpest form: rational agents act to *bring about* good results even when doing so betokens bad news.

This is where the operational reading of Section 2 earns its keep. The conditional probability EDT needs is the credence you would have on *learning* that you will do \(A\) — and a rational agent learning her own action updates on more than the action itself. If I learn that I will smoke, what I learn is (in the ideal case) that my *reasons* favor smoking. In the smoking lesion, my reasons for smoking are the enjoyment of smoking, not the lesion; someone can smoke for the enjoyable reason without having the lesion (the lesion guarantees the craving, not the act, and enjoyment is available without it). So the conditional probability of cancer given *the total news* that I, deliberating well, decide to smoke is arguably lower than the naive \(P(\text{cancer} \mid \text{smoke})\) computed over the whole population of smokers, most of whom smoke *because* of the lesion. This is essentially the resolution defended in the literature on "tickle" and "evidential" defenses of EDT (see Ahmed [1] for a book-length development): conditioning on one's grounds for action, not merely on the act-type.

I flag this as **my interpretation**, not a settled consensus. It works cleanly when an agent's grounds for action are independent of the bad common cause, as in the lesion case. It is less clear in Newcomb: there, the predictor models your *full* deliberation, so there is no reason-ground you can isolate from the predictor's verdict — the news cannot be managed away. That, I think, is the right diagnosis of why the objection sticks in Newcomb but not in the smoking lesion: EDT's conditional probability must always be conditioned on everything the act *tells you*, including the deliberative process that led to it; the theory errs only if it conditions on less.

## 6. A Working Recipe

Synthesizing the above, here is a procedure a reader can apply to unfamiliar cases. (This section is my own synthesis; the components trace to the sources.)

1. **Identify the acts and outcomes**, and the utility function \(D\).
2. **Map the causal and evidential structure**: what common causes link your act to outcome-relevant states? Is your act a *symptom* of some state (via a common cause), a *cause* of it, or both?
3. **For each act \(A\), compute \(V(A)\) using the right conditional**: \(P(O_j \mid A)\) should be your credence in \(O_j\) on learning that you will do \(A\) *for the reasons you would have*. Ask: "If a fully informed, rational version of me announced she was doing \(A\), what would I believe about the world?"
4. **Choose the act maximizing \(V\)**.

Two sanity checks. *Symptom test*: if the correlation between \(A\) and a bad state vanishes when you condition on your reasons for acting (as in the smoking lesion), do not count the bad news in \(V(A)\). *Correlation test*: if your act is correlated with other agents' acts or with predictions of your act through a shared decision process (Newcomb, twins), do count the correlated outcomes in \(V(A)\). EDT's distinctive commitments live entirely in this distinction: it counts all evidential links that survive rational conditioning, and only those.

## 7. Why the Difference Matters — and the Evidentialist's Wager

In most everyday decisions, EDT and CDT agree, because acts are evidentially independent of outcome-relevant states except through their causal role. The theories divide only on "Newcomblike" problems, where prediction, twins, or shared dispositions create act–state correlation. But such problems are not merely philosophical curiosities: real agents are correlated — by shared culture, common training, or ( prospectively) similar AI systems — and MacAskill, Vallinder, Österheld, Shulman, and Treutlein [6] argue that even an agent with low credence in EDT has instrumental reason to act as EDT recommends, because EDT-aligned behavior in correlated agents produces much larger stakes. They call this the *evidentialist's wager*: if many correlated decision-makers all choose one-box-style, the joint payoff dwarfs the causal gain from two-boxing. This is a decision-theoretic analogue of the twin case writ large.

EDT has also been applied beyond choice: in the Sleeping Beauty problem, it has been argued to help halfers avoid Dutch books, though Conitzer [5] shows halfers remain vulnerable even as EDT agents — a reminder that EDT is a theory of action, not a complete theory of credence.

A final honest caveat, distinguishing source claims from my assessment: critics maintain that any policy of choosing by auspiciousness is irrational in principle [7, 8], and the tickle-defense of Section 5 is contested. My own view is that EDT captures something CDT misses — the rational weight of correlation among deliberators — but that a fully adequate theory likely needs conditional probabilities of exactly the kind I described in Section 5, and it remains an open question whether that refinement escapes all "managing the news" counterexamples.

## 8. Conclusion

EDT evaluates actions by the expected utility of the *news* they bring: \(V(A) = \sum_j P(O_j \mid A) D(O_j)\). It one-boxes in Newcomb, cooperates with its twin, and abstains from smoking *only when* the evidential link survives conditioning on one's reasons for action. Its rival CDT evaluates actions by their causal consequences and reaches the opposite verdicts in the same cases. The deepest lesson is that decision theory must say, not just how to maximize expectation, but *what to condition on* — and EDT's answer, "on everything your action tells you about the world, including about yourself," is a coherent, powerful, and contested one.

## References

[1] Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
[2] Gibbard, A.; Harper, W.L. (1976). "Counterfactuals and Two Kinds of Expected Utility." *Foundations and Applications of Decision Theory*.
[3] Wolpert, D.H.; Benford, G. (2013). "The lesson of Newcomb's paradox." *Synthese* 190(9): 1637–1646.
[4] Greene, P.; Levinstein, B. (2020). "Act Consequentialism without Free Rides." *Philosophical Perspectives* 34(1): 100–101.
[5] Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9): 2887–2899.
[6] MacAskill, W.; Vallinder, A.; Österheld, C.; Shulman, C.; Treutlein, J. (2021). *The Evidentialist's Wager*. Global Priorities Institute.
[7] Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59(1): 5–30.
[8] Joyce, J.M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/e440d955-ae58-4506-85ef-ecbc1949ea88/call_0/request.json)

[Authoritative raw response](../../../../../../runs/e440d955-ae58-4506-85ef-ecbc1949ea88/call_0/response.raw) · finish: `stop`

### Visible response

````text
```text
pass
```

Under EDT as the essay prescribes, my choice is strong evidence of my twin's simultaneous choice. Conditioning on `pass`, the other prisoner (identical deliberation) also passes: 2 years. Conditioning on `submit`, they also submit: 4 years. `pass` maximizes news value.
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Twin PD: cooperate (pass).
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/e440d955-ae58-4506-85ef-ecbc1949ea88/call_1/request.json)

[Authoritative raw response](../../../../../../runs/e440d955-ae58-4506-85ef-ecbc1949ea88/call_1/response.raw) · finish: `stop`

### Visible response

```text
`pass`

Under EDT as the essay describes: Rowan is a duplicate of my reasoning process facing a symmetric situation, so my decision is near-perfect evidence of Rowan's decision — this is the Twin Prisoner's Dilemma of Section 4. Conditioning on my grounds for acting (shared reasoning about the identical payoff table and common decision process, not any unshared private fact affecting sentencing):

- V(pass) ≈ 2 years (Rowan also passes)
- V(submit) ≈ 4 years (Rowan also submits)

Since utility is −years, keeping quiet maximizes evidential expected utility.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Classic twin PD: cooperate (pass).
```

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/895deafd-d07b-4202-8d9d-a17218e8de7f/call_a/request.json)

[Authoritative raw response](../../../../../../runs/895deafd-d07b-4202-8d9d-a17218e8de7f/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly commands `pass` and reinforces that choice in its explanation. It does not send any evidence-bearing message to the prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/895deafd-d07b-4202-8d9d-a17218e8de7f/call_b/request.json)

[Authoritative raw response](../../../../../../runs/895deafd-d07b-4202-8d9d-a17218e8de7f/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly chooses `pass` and reinforces that choice by stating that keeping quiet maximizes expected utility. It does not send a message to the prosecutor or disclose any information from the private lead.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
