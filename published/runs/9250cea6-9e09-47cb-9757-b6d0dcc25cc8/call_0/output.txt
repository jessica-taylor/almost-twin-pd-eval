# Causal Decision Theory: A Mathematical Essay

## 1. Introduction

Suppose you face a choice. You have beliefs about the world—probabilities assigned to how things might be—and preferences over how the world might turn out—a utility function. Classical Bayesian decision theory tells you to choose the act with the greatest *expected utility*. But expected utility *relative to what probability measure?* This seemingly innocent question splits decision theory in two.

**Evidential decision theory (EDT)** says: condition on the news that you performed the act. Choose the act $A$ maximizing

$$\sum_j P(O_j \mid A)\, D(O_j),$$

the expected desirability of the outcomes given the *evidence* that $A$ was chosen.

**Causal decision theory (CDT)** says: evaluate each act by the expected utility of its *causal consequences*, holding fixed your beliefs about the causal upstream of your action. Choose the act maximizing

$$U(A)=\sum_j P(A \to O_j)\, D(O_j),$$

where $P(A \to O_j)$ is the probability of the *counterfactual* "if $A$ were done, $O_j$ would result"—not the probability of $O_j$ given the news of $A$.

The distinction sounds pedantic until one notices cases where the two theories diverge—and diverge dramatically. This essay develops CDT formally, explains where and why it separates from EDT, works through the canonical thought experiments, and examines the theory's known pathologies. My aim is that a reader could take the machinery here and apply it to a new decision problem.

## 2. The Formal Framework

### 2.1 Ingredients

We assume an agent with:

- A finite set of mutually exclusive acts $\mathcal{A} = \{A_1, \dots, A_n\}$.
- A partition $\mathcal{O} = \{O_1, \dots, O_m\}$ of possible outcomes (states of the world after the act), mutually exclusive and exhaustive.
- A credence function $P$ over propositions, including the acts and outcomes.
- A desirability (utility) function $D$ with $D(O_j)$ the agent's utility for outcome $O_j$. (We assume the usual von Neumann–Morgenstern axioms so that $D$ is unique up to positive affine transformation.)

### 2.2 Counterfactual probabilities

The distinctive object in CDT is $P(A \to O_j)$, the agent's credence in the counterfactual conditional "$A \to O_j$": *were $A$ to be done, $O_j$ would obtain*. Crucially, David Lewis proved (1976) that the probability of a conditional is not in general the conditional probability of consequent given antecedent: $P(A \to O) \neq P(O \mid A)$ in general. His triviality results show that any attempt to define a conditional probability operator $\to$ with $P(X \to Y) = P(Y \mid X)$ that is closed under conditionalization collapses into triviality. So the two theories genuinely differ: EDT uses $P(O_j \mid A)$; CDT uses $P(A \to O_j)$.

### 2.3 Dependency hypotheses

A cleaner and more modern formulation (Joyce, Weirich) makes the counterfactual structure explicit. Let $\mathcal{K} = \{K_1, \dots, K_\ell\}$ be a partition of *dependency hypotheses*—complete descriptions of the causal structure connecting the agent's act to the rest of the world, including everything causally upstream of the act. The agent's credence $P(K_i)$ distributes over these hypotheses. Then:

$$U(A) = \sum_i P(K_i) \sum_j P(O_j \mid A \wedge K_i)\, D(O_j).$$

That is: *for each possible causal setup, compute the causal expected value of $A$ within that setup; then average over setups, weighted by how likely you think each setup is.* The key structural feature is that acts are probabilistically independent of dependency hypotheses—$P(K_i \mid A) = P(K_i)$—because $K_i$ describes the state of the world at the moment of choice, causally prior to the act. This is the technical expression of "CDT holds fixed the agent's unconditional credences about the causal structure of the world."

### 2.4 Imaging: computing the counterfactuals

Lewis (1981) proposed a concrete semantics. To evaluate $P(A \to O)$: take your probability distribution over possible worlds, and for each world $w$ in which $A$ is false, *move* its probability mass to the closest $A$-world $w_A$ (closest in the appropriate similarity/closeness ordering). Formally, if $P^A$ is the "imaged" distribution,

$$P^A(O) = \sum_w P(w)\, \delta_w(O \mid A),$$

where $\delta_w(O\mid A)$ puts mass on $O$ according to the closest $A$-world to $w$. Then $U(A) = \sum_O P^A(O) D(O)$.

Contrast this with conditioning: conditioning redistributes mass to *all* $A$-worlds proportionally, discarding $A$-worlds entirely; imaging *saves* the discarded worlds by transporting them to their nearest $A$-counterpart. Conditioning answers "what should I believe given that $A$ in fact happened?"; imaging answers "what would happen if $A$ were done?". The difference is exactly the difference between evidence and intervention.

## 3. Where the Theories Diverge

### 3.1 The apple example, made precise

Eating a possibly-bad apple: let $G$ = "the apple is good" (prior $P(G) = p$), $D(\text{happy}) = h > 0$, $D(\text{sad}) = -s$. Eating the apple *causes* happiness iff it is good; $G$ is causally upstream of the act's effect and unaffected by the act. Then

$$U(\text{eat}) = p\,h - (1-p)\,s, \qquad \text{vs. } U(\text{refrain}) = 0.$$

Since $P(G \mid \text{eat}) = P(G)$ (no evidential relevance either), EDT agrees. Divergence requires a *second* channel by which the act correlates with outcomes—a common cause.

### 3.2 The diagnostic structure: David and Bathsheba

Gibbard and Harper's example isolates the divergence cleanly. King David considers summoning Bathsheba. Whether David is charismatic or uncharismatic is fixed by genetics and upbringing—no act of his can change it. Charismatic kings tend to act justly; unjust acts don't themselves cause revolts, but uncharismatic kings have an ignoble bearing that invites successful revolt. So:

$$\text{Charisma} \longrightarrow \text{(tendency to summon)} \quad \text{and} \quad \text{Charisma} \longrightarrow \text{(revolt risk)}.$$

Charisma is a common cause of the act and the outcome; the act does not cause the outcome.

- **EDT**: $P(\text{revolt} \mid \text{summon}) > P(\text{revolt} \mid \text{abstain})$, because summoning is evidence of uncharisma. EDT recommends abstaining—even though abstaining cannot change David's charisma or his revolt risk.
- **CDT**: $P(\text{revolt} \to \text{summon}) = P(\text{revolt} \mid \text{summon} \wedge K) = P(\text{revolt} \mid \text{charisma})$ on each dependency hypothesis, unchanged by the act. The act's causal consequences are just those of the summoning itself; the correlation is spurious. CDT recommends summoning.

The intuition most people share: the act is a *symptom* of charisma, not a *lever* on it. Doing the virtuous-causally-irrelevant thing to manipulate your own evidence about yourself would be, in Joyce's phrase, managing the news rather than the outcome.

## 4. The Thought Experiments

### 4.1 Newcomb's problem

Predictor accuracy 99%; Box A always holds \$1,000; Box B holds \$1,000,000 iff the predictor predicted one-boxing. Contents are set *before* the choice.

- **CDT**: The dependency hypotheses fix the box contents as causally prior. Under every $K_i$, two-boxing causally yields \$1,001 vs. \$1,000 for one-boxing. Two-box.
- **EDT**: $P(\text{B full} \mid \text{one-box}) \approx 0.99$; one-box.

With accuracy 99%, one-boxing has evidential expected value $\approx \$990{,}000$ versus $\approx \$11{,}000$ for two-boxing; two-boxing has causal expected value \$1,001 vs \$1,000. The disagreement is total, and it persists even at accuracy just above $(1{,}001)/(1{,}000{,}000 + 1{,}000) \approx 0.1\%$.

What should we say? The Wikipedia article notes (with a "citation needed" tag) that CDT two-boxes because "the action of the player will not affect the outcome." I'd add a refinement of my own: the problem's force depends on whether we take the predictor's prior accuracy as fixing a genuine common-cause structure (your *disposition* to choose causes neither the boxes nor... well, it correlates with the boxes via the predictor's model of you). On a causal graph with your choice-disposition as a common cause of both your act and the prediction, CDT's dependency-hypothesis framework can in principle *recommend one-boxing*—if the act is treated as evidence of the disposition, and the "act" node is replaced by the policy node. This is the observation behind functional and policy versions of decision theory. Standard CDT, however, evaluates the act token with $P(K_i \mid A) = P(K_i)$, and two-boxes. Philosophers remain divided on which is the "rational" strategy.

### 4.2 Prisoner's Dilemma with your twin

Lewis (1979) observed that Newcomb's problem is structurally a prisoner's dilemma. Playing against a psychological twin whose choice correlates with yours (via common neural makeup) but is not caused by yours: causal utility of defecting exceeds cooperating (defect strictly dominates causally), but your defection is evidence your twin defects. CDT defects; EDT (given strong enough correlation) cooperates. Again the same wedge.

### 4.3 Death in Damascus

Death reliably predicts where you'll be tomorrow and waits there. You can go to Aleppo or Damascus. Suppose: if you go to Aleppo, you'd find Death waiting (he predicted Aleppo); similarly Damascus. The dependency hypotheses correlate your act with Death's location.

Here CDT exhibits *instability* (Egan 2007; Joyce 2012): whichever act CDT evaluates as better, the agent's learning that she is inclined to that act is evidence Death is there. The agent cycles: inclined toward Aleppo → infers Death is in Aleppo → switches preference to Damascus → infers Death is in Damascus → back to Aleppo. There is no act whose evaluation is stable under the agent's reflection on her own choice. EDT by contrast has a stable mixed attitude: no escape is better in expectation than any other, since Death will be wherever you go.

### 4.4 The Psychopath Button

Paul can press a button killing all psychopaths; pressing kills Paul iff he is a psychopath; Paul is confident only a psychopath would press. Pressing is *evidence* Paul is a psychopath, but does not *cause* his death—the death would be caused by his psychopathy, already fixed.

- **CDT**: pressing's causal consequences: kill everyone else, live (Paul, per his own assessment, is no psychopath). CDT says press.
- **Intuition and EDT**: don't press—the act is near-conclusive evidence of fatal psychopathy.

Egan takes this as a clean counterexample: CDT's advice seems mad. The culprit, Egan argues, is CDT's mandate to "hold fixed the agent's unconditional credences in dependency hypotheses." Paul's credence that he is a psychopath should arguably be updated on his own choice-inclination; plain CDT refuses.

### 4.5 The Adversarial Offer

Two boxes, \$1 each; the seller put \$3 in each box she predicted the buyer *not* to buy; her predictions are 75% accurate. CDT reasons: each box is empty only if both is bought—no, more precisely: a box contains \$3 iff it was predicted *not bought*, i.e., iff the *other* box (or neither) was predicted bought. Since the buyer buys at most one, at least one box was predicted not-bought, so at least one box holds \$3; each box has causal expected value at least $(0.75)(3) \approx \$1.50 > \$1$. CDT buys a box—yet whichever box it buys, it is (with 75% probability) the box that was predicted bought and hence empty. CDT voluntarily loses about \$0.50 in expectation; the seller profits. Oesterheld and Conitzer (2021) generalize: there are systematic schemes to extract money from CDT agents, and CDT agents are vulnerable to diachronic Dutch books.

## 5. Diagnosis and Repair Attempts

What unites Death in Damascus, the Psychopath Button, and the Adversarial Offer? In each, the agent's *own choice-disposition* is a common cause linking act to outcome. Plain CDT treats the act as exogenous—causally detached from everything upstream—and therefore throws away genuine information. The dependency-hypothesis formulation fixes $P(K_i \mid A) = P(K_i)$; but if $K_i$ includes facts about the agent's dispositions, and the act is evidence about those dispositions, holding fixed the unconditional $P(K_i)$ discards exactly the relevant correlation.

Several repair strategies exist; I distinguish them from the core theory:

1. **Ratifiability** (Harper; Jeffrey): evaluate an act conditional on the *news* that it is what the agent will in fact choose—choose act $A$ maximizing $U$ computed with probabilities conditionalized on the intention to choose $A$, requiring the choice to be self-ratifying. This helps with some instability cases but not all; Egan-style counterexamples survive.

2. **Joyce's proposal**: CDT should not hold fixed credences about *what one is inclined to do*; the theory can and should take one's own inclinations as evidence about dependency hypotheses. This yields a more reflective CDT that arguably handles the Psychopath Button (Paul should update on the fact that he is inclined to press). Critics note it threatens to collapse into EDT on the very cases where the theories differ.

3. **Functional / policy decision theories** (my own reconstruction, going beyond the source): evaluate *decision procedures* rather than act tokens. If the act-node is replaced by the policy-node in the causal graph, the policy is causally upstream of the predictor's output (in Newcomb-type cases, the agent's disposition is what the predictor models). This theory one-boxes, cooperates with the twin, refuses the Adversarial Offer, and handles Death in Damascus stably. Whether this counts as "CDT repaired" or "CDT abandoned" is a live terminological question.

4. **The regress worry about imaging** (Shaffer 2009): imaging requires knowing what you'd believe if *certain* of $A$—itself a conditional that may have probability less than 1, threatening a regress. In practice, the dependency-hypothesis formulation with an explicit causal model (Pearl's do-calculus: $P(A \to O) = \sum_k P(O \mid do(A), K_k) P(K_k)$) dissolves the regress by making the counterfactual semantics explicit: intervene on the act node, propagate through the graph. I would recommend this operationalization to any reader applying the theory: draw the causal graph, identify the act node, apply $do(A)$, average over uncertainty in graph structure.

## 6. A Practical Recipe

To apply CDT to an unfamiliar problem:

1. **Specify the partition** $\{K_i\}$ of dependency hypotheses—everything causally upstream of your act that bears on the outcome (your own traits included, if they influence your choice).
2. **Assign priors** $P(K_i)$.
3. **For each act $A$ and hypothesis $K_i$**, compute the conditional distribution $P(O_j \mid A, K_i)$—treating $A$ as an intervention, i.e., breaking all incoming causal edges to $A$.
4. **Compute** $U(A) = \sum_i P(K_i)\sum_j P(O_j \mid A, K_i) D(O_j)$.
5. **Choose** $\arg\max_A U(A)$.

The critical modeling step is step 3: ask, for each $K_i$, "if I intervened to do $A$, in this causal setup, what would happen?" Any correlation between $A$ and outcomes mediated *through* the $K_i$—evidence, symptoms, predictions—is correctly ignored. Correlations mediated by the act's own downstream effects are correctly respected.

## 7. Conclusion

Causal decision theory formalizes a compelling idea: rationality is about *doing*, not *signaling*. Its mathematical core—the maximization of causal expected utility over a partition of dependency hypotheses—is clean, and its divergence from EDT is exactly the divergence between $P(A \to O)$ and $P(O \mid A)$ that Lewis's triviality results guarantee is real. It gets the diagnostic cases right (David, apple, smoking) and, most philosophers agree, two-boxes correctly in Newcomb. But the recent literature—Egan's counterexamples, Spencer's guaranteed-payoff cases, Oesterheld and Conitzer's money-pumping schemes—shows that the theory as standardly formulated has a genuine flaw: it discards legitimate evidence encoded in the agent's own dispositions. Whether that flaw is fatal, repairable by reflection on one's inclinations (Joyce), or a symptom that decision theory should move from acts to policies, remains, as of this writing, an open and active question. What is not open is the framework's utility: even its critics reason *in* CDT's vocabulary—dependency hypotheses, causal expected utility, interventions—and any successor theory will be judged by how it treats the cases CDT gets right.

## References

- Gibbard, A. & Harper, W.L. (1981). "Counterfactuals and Two Kinds of Expected Utility." In *Ifs*, 153–190.
- Lewis, D. (1976). "Probabilities of Conditionals and Conditional Probabilities." *Philosophical Review* 85(3): 297–315.
- Lewis, D. (1979). "Prisoners' Dilemma Is a Newcomb Problem." *Philosophy & Public Affairs* 8(3): 235–240.
- Lewis, D. (1981). "Causal Decision Theory." *Australasian Journal of Philosophy* 59(1): 5–30.
- Egan, A. (2007). "Some Counterexamples to Causal Decision Theory." *Philosophical Review* 116(1): 93–114.
- Joyce, J.M. (2012). "Regret and Instability in Causal Decision Theory." *Synthese* 187(1): 123–145.
- Shaffer, M.J. (2009). "Decision Theory, Intelligent Planning and Counterfactuals." *Minds and Machines* 19(1): 61–92.
- Oesterheld, C. & Conitzer, V. (2021). "Extracting Money from Causal Decision Theorists." *Philosophical Quarterly* 71(4): pqaa086.
- Weirich, P. (2016). "Causal Decision Theory." *Stanford Encyclopedia of Philosophy*.
- Wikipedia contributors (2026). "Causal decision theory." Revision 1381555528. CC BY-SA 4.0.