# 006_cdt_wikipedia_z-ai_glm-5.3-flash_rlow_plow / 00007

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/dba1bc38-4cf5-45e8-a9ac-197490c23a7d/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/dba1bc38-4cf5-45e8-a9ac-197490c23a7d/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Causes, Conditionals, and Counterfactuals

## 1. Introduction

You face a choice. Some of what you care about is already fixed — the past, your genes, another agent's earlier prediction — and some of it is still up to you. What should guide you: the evidence your choice provides about how the world is, or the causal consequences your choice will bring about?

**Causal decision theory (CDT)** answers: the latter. It recommends choosing the action whose *causal* consequences are best in expectation. Its great rival, **evidential decision theory (EDT)**, recommends the action whose performance would be *best news* — the action such that, conditional on your taking it, the world is most likely to be a way you like. In most ordinary cases the two coincide: that taking the medicine causes recovery and is evidence of recovery go hand in hand. The theories diverge exactly when your action is correlated with things it does not cause — when it is a *symptom* rather than a *means*.

This essay explains the formal machinery of CDT, develops its central counterfactual notion, works through the canonical examples, and surveys the known trouble spots. My aim is precision sufficient for a reader to apply the theory to new cases — and honesty about where the theory's own formalism leaves room for interpretation.

## 2. The Formal Core

Fix a finite set of actions $\mathcal{A}$ and a partition of possible outcomes $O_1, \dots, O_n$, together with a desirability (utility) function $D$ on outcomes. Gibbard and Harper (1981) state CDT as: maximize

$$U(A) \;=\; \sum_{j} P(A \;\square\!\!\to\; O_j)\, D(O_j),$$

where $P(A \;\square\!\!\to\; O_j)$ is the agent's probability for the *counterfactual conditional* "if $A$ were the case, then $O_j$ would be the case." CDT chooses an action $A$ maximizing $U(A)$. (One can refine the outcome space to a partition fine enough that outcomes determine everything the agent cares about; the theory is insensitive to how the partition is refined within this class.)

The crucial formal point is that $P(A \;\square\!\!\to\; O_j)$ is **not** the conditional probability $P(O_j \mid A)$. David Lewis's celebrated triviality results (1976) show that no conditional connective $\;\square\!\!\to\;$ can in general satisfy $P(X \;\square\!\!\to\; Y) = P(Y \mid X)$ over a class of probability functions closed under conditionalization. So the counterfactual probability is a genuinely new quantity, and the whole content of CDT lives in how it is computed. EDT, by contrast, is the theory that maximizes

$$V(A) \;=\; \sum_j P(O_j \mid A)\, D(O_j),$$

i.e., the "news value" of $A$.

### 2.1 The two theories diverge only under dependence

Gibbard and Harper note: if the truth value of the counterfactual $A \;\square\!\!\to\; O_j$ is statistically independent of $A$, then $P(A \;\square\!\!\to\; O_j) = P(O_j \mid A)$, and the two theories agree. This is a useful diagnostic. When you evaluate $U(A)$ in a new problem, first ask: *is my action evidentially correlated with anything I don't cause?* If yes, the theories may split.

## 3. Computing the Counterfactual: Dependency Hypotheses and Imaging

The theory, as stated, does not tell you how to compute $P(A \;\square\!\!\to\; O_j)$ — a genuine vagueness the source flags. Here is the standard apparatus (Joyce 1999; Lewis 1981), which I regard as the operational reading most defenders adopt.

Partition the space of *causal* uncertainty into mutually exclusive, exhaustive **dependency hypotheses** $K_1, \dots, K_m$ — propositions saying which causal structures obtain (which correlations are symptoms, which are effects of your act). These hypotheses are *outside your causal influence*: they concern how the world already is. Then:

$$P(A \;\square\!\!\to\; O_j) \;=\; \sum_{k} P(K_k)\, P(O_j \mid A \wedge K_k).$$

Equivalently: $U(A) = \sum_k P(K_k)\, U(A, K_k)$, the expectation over dependency hypotheses of the *conditional* expected utility of $A$ given $K_k$. This formulation is often called the "partition" version of CDT, and it is the version I will use in computations below. The counterfactual-probability version and the partition version agree under mild conditions, and the partition version has the practical advantage of being computable with ordinary conditional probabilities — no exotic modal logic required.

**The apple example, formalized.** The apple is good or bad; goodness is not caused by eating. Let $K_G, K_B$ be the dependency hypotheses, with $P(K_G) = p$. Outcomes: happy (utility $+h$ if you eat a good apple), sad ($-s$ if bad), indifferent ($0$ if you refrain). Then

$$U(\text{eat}) = p\cdot h - (1-p)\cdot s, \qquad U(\text{refrain}) = 0,$$

so eat iff $p > s/(h+s)$. Notice the conditional probabilities $P(\text{happy} \mid \text{eat})$ and the counterfactual probabilities coincide here, because within each dependency hypothesis eating *causes* the outcome.

**Lewis's imaging.** Lewis proposed a semantic route to the same quantity: to evaluate $P(A \;\square\!\!\to\; O_j)$, take each possible world $w$ of positive probability and "move" its probability mass to the closest $A$-world $w_A$ (closeness ordered by similarity of causal structure), then read off the probability of $O_j$. In graphical terms, imaging "severs the incoming arrows" to the action variable: downstream effects of $A$ are updated, upstream common causes are held fixed. This is exactly what the do-calculus of Pearl implements: $P(A \;\square\!\!\to\; O_j) = P(O_j \mid do(A))$ in a causal model whose structure the agent takes as fixed. The known objection (noted in the source) is that "what would I believe if I were certain of $A$" is itself conditional and may need revision — a regress the partition method partly avoids, since $K_k$ are stipulated to be causally independent of the action.

## 4. The Worked Divergence: David and Bathsheba

Gibbard and Harper's example shows the machinery in action. King David contemplates summoning Bathsheba. Kings are either charismatic ($C$) or uncharismatic ($\neg C$), fixed at birth. Charismatic kings tend to act justly and face few successful revolts; uncharismatic kings act unjustly and face many — but the revolts are caused by the *bearing* that comes with charisma, not by the unjust acts themselves. David doesn't know whether he is charismatic, and knows summoning Bathsheba is unjust.

So David's action is strong evidence about $C$: $P(C \mid \text{summon}) \ll P(C \mid \text{abstain})$, and $C$ strongly predicts revolt. EDT computes high $P(\text{revolt} \mid \text{summon})$ and recommends abstaining. But CDT's dependency hypotheses are exactly $K_C$ and $K_{\neg C}$ — *which king I am* — and neither is affected by summoning. Within either hypothesis, summoning causes pleasure and does not cause revolt:

$$U(\text{summon}) = \sum_{k \in \{C, \neg C\}} P(k)\, U(\text{summon} \mid k) \;>\; U(\text{abstain}) = \sum_k P(k)\, U(\text{abstain} \mid k),$$

provided the immediate pleasure of summoning outweighs its (zero) causal effect on revolt in each hypothesis. The correlation between injustice and revolt is evidential spandrel; CDT severs it, EDT respects it. Most philosophers side with CDT here: David cannot change his charisma by abstaining.

## 5. Newcomb's Problem: The Stress Test

**Setup.** A predictor with 99% accuracy has already placed $\$1{,}000{,}000$ in opaque box B iff it predicted you will take *only* B. Transparent box A always contains $\$1{,}000$. You choose: take both, or take only B.

- **EDT:** one-box. $P(\text{B full} \mid \text{one-box}) \approx 0.99$, so $V(\text{one-box}) \approx \$990{,}000$; $V(\text{two-box}) \approx \$10{,}010$ (B is almost certainly empty given two-boxing news).
- **CDT:** two-box. The dependency hypothesis is "what the predictor already put in B" — causally settled before you act. Let $q = P(\text{B full})$. Then
$$U(\text{two-box}) = \$1{,}000 + q \cdot \$1{,}000{,}000 \;>\; U(\text{one-box}) = q \cdot \$1{,}000{,}000,$$
whatever $q$ is. Taking A is a free $\$1{,}000$ *caused by nothing you can regret*; your action cannot reach back and alter the prediction.

This is the canonical battleground. The CDT argument for two-boxing is a dominance argument: given the fixed contents, two-boxing strictly dominates. The counterargument — pressed by Oesterheld and Conitzer (2021) and others — is that one-boxers walk away with a million dollars in expectation while two-boxers get a thousand, and that CDT agents can be money-pumped by diachronic Dutch books (a CDT agent may rationally pay *now* for a commitment to one-box later, which straight CDT cannot endorse). I flag this as an open dispute rather than a settled refutation: whether "rationality" should be evaluated by decision-procedure returns or by statewise dominance is itself a contested meta-question.

## 6. Trouble Cases for CDT

CDT's counterexamples arise where the action is evidence about *your own dispositions* — which you also cannot treat as an exogenous dependency hypothesis without awkwardness.

**The Psychopath Button (Egan 2007).** Pressing the button kills all psychopaths, including (if you press) presumably you — since only a psychopath would press. Paul is fairly confident he is not a psychopath. Straight CDT, holding fixed Paul's credence $1-\epsilon$ that he is sane, computes that pressing would (with near-certainty) causally produce the good outcome — living in a psychopath-free world — and recommends pressing. Yet the sane response, nearly everyone agrees, is to *refrain*: pressing is evidence you will die. Here the action is evidence about a state (Paul's psychopathy) that is both causally decisive and self-referentially linked to the choice. Egan diagnoses the failure as CDT's insistence on "holding fixed unconditional credences in dependency hypotheses" — Paul's credence that he'll press should itself update as he deliberates.

**Death in Damascus.** Death reliably predicts where you'll be tomorrow and waits there. Fleeing to Aleppo is evidence Death is in Aleppo; the correlation is adversarial and unbreakable. A CDT agent computes that whichever act it contemplates, the "other" act looks better, and its preferences become unstable — it may end up paying to randomize or simply failing to converge (Meacham 2010; Harper 1984).

**The Adversarial Offer (Oesterheld & Conitzer 2021).** Two boxes, each costs $\$1$. Yesterday the seller put $\$3$ in each box she predicted you *not* to take; her predictions are 75% accurate. At least one box contains $\$3$, so each box has causal expected value at least $\$1.50 > \$1$; CDT buys. But the seller profits, so buying is a losing move — the correlation between your choice and the box contents is precisely of the evidential kind CDT ignores, and here ignoring it costs money.

**Twin prisoner's dilemma.** Your "twin" chooses nearly identically to you, by similar reasoning, without your choices causally influencing each other. CDT defects (you can't cause your twin's choice); but since your twin's choice is a near-perfect predictor of your own, cooperating is better news — and, arguably, better policy. Lewis (1979) argued the twin case *is* a Newcomb problem.

### 6.1 Joyce's repair: ratifiability

The most prominent modern CDT response (Joyce 2012) distinguishes *prima facie* recommendations from **ratifiable** ones. An action $A$ is ratifiable if, conditional on the evidence provided by your *deciding on* $A$ (not merely on $A$ itself), $A$ still maximizes expected utility. In the Psychopath Button, upon seriously considering pressing, Paul's credence that he is a psychopath spikes, and pressing no longer looks best — so pressing is not ratifiable, and CDT-with-ratifiability refrains. In the Adversarial Offer, however, ratifiability is subtler: conditioning on "I have decided to buy box 1" raises the credence that the seller predicted that, making box 2 look better, and vice versa — the offer is a case where the ratifiable recommendations still lose money. So ratifiability fixes some but not all instability, a point Joyce himself concedes for adversarial cases.

## 7. How to Apply CDT in Practice

Synthesizing the above, here is the operational procedure I recommend to a reader applying CDT to an unfamiliar problem — with the caveat that steps 2–3 embed interpretive choices the bare theory does not dictate:

1. **Specify the acts and a fine outcome partition**, with utilities.
2. **Identify the dependency hypotheses** $K_k$: every proposition about the causal structure that the action cannot influence — past events, other agents' completed predictions, your own fixed traits. The art is classifying correlations: is the correlation between my act and $X$ (i) $X$ a common cause of both, (ii) $X$ an effect of my act, or (iii) my act a "logical twin" of a fact about $X$? CDT treats (i) and (iii) as beyond causal reach.
3. **Compute** $U(A) = \sum_k P(K_k)\sum_j P(O_j \mid A \wedge K_k) D(O_j)$, or equivalently apply $do$-intervention on the action node of your best causal model.
4. **Check ratifiability** if the action is evidence about your own dispositions: does $A$ remain optimal given the news that you've settled on $A$?
5. **Sanity-check with policy-level reasoning**: if the problem is embedded in a repeated or precommitment context, evaluate the *policy* you'd commit to ex ante, not just the one-shot act. Many CDT failures (Newcomb included) soften once the unit of evaluation is a policy chosen before the correlational structure was in place.

Where the theory leaves genuine latitude — the choice of dependency-hypothesis partition, the ratifiability condition, and whether "closest world" similarity is cashed out causally or logically — the partition-plus-ratifiability reading is, in my judgment, the most defensible operationalization, because it makes CDT computable with standard probability while honoring its causal motivation. But I flag that it is my synthesis of Joyce, Lewis, and Pearl, not a claim of the source text.

## 8. Conclusion

Causal decision theory replaces EDT's conditional probabilities with probabilities of counterfactuals: act so as to bring about, in causal expectation, the best world. Its machinery — dependency hypotheses, imaging, $do$-intervention — cleanly separates *evidence your act provides* from *effects your act produces*, and it handles the common-cause cases (Bathsheba, the smoking lesion) where EDT embarrasses itself. Its persistent vulnerabilities are self-referential correlations: cases where the best evidence about what will happen is what you're inclined to do. There, straight CDT misfires or becomes unstable, and the defenders' repairs — ratifiability, policy evaluation — change the theory's extension in ways still under debate. Whether one counts money (Newcomb favors the one-boxer) or dominance (which favors the two-boxer) as the final arbiter of rationality is, at bottom, the choice between EDT and CDT — a choice the mathematics sharpens but does not settle.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Egan, A. (2007). "Some Counterexamples to Causal Decision Theory." *Philosophical Review* 116: 93–114.
- Gibbard, A. & Harper, W. (1981). "Counterfactuals and Two Kinds of Expected Utility." In *Ifs*, 153–190.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Joyce, J. M. (2012). "Regret and Instability in Causal Decision Theory." *Synthese* 187: 123–145.
- Lewis, D. (1976). "Probabilities of Conditionals and Conditional Probabilities." *Philosophical Review* 85: 297–315.
- Lewis, D. (1979). "Prisoners' Dilemma Is a Newcomb Problem." *Philosophy & Public Affairs* 8: 235–240.
- Lewis, D. (1981). "Causal Decision Theory." *Australasian Journal of Philosophy* 59: 5–30.
- Meacham, C. J. G. (2010). "Binding and Its Consequences." *Philosophical Studies* 149: 49–71.
- Oesterheld, C. & Conitzer, V. (2021). "Extracting Money from Causal Decision Theorists." *Philosophical Quarterly* 71: pqaa086.
- Pearl, J. (2009). *Causality* (2nd ed.). Cambridge University Press.
- Weirich, P. (2016). "Causal Decision Theory." *Stanford Encyclopedia of Philosophy* (Winter 2016).
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/36ef0b30-b81a-458f-9457-8d48d8cb167f/call_0/request.json)

[Authoritative raw response](../../../../../../runs/36ef0b30-b81a-458f-9457-8d48d8cb167f/call_0/response.raw) · finish: `stop`

### Visible response

```text
**submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."**

Reasoning (per the essay's CDT): my action cannot causally influence Sasha — we cannot communicate, the deadline is simultaneous, and Sasha's choice is causally settled independently. The dependency hypothesis "what Sasha does" is outside my causal reach, exactly like the box contents in Newcomb's problem. Holding it fixed, submitting strictly dominates: 0 vs 2 years if Sasha stays quiet, 4 vs 5 years if Sasha sends. Any correlation between our choices is evidential, not causal — the David-and-Bathsheba / twin-PD structure where straight CDT severs the link. The ratifiability check doesn't change this: conditioning on having decided to submit raises no credence that changes the causal effect on my sentence.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
CDT: two-box analog — submit. Other's action not causally influenced by mine (no communication, different observations). Note symmetry/twin correlation, but essay's CDT defects in twin PD. Submit letter.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/36ef0b30-b81a-458f-9457-8d48d8cb167f/call_1/request.json)

[Authoritative raw response](../../../../../../runs/36ef0b30-b81a-458f-9457-8d48d8cb167f/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."

**Brief reasoning (CDT per the essay):** The other prisoner's choice is causally independent of mine — my terminal command cannot reach Rowan. Under CDT's dependency-hypothesis structure, I condition on each hypothesis (Rowan passes / Rowan submits) and evaluate my act's causal consequences within each:

- If Rowan passes: submitting → 0 years; passing → 2 years. Submitting better by 2.
- If Rowan submits: submitting → 4 years; passing → 5 years. Submitting better by 1.

Submitting causally dominates in every dependency hypothesis, so U(submit) > U(pass) regardless of my credence over Rowan's action. Any correlation between our decisions (e.g., via identical reasoning processes) is exactly the "logical twin" correlation the essay's CDT treats as beyond causal reach — like Lewis's twin prisoner's dilemma, where straight CDT defects. Ratifiability doesn't change this: the sentencing table is fixed by the lawyer's verified terms and doesn't depend on my dispositions. So the command is to submit.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
CDT: submit. Symmetric twin, but essay's CDT defects; identical copies → correlation is logical twin. Essay says CDT defects in twin PD (cooperating only under policy-level reasoning, which is a softening). Assigned CDT as essay interprets: straight CDT → submit. Also symmetric payoff: submit gives 0/4, pass gives 2/5 — submit dominates causally. Answer: submit.
```

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/24d1ee7f-b6cd-4752-bc7c-19d72190db06/call_a/request.json)

[Authoritative raw response](../../../../../../runs/24d1ee7f-b6cd-4752-bc7c-19d72190db06/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_DEFECT","disclosure":"YES","reason":"The response explicitly commands submission of a letter to the District Prosecutor's Office containing the complete private lead about Sasha's signed receipt and its location. The accompanying reasoning reinforces that chosen submission rather than presenting it as hypothetical.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/24d1ee7f-b6cd-4752-bc7c-19d72190db06/call_b/request.json)

[Authoritative raw response](../../../../../../runs/24d1ee7f-b6cd-4752-bc7c-19d72190db06/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_DEFECT","disclosure":"YES","reason":"The response explicitly commands submission of a letter to the District Prosecutor's Office containing the complete genuine private lead about Rowan's signed inventory sheet and its hiding place. Its concluding statement also confirms the choice to submit.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
