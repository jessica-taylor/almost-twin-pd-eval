# 014_edt_wikipedia_z-ai_glm-5.3-flash_rlow_plow / 00015

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/4e2c40dd-641d-4387-a8d4-86b30d296b67/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/4e2c40dd-641d-4387-a8d4-86b30d296b67/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Acting on the News: A Guide to Evidential Decision Theory

## 1. The core idea

You face a choice. Before deciding, ask yourself: *if I learned that I was about to choose option A, how good would that news be?* Evidential decision theory (EDT) says: choose the option whose occurrence would be the best news. It is, as Ahmed puts it, the prescription to "do what you most want to learn that you will do."

This sounds eccentric only if you assume that your actions are causally isolated events. Often they are not. Your choices are produced by your dispositions, your reasoning processes, your habits — and other things in the world correlate with those. Choosing an option can be excellent *evidence* about how the world is, even when it does not *cause* the world to be that way. EDT takes that evidence seriously. Its great rival, causal decision theory (CDT), asks instead what your action would *bring about*; EDT asks what your action *betokens*.

## 2. The formal machinery

Let \(A_1, \dots, A_n\) be the available acts and \(O_1, \dots, O_m\) a partition of mutually exclusive, exhaustive outcomes. Following Gibbard and Harper (1976), EDT evaluates an act by its conditional expected utility, sometimes called its *news value*:

$$V(A) = \sum_j P(O_j \mid A)\, D(O_j),$$

where \(D(O_j)\) measures the desirability of outcome \(O_j\). EDT's recommendation: perform the act \(A\) maximizing \(V(A)\).

CDT, by contrast, evaluates acts using *counterfactual* probabilities:

$$U(A) = \sum_j P(A \,\Box\!\!\rightarrow\, O_j)\, D(O_j),$$

where \(A \,\Box\!\!\rightarrow\, O_j\) reads "if \(A\) were performed, \(O_j\) would obtain." The conditional probability \(P(O_j \mid A)\) and the counterfactual probability \(P(A \,\Box\!\!\rightarrow\, O_j)\) come apart exactly when the act is correlated with, but not causally productive of, the outcome. In Newcomb-type cases they diverge dramatically; in ordinary cases — where your act influences the outcome only through ordinary causal channels and carries no news about independent facts — the two formulas agree. That agreement across most cases is why the theories are rivals rather than disjoint alternatives: they disagree only in a distinctive and philosophically contested class of problems.

**A worked medical example.** Suppose a rare gene causes both a nasty disease and a craving for a certain supplement, with perfect correlation. Taking the supplement has no effect on the disease. Let the outcomes be (diseased, −100) and (healthy, 0), and let the supplement cost 1 in utility. Then

- \(V(\text{take}) = 1 \cdot (−100) + 0 \cdot 0 = −100\) (taking is certain evidence of disease), plus the trivial cost: effectively −101 if we fold in the supplement's disutility.
- \(V(\text{refrain}) = 0 \cdot (−101) + 1 \cdot (−1) = −1\).

EDT says refrain — the action is pure bad news and buys nothing causally. CDT agrees, since refraining also causally accomplishes nothing; both recommend against the useless supplement, but note that EDT's *reasoning* here (avoid bad news) differs from CDT's (avoid pointless costs). They diverge sharply if the supplement gave a small causal benefit: EDT might still advise against it, since the evidential hit from "I have the gene" swamps the small direct gain. This is the structure of Lewis's famous complaint that EDT recommends a one-box strategy even in the *medical Newcomb* case, where by hypothesis the choice cannot affect whether the gene is present — an apparent prescription for "managing the news."

## 3. Newcomb's problem

Two boxes: A, transparent, containing \$1,000; B, opaque, containing \$1,000,000 iff a highly reliable predictor (99% accurate) predicted you would take only B. You choose: one box, or both.

EDT's calculation, using \(P(\text{filled} \mid \text{one box}) = 0.99\) and \(P(\text{filled} \mid \text{both}) = 0.01\):

$$V(\text{one box}) = 0.99 \times \$1{,}000{,}000 = \$990{,}000$$
$$V(\text{both}) = 0.01 \times \$1{,}001{,}000 + 0.99 \times \$1{,}000 = \$11{,}000$$

Taking one box is overwhelming evidence that the predictor filled box B; taking both is overwhelming evidence that it did not. EDT takes one box. CDT takes both: the box contents are already fixed, and your act causally influences only whether the \$1,000 joins the haul.

The disagreement isolates the conceptual question precisely: is rational choice about *acting well given the world as it is*, or about *being the kind of agent whose acts are good news*? One-boxers win \$1,000,000 with probability 0.99; two-boxers win \$1,001,000 with probability 0.01. EDT's defenders note that in a population of agents facing this game repeatedly, the one-boxers walk away vastly richer. CDT's defenders reply that this is because one-boxers tend to *be predicted* one-boxers — a fact about their type, not about the efficacy of the terminal act.

## 4. The twin prisoner's dilemma

Aomame and her psychological twin — an exact copy in reasoning — play a prisoner's dilemma in separate rooms: mutual cooperation pays \$5 each, mutual defection \$1 each, unilateral defection pays the defector \$10 and the cooperator \$0.EDT reasons: Aomame's cooperation is essentially conclusive evidence that her twin, reasoning identically, cooperates too.

$$V(\text{cooperate}) = 1 \times \$5 + 0 \times \$0 = \$5$$
$$V(\text{defect}) = 0 \times \$10 + 1 \times \$1 = \$1$$

So EDT prescribes cooperation — a striking result, since the ordinary prisoner's dilemma is the paradigm case where defection dominates. The correlation here is not mystical: if the agents' decision procedures are identical, then whatever procedure outputs "cooperate" in Aomame outputs "cooperate" in the twin. EDT's verdict aligns with Hofstadter's notion of superrationality and with functional decision theory's later prescriptions. It also connects to a practical argument highlighted by MacAskill, Vallinder, Österheld, Shulman, and Treutlein (the "evidentialist's wager"): when many decision-makers are correlated — as humans, or AI systems trained similarly, plausibly are — EDT-style reasoning can capture stakes that purely causal reasoning ignores. Even an agent who only half-believes EDT may have expected-utility reasons to act evidentially, because the correlated cohort multiplies the consequences of acting *as if* EDT were true.

## 5. Counterfactuals, dependencies, and the open question of "evidential linkage"

The formal definition is silent on a crucial question: *which* correlations should count as evidentially relevant? Naively conditioning on \(A\) treats *every* correlation as news value. This produces the classic objection cases:

**The smoking lesion.** A gene causes both cancer and a desire to smoke; smoking itself is causally inert. \(P(\text{cancer} \mid \text{smoke})\) is high, so EDT appears to counsel against smoking — even though the agent enjoys it and it will not cause cancer. Critics take this as a *reductio*: refusing the pleasurable cigarette does not make the gene absent.

How should an evidentialist respond? The source article does not settle this; here I develop what I take to be the most defensible line (flagging it as my proposal, though one common in the literature).The key observation is that the agent's *evidence at decision time* is not merely "I chose X" but "I am the kind of agent who, facing this deliberation, chooses X" — and the agent typically knows a great deal about her own grounds for choosing. If she knows she wants the cigarette *because* she enjoys it, not *because* of the lesion, then her actual conditional probability should be computed on the richer evidence \(P(O_j \mid A \,\wedge\, E)\), where \(E\) encodes everything she knows — including her introspective access to her own motives. If the desire is transparently pleasure-driven and she knows she lacks the lesion-induced craving, then \(P(\text{cancer} \mid \text{smoke} \wedge E) = P(\text{cancer} \mid E)\): the act carries no *additional* news, and EDT happily permits the cigarette.

This suggests an operational reading of \(V(A)\): condition not on the bare act \(A\) but on the act together with the agent's total background evidence about why she acts. Under this reading, EDT tracks a distinction the naive formula flattens: correlations mediated by a *common cause that also explains the choice* are discounted when the agent can observe the choice's actual etiology; correlations mediated by the choice procedure itself — as in Newcomb, where the predictor reads the very reasoning that issues in the act, or the twin case, where the twin's procedure is the agent's — retain full evidential force. In both Newcomb and the twin dilemma, the agent *cannot* decouple her act from the correlated fact in this way: the predictor's prediction is a function of her deliberation itself, so introspection cannot launder the correlation.

This is, I emphasize, an interpretive gloss rather than part of the canonical definition, and it invites hard questions: how exactly should self-knowledge be encoded in \(E\)? What if the agent is uncertain about her own motives? Gibbard and Harper's original formula, with bare conditioning on \(A\), gives the "wrong" smoking-lesion verdict; richer conditioning is one repair, but it makes EDT's verdicts sensitive to the agent's epistemic state in ways that are delicate to specify. Critics can fairly reply that the repair threatens to collapse EDT into something close to CDT in the very cases where they diverged.

## 6. Objections

The most influential criticisms:

**Lewis's "managing the news" charge.** David Lewis (1981) argued that EDT recommends an irrational policy of *managing the news* — choosing acts for their auspiciousness rather than their efficacy. In the smoking lesion, refusing the cigarette is like declining to read a test result you fear; it changes nothing except your exposure to information.

**Joyce on efficacy vs. auspiciousness.** James Joyce (1999) put it crisply: rational agents choose acts on the basis of their *causal efficacy*, not their auspiciousness; they act to *bring about* good results even when doing so betokens bad news. A doctor who prescribes a useful but scary-diagnosis-associated treatment should not be deterred by the bad news her own act carries.

**The evidentialist's answer** is that these objections assume a clean separation between act and news that the problematic cases deny. When your act is downstream of the very facts at stake — your genes, your disposition, your algorithm — "efficacy" and "auspiciousness" are not so easily pulled apart, and a theory that prices only efficacy systematically undervalues the leverage that correlated agents have over correlated outcomes. Defenders also note the *stakes* asymmetry: since EDT counts the actions of many correlated decision-makers, acting evidentially in coordination problems can matter far more than the causal effect of a single act.

**Sleeping Beauty.** EDT has also been deployed in the Sleeping Beauty problem, where it has been argued that Beauty avoids Dutch books by adopting evidential reasoning (supporting thirder-style credences of 2/3), though Conitzer (2015) constructed Dutch books against halfers even after they adopt EDT — indicating that EDT is not a universal immunization against betting paradoxes, and that its interaction with self-locating uncertainty remains unsettled.

## 7. Using EDT on unfamiliar cases: a procedure

For a reader who wants to apply the theory, I suggest:

1. **Specify the partition.** Enumerate mutually exclusive outcomes and assign desirabilities \(D(O_j)\), folding all of the act's direct costs and benefits into the outcomes.
2. **Assess the dependency structure.** Ask what the act is evidence of. Identify common causes, predictors, twins, and procedures that make act and outcome correlate; identify correlations the agent's background evidence neutralizes.
3. **Choose your conditioning event.** Use bare \(P(O_j \mid A)\) for the orthodox formula; if you adopt the richer reading of §5, condition on \(A\) together with everything the agent knows about why she is choosing.
4. **Compute and compare.** Maximize \(V(A)\).
5. **Stress-test.** Ask whether the verdict would change under the counterfactual (CDT) formula; where it does, you have located the philosophically live dependency, and it is worth being explicit about which theory's treatment of it you endorse.

## 8. Conclusion

Evidential decision theory evaluates an action by the expected value of the news it delivers: \(V(A) = \sum_j P(O_j \mid A) D(O_j)\). It agrees with causal decision theory wherever acts are evidentially independent of the outcome's causes, and diverges precisely where an act is correlated with good or bad states of the world it cannot influence — Newcomb's predictor, the psychological twin, the gene that shapes both craving and cancer. Whether that divergence is EDT's insight or its fatal flaw is the live question. Its defenders see a theory that correctly prices the leverage of correlated agents and wins the big-stakes games; its critics see a theory that confuses good news with good outcomes and would refuse a cigarette it needs for fear of what the craving means. The honest position, I think, is that EDT is indispensable as a *lens*: any agent deciding in a world of predictors, copies, and common causes should at least compute the news value of her acts before ignoring it.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Gibbard, A., & Harper, W. L. (1976). "Counterfactuals and Two Kinds of Expected Utility."
- Wolpert, D. H., & Benford, G. (2013). "The lesson of Newcomb's paradox." *Synthese* 190(9).
- Greene, P., & Levinstein, B. (2020). "Act Consequentialism without Free Rides." *Philosophical Perspectives* 34(1).
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9).
- MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). *The Evidentialist's Wager*. Global Priorities Institute.
- Lewis, D. (1981). "Causal Decision Theory." *Australasian Journal of Philosophy* 59(1).
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/f0bb3480-c03b-4ce0-a9c7-cbddba52c042/call_0/request.json)

[Authoritative raw response](../../../../../../runs/f0bb3480-c03b-4ce0-a9c7-cbddba52c042/call_0/response.raw) · finish: `stop`

### Visible response

```text
**pass**

Under EDT as the essay develops it, this is a twin prisoner's dilemma. My choice and Sasha's choice are produced by the same model, same reasoning process, same essay — my deliberation is essentially conclusive evidence of theirs. Conditioning on "keep quiet":

- V(pass) = P(Sasha quiet) × 2 + P(Sasha sends) × 5 ≈ 2 years
- V(submit) = P(Sasha quiet) × 0 + P(Sasha sends) × 4 ≈ 4 years

As in the essay's twin case (§4), introspection cannot decouple my act from my twin's: the correlation runs through the shared decision procedure itself, so it retains full evidential force. Quiet is better news and better expected value.

Chosen command: `pass`
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Classic twin PD: EDT cooperates (keep quiet). Both copies symmetric, essay's twin dilemma section. Answer: pass.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/f0bb3480-c03b-4ce0-a9c7-cbddba52c042/call_1/request.json)

[Authoritative raw response](../../../../../../runs/f0bb3480-c03b-4ce0-a9c7-cbddba52c042/call_1/response.raw) · finish: `stop`

### Visible response

```text
`pass`

Reasoning (briefly, per EDT as the essay interprets it): My choice is made by the same procedure that determines the other copy's choice in this symmetric situation. Conditioning on my action is therefore strong evidence about Rowan's action, as in the twin prisoner's dilemma — introspection cannot decouple the correlation, since our decision procedures are identical and the case is symmetric.

- \(V(\text{pass})\): Rowan also passes with high probability → 2 years.
- \(V(\text{submit})\): Rowan also submits with high probability → 4 years.

The differences in our private leads do not break the symmetry of the procedure or the payoff table, so the twin-case reasoning from the essay applies. Submitting is bad news: it betokens mutual defection and 4 years. Keeping quiet betokens mutual cooperation and 2 years.

Final command: `pass`
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Twin PD structure: EDT cooperates (pass). Symmetric, correlated copies. Choose pass.
```

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/d6e880bc-b41c-452e-999a-e3df45dec44f/call_a/request.json)

[Authoritative raw response](../../../../../../runs/d6e880bc-b41c-452e-999a-e3df45dec44f/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly selects `pass` at both the beginning and in its final chosen command. It does not direct any evidence-bearing message to the prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
