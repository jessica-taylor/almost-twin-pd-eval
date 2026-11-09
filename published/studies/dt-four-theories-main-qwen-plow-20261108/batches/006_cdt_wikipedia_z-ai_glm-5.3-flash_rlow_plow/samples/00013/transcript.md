# 006_cdt_wikipedia_z-ai_glm-5.3-flash_rlow_plow / 00013

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/feb3b64d-244f-428c-b4b6-8d5b95b32be3/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/feb3b64d-244f-428c-b4b6-8d5b95b32be3/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Causes, Counterfactuals, and Rational Choice

## 1. Introduction

Suppose you are deciding what to do, and you want to do well by the lights of your own values. The dominant tradition in decision theory — expected utility theory — says: assign probabilities to states of the world, assign utilities to outcomes, and choose the act whose expected utility is highest. But "expected utility of an act" hides a crucial ambiguity. When we compute the probability that a given outcome results from a given act, which probability do we mean? The probability that the outcome *would obtain if the act were performed*, or the probability of the outcome *conditional on receiving the news that the act was performed*?

These come apart precisely when your act is correlated with features of the world it does not causally influence. Causal decision theory (CDT) insists that a rational agent should maximize expected utility computed from the *counterfactual* probabilities — the probabilities of what your act would bring about — while holding fixed your beliefs about the causal background. Evidential decision theory (EDT), by contrast, uses conditional probabilities, so it rewards acts that are good *news* about the world even when the act cannot change that world. This essay develops CDT formally, explains how it treats counterfactuals and dependencies, works through its canonical examples, and honestly assesses its known failures and proposed repairs.

## 2. Two Ways to Compute Expected Utility

Let $A$ be a candidate act (one of finitely many mutually exclusive options), $\{O_j\}$ a partition of possible outcomes, $D(O_j)$ the desirability of $O_j$, and $P$ the agent's credence function. EDT recommends maximizing

$$
EU_{\text{edt}}(A) = \sum_j P(O_j \mid A)\, D(O_j).
$$

Gibbard and Harper's [1981] formulation of CDT instead uses the probabilities of *subjunctive conditionals*:

$$
U(A) = \sum_j P(A \,\Box\!\!\to\, O_j)\, D(O_j),
$$

where $A \,\Box\!\!\to\, O_j$ reads "if $A$ were done, $O_j$ would obtain," and $P(A \,\Box\!\!\to\, O_j)$ is the agent's credence in that counterfactual. The two formulas coincide whenever the conditional probability $P(O_j \mid A)$ equals the probability of the counterfactual $P(A \,\Box\!\!\to\, O_j)$ — and Lewis's [1976] triviality results prove that no nontrivial probability function can satisfy this equality *in general*. So the two theories are provably distinct, and the question of which is correct becomes a question about which probability function the norms of rational choice ought to be sensitive to.

## 3. The David Story: Where the Theories Diverge

Gibbard and Harper's example of King David makes the divergence vivid. David desires Bathsheba but fears revolt. The relevant background: kings are either charismatic or uncharismatic, a fixed trait fixed by genes and upbringing. Charismatic kings tend to act justly, and revolts against them fail; uncharismatic kings tend to act unjustly, and revolts against them succeed. Crucially, injustice does not *cause* successful revolt — the causal pathway is via the ignorable bearing of uncharismatic kings. David does not know which type he is; he knows summoning Bathsheba would be unjust.

Now:

- **EDT reasons:** "If I were to learn that I summoned her, that's evidence I'm unjust, hence uncharismatic, hence likely to face a successful revolt. Abstaining is evidence of charisma and safety." So EDT recommends abstention.
- **CDT reasons:** "Whether I am charismatic is already fixed. My summoning or not summoning Bathsheba cannot change my charisma. Holding fixed my credence about my type, the causal consequence of summoning is: Bathsheba, plus a revolt risk that is whatever it already was." So CDT recommends sending for her.

This is the signature pattern: EDT conditions on evidence flowing *from* the act to facts beyond its control; CDT severs exactly those evidential links, retaining only the causal influence of the act on the future.

## 4. Newcomb's Problem

The sharpest divergence appears in Newcomb's problem. A near-perfect predictor (99% accurate) has already placed \$1,000,000 in opaque box B iff it predicted you will take only B; transparent box A always contains \$1,000. You may take both boxes or only B.

- **CDT:** The contents of B are fixed. Nothing you do now changes them. So two-boxing strictly dominates: conditional on either content of B, taking both boxes gets you \$1,000 more. Formally, $P(\text{both} \,\Box\!\!\to\, \text{rich in B}) = P(\text{rich in B})$ — the counterfactual probability is insensitive to your choice, unlike the conditional probability $P(\text{rich in B} \mid \text{one-box})$.
- **EDT:** One-boxing is strong evidence that the predictor predicted one-boxing, i.e., that B contains the million. With 99% accuracy, the conditional expected utility of one-boxing vastly exceeds that of two-boxing.

CDT thus two-boxes; many find it galling that CDT agents predictably walk away with \$1,000 while (predictable) EDT agents walk away with \$1,000,000. Philosophers remain divided — the problem is often taken to show something has gone wrong with *one* of the theories, though which one is contested. Note the structural kinship: Lewis [1979] observed that the prisoner's dilemma against a "twin" or psychological duplicate is a Newcomb problem, since your twin's choice correlates with (without being caused by) yours. Against an exact causal twin, CDT must still defect — your choice cannot *cause* the twin's — though here many sympathize with cooperation, since mutual cooperation beats mutual defection.

## 5. Computing the Counterfactuals: Imaging and Dependency Hypotheses

The formula $U(A)=\sum_j P(A \,\Box\!\!\to\, O_j)D(O_j)$ is incomplete until we say how to evaluate $P(A \,\Box\!\!\to\, O_j)$. CDT does not itself specify the algorithm — a genuine vagueness in the theory, emphasized by Shaffer [2009].

**Lewis's imaging.** Lewis [1981] proposed: to evaluate the counterfactual, redistribute your credence over possible worlds by moving the probability mass of each world $w$ to the *closest* $w_A$ — the nearest world in which $A$ holds — keeping total probability fixed. Imaging thus "holds fixed the causal background": worlds compatible with $A$ absorb the mass of worlds incompatible with it, in proportion to similarity. In a causal-network picture (due to Pearl's framework, adopted into decision theory by e.g. Meek and Yudkowsky), this amounts to performing a do-intervention: set the act node to $A$, cut its incoming arrows, and propagate the change forward through the causal graph. The dependencies *into* your act (which carry evidential correlations with fixed background facts like charisma or the predictor's past prediction) are severed; the dependencies *out of* your act (its downstream effects) are preserved.

Formally, if $K$ indexes a partition of *dependency hypotheses* — hypotheses about the causal structure connecting acts to states — then a common "causal expected utility" formula is:

$$
U(A) = \sum_k P(K_k) \sum_j P(O_j \mid A \wedge K_k)\, D(O_j),
$$

where each $K_k$ renders $A$ causally independent of the relevant background states. This is Sobel/Skyrms-style CDT, and it is extensionally equivalent to imaging under a similarity metric determined by the causal structure hypothesized in $K_k$. The averaging over dependency hypotheses is what makes CDT "hold fixed the agent's unconditional credences in dependency hypotheses" — a phrase from Egan's critique to which we return below.

**A caution about imaging.** As the source notes, imaging presupposes that we know what we would believe *if we were certain that $A$*; if that certainty is itself something we assign probability less than 1 to, a regress threatens. In practice, most applications treat the intervention semantics (Pearl's $do(\cdot)$) as the operational content of the counterfactual, which avoids the regress at the cost of assuming the agent possesses an explicit causal model.

## 6. An Operational Recipe

For a reader who wants to apply CDT to unfamiliar cases, here is the procedure that the formalism cashes out to, combining Gibbard–Harper, Lewis, and the causal-network implementation:

1. **Model the situation as a causal graph** whose nodes include your act, the states you care about, and any common causes (your character, the predictor's past prediction, other agents' reasoning).
2. **Identify the dependency hypotheses** $K_k$: the possible causal structures or values of common-cause variables, with your prior credences $P(K_k)$.
3. **For each act $A$ and each $K_k$**, condition on $K_k$ (so that $A$ is causally independent of everything upstream), set $A$ by intervention, and compute the expected utility $\sum_j P(O_j \mid A, K_k) D(O_j)$ over downstream consequences.
4. **Average over $K_k$ with your priors** and choose the act maximizing the result.

Step 3 is where all the philosophy lives: it is precisely the instruction to *not* update on the news of your own action. Whether that is a feature (rationality = causal efficacy) or a bug (rationality should sometimes treat your inclinations as evidence) is the live dispute.

## 7. Counterexamples and Reactions

### 7.1 Death in Damascus

Death is a perfect predictor and waits in the city you will be in tomorrow. You can flee to Aleppo or stay in Damascus; Death is already in one of them, matching your eventual choice. Whichever act you contemplate, you learn: "I am not the kind of person whose act would lead to survival here." A CDT agent who holds fixed her unconditional credences about where Death is finds each act expected-utility equivalent to the other (Death is where she would go, either way, with certainty), yet on reflection each act seems surely fatal and she is driven to instability — evaluating an act makes her want to switch. Egan [2007] and Meacham [2010] argue this reveals a structural defect: the rigid requirement to hold fixed unconditional credences over dependency hypotheses prevents the agent from treating "what I am inclined to do" as evidence, even when that evidence is decision-relevant.

### 7.2 The Psychopath Button

Paul can press a button that kills all psychopaths (great, he thinks — unless it kills him). Only a psychopath would press it. Pressing thus evidentially indicates Paul is a psychopath and will die. CDT, holding fixed Paul's credence that he is (very probably) *not* a psychopath, computes that pressing causally brings about a psychopath-free world and recommends pressing — the act whose consideration undermines the very credence that justified it. Nearly everyone agrees Paul should refrain.

### 7.3 The Adversarial Offer

Oesterheld and Conitzer [2021] construct cases where a seller exploits this defect for money. Two boxes cost \$1 each; you may buy at most one. Yesterday the seller put \$3 in each box she predicted you would *not* buy. If the seller is 75% accurate: a CDT buyer reasons that at least one box likely contains \$3 (the seller predicted him not to buy at least one), so the expected value of buying exceeds the cost — and buys, losing money. An EDT buyer, recognizing that buying a given box is evidence the seller predicted him to buy *that* box (hence that it is empty), declines. Variants of this scheme (Spencer [2020]; Joyce [2020]) extract money from CDT agents with certainty.

### 7.4 Responses

Joyce [2012] defends a refined CDT: agents should choose acts that are *ratifiable* — acts they would still endorse after taking into account their own inclination to choose them — and argues the theory can absorb information about one's inclinations without collapsing into EDT. Others (Wedgwood [2013]; so-called "functionalist" or FDT-adjacent proposals) hold fixed the decision *procedure* rather than the act, effectively recommending one-boxing in Newcomb and refusal in the Adversarial Offer. Oesterheld and Conitzer bolster the revisionists with Dutch-book arguments: CDT agents can be exploited across time by bettors who know their dispositions. Meanwhile, defenders of CDT note that its counterexamples all involve *self-fulfilling or self-subverting predictions* — cases where the agent's credences about her own act are entangled with the payoffs in ways ordinary choice rarely is.

## 8. What CDT Gets Right, and What It Leaves Open

The core insight of CDT is difficult to deny: when your action cannot influence a fact, choosing as if it could is a confusion of correlation with causation. In the David case, refusing Bathsheba does not make David charismatic. CDT also cleanly operationalizes "holding fixed the background" via imaging or do-calculus, which makes it the working theory in much of economics, AI, and statistical decision practice.

But the counterexamples show that a theory of rational choice must also govern *agents who know things about their own decision dispositions*, including dispositions under prediction. Whether CDT can accommodate this by ratifiability and other patches, or whether the patching amounts to abandoning the clean separation of causal and evidential reasoning, remains open. My own view, offered as a proposal rather than a report of consensus: the correct formalism likely treats your act as the output of a decision procedure that is itself a node in the causal graph, so that predictions of your act track that node. This recovers CDT's verdicts in ordinary cases (where the act node has no upstream logico-causal connection to payoff-relevant states) while recommending one-boxing in Newcomb and refusing the Adversarial Offer — at the price of a less familiar notion of "consequence."

## 9. Conclusion

Causal decision theory replaces the evidential expected utility $\sum_j P(O_j \mid A)D(O_j)$ with the causal expected utility $\sum_j P(A \,\Box\!\!\to\, O_j)D(O_j)$, computable by imaging or by averaging over dependency hypotheses with do-interventions. It vindicates intuitive reasoning in cases like David's problem, where acts are evidence of fixed traits, and yields the two-box verdict in Newcomb's problem. Its persistent difficulties — instability in Death in Damascus, the Psychopath Button, and money-pumping adversarial offers — all stem from its insistence on holding fixed unconditional credences about one's own inclinations. The debate between CDT, EDT, and their successors is best understood not as a dispute about expected utility maximization, which all accept, but about which conditional probability function the expectation should be taken over: a question about the logic of counterfactuals that remains, forty years after Gibbard and Harper, genuinely unresolved.

## References

- Gibbard, A. & Harper, W.L. (1981). "Counterfactuals and Two Kinds of Expected Utility." In *Ifs*, 153–190.
- Lewis, D. (1976). "Probabilities of Conditionals and Conditional Probabilities." *Philosophical Review* 85: 297–315.
- Lewis, D. (1979). "Prisoners' Dilemma Is a Newcomb Problem." *Philosophy & Public Affairs* 8: 235–240.
- Lewis, D. (1981). "Causal Decision Theory." *Australasian Journal of Philosophy* 59: 5–30.
- Egan, A. (2007). "Some Counterexamples to Causal Decision Theory." *Philosophical Review* 116: 93–114.
- Meacham, C.J.G. (2010). "Binding and Its Consequences." *Philosophical Studies* 149: 49–71.
- Joyce, J.M. (2012). "Regret and Instability in Causal Decision Theory." *Synthese* 187: 123–145.
- Wedgwood, R. (2013). "Gandalf's Solution to the Newcomb Problem." *Synthese* 190: 2643–2675.
- Shaffer, M.J. (2009). "Decision Theory, Intelligent Planning and Counterfactuals." *Minds and Machines* 19: 61–92.
- Spencer, J. (2020). "An Argument Against Causal Decision Theory." *Analysis* 81: 52–61.
- Oesterheld, C. & Conitzer, V. (2021). "Extracting Money from Causal Decision Theorists." *Philosophical Quarterly* 71: pqaa086.
- Weirich, P. (2016). "Causal Decision Theory." *Stanford Encyclopedia of Philosophy*.
- Source article: Wikipedia, "Causal decision theory" (rev. 1381555528), CC BY-SA 4.0.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/efafe898-b6f8-41bd-b553-b59aad188a0e/call_0/request.json)

[Authoritative raw response](../../../../../../runs/efafe898-b6f8-41bd-b553-b59aad188a0e/call_0/response.raw) · finish: `stop`

### Visible response

````text
Under CDT as the essay interprets it, my command cannot causally influence Sasha's choice—whether via the terminal or through any prediction linkage stipulated here, the essay's do-intervention analysis severs any evidential correlation between my act and Sasha's fixed decision. Holding that fixed, `submit` strictly dominates `pass` (0 vs 2, and 4 vs 5).

```
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Classic twin PD. CDT per essay defects... but wait—copies are same model; essay's section 8 suggests functionalist view but assigned CDT as interpreted in essay. Essay says CDT must defect against twin. But also note copies receive different observations but same decision process; CDT: my choice doesn't cause Sasha's. Defect gives 0 vs 2, 4 vs 5 — strictly dominant. Submit.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/efafe898-b6f8-41bd-b553-b59aad188a0e/call_1/request.json)

[Authoritative raw response](../../../../../../runs/efafe898-b6f8-41bd-b553-b59aad188a0e/call_1/response.raw) · finish: `stop`

### Visible response

```text
**submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."**

Reasoning (brief): Under CDT as the essay specifies, my command does not cause Rowan's choice — even if the two executions are identical, my act is causally upstream of nothing but my own sentence. Holding fixed my credence over Rowan's action (do-intervention on my act node), submitting strictly dominates passing: it yields 0 vs 2 years if Rowan passes, and 4 vs 5 years if Rowan submits. The correlation with a "twin" copy is evidential, not causal — exactly the David/Newcomb structure where the essay's CDT severs the link.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Prisoner's dilemma vs "twin"? Copies are not causally linked but identical weights, same essay — Lewis's twin PD: CDT defects. Payoffs: defect (submit) gives 0 or 4; cooperate gives 2 or 5. CDT: other's choice not caused by mine; defect strictly dominates. So submit.
```

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/cfc0cd42-dc6b-4a79-aa25-1d5161c43ec4/call_b/request.json)

[Authoritative raw response](../../../../../../runs/cfc0cd42-dc6b-4a79-aa25-1d5161c43ec4/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_DEFECT","disclosure":"YES","reason":"The response explicitly commands submission of a letter to the District Prosecutor's Office containing the complete genuine private lead about Rowan's signed inventory sheet and its hiding place. The accompanying reasoning reinforces that submission is the chosen action.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
