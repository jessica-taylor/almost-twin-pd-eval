# 002_cdt_wikipedia_openai_gpt-6.1-terra_rlow_plow / 00017

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/578ea0d8-2027-4962-82ba-b515dea194cc/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/578ea0d8-2027-4962-82ba-b515dea194cc/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Choosing What Makes a Difference

A decision can be good news without being a good intervention. Carrying an umbrella is evidence that rain is likely, but carrying one does not ordinarily make it rain. A medical treatment might be associated with recovery because healthier patients tend to receive it, even if the treatment itself does little. Conversely, a painful procedure may be evidence of serious illness while still improving a patient’s prospects.

**Causal decision theory** (CDT) takes this distinction as fundamental. It recommends an action according to its expected *causal consequences*, not according to how favorable the world would appear if the agent learned that the action had been taken. The distinction becomes especially contentious when an action is correlated with features of the world that it cannot change: a person’s character, another agent’s prediction, or a previously filled box.

The reference article presents CDT as a family of approaches rather than a single complete algorithm. Its central idea is straightforward; applying it requires a probability model, a utility function, and an account of the relevant counterfactuals. This essay develops one operational interpretation using structural causal models, while distinguishing that interpretation from claims made by the source.

## 1. From causal consequences to expected utility

Suppose an agent can choose an action \(a\) from a set \(\mathcal A\). Let \(O\) denote an outcome and \(u(O)\) its utility. Under uncertainty, the causal value of \(a\) is the expected utility of the outcome that would occur *if \(a\) were performed*:

\[
V_C(a)=\mathbb E[u(O_a)\mid I],
\qquad
a^*\in\operatorname*{arg\,max}_{a\in\mathcal A}V_C(a).
\]

Here \(I\) is the information available at the decision point, and \(O_a\) is a counterfactual outcome: the outcome under action \(a\). The expectation averages over the agent’s uncertainty about the world and about how it would respond to the action.

For example, suppose an apple is good with probability \(0.8\). Eating it yields utility \(10\) if it is good and \(-6\) if it is bad. Its causal expected utility is

\[
0.8(10)+0.2(-6)=6.8.
\]

If eating an orange yields utility \(5\) for certain, CDT recommends the apple, assuming the two utilities include all relevant effects and eating the apple does not itself change its prior quality.

The word *utility* is doing important work. Monetary payoffs can serve as utilities in simple illustrations, but real decisions may involve risk aversion, moral costs, health, or consequences for others. CDT does not itself tell an agent how to value those things. It tells the agent how to compare actions once relevant outcomes, utilities, probabilities, and causal relationships have been specified.

The reference article gives a formulation associated with Gibbard and Harper:

\[
V_C(a)=\sum_j P(a\mathbin{\Box\!\!\to}O_j)\,u(O_j).
\]

The expression \(a\mathbin{\Box\!\!\to}O_j\) means that, *were \(a\) performed, \(O_j\) would occur*. This is a counterfactual conditional, not the claim that \(a\) logically or necessarily implies \(O_j\). In the potential-outcome notation above, the probability can be read as \(P(O_a=O_j\mid I)\). For the sum to be an ordinary expected utility, the \(O_j\) should form an exhaustive, mutually exclusive set of relevant outcomes.

## 2. Causal versus evidential evaluation

Evidential decision theory (EDT) evaluates an action by conditioning on it:

\[
V_E(a)=\mathbb E[u(O)\mid A=a,I],
\]

where \(A\) is the action actually taken. EDT asks, in effect: *How desirable would the world be, on average, conditional on my taking \(a\)?* CDT asks: *How desirable would the world be if I made \(a\) happen?*

These agree when conditioning on the action happens to produce the same outcome distribution as intervening on it. In the potential-outcome formulation, a sufficient condition is

\[
O_a\perp\!\!\!\perp A\mid I,
\]

together with **consistency**: when \(A=a\), the actual outcome equals \(O_a\). Then

\[
P(O_a=o\mid I)=P(O=o\mid A=a,I).
\]

Random assignment can create this sort of independence, provided that the assignment does not affect the outcome through some route other than the action being studied. But independence is a substantive assumption, not a general law of decision making.

The reference article notes Lewis’s result that probabilities of conditionals cannot generally be identified with ordinary conditional probabilities. The practical point is narrower but essential: \(P(O_a=o)\) and \(P(O=o\mid A=a)\) can differ because the actual choice \(A\) carries information about the circumstances in which it is made.

### Character and revolt

The article illustrates the difference with a story about King David. Imagine, for simplicity, that he may summon a woman or abstain. He prefers summoning her, all else equal, but also cares about avoiding a successful revolt. His unknown charisma affects both his tendency to act justly and his vulnerability to revolt. By stipulation, summoning her does not itself cause a revolt.

For a numerical version, suppose:

- David is charismatic with probability \(1/2\).
- A charismatic king summons with probability \(0.1\); an uncharismatic king does so with probability \(0.9\).
- Revolt succeeds with probability \(0.1\) if the king is charismatic and \(0.8\) if he is uncharismatic.
- Summoning provides utility \(5\); a successful revolt costs \(20\).

Conditioning on summoning makes uncharisma likely:

\[
P(\text{uncharismatic}\mid \text{summon})=0.9.
\]

Thus the evidential probability of revolt given summoning is

\[
0.1(0.1)+0.9(0.8)=0.73.
\]

Given abstention it is \(0.17\). EDT therefore assigns values \(5-20(0.73)=-9.6\) to summoning and \(-20(0.17)=-3.4\) to abstaining.

CDT instead holds fixed the probability of charisma under either intervention. The causal probability of revolt is \(0.45\) for both actions, so their values are \(-4\) and \(-9\), respectively. On these stipulated utilities CDT recommends summoning.

This is not a general endorsement of the conduct in the story. If the woman’s welfare, injustice, reputational effects, or other causal consequences matter, they belong in the outcome and utility model. The example isolates one point: an action can reveal an unfavorable trait without causing that trait or its independent effects.

## 3. An operational model of intervention

The reference article says that CDT does not itself specify an algorithm for counterfactual probabilities. A useful operational proposal is to supply a **structural causal model**.

Let \(X_1,\ldots,X_n\) be variables governed by equations

\[
X_i=f_i(\operatorname{Pa}_i,U_i),
\]

where \(\operatorname{Pa}_i\) are direct causal inputs and \(U_i\) represent background factors. Suppose one variable is the agent’s action \(A\). To evaluate \(a\), replace its ordinary generating equation with

\[
A:=a,
\]

and retain the other equations. This is written \(\operatorname{do}(A=a)\). Solving the modified model gives a counterfactual outcome \(O_a\), and the decision rule becomes

\[
V_C(a)=\mathbb E[u(O)\mid \operatorname{do}(A=a),I].
\]

The notation needs care: \(I\) represents information actually possessed before choosing, used to form beliefs about background variables and causal mechanisms. It is not the hypothetical news that the action has been taken. A prior observation can legitimately change beliefs about a hidden state even when the candidate action cannot change it.

As a small example, let

\[
A=U,\qquad O=U+A,
\]

where \(U\) is equally likely to be \(0\) or \(1\). Observationally, \(A=1\) reveals \(U=1\), so \(\mathbb E[O\mid A=1]=2\). Under \(\operatorname{do}(A=1)\), however, \(U\) remains equally likely to be either value, giving

\[
\mathbb E[O\mid\operatorname{do}(A=1)]=1.5.
\]

The intervention changes the action but not its common cause.

This procedure is a proposal for making CDT precise, not something uniquely mandated by its informal slogan. In particular, a modeler must decide which variable represents the feasible action and which mechanisms remain invariant. An intervention that changes a person’s hand movement while leaving their intention intact may describe a different option from a decision to form an intention. If different ways of realizing “the same” action have different effects, they should be represented separately.

Causal models also do not derive their structure from correlations alone. Observational data can sometimes identify an intervention effect under additional assumptions—for example, by adjusting for measured common causes:

\[
P(o\mid\operatorname{do}(a))
=\sum_z P(o\mid a,z)P(z).
\]

But this formula is justified only when the chosen variables \(Z\) block the relevant confounding paths and satisfy the necessary conditions. Otherwise causal knowledge, experiments, or further assumptions are needed. An agent can be uncertain about the model itself and average over plausible models, weighted by their probabilities given current evidence.

## 4. Counterfactuals and the limits of a formula

A causal decision rule cannot be more definite than its counterfactuals. Which features of the world should remain fixed when asking what would happen under a different action?

The reference article describes Lewis’s proposal of **imaging**: move probability mass from each possible world to a suitably close world in which the proposed action occurs. The outcome distribution in those worlds determines the action’s value. But “closeness” must be specified. A world where the action changes because of an external intervention may differ from one where it changes because the agent has a different personality; the two can have different predictions and outcomes.

Structural models make part of this choice explicit: background variables and non-intervened equations are retained while the action equation is replaced. Yet they do not eliminate philosophical uncertainty. The equations might be unknown, the action might have no well-defined intervention, or there may be multiple reasonable descriptions of the available choice.

The source also reports a concern that imaging may itself require a counterfactual specification of what the agent would believe under the supposition, threatening a regress. Whether that objection applies depends on the details of the imaging procedure. More generally, CDT’s mathematical expression is not a substitute for an account of how its counterfactual probabilities are obtained.

## 5. Newcomb’s problem: prediction without control

In Newcomb’s problem a predictor has already filled an opaque box \(B\): it contains \$1 million if the predictor predicted that the player would take only \(B\), and nothing if the predictor predicted that the player would take both boxes. A transparent box \(A\) contains \$1,000. The player now chooses one box or both.

Assume the predictor’s earlier act and the box contents are not causally affected by the present choice, and that money is valued linearly. If \(p\) is the current probability that \(B\) contains the million, then

\[
V_C(\text{one box})=1{,}000{,}000p,
\]
\[
V_C(\text{two boxes})=1{,}000{,}000p+1{,}000.
\]

Two-boxing causally dominates: for either fixed content of \(B\), it yields \$1,000 more. CDT therefore recommends taking both.

The predictor can nevertheless be highly accurate because prediction and choice share causes. To make the evidential calculation concrete, suppose one-boxers and two-boxers are equally common and the predictor is 99% accurate for each group. Then

\[
P(B\text{ full}\mid\text{one box})=0.99,\qquad
P(B\text{ full}\mid\text{two boxes})=0.01.
\]

EDT gives one-boxing an expected \$990,000 and two-boxing \$11,000. The figures depend on the joint distribution; an unconditional accuracy of 99% alone does not fix these conditional probabilities.

The disagreement is not that CDT denies the correlation. It is that CDT refuses to treat the correlation as causal control over an already filled box. Critics reply that a rule whose followers predictably receive less money is suspect. The reference article presents this as a genuine philosophical dispute, not a settled calculation of what rationality must demand. Nor is it true that every two-boxer necessarily gets only \$1,000: a predictor can be wrong, and a full box plus the transparent box pays \$1,001,000.

## 6. Policies, commitment, and timing

Many decisions concern policies rather than isolated acts. A policy \(\pi\) maps observations \(H\) to actions: \(A=\pi(H)\). A natural causal evaluation at the time a policy can be adopted is

\[
V_C(\pi)=\mathbb E[u(O_\pi)\mid I],
\]

where \(O_\pi\) is the outcome under an intervention installing that policy. This may include the causal effects of the policy on other people’s expectations, responses, and future events.

Timing matters. Suppose that *before* a predictor makes its prediction, a player can visibly bind themselves to one-box. If the binding causes the predictor to fill the opaque box, CDT can favor binding. Later, once the box is filled, an unbound player may still causally prefer two-boxing. These are different interventions at different times, with different available options and causal effects.

By contrast, if the predictor has already made its prediction, merely deciding now that one has a one-boxing “policy” does not automatically change the past. Whether an earlier policy choice actually causes a prediction is a modeling question, not a consequence of the word *policy*. Some alternative decision theories propose evaluating logical or subjunctive dependencies between an algorithm and a prediction even without an ordinary causal path; that is a substantive departure from the straightforward CDT interpretation developed here.

Sequential decisions also raise questions about commitment and consistency over time. If a future self can revise a policy, the initial evaluation should represent that possibility unless commitment is feasible. The source notes arguments that causal decision makers can be exposed to sequences of individually attractive trades that lose money overall. Assessing a particular “diachronic Dutch book” requires specifying what the agent knows, what commitments are available, and which trades are optional.

## 7. Information about one’s own choice

A common misunderstanding is that CDT must ignore evidence correlated with action. It does not. If David observes that he is strongly inclined to summon, and this inclination is evidence of uncharisma, he should update his beliefs before evaluating the available interventions. The reference article attributes to Joyce the view that CDT can account for information about what one is inclined or likely to do.

The delicate question is how far this updating should go. Learning one’s inclination is ordinary evidence. But simply considering the hypothetical intervention \(\operatorname{do}(A=a)\) is not, in the basic causal rule, the same as observing \(A=a\). Treating every contemplated action as news that it was actually chosen would collapse the distinction from EDT.

This tension appears in the **Psychopath Button**. Paul believes that pressing a button would kill all psychopaths, that a world without psychopaths would otherwise be better, and that only psychopaths would press it. He strongly prefers living with psychopaths to dying. If his current probability of being a psychopath is very low, a simple causal calculation may recommend pressing: the benefit seems to outweigh the small chance that he himself dies.

Yet pressing appears to be evidence that he is a psychopath. Critics argue that the recommendation is unstable or plainly wrong; defenders may say that Paul should incorporate evidence from his deliberation and inclinations. The case does not yield a unique numerical verdict without probabilities, utilities, and an account of what Paul knows at each stage. Its importance is that it challenges any crude instruction to “hold beliefs fixed” while ignoring genuine information acquired during deliberation.

## 8. Adversarial prediction and mixed choices

The reference article describes an **Adversarial Offer**. A buyer may purchase at most one of two boxes for \$1. Yesterday, the seller put \$3 in each box she predicted the buyer would not acquire. She predicts the buyer’s eventual choice with probability \(0.75\).

At least one box contains \$3: if the seller predicted purchase of one, the other is filled; if she predicted no purchase, both are filled. Holding the past filling fixed, the sum of the two boxes’ causal expected gross values is therefore at least \$3. At least one has gross expected value at least \$1.50, so a simple CDT calculation prefers buying some box to buying none.

But if the prediction is correct with probability \(0.75\), the box actually bought is empty in those correctly predicted purchase cases. In the standard setup, the buyer pays \$1 and receives \$3 only when the purchased box was predicted not to be purchased. Thus expected profit can be

\[
0.25(3)-1=-0.25.
\]

The tension is between the profitable-looking intervention, which holds fixed a distribution over past fillings, and the unfavorable distribution correlated with the choice actually made.

This example requires care about strategies and beliefs. A buyer might use a private randomizer, and the seller’s prediction accuracy must then be specified for that strategy rather than assumed unchanged. Randomization can alter what a predictor can know and can change the relevant probabilities. It also does not make the basic problem disappear by definition: the causal values of the available mixed policies must still be computed in a coherent joint model of prediction, randomization, and purchase. The example is a criticism of a straightforward causal procedure under its stipulated correlations, not a proof that every predictor can defeat every version of CDT.

## 9. A practical procedure

For an unfamiliar problem, the following workflow makes the assumptions visible:

1. **Fix the decision point and available options.** Distinguish an immediate act from an earlier commitment, a randomized choice, or a policy contingent on later observations.
2. **Specify outcomes and utilities.** Include relevant side effects, costs, risks, and the welfare of affected people.
3. **Record actual information.** Update on observations already available, including reliable evidence about one’s inclinations, without treating each hypothetical action as observed fact.
4. **Build causal hypotheses.** Identify common causes, downstream effects, other agents’ responses, and any uncertainty about the causal structure.
5. **Evaluate interventions.** For each feasible option, estimate the outcome distribution under that option while retaining the background and mechanisms appropriate to the intervention.
6. **Compare expected utilities and test sensitivity.** Check whether the recommendation changes under plausible probabilities, utilities, or causal models.

The most consequential step is often the fourth or fifth. Calling something “past,” “correlated,” or “a policy” does not by itself settle every causal question. The relevant issue is what the particular feasible intervention can change.

## Conclusion

CDT directs an agent toward the action with the best expected consequences under an appropriate causal counterfactual. Its appeal is that it separates making the world better from merely receiving good news about it. Its difficulty is that counterfactuals, information gained during deliberation, and the boundaries of feasible interventions are not supplied by the maxim itself. In ordinary cases a causal model can make the procedure usable; in prediction and self-knowledge cases, the right interpretation remains philosophically contested.

### References

- Gibbard, A. and Harper, W. L. (1981). “Counterfactuals and Two Kinds of Expected Utility.”
- Lewis, D. (1981). “Causal Decision Theory.” *Australasian Journal of Philosophy* 59.
- Egan, A. (2007). “Some Counterexamples to Causal Decision Theory.” *The Philosophical Review* 116.
- Oesterheld, C. and Conitzer, V. (2021). “Extracting Money from Causal Decision Theorists.” *The Philosophical Quarterly* 71.
- Wikipedia contributors. [“Causal decision theory,” revision 1381555528](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528). CC BY-SA 4.0.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/7599c93f-2519-4f0c-a95f-352fcde5b163/call_0/request.json)

[Authoritative raw response](../../../../../../runs/7599c93f-2519-4f0c-a95f-352fcde5b163/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/7599c93f-2519-4f0c-a95f-352fcde5b163/call_1/request.json)

[Authoritative raw response](../../../../../../runs/7599c93f-2519-4f0c-a95f-352fcde5b163/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
