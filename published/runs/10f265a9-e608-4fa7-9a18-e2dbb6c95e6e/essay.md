# Causal decision theory: choosing by consequences, not by news

Suppose that a medical test result is associated with recovery. Does producing that result help a patient recover, or does it merely indicate that the patient was likely to recover anyway? The difference between *bringing about* an outcome and *learning* that it is likely is central to causal decision theory.

Causal decision theory, or **CDT**, recommends choosing an available action according to its expected causal consequences. An action can be good news without being a good intervention: it might indicate that favorable conditions already obtain while doing nothing to produce them. Conversely, an action may be bad news about the agent while still improving the world relative to the alternative.

That distinction becomes contentious when an agent’s choice is correlated with hidden facts about the world: its own character, another person’s decision, or a prediction made before the choice. CDT’s appeal is that it asks what the agent can actually change. Its difficulty is that “what would happen if I acted differently?” is not determined by ordinary correlations alone.

## 1. The decision rule

Let \(\mathcal A\) be the set of actions available at a decision point, let \(O_1,\ldots,O_n\) be mutually exclusive and exhaustive outcomes, and let \(u(O_j)\) be the utility of outcome \(O_j\). Following the counterfactual formulation discussed by Gibbard and Harper, assign a probability to the proposition

\[
A \mathbin{\Box\!\!\to} O_j,
\]

read as “if action \(A\) were taken, outcome \(O_j\) would occur.” The causal value of \(A\) is

\[
V_{\mathrm C}(A)
 = \sum_{j=1}^n
 P(A\mathbin{\Box\!\!\to}O_j)\,u(O_j).
\]

CDT selects an action in

\[
\operatorname*{arg\,max}_{A\in\mathcal A}V_{\mathrm C}(A).
\]

The probabilities and utilities should reflect the information and preferences relevant at the decision point. If actions have costs, moral significance, or effects on people other than the chooser, those features must be represented in the outcomes or utility function. The theory does not say that money, survival, or happiness alone is always the objective.

The arrow denotes a **counterfactual**, not a strict logical implication. “If I ate this apple, I would be happy” is not the claim that eating it logically necessitates happiness in every possible circumstance. It is a claim about what would happen under the relevant alternative in the world as it might be.

For a simple illustration, suppose eating an apple yields utility \(10\) if it is good and \(-20\) if it is bad. The agent assigns probability \(0.8\) to its being good, and declining it has utility \(0\). If eating does not change whether the apple is good, then

\[
V_{\mathrm C}(\text{eat})
 =0.8(10)+0.2(-20)=4,
\qquad
V_{\mathrm C}(\text{decline})=0.
\]

Eating is preferred. Uncertainty is over the apple’s quality and thus over the action’s effect; CDT does not require the agent to know the outcome in advance.

An equivalent and often convenient notation uses **potential outcomes**. Let \(O(a)\) denote the outcome that would result were action \(a\) taken. Then

\[
V_{\mathrm C}(a)=\mathbb E[u(O(a))].
\]

This notation is an operational way of expressing the counterfactual rule, not a complete theory of how counterfactuals are determined.

## 2. Why causal value differs from evidential value

Evidential decision theory, or **EDT**, evaluates an action by the conditional expectation

\[
V_{\mathrm E}(a)=\mathbb E[u(O)\mid A=a].
\]

This asks what outcome the action would be *evidence for*, if the agent learned that it had been taken. CDT instead asks for the outcome under an intervention that makes the action \(a\). In causal-model notation, one often writes this as

\[
V_{\mathrm C}(a)
 =\mathbb E[u(O)\mid \operatorname{do}(A=a)].
\]

The two expressions agree in many familiar cases, but not in general. In particular, an observed action may reveal something about a common cause of the action and the outcome. Intervening on the action need not alter that common cause.

Consider a stylized version of the King David example in the reference article. A king is either charismatic, \(C\), or uncharismatic, \(N\), with prior probabilities \(1/2\) each. Suppose:

\[
\begin{array}{c|cc}
 & P(\text{unjust act}\mid\text{type})
 & P(\text{successful revolt}\mid\text{type})\\ \hline
 C & 0.1 & 0.1\\
 N & 0.9 & 0.9
\end{array}
\]

Assume that, given type, the unjust act does not itself affect revolt. Seeing that the king acts unjustly is nevertheless bad news:

\[
P(N\mid\text{unjust})=0.9,
\]

and hence

\[
P(\text{revolt}\mid\text{unjust})
 =0.9(0.9)+0.1(0.1)=0.82.
\]

By contrast, the corresponding probability conditional on a just act is \(0.18\). These are striking evidential differences. But under the stated causal assumptions, making the king act unjustly does not change his type. The probability of revolt under either intervention is

\[
P(\text{revolt}\mid\operatorname{do}(\text{unjust}))
 =\tfrac12(0.1)+\tfrac12(0.9)=0.5.
\]

Thus the revolt risk alone gives the king no causal reason to abstain. If the unjust act gives him some benefit and no other cost is counted, CDT favors it; EDT may abstain if the adverse evidence about revolt is sufficiently important. This is an example of the theory’s logic, not an endorsement of treating injustice as costless.

The reference article notes that causal and evidential values coincide under suitable independence assumptions. For instance, if the actual action \(A\) is independent of each relevant potential outcome \(O(a)\), and the observed outcome equals \(O(a)\) when \(A=a\), then

\[
P(O(a)=o)=P(O=o\mid A=a).
\]

Random assignment can produce such independence under appropriate conditions. Without it, the observational conditional generally cannot simply be substituted for the counterfactual probability. Lewis’s work on probabilities of conditionals reinforces the broader point: the probability of a conditional is not, in general, just an ordinary conditional probability.

## 3. A practical causal model

CDT itself does not provide a unique algorithm for calculating counterfactuals. One useful operational interpretation is to supply a **structural causal model**.

Suppose \(X_1,\ldots,X_m\) are variables in a model, with equations

\[
X_i=f_i(\operatorname{Pa}_i,U_i),
\]

where \(\operatorname{Pa}_i\) are the modeled direct causes of \(X_i\), and the \(U_i\) represent background factors. The agent has a probability distribution over the background factors, and possibly over rival models as well.

To evaluate \(\operatorname{do}(A=a)\):

1. Replace the equation normally determining \(A\) with \(A=a\).
2. Leave the other structural equations and the background factors unchanged.
3. Recompute downstream variables.
4. Average the resulting utilities using the agent’s current probabilities.

If \(M\) is uncertain, this takes the form

\[
V_{\mathrm C}(a)
 =\sum_m P(M=m\mid I)\,
   \mathbb E_m[u(O(a))\mid I],
\]

where \(I\) is the agent’s information. “Holding fixed” background factors does **not** mean assuming that their values are known; their uncertainty is averaged over. Nor does it mean holding every variable fixed: consequences caused by the action must be allowed to change.

For example, if taking medicine changes symptoms, and symptoms affect a later decision to visit a doctor, both symptoms and the later decision may change in the intervention. If a genetic condition affects both the initial inclination to take medicine and the chance of recovery, intervening on medicine does not by itself change that condition.

This framework makes several assumptions that the general slogan of CDT does not settle:

- **The intervention must be specified.** “Take medicine” may refer to different doses or methods with different effects.
- **The causal model must be justified.** Observational associations alone may not identify its arrows or counterfactual distributions.
- **The decision point matters.** A variable already set at one decision point may still be influenced by an earlier choice.
- **Information must be handled carefully.** Genuine observations should update beliefs before evaluating alternatives. But treating the hypothetical intervention itself as news about the agent’s hidden type would reintroduce the evidential reasoning CDT is meant to distinguish.

The reference article also mentions Lewis’s *imaging*: roughly, move probability mass from each possible world to a sufficiently close world in which the action occurs. That too requires an account of which worlds count as relevantly close. As the article observes, the counterfactual machinery is a source of vagueness and can raise questions about how the agent’s beliefs would change under a hypothetical action. Structural models make some of these choices explicit; they do not eliminate the philosophical dispute.

## 4. Newcomb’s problem

Newcomb’s problem isolates the difference between changing an outcome and being evidence about it. A predictor has already placed either \(\$1{,}000{,}000\) or nothing in an opaque box \(B\). A transparent box \(A\) contains \(\$1{,}000\). The agent may take \(B\) alone or both boxes. The predictor filled \(B\) if it predicted the agent would take \(B\) alone.

At the moment of choice, let \(p\) be the agent’s current probability that \(B\) is full. Assuming the present choice cannot alter the already-set contents,

\[
\begin{aligned}
V_{\mathrm C}(\text{one box})&=1{,}000{,}000p,\\
V_{\mathrm C}(\text{two boxes})&=1{,}000{,}000p+1{,}000.
\end{aligned}
\]

On linear monetary utility, two boxes are better by \(\$1{,}000\), whatever \(p\). More generally, two-boxing causally dominates if the extra money has positive utility and no relevant side effects.

EDT sees a different comparison. If, for illustration, a predictor is correct with probability \(0.99\) conditional on either action, then

\[
\begin{aligned}
V_{\mathrm E}(\text{one box})&=0.99(1{,}000{,}000)=990{,}000,\\
V_{\mathrm E}(\text{two boxes})&=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\end{aligned}
\]

EDT one-boxes. The conditional accuracies are an additional simplifying assumption: overall predictive accuracy alone does not necessarily determine each conditional probability.

The causal theorist’s answer is that the extra thousand is available in either state of the opaque box. The critic’s answer is that agents using the two-boxing rule predictably tend to receive much less. Neither observation by itself settles the dispute; each expresses a different view of how a choice should exploit its correlation with a prior prediction.

It would also be wrong to say that two-boxing **always** produces only \(\$1{,}000\). An inaccurate predictor can fill the opaque box even when the agent takes both.

## 5. Actions, policies, and timing

Many decisions are not single button presses but choices of **policies**: rules mapping future observations to actions. If \(H\) is information the agent may later receive, a policy is a function \(\pi\) with action \(\pi(H)\). A causal evaluation can be written

\[
V_{\mathrm C}(\pi)=\mathbb E[u(O(\pi))].
\]

The model must specify what implementing the policy causes—including which future observations occur and how later actions respond to them.

This is especially important in prediction problems. Suppose an agent can make an effective, observable commitment *before* a predictor fills the box. If that commitment causes the predictor to forecast one-boxing and fill \(B\), choosing the commitment may have high causal value. Once the box has been filled, however, an agent free to reconsider may still prefer two boxes at the later decision point. There is no contradiction: the available actions and causal consequences differ at the two times.

A policy’s existence must not simply be assumed to change a prediction made earlier. It may do so if the policy is chosen early enough, or if an actual causal mechanism connects the policy or commitment to the predictor’s information. At the later moment, merely contemplating a different policy is not automatically a causal intervention on the past. This distinction is useful in everyday settings too: an enforceable promise can change another person’s expectations and actions, while a private intention adopted after their action cannot undo it.

Randomized policies require similar care. In an ordinary model where an independent coin selects action \(a\) with probability \(q(a)\), the value is

\[
V_{\mathrm C}(q)=\sum_a q(a)V_{\mathrm C}(a).
\]

But if the predictor can observe the coin, or if randomization changes other participants’ behavior, those effects belong in the model. One cannot assume both that the lottery is independent of the predictor and that the predictor knows its result.

## 6. Difficult cases: self-knowledge and correlated agents

The reference article presents Egan’s “Psychopath Button.” Paul prefers a world without psychopaths but strongly prefers remaining alive to dying. Pressing the button kills all psychopaths; Paul believes that only a psychopath would press it.

A simple numerical model exposes the pressure on CDT. Suppose Paul’s current probability of being a psychopath is \(p\). Pressing gives utility \(+1\) if he is not one and \(-100\) if he is; not pressing has utility \(0\). If the button press cannot change his pre-existing type, then

\[
V_{\mathrm C}(\text{press})=(1-p)-100p=1-101p.
\]

At \(p=0.001\), this is positive, so the simple causal rule recommends pressing. Yet if pressing is compelling evidence that he is a psychopath, the recommendation looks dangerous: conditional on actually pressing, his chance of death may be very high.

The example does not show that CDT must ignore self-knowledge. Paul may learn from his deliberation: noticing a strong inclination to press could increase his probability \(p\), changing the calculation. The reference notes Joyce’s view that CDT can use information about what one is inclined or likely to do. The unresolved issue is how to represent such information without simply conditioning on each action being hypothetically selected. Different causal models and proposals for updating during deliberation can produce different recommendations.

A related issue arises when playing a prisoner’s dilemma against a highly similar agent. If the other player’s action is not caused by yours, defection may causally improve your payoff for either fixed action of theirs. Yet if the two decisions are strongly correlated, cooperators may generally meet cooperators while defectors meet defectors. CDT can take account of any causal influence on the other player—communication, threats, or a commitment they observe—but a bare correlation between simultaneous choices is not itself such an influence. Whether that restriction is rationally compelling is part of the disagreement.

## 7. The adversarial offer

The *Adversarial Offer* makes the concern particularly vivid. A seller offers two boxes at \(\$1\) each; the buyer may buy one or neither. Yesterday, the seller put \(\$3\) in each box she predicted the buyer would not acquire. Suppose both parties assign probability \(0.75\) to an accurate prediction.

At least one box contains \(\$3\): if the seller predicted one purchase, the other box was filled; if she predicted no purchase, both were filled. Let \(p_1,p_2\) be the buyer’s current probabilities that boxes 1 and 2 contain \(\$3\). Then

\[
p_1+p_2\geq 1.
\]

If the buyer’s present choice cannot change yesterday’s placement, the causal net values of buying the boxes are \(3p_1-1\) and \(3p_2-1\). Since at least one \(p_i\geq 1/2\), at least one purchase has value at least \(\$0.50\), exceeding the value of buying neither.

Nevertheless, if the buyer does purchase a box, an accurate prediction leaves that purchased box empty. Under the illustrative assumption that prediction is correct with probability \(0.75\) conditional on purchase, the buyer’s actual expected net payoff is

\[
0.75(-1)+0.25(2)=-0.25.
\]

The seller correspondingly expects to profit. The source uses this kind of example to challenge CDT, and discusses related money-extraction and diachronic Dutch-book arguments. The discrepancy between the causal calculation and the conditional payoff is precisely the issue: buying a particular box is evidence that it was the one predicted, even though the purchase does not causally empty it.

The assumptions matter. Overall \(75\%\) accuracy does not alone establish the displayed conditional payoff if some outcomes involve no purchase. Nor does every proposed money pump apply independently of the agent’s information, available commitments, or opportunities to refuse a sequence of trades. These cases challenge a decision rule only when those details are specified.

## 8. Using CDT on an unfamiliar problem

A disciplined application begins by separating the decision rule from the model supplied to it:

1. **Locate the decision point and feasible alternatives.** Is the agent choosing an immediate act, an enforceable commitment, or a contingent policy?
2. **Specify outcomes and utilities.** Include costs, risks, side effects, and morally relevant consequences rather than silently equating utility with cash.
3. **Record current information.** Update on observations already available, including reliable information about the agent’s dispositions.
4. **Draw the causal dependencies.** Identify common causes, descendants of the choice, predictions, and mechanisms by which other agents respond.
5. **Evaluate each intervention.** Change the action or policy, propagate its effects through the model, and average over uncertainty.
6. **Compare with evidential conditionals as a diagnostic.** A large difference between \(P(O\mid A=a)\) and \(P(O\mid\operatorname{do}(A=a))\) often reveals a prediction, selection effect, or common cause worth examining.
7. **Test the assumptions.** Ask whether the action can affect an apparently fixed variable, whether current self-knowledge changes the probabilities, and whether a different intervention or causal model changes the answer.

The result is conditional on the causal and utility assumptions. Where plausible models disagree, reporting that sensitivity is more informative than presenting a single recommendation as a theorem of CDT.

## Conclusion

CDT’s central principle is to choose by expected consequences of intervention, not merely by the news an action would convey. Structural models and potential outcomes make that principle usable, but they also expose its dependencies on causal assumptions, timing, information, and the definition of the available choice. Prediction and self-knowledge cases remain philosophically contested: they test whether holding fixed what an action cannot cause is a strength of rational choice or a limitation of it.

### References

- Gibbard, A. and Harper, W. L. (1981), “Counterfactuals and Two Kinds of Expected Utility,” in *Ifs: Conditionals, Beliefs, Decision, Chance, and Time*.
- Lewis, D. (1981), “Causal Decision Theory,” *Australasian Journal of Philosophy* 59, 5–30.
- Egan, A. (2007), “Some Counterexamples to Causal Decision Theory,” *The Philosophical Review* 116, 93–114.
- Oesterheld, C. and Conitzer, V. (2021), “Extracting Money from Causal Decision Theorists,” *The Philosophical Quarterly* 71.
- Wikipedia contributors, [“Causal decision theory,” revision 1381555528](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528).