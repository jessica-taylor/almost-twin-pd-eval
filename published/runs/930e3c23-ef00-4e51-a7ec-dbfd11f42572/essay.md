# Evidential Decision Theory: Choosing the Act You Would Most Like to Learn You Will Do

## 1. The slogan and the idea

Every expected-utility theory answers one question: *how should an agent's uncertainty about the world be combined with her preferences over outcomes to rank her options?* Evidential decision theory (EDT) gives the simplest possible answer. Treat your own action as one more proposition about the world, and ask how good the world is likely to be *given that* the proposition is true. Arif Ahmed's slogan, quoted in the reference article, puts it as an instruction: "do what you most want to learn that you will do."

The quantity EDT maximises is called **news value**. Imagine a reliable messenger telling you "you are going to do $A$." Some messages are welcome and some are not. EDT tells you to perform the act whose announcement would be the best news in expectation.

The main rival is **causal decision theory** (CDT), which tells you to perform the act that will *causally produce* the best outcome in expectation. In ordinary life the two theories agree. They diverge in a family of cases where your choice is correlated with features of the world that it does not cause. The canonical examples are Newcomb's problem and the twin prisoner's dilemma. Most of this essay is about why they diverge, how to compute EDT's verdict precisely, and where the theory's specification is underdetermined.

A note on provenance. The reference article (Wikipedia, "Evidential decision theory") supplies the core definition, the Gibbard–Harper contrast with CDT, the Newcomb and twin calculations, brief remarks on Sleeping Beauty and the "evidentialist's wager," and the criticisms by Lewis and Joyce. The following are my own additions and are flagged as such:

- the general threshold analyses,
- the smoking-lesion case and the tickle defence,
- the treatment of zero-probability acts and policies,
- the Sleeping Beauty betting calculation,
- the operational recipe in §7.

## 2. The formal definition

### 2.1 The source's formula

Following Gibbard and Harper (1976), the reference article defines the evidential expected utility of an action $A$ as

$$
V(A) = \sum_j P(O_j \mid A)\, D(O_j),
$$

where $\{O_j\}$ is a set of mutually exclusive, jointly exhaustive outcomes, $D(O_j)$ is the desirability of $O_j$, and $P(O_j \mid A)$ is the ordinary conditional probability:

$$
P(O_j \mid A) = \frac{P(O_j \wedge A)}{P(A)} .
$$

The contrast is with the causal or counterfactual expected utility,

$$
U(A) = \sum_j P(A \mathrel{\Box\!\!\rightarrow} O_j)\, D(O_j),
$$

where $P(A \mathrel{\Box\!\!\rightarrow} O_j)$ is the probability that *if $A$ were performed*, $O_j$ would obtain. The two theories differ in practice only because $P(O_j \mid A)$ and $P(A \mathrel{\Box\!\!\rightarrow} O_j)$ can come apart.

### 2.2 The general Jeffrey form (my elaboration)

The cleanest version of EDT is Richard Jeffrey's *Logic of Decision* (1965). In that framework acts, states and outcomes are all propositions, i.e. sets of possible worlds $w$. There is a single probability measure $P$ over worlds and a utility function $u$ on worlds. The desirability of any proposition $X$ with $P(X) > 0$ is

$$
V(X) = \sum_{w \in X} P(w \mid X)\, u(w) = \mathbb{E}[u \mid X],
$$

with integrals replacing sums in the continuous case. An act is simply a proposition the agent can make true. EDT says to choose

$$
A^* \in \arg\max_{A \in \mathcal{A}} \; \mathbb{E}[u \mid A].
$$

Two technical points follow.

**Partition invariance.** By the law of total expectation, for any partition $\{O_j\}$,

$$
V(A) = \sum_j P(O_j \mid A)\, V(O_j \wedge A).
$$

So it does not matter how coarsely or finely outcomes are carved, provided that each outcome's desirability is evaluated *in conjunction with* the act. The source's formula writes $D(O_j)$ rather than $D(O_j \wedge A)$. That is harmless when outcomes are described finely enough to fix everything the agent cares about, including the act itself where relevant. Otherwise, use the conjunctive form.

**Conditioning, not intervening.** In the vocabulary of causal Bayesian networks, EDT uses $P(O \mid A)$, the distribution of $O$ in worlds where $A$ happens. CDT (in its interventionist form) uses something like $P(O \mid \mathrm{do}(A))$, the distribution of $O$ when $A$ is set by surgery that cuts $A$ off from its causes. The two coincide when there is no "back-door" path between $A$ and $O$, that is, when every correlation between act and outcome runs through the act's causal influence.

## 3. When EDT and CDT agree

Let the outcome be a deterministic function $o(A, S)$ of the act and a state $S$, and write $u(A, S)$ for its utility. Then

$$
V(A) = \sum_S P(S \mid A)\, u(A,S), \qquad
\text{Savage-style EU}(A) = \sum_S P(S)\, u(A,S).
$$

If the state is **probabilistically independent** of the act, $P(S \mid A) = P(S)$, then $V(A)$ coincides with standard Savage expected utility. In that case it also coincides with CDT, since CDT's counterfactual probabilities reduce to $P(S)$ for states the act cannot influence.

Disagreement therefore requires **act–state dependence**: the state is not caused by the act, yet the act carries information about it. Such dependence typically arises in two ways:

1. **A common cause.** Your decision and the state share an upstream cause, such as your psychology, genes or upbringing.
2. **A model of you.** The state was produced by something that models your decision procedure, such as a predictor or a copy of you.

Everything interesting about EDT lives in these cases.

## 4. Worked examples

### 4.1 Newcomb's problem

Box A is transparent and contains \$1,000. Box B is opaque. A predictor, correct with probability $p$, has put \$1,000,000 in B if it predicted you would take only B, and nothing if it predicted you would take both.

With the source's $p = 0.99$:

$$
\begin{aligned}
V(\text{one-box}) &= 0.99 \times 1{,}000{,}000 + 0.01 \times 0 = 990{,}000,\\
V(\text{two-box}) &= 0.01 \times 1{,}001{,}000 + 0.99 \times 1{,}000 = 11{,}000.
\end{aligned}
$$

EDT one-boxes. CDT two-boxes, because the contents of B are already fixed. Whatever B holds, taking A as well adds \$1,000, so two-boxing causally dominates.

*Generalisation (mine).* Let the prize be $M$, the sure amount $K$, and take the predictor's accuracy to be $p$ regardless of what you choose. Then

$$
V(\text{one}) = pM, \qquad V(\text{two}) = (1-p)M + K,
$$

so EDT one-boxes iff

$$
p > \frac{M + K}{2M}.
$$

With $M = 10^6$ and $K = 10^3$, the threshold is $p > 0.5005$. A predictor barely better than a coin suffices. This shows how much weight EDT places on even weak correlations when the stakes are lopsided.

### 4.2 The twin prisoner's dilemma

Aomame plays a one-shot prisoner's dilemma against a psychological twin whose reasoning mirrors hers. The payoffs to Aomame are:

| | Twin C | Twin D |
|---|---|---|
| **Aomame C** | 5 | 0 |
| **Aomame D** | 10 | 1 |

The source assumes perfect correlation, $P(\text{twin C} \mid \text{C}) = 1$ and $P(\text{twin C} \mid \text{D}) = 0$. That gives $V(C) = 5$ and $V(D) = 1$, so EDT cooperates. CDT notes that defection dominates, because the twin's choice is causally independent of hers, and so it defects.

*Generalisation (mine).* Suppose the correlation is symmetric with strength $q$: the twin matches Aomame's choice with probability $q$. Then

$$
V(C) = 5q, \qquad V(D) = 10(1-q) + q = 10 - 9q,
$$

and EDT cooperates iff $q > 5/7 \approx 0.714$.

The lesson generalises. EDT's verdict depends continuously on how strongly your act is evidence about the other player. It reduces to ordinary dominance reasoning at $q = 1/2$, where your choice is uninformative. This is the formal content behind Hofstadter's "superrationality."

### 4.3 The smoking lesion and the tickle defence (not in the source)

The standard objection to EDT is a medical case. A gene (the lesion $L$) causes both lung cancer and a taste for smoking. Smoking itself is harmless. Suppose:

- utility is $+10$ for smoking and $-100$ for cancer;
- among people like you, $P(\text{cancer} \mid \text{smoke}) = 0.8$ and $P(\text{cancer} \mid \neg\text{smoke}) = 0.2$.

Naively applied, EDT computes

$$
V(\text{smoke}) = 10 - 80 = -70, \qquad V(\neg\text{smoke}) = -20,
$$

and tells you to abstain, which looks like an attempt to avoid cancer by avoiding the *symptom* of the gene. CDT smokes, and most people's intuitions side with CDT here.

The main evidentialist reply is the **tickle defence**, developed by Eells (1982) and others. The lesion can influence your choice only through something you can introspect, such as a desire, a "tickle" $T$. A deliberating agent already knows whether $T$ is present. Her credences should therefore condition on $T$, and given $T$, the act carries no further information about $L$:

$$
P(L \mid \text{smoke}, T) = P(L \mid T) = P(L \mid \neg\text{smoke}, T).
$$

With the act screened off from the lesion, §3 applies. EDT agrees with CDT and smokes, since the \$10-equivalent of pleasure comes free.

The general moral is this. EDT's verdicts depend on *which information the agent conditions on*. Correctly specified, they diverge from CDT only when the correlation survives everything the agent knows at the time of choice. In Newcomb and twin cases the correlation plausibly survives, because the predictor or twin tracks your *reasoning* and not merely an introspectible input to it. In lesion cases it plausibly does not.

## 5. Open questions and an operational interpretation

The reference article states the formula but leaves several things unspecified that matter for applying it. Here are the main gaps and the resolutions I would propose.

### 5.1 Whose probabilities, and at what time?

$P(O \mid A)$ requires a credence in one's own act, $P(A)$. There are at least two difficulties.

- **Self-prediction during deliberation.** Some philosophers (Levi, Spohn) argue that a deliberating agent cannot coherently assign credences to her own choices. If so, EDT cannot even be stated.
- **Drift of conditional probabilities.** As deliberation proceeds and the agent becomes confident she will do $A$, other conditional probabilities may change.

**Proposed operationalisation.** Model the agent's decision procedure as a node $\Pi$ in her own world model, with possible outputs $a \in \mathcal{A}$. Interpret "$A$" as the proposition $\Pi = a$. Compute

$$
V(a) = \mathbb{E}[u \mid \Pi = a, E],
$$

where $E$ is the total evidence available *before* the output of $\Pi$ is known, including introspective tickles.

This makes EDT a well-defined function of a model, as long as the model assigns a non-degenerate prior over the procedure's outputs. On this reading the predictor in Newcomb is correlated with $\Pi$, because it simulates $\Pi$. The lesion in the smoking case is correlated only with inputs to $\Pi$, and those inputs belong to $E$. This reproduces the verdicts defended in §4.

### 5.2 Acts of probability zero

If $P(A) = 0$, then $P(O \mid A)$ is undefined, so EDT is silent about the act. This is a real problem for an agent who is already certain what she will do.

There are three standard patches:

1. **Primitive conditional probabilities.** Use Popper functions, or lexicographic or non-standard probabilities, so that conditioning on null events is defined.
2. **Required uncertainty.** Require the agent to keep $P(A) > 0$ for every option until the moment of choice.
3. **Trembles.** Define $V(A)$ as the limit of conditional expectations under small "trembles," analogous to trembling-hand perfection in game theory.

I recommend (3) for practical purposes. It is the most transparent, and when the limit is unique it agrees with (1).

### 5.3 Acts versus policies

EDT as stated evaluates individual acts at the moment of choice. In multi-stage problems one can instead apply it to whole **policies**, i.e. functions from observations to acts, evaluated from a prior standpoint. The two can diverge.

In *transparent* Newcomb, where both boxes are visible:

- An act-level evidentialist who sees \$1M in box B learns nothing more from her act about B's contents, so she two-boxes.
- A policy-level evidentialist notes that the policy "one-box even when B is visibly full" is what gets B filled in the first place.

The source does not take a stand on this. My view is that the act/policy distinction is orthogonal to the evidential/causal one: "updateless" variants exist on both sides. When a problem involves predictors that respond to your *policy*, you should state which version you are using.

### 5.4 Sleeping Beauty and correlated copies of oneself

The source reports that EDT has been invoked to protect "halfers" in the Sleeping Beauty problem from Dutch books, and that Conitzer (2015) argues halfers remain exploitable even so. A short calculation shows why EDT is relevant (the calculation is my illustration of the standard point, cf. Briggs 2010).

The setup:

- Beauty is woken once if a fair coin lands heads and twice if it lands tails, with memory erased between wakings.
- At each waking she is offered a bet paying $+x$ if heads and $-y$ if tails.

A **thirder** who evaluates each waking causally accepts iff

$$
\tfrac{1}{3}x - \tfrac{2}{3}y > 0, \quad\text{i.e. } x > 2y.
$$

A **halfer** with credence $1/2$ in heads who evaluates causally accepts iff $x > y$. That mismatch with the thirder's betting behaviour is what opens her to exploitation.

A halfer who uses EDT reasons differently. Her two tails-wakings are in identical epistemic states, so accepting now is near-certain evidence that she accepts at every waking. Hence

$$
V(\text{accept}) = \tfrac{1}{2}x + \tfrac{1}{2}(-2y),
$$

and she accepts iff $x > 2y$, exactly the thirder's threshold.

So EDT plus halfing reproduces thirder betting behaviour on these bets. Conitzer's contribution is to construct a sequence of bets on which the EDT-halfer is nonetheless exploited, so the rescue is at best partial. The general lesson is that **EDT treats one's own correlated decisions, including those of copies and memory-erased selves, as a single choice.** That is precisely its behaviour in the twin dilemma.

## 6. Arguments for and against

### 6.1 For EDT

**Parsimony.** EDT needs only a probability function and a utility function. It does not require primitive counterfactuals, causal graphs, or a privileged notion of intervention. Its defenders, notably Ahmed (2021), argue that causal notions are either reducible to credences or do no rationally relevant work.

**"Why ain'cha rich?"** In Newcomb's problem, one-boxers predictably end up with about \$990,000 and two-boxers with about \$11,000 (§4.1). A theory whose followers reliably do worse in a fully described, repeatable situation owes us an explanation. Causalists reply that the predictor simply rewards irrationality. Evidentialists reply that a standard of rationality on which the rational predictably lose has a burden to discharge.

**The evidentialist's wager.** Reported in the source and due to MacAskill, Vallinder, Oesterheld, Shulman and Treutlein (2021), the argument applies even to someone who is uncertain which theory is correct.

Suppose there are $N$ agents whose decisions are strongly correlated with yours: copies, near-copies, or agents running similar procedures, perhaps across a large universe. Then the evidential value difference between two acts scales roughly with $N$, while the causal difference reflects only your own act. With credence $c$ in EDT and $1-c$ in CDT, an expected-choiceworthiness calculation looks like

$$
c \cdot N \cdot \Delta_{\text{EDT}} + (1-c) \cdot \Delta_{\text{CDT}}.
$$

For large $N$ this is dominated by the evidential term, even when $c$ is small. One should therefore act *as if* EDT were true.

My caveat is that the argument assumes intertheoretic comparability of value units, and it inherits the usual fanaticism worries about letting large-stakes hypotheses dominate.

### 6.2 Against EDT

**"Managing the news."** David Lewis (1981) called EDT "an irrational policy of managing the news." James Joyce (1999) put the point this way: "Rational agents choose acts on the basis of their *causal efficacy*, not their auspiciousness; they act to *bring about* good results even when doing so might betoken bad news."

The intuition is sharpest in the smoking lesion and in "medical Newcomb" cases. There, abstaining does nothing to your health, and choosing an act for its diagnostic value seems like a confusion of *learning* with *doing*.

How much force this criticism has depends on whether the tickle defence (§4.3) succeeds in general. If it does, EDT "manages the news" only when the news is about things *correlated with your reasoning itself*. In those cases evidentialists argue that the reasoning-level correlation is exactly what matters. If it does not, for instance because the lesion's influence bypasses introspection, the objection stands.

**Instability and ratifiability.** Jeffrey himself proposed that an act should be *ratifiable*: it should remain optimal conditional on the supposition that one has decided to do it. Some problems have no ratifiable act, or have several. Unratified EDT can also recommend acts the agent would regret upon learning she had chosen them. This critique, found in later literature though not in the source, motivates the deliberational refinements mentioned in §5.1.

## 7. A recipe for unfamiliar cases

Gathering the preceding sections, here is a procedure for applying EDT. Steps 1–3 and 5 come from the source's definition. Steps 2, 4 and 6 incorporate my proposed resolutions of the open questions.

1. **Enumerate acts** $\mathcal{A}$, or policies if the problem contains predictors that respond to your contingent plans. State which you are using.
2. **Build a joint model** containing your decision procedure $\Pi$, the relevant states, and other agents or predictors, together with everything you know at the time of choice, including introspective evidence.
3. **Define outcomes finely enough** to fix utility. Otherwise use $V(O_j \wedge A)$ in place of $D(O_j)$.
4. **Identify correlations** between $\Pi$ and the states. Ask whether each correlation survives conditioning on your current evidence. Correlations that run through *inputs* you already observe are screened off. Correlations that run through *your reasoning*, as with predictors, copies and twins, are not.
5. **Compute** $V(a) = \sum_j P(O_j \mid \Pi = a, E)\, V(O_j \wedge a)$ for each $a$, and choose the maximum.
6. **Check edge cases.** Handle acts with $P(a) = 0$ by trembles. Check whether the chosen act is ratifiable, and note it if it is not.

To illustrate, consider a case the source does not discuss. A firm and a rival use the same pricing algorithm, licensed from one vendor, and each independently decides whether to undercut. With a shared algorithm the correlation runs through the decision procedure itself, so step 4 says it is *not* screened off. EDT then behaves as in the twin dilemma: it evaluates "undercut" knowing that the rival's identical algorithm almost certainly undercuts too.

Change one detail. Suppose the firms merely share a market shock that makes both inclined to undercut, and each firm observes that shock. Now the correlation runs through an observed input. Step 4 screens it off, and EDT reduces to ordinary best-response reasoning.

## 8. Conclusion

Evidential decision theory ranks actions by the conditional expected utility $\mathbb{E}[u \mid A]$. It treats one's own choice as evidence about the world, exactly as one would treat any other proposition. Whenever the act is probabilistically independent of the states it does not cause, it agrees with causal decision theory. It departs from CDT only when the act carries information about such states, as in Newcomb's problem, where it one-boxes, and the twin dilemma, where it cooperates.

Its strengths are formal parsimony, apparent success in prediction cases, and, through the evidentialist's wager, a possible claim to guide action even under uncertainty about which decision theory is true. Its central liability is Lewis's charge of "managing the news," and the plausibility of that charge depends largely on whether correlations can be screened off by what the agent knows at deliberation time.

The formula alone underdetermines several practical questions: self-credence, zero-probability acts, and acts versus policies. Making them explicit, as above, turns EDT into a procedure that delivers determinate verdicts in new cases, and it shows exactly which modelling choices those verdicts depend on.

---

### References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Briggs, R. (2010). "Putting a value on Beauty." *Oxford Studies in Epistemology* 3.
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9): 2887–2899.
- Eells, E. (1982). *Rational Decision and Causality*. Cambridge University Press.
- Gibbard, A. & Harper, W. (1976). "Counterfactuals and Two Kinds of Expected Utility."
- Jeffrey, R. (1965). *The Logic of Decision*. McGraw-Hill.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59(1): 5–30.
- MacAskill, W., Vallinder, A., Oesterheld, C., Shulman, C. & Treutlein, J. (2021). "The Evidentialist's Wager." Global Priorities Institute.
- Wikipedia contributors, "Evidential decision theory," revision 1373679688 (CC BY-SA 4.0).