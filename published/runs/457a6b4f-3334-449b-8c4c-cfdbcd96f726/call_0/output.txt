# Causal decision theory: choosing by what actions bring about

A decision can be good news without being a good intervention. If people who carry umbrellas are unusually likely to encounter rain, acquiring an umbrella may make it more likely that one is the sort of person who expects rain. But, ordinarily, carrying it does not cause rain. It causes one to be better protected *if* it rains.

Causal decision theory (CDT) builds a rule for choice around that distinction. Roughly, an agent should choose the available action with the greatest expected utility under the hypothesis that the action is performed. The relevant hypothesis is counterfactual: what would happen *if the agent did this*, rather than what is likely to be true *on learning that the agent does this*?

This sounds simple, but its application requires more than a table of correlations. One needs a model of the effects of interventions, probabilities for uncertain features of the world, and utilities for outcomes. Moreover, CDT is a family of related proposals, not a complete algorithm for deriving those ingredients. The structural-model procedure developed below is an operational interpretation of the article’s central idea, not the only possible formulation of CDT.

## From expected outcomes to counterfactuals

Suppose the available actions are \(a\in\mathcal A\), and the outcomes \(O_1,\ldots,O_n\) form a mutually exclusive and exhaustive partition. Let \(u(O_j)\) be the utility of outcome \(O_j\). The reference article presents Gibbard and Harper’s formulation:

\[
V_{\mathrm C}(a)
  =\sum_{j=1}^n P(a\mathbin{\Box\!\!\to}O_j)\,u(O_j),
\qquad
a^*\in\operatorname*{arg\,max}_{a\in\mathcal A}V_{\mathrm C}(a).
\]

Here \(a\mathbin{\Box\!\!\to}O_j\) is the counterfactual “if \(a\) were done, \(O_j\) would occur.” It should not be read as ordinary material implication, nor as a claim that \(a\) logically or necessarily entails \(O_j\). The probability expresses uncertainty about the relevant counterfactual.

For example, an apple is good with probability \(0.7\). Eating a good apple has utility \(10\); eating a bad one has utility \(-8\). If eating the apple does not affect its quality, then

\[
V_{\mathrm C}(\text{eat})=0.7(10)+0.3(-8)=4.6.
\]

If declining has utility \(0\), CDT recommends eating. The example is uncontroversial because the causal structure is simple: apple quality is uncertain, and the effects of eating depend on it.

The utilities must include all consequences the agent cares about. They need not be money, and an action’s moral significance can be included if the agent values it. Expected utility also requires attention to risk: if the agent is risk-averse over money, the utility of \(\$1{,}000{,}000\) is not automatically one thousand times the utility of \(\$1{,}000\).

## Why conditioning is not the same question

Evidential decision theory (EDT) instead assigns an action the value

\[
V_{\mathrm E}(a)
  =\sum_j P(O_j\mid A=a)\,u(O_j).
\]

The question is what outcomes the action would be evidence for, conditional on the agent’s doing it. Both theories use expected utility, but they can use different probability distributions.

Consider a population in which a hidden trait \(H\) influences both a person’s preference for smoking and their risk of disease. Assume, for illustration, that smoking itself has no effect on disease. Smokers may then have a higher disease rate than nonsmokers:

\[
P(\text{disease}\mid A=\text{smoke})
>
P(\text{disease}\mid A=\text{abstain}).
\]

Yet setting smoking by intervention leaves the trait unchanged, so the disease probabilities under the two interventions are equal. CDT will not count abstaining as a way to remove disease risk due solely to \(H\). This is a hypothetical causal structure, not a claim about actual smoking.

The reference notes that, under suitable axioms, independence between an action and the relevant counterfactuals is sufficient for counterfactual probabilities to match the corresponding conditional probabilities. Intuitively, if the action is not evidence about which counterfactual circumstances obtain, learning that it occurs does not distort the assessment. In practice that independence must be argued for, not assumed.

The article also cites Lewis’s work on the difference between probabilities of conditionals and conditional probabilities. The important lesson for decision-making is modest but consequential: \(P(a\mathbin{\Box\!\!\to}O)\) cannot generally be replaced by \(P(O\mid a)\) merely as a matter of probability theory.

## An operational causal model

One useful way to make the counterfactual calculation explicit is to model the world with structural equations. Let \(W\) represent uncertain background features, \(A\) the action, and \(Y\) an outcome:

\[
A=f_A(W),\qquad Y=f_Y(A,W).
\]

In the actual world, the agent’s action may depend on \(W\): for instance, an inclination, information, or personality trait may influence the choice. To evaluate the intervention \(do(A=a)\), replace the first equation with \(A=a\), while retaining the other equations. The resulting outcome is

\[
Y_a=f_Y(a,W).
\]

Given current evidence \(E\), an operational CDT value is

\[
V_{\mathrm C}(a\mid E)
 =\mathbb E[u(Y_a,a)\mid E].
\]

The explicit \(a\) in the utility function allows the action itself, as well as the downstream outcome, to matter. If \(W\) takes discrete values, the same calculation is

\[
V_{\mathrm C}(a\mid E)
 =\sum_w P(w\mid E)\,u\!\left(f_Y(a,w),a\right).
\]

This equation clarifies what “holding fixed” means. The *same current distribution* over relevant background circumstances is used to evaluate each intervention. It does **not** mean that all variables are held fixed: variables causally downstream of the action must change when the model says they change. If taking medicine affects recovery, recovery is recalculated under each treatment. If a predictor has already filled a box and the current choice cannot alter its contents, those contents are not recalculated as a consequence of the choice.

The model may also contain uncertainty about causal laws. Let \(H\) index possible causal hypotheses, with different functions \(f_Y^H\). Then

\[
V_{\mathrm C}(a\mid E)
 =\sum_h P(h\mid E)\,
   \mathbb E\!\left[u(Y_a,a)\mid E,H=h\right].
\]

An agent need not know for certain whether medicine works, whether a threat is credible, or whether an opponent can observe an action. Those uncertainties enter the expectation. What CDT excludes is treating an action as if it changes a background hypothesis merely because the action would be evidence for that hypothesis.

This procedure depends on substantive assumptions. In particular, the proposed intervention must correspond to a meaningful available action, and the model must say which mechanisms remain stable when it is performed. Observational data alone do not always identify those mechanisms. Two models can fit the same correlations while disagreeing about what an intervention would do.

## The king and the revolt

The article’s example of King David brings the difference into focus. David desires to summon Bathsheba but fears a successful revolt. He believes that charismatic kings tend to behave justly and face less risk of successful revolt; uncharismatic kings tend to behave unjustly and face more risk. His charisma is fixed by earlier causes. Crucially, in the stipulated story, the unjust act itself does not cause revolt.

A numerical version makes the calculation visible. Suppose David assigns probability \(1/2\) to being charismatic. A successful revolt has probability \(0.1\) if he is charismatic and \(0.8\) otherwise. Let a revolt cost him \(100\) utility units, and let summoning Bathsheba provide a benefit of \(5\), with no other utility effect. His causal revolt probability under either action is

\[
\tfrac12(0.1)+\tfrac12(0.8)=0.45.
\]

Thus abstaining has value \(-45\), while summoning has value \(5-45=-40\). CDT recommends summoning on these stipulated utilities and causal assumptions.

The evidential calculation can differ. Suppose, for example, charismatic kings summon with probability \(0.1\), while uncharismatic kings do so with probability \(0.9\). Observing that David summons would then be strong evidence that he is uncharismatic. Abstention would be evidence in the opposite direction. EDT may therefore favor abstention, despite the assumption that abstention does not change charisma or revolt risk.

Nothing in CDT requires ignoring injustice, or believing unjust acts never provoke resistance. If David assigns a moral cost to the act, or has evidence that it affects revolt, those factors belong in the causal calculation. The example isolates the dispute by stipulation.

## Newcomb’s problem and causal dominance

In Newcomb’s problem, an opaque box contains \(\$1{,}000{,}000\) if a predictor previously predicted that the player would take only that box, and nothing otherwise. A transparent box always contains \(\$1{,}000\). The player chooses either the opaque box alone or both boxes.

At the moment of choice, assume the prediction and box contents are fixed, and the choice has no causal influence on them. Let \(B\) be the amount in the opaque box. Then

\[
\begin{aligned}
V_{\mathrm C}(\text{one box})&=\mathbb E[u(B)],\\
V_{\mathrm C}(\text{two boxes})&=\mathbb E[u(B+1000)].
\end{aligned}
\]

With money-valued utility, two-boxing is exactly \(\$1{,}000\) better in every fixed state. With any strictly increasing utility of money, it is still better. This is **causal dominance**: for each possible content of the opaque box, the two-box action produces the preferable result.

Nevertheless, if the predictor is 99% accurate, the observed correlation between choice and contents strongly favors one-boxers. Under the simple conditional assumptions

\[
P(B=\$1{,}000{,}000\mid\text{one box})=0.99,\quad
P(B=\$1{,}000{,}000\mid\text{two boxes})=0.01,
\]

and money-valued utility, EDT assigns one-boxing \(\$990{,}000\) and two-boxing \(\$11{,}000\). These probabilities are assumptions about the conditional distribution, not consequences of accuracy alone without further specification.

The disagreement is not that CDT denies the correlation. It denies that choosing one box now causes the earlier prediction or the already-set contents to change. Critics answer that a theory recommending the choice associated with much lower winnings has missed something important. The reference presents this as a genuine philosophical dispute, not a settled demonstration for either theory.

## Policies, commitments, and timing

An action can be a rule for future behavior rather than a single physical movement. Suppose an agent can now choose a policy \(\pi\), which maps later observations \(x\) to actions \(\pi(x)\). A causal evaluation of policies asks

\[
V_{\mathrm C}(\pi\mid E)
 =\mathbb E[u(Y_\pi)\mid E],
\]

where \(Y_\pi\) is the outcome under an intervention installing policy \(\pi\). The causal model must include the observations the agent will receive, how the policy responds, and how other people or predictors react to it.

Timing is decisive. If a player can commit to one-boxing *before* a predictor makes its prediction, and the commitment causally influences that prediction, CDT can value the commitment because it helps fill the opaque box. Once the prediction is made and the contents are fixed, the later choice may still favor two-boxing. This is not a contradiction: the two decisions have different available interventions and different causal consequences.

A policy must also be genuinely implementable. Writing “I shall one-box later” on paper is not necessarily a commitment if the agent can freely disregard it; conversely, a binding device may impose costs or remove later options. The model should represent those facts rather than treating every announced policy as enforced.

This issue appears in games. Against an opponent whose move is fixed and unaffected by one’s present move, CDT recommends a causally dominant defection in an ordinary prisoner’s dilemma. If choosing or committing to a policy influences the opponent’s response, cooperation may instead be causally valuable. A “twin” whose choice is highly correlated with yours, but not caused by it, recreates the difficult Newcomb-like distinction: correlation alone favors cooperation evidentially, while one-shot causal dominance can favor defection.

## Information about one’s own decision

The instruction to use current beliefs does not mean the agent must disregard evidence about itself. The reference reports Joyce’s view that CDT can take an agent’s information about what it is inclined or likely to do as evidence. If I notice that I am tempted to smoke, that observation may update my beliefs about a hidden trait before I evaluate smoking and abstaining. Both causal calculations should then use the updated beliefs.

But how much evidence about the choice is available *before* the choice is settled can be contested. Egan’s “Psychopath Button” makes the problem vivid. Paul prefers a world without psychopaths, but fears that only a psychopath would press a button killing all psychopaths. He strongly prefers living with psychopaths to dying.

For a numerical illustration, suppose Paul’s current probability of being a psychopath is \(0.01\); pressing yields utility \(10\) if he is not one and \(-100\) if he is; abstaining yields \(0\). A simple causal calculation gives

\[
V_{\mathrm C}(\text{press})=0.99(10)+0.01(-100)=8.9.
\]

It recommends pressing. Yet if the act of pressing would be extremely strong evidence that Paul is a psychopath, an evidential calculation might recommend abstaining.

The example exposes an ambiguity rather than mechanically refuting every version of CDT. If Paul’s awareness of his inclination already gives him strong evidence that he is a psychopath, his current probability might be far higher than \(0.01\), changing the causal recommendation. The difficult question is how deliberation and self-knowledge update that probability, and whether holding one fixed distribution throughout the comparison adequately represents an agent whose contemplated choice is itself informative. The reference identifies this concern but does not settle it.

## Adversarial prediction and randomized choices

The reference’s adversarial-offer example sharpens the worry. A seller offers two boxes, each costing \(\$1\). Yesterday she put \(\$3\) in every box she predicted the buyer would **not** acquire. The buyer may purchase at most one box. At least one box therefore contains \(\$3\), so, for any current beliefs about the fixed contents, the average causal value of the two boxes is at least \(\$1.50\). At least one box has causal expected net value at least \(\$0.50\), making purchase preferable to buying none.

Now assume the seller predicted the buyer’s actual acquired box with probability \(0.75\). On a correct prediction, that box is empty and the buyer loses \(\$1\); on an incorrect prediction of the other box, the acquired box contains \(\$3\), giving a net gain of \(\$2\). The correlated pattern of play therefore gives expected net payoff

\[
0.75(-1)+0.25(2)=-0.25.
\]

The causal recommendation and the negative payoff are not arithmetically inconsistent. The first uses fixed box contents across interventions; the second uses the correlation between the seller’s earlier prediction and the actual purchase. The example raises the question whether a rational rule should accept a locally attractive intervention when adherence to the rule predictably produces losses.

Randomization also requires a causal model. If an agent can use a private, genuinely unpredictable random device after the seller has filled the boxes, then an equal lottery over the two boxes has expected net value at least \(\$0.50\) under the stated setup. A claim that the seller predicts the *realized* random purchase with 75% accuracy would conflict with the assumption of an independent fair draw. Alternatively, the seller might predict the policy but not its realization, or have access to the random seed. “Randomize” is therefore not a complete solution until the timing and predictability of the randomization are specified.

## What CDT leaves open

The reference explicitly notes that CDT does not itself supply an algorithm for counterfactual probabilities. Lewis’s **imaging** is one proposal: to evaluate an action, move probability mass from each possible world to a closest world in which that action occurs, then inspect outcomes there. But “closest” depends on what features are preserved and what causal laws are allowed to change. The article also reports a regress worry about what the agent would believe if certain of the action.

Structural equations make those choices explicit rather than eliminating them. They require a specification of interventions and stable mechanisms; in unusual cases, especially choices correlated with predictions, different defensible specifications may yield different answers. Nor does causal decision theory alone determine utilities, identify available commitments, or resolve all questions about updating during deliberation.

For an unfamiliar problem, a practical procedure is therefore:

1. **Fix the decision point and options**, including any available policies or commitments.
2. **List relevant outcomes and utilities**, including costs and morally valued effects.
3. **Represent current evidence and causal uncertainty**, including evidence about one’s own dispositions.
4. **For each option, intervene on that option** and propagate its causal consequences without automatically changing upstream facts.
5. **Compare expected utilities**, checking whether correlations, timing, or an unstable causal model are doing essential work.

If the result is surprising, the next step is not necessarily to reject it: first check the stipulated causal links and available actions. But if the result remains unattractive, the case may reveal a substantive dispute about the decision rule itself.

## Conclusion

CDT recommends the action with the best expected causal consequences, not simply the action associated with the best news. Its strength is a disciplined distinction between changing the world and learning about it. Its difficulties arise when an agent’s action is deeply correlated with fixed but hidden circumstances, or when the relevant counterfactual intervention is unclear. Applying CDT well requires both a calculation and an explicit defense of the causal model that makes that calculation meaningful.

### References

- Wikipedia contributors, [“Causal decision theory,” revision 1381555528](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528).
- Gibbard, A. and Harper, W. L. (1981), “Counterfactuals and two kinds of expected utility,” in *Ifs: Conditionals, Beliefs, Decision, Chance, and Time*.
- Lewis, D. (1981), “Causal decision theory,” *Australasian Journal of Philosophy* 59, 5–30.
- Egan, A. (2007), “Some counterexamples to causal decision theory,” *The Philosophical Review* 116, 93–114.
- Oesterheld, C. and Conitzer, V. (2021), “Extracting Money from Causal Decision Theorists,” *The Philosophical Quarterly* 71.