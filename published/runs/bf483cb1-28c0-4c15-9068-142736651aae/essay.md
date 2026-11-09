# Causal Decision Theory: Choosing by What Your Actions Would Bring About

## 1. The idea in one sentence

Causal decision theory (CDT) says that a rational agent facing a set of options should pick the one that *causes* the best outcome in expectation. The phrase "causes" carries the weight. The rival view, evidential decision theory (EDT), recommends the option whose being chosen would be the best *news*: the act that, once you learned you had done it, would make you expect the best outcome.

Usually the two agree, because what an act indicates about outcomes is usually what it brings about. They come apart when an act is correlated with a good or bad state of the world without causing it. Those cases are the subject of this essay.

I first set out the formal machinery, drawing mainly on the reference article (which follows Gibbard and Harper 1981 and Lewis 1981). I then work through the standard examples numerically. Last, I address a question the reference article leaves open: how one should actually *compute* the counterfactual probabilities CDT needs, and what to do when the computation is unstable. I mark clearly where I go beyond the source.

## 2. A warm-up: expected causal consequences

The reference article starts with an apple. Suppose eating a good apple makes you happy (utility $u_h > 0$), eating a bad one makes you sad ($u_s < 0$), and not eating gives utility $0$. You assign probability $p$ to the apple being good. The apple's quality is a fact your choice does not affect, so

$$
U(\text{eat}) = p\,u_h + (1-p)\,u_s, \qquad U(\text{abstain}) = 0 .
$$

You eat iff $p\,u_h + (1-p)\,u_s > 0$. The three inputs the source lists appear explicitly: the probability of good versus bad, how good the good outcome is, and how bad the bad outcome is.

Nothing here distinguishes CDT from EDT. Eating is no evidence about the apple's quality, so conditional and unconditional probabilities coincide. The theories diverge only when the act is evidentially but not causally related to some relevant state.

## 3. The formal theory

### 3.1 Gibbard–Harper expected utility

Let $\mathcal{A}$ be the set of available acts and $\{O_j\}$ a partition of outcomes with desirabilities $D(O_j)$. Gibbard and Harper define the causal expected utility of an act $A$ as

$$
U(A) = \sum_j P(A \,\square\!\!\rightarrow O_j)\, D(O_j),
$$

where $A \,\square\!\!\rightarrow O_j$ is the counterfactual conditional "if $A$ were performed, $O_j$ would obtain."

The reference article glosses $P(A\,\square\!\!\rightarrow O_j)$ as the probability that "$A$ necessarily implies $O_j$." This should not be read as *strict* implication, i.e. $O_j$ true in every world where $A$ is. The intended object is the Stalnaker–Lewis counterfactual, which is true when $O_j$ holds in the *closest* $A$-world(s). The difference matters: almost no act strictly implies its outcome.

Compare EDT's evidential expected value:

$$
V(A) = \sum_j P(O_j \mid A)\, D(O_j).
$$

If $P(A\,\square\!\!\rightarrow O_j) = P(O_j\mid A)$ always held, the two theories would coincide. Lewis (1976) showed that no conditional connective can have this property in general. The reference article's footnote states his stronger result: if a class of probability functions is closed under conditionalization, a "probability conditional" exists only if every function in the class is trivial, assigning positive probability to at most two incompatible alternatives. So the probability of a conditional is a genuinely different quantity from a conditional probability, and CDT is a genuinely different theory.

### 3.2 When the two coincide: the Gibbard–Harper lemma

The reference article reports that, under two axioms, the statistical independence of $A$ from $A\,\square\!\!\rightarrow O_j$ is enough for agreement. A short reconstruction shows why. Assume:

1. **Conditional excluded middle (CEM):** for each $A$, exactly one of $A\,\square\!\!\rightarrow O_j$ (over the partition $\{O_j\}$) is true. This is the controversial axiom.
2. **Counterfactual modus ponens / centering:** if $A$ is actually true, then $A\,\square\!\!\rightarrow O_j$ is true iff $O_j$ is.

From (2), $A \wedge (A\,\square\!\!\rightarrow O_j)$ and $A\wedge O_j$ are the same proposition. Hence

$$
P(O_j\mid A) = P(A\,\square\!\!\rightarrow O_j \mid A).
$$

If $A$ is independent of $A\,\square\!\!\rightarrow O_j$, the right-hand side equals $P(A\,\square\!\!\rightarrow O_j)$, and $U(A)=V(A)$.

This identifies the diagnostic exactly. **CDT and EDT diverge precisely when your act is evidence about which counterfactuals are true**, that is, about how the world is causally set up to respond to you.

### 3.3 Lewis's dependency hypotheses

A more practical form, due to Lewis (1981), partitions possibilities into *dependency hypotheses* $K_1,\dots,K_n$. Each is a maximally specific proposition about how outcomes causally depend on acts, and none is under the agent's causal control. Then

$$
U(A) = \sum_k P(K_k) \sum_j P(O_j \mid A \wedge K_k)\, D(O_j).
$$

The EDT analogue replaces $P(K_k)$ with $P(K_k \mid A)$:

$$
V(A) = \sum_k P(K_k\mid A) \sum_j P(O_j \mid A\wedge K_k)\, D(O_j).
$$

This is the cleanest way to see the difference. **CDT holds fixed the agent's unconditional credence in the causal structure of the world. EDT lets the act shift that credence.** Egan's criticism, discussed below, targets exactly this feature.

### 3.4 Imaging

Lewis also proposed computing $P(A\,\square\!\!\rightarrow O)$ by *imaging*. Each world $w$ sends its probability mass to the closest world $w_A$ in which $A$ holds:

$$
P_A(w') = \sum_{w:\, w_A = w'} P(w), \qquad P(A\,\square\!\!\rightarrow O) = P_A(O).
$$

Conditionalization deletes the $\neg A$-worlds and renormalizes, so it moves mass toward $A$-worlds that are already probable. Imaging instead moves each world's mass to its own nearest $A$-variant, which preserves facts that $A$ would not have changed, such as yesterday's prediction or your genes.

The reference article (following Shaffer 2009) notes a worry here. Imaging presupposes we know the similarity ordering, i.e. what the closest $A$-world is. That is itself a counterfactual matter about which we may be uncertain, so the procedure threatens a regress. In general the source treats CDT as *underspecified*: it tells you to use probabilities of counterfactuals but gives no algorithm for obtaining them.

## 4. The central cases

### 4.1 King David and Bathsheba

Gibbard and Harper's example works as follows. Kings are either charismatic ($C$) or not ($\bar C$), and this is fixed by genes and upbringing. Charismatic kings tend to act justly, and they rarely face successful revolts. Unjust acts do not themselves cause revolts; a sneaky bearing does. David is unsure of his type. Sending for Bathsheba is unjust, and he wants her.

Take $K_1 = C$ and $K_2 = \bar C$. Let $b>0$ be the value of sending for her, $R>0$ the disvalue of a revolt, and $r_C < r_{\bar C}$ the revolt probabilities by type. These probabilities do not depend on the act. With $c = P(C)$:

$$
U(\text{send}) = b - R\,[\,c\,r_C + (1-c)\,r_{\bar C}\,], \qquad U(\text{abstain}) = -R\,[\,c\,r_C + (1-c)\,r_{\bar C}\,].
$$

The difference is $b>0$, so **CDT says send.** EDT, by contrast, notes that $P(C\mid\text{send}) < P(C\mid\text{abstain})$, because unjust acts are evidence of being uncharismatic. EDT recommends abstaining whenever

$$
b < R\,(r_{\bar C}-r_C)\,\big[P(C\mid\text{abstain}) - P(C\mid\text{send})\big].
$$

CDT's verdict is intuitive here. Abstaining would only *manage the news*; it would not make David more charismatic. The source reports that, when forced to choose, philosophers usually prefer CDT, and cases like this are the reason.

### 4.2 Newcomb's problem

Box A is transparent and holds \$1,000. Box B holds \$1,000,000 iff a 99%-reliable predictor predicted you would take only B. Let $q$ be your credence that B is full. The prediction is already made, so it is a dependency hypothesis outside your control:

$$
U(\text{two-box}) = q(1{,}001{,}000) + (1-q)(1{,}000) = U(\text{one-box}) + 1{,}000.
$$

Two-boxing wins by exactly \$1,000 *for every* $q$. **CDT recommends two-boxing**, and this is the dominance argument written in expected-utility form. EDT uses $P(\text{full}\mid\text{one-box}) = 0.99$:

$$
V(\text{one-box}) = 990{,}000, \qquad V(\text{two-box}) = 0.01(1{,}001{,}000) + 0.99(1{,}000) = 11{,}000.
$$

The reference article records the standard objection: CDT agents predictably walk away with about \$1,000 while one-boxers get about \$1,000,000. Philosophers remain divided over which choice is rational.

The defender of CDT replies that Newcomb rewards a certain *kind of agent* rather than an act. Given the box contents, which are fixed, the two-boxer always does better than she would have by one-boxing.

The **twin prisoner's dilemma** (Lewis 1979) has the same structure. Your twin's choice correlates with yours but is not caused by it. CDT treats the twin's choice as a fixed state, so defection dominates and CDT defects.

### 4.3 Death in Damascus

Death predicts where you will be tomorrow and waits there. You can stay in Damascus ($D$) or flee to Aleppo ($A$), and Death is reliable. Let $\pi = P(\text{I go to } D)$ be your current credence about your own choice. Since Death tracks you, your credence that Death is in Damascus is about $\pi$. With death costing $L$:

$$
U(D) \approx -\pi L, \qquad U(A) \approx -(1-\pi)L.
$$

Whichever act you currently favour looks worse, because favouring it raises your credence that Death is waiting there. The recommendation flips as your inclinations change.

The reference article describes this as CDT being "unable to process the correlation," citing Egan, Meacham and Harper. That characterization is contested. The CDT agent processes the correlation perfectly well through $P(K)$; the problem is that $P(K)$ depends on her own evolving credence about what she will do. Section 5 takes this up.

### 4.4 The Adversarial Offer

This case is from Oesterheld and Conitzer. There are two boxes at \$1 each, and you may buy one or neither. Yesterday the seller put \$3 into each box she predicted you would *not* buy, and her prediction is accurate with probability $0.75$.

Let $x_i = P(\text{box } i \text{ contains } \$3)$. The seller predicted at most one purchase, so at least one box is full, which gives $x_1 + x_2 \ge 1$ and $\max_i x_i \ge \tfrac12$. CDT therefore values the better box at

$$
U(\text{buy best}) = 3\max_i x_i - 1 \ \ge\ 0.5 > 0 = U(\text{buy none}),
$$

and **CDT buys**. But conditional on buying box $i$, that box is full only if the seller erred:

$$
P(\text{box } i \text{ full} \mid \text{buy } i) = 0.25, \qquad 3(0.25) - 1 = -0.25.
$$

The seller expects to earn \$0.25 per CDT customer, so a CDT agent can predictably be exploited for money. Oesterheld and Conitzer extend this kind of construction to diachronic Dutch books. Joyce (2020) replies that the agent is not irrational, merely facing an adversary who punishes a certain decision procedure.

### 4.5 The Psychopath Button

This is Egan's case. Paul could press a button that kills all psychopaths. He would prefer a world without them, but he is confident that only a psychopath would press it, and he much prefers living among psychopaths to dying.

Take utilities: no psychopaths $+10$, status quo $0$, death $-100$. Let Paul's unconditional credence that he is a psychopath be $0.05$, while $P(\text{psycho}\mid\text{press}) = 0.9$. Then

$$
U(\text{press}) = 0.05(-100) + 0.95(10) = 4.5 > 0 = U(\text{don't}),
$$

so naive CDT presses. EDT gives $0.9(-100)+0.1(10) = -89$ and does not press. Egan reports that "pretty much everyone" agrees Paul should not press. His diagnosis is that the intuitive rule, "do what you expect will bring about the best results," is not the same as CDT's rule, "maximize expected value holding fixed your initial credences in dependency hypotheses." On his view, the fixing of $P(K)$ is the defect.

## 5. The open question: which credences, and when?

The reference article raises two issues and does not resolve them:

1. CDT does not say how to compute counterfactual probabilities.
2. Joyce, CDT's leading defender, holds that CDT can "take into account information about what one is inclined or likely to do as evidence," but the article does not say how.

In this section I offer my own operational account. It is a synthesis of ideas from the literature (interventionist causal models; Harper's ratifiability; Skyrms's and Joyce's deliberational dynamics), not a restatement of the source.

### 5.1 Computing counterfactual probabilities via interventions

For agents with a causal model of the problem, i.e. a directed acyclic graph over variables including the decision node $A$, I propose reading $P(A\,\square\!\!\rightarrow O)$ as an *interventional* probability:

$$
P(A\,\square\!\!\rightarrow O) := P(O \mid \mathrm{do}(A)).
$$

If $K$ is a set of variables that are not causal descendants of $A$ and that block every back-door path from $A$ to $O$ (for example, the predictor's prediction or the king's charisma), the standard adjustment formula gives

$$
P(O\mid \mathrm{do}(A)) = \sum_k P(k)\,P(O\mid A, k).
$$

This is exactly Lewis's dependency-hypothesis formula. Values of $K$ play the role of dependency hypotheses, and "not under the agent's control" becomes "not a descendant of $A$ in the graph."

This reading largely dissolves the imaging regress. The similarity ordering is replaced by structural equations, and uncertainty about the structure itself is handled by a credence over graphs, to be averaged. Two cautions apply:

- **The reading is substantive.** It presupposes that decisions can be modelled as interventions, and that assumption is exactly what is strained by perfect predictors of the decision itself.
- **It leaves the hard question open.** It says to use $P(k)$, but not *which* $P(k)$: your credence before deliberation, or after you have settled what you will do?

### 5.2 Ratifiability

Harper's suggestion is to evaluate acts from the standpoint of having chosen them. Define the act-relative causal utility

$$
U_B(A) = \sum_k P(k\mid B) \sum_j P(O_j\mid A, k)\,D(O_j).
$$

This is the causal value of $A$, computed with the credences you would have if you had decided on $B$. An act $B$ is **ratifiable** if $U_B(B)\ge U_B(A)$ for all $A$, meaning that once you choose it, you do not wish you had done otherwise.

Applied to the cases:

- **Newcomb:** $P(k\mid \text{one-box})$ makes B likely full, but two-boxing is still better by \$1,000. Only two-boxing is ratifiable, and CDT's verdict stands.
- **Death in Damascus:** conditional on choosing $D$, Death is in $D$, so $A$ is better, and vice versa. *No pure act is ratifiable.*
- **Psychopath Button:** conditional on pressing, $P(\text{psycho})=0.9$, giving $U_{\text{press}}(\text{press}) = -89 < 0$, so pressing is not ratifiable. Conditional on not pressing, take $P(\text{psycho})=0.01$. Then $U_{\text{don't}}(\text{press}) = -1 + 9.9 = 8.9 > 0$, so not pressing is not ratifiable either.

Ratifiability therefore removes the embarrassing "press" verdict, but it can leave no option standing.

### 5.3 Deliberational equilibrium

Joyce's response, following Skyrms, treats deliberation as a dynamical process. Your credence $\pi$ about which act you will perform moves toward acts with higher current causal utility. Because $P(K)$ depends on $\pi$, the utilities move with it. You act at a fixed point, where every act still under consideration has equal causal utility.

In the Psychopath case, model

$$
P(\text{psycho}) = 0.9\,\pi + 0.01\,(1-\pi) = 0.01 + 0.89\,\pi,
$$

where $\pi$ is your credence that you will press. Pressing has causal utility $-100p + 10(1-p)$ with $p = P(\text{psycho})$. This is zero at $p = 1/11 \approx 0.091$, which corresponds to $\pi \approx 0.091$. Deliberation settles where Paul is about 91% confident he will *not* press.

If the final choice is read as following the equilibrium credence, or simply as "the act you are now almost sure to do," the refined CDT verdict is effectively *don't press*. That matches intuition, and no evidential reasoning has been used for the act's causal effects. In Death in Damascus the equilibrium is $\pi = \tfrac12$, which can be read as a coin flip that Death cannot exploit better than chance.

The cost of this approach is that the theory's output now depends on deliberational dynamics, on how $P(K)$ responds to $\pi$, and on how one interprets a mixed equilibrium. Critics (Egan, Spencer, Oesterheld–Conitzer) argue that in cases like the Adversarial Offer even equilibrium-CDT buys at a predictable loss.

To check this, suppose the seller predicts according to your equilibrium tendencies. At a symmetric equilibrium where you buy each box with equal probability, each box is full with probability at least $\tfrac12$, and buying still beats abstaining. So the money-pump survives the refinement.

### 5.4 Policies versus acts

The prompt asks about policies, and the source is silent on them. CDT evaluates whatever is chosen *at the time of choice*, by its causal consequences *from that time*.

If an agent can adopt a policy, such as a binding commitment to one-box, *before* the predictor forms the prediction, then adopting that policy does cause box B to be full. CDT itself then recommends adopting it. This is Meacham's theme of "binding."

The well-known CDT pattern is therefore: precommit to one-boxing if you can do so in time; two-box if you are asked only after the prediction. Critics read this time-inconsistency as a defect, since the agent would pay to constrain her future self. Defenders read it as the correct observation that once the prediction is past, there is nothing left to cause.

## 6. A procedure for unfamiliar cases

Collecting the above, here is a recipe. Steps 1–4 are standard CDT; steps 5–6 are my operationalization.

1. **List acts and outcomes**, and assign desirabilities $D(O)$.
2. **Draw the causal structure.** Separate variables downstream of the decision (its effects) from those that are not: predictions already made, others' choices, traits, physical states.
3. **Take the non-downstream variables as dependency hypotheses $K$.** Each act's causal utility is $U(A)=\sum_k P(k)\sum_j P(O_j\mid A,k)D(O_j)$.
4. **If $P(k)$ does not depend on your act choice,** as with the apple, stop: choose $\arg\max U$. CDT and EDT agree.
5. **If $P(k)$ is correlated with your choice** (predictors, twins, self-diagnosing acts), check ratifiability. If exactly one act is ratifiable, choose it; Newcomb gives two-boxing.
6. **If no act, or several, are ratifiable,** model $P(k)$ as a function of your credence $\pi$ over acts. Find the deliberational equilibria, and act on the one your deliberation reaches.
7. **If you can choose a policy before the correlated state is fixed,** evaluate the policy causally from that earlier time, since it may now be among the causes.

Some quick checks:

- **Medical "smoking lesion" cases.** A gene causes both a craving and a disease. If the act does not cause the disease, CDT says indulge. This is the Bathsheba structure.
- **Voting in large elections.** CDT counts only your causal influence on the outcome, which is tiny, plus any direct value of voting. EDT may count the correlation with like-minded voters, as in the twin prisoner's dilemma.
- **Bets against a perfect predictor of you.** Expect instability (steps 5–6) and possible exploitability (Section 4.4).

## 7. Assessment

**What the source establishes:**
- CDT's formal core, $U(A) = \sum_j P(A\,\square\!\!\rightarrow O_j)D(O_j)$.
- Its non-equivalence to EDT, via Lewis's triviality result.
- The Gibbard–Harper independence condition under which the two coincide.
- The standard verdicts: send for Bathsheba, two-box in Newcomb.
- The main lines of criticism: underspecification of counterfactual probabilities, Egan's counterexamples, and the money-pumps of Spencer and of Oesterheld–Conitzer.
- Joyce's defence.

**What I have added:**
- The derivation of the Gibbard–Harper lemma from CEM and centering.
- The interventionist reading of counterfactual probability as a way to make CDT computable.
- The ratifiability and deliberational-equilibrium machinery as a concrete version of Joyce's claim that CDT can use evidence about one's own inclinations.
- The worked Psychopath equilibrium at $\pi \approx 0.09$.
- The observation that the Adversarial Offer exploitation survives equilibrium refinement.
- The policy/precommitment analysis.

These are reasonable reconstructions, but none is uniquely mandated by the source.

## 8. Conclusion

CDT replaces "what would this act tell me?" with "what would this act do?" Formally, it weights outcomes by probabilities of counterfactuals. In Lewis's form, these are unconditional credences over causal dependency hypotheses combined with act-conditional outcome chances. That single change explains its successes: it refuses to manage the news in the Bathsheba and smoking-lesion cases. It equally explains its notorious verdicts: two-boxing in Newcomb, and instability or exploitability when the world contains accurate predictors of the agent's own choice.

The theory's main unfinished business is the one the reference article flags: how to compute counterfactual credences, and in particular which credences about oneself to hold fixed during deliberation. Interventionist models answer the first question well. Ratifiability and deliberational dynamics give a principled, if contested, answer to the second.

Whether the remaining exploitability of CDT agents is a refutation or simply the price of reasoning only about what one can affect remains an open question in decision theory.

## References

- Egan, A. (2007). "Some counterexamples to causal decision theory." *Philosophical Review* 116: 93–114.
- Gibbard, A. & Harper, W. (1981). "Counterfactuals and two kinds of expected utility." In *Ifs*, 153–190.
- Joyce, J. M. (2012). "Regret and instability in causal decision theory." *Synthese* 187: 123–145.
- Lewis, D. (1976). "Probabilities of conditionals and conditional probabilities." *Philosophical Review* 85: 297–315.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59: 5–30.
- Oesterheld, C. & Conitzer, V. (2021). "Extracting money from causal decision theorists." *Philosophical Quarterly* 71(4).
- Wikipedia contributors, "Causal decision theory," revision 1381555528 (CC BY-SA 4.0).