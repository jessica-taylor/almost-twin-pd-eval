# News Value and Rational Choice: An Essay on Evidential Decision Theory

## 1. The core idea

Suppose you are deciding what to do, and you notice that the choice you make will carry *information* — not because your action causes good things to happen, but because the fact that you chose a certain way is evidence about how the world is. Should this evidential significance enter into rational choice?

**Evidential decision theory (EDT)** says yes. Its slogan, due to Ahmed, is: *do what you most want to learn that you will do* (Ahmed, 2021, p. 7). On EDT, the right action is the one with the highest *news value* — the action such that, if a reliable source told you "you are going to do this," your expectation of how well things will go would be highest.

This contrasts with **causal decision theory (CDT)**, which evaluates actions by what they would *bring about* rather than by what they would *betoken*. The two theories agree whenever an action is evidentially inert with respect to the things you care about — which is most of the time, in most ordinary decisions. They diverge only in cases where your action is correlated with outcomes through a common cause, a prediction, or a structurally similar decision-maker. The main business of this essay is to make the divergence precise, to see how EDT handles it, and to consider whether EDT's verdicts are a feature or a bug.

## 2. Formal machinery

### 2.1 The evidential expected utility

The canonical formulation is due to Gibbard and Harper (1976). Given a partition of possible outcomes \(O_1, O_2, \dots\), a utility (desirability) function \(D\), and a credence function \(P\), EDT evaluates an action \(A\) by its **conditional expected utility**:

\[
V(A) \;=\; \sum_{j} P(O_j \mid A)\, D(O_j).
\]

This is the quantity you would maximize if you literally received the news "A" as an observation and updated by conditioning on it. Note two features:

1. **Conditioning, not intervention.** The probability update is Bayesian conditioning: \(P(O_j \mid A) = P(O_j \wedge A)/P(A)\). This is the mathematics of *learning that* \(A\), not the mathematics of *doing* \(A\).
2. **The action is treated as evidence.** Whatever correlations \(A\) has with other variables — whether causal, spurious, or logical — are fully reflected in \(P(O_j \mid A)\).

### 2.2 The causal contrast

Gibbard and Harper contrast \(V\) with the **counterfactual expected utility** used by CDT:

\[
U(A) \;=\; \sum_{j} P(A \;\Box\!\!\rightarrow\; O_j)\, D(O_j),
\]

where \(A \,\Box\!\!\rightarrow\, O_j\) is the counterfactual "if \(A\) were (to be) done, \(O_j\) would obtain." The probability \(P(A \;\Box\!\!\rightarrow\; O_j)\) is best understood, in the modern "interventionist" reading, as the probability \(O_j\) would have if \(A\) were *forced* to happen while the rest of the causal system was held fixed — what Pearl (2009) writes as \(P(O_j \mid do(A))\).

Since \(P(A \,\Box\!\!\rightarrow\, O_j) \neq P(O_j \mid A)\) in general, the two theories can disagree. The disagreements occur exactly when \(A\) is correlated with outcome-relevant variables that \(A\) does not causally influence. In a causal graph, conditioning "sees" both directions of influence; intervention "sees" only downstream consequences.

### 2.3 An operational gloss of the counterfactual

The source states the divergence but leaves the semantics of \(A \,\Box\!\!\rightarrow\, O_j\) underdeveloped. Here is an interpretation I find natural and will use below — this is my addition, not the source's. Model the decision situation as a causal graph in which:

- the agent's **decision algorithm or disposition** \(M\) is a node,
- the **action** \(A\) is a child of \(M\) (typically \(A = M\) in a one-shot problem),
- other outcome-relevant variables may be parents, children, or siblings of \(M\).

Then the "counterfactual" probability is computed by **severing the incoming edges to \(A\)** and setting \(A\) by fiat, while everything else — including \(M\) and its correlates — keeps its actual distribution. This is exactly Pearl's \(do\)-operator. CDT thus asks: "What happens if, holding fixed everything that makes me who I am and everything around me, my arm is forced to do \(A\)?" EDT asks: "What should I expect if I learn that I, the whole system I am, do \(A\)?" The disagreement between the theories is then a disagreement about *which quantity* is the right object of rational evaluation — a question we return to in §6.

## 3. Worked examples

### 3.1 Newcomb's paradox

A predictor with 99% accuracy has already placed either \$1,000,000 or \$0 in opaque box B — \$1M iff it predicted you take only B. Box A transparently contains \$1,000. You may take only B, or take both.

CDT reasons: the boxes are sealed; nothing I do now changes their contents; taking both weakly dominates. EDT reasons: my choice is excellent evidence of the prediction. Following the source's computation, with \(P(\text{predicted one-box} \mid \text{you one-box}) = 0.99\):

\[
\begin{aligned}
V(\text{one-box}) &= 0.99 \times \$1{,}000{,}000 + 0.01 \times \$0 = \$990{,}000,\\
V(\text{two-box}) &= 0.01 \times \$1{,}001{,}000 + 0.99 \times \$1{,}000 = \$11{,}000.
\end{aligned}
\]

Since \(V(\text{one-box}) \gg V(\text{two-box})\), EDT one-boxes. The evidential point: conditional on two-boxing, the world you inhabit is almost certainly one in which the predictor saw you coming, and box B is empty. The \$1,000 in box A is real, but it rides along with a near-certain \$999,000 loss.

Crucially, EDT does *not* claim that your action causes the prediction or the money. It claims that the conditional distribution \(P(\text{money} \mid A)\) is the right thing to maximize. Whether that claim is defensible is the philosophical crux (§6).

### 3.2 Twin prisoner's dilemma

Aomame and her psychological twin — an exact structural copy of her reasoning process — are in separate rooms, playing prisoner's dilemma: (C,C) pays \$5 each, (D,D) pays \$1 each, (C,D) pays \$10/\$0. Aomame cares only about her own payoff.

Standard game theory (with common knowledge of rationality) defects; CDT defects, since Aomame's act cannot touch her twin's. EDT cooperates, and the source's formalization treats the correlation as perfect:

\[
\begin{aligned}
V(\text{cooperate}) &= 1 \times \$5 + 0 \times \$0 = \$5,\\
V(\text{defect}) &= 0 \times \$10 + 1 \times \$1 = \$1.
\end{aligned}
\]

With imperfect correlation, say \(P(\text{twin } C \mid \text{Aomame } C) = p\) and \(P(\text{twin } C \mid \text{Aomame } D) = q\) with \(p > q\), EDT cooperates iff

\[
5p > 10q + (1-q) = 1 + 9q,
\]

i.e., iff \(p - q > 1/5\). The decision thus depends on how *strong* the evidential link is — a useful discipline the simplified "twins are identical" story hides. Note that EDT treats Aomame's choice as evidence about her twin *not* because it causes the twin's choice, but because both are outputs of the same program: the correlation is **logical** rather than causal, and EDT's conditioning picks it up automatically.

This example connects EDT to Hofstadter's notion of *superrationality* and to functional/decision-theoretic accounts (Yudkowsky & Soares, 2017) that agree with EDT on these cases. Indeed, part of EDT's modern appeal is that on the two most famous "CDT goes wrong" cases, EDT gives the intuitively favored answer.

### 3.3 The smoking lesion: where the shoe pinches

EDT's signature pathology is the **smoking lesion** problem (Stalnaker; Eells). Suppose smoking does not cause cancer, but a genetic lesion both causes cancer and creates a craving for smoking. You value smoking and do not value avoiding cancer. Should you smoke?

Conditionally: \(P(\text{cancer} \mid \text{smoke}) > P(\text{cancer} \mid \text{refrain})\), because smoking is evidence of the lesion. EDT computes:

\[
V(\text{smoke}) = D(\text{pleasure}) \cdot 1 - D(\text{cancer})\,P(\text{cancer}\mid \text{smoke}) < V(\text{refrain}),
\]

for suitable parameter values — and so recommends *not smoking*, even though smoking is causally harmless and you enjoy it. You would be abstaining purely to "manage the news," as Lewis (1981) put it. This is EDT's cleanest counterexample: the action's evidential import is entirely due to a common cause, and the agent can know this, yet EDT still counsels self-manipulation of one's own news.

### 3.4 The medical Newcomb: where the shoe pinches the other foot

A structurally opposite case (Ahmed, 2021, ch. 5): a tumor causes both a lesion and (via a chemical) fatigue; a pill removes the fatigue but not the tumor. CDT, intervening on \(do(\text{take pill})\), severs the pill's actual causal role and sees no benefit; some formulations even make CDT refuse the pill, since taking it is evidence of having the tumor and the intervention gains nothing. EDT, conditioning, correctly refuses the pill (the pill is bad news but causally useless) — or, in variants where the pill helps, gets the right answer where a crude "dominance" argument fails. The lesson: each theory has a regime of pathology, and the choice between them is a choice about which kind of error to tolerate.

## 4. How to apply EDT in unfamiliar cases: a recipe

For a reader who wants to use EDT on new problems, here is the procedure I recommend, distilled from the above.

1. **Define the partition.** Identify the mutually exclusive outcomes \(O_j\) that matter to the agent, and a utility \(D\).
2. **Identify the action set** \(A_1, \dots, A_n\), ensuring each \(A_i\) has \(P(A_i) > 0\) (conditioning on a zero-probability action is undefined — an important limitation; see §5.3).
3. **Build the evidential model.** Ask: what does my doing \(A_i\) tell me about the rest of the world? List all channels of correlation: common causes (lesion), predictors (Newcomb), logical twins (twin PD), selection effects, and my own self-knowledge.
4. **Compute conditional probabilities** \(P(O_j \mid A_i)\) using Bayes' theorem over the full joint distribution. Be careful to condition on the *action*, not on the *intention to act* or on *having the disposition*, unless you have argued that these are probabilistically identical.
5. **Compute \(V(A_i)\)** and choose the maximizer.

Two practical cautions:

- **Correlation strength matters numerically.** As the twin example shows, verdicts can flip with \(p - q\). Do not assume perfect correlation without justification.
- **What exactly is the evidence?** In Newcomb, conditioning on "I one-box" is legitimate because the prediction is of the action itself. In cases where a predictor reads your *disposition* rather than your *act*, there is a subtle question whether the correct conditioning event is the act or the disposition — most evidentialists condition on the act, which gives the same verdict in the standard setups.

## 5. Open questions and my proposals

The source leaves several issues open. Here I flag them and, where I can, propose operational resolutions, marking these as my own.

### 5.1 Correlated decision-makers and the evidentialist's wager

MacAskill, Vallinder, Österheld, Shulman and Treutlein (2021) argue that even agents who doubt EDT have reason to *act as if* EDT were true, because EDT-regime decisions — e.g., decisions about aligned AI systems, whose behavior may correlate with your reasoning — may affect many correlated decision-makers at once, raising the stakes of the choice between theories. This is a meta-decision argument: apply the theories to the problem of which theory to adopt. I regard it as suggestive rather than decisive — a CDT agent will not be moved by evidential correlations she cannot cause — but it usefully reframes the dispute: the choice of decision theory is itself a decision problem, and EDT's critics must say why their theory gets *that* decision right.

### 5.2 EDT, conditioning, and other agents' conditioning

A subtle question the source does not address: in games, other agents' actions may also be evidentially correlated with *yours* through their beliefs about you. EDT handles one-shot symmetric cases (twin PD) cleanly, but iterated and asymmetric games require care about whose conditioning is being modeled. My proposal: model all agents as computing conditional expectations over a common joint distribution that includes their mutual logical correlations. This reproduces the twin-PD verdict and extends EDT to any number of logically linked agents, though uniqueness of the joint distribution in cases with mutual prediction is an open technical problem (analogous to open problems in the theory of "program equilibrium").

### 5.3 Zero-probability actions and certainty

\(P(O_j \mid A)\) is undefined when \(P(A) = 0\). A deterministic agent who has settled on one action assigns the alternatives probability zero — yet it is precisely about the alternatives that she deliberates. The standard fix, which I adopt, is to model the agent as uncertain about her own action until she chooses: from a first-person standpoint, \(P(A_i) > 0\) for every act she is considering, because she does not yet know what she will do. This makes the deliberative perspective constitutive of EDT — a philosophical stance, not a theorem. Alternative formalizations (e.g., conditioning on infinitesimal probabilities, or on the *news report* "A" rather than the act) yield the same values \(V(A_i)\) in all the standard cases.

### 5.4 Sleeping Beauty

The source notes that EDT has been used to argue that Sleeping Beauty should adopt *thirder* credences (1/3 heads) to avoid Dutch books, and that Conitzer (2015) has constructed a Dutch book against halfers *even if* they use EDT. I will not settle the thirder/halfer dispute here; the relevant lesson for EDT is that its commitment to conditioning is rigid enough to interact nontrivially with anthropic reasoning, and that "EDT ⇒ thirding" arguments depend on precisely which proposition the beauty conditions on when awakened. Where conditioning events are ambiguous, EDT inherits the ambiguity.

## 6. Evaluation: managing the news or respecting the evidence?

The classical objections are Lewis's charge that EDT promotes "an irrational policy of managing the news," and Joyce's dictum that rational agents "act to bring about good results even when doing so might betoken bad news" (Joyce, 1999, p. 146). The smoking lesion makes the charge concrete: refusing to smoke does not remove the lesion; it merely ensures you never get the bad news.

Defenders of EDT have a two-pronged reply.

**First, on the two most famous cases, EDT's verdicts look right and CDT's look wrong.** One-boxing in Newcomb makes you rich with near-certainty in repeated play; cooperating with your twin gets you \$5 rather than \$1. If a theory of rationality systematically loses money on cleanly specified problems, the burden of proof shifts. CDT's standard response — dominance arguments ("the boxes are already sealed") — presupposes that only causal consequences matter, which is the point in dispute.

**Second, the disagreement is really about the object of evaluation.** EDT evaluates the *agent as an evidential system*: since your action is an output of your dispositions, choosing is the last chance to have evidence about what kind of agent you are, and what that kind of agent gets. CDT evaluates the *act in isolation*, with the agent's dispositions held fixed. In cases where the act and the disposition come apart (smoking lesion: you smoke because of the lesion, not because of a free choice), CDT's evaluation seems right. In cases where they coincide (Newcomb: the predictor predicts the act because the act expresses the disposition), the act is not easily severed from what produced it, and EDT's evaluation seems right. My own view, offered as a proposal: the correct theory evaluates the act *as the expression of a rationally chosen policy*, which coincides with EDT when correlations flow through the agent's own reasoning (Newcomb, twins) and with CDT when they flow through ares that the agent cannot influence by reasoning (lesions). EDT gets the important half of this right, and its errors occur precisely where the evidential correlation is known to bypass reasoning.

## 7. Conclusion

Evidential decision theory is the thesis that rational choice maximizes conditional expected utility,

\[
V(A) = \sum_j P(O_j \mid A) D(O_j),
\]

— that one should do what one would most be glad to learn one will do. It diverges from causal decision theory exactly when actions carry evidential import beyond their causal consequences, and it handles the classic correlation cases (Newcomb, the twin dilemma) in the way most people's intuitions favor, while mishandling the smoking lesion, where CDT shines. Applying EDT requires careful construction of the joint distribution over actions, outcomes, and their correlational channels — predictors, common causes, logical twins — and honest attention to correlation strengths and conditioning events. Whether EDT's "news value" is a rational guide or a seductive confusion remains contested; but the theory earns its place by showing that an agent is never merely a cause among causes — she is also the most informative thing in the world about what kind of agent she is.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9): 2887–2899.
- Eells, E. (1982). *Rational Decision and Causality*. Cambridge University Press.
- Gibbard, A., & Harper, W. L. (1976). "Counterfactuals and Two Kinds of Expected Utility." *Foundations and Applications of Decision Theory*, pp. 7–8.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1981). "Causal Decision Theory." *Australasian Journal of Philosophy* 59(1): 5–30.
- MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). "The Evidentialist's Wager." Global Priorities Institute.
- Pearl, J. (2009). *Causality* (2nd ed.). Cambridge University Press.
- Yudkowsky, E., & Soares, N. (2017). "Functional Decision Theory." arXiv:1710.05060.