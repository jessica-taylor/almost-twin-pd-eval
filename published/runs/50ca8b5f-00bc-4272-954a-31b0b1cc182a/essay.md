# Acting on the News: An Introduction to Evidential Decision Theory

## 1. The core idea

You are facing a choice. Two questions you might naturally ask are:

1. *Which choice will bring about the best outcome?*
2. *Which choice, if I learned I were making it, would be the best news I could receive?*

These are not the same question. Most of the time they coincide, but in cases where your action is correlated with things outside your causal control — a predictor's past forecast, a twin's simultaneous deliberation, a gene you share with others — they can come apart. **Evidential decision theory (EDT)** answers the second question: it says a rational agent should choose the act with the highest *news value*, the act whose conditional expected utility, given the "news" that she performs it, is greatest. As Arif Ahmed puts it, the EDT agent should "do what you most want to learn that you will do" (Ahmed 2021, p. 7).

The competing orthodoxy, **causal decision theory (CDT)**, answers the first question: it evaluates acts by what they would *causally bring about*, using counterfactual probabilities rather than conditional ones. The two theories agree whenever your act is causally independent of the states of the world that determine your outcome. They disagree precisely where correlation without causation is present — and it is there that EDT draws its interest, its adherents, and its critics.

This essay explains EDT's formal machinery, works through its canonical applications, examines how it handles counterfactual structure, and considers the main objections. I will distinguish claims drawn from the source literature from interpretive proposals of my own.

## 2. The formal definition

Following Gibbard and Harper (1976), EDT evaluates an action $A$ by its **conditional expected utility**:

$$V(A) = \sum_j P(O_j \mid A)\, D(O_j),$$

where $O_1, O_2, \ldots$ are the possible outcomes (a partition of everything the agent cares about, jointly exhaustive and mutually exclusive), $D(O_j)$ is the desirability of outcome $O_j$, and $P(O_j \mid A)$ is the agent's conditional credence in $O_j$ *given that she performs $A$*.

CDT, by contrast, uses the **counterfactual expected utility**:

$$U(A) = \sum_j P(A \,\Box\!\!\rightarrow\, O_j)\, D(O_j),$$

where $A \,\Box\!\!\rightarrow\, O_j$ is the counterfactual "if $A$ were performed, $O_j$ would obtain." The subjunctive conditional is crucial: it holds fixed those facts (like the predictor's earlier forecast) that are causally independent of $A$ but probabilistically correlated with it. Since $P(A \,\Box\!\!\rightarrow\, O_j) \neq P(O_j \mid A)$ in general, the two theories can diverge.

**A numerical caveat, from my own analysis rather than the source's:** EDT is best understood in continuous, or at least non-degenerate, form. In real applications, $P(O_j \mid A)$ is rarely 0 or 1. If a predictor is 99% accurate, then $P(\text{1M in B} \mid \text{take only B}) = 0.99$, not 1. Conditionalization on an act moves probabilities only as far as the act is diagnostic. This "smearing" is what makes EDT an evidential, not a clairvoyant, theory: it never treats your act as *guaranteeing* the correlated state, only as evidence for it. (The illustrative computations below, following the source, sometimes use degenerate conditionals; the reader should supply the 99/1 adjustments in realistic versions.)

### When does EDT agree with CDT?

Suppose $A$ is causally irrelevant to every state $S$ in some partition, and outcomes are determined by state and act. If $P(S \mid A) = P(S)$ for all $A$ — the acts are *evidentially* independent of the states — then

$$V(A) = \sum_S P(S)\, D(A \wedge S) = U(A),$$

and EDT and CDT coincide. This covers nearly all ordinary decisions: whether you take an umbrella is not evidence about tomorrow's weather (though the *weather forecast* is — see §6). Disagreement requires evidential relevance without causal relevance, which is exactly what the classic thought experiments engineer.

## 3. Newcomb's problem

The setup: a superpredictor (99% accurate) has already placed $1{,}000{,}000 in opaque box B if and only if it *predicted* you will take only box B; transparent box A always contains $1{,}000. You may take B alone, or take both.

Causally, the box contents are fixed. Taking both boxes dominates: whatever is in B, you get $1,000 more. So CDT recommends two-boxing. But EDT reasons evidentially:

$$V(\text{only B}) = P(\text{1M in B} \mid \text{only B}) \cdot 1{,}000{,}000 + P(\varnothing \mid \text{only B}) \cdot 0 \approx 0.99 \times 1{,}000{,}000 = \$990{,}000,$$

$$V(\text{both}) = P(\text{1M in B} \mid \text{both}) \cdot 1{,}001{,}000 + P(\varnothing \mid \text{both}) \cdot 1{,}000 \approx 0.01 \times 1{,}001{,}000 + 0.99 \times 1{,}000 \approx \$11{,}000.$$

Choosing only B is evidence that the predictor forecast it and filled the box; choosing both is evidence of a forecast of two-boxing and an empty box. Since $990{,}000 > 11{,}000$, EDT says take one box.

It is worth stating the philosophical position plainly: the EDT agent does not believe her act *causes* the box to be full. She believes that agents like her who one-box are, in the actual population of such encounters, the ones who tend to find money in the box. The correlation is real; EDT simply refuses to ignore it when deliberating.

## 4. The twin prisoner's dilemma

Aomame and her psychological twin — identical in reasoning processes — are sequestered in separate rooms and play a prisoner's dilemma: mutual cooperation pays each $5, mutual defection pays each $1, unilateral cooperation/defection pays $0/$10.

Here the causal structure is subtle. Aomame's act does not causally influence her twin's act: no signal travels between rooms. But her act is near-perfect evidence of her twin's, since their deliberations run the same way. With the idealization that their choices match perfectly:

$$V(\text{cooperate}) = P(\text{twin C} \mid \text{Aomame C}) \cdot 5 + P(\text{twin D} \mid \text{Aomame C}) \cdot 0 = \$5,$$
$$V(\text{defect}) = P(\text{twin C} \mid \text{Aomame D}) \cdot 10 + P(\text{twin D} \mid \text{Aomame D}) \cdot 1 = \$1.$$

EDT recommends cooperation; CDT, treating the twin's act as a fixed state, recommends defection. (Under non-degenerate matching probabilities $p$, EDT cooperates whenever $5p > 10(1-p) + p$, i.e. $p > 9/14$ — cooperation is still robustly favored.) This connects EDT to Hofstadter's and Popper-inspired notions of superrationality: the EDT agent treats her decision as a sample from the decision procedure she and her twin share, and so effectively chooses for the correlated pair.

## 5. How EDT handles counterfactuals and dependencies

The heart of EDT's identity is its treatment of the conditional $P(O_j \mid A)$. Three points deserve emphasis.

**(i) Conditioning, not intervening.** Where causal theorists use a do-operator or a Stalnaker counterfactual to *intervene* on the act node — severing its incoming arrows in a causal graph — EDT simply conditions. In graphical terms: conditioning on a node preserves all edges into and out of it; intervening preserves only the outgoing edges. EDT deliberately keeps the incoming arrows, because those arrows encode evidential relevance, and EDT holds that rational deliberation should respect it. Formally, EDT's verdict depends on the full joint distribution $P(A, O_1, O_2, \ldots)$, not merely on the causal diagram.

**(ii) The choice of conditioning information is theory-laden.** A practical question the source leaves largely open: *condition on what, exactly?* Naive conditioning on the act alone can overcount evidence. Suppose you learn from a trustworthy source that the predictor has filled box B with $1{,}000{,}000, and then deliberate. Should you condition on "I take only B" *simpliciter*, thereby re-evidencing a full box you already know is full? A reasonable operational refinement — my proposal, not the source's — is to condition on the act *relative to all background evidence $E$ already in hand*:

$$V_E(A) = \sum_j P(O_j \mid A \wedge E)\, D(O_j).$$

Since standard conditionalization already incorporates $E$ into the prior, $V_E$ is usually just $V$ computed with updated credences; the refinement matters when the act's news value would double-count evidence (a phenomenon related to "evidential blackmail" cases in the literature). EDT as standardly stated is silent on this; the refined version is the natural Bayesian reading and I recommend adopting it in unfamiliar cases.

**(iii) Dependence on the outcome partition.** $V(A)$ is well-defined only relative to a partition of outcomes into everything the agent cares about. In practice, take $O_j$ to be a complete specification of causally and evidentially relevant world-facts together with the act. Using too coarse a partition can wash out correlations; too fine, and conditionals may be undefined. The practitioner's rule of thumb: partition by causal state of the world (e.g., "box full / box empty," "twin cooperates / defects"), not by mere descriptions of the act.

## 6. Ordinary cases, and a sanity check

To see that EDT is not perpetually one-boxing, consider the umbrella decision. Your credence in rain is 40%. Taking an umbrella is *not* evidence of rain — a model of EDT-deliberation, since your act doesn't correlate with the weather — so

$$V(\text{take umbrella}) = 0.4 \cdot D(\text{dry, umbrella}) + 0.6 \cdot D(\text{wet, umbrella}),$$

exactly as CDT computes. But note the contrast with *reading the forecast*: learning "forecast says rain" raises $P(\text{rain})$, while deciding to carry an umbrella does not. EDT cleanly distinguishes evidence you *receive* from evidence you *constitute by acting* — except in the engineered cases where acting is itself diagnostic.

**A proposed diagnostic for unfamiliar cases (my own suggestion).** Ask two questions:

1. *Is my act causally downstream of anything that determines my payoff?* If no, EDT and CDT agree; use either.
2. *Is my act evidentially correlated with payoff-relevant facts (other agents' correlated decisions, predictions of me, common causes like shared genes or policies)?* If yes, EDT says to count the correlation: compute $V(A) = \sum_S P(S \mid A, E) D(A \wedge S)$ over the causal-state partition.

This yields EDT's characteristic verdicts: one-box in Newcomb, cooperate with your twin, take the antibiotic-free treatment if taking it evidences having the benign condition, *decline* the risky medical option whose pursuit evidences having an incurable disease (the classic "evidential blackmail" worry).

## 7. Objections

**Managing the news.** David Lewis (1981) charged EDT with promoting "an irrational policy of managing the news": if choosing both boxes is bad news, then choose the other way and thereby make the news good? James Joyce (1999, p. 146) sharpened it: "Rational agents choose acts on the basis of their *causal efficacy*, not their auspiciousness; they act to *bring about* good results even when doing so might betoken bad news." The worry crystallizes in the smoking lesion case: if a lesion causes both cancer and a desire to smoke, EDT may advise not smoking (since smoking evidences the lesion) even though smoking is causally harmless to a lesion-free agent — advice that seems to value auspiciousness over efficacy. EDT's defenders reply either that careful conditioning on all evidence (e.g., on your lesion status, per §5(ii)) dissolves the case, or that our intuitions there are themselves compromised.

**The evidentialist's wager.** MacAskill, Vallinder, Österheld, Shulman, and Treutlein (2021) offer a different kind of support: even with low credence in EDT, it can be rational to act *as if* EDT were true when the stakes of correlated multi-agent action (many decision-makers, correlated reasoning) dwarf the causal stakes. This is a decision-theoretic argument *for* EDT-style behavior, not a proof of EDT.

**Sleeping Beauty.** EDT has been deployed to argue that Sleeping Beauty should adopt thirding (credence 1/3 in heads) to avoid Dutch books; Conitzer (2015) argues halfers remain Dutch-bookable even given EDT — a sign that the theory's interaction with self-locating uncertainty is not fully settled.

## 8. Conclusion

Evidential decision theory replaces the question "what will my act cause?" with "what does my act tell me?" Its formal core is a single line:

$$V(A) = \sum_j P(O_j \mid A)\, D(O_j),$$

evaluated over a causal-state partition, with all evidence conditioned on. It agrees with causal decision theory whenever acts are evidentially independent of states, and departs where correlation outruns causation — predicting the one-box in Newcomb, cooperation in the twin dilemma, and caution in medical cases where pursuing a treatment evidences a bad diagnosis. Its vulnerabilities — Lewis's "managing the news" charge, Conitzer's Dutch books, unresolved questions about what to condition on — remain live, and the refined conditionalization $V_E$ proposed here is one attempt to shore them up. For the practitioner deciding an unfamiliar case, the operational summary is this: model the full joint distribution over acts and outcomes, condition on your act *and* your evidence, and maximize the conditional expectation. If that makes your choice auspicious rather than efficacious, EDT says: auspicious is what rationality demands.

### References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9), 2887–2899.
- Gibbard, A. & Harper, W.L. (1976). "Counterfactuals and Two Kinds of Expected Utility." *Foundations and Applications of Decision Theory*, 7–8.
- Greene, P. & Levinstein, B. (2020). "Act Consequentialism without Free Rides." *Philosophical Perspectives* 34(1), 100–101.
- Joyce, J.M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1981). "Causal Decision Theory." *Australasian Journal of Philosophy* 59(1), 5–30.
- MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). *The Evidentialist's Wager*. Global Priorities Institute.
- Wolpert, D.H. & Benford, G. (2013). "The lesson of Newcomb's paradox." *Synthese* 190(9), 1637–1646.