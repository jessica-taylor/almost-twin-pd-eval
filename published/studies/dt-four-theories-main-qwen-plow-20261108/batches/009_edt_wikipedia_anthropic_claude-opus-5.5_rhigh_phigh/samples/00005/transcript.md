# 009_edt_wikipedia_anthropic_claude-opus-5.5_rhigh_phigh / 00005

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/24bf53a2-3542-4491-8a61-dee147f3e7b9/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/24bf53a2-3542-4491-8a61-dee147f3e7b9/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Choosing the Action You Would Most Like to Hear About

## 1. The slogan and the idea

Evidential decision theory (EDT) is usually summarised by a slogan from Arif Ahmed: *do what you most want to learn that you will do* [1]. Picture a well-informed friend who tells you, "You are going to do $A$." That report would change what you expect about the world. EDT ranks each available act by how good that news would be in expectation. This quantity is the act's **news value**. EDT tells you to choose the act whose news value is highest.

The usual rival is causal decision theory (CDT), which ranks acts by what they would *bring about*. In most ordinary situations the two theories agree. They disagree when an act carries information about something it does not cause. Newcomb's problem and the twin prisoner's dilemma are the standard examples, and the reference article treats both [1, 2].

This essay does four things. It states EDT precisely, works through the canonical cases, isolates the questions that the bare formula leaves unsettled, and proposes an operational reading that a reader could apply to cases not discussed here. I mark which claims come from the source material and which are my own additions.

## 2. The formal definition

### 2.1 News value

Following Gibbard and Harper's 1976 distinction between "two kinds of expected utility" [2], the source defines EDT's value of an action $A$ as

$$
V(A) = \sum_j P(O_j \mid A)\, D(O_j),
$$

Here $\{O_j\}$ is a partition of possible outcomes, $D(O_j)$ is the desirability of outcome $O_j$, and $P(O_j \mid A)$ is the agent's ordinary conditional credence that $O_j$ obtains given that she performs $A$. EDT prescribes

$$
A^* \in \arg\max_{A \in \mathcal{A}} V(A).
$$

Two features of this definition matter for everything that follows.

1. **Acts are propositions.** The act "I take only box B" is an event in the same probability space as "box B contains \$1M." The agent therefore holds credences about her own behaviour, and she updates on a hypothetical act exactly as she would update on any other evidence.
2. **No counterfactual operator appears.** The dependence that matters is probabilistic. Whatever correlation the agent's credences encode between $A$ and $O_j$ affects $V(A)$, whether it comes from causation, a common cause, or anything else.

### 2.2 Partition invariance (my addition, drawing on Jeffrey's framework)

For EDT, the choice of outcome partition does not matter. This is a significant structural advantage. Take any partition $\{S_k\}$ of "states" and define the desirability of a conjunction $A \wedge S_k$ as its own conditional expectation. The law of total expectation then gives

$$
V(A) = \sum_k P(S_k \mid A)\, V(A \wedge S_k).
$$

The answer is the same whether you decompose by "contents of box B," "what the predictor predicted," or anything else. Savage-style expected utility works differently. It writes $\sum_k P(S_k)\,u(A, S_k)$ with *unconditional* state probabilities, and so it gives correct answers only when the states are chosen to be independent of the acts. EDT has no need to identify such a privileged partition. It conditions on the act and lets the probabilities handle the rest.

### 2.3 The causal contrast

The source contrasts $V$ with CDT's counterfactual expected utility:

$$
U(A) = \sum_j P(A \mathrel{\Box\!\!\rightarrow} O_j)\, D(O_j),
$$

where $P(A \mathrel{\Box\!\!\rightarrow} O_j)$ is the probability that $O_j$ *would* obtain if $A$ were performed [2]. The two theories diverge exactly when $P(A \mathrel{\Box\!\!\rightarrow} O_j) \neq P(O_j \mid A)$.

A useful sufficient condition for agreement follows (this is my framing). Suppose there is a partition of states $\{S_k\}$ that meets two conditions:

- (i) the states are **probabilistically independent** of the acts, $P(S_k \mid A) = P(S_k)$;
- (ii) the outcome is **fixed by act and state**, $O = f(A, S_k)$.

Then

$$
V(A) = \sum_k P(S_k)\, D(f(A,S_k)) = U(A),
$$

because under these conditions both the conditional and the counterfactual probability of an outcome reduce to the prior weight of the states that produce it. Every disagreement between EDT and CDT therefore requires an act that is *evidence about* a state it does not *cause*.

## 3. Canonical cases

### 3.1 Newcomb's problem

The setup is as follows. Box A is transparent and holds \$1,000. Box B is opaque. It holds \$1,000,000 if a reliable predictor foresaw that you would take only B, and nothing if it foresaw that you would take both [3]. Suppose the predictor's accuracy is $p$, in the sense that $P(\text{predicted } X \mid \text{do } X) = p$. Write $M = 10^6$ and $K = 10^3$. Then

$$
\begin{aligned}
V(\text{one-box}) &= pM, \\
V(\text{two-box}) &= (1-p)(M+K) + pK = (1-p)M + K.
\end{aligned}
$$

With $p = 0.99$ this gives \$990,000 against \$11,000, which matches the source [1]. More generally, EDT one-boxes if and only if

$$
pM > (1-p)M + K \iff p > \frac{M+K}{2M} = 0.5005.
$$

A predictor only slightly better than a coin is enough. The threshold tells us how the theory works internally. The \$1,000 in box A is a sure causal gain. It is outweighed whenever the evidential swing in box B's expected contents, $(2p-1)M$, is larger than that gain.

CDT reasons differently. The prediction has already been made, and choosing now cannot alter it. Whatever is in B, taking both yields \$1,000 more. CDT therefore two-boxes, and does so for every value of $p$.

### 3.2 The twin prisoner's dilemma

Aomame plays a one-shot prisoner's dilemma against a psychological twin who reasons exactly as she does [4]. The payoffs to Aomame are:

| | Twin cooperates | Twin defects |
|---|---|---|
| Aomame cooperates | 5 | 0 |
| Aomame defects | 10 | 1 |

The source assumes perfect correlation and obtains $V(C) = 5$ and $V(D) = 1$. To see how much the verdict depends on that assumption, let the correlation be imperfect: $P(\text{twin }C \mid C) = P(\text{twin }D \mid D) = q$. Then

$$
V(C) = 5q, \qquad V(D) = 10(1-q) + q = 10 - 9q,
$$

and EDT cooperates if and only if $q > 5/7 \approx 0.714$. Below that threshold, the correlation is too weak to outweigh the dominance advantage of defecting, and EDT defects just as CDT does. EDT is therefore not a theory that always cooperates. Its recommendation depends on how strong the correlation actually is.

This case shows that the correlations EDT responds to need not involve an external predictor. A shared decision procedure is enough. This is the link to Hofstadter's "superrationality," which the source lists under "See also."

### 3.3 A case where EDT looks bad: the smoking lesion (not in the source)

The source's criticism section deals only with general objections. The case most often pressed against EDT is the following. A genetic lesion causes both lung cancer and a liking for smoking. Smoking itself is harmless and mildly pleasant, worth $+1$. Cancer is worth $-100$. Suppose that in the population

$$
P(\text{cancer} \mid \text{smoke}) = 0.8, \qquad P(\text{cancer} \mid \neg\text{smoke}) = 0.2.
$$

A naive calculation gives

$$
V(\text{smoke}) = 1 - 80 = -79, \qquad V(\neg\text{smoke}) = -20.
$$

On this calculation EDT says not to smoke. Most people judge this an error, because abstaining changes only the news and not the risk. This is the "managing the news" charge in concrete form.

The standard evidentialist reply is the **tickle defence**, developed by Eells and others. The lesion can influence your choice only through something you can detect, such as a desire, an urge, or a "tickle." Let $T$ denote your current motivational state, which you know at the time of deciding. If the lesion's influence on the act passes entirely through $T$, then once you condition on $T$ the act carries no further information about the lesion:

$$
P(\text{cancer} \mid \text{smoke}, T) = P(\text{cancer} \mid \neg\text{smoke}, T) = P(\text{cancer} \mid T).
$$

With this screening-off in place,

$$
V(\text{smoke}) - V(\neg\text{smoke}) = 1 > 0,
$$

and EDT smokes. The general lesson is that the correlations in population statistics are not always the correlations that hold *from the agent's own epistemic position*. EDT asks for the second kind.

The tickle defence has costs of its own. It assumes a level of introspective access that may be unrealistic, and modified versions of the case have been built so that screening-off fails. Ahmed's book-length defence of EDT [1] engages these variants at length. For practical use, the key point is that whether EDT one-boxes, smokes, or cooperates depends on the conditional credences, and getting those right is where most of the substantive work lies.

## 4. Open questions and an operational interpretation

The formula $V(A) = \sum_j P(O_j \mid A) D(O_j)$ leaves several things unsettled. The source does not address them, but anyone who wants to apply EDT to new cases has to settle them somehow. For each, I describe the difficulty and propose a resolution. These resolutions are my own suggestions. They are not part of EDT as the source defines it.

### 4.1 Which credence function? (the conditioning base)

**Problem.** $P(O \mid A)$ depends on what else is in the background. Different background information can reverse the verdict, as the smoking lesion shows.

**Proposal.** Use the agent's credences *at the moment of decision*. These should be conditioned on everything she knows at that moment, including introspectively available facts about her own desires, beliefs, and reasoning. Population correlations should be used only after checking whether they survive this conditioning.

In practice this means asking a specific question. Given everything I currently know about myself, would learning that I did $A$ rather than $B$ still change my credence in $O$? If the answer is yes, the dependence counts.

- In Newcomb's problem it counts. The predictor tracks your actual decision procedure, including the part not yet resolved by your deliberation.
- In the twin case it counts. Your twin runs the same procedure you are now running.
- In a tickle-screened lesion case it does not count.

### 4.2 Zero-probability acts

**Problem.** If $P(A) = 0$, then $P(O \mid A) = P(O \wedge A)/P(A)$ is undefined. This is not a technicality. An agent who is confident in her own rationality may be nearly certain what she will do, and then conditioning on the alternatives becomes ill-defined or unstable.

**Proposal.** Treat deliberation as taking place under a credence function that gives every available act positive probability. A simple way to do this is to fix a small $\varepsilon > 0$, suppose that each act is chosen with probability at least $\varepsilon$ through some "tremble" independent of everything else, and take the limit as $\varepsilon \to 0$. This works when the limit exists. A more general approach uses conditional probability functions in the style of Popper or Rényi, which define conditioning on null events directly.

Both approaches carry a substantive commitment. You must say how the world would correlate with an act you will not in fact choose. The tremble model makes that commitment explicit. In Newcomb's problem, the question is whether the predictor tracks the trembles. The modeller has to state an answer. The formalism will not supply one.

### 4.3 Acts or policies?

**Problem.** The source evaluates single actions. Some problems, however, contain several decision points that are indistinguishable to the agent, or contain predictors that respond to how the agent *would* act in situations that never occur. In such problems it is unclear whether the "act" being conditioned on is the local choice or the whole policy.

**Proposal.** Whenever the agent's choices at different points come from the same procedure and cannot be distinguished from her own point of view, the evidential force of "I do $A$ here" spreads to every point where that procedure runs. The natural thing to condition on is therefore the policy. For EDT this is a consequence of the theory and not an additional principle, since learning that I choose $A$ now is evidence that I choose $A$ at every relevantly identical point.

Problems that are not covered by this argument, such as cases where the decision points differ in what the agent knows, are where "updateless" descendants of EDT depart from the standard theory. I leave those cases open.

### 4.4 An illustration: Sleeping Beauty

The source reports that EDT has been invoked to protect "halfers" in the Sleeping Beauty problem from Dutch books, and that Conitzer argues the protection fails [5]. A simple calculation, which is my own illustration, shows how the policy point drives the first claim.

A fair coin is tossed. On heads, Beauty is woken once. On tails, she is woken twice, with her memory erased in between. At every awakening she is offered the same bet: pay $x$ to receive \$1 if the coin landed tails.

- **Halfer using EDT.** Beauty's credence in tails is $1/2$. Her awakenings are indistinguishable, so accepting now is evidence that she accepts at every awakening. If the coin landed tails she gains $2(1-x)$. If it landed heads she loses $x$. So
$$V(\text{accept}) = \tfrac12 \cdot 2(1-x) - \tfrac12 x = 1 - \tfrac32 x,$$
which is positive exactly when $x < 2/3$.
- **Thirder using CDT.** Her credence in tails is $2/3$. She evaluates the single bet in front of her and accepts exactly when $x < 2/3$.

The two combinations price the bet identically, which is why pairing halfing with EDT can prevent the obvious Dutch book. Conitzer's 2015 paper constructs more elaborate betting arrangements against EDT halfers [5]. I do not reconstruct his argument here. The point to take away is that EDT's verdicts in self-locating problems depend on the correlation between one's choices at indistinguishable moments, which is exactly the issue in §4.3.

## 5. Arguments for and against

### 5.1 For: "Why ain'cha rich?" (beyond the source)

A common informal argument appeals to outcomes. Run Newcomb's problem many times. Agents who one-box walk away with about \$990,000 on average, and agents who two-box walk away with about \$11,000. A theory of rational choice ought to be one whose followers predictably do well.

The causalist reply goes back to Lewis. The predictor rewards a particular kind of irrationality, so it is no surprise that irrational agents end up richer, and their wealth does not show that their choices were correct. Whether that reply works depends on contested views about what rationality is for.

### 5.2 For: the evidentialist's wager (from the source)

The source reports an argument from MacAskill and colleagues [6]. Even an agent who gives most of her credence to CDT may have reason to *act* as though EDT were true.

The reasoning runs as follows. Suppose $N$ other agents' decisions are correlated with yours. Under EDT your choice is evidence about all $N + 1$ decisions, so the difference in value between your options grows roughly in proportion to $N$. Under CDT you control only your own decision.

Here is a toy version, which is my formalisation. Let $\Delta_C$ be CDT's per-agent difference in favour of $B$, and let $\Delta_E$ be EDT's per-agent difference in favour of $A$. If you assign credence $c$ to EDT and simply average the two theories' values on a common scale, then $A$ is favoured when

$$
c\,(N+1)\,\Delta_E > (1-c)\,\Delta_C.
$$

This holds for any $c > 0$ once $N$ is large enough. The argument rests on two contested assumptions: that values from different decision theories can be meaningfully compared on one scale, and that averaging is the right way to handle uncertainty about which decision theory is correct. Both remain open questions.

### 5.3 Against: managing the news

The objection the source emphasises comes from Lewis, who called EDT "an irrational policy of managing the news" [7]. Joyce put the same point this way: rational agents "act to *bring about* good results even when doing so might betoken bad news" [8].

The smoking lesion makes the objection concrete. When evidential and causal relevance come apart, EDT can recommend acts whose only merit is what they indicate.

Evidentialists answer in two steps.

1. **Many alleged counterexamples disappear on correct conditioning.** This is the tickle defence and the procedure in §4.1.
2. **In the cases that remain, the EDT verdict is defensible.** Newcomb's problem and the twin dilemma are the main examples. In both, the correlation runs through the agent's own decision procedure. Choosing differently there would plausibly mean *being* a different kind of agent, and that is not mere news management.

Whether this answer succeeds is still the central dispute in the field.

## 6. A procedure for unfamiliar cases

Here is the procedure I recommend, combining the source's definition with the proposals of §4.

1. **List the acts** $\mathcal{A}$ that are genuinely available to the agent. If her decision points share a procedure and cannot be told apart, treat the acts as policies.
2. **Choose any outcome partition** fine enough to capture everything that bears on desirability. Partition invariance means you need not search for "independent states."
3. **Fix the conditioning base.** Use the agent's credences at the time of deciding, including her self-knowledge. For each correlation between act and outcome, ask whether it survives conditioning on what she knows about her own motives. Discard correlations that are screened off.
4. **Handle null acts.** If some act has probability zero, define $P(\cdot \mid A)$ by an explicit tremble model or a conditional probability function, and state what the model assumes about whether trembles are correlated with the world.
5. **Compute** $V(A) = \sum_j P(O_j \mid A)\,D(O_j)$ for each act, and choose the maximum.
6. **Check whether EDT and CDT differ.** If the acts are independent of the states, the two theories coincide and the case raises no special issue. If they are not, find where the dependence comes from: causation, a common cause, or a shared procedure. Report how sensitive the verdict is, for example as a threshold like $p > 0.5005$ or $q > 5/7$.

## 7. Conclusion

EDT is expected-utility maximisation with the act treated as evidence. Its value function, $V(A) = \sum_j P(O_j \mid A)\,D(O_j)$, needs no counterfactuals and no privileged states, and it gives the same answer under any outcome partition.

EDT differs from CDT exactly when an act is evidence about something it does not cause. In that situation EDT one-boxes in Newcomb's problem once predictor accuracy exceeds $(M+K)/2M$, and cooperates with a twin once the correlation exceeds $5/7$ for the payoffs above.

The theory's problems lie less in the formula than in its inputs. Applying it requires deciding whose credences to use and conditioned on what, how to condition on acts one will not perform, and whether to evaluate single acts or whole policies. The proposals made here are to condition on the agent's full self-knowledge, to make tremble assumptions explicit, and to condition on policies when decision points are indistinguishable. Together they make EDT usable on new cases, though they do not settle the philosophical dispute with CDT. That dispute concerns whether the evidential relevance of one's choices is, in itself, a reason for action. EDT says it is. Lewis and Joyce say it amounts only to managing the news.

## References

1. Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
2. Gibbard, A., & Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*.
3. Wolpert, D. H., & Benford, G. (2013). "The lesson of Newcomb's paradox." *Synthese* 190(9).
4. Greene, P., & Levinstein, B. (2020). "Act Consequentialism without Free Rides." *Philosophical Perspectives* 34(1).
5. Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9).
6. MacAskill, W., Vallinder, A., Oesterheld, C., Shulman, C., & Treutlein, J. (2021). *The Evidentialist's Wager*.
7. Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59(1).
8. Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm planning a mathematical essay on evidential decision theory, around 2400 to 3000 words, and I need to keep track of which points come from the sources and which are my own additions. The outline covers the definition and news value, conditional probability, the contrast with causal decision theory, and the standard cases: Newcomb's problem, the twin prisoner's dilemma, and briefly Sleeping Beauty. It then moves to the evidentialist's wager, the managing-the-news criticism, the smoking lesion case, and the tickle defense, ending on open questions about zero-probability actions, what counts as an action, and partition invariance.

I'm checking the Newcomb payoffs, which work out to 11,000 for taking both boxes, and then setting up the technical points: partition invariance in Jeffrey's framework, when EDT and CDT agree, and the threshold accuracy for one-boxing in Newcomb's problem.

I'm verifying the twin prisoner's dilemma threshold: cooperating beats defecting once the twin's matching probability q exceeds 5/7. Then I'm working through the smoking lesion case, where naive EDT says abstain, while conditioning on one's own desires, the tickle, screens off the lesion and would have the agent smoke; I'll mark that defense as my addition rather than from the sources.

I'm working through the operational side now: treating the probability of each act as positive during deliberation, using something like Popper functions or small trembles to handle that, and asking whether the unit of choice should be a single act or a policy. I'm also sketching how the evidentialist's wager would scale with the number of correlated agents, and I'm noting the Sleeping Beauty point as a brief aside.

I'm now working through the Sleeping Beauty aside, specifically how an evidentialist would evaluate a bet offered at each awakening, since those awakenings are indistinguishable to her.

I'm checking the Sleeping Beauty illustration: a halfer using EDT, treating her bet at each awakening as correlated, gets a value of 1 − 1.5x, so she accepts below 2/3, the same threshold a thirder reaches under CDT.

I'm now writing up the operational procedure: specifying the acts, choosing a fine enough outcome partition, setting a joint credence that includes the agent's own dispositions, computing each act's value, and handling zero-probability acts through limits. I'm also noting that dependence should count only if the correlation survives conditioning on everything the agent knows about herself at decision time, and that EDT relies on indicative supposition rather than counterfactuals, so I'll contrast P(O|A) with the counterfactual P(A □→ O) and mention Lewis's imaging.

I'm laying out the essay's remaining sections: the formal definition with partition invariance, the contrast with causal decision theory, the Newcomb and twin prisoner's dilemma cases, the smoking lesion problem with the tickle defense, the open questions about policies and zero-probability acts, the arguments for and against, and a closing procedure checklist.

I'm wrapping up the essay plan by listing the closing sections, the references, and a word-count target of around 2700 words.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/db4c0ed1-74ed-44c7-a1bb-9fbc4ce4fe2a/call_0/request.json)

[Authoritative raw response](../../../../../../runs/db4c0ed1-74ed-44c7-a1bb-9fbc4ce4fe2a/call_0/response.raw) · finish: `content_filter`

### Visible response

No text returned.

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working through the twin prisoner's dilemma under evidential decision theory, looking at the payoffs for each cooperate-or-defect combination and how a correlation q between the twins shifts the expected value of cooperating.

```
