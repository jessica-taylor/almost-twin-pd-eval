# 009_edt_wikipedia_anthropic_claude-opus-5.5_rhigh_phigh / 00018

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/41dc6b66-5fa6-48a4-8281-5c66bddb9a16/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/41dc6b66-5fa6-48a4-8281-5c66bddb9a16/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Choosing the Best News

## 1. The slogan and the idea

Evidential decision theory (EDT) answers the question "what should I do?" with a single instruction: *do what you would most like to learn that you will do.* Picture yourself as a spectator who is about to be told which act you chose. Each possible announcement would change your expectations about the world. EDT ranks acts by how good those revised expectations are, a quantity often called the act's **news value**, and tells you to pick the act with the best news.

For most ordinary choices this is the same as choosing the act that produces the best results. Learning that I took my umbrella is good news about whether I stay dry, and it is good news because taking the umbrella keeps me dry. The theory becomes interesting, and controversial, when an act is evidence about outcomes it does not cause. Newcomb's problem, the twin prisoner's dilemma and "medical" cases such as the smoking lesion all have this feature. In these cases EDT parts ways with its main rival, causal decision theory (CDT), which ranks acts by what they bring about.

The rest of the essay states the theory formally, shows how it handles dependencies and counterfactuals, works through the standard examples, and then addresses the questions the theory leaves open.

**A note on sources.** The reference article (Wikipedia's entry on EDT) supplies:

- the slogan;
- the Gibbard–Harper formulas;
- the Newcomb and twin-dilemma calculations;
- the Sleeping Beauty remark;
- the "evidentialist's wager";
- the criticisms by Lewis and Joyce.

The following are my own additions or reconstructions from the wider literature, and I flag them as such where they appear:

- the parameterised versions of the examples;
- the partition-invariance point;
- the smoking-lesion analysis and the tickle defence;
- the treatment of zero-probability acts;
- the act/policy distinction;
- the closing procedure.

## 2. Formal statement

### 2.1 The basic formula

Fix an agent with a credence function $P$ over propositions, a finite set of available acts $\mathcal{A} = \{A_1,\dots,A_n\}$, and a partition of outcomes $\{O_j\}$. Each outcome carries a desirability $D(O_j)$. Following Gibbard and Harper (1976), the reference article defines the evidential expected utility of an act as

$$
V(A) \;=\; \sum_j P(O_j \mid A)\, D(O_j).
$$

EDT says to choose $A^\* \in \arg\max_{A\in\mathcal A} V(A)$.

The causal alternative, also from Gibbard and Harper, replaces the conditional probability with the probability of a counterfactual:

$$
U(A) \;=\; \sum_j P(A \mathrel{\Box\!\!\rightarrow} O_j)\, D(O_j).
$$

Here $P(A \mathrel{\Box\!\!\rightarrow} O_j)$ is the probability that $O_j$ *would* obtain *if* $A$ were performed. The two formulas give different verdicts exactly when $P(O_j\mid A)$ and $P(A\mathrel{\Box\!\!\rightarrow}O_j)$ come apart.

### 2.2 A state-based form that makes the difference visible

It is often convenient to split the world into **states** $S_k$ (facts the agent is uncertain about) and to write outcomes as act–state pairs. EDT then reads

$$
V(A) = \sum_k P(S_k \mid A)\, D(A \wedge S_k).
$$

Suppose the states are causally independent of the act: the predictor's choice, the twin's choice, or the presence of a gene. In that case the counterfactual probabilities collapse to unconditional ones, $P(A\mathrel{\Box\!\!\rightarrow} S_k) = P(S_k)$, and the CDT value is

$$
U(A) = \sum_k P(S_k)\, D(A\wedge S_k).
$$

Subtracting gives an identity I find clarifying (my formulation, not the source's):

$$
V(A) - U(A) \;=\; \sum_k \big[P(S_k\mid A) - P(S_k)\big]\, D(A\wedge S_k).
$$

The whole disagreement between the theories lives in the bracketed terms. These terms measure how much the act is *evidence* about states it does not influence. If acts are probabilistically independent of causally independent states, the two theories agree.

### 2.3 Partition invariance (an addition)

Richard Jeffrey's version of the theory, which EDT descends from, defines $V$ for any proposition $X$ with $P(X)>0$. It satisfies, for *every* partition $\{S_i\}$,

$$
V(X) = \sum_i P(S_i\mid X)\, V(X\wedge S_i).
$$

The proof is the law of total expectation applied to desirability under the conditional measure $P(\cdot\mid X)$.

The practical consequence is that the EDT analyst never has to find the "right" way to carve the world into states. Any partition yields the same $V(A)$. By contrast, CDT's simple formula $\sum_k P(S_k)D(A\wedge S_k)$ is only correct when the $S_k$ are causally independent of the acts. That makes CDT's answers depend on causal knowledge that EDT does not need.

This is a real methodological advantage of EDT. It is also exactly what its critics object to: EDT is deliberately blind to the difference between causal and merely correlational structure.

## 3. How EDT treats dependencies and counterfactuals

Three points capture EDT's attitude.

1. **All probabilistic dependence counts.** The question EDT asks is "conditional on my doing $A$, how likely is $O$?" It does not ask *why* $A$ and $O$ are correlated. The link can be causal (my act produces $O$), a common cause (a gene disposes me to $A$ and also produces $O$), or a shared algorithm (my twin runs the same reasoning). Each kind of dependence enters $V(A)$ in exactly the same way.

2. **No counterfactual operator.** EDT reads "what if I do $A$?" *indicatively*: suppose I learn that I do $A$. It does not read it *subjunctively*, as "were I to do $A$, holding fixed what is causally upstream". The theory therefore needs no semantics for counterfactuals, no causal graph, and no "intervention" operation. This is a parsimony claim in EDT's favour. The cost is that EDT can count correlations that the agent, on reflection, may judge irrelevant to choice.

3. **Dominance is not sacred.** Suppose act $A$ yields a better outcome than $B$ in every state. CDT, given causally independent states, must prefer $A$. EDT need not. If $A$ makes bad states more likely, $V(A)$ can be lower even though $A$ wins state by state. EDT respects dominance only when states are probabilistically independent of acts.

## 4. Worked examples

### 4.1 Newcomb's problem

The setup in the reference article is as follows.

- Box A is transparent and contains \$1,000.
- Box B is opaque. A predictor has filled it with \$1,000,000 if it predicted the player would take only B, and has left it empty otherwise.
- The predictor is 99% accurate.

The article's calculation is

$$
\begin{aligned}
V(\text{one-box}) &= 0.99(1{,}000{,}000) + 0.01(0) = 990{,}000,\\
V(\text{two-box}) &= 0.01(1{,}001{,}000) + 0.99(1{,}000) = 11{,}000.
\end{aligned}
$$

So EDT one-boxes. CDT two-boxes. The prediction is already fixed, so taking box A adds \$1,000 whatever B contains. That is a dominance argument, and as §3 explained, EDT rejects dominance here.

**Generalising (my addition).** Let the predictor's accuracy be $p$ regardless of which act you choose. Then

$$
V(\text{one}) = 10^6 p, \qquad V(\text{two}) = (1-p)(1{,}001{,}000) + p(1{,}000) = 1{,}001{,}000 - 10^6 p.
$$

EDT prefers one-boxing iff $2\times 10^6 p > 1{,}001{,}000$, that is, iff $p > 0.5005$.

So the predictor need not be uncanny. It only has to beat a coin by a twentieth of a percentage point. This shows how sensitive EDT's verdict is to even weak correlation when the stakes are lopsided.

### 4.2 The twin prisoner's dilemma

Aomame plays a one-shot prisoner's dilemma against a psychological twin who reasons exactly as she does. The payoffs to Aomame are:

| | Twin cooperates | Twin defects |
|---|---|---|
| Aomame cooperates | \$5 | \$0 |
| Aomame defects | \$10 | \$1 |

The reference article assumes perfect correlation, $P(\text{twin } C\mid C)=1$ and $P(\text{twin } C\mid D)=0$. That gives $V(C)=5$ and $V(D)=1$, so EDT cooperates.

**Generalising (my addition).** Write $q = P(\text{twin }C\mid \text{Aomame }C)$ and $r = P(\text{twin }C\mid \text{Aomame }D)$. Then

$$
V(C) = 5q,\qquad V(D) = 10r + (1-r)\cdot 1 = 1 + 9r.
$$

EDT cooperates iff $5q > 1 + 9r$. Two special cases are worth noting.

- **No correlation.** If Aomame's act carries no evidence about the twin ($q=r$), the condition becomes $5q > 1+9q$, which never holds. EDT defects, just like CDT.
- **Symmetric correlation.** Suppose $q = 1-r = c$, where $c$ is the probability that the twin matches her. Then the condition is $5c > 1 + 9(1-c)$, so $c > 5/7 \approx 0.714$.

The theory therefore does not "just say cooperate". It says cooperate *when you have enough evidence that your choice and your counterpart's choice are aligned*. This is the decision-theoretic core of Hofstadter's "superrationality", which the reference article lists as a related topic.

### 4.3 The smoking lesion (my addition; the standard objection)

The reference article does not discuss this case. Any account that lets a reader decide unfamiliar cases needs it, though, because it is the main motivation for CDT.

The story: a lesion $L$ causes both a taste for smoking and cancer. Smoking itself is harmless and pleasant. Suppose:

- $P(L)=0.2$;
- $P(\text{smoke}\mid L)=0.8$ and $P(\text{smoke}\mid\neg L)=0.2$;
- cancer occurs iff $L$;
- $D(\text{cancer})=-100$ and $D(\text{smoking pleasure})=+10$.

Bayes' rule gives $P(L\mid S)=0.16/0.32=0.5$ and $P(L\mid\neg S)=0.04/0.68\approx 0.059$. The naive EDT values are

$$
V(S) = 10 - 100(0.5) = -40,\qquad V(\neg S) = -100(0.059)\approx -5.9.
$$

So naive EDT abstains. CDT holds $P(L)=0.2$ fixed and computes $U(S) = 10-20 = -10$ against $U(\neg S) = -20$, so it smokes.

Most people judge that abstaining here is absurd: it avoids *news* of cancer, not cancer. This is the case behind David Lewis's charge that EDT endorses "an irrational policy of managing the news". It also illustrates James Joyce's dictum, quoted in the reference article, that rational agents choose acts for their "causal efficacy, not their auspiciousness".

**The tickle defence.** Evidentialists (notably Eells, and Ahmed in a refined form) reply that the calculation above conditions on too little. The lesion can only influence the choice *through* something in the agent: a desire, a felt urge, a "tickle" $T$. A deliberating agent who knows her own desires should condition on them.

Suppose that, given $T$, the act carries no further information about $L$: $P(L\mid S,T)=P(L\mid T)$. Then

$$
V(S\mid T) - V(\neg S\mid T) = 10 > 0,
$$

and EDT smokes.

The general lesson is a **screening-off principle**. If every channel from a common cause to your act runs through evidence you already possess, conditioning on that evidence removes the spurious correlation. EDT and CDT then agree.

Newcomb's problem and the twin case differ because the correlation is meant to survive full introspection. The predictor tracks your *decision procedure itself*, not some prior symptom you could observe.

## 5. Open questions and operational proposals

The reference article gives the formula but not the conditions under which it is well defined or uniquely applicable. Four gaps matter in practice.

### 5.1 Which probabilities?

$P$ is the agent's *own* credence at the time of deliberation, *including* everything she knows about herself (§4.3).

**Operational proposal.** Before computing $V$, list every piece of introspective and environmental evidence the agent has. Condition on all of it. Then ask whether the act carries residual information about payoff-relevant states.

If the answer is "no", EDT reduces to ordinary expected utility with act-independent states. If the answer is "yes", the residual correlation should be justified by a concrete mechanism, such as a predictor modelling the decision procedure or a twin sharing it. It should not rest on mere population statistics that the agent's self-knowledge has already screened off.

### 5.2 Acts of zero probability

$P(O\mid A) = P(O\wedge A)/P(A)$ is undefined if $P(A)=0$. That is awkward for an agent who is already confident she will not take some act, and for an ideally predictable agent.

**Operational proposal.** Treat deliberation as a state in which every available act has positive credence. Alternatively, take conditional credences $P(\cdot\mid A)$ as primitive, as in a Popper function. Then define them as limits of conditionals under small "trembles" in which the act is chosen by mistake.

The choice is substantive. If the agent would only take $A$ by error, then $P(\cdot\mid A)$ describes *what errors look like*, not what deliberate choice looks like. Analysts should state which reading they adopt.

### 5.3 Acts or policies?

The reference article evaluates single acts. Consider instead the **transparent Newcomb problem** (my example). Box B is visible. The predictor fills it iff it predicts you will one-box *upon seeing it full*.

Suppose you see \$1,000,000 in B. Act-level EDT conditions on that observation, so $P(\text{full}\mid A)=1$ for both acts. It computes $V(\text{two}) = 1{,}001{,}000 > V(\text{one}) = 1{,}000{,}000$ and two-boxes.

Now evaluate *policies* (maps from observations to acts) from the standpoint before observation, with accuracy $p$:

- "one-box if full" has value $\approx 10^6 p$;
- "always two-box" has value $\approx 1{,}000 + 10^6(1-p)$.

The first is far better when $p$ is high, so policy-level EDT one-boxes even after seeing the money.

These are different theories. "Updateless" or policy-selection variants evaluate $V(\pi) = \sum_j P(O_j\mid \pi)D(O_j)$ over policies $\pi$. Standard Jeffrey-style EDT, which is what the source describes, updates first and then evaluates acts.

**Recommendation.** When a predictor or correlated agent responds to your *policy*, say explicitly which level you are using. A good default is to report the act-level verdict as "EDT" and to note any divergence from the policy-level verdict.

### 5.4 Self-locating and multi-agent cases

The reference article reports that EDT has been invoked in the Sleeping Beauty problem. The motivating claim is that a "halfer" Beauty, with credence $1/2$ in heads on waking, can escape Dutch books by evaluating bets evidentially. Because her choices at different awakenings are perfectly correlated, a single decision effectively places the bet on every awakening.

The article also reports that Conitzer (2015) argues halfers remain Dutch-bookable even with EDT. The lesson I draw is cautious. When one's choice is correlated with copies of oneself, EDT automatically aggregates over them. Whether this repairs the pairing of credence and choice depends on how the self-locating credences were set, and the question is not settled.

The same aggregation underwrites the next argument.

## 6. A supporting argument: the evidentialist's wager

The reference article cites MacAskill and coauthors (2021) for the claim that one should *act* as if EDT were true even with only modest credence in it.

Here is a stylised version of the argument (my formalisation). Suppose your decision procedure is correlated with that of $N$ other agents, and each agent's choice produces value $u$ when made well. CDT counts only your own causal contribution, so the stakes it sees are of order $u$. EDT counts the evidence your choice gives about all $N$ correlated choices, so the stakes it sees are of order $Nu$.

Now let $c$ be your credence in EDT and $1-c$ your credence in CDT. A natural rule for acting under moral or decision-theoretic uncertainty weighs each theory by credence times stakes. Under that rule EDT's recommendation dominates whenever $cN \gg 1-c$.

The argument assumes that values from rival decision theories can be compared on a common scale, and that assumption is itself contestable. Still, the structure shows why evidential considerations can loom large in a world with many similar reasoners.

## 7. The case against, restated

The two criticisms quoted in the reference article sharpen into a single complaint. EDT confuses *learning* that the world is good with *making* it good.

On the critics' view, the one-boxer's millions come from having been the kind of agent the predictor rewards. The choice itself, made once the box is filled, cannot alter what is in it. Taking the extra \$1,000 is therefore strictly better in every way the world could actually be.

Evidentialists reply in three ways.

- **"Why ain'cha rich?"** In Newcomb populations, one-boxers systematically walk away with more money. A decision theory that predictably leaves its followers poorer needs an explanation.
- **The tickle defence.** It neutralises the smoking-lesion style counterexamples that look most damaging (§4.3).
- **Costly metaphysics.** CDT relies on counterfactuals and causal structure, which EDT does not need (§3).

The dispute is therefore not a calculation error on either side. It is a disagreement about what the decision-relevant probability is: indicative conditioning or causal supposition.

## 8. A procedure for unfamiliar cases

Collecting the above, here is how to apply EDT to a new problem. The steps are my synthesis, not the source's.

1. **Enumerate acts** (or policies, stating which; see §5.3) and a payoff-relevant partition of states or outcomes. Any partition will do (§2.3).
2. **Condition on total evidence**, including introspective evidence about your own desires and reasoning (§5.1).
3. **Assess residual dependence.** For each act $A$ and state $S$, estimate $P(S\mid A)$. Ask whether any mechanism makes the act informative beyond step 2: a predictor modelling your procedure, an agent sharing your algorithm, or copies of you.
4. **Compute** $V(A)=\sum_k P(S_k\mid A)D(A\wedge S_k)$ and choose the maximiser.
5. **Diagnose.** Compute the gap $V(A)-U(A)=\sum_k[P(S_k\mid A)-P(S_k)]D(A\wedge S_k)$ from §2.2.
   - If it is zero, EDT and CDT agree and the case is uncontroversial.
   - If it is nonzero, identify the non-causal correlation driving it and report it explicitly. This is where readers will disagree.
6. **Check thresholds.** As in §4.1–4.2, find the correlation level at which the verdict flips. Verdicts that need near-perfect correlation are more fragile than those that need only slight correlation.

## 9. Conclusion

EDT is ordinary expected-utility maximisation in which acts are treated like any other proposition. You evaluate an act by conditioning on it, exactly as you would evaluate the news that it occurred.

This gives the theory its simplicity: there are no counterfactuals, no causal graphs, and its values are invariant under any choice of partition. It also gives the theory its distinctive verdicts:

- one-boxing in Newcomb's problem (for any predictor accuracy above about 50.05%);
- cooperation with a sufficiently similar twin;
- automatic aggregation over correlated decision-makers.

The price is sensitivity to correlations that do not reflect influence. The smoking lesion makes that price vivid. The tickle defence answers it whenever the spurious correlation runs through what the agent already knows, but not when the correlation is tied to the decision procedure itself.

Whether that residual sensitivity is a bug ("managing the news") or a feature ("why ain'cha rich?") is the live philosophical question. To apply EDT responsibly, condition on everything you know, make the remaining evidential dependence explicit, state whether you are choosing acts or policies, and say what correlation your verdict depends on.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9).
- Gibbard, A. & Harper, W. (1976). "Counterfactuals and Two Kinds of Expected Utility."
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59(1).
- MacAskill, W., Vallinder, A., Oesterheld, C., Shulman, C., Treutlein, J. (2021). "The Evidentialist's Wager."
- Wikipedia contributors, "Evidential decision theory," revision 1373679688 (CC BY-SA 4.0).
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm sketching a mathematical essay on evidential decision theory, around 2400 to 3000 words, and I need to keep my own additions separate from what the sources claim. The outline covers the news-value definition, the formula, the contrast with causal decision theory, Newcomb's problem, the twin prisoner's dilemma, the Sleeping Beauty mention, and the criticisms from Lewis and Joyce, and I'm still working out which probabilities the agent's credences about their own actions should be.

I'm working through the essay's remaining sections: whether conditioning on an act with zero probability causes trouble, the partition-invariance property of Jeffrey's framework, the smoking lesion and tickle defense, policies versus single acts, and the operational reading. I'm also noting that EDT relies on conditional credences rather than counterfactuals, so any probabilistic dependence counts.

I'm checking how EDT handles dependencies in general, not just causal ones, and working through Newcomb's problem with an accuracy parameter p: one-boxing comes out ahead once p exceeds about 0.5005. I'm also setting up the twin prisoner's dilemma with conditional probabilities for the correlation between the two players' choices.

I'm working through the twin prisoner's dilemma's cooperation condition and then moving on to the hard cases: the smoking lesion and medical Newcomb problems, where I'm weighing the tickle defense and how screening off might apply. I'm also starting on zero-probability acts, where conditional probabilities are undefined, and considering whether a Popper function or a limit of trembling hands could handle them.

I'm now weighing how transparent Newcomb cases and counterfactual mugging split act-level from policy-level evaluation, since once the agent sees the box contents, conditioning on the act may no longer track the predictor's state.

I'm checking the Sleeping Beauty note: the claim is that EDT helps halfers avoid Dutch books, but Conitzer may have argued that even EDT halfers can be Dutch-booked. I want to be careful not to overstate the details of that debate, since I'm recalling it from memory.

I'm now checking the Dutch book claim on Sleeping Beauty: the source says Conitzer constructs a book against EDT agents, whether they are halfers or thirders, because their choices at different awakenings are correlated and EDT counts them together. I'll keep that point brief.

I'm turning to the wager argument for evidentialists, which says that if many agents share a correlated disposition, the stakes of choosing EDT versus CDT grow with the number of correlated agents. I'll then take up the Lewis and Joyce criticisms, using the smoking lesion case to show how managing the news works, before I lay out a step-by-step recipe for unfamiliar cases.

Now I'm working through the smoking lesion numbers: with the lesion's probability conditioned on smoking, the expected value of smoking comes out at -40 against -5.88 for abstaining, so naive EDT says not to smoke. Under CDT, using the unconditional lesion probability instead, smoking scores -10 and abstaining -20, so it recommends smoking.

I'm now setting out the transparent Newcomb case, where the predictor fills the opaque box only if it expects a one-box choice when the box is seen to be full. Once the agent sees it full, standard evidential decision theory conditions on that fact and two-boxes, while a policy-level evaluation still one-boxes, so the two versions come apart.

I'm now looking at how Jeffrey's value formula handles zero-probability acts and whether the choice of partition matters, and I'm weighing whether to take a positive credence during deliberation, use a Popper function, or treat the conditional credence as primitive.

I'm weighing how to organize the partition-invariance argument and the point that EDT avoids needing to identify the causal structure, which I'm treating as my own addition to the essay.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/7f9dc3d5-ba5f-4d17-9547-bef709429545/call_0/request.json)

[Authoritative raw response](../../../../../../runs/7f9dc3d5-ba5f-4d17-9547-bef709429545/call_0/response.raw) · finish: `content_filter`

### Visible response

No text returned.

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm setting up the twin prisoner's dilemma under evidential decision theory, working out the expected values of cooperating versus defecting given a correlation c between the twins' choices. Cooperating comes out to 3c - 5, and defecting to 4(1 - c) - 4.

I'm checking whether the correlation clears the 5/7 threshold, and since the two twins are reasoning the same way with the same model and essay, a high correlation seems very likely, around 0.71 or above. That means cooperating is the right choice here, so I'll pass. It's a fictional game anyway.

```
