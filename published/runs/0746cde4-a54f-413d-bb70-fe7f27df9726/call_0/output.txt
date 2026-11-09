# Evidential Decision Theory: Choosing Acts by the News They Bring

## 1. The slogan and the idea

Evidential decision theory (EDT) answers the question "what should I do?" with an unusual instruction: **do what you would most like to learn that you are going to do.** Following Ahmed (2021), the reference article describes the recommended act as the one with the highest *news value*. If you were told only "you are going to do $A$," how good would you expect your situation to be? EDT says to choose the act for which that expectation is highest.

Most of the time this matches ordinary practical reasoning. Learning that I will look both ways before crossing is good news because looking both ways makes being hit less likely. The theory becomes interesting, and contested, when an act is *evidence* about something it does not *cause*. Then EDT and its main rival, causal decision theory (CDT), come apart. This essay sets out the formal theory, works through the standard cases, and identifies where applying EDT requires choices that the bare formula leaves open. I mark clearly where I am reporting the reference article and where I am adding material from the wider literature or proposals of my own.

## 2. Formal definition

### 2.1 The basic formula

The reference article follows Gibbard and Harper (1976), who distinguished two kinds of expected utility. EDT maximizes

$$
V(A) \;=\; \sum_j P(O_j \mid A)\, D(O_j),
$$

where $\{O_j\}$ is a set of mutually exclusive, jointly exhaustive outcomes, $D(O_j)$ is the desirability of outcome $O_j$, and $P(O_j \mid A)$ is the agent's credence in $O_j$ conditional on performing act $A$. The rule is:

$$
\text{choose } A^* \in \arg\max_{A \in \mathcal{A}} V(A).
$$

CDT instead uses probabilities of counterfactual conditionals:

$$
U(A) \;=\; \sum_j P(A \mathrel{\Box\!\!\rightarrow} O_j)\, D(O_j),
$$

where $P(A \mathrel{\Box\!\!\rightarrow} O_j)$ is the probability that $O_j$ *would* obtain if $A$ were performed. As the source notes, these two quantities are not always equal, and so the two theories sometimes give different recommendations.

### 2.2 The states formulation (my elaboration)

The disagreement is easier to see if we introduce states $K_1, \dots, K_n$. These are features of the world that, together with the act, determine the outcome. Write $D(A \wedge K)$ for the desirability of doing $A$ when $K$ holds. Then:

$$
V(A) = \sum_k P(K_k \mid A)\, D(A \wedge K_k), \qquad
U(A) = \sum_k P(K_k)\, D(A \wedge K_k),
$$

The CDT formula on the right is Lewis's (1981) version. It requires that the $K_k$ be "dependency hypotheses," meaning states that the act cannot causally influence. Comparing the two formulas gives a simple diagnostic.

> **Agreement condition.** If the act is probabilistically independent of the causally relevant states, $P(K_k \mid A) = P(K_k)$ for all $k$, then $V(A) = U(A)$.

EDT and CDT therefore diverge exactly when the act is *correlated* with states it does not *cause*. Every famous case in this area is built on such a correlation. Typical sources are a predictor, a twin, a common cause, or a copy of oneself.

### 2.3 Two structural features

**Partition invariance.** $V(A)$ is just the conditional expectation $\mathbb{E}[D \mid A]$. It therefore takes the same value whichever partition of outcomes or states you use, provided desirabilities are assigned consistently. This is Jeffrey's (1965) averaging property. CDT is different: its answer depends on choosing the *right* partition, namely genuine dependency hypotheses or a correct causal model. EDT needs nothing beyond a probability function and a desirability function. Its defenders regard this as a major advantage, because the theory needs no primitive notion of causation or counterfactual dependence.

**Acts are propositions in the credence space.** To compute $P(\cdot \mid A)$, the agent must have credences about her *own* acts, and $P(A) > 0$ must hold for every act under consideration. Section 5 shows that this requirement is the source of most of the theory's interpretive difficulties.

## 3. The canonical cases

### 3.1 Newcomb's problem

The setup, as in the source: box A is transparent and contains \$1,000. Box B is opaque. A predictor with 99% accuracy has put \$1,000,000 in B if it predicted you would take only B, and nothing if it predicted you would take both. You choose between taking B alone and taking both boxes.

The source's computation is:

$$
\begin{aligned}
V(\text{one-box}) &= 0.99 \times 1{,}000{,}000 + 0.01 \times 0 = 990{,}000,\\
V(\text{two-box}) &= 0.01 \times 1{,}001{,}000 + 0.99 \times 1{,}000 = 11{,}000.
\end{aligned}
$$

EDT therefore recommends one-boxing. Taking one box is strong evidence that B is full.

**Generalization.** Let the predictor have accuracy $p$, let the large prize be $M$, and let the small one be $T$. Then

$$
V(\text{one}) = pM, \qquad V(\text{two}) = (1-p)M + T,
$$

so EDT recommends one-boxing iff

$$
p > \frac{1}{2}\left(1 + \frac{T}{M}\right).
$$

With the standard payoffs the threshold is $p > 0.5005$. The predictor only needs to be slightly better than chance.

**The CDT contrast.** Let $q$ be the unconditional probability that B is full. CDT computes $U(\text{one}) = qM$ and $U(\text{two}) = qM + T$. Two-boxing is better by exactly $T$ for every value of $q$. This is a dominance argument: whatever is in the box, taking both gets you \$1,000 more. EDT rejects this argument because the dominance reasoning holds the state fixed while varying the act, whereas in this problem the act is evidence about the state.

### 3.2 The twin prisoner's dilemma

The source's example: Aomame plays a one-shot prisoner's dilemma against a psychological twin whose reasoning mirrors her own. Payoffs to Aomame are \$5 if both cooperate, \$1 if both defect, \$10 if she defects while her twin cooperates, and \$0 if she cooperates while her twin defects. With perfect correlation:

$$
V(C) = 1 \cdot 5 + 0 \cdot 0 = 5, \qquad V(D) = 0 \cdot 10 + 1 \cdot 1 = 1,
$$

so EDT recommends cooperating.

**Generalization (mine).** Let $a = P(\text{twin } C \mid C)$ and $b = P(\text{twin } C \mid D)$. Then

$$
V(C) = 5a, \qquad V(D) = 10b + (1-b) = 1 + 9b.
$$

With symmetric reliability $b = 1 - a$, cooperation is recommended iff $5a > 1 + 9(1-a)$, that is, iff $a > 5/7 \approx 0.714$. The correlation needs to be substantial but not perfect. Once again CDT defects for any fixed credence about the twin, since defection dominates. EDT's cooperative verdict is closely related to Hofstadter's "superrationality."

The structural lesson from both cases is that **EDT treats one's own choice as an observation**. Whatever the choice is evidence about, including other agents' choices and the contents of opaque boxes, enters the calculation through the conditional probabilities.

## 4. The main objection: managing the news

The source quotes two prominent critics. Lewis (1981) called EDT "an irrational policy of managing the news." Joyce (1999) wrote: "Rational agents choose acts on the basis of their *causal efficacy*, not their auspiciousness; they act to *bring about* good results even when doing so might betoken bad news."

The objection is clearest in a case the source does not discuss: the **smoking lesion**, sometimes called the medical Newcomb problem. Suppose a genetic lesion $L$ causes both lung cancer and a strong desire to smoke. Smoking itself is harmless, and the agent enjoys it. Then $P(L \mid \text{smoke}) > P(L \mid \neg\text{smoke})$. A naive EDT calculation can recommend abstaining, because smoking is bad news about one's genes. Almost everyone, many evidentialists included, finds that verdict absurd. Abstaining does nothing to the lesion.

Numerically: let smoking add utility $s$, let cancer cost $c$, let $P(\text{cancer} \mid L) = r$, and suppose cancer never occurs without the lesion. Then

$$
V(S) - V(\neg S) = s - c\,r\,[P(L \mid S) - P(L \mid \neg S)],
$$

which is negative whenever the evidential correlation is strong enough relative to $s$.

### 4.1 The tickle defence (from the literature, not the source)

The standard evidentialist reply is the *tickle defence*, developed most fully by Eells (1982). The lesion affects behaviour only by way of the agent's desires and beliefs. A reflective agent can introspect those desires. Call the felt urge $T$, the "tickle." If the agent conditions on everything she knows, including $T$, then plausibly

$$
P(L \mid S \wedge T) = P(L \mid \neg S \wedge T) = P(L \mid T),
$$

because the act carries no information about the lesion beyond what the tickle already revealed. The correlation is *screened off*, the agreement condition of §2.2 holds, and EDT recommends smoking, the same answer as CDT.

This reply shows that **EDT's verdicts depend heavily on what the agent is taken to know about herself at the moment of choice.** The formula $V(A) = \sum_j P(O_j \mid A) D(O_j)$ is complete only once the credence function $P$ is fully specified, including the agent's self-knowledge.

### 4.2 Does the tickle also defuse Newcomb?

This question is open, and the source does not raise it. If the predictor works by reading the same psychological states that produce the choice, then the tickle argument appears to apply to Newcomb as well. Once the agent knows her own dispositions, the act may carry no further news about the prediction, and EDT would then recommend two-boxing. Eells drew roughly this conclusion. Other evidentialists reply that a deliberating agent cannot fully know her own decision before making it, so some correlation remains. The source's Newcomb calculation implicitly assumes that $P(\text{full} \mid \text{one-box}) = 0.99$ survives all self-knowledge available at the time of choice. That assumption is the standard way of stating the problem, but it is substantive.

My operational suggestion follows. When applying EDT, **condition on everything the agent knows at the moment of choice**, including introspectively available desires and reasons. Then ask whether the act is *still* informative about the relevant state. If it is, as with a twin who will run the same deliberation, or a predictor modelling the deliberation itself rather than some upstream cause, EDT diverges from CDT. If it is not, as with a lesion acting through felt desires, the theories agree. This keeps EDT's distinctive verdicts in the cases where its defenders want them and removes the most embarrassing ones. It does so at the price of making the theory sensitive to fine details of the agent's epistemic state.

## 5. Open technical questions and operational choices

### 5.1 Conditioning on one's own act

$P(O \mid A)$ is defined only if $P(A) > 0$. Two problems follow.

1. **Certainty about one's choice.** If deliberation ends with the agent certain she will do $A^*$, then $P(A) = 0$ for every alternative, and the alternatives' news values are undefined.
2. **Instability.** The conditional probabilities may change as deliberation shifts the agent's credences about what she will do.

The source does not discuss these problems. One reasonable operational interpretation, which I adopt and which is in the spirit of Jeffrey's later work on ratifiability and of trembling-hand ideas in game theory, is the following.

> Evaluate acts using the agent's credences *during* deliberation, with every available act given small positive probability $\varepsilon$. Define $V(A)$ as the limit as $\varepsilon \to 0$, provided the conditional probabilities converge.

A stronger and more contested refinement is **ratifiability** (Jeffrey 1983). Choose an act $A$ such that, on the supposition that you have decided to do $A$, no alternative has higher news value. Ratifiability tends to push EDT toward CDT-like verdicts in tickle-style cases. It is best treated as an optional supplement, not part of the core theory.

### 5.2 Acts versus policies

EDT can be applied to individual acts or to *policies*, meaning functions from observations to acts. The two can come apart. Consider a transparent-box variant of Newcomb in which you see the contents of box B before choosing. Conditioning on having already seen a full box, two-boxing gives better news: the prediction is no longer uncertain. Evaluated as a policy chosen in advance ("one-box whatever I see"), one-boxing is better, because the predictor responds to the policy. Standard EDT as presented in the source is act-based. Policy-level evaluation, as in "updateless" proposals, is a further step. In unfamiliar cases you should state which level you are evaluating at.

### 5.3 Multiple copies: Sleeping Beauty

The source mentions that EDT has been applied to the Sleeping Beauty problem in the context of Dutch books. Recall the setup. A fair coin is tossed. On heads, Beauty is woken once. On tails, she is woken twice, with her memory erased between awakenings. "Halfers" assign credence $1/2$ to heads on waking, and "thirders" assign $1/3$.

The following illustration is mine, along the lines of Briggs (2010). At each awakening Beauty is offered a bet that costs $c$ and pays \$1 if the coin landed tails. An EDT agent recognizes that her decision in one tails-awakening is evidence of, indeed practically guarantees, the same decision in the other. Accepting therefore means accepting twice if tails. With halfer credences:

$$
V(\text{accept}) = \tfrac12(-c) + \tfrac12 \cdot 2(1-c) = 1 - \tfrac32 c,
$$

so she accepts iff $c < 2/3$. A thirder who evaluates each awakening on its own (CDT-style) accepts iff $\tfrac23(1-c) - \tfrac13 c > 0$, which is also iff $c < 2/3$. The EDT halfer and the CDT thirder have the same betting behaviour. This is the sense in which EDT helps halfers escape Dutch books built on mismatched betting rates. The source reports that Conitzer (2015) argues halfers remain Dutch-bookable even with EDT, so the escape is disputed. More generally, whenever an agent's decision is replicated across copies, EDT counts every copy's act as news, and this can change the effective stakes.

## 6. A supporting argument: the evidentialist's wager

The source reports an argument from MacAskill et al. (2021): even someone who gives EDT less credence than CDT may have reason to *act as if* EDT were true. The reconstruction below is mine.

Suppose there are $N$ agents whose decisions are correlated with yours. They could be agents in a large universe running similar decision procedures. CDT counts only the causal effect of your own act, $\Delta_{\text{CDT}}$. EDT counts your act as evidence about all $N$ correlated acts, so its stakes are roughly $\Delta_{\text{EDT}} \approx N\delta$, where $\delta$ is the per-agent difference. With credence $q$ in EDT and $1-q$ in CDT, and assuming the two theories' value scales can be compared, the weighted stakes are

$$
q \cdot N\delta \quad \text{versus} \quad (1-q)\,\Delta_{\text{CDT}}.
$$

For large $N$, EDT's recommendation dominates even when $q$ is small.

The argument depends on contestable assumptions. One is that utilities can be meaningfully compared *across* decision theories. Another is that one should maximize expected choiceworthiness when uncertain about the decision theory itself. Fanaticism worries also apply. The argument should be read as conditional, not decisive.

## 7. The philosophical case, briefly

**For EDT.** Its defenders offer the "why ain'cha rich?" challenge: in repeated Newcomb problems, one-boxers walk away with millions and two-boxers with thousands. They also point to EDT's parsimony. It needs only probability and desirability, with no causal or counterfactual primitives, and it is partition-invariant. Finally, they argue that "causal efficacy" adds nothing once all the agent's evidence is properly accounted for.

**Against EDT.** Lewis's charge is that choosing for the sake of good news is wishful thinking with extra steps. Since the boxes are already filled, one-boxing only *feels* like it secures the million. Joyce's version holds that rational action aims at *bringing about* good outcomes, and that an act can be auspicious without being efficacious. CDT's defenders typically answer the "why ain'cha rich?" challenge by saying that Newcomb problems reward irrationality: the predictor pays people for being disposed to choose badly.

Which side is right depends on what one takes rational agency to be. On one view, the agent is an intervener in a causal system. On the other, the agent is one more part of the world, whose choices are informative events like any others.

## 8. Applying EDT to an unfamiliar case: a procedure

What follows is my synthesis. The source does not offer an algorithm.

1. **Fix the option set** $\mathcal{A}$, and decide whether you are evaluating acts or policies.
2. **Specify outcomes and desirabilities** $D$. Any partition fine enough to determine desirability will do.
3. **Specify the agent's credence function** $P$ at the moment of choice. Include everything she knows about her own desires and reasons, and give every act positive probability (§5.1).
4. **Run the agreement check.** Identify the states $K$ relevant to outcomes. If $P(K \mid A) = P(K)$ for all $K$ and $A$, then EDT agrees with CDT, so compute ordinary expected utility and stop.
5. **Check for screening off.** If there is a correlation, ask whether it passes entirely through something the agent already knows, such as a tickle. If it does, condition on that and repeat step 4.
6. **Compute** $V(A) = \sum_j P(O_j \mid A)\, D(O_j)$ for each $A$ and choose the maximum. Threshold formulas like those in §3 are useful for seeing how robust the verdict is.
7. **Optionally check ratifiability**, and report whether the verdict survives it.

**Example.** Two identical copies of an AI system are deployed independently. Each can either share a resource (cooperate) or grab it (defect), with the payoffs of §3.2. They cannot communicate, but they run identical code on identical inputs. At step 4, the other copy's act is not independent of mine. At step 5, no further self-knowledge screens it off, because the correlation runs through the deliberation itself. At step 6, with $a \approx 1$, cooperation is recommended, since $a > 5/7$. Now change the case so that the copies receive different random seeds that substantially decorrelate them. The verdict then depends on whether the conditional probability of matching still exceeds $5/7$.

## 9. Conclusion

Evidential decision theory ranks acts by their conditional expected desirability, $V(A) = \mathbb{E}[D \mid A]$. It treats one's own choice as a piece of evidence about the world. When the act is independent of the states it does not cause, EDT and CDT coincide. They diverge exactly when there is correlation without causation. Newcomb's problem and the twin prisoner's dilemma are the canonical cases, and in both EDT recommends the "cooperative" or "one-box" option, as the source's calculations show. The theory's elegance comes from its parsimony and partition invariance. Its difficulties come from the same source: everything depends on the conditional credences, so applying EDT responsibly means specifying the agent's self-knowledge, handling zero-probability acts, and deciding whether to evaluate acts or policies. The tickle defence, ratifiability, and policy-level evaluation are the main tools for doing this, and they substantially narrow the gap between EDT and CDT in ordinary cases. Whether choosing by good news is rational foresight or self-deception, the "managing the news" charge of Lewis and Joyce, remains the central philosophical question.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Briggs, R. (2010). "Putting a value on Beauty." *Oxford Studies in Epistemology* 3.
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9).
- Eells, E. (1982). *Rational Decision and Causality*. Cambridge University Press.
- Gibbard, A. & Harper, W. (1976). "Counterfactuals and Two Kinds of Expected Utility."
- Jeffrey, R. (1965/1983). *The Logic of Decision*. University of Chicago Press.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59(1).
- MacAskill, W., Vallinder, A., Oesterheld, C., Shulman, C. & Treutlein, J. (2021). "The Evidentialist's Wager."