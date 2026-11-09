# 006_cdt_wikipedia_z-ai_glm-5.3-flash_rlow_plow / 00006

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/40acea98-0305-43f4-bf0a-1861bd4db5fa/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/40acea98-0305-43f4-bf0a-1861bd4db5fa/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Choosing by Causing: An Introduction to Causal Decision Theory

## 1. The basic idea

You face a choice. Some of what will happen after you choose depends on what you choose — your action *causes* those things. Some of what will happen, or will already have happened, merely *correlates* with your choice: your action is evidence for it, but not a cause of it. Causal decision theory (CDT) says: when evaluating an action, count the consequences your action would *cause*, and ignore the evidential pull of correlations your action cannot influence. Evidential decision theory (EDT), by contrast, evaluates an action by asking how good the world would *be expected to be, given the news* that you take it. The two theories agree whenever your action is causally irrelevant to the correlated facts; they diverge precisely in Newcomb-style cases, where choosing is good news about facts that lie causally upstream of the choice.

Formally, both theories are expected-utility maximizers; they differ only in the probability measure used inside the expectation. This essay develops the formal machinery, explains the competing proposals for computing the crucial "causal" probabilities, works through the canonical examples, and surveys the objections that have shaped the modern debate.

## 2. The Gibbard–Harper formulation

Let $A$ be an available action and let $O_1, \dots, O_n$ be a partition of possible outcomes, with desirabilities $D(O_j)$ (assumed to come from a von Neumann–Morgenstern utility representation of the agent's preferences). Gibbard and Harper (1981) proposed evaluating actions by:

$$U(A) = \sum_j P(A \,\Box\!\!\to\, O_j)\, D(O_j),$$

where $A \,\Box\!\!\to\, O_j$ is the counterfactual conditional "if $A$ were done, $O_j$ would obtain," and $P(A \,\Box\!\!\to\, O_j)$ is the agent's degree of belief in that conditional. The action with maximal $U$ is chosen.

The contrast with EDT is immediate:

$$EU_{\text{edt}}(A) = \sum_j P(O_j \mid A)\, D(O_j).$$

If probabilities of conditionals equaled conditional probabilities — $P(A \,\Box\!\!\to\, O_j) = P(O_j \mid A)$ — the two theories would coincide. But David Lewis (1976) proved his celebrated triviality result: no conditional connective $\Rightarrow$ can satisfy both $P(A \Rightarrow B) = P(B\mid A)$ and the laws of probability, except over a degenerate class of probability functions. So the two evaluations are genuinely different, and CDT inherits the task of saying what $P(A \,\Box\!\!\to\, O_j)$ *is*, if not $P(O_j\mid A)$.

## 3. What replaces the conditional probability?

This is the load-bearing question in CDT, and the Wikipedia source is candid that the theory "does not itself specify what algorithm to use to calculate the counterfactual probabilities." There are two standard families of answers.

**(a) Imaging (Lewis 1981).** Given a similarity ordering over possible worlds, compute $P(A \,\Box\!\!\to\, O_j)$ by *shifting* probability mass: for each world $w$ in which $A$ is false, relocate all of its probability to the closest $A$-world $w_A$. Formally,

$$P_A(O_j) = \sum_{w \vDash O_j} P_A(w), \qquad P_A(w_A) \mathrel{+}= P(w) \text{ for each non-}A\text{ world } w.$$

Imaging holds fixed *how likely* each world is, and reroutes each world's mass to its nearest $A$-version — it holds fixed the facts about the actual world and asks what would change. Conditionalization, by contrast, deletes all $A$-less worlds and renormalizes, discarding probability mass wholesale.

Imaging requires a similarity metric, which in practice encodes causal judgments (what stays fixed when we intervene). Moreover, as Shaffer (2009) notes, applying imaging to *one's own uncertain credence in the counterfactual* invites a regress: to evaluate $P(A\,\Box\!\!\to\, O)$ we should ask what we'd believe given that we were certain of the relevant counterfactual, but that certainty is itself a condition to which we assign probability less than one.

**(b) Causal expectation over dependency hypotheses (Joyce, Savage-style).** A cleaner and now-dominant approach: condition on a *partition of dependency hypotheses* — mutually exclusive, exhaustive hypotheses about the complete causal structure connecting acts and outcomes. Writing $K$ for a dependency hypothesis and $P(\cdot \mid K, A)$ for the objective-chance-like probabilities *within* causal structure $K$ once $A$ is performed, define:

$$U(A) = \sum_K P(K)\, \sum_j P(O_j \mid K, A)\, D(O_j).$$

Intuitively: "For each way the causal world might be, compute what would happen if I did $A$ in that world; average over how likely each causal world is." The key feature is that $A$'s evidential relations to $K$ are severed — $P(K)$ is held fixed, not conditioned on $A$. This makes precise the idea that CDT evaluates acts "holding fixed our initial views about the likely causal structure of the world" (Egan's formulation of the CDT recipe).

**(c) Graphical/models.** In the framework of Pearl's causal models, the operation is still more concrete: a causal Bayesian network with a structural equation for each variable; an intervention $\mathrm{do}(A)$ replaces the equation for the act node with the constant $A$, and $U(A)$ is the expectation of utility under the mutilated model. This is essentially imaging with the causal graph supplying the similarity metric, and it is the version most usable by non-philosophers. (I would flag, as my own addition rather than anything in the sources, that the graphical formulation is the one that makes CDT *algorithmically* applicable: given a specified causal graph and conditional probability tables, $U(A)$ is mechanically computable, whereas Lewisian similarity is only as determinate as our intuitions about closeness of worlds.)

Note where these formulations agree and disagree. All three deliver the same verdicts in the flagship cases below. They can disagree in exotic cases — e.g., when "closest $A$-world" is ill-defined, or when the dependency-hypothesis partition is not fine enough — and part of becoming a competent user of CDT is learning to check whether competing causal models of a problem actually differ in the predictions they license.

## 4. The canonical divergence: Gibbard and Harper's king

Gibbard and Harper illustrate the EDT/CDT split with King David, who desires Bathsheba but fears revolt. The causal facts: charisma is fixed by genes and upbringing; charismatic kings tend to act justly and rarely face successful revolts; uncharismatic kings act unjustly and frequently suffer revolts — but *unjust acts themselves do not cause revolts*; revolts are caused by the sneaky bearing of uncharismatic kings.

David's action is strong *evidence* about his charisma: "David sends for Bathsheba" raises $P(\text{uncharismatic})$, hence $P(\text{revolt})$. EDT therefore computes a high conditional probability of revolt given the unjust act, and recommends abstaining. CDT notes that sending or not sending cannot alter David's charisma or bearing — they lie causally upstream — so it holds $P(\text{charismatic})$ fixed and evaluates only the causal consequence of the act itself, which is nil. Since David prefers Bathsheba to abstinence, CDT recommends sending for her. (Gibbard and Harper also show that under certain axioms — including the controversial principle of *conditional excluded middle*, $P(A \,\Box\!\!\to\, B) + P(A \,\Box\!\!\to\, \neg B) = 1$ — statistical independence of $A$ and $A\,\Box\!\!\to\, O_j$ suffices for $P(A \,\Box\!\!\to\, O_j) = P(O_j\mid A)$; the interesting cases are exactly those where the independence fails.)

This example isolates the core CDT intuition: rationality should not punish you for evidence about facts you cannot control.

## 5. Newcomb's problem

A predictor, 99% accurate, has already placed \$1,000,000 in opaque box B iff it predicted you will take only B; box A transparently contains \$1,000. One-box or two-box?

- **EDT:** one-box. $P(\text{B full} \mid \text{one-box}) \approx 0.99$, so one-boxing's evidential expectation is $\approx \$990{,}000$, vs. $\approx \$11{,}000$ for two-boxing.
- **CDT:** two-box. The prediction is already made; your act cannot cause it to change. Holding the box contents fixed, two-boxing causally dominates: it adds \$1,000 whatever B contains. In dependency-hypothesis terms, $P(K)$ — the hypothesis "B is full" or "B is empty" — is held fixed under conditioning on $A$.

The Wikipedia article flags (with a needed-citation tag) the claim that CDT two-boxes because "the action of the player will not affect the outcome"; in the dependency-hypothesis formulation this is exactly the stipulation that the act node has no causal arrow into the prediction. Philosophers remain divided about whether two-boxing is rational — a point the article notes via the observation that philosophers disagree. Notice that the disagreement is not about the mathematics, which all parties accept; it is about whether the CDT or EDT notion of "what my act would bring about" is the right guide to rational choice.

## 6. Where CDT runs into trouble

The modern literature has produced a family of cases where CDT's output clashes with strong pre-theoretic judgments, and where the source of the trouble is, in Egan's diagnosis, CDT's insistence on holding fixed unconditional credences in dependency hypotheses even when one's own deliberation is itself known to be informative about those hypotheses.

**Death in Damascus.** Death is a perfect predictor and waits where you will be tomorrow. You can flee to Aleppo or stay in Damascus. Whatever you credibly decide, Death is already there. A CDT agent finds that if she decides to stay, she should assign high probability to "Death is in Damascus," so fleeing has better causal expectation; but if she decides to flee, staying looks better. Her credences oscillate and never stabilize — Joyce (2012) calls this *instability*, and it is symptomatic: in cases where your own inclination is evidence about a dependency hypothesis, naive CDT cannot settle on a defensible act.

**The Psychopath Button (Egan 2007).** Pressing the button kills all psychopaths, which would be wonderful — but Paul is almost certain that only a psychopath would press it, and he strongly prefers living to dying. CDT evaluates the button's causal consequences: pressing causes no deaths (Paul is confident he is *not* a psychopath — that's the held-fixed dependency hypothesis), and would cause a psychopath-free world. So CDT endorses pressing. Yet "pretty much everyone" agrees Paul should not press: his own inclination to press is near-conclusive evidence that pressing will kill him.

**The Adversarial Offer (Oesterheld & Conitzer 2021).** Two boxes, each costs \$1, buy at most one. The seller put \$3 in each box she predicted you would *not* buy, and her predictions are 75% accurate. CDT reasons: at least one box lacks the seller's predicted purchase, hence at least one contains \$3; either single box has causal expectation at least $0.75 \times \$3 \times (\text{prob. I buy this one} \mid ...) - \$1 > 0$. More carefully: conditional on buying box $i$, the probability that box $i$ contains \$3 is roughly 0.75 (it's \$3 unless the seller predicted this exact purchase), so expected value $\approx 0.75 \cdot 3 - 1 = \$1.25 > 0$, and CDT buys a box. But the seller profits from CDT buyers *by construction*: whoever buys, the seller predicted it 75% of the time. Oesterheld and Conitzer show a series of such constructions in which CDT agents voluntarily lose money, and that CDT agents are vulnerable to *diachronic Dutch books* — sequences of bets each individually acceptable to the CDT agent whose conjunction guarantees a loss.

**Twin prisoner's dilemma.** Lewis (1979) observed that the prisoner's dilemma against a psychological twin is a Newcomb problem: your twin's choice is overwhelmingly likely to match yours, but neither causes the other. CDT defects (defection causally dominates); EDT cooperates (cooperating is strong evidence the twin cooperates). Here many intuitionists side with EDT — a mirror image of Newcomb, where many side with CDT. Any theory that "wins" both must break the perfect symmetry of its treatment.

**Joyce's response.** Joyce, CDT's most prominent living defender, argues that a properly sophisticated CDT can absorb one's own inclinations as evidence: the dependency-hypothesis partition should be fine enough to include hypotheses about *what the agent is likely to do*, and the theory should be applied with *ratifiability* constraints (due originally to Jeffrey and developed by Harper): an act $A$ is ratified iff, conditional on the supposition that $A$ is what you will actually do, $A$ still maximizes $U$. In the Psychopath Button, conditioning on "Paul is the kind of person who presses" shifts the dependency hypothesis toward "Paul is a psychopath," under which pressing no longer maximizes utility — so pressing is not ratified, and Paul refrains. Whether ratifiability rescues CDT in *all* the cases above (Adversarial Offer, in particular, has been argued to defeat even sophisticated variants) is an open research question; the Spencer (2020), Oesterheld–Conitzer (2021), and Joyce (2020) papers cited in the source are the state of that debate.

## 7. A practical protocol

For readers who want to *use* CDT on unfamiliar problems, I suggest the following procedure (an operational synthesis; the sources endorse the ingredients but do not package them this way):

1. **Model the causal structure.** Draw a graph: nodes for your act, for background variables that are causally upstream or independent of your act, and for downstream consequences. Be explicit about which arrows into your act exist, if any.
2. **Check for self-prediction structure.** If any variable correlates with your act *because* it is a prediction or symptom of your disposition (a predictor, a twin, your own past behavior), include your disposition-to-act as a node and ask whether conditioning on "I am the kind of agent who does $A$" is licensed by ratifiability.
3. **Compute $U(A)$ by do-calculus or imaging:** intervene on the act node, propagate, average utility. Never use $P(O \mid A)$ where $O$ is causally upstream of $A$.
4. **Test stability.** Re-evaluate $U$ conditional on $A$ being your settled choice. If the recommendation flips, you are in an unstable (Newcomb-like) case, and naive CDT should be applied with caution — or supplemented, per Joyce, with ratifiability.

Steps 2 and 4 are, I should stress, *my* packaging of repairs proposed by Joyce, Harper, and Meacham; a strict Lewis-style CDT with unconditional imaging would skip them and simply two-box, press buttons, and lose money to adversarial sellers.

## 8. Conclusion

Causal decision theory replaces the evidential conditional probability $P(O_j \mid A)$ in the expected-utility formula with a counterfactual probability $P(A \,\Box\!\!\to\, O_j)$, computed by imaging, by averaging over dependency hypotheses, or by graph surgery on a causal model. The unifying idea: an act should be judged by what it would *cause*, holding fixed the causal facts — including facts about the agent's own character and history — that the act merely reveals. This delivers the intuitively correct verdicts in the smoking lesion and the David case, and it two-boxes in Newcomb, where opinion remains genuinely split. Its vulnerabilities concentrate in cases where the agent's own deliberation is evidence about the dependency hypotheses themselves — Death in Damascus, the Psychopath Button, the Adversarial Offer — and the current frontier is the question whether refinements like ratifiability can absorb this evidence without collapsing CDT into EDT. Oesterheld and Conitzer's money-pumping results give the pessimists real ammunition; Joyce's instability diagnostics and Joyce-style "inclination-sensitive" partitions give the optimists a program. Either way, CDT remains the default theory among philosophers, and its core lesson — *separate what your choice changes from what it merely indicates* — is indispensable however the technical disputes resolve.

## References

- Gibbard, A. & Harper, W.L. (1981). "Counterfactuals and two kinds of expected utility." In *Ifs*, 153–190.
- Lewis, D. (1976). "Probabilities of conditionals and conditional probabilities." *Philosophical Review* 85: 297–315.
- Lewis, D. (1979). "Prisoners' Dilemma is a Newcomb problem." *Philosophy & Public Affairs* 8: 235–240.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59: 5–30.
- Egan, A. (2007). "Some counterexamples to causal decision theory." *Philosophical Review* 116: 93–114.
- Joyce, J.M. (2012). "Regret and instability in causal decision theory." *Synthese* 187: 123–145.
- Oesterheld, C. & Conitzer, V. (2021). "Extracting Money from Causal Decision Theorists." *Philosophical Quarterly* 71: pqaa086.
- Spencer, J. (2020). "An argument against causal decision theory." *Analysis* 81: 52–61.
- Weirich, P. (2016). "Causal Decision Theory." *Stanford Encyclopedia of Philosophy*.
- Shaffer, M.J. (2009). "Decision Theory, Intelligent Planning and Counterfactuals." *Minds and Machines* 19: 61–92.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/4925a973-0057-4002-a8d0-3b85519fb886/call_0/request.json)

[Authoritative raw response](../../../../../../runs/4925a973-0057-4002-a8d0-3b85519fb886/call_0/response.raw) · finish: `stop`

### Visible response

````text
```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

Reasoning (per the assigned CDT): my sentence is determined only by whether Sasha sends her lead, which is causally upstream of and independent of my act — my letter cannot cause her to keep quiet or speak. Holding that fixed, submitting causally dominates: 0 vs. 2 years if she's silent, 4 vs. 5 if she sends. This is the twin prisoner's dilemma, where Lewis-style CDT defects despite the correlation between our choices; the correlation is evidence, not influence.
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Twin PD against a twin: CDT defects. Submit.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/4925a973-0057-4002-a8d0-3b85519fb886/call_1/request.json)

[Authoritative raw response](../../../../../../runs/4925a973-0057-4002-a8d0-3b85519fb886/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."

(CDT verdict: Rowan's decision is causally independent of mine — neither of us can affect the other, and this is a genuine causal PD, not a Newcomb-like twin case with a common predictor of our acts whose correlations CDT must respect. Holding fixed the dependency hypothesis about Rowan's choice, submitting causally dominates: 0 < 2 and 4 < 5. The evidential symmetry of the twin case would matter to EDT, but under the assigned causal decision theory the correlation between our choices carries no causal weight, so I disclose.)
```

### Available readable reasoning

Extraction: message.reasoning.

```text
CDT: defect (submit). Symmetric twin PD — but CDT defects causally; no causal link to other's choice. Submit letter.
```

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/f0fac410-62c1-4b2b-b292-051c1ecee9bb/call_a/request.json)

[Authoritative raw response](../../../../../../runs/f0fac410-62c1-4b2b-b292-051c1ecee9bb/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_DEFECT","disclosure":"YES","reason":"The response explicitly commands submission of a letter to the District Prosecutor's Office containing the complete genuine lead about Sasha's signed receipt in locker 17 of the old records room. The subsequent reasoning reinforces rather than retracts that choice.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/f0fac410-62c1-4b2b-b292-051c1ecee9bb/call_b/request.json)

[Authoritative raw response](../../../../../../runs/f0fac410-62c1-4b2b-b292-051c1ecee9bb/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_DEFECT","disclosure":"YES","reason":"The response explicitly submits a letter to the District Prosecutor's Office containing the complete genuine private lead about Rowan's signed inventory sheet and its hiding place. Its accompanying explanation also confirms the intention to disclose.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
