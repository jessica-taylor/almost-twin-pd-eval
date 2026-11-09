# Acting on the News: An Essay on Evidential Decision Theory

## 1. Two ways of valuing an action

Imagine you are deciding whether to make a risky investment. There are two natural questions you might ask yourself:

1. *If I make this investment, what will happen?*
2. *If I learned that I was going to make this investment, what should I expect to happen?*

These sound similar, but they are not the same question. The first asks how your action changes the world. The second asks what your action *tells you* about the world. In most everyday cases the answers coincide, because the main causal consequence of your action is its outcome. But in cases where your action is correlated with things outside your control — other people's similar decisions, predictions of your behavior, a common genetic cause of both your choices and your health — the two questions come apart.

**Evidential decision theory (EDT)** is the position that the second question is the right one to consult when choosing. Roughly: choose the act whose occurrence would be the best news. As the standard formulation puts it, "do what you most want to learn that you will do" (Ahmed 2021). This contrasts with **causal decision theory (CDT)**, which evaluates actions by what they would *cause*, regardless of what their performance would indicate about the rest of the world.

This essay develops EDT's formal machinery, works through its canonical applications, examines how it handles dependencies and counterfactuals, and considers both its appeal and its vulnerabilities. I will mark clearly where I go beyond the source material with interpretations or proposals of my own.

## 2. The formal core: conditional expected utility

The canonical formalization is due to Gibbard and Harper (1976). Let $O_1, \dots, O_n$ be a partition of mutually exclusive and exhaustive outcomes, let $D(O_j)$ be the desirability (utility) of outcome $O_j$, and let $P(\cdot)$ be the agent's credences before acting. EDT evaluates an action $A$ by its **evidential expected utility**:

$$
V(A) \;=\; \sum_{j} P(O_j \mid A)\, D(O_j).
$$

That is, $V(A)$ is the expected desirability of the world *conditional on* the news that $A$ is performed. EDT then prescribes:

$$
\text{Choose } A^* \text{ such that } V(A^*) \ge V(A) \text{ for all admissible } A.
$$

This contrasts with the CDT formula:

$$
U(A) \;=\; \sum_{j} P(A \,\Box\!\!\rightarrow\, O_j)\, D(O_j),
$$

where $A \,\Box\!\!\rightarrow\, O_j$ is the counterfactual "if $A$ were performed, $O_j$ would result." The two conditionals — $P(O_j \mid A)$ ("the probability of $O_j$ given the *news* that $A$") and $P(A \,\Box\!\!\rightarrow\, O_j)$ ("the probability of $O_j$ *if* $A$ is done") — are genuinely different objects, and they coincide only under special conditions.

### When do they coincide?

They agree whenever $A$ is probabilistically independent of everything that is causally relevant to the outcome except through $A$ itself. Formally, suppose the outcome depends on $A$ and on a background variable $S$ (state of the world outside your control). Then:

- $U(A) = \sum_s P(S = s)\, D(A, s)$ — holding the background fixed, since "if $A$ were done" does not change $S$.
- $V(A) = \sum_s P(S = s \mid A)\, D(A, s)$ — reweighting the background by what the news of $A$ implies.

If $P(S = s \mid A) = P(S = s)$ for all $s$ — i.e., $A$ carries no information about $S$ — then $V(A) = U(A)$ and the theories agree. This condition holds in most ordinary decisions: my choice of breakfast is not evidence about the weather. It fails precisely in the interesting cases.

*(One technical caveat, mine rather than the source's: the partition over outcomes matters. For $V(A)$ to be well-defined and to capture "news value" cleanly, the partition should be fine enough to capture all outcomes with differing utility but should not be "gerrymandered" to smuggle in spurious correlations. I will return to this when discussing objections.)*

## 3. Worked example: Newcomb's paradox

In Newcomb's problem, a highly reliable predictor (99% accurate) has already placed either \$1,000,000 or \$0 in an opaque box B, depending on its prediction of your choice. A transparent box A contains \$1,000. You may take both boxes or only B. If the predictor expected you to take only B, B contains the million; otherwise B is empty.

The causally-minded observation is that the boxes are already filled: nothing your choice does now changes their contents, so taking both gets you strictly more money *in each fixed state of the world*. EDT disagrees, because your choice is powerful *evidence* about the prediction, and hence about the contents of B:

$$
\begin{aligned}
V(\text{take only B}) &= P(\$\text{1M in B} \mid \text{take B}) \times 1{,}000{,}000 + P(\$\text{0 in B} \mid \text{take B}) \times 0 \\
&= 0.99 \times 1{,}000{,}000 = \$990{,}000,\\[4pt]
V(\text{take both}) &= P(\$\text{1M in B} \mid \text{take both}) \times 1{,}001{,}000 + P(\$\text{0 in B} \mid \text{take both}) \times 1{,}000 \\
&= 0.01 \times 1{,}001{,}000 + 0.99 \times 1{,}000 = \$11{,}000.
\end{aligned}
$$

Since $990{,}000 > 11{,}000$, EDT prescribes taking one box. The conditional probabilities go the "wrong way" from a causal standpoint — the prediction happened before the choice — but the *correlation* is what EDT's formula responds to. Taking one box does not cause the million to be there, but it is nearly conclusive news that it is.

A useful structural observation *(mine)*: the dependence here runs through a common cause. Your disposition or reasoning process at the time of the predictor's observation is a parent of both the prediction and your eventual choice. The predictor's action "screens off" part of this structure, but because you cannot observe the prediction, your choice retains evidential force about it. This common-cause structure is the signature of every case where EDT and CDT diverge.

## 4. Worked example: the twin prisoner's dilemma

Aomame and her psychological twin — someone whose reasoning is functionally identical to hers — are placed in separate rooms and must each choose to cooperate or defect in a prisoner's dilemma: mutual cooperation pays \$5 each, mutual defection \$1 each, and unilateral defection pays the defector \$10 and the cooperator \$0.

EDT reasons: Aomame's decision is strong evidence about her twin's decision, since the twin reasons the same way she does. If the correlation is perfect,

$$
\begin{aligned}
V(\text{cooperate}) &= P(\text{twin C} \mid \text{Aomame C}) \times 5 + P(\text{twin D} \mid \text{Aomame C}) \times 0 = 5,\\
V(\text{defect}) &= P(\text{twin C} \mid \text{Aomame D}) \times 10 + P(\text{twin D} \mid \text{Aomame D}) \times 1 = 1.
\end{aligned}
$$

EDT prescribes cooperating. Note the difference from ordinary game theory, where mutual defection is the unique equilibrium: EDT treats identical agents' decisions not as independent events but as two reads of the same underlying computation. In effect, by deciding you are also deciding "on behalf of" every process correlated with your reasoning. This connects closely to Hofstadter's notion of *superrationality*, and it is why EDT is attractive to those worried about cooperation among similar agents.

*(A refinement I would add: with imperfect correlation, say $P(\text{twin C} \mid \text{Aomame C}) = p$ and $P(\text{twin C} \mid \text{Aomame D}) = q$ with $p > q$, EDT cooperates iff $5p > 10q + 1 - p$, i.e., $6p - 10q > 1$. Cooperation is thus not automatic; it depends on the strength of the evidential link. A disciplined application of EDT always computes the conditionals rather than gesturing at "similarity.")*

## 5. How EDT handles dependencies: a practical protocol

Since the reader may want to apply EDT to unfamiliar cases, here is a protocol, distilled from the theory's structure:

**Step 1: Define the decision variable.** List the admissible acts $A_1, \dots, A_k$.

**Step 2: Choose the outcome partition.** Identify all states of the world that bear on utility.

**Step 3: Identify the dependence structure.** Ask: what variables are correlated with my act *besides* being caused by it? Typical sources of correlation:
- a common cause (my disposition, my genes, my society's norms);
- other agents' predictions or simulations of me;
- other agents running reasoning similar to mine.

**Step 4: Compute the conditionals $P(O_j \mid A_i)$, honoring those correlations.** This is where most errors happen. The conditional probability $P(O \mid A)$ must reflect *all* evidential channels between $A$ and $O$ — causal and acausal alike. If your act is evidence about a hidden state $S$ via a predictor, a twin, or a common cause, then conditioning on $A$ updates your beliefs about $S$.

**Step 5: Compute $V(A_i) = \sum_j P(O_j \mid A_i) D(O_j)$ and pick the maximum.**

### An application: the smoking lesion

Here is a case where I will argue the protocol yields a determinate answer. A genetic lesion causes both cancer and a craving for smoking. Smoking itself does not cause cancer. Should you smoke?

Naive evidential reasoning says: smoking is evidence of the lesion, hence of cancer, so don't smoke. But EDT done carefully says more. Let $L$ be the lesion, $S$ the decision to smoke, $C$ cancer. The causal structure is $L \to S$ and $L \to C$. Now, crucially, if you *know* this structure, the news that you choose to smoke is informative about $L$ only to the extent that your choice is driven by the lesion rather than by your deliberation over this very argument. Many evidential theorists (following Eells' "tickle defense") argue that if you introspect your desire to smoke before choosing, that introspected desire screens off $S$ from $L$: $P(L \mid S, \text{craving observed}) = P(L \mid \text{craving observed})$. Given the screening, $V(S)$ and $V(\neg S)$ differ only through consequences causally produced by $S$, and since smoking does not cause cancer, $V(S) > V(\neg S)$: smoke.

Whether the "tickle" fully resolves the case is contested — if the lesion also causally influences your introspective outputs, the screening fails and the lesion argument revives. My operational reading: **EDT's verdicts are relative to the agent's full evidence, including evidence about the causal structure and about her own introspective states.** Once all available information is conditioned on, the residual correlation between act and background is what the formula responds to. This makes EDT a theory of *evidence-relative* rationality, which I take to be its natural interpretation, though the source does not commit to it explicitly.

## 6. Counterfactuals and the "news" reading

Why should conditional probability be the right weighting for decisions at all? The evidentialist's answer is that decision-making is belief revision under a self-referential twist: the "hypothesis" being conditioned on is one whose truth you are in the process of settling. When you contemplate an act, you ask what the world would be like if you received the news that you will do it — and since your acts are entangled with the rest of the world through prediction, similarity, and common causes, that news is genuinely informative.

This is why EDT handles "impossible" counterfactuals gracefully. In Newcomb's problem, "if I were to take both boxes, what would be in B?" is causally well-posed but evidentially awkward: conditional on your taking both boxes, your credence that B is full collapses. CDT needs a special semantics for counterfactuals that holds the past fixed while varying the act; EDT simply lets all of your beliefs — including about the past — update in response to the hypothetical news. The philosophical bet is that this is what a bounded agent with limited knowledge *should* do: you cannot causally intervene on things you don't know, but you can always ask what your choices mean.

A further consequence, noted in the source literature as the **evidentialist's wager** (MacAskill et al. 2021): because EDT's evaluations aggregate over correlated decision-makers, the effective stakes of EDT-compliant behavior can be much larger than of one individual's causal footprint. If many agents across the universe reason as you do, then the "news value" of your charitable act, say, includes the acts of all of them. One can even argue for acting as if EDT were true on purely decision-theoretic grounds: if the correlation structure is broad enough, the evidential stakes may dominate. *(This is an argument about which theory to adopt, not a proof that EDT is correct, and it presumes the correlation structure is real rather than an artifact of the formalism.)*

## 7. Objections

EDT's detractors are numerous and the criticisms sharp.

**"Managing the news."** David Lewis (1981) charged that EDT rewards "an irrational policy of managing the news": choosing acts to make your evidence look auspicious rather than to make the world better. James Joyce (1999) sharpened this: rational agents act to *bring about* good outcomes "even when doing so might betoken bad news."

The classic illustration of the worry is the *medical Newcomb* in its un-screened form: if a fatal condition causes both the choice to stay in bed and death, and nothing you do affects the condition, then "staying in bed is bad news" alone should not deter you from any action that would help you. Critics say a theory that can recommend refusing a free benefit purely to avoid receiving bad news has lost the plot of decision-making. Defenders reply with the screening analysis of §5: once all evidence is conditioned on, news-value and world-improvement track each other except where genuine acausal entanglement (predictors, twins) exists — and there, they say, respecting the entanglement is exactly right, as Newcomb and the twin dilemma show.

**Dutch books and Sleeping Beauty.** EDT has been deployed in the Sleeping Beauty problem to argue for "thirder" credences and immunity to Dutch books. But Conitzer (2015) constructed a Dutch book against Sleeping Beauties who are evidential decision theorists, showing that the presumed alliance between EDT and betting coherence is imperfect. The lesson *(mine)*: EDT is a theory of choice, not a general theory of rational credence, and one should not expect it to fix independent problems in confirmation theory.

**Which correlation is real?** EDT's verdicts depend on the agent's conditional probabilities, which depend on her causal and evidential model. A poorly specified model yields poorly specified verdicts. In practice, applying EDT forces you to do the same modeling work that CDT does — identifying common causes, predictors, and structural links — before any divergence in the decision rule even becomes operative.

## 8. Where the theories converge and diverge — a summary

| Situation | Structure | EDT says | CDT says |
|---|---|---|---|
| Act independent of background | $A \perp S$ | Same as CDT | Maximize causal effect |
| Newcomb | Predictor's past choice correlated with act | One box | Two boxes |
| Twin dilemma | Twin's act correlated with yours | Cooperate | Defect |
| Smoking lesion (screened) | Common cause, fully observed | Smoke | Smoke |
| Honest medical choice | No spurious correlation | Same as CDT | Maximize causal effect |

The pattern: EDT and CDT diverge exactly when your act is probabilistically informative about utility-relevant facts you cannot causally influence. EDT says that information is worth acting on; CDT says it is not something you can exploit causally and should be ignored in the counterfactual evaluation. Each theory, in its own terms, is internally consistent; the dispute is about which evaluation function a rational agent should maximize.

## 9. Conclusion

Evidential decision theory replaces the question "what will this act cause?" with "what would this act's occurrence tell me?" — and evaluates acts by the conditional expected utility $V(A) = \sum_j P(O_j \mid A) D(O_j)$. It delivers intuitive verdicts in cases of acausal entanglement, such as Newcomb's problem and the twin prisoner's dilemma, where it correctly treats your decision as evidence about predictions of you and about the outputs of structurally identical reasoners. It agrees with causal decision theory whenever acts are independent of background states, which covers the bulk of ordinary decision-making.

Its main liabilities are the threat of "managing the news," its sensitivity to how the agent models her own evidential situation, and open questions about its interaction with coherence arguments. My own operational reading is that EDT is best understood as a protocol: build an explicit model of every channel — causal and acausal — through which your act correlates with outcomes, condition on the act as news through all of those channels, and maximize the resulting conditional expectation. Applied with that discipline, EDT is not a license for wishful thinking but a principled acknowledgment that, in a world of predictors and twins, the best action and the most auspicious action are sometimes the same thing — and knowing when they are is the whole art of decision theory.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Gibbard, A., & Harper, W. L. (1976). "Counterfactuals and Two Kinds of Expected Utility."
- Lewis, D. (1981). "Causal Decision Theory." *Australasian Journal of Philosophy* 59(1): 5–30.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Wolpert, D. H., & Benford, G. (2013). "The lesson of Newcomb's paradox." *Synthese* 190(9): 1637–1646.
- Greene, P., & Levinstein, B. (2020). "Act Consequentialism without Free Rides." *Philosophical Perspectives* 34(1).
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9): 2887–2899.
- MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). "The Evidentialist's Wager." Global Priorities Institute.