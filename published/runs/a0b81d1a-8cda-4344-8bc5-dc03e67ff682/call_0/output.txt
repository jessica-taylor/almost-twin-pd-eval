# Causal Decision Theory: Choosing What Causes Good Outcomes

Causal decision theory (CDT) is a school of thought in decision theory that says, roughly: choose the action that you expect will causally bring about the best outcome. The reference article states this contrast sharply: CDT recommends the action with the best expected *causal consequences*, whereas evidential decision theory (EDT) recommends the action that would be the best *news* if you learned that you had taken it. If eating an apple causes happiness and eating an orange causes sadness, CDT says eat the apple. If the apple might be good or bad, CDT says compare the expected causal effects, weighting the possible good and bad consequences by their probabilities.

The interesting cases arise when an action is evidence about the world but does not causally change the relevant facts. Should a king send for Bathsheba if doing so would indicate that he is uncharismatic, even though his charisma cannot be changed? Should a player take both boxes in Newcomb’s problem if taking both is strong evidence that the opaque box is empty, even though the box was filled yesterday? CDT’s answer is that rational choice should track causal influence, not merely evidential connection.

This essay gives a formal account of CDT, explains how it evaluates actions and policies, and discusses how it treats dependencies and counterfactuals. The reference article leaves the computation of counterfactual probabilities under-specified, so I also develop an operational interpretation using causal models. Where I go beyond the source, I will say so.

---

## 1. Expected utility: evidential versus causal

Let \(A\) be a finite set of possible actions, and let \(O_1,\dots,O_n\) be a partition of possible outcomes. Let \(D(O_j)\) be the desirability, or utility, of outcome \(O_j\).

Evidential decision theory evaluates an action \(a\) by conditional expected utility:

\[
U_E(a)=\sum_j P(O_j \mid a)\,D(O_j).
\]

Here \(P(O_j \mid a)\) is the ordinary conditional probability of \(O_j\) given that the agent performs \(a\). EDT asks: if I learned as news that I had done \(a\), how good would the world likely be?

CDT instead evaluates an action by its expected causal consequences. In the formulation attributed in the source to Gibbard and Harper (1981),

\[
U_C(a)=\sum_j P(a \,\Box\!\rightarrow\, O_j)\,D(O_j),
\]

where \(P(a \,\Box\!\rightarrow\, O_j)\) is the probability of the counterfactual: if \(a\) were performed, \(O_j\) would obtain. The arrow is not material implication. It is a counterfactual conditional, or, in modern causal language, an interventionist probability. We can often write it as

\[
P(a \,\Box\!\rightarrow\, O_j) \approx P(O_j \mid do(a)),
\]

where \(do(a)\) means “intervene to make \(a\) happen,” rather than merely “condition on observing \(a\).”

Thus a compact modern rendering of CDT is:

\[
U_C(a)=\sum_j P(O_j \mid do(a))\,D(O_j).
\]

The difference between \(P(O_j \mid a)\) and \(P(O_j \mid do(a))\) is the central issue.

---

## 2. Expected causal effects under uncertainty

The source’s informal apple example illustrates the basic computation. Suppose eating an apple may make you happy if the apple is good, or sad if it is bad. Let

- \(G\): the apple is good, with prior probability \(p\);
- \(B\): the apple is bad, with probability \(1-p\);
- \(D(\text{happy})=h>0\);
- \(D(\text{sad})=-s<0\).

If eating the apple causally produces happiness when good and sadness when bad, then

\[
U_C(\text{eat apple})=p h +(1-p)(-s).
\]

If eating an orange has utility \(0\), CDT says eat the apple exactly when

\[
p h -(1-p)s > 0.
\]

In this simple case, EDT and CDT agree, because your choice is not evidence about whether the apple is good or bad. The two theories diverge when the action is correlated with some relevant background fact that it does not cause.

---

## 3. Dependency hypotheses and causal structure

Real decision problems often involve uncertainty about how the world works. The source mentions “dependency hypotheses” implicitly through Egan’s criticism: CDT is said to hold fixed the agent’s unconditional credences in dependency hypotheses. We can make this explicit.

Let \(K_1,\dots,K_m\) be possible causal structures, or dependency hypotheses. Each \(K_k\) specifies how actions causally affect outcomes. Then a general CDT evaluation is:

\[
U_C(a)=\sum_k P(K_k)\sum_j P(O_j \mid do(a), K_k)\,D(O_j).
\]

Here \(P(K_k)\) is the agent’s prior credence in causal hypothesis \(K_k\). The inner sum is the expected utility of \(a\) conditional on \(K_k\), evaluated using interventionist probabilities.

Compare EDT:

\[
U_E(a)=\sum_k P(K_k \mid a)\sum_j P(O_j \mid a, K_k)\,D(O_j).
\]

EDT allows the action to change the probabilities of dependency hypotheses through conditioning: \(P(K_k \mid a)\) may differ from \(P(K_k)\). CDT, in its standard form, does not let the mere evidential bearing of an action on a dependency hypothesis change the causal evaluation. This is what Egan criticizes when he says CDT “holds fixed” the agent’s initial views about the likely causal structure.

This distinction is not merely technical. In cases involving predictors, twins, or self-knowledge, the action can be strong evidence about what kind of agent one is or what the world is like. EDT uses that evidence; CDT asks whether the action itself causally changes the outcome.

---

## 4. Counterfactuals and interventions

The source correctly notes that CDT does not itself specify an algorithm for computing counterfactual probabilities. Gibbard and Harper give the formal schema, but the content of \(P(a \,\Box\!\rightarrow\, O_j)\) needs a semantics.

The source mentions David Lewis’s “imaging” proposal: to evaluate \(P(a \,\Box\!\rightarrow\, O_j)\), move probability mass from each possible world \(w\) to the closest possible world \(w_a\) in which \(a\) holds, then see whether \(O_j\) holds there. Imaging captures the idea that counterfactual reasoning considers the nearest worlds where the action is performed. But the source also notes a regress problem: to know what one would believe if certain of \(a\), one may need further conditional beliefs, and so on.

A natural operational interpretation, not stated in the source but widely used in contemporary causal inference, is to use a structural causal model. This is my proposed way of making CDT precise enough for application.

A structural causal model contains variables, such as action \(A\), background conditions \(C\), and outcome \(O\), together with equations describing how variables depend on their causes. For example,

\[
A = f_A(C,U_A),
\]
\[
O = f_O(A,C,U_O),
\]

where \(U_A,U_O\) are exogenous noise variables.

To intervene and set \(A=a\), we replace the equation for \(A\) with

\[
A := a.
\]

The resulting modified model gives a distribution over outcomes. We define

\[
P(O_j \mid do(a)) = \Pr_{U}\bigl(O_j \text{ occurs in the modified model with } A:=a\bigr).
\]

This gives an operational meaning to the Gibbard-Harper counterfactual probability:

\[
P(a \,\Box\!\rightarrow\, O_j) \equiv P(O_j \mid do(a)).
\]

If the agent is uncertain among several causal models \(M_1,\dots,M_m\), we average:

\[
P(a \,\Box\!\rightarrow\, O_j)=\sum_r P(M_r)P_{M_r}(O_j \mid do(a)).
\]

This proposal makes CDT usable in concrete problems, provided one has a causal model or at least defensible assumptions about causal structure. It also clarifies the distinction between conditioning and intervening. Conditioning on \(A=a\) preserves all normal evidential associations. Intervening on \(A=a\) breaks the usual causal arrows into \(A\), while preserving the downstream causal consequences of \(A\).

---

## 5. Policies, not just one-off actions

The reference article mostly discusses single actions, but decision theory often evaluates policies. A policy \(\pi\) is a rule mapping information available at decision time to actions. For example, a policy might say: “if the traffic light is red, stop; if green, go.”

CDT can evaluate a policy by treating the implementation of the policy as an intervention. If \(\pi\) determines actions \(A_t\) at various times as functions of available information \(H_t\), then \(do(\pi)\) means replacing the relevant decision equations with

\[
A_t := \pi_t(H_t).
\]

The causal expected utility of a policy is then

\[
U_C(\pi)=\sum_k P(K_k)\sum_j P(O_j \mid do(\pi), K_k)\,D(O_j).
\]

This is my operational extension of the basic CDT formula. It says: evaluate the expected outcome of causally implementing the policy, not merely the expected outcome conditional on observing that the policy is being followed.

This distinction matters. A policy may be correlated with favorable outcomes without causing them. For instance, a cautious driving policy may be correlated with being a careful person, but the causal question is what happens if we intervene to make the driver follow that policy. Similarly, in sequential problems, an agent may want to evaluate precommitment to a policy rather than re-optimizing at every moment. CDT can evaluate precommitment as an intervention on a disposition or policy variable, but the reference article does not settle the details. This is one of the areas where CDT needs additional machinery.

---

## 6. Why counterfactual probabilities are not conditional probabilities

The source notes that Lewis proved the probability of a conditional does not generally equal the corresponding conditional probability. In the present context, this means that

\[
P(a \,\Box\!\rightarrow\, O_j)
\]

need not equal

\[
P(O_j \mid a).
\]

If they always were equal, CDT would collapse into EDT. Lewis’s triviality result shows that, under broad assumptions, probabilities of conditionals cannot simply be identified with conditional probabilities except in trivial cases.

Gibbard and Harper showed that under certain axioms, one related to the controversial principle of conditional excluded middle, statistical independence between the action and the relevant counterfactual can make the two quantities coincide. Informally: if performing \(a\) gives you no evidence about whether the counterfactual “if \(a\) were performed, \(O_j\) would happen” is true, then the counterfactual probability may match the conditional probability. But many philosophically interesting cases violate this independence.

A helpful way to see this is through causal graphs. If \(A\) and \(O\) share a common cause \(C\), then observing \(A\) gives information about \(C\), and thereby about \(O\). But intervening on \(A\) does not change \(C\). Thus

\[
P(O \mid A) \neq P(O \mid do(A))
\]

in general. CDT uses the latter; EDT uses the former.

---

## 7. King David and the value of bad news

The reference article gives Gibbard and Harper’s example of King David. David wants Bathsheba but fears that summoning her would provoke revolt. He knows that kings are either charismatic or uncharismatic, and that charisma is fixed in adulthood. Charismatic kings tend to act justly and rarely face successful revolts; uncharismatic kings act unjustly and often face revolts. But unjust acts themselves do not cause revolts; the revolts are caused by the king’s ignoble bearing.

Let

- \(C\): David is charismatic;
- \(\neg C\): David is uncharismatic;
- \(S\): David summons Bathsheba;
- \(R\): successful revolt.

The causal structure is:

\[
C \rightarrow \text{behavior}, \quad C \rightarrow R,
\]
\[
S \rightarrow \text{pleasure/injustice},
\]

but, by assumption,

\[
S \not\rightarrow R.
\]

EDT may recommend abstaining because

\[
P(R \mid S)
\]

is high: summoning Bathsheba is evidence that David is uncharismatic, and uncharismatic kings face revolts. But CDT asks whether summoning her causally affects revolt. Given David’s type, it does not. So the causal expected utility of summoning includes whatever benefit David receives, without increasing the probability of revolt. The source says CDT recommends sending for her, assuming the relevant benefits dominate any moral disutility.

The example illustrates CDT’s core idea: it is irrational to refrain from an action merely because it would be bad news. If the action does not cause the bad outcome, CDT does not count the bad news against it.

---

## 8. Newcomb’s problem

Newcomb’s problem is the most famous test case. The source describes it as follows. A predictor, reliable say 99% of the time, predicts whether the player will take both boxes or only one. Box A always contains \$1,000. Box B contains \$1,000,000 if the predictor predicted one-boxing, and nothing if the predictor predicted two-boxing. The player chooses after the predictor has already acted.

Let

- \(T\): take both boxes;
- \(O\): take only box B;
- \(X\): amount in box B, either \$0 or \$1,000,000.

The payoffs are:

\[
\text{Payoff}(O)=X,
\]
\[
\text{Payoff}(T)=X+1000.
\]

CDT reasons that at the moment of choice, the predictor’s prediction is already fixed. Therefore the player’s current action does not causally affect \(X\). Under an intervention,

\[
P(X \mid do(T)) = P(X \mid do(O)),
\]

or, more precisely, whatever value \(X\) has, two-boxing yields \$1,000 more than one-boxing. Hence

\[
U_C(T)=U_C(O)+1000,
\]

so CDT recommends taking both boxes.

EDT reasons differently. Since the predictor is highly accurate,

\[
P(X=1{,}000{,}000 \mid O)
\]

is high, while

\[
P(X=1{,}000{,}000 \mid T)
\]

is low. With 99% accuracy, EDT approximately gives:

\[
U_E(O)\approx 0.99 \times 1{,}000{,}000 = 990{,}000,
\]

whereas

\[
U_E(T)\approx 0.01 \times 1{,}000{,}000 + 1000 = 11{,}000.
\]

So EDT recommends one-boxing.

The source notes that philosophers disagree about whether one-boxing or two-boxing is rational, but that CDT’s recommendation is two-boxing. The reason is not that CDT ignores prediction. Rather, CDT treats the prediction as already causally fixed. Your present choice may be evidence about the prediction, but it does not cause the prediction.

---

## 9. Criticisms and counterexamples

The reference article lists several criticisms. The most important are vagueness and alleged counterexamples.

### Vagueness

CDT says to maximize expected utility computed from counterfactual probabilities, but it does not by itself say how to compute those probabilities. Lewis’s imaging is one proposal, but the source notes a regress: to evaluate what one would believe if certain of \(A\), one may need further counterfactual beliefs. This is a serious philosophical difficulty.

The structural-causal-model interpretation above is one way to reduce the vagueness. Given a causal graph and structural equations, \(P(O \mid do(A))\) is well-defined. But this moves the difficulty into specifying the correct causal model. CDT does not magically reveal which variables are causes, which are evidential correlates, or what the right counterfactual semantics is.

### Newcomb-style predictors

Newcomb’s problem is also listed as a counterexample by critics. Because your choice cannot causally affect the predictor’s earlier guess, CDT recommends two-boxing. But two-boxing typically yields only \$1,000, while one-boxing yields \$1,000,000. Critics ask: why should a rational theory recommend leaving a million dollars on the table?

A CDT defender may respond that the million dollars was already unavailable by the time the agent chooses. The agent can only choose between \$1,000 and \$1,000,000 plus \$1,000, given the actual contents of the boxes. But the disagreement reflects a deeper issue about how counterfactuals should treat predictors, dispositions, and the agent’s own decision procedure.

### Death in Damascus

The source mentions the “Death in Damascus” scenario. Death predicts where you will be tomorrow and waits there. If Death is a reliable predictor, then choosing to flee to Aleppo may be strong evidence that Death predicted Aleppo, or Damascus, depending on the details. CDT may struggle to process the correlation between the agent’s choice and Death’s prediction, because the choice does not causally affect the earlier prediction.

The source says CDT may make irrational decisions in such cases. The deeper issue is that CDT can be unstable when the agent’s choice is predictable and the predictor’s action depends on that prediction. If every available action is evidence that the predictor has arranged a bad outcome, EDT may treat all options differently from CDT. Some variants are designed to show that CDT voluntarily loses money or forgoes guaranteed payoffs.

### The Adversarial Offer

The source describes the Adversarial Offer, due to Oesterheld and Conitzer. Two boxes are on sale. Each costs \$1. The buyer may buy one box or none, but not both. Yesterday, the seller put \$3 in each box that she predicted the buyer would not acquire. Both sides believe the seller’s prediction is accurate with probability \(0.75\).

From the buyer’s perspective, if they will buy at most one box, then at least one box will not be acquired. If the seller is accurate, at least one box likely contains \$3. The source says CDT reasons that the average box contains at least \$1.50 in causal expected value, which exceeds the \$1 cost. Hence CDT requires buying a box. But this is profitable for the seller.

The problem is that the buyer’s choice may be evidence about which box the seller predicted they would acquire. If I choose box 1, that may be evidence that the seller predicted I would acquire box 1, so box 1 is likely empty. EDT would condition on the choice and might avoid buying. CDT, focusing on the causal effect of buying a box while holding fixed the seller’s prior prediction, may fail to recognize the exploitable correlation.

This example is important because it suggests that CDT can be dynamically vulnerable: a seller can design offers that make CDT agents pay for predictably empty boxes.

### The Psychopath Button

The source gives Egan’s Psychopath Button. Paul is considering pressing a button that would kill all psychopaths. Paul thinks a world without psychopaths would be much better. But he is confident that only a psychopath would press such a button. Paul strongly prefers living in a world with psychopaths to dying.

Let

- \(P\): Paul is a psychopath;
- \(B\): Paul presses the button.

If Paul is not a psychopath and presses, the outcome may be a world without psychopaths and Paul alive, which is best. If Paul is a psychopath and presses, he dies, which is worst. If he does not press, he lives in a world with psychopaths, intermediate.

EDT says: pressing the button is strong evidence that Paul is a psychopath, so do not press. Simple CDT may instead hold fixed Paul’s type and ask what pressing would cause given each type. If Paul’s prior probability of being a psychopath is low enough, or if the causal benefit of a psychopath-free world is large enough, CDT may endorse pressing. The source says Egan claims CDT endorses pressing, while “pretty much everyone” agrees Paul should not.

This example highlights the tension in CDT’s treatment of self-knowledge. Paul’s inclination to press is evidence about his own nature. A sophisticated CDT may be able to incorporate evidence about one’s inclinations, as Joyce argues. But the reference article leaves unresolved exactly how CDT should handle such reflexive evidence. My own view is that a fully specified causal model should include Paul’s decision procedure or psychological type as a variable, and should evaluate pressing as an intervention on that model. Still, if the act of forming the intention to press is itself evidence of type, CDT may need additional principles, such as ratifiability, to avoid counterintuitive verdicts. That move goes beyond the source.

---

## 10. What CDT gets right, and where it remains unsettled

CDT captures an important normative intuition: one should not choose an action merely because it would be good evidence. Making yourself sick to get good news is irrational; choosing a medical treatment because it causes recovery is rational. CDT formalizes this by replacing conditional probabilities with counterfactual or interventionist probabilities.

The theory is most compelling when the causal structure is clear. If an action has a direct causal effect on outcomes, and the action is not confounded with hidden causes, CDT gives ordinary expected-utility advice. If a randomized experiment tells us that a treatment works, then

\[
P(O \mid do(A)) = P(O \mid A),
\]

and CDT and EDT agree. Randomization removes the difference between evidence and causation.

The theory is least settled in cases where the agent’s decision procedure is itself predictable, correlated with background traits, or modeled as part of the world. Newcomb’s problem, Death in Damascus, the Adversarial Offer, and the Psychopath Button all exploit this. The source correctly identifies that CDT does not specify how to compute counterfactuals, and that critics argue this leads to irrational decisions.

A reasonable operational rule, which I have developed here, is:

1. Specify a causal model, including the agent’s decision variable, relevant background variables, and outcomes.
2. Identify the action or policy as an intervention on the decision variable.
3. Compute the distribution of outcomes under that intervention.
4. Average desirability by that distribution.
5. If uncertain about the causal model, average over models using prior credences.

This gives a precise procedure, but it inherits the difficulty of causal modeling. In unfamiliar cases, the main work is not applying the CDT formula; it is deciding what the true causal dependencies are.

---

## Conclusion

Causal decision theory says that rational action should be judged by what it causes, not by what it merely indicates. Formally, it evaluates an action \(a\) by

\[
U_C(a)=\sum_j P(a \,\Box\!\rightarrow\, O_j)D(O_j),
\]

or, in interventionist notation,

\[
U_C(a)=\sum_j P(O_j \mid do(a))D(O_j).
\]

This distinguishes it from evidential decision theory, which uses ordinary conditional probabilities. In simple cases the two agree. In predictor problems, twin prisoner’s dilemmas, and cases involving self-knowledge, they can diverge sharply.

The reference article presents CDT as philosophically attractive but incomplete: it relies on counterfactual probabilities without giving a full algorithm for computing them. Lewis’s imaging is one response, but it raises regress problems. A more operational approach uses structural causal models and interventions. That approach makes CDT applicable to concrete decision problems and policies, but it also makes explicit that CDT depends on substantive assumptions about causal structure. The central challenge of CDT is therefore not merely formal; it is determining which dependencies in the world are genuinely causal.

---

## References

Gibbard, Allan, and William L. Harper. 1981. “Counterfactuals and Two Kinds of Expected Utility.” In *Ifs: Conditionals, Belief, Decision, Chance, and Time*, 153–90.

Lewis, David. 1976. “Probabilities of Conditionals and Conditional Probabilities.” *Philosophical Review* 85 (3): 297–315.

Lewis, David. 1981. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59 (1): 5–30.

Pearl, Judea. 2009. *Causality: Models, Reasoning, and Inference*. 2nd ed. Cambridge University Press.

Wikipedia contributors. 2026. “Causal Decision Theory.” Revision 1381555528. Wikimedia Foundation. https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528.