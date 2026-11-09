# Evidential Decision Theory: Choosing the Best News

## 1. The idea in one sentence

Evidential decision theory (EDT) tells an agent to choose the action whose performance would be the best *news*. Suppose an oracle announced, "you are going to do $A$." How good would you then expect the world to be? Compute that for every available action and pick the highest. Arif Ahmed's slogan, quoted in the reference article, puts it compactly: *do what you most want to learn that you will do.*

At first this sounds like ordinary expected-utility maximization. Usually it is. The theory becomes philosophically interesting only where learning that you do $A$ tells you something about the world that doing $A$ does not *cause*. In those cases EDT parts ways with causal decision theory (CDT), and its verdicts look either wise or perverse, depending on whom you ask.

This essay sets out the formal theory and works through the standard examples with general parameters rather than fixed numbers. It then takes up the questions the reference article leaves open: what exactly to condition on, whether to evaluate acts or policies, and what to do about zero-probability actions. I flag where I go beyond the source.

## 2. Formal setup

### 2.1 The basic formula

The reference article, following Gibbard and Harper (1976), states EDT as maximizing

$$
V(A) = \sum_j P(O_j \mid A)\, D(O_j),
$$

where the $O_j$ are mutually exclusive and exhaustive outcomes, $D(O_j)$ is the desirability of outcome $O_j$, and $P(O_j \mid A) = P(O_j \wedge A)/P(A)$ is the ordinary conditional probability. The recommended action is

$$
A^* \in \arg\max_{A \in \mathcal{A}} V(A),
$$

where $\mathcal{A}$ is the set of actions available to the agent.

Three features matter.

1. **Actions are propositions.** In Richard Jeffrey's framework (*The Logic of Decision*, 1965), from which EDT descends, acts, states and outcomes all belong to a single algebra of propositions. One credence function $P$ covers all of them. Acts are not special objects that "intervene" on the world. They are propositions the agent can make true, and she has credences about them like anything else.

2. **No separate notion of dependence.** The formula contains no causal graph, no counterfactual and no "dependency hypothesis." Every relationship between action and outcome is carried by the conditional probability.

3. **Desirability is the agent's own.** $D$ encodes preferences. EDT takes these as given, as CDT does.

### 2.2 The general Jeffrey form and partition invariance

The source writes $D(O_j)$ as if outcomes fix desirability independently of the act. That is a simplification. In Jeffrey's general formulation the value of any proposition $X$ with $P(X) > 0$ is

$$
V(X) = \sum_j P(O_j \mid X)\, V(O_j \wedge X)
$$

for *any* partition $\{O_j\}$. If the partition is fine enough that each $O_j$ settles everything the agent cares about, then $V(O_j \wedge A) = D(O_j)$ and we recover the source's formula.

A pleasant consequence, which is my emphasis rather than the source's, is **partition invariance**. Any way of carving up outcomes gives the same $V(A)$. This follows from the law of total expectation: $V(A)$ is just the conditional expectation of a utility random variable $u$ given the event $A$,

$$
V(A) = \mathbb{E}[\,u \mid A\,].
$$

So the evidential decision theorist never has to ask which partition is the right one for describing the decision problem. Causal decision theorists in the Lewis–Skyrms tradition do have to ask this, because their formula requires a partition into states that are causally independent of the act. EDT's austerity here is a real advantage. It needs only a joint probability distribution and a utility function.

### 2.3 Contrast with CDT

The source contrasts $V$ with the causal expected utility

$$
U(A) = \sum_j P(A \mathrel{\Box\!\!\rightarrow} O_j)\, D(O_j),
$$

where $P(A \mathrel{\Box\!\!\rightarrow} O_j)$ is the probability that $O_j$ *would* obtain *were* $A$ performed. A useful way to see the difference is by the form of supposition each theory uses:

- EDT uses **indicative** supposition: *given that* I do $A$, what is the world probably like?
- CDT uses **subjunctive** supposition: *if I were to* do $A$, what would the world be like?

Readers familiar with causal Bayesian networks can view CDT's quantity as something like $P(O_j \mid \mathrm{do}(A))$ and EDT's as plain $P(O_j \mid A)$. This analogy is mine, and it is imprecise at the edges, but it makes the structural point clear. The two differ exactly when $A$ and $O_j$ are correlated through a channel other than $A$'s causal influence on $O_j$. Typically that channel is a common cause, or a process (a predictor, a twin) whose behaviour mirrors the agent's own decision procedure.

**When they agree.** Write outcomes as act–state pairs, $O = (A, S)$, with $D(A,S)$ the desirability. Suppose the states are *evidentially* independent of the act, so $P(S \mid A) = P(S)$ for all $S$ and $A$. Then

$$
V(A) = \sum_S P(S)\, D(A, S).
$$

This is the familiar Savage-style expected utility. If the states are also causally independent of the act, CDT gives the same number. Most everyday decisions (umbrellas, investments, medical treatments chosen on reliable trial data) satisfy both conditions, which is why the reference article notes that the theories "agree in many cases."

## 3. Newcomb's problem with a general predictor

The reference article's central example is Newcomb's problem. Box A holds a visible \$1,000. Box B holds \$1,000,000 if a predictor foresaw that you would take only B, and nothing if it foresaw that you would take both. The source assumes 99% accuracy. Here I let the accuracy be a parameter $a$, symmetric across both kinds of prediction:

$$
P(\text{B full} \mid \text{one-box}) = a, \qquad P(\text{B full} \mid \text{two-box}) = 1 - a.
$$

Then

$$
\begin{aligned}
V(\text{one-box}) &= a \cdot 1{,}000{,}000, \\
V(\text{two-box}) &= (1-a)\cdot 1{,}001{,}000 + a \cdot 1{,}000 = 1{,}001{,}000 - 1{,}000{,}000\,a.
\end{aligned}
$$

EDT recommends one-boxing iff $2{,}000{,}000\,a > 1{,}001{,}000$, that is, iff

$$
a > 0.5005.
$$

At $a = 0.99$ we get the source's figures: \$990,000 versus \$11,000. The threshold shows how little predictive reliability EDT needs before it switches. Any predictor even slightly better than a coin flip suffices, because the prize ratio is 1000:1. In general, with a small prize $k$ in box A and a large prize $M$ in box B, the threshold is $a > (M + k)/(2M)$.

CDT reasons differently. The prediction is already made and the box contents are fixed. Whatever B contains, taking both yields \$1,000 more. Formally, for each state $S \in \{\text{full}, \text{empty}\}$, $D(\text{two-box}, S) = D(\text{one-box}, S) + 1000$, and since $P(\text{two-box} \mathrel{\Box\!\!\rightarrow} S) = P(S)$, two-boxing dominates.

The disagreement comes down to this. EDT does not regard the box contents as independent of the act *in the relevant sense*. Evidentially they are not independent, and evidential dependence is the only kind EDT recognises. **Dominance reasoning is valid for EDT only when states are evidentially independent of acts.**

## 4. The twin prisoner's dilemma

The source's second example concerns Aomame and her psychological twin. Mutual cooperation pays \$5 each, mutual defection \$1 each, and unilateral defection pays \$10 to the defector and \$0 to the cooperator. The source assumes perfect correlation. Let us weaken it:

$$
P(\text{twin C} \mid \text{C}) = p, \qquad P(\text{twin D} \mid \text{D}) = q.
$$

Then

$$
V(C) = 5p, \qquad V(D) = 10(1-q) + q = 10 - 9q.
$$

With symmetric correlation $p = q$, EDT recommends cooperation iff $5p > 10 - 9p$, that is, $p > 5/7 \approx 0.714$. With $p = q = 1$ we recover the source's values of \$5 and \$1.

This example is philosophically cleaner than Newcomb's problem because there is no mysterious predictor. The correlation comes entirely from shared computation. Two instances of the same reasoning process, given the same inputs, produce the same output. EDT treats this correlation as decision-relevant. CDT does not, because nothing Aomame does physically affects her twin, so CDT recommends defection, which dominates. The link to Hofstadter's notion of *superrationality*, which the source lists under "See also," is direct.

## 5. Common causes and the "managing the news" objection

The reference article reports David Lewis's charge that EDT embodies "an irrational policy of managing the news," and James Joyce's dictum that rational agents act on *causal efficacy*, not *auspiciousness*. The source does not give the example that makes these criticisms bite hardest. It deserves careful treatment, because how EDT handles it determines how the theory applies to many unfamiliar cases.

### 5.1 The smoking lesion

Suppose a genetic lesion $L$ causes both cancer and a desire to smoke. Smoking itself is harmless and enjoyable. Take these illustrative numbers:

- Utility: $+10$ for smoking, $-100$ for cancer, additive.
- $P(\text{cancer} \mid L) = 0.8$ and $P(\text{cancer} \mid \neg L) = 0.05$.
- Population statistics: $P(L \mid S) = 0.6$ and $P(L \mid \neg S) = 0.1$.

If the agent naively uses the population statistics as her conditional credences, then

$$
\begin{aligned}
P(\text{cancer} \mid S) &= 0.6(0.8) + 0.4(0.05) = 0.50, \\
P(\text{cancer} \mid \neg S) &= 0.1(0.8) + 0.9(0.05) = 0.125,
\end{aligned}
$$

which gives $V(S) = 10 - 50 = -40$ and $V(\neg S) = -12.5$. On this computation EDT says abstain. That seems absurd. Abstaining does nothing to your genes. It only spares you the bad news.

### 5.2 The tickle defence

The standard evidentialist reply, developed by Ellery Eells (1982), goes beyond the source. The lesion can affect the agent's choice only *through* her beliefs and desires. If so, she can introspect on those states before deciding. Call the relevant observed mental state the "tickle" $T$. Once the agent conditions on $T$, as EDT requires her to condition on all her evidence, the act carries no further information about the lesion:

$$
P(L \mid S, T) = P(L \mid T) = P(L \mid \neg S, T).
$$

Hence $P(\text{cancer} \mid S, T) = P(\text{cancer} \mid \neg S, T) =: c$. We get $V(S) = 10 - 100c$ and $V(\neg S) = -100c$, so EDT says *smoke*. The objection fails because the agent's own evidence **screens off** the spurious correlation.

The general lesson, which I adopt as an operational rule below, is this. The relevant probabilities are the agent's own credences after conditioning on everything she knows, including what she knows about her own mind. They are not population frequencies.

### 5.3 An open question: does screening off go too far?

There is a well-known complication that the source does not mention. Eells himself argued that a sufficiently self-aware agent can apply similar "metatickle" reasoning in Newcomb's problem. The predictor bases its prediction on some features of the agent's psychology. If the agent can observe those features, they screen off her act from the prediction, and EDT then recommends two-boxing.

Evidentialists such as Ahmed (2014) resist this. They argue that in a well-designed Newcomb case the predictor tracks the *output of the deliberation itself*, which the agent cannot observe before she finishes deliberating, so no screening-off occurs. The twin case makes the point vivid. What correlates with the twin's choice is precisely the result of Aomame's reasoning, not any prior state she could inspect.

My assessment is that EDT's verdict depends on a modelling question it does not itself answer. **Does some state, accessible to the agent before she acts, screen off her act from the payoff-relevant state?** If yes, EDT behaves causally. If the correlation runs through the deliberative process itself, EDT behaves "evidentially." When you apply EDT to a new case, you must commit to an answer and make it explicit.

## 6. Acts or policies?

The source speaks only of evaluating "actions." There is a further choice point, and it produces different verdicts.

**Act-level EDT** evaluates each action at the moment of choice, conditioning on all evidence then available.

**Policy-level EDT**, which is a proposal from the wider literature and not from the source, evaluates complete contingency plans $\pi: \text{Observations} \to \text{Actions}$ from an earlier epistemic standpoint. It then follows whichever plan maximises $\mathbb{E}[u \mid \pi]$.

**Transparent Newcomb** separates the two. Suppose both boxes are transparent and you see \$1,000,000 in box B. Act-level EDT conditions on this observation, so $P(\text{B full} \mid \text{two-box}, \text{see full}) = 1$, and two-boxing is better by \$1,000. However, a reliable predictor fills box B only for agents whose policy is to one-box *on seeing it full*. Evaluating policies before the observation gives

$$
\mathbb{E}[u \mid \pi_{\text{one-box if full}}] \approx 1{,}000{,}000 \gg \mathbb{E}[u \mid \pi_{\text{always two-box}}] \approx 1{,}000.
$$

Act-level EDT therefore faces a version of the objection it presses against CDT. Agents of its type predictably end up poorer in this problem.

Which version is "EDT"? Historically and in the source, the theory is act-level: one maximises news value given current evidence. I treat policy-level evaluation as a distinct extension, sometimes called "updateless." It is motivated by the same idea that correlations with predictors and copies matter, but it gives up the principle that one always conditions on all current information. When you apply EDT to a sequential problem, state which version you are using. They agree whenever no other process's behaviour depends on what the agent *would* do in situations she is not actually in.

## 7. Technical loose ends

### 7.1 Zero-probability acts

$P(O \mid A)$ is undefined when $P(A) = 0$. This is not idle. An agent who has nearly finished deliberating may be almost certain what she will do, and then the conditional probabilities for the alternatives become undefined or numerically unstable. The source is silent on this.

I propose the following operational fix. Evaluate actions using the credences the agent holds *while deliberation is open*, before she is certain of her choice. Where needed, define

$$
V(A) = \lim_{\varepsilon \to 0} \mathbb{E}_{P_\varepsilon}[\,u \mid A\,],
$$

where $P_\varepsilon$ mixes $P$ with an $\varepsilon$-probability "tremble" that the agent performs $A$ by mistake. The tremble must be modelled so that it carries no other information. In particular, it should not correlate with the predictor's output unless the predictor would also have predicted the tremble.

This choice is substantive. The way the tremble is modelled can change the answer. One could instead use Popper functions (primitive conditional probabilities), and the same modelling choice reappears there.

### 7.2 Self-knowledge during deliberation

EDT asks the agent to have credences about her own future acts. Some philosophers deny that a deliberating agent can coherently have them; others regard this as harmless. For practical purposes it is enough that $P(A) > 0$ for each live option and that conditional credences are well defined. The fix in 7.1 guarantees that.

## 8. Further arguments around EDT

**"Why ain'cha rich?"** In Newcomb's problem, one-boxers predictably walk away richer. Lewis wrote a paper under exactly that title, giving the CDT reply that the problem rewards irrationality. Evidentialists treat the asymmetry as evidence for their view. CDT's counter is that the agents face different situations, since one-boxers are presented with full boxes.

**The evidentialist's wager.** The source mentions an argument from MacAskill, Vallinder, Oesterheld, Shulman and Treutlein (2021). Suppose you are uncertain whether EDT or CDT is correct. In a large universe, your decision is correlated with the decisions of many similar agents. Suppose $N$ agents choose as you do. Then the difference in news value between two acts can scale roughly as $N \cdot \Delta$, while the causal difference stays at $\Delta$. If you aggregate across theories by credence-weighted expected value,

$$
c_{\text{EDT}} \cdot N\Delta_{\text{EDT}} \;\text{ vs. }\; c_{\text{CDT}} \cdot \Delta_{\text{CDT}},
$$

then even a small credence $c_{\text{EDT}}$ can dominate when $N$ is large. The argument assumes that values can be compared across theories, which is itself contested.

**Sleeping Beauty.** The source notes that some authors have argued that a "halfer" Sleeping Beauty, who assigns credence 1/2 to heads on waking, can avoid Dutch books by betting according to EDT. Vincent Conitzer (2015) argues that she remains Dutch-bookable even then. The episode shows that decision theory and the theory of self-locating credence cannot be fully separated. Which bets EDT endorses depends on which credences go into $P$.

**The core criticism.** Lewis and Joyce, as quoted in the source, hold that choosing an act for what it *indicates*, rather than what it *does*, confuses evidence with influence. The smoking lesion is their paradigm case. The tickle defence answers it for many such cases, but at a price: if screening off is pervasive, EDT may collapse into CDT, and its distinctive Newcomb verdict disappears with it. The theory's attractions and its vulnerabilities come from the same feature, its refusal to distinguish evidential from causal dependence at the level of the formula.

## 9. A procedure for unfamiliar cases

Collecting the above, here is how I would apply EDT to a new problem. Items marked † are my operational proposals rather than claims of the source.

1. **Specify the acts** $\mathcal{A}$ as propositions the agent can make true. Decide whether you are evaluating single acts or policies, and say so.†
2. **Build a joint credence model** over acts, states and outcomes. Include every process whose behaviour correlates with the agent's decision: predictors, copies, common causes, other agents running similar reasoning.
3. **Condition on all current evidence**, including introspective evidence about the agent's own desires and beliefs.† Check for screening off. Ask whether some variable the agent already observes renders the act probabilistically independent of payoff-relevant states. If it does, the act carries no extra news about those states.
4. **Compute** $V(A) = \mathbb{E}[u \mid A, E]$ for each act, with $E$ the agent's evidence, using any convenient partition of outcomes (the result is partition-invariant).
5. **Handle degeneracies** by evaluating at deliberation-time credences or by trembling-hand limits.†
6. **Choose** $\arg\max V$. Where it helps, report the threshold parameters (predictor accuracy, twin correlation) at which the verdict flips, as in §§3–4. This makes clear which empirical assumptions are doing the work.

**Quick test case.** A charity tells you that people who donate today are disproportionately those whose earlier donations were matched. You know the matching was decided by a lottery last week, and you know your own lottery result. Your act carries no further news about the lottery once you condition on your result. So the correlation is screened off, and EDT evaluates the donation on its ordinary merits. Compare a case in which an algorithm that simulates your decision procedure decides *now* whether to match donors. There the correlation runs through your deliberation, and EDT counts it.

## 10. Conclusion

Evidential decision theory is expected-utility theory with nothing added. Value is the conditional expectation of utility given the act, $V(A) = \mathbb{E}[u \mid A]$, computed from a single credence function over a single algebra of propositions. That simplicity gives it partition invariance and makes it well suited to cases where correlation arises through shared computation, as with Newcomb predictors and psychological twins. In those cases it recommends one-boxing and cooperation once correlation passes modest thresholds ($a > 0.5005$ and $p > 5/7$ in the examples above).

The same simplicity draws the "managing the news" objection. Whether EDT survives that objection depends on screening off: on whether the agent's evidence, properly conditioned on, removes spurious correlations without also removing the ones evidentialists want to keep. Anyone applying the theory must also settle questions the canonical formula leaves open: acts versus policies, and how to condition on improbable acts. With those choices made explicit, EDT gives a determinate and mechanically computable verdict in any decision problem.

## References

- Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9).
- Eells, E. (1982). *Rational Decision and Causality*. Cambridge University Press.
- Gibbard, A. & Harper, W. (1976). "Counterfactuals and Two Kinds of Expected Utility."
- Jeffrey, R. (1965). *The Logic of Decision*. McGraw-Hill.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59(1).
- MacAskill, W., Vallinder, A., Oesterheld, C., Shulman, C. & Treutlein, J. (2021). "The Evidentialist's Wager."
- Wikipedia contributors, "Evidential decision theory," revision 1373679688 (CC BY-SA 4.0), the reference source for this essay.