# Causal Decision Theory: Acting on What You Can Change

## 1. The core idea

Decision theory asks which of several available actions a rational agent should choose. The standard answer is to maximize expected utility. That answer leaves open what the "expectation" is taken *with respect to*. **Causal decision theory** (CDT) gives a definite reply: you should choose the action that **causes** the best outcome in expectation. Its main rival, **evidential decision theory** (EDT), recommends the action that would be the best *news*: the act whose performance would most raise your expectation of good outcomes, whether or not it brings them about.

In most ordinary decisions the two theories agree, because acts usually are evidence of good outcomes exactly when they cause them. They come apart when an act is *correlated* with outcomes through some channel other than its own causal influence, typically a common cause or a predictor. This essay sets out the formal machinery, works through the standard cases with numbers, and then turns to the main unresolved question: which credences CDT should "hold fixed". For that question I propose an operational procedure.

As the brief requires, I mark the boundary between source material and my own additions. The reference article I am drawing on supplies the Gibbard–Harper formula, Lewis's triviality result and imaging proposal, and the following examples:

- Bathsheba,
- Newcomb,
- the twin prisoner's dilemma,
- Death in Damascus,
- the Adversarial Offer,
- the Psychopath Button.

The numerical parameters in the worked examples, the interventionist reformulation, and the ratifiability-based decision procedure are my own presentation. They draw on the wider literature but are not claims made by the source.

## 2. An informal warm-up

Suppose you are deciding whether to eat an apple that may be good or bad. Eating a good apple makes you happy and eating a bad one makes you sad, but you do not know which kind this apple is. You therefore cannot know the causal consequence of eating it. You can, however, compute its *expected* causal consequence. That depends on three things:

- how likely you think it is that the apple is good;
- how happy a good apple makes you;
- how sad a bad apple makes you.

Set the utilities at $+5$ for a good apple, $-3$ for a bad one, and $0$ for not eating, with $P(\text{good}) = 0.6$. Then

$$
U(\text{eat}) = 0.6(5) + 0.4(-3) = 1.8 > 0 = U(\text{abstain}).
$$

The crucial feature is that the state of the apple is *not affected by your choice*, and it is also not *evidentially* affected: deciding to eat tells you nothing about whether the apple is good. Here CDT and EDT agree. The rest of this essay concerns what happens when the second condition fails but the first still holds.

## 3. The formal theory

### 3.1 Gibbard and Harper: probabilities of counterfactuals

Gibbard and Harper (1981) define the causal expected utility of an act $A$ as

$$
U(A) = \sum_j P(A \,\square\!\!\rightarrow O_j)\, D(O_j).
$$

Here the outcomes $O_j$ are mutually exclusive and jointly exhaustive, $D(O_j)$ is the desirability of outcome $O_j$, and $A \,\square\!\!\rightarrow O_j$ is the counterfactual conditional "if I were to do $A$, $O_j$ would obtain." (The source writes this as $A \to O_j$.) The agent weighs each outcome by her credence that the act *would bring it about*.

EDT instead uses the conditional probability of the outcome given the act:

$$
V(A) = \sum_j P(O_j \mid A)\, D(O_j).
$$

If $P(A \,\square\!\!\rightarrow O_j)$ always equalled $P(O_j\mid A)$, the two theories would coincide. Lewis (1976) showed that no conditional connective can satisfy this identity in general, except for trivial probability functions. So the two quantities are genuinely different.

Gibbard and Harper identify when they *do* coincide. Assume two things:

- **Centering / modus ponens.** Given $A$, the counterfactual $A \,\square\!\!\rightarrow O_j$ holds exactly when $O_j$ holds. That is, $A \wedge (A\,\square\!\!\rightarrow O_j) \equiv A \wedge O_j$.
- **Conditional excluded middle (CEM).** For each act, exactly one of the counterfactuals $A\,\square\!\!\rightarrow O_j$ is true, so they form a partition.

Now suppose that the counterfactual is probabilistically independent of the act. Then

$$
P(A\,\square\!\!\rightarrow O_j) = P(A\,\square\!\!\rightarrow O_j \mid A) = \frac{P(A \wedge O_j)}{P(A)} = P(O_j\mid A).
$$

Under these assumptions, CDT and EDT diverge **exactly when the act carries information about which counterfactuals are true**. CEM is controversial, which is one reason later authors reformulated the theory.

### 3.2 Lewis's dependency hypotheses

A formulation that I find more usable comes from Lewis (1981), who also proposed the imaging technique the source mentions. A **dependency hypothesis** $K$ is a maximally specific proposition about how outcomes depend causally on your acts. It settles everything that is outside your influence but relevant to what your acts would do. The dependency hypotheses form a partition $\mathcal{K}$, and causal expected utility becomes

$$
U(A) = \sum_{K\in\mathcal{K}} P(K) \sum_j P(O_j \mid A \wedge K)\, D(O_j). \tag{CDT}
$$

The evidential value has the same shape with one change:

$$
V(A) = \sum_{K\in\mathcal{K}} P(K\mid A) \sum_j P(O_j \mid A \wedge K)\, D(O_j). \tag{EDT}
$$

The whole disagreement comes down to one substitution: **CDT weights the background causal facts by their unconditional probability $P(K)$; EDT weights them by $P(K\mid A)$.** CDT treats the facts you cannot influence as fixed and asks what your act would do against them. EDT lets the act serve as evidence about those facts.

### 3.3 An interventionist reading (my addition)

The source notes that CDT "does not itself specify what algorithm to use to calculate the counterfactual probabilities." It mentions Lewis's *imaging* proposal: shift each world's probability to the nearest world where $A$ holds. It also records Shaffer's worry that imaging requires knowing what one would believe on supposing $A$, which invites a regress.

A practical way around this, which I am adding rather than taking from the source, is to represent the problem as a causal graph and to read the act as an *intervention*. Let $\mathbf{Z}$ be the variables that are causal ancestors of the act, or that share common causes with it, but that are not descendants of it. Then

$$
P(A \,\square\!\!\rightarrow O) \approx P(O \mid \mathrm{do}(A)) = \sum_{\mathbf{z}} P(\mathbf{z})\, P(O \mid A, \mathbf{z}).
$$

This is formally the same as (CDT), with the configurations $\mathbf{z}$ playing the role of dependency hypotheses. The recipe for a new case is short:

1. Draw the causal structure.
2. Cut every arrow *into* the act node.
3. Propagate effects downstream only.

Anything that is not downstream of the act keeps its unconditional distribution. This does not dissolve every philosophical worry, because one still needs the right graph. It does turn "probability of a counterfactual" into a computation that a reader can carry out.

## 4. Where CDT and EDT diverge

### 4.1 King David and Bathsheba

Gibbard and Harper's own example works as follows. Charisma is fixed by genes and upbringing. Charismatic kings tend to act justly, and they rarely face successful revolts. Uncharismatic kings tend to act unjustly and often face revolts. However, unjust acts do not *cause* revolts; the revolts come from an uncharismatic king's "sneaky, ignoble bearing." David wants Bathsheba but knows that summoning her is unjust.

Choose some illustrative parameters:

| Parameter | Value |
|---|---|
| Prior probability David is charismatic | $0.5$ |
| $P(\text{send}\mid \text{charismatic})$ | $0.2$ |
| $P(\text{send}\mid\text{uncharismatic})$ | $0.9$ |
| $P(\text{revolt}\mid\text{charismatic})$ | $0.1$ |
| $P(\text{revolt}\mid\text{uncharismatic})$ | $0.8$ |
| Utility of Bathsheba | $+10$ |
| Utility of revolt | $-50$ |

**CDT.** The dependency hypotheses are {charismatic, uncharismatic}, and their probabilities stay at the prior. The probability of revolt is therefore $0.5(0.1)+0.5(0.8)=0.45$ whatever David does. This gives

$$
U(\text{send}) = 10 - 50(0.45) = -12.5, \qquad U(\text{abstain}) = -22.5.
$$

Sending wins, and by exactly $10$, the value of Bathsheba. The same margin holds at *any* prior.

**EDT.** Conditioning on the act changes David's view of his own charisma. First, $P(\text{char}\mid\text{send}) = 0.1/0.55 \approx 0.18$. So $P(\text{revolt}\mid\text{send}) \approx 0.18(0.1)+0.82(0.8)\approx 0.67$, and $V(\text{send})\approx 10-33.6 = -23.6$. Second, $P(\text{char}\mid\text{abstain}) = 0.4/0.45\approx 0.89$. So $P(\text{revolt}\mid\text{abstain})\approx 0.18$, and $V(\text{abstain})\approx -8.9$. EDT says abstain.

The source reports that most philosophers side with CDT here. Abstaining would amount to "managing the news" about a trait David cannot change. Structurally the case is the "smoking lesion" familiar from the literature: a common cause produces both the act and the bad outcome.

### 4.2 Newcomb's problem

A predictor that is 99% reliable has already placed \$1,000,000 in opaque box B if it predicted you would take only B, and nothing otherwise. Transparent box A holds \$1,000. Let $q$ be your credence that B is full.

**CDT.** The prediction is already fixed, so $q$ does not depend on the act:

$$
U(\text{two}) = q(1{,}001{,}000) + (1-q)(1{,}000), \qquad U(\text{one}) = q(1{,}000{,}000).
$$

Two-boxing comes out ahead by exactly \$1,000 for *every* $q$. This is a dominance argument. In graph terms, your disposition is a common cause of the prediction and the act. Intervening on the act cuts the link, so the prediction keeps its prior distribution.

**EDT.** Here $P(\text{full}\mid\text{one})=0.99$ and $P(\text{full}\mid\text{two})=0.01$:

$$
V(\text{one}) = 990{,}000, \qquad V(\text{two}) = 0.01(1{,}001{,}000)+0.99(1{,}000) = 11{,}010.
$$

The source presents Newcomb's problem as an early alleged counterexample to CDT. CDT agents predictably walk away with about \$1,000 while one-boxers collect about \$1,000,000. Philosophers remain divided. A common reply from causalists, found in the wider literature (Lewis's "Why ain'cha rich?") rather than in the source, is that the predictor rewards an *irrational disposition*. On this reply the CDT agent loses because of who she is, not because of what she does at the moment of choice. Whatever one makes of that reply, the formal verdict is clear.

### 4.3 The twin prisoner's dilemma

Lewis (1979) observed that a prisoner's dilemma played against a near-copy is a Newcomb problem. Your twin's choice is strongly *correlated* with yours, because you share a common cause, but it is not *caused* by yours. CDT holds fixed your credence $q$ that the twin cooperates. Defection dominates for every $q$, so CDT defects. EDT cooperates, because cooperating is excellent evidence that the twin cooperates.

**A rule of thumb for unfamiliar cases.** If the act's correlation with a good state runs entirely through a common cause or a past prediction, CDT ignores that correlation. Whenever the act dominates causally, CDT recommends it.

## 5. The open problem: which credences are held fixed?

Formula (CDT) requires the agent's unconditional credences $P(K)$. Those credences may themselves depend on what the agent expects to do. When states are correlated with acts through a predictor, P(K) shifts as the agent's view of her own likely choice shifts. Egan (2007), as the source summarizes him, locates CDT's trouble exactly here. On his account, CDT does not follow "do what you expect will bring about the best results." It follows "do whatever has the best expected outcome, *holding fixed our initial views* about the causal structure," and it is the holding-fixed that misfires.

### 5.1 Death in Damascus

Death predicts where you will be tomorrow and waits there. Its reliability is $r=0.9$. You can go to Damascus or Aleppo. Utility is $1$ if you live and $0$ if you meet Death. Let $p$ be your current credence that you will go to Damascus. Then

$$
P(\text{Death in Damascus}) = rp + (1-r)(1-p) = 0.1 + 0.8p.
$$

The causal expected utilities are

$$
U(\text{Dam}) = 0.9 - 0.8p, \qquad U(\text{Al}) = 0.1 + 0.8p.
$$

Damascus is better if and only if $p<1/2$. If you lean toward Damascus, Aleppo looks better; if you lean toward Aleppo, Damascus looks better. The recommendation is **unstable**. Whichever act you settle on, the theory tells you, once you have settled, that you should have chosen the other.

### 5.2 Ratifiability and deliberational equilibrium (my operational proposal)

The source says only that Joyce, CDT's most prominent modern defender, holds that CDT can take into account "information about what one is inclined or likely to do as evidence." I propose making this precise along the lines of Jeffrey, Harper, Skyrms, and Joyce.

**Definition (ratifiability).** For acts $A, B$ define

$$
U_A(B) = \sum_K P(K\mid A)\sum_j P(O_j\mid B\wedge K)\,D(O_j).
$$

This is the causal value of $B$, computed with the credences you would have *on learning that you had decided on $A$*. Act $A$ is **ratifiable** if $U_A(A)\ge U_A(B)$ for all $B$.

**Procedure.**

1. Compute $U$ via (CDT) for your current credences $p$ about your own choice.
2. Shift $p$ toward the acts with higher $U$, in the manner of Skyrms's deliberational dynamics.
3. Update $P(K)$ accordingly and repeat.
4. Stop at an **equilibrium** $p^*$, meaning a credal state in which every act you assign positive probability has maximal causal utility.
5. Choose an act in the support of $p^*$. If you have a randomizing device that the predictor cannot anticipate, carry out $p^*$ with it.

Under mild continuity assumptions an equilibrium always exists, by a fixed-point argument. If an act is strictly ratifiable, it is the equilibrium.

In Death in Damascus, $p^*=1/2$. At that point both cities have utility $0.5$. A coin that Death cannot predict guarantees exactly this, and that is arguably the best one can do. Without such a coin, CDT with ratifiability judges the two acts equally choiceworthy. This at least removes the regret loop.

The proposal is justified in two ways. First, it keeps CDT's core commitment: only causal consequences count, and states are never treated as manipulable. Second, it requires the agent's credences about the world to be consistent with her credences about her own decision. Simply freezing "initial" credences, which may be arbitrary, does not meet that requirement.

### 5.3 The Psychopath Button

Paul can press a button that kills all psychopaths. He would prefer a world without psychopaths, but he is confident that only a psychopath would press, and he much prefers living among psychopaths to dying. Egan reports that "pretty much everyone" says Paul should not press. Yet CDT seems to endorse pressing.

Here is an illustrative parameterization. The utility of pressing while not a psychopath is $+10$, of pressing while a psychopath is $-100$, and of not pressing is $0$. With $s = P(\text{psychopath})$,

$$
U(\text{press}) = 10(1-s) - 100s = 10 - 110s,
$$

which is positive if and only if $s<1/11$. If Paul begins with a low prior $s=0.01$, naive CDT tells him to press. This is Egan's counterexample.

Now apply the ratifiability procedure. Suppose being a psychopath strongly raises the propensity to press, so that $s(p) = 0.01 + 0.89p$, where $p$ is Paul's credence that he will press. Pressing is not ratifiable: conditional on pressing, $s\approx 0.9$ and $U\approx -89$. Not pressing is not ratifiable either: conditional on not pressing, $s\approx 0.01$ and pressing looks good.

Deliberation pushes $p$ upward from 0 until $s(p^*) = 1/11$, that is, $p^*\approx 0.09$. At that point both acts have causal value 0. The equilibrium leans heavily toward *not pressing*, but it still allows pressing as a tie. Joyce accepts this verdict. Egan regards even permitting the button as wrong.

My assessment is that ratifiability softens the counterexample without fully answering it. That is one of the genuinely open points in the debate.

## 6. Exploitation arguments

A newer line of criticism tries to show that CDT agents can be made to lose money. Spencer (2020), Oesterheld and Conitzer (2021), and Joyce (2020) all address versions of this argument.

### 6.1 The Adversarial Offer

Two boxes are for sale at \$1 each, and the buyer may take one or none. Yesterday the seller put \$3 in each box she predicted the buyer would *not* acquire. Her predictions are accurate with probability $0.75$.

**CDT.** Whatever was predicted, at least one box holds \$3. If "none" was predicted, both do. So for any credences, $E[\text{box}_1] + E[\text{box}_2]\ge 3$, and the better box has a causal expected value of at least $1.5 > 1$. Buying some box therefore always beats buying none. CDT never declines.

**The result.** The seller predicts which box the buyer takes with accuracy $0.75$. The buyer's expected return is $0.25(3) - 1 = -0.25$ per round, which is a profit for the seller. EDT sees this coming: $V(\text{buy box}_i) = 0.25(3)-1 = -0.25 < 0 = V(\text{none})$.

**With ratifiability.** The procedure from 5.2 does not escape here, because "buy nothing" is never causally optimal under any credal state. The equilibrium mixes the two boxes. If the buyer has an unpredictable randomizer, the seller's accuracy drops to $1/2$ per box, and the buyer's expectation becomes $0.5(3) - 1 = +0.5$. That is the CDT defender's natural reply. If the seller predicts even the randomization, the loss remains.

Oesterheld and Conitzer go further and argue that CDT agents are open to diachronic Dutch books. The source reports this argument; I do not develop it here.

## 7. A procedure for deciding unfamiliar cases

The following summarizes the theory as I would operationalize it. The ratifiability step and the use of randomization are my additions.

1. **List the acts and the outcomes**, and assign desirabilities $D(O_j)$.
2. **Identify the causal structure.** Determine which relevant variables are downstream of the act and which are not. Those that are not, including past predictions, common causes, and fixed traits, are the dependency hypotheses $K$.
3. **Compute $U(A) = \sum_K P(K)\sum_j P(O_j\mid A\wedge K)D(O_j)$**, using unconditional credences over $K$. Equivalently, compute $P(O\mid \mathrm{do}(A))$.
4. **Check for act–state correlation.** If $P(K)$ depends on your own expected choice, as with predictors or self-diagnosing traits, run the deliberational dynamics. Choose a ratifiable act, or an equilibrium mixture.
5. **Note dominance shortcuts.** If one act is causally better under every $K$, CDT recommends it immediately, and steps 3–4 are unnecessary. This covers Newcomb, the twin dilemma, and Bathsheba.
6. **Compare with EDT** to diagnose the case. If they agree, the case is uncontroversial. If they disagree, the disagreement traces exactly to $P(K)$ versus $P(K\mid A)$.

## 8. Conclusion

Causal decision theory turns a compelling slogan, "do what brings about the best results," into a precise formula. Weight each background causal possibility by your unconditional credence in it, and evaluate each act by what it would *produce* given that possibility. The contrast with EDT is a single substitution, $P(K)$ in place of $P(K\mid A)$. This substitution yields CDT's characteristic verdicts:

- send for Bathsheba;
- take both boxes in Newcomb's problem;
- defect against a twin.

The source leaves two matters open, and both are real. The first is how to compute counterfactual probabilities at all. Imaging faces a regress worry; interventionist causal models offer a workable answer whenever a causal graph is available. The second, deeper, matter is which credences to hold fixed when an agent's beliefs about the world depend on her beliefs about her own choice. Death in Damascus, the Psychopath Button, and the Adversarial Offer all exploit this gap. Supplementing CDT with ratifiability and deliberational equilibrium gives a principled operational answer: it removes the regret loops and often recovers sensible verdicts. It does not fully defuse every counterexample, especially against predictors that cannot be fooled by randomization. Whether these remaining cases refute CDT, or show that some environments reward irrationality, is still contested.

## References

- Egan, A. (2007). "Some counterexamples to causal decision theory." *Philosophical Review* 116(1).
- Gibbard, A. & Harper, W. (1981). "Counterfactuals and two kinds of expected utility." In *Ifs*.
- Joyce, J. (2012). "Regret and instability in causal decision theory." *Synthese* 187.
- Lewis, D. (1976). "Probabilities of conditionals and conditional probabilities." *Phil. Review* 85; (1979) "Prisoners' dilemma is a Newcomb problem"; (1981) "Causal decision theory." *AJP* 59.
- Oesterheld, C. & Conitzer, V. (2021). "Extracting money from causal decision theorists." *Phil. Quarterly* 71(4).
- Wikipedia contributors, "Causal decision theory," rev. 1381555528 (source article, CC BY-SA 4.0).