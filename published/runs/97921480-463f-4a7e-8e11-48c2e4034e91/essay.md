# Causal Decision Theory: Choosing by What You Bring About

## 1. The guiding idea

Decision theory asks which of several available actions a rational agent should take, given what the agent believes and what the agent wants. Most answers start from expected utility: weight the value of each possible outcome by how likely it is, then add up. The question is *which* "how likely" to use.

**Causal decision theory** (CDT) answers that a rational agent should choose the action that *causes* the best outcome in expectation. The reference article contrasts this with **evidential decision theory** (EDT), which recommends the action that would be the best *news* to receive about oneself. Usually the two coincide, because an act is usually good news exactly when it causes good things. They come apart when an act is correlated with good or bad outcomes without causing them. Most of the philosophical interest of CDT lies in those cases.

This essay sets out the formal theory and explains how it handles dependencies and counterfactuals. It works through the standard examples and then turns to the problem cases. Where the reference article leaves things open, most notably how counterfactual probabilities are actually computed and what to do when CDT's verdict is unstable, I propose an operational procedure. I mark it as my own addition.

## 2. Setup: acts, states, outcomes

Fix a finite set of acts $\mathcal{A}$, a set of outcomes $\{O_j\}$, a credence function $P$, and a desirability (utility) function $D$ on outcomes.

The textbook Savage-style formula partitions the world into states $S_i$ and writes

$$
EU(A) = \sum_i P(S_i)\, D(A, S_i),
$$

where $D(A,S_i)$ is the value of doing $A$ in state $S_i$. This formula silently assumes that the probability of the state does not depend on the act. When that assumption fails, there are two natural repairs, and they define the two theories.

**Evidential expected utility** (Jeffrey's "news value") conditions on the act:

$$
V(A) = \sum_j P(O_j \mid A)\, D(O_j).
$$

**Causal expected utility**, in the formulation of Gibbard and Harper (1981) quoted in the source, uses probabilities of counterfactual conditionals:

$$
U(A) = \sum_j P(A \mathbin{\square\!\!\rightarrow} O_j)\, D(O_j).
$$

Here $A \mathbin{\square\!\!\rightarrow} O_j$ reads "if I were to do $A$, $O_j$ would result." The source glosses this as the probability that $A$ "necessarily implies" $O_j$. The standard reading, which I adopt, is the subjunctive one: it concerns what *would* happen under $A$, not what $A$ indicates.

### Why the two can differ

If probabilities of conditionals always equalled conditional probabilities, so that $P(A \mathbin{\square\!\!\rightarrow} O) = P(O\mid A)$, then $U = V$ and the debate would vanish. The source notes that Lewis (1976) proved this identity cannot hold in general. His triviality result shows that no conditional connective has probabilities matching conditional probabilities across a class of probability functions closed under conditionalization, unless those functions are trivial.

Gibbard and Harper identified when the two do agree. Assume two axioms, one closely related to the contested principle of *conditional excluded middle* (for every $A$ and $O$, either $A \mathbin{\square\!\!\rightarrow} O$ or $A \mathbin{\square\!\!\rightarrow} \neg O$). Under those axioms, statistical independence of $A$ from the counterfactual $A \mathbin{\square\!\!\rightarrow} O_j$ guarantees

$$
P(A \mathbin{\square\!\!\rightarrow} O_j) = P(O_j \mid A).
$$

So the two theories diverge exactly when the agent's choice is *evidence about* which counterfactuals hold. This happens when some factor the agent cannot influence both shapes the outcomes and correlates with the choice.

## 3. Making counterfactual probabilities operational

The source openly states a weakness here: CDT "does not itself specify what algorithm to use to calculate the counterfactual probabilities." It mentions one proposal, Lewis's *imaging*. I present imaging and then two further formulations that are standard in the literature but not described in the source. I find these more useful in practice.

### 3.1 Imaging (source)

To compute $P(A \mathbin{\square\!\!\rightarrow} O)$, take each possible world $w$ and move its probability mass to $w_A$, the closest world to $w$ in which $A$ is true. Then measure the probability of $O$ in the resulting distribution $P_A$:

$$
P(A \mathbin{\square\!\!\rightarrow} O) = P_A(O) = \sum_{w} P(w)\, \mathbb{1}[O \text{ holds at } w_A].
$$

Conditioning differs in how it treats the same worlds. It deletes the $\neg A$ worlds and renormalizes, so it keeps whatever the surviving $A$-worlds "say" about hidden causes. Imaging instead *moves* every world minimally, so features of the world that $A$ cannot affect stay where they were. The source records an objection due to Shaffer (2009): imaging presupposes knowing what one would believe if one were certain of $A$. That is itself a conditional one may be unsure of, which threatens a regress.

### 3.2 Dependency hypotheses (Lewis 1981; my exposition)

A more tractable formulation partitions possibilities into **dependency hypotheses** $K_1, \dots, K_n$. Each $K$ is a maximally specific proposition about how outcomes depend causally on acts, and so each describes features of the world that lie outside the agent's control. Then

$$
U(A) = \sum_{K} P(K) \sum_j P(O_j \mid A \wedge K)\, D(O_j).
$$

The crucial feature is that $P(K)$ is **unconditional**. The agent does not update beliefs about the causal structure on the basis of its own choice. Compare EDT, which in the same notation is

$$
V(A) = \sum_{K} P(K \mid A) \sum_j P(O_j \mid A \wedge K)\, D(O_j).
$$

The entire difference between the theories is the substitution of $P(K)$ for $P(K\mid A)$. This matches the source's report of Egan's diagnosis: CDT "hold[s] fixed the agent's unconditional credences in dependency hypotheses." When the act is independent of $K$, the two coincide, which is the Gibbard–Harper condition restated.

### 3.3 Interventions (my addition)

In a causal Bayes net, the counterfactual probability is naturally read as the interventional probability $P(O \mid do(A))$. Suppose $Z$ is a set of variables satisfying the back-door criterion: roughly, $Z$ blocks every non-causal path from act to outcome. Then

$$
P(O\mid do(A)) = \sum_z P(z)\, P(O \mid A, z).
$$

This is formally the dependency-hypothesis formula with $K$ replaced by the confounders $Z$. It offers a concrete answer to the "vagueness" objection. If the agent has a causal model, counterfactual probabilities are computable from it. The vagueness is relocated rather than eliminated, however, because CDT now inherits whatever uncertainty there is about which causal model is correct.

## 4. Easy cases

### The apple (source)

The source's informal example: eating a good apple causes happiness, eating a bad one sadness, and you are unsure which you have. Let $p = P(\text{good})$, with $D(\text{happy}) = h > 0$, $D(\text{sad}) = -s < 0$, and not eating worth $0$. Whether the apple is good does not depend on whether you eat it, so

$$
U(\text{eat}) = p h - (1-p)s,
$$

and you should eat iff $p > s/(h+s)$. These are the source's "three things": the probability, the upside, and the downside. Because eating gives no evidence about the apple's quality, $U = V$ here. Most real decisions are like this.

### King David (source)

Gibbard and Harper's case is the first in which CDT and EDT really disagree. A king's charisma $C$ is fixed by genes and upbringing. Charismatic kings tend to act justly and rarely face successful revolts. Uncharismatic kings tend to act unjustly and frequently face revolts, because of their "sneaky, ignoble bearing," *not* because of the unjust acts. David doesn't know his type. Sending for Bathsheba is unjust.

To make the case concrete, I add illustrative numbers that are not in the source:

- $P(C) = 0.5$.
- $P(\text{revolt}\mid C) = 0.1$ and $P(\text{revolt}\mid\neg C) = 0.8$, independent of the act.
- $P(\text{send}\mid C) = 0.2$ and $P(\text{send}\mid \neg C)= 0.8$.
- Bathsheba is worth $+10$ and a revolt $-50$.

**CDT.** Hold $P(C)=0.5$ fixed. Then $P(\text{revolt}) = 0.45$ whichever act is chosen, and

$$
U(\text{send}) = 10 - 50(0.45) = -12.5, \qquad U(\text{abstain}) = -22.5.
$$

Sending wins by exactly $10$. This is just dominance: in each charisma state, sending is better by 10.

**EDT.** Bayes gives $P(C\mid\text{send}) = 0.2$ and $P(C\mid\text{abstain}) = 0.8$. Hence $P(\text{revolt}\mid \text{send}) = 0.66$ and $P(\text{revolt}\mid\text{abstain}) = 0.24$, so

$$
V(\text{send}) = 10 - 33 = -23, \qquad V(\text{abstain}) = -12.
$$

EDT says abstain, since abstaining is good news about one's charisma. CDT says send, because abstaining cannot change one's charisma. The source reports that philosophers forced to choose here usually side with CDT. The intuition is that refraining from what you want merely to *seem* charismatic to yourself is "managing the news."

## 5. Newcomb's problem and its relatives

### Newcomb (source)

Box A is transparent and holds \$1,000. Box B is opaque and contains \$1,000,000 iff a 99%-reliable predictor predicted you would take only B. You choose between B alone and both boxes.

**CDT.** Let $q$ be your unconditional credence that B is full. The prediction is already made, so $q$ does not vary with the act:

$$
U(\text{two}) = q(1{,}001{,}000) + (1-q)(1{,}000) = U(\text{one}) + 1{,}000.
$$

Two-boxing wins by \$1,000 for *every* $q$, and CDT two-boxes.

**EDT.** With conditional credences,

$$
V(\text{one}) = 0.99 \times 10^6 = 990{,}000,
$$

$$
V(\text{two}) = 0.01(1{,}001{,}000) + 0.99(1{,}000) = 11{,}000.
$$

EDT one-boxes.

The source presents this as an "early alleged counterexample" to CDT. Two-boxers predictably walk away with about \$1,000 and one-boxers with about \$1,000,000. It also records that philosophers remain divided on which is rational. The CDT reply is "Why ain't you rich?" in reverse: the predictor rewards a certain kind of agent, and by the time you choose, which kind you are is no longer up to this choice.

### Twin prisoner's dilemma (source)

Lewis (1979) argued that the prisoner's dilemma is a Newcomb problem. Suppose you play against a near-duplicate whose choice correlates strongly with yours but is not caused by it. CDT holds the twin's act fixed and defects by dominance. EDT notes that cooperating is evidence the twin cooperates and cooperates. The structure is the same as in Newcomb's problem.

### Acts versus policies (my addition)

The task asks how CDT evaluates *policies*. CDT evaluates whatever is chosen *at the moment of choice*, by its causal consequences from then on. Suppose you can bind yourself to one-boxing *before* the predictor forms its prediction, and the predictor reads such commitments. Then the commitment causally influences the box contents, and CDT itself recommends making it. Meacham's (2010) discussion of binding, cited in the source, explores this.

So CDT is not hostile to one-boxing policies. It holds that a policy is worth adopting only if adopting it *causes* better results, and that at a later choice point an unbinding agent re-evaluates. This yields a clean test for unfamiliar cases: locate the moment of choice and ask what that choice can still affect. Agents who foresee being CDT-reasoners in Newcomb-like futures have causal reason to acquire commitment devices now.

## 6. Instability: when the act changes the beliefs that evaluate it

The formula in §3.2 takes $P(K)$ as given. But $P(K)$ may itself depend on the agent's credence about what it will do, and that credence shifts as deliberation proceeds. The problem cases in the source's "Counterexamples" section mostly exploit this.

### Death in Damascus (source)

Death predicts where you will be tomorrow and waits there. You choose between Damascus ($D$) and Aleppo. Let $r > 1/2$ be Death's reliability and $x$ your current credence that you will go to Damascus. Then

$$
P(\text{Death at } D) = rx + (1-r)(1-x).
$$

With survival worth $1$ and death $0$, a short calculation gives

$$
U(D) - U(\text{Aleppo}) = (2r-1)(1-2x).
$$

If you lean toward Damascus ($x > 1/2$), Aleppo looks better. If you lean toward Aleppo, Damascus looks better. Neither pure act survives being chosen. The source puts it that a CDT agent "would be unable to process the correlation." That is, CDT's recommendation depends on a credence that the recommendation itself undermines.

### Ratifiability and deliberational equilibrium (largely my exposition)

Two tools from the CDT literature address this. Harper (1984), cited in the source, uses ratifiability. Joyce (2012), also cited, develops what he calls taking "information about what one is inclined or likely to do as evidence."

**Ratifiability.** Let $U_A(B) = \sum_K P(K\mid A) \sum_j P(O_j\mid B\wedge K)D(O_j)$ denote the causal utility of $B$ *computed by someone who has learned they will do $A$*. Act $A$ is **ratifiable** iff

$$
U_A(A) \ge U_A(B) \quad\text{for all } B \in \mathcal{A}.
$$

A ratifiable act is one you would not regret choosing given the information that you chose it. In Newcomb, two-boxing is ratifiable and one-boxing is not. In Death in Damascus, neither pure act is ratifiable.

**Deliberational dynamics.** Treat deliberation as a process on the credence vector $x$ over acts. Update credences toward acts with higher current $U$, for example

$$
x_{t+1} = x_t + k\,(U_{x_t}(D) - U_{x_t}(\text{Aleppo})),
$$

clipped to $[0,1]$, and recompute $P(K)$ from $x_{t+1}$ at each step. Deliberation ends at a fixed point where no act has higher causal utility than the agent's current mixture. In Death in Damascus the fixed point is $x = 1/2$. You become maximally uncertain where you will go, and then either city is equally choiceworthy. A coin flip implements this, and against a predictor who cannot predict the coin, it also yields the best survival odds of $1/2$.

### The Psychopath Button (source)

Paul can press a button that kills all psychopaths. He would prefer a world without psychopaths, but he is confident that only a psychopath would press it, and he strongly prefers living among psychopaths to dying. Egan reports that "pretty much everyone" thinks Paul should not press. Naive CDT presses: with Paul's unconditional credence that he is a psychopath low, pressing causally rids the world of others at small expected cost.

Ratifiability reveals the structure. Pressing is unratifiable, because conditional on pressing, Paul is probably a psychopath and would die. Not pressing may *also* be unratifiable, because conditional on not pressing, he is probably sane and pressing looks good. Deliberational CDT therefore drives Paul's credence in pressing toward an intermediate equilibrium $x^*$. Pressing at $x^*$ implies a substantial credence of being a psychopath, and that is usually enough to make not pressing at least as good.

Whether this rescues the intuitive verdict depends on the numbers, and critics regard the reliance on mixed equilibria as ad hoc. Egan's own conclusion, reported in the source, is that the fault lies precisely in holding dependency-hypothesis credences fixed.

### The Adversarial Offer (source)

There are two boxes, each costing \$1, and you may buy at most one. Yesterday a seller who is 75% accurate put \$3 in each box she predicted you would *not* buy. The source states CDT's reasoning: at least one box contains \$3, so the boxes jointly hold at least \$3 in expectation. Some box must therefore have expected content of at least \$1.50 under your fixed credences, which exceeds the \$1 price, so CDT buys.

Conditional on buying box 1, however, the seller probably predicted it and left it empty. So $V(\text{buy }1) = 0.25\times 3 - 1 = -0.25$, and EDT declines. Even a deliberating CDT agent who mixes evenly over the boxes still sees expected content $\ge 1.5$ in each and buys. The seller profits about \$0.25 per sale on average. Oesterheld and Conitzer (2021), along with Spencer (2020), use such cases to argue that CDT agents can be money-pumped, including by diachronic Dutch books, and can forgo guaranteed payoffs. The source lists Joyce's reply paper, "Yet Another Refutation of Causal Decision Theory?", but does not detail its argument.

## 7. An operational procedure (my proposal)

The source leaves two things open: how to compute counterfactual probabilities, and what CDT says when its verdict is self-undermining. The following procedure seems to me the most defensible reading, consistent with Lewis's and Joyce's versions of CDT. It is an interpretation, not settled doctrine.

1. **Fix the choice point.** Identify exactly what is being chosen and when: an act now, or a policy or commitment adopted earlier.
2. **Partition by dependency hypotheses.** Let $K$ range over everything relevant to outcomes that the choice cannot causally affect: past events, others' fixed dispositions, predictions already made, the agent's own type. If a causal graph is available, $K$ is a back-door adjustment set.
3. **Compute causal utilities** $U(A) = \sum_K P(K)\sum_j P(O_j\mid A\wedge K)D(O_j)$ for every $A$.
4. **Check ratifiability.** Recompute $P(K)$ under the supposition that you will do $A$ and see whether $A$ remains optimal. If the $U$-maximizing act is ratifiable, choose it.
5. **Otherwise, deliberate to equilibrium.** Iterate credences over acts toward higher-$U$ acts until reaching a fixed point $x^*$. Choose any act in the support of $x^*$, using a randomizer if mixing is literally available. All acts in the support have equal causal utility at equilibrium.
6. **Consider earlier choice points.** If there was an opportunity to bind oneself before correlated states were fixed, evaluate the commitment by the same procedure at that earlier time.

Applied to the cases above, this yields the following verdicts:

| Case | Verdict |
|---|---|
| Apple | Eat iff $p > s/(h+s)$ |
| King David | Send |
| Newcomb | Two-box at the moment of choice; pre-commit to one-boxing if possible beforehand |
| Twin PD | Defect |
| Death in Damascus | 50/50 |
| Psychopath Button | Intermediate mixture, often favoring not pressing |
| Adversarial Offer | Buy, a verdict critics regard as a defect |

## 8. Assessment

The case for CDT rests on a simple principle: rational choice is about *making a difference*. If nothing you do now can alter whether box B is full, or whether you are charismatic, then letting such facts sway you is acting for appearances. Dominance reasoning in Newcomb and Bathsheba is its clearest expression. The source's observation that philosophers generally prefer CDT to EDT reflects the persuasiveness of this thought.

The source groups the criticisms into two families.

- **Vagueness.** CDT needs counterfactual probabilities and no canonical algorithm supplies them. Imaging faces a regress worry. Causal models help, but only relative to a trusted model.
- **Counterexamples.** Newcomb-type cases yield poor outcomes for CDT agents, and the newer cases (Death in Damascus variants, the Adversarial Offer, the Psychopath Button) show instability or exploitability. Egan traces all of these to holding $P(K)$ fixed. Oesterheld and Conitzer argue that the exploitability is a sign of irrationality.

Defenders, led by Joyce, respond that a properly deliberating CDT agent *does* use evidence about its own inclinations. Instability is then a feature of the problems, not a bug in the theory. In my judgment the deliberational version answers Death in Damascus well and the Psychopath Button partially. The Adversarial Offer remains the sharpest challenge, because there the equilibrium itself is exploitable.

## 9. Conclusion

CDT replaces the evidential question "what does my act indicate?" with the causal question "what does my act bring about?" Formally, it weights outcomes by counterfactual probabilities $P(A \mathbin{\square\!\!\rightarrow} O)$. In the dependency-hypothesis form, it averages conditional outcome probabilities over *unconditional* credences in the causal structure. This one modification separates it from EDT. It recommends sending for Bathsheba, two-boxing in Newcomb, and defecting against a twin, and it agrees with EDT whenever acts carry no evidence about what they cannot affect.

Its open problems are how to compute counterfactual probabilities and what to do when an act's own selection undermines it. I have suggested an operational answer for each: causal models or dependency partitions for the first, and ratifiability plus deliberational equilibrium for the second. Whether that is enough to meet Egan's and Oesterheld–Conitzer's counterexamples remains, as the reference article indicates, an active dispute.

---

**References (selected)**
Gibbard, A. & Harper, W. (1981). "Counterfactuals and two kinds of expected utility."
Lewis, D. (1976). "Probabilities of conditionals and conditional probabilities"; (1979). "Prisoners' dilemma is a Newcomb problem"; (1981). "Causal decision theory."
Egan, A. (2007). "Some counterexamples to causal decision theory."
Joyce, J. (2012). "Regret and instability in causal decision theory."
Oesterheld, C. & Conitzer, V. (2021). "Extracting money from causal decision theorists."
Wikipedia, "Causal decision theory," rev. 1381555528 (reference article).