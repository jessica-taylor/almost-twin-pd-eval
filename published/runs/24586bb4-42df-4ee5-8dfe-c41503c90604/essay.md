# Causal Decision Theory: A Working Guide

## 1. Two ways to value an action

Suppose you face a choice among acts $A, B, C, \dots$, and you have credences about how the world is and a utility function $D(O)$ over outcomes $O$. Expected utility maximization is the common skeleton of modern decision theories; the theories differ on *which probabilities* go into the expectation.

**Evidential decision theory (EDT)** says: choose the act with the best *news value*. Its value function is

$$
EU_{\text{ev}}(A) = \sum_j P(O_j \mid A)\, D(O_j).
$$

You evaluate $A$ by asking how learning that you will do $A$ would change your beliefs about the world.

**Causal decision theory (CDT)** says: choose the act with the best *expected causal consequences*. The version due to Gibbard and Harper (1981) computes

$$
U(A) = \sum_j P(A \to O_j)\, D(O_j),
$$

where $P(A \to O_j)$ is the probability of the *counterfactual conditional* "if $A$ were done, $O_j$ would obtain," and $D(O_j)$ is the desirability of $O_j$. The agent asks, not "what does doing $A$ tell me about the world?" but "what would happen *because of* my doing $A$?"

A toy example makes the contrast sharp. You are unsure whether an apple is good or bad. Eating a good apple causes happiness; eating a bad apple causes sadness. If eating a rotten apple were also *evidence* that you are the kind of person who dislikes apples (so your act carries information about something it cannot influence), EDT and CDT would come apart even in this trivial case. CDT evaluates the apple's actual causal effect given your uncertainty about its quality; EDT evaluates what eating it would suggest about it and about you.

## 2. Why the counterfactual probability is not the conditional probability

One might hope $P(A \to O_j) = P(O_j \mid A)$, in which case CDT and EDT collapse. David Lewis (1976) proved this cannot hold in general: his triviality result shows that no nontrivial class of probability functions, closed under conditionalization, admits a probability-valued conditional connective satisfying $P(A \to B) = P(B \mid A)$. The two quantities genuinely differ.

Gibbard and Harper showed that under two axioms (one of them the controversial *conditional excluded middle*: of "if $A$ then $O$" and "if $A$ then not-$O$", exactly one is true) statistical independence of $A$ and $A \to O_j$ suffices to make them coincide. Intuitively: if your act is evidentially irrelevant to the causal structure that determines the outcome, "what would happen if I did $A$" and "what will happen given that I do $A$" agree. They come apart exactly when the act is correlated with the relevant background facts without causing them — precisely the interesting cases.

## 3. King David: the master example

Gibbard and Harper's illustration is worth stating carefully, because it isolates the core intuition of CDT.

King David desires Bathsheba but fears that summoning her would provoke a revolt. Political science teaches him: kings are either charismatic or uncharismatic; charisma is fixed by genes and upbringing and cannot be changed in adulthood; charismatic kings tend to act justly, uncharismatic kings unjustly; revolts succeed against charismatic kings only rarely but against uncharismatic kings frequently — because uncharismatic kings have a sneaky bearing that emboldens plotters, *not* because unjust acts themselves cause revolts. David does not know whether he is charismatic, and he knows summoning Bathsheba is unjust.

**EDT's calculation.** Since unjust kings are overwhelmingly uncharismatic, learning "David summons her" makes it very likely David is uncharismatic, and hence that a revolt will succeed. Conditional on summoning, the news is bad. EDT recommends abstaining.

**CDT's calculation.** Summoning her does not change David's charisma. Holding fixed David's credence over his own type, the counterfactual "if I summon her, a revolt succeeds" has exactly the same probability as the counterfactual "if I abstain, a revolt succeeds" — his character, and thus the revolt risk, is fixed either way. Abstaining buys nothing. Since David values Bathsheba, CDT recommends summoning her.

This is the pattern in which CDT's intuitions are strongest: an act correlated with a fixed, causally upstream fact should not deter you, because you cannot causally influence the fact. The act is a *symptom* of your type, not a *handle* on your circumstances.

## 4. Newcomb's problem

Now the canonical stress test. A predictor with 99% accuracy has already placed either \$1,000,000 or nothing in opaque box B (million if it predicted you take only B, nothing if it predicted you take both). Transparent box A always holds \$1,000. You may take both boxes or only B.

- **EDT**: taking only B is strong evidence the predictor predicted one-boxing, so B is full: $P(\text{full}\mid \text{one-box}) \approx 0.99$. One-boxing dominates the conditional expectation (\$990,000 vs. about \$10,000... let me compute: two-boxing's news value is $0.01 \cdot 1{,}001{,}000 + 0.99 \cdot 1{,}000 \approx \$11{,}000$). EDT one-boxes.
- **CDT**: the contents of B are already fixed; your act cannot cause them to change. Conditioned on either content of B, two-boxing yields \$1,000 more. Formally, the counterfactuals "if I took both boxes, B would be full" and "if I took only B, B would be full" have the same probability (both are downstream of the already-set prediction). CDT two-boxes.

The source notes that philosophers who must choose between the theories usually prefer CDT — largely on the strength of cases like King David — yet Newcomb divides them, and many find two-boxing's outcome (walking away with \$1,000 while the one-boxer leaves with \$1,000,000) hard to call "rational." Note the structural similarity between Newcomb and King David: in both, the act is evidence about a fixed state. The difference is that in Newcomb the fixed state was *set by a process that modelled your very decision*, which is why the case is contested rather than trivial.

## 5. How CDT is actually applied: dependency hypotheses and imaging

The Gibbard–Harper formula leaves open how to compute $P(A \to O_j)$. The standard operationalization, due to Lewis (1981), runs through **dependency hypotheses**.

Partition the background causal situation into hypotheses $K$ about which causal connections hold (e.g., "the predictor predicted one-box," "I am charismatic," "my twin will cooperate"). Then:

$$
U(A) = \sum_K P(K) \sum_j P(O_j \mid A \wedge K)\, D(O_j).
$$

Equivalently: *condition on each dependency hypothesis* (fixing what the world's causal structure is, and where your act sits in it), compute the ordinary conditional expected utility of $A$ given $K$, and average over hypotheses weighted by your unconditional credence $P(K)$. This is the content of Egan's formulation of CDT's policy: "do whatever has the best expected outcome, holding fixed our initial views about the likely causal structure of the world."

A dual implementation is Lewis's **imaging**: to evaluate $P(A \to O_j)$, take each possible world $w$ and reassign its probability mass to the closest world $w_A$ in which $A$ holds. Imaging "moves you" to the nearest $A$-world without disturbing your beliefs about causally upstream matters, whereas conditioning redistributes mass over all worlds proportionally, including upstream ones. Imaging is exactly the right operation for King David: it preserves $P(\text{charismatic})$ while changing the act, which conditioning does not do.

**The regress problem** (flagged by Shaffer 2009): imaging requires knowing what you *would* believe if you were certain of $A$, which is itself a conditional to which you may assign probability less than 1. In practice, the dependency-hypothesis formulation avoids explicit counterfactuals: the agent supplies a causal model (or a partition of them with credences) and does ordinary conditioning *within* each model. CDT is thus best applied by asking: *what are the causally upstream, act-independent variables? Condition on them; then maximize.* This is how a reader should operationalize the theory in unfamiliar cases:

1. List acts and outcomes; assign utilities.
2. Enumerate dependency hypotheses $K$: propositions describing which features of the situation are causally fixed relative to the act (the predictor's past prediction, your character, another agent's simultaneous choice, etc.).
3. For each $K$, compute $EU(A \mid K)$ using ordinary conditional probabilities *within* $K$.
4. Average over $K$ with your prior credences; choose the maximizing act.

Crucially, $P(K)$ is your credence *before* conditioning on your own action. That "holding fixed" is both CDT's defining feature and, we will see, the locus of its troubles.

## 6. Counterexamples: where CDT's verdicts look insane

**Death in Damascus.** Death predicts where you will be tomorrow and waits there; the prediction is reliable. You can flee to Aleppo or Damascus. If you decide to stay in Damascus, you should expect Death is there; if you decide to flee to Aleppo, you should expect Death is there. Whatever you conditionally expect, your act is evidence Death has anticipated it. A CDT agent evaluating acts while holding fixed its credence about its own inclinations finds each act's causal expected value chased down by Death: on evaluating "go to Aleppo," it comes to believe Death is in Aleppo (since it now knows it will go there), making staying look better; then it evaluates staying, believes Death is in Damascus, and so on — the decision problem is unstable. EDT, which conditionally expects to meet Death under either act, at least evaluates both acts as equally bad. The deeper diagnosis (Egan 2007; Meacham 2010) is the "fundamental disconnect": the intuitive rule "do what you expect will bring about the best results" conflicts with CDT's "hold fixed your unconditional credences about the causal structure," because *your knowledge of your own dispositions* is itself relevant information CDT refuses to use at decision time.

**The Psychopath Button.** Pressing the button kills all psychopaths (good, Paul thinks) but kills the presser if the presser is a psychopath. Paul is nearly certain only a psychopath would press. Nearly everyone agrees: don't press. Yet CDT, holding fixed Paul's credence that *he* is not a psychopath (he wouldn't press — or would he?), conditionalizes on "I'm not a psychopath" within each dependency hypothesis, where pressing is causally safe and beneficial. So CDT presses. The act is excellent evidence Paul is a psychopath, but poor evidence is, by CDT's lights, no reason not to act. Intuitively, your own decision propensity is information you should use; classical CDT holds it fixed anyway.

**The Adversarial Offer (Oesterheld & Conitzer 2021).** Two boxes cost \$1 each; you may buy at most one. Yesterday the seller put \$3 in each box she predicted you *not* to buy. The prediction is accurate with probability 0.75. CDT reasons: at least one box went unbought, so at least one holds \$3; the average box holds at least \$1.50 of causal expected value, exceeding the \$1 price — buy one. But the seller predicted exactly this reasoning; buying is what she anticipated, so with probability 0.75 your purchased box is empty and you lose \$1 on average ($0.75 \cdot (-1) + 0.25 \cdot 2 = -0.25$). The victim is again the "hold fixed" clause: CDT evaluates each act against its *prior* credence that it will buy that box, a credence the adversarial predictor has outmodelled.

**Twin prisoner's dilemma.** Lewis (1979) observed the prisoner's dilemma against a psychological twin *is* a Newcomb problem: your twin's choice correlates almost perfectly with yours (common causes — shared genes and upbringing) but neither causes the other. EDT cooperates (cooperation is evidence the twin cooperates); CDT defects, since nothing you do causally influences the twin. Whether that is rational when facing a perfect simulation or twin remains one of the sharpest live disputes — and matters practically, since real agents (and prospective AI systems) often face exactly such correlations.

**Money-pumping.** Oesterheld and Conitzer argue further that CDT agents can be *diachronically* exploited: an adversary who knows the CDT agent's decision rule can construct a sequence of offers, each locally attractive by CDT's lights, whose net effect is a guaranteed loss.

## 7. Replies and open questions

Joyce (2012), CDT's most prominent modern defender, argues that these counterexamples attack a simplified target: a proper causal decision theory *can* take into account "information about what one is inclined or likely to do as evidence." On his view the dependency hypotheses should be formulated finely enough to include facts about the agent's own decision dispositions; when they are, the Psychopath Button and Adversarial Offer cases either recommend the sane act or expose the problem as having no stable recommendation. Relatedly, Harper's *ratifiability* condition requires that an act be optimal given the belief that one will perform it — filtering out acts whose evaluation undermines itself. Whether these repairs yield a stable, fully general theory, or merely relocate the instability, is unresolved. Egan-style instability also suggests CDT needs a story about *reflective equilibrium* between credences about one's own actions and evaluations of actions — something EDT possesses naturally, since EDT simply conditions on the act.

A more radical response, worth noting though the source does not endorse it: functional or "policy" versions of decision theory evaluate *decision procedures* rather than acts — ask which algorithm, if run, would cause the best outcomes. Such theories (of which so-called updateless or functional decision theories are recent proposals) one-box, cooperate with twins, and refuse the Adversarial Offer, while agreeing with CDT in King David. They treat the agent's decision algorithm as a causally upstream node whose outputs correlate with what predictors and twins infer. My own operational gloss: when the act-independent facts were *set by a model of your decision rule*, treat your decision rule, not the individual act, as the causal variable. This is a proposal beyond the source, but it dissolves the Adversarial Offer cleanly (the seller predicted the *rule*; the rule can cause the \$3 to appear) while preserving CDT's correct verdicts elsewhere.

## 8. Practical summary

To apply CDT to an unfamiliar problem:

- Identify what your act can *cause*, tracing causal arrows downstream only.
- Identify upstream, act-independent facts (predictions already made, fixed traits, others' simultaneous choices) and your credences over them.
- Compute each act's expected utility conditional on each configuration of those facts, and average.
- Ignore the evidential import of your act concerning those upstream facts — unless your theory of your own decision dispositions is itself part of the dependency hypotheses (Joyce's move), in which case the case must be checked for stability/ratifiability.

CDT gets right the large class of cases where refusing an act because of what it *says about you* is superstition: David and Bathsheba, smoking lesions, genetic predispositions. It gets into trouble exactly when the correlation between act and fixed fact is mediated by a model of the agent's own reasoning — predictors, twins, adversarial sellers. That boundary, and whether a single expected-utility formula can handle both sides of it, remains the central open question of decision theory.

## Conclusion

Causal decision theory refines expected utility maximization by replacing conditional probabilities with counterfactual ones: value an act by what it would *bring about*, not what it would *indicate*. The formal machinery — Gibbard–Harper counterfactual probabilities, Lewis's imaging, dependency hypotheses — is precise enough to compute verdicts, and its core insight is robust: do not let a correlation with the unalterable deter you. Its failures (Newcomb, the Psychopath Button, Death in Damascus, the Adversarial Offer) all share a structure in which the agent's own disposition is the hidden causal node, and the theory's stipulation to hold fixed one's prior credences about it becomes a self-imposed blindness. Whether Joyce's enriched dependency hypotheses or policy-level evaluation best repairs this is an open and active question — but one cannot understand modern decision theory without mastering CDT's exact dividing line between evidence and cause.

## References

- Gibbard, A. & Harper, W. L. (1981). "Counterfactuals and Two Kinds of Expected Utility." In *Ifs*, 153–190.
- Lewis, D. (1976). "Probabilities of Conditionals and Conditional Probabilities." *Philosophical Review* 85(3): 297–315.
- Lewis, D. (1979). "Prisoners' Dilemma Is a Newcomb Problem." *Philosophy & Public Affairs* 8(3): 235–240.
- Lewis, D. (1981). "Causal Decision Theory." *Australasian Journal of Philosophy* 59(1): 5–30.
- Egan, A. (2007). "Some Counterexamples to Causal Decision Theory." *Philosophical Review* 116(1): 93–114.
- Joyce, J. M. (2012). "Regret and Instability in Causal Decision Theory." *Synthese* 187(1): 123–145.
- Meacham, C. J. G. (2010). "Binding and Its Consequences." *Philosophical Studies* 149(1): 49–71.
- Oesterheld, C. & Conitzer, V. (2021). "Extracting Money from Causal Decision Theorists." *Philosophical Quarterly* 71(4): pqaa086.
- Shaffer, M. J. (2009). "Decision Theory, Intelligent Planning and Counterfactuals." *Minds and Machines* 19(1): 61–92.
- Weirich, P. (2016). "Causal Decision Theory." *Stanford Encyclopedia of Philosophy*.