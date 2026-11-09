# 002_cdt_wikipedia_openai_gpt-6.1-terra_rlow_plow / 00009

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/dd79523e-0b1b-4dff-8e35-3596542b9725/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/dd79523e-0b1b-4dff-8e35-3596542b9725/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal decision theory: choosing what makes a difference

A decision can be good news without being a good intervention. A patient who takes a drug may be less likely to recover than one who does not, because doctors reserve it for the sickest patients. A driver who brakes hard may be unusually likely to crash, because braking is often a response to imminent danger. In neither case does the correlation by itself tell us what would happen if we changed the action.

Causal decision theory (CDT) turns this distinction into a rule for choice: select an available action with the best **expected causal consequences**. It contrasts with evidential decision theory (EDT), which evaluates an action by asking how desirable the world would be *conditional on receiving the news that the action was taken*. The theories agree in many ordinary decisions, but they can disagree when an action is evidence about circumstances that it does not cause.

The reference article presents CDT through counterfactual probabilities and emphasizes that it is a family of views rather than a complete algorithm. To use it in a concrete problem, one needs probabilities, utilities, and an account of what changes under each hypothetical action. Structural causal models provide one useful operational interpretation, but they are an additional modeling choice, not a definition supplied by CDT itself.

## 1. Actions, outcomes, and counterfactuals

Suppose an agent has a set of available actions \(\mathcal A\), possible outcomes \(O_1,\ldots,O_n\), and utilities \(u(O_j)\). Gibbard and Harper’s formulation, as reported in the reference article, assigns an action \(a\) the value

\[
V_{\mathrm C}(a)
=\sum_{j=1}^{n} P(a\mathbin{\Box\!\!\to}O_j)\,u(O_j),
\]

and recommends an action in

\[
\operatorname*{arg\,max}_{a\in\mathcal A}V_{\mathrm C}(a).
\]

Here \(a\mathbin{\Box\!\!\to}O_j\) expresses a counterfactual: *were action \(a\) taken, outcome \(O_j\) would occur*. Its probability measures uncertainty about that counterfactual, not merely the frequency of \(O_j\) among occasions on which \(a\) is actually taken. The arrow should not be read as ordinary material implication or as the claim that \(a\) logically necessitates \(O_j\).

For the formula to behave as an expected-utility calculation, the relevant counterfactual outcomes should be sufficiently well specified and mutually exclusive and exhaustive. If actions themselves matter—for example, a person regards an unjust act as bad even if it has no adverse external consequences—include the action in the outcome description, or write utility as \(u(a,O_j)\).

Consider an apple that is good with probability \(0.7\). Eating it yields utility \(+10\) if good and \(-8\) if bad; declining it has utility \(0\). If eating does not alter its prior condition, then

\[
V_{\mathrm C}(\text{eat})
=0.7(10)+0.3(-8)=4.6,
\qquad
V_{\mathrm C}(\text{decline})=0.
\]

CDT recommends eating. The example is simple because “good apple” is a relevant background condition unaffected by the action. In difficult cases the dispute is precisely over which conditions to hold fixed and which consequences to let change.

EDT instead uses

\[
V_{\mathrm E}(a)
=\sum_j P(O_j\mid A=a)\,u(O_j),
\]

where \(A\) denotes the action actually taken. In the apple example, the two values agree if the choice provides no further evidence about the apple’s condition. They can differ if, for instance, the agent tends to eat only apples that a reliable but unconscious sensory process detects as good.

The reference notes that Gibbard and Harper give sufficient conditions under which the probability of an action and that of the relevant counterfactual are independent, making causal and evidential probabilities coincide. But such independence cannot be assumed in general. Lewis’s results on probabilities of conditionals also warn against identifying counterfactual probability with ordinary conditional probability as a universal rule.

## 2. A practical causal-model interpretation

A useful way to make the counterfactual calculation operational is to model the situation with structural equations. Let \(H\) describe background factors and causal mechanisms, and let \(Y\) be the outcome. A simple model might have

\[
A=g(H,\varepsilon_A),\qquad
Y=f(A,H,\varepsilon_Y).
\]

The first equation describes how the actual action is generated; the second describes how action and circumstances generate the outcome. To evaluate an intervention \(do(A=a)\), replace the first equation by \(A=a\), while leaving the other mechanisms in place. Then

\[
V_{\mathrm C}(a)
=\mathbb E\!\left[u(a,Y)\mid do(A=a),E\right],
\]

where \(E\) is the agent’s information at the decision point. Equivalently, with \(Y_a\) denoting the outcome that would result from \(a\),

\[
V_{\mathrm C}(a)=\mathbb E[u(a,Y_a)\mid E].
\]

This intervention breaks the ordinary causal links *into* the action, not the links *out of* it. If taking medicine causes side effects, the side effects remain in the calculation. If poor health causes a doctor to prescribe medicine, intervening on the prescription does not thereby make the patient healthy.

A dependency-state formulation makes the same idea explicit. Let \(h\) specify enough about the world to determine the consequences of each action, and let \(Y(a,h)\) be the outcome under \(a\). Then

\[
V_{\mathrm C}(a)=\sum_h P(h\mid E)\,u(a,Y(a,h)).
\]

The same distribution \(P(h\mid E)\) is used for each candidate action, provided \(h\) describes background factors or mechanisms unaffected by that intervention. This is the sense in which CDT “holds fixed” prior views about dependency hypotheses. It does **not** mean holding all features of the world fixed: descendants of the action must be recomputed.

This interpretation has limits. A causal diagram does not arrive with the problem; the agent must choose variables, directions, equations, and probabilities. The intervention \(do(A=a)\) is also an idealization. If forcing a decision would itself require a drug, threat, or mechanical device with side effects, those effects need either to be included in the action or distinguished from the intended counterfactual. An action description such as “press the button” may be too coarse if different ways of pressing it have different consequences.

## 3. Correlation, evidence, and the king

The reference recounts Gibbard and Harper’s example of King David. David wants to summon Bathsheba but fears revolt. Charismatic kings tend to behave justly and rarely face successful revolts; uncharismatic kings tend to behave unjustly and more often face successful revolts. The personality type is fixed by early causes. By assumption, the unjust act itself does not cause a successful revolt.

The relevant structure is

\[
\text{charisma}\longrightarrow\text{action},
\qquad
\text{charisma}\longrightarrow\text{revolt}.
\]

There is no arrow from the particular act to revolt. Thus David’s summoning may be evidence that he is uncharismatic, and therefore evidence of revolt. But if the stipulated causal model is right, deciding to summon does not change his charisma or the revolt probability.

The example becomes clearer with numbers. Suppose charismatic and uncharismatic types each have prior probability \(1/2\); summoning is chosen with probabilities \(0.1\) and \(0.9\), respectively; and revolt probabilities are \(0.01\) and \(0.30\). Conditioning on the act gives

\[
P(\text{uncharismatic}\mid\text{summon})=0.9,
\]

so

\[
P(\text{revolt}\mid\text{summon})
=0.9(0.30)+0.1(0.01)=0.271.
\]

By contrast, conditioning on abstention gives a revolt probability of \(0.039\). But under either intervention, with the prior type distribution unchanged,

\[
P(\text{revolt}\mid do(\text{summon}))
=P(\text{revolt}\mid do(\text{abstain}))
=0.155.
\]

EDT can therefore count summoning as bad news about revolt; CDT does not count the evidential association as an effect of summoning. Whether CDT ultimately recommends it still depends on all utilities. The reference’s recommendation assumes that David’s benefit from summoning exceeds any other disvalue of the act. CDT does not itself say that injustice has zero utility cost.

## 4. Newcomb’s problem and causal dominance

Newcomb’s problem makes the same distinction especially vivid. A transparent box contains \$1,000. An opaque box contains either \$1 million or nothing, according to a prediction already made: it is filled if the predictor predicted that the player would take only the opaque box, and empty if the predictor predicted both boxes.

At the moment of choice, let \(B\) be the opaque box’s fixed content. Assuming utility is linear in these monetary amounts, causal evaluation gives

\[
V_{\mathrm C}(\text{both})=\mathbb E[B\mid E]+1000,
\qquad
V_{\mathrm C}(\text{opaque only})=\mathbb E[B\mid E].
\]

Taking both causally dominates: whatever is already in the opaque box, both yields \$1,000 more. This conclusion depends on the stipulation that the present intervention cannot change the past prediction or the box’s contents.

Yet if the predictor is \(99\%\) accurate, a simplified evidential calculation gives

\[
V_{\mathrm E}(\text{opaque only})\approx \$990{,}000,
\qquad
V_{\mathrm E}(\text{both})\approx \$11{,}000.
\]

The numerical conditional probabilities require a suitable calibration assumption—for example, \(99\%\) accuracy conditional on each kind of choice, not merely \(99\%\) overall. On those assumptions, one-boxing is strong evidence that the opaque box is full.

The disagreement is not over arithmetic but over which question governs choice. CDT asks what adding the transparent box changes, holding fixed the already determined content. EDT asks what the choice reveals about that content. A one-boxer can point out that players like them generally receive more; a two-boxer can reply that, at the choice point, taking the extra \$1,000 cannot empty a box already filled. The reference treats which answer is rational as contested.

The same issue appears in a prisoner’s dilemma against a highly similar “twin.” If the twin’s move is correlated with yours through common dispositions, but your present move does not cause theirs, standard CDT can recommend defection even though cooperation would be evidence of mutual cooperation. If, however, your move is observed and causally influences the other player, that influence belongs in CDT’s calculation. Correlation alone and causal response are different models.

## 5. Choosing a policy rather than an immediate act

The unit of choice matters. Suppose, before the predictor examines you, you can install a binding mechanism that makes you take only the opaque box. If the predictor can detect that mechanism, installing it may *cause* the predictor to fill the box. CDT can then favor the commitment, even though at the later choice point, absent an effective constraint, it favors taking both boxes.

More generally, a policy \(\pi\) maps future information \(s\) to actions, \(a=\pi(s)\). Its causal value is

\[
V_{\mathrm C}(\pi)
=\mathbb E[u(Y_\pi)\mid E_0],
\]

where \(Y_\pi\) is the outcome under an intervention that adopts the policy at the earlier decision point. The model must include how adoption affects later information, other people’s responses, and available actions. One should not simply substitute the evidential association between a policy and success for its causal effect.

This creates a potential tension between ex ante and later evaluation. An earlier self may want to bind a later self precisely because the later self, reassessing the remaining options, would choose differently. A commitment is valuable only if it is available and sufficiently reliable; merely announcing an intention is not the same as making future deviation impossible. If the predictor acted before any possible policy adoption, the earlier causal advantage may disappear.

Thus “CDT recommends two-boxing” is a claim about a particular decision point and option set. It is not a general prohibition on precommitment or on designing a decision procedure with good causal effects.

## 6. What evidence should the agent use?

Holding a probability distribution fixed *across counterfactual interventions* does not require ignoring actual information. If David learns from a test that he is likely uncharismatic, or if Paul notices a strong inclination to press a disturbing button, CDT can update on that evidence before evaluating alternatives.

The distinction becomes delicate when deliberation itself changes what the agent knows. In Egan’s “psychopath button” example, Paul prefers a world without psychopaths but strongly prefers survival to death; he also believes that only a psychopath would press the button. If his pre-decision probability of being a psychopath is very low, a simple CDT calculation might favor pressing: it treats his type as fixed and weighs the benefit of eliminating others against the small chance of killing himself. Yet pressing would be alarming evidence that he is himself a psychopath.

For an illustration, suppose the benefit if he is not a psychopath is \(+10\), the cost if he is one is \(-1000\), and his current probability of being one is \(0.001\). Taking not pressing as utility zero,

\[
V_{\mathrm C}(\text{press})
=0.999(10)+0.001(-1000)=8.99.
\]

But if the actual inclination to press raises his probability of psychopathy above roughly \(10/1010\), pressing becomes causally unfavorable on these utilities. Joyce’s response, noted in the reference, is that CDT can use information about one’s inclinations. The hard question is which such information is available during deliberation and how to reach a stable assessment without treating a merely hypothetical choice as observed evidence.

One operational proposal is to distinguish three stages: update on genuine observations available now; evaluate each intervention using that same updated background distribution; update again if deliberation produces a genuinely informative observation. This is useful, but it does not settle every case. An agent may find that deciding to press would itself be evidence against pressing, creating instability between a provisional decision and the credences it induces. CDT has variants and proposed responses to such cases; the basic expected-utility formula alone does not specify which stability requirement to impose.

## 7. Adversarial prediction and guaranteed losses

The reference also describes the *Adversarial Offer*. A seller predicts which of two boxes a buyer will acquire and previously puts \$3 in every box predicted not to be acquired. Each box costs \$1; the buyer may buy at most one or buy none.

At least one box contains \$3, assuming the seller follows the stated rule even if she predicts no purchase. Hence the sum of the two boxes’ expected contents is at least \$3, so at least one has expected content at least \$1.50. If the contents are already fixed and a purchase cannot change them, a simple CDT calculation assigns that box an expected net value of at least

\[
\$1.50-\$1=\$0.50.
\]

Buying it therefore looks better than abstaining, which yields zero.

Now suppose the seller’s prediction of the actual purchase is correct with probability \(0.75\), and when correct she leaves the acquired box empty. The buyer’s actual expected net payoff is at most

\[
0.75(-\$1)+0.25(\$2)=-\$0.25.
\]

The upper bound assumes that every incorrect prediction results in the purchased box being filled. The seller’s expected profit is correspondingly positive if the buyer buys. There is no contradiction in the two calculations: the causal calculation evaluates a chosen box against the fixed distribution of contents, while prediction accuracy describes a correlation between the actual purchase and which box was left empty. The example challenges whether maximizing the former is adequate when an adversary can exploit the latter.

It also exposes a modeling issue: probabilities, prediction accuracy, and the agent’s decision procedure must fit together consistently. It is not enough to stipulate arbitrary conditional probabilities independently of how the seller predicts and how the buyer chooses. The source reports further arguments involving repeated or sequential offers and diachronic Dutch books; their force depends on the timing and commitments in the particular construction.

## 8. What CDT leaves open

The central instruction—choose by expected causal consequences—does not uniquely determine a counterfactual model. Lewis’s proposed *imaging* is one approach: move probability mass from each world to a closest world where the contemplated action occurs. The difficulty is specifying closeness. A world in which an agent acts differently may also differ in psychology, prediction, or history; different similarity rules can produce different answers. The reference reports a further regress worry about what the agent would believe if certain of the action.

Structural interventions avoid some of that ambiguity by explicitly specifying what equations change. But they do not eliminate substantive assumptions. Which variables are causally upstream? Can the agent actually implement each intervention? Are the relevant mechanisms known? Can one identify interventional effects from available data? Observational associations alone generally cannot answer those questions without causal assumptions.

For an unfamiliar problem, a disciplined application is therefore:

1. **Fix the decision point, feasible options, and utility.** Include morally or personally relevant features in the outcomes.
2. **Record the evidence actually available.** Distinguish it from the hypothetical supposition that an option is taken.
3. **Model causal dependencies.** Identify background factors, mechanisms, and consequences that each action may change.
4. **Evaluate each intervention** using the same evidence-conditioned background distribution, while propagating its downstream effects.
5. **Check sensitivity.** If a different causal model, information state, policy option, or utility ordering changes the answer, state that dependence.

This procedure is a practical proposal consistent with the reference’s account, not a claim that all causal decision theorists resolve every counterexample in the same way.

## Conclusion

CDT asks what each available action would bring about, not merely what it would reveal. Its strength is the insistence that correlation and causal influence be distinguished; its difficulty is that the counterfactuals needed for choice are themselves substantive and sometimes controversial. Careful application requires more than the slogan “cause the best outcome”: it requires an explicit decision point, a causal model, appropriate evidence, and attention to whether the object of choice is an immediate act or an earlier policy.

### References

- Wikipedia contributors, [“Causal decision theory,” revision 1381555528](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528).
- Gibbard, A., and Harper, W. L. (1981), “Counterfactuals and two kinds of expected utility.”
- Lewis, D. (1981), “Causal decision theory,” *Australasian Journal of Philosophy* 59: 5–30.
- Egan, A. (2007), “Some counterexamples to causal decision theory,” *The Philosophical Review* 116: 93–114.
- Oesterheld, C., and Conitzer, V. (2021), “Extracting Money from Causal Decision Theorists,” *The Philosophical Quarterly* 71.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/bb97cc3f-f932-4350-9ffb-f269c2cb3961/call_0/request.json)

[Authoritative raw response](../../../../../../runs/bb97cc3f-f932-4350-9ffb-f269c2cb3961/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/bb97cc3f-f932-4350-9ffb-f269c2cb3961/call_1/request.json)

[Authoritative raw response](../../../../../../runs/bb97cc3f-f932-4350-9ffb-f269c2cb3961/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
