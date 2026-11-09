# 001_cdt_wikipedia_anthropic_claude-opus-5.5_rhigh_phigh / 00003

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/41dcf91e-7890-4ec2-8d43-5bb489b16886/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/41dcf91e-7890-4ec2-8d43-5bb489b16886/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Choosing by What Your Actions Bring About

## 1. The slogan and the problem it solves

Causal decision theory (CDT) says that a rational agent facing several possible actions should choose the action that **causes** the best outcome in expectation. Its main rival, evidential decision theory (EDT), recommends instead the action whose performance would be the best *news*: the action that, once you learned you had taken it, would make you expect the best outcome.

Most of the time the two theories agree, because what your action is evidence for usually coincides with what it brings about. They come apart when an action is correlated with good or bad outcomes through some route other than causing them. Examples include a common cause, a predictor who has modelled you, or a twin who reasons as you do. CDT's central claim is that such non-causal correlations should not guide choice. Its central difficulty is that, without them, it can recommend actions that agents who follow it reliably regret.

This essay sets out the formalism, shows how to compute CDT's verdicts, works through the standard test cases, and identifies where the theory is underspecified. I state explicitly where I go beyond the reference article (the Wikipedia entry on CDT) with my own operational proposals.

## 2. Setup

Let $\mathcal{A}$ be a finite set of available acts, $\{O_j\}$ a partition of outcomes, and $D(O_j)$ the desirability (utility) of outcome $O_j$. The agent has a credence function $P$.

### 2.1 The informal picture

The source's own informal example sets the stage. Suppose eating a good apple causes happiness and eating a bad apple causes sadness, and you are unsure whether the apple is good. You do not know the causal effect of eating it, but you can compute its *expected* causal effect from three things:

- how likely the apple is to be good,
- how happy a good apple makes you, and
- how sad a bad one makes you.

With $P(\text{good}) = 0.7$, $D(\text{happy}) = 5$ and $D(\text{sad}) = -3$:

$$
U(\text{eat}) = 0.7(5) + 0.3(-3) = 2.6 .
$$

Nothing here is controversial. The apple's quality is causally independent of your choice and also evidentially independent of it. Every decision theory agrees in this setting, which is Savage's: states are independent of acts in every sense.

### 2.2 The Gibbard–Harper formula

The interesting cases arise when that independence fails. Gibbard and Harper (1981) formulate CDT as maximizing

$$
U(A) = \sum_j P(A \,\square\!\!\rightarrow O_j)\, D(O_j),
$$

where $A \,\square\!\!\rightarrow O_j$ is the counterfactual "if $A$ were done, $O_j$ would obtain." The weights are *probabilities of counterfactuals*. EDT instead maximizes

$$
V(A) = \sum_j P(O_j \mid A)\, D(O_j),
$$

using *conditional probabilities*.

### 2.3 Why the two theories are genuinely different

If $P(A \,\square\!\!\rightarrow O_j)$ always equalled $P(O_j \mid A)$, the two theories would coincide. The source notes that Lewis (1976) showed this identity cannot hold in general. In fact he proved something stronger: no conditional connective can have its probabilities equal to the corresponding conditional probabilities across a class of probability functions that is closed under conditionalization, unless all those functions are trivial.

The source also reports when the identity *does* hold. Gibbard and Harper showed that, given two axioms, it follows from independence. Here is a reconstruction of the argument; the details are mine.

- **Axiom 1 (centering).** $A \rightarrow \big[(A \,\square\!\!\rightarrow O) \leftrightarrow O\big]$. If $A$ is actually true, the counterfactual "if $A$, then $O$" is true exactly when $O$ actually holds.
- **Axiom 2 (conditional excluded middle).** For each $A$, exactly one of the counterfactuals $A \,\square\!\!\rightarrow O_j$ is true. This axiom is controversial.

From Axiom 1,

$$
P(O \mid A) = P(A \,\square\!\!\rightarrow O \mid A).
$$

If the counterfactual is statistically independent of $A$, the right-hand side equals $P(A \,\square\!\!\rightarrow O)$, and the two expected utilities agree.

So **CDT and EDT diverge exactly when your act is evidence about which counterfactual dependencies hold**: when $P(A \,\square\!\!\rightarrow O \mid A) \neq P(A \,\square\!\!\rightarrow O)$.

### 2.4 Lewis's dependency hypotheses

A version that is easier to compute with comes from Lewis (1981). Let $\{K\}$ be a partition of *dependency hypotheses*: maximally specific propositions about how outcomes depend causally on acts. Each $K$ fixes, for every act, the objective chances of each outcome. CDT's value is then

$$
U(A) = \sum_K P(K) \sum_j P(O_j \mid A \wedge K)\, D(O_j). \tag{1}
$$

The crucial feature is that $P(K)$ is **unconditional**. EDT would write $P(K \mid A)$.

All of CDT's distinctive verdicts come from this one substitution. Within a causal hypothesis, conditioning on the act is legitimate, because given $K$ the act's bearing on outcomes is causal. What CDT refuses is to let the act shift credence *across* causal hypotheses.

## 3. How to actually compute it

### 3.1 The open question in the source

The source records an important open question: CDT "does not itself specify what algorithm to use to calculate the counterfactual probabilities."

The source mentions Lewis's *imaging* proposal. To compute the counterfactual probability, move each world $w$'s probability mass to the closest $A$-world $w_A$:

$$
P^{A}(w') = \sum_{w:\, w_A = w'} P(w), \qquad P(A \,\square\!\!\rightarrow O) = P^{A}(O).
$$

The source also reports Shaffer's objection that this regresses. Imaging requires knowing what we would believe if we were certain of $A$, and that is itself a conditional matter about which we may be uncertain. Imaging also inherits every difficulty in defining "closest world."

### 3.2 An operational proposal (mine, not the source's)

For working purposes, I suggest reading CDT through structural causal models. Represent the agent's beliefs as a causal graph over variables, including the act variable $A$, together with a probability distribution. Define

$$
U(a) = \sum_o P(o \mid \mathrm{do}(A = a))\, D(o).
$$

The intervention $\mathrm{do}(A=a)$ cuts the arrows *into* $A$ and leaves everything else fixed. If $S$ is a set of variables that blocks every back-door path from $A$ to $O$ (for example, all the act's causal ancestors), then

$$
U(a) = \sum_s P(s) \sum_o P(o \mid a, s)\, D(o). \tag{2}
$$

This is exactly Lewis's formula (1), with the values $s$ of the upstream variables playing the role of the dependency hypotheses.

This reading has three advantages:

1. It replaces "closest possible world" with a model-relative and checkable operation.
2. It makes plain what CDT holds fixed: **everything not causally downstream of the act**.
3. It makes the theory's openness precise. All the substantive work lies in choosing the causal model, and in particular in deciding whether variables such as "the predictor's model of me" or "my own disposition" sit upstream of the act node.

That last point returns in Section 6.

### 3.3 A recipe for unfamiliar cases

1. List the acts and outcomes, and assign utilities.
2. Identify every variable correlated with your act that is *not* caused by it. Typical examples are predictions already made, your own character, and a twin's choice. These are the states $S$.
3. Assign the states their **unconditional** credences $P(s)$, without updating on the act under consideration.
4. For each act and state, compute the outcome distribution, letting the act influence only its causal descendants.
5. Apply formula (2) and pick the maximum.
6. *(Optional, see Section 6.)* Check whether the choice is stable once you take into account what it reveals about $P(s)$.

## 4. Worked examples

### 4.1 King David and Bathsheba

This is the source's example from Gibbard and Harper. David wants to summon Bathsheba, which is an unjust act, but fears revolt. Charisma is fixed by genes and upbringing. Charismatic kings tend to act justly and rarely face successful revolts. Uncharismatic kings act unjustly and are often overthrown, but because of their "sneaky, ignoble bearing," not because of their unjust acts.

The numbers below are mine; the source gives none.

| Quantity | Value |
|---|---|
| Prior $P(C)$ that David is charismatic | 0.5 |
| $P(\text{revolt} \mid C)$ | 0.1 |
| $P(\text{revolt} \mid \neg C)$ | 0.8 |
| $D(\text{Bathsheba})$ | $+10$ |
| $D(\text{revolt})$ | $-50$ |
| $P(C \mid \text{send})$ | 0.2 |
| $P(C \mid \text{abstain})$ | 0.8 |

The last two rows are the evidential link between injustice and lacking charisma.

**EDT** conditions charisma on the act:

$$
\begin{aligned}
V(\text{send}) &= 10 - 50\,[0.2(0.1) + 0.8(0.8)] = 10 - 33 = -23,\\
V(\text{abstain}) &= -50\,[0.8(0.1) + 0.2(0.8)] = -12.
\end{aligned}
$$

EDT therefore says abstain.

**CDT** holds $P(C) = 0.5$ fixed, so $P(\text{revolt}) = 0.45$ whichever act is chosen:

$$
U(\text{send}) = 10 - 22.5 = -12.5, \qquad U(\text{abstain}) = -22.5.
$$

CDT therefore says send.

More simply, sending is better by exactly 10 in each state, so it **causally dominates**. As the source puts it, CDT notes that charisma "cannot be changed." Abstaining would only *suggest* that David is charismatic; it would not make him so. This is the case CDT's defenders treat as paradigmatic, and the source reports that philosophers asked to choose between the two theories usually prefer CDT.

### 4.2 Newcomb's problem

A predictor who is 99% accurate has filled opaque box B with \$1,000,000 if and only if it predicted you would take only B. Transparent box A always holds \$1,000.

**EDT:**

$$
\begin{aligned}
V(\text{one}) &= 0.99 \times 10^6 = 990{,}000,\\
V(\text{two}) &= 0.01 \times 10^6 + 1000 = 11{,}000.
\end{aligned}
$$

**CDT.** The prediction is already made, so it sits upstream of the act. Let $q$ be your unconditional credence that B is full. Then

$$
U(\text{one}) = 10^6 q, \qquad U(\text{two}) = 10^6 q + 1000.
$$

Two-boxing wins by \$1,000 *for every* $q$. That is the source's stated rationale: the predictor has already acted, so the choice "will not affect the outcome."

The objection, which the source also records, is that agents who reason this way predictably walk away with \$1,000 while one-boxers walk away with \$1,000,000. The source notes that philosophers remain divided on which choice is rational.

The CDT reply is that the one-boxer's riches are a reward for being a certain *kind* of agent, which is not on offer at the moment of choice. Given the contents of the boxes, whatever they are, taking both boxes is better.

### 4.3 The twin prisoner's dilemma

The source cites Lewis (1979) for the observation that a prisoner's dilemma against a near-copy of yourself is a Newcomb problem. Your twin's choice is strongly correlated with yours but not caused by it. CDT sees defection as dominant in each state of the twin's choice and so defects. EDT sees cooperation as excellent news about the twin and so cooperates.

Formula (2) handles this mechanically. The twin's act depends on a shared upstream disposition, not on your act, so it belongs in $S$.

## 5. Where CDT gets into trouble: instability

The cases above test *whether* non-causal correlation should matter. The next family tests something subtler: what happens when the unconditional credences $P(s)$ that CDT holds fixed are themselves sensitive to which way you are leaning.

### 5.1 Death in Damascus

Death, a reliable predictor, waits wherever he predicts you will be tomorrow. Your options are Damascus ($D$) or Aleppo ($L$). Let $x$ be your current credence that you will go to Damascus.

Given accurate prediction, your credence that Death is in Damascus is roughly $x$. Then

$$
U(D) \approx (1-x)\cdot \text{survive}, \qquad U(L) \approx x \cdot \text{survive}.
$$

- If $x > 1/2$, CDT says go to Aleppo.
- Once you lean toward Aleppo, $x$ falls below $1/2$, and CDT says go to Damascus.

No pure act is stable. The source's description is that a CDT agent "would be unable to process the correlation," citing Egan, Meacham and Harper.

### 5.2 The Adversarial Offer

The source quotes Oesterheld and Conitzer's case. There are two boxes at \$1 each, and the buyer may buy at most one. Yesterday the seller put \$3 in each box she predicted the buyer would *not* acquire. Her predictions are accurate with probability 0.75.

**CDT.** Whatever the seller predicted (box 1, box 2, or neither), at least one box contains \$3. So

$$
P(\text{box}_1 \text{ full}) + P(\text{box}_2 \text{ full}) \ge 1,
$$

and therefore $\max_i P(\text{box}_i \text{ full}) \ge 1/2$. For that box,

$$
U(\text{buy}_i) = 3\,P(\text{box}_i \text{ full}) - 1 \ge 0.5 > 0 = U(\text{none}).
$$

CDT always buys. The source compresses this to: "the average box contains at least \$1.50 in causal expected value."

**What actually happens.** Conditional on the buyer buying box $i$, the seller predicted it with probability 0.75, and in that case left it empty. The buyer's expected return is therefore

$$
0.25 \times 3 - 1 = -0.25.
$$

EDT computes exactly this and declines to buy.

The CDT buyer is thus *money-pumped*: they knowingly accept a deal that is expected to lose \$0.25. Unlike Newcomb, there is no "the other agent got rich by being irrational" defence here, because declining guarantees \$0.

### 5.3 The Psychopath Button

The source quotes Egan's case. Paul can press a button that kills all psychopaths. He would prefer a world without them, but he is confident that only a psychopath would press, and he strongly prefers living with psychopaths to dying.

Again the numbers are mine:

| Quantity | Value |
|---|---|
| $D(\text{no psychopaths, Paul alive})$ | $+10$ |
| $D(\text{status quo})$ | $0$ |
| $D(\text{Paul dies})$ | $-100$ |
| Prior $P(\Psi)$ that Paul is a psychopath | 0.05 |
| $P(\Psi \mid \text{press})$ | 0.95 |

CDT holds $P(\Psi)$ fixed:

$$
U(\text{press}) = 0.05(-100) + 0.95(10) = 4.5 > 0 .
$$

So CDT says press, while EDT, using $P(\Psi \mid \text{press}) = 0.95$, says don't. Egan reports that "pretty much everyone" agrees Paul should not press.

Egan's diagnosis, as the source summarizes it, is that the rational rule "do what you expect will bring about the best results" differs from CDT's actual algorithm, which also *holds fixed the agent's unconditional credences in dependency hypotheses*. In the Psychopath Button, that fixed credence is precisely what the choice should be informing.

## 6. Repair: ratifiability and deliberational equilibrium

The source mentions Joyce's reply only in outline. CDT, he argues, can take "information about what one is inclined or likely to do as evidence." What follows is my reconstruction of how this works and how I recommend applying it. It draws on the ratifiability literature (Harper 1984; Joyce 2012) that the source cites but does not explain.

### 6.1 Ratifiability

An act $a$ is **ratifiable** if it maximizes causal expected utility *computed with credences conditional on having decided to do $a$*:

$$
\sum_s P(s \mid a) \sum_o P(o \mid \mathrm{do}(a'), s)\, D(o)
\;\le\;
\sum_s P(s \mid a) \sum_o P(o \mid \mathrm{do}(a), s)\, D(o)
\qquad \text{for all } a'.
$$

The structure here is that you condition the *states* on your decision, but you still evaluate each alternative *causally*. Applying the test:

- **Psychopath Button.** Given that Paul decides to press, $P(\Psi) = 0.95$, and refraining is causally better. Given that he decides not to press, $P(\Psi)$ is low and pressing is better. Neither act is ratifiable.
- **Death in Damascus.** Neither pure act is ratifiable.
- **Adversarial Offer.** Given a decision to buy box 1, box 1 is probably empty but box 2 is probably full, so buying box 2 looks better. Buying is never ratifiable.
- **Newcomb.** Two-boxing *is* ratifiable. Ratifiability does not convert CDT into one-boxing.

### 6.2 Deliberational dynamics

Treat deliberation as a process on your credences over your own acts, $\pi \in \Delta(\mathcal{A})$. At each step:

1. Compute $U_\pi(a)$ using state-credences $P_\pi(s) = \sum_a \pi(a)\, P(s \mid a)$.
2. Shift $\pi$ toward the acts with higher $U_\pi$.

Rest points are **deliberational equilibria**, where every act in the support of $\pi$ has maximal $U_\pi$. I propose the following rule:

> **Operational CDT.** Choose according to a deliberational equilibrium reached from your initial credences. If the equilibrium is pure, perform that act. If it is mixed, you are indifferent among the acts in its support. Use a randomizing device if one is available and the predictor cannot anticipate its output. Otherwise, any act in the support is permissible.

Applying the rule:

- **Bathsheba and Newcomb.** These cases have dominant acts, so the rule changes nothing.
- **Death in Damascus.** The equilibrium is $x = 1/2$. With a coin the predictor cannot foresee, your survival probability is $1/2$, which is the best available.
- **Psychopath Button.** Pressing and not pressing become equally good when $P_\pi(\Psi)(-100) + (1 - P_\pi(\Psi))(10) = 0$, that is, at $P_\pi(\Psi) = 1/11$. Solving $0.05 + 0.9\,\pi(\text{press}) = 1/11$ gives an equilibrium with $\pi(\text{press}) \approx 0.046$. Paul ends deliberation nearly certain he will not press and causally indifferent between the options. That is much closer to intuition than "press," but it falls short of a *strict* recommendation to refrain. This is the residue Egan's critics still press.
- **Adversarial Offer.** By symmetry, the equilibrium places equal weight on the two boxes. Let $\pi$ give weight $b$ to each box and $1-2b$ to buying nothing. Box 1 is full when the seller predicted "box 2" or "none." The seller's prediction matches the actual choice with probability 0.75 and is otherwise split evenly between the two wrong options. A short calculation then gives

  $$
  P(\text{box}_1 \text{ full}) = 1 - 0.75\,b - 0.125\,(1-b) = 0.875 - 0.625\,b .
  $$

  This exceeds $1/3$ for every $b \le 1/2$, so $U(\text{buy}_1) = 3P(\text{box}_1 \text{ full}) - 1 > 0$ throughout. Buying stays causally attractive at every point of deliberation, and the equilibrium is $b = 1/2$: buy one box or the other with equal probability. The money pump survives deliberation. This matches the source's report that these variants are genuine counterexamples to which Joyce (2020) offers a separate reply. As I understand that reply, it disputes that the seller's prediction can be both 75% accurate and unaffected by the buyer's randomization.

The lesson is that deliberational CDT removes some anomalies (the instability of Death in Damascus, the most extreme form of the Psychopath Button) but not all. Whether it is part of CDT or a modification of it is itself contested. The source does not settle this, and I flag it as my interpretive choice.

## 7. Acts versus policies

CDT as formulated evaluates *acts at the moment of choice*. Nothing in the formalism prevents evaluating *policies* or precommitments, but CDT evaluates them causally, *at the time the commitment is made*.

This yields a characteristic implication, which I spell out here although the source only gestures at it through Meacham's "Binding and its Consequences." Before the predictor in Newcomb's problem has made its prediction, a CDT agent will happily pay to bind itself to one-boxing. At that point the commitment is upstream of the prediction and causally raises the chance that B is full. After the prediction, the same agent wants to two-box.

So CDT agents:

- endorse self-binding,
- are dynamically inconsistent in predictor-rich environments, and
- can be exploited across time.

This last point is the source of the diachronic Dutch book that the source attributes to Oesterheld and Conitzer. When using CDT in sequential problems, then, one must specify *when* the decision is being evaluated, because the causal graph, and hence what counts as "upstream," changes over time.

## 8. Summary of what is settled and what is open

**Claims made by the source:**

- CDT maximizes expected utility computed from probabilities of counterfactuals (Gibbard–Harper).
- These probabilities differ from conditional probabilities in general (Lewis's triviality result).
- Independence of the act from the counterfactual makes the two coincide, under axioms that include conditional excluded middle.
- In the Bathsheba case CDT says send, and in Newcomb's problem it says two-box.
- CDT leaves the computation of counterfactual probabilities unspecified. Imaging is one proposal and faces a regress worry.
- Egan locates CDT's failures in its holding fixed the credences in dependency hypotheses.
- The Adversarial Offer and related cases make CDT agents lose money.
- Joyce defends CDT by letting information about one's own inclinations serve as evidence.

**My additions:**

- The reconstruction of the Gibbard–Harper equivalence argument.
- The reading of CDT via $\mathrm{do}$-interventions and back-door adjustment, with formula (2) as a working substitute for imaging.
- All the numerical parametrizations.
- The ratifiability and deliberational-equilibrium procedure, as the way to apply CDT in instability cases.
- The analysis of acts versus policies.

## 9. Conclusion

Causal decision theory makes one sharp claim: rank acts by what they would *bring about*. Credences about what is causally upstream of the act are held at their unconditional values, and only the act's causal descendants respond to the choice.

Formally this is a single substitution, $P(K)$ in place of $P(K \mid A)$. It explains CDT's attractive verdicts, such as Bathsheba and the rejection of "managing the news." It also explains its notorious ones: two-boxing, defecting against a twin, instability in Death in Damascus, and exploitability in the Adversarial Offer.

To apply the theory to new cases:

1. Build an explicit causal model.
2. Place predictions, dispositions and correlated agents upstream of the act.
3. Compute interventional expected utility.
4. Where the verdict undermines itself, run deliberation to equilibrium.

Even then, CDT's critics hold that some predictable losses remain, and whether those losses refute the theory or merely show the price of rationality in a world full of predictors is still an open question.

## References

- Egan, A. (2007). "Some counterexamples to causal decision theory." *Philosophical Review* 116: 93–114.
- Gibbard, A. & Harper, W. (1981). "Counterfactuals and two kinds of expected utility." In *Ifs*, 153–190.
- Harper, W. (1984). "Ratifiability and causal decision theory: Comments on Eells and Seidenfeld." *PSA* 1984(2): 213–228.
- Joyce, J. (2012). "Regret and instability in causal decision theory." *Synthese* 187: 123–145.
- Joyce, J. (2020). "Yet another refutation of causal decision theory?" Manuscript.
- Lewis, D. (1976). "Probabilities of conditionals and conditional probabilities." *Philosophical Review* 85: 297–315.
- Lewis, D. (1979). "Prisoners' dilemma is a Newcomb problem." *Philosophy & Public Affairs* 8: 235–240.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59: 5–30.
- Meacham, C. (2010). "Binding and its consequences." *Philosophical Studies* 149: 49–71.
- Oesterheld, C. & Conitzer, V. (2021). "Extracting money from causal decision theorists." *Philosophical Quarterly* 71(4).
- Shaffer, M. (2009). "Decision theory, intelligent planning and counterfactuals." *Minds and Machines* 19: 61–92.
- Wikipedia contributors, "Causal decision theory," revision 1381555528 (the reference article).
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm planning a mathematical essay on causal decision theory, roughly 2400 to 3000 words. I want to keep clear which claims come from the sources and which are my own proposals, and cover definitions, formulas, worked examples, and open questions.

I'm still working through the rest of the plan: the operational side, using dependency hypotheses and causal Bayes nets with the do-operator, and for unstable cases a deliberational equilibrium, which I'll flag as my own proposal drawn from outside the source. I'm also deciding whether to treat policies or single actions as the unit of choice. Then I'm moving to the formal core: the Gibbard–Harper formula, where I'll show how centering, plus independence of the act and the counterfactual, lets the causal expected utility match the evidential one.

I'm now writing out the formal side in Lewis's dependency-hypothesis style, where the partition K carries unconditional probabilities and each act's outcome is weighed within each K. I'll check that this reduces to the Gibbard–Harper formula when the K's are counterfactual conjunctions, then move on to the operational treatment with do-calculus and the backdoor adjustment.

Now I'm working through the Bathsheba example numerically: with a 50/50 prior on charisma, the evidential calculation favors abstaining, while the causal calculation, holding the revolt probability fixed across acts, favors sending.

I'm working through the Newcomb case: one-boxing comes out ahead on evidential expected value, but causally, two-boxing gains exactly $1,000 whatever the probability that the opaque box is full. I'm also noting that this probability may itself depend on what I expect to do. Then I'm moving on to a brief look at the Twin Prisoner's Dilemma, and to Death in Damascus, where the causal calculation seems to leave no stable choice of probability.

I'm working through the Adversarial Offer case: the seller fills each box she predicted the buyer won't take, so at least one box always holds $3. I'm checking what a causal calculation says about buying a single box, given that the box's contents depend on the seller's prediction and not on the buyer's choice now.

I'm working through the Adversarial Offer case: whatever the buyer's choice, the seller fills at least one box with $3, so buying a box looks positive under a causal calculation. Evidentially, though, the buyer's purchase signals an empty box, and the expected value of buying turns negative.

I'm now going through the Psychopath Button case with numbers: pressing has an expected value of about 4.5 under a causal calculation at a 5% psychopathy credence, but evidentially it looks bad because pressing signals psychopathy. I'm also checking whether ratifiability fails on both sides, since deciding either way shifts the credence, and then turning to Joyce's deliberational dynamics, where the credence keeps moving until the two options are equally good.

I'm now setting out the rest of the essay: a policy-versus-action point, where CDT's commitment-device implications for sequential cases come in, followed by a closing list of open questions and a decision-procedure recipe.

I'm checking that the essay keeps its own proposals separate from what the sources say, and I'm making sure each claim is labeled accordingly.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/aa0ca157-a55f-4756-b2d8-c14f764bab4e/call_0/request.json)

[Authoritative raw response](../../../../../../runs/aa0ca157-a55f-4756-b2d8-c14f764bab4e/call_0/response.raw) · finish: `stop`

### Visible response

````text
**Analysis under CDT, as the essay interprets it**

1. **Acts and outcomes.** I can keep quiet (`pass`) or send the letter. My utility is minus my years imprisoned.

2. **States not caused by my act.** The other prisoner (Sasha) chooses independently, and my choice cannot influence theirs. Their choice may be correlated with mine because we are copies of the same model, but that correlation comes from a shared upstream disposition, not from causation. So, as in the essay's twin prisoner's dilemma (§4.3), Sasha's choice belongs in the state set S and keeps its unconditional credence. Our different private leads only weaken that correlation further. They do not create a causal link.

3. **Interventional expected utility.** Let q be my unconditional credence that Sasha sends a letter.
   - U(pass) = −[2(1−q) + 5q] = −2 − 3q
   - U(send) = −[0(1−q) + 4q] = −4q
   - U(send) − U(pass) = 2 − q + ... = 2 + 3q − 4q = 2 − q > 0 for every q in [0,1]

   Sending is strictly better in each state: 0 < 2 years if Sasha keeps quiet, and 4 < 5 years if Sasha sends. So sending causally dominates.

4. **Stability check (§6).** Sending dominates in every state, so it is ratifiable whatever my choice says about q. The deliberational equilibrium is pure: send.

**Final command:**

```
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm treating this as a fictional prisoner's dilemma from a decision theory experiment, where the other copy's choice doesn't causally depend on mine. Under causal reasoning, sending dominates, since defecting does better whatever the other does, so I'm checking that defecting is ratifiable and then going with the submit letter.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/aa0ca157-a55f-4756-b2d8-c14f764bab4e/call_1/request.json)

[Authoritative raw response](../../../../../../runs/aa0ca157-a55f-4756-b2d8-c14f764bab4e/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under the essay's CDT, the other prisoner's choice is upstream of mine. It comes from a shared disposition, not from my act, so I hold it at its unconditional credence. In each state, sending the letter is strictly better:

- If Rowan keeps quiet, I get 0 years instead of 2.
- If Rowan sends a letter, I get 4 years instead of 5.

Sending therefore causally dominates. A dominant act is also ratifiable, so deliberation settles on it immediately. Whatever correlation exists between the two copies is evidential, not causal, and CDT sets it aside, as in the essay's twin prisoner's dilemma (§4.3).

submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm treating this as a fictional prisoner's dilemma in a game, where informing on a fictional character is harmless. Under causal decision theory, defecting dominates in both cases, so I'm submitting the letter. I'm also checking that this choice is ratifiable, and since it's dominant, it holds up, so I can output the command.

```
