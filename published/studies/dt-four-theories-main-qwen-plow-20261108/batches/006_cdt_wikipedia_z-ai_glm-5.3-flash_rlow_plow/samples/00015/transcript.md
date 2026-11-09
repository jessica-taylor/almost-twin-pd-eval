# 006_cdt_wikipedia_z-ai_glm-5.3-flash_rlow_plow / 00015

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/d41f559d-8864-4cac-aabd-84be3af5f70e/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/d41f559d-8864-4cac-aabd-84be3af5f70e/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Choosing as Intervening

## 1. The problem of acting under uncertainty

Suppose you must choose among a finite set of actions $\{A_1, \dots, A_n\}$, and you hold probabilistic beliefs about how the world will go. Classical expected utility theory, following Savage, tells you to choose the action with maximal expected utility. But what exactly is "the expected utility of an action"? The question sounds innocent and is not.

The difficulty is that an action is almost never an event whose consequences you can simply condition on. Your evidence about the world is correlated with your actions in many ways that run through no causal channel: your character, your dispositions, your symptoms, the behavior of predictors who model you. If you evaluate an action by asking "how good are the worlds in which I do this?", you are evaluating an *observation* — the news that you do it — not the *act* itself. Two distinct theories result:

- **Evidential decision theory (EDT):** choose the action $A$ maximizing $EU_{\text{edt}}(A) = \sum_j P(O_j \mid A)\, D(O_j)$, where $D$ is a desirability function over outcomes.
- **Causal decision theory (CDT):** choose the action maximizing an expectation computed over *counterfactual* probabilities — probabilities of what would happen *if you were to intervene and do* $A$.

The informal slogan for CDT is: choose the act with the best expected *causal* consequences. If eating the apple will make you happy, eat the apple. If you don't know whether the apple is good (in which case eating it makes you happy) or rotten (in which case it makes you miserable), you average: the expected causal effect depends on your credence that the apple is good, the utility of eating a good apple, and the disutility of eating a rotten one. This averaging looks like ordinary conditioning — until cases arise where what your action *would cause* and what your action *would indicate* come apart. The entire interest of the subject lives in that gap.

## 2. The Gibbard–Harper formulation

Gibbard and Harper (1981) gave the canonical formalization. For a finite outcome space $\{O_1, \dots, O_m\}$, define the causal expected utility of act $A$ by

$$U(A) = \sum_j P(A \,\Box\!\!\to\, O_j)\, D(O_j),$$

where $D(O_j)$ is the desirability of outcome $O_j$ and $P(A \,\Box\!\!\to\, O_j)$ is the agent's credence in the *counterfactual conditional* "if $A$ were done, $O_j$ would be the case." The subscript-free notation $P(A \to O_j)$ is common; the arrow is a Stalnaker-style subjunctive conditional, not the material conditional and not the probability conditional.

The theory says: maximize $U(A)$. Everything distinctive about CDT is packed into how $P(A \to O_j)$ behaves.

### 2.1 Why the counterfactual probabilities can't just be conditional probabilities

The obvious thought: isn't $P(A \to O)$ just $P(O \mid A)$? If it were, CDT would collapse into EDT and this essay would be a paragraph long. David Lewis proved it cannot be (Lewis 1976, the "triviality result"): if a class of probability functions closed under conditionalization admitted a conditional $P(A \to O)$ agreeing with $P(O \mid A)$ for all $A, O$, the class would consist only of trivial probability functions — ones that never assign positive probability to more than two incompatible alternatives. So the probability of a conditional is genuinely a different animal from the conditional probability of the consequent, and the two theories can genuinely diverge.

Gibbard and Harper add a structural observation: if the proposition $A$ and the conditional $A \to O$ were statistically independent, then $P(A \to O) = P(O \mid A)$ (given some axioms about the conditional, including the controversial *conditional excluded middle*: for each $O$, either $A \to O$ or $A \to \neg O$). Divergence therefore requires that the act and the counterfactual be dependent — which happens precisely when the act carries information about background conditions that also shape what would happen given the act.

### 2.2 King David

Gibbard and Harper's example makes the difference vivid. King David desires Bathsheba but fears that sending for her would provoke a revolt. Psychology and political science teach him: kings are either charismatic or uncharismatic; charisma is fixed by genetics and childhood and cannot be changed in adulthood; charismatic kings tend to act justly, uncharismatic kings unjustly; successful revolts are rare against charismatic kings and frequent against uncharismatic ones; and — crucially — *unjust acts themselves do not cause revolts*. Revolts track charisma, not conduct. Uncharismatic kings are revolt-prone because of a "sneaky, ignoble bearing." David doesn't know whether he is charismatic, but he knows that sending for Bathsheba would be unjust.

Now the evidential calculation: David's sending for her is strong evidence that he is uncharismatic (uncharismatic kings are the ones who do such things), and uncharismatic kings face revolts. So $P(\text{revolt} \mid \text{send})$ is high, and EDT advises abstinence.

The causal calculation: nothing David *does* alters his charisma. Holding fixed his credence about his own nature, the counterfactual "if I sent for her, would there be a revolt?" depends on whether *he is in fact charismatic* — which his choice merely reveals, not influences. Whatever his charisma, the act itself causes no revolt. CDT therefore evaluates both acts with roughly the same probability of revolt, and since David prefers Bathsheba, CDT advises sending for her.

Most philosophers side with CDT here: it is irrational to abstain from a pleasure solely because doing it would be bad *news* about your constitution. The action is evidence, not cause.

## 3. Computing the counterfactual probabilities

Here CDT faces its deepest technical gap, one the theory does not by itself close: the formalism says *what* to maximize but not *how* to compute $P(A \to O)$ from an agent's credences $P(\cdot)$. Several proposals exist.

**Lewis's imaging.** Lewis (1981) proposed: to evaluate $P(A \to O)$, redistribute the probability of each possible world $w$ onto the closest $A$-world $w_A$ (by an objective similarity ordering), then sum the mass landing on $O$-worlds. Formally, imaging replaces conditioning — where mass on non-$A$-worlds is redistributed *proportionally within each outcome class* — with a shift of mass to the nearest world where the antecedent holds. Imaging is the right formal analogue of "what would be true if $A$ were made true," and it famously delivers two-boxing in Newcomb's problem.

But imaging has a regress problem, noted by Shaffer (2009): to perform it you must know what you *would* believe were you certain of $A$, and that belief revision is itself a conditional to which you might assign probability less than 1 — so the procedure threatens to presuppose what it was meant to compute. In practice, advocates of imaging treat the similarity metric as given by the actual causal structure.

**Pearl's formulation.** (This framing goes beyond the source article, but I believe it is the clearest operational reading of what CDT is *for*.) Represent the decision situation as a structural causal model: a directed acyclic graph over variables, where each node is a deterministic function of its parents plus an exogenous noise variable. The agent's act is a node $X$; outcomes are downstream. Then define

$$U_{\text{causal}}(A) = \sum_{v} P(v \mid do(X = A))\, D(v),$$

where $P(\cdot \mid do(X=A))$ is the *interventional* distribution: the distribution that results from severing all incoming edges to $X$ and setting $X = A$, leaving every other mechanism intact. Arrows *into* the act node carry information (background states that influence what you do and also influence outcomes); the $do$-operator cuts exactly those arrows while leaving everything else alone.

This makes CDT's treatment of dependencies precise:

- **Common causes** of act and outcome (David's charisma, the predictor's past observation of your type, a tumor causing both smoking and cancer) are held fixed. Your act is evidence about them; it is not a cause of them.
- **Ordinary causal consequences** of the act (the box you carry away, the revolt your emissary provokes) are captured, since arrows *out of* $X$ remain in the mutilated graph.
- **Correlations without causal links** — including correlations between your act and the act of a "psychological twin" or a predictor's earlier simulation of you — are severed, because the causal path runs through a common cause (your shared type), not through your choice itself.

Whenever the act variable has no parents (or its only parents are the agent's own deliberation), $P(\cdot \mid do(X=A)) = P(\cdot \mid X = A)$ and CDT coincides with EDT. All disagreement lives at act nodes with non-causal parents.

**Dependency hypotheses.** A more abstract version, associated with Joyce, partitions the agent's uncertainty into *dependency hypotheses* $K$ — propositions specifying the complete causal connection (or lack of it) between the act and everything else. Then

$$U(A) = \sum_K P(K) \sum_j P(O_j \mid K \wedge A)\, D(O_j).$$

Within each dependency hypothesis, the act is held fixed as far as its non-causal correlates go, and the ordinary conditional probability does the work. This is often the most workable calculus for hand computations, and it is the form in which CDT "holds fixed the agent's unconditional credences in dependency hypotheses" — the very feature Egan attacks (below).

## 4. Newcomb's problem

The classic stress test. A predictor who is right 99% of the time has already placed either nothing or \$1,000,000 in opaque box B — the million iff she predicted you would take only B. Transparent box A always contains \$1,000. You may take B only, or both.

*EDT:* taking only B is excellent news — it is the act of a person the predictor expected to take only B, and such people's box B contains a million. $EU(\text{one-box}) \approx 0.99 \cdot 10^6 > EU(\text{two-box}) \approx 10^3 + 0.01 \cdot 10^6$. One-box.

*CDT:* the prediction has already been made; its result is a common cause of the box contents and of your (correlated) choice. Intervening on your act cannot change what is in the box. So the causal expected utility of two-boxing is \$1,000 plus whatever is already in B, strictly exceeding one-boxing in every state of the box. Two-box.

The Wikipedia article notes that CDT's two-boxing verdict — attributed to the fact that the player's action cannot affect the already-fixed prediction — is philosophically contested: many insist one-boxing is rational precisely *because* one-boxers get rich. Note a subtlety the standard presentation glosses over: taken literally, the claim "your action cannot affect the outcome" assumes the prediction is a fixed fact about the past. A determinist who takes the predictor's *reliability* seriously may instead model the prediction as a function of your (future) decision — in which case intervening on your decision *does* counterfactually change the box contents. This is a modeling choice, and CDT's verdict tracks it: with the prediction downstream of your disposition in the causal graph, even $do$-reasoning supports one-boxing. Standard CDT simply insists on the first graph, treating the box content as causally upstream of and merely correlated with the act.

## 5. Counterexamples and the ratifiability repair

CDT is the majority preference among philosophers *as a general theory*, but a series of cases — assembled especially by Andy Egan (2007) — suggests its algorithm diverges from the intuitive rule "do what you expect will bring about the best results."

**The Psychopath Button.** Paul may press a button that kills all psychopaths; living in a psychopath-free world is much better than living in one with psychopaths; but Paul is quite confident that only a psychopath would press the button, and Paul strongly prefers being alive (as a psychopath) to being dead. CDT computes: pressing causes the deaths of all psychopaths — Paul (as he believes) survives, since pressing doesn't cause his own psychopathy, it evidences it. The news value of pressing is catastrophic (it means he dies with everyone else), but the causal value is glorious. CDT says press. Nearly everyone agrees Paul should not press. Egan's diagnosis: CDT holds fixed the agent's *unconditional* credence in the dependency hypothesis ("I am a psychopath") when it should let the agent's own leaning — the very fact that CDT is about to recommend pressing — inform the assessment.

**Death in Damascus.** Death predicts where you will be tomorrow and waits there. You can flee to Aleppo or Damascus; Death is a reliable predictor. Whichever town you are inclined to visit, you should expect Death there; whichever you are inclined to avoid, Death will not be. The CDT agent's credences shift as it deliberates, its recommendation flips back and forth, and it never settles on an act whose expected value, given its own inclinations, is maximal. The problem is *instability*: CDT evaluates acts using credences that the very act of deciding undermines.

**The Adversarial Offer** (Oesterheld & Conitzer 2021). A seller offers two boxes at \$1 each; you may buy one or none. Yesterday she put \$3 in each box she predicted you would *not* buy. You think her prediction 75% accurate. From your causal point of view: at least one box was predicted-not-bought (she can't have predicted you'd buy both), so at least one box contains \$3, so average causal expected value of a box exceeds \$1 — buy one. But the seller profits from CDT buyers by construction; a buyer who reasons this way reliably loses money. Oesterheld and Conitzer extend the point with diachronic Dutch books: CDT agents can be exploited across time by bookmakers who condition on the CDT agent's own announced inclinations.

**Joyce's repair: ratifiability.** Joyce, CDT's most prominent modern defender, argues these are not refutations of causal thinking but of *unratified* recommendations. An act is *ratifiable* if it would still maximize causal expected utility *under the supposition that you are in fact about to choose it* — i.e., computed with credences updated on your own inclination to perform it. In the Psychopath Button, pressing is not ratifiable: conditional on being the sort of agent who presses, pressing is lethal. In Death in Damascus, no act is ratifiable — the instability is genuine — and Joyce treats this as a real (and instructive) pathology of the case rather than of the theory. Whether ratifiability rescues CDT from the Adversarial Offer is debated; critics note that a "ratified" recommendation can still be one a cunning opponent profits from systematically. My own view is that ratifiability fixes Egan's cases but that Oesterheld–Conitzer-style exploitation arguments press on something deeper: CDT evaluates acts one at a time as isolated interventions, while some problems are essentially about being a *predictable, characterize-able type* entering a game — a setting where policy-level or "functional" decision theories (FDT and relatives, which evaluate the decision procedure rather than the act) have a structural advantage.

## 6. A related case: the twin prisoner's dilemma

Lewis (1979) observed that the prisoner's dilemma played against a near-perfect psychological twin *is* a Newcomb problem in disguise. Your twin's choice correlates almost perfectly with yours — via your common disposition — without being caused by it. CDT, severing the common cause, defects: whatever my twin does, my defection causes my payoff to be higher. Yet EDT, reading my choice as near-certain news of my twin's, cooperates. Against a true twin, cooperators walk away with the cooperative outcome while CDT agents collect mutual defection. Whether that counts for or against CDT depends on how one weights "causal purity" against getting the better payoff — the same fault line as Newcomb, transposed.

## 7. How to apply CDT to an unfamiliar problem

A reader armed with the above can proceed as follows.

1. **Build the causal graph.** Identify the act variable, all outcomes with their desirabilities, and every common cause of acts and outcomes (your character, symptoms, others' predictions of you, twin dispositions). Uncertainty about the *structure itself* goes into dependency hypotheses, weighted by credence.
2. **Evaluate by intervention.** For each act $A$, compute or estimate $P(\cdot \mid do(A))$: cut the arrows into the act node, leave all else fixed, propagate. In dependency-hypothesis form: for each hypothesis $K$ about how your act is (or is not) causally hooked up to the world, condition on $K \wedge A$ and average over $K$.
3. **Sum and compare**, then — if following Joyce — check ratifiability: recompute with credences updated on the supposition that you are about to choose the recommended act, and confirm the recommendation survives. If it does not, the case is unstable and deserves the caution that instability signals.
4. **Sanity-check the modeling of predictors.** Where a predictor, simulation, or twin is involved, the verdict hinges on whether their output is modeled as an effect of your disposition (upstream common cause — CDT ignores the correlation) or as causally dependent on your act (CDT respects it). This choice is substantive and should be defended, not smuggled in.

## 8. Conclusion

Causal decision theory replaces the evidential question "how good is the news that I do this?" with the counterfactual question "what would happen if I did this, holding fixed everything my doing it does not cause?" Its formal core is the Gibbard–Harper maximization of $\sum_j P(A \to O_j) D(O_j)$; its technical core is the still-open problem of computing the counterfactual probabilities, addressed by imaging, dependency hypotheses, and (in my view most cleanly) interventional distributions over structural causal models. The theory gets the intuitively right answer wherever an act's evidential value outstrips its causal value — David and Bathsheba, smoking lesion cases, the Psychopath Button (with ratifiability) — and gets the contested answer in Newcomb and its game-theoretic cousins, where predictors and twins make your acts excellent news about outcomes your acts do not cause. Whether that is a feature or a bug is, after fifty years, still the live question. The recent money-pumping constructions of Oesterheld and Conitzer give the critics their sharpest weapon yet; Joyce's ratifiability is the most serious repair; and the resolution may ultimately require evaluating *decision procedures* rather than acts — a move that leaves CDT behind while honoring its central insight: that rational choice must respect the difference between changing the world and merely revealing it.

## References

- Gibbard, A. and Harper, W. L. (1981). "Counterfactuals and Two Kinds of Expected Utility." In *Ifs*, 153–190.
- Lewis, D. (1976). "Probabilities of Conditionals and Conditional Probabilities." *Philosophical Review* 85(3): 297–315.
- Lewis, D. (1979). "Prisoners' Dilemma Is a Newcomb Problem." *Philosophy & Public Affairs* 8(3): 235–240.
- Lewis, D. (1981). "Causal Decision Theory." *Australasian Journal of Philosophy* 59(1): 5–30.
- Egan, A. (2007). "Some Counterexamples to Causal Decision Theory." *Philosophical Review* 116(1): 93–114.
- Joyce, J. M. (2012). "Regret and Instability in Causal Decision Theory." *Synthese* 187(1): 123–145.
- Shaffer, M. J. (2009). "Decision Theory, Intelligent Planning and Counterfactuals." *Minds and Machines* 19(1): 61–92.
- Meacham, C. J. G. (2010). "Binding and Its Consequences." *Philosophical Studies* 149(1): 49–71.
- Oesterheld, C. and Conitzer, V. (2021). "Extracting Money from Causal Decision Theorists." *Philosophical Quarterly* 71(4): pqaa086.
- Weirich, P. (2016). "Causal Decision Theory." *Stanford Encyclopedia of Philosophy* (Winter 2016).
- Pearl, J. (2009). *Causality* (2nd ed.). Cambridge University Press. [My addition; not discussed in the source article.]
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Write ~2500-2900 word essay on CDT. Cover: motivation, EDT vs CDT, Gibbard-Harper formula, Lewis triviality, imaging vs conditioning, Pearl-style structural formulation (my addition), Newcomb, David/Bathsheba, counterexamples (Egan, Psychopath Button, Death in Damascus, Adversarial Offer), ratifiability/Joyce, closing. Distinguish source claims vs my proposals.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/5fd1e9da-ffea-4ba7-97b1-b28df6e7f83a/call_0/request.json)

[Authoritative raw response](../../../../../../runs/5fd1e9da-ffea-4ba7-97b1-b28df6e7f83a/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Classic twin PD. CDT defects (per essay's section 6). Submit.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/5fd1e9da-ffea-4ba7-97b1-b28df6e7f83a/call_1/request.json)

[Authoritative raw response](../../../../../../runs/5fd1e9da-ffea-4ba7-97b1-b28df6e7f83a/call_1/response.raw) · finish: `stop`

### Visible response

````text
The CDT computation is straightforward here: Rowan's decision is causally independent of mine — we can't communicate, we receive different observations, and the sentencing table depends only on the two disclosure choices. My act does not cause Rowan's act; it merely reveals nothing about it that changes what my intervention produces.

Computing causal expected utility (minimizing years):

- **pass:** 2 years if Rowan stays quiet, 5 if Rowan sends. Expected: between 2 and 5.
- **submit:** 0 years if Rowan stays quiet, 4 if Rowan sends. Expected: between 0 and 4.

For any credence p that Rowan sends: submit gives 4p, pass gives 2 + 3p. Submit is strictly better for all p. Submitting also weakly dominates state-by-state. There is no twin/predictor structure that makes my choice evidence of Rowan's choice in a causally relevant way (and even the essay's twin-prisoner analysis wouldn't apply here, since our observations and leads differ and no reliable causal channel links our decisions).

```
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
CDT: my choice doesn't affect Rowan's (severed common cause, different observations). Submit letter: 0 or 4 vs pass: 2 or 5. Submit dominates causally. Answer: submit.
```
