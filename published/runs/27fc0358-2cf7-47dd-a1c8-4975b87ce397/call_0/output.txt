# Causal decision theory: acting on the world, not merely learning about it

A decision can be informative without being effective. A person’s choice to carry an umbrella may indicate that rain is likely, but carrying it does not thereby cause rain. Conversely, an action can have a favorable causal effect even when people who usually perform it tend to fare badly: a treatment may help patients despite being associated with poor outcomes because it is normally given to the sickest patients.

Causal decision theory (CDT) makes this distinction central to rational choice. Its guiding recommendation is to choose the available action with the best *expected causal consequences*. Evidential decision theory (EDT), by contrast, evaluates an action partly by asking what taking it would indicate about the world. The two theories often agree, but they can disagree sharply when an action is correlated with circumstances it cannot change.

This distinction sounds simple; applying it is not. One must say what would happen under each alternative, what information the agent should use, and which features of the world remain fixed when an action is varied. The reference article presents CDT as a family of approaches rather than a single algorithm. The structural models developed below are an operational interpretation of its central idea, not machinery uniquely specified by the article.

## 1. Expected causal utility

Suppose an agent must choose an action \(a\) from a set \(\mathcal A\). Let \(Y_a\) denote the outcome that would obtain if the agent performed \(a\), and let \(u(a,Y_a)\) be its utility. Given the agent’s current information \(I\), a natural statement of CDT is

\[
V_C(a\mid I)
=
\mathbb E\!\left[u(a,Y_a)\mid I\right],
\qquad
a^*\in\operatorname*{arg\,max}_{a\in\mathcal A}V_C(a\mid I).
\]

The variable \(Y_a\) is a *counterfactual* or potential outcome. It need not be the outcome actually observed: if the agent eats an apple, the outcome of eating an orange is still relevant to the comparison, even though it is not observed.

For a finite set of outcomes \(o_1,\ldots,o_n\), this becomes

\[
V_C(a\mid I)
=
\sum_{j=1}^{n}
P(Y_a=o_j\mid I)\,u(a,o_j).
\]

The reference article gives a closely related formulation attributed to Gibbard and Harper:

\[
U(A)=\sum_j P(A\mathbin{\to} O_j)D(O_j),
\]

where \(A\to O_j\) is the counterfactual “if \(A\) were performed, \(O_j\) would result.” It is better to read this as a claim about the outcome *under the counterfactual action* than as saying that \(A\) logically or necessarily implies \(O_j\). The agent may be uncertain about which counterfactual is true.

For example, suppose an apple is good with probability \(0.8\). Eating it yields utility \(10\) if good and \(-8\) if bad. Then

\[
V_C(\text{apple})=0.8(10)+0.2(-8)=6.4.
\]

If an orange gives utility \(5\) for certain, CDT recommends the apple. The recommendation depends on both the probabilities and the utilities: “best consequences” means best *in expectation*, not best in every possible state.

Utility may represent money, health, obligations, other people’s welfare, or whatever the agent’s evaluative commitments require. CDT by itself does not say that money is the only relevant outcome, nor that a benefit to oneself justifies harm to others. Its distinctive contribution is how it relates alternatives to their consequences.

## 2. Why conditioning is different

EDT evaluates the same action using the ordinary conditional distribution of outcomes among cases in which the action occurs:

\[
V_E(a\mid I)
=
\mathbb E\!\left[u(a,Y)\mid A=a,I\right],
\]

where \(A\) and \(Y\) are the actual action and actual outcome. Roughly, EDT asks, “What would the news that I took \(a\) tell me?” CDT asks, “What would result if I took \(a\)?”

These questions can have different answers because \(A=a\) may be evidence about a cause of both the action and the outcome. Consider a numerical version of the reference article’s King David example. Let \(C\) mean that a king is charismatic. Suppose

\[
P(C)=\tfrac12,\quad
P(A=\text{summon}\mid C)=0.1,\quad
P(A=\text{summon}\mid \neg C)=0.9.
\]

Suppose also that revolt occurs with probability \(0.1\) for a charismatic king and \(0.9\) for an uncharismatic king, and that summoning itself has no effect on revolt. Bayes’ rule gives

\[
P(C\mid \text{summon})=0.1,
\qquad
P(C\mid \text{abstain})=0.9.
\]

Consequently, under these assumptions,

\[
P(\text{revolt}\mid \text{summon})=0.82,\qquad
P(\text{revolt}\mid \text{abstain})=0.18.
\]

Summoning is bad *news* about charisma and hence revolt. But if charisma is already fixed and the action does not affect revolt, the causal probability of revolt is \(0.5\) under either action. If, additionally, David values summoning and assigns no relevant disutility to its injustice, CDT recommends summoning, while EDT may recommend abstaining if the evidential difference in revolt risk is sufficiently costly.

That last qualification matters. The example isolates a disagreement about inference; it does not establish that an actual unjust action should be performed. Once moral harms are included in utility, the causal recommendation may change.

In general, even when the observed outcome equals \(Y_A\), it does not follow that

\[
P(Y_a=o\mid I)=P(Y=o\mid A=a,I).
\]

Equality does hold under suitable conditions—for example, when, conditional on \(I\), action assignment is independent of the potential outcome \(Y_a\), and the observed outcome agrees with \(Y_a\) for those who take \(a\). A genuinely randomized action with no relevant interference is a standard setting in which this can be reasonable. The reference article notes a related result from Gibbard and Harper: under specified conditional-logic assumptions, independence of an action and its associated counterfactual suffices for the counterfactual probability to equal the ordinary conditional probability.

Lewis’s work on probabilities of conditionals supplies a broader warning: one cannot generally identify the probability of a counterfactual conditional with an ordinary conditional probability. The issue is not that conditioning is invalid; it is that conditioning answers a different question.

## 3. Building counterfactuals with a causal model

How should an agent calculate \(P(Y_a=o\mid I)\)? The reference article explicitly leaves this open. One useful proposal is to represent the world by a structural causal model.

Let variables \(X_1,\ldots,X_m\), including action \(A\) and outcome \(Y\), satisfy equations

\[
X_i=f_i(\operatorname{Pa}_i,U_i),
\]

where \(\operatorname{Pa}_i\) are the modeled direct causes of \(X_i\), and the \(U_i\) collect background factors. A probability distribution over the background factors represents uncertainty. The equations specify how downstream variables respond when their inputs change.

To evaluate \(a\), replace the equation for \(A\) with \(A=a\), leaving the other equations intact. This intervention is written \(\operatorname{do}(A=a)\). In an appropriate model,

\[
V_C(a\mid I)
=
\mathbb E\!\left[u(a,Y)\mid
\operatorname{do}(A=a),I\right].
\]

This notation needs care when \(I\) includes information about the actual world. A safe operational procedure is:

1. **Update:** use current evidence \(I\) to form a posterior over background factors and, if necessary, over competing causal models.
2. **Intervene:** in each model, replace the action equation by \(A=a\).
3. **Propagate:** calculate the resulting outcome while preserving the relevant background factors and other structural equations.
4. **Average:** take expected utility over the posterior uncertainty.
5. **Compare:** repeat for each feasible alternative.

If the evidence includes observations that are descendants of the action, simply conditioning on them in an intervened distribution may not implement this procedure. For a personal counterfactual—“given what I have actually observed, what would happen if I acted differently?”—the posterior over the actual background factors must first be inferred. The model then carries those factors into the alternative scenario.

In David’s case, the causal picture contains arrows

\[
C\longrightarrow A,\qquad C\longrightarrow Y,
\]

but, by stipulation, no arrow from \(A\) to revolt \(Y\). Intervening on \(A\) removes the influence of charisma on the action; it does not remove charisma’s influence on revolt. Nor does it erase uncertainty about charisma. Thus the intervention preserves the common cause while breaking the evidential association generated by the action-selection equation.

This is not a rule to hold *everything except the action* fixed. If summoning caused a scandal and the scandal caused revolt, both scandal and revolt should be allowed to respond. The crucial distinction is between variables causally downstream of the intervention and background features the intervention does not change. Choosing that boundary is a substantive modeling judgment.

If the causal structure is uncertain, include that uncertainty. Let \(M\) index models and \(U\) their background factors. Then an operational version of CDT is

\[
V_C(a\mid I)
=
\sum_M\int
u\!\left(a,Y_a(M,u)\right)
\,P(d u,M\mid I).
\]

A possible causal effect should not be discarded merely because another model denies it. Conversely, an observed correlation should not be treated as an effect without support for the relevant causal pathway.

## 4. Newcomb’s problem and fixed past predictions

Newcomb’s problem puts pressure on the causal/evidential distinction. There is a transparent box containing \$1,000 and an opaque box containing either \$1 million or nothing. Earlier, a highly reliable predictor filled the opaque box if it predicted that the player would take only that box, and left it empty if it predicted that the player would take both.

Let \(B\in\{0,1\}\) indicate whether the opaque box is full. At the moment of choice, suppose the box’s content is already fixed and the present choice cannot affect it. Taking both yields

\[
Y_{\text{both}}=1{,}000+1{,}000{,}000B,
\]

whereas taking only the opaque box yields

\[
Y_{\text{one}}=1{,}000{,}000B.
\]

For either value of \(B\), taking both gives \$1,000 more. With utility linear in these payoffs, and indeed with any strictly increasing utility of money under these simple outcomes, causal dominance recommends taking both.

EDT may recommend one box because the choice is strong evidence about what the predictor predicted. For an illustrative calculation, suppose

\[
P(B=1\mid A=\text{one})=0.99,\qquad
P(B=1\mid A=\text{both})=0.01.
\]

Then the evidential expected payoffs are \$990,000 for one box and \$11,000 for both. An overall prediction accuracy of 99% alone does not guarantee these two particular conditional probabilities; they are additional assumptions about how the errors and choices are distributed.

The reference article says that two-boxing “results in” only \$1,000. That is a typical result for a successfully predicted two-boxer, not a logical consequence of two-boxing: if the predictor was wrong, the two-boxer receives \$1,001,000. The dispute is precisely whether the action’s correlation with the earlier prediction should influence its evaluation in the way EDT proposes.

The CDT argument also has a boundary. If the player acts *before* the predictor observes a commitment or if the predictor can causally respond to an earlier policy choice, that earlier choice may affect the box. It would be a different intervention at a different time.

## 5. Actions, policies, and commitment

Many practical decisions concern a policy rather than a single immediate act. A policy \(\pi\) maps observations \(h\) available later into actions: \(A=\pi(h)\). One can evaluate it causally by replacing the relevant decision rule in a model and computing

\[
V_C(\pi\mid I)
=
\mathbb E\!\left[u(Y_\pi)\mid I\right].
\]

Here \(Y_\pi\) includes the consequences of future observations, actions, and responses to those actions. If a genuine commitment device can install \(\pi\), its costs and causal effects belong in the model. The device may also change what other agents see or predict.

This can generate a difference between what is desirable *now* and what a later agent will prefer without commitment. Before a predictor fills the box, making an observable and binding commitment to one-box may causally lead to a full box. After the box is filled, an unbound agent faces the \$1,000 causal advantage of taking both. There is no contradiction: the interventions act on different variables at different times. Whether an early commitment actually affects a predictor depends on the mechanism; merely declaring a policy after the prediction does not alter the past.

The same caution applies to opponents. In a prisoner’s dilemma, defection may give a better payoff against either fixed choice of the other player. If the opponent’s choice is causally independent of one’s present act, standard CDT therefore defects. But if an earlier commitment can be observed and changes the opponent’s response, cooperation as a committed policy may have better causal value. A merely similar or “twin” opponent introduces a harder case: correlated decisions may be highly predictive of each other without either present act causing the other.

## 6. The cost of ignoring predictive correlations

The reference article collects objections that challenge whether the ordinary causal criterion always gives a plausible recommendation.

Consider the **adversarial offer**. A buyer may purchase one of two boxes for \$1, or buy neither. Earlier, the seller placed \$3 in each box she predicted the buyer would not acquire. Thus at least one box contains \$3. If \(p_L,p_R\) are the buyer’s current probabilities that the left and right boxes contain money, then

\[
p_L+p_R\geq 1.
\]

At least one box consequently has \(p_i\geq \tfrac12\), and its causal expected net value is

\[
3p_i-1\geq \$0.50.
\]

On the ordinary one-shot calculation, buying a maximally promising box beats buying nothing. Yet if the seller predicts the purchased box correctly with probability \(0.75\), the buyer’s actual average net payoff from a purchase is

\[
0.75(-1)+0.25(2)=-\$0.25.
\]

The apparent tension is not an arithmetic error. The causal calculation holds the previously filled boxes fixed while varying the purchase; the realized conditional distribution of contents given the eventual purchase can reflect the seller’s prediction. The \(0.75\) accuracy assumption must apply to the actual purchase behavior under discussion, including any randomization, rather than merely to some other population or strategy.

The example also raises a question about *which beliefs are stable at the point of choice*. In a symmetric setup, the causal calculation may favor buying either box; but a buyer who becomes confident of buying left might treat that inclination as evidence that the seller predicted left. Updating on such evidence can change \(p_L\) and \(p_R\), potentially changing the preferred action again. The reference article notes Joyce’s view that CDT can use information about one’s inclinations as evidence. It also reports Egan’s criticism that fixing initial credences in causal dependencies can lead to implausible or unstable recommendations. How to model deliberation and find a stable recommendation is a live issue, not something settled by the basic expected-value formula.

A related example is Egan’s **psychopath button**. Paul would prefer a world without psychopaths, but believes that only a psychopath would press a button killing them; he strongly prefers life among psychopaths to his own death. Pressing may be evidence that Paul is a psychopath. It also causally kills him if he is one. A simple causal calculation uses his present probability \(p\) of being a psychopath in both action comparisons. If the benefit of pressing when he is not a psychopath is \(b\), and the cost of death is \(d\), pressing is favored when

\[
(1-p)b-pd>0,
\]

assuming abstention has utility zero and omitting other costs. For sufficiently small \(p\), this can recommend pressing, even though discovering a genuine inclination to press might itself increase \(p\). The example exposes a question about when and how self-locating evidence enters deliberation. It does not show that CDT must ignore such evidence altogether.

## 7. What the formalism leaves open

Structural models make CDT calculable, but they do not eliminate philosophical choices.

First, a causal graph or set of equations must be justified. Observational data alone may not identify whether a correlation reflects causation, confounding, or selection. Experiments, background science, and sensitivity analysis can support a model, but a decision rule cannot manufacture missing causal knowledge.

Second, the counterfactual intervention itself may be ambiguous. “Choose differently” could mean a last-moment bodily movement, a change in a decision rule, or an earlier commitment. These can have different effects on predictors and observers. A useful practice is to state the intervention in ordinary language before writing \(\operatorname{do}(\cdot)\).

Third, some counterfactuals may lack a clear structural representation. The reference article describes Lewis’s **imaging** proposal: move probability mass from each possible world to a closest world where the action occurs. But “closest” requires a similarity standard, and the article reports a worry that specifying the appropriate beliefs about the supposed action may lead to regress. Imaging is an alternative account of counterfactual probabilities, not an automatic solution.

Finally, CDT is a family of views about causal evaluation. Variants differ over deliberation, mixed strategies, ratifiability, and the treatment of information about one’s own impending decision. Dutch-book and money-extraction arguments cited in the reference article press the concern that a sequence of locally causal choices can yield a predictably bad overall result. A defender may respond by examining commitments, information updates, and the exact sequence of offers; the force of such a response depends on the case.

## Conclusion

CDT recommends maximizing expected utility under alternatives understood as interventions: preserve what the action cannot change, propagate what it can change, and average over uncertainty. Its appeal is that evidence of a good outcome is not the same thing as producing one. Its hardest cases arise when an agent’s decision is itself powerful evidence about a predictor, an opponent, or the agent’s own type. Applying CDT well therefore requires more than a formula: it requires an explicit causal model, a carefully specified decision point, and attention to what the agent has learned while deciding.

**References**

- Wikipedia contributors, “[Causal decision theory](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528),” revision 1381555528; licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- Gibbard, A., and Harper, W. L. (1981), “Counterfactuals and two kinds of expected utility.”
- Lewis, D. (1981), “Causal decision theory,” *Australasian Journal of Philosophy* 59, 5–30.
- Egan, A. (2007), “Some counterexamples to causal decision theory,” *The Philosophical Review* 116, 93–114.
- Oesterheld, C., and Conitzer, V. (2021), “Extracting money from causal decision theorists,” *The Philosophical Quarterly* 71.