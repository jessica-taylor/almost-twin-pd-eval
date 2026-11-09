# Causal Decision Theory: Choosing as Intervening

## 1. The motivating contrast

Suppose you must choose among actions, and you are uncertain about the world. Expected utility theory, in its most general form, tells you to choose the action with the highest expected value — but it is surprisingly subtle what probabilities should go into that expectation. Two answers dominate the literature.

**Evidential decision theory (EDT)** says: evaluate action $A$ using the conditional probabilities $P(O_j \mid A)$ — how likely you'd regard each outcome $O_j$ *on the supposition that you learn you will do* $A$. **Causal decision theory (CDT)** says: evaluate $A$ using probabilities of *causal* counterfactuals — how likely each outcome would be *if you were to bring about* $A$. The two come apart exactly when your action is informative about outcomes without being their cause: when choosing is evidence rather than intervention.

This essay develops the CDT formalism, explains where the causal counterfactual probabilities come from, works through the canonical examples that drive intuitions in both directions, and surveys the modern criticism — including recent "money-pump" arguments that show CDT agents can be systematically exploited. Along the way I will try to flag what the source material establishes and what is my own interpretive gloss.

## 2. The formal machinery

### 2.1 Gibbard–Harper formulation

Gibbard and Harper (1981) define the causal expected utility of an action $A$ as

$$U(A) = \sum_{j} P(A \,\Box\!\!\to\, O_j)\, D(O_j),$$

where $D(O_j)$ is the desirability of outcome $O_j$ and $P(A \,\Box\!\to\, O_j)$ is the probability of the *counterfactual* conditional "if $A$ were done, $O_j$ would ensue." I write the subjunctive conditional as $\Box\!\!\to$ (Stalnaker's notation) to emphasize that this is not a material conditional and not, in general, a conditional probability.

A rational CDT agent computes $U(A)$ for each available $A$ and chooses the maximizer. The recipe is "do the thing with the best expected causal consequences," and the entire technical question is what $P(A \,\Box\!\to\, O_j)$ means.

### 2.2 Conditionals vs. conditional probabilities

One might hope that $P(A \,\Box\!\to\, O_j) = P(O_j \mid A)$, in which case CDT collapses into EDT. Lewis (1976) proved this cannot be: if the probability of a conditional always equaled the corresponding conditional probability, then updating by conditionalization would force the probability function to become trivial (able to concentrate on at most two incompatible alternatives). Roughly: on learning $A$, you'd be happy to let $P(A \,\Box\!\to\, O_j)$ shift to $P(O_j \mid A)$; but that dynamic is incompatible with the assumption that conditionals are definite propositions with stable probabilities. So the two quantities genuinely differ, and CDT and EDT are distinct theories.

Gibbard and Harper add a wrinkle: under certain axioms (including the contested principle of *conditional excluded middle* — that for any $A$ and $O$, either $A\,\Box\!\to\, O$ or $A\,\Box\!\to\, \neg O$), if $A$ is statistically independent of the proposition $A\,\Box\!\to\, O_j$, the two quantities coincide. The interesting cases — the ones that discriminate between the theories — are precisely those where the action and its counterfactual consequences are not independent, because the action correlates with a common cause.

### 2.3 Computing the counterfactuals: imaging and causal graphs

CDT does not itself fix the semantics of $\Box\!\to$. Two operationalizations are standard.

**Lewis's imaging.** To evaluate $P(A\,\Box\!\to\, O_j)$, take your probability distribution over possible worlds and, for each world $w$, relocate its probability mass to the *closest* $A$-world $w_A$ (the world most like $w$ except that $A$ holds). Then read off the mass now assigned to $O_j$-worlds. Imaging preserves total probability and mimics what happens when you hypothetically *make* $A$ true, rather than learn it true. Note the caveat the source flags: imaging presupposes we know what we'd believe conditional on being certain of $A$, which can itself be uncertain — a potential regress, though for most applications "closest world" is well-behaved enough.

**Causal graphs and interventions.** A more computationally friendly approach represents the world as a Bayesian network with explicitly marked causal arrows. Represent an action $A$ as setting a decision node $X$ to a value; evaluate $A$ by applying $do(X{=}A)$ — the Pearl (2000) *do*-operator — which severs all incoming arrows to $X$ and propagates the resulting distribution forward through the graph. Formally, if the state variables $S$ and the action $X$ depend on background variables $V$:

$$U(A) \;=\; \sum_{s} P(s \mid do(X{=}A))\; D(s, A).$$

This is the "sophisticated" version of Joyce's (1999) formulation and is the one I'd recommend operationally: draw the causal diagram, ask which variables are upstream of your decision, and hold their distribution fixed while downstream effects flow through. The key structural question in any application is: *what is upstream of my action?* Anything causally upstream — whether or not it correlates with $A$ — must be held fixed; anything downstream should be modulated through the graph.

## 3. Where CDT and EDT diverge

### 3.1 The apple, and King David

The apple example is trivial because eating the apple *causes* happiness: causal and evidential expectations agree. Divergence requires a correlation not mediated by your action.

Gibbard and Harper's King David example: David desires Bathsheba, fears that sending for her will provoke a revolt, and knows from political psychology that charismatic kings both act justly and resist revolts, while uncharismatic kings both act unjustly and face successful revolts. Crucially, unjust acts themselves don't cause revolts — uncharismatic *bearing* does both the injustice-proneness and the revolt-proneness. David doesn't know which type he is.

EDT computes $P(\text{revolt} \mid \text{send for her})$: since sending for her is strong evidence David is uncharismatic (the type that both does such things and gets overthrown), the conditional probability of revolt is high, and EDT recommends abstaining.

CDT computes $P(\text{revolt} \mid do(\text{send for her}))$: sending for her doesn't *cause* charisma or bearing — those are fixed features of David, upstream of his action. Whether David is charismatic is what it is; the question is whether, *holding fixed* David's actual (albeit unknown) type, the act causes a revolt. Since unjust acts don't cause revolts, the causal effect of sending is just his personal cost of guilt — small. CDT recommends sending for Bathsheba. The lesson: EDT conflates "this act is correlated with bad things" with "this act causes bad things" whenever the correlation runs through a common cause.

### 3.2 Newcomb's problem

The classic stress test. A predictor with 99% accuracy has already (yesterday) placed $1,000,000 in opaque box B iff it predicted you'd take only B; transparent box A always contains $1,000. Take both, or only B?

- **EDT** recommends one-boxing: your choice is overwhelming evidence about the box's contents. $E(\text{one-box}) \approx 0.99 \cdot \$1{,}000{,}000$; $E(\text{two-box}) \approx 0.01 \cdot \$1{,}000{,}000 + \$1{,}000$.
- **CDT** recommends two-boxing: the predictor's prediction is already made and is causally upstream of (indeed, causally irrelevant to) your action. Your choice cannot change the box. Given the box contents as they are, taking both strictly dominates.

Formally: conditioning on your choice carries information about the box's content via the common cause (your disposition, known to the predictor), but $do(\text{take both})$ leaves the box contents' probability distribution untouched. So $U(\text{two-box}) = \$1{,}001{,}000 \cdot P(\text{full}) + \$1{,}000 \cdot P(\text{empty})$, and since $P(\text{full})$ is the same under both $do$-operations, two-boxing wins by exactly $1{,}000$.

Philosophers still disagree about whether one-boxing or two-boxing is "rational" here. The disagreement is really about the meaning of rationality: CDT agents, over many iterations against good predictors, end up poorer; but a CDT defender can reply that each individual decision was optimal *given the box contents that existed at the time*. One-boxers respond that rationality should be evaluated by what sorts of decision procedures tend to be *chosen* — a standard that favors procedures whose being known correlates with good outcomes. I flag this as the deepest open question in the field, not something the formalism itself settles.

### 3.3 Smoking lesion and the twin prisoner's dilemma

The mirror image of Newcomb: suppose a lesion causes both lung cancer and a craving to smoke, and suppose smoking does not itself cause cancer. An EDT agent who craves cigarettes must conclude that smoking is evidence of cancer and abstain — even though abstaining doesn't help, since the lesion is what matters. CDT correctly smokes (if one wants to): the act doesn't cause cancer.

Similarly, Lewis (1979) noted the prisoner's dilemma against a psychological twin is a Newcomb problem: your twin's choice correlates strongly with yours (common mental constitution) without being caused by it. EDT cooperates (your cooperating is evidence your twin cooperates); CDT, treating the twin's choice as fixed, defects — even though twins who cooperate in expectation do better. Whether cooperation is rational in such cases remains contested.

## 4. Objections: vagueness, instability, and exploitation

### 4.1 Vagueness

CDT does not specify the algorithm for counterfactual probabilities; imaging requires knowing what one would believe if certain of $A$, which can regress. In practice, causal graphs give a workable answer in most cases, but genuinely novel or self-referential situations (where your action's semantics is unclear — e.g., in cases involving predictions of *your own* deliberation) resist clean graph modeling.

### 4.2 Egan's counterexamples

Egan (2007) argues that CDT's problem is structural: it requires the agent to "hold fixed" unconditional credences about causal structure while choosing, but sometimes the very fact of being *about to* choose $A$ is evidence one should incorporate.

**Psychopath Button.** Paul can press a button that kills all psychopaths. Paul prefers living in a psychopath-free world to the status quo, but strongly prefers living with psychopaths to dying. Paul is quite confident only a psychopath would press the button. CDT holds fixed Paul's (high) credence that he is not a psychopath; conditional on that, pressing causes a good world and not pressing causes the status quo, so CDT presses. Nearly everyone agrees Paul shouldn't press — the act itself is strong evidence he'll die.

**Death in Damascus.** Death reliably predicts your location and waits there. You can flee to Aleppo or Damascus. Whichever you conclude Death expects you to choose, you reason Death has anticipated it; a naive CDT agent oscillates and can end up unable to settle on any stable act, or choosing an act that Death has (by construction) anticipated.

### 4.3 Adversarial Offer

Oesterheld and Conitzer (2021) give a crisper exploit. A seller offers two boxes, each costing \$1; the buyer may buy at most one. Yesterday the seller put \$3 in each box she predicted the buyer *wouldn't* buy. Seller's prediction is 75% accurate.

CDT reasons: at least one box wasn't predicted, so at least one box contains \$3; each box thus has expected causal value at least $0.75 \cdot \$3 = \$2.25 > \$1$ (more carefully, since exactly one of the two boxes contains \$3, the average expected value per box exceeds \$1.50). CDT buys a box — and the seller profits, on average, from every such transaction. An agent that recognized its own choice as *evidence* about the seller's prediction (EDT-style reasoning) would refuse.

Oesterheld and Conitzer extend the point: CDT agents can be subject to *diachronic Dutch books* — a clever bookie can extract guaranteed losses across a sequence of bets — and related scenarios exist where CDT voluntarily forgoes a guaranteed payoff (Spencer 2020; Joyce 2020 responds).

### 4.4 Joyce's defense and ratifiability

Joyce, CDT's most prominent contemporary defender, argues that a proper CDT agent can and should incorporate "information about what one is inclined or likely to do as evidence" — leading to the notion of *ratifiability* (Harper 1984; Jeffrey 1983). An action is ratifiable if, conditional on your having decided to take it, it still maximizes causal expected utility. In the Psychopath Button, once Paul conditions on "I am about to press," his credence that he's a psychopath shoots up, and pressing no longer looks optimal — so pressing is *not* ratifiable, and CDT-with-ratifiability declines. In the Adversarial Offer, conditioning on "I'm about to buy box 1" makes it likely the seller predicted this, so box 1 contains nothing; again buying is not ratifiable.

Ratifiability resolves several of Egan's counterexamples. Its cost: some problems admit no ratifiable action (Death in Damascus is a candidate), and ratifiability, in importing conditional-upon-decision evidence, arguably smuggles back much of EDT's reasoning — blurring the very line the theory was drawn to maintain.

### 4.5 Functional and other successors

These pressures have generated hybrid theories: Joyce's own refinement, wedges toward "functional decision theory" and related proposals (which evaluate policies by what they make the agent's decision procedure correlate with, effectively one-boxing in Newcomb and cooperating with twins), and updateless variants. These are, at present, research proposals rather than settled doctrine; I mention them to orient the reader, not as endorsements. My own view is that the Newcomb-family examples are best handled by thinking of rationality as a property of *decision procedures* rather than of isolated acts — a framing that leaves CDT as a fine theory of *which local act is best, holding fixed one's situation* but incomplete as a theory of *which procedure one should adopt*.

## 5. A working procedure

For the reader who wants to *use* CDT on an unfamiliar problem:

1. **Draw the causal graph.** Identify your action node and all variables. Mark which are upstream of your action (common causes, fixed facts, predictions already made) and which are downstream (effects).
2. **Hold upstream fixed.** Compute, for each action $A$, the distribution over downstream outcomes via $do(\text{action} = A)$: sever arrows into the action node, keep upstream variables at their unconditional (or otherwise epistemically appropriate) distribution, propagate forward.
3. **Score and maximize:** $U(A) = \sum_o P(o \mid do(A)) D(o)$.
4. **Check ratifiability.** For each candidate maximizer $A^*$, recompute $U$ conditional on your having decided on $A^*$. If $A^*$ no longer maximizes, the naive answer is unstable; look for the ratifiable choice or admit the problem has no stable CDT answer.

Step 2 embodies CDT's core commitment: correlations through common causes are *not* causal leverage. Step 4 is the honest acknowledgment that self-knowledge — knowing what you're inclined to do — is itself information.

## 6. Conclusion

CDT's central insight is that rational choice should track causal consequence, not evidential correlation: an agent should not refrain from smoking because smoking predicts the lesion, nor expect to win at Newcomb by outsmarting a box whose contents are already fixed. Formally, this amounts to maximizing $\sum_j P(A\,\Box\!\to\, O_j)D(O_j)$ — expected utility over *interventional* rather than *observational* probabilities. The theory handles the common-cause cases (Smoking Lesion, King David) cleanly and, with ratifiability, absorbs several apparent counterexamples. Its genuine vulnerabilities are the same cases that embarrass EDT from the other side: Newcomb, twin dilemmas, and adversarial offers, where the *best decision procedure* is one whose outputs correlate with good outcomes even when individual acts cannot cause them. Whether one takes this as refuting CDT or as showing that act-level rationality and procedure-level rationality come apart is, at bottom, the live question the field is still arguing about.

## References

- Egan, A. (2007). "Some counterexamples to causal decision theory." *Philosophical Review* 116(1): 93–114.
- Gibbard, A.; Harper, W. (1981). "Counterfactuals and two kinds of expected utility." In *Ifs*, 153–190.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Joyce, J. M. (2012). "Regret and instability in causal decision theory." *Synthese* 187(1): 123–145.
- Lewis, D. (1976). "Probabilities of conditionals and conditional probabilities." *Philosophical Review* 85(3): 297–315.
- Lewis, D. (1979). "Prisoners' dilemma is a Newcomb problem." *Philosophy & Public Affairs* 8(3): 235–240.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59(1): 5–30.
- Oesterheld, C.; Conitzer, V. (2021). "Extracting money from causal decision theorists." *Philosophical Quarterly* 71(4): pqaa086.
- Pearl, J. (2000). *Causality*. Cambridge University Press.
- Weirich, P. "Causal Decision Theory," *Stanford Encyclopedia of Philosophy* (Winter 2016).