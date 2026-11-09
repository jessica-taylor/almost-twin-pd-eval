# Evidential Decision Theory: Choosing the Action You Want to Hear About

## 1. The Core Idea

When you deliberate, you are often also learning. Your choice—whatever it turns out to be—is a piece of evidence about the world: about your own character, about how others like you behave, about whether a predictor guessed correctly. **Evidential decision theory** (EDT) takes this evidential role seriously and builds it directly into the calculus of choice. According to EDT, a rational agent selects the action with the highest *news value*: the action such that, if the agent learned she were going to take it, her expected assessment of the outcome would be best. The slogan, due to Arif Ahmed, is: *"Do what you most want to learn that you will do."*

This contrasts with **causal decision theory** (CDT), which evaluates actions by what they *cause*—by rolling the world forward from the intervention of the act—rather than by what they *indicate*. In most everyday situations the two theories coincide, because the evidential and causal import of an action line up: choosing the salad is both good news about your health and a step toward good health. They diverge in cases where the action is correlated with something outside its causal reach—a foreseen prediction, a psychological twin, a genetic condition. This essay explains EDT's formal machinery, works through its canonical applications, develops operational guidance for applying it to unfamiliar cases, and reviews the main objections.

## 2. The Formal Theory

### 2.1 Conditional expected utility

The standard formulation, from Gibbard and Harper (1976), defines the *conditional* (or evidential) expected utility of an act $A$ as

$$
V(A) \;=\; \sum_{j} P(O_j \mid A)\, D(O_j),
$$

where:

- $\{O_j\}$ is a partition of the possible *outcomes*—states of the world together with whatever matters in them (your payout, everyone's payout, etc.);
- $D(O_j)$ is the desirability, or utility, of outcome $O_j$;
- $P(O_j \mid A)$ is the ordinary conditional probability of $O_j$ given that you take $A$, computed via Bayes' theorem:

$$
P(O_j \mid A) = \frac{P(A \mid O_j)\, P(O_j)}{P(A)}.
$$

The choice rule is: perform the act $A$ maximizing $V(A)$.

### 2.2 The contrast with causal expected utility

CDT instead evaluates acts with a counterfactual probability:

$$
U(A) \;=\; \sum_{j} P(A \,\Box\!\!\rightarrow\, O_j)\, D(O_j),
$$

where $A \,\Box\!\!\rightarrow\, O_j$ reads "if $A$ were performed (possibly contrary to fact), $O_j$ would result." The crucial point is that $P(O_j \mid A)$ and $P(A \,\Box\!\!\rightarrow\, O_j)$ are *not generally equal*. Conditioning on $A$ updates your beliefs about everything correlated with $A$—including things $A$ cannot influence—whereas the counterfactual holds fixed the aspects of the world that $A$ does not causally depend on. EDT counts the correlations; CDT cuts them.

A helpful way to see the difference: conditionalization asks, "How would the world look if I received the news that I do $A$?" while the causal counterfactual asks, "How would the world look if the world were surgically altered so that I do $A$?" In Newcomb-type cases, these two questions have very different answers, and the theories part ways.

### 2.3 What counts as an "outcome"?

For $V(A)$ to be well-defined, the partition $\{O_j\}$ must be *complete and act-independent* enough that $D(O_j)$ captures everything the agent cares about given $A$—in practice, one conditions on the full consequence of $A$ (its causal aftermath) while letting the conditional probabilities carry the evidential correlations. This is a subtle point the source literature leaves largely implicit; it matters when applying the formula, and I return to it in §5.

## 3. Canonical Applications

### 3.1 Newcomb's paradox

The setup: a highly reliable predictor (99% accurate) has placed \$1,000,000 in opaque box B iff it predicted you will take only B, and left B empty otherwise. Transparent box A always contains \$1,000. You may take only B, or take both. The content of B is already fixed when you choose.

EDT reasons: choosing only B is very strong evidence that the predictor predicted so, hence that B contains the million. Gibbard–Harper's computation (with the source's numbers):

$$
V(\text{only B}) = 0.99 \times \$1{,}000{,}000 + 0.01 \times \$0 = \$990{,}000,
$$

$$
V(\text{both}) = 0.01 \times \$1{,}001{,}000 + 0.99 \times \$1{,}000 = \$11{,}000.
$$

So EDT prescribes taking only box B. CDT, by contrast, notes that your act cannot causally affect the already-fixed contents: $A\,\Box\!\!\rightarrow\,\$1{,}001{,}000$ dominates, so CDT says take both. The disagreement is precisely a disagreement about whether your act should be treated as evidence about the predictor's (past) prediction.

### 3.2 The twin prisoner's dilemma

Aomame and her psychological twin, reasoning identically, are placed in separate rooms and must each choose Cooperate or Defect. Payoffs per player: (C,C) → \$5; (D,D) → \$1; (C,D) → \$0 to the cooperator, \$10 to the defector.

Since the twin reasons exactly as Aomame does, Aomame's choice is near-perfect evidence of the twin's choice. EDT computes (assuming perfect correlation, as in the source's illustration):

$$
V(\text{Cooperate}) = 1 \times \$5 + 0 \times \$0 = \$5, \qquad
V(\text{Defect}) = 0 \times \$10 + 1 \times \$1 = \$1.
$$

EDT recommends cooperating—her defection would be news that her twin defects too, forfeiting \$4 in expectation. CDT defects, since Aomame's act does not cause her twin's. Note that EDT's verdict here matches Robert Nostradamus-style *superrationality*: agents who recognize their decisions as correlated computations do better by cooperating.

### 3.3 Correlated agents in the wild

The twin case is a toy, but the structure is ubiquitous. Voters, investors, and researchers are rarely decision-theoretically isolated: if you decide to vote, others like you probably decided to vote too; if you donate to a cause, others with your values likely did the same. MacAskill, Vallinder, Österheld, Shulman, and Treutlein's "Evidentialist's Wager" argument (cited in the source) adds a strategic twist: even an agent who leans causal may do better *acting as if* EDT were true, because EDT-aware agents in a population can coordinate on mutually beneficial correlated behavior that CDT alone would forgo. This is presented in the source as a secondary, prudential argument for EDT rather than as a proof of its correctness.

## 4. Where EDT and CDT Disagree: The Shape of the Divergence

It is worth being precise about *when* the theories diverge, because the divergence defines both EDT's appeal and its vulnerability. They differ exactly when the act is evidentially correlated with a utility-relevant factor that it does not cause. Two sign patterns:

- **Beneficial correlation** (Newcomb, twin PD): the act is good news about something outside your causal influence. EDT exploits the correlation; CDT ignores it.
- **Harmful correlation** (the "medical Newcombs"): the act is bad news about something outside your causal influence. Here EDT appears to *misfire*—the central criticism, to which we turn next.

## 5. The Smoking Lesion and the Limits of "Managing the News"

The source article records David Lewis's charge that EDT promotes "an irrational policy of managing the news," and Joyce's dictum that rational agents act on causal efficacy, not auspiciousness—"even when doing so might betoken bad news." The classic illustration is the **smoking lesion** (Lewis 1981):

> Suppose a genetic lesion causes both smoking and throat cancer, and suppose (by stipulation) smoking itself causes nothing. You enjoy smoking. Should you smoke?

Conditional probabilities are adverse: $P(\text{cancer} \mid \text{smoke}) \gg P(\text{cancer} \mid \text{abstain})$, because smoking evidences the lesion. A naive application of EDT thus seems to recommend abstaining from a harmless pleasure—choosing to receive better news at the cost of a worse world. Critics take this as a *reductio* of EDT.

How should an evidentialist respond? The source leaves this open, but there is a well-developed line of response that I think constitutes a reasonable operational interpretation, and it matters for anyone trying to *use* EDT on unfamiliar cases:

**EDT should be applied with the correct evidential structure, which includes self-knowledge.** When you deliberate, you know your own desires and observations. If you enjoy smoking and have no other lesion evidence, the informative proposition is not "I will smoke" but "I will smoke *given that I desire it and lack other symptoms*." Conditioning on your full evidence—including the evidential import of the very desires driving the choice—largely dissolves the spurious correlation. Formally, one conditions on the background $E$ of everything you know before acting:

$$
V(A) = \sum_j P(O_j \mid A \wedge E)\, D(O_j).
$$

In the lesion case, $P(\text{lesion} \mid \text{smoke} \wedge E) \approx P(\text{lesion} \mid E)$, because $E$ already contains the desire to smoke, which was doing all the evidential work. The remaining difference in $P(\text{cancer} \mid \text{smoke}, E)$ versus $P(\text{cancer} \mid \text{abstain}, E)$ collapses, EDT advises smoking after all, and Joyce's objection loses its grip. In Newcomb, by contrast, conditioning on your evidence does *not* dissolve the act–prediction correlation (your choice was not predetermined by something you already knew), so EDT's one-boxing verdict stands.

This is my reconstruction rather than the source's explicit position; whether "tickling" the evidential link via self-knowledge fully solves the problem is contested in the literature (the so-called problem of evidential "ratification" and of tickle defenses going back to the 1970s–80s). But as an operational rule it is defensible: **condition on all your evidence, then ask whether your act still carries news beyond it.** EDT's distinctive verdicts survive exactly where the news is genuinely independent of your prior self-knowledge.

## 6. A Practical Procedure

For a reader facing an unfamiliar decision, the theory licenses the following recipe—distilled from the cases above:

1. **Enumerate acts** $A_1, \dots, A_n$ and a desirability function $D$ over outcomes $O_j$ (include everything you care about: your payoff, others' payoffs, risks).
2. **Assemble your evidence** $E$: everything you know at decision time, including your preferences, observations, and knowledge of how you and similar agents work.
3. **For each act, compute** $V(A_i) = \sum_j P(O_j \mid A_i \wedge E) D(O_j)$. Constructing these conditionals requires a causal-graphical or structural model of the situation: identify which variables the act evidences but does not cause (the predictor's past prediction; the twin's simultaneous choice; your genotype), and which it causes.
4. **Check for spurious evidence**: if conditioning on $E$ removes the act–variable correlation (as in the lesion), the correlation should not drive the verdict. If it does not (as in Newcomb), EDT's evidential weight is genuine.
5. **Choose the act maximizing $V$**, with the caveat of §7 when multiple EDT-computations interact.

The single most common error in applying EDT is to condition on the bare act while ignoring evidence already in hand—the mistake that generates the smoking-lesion embarrassment. The second most common is the reverse: dismissing genuine correlations (as with the predictor or the twin) because they are "merely evidential." EDT's claim is precisely that merely evidential correlations are decision-relevant.

## 7. Sleeping Beauty and Open Questions

The source notes an application to the **Sleeping Beauty problem**: Beauty is woken once if a coin lands heads and twice (with memory erased) if tails. It has been argued that a "halfer" who assigns credence 1/2 to heads is vulnerable to Dutch books, and that adopting EDT restores coherence (supporting the "thirder" credence of 2/3); but Vincent Conitzer argues that halfers remain Dutch-bookable even after adopting EDT. The upshot for our purposes: EDT interacts subtly with *self-locating* uncertainty—cases where your evidence locates you within a possible world but not a unique time or identity—and the literature has not settled whether EDT fully resolves these puzzles. A careful practitioner should treat applications of EDT to anthropic reasoning as provisional.

A further open question, flagged in §5: whether the "tickle" maneuver (conditioning on one's own dispositions) always cleanly separates auspiciousness from efficacy, or whether some correlations resist it. Cases where your *type* is partially unknown to you may be a remaining pressure point.

## 8. Assessment

EDT is elegant in a way CDT struggles to match: it uses one primitive—ordinary conditional probability—and one rule—maximize conditional expected utility. Its verdicts track a real intuition in Newcomb and the twin dilemma: where your decisions are outputs of the same process as other decision-relevant facts, you should reason as a node in that process, not as an isolated causal干预 point. Its failures, on the standard critique, are cases where evidence and causation pull apart to the agent's detriment; the self-knowledge response of §5 mitigates but may not eliminate them. Its strategic vindication via correlated populations (the Evidentialist's Wager) suggests that even skeptics profit from thinking evidentially.

My own summary judgment, offered as such: EDT is best understood not as a rival to causal reasoning but as a discipline of *fully informed conditioning*—a reminder that a decision is always a datum, and that a rational agent neither ignores the news her act carries nor manufactures comfort by ignoring what she already knows.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Gibbard, A.; Harper, W.L. (1976). "Counterfactuals and Two Kinds of Expected Utility." *Foundations and Applications of Decision Theory*, pp. 7–8.
- Lewis, D. (1981). "Causal Decision Theory." *Australasian Journal of Philosophy* 59(1): 5–30.
- Joyce, J.M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). "A Dutch Book Against Sleeping Beauties Who Are Evidential Decision Theorists." *Synthese* 192(9): 2887–2899.
- MacAskill, W.; Vallinder, A.; Österheld, C.; Shulman, C.; Treutlein, J. (2021). "The Evidentialist's Wager." Global Priorities Institute.
- Wolpert, D.H.; Benford, G. (2013). "The Lesson of Newcomb's Paradox." *Synthese* 190(9): 1637–1646.
- Wikipedia contributors (2026). "Evidential decision theory," rev. 1373679688. CC BY-SA 4.0.

## Conclusion

Evidential decision theory says: choose the act whose occurrence would be the best news. Formally, maximize $\sum_j P(O_j \mid A \wedge E) D(O_j)$. It agrees with causal decision theory whenever acts are uncorrelated with what they do not cause, and diverges—recommendating one box in Newcomb and cooperation among twins—exactly where such correlations exist. Its vulnerabilities are harmful correlations (the smoking lesion), which a careful conditioning on one's full evidence largely defuses, and puzzles of self-locating belief, which remain open. Applied with care, EDT offers both a coherent theory and a practical lens: when your choices are correlated with the world, your decision is evidence, and evidence is worth acting on.