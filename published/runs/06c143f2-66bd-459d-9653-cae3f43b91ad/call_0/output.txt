# Causal decision theory: choosing what to bring about

A decision can be good news without being a good cause. Taking an umbrella is evidence that rain is likely, but it does not ordinarily make rain more likely. Conversely, choosing an unpleasant medical treatment may be evidence of serious illness even when the treatment improves the patient’s prospects.

Causal decision theory (CDT) builds its account of rational choice around that distinction. Its central recommendation is to choose the available action with the best *expected causal consequences*. Evidential decision theory (EDT), by contrast, evaluates an action by asking how desirable the world would be, on average, conditional on the news that the action was taken.

In ordinary cases the two methods often agree. Their differences become striking when a choice is correlated with a desirable or undesirable state that the choice itself cannot affect: a predictor’s earlier forecast, a hidden personality trait, or another agent’s independent but similar decision.

The reference article presents CDT as a family of approaches rather than a complete algorithm. In particular, it does not settle how counterfactual probabilities are to be calculated. Below I first explain its core rule and then develop a structural causal model as one operational interpretation. That model is a useful implementation, not an additional claim that every causal decision theorist must accept it.

## 1. Actions, outcomes, and causal value

Suppose an agent has a set of feasible actions \(\mathcal A\). Let \(O_1,\ldots,O_n\) be mutually exclusive and exhaustive outcomes, and let \(u(O_j)\) represent the agent’s utility for outcome \(O_j\). For an action \(a\), write \(O_a\) for the outcome that would occur if the agent performed \(a\).

A natural formulation of causal expected utility is

\[
V_C(a)=\sum_{j=1}^n \Pr(O_a=O_j\mid E)\,u(O_j),
\]

where \(E\) is the evidence available at the decision point. CDT recommends an action in

\[
\operatorname*{arg\,max}_{a\in\mathcal A} V_C(a).
\]

This expression incorporates uncertainty about both the world and the consequences of acting. If an apple is good with probability \(0.8\), eating it gives utility \(5\) if good and \(-4\) if bad, then, assuming eating does not change its quality,

\[
V_C(\text{eat})=0.8(5)+0.2(-4)=3.2.
\]

If not eating has utility \(0\), eating is preferred. The numbers are utilities, not necessarily amounts of pleasure or money; they must represent the relevant preferences over complete outcomes. If an action has a cost, that cost belongs in the outcome’s utility.

The reference gives Gibbard and Harper’s counterfactual formulation,

\[
U(A)=\sum_j P(A\to O_j)\,D(O_j).
\]

Here \(A\to O_j\) is a counterfactual conditional: roughly, *were \(A\) performed, \(O_j\) would result*. It should not be read as saying that \(A\) logically necessitates \(O_j\). The probability represents uncertainty about whether the counterfactual is true.

For the formula to behave like an expected utility over outcomes, the counterfactual outcomes must form an appropriate partition: for each possible action, exactly one of the specified outcomes results in each relevant scenario. This can be arranged in deterministic causal models by including enough detail about background circumstances. Stochastic formulations require corresponding care about how chances and counterfactuals are represented.

## 2. Why conditional probability is different

EDT instead evaluates the action through

\[
V_E(a)=\sum_j \Pr(O=O_j\mid A=a,E)\,u(O_j),
\]

assuming the conditional probabilities are defined. The two expressions answer different questions:

- **Causal:** What would happen if the action were performed?
- **Evidential:** What should I believe about the outcome on learning that the action was performed?

For example, let \(H\) mean that a person has an illness, \(A\) that they take a treatment, and \(R\) that they recover. Ill people are more likely to seek treatment, so it is possible that

\[
\Pr(R\mid A)<\Pr(R\mid \neg A)
\]

even though treatment improves each patient’s prospects. The observed association reflects selection into treatment; it is not by itself the effect of treatment.

The reference notes that probabilities of counterfactual conditionals cannot generally be equated with ordinary conditional probabilities. Gibbard and Harper identify conditions under which they agree, including, with suitable additional axioms, independence between the action and the relevant counterfactual. Intuitively, if learning what action was taken tells us nothing about what would happen under that action, the evidential and causal calculations can coincide. But this independence is precisely what fails in many philosophically interesting examples.

This does not mean CDT ignores evidence. The agent should update on information already available: test results, observed behaviour, and even knowledge of their own dispositions. The disputed step is treating the action *under consideration* as fresh observational evidence about a cause of that action, rather than assessing what changing the action would cause.

## 3. An operational model: intervention

One practical way to calculate causal values is to use a **structural causal model**. This is an additional modelling proposal, not a unique procedure supplied by CDT.

Let a model \(M\) specify equations for variables and a probability distribution over background factors \(Z\). For example,

\[
A=f_A(Z_A),\qquad Y=f_Y(A,Z_Y),
\]

where \(A\) is the action and \(Y\) is an outcome. The background factors may be correlated: perhaps a common variable influences both the agent’s action and the outcome.

To evaluate \(a\), replace the ordinary equation for \(A\) with

\[
A:=a,
\]

while retaining the other structural equations. This operation is written \(\operatorname{do}(A=a)\). It severs the causal influences *into* the action variable, but preserves causal influences *out of* it. The proposed calculation is

\[
V_C(a)=\mathbb E\!\left[u(Y)\mid \operatorname{do}(A=a),E\right],
\]

under an interpretation in which \(E\) is evidence available before the intervention. More explicitly, one can update the distribution of background factors on \(E\), simulate the consequences of setting \(A=a\), and average utility across the resulting possibilities.

This procedure clarifies “holding fixed” background circumstances. It does **not** mean holding everything other than the action fixed. If pressing a switch causes a light to turn on, the light must change in the intervention. What is retained are the relevant background variables and causal laws; downstream effects are recomputed.

It also does not mean ignoring uncertainty about the causal structure. If the agent assigns probability \(q_m\) to model \(M_m\), an operational rule is

\[
V_C(a)=\sum_m q_m\,
\mathbb E_{M_m}\!\left[u(Y)\mid\operatorname{do}(A=a),E\right].
\]

A treatment might help under one biological mechanism and harm under another. CDT averages over these hypotheses using the agent’s current informed credences. The competing actions are evaluated against the same distribution over hypotheses, unless new evidence is obtained before the choice.

Several cautions matter in applying the model. An intervention must correspond to a genuine option: “be a different person since birth” may not be available at the present decision point. The time at which \(E\) is acquired also matters; evidence produced by an action cannot simply be treated as fixed prior evidence for every alternative. And observational data alone do not always identify an interventional distribution. A causal graph, experiment, or further substantive assumptions may be needed.

## 4. The hidden trait: David and Bathsheba

The reference’s example of King David illustrates a common-cause dependency. David wants to summon Bathsheba, but fears a successful revolt. Suppose his underlying charisma \(C\) influences both his inclination to act unjustly and the probability of revolt. By stipulation, summoning her does not itself cause revolt, and his adult choice does not change his charisma.

Schematically,

\[
C\longrightarrow A,\qquad C\longrightarrow R,
\]

where \(A\) is the choice and \(R\) is revolt. Observing that a king summons Bathsheba can be bad news: it may indicate that he is uncharismatic, hence at greater risk of revolt. But intervening to make David summon her leaves his charisma as it was. Thus, in the stipulated model,

\[
\Pr(R\mid A=\text{summon})\ne
\Pr(R\mid\operatorname{do}(A=\text{summon})),
\]

and the causal revolt probability is the same for summoning and abstaining.

If David values the encounter and assigns no sufficiently large independent disutility to its injustice, the causal calculation favors summoning. The reference reports this as CDT’s recommendation. It is not a general license to ignore moral costs: if David’s utility includes harm to Bathsheba or a moral objection to coercion, those consequences must be included and could reverse the result. Nor does the causal conclusion survive if unjust acts themselves increase the risk of revolt. The point depends on the stated causal model.

## 5. Newcomb’s problem and causal dominance

In Newcomb’s problem a predictor has already placed either \$1 million or nothing in an opaque box \(B\). A transparent box \(A\) contains \$1,000. The agent may take only \(B\), or take both. The predictor put the million in \(B\) if it predicted one-boxing, and nothing there if it predicted two-boxing.

Let \(F\) be the event that \(B\) is full and let \(p=\Pr(F\mid E)\) at the choice point. If the present act cannot causally change the already-filled box and utility is linear in money, then

\[
V_C(\text{one box})=1{,}000{,}000p
\]

and

\[
V_C(\text{two boxes})=1{,}000{,}000p+1{,}000.
\]

Two-boxing adds \$1,000 in either possible state of the opaque box. CDT therefore recommends it under these assumptions.

EDT can recommend the opposite. For illustration, suppose the agent’s choice is equally likely to be one-boxing or two-boxing and the predictor is correct with probability \(0.99\) conditional on each choice. Then

\[
V_E(\text{one box})=0.99(1{,}000{,}000)=990{,}000,
\]

whereas

\[
V_E(\text{two boxes})
=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\]

The extra symmetry assumption is important: an overall accuracy of 99% alone does not determine both conditional probabilities.

The disagreement is not about arithmetic. CDT says that taking both boxes cannot change the prediction already made. EDT says that one-boxing is powerful evidence that the prediction favored one-boxing. Critics regard the fact that successful predictors tend to leave two-boxers poor as a serious problem for CDT; defenders emphasize that, with the box’s contents fixed, refusing an extra \$1,000 changes nothing for the better. The reference reports both the recommendation and the continuing dispute.

## 6. Choosing policies rather than isolated acts

The action variable must match the actual decision. A policy can be an action too.

Suppose an agent can, *before* a predictor observes or forecasts them, install a binding mechanism that will later make them one-box. If installing the mechanism causally influences the prediction, then the relevant intervention is on the earlier commitment, not just on the later box choice. In such a model, CDT may favor commitment to one-boxing even though, at the later uncommitted choice point, it favors taking both boxes.

More generally, let a policy \(\pi\) map future observations \(h\) to actions. Its causal value can be written

\[
V_C(\pi)=\mathbb E\!\left[u(Y)\mid\operatorname{do}(\Pi=\pi),E\right].
\]

The model should include effects of adopting the policy: others may observe it, institutions may respond to it, and it may constrain later actions. One must not simply hold the predictor’s earlier output fixed when evaluating an intervention that occurs *before and causes* that output.

This produces a familiar tension between planning and later choice. An earlier agent may prefer a binding policy whose future act would not be optimal if reconsidered without the commitment. Whether a binding mechanism is available, effective, and worth its cost is an empirical part of the problem. Merely wishing now that one had committed earlier does not make the earlier commitment a current option.

The same distinction matters in games. Against a prisoner’s-dilemma opponent whose move is unaffected by yours, defection may causally dominate cooperation even if the opponent is your psychological twin and your moves are strongly correlated. But if you can communicate, commit in advance, or influence their decision process, those causal pathways belong in the model and may make cooperation advantageous.

## 7. Self-knowledge and unstable deliberation

The reference’s “Psychopath Button” challenges the idea that an agent should keep their initial beliefs fixed while evaluating actions. Paul can press a button that kills all psychopaths. He prefers a world without psychopaths but strongly prefers survival. He also believes that only a psychopath would press the button.

In a simple model, let \(q\) be Paul’s current probability of being a psychopath, \(g>0\) the benefit if he presses and survives, and \(L>0\) the loss if he presses and dies. Ignoring other consequences,

\[
V_C(\text{press})=(1-q)g-qL,\qquad
V_C(\text{abstain})=0.
\]

If \(q\) is sufficiently small, pressing has positive causal value. Yet the prospect of pressing seems itself to reveal that Paul is a psychopath. Egan uses such cases to argue that a rule fixing unconditional credences in causal dependency hypotheses can diverge from the intuitive instruction to bring about the best results.

The timing of evidence is crucial. If Paul already knows that he is inclined to press, he should condition on that self-knowledge when setting \(q\). The reference notes Joyce’s response that CDT can use information about what an agent is inclined or likely to do. But there remains a difficult question: can deliberation itself generate new evidence about Paul’s type, and if so when should it be incorporated? If each tentative conclusion changes his beliefs and therefore changes the recommended act, the choice process may be unstable.

A simple intervention calculation does not settle this issue. A more detailed model could represent deliberation, introspection, and any observations Paul receives before a final choice. That is a reasonable operational response, but it is an extension requiring assumptions about how self-evidence arises; it is not a proof that every version of CDT avoids the objection.

## 8. Adversarial predictions and the limits of a one-step calculation

The reference also describes an adversarial offer. A seller offers two boxes for \$1 each; the buyer may purchase at most one. Yesterday the seller placed \$3 in each box she predicted the buyer would **not** acquire. The seller predicts the buyer’s choice correctly with probability \(0.75\).

At the purchase point, the contents are already fixed. At least one box contains \$3: if the seller predicted purchase of one, the other was filled; if she predicted no purchase, both were filled. Consequently the sum of the two boxes’ causal expected contents is at least \$3. At least one box therefore has expected contents of at least \$1.50, exceeding its \$1 price. On the simple fixed-credence calculation, buying an appropriately chosen box is better than buying none.

But if the buyer buys a box and the seller’s prediction is correct with probability \(0.75\), the purchased box is empty on correct predictions. Even if it contains \$3 whenever the prediction is wrong, the buyer’s expected net payoff is at most

\[
0.25(3)-1=-0.25.
\]

The apparent conflict depends on how the choice rule, predictor, and probabilities fit together. In particular, if the rule would sometimes recommend buying none, one must specify prediction accuracy conditional on purchase before using the last calculation. Randomization, learning one’s own intended choice, and the predictor’s access to that randomization can also change the model. The example is nevertheless a sharp challenge: a locally attractive purchase can correlate with precisely the adverse earlier prediction that makes purchases lose money.

It also illustrates why guaranteed-payoff and diachronic objections need careful formulation. A critic may show that a sequence of decisions, each evaluated locally, yields a loss or forgoes a guarantee. A defender can ask whether an earlier commitment, a different information state, or a revised model was available. Neither side can resolve the dispute simply by labeling a correlation “noncausal”; the full decision sequence and its feasible interventions must be specified.

## 9. What CDT leaves open

The reference emphasizes that CDT itself does not supply a universal algorithm for counterfactual probabilities. Lewis’s **imaging** is one proposal: for each possible world, move its probability mass to a sufficiently close world where the contemplated action occurs, then calculate the outcome distribution there. But “closest” requires a substantive account of what remains similar when the action changes. Different similarity rules can produce different verdicts, and the reference notes worries about a regress in specifying the relevant conditional beliefs.

Structural intervention gives a more explicit operational alternative when an adequate causal model is available. It does not eliminate the philosophical work. The modeller must decide what intervention represents the agent’s option, which variables and mechanisms persist, how to represent uncertainty, and what evidence is available at each point. Different defensible answers can yield different causal recommendations.

A practical application should therefore proceed in stages: specify the decision time and feasible acts or policies; list the outcomes and utilities; draw the relevant causal dependencies, including common causes and downstream effects; update on available evidence; calculate the outcome distribution under each intervention; and test whether the conclusion changes under plausible alternative models. If a counterfactual cannot be identified, the honest result is a conditional recommendation—*choose \(a\) if these causal assumptions hold*—rather than a spurious exact answer.

## Conclusion

CDT evaluates alternatives by their expected effects, not merely by what choosing them would reveal. That principle explains its treatment of confounding, its two-boxing recommendation in standard Newcomb’s problem, and its willingness to value earlier commitments that causally affect later circumstances.

Its central difficulty is equally clear: the principle needs a defensible account of the relevant counterfactuals and of evidence gained during deliberation. A causal model can make those assumptions explicit and usable, but predictive and self-referential cases show why choosing the model is itself part of the theory’s challenge.

### References

- Gibbard, A. and Harper, W. L. (1981), “Counterfactuals and Two Kinds of Expected Utility.”
- Lewis, D. (1981), “Causal Decision Theory,” *Australasian Journal of Philosophy*.
- Egan, A. (2007), “Some Counterexamples to Causal Decision Theory,” *The Philosophical Review*.
- Wikipedia contributors, [“Causal decision theory,” revision 1381555528](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528), CC BY-SA 4.0.