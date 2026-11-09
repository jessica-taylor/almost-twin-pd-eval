# Choosing Causes, Not Signs: A Mathematical Guide to Causal Decision Theory

A decision can matter in two different ways. It can **change what happens**, and it can **indicate what was already likely to happen**. These often coincide, but they need not. Taking medicine may improve your health while also being evidence that you are seriously ill. Refusing the medicine would remove that evidence without necessarily removing the illness.

Causal decision theory (CDT) distinguishes these roles. Its central recommendation is to choose the action with the best expected **causal consequences**, rather than the action most strongly associated with desirable outcomes.

That principle is intuitive. The difficulty lies in specifying what would happen *if an action were performed*, especially when actions correlate with hidden traits, predictors, or other agents. This essay develops the reference article’s counterfactual formulation, gives an operational interpretation using causal models, and examines where that interpretation remains controversial.

## 1. Expected utility over counterfactual outcomes

Let:

- \(\mathcal A\) be the available actions;
- \(I\) be the agent’s present information;
- \(O_1,\ldots,O_n\) be mutually exclusive, exhaustive outcomes;
- \(u(O_j)\) be the utility of outcome \(O_j\).

Utilities represent everything the agent values, including costs, risks, moral considerations, and effects on others. They need not equal money.

The reference article presents Gibbard and Harper’s formulation:

\[
U(A)=\sum_j P(A\to O_j)D(O_j).
\]

The intended conditional is counterfactual: roughly, “if \(A\) were performed, \(O_j\) would result.” It should not be read as material implication or as a claim of logical necessity.

Write \(O_a\) for the outcome that would occur under action \(a\). Then a convenient formulation is

\[
V_{\mathrm C}(a\mid I)
=\mathbb E[u(O_a)\mid I]
=\sum_j P(O_a=O_j\mid I)u(O_j).
\]

CDT recommends any maximizer:

\[
a^*\in\operatorname*{arg\,max}_{a\in\mathcal A}
V_{\mathrm C}(a\mid I).
\]

Uncertainty concerns which consequences the action would produce. Suppose eating an apple yields utility \(4\) if it is good and \(-6\) if it is bad, while declining yields \(0\). If the probability that it is good is \(p\), then

\[
V_{\mathrm C}(\text{eat})=4p-6(1-p)=10p-6.
\]

Eating is recommended exactly when \(p>0.6\).

This familiar calculation becomes distinctively causal when the probability of an apple’s being good *conditional on your eating it* differs from its probability under the hypothetical intervention of making yourself eat it.

## 2. Intervention is not observation

Evidential decision theory (EDT) instead evaluates

\[
V_{\mathrm E}(a\mid I)
=\mathbb E[u(O)\mid A=a,I].
\]

Its question is: *How good would the news be that I performed this action?* CDT asks: *How good would the consequences be if I performed it?*

The difference is between

\[
P(O_a=o\mid I)
\quad\text{and}\quad
P(O=o\mid A=a,I).
\]

An action can reveal something about the world without changing that thing.

Consider the reference article’s King David example. David’s fixed personality type affects both his tendency to behave unjustly and the probability of a successful revolt. The stipulated causal structure is

\[
\text{personality}\longrightarrow\text{action},
\qquad
\text{personality}\longrightarrow\text{revolt}.
\]

There is, by hypothesis, no causal arrow from the particular unjust action to revolt.

Learning that David performed the action would provide evidence about his personality and therefore about revolt. Intervening to make him perform it would not change his personality. Consequently, evidential and causal evaluations can disagree.

This does not establish that David should act unjustly. That conclusion additionally requires the action’s overall utility—including its moral costs—to favor it once revolt risk is held fixed. CDT supplies a rule for combining beliefs and values, not a license to disregard wrongdoing.

The two theories agree under suitable independence conditions. In a potential-outcome formulation, assume consistency: when \(A=a\), the observed outcome equals \(O_a\). If also

\[
O_a\perp A\mid I,
\]

then, for actions having positive conditional probability,

\[
P(O=o\mid A=a,I)
=P(O_a=o\mid I).
\]

Randomization often establishes this independence. Mere correlation does not. The reference discusses related results involving additional logical assumptions; none warrants identifying counterfactual probabilities with ordinary conditional probabilities universally.

## 3. Making the counterfactuals operational

The reference identifies an important incompleteness: CDT does not, by itself, provide an algorithm for calculating counterfactual probabilities.

One operational interpretation is a **structural causal model**. This is an additional modeling framework, not something uniquely mandated by the article’s definition.

Let the world be described by equations

\[
X_k=f_k(\operatorname{Pa}_k,E_k),
\]

where \(\operatorname{Pa}_k\) are the direct causal parents of \(X_k\), and the \(E_k\) encode background circumstances. Assume the equations determine an outcome for each relevant intervention.

Ordinarily, the action variable also has an equation, perhaps

\[
A=f_A(\text{beliefs},\text{character},E_A).
\]

To evaluate action \(a\), replace that equation with

\[
A:=a.
\]

Keep the other mechanisms intact and propagate the consequences. The resulting outcome, given background circumstances \(e\), is \(O_a(e)\). Therefore,

\[
V_{\mathrm C}(a\mid I)
=\sum_e P(e\mid I)\,u(O_a(e)).
\]

For continuous variables, replace the sum by an integral.

This is often expressed using intervention notation, \(\operatorname{do}(A=a)\). The counterfactual formulation is particularly useful because it makes the informational order explicit: first update on actual information \(I\), then evaluate each intervention using that posterior.

Three features matter.

**First, causes of the action are not automatically changed along with it.** Forcing the action does not force the hidden personality trait that ordinarily produces it.

**Second, consequences are recomputed.** Holding background circumstances fixed does not mean holding the entire world fixed. Descendants of the action may change substantially.

**Third, genuine evidence remains relevant.** A medical test, observed inclination, or newly discovered fact can update \(P(e\mid I)\). What does not automatically update it is merely supposing an action for purposes of comparison.

Uncertainty about the causal model can also be represented:

\[
V_{\mathrm C}(a\mid I)
=\sum_m P(M=m\mid I)
\sum_e P(e\mid M=m,I)\,
u(O_a^{m}(e)).
\]

Thus CDT need not assume certainty about causation. But it does require a defensible distribution over causal possibilities.

The reference also discusses Lewis’s **imaging**: move probability from each world to a suitably “closest” world where the action occurs. A structural model supplies one concrete rule for this movement—preserve background circumstances, replace the action equation, and follow the remaining mechanisms. It relocates, rather than eliminates, the substantive question: *Which mechanisms should remain fixed?*

## 4. Newcomb’s problem: causal dominance against predictive success

In Newcomb’s problem, a transparent box contains \$1,000. An opaque box contains either \$1,000,000 or nothing. A predictor has already filled the opaque box, rewarding a predicted choice of that box alone and leaving it empty after predicting that both boxes will be taken.

Let \(F\in\{0,10^6\}\) denote the opaque box’s contents. Assuming utility is linear in money,

\[
u(\text{one},F)=F,
\qquad
u(\text{two},F)=F+1000.
\]

Under the usual assumption that the present action does not causally affect the earlier filling,

\[
V_{\mathrm C}(\text{two}\mid I)
-
V_{\mathrm C}(\text{one}\mid I)
=1000.
\]

This holds whatever the current probability that the opaque box is full. Taking both boxes wins in each fixed filling-state.

EDT can recommend otherwise. For illustration, suppose the predictive relationship satisfies

\[
P(F=10^6\mid A=\text{one})=0.99,
\]

\[
P(F=10^6\mid A=\text{two})=0.01.
\]

These conditional assumptions are more specific than merely saying that the predictor has 99% overall accuracy. They yield

\[
V_{\mathrm E}(\text{one})=990{,}000,
\qquad
V_{\mathrm E}(\text{two})=11{,}000.
\]

The disagreement is not arithmetic. It concerns which dependence should enter the comparison.

CDT accepts that choosing one box is excellent evidence of a full opaque box. It denies that changing the present action would thereby change the earlier filling. The predictor may have observed causes of the action, producing a strong correlation without a causal influence running backward from action to prediction.

Two-boxers therefore often receive less money, even though CDT judges two-boxing superior at the moment of choice. Whether this separates rational action from successful decision-making, or exposes a defect in CDT, is precisely the controversy.

## 5. Policies, commitments, and when the choice occurs

A policy specifies actions across possible observations. In a sequential problem, write

\[
A_t=\pi_t(H_t),
\]

where \(H_t\) is the history available at time \(t\). A causal evaluation of policy \(\pi\) replaces the relevant action mechanisms by these policy rules:

\[
V_{\mathrm C}(\pi\mid I)
=
\mathbb E\!\left[
u(O)\mid
\operatorname{do}(A_t:=\pi_t(H_t)\text{ for relevant }t),I
\right].
\]

This is a natural extension of the action-based formulation. Its interpretation must nevertheless be specified: **what is the agent presently able to implement?**

Suppose, before Newcomb’s predictor operates, you can install a binding device that ensures one-boxing. If the device affects what the predictor observes, installing it may causally increase the probability of a full box. CDT can recommend installing it.

At the later moment, however, an uncommitted agent cannot retroactively install that earlier device. Calling the present choice a “policy choice” does not create a causal influence on yesterday.

This distinction explains how CDT can favor advance commitment while favoring a different action when commitment is absent. Planning a future action and being bound to perform it are different causal interventions.

For a fixed decision problem, independent private randomization has value

\[
V_{\mathrm C}(\mu)=\sum_a\mu(a)V_{\mathrm C}(a).
\]

It cannot exceed the best pure action. Randomization can matter strategically when its availability, publicity, or predictability changes others’ behavior; those effects belong in the causal model.

## 6. Self-evidence and the psychopath button

The hardest disputes concern cases where deciding what to do is itself informative.

In the reference article’s “psychopath button” case, Paul values eliminating psychopaths but believes that almost only a psychopath would press the button. Pressing kills psychopaths, including Paul if he is one.

For a simplified numerical model, suppose:

- Paul’s present probability of being a psychopath is \(p\);
- pressing, if he is not one, yields utility \(b>0\);
- pressing, if he is one, yields utility \(-L\);
- not pressing yields utility \(0\).

The fixed-belief causal evaluation is

\[
V_{\mathrm C}(\text{press})=(1-p)b-pL.
\]

It favors pressing when

\[
p<\frac{b}{b+L}.
\]

With \(p=0.001\), \(b=10\), and \(L=1000\), pressing has positive causal expected utility.

Yet if pressing would be overwhelming evidence that Paul is a psychopath, this recommendation seems alarming. These numbers represent his beliefs *before* treating his own emerging decision as evidence. Whether those beliefs should remain unchanged through deliberation is the contested issue.

The reference reports Egan’s criticism of holding fixed unconditional credences in causal dependency hypotheses, and Joyce’s response that CDT can use information about one’s inclinations as evidence.

A reasonable operational distinction is:

- An **observed inclination** is information and may update beliefs.
- A **hypothetical intervention** considered during comparison is not, merely as such, an observation.

Thus discovering “I strongly want to press” may change \(p\), after which Paul should recompute both action values. But evaluating “suppose I press” need not do so.

This distinction preserves the separation between evidence and intervention. It does not settle every case. A full theory must explain what deliberation reveals, when belief updates occur, and whether the eventual recommendation remains stable after those updates.

## 7. Prediction-based exploitation

The reference’s adversarial offer sharpens the concern. Two boxes each cost \$1. Yesterday, a seller placed \$3 in every box she predicted the buyer would *not* acquire. The buyer may acquire one box or neither. Prediction accuracy is stipulated to be \(0.75\).

At least one box contains \$3. Consequently,

\[
\mathbb E[C_1\mid I]+\mathbb E[C_2\mid I]\ge 3.
\]

Holding those already determined contents causally fixed, at least one purchase has expected net value at least

\[
\frac{3}{2}-1=0.50.
\]

A straightforward CDT evaluation therefore favors buying some box.

But an accurately predicted purchase selects an empty box. If the stipulated accuracy applies to the resulting purchase, the buyer’s expected realized profit is

\[
0.75(-1)+0.25(3-1)=-0.25.
\]

The example exposes a tension between favorable intervention-based valuations and unfavorable outcomes when the selected action is prediction-linked to the world’s state.

It is not resolved simply by saying “correlation is not causation”: the critic already grants the absence of causal influence on yesterday’s filling. The complaint concerns whether rational deliberation should ignore the evidential significance of its own conclusion. Defenders can contest the treatment of deliberation, information, or available commitments, but the required answer must address those details.

## 8. Applying CDT to an unfamiliar problem

A disciplined application should proceed as follows:

1. **Specify the present choice.** Is it an immediate act, a commitment, or an implementable policy?
2. **Specify utilities completely.** Include costs, risk preferences, ethical concerns, and effects on others.
3. **Separate evidence from intervention.** What information is actually available, and what is merely being supposed?
4. **Model the causal dependencies.** Which variables generate the action, which respond to it, and which merely correlate with it?
5. **Construct each counterfactual.** Change the action mechanism, preserve the justified background assumptions, and propagate consequences.
6. **Average and compare.** Use the posterior distribution appropriate to the actual information.
7. **Check deliberative stability.** Would adopting the recommendation reveal information that materially changes the calculation?

The final check identifies an open issue rather than a universally agreed extra axiom of CDT.

## Conclusion

CDT’s distinctive claim is not simply “maximize expected utility.” It is that alternatives should be evaluated using probabilities of their causal consequences, not probabilities obtained by treating their occurrence as news.

With explicit causal models and well-defined interventions, that instruction becomes mathematically precise. Its difficult boundary lies in prediction, commitment, and self-knowledge: choosing an action may reveal facts that hypothetically forcing it would not. Understanding CDT requires keeping those operations separate—and recognizing where a theory of deliberation is still needed.

### References

- Wikipedia contributors, “[Causal decision theory](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528),” supplied revision; CC BY-SA 4.0.
- Gibbard, A., and Harper, W. L. (1981). “Counterfactuals and two kinds of expected utility.”
- Lewis, D. (1981). “Causal decision theory.”
- Egan, A. (2007). “Some counterexamples to causal decision theory.”
- Joyce, J. M. (2012). “Regret and instability in causal decision theory.”
- Oesterheld, C., and Conitzer, V. (2021). “Extracting Money from Causal Decision Theorists.”