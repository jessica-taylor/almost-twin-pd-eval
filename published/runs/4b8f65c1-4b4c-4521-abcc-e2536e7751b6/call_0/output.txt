# Evidential Decision Theory: Choosing the Act You Would Most Like to Hear About

## 1. The slogan and the idea

Evidential decision theory (EDT) answers the question "what should I do?" with an unusual piece of advice: *do what you would most want to learn that you will do.* Arif Ahmed uses this phrase to summarize the theory, and the reference article repeats it. The idea is that an action is a proposition about the world, like any other. Learning that it is true would change your beliefs about many other things. EDT ranks actions by how good the world looks once you condition on each one. Following Jeffrey, this quantity is called the action's **news value**.

On this view, deciding is a kind of self-prediction. When I choose, I do two things. I bring about whatever my act causes, and I also learn something about the kind of world I am in. That second part includes facts my act does not cause, such as what a predictor foresaw or what a reasoner very like me will do. EDT counts both. Its main rival, causal decision theory (CDT), counts only the first.

This essay sets out the formal theory, works through the standard cases, and then takes up the questions the reference article leaves open: where the probabilities come from, what to condition on, and how to handle acts one is sure not to perform. I mark clearly where I go beyond the source.

## 2. The formal definition

The source follows Gibbard and Harper (1976) in contrasting two kinds of expected utility. The setup is as follows.

- A finite set of **actions** $A_1, \dots, A_n$. These are mutually exclusive propositions, exactly one of which you will make true.
- A partition of **outcomes** $O_1, \dots, O_m$. An outcome should include everything you care about.
- A **credence function** $P$ over a space of possibilities that includes your own actions.
- A **desirability** function $D(O_j)$, the value you place on outcome $O_j$.

EDT's value of an action is

$$
V(A) = \sum_j P(O_j \mid A)\, D(O_j),
$$

and EDT recommends choosing $A^\ast \in \arg\max_A V(A)$.

CDT uses the probability of the counterfactual "if I were to do $A$, $O_j$ would obtain" in place of the conditional probability:

$$
U(A) = \sum_j P(A \mathrel{\Box\!\!\rightarrow} O_j)\, D(O_j).
$$

As the source stresses, $P(O_j \mid A)$ and $P(A \mathrel{\Box\!\!\rightarrow} O_j)$ need not be equal. That gap is the entire disagreement between the two theories.

Some features of $V$ follow from the definition and are worth stating before the examples.

**(i) $V$ is a conditional expectation.** $V(A) = \mathbb{E}_P[D \mid A]$. Nothing about the formula is special to actions, since one could compute $V$ of any proposition. This is what "news value" means: $V(X)$ is how good you expect things to be on learning $X$.

**(ii) Partition invariance.** Suppose we refine the outcomes by a partition of states $S_k$. By the law of total probability,

$$
V(A) = \sum_k P(S_k \mid A)\, V(A \wedge S_k).
$$

The answer therefore does not depend on how finely we describe the world. This is a notable advantage over Savage-style theories, whose verdicts can depend on choosing a partition of states that is independent of the acts.

**(iii) Agreement with CDT under independence.** Suppose the world is described by states $S_k$ and acts $A$ that together fix the outcome $O(A,S_k)$. If states are probabilistically independent of acts, so that $P(S_k\mid A) = P(S_k)$, then

$$
V(A) = \sum_k P(S_k)\, D(O(A,S_k)),
$$

which is Savage's expected utility. CDT, on any reasonable semantics for counterfactuals, gives the same number when the act does not influence the state. In ordinary decisions the theories therefore agree, as the source notes. They come apart only when **an act is evidence about a state it does not cause.** The usual source of such evidence is a common cause: something upstream influences both your choice and the state of the world.

## 3. Newcomb's problem

Newcomb's problem is the standard case where the theories diverge. Box A is transparent and contains \$1,000. Box B is opaque. A reliable predictor has put \$1,000,000 in B if it predicted you would take only B, and nothing if it predicted you would take both boxes. You know all of this but not what the prediction was.

The source computes the values with 99% accuracy. Here is the general version. Write $M = 10^6$, $K = 10^3$, and let $p$ be the predictor's accuracy, assumed the same for both kinds of prediction. Then

$$
\begin{aligned}
V(\text{one-box}) &= pM, \\
V(\text{two-box}) &= (1-p)(M+K) + pK = (1-p)M + K.
\end{aligned}
$$

One-boxing wins if and only if $(2p-1)M > K$, that is,

$$
p > \tfrac12\left(1 + \tfrac{K}{M}\right) = 0.5005.
$$

At $p = 0.99$ we recover the source's figures: \$990,000 against \$11,000. The threshold is low. A predictor only slightly better than a coin is enough to make EDT one-box.

CDT reasons differently. The contents of box B are already fixed. Whatever they are, taking both boxes adds \$1,000. The **dominance argument** says that two-boxing is better in every state, so you should two-box.

EDT's reply makes clear what the theory assumes. Dominance reasoning is valid only when the states are independent of the acts. If we let $S \in \{\text{full}, \text{empty}\}$, then $P(S \mid \text{one-box}) \neq P(S \mid \text{two-box})$. Comparing payoffs state by state while ignoring that the act changes which state you should expect to be in is exactly the error that point (iii) identified. For the evidentialist, the dominance principle is a special case of expected-utility reasoning that holds under independence. It is not a basic principle of rationality.

## 4. The twin prisoner's dilemma

The source's second example removes the predictor. Aomame plays a one-shot prisoner's dilemma against a psychological twin whose reasoning mirrors hers exactly. The payoffs to her are \$5 if both cooperate, \$1 if both defect, \$10 if she defects and the twin cooperates, and \$0 if she cooperates and the twin defects. With perfect correlation, the source gets $V(C) = 5$ and $V(D) = 1$, so EDT says cooperate.

Again it helps to vary the strength of the correlation. Let $q = P(\text{twin matches} \mid \text{Aomame's act})$, assumed the same whichever act she takes. Then

$$
V(C) = 5q, \qquad V(D) = 10(1-q) + 1\cdot q = 10 - 9q,
$$

so EDT recommends cooperation if and only if $q > 5/7 \approx 0.714$.

Two observations follow.

1. The verdict depends on **how similar the twin is**, and EDT can say how similar is enough. This is the formal version of Hofstadter's "superrationality," which the source lists as related.
2. As in Newcomb's problem, the causal structure is a common cause: shared dispositions produce both agents' choices. CDT holds the twin's act fixed. Since defection dominates for any fixed act of the twin, CDT defects.

## 5. Common-cause cases where EDT seems to go wrong

The source presents EDT's verdicts in Newcomb's problem and the twin PD as natural. A serious account must also face the case usually taken to be EDT's weakest point. This example is my addition; the source does not discuss it.

**Smoking lesion.** Suppose a genetic lesion $L$ causes both lung cancer and a liking for smoking. Smoking itself causes nothing harmful and gives a small pleasure, worth $+1$. Cancer is worth $-100$. Take $P(C \mid L) = 0.9$, $P(C \mid \neg L) = 0.01$, and suppose that across the population $P(L \mid S) = 0.8$ and $P(L \mid \neg S) = 0.2$. A naive calculation gives

$$
\begin{aligned}
P(C\mid S) &= 0.8(0.9) + 0.2(0.01) = 0.722, \\
P(C \mid \neg S) &= 0.2(0.9) + 0.8(0.01) = 0.188, \\
V(S) &= 1 - 72.2 = -71.2, \qquad V(\neg S) = -18.8 .
\end{aligned}
$$

So naive EDT says to abstain. Most people find that absurd. Abstaining does not protect you; it only gives you better news about yourself. This is the force behind David Lewis's charge, quoted in the source, that EDT endorses "an irrational policy of managing the news."

**The tickle defence.** Evidentialists (notably Eells) answer that the naive calculation conditions on the wrong information. In the story, the lesion influences behaviour only through a desire $T$. A deliberating agent can feel her own desire, the "tickle," before she acts. The causal structure is $L \to T \to S$, with $L \to C$ as well. Conditional on the agent's actual desire $t$, the lesion is independent of the act:

$$
P(L \mid S, t) = P(L \mid t) = P(L \mid \neg S, t).
$$

Then $P(C \mid S, t) = P(C \mid \neg S, t)$, so $V(S \mid t) - V(\neg S \mid t) = +1$, and EDT says to smoke. The general lesson is that **EDT applied to an agent's total evidence, including what she knows about her own mental states, agrees with CDT whenever her inner states screen off the common cause from her act.**

Newcomb's problem and the twin PD are different. There the correlation runs through the *decision procedure itself*: the predictor models how you deliberate, and the twin deliberates the same way you do. Introspecting on your desires cannot screen this off, because the thing correlated with the state is the conclusion your reasoning reaches. On this reading EDT's divergence from CDT is principled. It diverges exactly when your *reasoning* is evidence about the world, and not merely your initial dispositions. This diagnosis is my interpretation. It is widely shared among evidentialists but is not stated in the source.

## 6. Open questions and an operational reading

The formula $V(A) = \sum_j P(O_j\mid A)D(O_j)$ is simple. Applying it to an unfamiliar case requires settling several questions the source does not raise. I take them in turn and propose working answers. These are my proposals.

### 6.1 Which probability function?

$P$ is the agent's credence **at the time of decision**, conditional on everything she knows at that moment: her observations, her introspective states, and the structure of the problem. In practice the steps are:

1. Write down a model of the situation, such as a causal graph or any joint distribution, that includes your own decision procedure as a variable.
2. Condition on all information available at the moment of choice.
3. For each act $A$, condition additionally on $A$ and compute $\mathbb{E}[D \mid A]$.

Section 5 shows that step 2 carries much of the weight. Leaving out introspective evidence is what produces the bad smoking-lesion verdict.

### 6.2 Acts you are sure you won't take

If $P(A) = 0$, then $P(O_j \mid A)$ is undefined, and a fully confident agent cannot evaluate her alternatives. This is a real problem: a perfectly self-predicting agent deliberating near the end would have $P(A)\to 0$ for every act but one. Three responses are reasonable:

- **Primitive conditional probability** (Popper–Rényi functions), in which $P(\cdot \mid A)$ is defined even when $P(A) = 0$.
- **Trembles.** Assign each act a small probability $\varepsilon$ of being chosen by mistake, compute $V_\varepsilon$, and take the limit $\varepsilon\to 0$. This works if the correlations of interest survive the limit.
- **Evaluate before self-prediction is settled.** Take $P$ to be credence formed *during* deliberation, before the agent has decided. This fits the "news" framing: you are asking what you would like to learn.

I recommend trembles as the default operational rule because it is the easiest to compute. It also makes explicit an assumption one would otherwise make silently: how a slip relates to the rest of the world. For instance, a slip should not carry information about the predictor's prediction unless the predictor anticipates slips.

### 6.3 Acts or policies?

The source frames EDT in terms of acts. Consider **transparent Newcomb**, in which box B is also transparent and you can see that it is full. Conditioning on what you see, $P(\text{full} \mid \text{two-box}, \text{sees full}) = 1$, so act-level EDT takes both boxes. The predictor, anticipating this, would leave B empty for agents who reason this way. Agents whose *policy* is "one-box whenever B is full" end up richer. Act-level EDT and a policy-level version, which evaluates $V(\pi) = \mathbb{E}[D \mid \text{my policy is } \pi]$ before any observation, disagree here. The literature contains this distinction ("updateless" variants), but the source is silent on it, and I do not think EDT as usually stated settles it. Act-level EDT is the standard reading. Readers should know that the standard reading gives up on policy-level gains in problems where predictors respond to policies.

### 6.4 Stability

Self-knowledge can feed back into the probabilities. Becoming more confident that you will do $A$ can change $P(S\mid B)$ for the other acts. Jeffrey's response was to require **ratifiability**: choose $A$ only if, conditional on having decided on $A$, no alternative has higher news value. Formally, $V(A \mid \text{decide } A) \ge V(B \mid \text{decide } A)$ for all $B$. Ratifiability is an optional refinement. It helps with instability but sometimes leaves no act ratifiable.

## 7. Sleeping Beauty and Dutch books

The source mentions an application of EDT in a different area: self-locating belief. In the Sleeping Beauty problem, a fair coin is tossed. If it lands heads, Beauty is woken once. If tails, she is woken twice, with her memory of the first waking erased. "Halfers" hold that on waking her credence in heads should be $1/2$. "Thirders" say $1/3$.

The source reports that halfers have been argued to be vulnerable to Dutch books, meaning sequences of bets each acceptable by their own lights that together guarantee a loss. It also reports that adopting EDT has been proposed as a way out. The mechanism is easy to see. On tails, Beauty's two wakings are subjectively identical, so whatever she decides at one waking is strong evidence that she decides the same at the other. This is the twin-PD correlation, with her own other waking as the twin. An evidential halfer accepting a bet therefore counts its tails payoff twice. That can restore the betting behaviour a thirder would show.

The source also notes Conitzer's (2015) argument that the remedy is incomplete: he constructs a Dutch book against halfers even when they reason evidentially. The literature has not settled which combinations of credence and decision theory avoid all such books. The lesson for us is modest. EDT's treatment of correlated decisions also applies to correlations between copies or time-slices of one agent, and how it interacts with theories of self-locating credence is still being worked out.

## 8. The evidentialist's wager

The source records one argument for EDT that is unusual because it does not rely on EDT being correct. MacAskill and coauthors argue that even if your credence in EDT is low, you may have reason to act as EDT recommends, because EDT's stakes are larger.

Here is a reconstruction. Suppose your action correlates with the choices of $N$ similar decision-makers, and each choice produces value $v$ for the world. Since your choice is evidence about all $N$, the evidential difference between two acts grows roughly like $N v$. The causal difference is about $v$, since you control only your own act. Under a rule that maximizes expected choiceworthiness across theories, with credence $c$ in EDT and $1-c$ in CDT, the EDT term dominates when roughly

$$
c \cdot N v_{\text{EDT}} > (1-c)\, v_{\text{CDT}},
$$

which, for large $N$, can hold even when $c$ is small. The argument depends on contested assumptions: that the two theories' values can be compared on a common scale, that maximizing expected choiceworthiness is the right way to handle uncertainty about theories, and that there really are many agents whose decisions correlate with yours. As a structural point it is still notable. EDT values grow with the number of correlated agents, and CDT values do not.

## 9. The central criticism

The objection in the source comes from Lewis and Joyce. Lewis calls EDT "an irrational policy of managing the news." Joyce writes that rational agents "choose acts on the basis of their *causal efficacy*, not their auspiciousness; they act to *bring about* good results even when doing so might betoken bad news."

The objection is strongest in cases like the smoking lesion, where EDT appears to recommend actions for their auspiciousness alone. Section 5 suggested that the tickle defence answers many such cases. What is left is a disagreement about cases like Newcomb's problem, where the correlation runs through the decision itself. There the evidentialist has a well-known counter, which Lewis himself discussed: "*Why ain'cha rich?*" Facing a reliable predictor, one-boxers predictably leave with about \$990,000 and two-boxers with about \$11,000. If rationality is supposed to serve the agent's ends, a theory whose followers reliably do worse needs some explanation.

The causalist answers that Newcomb's problem rewards irrationality: the predictor pays people for having a disposition, whatever makes that disposition rational. The evidentialist replies that "bringing about" is not the only thing that matters. Your choice is part of the world, and the world contains predictors, twins, and copies whose behaviour is bound up with yours. Neither side's argument settles the matter. What the formalism shows is exactly where they disagree. The theories coincide whenever $P(S \mid A) = P(S)$ for the relevant states. They differ only when the act is evidence about states it does not cause, and EDT counts that evidence.

## 10. A short procedure for unfamiliar cases

Collecting the above, here is a procedure for applying EDT. The source supplies the formula. The steps around it are my own.

1. **Specify outcomes and desirabilities** $D(O_j)$ finely enough to include everything you care about.
2. **Model the dependencies**, including your own deliberation and anything that responds to it or shares it: predictors, copies, similar agents.
3. **Condition on your total evidence**, especially introspective evidence about your desires and inclinations. This applies the tickle defence automatically.
4. **For each act $A$, compute** $V(A) = \sum_j P(O_j \mid A, E)\,D(O_j)$. If $P(A\mid E) = 0$, use a tremble limit.
5. **Choose the maximum.** If you are worried about instability, check ratifiability as well.
6. **Note whether act-level or policy-level evaluation matters.** It matters if something in the problem responds to your policy instead of your act. Report the verdict of each.

Applied to Newcomb's problem, this gives one-boxing whenever $p > 0.5005$. In the twin PD it gives cooperation whenever $q > 5/7$. In the smoking lesion with introspective access to one's desires, it says to smoke. In the ordinary case of carrying an umbrella, it gives the same answer as every other expected-utility theory.

## 11. Conclusion

EDT is the simplest form of expected-utility theory: the value of an act is the conditional expectation of desirability given that act. It agrees with Savage and with CDT whenever acts are independent of states. It disagrees exactly when an act is evidence about something it does not cause. In those cases, such as Newcomb's problem and the twin prisoner's dilemma, EDT follows the correlation and recommends the act associated with the better world. Its critics call this managing the news. Its defenders reply that one's reasoning is part of the world, and that ignoring correlations running through it is the real mistake. Applying the theory well depends on matters the bare formula leaves open: conditioning on total evidence, handling acts of probability zero, and deciding whether to evaluate acts or policies. With those settled, EDT gives a definite answer to any decision problem.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9).
- Gibbard, A. & Harper, W. (1976). *Counterfactuals and Two Kinds of Expected Utility.*
- Greene, P. & Levinstein, B. (2020). "Act Consequentialism without Free Rides." *Philosophical Perspectives* 34.
- Jeffrey, R. (1965/1983). *The Logic of Decision*. (Not cited in the source; the origin of news value and ratifiability.)
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59(1).
- MacAskill, W., Vallinder, A., Oesterheld, C., Shulman, C. & Treutlein, J. (2021). "The Evidentialist's Wager."
- Wikipedia contributors, "Evidential decision theory," revision 1373679688 (CC BY-SA 4.0).