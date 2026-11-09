# Causal decision theory: choosing what to bring about

A decision can be good news without being a good intervention. A patient’s recovery may be correlated with taking a medicine because healthier patients are more likely to receive it. A king’s unjust conduct may be evidence that he is unpopular, even if that particular act does not make him unpopular. And a choice may be evidence that a reliable predictor has already prepared a reward, even though the choice cannot change what the predictor did.

Causal decision theory, or **CDT**, draws its motivating distinction from cases like these. It recommends choosing the available action with the best *expected causal consequences*, not necessarily the action that would be the best news about the world. To apply it, one must ask what would happen under each alternative action, holding fixed the appropriate features of the situation and allowing the action’s effects to vary.

That formulation is attractive, but it leaves work to do. Which features should be held fixed? What probabilities should be assigned to counterfactual outcomes? Should an agent treat its own emerging inclination to act as evidence? The reference article presents CDT as a family of views and emphasizes both its intuitive motivation and its contested applications. The structural-model procedure below is one useful operational interpretation, not an algorithm uniquely prescribed by the article.

## 1. From consequences to expected utility

Suppose an agent can choose an action \(a\) from a set \(\mathcal A\). Let \(Y_a\) denote the outcome that would occur if the agent were to choose \(a\), and let \(u\) assign utilities to outcomes. A compact statement of CDT is

\[
a^*\in\operatorname*{arg\,max}_{a\in\mathcal A}
\mathbb E[u(Y_a)\mid I],
\]

where \(I\) is the information available at the decision point. If several actions maximize expected utility, this rule alone permits any of them.

For discrete, mutually exclusive and exhaustive outcomes \(o_1,\ldots,o_n\),

\[
\operatorname{CEU}(a\mid I)
=\sum_{j=1}^n P(Y_a=o_j\mid I)\,u(o_j).
\]

The expectation matters because the agent may not know which causal situation obtains. Suppose an apple is good with probability \(0.8\). Eating it gives utility \(10\) if good and \(-20\) if bad; declining gives utility \(0\). Then

\[
\operatorname{CEU}(\text{eat})=0.8(10)+0.2(-20)=4,
\]

so eating is preferred. If the apple is good with probability \(0.6\), its expected utility falls to \(-2\), and declining is preferred.

The utilities need not be amounts of money or pleasure. They should represent the preferences relevant to the decision, including, where appropriate, risk, moral costs, and consequences for other people. In money examples below, I assume for simplicity that utility is linear in dollars; that is an extra assumption, not a requirement of CDT.

The reference article gives Gibbard and Harper’s formulation in terms of probabilities of counterfactual conditionals:

\[
U(A)=\sum_j P(A\to O_j)D(O_j).
\]

Here \(A\to O_j\) is naturally read as “if \(A\) were done, \(O_j\) would result.” It should not be confused with material implication, nor does the expression require the agent to be certain that \(A\) produces \(O_j\). It is the probability assigned to the counterfactual outcome. The potential-outcome notation \(Y_a\) makes the same kind of calculation explicit, though particular accounts of counterfactuals can differ.

## 2. Causal expectation is not conditional expectation

Evidential decision theory, or **EDT**, instead evaluates an action by ordinary conditional probability:

\[
\operatorname{EEU}(a\mid I)
=\sum_j P(Y=o_j\mid A=a,I)\,u(o_j),
\]

assuming \(P(A=a\mid I)>0\). This asks what the action would tell the agent about the outcome. CDT asks what outcome the action would bring about.

These can agree. In a randomized experiment, for example, treatment assignment may be independent of the factors determining the potential outcomes. Under suitable assumptions,

\[
P(Y=o\mid A=a,I)=P(Y_a=o\mid I).
\]

Then treatment is both evidence of and a cause of the same outcome distribution. The equality is not automatic: randomization and a well-defined treatment are substantive causal assumptions.

The reference article notes that, under additional axioms about counterfactuals, independence between an action and the relevant action-counterfactual can suffice for equality with the corresponding conditional probability. It also cites Lewis’s result against identifying probabilities of conditionals with conditional probabilities in general. The practical lesson is that an observational association alone does not establish a causal effect.

A simple common-cause example makes the distinction concrete. Let \(T\) be a person’s health type, and suppose healthier people are more likely both to take a supplement and to recover. Observing that someone took the supplement can raise the probability that they recover. But if the supplement itself has no effect, then

\[
P(Y_{\text{take}}=\text{recover}\mid I)
=
P(Y_{\text{decline}}=\text{recover}\mid I),
\]

even while

\[
P(Y=\text{recover}\mid A=\text{take},I)
>
P(Y=\text{recover}\mid A=\text{decline},I).
\]

If the supplement has a cost, CDT recommends declining it. The action is a useful *diagnostic sign*, but not a useful *treatment*.

## 3. Building a causal calculation

One way to make CDT operational is to supply a structural causal model. This is an additional modeling proposal: the reference article says CDT itself does not specify a unique algorithm for counterfactual probabilities.

Let \(S\) summarize uncertain background conditions and causal mechanisms, let \(A\) be the action, and suppose the outcome is

\[
Y=f(A,S).
\]

For each alternative \(a\), define the potential outcome

\[
Y_a=f(a,S).
\]

Then

\[
\operatorname{CEU}(a\mid I)
=\sum_s P(S=s\mid I)\,u(f(a,s)).
\]

The crucial feature is that the **same distribution over background states** is used when comparing alternatives. The agent does not replace it with \(P(S=s\mid A=a,I)\) merely because the action might be correlated with those states. The model nevertheless allows any effect of the action represented in \(f\).

A more detailed model may have variables satisfying equations such as

\[
A=g(T,U_A),\qquad
M=h(A,T,U_M),\qquad
Y=k(A,M,T,U_Y).
\]

Here \(T\) may influence both the action and outcome, while \(M\) is an intermediate consequence of the action. To calculate the intervention \(\operatorname{do}(A=a)\), replace the equation for \(A\) with \(A=a\), retain the other equations, and propagate the consequences:

\[
P(Y_a=y\mid I)
=
P(Y=y\mid \operatorname{do}(A=a),I).
\]

This notation expresses an intervention, not ordinary conditioning. In particular, the intervention cuts the modeled causes of \(A\); it does not cut causal paths from \(A\) to its effects. If an action changes a person’s future health, other people’s responses, or the information later available, those changes belong in the calculation.

Some precautions are important:

* **Specify the action.** “Take medicine” may have different effects depending on dose and timing. Counterfactual outcomes require a sufficiently definite intervention.
* **Condition on actual information.** Known test results, observed behavior, and causal evidence update \(P(S\mid I)\). Holding background conditions fixed across alternatives does not mean ignoring evidence.
* **Keep causal uncertainty.** If the agent is unsure whether the medicine works, the state \(S\) can include the unknown causal mechanism. Average over the plausible mechanisms rather than pretending one is known.
* **Do not hold effects fixed.** If the choice changes a later variable, fixing that variable while varying the choice can erase a genuine benefit or harm.
* **Use a common outcome description.** Include costs of the action itself and all relevant downstream effects; otherwise the comparison may omit what matters.

The difficult step is choosing the causal model. Observational data may not identify the intervention distribution: distinct models can produce the same correlations but imply different effects. CDT tells the agent to prefer the better causal prospect; it does not, by itself, reveal which causal prospect is better.

## 4. David, Bathsheba, and a common cause

The reference article’s example of King David is designed to separate evidence from influence. David wants to summon Bathsheba but fears revolt. His fixed personality type, charismatic or uncharismatic, influences both his tendency to act unjustly and the likelihood of successful revolt. The stipulated causal facts say that this particular unjust act does **not** itself cause revolt.

For illustration, suppose David currently assigns probability \(0.5\) to each type. A charismatic king has a \(0.1\) chance of successful revolt, and an uncharismatic king a \(0.9\) chance. Suppose further that summoning is much more likely for the uncharismatic type. Observing a king summon someone would then be bad news about his type and hence about revolt.

But if summoning does not change type or revolt, the intervention probabilities are

\[
P(\text{revolt}\mid\operatorname{do}(\text{summon}))
=
P(\text{revolt}\mid\operatorname{do}(\text{abstain}))
=0.5.
\]

On those assumptions, the feared revolt is not a causal reason to abstain. If David values the encounter and no other relevant cost is included, CDT favors summoning.

That last qualification matters. The example stipulates a specific relationship between injustice and revolt; it does not establish that the act is morally costless. If David assigns disutility to harming Bathsheba or acting unjustly, that belongs in \(u\), and the recommendation may reverse. CDT separates the causal question from the question of what outcomes are valued.

## 5. Newcomb’s problem and fixed past events

Newcomb’s problem makes the disagreement sharper. A transparent box contains \$1,000. An opaque box contains either \$1,000,000 or nothing, according to a prediction made before the choice. A highly reliable predictor filled it if it predicted that the player would take only the opaque box; otherwise it left the box empty.

Let \(F\) mean that the opaque box is full, and write \(p=P(F\mid I)\). On the standard causal assumptions, the predictor’s past act and the box’s present contents are not affected by the player’s current choice. Thus

\[
\begin{aligned}
\operatorname{CEU}(\text{one box})&=1{,}000{,}000p,\\
\operatorname{CEU}(\text{two boxes})&=1{,}000{,}000p+1{,}000.
\end{aligned}
\]

Two-boxing is better by \$1,000 for every \(p\). This is a dominance argument: whatever is already in the opaque box, taking both adds the transparent box’s contents.

An evidential calculation can point the other way. Suppose, additionally, that

\[
P(F\mid\text{one box},I)=0.99,\qquad
P(F\mid\text{two boxes},I)=0.01.
\]

Then the evidential expected monetary values are \$990,000 for one-boxing and \$11,000 for two-boxing. These conditional probabilities are stronger assumptions than the bare claim of 99% overall predictive accuracy; the latter alone does not fix both conditional probabilities without information about how often each choice occurs.

The contrast captures the philosophical dispute. CDT says a present choice cannot change the already-set contents; EDT says the choice is powerful evidence of those contents. The article reports the standard CDT recommendation of two-boxing but also treats Newcomb’s problem as a major alleged counterexample. It would be too strong to say that every two-boxer receives only \$1,000: a mistaken predictor could leave a two-boxer with \$1,001,000. The criticism is about the overall association between the decision procedure and the predictor’s preparation.

The timing and causal structure are essential. If the predictor is still watching and will fill the box *after* the choice, or if a genuine causal channel runs from the choice to the filling, CDT must include that effect. It is not a universal rule to ignore predictions.

## 6. Policies, commitment, and other agents

Actions can be policies rather than single movements. A policy \(\pi\) maps future observations \(H\) to actions, \(A=\pi(H)\). If the present choice installs a policy, its causal value is

\[
\operatorname{CEU}(\pi\mid I)
=\mathbb E[u(Y_\pi)\mid I].
\]

Here \(Y_\pi\) must be calculated from a model of what installing that policy changes. A policy may influence others who can observe it, a predictor who examines it, or the agent’s own future options. A physically effective commitment to one-box, made before a predictor inspects it, could therefore be causally valuable. That is a different decision from choosing at the boxes after the contents have been fixed.

The distinction also matters in games. In a standard one-shot prisoner’s dilemma, defecting gives a higher payoff than cooperating for either fixed choice of the other player. If the other player’s simultaneous choice is causally unaffected by yours, CDT recommends defecting. But suppose an earlier commitment to cooperate is observable and induces the other player to cooperate; that is a causal pathway and may make the commitment worthwhile.

A “twin” version is more troubling. If another player reasons almost exactly as you do, their choice may be highly correlated with yours even without a causal arrow from your present choice to theirs. CDT’s standard local calculation holds their choice fixed under your intervention and can recommend mutual defection, whereas a theory that exploits the correlation might favor cooperation. Whether that alternative captures a rational opportunity or improperly treats correlation as causal leverage is contested.

Policy evaluation also requires attention to time consistency. An agent might value a binding commitment now but, if the commitment fails and the later decision is reached, prefer a different act then. CDT can represent both decisions; it does not automatically guarantee that the earlier preferred plan will remain optimal at every later information state.

## 7. Imaging and the problem of counterfactuals

The structural-model calculation is not the only way to understand \(P(Y_a=o)\). The article describes Lewis’s **imaging** proposal: for each possible world, move its probability mass to a closest world where the action occurs. The probability of an outcome after imaging is the total mass moved to worlds with that outcome.

This illustrates both the promise and difficulty of counterfactuals. “Closest” cannot merely mean most similar in every respect. If an agent’s action is correlated with a past prediction, the closest action-world might also have a different prediction. A causal account must explain why the appropriate comparison preserves some features—such as an already-filled box—while allowing downstream consequences to change.

The article also reports a concern that imaging can require further conditional judgments about what the agent would believe if certain of the action, potentially leading to regress. Structural equations make some such choices explicit, but they do not eliminate the philosophical issue: which equations and interventions correctly represent the available act remains a modeling judgment. In unusual cases, counterfactual semantics, causal direction, and even the set of genuinely available actions may be disputed.

## 8. Self-knowledge and alleged counterexamples

The Psychopath Button, discussed in the reference article, exposes a tension within CDT. Paul would prefer a world without psychopaths, but the button kills all psychopaths, and he strongly prefers not to die. He also believes that only a psychopath would press it.

A simplified numerical model shows the issue. Let \(T\) indicate whether Paul is a psychopath. If he is not, pressing gives utility \(+10\); if he is, pressing kills him and gives utility \(-100\). Not pressing gives utility \(0\). If his current credence is \(P(T\mid I)=0.05\), then

\[
\operatorname{CEU}(\text{press})
=0.95(10)+0.05(-100)=4.5.
\]

A simple CDT calculation recommends pressing. Yet if the contemplated act is compelling evidence that Paul is a psychopath, pressing seems reckless.

The precise informational setup matters. If Paul observes an independent psychological test or a strong urge to press, he should update on that evidence before calculating: for instance, if his credence rises to \(0.5\), pressing has expected utility \(-45\). The article notes Joyce’s view that CDT can take information about one’s inclinations into account. The unresolved issue is what happens when the inclination or decision itself is the evidence, and how an agent should reason while that evidence is emerging. Different CDT proposals about deliberation, stability, and self-knowledge can give different answers.

A related challenge is the **adversarial offer**. A seller predicts which of two boxes a buyer will acquire and puts \$3 in each box predicted not to be acquired. A box costs \$1; the buyer may buy one or none. Since at least one box contains \$3, the average box has causal expected gross value at least \$1.50. If the seller’s placement is already fixed, a straightforward CDT calculation therefore finds some box worth buying.

Yet if the seller correctly predicts the acquired box with probability \(0.75\), the buyer’s expected net return from buying is

\[
0.75(-1)+0.25(2)=-0.25,
\]

assuming exactly one box is predicted for acquisition and the other is filled. The seller profits on average. This is not a contradiction in arithmetic: the causal comparison treats the past placement as fixed, whereas the actual purchase is correlated with that placement. The challenge is whether a rule that can predictably produce such losses has correctly captured practical rationality. As with the button, the exact information available to the buyer and any randomization procedure matter.

## Conclusion

CDT evaluates alternatives by their expected outcomes under causal counterfactuals. Its central discipline is to distinguish what an act **changes** from what it merely **indicates**. Structural models, intervention probabilities, and policy-level analysis make that discipline usable, provided their causal assumptions are stated and tested.

The hardest cases are not failures to compute an expectation; they concern which counterfactuals and information states the expectation should use. Newcomb-style predictors, correlated agents, and self-knowledge make those choices philosophically consequential. CDT offers a powerful framework for causal control, but its application depends on a defensible account of the causal structure and of what the deliberating agent knows.

## References

- Wikipedia contributors, [“Causal decision theory,” revision 1381555528](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528), licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- Gibbard, A. and Harper, W. L. (1981), “Counterfactuals and Two Kinds of Expected Utility,” in *Ifs*.
- Lewis, D. (1981), “Causal Decision Theory,” *Australasian Journal of Philosophy* 59: 5–30.
- Egan, A. (2007), “Some Counterexamples to Causal Decision Theory,” *The Philosophical Review* 116: 93–114.
- Oesterheld, C. and Conitzer, V. (2021), “Extracting Money from Causal Decision Theorists,” *The Philosophical Quarterly* 71.