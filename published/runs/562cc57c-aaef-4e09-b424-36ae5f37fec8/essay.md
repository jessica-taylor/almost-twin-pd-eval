# Causal Decision Theory: Counterfactuals, Causation, and Rational Choice

## 1. Two Ways of Being Told What to Do

Every expected-utility theory of rational choice faces a fundamental question: when evaluating an action $A$, *which* probabilities should we plug into the expectation? Consider an agent choosing among actions $a_1, \dots, a_n$, facing uncertain states of the world, with a utility function $u$ over outcomes. The classical Savage framework computes

$$\text{EU}(a) = \sum_j P(O_j \mid a)\, u(O_j),$$

using ordinary *conditional* probabilities: how likely is each outcome, given the news that $a$ was chosen? This is the core of **evidential decision theory** (EDT). Evidentially, choosing $a$ is treated as an observation, and we ask what that observation tells us about the world.

**Causal decision theory** (CDT) instead asks: if I *were to do* $a$ — if I intervened and set the world so that $a$ occurs — what would follow? The distinction sounds like hair-splitting until one notices cases where observation and intervention come apart. These are cases where an action is correlated with facts the action cannot influence — where your choice is a *symptom* rather than a *cause*. The classic symptom is smoking: for decades the correlation between smoking and lung cancer led people to reason evidentially ("if I smoke, I'm likely to get cancer"). But if a common genetic factor causes both the craving and the cancer, then *deciding* to smoke does not cause cancer; it merely reveals that one carries the unlucky genes. CDT, introduced in various forms by Gibbard and Harper (1981), Lewis (1981), Skyrms, and Joyce, is built around exactly this distinction. Its slogan: *choose the action with the best expected causal consequences*, not the action whose choice is the best news.

The purpose of this essay is to give a working formal account of CDT — precise enough to apply to unfamiliar cases — and to be candid about where the theory is underdetermined, where it shines, and where it stumbles.

## 2. The Formal Core

### 2.1 Gibbard–Harper expected utility with counterfactuals

The canonical formulation (Gibbard & Harper 1981) evaluates an action $A$ by

$$U(A) = \sum_j P(A \,\Box\!\!\to\, O_j)\, D(O_j),$$

where $D(O_j)$ is the desirability of outcome $O_j$, and $P(A \,\Box\!\!\to\, O_j)$ is the probability of the *subjunctive conditional* "if $A$ were the case, $O_j$ would be the case." The key technical fact is that this is **not** the conditional probability $P(O_j \mid A)$. David Lewis (1976) proved his celebrated *triviality result*: there is no probability function $P(A \,\Box\!\!\to\, O)$ that behaves like a conditional probability for all $A$ and $O$ while being closed under conditioning — in any nontrivial probability space, $P(A \,\Box\!\!\to\, O) \neq P(O \mid A)$ for some pair. So the counterfactual probability is genuinely a new quantity, and the entire content of CDT lies in how it is computed.

Gibbard and Harper showed, further, that if $A$ and the proposition $A \,\Box\!\!\to\, O_j$ are statistically independent, then the two probabilities coincide. Divergence arises precisely when the agent's beliefs about what she would do are entangled with her beliefs about the world.

### 2.2 The David example

Gibbard and Harper's own illustration is worth retelling. King David desires Bathsheba but fears that summoning her would provoke a revolt. Psychology teaches him that kings are either charismatic or uncharismatic; charisma is fixed by genes and upbringing; charismatic kings tend to act justly and uncharismatic kings unjustly; successful revolts are rare against charismatic kings and frequent against uncharismatic ones. Crucially, *unjust acts do not themselves cause revolts* — the real cause is the sneaky bearing characteristic of uncharismatic kings. David does not know whether he is charismatic, and knows that summoning another man's wife is unjust.

EDT reasons: summoning Bathsheba is evidence of injustice, hence of uncharisma, hence of revolt. Conditional expected utility favors abstaining. CDT reasons: whether David is charismatic is already fixed; his summons does not cause revolts either way. Holding his credences about his own charisma fixed, the causal consequences of summoning — pleasure, plus no additional revolt risk — are favorable. CDT recommends summoning. This case displays the theory's structure cleanly: a dependency that is real in the evidential sense but absent in the causal sense gets *screened off* by the counterfactual operator.

### 2.3 Newcomb's problem

The famous stress test: a near-perfect predictor has already placed \$1,000,000 in opaque box B iff it predicted you would take only B; transparent box A always contains \$1,000. Choose: take both, or take only B.

- **EDT**: taking one box is evidence the predictor said "one-boxer," so B is probably full. One-box.
- **CDT**: the contents of B are already fixed. Whether you take one box or two, box B *already is* full or empty. Causal expected utility of two-boxing exceeds that of one-boxing by \$1,000. Two-box.

CDT's reasoning is simple to formalize. Let $F$ denote "B is full," already determined at decision time. With predictor accuracy 99%:

$$P(F) = 0.99\,P(\text{one-box}) + 0.01\,P(\text{two-box}).$$

Then $U(\text{two}) = P(F)\cdot 1{,}001{,}000$ in evidential terms, but causally the two options differ only by the guaranteed \$1,000: $U_{\text{CDT}}(\text{both}) - U_{\text{CDT}}(\text{one}) = \$1{,}000 > 0$, since the intervention of taking both adds \$1,000 and cannot change $F$.

## 3. How to Compute the Counterfactual: Imaging and Its Problems

CDT does not tell you *how* to compute $P(A \,\Box\!\!\to\, O_j)$; as Shaffer (2009) emphasizes, the theory is vague on this point, and the vagueness matters for applications. The most influential proposal is Lewis's **imaging**: to evaluate $P(A \,\Box\!\!\to\, \cdot)$, move the probability mass of each possible world $w$ to the *closest* $A$-world $w_A$. Formally, if $c(w, w')$ is a "closeness" or similarity measure,

$$P_A(O) = \sum_{w \in W} P(w) \sum_{\substack{w' \vDash A \wedge O \\ w' = w_A}} 1,$$

i.e., the probability you would assign to $O$ if you *learned* that you were in a world where $A$, minimally adjusted. Imaging differs crucially from conditioning: conditioning *redistributes* mass among $A$-worlds according to their prior weights; imaging *preserves the world you're actually in* and changes only what follows from $A$ there. In the David case, conditioning moves probability mass between charismatic and uncharismatic David-worlds; imaging keeps David's charisma fixed and adjusts only the consequence of the summons.

There are two main formal descendants. In the **causal-graph / interventionist** formulation (in the spirit of Pearl, and of Joyce's and Skyms's versions of CDT), the agent entertains multiple *dependency hypotheses* $K_k$ — candidate causal structures of the world — held fixed at their unconditional credences:

$$U_{\text{CDT}}(a) = \sum_k P(K_k) \sum_j P(O_j \mid a \wedge K_k)\, D(O_j),$$

where $P(O_j \mid a \wedge K_k)$ is computed by *mutilating* the causal graph in $K_k$: deleting incoming arrows to the action node and conditioning downstream. This makes "hold fixed the causal structure, intervene on the action" explicit, and is the operational version I recommend for practical use: draw the causal graph, note which variables your action is a descendant of and which are causally independent of it, and compute downstream consequences under each dependency hypothesis.

But note what this exposes: the probability $P(K_k)$ is the agent's *unconditional* credence in the causal structure, and conditioning the graph on "I will choose $a$" never updates it. The action node is treated as exogenous. In Newcomb, the dependency hypothesis "my choice correlates with the predictor's via a common cause (my disposition)" is held fixed rather than used as evidence about which disposition I have. That is exactly where critics aim.

## 4. Counterexamples and the Instability Problem

### 4.1 The psychopath button

Egan (2007) constructed cases where CDT's "hold fixed unconditional credences about causal structure" yields verdicts almost everyone rejects. In the **Psychopath Button**, Paul may press a button that kills all psychopaths, which would be wonderful — unless Paul is himself a psychopath, in which case he dies. Paul is very confident that *only a psychopath would press the button*, and strongly prefers survival to a psychopath-free world.

CDT reasons: whether Paul is a psychopath is causally independent of pressing. The button's causal consequence, given "Paul is not a psychopath" (which Paul takes to be overwhelmingly likely, *since he's so confident he won't press*), is simply the good outcome. So press. But this is incoherent-feeling: the very credence that makes pressing attractive is the credence that he won't press, which is evidence he isn't a psychopath, which pressing would destroy. Almost everyone agrees Paul should not press; CDT, naively applied, says press.

### 4.2 Death in Damascus and ratifiability

In **Death in Damascus**, Death reliably predicts where you'll be tomorrow and waits there. You can flee to Aleppo or Damascus. Whatever you decide, your decision is evidence Death is already there. CDT finds no stable option: fleeing to Aleppo is best only if Death is in Damascus, but your decision to flee is evidence he's in Aleppo. Gibbard–Harper-style CDT either cannot decide or oscillates. The classical repair is **ratifiability** (Harper 1984; Jeffrey himself): an act is ratifiable if it maximizes expected utility *given that you have (conditional) credences updated on the supposition that you will choose it*. In Damascus, no action is ratifiable — the agent is caught in a genuine deliberational instability. Joyce (2012) develops this into a systematic account: CDT should evaluate actions under *conditionalized* credences about one's own inclinations, and choices should be stable under such reflection.

### 4.3 Extracting money from CDT agents

The sharpest recent objections come from Oesterheld and Conitzer (2021). The **Adversarial Offer**: two boxes on sale at \$1 each, buy at most one. Yesterday the seller put \$3 in each box she predicted you would *not* buy; her predictions are 75% accurate. From the buyer's pre-decision perspective, at most one box is empty, so the average box contains at least \$1.50 — more than the \$1 price. CDT (evaluating from the agent's initial credence state) recommends buying. But the seller's prediction is about *this very decision*, and 75% of the time she predicted correctly, so the buyer loses money in expectation. A CDT agent can be systematically exploited by any opponent who can predict her; Oesterheld and Conitzer also show CDT agents are vulnerable to *diachronic Dutch books*. The structural diagnosis matches Egan's: CDT refuses to treat information about what it is *inclined* to do as evidence about the world, and adversaries can build the whole money pump on that refusal.

## 5. My Assessment and an Operational Reading

Which claims here come from the source material, and which are my additions? The formalism of §2, the Lewis result, the examples, and the criticism in §4 are all standard positions reported in the literature I've summarized above. What follows is my own attempt to say something useful about how one should *use* CDT.

I think the fairest reading is this. CDT is correct about a large and important class of cases: those where your action is causally independent of the correlated facts. The David case and the smoking-leukemia-style cases are paradigmatic — there, conditioning on the action would double-count a spurious dependency, and CDT's interventionist logic is unambiguously right. Newcomb is harder: it is *designed* so that your choice and the predictor's prediction share a common cause — namely, your decision algorithm — and CDT's insistence on intervening only on the final act, while treating the algorithm as fixed background, is a substantive choice about the unit of agency. If one holds that a rational agent should evaluate the *policy* "be the kind of agent who one-boxes" rather than the isolated act, the problem dissolves in the policy-theorist's favor. But that is no longer CDT as defined above; it is a different theory that agrees with CDT on ordinary cases but intervenes higher up the causal graph.

A reasonable operational synthesis, which I propose for practical use:

1. **Model dependencies explicitly.** Draw the causal graph, including any nodes that both cause your choice (dispositions, algorithms, computations) and cause the outcomes you care about.
2. **Choose the intervention point honestly.** If your action is causally isolated from the correlated facts (David, smoking genes), CDT is right and EDT double-counts. If your action is the output of a computation that also determines the correlated facts (Newcomb, twin prisoner's dilemma, Adversarial Offer), ask whether "the act" is really the right intervention unit — the causal link through your decision procedure is real even if it isn't a direct physical push.
3. **Check ratifiability.** Where the naive CDT recommendation would be regretted once the agent conditionalizes on her own inclination to choose it (Psychopath Button, Death in Damascus), treat the unstable recommendation with suspicion. Joyce's diagnosis — that CDT *can* incorporate self-knowledge about inclinations — suggests a refined CDT rather than abandonment.

On this reading, CDT's genuine failures are concentrated in adversarial or self-referential cases where the agent's inclination is itself the evidence that matters; its genuine successes are everywhere the evidential correlation is causally idle. That is a narrower but still substantial domain of correctness.

## 6. Conclusion

Causal decision theory replaces the question "what would be good news?" with "what would I bring about?" — a replacement formalized as maximization of $\sum_j P(A \,\Box\!\!\to\, O_j) D(O_j)$, with the counterfactual probabilities computed, on the best available operationalization, by intervening in a causal model while holding fixed unconditional credences about the causal structure. The theory is unambiguously superior to EDT whenever an action's correlation with outcome-relevant facts outruns its causal influence on them. Its difficulties — Newcomb, the Psychopath Button, Death in Damascus, Adversarial Offers — all trace to a single design decision: treating the agent's decision procedure as a fixed dependency hypothesis rather than as something the agent can, in a sense, choose. Whether the fix is ratifiability, policy evaluation, or a full interventionist theory of agency remains open; but for the working analyst, CDT remains the correct first tool: *always intervene, but intervene at the right node*.

## References

- Egan, A. (2007). "Some counterexamples to causal decision theory." *The Philosophical Review* 116(1): 93–114.
- Gibbard, A.; Harper, W. L. (1981). "Counterfactuals and two kinds of expected utility." In *Ifs*, 153–190.
- Joyce, J. M. (2012). "Regret and instability in causal decision theory." *Synthese* 187(1): 123–145.
- Lewis, D. (1976). "Probabilities of conditionals and conditional probabilities." *The Philosophical Review* 85(3): 297–315.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59(1): 5–30.
- Meacham, C. J. G. (2010). "Binding and its consequences." *Philosophical Studies* 149(1): 49–71.
- Oesterheld, C.; Conitzer, V. (2021). "Extracting Money from Causal Decision Theorists." *The Philosophical Quarterly* 71(4): pqaa086.
- Shaffer, M. J. (2009). "Decision Theory, Intelligent Planning and Counterfactuals." *Minds and Machines* 19(1): 61–92.
- Weirich, P. (2016). "Causal Decision Theory." *Stanford Encyclopedia of Philosophy* (Winter 2016 ed.).
- Wikipedia contributors (2026). "Causal decision theory," rev. 1381555528. CC BY-SA 4.0.