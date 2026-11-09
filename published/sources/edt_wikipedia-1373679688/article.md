# Evidential decision theory

By Wikipedia contributors ([revision history](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&action=history)). [Permanent revision 1373679688](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688), 2026-09-07T07:36:26Z.

License: [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).

Conversion modifications: Mechanically converted revision-pinned rendered HTML to Markdown; retained article prose, headings, lists, tables, citations and references. Recovered formula LaTeX from MathML annotations/image alt text, or the same revision wikitext in order when counts match; did not rewrite, summarize or repair formulas. Removed navigation, edit controls, styles and website UI; excluded media bytes/URLs while retaining meaningful text descriptions. Prepended title, contributor attribution, revision/history URLs, license and conversion notice.

Individual media and third-party quoted material may have separate rights. Source reuse or adaptations in future publications may carry attribution/share-alike or other obligations.

School of thought within decision theory

**Evidential decision theory** (EDT) is a school of thought within [decision theory](https://en.wikipedia.org/wiki/Decision_theory) which states that, when a rational agent is confronted with a set of possible actions, one should select the action with the highest *news value*, that is, the action which would be indicative of the best outcome [in expectation](https://en.wikipedia.org/wiki/Expected_value) if one received the "news" that it had been taken. In other words, it recommends to "do what you most want to learn that you will do."<a id="cite_ref-Ahmed_1-0"></a><sup>[[1]](#cite_note-Ahmed-1)</sup><sup>: 7 </sup>

EDT contrasts with [causal decision theory](https://en.wikipedia.org/wiki/Causal_decision_theory) (CDT), which prescribes taking the action that will causally produce the best outcome. While these two theories agree in many cases, they give different verdicts in certain philosophical thought experiments. For example, EDT prescribes taking only one box in [Newcomb's paradox](https://en.wikipedia.org/wiki/Newcomb%27s_paradox), while CDT recommends taking both boxes.<a id="cite_ref-Ahmed_1-1"></a><sup>[[1]](#cite_note-Ahmed-1)</sup><sup>: 22–26 </sup>

## Formal description

In a 1976 paper, [Allan Gibbard](https://en.wikipedia.org/wiki/Allan_Gibbard) and William Harper distinguished between two kinds of [expected utility](https://en.wikipedia.org/wiki/Expected_utility) maximization. EDT proposes to maximize the expected utility of actions computed using [conditional probabilities](https://en.wikipedia.org/wiki/Conditional_probability), namely

\[
V(A)=\sum\limits_{j} P(O_j | A) D(O_j),
\]

where \(D(O_j)\) is the desirability of outcome \(O_j\) and \(P(O_j | A)\) is the conditional probability of \(O_j\) given that action \(A\) occurs.<a id="cite_ref-GibbardHarper_2-0"></a><sup>[[2]](#cite_note-GibbardHarper-2)</sup> This is in contrast to the counterfactual formulation of expected utility used by causal decision theory

\[
U(A)=\sum\limits_{j} P(A \mathrel{\Box{\rightarrow}} O_j) D(O_j),
\]

where the expression \(P(A \mathrel{\Box{\rightarrow}} O_j)\) indicates the probability of outcome \(O_j\) in the [counterfactual](https://en.wikipedia.org/wiki/Counterfactual) situation in which action \(A\) is performed. Since \(P(A \mathrel{\Box{\rightarrow}} O_j)\) and \(P(O_j | A)\) are not always equal, these formulations of expected utility are not equivalent,<a id="cite_ref-GibbardHarper_2-1"></a><sup>[[2]](#cite_note-GibbardHarper-2)</sup> leading to differences in actions prescribed by EDT and CDT.

## Thought experiments

Different decision theories are often examined in their recommendations for action in different [thought experiments](https://en.wikipedia.org/wiki/Thought_experiment).

### Newcomb's paradox

Main article: [Newcomb's paradox](https://en.wikipedia.org/wiki/Newcomb%27s_paradox)

In Newcomb's paradox, there is a predictor, a player, and two boxes designated A and B. The predictor is able to reliably predict the player's choices— say, with 99% accuracy. The player is given a choice between taking only box B, or taking both boxes A and B. The player knows the following:<a id="cite_ref-Wolpert_3-0"></a><sup>[[3]](#cite_note-Wolpert-3)</sup>

- Box A is transparent and always contains a visible $1,000.

- Box B is opaque, and its content has already been set by the predictor:

- If the predictor has predicted the player will take both boxes A and B, then box B contains nothing.

- If the predictor has predicted that the player will take only box B, then box B contains $1,000,000.

The player does not know what the predictor predicted or what box B contains while making the choice. Should the player take both boxes, or only box B?

Evidential decision theory recommends taking only box B in this scenario, because taking only box B is strong evidence that the predictor anticipated that the player would only take box B, and therefore it is very likely that box B contains $1,000,000. Conversely, choosing to take both boxes is strong evidence that the predictor knew that the player would take both boxes; therefore we should expect that box B contains nothing.<a id="cite_ref-Ahmed_1-2"></a><sup>[[1]](#cite_note-Ahmed-1)</sup><sup>: 22 </sup>

Conversely, [causal decision theory](https://en.wikipedia.org/wiki/Causal_decision_theory) (CDT) would have recommended that the player take both boxes, because by that time the predictor has already made a prediction (therefore, the action of the player will not affect the outcome).

Formally, the expected utilities in EDT are

\[
\begin{align}
V(\text{take only B}) &= P(\text{1M in box B}|\text{take only B}) \times \$1,000,000 + P(\text{nothing in box B}|\text{take only B}) \times \$0 \\
&= 0.99 \times \$1,000,000 + 0.01 \times \$0 = \$990,000 \\
V(\text{take both boxes}) &= P(\text{1M in box B}|\text{take both boxes}) \times \$1,001,000 + P(\text{nothing in box B}|\text{take both boxes}) \times \$1,000 \\
&= 0.01 \times \$1,001,000 + 0.99 \times \$1,000 = \$11,000
\end{align}
\]

Since \(V(\text{take only B}) > V(\text{take both boxes})\), EDT recommends taking only box B.

### Twin prisoner's dilemma

See also: [Prisoner's dilemma](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma)

In this variation on the [Prisoner's Dilemma](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma) thought experiment, an agent must choose whether to cooperate or defect against her psychological twin, whose reasoning processes are exactly analogous to her own.

Aomame and her psychological twin are put in separate rooms and cannot communicate. If they both cooperate, they each get $5. If they  both defect, they each get $1. If one cooperates and the other defects, then one gets $10, and the other gets $0. Assuming Aomame only cares about her individual payout, what should she do?<a id="cite_ref-GreeneLevinstein_4-0"></a><sup>[[4]](#cite_note-GreeneLevinstein-4)</sup>

Evidential decision theory recommends cooperating in this situation, because Aomame's decision to cooperate is strong evidence that her psychological twin will also cooperate, meaning that her expected payoff is $5. On the other hand, if Aomame defects, this would be strong evidence that her twin will also defect, resulting in an expected payoff of $1. Formally, the expected utilities are

\[
\begin{align}
V(\text{Aomame cooperates}) &= P(\text{twin cooperates}|\text{Aomame cooperates}) \times \$5 + P(\text{twin defects}|\text{Aomame cooperates}) \times \$0  \\
&= 1 \times \$5 + 0 \times \$0 = \$5 \\
V(\text{Aomame defects}) &= P(\text{twin cooperates}|\text{Aomame defects}) \times \$10 + P(\text{twin defects}|\text{Aomame defects}) \times \$1 \\
&= 0 \times \$10 + 1 \times \$1 = \$1.
\end{align}
\]

Since \(V(\text{Aomame cooperates}) > V(\text{Aomame defects})\), EDT recommends cooperating.

### Sleeping beauty problem

Main article: [Sleeping beauty problem](https://en.wikipedia.org/wiki/Sleeping_beauty_problem)

Evidential decision theory has been applied to the Sleeping Beauty Problem in order to avoid [Dutch book arguments](https://en.wikipedia.org/wiki/Dutch_book_arguments). It has been argued that Sleeping Beauty is subject to Dutch books if she assigns a credence of 1/2 of the coin flip being heads, but can avoid them by adopting evidential decision theory. However, Vincent Conitzer argues that halfers are still affected by Dutch books even after adopting evidential decision theory.<a id="cite_ref-5"></a><sup>[[5]](#cite_note-5)</sup>

## Other supporting arguments

Even if one puts less credence on evidential decision theory, it may be reasonable to act as if EDT were true. Namely, because EDT can involve the actions of many correlated decision-makers, its stakes may be higher than causal decision theory and thus take priority.<a id="cite_ref-6"></a><sup>[[6]](#cite_note-6)</sup>

## Criticism

[David Lewis](https://en.wikipedia.org/wiki/David_Kellogg_Lewis) has characterized evidential decision theory as promoting "an irrational 
policy of managing the news".<a id="cite_ref-Lewis1981_7-0"></a><sup>[[7]](#cite_note-Lewis1981-7)</sup> [James M. Joyce](https://en.wikipedia.org/wiki/James_M._Joyce) asserted, "Rational agents choose acts on the basis of their *causal efficacy*, not their auspiciousness; they act to *bring about* good results even when doing so might betoken bad news."<a id="cite_ref-Joyce1999_8-0"></a><sup>[[8]](#cite_note-Joyce1999-8)</sup>

## See also

- [Causal decision theory](https://en.wikipedia.org/wiki/Causal_decision_theory)

- [Decision making](https://en.wikipedia.org/wiki/Decision_making)

- [Expected utility hypothesis](https://en.wikipedia.org/wiki/Expected_utility_hypothesis)

- [Game theory](https://en.wikipedia.org/wiki/Game_theory)

- [Newcomb's paradox](https://en.wikipedia.org/wiki/Newcomb%27s_paradox)

- [Superrationality](https://en.wikipedia.org/wiki/Superrationality)

## References

- <a id="cite_note-Ahmed-1"></a>^ [<sup>***a***</sup>](#cite_ref-Ahmed_1-0) [<sup>***b***</sup>](#cite_ref-Ahmed_1-1) [<sup>***c***</sup>](#cite_ref-Ahmed_1-2) [Ahmed, Arif](https://en.wikipedia.org/wiki/Arif_Ahmed_(philosopher)) (2021). *Evidential Decision Theory*. Cambridge University Press. [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier)) [9781108607865](https://en.wikipedia.org/wiki/Special:BookSources/9781108607865).

- <a id="cite_note-GibbardHarper-2"></a>^ [<sup>***a***</sup>](#cite_ref-GibbardHarper_2-0) [<sup>***b***</sup>](#cite_ref-GibbardHarper_2-1) Gibbard, A.; Harper, W.L. (1976), [*Counterfactuals and Two Kinds of Expected Utility*](https://www.econstor.eu/bitstream/10419/220553/1/cmsems-dp0194.pdf) (PDF), pp. 7–8

- <a id="cite_note-Wolpert-3"></a>**[^](#cite_ref-Wolpert_3-0)** Wolpert, D. H.; Benford, G. (June 2013). "The lesson of Newcomb's paradox". *[Synthese](https://en.wikipedia.org/wiki/Synthese)*. **190** (9): 1637–1646. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1007/s11229-011-9899-3](https://doi.org/10.1007%2Fs11229-011-9899-3). [JSTOR](https://en.wikipedia.org/wiki/JSTOR_(identifier)) [41931515](https://www.jstor.org/stable/41931515). [S2CID](https://en.wikipedia.org/wiki/S2CID_(identifier)) [113227](https://api.semanticscholar.org/CorpusID:113227).

- <a id="cite_note-GreeneLevinstein-4"></a>**[^](#cite_ref-GreeneLevinstein_4-0)** Greene, P.; Levinstein, B. (2020). ["Act Consequentialism without Free Rides"](https://philpapers.org/rec/GREACW-2). *Philosophical Perspectives*. **34** (1): 100–101. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1111/phpe.12138](https://doi.org/10.1111%2Fphpe.12138). [S2CID](https://en.wikipedia.org/wiki/S2CID_(identifier)) [211161349](https://api.semanticscholar.org/CorpusID:211161349).

- <a id="cite_note-5"></a>**[^](#cite_ref-5)** Conitzer, Vincent (2015). ["A Dutch book against sleeping beauties who are evidential decision theorists"](https://philpapers.org/rec/CONADB). *Synthese*. **192** (9). Springer Netherlands: 2887–2899. [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[1705.03560](https://arxiv.org/abs/1705.03560). [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1007/s11229-015-0691-7](https://doi.org/10.1007%2Fs11229-015-0691-7). Retrieved 4 July 2025.

- <a id="cite_note-6"></a>**[^](#cite_ref-6)** MacAskill, William; Vallinder, Aron; Österheld, Caspar; Shulman, Carl; Treutlein, Johannes (2021), [*The Evidentialist's Wager*](https://globalprioritiesinstitute.org/wp-content/uploads/2019/MacAskill_et_al_Evidentialist_Wager.pdf) (PDF)

- <a id="cite_note-Lewis1981-7"></a>**[^](#cite_ref-Lewis1981_7-0)** Lewis, D. (1981), ["Causal decision theory"](http://www.informaworld.com/index/739194078.pdf) (PDF), *Australasian Journal of Philosophy*, **59** (1): 5–30, [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1080/00048408112340011](https://doi.org/10.1080%2F00048408112340011), retrieved 2009-05-29

- <a id="cite_note-Joyce1999-8"></a>**[^](#cite_ref-Joyce1999_8-0)** Joyce, J.M. (1999), [*The foundations of causal decision theory*](https://archive.org/details/foundationsofcau0000joyc/page/n7/mode/2up), p. 146

## External links

- [Causal Decision Theory](http://plato.stanford.edu/entries/decision-causal/) at the [Stanford Encyclopedia of Philosophy](https://en.wikipedia.org/wiki/Stanford_Encyclopedia_of_Philosophy)
