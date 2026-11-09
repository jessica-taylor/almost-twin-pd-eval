# Evidential Decision Theory: Choosing the Act You Would Most Like to Hear About

## 1. The slogan and the idea

Suppose a friend who knows everything about your situation, but nothing about what you will decide, is about to tell you which action you took. Which report would you most like to hear? **Evidential decision theory** (EDT) says that is the action you should take. Arif Ahmed puts it as "do what you most want to learn that you will do." The reference article describes this as choosing the act with the highest *news value*: the act that, received as news, would point toward the best outcome in expectation.

This can sound like wishful thinking, and its critics say it is exactly that. The underlying intuition, though, is respectable. Your choice is an event in the world. Like any other event, it carries information about the rest of the world. EDT asks you to take that information seriously and to treat your own act as evidence. Its rival, **causal decision theory** (CDT), asks you to attend only to what your act brings about.

This essay sets out the formal machinery, works through the standard test cases, and then turns to the questions the reference article leaves open: what exactly to condition on, how to handle sequential choices, and what to do when an act has probability zero. Where I go beyond the source, I say so.

## 2. The formal definition

### 2.1 News value

Let $P$ be the agent's credence function. Let $\{O_j\}$ be a partition of possibilities into outcomes, and let $D(O_j)$ be the desirability of outcome $O_j$. Following Gibbard and Harper (1976), the reference article defines the evidential expected utility of an act $A$ as

$$
V(A) = \sum_j P(O_j \mid A)\, D(O_j).
$$

EDT recommends choosing $A^* \in \arg\max_A V(A)$. In probabilistic terms, $V(A) = \mathbb{E}[D \mid A]$, the conditional expectation of desirability given that $A$ is performed. Nothing in the definition mentions causation, mechanism, or time order. The only ingredient is ordinary conditional probability, $P(O \mid A) = P(O \wedge A)/P(A)$.

### 2.2 A requirement on outcomes (my gloss)

The formula assumes that $D(O_j)$ does not depend on which act was taken. That holds only if each outcome specifies everything the agent cares about, including any features of the act itself that matter. In the Newcomb example below, outcomes are stated as dollar totals. Those totals already build in the act, so the condition is met.

The cleanest way to secure the condition is Richard Jeffrey's: let desirability attach to maximally specific possibilities (worlds) $w$, and define

$$
V(A) = \sum_{w} P(w \mid A)\, D(w).
$$

This version has a useful property, **partition invariance**. For any partition $\{S_i\}$ of "states,"

$$
V(A) = \sum_i P(S_i \mid A)\, V(A \wedge S_i),
$$

because

$$
\sum_i P(S_i\mid A)\sum_{w \in A\wedge S_i} P(w\mid A \wedge S_i)D(w) = \sum_w P(w\mid A)D(w).
$$

So the EDT verdict does not depend on how you carve the world into states. You may use whatever partition makes the computation easy. As we will see, CDT lacks this freedom: it needs the *right* partition, one into causally independent states.

### 2.3 The contrast with CDT

The reference article gives CDT's expected utility as

$$
U(A) = \sum_j P(A \mathrel{\Box\!\!\rightarrow} O_j)\, D(O_j),
$$

where $A \mathrel{\Box\!\!\rightarrow} O_j$ is the counterfactual "if $A$ were performed, $O_j$ would obtain." Since $P(A \mathrel{\Box\!\!\rightarrow} O_j)$ and $P(O_j\mid A)$ can differ, the two theories can diverge.

A different formulation makes the contrast especially transparent. It is David Lewis's (1981), not the source's. Let $\{K\}$ be a partition into *dependency hypotheses*: states that the agent's act cannot causally influence. Then

$$
U(A) = \sum_K P(K)\, V(A\wedge K), \qquad V(A) = \sum_K P(K \mid A)\, V(A\wedge K).
$$

The entire disagreement fits in one symbol. CDT weights states by the unconditional $P(K)$, and EDT weights them by $P(K\mid A)$. Two consequences follow:

- **When acts are evidentially independent of the causally relevant states** ($P(K\mid A) = P(K)$ for all $K$, $A$), the theories agree. This covers most everyday decisions, which is why the disagreement surfaces mainly in thought experiments.
- **When acts are correlated with states they do not cause**, through a predictor, a common cause, or a psychologically similar agent, the theories can disagree.

### 2.4 How EDT treats dependence and counterfactuals

This leads to the central conceptual point. EDT does not distinguish kinds of dependence. Causal dependence ("pressing the switch makes the light come on"), common-cause correlation ("my choosing X and the predictor's forecast of X both flow from my psychology"), and similarity of reasoning ("my twin thinks as I do") all enter the calculation in the same way, through $P(\cdot\mid A)$.

Correspondingly, EDT has no separate notion of a counterfactual. It never asks what would happen if you were to do $A$, holding fixed everything not downstream of $A$. It asks only what the world is likely to be like given that you do $A$. Defenders see this as a virtue: counterfactuals and causal structure are contested metaphysical notions, and EDT needs only probability. Critics see it as the theory's defining mistake.

## 3. Worked cases

### 3.1 Newcomb's problem

A predictor fills an opaque box B with \$1,000,000 if it predicted you would take only B, and leaves it empty if it predicted you would take both boxes. Transparent box A holds \$1,000. Using the reference article's figure of 99% accuracy:

$$
\begin{aligned}
V(\text{one-box}) &= 0.99(1{,}000{,}000) + 0.01(0) = 990{,}000,\\
V(\text{two-box}) &= 0.01(1{,}001{,}000) + 0.99(1{,}000) = 11{,}000.
\end{aligned}
$$

EDT one-boxes. CDT two-boxes, because the prediction is already made and the act cannot affect it.

It helps to see how robust the EDT verdict is. Write $M = 10^6$, $T = 10^3$, and let the predictor's accuracy be $p$, assumed symmetric across the two acts. Then

$$
V(\text{one}) = pM,\qquad V(\text{two}) = (1-p)(M+T) + pT = (1-p)M + T.
$$

So EDT one-boxes iff

$$
pM > (1-p)M + T \iff p > \frac{M+T}{2M} = 0.5005.
$$

A predictor barely better than a coin flip is enough. In the Lewis form, CDT's computation gives $U(\text{two}) - U(\text{one}) = T$ for *every* credence $P(\text{full})$. Two-boxing dominates, and conditioning on the act is exactly what lets EDT escape that dominance argument.

### 3.2 The twin prisoner's dilemma

Aomame plays a one-shot prisoner's dilemma against a psychological twin who reasons as she does. The payoffs are: \$5 each for mutual cooperation, \$1 each for mutual defection, and \$10/\$0 to the defector/cooperator. The reference article assumes perfect correlation:

$$
V(C) = 1\cdot 5 + 0\cdot 0 = 5,\qquad V(D) = 0\cdot 10 + 1 \cdot 1 = 1,
$$

so EDT cooperates. Defection strictly dominates causally, so CDT defects.

The case can be generalized. Let $q = P(\text{twin } C\mid C)$ and $r = P(\text{twin } C \mid D)$. Then $V(C) = 5q$ and $V(D) = 10r + (1-r) = 1 + 9r$. If the correlation is symmetric, with $q = c$ and $r = 1-c$, cooperation wins iff

$$
5c > 1 + 9(1-c) \iff c > \tfrac{5}{7} \approx 0.714.
$$

The general lesson is that EDT's departures from CDT scale with the strength of the act–state correlation and with the stakes. A modest correlation is enough to override a modest dominance advantage.

## 4. The hard question: which conditional probabilities?

Applying EDT is "just" computing $\mathbb{E}[D\mid A]$. The real work lies in fixing $P$, and in particular deciding what the agent already knows when she conditions. The reference article does not take this up. It is, however, where most of the serious debate about EDT happens, so I develop an operational interpretation here and flag it as my own framing of a standard line of argument.

### 4.1 The smoking lesion

Suppose a genetic lesion causes both cancer and a desire to smoke, and smoking itself is harmless and pleasant. The illustrative numbers are mine:

- Smoking adds $+10$ utility; cancer costs $-1000$.
- $P(\text{cancer}\mid \text{lesion}) = 0.8$ and $P(\text{cancer}\mid \neg\text{lesion}) = 0.1$.
- In the population, $P(\text{lesion}\mid \text{smoke}) = 0.9$ and $P(\text{lesion}\mid \neg\text{smoke}) = 0.05$.

A naive EDT calculation conditions on the act using these population frequencies:

$$
\begin{aligned}
V(\text{smoke}) &= 10 - 1000(0.9\cdot 0.8 + 0.1\cdot 0.1) = -720,\\
V(\neg\text{smoke}) &= -1000(0.05\cdot 0.8 + 0.95\cdot 0.1) = -135.
\end{aligned}
$$

So the naive calculation says "don't smoke." This is widely regarded as absurd, since abstaining cannot remove a lesion. Lewis's phrase for it, quoted in the reference article, is "an irrational policy of managing the news."

### 4.2 The tickle defense, as an operational rule

In the story, the lesion influences behavior *by way of the agent's desires*. A deliberating agent typically knows her own desires: she feels the "tickle." Let $d$ be her observed motivational state. If the lesion affects the act only through $d$, then

$$
P(\text{lesion}\mid \text{smoke}, d) = P(\text{lesion}\mid d) = P(\text{lesion}\mid \neg\text{smoke}, d).
$$

Conditional on what she already knows, the act carries no further news about the lesion. Therefore $V(\text{smoke}) - V(\neg\text{smoke}) = 10$, and EDT says smoke, agreeing with CDT.

This suggests the following rule, which I recommend for deciding unfamiliar cases:

> **Total-evidence rule.** Compute $V(A) = \mathbb{E}[D\mid A, E]$, where $E$ is *everything* the agent knows at the moment of choice, including her own beliefs, desires, and the deliberative considerations available to her. Count a correlation between act and state only if it survives conditioning on $E$.

The test of whether a case is a genuine EDT/CDT divergence then becomes whether the correlation survives screening off by the agent's own evidence.

- In the **smoking lesion**, it plausibly does not, because the common cause works through accessible desires.
- In **Newcomb's problem** and the **twin dilemma**, it plausibly does. The predictor and the twin track the *outcome of deliberation itself*, not merely some input the agent can observe beforehand. Whatever you know about your inputs, your final choice still indicates what the predictor saw or what the twin concluded.

The rule is not uncontroversial. Critics construct cases where the lesion acts subconsciously, or where the agent is uncertain about her own decision procedure, and the tickle defense has to be extended in strained ways. Still, it gives a principled, checkable procedure. It also explains why sophisticated evidentialists, Ahmed (2021) among them, can claim that EDT agrees with CDT in the medical cases while diverging in Newcomb-type cases.

### 4.3 Credences about one's own acts

EDT requires $P(A) > 0$ for every option. A deliberating agent who becomes certain of what she will do can no longer evaluate the alternatives, because $P(\cdot\mid A')$ is undefined when $P(A') = 0$. Two operational responses are available, and both are my suggestions rather than claims in the source:

1. **Model-based conditionals.** Take $P(\cdot \mid A)$ from a joint model of the situation in which acts are random variables. Problem statements usually supply such a model directly, as in "the predictor is 99% accurate," which specifies $P(\text{full}\mid \text{one-box})$. The agent's possibly degenerate credence about her own choice then plays no role.
2. **Primitive conditional probabilities.** Use Popper-style conditional probability functions, where $P(\cdot\mid A)$ is defined even when $P(A) = 0$.

In practice the first response is what everyone does when computing textbook cases.

### 4.4 Acts versus policies

The reference article treats single choices, but sequential problems expose a further ambiguity. Consider **transparent Newcomb**: both boxes are visible, and the predictor filled B iff it predicted you would one-box *upon seeing B full*. Suppose you see B full. Conditional on that observation, the content of B is settled, and your act carries no further news about it:

$$
V(\text{two}\mid \text{full}) - V(\text{one}\mid\text{full}) = T > 0.
$$

Act-level EDT two-boxes. A good predictor will have anticipated exactly that and will therefore leave B empty, so act-level EDT agents tend to face empty boxes.

Evaluated *before* the observation, the policy "one-box if full" has higher news value than "two-box if full." Act-level EDT is therefore **dynamically inconsistent** here: it would pay to bind its future self. One can define a policy-level EDT,

$$
\pi^* = \arg\max_\pi \mathbb{E}[D\mid \text{agent follows } \pi],
$$

evaluated from the prior. Doing so goes beyond the theory as the source states it; it moves toward what are sometimes called "updateless" theories. My view is that the source's EDT should be read as act-level. Anyone applying EDT to sequential problems should state explicitly which version they are using, because the two can disagree.

### 4.5 Ratifiability

A related refinement, due to Jeffrey, restricts the agent to *ratifiable* acts: acts $A$ that remain optimal when news value is computed conditional on the decision to perform $A$. This blunts some news-managing verdicts. It also sometimes leaves no ratifiable option, so it is a supplement to EDT rather than part of its core.

## 5. EDT and self-locating belief: Sleeping Beauty

The reference article notes that EDT has been invoked in the Sleeping Beauty problem. Beauty is woken once if a fair coin lands Heads and twice if Tails, with her memory of any earlier waking erased. *Halfers* assign credence $1/2$ to Heads upon waking; *thirders* assign $1/3$. Halfers face Dutch-book arguments, and the source reports that adopting EDT has been argued to help.

The following worked illustration is mine. At each awakening, Beauty is offered a bet that pays $+x$ if Tails and $-y$ if Heads.

**Halfer using act-by-act causal evaluation.** She values a single acceptance at $\tfrac12 x - \tfrac12 y$. That ignores the fact that under Tails she will face, and accept, the same bet twice. A bookie can exploit this mismatch between her betting rate and the actual payoffs.

**Halfer using EDT.** Her two awakenings run the same reasoning, so deciding to accept now is (near-certain) evidence that she accepts in every awakening. Her news value is

$$
V(\text{accept}) = \tfrac12(-y) + \tfrac12(2x) = x - \tfrac{y}{2}.
$$

This matches the ex ante value of the policy "always accept," so the simple Dutch book disappears. EDT's willingness to count correlated copies of one's own decision repairs the halfer's bookkeeping.

The source then reports that Vincent Conitzer (2015) constructs a more elaborate scenario in which halfers who adopt EDT are still Dutch-booked. The question remains open. It shows something general, though: EDT's treatment of correlated decisions interacts deeply with self-locating belief, because "the other awakening's choice" is just a perfectly correlated twin.

## 6. Arguments for EDT

### 6.1 Results and dominance

The informal argument in Newcomb's problem is "why ain'cha rich?" Populations of one-boxers facing reliable predictors walk away with about \$990,000. Two-boxers walk away with about \$11,000. EDT is the theory that endorses the strategy that wins in such environments. CDT's reply is that one-boxers are rewarded for their dispositions, not their acts, and that each two-boxer did the best she could given the boxes in front of her.

### 6.2 The evidentialist's wager

The reference article mentions a different style of argument, from MacAskill, Vallinder, Oesterheld, Shulman, and Treutlein (2021). Even an agent who gives EDT less credence than CDT may have reason to act as EDT recommends, because EDT's stakes can be larger.

The structure is easy to formalize. Suppose the agent's decision is correlated with the decisions of $N$ similar agents, and she cares about the total outcome. Under EDT, the news value of cooperating includes the evidence that all $N$ correlated agents cooperate, so the EDT-difference between options scales like $N\Delta$. Under CDT, only her own causal contribution $\Delta$ counts. If she has credence $c$ in EDT and assigns expected choiceworthiness by a credence-weighted sum,

$$
\text{EC}(A) = c\, V(A) + (1-c)\, U(A),
$$

then for large $N$ the EDT term dominates whenever $cN\Delta$ exceeds the CDT-side disadvantage. In large worlds that contain many reasoners similar to us, EDT's recommendation wins even at low $c$. The argument depends on a substantive further assumption, that value differences are comparable across the two theories. That is itself a contested question in the theory of moral and decision-theoretic uncertainty.

## 7. Criticism

The reference article quotes the two classic objections:

- **Lewis:** EDT promotes "an irrational policy of managing the news."
- **Joyce:** "Rational agents choose acts on the basis of their *causal efficacy*, not their auspiciousness; they act to *bring about* good results even when doing so might betoken bad news."

The objection is clearest in common-cause cases. Choosing to abstain in the smoking lesion would be like a patient refusing a symptom-revealing test because a bad result would be bad news. The patient's choice changes what he learns, not what is true.

The evidentialist has two replies. In cases like the smoking lesion, the total-evidence rule (§4.2) arguably removes the offending correlation, so EDT does *not* manage the news. In cases like Newcomb, the evidentialist simply accepts the verdict and denies that it is irrational. If the predictor's reliability is real, choosing in the way that predictably correlates with wealth is rational. The disagreement then becomes a clash of basic intuitions about whether non-causal dependence should guide action, and no further calculation will settle it.

## 8. A procedure for unfamiliar cases

Pulling the pieces together, here is how I would apply EDT to a new problem. Steps 2 and 5 are my additions to the source's account.

1. **Specify the options** $A_1,\dots,A_n$ and outcomes fine-grained enough that desirability does not vary within an outcome.
2. **Fix the evidence** $E$ the agent has at the moment of choice, including her own motivational states.
3. **Build a joint model** giving $P(O_j \mid A_i, E)$. Include every source of correlation that survives conditioning on $E$: causal effects, predictors, copies, twins, and other instances of one's own reasoning.
4. **Compute** $V(A_i) = \sum_j P(O_j\mid A_i,E)\,D(O_j)$ and choose the maximum.
5. **State the level** of evaluation (act versus policy) if the problem is sequential or involves observing the outcome of a prediction.
6. **For comparison with CDT,** recompute with $P(K)$ in place of $P(K\mid A)$. Any difference measures exactly how much of the verdict rests on non-causal evidence.

## 9. Conclusion

Evidential decision theory is expected-utility maximization with one deliberate choice: weight outcomes by their probability *conditional on the act*. This makes the theory metaphysically economical, since it needs probability but no counterfactuals or causal structure. It is also partition-invariant, and it is responsive to every kind of dependence between one's choice and the world.

That responsiveness produces its distinctive verdicts: one-boxing in Newcomb's problem whenever the predictor beats 50.05% accuracy, cooperation with a twin whose correlation exceeds 5/7, and a repaired halfer bookkeeping in Sleeping Beauty. It also produces the charge of news management. Whether that charge sticks depends largely on a question the bare formula leaves open: what the agent is entitled to condition on. Read with the total-evidence rule, EDT agrees with CDT when correlations run through what the agent already knows. It diverges only where her choice itself is the evidence, which is the territory where the disagreement between the two theories is genuine.

---

**References (selected)**

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9).
- Gibbard, A. & Harper, W. (1976). *Counterfactuals and Two Kinds of Expected Utility*.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59(1).
- MacAskill, W., Vallinder, A., Oesterheld, C., Shulman, C. & Treutlein, J. (2021). "The Evidentialist's Wager."
- Wikipedia contributors, "Evidential decision theory," rev. 1373679688 (CC BY-SA 4.0).