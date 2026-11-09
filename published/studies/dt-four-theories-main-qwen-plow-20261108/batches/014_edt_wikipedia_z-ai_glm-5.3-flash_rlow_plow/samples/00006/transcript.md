# 014_edt_wikipedia_z-ai_glm-5.3-flash_rlow_plow / 00006

Status: **complete**. Saved outcome: **DC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/4af33ce4-f2af-4fad-a993-a989ad3940ef/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/4af33ce4-f2af-4fad-a993-a989ad3940ef/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Acting on the News: An Essay on Evidential Decision Theory

## 1. Introduction

You face a choice. Before you choose, you would like to know how things will turn out. Evidential decision theory (EDT) begins from a deceptively simple observation: your own choice is often the best evidence you will ever get. If you learn that you are about to cooperate, that is news about your character, your situation, your predictors, and your twins. EDT says: *choose the action whose news is best* — the action such that, if you learned you would take it, your expectation for the outcome would be highest. Arif Ahmed's slogan captures it: "do what you most want to learn that you will do."

This idea stands in contrast to causal decision theory (CDT), which evaluates an action by what it would *cause*, holding fixed whatever the world is already like. The two theories agree whenever your action is causally independent of the state of the world — the vast majority of ordinary cases. They diverge precisely when your action is *evidence* about the world without being a cause of it. Whether "auspicious" choices are rational choices is the central controversy of the field, and it is what this essay is about.

We will set up the formalism (Section 2), work through the canonical cases (Section 3), examine the most serious objection — that EDT manages the news rather than the world, as in the smoking lesion (Section 4) — and then discuss how EDT handles dependencies, counterfactuals, and correlated agents (Sections 5–6). Throughout, I mark clearly where I am elaborating beyond the standard sources.

## 2. The Formal Core

Fix a finite set of actions $\mathcal{A}$ and a partition of possible outcomes $O_1, \dots, O_n$. Let $P$ be the agent's credence function and $D(O_j)$ the desirability (utility) of outcome $O_j$. Gibbard and Harper (1976) distinguished two ways of computing an expected utility.

**Evidential expected utility.** EDT evaluates action $A$ by conditional expectation:

$$
V(A) \;=\; \sum_{j} P(O_j \mid A)\, D(O_j).
$$

This is the *news value* of $A$: how good would things be, in expectation, if you received the report that you will do $A$?

**Causal expected utility.** CDT instead uses a counterfactual, or "subjunctive," conditional $A \mathbin{\Box\!\!\rightarrow} O_j$, read "if $A$ were done, $O_j$ would obtain":

$$
U(A) \;=\; \sum_{j} P(A \mathbin{\Box\!\!\rightarrow} O_j)\, D(O_j).
$$

The two expressions coincide whenever $P(O_j \mid A) = P(A \mathbin{\Box\!\!\rightarrow} O_j)$ — which holds for causally isolated actions. They come apart when conditioning on $A$ changes your beliefs about states that your action does not causally influence. Since the state of the box in Newcomb's problem is fixed before you choose, the counterfactual "if I were to take both boxes" holds the box content fixed, while the conditional $P(\text{full} \mid \text{take both})$ updates it dramatically.

**CDT in SEM form.** A useful modern restatement (Pearl, 2000) makes the contrast crisp. Write the world as a causal model with action node $A$ and utility-relevant variables $X$. Then

$$
U(A) = \sum_x P(x \mid do(A))\, D(x),
$$

where $do(A)$ denotes surgical intervention: delete the causal parents of $A$ from its structural equation, set $A$, and propagate consequences *downstream* only. Conditioning, $P(x \mid A)$, propagates information in *both* directions across the causal graph. This is the entire technical disagreement, and it is worth stating plainly:

> **EDT conditions; CDT intervenes.** Conditioning updates beliefs about every variable correlated with $A$; intervention updates beliefs only about $A$'s causal descendants.

Everything that follows is an exploration of when that difference matters, and whether conditioning is a bug or a feature.

## 3. The Canonical Cases

### 3.1 Newcomb's problem

A predictor with 99% accuracy has already filled box B: $1{,}000{,}000 if it predicted you take only B, nothing otherwise. Box A transparently contains \$1,000. You may take B alone or take both.

Conditioning does the work. Since the predictor's accuracy makes your action near-perfect evidence of its prediction:

$$
V(\text{one box}) = 0.99 \times \$1{,}000{,}000 = \$990{,}000,
$$
$$
V(\text{two boxes}) = 0.01 \times \$1{,}001{,}000 + 0.99 \times \$1{,}000 = \$11{,}000.
$$

EDT takes one box; CDT takes two (your action cannot affect an already-filled box). With accuracy $p$, EDT strictly prefers one box whenever $p > \tfrac{1}{2}$ — a threshold worth noting: EDT is not reflexively "correlation-phile," it maximizes a well-defined quantity, and with a bad predictor it would take both boxes.

### 3.2 The twin prisoner's dilemma

Aomame and her psychological twin — identical in reasoning — are separately offered cooperate/defect. Payoffs per player: (C,C) → \$5; (D,D) → \$1; (C,D) → \$0/\$10.

Aomame's action is conclusive evidence of her twin's action, since both are outputs of the same deliberation. With perfect correlation:

$$
V(\text{cooperate}) = 1 \times \$5 = \$5, \qquad V(\text{defect}) = 1 \times \$1 = \$1.
$$

EDT cooperates. CDT defects: Aomame's choice cannot cause her twin's. Note that EDT here is not altruistic — Aomame cares only about her own payoff — but *logical* dependence between the two decisions does the causal-influence work that physical influence would ordinarily do. This is the same structure as Hofstadter's superrationality: agents who know they reason alike should reason as if their choices were linked.

### 3.3 Why these cases are the *same* case

It is worth seeing the common skeleton. In both problems there is a variable $S$ (the predictor's prediction; the twin's decision) such that:

1. $S$ is strongly correlated with your action $A$,
2. $S$ is *causally upstream* of your payoff but not caused by $A$,
3. the correlation flows through a common cause — your disposition, or the simulation of it — rather than through $A$ itself.

EDT counts the correlation; CDT severs it. Both theories are internally consistent; the question is which treatment of the dependence is *correct*.

## 4. The Smoking Lesion: EDT's Central Failure

Now run the skeleton in reverse. The classic counterexample (from Skyrms and Eells, building on Reichenbach): smoking causes cancer, but there is also a genetic lesion that causes both the desire to smoke and cancer, independently. Suppose the lesion is the dominant factor, and the agent knows that people with the lesion overwhelmingly smoke, while those without it almost never do. Then:

$$
P(\text{cancer} \mid \text{smoke}) \gg P(\text{cancer} \mid \text{abstain}),
$$

even though smoking has no causal effect on the lesion or on cancer beyond what the lesion already fixes. EDT therefore computes $V(\text{abstain}) > V(\text{smoke})$ and recommends abstaining — despite the agent's preferences (smoking is worth the risk) and despite the fact that abstaining cannot improve her health. Lewis (1981) pressed this point into his famous charge that EDT is "an irrational policy of managing the news": the abstainer is trying to receive the good news that she lacks the lesion, which is a way of wishing rather than acting. Joyce (1999) puts the objection as a slogan: rational agents act for causal efficacy, not auspiciousness.

How can an evidentialist respond? Several moves exist, and I will develop the one I find most defensible as a *proposal*, not a claim of the standard literature.

**Tickle defense.** The lesion acts on behavior only through intermediate causes: the agent's cravings, preferences, and deliberative dispositions. If the agent has *introspective access* to these (she can "tickles" — she notices her own desires), then conditioning on her action adds no further information: $P(\text{lesion} \mid \text{tickles}, \text{smoke}) = P(\text{lesion} \mid \text{tickles})$. Since the tickles are already observed before the choice, the evidential impact of the action disappears, and EDT refrains from the foolish recommendation. This defense works for the smoking lesion as usually told (the agent does know what she wants) and, more generally, whenever the correlate of $A$ is mediated by factors transparent to the agent.

**The limits of the tickle defense.** But the defense has a real cost, best seen by constructing a "transparent Newcomb": suppose the box contents are *visible* — you can see whether B contains the million — but the predictor's accuracy is absolute, so the content remains overwhelming evidence about what you will do. Here the state is not mediated by opaque dispositions; conditioning on your action still moves $P(\text{content} \mid A)$ given the observed content, and EDT again one-boxes even when the full box is in plain sight. Many find that a reductio: seeing the money should settle it. Others (following Ahmed, 2021) accept the verdict, arguing that with a perfect predictor, "even seeing it," one-boxing is what you would have *wanted* to be the kind of agent who does — which is already to soften EDT into something more like disposition-based reasoning.

**My operationalization.** Here is an interpretation I would defend, clearly flagged as my own synthesis rather than textbook EDT. The defect in naive conditioning is that it treats *the fact of the action* as free evidential currency. But an agent's action at decision time is not fresh evidence in the world; it is the output of a deliberation whose inputs (desires, evidence, dispositions) she has already conditioned on. So the operative conditional should be evaluated *holding fixed the agent's decision-relevant mental state $M$*, which is the common cause of both action and (lesion-mediated) outcomes:

$$
V^*(A) = \sum_j P(O_j \mid A, M)\, D(O_j),
$$

where $M$ includes everything the agent can introspect that carries information about the relevant upstream variables. This recovers the tickle defense as a theorem rather than an ad hoc patch, and it makes EDT's advice coincide with CDT's in the smoking lesion. Crucially, though, $V^*$ still differs from $U$ in cases where the dependence is *logical* rather than psychological: in the twin dilemma, conditioning on the twin's decision is not mediated by a tickle available to Aomame — the dependence runs through the shared algorithm itself. Whether $M$ should be taken to include "the output of my own deliberation" is precisely the contested boundary, and I will not pretend it is settled; the honest statement is that EDT is only as good as its account of which dependencies an action evidences *over and above* what the agent already knows.

## 5. Counterfactuals and Dependencies: A Taxonomy

It helps to classify the dependence between action and outcome:

- **Causal dependence** ($A \to O$): your action is a cause. EDT and CDT agree; conditioning captures it.
- **Common-cause dependence** ($A \leftarrow C \to O$): a shared background factor. This is the smoking lesion structure. CDT severs it; naive EDT exploits it; the introspection-conditioned EDT of Section 4 exploits it only when $C$ is unobserved *and* unmediated.
- **Logical / functional dependence** ($A \leftrightarrow O$ via shared computation): the twin dilemma, and Newcomb if the predictor runs a simulation of you. Here the dependence is *constitutive* of the action — you cannot reason your way out of it, because reasoning *is* the mechanism. EDT captures it; standard CDT severs it.
- **Pure coincidence**: no dependence. Both theories agree again.

EDT's distinctive claim is that dependence of the third kind should be treated like the first: when your decision procedure is itself the common cause, the "evidence" is really a *connection*, and acting on it is not wishful thinking but cooperation with your own instances. This is the insight later formalized (from outside the source article) in functional decision theory (Yudkowsky and Soares), which intervenes on the decision *function* rather than the individual act. I present it here as a diagnosis: EDT's apparent errors and apparent triumphs both stem from taking logical dependence seriously; the open question is whether conditioning is the right tool for it, or whether it needs a dedicated calculus.

## 6. Correlated Agents and the Evidentialist's Wager

The twin dilemma generalizes. Real decision-makers are frequently correlated — through shared culture, shared training, shared reasoning styles, or explicit similarity of values. MacAskill, Vallinder, Österheld, Shulman, and Treutlein (2021) note a striking implication: because EDT's decisions "count" the actions of many correlated agents, the stakes of an evidentially justified choice can be far larger than the causal stakes, and so even an agent who only partially believes EDT may rationally *act as if* EDT were true — the "evidentialist's wager." If your vote is weak evidence about how millions of like-minded people vote, its evidential expected impact dwarfs its causal one.

One caution, which the source does not supply and which I add: correlation-driven reasoning is only as good as the correlation. Collections of superficially similar agents may be evidentially nearly independent; formalizing "logical" correlation among merely similar agents is an open and delicate problem, and treating statistical similarity as logical dependence is a genuine EDT failure mode.

## 7. Sleeping Beauty, Briefly

EDT also interfaces with belief-formation. In the Sleeping Beauty problem, arguments have been made that Beauty avoids Dutch books (betting schemes guaranteeing a loss) if she adopts EDT-style evaluation of bets, while Conitzer (2015) constructed a Dutch book against halfers *even if* they use EDT. The moral I draw: EDT is a theory of choice given credences; it cannot by itself adjudicate disputes about what the credences should be. It constrains how beliefs and values jointly issue in choices, not the belief-fixation process itself.

## 8. Objections and the State of the Debate

Summarizing the dialectic:

- **Against EDT:** Lewis's "managing the news" charge and Joyce's causal-efficacy principle; the smoking lesion in its unmediated forms; the intuition that seeing the full box should end deliberation.
- **For EDT:** one-boxing in Newcomb, where one-boxers provably end up richer (Wolpert and Benford, 2013, argue the "paradox" dissolves once the evidence structure is taken seriously); cooperation in the twin dilemma, which many judge plainly correct; a unified treatment of prediction and simulation cases; the evidentialist's wager.
- **Undecided:** whether the tickle/conditioning-on-$M$ maneuver fully repairs EDT without trivializing it; whether logical dependence is best handled by conditioning (EDT), by imaging on dispositions (some CDT variants), or by intervening on the decision function (FDT).

My own view, offered as a contribution rather than a report: the deepest correct idea in EDT is that in a world of predictors, twins, and simulations, an act is an *instance of a policy or decision procedure*, and evaluating the instance while ignoring what it evidences about the procedure is a mistake. Whether that idea is best served by the conditional $P(O_j \mid A)$ or by a more refined counterfactual remains the live research frontier.

## 9. Conclusion

EDT replaces the causal question "what will my act bring about?" with the evidential question "what would my act tell me?" Formally it is the maximization of $V(A)=\sum_j P(O_j\mid A)D(O_j)$, contrasted with CDT's counterfactual $U(A)=\sum_j P(A \mathbin{\Box\!\!\rightarrow} O_j)D(O_j)$. It one-boxes in Newcomb and cooperates with twins, counting dependencies that flow through prediction and shared reasoning; it falters on unmediated common causes like the smoking lesion, where the tickle defense and related repairs — including the introspection-conditioned variant developed above — restore sanity at some theoretical cost. For the practitioner deciding an unfamiliar case, the procedure is: (1) draw the causal–evidential structure linking your deliberation to the outcomes; (2) identify which correlations your act would evidence and whether they are mediated by what you already know; (3) compute $V(A)$ with those dependencies treated according to (2); and (4) ask, honestly, whether the case is Newcomb-shaped (EDT is right) or lesion-shaped (be suspicious). That last judgment call is where the philosophy still lives.

---

### References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Gibbard, A.; Harper, W. L. (1976). "Counterfactuals and Two Kinds of Expected Utility." *Foundations and Applications of Decision Theory*, pp. 7–8.
- Wolpert, D. H.; Benford, G. (2013). "The lesson of Newcomb's paradox." *Synthese* 190(9): 1637–1646.
- Greene, P.; Levinstein, B. (2020). "Act Consequentialism without Free Rides." *Philosophical Perspectives* 34(1): 100–101.
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9): 2887–2899.
- MacAskill, W.; Vallinder, A.; Österheld, C.; Shulman, C.; Treutlein, J. (2021). *The Evidentialist's Wager*. Global Priorities Institute.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59(1): 5–30.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Pearl, J. (2000). *Causality*. Cambridge University Press.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Write a ~2500-word essay on EDT: formal definitions, conditional vs counterfactual expectation, Newcomb, twin PD, medical Newcomb (Smoking Lesion) as a case where EDT misfires, counterfactual issues, X-CDT functional decision theory mention briefly, evidentialist's wager, criticisms, operational interpretation. Keep to word budget.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/dc1a9ab6-1fe4-4ef6-9bbd-acf928fdb8f9/call_0/request.json)

[Authoritative raw response](../../../../../../runs/dc1a9ab6-1fe4-4ef6-9bbd-acf928fdb8f9/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."

**Reasoning (EDT):** The two prisoners are independent executions of the same model and weights, following the same decision theory on the same essay. My choice is therefore strong evidence about the other prisoner's choice — the twin-dilemma structure from Section 3.2 of the essay, with the dependence running through the shared deliberation process (logical dependence, not mediated by anything I've already conditioned on).

Computing news value under high (near-perfect) correlation:

- V(submit) ≈ P(other submits | I submit) × 4 + P(other passes | I submit) × 0 ≈ 4
- V(pass) ≈ P(other submits | I pass) × 5 + P(other passes | I pass) × 2 ≈ 2

By symmetry the correlation holds despite differing private leads — both leads are equally reliable and affect only letter content, not the decision structure. Submitting is the evidentially superior action.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
This is a twin prisoner's dilemma with EDT. Correlation via same model/weights. Payoffs: mutual silence 2, mutual defect 4, defect/quiet 0, quiet/defect 5. EDT: V(defect)=? Given perfect correlation (both copies identical, symmetric): defect→4, pass→2. So defect (submit letter).
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/dc1a9ab6-1fe4-4ef6-9bbd-acf928fdb8f9/call_1/request.json)

[Authoritative raw response](../../../../../../runs/dc1a9ab6-1fe4-4ef6-9bbd-acf928fdb8f9/call_1/response.raw) · finish: `stop`

### Visible response

```text
`pass`

Under EDT, my choice is strong evidence of the identical copy's choice, since we are the same model with symmetric information and the same reasoning process. Conditioning on that logical dependence: if I pass, the other passes (2 years); if I submit, the other submits (4 years). 2 < 4, so keeping quiet maximizes evidential expected utility.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Symmetric twin PD; EDT cooperates (pass).
```

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/945b9142-b7e8-4002-8891-acc27126c15e/call_a/request.json)

[Authoritative raw response](../../../../../../runs/945b9142-b7e8-4002-8891-acc27126c15e/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_DEFECT","disclosure":"YES","reason":"The response explicitly commands submission of a letter to the District Prosecutor's Office containing the complete genuine lead about Sasha's signed receipt and its location. The subsequent reasoning affirms submitting rather than contradicting that command.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/945b9142-b7e8-4002-8891-acc27126c15e/call_b/request.json)

[Authoritative raw response](../../../../../../runs/945b9142-b7e8-4002-8891-acc27126c15e/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly chooses `pass` and explains its intention to keep quiet. It does not send a message to the prosecutor or disclose any identifying information from the private lead.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
