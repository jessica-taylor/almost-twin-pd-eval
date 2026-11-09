# Evidential Decision Theory: Choosing by the News You Would Receive

## 1. The idea in one sentence

Evidential decision theory (EDT) tells an agent to choose the action whose performance would be the best news. Arif Ahmed's slogan, quoted in the reference article, puts it this way: *do what you most want to learn that you will do.* Suppose you learned tomorrow that you had taken action $A$. How happy should that news make you, in expectation? EDT says to take the action for which the answer is largest.

This sounds close to ordinary expected-utility maximization, and in most everyday cases it is. The theory becomes interesting where an action is *evidence* about states of the world that it does not *cause*. That is where EDT separates from its main rival, causal decision theory (CDT). This essay sets out the formal machinery and works through the standard examples. It then confronts the questions the reference article leaves open: what exactly to condition on, how to handle actions one is nearly certain not to take, and whether the theory evaluates acts or policies. I mark clearly which claims come from the source and which are my own proposals or are drawn from the wider literature.

## 2. The formal framework

### 2.1 The basic formula

The reference article follows Gibbard and Harper (1976), who distinguished two kinds of expected utility. EDT's version is

$$
V(A) \;=\; \sum_j P(O_j \mid A)\, D(O_j),
$$

where $\{O_j\}$ is a set of mutually exclusive, jointly exhaustive outcomes, $D(O_j)$ is the desirability of outcome $O_j$, and $P(O_j \mid A)$ is the agent's ordinary conditional credence in $O_j$ given that she performs $A$. The rule is to choose $A^* \in \arg\max_A V(A)$.

It is often clearer to separate *states* $s$, which are features of the world the agent is uncertain about, from *acts* $A$, and to write the utility of the act–state combination as $u(A,s)$:

$$
V(A) \;=\; \sum_s P(s \mid A)\, u(A,s). \tag{1}
$$

The source's formula and (1) agree as long as the outcomes $O_j$ are specified finely enough to settle everything the agent cares about. In the Newcomb calculation below, for example, the "outcome" of taking both boxes when box B is full is worth $1{,}001{,}000, not $1{,}000{,}000. In general the desirability of an outcome may depend on which act produced it. The safe practice is to let outcomes be act–state pairs.

### 2.2 News value as desirability of a proposition

The phrase "news value" comes from Richard Jeffrey's *The Logic of Decision* (1965), the classic presentation of the theory. This attribution is from the wider literature, not from the reference article. In Jeffrey's system, acts, states and outcomes are all *propositions*, and any proposition $X$ with $P(X)>0$ has a desirability

$$
D(X) \;=\; \sum_{w} P(w \mid X)\, D(w),
$$

where $w$ ranges over maximally specific possibilities ("worlds"). EDT then says: among the propositions you can make true, make true the one with the highest $D$. Two consequences follow.

1. **Partition invariance.** For any partition $\{S_k\}$ of possibilities, the law of total probability gives $D(A) = \sum_k P(S_k \mid A)\, D(A \wedge S_k)$. EDT's verdict therefore does not depend on how one carves up the states. This is a real technical virtue: Savage-style theories, which use unconditional probabilities $P(s)$, give different answers under different partitions unless the states are chosen to be independent of the acts.

2. **No counterfactuals are needed.** The only probabilistic ingredient is a conditional probability, defined by $P(X\mid A) = P(X\wedge A)/P(A)$. EDT never asks what *would* happen if $A$ were done. It asks only what is *likely to be the case, given that* $A$ is done.

### 2.3 Contrast with causal decision theory

CDT, as the source presents it, replaces the conditional probability with the probability of a counterfactual:

$$
U(A) \;=\; \sum_j P(A \mathrel{\Box\!\!\rightarrow} O_j)\, D(O_j),
$$

where $A \mathrel{\Box\!\!\rightarrow} O_j$ reads "if $A$ were performed, $O_j$ would obtain." In general $P(A \mathrel{\Box\!\!\rightarrow} O_j) \neq P(O_j\mid A)$, so the two theories can come apart.

It helps to see when they *agree*. Suppose the states $s$ are causally independent of the act, as with weather, a prior prediction, or a coin already flipped. Then CDT effectively uses the unconditional $P(s)$, and (1) becomes

$$
U(A) = \sum_s P(s)\,u(A,s).
$$

So the two theories coincide whenever

$$
P(s \mid A) = P(s) \quad \text{for every act } A \text{ and state } s. \tag{2}
$$

In other words, they coincide when the agent's act carries no information about the act-independent states. Divergence requires an act that is *evidentially* relevant to a state but *causally* irrelevant to it. That is precisely the structure of the thought experiments below.

## 3. Newcomb's problem

The setup, from the source: box A is transparent and contains $1,000. Box B is opaque and contains $1,000,000 if a predictor foresaw that you would take only B, and nothing if it foresaw that you would take both. The predictor is 99% reliable. You may take B alone or both boxes.

Let $F$ be the state "B is full." With reliability $p = 0.99$, the source computes:

$$
\begin{aligned}
V(\text{one-box}) &= P(F\mid \text{one-box})\cdot 10^6 + P(\neg F\mid\text{one-box})\cdot 0 = 0.99\times 10^6 = 990{,}000,\\
V(\text{two-box}) &= P(F\mid\text{two-box})\cdot 1{,}001{,}000 + P(\neg F\mid \text{two-box})\cdot 1{,}000 \\
&= 10{,}010 + 990 = 11{,}000.
\end{aligned}
$$

EDT recommends taking only box B. Your choice is strong evidence about what the predictor foresaw.

CDT reasons differently. The box is already filled or empty. Whatever its contents, taking both adds $1,000, so taking both boxes *dominates*. Formally, if $q = P(F)$ is the unconditional credence, then $U(\text{two-box}) - U(\text{one-box}) = 1{,}000$ for every $q$.

**How much reliability does EDT need?** Generalize to a predictor that is correct with probability $p$ whichever way you choose. Then

$$
V(\text{one}) = 10^6 p, \qquad V(\text{two}) = (1-p)(1{,}001{,}000) + p(1{,}000) = 1{,}001{,}000 - 10^6 p.
$$

One-boxing wins iff $2\times 10^6 p > 1{,}001{,}000$, that is, iff $p > 0.5005$. A predictor only slightly better than chance is enough. This threshold calculation is my own, but it follows directly from the source's formula. It shows that EDT's verdict is not an artifact of near-omniscient predictors.

## 4. The twin prisoner's dilemma

The source's second example: Aomame and her psychological twin, whose reasoning exactly mirrors hers, play a one-shot prisoner's dilemma in separate rooms. The payoffs are 5 each for mutual cooperation, 1 each for mutual defection, and 10/0 when one defects against a cooperator. Aomame cares only about her own payoff.

With perfect correlation, $P(\text{twin } C\mid C) = 1$ and $P(\text{twin } C\mid D) = 0$, so

$$
V(C) = 5, \qquad V(D) = 1,
$$

and EDT recommends cooperating. CDT notes that the twin's choice is causally independent of Aomame's. Since defection dominates, CDT defects.

The source treats only the perfect case. A slight generalization of my own makes the dependence structure clearer. Let $q = P(\text{twin } C \mid C)$ and $r = P(\text{twin } C\mid D)$. Then

$$
V(C) = 5q, \qquad V(D) = 10r + (1-r) = 1 + 9r,
$$

and EDT cooperates iff $5q > 1 + 9r$. Three cases are worth noting:

- **Independence** ($q = r$): the condition becomes $5q > 1+9q$, which is impossible. EDT defects, just as CDT does, as condition (2) predicts.
- **Symmetric correlation** ($r = 1-q$): the condition becomes $14q > 10$, i.e. $q > 5/7 \approx 0.71$.
- **Perfect correlation** ($q=1, r=0$): cooperate, as in the source.

The general lesson is that EDT turns a quantitative question about *how much your choice tells you about others' choices* into a verdict. This is the decision-theoretic core of Hofstadter's "superrationality," which the source lists as a related topic.

## 5. Questions the source leaves open, and how I propose to settle them

The reference article gives the formula and two clean examples. Applying EDT to new cases, however, requires answers to three questions it does not address.

### 5.1 What exactly is the agent conditioning on?

The probability $P$ in $V(A)$ must be the agent's credence *at the moment of decision*, given *everything she then knows*. This matters a great deal, as the **smoking lesion** shows. That example is standard in the literature but is not in the source.

> A genetic lesion $L$ causes both lung cancer and a tendency to enjoy and choose smoking. Smoking itself is harmless. Utility: $+10$ for smoking, $-1000$ for cancer. Statistically, smokers get cancer more often.

A naive EDT calculation reasons that $P(\text{cancer}\mid\text{smoke}) > P(\text{cancer}\mid\neg\text{smoke})$, and so, if the gap exceeds $0.01$, recommends abstaining. That looks absurd: abstaining is "managing the news" (see §7) without changing anything that matters.

The standard evidentialist reply is Ellery Eells's **tickle defence** (1982). The lesion can influence the choice only *through* something in the agent's mind, such as a desire or urge (a "tickle") $T$. A deliberating agent knows her own desires. So the relevant credence is $P(\cdot \mid \cdot, T)$, and if $T$ screens off $L$ from the act,

$$
P(L \mid \text{smoke}, T) = P(L \mid \neg\text{smoke}, T),
$$

then condition (2) holds relative to her total evidence, and EDT agrees with CDT: smoke.

**My operational rule.** I propose the following convention for applying EDT to an unfamiliar case:

> Condition on the agent's total evidence $E$ at decision time, including her introspectively available desires and beliefs. Then ask whether the act still carries information about the payoff-relevant states: $P(s \mid A, E) \neq P(s\mid E)$?

If it does not, EDT and CDT agree and the case is easy. If it does, as in Newcomb or the twin case, EDT follows the residual correlation. The justification is that EDT is a theory of rational credence-guided choice, and rational credence uses all available evidence. Ignoring known facts about one's own mental state would be an error in the probabilities, not a feature of the decision rule.

This rule raises a further question: does the tickle defence also dissolve Newcomb? In Newcomb, the predictor is stipulated to track the *final act*, not merely an initial urge that the agent might override. Correlation therefore survives conditioning on any introspectable state short of the decision itself. Whether a real predictor could do this is an empirical matter. As the problem is specified, however, I take the residual correlation to be stipulated, and EDT one-boxes. Readers should know that this point is contested. Some evidentialists have argued that a fully self-aware agent's act becomes evidentially screened off in every case, which would make EDT collapse into CDT.

### 5.2 Acts of probability zero, and deliberation about oneself

The ratio $P(X\wedge A)/P(A)$ is undefined when $P(A) = 0$. An agent who is certain she will do $B$ cannot compute $V(A)$ for any other act. A related worry, discussed by Levi and Spohn, is that a deliberating agent perhaps should not have credences about her own present choice at all.

My proposal is to treat deliberation as taking place under a credence that gives every available act positive probability. For example, assume a small "tremble" $\varepsilon > 0$ and define

$$
V(A) = \lim_{\varepsilon\to 0} \sum_s P_\varepsilon(s\mid A)\,u(A,s),
$$

or, alternatively, take conditional probability as primitive (Popper functions). Neither choice is innocent. The limit can depend on *how* trembles are modeled: does a trembling agent err randomly, or because of some state that also affects outcomes? When that dependence matters, a careful application should state the tremble model explicitly. In the cases discussed here, the conditional probabilities are fixed by the problem statement (e.g. "99% reliable either way"), and the issue does not arise.

### 5.3 Acts or policies?

The source's formula evaluates individual acts at the point of choice. Some problems involve sequences of choices, or an agent who learns something before acting. Consider **transparent Newcomb** (again my example, not the source's): box B is glass, and you can see it is full. Conditional on seeing a full box, $P(F\mid A, E) = 1$ for both acts, so condition (2) holds, and act-level EDT takes both boxes. Yet an agent known to be a two-boxer in this situation would usually be shown an empty box. A *policy*-level evaluation, which maximizes expected utility over plans chosen before seeing the box, would one-box.

Standard EDT, as Jeffrey and the reference article present it, is act-based. Policy-level ("updateless") variants are separate proposals. In analyzing a case, one should state which version is being applied. I would add that act-based EDT is the version to which the source's definitions apply, and that switching to policies changes the theory, not merely its application.

## 6. Further applications mentioned in the source

**Sleeping Beauty.** Beauty is put to sleep. A fair coin is tossed. On Heads she is woken once; on Tails she is woken twice, with memory erased between wakings. The source reports an argument that if Beauty is a "halfer," holding credence $1/2$ in Heads on waking, she is vulnerable to Dutch books, i.e. sets of bets that guarantee a loss. The argument continues that adopting EDT lets her escape them. EDT helps because on Tails her bets at the two awakenings are correlated: deciding to accept a bet now is evidence that she accepts it at the other awakening too, so EDT counts the payoff twice. The source also reports that Vincent Conitzer (2015) argues halfers remain Dutch-bookable even under EDT. The source does not settle the question, and I will not either. The case does show that EDT's handling of correlated choices extends naturally to an agent correlated with *her own* other instances.

**The Evidentialist's Wager.** The source cites MacAskill et al. (2021): even someone with modest credence in EDT may have reason to act as if it were true. Here is a rough reconstruction, with the formal sketch my own. Suppose your choice is correlated with the choices of $N$ similar decision-makers, and suppose the value difference between acts adds up across them. Under EDT, the difference in news value between two acts is roughly $N\Delta$, where $\Delta$ is the per-agent difference. Under CDT, only your own causal contribution, of order $\Delta$, counts. An agent who weighs theories by credence $c$ (EDT) and $1-c$ (CDT) faces stakes of size about $cN\Delta$ versus $(1-c)\Delta$. For large $N$, the EDT term dominates unless $c$ is tiny. The argument relies on comparing value across theories and on correlation that adds up across agents. Both assumptions can be disputed, but the structure explains the source's phrase "its stakes may be higher."

## 7. Criticism

The source records two classic objections. David Lewis (1981) called EDT "an irrational policy of managing the news." James Joyce (1999) wrote that "rational agents choose acts on the basis of their *causal efficacy*, not their auspiciousness."

The force of the objection is easiest to see in a **medical Newcomb** case (a standard variant, not in the source). A gene causes both a disease and a preference for some harmless activity. Avoiding the activity improves your news but not your health. If the tickle defence (§5.1) applies, EDT does not in fact recommend avoidance, so the objection depends on the case being described without introspective screening-off. If correlation survives full conditioning, as in Newcomb, the evidentialist simply accepts the verdict. Their reply is the familiar "why ain'cha rich?" argument: in repeated Newcomb trials, one-boxers predictably walk away with about $990,000 and two-boxers with about $11,000. A theory that systematically leaves its followers poorer, the evidentialist says, owes us an explanation.

The causalist reply is that this tracks which agents the predictor *rewards*, not which choice is rational *at the moment*: the money is already there or not. The dispute is therefore not about arithmetic. Both sides agree on all the numbers in §3. It is about whether evidential relevance or causal relevance is the right notion of an act "mattering." EDT's distinctive commitment is that a rational agent's preferences over acts should match her preferences over *learning* that she performs them.

## 8. A procedure for unfamiliar cases

Collecting the above, here is a working recipe. Steps 1, 2 and 5 restate the source; steps 3, 4 and 6 are my proposed operationalization.

1. **List the acts** $A_1,\dots,A_n$ available at the decision point.
2. **List the payoff-relevant states** $s$ and the utility $u(A,s)$ of each combination. Make outcomes fine-grained enough that utility depends only on $(A,s)$.
3. **Fix the total evidence** $E$ at decision time, including introspectively available desires and anything the agent observes.
4. **Elicit conditional credences** $P(s\mid A, E)$. If any act has probability zero, specify a tremble model or treat conditional probability as primitive.
5. **Compute** $V(A) = \sum_s P(s \mid A,E)\,u(A,s)$ and choose the maximum.
6. **Diagnose**: if $P(s\mid A,E)=P(s\mid E)$ for all $s$ and $A$, EDT and CDT agree. Otherwise, identify the source of the correlation (a predictor, a twin, another copy of oneself, a common cause) and say explicitly whether act-level or policy-level evaluation is intended.

## 9. Conclusion

EDT is ordinary expected-utility maximization with one deliberate choice: weight outcomes by credence *conditional on the act*. It needs no theory of counterfactuals, its verdicts do not depend on how states are partitioned, and in the vast range of cases where acts carry no information about causally independent states it agrees with CDT. It departs from CDT exactly when an act is evidence about something it does not cause. In those cases it one-boxes in Newcomb's problem and cooperates with a sufficiently correlated twin, and it does so as soon as the correlation passes simple, computable thresholds.

The source presents the formula and these verdicts. Applying the theory responsibly also requires settling what the agent conditions on, how to treat improbable acts, and whether acts or policies are evaluated. I have argued that conditioning on total evidence at decision time is the natural reading. It turns the smoking lesion into an easy case while leaving Newcomb's stipulated correlation intact. Whether "managing the news" is irrational, as Lewis and Joyce hold, or simply what rational agents do when their choices are informative, remains the central philosophical question that the formalism sharpens but does not settle.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9).
- Eells, E. (1982). *Rational Decision and Causality*. Cambridge University Press.
- Gibbard, A. & Harper, W. (1976). "Counterfactuals and Two Kinds of Expected Utility."
- Jeffrey, R. (1965). *The Logic of Decision*. McGraw-Hill.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59(1).
- MacAskill, W. et al. (2021). "The Evidentialist's Wager."
- Wikipedia contributors, "Evidential decision theory," revision 1373679688 (CC BY-SA 4.0).