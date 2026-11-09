# Evidential Decision Theory: Choosing the Action You Would Most Like to Hear About

## 1. The slogan and the idea

Evidential decision theory (EDT) answers the question "what should I do?" with an unusual instruction:

> **Do what you would most want to learn that you will do.**

The reference article attributes this slogan to Arif Ahmed's *Evidential Decision Theory* (2021). It says EDT selects the action with the highest **news value**: the action that, if you received the "news" that you had taken it, would indicate the best outcome in expectation.

In most everyday cases this is unremarkable. Learning that I took my umbrella is good news about whether I will stay dry, because taking the umbrella *causes* me to stay dry. The theory becomes philosophically interesting when an action is evidence about good or bad outcomes that it does not cause. A predictor might have anticipated my choice. A twin might reason exactly as I do. A gene might influence both my behaviour and my health.

EDT treats such evidential connections as relevant to choice. Its main rival, **causal decision theory** (CDT), treats them as irrelevant. This essay does four things:

1. It sets out the formal theory.
2. It works through the standard test cases.
3. It identifies questions the source leaves open, and proposes an operational reading where one seems reasonable.
4. It surveys the main arguments for and against EDT.

Throughout, I mark which claims come from the reference article and which are my own additions.

## 2. The formal framework

### 2.1 News value

Following Gibbard and Harper (1976), the source writes EDT's evaluation of an act $A$ as

$$
V(A) \;=\; \sum_j P(O_j \mid A)\, D(O_j),
$$

where:

- $\{O_j\}$ is a set of mutually exclusive, jointly exhaustive outcomes;
- $D(O_j)$ is the desirability of outcome $O_j$;
- $P(O_j \mid A)$ is the agent's ordinary conditional probability of $O_j$ given that $A$ is performed.

The only change from textbook expected utility is that outcome probabilities are *conditioned on the act*. EDT applies the standard ratio definition $P(O\mid A)=P(O\wedge A)/P(A)$ to the proposition that one performs $A$.

**Decision rule.** Choose $A^* \in \arg\max_A V(A)$.

### 2.2 Why this is natural: Jeffrey's framework

The following background is mine, not the source's. The formula is the core of Richard Jeffrey's *The Logic of Decision* (1965).

In Jeffrey's framework, acts, states and outcomes are all *propositions* in a single algebra. Every non-null proposition $X$ gets a desirability, defined as the conditional expectation of utility over the possible worlds $w$ where $X$ is true:

$$
V(X) = \sum_{w} P(w \mid X)\, u(w).
$$

An act is just a proposition the agent can make true. Two features follow.

- **Partition invariance.** For any partition $\{O_j\}$, the identity $V(A)=\sum_j P(O_j\mid A)\,V(O_j \wedge A)$ holds. It is just the law of total expectation. You can therefore compute news value using coarse or fine outcome descriptions and always get the same answer, *provided* $D(O_j)$ is understood as $V(O_j\wedge A)$. In other words, each outcome must be described finely enough that its desirability does not depend further on which act produced it.

  Savage-style theories lack this property. They require a partition of "states" that are probabilistically independent of the acts. EDT imposes no such requirement, so it never needs to search for the "right" partition.

- **Agreement in ordinary cases.** Suppose the outcome-relevant states $S$ are probabilistically independent of the act, so $P(S\mid A)=P(S)$. Then $V(A)=\sum_S P(S)\,u(A,S)$, which is exactly Savage's expected utility. CDT gives the same verdict. EDT and CDT can diverge *only* when the act is correlated with states it does not control.

### 2.3 The causal alternative

The source contrasts $V$ with the counterfactual expected utility of CDT:

$$
U(A) = \sum_j P(A \mathrel{\Box\!\!\rightarrow} O_j)\, D(O_j),
$$

where $P(A \mathrel{\Box\!\!\rightarrow} O_j)$ is the probability that $O_j$ *would* obtain if $A$ were performed. Since $P(O_j\mid A)$ and $P(A\mathrel{\Box\!\!\rightarrow} O_j)$ need not coincide, the theories can disagree.

In modern causal-model notation (my gloss, following Pearl), the contrast is between two quantities:

- **Observing the act:** $P(O \mid A)$. This is what EDT uses.
- **Intervening on it:** $P(O \mid \mathrm{do}(A))$. This is a common way of making CDT precise.

The two coincide when no "back-door" path connects the act to the outcome, that is, when every dependence between $A$ and $O$ runs through $A$'s causal effects. Every disagreement between the theories is a case with a common cause, or a correlated copy, sitting behind the act.

## 3. Worked examples

### 3.1 Newcomb's problem

The setup, as given in the source:

- Box A is transparent and contains \$1,000.
- Box B is opaque. It contains \$1,000,000 if a predictor (99% accurate) foresaw that you would take only B, and nothing if it foresaw that you would take both.
- You must choose between taking only B and taking both boxes.

The source computes:

$$
\begin{aligned}
V(\text{one-box}) &= 0.99\times \$1{,}000{,}000 + 0.01\times \$0 = \$990{,}000,\\
V(\text{two-box}) &= 0.01\times \$1{,}001{,}000 + 0.99\times \$1{,}000 = \$11{,}000.
\end{aligned}
$$

EDT therefore recommends one-boxing. Taking one box is strong evidence that the million is there.

CDT reasons differently. The prediction has already been made, so whatever is in box B, taking both boxes yields \$1,000 more. CDT therefore two-boxes.

**How much accuracy does EDT need?** This generalisation is mine. Let $p$ be the probability that the predictor is right about whichever act you perform. Then

$$
V(\text{one}) = 10^6 p,\qquad V(\text{two}) = 10^6(1-p) + 10^3 .
$$

One-boxing wins if and only if $2p-1 > 10^{-3}$, that is, $p > 0.5005$.

EDT's verdict is therefore not an artefact of an extreme 99% predictor. A predictor that is barely better than chance suffices, given these stakes. The verdict depends only on the *correlation* between act and prediction. It does not matter whether the predictor is a superintelligence or a psychologist who is right 51% of the time.

### 3.2 The twin prisoner's dilemma

The setup, from the source:

- Aomame and her psychological twin are in separate rooms and cannot communicate.
- Both cooperate: each gets \$5. Both defect: each gets \$1.
- One cooperates and the other defects: the defector gets \$10 and the cooperator gets \$0.
- Aomame cares only about her own payout.

The source assumes perfect correlation. The twin's choice matches hers with probability 1. Then $V(C)=\$5$ and $V(D)=\$1$, so EDT recommends cooperating.

CDT notes that defection dominates: whatever the twin does, defecting pays more, and Aomame's choice cannot causally affect her twin. CDT therefore defects.

**Imperfect correlation.** Again the generalisation is mine. Let $P(\text{twin } C\mid C)=q$ and $P(\text{twin } C\mid D)=r$. Then

$$
V(C) = 5q,\qquad V(D) = 10r + (1-r) = 1 + 9r.
$$

With symmetric reliability, $q=p$ and $r=1-p$. Cooperation is then optimal if and only if $5p > 10-9p$, that is, $p>5/7\approx 0.714$.

This is the decision-theoretic core of Hofstadter's "superrationality," which the source lists as a related concept. Agents who know they reason alike treat their choices as evidence about each other's, and so cooperate.

### 3.3 The smoking lesion, and screening off

The source does not discuss this case, but no account of EDT is complete without it.

Suppose a gene causes both a desire to smoke and lung cancer, and smoking itself is harmless. Smoking is then correlated with cancer, so $P(\text{cancer}\mid \text{smoke}) > P(\text{cancer}\mid\neg\text{smoke})$. A naive application of EDT says: don't smoke, because smoking is bad news. Almost everyone, including most evidentialists, finds this absurd. Abstaining is purely "managing the news."

The standard evidentialist reply is the **tickle defence** (Eells 1982; see also Ahmed 2014). It runs as follows:

1. The lesion can influence the decision only through something the agent can introspect: a desire, a "tickle" $T$.
2. A decision is made on the basis of the agent's total evidence, which includes $T$.
3. The relevant probabilities are therefore $P(\cdot\mid A, T)$, not $P(\cdot \mid A)$.
4. If the lesion affects action *only* via $T$, then $T$ **screens off** the act from the lesion:
$$
P(\text{cancer}\mid \text{smoke}, T) = P(\text{cancer}\mid T) = P(\text{cancer}\mid \neg\text{smoke}, T).
$$
5. Conditional on what the agent already knows, smoking is no longer evidence of cancer. EDT then smokes, as it should.

The general principle is this:

> **EDT and CDT agree whenever the agent's evidence screens off the act from every non-effect it is correlated with.**

Newcomb's problem and the twin case resist this treatment. There, the correlation runs through the agent's *reasoning itself*, not through some prior symptom. Knowing my desires does not tell me what my deliberation will output, and the predictor or twin tracks that output. This explains why evidentialists can accept smoking while still one-boxing, without inconsistency.

## 4. Open questions and an operational reading

The source states the formula but leaves several things unspecified that you need before applying it to unfamiliar cases. Below I identify four gaps and propose how to fill each. These proposals are mine, though each follows a reasonably established line in the literature.

### 4.1 Whose probabilities, and when?

$P$ should be the agent's credence **at the moment of decision, conditioned on all evidence then available**. That includes evidence about her own mental states, as the tickle defence requires.

This blocks the cheapest objections, such as the smoking lesion. It also keeps the theory's distinctive verdicts where the correlation genuinely passes through the decision procedure.

### 4.2 Conditioning on acts you are sure you won't take

$P(O\mid A)$ is undefined when $P(A)=0$. It is unstable when $P(A)$ is tiny, which may happen near the end of deliberation, once the agent is nearly sure what she will do. The source is silent on this.

Three operational fixes are available:

- **Primitive conditional probabilities.** Treat $P(\cdot\mid A)$ as primitive (Popper/Rényi functions), so that it is defined even when $P(A)=0$.
- **Trembles.** Evaluate $V$ as the limit as $\varepsilon\to 0$ under a model in which each act is performed with probability at least $\varepsilon$ by "mistake." One must then specify what the tremble correlates with. The cleanest choice is that the tremble is independent of everything except the act itself.
- **Pre-deliberative credences.** Compute $V$ using credences held *before* the agent has settled her choice, while every act is still a live option.

I recommend the third as the default and the second as a check. In the examples above, all three give the same answers.

### 4.3 Acts or policies?

In dynamic problems the agent may observe something before acting. Two readings of EDT then come apart:

- **Act-level EDT:** after observing $e$, choose $A$ to maximise $\sum_j P(O_j\mid A, e)D(O_j)$.
- **Policy-level EDT:** before observing anything, choose a policy $\pi:\{e\}\to\{A\}$ that maximises $\sum_j P(O_j\mid \pi)D(O_j)$, and then follow it.

The two diverge in cases such as **transparent Newcomb**, where you can see that box B is full before choosing.

- Act-level EDT conditions on the full box. Your act is no longer evidence about the box's contents, so it two-boxes.
- Policy-level EDT notes that the predictor fills the box only for agents whose *policy* is "one-box even upon seeing it full," and so it one-boxes.

The source's formulation is act-level. Policy-level ("updateless") variants are a substantive extension. They gain dynamic consistency, in the sense that the agent never wishes beforehand to bind her future self. The price is departing from conditioning on all current evidence.

When applying EDT, state explicitly which version you mean. I would use act-level EDT as the default reading of "EDT" and flag policy-level verdicts separately.

### 4.4 Outcome descriptions

As noted in §2.2, $D(O_j)$ must not depend on which act produced $O_j$. If it does, refine the partition, for example by distinguishing "\$1,000 by taking both boxes" from "\$1,000 by taking one box." Once outcomes are described this finely, the choice of partition makes no difference.

### 4.5 A procedure for unfamiliar cases

Putting these together:

1. List the acts and a sufficiently fine outcome partition. Assign $D$.
2. Build a joint credence over acts, outcomes and the relevant hidden variables, such as predictions, twins' choices and genes. Condition on all evidence you have at decision time, including introspective evidence.
3. For each act $A$, compute $P(O_j\mid A)$ in that model. Any correlations that survive the conditioning in step 2 count fully.
4. Choose the act with the highest $V(A)$. In sequential problems, say whether you are applying act-level or policy-level EDT.
5. Diagnostic: also compute CDT's $U(A)$. If $U$ and $V$ disagree, find the back-door correlation responsible. That correlation is exactly the feature of the case on which the two theories' philosophical disagreement rests.

## 5. Sleeping Beauty and Dutch books

The source reports two claims:

- EDT has been invoked in the Sleeping Beauty problem to protect "halfers," who assign credence $1/2$ to Heads on waking, against Dutch books.
- Conitzer (2015) argues that halfers who adopt EDT remain Dutch-bookable.

Here is my sketch of why EDT might help.

**The setup.** Beauty is woken once if the coin lands Heads, and twice (with memory erasure between wakings) if it lands Tails. At each waking she is offered a ticket costing $c$ that pays \$1 if Tails.

**The halfer's EDT calculation.** Her two Tails-wakings are subjectively identical, so her decision at one waking is perfect evidence of her decision at the other. Buying is therefore evidence that she buys twice if Tails. With credence $1/2$ in Heads, and caring about total winnings,

$$
V(\text{buy}) = \tfrac12(-c) + \tfrac12\cdot 2(1-c) = 1 - \tfrac32 c,
$$

so she buys if and only if $c<2/3$.

**Comparison.** Consider a "thirder" who uses CDT, treating each waking's bet in isolation with $P(\text{Tails})=2/3$. That agent sets the same threshold. So does Beauty planning on Sunday, before the experiment begins. Because her betting behaviour agrees with her ex ante plan, the simplest Dutch book against halfing disappears.

This pairing result is often associated with Briggs (2010): halfing pairs coherently with EDT, and thirding with CDT.

Conitzer's paper constructs a more elaborate betting scenario in which EDT halfers still accept a sure loss. The source reports this argument without adjudicating it, and I will not either. The episode illustrates a broader point: one's theory of rational choice and one's theory of self-locating credence cannot be assessed independently.

## 6. The evidentialist's wager

The source mentions an argument by MacAskill, Vallinder, Oesterheld, Shulman and Treutlein (2021): even if you have less credence in EDT than in CDT, you may have reason to *act as if* EDT were true. The reason is that EDT counts the choices of all agents correlated with you.

Here is a stylised version, with my notation. Suppose $N$ agents' decisions are correlated with yours, each producing value $\Delta$ by taking some act.

- By CDT's lights, the stakes of your choice are about $\Delta$, since you control only yourself.
- By EDT's lights, they are about $N\Delta$, since your choice is evidence about all $N$ choices.

Let $c$ be your credence in EDT. Under an expected-choiceworthiness rule for moral or decision-theoretic uncertainty, you would weigh $c\cdot N\Delta$ against $(1-c)\cdot\Delta$. When $N$ is large, the evidential term dominates even for small $c$.

Whether choiceworthiness can be compared across theories in this way is itself contested. The argument needs that assumption, and it is the natural point at which to resist it.

## 7. Criticisms and replies

### 7.1 "Managing the news"

The source quotes David Lewis (1981), who calls EDT "an irrational policy of managing the news." It also quotes James Joyce (1999): "Rational agents choose acts on the basis of their causal efficacy, not their auspiciousness; they act to bring about good results even when doing so might betoken bad news."

The objection is that EDT confuses *learning* that things are good with *making* them good. In Newcomb's problem the million is either there or not. One-boxing leaves you \$1,000 poorer than you could have been, *whatever the contents*. The causalist presses the dominance argument: if, for every fixed state of the world, act X does better than act Y, you should do X.

### 7.2 The evidentialist's replies

These replies go beyond the source but are standard.

- **"Why ain'cha rich?"** In repeated Newcomb trials, one-boxers walk away with about \$990,000 on average and two-boxers with about \$11,000. A theory of rational choice that predictably makes its adherents poorer needs to explain why. The causalist's answer is that the predictor rewards irrationality. Whether that answer is satisfying is the crux of the debate.
- **Dominance presupposes independence.** Dominance reasoning is valid only when the states are independent of the acts. In Newcomb's problem they are not *probabilistically* independent, even though they are causally independent. Insisting on dominance therefore assumes CDT; it does not argue for it.
- **The cost of CDT's metaphysics.** CDT needs counterfactuals or interventions, which are additional and contested structure. EDT needs only a credence function and Bayesian conditioning.
- **Defusing the hard cases.** The cases most damaging to EDT, such as the smoking lesion, are arguably defused once the agent conditions on her full introspective evidence (§3.3).

### 7.3 Residual worries

Critics have answers of their own:

- Some reply that the tickle defence fails when agents lack introspective access to their motives.
- The problem of conditioning on low-probability acts (§4.2) remains awkward.
- Act-level EDT can be dynamically inconsistent. In transparent Newcomb, an agent may wish beforehand to bind herself to a choice she will not make when the time comes.

Each of these pressures EDT toward a refined form, whether by adding conditioning on introspective evidence, adopting trembles, or moving to policy-level evaluation. None of them involves abandoning conditional probability for causal counterfactuals.

## 8. Conclusion

EDT is ordinary expected-utility maximisation with one principled choice: **the probability of an outcome given an act is the conditional probability $P(O\mid A)$**. In other words, the act is treated as a piece of evidence like any other.

- When acts are independent of everything they do not cause, EDT coincides with Savage and with CDT.
- When an act is correlated with a predictor's forecast, a twin's choice, or anything else that tracks the agent's reasoning, EDT counts that correlation. It therefore one-boxes in Newcomb's problem (whenever predictor accuracy exceeds about 50.05% at the standard stakes) and cooperates in the twin dilemma (when reliability exceeds $5/7$).

The source presents these verdicts together with the formal contrast against CDT and the "managing the news" objection. To apply EDT to unfamiliar problems, I have argued that one should also fix four things:

1. condition on all evidence at decision time, including introspective "tickles";
2. use a principled treatment of acts with near-zero probability;
3. state whether evaluation is act-level or policy-level;
4. describe outcomes finely enough that their desirability does not depend on the act that produced them.

With these settled, EDT becomes a determinate procedure. Its remaining disagreements with CDT then come down to one philosophical question: whether a rational agent should care about what her choice *indicates*, or only about what it *does*.

## References

- Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Briggs, R. (2010). "Putting a Value on Beauty." *Oxford Studies in Epistemology* 3.
- Conitzer, V. (2015). "A Dutch Book against Sleeping Beauties Who Are Evidential Decision Theorists." *Synthese* 192(9).
- Eells, E. (1982). *Rational Decision and Causality*. Cambridge University Press.
- Gibbard, A. & Harper, W. (1976). "Counterfactuals and Two Kinds of Expected Utility."
- Jeffrey, R. (1965). *The Logic of Decision*. McGraw-Hill.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1981). "Causal Decision Theory." *Australasian Journal of Philosophy* 59(1).
- MacAskill, W., Vallinder, A., Oesterheld, C., Shulman, C. & Treutlein, J. (2021). "The Evidentialist's Wager."
- Wikipedia contributors, "Evidential decision theory," revision 1373679688 (CC BY-SA 4.0).