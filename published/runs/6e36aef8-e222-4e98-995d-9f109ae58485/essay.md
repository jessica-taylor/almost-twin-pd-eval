# Causal Decision Theory: Choosing by What Your Actions Bring About

## 1. The guiding idea

Decision theory asks which of several available actions a rational agent should choose. Causal decision theory (CDT) answers: choose the action that **causes** the best outcome in expectation. The rival view is evidential decision theory (EDT), which recommends the action whose performance would be the best *news*, meaning the action whose being chosen most strongly indicates a good outcome.

In most ordinary cases the two theories agree. If eating an apple will make you happy and eating an orange will make you sad, eat the apple. Choosing the apple is both a cause of happiness and good evidence of it. The theories come apart only when an action is *correlated* with good or bad outcomes without *producing* them. That gap between correlation and causation is the subject of this essay.

I first set out the formal machinery, then work through the standard examples, and then take up the open question of how the counterfactual probabilities are to be computed. Where I go beyond the reference article (the Wikipedia entry on CDT), I flag it. The main additions are an interventionist reading of the counterfactuals, an explicit procedure for applying the theory, and a treatment of unstable cases through deliberational equilibrium.

## 2. Expected causal consequences

Even when causal structure is clear, outcomes are uncertain. The source's example: a good apple makes you happy, a bad apple makes you sad, and you don't know which this apple is. The expected causal effect of eating it depends on three things:

- how likely the apple is to be good,
- how happy a good apple makes you,
- how sad a bad apple makes you.

If $p$ is your credence that the apple is good, $h$ the utility of happiness, and $s$ the (negative) utility of sadness, eating has value $p\,h + (1-p)\,s$. This is ordinary expected utility. The key feature is that the quality of the apple is **not affected by your choice to eat it**. Your credence $p$ is the same whether or not you eat. All the theoretical interest lies in what to do when that independence fails.

## 3. Formal definitions

### 3.1 Gibbard–Harper: probabilities of counterfactuals

Gibbard and Harper (1981) define the causal expected utility of an action $A$ as

$$
U(A) \;=\; \sum_j P(A \,\square\!\!\rightarrow O_j)\, D(O_j),
$$

where:

- the $O_j$ are mutually exclusive, jointly exhaustive outcomes,
- $D(O_j)$ is the desirability (utility) of outcome $O_j$,
- $A \,\square\!\!\rightarrow O_j$ is the counterfactual "if $A$ were done, $O_j$ would obtain,"
- $P(\cdot)$ is the agent's credence in that counterfactual.

EDT replaces the probability of a counterfactual with a conditional probability:

$$
V(A) \;=\; \sum_j P(O_j \mid A)\, D(O_j).
$$

### 3.2 Why these differ

One might hope that $P(A \,\square\!\!\rightarrow O) = P(O \mid A)$ always, in which case CDT and EDT would coincide. Lewis (1976) showed that this cannot hold in general. His triviality result says that no conditional connective can have probabilities equal to the corresponding conditional probabilities across a class of probability functions closed under conditionalization, unless those functions are trivial.

Gibbard and Harper identified when the equality *does* hold. Assume:

1. **Centering:** $A \wedge (A \,\square\!\!\rightarrow O) \leftrightarrow A \wedge O$. In actual $A$-worlds, the counterfactual's consequent is just what actually happens.
2. **Conditional excluded middle:** for each $A$ and $O$, either $A \,\square\!\!\rightarrow O$ or $A \,\square\!\!\rightarrow \neg O$.

The source flags the second assumption as controversial. Given both, suppose the counterfactual is probabilistically independent of the act: $P(A \,\square\!\!\rightarrow O \mid A) = P(A \,\square\!\!\rightarrow O)$. Then

$$
P(A \,\square\!\!\rightarrow O) = P(A \,\square\!\!\rightarrow O \mid A) = \frac{P(A \wedge (A \,\square\!\!\rightarrow O))}{P(A)} = \frac{P(A\wedge O)}{P(A)} = P(O\mid A).
$$

So CDT and EDT agree exactly when **the act carries no evidence about what the act would cause**. They disagree when the act is evidence about the counterfactual dependencies themselves, typically because some common cause influences both the choice and the outcome.

### 3.3 An equivalent and more usable form: dependency hypotheses

*(This formulation is due to Lewis 1981, which the source cites but does not spell out.)*

Partition possibilities into **dependency hypotheses** $K_1,\dots,K_m$. Each $K_i$ is a maximally specific proposition about how outcomes depend causally on acts, and none is causally affected by the agent's choice. Then

$$
U(A) \;=\; \sum_i P(K_i) \sum_j P(O_j \mid A \wedge K_i)\, D(O_j).
$$

Contrast this with EDT, which in the same partition reads

$$
V(A) = \sum_i P(K_i \mid A) \sum_j P(O_j \mid A\wedge K_i) D(O_j).
$$

The entire difference sits in one place. **CDT weights dependency hypotheses by their unconditional probability $P(K_i)$; EDT weights them by $P(K_i \mid A)$.** CDT refuses to let the act serve as evidence about states it cannot influence.

### 3.4 An interventionist reading (my addition)

A modern way to make "causes" precise is Pearl's intervention operator. Model the situation as a causal graph. Let $\mathrm{Pa}$ denote the set of variables that are not descendants of the act node. Then

$$
U(A) = \sum_j P(O_j \mid \mathrm{do}(A))\, D(O_j), \qquad P(O\mid \mathrm{do}(A)) = \sum_{k} P(\mathrm{Pa}=k)\,P(O \mid A, \mathrm{Pa}=k),
$$

which is the "adjustment formula." This is the Lewis $K$-partition formula with dependency hypotheses identified with configurations of the act's non-descendants. The source does not use this formalism. I include it because it gives a concrete, checkable answer to "what should I hold fixed?" in many practical cases.

## 4. The diagnostic example: David and Bathsheba

Gibbard and Harper's example, quoted in the source, has the cleanest structure. Kings are either charismatic ($C$) or not ($\bar C$), and this is fixed by genes and childhood. Charismatic kings tend to act justly. Uncharismatic kings tend to act unjustly and also suffer successful revolts, because of their "sneaky, ignoble bearing." Unjust acts themselves do not cause revolts. David wants Bathsheba, and summoning her would be unjust.

The causal graph is $\text{Act} \leftarrow \text{Charisma} \rightarrow \text{Revolt}$, with no arrow from Act to Revolt.

Assign utilities as follows:

- Let $b>0$ be the value of having Bathsheba.
- Let $-r$ be the value of a revolt.
- Let $\rho_C < \rho_{\bar C}$ be the revolt probabilities for the two types.
- Let $c = P(C)$ be David's credence that he is charismatic.

**CDT:**

$$
U(\text{summon}) = b - r[c\rho_C + (1-c)\rho_{\bar C}], \qquad U(\text{abstain}) = - r[c\rho_C + (1-c)\rho_{\bar C}].
$$

The revolt term is identical for both acts, so $U(\text{summon}) - U(\text{abstain}) = b > 0$. CDT says summon.

**EDT:** EDT replaces $c$ with $P(C\mid \text{summon})$ in one line and $P(C \mid \text{abstain})$ in the other. Since summoning is evidence of being uncharismatic, $P(C\mid\text{summon}) < P(C\mid \text{abstain})$. If $r(\rho_{\bar C}-\rho_C)$ times that evidential gap exceeds $b$, EDT recommends abstaining.

Most people find the EDT verdict odd here. Abstaining does not make David charismatic. It merely deprives him of evidence that he isn't. This is the "medical Newcomb" pattern, and it is the main reason the source reports that philosophers who must choose usually prefer CDT.

## 5. Newcomb's problem

A predictor that is 99% reliable has filled opaque box B with \$1,000,000 if it predicted you would take only B, and left it empty otherwise. Transparent box A holds \$1,000. You may take B alone or both boxes.

The prediction was made in the past. It is a non-descendant of your act, so it is a dependency hypothesis: $K_M$ (million present) or $K_E$ (empty). Let $q = P(K_M)$.

**CDT:**

$$
U(\text{one-box}) = 10^6 q, \qquad U(\text{two-box}) = 10^6 q + 10^3.
$$

Two-boxing is better by \$1,000 for *every* value of $q$. This is a dominance argument, and CDT endorses it because the states are causally independent of the act.

**EDT:**

$$
V(\text{one-box}) = 0.99\cdot 10^6 = 990{,}000, \qquad V(\text{two-box}) = 0.01\cdot 10^6 + 10^3 = 11{,}000.
$$

EDT one-boxes.

The CDT reply to the obvious objection ("why aren't you rich?") is that the predictor rewards a certain *disposition*, not the act. Given whatever is in the box, taking the extra \$1,000 is better. Critics reply that an agent who reliably follows CDT reliably walks away with \$1,000. The source notes that philosophers remain divided.

### The twin prisoner's dilemma

Lewis (1979) observed that a prisoner's dilemma against a near-copy of yourself has the same structure. Your twin's choice is strongly correlated with yours, through common origin, but not caused by it. Hold the twin's action fixed: defecting dominates. So CDT defects even when it is nearly certain the twin reasons identically.

### Acts versus policies (my elaboration, informed by Meacham 2010 on binding)

The question of policies matters for applying the theory. CDT evaluates **acts available at the point of decision**, using the causal structure that holds at that moment. It has no built-in notion of "choosing a policy" except when adopting a policy is itself an act with causal consequences.

So if you can bind yourself to one-boxing *before* the predictor scans you, the binding act is causally upstream of the prediction. CDT then evaluates it favourably:

$$
U(\text{bind}) \approx 0.99\cdot 10^6 \gg U(\text{don't bind}) \approx 10^3 + 0.01\cdot 10^6.
$$

A CDT agent who anticipates Newcomb problems therefore wants to become a one-boxer. Yet at the moment of choice, unbound, it still two-boxes. CDT is in this sense *dynamically inconsistent about which decision procedure it endorses*. That is a real cost, and it is distinct from the question of which act is right in the one-shot case.

## 6. The open problem: where do the counterfactual probabilities come from?

The source states plainly that CDT "does not itself specify what algorithm to use to calculate the counterfactual probabilities." Three answers are on the table.

### 6.1 Lewis's imaging

To compute $P(A\,\square\!\!\rightarrow O)$, take each world $w$ and move its probability mass to $w_A$, the closest world in which $A$ holds:

$$
P^{A}(w') = \sum_{w:\, w_A = w'} P(w), \qquad P(A\,\square\!\!\rightarrow O) = P^{A}(O).
$$

Compare conditioning, which deletes the $\neg A$-worlds and renormalizes. Conditioning lets the surviving $A$-worlds be atypical, as with the uncharismatic kings. Imaging instead keeps every world's "background" and changes only what $A$ forces.

The source raises a worry: imaging requires knowing which world is closest. Equivalently, it requires knowing what would be the case if $A$ held. That is itself a counterfactual matter about which the agent may be uncertain, which threatens a regress.

### 6.2 Dependency hypotheses

Lewis's $K$-partition moves the uncertainty into the states. You need not know which world is closest; you only need a credence over hypotheses about causal dependence. The regress is stopped by requiring that each $K_i$ settle the dependence completely. The remaining burden is to identify the partition.

### 6.3 Causal models (my proposal for operational use)

For most problems someone would actually pose, I suggest the following practical rule:

> **Hold fixed exactly those variables that are not causal descendants of the act. Use unconditional credences for them, and condition on the act only downstream.**

This reproduces every textbook CDT verdict:

- Charisma is upstream of Act, so it is held fixed.
- The prediction is upstream, so it is held fixed.
- The twin's choice is a non-descendant, so it is held fixed.

It also tells you what to do when you are unsure of the graph itself. Put a credence over candidate graphs and treat each graph as a dependency hypothesis.

This rule assumes the agent can identify the causal graph. That is not always easy, as with predictors whose mechanism is opaque or with "logical" correlations between copies of a program. Whether such correlations should count as causal is precisely what rival theories dispute, so the rule does not settle every case. It does make CDT's commitments explicit.

## 7. Instability: Death in Damascus

Death will meet you tomorrow wherever it predicted you would be. Death is a reliable predictor. You are in Damascus and can stay or flee to Aleppo. Let $d$ be your credence that Death is in Damascus, and let survival be worth 1 and death 0. Then

$$
U(\text{Damascus}) = 1-d, \qquad U(\text{Aleppo}) = d.
$$

CDT says go wherever Death is less likely to be. But Death's location tracks your choice. As soon as you lean toward Aleppo, you should raise your credence that Death predicted Aleppo, which makes Damascus look better, and so on. No pure act is **ratifiable**, where an act is ratifiable if it maximizes $U$ computed with the credences you would have upon deciding to perform it. The source cites this case, via Egan, Meacham, and Harper, as one in which a CDT agent "would be unable to process the correlation."

**Operational resolution (from Harper, Skyrms, and Joyce, beyond the source's own text).** Treat deliberation as a dynamical process. Let $x$ be your current credence that you will choose Aleppo. Reliability links your credences about Death to $x$:

$$
d(x) \approx 1-x.
$$

Deliberation shifts probability toward whichever act currently has higher $U$. A **deliberational equilibrium** is a value $x^*$ at which no act has strictly greater causal expected utility. Here $U(\text{Damascus}) = U(\text{Aleppo})$ requires $d = 1/2$, so $x^* = 1/2$. At equilibrium you are indifferent, and CDT permits either act, or a coin flip if one is available and the predictor cannot anticipate its outcome.

This is what Joyce means, in the source's paraphrase, by saying CDT can take "information about what one is inclined or likely to do as evidence." The unconditional credences $P(K_i)$ are not frozen at the start of deliberation. They are whatever they are at the end of it.

## 8. The newer counterexamples

### 8.1 The Psychopath Button (Egan 2007)

Paul can press a button that kills all psychopaths. He would prefer a world without psychopaths, but he strongly prefers living among them to dying, and he believes only a psychopath would press the button.

I use illustrative numbers of my own:

| Outcome | Utility |
|---|---|
| Status quo (no press, or press as a non-psychopath with no further effect) | 0 |
| No psychopaths, Paul alive | 10 |
| Paul dead | −100 |

Let $\varepsilon = P(\text{Paul is a psychopath})$. Whether Paul is a psychopath is upstream of the press, so CDT gives

$$
U(\text{press}) = 10(1-\varepsilon) - 100\varepsilon, \qquad U(\text{refrain}) = 0.
$$

Pressing wins iff $\varepsilon < 1/11 \approx 0.091$. With a low prior, say $\varepsilon = 0.05$, naive CDT presses: $U = 4.5$. Egan reports that "pretty much everyone" thinks Paul should not press.

The deliberational response changes the picture. Suppose $P(\text{psycho}\mid\text{press}) = 0.9$ and $P(\text{psycho} \mid \text{refrain}) = 0.01$. If $x$ is Paul's credence that he will press, then $\varepsilon(x) = 0.01 + 0.89x$. Indifference requires $\varepsilon(x^*) = 1/11$, so

$$
x^* = \frac{1/11 - 0.01}{0.89} \approx 0.091.
$$

At equilibrium Paul is about 91% sure he won't press, and he is indifferent. Any initial tendency to press raises $\varepsilon$ past the threshold and pushes him back. So sophisticated CDT does not straightforwardly endorse pressing. It ends near "don't press," though it stops at indifference rather than a firm prohibition. (These numbers are my own illustration of the Joyce-style reply.)

Egan's diagnosis is that the problem lies in CDT's demand to "hold fixed the agent's unconditional credences in dependency hypotheses." The deliberational move answers him by letting those credences evolve during deliberation. Whether that fully answers him is contested.

### 8.2 The Adversarial Offer (Oesterheld & Conitzer 2021)

Two boxes cost \$1 each, and you may buy one or neither. Yesterday the seller put \$3 in each box she predicted you would *not* buy. Her prediction is 75% accurate.

Let $p_1, p_2, p_0$ be your credences that she predicted "box 1," "box 2," or "neither." The prediction is upstream, so CDT gives

$$
U(\text{buy }1) = 3(p_2+p_0) - 1, \qquad U(\text{buy }2) = 3(p_1+p_0) - 1, \qquad U(\text{neither}) = 0.
$$

Summing the first two: $U(1)+U(2) = 3(1+p_0) - 2 \ge 1$. So $\max(U(1),U(2)) \ge 1/2 > 0$ for *every* credence distribution. CDT always buys a box, and no amount of deliberation changes this, since the inequality holds everywhere.

Now look from outside. Whichever box you buy, the seller predicted it with probability 0.75, so it is empty with probability 0.75. Your expected payoff is $0.25\cdot 3 - 1 = -0.25$. A CDT agent predictably and voluntarily loses money. Oesterheld and Conitzer extend this to diachronic Dutch books.

Joyce's reply (2020) is roughly that the loss reflects facing an adversary who predicts you, not an incoherence in your preferences. Each purchase is causally the best available act given the actual contents of the boxes.

This case is harder for CDT than the Psychopath Button. Deliberational dynamics cannot rescue the verdict, because buying beats abstaining at every credence. It isolates the core commitment: CDT ranks acts by what they bring about, given a world that a predictor may have arranged against them.

## 9. A procedure for unfamiliar cases

Synthesizing the source's formal definition with the operational additions above:

1. **List acts** available *now*. Include acts of binding or commitment if they are available earlier and causally upstream of relevant variables.
2. **Draw the causal structure.** Separate variables downstream of the act from everything else: past events, common causes, other agents' predictions, correlated copies.
3. **Form dependency hypotheses** $K_i$ from the non-descendant variables. If you are unsure of the structure itself, include graph uncertainty in the $K_i$.
4. **Compute** $U(A) = \sum_i P(K_i)\sum_j P(O_j\mid A\wedge K_i) D(O_j)$, using *unconditional* credences for the $K_i$.
5. **Check ratifiability.** If your credences in the $K_i$ depend on what you expect to do, as with predictors and self-diagnostic acts, iterate. Update $P(K_i)$ given your current inclination and recompute until you reach a deliberational equilibrium. Choose among acts optimal at equilibrium, randomizing if permitted. *(Step 5 is not in the source's definition. It reflects the Harper/Skyrms/Joyce tradition, which the source alludes to through Joyce.)*

Checking the procedure against the cases:

| Case | Verdict |
|---|---|
| Bathsheba | Summon |
| Newcomb (unbound) | Two-box |
| Newcomb (binding available beforehand) | Bind |
| Twin prisoner's dilemma | Defect |
| Death in Damascus | Indifference / mix |
| Psychopath Button | Equilibrium near refraining |
| Adversarial Offer | Buy |

## 10. Assessment

CDT's appeal is that it captures a widely shared intuition: rational choice is about *making a difference*. A rational agent should not pursue correlations it cannot exploit, like abstaining to seem charismatic. In "medical Newcomb" cases, where the correlation runs through a common cause the agent can recognize, this verdict is compelling. That is one reason the theory is the majority view among philosophers.

Its difficulties cluster around a single feature. Holding fixed what the act does not cause is exactly right when the non-descendants are inert, and controversial when they include *predictions of, or copies of, the agent's own decision procedure*. In those environments CDT's evaluation of acts and the evaluation of CDT itself as a policy come apart. The CDT agent would pay to stop being one.

Finally, the source is right that CDT is underspecified. Imaging, dependency hypotheses, and causal-graph interventions are three implementations. They agree in standard cases, but they need supplementing, for instance by deliberational dynamics, in unstable cases where the agent's own inclinations bear on the states.

## 11. Conclusion

Causal decision theory evaluates an action by the expected value of what it would bring about. Formally, it weights outcomes by probabilities of counterfactuals or, equivalently, holds fixed unconditional credences over causally independent dependency hypotheses. It agrees with evidential decision theory whenever acts carry no evidence about those hypotheses. It diverges, recommending summoning, two-boxing, and defecting against a twin, when they do.

Applying it requires settling what the act causes. The source leaves this open, and causal graphs offer a workable answer. Unstable cases additionally call for treating deliberation as a process that ends in ratifiable equilibrium. With these supplements CDT yields determinate verdicts in a wide range of cases. The remaining dispute, sharpest in the Adversarial Offer, is over whether choosing by causal efficacy can be rational when the world is shaped by predictions of that very choice.

### References (selected)

- Gibbard, A. & Harper, W. (1981). "Counterfactuals and two kinds of expected utility." *Ifs*, 153–190.
- Lewis, D. (1976). "Probabilities of conditionals and conditional probabilities." *Phil. Review* 85.
- Lewis, D. (1981). "Causal decision theory." *Australasian J. Phil.* 59.
- Egan, A. (2007). "Some counterexamples to causal decision theory." *Phil. Review* 116.
- Joyce, J. (2012). "Regret and instability in causal decision theory." *Synthese* 187.
- Oesterheld, C. & Conitzer, V. (2021). "Extracting money from causal decision theorists." *Phil. Quarterly* 71.