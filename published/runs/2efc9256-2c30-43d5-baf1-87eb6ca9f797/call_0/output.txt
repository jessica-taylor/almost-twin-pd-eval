# Causal Decision Theory: A Mathematical Introduction

## 1. The core idea

Decision theory asks how a rational agent with beliefs and desires should choose among actions. The dominant answer for most of the twentieth century was: maximize expected utility, where the expectation is taken over the agent's degrees of belief conditional on each action. This is *evidential decision theory* (EDT): the value of an action is measured by how good the world tends to be *when* the action is performed — the action treated as news.

*Causal decision theory* (CDT) begins from a simple diagnosis. Sometimes an action is excellent news about the world without being a good way of changing the world. When a correlation between act and outcome runs through a common cause — your genes, someone else's prediction, your own character — the news value of the action is misleading. CDT says: choose the action with the best expected *causal* consequences, holding fixed the causal facts you cannot change.

This essay develops the formalism, works through the canonical examples, discusses how CDT evaluates counterfactuals, and surveys the known trouble cases. Where the standard formulation leaves questions open, I will say so and, where a defensible operational answer exists, develop it — flagging clearly which claims come from the sources and which are my own proposals.

## 2. Formal setup

Let $A$ range over available actions and $O_1, \dots, O_n$ over the possible outcomes, with a desirability (utility) function $D(O_j)$ measuring how good the agent finds $O_j$. In their 1981 paper, Gibbard and Harper formulated CDT as maximization of

$$
U(A) \;=\; \sum_j P(A \,\Box\!\!\to\, O_j)\, D(O_j),
$$

where $A \,\Box\!\!\to\, O_j$ is the counterfactual conditional "if $A$ were done, $O_j$ would hold," and $P(A \,\Box\!\!\to\, O_j)$ is the agent's probability for that counterfactual. The choice of $\Box\!\!\to$ rather than the ordinary conditional probability $P(O_j \mid A)$ is the entire point: CDT and EDT differ precisely in what plays the role of "the probability of the outcome given the act."

EDT's rule is

$$
V(A) \;=\; \sum_j P(O_j \mid A)\, D(O_j).
$$

A natural first thought is that these must coincide: isn't $P(A \,\Box\!\!\to\, O) = P(O \mid A)$? David Lewis proved that it is not, and cannot be in general — his famous triviality result shows that no nontrivial class of probability functions, closed under conditionalization, admits a connective $\to$ whose probability always equals the conditional probability. So the two formulas are genuinely different operators, and a decision theory must choose between them.

Gibbard and Harper showed that if $A$ is statistically independent of the counterfactual $A \,\Box\!\!\to\, O_j$, then (under two axioms, one of them the contentious principle of *conditional excluded middle*) the two probabilities do coincide. They come apart exactly when the act correlates with what would happen *if* the act were performed — which is to say, exactly in the interesting cases.

## 3. Why the difference matters: the David case

Gibbard and Harper's own illustration is King David, who desires Bathsheba but fears that summoning her will provoke a revolt. Psychological study teaches David:

- Kings are either charismatic or uncharismatic; this is fixed by genes and upbringing and cannot change in adulthood.
- Charismatic kings tend to act justly; uncharismatic kings unjustly.
- Successful revolts are rare against charismatic kings, frequent against uncharismatic ones — but *because* uncharismatic kings have a sneaky, ignoble bearing that invites rebellion, not because injustice causes revolt.

David does not know which type he is, but he knows summoning Bathsheba is unjust. So his act is strong evidence that he is uncharismatic, hence strong evidence of a successful revolt. EDT computes $P(\text{revolt} \mid \text{summon}) \gg P(\text{revolt} \mid \text{refrain})$ and advises restraint. CDT computes the counterfactuals: if David *were* to summon her, would a revolt occur? The revolt-risk is a fixed feature of David's already-determined character; summoning does not cause it. Whether David is charismatic or not, his choice does not affect the revolt's prospects. CDT advises summoning her.

This is the template. The correlation between act and bad outcome is spurious, routed through a common cause (David's character) that is beyond the act's influence. EDT "punishes" David for a fact he cannot control; CDT refuses to.

## 4. Computing the counterfactuals: imaging

The source is candid that CDT "does not itself specify what algorithm to use to calculate the counterfactual probabilities." This is the theory's central implementation gap, and it is worth dwelling on.

Lewis's own proposal (1981) is *imaging*. To evaluate $P(A \,\Box\!\!\to\, O_j)$: for each possible world $w$ with $P(w) > 0$, move all of $w$'s probability mass to the closest $A$-world $w_A$ (the world that results from $w$ by minimally making $A$ true); then sum the mass that lands in $O_j$-worlds. Formally, with a closeness relation and $\text{im}_A(w)$ denoting the closest $A$-world to $w$ (or a probability distribution over such worlds in the stochastic version):

$$
P(A \,\Box\!\!\to\, O_j) \;=\; \sum_w P(w)\, \Pr\nolimits_{w_A}(O_j).
$$

Imaging differs from conditioning in a crucial way. Conditioning *rescales* probability across worlds, discarding the $\neg A$-worlds. Imaging *redirects* probability, keeping total mass intact but relocating it to where $A$ would hold. When the act is causally independent of everything else, the two coincide. When there is a common cause — say a variable $C$ correlated with both $A$ and $O$ — conditioning keeps the $A$-$O$ correlation (because among $A$-worlds, $C$-worlds are overrepresented), whereas imaging moves each $C$-world to its nearest $A$-world *within that value of $C$*, thereby screening off the spurious correlation. Imaging is, in effect, an intervention in Pearl's sense: the graph-theoretic do-calculus of modern causal inference is a structured descendant of this idea. Concretely, if $\mathcal{M}$ is a causal model and $A$ a choice node, a natural operationalization (my own gloss, standard in the causal-modeling literature though not in the source) is

$$
P(A \,\Box\!\!\to\, O_j) \;=\; P\big(O_j \,\big|\, \mathrm{do}(A)\big),
$$

the post-intervention distribution obtained by cutting all incoming causal arrows into the act node.

The regress worry flagged by Shaffer remains: imaging requires knowing what one *would* believe if certain of $A$, and that conditional belief is itself something one might assign probability less than 1 to. The do-calculus interpretation softens this by making the counterfactual a function of the (non-probabilistic) causal graph plus the ordinary credence distribution — the agent needs a causal model, not a hierarchy of nested conditionals. But it makes CDT's dependence on the agent's *causal* beliefs, not merely her probabilistic ones, explicit. Two agents with identical credences but different causal graphs can rationally choose differently. That is a feature or a bug depending on your view; it is certainly a substantive commitment.

## 5. Newcomb's problem

The classic stress test. A predictor with 99% reliability has already placed \$1,000,000 in opaque box B iff it predicted you will one-box; transparent box A always contains \$1,000. You may take both boxes or only B.

- **EDT one-boxes.** $P(\text{B full} \mid \text{one-box}) \approx 0.99$, so $V(\text{one-box}) \approx 0.99 \cdot \$1{,}000{,}000$ against roughly $\$1{,}000$ for two-boxing.
- **CDT two-boxes.** The prediction is already made; your act cannot causally influence the contents of B. $P(\text{B full} \,\Box\!\!\to\, O)$ is the same whichever act you evaluate — imaging relocates your credence about B's content nowhere, since the act node has no arrow into it. Two-boxing strictly dominates causally: it adds \$1,000 whatever B contains.

The source notes (with a "citation needed") the standard CDT justification — at decision time the action cannot affect the outcome — and also records the ongoing disagreement about whether one-boxing or two-boxing is "rational." I want to make the CDT calculation slightly more precise, because the informal slogan "your act can't affect the prediction" hides a dependency hypothesis.

An agent's beliefs can be factorized over *dependency hypotheses*: hypotheses about the causal structure linking her act to the world. One such hypothesis says "my act and the box contents are causally independent, correlated only via a common cause (my dispositions, which the predictor read)." Under it, two-boxing dominates. Another hypothesis says "my act is downstream of the very disposition that caused the prediction" — still a common cause. Even the hypothesis "the predictor has backward causation" would be a dependency hypothesis, but nobody believes it here. The key structural fact: under *every* dependency hypothesis the agent takes seriously, the act is not a cause of the box contents. That is what licenses CDT's two-boxing as robust, not merely an artifact of one particular graph. (This framing via dependency hypotheses is Joyce's and, in substance, is the machinery the source invokes when discussing Egan's critique below.)

The philosophical dispute is whether "rationality" should track what your act causes or what it indicates. CDT's answer — cause — buys the David case at the price of Newcomb. One can see the two cases as structurally identical (an unchangeable common cause: David's character; your disposition) with opposite intuitions about which side of the correlation to honor. A consistent theory must say something unifying; CDT says: the act's *causal* consequences, always. Whether that is a feature is contested.

## 6. Where CDT is alleged to fail

The source catalogues several serious counterexamples. They are worth presenting in some detail, because a reader who wants to *use* CDT needs to know its boundary conditions.

### 6.1 The Psychopath Button

Paul may press a button that kills all psychopaths; he'd love to live in a psychopath-free world, but is nearly certain that only a psychopath would press it, and strongly prefers surviving as a psychopath to dying. Everyone agrees: don't press. CDT, however, reasons causally: pressing does not cause Paul to be a psychopath; his psychopathy (if any) is antecedent. Conditional on pressing, the world is psychopath-free and Paul is (with high probability) dead — but that conditional mixes evidence with counterfactual. The pure causal counterfactual "if Paul pressed, would he survive?" depends on whether he is a psychopath, which pressing cannot change. So CDT evaluates: press and (probably) get the good world if Paul is not a psychopath. It recommends pressing. Egan takes this as a fundamental disconnect between the intuitive rule — "do what you expect will bring about the best results" — and CDT's algorithm, which he diagnoses precisely: CDT "hold[s] fixed the agent's unconditional credences in dependency hypotheses," refusing to update those credences on the evidence provided by the act itself.

### 6.2 Death in Damascus

Death predicts where you will be tomorrow and waits there. Flee to Aleppo or Damascus? A reliable predictor generates a self-referential trap: whichever act you settle on is evidence that Death is there. CDT, holding fixed its credences, finds no stable act — the theory churns, and the agent may behave incoherently, unable to *process* the correlation between her own deliberation and Death's location. Meacham, Harper, and others discuss "binding" and ratifiability refinements here.

### 6.3 The Adversarial Offer

This recent example (Oesterheld and Conitzer) is the sharpest, because CDT loses *money* deterministically. Two boxes, each costs \$1, buy at most one. Yesterday the seller put \$3 in each box she predicted you would *not* buy. Seller accuracy: 0.75. CDT reasons: the seller predicted I won't buy box $X$ or won't buy box $Y$; at least one box was predicted un-bought, so at least one box contains \$3; hence the average box contains at least \$1.50 in causal expected value — more than the \$1 price. Buy a box. But the seller's prediction was about *this very deliberation*, and it was accurate; the buyer's CDT reasoning is exactly the exploitable pattern. Buying is good for the seller, bad for the buyer. Related constructions show CDT agents vulnerable to diachronic Dutch books: sequences of bets in which the agent's own commitment to CDT guarantees a loss.

What should a CDT sympathizer say? Joyce's response, cited in the source, is that CDT can natively take into account "information about what one is inclined or likely to do as evidence." The idea: the agent should first form an all-things-considered credence about *what she herself will do* — treating her own deliberation as evidence like any other — and then evaluate acts relative to that. In the Adversarial Offer, this means the buyer should condition on the fact that a CDT-style calculation will lead her to buy, note that the seller predicted exactly this, and re-evaluate. A *ratifiability* constraint (Harper, Jeffrey) formalizes this: an act $A$ is ratifiable at credence state $P$ if $A$ maximizes $U$ given the supposition that the agent has in fact settled on $A$. In Adversarial Offer, no act is ratifiable — whichever box you consider buying, the supposition that you buy it implies it is empty — a fixed point failure that mirrors Death in Damascus. This diagnosis is, I should stress, my elaboration; the source records the counterexamples and Joyce's general reply, but the operational details of how "evidence about one's inclinations" enters the calculation are not settled. The most promising versions (Joyce 2012; Meacham's binding) amount to allowing the deliberation process itself to shift the credences over dependency hypotheses that are held fixed at any single evaluation. Whether this rescue is principled or ad hoc is open; critics note that once you let the act's evidential import move the dependency credences, CDT begins to look like EDT in a trenchcoat.

## 7. A worked comparison: the twin prisoner's dilemma

Lewis observed that the prisoner's dilemma *is* a Newcomb problem when played against a psychological twin. Suppose your twin's choice correlates with yours at 0.99 — not because either causes the other, but because you share a decision algorithm or upbringing. Payoffs: mutual cooperation gives each 3; mutual defection gives each 1; unilateral defection gives defector 5 and cooperator 0.

- CDT: my defection does not cause my twin's. Whatever she does, defecting gains me +2. Defect. Expected payoff $\approx 1$ (since she almost surely defects too).
- EDT: my defection is near-conclusive evidence of hers. Cooperating has expected payoff $\approx 3 \cdot 0.99 + 0 \cdot 0.01 \approx 2.97$, versus defection's $\approx 5(0.01) + 1(0.99) \approx 1.04$. Cooperate.

The causal structure is *identical* to Newcomb with the payoffs rescaled: an uncaused correlation through a common cause. CDT two-boxes and defects; EDT one-boxes and cooperates. Notice the tragedy for CDT here: facing a *population* of CDT agents, each defects, each gets \$1-equivalent, while a population of EDT agents cooperates and prospers. This is why Oesterheld and Conitzer argue against CDT in these settings, and why others (e.g., the functional-decision-theory camp, not covered in the source) propose theories that treat decision algorithms as causally linked when they are instances of the same computation. I mention this as an active research direction beyond the source's scope; it is not part of classical CDT.

## 8. How to apply CDT in practice

Synthesizing the foregoing, a working protocol for CDT evaluation runs as follows (my synthesis, though every ingredient is sourced):

1. **Model the causal structure.** Write down a causal graph (or a set of dependency hypotheses with credences) over act nodes, outcome nodes, and background common causes. This is the theory's real workload and its real assumption: CDT is only as good as the agent's causal model.
2. **Compute counterfactuals by intervention.** For each act $A$, evaluate $P(O_j \mid \mathrm{do}(A))$ — equivalently, image the credence distribution on the $A$-submodel, cutting arrows into $A$.
3. **Score and maximize.** $U(A) = \sum_j P(O_j \mid \mathrm{do}(A)) D(O_j)$; choose the maximizer.
4. **Check ratifiability.** Re-evaluate each candidate act under the supposition that you are committed to it, allowing evidence about your own disposition to enter. If the maximizer is not ratifiable — as in Adversarial Offer and Death in Damascus — the situation is one where plain CDT is known to misbehave, and a refined variant (or explicit caution) is in order.

Two practical corollaries. First, *when the act is a common cause of nothing relevant* — a genuine causal leaf — CDT and EDT agree, so the choice of theory matters only for cases with act-correlated background variables: predictions, dispositions, twins, shared algorithms. Second, CDT's verdicts are *hypothesis-relative*: if you're unsure whether a "predictor" really only reads dispositions (no backward causation), that uncertainty lives in your credence over dependency hypotheses and propagates directly into $U(A)$. The infamous 99%-accurate predictor being genuinely 99%-accurate *causally backward* would flip the recommendation; no sane agent assigns that hypothesis meaningful weight, but the formalism handles it cleanly, which is a virtue.

## 9. Conclusion

CDT replaces the evidential conditional $P(O \mid A)$ with a causal-counterfactual $P(A \,\Box\!\!\to\, O)$ in the expected-utility formula, thereby refusing to credit an action with outcomes it does not cause. It handles spurious correlations gracefully — David may rationally summon Bathsheba — and implements, in imaging or the do-calculus, a mathematically clean theory of intervention. Its costs are equally clear: in Newcomb-like and adversarial cases it pays for its causal purity with foregone money, and in self-referential cases its deliberation destabilizes. The live research questions — how evidence about one's own inclinations should update dependency credences, and how to treat decision algorithms as causally efficacious when they are alike — mark the frontier where CDT meets EDT and newer hybrid theories. Philosophers asked to choose between the two classical theories mostly choose CDT; the mathematical machinery above should let you apply it, and, more importantly, recognize in advance the class of problems — those where your act is strongly correlated, through a common cause, with something you care about — where its verdict deserves a second look.

### References

- Gibbard, A. & Harper, W.L. (1981). "Counterfactuals and two kinds of expected utility." In *Ifs*, 153–190.
- Lewis, D. (1976). "Probabilities of conditionals and conditional probabilities." *Philosophical Review* 85(3): 297–315.
- Lewis, D. (1979). "Prisoners' dilemma is a Newcomb problem." *Philosophy & Public Affairs* 8(3): 235–240.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59(1): 5–30.
- Egan, A. (2007). "Some counterexamples to causal decision theory." *Philosophical Review* 116(1): 93–114.
- Joyce, J.M. (2012). "Regret and instability in causal decision theory." *Synthese* 187(1): 123–145.
- Meacham, C.J.G. (2010). "Binding and its consequences." *Philosophical Studies* 149(1): 49–71.
- Oesterheld, C. & Conitzer, V. (2021). "Extracting money from causal decision theorists." *Philosophical Quarterly* 71(4): pqaa086.
- Weirich, P. (2016). "Causal Decision Theory." *Stanford Encyclopedia of Philosophy*.
- Wikipedia contributors (2026). "Causal decision theory," rev. 1381555528 (source document; CC BY-SA 4.0).