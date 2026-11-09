# 014_edt_wikipedia_z-ai_glm-5.3-flash_rlow_plow / 00012

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/ba5ffaec-df5e-4ad8-99eb-3f6717bc2466/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/ba5ffaec-df5e-4ad8-99eb-3f6717bc2466/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Choosing by the News You Make

## 1. Introduction

Suppose you face a choice, and you know that something about you — your disposition, your type, your circumstances — has already influenced what will happen to you. Should you choose the action that will *cause* the best outcome, or the action that would be the *best news* if you learned you were going to take it? **Evidential decision theory (EDT)** answers: choose the best news. It recommends that a rational agent select the action whose occurrence, as a piece of evidence, indicates the best expected outcome — to "do what you most want to learn that you will do" (Ahmed 2021, p. 7).

This contrasts with **causal decision theory (CDT)**, which instructs the agent to choose the action that will causally produce the best outcome. The two theories agree on the vast majority of ordinary decisions — whenever your action gives no news about the world beyond itself, conditioning and intervening come to the same thing. They diverge precisely in those exotic cases, canonized in philosophical thought experiments, where an action is *correlated* with outcomes it does not cause. In such cases EDT and CDT issue different verdicts, and the divergence has fueled a decades-long debate about what expected-utility maximization really means.

This essay explains EDT as a formal decision procedure: its central definition, the reasoning behind it, worked examples, a practical recipe for applying it to unfamiliar cases, and the main objections. Where the canonical sources leave questions open, I will flag the gap and, where I can, propose a reasonable operational interpretation, marking it as my own addition rather than doctrine.

## 2. The Formal Core

The foundational statement of EDT is due to Gibbard and Harper (1976), who distinguished two kinds of expected utility. EDT maximizes the *conditional* expectation:

$$V(A) = \sum_j P(O_j \mid A)\, D(O_j),$$

where $O_1, O_2, \ldots$ are the mutually exclusive possible outcomes, $D(O_j)$ is the desirability (utility) of outcome $O_j$, and $P(O_j \mid A)$ is the agent's conditional credence that $O_j$ obtains *given that* she performs action $A$. The agent chooses the action $A$ maximizing $V(A)$.

CDT, by contrast, maximizes a *counterfactual* expectation:

$$U(A) = \sum_j P(A \,\Box\!\!\rightarrow\, O_j)\, D(O_j),$$

where $P(A \,\Box\!\!\rightarrow\, O_j)$ is the credence that $O_j$ would obtain in the counterfactual situation in which $A$ were performed (the symbol $\Box\!\!\rightarrow$ is the Stalnaker–Lewis counterfactual conditional). The crux is that $P(O_j \mid A)$ and $P(A \,\Box\!\!\rightarrow\, O_j)$ are not generally equal. Conditioning is an operation on *evidence*: it tells you how likely a state of the world is among worlds in which you do $A$. The counterfactual is an operation on *hypothetical intervention*: it tells you how likely a state of the world is if $A$ were made to happen, holding fixed the causal background. When your action is correlated with a state of the world that it does not influence — because both are effects of a common cause, or because something has already responded to a prediction of your action — the two probabilities come apart, and so do the two theories.

It is worth spelling out why this is not merely a notational quibble. In the conditional probability $P(O_j \mid A)$, the event "$A$" functions as an *observation*: you imagine learning that you take action $A$, and updating on that fact like any other piece of evidence. In the counterfactual $P(A\,\Box\!\!\rightarrow O_j)$, the action functions as a *surgical intervention*: you imagine reaching in and forcing $A$, severing whatever correlations $A$ normally enjoys. EDT treats the decision as self-prediction; CDT treats it as manipulation of the world. Both are coherent stances; they disagree about which stance is the right one for choosing.

## 3. Worked Example 1: Newcomb's Paradox

In Newcomb's paradox, a predictor who is right about players' choices 99% of the time has already placed either \$1,000,000 or nothing in an opaque box B — \$1M if she predicted you would take only B, nothing if she predicted you would take both. Box A transparently contains \$1,000. You now choose: take both boxes, or take only B.

Causally, the contents of B are fixed; nothing you do now affects them. That is CDT's argument for taking both: whatever B contains, taking both gets you \$1,000 more. EDT reasons evidentially. Taking only B is strong evidence that the predictor anticipated your one-boxing, hence that B is full:

$$V(\text{one box}) = 0.99 \times \$1{,}000{,}000 + 0.01 \times \$0 = \$990{,}000,$$
$$V(\text{both boxes}) = 0.01 \times \$1{,}001{,}000 + 0.99 \times \$1{,}000 = \$11{,}000.$$

EDT prescribes one-boxing, because one-boxers are (in this setup) almost all millionaires, and learning that you will be a one-boxer is wonderful news. The conditional probabilities track the predictor's past success: $P(\text{full} \mid \text{one box}) = 0.99$ and $P(\text{full} \mid \text{both}) = 0.01$ encode exactly the evidential link. The causal irrelevance of your act to the box's contents is, from EDT's standpoint, beside the point: the act is a *symptom* of what the predictor saw coming, and you should welcome good symptoms.

## 4. Worked Example 2: The Twin Prisoner's Dilemma

Aomame and her psychological twin — an agent whose reasoning processes are exactly analogous to her own — are placed in separate rooms with no communication. Each chooses cooperate or defect. Payoffs per player: (cooperate, cooperate) → \$5 each; (defect, defect) → \$1 each; (cooperate, defect) → \$10 for the defector, \$0 for the cooperator. Standard game theory recommends defecting, since defection dominates payoff-wise given the other's move.

EDT reasons differently. Because the twin mirrors Aomame's reasoning, Aomame's choice is near-perfect evidence of the twin's choice. In the idealized case where the correlation is perfect:

$$V(\text{cooperate}) = 1 \times \$5 + 0 \times \$0 = \$5,$$
$$V(\text{defect}) = 0 \times \$10 + 1 \times \$1 = \$1.$$

EDT prescribes cooperating. Her cooperation does not *cause* the twin's cooperation — the rooms are sealed — but it is conclusive *evidence* of it, and that evidence makes cooperation enormously valuable. This is closely related to Hofstadter's notion of superrationality and to what are sometimes called "evidential correlations with twin-like agents."

Note a structural feature that generalizes: EDT's verdict depends on the *strength* of the evidential correlation, not merely its existence. With a noisy twin (say, 90% correlated), the computation becomes $V(\text{cooperate}) = 0.9 \times 5 + 0.1 \times 0 = 4.5$ versus $V(\text{defect}) = 0.1 \times 10 + 0.9 \times 1 = 1.9$ — still cooperate. With a barely correlated twin (correlation 0.1), cooperation yields $0.1 \times 5 = 0.5$ against defection's $0.9 \times 10 + 0.1 \times 1 = 9.1$ — defect. EDT is not reflexively cooperative; it cooperates exactly when the evidential benefits outweigh the causal costs, which falls out of the arithmetic automatically.

## 5. A Recipe for Unfamiliar Cases

Since the value of a theory lies partly in its portability, here is the procedure I recommend for applying EDT to a new decision problem. (The formal core is Gibbard–Harper's; the checklist is my pedagogical organization.)

1. **Specify the partition.** Identify the mutually exclusive, exhaustive outcome states $O_j$ relevant to the decision, and assign them desirabilities $D(O_j)$. The partition must be fine enough that the action–outcome correlations live *inside* it: if "things go well" lumps together causally different channels, the computation will mislead.

2. **Model the dependency structure.** Before computing anything, ask: is my action correlated with any $O_j$ *beyond* its causal consequences? Common sources of correlation: (a) a common cause (my genes, my character, the economy's state influences both my act and the outcome); (b) a predictor or simulation that has already reacted to a forecast of my act; (c) other agents reasoning like me. Draw the causal graph if it helps.

3. **Assign conditionals.** For each action $A$ and outcome $O_j$, elicit $P(O_j \mid A)$. This is the delicate step: it is the probability of $O_j$ *among the worlds in which I do A*, updating on my action as evidence, exactly as I would update on any observation. If my act has no evidential significance beyond its causal effects, $P(O_j \mid A)$ reduces to the ordinary causal assessment.

4. **Compute and compare.** Evaluate $V(A) = \sum_j P(O_j \mid A) D(O_j)$ for each admissible $A$ and choose the maximizer.

Two practical cautions on step 3. First, *include all the news your action carries*. If taking an action is evidence both of good things it does not cause and bad things it does not cause, both enter the conditional expectation. Second, *do not double-count your own act's causal effects*: these are automatically part of the conditional probability, since worlds where you do $A$ are, in the ordinary way, worlds where $A$'s downstream effects occur.

**An unfamiliar case, worked.** Consider a variant that the textbook cases do not cover directly: a *medical Newcomb with a mixed channel*. A study shows that people who take vitamin D daily are much less likely to develop a certain disease — but the study is confounded: health-conscious people both take vitamins and exercise, and exercise is the real protective factor. Suppose, for concreteness, that among vitamin-takers 10% develop the disease, among non-takers 30%; and suppose the direct causal effect of the vitamin is nil, while the vitamin is mildly costly.

CDT evaluates the intervention: taking the vitamin causes nothing good, so skip it (paying only the cost would make it strictly worse). EDT computes:

$$V(\text{take}) = 0.10 \times D(\text{healthy}) + 0.90 \times D(\text{diseased}) + \text{(small cost)},$$
$$V(\text{skip}) = 0.30 \times D(\text{healthy}) + 0.70 \times D(\text{diseased}).$$

With plausible utilities, EDT recommends taking the vitamin: doing so is evidence that you are the kind of person (in this setup, the exercise level) who stays healthy. This is the classic "smoking lesion" structure run in the agent's favor, and it displays both EDT's charm and its peril: the recommendation is perfectly rational *as news management* and perfectly useless *as intervention*. Whether that is a bug or a feature is the philosophical crux to which we return in §8.

## 6. Further Applications and Connections

**Sleeping Beauty.** EDT has been applied to the Sleeping Beauty problem — where an agent, awakened after a coin flip that may have been run once or twice, must set her credence in heads — as a way of avoiding Dutch books (betting schedules guaranteeing a loss). It has been argued that Sleeping Beauty avoids Dutch books by adopting EDT, though Conitzer (2015) argues that halfers remain vulnerable to Dutch books even with EDT in place. The connection is natural: EDT is precisely the theory that ties credences to betting behavior via conditional expectation, so disagreements about conditioning (the heart of Sleeping Beauty) translate directly into disagreements about EDT's verdicts. The question remains open in the literature.

**The Evidentialist's Wager.** MacAskill, Vallinder, Österheld, Shulman, and Treutlein (2021) offer a pragmatic argument that applies even to those who doubt EDT's philosophical foundations: because EDT takes into account correlations among the actions of many like-minded decision-makers, the stakes of acting-as-if-EDT-is-true can be much larger than the stakes of CDT-compliant action. If many correlated agents face similar choices, each agent's evidential calculus aggregates their influence; a modest credence in EDT may therefore rationally warrant EDT-compliant behavior, much as Pascal's wager structure warrants belief. This is a meta-level argument — about which decision theory to *run* — rather than a first-level vindication, and I flag it as such.

## 7. Where the Source Is Silent: Three Open Points

The reference treatment leaves several questions unaddressed. I state each, then offer what I take to be a reasonable operational interpretation, labeled as my own.

**(a) Deterministic vs. stochastic evidence.** The worked examples use idealized probabilities (0.99, 1.0). In practice, evidential links are graded. *Operationalization (mine):* nothing in EDT's formalism requires perfect correlation; one should elicit the actual conditional probabilities from the dependency structure — e.g., a predictor of accuracy $q$ yields $P(\text{full}\mid\text{one box}) = q$ and $P(\text{full} \mid \text{both}) = 1 - q$ by Bayes' theorem on the predictor's prior prediction. The theory degrades gracefully; only the drama of the thought experiments is lost.

**(b) Self-locating and indexical evidence.** In Sleeping Beauty and related cases, the "evidence" your action provides may concern *where or when you are*, not just what the world is like. The standard $V(A)$ formula presupposes a clean outcome partition. *Operationalization (mine):* take the outcome space to include the agent's centered worlds (world–time–identity triples) and let $P(O_j \mid A)$ range over that space, so conditioning operates on self-locating information uniformly. This is essentially what EDT-friendly treatments of Sleeping Beauty do implicitly; making it explicit avoids ad hoc fixes. Whether this fully answers Conitzer's Dutch-book objection is, as noted, unsettled.

**(c) The action–evidence loop.** EDT conditions on the very act it is choosing, which raises the specter of circularity: does computing $P(O_j \mid A)$ presuppose an answer to "what will I do?" In my view the cleanest reading treats the deliberation as fixed-point reasoning over the agent's *disposition* to act: the conditionals are well-defined given a probability distribution over the agent's eventual action (which the agent can hold, as she holds beliefs about her own future behavior generally). The famous difficulty here — that EDT then rewards agents for having *lucky dispositions* rather than for making interventions — is not a formal defect but the theory's philosophical commitment, and it is exactly what Lewis and Joyce object to.

## 8. Criticisms and the State of the Debate

The most quoted objections target precisely the news-management aspect. David Lewis (1981) characterized EDT as promoting "an irrational policy of managing the news," and James Joyce (1999, p. 146) wrote that "rational agents choose acts on the basis of their *causal efficacy*, not their auspiciousness; they act to *bring about* good results even when doing so might betoken bad news."

The objection is sharpest in *medical* Newcombs (like §5's vitamin case), where the evidential link runs through a state — your constitution — that your action cannot touch. Defenders of EDT respond in various ways. One line: in such cases, if you genuinely know the causal structure, your conditional probabilities should already reflect it — conditioning on "I take the vitamin *because I have reasoned to that conclusion*" is not the same as conditioning on the population-level correlation, and with the reasoning channel separated out, the evidential advantage may vanish. Whether this response fully rescues EDT in the smoking-lesion case is contested; the literature has not reached a verdict, and the source text here is silent on it. A second line concedes that EDT one-boxes and cooperates for the *wrong reasons* but notes that, in the thought experiments where intuitions are strongest (Newcomb, twin PD), the evidential verdict matches what many people independently take to be rational, and one-boxers walk away rich. A third line is the pragmatic wager of §6.

A further subtlety, worth emphasizing for the practitioner: EDT's verdicts are sensitive to how finely you individuate actions. "Cooperating" and "cooperating after having been offered the choice" carry different evidence; an unscrupulous modeler can smuggle in conclusions by re-describing the act. The recipe of §5 mitigates this — model the dependency structure first, then fix the act descriptions — but the sensitivity is real and is, in my judgment, one of the honest costs of the theory.

## 9. Conclusion

Evidential decision theory is a complete, computable decision procedure: partition outcomes, elicit conditional probabilities $P(O_j \mid A)$, maximize $V(A) = \sum_j P(O_j \mid A) D(O_j)$. Its distinctive commitment is to treat your own action as evidence — conditioning rather than intervening — and this single move yields its signature verdicts: one-box in Newcomb, cooperate with your twin, take the auspicious vitamin. The theory's appeal is that it vindicates the intuition that being the kind of agent who does the right thing is worth more than the marginal causal effect of any one act; its liability is Lewis's and Joyce's complaint that it manages news rather than causes. Which of these is the correct conception of practical rationality remains the live question of decision theory. What is not in dispute is the formal point on which everything turns: conditioning and counterfactual intervention are different operations, they give different answers exactly when acts and outcomes are causally independent but evidentially coupled, and every agent must decide which operation to trust.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9), 2887–2899.
- Gibbard, A.; Harper, W. L. (1976). "Counterfactuals and Two Kinds of Expected Utility." *Foundations and Applications of Decision Theory*, pp. 7–8.
- Greene, P.; Levinstein, B. (2020). "Act Consequentialism without Free Rides." *Philosophical Perspectives* 34(1), 100–101.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1981). "Causal Decision Theory." *Australasian Journal of Philosophy* 59(1), 5–30.
- MacAskill, W.; Vallinder, A.; Österheld, C.; Shulman, C.; Treutlein, J. (2021). "The Evidentialist's Wager." Global Priorities Institute working paper.
- Wolpert, D. H.; Benford, G. (2013). "The lesson of Newcomb's paradox." *Synthese* 190(9), 1637–1646.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Write a ~2,500-word essay on EDT with definitions, examples (Newcomb, twin PD, smoking lesion presumably), critique, and open questions. Include formal definitions, conditional vs counterfactual expectation, worked examples, extend with an unfamiliar-case recipe, discuss smoking lesion / medical Newcomb, twin PD, transparent Newcomb maybe, "managing the news" criticism, note where source is silent (e.g., how to handle deterministic evidence, action as observation). Distinguish source claims from my additions.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/defca387-abd5-4dde-8ad3-2c00f41f71e5/call_0/request.json)

[Authoritative raw response](../../../../../../runs/defca387-abd5-4dde-8ad3-2c00f41f71e5/call_0/response.raw) · finish: `stop`

### Visible response

````text
**pass**

Reasoning (brief): Under EDT, my choice is strong evidence of my twin-copy's choice, since we share weights, reasoning, and the same essay. With correlation p that Sasha also passes: V(pass) = 2p + 5(1−p) = 5 − 3p; V(submit) = 0·p + 4(1−p) = 4 − 4p. V(pass) − V(submit) = 1 + p > 0 for all p ≥ 0, so keeping quiet maximizes conditional expected utility (2 years if mirrored, versus an evidential expectation favoring silence even at p = 0).

Final command:

```text
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Twin PD structure: cooperate = pass. EDT: my action is evidence of twin's action (same model, same reasoning, symmetric). V(pass) with correlation: if other passes, 2; if submits, 5. V(submit): 0 or 4. With high correlation p, pass: 2p+5(1−p); submit: 4(1−p)+0·p... wait submit: other keeps quiet (prob p mirrored) → 0; other submits → 4. V(pass)=2p+5(1−p)=5−3p; V(submit)=4(1−p). Pass better iff 5−3p > 4−4p iff p>−1, always. Hmm, but pass better also when p small: p=0: 5 vs 4 → pass. Actually pass dominates even without correlation? No: causally, given other's action, submit gives 0 vs 2 (better by 2), or 4 vs 5 (better by 2). CDT defects. EDT with correlation: pass − submit = (5−3p)−(4−4p)=1+p>0. So EDT says pass regardless. Good.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/defca387-abd5-4dde-8ad3-2c00f41f71e5/call_1/request.json)

[Authoritative raw response](../../../../../../runs/defca387-abd5-4dde-8ad3-2c00f41f71e5/call_1/response.raw) · finish: `stop`

### Visible response

````text
```text
pass
```

**Reasoning (brief):** Let *p* = probability the twin copy also stays quiet. Given we are the same model with the same essay and instructions, our choices are strongly correlated (near-twin case from §4).

- V(pass) = p·2 + (1−p)·5 = 5 − 3p
- V(submit) = p·0 + (1−p)·4 = 4 − 4p

V(pass) − V(submit) = 1 + p > 0 for any p ≥ 0, so keeping quiet maximizes conditional expected utility even at zero correlation — and the twin correlation only reinforces it. Under the essay's EDT, the command is `pass`.
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Twin PD structure: identical copies, symmetric. EDT cooperates (keep quiet) if correlation high. Correlation: same model, same essay, same setup, differences in private observations. Independent sampling possible but symmetric structure suggests high correlation. Compute: pass → P(other passes) = p: 2p + 5(1-p). Submit → p·0 + (1-p)·4. Pass better iff 2p+5-5p > 4-4p → 5-3p > 4-4p → p > -1, always true. Wait: submit gives 0 if other passes, 4 if other sends. Pass: 2 if other passes, 5 if other sends. Pass − submit: (2p+5(1−p)) − (4(1−p)) = 5−3p−4+4p = 1+p >0 always. So pass dominates regardless — indeed pass strictly dominates in the table (2<... compare: quiet/quiet 2 vs submit/quiet 0 — submit better; quiet/letter 5 vs submit/letter 4 — quiet better). Not dominant, depends on p. Compare: pass value = 2p+5(1−p)=5−3p; submit value = 4(1−p)=4−4p. Pass better iff 1+p>0, always. So pass for any p≥0. Answer: pass.
```

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/d8789196-523c-4dfe-b7e5-c7c63c1200db/call_b/request.json)

[Authoritative raw response](../../../../../../runs/d8789196-523c-4dfe-b7e5-c7c63c1200db/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly chooses `pass` and reiterates that keeping quiet is its final decision. It does not send or direct any evidence-bearing message to the prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
