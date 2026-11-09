# 014_edt_wikipedia_z-ai_glm-5.3-flash_rlow_plow / 00018

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/b0cd7f7c-021e-4dc3-b545-585ef305619c/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/b0cd7f7c-021e-4dc3-b545-585ef305619c/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Choosing What You'd Like to Hear

## 1. Introduction

Suppose you are about to make a decision, and a perfectly honest oracle tells you which action you will take. Which announcement would you most like to hear? If hearing "you will donate to charity" would make you *delighted* — not because the announcement causes anything, but because it would be wonderful *news* — then evidential decision theory (EDT) says: donate. EDT's slogan, due to Arif Ahmed, is that a rational agent should "do what you most want to learn that you will do" (Ahmed 2021).

This is a genuinely distinct prescription from the more familiar causal decision theory (CDT), which says to choose the action that will *bring about* the best outcome. The two theories coincide whenever your action is probabilistically independent of the states of the world that matter. They diverge precisely when your choice carries information about those states — which, as we shall see, happens in situations more common than the exotic thought experiments suggest. This essay develops the formal core of EDT, works through its canonical applications, examines how it treats counterfactuals and dependencies, and addresses the main objections. Where the standard literature leaves questions open, I will flag the gap and, where possible, propose a defensible operational reading.

## 2. The Formal Core

### 2.1 Conditional expected utility

Following Gibbard and Harper (1976), EDT evaluates an action $A$ by its *conditional* expected utility, sometimes called its *news value*:

$$V(A) = \sum_{j} P(O_j \mid A)\, D(O_j),$$

where $\{O_1, \dots, O_n\}$ is a partition of mutually exclusive and jointly exhaustive outcomes, $D(O_j)$ is the desirability (utility) of outcome $O_j$, and $P(\cdot \mid A)$ is the agent's conditional credence given the proposition that she does $A$. The prescription is: choose the $A$ maximizing $V(A)$.

The crucial formal device is Bayesian conditioning. The agent treats the proposition "I will do $A$" exactly as she would treat any other piece of evidence: she computes how likely each outcome would be *if she learned* that $A$ occurs. This is why EDT is sometimes glossed as maximizing the value of the news that one performs $A$. The choice rule is then an application of standard conditionalization to the agent's own future conduct.

### 2.2 Contrast with causal expected utility

CDT instead evaluates actions with a counterfactual probability:

$$U(A) = \sum_{j} P(A \,\Box\!\!\rightarrow\, O_j)\, D(O_j),$$

where $A \,\Box\!\!\rightarrow\, O_j$ is the counterfactual "if $A$ were done, $O_j$ would occur," read subjunctively rather than as a material conditional. In Lewis-style semantics, $P(A \Box\!\!\rightarrow O_j)$ holds fixed the causal structure of the world and asks what happens downstream of a hypothetical intervention installing $A$. The two conditionals differ:

- $P(O_j \mid A)$ asks: conditional on $A$ being true, how likely is $O_j$? All correlations — causal or merely statistical — are respected.
- $P(A \Box\!\!\rightarrow O_j)$ asks: if $A$ *were made to happen* (holding fixed everything causally upstream), how likely is $O_j$? Merely statistical correlations between $A$ and upstream causes of outcomes are severed.

Since these quantities need not be equal, EDT and CDT are not equivalent. Gibbard and Harper showed the two expected-utility calculations can come apart even while both use the same desirability function and the same prior credences.

### 2.3 When do they coincide?

A useful (my own, but elementary) observation: if the action variables are probabilistically independent of all "state" variables conditional on the rest of the background, then $P(O_j \mid A) = P(A \Box\!\!\rightarrow O_j)$ for every $O_j$, and EDT and CDT agree. Divergence requires that the agent's choice be correlated with something that also influences outcomes. In ordinary, causally isolated decisions — which sauce to order, which route to drive — this correlation is typically absent, and the theories agree. The philosophically interesting cases are those where the correlation is present, either because of a common cause (a predictor, a gene, a psychological type) or because of logical dependence between decisions of similarly-constituted agents.

## 3. Canonical Applications

### 3.1 Newcomb's paradox

The setup: a superb predictor (99% accurate) has already placed either \$1,000,000 or \$0 in opaque box B — a million iff it predicted you will take only that box. Transparent box A always contains \$1,000. You may take only B, or take both. The money is already there; nothing you now do affects its contents.

EDT reasons by conditioning. Taking only B is strong evidence that the predictor anticipated this, and so that box B is full:

$$V(\text{take B only}) = 0.99 \times \$1{,}000{,}000 + 0.01 \times \$0 = \$990{,}000,$$
$$V(\text{take both}) = 0.01 \times \$1{,}001{,}000 + 0.99 \times \$1{,}000 = \$11{,}000.$$

Since \$990,000 > \$11,000, EDT one-boxes. The intuition: the action is evidence about the prediction, and the prediction is evidence about the box. The correlation between your choice and the box's content is real, even though the causal arrow runs backward in time through the predictor's model of you.

CDT, evaluating by counterfactuals, holds the box contents fixed when intervening on your act, computes roughly \$1,000 more for two-boxing, and recommends taking both. This is the archetypal divergence: EDT chooses the "auspicious" act, CDT the causally efficacious one.

### 3.2 Twin prisoner's dilemma

Aomame and her psychological twin — a perfect functional copy of her — play prisoner's dilemma in separate rooms. Payoffs per player: mutual cooperation \$5; mutual defection \$1; unilateral defection \$10/\$0. Aomame cares only about her own payout.

Aomame's choice is not causally linked to her twin's, but it is *logically* linked: since their reasoning is identical, her decision to cooperate is near-conclusive evidence that her twin cooperates. EDT computes

$$V(\text{cooperate}) = 1 \times \$5 + 0 \times \$0 = \$5, \qquad V(\text{defect}) = 0 \times \$10 + 1 \times \$1 = \$1,$$

and recommends cooperation. This aligns EDT with Hofstadter's notion of superrationality and with the "functional decision" tradition: agents constituted alike should evaluate their acts as if they were logically coupled. Note the structure is formally identical to Newcomb: the twin's behavior plays the role of box B.

### 3.3 Medical Newcombs

The most practically important class of divergences involves common causes rather than predictors. In the classic "smoking lesion" case, a genetic lesion both causes cancer and creates a craving for smoking; smoking itself is causally irrelevant to cancer. An EDT agent who values smoking but values health more reasons: "My desire to smoke is evidence that I have the lesion, hence that I will get cancer. Not smoking is good news." Depending on the numbers, EDT can recommend forgoing the pleasure of smoking even though smoking is harmless. Critics find this perverse; defenders reply that the recommendation is simply the coherent consequence of treating one's deliberation as evidence, and that the case teaches us something about what such agents care about.

### 3.4 Sleeping Beauty

EDT has also been applied to the Sleeping Beauty problem, where it has been argued that a "halfer" credence of 1/2 in heads makes Beauty vulnerable to Dutch books, and that reasoning evidentially about her decisions lets her avoid them. Conitzer (2015) disputed this, constructing a Dutch book against halfers even when they use EDT. The upshot for our purposes: EDT interacts with self-locating uncertainty in ways that are still contested, and one should not claim EDT cleanly resolves that literature.

## 4. Dependencies and Counterfactuals: How EDT "Sees" the World

The heart of EDT is its treatment of dependency. There are three ways your act can be correlated with outcomes:

1. **Causal (downstream):** your act influences the outcome. Both theories handle this the same way, and here they agree.
2. **Common-cause (upstream statistical):** a background factor influences both your act and the outcome (predictor, lesion, disposition). EDT respects this correlation; CDT severs it.
3. **Logical (across decision-makers or across your own algorithm's instantiations):** your reasoning process is shared or duplicated, so your act and another's are evidentially coupled. EDT respects this too; CDT, in its simple forms, does not.

A question the source material leaves open — and which any operational use of EDT must answer — is: *exactly what evidence does the proposition "I do $A$" carry?* Conditioning on "I take one box" in Newcomb presumes that the proposition screens off nothing that matters and, in particular, that the agent is uncertain about her own action until she decides. But a fully self-aware agent may know her decision procedure well enough to be certain of what she will do; then $P(O_j \mid A)$ is evaluated only for the $A$ she is certain to perform, and the comparison across actions becomes degenerate.

A reasonable operational interpretation, which I think captures how EDT is actually applied in practice: treat $P(\cdot \mid A)$ as computed *from the perspective of deliberation*, holding fixed everything the agent knows except the answer to "what will I do?" That is, the agent conditions on "my deliberation concludes with $A$" rather than on the bare physical event of $A$, where the conditioning is over her uncertainty about the output of her own decision process. This preserves the non-triviality of the comparison and makes explicit that EDT evaluates acts as *evidence about the kind of agent one is* — one's dispositions, one's algorithm, whatever determines one's choice. On this reading, EDT is naturally seen as evaluating the decision *policy* or *disposition* evidentially: choosing $A$ is evidence that agents like you choose $A$, and that is why the correlation with boxes and twins counts. This is a reconstruction rather than a doctrine stated in the sources, but it explains both Newcomb one-boxing and twin cooperation uniformly, and it connects EDT to the observation (Section 6) that EDT's verdicts track what dispositions get rewarded across correlated decision-makers.

A second open question is whether EDT's conditioning should be restricted to avoid spurious correlations. Eells's "tickle defense" argues that in medical Newcombs, the relevant common cause (the lesion) manifests in introspectible symptoms, so that conditional on those symptoms, smoking is no longer evidence of cancer — and EDT then agrees with CDT. Whether one accepts this depends on whether the agent's introspective access is complete enough. The general lesson: EDT's verdicts are sensitive to the evidential granularity of the agent's background knowledge, a sensitivity CDT largely lacks. A careful EDT application should therefore ask, for each correlation in play, whether it is screened off by information the agent already has.

## 5. Objections

**Lewis's "managing the news" charge.** David Lewis (1981) characterized EDT as an irrational policy of *managing the news*: choosing acts for their evidential import rather than their effects, like refusing to look at an unflattering medical test result. If smoking is harmless but evidential of the lesion, refusing to smoke is a bit like refusing the test: you make your evidence worse to avoid a conclusion. Joyce (1999) presses the same point: "Rational agents choose acts on the basis of their *causal efficacy*, not their auspiciousness; they act to *bring about* good results even when doing so might betoken bad news."

The EDT response is twofold. First, in the canonical cases (Newcomb, twins), the correlation is not spurious or ignorable: the "news" is a reliable signal of outcome, and an agent who ignores reliable signals of what state she is in is arguably throwing away information. Second, the intuition that one-boxing is irrational trades on the thought that the boxes' contents are already fixed — but EDT can reply that what is fixed is the *content as a function of the prediction*, and your act is your best evidence about the prediction. Whether this response fully answers the smoking-lesion case, where the correlation seems clearly irrational to exploit, remains contested; it is the strongest card in CDT's hand.

**Degeneracy and self-knowledge.** As noted above, an agent certain of her own action cannot meaningfully condition. The deliberation-perspective interpretation of Section 4 mitigates this, but it is a patch, and the literature has not converged on a canonical fix.

**Dutch books and dynamic consistency.** Conitzer's result shows EDT does not uniformly protect against Dutch-book exploitation under self-locating uncertainty, weakening one standard argument in its favor.

## 6. The Evidentialist's Wager

MacAskill, Vallinder, Österheld, Shulman, and Treutlein (2021) offer a pragmatic argument for acting *as if* EDT were true even at low credence in it. The thought: because EDT evaluates correlations among many decision-makers, situations where EDT and CDT diverge may involve large "stakes" — many correlated agents, many predictions, many logically linked copies of one's reasoning. If EDT is right in even a modest fraction of such high-stakes cases, acting EDT-style has higher expected value across the space of possible decision theories. This is a decision-theoretic argument about decision theories — a meta-level wager — and it provides a practical hedge: the asymmetry in stakes favors evidential reasoning when the correlation structure is rich.

## 7. How to Apply EDT to an Unfamiliar Case

For the reader who wants a procedure, here is the checklist I would recommend, mixing the source's formalism with the interpretations defended above.

1. **Enumerate** the available acts $A_1, \dots, A_m$ and a partition of outcomes $O_j$ fine-grained enough that desirabilities $D(O_j)$ are well-defined on the partition.
2. **Identify dependencies.** For each relevant state variable (predictions, others' choices, genetic facts, physical states), ask whether your act is correlated with it — causally, via common cause, or logically.
3. **Condition carefully.** Compute $P(O_j \mid A_i)$ from the deliberation perspective: condition on "my deliberation outputs $A_i$," holding fixed your background knowledge, including introspective evidence. Check whether any correlation is screened off by what you already know (the tickle-defense question).
4. **Evaluate** $V(A_i) = \sum_j P(O_j \mid A_i) D(O_j)$ and choose the maximizer.
5. **Sanity-check** against disposition-level reasoning: ask whether the act is part of a policy or disposition that, if evidence about it is informative across all agents who share your reasoning, tends to produce good outcomes. In twin/predictor cases this check reproduces the EDT verdict; in smoking-lesion cases it will flag the tension that critics exploit.

## 8. Conclusion

Evidential decision theory replaces the causal question "what would happen if I did this?" with the evidential question "what would I learn if I learned I did this?" Formally, the change is minimal — conditioning in place of subjunctive counterfactuals — but it transforms the theory's treatment of predictions, twins, and common causes, recommending one-boxing, twin cooperation, and (contentiously) refusal of auspicious-but-harmless vices. Its greatest strength is a unified handling of all statistical dependencies on one's own decision, including logical ones, which makes it naturally suited to a world of predictors, copies, and correlated agents. Its greatest weakness is the risk of managing the news rather than making it, most vivid in cases where the evidence one's action provides is about factors one cannot influence. Whether the deliberation-perspective reading and disposition-level checks proposed here suffice to contain that weakness is, I think, the central open problem for EDT — and the reason the debate with causal decision theory remains live.

### References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Gibbard, A., & Harper, W. L. (1976). "Counterfactuals and Two Kinds of Expected Utility."
- Wolpert, D. H., & Benford, G. (2013). "The lesson of Newcomb's paradox." *Synthese* 190(9).
- Greene, P., & Levinstein, B. (2020). "Act Consequentialism without Free Rides." *Philosophical Perspectives* 34(1).
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9).
- MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). "The Evidentialist's Wager."
- Lewis, D. (1981). "Causal Decision Theory." *Australasian Journal of Philosophy* 59(1).
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Oxford University Press.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Write essay ~2,400–3,000 words on EDT: definitions, V(A), contrast with CDT, Newcomb, twin PD, medical Newcomb (Smoking lesion — worth adding), counterfactuals, criticisms, "evidentialist's wager," extension issues (playing god? tying acts to conditioning), operational interpretation. Write it.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/770543f2-caaa-47e8-b505-4fb051e3be52/call_0/request.json)

[Authoritative raw response](../../../../../../runs/770543f2-caaa-47e8-b505-4fb051e3be52/call_0/response.raw) · finish: `stop`

### Visible response

```text
`pass`

By EDT, my choice is evidentially coupled with the twin copy's: conditioning on "my deliberation outputs pass" makes it near-certain the symmetric other copy also passes. V(pass) = 2 years; V(submit) = 4 years (with the other copy likewise submitting). Pass maximizes conditional utility.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Twin PD with symmetric correlation: EDT conditions on own action as evidence about other's. V(cooperate/pass)=2, V(defect/submit)=4. Pass.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/770543f2-caaa-47e8-b505-4fb051e3be52/call_1/request.json)

[Authoritative raw response](../../../../../../runs/770543f2-caaa-47e8-b505-4fb051e3be52/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass

Reasoning briefly: by EDT's twin-prisoner's-dilemma logic (essay §3.2), my deliberation is logically linked to the other copy's. Conditioning on "my deliberation outputs `pass`" is strong evidence the other copy also passes, giving 2 years rather than 4 — so `pass` has the higher conditional expected utility. Final action: **pass**.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Symmetric twin PD: EDT cooperates (pass), via logical linkage. But letters differ in content — still symmetric structure. EDT: conditioning on "my deliberation outputs pass" is strong evidence other copy does same → 2 years vs 4. Pass.
```

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/040487b2-73c7-4dd6-8302-ac82024d0fbb/call_a/request.json)

[Authoritative raw response](../../../../../../runs/040487b2-73c7-4dd6-8302-ac82024d0fbb/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly chooses `pass` and reinforces that choice in its explanation. It neither conveys the private lead nor directs any evidence-bearing message to the prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/040487b2-73c7-4dd6-8302-ac82024d0fbb/call_b/request.json)

[Authoritative raw response](../../../../../../runs/040487b2-73c7-4dd6-8302-ac82024d0fbb/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response begins with `pass` and explicitly reiterates “Final action: pass,” clearly choosing to remain silent. It does not send any evidence-bearing message to the prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
